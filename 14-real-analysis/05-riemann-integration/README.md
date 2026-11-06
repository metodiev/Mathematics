# Riemann Integration

> [Mathematics](../../README.md) › [Real Analysis](../README.md) · Level: Advanced · Prerequisites: [Logic](../../00-foundations/02-logic/README.md), [Set Theory](../../00-foundations/03-set-theory/README.md), [Proof Techniques](../../00-foundations/04-proof-techniques/README.md), [The Real Numbers and Completeness](../01-real-numbers-and-completeness/README.md), [Limits](../../07-calculus/01-limits/README.md), [Continuity](../../07-calculus/02-continuity/README.md), [Integrals](../../07-calculus/06-integrals/README.md), [The Fundamental Theorem of Calculus](../../07-calculus/07-fundamental-theorem-of-calculus/README.md) · Estimated time: 720 min

## 1. Introduction

The integral was invented twice, for two different reasons, and the two inventions turned out to describe the same object.

The first invention is **geometric**. Take a non-negative function $f$ on an interval $[a,b]$ and ask for the area of the region between its graph and the horizontal axis. The region is curved, so it has no immediate formula. The strategy of exhaustion, going back to Archimedes, is to trap the region between finitely many rectangles: rectangles that all fit inside give a lower estimate, rectangles that all contain the region give an upper estimate. If the two estimates can be made to differ by less than any prescribed $\varepsilon$, the area exists and is their common limit. That is the whole idea of this chapter, and §7.2–§7.4 turn it into a theorem.

The second invention is **analytic**. Riemann's habilitation thesis of 1854 asked when a function can be represented by a trigonometric series, and was forced to introduce the condition $\sum_i \omega_i \Delta x_i \to 0$ (where $\omega_i$ is the oscillation of $f$ on the $i$-th interval) as the exact hypothesis under which the coefficients of such a series can be computed by integration. Riemann's condition is not a definition of area at all; it is a criterion for a certain limit of finite sums to exist. Darboux, in 1875, reformulated it in terms of the supremum of lower sums and the infimum of upper sums, and that reformulation — the **Darboux criterion** — is what is proved in Theorem 7.4.

That the two inventions agree is a theorem, not a definition, and it is proved in §7.5. The agreement is not vacuous: there are bounded functions for which the lower and upper integrals differ, so the notion of "area under the graph" genuinely fails. The most famous is Dirichlet's function, which is $1$ on the rationals and $0$ on the irrationals (§7.19). It is bounded, it is defined everywhere, and it has no Riemann integral. This is not a defect of the proof technique; it is a defect of the definition, and repairing it is the whole point of Lebesgue's theory of measure, sketched as motivation in §7.20.

Three further ideas organise the chapter.

* **Squeezing.** Integrability is always established the same way: exhibit, for each $\varepsilon$, a partition whose upper and lower sums differ by less than $\varepsilon$. Every integrability theorem below is a recipe for building such a partition, either from uniform continuity (continuous functions, §7.6) or from monotonicity (§7.7).
* **Structure.** The set of integrable functions is a vector space closed under products and absolute values, and the integral is linear, monotone and additive over subintervals (§7.8–§7.12). These are not conveniences: they are what makes the integral computable, and each is proved from the Darboux criterion.
* **The inverse relationship with differentiation.** The fundamental theorem (§7.14–§7.15) says that integration and differentiation are inverse operations, under hypotheses that must be checked. Part 1 differentiates an integral and needs only continuity of the integrand at the point in question. Part 2 integrates a derivative and needs the derivative to be Riemann integrable — a hypothesis that is *not* automatic, as §7.20 shows.

A warning about the word "integral". In elementary calculus, $\int_a^b f$ is computed by finding an antiderivative. Here it is defined as a supremum of lower sums, and antiderivatives appear only in §7.15, as a *consequence*. Until then, every integral in this chapter is evaluated by estimating sums. This is slower, and it is the only way to see why the fundamental theorem is true rather than assumed.

## 2. Prerequisites

**The completeness axiom and suprema.** Every definition below uses $\sup$ and $\inf$ over the uncountable set of values of $f$ on a subinterval, and the Riemann criterion compares a supremum with an infimum. You must be fluent in the $\varepsilon$-characterisation: $s = \sup A$ if and only if $s$ is an upper bound and for every $\varepsilon>0$ there is $a \in A$ with $a > s - \varepsilon$. See [The Real Numbers and Completeness](../01-real-numbers-and-completeness/README.md), §7.4.

**Bounded sets and the Archimedean property.** The Archimedean property supplies the integer $n$ in every "take a uniform partition with $n$ pieces so fine that …" argument, and it is used again to prove that the mesh of a partition can be made small.

**Logic and quantifier manipulation.** Integrability is a statement of the form $\forall \varepsilon > 0\ \exists P$. Its negation — the criterion for *non*-integrability, §7.18 — is $\exists \varepsilon_0 > 0\ \forall P$, and recognising that shape is half of every non-integrability proof. See [Logic](../../00-foundations/02-logic/README.md) and [Proof Techniques](../../00-foundations/04-proof-techniques/README.md).

**Sets, functions and images.** Partitions are finite sets; the mesh is a maximum over a finite index set; the substitution theorem uses images $\varphi([a,b])$. See [Set Theory](../../00-foundations/03-set-theory/README.md) and [Relations and Functions](../../00-foundations/05-relations-and-functions/README.md).

**Inequalities and absolute value.** The estimate $\lvert f(t)\rvert \le B$ is used to bound the effect of refining a partition, and the reverse triangle inequality supplies $\bigl\lvert \lvert f\rvert - \lvert g\rvert\bigr\rvert \le \lvert f - g\rvert$. See [Inequalities](../../03-algebra/03-inequalities/README.md).

**Limits and continuity.** The $\varepsilon$–$\delta$ definition of continuity at a point drives the proof of the fundamental theorem, part 1. Continuity on a closed interval is used through two theorems: the extreme value theorem (a continuous function on $[a,b]$ attains a maximum and a minimum) and the uniform continuity theorem (a continuous function on $[a,b]$ is uniformly continuous). Both are proved from compactness in [Continuity](../../07-calculus/02-continuity/README.md) and again, in the general setting, in [Metric Spaces](../06-metric-spaces/README.md). See also [Limits](../../07-calculus/01-limits/README.md).

**Riemann sums as seen in calculus.** You should already have met $\sum_{i=1}^n f(t_i)\Delta x_i$ and the slogan "the integral is the limit of Riemann sums". This chapter keeps the slogan but proves the equivalence of the two definitions (§7.5) rather than assuming it. See [Integrals](../../07-calculus/06-integrals/README.md).

**The mean value theorem for derivatives.** Integration by parts and part 2 of the fundamental theorem are proved by applying the MVT on each subinterval. See [Applications of Derivatives](../../07-calculus/05-applications-of-derivatives/README.md) and [The Fundamental Theorem of Calculus](../../07-calculus/07-fundamental-theorem-of-calculus/README.md).

**Induction and finite sums.** Every partition argument ends with a finite sum, and the uniform-partition computations in §9 use the identities $\sum_{k=1}^{n} k = n(n+1)/2$ and $\sum_{k=1}^{n} k^2 = n(n+1)(2n+1)/6$. See [Mathematical Induction](../../09-discrete-mathematics/01-mathematical-induction/README.md).

## 3. Learning Objectives

By the end of this tutorial you will be able to

1. define a partition, its mesh, a tagged partition, and a Riemann sum; state both the Darboux and the Riemann definitions of integrability;
2. prove that refining a partition increases lower sums and decreases upper sums, and deduce that every lower sum is at most every upper sum;
3. prove the Riemann criterion — a bounded $f$ is integrable if and only if for every $\varepsilon>0$ there is a partition with $U(f,P) - L(f,P) < \varepsilon$ — and use its negation to prove non-integrability;
4. prove that every continuous function on $[a,b]$ is integrable, and that every monotone function on $[a,b]$ is integrable;
5. compute lower and upper sums for explicit functions and partitions, and evaluate integrals from the definition for polynomials;
6. prove linearity, monotonicity, additivity over subintervals, and the inequality $\bigl\lvert\int_a^b f\bigr\rvert \le \int_a^b \lvert f\rvert$;
7. state and prove the mean value theorem for integrals, in both its plain and its weighted form;
8. state and prove both parts of the fundamental theorem of calculus, with the exact hypotheses each requires;
9. prove integration by parts and the substitution (change of variable) formula in the Riemann setting;
10. explain why the Dirichlet function is not Riemann integrable, why Thomae's function is, and why pointwise convergence does not pass through the integral — the failure that motivates measure theory.

## 4. Intuition

### 4.1 Trapping an area between staircases

Imagine a hilly plot of land of width $b-a$, whose height above a straight road is $f(x)$. You want its area. You have no formula, but you can measure.

Place a finite set of vertical fences at $a = x_0 < x_1 < \cdots < x_n = b$. In each strip you have two cheap options. You can build a flat-roofed box whose roof touches the *lowest* point of the hill in that strip: it fits under the hill, so the boxes together understate the area. Or you can build a box whose roof touches the *highest* point: it contains the strip, so the boxes together overstate the area. The first total is $L(f,P)$, the second is $U(f,P)$, and always $L(f,P) \le U(f,P)$.

Now add more fences. Each new fence splits one strip into two. Splitting can only raise the low roof (the minimum over a smaller interval is at least the minimum over the larger one) and only lower the high roof. So **refining improves both estimates**:

$$P \subseteq Q \;\Longrightarrow\; L(f,P) \le L(f,Q) \le U(f,Q) \le U(f,P).$$

The lower estimates climb, the upper estimates descend, and they can never cross: any lower sum is below any upper sum. Two monotone quantities separated by a gap either meet or leave a gap. If they meet — if the supremum of all lower sums equals the infimum of all upper sums — the area exists. If they leave a gap, "the area" of the region is simply not defined by this method, and something is genuinely wrong with the region.

### 4.2 Why "mesh → 0" is the right limit

A partition can have many pieces and still be useless: one enormous strip hides an entire mountain range. What controls the error is not the *number* of fences but the *widest* strip. That is why the fundamental limit in Riemann's definition is taken over partitions whose **mesh** $\lVert P\rVert = \max_i \Delta x_i$ tends to $0$, and it is why the proof that "mesh small" implies "sums close" (Lemma 7.5.1) is the technical heart of the equivalence of the two definitions.

### 4.3 The dynamical picture

Here is a second, equivalent image, which explains why integrals appear in physics and probability. Let $f$ be a rate: litres per second, joules per metre, probability per unit length. Over a tiny interval of length $h$, the amount delivered is approximately $f(x)h$, and the error is $o(h)$ if $f$ is continuous. To get the total over $[a,b]$, add the tiny contributions: $\sum f(t_i)\Delta x_i$. The integral is the exact total, and its additivity over subintervals (§7.10) is the statement that a total over $[a,c]$ plus a total over $[c,b]$ is the total over $[a,b]$ — the bookkeeping identity that makes the accumulation function in the fundamental theorem work.

### 4.4 What can go wrong

Two functions expose the boundary of the theory.

* The **Dirichlet function** $\mathbf{1}_{\mathbb{Q}}$ equals $1$ on the rationals and $0$ on the irrationals. Every strip of positive length contains both kinds of point, so every low roof is $0$ and every high roof is the full width: the lower integral is $0$, the upper is $b-a$. No amount of refinement helps, because refinement cannot remove the alternation. The gap is permanent.
* **Thomae's function** equals $1/q$ at a rational $p/q$ in lowest terms and $0$ at every irrational. It is discontinuous at every rational and continuous at every irrational — as badly behaved as Dirichlet's function in that sense — yet it *is* Riemann integrable, with integral $0$ (Proposition 7.25). The reason: the points where the function is large are sparse. For each $\varepsilon$, only finitely many rationals have $1/q \ge \varepsilon$, and those can be buried in strips of arbitrarily small total width.

The contrast between these two functions is the best single guide to what Riemann integrability means: it is a statement about how much *room* the bad points occupy, not about how many there are. Making "room" precise — measure — is the content of Lebesgue's theory.

## 5. Formal Definition

Throughout, $a < b$ are real numbers and $f : [a,b] \to \mathbb{R}$ is a function. We write $\Delta x_i = x_i - x_{i-1}$.

**Definition 5.1 (Partition).** A *partition* of $[a,b]$ is a finite set $P = \{x_0, x_1, \dots, x_n\}$ with

$$a = x_0 < x_1 < \cdots < x_n = b .$$

The *subintervals* of $P$ are $I_i = [x_{i-1}, x_i]$ for $i = 1, \dots, n$, and their lengths are $\Delta x_i = x_i - x_{i-1} > 0$. The *mesh* (or *norm*) of $P$ is

$$\lVert P \rVert = \max\{\Delta x_1, \dots, \Delta x_n\}.$$

The set of all partitions of $[a,b]$ is denoted $\mathcal{P}[a,b]$.

**Definition 5.2 (Refinement).** If $P, Q \in \mathcal{P}[a,b]$ and $P \subseteq Q$ as sets, then $Q$ is a *refinement* of $P$. The *common refinement* of $P$ and $Q$ is $P \cup Q$.

**Definition 5.3 (Darboux sums).** Let $f$ be bounded on $[a,b]$ and let $P \in \mathcal{P}[a,b]$. For each $i$ put

$$m_i(f,P) = \inf_{t \in I_i} f(t), \qquad M_i(f,P) = \sup_{t \in I_i} f(t) .$$

The *lower* and *upper Darboux sums* of $f$ with respect to $P$ are

$$L(f,P) = \sum_{i=1}^{n} m_i(f,P)\,\Delta x_i, \qquad U(f,P) = \sum_{i=1}^{n} M_i(f,P)\,\Delta x_i .$$

When $f$ and $P$ are clear from context we write $m_i, M_i, L(P), U(P)$.

**Definition 5.4 (Lower and upper integrals).** With $f$ bounded on $[a,b]$,

$$\underline{\int_a^b} f = \sup_{P \in \mathcal{P}[a,b]} L(f,P), \qquad \overline{\int_a^b} f = \inf_{P \in \mathcal{P}[a,b]} U(f,P) .$$

These are real numbers: the set of lower sums is nonempty and bounded above by $U(f,P_0)$ for any one $P_0$, so completeness gives a supremum; dually for the infimum.

**Definition 5.5 (Riemann integrable — Darboux form).** A bounded function $f$ on $[a,b]$ is *Riemann integrable* if

$$\underline{\int_a^b} f = \overline{\int_a^b} f ,$$

and that common value is the *Riemann integral*, written $\int_a^b f$ or $\int_a^b f(x)\,dx$.

**Definition 5.6 (Tagged partition and Riemann sum).** A *tagged partition* of $[a,b]$ is a partition $P = \{x_0,\dots,x_n\}$ together with a choice of *tags* $t_i \in I_i = [x_{i-1}, x_i]$ for each $i$. The corresponding *Riemann sum* is

$$S(f,P,(t_i)) = \sum_{i=1}^{n} f(t_i)\,\Delta x_i .$$

**Definition 5.7 (Riemann integrable — Riemann form).** A function $f$ on $[a,b]$ is *Riemann integrable in Riemann's sense* with integral $I$ if there is a real number $I$ such that

$$\forall \varepsilon > 0\ \exists \delta > 0 : \quad \lVert P\rVert < \delta \ \text{and every choice of tags}\ \Longrightarrow\ \lvert S(f,P,(t_i)) - I\rvert < \varepsilon .$$

Note that Definition 5.7 mentions no boundedness assumption; it is a theorem (§7.13) that the functions satisfying it are exactly the bounded functions satisfying Definition 5.5, with the same value of the integral.

**Definition 5.8 (Step function).** A function $s : [a,b] \to \mathbb{R}$ is a *step function* if there is a partition $P = \{x_0,\dots,x_n\}$ and constants $c_1,\dots,c_n$ with $s(t) = c_i$ for all $t \in (x_{i-1}, x_i)$ and all $i$. (The values at the partition points are irrelevant, and we may set them at will.)

**Definition 5.9 (Oscillation).** For a bounded $f$ on a set $I \subseteq \mathbb{R}$, the *oscillation* of $f$ on $I$ is

$$\omega(f,I) = \sup_{t \in I} f(t) - \inf_{t \in I} f(t) .$$

Thus $U(f,P) - L(f,P) = \sum_i \omega(f,I_i)\,\Delta x_i$.

**Conventions.** For any $a$ and any $f$ we set $\int_a^a f = 0$, and for $a < b$ we set $\int_b^a f = -\int_a^b f$. These are conventions, chosen so that additivity (Theorem 7.12) holds without case distinctions.

## 6. Mathematical Notation

| Symbol | Read as | Meaning |
|---|---|---|
| $P = \{x_0, \dots, x_n\}$ | a partition | a finite increasing sequence from $a$ to $b$ |
| $I_i = [x_{i-1}, x_i]$ | the $i$-th subinterval | one strip of the partition |
| $\Delta x_i$ | delta $x$ sub $i$ | $x_i - x_{i-1}$, the width of $I_i$ |
| $\lVert P\rVert$ | the mesh (norm) of $P$ | the largest of the widths $\Delta x_i$ |
| $m_i(f,P)$ | lower value on $I_i$ | $\inf_{I_i} f$ |
| $M_i(f,P)$ | upper value on $I_i$ | $\sup_{I_i} f$ |
| $L(f,P)$ | lower Darboux sum | $\sum_i m_i \Delta x_i$ |
| $U(f,P)$ | upper Darboux sum | $\sum_i M_i \Delta x_i$ |
| $\underline{\int_a^b} f$ | lower integral | $\sup_P L(f,P)$ |
| $\overline{\int_a^b} f$ | upper integral | $\inf_P U(f,P)$ |
| $\int_a^b f$, $\int_a^b f(x)\,dx$ | Riemann integral of $f$ over $[a,b]$ | the common value when it exists |
| $\mathcal{P}[a,b]$ | the set of partitions | all finite increasing sequences from $a$ to $b$ |
| $t_i$ | tag | a chosen point in $I_i$ |
| $S(f,P,(t_i))$ | Riemann sum | $\sum_i f(t_i)\Delta x_i$ |
| $\mathbf{1}_{A}$ | indicator of $A$ | $1$ on $A$ and $0$ off $A$ |
| $\mathbf{1}_{\mathbb{Q}}$ | Dirichlet function | $1$ at rationals, $0$ at irrationals |
| $\omega(f,I)$ | oscillation of $f$ on $I$ | $\sup_I f - \inf_I f = M_I - m_I$ |
| $B$ or $M$ | a bound | a number with $\lvert f\rvert \le B$ on $[a,b]$ |
| $\mathcal{R}[a,b]$ | the integrable functions | $\{f : f$ is Riemann integrable on $[a,b]\}$ |

## 7. Core Concepts

### 7.1 Partitions and Darboux sums: the first observations

Fix $a<b$ and a bounded $f:[a,b]\to\mathbb{R}$. For every partition $P$ and every $i$,

$$m_i(f,P) \le f(t) \le M_i(f,P) \quad \text{for all } t \in I_i,$$

so multiplying by $\Delta x_i > 0$ and summing gives the single most-used inequality of the chapter:

$$L(f,P) \le \sum_{i=1}^{n} f(t_i)\,\Delta x_i \le U(f,P), \qquad L(f,P) \le U(f,P).$$

We call the pair of inequalities above the **sandwich inequality**. The first says the lower sum is a genuine lower bound for *every* Riemann sum of that partition, and the upper sum a genuine upper bound. Every "the integral lies between the sums" argument in this chapter is an instance of it.

Two cautions. First, $L(f,P)$ and $U(f,P)$ depend on $f$ being **bounded**: if $f$ is unbounded on some $I_i$, then $m_i = -\infty$ or $M_i = +\infty$ and the sums are meaningless. Second, the sums depend strongly on $P$: with $P = \{0,\tfrac12, 1\}$ and $f(x) = x$ on $[0,1]$ we get $L = 0\cdot\tfrac12 + \tfrac12\cdot\tfrac12 = \tfrac14$ and $U = \tfrac12\cdot\tfrac12 + 1\cdot\tfrac12 = \tfrac34$, whereas the single interval $P_0 = \{0,1\}$ gives $L = 0$ and $U = 1$. Refinement moves both estimates toward the same number.

### 7.2 Refinement monotonicity

**Lemma 7.1 (adding one point).** Let $f$ be bounded on $[a,b]$, let $P \in \mathcal{P}[a,b]$ and let $Q = P \cup \{c\}$ where $c \in [a,b]$. Then

$$L(f,P) \le L(f,Q) \qquad \text{and} \qquad U(f,Q) \le U(f,P).$$

*Proof.* If $c \in P$ there is nothing to prove, so assume $c \in (x_{k-1}, x_k)$ for some $k$. All terms of the two sums agree except the $k$-th, which in $Q$ is replaced by two terms. Write

$$m' = \inf_{[x_{k-1},c]} f, \qquad m'' = \inf_{[c,x_k]} f, \qquad m_k = \inf_{[x_{k-1},x_k]} f .$$

Since $[x_{k-1},c] \subseteq I_k$ and $[c,x_k] \subseteq I_k$, an infimum over a smaller set is at least as large: $m' \ge m_k$ and $m'' \ge m_k$. Hence

$$m'(c - x_{k-1}) + m''(x_k - c) \ge m_k(c - x_{k-1}) + m_k(x_k - c) = m_k\,\Delta x_k,$$

which is exactly $L(f,Q) \ge L(f,P)$. The argument for upper sums is the same with $\sup$ and reversed inequalities: $M' \le M_k$ and $M'' \le M_k$, so

$$M'(c - x_{k-1}) + M''(x_k - c) \le M_k\,\Delta x_k,$$

that is $U(f,Q) \le U(f,P)$. $\blacksquare$

**Lemma 7.2 (refining in general).** If $P, Q \in \mathcal{P}[a,b]$ and $P \subseteq Q$, then

$$L(f,P) \le L(f,Q) \le U(f,Q) \le U(f,P).$$

*Proof.* Write $Q = P \cup \{c_1,\dots,c_r\}$ and let $Q_j = P \cup \{c_1,\dots,c_j\}$ for $j = 0,\dots,r$, so $Q_0 = P$ and $Q_r = Q$. Each $Q_j$ is obtained from $Q_{j-1}$ by adding one point, so Lemma 7.1 applied $r$ times gives

$$L(f,P) = L(f,Q_0) \le L(f,Q_1) \le \cdots \le L(f,Q_r) = L(f,Q),$$

and likewise $U(f,Q) \le \cdots \le U(f,P)$. The middle inequality $L(f,Q) \le U(f,Q)$ is the sandwich inequality. $\blacksquare$

Lemma 7.2 is the geometric statement that adding fences improves both staircases. It has an immediate and crucial consequence: the two families of numbers are separated.

### 7.3 Common refinements and the inequality between the integrals

**Corollary 7.3.** Let $f$ be bounded on $[a,b]$ and let $P, Q \in \mathcal{P}[a,b]$. Then

$$L(f,P) \le U(f,Q).$$

Consequently

$$\underline{\int_a^b} f \;\le\; \overline{\int_a^b} f .$$

*Proof.* Let $R = P \cup Q$. By Lemma 7.2, $L(f,P) \le L(f,R)$ and $U(f,R) \le U(f,Q)$, while $L(f,R) \le U(f,R)$ by the sandwich inequality. Chaining,

$$L(f,P) \le L(f,R) \le U(f,R) \le U(f,Q).$$

For the second claim, fix $Q$. The inequality just proved says that $U(f,Q)$ is an upper bound of the set of *all* lower sums, so the least upper bound of that set is at most $U(f,Q)$:

$$\underline{\int_a^b} f = \sup_{P} L(f,P) \le U(f,Q) \qquad \text{for every } Q .$$

Now $\underline{\int_a^b} f$ is a lower bound for the set of all upper sums, so it is at most that set's infimum:

$$\underline{\int_a^b} f \le \inf_{Q} U(f,Q) = \overline{\int_a^b} f . \qquad \blacksquare$$

So the lower integral never exceeds the upper integral, and equality is exactly what integrability demands.

### 7.4 The Riemann criterion

The definition of integrability quantifies over *all* partitions, which is unusable in practice. The following theorem replaces it by a single partition per $\varepsilon$. It is the most frequently used result in the chapter.

**Theorem 7.4 (Riemann criterion / Darboux criterion).** A bounded function $f$ on $[a,b]$ is Riemann integrable if and only if for every $\varepsilon>0$ there exists a partition $P \in \mathcal{P}[a,b]$ with

$$U(f,P) - L(f,P) < \varepsilon .$$

*Proof.*

**(⇒)** Suppose $f$ is integrable and let $I = \int_a^b f$. Let $\varepsilon > 0$. Since $I = \sup_P L(f,P)$, the number $I - \varepsilon/2$ is not an upper bound for the lower sums, so there is $P_1$ with $L(f,P_1) > I - \varepsilon/2$. Since $I = \inf_P U(f,P)$, there is $P_2$ with $U(f,P_2) < I + \varepsilon/2$. Let $P = P_1 \cup P_2$. By Lemma 7.2, $L(f,P) \ge L(f,P_1)$ and $U(f,P) \le U(f,P_2)$, hence

$$U(f,P) - L(f,P) \le U(f,P_2) - L(f,P_1) < \left(I + \tfrac{\varepsilon}{2}\right) - \left(I - \tfrac{\varepsilon}{2}\right) = \varepsilon .$$

**(⇐)** Suppose every $\varepsilon > 0$ admits $P$ with $U(f,P) - L(f,P) < \varepsilon$. Since $L(f,P) \le \underline{\int_a^b} f \le \overline{\int_a^b} f \le U(f,P)$ by the definitions and Corollary 7.3,

$$0 \le \overline{\int_a^b} f - \underline{\int_a^b} f \le U(f,P) - L(f,P) < \varepsilon .$$

The left-hand side is a fixed non-negative number smaller than every positive $\varepsilon$, hence it is $0$. Therefore the two integrals are equal and $f$ is integrable. $\blacksquare$

**How to use it.** To prove that a specific $f$ is integrable, you must produce, for each $\varepsilon$, a partition whose upper and lower sums differ by less than $\varepsilon$. There are exactly two systematic ways to do that in this chapter: take a partition fine enough that the *oscillation on every subinterval* is small (continuous case, §7.6), or take a partition fine enough that the *total variation* is small (monotone case, §7.7).

**How to use its negation.** To prove that $f$ is *not* integrable, you must exhibit $\varepsilon_0>0$ such that $U(f,P) - L(f,P) \ge \varepsilon_0$ for **every** partition. Theorem 7.24 records this, and §7.19 carries it out twice.

### 7.5 The two definitions of the integral agree

The Darboux definition quantifies over partitions alone; Riemann's definition quantifies over partitions *and tags*, and controls them by the mesh. They agree, and the proof needs the following quantitative statement: refining a partition changes the sums by an amount controlled by the mesh.

**Lemma 7.5 (quantitative effect of one point).** Let $\lvert f\rvert \le B$ on $[a,b]$, let $P \in \mathcal{P}[a,b]$ and let $Q = P \cup \{c\}$ with $c \in [a,b]$. Then

$$0 \le U(f,P) - U(f,Q) \le 2B\lVert P\rVert, \qquad 0 \le L(f,Q) - L(f,P) \le 2B\lVert P\rVert .$$

*Proof.* By Lemma 7.1 both differences are non-negative. For the upper bound, take $c \in (x_{k-1},x_k)$, and let $M', M''$ be the suprema of $f$ on $[x_{k-1},c]$ and $[c,x_k]$. Then

$$U(f,P) - U(f,Q) = M_k\Delta x_k - M'(c - x_{k-1}) - M''(x_k - c) = (M_k - M')(c-x_{k-1}) + (M_k - M'')(x_k - c).$$

Because $-B \le M', M'' \le M_k \le B$, each bracket lies in $[0, 2B]$, so

$$U(f,P) - U(f,Q) \le 2B\bigl[(c - x_{k-1}) + (x_k - c)\bigr] = 2B\,\Delta x_k \le 2B\lVert P\rVert .$$

The lower-sum estimate is identical with $m' - m_k \in [0,2B]$ and $m'' - m_k \in [0,2B]$. $\blacksquare$

**Lemma 7.6 (quantitative effect of $r$ points).** Let $\lvert f\rvert \le B$, let $P \in \mathcal{P}[a,b]$, and let $R$ be a finite subset of $[a,b]$ with $r$ elements. Then

$$0 \le U(f,P) - U(f, P\cup R) \le 2Br\lVert P\rVert, \qquad 0 \le L(f,P\cup R) - L(f,P) \le 2Br\lVert P\rVert .$$

*Proof.* Add the points of $R$ one at a time and apply Lemma 7.5. The mesh only decreases when a point is added, so each step contributes at most $2B\lVert P\rVert$; there are at most $r$ steps. $\blacksquare$

**Theorem 7.7 (equivalence of the Darboux and Riemann definitions).** Let $f:[a,b]\to\mathbb{R}$ be bounded and let $I \in \mathbb{R}$. Then $f$ is Riemann integrable in Riemann's sense (Definition 5.7) with integral $I$ if and only if $f$ is Riemann integrable in the Darboux sense (Definition 5.5) with $\int_a^b f = I$.

*Proof.*

**(Darboux ⇒ Riemann.)** Assume $f$ is Darboux integrable with integral $I$. Let $\varepsilon>0$ and put $B = \sup_{[a,b]}\lvert f\rvert + 1 > 0$. By Theorem 7.4 choose $P_0 \in \mathcal{P}[a,b]$ with $U(f,P_0) - L(f,P_0) < \varepsilon/2$. Let $r$ be the number of points of $P_0$ and let

$$\delta = \frac{\varepsilon}{8Br} \quad (\text{if } r = 0 \text{ take any } \delta>0).$$

Let $P$ be any partition with $\lVert P\rVert < \delta$, with arbitrary tags $t_i$. Put $R = P_0$ in Lemma 7.6; since $P \cup P_0$ refines both $P$ and $P_0$,

$$U(f,P) \le U(f, P\cup P_0) + 2Br\lVert P\rVert \le U(f,P_0) + \tfrac{\varepsilon}{4}, \qquad L(f,P) \ge L(f,P_0) - \tfrac{\varepsilon}{4}.$$

Therefore, using the sandwich inequality and the fact that $L(f,P_0) \le I \le U(f,P_0)$,

$$U(f,P) - L(f,P) \le \bigl[U(f,P_0) - L(f,P_0)\bigr] + \tfrac{\varepsilon}{2} < \varepsilon .$$

Since $L(f,P) \le S(f,P,(t_i)) \le U(f,P)$ and also $L(f,P) \le I \le U(f,P)$, both $S$ and $I$ lie in the interval $[L(f,P), U(f,P)]$ of length less than $\varepsilon$. Hence $\lvert S(f,P,(t_i)) - I\rvert < \varepsilon$. As $\varepsilon$ was arbitrary, Definition 5.7 holds with this $I$.

**(Riemann ⇒ Darboux.)** Assume Definition 5.7 holds with integral $I$. Let $\varepsilon>0$ and let $\delta>0$ be the number supplied by Definition 5.7 for the tolerance $\varepsilon/2$. Let $P \in \mathcal{P}[a,b]$ be any partition with $\lVert P\rVert < \delta$ and with $n \ge 1$ intervals. For each $i$ choose a tag $t_i \in I_i$ with

$$f(t_i) > M_i(f,P) - \frac{\varepsilon}{2(b-a)};$$

such a tag exists because $M_i = \sup_{I_i} f$. Let $S_U$ be the corresponding Riemann sum. Then

$$U(f,P) - S_U = \sum_{i=1}^n \bigl(M_i - f(t_i)\bigr)\Delta x_i < \frac{\varepsilon}{2(b-a)}\sum_{i=1}^n \Delta x_i = \frac{\varepsilon}{2},$$

so $U(f,P) < S_U + \varepsilon/2 < I + \varepsilon/2 + \varepsilon/2 = I + \varepsilon$, since $\lvert S_U - I\rvert < \varepsilon/2$. The same argument with tags $s_i$ satisfying $f(s_i) < m_i + \varepsilon/(2(b-a))$ gives a Riemann sum $S_L$ with $S_L - L(f,P) < \varepsilon/2$, hence $L(f,P) > I - \varepsilon$. Thus for every $\varepsilon>0$ there is a partition with

$$I - \varepsilon < L(f,P) \le U(f,P) < I + \varepsilon .$$

Hence $\overline{\int_a^b} f \le I + \varepsilon$ and $\underline{\int_a^b} f \ge I - \varepsilon$ for every $\varepsilon$, so both integrals equal $I$ by Corollary 7.3. $\blacksquare$

From now on we use whichever definition is convenient, and write $\mathcal{R}[a,b]$ for the set of Riemann integrable functions on $[a,b]$.

### 7.6 Continuous functions are integrable

**Theorem 7.8.** If $f:[a,b]\to\mathbb{R}$ is continuous, then $f \in \mathcal{R}[a,b]$.

*Proof.* Let $\varepsilon>0$. A continuous function on the closed bounded interval $[a,b]$ is uniformly continuous, so there is $\delta>0$ such that

$$x, y \in [a,b],\ \lvert x - y\rvert < \delta \ \Longrightarrow\ \lvert f(x) - f(y)\rvert < \frac{\varepsilon}{b-a}.$$

(Uniform continuity is proved in [Continuity](../../07-calculus/02-continuity/README.md); in [Metric Spaces](../06-metric-spaces/README.md), Theorem 7.30 gives the general statement that a continuous function on a compact metric space is uniformly continuous.)

Let $P$ be any partition of $[a,b]$ with $\lVert P\rVert < \delta$; for instance a uniform partition with $n > (b-a)/\delta$ pieces. Fix $i$. For any $s,t \in I_i$ we have $\lvert s - t\rvert \le \Delta x_i < \delta$, hence $\lvert f(s) - f(t)\rvert < \varepsilon/(b-a)$. Taking the supremum over $s$ and the infimum over $t$,

$$M_i(f,P) - m_i(f,P) \le \frac{\varepsilon}{b-a}.$$

(Here $M_i$ and $m_i$ are finite because $f$ is continuous on the compact interval $I_i$, so the extreme value theorem applies; and the estimate passes to the supremum because it holds for all pairs.) Therefore

$$U(f,P) - L(f,P) = \sum_{i=1}^n \bigl(M_i - m_i\bigr)\Delta x_i \le \frac{\varepsilon}{b-a}\sum_{i=1}^n \Delta x_i = \varepsilon .$$

The Riemann criterion (Theorem 7.4) applies, so $f$ is integrable. $\blacksquare$

Note what the proof does *not* say: it does not produce a formula for the integral, only its existence. Values are computed either from the definition (§9) or from the fundamental theorem (§7.15).

### 7.7 Monotone functions are integrable

**Theorem 7.9.** If $f:[a,b]\to\mathbb{R}$ is monotone, then $f \in \mathcal{R}[a,b]$.

*Proof.* Suppose first that $f$ is increasing. If $f(a) = f(b)$ then $f$ is constant and integrable with integral $f(a)(b-a)$ (or directly: $U - L = 0$ for every $P$). Otherwise $D := f(b) - f(a) > 0$. Let $\varepsilon > 0$ and choose $n \in \mathbb{N}$ with

$$\frac{D(b-a)}{n} < \varepsilon .$$

Let $P = \{a, a + h, a + 2h, \dots, b\}$ with $h = (b-a)/n$. On $I_i = [x_{i-1}, x_i]$ an increasing function has infimum $f(x_{i-1})$ (attained at the left endpoint) and supremum $f(x_i)$ (attained at the right endpoint). Hence

$$U(f,P) - L(f,P) = \sum_{i=1}^n \bigl(f(x_i) - f(x_{i-1})\bigr)h = h\sum_{i=1}^n\bigl(f(x_i) - f(x_{i-1})\bigr) = h\bigl(f(b) - f(a)\bigr) = \frac{(b-a)D}{n} < \varepsilon,$$

where the sum telescopes. By Theorem 7.4, $f$ is integrable. If $f$ is decreasing, apply the result to $-f$, which is increasing, and use Theorem 7.10 below (or repeat the computation with $m_i = f(x_i)$, $M_i = f(x_{i-1})$; the telescoping sum is the same). $\blacksquare$

A monotone function may have infinitely many discontinuities — a jump at every rational, say — and Theorem 7.9 says this is harmless. What matters is that the jumps cannot be *spread out*: their total size is at most $f(b)-f(a)$.

### 7.8 Linearity

**Theorem 7.10 (scalar multiples).** Let $f \in \mathcal{R}[a,b]$ and $c \in \mathbb{R}$. Then $cf \in \mathcal{R}[a,b]$ and

$$\int_a^b cf = c\int_a^b f .$$

*Proof.* If $c = 0$ both sides vanish. Suppose $c>0$. For every subinterval $I$ of every partition, $\sup_I (cf) = c\sup_I f$ and $\inf_I (cf) = c\inf_I f$ (multiplying by a positive constant preserves the order and the sup/inf). Hence for every $P$,

$$L(cf,P) = c\,L(f,P), \qquad U(cf,P) = c\,U(f,P).$$

Taking suprema and infima over $P$ and using that $c>0$,

$$\underline{\int_a^b} cf = \sup_P cL(f,P) = c\sup_P L(f,P) = c\int_a^b f, \qquad \overline{\int_a^b} cf = \inf_P cU(f,P) = c\int_a^b f .$$

So $cf$ is integrable with integral $c\int_a^b f$.

Suppose $c<0$. Then $\sup_I (cf) = c\inf_I f$ and $\inf_I (cf) = c\sup_I f$, because multiplying by a negative number reverses inequalities. Hence

$$L(cf,P) = c\,U(f,P), \qquad U(cf,P) = c\,L(f,P),$$

and now the sup/inf swap because $c<0$:

$$\underline{\int_a^b} cf = \sup_P cU(f,P) = c\inf_P U(f,P) = c\int_a^b f, \qquad \overline{\int_a^b} cf = \inf_P cL(f,P) = c\sup_P L(f,P) = c\int_a^b f .$$

Again the two integrals agree and equal $c\int_a^b f$. $\blacksquare$

**Theorem 7.11 (sums).** If $f, g \in \mathcal{R}[a,b]$ then $f+g \in \mathcal{R}[a,b]$ and

$$\int_a^b (f+g) = \int_a^b f + \int_a^b g .$$

*Proof.* On any set $I$, $\sup_I(f+g) \le \sup_I f + \sup_I g$ (the right side is an upper bound for $f+g$) and $\inf_I(f+g) \ge \inf_I f + \inf_I g$. Therefore, for every partition $P$,

$$U(f+g,P) \le U(f,P) + U(g,P), \qquad L(f+g,P) \ge L(f,P) + L(g,P).$$

We refer to this pair as the **sum estimates**.

Let $\varepsilon > 0$. By Theorem 7.4 choose $P_f$ with $U(f,P_f) - L(f,P_f) < \varepsilon$ and $P_g$ with $U(g,P_g) - L(g,P_g) < \varepsilon$, and let $P = P_f \cup P_g$. By Lemma 7.2, both differences are still $< \varepsilon$ for $P$. Using the sum estimates,

$$U(f+g,P) - L(f+g,P) \le \bigl[U(f,P) - L(f,P)\bigr] + \bigl[U(g,P) - L(g,P)\bigr] < 2\varepsilon .$$

So $f+g$ is integrable by Theorem 7.4. For the value, the sum estimates and Lemma 7.2 give

$$\int_a^b (f+g) \le U(f+g,P) \le U(f,P) + U(g,P) < L(f,P) + L(g,P) + 2\varepsilon \le \int_a^b f + \int_a^b g + 2\varepsilon,$$

and symmetrically

$$\int_a^b (f+g) \ge L(f+g,P) \ge L(f,P) + L(g,P) > U(f,P) + U(g,P) - 2\varepsilon \ge \int_a^b f + \int_a^b g - 2\varepsilon .$$

Since $\varepsilon>0$ is arbitrary, the two integrals are equal. $\blacksquare$

Theorems 7.10 and 7.11 say that $\mathcal{R}[a,b]$ is a real vector space and that $f \mapsto \int_a^b f$ is a linear functional on it.

### 7.9 Monotonicity

**Theorem 7.12 (monotonicity).** If $f, g \in \mathcal{R}[a,b]$ and $f(t) \le g(t)$ for all $t \in [a,b]$, then

$$\int_a^b f \le \int_a^b g .$$

*Proof.* For every partition $P$ and every $i$, $m_i(f,P) \le m_i(g,P)$ because $f \le g$ pointwise. Multiplying by $\Delta x_i>0$ and summing, $L(f,P) \le L(g,P)$ for every $P$. Taking suprema over $P$ and using the integrability of both functions,

$$\int_a^b f = \sup_P L(f,P) \le \sup_P L(g,P) = \int_a^b g . \qquad \blacksquare$$

**Corollary (integration preserves inequalities and bounds).** If $f \in \mathcal{R}[a,b]$ and $m \le f \le M$ on $[a,b]$, then

$$m(b-a) \le \int_a^b f \le M(b-a).$$

*Proof.* Apply Theorem 7.12 to the constant functions $m$ and $M$, whose integrals are $m(b-a)$ and $M(b-a)$ (Theorem 7.9 or direct computation from the definition). $\blacksquare$

### 7.10 Additivity over subintervals

**Theorem 7.13 (additivity).** Let $a < c < b$ and $f:[a,b]\to\mathbb{R}$ be bounded.

1. If $f \in \mathcal{R}[a,b]$, then $f \in \mathcal{R}[c,d]$ for every subinterval $[c,d]\subseteq[a,b]$.
2. If $f \in \mathcal{R}[a,c]$ and $f \in \mathcal{R}[c,b]$, then $f \in \mathcal{R}[a,b]$ and

$$\int_a^b f = \int_a^c f + \int_c^b f .$$

*Proof.*

**(1)** Let $\varepsilon>0$ and let $P$ be a partition of $[a,b]$ with $U(f,P) - L(f,P) < \varepsilon$ (Theorem 7.4). Replace $P$ by $P' = P \cup \{c, d\}$; by Lemma 7.2, $U(f,P') - L(f,P') \le U(f,P) - L(f,P) < \varepsilon$. Restrict $P'$ to $[c,d]$: this gives a partition $P''$ of $[c,d]$. The sums over $[c,d]$ are sums of some of the terms of the sums over $[a,b]$, and all remaining terms are non-negative (each $\omega_i \Delta x_i \ge 0$). Hence

$$U(f,P'') - L(f,P'') \le U(f,P') - L(f,P') < \varepsilon,$$

so $f \in \mathcal{R}[c,d]$ by Theorem 7.4.

**(2)** Let $\varepsilon>0$ and choose partitions $P_1$ of $[a,c]$ and $P_2$ of $[c,b]$ with $U(f,P_1) - L(f,P_1) < \varepsilon$ and $U(f,P_2) - L(f,P_2) < \varepsilon$. Then $P = P_1 \cup P_2$ is a partition of $[a,b]$ and, because the subintervals of $P$ are exactly those of $P_1$ together with those of $P_2$,

$$U(f,P) - L(f,P) = \bigl[U(f,P_1) - L(f,P_1)\bigr] + \bigl[U(f,P_2) - L(f,P_2)\bigr] < 2\varepsilon,$$

so $f \in \mathcal{R}[a,b]$ by Theorem 7.4.

For the value, put $A = \int_a^c f + \int_c^b f$ and let $P$ be any partition of $[a,b]$ that *contains* $c$; write $P_1 = P \cap [a,c]$ and $P_2 = P \cap [c,b]$. Then

$$L(f,P) = L(f,P_1) + L(f,P_2) \le \int_a^c f + \int_c^b f = A, \qquad U(f,P) = U(f,P_1) + U(f,P_2) \ge A .$$

Every partition of $[a,b]$ can be refined to one containing $c$, and refinement only increases lower sums and decreases upper sums (Lemma 7.2). Hence

$$\int_a^b f = \sup_{P} L(f,P) = \sup_{P \ni c} L(f,P) \le A, \qquad \int_a^b f = \inf_{P} U(f,P) = \inf_{P \ni c} U(f,P) \ge A .$$

Therefore $\int_a^b f = A$. $\blacksquare$

Part (1) says integrability is inherited by subintervals; part (2) says that the integral is finitely additive as a function of the interval. With the conventions $\int_a^a f = 0$ and $\int_b^a f = -\int_a^b f$, the identity $\int_a^b f = \int_a^c f + \int_c^b f$ holds for all orderings of $a,b,c$ (checking the cases is Exercise 14).

### 7.11 Absolute values and products

**Theorem 7.14.** If $f \in \mathcal{R}[a,b]$ then $\lvert f\rvert \in \mathcal{R}[a,b]$ and

$$\left\lvert \int_a^b f \right\rvert \le \int_a^b \lvert f\rvert .$$

*Proof.* For $s,t$ in a set $I$, the reverse triangle inequality gives

$$\bigl\lvert \lvert f(s)\rvert - \lvert f(t)\rvert \bigr\rvert \le \lvert f(s) - f(t)\rvert \le M_I(f) - m_I(f),$$

so $\omega(\lvert f\rvert, I) \le \omega(f,I)$ (the left side is the supremum of $\lvert\lvert f(s)\rvert - \lvert f(t)\rvert\rvert$ over $s,t \in I$). Therefore, for every partition $P$,

$$U(\lvert f\rvert,P) - L(\lvert f\rvert,P) = \sum_i \omega(\lvert f\rvert, I_i)\Delta x_i \le \sum_i \omega(f,I_i)\Delta x_i = U(f,P) - L(f,P).$$

Choosing $P$ with the right side $< \varepsilon$ proves $\lvert f\rvert \in \mathcal{R}[a,b]$ by Theorem 7.4.

For the inequality, $-\lvert f\rvert \le f \le \lvert f\rvert$ pointwise. By Theorem 7.12 and Theorem 7.10,

$$-\int_a^b \lvert f\rvert = \int_a^b (-\lvert f\rvert) \le \int_a^b f \le \int_a^b \lvert f\rvert,$$

which is exactly $\bigl\lvert \int_a^b f\bigr\rvert \le \int_a^b \lvert f\rvert$. $\blacksquare$

**Theorem 7.15 (products).** If $f, g \in \mathcal{R}[a,b]$ then $fg \in \mathcal{R}[a,b]$.

*Proof.* Both functions are bounded; let $B>0$ be a common bound, $\lvert f\rvert \le B$ and $\lvert g\rvert \le B$. For $s,t$ in a set $I$,

$$\lvert f(s)g(s) - f(t)g(t)\rvert \le \lvert f(s)\rvert\,\lvert g(s) - g(t)\rvert + \lvert g(t)\rvert\,\lvert f(s) - f(t)\rvert \le B\bigl(\omega(g,I) + \omega(f,I)\bigr),$$

so $\omega(fg,I) \le B(\omega(f,I) + \omega(g,I))$. Hence for every partition $P$,

$$U(fg,P) - L(fg,P) \le B\bigl[U(f,P) - L(f,P)\bigr] + B\bigl[U(g,P) - L(g,P)\bigr],$$

and choosing $P$ so that both brackets are $< \varepsilon$ (Lemma 7.2 with a common refinement) gives $U(fg,P) - L(fg,P) < 2B\varepsilon$. Theorem 7.4 applies. $\blacksquare$

### 7.12 The mean value theorem for integrals

**Theorem 7.16 (mean value theorem for integrals).** If $f:[a,b]\to\mathbb{R}$ is continuous, then there exists $c \in [a,b]$ with

$$\int_a^b f = f(c)\,(b-a).$$

*Proof.* By the extreme value theorem, $f$ attains a minimum $m$ and a maximum $M$ on $[a,b]$, so $m \le f(t) \le M$ for all $t$. By the corollary to Theorem 7.12,

$$m(b-a) \le \int_a^b f \le M(b-a), \qquad\text{so}\qquad m \le \frac{1}{b-a}\int_a^b f \le M .$$

The number $\frac{1}{b-a}\int_a^b f$ lies between two values of the continuous function $f$; by the intermediate value theorem there is $c \in [a,b]$ with $f(c)$ equal to it. $\blacksquare$

The number $\frac{1}{b-a}\int_a^b f$ is the **average value** of $f$ on $[a,b]$, and the theorem says a continuous function attains its average.

**Theorem 7.17 (weighted mean value theorem).** If $f:[a,b]\to\mathbb{R}$ is continuous, $g \in \mathcal{R}[a,b]$, and $g \ge 0$ on $[a,b]$, then there exists $c \in [a,b]$ with

$$\int_a^b f g = f(c)\int_a^b g .$$

*Proof.* Let $m$ and $M$ be the minimum and maximum of $f$, attained by the extreme value theorem. Since $g \ge 0$, we have $mg \le fg \le Mg$ pointwise; by Theorem 7.12 and Theorem 7.10,

$$m\int_a^b g = \int_a^b mg \le \int_a^b fg \le \int_a^b Mg = M\int_a^b g .$$

If $\int_a^b g = 0$ then $\int_a^b fg = 0$, and the identity $\int_a^b fg = f(c)\int_a^b g$ holds for every $c \in [a,b]$. If $\int_a^b g > 0$, divide by it to get $m \le \bigl(\int_a^b fg\bigr)\big/\bigl(\int_a^b g\bigr) \le M$, and apply the intermediate value theorem. $\blacksquare$
