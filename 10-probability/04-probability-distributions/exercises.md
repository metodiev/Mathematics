# Probability Distributions — Exercises

> [Probability Distributions](README.md) · 36 problems · Beginner → Challenge · Solutions: [solutions.md](solutions.md)

Attempt each problem before reading [solutions.md](solutions.md). The section reference names where the
necessary material is. Use the conventions of the tutorial: the geometric and negative binomial families count
trials, not failures, and gamma laws are parametrised by a rate.

**Conventions.** $q=1-p$. $\Phi$ is the standard normal CDF. Numerical answers are given to four decimal places;
exact answers are preferred where they are available.

## Beginner

**1.** *(§7.1, §7.2)* Let $X\sim\operatorname{Bin}(5,0.3)$.

(a) Compute $\Pr(X=0)$, $\Pr(X=1)$ and $\Pr(X=2)$.
(b) Compute $\Pr(X\ge1)$ and $\Pr(X\le2)$.
(c) State $\mathbb{E}[X]$, $\operatorname{Var}(X)$ and the standard deviation.
(d) Explain why $\Pr(X=0)=(0.7)^5$ and not $(0.3)^5$.

**2.** *(§7.3)* Let $X\sim\text{Geometric}(0.25)$.

(a) Compute $\Pr(X=4)$ and $\Pr(X>4)$.
(b) Compute $\Pr(X\le2)$.
(c) State the mean, the variance and the standard deviation.
(d) Compute $\Pr(X>8\mid X>4)$ and explain the answer without computing conditional probabilities.

**3.** *(§7.6)* Let $X\sim\operatorname{Pois}(2)$.

(a) Compute $\Pr(X=0)$, $\Pr(X=1)$, $\Pr(X=3)$.
(b) Compute $\Pr(X\ge1)$ and $\Pr(X\ge2)$.
(c) State the mean, the variance and the standard deviation.
(d) Show that $\Pr(X=k+1)/\Pr(X=k)=\lambda/(k+1)$ for every $k\ge0$, and use it to compute $\Pr(X=4)$ from
$\Pr(X=3)$. Comment on what the ratio says about the shape of the pmf.

**4.** *(§7.7)* Let $X\sim\text{Uniform}(1,5)$.

(a) Write the density and the CDF.
(b) Compute the mean and the variance.
(c) Compute $\Pr(2<X<4)$ and $\Pr(X=3)$.
(d) Find the median and the interquartile range.

**5.** *(§7.8)* Let $X\sim\text{Exponential}(0.5)$.

(a) Compute the mean, the variance and the standard deviation.
(b) Compute $\Pr(X>2)$ and $\Pr(X\le1)$.
(c) Find the median.
(d) Find the hazard rate and explain what it means.

**6.** *(§7.12)* Let $X\sim\mathcal{N}(10,4)$, so $\sigma=2$.

(a) Compute $\Pr(X\le12)$ and $\Pr(8<X<12)$.
(b) Find the $0.975$-quantile.
(c) Compute $\Pr(X=10)$.
(d) State the interval containing $99.73\%$ of the mass, and check it against the empirical rule.

**7.** *(§7.9)* Let $X\sim\text{Gamma}(2,3)$.

(a) Write the density and verify that it integrates to $1$.
(b) Compute the mean and the variance.
(c) Write the MGF.
(d) Identify $X$ as a sum of independent exponential variables, naming their rate.

**8.** *(§7.10)* Let $P\sim\text{Beta}(3,2)$.

(a) Write the density, evaluating $B(3,2)$.
(b) Compute $\mathbb{E}[P]$, $\operatorname{Var}(P)$ and the mode.
(c) Compute the density at $p=0.5$.
(d) Compute $\Pr(P\le0.5)$.

**9.** *(§7.11)* Let $X\sim\chi^2_4$.

(a) Identify $X$ as a gamma variable, giving shape and rate.
(b) Write the density in closed form and compute $f(2)$.
(c) Compute the mean and the variance.
(d) Write the MGF and use it to find the law of $X+Y$ when $Y\sim\chi^2_3$ is independent of $X$.

**10.** *(§7.5)* An urn contains $20$ balls, $5$ of them red. Four are drawn without replacement. Let $X$ be the
number of red balls drawn.

(a) Compute $\Pr(X=0)$ and $\Pr(X=4)$.
(b) Compute the mean and the variance.
(c) Compare the variance with the binomial variance for $n=4$, $p=0.25$, and explain the difference.
(d) What is the support of $X$?

**11.** *(§7.4)* Let $X\sim\text{NegativeBinomial}(4,0.5)$, counting trials.

(a) Compute $\Pr(X=4)$ and $\Pr(X=6)$.
(b) State the mean and the variance.
(c) Verify that $\Pr(X=4)=p^4$ and explain why.
(d) Express $X$ as a sum of simpler variables and use this to check the mean.

**12.** *(§5, §7)* Name the family (with parameters) for each experiment, and justify the choice in one line:

(a) the number of sixes in $12$ rolls of a fair die;
(b) the number of rolls until the first six;
(c) the number of defective items in a sample of $10$ drawn without replacement from a lot of $200$ containing
$20$ defectives;
(d) the number of emails arriving in one hour at a mean rate of $30$ per hour, assuming independent arrivals;
(e) the time until a radioactive atom decays, given a constant decay rate;
(f) the fraction of a population carrying a rare allele, when a genetic model suggests a flexible density on
$(0,1)$ with mean $0.2$.

## Intermediate

**13.** *(§7.6, §8.4)* Let $X\sim\operatorname{Bin}(20,0.1)$.

(a) Compute $\Pr(X=0)$, $\Pr(X=1)$ and $\Pr(X\le1)$ exactly.
(b) Approximate the same quantities with a Poisson law of the same mean, and compare.
(c) Explain which of the two models is exact here and why the approximation is nevertheless accurate.

**14.** *(§7.4)* A basketball player scores with probability $0.4$ per shot, independently. Let $X$ be the number
of shots up to and including the third basket.

(a) Compute $\Pr(X=5)$ and $\Pr(X\le5)$.
(b) State the mean and the standard deviation.
(c) Compute $\Pr(X>10)$ using the binomial law rather than the negative binomial pmf.
(d) Verify your answer to (c) by a direct sum of the negative binomial pmf up to $k=10$.

**15.** *(§7.5)* A population has $100$ members, $20$ of them "marked". A sample of $10$ is drawn.

(a) Compute $\Pr(X=2)$ under sampling without replacement (hypergeometric).
(b) Compute $\Pr(X=2)$ under sampling with replacement (binomial with $p=0.2$).
(c) Compare the two variances.
(d) Explain the direction of the difference in (c).

**16.** *(§7.6, §8.5)* Events occur in a Poisson process of rate $4$ per hour. Let $N(A)$ be the number of events
in an interval $A$.

(a) Compute $\Pr\bigl(N((0,0.5])=0\bigr)$.
(b) Compute $\Pr\bigl(N((0,1])=3\bigr)$.
(c) State the distribution of the waiting time $T$ to the first event, and compute $\Pr\bigl(T>\tfrac13\bigr)$.
(d) Compute the probability that at least one event occurs in each of two disjoint half-hour intervals.

**17.** *(§7.8)* The lifetime $T$ of a component is exponential with mean $8$ years.

(a) Compute $\Pr(T>10)$ and the median lifetime.
(b) Compute $\Pr(T>18\mid T>8)$ and interpret.
(c) Compute $\Pr(T\le10\mid T>8)$.
(d) A second component is known to have a wear-out hazard that increases with age. Would your answer to (b) be
larger or smaller for it? Explain.

**18.** *(§7.9, §7.6)* The times between events of a Poisson process are iid exponential with rate $0.5$ per hour.
Let $S_3$ be the time of the third event.

(a) State the law of $S_3$ with its parameters, mean and variance.
(b) Compute $\Pr(S_3\le2)$ by integrating the gamma density.
(c) Compute the same probability by a Poisson count and check that the answers agree.
(d) Explain why the two computations must agree.

**19.** *(§7.10)* Let $P\sim\text{Beta}(2,4)$.

(a) Compute the mean, the variance and the mode.
(b) Write the density and compute $f(0.5)$.
(c) Compute $\Pr(P\le0.5)$.
(d) Is the distribution left-skewed or right-skewed? Justify with the mean, the median and the mode.

**20.** *(§7.12)* Let $X\sim\operatorname{Bin}(100,0.4)$.

(a) Compute $\Pr(X\le35)$ with a continuity-corrected normal approximation, and compare with the exact value
$0.1795$.
(b) Approximate $\Pr(X=40)$ by the normal density over $[39.5,40.5]$ and compare with the exact $0.0812$.
(c) Explain why the continuity correction improves the approximation.
(d) State the mean and the variance of the approximating normal law.

**21.** *(§7.11, §7.12)* Let $Z\sim\mathcal{N}(0,1)$.

(a) Derive the density of $Y=Z^2$ from the normal density.
(b) Show that $Y\sim\chi^2_1$ by comparing with the chi-squared density.
(c) Compute $\Pr(Z^2\le1)$ from the normal CDF and from the chi-squared density, and check that the answers agree.
(d) Use the result to explain why a $\chi^2_1$ variable has a density that blows up at $0$.

**22.** *(§7.9, §8.1)* Let $X\sim\text{Gamma}(\alpha,\lambda)$.

(a) Starting from $M(t)=(\lambda/(\lambda-t))^\alpha$, compute $\log M$, $(\log M)'$ and $(\log M)''$.
(b) Evaluate at $t=0$ and read off the mean and variance.
(c) Check that the answers agree with §7.9.
(d) Explain why $(\log M)''(0)=\operatorname{Var}(X)$ and not merely $\mathbb{E}[X^2]$.

**23.** *(§7.6, §7.9)* Let $X\sim\operatorname{Pois}(2)$ and $Y\sim\operatorname{Pois}(3)$ be independent.

(a) Show that $X+Y\sim\operatorname{Pois}(5)$.
(b) Compute $\Pr(X+Y\le1)$.
(c) Compute $\Pr(X=1\mid X+Y=3)$ by direct calculation with the joint pmf.
(d) Identify the conditional law of $X$ given $X+Y=n$, and state its mean.

## Advanced

**24.** *(§7.4)* Let $X\sim\text{NegativeBinomial}(r,p)$ with pmf $\Pr(X=k)=\binom{k-1}{r-1}p^rq^{k-r}$ for $k\ge r$.

(a) Prove the normalisation $\sum_{k\ge r}\Pr(X=k)=1$ using the negative binomial series.
(b) Prove that $\mathbb{E}[X]=r/p$ by direct summation, using the identities
$(j+r)\binom{j+r-1}{j}=r\binom{j+r}{j}$ and $\sum_{j\ge0}\binom{j+r}{j}q^j=(1-q)^{-r-1}$, where $j=k-r$.
(c) Prove by induction on $r$ that the sum of $r$ iid Geometric$(p)$ variables has this pmf, using the hockey-stick
identity $\sum_{j=a}^{b}\binom{j}{a}=\binom{b+1}{a+1}$.
(d) Deduce the mean and variance of the negative binomial from (c), stating clearly which property of expectation
and variance you use.

**25.** *(§7.3, §8.5)* Let $X$ take values in $\{1,2,3,\dots\}$.

(a) Prove that if $X$ is geometric with parameter $p$, then $\Pr(X>n+k\mid X>n)=\Pr(X>k)$ for all $n,k\ge0$.
(b) Conversely, suppose $\Pr(X>n+k\mid X>n)=\Pr(X>k)$ for all $n,k\ge0$ and that $\Pr(X>1)\in(0,1)$. Put
$S(n)=\Pr(X>n)$ and prove that $S(n)=S(1)^n$.
(c) Deduce that $X$ is geometric with $p=1-S(1)$.
(d) Explain where the converse fails if one allows $X$ to be unbounded below or to have $\Pr(X>1)=0$.

**26.** *(§7.6, §8.4)* Let $X_n\sim\operatorname{Bin}(n,\lambda_n)$ with $\lambda_n=np_n\to\lambda>0$. Fix $k\ge0$.

(a) Write $\Pr(X_n=k)$ as a product of the four factors displayed in §7.6.
(b) Show that the first factor differs from $1$ by at most $k(k-1)/(2n)$.
(c) Show that $\bigl\lvert(1-\lambda_n/n)^n-e^{-\lambda_n}\bigr\rvert\le C/n$ for some constant $C$ depending on
$\lambda$ alone, when $\lambda_n\le2\lambda$. (Hint: compare the logarithms, using
$\log(1-x)=-x-x^2/2+O(x^3)$.)
(d) Conclude that $\lvert\Pr(X_n=k)-e^{-\lambda}\lambda^k/k!\rvert\le C_k/n$ for a constant $C_k$ depending on
$k$ and $\lambda$.

**27.** *(§7.6)* Let $X\sim\operatorname{Pois}(\lambda)$ and $Y\sim\operatorname{Pois}(\mu)$ be independent.

(a) Compute the conditional pmf of $X$ given $X+Y=n$ from the joint pmf.
(b) Identify the conditional law and its parameters.
(c) Compute $\Pr(X=1\mid X+Y=3)$ for $\lambda=2$, $\mu=3$ and check against Exercise 23(c).
(d) Interpret the result as "thinning": each of the $n$ events is independently of type $X$ with probability
$\lambda/(\lambda+\mu)$.

**28.** *(§7.5, §8.4)* Let $X_N\sim\text{Hypergeometric}(N,K,n)$ with $K=K_N$ and $K_N/N\to p\in(0,1)$, and let
$Y\sim\operatorname{Bin}(n,p)$. Fix $k$ in the support.

(a) Write $\Pr(X_N=k)$ as a product of binomial-coefficient ratios.
(b) Show that $\binom{K_N}{k}\big/\binom{N}{k}\to p^k$ and that
$\binom{N-K_N}{n-k}\big/\binom{N-k}{n-k}\to(1-p)^{n-k}$.
(c) Show that $\binom{N}{k}\binom{N-k}{n-k}=\binom{N}{n}\binom{n}{k}$, so the third factor is the constant
$\binom{n}{k}$.
(d) Conclude that $\Pr(X_N=k)\to\Pr(Y=k)$, and explain why this is consistent with the variance formula
$np(1-p)(N-n)/(N-1)\to np(1-p)$.

**29.** *(§7.8, §8.5)* Let $T$ be a positive random variable with survival function $S(t)=\Pr(T>t)$ that is
non-increasing and right-continuous, with $S(0)=1$.

(a) Show that memorylessness, $S(s+t)=S(s)S(t)$ for all $s,t\ge0$, holds for the exponential law.
(b) Conversely, assume memorylessness and $S(1)\in(0,1)$. Prove $S(n)=S(1)^n$ for integers $n$, then
$S(1/m)=S(1)^{1/m}$, then $S(q)=S(1)^q$ for rational $q\ge0$.
(c) Use right-continuity and monotonicity to extend the identity to all real $t\ge0$, and conclude that
$S(t)=e^{-\lambda t}$ with $\lambda=-\log S(1)$.
(d) Explain why the argument fails without right-continuity, and what pathologies can occur.

**30.** *(§7.11)* Let $Z_1,\dots,Z_\nu$ be iid standard normal and $X=\sum_{i=1}^\nu Z_i^2$.

(a) Show that $Z_1^2\sim\text{Gamma}(\tfrac12,\tfrac12)$ by computing its density.
(b) Deduce the density of $X$ from the gamma family, and verify the normalising constant.
(c) Compute $\mathbb{E}[X]$ and $\operatorname{Var}(X)$ two ways: from the gamma formulas and from the
representation as a sum of squares (using $\mathbb{E}[Z^2]=1$ and $\mathbb{E}[Z^4]=3$).
(d) Write the MGF of $X$ and use it to identify the law of the sum of independent $\chi^2_{\nu_1}$ and
$\chi^2_{\nu_2}$ variables.

## Challenge

**31.** *(§7.10, §7.14)* Let $X\sim\text{Gamma}(a,\lambda)$ and $Y\sim\text{Gamma}(b,\lambda)$ be independent, and
put $U=X/(X+Y)$ and $V=X+Y$.

(a) Write the joint density of $(X,Y)$.
(b) Apply the change of variables $(x,y)\mapsto(u,v)$ with $x=uv$, $y=(1-u)v$ and compute the Jacobian.
(c) Show that the joint density of $(U,V)$ factorises as a function of $u$ times a function of $v$, and identify
both factors.
(d) Conclude that $U\sim\text{Beta}(a,b)$, that $V\sim\text{Gamma}(a+b,\lambda)$, and that $U$ and $V$ are
independent.
(e) Deduce the identity $B(a,b)=\Gamma(a)\Gamma(b)/\Gamma(a+b)$ by integrating the density of $U$.

**32.** *(§7.6, §8.3)* Let $X\sim\operatorname{Pois}(\lambda)$ and $Y\sim\operatorname{Pois}(\mu)$ be independent.

(a) Compute $\Pr(X+Y=n)$ by direct convolution, using Vandermonde's identity.
(b) Show that the result is the $\operatorname{Pois}(\lambda+\mu)$ pmf.
(c) Explain why this second proof (the first being via MGFs) does not rely on uniqueness of moment generating
functions, and why that matters conceptually.
(d) Extend the argument by induction to $n$ independent Poisson variables.

**33.** *(§5, §7.12, §7.13)* Let $\varphi_d(x)=(2\pi)^{-d/2}e^{-\lvert x\rvert^2/2}$ on $\mathbb{R}^d$.

(a) Prove that $\int_{\mathbb{R}}\varphi_1(x)dx=1$ by computing the square of the integral in polar coordinates.
(b) Prove by Fubini that $\int_{\mathbb{R}^d}\varphi_d(x)dx=1$.
(c) For an invertible $d\times d$ matrix $A$, derive the density of $Y=AZ$ where $Z$ has density $\varphi_d$, using
the change-of-variables formula with the Jacobian determinant.
(d) Show that the result is the multivariate normal density with $\mu=0$ and $\Sigma=AA^{\mathsf{T}}$, and check
that the normalising constant is $(2\pi)^{d/2}\sqrt{\det\Sigma}$.

**34.** *(§7.14)* Let $\Lambda\sim\text{Gamma}(\alpha,\beta)$ and, conditionally on $\Lambda=\lambda$, let
$N\sim\operatorname{Pois}(\lambda)$.

(a) Write $\Pr(N=n\mid\Lambda=\lambda)$ and the density of $\Lambda$.
(b) Compute $\Pr(N=n)$ by integrating over $\lambda$.
(c) Evaluate the integral using the gamma function and identify the result as a negative binomial (polya) pmf
with parameters $\alpha$ and $p=\beta/(\beta+1)$.
(d) Compute $\mathbb{E}[N]$ two ways: directly from the mixture, and from the negative binomial mean formula.
(e) Explain why the mixture has a larger variance than a Poisson law with the same mean.

**35.** *(§7.10)* Let $P\sim\text{Beta}(a,b)$.

(a) Show that the density satisfies $f'(x)=\dfrac{f(x)}{x(1-x)}\bigl[(a-1)(1-x)-(b-1)x\bigr]$ for $0<x<1$.
(b) Deduce that if $a>1$ and $b>1$ the density has a unique maximum at $(a-1)/(a+b-2)$, and compute its value.
(c) Show that if $a<1$ and $b<1$ the density tends to $+\infty$ at both endpoints and has a unique minimum at
$(a-1)/(a+b-2)$; conclude that the density is U-shaped.
(d) Show that if $a=1$, $b>1$ the density is strictly decreasing, and describe the case $a=b=1$.
(e) Sketch, in words, the four shapes and give one modelling situation for each.

**36.** *(§7.12, §8.3)* Let $X\sim\mathcal{N}(\mu_1,\sigma_1^2)$ and $Y\sim\mathcal{N}(\mu_2,\sigma_2^2)$ be
independent.

(a) Write the convolution integral for the density of $X+Y$.
(b) Combine the two exponents into a single quadratic in $x$, and complete the square to write it as
$-\dfrac{(x-m)^2}{2s^2}+c$ for suitable $m$ and $s^2$ and a constant $c$ not depending on $x$.
(c) Evaluate the remaining Gaussian integral and show that the result is the
$\mathcal{N}(\mu_1+\mu_2,\sigma_1^2+\sigma_2^2)$ density.
(d) Identify $m$ and $s^2$ in terms of the parameters, and explain why this computation is the two-variable
version of the MGF proof.
