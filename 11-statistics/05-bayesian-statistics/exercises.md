# Bayesian Statistics — Exercises

> [Bayesian Statistics](README.md) · 36 problems · Beginner → Challenge · Solutions: [solutions.md](solutions.md)

Attempt every problem in writing before looking at [solutions.md](solutions.md). Each problem names the section of the tutorial that supplies the method. Numerical answers should be checked by a second method where one is available.

Notation: $\pi(\theta)$ is the prior density, $L(\theta;x)$ the likelihood, $\pi(\theta\mid x)$ the posterior, and $m(x)$ the marginal likelihood. $\operatorname{Beta}(\alpha,\beta)$ has mean $\alpha/(\alpha+\beta)$ and variance $\alpha\beta/[(\alpha+\beta)^2(\alpha+\beta+1)]$. $\operatorname{Gamma}(\alpha,\beta)$ is parametrised by shape $\alpha$ and rate $\beta$, with mean $\alpha/\beta$ and variance $\alpha/\beta^2$. All normal models use $\mathcal{N}(\mu,\sigma^2)$ with variance $\sigma^2$.

## Beginner

**1.** *(§5.3, §12)* A disease has prevalence $1\%$. A test has sensitivity $95\%$ and specificity $90\%$. A randomly chosen person tests positive. Compute the posterior probability that the person has the disease, stating the prior, the likelihood, and the normalising constant explicitly.

**2.** *(§7.2)* The prior for a success probability is $\operatorname{Beta}(3,5)$. In six Bernoulli trials, four successes and two failures are observed.

(a) Find the posterior distribution.
(b) Compute the posterior mean, posterior mode, and prior mean.
(c) Compare the posterior mean with the sample proportion and explain the direction of the difference.

**3.** *(§7.2)* With a uniform prior, ten Bernoulli trials produce eight successes.

(a) Find the posterior distribution, its mean, mode, and standard deviation.
(b) Compute $\Pr(\theta>0.5\mid x)$ exactly.
(c) What would the MLE and the Wald estimate be, and why do they differ from the posterior mean?

**4.** *(§7.3)* The prior is $\mu\sim\mathcal{N}(10,4)$ and one observation $x=13$ is made from $\mathcal{N}(\mu,4)$.

(a) Find the posterior distribution.
(b) Compute the posterior weight on the data.
(c) Find a $95\%$ credible interval.

**5.** *(§7.3)* The prior is $\mu\sim\mathcal{N}(0,9)$. Four independent observations from $\mathcal{N}(\mu,4)$ have sample mean $5$.

(a) Find the posterior distribution and the posterior precision.
(b) Find the posterior predictive distribution of a fifth observation.
(c) How large would $n$ have to be for the posterior variance to be at most $0.5$?

**6.** *(§7.4)* The prior for a Poisson rate is $\operatorname{Gamma}(3,2)$. Over two units of exposure, seven events are observed.

(a) Find the posterior distribution, its mean, mode, and variance.
(b) Find the posterior predictive probability of zero events in one future unit of exposure.
(c) Compare the posterior mean with the empirical rate $7/2$.

**7.** *(§7.4)* Let $\lambda\sim\operatorname{Gamma}(2,1)$ and let $Y\mid\lambda\sim\operatorname{Poisson}(\lambda)$.

(a) Compute the prior predictive probabilities $\Pr(Y=0)$, $\Pr(Y=1)$, and $\Pr(Y=2)$.
(b) Verify that they sum to $1$ if you also include $\Pr(Y=3)$? (They do not; explain why the first three need not sum to $1$.)
(c) Compute the prior predictive mean and variance and compare them with the Poisson values at $\mathbb{E}[\lambda]$.

**8.** *(§7.5)* For each statement, say whether it is a Bayesian credible statement, a frequentist confidence statement, both, or neither, and explain.

(a) "There is a $95\%$ probability that $\theta$ lies in $[1.2,3.4]$, given the data and the prior."
(b) "If we repeated the experiment many times, $95\%$ of the intervals constructed this way would contain the true $\theta$."
(c) "The probability that the null hypothesis is true is $0.03$."
(d) "The posterior probability that $\theta>0$ is $0.97$."

**9.** *(§7.6)* Let $\theta\sim\operatorname{Beta}(2,2)$ and $X\mid\theta\sim\operatorname{Binomial}(5,\theta)$. Compute the prior predictive probabilities $\Pr(X=0)$, $\Pr(X=1)$, and $\Pr(X=5)$.

**10.** *(§7.1)* Start with $\theta\sim\operatorname{Beta}(2,3)$. Update first with three successes, then with two failures. Show that the result is the same as updating once with the batch of three successes and two failures.

**11.** *(§7.2–§7.4)* Match each likelihood to its conjugate prior and posterior family. Write the updated parameters.

(a) $X\mid\theta\sim\operatorname{Binomial}(n,\theta)$.
(b) $X\mid\lambda\sim\operatorname{Poisson}(\lambda)$.
(c) $X\mid\mu\sim\mathcal{N}(\mu,\sigma^2)$ with $\sigma^2$ known.
(d) $X\mid\lambda\sim\operatorname{Exponential}(\lambda)$ with rate $\lambda$ (density $\lambda e^{-\lambda x}$).

**12.** *(§5.7, §7.10)* Two models have marginal likelihoods $m_1=0.05$ and $m_2=0.10$. The prior model probabilities are equal.

(a) Compute $\operatorname{BF}_{21}$ and $\operatorname{BF}_{12}$.
(b) Compute the posterior model probabilities.
(c) If the prior odds were $10:1$ in favour of $M_1$, what would the posterior odds be?

## Intermediate

**13.** *(§7.2)* Derive the posterior for a Bernoulli model with a uniform prior $\pi(\theta)=1$ on $(0,1)$ and data consisting of $x$ successes in $n$ trials. Show that the posterior is $\operatorname{Beta}(x+1,n-x+1)$ and compute the posterior mean for $x=3$, $n=10$.

**14.** *(§7.6)* For the beta-binomial model with prior $\operatorname{Beta}(\alpha,\beta)$ and $n$ observations with $x$ successes, derive the mean and variance of the posterior predictive distribution of $\tilde X$ successes in $\tilde n$ future trials. Then compute both for $\alpha=3$, $\beta=2$, $\tilde n=4$.

**15.** *(§7.7)* Derive the Jeffreys prior for the Poisson model with rate $\lambda$. Compute the posterior for $s$ observed events over exposure $T$, and evaluate the posterior mean and mode for $s=5$, $T=2$. Is the prior proper?

**16.** *(§7.3)* The prior is $\mu\sim\mathcal{N}(0,1)$ and observations have known variance $\sigma^2=4$. Find the smallest sample size $n$ such that the posterior standard deviation of $\mu$ is at most $0.5$. For that $n$, compute the posterior mean when $\bar x=2$ and the weight on the data.

**17.** *(§7.5, §7.6)* Ten Bernoulli trials produce ten successes, and the prior is uniform.

(a) Find the posterior distribution.
(b) Find the exact $95\%$ equal-tailed lower bound.
(c) Compare it with the Wald interval and with the rule-of-three approximation $1-3/n$. Which is more sensible, and why?

**18.** *(§7.7)* In ten trials, six successes are observed. Compute the posterior mean under $\operatorname{Beta}(1,1)$, $\operatorname{Beta}(10,10)$, and $\operatorname{Beta}(2,8)$. Express each posterior mean as a weighted average of the prior mean and the sample proportion, and identify how much weight the prior carries in each case.

**19.** *(§7.9)* The target density is $\pi(\theta)=e^{-\theta}$ on $(0,\infty)$. The independence proposal is $q(\theta'\mid\theta)=\lambda e^{-\lambda\theta'}$ with $\lambda=1/2$. Starting from $\theta=2$, the proposal is $\theta'=0.5$.

(a) Derive the acceptance ratio $R(\theta,\theta')$ for general $\lambda>0$.
(b) Compute the acceptance probability for the stated values.
(c) If $u=0.3$, is the proposal accepted? If $u=0.6$?

**20.** *(§7.8, §7.9)* Consider the model $x_i\mid\mu,\sigma^2\sim\mathcal{N}(\mu,\sigma^2)$ with prior $\mu\sim\mathcal{N}(\mu_0,\tau^2)$ and $\sigma^2\sim\operatorname{InvGamma}(\alpha_0,\beta_0)$, with $\mu$ and $\sigma^2$ independent a priori. Write down the two full conditional distributions needed for a Gibbs sampler.

**21.** *(§7.10)* Ten trials produce eight successes. Compare $M_1:\theta=1/2$ with $M_2:\theta\sim\operatorname{Beta}(2,2)$.

(a) Compute the marginal likelihoods.
(b) Compute $\operatorname{BF}_{21}$.
(c) With equal prior probabilities, compute $\Pr(M_2\mid x)$.
(d) Interpret the result on Jeffreys' scale.

**22.** *(§7.8)* Group means follow $\theta_j\sim\mathcal{N}(\mu,\tau^2)$ with $\mu=12$, $\tau^2=4$, and observations have $\sigma^2=4$. Group 1 has $n_1=4$, $\bar y_1=10$; group 2 has $n_2=16$, $\bar y_2=14$.

(a) Compute the shrinkage factor $B_j$ for each group.
(b) Compute the posterior mean of each $\theta_j$ conditional on $\mu$ and $\tau^2$.
(c) Which group shrinks more, and why?

## Advanced

**23.** *(§7.1)* Let $x_{1:n}$ be independent observations with density $p(x_i\mid\theta)$, and let $\pi$ be a proper prior. Prove rigorously that updating sequentially in two batches gives the same posterior as updating once with the full sample. State where independence is used.

**24.** *(§7.6)* For the beta-binomial model, derive the posterior predictive probability mass function
$$
p(\tilde x\mid x)=\binom{\tilde n}{\tilde x}\frac{B(\alpha+x+\tilde x,\beta+n-x+\tilde n-\tilde x)}{B(\alpha+x,\beta+n-x)}
$$
from the integral defining the posterior predictive. Then derive its mean and variance. You may use the mean and variance of the beta-binomial distribution if you prove them from the beta integral.

**25.** *(§7.4)* Derive the gamma-Poisson posterior predictive distribution and show that its variance exceeds the variance of a Poisson distribution with the same mean. Explain the extra term probabilistically using the law of total variance.

**26.** *(§7.9)* State and prove the detailed-balance identity for Metropolis-Hastings with acceptance probability $\alpha(\theta,\theta')=\min\{1,R(\theta,\theta')\}$, where $R(\theta,\theta')=\pi(\theta')q(\theta\mid\theta')/[\pi(\theta)q(\theta'\mid\theta)]$. Then show that $\pi$ is invariant for the chain, being explicit about the rejection term.

**27.** *(§7.9)* Prove that a Gibbs update is a Metropolis-Hastings update with acceptance probability one, and that it leaves the target distribution invariant. Explain why the full conditional proposal is not symmetric in general.

**28.** *(§7.7)* Derive the Jeffreys prior for the Bernoulli model and show that it is $\operatorname{Beta}(1/2,1/2)$. Then prove that the Jeffreys prior is invariant under a smooth one-to-one reparameterisation $\phi=h(\theta)$.

**29.** *(§5.4)* Prove that, under squared-error loss, a Bayes estimator is the posterior mean, and that under absolute-error loss, a Bayes estimator is a posterior median. State the regularity conditions needed for the median result.

**30.** *(§7.3, §7.7)* Consider $x_1,\dots,x_n\mid\mu,\sigma^2\sim\mathcal{N}(\mu,\sigma^2)$ with the improper prior $\pi(\mu,\sigma^2)\propto1/\sigma^2$. Derive the marginal posterior density of $\mu$ and identify it as a Student $t$ distribution. State the condition on $n$ for the posterior to be proper.

## Challenge

**31.** *(§7.10)* Lindley's paradox. Let $x_1,\dots,x_n\mid\mu\sim\mathcal{N}(\mu,1)$, and compare $M_0:\mu=0$ with $M_1:\mu\sim\mathcal{N}(0,\tau^2)$.

(a) Derive $\operatorname{BF}_{10}$ as a function of $\bar x$, $n$, and $\tau^2$.
(b) Show that, for fixed $\bar x\ne0$ and fixed $n$, $\operatorname{BF}_{10}\to0$ as $\tau^2\to\infty$.
(c) Explain why this is not a contradiction: what does the Bayes factor actually compare?

**32.** *(§7.5)* Let $\theta\sim\pi$ be a proper prior, $X\mid\theta\sim p(\cdot\mid\theta)$, and suppose the posterior is continuous with strictly increasing CDF for every $x$. Prove that the equal-tailed $95\%$ credible interval has prior-averaged coverage exactly $0.95$:
$$
\Pr_{\theta\sim\pi,\,X\sim p(\cdot\mid\theta)}\bigl(\theta\in[q_{0.025}(X),q_{0.975}(X)]\bigr)=0.95.
$$
Explain why this does not imply $95\%$ coverage at each fixed $\theta$.

**33.** *(§7.11)* Let $\Theta=\{\theta_1,\dots,\theta_K\}$ be finite, let $\pi$ be a prior with $\pi(\theta)>0$ for all $\theta$, and let $x_1,x_2,\dots$ be iid with density $p(\cdot\mid\theta)$. Assume the model is identifiable: $\theta\ne\theta'$ implies $p(\cdot\mid\theta)\ne p(\cdot\mid\theta')$ almost everywhere. Prove that the posterior concentrates on the true parameter almost surely:
$$
\Pr(\theta=\theta_{\mathrm{true}}\mid x_{1:n})\to1\quad\text{a.s.}
$$
You may use the strong law of large numbers for the log-likelihood ratio.

**34.** *(§7.8)* Empirical Bayes for the normal hierarchy. Suppose $\bar y_j\mid\theta_j\sim\mathcal{N}(\theta_j,\sigma^2/n_j)$ and $\theta_j\sim\mathcal{N}(\mu,\tau^2)$, with $\sigma^2$ and $\mu$ known. Derive the marginal distribution of $\bar y_j$, the type-II maximum likelihood estimator of $\tau^2$, and the resulting shrinkage estimator of $\theta_j$. Discuss what happens when the estimator of $\tau^2$ is negative.

**35.** *(§7.5)* Construct an explicit example showing that a $95\%$ credible region need not be a $95\%$ confidence region. Take $\theta\in\{0,1\}$, prior $\Pr(\theta=0)=0.99$, and $X\mid\theta\sim\mathcal{N}(\theta,1)$. Compute the $95\%$ credible region as a function of $X$, and compute its frequentist coverage at $\theta=1$.

**36.** *(§5.7)* Prove that a Bayes factor is invariant under a smooth one-to-one reparameterisation of each model's parameter, provided the priors are transformed with the appropriate Jacobian. Then explain why a Bayes factor can change if the data are transformed without including the Jacobian of the data transformation.
