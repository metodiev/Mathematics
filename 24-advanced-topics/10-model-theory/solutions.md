# Model Theory — Solutions

> [Model Theory](README.md) · Solutions to [exercises.md](exercises.md) · 36 problems

Each solution states the strategy, then carries out every step. Section references point into
[README.md](README.md). Notation is that of the exercises.

## Beginner

**1.** **Strategy.** Translate each phrase into a quantifier over elements; the domain is always $\mathbb{N}$.

(a) $x\mid y$ is $\exists z\,(x\cdot z = y)$. (Divisibility is definable because multiplication is in the language.)

(b) "$x$ is prime" is
$$\varphi(x) := \bigl(1<x\bigr)\wedge\forall y\,\forall z\,\bigl(y\cdot z = x\to (y = 1\vee z = 1)\bigr).$$
If $x>1$ is prime, any factorisation has a factor $1$; if $x$ is composite, $x = yz$ with $1<y,z<x$ refutes the
second conjunct; and $x = 0,1$ fail the first conjunct.

(c) "$x$ is a sum of two squares" is $\exists u\,\exists v\,(u\cdot u + v\cdot v = x)$. Note that the variables
$u,v$ are bound and $x$ is free.

**2.** **Strategy.** A variable occurrence is bound if it lies in the scope of a quantifier on that variable.

(a) $y$ is free; not a sentence. (b) $x$ is free; not a sentence. (c) no free variables; a sentence. (d) $z$ is
free; not a sentence. (e) the occurrence of $y$ in $R(x,y)$ is free, because the later $\exists y$ binds only the
occurrence inside its scope; so $y$ is free and the formula is not a sentence. Part (e) is the standard warning
about shadowing.

**3.** **Strategy.** Interpret each quantifier as ranging over all integers.

(a) True: for each $x$, $y = x+1$ works. (b) False: no integer exceeds all integers (take $x = y$). (c) True:
$2x = 0$ in $\mathbb{Z}$ forces $x = 0$. (d) False: $x = 1$ is odd, so $y+y = 1$ has no integer solution.
(e) False: $2x = 1$ has no integer solution.

**4.** **Strategy.** Use a sentence that separates the two structures, then exhibit the isomorphisms directly.

(a) The density sentence $\forall x\forall y\,(x<y\to\exists z(x<z\wedge z<y))$ is true in $(\mathbb{Q},<)$ and
false in $(\mathbb{Z},<)$ (take $x = 0, y = 1$). Hence the structures are not elementarily equivalent.

(b) The identity map $h(n) = n$ satisfies $a<b \iff h(a) > h(b)$, where the symbol $<$ is interpreted in the second
structure as the opposite order. Hence $h$ is an isomorphism $(\mathbb{N},<)\to(\mathbb{N},>)$. (It is a bijection
and preserves the interpreted relation.)

(c) The map $q\mapsto -q$ is a bijection $\mathbb{Q}\to\mathbb{Q}$ with $p<q \iff -p > -q$, so it is an isomorphism
$(\mathbb{Q},<)\to(\mathbb{Q},>)$.

**5.** **Strategy.** Write each property as a sentence in the group language; torsion-freeness needs a scheme because
the exponent is unbounded.

(a) $\forall x\forall y\,(x\cdot y = y\cdot x)$.

(b) $\forall x\,(x\cdot x = e)$.

(c) $\exists x\exists y\exists z\,\bigl(x\ne y\wedge x\ne z\wedge y\ne z\wedge\forall w(w = x\vee w = y\vee w =
z)\bigr)$.

(d) For each $n\ge 1$: $\forall x\,(x^n = e\to x = e)$, where $x^n$ abbreviates the $n$-fold product. The whole
property is the set of these sentences.

**6.** **Strategy.** Compactness turns "arbitrarily large finite" into "infinite".

Suppose a single sentence $\sigma$ were true exactly in the finite structures. Then
$$T := \{\sigma\}\cup\{\lambda_n : n\ge 1\}$$
is finitely satisfiable: a finite subset involves finitely many $\lambda_n$, say up to $n\le N$, and a finite
structure with at least $N$ elements satisfies $\sigma$ by hypothesis. But a model of $T$ would be finite (it
satisfies $\sigma$) and would satisfy every $\lambda_n$, which is impossible. This contradicts compactness.

For each $n$, $\chi_n := \lambda_n\wedge\neg\lambda_{n+1}$ is a sentence satisfied exactly by the structures with
exactly $n$ elements. So each finite cardinality is definable, but finiteness as a property is not.

**7.** **Strategy.** Check each sentence against the order type $\omega$.

(a) True: $y = x+1$ works. (b) False: $\mathbb{N}$ has no greatest element. (c) False: $x = 0$ has no predecessor,
so no $y<0$ exists. (d) True: if $x$ has a predecessor, then the predecessor $y$ is unique and is the greatest element
below $x$, since for any $z<x$ we have $z\le y$ (in a linear order, $z<x$ with $z\ne y$ and $y<x$ implies $z<y$;
more directly, $y = x-1$ and any $z<x$ is at most $x-1$).

**8.** **Strategy.** A substructure must be closed under the operations and inherit the relations; elementarity is
tested by a formula with a quantifier.

*Substructure.* $\mathbb{Q}\subseteq\mathbb{R}$, and $\mathbb{Q}$ is closed under $0,1,+,-,\cdot$; the order is
inherited. So $\mathbb{Q}$ is a substructure of the ordered field $\mathbb{R}$.

*Not elementary.* The formula $\varphi := \exists x\,(x\cdot x = 1+1)$ has no free variables. In $\mathbb{R}$ it
holds, because $x = \sqrt2$ satisfies $x^2 = 2$. In $\mathbb{Q}$ it fails: if $x\in\mathbb{Q}$ and $x^2 = 2$ then
$x = p/q$ in lowest terms gives $p^2 = 2q^2$, so $2\mid p$, say $p = 2r$, whence $4r^2 = 2q^2$ and $q^2 = 2r^2$, so
$2\mid q$, contradicting coprimality. Hence $\mathcal{Q}\not\preceq\mathcal{R}$, although
$\mathbb{Q}\models\varphi$ is false and $\mathbb{R}\models\varphi$ is true.

**9.** **Strategy.** Use automorphisms: a definable set must be fixed by every automorphism of the structure.

(a) In $(\mathbb{R},0,+,<)$ the set $\{0\}$ is defined by $x = 0$ (or by $x+x = x$). The map $h(x) = 2x$ is a
bijection preserving $0$, $+$ and $<$: $h(x+y) = 2x+2y = h(x)+h(y)$ and $x<y\iff 2x<2y$. If $\{1\}$ were defined
by a formula $\varphi(x)$ without parameters, then $\mathbb{R}\models\varphi(1)$ and, by isomorphism invariance
(Lemma 7.8), $\mathbb{R}\models\varphi(h(1)) = \varphi(2)$, so $2\in\{1\}$ — contradiction. Hence $\{1\}$ is not
definable without parameters.

(b) In $(\mathbb{Z},0,1,+,-)$ the even integers are defined by $\exists y\,(y+y = x)$.

(c) In $(\mathbb{Z},0,+)$ the map $h(x) = -x$ is a group automorphism fixing $0$. If the positive integers were
defined by a parameter-free formula $\varphi(x)$, then $\varphi(1)$ holds, so by isomorphism invariance
$\varphi(h(1)) = \varphi(-1)$ holds, and $-1$ would be positive — contradiction.

**10.** **Strategy.** Isomorphism requires a structure-preserving bijection; elementary equivalence only requires
agreement on sentences.

*Isomorphic, different domains.* $(\mathbb{N},<)$ and $(\mathbb{N}\setminus\{0\},<)$ have different domains, and
$n\mapsto n-1$ is an isomorphism: it is a bijection and $a<b\iff (a-1)<(b-1)$ for $a,b\ge 1$.

*Elementarily equivalent, not isomorphic.* $(\mathbb{Q},<)$ and $(\mathbb{R},<)$ are both dense linear orders
without endpoints, hence elementarily equivalent (Theorem 7.30); they are not isomorphic because one is countable
and the other uncountable.

**11.** **Strategy.** Each axiom is inherited from the corresponding property of bijections.

*Reflexive.* The identity map is an isomorphism $\mathcal{M}\to\mathcal{M}$, so $\mathcal{M}\equiv\mathcal{M}$.

*Symmetric.* If $h:\mathcal{M}\to\mathcal{N}$ is an isomorphism then $h^{-1}:\mathcal{N}\to\mathcal{M}$ preserves
the operations and relations: for example $\bar a\in R^{\mathcal{M}} \iff h(\bar a)\in R^{\mathcal{N}}$, and
applying $h^{-1}$ gives the reverse. Since $\mathcal{M}\models\sigma \iff \mathcal{N}\models\sigma$ by Lemma 7.8,
$\mathcal{M}\equiv\mathcal{N}$ implies $\mathcal{N}\equiv\mathcal{M}$.

*Transitive.* If $h:\mathcal{M}\to\mathcal{N}$ and $k:\mathcal{N}\to\mathcal{P}$ are isomorphisms, then $k\circ h$
is an isomorphism $\mathcal{M}\to\mathcal{P}$; so $\mathcal{M}\equiv\mathcal{N}\equiv\mathcal{P}$ implies
$\mathcal{M}\equiv\mathcal{P}$ by applying Lemma 7.8 twice.

**12.** **Strategy.** Count solutions with explicit distinctness and universality clauses.

(a) "The equation $x^2 = 2$ has exactly two solutions":
$$\exists x\exists y\,\bigl(x\cdot x = 2\wedge y\cdot y = 2\wedge x\ne y\wedge\forall z(z\cdot z = 2\to (z = x\vee
z = y))\bigr).$$

(b) "Every element has a cube root": $\forall x\,\exists y\,(y\cdot y\cdot y = x)$.

(c) "There are exactly three elements": $\lambda_3\wedge\neg\lambda_4$, or explicitly
$\exists x\exists y\exists z\,(x\ne y\wedge x\ne z\wedge y\ne z\wedge\forall w(w = x\vee w = y\vee w = z))$.

## Intermediate

**13.** **Strategy.** Elementarity with zero parameters is elementary equivalence; for the counterexample use two
copies of $\mathbb{N}$ shifted by one.

*Elementary implies equivalent.* Let $\sigma$ be a sentence and $\mathcal{M}\preceq\mathcal{N}$; applying Definition
5.12 with the empty tuple of parameters gives $\mathcal{M}\models\sigma\iff\mathcal{N}\models\sigma$. Hence
$\mathcal{M}\equiv\mathcal{N}$.

*The converse fails.* Let $\mathcal{N} = (\mathbb{N},<)$ and $\mathcal{M} = (\mathbb{N}\setminus\{0\},<)$, a
substructure. The map $n\mapsto n-1$ is an isomorphism $\mathcal{M}\to\mathcal{N}$, so $\mathcal{M}\equiv\mathcal{N}$
by Exercise 11 and Lemma 7.8. But the sentence $\exists x\forall y\,(x\le y)$ ("there is a least element") is true
in $\mathcal{N}$ and false in $\mathcal{M}$. Hence $\mathcal{M}\not\preceq\mathcal{N}$.

**14.** **Strategy.** Induction on the complexity of $\varphi$, with the term case done first.

*Terms.* If $\sigma$ and $\tau$ agree on the variables of a term $t$, then $t^{\mathcal{M}}[\sigma] =
t^{\mathcal{M}}[\tau]$: induction on $t$ (variables by hypothesis, constants trivially, function symbols by the
induction hypothesis applied to the arguments).

*Atomic formulas.* $t_1 = t_2$ and $R(\bar t)$ depend only on the values of the terms, hence only on the free
variables.

*Connectives.* Immediate from the induction hypothesis.

*Quantifiers.* Suppose $\sigma$ and $\tau$ agree on the free variables of $\exists x\,\psi$. The free variables of
$\psi$ are those of $\exists x\psi$ together with possibly $x$. For each $a\in M$, the assignments
$\sigma[x\mapsto a]$ and $\tau[x\mapsto a]$ agree on the free variables of $\psi$; by induction they give the same
truth value to $\psi$, so the sets of witnesses $a$ for which $\psi$ holds coincide, and the existential truth
values agree. The universal case is dual.

**15.** **Strategy.** Add axioms excluding each characteristic and apply compactness.

Let $T' := T\cup\{\underline{p}\ne 0 : p \text{ prime}\}$. A finite subset of $T'$ involves a finite $T_0\subseteq T$
and finitely many sentences $\underline{p}\ne 0$ for $p\in F$, with $F$ a finite set of primes. By hypothesis $T$
has a model of characteristic $p_0$ for infinitely many primes $p_0$; choose $p_0\notin F$. That model satisfies $T_0$
and all $\underline{p}\ne 0$ for $p\in F$, because in characteristic $p_0$ the integer $p\cdot 1$ is nonzero whenever
$p\ne p_0$. So every finite subset of $T'$ has a model; by compactness $T'$ has a model, and that model has
characteristic $0$ since no prime is zero in it.

**16.** **Strategy.** Produce a countable model that is not isomorphic to $\mathcal{N}$.

By Theorem 7.19 and the downward Löwenheim–Skolem theorem applied to its theory, there is a countable model
$\mathcal{N}^*$ of $\operatorname{Th}(\mathcal{N})$ containing an element $c$ with $c>\bar n^{\mathcal{N}^*}$ for every
$n$. The standard copy $\{\bar n^{\mathcal{N}^*} : n\in\mathbb{N}\}$ is an initial segment isomorphic to
$\mathbb{N}$, and $c$ is outside it. If $h:\mathcal{N}^*\to\mathcal{N}$ were an isomorphism, $h(c)$ would be a natural
number exceeding every $n$, impossible. So $\mathcal{N}^*$ and $\mathcal{N}$ are two non-isomorphic countable models of
$\operatorname{Th}(\mathcal{N})$, and the theory is not $\aleph_0$-categorical.

**17.** **Strategy.** Compactness for (a); the transfer theorem for (b).

(a) Suppose $T$ axiomatises the finite fields. The finite fields $\mathbb{F}_{2^k}$ exist for every $k$, so $T$ has
models of every size $2^k$; in particular $T$ has arbitrarily large finite models. Then $T\cup\{\lambda_n : n\ge 1\}$
is finitely satisfiable (a finite subset needs a finite field of size at least $N$, and $\mathbb{F}_{2^k}$ with
$2^k\ge N$ works), so by compactness it has a model, which is an infinite field satisfying $T$ — contradiction.

(b) The class of algebraically closed fields is axiomatised by the field axioms together with the scheme in Example
7.1. For characteristic $0$: if a single sentence $\sigma$ axiomatised characteristic $0$ among fields, then $\sigma$
would hold in all algebraically closed fields of characteristic $0$; by the transfer theorem (Theorem 7.20) it would
hold in every algebraically closed field of characteristic $p$ for all but finitely many $p$. But $\sigma$ also
*defines* characteristic $0$, so it fails in every field of characteristic $p$. Contradiction.

**18.** **Strategy.** Exhibit $\mathbb{Q}$ and check elementarity via quantifier elimination.

*Explicit substructure.* $\mathbb{Q}\subseteq\mathbb{R}$ and both are dense linear orders without endpoints. By QE
for $\mathrm{DLO}$, every formula $\varphi(x_1,\dots,x_n)$ is equivalent modulo $\mathrm{DLO}$ to a quantifier-free
formula. Both structures satisfy the $\mathrm{DLO}$ axioms, and quantifier-free formulas are preserved between a
substructure and the ambient structure (Proposition 7.4). Hence for $\bar a\in\mathbb{Q}^n$,
$$\mathbb{Q}\models\varphi(\bar a)\iff\mathbb{Q}\models\psi(\bar a)\iff\mathbb{R}\models\psi(\bar a)\iff
\mathbb{R}\models\varphi(\bar a),$$
where $\psi$ is quantifier-free. So $\mathbb{Q}\preceq\mathbb{R}$.

*General argument.* The downward Löwenheim–Skolem theorem gives a countable elementary substructure directly, since
the language $\{<\}$ is countable.

**19.** **Strategy.** Apply the elimination rule of Theorem 7.28: a conjunction $\bigwedge y_i<x<z_j$ is replaced by
the conjunction of all $y_i<z_j$; empty bounds contribute nothing.

(a) $\exists x\,(x<y)$: here $R = \{y\}$ and $L = \varnothing$, so the eliminated formula is the empty conjunction,
i.e. $\top$. This is correct: no left endpoint.

(b) $\exists x\,(y_1<x\wedge x<y_2)$ eliminates to $y_1<y_2$. If $y_1<y_2$, density provides $x$ strictly between;
conversely such an $x$ gives $y_1<y_2$ by transitivity.

(c) $\exists x\,(x<y_1\wedge x<y_2)$: here $L = \varnothing$ and $R=\{y_1,y_2\}$, so the result is $\top$. Correct:
there is always an element below both $y_1$ and $y_2$ (below $\min(y_1,y_2)$), by "no left endpoint".

(d) $\exists x\,(x\ne y_1\wedge x\ne y_2)$: after Step 1 the matrix has $L=R=\varnothing$ and two inequations, and
the eliminated formula is $\top$. Correct: a dense order without endpoints is infinite, so it has an element
different from the two given ones.

**20.** **Strategy.** Use that an algebraically closed field is algebraically closed for every degree and that
nonzero polynomials have finitely many roots.

(a) $\exists x\,(x^3 = y)$ is equivalent to $\top$: for every $y$ the polynomial $T^3-y$ has a root.

(b) $\exists x\,(x^2 = y\wedge x\ne 0)$ is equivalent to $y\ne 0$: if $x^2 = y$ and $x\ne0$ then $y = x^2\ne 0$; if
$y\ne 0$ choose a square root $x$ of $y$, which is nonzero.

(c) $\exists x\,(x^2 = y\wedge x^2 = y+1)$ is equivalent to $\bot$: the two equations force $y = y+1$, i.e. $0 = 1$,
which is impossible in a field.

**21.** **Strategy.** Use quantifier elimination to classify the definable sets.

*Definability.* $\{0\}$ is defined by $x = 0$ (the constant $0$ is in the language). The graph of $z\mapsto z^2$ is
defined by $y = x\cdot x$ in the variables $(x,y)$.

*Non-definability of $\mathbb{R}$.* By QE (Theorem 7.30), every formula is equivalent to a boolean combination of
polynomial equations, so every definable subset of $\mathbb{C}$ is constructible, and in one dimension
(Corollary 7.31) it is finite or cofinite. The set $\mathbb{R}\subseteq\mathbb{C}$ is neither: it is uncountable and
its complement is also uncountable. Hence it is not definable in $\mathcal{C}$.

**22.** **Strategy.** Back-and-forth gives $\aleph_0$-categoricity; Vaught's test converts categoricity into
completeness.

*$\aleph_0$-categoricity.* Let $\mathcal{M},\mathcal{N}$ be countable models of $\mathrm{DLO}$. Enumerate
$M = \{a_0,a_1,\dots\}$ and $N = \{b_0,b_1,\dots\}$ and build a finite partial isomorphism $f_0\subseteq f_1\subseteq
\cdots$ by back-and-forth: at stage $2n$ extend the domain to $a_n$ by choosing a suitable $b$, and at stage $2n+1$
extend the range to $b_n$ by choosing a suitable $a$. "Suitable" means: the new pair realises the same cut in the
finite set already matched. This is always possible because both orders are dense and have no endpoints (if $a_n$
is above all of the current domain, choose $b$ above all of the current range; if it lies between two matched
elements, choose $b$ between their images, using density). The union of the stages is an isomorphism.

*Completeness.* $\mathrm{DLO}$ is a theory in a countable language with no finite models (any model is infinite:
given $x$ there is $y>x$, then $z$ between, and so on). By Vaught's test (Exercise 26) with $\kappa = \aleph_0$,
$\mathrm{DLO}$ is complete.

*$(\mathbb{N},<)$ is not $\aleph_0$-categorical.* By compactness (as in Theorem 7.19) the theory
$\operatorname{Th}(\mathbb{N},<)$ has a countable model with an element $c$ above every numeral; that model has an
element with infinitely many predecessors, whereas every element of $\mathbb{N}$ has finitely many. Hence it is not
isomorphic to $(\mathbb{N},<)$, and the two countable models are non-isomorphic.

**23.** **Strategy.** Show finite satisfiability, then omission by the Archimedean property.

*Finitely satisfiable.* A finite subset of $p$ is $\{x>\bar n : n\in F\}$ for a finite set $F$; choosing a rational
larger than $\max F$ satisfies it in $(\mathbb{Q},<)$.

*Omitted.* If $q\in\mathbb{Q}$ realised $p$, then $q>n$ for every natural $n$, contradicting the Archimedean
property of $\mathbb{Q}$ (given $q = a/b$ with $b>0$, we have $q<a+1$).

*Realised in $\mathbb{R}$.* Any real larger than every natural number, for instance $\sqrt2\cdot 10^{10}$ or simply
"an element" by completeness of $\mathbb{R}$: the set $\mathbb{N}$ is bounded above in $\mathbb{R}$, so it has a
least upper bound $s$, and $s+1>n$ for all $n$; so $x = s+1$ realises $p$.

## Advanced

**24.** **Strategy.** Prove by induction on formulas that truth in $\mathcal{M}_\omega$ agrees with truth in some
(hence every later) stage.

**Setup.** Let $M_\omega := \bigcup_n M_n$ and interpret each symbol as the union of its interpretations; this is
well defined because the chain is elementary, hence in particular a chain of substructures, so the interpretations
are coherent. Then every $\mathcal{M}_n$ is a substructure of $\mathcal{M}_\omega$.

**Claim.** For every $n$, every formula $\varphi(\bar x)$ and every $\bar a\in M_n^k$,
$$\mathcal{M}_n\models\varphi(\bar a)\iff\mathcal{M}_\omega\models\varphi(\bar a).$$
*Proof.* Induction on $\varphi$. Atomic and propositional cases are immediate because the interpretations agree on
$M_n$. For $\varphi = \exists x\,\psi(x,\bar a)$: if $\mathcal{M}_n\models\varphi$, a witness $b\in M_n$ gives
$\mathcal{M}_\omega\models\psi(b,\bar a)$ by induction, hence $\mathcal{M}_\omega\models\varphi$. Conversely if
$\mathcal{M}_\omega\models\varphi$, some $b\in M_\omega$ witnesses $\psi(b,\bar a)$; choose $m\ge n$ with $b\in M_m$.
By induction applied at stage $m$, $\mathcal{M}_m\models\psi(b,\bar a)$, so $\mathcal{M}_m\models\exists
x\,\psi(x,\bar a)$. Since $\mathcal{M}_n\preceq\mathcal{M}_m$, the same sentence holds in $\mathcal{M}_n$. The
universal case is dual. $\blacksquare$

Hence $\mathcal{M}_n\preceq\mathcal{M}_\omega$ for every $n$. In particular, a union of an elementary chain is an
elementary extension of each of its members, and $\mathcal{M}_\omega\equiv\mathcal{M}_n$ for all $n$.

**25.** **Strategy.** Build a Skolem hull of size $\kappa$ and verify elementarity by the Tarski–Vaught test.

**Step 1: Tarski–Vaught test.** Let $\mathcal{N}$ be a structure, $A\subseteq N$ nonempty and closed under all
functions and containing all constants, and suppose that for every formula $\psi(x,\bar y)$ and $\bar a\in A^{|\bar
y|}$, if $\mathcal{N}\models\exists x\,\psi(x,\bar a)$ then some $b\in A$ satisfies $\mathcal{N}\models\psi(b,\bar
a)$. Then $A$ is the domain of an elementary substructure.

*Proof of the test.* $A$ is the domain of a substructure $\mathcal{A}$. Show $\mathcal{A}\models\varphi(\bar a)\iff
\mathcal{N}\models\varphi(\bar a)$ for $\bar a\in A^k$ by induction on $\varphi$. Atomic formulas are absolute
because $\mathcal{A}$ is a substructure. Propositional cases are immediate. For $\exists x\,\psi(x,\bar a)$: if
$\mathcal{A}$ satisfies it, a witness $b\in A$ satisfies $\psi$ in $\mathcal{A}$, hence in $\mathcal{N}$ by
induction, so $\mathcal{N}$ satisfies the existential. Conversely, if $\mathcal{N}$ satisfies it, the hypothesis
gives $b\in A$ with $\mathcal{N}\models\psi(b,\bar a)$; by induction $\mathcal{A}\models\psi(b,\bar a)$, so
$\mathcal{A}$ satisfies the existential. Universals follow by negation. $\square$

**Step 2: the hull.** For each formula $\psi(x,\bar y)$ choose a function $f_\psi:M^{|\bar y|}\to M$ such that
$f_\psi(\bar b)$ is a witness for $\exists x\,\psi(x,\bar b)$ whenever such a witness exists (axiom of choice), and
arbitrary otherwise. Let $X_0\subseteq M$ be any subset of size $\le\kappa$ that contains all interpretations of
constants (if the language has no constants, take any singleton). Define $X_{n+1}$ to be the closure of $X_n$ under
all functions of $\mathcal{M}$ and all Skolem functions $f_\psi$. Since there are at most $\kappa$ formulas and
$|X_n|\le\kappa$, we get $|X_{n+1}|\le\kappa$. Put $A := \bigcup_n X_n$; then $|A|\le\kappa$.

**Step 3: verification.** $A$ is closed under the functions (by construction) and under witnesses (if $\mathcal{M}
\models\exists x\,\psi(x,\bar a)$ with $\bar a\in A$, then $\bar a\in X_n$ for some $n$ and $f_\psi(\bar a)\in
X_{n+1}\subseteq A$ is a witness). By the Tarski–Vaught test, $A$ is the domain of an elementary substructure
$\mathcal{A}\preceq\mathcal{M}$ of cardinality $\le\kappa$. $\blacksquare$

**26.** **Strategy.** Categoricity plus Löwenheim–Skolem forces all models of the relevant size to be isomorphic.

Let $T$ be a theory in a countable language, with no finite models, and $\kappa$-categorical for some infinite
$\kappa$. Suppose $T$ were not complete: then there is a sentence $\sigma$ with $T\nvdash\sigma$ and
$T\nvdash\neg\sigma$, so there are models $\mathcal{M}\models T\cup\{\sigma\}$ and $\mathcal{N}\models
T\cup\{\neg\sigma\}$.

*Enlarge or shrink to size $\kappa$.* Since $T$ has no finite models, $\mathcal{M}$ and $\mathcal{N}$ are infinite.
By the upward Löwenheim–Skolem theorem (applied in the countable language) each has an elementary extension of
cardinality $\kappa$; alternatively, if a model has size $>\kappa$, the downward theorem gives an elementary
substructure of size $\le\kappa$, and since it contains an infinite model we may arrange size exactly $\kappa$. So
there are models $\mathcal{M}',\mathcal{N}'$ of $T$ of cardinality $\kappa$ with $\mathcal{M}'\models\sigma$ and
$\mathcal{N}'\models\neg\sigma$.

*Contradiction.* By $\kappa$-categoricity, $\mathcal{M}'\cong\mathcal{N}'$, hence $\mathcal{M}'\equiv\mathcal{N}'$
(Lemma 7.8). But $\sigma$ is true in the first and false in the second. Contradiction. So $T$ is complete.
$\blacksquare$

**27.** **Strategy.** Write the assertion as a first-order sentence, verify it in finite fields, transfer to
algebraically closed fields by an ultraproduct, and finish with the Lefschetz principle.

**Step 1: first-order formulation.** Fix $n\ge 1$ and $d\ge 1$. A polynomial map $F = (F_1,\dots,F_n)$ with each
$F_i$ of total degree $\le d$ is determined by its coefficient tuple
$\bar c = (c_{i,\alpha})$ with $i\le n$ and $|\alpha|\le d$. The assertion
$$\sigma_{n,d} := \forall \bar c\,\Bigl(\bigl(\forall \bar x\forall \bar y\,(F_{\bar c}(\bar x) = F_{\bar
c}(\bar y)\to \bar x = \bar y)\bigr)\to\forall \bar z\exists \bar x\,(F_{\bar c}(\bar x) = \bar z)\Bigr)$$
is a first-order sentence in the language of rings.

**Step 2: finite fields.** In a finite field $K$, an injective map $K^n\to K^n$ is surjective because $K^n$ is
finite. Hence $\sigma_{n,d}$ holds in every finite field.

**Step 3: an algebraically closed ultraproduct.** Fix a prime $p$ and let $\mathcal U$ be a nonprincipal
ultrafilter on $\mathbb{N}$. Let $K_i := \mathbb{F}_{p^{\,i!}}$ and $K := \prod_{\mathcal U}K_i$. Then $K$ is a
field of characteristic $p$. For each $m$, every polynomial of degree $\le m$ over $\mathbb{F}_{p^{\,i!}}$ has a root
in $\mathbb{F}_{p^{\,i!}}$ whenever $m \mid i!$, which holds for all $i\ge m$ (since $m \mid i!$). So for each
$m$ the set of $i$ for which "every polynomial of degree $\le m$ has a root" holds is cofinite, hence in $\mathcal
U$; by Łoś's theorem $K$ satisfies the same for every $m$, i.e. $K$ is algebraically closed. Therefore
$K\models\mathrm{ACF}_p$.

**Step 4: transfer to all algebraically closed fields.** By Łoś, $K\models\sigma_{n,d}$ (each $K_i$ does). Hence
some model of $\mathrm{ACF}_p$ satisfies $\sigma_{n,d}$; since $\mathrm{ACF}_p$ is complete (Corollary 7.32), every
algebraically closed field of characteristic $p$ satisfies it.

**Step 5: characteristic $0$.** By the Lefschetz principle (Theorem 7.33), $\sigma_{n,d}$ holds in every
algebraically closed field of characteristic $0$, in particular in $\mathbb{C}$.

**Conclusion.** An injective polynomial map $\mathbb{C}^n\to\mathbb{C}^n$ is surjective. $\blacksquare$

**28.** **Strategy.** For the forward direction use the elementary diagram; the reverse is immediate.

*(⇒)* Suppose $T$ is complete and $\mathcal{M},\mathcal{N}\models T$. Then $\mathcal{M}\equiv\mathcal{N}$. Expand
the language by constants $c_n$ for each $n\in N$ and let
$$\Sigma := \operatorname{Th}(\mathcal{M})\cup\{\varphi(c_{\bar n}) : \mathcal{N}\models\varphi(\bar n),\ \varphi
\text{ a formula}\}$$
be the union of the theory of $\mathcal{M}$ and the elementary diagram of $\mathcal{N}$. Every finite subset of
$\Sigma$ involves finitely many constants $\bar n$ and finitely many formulas; since $\mathcal{M}\equiv\mathcal{N}$,
the finite type of $\bar n$ in $\mathcal{N}$ is realised in some elementary extension of $\mathcal{M}$ (by
compactness applied to the finite conjunction), so every finite subset of $\Sigma$ is satisfiable. By compactness,
$\Sigma$ has a model $\mathcal{K}$. Then $\mathcal{K}\models\operatorname{Th}(\mathcal{M})$, so $\mathcal{M}\equiv
\mathcal{K}$, and $\mathcal{N}$ embeds elementarily into $\mathcal{K}$ because $\mathcal{K}$ satisfies the elementary
diagram of $\mathcal{N}$. Hence $\mathcal{K}$ is a common elementary extension.

*(⇐)* If any two models of $T$ have a common elementary extension $\mathcal{K}$, then for models $\mathcal{M},
\mathcal{N}$ we get $\mathcal{M}\equiv\mathcal{K}\equiv\mathcal{N}$, so any two models of $T$ are elementarily
equivalent, which is exactly completeness of $T$. $\blacksquare$

**29.** **Strategy.** Completeness supplies a guarantee of provability, and recursive axiomatisation supplies an
enumeration.

Let $T$ be recursively axiomatised, with QE, and complete. Because $T$ is recursively axiomatised, the set of
consequences of $T$ is recursively enumerable: enumerate all finite sequences of symbols, check each is a proof from
the axioms (this is decidable), and output the conclusion.

Now let $\sigma$ be any sentence. Because $T$ is complete, either $T\vdash\sigma$ or $T\vdash\neg\sigma$. Run the
enumeration of theorems of $T$; eventually either $\sigma$ or $\neg\sigma$ appears. Output "yes" in the first case
and "no" in the second. This decides the theory.

*Where is QE used?* In practice QE is what makes completeness provable: for $\mathrm{DLO}$ and $\mathrm{ACF}_p$ the
proof of completeness goes through QE, and the decision procedure can be made primitive recursive by eliminating
quantifiers and evaluating the resulting quantifier-free sentence directly. The argument above shows that
completeness plus recursive axiomatisation already suffices for decidability, and QE is the standard route to
completeness. $\blacksquare$

**30.** **Strategy.** Each theorem is equivalent to "consistent implies satisfiable"; connect the two notions.

*Completeness $\Rightarrow$ compactness.* Let $T$ be finitely satisfiable. A derivation of $\bot$ from $T$ uses
finitely many hypotheses (proofs are finite), so some finite $T_0\subseteq T$ derives $\bot$; by soundness $T_0$ has
no model, contradicting finite satisfiability. Hence $T$ is consistent; by the completeness theorem $T$ has a model.

*Compactness $\Rightarrow$ completeness.* Let $T$ be consistent. Every finite subset $T_0\subseteq T$ is consistent
(otherwise a finite proof of $\bot$ from $T$ would exist), and the finite case of the completeness theorem — proved by
the Henkin construction for a finite theory, or equivalently by extending $T_0$ to a maximal consistent Henkin set —
gives a model of $T_0$. So every finite subset of $T$ has a model, and compactness gives a model of $T$. Hence every
consistent theory has a model, which is the completeness theorem. $\blacksquare$

**31.** **Strategy.** Extend the cofinite filter by Zorn's lemma; distinguish the identity function from all constant
functions.

**Existence.** Let $\mathcal{F}_0 := \{X\subseteq\mathbb{N} : \mathbb{N}\setminus X \text{ is finite}\}$ be the
cofinite filter. It is a proper filter: it contains $\mathbb{N}$, is closed under finite intersections (finite unions
of finite sets are finite) and upward closed, and $\varnothing\notin\mathcal{F}_0$. Order the proper filters
containing $\mathcal{F}_0$ by inclusion; the union of a chain of proper filters is a proper filter (a finite
intersection of elements from the union lies in one member), so Zorn's lemma gives a maximal one, $\mathcal U$. A
maximal proper filter is an ultrafilter: if $X\notin\mathcal U$, then $\{Y : Y\supseteq X\cap Z,\ Z\in\mathcal U\}$
is a proper filter strictly containing $\mathcal U$ unless $X\cap Z = \varnothing$ for some $Z$, in which case
$\mathbb{N}\setminus X\supseteq Z\in\mathcal U$. Finally $\mathcal U$ is non-principal because it contains the
cofinite filter, and no finite set is cofinite.

**The diagonal is not surjective.** Let $f:\mathbb{N}\to\mathbb{N}$ be the identity, $f(n) = n$, and let
$c_k$ be the constant function with value $k$. For each $k$,
$$\{n : f(n) = c_k(n)\} = \{k\},$$
a finite set, which is not in the non-principal ultrafilter $\mathcal U$. So $[f]\ne[c_k]$ for every $k$, while the
diagonal image consists exactly of the classes $[c_k]$. Hence the embedding is not surjective. $\blacksquare$

## Challenge

**32.** **Strategy.** One direction is compactness (Theorem 7.20); the other is an ultraproduct of fields of
characteristic $p$, using Łoś and completeness of $\mathrm{ACF}_0$.

Let $\sigma$ be a sentence in the language of rings.

*(1) $\Rightarrow$ (3).* Suppose $\sigma$ holds in every algebraically closed field of characteristic $0$, i.e.
$\mathrm{ACF}_0\models\sigma$ where $\mathrm{ACF}_0 = \mathrm{ACF}\cup\{\underline{p}\ne 0 : p \text{ prime}\}$. By
Corollary 7.16 there is a finite subset
$$\mathrm{ACF}^{(0)}\cup\{\underline{p}\ne 0 : p\in F\}\models\sigma$$
with $\mathrm{ACF}^{(0)}\subseteq \mathrm{ACF}$ finite and $F$ a finite set of primes. Every algebraically closed
field of characteristic $p\notin F$ satisfies $\mathrm{ACF}^{(0)}$ and $\underline{q}\ne 0$ for all $q\in F$, hence
satisfies $\sigma$. So $\sigma$ holds in all characteristics outside the finite set $F$.

*(3) $\Rightarrow$ (2).* Suppose $\sigma$ holds in every algebraically closed field of characteristic $p$ for all
$p\notin F$. Let $P$ be the cofinite set of primes outside $F$, and let $\mathcal U$ be a non-principal ultrafilter on
$P$ (it exists because $P$ is infinite; extend the cofinite filter on $P$). Let $K := \prod_{\mathcal U}
\overline{\mathbb{F}_p}$. By Łoś's theorem $K$ is a field; it is algebraically closed because each factor satisfies
each instance of the algebraic-closure scheme, so the set of indices where that instance holds is all of $P\in\mathcal
U$. It has characteristic $0$: for each prime $q$, the set $\{p\in P : p\ne q\}$ is cofinite in $P$, hence in
$\mathcal U$, so $\underline{q}\ne 0$ holds in $K$. Finally $K\models\sigma$ because $\sigma$ holds at every factor.
So some algebraically closed field of characteristic $0$ satisfies $\sigma$.

*(2) $\Rightarrow$ (1).* If some algebraically closed field of characteristic $0$ satisfies $\sigma$, then by
completeness of $\mathrm{ACF}_0$ (Corollary 7.32) every such field does. $\blacksquare$

**33.** **Strategy.** A recursively axiomatisable complete theory extending $Q$ would contradict incompleteness.

*The argument.* Suppose $\operatorname{Th}(\mathcal{N})$ were recursively axiomatisable, say as the set of
consequences of a recursive set $T$ of sentences. Then:

1. $T$ is consistent, because $\mathcal{N}\models T$ (every axiom is true in $\mathcal{N}$).
2. $T$ contains $Q$: every axiom of $Q$ is true in $\mathcal{N}$, hence belongs to $\operatorname{Th}(\mathcal{N})$,
   hence is a consequence of $T$ — so $T$ proves all axioms of $Q$.
3. $T$ is complete: for every sentence $\sigma$, either $\mathcal{N}\models\sigma$ or
   $\mathcal{N}\models\neg\sigma$; in the first case $\sigma\in\operatorname{Th}(\mathcal{N})$ and $\sigma$ is a
   consequence of $T$, in the second $\neg\sigma$ is.

But Gödel's first incompleteness theorem says that no consistent recursively axiomatisable theory extending $Q$ is
complete. Contradiction. Hence $\operatorname{Th}(\mathcal{N})$ is not recursively axiomatisable.

*Consistency with the completeness theorem.* The completeness theorem says: for any set $T$ of sentences and any
$\sigma$, $T\models\sigma$ implies $T\vdash\sigma$. It does not assert that $T$ is recursive, nor that $T$ decides
every sentence. $\operatorname{Th}(\mathcal{N})$ is a perfectly good theory — a set of sentences — and it is
complete and has a model; what fails is that it cannot be *listed by an algorithm*. The completeness theorem still
applies to it: every semantic consequence of $\operatorname{Th}(\mathcal{N})$ is provable from it (trivially, since
it is deductively closed). What incompleteness forbids is an effective description, not a set. $\blacksquare$

**34.** **Strategy.** Build the isomorphism in countably many stages, alternating between extending the domain and
the range.

Let $\mathcal{M},\mathcal{N}$ be countable dense linear orders without endpoints, with enumerations $M =
\{a_0,a_1,\dots\}$ and $N = \{b_0,b_1,\dots\}$. We construct finite partial isomorphisms $f_0\subseteq f_1\subseteq
\cdots$ such that every $a_i$ eventually lies in the domain and every $b_j$ in the range.

*Stage $0$.* $f_0 := \varnothing$.

*Even stage $2n+1$: extend the domain.* If $a_n\in\operatorname{dom} f_{2n}$, set $f_{2n+1} := f_{2n}$. Otherwise let
$A := \operatorname{dom} f_{2n}$ and put
$$A^- := \{a\in A : a<a_n\}, \qquad A^+ := \{a\in A : a_n<a\}.$$
Since $A$ is finite, $A^-$ has a greatest element $\ell$ (if nonempty) and $A^+$ has a least element $r$ (if
nonempty). Choose $b\in N$ with $f(a)<b$ for all $a\in A^-$ and $b<f(a)$ for all $a\in A^+$: if both sets are
nonempty use density inside $(f(\ell), f(r))$; if $A^-$ is empty and $A^+$ nonempty use "no left endpoint" to find
$b<f(r)$; if $A^+$ is empty and $A^-$ nonempty use "no right endpoint"; if both are empty take any $b$. Set
$f_{2n+1} := f_{2n}\cup\{(a_n,b)\}$.

*Odd stage $2n+2$: extend the range.* If $b_n\in\operatorname{ran} f_{2n+1}$, set $f_{2n+2} := f_{2n+1}$. Otherwise
choose $a\in M$ realising the corresponding cut of $\operatorname{ran} f_{2n+1}$ in $M$ (same argument, using
density and the absence of endpoints in $\mathcal{M}$) and set $f_{2n+2} := f_{2n+1}\cup\{(a,b_n)\}$.

*Conclusion.* Each $f_n$ is a finite partial isomorphism (order preserving and reflecting on its finite domain), and
the sequence is increasing. Let $f := \bigcup_n f_n$. Then $f$ is a bijection $M\to N$: every $a_n$ enters the domain
at stage $2n+1$ and every $b_n$ enters the range at stage $2n+2$. It preserves and reflects the order, because each
finite stage does, and $a<a'$ for $a,a'\in M$ is decided at the stage where both have entered the domain. Hence $f$
is an isomorphism. $\blacksquare$

**35.** **Strategy.** Separate the two languages: the model's internal notion of function versus the external one.

*Statement.* If ZFC is consistent, then by the completeness theorem it has a model $\mathcal{M}$. Applying the
downward Löwenheim–Skolem theorem in the countable language of set theory gives an elementary substructure
$\mathcal{N}\preceq\mathcal{M}$ of countable cardinality. Inside $\mathcal{N}$, Cantor's theorem holds:
$$\mathcal{N}\models\text{"there is no surjection from }\omega\text{ onto }\mathcal{P}(\omega)\text{"},$$
so $\mathcal{N}$ believes that the set it calls $\mathcal{P}(\omega)^{\mathcal{N}}$ is uncountable.

*The apparent contradiction.* From outside, $\mathcal{N}$ is countable, so its version of $\mathcal{P}(\omega)$ is a
countable set and there is a bijection between it and $\omega$ in the real world.

*Resolution.* "Uncountable" is defined *relative to a model*: a set $X$ is uncountable in $\mathcal{N}$ if there is
no function $f$ *in the domain of $\mathcal{N}$* that bijects $\omega^{\mathcal{N}}$ with $X$. A countable model has
only countably many functions, so most bijections of the real world are simply not elements of $\mathcal{N}$.
Cantor's theorem is not violated: it says that no *internal* function is a surjection, which is true. The mistaken
step is to read the model's "there is no function" as the meta-mathematical "there is no function at all".

*Moral.* The Löwenheim–Skolem theorem shows that cardinality and its relatives are not absolute between a model and
the universe; this is the same phenomenon as Skolem's paradox and the reason model theorists speak of the model's
own version of set theory. $\blacksquare$

**36.** **Strategy.** Use quantifier elimination to reduce each type over a finite set to polynomial conditions, and
use that $\mathbb{C}$ is algebraically closed with infinite transcendence degree.

Let $A\subseteq\mathbb{C}$ be finite and let $p(x)$ be a finitely satisfiable set of formulas with parameters in $A$;
extend it to a complete type, which by QE (Theorem 7.30) is determined by its quantifier-free part. Let $F :=
\mathbb{Q}(A)\subseteq\mathbb{C}$ be the subfield generated by $A$; it is finitely generated, hence countable.

A quantifier-free type over $A$ specifies, for each polynomial $h(x)\in F[x]$, whether $h(x) = 0$ or $h(x)\ne 0$. Let
$S\subseteq F[x]$ be the set of polynomials that $p$ requires to vanish.

*Case 1: $S$ contains a nonzero polynomial $h$.* Then any realisation $x$ must be a root of $h$, hence algebraic over
$F$, of degree at most $\deg h$. Since $\mathbb{C}$ is algebraically closed and contains $F$, all roots of $h$ lie in
$\mathbb{C}$. Finite satisfiability of $p$ guarantees that $h$ has a root avoiding the finitely many polynomials that
$p$ requires to be nonzero: otherwise every root of $h$ would be a root of some $q_j$, i.e. $h \mid \prod_j q_j$ in
$F[x]$, and then $p$ would be inconsistent (a formal contradiction obtained from $h = 0$ and the $q_j\ne 0$). So any
such root realises $p$.

*Case 2: $S = \{0\}$, i.e. $p$ requires $x$ to be transcendental over $F$* (equivalently, $p$ contains $h(x)\ne 0$ for
every nonzero $h \in F[x]$). Finite satisfiability holds because $F[x]$ has infinitely many non-roots in
$\mathbb{C}$ (indeed $\mathbb{C}$ is infinite and a nonzero polynomial has finitely many roots). Then $\mathbb{C}$
contains elements transcendental over $F$: the transcendence degree of $\mathbb{C}$ over $\mathbb{Q}$ is infinite
(uncountable), while $F$ is finitely generated, so $\mathbb{C}\not\subseteq\overline{F}$. Any such element realises
$p$.

In both cases $p$ is realised in $\mathbb{C}$, which is therefore $\omega$-saturated.
