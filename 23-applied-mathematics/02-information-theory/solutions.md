# Information Theory — Solutions

> [Information Theory](README.md) · Solutions to the 36 problems in [exercises.md](exercises.md)

Each solution states the strategy, carries out every significant step and ends with a check where one
is available. Logarithms are base $2$. Section references point into the [tutorial](README.md).

## Beginner

**1.** *(Strategy: apply Definition 5.3 term by term; then compare with the uniform bound of Proposition 7.5(b).)*

(a) The four terms are $-p\log_2 p$ with $p = 0.5,\,0.2,\,0.2,\,0.1$. Using $\log_2 0.5 = -1$,
$\log_2 0.2 = -2.32193$ and $\log_2 0.1 = -3.32193$:

$$\begin{aligned}
H(X) &= 0.5(1) + 0.2(2.32193) + 0.2(2.32193) + 0.1(3.32193)\\
&= 0.5 + 0.46439 + 0.46439 + 0.33219 = 1.76096\ \text{bits}.
\end{aligned}$$

(b) $\log_2 4 = 2$. By Proposition 7.5(b) the entropy of a four-point distribution is at most $2$
bits, with equality exactly when the distribution is uniform. Here the probabilities are unequal, so
the uncertainty is strictly less: the outcome is partly predictable.

(c) The contributions are $0.5$, $0.46439$, $0.46439$ and $0.33219$. The largest is the term for
$p=0.5$ and the smallest the term for $p = 0.1$. It is tempting to say "the smallest probability
contributes the most, because it is the most surprising", but the entropy weights surprise *by the
probability of needing it*. The function $\varphi(p) = -p\log_2 p$ increases on $(0,e^{-1})$ and
decreases on $(e^{-1},1)$, with maximum $\approx 0.5307$ at $p = e^{-1}\approx0.3679$; among
$0.5,0.2,0.1$ the values are $0.5$, $0.46439$, $0.33219$, so the largest probability happens to give
the largest term here, and the smallest probability the smallest.

*Check:* $H \le \log_2 4 = 2$, and the four terms sum to the value in (a). ✓

**2.** *(Strategy: Definition 5.2, with the logarithm evaluated directly.)*

$$i(1) = -\log_2 1 = 0,\qquad i(0.4) = -\log_2 0.4 = 1.32193,$$
$$i(0.01) = -\log_2 0.01 = \log_2 100 = 6.64386,\qquad i(2^{-10}) = 10.$$

In words: an event of probability $1$ conveys nothing; an event of probability $0.4$ conveys about
$1.32$ bits, i.e. slightly more than one fair coin; an event of probability $0.01$ conveys about
$6.64$ bits, like six or seven fair coins; and an event of probability $2^{-10}$ conveys exactly $10$
bits, the same as ten fair coin tosses.

*Check:* $i$ is decreasing, and $i(p)\to\infty$ as $p\to0^+$, as Theorem 7.1 requires. ✓

**3.** *(Strategy: compute from the definition, then use the algebraic symmetry of the formula.)*

(a) $\log_2 0.2 = -2.32193$, $\log_2 0.8 = -0.32193$, $\log_2 0.25 = -2$, so

$$H_b(0.2) = 0.2(2.32193)+0.8(0.32193) = 0.46439+0.25754 = 0.72193,$$
$$H_b(0.8) = 0.8(0.32193)+0.2(2.32193) = 0.25754+0.46439 = 0.72193,$$
$$H_b(0.25) = 0.25(2)+0.75(0.41504) = 0.5+0.31128 = 0.81128,$$
$$H_b(0) = -0\cdot\log_2 0 - 1\cdot\log_2 1 = 0,\qquad H_b(1) = 0.$$

(b) Substitute $1-p$ for $p$:

$$H_b(1-p) = -(1-p)\log_2(1-p) - \big(1-(1-p)\big)\log_2\big(1-(1-p)\big) = -(1-p)\log_2(1-p) - p\log_2 p = H_b(p).$$

The two terms are merely exchanged.

(c) $H_b$ attains its maximum $1$ bit at $p = \tfrac12$, by the derivative computed in §7.6,
$\frac{d}{dp}H_b = \log_2\frac{1-p}{p}$.

*Check:* $H_b(0.2) = H_b(0.8)$ and both are below $H_b(0.25) = H_b(0.75)$, consistent with symmetry
and with the maximum at $\tfrac12$. ✓

**4.** *(Strategy: treat the loaded die as a five-outcome-plus-one source; then verify the identity
"entropy = expected surprise".)*

(a) With $p_1 = \tfrac12$ and $p_2=\dots=p_6 = \tfrac1{10}$:

$$H = \tfrac12\log_2 2 + 5\cdot\tfrac1{10}\log_2 10 = 0.5 + 5(0.1)(3.32193) = 0.5+1.66096 = 2.16096\ \text{bits}.$$

(b) $\log_2 6 = 2.58496$, so $H = 2.16096 < 2.58496$. The loaded die is more predictable than the fair
one: by Proposition 7.5(b) the uniform distribution is the unique maximiser of entropy on six points,
so any deviation from uniformity lowers it.

(c) The expected self-information is $\sum_i p_i i_i = \sum_i p_i(-\log_2 p_i) = H$, so of course it
equals (a); the computation is

$$\tfrac12(1) + 5\cdot\tfrac1{10}(3.32193) = 0.5+1.66096 = 2.16096.$$

The identity is not a coincidence but the definition of entropy as expected surprise.

*Check:* $2.16096 < 2.58496$ and $2.16096 > 0$. ✓

**5.** *(Strategy: a uniform source on $n$ points has entropy $\log_2 n$; evaluate.)*

$$\log_2 3 = 1.58496,\quad \log_2 5 = 2.32193,\quad \log_2 26 = 4.70044,\quad \log_2 365 = 8.51175.$$

A fair three-sided die carries $1.5850$ bits; a fair five-sided die $2.3219$ bits; a uniformly random
letter $4.7004$ bits; a uniformly random day of a non-leap year $8.5118$ bits. Note that $26$ letters
need fewer than $5$ bits and $365$ days need fewer than $9$; entropy counts *average* distinctions, and
a prefix code for $365$ symbols needs lengths around $\log_2 365$ (a fixed-length code would use $9$
bits, since $2^8 = 256 < 365 \le 512 = 2^9$).

*Check:* the values increase with $n$, and each lies between $\lfloor\log_2 n\rfloor$ and
$\lceil\log_2 n\rceil$. ✓

**6.** *(Strategy: marginals first, then the joint entropy from the definition, then the chain rule.)*

*Marginals.* $p_X(0) = 0.3+0.2 = 0.5$, $p_X(1) = 0.1+0.4 = 0.5$;
$p_Y(0) = 0.3+0.1 = 0.4$, $p_Y(1) = 0.2+0.4 = 0.6$.

*Entropies of the marginals.*

$$H(X) = 2(0.5)(1) = 1\ \text{bit},\qquad H(Y) = H_b(0.4) = 0.4(1.32193)+0.6(0.73697) = 0.52877+0.44218 = 0.97095.$$

*Joint entropy.* Each of the four cells contributes $-p\log_2 p$:

$$\begin{aligned}
H(X,Y) &= 0.3(1.73697) + 0.2(2.32193) + 0.1(3.32193) + 0.4(1.32193)\\
&= 0.52109+0.46439+0.33219+0.52877 = 1.84644\ \text{bits}.
\end{aligned}$$

*Conditional entropy.* By the chain rule, $H(Y\mid X) = H(X,Y)-H(X) = 1.84644-1 = 0.84644$.

*Mutual information.* $I(X;Y) = H(Y)-H(Y\mid X) = 0.97095-0.84644 = 0.12451$.

*Verifications.* The second formula gives $H(X)+H(Y)-H(X,Y) = 1+0.97095-1.84644 = 0.12451$, the same
number. Note that $I>0$, so the variables are dependent; direct inspection confirms it, since
$p(0,0) = 0.3 \ne p_X(0)p_Y(0) = 0.2$.

**7.** *(Strategy: use the chain rule and the two extreme cases — independence and determinism.)*

(a) Independent: the chain rule gives $H(X,Y) = H(X)+H(Y\mid X) = H(X)+H(Y) = 1.5+0.8 = 2.3$ bits.

(b) $X=Y$: then $H(Y\mid X) = 0$, so $H(X,Y) = H(X) = 1.5$ bits.

(c) $Y = f(X)$: again $Y$ is determined by $X$, so $H(Y\mid X) = 0$ and $H(X,Y) = 1.5$ bits. Note that
$H(X\mid Y)$ is $1.5-0.6 = 0.9$ bits, not zero: knowing $Y = f(X)$ does not determine $X$ unless $f$ is
injective.

(d) $Z=(X,Y)$ with $X,Y$ independent: $H(Z) = H(X,Y) = H(X)+H(Y) = 2$ bits.

*Check:* all four answers lie between $\max(H(X),H(Y))$ and $H(X)+H(Y)$, as
$\max\{H(X),H(Y)\}\le H(X,Y)\le H(X)+H(Y)$ requires. This inequality is proved by combining
$H(X,Y) = H(X)+H(Y\mid X)$ with $0 \le H(Y\mid X)\le H(Y)$. ✓

**8.** *(Strategy: Shannon lengths, Kraft, then compare with the entropy.)*

(a) $\log_2(1/0.5) = 1$, $\log_2(1/0.25) = 2$, $\log_2(1/0.125) = 3$, $\log_2(1/0.125) = 3$. These are
already integers, so $\lceil\cdot\rceil$ does nothing: lengths $(1,2,3,3)$. Kraft:

$$\sum_i 2^{-l_i} = \tfrac12+\tfrac14+\tfrac18+\tfrac18 = 1 \le 1 .$$

(b) $L = 0.5(1)+0.25(2)+0.125(3)+0.125(3) = 0.5+0.5+0.375+0.375 = 1.75$ bits. The entropy is computed
in Example 7.6: $H = 1.75$ bits. So $L = H$ exactly.

(c) Equality in Theorem 7.21 requires two things: the Kraft sum must be $1$ (true here, so
$-\log_2 K = 0$) and the divergence $D(p\|q)$ with $q_i = 2^{-l_i}$ must vanish. Here
$2^{-l_i} = 0.5,\,0.25,\,0.125,\,0.125 = p_i$ exactly, so $q = p$ and the divergence is zero. In words:
the codes have exactly the lengths $-\log_2 p_i$, and the source is *dyadic*.

*Check:* an explicit code is $0$, $10$, $110$, $111$ — prefix-free, with the stated lengths. ✓

**9.** *(Strategy: Kraft's inequality is necessary and sufficient for binary prefix codes.)*

Compute $\sum_i 2^{-l_i}$ in each case.

| Lengths | Kraft sum | Verdict |
|---|---|---|
| $(1,2,3,3)$ | $\tfrac12+\tfrac14+\tfrac18+\tfrac18 = 1$ | exists (complete tree) |
| $(1,1,2)$ | $\tfrac12+\tfrac12+\tfrac14 = 1.25$ | impossible |
| $(2,2,2,2)$ | $4\cdot\tfrac14 = 1$ | exists (all words of length $2$) |
| $(1,2,2,3)$ | $\tfrac12+\tfrac14+\tfrac14+\tfrac18 = 1.125$ | impossible |
| $(2,2,2,3,3)$ | $3\cdot\tfrac14+2\cdot\tfrac18 = 1$ | exists |
| $(1,1,2,4)$ | $\tfrac12+\tfrac12+\tfrac14+\tfrac1{16} = 1.3125$ | impossible |

Sufficiency is the construction in the second half of Theorem 7.19: order the lengths and lay out
intervals of lengths $2^{-l_i}$ left to right inside $[0,1)$.

*Check:* every accepted set has Kraft sum $\le 1$ and every rejected set exceeds $1$, so no
arithmetical judgement is involved. Note that a Kraft sum *strictly* below $1$ is also realisable, for
example $(2,2,2)$ with sum $0.75$ (use $00,01,10$ and leave $11$ unused). ✓

**10.** *(Strategy: $C = 1-H_b(\varepsilon)$, with the values already tabulated.)*

$$C(\varepsilon) = 1-H_b(\varepsilon).$$

* $\varepsilon = 0$: $H_b(0) = 0$, so $C = 1$ bit per use. The channel is perfect; one bit in, one bit
  out.
* $\varepsilon = 0.1$: $H_b(0.1) = 0.46900$, so $C = 0.53100$ bits per use. About $53\%$ of the raw
  binary rate is recoverable.
* $\varepsilon = 0.25$: $H_b(0.25) = 0.81128$, so $C = 0.18872$ bits per use. Three quarters of the
  symbols arrive correctly, yet less than a fifth of a bit per use survives; errors are far more
  damaging than their frequency suggests.
* $\varepsilon = 0.5$: $H_b(0.5) = 1$, so $C = 0$. The output is independent of the input and no
  communication is possible.

*Check:* $C$ decreases as $\varepsilon$ grows on $[0,\tfrac12]$, $C(0)=1$, $C(\tfrac12)=0$, and
$C(\varepsilon) = C(1-\varepsilon)$ because $H_b$ is symmetric. ✓

**11.** *(Strategy: apply Definition 5.7 twice, being careful about which distribution weights the
log-ratio.)*

(a) With $p = (0.5,0.5)$ and $q = (0.25,0.75)$:

$$D(p\|q) = 0.5\log_2\frac{0.5}{0.25} + 0.5\log_2\frac{0.5}{0.75} = 0.5(1) + 0.5(-0.58496) = 0.5-0.29248 = 0.20752,$$

$$D(q\|p) = 0.25\log_2\frac{0.25}{0.5} + 0.75\log_2\frac{0.75}{0.5} = 0.25(-1) + 0.75(0.58496) = -0.25+0.43872 = 0.18872 .$$

(b) $D(p\|q)$ weights the mismatches by $p$: it is large when $p$ puts mass where $q$ puts little.
$D(q\|p)$ weights them by $q$, so it instead penalises mass that $q$ places where $p$ places little.
Here $q$ is more concentrated on the second symbol, and the two asymmetric penalties differ by about
$0.019$ bits.

(c) Neither is a distance. Both are non-negative and vanish exactly when $p=q$, but
$D(p\|q)\ne D(q\|p)$ here, and the triangle inequality fails in general (Proposition 7.31). A
divergence is not a metric.

*Check:* both values are positive, as Gibbs' inequality requires, and they differ. ✓

**12.** *(Strategy: compute $H(p)$, then the cross-entropy, then take the difference.)*

(a) With $\log_2 0.5 = -1$, $\log_2 0.3 = -1.73697$, $\log_2 0.2 = -2.32193$:

$$H(p) = 0.5(1)+0.3(1.73697)+0.2(2.32193) = 0.5+0.52109+0.46439 = 1.48548 .$$

Since $q$ is uniform, every term of the cross-entropy is $\log_2 3 = 1.58496$:

$$H(p,q) = 0.5(1.58496)+0.3(1.58496)+0.2(1.58496) = 1.58496 .$$

(b) $D(p\|q) = H(p,q)-H(p) = 1.58496-1.48548 = 0.09949$ bits. Directly:
$0.5\log_2\frac{0.5}{1/3}+0.3\log_2\frac{0.3}{1/3}+0.2\log_2\frac{0.2}{1/3} = 0.29248-0.04732-0.14567 = 0.09949$, the same to five decimal places. Theorem 7.29 holds.

(c) $H(p) = 1.48548$ is the smallest of the three. It must be the smallest: by Theorem 7.29,
$H(p,q) = H(p)+D(p\|q)$ and $D\ge0$, and in fact $H(p) = \min_q H(p,q)$, attained at $q=p$. Reporting a
cross-entropy therefore only means something relative to the entropy of the labels.

*Check:* ## Intermediate

**13.** *(Strategy: use the closed forms of §7.6, and be careful about what "uniform on the mean" would mean.)*

(a) For a geometric variable with parameter $p$, $\mathbb{E}[X] = 1/p = 5$. The entropy formula of §7.6
gives

$$H(X) = -\log_2 p - \frac{1-p}{p}\log_2(1-p) = -\log_2 0.2 - 4\log_2 0.8 = 2.32193 + 4(0.32193) = 2.32193+1.28771 = 3.60964 .$$

(b) $\log_2 5 = 2.32193$ is the entropy of the uniform distribution on *five points*, and that
distribution has mean $3$, not $5$; it is therefore not a distribution with the same mean, and the
comparison is not an entropy bound for this problem. A fair competitor with mean $5$ is the uniform
distribution on $\{1,\dots,9\}$, whose entropy is $\log_2 9 = 3.16993$, and $3.60964 > 3.16993$. The
geometric law is larger because, by the maximum-entropy result of Example 9.9, the geometric is the
*unique* maximiser of entropy among all distributions on $\{1,2,\dots\}$ with mean $5$.

(c) $H(X) = -\log_2 p - \frac{1-p}{p}\log_2(1-p)$ is strictly decreasing in $p$ (its derivative is
negative for $p\in(0,1)$; numerically $H(0.45) = 2.20617$, $H(0.5) = 2$, $H(0.55) = 1.80504$), and
$p = \tfrac12$ gives $-(-1) - 1\cdot(-1) = 2$. Hence $p = \tfrac12$ is the unique solution.

*Check:* $H(0.5) = 2$ exactly, and the value increases as $p$ decreases, consistent with a longer
tail. ✓

**14.** *(Strategy: compute the mass function exactly, then the entropy from its definition, then
Stirling.)*

(a) With $n=5$, $p=0.4$, $q=0.6$:

| $k$ | $0$ | $1$ | $2$ | $3$ | $4$ | $5$ |
|---|---|---|---|---|---|---|
| $p_k$ | $0.07776$ | $0.25920$ | $0.34560$ | $0.23040$ | $0.07680$ | $0.01024$ |

The values follow from $\binom{5}{k}(0.4)^k(0.6)^{5-k}$; for instance
$\binom{5}{2}(0.16)(0.216) = 10(0.03456) = 0.3456$. The sum is $1.00000$.

(b) Using $\log_2 p_k$ for each $k$:

$$\begin{aligned}
H &= 0.07776(3.68483) + 0.25920(1.94786) + 0.34560(1.53283) + 0.23040(2.11779) + 0.07680(3.70275) + 0.01024(6.60964)\\
&= 0.28653 + 0.50489 + 0.52974 + 0.48794 + 0.28437 + 0.06768 = 2.16115\ \text{bits}.
\end{aligned}$$

(c) The Stirling approximation is

$$\tfrac12\log_2(2\pi e\,npq) = \tfrac12\log_2(2\pi e\cdot5\cdot0.24) = \tfrac12\log_2 20.49536 = \tfrac12(4.35722) = 2.17861 .$$

The approximation overshoots by $0.0175$ bits, about $0.8\%$. The error is $O(1/n) = O(0.2)$, so a
$0.8\%$ error at $n=5$ is consistent.

*Check:* $H \le \log_2 6 = 2.5850$ (the support has six points), and the approximation lies within a
few percent. ✓

**15.** *(Strategy: sum the series numerically; then compare with the asymptotic formula.)*

(a) With $p_k = e^{-4}4^k/k!$:

| $k$ | $0$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ | $7$ | $8$ |
|---|---|---|---|---|---|---|---|---|---|
| $p_k$ | $0.01832$ | $0.07326$ | $0.14653$ | $0.19537$ | $0.19537$ | $0.15629$ | $0.10420$ | $0.05954$ | $0.02977$ |

Continuing to $k=20$ (the tail is below $10^{-6}$) and summing $-p_k\log_2 p_k$ gives

$$H(X) = 3.01043\ \text{bits}.$$

(b) The approximation is
$\tfrac12\log_2(2\pi e\cdot4) = \tfrac12\log_2 68.31750 = \tfrac12(6.09419) = 3.04710$, an overshoot of
$0.0367$ bits, about $1.2\%$.

(c) The approximation comes from replacing $k!$ by Stirling's formula and expanding around $k=\lambda$;
both steps have relative error $O(1/\lambda)$. At $\lambda = 100$ the same computation gives
$5.36782$ against the approximation $5.36902$, an error of $0.02\%$ — four times smaller in absolute
value than at $\lambda=4$ would be if the error were $1/\lambda$, which it is not quite at these small
values, but the trend is clear.

*Check:* the probabilities sum to $1$ (to the accuracy stated), and the entropy lies below
$\tfrac12\log_2(2\pi e\lambda)+1$ comfortably. ✓

**16.** *(Strategy: table first, then the four quantities, then both versions of the chain rule.)*

The joint law is

| $p(x,y)$ | $y=0$ | $y=1$ | $y=2$ |
|---|---|---|---|
| $x=0$ | $0.25$ | $0.25$ | $0$ |
| $x=1$ | $0$ | $0.125$ | $0.375$ |

*Marginals.* $p_X = (0.5, 0.5)$, so $H(X) = 1$ bit. $p_Y = (0.25, 0.25+0.125, 0.375) = (0.25,0.375,0.375)$, so

$$H(Y) = 0.25(2) + 0.375(1.41504) + 0.375(1.41504) = 0.5+0.53064+0.53064 = 1.56128 .$$

*Joint entropy.* Four non-zero cells:

$$H(X,Y) = 0.25(2)+0.25(2)+0.125(3)+0.375(1.41504) = 0.5+0.5+0.375+0.53064 = 1.90564 .$$

*Conditionals.* $H(Y\mid X) = 1.90564-1 = 0.90564$ and $H(X\mid Y) = 1.90564-1.56128 = 0.34436$.

*Mutual information.* $I = H(X)-H(X\mid Y) = 1-0.34436 = 0.65564$, and indeed
$H(X)+H(Y)-H(X,Y) = 1+1.56128-1.90564 = 0.65564$.

*Both chain rules.* $H(X)+H(Y\mid X) = 1+0.90564 = 1.90564 = H(X,Y)$ and
$H(Y)+H(X\mid Y) = 1.56128+0.34436 = 1.90564$. ✓

*Check:* $I \le \min\{H(X),H(Y)\} = 1$, and all conditional entropies are non-negative. ✓

**17.** *(Strategy: a composition of two BSCs is a BSC; then the chain rule along the Markov chain.)*

(a) An error occurs in the composite exactly when exactly one of the two channels errs:

$$\varepsilon_{XZ} = 0.1(1-0.2) + (1-0.1)(0.2) = 0.08+0.18 = 0.26 .$$

(b) Since $Z$ is conditionally independent of $X$ given $Y$, $H(Z\mid X,Y) = H(Z\mid Y) = H_b(0.2) = 0.72193$. Therefore

$$H(X,Y,Z) = H(X)+H(Y\mid X)+H(Z\mid X,Y) = 1+0.46900+0.72193 = 2.19092 .$$

(c) $I(X;Y) = 1-H_b(0.1) = 1-0.46900 = 0.53100$.
$I(X;Z) = 1-H_b(0.26) = 1-0.82675 = 0.17325$.
For $I(X;Y\mid Z)$: the chain rule in the form $I(X;Y,Z) = I(X;Z)+I(X;Y\mid Z)$ and the Markov property
$I(X;Z\mid Y) = 0$ (so that $I(X;Y,Z) = I(X;Y)+I(X;Z\mid Y) = I(X;Y)$) give

$$I(X;Y\mid Z) = I(X;Y)-I(X;Z) = 0.53100-0.17325 = 0.35775 .$$

The data processing inequality holds: $0.17325 \le 0.53100$, with a substantial loss because the second
channel adds noise. Processing $Y$ into $Z$ cannot increase the information about $X$.

*Check:* $I(X;Y\mid Z)\ge0$ and $I(X;Z)\ge0$; the identity
$I(X;Y) = I(X;Z)+I(X;Y\mid Z)$ gives back $0.53100$. ✓

**18.** *(Strategy: one direction is Corollary 7.11; the other reads the equality case of the proof of
Theorem 7.10.)*

*If $X$ and $Y$ are independent*, then $p(y\mid x) = p(y)$ for every $x$ with $p(x)>0$, hence
$H(Y\mid X) = \sum_x p(x)H(Y) = H(Y)$, and the chain rule gives $H(X,Y) = H(X)+H(Y)$.

*Conversely*, suppose $H(X,Y) = H(X)+H(Y)$. By the chain rule this says $H(Y\mid X) = H(Y)$, i.e.
$H(Y)-H(Y\mid X) = 0$. Now

$$H(Y)-H(Y\mid X) = \sum_{x,y} p(x,y)\log_2\frac{p(y\mid x)}{p(y)} = \frac{1}{\ln 2}\sum_{x,y}p(x,y)\ln\frac{p(y\mid x)}{p(y)} .$$

Apply the elementary inequality $\ln s \ge 1-1/s$, valid for all $s>0$ with equality only at $s=1$
(equivalently $\ln t \le t-1$ with $t = 1/s$), to each pair with $p(y\mid x)>0$, taking
$s = p(y\mid x)/p(y)$; pairs with $p(y\mid x)=0$ have $p(x,y)=0$ and contribute nothing:

$$\sum_{x,y}p(x,y)\ln\frac{p(y\mid x)}{p(y)} \ge \sum_{x,y}p(x,y)\Big(1-\frac{p(y)}{p(y\mid x)}\Big) = 1-\sum_{x,y}\frac{p(x,y)p(y)}{p(y\mid x)} = 1-\sum_y p(y)\sum_x p(x) = 1-1 = 0 .$$

So $H(Y)-H(Y\mid X)\ge0$ always, and equality holds only if $\ln s = 1-1/s$, i.e. $s=1$, for every
pair with $p(x,y)>0$; that is $p(y\mid x) = p(y)$. Exactly independence. $\blacksquare$

**19.** *(Strategy: use the identification of $I$ with a divergence, and Gibbs' inequality.)*

By Theorem 7.13, $I(X;Y) = D(p_{XY}\|p_Xp_Y)$. By Gibbs' inequality (Theorem 7.30), a divergence is
zero if and only if its two arguments agree:

$$D(p_{XY}\|p_Xp_Y) = 0 \iff p_{XY}(x,y) = p_X(x)p_Y(y)\ \text{for all } x,y \iff X\perp\!\!\!\perp Y .$$

Independence gives the factorisation, and the factorisation gives independence, by definition.
$\blacksquare$

*Remark.* The same conclusion follows from Theorem 7.14(a) and the equality case of Theorem 7.10. The
two routes are the same computation seen once as a divergence and once as a difference of entropies.

**20.** *(Strategy: compute the output distribution, then subtract the conditional entropy.)*

(a) $\Pr(Y=1) = \Pr(X=1)(1-\varepsilon) + \Pr(X=0)\varepsilon = 0.3(0.8)+0.7(0.2) = 0.24+0.14 = 0.38$. Hence

$$H(Y) = H_b(0.38) = 0.38(1.39593)+0.62(0.68966) = 0.53045+0.42759 = 0.95804 .$$

For either input, the output is a Bernoulli$(\varepsilon)$, so $H(Y\mid X) = H_b(0.2) = 0.72193$.

(b) $I(X;Y) = 0.95804-0.72193 = 0.23611$ bits, against $C = 1-H_b(0.2) = 0.27807$ bits. The skewed
input wastes about $0.042$ bits per use.

(c) A predictable input produces a predictable output, and a predictable output cannot reveal much
about the input: the channel's effect is visible only in the *unpredictable* part of the signal. The
uniform input maximises $H(Y)$ and hence $I$, which is why capacity is defined as a maximum over input
distributions.

*Check:* $0 < I < C$, and $I = 0$ would require $H(Y) = H_b(0.2)$, i.e. $Y$ independent of $X$. ✓

**21.** *(Strategy: run the algorithm, then verify optimality by the two sanity conditions — Kraft
equality and $H\le L$.)*

(a) Weights $0.45, 0.20, 0.15, 0.10, 0.06, 0.04$.

1. Merge $0.06+0.04 = 0.10$ (call it $A$). Set: $0.45, 0.20, 0.15, 0.10, 0.10(A)$.
2. Merge $0.10+0.10(A) = 0.20$ (call it $B$). Set: $0.45, 0.20, 0.20(B), 0.15$.
3. Merge $0.15+0.20 = 0.35$ (call it $C$). Set: $0.45, 0.20(B), 0.35(C)$.
4. Merge $0.20(B)+0.35(C) = 0.55$ (call it $D$). Set: $0.45, 0.55(D)$.
5. Merge to the root $1.00$.

(b) One labelling gives:

| Symbol | $p$ | Code | $l$ |
|---|---|---|---|
| $a$ | $0.45$ | $0$ | $1$ |
| $b$ | $0.20$ | $111$ | $3$ |
| $c$ | $0.15$ | $110$ | $3$ |
| $d$ | $0.10$ | $100$ | $3$ |
| $e$ | $0.06$ | $1011$ | $4$ |
| $f$ | $0.04$ | $1010$ | $4$ |

(c) The entropy, with $\log_2 0.45 = -1.15200$, $\log_2 0.2 = -2.32193$, $\log_2 0.15 = -2.73697$,
$\log_2 0.1 = -3.32193$, $\log_2 0.06 = -4.05889$, $\log_2 0.04 = -4.64386$:

$$\begin{aligned}
H &= 0.45(1.15200)+0.20(2.32193)+0.15(2.73697)+0.10(3.32193)+0.06(4.05889)+0.04(4.64386)\\
&= 0.51840+0.46439+0.41055+0.33219+0.24353+0.18575 = 2.15481 .
\end{aligned}$$

$$L = 0.45(1)+0.20(3)+0.15(3)+0.10(3)+0.06(4)+0.04(4) = 0.45+0.60+0.45+0.30+0.24+0.16 = 2.20 .$$

The redundancy is $L-H = 2.20-2.15481 = 0.04519$ bits per symbol.

(d) Kraft: $\tfrac12 + 3\cdot\tfrac18 + 2\cdot\tfrac1{16} = 0.5+0.375+0.125 = 1$, so the code is
complete and no codeword can be shortened without lengthening another. The bounds
$2.15481 \le 2.20 < 3.15481$ hold.

*Check:* the code is prefix-free ($0$ is a prefix of nothing else; $111,110,100$ are all length $3$;
$1011,1010$ share the prefix $101$ only with each other's parent), and the two longest codewords go to
the two least probable symbols, as Theorem 7.24 requires. ✓

**22.** *(Strategy: Shannon lengths use ceilings; Huffman uses the tree. Compare.)*

(a) $\log_2(1/0.4) = 1.32193 \Rightarrow l_1 = 2$;
$\log_2(1/0.3) = 1.73697 \Rightarrow l_2 = 2$;
$\log_2(1/0.2) = 2.32193 \Rightarrow l_3 = 3$;
$\log_2(1/0.1) = 3.32193 \Rightarrow l_4 = 4$.
Kraft: $0.25+0.25+0.125+0.0625 = 0.6875 \le 1$. Then

$$L_{\text{Shannon}} = 0.4(2)+0.3(2)+0.2(3)+0.1(4) = 0.8+0.6+0.6+0.4 = 2.4 .$$

The entropy is $H = 0.4(1.32193)+0.3(1.73697)+0.2(2.32193)+0.1(3.32193) = 0.52877+0.52109+0.46439+0.33219 = 1.84644$, and indeed $1.84644 \le 2.4 < 2.84644$.

(b) Huffman: merge $0.1+0.2 = 0.3$; merge the two $0.3$ nodes into $0.6$; merge $0.4+0.6$. The lengths
are $(1,2,3,3)$ for $(0.4,0.3,0.2,0.1)$ respectively, so

$$L_{\text{Huffman}} = 0.4(1)+0.3(2)+0.2(3)+0.1(3) = 0.4+0.6+0.6+0.3 = 1.9 .$$

(c) Huffman saves $2.4-1.9 = 0.5$ bits per symbol, $21\%$ of the Shannon length. The Shannon code is
not optimal because $\lceil\log_2(1/p_i)\rceil$ rounds every length *up* — here by $0.67807$,
$0.26303$, $0.67807$ and $0.67807$ bits — and the weighted excess is
$\sum_i p_i(\lceil\log_2(1/p_i)\rceil-\log_2(1/p_i)) = 0.55356$ bits. Huffman's tree does better
because it spends lengths where they buy the most: it gives the most probable symbol length $1$ and
accepts length $3$ for the least probable, a trade the per-symbol ceiling rule cannot make.

*Check:* $1.84644 \le 1.9$, and the Kraft sum of $(1,2,3,3)$ is $1$. ✓

## Advanced

**23.** *(Strategy: write $H-\log_2 n$ as a single sum and apply Jensen to the strictly concave
logarithm.)*

Let $S = \operatorname{supp}p$ and $n = \lvert S\rvert$. (If $n=0$ there is no random variable; if
$n=1$ then $H=0=\log_2 1$ and there is nothing to prove.) For $x \in S$ put $u(x) = 1/n$, the uniform
distribution on $S$. Then

$$H(X)-\log_2 n = -\sum_{x\in S}p(x)\log_2 p(x) - \sum_{x\in S}p(x)\log_2 n = \sum_{x\in S}p(x)\log_2\frac{1}{n\,p(x)} .$$

The function $\log_2$ is strictly concave on $(0,\infty)$, because its second derivative is
$-1/(t^2\ln2)<0$. Jensen's inequality for a concave function and weights $p(x)$ summing to $1$ says

$$\sum_{x\in S}p(x)\log_2 y_x \le \log_2\Big(\sum_{x\in S}p(x)y_x\Big),$$

with equality if and only if all the $y_x$ with $p(x)>0$ are equal (strict concavity). Take
$y_x = 1/(n\,p(x))$:

$$\sum_{x\in S}p(x)\log_2\frac{1}{n\,p(x)} \le \log_2\Big(\sum_{x\in S}p(x)\cdot\frac{1}{n\,p(x)}\Big) = \log_2\Big(\sum_{x\in S}\frac1n\Big) = \log_2 1 = 0 .$$

Therefore $H(X) \le \log_2 n$. Equality holds if and only if $1/(np(x))$ is the same for every
$x\in S$, i.e. $p(x) = 1/n$ for all $x \in S$: the uniform distribution on the support. $\blacksquare$

*Remark.* If one refuses Jensen, the same argument can be written as weighted AM–GM:
$\prod_x (1/(np(x)))^{p(x)} \le \sum_x p(x)/(np(x)) = 1$, and taking $\log_2$ gives the result.

**24.** *(Strategy: reduce to the one-variable statement $\varphi''<0$, then sum.)*

Define $\varphi:[0,\infty)\to\mathbb{R}$ by $\varphi(t) = -t\log_2 t$ for $t>0$ and $\varphi(0)=0$. On
$(0,\infty)$,

$$\varphi'(t) = -\log_2 t - \frac{1}{\ln 2}, \qquad \varphi''(t) = -\frac{1}{t\ln 2} < 0,$$

so $\varphi$ is strictly concave, and it is continuous at $0$ from the right
($\lim_{t\to0^+}t\log_2 t = 0$).

For a probability vector $p = (p_1,\dots,p_n)$ and a fixed index $i$, the map
$t\mapsto\varphi(t)$ composed with the coordinate projection $p\mapsto p_i$ is concave; hence
$H(p) = \sum_{i=1}^n\varphi(p_i)$ is a sum of concave functions, therefore concave on the simplex.
Concavity means exactly

$$H(\lambda p + (1-\lambda)q) \ge \lambda H(p)+(1-\lambda)H(q) \qquad (0\le\lambda\le1). \ \blacksquare$$

*Interpretation.* Choose a source at random — source $p$ with probability $\lambda$, source $q$ with
probability $1-\lambda$ — and then draw one symbol from the chosen source. The marginal law of the
symbol is $\lambda p+(1-\lambda)q$, and by the chain rule its entropy is

$$H(\text{symbol}) = H(\text{which source}) + \lambda H(p)+(1-\lambda)H(q) = H_b(\lambda)+\lambda H(p)+(1-\lambda)H(q),$$

provided the choice is independent of the draw. So the mixture's entropy exceeds the average of the two
entropies by exactly $H_b(\lambda)$: the identity of the source is itself an extra unknown, and mixing
cannot reduce uncertainty. $\blacksquare$

**25.** *(Strategy: telescope the definitions; then use the Markov property to delete one conditional
mutual information.)*

*The chain rule.* By definition $I(X;Y,Z) = H(X)-H(X\mid Y,Z)$ and
$I(X;Z) = H(X)-H(X\mid Z)$, $I(X;Y\mid Z) = H(X\mid Z)-H(X\mid Y,Z)$. Adding the last two,

$$I(X;Z)+I(X;Y\mid Z) = \big[H(X)-H(X\mid Z)\big]+\big[H(X\mid Z)-H(X\mid Y,Z)\big] = H(X)-H(X\mid Y,Z) = I(X;Y,Z).$$

Note that only the definitions were used; the identity holds for every joint distribution. $\blacksquare$

*The data processing inequality.* Suppose $X\to Y\to Z$ is a Markov chain, i.e.
$p(z\mid x,y) = p(z\mid y)$ whenever the conditioning events have positive probability. Two
applications of the chain rule, in two different orders, give

$$I(X;Y,Z) = I(X;Y)+I(X;Z\mid Y), \qquad I(X;Y,Z) = I(X;Z)+I(X;Y\mid Z).$$

Under the Markov property, $X$ and $Z$ are conditionally independent given $Y$: for every $x,z$ with
$p(x,y)>0$,

$$p(x,z\mid y) = p(x\mid y)\,p(z\mid x,y) = p(x\mid y)\,p(z\mid y).$$

Therefore $I(X;Z\mid Y) = 0$ (by the conditional version of Exercise 19), and the first identity gives
$I(X;Y,Z) = I(X;Y)$. Substituting into the second,

$$I(X;Z) = I(X;Y)-I(X;Y\mid Z) \le I(X;Y),$$

because conditional mutual information is a divergence and hence non-negative (Definition 7.15).
$\blacksquare$

*Where each hypothesis is used.* The Markov property is used exactly once, to conclude
$I(X;Z\mid Y)=0$. Non-negativity of conditional mutual information (Theorem 7.14 applied to the
conditional law) gives the final inequality. If the chain is not Markov, $I(X;Z)$ can exceed $I(X;Y)$;
for instance $X=Z$ uniform and $Y$ a constant gives $I(X;Z) = 1 > 0 = I(X;Y)$.

**26.** *(Strategy: group the outcomes of $X$ by the value of $f(X)$ and apply the grouping
lemma.)*

Let $Y = f(X)$ and let $\mathcal{Y}$ be the set of values $y$ with $p_Y(y) = \sum_{x:\,f(x)=y}p_X(x) > 0$.
The events $\{X = x\}$ for $x$ in the preimage $f^{-1}(y)$ form a block of the partition of the sample
space, with total probability $p_Y(y)$. By Lemma 7.3 (generalised grouping),

$$H(X) = H(Y) + \sum_{y\in\mathcal{Y}} p_Y(y)\,H\big(X \mid Y=y\big),$$

where $H(X\mid Y=y)$ is the entropy of the conditional distribution $p_X(x)/p_Y(y)$ over
$x \in f^{-1}(y)$. Each conditional entropy is non-negative, so

$$H(f(X)) = H(Y) \le H(X).$$

Equality holds if and only if every conditional entropy is zero, i.e. for every $y$ with $p_Y(y)>0$
the conditional distribution is concentrated on a single point of the support: each preimage contains
exactly one $x$ with $p_X(x)>0$. That is precisely injectivity of $f$ on $\operatorname{supp}p_X$.
$\blacksquare$

*Relabelling.* If $f$ is a bijection of the (finite) alphabet, it is injective on the support, so
$H(f(X)) = H(X)$: entropy depends on the probabilities, not on the names of the outcomes.

**27.** *(Strategy: write the difference as an expectation of a log-ratio and apply
$\ln t\le t-1$.)*

Let $p(x,y)$ be the joint law, with marginals $p_X,p_Y$. For pairs with $p(x,y)>0$ define
$t(x,y) = p_X(x)p_Y(y)/p(x,y) > 0$. Then

$$H(X)+H(Y)-H(X,Y) = \sum_{x,y} p(x,y)\log_2\frac{p_X(x)p_Y(y)}{p(x,y)} = \frac{1}{\ln 2}\sum_{p(x,y)>0} p(x,y)\ln t(x,y).$$

Apply $\ln t \le t-1$ term by term and sum, noting that every term with $p(x,y)=0$ is absent from the
sum:

$$\sum_{p(x,y)>0}p(x,y)\ln t(x,y) \le \sum_{p(x,y)>0}p(x,y)\big(t(x,y)-1\big) = \sum_{p(x,y)>0}p_X(x)p_Y(y) - \sum_{p(x,y)>0}p(x,y).$$

The second sum is $1$. The first is at most $\sum_{x,y}p_X(x)p_Y(y) = 1$, since it omits the non-negative
terms with $p(x,y)=0$. Hence the right side is $\le 1-1 = 0$, and dividing by $\ln 2>0$,

$$H(X)+H(Y)-H(X,Y) \le 0, \qquad\text{i.e.}\qquad H(X,Y)\le H(X)+H(Y).$$

Equality requires $\ln t = t-1$ for every pair with $p(x,y)>0$, which happens exactly when
$t(x,y)=1$, i.e. $p(x,y) = p_X(x)p_Y(y)$ for all such pairs. This is independence (the remaining
entries are zero on both sides). Conversely, if $X\perp\!\!\!\perp Y$ then $p(x,y) = p_X(x)p_Y(y)$ and
each log-ratio is zero, so equality holds. $\blacksquare$

**28.** *(Strategy: the same $D(f\|g)\ge0$ device as Theorem 7.18, with the exponential as the
comparison density.)*

Let $f$ be a density on $[0,\infty)$ with $\int_0^\infty x f(x)\,dx = \mu \in (0,\infty)$, and let
$g(x) = \frac1\mu e^{-x/\mu}$ be the exponential density with the same mean. Then

$$\log_2 g(x) = -\log_2\mu - \frac{x}{\mu}\log_2 e,$$

so

$$-\int_0^\infty f\log_2 g = \log_2\mu + \frac{\log_2 e}{\mu}\int_0^\infty x f(x)\,dx = \log_2\mu + \log_2 e = \log_2(e\mu).$$

This equals $h(g)$ by the computation of §7.7 (with $\lambda = 1/\mu$).

For the comparison, use non-negativity of the divergence for densities: if $f$ and $g$ are densities
with $f$ absolutely continuous with respect to $g$ (here $g>0$ on $[0,\infty)$ and $f$ is supported
there), then

$$D(f\|g) = \int_0^\infty f\log_2\frac{f}{g} = \frac{1}{\ln2}\int_0^\infty f\ln\frac{f}{g} \ge 0,$$

because $\ln$ is concave and Jensen gives
$\int f\ln(g/f) \le \ln\int f(g/f) = \ln 1 = 0$ (equivalently, apply $\ln s\ge1-1/s$ pointwise). Hence

$$0 \le D(f\|g) = -h(f) + h(g) \implies h(f) \le h(g) = \log_2(e\mu),$$

with equality if and only if $f = g$ almost everywhere. So the exponential with rate $1/\mu$ is the
unique maximiser, and the maximum is $\log_2(e\mu)$ bits. $\blacksquare$

*Check.* For $\mu = 1$ the maximum is $\log_2 e = 1.44270$ bits, and indeed the unit-rate exponential
has $h = \log_2(e/1) = 1.44270$. ✓

**29.** *(Strategy: factorise both joint laws and split the logarithm.)*

Assume first that $p(x,y)>0$ and $q(x,y)>0$ for all pairs, so that every conditional probability below
is defined and positive. Write $p(x,y) = p(x)p(y\mid x)$ and $q(x,y) = q(x)q(y\mid x)$; then

$$\log_2\frac{p(x,y)}{q(x,y)} = \log_2\frac{p(x)}{q(x)} + \log_2\frac{p(y\mid x)}{q(y\mid x)} .$$

Multiply by $p(x,y)$, sum over all $(x,y)$ and split:

$$\sum_{x,y}p(x,y)\log_2\frac{p(x,y)}{q(x,y)} = \sum_x p(x)\log_2\frac{p(x)}{q(x)} + \sum_x p(x)\sum_y p(y\mid x)\log_2\frac{p(y\mid x)}{q(y\mid x)},$$

where in the first term we used $\sum_y p(x,y) = p(x)$ and in the second the definition
$p(x,y) = p(x)p(y\mid x)$. The left side is $D(p(x,y)\|q(x,y))$, the first term on the right is
$D(p(x)\|q(x))$, and the inner sum is $D(p(y\mid x)\|q(y\mid x))$. $\blacksquare$

*Conventions.* (i) If $p(x)=0$, the whole slice contributes $0$ to both sides, so no conditional
probability need be defined there; the second term is understood as a sum over $x$ with $p(x)>0$.
(ii) If $q(y\mid x) = 0$ while $p(y\mid x)>0$ and $p(x)>0$, the corresponding term of
$D(p(y\mid x)\|q(y\mid x))$ is $+\infty$ and both sides are $+\infty$ — consistent, but the identity is
then an identity in $[0,\infty]$. (iii) If $q(x)=0$ with $p(x)>0$, the first term is $+\infty$ and the
joint divergence is $+\infty$ as well.

**30.** *(Strategy: the pointwise logarithm inequality, summed; then the decomposition of Theorem
7.29.)*

Let $p,q$ be probability mass functions on a finite alphabet $\mathcal{X}$. Restrict the sum to
$S = \operatorname{supp}p$. For $x\in S$ put $t(x) = q(x)/p(x) \ge 0$, and note that a term with
$q(x)=0$ has $\log_2 0 = -\infty$, in which case $D = +\infty$ and the inequality is trivial; so assume
$q(x)>0$ for $x\in S$. Using $\ln t \le t-1$,

$$-D(p\|q)\ln 2 = \sum_{x\in S}p(x)\ln\frac{q(x)}{p(x)} \le \sum_{x\in S}p(x)\Big(\frac{q(x)}{p(x)}-1\Big) = \sum_{x\in S}q(x) - \sum_{x\in S}p(x) = \sum_{x\in S}q(x) - 1 \le 0,$$

because $\sum_{x\in S}q(x)\le\sum_{x\in\mathcal{X}}q(x) = 1$. Dividing by $\ln 2>0$ gives
$-D(p\|q)\le0$, i.e. $D(p\|q)\ge0$.

*Equality.* Both inequalities must be equalities. The first requires $\ln t = t-1$, hence $t = 1$, for
every $x \in S$ with $p(x)>0$, i.e. $q(x) = p(x)$ on $S$. The second requires
$\sum_{x\in S}q(x) = 1$, i.e. $q = 0$ off $S$. Together these say $q = p$. Conversely $p=q$ clearly
gives $D=0$. $\blacksquare$

*Cross-entropy.* By Theorem 7.29, $H(p,q) = H(p)+D(p\|q)$. Since $D(p\|q)\ge0$, we get
$H(p,q)\ge H(p)$, with equality exactly when $D(p\|q)=0$, i.e. $q=p$. Thus the cross-entropy is
minimised, for fixed $p$, at $q=p$, and the minimum value is the entropy $H(p)$.

## Challenge

**31.** *(Strategy: introduce the error indicator, split the conditional entropy by it, and bound the
two pieces.)*

Let $\mathcal{X}$ be the alphabet of $X$, let $\hat X = g(Y)$ be the decoder's output, and let
$E = \mathbf{1}\{\hat X \ne X\}$ with $P_e = \Pr(E=1)$.

*Step 1: adding a variable cannot lower the conditional entropy.* Since $H(X\mid Y) \le H(X,E\mid Y)$
by Theorem 7.10 (conditioning on the extra variable $E$ can only reduce the entropy of $X$, so
releasing $E$ can only increase it), and by the chain rule
$H(X,E\mid Y) = H(E\mid Y)+H(X\mid E,Y)$,

$$H(X\mid Y) \le H(E\mid Y)+H(X\mid E,Y).$$

*Step 2: the error term.* $H(E\mid Y)\le H(E) = H_b(P_e)$ by Theorem 7.10 again, and $H(E) = H_b(P_e)$
because $E$ is binary with $\Pr(E=1)=P_e$.

*Step 3: the remaining uncertainty.* Split on $E$:

$$H(X\mid E,Y) = \Pr(E=0)\,H(X\mid Y,E=0) + \Pr(E=1)\,H(X\mid Y,E=1).$$

On the event $E=0$ we have $X = \hat X = g(Y)$, which is a function of $Y$; hence
$H(X\mid Y,E=0)=0$. On the event $E=1$ we know $X \ne g(Y)$, so conditionally on $Y$ and $E=1$ the
variable $X$ is supported on the remaining $\lvert\mathcal{X}\rvert-1$ symbols and

$$H(X\mid Y,E=1) \le \log_2(\lvert\mathcal{X}\rvert-1)$$

by Proposition 7.5(b) (with the convention $\log_2 0 = -\infty$ and entropy $0$ when the alphabet has
one symbol, in which case the bound is vacuous and $P_e=0$ anyway).

*Conclusion.* Substituting into Step 1,

$$H(X\mid Y) \le H_b(P_e) + P_e\log_2(\lvert\mathcal{X}\rvert-1). \ \blacksquare$$

*Use.* Dividing by $n$ and inserting the bound into $nR = H(X^n) \le I(X^n;Y^n)+H(X^n\mid Y^n)$ gives
the converse direction of Theorem 7.28: if $P_e\to0$ then $R \le C$. Note that the bound is only
useful when $P_e$ is small; for $P_e$ near $1$ the right side exceeds $\log_2\lvert\mathcal{X}\rvert$.

**32.** *(Strategy: expand $L-H$ as a divergence, using the fact that $q_i = 2^{-l_i}$ is a
distribution precisely because the Kraft sum is $1$.)*

Suppose the code is complete, i.e. $\sum_i 2^{-l_i} = 1$, and set $q_i = 2^{-l_i}$. Then
$q_i \ge 0$ and $\sum_i q_i = 1$, so $q$ is a probability distribution on the same alphabet, and

$$\begin{aligned}
L - H(p) &= \sum_i p_i l_i + \sum_i p_i\log_2 p_i
= \sum_i p_i\log_2\frac{1}{2^{-l_i}} + \sum_i p_i\log_2 p_i\\
&= \sum_i p_i \log_2\frac{p_i}{2^{-l_i}} = \sum_i p_i\log_2\frac{p_i}{q_i} = D(p\|q).
\end{aligned}$$

By Gibbs' inequality (Theorem 7.30), $D(p\|q)\ge0$, so $L\ge H(p)$: this recovers Theorem 7.21 for
complete codes. Moreover $L = H(p)$ if and only if $D(p\|q)=0$, if and only if $p_i = q_i = 2^{-l_i}$
for every $i$.

Since each $l_i$ is a positive integer, $2^{-l_i}$ is a negative power of $2$. So equality $L=H$ forces
every $p_i$ to be of the form $2^{-k}$; a distribution such as $(0.3,0.7)$ can never be coded with
expected length equal to its entropy, and indeed $H(0.3) = 0.88129$ is not a sum of integer-weighted
negative powers of $2$ in that way. Conversely, if $p_i = 2^{-k_i}$ with $\sum_i 2^{-k_i}=1$, the
assignment $l_i = k_i$ is a complete prefix code by Kraft and attains $L = H$ — this is the dyadic case
of Example 7.6 and Exercise 8.

*For an incomplete code* the same computation gives $L-H = D(p\|q') - \log_2 K$, where
$K = \sum_i 2^{-l_i} \le 1$ and $q'_i = 2^{-l_i}/K$; the extra term $-\log_2 K \ge 0$ is the price of
wasting part of the Kraft budget, and can be removed by extending the code to a complete one.

**33.** *(Strategy: condition on $Y$; adding a constant is a bijection, and conditioning cannot increase
entropy.)*

Let $Z = X + Y$. For each fixed value $y$ of $Y$ with $\Pr(Y=y)>0$, the map $x \mapsto x+y$ is a
bijection of the integers, so by Exercise 26 (or directly, by relabelling the outcomes)

$$H(Z \mid Y = y) = H(X+Y \mid Y=y) = H(X\mid Y=y) = H(X),$$

the last equality because $X \perp\!\!\!\perp Y$. Hence $H(Z\mid Y) = \sum_y p_Y(y)H(X) = H(X)$. Now
Theorem 7.10 gives

$$H(Z) \ge H(Z\mid Y) = H(X),$$

and exchanging the roles of $X$ and $Y$ gives $H(Z)\ge H(Y)$. Therefore
$H(X+Y)\ge\max\{H(X),H(Y)\}$. $\blacksquare$

*Equality.* Take $Y\equiv0$ (a degenerate variable): then $Z = X$ and $H(Z) = H(X) = \max\{H(X),0\}$.
More generally any degenerate summand gives equality for the non-degenerate one.

*Strictness.* Let $X,Y$ be independent Bernoulli$(\tfrac12)$; then $H(X)=H(Y)=1$ but $X+Y$ takes the
values $0,1,2$ with probabilities $\tfrac14,\tfrac12,\tfrac14$ and

$$H(X+Y) = \tfrac12(1) + 2\cdot\tfrac14(2) = 1.5 > 1 .$$

*Without independence the result fails.* Take $X$ uniform on $\{0,1\}$ and $Y = -X$; then $X+Y=0$
identically, so $H(X+Y)=0<1=H(X)$. The proof uses independence twice: to compute $H(X\mid Y)=H(X)$ and
to justify conditioning on $Y$ at all. (The inequality $H(X+Y)\ge H(X+Y\mid Y)$ itself needs no
independence; it is the identification of the right side with $H(X)$ that does.)

**34.** *(Strategy: normalise to probability vectors and quote Gibbs; then apply the inequality
coordinate by coordinate.)*

*The log-sum inequality.* Let $a_i,b_i\ge0$ with $A = \sum_i a_i$ and $B = \sum_i b_i > 0$.

If $A = 0$ then all $a_i = 0$ and both sides are $0$ (with the convention $0\log 0 = 0$). Assume
$A>0$. If some $b_i = 0$ with $a_i>0$, the left side is $+\infty$ and the inequality is trivial; so
assume $b_i>0$ whenever $a_i>0$. Put $\alpha_i = a_i/A$ and $\beta_i = b_i/B$, two probability
vectors. Then

$$\begin{aligned}
\sum_i a_i\log_2\frac{a_i}{b_i}
&= A\sum_i \alpha_i\log_2\frac{\alpha_i A}{\beta_i B}
= A\sum_i\alpha_i\log_2\frac{\alpha_i}{\beta_i} + A\log_2\frac{A}{B}\sum_i\alpha_i\\
&= A\,D(\alpha\|\beta) + A\log_2\frac{A}{B} \ge A\log_2\frac{A}{B},
\end{aligned}$$

because $D(\alpha\|\beta)\ge0$ by Gibbs. $\blacksquare$

*Joint convexity.* Let $0\le\lambda\le1$, let $p = \lambda p_1+(1-\lambda)p_2$ and
$q = \lambda q_1+(1-\lambda)q_2$. For each $x$ apply the log-sum inequality to the two non-negative
numbers $a_1 = \lambda p_1(x)$, $a_2 = (1-\lambda)p_2(x)$ and $b_1 = \lambda q_1(x)$,
$b_2 = (1-\lambda)q_2(x)$, which are indexed by $j\in\{1,2\}$:

$$\lambda p_1(x)\log_2\frac{\lambda p_1(x)}{\lambda q_1(x)} + (1-\lambda)p_2(x)\log_2\frac{(1-\lambda)p_2(x)}{(1-\lambda)q_2(x)} \ \ge\ p(x)\log_2\frac{p(x)}{q(x)} .$$

The factors $\lambda$ and $1-\lambda$ cancel inside the logarithms on the left, so summing over $x$
gives

$$\lambda D(p_1\|q_1) + (1-\lambda)D(p_2\|q_2) \ge D(p\|q). \ \blacksquare$$

*Conventions.* Terms with $a_j = 0$ contribute $0$; if $b_j = 0$ but $a_j>0$ the left side is $+\infty$
and the inequality holds; if $q(x) = 0$ but $p(x)>0$ then $D(p\|q) = +\infty$ and the right side is
$+\infty$.

**35.** *(Strategy: exchange argument, contraction, induction.)*

Let $p_1,\dots,p_n>0$ and let $T$ be a binary tree with leaves carrying these weights. Write
$L(T) = \sum_i p_i\,\mathrm{depth}(i)$.

*(i) An optimal tree can be chosen with the two least probable symbols as deepest siblings.*

Let $x,y$ be two symbols of smallest probability, and let $a,b$ be siblings at maximum depth $D$ in an
optimal tree $T$. (Such a pair exists: take a leaf of maximum depth; its sibling exists and, being at
the same depth, is also a leaf, since otherwise a child of it would be deeper.) Swap the labels of
$x$ and $a$, and of $y$ and $b$. The change in $L$ is

$$\Delta = (p_x - p_a)(D - l_x) + (p_y - p_b)(D - l_y),$$

where $l_x, l_y$ are the depths at which $x,y$ sat in $T$. Each factor is non-positive: $p_x \le p_a$
and $p_y\le p_b$ by choice of $x,y$, and $D \ge l_x, l_y$ because $D$ is the maximum depth. Hence
$\Delta\le0$. Since $T$ was optimal, $L(T+\text{swap}) \ge L(T)$, so $\Delta = 0$ and the swapped tree
is optimal with $x,y$ as deepest siblings.

*(ii) Contraction.* Let $T$ be such an optimal tree and let $T'$ be the tree obtained by deleting $x$
and $y$ and making their common parent a leaf of weight $p_x+p_y$. Every codeword of a symbol
$z \notin\{x,y\}$ has the same length in $T$ and $T'$, while $x$ and $y$ have length
$\mathrm{depth}_{T'}(\text{parent})+1$. Therefore

$$L(T) = L(T') + (p_x+p_y) .$$

Moreover $T'$ must be optimal for the contracted instance: if a tree $T''$ for $n-1$ symbols had
$L(T'') < L(T')$, expanding the contracted leaf back into $x$ and $y$ would give a tree for the
original instance with length $L(T'')+(p_x+p_y) < L(T)$, contradicting optimality of $T$.

*(iii) Induction.* The base cases $n=1,2$ are immediate: one symbol gets the empty word (or a single
bit, depending on the convention) and two symbols get $0$ and $1$, which is optimal. For the step,
Huffman's algorithm merges two symbols of smallest weight — exactly the pair $x,y$ of (i) — and then
runs on the contracted instance of $n-1$ symbols. By (ii) an optimal tree for the original instance is
the expansion of an optimal tree for the contracted one, and by the induction hypothesis Huffman's
recursive call produces an optimal tree for the contracted instance. Expanding it gives a tree of
length $L^{*}_{n-1}+(p_x+p_y) = L^{*}_n$, so Huffman's output is optimal. $\blacksquare$

*Remark on ties.* If several symbols share the smallest weight, any two of them may be merged: the
exchange argument of (i) applies to any pair $(x,y)$ of symbols whose weights are the two smallest
(with multiplicity), and the rest of the proof is unchanged. Different tie-breakings give different
codes but the same optimal length.

**36.** *(Strategy: the average of $-\log_2 p(X_i)$ is a sum of i.i.d. variables; the law of large
numbers converts it into the defining condition of the typical set.)*

Write $p(x_1,\dots,x_n) = \prod_{i=1}^n p(x_i)$ for the product law. Define
$Y_i = -\log_2 p(X_i)$. The $Y_i$ are i.i.d. with

$$\mathbb{E}[Y_i] = -\sum_x p(x)\log_2 p(x) = H,$$

finite because the alphabet is finite. Also

$$\frac1n\sum_{i=1}^n Y_i = -\frac1n\sum_{i=1}^n\log_2 p(X_i) = -\frac1n\log_2 p(X_1,\dots,X_n).$$

*(a)* By the weak law of large numbers, $\frac1n\sum_i Y_i \to H$ in probability; that is, for every
$\varepsilon>0$,

$$\Pr\Big(\Big\lvert -\tfrac1n\log_2 p(X_1,\dots,X_n) - H\Big\rvert \le \varepsilon\Big) \ge 1-\varepsilon
\quad\text{for all sufficiently large } n.$$

The event in parentheses is exactly $\{(X_1,\dots,X_n)\in\mathcal{T}_n(\varepsilon)\}$.

*(b)* If $x^n = (x_1,\dots,x_n) \in \mathcal{T}_n(\varepsilon)$ then, multiplying the defining
inequality by $n$ and negating,

$$n(H-\varepsilon) \le -\log_2 p(x^n) \le n(H+\varepsilon),$$

so

$$2^{-n(H+\varepsilon)} \le p(x^n) \le 2^{-n(H-\varepsilon)} .$$

*(c)* Summing the upper bound over the typical set,

$$1-\varepsilon \le \Pr(\mathcal{T}_n(\varepsilon)) = \sum_{x^n\in\mathcal{T}_n(\varepsilon)}p(x^n) \le \lvert\mathcal{T}_n(\varepsilon)\rvert\,2^{-n(H-\varepsilon)},$$

hence $\lvert\mathcal{T}_n(\varepsilon)\rvert \ge (1-\varepsilon)2^{n(H-\varepsilon)}$. Summing the
lower bound,

$$1 \ge \Pr(\mathcal{T}_n(\varepsilon)) \ge \lvert\mathcal{T}_n(\varepsilon)\rvert\,2^{-n(H+\varepsilon)},$$

hence $\lvert\mathcal{T}_n(\varepsilon)\rvert\le 2^{n(H+\varepsilon)}$. $\blacksquare$

*How this yields source coding.* There are at most $2^{n(H+\varepsilon)}$ typical sequences, so naming
one of them needs at most $n(H+\varepsilon)$ bits, and a short escape code handles the exceptional
sequences, whose total probability is at most $\varepsilon$; this gives a code with expected length at
most $n(H+\varepsilon)+1+O(\varepsilon n)$, i.e. rate $H+O(\varepsilon)$. In the other direction,
any injective code must give essentially distinct words to the typical sequences, of which there are
at least $(1-\varepsilon)2^{n(H-\varepsilon)}$, so its rate is at least $H-\varepsilon-O(1/n)$. Letting
$n\to\infty$ and then $\varepsilon\to0$ gives Theorem 7.25.


