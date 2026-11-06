# Measure Theory — Exercises

> [Measure Theory](README.md) · 38 problems · Beginner → Challenge · Solutions: [solutions.md](solutions.md)

Every problem is a proof unless it explicitly asks for a computation. A computation is complete only when the
measure, the σ-algebra and the theorem being applied are named, and when every hypothesis of that theorem has
been checked. You may use anything proved in the [tutorial](README.md); results that the tutorial only states
(the Radon–Nikodym theorem, Riesz–Fischer completeness, Lebesgue's criterion) may be quoted but not reproved.

Notation: $(X,\mathcal{A},\mu)$ is a measure space, $\lambda$ is Lebesgue measure on $(\mathbb{R},\mathcal{L})$,
$\mathcal{B}(\mathbb{R})$ is the Borel σ-algebra, $\mu^*$ is an outer measure, $\mathbf{1}_A$ is the indicator of
$A$, and "a.e." means "$\mu$-almost everywhere". The symbol $\mathcal{R}[a,b]$ denotes the Riemann integrable
functions on $[a,b]$.

Do not open [solutions.md](solutions.md) before writing an attempt.

## Beginner

**1.** *(§7.2)* Let $X = \{1,2,3\}$. Decide, with justification, which of the following families are σ-algebras
on $X$:

(a) $\{\varnothing, X\}$; (b) $\{\varnothing,\{1\},\{2,3\},X\}$; (c) $\{\varnothing,\{1\},\{2\},\{1,2\},X\}$;
(d) $\{\varnothing,\{1,2\},X\}$.

**2.** *(§7.2)* Let $\mathcal{A}$ be a σ-algebra on $X$ and let $A, B, A_1, A_2, \dots \in \mathcal{A}$. Prove
that $A \triangle B \in \mathcal{A}$ and that $\bigcap_{n\ge1} A_n \in \mathcal{A}$. Quote only the three axioms
of Definition 5.1 at each step.

**3.** *(§7.2)* Let $\mathcal{E}_1 \subseteq \mathcal{E}_2 \subseteq \mathcal{P}(X)$. Prove that
$\sigma(\mathcal{E}_1) \subseteq \sigma(\mathcal{E}_2)$. Deduce that for $A \subseteq X$,
$$
\sigma(\{A\}) = \{\varnothing, A, A^\complement, X\},
$$
and verify directly that the right-hand side is a σ-algebra.

**4.** *(§7.2)* Let $X$ be an uncountable set and let
$\mathcal{C} = \{A \subseteq X : A \text{ is countable or } A^\complement \text{ is countable}\}$.
Prove that $\mathcal{C}$ is a σ-algebra, that $\{x\} \in \mathcal{C}$ for every $x$, and that
$\mathcal{C} \neq \mathcal{P}(X)$.

**5.** *(§7.3)* Let $\mu$ be a measure on $(X,\mathcal{A})$ and let $A, B \in \mathcal{A}$ with
$\mu(A \cup B) < \infty$. Prove that
$$
\mu(A \cup B) + \mu(A \cap B) = \mu(A) + \mu(B),
$$
and explain why the finiteness hypothesis is needed to rearrange this as
$\mu(A\cap B) = \mu(A)+\mu(B)-\mu(A\cup B)$. Give an example of measurable $A,B$ for which
$\mu(A\cup B) = \mu(A) = \mu(B) = \mu(A\cap B) = \infty$, and explain why the displayed identity itself survives
there while the rearranged form does not.

**6.** *(§7.3)* Let $X = \{1,2\}$ with $\mathcal{A} = \mathcal{P}(X)$ and $\mu = \delta_1 + 2\delta_2$, that is,
$\mu(A) = \mathbf{1}_A(1) + 2\mathbf{1}_A(2)$. Tabulate $\mu$ on all four measurable sets, prove that $\mu$ is a
measure, and compute $\int_X f\,d\mu$ and $\int_X \lvert f\rvert\,d\mu$ for $f(1) = 3$, $f(2) = -1$, in two ways:
from the definition of the integral of a simple function, and from the layer-cake formula applied to $\lvert f\rvert$.

**7.** *(§7.3)* Let $A_1, A_2, \dots \in \mathcal{A}$. Prove that $\mu\bigl(\bigcup_n A_n\bigr) \le \sum_n \mu(A_n)$,
and give an example on $(\mathbb{R},\mathcal{L},\lambda)$ in which the inequality is strict.

**8.** *(§7.5)* Compute, naming the property of $\lambda$ used at each step:

(a) $\lambda\bigl(\{1/n : n \in \mathbb{N}\} \cup \{0\}\bigr)$; (b) $\lambda\bigl((0,1)\cap\mathbb{Q}\bigr)$;
(c) $\lambda\bigl([0,1]\setminus\mathbb{Q}\bigr)$; (d) $\lambda\bigl(\bigcup_{n\ge1}(2n,2n+1)\bigr)$.

**9.** *(§7.3)* On $(\mathbb{R},\mathcal{L},\lambda)$ let $A_n = [0, 1 - 1/n]$ for $n \ge 2$. Compute
$\lambda(A_n)$ and $\lambda\bigl(\bigcup_{n\ge2} A_n\bigr)$, and identify which theorem licenses the
computation.

**10.** *(§7.3)* On $(\mathbb{R},\mathcal{L},\lambda)$ let $A_n = [n,\infty)$ for $n \ge 1$. Compute
$\lambda(A_n)$, $\bigcap_n A_n$ and $\lim_n \lambda(A_n)$. State precisely which hypothesis of Theorem 7.14
fails, and explain where the proof uses it.

**11.** *(§7.1, §7.12)* Let $D = \mathbf{1}_{\mathbb{Q}\cap[0,1]}$. Prove that $D \notin \mathcal{R}[0,1]$ and
that $D$ is Lebesgue measurable with $\int_{[0,1]} D\,d\lambda = 0$, using only the definition of the integral of
a simple function.

**12.** *(§7.6)* Let $f = \mathbf{1}_{\mathbb{Q}}$ and $g(x) = x\mathbf{1}_{\mathbb{Q}}(x)$ on $\mathbb{R}$.
Prove that both are Borel measurable, and write $\{g > a\}$ explicitly for $a < 0$, $a = 0$ and $a > 0$.

## Intermediate

**13.** *(§7.7)* Let $f(x) = x$ on $[0,1]$ and let $\varphi_n$ be the simple approximation of Theorem 7.37.
Write out $\varphi_1$ and $\varphi_2$ as explicit finite sums, evaluate $\varphi_1$ and $\varphi_2$ at
$x = 0.3$ and at $x = 0.8$, and verify the three claims of the theorem at those points.

**14.** *(§7.6)* Let $(X,\mathcal{A})$ be a measurable space and $f : X \to \mathbb{R}$. Prove that $f$ is
measurable if and only if $\{f > q\} \in \mathcal{A}$ for every $q \in \mathbb{Q}$. In your proof, show that
$\mathcal{G} = \{B \subseteq \mathbb{R} : f^{-1}(B) \in \mathcal{A}\}$ is a σ-algebra.

**15.** *(§7.6)* Let $f, g : X \to \mathbb{R}$ be measurable. Prove that $f \vee g$, $f \wedge g$, $\lvert f\rvert$,
$f^2$ and $\{f = g\}$ are measurable. (For $f^2$ you may use that $t \mapsto t^2$ is continuous and cite
Proposition 7.34, but then say exactly which hypothesis of that proposition is being used.)

**16.** *(§7.7, §7.8)* On $[0,1]$ let
$f = \sum_{n\ge1} 2^{-n}\,\mathbf{1}_{[1/(n+1),\,1/n)}$.

(a) Prove that $f$ is a pointwise limit of an increasing sequence of simple functions and compute
$\int_{[0,1]} f\,d\lambda$ from the definition.
(b) Compute the same integral with the layer-cake formula, and check that the two answers agree.

**17.** *(§7.8)* Let $f \ge 0$ be measurable. Prove Markov's inequality
$\mu(\{f \ge a\}) \le a^{-1}\int f\,d\mu$ for $a > 0$, and deduce that if $\int f\,d\mu < \infty$ then
$f < \infty$ a.e. Where is continuity from above used, and why is its finiteness hypothesis satisfied?

**18.** *(§7.9)* Let $f_1, f_2, \dots \ge 0$ be measurable. Prove that
$\int \sum_{n\ge1} f_n\,d\mu = \sum_{n\ge1} \int f_n\,d\mu$, stating precisely which theorem is applied to which
sequence. Deduce that $\int \sum_n \mathbf{1}_{A_n} = \sum_n \mu(A_n)$ for measurable $A_n$, with no hypothesis
of disjointness.

**19.** *(§7.10)* Give an example of measurable $f_n \ge 0$ on $[0,1]$ with
$\int \liminf_n f_n < \liminf_n \int f_n$, compute both sides, and verify that Fatou's inequality holds strictly.
Explain why no integrable dominating function can exist.

**20.** *(§7.11)* Compute
$$
\lim_{n\to\infty} \int_0^\infty \frac{n \sin(x/n)}{x\,(1+x^2)}\,dx,
$$
justifying the interchange with a named theorem and verifying each of its hypotheses.

**21.** *(§7.12)* Let $T : [0,1] \to \mathbb{R}$ be Thomae's function: $T(p/q) = 1/q$ for $p/q$ in lowest terms
with $q \ge 1$, and $T(x) = 0$ for irrational $x$. Using Lebesgue's criterion (Theorem 7.56, quoted), prove that
$T$ is Riemann integrable and compute its Lebesgue integral. Contrast with Problem 11.

**22.** *(§7.12)* Prove that $x^{-1/2} \in L^1((0,1),\lambda)$ and compute its integral, using monotone
convergence and Riemann integrals on $[\varepsilon,1]$. Explain why $x^{-1/2}$ is nevertheless not Riemann
integrable on $[0,1]$ in the proper sense.

**23.** *(§7.8)* Let $f$ be measurable and integrable. Prove that $\int \lvert f\rvert\,d\mu = 0$ if and only if
$f = 0$ a.e. Deduce that if $f = g$ a.e. and $f$ is integrable, then $g$ is integrable with
$\int g = \int f$.

**24.** *(§7.13)* Let $\mu(X) < \infty$ and $1 \le p < q \le \infty$.

(a) Prove that $L^q(\mu) \subseteq L^p(\mu)$ and that
$\lVert f\rVert_p \le \mu(X)^{1/p - 1/q}\lVert f\rVert_q$.
(b) Show by example on $([0,1],\lambda)$ that the inclusion can be strict, and by example on
$(\mathbb{R},\lambda)$ that it can fail altogether when $\mu(X) = \infty$.

## Advanced

**25.** *(§7.4)* Let $\mu^*$ be an outer measure on $X$ and let $\mathcal{M}$ be the family of sets satisfying
Carathéodory's criterion (Definition 5.9).

(a) Prove that $\mathcal{M}$ is closed under finite unions.
(b) Prove that $\mu^*$ is finitely additive on disjoint members of $\mathcal{M}$.
(c) Deduce that $\mathcal{M}$ is an algebra of sets (closed under complements, finite unions and finite
intersections).

**26.** *(§7.5)* Prove from Definition 7.22 that $\lambda^*([a,b]) = b - a$ for $-\infty < a < b < \infty$,
giving both inequalities and using compactness (Heine–Borel) for the harder one. Then deduce
$\lambda((a,b)) = \lambda([a,b)) = \lambda((a,b]) = b - a$.

**27.** *(§7.5)* For $t \in \mathbb{R}$ and $A \subseteq \mathbb{R}$ let $A + t = \{a + t : a \in A\}$. Prove that
$\lambda^*(A+t) = \lambda^*(A)$, that $A \in \mathcal{L}$ if and only if $A + t \in \mathcal{L}$, and that then
$\lambda(A+t) = \lambda(A)$.

**28.** *(§7.5)* Carry out Vitali's construction in full: define $x \sim y \iff x - y \in \mathbb{Q}$, choose one
representative per class inside $[0,1)$ to form $V$, and prove that $V$ is not Lebesgue measurable. Your proof
must show explicitly that the translates $V + q$, $q \in \mathbb{Q}\cap(-1,1)$, are pairwise disjoint and that
their union contains $[0,1)$.

**29.** *(§7.10)* Prove Fatou's lemma from the monotone convergence theorem in full, including the proof that
$g_n = \inf_{k\ge n} f_k$ is measurable, increasing, and converges to $\liminf_n f_n$.

**30.** *(§7.11)* Prove the dominated convergence theorem from Fatou's lemma in full, and deduce from it the
bounded convergence theorem. In your proof, identify the two places where the finiteness of $\int g\,d\mu$ is
used.

**31.** *(§7.13)* Prove Young's inequality $ab \le a^p/p + b^q/q$ for $a,b \ge 0$ and $\frac1p + \frac1q = 1$,
$1 < p < \infty$, and deduce Hölder's inequality
$\int\lvert fg\rvert\,d\mu \le \lVert f\rVert_p\lVert g\rVert_q$. Treat the cases $\lVert f\rVert_p = 0$,
$\lVert f\rVert_p = \infty$ and $0 < \lVert f\rVert_p < \infty$ separately.

**32.** *(§7.12)* Let $f \in \mathcal{R}[a,b]$. Prove that $f$ is Lebesgue measurable and that
$\int_{[a,b]} f\,d\lambda = \int_a^b f(x)\,dx$, by constructing step functions from partitions $P_n$ with
$U(f,P_n) - L(f,P_n) < 1/n$ and applying monotonicity and completeness of $\lambda$.

## Challenge

**33.** *(§7.3)* Let $A_1 \supseteq A_2 \supseteq \cdots$ be measurable with $A = \bigcap_n A_n$, and suppose only
that $\mu(A_N) < \infty$ for **some** $N$ (not necessarily $N = 1$). Prove that $\mu(A) = \lim_n \mu(A_n)$.
Then construct a decreasing sequence on some measure space with $\mu(A_N) = \infty$ for every $N$ and
$\mu(A) \ne \lim_n\mu(A_n)$, and explain why the theorem's hypothesis is exactly the borderline.

**34.** *(§7.3, §7.16)* Prove the first Borel–Cantelli lemma: if $\sum_n \mu(A_n) < \infty$ then
$\mu(\limsup_n A_n) = 0$. Deduce that if $f_n, f$ are measurable and
$\sum_{n\ge1}\mu\bigl(\{\lvert f_n - f\rvert > \varepsilon\}\bigr) < \infty$ for every $\varepsilon > 0$, then
$f_n \to f$ a.e.

**35.** *(§7.9)* Let $f \ge 0$ be measurable on $(X,\mathcal{A},\mu)$ and put $\nu(A) = \int_A f\,d\mu$.

(a) Prove that $\nu$ is a measure and that $\nu \ll \mu$.
(b) Prove the chain rule: if $\rho(A) = \int_A g\,d\nu$ with $g \ge 0$ measurable, then
$\rho(A) = \int_A fg\,d\mu$ for all $A$.
(c) Show that $\nu(X) < \infty$ does not imply $\mu(X) < \infty$, and explain why (a) and (b) do *not* give the
Radon–Nikodym theorem.

**36.** *(§7.13)* Let $\mu(X) < \infty$ and $f \in L^\infty(\mu)$. Prove that
$\lVert f\rVert_p \to \lVert f\rVert_\infty$ as $p \to \infty$, by proving the two inequalities
$\liminf_p\lVert f\rVert_p \ge \lVert f\rVert_\infty$ and $\limsup_p\lVert f\rVert_p \le \lVert f\rVert_\infty$
separately. (Chebyshev's inequality and the finite measure of $X$ are the only tools needed.)

**37.** *(§7.14)* On $(0,1)^2$ let $f(x,y) = \dfrac{x-y}{(x+y)^3}$.

(a) Compute both iterated integrals of $f$ and show that they differ.
(b) Show that $\displaystyle\int_{(0,1)^2}\lvert f\rvert\,d(\lambda\times\lambda) = \infty$.
(c) Explain why this does not contradict Fubini's theorem, and identify the exact hypothesis that fails.

**38.** *(§7.6, §7.2)* Let $(X,\mathcal{A},\mu)$ be a measure space and let
$\mathcal{N} = \{N \subseteq X : N \subseteq M \text{ for some } M \in \mathcal{A} \text{ with } \mu(M) = 0\}$.
Put $\bar{\mathcal{A}} = \{A \cup N : A \in \mathcal{A},\ N \in \mathcal{N}\}$ and define
$\bar\mu(A \cup N) = \mu(A)$.

(a) Prove that $\bar{\mathcal{A}}$ is a σ-algebra containing $\mathcal{A}$ and $\mathcal{N}$.
(b) Prove that $\bar\mu$ is well defined, that is, independent of the representation $A \cup N$.
(c) Prove that $\bar\mu$ is a complete measure extending $\mu$. (This is the **completion** of $\mu$.)
