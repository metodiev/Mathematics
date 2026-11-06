# References and How to Cite

Part of the [Mathematics](../README.md) repository. This page explains how sources are used here:
how to tell primary from secondary material, how to check a theorem before relying on it, why a
web search is not a proof, and how to cite books and articles. It closes with the reference works
that serve as the default authorities for the repository.

The authoring standard in [CONTRIBUTING.md](../CONTRIBUTING.md) requires every theorem to state its
hypotheses and to have either a complete proof or a precise citation. This page describes what a
precise citation looks like. The books themselves are listed in
[Recommended Textbooks](textbooks.md), and free online resources are in
[External Resources](external-resources.md).

## 1. Why Sources Matter

A proof is a chain of inferences from definitions and previously established results. A citation is
a pointer to such a chain, not a substitute for it. Sources do three jobs:

- **Attribution.** They identify who first stated or proved a result, and where.
- **Verification.** They give a complete statement and proof that a reader can check.
- **Standardisation.** They fix terminology and conventions, which differ between books.

A source is useful only if a reader can find the exact statement and check that its hypotheses
apply. "The book says so somewhere" is not a citation; a theorem number, a page and an edition are.

## 2. Primary, Secondary and Tertiary Sources

| Kind | What it is | Examples | Typical use here |
|---|---|---|---|
| **Primary** | The original source of a result or a historical document | A research article, an author's own lecture notes, an original edition, an official errata list, a manuscript | Attribution, priority, history, and cases where the original formulation differs from later versions |
| **Secondary** | A work that presents, reorganises or proves results from primary sources | A textbook, monograph, survey, or edited reference work | Standard statements, complete proofs, and the usual source for a citation |
| **Tertiary** | A work that summarises or indexes other sources | An encyclopedia, wiki, forum answer, popular account, or AI-generated summary | Orientation, vocabulary, and pointers to better sources; not a proof authority |

In mathematics, the distinction is not the same as in history. For a standard theorem, a
well-edited textbook is often a better authority than the original paper: it states the result in
modern terminology, supplies a complete proof, and notes corrections. The original paper still
matters for attribution and priority, and sometimes the original statement is the one a historian
or a specialist needs.

"Secondary" does not mean unreliable, and "primary" does not mean correct. A source earns authority
by being checkable, reviewed and used, not by its category. A textbook with a complete proof and a
record of corrections is stronger evidence than an anonymous page that merely states the result.

## 3. How to Verify a Theorem Statement

Before using a theorem, write it out in full and check the following.

1. **Quantifiers.** Is it "for every" or "there exists"? Is the order of quantifiers explicit?
   A statement can fail when two quantifiers are exchanged.
2. **Hypotheses.** List every assumption: continuity, differentiability, compactness, finiteness,
   connectedness, characteristic, positivity, non-emptiness. Check each one against your situation.
3. **Definitions.** The same word can mean different things. Does "ring" require a multiplicative
   identity? Does "compact" include Hausdorff? Is "measurable" with respect to the same $\sigma$-algebra?
4. **Direction.** Many theorems are one-way implications. Check that you are not using the converse
   or the inverse without a separate argument.
5. **Edge cases.** Test the empty set, $n=0$, degenerate intervals, zero and negative values,
   characteristic $2$, non-commutative rings, and equality cases. A theorem that fails at an edge
   case needs an extra hypothesis.
6. **The proof.** Find the proof, not only the statement. Skim it to see which hypotheses are
   actually used; this often reveals why a hypothesis cannot be dropped.
7. **A second source.** Confirm the statement in an independent textbook or survey. Two sources
   that copy each other do not count as independent.
8. **A computation.** Check a special case numerically or symbolically. This can catch a
   misstatement or a missing hypothesis, but it is evidence, not proof.
9. **The citation record.** Record the author, title, edition, year, theorem or proposition number,
   and page. Check the publisher's errata if the result is central to your argument.
10. **Applicability.** Confirm that the cited theorem implies *your* statement. A theorem with
    stronger hypotheses may not apply, and a theorem about $\mathbb{R}$ may not hold in $\mathbb{C}$
    or in a general metric space.

If two sources disagree, compare their definitions and hypotheses before assuming an error. Then
check editions and errata, and consult a survey or monograph. State in your writing which version
you are using.

## 4. Why "I Found It Online" Is Not a Proof

A proof is a sequence of inferences that a reader can check from definitions and accepted results.
Finding a statement online establishes only that someone wrote it down. That is not enough, for
several reasons:

- **The source may be wrong.** Wikis, forums, lecture notes and encyclopedias contain errors,
  outdated statements and unsupported claims.
- **The page may have changed.** Online material is edited, moved or deleted; a link is not a stable
  reference unless it is archived or versioned.
- **The statement may not apply.** A correct theorem with different hypotheses does not prove your
  case. The most common citation error is omitting a hypothesis that the cited proof uses.
- **The source may be derivative.** A page that copies a textbook without a reference gives no way
  to check the proof or the attribution.
- **Generated text is not a source.** A language model can produce a fluent theorem and a
  plausible-looking citation that does not exist. Treat generated text as a lead to verify, never as
  a reference.

Citing a standard theorem is legitimate: a proof may say "by the intermediate value theorem
(Rudin 1976, Theorem 4.23)" if the hypotheses have been checked. What is not legitimate is treating
a search result, a vote count or an anonymous answer as the proof. If a result is not standard, or
if no precise citation is available, prove it in full or do not use it.

Copying a proof from a source without attribution is also a plagiarism problem. Paraphrase the
argument, cite the source, and make the dependence clear.

## 5. Citation Formats

The repository uses a compact author–year style with a full reference list. The exact punctuation
matters less than consistency and completeness: a reader should be able to find the exact edition
and the exact theorem.

### Books

> Rudin, Walter. *Principles of Mathematical Analysis*. 3rd ed. New York: McGraw-Hill, 1976.

> Dummit, David S., and Richard M. Foote. *Abstract Algebra*. 3rd ed. Hoboken, NJ: Wiley, 2004.

Elements, in order: author(s); title in italics; edition; place of publication; publisher; year.
Include the edition whenever it is not the first, because theorem and exercise numbers change.

### Articles

> Wiles, Andrew. "Modular Elliptic Curves and Fermat's Last Theorem." *Annals of Mathematics* 141,
> no. 3 (1995): 443–551.

Elements: author(s); article title in quotation marks; journal in italics; volume; issue; year;
page range. Add a DOI when one is available.

### Chapters or sections in an edited book

> Author, A. "Chapter Title." In *Book Title*, edited by B. Editor, 123–145. Place: Publisher, Year.

### Preprints

> Author, A. "Title." arXiv:YYMM.NNNNN (Year). https://arxiv.org/abs/YYMM.NNNNN

Cite the version you read, and replace the preprint with the published version when one exists.

### Websites and reference works

> Organisation or author. "Page Title." Site Name. Accessed Month Day, Year. URL.

For a wiki or a database entry, include the page title, the date accessed and, where available, a
stable identifier such as an OEIS sequence number or a Stacks Project tag.

### In-text citations

Use the shortest form that identifies the source and the exact result:

- `(Rudin 1976, Theorem 3.11)`
- `(Dummit and Foote 2004, Proposition 5.4)`
- `(Hardy and Wright 2008, Theorem 2.3)`
- `See Spivak (2008), Chapter 8, for a proof.`

For a theorem that is central to an argument, give the theorem number and, if useful, the page. A
bare author–year citation is not enough when the work contains several similarly named results.

## 6. Reference Works Used as Authority

The following works are the repository's default authorities. A tutorial may cite a more specialised
monograph, but the citation should still point to a specific, checkable statement. The list is a
baseline, not a claim that these are the only useful books.

| Area | Default authorities | Used for |
|---|---|---|
| Proof and foundations | Velleman, *How to Prove It*; Halmos, *Naive Set Theory*; Enderton, *Elements of Set Theory* | Logic of proof, sets, relations, functions, ordinals and cardinals |
| Mathematical logic | Enderton, *A Mathematical Introduction to Logic*; Mendelson, *Introduction to Mathematical Logic* | Propositional and first-order logic, completeness, compactness, incompleteness |
| Precalculus | OpenStax, *Precalculus*; Stitz and Zeager, *Precalculus* | Functions, trigonometry, sequences, analytic geometry |
| Calculus | Spivak, *Calculus*; Apostol, *Calculus, Vol. I*; Stewart, *Calculus: Early Transcendentals*; OpenStax, *Calculus* | Limits, derivatives, integrals, series, multivariable calculus |
| Real analysis | Rudin, *Principles of Mathematical Analysis*; Rudin, *Real and Complex Analysis*; Abbott, *Understanding Analysis*; Ross, *Elementary Analysis*; Apostol, *Mathematical Analysis* | Completeness, limits, continuity, differentiation, integration, measure theory |
| Linear algebra | Axler, *Linear Algebra Done Right*; Hoffman and Kunze, *Linear Algebra*; Horn and Johnson, *Matrix Analysis*; Strang, *Introduction to Linear Algebra* | Vector spaces, linear maps, determinants, canonical forms, matrix analysis |
| Abstract algebra | Dummit and Foote, *Abstract Algebra*; Artin, *Algebra*; Aluffi, *Algebra: Chapter 0* | Groups, rings, modules, fields, Galois theory |
| Geometry | Coxeter, *Introduction to Geometry*; Hartshorne, *Geometry: Euclid and Beyond*; Coxeter and Greitzer, *Geometry Revisited* | Euclidean and classical geometry, transformations, projective and non-Euclidean geometry |
| Topology | Munkres, *Topology*; Hatcher, *Algebraic Topology*; Lee, *Introduction to Topological Manifolds* | Point-set topology, surfaces, fundamental group, homology, manifolds |
| Discrete mathematics and combinatorics | Rosen, *Discrete Mathematics and Its Applications*; Graham, Knuth and Patashnik, *Concrete Mathematics*; Stanley, *Enumerative Combinatorics*; West, *Introduction to Graph Theory*; Diestel, *Graph Theory* | Counting, recurrences, generating functions, graphs, algorithms |
| Probability | Feller, *An Introduction to Probability Theory and Its Applications*; Grimmett and Stirzaker, *Probability and Random Processes*; Ross, *A First Course in Probability* | Probability spaces, conditioning, random variables, limit theorems, Markov chains |
| Statistics | Casella and Berger, *Statistical Inference*; Wasserman, *All of Statistics*; Hastie, Tibshirani and Friedman, *The Elements of Statistical Learning* | Estimation, testing, regression, statistical learning |
| Number theory | Hardy and Wright, *An Introduction to the Theory of Numbers*; Ireland and Rosen, *A Classical Introduction to Modern Number Theory*; Apostol, *Introduction to Analytic Number Theory*; Niven, Zuckerman and Montgomery, *An Introduction to the Theory of Numbers* | Divisibility, congruences, reciprocity, arithmetic functions, algebraic and analytic number theory |
| Differential equations | Arnold, *Ordinary Differential Equations*; Evans, *Partial Differential Equations*; Boyce, DiPrima and Meade, *Elementary Differential Equations and Boundary Value Problems*; Strauss, *Partial Differential Equations: An Introduction* | ODEs, dynamical systems, PDEs, boundary value problems |
| Applied mathematics | Boyd and Vandenberghe, *Convex Optimization*; Cover and Thomas, *Elements of Information Theory*; Burden, Faires and Burden, *Numerical Analysis*; Kreyszig, *Advanced Engineering Mathematics* | Optimization, information theory, numerical methods, applied methods |
| Reference and orientation | Wolfram MathWorld; ProofWiki; nLab; The Stacks Project; OEIS | Definitions, pointers, and checks; not cited as a proof authority |

> **Traceability rule.** Every nontrivial theorem in this repository should be traceable to a
> standard text. If a theorem is stated without proof, the tutorial must cite a specific theorem,
> proposition or lemma in a published source, and the hypotheses of that source must match the
> statement in the repository. A result that cannot be traced this way should be proved in full or
> removed.

## 7. A Practical Checklist

Before submitting a tutorial or an exercise solution, check:

- [ ] Every theorem has its hypotheses stated.
- [ ] Every theorem without a proof has a precise citation.
- [ ] The cited statement actually implies the theorem being used.
- [ ] Definitions match the source, especially across specialities.
- [ ] Edge cases and equality cases have been checked.
- [ ] The edition, year and theorem number are recorded.
- [ ] Online sources have an access date, and key claims are confirmed in a book or paper.
- [ ] Quoted or closely paraphrased material is attributed.
- [ ] Links resolve, and unstable links are replaced by a citation or an archived copy.

For the authoring standard that these checks support, see [CONTRIBUTING.md](../CONTRIBUTING.md).
For the topic inventory and completion status, see [ROADMAP.md](../ROADMAP.md).
