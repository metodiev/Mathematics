# Sampling and Estimation

> [Statistics](../README.md) · Level: Intermediate · Prerequisites: [Descriptive Statistics](../01-descriptive-statistics/README.md), [Probability Foundations](../../10-probability/01-probability-foundations/README.md), [Limits](../../07-calculus/01-limits/README.md) · Estimated time: 540 min

## 1. Introduction

Descriptive statistics summarises what was observed. Sampling and estimation answers the harder question:
what does the sample say about the population it came from? A poll of $1{,}000$ voters is used to forecast
an election; a clinical trial of $200$ patients is used to license a drug; a sample of $50$ components is
used to certify a production line. In each case a *statistic* computed from the sample is treated as
evidence about a *parameter* of a much larger population, and in each case the inference can fail because
the sample was badly chosen or because the statistic is noisy.

Three questions organise the theory. **How should the sample be chosen?** Probability sampling gives every
unit a known chance of selection and makes the sampling distribution calculable; non-probability samples
do not, and no amount of arithmetic repairs them. **How precise is a statistic?** The sampling
distribution of an estimator describes its variability from sample to sample, and its standard deviation
is the standard error. **How should a parameter be estimated, and with what uncertainty?** Point
estimators such as the sample mean and the maximum-likelihood estimator answer the first part; confidence
intervals answer the second.

The subject has a short, sharp history. Laplace and Gauss used least squares and normal approximations
around 1800; Gossett ("Student") derived the $t$ distribution in 1908 while working for Guinness;
R. A. Fisher introduced maximum likelihood, sufficiency and the analysis of variance between 1912 and
1925; Jerzy Neyman formulated confidence intervals and the modern theory of sampling in the 1930s; and
Bradley Efron introduced the bootstrap in 1979. Each idea replaced an approximation by a procedure with a
stated guarantee, and each came with assumptions that are easy to forget.

This topic is the bridge from probability to all of inferential statistics. Hypothesis testing (the next
topic) asks whether a parameter could plausibly take a specified value; regression estimates conditional
means; Bayesian statistics replaces sampling distributions by posterior distributions. Every one of them
uses the sampling distribution, the standard error and the confidence-interval logic developed here.

## 2. Prerequisites

* **Descriptive statistics** — mean, variance, standard deviation, quantiles, $z$-scores and the
  distinction between population and sample:
  [Descriptive Statistics](../01-descriptive-statistics/README.md).
* **Probability** — random variables, expectation, variance, independence, the normal, binomial,
  exponential and chi-square distributions, and the central limit theorem:
  [Probability Foundations](../../10-probability/01-probability-foundations/README.md).
* **Limits and convergence** — $\lim_{n\to\infty}a_n$, and the idea of convergence in probability, used
  for consistency and the law of large numbers: [Limits](../../07-calculus/01-limits/README.md).
* **Logarithms and calculus** — differentiating $\log L(\theta)$ and solving score equations for maximum
  likelihood:
  [Exponential and Logarithmic Functions](../../03-algebra/12-exponential-and-logarithmic-functions/README.md)
  and [Derivatives](../../07-calculus/03-derivatives/README.md).
* **Proof technique** — the Chebyshev argument for consistency uses inequalities and limits:
  [Proof Techniques](../../00-foundations/04-proof-techniques/README.md).

## 3. Learning Objectives

After this tutorial you will be able to:

1. Explain the principal probability sampling designs and the main sources of survey bias.
2. Derive $\mathbb{E}[\bar{X}]=\mu$ and $\operatorname{Var}(\bar{X})=\sigma^2/n$, and define the standard
   error.
3. State the central limit theorem and the law of large numbers, and explain what neither of them says.
4. Define unbiasedness, consistency, efficiency and the mean squared error, and prove
   $\operatorname{MSE}=\text{bias}^2+\text{variance}$.
5. Construct method-of-moments estimators for the Bernoulli, exponential, normal and uniform parameters.
6. Derive maximum-likelihood estimators for the Bernoulli, exponential, normal and uniform parameters, and
   explain the failure of regularity in the uniform case.
7. Compute and interpret confidence intervals for a mean with known and unknown variance, for a
   proportion, and for a difference of means.
8. Explain precisely what "95% confidence" means, and what it does not mean.
9. Choose a sample size for a required margin of error, for a mean or a proportion.
10. Describe the bootstrap, compute a bootstrap standard error in simple cases, and state its limitations.

## 4. Intuition

**Tasting soup.** A cook tastes a spoonful to judge the pot. The spoonful is a sample; the pot is the
population; the cook's inference assumes the soup is well mixed. Stirring is randomisation: it gives every
molecule a chance to enter the spoon. A spoonful from an unstirred pot is a biased sample, and a larger
spoon does not fix it.

**The sampling distribution.** Imagine drawing many samples of size $n$ and computing the mean each time.
The histogram of those means is the sampling distribution of $\bar{X}$. It is centred at the population
mean $\mu$ and its spread shrinks as $n$ grows, like $1/\sqrt{n}$. This is the single most important fact
in the topic: quadrupling the sample halves the standard error, so reducing uncertainty by a factor of
$10$ costs $100$ times the data.

**Bias and variance as a rifle.** An estimator is a rule for shooting at a target. *Bias* is the average
distance of the bullet cluster from the bullseye; *variance* is the size of the cluster. A rifle with a
sights error is biased: more shots do not help. A rifle with a loose barrel is unbiased but imprecise:
more shots average out. The mean squared error combines both, and an estimator with a little bias and much
less variance can beat an unbiased one.

**Confidence intervals as a net.** A $95\%$ confidence interval is a net thrown repeatedly at a moving
fish. The net is constructed by a rule that catches the fish in $95\%$ of throws. After one throw, the net
either contains the fish or not; the probability statement is about the rule, not about the particular
interval. Saying "there is a $95\%$ probability that $\mu$ lies in $[98.4,106.2]$" is, under the
frequentist interpretation used here, a category error, although it is often a harmless approximation to a
Bayesian statement.

**The bootstrap.** If the sample were the population, we could simulate the sampling distribution by
drawing many samples from it. The bootstrap does exactly that: it treats the empirical distribution as a
stand-in for the population and resamples with replacement. It is a computational answer to a question
that is often analytically intractable, and it works for the same reason the plug-in principle works — the
empirical distribution converges to the true one.

## 5. Formal Definition

**Definition 5.1 (Parameter, statistic, estimator, estimate).** A *parameter* $\theta$ is a numerical
characteristic of a population distribution, belonging to a parameter space $\Theta$. A *statistic* is a
function of the sample that does not depend on $\theta$. An *estimator* $\hat\theta$ is a statistic used to
estimate $\theta$; it is a random variable before the data are observed. An *estimate* is its realised
value.

**Definition 5.2 (Probability sampling designs).** A *simple random sample* (SRS) of size $n$ gives every
subset of size $n$ the same probability. *Stratified sampling* divides the population into strata and
samples independently within each stratum. *Cluster sampling* selects whole groups (clusters) and observes
every unit in the selected clusters. *Systematic sampling* selects every $k$-th unit from a randomly
chosen start. *Multistage sampling* combines these, for example selecting counties, then schools, then
pupils. In a *probability sample* every unit has a known, positive inclusion probability; otherwise the
sample is *non-probability* (convenience, voluntary response, quota, snowball).

**Definition 5.3 (Sampling distribution and standard error).** The *sampling distribution* of a statistic
$T$ is its probability distribution over repeated samples under the sampling design. Its standard
deviation is the *standard error*: $\operatorname{SE}(T)=\sqrt{\operatorname{Var}(T)}$. When the standard
error depends on unknown parameters, an *estimated standard error* replaces them by estimates.

**Definition 5.4 (Bias, variance, MSE, consistency, efficiency).** For an estimator $\hat\theta$ of
$\theta$,

$$\operatorname{Bias}(\hat\theta)=\mathbb{E}[\hat\theta]-\theta,\qquad
\operatorname{MSE}(\hat\theta)=\mathbb{E}[(\hat\theta-\theta)^2].$$

The estimator is *unbiased* if the bias is zero for every $\theta\in\Theta$. It is *consistent* if
$\hat\theta_n\xrightarrow{p}\theta$ as $n\to\infty$: for every $\varepsilon>0$,
$\Pr(\lvert\hat\theta_n-\theta\rvert>\varepsilon)\to0$. For two unbiased estimators, $\hat\theta_1$ is
*more efficient* than $\hat\theta_2$ if $\operatorname{Var}(\hat\theta_1)<\operatorname{Var}(\hat\theta_2)$;
the *relative efficiency* is the ratio of their variances.

**Definition 5.5 (Likelihood, MLE, Fisher information).** For data $x_1,\dots,x_n$ with joint density or
mass $f(x_1,\dots,x_n;\theta)$, the *likelihood* is $L(\theta)=f(x_1,\dots,x_n;\theta)$ read as a function
of $\theta$ for fixed data, and the *log-likelihood* is $\ell(\theta)=\log L(\theta)$. The
*maximum-likelihood estimator* (MLE) is $\hat\theta=\arg\max_{\theta\in\Theta}\ell(\theta)$. For
differentiable densities, the *score* is $\ell'(\theta)$ and the *Fisher information* is
$I(\theta)=\mathbb{E}[(\ell'(\theta))^2]=-\mathbb{E}[\ell''(\theta)]$ when the interchange of derivative
and integral is justified.

**Definition 5.6 (Confidence interval and coverage).** A $100(1-\alpha)\%$ *confidence interval* for
$\theta$ is a pair of statistics $[L(X),U(X)]$ such that
$\Pr_\theta(L(X)\le\theta\le U(X))\ge1-\alpha$ for every $\theta\in\Theta$. The probability is the
*coverage* of the procedure over repeated samples. A *one-sided* interval replaces one endpoint by
$-\infty$ or $+\infty$.

**Definition 5.7 (Margin of error).** For a two-sided interval of the form $\hat\theta\pm E$, the
*margin of error* is $E$, the half-width. It is usually a multiple of the standard error.

**Definition 5.8 (Bootstrap sample and bootstrap distribution).** Given data $x_1,\dots,x_n$, let
$\hat F_n$ be the empirical distribution putting mass $1/n$ on each observation. A *bootstrap sample*
$x_1^*,\dots,x_n^*$ is a sample of size $n$ drawn independently with replacement from $\hat F_n$. The
*bootstrap distribution* of a statistic $T$ is its distribution over repeated bootstrap samples. The
*bootstrap standard error* is the standard deviation of that distribution, and a *percentile interval*
takes its $(\alpha/2)$ and $(1-\alpha/2)$ quantiles.

## 6. Mathematical Notation

| Symbol | Read as | Meaning |
|---|---|---|
| $\theta$, $\Theta$ | theta, capital theta | parameter; parameter space |
| $\hat\theta$ | theta hat | estimator or estimate of $\theta$ |
| $\mu$, $\sigma^2$ | mu, sigma squared | population mean and variance |
| $\bar{X}$, $\bar{x}$ | $X$ bar, $x$ bar | sample mean as a random variable; its observed value |
| $s^2$, $s$ | $s$ squared, $s$ | sample variance and standard deviation (divisor $n-1$) |
| $\operatorname{SE}$, $\widehat{\operatorname{SE}}$ | standard error | standard deviation of a statistic; its estimate |
| $p$, $\hat p$ | $p$, $p$ hat | population proportion; sample proportion |
| $\alpha$, $1-\alpha$ | alpha, confidence level | tail probability; confidence level |
| $z_{1-\alpha/2}$ | z critical value | the $1-\alpha/2$ quantile of $\mathcal N(0,1)$ |
| $t_{\nu,1-\alpha/2}$ | t critical value | the $1-\alpha/2$ quantile of $t_\nu$ |
| $\nu$ | nu | degrees of freedom |
| $\operatorname{Bias}$, $\operatorname{MSE}$ | bias, M-S-E | bias; mean squared error |
| $L(\theta)$, $\ell(\theta)$ | likelihood, log-likelihood | joint density as a function of $\theta$; its logarithm |
| $I(\theta)$ | Fisher information | expected squared score |
| $\xrightarrow{p}$, $\xrightarrow{d}$ | convergence in probability, in distribution | modes of convergence |
| $F_n$, $\hat F_n$ | empirical distribution | the distribution putting mass $1/n$ on each observation |
| $B$ | number of bootstrap replications | computational parameter |
| $N$, $n$ | population size, sample size | finite population; sample |
| $\sigma_{\bar X}$ | standard error of the mean | $\sigma/\sqrt n$ |

## 7. Core Concepts

### 7.1 Sampling methods and bias

The sampling design determines whether inference is possible at all. A probability sample gives every unit
a known positive chance of selection, which makes the sampling distribution — and therefore the standard
error — calculable. A non-probability sample does not, and no arithmetic can supply what the design did not.

**Simple random sampling.** Every subset of size $n$ is equally likely; equivalently, units are drawn
without replacement with equal inclusion probabilities $n/N$. It is the reference design, easy to describe
and analyse, but it may be impractical (a list of all units may not exist) and it ignores information
about strata.

**Stratified sampling.** The population is divided into strata that are internally homogeneous (age groups,
regions, income bands), and an SRS is taken in each. If the strata means differ, the stratified estimator

$$\bar{x}_{st}=\sum_{h=1}^{H}W_h\bar{x}_h,\qquad W_h=N_h/N,$$

has smaller variance than an SRS of the same size. With *proportional allocation* $n_h=nW_h$, its variance
is $\sum_h W_h^2\sigma_h^2/n_h=(1/n)\sum_h W_h\sigma_h^2$, compared with the SRS variance
$\sigma^2/n=(1/n)\bigl[\sum_h W_h\sigma_h^2+\sum_h W_h(\mu_h-\mu)^2\bigr]$; the difference is the
between-stratum term. *Optimal allocation* samples more from strata with larger $N_h\sigma_h$.

**Cluster sampling.** Whole clusters (schools, villages, hospitals) are selected and all their units
observed. It is cheaper when a sampling frame of units is unavailable, but it is less precise than SRS of
the same number of units, because units in a cluster resemble one another. The design effect is often
written $1+(m-1)\rho$ for clusters of size $m$ with intraclass correlation $\rho$; the effective sample
size is the actual size divided by the design effect.

**Systematic and multistage sampling.** Systematic sampling takes every $k$-th unit from a random start; it
behaves like SRS unless the list has a periodic pattern with period $k$. Multistage sampling selects
primary units, then secondary units within them, and is the standard design of large official surveys;
each stage contributes to the design effect.

**Non-probability samples.** *Convenience*, *voluntary response*, *quota* and *snowball* samples are common
and cheap, but cannot estimate a population mean without an unverifiable model of how selection depended on
the variable. The failure is **selection bias**, and it does not shrink with sample size: the 1936 Literary
Digest poll drew $2.4$ million responses from its own readership and predicted the wrong winner, while a
much smaller probability sample was closer.

**Other sources of bias.** *Undercoverage* occurs when the frame omits part of the target population;
*non-response bias* occurs when the people who answer differ systematically from those who do not;
*response bias* arises from question wording, social desirability or interviewer effects; *measurement
bias* from instruments that read consistently high or low; *survivorship bias* from observing only the
units that survived a selection process. **Sampling error** is the random variation that shrinks with
$n$; **non-sampling error** does not, and it is often larger.

### 7.2 The sampling distribution and the standard error

Let $X_1,\dots,X_n$ be independent observations from a population with mean $\mu$ and variance $\sigma^2$.
The sample mean is

$$\bar{X}=\frac1n\sum_{i=1}^{n}X_i .$$

**Mean and variance.** By linearity of expectation,

$$\mathbb{E}[\bar{X}]=\frac1n\sum_{i=1}^{n}\mathbb{E}[X_i]=\frac1n(n\mu)=\mu,$$

so $\bar{X}$ is unbiased. For independent observations,

$$\operatorname{Var}(\bar{X})=\frac{1}{n^2}\sum_{i=1}^{n}\operatorname{Var}(X_i)
=\frac{1}{n^2}(n\sigma^2)=\frac{\sigma^2}{n},$$

so the standard error is

$$\operatorname{SE}(\bar{X})=\frac{\sigma}{\sqrt n}.$$

If the observations are correlated, the cross-covariances do not vanish; the variance becomes
$\frac{\sigma^2}{n}+\frac{2}{n^2}\sum_{i<j}\operatorname{Cov}(X_i,X_j)$, which can be much larger. The
independence assumption is doing real work.

For sampling *without replacement* from a finite population of size $N$, the variance is

$$\operatorname{Var}(\bar{X})=\frac{\sigma^2}{n}\cdot\frac{N-n}{N-1},$$

the *finite population correction*. The factor is close to $1$ when $n\ll N$ and tends to $0$ when $n\to N$,
because a census has no sampling error.

**The central limit theorem.** If $X_1,\dots,X_n$ are iid with mean $\mu$ and finite variance $\sigma^2$,
then

$$\frac{\bar{X}-\mu}{\sigma/\sqrt n}\xrightarrow{d}\mathcal N(0,1)\quad\text{as }n\to\infty .$$

This is why the normal distribution appears in nearly every interval formula below. It is an asymptotic
statement: for finite $n$ the approximation is better when the population is close to normal and worse
when it is strongly skewed or has heavy tails. The rule of thumb "$n\ge30$" is a convention, not a
theorem; for a strongly skewed population a much larger $n$ may be needed.

**The sample proportion.** For $X_1,\dots,X_n\sim\operatorname{Bernoulli}(p)$, the sample proportion
$\hat p=\bar{X}$ has

$$\mathbb{E}[\hat p]=p,\qquad \operatorname{Var}(\hat p)=\frac{p(1-p)}{n},\qquad
\operatorname{SE}(\hat p)=\sqrt{\frac{p(1-p)}{n}},$$

and the central limit theorem gives approximate normality when $np$ and $n(1-p)$ are both moderately
large. The estimated standard error replaces $p$ by $\hat p$.

**The sample variance.** For a normal sample, $\bar{X}$ and $s^2$ are independent and

$$\frac{(n-1)s^2}{\sigma^2}\sim\chi^2_{n-1}.$$

This is Fisher's theorem and is the reason the $t$ distribution arises in §7.7. For non-normal data the
chi-square statement is only approximate, but $s^2$ remains unbiased and consistent.

**Standard deviation versus standard error.** The standard deviation $\sigma$ describes the variability of
individual observations and stays roughly constant as $n$ grows. The standard error $\sigma/\sqrt n$
describes the variability of the mean and shrinks. A statement such as "the mean weight is $70\pm5$ kg"
is ambiguous until one says whether $5$ is the standard deviation of the people or the standard error of
the mean; the latter is smaller by a factor of $\sqrt n$.

### 7.3 The law of large numbers in practice

The *weak law of large numbers* (WLLN) says that for iid observations with finite mean $\mu$,
$\bar{X}_n\xrightarrow{p}\mu$: for every $\varepsilon>0$,

$$\Pr\bigl(\lvert\bar{X}_n-\mu\rvert>\varepsilon\bigr)\to0 .$$

When the variance is finite, Chebyshev's inequality gives the proof and a rate:

$$\Pr\bigl(\lvert\bar{X}_n-\mu\rvert\ge\varepsilon\bigr)\le\frac{\operatorname{Var}(\bar{X}_n)}{\varepsilon^2}
=\frac{\sigma^2}{n\varepsilon^2}.$$

For a fair die ($\mu=3.5$, $\sigma^2=35/12\approx2.917$), the bound for $\varepsilon=0.5$ is
$2.917/(0.25n)=11.667/n$: at $n=100$ it gives at most $11.7\%$, while the normal approximation gives about
$0.34\%$. Chebyshev is valid but very loose. The *strong law* (Kolmogorov) says that
$\Pr(\lim_{n\to\infty}\bar{X}_n=\mu)=1$, a stronger almost-sure statement; it also requires only a finite
mean.

**What the law does not say.** It does not say that a small sample is representative. It does not say
that deviations are "compensated" by opposite deviations: a coin that has produced ten heads is not more
likely to produce tails next, because the coin has no memory. It does not say that a large sample repairs
a biased design: if the expected value of the sampling mechanism is not $\mu$, the sample mean converges
to the wrong number. And it says nothing about the *rate* beyond the $1/\sqrt n$ scale of the standard
error; convergence can be arbitrarily slow for heavy-tailed distributions, whose mean may not even exist.

**The law of small numbers.** The opposite fallacy is to expect small samples to resemble the population
closely. Short runs fluctuate more than intuition suggests: $14$ or more heads in $20$ tosses is not rare,
and a hospital with $20$ deliveries a month can easily record $70\%$ boys. Extreme rates in small
subgroups regress towards the mean as data accumulate.

### 7.4 Point estimators and their properties

An estimator is judged by its distribution over repeated samples. Four properties matter.

**Unbiasedness.** $\hat\theta$ is unbiased if $\mathbb{E}[\hat\theta]=\theta$ for every $\theta$. The sample
mean is unbiased for $\mu$; the sample variance $s^2$ is unbiased for $\sigma^2$ under independent
sampling (proved in [Descriptive Statistics](../01-descriptive-statistics/README.md) §8.5); the sample
proportion $\hat p$ is unbiased for $p$; and $2\bar{X}$ is unbiased for the upper endpoint $\theta$ of a
uniform distribution on $[0,\theta]$, because $\mathbb{E}[2\bar{X}]=2(\theta/2)=\theta$. Biased examples
are equally important: the MLE of a normal variance,
$\hat\sigma^2=\frac1n\sum_i(X_i-\bar{X})^2$, has expectation $\frac{n-1}{n}\sigma^2$, and the MLE of
$\theta$ for a uniform distribution, $M=\max_iX_i$, has expectation $\frac{n}{n+1}\theta$.

Unbiasedness is a property of the *procedure*, not of a particular estimate, and it is not the only virtue.
An unbiased estimator can have enormous variance, and a slightly biased estimator can be far more accurate.

**Consistency.** $\hat\theta_n$ is consistent if $\hat\theta_n\xrightarrow{p}\theta$. A sufficient condition
is that the bias tends to $0$ and the variance tends to $0$: by Chebyshev, for every $\varepsilon>0$,

$$\Pr(\lvert\hat\theta_n-\theta\rvert>\varepsilon)
\le\frac{\mathbb{E}[(\hat\theta_n-\theta)^2]}{\varepsilon^2}
=\frac{\operatorname{Bias}(\hat\theta_n)^2+\operatorname{Var}(\hat\theta_n)}{\varepsilon^2}\to0.$$

The sample mean, $s^2$ and the biased estimators $\frac{n-1}{n}s^2$ and $\frac{n}{n+1}M$ are consistent.
Unbiasedness neither implies nor follows from consistency: $X_1$ is unbiased but inconsistent, while
$\bar{X}_n+1/n$ is biased but consistent.

**Efficiency.** Among unbiased estimators, the smallest variance wins. The *relative efficiency* of
$\hat\theta_1$ to $\hat\theta_2$ is $\operatorname{Var}(\hat\theta_2)/\operatorname{Var}(\hat\theta_1)$.
For a normal sample the median is unbiased but has variance about $\pi/2\approx1.571$ times that of the
mean, so the median needs about $57\%$ more observations for the same precision. The Cramér–Rao bound
(§7.6) is the lower bound for regular problems; irregular problems such as the uniform endpoint can
converge faster than $1/\sqrt n$.

**Mean squared error.** Proposition 8.3 proves
$\operatorname{MSE}(\hat\theta)=\operatorname{Bias}(\hat\theta)^2+\operatorname{Var}(\hat\theta)$: a small
bias can be worth a large reduction in variance, as shrinkage and ridge estimators exploit.

**Asymptotic normality.** Most good estimators satisfy
$\sqrt n(\hat\theta_n-\theta)\xrightarrow{d}\mathcal N(0,V)$; for the MLE, $V=1/I(\theta)$.

### 7.5 The method of moments

The method of moments equates population moments to sample moments. If there are $p$ parameters, write
$\mu_k(\theta_1,\dots,\theta_p)=\mathbb{E}[X^k]$ and $m_k=\frac1n\sum_iX_i^k$, and solve the $p$ equations

$$\mu_k(\theta_1,\dots,\theta_p)=m_k,\qquad k=1,\dots,p,$$

for $\theta_1,\dots,\theta_p$.

**Bernoulli($p$).** $\mathbb{E}[X]=p$ and $m_1=\bar{X}$, so $\hat p_{MoM}=\bar{X}$.

**Exponential($\lambda$).** $\mathbb{E}[X]=1/\lambda$, so $1/\hat\lambda=\bar{X}$ and
$\hat\lambda_{MoM}=1/\bar{X}$.

**Normal($\mu,\sigma^2$).** $\mathbb{E}[X]=\mu$ and $\mathbb{E}[X^2]=\mu^2+\sigma^2$. The first equation
gives $\hat\mu=\bar{X}$; the second gives
$\hat\sigma^2_{MoM}=\frac1n\sum_i(X_i-\bar{X})^2$, the divisor-$n$ variance.

**Uniform$(0,\theta)$.** $\mathbb{E}[X]=\theta/2$, so $\hat\theta_{MoM}=2\bar{X}$. This estimator is
unbiased and consistent, but it can fall below the largest observation, which is impossible for a
uniform$(0,\theta)$ sample; a moment estimator need not respect the parameter space.

**Poisson($\lambda$).** Both moments equal $\lambda$; the first gives $\hat\lambda=\bar{X}$ and the second
gives the sample variance, generally a different number, so the method requires a choice.

Method-of-moments estimators are easy and usually consistent, but can be inefficient, can leave $\Theta$,
and are not invariant under reparameterisation.

### 7.6 Maximum likelihood

The likelihood is the joint density of the data regarded as a function of the parameter. The MLE is the
parameter value under which the observed data are most probable. Because products are awkward, one
maximises the log-likelihood; because the logarithm is increasing, the maximiser is the same.

**Bernoulli.** For $x$ successes in $n$ independent trials,

$$L(p)=p^x(1-p)^{n-x},\qquad \ell(p)=x\log p+(n-x)\log(1-p).$$

Differentiating,

$$\ell'(p)=\frac{x}{p}-\frac{n-x}{1-p}.$$

Setting $\ell'(p)=0$ gives $x(1-p)=p(n-x)$, hence $x=np$ and $\hat p=x/n$. The second derivative

$$\ell''(p)=-\frac{x}{p^2}-\frac{n-x}{(1-p)^2}<0$$

confirms a maximum (for $0<x<n$). The MLE is the sample proportion.

**Exponential.** With rate $\lambda$ and data $x_1,\dots,x_n$,

$$\ell(\lambda)=n\log\lambda-\lambda\sum_i x_i,\qquad \ell'(\lambda)=\frac{n}{\lambda}-\sum_i x_i .$$

Setting $\ell'=0$ gives $\hat\lambda=n/\sum_i x_i=1/\bar{x}$, and
$\ell''(\lambda)=-n/\lambda^2<0$ confirms a maximum.

**Normal.** With $\theta=(\mu,\sigma^2)$,

$$\ell(\mu,\sigma^2)=-\frac n2\log(2\pi)-\frac n2\log\sigma^2
-\frac{1}{2\sigma^2}\sum_i(x_i-\mu)^2 .$$

The partial derivatives are

$$\frac{\partial\ell}{\partial\mu}=\frac{1}{\sigma^2}\sum_i(x_i-\mu),\qquad
\frac{\partial\ell}{\partial\sigma^2}=-\frac{n}{2\sigma^2}+\frac{1}{2\sigma^4}\sum_i(x_i-\mu)^2 .$$

Setting both to zero gives $\hat\mu=\bar{x}$ and
$\hat\sigma^2=\frac1n\sum_i(x_i-\bar{x})^2$. The Hessian is negative definite at this point, so it is a
maximum. Note that the MLE of $\sigma^2$ is biased; the unbiased $s^2$ is not the MLE.

**Uniform$(0,\theta)$.** Here $L(\theta)=\theta^{-n}$ if $\theta\ge\max_i x_i$ and $0$ otherwise. The
likelihood increases as $\theta$ decreases on $[\max_i x_i,\infty)$, so the maximum is at the boundary
$\hat\theta=\max_i x_i$. This is a non-regular problem: the support depends on the parameter, the score at
the maximum is not zero, the usual asymptotic normality fails, and the MLE converges at rate $1/n$ rather
than $1/\sqrt n$. It is still consistent: for $\varepsilon>0$,
$\Pr(\hat\theta\le\theta-\varepsilon)=(1-\varepsilon/\theta)^n\to0$, and $\hat\theta\le\theta$ always.

**Invariance.** If $\hat\theta$ is the MLE of $\theta$ and $g$ is a function, then $g(\hat\theta)$ is the
MLE of $g(\theta)$ under the induced likelihood. For a one-to-one $g$ this follows by reparameterisation;
for a general $g$ it follows by maximising the induced likelihood over the preimages. This is why the MLE
of $\sigma$ is the square root of the MLE of $\sigma^2$.

**Asymptotics and Fisher information.** Under regularity conditions (the support does not depend on
$\theta$, the density is smooth, differentiation under the integral is justified, and the information is
positive), the MLE is consistent and asymptotically normal:

$$\sqrt n(\hat\theta_n-\theta)\xrightarrow{d}\mathcal N\bigl(0,\,I(\theta)^{-1}\bigr),$$

where $I(\theta)$ is the Fisher information per observation. For a Bernoulli parameter,
$I(p)=1/(p(1-p))$, so the asymptotic variance is $p(1-p)/n$, which the sample proportion attains exactly.
For an exponential rate, $I(\lambda)=1/\lambda^2$, so the asymptotic variance is $\lambda^2/n$, again
attained. The Cramér–Rao inequality states that any unbiased estimator has variance at least
$1/(nI(\theta))$ under the same regularity; an estimator attaining it is efficient.

**When maximum likelihood misbehaves.** The parameter may be on the boundary (uniform endpoint, variance
component fixed at zero); the likelihood may be unbounded (mixtures with a component of zero variance);
the model may be non-identifiable (two parameter values giving the same distribution); the sample may be
small and the likelihood surface multimodal. These are not curiosities: they arise routinely in mixed
models, factor analysis and mixture models, and they are why software reports convergence warnings.

### 7.7 Confidence intervals

A confidence interval is built from a *pivot*: a function of the data and the parameter whose distribution
does not depend on the parameter. Solving the inequality that defines a central probability region for
the pivot gives the interval.

**Mean, known variance.** If $X_1,\dots,X_n$ are iid $\mathcal N(\mu,\sigma^2)$ with $\sigma$ known, then

$$Z=\frac{\bar{X}-\mu}{\sigma/\sqrt n}\sim\mathcal N(0,1).$$

For a two-sided $100(1-\alpha)\%$ interval, choose $z_{1-\alpha/2}$ with
$\Pr(-\ z_{1-\alpha/2}\le Z\le z_{1-\alpha/2})=1-\alpha$. Then

$$\Pr\left(\bar{X}-z_{1-\alpha/2}\frac{\sigma}{\sqrt n}\le\mu\le
\bar{X}+z_{1-\alpha/2}\frac{\sigma}{\sqrt n}\right)=1-\alpha,$$

so the interval is

$$\bar{X}\pm z_{1-\alpha/2}\frac{\sigma}{\sqrt n}.$$

The central limit theorem extends it approximately to non-normal data for large $n$.

**Mean, unknown variance.** Replacing $\sigma$ by $s$ introduces extra variability. Fisher's theorem says
that for a normal sample, $\bar{X}$ and $s^2$ are independent and $(n-1)s^2/\sigma^2\sim\chi^2_{n-1}$.
Hence

$$T=\frac{\bar{X}-\mu}{s/\sqrt n}=\frac{Z}{\sqrt{V/(n-1)}},\qquad
Z\sim\mathcal N(0,1),\quad V\sim\chi^2_{n-1},\quad Z\perp\!\!\!\perp V,$$

which is the definition of a $t$ distribution with $n-1$ degrees of freedom. The interval is

$$\bar{X}\pm t_{n-1,1-\alpha/2}\frac{s}{\sqrt n}.$$

The $t$ critical value exceeds the normal one and compensates for estimating $\sigma$. For $n=8$,
$t_{7,0.975}=2.365$ against $z_{0.975}=1.960$; for $n=30$, $t_{29,0.975}=2.045$; the difference vanishes
as $n\to\infty$. The interval assumes a normal population; for large $n$ it is robust to moderate non-normality, but not to
heavy tails or strong skewness in small samples.

**Proportion.** For $\hat p=x/n$, the *Wald* interval is

$$\hat p\pm z_{1-\alpha/2}\sqrt{\frac{\hat p(1-\hat p)}{n}}.$$

It is the textbook formula and it fails badly when $np$ or $n(1-p)$ is small: at $\hat p=0$ it has zero
width, and its actual coverage can be far below the nominal level (Exercise 35). The *Wilson* (score)
interval inverts the
score test instead of linearising it:

$$\frac{\hat p+\dfrac{z^2}{2n}\pm z\sqrt{\dfrac{\hat p(1-\hat p)}{n}+\dfrac{z^2}{4n^2}}}{1+\dfrac{z^2}{n}},$$

with $z=z_{1-\alpha/2}$. It is better behaved near $0$ and $1$, has coverage closer to nominal, and is
the default recommendation for moderate $n$. The *Agresti–Coull* interval adds $z^2/2$ successes and
$z^2/2$ failures and then applies the Wald formula; it is a close and simple approximation to Wilson.
The *Clopper–Pearson* interval is exact — its coverage is at least $1-\alpha$ for every $p$ — but
conservative; it is obtained from beta quantiles.

**Difference of means.** For two independent samples with means $\bar{X}_1,\bar{X}_2$, variances
$s_1^2,s_2^2$ and sizes $n_1,n_2$, the natural estimator of $\mu_1-\mu_2$ is
$\bar{X}_1-\bar{X}_2$ with variance $\sigma_1^2/n_1+\sigma_2^2/n_2$. If the variances are assumed equal,
pool

$$s_p^2=\frac{(n_1-1)s_1^2+(n_2-1)s_2^2}{n_1+n_2-2},$$

and use the $t$ interval with $n_1+n_2-2$ degrees of freedom:

$$(\bar{X}_1-\bar{X}_2)\pm t_{n_1+n_2-2,1-\alpha/2}\,s_p\sqrt{\frac1{n_1}+\frac1{n_2}}.$$

Without the equal-variance assumption, the *Welch* interval uses

$$\operatorname{SE}=\sqrt{\frac{s_1^2}{n_1}+\frac{s_2^2}{n_2}}$$

and the Satterthwaite degrees of freedom

$$\nu=\frac{\left(\dfrac{s_1^2}{n_1}+\dfrac{s_2^2}{n_2}\right)^2}
{\dfrac{(s_1^2/n_1)^2}{n_1-1}+\dfrac{(s_2^2/n_2)^2}{n_2-1}},$$

which is generally not an integer. Welch is the safer default; the pooled interval is slightly shorter when
the equal-variance assumption is true.

**Paired data and one-sided intervals.** For paired measurements, reduce to the differences
$d_i=x_{i1}-x_{i2}$ and apply the one-sample $t$ interval to $\bar d$; treating paired data as independent
usually gives a misleadingly wide interval. Replacing $z_{1-\alpha/2}$ by $z_{1-\alpha}$ and keeping one
side gives a $100(1-\alpha)\%$ one-sided interval, appropriate when only one direction matters.

### 7.8 Interpreting confidence intervals

The correct frequentist statement is about the *procedure*: if samples were drawn repeatedly and the
interval recomputed each time, about $100(1-\alpha)\%$ of the resulting intervals would contain $\theta$.
The probability is attached to the random interval $[L(X),U(X)]$, not to the fixed parameter:
$\Pr_\theta(L(X)\le\theta\le U(X))=1-\alpha$.

After the data are observed, the interval $[98.4,106.2]$ either contains $\mu$ or does not; the frequentist
cannot assign it a probability without a prior. What can be said is that the procedure has $95\%$ coverage,
that the interval is one realisation of it, and that intervals constructed this way fail $5\%$ of the time.
A Bayesian *credible interval* does make a probability statement about $\theta$, but it requires a prior
and answers a different question.

Four further distinctions matter. A $95\%$ confidence interval is **not** an interval containing $95\%$ of
the data; that is a tolerance interval, and it is much wider. It is **not** a prediction interval for a
future observation; prediction intervals include the variability of the observation itself. It does
**not** say that $95\%$ of sample means lie in it. And a $95\%$ interval does **not** have a $95\%$ chance
of being "correct" conditional on the observed data, because the parameter is fixed.

Width is controlled by three quantities: the confidence level (higher confidence, wider interval), the
standard error (larger $\sigma$ or smaller $n$, wider interval), and the sample size (width shrinks like
$1/\sqrt n$). A $99\%$ interval is wider than a $95\%$ interval on the same data; to halve the width at the
same confidence one needs four times the sample size. A very narrow interval from a biased sample is
precisely wrong: precision is not accuracy.

### 7.9 Margin of error and sample-size calculations

For an interval of the form $\hat\theta\pm E$, the margin of error is $E$. For a mean with known $\sigma$,

$$E=z_{1-\alpha/2}\frac{\sigma}{\sqrt n}
\quad\Longrightarrow\quad
n=\left(\frac{z_{1-\alpha/2}\,\sigma}{E}\right)^2,$$

rounded up to the next integer. With unknown $\sigma$, use a pilot estimate $s$ and iterate: start with
$z$, compute $n$, then replace $z$ by $t_{n-1,1-\alpha/2}$ and recompute until $n$ stabilises. For a
proportion,

$$n=\frac{z_{1-\alpha/2}^2\,p(1-p)}{E^2},$$

and when no prior guess for $p$ is available, use the worst case $p=1/2$, which maximises $p(1-p)=1/4$:

$$n=\frac{z_{1-\alpha/2}^2}{4E^2}.$$

The sample size grows like $1/E^2$: halving the margin of error quadruples the sample. A $95\%$ margin of
error of $3$ percentage points for a proportion requires $n\approx1068$ at $p=0.5$; a margin of $1$ point
requires about $9604$. These are the numbers behind "the poll has a margin of error of three points".

Three corrections matter in practice: the finite population factor $(N-n)/(N-1)$; the design effect (for
cluster sampling roughly $1+(m-1)\rho$); and the response rate, since obtaining $n$ interviews at a $60\%$
response rate requires inviting $n/0.6$ units. None repairs non-response bias.

### 7.10 The bootstrap

The bootstrap replaces the unknown population distribution by the empirical distribution $\hat F_n$ and
simulates the sampling distribution. The algorithm is:

1. Draw $B$ bootstrap samples of size $n$ with replacement from $x_1,\dots,x_n$.
2. Compute the statistic $\hat\theta^*_b$ on each sample.
3. Estimate the standard error by the standard deviation of the $\hat\theta^*_b$, and form a percentile
   interval from their $\alpha/2$ and $1-\alpha/2$ quantiles.

The plug-in principle justifies it: $\hat F_n$ converges to $F$, and functionals that depend continuously
on the distribution converge too. For the mean, the bootstrap variance has a closed form. The empirical
distribution has variance $\frac1n\sum_i(x_i-\bar{x})^2=\frac{n-1}{n}s^2$, so the variance of a bootstrap
sample mean is that divided by $n$:

$$\operatorname{Var}^*(\bar{X}^*)=\frac{n-1}{n^2}s^2,\qquad
\operatorname{SE}^*=\frac{s\sqrt{n-1}}{n},$$

slightly smaller than $s/\sqrt n$. For the data $3,5,5,7,10$, $s=2.646$, the bootstrap standard error is
$1.058$ against $s/\sqrt5=1.183$, and the exact percentile interval obtained by enumerating all $5^5=3125$
resamples is $[4.2,8.2]$.

The bootstrap is valuable for complicated statistics (ratios, correlations, quantiles, regression
coefficients) where no analytic standard error exists. It assumes a representative sample and independent
observations; it fails for dependent data, extreme quantiles and maxima (a resample cannot exceed the
observed maximum), and very small $n$. It also reproduces any bias in the original sample.

## 8. Formulas and Properties

**Proposition 8.1 (Mean and variance of the sample mean).** Let $X_1,\dots,X_n$ be independent with
$\mathbb{E}[X_i]=\mu$ and $\operatorname{Var}(X_i)=\sigma^2<\infty$. Then
$\mathbb{E}[\bar{X}]=\mu$ and $\operatorname{Var}(\bar{X})=\sigma^2/n$, so
$\operatorname{SE}(\bar{X})=\sigma/\sqrt n$.

*Proof.* Linearity gives $\mathbb{E}[\bar{X}]=\frac1n\sum_i\mathbb{E}[X_i]=\mu$. Independence makes the
covariances vanish, so
$\operatorname{Var}(\bar{X})=\frac{1}{n^2}\sum_i\operatorname{Var}(X_i)=\frac{n\sigma^2}{n^2}=\frac{\sigma^2}{n}$.
$\blacksquare$

Without independence,
$\operatorname{Var}(\bar{X})=\frac{\sigma^2}{n}+\frac{2}{n^2}\sum_{i<j}\operatorname{Cov}(X_i,X_j)$, which
can be much larger.

**Proposition 8.2 (Finite population correction).** For an SRS of size $n$ without replacement from a
population of size $N$ with variance $\sigma^2$,

$$\operatorname{Var}(\bar{X})=\frac{\sigma^2}{n}\cdot\frac{N-n}{N-1}.$$

*Proof.* For $i\ne j$, $\operatorname{Cov}(X_i,X_j)=-\sigma^2/(N-1)$ (a standard result for sampling
without replacement). There are $n(n-1)$ ordered pairs, so

$$\operatorname{Var}(\bar{X})=\frac{\sigma^2}{n}+\frac{2}{n^2}\cdot\frac{n(n-1)}{2}\left(-\frac{\sigma^2}{N-1}\right)
=\frac{\sigma^2}{n}\left(1-\frac{n-1}{N-1}\right)=\frac{\sigma^2}{n}\cdot\frac{N-n}{N-1}. \qquad\blacksquare$$

**Proposition 8.3 (MSE decomposition).** For any estimator $\hat\theta$ of $\theta$ with finite second
moment,

$$\operatorname{MSE}(\hat\theta)=\operatorname{Bias}(\hat\theta)^2+\operatorname{Var}(\hat\theta).$$

*Proof.* Write $\hat\theta-\theta=(\hat\theta-\mathbb{E}\hat\theta)+(\mathbb{E}\hat\theta-\theta)$.
Squaring and taking expectations, the cross term is
$2(\mathbb{E}\hat\theta-\theta)\mathbb{E}[\hat\theta-\mathbb{E}\hat\theta]=0$. The remaining terms are the
variance and the squared bias. $\blacksquare$

**Proposition 8.4 (Bias and variance imply consistency).** If $\operatorname{Bias}(\hat\theta_n)\to0$ and
$\operatorname{Var}(\hat\theta_n)\to0$, then $\hat\theta_n\xrightarrow{p}\theta$.

*Proof.* By Proposition 8.3 and Chebyshev, for $\varepsilon>0$,

$$\Pr(\lvert\hat\theta_n-\theta\rvert>\varepsilon)
\le\frac{\operatorname{Bias}(\hat\theta_n)^2+\operatorname{Var}(\hat\theta_n)}{\varepsilon^2}\to0. \qquad\blacksquare$$

**Proposition 8.5 (Method-of-moments estimators).** Equating moments gives:

* Bernoulli: $\hat p=\bar{X}$;
* exponential rate: $\hat\lambda=1/\bar{X}$;
* normal: $\hat\mu=\bar{X}$, $\hat\sigma^2=\frac1n\sum_i(X_i-\bar{X})^2$;
* uniform$(0,\theta)$: $\hat\theta=2\bar{X}$;
* Poisson: $\hat\lambda=\bar{X}$.

Each is obtained by solving $\mu_1(\theta)=m_1$ (and $\mu_2(\theta)=m_2$ in the normal case), and each is
consistent under the usual moment conditions.

**Proposition 8.6 (Maximum-likelihood estimators).** For the models of §7.6:

* Bernoulli$(p)$: $\hat p=x/n$;
* exponential$(\lambda)$: $\hat\lambda=1/\bar{x}$;
* normal$(\mu,\sigma^2)$: $\hat\mu=\bar{x}$, $\hat\sigma^2=\frac1n\sum_i(x_i-\bar{x})^2$;
* uniform$(0,\theta)$: $\hat\theta=\max_i x_i$.

*Derivation.* The Bernoulli, exponential and normal cases follow from setting the score to zero and
checking the second derivative, as displayed in §7.6. In the uniform case $L(\theta)=\theta^{-n}$ for
$\theta\ge\max_i x_i$ and $0$ otherwise; $\theta^{-n}$ is decreasing, so the maximum is at the smallest
admissible value, $\max_i x_i$. $\blacksquare$

**Proposition 8.7 ($t$ pivot).** For a normal sample, $\bar{X}$ and $s^2$ are independent,
$(n-1)s^2/\sigma^2\sim\chi^2_{n-1}$, and

$$T=\frac{\bar{X}-\mu}{s/\sqrt n}\sim t_{n-1}.$$

*Proof.* By Fisher's theorem (a standard result proved by an orthogonal change of basis), $\bar{X}$ and
$s^2$ are independent and the chi-square statement holds. A $t_\nu$ variable is by definition
$Z/\sqrt{V/\nu}$ with independent $Z\sim\mathcal N(0,1)$ and $V\sim\chi^2_\nu$. Put
$Z=(\bar{X}-\mu)/(\sigma/\sqrt n)$ and $V=(n-1)s^2/\sigma^2$ with $\nu=n-1$; substitution gives the
displayed $T$. $\blacksquare$

**Proposition 8.8 (Wilson interval).** The set of $p$ satisfying
$(\hat p-p)^2\le z^2p(1-p)/n$ is the interval

$$\frac{\hat p+\dfrac{z^2}{2n}\pm z\sqrt{\dfrac{\hat p(1-\hat p)}{n}+\dfrac{z^2}{4n^2}}}{1+\dfrac{z^2}{n}}.$$

*Proof.* Expand the inequality:

$$n(\hat p-p)^2\le z^2p(1-p)
\iff (n+z^2)p^2-(2n\hat p+z^2)p+n\hat p^2\le0.$$

The quadratic opens upwards, so its solution is the interval between its roots. The discriminant is

$$(2n\hat p+z^2)^2-4(n+z^2)n\hat p^2
=4n^2\hat p^2+4nz^2\hat p+z^4-4n^2\hat p^2-4nz^2\hat p^2
=4nz^2\bigl(\hat p(1-\hat p)\bigr)+z^4 .$$

Dividing by $4(n+z^2)^2$ and taking square roots gives the stated half-width, and the root midpoint gives
the centre. $\blacksquare$

**Proposition 8.9 (Sample size for a given margin of error).** For $\bar{X}\pm E$ with known $\sigma$,

$$n=\left(\frac{z_{1-\alpha/2}\sigma}{E}\right)^2.$$

For a proportion with target margin $E$,

$$n=\frac{z_{1-\alpha/2}^2p(1-p)}{E^2}\le\frac{z_{1-\alpha/2}^2}{4E^2},$$

with equality at $p=1/2$.

*Proof.* Set $E=z_{1-\alpha/2}\sigma/\sqrt n$ and solve for $n$. For the proportion, solve
$E=z\sqrt{p(1-p)/n}$; the bound uses $p(1-p)\le1/4$, which follows from
$(p-1/2)^2\ge0$. $\blacksquare$

## 9. Step-by-Step Examples

### 9.1 The sampling distribution by enumeration

Take the population $\{1,2,3,4\}$ and samples of size $2$ with replacement. There are $16$ equally likely
samples, and the sampling distribution of $\bar{X}$ is

| $\bar{x}$ | $1$ | $1.5$ | $2$ | $2.5$ | $3$ | $3.5$ | $4$ |
|---|---|---|---|---|---|---|---|
| count | $1$ | $2$ | $3$ | $4$ | $3$ | $2$ | $1$ |

The population mean is $2.5$ and the population variance is $1.25$. The mean of the $16$ sample means is
$2.5$, and their variance is $0.625=1.25/2$, so $\operatorname{SE}(\bar{X})=\sqrt{0.625}=0.7906$. This is
the content of Proposition 8.1: centring and $1/\sqrt n$ scaling are visible in a finite example.

### 9.2 Standard error of a proportion

With $p=0.4$ and $n=100$, $\operatorname{SE}(\hat p)=\sqrt{0.4(0.6)/100}=\sqrt{0.0024}=0.04899$. The
probability that $\hat p$ lies within $0.1$ of $p$ is, by the normal approximation,
$2\Phi(0.1/0.04899)-1=2\Phi(2.041)-1=0.9588$. The exact binomial probability is $0.9685$. The normal
approximation is close but not exact, and the exact value requires the binomial distribution.

### 9.3 Method of moments

For the exponential sample $2.1,0.8,3.4,1.5,2.2$, the mean is $10.0/5=2.0$, so the moment estimator is
$\hat\lambda=1/\bar{x}=0.5$. For a uniform$(0,\theta)$ sample with $\bar{x}=3.2$, the moment estimator is
$\hat\theta=2(3.2)=6.4$; note that it could in principle be smaller than the largest observation, which would
be impossible.

### 9.4 Maximum likelihood for a Bernoulli model

With $7$ successes in $20$ trials, $\hat p=7/20=0.35$. The log-likelihood is
$\ell(p)=7\log p+13\log(1-p)$. At the MLE,
$\ell(0.35)=7(-1.0498)+13(-0.4308)=-12.949$. At $p=0.3$,
$\ell(0.3)=7(-1.2040)+13(-0.3567)=-13.065$; at $p=0.5$,
$\ell(0.5)=20(-0.6931)=-13.863$. The MLE is the largest of the three, and the derivative
$\ell'(p)=7/p-13/(1-p)$ vanishes at $p=0.35$: $7/0.35=20$ and $13/0.65=20$.

### 9.5 Maximum likelihood for a normal model

For $4,7,9,10,12$: $n=5$, $\bar{x}=42/5=8.4$, and
$\sum_i(x_i-\bar{x})^2=19.36+1.96+0.36+2.56+12.96=37.2$. Hence
$\hat\mu=8.4$, $\hat\sigma^2=37.2/5=7.44$ and $\hat\sigma=2.728$. The unbiased sample variance is
$s^2=37.2/4=9.30$, with $s=3.050$; the MLE is smaller by the factor $4/5$.

### 9.6 Confidence intervals for a mean

**Known variance.** With $\bar{x}=102.3$, $\sigma=12$ and $n=36$, the standard error is $12/6=2$ and the
$95\%$ interval is

$$102.3\pm1.96(2)=102.3\pm3.92=[98.38,\ 106.22].$$

**Unknown variance.** For $12.1,11.4,12.8,13.0,11.9,12.5,12.2,11.7$: $n=8$, $\bar{x}=12.2$,
$\sum_i(x_i-\bar{x})^2=2.08$, $s^2=0.29714$, $s=0.5451$, and the standard error is
$0.5451/\sqrt8=0.19272$. With $t_{7,0.975}=2.3646$,

$$12.2\pm2.3646(0.19272)=12.2\pm0.4557=[11.744,\ 12.656].$$

The $t$ multiplier is $20.6\%$ larger than $1.96$; with only seven degrees of freedom, estimating $\sigma$
costs real width.

### 9.7 Confidence intervals for a proportion and a difference

For $45$ successes in $200$, $\hat p=0.225$ and
$\operatorname{SE}=\sqrt{0.225(0.775)/200}=0.02953$. The Wald interval is
$0.225\pm1.96(0.02953)=[0.1671,\ 0.2829]$. The Wilson interval is
$[0.1726,\ 0.2877]$: it is shifted towards $0.5$ and slightly wider, the usual behaviour near a boundary.

For two independent groups with $n_1=12$, $\bar{x}_1=5.2$, $s_1=1.1$ and $n_2=15$, $\bar{x}_2=4.5$,
$s_2=1.4$: the pooled variance is
$s_p^2=(11(1.21)+14(1.96))/25=40.75/25=1.63$, so $s_p=1.2767$ and
$\operatorname{SE}=1.2767\sqrt{1/12+1/15}=0.49447$. With $25$ degrees of freedom,
$t_{25,0.975}=2.0595$, giving

$$0.7\pm2.0595(0.49447)=0.7\pm1.018=[-0.318,\ 1.718].$$

Welch gives $[-0.291,\ 1.691]$ with $\nu\approx25.0$. Both intervals contain zero, so the data are
compatible with no difference at $5\%$; the interval, not the point estimate, is the honest summary.

## 10. Visual Explanations

| Target | $100(1-\alpha)\%$ interval | Main requirements |
|---|---|---|
| Mean, known $\sigma$ | $\bar{x}\pm z_{1-\alpha/2}\,\sigma/\sqrt n$ | normal population, or large $n$ by the CLT |
| Mean, unknown $\sigma$ | $\bar{x}\pm t_{n-1,1-\alpha/2}\,s/\sqrt n$ | normal population; robust for large $n$ |
| Proportion | Wilson interval of §7.7 | moderate $n\hat p$ and $n(1-\hat p)$; Wald otherwise |
| Difference of means | pooled or Welch interval of §7.7 | independent samples; Welch if variances differ |

The width of every interval has the form (critical value) $\times$ (standard error), and the standard
error shrinks like $1/\sqrt n$. The critical value grows with the confidence level; the standard error
grows with the variability of the data.

## 11. Common Mistakes

1. **Reporting a standard error as a standard deviation** (or the reverse). The first describes a
   statistic and shrinks with $n$; the second describes observations.
2. **Saying "there is a 95% probability that $\mu$ lies in this interval".** Under the frequentist
   definition the probability is a property of the procedure, not of the realised interval.
3. **Using the Wald interval when $n\hat p$ or $n(1-\hat p)$ is small.** It can have near-zero width at
   $\hat p=0$ and coverage far below nominal; use Wilson or Clopper–Pearson.
4. **Ignoring clustering and design effects.** Treating $500$ students in $10$ classes as $500$
   independent observations overstates the effective sample size by a large factor.
5. **Expecting the law of large numbers to repair a biased sample,** or confusing unbiasedness with
   accuracy. The theorem makes a statistic converge to the expectation of the sampling mechanism, and an
   unbiased estimator with huge variance is still unreliable.
6. **Choosing $n$ by a rule of thumb, or treating a confidence interval as a prediction interval.** The
   required sample depends on the margin, variability, design and non-response; a prediction interval is
   wider because it includes the observation's own variability.

## 12. Applications

* **Polls and surveys.** The "margin of error of $\pm3$ points" is $z\sqrt{\hat p(1-\hat p)/n}$ for a
  simple random sample; real polls multiply by design effects and are affected by non-response.
* **Clinical trials.** Treatment effects are reported with confidence intervals because the interval
  conveys both size and precision; a trial can be significant and clinically irrelevant if the interval is
  narrow around a tiny effect.
* **Quality control and machine learning.** Subgroup standard errors set control limits; cross-validation
  standard errors over folds quantify uncertainty; the bootstrap gives intervals for complex metrics.
* **Official statistics.** Labour-force and price statistics come from stratified multistage samples, and
  their published standard errors reflect the design.

## 13. Exercises

There are **36 problems** in [exercises.md](exercises.md): Beginner (1–12), Intermediate (13–22), Advanced
(23–30), Challenge (31–36).

## 14. Solutions

Complete worked solutions for all 36 problems are in [solutions.md](solutions.md).

## 15. Summary

* A **probability sample** makes the sampling distribution calculable; a non-probability sample does not,
  and larger samples do not repair selection bias.
* $\mathbb{E}[\bar{X}]=\mu$ and $\operatorname{Var}(\bar{X})=\sigma^2/n$ under independence, so
  $\operatorname{SE}(\bar{X})=\sigma/\sqrt n$; the finite population correction multiplies the variance by
  $(N-n)/(N-1)$.
* The **central limit theorem** makes $\bar{X}$ approximately normal for large $n$; the **law of large
  numbers** makes it converge to $\mu$. Neither repairs a biased sample, and both are asymptotic.
* An estimator is judged by **bias, variance, MSE and consistency**. MSE $=$ bias$^2$ $+$ variance;
  bias $\to0$ and variance $\to0$ imply consistency, not the reverse.
* **Method of moments** equates sample and population moments; **maximum likelihood** maximises the
  log-likelihood. The first is simple but can be inefficient; the second is invariant and asymptotically
  efficient under regularity, but fails at boundaries and in non-identified models.
* A **confidence interval** is a procedure with a stated coverage. A $95\%$ interval is not a $95\%$
  probability statement about $\theta$, not an interval containing $95\%$ of the data, and not a
  prediction interval.
* **Width** is critical value $\times$ standard error; it shrinks like $1/\sqrt n$, so quadrupling $n$
  halves it, and the required $n$ grows like $1/E^2$.
* The **bootstrap** resamples from the empirical distribution to approximate a sampling distribution. It
  is flexible but assumes independence and a representative sample, and it fails for extremes, maxima and
  dependent data.

## 16. Further Learning

* **Next topic:** hypothesis testing, which turns the intervals of this topic into decisions about
  parameters, with p-values, power and multiplicity corrections.
* **Probability behind the derivations:**
  [Probability Foundations](../../10-probability/01-probability-foundations/README.md) for the CLT, the
  chi-square distribution and convergence in probability.
* **Reference:** [Reference: Formulas](../../reference/formulas/README.md). **Books:** Casella and Berger,
  *Statistical Inference*, for estimation theory; Wasserman, *All of Statistics*, for a compact modern
  account; Efron and Tibshirani, *An Introduction to the Bootstrap* (1993); Cochran, *Sampling Techniques*.
