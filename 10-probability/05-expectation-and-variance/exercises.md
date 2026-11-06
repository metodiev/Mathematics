# Expectation and Variance — Exercises

> [Expectation and Variance](README.md) · 36 problems · Beginner → Challenge · Solutions: [solutions.md](solutions.md)

Work through the problems in order. Every problem is solvable with the definitions and theorems of the
tutorial, and the section reference tells you where to look. Do not consult [solutions.md](solutions.md)
until you have written an attempt: the attempt is where the learning happens.

**Conventions.** Dice are fair and independent, "uniform" means the uniform distribution on the stated
set, $\mathbb{N}=\{1,2,3,\dots\}$, and $\mathbb{E}[X]$ is understood only when the absolute sum or
integral converges. $\operatorname{Var}$ always means the population variance, and $\rho$ the Pearson
correlation. Logarithms in entropy questions are base $2$ unless stated otherwise.

## Beginner

**1.** *(§5.2)* A discrete random variable takes the values $-1$, $0$ and $2$ with probabilities $0.2$,
$0.5$ and $0.3$ respectively.

(a) Compute $\mathbb{E}[X]$ and $\mathbb{E}[X^{2}]$.
(b) Compute $\operatorname{Var}(X)$ and $\sigma_X$.
(c) Compute $\mathbb{E}[2X+3]$ twice: from the definition, and from linearity.

**2.** *(§7.8)* A non-negative random variable has $\mathbb{E}[X]=4$ and $\operatorname{Var}(X)=1$.

(a) Bound $\Pr(X\ge10)$ with Markov's inequality.
(b) Bound $\Pr(\lvert X-4\rvert\ge3)$ with Chebyshev's inequality.
(c) Show that the bound in (a) cannot be improved by any argument that uses only the mean: exhibit a
distribution with $\mathbb{E}[X]=4$ for which $\Pr(X\ge10)=0.4$ exactly.

**3.** *(§7.4)* A fair die shows $X$.

(a) Compute $\mathbb{E}[X]$ and $\operatorname{Var}(X)$.
(b) Compute $\mathbb{E}[2X-1]$ and $\operatorname{Var}(2X-1)$.

**4.** *(§7.4)* $X$ is uniform on the interval $[2,8]$.

(a) Write down its density and compute $\mathbb{E}[X]$.
(b) Compute $\mathbb{E}[X^{2}]$ and $\operatorname{Var}(X)$.
(c) Verify $\operatorname{Var}(X)=(b-a)^{2}/12$ for these $a,b$.

**5.** *(§7.3, §7.7)* Let $X\sim\operatorname{Exp}(2)$, so $f(x)=2e^{-2x}$ for $x\ge0$.

(a) Compute $\mathbb{E}[X]$ and $\mathbb{E}[X^{3}]$.
(b) Compute $\mathbb{E}[e^{X}]$ by LOTUS. Is the answer finite? Explain via the MGF.
(c) Compute $\mathbb{E}[e^{2X}]$ and explain why it is infinite.

**6.** *(§7.4)* Two random variables have $\operatorname{Var}(X)=4$, $\operatorname{Var}(Y)=9$ and
$\operatorname{Cov}(X,Y)=4$.

(a) Compute $\operatorname{Var}(X+Y)$ and $\operatorname{Var}(X-Y)$.
(b) Compute $\rho(X,Y)$.
(c) Verify the parallelogram law $\operatorname{Var}(X+Y)+\operatorname{Var}(X-Y)=2\operatorname{Var}(X)+2\operatorname{Var}(Y)$.

**7.** *(§7.4)* Let $X$ take the values $+1$ and $-1$ with probability $\tfrac12$ each.

(a) Compute $\mathbb{E}[X]$ and $\operatorname{Var}(X)$.
(b) Put $Y=X^{2}$ and compute $\operatorname{Var}(Y)$.
(c) Which theorem explains the second answer without computation?

**8.** *(§7.2)* An urn holds $10$ balls, $3$ of them red. Five are drawn without replacement. Using
indicator variables, compute the expected number of red balls drawn.

**9.** *(§7.4)* A random variable has $\mathbb{E}[X]=10$ and $\operatorname{Var}(X)=4$. Compute
$\mathbb{E}[(X-c)^{2}]$ for $c=10$, $c=12$ and $c=0$, and say which $c$ is optimal.

**10.** *(§7.9)* Compute the entropy in bits and in nats of

(a) a uniform distribution on $8$ points;
(b) the distribution $\bigl(\tfrac12,\tfrac14,\tfrac18,\tfrac18\bigr)$.

**11.** *(§7.7)* A random variable has MGF $M(t)=\exp\bigl(3(e^{t}-1)\bigr)$.

(a) Identify the distribution.
(b) Read off $\mathbb{E}[X]$ and $\operatorname{Var}(X)$.
(c) Compute $\Pr(X=2)$.

## Intermediate

**12.** *(§7.8)* Let $X\sim\operatorname{Bin}(100,\tfrac12)$.

(a) Use Chebyshev to bound $\Pr(\lvert X-50\rvert\ge20)$.
(b) Compute the exact probability (to four significant figures are enough) and the ratio of the bound to
the truth.
(c) Which inequality would you use for a bound on $\Pr(X\ge70)$, and why is it better here?

**13.** *(§7.2, §7.4)* An urn holds $N=10$ balls, $K=3$ red; $n=5$ are drawn without replacement, and
$X$ counts reds.

(a) Compute $\mathbb{E}[X]$ and $\operatorname{Var}(X)$ using the hypergeometric formulas
$\mathbb{E}[X]=nK/N$ and $\operatorname{Var}(X)=n\frac KN\bigl(1-\frac KN\bigr)\frac{N-n}{N-1}$.
(b) Compute the variance of the corresponding binomial count that would arise *with* replacement, and
explain the direction of the difference in words.

**14.** *(§7.2)* A collector draws uniformly with replacement from $6$ coupon types.

(a) Compute the expected number of draws needed to obtain all six.
(b) Compute the expected number of *distinct* types obtained after exactly $6$ draws.
(c) Explain why (a) and (b) can both be computed by linearity without knowing any joint distribution.

**15.** *(§7.3)* Let $X$ be uniform on $\{1,2,3,4\}$. Compute

(a) $\mathbb{E}\bigl[(-1)^{X}\bigr]$;
(b) $\mathbb{E}\bigl[\lvert X-2.5\rvert\bigr]$;
(c) $\mathbb{E}\bigl[\min(X,3)\bigr]$.

**16.** *(§7.5)* Let $X$ be uniform on $\{-1,0,1\}$ and $Y=X^{2}$.

(a) Show $\operatorname{Cov}(X,Y)=0$.
(b) Show $X$ and $Y$ are not independent by comparing $\Pr(Y=1\mid X=0)$ with $\Pr(Y=1)$.
(c) What does this example disprove, and what does it *not* disprove?

**17.** *(§7.7)* Let $X\sim\mathcal{N}(1,4)$ and $Y\sim\mathcal{N}(2,9)$ be independent.

(a) Write down $M_X(t)$ and $M_Y(t)$.
(b) Find the distribution of $2X-Y$, justifying the mean and variance you use.
(c) Compute $\mathbb{E}[e^{X}]$.

**18.** *(§7.5)* Let $U$ be uniform on $[0,1]$. Compute $\operatorname{Cov}(U,U^{2})$ and $\rho(U,U^{2})$,
and comment on the sign and size.

**19.** *(§7.6)* The pair $(X,Y)$ takes values in $\{0,1\}^{2}$ with $\Pr(X=0,Y=0)=0.2$,
$\Pr(X=1,Y=0)=0.3$, $\Pr(X=0,Y=1)=0.1$, $\Pr(X=1,Y=1)=0.4$.

(a) Compute $\mathbb{E}[X\mid Y=0]$ and $\mathbb{E}[X\mid Y=1]$.
(b) Verify the tower property numerically.
(c) Verify the law of total variance numerically.

**20.** *(§7.8)* Let $X$ take the values $1$ and $9$ with probability $\tfrac12$ each.

(a) Compute $\mathbb{E}[X]$, $\mathbb{E}[X^{2}]$ and $(\mathbb{E}X)^{2}$, and observe the direction of
Jensen's inequality for $\varphi(x)=x^{2}$.
(b) Verify AM–GM for the two numbers: compare $\sqrt{1\cdot9}$ with $(1+9)/2$.
(c) Explain why $\mathbb{E}[\ln X]\le\ln\mathbb{E}[X]$ is the same inequality with a different $\varphi$.

**21.** *(§7.6)* A random number $N$ is uniform on $\{1,\dots,10\}$. Given $N=n$, the variables
$X_1,\dots,X_n$ are i.i.d. $\operatorname{Exp}(1)$ and $S_N=X_1+\cdots+X_N$.

(a) Compute $\mathbb{E}[S_N]$ using conditioning.
(b) Compute $\operatorname{Var}(S_N)$ using the law of total variance.
(c) State which independence assumptions you used at each step.

**22.** *(§7.8)* For a random variable with mean $\mu$ and variance $\sigma^{2}$, Chebyshev's inequality
gives $\Pr(\lvert X-\mu\rvert\ge k\sigma)\le1/k^{2}$.

(a) Which $k$ makes the bound equal to $0.01$?
(b) What does the bound say at $k=1$? Is that informative?
(c) Give a distribution for which the bound is attained at $k=2$.

**23.** *(§7.7)* Let $X\sim\operatorname{Pois}(2)$ and $Y\sim\operatorname{Pois}(3)$ be independent.

(a) Identify the distribution of $X+Y$ and justify it with MGFs.
(b) Compute $\Pr(X+Y=0)$ and $\mathbb{E}[(X+Y)^{2}]$.
(c) Compute $\operatorname{Cov}(X,X+Y)$.

## Advanced

**24.** *(§5.5)*

(a) Prove that $\mathbb{E}[X^{2}]<\infty$ implies $\mathbb{E}\lvert X\rvert<\infty$, using
$\lvert x\rvert\le1+x^{2}$.
(b) Give a distribution with finite mean and infinite second moment, and prove both claims.
(c) Explain why the converse of (a) cannot hold.

**25.** *(§8.2)* Let $X$ take values in $\{0,1,2,\dots\}$ with $\mathbb{E}[X]<\infty$.

(a) Prove $\mathbb{E}[X]=\sum_{k\ge1}\Pr(X\ge k)$.
(b) Use it to compute $\mathbb{E}[T]$ for a geometric variable $T$ with success probability $p$, where
$\Pr(T\ge k)=(1-p)^{k-1}$.
(c) Compute $\sum_{k\ge1}k\Pr(T\ge k)$ and explain what quantity it represents.

**26.** *(§7.8)*

(a) Prove Chebyshev's inequality from Markov's inequality.
(b) Show that the bound is attained, for each $k>1$, by a three-point distribution, and give its masses.
(c) Deduce that no better bound depending only on $\mu$ and $\sigma$ is possible.

**27.** *(§7.5)*

(a) Prove that $(\mathbb{E}[XY])^{2}\le\mathbb{E}[X^{2}]\mathbb{E}[Y^{2}]$ for $X,Y\in L^{2}$.
(b) Deduce $\mathbb{E}\lvert XY\rvert\le\sqrt{\mathbb{E}[X^{2}]\mathbb{E}[Y^{2}]}$.
(c) Show that $\mathbb{E}\lvert X\rvert\le\sqrt{\mathbb{E}[X^{2}]}$ and identify when equality holds.

**28.** *(§7.6)* Let $X$ and $Y$ be discrete with finite ranges, and let $Z$ be discrete.

(a) Prove $\mathbb{E}\bigl[\mathbb{E}[X\mid Y,Z]\bigm|Y\bigr]=\mathbb{E}[X\mid Y]$ by direct summation.
(b) Explain where the hypothesis "$\sigma(Y)\subseteq\sigma(Y,Z)$" is used.
(c) Give a one-line counterexample showing that
$\mathbb{E}\bigl[\mathbb{E}[X\mid Y]\bigm|Y,Z\bigr]=\mathbb{E}[X\mid Y]$ is nevertheless also true.

**29.** *(§7.6)* Prove the law of total variance
$\operatorname{Var}(X)=\mathbb{E}[\operatorname{Var}(X\mid Y)]+\operatorname{Var}(\mathbb{E}[X\mid Y])$
under the hypothesis $\mathbb{E}[X^{2}]<\infty$, stating which theorems you use at each step.

**30.** *(§7.7)*

(a) Prove $M_{X+Y}=M_XM_Y$ for independent $X,Y$ at a value $t$ where both MGFs are finite.
(b) Use it to prove that the sum of independent $\operatorname{Bin}(m,p)$ and $\operatorname{Bin}(n,p)$
variables is $\operatorname{Bin}(m+n,p)$.
(c) Explain why the same argument does *not* prove that a sum of binomials with different $p$'s is
binomial.

**31.** *(§7.8, extension)* *(Cantelli's one-sided inequality.)* Let $\operatorname{Var}(X)=\sigma^{2}$ and
$a>0$.

(a) For $t>0$, apply Markov to $(X-\mu+t)^{2}$ to show
$\Pr(X-\mu\ge a)\le(\sigma^{2}+t^{2})/(a+t)^{2}$.
(b) Minimise over $t>0$ and conclude $\Pr(X-\mu\ge a)\le\sigma^{2}/(\sigma^{2}+a^{2})$.
(c) Evaluate both Cantelli's bound and the two-sided Chebyshev bound for $a=2\sigma$, and comment.

## Challenge

**32.** *(§5.4, St Petersburg)* A game pays $2^{k}$ with probability $2^{-k-1}$, for $k=0,1,2,\dots$

(a) Show that the payoffs have total probability $1$.
(b) Show that $\mathbb{E}[X]=+\infty$, and check that this is not a case of an undefined mean.
(c) Show that the capped payoff $X_m=\min(X,2^{m})$ has $\mathbb{E}[X_m]=(m+2)/2$.
(d) A casino charges $\mathbb{E}[X_m]$ to play the capped game. Discuss why "the mean is infinite, so any
finite fee is favourable" is not a valid decision rule.

**33.** *(§7.7, challenge)* Let $f(x)=\frac{1}{x\sqrt{2\pi}}e^{-(\ln x)^{2}/2}$ for $x>0$ be the
lognormal density, and put $g(x)=f(x)\bigl(1+\sin(2\pi\ln x)\bigr)$.

(a) Show $g\ge0$ and $\int_0^\infty g=1$.
(b) Show $\int_0^\infty x^{k}g(x)\,dx=\int_0^\infty x^{k}f(x)\,dx$ for every integer $k\ge0$.
(c) Conclude that two different distributions can have identical moments, and explain why this does not
contradict Theorem 7.27.

**34.** *(§5.4)* Let $X$ have the standard Cauchy density $f(x)=\frac{1}{\pi(1+x^{2})}$.

(a) Verify that $f$ is a density.
(b) Show $\mathbb{E}\lvert X\rvert=\infty$.
(c) Show that $\lim_{M\to\infty}\mathbb{E}[X\mathbf{1}_{\lvert X\rvert\le M}]=0$ for this symmetric law,
and explain why that limit is *not* the expectation. (It is the Cauchy principal value.)
(d) Explain what part of the proof of the weak law of large numbers fails for Cauchy variables.

**35.** *(§7.5)* Let $X,Y\in L^{2}$.

(a) Prove that equality holds in Cauchy–Schwarz if and only if $X$ and $Y$ are linearly dependent almost
surely: there are constants $\alpha,\beta$, not both zero, with $\alpha X+\beta Y=0$ a.s.
(b) Deduce that, when $\sigma_X>0$ and $\sigma_Y>0$, $\rho(X,Y)=1$ forces $Y=aX+b$ a.s. with $a>0$, and
$\rho(X,Y)=-1$ forces $a<0$.
(c) Give an example with $\rho=1$ in which $Y\ne X$, to show that correlation one is not equality.

**36.** *(§7.6)* Prove Theorem 7.25: for $X\in L^{2}$ and any function $g$ with
$\mathbb{E}[g(Y)^{2}]<\infty$,

$$\mathbb{E}\bigl[(X-g(Y))^{2}\bigr]=\mathbb{E}\bigl[\operatorname{Var}(X\mid Y)\bigr]+\mathbb{E}\bigl[(\mathbb{E}[X\mid Y]-g(Y))^{2}\bigr],$$

and conclude that $\mathbb{E}[X\mid Y]$ is the best predictor of $X$ from $Y$ in mean square. State the
minimum value.
