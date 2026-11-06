# Probability Distributions — Solutions

> [Probability Distributions](README.md) · Solutions to the 36 problems in [exercises.md](exercises.md)

Each solution states the strategy, carries out every significant step and ends with a check. Proofs are complete.
All numeric answers use the conventions of the tutorial: geometric and negative binomial count trials; gamma laws
carry a rate.

## Beginner

**1.** *(Strategy: read values off the binomial pmf; a single term is a product of a binomial coefficient, the
success probability to the power of the successes, and the failure probability to the power of the failures.)*

(a) $\Pr(X=0)=\binom50(0.3)^0(0.7)^5=(0.7)^5=0.16807$;
$\Pr(X=1)=\binom51(0.3)(0.7)^4=5(0.3)(0.2401)=0.36015$;
$\Pr(X=2)=\binom52(0.3)^2(0.7)^3=10(0.09)(0.343)=0.30870$.

(b) $\Pr(X\ge1)=1-\Pr(X=0)=0.83193$;
$\Pr(X\le2)=0.16807+0.36015+0.30870=0.83692$.

(c) $\mathbb{E}[X]=np=5(0.3)=1.5$; $\operatorname{Var}(X)=npq=5(0.3)(0.7)=1.05$; standard deviation
$\sqrt{1.05}\approx1.0247$.

(d) $\Pr(X=0)$ is the event "all five trials fail", whose probability is $q^5$ by independence. The factor
$p=0.3$ is the probability of success, which would be the correct factor for $\Pr(X=5)$.

*Check:* all six probabilities sum to $1$; the largest term is at $k=1$, close to the mean $1.5$. ✓

**2.** *(Strategy: the geometric pmf is $q^{k-1}p$; tail probabilities are pure powers of $q$.)*

(a) $\Pr(X=4)=(0.75)^3(0.25)=0.10547$; $\Pr(X>4)=(0.75)^4=0.31641$, because $X>4$ means the first four trials all
fail.

(b) $\Pr(X\le2)=0.25+(0.75)(0.25)=0.4375$.

(c) $\mathbb{E}[X]=1/p=4$; $\operatorname{Var}(X)=q/p^2=0.75/0.0625=12$; standard deviation $\approx3.4641$.

(d) $\Pr(X>8\mid X>4)=\Pr(X>4)$ by memorylessness $=0.31641$. Without the conditional formula:
$\Pr(X>8)/\Pr(X>4)=(0.75)^8/(0.75)^4=(0.75)^4$. Having survived four trials tells us nothing about the remaining
wait, which is again geometric with the same parameter.

*Check:* $\Pr(X\le4)=1-(0.75)^4=0.6836$, and $\Pr(X\le2)=0.4375<\Pr(X\le4)$. ✓

**3.** *(Strategy: the Poisson pmf has the recursion $\Pr(X=k+1)/\Pr(X=k)=\lambda/(k+1)$, which makes hand
computation quick.)*

(a) $\Pr(X=0)=e^{-2}=0.13534$; $\Pr(X=1)=2e^{-2}=0.27067$; $\Pr(X=3)=e^{-2}8/6=0.18045$.

(b) $\Pr(X\ge1)=1-e^{-2}=0.86466$; $\Pr(X\ge2)=1-e^{-2}(1+2)=1-3e^{-2}=0.59399$.

(c) Mean $=$ variance $=\lambda=2$; standard deviation $\sqrt2\approx1.4142$.

(d) The ratio is $\Pr(X=k+1)/\Pr(X=k)=\lambda/(k+1)=2/(k+1)$, which exceeds $1$ for $k<2$ and is below $1$ for
$k>2$: the pmf increases up to $k=2$ and decreases after it. Hence
$\Pr(X=4)=\Pr(X=3)\cdot\tfrac25=0.18045\cdot0.4=0.07218$.

*Check:* $\Pr(X\le3)=e^{-2}(1+2+2+1.3333)=0.85712$, so $\Pr(X\ge4)=0.14288$; the recursion gives
$\Pr(X=4)=0.07218$ for the first omitted term. ✓

**4.** *(Strategy: for a uniform law, probabilities are lengths divided by the total length.)*

(a) $f(x)=\tfrac14$ on $(1,5)$ and $0$ elsewhere; $F(x)=0$ for $x<1$, $F(x)=(x-1)/4$ for $1\le x<5$, $F(x)=1$ for
$x\ge5$.

(b) $\mathbb{E}[X]=(1+5)/2=3$; $\operatorname{Var}(X)=(5-1)^2/12=16/12=4/3$.

(c) $\Pr(2<X<4)=(4-2)/4=0.5$; $\Pr(X=3)=0$ by Proposition 8.4 of the previous topic.

(d) The median solves $(m-1)/4=\tfrac12$, so $m=3$. Also $Q(\tfrac14)=1+4(\tfrac14)=2$ and
$Q(\tfrac34)=1+4(\tfrac34)=4$, so the interquartile range is $2$.

*Check:* the mean and median agree, as symmetry requires; the IQR is half the range, as it must be for a uniform
law. ✓

**5.** *(Strategy: use $\Pr(X>t)=e^{-\lambda t}$ and the moment formulas for the exponential.)*

(a) $\mathbb{E}[X]=1/\lambda=2$; $\operatorname{Var}(X)=1/\lambda^2=4$; standard deviation $2$ — equal to the
mean.

(b) $\Pr(X>2)=e^{-0.5\cdot2}=e^{-1}=0.36788$; $\Pr(X\le1)=1-e^{-0.5}=0.39347$.

(c) $1-e^{-0.5m}=\tfrac12$ gives $m=2\ln2=1.38629$.

(d) The hazard is $h(t)=f(t)/\Pr(T>t)=0.5e^{-0.5t}/e^{-0.5t}=0.5$: a constant failure rate, meaning the
probability of failing in the next instant does not depend on the current age.

*Check:* median $1.386<$ mean $2$, consistent with a right-skewed density; $\Pr(X>2)+\Pr(X\le2)=1$. ✓

**6.** *(Strategy: standardise, $z=(x-\mu)/\sigma$, then use the standard normal table.)*

(a) $\Pr(X\le12)=\Phi\bigl((12-10)/2\bigr)=\Phi(1)=0.84134$;
$\Pr(8<X<12)=\Phi(1)-\Phi(-1)=2\Phi(1)-1=0.68269$.

(b) $Q(0.975)=10+2(1.95996)=13.9199$.

(c) $\Pr(X=10)=0$: the normal law is continuous.

(d) $10\pm3(2)=(4,16)$ contains $99.73\%$ of the mass, matching the empirical rule.

*Check:* the interval $(8,12)$ is exactly $\mu\pm\sigma$, and the empirical rule gives $68.27\%$. ✓

**7.** *(Strategy: a gamma density is a power times a decaying exponential, normalised by $\Gamma(\alpha)$.)*

(a) With $\alpha=2$, $\lambda=3$, $\Gamma(2)=1$,
$$
f(x)=\frac{3^2x^{2-1}e^{-3x}}{\Gamma(2)}=9xe^{-3x},\quad x>0,\qquad
\int_0^\infty9xe^{-3x}dx=9\cdot\frac{\Gamma(2)}{3^2}=1 .
$$

(b) $\mathbb{E}[X]=\alpha/\lambda=2/3$; $\operatorname{Var}(X)=\alpha/\lambda^2=2/9$.

(c) $M(t)=\bigl(3/(3-t)\bigr)^2$ for $t<3$.

(d) $X$ is the sum of two iid $\text{Exponential}(3)$ variables, since $\text{Gamma}(1,3)$ is $\text{Exp}(3)$ and
shapes add.

*Check:* the density has its maximum where $9e^{-3x}(1-3x)=0$, i.e. $x=1/3=(\alpha-1)/\lambda$, and the mean
$2/3=2\times$ the mode. ✓

**8.** *(Strategy: a beta density is a power times a power of $(1-x)$; the constant is $1/B(a,b)$.)*

(a) $B(3,2)=\Gamma(3)\Gamma(2)/\Gamma(5)=2\cdot1/24=1/12$, so $f(p)=12p^2(1-p)$ on $(0,1)$.

(b) $\mathbb{E}[P]=3/5=0.6$; $\operatorname{Var}(P)=\dfrac{3\cdot2}{5^2\cdot6}=0.04$; mode
$(a-1)/(a+b-2)=2/3\approx0.6667$.

(c) $f(0.5)=12(0.25)(0.5)=1.5$, above $1$ — a density value, not a probability.

(d) $\Pr(P\le0.5)=\int_0^{1/2}12p^2(1-p)dp=12\bigl[\tfrac{p^3}{3}-\tfrac{p^4}{4}\bigr]_0^{1/2}$, which equals
$12(\tfrac1{24}-\tfrac1{64})=\tfrac{5}{16}=0.3125$.

*Check:* $f$ integrates to $12B(3,2)=1$; the mode $0.667$ exceeds the mean $0.6$, as expected for a left-skewed
density. ✓

**9.** *(Strategy: the chi-squared family is the gamma family with rate $\tfrac12$.)*

(a) $\chi^2_\nu=\text{Gamma}(\nu/2,\tfrac12)$, so $X\sim\text{Gamma}(2,\tfrac12)$.

(b) With $\Gamma(2)=1$: $f(x)=\dfrac{(1/2)^2x^{2-1}e^{-x/2}}{\Gamma(2)}=\dfrac{xe^{-x/2}}{4}$. Then
$f(2)=\dfrac{2e^{-1}}{4}\approx0.18394$.

(c) $\mathbb{E}[X]=\nu=4$; $\operatorname{Var}(X)=2\nu=8$.

(d) $M(t)=(1-2t)^{-2}$. With $Y\sim\chi^2_3$ independent, $M_{X+Y}=(1-2t)^{-2}(1-2t)^{-3/2}=(1-2t)^{-7/2}$, so
$X+Y\sim\chi^2_7$.

*Check:* the gamma formulas give mean $2/(1/2)=4$ and variance $2/(1/4)=8$. ✓

**10.** *(Strategy: count favourable draws; the population is finite, so the draws are dependent.)*

(a) $\Pr(X=0)=\dfrac{\binom{15}{4}}{\binom{20}{4}}=\dfrac{1365}{4845}=0.28173$;
$\Pr(X=4)=\dfrac{\binom54\binom{15}{0}}{4845}=\dfrac{5}{4845}=0.00103$.

(b) $\mathbb{E}[X]=nK/N=4(0.25)=1$;
$\operatorname{Var}(X)=npq\dfrac{N-n}{N-1}=4(0.25)(0.75)\dfrac{16}{19}=0.63158$.

(c) The binomial variance with $n=4$, $p=0.25$ is $4(0.25)(0.75)=0.75$. The hypergeometric variance is smaller by
the finite population correction $16/19\approx0.8421$.

(d) The support is $\{\max(0,4+5-20),\dots,\min(4,5)\}=\{0,1,2,3,4\}$.

*Check:* $\Pr(X=4)=5/\binom{20}{4}$ is tiny, so the mean $1$ is far above the mass at the top of the support. ✓

**11.** *(Strategy: count the arrangements of the first $k-1$ trials.)*

(a) $\Pr(X=4)=p^4=0.0625$ (four successes in a row);
$\Pr(X=6)=\binom{5}{3}p^4q^2=10(0.0625)(0.25)=0.15625$.

(b) $\mathbb{E}[X]=r/p=8$; $\operatorname{Var}(X)=rq/p^2=4(0.5)/0.25=8$.

(c) $X=4$ means all of the first four trials are successes, an event of probability $p^4$, and the formula
$\binom{3}{3}p^4q^0=p^4$ agrees.

(d) $X$ is the sum of $r=4$ iid Geometric$(0.5)$ variables, so its mean is $4\times2=8$, matching (b).

*Check:* the pmf over $k\ge4$ sums to $1$; the values in (a) are below the maximum of the pmf, which is near
$k=7$–$8$, consistent with a mean of $8$. ✓

**12.** *(Strategy: identify the mechanism — fixed trials, waiting, sampling without replacement, rare events,
constant hazard, proportion.)*

(a) $\operatorname{Bin}(12,1/6)$: a fixed number of independent trials with a constant success probability.
(b) $\text{Geometric}(1/6)$: the number of trials until the first success.
(c) $\text{Hypergeometric}(200,20,10)$: sampling without replacement from a finite population; $\text{Bin}(10,0.1)$
is a good approximation because $200$ is large relative to $10$.
(d) $\operatorname{Pois}(30)$: counts of rare events in a fixed window, with independent arrivals.
(e) $\text{Exponential}(\lambda)$ with $\lambda$ the decay rate: a wait with constant hazard.
(f) $\text{Beta}(a,b)$ with $a/(a+b)=0.2$: a flexible density on $(0,1)$ with the required mean.

*Check:* each answer names a family whose support matches the observable: counts on $\{0,\dots,n\}$, waits on
$\{1,2,\dots\}$ or $(0,\infty)$, a proportion on $(0,1)$. ✓

## Intermediate

**13.** *(Strategy: compute the binomial exactly, then replace it by a Poisson with the same mean.)*

(a) $\Pr(X=0)=(0.9)^{20}=0.12158$; $\Pr(X=1)=20(0.1)(0.9)^{19}=0.27017$; hence
$\Pr(X\le1)=0.39175$.

(b) With $\lambda=2$: $e^{-2}=0.13534$, $2e^{-2}=0.27067$, and $\Pr(\text{Pois}(2)\le1)=3e^{-2}=0.40601$.

(c) The binomial is exact here: $20$ independent trials with constant $p=0.1$ is precisely its mechanism. The
Poisson is the limit of $\operatorname{Bin}(n,\lambda/n)$ as $n\to\infty$ with $np=\lambda$, and at $n=20$ the
error is already only about $0.014$ in the CDF.

*Check:* the two values of $\Pr(X=1)$ agree to three decimal places while $\Pr(X=0)$ differs by $0.014$; the
Poisson over-weights $0$, as it must since it allows $n\to\infty$ trials. ✓

**14.** *(Strategy: a "third success" event is a negative binomial event, and the same event can be read as a
binomial event counting successes in a fixed number of shots.)*

(a) $\Pr(X=5)=\binom42(0.4)^3(0.6)^2=6(0.064)(0.36)=0.13824$. Also
$\Pr(X=3)=0.4^3=0.064$ and $\Pr(X=4)=\binom32(0.4)^3(0.6)=0.1152$, so
$\Pr(X\le5)=0.064+0.1152+0.13824=0.31744$.

(b) $\mathbb{E}[X]=3/0.4=7.5$; $\operatorname{Var}(X)=3(0.6)/0.16=11.25$, so the standard deviation is
$\sqrt{11.25}\approx3.3541$.

(c) $X>10$ means fewer than three baskets in the first ten shots:
$$
\Pr(X>10)=\sum_{j=0}^{2}\binom{10}{j}(0.4)^j(0.6)^{10-j}
=0.0060466+0.0403108+0.1209324=0.16729 .
$$

(d) Summing the negative binomial pmf from $k=3$ to $10$ gives the complementary event $X\le10$, whose complement
is $X>10$; the binomial computation in (c) is the shorter route, avoiding the sum.

*Check:* $\Pr(X\le10)=1-0.16729=0.83271$, and the mean $7.5$ lies inside that range, as it should. ✓

**15.** *(Strategy: same mean, different dependence structure.)*

(a) $\Pr(X=2)=\dfrac{\binom{20}{2}\binom{80}{8}}{\binom{100}{10}}=0.31817$.

(b) $\Pr(X=2)=\binom{10}{2}(0.2)^2(0.8)^8=0.30199$.

(c) Hypergeometric: $10(0.2)(0.8)(90/99)=1.45455$. Binomial: $10(0.2)(0.8)=1.6$.

(d) Sampling without replacement makes the draws negatively dependent: a marked item drawn reduces the
proportion of marked items left, so the count is less variable. The correction factor is $(N-n)/(N-1)=90/99$.

*Check:* the two probabilities differ by $0.016$, and the variance ratio $1.45455/1.6=0.9091$ equals $90/99$. ✓

**16.** *(Strategy: Poisson counts in windows; waits are exponential with the same rate.)*

(a) $N\bigl((0,0.5]\bigr)\sim\operatorname{Pois}(4\cdot0.5)=\operatorname{Pois}(2)$, so the probability of no
event is $e^{-2}=0.13534$.

(b) $N\bigl((0,1]\bigr)\sim\operatorname{Pois}(4)$, so $\Pr(N=3)=e^{-4}4^3/3!=0.19537$.

(c) $T\sim\text{Exponential}(4)$: $\Pr(T>t)=e^{-4t}$, so $\Pr(T>1/3)=e^{-4/3}=0.26360$. Also
$\mathbb{E}[T]=1/4$ hour $=15$ minutes.

(d) Half-hour counts are independent $\operatorname{Pois}(2)$; the probability that each is at least $1$ is
$(1-e^{-2})^2=0.86466^2=0.74764$.

*Check:* $\Pr(N((0,1])\ge1)=1-e^{-4}=0.98168$, larger than the value in (d) for a single half-hour. ✓

**17.** *(Strategy: exponential tails and memorylessness.)*

(a) $\lambda=1/8$: $\Pr(T>10)=e^{-10/8}=e^{-1.25}=0.28650$. Median $8\ln2=5.54518$.

(b) $\Pr(T>18\mid T>8)=\Pr(T>10)=0.28650$ by memorylessness: having survived eight years, the residual life has
the same exponential law, regardless of the age.

(c) $\Pr(T\le10\mid T>8)=1-0.28650=0.71350$.

(d) For a wear-out component the hazard increases with age, so survival past $18$ given survival past $8$ is
*less* likely: the answer would be smaller than $0.28650$.

*Check:* the median $5.545$ is below the mean $8$, consistent with the right skew, and
$\Pr(T>8)=e^{-1}=0.36788>\Pr(T>10)=0.28650$. ✓

**18.** *(Strategy: a sum of exponential waits is gamma, and the waiting time event is a count event.)*

(a) $S_3\sim\text{Gamma}(3,0.5)$: mean $3/0.5=6$ hours, variance $3/0.25=12$.

(b) With $\Gamma(3)=2$ and $\lambda^3=0.125$,
$$
\Pr(S_3\le2)=\int_0^2\frac{0.125x^2e^{-0.5x}}{2}dx=0.0625\int_0^2x^2e^{-x/2}dx .
$$
Substituting $x=2u$ gives $\int_0^2x^2e^{-x/2}dx=8\int_0^1u^2e^{-u}du=8(2-5e^{-1})=1.28479$, so the probability is
$0.0625(1.28479)=0.08030$.

(c) $S_3\le2$ if and only if at least three events occur in $[0,2]$, i.e. $N(2)\ge3$ with $N(2)\sim\text{Pois}(1)$:
$$
\Pr(N(2)\ge3)=1-e^{-1}\Bigl(1+1+\frac12\Bigr)=1-2.5e^{-1}=0.08030 .
$$

(d) The two events are identical: "the third event occurs by time $2$" is the same statement as "at least three
events occur by time $2$". So the gamma CDF of the waiting time equals the Poisson tail of the count.

*Check:* both computations give $0.08030$; the closed form $1-\tfrac52e^{-1}$ is exact. ✓

**19.** *(Strategy: use the moments and the derivative of the beta density.)*

(a) $\mathbb{E}[P]=2/6=1/3\approx0.33333$; $\operatorname{Var}(P)=\dfrac{2\cdot4}{6^2\cdot7}=\dfrac{2}{63}\approx0.03175$;
mode $(a-1)/(a+b-2)=1/4=0.25$.

(b) $B(2,4)=\Gamma(2)\Gamma(4)/\Gamma(6)=6/120=0.05$, so $f(p)=20p(1-p)^3$, and $f(0.5)=20(0.5)(0.125)=1.25$.

(c) $\Pr(P\le0.5)=\int_0^{1/2}20p(1-p)^3dp$. With $(1-p)^3=1-3p+3p^2-p^3$,
$$
\int_0^{1/2}20(p-3p^2+3p^3-p^4)dp=20\Bigl(\frac18-\frac18+\frac{3}{64}-\frac{1}{160}\Bigr)
=20\Bigl(\frac{15-2}{320}\Bigr)=\frac{13}{16}=0.8125 .
$$

(d) Mode $0.25<$ median $\approx0.3138<$ mean $0.3333$: the density has a long right tail, so it is
right-skewed.

*Check:* $f$ integrates to $20B(2,4)=1$; $\Pr(P\le0.5)=0.8125>\tfrac12$ implies the median is below $0.5$. ✓

**20.** *(Strategy: approximate a lattice distribution by a normal with the same mean and variance, applying the
continuity correction.)*

(a) Mean $40$, variance $100(0.4)(0.6)=24$, standard deviation $4.8990$. With the correction,
$$
\Pr(X\le35)\approx\Phi\Bigl(\frac{35.5-40}{\sqrt{24}}\Bigr)=\Phi(-0.91856)=0.17916,
$$
against the exact $0.17947$: an error of $0.0003$.

(b) $\Pr(X=40)\approx\Phi(0.10206)-\Phi(-0.10206)=0.08129$, against the exact $0.08122$.

(c) The binomial is supported on integers, so $\{X\le35\}$ corresponds to the interval $(-\infty,35.5]$ in the
continuous approximation; without the $0.5$ shift the normal would attribute to $35$ only the area up to $35$,
biasing the answer.

(d) $\mathcal{N}(40,24)$.

*Check:* both approximations are within $0.0004$ of the exact values, which is the accuracy the correction
typically delivers at $n=100$. ✓

**21.** *(Strategy: compute the CDF of $Z^2$, differentiate, and compare with the chi-squared density.)*

(a) For $y>0$, $F_Y(y)=\Pr(-\sqrt y\le Z\le\sqrt y)=2\Phi(\sqrt y)-1$; differentiating with the chain rule and
$\varphi(z)=e^{-z^2/2}/\sqrt{2\pi}$,
$$
f_Y(y)=2\varphi(\sqrt y)\frac{1}{2\sqrt y}=\frac{e^{-y/2}}{\sqrt{2\pi y}} .
$$

(b) This is the $\chi^2_1$ density: $\dfrac{y^{1/2-1}e^{-y/2}}{2^{1/2}\Gamma(1/2)}$ with $\Gamma(\tfrac12)=\sqrt\pi$
equals $\dfrac{e^{-y/2}}{\sqrt{2\pi y}}$. ✓

(c) From the normal, $\Pr(Z^2\le1)=\Pr(-1\le Z\le1)=2\Phi(1)-1=0.68269$. From the density, the substitution
$y=z^2$, $dy=2z\,dz$ gives
$\int_0^1\dfrac{e^{-y/2}}{\sqrt{2\pi y}}dy=2\int_0^1\varphi(z)dz=0.68269$. ✓

(d) The density behaves like $1/\sqrt y$ near $0$, so it is unbounded there, although its integral over $(0,1)$ is
finite. A density, unlike a mass, may be unbounded.

*Check:* the $\chi^2_1$ density integrates to $1$ because $\Gamma(\tfrac12)=\sqrt\pi$; and its mean
$\nu=1$ matches $\mathbb{E}[Z^2]=1$. ✓

**22.** *(Strategy: differentiate the log MGF twice and evaluate at zero.)*

(a) $\log M(t)=\alpha\bigl(\log\lambda-\log(\lambda-t)\bigr)$, so
$(\log M)'(t)=\dfrac{\alpha}{\lambda-t}$ and $(\log M)''(t)=\dfrac{\alpha}{(\lambda-t)^2}$.

(b) At $t=0$: $\mathbb{E}[X]=\alpha/\lambda$ and $\operatorname{Var}(X)=\alpha/\lambda^2$.

(c) These agree with the gamma moments derived in §7.9 by integration.

(d) $(\log M)''=M''/M-(M'/M)^2$, which at $0$ equals $\mathbb{E}[X^2]-\mathbb{E}[X]^2$: the second derivative of
the log subtracts the square of the mean automatically. The second derivative of $M$ alone gives
$\mathbb{E}[X^2]$, which is not the variance.

*Check:* for $\alpha=2,\lambda=3$ this gives $2/3$ and $2/9$, matching Exercise 7. ✓

**23.** *(Strategy: multiply MGFs for the sum; condition by dividing joint probabilities.)*

(a) $M_{X+Y}(t)=e^{2(e^t-1)}e^{3(e^t-1)}=e^{5(e^t-1)}$, which is the $\operatorname{Pois}(5)$ MGF; by
uniqueness, $X+Y\sim\operatorname{Pois}(5)$.

(b) $\Pr(X+Y\le1)=e^{-5}(1+5)=6e^{-5}=0.04043$.

(c) The joint pmf is $\Pr(X=x,Y=y)=e^{-2}2^x/x!\cdot e^{-3}3^y/y!$, so
$$
\Pr(X=1\mid X+Y=3)=\frac{\Pr(X=1,Y=2)}{\Pr(X+Y=3)}
=\frac{e^{-2}\cdot2\cdot e^{-3}\cdot\frac92}{e^{-5}\frac{125}{6}}
=\frac{9}{125/6}=\frac{54}{125}=0.432 .
$$

(d) In general $X\mid X+Y=n\sim\operatorname{Bin}\bigl(n,\lambda/(\lambda+\mu)\bigr)$, with mean
$n\lambda/(\lambda+\mu)$. Here that is $\operatorname{Bin}(3,0.4)$, whose value at $1$ is
$\binom31(0.4)(0.6)^2=0.432$. ✓

*Check:* (c) and (d) agree, and $\Pr(X+Y=3)=e^{-5}125/6=0.14037$ is a valid probability. ✓

## Advanced

**24.** *(Strategy: substitute $j=k-r$, then use the generating function of $\binom{j+r-1}{j}$ and the hockey-stick
identity.)*

(a) With $j=k-r\ge0$ and $\binom{k-1}{r-1}=\binom{j+r-1}{j}$,
$$
\sum_{k\ge r}\binom{k-1}{r-1}p^rq^{k-r}=p^r\sum_{j\ge0}\binom{j+r-1}{j}q^j=p^r(1-q)^{-r}=p^rp^{-r}=1,
$$
using the negative binomial series $(1-x)^{-r}=\sum_{j\ge0}\binom{j+r-1}{j}x^j$ for $\lvert x\rvert<1$.

(b) Since $k=j+r$,
$$
\mathbb{E}[X]=p^r\sum_{j\ge0}(j+r)\binom{j+r-1}{j}q^j .
$$
The identity $(j+r)\binom{j+r-1}{j}=\dfrac{(j+r)!}{j!\,(r-1)!}=r\binom{j+r}{j}$ holds because
$\binom{j+r}{j}=\dfrac{(j+r)!}{j!\,r!}$. Therefore
$$
\mathbb{E}[X]=rp^r\sum_{j\ge0}\binom{j+r}{j}q^j=rp^r(1-q)^{-r-1}=rp^rp^{-r-1}=\frac rp,
$$
using $(1-x)^{-r-1}=\sum_{j\ge0}\binom{j+r}{j}x^j$.

(c) For $r=1$ the pmf is $q^{k-1}p$, which is Geometric$(p)$. Suppose the sum of $r-1$ iid Geometric$(p)$ variables
has pmf $\binom{j-1}{r-2}p^{r-1}q^{j-r+1}$. Convolving with one more geometric variable, for $k\ge r$,
$$
\Pr(S_r=k)=\sum_{j=r-1}^{k-1}\binom{j-1}{r-2}p^{r-1}q^{j-r+1}\cdot pq^{k-j-1}
=p^rq^{k-r}\sum_{j=r-1}^{k-1}\binom{j-1}{r-2}.
$$
The hockey-stick identity $\sum_{m=r-2}^{k-2}\binom{m}{r-2}=\binom{k-1}{r-1}$ (with $m=j-1$) turns the sum into
$\binom{k-1}{r-1}$, so $\Pr(S_r=k)=\binom{k-1}{r-1}p^rq^{k-r}$, the negative binomial pmf. By induction this holds
for every $r\ge1$.

(d) Expectations add for sums of random variables and variances add for sums of *independent* variables. Since the
$r$ geometrics are independent with mean $1/p$ and variance $q/p^2$, the sum has mean $r/p$ and variance $rq/p^2$,
matching the MGF computation of §7.4.

*Check:* at $r=1$, (b) gives $1/p$, the geometric mean; and (c) at $k=r$ gives $p^r$, the probability that the
first $r$ trials are all successes. ✓

**25.** *(Strategy: $S(n)=\Pr(X>n)$ satisfies $S(n+1)=S(n)S(1)$.)*

(a) For the geometric law, $\Pr(X>m)=q^m$ for $m\ge0$ (the first $m$ trials all fail). Then
$$
\Pr(X>n+k\mid X>n)=\frac{\Pr(X>n+k)}{\Pr(X>n)}=\frac{q^{n+k}}{q^n}=q^k=\Pr(X>k).
$$

(b) Take $k=1$ in the identity: $\Pr(X>n+1\mid X>n)=\Pr(X>1)=q$, where $q=S(1)$. Since
$\Pr(X>n\mid X>n)=1$ and $S(n)>0$ for all $n$ (because $S(n)=q^n>0$ by induction from $S(0)=1$ and
$S(n+1)=qS(n)$), we get $S(n+1)=qS(n)$; induction gives $S(n)=q^n$.

(c) Then $\Pr(X=n)=S(n-1)-S(n)=q^{n-1}-q^n=q^{n-1}(1-q)=q^{n-1}p$ with $p=1-S(1)\in(0,1)$, which is the
geometric pmf.

(d) If $S(1)=0$ then $S(n)=0$ for all $n\ge1$ and $X=1$ almost surely: a degenerate variable, which is the
boundary case $p=1$ of the family, so nothing genuinely new occurs. If $X$ is allowed to take values in
$\mathbb{Z}$ rather than $\{1,2,\dots\}$, the shifted geometric laws $X=G+c$ satisfy the same identity but are not
geometric in the stated sense; and if $X$ may take non-integer values, the step $k=1$ no longer controls the whole
support.

*Check:* $\Pr(X=n)=q^{n-1}p$ sums to $1$; the identity was verified directly in (a). ✓

**26.** *(Strategy: bound each factor in the product display of §7.6.)*

(a) With $\lambda_n=np_n$,
$$
\Pr(X_n=k)=\Bigl[\prod_{j=0}^{k-1}\Bigl(1-\frac jn\Bigr)\Bigr]\cdot\frac{\lambda_n^k}{k!}\cdot
\Bigl(1-\frac{\lambda_n}{n}\Bigr)^{n}\cdot\Bigl(1-\frac{\lambda_n}{n}\Bigr)^{-k}.
$$

(b) Each factor is at most $1$, and by the union bound (or Bernoulli's inequality)
$$
\prod_{j=0}^{k-1}\Bigl(1-\frac jn\Bigr)\ \ge\ 1-\sum_{j=0}^{k-1}\frac jn=1-\frac{k(k-1)}{2n}.
$$
So the first factor lies in $[1-k(k-1)/(2n),\,1]$; its distance from $1$ is at most $k(k-1)/(2n)$.

(c) Using $\log(1-x)=-x-\frac{x^2}{2}+O(x^3)$ for $x\to0$,
$$
n\log\Bigl(1-\frac{\lambda_n}{n}\Bigr)=-\lambda_n-\frac{\lambda_n^2}{2n}+O\Bigl(\frac{\lambda_n^3}{n^2}\Bigr),
$$
so the difference between the two logarithms is bounded by $C\lambda_n^2/n\le C(2\lambda)^2/n$ when
$\lambda_n\le2\lambda$. Since $\lvert e^a-e^b\rvert\le e^{\max(a,b)}\lvert a-b\rvert$ and the exponents are bounded
near $-\lambda$, the third factor differs from $e^{-\lambda_n}$ by at most $C'/n$. Finally
$\lvert e^{-\lambda_n}-e^{-\lambda}\rvert\le\lvert\lambda_n-\lambda\rvert$, of order $1/n$ in the standard case
$p_n=\lambda/n$.

(d) The fourth factor differs from $1$ by $O(1/n)$, and $\lambda_n^k/k!\to\lambda^k/k!$ with an error of order
$O(\lvert\lambda_n-\lambda\rvert)=O(1/n)$. Multiplying the four bounds gives
$$
\Bigl\lvert\Pr(X_n=k)-e^{-\lambda}\frac{\lambda^k}{k!}\Bigr\rvert\le\frac{C_k}{n},
$$
as claimed.

*Check:* at $n=1000$, $p=0.003$, $k=0$ the bound predicts an error of order $10^{-3}$, and the actual error is
$2\times10^{-4}$ (Exercise 9.4 of the tutorial). ✓

**27.** *(Strategy: divide the joint pmf by the pmf of the sum.)*

(a) For $0\le x\le n$, by independence,
$$
\Pr(X=x\mid X+Y=n)=\frac{e^{-\lambda}\dfrac{\lambda^x}{x!}\cdot e^{-\mu}\dfrac{\mu^{n-x}}{(n-x)!}}
{e^{-(\lambda+\mu)}\dfrac{(\lambda+\mu)^n}{n!}}
=\binom{n}{x}\frac{\lambda^x\mu^{n-x}}{(\lambda+\mu)^n}.
$$

(b) This is the $\operatorname{Bin}\bigl(n,\lambda/(\lambda+\mu)\bigr)$ pmf: set $p=\lambda/(\lambda+\mu)$, then
$\lambda^x\mu^{n-x}/(\lambda+\mu)^n=p^x(1-p)^{n-x}$.

(c) With $\lambda=2$, $\mu=3$: $p=0.4$ and $\binom31(0.4)(0.6)^2=0.432$, matching Exercise 23(c).

(d) Given that $n$ events occurred in total, each event is independently of the first type with probability
$p=\lambda/(\lambda+\mu)$: the two Poisson streams are two independent thinnings of a combined stream. This is the
discrete analogue of splitting a Poisson process, and it is the reason a Poisson count conditioned on its total is
binomial.

*Check:* the conditional pmf sums to $1$ over $x=0,\dots,n$ by the binomial theorem; its mean
$np=n\lambda/(\lambda+\mu)$ lies between $0$ and $n$. ✓

**28.** *(Strategy: write the hypergeometric pmf as a product of ratios that converge separately.)*

(a) Using $\binom{N}{k}\binom{N-k}{n-k}=\binom{N}{n}\binom{n}{k}$,
$$
\Pr(X_N=k)=\frac{\binom{K}{k}}{\binom{N}{k}}\cdot
\frac{\binom{N-K}{n-k}}{\binom{N-k}{n-k}}\cdot\binom{n}{k}.
$$

(b) Expanding the first ratio,
$$
\frac{\binom{K}{k}}{\binom{N}{k}}=\prod_{j=0}^{k-1}\frac{K-j}{N-j}\longrightarrow p^k,
$$
since $\frac{K-j}{N-j}=\frac{K/N-j/N}{1-j/N}\to p$ for each fixed $j$. Similarly
$$
\frac{\binom{N-K}{n-k}}{\binom{N-k}{n-k}}=\prod_{j=0}^{n-k-1}\frac{N-K-j}{N-k-j}\longrightarrow(1-p)^{n-k}.
$$

(c) $\binom{N}{k}\binom{N-k}{n-k}=\dfrac{N!}{k!\,(N-k)!}\cdot\dfrac{(N-k)!}{(n-k)!\,(N-n)!}$, and cancelling
$(N-k)!$ gives $\dfrac{N!}{k!\,(n-k)!\,(N-n)!}=\binom{N}{n}\binom{n}{k}$.

(d) Multiplying the limits, $\Pr(X_N=k)\to\binom{n}{k}p^k(1-p)^{n-k}$, the binomial pmf. The variance formula
behaves consistently: $np(1-p)\frac{N-n}{N-1}\to np(1-p)$ since $(N-n)/(N-1)\to1$ for fixed $n$; the finite
population correction disappears in the limit, as it should when sampling a vanishing fraction of an infinite
population.

*Check:* at $n=10$, $p=0.2$ the limit value $0.30199$ is close to the finite-$N$ value $0.31817$ (Exercise 15);
the difference shrinks as $N$ grows. ✓

**29.** *(Strategy: reduce the functional equation to the Cauchy equation on a dense set.)*

(a) For $S(t)=e^{-\lambda t}$, $S(s+t)=e^{-\lambda(s+t)}=e^{-\lambda s}e^{-\lambda t}=S(s)S(t)$.

(b) With $s=t$: $S(2)=S(1)^2$, and by induction $S(n)=S(1)^n$ for $n\in\mathbb{N}$. Next,
$S(1)=S(1/m)^m$ gives $S(1/m)=S(1)^{1/m}$, and then
$S(n/m)=S(1/m)^n=S(1)^{n/m}$. So $S(q)=S(1)^q$ for every rational $q\ge0$.

(c) For real $t\ge0$ choose rationals $q_n\downarrow t$. Monotonicity and right-continuity give
$S(t)=\lim_nS(q_n)=\lim_nS(1)^{q_n}=S(1)^t=e^{t\log S(1)}$. Since $S$ is non-increasing and $S(1)\in(0,1)$, put
$\lambda=-\log S(1)>0$: then $S(t)=e^{-\lambda t}$.

(d) The extension step needs regularity. Without right-continuity the values on the rationals do not determine the
value at an irrational point; and if monotonicity is dropped as well, the multiplicative Cauchy equation admits
wild solutions built from a Hamel basis. Monotonicity together with the functional equation already forces
continuity, so right-continuity is a convenient hypothesis rather than a necessary one, but *some* regularity is
needed for the argument as written.

*Check:* $\lambda=-\log S(1)$ is positive exactly because $S(1)<1$, and $S(t)\to0$ as $t\to\infty$ for $\lambda>0$,
as a survival function must. ✓

**30.** *(Strategy: identify the chi-squared family inside the gamma family.)*

(a) For $Y=Z_1^2$ and $y>0$, summing over the two preimages,
$$
f_Y(y)=\frac{\varphi(\sqrt y)+\varphi(-\sqrt y)}{2\sqrt y}
=\frac{e^{-y/2}}{\sqrt{2\pi y}}
=\frac{(1/2)^{1/2}y^{1/2-1}e^{-y/2}}{\Gamma(1/2)},
$$
using $\Gamma(\tfrac12)=\sqrt\pi$; this is $\text{Gamma}(\tfrac12,\tfrac12)$.

(b) Each $Z_i^2$ is independent $\text{Gamma}(\tfrac12,\tfrac12)$, and gammas with a common rate add shapes, so
$X\sim\text{Gamma}(\nu/2,\tfrac12)$, i.e.
$$
f_X(x)=\frac{x^{\nu/2-1}e^{-x/2}}{2^{\nu/2}\Gamma(\nu/2)},\quad x>0,
$$
which integrates to $1$ because $\int_0^\infty x^{\nu/2-1}e^{-x/2}dx=2^{\nu/2}\Gamma(\nu/2)$ by the substitution
$x=2u$.

(c) From the gamma formulas, $\mathbb{E}[X]=\frac{\nu/2}{1/2}=\nu$ and
$\operatorname{Var}(X)=\frac{\nu/2}{1/4}=2\nu$. From the representation, $\mathbb{E}[X]=\sum_i\mathbb{E}[Z_i^2]=\nu$
and, by independence, $\operatorname{Var}(X)=\sum_i\operatorname{Var}(Z_i^2)=\nu(3-1)=2\nu$, using
$\mathbb{E}[Z^4]=3$ for a standard normal. The two agree.

(d) $M_X(t)=(1-2t)^{-\nu/2}$. For independent $X_1\sim\chi^2_{\nu_1}$ and $X_2\sim\chi^2_{\nu_2}$,
$M_{X_1+X_2}=(1-2t)^{-(\nu_1+\nu_2)/2}$, so $X_1+X_2\sim\chi^2_{\nu_1+\nu_2}$.

*Check:* $\nu=1$ gives $\mathbb{E}[X]=1$ and $\operatorname{Var}(X)=2$, matching the moments of $Z^2$
($\mathbb{E}[Z^2]=1$, $\mathbb{E}[Z^4]=3$). ✓

## Challenge

**31.** *(Strategy: change variables in the joint density; the Jacobian makes the two coordinates separate.)*

(a) By independence,
$$
f_{X,Y}(x,y)=\frac{\lambda^ax^{a-1}e^{-\lambda x}}{\Gamma(a)}\cdot\frac{\lambda^by^{b-1}e^{-\lambda y}}{\Gamma(b)}
=\frac{\lambda^{a+b}}{\Gamma(a)\Gamma(b)}x^{a-1}y^{b-1}e^{-\lambda(x+y)},\quad x,y>0 .
$$

(b) The map $x=uv$, $y=(1-u)v$ has Jacobian
$$
\frac{\partial(x,y)}{\partial(u,v)}=\det\begin{pmatrix}v&u\\-v&1-u\end{pmatrix}=v(1-u)+uv=v,
$$
so $dx\,dy=v\,du\,dv$, with $u\in(0,1)$ and $v>0$.

(c) Substituting, and using $x^{a-1}y^{b-1}=(uv)^{a-1}\bigl((1-u)v\bigr)^{b-1}=u^{a-1}(1-u)^{b-1}v^{a+b-2}$,
$$
f_{U,V}(u,v)=\frac{\lambda^{a+b}}{\Gamma(a)\Gamma(b)}u^{a-1}(1-u)^{b-1}v^{a+b-1}e^{-\lambda v}.
$$
This factorises into a function of $u$ and a function of $v$.

(d) The total integral is
$$
\frac{\lambda^{a+b}}{\Gamma(a)\Gamma(b)}
\Bigl(\int_0^1u^{a-1}(1-u)^{b-1}du\Bigr)
\Bigl(\int_0^\infty v^{a+b-1}e^{-\lambda v}dv\Bigr)=1,
$$
and the second integral equals $\Gamma(a+b)/\lambda^{a+b}$. Hence the first integral equals
$\Gamma(a)\Gamma(b)/\Gamma(a+b)$, and
$$
f_{U,V}(u,v)=\underbrace{\frac{u^{a-1}(1-u)^{b-1}}{B(a,b)}}_{\text{Beta}(a,b)}
\cdot\underbrace{\frac{\lambda^{a+b}v^{a+b-1}e^{-\lambda v}}{\Gamma(a+b)}}_{\text{Gamma}(a+b,\lambda)} .
$$
A joint density that is the product of a function of $u$ and a function of $v$, each integrating to $1$, makes the
coordinates independent with those marginals. So $U\sim\text{Beta}(a,b)$,
$V\sim\text{Gamma}(a+b,\lambda)$, and $U\perp\!\!\!\perp V$.

(e) The computation in (d) shows $\int_0^1u^{a-1}(1-u)^{b-1}du=\Gamma(a)\Gamma(b)/\Gamma(a+b)$, which is exactly
$B(a,b)=\Gamma(a)\Gamma(b)/\Gamma(a+b)$.

*Check:* with $a=b=1$ the result says $U\sim\text{Beta}(1,1)=\text{Uniform}(0,1)$, and indeed for independent
exponentials $X/(X+Y)$ is uniform — a standard fact worth verifying by symmetry. ✓

**32.** *(Strategy: one convolution, one binomial theorem.)*

(a) For $n\ge0$, by independence and the law of total probability on the value of $X$,
$$
\Pr(X+Y=n)=\sum_{k=0}^{n}\Pr(X=k)\Pr(Y=n-k)
=e^{-(\lambda+\mu)}\sum_{k=0}^{n}\frac{\lambda^k\mu^{n-k}}{k!\,(n-k)!}.
$$
Multiplying and dividing by $n!$ turns the sum into $\frac1{n!}\sum_k\binom{n}{k}\lambda^k\mu^{n-k}$, which is
$\frac{(\lambda+\mu)^n}{n!}$ by the binomial theorem. Hence
$\Pr(X+Y=n)=e^{-(\lambda+\mu)}\frac{(\lambda+\mu)^n}{n!}$.

(b) This is exactly the $\operatorname{Pois}(\lambda+\mu)$ pmf.

(c) The argument uses only the pmfs and the binomial theorem: no moment generating function, no uniqueness theorem,
no assumption that any MGF exists. Conceptually it exhibits the closure as a combinatorial fact — Poisson variables
are "binomial coefficients in disguise" — and it extends to cases where the MGF argument would need care about
convergence.

(d) Induction: the case of two variables is (a); if $S_{m}\sim\operatorname{Pois}(\lambda_1+\cdots+\lambda_m)$ and
$X_{m+1}\sim\operatorname{Pois}(\lambda_{m+1})$ is independent of $S_m$, then (a) applied to the pair gives
$S_{m+1}\sim\operatorname{Pois}(\lambda_1+\cdots+\lambda_{m+1})$.

*Check:* $\lambda=2$, $\mu=3$ gives $X+Y\sim\operatorname{Pois}(5)$, whose value at $n=1$ is $6e^{-5}=0.04043$,
matching Exercise 23(b). ✓

**33.** *(Strategy: reduce the $d$-dimensional integral to a product of one-dimensional ones.)*

(a) Let $I=\int_{\mathbb{R}}e^{-x^2/2}dx$. Then
$$
I^2=\int_{\mathbb{R}}\int_{\mathbb{R}}e^{-(x^2+y^2)/2}dx\,dy
=\int_0^{2\pi}\int_0^\infty e^{-r^2/2}r\,dr\,d\theta
=2\pi\Bigl[-e^{-r^2/2}\Bigr]_0^\infty=2\pi,
$$
so $I=\sqrt{2\pi}$ and $\int\varphi_1=1$.

(b) Since $\varphi_d(x)=\prod_{i=1}^d\varphi_1(x_i)$, Tonelli's theorem (the integrand is non-negative) gives
$$
\int_{\mathbb{R}^d}\varphi_d(x)dx=\prod_{i=1}^d\int_{\mathbb{R}}\varphi_1(x_i)dx_i=1^d=1 .
$$

(c) For $Y=AZ$ with $A$ invertible, the change-of-variables formula for a linear map gives
$$
f_Y(y)=\varphi_d(A^{-1}y)\,\lvert\det A^{-1}\rvert
=(2\pi)^{-d/2}\lvert\det A\rvert^{-1}\exp\Bigl(-\tfrac12\lvert A^{-1}y\rvert^2\Bigr).
$$

(d) Now $\lvert A^{-1}y\rvert^2=y^{\mathsf{T}}(A^{-1})^{\mathsf{T}}A^{-1}y=y^{\mathsf{T}}(AA^{\mathsf{T}})^{-1}y$,
and $\det\Sigma=\det(AA^{\mathsf{T}})=(\det A)^2$, so $\lvert\det A\rvert=\sqrt{\det\Sigma}$. Substituting,
$$
f_Y(y)=\frac{1}{(2\pi)^{d/2}\sqrt{\det\Sigma}}\exp\Bigl(-\tfrac12y^{\mathsf{T}}\Sigma^{-1}y\Bigr),
$$
which is the multivariate normal density with $\mu=0$ and $\Sigma=AA^{\mathsf{T}}$; translation by $\mu$ gives the
general case.

*Check:* for $d=1$ and $A=\sigma>0$, the formula gives $\Sigma=\sigma^2$ and the usual
$\mathcal{N}(0,\sigma^2)$ density. ✓

**34.** *(Strategy: integrate the conditional pmf against the gamma density; the integral is a gamma integral.)*

(a) $\Pr(N=n\mid\Lambda=\lambda)=e^{-\lambda}\lambda^n/n!$ and
$f_\Lambda(\lambda)=\beta^\alpha\lambda^{\alpha-1}e^{-\beta\lambda}/\Gamma(\alpha)$ for $\lambda>0$.

(b) By the law of total probability,
$$
\Pr(N=n)=\int_0^\infty e^{-\lambda}\frac{\lambda^n}{n!}\cdot
\frac{\beta^\alpha\lambda^{\alpha-1}e^{-\beta\lambda}}{\Gamma(\alpha)}d\lambda
=\frac{\beta^\alpha}{n!\,\Gamma(\alpha)}\int_0^\infty\lambda^{n+\alpha-1}e^{-(\beta+1)\lambda}d\lambda .
$$

(c) The integral is $\Gamma(n+\alpha)/(\beta+1)^{n+\alpha}$, so
$$
\Pr(N=n)=\frac{\Gamma(n+\alpha)}{n!\,\Gamma(\alpha)}\cdot
\Bigl(\frac{\beta}{\beta+1}\Bigr)^{\alpha}\Bigl(\frac{1}{\beta+1}\Bigr)^{n}
=\binom{n+\alpha-1}{n}p^\alpha(1-p)^n,
$$
with $p=\beta/(\beta+1)$, using $\Gamma(n+\alpha)/\Gamma(\alpha)=(n+\alpha-1)\cdots\alpha$ and
$\binom{n+\alpha-1}{n}=\Gamma(n+\alpha)/(n!\Gamma(\alpha))$. This is the negative binomial pmf in its
failure-counting form, with shape $\alpha$ and success probability $p$.

(d) By the tower property, $\mathbb{E}[N]=\mathbb{E}\bigl[\mathbb{E}[N\mid\Lambda]\bigr]=\mathbb{E}[\Lambda]=\alpha/\beta$.
From the negative binomial formula in the failure parametrisation, mean $=r(1-p)/p=\alpha\cdot\frac{1/(\beta+1)}{\beta/(\beta+1)}=\alpha/\beta$.
They agree.

(e) The conditional variance decomposition gives
$$
\operatorname{Var}(N)=\mathbb{E}\bigl[\operatorname{Var}(N\mid\Lambda)\bigr]+\operatorname{Var}\bigl(\mathbb{E}[N\mid\Lambda]\bigr)
=\mathbb{E}[\Lambda]+\operatorname{Var}(\Lambda)=\frac{\alpha}{\beta}+\frac{\alpha}{\beta^2},
$$
which exceeds the mean $\alpha/\beta$ by $\alpha/\beta^2>0$. A Poisson law has variance equal to its mean, so
mixing over an uncertain rate inflates the variance: the counts inherit the variability of $\Lambda$.

*Check:* setting $\alpha=1$ gives $p=\beta/(\beta+1)$ and the geometric failure-count pmf
$p(1-p)^n$, as the mixture of a Poisson with an exponential rate should. ✓

**35.** *(Strategy: take logarithms and differentiate; the sign of one linear factor decides the shape.)*

(a) For $0<x<1$, $\log f(x)=(a-1)\log x+(b-1)\log(1-x)-\log B(a,b)$, so
$$
f'(x)=f(x)\Bigl[\frac{a-1}{x}-\frac{b-1}{1-x}\Bigr]
=\frac{f(x)}{x(1-x)}\bigl[(a-1)(1-x)-(b-1)x\bigr].
$$

(b) Since $f>0$ and $x(1-x)>0$ on $(0,1)$, the sign of $f'$ is the sign of the linear function
$g(x)=(a-1)(1-x)-(b-1)x=(a-1)-x(a+b-2)$. If $a>1$ and $b>1$ then $a+b-2>0$ and $g$ decreases from $a-1>0$ at
$x=0$ to $-(b-1)<0$ at $x=1$, vanishing exactly at $x^\ast=(a-1)/(a+b-2)$. So $f$ increases then decreases: a
unique maximum, with value
$f(x^\ast)=\dfrac{(x^\ast)^{a-1}(1-x^\ast)^{b-1}}{B(a,b)}$.

(c) If $a<1$ and $b<1$ then $a-1<0$ and $b-1<0$, so $g(0)=a-1<0$ and $g(1)=-(b-1)>0$; $g$ is increasing (since
$-(a+b-2)>0$) and vanishes again at the same $x^\ast$. So $f$ decreases then increases: a unique minimum. Also
$f(x)\sim x^{a-1}$ as $x\to0^+$ with $a-1<0$, so $f\to+\infty$; similarly $f\to+\infty$ as $x\to1^-$. The density
is U-shaped.

(d) If $a=1$ and $b>1$ then $g(x)=-(b-1)x<0$ for $x>0$, so $f$ is strictly decreasing. If $a=b=1$, $g\equiv0$ and
$f\equiv1$: the uniform density.

(e) The four shapes and a use for each: **unimodal** (Beta$(2,5)$, a proportion with a most likely value away from
the endpoints); **U-shaped** (Beta$(0.5,0.5)$, allele frequencies under a model that pushes mass to fixation);
**monotone decreasing** (Beta$(1,3)$, a proportion of which we only know an upper bound); **uniform**
(Beta$(1,1)$, total ignorance on $(0,1)$, which is the prior of Bayes and Laplace).

*Check:* at $a=b=2$ the mode is $\tfrac12$ and $f$ is symmetric; at $a=2$, $b=5$ the mode is $1/5$ and $f$ is
right-skewed, consistent with the mean $2/7\approx0.286$ exceeding the mode. ✓

**36.** *(Strategy: one convolution, then complete the square in $x$.)*

(a) By independence, $f_{X+Y}(z)=\int_{\mathbb{R}}f_X(x)f_Y(z-x)dx$, i.e.
$$
f_{X+Y}(z)=\frac{1}{2\pi\sigma_1\sigma_2}\int_{\mathbb{R}}
\exp\Bigl(-\frac{(x-\mu_1)^2}{2\sigma_1^2}-\frac{(z-x-\mu_2)^2}{2\sigma_2^2}\Bigr)dx .
$$

(b) The exponent is $-\tfrac12\bigl[A x^2-2Bx+C\bigr]$ with
$$
A=\frac{1}{\sigma_1^2}+\frac{1}{\sigma_2^2}=\frac{\sigma_1^2+\sigma_2^2}{\sigma_1^2\sigma_2^2},\qquad
B=\frac{\mu_1}{\sigma_1^2}+\frac{z-\mu_2}{\sigma_2^2},\qquad
C=\frac{\mu_1^2}{\sigma_1^2}+\frac{(z-\mu_2)^2}{\sigma_2^2}.
$$
Completing the square, $Ax^2-2Bx+C=A(x-m)^2+C-B^2/A$ with $m=B/A$. So
$$
m=\frac{\mu_1\sigma_2^2+(z-\mu_2)\sigma_1^2}{\sigma_1^2+\sigma_2^2},\qquad
s^2=\frac1A=\frac{\sigma_1^2\sigma_2^2}{\sigma_1^2+\sigma_2^2},
$$
and the exponent is $-\dfrac{(x-m)^2}{2s^2}-\dfrac{C-B^2/A}{2}$, with the second term independent of $x$.

(c) The integral over $x$ is $\int e^{-(x-m)^2/(2s^2)}dx=\sqrt{2\pi}s$, so
$$
f_{X+Y}(z)=\frac{\sqrt{2\pi}s}{2\pi\sigma_1\sigma_2}
\exp\Bigl(-\frac{C-B^2/A}{2}\Bigr).
$$
A short simplification gives $C-B^2/A=\dfrac{(z-\mu_1-\mu_2)^2}{\sigma_1^2+\sigma_2^2}$ and
$\dfrac{s}{\sigma_1\sigma_2}=\dfrac{1}{\sqrt{\sigma_1^2+\sigma_2^2}}$, so
$$
f_{X+Y}(z)=\frac{1}{\sqrt{2\pi(\sigma_1^2+\sigma_2^2)}}\exp\Bigl(-\frac{(z-\mu_1-\mu_2)^2}{2(\sigma_1^2+\sigma_2^2)}\Bigr),
$$
the $\mathcal{N}(\mu_1+\mu_2,\sigma_1^2+\sigma_2^2)$ density.

(d) $m$ is the conditional mean of $X$ given $X+Y=z$, and $s^2=\sigma_1^2\sigma_2^2/(\sigma_1^2+\sigma_2^2)$ is the
corresponding conditional variance — the "harmonic" combination familiar from the precision-additivity formula. The
computation is the two-variable form of the MGF proof of Theorem 8.4(v): there the algebra is multiplication of
exponentials, here it is completing the square, but both show that the exponents add, which is why means and
variances add.

*Check:* with $\mu_1=\mu_2=0$ and $\sigma_1=\sigma_2=1$, the result is $\mathcal{N}(0,2)$, whose variance $2$ is
the sum of the two unit variances. ✓

