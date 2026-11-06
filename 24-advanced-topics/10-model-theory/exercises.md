# Model Theory — Exercises

> [Model Theory](README.md) · 36 problems · Beginner → Challenge · Solutions: [solutions.md](solutions.md)

Attempt every problem in writing before consulting [solutions.md](solutions.md). Problems marked *(proof)* require a
complete argument with all hypotheses stated. Section references point into [README.md](README.md).

**Notation.** $\mathcal{L}$ is a first-order signature; $\mathcal{M}\models\varphi$ means that the structure
$\mathcal{M}$ satisfies the sentence $\varphi$; $\equiv$ denotes elementary equivalence and $\cong$ isomorphism;
$\operatorname{Th}(\mathcal{M})$ is the set of sentences true in $\mathcal{M}$; $\lambda_n$ is the sentence "there are
at least $n$ elements". The language of arithmetic is $\{0,S,+,\cdot\}$ unless stated otherwise, and
$\mathcal{N} = (\mathbb{N},0,1,+,\cdot,<)$.

## Beginner

**1.** Write formulas in the language $\{0,1,+,\cdot,<\}$ that define, in $(\mathbb{N},0,1,+,\cdot,<)$: (a) the
relation "$x$ divides $y$"; (b) the set of primes; (c) the set of numbers that are sums of two squares.

**2.** For each formula, list its free variables and decide whether it is a sentence: (a) $\forall x\,(x+y = y+x)$;
(b) $\exists y\,(y\cdot y = x)$; (c) $\forall x\exists y\,(x<y)$; (d) $\exists x\,(x = x)\wedge z = z$;
(e) $\forall x\,(R(x,y)\to\exists y\,R(x,y))$.

**3.** In $\mathcal{Z} = (\mathbb{Z},0,1,+,-,<)$ determine the truth value of each sentence and justify:
(a) $\forall x\exists y\,(x<y)$; (b) $\exists y\forall x\,(x<y)$; (c) $\forall x\,(x+x = 0 \to x = 0)$;
(d) $\forall x\exists y\,(y+y = x)$; (e) $\exists x\,(x+x = 1)$.

**4.** *(proof)* (a) Show that $(\mathbb{Q},<)\not\equiv(\mathbb{Z},<)$. (b) Show that $(\mathbb{N},<)\cong
(\mathbb{N},>)$, where $>$ interprets the symbol $<$ as the opposite order. (c) Show that $(\mathbb{Q},<)$ and
$(\mathbb{Q},>)$ are isomorphic.

**5.** Write sentences in the language of groups $\{e,\cdot,{}^{-1}\}$ expressing: (a) the group is abelian;
(b) every element satisfies $x^2 = e$; (c) the group has exactly three elements; (d) the group is torsion-free
(this is a scheme — write the scheme).

**6.** *(proof)* Show that there is no sentence $\sigma$ in the empty language (or in any language) such that
$\mathcal{M}\models\sigma$ exactly when $M$ is finite. Then show that for each $n \ge 1$ there is a sentence
$\chi_n$ such that $\mathcal{M}\models\chi_n$ iff $|M| = n$.

**7.** In $(\mathbb{N},<)$ determine which of the following hold and explain the difference:
(a) $\forall x\exists y\,(x<y)$; (b) $\exists y\forall x\,(x<y)$; (c) $\forall x\exists y\,(y<x\wedge \forall
z(z<x\to z\le y))$; (d) $\forall x\,\bigl(\exists y\,(y<x)\to\exists y\,(y<x\wedge\forall z(z<x\to z\le y))\bigr)$.

**8.** *(proof)* Show that $\mathbb{Q}\subseteq\mathbb{R}$ is a substructure of the ordered field $\mathbb{R}$ but
not an elementary substructure. Give a formula that witnesses the failure.

**9.** *(proof)* (a) In $(\mathbb{R},0,+,<)$ show that $\{0\}$ is definable without parameters but $\{1\}$ is not,
by exhibiting an automorphism. (b) In $(\mathbb{Z},0,1,+,-)$ show that the set of even integers is definable.
(c) In $(\mathbb{Z},0,+)$ show that the set of positive integers is **not** definable without parameters, again by an
automorphism.

**10.** Give one example of two isomorphic structures with different domains, and one example of two elementarily
equivalent structures that are not isomorphic. Justify both.

**11.** *(proof)* Show that elementary equivalence $\equiv$ is an equivalence relation on $\mathcal{L}$-structures.

**12.** Write sentences in the language of rings expressing: (a) "the equation $x^2 = 2$ has exactly two solutions";
(b) "every element has a cube root"; (c) "there are exactly three elements".

## Intermediate

**13.** *(proof)* Let $\mathcal{M}\preceq\mathcal{N}$ be an elementary substructure. Prove that
$\mathcal{M}\equiv\mathcal{N}$. Show by example that $\mathcal{M}\subseteq\mathcal{N}$ and
$\mathcal{M}\equiv\mathcal{N}$ together do not imply $\mathcal{M}\preceq\mathcal{N}$.

**14.** *(proof)* Prove the coincidence lemma: if two assignments agree on the free variables of $\varphi$, then
they give the same truth value to $\varphi$ in $\mathcal{M}$.

**15.** *(proof)* Let $T$ be a set of sentences in the language of rings such that for infinitely many primes $p$
there is a model of $T$ of characteristic $p$. Prove, using compactness, that $T$ has a model of characteristic $0$.

**16.** *(proof)* Show that $\operatorname{Th}(\mathcal{N})$ is not $\aleph_0$-categorical, i.e. it has two countable
models that are not isomorphic.

**17.** *(proof)* Show that there is no theory $T$ whose models are exactly the finite fields. Show also that the
class of algebraically closed fields is elementary but the class of fields of characteristic $0$ is not finitely
axiomatisable.

**18.** *(proof)* Using the downward Löwenheim–Skolem theorem (or directly by Tarski–Vaught), prove that
$(\mathbb{R},<)$ has a countable elementary substructure. Describe one explicitly.

**19.** Eliminate the quantifier modulo $\mathrm{DLO}$: (a) $\exists x\,(x<y)$; (b) $\exists x\,(y_1<x\wedge
x<y_2)$; (c) $\exists x\,(x<y_1\wedge x<y_2)$; (d) $\exists x\,(x\ne y_1\wedge x\ne y_2)$.

**20.** Modulo $\mathrm{ACF}$, show that: (a) $\exists x\,(x^3 = y)$ is equivalent to $\top$; (b)
$\exists x\,(x^2 = y \wedge x\ne 0)$ is equivalent to $y\ne 0$; (c) $\exists x\,(x^2 = y \wedge x^2 = y+1)$ is
equivalent to $\bot$.

**21.** *(proof)* In $\mathcal{C} = (\mathbb{C},0,1,+,\cdot)$ show that $\{0\}$ and the graph of $z\mapsto z^2$ are
definable, and that $\mathbb{R}$ is not definable.

**22.** *(proof)* Prove that $\mathrm{DLO}$ is $\aleph_0$-categorical (by back-and-forth) and use Vaught's test
(Exercise 26) to deduce that $\mathrm{DLO}$ is complete. Show also that the theory of $(\mathbb{N},<)$ is not
$\aleph_0$-categorical.

**23.** *(proof)* In $(\mathbb{Q},<)$ show that the type $p(x) = \{x>\bar n : n\in\mathbb{N}\}$ is finitely
satisfiable but omitted, and that it is realised in $(\mathbb{R},<)$.

## Advanced

**24.** *(proof)* Prove the elementary chain theorem: if $\mathcal{M}_0\preceq\mathcal{M}_1\preceq\cdots$ is an
increasing chain of structures and $\mathcal{M}_\omega := \bigcup_n \mathcal{M}_n$ (with the union of the
interpretations), then each $\mathcal{M}_n\preceq\mathcal{M}_\omega$.

**25.** *(proof)* Give a complete proof of the downward Löwenheim–Skolem theorem: if $\mathcal{M}$ is an
$\mathcal{L}$-structure and $\kappa = \max(\aleph_0,|\mathcal{L}|)$, then $\mathcal{M}$ has an elementary
substructure of cardinality at most $\kappa$. Do not appeal to the Tarski–Vaught test without proving it.

**26.** *(proof)* Prove Vaught's test: if $T$ is a theory in a countable language with no finite models and $T$ is
$\kappa$-categorical for some infinite cardinal $\kappa$, then $T$ is complete.

**27.** *(proof)* Prove the Ax–Grothendieck theorem: if $F : \mathbb{C}^n\to\mathbb{C}^n$ is a polynomial map that is
injective, then $F$ is surjective. Use the Lefschetz principle and the finite-field case.

**28.** *(proof)* Prove that a theory $T$ is complete if and only if any two models of $T$ have a common elementary
extension.

**29.** *(proof)* Prove that if $T$ is a recursively axiomatised theory with quantifier elimination and $T$ is
complete, then $T$ is decidable.

**30.** *(proof)* Prove that the compactness theorem and the completeness theorem are equivalent: derive each from
the other.

**31.** *(proof)* Prove that a non-principal ultrafilter on $\mathbb{N}$ exists, and that the diagonal embedding
$\mathbb{N}\to\prod_{\mathcal U}\mathbb{N}$ into an ultrapower by a non-principal ultrafilter is not surjective.

## Challenge

**32.** *(proof)* Prove the Lefschetz principle in full: for a sentence $\sigma$ in the language of rings, $\sigma$
holds in every algebraically closed field of characteristic $0$ if and only if it holds in every algebraically closed
field of characteristic $p$ for all but finitely many primes $p$. You may use Łoś's theorem and the completeness of
$\mathrm{ACF}_0$.

**33.** *(proof)* Assuming Gödel's first incompleteness theorem, prove that $\operatorname{Th}(\mathcal{N})$ is not
recursively axiomatisable. Explain why this is consistent with the completeness theorem.

**34.** *(proof)* Prove by back-and-forth that any two countable dense linear orders without endpoints are
isomorphic.

**35.** *(proof)* State Skolem's paradox precisely and resolve it: if ZFC has a model, it has a countable model, yet
ZFC proves that uncountable sets exist. Explain exactly which hypothesis is being misread.

**36.** *(proof)* Prove that $\mathbb{C}$, as an algebraically closed field, is $\omega$-saturated: every type over
a finite parameter set that is finitely satisfiable is realised.
