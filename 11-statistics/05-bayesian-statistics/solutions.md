# Bayesian Statistics — Solutions

> [Bayesian Statistics](README.md) · Solutions to the 36 problems in [exercises.md](exercises.md)

Every solution names the strategy and the theorem used. Numerical answers are checked by a second method where one is available. Section references point into the [tutorial](README.md).

## Beginner

**1.** *Strategy: Bayes' theorem for events, with the positive test as the conditioning event.*

Let $D$ be "disease" and $+$ be "positive test". The prior is $\Pr(D)=0.01$, so $\Pr(D^{\complement})=0.99$. The likelihoods are $\Pr(+\mid D)=0.95$ and $\Pr(+\mid D^{\complement})=0.10$ (since specificity $0.90$ means a $10\%$ false-positive rate). By Bayes' theorem,

$$
\Pr(D\mid +)=\frac{0.01\cdot0.95}{0.01\cdot0.95+0.99\cdot0.10}
=\frac{0.0095}{0.0095+0.099}
=\frac{0.0095}{0.1085}
=\frac{19}{217}\approx0.0876.
$$

So the posterior probability of disease is about $8.8\%$. The positive test raises the probability from $1\%$ to $8.8\%$, but the disease is still unlikely because it is rare. The normalising constant $0.1085$ is the prior predictive probability of a positive test.

**2.** *Strategy: beta-binomial conjugacy, then compare the posterior mean with the prior mean and the sample proportion.*

(a) With $\alpha=3$, $\beta=5$, $x=4$, $n=6$, the posterior is

$$
\operatorname{Beta}(3+4,5+2)=\operatorname{Beta}(7,7).
$$

(b) The posterior mean is $7/(7+7)=1/2$. The posterior mode is $(7-1)/(14-2)=6/12=1/2$. The prior mean is $3/(3+5)=3/8=0.375$.

(c) The sample proportion is $4/6=2/3\approx0.667$. The posterior mean $0.5$ lies between the prior mean $0.375$ and the sample proportion $0.667$, closer to the prior because the prior has weight $8/(8+6)=4/7\approx0.571$. Explicitly,

$$
\mathbb{E}[\theta\mid x]=\frac{8}{14}\cdot\frac38+\frac{6}{14}\cdot\frac46
=\frac{3}{14}+\frac{4}{14}=\frac12.
$$

The posterior variance is $49/(14^2\cdot15)=49/2940\approx0.01667$, so the posterior standard deviation is about $0.129$.

**3.** *Strategy: uniform prior is $\operatorname{Beta}(1,1)$; integrate the beta density exactly for the tail probability.*

(a) The posterior is $\operatorname{Beta}(1+8,1+2)=\operatorname{Beta}(9,3)$. Its mean is $9/12=3/4=0.75$, its mode is $(9-1)/(12-2)=8/10=0.8$, and its variance is

$$
\frac{9\cdot3}{12^2\cdot13}=\frac{27}{1872}\approx0.01442,
$$

so the standard deviation is about $0.1201$.

(b) The density is

$$
\pi(\theta\mid x)=\frac{1}{B(9,3)}\theta^8(1-\theta)^2,
\qquad
B(9,3)=\frac{\Gamma(9)\Gamma(3)}{\Gamma(12)}
=\frac{8!\cdot2!}{11!}=\frac{1}{495}.
$$

Thus

$$
\Pr(\theta\le1/2\mid x)
=495\int_0^{1/2}\theta^8(1-2\theta+\theta^2)\,d\theta
=495\left[\frac{\theta^9}{9}-\frac{2\theta^{10}}{10}+\frac{\theta^{11}}{11}\right]_0^{1/2}.
$$

At $\theta=1/2$,

$$
495\left(\frac{1}{9\cdot512}-\frac{2}{10\cdot1024}+\frac{1}{11\cdot2048}\right)
=495\left(\frac{1}{4608}-\frac{1}{5120}+\frac{1}{22528}\right)
=\frac{67}{2048}.
$$

Therefore $\Pr(\theta>1/2\mid x)=1-67/2048=1981/2048\approx0.9673$.

(c) The MLE is $\hat\theta_{\mathrm{MLE}}=8/10=0.8$. The Wald estimate is the same $0.8$, with standard error $\sqrt{0.8\cdot0.2/10}\approx0.1265$; the Wald interval $0.8\pm1.96(0.1265)=[0.552,1.048]$ crosses $1$ and is not trustworthy near the boundary. The posterior mean is $0.75$, pulled towards the prior mean $0.5$; the uniform prior acts like one prior success and one prior failure.

**4.** *Strategy: normal-normal update with one observation; posterior precision is the sum of precisions.*

(a) The prior precision is $1/4$ and the data precision is $1/4$, so the posterior precision is $1/2$ and the posterior variance is $2$. The posterior mean is

$$
\mu_1=\frac{\sigma^2\mu_0+\tau^2x}{\sigma^2+\tau^2}
=\frac{4\cdot10+4\cdot13}{8}=11.5.
$$

Thus $\mu\mid x\sim\mathcal{N}(11.5,2)$.

(b) The weight on the data is $\tau^2/(\sigma^2+\tau^2)=4/8=1/2$.

(c) The posterior standard deviation is $\sqrt2\approx1.414$, so the $95\%$ credible interval is

$$
11.5\pm1.96\sqrt2=[8.728,14.272].
$$

**5.** *Strategy: normal-normal update with $n$ observations and known variance.*

(a) The prior precision is $1/9$ and the data precision is $n/\sigma^2=4/4=1$. Hence

$$
\frac{1}{\tau_4^2}=\frac19+1=\frac{10}{9},
\qquad
\tau_4^2=0.9,
\qquad
\mu_4=\frac{\sigma^2\mu_0+n\tau^2\bar x}{\sigma^2+n\tau^2}
=\frac{4\cdot0+4\cdot9\cdot5}{4+36}=\frac{180}{40}=4.5.
$$

Thus $\mu\mid x\sim\mathcal{N}(4.5,0.9)$.

(b) The predictive variance is $\sigma^2+\tau_4^2=4+0.9=4.9$, so
$\tilde x\mid x\sim\mathcal{N}(4.5,4.9)$.

(c) Solve

$$
\frac{1}{1/9+n/4}\le0.5
\iff \frac19+\frac n4\ge2
\iff \frac n4\ge\frac{17}{9}
\iff n\ge\frac{68}{9}=7.56.
$$

The smallest integer is $n=8$. For $n=8$, the posterior variance is $9/19\approx0.474$.

**6.** *Strategy: gamma-Poisson conjugacy with exposure $T=2$, then the negative-binomial predictive.*

(a) The prior is $\operatorname{Gamma}(3,2)$ and the likelihood has $s=7$, $T=2$. Hence

$$
\lambda\mid x\sim\operatorname{Gamma}(3+7,2+2)=\operatorname{Gamma}(10,4).
$$

The posterior mean is $10/4=2.5$, the mode is $(10-1)/4=9/4=2.25$, and the variance is $10/4^2=10/16=0.625$.

(b) For one future unit, the predictive is negative binomial with $r=10$ and
$p=\beta'/(\beta'+1)=4/5$. Thus

$$
\Pr(Y=0\mid x)=p^r=(4/5)^{10}\approx0.1074.
$$

(c) The empirical rate is $7/2=3.5$. The posterior mean $2.5$ is a weighted average of the prior mean $3/2=1.5$ and the empirical rate $3.5$, with weights $\beta/(\beta+T)=2/4=1/2$ and $T/(\beta+T)=2/4=1/2$:

$$
\frac12\cdot1.5+\frac12\cdot3.5=2.5.
$$

**7.** *Strategy: integrate the Poisson likelihood against the gamma prior; the result is negative binomial.*

(a) For $Y=y$,

$$
\Pr(Y=y)=\int_0^\infty\frac{e^{-\lambda}\lambda^y}{y!}\cdot\frac{\lambda^{2-1}e^{-\lambda}}{\Gamma(2)}\,d\lambda
=\frac{1}{y!}\int_0^\infty\lambda^{y+1}e^{-2\lambda}\,d\lambda
=\frac{\Gamma(y+2)}{y!\,2^{y+2}}.
$$

For $y=0,1,2$:

$$
\Pr(Y=0)=\frac{1}{4},\qquad
\Pr(Y=1)=\frac{2}{8}=\frac14,\qquad
\Pr(Y=2)=\frac{6}{2\cdot16}=\frac{3}{16}=0.1875.
$$

(b) These three probabilities sum to $11/16=0.6875$; the remaining probability is $\Pr(Y\ge3)=5/16$. There is no reason for the first three values to sum to one.

(c) The negative-binomial form has $r=2$ and $p=1/2$, so the mean is $r(1-p)/p=2$ and the variance is $r(1-p)/p^2=4$. A Poisson variable with mean $2$ has variance $2$. The prior predictive is over-dispersed because $\lambda$ is uncertain; the law of total variance gives $\operatorname{Var}(Y)=\mathbb{E}[\lambda]+\operatorname{Var}(\lambda)=2+2=4$.

**8.** *Strategy: identify the probability space and the conditioning event in each statement.*

(a) **Bayesian credible statement.** It conditions on the data and uses the posterior; the prior is implicit.

(b) **Frequentist confidence statement.** It refers to the long-run coverage of a procedure over repeated samples, with $\theta$ fixed.

(c) **Neither.** "The probability that the null hypothesis is true" requires a prior probability on the null and a posterior; a p-value is $\Pr(\text{data at least as extreme}\mid H_0)$, not $\Pr(H_0\mid\text{data})$.

(d) **Bayesian posterior statement.** It is a direct probability statement about $\theta$ given the data and the model.

**9.** *Strategy: beta-binomial prior predictive with $\alpha=\beta=2$ and $n=5$.*

The prior predictive is

$$
\Pr(X=k)=\binom{5}{k}\frac{B(2+k,2+5-k)}{B(2,2)}.
$$

For $k=0$:

$$
\Pr(X=0)=\frac{B(2,7)}{B(2,2)}
=\frac{\Gamma(2)\Gamma(7)/\Gamma(9)}{\Gamma(2)\Gamma(2)/\Gamma(4)}
=\frac{1/56}{1/6}=\frac{3}{28}.
$$

For $k=1$:

$$
\Pr(X=1)=5\frac{B(3,6)}{B(2,2)}
=5\frac{1/168}{1/6}
=\frac{5}{28}.
$$

For $k=5$:

$$
\Pr(X=5)=\frac{B(7,2)}{B(2,2)}
=\frac{1/56}{1/6}
=\frac{3}{28}.
$$

As a check, the full distribution is $(3,5,6,6,5,3)/28$, which sums to $28/28=1$.

**10.** *Strategy: apply the beta update twice and compare with one batch update.*

Starting with $\operatorname{Beta}(2,3)$ and three successes gives

$$
\operatorname{Beta}(2+3,3)=\operatorname{Beta}(5,3).
$$

Then two failures give

$$
\operatorname{Beta}(5,3+2)=\operatorname{Beta}(5,5).
$$

A single batch with $x=3$ successes and $n-x=2$ failures gives

$$
\operatorname{Beta}(2+3,3+2)=\operatorname{Beta}(5,5).
$$

The results agree, as sequential updating guarantees.

**11.** *Strategy: match the kernel of the likelihood to the kernel of the conjugate prior.*

(a) Binomial with beta prior: $\operatorname{Beta}(\alpha,\beta)\to\operatorname{Beta}(\alpha+x,\beta+n-x)$.

(b) Poisson with gamma prior: $\operatorname{Gamma}(\alpha,\beta)\to\operatorname{Gamma}(\alpha+s,\beta+T)$, where $s$ is the total count and $T$ the total exposure.

(c) Normal with normal prior and known $\sigma^2$:
$\mathcal{N}(\mu_0,\tau^2)\to\mathcal{N}(\mu_n,\tau_n^2)$ with
$1/\tau_n^2=1/\tau^2+n/\sigma^2$ and
$\mu_n=(\sigma^2\mu_0+n\tau^2\bar x)/(\sigma^2+n\tau^2)$.

(d) Exponential with rate $\lambda$ and gamma prior:
the likelihood for $n$ observations is $\lambda^n e^{-\lambda\sum x_i}$, so
$\operatorname{Gamma}(\alpha,\beta)\to\operatorname{Gamma}(\alpha+n,\beta+\sum x_i)$.

**12.** *Strategy: Bayes factor is a ratio of marginal likelihoods; posterior odds multiply prior odds.*

(a) $\operatorname{BF}_{21}=m_2/m_1=0.10/0.05=2$, and $\operatorname{BF}_{12}=1/2$.

(b) With equal prior probabilities,

$$
\Pr(M_2\mid x)=\frac{2}{1+2}=\frac23,
\qquad
\Pr(M_1\mid x)=\frac13.
$$

(c) Prior odds $M_1:M_2=10:1$. Posterior odds $M_1:M_2=10\cdot\operatorname{BF}_{12}=10\cdot(1/2)=5:1$.

## Intermediate

**13.** *Strategy: multiply the likelihood by the uniform density and recognise a beta kernel.*

With $\pi(\theta)=1$,

$$
\pi(\theta\mid x)\propto\binom{n}{x}\theta^x(1-\theta)^{n-x}
\propto\theta^{(x+1)-1}(1-\theta)^{(n-x+1)-1}.
$$

The kernel is $\operatorname{Beta}(x+1,n-x+1)$. The normalising constant is
$\binom{n}{x}B(x+1,n-x+1)$. For $x=3$, $n=10$, the posterior is
$\operatorname{Beta}(4,8)$ and its mean is

$$
\frac{4}{4+8}=\frac13.
$$

The sample proportion is $0.3$; the posterior mean is slightly larger because the uniform prior contributes one success and one failure, shrinking towards $0.5$ from below.

**14.** *Strategy: derive the predictive by integrating over the beta posterior, then use the law of total variance.*

Let $\alpha'=\alpha+x$, $\beta'=\beta+n-x$, and $N=\alpha'+\beta'$. For $\tilde n$ future trials,

$$
p(\tilde x\mid x)
=\int_0^1\binom{\tilde n}{\tilde x}\theta^{\tilde x}(1-\theta)^{\tilde n-\tilde x}
\frac{\theta^{\alpha'-1}(1-\theta)^{\beta'-1}}{B(\alpha',\beta')}\,d\theta
=\binom{\tilde n}{\tilde x}\frac{B(\alpha'+\tilde x,\beta'+\tilde n-\tilde x)}{B(\alpha',\beta')}.
$$

This is beta-binomial with parameters $(\tilde n,\alpha',\beta')$. Its mean is
$\tilde n\alpha'/(\alpha'+\beta')$. To derive the variance, condition on $\theta$: $\tilde X\mid\theta$ is binomial, so $\mathbb{E}[\tilde X\mid\theta]=\tilde n\theta$ and
$\operatorname{Var}(\tilde X\mid\theta)=\tilde n\theta(1-\theta)$. Therefore

$$
\operatorname{Var}(\tilde X)
=\tilde n\mathbb{E}[\theta(1-\theta)]+\tilde n^2\operatorname{Var}(\theta)
=\frac{\tilde n Np(1-p)}{N+1}+\frac{\tilde n^2p(1-p)}{N+1}
=\tilde n p(1-p)\frac{N+\tilde n}{N+1},
$$

where $p=\alpha'/N$. For $\alpha=3$, $\beta=2$, $x=0$ (so $\alpha'=3$, $\beta'=2$, $N=5$), $\tilde n=4$:

$$
\mathbb{E}[\tilde X]=4\cdot\frac35=2.4,
\qquad
\operatorname{Var}(\tilde X)=4\cdot\frac35\cdot\frac25\cdot\frac{5+4}{6}
=\frac{144}{100}=1.44.
$$

**15.** *Strategy: Fisher information for the Poisson model, then conjugate update.*

The log-density for one observation is $\ell(\lambda)=x\log\lambda-\lambda-\log(x!)$. Then

$$
\ell'(\lambda)=\frac{x}{\lambda}-1,
\qquad
\ell''(\lambda)=-\frac{x}{\lambda^2},
\qquad
I(\lambda)=-\mathbb{E}[\ell''(\lambda)]=\frac{\mathbb{E}[X]}{\lambda^2}=\frac1\lambda.
$$

Thus $\pi(\lambda)\propto\sqrt{I(\lambda)}=\lambda^{-1/2}$, which is improper because
$\int_0^\infty\lambda^{-1/2}\,d\lambda=\infty$. With $s$ events and exposure $T$, the likelihood is
$\propto\lambda^s e^{-T\lambda}$, so

$$
\pi(\lambda\mid x)\propto\lambda^{s-1/2}e^{-T\lambda},
$$

which is $\operatorname{Gamma}(s+1/2,T)$. For $s=5$, $T=2$, the posterior is
$\operatorname{Gamma}(11/2,2)$, with mean $(11/2)/2=11/4=2.75$ and mode
$(11/2-1)/2=(9/2)/2=9/4=2.25$. The posterior is proper because $s+1/2>0$.

**16.** *Strategy: posterior precision grows linearly in $n$; solve the variance inequality.*

The posterior variance with prior $\tau^2=1$ and observation variance $\sigma^2=4$ is

$$
\tau_n^2=\frac{1}{1/1+n/4}=\frac{4}{4+n}.
$$

Require $\tau_n^2\le0.5$:

$$
\frac{4}{4+n}\le\frac12
\iff 8\le4+n
\iff n\ge4.
$$

The posterior precision is $1+n/4$, so the variance is $1/(1+n/4)=4/(4+n)$, and the smallest
integer satisfying the inequality is $n=4$. For $n=4$,

$$
\mu_4=\frac{\sigma^2\mu_0+n\tau^2\bar x}{\sigma^2+n\tau^2}
=\frac{4\cdot0+4\cdot1\cdot2}{4+4}=1,
$$

and the weight on the data is $n\tau^2/(\sigma^2+n\tau^2)=4/8=1/2$.

**17.** *Strategy: beta posterior, exact tail, and comparison with a boundary-truncated Wald interval.*

(a) With ten successes and a uniform prior, the posterior is
$\operatorname{Beta}(11,1)$.

(b) The posterior density is $11\theta^{10}$ on $(0,1)$. The $5\%$ quantile $q$ satisfies

$$
\int_0^q11\theta^{10}\,d\theta=q^{11}=0.05,
$$

so $q=0.05^{1/11}\approx0.7616$. The $95\%$ equal-tailed interval is $[0.7616,1]$.

(c) The MLE is $1$, and the Wald interval degenerates to $[1,1]$, which is not a useful uncertainty statement. The rule-of-three approximation $1-3/n=0.7$ is a rough lower bound. The Bayesian lower bound $0.7616$ is larger than $0.7$ because the uniform prior and the exact beta tail give more information than the crude rule. All three reflect the same fact: after ten successes, small values of $\theta$ are strongly excluded, but $\theta$ could still be modestly below $1$.

**18.** *Strategy: use the weighted-average form of the beta posterior mean.*

For prior $\operatorname{Beta}(\alpha,\beta)$ and data $x=6$, $n=10$,

$$
\mathbb{E}[\theta\mid x]
=\frac{\alpha+\beta}{\alpha+\beta+10}\cdot\frac{\alpha}{\alpha+\beta}
+\frac{10}{\alpha+\beta+10}\cdot\frac{6}{10}.
$$

* $\operatorname{Beta}(1,1)$: posterior $\operatorname{Beta}(7,5)$, mean $7/12=0.5833$. The prior mean is $0.5$, and the prior weight is $2/12=1/6\approx0.167$.
* $\operatorname{Beta}(10,10)$: posterior $\operatorname{Beta}(16,14)$, mean $16/30=0.5333$. The prior mean is $0.5$, and the prior weight is $20/30=2/3\approx0.667$.
* $\operatorname{Beta}(2,8)$: posterior $\operatorname{Beta}(8,12)$, mean $8/20=0.4$. The prior mean is $0.2$, and the prior weight is $10/20=1/2$.

The sample proportion is $0.6$. The posterior mean moves towards the prior mean, and the movement is largest when the prior is concentrated and far from the data.

**19.** *Strategy: independence proposal; ratio of target times reverse proposal to target times forward proposal.*

(a) For the independence proposal $q(\theta'\mid\theta)=\lambda e^{-\lambda\theta'}$,

$$
R(\theta,\theta')
=\frac{e^{-\theta'}\lambda e^{-\lambda\theta}}{e^{-\theta}\lambda e^{-\lambda\theta'}}
=e^{(\lambda-1)(\theta-\theta')}.
$$

(b) With $\lambda=1/2$, $\theta=2$, $\theta'=0.5$,

$$
R=e^{(1/2-1)(2-0.5)}=e^{-0.75}\approx0.4724.
$$

Thus $\alpha=\min\{1,0.4724\}=0.4724$.

(c) If $u=0.3\le0.4724$, accept. If $u=0.6>0.4724$, reject and keep $\theta=2$. The rejection is more likely here because the exponential proposal with rate $1/2$ has mean $2$, so proposing $0.5$ is a move to a lower-density region of the proposal and of the target.

**20.** *Strategy: treat one parameter as fixed and complete the square in the other.*

With $\mu\sim\mathcal{N}(\mu_0,\tau^2)$ and $\sigma^2\sim\operatorname{InvGamma}(\alpha_0,\beta_0)$ independent, the joint prior is proportional to

$$
(\sigma^2)^{-1/2}\exp\left(-\frac{(\mu-\mu_0)^2}{2\tau^2}\right)
(\sigma^2)^{-\alpha_0-1}\exp\left(-\frac{\beta_0}{\sigma^2}\right).
$$

Conditional on $\sigma^2$, the normal-normal update gives

$$
\mu\mid\sigma^2,x\sim\mathcal{N}\left(
\frac{\mu_0/\tau^2+n\bar x/\sigma^2}{1/\tau^2+n/\sigma^2},
\frac{1}{1/\tau^2+n/\sigma^2}
\right).
$$

Conditional on $\mu$, the likelihood is proportional to
$(\sigma^2)^{-n/2}\exp[-\frac{1}{2\sigma^2}\sum_i(x_i-\mu)^2]$, and the inverse-gamma prior is conjugate:

$$
\sigma^2\mid\mu,x\sim\operatorname{InvGamma}\left(
\alpha_0+\frac n2,\ \beta_0+\frac12\sum_{i=1}^{n}(x_i-\mu)^2
\right).
$$

These two full conditionals define a valid Gibbs sampler because the joint posterior is proper (assuming a proper prior and $n\ge1$).

**21.** *Strategy: compute marginal likelihoods exactly using the beta integral.*

(a) Under $M_1$, $\theta=1/2$, so

$$
m_1=\binom{10}{8}\left(\frac12\right)^{10}=\frac{45}{1024}\approx0.04395.
$$

Under $M_2$, the prior density is $6\theta(1-\theta)$. Hence

$$
m_2=\int_0^1\binom{10}{8}\theta^8(1-\theta)^2\cdot6\theta(1-\theta)\,d\theta
=45\cdot6\cdot B(10,4).
$$

Now $B(10,4)=\Gamma(10)\Gamma(4)/\Gamma(14)=362880\cdot6/6227020800=1/2860$, so

$$
m_2=\frac{270}{2860}=\frac{27}{286}\approx0.09441.
$$

(b) $\operatorname{BF}_{21}=m_2/m_1=(27/286)/(45/1024)=1536/715\approx2.148$.

(c) With equal prior probabilities,

$$
\Pr(M_2\mid x)=\frac{1536/715}{1+1536/715}
=\frac{1536}{2251}\approx0.6824.
$$

(d) A Bayes factor of about $2.15$ is in the "barely worth mentioning" range on Jeffreys' scale. The data slightly favour the beta prior model over the exact fair coin, but the evidence is weak.

**22.** *Strategy: normal-normal conditional posterior with $\mu$ and $\tau^2$ fixed.*

(a) The shrinkage factor is $B_j=\sigma^2/(\sigma^2+n_j\tau^2)$:

$$
B_1=\frac{4}{4+4\cdot4}=\frac{4}{20}=0.2,
\qquad
B_2=\frac{4}{4+16\cdot4}=\frac{4}{68}=\frac1{17}\approx0.0588.
$$

(b) The conditional posterior means are

$$
\mathbb{E}[\theta_1\mid\mu,\tau^2,y]=(1-0.2)\cdot10+0.2\cdot12=8+2.4=10.4,
$$

$$
\mathbb{E}[\theta_2\mid\mu,\tau^2,y]=\frac{16}{17}\cdot14+\frac1{17}\cdot12
=\frac{224+12}{17}=\frac{236}{17}\approx13.882.
$$

(c) Group 1 shrinks more because it has only $n_1=4$ observations, so its data-based estimate is less precise. Its shrinkage factor $0.2$ is much larger than group 2's $0.0588$.

## Advanced

**23.** *Strategy: write both posteriors as likelihood times prior and compare normalising constants.*

Let $x_{1:m}$ and $x_{m+1:n}$ be the two batches. The full posterior is

$$
\pi(\theta\mid x_{1:n})
=\frac{p(x_{1:n}\mid\theta)\pi(\theta)}{m(x_{1:n})}.
$$

Because the observations are independent conditional on $\theta$,

$$
p(x_{1:n}\mid\theta)=p(x_{1:m}\mid\theta)\,p(x_{m+1:n}\mid\theta).
$$

Therefore

$$
\pi(\theta\mid x_{1:n})
=\frac{p(x_{m+1:n}\mid\theta)\,p(x_{1:m}\mid\theta)\pi(\theta)}{m(x_{1:n})}
=\frac{p(x_{m+1:n}\mid\theta)\,\pi(\theta\mid x_{1:m})\,m(x_{1:m})}{m(x_{1:n})}.
$$

The factor $m(x_{1:m})/m(x_{1:n})$ does not depend on $\theta$, so

$$
\pi(\theta\mid x_{1:n})\propto p(x_{m+1:n}\mid\theta)\,\pi(\theta\mid x_{1:m}).
$$

This is exactly the posterior obtained by using $\pi(\theta\mid x_{1:m})$ as the prior and updating with the second batch. The normalising constant of the sequential update is
$m(x_{1:n})/m(x_{1:m})$. Independence is used in the factorisation of the likelihood; without it, the second factor would be $p(x_{m+1:n}\mid\theta,x_{1:m})$, and the simple prior-to-posterior update would fail.

**24.** *Strategy: exchange the order of integration, then use beta-binomial moments.*

The predictive integral is

$$
p(\tilde x\mid x)
=\int_0^1\binom{\tilde n}{\tilde x}\theta^{\tilde x}(1-\theta)^{\tilde n-\tilde x}
\frac{\theta^{\alpha+x-1}(1-\theta)^{\beta+n-x-1}}{B(\alpha+x,\beta+n-x)}\,d\theta.
$$

The beta integral is

$$
\int_0^1\theta^{\alpha+x+\tilde x-1}(1-\theta)^{\beta+n-x+\tilde n-\tilde x-1}\,d\theta
=B(\alpha+x+\tilde x,\beta+n-x+\tilde n-\tilde x),
$$

so

$$
p(\tilde x\mid x)=\binom{\tilde n}{\tilde x}
\frac{B(\alpha+x+\tilde x,\beta+n-x+\tilde n-\tilde x)}
{B(\alpha+x,\beta+n-x)}.
$$

For the mean, condition on $\theta$: each future trial has success probability $\theta$, so
$\mathbb{E}[\tilde X\mid\theta]=\tilde n\theta$ and
$\mathbb{E}[\tilde X]=\tilde n\mathbb{E}[\theta\mid x]=\tilde n(\alpha+x)/(\alpha+\beta+n)$.

For the variance, use
$\operatorname{Var}(\tilde X)=\mathbb{E}[\operatorname{Var}(\tilde X\mid\theta)] +\operatorname{Var}(\mathbb{E}[\tilde X\mid\theta])$. With $\tilde X\mid\theta\sim\operatorname{Bin}(\tilde n,\theta)$,

$$
\operatorname{Var}(\tilde X)=\tilde n\mathbb{E}[\theta(1-\theta)]
+\tilde n^2\operatorname{Var}(\theta).
$$

Let $p=(\alpha+x)/(\alpha+\beta+n)$ and $N=\alpha+\beta+n$. For a beta distribution,
$\operatorname{Var}(\theta)=p(1-p)/(N+1)$, so
$\mathbb{E}[\theta^2]=p^2+p(1-p)/(N+1)$ and
$$
\mathbb{E}[\theta(1-\theta)]
=p-\mathbb{E}[\theta^2]
=p(1-p)-\frac{p(1-p)}{N+1}
=\frac{Np(1-p)}{N+1}.
$$

Hence

$$
\operatorname{Var}(\tilde X)
=\frac{\tilde n Np(1-p)}{N+1}+\frac{\tilde n^2p(1-p)}{N+1}
=\frac{\tilde n p(1-p)(N+\tilde n)}{N+1}.
$$

This agrees with the beta-binomial variance formula with parameters $(\tilde n,\alpha+x,\beta+n-x)$.

**25.** *Strategy: gamma integral, then the law of total variance.*

With posterior $\operatorname{Gamma}(\alpha',\beta')$, where $\alpha'=\alpha+s$ and $\beta'=\beta+T$,

$$
p(y\mid x)
=\int_0^\infty\frac{e^{-\lambda}\lambda^y}{y!}
\frac{(\beta')^{\alpha'}}{\Gamma(\alpha')}\lambda^{\alpha'-1}e^{-\beta'\lambda}\,d\lambda
=\frac{(\beta')^{\alpha'}}{y!\Gamma(\alpha')}
\int_0^\infty\lambda^{\alpha'+y-1}e^{-(\beta'+1)\lambda}\,d\lambda.
$$

The integral is $\Gamma(\alpha'+y)/(\beta'+1)^{\alpha'+y}$, so

$$
p(y\mid x)=\frac{\Gamma(\alpha'+y)}{\Gamma(\alpha')y!}
\left(\frac{\beta'}{\beta'+1}\right)^{\alpha'}
\left(\frac{1}{\beta'+1}\right)^y,
$$

which is negative binomial with $r=\alpha'$ and $p=\beta'/(\beta'+1)$.

Its mean is $r(1-p)/p=\alpha'/\beta'$. Its variance is
$r(1-p)/p^2=\alpha'(\beta'+1)/(\beta')^2=\alpha'/\beta'+\alpha'/(\beta')^2$. The Poisson variance with the same mean would be $\alpha'/\beta'$. The extra term $\alpha'/(\beta')^2$ is the variance of $\lambda$ under the posterior. The law of total variance gives

$$
\operatorname{Var}(Y)=\mathbb{E}[\operatorname{Var}(Y\mid\lambda)]
+\operatorname{Var}(\mathbb{E}[Y\mid\lambda])
=\mathbb{E}[\lambda]+\operatorname{Var}(\lambda)
=\frac{\alpha'}{\beta'}+\frac{\alpha'}{(\beta')^2}.
$$

Thus parameter uncertainty always increases predictive variance relative to a Poisson model at a point estimate.

**26.** *Strategy: verify detailed balance case by case, then integrate it over the starting state.*

Let $\pi$ be the target density and $q$ the proposal. Define

$$
R(\theta,\theta')=\frac{\pi(\theta')q(\theta\mid\theta')}{\pi(\theta)q(\theta'\mid\theta)},
\qquad
\alpha(\theta,\theta')=\min\{1,R(\theta,\theta')\}.
$$

If $\pi(\theta')q(\theta\mid\theta')\ge\pi(\theta)q(\theta'\mid\theta)$, then
$\alpha(\theta,\theta')=1$ and
$\alpha(\theta',\theta)=\pi(\theta)q(\theta'\mid\theta)/[\pi(\theta')q(\theta\mid\theta')]$.
Hence

$$
\pi(\theta)q(\theta'\mid\theta)\alpha(\theta,\theta')
=\pi(\theta)q(\theta'\mid\theta)
=\pi(\theta')q(\theta\mid\theta')\alpha(\theta',\theta).
$$

The other case is identical with $\theta$ and $\theta'$ interchanged. Therefore detailed balance holds.

For invariance, write the transition kernel as

$$
P(\theta,A)=\int_A q(\theta'\mid\theta)\alpha(\theta,\theta')\,d\theta'
+\mathbf1\{\theta\in A\}\int q(\theta'\mid\theta)(1-\alpha(\theta,\theta'))\,d\theta'.
$$

The second term is the probability of rejection, which leaves the chain at $\theta$. Then

$$
\int\pi(\theta)P(\theta,A)\,d\theta
=\int_A\int\pi(\theta)q(\theta'\mid\theta)\alpha(\theta,\theta')\,d\theta\,d\theta'
+\int_A\pi(\theta)r(\theta)\,d\theta,
$$

where $r(\theta)=\int q(\theta'\mid\theta)(1-\alpha(\theta,\theta'))\,d\theta'$. By detailed balance, the double integral equals

$$
\int_A\pi(\theta')\int q(\theta\mid\theta')\alpha(\theta',\theta)\,d\theta\,d\theta'.
$$

The inner integral is $1-r(\theta')$, so the two terms combine to

$$
\int_A\pi(\theta')\bigl(1-r(\theta')+r(\theta')\bigr)\,d\theta'
=\int_A\pi(\theta')\,d\theta'.
$$

Thus $\pi P=\pi$. Ergodicity (irreducibility, aperiodicity, positive recurrence) is a separate assumption needed for convergence from a starting point, not for invariance.

**27.** *Strategy: substitute the full conditional into the Metropolis-Hastings ratio.*

Suppose the current state is $\theta=(\theta_i,\theta_{-i})$ and the proposal changes only $\theta_i$ to $\theta_i'$, drawn from the full conditional
$q(\theta_i'\mid\theta)=\pi(\theta_i'\mid\theta_{-i})$. The reverse proposal is
$q(\theta_i\mid\theta')=\pi(\theta_i\mid\theta_{-i})$. The joint density factorises as

$$
\pi(\theta_i,\theta_{-i})=\pi(\theta_i\mid\theta_{-i})\pi(\theta_{-i}).
$$

Hence the acceptance ratio is

$$
R
=\frac{\pi(\theta_i',\theta_{-i})\,\pi(\theta_i\mid\theta_{-i})}
{\pi(\theta_i,\theta_{-i})\,\pi(\theta_i'\mid\theta_{-i})}
=\frac{\pi(\theta_i'\mid\theta_{-i})\pi(\theta_{-i})\pi(\theta_i\mid\theta_{-i})}
{\pi(\theta_i\mid\theta_{-i})\pi(\theta_{-i})\pi(\theta_i'\mid\theta_{-i})}
=1.
$$

Thus $\alpha=1$ and the update is always accepted. It leaves the target invariant by the general Metropolis-Hastings invariance theorem. The full conditional proposal is not symmetric in general: the density of proposing $\theta_i'$ from $\theta_i$ is $\pi(\theta_i'\mid\theta_{-i})$, while the reverse density is $\pi(\theta_i\mid\theta_{-i})$; these are different functions unless the full conditional is symmetric.

**28.** *Strategy: compute the Fisher information and use the change-of-variables formula.*

For $X\sim\operatorname{Bernoulli}(\theta)$, the log-density is

$$
\ell(\theta)=x\log\theta+(1-x)\log(1-\theta).
$$

Then

$$
\ell'(\theta)=\frac{x}{\theta}-\frac{1-x}{1-\theta},
\qquad
\ell''(\theta)=-\frac{x}{\theta^2}-\frac{1-x}{(1-\theta)^2}.
$$

Since $\mathbb{E}[X]=\theta$,

$$
I(\theta)=\frac{\theta}{\theta^2}+\frac{1-\theta}{(1-\theta)^2}
=\frac1\theta+\frac1{1-\theta}
=\frac{1}{\theta(1-\theta)}.
$$

Thus

$$
\pi(\theta)\propto\sqrt{I(\theta)}
=\theta^{-1/2}(1-\theta)^{-1/2},
$$

which is the kernel of $\operatorname{Beta}(1/2,1/2)$.

For invariance, let $\phi=h(\theta)$ be smooth and strictly monotone, with inverse $\theta=h^{-1}(\phi)$. Fisher information transforms as

$$
I_\phi(\phi)=I_\theta(\theta)\left(\frac{d\theta}{d\phi}\right)^2.
$$

The Jeffreys density in $\phi$ is therefore

$$
\pi_\phi(\phi)\propto\sqrt{I_\phi(\phi)}
=\sqrt{I_\theta(\theta)}\left|\frac{d\theta}{d\phi}\right|
=\pi_\theta(\theta)\left|\frac{d\theta}{d\phi}\right|,
$$

which is exactly the transformation law for a density under $\phi=h(\theta)$. Hence the Jeffreys prior is invariant.

**29.** *Strategy: differentiate the posterior expected loss; use convexity for the minimum.*

For squared error,

$$
R(a)=\int_\Theta(\theta-a)^2\pi(\theta\mid x)\,d\theta.
$$

Differentiating under the integral sign,

$$
R'(a)=-2\int_\Theta(\theta-a)\pi(\theta\mid x)\,d\theta
=-2\left(\mathbb{E}[\theta\mid x]-a\right).
$$

Setting $R'(a)=0$ gives $a=\mathbb{E}[\theta\mid x]$. Since $R''(a)=2>0$, this critical point is the unique global minimum. (Finiteness of the posterior second moment is assumed.)

For absolute error,

$$
R(a)=\int_\Theta\lvert\theta-a\rvert\pi(\theta\mid x)\,d\theta.
$$

A subgradient is

$$
R'(a)=\int_{\theta<a}\pi(\theta\mid x)\,d\theta-\int_{\theta>a}\pi(\theta\mid x)\,d\theta
=\Pr(\theta<a\mid x)-\Pr(\theta>a\mid x).
$$

At a point where both tails have posterior probability $1/2$, zero belongs to the subdifferential, and convexity of $R$ makes $a$ a global minimiser. Such an $a$ is a posterior median. If the posterior is continuous, the median is unique; if there is an atom or a flat region, every median is a Bayes estimator.

**30.** *Strategy: integrate out $\sigma^2$ from the joint posterior.*

With $\pi(\mu,\sigma^2)\propto1/\sigma^2$, the joint posterior is

$$
\pi(\mu,\sigma^2\mid x)
\propto(\sigma^2)^{-n/2-1}
\exp\left[-\frac{1}{2\sigma^2}\left(n(\mu-\bar x)^2+S\right)\right],
\qquad
S=\sum_{i=1}^{n}(x_i-\bar x)^2.
$$

Let $A=S+n(\mu-\bar x)^2>0$. Then

$$
\pi(\mu\mid x)\propto\int_0^\infty(\sigma^2)^{-n/2-1}e^{-A/(2\sigma^2)}\,d\sigma^2.
$$

Substitute $u=A/(2\sigma^2)$, so $\sigma^2=A/(2u)$ and $d\sigma^2=-A/(2u^2)\,du$. Then

$$
\int_0^\infty(\sigma^2)^{-n/2-1}e^{-A/(2\sigma^2)}\,d\sigma^2
\propto A^{-n/2}\int_0^\infty u^{n/2-1}e^{-u}\,du
=A^{-n/2}\Gamma(n/2).
$$

Therefore

$$
\pi(\mu\mid x)\propto\left[S+n(\mu-\bar x)^2\right]^{-n/2}
=\left[1+\frac{(\mu-\bar x)^2}{S/n}\right]^{-n/2}.
$$

This is a Student $t$ density with $\nu=n-1$ degrees of freedom, location $\bar x$, and scale $s/\sqrt n$, where $s^2=S/(n-1)$, because

$$
\left[1+\frac{(\mu-\bar x)^2}{(n-1)s^2/n}\right]^{-(n+1)/2}
=\left[1+\frac{(\mu-\bar x)^2}{S/n}\right]^{-n/2}.
$$

The posterior is proper for $n\ge2$; for $n=1$, $S=0$ and the density is proportional to $\lvert\mu-\bar x\rvert^{-1}$, which is not integrable. The improper prior is therefore usable only when the data contain at least two observations.

## Challenge

**31.** *Strategy: compute the two marginal likelihoods via the distribution of $\bar x$.*

(a) Under $M_0:\mu=0$, $\bar x\sim\mathcal{N}(0,1/n)$, so

$$
m_0=\left(\frac{n}{2\pi}\right)^{1/2}e^{-n\bar x^2/2}.
$$

Under $M_1:\mu\sim\mathcal{N}(0,\tau^2)$, $\bar x\sim\mathcal{N}(0,\tau^2+1/n)$, so

$$
m_1=\left(\frac{1}{2\pi(\tau^2+1/n)}\right)^{1/2}
\exp\left(-\frac{\bar x^2}{2(\tau^2+1/n)}\right).
$$

Therefore

$$
\operatorname{BF}_{10}
=\frac{m_1}{m_0}
=(1+n\tau^2)^{-1/2}
\exp\left(\frac{n\bar x^2}{2}\cdot\frac{n\tau^2}{1+n\tau^2}\right).
$$

In terms of $z=\sqrt n\,\bar x$, the exponent is $z^2n\tau^2/[2(1+n\tau^2)]$.

(b) For fixed $\bar x\ne0$ and fixed $n$, as $\tau^2\to\infty$,

$$
(1+n\tau^2)^{-1/2}\to0,
\qquad
\exp\left(\frac{n\bar x^2}{2}\cdot\frac{n\tau^2}{1+n\tau^2}\right)
\to e^{n\bar x^2/2}.
$$

The product tends to $0$. Thus a very diffuse prior on the alternative makes the Bayes factor favour the point null, even when $\bar x$ is several standard errors from $0$.

(c) The Bayes factor compares the prior predictive density of the data under each model. A diffuse $\mathcal{N}(0,\tau^2)$ prior spreads its mass over a wide range, so it assigns low density to the actual data. The point null concentrates all its mass at $\mu=0$. The comparison is therefore sensitive to the prior spread, not only to the distance of the data from the null. This is Lindley's paradox; it is not a contradiction, because the alternative model is a different model for each $\tau^2$. A sensitivity analysis over realistic $\tau^2$ is essential.

**32.** *Strategy: condition on $\theta$, integrate over the data, and use the definition of the posterior quantile.*

Let $F_x$ be the posterior CDF and $q_p(x)=F_x^{-1}(p)$. By continuity,
$\Pr(\theta\le q_p(x)\mid x)=p$ for each $x$. Hence, for every $x$,

$$
\Pr\bigl(\theta\in[q_{0.025}(x),q_{0.975}(x)]\mid x\bigr)
=0.975-0.025=0.95.
$$

Now average over the marginal distribution of $X$. Since the prior is proper, the joint distribution of $(\theta,X)$ has density $\pi(\theta)p(x\mid\theta)$ and

$$
\Pr\bigl(\theta\in C(X)\bigr)
=\int_\Theta\int_{\mathcal X}\mathbf1\{\theta\in C(x)\}p(x\mid\theta)\pi(\theta)\,dx\,d\theta.
$$

By Fubini and the display above,

$$
=\int_{\mathcal X}\Pr\bigl(\theta\in C(x)\mid X=x\bigr)m(x)\,dx
=\int_{\mathcal X}0.95\,m(x)\,dx
=0.95.
$$

This is coverage averaged over the prior. It does not say that for a fixed $\theta$ the random interval has $95\%$ coverage; the conditional coverage given $\theta$ can be far from $0.95$. That is the difference between a Bayesian credible procedure and a frequentist confidence procedure.

**33.** *Strategy: compare each alternative with the truth by a log-likelihood ratio and apply the strong law.*

Fix $k\ne\mathrm{true}$ and define

$$
\Lambda_n(k)=\sum_{i=1}^{n}\log\frac{p(x_i\mid\theta_k)}{p(x_i\mid\theta_{\mathrm{true}})}.
$$

The summands are iid with mean

$$
\mathbb{E}_{\mathrm{true}}\left[\log\frac{p(X\mid\theta_k)}{p(X\mid\theta_{\mathrm{true}})}\right]
=-D_{\mathrm{KL}}\bigl(p(\cdot\mid\theta_{\mathrm{true}})\,\|\,p(\cdot\mid\theta_k)\bigr)<0.
$$

The strict inequality follows from identifiability: if the KL divergence were $0$, the two densities would agree almost everywhere, contradicting $\theta_k\ne\theta_{\mathrm{true}}$. By the strong law of large numbers,

$$
\frac{\Lambda_n(k)}{n}\to-D_{\mathrm{KL}}<0
\quad\text{almost surely},
$$

so $\Lambda_n(k)\to-\infty$ almost surely.

The posterior odds of $k$ against the truth are

$$
\frac{\pi(\theta_k\mid x_{1:n})}{\pi(\theta_{\mathrm{true}}\mid x_{1:n})}
=\frac{\pi(\theta_k)}{\pi(\theta_{\mathrm{true}})}e^{\Lambda_n(k)}
\to0
\quad\text{almost surely}.
$$

There are finitely many $k\ne\mathrm{true}$, so the convergence holds simultaneously for all of them on a single probability-one event. Since

$$
\Pr(\theta=\theta_{\mathrm{true}}\mid x_{1:n})
=\frac{1}{1+\sum_{k\ne\mathrm{true}}\frac{\pi(\theta_k\mid x)}{\pi(\theta_{\mathrm{true}}\mid x)}},
$$

the sum tends to $0$ and the posterior probability tends to $1$.

**34.** *Strategy: marginalise the hierarchy, then maximise the type-II likelihood.*

Since $\bar y_j=\theta_j+\varepsilon_j$ with $\theta_j\sim\mathcal{N}(\mu,\tau^2)$ and
$\varepsilon_j\sim\mathcal{N}(0,\sigma^2/n_j)$ independent,

$$
\bar y_j\sim\mathcal{N}\left(\mu,\ \tau^2+\frac{\sigma^2}{n_j}\right).
$$

Assume for simplicity that all $n_j=n$, and set $v=\sigma^2/n$. The type-II log-likelihood is

$$
\ell(\tau^2)=-\frac J2\log(2\pi)-\frac12\sum_{j=1}^{J}\log(\tau^2+v)
-\frac{1}{2}\sum_{j=1}^{J}\frac{(\bar y_j-\mu)^2}{\tau^2+v}.
$$

Differentiate with respect to $\tau^2$:

$$
\ell'(\tau^2)=-\frac12\sum_{j=1}^{J}\frac{1}{\tau^2+v}
+\frac12\sum_{j=1}^{J}\frac{(\bar y_j-\mu)^2}{(\tau^2+v)^2}.
$$

Setting $\ell'=0$ gives

$$
J(\tau^2+v)=\sum_{j=1}^{J}(\bar y_j-\mu)^2,
\qquad
\widehat{\tau^2}=\frac1J\sum_{j=1}^{J}(\bar y_j-\mu)^2-v.
$$

Because a variance cannot be negative, the constrained estimator is
$\max\{0,\widehat{\tau^2}\}$. The conditional posterior mean is

$$
\mathbb{E}[\theta_j\mid y,\mu,\tau^2]
=\frac{\mu/\tau^2+\bar y_j/v}{1/\tau^2+1/v}
=(1-B_j)\bar y_j+B_j\mu,
\qquad
B_j=\frac{v}{v+\tau^2}.
$$

If $\widehat{\tau^2}\le0$, the model is pooled completely: $\theta_j$ is estimated by $\mu$ for every $j$. With unequal $n_j$, the maximisation has no closed form in general; one solves

$$
\sum_j\frac{(\bar y_j-\mu)^2-(v_j+\tau^2)}{(v_j+\tau^2)^2}=0
$$

numerically, truncated at zero.

**35.** *Strategy: compute posterior odds, choose the $95\%$ highest-posterior region, and evaluate its coverage under $\theta=1$.*

The prior odds are $\Pr(\theta=1)/\Pr(\theta=0)=0.01/0.99=1/99$. The likelihood ratio for $X=x$ is

$$
\frac{p(x\mid1)}{p(x\mid0)}
=\frac{e^{-(x-1)^2/2}}{e^{-x^2/2}}
=e^{x-1/2}.
$$

Hence the posterior odds are

$$
\frac{\Pr(\theta=1\mid x)}{\Pr(\theta=0\mid x)}
=\frac{1}{99}e^{x-1/2}.
$$

The posterior probability of $\theta=1$ reaches $0.05$ when the odds equal $1/19$:

$$
\frac{1}{99}e^{x-1/2}=\frac1{19}
\iff e^{x-1/2}=\frac{99}{19}
\iff x=\frac12+\log\frac{99}{19}\approx2.151.
$$

It reaches $0.95$ when the odds equal $19$:

$$
\frac{1}{99}e^{x-1/2}=19
\iff x=\frac12+\log(1881)\approx7.539.
$$

Thus a $95\%$ highest-posterior region is

$$
C(x)=
\begin{cases}
\{0\}, & x<2.151,\\
\{0,1\}, & 2.151\le x<7.539,\\
\{1\}, & x\ge7.539.
\end{cases}
$$

At $\theta=1$, the region contains $1$ exactly when $X\ge2.151$. Therefore

$$
\Pr_{\theta=1}(1\in C(X))
=\Pr(X\ge2.151\mid\theta=1)
=1-\Phi(1.151)
\approx0.125.
$$

So a region with $95\%$ posterior probability can have only about $12.5\%$ frequentist coverage at $\theta=1$. The discrepancy is possible because the prior puts $99\%$ mass on $\theta=0$; the Bayesian procedure is calibrated by that prior, not by repeated sampling at each fixed $\theta$. At $\theta=0$ the coverage is essentially $1$, so the prior-averaged coverage is high.

**36.** *Strategy: change variables inside each marginal likelihood.*

For model $k$, let $\phi_k=h_k(\theta_k)$ be a smooth one-to-one reparameterisation, with inverse $\theta_k=h_k^{-1}(\phi_k)$. The prior density transforms as

$$
\pi_k^{\phi}(\phi_k)=\pi_k^{\theta}(h_k^{-1}(\phi_k))
\left|\frac{d h_k^{-1}}{d\phi_k}\right|.
$$

The marginal likelihood in the new parameterisation is

$$
m_k(x)=\int p_k(x\mid h_k^{-1}(\phi_k))\,
\pi_k^{\theta}(h_k^{-1}(\phi_k))
\left|\frac{d h_k^{-1}}{d\phi_k}\right|\,d\phi_k.
$$

Substituting $\theta_k=h_k^{-1}(\phi_k)$ and
$d\phi_k=|h_k'(\theta_k)|\,d\theta_k$ gives

$$
m_k(x)=\int p_k(x\mid\theta_k)\pi_k^{\theta}(\theta_k)\,d\theta_k,
$$

which is the original marginal likelihood. Hence each $m_k$ is unchanged, and so is
$\operatorname{BF}_{10}=m_1/m_0$.

For a data transformation $y=g(x)$, the density of $Y$ is

$$
p_Y(y\mid\theta)=p_X(g^{-1}(y)\mid\theta)
\left|\frac{d g^{-1}}{dy}\right|.
$$

If the same one-to-one transformation is applied to the data under both models, the Jacobian factor is identical and cancels in the ratio of marginal likelihoods. If it is omitted, the two marginal likelihoods are densities with respect to different measures, and their ratio is not a Bayes factor. Likewise, comparing models for different transformations of the response (for example, a model for $y$ against a model for $\log y$) requires including the Jacobian explicitly; otherwise the comparison is between non-comparable densities.
