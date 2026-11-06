# Law of Large Numbers and the Central Limit Theorem — Solutions

> [Law of Large Numbers and the Central Limit Theorem](README.md) · Solutions to the 36 problems in [exercises.md](exercises.md)

Each solution states the strategy, carries out every significant step, and ends with an independent
check. Proofs are complete. Pitfalls are flagged where a problem is designed to expose one.

## Beginner

**1.** *(Strategy: match the quantifier structure of each statement to the definitions of §5.)*

(a) **In probability**, and correct: this is Definition 5.1 verbatim.

(b) **Almost surely**, and correct: this is Definition 5.2, the probability that the numerical sequence
converges being $1$.

(c) **In distribution**, but *not correct as stated*. The definition requires convergence only at the
points where $F$ is continuous; at an atom the CDFs need not converge. The correct statement is
"$F_n(x)\to F(x)$ for every continuity point $x$ of $F$".

(d) **In distribution**, and correct: this is the portmanteau form of the definition, valid for every
bounded continuous $f$.

*Check:* (a) and (b) involve the joint law of the whole sequence on one space; (c) and (d) involve only
the one-dimensional laws. That is precisely the distinction between the first two modes and the third.

**2.** *(Strategy: Chebyshev applied to $\bar X_n$; the variance of the average is $\sigma^{2}/n$.)*

(a) For one roll $\mu=3.5$ and $\sigma^{2}=\frac{1}{6}(1+4+9+16+25+36)-3.5^{2}=\frac{91}{6}-\frac{49}{4}=\frac{35}{12}=2.9167$.

(b) $\operatorname{Var}(\bar X_n)=\frac{35/12}{2000}=0.0014583$, so

$$\Pr(\lvert\bar X_n-3.5\rvert\ge0.3)\le\frac{0.0014583}{0.09}=0.01620.$$

(c) At $n=8000$ the variance is four times smaller, so the bound is $0.004051$: quadrupling $n$ quarters
the bound, because it is proportional to $1/n$.

*Check:* the bound exceeds the CLT estimate by a large factor, as always, but it is below $1$ and hence
informative; the exact probability is astronomically small. The scaling $4\times$ in $n$ giving $4\times$
smaller bound is the $1/(n\varepsilon^{2})$ law.

**3.** *(Strategy: standardise with the corrected endpoints.)*

Here $np=32$ and $\sqrt{npq}=\sqrt{64\cdot\tfrac12\cdot\tfrac12}=4$.

(a) $\Pr(S\le40)\approx\Phi\bigl(\frac{40.5-32}{4}\bigr)=\Phi(2.125)=0.98321$.

(b) Without the correction, $\Phi\bigl(\frac{40-32}{4}\bigr)=\Phi(2)=0.97725$.

(c) The exact value is $0.983617$. The corrected error is $0.00041$; the uncorrected error is $0.00637$,
about $16$ times larger.

*Check:* both approximations are on the correct side of the exact value and both errors decrease with $n$;
the correction is worth roughly one decimal digit at this $n$.

**4.** *(Strategy: $\mu=20$, $\sigma=\sqrt{12}$, corrected endpoint $24.5$.)*

(a) $\Pr(S\ge25)\approx1-\Phi\bigl(\frac{24.5-20}{\sqrt{12}}\bigr)=1-\Phi(1.2985)=1-0.90303=0.09697$.

(b) Without the correction, $1-\Phi\bigl(\frac{25-20}{\sqrt{12}}\bigr)=1-\Phi(1.4434)=0.07445$.

(c) The exact value is $0.097807$. The corrected error is $0.00084$, the uncorrected error $0.02335$ —
a factor of $28$. The corrected approximation is better.

*Check:* the exact probability is close to $10\%$, and the uncorrected approximation understates it by a
quarter of its value; omitting the correction biases $\Pr(S\ge k)$ downward when $k$ is above the mean,
since the bar at $k$ extends below $k$.

**5.** *(Strategy: De Moivre–Laplace, then solve the margin-of-error inequality.)*

(a) With $\hat p_n=S_n/n$, the theorem states
$\dfrac{\hat p_n-p}{\sqrt{p(1-p)/n}}\xrightarrow{d}\mathcal{N}(0,1)$. For $p=\tfrac12$ this is
$2\sqrt n\bigl(\hat p_n-\tfrac12\bigr)\xrightarrow{d}\mathcal{N}(0,1)$.

(b) The $95\%$ margin is $1.96\sqrt{0.25/n}=0.98/\sqrt n$. Requiring $0.98/\sqrt n\le0.01$ gives
$\sqrt n\ge98$, i.e. $n\ge9604$.

(c) Requiring $0.98/\sqrt n\le0.05$ gives $\sqrt n\ge19.6$, i.e. $n\ge385$ (since $19.6^{2}=384.16$).

*Check:* $9604/385=24.9\approx25=(0.05/0.01)^{2}$, as the $\sqrt n$ scaling requires. ✓

**6.** *(Strategy: the standard error is $\sigma/\sqrt n$; standardise.)*

(a) $\sigma/\sqrt n=5/20=0.25$.

(b) $\Pr(\lvert\bar X_n-\mu\rvert\le0.5)\approx2\Phi\bigl(\frac{0.5}{0.25}\bigr)-1=2\Phi(2)-1=0.9545$.

(c) Halving the standard error requires quadrupling $n$: $n=1600$, since $5/\sqrt{1600}=0.125$.

*Check:* the answer to (b) is the familiar $95\%$ coverage, which is exactly why $1.96\approx2$ standard
errors is the conventional interval. At $n=400$ one half-unit is two standard errors.

**7.** *(Strategy: check i.i.d., finite mean and $0<\sigma^{2}<\infty$.)*

(a) Bernoulli$(0.3)$: **yes**; $\sigma^{2}=0.21$.

(b) Poisson$(4)$: **yes**; $\sigma^{2}=4$.

(c) Standard Cauchy: **no**; even the mean does not exist, so there is no $\mu$ to centre at and no finite
$\sigma$.

(d) Pareto with $\alpha=1.5$: **no**; the mean is finite ($\alpha>1$) but the variance is infinite
($\alpha<2$), so no normal limit with $\sqrt n$ scaling.

(e) Uniform$[0,1]$: **yes**; $\sigma^{2}=1/12$.

(f) $X_n=\pm2^{n}$: **no**; the variables are not identically distributed, and the Lindeberg condition
fails because the $n$-th term dominates the sum.

*Check:* the three "yes" cases are exactly those with a finite second moment and identical distributions;
(f) shows that identical distributions are not the only requirement — the Lindeberg condition matters when
the variances grow.

**8.** *(Strategy: compare a distribution-free bound with a distribution-specific estimate.)*

(a) $\operatorname{Var}(\bar X_{100})=\frac{35/12}{100}=0.029167$, so Chebyshev gives
$\Pr(\lvert\bar X_{100}-3.5\rvert\ge0.1)\le0.029167/0.01=2.917$. A probability cannot exceed $1$, so the
bound is vacuous.

(b) The standard error is $\sqrt{0.029167}=0.17078$, so $0.1$ is $0.5855$ standard errors and the estimate
is $2(1-\Phi(0.5855))=2(0.279106)=0.5582$.

(c) Chebyshev must hold for the worst distribution with that variance, and the worst case puts mass far
from the mean; with $100$ observations the CLT applies and shows the deviation is a fraction of a single
standard error, which is a typical event, not a rare one.

*Check:* the CLT value $0.558$ is close to $1/2$, plausible because $0.1$ is a small fraction of the
standard error $0.171$; and Chebyshev's bound exceeding $1$ is a clear signal that $n$ is too small for it
to be useful at this threshold.

**9.** *(Strategy: mean $1/\lambda$, variance $1/\lambda^{2}$, standard error $\sigma/\sqrt n$.)*

(a) $\mathbb{E}[X_i]=1/2$ and $\operatorname{Var}(X_i)=1/4$.

(b) $\sigma/\sqrt n=0.5/5=0.1$.

(c) $\Pr(\bar X_{25}\le0.6)\approx\Phi\bigl(\frac{0.6-0.5}{0.1}\bigr)=\Phi(1)=0.8413$.

*Check:* the median of $\bar X_{25}$ is slightly below its mean because the sum of exponentials is
right-skewed; the CLT ignores the skew, so $0.8413$ is an approximation whose error is of order
$1/\sqrt{25}=0.2$ times the skewness correction. The exact value from a Gamma$(25,25)$ law is about
$0.843$, so the error is small here.

**10.** *(Strategy: deterministic sequences converge in every sense, and the limit law is degenerate.)*

(a) For every $\varepsilon>0$ and every $n>1/\varepsilon$ we have $\lvert X_n\rvert=1/n<\varepsilon$, so
$\Pr(\lvert X_n\rvert\ge\varepsilon)=0$ for all large $n$: convergence in probability. The numerical
sequence $1/n\to0$ for every $\omega$, so the set of convergence has probability $1$: almost sure
convergence. The CDF of $X_n$ is $F_n(x)=0$ for $x<1/n$ and $1$ for $x\ge1/n$; for $x<0$ it is $0$, and
for $x>0$ it is $1$ once $n>1/x$. So $F_n(x)\to F(x)$ for every $x\ne0$.

(b) The limit law is the point mass $\delta_0$ at $0$, whose CDF is $0$ for $x<0$ and $1$ for $x\ge0$.
Convergence holds at every $x\ne0$: for $x<0$ both sides are $0$, and for $x>0$ we have $1/n<x$ once $n>1/x$,
so $F_n(x)=1=F(x)$. At the atom $x=0$ it fails, since $F_n(0)=\Pr(1/n\le0)=0$ for every $n$ while
$F(0)=1$ — exactly the exception built into Definition 5.3.

(c) For $X_n=n$, for any fixed $\varepsilon$ we have $\Pr(\lvert X_n\rvert\ge\varepsilon)=1$ for all $n$,
so there is no convergence in probability and none almost surely. Nor is there convergence in
distribution: $F_n(x)=0$ for all $n>x$, so $F_n(x)\to0$ for every fixed $x$, and the limit is not a CDF.
The mass escapes to infinity.

*Check:* (a)–(b) illustrate that convergence in distribution is blind to dependence and to path
behaviour; (c) shows that a sequence can fail every mode, and that "convergence in distribution" requires
a proper limit law.

**11.** *(Strategy: $\mu=168$, $\sigma=\sqrt{140}$, continuity correction at $199.5$.)*

$\mathbb{E}[S]=48(3.5)=168$ and $\operatorname{Var}(S)=48(35/12)=140$, so $\sigma=11.832$. Then

$$\Pr(S\ge200)\approx1-\Phi\Bigl(\frac{199.5-168}{11.832}\Bigr)=1-\Phi(2.663)=1-0.996128=0.003872.$$

*Check:* the exact value, computed by convolving the die distribution 48 times, is $0.003732$, so the
relative error is $3.7\%$. Without the correction the estimate would be
$1-\Phi(2.704)=0.00343$, which is worse.

## Intermediate

**12.** *(Strategy: compare the two boundary corrections over a wide interval.)*

Exact: $\Pr(40\le S\le60)=0.964800$. With the correction,

$$\Phi\Bigl(\frac{60.5-50}{5}\Bigr)-\Phi\Bigl(\frac{39.5-50}{5}\Bigr)=\Phi(2.1)-\Phi(-2.1)=0.964271,$$

an error of $0.000529$. Without the correction,
$\Phi(2)-\Phi(-2)=0.954500$, an error of $0.010300$.

The correction improves the answer by a factor of about $19$, whereas for $[45,55]$ the improvement was
by a factor of about $580$. The reason is that the correction moves each endpoint by half a unit, which
changes the approximated probability by roughly $\tfrac12\phi(z)/\sigma$ per endpoint. For $[45,55]$,
$z=\pm1.1$ and $\phi(1.1)=0.218$, so the shift is worth about $0.022$ per endpoint; for $[40,60]$,
$z=\pm2$ and $\phi(2)=0.054$, four times smaller.

*Check:* the errors $0.00053$ and $0.0103$ are both $O(1/\sqrt n)$ with $n=100$, i.e. of order $0.01$;
that is exactly the Berry–Esseen scale. The two-error comparison confirms that the correction is most
valuable where the density is largest.

**13.** *(Strategy: standardise and compare with the exact Gamma probability.)*

(a) $\bar X_{100}$ has mean $1$ and standard error $1/\sqrt{100}=0.1$, so the CLT gives
$\Phi\bigl(\frac{1.2-1}{0.1}\bigr)=\Phi(2)=0.97725$ against the exact $0.97214$; the error is
$-0.00511$.

(b) At $n=400$ the standard error is $0.05$, so the approximation is $\Phi(4)=0.999968$ against the exact
$0.999921$; the error is $-0.0000476$.

(c) The error fell by a factor of $107$. Berry–Esseen only promises a factor of $2$ (from $1/\sqrt n$),
because the two calculations are at *different* standardised points ($z=2$ and $z=4$). At a fixed $z$ the
error does halve when $n$ quadruples; the Edgeworth correction
$\frac{\rho}{6\sigma^{3}\sqrt n}(1-z^{2})\phi(z)$ gives $-0.0065$ at $(z,n)=(2,100)$ and $-8.1\times10^{-5}$
at $(4,100)$, and $-4.0\times10^{-5}$ at $(4,400)$ — the last two differ by exactly the factor $2$. The
improvement from (a) to (b) is mostly due to the smaller density at $z=4$.

*Check:* the Edgeworth predictions $-0.0065$ and $-0.000040$ match the observed errors $-0.0051$ and
$-0.0000476$ in sign and magnitude, confirming that the leading error is the skewness term.

**14.** *(Strategy: two variables with the same law need not be close.)*

(a) $X_n=-X$ takes the values $\pm1$ with probability $\tfrac12$ each, exactly as $X$ does. Hence
$F_{X_n}=F_X$ for every $n$ and trivially $F_{X_n}(x)\to F_X(x)$ everywhere.

(b) $\Pr(\lvert X_n-X\rvert\ge\tfrac12)=\Pr(\lvert-2X\rvert\ge\tfrac12)=\Pr(\lvert X\rvert\ge\tfrac14)=1$
for every $n$, so the probability does not tend to $0$: no convergence in probability to $X$.

(c) Since $X_n=-X$ for every $n$, the sequence is constant and converges in probability to its own value
$-X$; that is a different limit, and it shows that a probability limit, when it exists, is unique
(Exercise 22).

*Check:* $X$ and $-X$ have the same law, so every distributional statement about them coincides; but as
random variables on the same space they disagree everywhere. This is the cleanest example of the gap
between $\xrightarrow{d}$ and $\xrightarrow{p}$.

**15.** *(Strategy: one direction is Theorem 7.5; the other is a contradiction argument.)*

*($\Rightarrow$)* If $X_n\xrightarrow{p}X$, every subsequence $(X_{n_k})$ also converges in probability
to $X$ (the same tail bounds apply). Theorem 7.5 applied to that subsequence produces a further
subsequence converging almost surely.

*($\Leftarrow$)* Suppose $X_n$ does not converge to $X$ in probability. Then there are
$\varepsilon,\delta>0$ and infinitely many $n$ with $\Pr(\lvert X_n-X\rvert\ge\varepsilon)\ge\delta$.
Enumerate those indices as $n_1<n_2<\cdots$. By hypothesis this subsequence has a further subsequence
$n_{k_j}$ converging almost surely to $X$; by Theorem 7.2 it also converges in probability to $X$, so
$\Pr(\lvert X_{n_{k_j}}-X\rvert\ge\varepsilon)\to0$, contradicting the lower bound $\delta>0$. Hence
$X_n\xrightarrow{p}X$. $\blacksquare$

*Check:* the statement is a useful criterion: it converts a statement about probabilities into one about
almost sure convergence along subsequences, which is often easier to verify with Borel–Cantelli.

**16.** *(Strategy: compute the moments, then see which theorem's hypotheses hold.)*

(a) $\mathbb{E}[X]=\int_1^\infty x\cdot\frac32x^{-5/2}dx=\frac32\int_1^\infty x^{-3/2}dx=\frac32\cdot2=3$.
And $\mathbb{E}[X^{2}]=\frac32\int_1^\infty x^{-1/2}dx=\infty$, so the variance is infinite.

(b) Yes: Khinchin's weak law (Theorem 7.9) needs only $\mathbb{E}\lvert X\rvert<\infty$, and
$\bar X_n\xrightarrow{p}3$.

(c) The Chebyshev proof of §7.2 uses $\operatorname{Var}(\bar X_n)=\sigma^{2}/n$ and then bounds
$\sigma^{2}/(n\varepsilon^{2})$; with $\sigma^{2}=\infty$ the bound is infinite and asserts nothing. The
conclusion of the theorem remains true here, but this proof cannot reach it.

*Check:* the exact tail $\Pr(X>t)=t^{-3/2}$ for $t\ge1$ satisfies $t\Pr(X>t)=t^{-1/2}\to0$, so the mean is
finite; and $t^{2}\Pr(X>t)=t^{1/2}\to\infty$, which is the signature of an infinite second moment.

**17.** *(Strategy: $\rho=p(1-p)^{3}+(1-p)p^{3}$.)*

For $p=0.1$: $\rho=0.1(0.9)^{3}+0.9(0.1)^{3}=0.0729+0.0009=0.0738$. Also $\sigma^{2}=0.09$, so $\sigma=0.3$
and $\sigma^{3}=0.027$. The bound at $n=100$ is

$$\frac{C\rho}{\sigma^{3}\sqrt n}=\frac{0.4748(0.0738)}{0.027(10)}=\frac{0.03504}{0.27}=0.1298.$$

*Check:* at $n=100$ the bound is $0.1298$, larger than the $0.0950$ obtained for $p=\tfrac12$: although
the third central moment is much smaller ($0.0738$ against $0.25$), the cube of the standard deviation is
smaller still ($0.027$ against $0.125$), so the ratio $\rho/\sigma^{3}=2.733$ exceeds $2$. Skewness, not
the absolute size of the third moment, is what enters.

**18.** *(Strategy: $n=(\sigma/\text{se})^{2}$ and $n=(z\sigma/\text{half-width})^{2}$.)*

(a) $n=(2/0.05)^{2}=1600$.

(b) $n=(1.96\cdot2/0.1)^{2}=39.2^{2}=1536.6$, so $n=1537$.

(c) Accuracy depends on $\sigma$ and $n$ only, through $\sigma/\sqrt n$; doubling the cost per sample does
not change the required $n$, but with a fixed budget it halves the affordable $n$ and so multiplies the
error by $\sqrt2$. The economical response is variance reduction — lowering $\sigma$ — since
$\sigma/\sqrt n$ improves linearly in $\sigma$ but only as the square root in $n$.

*Check:* $1537<1600$, as it must be: a $95\%$ interval with half-width $0.1$ corresponds to exactly
$1.96$ standard errors, i.e. a standard error of $0.051$, slightly larger than $0.05$.

**19.** *(Strategy: think of the mass at $k$ as an interval of length $1$.)*

(a) Adding $\tfrac12$ increases the numerator, hence increases $z$ and $\Phi(z)$: the approximated value of
$\Pr(S\le k)$ **increases**.

(b) $\Pr(S\le k)$ is the total mass of the bars at $0,1,\dots,k$. Each bar at $j$ occupies
$[j-\tfrac12,j+\tfrac12)$, so the mass up to and including $k$ fills the interval up to $k+\tfrac12$. The
normal approximation should therefore integrate the density up to $k+\tfrac12$.

(c) For $k>np$ the correction also increases $z$ and hence the value. This is still correct: the
interval $(-\infty,k+\tfrac12]$ includes the whole bar at $k$, whose upper half lies above $k$. So the
correction always pushes the CDF approximation up, and its size is governed by the density at the
endpoint.

*Check:* numerically for Bin$(100,\tfrac12)$ and $k=60$: uncorrected $\Phi(2)=0.9772$, corrected
$\Phi(2.1)=0.9821$, exact $0.9824$. The correction moves the approximation in the right direction. ✓

**20.** *(Strategy: the lattice has span $2$, so each atom owns an interval of length $2$.)*

(a) $S=10$ requires exactly five of the ten variables to equal $2$: $\Pr(S=10)=\binom{10}{5}2^{-10}=252/1024=0.246094$.

(b) $\mathbb{E}[S]=10$ and $\operatorname{Var}(S)=10$, so $\sigma=3.1623$. The width-$1$ correction gives

$$\Phi\Bigl(\frac{10.5-10}{3.1623}\Bigr)-\Phi\Bigl(\frac{9.5-10}{3.1623}\Bigr)=2\Phi(0.1581)-1=0.12563,$$

about half the true value.

(c) With span $2$ the local limit theorem reads $\Pr(S=k)\approx\frac{2}{\sigma\sqrt n}\phi(z)$, giving
$\frac{2}{3.1623}(0.398942)=0.252313$, which is close to $0.246094$.

The discrepancy in (b) is exactly the factor of $2$: the bar at $10$ has width $2$, not $1$, so using a
unit-wide bar halves the estimated mass. The CDF-level CLT still holds; it is the local (mass-level)
approximation that needs the correct span.

*Check:* $0.2523/0.2461=1.025$, a $2.5\%$ error, while (b) is off by $49\%$. This is why a continuity
correction must use half the lattice span.

**21.** *(Strategy: expand the variance of the average into variances and covariances.)*

(a) By Corollary 7.15 of the previous topic,

$$\operatorname{Var}(\bar Y_n)=\frac{1}{n^{2}}\Bigl(\sum_{i=1}^{n}\operatorname{Var}(Y_i)+2\sum_{i<j}\operatorname{Cov}(Y_i,Y_j)\Bigr)=\frac{1}{n^{2}}\bigl(n+2\tbinom n2\rho\bigr)=\frac1n+\Bigl(1-\frac1n\Bigr)\rho.$$

(b) At $n=100$: $0.01+0.99(0.5)=0.01+0.495=0.505$. The limit as $n\to\infty$ is $\rho=0.5$.

(c) The variance does not tend to $0$, so $\bar Y_n$ does not concentrate: there is no law of large
numbers for $\mu$, and $\bar Y_n$ retains a random limit with variance $\rho\sigma^{2}$. Only the
"idiosyncratic" part $1/n$ averages out; the common part does not.

*Check:* the formula reduces correctly at $\rho=0$ (giving $1/n$) and at $\rho=1$ (giving $1$, the case
$Y_i=Y_1$). For $\rho=0.5$ the asymptotic standard deviation is $0.707$, not $0$.

**22.** *(Strategy: the union bound and a limiting argument over $\varepsilon=1/m$.)*

For any $\varepsilon>0$, $\lvert X-Y\rvert\le\lvert X-X_n\rvert+\lvert X_n-Y\rvert$, so

$$\Pr(\lvert X-Y\rvert\ge\varepsilon)\le\Pr\bigl(\lvert X-X_n\rvert\ge\tfrac\varepsilon2\bigr)+\Pr\bigl(\lvert X_n-Y\rvert\ge\tfrac\varepsilon2\bigr)\longrightarrow0+0=0.$$

Hence $\Pr(\lvert X-Y\rvert\ge1/m)=0$ for every $m$, and by countable subadditivity
$\Pr(X\ne Y)=\Pr\bigl(\bigcup_m\{\lvert X-Y\rvert\ge1/m\}\bigr)\le\sum_m0=0$. So $\Pr(X=Y)=1$.
$\blacksquare$

*Check:* the same argument works for almost sure limits and for $L^{1}$ limits; in each case the limit is
unique in the appropriate sense (a.s. equality, or equality in norm).

**23.** *(Strategy: for i.i.d. variables the Lindeberg ratio is a single expectation.)*

With $s_n^{2}=n\sigma^{2}$, the Lindeberg sum is $n\,\mathbb{E}\bigl[(X_1-\mu)^{2}\mathbf{1}_{\{\lvert X_1-\mu\rvert>\varepsilon\sigma\sqrt n\}}\bigr]$,
so the ratio is

$$\frac{1}{\sigma^{2}}\mathbb{E}\Bigl[(X_1-\mu)^{2}\mathbf{1}_{\{\lvert X_1-\mu\rvert>\varepsilon\sigma\sqrt n\}}\Bigr].$$

As $n\to\infty$ the indicator decreases to $0$ pointwise (since $\sqrt n\to\infty$), and
$(X_1-\mu)^{2}$ is integrable, so dominated convergence gives the limit $0$. $\blacksquare$

*Check:* no independence between different $i$ was used here — the Lindeberg condition is about the size
of individual terms relative to the total, and for identically distributed summands it is automatic once
the second moment is finite. This is why Theorem 5.8 needs no extra hypothesis.

## Advanced

**24.** *(Strategy: only the variance of the sum is needed, and pairwise uncorrelatedness makes the cross terms vanish.)*

By linearity $\mathbb{E}[\bar X_n]=\frac1n\sum_{i\le n}\mu=\mu$. Since the variables are pairwise
uncorrelated, $\operatorname{Cov}(X_i,X_j)=0$ for $i\ne j$, so

$$\operatorname{Var}(\bar X_n)=\frac{1}{n^{2}}\sum_{i=1}^{n}\operatorname{Var}(X_i)\le\frac{n\sigma^{2}}{n^{2}}=\frac{\sigma^{2}}{n}.$$

Chebyshev gives $\Pr(\lvert\bar X_n-\mu\rvert\ge\varepsilon)\le\sigma^{2}/(n\varepsilon^{2})\to0$.
$\blacksquare$

*Check:* neither identical distributions nor independence were used; only $\mathbb{E}[X_i]=\mu$ and a
uniform variance bound. The price is that the bound is not sharp, but the conclusion is the same.

**25.** *(Strategy: centre, expand the fourth power, keep only the terms that survive independence.)*

Assume first $\mu=0$; write $\sigma^{2}=\mathbb{E}[X_1^{2}]$ and $M=\mathbb{E}[X_1^{4}]$. Expanding,

$$S_n^{4}=\sum_iX_i^{4}+4\sum_{i\ne j}X_i^{3}X_j+6\sum_{i<j}X_i^{2}X_j^{2}+12\!\!\sum_{i<j<k}\!\!X_i^{2}X_jX_k+24\!\!\sum_{i<j<k<\ell}\!\!X_iX_jX_kX_\ell.$$

Every term in which some index appears exactly once has expectation $0$, because the variables are
independent and centred. The survivors are $\sum_iX_i^{4}$ (expectation $nM$) and
$6\sum_{i<j}X_i^{2}X_j^{2}$ (expectation $6\binom n2\sigma^{4}=3n(n-1)\sigma^{4}$). Hence

$$\mathbb{E}[S_n^{4}]=nM+3n(n-1)\sigma^{4}\le nM+3n^{2}\sigma^{4}.$$

Markov's inequality on the non-negative variable $S_n^{4}$ gives, for $\varepsilon>0$,

$$\Pr(\lvert S_n\rvert\ge n\varepsilon)=\Pr(S_n^{4}\ge n^{4}\varepsilon^{4})\le\frac{nM+3n^{2}\sigma^{4}}{n^{4}\varepsilon^{4}}=\frac{M}{n^{3}\varepsilon^{4}}+\frac{3\sigma^{4}}{n^{2}\varepsilon^{4}}.$$

Since $\sum_nn^{-2}<\infty$, Borel–Cantelli (Lemma 7.1(i)) gives
$\Pr(\lvert S_n\rvert\ge n\varepsilon\text{ i.o.})=0$: almost surely $\lvert S_n\rvert<n\varepsilon$ for
all sufficiently large $n$, and since $\varepsilon$ is arbitrary, $S_n/n\to0$ a.s.

For general $\mu$, apply the result to $X_i-\mu$ (which has fourth moment finite by the inequality
$\lvert x-\mu\rvert^{4}\le8(\lvert x\rvert^{4}+\lvert\mu\rvert^{4})$) and add back
$\frac1n\sum_{i\le n}\mu=\mu$. $\blacksquare$

*Check:* the two surviving families are exactly those in which every index is repeated; the count
$6\binom n2=3n(n-1)$ is the check that no term is missed.

**26.** *(Strategy: sandwich the CDF of the sum between shifted CDFs of $X_n$, then use that
$Y_n\to c$ in probability.)*

Let $x$ be a continuity point of the CDF of $X+c$. Fix $\delta>0$ and note the two implications

$$\{X_n+Y_n\le x\}\subseteq\{X_n\le x-c+\delta\}\cup\{\lvert Y_n-c\rvert>\delta\},$$

$$\{X_n\le x-c-\delta\}\subseteq\{X_n+Y_n\le x\}\cup\{\lvert Y_n-c\rvert>\delta\}.$$

Hence

$$F_{X_n}(x-c-\delta)-a_n\le\Pr(X_n+Y_n\le x)\le F_{X_n}(x-c+\delta)+a_n,\qquad a_n=\Pr(\lvert Y_n-c\rvert>\delta).$$

Because $x-c\pm\delta$ can be chosen as continuity points of the limit law and $X_n\xrightarrow{d}X$, the
two outer CDFs converge to $F_X(x-c-\delta)$ and $F_X(x-c+\delta)$; also $a_n\to0$. Letting $n\to\infty$
and then $\delta\downarrow0$ gives $\Pr(X_n+Y_n\le x)\to F_X(x-c)$. $\blacksquare$

The hypothesis that the limit is a **constant** is used twice: to write the target CDF as a *shift* of
$F_X$, and to have $Y_n\to c$ in probability at all. For a non-degenerate limit $Y$, convergence in
distribution of $X_n$ and $Y_n$ separately gives no information about $X_n+Y_n$ without a joint
convergence assumption.

*Check:* the argument also shows why $c$ must be deterministic: if $Y_n\xrightarrow{d}Y$ independently
of $X_n$, the sum's limit is the convolution of the two laws, not a shift of $F_X$.

**27.** *(Strategy: approximate $f$ by a step function built on continuity points of $F$.)*

(a) Let $\lvert f\rvert\le B$ and let $\omega(\delta)=\sup\{\lvert f(x)-f(y)\rvert:\lvert x-y\rvert\le\delta\}$
be its modulus of continuity, which tends to $0$ as $\delta\downarrow0$ by uniform continuity. Fix
$\delta>0$ and choose $a<b$ that are continuity points of $F$ with $F(a)<\delta$ and $1-F(b)<\delta$, and a
partition $a=x_0<x_1<\cdots<x_m=b$ of continuity points of $F$ with mesh below $\delta$. Define the step
function $s=\sum_{i=1}^{m}f(x_i)\mathbf{1}_{(x_{i-1},x_i]}$, so $\lvert f-s\rvert\le\omega(\delta)$
uniformly on $(a,b]$, and both are bounded by $B$ elsewhere. Then

$$\bigl\lvert\mathbb{E}[f(X_n)]-\mathbb{E}[f(X)]\bigr\rvert\le2\omega(\delta)+2B\delta+\Bigl\lvert\sum_{i=1}^{m}f(x_i)\bigl(F_n(x_i)-F_n(x_{i-1})-F(x_i)+F(x_{i-1})\bigr)\Bigr\rvert,$$

and the last sum tends to $0$ because $F_n\to F$ at each $x_i$. Taking $n\to\infty$ and then
$\delta\downarrow0$ gives the claim. $\blacksquare$

(b) Take $X_n=n$ with probability $1/n$ and $0$ otherwise; then $X_n\xrightarrow{d}0$ (Exercise 29), and
$f(x)=x$ is continuous and unbounded. Then $\mathbb{E}[f(X_n)]=n\cdot\frac1n=1$ for every $n$, which does
not tend to $f(0)=0$.

*Check:* this is exactly the failure of uniform integrability, and it is why the portmanteau theorem pairs
"bounded" with "continuous". Boundedness of $f$ is not merely convenient: without it, mass escaping to
infinity can carry a fixed expectation.

**28.** *(Strategy: Stirling on the binomial coefficient and a Taylor expansion of the Kullback–Leibler
divergence.)*

Write $k=k_n=np+z\sqrt{npq}$ and $q=1-p$. Stirling gives

$$\binom nk\sim\frac{1}{\sqrt{2\pi}}\sqrt{\frac{n}{k(n-k)}}\;\frac{n^{n}}{k^{k}(n-k)^{n-k}},$$

so, with $x=k/n$,

$$\Pr(S_n=k)=\binom nk p^{k}q^{n-k}\sim\frac{1}{\sqrt{2\pi n\,x(1-x)}}\exp\bigl(-nD(x\,\Vert\,p)\bigr),$$

where $D(x\Vert p)=x\ln\frac xp+(1-x)\ln\frac{1-x}{q}$ is the Kullback–Leibler divergence. Here
$x=p+\delta$ with $\delta=z\sqrt{pq/n}\to0$. Since $D(p\Vert p)=0$,
$D'(x\Vert p)=\ln\frac{x}{p}-\ln\frac{1-x}{q}$ vanishes at $x=p$, and
$D''(x\Vert p)=\frac1x+\frac1{1-x}$ equals $\frac1{pq}$ at $x=p$, Taylor's theorem gives

$$D(p+\delta\,\Vert\,p)=\frac{\delta^{2}}{2pq}+O(\delta^{3})=\frac{z^{2}}{2n}+O(n^{-3/2}),$$

so $nD\to z^{2}/2$. Also $x(1-x)\to pq$. Therefore

$$\Pr(S_n=k_n)\sim\frac{1}{\sqrt{2\pi npq}}e^{-z^{2}/2}. \qquad\blacksquare$$

*Check:* summing over $z$ in steps of $1/\sqrt{npq}$ turns the sum into a Riemann sum for the standard
normal density, recovering the CDF-level CLT. And for $z=0$ the formula is $1/\sqrt{2\pi npq}$, matching
the local limit value used in Example 9.3: $1/(5\sqrt{2\pi})=0.079577$.

**29.** *(Strategy: a small probability of a huge value gives convergence in distribution but not in mean.)*

(a) For $\varepsilon>0$ and $n>\varepsilon$, $\Pr(\lvert X_n\rvert\ge\varepsilon)=\Pr(X_n=n)=1/n\to0$:
convergence in probability, hence in distribution, to $0$.

(b) $\mathbb{E}[X_n]=n\cdot\frac1n+0\cdot\bigl(1-\frac1n\bigr)=1$ for every $n$; the expectations do not
converge to $0$.

(c) One needs **uniform integrability** of the family $\{X_n\}$ (equivalently, tightness plus domination by
an integrable variable). Here $\sup_n\mathbb{E}\bigl[X_n\mathbf{1}_{\{X_n>K\}}\bigr]=1$ for every $K$,
because taking $n>K$ leaves the whole mass of $X_n$ above $K$. If the family were uniformly integrable,
convergence in probability would imply $\mathbb{E}[X_n]\to\mathbb{E}[X]$.

*Check:* the variance is $\mathbb{E}[X_n^{2}]-1=n-1\to\infty$, which is another symptom of the same
failure: the second moment is not controlled.

**30.** *(Strategy: Taylor-expand $g$ around $\mu$, then treat the linear term with Slutsky.)*

Since $g$ is differentiable at $\mu$, $g(x)=g(\mu)+g'(\mu)(x-\mu)+r(x)$ with
$r(x)/(x-\mu)\to0$ as $x\to\mu$. Then

$$\sqrt n\bigl(g(\bar X_n)-g(\mu)\bigr)=g'(\mu)\sqrt n(\bar X_n-\mu)+\sqrt n\,r(\bar X_n).$$

The first term converges in distribution to $\mathcal{N}(0,\sigma^{2}g'(\mu)^{2})$ by the CLT and
Theorem 7.28 of the previous topic (scaling a normal limit by the constant $g'(\mu)$). For the second,
write $\sqrt n\,r(\bar X_n)=\dfrac{r(\bar X_n)}{\bar X_n-\mu}\cdot\sqrt n(\bar X_n-\mu)$ on the event
$\bar X_n\ne\mu$; the first factor tends to $0$ in probability because $\bar X_n\to\mu$ in probability
and $r(x)/(x-\mu)\to0$, while $\sqrt n(\bar X_n-\mu)=O_p(1)$ by the CLT. Hence the second term is $o_p(1)$.
Slutsky's theorem (Exercise 26) then gives the stated limit. $\blacksquare$

Taylor's theorem supplies the linearisation; Slutsky's theorem lets the $o_p(1)$ remainder be discarded;
$g'(\mu)\ne0$ ensures the limiting variance is positive, so the limit is a genuine non-degenerate normal
law.

*Check:* with $g(x)=x^{2}$ and $X_i\sim\text{Poisson}(\lambda)$, $g'(\lambda)=2\lambda$, so
$\sqrt n(\bar X_n^{2}-\lambda^{2})\xrightarrow{d}\mathcal{N}(0,4\lambda^{3})$; the variance
$\sigma^{2}g'(\mu)^{2}=\lambda(2\lambda)^{2}=4\lambda^{3}$ matches a direct delta-method computation. ✓

**31.** *(Strategy: the CLT controls the whole distribution, so it implies concentration; the converse
fails for infinite variance.)*

(a) From $Z_n\xrightarrow{d}\mathcal{N}(0,1)$, for any $\eta>0$ there is $M$ with
$\sup_n\Pr(\lvert Z_n\rvert>M)<\eta$. (Convergence in distribution makes the sequence tight: choose $M$
with $\Phi(M)-\Phi(-M)>1-\eta$ and use convergence at $\pm M$.) Then for $\delta>0$,

$$\Pr(\lvert\bar X_n-\mu\rvert\ge\delta)=\Pr\Bigl(\lvert Z_n\rvert\ge\frac{\delta\sqrt n}{\sigma}\Bigr)\le\Pr(\lvert Z_n\rvert>M)<\eta$$

once $\delta\sqrt n/\sigma>M$. Hence $\bar X_n\xrightarrow{p}\mu$. $\blacksquare$

(b) Take $X_i$ Pareto with $\alpha=\tfrac32$ (Exercise 16): the mean is finite, so Khinchin's weak law
gives $\bar X_n\xrightarrow{p}3$. But $\operatorname{Var}(X_i)=\infty$. If a CLT held in the form
$(S_n-3n)/(\sigma\sqrt n)\xrightarrow{d}\mathcal{N}(0,1)$, Feller's converse (stated in §7.4) would force
$\mathbb{E}[X_1^{2}]<\infty$ and $a_n\sim\sigma\sqrt n$, a contradiction. The actual limit of suitably
normalised sums is a stable law with index $\tfrac32$, whose fluctuations are of order $n^{2/3}$.

(c) The CLT is strictly stronger: it implies the weak law (part (a)) but is not implied by it (part (b)).
So a proof of convergence of averages says nothing about the shape of the fluctuations.

*Check:* the density of fluctuations differs sharply: $\sqrt n$ versus $n^{2/3}$, and the limit law is
heavy-tailed. Using a normal interval on such data understates the error at large $n$.

## Challenge

**32.** *(Strategy: at the mean, symmetry turns the CDF gap into half the central mass, which Stirling
computes.)*

(a) For $n=2m$ with $p=\tfrac12$, $Z_n=(S_n-m)/\sqrt{m/2}$, so $Z_n\le0\iff S_n\le m$. By symmetry
$\Pr(S_n<m)=\Pr(S_n>m)=\tfrac12\bigl(1-\Pr(S_n=m)\bigr)$, hence

$$\Pr(S_n\le m)=\tfrac12\bigl(1-\Pr(S_n=m)\bigr)+\Pr(S_n=m)=\tfrac12+\tfrac12\Pr(S_n=m),$$

and therefore $F_{Z_n}(0)-\Phi(0)=\tfrac12\Pr(S_n=m)$.

(b) $\Pr(S_{2m}=m)=\binom{2m}{m}4^{-m}$. Stirling's formula gives
$\binom{2m}{m}\sim\frac{4^{m}}{\sqrt{\pi m}}$, so $\Pr(S_{2m}=m)\sim\frac{1}{\sqrt{\pi m}}$ and

$$\sup_x\bigl\lvert F_{Z_n}(x)-\Phi(x)\bigr\rvert\ge F_{Z_n}(0)-\Phi(0)\sim\frac{1}{2\sqrt{\pi m}}=\frac{1}{\sqrt{2\pi n}}\approx\frac{0.3989}{\sqrt n}.$$

(c) Berry–Esseen asserts an upper bound $C\rho/(\sigma^{3}\sqrt n)$ that must hold for *every* law with
the stated moments. The Bernoulli$(\tfrac12)$ law is such a law, and its supremum error is at least
$0.3989/\sqrt n$; hence $C\cdot2\ge0.3989$, i.e. $C\ge0.199$. More to the point, the error cannot decay
faster than $n^{-1/2}$ for this law, so no bound with $n^{-1/2-\varepsilon}$ can hold universally: the
rate in Berry–Esseen is exact. (The sharp constant is larger, about $0.4097$, obtained from a slightly
different two-point example.)

*Check:* the numerical table of Example 9.7 shows errors $0.123,0.088,0.056,0.040,0.028,0.018$ at
$n=10,20,50,100,200,500$, and $0.3989/\sqrt n$ gives $0.126,0.089,0.056,0.040,0.028,0.018$ — agreement to
two digits. This confirms that the lower bound is attained, not merely valid.

**33.** *(Strategy: characteristic functions multiply under independent sums.)*

(a) With $\varphi(t)=e^{-\lvert t\rvert}$,

$$\varphi_{\bar X_n}(t)=\mathbb{E}\bigl[e^{itS_n/n}\bigr]=\prod_{j=1}^{n}\mathbb{E}\bigl[e^{i(t/n)X_j}\bigr]=\bigl[\varphi(t/n)\bigr]^{n}=\bigl[e^{-\lvert t\rvert/n}\bigr]^{n}=e^{-\lvert t\rvert}.$$

(b) The characteristic function $e^{-\lvert t\rvert}$ is that of the standard Cauchy law, and characteristic
functions determine laws, so $\bar X_n$ is standard Cauchy for every $n$. Hence
$\Pr(\lvert\bar X_n\rvert\le1)=\frac{2}{\pi}\arctan1=\frac12$ for every $n$, while convergence in
probability to a constant would force this to tend to $1$. The weak law fails, and with it the strong law.

(c) If $\sigma^{2}<\infty$ the CLT would give $(S_n-n\mu)/(\sigma\sqrt n)\xrightarrow{d}\mathcal{N}(0,1)$.
Here $\mu$ and $\sigma$ do not exist, so the expression is undefined. There is no rescaling by $\sqrt n$
that produces a non-degenerate limit: $S_n$ is Cauchy with scale $n$, so the fluctuations grow like $n$,
not $\sqrt n$, and after dividing by $n$ the law is unchanged. The correct statement is that the
normalised sums with scale $n^{1/\alpha}$ converge to an $\alpha$-stable law, here $\alpha=1$.

*Check:* part (a) uses only that the $X_j$ are independent and identically distributed; no moment
hypothesis is needed, which is the point. And $\varphi_{S_n}(t)=e^{-n\lvert t\rvert}$, the Cauchy law with
scale $n$: the sum spreads out linearly, exactly cancelling the division by $n$.

**34.** *(Strategy: direct computation for fixed $k$, then compare the scales.)*

(a) For fixed $k\le n$,

$$\Pr(S_n=k)=\binom nk\Bigl(\frac\lambda n\Bigr)^{k}\Bigl(1-\frac\lambda n\Bigr)^{n-k}\longrightarrow\frac{\lambda^{k}}{k!}\cdot1\cdot e^{-\lambda},$$

using $\binom nk/n^{k}\to1/k!$ and $\bigl(1-\lambda/n\bigr)^{n-k}\to e^{-\lambda}$.

(b) At $k=0$ the limit is $e^{-\lambda}>0$, a fixed positive number.

(c) There is no contradiction because the two statements describe different scales. The CLT for
$S_n\sim\operatorname{Bin}(n,\lambda/n)$ says that $(S_n-\lambda)/\sqrt{\lambda(1-\lambda/n)}$ is
approximately $\mathcal{N}(0,1)$; this is a statement about intervals whose width is of order $\sqrt n$ in
the original units — but here the whole distribution occupies only a bounded range, so no interval in
$k$ grows with $n$. The Poisson limit is a *local* statement at fixed $k$; the normal approximation is a
statement about standardised intervals. Both are true, and they agree well only when $\lambda$ is large,
where $\operatorname{Pois}(\lambda)$ is itself approximately normal. For $\lambda=1$ the normal
approximation of $\Pr(S_n=0)$ gives $\Phi(-0.5)=0.31$ against $e^{-1}=0.368$, a $15\%$ error, while the
Poisson limit is exact.

*Check:* the means agree: $\mathbb{E}[S_n]=\lambda$ for every $n$ and $\operatorname{Pois}(\lambda)$ has
mean $\lambda$; the variances agree too, since $n\cdot\frac\lambda n\bigl(1-\frac\lambda n\bigr)=\lambda(1-\lambda/n)\to\lambda$.
This is the standard "law of rare events" and the reason the Poisson distribution models counts.

**35.** *(Strategy: the summands have wildly unequal variances, so the Lindeberg condition fails.)*

(a) $G_j$ is geometric with success probability $p_j=j/n$ on $\{1,2,\dots\}$, so
$\operatorname{Var}(G_j)=\frac{1-p_j}{p_j^{2}}=\frac{n(n-j)}{j^{2}}=\frac{n^{2}}{j^{2}}-\frac nj$.
Independence gives

$$\operatorname{Var}(T_n)=\sum_{j=1}^{n}\Bigl(\frac{n^{2}}{j^{2}}-\frac nj\Bigr)=n^{2}\sum_{j=1}^{n}\frac1{j^{2}}-n\sum_{j=1}^{n}\frac1j.$$

As $n\to\infty$, $\sum j^{-2}\to\pi^{2}/6$ and the second term is $n\ln n=o(n^{2})$, so
$\operatorname{Var}(T_n)\sim\frac{\pi^{2}}{6}n^{2}$.

(b) $\operatorname{Var}(G_1)=n(n-1)\sim n^{2}$, while $\operatorname{Var}(T_n)\sim1.645\,n^{2}$: the
single summand $G_1$ (the wait for the last, hardest coupon) carries a fraction
$1/(\pi^{2}/6)=6/\pi^{2}\approx0.608$ of the total variance. No summand is negligible compared with the
sum, which is exactly the negation of the Lindeberg condition.

(c) Because one term dominates, the fluctuations are those of $G_1$ rather than an average of many small
contributions. Centring and scaling by $n$, $(T_n-nH_n)/n$ has a Gumbel-type limit, reflecting
$\max_j G_j$, not a normal one. For small $n$ the number of terms is too small for the CLT to be accurate
in any case — at $n=6$, $\operatorname{Var}(T_6)=38.99$ and $T_6$ is strongly right-skewed — and for large
$n$ the dominance of the final coupon makes the approximation worse rather than better. There is no range
of $n$ in which the normal approximation is reliable at the tails.

*Check:* at $n=6$, the formula gives $36(1.4914)-6(2.45)=53.69-14.70=38.99$, matching the direct sum, and
$\operatorname{Var}(G_1)=30$, i.e. $77\%$ of the total at this small $n$ — the dominance is already
visible.

**36.** *(Strategy: the estimate is a sample mean of indicators, so the LLN gives consistency and the CLT
gives the error bar.)*

(a) Let $I_j=\mathbf{1}_{\{\lvert Z^{(j)}\rvert\le1\}}$, so $\hat p_N=\frac1N\sum_{j\le N}I_j$ is a mean of
i.i.d. Bernoulli$(p)$ variables. Its standard error is

$$\operatorname{se}(\hat p_N)=\sqrt{\frac{p(1-p)}{N}}=\sqrt{\frac{0.6827(0.3173)}{N}}=\sqrt{\frac{0.21662}{N}}.$$

(b) Requiring $\sqrt{0.21662/N}\le0.005$ gives $N\ge0.21662/0.000025=8665$; so $N=8665$ (round up).

(c) Yes, the estimate is consistent in $N$: by the law of large numbers, $\hat p_N$ converges almost surely
to $\Pr(\lvert Z^{(1)}\rvert\le1)$, whatever the distribution of $Z^{(1)}$ is. What the CLT supplies is the
*error bar* and the approximate normality of $\hat p_N$. But if the simulated $Z^{(i)}$ are only
approximately normal, the limit is the probability computed under the simulated law, not necessarily the
normal value $0.6827$: the discrepancy is a bias in the model, not a variance that more samples can
remove. Consistency in $N$ and correctness of the target are different questions, and only the first is
answered by the law of large numbers.

*Check:* $8665(0.005)^{2}=0.2166$, so the standard error at $N=8665$ is exactly $0.005$. Doubling $N$ would
reduce it only to $0.0035$, a factor $\sqrt2$ — the quadratic cost again.
