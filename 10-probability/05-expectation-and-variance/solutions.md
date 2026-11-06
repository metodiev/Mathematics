# Expectation and Variance — Solutions

> [Expectation and Variance](README.md) · Solutions to the 36 problems in [exercises.md](exercises.md)

Each solution states the strategy, carries out every significant step, and ends with an independent
check. Proofs are complete. Pitfalls are flagged where a problem is designed to expose one.

## Beginner

**1.** *(Strategy: apply Definitions 5.6 and 5.11 directly; the last part compares two routes.)*

(a) By Definition 5.6,

$$\mathbb{E}[X]=(-1)(0.2)+0(0.5)+2(0.3)=-0.2+0+0.6=0.4,$$

$$\mathbb{E}[X^{2}]=(1)(0.2)+0(0.5)+4(0.3)=0.2+0+1.2=1.4.$$

(b) By Theorem 7.11, $\operatorname{Var}(X)=1.4-(0.4)^{2}=1.4-0.16=1.24$, so
$\sigma_X=\sqrt{1.24}\approx1.1136$.

(c) From the definition, $2X+3$ takes the values $2(-1)+3=1$, $2(0)+3=3$ and $2(2)+3=7$ with the same
probabilities, so $\mathbb{E}[2X+3]=1(0.2)+3(0.5)+7(0.3)=0.2+1.5+2.1=3.8$. By linearity,
$2(0.4)+3=3.8$.

*Check:* the two routes agree, and $\operatorname{Var}(2X+3)=4(1.24)=4.96$ by Theorem 7.12; directly the
values $\lbrace1,3,7\rbrace$ have mean $3.8$ and variance
$0.2(1-3.8)^{2}+0.5(3-3.8)^{2}+0.3(7-3.8)^{2}=0.2(7.84)+0.5(0.64)+0.3(10.24)=1.568+0.32+3.072=4.96$. ✓

**2.** *(Strategy: Markov needs non-negativity, Chebyshev needs the variance; both are universal.)*

(a) $X\ge0$ and $a=10$, so $\Pr(X\ge10)\le\mathbb{E}[X]/10=4/10=0.4$.

(b) With $\mu=4$, $\sigma^{2}=1$ and $a=3$: $\Pr(\lvert X-4\rvert\ge3)\le1/9\approx0.1111$.

(c) Both bounds are attained in the worst case. For (a), the variable with $\Pr(X=10)=0.4$ and
$\Pr(X=0)=0.6$ has mean $0.4\cdot10=4$ and gives $\Pr(X\ge10)=0.4$ exactly, so no argument using the mean
alone can produce a smaller number. That variable has variance $24$, not $1$, so it does not show that (b)
is optimal for the given pair of moments; with the variance available one can do better than (a), for
instance Cantelli's one-sided bound $\sigma^{2}/(\sigma^{2}+a^{2})=1/(1+36)=1/37\approx0.027$ with
$a=6$ (Exercise 31). The moral is that each bound uses exactly the moments it is given.

*Check:* both bounds are probabilities in $[0,1]$, and $0.4\le1$, $0.1111\le1$. Note also that Markov's
bound exceeds Chebyshev's here, as expected: the variance information is genuinely extra.

**3.** *(Strategy: uniform law on six points; then the scaling rule.)*

(a) $\mathbb{E}[X]=21/6=3.5$ and, by LOTUS, $\mathbb{E}[X^{2}]=(1+4+9+16+25+36)/6=91/6$. Hence
$\operatorname{Var}(X)=91/6-49/4=(182-147)/12=35/12\approx2.9167$.

(b) $\mathbb{E}[2X-1]=2(3.5)-1=6$ and, by Theorem 7.12, $\operatorname{Var}(2X-1)=4\cdot35/12=35/3\approx11.6667$.

*Check:* adding a constant and doubling cannot change the shape; the standard deviation doubles from
$\sqrt{35/12}\approx1.7078$ to $\approx3.4157$, and indeed $\sqrt{35/3}=2\sqrt{35/12}$. ✓

**4.** *(Strategy: a density is $1/(b-a)$; integrate $x$ and $x^{2}$.)*

(a) $f(x)=1/6$ on $[2,8]$ and $0$ elsewhere. Then
$\mathbb{E}[X]=\int_2^8\frac{x}{6}dx=\frac{1}{6}\cdot\frac{64-4}{2}=\frac{60}{12}=5$.

(b) $\mathbb{E}[X^{2}]=\int_2^8\frac{x^{2}}{6}dx=\frac{1}{6}\cdot\frac{512-8}{3}=\frac{504}{18}=28$, so
$\operatorname{Var}(X)=28-25=3$.

(c) $(b-a)^{2}/12=36/12=3$, in agreement.

*Check:* the mean is the midpoint $(2+8)/2=5$, as symmetry requires; the variance lies below
$(b-a)^{2}/4=9$, which holds because the uniform law does not put all mass at the endpoints.

**5.** *(Strategy: Definition 5.7 for moments, LOTUS for functions, and the MGF to see finiteness.)*

(a) From the catalogue in §7.7, $\mathbb{E}[X]=1/\lambda=0.5$. With $\lambda=2$,
$\mathbb{E}[X^{3}]=3!/\lambda^{3}=6/8=0.75$ (the general formula follows by repeated integration by
parts: each integration lowers the power of $x$ and contributes a factor $1/\lambda$).

(b) By LOTUS,
$\mathbb{E}[e^{X}]=\int_0^\infty e^{x}\,2e^{-2x}dx=2\int_0^\infty e^{-x}dx=2$. This is $M_X(1)$ and it is
finite because $1<\lambda=2$; the MGF of the exponential is $\lambda/(\lambda-t)$ for $t<\lambda$.

(c) $M_X(2)=\lambda/(\lambda-2)=2/0$, which diverges: the integral
$\int_0^\infty e^{2x}\cdot2e^{-2x}dx=\int_0^\infty2\,dx=\infty$. The MGF is finite only on $t<\lambda$,
so at the endpoint the expectation is infinite.

*Check:* $2$ is a plausible value, since $e^{X}$ is close to $e^{0.5}\approx1.649$ in the bulk of the
distribution and the integrand decays like $e^{-x}$. Also $\mathbb{E}[e^{X}]>e^{\mathbb{E}X}$ by Jensen
with the convex exponential: $2>e^{0.5}=1.6487$. ✓

**6.** *(Strategy: Theorem 7.14 twice, then Definition 5.13.)*

(a) $\operatorname{Var}(X+Y)=4+9+2(4)=21$ and $\operatorname{Var}(X-Y)=4+9-2(4)=5$.

(b) $\sigma_X=2$, $\sigma_Y=3$, so $\rho=4/(2\cdot3)=2/3\approx0.6667$.

(c) $21+5=26$ and $2(4)+2(9)=26$. ✓

*Check:* $\rho\in[-1,1]$; $\operatorname{Var}(X-Y)$ is smaller than $\operatorname{Var}(X+Y)$ because the
positive covariance makes the variables reinforce in one case and cancel in the other; and
$5\ge0$ is consistent with Cauchy–Schwarz, $4\le2\cdot3$.

**7.** *(Strategy: a two-point symmetric law; then Theorem 7.13.)*

(a) $\mathbb{E}[X]=\tfrac12-\tfrac12=0$ and $\mathbb{E}[X^{2}]=1$, so $\operatorname{Var}(X)=1$.

(b) $Y=X^{2}=1$ for both outcomes, so $Y$ is constant and $\operatorname{Var}(Y)=0$.

(c) Theorem 7.13: variance zero if and only if the variable is almost surely constant, which $Y$ is.

*Check:* direct computation for (b): $\mathbb{E}[Y]=1$, $\mathbb{E}[Y^{2}]=1$, so
$\operatorname{Var}(Y)=1-1=0$. ✓ Note that $\operatorname{Cov}(X,Y)=\mathbb{E}[X^{3}]-\mathbb{E}[X]\mathbb{E}[Y]=0$,
although $Y$ is a function of $X$ (Exercise 16).

**8.** *(Strategy: indicators, avoiding any hypergeometric computation.)*

Let $A_i$ be the event that the $i$-th draw is red, $i=1,\dots,5$. By symmetry among positions,
$\Pr(A_i)=3/10$ for every $i$ — the marginal law of draw $i$ is that of a uniformly random ball. Hence

$$\mathbb{E}[X]=\sum_{i=1}^{5}\Pr(A_i)=5\cdot\frac{3}{10}=1.5.$$

*Check:* the answer is $nK/N=5\cdot3/10=1.5$ and lies between $0$ and $\min(3,5)=3$; with replacement the
mean would be the same, while the variance differs. A second check: by exchangeability, the expected
number of reds among the first five equals $\mathbb{E}[\text{red in draw }1]\cdot5$. ✓

**9.** *(Strategy: Theorem 7.17 in the form $\mathbb{E}[(X-c)^{2}]=\operatorname{Var}(X)+(\mu-c)^{2}$.)*

With $\mu=10$ and $\operatorname{Var}(X)=4$:

* $c=10$: $\mathbb{E}[(X-10)^{2}]=4+0=4$;
* $c=12$: $4+(10-12)^{2}=4+4=8$;
* $c=0$: $4+100=104$.

The optimal constant is $c=\mu=10$, the unique minimiser by Theorem 7.17.

*Check:* the values increase as $c$ moves away from the mean, and $\mathbb{E}[(X-10)^{2}]$ is exactly
$\operatorname{Var}(X)$ by definition. If $X$ had been concentrated at $10$, all three values would have
been $0$, $4$ and $100$.

**10.** *(Strategy: Definition 5.18, with the change of base $\log_2x=\ln x/\ln2$.)*

(a) $H=-\sum_{j=1}^{8}\frac18\log_2\frac18=8\cdot\frac18\cdot3=3$ bits. In nats,
$H=3\ln2=3(0.693147)=2.0794$ nats.

(b) Here

$$H=-\tfrac12\log_2\tfrac12-\tfrac14\log_2\tfrac14-\tfrac18\log_2\tfrac18-\tfrac18\log_2\tfrac18=\tfrac12+\tfrac12+\tfrac38+\tfrac38=1.75,$$

so $H=1.75$ bits, i.e. $1.75\ln2=1.2130$ nats.

*Check:* both are below the maximum $\log_2n$ for their supports — $3$ bits for $n=8$, and
$\log_24=2$ bits for (b) — consistent with Theorem 7.34. Also (b) is a uniform distribution "stretched"
to non-uniform masses, so it must carry less than the $2$ bits of the uniform law on four points. ✓

**11.** *(Strategy: recognise the Poisson MGF, then read the parameter.)*

(a) $M(t)=\exp\bigl(\lambda(e^{t}-1)\bigr)$ with $\lambda=3$, so $X\sim\operatorname{Pois}(3)$ by the
catalogue and Theorem 7.27.

(b) For a Poisson variable, $\mathbb{E}[X]=\lambda=3$ and $\operatorname{Var}(X)=\lambda=3$. Both agree
with $M'(0)=3$ and $M''(0)=3+9=12$, since $\operatorname{Var}=12-9=3$.

(c) $\Pr(X=2)=e^{-3}3^{2}/2!=4.5e^{-3}=4.5(0.0497871)=0.224042$.

*Check:* the masses sum to $1$ in principle; $\Pr(X=0)=e^{-3}=0.0498$ and $\Pr(X=1)=0.1494$, so the three
lowest values account for about $0.423$ of the mass, leaving $0.577$ above $2$ — plausible for a Poisson
variable with $\lambda=3$.

## Intermediate

**12.** *(Strategy: Chebyshev is two-sided and needs only the variance; compare with the exact tail.)*

(a) $\mathbb{E}[X]=np=50$ and $\operatorname{Var}(X)=np(1-p)=25$, so with $a=20$,
$\Pr(\lvert X-50\rvert\ge20)\le25/400=0.0625$.

(b) The exact value is $2\Pr(X\le30)$. Since $\sigma=5$ and $20=4\sigma$, this is a $4\sigma$ tail:

$$\Pr(\lvert X-50\rvert\ge20)=2\sum_{k=0}^{30}\binom{100}{k}2^{-100}=7.85\times10^{-5}.$$

The bound exceeds the truth by a factor of about $796$.

(c) For the one-sided event $\{X\ge70\}$ Markov applied to $X$ gives $50/70=0.714$, which is useless.
Chebyshev, equivalently Markov applied to $(X-50)^{2}$ with threshold $400$, gives $0.0625$, far better,
because the variance captures the concentration around the mean. A one-sided refinement (Exercise 31)
gives $\sigma^{2}/(\sigma^{2}+a^{2})=25/425=0.0588$, slightly better still.

*Check:* the exact probability is far smaller than any moment bound, as it must be for a $4\sigma$
threshold in a light-tailed law; and Chebyshev's bound is below $1$, so it is informative, unlike the
Markov bound on $X$ itself.

**13.** *(Strategy: the formulas of §7.2 and §7.4, then a sanity comparison.)*

(a) $\mathbb{E}[X]=5\cdot\frac{3}{10}=1.5$ and

$$\operatorname{Var}(X)=5\cdot\frac{3}{10}\cdot\frac{7}{10}\cdot\frac{10-5}{10-1}=5(0.21)\frac{5}{9}=1.05\cdot0.5556=0.5833.$$

(b) With replacement the count is $\operatorname{Bin}(5,0.3)$, whose variance is $5(0.3)(0.7)=1.05$. The
finite-population factor $(N-n)/(N-1)=5/9<1$ shrinks it, because drawing without replacement removes
red balls as they are drawn, which limits how far the count can stray from its mean: the count cannot
exceed $3$, whereas a binomial count could reach $5$.

*Check:* $0.5833<1.05$ and both are below the maximum possible variance of a variable on
$\{0,\dots,5\}$, which is $6.25$. Also $\operatorname{Var}(X)\to1.05$ as $N\to\infty$ with $K/N=0.3$ fixed,
since $(N-n)/(N-1)\to1$. ✓

**14.** *(Strategy: indicator variables on both parts; no distribution needed.)*

(a) With six coupons, $\mathbb{E}[T]=6H_6=6\bigl(1+\tfrac12+\tfrac13+\tfrac14+\tfrac15+\tfrac16\bigr)=6(2.45)=14.7$.

(b) Let $A_j$ be the event that type $j$ appears among the six draws. Then
$\Pr(A_j)=1-\bigl(\tfrac56\bigr)^{6}=1-0.334898=0.665102$, so the expected number of distinct types is
$6(0.665102)=3.99061$.

(c) In both parts the unknown quantity is written as a sum of indicators — $T=\sum_{j=0}^{5}G_j$ in (a),
$D=\sum_j\mathbf{1}_{A_j}$ in (b) — and linearity computes the mean from the marginal probabilities
alone. The $G_j$ are dependent in (a) only through the past, and the $A_j$ are certainly dependent in
(b) (six types cannot occupy fewer than one draw each), but linearity never asks for a joint law.

*Check:* (b)'s answer is below the maximum $6$ and above $6\cdot\frac{5}{6}$-type heuristics; with one
draw it would be $1$, with many draws it tends to $6$. And $14.7$ lies between $6$ (a lower bound, since
all six are needed) and the crude bound $6\cdot6=36$.

**15.** *(Strategy: LOTUS evaluates $\mathbb{E}[g(X)]$ by averaging over the four equally likely values.)*

(a) $(-1)^{X}$ equals $+1$ for $X=2,4$ and $-1$ for $X=1,3$, so the mean is
$\tfrac14(1-1-1+1)=0$.

(b) The values of $\lvert X-2.5\rvert$ are $1.5,0.5,0.5,1.5$, so
$\mathbb{E}\lvert X-2.5\rvert=\tfrac14(1.5+0.5+0.5+1.5)=1$.

(c) $\min(X,3)$ takes the values $1,2,3,3$, so the mean is $\tfrac14(1+2+3+3)=2.25$.

*Check:* (a) is a symmetry statement, since the distribution of $X$ is not symmetric about $2.5$ yet the
alternating signs cancel exactly. For (c), $\min(X,3)\le X$ pointwise, so its mean must not exceed
$\mathbb{E}[X]=2.5$; indeed $2.25<2.5$. For (b), $\mathbb{E}\lvert X-2.5\rvert\ge\lvert\mathbb{E}X-2.5\rvert=0$
by Jensen with the convex absolute value, and $1\ge0$. ✓

**16.** *(Strategy: compute the covariance with the product rule, then exhibit a failed factorisation.)*

(a) $\mathbb{E}[X]=0$ and $\mathbb{E}[X^{3}]=\tfrac13(-1+0+1)=0$, so
$\operatorname{Cov}(X,Y)=\mathbb{E}[X^{3}]-\mathbb{E}[X]\mathbb{E}[X^{2}]=0$.

(b) $\Pr(Y=1\mid X=0)=\Pr(X=0,Y=1)/\Pr(X=0)=0/(1/3)=0$, whereas
$\Pr(Y=1)=\Pr(X=\pm1)=\tfrac23$. Since $0\ne\tfrac23$, the variables are not independent (indeed $Y$ is a
function of $X$).

(c) It disproves the implication "uncorrelated implies independent". It does **not** disprove the valid
implication "independent implies uncorrelated" (Theorem 7.16), nor the inequality $\lvert\rho\rvert\le1$.

*Check:* the covariance is exactly zero because $\mathbb{E}[X^{3}]=\mathbb{E}[X]=0$ by symmetry, and the
dependence is total: knowing $X$ determines $Y$ exactly. This is the standard example behind Mistake 6
of §11.

**17.** *(Strategy: Theorems 7.28 and 7.29, plus $\mathcal{N}(\mu,\sigma^{2})$ has MGF
$\exp(\mu t+\tfrac12\sigma^{2}t^{2})$.)*

(a) $M_X(t)=\exp\bigl(t+2t^{2}\bigr)$ and $M_Y(t)=\exp\bigl(2t+\tfrac92t^{2}\bigr)$.

(b) By Theorem 7.28, $M_{2X}(t)=M_X(2t)=\exp(2t+8t^{2})$ and $M_{-Y}(t)=M_Y(-t)=\exp(-2t+\tfrac92t^{2})$.
Independence permits Theorem 7.29, so

$$M_{2X-Y}(t)=\exp(2t+8t^{2})\exp\bigl(-2t+\tfrac92t^{2}\bigr)=\exp\bigl(\tfrac{25}{2}t^{2}\bigr),$$

which is the MGF of $\mathcal{N}(0,25)$. By Theorem 7.27, $2X-Y\sim\mathcal{N}(0,25)$. The mean is
$2(1)-2=0$ and the variance $4(4)+9=25$, matching the exponent.

(c) $\mathbb{E}[e^{X}]=M_X(1)=\exp(1+2)=e^{3}\approx20.0855$.

*Check:* the variance computation uses $\operatorname{Var}(2X-Y)=4\operatorname{Var}(X)+\operatorname{Var}(Y)$,
valid because of independence; the MGF computation reproduces it, which is the check. And
$\mathbb{E}[e^{X}]>e^{\mathbb{E}X}=e$, as Jensen requires for the convex exponential.

**18.** *(Strategy: moments of the uniform law, then the definition of correlation.)*

$\mathbb{E}[U]=\tfrac12$, $\mathbb{E}[U^{2}]=\tfrac13$, $\mathbb{E}[U^{3}]=\tfrac14$ and
$\mathbb{E}[U^{4}]=\tfrac15$. Hence

$$\operatorname{Cov}(U,U^{2})=\tfrac14-\tfrac12\cdot\tfrac13=\tfrac14-\tfrac16=\tfrac1{12},$$

$$\operatorname{Var}(U)=\tfrac13-\tfrac14=\tfrac1{12},\qquad \operatorname{Var}(U^{2})=\tfrac15-\tfrac19=\tfrac{4}{45},$$

$$\rho=\frac{1/12}{\sqrt{(1/12)(4/45)}}=\frac{1/12}{\sqrt{4/540}}=\frac{\sqrt{540}}{24}=\frac{6\sqrt{15}}{24}=\frac{\sqrt{15}}{4}\approx0.9682.$$

*Check:* $\rho<1$ strictly, as it must be since $U^{2}$ is not affine in $U$ (Theorem 7.20). The value is
large and positive because $U^{2}$ is increasing on $[0,1]$; $\rho^{2}=15/16=0.9375$, so a linear fit
explains about $94\%$ of the variance of $U^{2}$. Note the covariance $1/12$ happens to equal
$\operatorname{Var}(U)$.

**19.** *(Strategy: condition on each value of $Y$ using
$p_{X\mid Y}(x\mid y)=p(x,y)/p_Y(y)$.)*

(a) Marginals: $\Pr(Y=0)=0.2+0.3=0.5$ and $\Pr(Y=1)=0.1+0.4=0.5$. Therefore

$$\mathbb{E}[X\mid Y=0]=\frac{0(0.2)+1(0.3)}{0.5}=0.6,\qquad \mathbb{E}[X\mid Y=1]=\frac{0(0.1)+1(0.4)}{0.5}=0.8.$$

(b) $\Pr(X=1)=0.3+0.4=0.7$, so $\mathbb{E}[X]=0.7$. And
$\mathbb{E}\bigl[\mathbb{E}[X\mid Y]\bigr]=0.5(0.6)+0.5(0.8)=0.3+0.4=0.7$. ✓

(c) $\operatorname{Var}(X)=0.7(0.3)=0.21$ (an indicator). Within groups:
$\operatorname{Var}(X\mid Y=0)=0.6(0.4)=0.24$ and $\operatorname{Var}(X\mid Y=1)=0.8(0.2)=0.16$, so
$\mathbb{E}[\operatorname{Var}(X\mid Y)]=0.5(0.24)+0.5(0.16)=0.20$. Between groups:
$\operatorname{Var}(\mathbb{E}[X\mid Y])=\operatorname{Var}(0.6,0.8\text{ with prob }\tfrac12)=\tfrac14(0.04)+\tfrac14(0.04)=0.01$.
Sum: $0.20+0.01=0.21$. ✓

*Check:* all three routes agree, and the between-group term is small, meaning $Y$ carries little
information about $X$ — consistent with the small correlation computed in Example 9.5 of a related table.

**20.** *(Strategy: direct moments, then the two named inequalities.)*

(a) $\mathbb{E}[X]=\tfrac12(1+9)=5$, $\mathbb{E}[X^{2}]=\tfrac12(1+81)=41$ and $(\mathbb{E}X)^{2}=25$. Since
$41\ge25$, Jensen's inequality holds for the convex $\varphi(x)=x^{2}$, and
$\operatorname{Var}(X)=41-25=16$.

(b) $\sqrt{1\cdot9}=3\le5=\tfrac{1+9}{2}$.

(c) Because $\varphi(x)=\ln x$ is concave, Jensen gives $\mathbb{E}[\ln X]\le\ln\mathbb{E}[X]$, i.e.
$\exp(\mathbb{E}\ln X)\le\mathbb{E}X$: the geometric mean is at most the arithmetic mean. Equivalently,
$-\ln$ is convex and $-\ln\mathbb{E}X\le\mathbb{E}[-\ln X]$.

*Check:* for (a), $16>0$ as it must be; for (b), equality in AM–GM holds exactly when the numbers agree,
and here they do not ($1\ne9$), so the inequality is strict. $\mathbb{E}[\ln X]=\tfrac12\ln9=\ln3=1.0986$
and $\ln5=1.6094$, so indeed $1.0986<1.6094$.

**21.** *(Strategy: condition on $N$, then use the tower property and the law of total variance.)*

(a) $\mathbb{E}[S_N\mid N=n]=\sum_{i=1}^n1=n$, so $\mathbb{E}[S_N\mid N]=N$ and, by Theorem 7.21,
$\mathbb{E}[S_N]=\mathbb{E}[N]=5.5$.

(b) For fixed $n$, independence of the $X_i$ gives $\operatorname{Var}(S_N\mid N=n)=n$. Also
$\operatorname{Var}(N)=\frac{10^{2}-1}{12}=8.25$ and $\mathbb{E}[N]=5.5$. Hence

$$\operatorname{Var}(S_N)=\mathbb{E}[\operatorname{Var}(S_N\mid N)]+\operatorname{Var}(\mathbb{E}[S_N\mid N])=5.5+8.25=13.75.$$

(c) Within each block, independence of $X_1,\dots,X_n$ and of $N$ is used to write
$\operatorname{Var}(S_N\mid N=n)=n$ and to write the conditional mean as $n$. For the tower property and
the law of total variance nothing beyond integrability is needed.

*Check:* $13.75>5.5$, and it would equal $\mathbb{E}[N]\operatorname{Var}(X)$ if $N$ were deterministic.
The extra $8.25$ is the contribution of the randomness in the number of terms, exactly the between-group
term.

**22.** *(Strategy: solve the bound as an equation, then construct the extremal law.)*

(a) $1/k^{2}=0.01$ gives $k^{2}=100$, so $k=10$.

(b) At $k=1$ the bound is $1$, which asserts only that a probability is at most $1$; it carries no
information. Chebyshev only becomes useful for $k$ of moderate size, and it decays slowly — quadratically
in $1/k$.

(c) Take $\Pr(X=\mu+k\sigma)=\Pr(X=\mu-k\sigma)=\dfrac{1}{2k^{2}}$ and
$\Pr(X=\mu)=1-\dfrac{1}{k^{2}}$. Its mean is $\mu$ by symmetry and its variance is
$2\cdot\dfrac{1}{2k^{2}}\cdot k^{2}\sigma^{2}=\sigma^{2}$; the deviation is at least $k\sigma$ exactly on
the two outer points, giving probability $1/k^{2}$. At $k=2$: mass $\tfrac18$ at each of $\mu\pm2\sigma$
and $\tfrac34$ at $\mu$.

*Check:* the masses sum to $1$ for $k>1$, and the variance is $\sigma^{2}$ as computed. For $k=2$ the
bound $1/4$ is attained, which shows the inequality cannot be improved.

**23.** *(Strategy: product of MGFs, then the moment formulas.)*

(a) $M_{X+Y}(t)=\exp\bigl(2(e^{t}-1)\bigr)\exp\bigl(3(e^{t}-1)\bigr)=\exp\bigl(5(e^{t}-1)\bigr)$, the MGF of
$\operatorname{Pois}(5)$; by Theorem 7.27, $X+Y\sim\operatorname{Pois}(5)$.

(b) $\Pr(X+Y=0)=e^{-5}=0.006738$, and $\mathbb{E}[(X+Y)^{2}]=\operatorname{Var}+\bigl(\mathbb{E}\bigr)^{2}=5+25=30$.

(c) By bilinearity (Theorem 7.18) and independence,
$\operatorname{Cov}(X,X+Y)=\operatorname{Var}(X)+\operatorname{Cov}(X,Y)=2+0=2$.

*Check:* $\mathbb{E}[X+Y]=5$; direct computation of $\mathbb{E}[XY]=\mathbb{E}[X]\mathbb{E}[Y]=6$ gives
$\operatorname{Cov}(X,X+Y)=\mathbb{E}[X^{2}+XY]-\mathbb{E}[X]\mathbb{E}[X+Y]=(2+4)+6-2\cdot5=2$. ✓

## Advanced

**24.** *(Strategy: the pointwise bound $\lvert x\rvert\le1+x^{2}$ turns a second-moment hypothesis into a
first-moment one; a power-law density shows the converse fails.)*

(a) For every real $x$: if $\lvert x\rvert\le1$ then $\lvert x\rvert\le1\le1+x^{2}$; if $\lvert x\rvert>1$
then $\lvert x\rvert<x^{2}<1+x^{2}$. So $\lvert x\rvert\le1+x^{2}$ always. Taking expectations and using
monotonicity and linearity,

$$\mathbb{E}\lvert X\rvert\le1+\mathbb{E}[X^{2}]<\infty.$$

(b) Let $f(x)=2x^{-3}$ for $x\ge1$ and $f(x)=0$ otherwise. It is a density because

$$\int_1^\infty 2x^{-3}dx=\Bigl[-x^{-2}\Bigr]_1^\infty=1.$$

Its mean is finite:

$$\mathbb{E}[X]=\int_1^\infty x\cdot2x^{-3}dx=2\int_1^\infty x^{-2}dx=2\Bigl[-x^{-1}\Bigr]_1^\infty=2,$$

but its second moment diverges:

$$\mathbb{E}[X^{2}]=\int_1^\infty x^{2}\cdot2x^{-3}dx=2\int_1^\infty\frac{dx}{x}=\infty.$$

(c) Finite mean is a strictly weaker requirement than finite variance; (b) exhibits the gap. More
generally $f(x)\propto x^{-(1+\alpha)}$ on $[1,\infty)$ has $\mathbb{E}[X]<\infty$ exactly when $\alpha>1$
and $\mathbb{E}[X^{2}]<\infty$ exactly when $\alpha>2$, so every $\alpha\in(1,2]$ gives finite mean and
infinite second moment. No hypothesis on $\mathbb{E}\lvert X\rvert$ alone can bound $\mathbb{E}[X^{2}]$.

*Check:* $\mathbb{E}[X]=2$ and $\Pr(X\ge t)=t^{-2}$ for $t\ge1$, so by the tail formula
$\mathbb{E}[X]=\int_0^1 1\,dt+\int_1^\infty t^{-2}dt=1+1=2$, in agreement.

**25.** *(Strategy: interchange two non-negative sums — the discrete layer-cake identity.)*

(a) Write $\Pr(X\ge k)=\sum_{j\ge k}p(j)$ and interchange:

$$\sum_{k\ge1}\Pr(X\ge k)=\sum_{k\ge1}\sum_{j\ge k}p(j)=\sum_{j\ge1}\sum_{k=1}^{j}p(j)=\sum_{j\ge1}j\,p(j)=\mathbb{E}[X].$$

The interchange is legitimate by Lemma 7.1 since every term is non-negative, and the identity holds also
when both sides are $+\infty$.

(b) Here $\Pr(T\ge k)=(1-p)^{k-1}$ (the first $k-1$ trials all fail), so

$$\mathbb{E}[T]=\sum_{k\ge1}(1-p)^{k-1}=\frac{1}{1-(1-p)}=\frac1p.$$

(c) Similarly,

$$\sum_{k\ge1}k\Pr(T\ge k)=\sum_{k\ge1}k(1-p)^{k-1}=\frac{1}{\bigl(1-(1-p)\bigr)^{2}}=\frac{1}{p^{2}},$$

using $\sum_{k\ge1}kx^{k-1}=(1-x)^{-2}$ for $\lvert x\rvert<1$. By the same interchange as in (a) with an
extra factor $k$,

$$\sum_{k\ge1}k\Pr(T\ge k)=\sum_{j\ge1}p(j)\sum_{k=1}^{j}k=\sum_{j\ge1}p(j)\frac{j(j+1)}{2}=\mathbb{E}\Bigl[\frac{T(T+1)}{2}\Bigr].$$

So the quantity computed is $\mathbb{E}\bigl[T(T+1)/2\bigr]=1/p^{2}$, not $\mathbb{E}[T^{2}]$.

*Check:* with $p=\tfrac12$, $\mathbb{E}[T]=2$ and $\mathbb{E}[T^{2}]=(2-p)/p^{2}=1.5/0.25=6$; the identity
gives $\mathbb{E}[T(T+1)/2]=(6+2)/2=4=1/p^{2}$. ✓

**26.** *(Strategy: apply Markov to the squared deviation, then exhibit the extremal law.)*

(a) $(X-\mu)^{2}$ is non-negative, so Markov (Theorem 7.30) with threshold $a^{2}>0$ gives

$$\Pr\bigl(\lvert X-\mu\rvert\ge a\bigr)=\Pr\bigl((X-\mu)^{2}\ge a^{2}\bigr)\le\frac{\mathbb{E}[(X-\mu)^{2}]}{a^{2}}=\frac{\sigma^{2}}{a^{2}}.$$

(b) For $k>1$ put $\Pr(X=\mu+k\sigma)=\Pr(X=\mu-k\sigma)=\dfrac{1}{2k^{2}}$ and
$\Pr(X=\mu)=1-\dfrac{1}{k^{2}}$. The masses are non-negative and sum to $1$. By symmetry
$\mathbb{E}[X]=\mu$, and

$$\operatorname{Var}(X)=2\cdot\frac{1}{2k^{2}}\cdot(k\sigma)^{2}=\sigma^{2}.$$

The event $\lvert X-\mu\rvert\ge k\sigma$ occurs exactly at the two outer points, so its probability is
$1/k^{2}$, which equals the bound.

(c) Fix $k>1$. Any function $B(\mu,\sigma)$ that bounds $\Pr(\lvert X-\mu\rvert\ge k\sigma)$ for every
variable with mean $\mu$ and variance $\sigma^{2}$ must satisfy
$B(\mu,\sigma)\ge1/k^{2}$, because the law in (b) is admissible and attains $1/k^{2}$. Hence no bound
using only the two moments can be uniformly smaller, and Chebyshev's inequality is optimal in that class.

*Check:* for $k=2$ the masses are $\tfrac18,\tfrac34,\tfrac18$, the variance is
$2\cdot\tfrac18\cdot4\sigma^{2}=\sigma^{2}$, and the tail probability is $\tfrac14=1/4$. ✓

**27.** *(Strategy: the discriminant argument, then specialisation.)*

(a) For every $t\in\mathbb{R}$, $0\le\mathbb{E}[(X+tY)^{2}]=\mathbb{E}[X^{2}]+2t\mathbb{E}[XY]+t^{2}\mathbb{E}[Y^{2}]$.
If $\mathbb{E}[Y^{2}]=0$ then $Y=0$ a.s. by Theorem 7.13 and both sides of the claimed inequality are $0$.
Otherwise the quadratic is non-negative for all $t$, so its discriminant
$4(\mathbb{E}[XY])^{2}-4\mathbb{E}[X^{2}]\mathbb{E}[Y^{2}]$ is at most $0$, which is the claim.

(b) Apply (a) to the non-negative variables $\lvert X\rvert$ and $\lvert Y\rvert$: their second moments
are $\mathbb{E}[X^{2}]$ and $\mathbb{E}[Y^{2}]$, and $\mathbb{E}[\lvert X\rvert\lvert Y\rvert]=\mathbb{E}\lvert XY\rvert$.
Hence $\bigl(\mathbb{E}\lvert XY\rvert\bigr)^{2}\le\mathbb{E}[X^{2}]\mathbb{E}[Y^{2}]$, and taking square
roots gives the result.

(c) Take $Y\equiv1$, which is in $L^{2}$: $\bigl(\mathbb{E}\lvert X\rvert\bigr)^{2}\le\mathbb{E}[X^{2}]\cdot1$,
so $\mathbb{E}\lvert X\rvert\le\sqrt{\mathbb{E}[X^{2}]}$. Equality in (a) requires $X=-t_0Y=-t_0$ a.s.,
i.e. $\lvert X\rvert$ constant almost surely.

*Check:* for $X$ uniform on $\{-1,1\}$, $\mathbb{E}\lvert X\rvert=1=\sqrt{\mathbb{E}[X^{2}]}$, and indeed
$\lvert X\rvert$ is constant. For $X$ uniform on $[0,1]$, $\mathbb{E}\lvert X\rvert=\tfrac12$ and
$\sqrt{\mathbb{E}[X^{2}]}=1/\sqrt3\approx0.577$, a strict inequality as $\lvert X\rvert$ is not constant.

**28.** *(Strategy: sum over the finer variable first; then discuss the information condition.)*

(a) Fix $y$ with $\Pr(Y=y)>0$ and abbreviate $q(z)=\Pr(Z=z\mid Y=y)$. Since the range is finite,

$$\mathbb{E}\bigl[\mathbb{E}[X\mid Y,Z]\bigm|Y=y\bigr]=\sum_z\mathbb{E}[X\mid Y=y,Z=z]\,q(z)=\sum_z\Bigl(\sum_x x\,\Pr(X=x\mid Y=y,Z=z)\Bigr)q(z).$$

Now $\Pr(X=x\mid Y=y,Z=z)q(z)=\Pr(X=x,Z=z\mid Y=y)$ by the multiplication rule for conditional
probabilities, so

$$=\sum_x x\sum_z\Pr(X=x,Z=z\mid Y=y)=\sum_x x\,\Pr(X=x\mid Y=y)=\mathbb{E}[X\mid Y=y],$$

because the events $\{Z=z\}$ partition the space given $\{Y=y\}$. As this holds for every $y$ with
positive mass, the random variables agree almost surely.

(b) The condition is used to know that $\{Y=y\}\in\sigma(Y,Z)$, i.e. that conditioning on $(Y,Z)$ retains
the information carried by $Y$. Without it, $\Pr(X=x\mid Y=y,Z=z)$ would not be defined as a conditional
probability given the finer information, and the tower property's hypothesis $\sigma(Y)\subseteq\sigma(Y,Z)$
would fail.

(c) $\mathbb{E}[X\mid Y]$ is determined by $Y$, hence by $(Y,Z)$: it is $\sigma(Y,Z)$-measurable and
integrable, so conditioning it on $\sigma(Y,Z)$ reproduces it,
$\mathbb{E}\bigl[\mathbb{E}[X\mid Y]\bigm|Y,Z\bigr]=\mathbb{E}[X\mid Y]$ a.s. This is Theorem 7.23 with
$X\equiv1$, or the general fact that $\mathbb{E}[Z\mid\mathcal{G}]=Z$ for $\mathcal{G}$-measurable
integrable $Z$.

*Check:* part (a) is the "smaller $\sigma$-algebra first" direction, (c) the "larger first" direction; both
give $\mathbb{E}[X\mid Y]$, which is why nested conditioning is often described as projection onto
successively coarser information.

**29.** *(Strategy: write the conditional variance with Theorem 7.11, then telescope.)*

Let $\mu=\mathbb{E}[X]$ and $Z=\mathbb{E}[X\mid Y]$. Since $\mathbb{E}[X^{2}]<\infty$, the conditional
expectation $\mathbb{E}[X^{2}\mid Y]$ is finite a.s. and $\mathbb{E}[\mathbb{E}[X^{2}\mid Y]]=\mathbb{E}[X^{2}]$
by Theorem 7.21. Applying Theorem 7.11 conditionally (legitimate: within each conditioning event $Y=y$ the
conditional law is a genuine probability law with a finite second moment),

$$\operatorname{Var}(X\mid Y)=\mathbb{E}[X^{2}\mid Y]-\bigl(\mathbb{E}[X\mid Y]\bigr)^{2}=\mathbb{E}[X^{2}\mid Y]-Z^{2}.$$

Taking expectations and using linearity and Theorem 7.21,

$$\mathbb{E}\bigl[\operatorname{Var}(X\mid Y)\bigr]=\mathbb{E}[X^{2}]-\mathbb{E}[Z^{2}].$$

On the other hand, $\mathbb{E}[Z]=\mathbb{E}\bigl[\mathbb{E}[X\mid Y]\bigr]=\mathbb{E}[X]=\mu$ by
Theorem 7.21, so Theorem 7.11 applied to $Z$ gives
$\operatorname{Var}(Z)=\mathbb{E}[Z^{2}]-\mu^{2}$. Adding,

$$\mathbb{E}\bigl[\operatorname{Var}(X\mid Y)\bigr]+\operatorname{Var}(Z)=\mathbb{E}[X^{2}]-\mu^{2}=\operatorname{Var}(X),$$

again by Theorem 7.11. $\blacksquare$

*Check:* both terms are non-negative and sum to $\operatorname{Var}(X)$; if $Y$ is independent of $X$ then
$Z=\mu$, the between-group term vanishes and $\mathbb{E}[\operatorname{Var}(X\mid Y)]=\operatorname{Var}(X)$,
which is consistent with the interpretation.

**30.** *(Strategy: factorise the exponential, then read MGFs.)*

(a) For fixed $t$ at which both MGFs are finite, $e^{tX}$ and $e^{tY}$ are integrable. Independence and
Theorem 7.16 give

$$M_{X+Y}(t)=\mathbb{E}\bigl[e^{t(X+Y)}\bigr]=\mathbb{E}\bigl[e^{tX}e^{tY}\bigr]=\mathbb{E}[e^{tX}]\mathbb{E}[e^{tY}]=M_X(t)M_Y(t).$$

(b) For $X\sim\operatorname{Bin}(m,p)$ and $Y\sim\operatorname{Bin}(n,p)$ independent,
$M_X(t)=(1-p+pe^{t})^{m}$ and $M_Y(t)=(1-p+pe^{t})^{n}$, so
$M_{X+Y}(t)=(1-p+pe^{t})^{m+n}$, the MGF of $\operatorname{Bin}(m+n,p)$. By Theorem 7.27 the laws agree.

(c) With different parameters the product is $(1-p_1+p_1e^{t})^{m}(1-p_2+p_2e^{t})^{n}$. As a polynomial
in $s=e^{t}$, a binomial MGF $(1-p+ps)^{m+n}$ has the single root $s=-(1-p)/p$ of multiplicity $m+n$,
whereas the product has the two distinct roots $-(1-p_1)/p_1$ and $-(1-p_2)/p_2$ when $p_1\ne p_2$. Hence
the product is not a binomial MGF, and indeed the sum of binomials with different $p$ is not binomial:
the sum counts successes in trials with unequal probabilities.

*Check:* for $m=n=1$ with $p_1=p_2=p$, the sum is $\operatorname{Bin}(2,p)$, and
$(1-p+ps)^{2}$ expands to the correct MGF; with $p_1\ne p_2$, $\Pr(X+Y=0)=(1-p_1)(1-p_2)$, which no single
binomial with two trials and probability $p$ reproduces unless $p_1=p_2$.

**31.** *(Strategy: shift the variable so that Markov applies to a one-sided event, then optimise.)*

(a) Let $W=(X-\mu)+t$ with $t>0$. Then $\mathbb{E}[W^{2}]=\operatorname{Var}(X)+t^{2}=\sigma^{2}+t^{2}$,
because $\mathbb{E}[X-\mu]=0$ kills the cross term. Also
$\{X-\mu\ge a\}=\{W\ge a+t\}$ with $a+t>0$, so Markov gives

$$\Pr(X-\mu\ge a)\le\frac{\mathbb{E}[W^{2}]}{(a+t)^{2}}=\frac{\sigma^{2}+t^{2}}{(a+t)^{2}}.$$

(b) Differentiate $f(t)=(\sigma^{2}+t^{2})/(a+t)^{2}$:

$$f'(t)=\frac{2t(a+t)^{2}-2(a+t)(\sigma^{2}+t^{2})}{(a+t)^{4}}=\frac{2(ta-\sigma^{2})}{(a+t)^{3}},$$

so $f'(t)<0$ for $t<\sigma^{2}/a$ and $f'(t)>0$ afterwards: the minimum is at $t=\sigma^{2}/a>0$. Its value is

$$\frac{\sigma^{2}+\sigma^{4}/a^{2}}{\bigl(a+\sigma^{2}/a\bigr)^{2}}=\frac{\sigma^{2}(a^{2}+\sigma^{2})/a^{2}}{(a^{2}+\sigma^{2})^{2}/a^{2}}=\frac{\sigma^{2}}{\sigma^{2}+a^{2}}.$$

The same argument applied to $-X$ bounds the lower tail.

(c) For $a=2\sigma$: Cantelli gives $\sigma^{2}/(\sigma^{2}+4\sigma^{2})=1/5=0.2$, while two-sided
Chebyshev gives $1/4=0.25$. Cantelli is sharper because the event is one-sided and the shifted square
exploits that; the improvement is genuine, not an artefact.

*Check:* as $a\to0$, Cantelli's bound tends to $1$, and as $a\to\infty$ it decays like $\sigma^{2}/a^{2}$,
matching the Chebyshev rate. At $a=\sigma$ it gives $1/2$, whereas Chebyshev gives $1$; the one-sided
statement is dramatically stronger for small $a$.

## Challenge

**32.** *(Strategy: separate the well-definedness of $+\infty$ from undefinedness, then consider capped
payoffs and decision theory.)*

(a) $\sum_{k\ge0}2^{-k-1}=\tfrac12\sum_{k\ge0}2^{-k}=\tfrac12\cdot2=1$.

(b) Since $X\ge0$, Proposition 5.10 applies and the expectation exists in $[0,\infty]$. But

$$\mathbb{E}[X]=\sum_{k\ge0}2^{k}\cdot2^{-k-1}=\sum_{k\ge0}\tfrac12=+\infty.$$

This is *defined* as $+\infty$, not undefined: each term $2^k\cdot2^{-k-1}=\tfrac12$ is finite and the
partial sums diverge monotonically. An undefined mean would require the positive and negative parts both
to be infinite, which cannot happen for a non-negative variable.

(c) With $X_m=\min(X,2^{m})$,

$$\mathbb{E}[X_m]=\sum_{k=0}^{m-1}2^{k}\cdot2^{-k-1}+\sum_{k\ge m}2^{m}\cdot2^{-k-1}=\frac m2+2^{m}\cdot2^{-m}=\frac m2+1=\frac{m+2}{2}.$$

(d) The mean of the uncapped game is infinite, so "any finite fee is favourable in expectation" is
literally true and practically useless. Three reasons: the median payoff is $1$ (with probability
$\tfrac12$ the payoff is $1$), so with any fee above $1$ the player loses more often than not; a single
play has a heavy-tailed payoff whose typical values are small; and expected value is not preserved by
non-linear utility. The capped computation makes the dependence on the cap explicit: the fair fee for the
capped game grows like $\tfrac12\log_2(\text{cap})$, so it is the logarithm, not the payoff, that scales.
A decision rule based on expectation assumes risk neutrality and repeated play on the same terms, neither
of which holds.

*Check:* parts (c) and (b) are consistent: $\mathbb{E}[X_m]\uparrow\infty$ as $m\to\infty$ but only
logarithmically — $m=10$ gives a fair fee of $6$, while the payoff exceeds $10^6$ with probability about
$10^{-6}$.

**33.** *(Strategy: the sine factor is orthogonal to every polynomial in $x$ after the substitution
$x=e^{u}$, because it is the imaginary part of a Gaussian characteristic function at an integer multiple
of $2\pi$.)*

(a) Since $\sin\ge-1$, $g=f(1+\sin(2\pi\ln x))\ge0$. For the total mass, substitute $x=e^{u}$,
$dx=e^{u}du$; the lognormal density satisfies $f(e^{u})e^{u}=\frac{1}{\sqrt{2\pi}}e^{-u^{2}/2}$. Hence

$$\int_0^\infty f(x)\sin(2\pi\ln x)\,dx=\int_{-\infty}^{\infty}\frac{1}{\sqrt{2\pi}}e^{-u^{2}/2}\sin(2\pi u)\,du=\operatorname{Im}\Bigl[e^{-\frac{(2\pi)^{2}}{2}}\Bigr]=0,$$

because the characteristic function of $\mathcal{N}(0,1)$ at $2\pi$ is the real number $e^{-2\pi^{2}}$.
Therefore $\int g=\int f+0=1$, and $g$ is a density.

(b) For an integer $k\ge0$, again with $x=e^{u}$,

$$\int_0^\infty x^{k}f(x)\sin(2\pi\ln x)\,dx=\operatorname{Im}\int_{-\infty}^{\infty}\frac{1}{\sqrt{2\pi}}e^{-u^{2}/2}e^{ku}e^{2\pi iu}\,du=\operatorname{Im}\Bigl[e^{k^{2}/2}e^{2\pi ik}e^{-2\pi^{2}}\Bigr],$$

using the characteristic function of $\mathcal{N}(k,1)$ at $2\pi$. Since $k$ is an integer,
$e^{2\pi ik}=1$ and the bracket is real, so the imaginary part is zero. Hence
$\int x^{k}g=\int x^{k}f$ for every $k\ge0$, i.e. all moments agree.

(c) $g\ne f$, since $g(x)/f(x)=1+\sin(2\pi\ln x)$ is not identically $1$ (it equals $2$ when
$\ln x=\tfrac14$, i.e. $x=e^{1/4}$). So two distinct distributions have identical moments, and no
contradiction with Theorem 7.27 arises: that theorem assumes $M_X<\infty$ on an interval $(-\delta,\delta)$,
whereas the lognormal has $M(t)=\infty$ for every $t>0$, so its MGF is finite only at $t\le0$ and the
hypothesis fails.

*Check:* taking $k=0$ in (b) recovers (a); taking $k=1$ says the two laws have the same mean
$e^{1/2}\approx1.6487$, which is also the median of the lognormal — credible since the sine perturbation is
symmetric in $\ln x$ on average.

**34.** *(Strategy: test integrability with the definition, then separate the symmetric truncation from
the absolute integral.)*

(a) $f>0$ everywhere and

$$\int_{-\infty}^{\infty}\frac{dx}{\pi(1+x^{2})}=\frac{1}{\pi}\Bigl[\arctan x\Bigr]_{-\infty}^{\infty}=\frac{1}{\pi}\Bigl(\frac\pi2+\frac\pi2\Bigr)=1.$$

(b) By symmetry of the integrand,

$$\mathbb{E}\lvert X\rvert=\frac{2}{\pi}\int_0^\infty\frac{x}{1+x^{2}}dx=\frac{1}{\pi}\lim_{M\to\infty}\Bigl[\ln(1+x^{2})\Bigr]_0^{M}=\frac{1}{\pi}\lim_{M\to\infty}\ln(1+M^{2})=+\infty.$$

So $X\notin L^{1}$ and, by Definition 5.7, $\mathbb{E}[X]$ is undefined.

(c) For every $M>0$ the truncated variable $X\mathbf{1}_{\lvert X\rvert\le M}$ has an odd density, so its
expectation is $0$; hence the limit is $0$. This is the *Cauchy principal value* of $\int x f(x)dx$, not
the expectation: the expectation requires $\int\lvert x\rvert f(x)dx<\infty$, which fails by (b). Different
truncations give different answers — for instance truncating to $[-M,2M]$ gives a nonzero limit, because
the positive side receives twice the range of the negative side.

(d) The Chebyshev proof of the weak law needs $\operatorname{Var}(X)<\infty$; here $\mathbb{E}[X^{2}]=\infty$,
so $\Pr(\lvert\bar X_n-\mu\rvert\ge\varepsilon)\le\sigma^{2}/(n\varepsilon^{2})$ is a bound by an infinite
quantity and says nothing. In fact the average of $n$ independent standard Cauchy variables is again
standard Cauchy, so $\bar X_n$ has the same spread for every $n$ and does not concentrate at all (see the
next topic).

*Check:* (b) and (c) are consistent: the absolute integral diverges logarithmically while the symmetric
partial integrals vanish identically. This is the exact mechanism the absolute-convergence hypothesis of
Definition 5.7 is designed to exclude.

**35.** *(Strategy: read equality in the discriminant argument as the existence of a real root.)*

(a) Consider $q(t)=\mathbb{E}[(X+tY)^{2}]=\mathbb{E}[X^{2}]+2t\mathbb{E}[XY]+t^{2}\mathbb{E}[Y^{2}]$.
If $\mathbb{E}[Y^{2}]=0$ then $Y=0$ a.s. and the relation $0\cdot X+1\cdot Y=0$ exhibits linear dependence;
the claimed equality $(0)^{2}=0=\mathbb{E}[X^{2}]\cdot0$ holds. Similarly if $\mathbb{E}[X^{2}]=0$. Assume
now both second moments are positive. Equality in Cauchy–Schwarz says the discriminant of $q$ is $0$, so
$q$ has a real root $t_0$, and then $\mathbb{E}[(X+t_0Y)^{2}]=0$ forces $X=-t_0Y$ a.s. by Theorem 7.13.
Conversely, if $\alpha X+\beta Y=0$ a.s. with $(\alpha,\beta)\ne(0,0)$ and both second moments positive,
then $\alpha,\beta\ne0$ and $Y=aX$ a.s. with $a=-\alpha/\beta$; substituting,
$(\mathbb{E}[XY])^{2}=a^{2}(\mathbb{E}[X^{2}])^{2}=\mathbb{E}[X^{2}]\mathbb{E}[Y^{2}]$.

(b) Apply (a) to $U=X-\mathbb{E}X$ and $V=Y-\mathbb{E}Y$, which have positive variances by hypothesis.
Equality $\lvert\rho\rvert=1$ means $\lvert\operatorname{Cov}(X,Y)\rvert=\sigma_X\sigma_Y$, so $V=aU$ a.s.
and $Y=aX+(\mathbb{E}Y-a\mathbb{E}X)$. Moreover $\operatorname{Cov}(X,Y)=a\sigma_X^{2}$, so the sign of
$\rho$ is the sign of $a$: $\rho=1$ gives $a>0$ and $\rho=-1$ gives $a<0$.

(c) Let $X\sim\mathcal{N}(0,1)$ and $Y=2X$. Then $\operatorname{Cov}(X,Y)=2$, $\sigma_X=1$, $\sigma_Y=2$,
so $\rho=1$, while $Y\ne X$ on a set of probability $1$. Correlation one means a positive affine
relation, not equality.

*Check:* with $X$ standard normal and $Y=-3X+5$, $\rho=-1$ and $\sigma_Y=3$, consistent with
$\operatorname{Cov}(X,Y)=-3=-1\cdot1\cdot3$.

**36.** *(Strategy: add and subtract $Z=\mathbb{E}[X\mid Y]$, then show the cross term vanishes by the
tower property.)*

Write $Z=\mathbb{E}[X\mid Y]$ and $\Delta=Z-g(Y)$, so that $X-g(Y)=(X-Z)+\Delta$. Expanding,

$$\mathbb{E}\bigl[(X-g(Y))^{2}\bigr]=\mathbb{E}\bigl[(X-Z)^{2}\bigr]+2\mathbb{E}\bigl[(X-Z)\Delta\bigr]+\mathbb{E}[\Delta^{2}].$$

For the cross term, condition on $Y$ and use Theorem 7.23 with the bounded (or, by truncation, merely
square-integrable) function $\Delta$, which is determined by $Y$:

$$\mathbb{E}\bigl[(X-Z)\Delta\bigr]=\mathbb{E}\Bigl[\mathbb{E}\bigl[(X-Z)\Delta\mid Y\bigr]\Bigr]=\mathbb{E}\Bigl[\Delta\,\mathbb{E}[X-Z\mid Y]\Bigr]=\mathbb{E}\bigl[\Delta\,(Z-Z)\bigr]=0,$$

because $\mathbb{E}[X-Z\mid Y]=\mathbb{E}[X\mid Y]-Z=0$. Also
$\mathbb{E}[(X-Z)^{2}]=\mathbb{E}\bigl[\mathbb{E}[(X-Z)^{2}\mid Y]\bigr]=\mathbb{E}[\operatorname{Var}(X\mid Y)]$,
since $\mathbb{E}[X\mid Y]=Z$ inside the conditional world. Therefore

$$\mathbb{E}\bigl[(X-g(Y))^{2}\bigr]=\mathbb{E}\bigl[\operatorname{Var}(X\mid Y)\bigr]+\mathbb{E}\bigl[(Z-g(Y))^{2}\bigr].$$

The first term does not involve $g$ and the second is non-negative, vanishing exactly when $g(Y)=Z$ a.s.
Hence the minimum is $\mathbb{E}[\operatorname{Var}(X\mid Y)]$, attained at the conditional expectation (and
at any $g$ that agrees with it almost surely). $\blacksquare$

*Check:* taking $g\equiv\mathbb{E}[X]$ (no information) gives
$\mathbb{E}[(X-\mathbb{E}X)^{2}]=\operatorname{Var}(X)=\mathbb{E}[\operatorname{Var}(X\mid Y)]+\operatorname{Var}(\mathbb{E}[X\mid Y])$,
which is Theorem 7.24. So the best predictor is at least as good as the best constant, and the gain is
exactly the between-group variance.
