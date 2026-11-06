# Mathematical Notation

Every symbol used in this repository is defined where it first appears. This page is the shared
reference so that notation stays consistent across two dozen disciplines.

**Conventions used throughout**

* Variables are italic: $x$, $n$, $f$. Named constants and operators are upright: $\pi$, $e$,
  $\sin$, $\log$, $\operatorname{rank}$.
* A *definition* is written $:=$ or "we define …". An *identity* holds for all values; an *equation*
  holds for some values and is a problem to solve.
* Brackets are used only for grouping, never as a second kind of parenthesis.
* Decimal commas are not used: $3.14$, never $3,14$.

---

## 1. Logic

| Symbol | Read as | Meaning |
|---|---|---|
| $\neg P$ | not $P$ | negation |
| $P \land Q$ | $P$ and $Q$ | conjunction; true only when both are true |
| $P \lor Q$ | $P$ or $Q$ | disjunction; *inclusive* or unless stated otherwise |
| $P \oplus Q$ | $P$ xor $Q$ | exclusive or; true when exactly one is true |
| $P \Rightarrow Q$ | if $P$ then $Q$ | implication; false only when $P$ is true and $Q$ is false |
| $P \Leftrightarrow Q$ | $P$ if and only if $Q$ | logical equivalence |
| $\forall x \in S,\ P(x)$ | for all $x$ in $S$, $P(x)$ | universal quantifier |
| $\exists x \in S,\ P(x)$ | there exists $x$ in $S$ such that $P(x)$ | existential quantifier |
| $\exists! x,\ P(x)$ | there exists a unique $x$ such that $P(x)$ | existence and uniqueness |
| $\therefore$ | therefore | conclusion of an argument |
| $\because$ | because | justification |
| $\blacksquare$ / $\square$ | end of proof | end of a completed proof |
| $\vdash$ | proves | syntactic derivability (advanced logic) |
| $\models$ | models / entails | semantic consequence (advanced logic) |

Negation rules worth memorising:

$$\neg\forall x\,P(x) \equiv \exists x\,\neg P(x), \qquad \neg\exists x\,P(x) \equiv \forall x\,\neg P(x).$$

---

## 2. Sets and numbers

| Symbol | Read as | Meaning |
|---|---|---|
| $\{a, b, c\}$ | set of $a$, $b$, $c$ | explicit listing |
| $\{x \in S : P(x)\}$ | the set of $x$ in $S$ such that $P(x)$ | set-builder notation |
| $x \in A$ | $x$ is an element of $A$ | membership |
| $x \notin A$ | $x$ is not an element of $A$ | non-membership |
| $A \subseteq B$ | $A$ is a subset of $B$ | every element of $A$ is in $B$ |
| $A \subsetneq B$ | $A$ is a proper subset of $B$ | subset, not equal |
| $A \cup B$ | $A$ union $B$ | elements in either |
| $A \cap B$ | $A$ intersect $B$ | elements in both |
| $A \setminus B$ | $A$ minus $B$ | elements of $A$ not in $B$ |
| $A^{\complement}$ | complement of $A$ | relative to a fixed universe |
| $A \triangle B$ | symmetric difference | elements in exactly one |
| $A \times B$ | Cartesian product | set of ordered pairs $(a,b)$ |
| $\varnothing$ | the empty set | the set with no elements |
| $\lvert A\rvert$, $\#A$ | cardinality of $A$ | number of elements |
| $\mathcal{P}(A)$ | power set of $A$ | set of all subsets |
| $\bigcup_{i \in I} A_i$, $\bigcap_{i \in I} A_i$ | union / intersection over $I$ | indexed families |
| $\sqcup$ | disjoint union | union of pairwise disjoint sets |
| $\mathbb{N}$ | the natural numbers | $\{1,2,3,\dots\}$ — see the note below |
| $\mathbb{N}_0$ | the natural numbers with zero | $\{0,1,2,3,\dots\}$ |
| $\mathbb{Z}$ | the integers | $\{\dots,-2,-1,0,1,2,\dots\}$ |
| $\mathbb{Q}$ | the rationals | $p/q$ with $p,q \in \mathbb{Z}$, $q \ne 0$ |
| $\mathbb{R}$ | the reals | the complete ordered field |
| $\mathbb{C}$ | the complex numbers | $\{a + bi : a,b \in \mathbb{R}\}$ |
| $\mathbb{F}_p$ | the field with $p$ elements | $p$ prime |
| $[a,b]$, $(a,b)$, $[a,b)$, $(a,b]$ | closed / open intervals | whether the endpoints are included |
| $\infty$ | infinity | a limit symbol, not a number |

> **Note.** Some texts define $\mathbb{N}$ to include $0$. This repository uses
> $\mathbb{N} = \{1,2,3,\dots\}$ and writes $\mathbb{N}_0$ when zero is included. Whenever a result
> depends on the convention it is stated explicitly.

---

## 3. Arithmetic and algebra

| Symbol | Read as | Meaning |
|---|---|---|
| $a \mid b$ | $a$ divides $b$ | $b = ak$ for some integer $k$ |
| $a \nmid b$ | $a$ does not divide $b$ | negation of the above |
| $a \equiv b \pmod n$ | $a$ is congruent to $b$ mod $n$ | $n \mid (a-b)$ |
| $\gcd(a,b)$ | greatest common divisor | largest $d$ with $d \mid a$ and $d \mid b$ |
| $\operatorname{lcm}(a,b)$ | least common multiple | smallest positive common multiple |
| $n!$ | $n$ factorial | $n(n-1)\cdots 2 \cdot 1$, with $0! = 1$ |
| $\binom{n}{k}$ | $n$ choose $k$ | $\dfrac{n!}{k!(n-k)!}$ |
| $\lfloor x \rfloor$ | floor of $x$ | greatest integer $\le x$ |
| $\lceil x \rceil$ | ceiling of $x$ | least integer $\ge x$ |
| $\lvert x \rvert$ | absolute value of $x$ | distance from $x$ to $0$ |
| $\pm$ | plus or minus | two signs taken consistently |
| $\sqrt[n]{x}$, $x^{1/n}$ | $n$-th root of $x$ | the non-negative root for even $n$, $x \ge 0$ |
| $\sum_{k=1}^{n} a_k$ | sum of $a_k$ for $k$ from 1 to $n$ | $\sigma$ notation |
| $\prod_{k=1}^{n} a_k$ | product | $\pi$ notation |
| $\infty$ in a sum | — | only in the sense of a limit; see series |
| $x \propto y$ | $x$ is proportional to $y$ | $x = ky$ for some constant $k$ |
| $\log_a x$, $\ln x$, $\log x$ | log base $a$, natural log, base-10 log | $\ln$ always means $\log_e$; $\log$ without a base means $\log_{10}$ in elementary chapters and $\ln$ in analysis, stated explicitly |
| $\operatorname{Re} z$, $\operatorname{Im} z$ | real / imaginary part | $z = \operatorname{Re} z + i\operatorname{Im} z$ |
| $\bar{z}$ | complex conjugate | $a - bi$ for $z = a + bi$ |
| $\lvert z \rvert$, $\arg z$ | modulus / argument | polar coordinates in the plane |

---

## 4. Functions and relations

| Symbol | Read as | Meaning |
|---|---|---|
| $f : A \to B$ | $f$ maps $A$ to $B$ | domain $A$, codomain $B$ |
| $f(x)$ | $f$ of $x$ | the value of $f$ at $x$ |
| $f \circ g$ | $f$ composed with $g$ | $(f \circ g)(x) = f(g(x))$; apply the right one first |
| $f^{-1}$ | inverse of $f$ | exists only when $f$ is a bijection |
| $f[A]$, $f^{-1}[B]$ | image / preimage of a set | sets, not points |
| $a \sim b$ | $a$ is equivalent to $b$ | equivalence relation |
| $a \le b$ | $a$ is at most $b$ | partial or total order, depending on context |
| $\sup S$, $\inf S$ | supremum / infimum | least upper / greatest lower bound |
| $\max S$, $\min S$ | maximum / minimum | attained extremum |
| $\operatorname{dom} f$, $\operatorname{ran} f$ | domain / range | |
| $\mathbf{1}_A$ | indicator of $A$ | $1$ on $A$, $0$ outside |
| $\delta_{ij}$ | Kronecker delta | $1$ if $i=j$, else $0$ |

---

## 5. Calculus and analysis

| Symbol | Read as | Meaning |
|---|---|---|
| $\lim_{x \to a} f(x) = L$ | the limit of $f$ at $a$ is $L$ | as $x$ approaches $a$ |
| $\lim_{x \to a^+}$, $\lim_{x \to a^-}$ | right / left limit | one-sided |
| $\lim_{n \to \infty} a_n$ | limit of the sequence | convergence of a sequence |
| $f'(x)$, $\dfrac{df}{dx}$ | derivative of $f$ | instantaneous rate of change |
| $\dfrac{\partial f}{\partial x}$ | partial derivative | derivative in $x$, others held fixed |
| $\nabla f$ | gradient of $f$ | vector of partial derivatives |
| $\int_a^b f(x)\,dx$ | integral from $a$ to $b$ | signed area / accumulation |
| $\int f(x)\,dx$ | indefinite integral | an antiderivative, up to a constant |
| $\sum_{n=1}^{\infty} a_n$ | infinite series | limit of partial sums |
| $f(x) = O(g(x))$ | big-O | $\lvert f\rvert \le C\lvert g\rvert$ eventually |
| $f(x) = o(g(x))$ | little-o | $f/g \to 0$ |
| $f \sim g$ | asymptotic equivalence | $f/g \to 1$ |
| $x \to a$ | $x$ tends to $a$ | approach, not equality |
| $\varepsilon, \delta$ | epsilon, delta | arbitrarily small positive numbers |
| $\mathbb{R}^n$ | $n$-dimensional Euclidean space | tuples of $n$ reals |
| $\lVert x \rVert$ | norm of $x$ | length; $\lVert x\rVert_2$ for Euclidean norm |
| $\langle x, y \rangle$ | inner product | generalises the dot product |
| $\operatorname{diam} S$ | diameter of $S$ | $\sup\{d(x,y) : x,y \in S\}$ |
| $\overline{S}$, $S^\circ$, $\partial S$ | closure, interior, boundary | topological operations |
| $B_r(x)$ | open ball of radius $r$ about $x$ | $\{y : d(x,y) < r\}$ |

Notation for derivatives at a point uses the same symbol: $f'(a)$ and $\left.\dfrac{df}{dx}\right|_{x=a}$
mean the same thing.

---

## 6. Linear algebra

| Symbol | Read as | Meaning |
|---|---|---|
| $\mathbf{v}$, $\vec{v}$ | vector $v$ | bold in print; arrows in handwriting |
| $\mathbf{0}$ | zero vector | the additive identity of a vector space |
| $\mathbf{e}_1,\dots,\mathbf{e}_n$ | standard basis vectors | $1$ in one coordinate, $0$ elsewhere |
| $\mathbf{u} \cdot \mathbf{v}$ | dot product | $\sum_i u_i v_i$ |
| $\mathbf{u} \times \mathbf{v}$ | cross product | defined in $\mathbb{R}^3$ only |
| $A^{\mathsf{T}}$ | transpose of $A$ | rows become columns |
| $A^{-1}$ | inverse of $A$ | exists iff $\det A \ne 0$ |
| $A^{*}$ | conjugate transpose | for complex matrices |
| $\det A$, $\lvert A\rvert$ | determinant of $A$ | signed volume scaling factor |
| $\operatorname{tr} A$ | trace of $A$ | sum of diagonal entries |
| $\operatorname{rank} A$ | rank of $A$ | dimension of the column space |
| $\operatorname{null} A$ | null space | $\{x : Ax = 0\}$ |
| $\operatorname{span} S$ | span of $S$ | all linear combinations |
| $\dim V$ | dimension of $V$ | size of any basis |
| $\ker T$, $\operatorname{im} T$ | kernel and image | of a linear map |
| $V \cong W$ | $V$ is isomorphic to $W$ | there is an invertible structure-preserving map |
| $V \oplus W$ | direct sum | every element is a unique sum |
| $\lambda$ | eigenvalue | $Av = \lambda v$ with $v \ne 0$ |
| $\langle \cdot, \cdot \rangle$ | inner product | positive definite bilinear (or sesquilinear) form |

---

## 7. Probability and statistics

| Symbol | Read as | Meaning |
|---|---|---|
| $\Pr(A)$, $P(A)$ | probability of $A$ | a number in $[0,1]$ |
| $A^{\complement}$ | complement of $A$ | "not $A$" |
| $\Pr(A \mid B)$ | probability of $A$ given $B$ | $\Pr(A\cap B)/\Pr(B)$ |
| $X, Y$ | random variables | functions on a sample space |
| $X \sim F$ | $X$ has distribution $F$ | "is distributed as" |
| $X \sim \mathcal{N}(\mu,\sigma^2)$ | normal distribution | mean $\mu$, variance $\sigma^2$ |
| $X \sim \operatorname{Bin}(n,p)$ | binomial distribution | $n$ trials, success probability $p$ |
| $X \sim \operatorname{Pois}(\lambda)$ | Poisson distribution | rate $\lambda$ |
| $f_X$ | probability density function | continuous case |
| $F_X$ | cumulative distribution function | $F_X(x) = \Pr(X \le x)$ |
| $\mathbb{E}[X]$, $\mu$ | expectation | mean value |
| $\operatorname{Var}(X)$, $\sigma^2$ | variance | $\mathbb{E}[(X-\mu)^2]$ |
| $\sigma$ | standard deviation | $\sqrt{\operatorname{Var}(X)}$ |
| $\operatorname{Cov}(X,Y)$ | covariance | measure of joint variation |
| $\rho$ | correlation | normalised covariance |
| $\hat{\theta}$ | estimate of a parameter | the hat marks an estimator |
| $\bar{x}$ | sample mean | average of observations |
| $s^2$ | sample variance | with $n-1$ in the denominator |
| $\perp\!\!\!\perp$ | independent | $X \perp\!\!\!\perp Y$ |
| $\xrightarrow{d}$, $\xrightarrow{p}$ | convergence in distribution / probability | modes of convergence |
| $\Phi$, $\phi$ | standard normal CDF / PDF | |

---

## 8. Quantifiers and proof idioms

| Phrase in a theorem | Formal content |
|---|---|
| "for every $\varepsilon > 0$ there exists $\delta > 0$ such that …" | $\forall \varepsilon > 0\ \exists \delta > 0\ \forall x\ (\lvert x-a\rvert < \delta \Rightarrow \lvert f(x)-L\rvert < \varepsilon)$ |
| "$P$ if and only if $Q$" | prove $P \Rightarrow Q$ and $Q \Rightarrow P$ separately |
| "$P$ is necessary for $Q$" | $Q \Rightarrow P$ |
| "$P$ is sufficient for $Q$" | $P \Rightarrow Q$ |
| "unique" | at most one exists; uniqueness must be proved, not assumed |
| "without loss of generality" | a symmetry argument justifies the restriction; it must be stated |
| "if and only if" in a definition | both directions are part of the meaning |

---

## 9. Greek letters

| Letter | Name | Common use |
|---|---|---|
| $\alpha, \beta, \gamma$ | alpha, beta, gamma | angles, coefficients, scalars |
| $\delta, \varepsilon$ | delta, epsilon | small quantities in limits |
| $\zeta$ | zeta | the Riemann zeta function |
| $\eta, \theta, \vartheta$ | eta, theta | angles, parameters |
| $\kappa$ | kappa | curvature, condition number |
| $\lambda, \mu$ | lambda, mu | eigenvalues, means, rates |
| $\nu, \xi$ | nu, xi | measures, indices |
| $\pi$ | pi | $3.14159\dots$; also a projection map |
| $\rho$ | rho | density, correlation, spectral radius |
| $\sigma, \tau$ | sigma, tau | standard deviation, permutations, topology |
| $\phi, \varphi, \Phi$ | phi | angles, Euler's totient, normal CDF |
| $\chi$ | chi | characteristic, Euler characteristic |
| $\psi, \omega, \Omega$ | psi, omega | wave functions, angular frequency, sample space |

---

## 10. Typography of mathematics

* Multi-letter names are not italicised: write $\operatorname{rank}(A)$, not $rank(A)$.
* Distinguish $f^{-1}(x)$ (inverse function) from $f(x)^{-1} = 1/f(x)$.
* Distinguish $\sin^2 x = (\sin x)^2$ from $\sin^{-1} x = \arcsin x$; the $-1$ on a function name means
  inverse, while the exponent on a trigonometric function means a power. Where ambiguity is possible,
  write $\arcsin$ and $(\sin x)^2$.
* $0 \le x \le 1$ is a chain of two inequalities; $0 \le x \ge 1$ is meaningless because it asserts
  nothing about the relation between the outer terms.
* Use $\Rightarrow$ between *statements*, not between *numbers*: $x + 1 = 3 \Rightarrow x = 2$ is fine;
  $x + 1 \Rightarrow x$ is not.
* Do not use $=$ to mean "the next step is": in a derivation, write one equality per line, or use an
  `aligned` environment so that the relation is explicit.
