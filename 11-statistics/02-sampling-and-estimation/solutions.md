# Sampling and Estimation — Solutions

> [Sampling and Estimation](README.md) · Solutions to the 36 problems in [exercises.md](exercises.md)

Each solution states the strategy, shows every significant step, and checks the result where a check
exists. Pitfalls are flagged where the problem is designed to expose one.

## Beginner

**1.** *(Strategy: name each object in the sampling diagram before computing anything.)*

(a) The **target population** is all adults living in the city. The **sampling frame** is the electoral
register. The **sample** is the $400$ selected adults. The **variable** is daily commute time in minutes;
it is quantitative, continuous and measured on a ratio scale (zero minutes means no commute, and ratios
are meaningful).

(b) The **parameter** is the population mean commute time $\mu$. The **statistic** is the sample mean
$\bar{x}=38.2$ minutes. The parameter is unknown and fixed; the statistic is known and random.

(c) **Undercoverage:** the electoral register omits adults who are not registered, who may commute
differently from registered adults. **Non-sampling error:** respondents may misreport their commute, or
people who commute may be less likely to answer (non-response).

**2.** *(Strategy: a probability sample requires a known positive inclusion probability for every unit.)*

| Scenario | Design | Probability sample? |
|---|---|---|
| (a) every $20$th item | systematic | yes, if the list has no period-$20$ pattern |
| (b) random sample within each faculty | stratified | yes |
| (c) first $50$ shoppers | convenience | no |
| (d) $100$ schools, all teachers | cluster | yes |
| (e) $10$ names from a complete list | simple random | yes |
| (f) website vote | voluntary response | no |

In (a) the inclusion probability is $1/20$ for each item, provided the starting point is random and the
list has no periodic structure aligned with the interval. In (f) the respondents select themselves, so
the inclusion probability is unknown and likely related to the question.

**3.** *(Strategy: the standard error is $\sigma/\sqrt n$; the finite population correction multiplies the
variance, not the standard error.)*

(a) With replacement, $\operatorname{SE}(\bar{X})=\sigma/\sqrt n=15/\sqrt{100}=15/10=1.5$.

(b) The correction factor is

$$\sqrt{\frac{N-n}{N-1}}=\sqrt{\frac{1000-100}{1000-1}}=\sqrt{\frac{900}{999}}=\sqrt{0.900901}=0.9492 .$$

Hence $\operatorname{SE}=1.5(0.9492)=1.4237$.

(c) Here $n/N=0.1$, so the sample is a small fraction of the population and the correction is close to
$1$. When $n=N$ the factor is $0$: a census has no sampling error. The correction matters when the sample
is a substantial fraction of the population, as in audits of small populations.

**4.** *(Strategy: compute the mean, the sample variance with divisor $n-1$, then divide by $\sqrt n$.)*

The sum is $5+7+8+8+9+10+11+12+14=84$, so $\bar{x}=84/9=9.3333$. The deviations are
$-4.333,-2.333,-1.333,-1.333,-0.333,0.667,1.667,2.667,4.667$; their squares sum to $60.00$, so

$$s^2=\frac{60}{9-1}=7.5,\qquad s=\sqrt{7.5}=2.7386 .$$

The estimated standard error is

$$\widehat{\operatorname{SE}}(\bar{X})=\frac{s}{\sqrt n}=\frac{2.7386}{3}=0.9129 .$$

*Check.* $\sum x_i^2=25+49+64+64+81+100+121+144+196=844$, and
$844-84^2/9=844-784=60$. $\checkmark$

**5.** *(Strategy: a parameter is a fixed property of the population; a statistic is computed from the
sample and varies between samples.)*

(a) **Parameter**, $\mu$: the mean of all adults in the city.
(b) **Statistic**, $\bar{x}$: the mean of the $400$ sampled adults.
(c) **Parameter**, $p$: the proportion defective in the whole batch.
(d) **Statistic**, $\hat p$: the proportion defective among the $50$ inspected items.
(e) **Statistic**, $s$: the standard deviation of the $400$ sampled commute times.

The symbols are conventions: $\mu$ and $p$ describe populations, $\bar{x}$, $\hat p$ and $s$ describe
samples. The parameter is unknown; the statistic is observed and has a sampling distribution.

**6.** *(Strategy: the standard error scales like $1/\sqrt n$.)*

(a) With $\sigma=20$:

| $n$ | $25$ | $100$ | $400$ |
|---|---|---|---|
| $\operatorname{SE}=20/\sqrt n$ | $4$ | $2$ | $1$ |

(b) Quadrupling $n$ multiplies the standard error by $1/\sqrt4=1/2$: from $4$ to $2$ and from $2$ to $1$.
To halve the standard error, one needs four times the data.

(c) Solve $20/\sqrt n=0.5$: $\sqrt n=40$, so $n=1600$.

**7.** *(Strategy: $\sigma$ is known, so the interval is $\bar{x}\pm z\sigma/\sqrt n$.)*

The standard error is $\sigma/\sqrt n=10/\sqrt{49}=10/7=1.42857$. The $95\%$ interval is

$$64\pm1.96(1.42857)=64\pm2.800=[61.20,\ 66.80].$$

*Check.* The interval is symmetric about $64$ and its half-width is $2.800$. $\checkmark$

**8.** *(Strategy: only the critical value changes; the standard error is fixed.)*

The standard error is again $1.42857$.

* $90\%$: $z=1.645$, so the margin is $1.645(1.42857)=2.3498$ and the interval is $[61.65,\ 66.35]$,
  with width $4.6996$.
* $95\%$: margin $2.8000$, interval $[61.20,\ 66.80]$, width $5.5999$.
* $99\%$: $z=2.576$, margin $3.6798$, interval $[60.32,\ 67.68]$, width $7.3595$.

The widths grow with the confidence level: $4.70$, $5.60$ and $7.36$. A more confident procedure must
cover more possible values of $\mu$, so it needs a larger multiplier; the growth is not proportional
because the normal tail probability falls rapidly as the critical value moves out.

**9.** *(Strategy: the Wald interval substitutes $\hat p$ for $p$ in the standard error.)*

The sample proportion is $\hat p=36/120=0.3$. Its standard error is

$$\operatorname{SE}=\sqrt{\frac{\hat p(1-\hat p)}{n}}
=\sqrt{\frac{0.3(0.7)}{120}}=\sqrt{0.00175}=0.041833 .$$

The margin of error is $1.96(0.041833)=0.081993$, so the interval is

$$0.3\pm0.0820=[0.2180,\ 0.3820].$$

*Check.* The interval lies inside $[0,1]$ and is centred at $\hat p$. $\checkmark$ With $n\hat p=36$ and
$n(1-\hat p)=84$, both are comfortably above $10$, so the Wald interval is reasonable here.

**10.** *(Strategy: the frequentist probability belongs to the procedure, not to the realised interval or
to the parameter.)*

(a) **Incorrect.** In the frequentist framework $\mu$ is fixed and unknown; the interval is random. The
$95\%$ refers to the procedure, not to this realised interval.
(b) **Correct.** This is the definition of coverage.
(c) **Incorrect.** That is a tolerance interval, which contains $95\%$ of the *data*. A confidence
interval for the mean is much narrower.
(d) **Correct.** Coverage is a property of the rule that produced the interval.
(e) **Incorrect.** A prediction interval for a future observation is wider because it includes the
observation's own variability. The probability statement would also refer to the procedure, not to this
particular interval.

**11.** *(Strategy: Chebyshev bounds the probability by variance divided by $\varepsilon^2$.)*

(a) With $\mu=3.5$ and $\sigma^2=35/12=2.9167$,

$$\Pr(\lvert\bar{X}-3.5\rvert\ge0.5)\le\frac{\operatorname{Var}(\bar{X})}{0.5^2}
=\frac{35/12}{n(0.25)}=\frac{2.9167}{0.25n}=\frac{11.667}{n}.$$

(b) Set $11.667/n\le0.10$: $n\ge116.67$, so $n=117$ rolls are sufficient for the bound.

(c) At $n=117$, the standard error is $\sqrt{2.9167/117}=\sqrt{0.02493}=0.1579$, so $0.5$ is
$0.5/0.1579=3.17$ standard errors. The normal approximation gives
$2(1-\Phi(3.17))\approx0.0015$, about sixty-five times smaller than the Chebyshev bound $0.10$. Chebyshev
must hold for every distribution with finite variance, so it is necessarily loose for the friendly case of
a die.

**12.** *(Strategy: name the mechanism by which the sample differs systematically from the target.)*

(a) **Undercoverage.** Landline ownership is associated with age, region and health; the frame omits
mobile-only adults. Remedy: a mixed frame with random-digit dialling of mobile and landline numbers, plus
weighting.
(b) **Non-response bias.** The $12\%$ who answer may differ from the $88\%$ who do not. Remedy: follow-up
of a random subsample of non-respondents, incentives, and non-response weighting.
(c) **Response bias** from a leading question. The wording presupposes that the policy is an improvement
and invites agreement. Remedy: neutral wording, for example "To what extent do you support or oppose the
new policy?", ideally with a balanced scale.
(d) **Survivorship bias.** Patients who die or stop treatment are excluded, so the observed outcomes are
those of the survivors. Remedy: an intention-to-treat analysis including all randomised patients, with
follow-up of withdrawals.

## Intermediate

**13.** *(Strategy: enumerate the equally likely samples and compute the sampling distribution directly.)*

(a) The population mean is $(2+4+6+8)/4=20/4=5$. The population variance is

$$\sigma^2=\frac{(2-5)^2+(4-5)^2+(6-5)^2+(8-5)^2}{4}
=\frac{9+1+1+9}{4}=\frac{20}{4}=5 .$$

(b) With replacement there are $4^2=16$ equally likely ordered samples. Listing them with their means:

$$(2,2):2,\ (2,4):3,\ (2,6):4,\ (2,8):5,\ (4,2):3,\ (4,4):4,\ (4,6):5,\ (4,8):6,$$
$$(6,2):4,\ (6,4):5,\ (6,6):6,\ (6,8):7,\ (8,2):5,\ (8,4):6,\ (8,6):7,\ (8,8):8 .$$

Hence the sampling distribution is

| $\bar{x}$ | $2$ | $3$ | $4$ | $5$ | $6$ | $7$ | $8$ |
|---|---|---|---|---|---|---|---|
| count | $1$ | $2$ | $3$ | $4$ | $3$ | $2$ | $1$ |

For example, $\bar{x}=3$ arises from $(2,4)$ and $(4,2)$; $\bar{x}=5$ arises from $(2,8),(4,6),(6,4)$
and $(8,2)$.

(c) The mean of the sampling distribution is

$$\mathbb{E}[\bar{X}]=\frac{1(2)+2(3)+3(4)+4(5)+3(6)+2(7)+1(8)}{16}
=\frac{2+6+12+20+18+14+8}{16}=\frac{80}{16}=5 .$$

For the variance, compute

$$\mathbb{E}[\bar{X}^2]=\frac{1(4)+2(9)+3(16)+4(25)+3(36)+2(49)+1(64)}{16}
=\frac{4+18+48+100+108+98+64}{16}=\frac{440}{16}=27.5 .$$

Hence $\operatorname{Var}(\bar{X})=27.5-5^2=2.5=\sigma^2/2$.

(d) The standard error is $\sqrt{2.5}=1.5811$.

*Check.* The counts sum to $1+2+3+4+3+2+1=16$. $\checkmark$

**14.** *(Strategy: use the law of total variance for the population, then the stratified variance formula.)*

(a) The overall mean is

$$\mu=W_1\mu_1+W_2\mu_2=0.6(70)+0.4(85)=42+34=76 .$$

The population variance is

$$\sigma^2=\sum_h W_h\bigl[\sigma_h^2+(\mu_h-\mu)^2\bigr]
=0.6[100+(70-76)^2]+0.4[225+(85-76)^2]$$
$$=0.6(136)+0.4(306)=81.6+122.4=204 .$$

(b) Under simple random sampling of $100$,
$\operatorname{Var}(\bar{X})=\sigma^2/n=204/100=2.04$, so the standard error is $1.4283$.

(c) With proportional allocation, $n_1=60$ and $n_2=40$, and

$$\operatorname{Var}(\bar{X}_{st})=\sum_h\frac{W_h^2\sigma_h^2}{n_h}
=\frac{0.36(100)}{60}+\frac{0.16(225)}{40}=0.6+0.9=1.5 .$$

The standard error is $1.2247$, and the variance ratio is $1.5/2.04=0.7353$: stratification removes
$26.5\%$ of the variance, or $14.2\%$ of the standard error.

(d) The removed part is the between-stratum variance
$\sum_h W_h(\mu_h-\mu)^2=0.6(36)+0.4(81)=21.6+32.4=54$. Since
$204=150+54$, the stratified variance is $150/100=1.5$ against $204/100=2.04$. Stratification exploits
the fact that the strata means differ; the more homogeneous the strata, the larger the gain.

**15.** *(Strategy: equate the first population moment to the first sample moment.)*

For the Poisson, $\mathbb{E}[X]=\lambda$, so $\hat\lambda_{MoM}=\bar{x}=(3+1+4+2+5)/5=15/5=3$.

For the Bernoulli, $\mathbb{E}[X]=p$, so $\hat p_{MoM}=18/60=0.3$.

*Check.* In the Poisson case the sample mean is also the MLE, but that is a coincidence of the
one-parameter exponential family; the method of moments is defined without reference to likelihood.

**16.** *(Strategy: the exponential mean is $1/\lambda$; the likelihood is maximised by the same equation.)*

(a) The sample mean is $(1.2+2.4+0.8+3.6+3.0)/5=11.0/5=2.2$. Since $\mathbb{E}[X]=1/\lambda$, the moment
estimator solves $1/\hat\lambda=2.2$, so $\hat\lambda=1/2.2=0.4545$.

(b) The log-likelihood is

$$\ell(\lambda)=n\log\lambda-\lambda\sum_i x_i=5\log\lambda-11\lambda .$$

Differentiating, $\ell'(\lambda)=5/\lambda-11$; setting it to zero gives $\hat\lambda=5/11=0.4545$. Since
$\ell''(\lambda)=-5/\lambda^2<0$, this is a maximum.

(c) The two estimators coincide because the first moment equation $1/\lambda=\bar{x}$ is exactly the score
equation $n/\lambda-\sum_i x_i=0$ divided by $n$. This happens for one-parameter exponential families in
general when the moment is the sufficient statistic, but not in general.

**17.** *(Strategy: differentiate the log-likelihood, solve, and check the second derivative.)*

(a) For $x=12$ successes in $n=40$ trials,

$$\ell(p)=12\log p+28\log(1-p),\qquad \ell'(p)=\frac{12}{p}-\frac{28}{1-p}.$$

Setting $\ell'=0$ gives $12(1-p)=28p$, hence $12=40p$ and $\hat p=12/40=0.3$. Also
$\ell''(p)=-12/p^2-28/(1-p)^2<0$, so it is a maximum.

(b) The values are

| $p$ | $\ell(p)$ |
|---|---|
| $0.25$ | $12\log0.25+28\log0.75=-16.6355-8.0551=-24.691$ |
| $0.30$ | $12\log0.30+28\log0.70=-14.4477-9.9868=-24.435$ |
| $0.40$ | $12\log0.40+28\log0.60=-10.9955-14.3031=-25.299$ |

The largest is at $p=0.30$, the MLE.

(c) At $p=0.30$, $12/0.30=40$ and $28/0.70=40$, so $\ell'(0.30)=40-40=0$.

*Check.* The likelihood is maximised where the observed proportion of successes equals the model's
probability; this is the general Bernoulli result. $\checkmark$

**18.** *(Strategy: use linearity for $2\bar{X}$ and the distribution of the maximum for $M$.)*

(a) Since $X_i\sim$ Uniform$(0,\theta)$, $\mathbb{E}[X_i]=\theta/2$. By linearity,
$\mathbb{E}[2\bar{X}]=2(\theta/2)=\theta$, so $2\bar{X}$ is unbiased.

(b) The distribution function of $M$ is

$$F_M(m)=\Pr(M\le m)=\Pr(X_1\le m,\dots,X_n\le m)=\left(\frac{m}{\theta}\right)^n,\qquad0\le m\le\theta .$$

Differentiating, the density is $f_M(m)=nm^{n-1}/\theta^n$, so

$$\mathbb{E}[M]=\int_0^\theta m\,\frac{nm^{n-1}}{\theta^n}\,dm
=\frac{n}{\theta^n}\cdot\frac{\theta^{n+1}}{n+1}=\frac{n}{n+1}\theta .$$

Hence the bias is $\frac{n}{n+1}\theta-\theta=-\frac{\theta}{n+1}$.

(c) To make $cM$ unbiased, solve $c\frac{n}{n+1}\theta=\theta$, so $c=(n+1)/n$. For $n=5$,
$c=6/5$ and the bias of $M$ is $-\theta/6$.

*Pitfall.* $2\bar{X}$ is unbiased but can exceed $\theta$; $M$ is biased but never exceeds $\theta$. Which
is preferable depends on the loss function: the variance of $M$ is
$n\theta^2/[(n+2)(n+1)^2]=O(\theta^2/n^2)$, against $O(\theta^2/n)$ for $2\bar{X}$, so $M$ has the smaller
MSE for $n\ge3$ (the two are equal at $n=2$) despite its bias.

**19.** *(Strategy: MSE $=$ bias$^2$ $+$ variance, then Chebyshev.)*

(a) $\operatorname{MSE}=(1/n)^2+4/n=1/n^2+4/n$.

(b) By Chebyshev,

$$\Pr(\lvert\hat\theta_n-\theta\rvert>0.5)\le\frac{\operatorname{MSE}}{0.5^2}
=\frac{1/n^2+4/n}{0.25}=4\left(\frac{1}{n^2}+\frac{4}{n}\right).$$

(c) Require $4(1/n^2+4/n)\le0.05$, i.e. $1/n^2+4/n\le0.0125$. Multiplying by $n^2>0$,

$$1+4n\le0.0125n^2\iff0.0125n^2-4n-1\ge0 .$$

The positive root is

$$n=\frac{4+\sqrt{16+0.05}}{0.025}=\frac{4+4.00624}{0.025}=320.25,$$

so $n=321$ is the smallest integer. At $n=321$ the bound is $4(1/321^2+4/321)=0.04988\le0.05$.

*Check.* At $n=320$ the bound is $0.05004>0.05$, so the rounding matters. $\checkmark$

**20.** *(Strategy: relative efficiency is a ratio of variances; translate it into a sample-size ratio.)*

(a) The variance of the median is $\pi\sigma^2/(2n)$ and that of the mean is $\sigma^2/n$, so

$$\frac{\operatorname{Var}(\text{median})}{\operatorname{Var}(\text{mean})}
=\frac{\pi}{2}\approx1.571 .$$

The mean is $1.571$ times as efficient; equivalently, the median's relative efficiency is
$2/\pi\approx0.637$.

(b) To match the mean's variance at $n_{\text{mean}}=100$, the median needs
$n_{\text{median}}=(\pi/2)(100)=157.08$, so $158$ observations.

(c) The comparison assumes a normal population. For heavy-tailed or contaminated data the mean's variance
can be much larger, and for the Cauchy distribution the population mean does not even exist while the
median is well behaved. The mean is preferred when the data are approximately normal and outliers are
absent; the median when robustness matters.

**21.** *(Strategy: compute the sample standard deviation, then use $t_{n-1}$.)*

The sum is $50.0$, so $\bar{x}=5.0$. The deviations are
$-0.9,-0.6,-0.3,-0.1,0,0,0.1,0.3,0.6,0.9$, whose squares sum to

$$0.81+0.36+0.09+0.01+0+0+0.01+0.09+0.36+0.81=2.54 .$$

Hence $s^2=2.54/9=0.28222$ and $s=0.53125$. The standard error is
$s/\sqrt{10}=0.53125/3.1623=0.16799$. With $t_{9,0.975}=2.2622$,

$$5.0\pm2.2622(0.16799)=5.0\pm0.3800=[4.620,\ 5.380].$$

*Check.* The interval is symmetric about $5$ and much narrower than the range $[4.1,5.9]$, as expected for
a mean of ten observations. $\checkmark$

**22.** *(Strategy: pool the variances, then use the two-sample $t$ formula with $n_1+n_2-2$ degrees of
freedom.)*

The pooled variance is

$$s_p^2=\frac{(10-1)(4.2)^2+(12-1)(3.6)^2}{10+12-2}
=\frac{9(17.64)+11(12.96)}{20}=\frac{158.76+142.56}{20}=\frac{301.32}{20}=15.066 .$$

Hence $s_p=\sqrt{15.066}=3.8815$. The standard error of the difference is

$$\operatorname{SE}=s_p\sqrt{\frac1{10}+\frac1{12}}
=3.8815\sqrt{0.183333}=3.8815(0.428174)=1.66196 .$$

With $20$ degrees of freedom, $t_{20,0.975}=2.086$, so the margin is $2.086(1.66196)=3.4668$ and the
interval is

$$(32.4-28.1)\pm3.4668=4.3\pm3.4668=[0.833,\ 7.767].$$

The interval excludes zero, so the data suggest a positive difference at the $5\%$ level. Welch's
interval would be slightly wider because the sample sizes and standard deviations differ.

## Advanced

**23.** *(Strategy: expand the variance of a sum and count the covariance terms.)*

(a) For correlated observations with common variance $\sigma^2$ and common covariance $\rho\sigma^2$,

$$\operatorname{Var}(\bar{X})=\frac{1}{n^2}\left[\sum_i\operatorname{Var}(X_i)
+2\sum_{i<j}\operatorname{Cov}(X_i,X_j)\right]
=\frac{1}{n^2}\left[n\sigma^2+2\cdot\frac{n(n-1)}{2}\rho\sigma^2\right]
=\frac{\sigma^2}{n}\bigl[1+(n-1)\rho\bigr].$$

(b) For $n=2$ and $\rho=0.5$, $\operatorname{Var}(\bar{X})=\sigma^2(1+0.5)/2=0.75\sigma^2$, compared with
$0.5\sigma^2$ in the independent case: the positive correlation inflates the variance by $50\%$.

(c) As $n\to\infty$ with $\rho>0$ fixed,
$\operatorname{Var}(\bar{X})=\sigma^2[1/n+(1-1/n)\rho]\to\rho\sigma^2>0$. The sample mean does not
converge to $\mu$ in probability, so it is inconsistent. Dependence, not sample size, is the obstacle; this
is why cluster sampling and time series need special treatment.

**24.** *(Strategy: use the given bias and variance, then compare MSEs by cross-multiplication.)*

(a) From the general result $\mathbb{E}[s^2]=\sigma^2$ and
$\hat\sigma^2=\frac{n-1}{n}s^2$,

$$\mathbb{E}[\hat\sigma^2]=\frac{n-1}{n}\sigma^2,\qquad
\operatorname{Bias}(\hat\sigma^2)=-\frac{\sigma^2}{n}.$$

(b) $\operatorname{MSE}(\hat\sigma^2)=\frac{\sigma^4}{n^2}+\frac{2(n-1)\sigma^4}{n^2}
=\frac{(2n-1)\sigma^4}{n^2}$.

(c) The unbiased estimator has $\operatorname{MSE}(s^2)=\operatorname{Var}(s^2)=2\sigma^4/(n-1)$.
Compare

$$\frac{2n-1}{n^2}\quad\text{with}\quad\frac{2}{n-1}.$$

Cross-multiplying positive quantities, $(2n-1)(n-1)=2n^2-3n+1<2n^2$ for $n\ge1$. Hence the MLE has the
smaller MSE for every $n\ge2$, despite being biased. This is the bias–variance trade-off in its simplest
form.

**25.** *(Strategy: compute bias and variance, write the MSE, and differentiate.)*

(a) $\mathbb{E}[\hat\mu_c]=c\mu$, so the bias is $(c-1)\mu$. Also
$\operatorname{Var}(\hat\mu_c)=c^2\operatorname{Var}(\bar{X})=c^2\sigma^2/n$.

(b) By Proposition 8.3,

$$\operatorname{MSE}(c)=(c-1)^2\mu^2+\frac{c^2\sigma^2}{n}.$$

Differentiating with respect to $c$,

$$\frac{d}{dc}\operatorname{MSE}=2(c-1)\mu^2+\frac{2c\sigma^2}{n}.$$

Setting this to zero gives

$$c\left(\mu^2+\frac{\sigma^2}{n}\right)=\mu^2,\qquad
c^*=\frac{\mu^2}{\mu^2+\sigma^2/n}.$$

The second derivative is $2\mu^2+2\sigma^2/n>0$, so this is a minimum.

(c) The optimal constant is between $0$ and $1$: the estimator shrinks the sample mean towards zero. The
amount of shrinkage is governed by the signal-to-noise ratio $\mu^2/(\sigma^2/n)$. When the mean is large
relative to its standard error, $c^*\approx1$ and little shrinkage occurs; when the noise is large,
$c^*$ is small and shrinkage substantially reduces variance at the cost of bias. If $\mu=0$, the optimal
estimator is $0$, which is correct but useless without prior knowledge that $\mu$ is near zero. The
exercise illustrates why shrinkage estimators require a model of the prior or a constraint.

**26.** *(Strategy: use linearity of expectation and the chi-square interpretation of the sample
variance.)*

(a) Each $s_i^2$ is unbiased for $\sigma^2$, so

$$\mathbb{E}[s_p^2]=\frac{(n_1-1)\sigma^2+(n_2-1)\sigma^2}{n_1+n_2-2}
=\frac{(n_1+n_2-2)\sigma^2}{n_1+n_2-2}=\sigma^2 .$$

(b) Write

$$s_p^2=\frac{n_1-1}{n_1+n_2-2}s_1^2+\frac{n_2-1}{n_1+n_2-2}s_2^2,$$

a weighted average with positive weights summing to $1$.

(c) For normal samples, $(n_i-1)s_i^2/\sigma^2\sim\chi^2_{n_i-1}$ independently, so the sum
$[(n_1-1)s_1^2+(n_2-1)s_2^2]/\sigma^2$ is $\chi^2_{n_1+n_2-2}$. The $t$ statistic is the ratio of a
standard normal to the square root of an independent chi-square divided by its degrees of freedom, and the
independence of $\bar{X}_1-\bar{X}_2$ from the two sample variances gives $n_1+n_2-2$ degrees of freedom.

**27.** *(Strategy: solve the margin-of-error equation, then bound $p(1-p)$.)*

(a) The margin of error is $E=z\sqrt{p(1-p)/n}$. Squaring,

$$E^2=\frac{z^2p(1-p)}{n}\quad\Longrightarrow\quad n=\frac{z^2p(1-p)}{E^2}.$$

(b) Complete the square:

$$p(1-p)=\frac14-\left(p-\frac12\right)^2\le\frac14,$$

with equality exactly at $p=1/2$.

(c) With $z=1.96$, $z^2=3.8416$. For $E=0.02$ and no prior guess, $p=1/2$:

$$n=\frac{3.8416(0.25)}{0.0004}=\frac{0.9604}{0.0004}=2401 .$$

With $p=0.1$:

$$n=\frac{3.8416(0.09)}{0.0004}=\frac{0.345744}{0.0004}=864.36,$$

so $865$ observations are required. The prior estimate nearly triples the efficiency, which is why pilot
studies are valuable.

**28.** *(Strategy: use the quadratic of Proposition 8.8 and bound the width using $p(1-p)\le1/4$.)*

(a) By Proposition 8.8, the endpoints of the Wilson interval are the two roots of

$$(n+z^2)p^2-(2n\hat p+z^2)p+n\hat p^2=0,$$

which is the expansion of $n(\hat p-p)^2=z^2p(1-p)$. Substituting either root makes the quadratic vanish,
hence satisfies $(\hat p-p)^2=z^2p(1-p)/n$ with equality. Those are exactly the parameter values for which
the score statistic equals $\pm z$; values between the roots satisfy the inequality strictly.

(b) The width is twice the half-width:

$$W=\frac{2z\sqrt{\dfrac{\hat p(1-\hat p)}{n}+\dfrac{z^2}{4n^2}}}{1+\dfrac{z^2}{n}}.$$

Since $\hat p(1-\hat p)\le1/4$,

$$W\le\frac{2z\sqrt{\dfrac{1}{4n}+\dfrac{z^2}{4n^2}}}{1+\dfrac{z^2}{n}}
=\frac{z\sqrt{\dfrac1n+\dfrac{z^2}{n^2}}}{1+\dfrac{z^2}{n}}
=\frac{z}{\sqrt n}\cdot\frac{\sqrt{1+z^2/n}}{1+z^2/n}
=\frac{z}{\sqrt n}\cdot\frac{1}{\sqrt{1+z^2/n}}<\frac{z}{\sqrt n}.$$

As $n\to\infty$, $z^2/n\to0$, so the centre $\hat p+z^2/(2n)\to\hat p$, the factor
$1/(1+z^2/n)\to1$, and $W\to2z\sqrt{\hat p(1-\hat p)/n}$, the Wald width.

(c) For $24$ successes in $80$: $\hat p=0.30$, $z=1.96$, $z^2=3.8416$. The Wilson interval is
$[0.2106,\ 0.4077]$, while the Wald interval is $[0.1996,\ 0.4004]$. The Wilson interval is shifted
towards $0.5$ and wider, reflecting the asymmetry of the binomial away from the centre. Its width
$0.1971$ is below $z/\sqrt n=1.96/\sqrt{80}=0.2191$, as part (b) guarantees.

**29.** *(Strategy: condition on the stratum and use the law of total variance.)*

(a) Let $H$ be the stratum label, with $\Pr(H=h)=W_h$. Then
$\mathbb{E}[X\mid H=h]=\mu_h$ and $\operatorname{Var}(X\mid H=h)=\sigma_h^2$. The law of total variance
gives

$$\sigma^2=\operatorname{Var}(X)=\mathbb{E}[\operatorname{Var}(X\mid H)]
+\operatorname{Var}(\mathbb{E}[X\mid H])
=\sum_h W_h\sigma_h^2+\sum_h W_h(\mu_h-\mu)^2 .$$

Directly: write $X-\mu=(X-\mu_H)+(\mu_H-\mu)$; the cross term has conditional mean zero within each
stratum and therefore vanishes.

(b) With $n_h=nW_h$,

$$\operatorname{Var}(\bar{X}_{st})=\sum_h\frac{W_h^2\sigma_h^2}{n_h}
=\sum_h\frac{W_h^2\sigma_h^2}{nW_h}=\frac1n\sum_h W_h\sigma_h^2 .$$

(c) By (a),

$$\frac{\sigma^2}{n}=\frac1n\sum_h W_h\sigma_h^2+\frac1n\sum_h W_h(\mu_h-\mu)^2
\ge\frac1n\sum_h W_h\sigma_h^2,$$

with equality exactly when every $\mu_h=\mu$. Hence proportional stratification never has larger variance
than SRS, and the gain is the between-stratum term.

**30.** *(Strategy: the empirical distribution has a known variance; average $n$ independent draws from
it.)*

(a) The empirical distribution puts mass $1/n$ on each $x_i$. Its mean is $\bar{x}$ and its variance is

$$\frac1n\sum_i(x_i-\bar{x})^2=\frac{n-1}{n}s^2 .$$

A bootstrap sample consists of $n$ independent draws from this distribution, so the variance of its mean
is

$$\operatorname{Var}^*(\bar{X}^*)=\frac{1}{n}\cdot\frac{n-1}{n}s^2=\frac{n-1}{n^2}s^2 .$$

Hence $\operatorname{SE}^*=s\sqrt{n-1}/n$.

(b) For $2,3,5,8,12$: $\bar{x}=6$, the deviations are $-4,-3,-1,2,6$, the sum of squares is
$16+9+1+4+36=66$, and $s^2=66/4=16.5$. Hence $\operatorname{Var}^*=4(16.5)/25=2.64$ and
$\operatorname{SE}^*=1.6248$. By comparison, $s^2/n=16.5/5=3.3$ and $s/\sqrt5=1.8166$.

(c) The bootstrap standard error is smaller by the factor $\sqrt{(n-1)/n}$, which is $0.894$ at $n=5$ and
$0.995$ at $n=200$. The difference arises because the empirical distribution uses the divisor $n$ and
because the bootstrap resamples are drawn from a distribution whose mean is already estimated. For
moderate or large $n$ it is negligible compared with Monte Carlo error; for very small $n$ it is a symptom
of the bootstrap's limited information.

## Challenge

**31.** *(Strategy: impose unbiasedness, then minimise a quadratic subject to a linear constraint.)*

(a) $\mathbb{E}[\hat\mu]=\sum_i a_i\mathbb{E}[X_i]=\mu\sum_i a_i$. For this to equal $\mu$ for every
$\mu$, we need $\sum_i a_i=1$.

(b) Minimise $\sum_i a_i^2$ subject to $\sum_i a_i=1$. By Cauchy–Schwarz,

$$\left(\sum_i a_i\right)^2\le n\sum_i a_i^2,$$

so $\sum_i a_i^2\ge1/n$, with equality exactly when all $a_i$ are equal. The constraint then gives
$a_i=1/n$. Equivalently, the Lagrange multiplier equations $2a_i=\lambda$ force all $a_i$ equal.

(c) The variance is $\sigma^2\sum_i a_i^2\ge\sigma^2/n$, with equality at $a_i=1/n$, which is $\bar{X}$.
Hence $\bar{X}$ is the best linear unbiased estimator. For an arbitrary unbiased linear estimator, the
variance ratio is

$$\frac{\operatorname{Var}(\hat\mu)}{\operatorname{Var}(\bar{X})}=n\sum_i a_i^2\ge1 .$$

*Remark.* This is a finite-sample optimality result that does not require normality, only uncorrelatedness
and equal variances. It does not say that $\bar{X}$ is best among all estimators, only among linear
unbiased ones.

**32.** *(Strategy: differentiate the log-likelihood twice and take expectations.)*

(a) $\ell(p)=x\log p+(n-x)\log(1-p)$, so

$$\ell'(p)=\frac{x}{p}-\frac{n-x}{1-p},\qquad
\ell''(p)=-\frac{x}{p^2}-\frac{n-x}{(1-p)^2}.$$

Since $\mathbb{E}[X]=np$,

$$I(p)=-\mathbb{E}[\ell''(p)]=\frac{np}{p^2}+\frac{n(1-p)}{(1-p)^2}
=\frac{n}{p}+\frac{n}{1-p}=\frac{n}{p(1-p)} .$$

Per observation, $I(p)=1/(p(1-p))$.

(b) The Cramér–Rao bound for an unbiased estimator of $p$ is

$$\operatorname{Var}(\hat p)\ge\frac{1}{nI(p)}=\frac{p(1-p)}{n}.$$

The sample proportion has exactly this variance and is unbiased, so it attains the bound and is efficient.

(c) For the exponential rate, $\ell(\lambda)=n\log\lambda-\lambda\sum_i x_i$, so
$\ell''(\lambda)=-n/\lambda^2$ and $I(\lambda)=n/\lambda^2$; per observation $1/\lambda^2$. The asymptotic
variance of $\hat\lambda=1/\bar{X}$ is $\lambda^2/n$, which equals the Cramér–Rao bound. In finite samples
$\hat\lambda$ is biased: $\mathbb{E}[1/\bar{X}]=n\lambda/(n-1)$ for $n>1$, so the bound for unbiased
estimators is attained only in the limit. The MLE is asymptotically efficient.

**33.** *(Strategy: compare likelihoods through the transformation.)*

(a) Let $g$ be bijective and $\phi=g(\theta)$. The induced likelihood is
$L^*(\phi)=L(g^{-1}(\phi))$. For any $\phi$,
$L^*(\phi)=L(g^{-1}(\phi))\le L(\hat\theta)=L^*(\phi_0)$ where $\phi_0=g(\hat\theta)$, because $\hat\theta$
maximises $L$. Hence $\hat\phi=\phi_0=g(\hat\theta)$ maximises $L^*$.

(b) For general $g$, define $L^*(\phi)=\max_{\theta\in g^{-1}(\phi)}L(\theta)$. For any $\phi$ and any
$\theta\in g^{-1}(\phi)$, $L(\theta)\le L(\hat\theta)$, so $L^*(\phi)\le L(\hat\theta)$. But
$\hat\theta\in g^{-1}(g(\hat\theta))$, so $L^*(g(\hat\theta))=L(\hat\theta)$. Hence $g(\hat\theta)$ maximises
$L^*$.

(c) Take $L(\theta)=e^{-\theta^2/2}$, with $\hat\theta=0$, and $g(\theta)=\theta^2$. For $\phi\ge0$,

$$L^*(\phi)=\max_{\theta\in\{-\sqrt\phi,\sqrt\phi\}}e^{-\theta^2/2}=e^{-\phi/2},$$

which is maximised at $\phi=0$. And $g(\hat\theta)=0^2=0$, in agreement. The two parameter values
$\pm\sqrt\phi$ map to the same $\phi$; the induced likelihood takes the larger of their likelihoods, which
is the same by symmetry. Invariance still holds because the definition of $L^*$ maximises over preimages,
not because $g$ has an inverse.

**34.** *(Strategy: compare weighting by sample sizes with weighting by population sizes.)*

(a) The naive pooled estimate ignores the strata:

$$\hat p_{\text{pooled}}=\frac{100(0.2)+100(0.8)}{200}=\frac{20+80}{200}=0.5 .$$

(b) The stratified estimate weights each stratum proportion by its population share:

$$\hat p_{st}=\frac{900}{1000}(0.2)+\frac{100}{1000}(0.8)=0.9(0.2)+0.1(0.8)=0.18+0.08=0.26 .$$

(c) The stratified estimate answers "what is the population proportion?" because the weights reflect the
population composition. The pooled estimate answers "what is the proportion in the sample?" and is
dominated by stratum 2, which contributes half the sample but only a tenth of the population.

(d) This is the same mechanism as Simpson's paradox: a weighted average with weights that differ between
the sample and the population can give a completely different answer. Here the sample is deliberately
over-weighted towards the high-proportion stratum; in an observational comparison, unequal group sizes
play the same role. The remedy is to weight by the population shares (or to analyse the strata
separately).

**35.** *(Strategy: enumerate the binomial distribution and check whether the interval covers the true
$p$ at each possible $x$.)*

(a) The exact coverage is

$$\sum_{x=0}^{n} \binom{n}{x}p^x(1-p)^{n-x}\mathbf 1\{p\in[\hat p-z\hat{\operatorname{SE}},\hat p+z\hat{\operatorname{SE}}]\},$$

with $\hat p=x/n$ and $\hat{\operatorname{SE}}=\sqrt{\hat p(1-\hat p)/n}$. Evaluating:

| setting | Wald coverage |
|---|---|
| $n=20$, $p=0.05$ | $0.6389$ |
| $n=20$, $p=0.5$ | $0.9586$ |
| $n=100$, $p=0.05$ | $0.8775$ |

(b) Wilson coverage:

| setting | Wilson coverage |
|---|---|
| $n=20$, $p=0.05$ | $0.9245$ |
| $n=20$, $p=0.5$ | $0.9586$ |
| $n=100$, $p=0.05$ | $0.9659$ |

(c) Near $p=0$, the most likely observation is $x=0$, for which $\hat p=0$ and the Wald interval is
$[0,0]$, which can never contain $p=0.05$. Other small counts give intervals that are too short and
shifted towards zero. The Wald interval's symmetry and its use of $\hat p$ in the standard error are both
inappropriate near the boundary. The Wilson interval shifts the centre and gives a positive upper limit at
$x=0$, so it covers $p$ in far more samples. This is why Wilson (or Clopper–Pearson) is preferred when
$n\hat p$ or $n(1-\hat p)$ is small.

**36.** *(Strategy: compute the probability that no bootstrap draw equals the maximum.)*

(a) The bootstrap draws $n$ values independently with replacement from the observed sample. The maximum
$M$ is one of the observed values. If $M$ occurs once, the probability that a single draw is not $M$ is
$1-1/n$, so

$$\Pr(M^*=M)=1-\Pr(\text{no draw equals }M)=1-\left(1-\frac1n\right)^n .$$

If $M$ occurs $k$ times, the same argument gives $1-(1-k/n)^n$; the formula in the question is the
generic case of a unique maximum.

(b) The values are

| $n$ | $1-(1-1/n)^n$ |
|---|---|
| $5$ | $0.6723$ |
| $20$ | $0.6415$ |
| $100$ | $0.6340$ |
| $\infty$ | $1-e^{-1}=0.6321$ |

So in large samples the bootstrap maximum equals the observed maximum in about $63\%$ of resamples.

(c) The nonparametric bootstrap distribution of $M^*$ is supported on the observed values, all of which
are at most $M$. It cannot produce values between $M$ and $\theta$, yet the sampling distribution of $M$
has substantial mass in that region: $M$ underestimates $\theta$ by a term of order $\theta/n$. The
bootstrap therefore cannot approximate the distribution of $M-\theta$; it is centred at $M$, not at
$\theta$, and its spread reflects the gaps between the largest observations rather than the distance to
the boundary. A *parametric* bootstrap that simulates from Uniform$(0,M)$ does work here, because the
pivot $M/\theta$ is distribution-free: if $M^*$ is the maximum of $n$ uniform$(0,M)$ draws, then $M^*/M$
has the same Beta$(n,1)$ distribution as $M/\theta$, so the simulated distribution of $M^*-M$ mimics that
of $M-\theta$. The lesson is that the bootstrap is not automatically nonparametric; the resampling scheme
must respect the structure of the problem.
