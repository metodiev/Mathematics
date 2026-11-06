# Theorem Reference

A theorem is only as strong as its hypotheses. The catalogue below gives, for each result, the
precise statement with every hypothesis in place, one sentence explaining why the result is true, and
a link to the tutorial in this repository that proves it where that tutorial has been written. A dash
in the last column means the proof is not yet in the repository — never that the result is optional or
obvious.

Statements are phrased so that they remain true, not so that they look tidy. Where a theorem is
commonly misquoted, the misquotation is excluded explicitly: the mean value theorem is stated with
continuity on the closed interval and differentiability only on the open one; L'Hôpital's rule
demands the indeterminate form; the central limit theorem demands finite variance. If a statement
here disagrees with a tutorial, the tutorial's proof is the arbiter — and a discrepancy is a bug worth
reporting.

The "Idea" column is a sketch, not a proof: it names the mechanism (completeness, counting,
contraction, diagonalisation) that a full proof exploits. Follow the tutorial link for the argument in
full. Notation follows [MATHEMATICAL_NOTATION.md](../../MATHEMATICAL_NOTATION.md).

## 1. The Catalogue at a Glance

| Field | Theorems | Section |
|---|---|---|
| Number theory | 7 | [§2](#2-number-theory) |
| Algebra | 6 | [§3](#3-algebra) |
| Linear algebra | 6 | [§4](#4-linear-algebra) |
| Calculus | 7 | [§5](#5-calculus) |
| Real analysis | 7 | [§6](#6-real-analysis) |
| Complex analysis | 7 | [§7](#7-complex-analysis) |
| Topology | 7 | [§8](#8-topology) |
| Probability | 7 | [§9](#9-probability) |
| Combinatorics | 7 | [§10](#10-combinatorics) |
| Graph theory | 8 | [§11](#11-graph-theory) |
| Logic | 7 | [§12](#12-logic) |
| Differential equations | 7 | [§13](#13-differential-equations) |

Eighty-three theorems in total, each with its hypotheses and the idea of its proof.

## 2. Number Theory

Full treatment: [Number Theory](../../12-number-theory/README.md).

| Theorem | Statement and hypotheses | Idea of the proof | Proved in |
|---|---|---|---|
| Division algorithm | For $a\in\mathbb{Z}$ and $b\in\mathbb{N}$ with $b\ge1$ there exist unique $q,r\in\mathbb{Z}$ with $a=qb+r$ and $0\le r<b$. | Take the largest multiple of $b$ not exceeding $a$ (well-ordering); two such representations differ by a multiple of $b$ whose absolute value is less than $b$, hence zero. | [Natural Numbers](../../01-arithmetic/01-natural-numbers/README.md) |
| Bézout's identity | For $a,b\in\mathbb{Z}$ not both zero there exist $x,y\in\mathbb{Z}$ with $ax+by=\gcd(a,b)$; moreover $\gcd(a,b)$ is the least positive integer of the form $ax+by$. | The integer combinations of $a$ and $b$ are closed under subtraction, so the least positive one divides both $a$ and $b$ and is therefore the gcd. | [Natural Numbers](../../01-arithmetic/01-natural-numbers/README.md) |
| Euclid's lemma | If $p$ is prime and $p\mid ab$ with $a,b\in\mathbb{Z}$, then $p\mid a$ or $p\mid b$. | If $p\nmid a$ then $\gcd(p,a)=1$, so Bézout gives $1=px+ay$; multiplying by $b$ exhibits $b$ as a combination of multiples of $p$ and of $ab$. | [Natural Numbers](../../01-arithmetic/01-natural-numbers/README.md) |
| Fundamental theorem of arithmetic | Every integer $n\ge2$ is a product of primes, and the factorisation is unique up to the order of the factors. | Existence by strong induction on $n$; uniqueness by cancelling the factors one at a time with Euclid's lemma. | [Natural Numbers](../../01-arithmetic/01-natural-numbers/README.md) |
| Infinitely many primes | The set of primes is infinite. | If $p_1,\dots,p_k$ were all the primes, then $N=p_1\cdots p_k+1>1$ would have a prime divisor, and no $p_i$ could divide it, since that would force $p_i\mid1$. | [Natural Numbers](../../01-arithmetic/01-natural-numbers/README.md) |
| Fermat's little theorem | If $p$ is prime and $a\in\mathbb{Z}$ with $p\nmid a$, then $a^{p-1}\equiv1\pmod p$. Equivalently, $a^p\equiv a\pmod p$ for every $a\in\mathbb{Z}$. | Multiplication by $a$ permutes the $p-1$ nonzero residues modulo $p$, so their product is unchanged; cancel $(p-1)!$, which is invertible. | — |
| Chinese remainder theorem | If $m_1,\dots,m_k$ are pairwise coprime positive integers and $M=m_1\cdots m_k$, then for any $a_1,\dots,a_k\in\mathbb{Z}$ the system $x\equiv a_i\pmod{m_i}$ has a unique solution modulo $M$. | With $M_i=M/m_i$ and $y_i$ an inverse of $M_i$ modulo $m_i$, the sum $\sum_i a_iM_iy_i$ is a solution; two solutions differ by a multiple of every $m_i$, hence of $M$. | — |

## 3. Algebra

Full treatment: [Abstract Algebra](../../13-abstract-algebra/README.md).

| Theorem | Statement and hypotheses | Idea of the proof | Proved in |
|---|---|---|---|
| Lagrange's theorem | If $G$ is a finite group and $H\le G$, then $\lvert G\rvert=[G:H]\,\lvert H\rvert$. | The left cosets of $H$ partition $G$, and $h\mapsto gh$ is a bijection $H\to gH$, so every coset has exactly $\lvert H\rvert$ elements. | — |
| First isomorphism theorem | If $\varphi:G\to H$ is a group homomorphism, then $\ker\varphi$ is normal in $G$ and $G/\ker\varphi\cong\operatorname{im}\varphi$ via $g\ker\varphi\mapsto\varphi(g)$. | The map is well defined precisely because elements of the kernel are sent to the identity, and it is a bijective homomorphism by the homomorphism laws. | — |
| Cayley's theorem | Every group $G$ is isomorphic to a subgroup of the symmetric group $\operatorname{Sym}(G)$. | Left multiplication by $g$ is a permutation of $G$, and $g\mapsto(x\mapsto gx)$ is an injective homomorphism. | — |
| Orbit–stabiliser theorem | If a finite group $G$ acts on a set $X$ and $x\in X$, then $\lvert G\rvert=\lvert\operatorname{Orb}(x)\rvert\cdot\lvert\operatorname{Stab}(x)\rvert$; equivalently $\lvert\operatorname{Orb}(x)\rvert=[G:\operatorname{Stab}(x)]$. | The map $g\operatorname{Stab}(x)\mapsto g\cdot x$ is a bijection from the cosets of the stabiliser onto the orbit. | — |
| Eisenstein's criterion | Let $f(x)=a_nx^n+\cdots+a_0\in\mathbb{Z}[x]$ with $n\ge1$. If a prime $p$ satisfies $p\nmid a_n$, $p\mid a_i$ for every $i<n$, and $p^2\nmid a_0$, then $f$ is irreducible over $\mathbb{Q}$. | Reducing a hypothetical factorisation modulo $p$ forces both factors to have all but their leading coefficients divisible by $p$, so $p^2\mid a_0$, a contradiction. | — |
| Cauchy's theorem for groups | If $G$ is a finite group and $p$ is a prime dividing $\lvert G\rvert$, then $G$ has an element of order $p$. | Let $C_p$ act cyclically on the $p$-tuples whose product is $e$; the orbits have size $1$ or $p$, and counting the non-fixed tuples shows a non-identity tuple $(g,\dots,g)$ exists, so $g^p=e$. | — |

## 4. Linear Algebra

Full treatment: [Linear Algebra](../../08-linear-algebra/README.md).

| Theorem | Statement and hypotheses | Idea of the proof | Proved in |
|---|---|---|---|
| Rank–nullity theorem | If $V$ is finite-dimensional and $T:V\to W$ is linear, then $\dim V=\dim\ker T+\dim\operatorname{im}T$. | Extend a basis of $\ker T$ to a basis of $V$; the added vectors map to a basis of the image. | — |
| Invertible matrix theorem | For $A\in M_n(F)$ the following are equivalent: $A$ is invertible; $\det A\ne0$; $\operatorname{rank}A=n$; $\ker A=\{0\}$; the columns of $A$ are linearly independent; $0$ is not an eigenvalue; $Ax=b$ has a unique solution for every $b\in F^n$. | Every condition is a restatement of "$n$ vectors in an $n$-dimensional space are linearly independent iff they span". | [Systems of Equations](../../03-algebra/05-systems-of-equations/README.md) |
| Spectral theorem for real symmetric matrices | If $A\in M_n(\mathbb{R})$ satisfies $A^{\mathsf T}=A$, then there are an orthogonal matrix $Q$ and a real diagonal matrix $\Lambda$ with $A=Q\Lambda Q^{\mathsf T}$. In particular the eigenvalues of $A$ are real, and eigenvectors belonging to distinct eigenvalues are orthogonal. | The Rayleigh quotient $\langle Av,v\rangle/\langle v,v\rangle$ is real, so eigenvalues are real; the orthogonal complement of an eigenvector is $A$-invariant, which allows induction on $n$. | — |
| Cayley–Hamilton theorem | For $A\in M_n(F)$ with characteristic polynomial $p_A(t)=\det(tI-A)$, one has $p_A(A)=0$. | The adjugate identity $(tI-A)\operatorname{adj}(tI-A)=p_A(t)I$ holds in $M_n(F[t])$; evaluating at $t=A$ gives $0=p_A(A)$. | — |
| Determinant is multiplicative | For $A,B\in M_n(F)$, $\det(AB)=\det A\,\det B$. | Both sides give the factor by which the composite map multiplies $n$-dimensional volume; equivalently, check the identity on elementary matrices and extend by multiplicativity of row operations. | — |
| Cauchy–Schwarz inequality | In a real or complex inner product space, $\lvert\langle u,v\rangle\rvert\le\lVert u\rVert\,\lVert v\rVert$ for all $u,v$, with equality iff $u$ and $v$ are linearly dependent. | If $v\ne0$, the quadratic $\lVert u-tv\rVert^2\ge0$ in the real parameter $t$ has non-positive discriminant, which is exactly the inequality. | — |

## 5. Calculus

Full treatment: [Calculus](../../07-calculus/README.md).

| Theorem | Statement and hypotheses | Idea of the proof | Proved in |
|---|---|---|---|
| Intermediate value theorem | If $f$ is continuous on $[a,b]$ and $y$ lies strictly between $f(a)$ and $f(b)$, then there is $c\in(a,b)$ with $f(c)=y$. | Assume $f(a)<y<f(b)$ (otherwise replace $f$ by $-f$); the supremum of $\{x\in[a,b]:f(x)\le y\}$ is a crossing point, and continuity makes the value exactly $y$. | — |
| Extreme value theorem | If $f$ is continuous on the closed bounded interval $[a,b]$, then $f$ attains a maximum and a minimum on $[a,b]$. | The continuous image of a compact interval is compact, hence closed and bounded, so its supremum and infimum belong to it. | — |
| Rolle's theorem | If $f$ is continuous on $[a,b]$, differentiable on $(a,b)$, and $f(a)=f(b)$, then there is $c\in(a,b)$ with $f'(c)=0$. | The extreme value theorem produces an extremum; if it is interior, Fermat's interior-extremum condition forces the derivative to vanish, and if $f$ is constant every $c$ works. | — |
| Mean value theorem | If $f$ is continuous on $[a,b]$ and differentiable on $(a,b)$, then there is $c\in(a,b)$ with $f'(c)=\dfrac{f(b)-f(a)}{b-a}$. | Apply Rolle's theorem to $g(x)=f(x)-\dfrac{f(b)-f(a)}{b-a}(x-a)$, which vanishes at both endpoints. | — |
| Fundamental theorem of calculus | (i) If $f$ is continuous on $[a,b]$ and $F(x)=\int_a^x f(t)\,dt$, then $F$ is differentiable on $(a,b)$ with $F'=f$. (ii) If $F$ is differentiable on $[a,b]$ and $F'$ is Riemann integrable there, then $\int_a^b F'(x)\,dx=F(b)-F(a)$. | (i) The difference quotient of $F$ is an average of $f$ near $x$, which tends to $f(x)$ by continuity. (ii) Apply the mean value theorem on each subinterval of a partition and let the mesh tend to zero. | — |
| L'Hôpital's rule | Let $f,g$ be differentiable on a punctured neighbourhood of $a$, with $g(x)\ne0$ and $g'(x)\ne0$ there. If $\lim_{x\to a}f(x)=\lim_{x\to a}g(x)=0$, or if both limits are $\pm\infty$, and $\lim_{x\to a}\dfrac{f'(x)}{g'(x)}=L$ exists in $[-\infty,+\infty]$, then $\lim_{x\to a}\dfrac{f(x)}{g(x)}=L$. | Cauchy's mean value theorem writes $\dfrac{f(x)}{g(x)}=\dfrac{f'(\xi)}{g'(\xi)}$ for some $\xi$ between $a$ and $x$, and $\xi\to a$ as $x\to a$. | — |
| Taylor's theorem with Lagrange remainder | If $f$ is $n+1$ times differentiable on an open interval $I$ containing $a$ and $x$, then for some $\xi$ strictly between $a$ and $x$, $f(x)=\sum_{k=0}^{n}\dfrac{f^{(k)}(a)}{k!}(x-a)^k+\dfrac{f^{(n+1)}(\xi)}{(n+1)!}(x-a)^{n+1}$. | Apply Rolle's theorem repeatedly to the difference between $f$ and its Taylor polynomial plus a multiple of $(x-a)^{n+1}$ chosen to vanish at $x$. | — |

## 6. Real Analysis

Full treatment: [Real Analysis](../../14-real-analysis/README.md).

| Theorem | Statement and hypotheses | Idea of the proof | Proved in |
|---|---|---|---|
| Monotone convergence theorem | A monotone sequence in $\mathbb{R}$ converges iff it is bounded; if $(a_n)$ is increasing and bounded above, its limit is $\sup_n a_n$. | Completeness of $\mathbb{R}$ supplies the supremum, and the definition of supremum is exactly the $\varepsilon$-condition for convergence. | — |
| Bolzano–Weierstrass theorem | Every bounded sequence in $\mathbb{R}$ has a convergent subsequence. | Bisect an interval containing the terms, always keeping a half containing infinitely many terms; the nested intervals have a common point, which is the limit of a subsequence. | — |
| Cauchy criterion | A sequence in $\mathbb{R}$ converges iff it is Cauchy. | Convergence implies Cauchy by the triangle inequality; a Cauchy sequence is bounded, so Bolzano–Weierstrass gives a convergent subsequence, and Cauchy-ness forces the whole sequence to that limit. | — |
| Heine–Borel theorem | A subset of $\mathbb{R}$ is compact (every open cover has a finite subcover) iff it is closed and bounded. | Closed and bounded sets are sequentially compact by Bolzano–Weierstrass, and sequential compactness is equivalent to compactness in metric spaces; an unbounded set or one missing a limit point admits a cover with no finite subcover. | — |
| Uniform limit theorem | If $f_n:X\to\mathbb{R}$ are continuous and $f_n\to f$ uniformly on $X$, then $f$ is continuous. | The $\varepsilon/3$ argument: pick $n$ with $\lVert f_n-f\rVert_\infty<\varepsilon/3$, then use continuity of $f_n$ at the point. | — |
| Weierstrass M-test | If $\lvert f_n(x)\rvert\le M_n$ for all $x$ in a set $E$ and all $n$, and $\sum_n M_n$ converges, then $\sum_n f_n$ converges uniformly and absolutely on $E$. | The uniform Cauchy criterion follows from the tail bound $\sum_{n>N}M_n\to0$, which is independent of $x$. | — |
| Banach fixed point theorem | Let $(X,d)$ be a complete metric space and $T:X\to X$ a contraction: $d(Tx,Ty)\le q\,d(x,y)$ for all $x,y$ and some fixed $0\le q<1$. Then $T$ has exactly one fixed point $x^*$, and for every $x_0$ the iterates satisfy $d(x_n,x^*)\le\dfrac{q^n}{1-q}d(x_0,Tx_0)$. | Consecutive iterates shrink geometrically, so $(x_n)$ is Cauchy; its limit is fixed by continuity, and uniqueness follows from the contraction inequality. | — |

## 7. Complex Analysis

Full treatment: [Complex Analysis](../../15-complex-analysis/README.md).

| Theorem | Statement and hypotheses | Idea of the proof | Proved in |
|---|---|---|---|
| Cauchy–Riemann equations | Let $f=u+iv$ be defined on an open set containing $z_0$. If $f$ is complex differentiable at $z_0$, then $u_x,u_y,v_x,v_y$ exist at $z_0$ and $u_x=v_y$, $u_y=-v_x$ there. Conversely, if $u,v$ have continuous partial derivatives on a neighbourhood of $z_0$ and satisfy these equations at $z_0$, then $f$ is complex differentiable at $z_0$. | Compare the real-linear approximation of $f$ along the real and the imaginary direction; both must equal multiplication by the same complex number. | — |
| Cauchy's integral theorem | If $f$ is holomorphic on a simply connected domain $D$ and $\gamma$ is a closed piecewise-smooth contour in $D$, then $\oint_\gamma f(z)\,dz=0$. | Green's theorem converts the contour integral into a double integral whose integrand vanishes by the Cauchy–Riemann equations. | — |
| Cauchy's integral formula | Let $D$ be simply connected, $f$ holomorphic on $D$, $\gamma$ a positively oriented simple closed piecewise-smooth contour in $D$, and $a$ a point inside $\gamma$. Then $f(a)=\dfrac{1}{2\pi i}\oint_\gamma\dfrac{f(z)}{z-a}\,dz$, and $f^{(n)}(a)=\dfrac{n!}{2\pi i}\oint_\gamma\dfrac{f(z)}{(z-a)^{n+1}}\,dz$ for $n\ge0$. | Shrink $\gamma$ to a small circle around $a$; continuity of $f$ at $a$ makes the integral tend to $2\pi i\,f(a)$, and differentiation under the integral gives the higher derivatives. | — |
| Liouville's theorem | Every bounded entire function is constant. | Cauchy's estimate $\lvert f'(a)\rvert\le M/R$ on circles of arbitrarily large radius $R$ forces $f'(a)=0$ for every $a$. | — |
| Fundamental theorem of algebra | Every nonconstant polynomial with complex coefficients has a root in $\mathbb{C}$. | If $p$ never vanished, then $1/p$ would be entire and bounded, because $\lvert p(z)\rvert\to\infty$ as $\lvert z\rvert\to\infty$; Liouville would make $1/p$ constant, hence $p$ constant. | — |
| Maximum modulus principle | If $f$ is holomorphic and nonconstant on a domain $D$, then $\lvert f\rvert$ has no local maximum in $D$. | The mean value property expresses $f(a)$ as an average over small circles, so a maximum of $\lvert f\rvert$ forces $f$ to be constant near $a$. | — |
| Residue theorem | If $f$ is holomorphic on a simply connected domain except for isolated singularities $a_1,\dots,a_n$ lying inside a positively oriented simple closed contour $\gamma$, then $\oint_\gamma f(z)\,dz=2\pi i\sum_{k=1}^{n}\operatorname{Res}(f,a_k)$. | Integrate the Laurent expansion around each singularity term by term; every power of $z-a_k$ integrates to zero except $(z-a_k)^{-1}$. | — |

## 8. Topology

Full treatment: [Topology](../../17-topology/README.md).

| Theorem | Statement and hypotheses | Idea of the proof | Proved in |
|---|---|---|---|
| Characterisations of continuity | For $f:X\to Y$ the following are equivalent: $f$ is continuous at every point; $f^{-1}(U)$ is open for every open $U\subseteq Y$; $f^{-1}(F)$ is closed for every closed $F\subseteq Y$; $f(\overline{A})\subseteq\overline{f(A)}$ for every $A\subseteq X$. | Each condition is a rewriting of the pointwise definition with open sets in place of balls around a point. | — |
| Continuous image of a compact set | If $X$ is compact and $f:X\to Y$ is continuous, then $f(X)$ is compact. | Pull back an open cover of $f(X)$ to an open cover of $X$; a finite subcover descends to a finite subcover of $f(X)$. | — |
| Continuous image of a connected set | If $X$ is connected and $f:X\to Y$ is continuous, then $f(X)$ is connected. | A separation of $f(X)$ would pull back along $f$ to a separation of $X$. | — |
| Urysohn's lemma | If $X$ is normal and $A,B\subseteq X$ are disjoint closed sets, then there is a continuous $f:X\to[0,1]$ with $f=0$ on $A$ and $f=1$ on $B$. | Build open sets $U_q$ indexed by dyadic rationals with $A\subseteq U_q\subseteq\overline{U_q}\subseteq U_r$ whenever $q<r$, then set $f(x)=\inf\{q:x\in U_q\}$. | — |
| Tietze extension theorem | If $X$ is normal, $A\subseteq X$ is closed, and $f:A\to[a,b]$ is continuous, then $f$ extends to a continuous $F:X\to[a,b]$. | Approximate the successive defects by Urysohn functions whose sup norms shrink geometrically, and add the resulting uniformly convergent series. | — |
| Brouwer fixed point theorem | Every continuous map $f:\overline{B^n}\to\overline{B^n}$ from the closed unit ball of $\mathbb{R}^n$ to itself has a fixed point. | A fixed-point-free map would produce a retraction of the ball onto its boundary sphere, which degree theory (or the no-retraction theorem) forbids. | — |
| Baire category theorem | A nonempty complete metric space is not the union of countably many nowhere dense subsets. | Choose nested closed balls of radius $2^{-n}$ avoiding each nowhere dense set in turn; completeness supplies a point in their intersection, which lies outside every set. | — |

## 9. Probability

Full treatment: [Probability](../../10-probability/README.md).

| Theorem | Statement and hypotheses | Idea of the proof | Proved in |
|---|---|---|---|
| Law of total probability | If $\{B_i\}$ is a finite or countable partition of the sample space with $\Pr(B_i)>0$ for every $i$, then $\Pr(A)=\sum_i\Pr(A\mid B_i)\Pr(B_i)$. | $A$ is the disjoint union of the sets $A\cap B_i$, and probability is countably additive. | — |
| Bayes' theorem | If $\Pr(A)>0$ and $\Pr(B)>0$, then $\Pr(B\mid A)=\dfrac{\Pr(A\mid B)\Pr(B)}{\Pr(A)}$. | Both sides equal $\Pr(A\cap B)/\Pr(A)$ after expanding the conditional probabilities. | — |
| Markov's inequality | If $X\ge0$ almost surely and $a>0$, then $\Pr(X\ge a)\le\dfrac{\mathbb{E}[X]}{a}$. | On the event $\{X\ge a\}$ the integral of $X$ is at least $a$ times the probability of that event, and the integral over the complement is non-negative. | — |
| Chebyshev's inequality | If $\mathbb{E}[X]=\mu$ and $\operatorname{Var}(X)=\sigma^2<\infty$, then $\Pr(\lvert X-\mu\rvert\ge a)\le\dfrac{\sigma^2}{a^2}$ for every $a>0$. | Apply Markov's inequality to the non-negative random variable $(X-\mu)^2$ with threshold $a^2$. | — |
| First Borel–Cantelli lemma | If $\sum_{n\ge1}\Pr(A_n)<\infty$, then $\Pr\left(\limsup_n A_n\right)=0$. No independence is required. | Continuity from above together with the union bound: $\Pr\left(\bigcup_{n\ge N}A_n\right)\le\sum_{n\ge N}\Pr(A_n)\to0$ as $N\to\infty$. | — |
| Strong law of large numbers | If $X_1,X_2,\dots$ are independent and identically distributed with $\mathbb{E}\lvert X_1\rvert<\infty$, then $\dfrac1n\sum_{i=1}^{n}X_i\to\mathbb{E}[X_1]$ almost surely. | Truncation reduces the problem to bounded variables, for which Borel–Cantelli applied to the deviations gives almost-sure convergence; integrability controls the truncation error. | — |
| Central limit theorem | If $X_1,X_2,\dots$ are independent and identically distributed with mean $\mu$ and $0<\sigma^2<\infty$, then $\dfrac{S_n-n\mu}{\sigma\sqrt n}\xrightarrow{d}\mathcal{N}(0,1)$ as $n\to\infty$, where $S_n=\sum_{i=1}^{n}X_i$. | The characteristic function of the standardised sum expands as $\left(1-\dfrac{t^2}{2n}+o\left(\dfrac1n\right)\right)^n\to e^{-t^2/2}$, the characteristic function of the standard normal law. | — |

## 10. Combinatorics

Full treatment: [Combinatorics](../../20-combinatorics/README.md).

| Theorem | Statement and hypotheses | Idea of the proof | Proved in |
|---|---|---|---|
| Binomial theorem | For $n\in\mathbb{N}_0$ and commuting $x,y$, $(x+y)^n=\sum_{k=0}^{n}\dbinom{n}{k}x^{n-k}y^{k}$. | Each term arises by choosing $y$ from exactly $k$ of the $n$ factors, and there are $\dbinom{n}{k}$ ways to make that choice. | [Intermediate Algebra](../../03-algebra/04-intermediate-algebra/README.md) |
| Pascal's rule | $\dbinom{n}{k}=\dbinom{n-1}{k-1}+\dbinom{n-1}{k}$ for $1\le k\le n-1$. | Split the $k$-subsets of an $n$-element set into those containing a fixed element and those not containing it. | — |
| Vandermonde's identity | $\sum_{k=0}^{r}\dbinom{m}{k}\dbinom{n}{r-k}=\dbinom{m+n}{r}$ for $m,n,r\ge0$. | Count the $r$-subsets of an $(m+n)$-element set by how many elements they take from the first $m$. | — |
| Hockey-stick identity | $\sum_{i=r}^{n}\dbinom{i}{r}=\dbinom{n+1}{r+1}$ for $0\le r\le n$. | Induction on $n$ using Pascal's rule; equivalently, count the $(r+1)$-subsets of $\{1,\dots,n+1\}$ by their largest element. | — |
| Pigeonhole principle | If $n$ objects are placed in $k$ containers, then some container contains at least $\left\lceil n/k\right\rceil$ objects. | If every container held at most $\lceil n/k\rceil-1$ objects, the total would be at most $k\left(\lceil n/k\rceil-1\right)<n$. | [Mathematical Thinking](../../00-foundations/01-mathematical-thinking/README.md) |
| Inclusion–exclusion principle | For finite sets $A_1,\dots,A_n$, $\left\lvert\bigcup_{i=1}^{n}A_i\right\rvert=\sum_i\lvert A_i\rvert-\sum_{i<j}\lvert A_i\cap A_j\rvert+\cdots+(-1)^{n+1}\lvert A_1\cap\cdots\cap A_n\rvert$. | An element lying in exactly $m$ of the sets is counted $\sum_{j=1}^{m}(-1)^{j+1}\dbinom{m}{j}=1$ times. | — |
| Multinomial theorem | For $n\in\mathbb{N}_0$ and commuting $x_1,\dots,x_m$, $(x_1+\cdots+x_m)^n=\sum_{k_1+\cdots+k_m=n}\dfrac{n!}{k_1!\cdots k_m!}x_1^{k_1}\cdots x_m^{k_m}$. | Choose which $k_1$ of the $n$ factors contribute $x_1$, then which $k_2$ of the rest contribute $x_2$, and so on. | — |

## 11. Graph Theory

Full treatment: [Graph Theory](../../21-graph-theory/README.md).

| Theorem | Statement and hypotheses | Idea of the proof | Proved in |
|---|---|---|---|
| Handshake lemma | In a finite graph, $\sum_{v\in V}\deg v=2\lvert E\rvert$; consequently the number of vertices of odd degree is even. | Each edge contributes exactly $1$ to the degree of each of its two endpoints. | [Mathematical Thinking](../../00-foundations/01-mathematical-thinking/README.md) |
| Euler's formula for planar graphs | If $G$ is a connected planar graph embedded in the plane with $V$ vertices, $E$ edges and $F$ faces including the unbounded one, then $V-E+F=2$. Equivalently, every convex polyhedron satisfies $V-E+F=2$. | Build the graph one edge at a time from a spanning tree: each added edge creates exactly one new face, and the alternating count is unchanged. | [Solid Geometry](../../04-geometry/05-solid-geometry/README.md) |
| Hall's marriage theorem | A bipartite graph with parts $X$ and $Y$ has a matching saturating $X$ iff $\lvert N(S)\rvert\ge\lvert S\rvert$ for every $S\subseteq X$. | In a maximum matching, let $S$ be the set of vertices of $X$ reachable by alternating paths from the unmatched vertices of $X$; then $N(S)$ is matched into $S$ and $S$ contains an unmatched vertex, so $\lvert N(S)\rvert<\lvert S\rvert$. | — |
| König's theorem | In a bipartite graph, the maximum size of a matching equals the minimum size of a vertex cover. | From a maximum matching, the vertices reachable by alternating paths from the unmatched vertices of $X$ form a vertex cover of the same size. | — |
| Cayley's formula | The number of labelled trees on $n\ge1$ vertices is $n^{n-2}$. | Prüfer codes give a bijection between labelled trees on $n$ vertices and sequences in $\{1,\dots,n\}^{n-2}$. | — |
| Eulerian circuit criterion | A finite connected graph with at least one edge has a closed walk using every edge exactly once iff every vertex has even degree. | Necessity is degree counting; sufficiency is Hierholzer's algorithm, which splices cycles together until every edge is used. | — |
| Ramsey's theorem | For all $s,t\ge1$ there is a least integer $R(s,t)$ such that every red-blue colouring of the edges of $K_{R(s,t)}$ contains a red $K_s$ or a blue $K_t$; moreover $R(s,t)\le\dbinom{s+t-2}{s-1}$. | Induction on $s+t$: at a vertex of $K_{R(s-1,t)+R(s,t-1)}$ the pigeonhole principle gives either $R(s-1,t)$ red edges or $R(s,t-1)$ blue edges. | — |
| Max-flow min-cut theorem | In a finite network with non-negative capacities, the maximum value of an $s$–$t$ flow equals the minimum capacity of an $s$–$t$ cut. | A maximum flow admits no augmenting path; the vertices reachable from $s$ in the residual graph define a cut whose capacity equals the flow value. | — |

## 12. Logic

Full treatment: [Foundations](../../00-foundations/README.md).

| Theorem | Statement and hypotheses | Idea of the proof | Proved in |
|---|---|---|---|
| Soundness theorem | For a first-order theory $T$ and a sentence $\varphi$, $T\vdash\varphi$ implies $T\models\varphi$. | Induction on the length of the derivation: every logical axiom is valid and every rule of inference preserves truth in all models. | — |
| Gödel's completeness theorem | For a first-order theory $T$ and a sentence $\varphi$, $T\models\varphi$ implies $T\vdash\varphi$. Equivalently, every consistent set of sentences has a model. | Henkin's construction adds witnesses for existential statements and builds a term model whose elements are equivalence classes of terms. | — |
| Compactness theorem | A first-order theory $T$ has a model iff every finite subset of $T$ has a model. | A derivation uses only finitely many hypotheses, so an inconsistency of $T$ would already appear in a finite subset; the other direction is immediate. | — |
| Downward Löwenheim–Skolem theorem | If a countable first-order theory $T$ in a countable language has an infinite model, then $T$ has a countably infinite model. | Start from a countable set of elements and repeatedly add witnesses for every existential formula; the Skolem hull remains countable and is a model. | — |
| Gödel's first incompleteness theorem | Let $T$ be a consistent, recursively axiomatisable theory in the language of arithmetic that proves a sufficient fragment of arithmetic, such as Robinson's $Q$. Then $T$ is incomplete: there is a sentence $\varphi$ with $T\nvdash\varphi$ and $T\nvdash\neg\varphi$. If $T$ is $\Sigma_1$-sound, $\varphi$ can be chosen true in the standard model. | Arithmetise provability and apply the diagonal lemma to obtain a sentence asserting its own unprovability — the formal liar. | — |
| Gödel's second incompleteness theorem | Under the same hypotheses on $T$, if $T$ is consistent then $T\nvdash\operatorname{Con}(T)$, where $\operatorname{Con}(T)$ arithmetically expresses the consistency of $T$. | Formalise the proof of the first incompleteness theorem inside $T$; its only unproved hypothesis is the consistency of $T$ itself. | — |
| Cantor's theorem | For every set $X$ there is no surjection $X\to\mathcal{P}(X)$; hence $\lvert X\rvert<\lvert\mathcal{P}(X)\rvert$. | Given any $f:X\to\mathcal{P}(X)$, the diagonal set $\{x\in X:x\notin f(x)\}$ cannot belong to the image of $f$. | [Set Theory](../../00-foundations/03-set-theory/README.md) |

## 13. Differential Equations

Full treatment: [Differential Equations](../../16-differential-equations/README.md).

| Theorem | Statement and hypotheses | Idea of the proof | Proved in |
|---|---|---|---|
| Picard–Lindelöf theorem | Let $f(t,y)$ be continuous on the rectangle $R=[t_0-a,t_0+a]\times[y_0-b,y_0+b]$ and Lipschitz in $y$: $\lvert f(t,y_1)-f(t,y_2)\rvert\le L\lvert y_1-y_2\rvert$ for all points of $R$. Then $y'=f(t,y)$, $y(t_0)=y_0$ has exactly one solution on $\lvert t-t_0\rvert\le h=\min\left(a,\dfrac{b}{M}\right)$, where $M=\max_R\lvert f\rvert$. | The integral operator is a contraction on a complete space of continuous functions on that interval, so the Banach fixed point theorem supplies a unique solution. | — |
| Peano existence theorem | If $f$ is continuous on an open set containing $(t_0,y_0)$, then $y'=f(t,y)$, $y(t_0)=y_0$ has at least one solution on some interval about $t_0$. | Euler polygons are uniformly bounded and equicontinuous, so the Arzelà–Ascoli theorem gives a convergent subsequence whose limit solves the integral equation. | — |
| Grönwall's inequality | If $\varphi,\alpha,\beta$ are continuous on $[a,b]$, $\beta\ge0$, and $\varphi(t)\le\alpha(t)+\int_a^t\beta(s)\varphi(s)\,ds$ for all $t\in[a,b]$, then $\varphi(t)\le\alpha(t)+\int_a^t\alpha(s)\beta(s)\exp\left(\int_s^t\beta(r)\,dr\right)ds$. In particular, if $\alpha$ is constant, $\varphi(t)\le\alpha\exp\left(\int_a^t\beta\right)$. | Multiply by the integrating factor $\exp\left(-\int_a^t\beta\right)$ and differentiate the resulting inequality. | — |
| Solution of a first-order linear equation | If $p,q$ are continuous on an interval $I$ containing $t_0$, then $y'+p(t)y=q(t)$ with $y(t_0)=y_0$ has the unique solution $y(t)=e^{-P(t)}\left(y_0+\int_{t_0}^t e^{P(s)}q(s)\,ds\right)$, where $P(t)=\int_{t_0}^t p(s)\,ds$. | The integrating factor $e^{P}$ turns the left side into the derivative of $e^{P}y$; continuity of $p$ and $q$ gives existence and uniqueness. | — |
| Dimension of the solution space | For $y^{(n)}+a_{n-1}(t)y^{(n-1)}+\cdots+a_0(t)y=0$ with continuous coefficients on an interval $I$, the solution set is an $n$-dimensional vector space, and the initial value problem with $n$ conditions at $t_0\in I$ has exactly one solution on $I$. | Linearity makes the solution set a vector space; Picard–Lindelöf gives existence and uniqueness, and the $n$ solutions with initial data $e_1,\dots,e_n$ are independent because their Wronskian at $t_0$ is $1$. | — |
| Wronskian criterion | If $y_1,\dots,y_n$ solve such an equation on $I$, then they are linearly independent iff their Wronskian $W(t)$ is nonzero at some, equivalently at every, $t\in I$; if $W$ vanishes at one point it vanishes identically. | A zero Wronskian at $t_0$ produces a nontrivial linear combination with zero initial data, which must be the zero solution by uniqueness. | — |
| Method of characteristics | For a quasilinear first-order equation $a(x,y,u)u_x+b(x,y,u)u_y=c(x,y,u)$ with $a,b,c$ continuously differentiable, the solution through a curve of initial data is determined by the characteristic system $\dot{x}=a$, $\dot{y}=b$, $\dot{u}=c$, and exists locally where the initial curve is transverse to the characteristics. | Along the projected characteristic curves the equation reduces to the ODE $\dot{u}=c$, so the PDE becomes a system of ODEs. | — |

## 14. Reading the Catalogue

Three habits make a theorem reference reliable.

**Check every hypothesis against your situation, not against the conclusion.** The mean value theorem
does not need differentiability at the endpoints; Rolle's theorem does not need $f'$ continuous;
Heine–Borel is a statement about subsets of $\mathbb{R}$, not about arbitrary metric spaces;
L'Hôpital's rule is silent when the quotient is not indeterminate.

**Read the conclusion as the weakest thing proved.** The intermediate value theorem asserts existence
and nothing about uniqueness or about how to find $c$. Hall's theorem asserts the existence of a
matching and says nothing about its size beyond saturating $X$.

**Separate the theorem from its converse.** Pythagoras and its converse are both true. The converse of
Lagrange's theorem fails: $A_4$ has order $12$ but no subgroup of order $6$. The converse of the ratio
test fails: $\sum_n 1/n^2$ converges although the ratio of consecutive terms tends to $1$, so the test
is inconclusive rather than negative.

---

*Part of the [Reference Library](../README.md). Notation follows
[MATHEMATICAL_NOTATION.md](../../MATHEMATICAL_NOTATION.md); terms are defined in
[GLOSSARY.md](../../GLOSSARY.md); the curriculum itself begins at [README.md](../../README.md).*
