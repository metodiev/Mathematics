# Reference Library

The tutorials in this repository teach a subject from first principles upwards; this section is
for looking things up once you have met them. It holds the four kinds of fact a reader returns to
constantly — **symbols**, **formulas**, **identities** and **theorems** — dense enough to scan in
seconds and precise enough to trust. A reference entry states *what* is true; the tutorial it links
to explains *why*.

Each page answers a different question. The [Symbol Reference](symbols/README.md) answers "what does
that symbol mean?" and is ordered by symbol rather than by topic, so a symbol met in a paper can be
found directly. The [Formula Reference](formulas/README.md) answers "what is the formula, and when
may I use it?" — every formula is printed beside the hypotheses under which it holds, because a
formula divorced from its conditions is usually false. The [Identity Reference](identities/README.md)
answers "which identity turns this expression into that one?", and the
[Theorem Reference](theorems/README.md) answers "what exactly does this theorem require?" by pairing
each statement with the idea of its proof.

All four pages follow [MATHEMATICAL_NOTATION.md](../MATHEMATICAL_NOTATION.md): angles are in radians
unless a degree sign is written, $\ln$ always means $\log_e$, and hypotheses are stated rather than
implied. Terms are defined in [GLOSSARY.md](../GLOSSARY.md), the authoring standard is in
[CONTRIBUTING.md](../CONTRIBUTING.md), and the curriculum itself begins at [README.md](../README.md).

## 1. What Is Here

| Reference | Contains | Typical question it answers |
|---|---|---|
| [Symbols](symbols/README.md) | Three lookup tables — non-letter symbols, Latin letters, Greek letters — each row giving a symbol, its name, its meaning and a true example, plus a table of symbols with several meanings | "What does $\varnothing$ mean?" · "Which way round is $\subseteq$?" |
| [Formulas](formulas/README.md) | Nine numbered sections: arithmetic and percentages, algebra, geometry, trigonometry, sequences and series, calculus, linear algebra, probability and statistics, with a conditions column throughout | "What is the volume of a cone?" · "May I use L'Hôpital here?" |
| [Identities](identities/README.md) | Trigonometric, algebraic, exponential–logarithmic, hyperbolic and combinatorial identities, each in display math with a note on when to reach for it, and a short account of how identities are proved | "How do I write $\sin A\cos B$ as a sum?" · "What is $(a+b)^4$?" |
| [Theorems](theorems/README.md) | The central theorems of twelve fields, each with its precise hypotheses, a one-sentence idea of the proof, and a link to the tutorial that proves it where that tutorial exists | "Does the mean value theorem need differentiability at the endpoints?" |

## 2. How to Use a Reference

Read the conditions before the formula. The commonest error in using a reference is to quote a
statement and drop its hypotheses: $\sqrt{x^2}=x$ needs $x\ge0$, $\ln(xy)=\ln x+\ln y$ needs
$x,y>0$, and the mean value theorem needs continuity on the closed interval but only
differentiability on the open one. A missing condition is a bug in this section, not a licence.

When an entry surprises you, follow the links. Every page points to the discipline that teaches it,
and the tutorials in [the curriculum](../README.md) supply the definitions, the derivations and the
worked examples that a reference deliberately omits.
