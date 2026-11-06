# External Resources

Part of the [Mathematics](../README.md) repository. These are free, publicly accessible resources
that can support study alongside the tutorials and the books in [Recommended Textbooks](textbooks.md).
They are supplements, not authorities: a video, a forum answer or a computer calculation can suggest
what is true, but it cannot replace a proof or a careful reading of a published source.

Links point to stable home pages rather than individual pages, because deep links move and disappear.
If a link no longer works, search for the resource by name. The repository's policy on sources and
citation is in [References and How to Cite](references.md).

## Choosing a Resource

| Need | Useful starting points |
|---|---|
| A structured course with exercises | OpenStax, MIT OpenCourseWare, LibreTexts |
| Practice and immediate feedback | Khan Academy, Paul's Online Math Notes, Art of Problem Solving |
| A proof of a standard theorem | ProofWiki, then a textbook from [Recommended Textbooks](textbooks.md) |
| Current research or a survey | arXiv, MathOverflow, nLab |
| A precise algebraic-geometry statement | The Stacks Project |
| Numerical or symbolic computation | SageMath, SymPy, NumPy, SciPy |
| Graphs and networks | NetworkX |
| Visual exploration | Desmos, GeoGebra |
| Identifying an integer sequence | OEIS |
| A quick definition or formula | Wolfram MathWorld, with caution |
| Asking a specific question | Mathematics Stack Exchange, MathOverflow |

## General Course Materials and Textbooks

| Resource | What it is | Good for | Limitations |
|---|---|---|---|
| [OpenStax](https://openstax.org) | A publisher of free, peer-reviewed university textbooks in mathematics, science and other subjects. | Standard lower-division courses, especially precalculus, calculus, algebra and statistics; the books include exercises and are openly licensed. | Coverage is strongest at the lower-division level; most titles are not proof-based; some advanced topics are absent, and the sequence follows US course conventions. |
| [MIT OpenCourseWare](https://ocw.mit.edu) | An archive of course materials from MIT, including lecture notes, problem sets, exams, syllabi and some video lectures. | Seeing how a full course is organised, finding additional problems, and following a topic through a coherent sequence of lectures. | Materials vary by course and instructor; solutions are not always available; courses assume different prerequisites, and the archive is not a single curriculum. |
| [Khan Academy](https://www.khanacademy.org) | Free lessons, worked examples and adaptive practice across school and early university mathematics. | Building fluency in arithmetic, algebra, trigonometry and early calculus, with immediate feedback and short explanations. | The emphasis is procedural; proofs and abstract arguments are limited; the sequence follows US school standards and does not reach honours or graduate material. |
| [Paul's Online Math Notes](https://tutorial.math.lamar.edu) | Free, concise notes and worked examples for algebra, calculus and differential equations, written by Paul Dawkins. | Reviewing a technique, seeing a worked example, or finding a short explanation of a standard method. | The focus is service-course mathematics; there are few proofs, and notation and conventions are those of one author. |
| [LibreTexts Mathematics](https://math.libretexts.org) | A library of free, openly licensed textbooks, course notes and ancillary materials contributed by instructors. | Finding a free book or set of notes on a specific topic, especially for standard undergraduate courses. | Quality and depth vary by book; check the author, edition and licence; the library is a collection, not a curated curriculum. |
| [Art of Problem Solving](https://artofproblemsolving.com) | A community and resource site centred on competition mathematics, with forums, problem collections and courses. | Olympiad and contest preparation, challenging problems, and discussion of solution techniques. | Forum posts are not peer-reviewed and vary in quality; the focus is competition-style problem solving rather than a systematic course; some resources are commercial. |

## Proofs, References and Research

| Resource | What it is | Good for | Limitations |
|---|---|---|---|
| [ProofWiki](https://proofwiki.org) | A collaborative catalogue of mathematical definitions, theorems and proofs. | Locating a proof of a standard result, comparing proof strategies, and finding related definitions. | Coverage is uneven; notation and conventions vary between pages; it is not a textbook, some pages lack complete references, and a proof may depend on results stated elsewhere. Verify a key theorem against a standard text. |
| [Wolfram MathWorld](https://mathworld.wolfram.com) | An online mathematics encyclopedia with definitions, formulas, diagrams and references. | Quick orientation, a formula to check against a textbook, and pointers to further reading. | It is a reference work, not a primary authority; occasional errors and incomplete citations occur; it should not be the only source for a theorem or proof. |
| [nLab](https://ncatlab.org/nlab) | A wiki devoted to category theory, homotopy theory, algebraic geometry and mathematical physics, with an emphasis on structural connections. | Research-level definitions, statements of higher categorical results, and pointers to the literature. | It assumes substantial background; notation and conventions are idiosyncratic; page quality and completeness vary; it is not an introductory text. |
| [The Stacks Project](https://stacks.math.columbia.edu) | A large, collaborative reference for algebraic geometry and commutative algebra, organised with precise tags and dependencies. | Checking a precise statement in scheme theory or commutative algebra and following its proof to earlier results. | It is graduate-level and assumes algebra and geometry; there are no exercises or motivation for beginners; it is a reference, not a course. |
| [arXiv](https://arxiv.org) | A preprint server for mathematics, physics, computer science and related fields. | Current research, surveys, and the original version of a recent theorem. | Preprints are not peer-reviewed; versions change; quality varies, and a published version may differ. Use the published record when one exists and cite the version you read. |
| [OEIS](https://oeis.org) | The On-Line Encyclopedia of Integer Sequences, a searchable database of sequences with formulas, comments and references. | Identifying a sequence, finding a conjectured formula, and locating references to a combinatorial or number-theoretic sequence. | Entries mix proved results, conjectures and empirical observations; the database is not a proof source; cite the sequence number and the date accessed. |
| [Mathematics Stack Exchange](https://math.stackexchange.com) | A question-and-answer site for mathematics at school and university level. | Hints, alternative explanations, and identifying the name of a standard result or technique. | Answers are not vetted; a highly voted answer can still be wrong; the site is useful as a pointer, not as an authority for a proof. |
| [MathOverflow](https://mathoverflow.net) | A question-and-answer site for research-level mathematics. | Research context, references, and expert pointers to the literature. | It is not intended for standard exercises or first courses; answers can be terse or assume specialist background; it is not a citable proof source. |

## Computation and Visualisation

| Resource | What it is | Good for | Limitations |
|---|---|---|---|
| [SageMath](https://www.sagemath.org) | An open-source computer algebra system built on Python, with extensive facilities for algebra, number theory, calculus, combinatorics and plotting. | Exact symbolic and algebraic computation, experimentation with conjectures, and checking a calculation by a second method. | It is not a proof assistant; some algorithms are heuristic or have hidden assumptions; installation and learning take effort, and results must be interpreted. |
| [SymPy](https://www.sympy.org) | A Python library for symbolic mathematics. | Symbolic algebra, calculus, equation solving and scripting a calculation inside a Python workflow. | It is not a proof system; assumptions about variables matter; it can return conditional or incomplete results, and it should be checked against theory. |
| [NumPy](https://numpy.org) | A Python library for arrays and numerical computation. | Numerical linear algebra, array manipulation, and the computational foundation for scientific Python. | Floating-point arithmetic is not exact; rounding and conditioning affect results; it provides numerical evidence, not proof. |
| [SciPy](https://scipy.org) | A Python library for scientific computing, built on NumPy. | Numerical integration, optimization, interpolation, linear algebra and statistics. | Numerical methods have convergence and stability assumptions; results are approximations, and the library is not a proof tool. |
| [NetworkX](https://networkx.org) | A Python library for creating, analysing and visualising graphs and networks. | Graph algorithms, combinatorial experiments, and checking small cases of a graph-theoretic statement. | An implementation is not a proof; algorithm choices and graph representations affect results; performance is limited for very large graphs. |
| [Desmos](https://www.desmos.com) | A browser-based graphing calculator and geometry tool. | Plotting functions, exploring parameters, and building quick numerical intuition. | A graph is visual and numerical evidence, not a proof; plotting ranges and resolution can hide behaviour; it does not handle symbolic proof. |
| [GeoGebra](https://www.geogebra.org) | Interactive geometry, algebra, graphing and calculus software, available in the browser and as an application. | Dynamic geometry constructions, exploring transformations, and visualising algebraic and calculus relationships. | Numerical and visual evidence is not proof; applet quality varies; exact behaviour can depend on the construction and rounding. |

## How to Use These Resources Well

1. **Use a resource for a specific purpose.** A video is good for intuition, a problem set for
   practice, and a reference work for a definition; none of them is a complete course by itself.
2. **Check the version.** Online notes change, preprints are revised and wiki pages are edited.
   Record the date you accessed a page and the version of any preprint you read.
3. **Follow a pointer to a source.** When a forum answer or wiki page states a theorem, find the
   textbook or paper it relies on and check the hypotheses yourself.
4. **Separate computation from proof.** A symbolic result or a graph can suggest a theorem and
   catch an error, but it does not establish a statement for all cases.
5. **Do not cite a search result as authority.** "I found it online" is not a proof; see
   [References and How to Cite](references.md) for what a usable citation needs.

For books that can serve as the standard reference behind these resources, see
[Recommended Textbooks](textbooks.md). For the repository's own conventions on sources, proofs and
citation, see [References and How to Cite](references.md). For the topics these resources support,
see the [Roadmap](../ROADMAP.md).
