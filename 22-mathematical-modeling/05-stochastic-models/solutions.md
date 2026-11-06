# Stochastic Models — Solutions

> [Stochastic Models](README.md) · Solutions to the 40 problems in [exercises.md](exercises.md)

Each solution states the strategy, carries out the significant steps and ends with a check where one is available. Section references point into the [tutorial](README.md).

## Beginner

**1.** *(Strategy: ask whether more data would remove the uncertainty.)*

(a) **Aleatory.** Arrivals are genuinely random; the distribution is stable, the individual outcome is not predictable. A stochastic model is appropriate.
(b) **Epistemic.** The batch has a definite but unknown mean lifetime. A confidence interval, not a probability distribution of lifetimes, is the right object for the estimate — although the individual lifetimes are also random (aleatory).
(c) **Aleatory.** A fair die has a known distribution; no amount of data changes it.
(d) **Mixed.** Whether an individual responds is aleatory (biological variability); the probability of response is epistemic (estimated from a trial). Reporting a single "probability of success" without saying which one it is is the error the distinction exists to prevent.
(e) **Epistemic.** The failure rate is a fixed property of the component, unknown before testing.

**2.** *(Strategy: build the cumulative table and compare each uniform with it.)*

(a) Cumulative probabilities: A up to $0.15$, B up to $0.70$, C up to $1.00$. Hence

| $U$ | Interval | Grade |
|---|---|---|
| 0.83 | $(0.70, 1.00]$ | C |
| 0.07 | $[0, 0.15]$ | A |
| 0.62 | $(0.15, 0.70]$ | B |
| 0.99 | $(0.70, 1.00]$ | C |

(b) $\mathbb{E}[X] = 0.15(90) + 0.55(75) + 0.30(60) = 13.5 + 41.25 + 18 = 72.75$. Second moment: $0.15(8100) + 0.55(5625) + 0.30(3600) = 1215 + 3093.75 + 1080 = 5388.75$. So

$$
\operatorname{Var}(X) = 5388.75 - 72.75^2 = 5388.75 - 5292.5625 = 96.1875 .
$$

*Check.* $\sqrt{96.1875} = 9.808$, about a tenth of the mean, which is plausible for grades spread over $60$–$90$ ✓.

**3.** *(Strategy: invert the CDF.)*

(a) $F(x) = 1 - e^{-\lambda x}$, so $F^{-1}(u) = -\ln(1-u)/\lambda$. Since $1-U$ is also uniform, the simpler $X = -\ln U/\lambda$ has the same distribution.

(b) With $\lambda = 0.25$: $X = -4\ln U$.

| $u$ | $-\ln u$ | $X$ (minutes) |
|---|---|---|
| 0.1 | 2.30259 | 9.210 |
| 0.5 | 0.69315 | 2.773 |
| 0.9 | 0.10536 | 0.421 |

(c) $\mathbb{E}[X] = -4\int_0^1 \ln u\,du = -4(-1) = 4$ minutes, using $\int_0^1 \ln u\,du = -1$ ✓. Equivalently $1/\lambda = 4$.

*Comment.* The draws are heavily skewed: $u = 0.1$ gives more than twice the mean. A single exponential draw is a poor guide to the distribution, which is why simulation reports averages rather than single runs.

**4.** *(Strategy: sample statistics, then the standard error.)*

(a) $\sum x_i = 42+38+51+45+47+39+44+40 = 346$, so $\bar x = 43.25$. Deviations from the mean: $-1.25, -5.25, 7.75, 1.75, 3.75, -4.25, 0.75, -3.25$; their squares sum to $135.5$, so

$$
s^2 = \frac{135.5}{8-1} = 19.357, \qquad s = 4.400 .
$$

(b) $\operatorname{se} = s/\sqrt n = 4.400/\sqrt 8 = 1.556$, and the 95 % interval is $43.25 \pm 1.96(1.556) = 43.25 \pm 3.05$, i.e. $[40.20, 46.30]$.

(c) The width is proportional to $1/\sqrt n$, so halving it requires four times as many runs: $32$.

*Check.* $s^2$ with $n$ rather than $n-1$ would give $16.94$ and $s = 4.116$; the difference matters at $n = 8$, which is why the $n-1$ convention exists ✓.

**5.** *(Strategy: $\operatorname{se} = \sigma/\sqrt n$.)*

(a) $2.5/\sqrt n$:

| $n$ | $\operatorname{se}$ |
|---|---|
| 100 | 0.250 |
| 1000 | 0.0791 |
| $10^4$ | 0.0250 |
| $10^6$ | 0.0025 |

(b) $2.5/\sqrt n \le 0.01 \Rightarrow \sqrt n \ge 250 \Rightarrow n \ge 62\,500$.

(c) Because the standard error of the mean depends on the *spread* of the draws and on the number of draws, not on where the distribution is centred. A mean of $10^6$ with $\sigma = 2.5$ is estimated as precisely as a mean of $1$ with the same spread — in absolute terms. (Relative precision does depend on the mean.)

**6.** *(Strategy: $\rho = \lambda/\mu$, then the formulas of Theorem 8.9.)*

(a) $\rho = 4/6 = 2/3 < 1$: the queue is stable and a stationary distribution exists.

(b) $P_0 = 1 - \rho = 1/3$. Then

$$
L = \frac{\rho}{1-\rho} = \frac{2/3}{1/3} = 2,\qquad
L_q = \frac{\rho^2}{1-\rho} = \frac{4/9}{1/3} = \frac43,
$$
$$
W = \frac{1}{\mu-\lambda} = \frac12\ \text{h},\qquad
W_q = \frac{\lambda}{\mu(\mu-\lambda)} = \frac{4}{6\cdot 2} = \frac13\ \text{h}.
$$

(c) $\Pr(N \ge 3) = \rho^3 = (2/3)^3 = 8/27 = 0.2963$.

*Check.* Little: $\lambda W = 4(0.5) = 2 = L$ ✓ and $\lambda W_q = 4/3 = L_q$ ✓; $L - L_q = 2/3 = \rho$ ✓.

**7.** *(Strategy: $L = \lambda W$ applied twice.)*

(a) $\lambda = L/W = 12/0.25 = 48$ customers per hour.

(b) $L = \lambda W = 60(0.25) = 15$ customers.

(c) Both use the same assumptions: steady state over the measurement period, and a stable system in which the long-run averages exist. If the shop is growing or shrinking during the measurement, the identity relates interval averages and the ratios need not equal the steady-state values.

**8.** *(Strategy: Theorem 8.10 with $p = q = 1/2$.)*

(a) Ruin probability $= (N-i)/N = 20/50 = 0.4$; the probability of reaching 50 is $0.6$.

(b) $T(i) = i(N-i) = 30(20) = 600$ steps.

(c) The hitting probability is a harmonic function of position, so it is invariant under a rescaling of the step: a walk with steps $\pm s$ reaches the same barrier with the same probability starting from the same *relative* position. The expected number of steps, however, scales as $1/s^2$ — with steps of size 2 the gambler covers the same distance in a quarter of the steps.

**9.** *(Strategy: the normal formulas $\mu + \sigma z_\alpha$ and $\mu + \sigma\phi(z_\alpha)/(1-\alpha)$.)*

(a) $z_{0.99} = 2.32635$, so $\operatorname{VaR}_{0.99} = 2 + 5(2.32635) = 13.63$. With $\phi(2.32635) = 0.026652$,

$$
\operatorname{ES}_{0.99} = 2 + \frac{5(0.026652)}{0.01} = 2 + 13.326 = 15.33 .
$$

(b) $z_{0.975} = 1.95996$, so $\operatorname{VaR}_{0.975} = 2 + 5(1.95996) = 11.80$. With $\phi(1.95996) = 0.058445$,

$$
\operatorname{ES}_{0.975} = 2 + \frac{5(0.058445)}{0.025} = 2 + 11.689 = 13.69 .
$$

(c) ES is the average of the losses beyond the quantile, so it must exceed VaR whenever the distribution has any mass above the quantile. The ratio is $15.33/13.63 = 1.124$ at 99 % and $13.69/11.80 = 1.160$ at 97.5 %: the tail average is *relatively* further above the quantile at lower confidence, because a larger part of the tail is being averaged.

**10.** *(Strategy: compute the quantile from the distribution function, then integrate the tail.)*

(a) $F(0) = 0.9$, so the $90\,\%$ quantile is $0$: $\operatorname{VaR}_{0.9} = 0$. For ES, $\operatorname{VaR}_u = 0$ for $u \le 0.9$ and $50$ for $u \in (0.9, 1]$, so

$$
\operatorname{ES}_{0.9} = \frac{1}{0.1}\int_{0.9}^{1}50\,du = \frac{5}{0.1} = 50 .
$$

(b) VaR reports the threshold that is exceeded only $10\,\%$ of the time — and that threshold is zero, because a loss of 50 happens only $10\,\%$ of the time. ES reports the *average* of the tail, which is the whole 50. For a regulator, ES is the more informative number: it says that when the tail event happens, the loss is 50, whereas VaR says only that it happens rarely.

*Comment.* This is the sharpest illustration of VaR's blindness: a distribution with a large loss in the tail has $\operatorname{VaR}_{0.9} = 0$ as long as the tail probability is below $0.1$.

**11.** *(Strategy: the acceptance ratio is $f/(Mg)$.)*

(a) Draw $Y \sim \mathcal{U}(0,1)$ and $V \sim \mathcal{U}(0,1)$; accept if $V \le \dfrac{2Y}{2\cdot 1} = Y$.

(b) Acceptance probability $= 1/M = 1/2$, so 1000 accepted draws need on average 2000 proposals (a geometric number with mean 2).

(c) The accepted density is $f(x) = 2x$, whose mean is

$$
\int_0^1 x\cdot 2x\,dx = \frac23 .
$$

*Check.* $\int_0^1 2x\,dx = 1$ ✓, and the acceptance probability computed directly is $\int_0^1 \Pr(V \le y)\,dy = \int_0^1 y\,dy = 1/2$ ✓.

**12.** *(Strategy: write $S_T$ as a lognormal and transform the probability.)*

(a) $\mathbb{E}[S_T] = 50e^{0.08(2)} = 50e^{0.16} = 58.68$. The median is $50\exp((\mu - \sigma^2/2)T) = 50\exp((0.08 - 0.03125)2) = 50e^{0.0975} = 55.12$.

(b) $\ln(S_T/50) \sim \mathcal{N}(0.0975,\ 0.125)$, so

$$
\Pr(S_T < 50) = \Phi\!\left(\frac{0 - 0.0975}{\sqrt{0.125}}\right) = \Phi(-0.2758) = 0.3914 .
$$

(c) The distribution is lognormal and hence right-skewed: a few very large outcomes pull the mean above the median. A long-term investor comparing the share to a fixed-income alternative should quote the mean (the expected return), but should also know that the typical (median) outcome is lower and that $\Pr(S_T < S_0) = 39\,\%$ even with a positive drift.

## Intermediate

**13.** *(Strategy: expand the variance of the pair average.)*

(a) $\mathbb{E}[U^2] = 1/3$ and $\mathbb{E}[U^4] = 1/5$, so $\operatorname{Var}(U^2) = 1/5 - 1/9 = 4/45 = 0.08889$.

(b) $g(U) = \frac12(U^2 + (1-U)^2) = U^2 - U + \frac12$. Then

$$
\operatorname{Var}(g) = \operatorname{Var}(U^2) + \operatorname{Var}(U) - 2\operatorname{Cov}(U^2, U)
= \frac{4}{45} + \frac{1}{12} - 2\left(\frac14 - \frac13\cdot\frac12\right) = \frac{4}{45} - \frac{1}{12} = \frac{1}{180}.
$$

(c) For the same $2n$ evaluations, the naive variance is $\frac{1}{2n}\cdot\frac{4}{45}$ and the antithetic variance is $\frac1n\cdot\frac{1}{180}$, so the ratio is

$$
\frac{2\cdot(1/180)}{4/45} = \frac{2}{180}\cdot\frac{45}{4} = \frac18 = 0.125,
$$

an eightfold reduction in the number of evaluations for the same precision.

*Check.* $\operatorname{Cov}(U^2,U) = 1/12 > 0$ and the antithetic covariance is $-1/12$ ✓, consistent with the monotonicity argument.

**14.** *(Strategy: change of measure, then minimise the second moment.)*

(a) With $p(x) = e^{-x}$ and $q(x) = \lambda e^{-\lambda x}$,

$$
\frac{p(x)}{q(x)} = \frac{1}{\lambda}e^{-(1-\lambda)x},
\qquad
\hat p = \frac1n\sum_i \frac{1}{\lambda}e^{-(1-\lambda)Y_i}\mathbf{1}\{Y_i > 3\}.
$$

Unbiasedness: $\mathbb{E}_q[\hat p] = \frac{1}{\lambda}\int_3^\infty e^{-(1-\lambda)x}\lambda e^{-\lambda x}dx = \int_3^\infty e^{-x}dx = e^{-3}$ ✓.

(b) The second moment is

$$
m_2(\lambda) = \frac{1}{\lambda^2}\int_3^\infty e^{-2(1-\lambda)x}\lambda e^{-\lambda x}dx
= \frac{1}{\lambda}\cdot\frac{e^{-(2-\lambda)3}}{2-\lambda}, \qquad 0 < \lambda < 2 .
$$

Differentiate $\ln m_2 = -\ln\lambda - 3(2-\lambda) - \ln(2-\lambda)$:

$$
-\frac1\lambda + 3 + \frac{1}{2-\lambda} = 0
\iff 3 = \frac{1}{\lambda} - \frac{1}{2-\lambda} = \frac{2-2\lambda}{\lambda(2-\lambda)}
\iff 3\lambda^2 - 8\lambda + 2 = 0,
$$

so $\lambda = (8 \pm \sqrt{40})/6$, and the admissible root is $\lambda^\ast = 0.2792$.

(c) At $\lambda^\ast$: $m_2 = 0.011922$, so $\operatorname{Var} = 0.011922 - (0.049787)^2 = 0.011922 - 0.002479 = 0.009443$. The naive variance is $p(1-p) = 0.047308$, so the variance ratio is

$$
\frac{0.047308}{0.009443} = 5.01,
$$

a fivefold reduction. Note that the gain is modest because the event is not rare ($p \approx 5\,\%$); for $p = 10^{-4}$ the same construction gains several orders of magnitude.

*Check.* $\lambda^\ast \approx 0.279$ corresponds to a proposal mean of $1/\lambda^\ast = 3.58$, somewhat above the threshold 3 — tilting past the event, as expected.

**15.** *(Strategy: solve the inequality $W_q \le 0.05$.)*

(a) $W_q = \lambda/(\mu(\mu-\lambda))$, so with $\lambda = 10$:

$$
\frac{10}{\mu(\mu-10)} \le 0.05
\iff 200 \le \mu^2 - 10\mu
\iff \mu^2 - 10\mu - 200 \ge 0 .
$$

The positive root is $\mu = (10 + \sqrt{100 + 800})/2 = 20$, so the smallest service rate is $\mu = 20$ per hour.

(b) At $\mu = 20$: $\rho = 0.5$, $W = 1/(20-10) = 0.1$ h, $L = \lambda W = 1$, $W_q = 0.05$ h and $L_q = 0.5$.

(c) The load is $\lambda = 10$; the required capacity is $\mu = 20$, twice the load. The excess is what keeps the queue short: $W_q$ depends on $\mu - \lambda$, so at $\mu = 11$ the wait would be $10/(11 \cdot 1) = 0.909$ h, eighteen times longer than at $\mu = 20$, even though the spare capacity is 10 % rather than 50 %.

**16.** *(Strategy: Theorem 8.10 and Theorem 8.11 with $p = 0.6$.)*

(a) With $q/p = 0.4/0.6 = 2/3$ and $i = 20$, $N = 40$:

$$
(q/p)^{20} = e^{20\ln(2/3)} = e^{-8.109} = 3.007\times10^{-4},
$$

and $(q/p)^{40} = 9.04\times10^{-8}$, so

$$
h(20) = \frac{1 - 3.007\times10^{-4}}{1 - 9.04\times10^{-8}} = 0.999699 .
$$

(b) With $q - p = -0.2$,

$$
T(20) = \frac{20}{-0.2} - \frac{40}{-0.2}(0.999699) = -100 + 199.94 = 99.94\ \text{rounds}.
$$

(c) The fair game gives $h = 0.5$ and $T = 20 \times 20 = 400$ rounds. The bias makes success almost certain (0.9997 against 0.5) *and* shortens the game (100 against 400 rounds), because the drift pushes the walk towards the upper barrier instead of letting it wander.

**17.** *(Strategy: compare the bias with the standard error.)*

(a) Discretisation bias from the Euler–Maruyama scheme (weak order 1: $O(\Delta t)$), and Monte Carlo error from the finite number of paths ($O(1/\sqrt n)$).

(b) The bias is $110.4713 - 110.5171 = -0.0458$. The Monte Carlo standard error is $0.005$, so the discrepancy is $0.0458/0.005 = 9.2$ standard errors. Discretisation dominates by an order of magnitude: no feasible number of paths removes it.

(c) Refine the time grid (halving $\Delta t$ halves the bias), or, when the SDE has a closed-form solution as this one does, simulate the exact solution and use the scheme only where it is needed. Adding paths is the wrong response.

**18.** *(Strategy: compute the portfolio distribution and then the two measures.)*

(a) Single asset: $\Pr(100) = 0.03 < 0.05$, so $\operatorname{VaR}_{0.95} = 0$. And

$$
\operatorname{ES}_{0.95} = \frac{100 \times 0.03}{0.05} = 60 .
$$

(b) Portfolio of three: $P(0) = 0.97^3 = 0.912673$, $P(100) = 3(0.03)(0.97)^2 = 0.084681$, $P(200) = 3(0.0009)(0.97) = 0.002619$, $P(300) = 0.000027$. Since $\Pr(\text{loss} \ge 100) = 0.087327 > 0.05$, we have $\operatorname{VaR}_{0.95} = 100$. And

$$
\operatorname{ES}_{0.95} = \frac{1}{0.05}\bigl[100(0.047354) + 200(0.002619) + 300(0.000027)\bigr] = \frac{5.2673}{0.05} = 105.35 .
$$

(c) VaR: $100 > 0 + 0 + 0$, so VaR is **not** subadditive — diversification appears to create risk. ES: $105.35 \le 60 + 60 + 60 = 180$ ✓, so ES is subadditive, with a large diversification benefit.

*Comment.* The VaR failure is not a numerical accident: three assets of $3\,\%$ default probability each have a $8.7\,\%$ chance that at least one defaults, which crosses the $5\,\%$ threshold, while each individually does not.

**19.** *(Strategy: invert the relative standard error formula.)*

(a) For a Bernoulli$(p)$ average, the relative standard error is $\sqrt{(1-p)/(np)}$. Requiring it to be at most $\varepsilon$ gives

$$
n \ge \frac{1-p}{p\,\varepsilon^2} .
$$

(b) $p = 0.02$, $\varepsilon = 0.1$: $n \ge 0.98/(0.02 \times 0.01) = 4900$. For $p = 0.2$: $n \ge 0.8/(0.2 \times 0.01) = 400$.

(c) The number of *events* is what matters: the standard error of $\hat p$ is $\sqrt{p(1-p)/n}$, so a relative precision of $\varepsilon$ requires about $1/(\varepsilon^2p)$ observations, i.e. $1/\varepsilon^2$ *events*. A rare event needs many more trials to produce the same number of events.

*Check.* With $n = 4900$ and $p = 0.02$, about 98 events are observed; $1/\varepsilon^2 = 100$ ✓.

**20.** *(Strategy: one Euler–Maruyama step and the exact solution on the same path.)*

Euler–Maruyama with one step: $\bar S_1 = 100(1 + 0.1(1) + 0.2(1)(0)) = 110.0$. The exact solution with $W_1 = 0$ is $100e^{0.08} = 108.329$.

The difference is $1.671$, about $1.5\,\%$ of the value — one step of length 1 is far too coarse: the scheme ignores the $- \tfrac12\sigma^2$ correction entirely within the step and treats the noise as additive-linear. Refining to $n = 12$ cuts the error to about $0.05$ (Exercise 17), which is the weak-order-1 behaviour in action.

*Check.* The exact value corresponds to the median of $S_T$ ($108.3287$) because $W_T = 0$ ✓ — a useful sanity check.

**21.** *(Strategy: Kupiec's statistic.)*

(a) With $n = 250$, $x = 15$, $p = 0.05$:

$$
(n-x)\ln(1-p) + x\ln p = 235(-0.0512933) + 15(-2.995732) = -12.0539 - 44.9360 = -56.9899,
$$
$$
(n-x)\ln\!\Bigl(1-\tfrac{x}{n}\Bigr) + x\ln\tfrac{x}{n} = 235\ln(0.94) + 15\ln(0.06) = -14.5406 - 42.2012 = -56.7418,
$$

so $\mathrm{LR} = -2(-56.9899 + 56.7418) = 0.496$. Under the null, $\mathrm{LR} \sim \chi^2_1$, giving a p-value of $0.481$.

(b) There is no evidence against the model at the 5 % level: 15 exceedances against an expected $12.5$ is well within sampling variation.

(c) The test looks only at the *number* of exceedances. It does not detect clustering (failures arriving in runs, which is the signature of a model that ignores volatility), it does not check the size of the losses, and it has low power: with 250 observations it can only reliably detect large proportional errors. Christoffersen's independence test, applied to the sequence of exceedances, addresses the first of these.

**22.** *(Strategy: Theorem 8.10 for the exact value; the Brownian formula with the correct barriers for the approximation.)*

(a) $q/p = 0.48/0.52 = 0.923077$, so $(q/p)^{20} = 0.2019$ and $(q/p)^{40} = 0.04075$. Hence

$$
h(20) = \frac{1 - 0.2019}{1 - 0.04075} = 0.8321 .
$$

(b) With $\mu = 0.04$, $\sigma^2 = 4(0.52)(0.48) = 0.9984$, and the barriers at $+a = +20$ and $-b = -20$ relative to the start:

$$
\Pr \approx \frac{1 - e^{-2(0.04)(20)/0.9984}}{1 - e^{-2(0.04)(40)/0.9984}} = \frac{1 - e^{-1.6026}}{1 - e^{-3.2051}} = \frac{0.7985}{0.9595} = 0.8322 .
$$

(c) The approximation is excellent here — $0.8322$ against $0.8321$ — because the barriers are twenty steps away, so the lattice is invisible, and the exponents $1.60$ and $3.21$ are moderate, so the exponential differences retain precision. It deteriorates when the barriers are only a few steps away, when the drift is so large that the probability is essentially 1 and the formula subtracts nearly equal numbers, and whenever the identification of $a$, $b$, $\mu$ and $\sigma^2$ with the discrete model's parameters is wrong. That last point is the practical one: the formula is only as good as the mapping from the discrete problem to the continuous one.

## Advanced

**23.** *(Strategy: Chebyshev for the law; the CLT for the rate.)*

Let $X_i$ be i.i.d. with mean $\theta$ and variance $\sigma^2 < \infty$. Then $\mathbb{E}[\hat\theta_n] = \theta$ and, by independence,

$$
\operatorname{Var}(\hat\theta_n) = \frac{1}{n^2}\sum_{i=1}^n\operatorname{Var}(X_i) = \frac{\sigma^2}{n}.
$$

Chebyshev's inequality, applied to $\hat\theta_n$, gives

$$
\Pr\bigl(|\hat\theta_n - \theta| \ge \varepsilon\bigr) \le \frac{\operatorname{Var}(\hat\theta_n)}{\varepsilon^2} = \frac{\sigma^2}{n\varepsilon^2} \to 0
$$

for every $\varepsilon > 0$, which is convergence in probability. $\blacksquare$

The CLT adds the *distribution* of the error: $(\hat\theta_n - \theta)/(\sigma/\sqrt n) \Rightarrow \mathcal{N}(0,1)$. The law says the error goes to zero; the CLT says how it fluctuates on the way, which is what turns an estimate into an interval.

What the law does not say: it does not say that $\hat\theta_n$ is close to any *external* quantity. It says that the average converges to the expectation under the model. If the model's distribution is wrong, the average converges to the wrong number with the same $1/\sqrt n$ precision. Convergence is a statement about the sampler, not about the world.

**24.** *(Strategy: expand the variance; then use monotonicity.)*

Let $g(u) = f(1-u)$. Since $g(U) \overset{d}{=} f(U)$,

$$
\operatorname{Var}\!\left(\frac{f(U)+g(U)}{2}\right)
= \frac14\bigl(\operatorname{Var} f + \operatorname{Var} g + 2\operatorname{Cov}(f,g)\bigr)
= \frac12\bigl(\operatorname{Var} f + \operatorname{Cov}(f,g)\bigr).
$$

For the covariance inequality, suppose $f$ is non-decreasing and let $U, V$ be independent uniform. Then $(f(U)-f(V))(g(U)-g(V)) \le 0$ pointwise, because $f$ increasing and $g$ decreasing mean the two differences have opposite signs (or one is zero). Taking expectations,

$$
2\operatorname{Cov}(f(U), g(U)) = \mathbb{E}\bigl[(f(U)-f(V))(g(U)-g(V))\bigr] \le 0 .
$$

Hence $\operatorname{Var}(\text{pair average}) \le \tfrac12\operatorname{Var}(f(U))$, i.e. antithetic sampling is at least as good as two independent draws. $\blacksquare$

When it cannot help: if $\operatorname{Cov}(f(U), f(1-U)) > 0$ the pair average has variance *larger* than $\tfrac12\operatorname{Var} f$. This happens for symmetric integrands such as $f(u) = u(1-u)$, where $f(U) = f(1-U)$ and the two draws are perfectly correlated — antithetic sampling then gives no reduction at all, and the variance per evaluation is twice that of naive sampling.

**25.** *(Strategy: use the equivalence $F^{-1}(u) \le x \iff u \le F(x)$.)*

Let $F$ be a distribution function, $F^{-1}(u) = \inf\{x : F(x) \ge u\}$ and $U \sim \mathcal{U}(0,1)$.

*Claim.* For all $x \in \mathbb{R}$ and $u \in (0,1)$, $F^{-1}(u) \le x \iff u \le F(x)$.

*Proof.* If $F^{-1}(u) \le x$ then, for every $\varepsilon > 0$, $x + \varepsilon$ belongs to $\{y : F(y) \ge u\}$, so $F(x+\varepsilon) \ge u$; right-continuity of $F$ gives $F(x) \ge u$. Conversely, if $u \le F(x)$ then $x \in \{y : F(y) \ge u\}$, so the infimum of that set is at most $x$. $\square$

Therefore

$$
\Pr(X \le x) = \Pr\bigl(F^{-1}(U) \le x\bigr) = \Pr\bigl(U \le F(x)\bigr) = F(x),
$$

since $U$ is uniform. $\blacksquare$

*Jumps.* If $F$ jumps at $x_0$, the generalised inverse is constant on the interval of $u$ between $F(x_0^-)$ and $F(x_0)$, and that interval has length equal to the atom's probability. So the jump receives exactly the right mass, which is why the discrete inverse transform of Exercise 2 works: the thresholds are the cumulative probabilities and each interval of $u$ has length equal to the corresponding probability.

**26.** *(Strategy: two-dimensional integral over $(Y, V)$.)*

Let $f \le Mg$ with $M < \infty$. For a measurable set $A$,

$$
\Pr(Y \in A,\ \text{accept}) = \int_A\int_0^{f(y)/(Mg(y))} g(y)\,dv\,dy = \frac1M\int_A f(y)\,dy .
$$

Setting $A = \mathbb{R}$ gives $\Pr(\text{accept}) = 1/M$. Dividing,

$$
\Pr(Y \in A \mid \text{accept}) = \frac{(1/M)\int_A f}{1/M} = \int_A f,
$$

so the accepted value has density $f$. The number of proposals is geometric with success probability $1/M$, hence mean $M$. $\blacksquare$

*Why high dimensions are fatal.* A proposal must satisfy $M \ge \sup f/g$, and in $d$ dimensions the ratio of the target's effective volume to the proposal's grows at least exponentially in $d$ for any fixed simple envelope. For a standard normal target and a uniform envelope on a box, the acceptance probability decays like $d^{-d/2}$ up to constants: it is already small at $d = 10$ and hopeless at $d = 100$. Rejection sampling is a tool for one to three dimensions; MCMC or importance sampling replaces it beyond that.

**27.** *(Strategy: the variational representation makes subadditivity a property of $x^+$.)*

By Theorem 8.17, $\operatorname{ES}_\alpha(L) = \min_c\{c + (1-\alpha)^{-1}\mathbb{E}[(L-c)^+]\}$. For any $c_1, c_2$,

$$
\operatorname{ES}_\alpha(L_1+L_2) \le (c_1+c_2) + \frac{1}{1-\alpha}\mathbb{E}\bigl[(L_1-c_1)^+ + (L_2-c_2)^+\bigr],
$$

using $(x+y)^+ \le x^+ + y^+$. Minimising the right-hand side over $c_1$ and $c_2$ separately gives

$$
\operatorname{ES}_\alpha(L_1+L_2) \le \operatorname{ES}_\alpha(L_1) + \operatorname{ES}_\alpha(L_2). \qquad \blacksquare
$$

*VaR fails.* Take three independent assets, each losing $100$ with probability $p$, and $\alpha = 0.95$. For one asset, $\operatorname{VaR}_{0.95} = 0$ as long as $p \le 0.05$. For the portfolio, $\Pr(\text{loss} \ge 100) = 1-(1-p)^3$, which exceeds $0.05$ exactly when

$$
(1-p)^3 < 0.95 \iff 1-p < 0.95^{1/3} = 0.983048 \iff p > 0.016952 .
$$

So for every $p \in (0.01695,\ 0.05]$ we have $\operatorname{VaR}_{0.95}(\text{portfolio}) = 100$ while each $\operatorname{VaR}_{0.95} = 0$: a violation of subadditivity by the full loss size. At $p = 0.03$ (Exercise 18) the violation is exactly $100$. $\blacksquare$

**28.** *(Strategy: solve the balance equations, then sum.)*

*Stationarity.* Let $P_n$ be the stationary probability of $n$ customers. Flow balance at state $n \ge 1$ is

$$
\lambda P_{n-1} + \mu P_{n+1} = (\lambda+\mu)P_n,
$$

and at $n = 0$, $\lambda P_0 = \mu P_1$. Rearranging the first equation,

$$
\mu(P_{n+1} - P_n) = \lambda(P_n - P_{n-1}),
$$

so $P_{n+1} - P_n = \rho(P_n - P_{n-1})$ with $\rho = \lambda/\mu$. Hence $P_n - P_{n-1} = \rho^{n-1}(P_1 - P_0) = \rho^{n-1}(\rho-1)P_0 = -(1-\rho)\rho^{n-1}P_0$, using $P_1 = \rho P_0$. Summing telescopically,

$$
P_n = P_0 - (1-\rho)P_0\sum_{k=1}^{n}\rho^{k-1}
= P_0\bigl(1 - (1-\rho^n)\bigr) = P_0\rho^n .
$$

Normalising: $\sum_{n\ge0}P_n = P_0/(1-\rho) = 1$ requires $\rho < 1$, and then $P_0 = 1-\rho$. If $\rho \ge 1$ the sum diverges, so no stationary distribution exists. $\blacksquare$

*Measures.* $L = (1-\rho)\sum_{n\ge0}n\rho^n = (1-\rho)\rho/(1-\rho)^2 = \rho/(1-\rho)$, using $\sum n\rho^n = \rho/(1-\rho)^2$. The mean number in service is $\Pr(N \ge 1) = \rho$, so $L_q = L - \rho = \rho^2/(1-\rho)$. Little's law gives $W = L/\lambda = 1/(\mu-\lambda)$ and $W_q = L_q/\lambda = \rho/(\mu-\lambda)$. $\blacksquare$

**29.** *(Strategy: count time in the system two ways.)*

Fix a sample path on $[0,T]$. Let $N(t)$ be the number in the system, $A(T) = A$ the number of arrivals and $W_1,\dots,W_A$ their sojourn times. If the system is empty at $0$ and at $T$, every sojourn is complete and

$$
\int_0^T N(t)\,dt = \sum_{i=1}^{A} W_i,
$$

because both sides count the total customer-time in the system. Dividing by $T$,

$$
\frac1T\int_0^T N(t)\,dt = \frac{A}{T}\cdot\frac{1}{A}\sum_{i=1}^A W_i,
$$

i.e. $L_T = \lambda_T W_T$ exactly, for every such path and every $T$.

*Boundary terms.* If the system is not empty at $0$ or $T$, the identity fails by at most $2N_{\max}W_{\max}$: the customers present at the endpoints contribute partial sojourns that one side counts and the other does not, and each such contribution is bounded by the maximum sojourn time. Divided by $T$ and let $T \to \infty$, this vanishes. Taking limits (which exist by hypothesis) gives $L = \lambda W$. $\blacksquare$

*Transients.* During a transient the three quantities are time-dependent: the identity still holds for the averages over $[0,T]$, but it does not relate the instantaneous $L(t)$ to a constant $\lambda$ and $W$. Measuring $L$ before the system settles and $W$ after it has settled, and dividing, gives a number that is not the arrival rate.

**30.** *(Strategy: apply Itô's lemma to $\ln S$.)*

With $dS = \mu S\,dt + \sigma S\,dW$ and $f(s) = \ln s$: $f'(s) = 1/s$, $f''(s) = -1/s^2$, so Theorem 8.13 gives

$$
d\ln S_t = \left(\frac{\mu S_t}{S_t} - \frac12\frac{\sigma^2S_t^2}{S_t^2}\right)dt + \frac{\sigma S_t}{S_t}dW_t
= \left(\mu - \tfrac12\sigma^2\right)dt + \sigma\,dW_t .
$$

Integrating from $0$ to $t$:

$$
S_t = S_0\exp\left(\left(\mu - \tfrac12\sigma^2\right)t + \sigma W_t\right). \qquad \blacksquare
$$

*Moments.* Since $W_t \sim \mathcal{N}(0,t)$, the exponent is normal with mean $(\mu - \tfrac12\sigma^2)t$ and variance $\sigma^2t$, so

$$
\mathbb{E}[S_t] = S_0e^{(\mu - \sigma^2/2)t}\cdot e^{\sigma^2t/2} = S_0e^{\mu t},
\qquad
\operatorname{Var}(S_t) = S_0^2e^{2\mu t}\left(e^{\sigma^2t} - 1\right).
$$

*Median.* The median of a lognormal is $\exp$ of the median of the exponent, i.e. $S_0e^{(\mu - \sigma^2/2)t}$: the typical path grows at the rate reduced by the variance drag $\tfrac12\sigma^2$, while the mean grows at $\mu$. The gap measures how much of the expected return is delivered by rare large outcomes — with $\mu = 0.1$ and $\sigma = 0.2$, the median grows at $0.08$ and the mean at $0.10$.

**31.** *(Strategy: differentiate a convex function of the threshold.)*

Define $\psi(c) = c + \frac{1}{1-\alpha}\mathbb{E}[(L-c)^+]$, which is convex in $c$. Its derivative, where it exists, is

$$
\psi'(c) = 1 - \frac{1}{1-\alpha}\Pr(L > c).
$$

Setting $\psi'(c) = 0$ gives $\Pr(L > c) = 1-\alpha$, i.e. $c$ is the $\alpha$-quantile $q = \operatorname{VaR}_\alpha(L)$. At $c = q$,

$$
\psi(q) = q + \frac{1}{1-\alpha}\mathbb{E}[(L-q)^+]
= q + \frac{1}{1-\alpha}\int_q^\infty (1-F_L(t))\,dt .
$$

For continuous $F_L$ the last expression is $\mathbb{E}[L \mid L > q] = \operatorname{ES}_\alpha(L)$; hence the minimum is $\operatorname{ES}$ and it is attained at $c = q$. $\blacksquare$

*ES dominates VaR.* At $c = q$ the term $\mathbb{E}[(L-q)^+]$ is non-negative, so

$$
\operatorname{ES}_\alpha(L) = q + \frac{1}{1-\alpha}\mathbb{E}[(L-q)^+] \ge q = \operatorname{VaR}_\alpha(L). \qquad \blacksquare
$$

*Check on Exercise 9.* With $\mu = 2$, $\sigma = 5$, $\alpha = 0.99$: $q = 13.63$ and $\operatorname{ES} = 15.33 \ge 13.63$ ✓, the gap being the expected excess over the quantile divided by $1-\alpha$.

## Challenge

**32.** *(Strategy: stationarity gives the variance; the covariance sum gives the inflation.)*

(a) Squaring $X_t = \rho X_{t-1} + \varepsilon_t$ and taking expectations, with $\operatorname{Cov}(X_{t-1},\varepsilon_t) = 0$:

$$
\gamma_0 = \rho^2\gamma_0 + \sigma_\varepsilon^2 \implies \gamma_0 = \frac{\sigma_\varepsilon^2}{1-\rho^2} = \sigma^2 .
$$

Multiplying by $X_{t-k}$ and taking expectations gives $\gamma_k = \rho\gamma_{k-1}$, so $\gamma_k = \rho^k\sigma^2$ and $\rho_k = \rho^k$.

(b) $\operatorname{Var}(\bar X_n) = \frac{1}{n^2}\sum_{i,j}\operatorname{Cov}(X_i,X_j) = \frac{\sigma^2}{n}\left[1 + 2\sum_{k=1}^{n-1}\left(1-\frac{k}{n}\right)\rho^k\right]$. As $n \to \infty$ the bracket tends to $1 + 2\rho/(1-\rho) = (1+\rho)/(1-\rho)$, so

$$
\operatorname{Var}(\bar X_n) \approx \frac{\sigma^2}{n}\cdot\frac{1+\rho}{1-\rho}. \qquad \blacksquare
$$

(c) For $\rho = 0.9$ the factor is $1.9/0.1 = 19$, so the standard error is inflated by $\sqrt{19} = 4.36$: the naive interval is less than a quarter of its true width. A simulation whose output is autocorrelated therefore reports a precision that is too good by a factor of more than four unless the correlation is accounted for (batch means, an effective sample size, or thinning).

**33.** *(Strategy: compute the second moment of the weight.)*

(a) With $p(x) = e^{-x}$, $q(x) = 2e^{-2x}$ and $f \equiv 1$, the weight is $p/q = \tfrac12 e^{x}$ and

$$
\mathbb{E}_q\!\left[\frac{p(Y)}{q(Y)}\right] = \int_0^\infty \frac12 e^{y}\cdot 2e^{-2y}dy = \int_0^\infty e^{-y}dy = 1 .
$$

(b) The second moment is

$$
\mathbb{E}_q\!\left[\frac{p(Y)^2}{q(Y)^2}\right] = \int_0^\infty \frac14 e^{2y}\cdot 2e^{-2y}dy = \int_0^\infty \frac12\,dy = \infty .
$$

So the estimator is unbiased with infinite variance. $\blacksquare$

(c) A pilot run of moderate size looks perfectly reasonable: the weights are $e^y/2$, and for the values typically drawn from $q$ (mean $1/2$) they are of order $1$. The divergence comes from the far tail, where $q$ decays twice as fast as $p$ and the ratio grows exponentially — an event too rare to appear in a pilot. The diagnostic is structural: **check that the proposal has at least as heavy a tail as the target**, analytically or by examining the empirical tail of the weights and the ratio of fitted tail indices. A plot of the sorted weights, or the fraction of total weight carried by the largest few draws, reveals the problem before it produces a wild estimate.

**34.** *(Strategy: tail integrals, then regular variation.)*

(a) For $x \ge 1$ with $\Pr(X > x) = x^{-\alpha}$,

$$
\mathbb{E}[X] = \int_0^\infty \Pr(X > t)\,dt = 1 + \int_1^\infty t^{-\alpha}dt = 1 + \frac{1}{\alpha-1},
$$

finite for $\alpha > 1$. For the second moment, $\mathbb{E}[X^2] = \int_0^\infty 2t\Pr(X>t)\,dt \ge \int_1^\infty 2t^{1-\alpha}dt$, and this last integral equals $2/(\alpha-2)$ when $\alpha > 2$ and diverges when $\alpha \le 2$. So the mean is finite and the variance is not. $\blacksquare$

(b) The CLT requires a finite variance; with $\alpha < 2$ the distribution of $\bar X_n$ is dominated by the largest observation, so its fluctuations are not Gaussian and do not shrink like $n^{-1/2}$.

(c) The correct scaling is $n^{1-1/\alpha}$: $n^{1-1/\alpha}(\bar X_n - \mu)$ converges in distribution to a stable law of index $\alpha$. For $\alpha = 1.5$ the exponent is $1 - 2/3 = 1/3$, so the sample mean converges at rate $n^{-1/3}$, much slower than $n^{-1/2}$. $\blacksquare$

(d) A confidence interval built from $s/\sqrt n$ is meaningless: $s^2$ is itself dominated by the largest observation and does not converge, and the intervals it produces are far too narrow. The mean of a heavy-tailed loss should be estimated with tail-aware methods (fit the tail index, use the Hill estimator, report quantiles as well as the mean), and any simulation must be checked against the $n^{-1/3}$ rate rather than the usual $n^{-1/2}$.

**35.** *(Strategy: compute both budgets from the relative standard error.)*

(a) Brute force: the relative standard error with $n$ paths is $\sqrt{(1-p)/(np)}$, so for a relative error of $0.1$,

$$
n \ge \frac{1-p}{p(0.1)^2} \approx \frac{1}{10^{-6}\times 0.01} = 10^8\ \text{paths}.
$$

(b) Importance sampling with a proposal that makes the loss event common. If the tilted proposal gives a relative standard error of about $2$ per path — a typical figure for a well-designed rare-event sampler — then $n = (2/0.1)^2 = 400$ paths suffice. The scheme must be designed for the particular loss distribution; the essential requirements are that the proposal has at least as heavy a tail as the target and that the weights are bounded.

(c) The budgets differ by a factor of $2.5\times10^5$. The comparison is optimistic because it assumes (i) the proposal can be designed and sampled cheaply, (ii) the variance estimate used to size $n$ is reliable — it needs its own pilot, and (iii) the tail of the loss distribution is known well enough to build a proposal with the right tail. If the tail is misspecified, the importance sampler produces a precise estimate of the wrong quantity.

**36.** *(Strategy: separate the estimate, its error and its interpretation.)*

*Errors and omissions.*

1. **No standard error for the estimate.** The €1.1 m is the standard deviation of a *single path*, not of the mean. The standard error of the mean is $1.1/\sqrt{1000} = €0.0348$ m.
2. **No confidence interval.** With the standard error, the 95 % interval is $4.2 \pm 1.96(0.0348)$, i.e. €$[4.132, 4.268]$ m.
3. **"The expected cost is €4.2 m" conflates the estimate with the truth.** The correct statement is that €4.2 m estimates the model's mean, with a stated uncertainty.
4. **No model statement.** The expectation is under the model; its structural assumptions and their effect are not mentioned.
5. **No bias discussion.** Discretisation, truncation of a horizon, or sampling an input distribution imperfectly can bias the estimate; a second run at a finer resolution is the standard check.
6. **Seed without software or version.** A seed alone does not make the run reproducible.
7. **No sensitivity analysis.** The conclusion is a single number from a single configuration.

*A correct report.* "Across 1000 independent paths (seed 42; software version recorded in Appendix A), the mean simulated cost was €4.20 m with a standard error of €0.035 m, giving a 95 % confidence interval of €[4.13, 4.27] m for the mean cost under the model described in §2. Halving the time step changed the mean by less than €0.01 m, so discretisation bias is small relative to the sampling error. The estimate is conditional on the demand and price assumptions of §2; §5 reports how the mean moves under alternative assumptions."

**37.** *(Strategy: a match within 1 % is a test, and a test needs power.)*

Matching a simulated mean to an observed mean within 1 % is a hypothesis test whose outcome depends on the number of observations and on the variability of both quantities. Three problems make it uninformative.

1. **It may have no power.** If the observed mean is itself estimated from a short series, its standard error may exceed 1 %, so the criterion cannot distinguish a good model from a mediocre one: any model within a wide band would pass.
2. **It checks only the first moment.** A model can reproduce the mean and be badly wrong about the variance, the 95th percentile, the autocorrelation or the tail — precisely the features that matter for capacity planning, staffing and risk.
3. **It invites over-fitting.** If the model has enough parameters, matching the mean is easy and conveys almost nothing; the check must use features that were not calibrated.

*A better design.* Compare several statistics — mean, variance, median, 95th percentile, and the autocorrelation at a few lags — with confidence intervals that account for the sampling error of both the data and the simulation. Report the discrepancy in standard errors rather than as a percentage, and use out-of-sample periods for validation. State in advance what size of discrepancy would count as evidence against the model, so that the check is a test rather than a search for agreement.

**38.** *(Strategy: ask what the number is a function of.)*

Questions to ask, and what each reveals:

1. **What is the loss distribution, and how was it estimated?** A 99 % VaR is a tail quantile; from 250 observations it rests on about 2.5 data points beyond it, so the number is largely an extrapolation from a fitted model (normal, historical, filtered, extreme-value). The answer determines whether the number is data-driven or assumption-driven.
2. **Is it a one-day or a ten-day horizon, and how was it scaled?** If it was scaled by $\sqrt{10}$, the model assumes i.i.d. returns; with volatility clustering or autocorrelation the scaling is wrong, usually too small.
3. **Is it a diversified portfolio number, and what dependence was assumed?** A correlation matrix implies tail independence for the normal family, which understates joint crashes.
4. **What is the estimation error?** With 250 observations the standard error of a 99 % quantile is large; a number quoted to two significant figures without an interval is over-precise.
5. **Has it been backtested, and how many exceedances were observed?** A model that has never been tested is a claim, not a measurement.
6. **What happened in the worst historical episodes?** A stress test that does not depend on the fitted tail is the only defence against the tail being wrong.
7. **What is the expected shortfall at the same level?** ES says how bad the tail is; VaR does not.

Each question tests a different assumption, and together they determine whether the €4.2 m is a measurement, an extrapolation or a guess dressed as a number.

**39.** *(Strategy: separate bias from noise by design.)*

*Design.* Choose a sequence of time steps $\Delta t_k = T/2^k$ for $k = 4, 5, 6, 7$ (so $n = 16, 32, 64, 128$ steps), and for each use $N$ paths with common random numbers across the grids (the same Brownian path, refined) so that the *differences* between grids are not contaminated by independent sampling noise. Estimate the target functional $\hat\theta_k$ and its Monte Carlo standard error $\mathrm{se}_k$ on each grid.

*Quantities to compare.* (i) The functional itself, e.g. $\mathbb{E}[g(X_T)]$; (ii) its difference across successive grids, $\hat\theta_{k+1} - \hat\theta_k$, with the standard error of that difference; (iii) a pathwise strong-error proxy, such as $\max_t|\bar X^{(k)}_t - \bar X^{(k+1)}_t|$ on a subsample of paths.

*Decision rule.* If $|\hat\theta_{k+1} - \hat\theta_k|$ is large relative to the difference's standard error and the differences shrink by roughly a factor of two per refinement, the scheme is in its asymptotic weak-order-1 regime and the remaining bias can be estimated by Richardson extrapolation. If the differences do not shrink, either the grid is not yet fine or the observed order is lower than expected (for instance because the payoff is non-smooth). If the differences are dominated by Monte Carlo noise, increase $N$ rather than refine further. Report the extrapolated value with an interval that combines the estimated bias and the final standard error.

**40.** *(Strategy: both models can be right about different things.)*

Three consistent explanations:

1. **The deterministic model evaluates the objective at the mean input, and the objective is nonlinear.** By Jensen's inequality the stochastic model's mean cost differs from the cost at mean demand by a term proportional to the curvature and the variance. The 20 % gap is then a real consequence of variability, not an error; the data that distinguishes this explanation is the *distribution* of the input — its variance — not just its mean.
2. **The two models use different boundary rules.** A deterministic model may allow unmet demand to be back-ordered, or may not model capacity at all; the stochastic model may lose sales when stock runs out. The difference is a modelling choice, and the data that reveals it is the frequency and size of stockouts (or of back-orders) in the operating records.
3. **The stochastic model's input distribution is mis-specified.** If the simulated demand has a heavier tail than the real demand, the mean cost is inflated: the models agree on the mean input but not on its spread. The data that distinguishes this is a comparison of the empirical distribution of demand with the fitted one — a goodness-of-fit check on the tail, not a comparison of means.

A fourth possibility, worth stating, is that both models are correctly implemented but answer different questions: one includes a cost component the other omits, in which case the data needed is the cost accounting, not more observations. In all cases the resolution is to find the *feature* that produces the gap and test it, rather than to average the two answers.
