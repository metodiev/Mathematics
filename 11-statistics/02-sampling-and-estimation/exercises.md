# Sampling and Estimation — Exercises

> [Sampling and Estimation](README.md) · 36 problems · Beginner → Challenge · Solutions: [solutions.md](solutions.md)

Attempt each problem in writing before consulting [solutions.md](solutions.md). The problems are grouped
by level but numbered continuously; the section of the tutorial tested is given in italics.

**Conventions.** Unless stated otherwise, samples are independent and identically distributed, variances
use divisor $n-1$, and intervals are two-sided $95\%$ intervals with $z_{0.975}=1.960$ and the following
$t$ critical values: $t_{7}=2.365$, $t_{9}=2.262$, $t_{19}=2.093$, $t_{20}=2.086$, $t_{25}=2.060$,
$t_{29}=2.045$. For $90\%$ use $z=1.645$; for $99\%$ use $z=2.576$. Normal probabilities may be read from
a table: $\Phi(1)=0.8413$, $\Phi(1.5)=0.9332$, $\Phi(1.96)=0.9750$, $\Phi(2)=0.9772$, $\Phi(2.04)=0.9793$.
Keep full precision during calculations and round final answers to four significant figures.

## Beginner

**1.** *(§5.1, §7.1)* A city health department wants to estimate the mean number of minutes adults living
in the city spend commuting each day. It selects $400$ adults at random from the electoral register,
measures their commute, and obtains a mean of $38.2$ minutes.

(a) Identify the target population, the sampling frame, the sample, the variable and its scale.
(b) Identify the parameter of interest and the statistic used to estimate it.
(c) State one source of undercoverage and one source of non-sampling error.

**2.** *(§7.1)* Identify the sampling design in each scenario as simple random, stratified, cluster,
systematic or convenience, and say whether it is a probability sample.

(a) A factory selects every $20$th item from the production line after a random start.
(b) A university divides students by faculty and draws a random sample from each faculty.
(c) A researcher interviews the first $50$ people who enter a shopping centre.
(d) A national survey selects $100$ schools at random and interviews every teacher in them.
(e) A lottery draws $10$ names from a complete list of members.
(f) A website asks visitors to vote on a question.

**3.** *(§7.2, §8.2)* A population has $N=1000$ units and standard deviation $\sigma=15$. A simple random
sample of $n=100$ is taken.

(a) Compute the standard error of the sample mean assuming sampling with replacement.
(b) Compute the finite population correction and the corrected standard error.
(c) Explain why the correction is close to $1$ here and what happens when $n=N$.

**4.** *(§7.2)* A sample of nine measurements is
$$5,\ 7,\ 8,\ 8,\ 9,\ 10,\ 11,\ 12,\ 14.$$
Compute the sample mean, the sample standard deviation and the estimated standard error of the mean.

**5.** *(§5.1)* Classify each of the following as a parameter or a statistic, and write it with an
appropriate symbol.

(a) The mean commute time of all adults in the city.
(b) The mean commute time of the $400$ sampled adults.
(c) The proportion of defective items in a production batch of $10{,}000$.
(d) The proportion of defective items in the $50$ items inspected.
(e) The standard deviation of the $400$ commute times.

**6.** *(§7.2, §7.3)* A population has standard deviation $\sigma=20$.

(a) Compute $\operatorname{SE}(\bar{X})$ for $n=25$, $n=100$ and $n=400$.
(b) How does the standard error change when the sample size is quadrupled? Verify with the three values.
(c) What sample size is needed for a standard error of $0.5$?

**7.** *(§7.7)* A sample of $n=49$ observations from a normal population with known $\sigma=10$ has
$\bar{x}=64$. Compute the $95\%$ confidence interval for $\mu$.

**8.** *(§7.7)* Using the data of Exercise 7, compute the $90\%$ and $99\%$ confidence intervals for $\mu$
and compare their widths with the $95\%$ interval.

**9.** *(§7.7)* In a survey, $36$ of $120$ respondents support a proposal. Compute the sample proportion,
its standard error, and the $95\%$ Wald confidence interval.

**10.** *(§7.8)* A $95\%$ confidence interval for a population mean is $[12.4, 18.6]$. Decide whether each
statement is a correct frequentist interpretation, and explain the error in each incorrect one.

(a) There is a $95\%$ probability that $\mu$ lies between $12.4$ and $18.6$.
(b) If the study were repeated many times, about $95\%$ of the intervals computed this way would contain
$\mu$.
(c) About $95\%$ of the population lies between $12.4$ and $18.6$.
(d) The procedure that produced this interval has $95\%$ coverage.
(e) A future observation will lie between $12.4$ and $18.6$ with probability $0.95$.

**11.** *(§7.3)* A fair die has mean $3.5$ and variance $35/12$.

(a) Using Chebyshev's inequality, bound $\Pr(\lvert\bar{X}-3.5\rvert\ge0.5)$ for $n$ rolls.
(b) Find the smallest $n$ for which the bound is at most $0.10$.
(c) Explain why the bound is much larger than the normal approximation at that $n$.

**12.** *(§7.1)* Identify the main source of bias in each scenario and state one design change that would
reduce it.

(a) A telephone poll conducted on landlines in 2024.
(b) A customer-satisfaction survey with a $12\%$ response rate.
(c) A question asking "Do you agree that the new policy is an improvement?"
(d) A study of the health effects of a drug that includes only patients who survived the first year.

## Intermediate

**13.** *(§7.2)* A population consists of $\{2,4,6,8\}$. Samples of size $2$ are drawn with replacement.

(a) Compute the population mean and variance.
(b) List all $16$ samples, compute their means, and tabulate the sampling distribution.
(c) Verify $\mathbb{E}[\bar{X}]=5$ and $\operatorname{Var}(\bar{X})=\sigma^2/2$.
(d) State the standard error.

**14.** *(§7.1)* A population has two strata with weights $W_1=0.6$, $W_2=0.4$, means $\mu_1=70$,
$\mu_2=85$ and standard deviations $\sigma_1=10$, $\sigma_2=15$. A sample of $n=100$ is allocated
proportionally.

(a) Compute the overall population mean and variance.
(b) Compute the variance of the sample mean under simple random sampling of $100$.
(c) Compute the variance under proportional stratified sampling and the ratio of the two variances.
(d) Explain the source of the reduction.

**15.** *(§7.5)* A Poisson sample is $3,1,4,2,5$. Estimate $\lambda$ by the method of moments using the
first moment. A Bernoulli sample has $18$ successes in $60$ trials; estimate $p$ by the method of moments.

**16.** *(§7.5, §7.6)* An exponential sample is $1.2,2.4,0.8,3.6,3.0$.

(a) Compute the method-of-moments estimate of the rate $\lambda$.
(b) Derive the maximum-likelihood estimator and compute it for these data.
(c) Explain why the two estimates coincide.

**17.** *(§7.6)* A Bernoulli sample has $12$ successes in $40$ trials.

(a) Derive the MLE of $p$.
(b) Evaluate the log-likelihood at $p=0.25$, $p=0.30$ and $p=0.40$ and confirm that the maximum is at the
MLE.
(c) Verify that the score is zero at the MLE.

**18.** *(§7.4)* Let $X_1,\dots,X_n$ be uniform on $(0,\theta)$.

(a) Show that $2\bar{X}$ is unbiased for $\theta$.
(b) Show that $M=\max_iX_i$ has expectation $\frac{n}{n+1}\theta$, hence bias $-\frac{1}{n+1}\theta$.
(c) Find the constant $c$ such that $cM$ is unbiased, and compute the bias of $M$ for $n=5$.

**19.** *(§7.4, §8.4)* An estimator $\hat\theta_n$ has bias $1/n$ and variance $4/n$.

(a) Compute its MSE.
(b) Use Chebyshev's inequality to bound $\Pr(\lvert\hat\theta_n-\theta\rvert>0.5)$.
(c) Find the smallest $n$ for which the bound is at most $0.05$.

**20.** *(§7.4)* For a normal population, the sample median is unbiased for $\mu$ with variance
approximately $\pi\sigma^2/(2n)$, while the sample mean has variance $\sigma^2/n$.

(a) Compute the relative efficiency of the mean to the median.
(b) How many observations does the median need to match the precision of a mean based on $100$
observations?
(c) Explain why the mean is nevertheless not always preferred.

**21.** *(§7.7)* For the ten observations
$$4.1,\ 4.4,\ 4.7,\ 4.9,\ 5.0,\ 5.0,\ 5.1,\ 5.3,\ 5.6,\ 5.9,$$
compute $\bar{x}$, $s$ and the estimated standard error, and construct the $95\%$ $t$ interval for $\mu$.

**22.** *(§7.7)* Two independent samples give

* sample 1: $n_1=10$, $\bar{x}_1=32.4$, $s_1=4.2$;
* sample 2: $n_2=12$, $\bar{x}_2=28.1$, $s_2=3.6$.

Assuming equal variances, compute the pooled variance, the standard error of the difference and the $95\%$
confidence interval for $\mu_1-\mu_2$.

## Advanced

**23.** *(§8.1)* Let $X_1,\dots,X_n$ have common mean $\mu$ and variance $\sigma^2$ but be possibly
correlated, with $\operatorname{Cov}(X_i,X_j)=\rho\sigma^2$ for $i\ne j$.

(a) Derive $\operatorname{Var}(\bar{X})$ in terms of $\sigma^2$, $\rho$ and $n$.
(b) Evaluate it for $n=2$ and $\rho=0.5$, and compare with the independent case.
(c) Explain what happens as $n\to\infty$ when $\rho>0$ is fixed.

**24.** *(§7.4, §7.6)* For a normal sample, the MLE of $\sigma^2$ is
$\hat\sigma^2=\frac1n\sum_i(X_i-\bar{X})^2$.

(a) Show that $\operatorname{Bias}(\hat\sigma^2)=-\sigma^2/n$.
(b) Given that $\operatorname{Var}(\hat\sigma^2)=2(n-1)\sigma^4/n^2$, compute its MSE.
(c) Compare with the MSE of the unbiased estimator $s^2$, whose variance is $2\sigma^4/(n-1)$, and say
which is smaller for $n\ge2$.

**25.** *(§7.4, §8.3)* Consider estimators of a normal mean $\mu$ of the form $\hat\mu_c=c\bar{X}$ with
$c>0$.

(a) Show that $\operatorname{Bias}(\hat\mu_c)=(c-1)\mu$ and
$\operatorname{Var}(\hat\mu_c)=c^2\sigma^2/n$.
(b) Write the MSE and minimise it over $c$.
(c) Interpret the optimal $c$ and explain why it depends on $\mu^2/(\sigma^2/n)$.

**26.** *(§7.7)* Two independent normal samples have equal population variance $\sigma^2$.

(a) Prove that the pooled estimator
$$s_p^2=\frac{(n_1-1)s_1^2+(n_2-1)s_2^2}{n_1+n_2-2}$$
is unbiased for $\sigma^2$.
(b) Show that $s_p^2$ is a weighted average of $s_1^2$ and $s_2^2$ with weights summing to $1$.
(c) Explain why the pooled $t$ interval has $n_1+n_2-2$ degrees of freedom.

**27.** *(§7.9, §8.9)* Derive the sample-size formula for estimating a proportion with margin of error
$E$.

(a) Show that the required $n$ is $z^2p(1-p)/E^2$.
(b) Prove that $p(1-p)\le1/4$ on $[0,1]$, with equality at $p=1/2$.
(c) Compute $n$ for $E=0.02$ with no prior guess, and for $E=0.02$ with a pilot estimate $p=0.1$.

**28.** *(§7.7, §8.8)* For the Wilson interval:

(a) Verify by substitution that the two endpoints satisfy $(\hat p-p)^2=z^2p(1-p)/n$.
(b) Show that the width of the Wilson interval is at most $z/\sqrt n$, and that it tends to the Wald width
as $n\to\infty$.
(c) Evaluate the Wilson interval for $24$ successes in $80$ trials and compare it with the Wald interval.

**29.** *(§7.1)* Suppose a population is divided into $H$ strata with weights $W_h=N_h/N$, means
$\mu_h$ and variances $\sigma_h^2$.

(a) Prove the law of total variance
$$\sigma^2=\sum_h W_h\sigma_h^2+\sum_h W_h(\mu_h-\mu)^2.$$
(b) Show that proportional stratified sampling with $n_h=nW_h$ has variance
$(1/n)\sum_h W_h\sigma_h^2$.
(c) Deduce that proportional stratification never has larger variance than simple random sampling, with
equality exactly when the stratum means are all equal.

**30.** *(§7.10)* For data $x_1,\dots,x_n$ with sample variance $s^2$, let $\bar{X}^*$ be the mean of a
bootstrap sample of size $n$.

(a) Show that the bootstrap variance is $\operatorname{Var}^*(\bar{X}^*)=\frac{n-1}{n^2}s^2$.
(b) Compute it for $2,3,5,8,12$ and compare with $s^2/n$.
(c) Explain why the bootstrap standard error is slightly smaller and whether the difference matters in
practice.

## Challenge

**31.** *(§7.4)* Let $X_1,\dots,X_n$ be independent with mean $\mu$ and variance $\sigma^2$. Consider
linear estimators $\hat\mu=\sum_i a_iX_i$.

(a) Show that unbiasedness requires $\sum_i a_i=1$.
(b) Minimise $\operatorname{Var}(\hat\mu)=\sigma^2\sum_i a_i^2$ subject to $\sum_i a_i=1$ and show that
the minimum is attained at $a_i=1/n$.
(c) Deduce that $\bar{X}$ is the best linear unbiased estimator (BLUE) of $\mu$, and compute the variance
ratio between an arbitrary unbiased linear estimator and $\bar{X}$.

**32.** *(§7.6)* (a) For a Bernoulli model, compute the Fisher information
$I(p)=-\mathbb{E}[\ell''(p)]$ per observation and show that it equals $1/(p(1-p))$.
(b) State the Cramér–Rao bound for unbiased estimators of $p$ and show that $\hat p$ attains it.
(c) Repeat for the exponential rate $\lambda$: show $I(\lambda)=1/\lambda^2$ and that $\hat\lambda=1/\bar{X}$
attains the bound asymptotically.

**33.** *(§7.6)* (a) Prove the invariance of the MLE under a one-to-one reparameterisation: if
$\hat\theta$ maximises $L(\theta)$ and $\phi=g(\theta)$ with $g$ bijective, then $\hat\phi=g(\hat\theta)$
maximises the induced likelihood.
(b) Extend the argument to a non-injective $g$ by defining the induced likelihood
$L^*(\phi)=\max_{\theta:g(\theta)=\phi}L(\theta)$, and show that $g(\hat\theta)$ maximises $L^*$.
(c) Illustrate with $g(\theta)=\theta^2$ and the symmetric likelihood $L(\theta)=e^{-\theta^2/2}$:
identify the two parameter values $\theta=\pm\sqrt{\phi}$ that map to the same $\phi$, and explain why the
induced likelihood still attains its maximum at $g(\hat\theta)=0$.

**34.** *(§7.1, §7.9)* A population has two strata: stratum 1 has $N_1=900$ units with proportion
$p_1=0.2$, and stratum 2 has $N_2=100$ units with proportion $p_2=0.8$. A sample of $100$ is taken from
each stratum.

(a) Compute the naive pooled estimate that ignores the strata.
(b) Compute the stratified estimate using the population weights.
(c) Explain which estimate answers "what is the population proportion?" and which answers "what is the
proportion in the sample?".
(d) Explain the connection with Simpson's paradox.

**35.** *(§7.7, §7.8)* Consider the nominal $95\%$ Wald interval for a proportion.

(a) Compute the exact coverage by binomial enumeration at $n=20$, $p=0.05$; at $n=20$, $p=0.5$; and at
$n=100$, $p=0.05$.
(b) Compute the Wilson coverage at the same settings.
(c) Explain why the Wald coverage collapses when $p$ is near $0$ or $1$, and why the Wilson interval is
preferred there.

**36.** *(§7.10)* Let $X_1,\dots,X_n$ be uniform on $(0,\theta)$ and let $M=\max_iX_i$. A bootstrap is
performed by resampling from the observed values.

(a) Show that $\Pr(M^*=M)=1-(1-1/n)^n$.
(b) Evaluate this for $n=5$, $n=20$ and $n=100$, and compare with $1-e^{-1}$.
(c) Explain why the bootstrap distribution of $M^*$ cannot approximate the distribution of $M-\theta$, and
what a parametric bootstrap would do differently.
