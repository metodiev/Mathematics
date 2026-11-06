#!/usr/bin/env python3
"""Validate the repository: links, fences, Mermaid labels, exercise/solution parity.

Usage:  python tools/validate_repo.py [--quiet]

Exit code 1 if any error is found, 0 otherwise. Warnings never fail the build.
"""
from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parent.parent

LINK_RE = re.compile(r"(?<!!)\[([^\]]*)\]\(\s*<?([^)>\s]+)>?(?:\s+\"[^\"]*\")?\s*\)")
FENCE_RE = re.compile(r"^(\s*)(`{3,}|~{3,})\s*([\w+-]*)")
MERMAID_BAD_LABEL_RE = re.compile(r"\b[\w]+\s*\[([^\]\"]*[(),:;/=+→][^\]\"]*)\]")
EXERCISE_RE = re.compile(r"^\*\*(\d+)\.\*\*")
SKIP_SCHEMES = ("http://", "https://", "mailto:", "tel:", "ftp://")


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.checked_links = 0
        self.files = 0

    def error(self, where: str, message: str) -> None:
        self.errors.append(f"{where}: {message}")

    def warn(self, where: str, message: str) -> None:
        self.warnings.append(f"{where}: {message}")


def md_files() -> list[Path]:
    return sorted(p for p in ROOT.rglob("*.md") if ".git" not in p.parts)


def case_sensitive_exists(path: Path) -> tuple[bool, bool]:
    """Return (exists_exactly, exists_ignoring_case)."""
    if not path.exists():
        return False, False
    parent = path.parent
    if not parent.exists():
        return False, False
    try:
        names = {p.name for p in parent.iterdir()}
    except OSError:
        return True, True
    return path.name in names, True


def check_links(path: Path, text: str, report: Report) -> None:
    lines = text.splitlines()
    in_fence = False
    for lineno, line in enumerate(lines, start=1):
        if FENCE_RE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        for match in LINK_RE.finditer(line):
            target = match.group(2).strip()
            if not target or target.startswith("#") or target.startswith(SKIP_SCHEMES):
                continue
            target = unquote(target)
            target = target.split("#", 1)[0].split("?", 1)[0]
            if not target:
                continue
            report.checked_links += 1
            if target.startswith("/"):
                resolved = ROOT / target.lstrip("/")
            else:
                resolved = (path.parent / target).resolve()
            exact, any_case = case_sensitive_exists(resolved)
            where = f"{path.relative_to(ROOT).as_posix()}:{lineno}"
            if not any_case:
                report.error(where, f"broken link -> {match.group(2)}")
            elif not exact:
                report.error(where, f"wrong letter case in link -> {match.group(2)}")
            elif resolved.is_dir() and not (resolved / "README.md").exists():
                report.warn(where, f"link points to a directory without README.md -> {match.group(2)}")


def check_fences(path: Path, text: str, report: Report) -> None:
    in_fence = False
    fence_lang = ""
    fence_start = 0
    mermaid_labels: list[tuple[int, str]] = []
    in_mermaid = False
    for lineno, line in enumerate(text.splitlines(), start=1):
        m = FENCE_RE.match(line)
        if m:
            if not in_fence:
                in_fence = True
                fence_lang = m.group(3).lower()
                fence_start = lineno
                in_mermaid = fence_lang == "mermaid"
            else:
                in_fence = False
                in_mermaid = False
            continue
        if in_mermaid:
            for bad in MERMAID_BAD_LABEL_RE.finditer(line):
                mermaid_labels.append((lineno, bad.group(1)))
    where = path.relative_to(ROOT).as_posix()
    if in_fence:
        report.error(where, f"unclosed code fence opened at line {fence_start} ({fence_lang or 'no language'})")
    for lineno, label in mermaid_labels:
        report.warn(f"{where}:{lineno}", f"Mermaid label with special characters should be quoted -> [{label}]")
    if text.count("$$") % 2 == 1:
        report.warn(where, "odd number of $$ delimiters — display math may not render")


def check_exercise_parity(report: Report) -> None:
    for exercises in sorted(ROOT.rglob("exercises.md")):
        directory = exercises.parent
        solutions = directory / "solutions.md"
        ex_numbers = {
            int(m.group(1))
            for line in exercises.read_text(encoding="utf-8", errors="replace").splitlines()
            if (m := EXERCISE_RE.match(line.strip()))
        }
        where = exercises.relative_to(ROOT).as_posix()
        if len(ex_numbers) < 30:
            report.warn(where, f"only {len(ex_numbers)} numbered exercises (standard requires >= 30)")
        if not ex_numbers:
            report.error(where, "no exercises found in the expected `**1.**` format")
            continue
        expected = set(range(1, max(ex_numbers) + 1))
        missing = sorted(expected - ex_numbers)
        if missing:
            report.warn(where, f"numbering gaps at {missing[:12]}{'…' if len(missing) > 12 else ''}")
        if not solutions.exists():
            report.error(where, "exercises.md without solutions.md")
            continue
        sol_numbers = {
            int(m.group(1))
            for line in solutions.read_text(encoding="utf-8", errors="replace").splitlines()
            if (m := EXERCISE_RE.match(line.strip()))
        }
        sol_where = solutions.relative_to(ROOT).as_posix()
        unsolved = sorted(ex_numbers - sol_numbers)
        extra = sorted(sol_numbers - ex_numbers)
        if unsolved:
            report.error(sol_where, f"no solution for exercises {unsolved[:12]}{'…' if len(unsolved) > 12 else ''}")
        if extra:
            report.warn(sol_where, f"solutions for non-existent exercises {extra[:12]}")


def check_topics(report: Report) -> None:
    for readme in sorted(ROOT.glob("[0-9][0-9]-*/*/README.md")):
        directory = readme.parent
        text = readme.read_text(encoding="utf-8", errors="replace")
        where = readme.relative_to(ROOT).as_posix()
        if "## 1. Introduction" not in text:
            report.warn(where, "missing the standard numbered sections (see CONTRIBUTING.md)")
        if not (directory / "exercises.md").exists():
            report.warn(where, "tutorial without exercises.md")
        if not (directory / "solutions.md").exists():
            report.warn(where, "tutorial without solutions.md")


def duplicated_headings(report: Report) -> None:
    seen: dict[tuple[Path, str], int] = defaultdict(int)
    for path in md_files():
        for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
            if line.startswith("## "):
                seen[(path, line.strip())] += 1
    for (path, heading), count in seen.items():
        if count > 1:
            report.warn(path.relative_to(ROOT).as_posix(), f"duplicate heading {heading!r} ({count}×)")


def main() -> int:
    report = Report()
    files = md_files()
    report.files = len(files)
    for path in files:
        text = path.read_text(encoding="utf-8", errors="replace")
        check_links(path, text, report)
        check_fences(path, text, report)
    check_exercise_parity(report)
    check_topics(report)
    duplicated_headings(report)

    print(f"Scanned {report.files} Markdown files, {report.checked_links} internal links.")
    if report.warnings:
        print(f"\n{len(report.warnings)} warning(s):")
        for w in report.warnings:
            print("  ~", w)
    if report.errors:
        print(f"\n{len(report.errors)} error(s):")
        for e in report.errors:
            print("  !", e)
        return 1
    print("\nNo errors.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
