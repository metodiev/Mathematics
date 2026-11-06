# Commutative Algebra — Exercises

> [Commutative Algebra](README.md) · 36 problems · Beginner → Challenge · Solutions: [solutions.md](solutions.md)

Every problem is a proof unless it asks for a computation. A computation is complete only when the ring, the
ideals and the theorem applied are named, and when every hypothesis has been checked. You may use anything proved
in the [tutorial](README.md); results that the tutorial only *states* — the Lasker–Noether theorem, the
Krull–Cohen–Seidenberg theorem, Noether normalisation, the principal ideal theorem, Zariski's lemma, the
properties of completion, Krull's intersection theorem — may be quoted by name, but their hypotheses must be
verified. Problems that ask you to prove one of these statements say so explicitly.

Notation follows the tutorial: $A$ is a commutative ring with $1$, $\mathfrak{a},\mathfrak{b}$ are ideals,
$\mathfrak{p},\mathfrak{q},\mathfrak{m}$ are prime, primary and maximal ideals, $S^{-1}A$ is a localisation,
$\operatorname{Spec}A$ carries the Zariski topology, and $\dim$, $\operatorname{ht}$ denote Krull dimension and
height. The reference *(§7.k)* points to the section of the tutorial that the problem exercises.

Do not open [solutions.md](solutions.md) before writing an attempt of your own.

## Beginner

**1.** *(§7.1)* (a) Prove that the intersection of any family of ideals of $A$ is an ideal. (b) Prove that the sum
of two ideals is an ideal. (c) Give ideals $I,J\subseteq k[x,y]$ such that $I\cup J$ is not an ideal, and identify
the smallest ideal containing $I\cup J$.

**2.** *(§9, Example 9.1)* Prove that $(2,x)\subseteq\mathbb{Z}[x]$ is a maximal ideal, that
$\mathbb{Z}[x]/(2,x)\cong\mathbb{F}_{2}$, and that $(2,x)$ is not principal. Deduce that $\mathbb{Z}[x]$ is
Noetherian but not a principal ideal domain.

**3.** *(§7.1)* Prove that an ideal $\mathfrak{a}\subsetneq A$ is prime if and only if $A/\mathfrak{a}$ is a domain,
and maximal if and only if $A/\mathfrak{a}$ is a field. Give an example of a prime ideal that is not maximal in
(a) $\mathbb{Z}$ and (b) $k[x,y]$, justifying both claims.

**4.** *(§7.3)* Compute $\operatorname{Spec}(\mathbb{Z}/6\mathbb{Z})$ and list all its closed subsets. Are all its
points closed? Is the space Hausdorff?

**5.** *(§7.2)* Let $S\subseteq A$ be multiplicative. Prove that $S^{-1}A=0$ if and only if $0\in S$. Give an
example with $A$ a domain, $S$ multiplicative, and $S^{-1}A=0$.

**6.** *(§7.2)* For a prime $p$, describe $\mathbb{Z}_{(p)}$ explicitly, prove it is a local ring with maximal
ideal $p\mathbb{Z}_{(p)}$, identify its residue field, and determine its group of units.

**7.** *(§7.2)* Let $(A,\mathfrak{m})$ be a local ring. Prove that $A^{\times}=A\setminus\mathfrak{m}$, i.e. that
the non-units form an ideal. Deduce that in a local ring the sum of two non-units is a non-unit.

**8.** *(§7.1)* Prove the Chinese remainder theorem in the form $\mathbb{Z}/6\mathbb{Z}\cong\mathbb{Z}/2\mathbb{Z}\times\mathbb{Z}/3\mathbb{Z}$,
and describe $\operatorname{Spec}$ of the product ring in terms of the spectra of the factors.

**9.** *(§7.3)* Let $k_{1},k_{2}$ be fields and $A=k_{1}\times k_{2}$. Prove that $A$ has exactly two prime ideals,
that both are maximal, and that $\dim A=0$. What is the Zariski topology on $\operatorname{Spec}A$?

**10.** *(§7.1)* Prove that $(0)$ is prime if and only if $A$ is a domain, and that $(0)$ is maximal if and only if
$A$ is a field. Give an example of a ring in which $(0)$ is prime but not maximal, and one in which $(0)$ is
neither.

## Intermediate

**11.** *(§7.2)* Verify the universal property of Theorem 7.4 in the concrete case $A=\mathbb{Z}$, $S=\mathbb{Z}\setminus(p)$,
and $\varphi:\mathbb{Z}\to\mathbb{F}_{p}$ the reduction map: show that $\varphi$ inverts $S$, that the induced
$\psi:\mathbb{Z}_{(p)}\to\mathbb{F}_{p}$ is reduction of fractions, and that it is the only such homomorphism.

**12.** *(§7.2)* Prove that for an ideal $I\subseteq A$ and a multiplicative set $S$,
$$
S^{-1}(A/I)\cong S^{-1}A\,/\,S^{-1}I .
$$
Say precisely which theorem makes the proof work, and where the hypothesis (if any) is used.

**13.** *(§7.2)* Prove in full that localisation is exact: if $0\to M'\xrightarrow{f}M\xrightarrow{g}M''\to0$ is
exact, then so is $0\to S^{-1}M'\to S^{-1}M\to S^{-1}M''\to0$. Pay particular attention to injectivity, and say
where the multiplicative set is used.

**14.** *(§7.2)* Prove that an $A$-module $M$ is zero if and only if $M_{\mathfrak{p}}=0$ for every prime
$\mathfrak{p}$, and if and only if $M_{\mathfrak{m}}=0$ for every maximal ideal $\mathfrak{m}$. Show by example
that the analogous statement for a single prime is false.

**15.** *(§7.4)* Write out the proof of the Hilbert basis theorem in full, including the verification that the set
$L$ of leading coefficients is an ideal and the induction that shows $I=M+(f_{1},\dots,f_{n})$.

**16.** *(§7.5)* Let $(A,\mathfrak{m})$ be a local ring with residue field $k$ and $M$ a finitely generated
$A$-module. Prove that $M=\mathfrak{m}M$ implies $M=0$, and deduce that elements $m_{1},\dots,m_{r}$ generate $M$
if and only if their images span $M/\mathfrak{m}M$ over $k$.

**17.** *(§7.3)* Let $A=k[x,y]/(xy)$. Show that $A$ is not a domain, find its minimal primes, compute $\dim A$,
and describe the localisations of $A$ at its minimal primes.

**18.** *(§7.7)* Let $A\subseteq B$ be an integral extension. Prove that if $B$ is a field then $A$ is a field. Prove
also that if $A$ is a field and $B$ is an integral *domain*, then $B$ is a field. Finally, show that the hypothesis
that $B$ is a domain cannot be dropped in the second statement, by considering $\mathbb{Q}\subseteq\mathbb{Q}\times\mathbb{Q}$.

**19.** *(§7.9)* Prove that a discrete valuation ring is a principal ideal domain with exactly one non-zero prime
ideal. Then show that $\mathbb{Z}$ is a principal ideal domain that is not a discrete valuation ring.

**20.** *(§7.8, §7.9)* Let $A=k[x,y]/(y^{2}-x^{3})$. Show that $A$ is a domain of dimension $1$, that it is not
integrally closed, and hence that it is not a Dedekind domain. Identify its integral closure.

## Advanced

**21.** *(§7.4)* Prove that if $A$ is Noetherian then $A[x]$ is Noetherian, and deduce that every finitely
generated $A$-algebra is Noetherian. Then prove that the subring $k[x,xy,xy^{2},\dots]\subseteq k[x,y]$ is *not*
Noetherian, and explain why this does not contradict the first part.

**22.** *(§7.5)* Prove that for $x\in A$ the following are equivalent: (i) $x\in\operatorname{Jac}(A)$; (ii) $1-xy$
is a unit for every $y\in A$. Then prove Nakayama's lemma in full, including the choice of a minimal generating
set, and deduce that a finitely generated module over a local ring is zero if its fibre is zero.

**23.** *(§7.6)* Prove that in a principal ideal domain every non-zero proper ideal is an intersection of primary
ideals, and that the decomposition is unique up to order. Explain which part of the Lasker–Noether theorem this
verifies and which part it does not.

**24.** *(§7.7)* Prove that $\mathbb{Z}$ is integrally closed in $\mathbb{Q}$, and that $\mathbb{Z}[\sqrt5]$ is not
integrally closed in $\mathbb{Q}(\sqrt5)$. In each case identify the integral closure explicitly.

**25.** *(§7.8)* Prove that $\dim A=\sup_{\mathfrak{m}}\dim A_{\mathfrak{m}}$ and that
$\operatorname{ht}\mathfrak{p}=\dim A_{\mathfrak{p}}$ for every prime $\mathfrak{p}$. Deduce that $\dim A=0$ if and
only if every prime of $A$ is maximal.

**26.** *(§7.7)* Prove the lying-over theorem: if $A\subseteq B$ is integral and $\mathfrak{p}$ is a prime of $A$,
there is a prime $\mathfrak{q}$ of $B$ with $\mathfrak{q}\cap A=\mathfrak{p}$. State and prove the lemma about
integral extensions and fields that your proof needs.

**27.** *(§7.7)* Assuming lying over (Theorem 7.28), going up (Theorem 7.29) and incomparability (Theorem 7.30),
prove that $\dim A=\dim B$ for an integral extension $A\subseteq B$ of domains.

**28.** *(§7.9)* Using the characterisations of Theorem 7.44, prove that in a Dedekind domain every non-zero prime
ideal is maximal, and that the localisation at every non-zero prime is a discrete valuation ring. Explain why
$\mathbb{Z}[x]$ is not a Dedekind domain.

**29.** *(§7.10)* Show that $\mathbb{Z}_{p}$ is a local ring with maximal ideal $(p)$ and residue field
$\mathbb{F}_{p}$, that it is a discrete valuation ring, and that $p$ is not nilpotent. Show moreover that
$\mathbb{Z}_{p}$ is uncountable, and explain why this is compatible with it being an inverse limit of finite rings.

**30.** *(§7.10)* Prove that the completion of $k[x]_{(x)}$ with respect to $(x)$ is $k[[x]]$: construct the map,
show it is injective and surjective, and identify the image of the local ring inside the power series ring.

## Challenge

**31.** *(§7.6)* Prove the existence part of the Lasker–Noether theorem by Noetherian induction: (a) prove that
every ideal of a Noetherian ring is a finite intersection of irreducible ideals; (b) prove that every irreducible
ideal of a Noetherian ring is primary, using the ascending chain $(\mathfrak{q}:y)\subseteq(\mathfrak{q}:y^{2})\subseteq\cdots$
and the identity $\mathfrak{q}=(\mathfrak{q}+(x))\cap(\mathfrak{q}+(y^{n}))$ when the chain stabilises at $n$.

**32.** *(§7.7, §7.9)* Prove that a unique factorisation domain is integrally closed in its fraction field. Use
Gauss's lemma, and deduce that $k[x,y]$ and $\mathbb{Z}[x]$ are integrally closed.

**33.** *(§7.5)* Show that Nakayama's lemma fails without the hypothesis of finite generation: exhibit a local ring
$(A,\mathfrak{m})$ and a non-zero $A$-module $M$ with $\mathfrak{m}M=M$. Identify the exact step of the proof that
breaks down.

**34.** *(§7.7)* Prove Zariski's lemma: if $k$ is a field and $A$ is a finitely generated $k$-algebra that is a
field, then $A$ is a finite algebraic extension of $k$. Use Noether normalisation (Theorem 7.35) and the fact that
a polynomial ring in at least one variable is not a field.

**35.** *(§7.6)* Let $A$ be Noetherian. Prove that the set of zero divisors of $A$ is the union of the associated
primes of $(0)$. You may use Theorem 7.24, including the statement that the associated primes are exactly the
radicals of the components of an irredundant primary decomposition of $(0)$.

**36.** *(§7.9)* (a) Prove that a discrete valuation ring $A$ with fraction field $K$ is a maximal proper subring
of $K$: there is no ring $B$ with $A\subsetneq B\subseteq K$. (b) Show that $\mathbb{Z}$ does not have this
property, by exhibiting a chain $\mathbb{Z}\subsetneq B\subsetneq\mathbb{Q}$.

<!--END-->
