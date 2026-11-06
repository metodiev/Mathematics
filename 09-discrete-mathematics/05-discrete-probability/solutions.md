# Discrete Probability — Solutions

> [Discrete Probability](README.md) · Solutions to the 37 problems in [exercises.md](exercises.md)

Each solution names the method, carries out every significant algebraic step, and checks the answer
where a check is available. Decimal answers are rounded at the end, not during the computation. The
common pitfall for each problem is flagged where it is most likely to occur.

## Beginner

**1.** *Strategy: list the atoms and use the uniform formula.*

The space is $\Omega=\{1,2,3,4,5,6\}$ with $\Pr(\{k\})=1/6$. Then
$A=\{2,4,6\}$ and $B=\{2,3,5\}$, so

$$\Pr(A)=\frac36=\frac12,\qquad \Pr(B)=\frac36=\frac12.$$

The union is $A\cup B=\{2,3,4,5,6\}$, five outcomes, so $\Pr(A\cup B)=5/6$. The intersection is
$A\cap B=\{2\}$, so $\Pr(A\cap B)=1/6$.

*Check the addition rule.* $\Pr(A)+\Pr(B)-\Pr(A\cap B)=\frac12+\frac12-\frac16=\frac56$, which matches
$\Pr(A\cup B)$ ✓.

*Independence.* $\Pr(A)\Pr(B)=\frac12\cdot\frac12=\frac14$, while $\Pr(A\cap B)=\frac16$. Since
$\frac16\ne\frac14$, the events are **not** independent. Intuitively, $B$ contains only one even
number ($2$), so knowing $B$ makes $A$ less likely, not equally likely.

*Pitfall.* Do not conclude independence from $\Pr(A)=\Pr(B)$; the product rule is the test.

**2.** *Strategy: the atoms are ordered pairs, not counts of heads.*

The sample space is $\Omega=\{HH,HT,TH,TT\}$, four equally likely outcomes. Exactly one head is
$\{HT,TH\}$, so the probability is $2/4=1/2$. At least one head is $\{HH,HT,TH\}$, so the probability
is $3/4$.

*Why $\{0,1,2\}$ is not uniform.* The description "one head" contains two atoms ($HT$ and $TH$),
"zero heads" contains one ($TT$) and "two heads" contains one ($HH$). The correct probabilities are
$1/4,1/2,1/4$. Treating $\{0,1,2\}$ as uniform would give $1/3$ to each, contradicting the
multiplication principle: the two tosses are independent, and each ordered pair has probability
$1/4$. The uniform formula may be applied only to the atoms of a symmetric model.

**3.** *Strategy: count the relevant cards, using inclusion–exclusion for the union.*

There are $13$ hearts and $4$ kings, with one card (the king of hearts) in both sets. Hence

$$\Pr(\text{heart or king})=\frac{13+4-1}{52}=\frac{16}{52}=\frac{4}{13}.$$

Among the $13$ hearts there are $3$ face cards (jack, queen, king), so
$\Pr(\text{face}\mid\text{heart})=3/13$. There are $12$ face cards in total and $4$ of them are kings,
so $\Pr(\text{king}\mid\text{face})=4/12=1/3$.

*Pitfall.* In the first part, adding $13+4=17$ double-counts the king of hearts. Inclusion–exclusion
corrects it.

**4.** *Strategy: count the $36$ ordered pairs.*

Sums at most $4$: sum $2$ has $1$ representation, sum $3$ has $2$, sum $4$ has $3$; total $6$.
Therefore $\Pr(\text{sum}\le4)=6/36=1/6$.

Product even: the product is odd exactly when both dice are odd. That event has probability
$\frac36\cdot\frac36=\frac14$ by independence, so the product is even with probability
$1-\frac14=\frac34$.

Sum odd: one die is even and the other odd. There are $3\cdot3=9$ ordered pairs with first even and
second odd, and $9$ with first odd and second even, so $18$ outcomes. The sum $7$ has $6$
representations, and every one of them is an odd sum. Therefore

$$\Pr(\text{sum}=7\mid\text{sum odd})=\frac{6}{18}=\frac13.$$

*Check.* The conditional probability is computed in the restricted space of $18$ equally likely
outcomes, not in the original $36$.

**5.** *Strategy: compute the complement, "no six in any roll".*

(a) In four rolls the probability of no six is $(5/6)^4$, so

$$\Pr(\text{at least one six})=1-\left(\frac56\right)^4=1-\frac{625}{1296}=\frac{671}{1296}
\approx0.5177.$$

(b) In one roll of two dice the probability of double-six is $1/36$, so in $24$ rolls

$$\Pr(\text{at least one double-six})=1-\left(\frac{35}{36}\right)^{24}\approx0.4914.$$

The first game is slightly favourable, the second slightly unfavourable, even though $4/6=24/36$.
The expected number of successes is the same in both games ($4\cdot\frac16=24\cdot\frac1{36}=\frac23$),
but the probability of at least one success depends on the number of trials as well as the mean. This
discrepancy is the classical observation attributed to the Chevalier de Méré; it is a warning that
"expected number" and "probability of at least one" are different quantities.

*Pitfall.* Multiplying $24$ by $1/36$ gives the expected count, not the probability.

**6.** *Strategy: count hands as unordered five-element subsets.*

There are $\binom{52}{5}=2{,}598{,}960$ equally likely hands.

(a) All hearts: choose all five cards from the $13$ hearts:

$$\Pr(\text{all hearts})=\frac{\binom{13}{5}}{\binom{52}{5}}
=\frac{1287}{2{,}598{,}960}\approx0.0004952.$$

(b) Exactly one ace: choose one of the $4$ aces and four of the $48$ non-aces:

$$\Pr(\text{exactly one ace})=\frac{\binom41\binom{48}{4}}{\binom{52}{5}}
=\frac{4\cdot194{,}580}{2{,}598{,}960}=\frac{778{,}320}{2{,}598{,}960}\approx0.2995.$$

*Pitfall.* Hands are unordered. Counting ordered five-card sequences counts every hand $5!$ times in
both numerator and denominator, so the ratio is unchanged, but the binomial-coefficient formulation is
less error-prone.

**7.** *Strategy: restrict to the conditioning group and renormalise.*

Let $C$ be coffee and $T$ tea, with $\Pr(C)=0.60$, $\Pr(T)=0.45$, $\Pr(C\cap T)=0.25$. Then

$$\Pr(C\mid T)=\frac{0.25}{0.45}=\frac59\approx0.5556,\qquad
\Pr(T\mid C)=\frac{0.25}{0.60}=\frac5{12}\approx0.4167.$$

By inclusion–exclusion,
$\Pr(C\cup T)=0.60+0.45-0.25=0.80$.

*Independence.* $\Pr(C)\Pr(T)=0.60\cdot0.45=0.27\ne0.25=\Pr(C\cap T)$, so the habits are not
independent. Coffee drinkers are slightly less likely than average to drink tea.

**8.** *Strategy: total probability, then Bayes.*

Let $R$ be red and $A$ the event that urn A is chosen. Then $\Pr(A)=\Pr(A^{\complement})=1/2$,

$$\Pr(R)=\frac12\cdot\frac35+\frac12\cdot\frac15=\frac3{10}+\frac1{10}=\frac25,$$

and

$$\Pr(A\mid R)=\frac{\Pr(R\mid A)\Pr(A)}{\Pr(R)}=\frac{(3/5)(1/2)}{2/5}=\frac{3/10}{2/5}=\frac34.$$

*Check.* The two posterior probabilities sum to $1$: $\Pr(B\mid R)=\frac{(1/5)(1/2)}{2/5}=\frac14$ ✓.
The red ball is three times as likely to have come from A, whose red fraction is three times as large.

**9.** *Strategy: apply the binomial mass function and the formulas for mean and variance.*

With $n=5$, $p=0.3$, $q=0.7$:

$$\Pr(X=2)=\binom52(0.3)^2(0.7)^3=10\cdot0.09\cdot0.343=0.3087.$$

$$\Pr(X\ge1)=1-\Pr(X=0)=1-(0.7)^5=1-0.16807=0.83193.$$

The mean is $np=5\cdot0.3=1.5$, the variance is $np(1-p)=5\cdot0.3\cdot0.7=1.05$, and the standard
deviation is $\sqrt{1.05}\approx1.0247$.

*Pitfall.* The variance is not $p(1-p)$; that is the variance of a single Bernoulli trial.

**10.** *Strategy: use the geometric mass function and tail formula.*

For $T\sim\operatorname{Geom}(0.2)$ and $q=0.8$:

$$\Pr(T=3)=q^2p=(0.8)^2(0.2)=0.128,$$
$$\Pr(T\le3)=1-\Pr(T>3)=1-q^3=1-0.512=0.488,$$
$$\Pr(T>5)=q^5=0.32768.$$

The mean is $1/p=5$, the variance is $q/p^2=0.8/0.04=20$, and the standard deviation is
$\sqrt{20}\approx4.4721$.

*Pitfall.* $\Pr(T\le3)$ is not $p+p^2+p^3$ unless the trials are interpreted correctly; the
complement is shorter. Also $T$ starts at $1$, so $\Pr(T\le3)$ involves three trials, not two.

**11.** *Strategy: compute the first two moments, then use the variance identity.*

$$\mathbb{E}[X]=0(0.1)+1(0.3)+2(0.4)+3(0.2)=0.3+0.8+0.6=1.7.$$

$$\mathbb{E}[X^2]=0^2(0.1)+1^2(0.3)+2^2(0.4)+3^2(0.2)=0.3+1.6+1.8=3.7.$$

Therefore $\operatorname{Var}(X)=3.7-(1.7)^2=3.7-2.89=0.81$, and $\sigma_X=0.9$.

By linearity, $\mathbb{E}[2X+1]=2(1.7)+1=4.4$. By the scaling rule,
$\operatorname{Var}(2X+1)=2^2\operatorname{Var}(X)=4(0.81)=3.24$.

*Check.* $\mathbb{E}[(2X+1)^2]=4\mathbb{E}[X^2]+4\mathbb{E}[X]+1=14.8+6.8+1=22.6$, and
$22.6-(4.4)^2=22.6-19.36=3.24$ ✓.

**12.** *Strategy: expand the square and use linearity.*

Let $\mu=\mathbb{E}[X]$. Then

$$(X-\mu)^2=X^2-2\mu X+\mu^2.$$

Taking expectations,

$$\mathbb{E}[(X-\mu)^2]=\mathbb{E}[X^2]-2\mu\mathbb{E}[X]+\mu^2
=\mathbb{E}[X^2]-2\mu^2+\mu^2=\mathbb{E}[X^2]-\mu^2.$$

For $X\sim\operatorname{Bernoulli}(p)$, the definition gives
$\mathbb{E}[X]=0(1-p)+1(p)=p$ and $\mathbb{E}[X^2]=0^2(1-p)+1^2p=p$. Hence

$$\operatorname{Var}(X)=p-p^2=p(1-p).$$

*Remark.* The identity is valid for every random variable with a finite second moment; no
independence or symmetry is involved.

**13.** *Strategy: use linearity for the mean and independence for the variance.*

Each die has mean $\frac{1+2+3+4+5+6}{6}=3.5$ and variance

$$\mathbb{E}[D^2]-\mathbb{E}[D]^2=\frac{1+4+9+16+25+36}{6}-\left(\frac72\right)^2
=\frac{91}{6}-\frac{49}{4}=\frac{182-147}{12}=\frac{35}{12}.$$

By linearity, $\mathbb{E}[S]=10\cdot3.5=35$. Because the dice are independent, the variances add:

$$\operatorname{Var}(S)=10\cdot\frac{35}{12}=\frac{350}{12}=\frac{175}{6}\approx29.1667,
\qquad \sigma_S\approx5.4006.$$

The number of sixes is $N\sim\operatorname{Bin}(10,1/6)$, so

$$\mathbb{E}[N]=10\cdot\frac16=\frac53\approx1.6667,\qquad
\operatorname{Var}(N)=10\cdot\frac16\cdot\frac56=\frac{50}{36}=\frac{25}{18}\approx1.3889.$$

Independence is needed for $\operatorname{Var}(S)$ and for the binomial variance. The mean
computations use only linearity and would remain valid for dependent dice.

## Intermediate

**14.** *Strategy: inclusion–exclusion for the union, then a direct decomposition for "exactly one".*

Let $M,P,C$ denote the three subjects. The union has size

$$\lvert M\cup P\cup C\rvert=50+40+30-20-15-10+5=80.$$

Hence $\Pr(\text{at least one})=80/100=0.8$ and $\Pr(\text{none})=0.2$.

For exactly one, remove the students who study two or three subjects. The number who study mathematics
only is

$$50-20-15+5=20,$$

because subtracting the $M\cap P$ and $M\cap C$ students removes the triple intersection twice; adding
it back once corrects the count. Similarly,

$$\lvert P\text{ only}\rvert=40-20-10+5=15,\qquad
\lvert C\text{ only}\rvert=30-15-10+5=10.$$

The total is $20+15+10=45$, so the probability is $0.45$.

*Consistency check.* The exactly-two counts are $20-5=15$ (M and P), $15-5=10$ (M and C) and
$10-5=5$ (P and C), totalling $30$. Together with $45$ exactly-one and $5$ all-three students this
accounts for $45+30+5=80$ students ✓. Equivalently,
$45+2(30)+3(5)=120=50+40+30$ ✓.

*Pitfall.* Adding the three single-subject totals and subtracting all pairwise intersections
double-subtracts the triple intersection; the $+5$ is essential.

**15.** *Strategy: total probability with the two disease states, then Bayes.*

Let $D$ be disease, $H=D^{\complement}$, and $+$ a positive test. Then
$\Pr(D)=0.005$, $\Pr(H)=0.995$, $\Pr(+\mid D)=0.98$, $\Pr(-\mid H)=0.96$, so
$\Pr(+\mid H)=0.04$ and $\Pr(-\mid D)=0.02$.

*Positive predictive value.*

$$\Pr(D\mid+)=\frac{0.005\cdot0.98}{0.005\cdot0.98+0.995\cdot0.04}
=\frac{0.0049}{0.0049+0.0398}=\frac{0.0049}{0.0447}\approx0.1096.$$

*Negative predictive value.*

$$\Pr(H\mid-)=\frac{0.995\cdot0.96}{0.995\cdot0.96+0.005\cdot0.02}
=\frac{0.9552}{0.9552+0.0001}=\frac{0.9552}{0.9553}\approx0.9999.$$

A positive result raises the probability of disease from $0.5\%$ to about $11\%$, which is a large
relative increase but still a small absolute probability. A negative result is far more informative,
because most people are healthy to begin with. The asymmetry is the base-rate effect; both numbers are
correct conditional probabilities with different conditioning events.

**16.** *Strategy: enumerate the four equally likely outcomes and test each product.*

The outcomes are $HH,HT,TH,TT$. The events are $A=\{HH,HT\}$, $B=\{HH,TH\}$ and
$C=\{HH,TT\}$, each of probability $1/2$. Their pairwise intersections are all $\{HH\}$:

$$\Pr(A\cap B)=\Pr(A\cap C)=\Pr(B\cap C)=\frac14
=\frac12\cdot\frac12.$$

Hence the three events are pairwise independent. But

$$A\cap B\cap C=\{HH\},\qquad \Pr(A\cap B\cap C)=\frac14\ne\frac18
=\Pr(A)\Pr(B)\Pr(C).$$

Only the triple product identity fails; all three pairwise identities hold. This is exactly the
distinction between pairwise and mutual independence.

**17.** *Strategy: regroup the probabilities by the value of $Y$, then compute moments.*

$Y=\lvert X\rvert$ takes the values $0,1,2$. The value $0$ arises only from $X=0$, so
$\Pr(Y=0)=0.3$. The value $1$ arises from $X=-1$ and $X=1$, so
$\Pr(Y=1)=0.2+0.3=0.5$. The value $2$ arises from $X=2$, so $\Pr(Y=2)=0.2$. Check:
$0.3+0.5+0.2=1$ ✓.

For $X$:

$$\mathbb{E}[X]=(-1)(0.2)+0(0.3)+1(0.3)+2(0.2)=-0.2+0.3+0.4=0.5,$$
$$\mathbb{E}[X^2]=(1)(0.2)+0+1(0.3)+4(0.2)=0.2+0.3+0.8=1.3,$$
$$\operatorname{Var}(X)=1.3-(0.5)^2=1.3-0.25=1.05.$$

For $Y$:

$$\mathbb{E}[Y]=0(0.3)+1(0.5)+2(0.2)=0.9,\qquad
\mathbb{E}[Y^2]=0+1(0.5)+4(0.2)=1.3.$$

The equality $\mathbb{E}[Y^2]=\mathbb{E}[X^2]$ holds because $Y^2=\lvert X\rvert^2=X^2$ for every
outcome, so the two random variables are identical; no separate computation is needed.

*Pitfall.* $\mathbb{E}[Y]\ne\lvert\mathbb{E}[X]\rvert$ in general: here $0.9\ne0.5$. Taking absolute
values does not commute with expectation.

**18.** *Strategy: count the subset of four items, then compare with the with-replacement model.*

There are $\binom{20}{4}=4845$ equally likely four-element subsets. Exactly two defective means
choosing $2$ of the $5$ defective and $2$ of the $15$ non-defective:

$$\Pr(\text{two defective})=\frac{\binom52\binom{15}{2}}{\binom{20}{4}}
=\frac{10\cdot105}{4845}=\frac{1050}{4845}\approx0.2167.$$

The binomial model with $n=4$ and $p=5/20=0.25$ gives

$$\binom42(0.25)^2(0.75)^2=6\cdot0.0625\cdot0.5625=0.2109375\approx0.2109.$$

The hypergeometric probability is slightly larger. Without replacement the draws are negatively
correlated: a defective item removed on the first draw lowers the defective proportion for later
draws, so the count is less variable than a binomial count (the finite-population correction is
$(N-n)/(N-1)=16/19<1$). A less variable distribution puts more mass near its mean of $1$, raising
both $\Pr(1)$ and $\Pr(2)$ while lowering the extreme tails.

**19.** *Strategy: indicators and symmetry.*

For $i=1,\dots,n$, let $F_i$ be the event that object $i$ is fixed and let
$F=\sum_{i=1}^n\mathbf{1}_{F_i}$. In a uniformly random permutation, object $i$ is equally likely to
occupy any of the $n$ positions, so $\Pr(F_i)=1/n$. Therefore

$$\mathbb{E}[F]=\sum_{i=1}^n\Pr(F_i)=n\cdot\frac1n=1.$$

The expectation does not depend on $n$, even though the distribution of $F$ does.

For $n=5$, the number of derangements is $!5=44$, so
$\Pr(F=0)=44/120=11/30$ and

$$\Pr(F\ge1)=1-\frac{44}{120}=\frac{76}{120}=\frac{19}{30}\approx0.6333.$$

*Remark.* The indicators $F_i$ are dependent — if $n-1$ objects are fixed, so is the last — but
linearity does not care, which is the point of the method.

**20.** *Strategy: exchange the order of summation.*

(a) For each outcome $\omega$, $X(\omega)$ equals the number of integers $k\ge1$ with
$k\le X(\omega)$. Hence

$$\mathbb{E}[X]=\sum_\omega X(\omega)p(\omega)
=\sum_\omega\sum_{k=1}^{X(\omega)}p(\omega)
=\sum_{k\ge1}\sum_{\omega:\,X(\omega)\ge k}p(\omega)
=\sum_{k\ge1}\Pr(X\ge k).$$

The interchange is legitimate because $X$ is nonnegative and the sum over $\omega$ is finite.

(b) For $T\sim\operatorname{Geom}(p)$, $\Pr(T>k)=(1-p)^k$ for $k\ge0$, and $T\ge1$ is automatic, so
$\Pr(T\ge k)=\Pr(T>k-1)=(1-p)^{k-1}$. Therefore

$$\mathbb{E}[T]=\sum_{k\ge1}\Pr(T\ge k)=\sum_{k\ge1}(1-p)^{k-1}=\frac1p.$$

(c) For $X$ uniform on $\{1,\dots,n\}$, $\Pr(X\ge k)=(n-k+1)/n$ for $1\le k\le n$ and $0$ afterwards.
Thus

$$\mathbb{E}[X]=\sum_{k=1}^{n}\frac{n-k+1}{n}
=\frac{n+(n-1)+\cdots+1}{n}=\frac{n(n+1)/2}{n}=\frac{n+1}{2},$$

which is the correct mean of a uniform variable on $\{1,\dots,n\}$ ✓.

**21.** *Strategy: evaluate the Poisson mass function, using $e^{-2.5}$ as a common factor.*

With $\lambda=2.5$ and $e^{-2.5}=0.0820850$:

$$\Pr(X=0)=e^{-2.5}=0.082085,$$
$$\Pr(X\ge1)=1-\Pr(X=0)=0.917915,$$
$$\Pr(X=3)=e^{-2.5}\frac{2.5^3}{3!}=0.0820850\cdot\frac{15.625}{6}=0.213763.$$

For the lower tail,

$$\Pr(X\le3)=e^{-2.5}\left(1+2.5+\frac{2.5^2}{2}+\frac{2.5^3}{6}\right)
=0.0820850\,(1+2.5+3.125+2.604167)=0.757576.$$

The mean and variance are both $\lambda=2.5$.

*Check.* $\Pr(X\ge1)+\Pr(X=0)=0.917915+0.082085=1$ ✓. Also $\Pr(X\le3)=0.7576$ and
$\Pr(X\ge4)=0.2424$ sum to $1$ ✓.

**22.** *Strategy: exact birthday product, then the exponential bound.*

The exact no-collision probability is

$$\prod_{i=0}^{49}\left(1-\frac{i}{1000}\right)=\frac{1000\cdot999\cdots951}{1000^{50}}.$$

Numerically this is $0.287731\ldots$, so the exact collision probability is
$1-0.287731=0.712269\ldots\approx0.7123$.

The approximation is

$$1-\exp\left(-\frac{50\cdot49}{2\cdot1000}\right)=1-e^{-1.225}=1-0.293758=0.706242\approx0.7062.$$

Since $1-x\le e^{-x}$ for $x\ge0$,

$$\Pr(\text{no collision})=\prod_i\left(1-\frac{i}{m}\right)\le\prod_i e^{-i/m}
=\exp\left(-\frac{n(n-1)}{2m}\right).$$

Therefore $\Pr(\text{collision})\ge1-\exp(-n(n-1)/(2m))$: the approximation is a **lower bound** on the
true collision probability. The exact value $0.7123$ indeed exceeds $0.7062$. The gap is
$0.0060$, about $0.8$ percentage points.

*Pitfall.* The approximation is not an equality; it understates the risk slightly. It is conservative,
which is the safe direction for security estimates.

**23.** *Strategy: evaluate the harmonic formula and check one case against the defining sum.*

The harmonic numbers are $H_1=1$, $H_2=1.5$, $H_3=1.833333$, $H_4=2.083333$, $H_5=2.283333$. Then

| $n$ | $2(n+1)H_n-4n$ | Worst case $\binom n2$ |
|---|---|---|
| 1 | $0$ | 0 |
| 2 | $1$ | 1 |
| 3 | $2.6667$ | 3 |
| 4 | $4.8333$ | 6 |
| 5 | $7.4$ | 10 |

For $n=5$, the direct sum is

$$\sum_{d=1}^{4}(5-d)\frac{2}{d+1}=4\cdot\frac22+3\cdot\frac23+2\cdot\frac24+1\cdot\frac25
=4+2+1+0.4=7.4,$$

which matches ✓. The expected count is $74\%$ of the worst case at $n=5$; the ratio decreases as $n$
grows.

**24.** *Strategy: $nH_n$ for the exact mean; invert a tail bound for the $90\%$ statement.*

For $n=5$, $\mathbb{E}[T]=5H_5=5(2.283333)=11.4167$.
For $n=10$, $\mathbb{E}[T]=10H_{10}=10(2.928968)=29.2897$.

The bound $\Pr(T>t)\le ne^{-t/n}$ is not exact; it is a union-bound estimate. Setting
$ne^{-t/n}=0.1$ gives

$$e^{-t/10}=0.01,\qquad t=10\ln100=46.0517.$$

So the bound equals $0.1$ at $t=46.0517$; since $t$ must be an integer, $47$ draws make the bound at
most $0.1$. The true probability at that $t$ is below the bound, so $90\%$ confidence is conservative.
One should not report "$90\%$ chance" from the bound without saying it is a bound.

**25.** *Strategy: solve $\pi P=\pi$ and the first-step equations.*

Let $\pi=(\pi_1,\pi_2)$. The stationarity equations are

$$\pi_1=0.9\pi_1+0.4\pi_2,\qquad \pi_2=0.1\pi_1+0.6\pi_2,\qquad \pi_1+\pi_2=1.$$

The first equation gives $0.1\pi_1=0.4\pi_2$, so $\pi_1=4\pi_2$. With $\pi_1+\pi_2=1$,
$5\pi_2=1$, hence $\pi_2=0.2$ and $\pi_1=0.8$. Thus $\pi=(0.8,0.2)$.

*Hitting time from $1$ to $2$.* Let $h_1$ be the expected time, with $h_2=0$. Then
$h_1=1+0.9h_1+0.1\cdot0$, so $0.1h_1=1$ and $h_1=10$ days.

*Mean return time to $1$.* It is $1/\pi_1=1/0.8=1.25$. Verify directly: from state $1$, the chain
returns immediately with probability $0.9$, or moves to $2$ with probability $0.1$ and then needs
$h_{2\to1}$ steps. Since $h_2=1+0.6h_2$, $h_2=2.5$, the return time is
$1+0.1(2.5)=1.25$ ✓.

## Advanced

**26.** *Strategy: two independent derivations, then compare.*

**(a) Tail sum and factorial moment.**

For $k\ge0$, $\Pr(T>k)=(1-p)^k$. By the tail-sum formula,

$$\mathbb{E}[T]=\sum_{k\ge0}\Pr(T>k)=\sum_{k\ge0}(1-p)^k=\frac1p.$$

Put $q=1-p$. The factorial moment is

$$\mathbb{E}[T(T-1)]=\sum_{k\ge2}k(k-1)q^{k-1}p
=pq\sum_{k\ge2}k(k-1)q^{k-2}=pq\cdot\frac{2}{(1-q)^3}=\frac{2q}{p^2},$$

using the third series identity of §8.5. Then

$$\operatorname{Var}(T)=\mathbb{E}[T(T-1)]+\mathbb{E}[T]-\mathbb{E}[T]^2
=\frac{2q}{p^2}+\frac1p-\frac1{p^2}
=\frac{2q+p-1}{p^2}
=\frac{q}{p^2},$$

because $2q+p-1=2(1-p)+p-1=1-p=q$.

**(b) First-step equations.**

After one draw, either the first trial succeeds (probability $p$, and $T=1$) or it fails (probability
$q$) and the remaining waiting time is a fresh copy of $T$. Hence

$$\mathbb{E}[T]=p\cdot1+q\,\mathbb{E}[T+1]=p+q(\mathbb{E}[T]+1).$$

Since $p+q=1$, this gives $p\mathbb{E}[T]=1$, so $\mathbb{E}[T]=1/p$.

For the second moment, condition on the first trial:

$$\mathbb{E}[T^2]=p\cdot1^2+q\,\mathbb{E}[(T+1)^2]
=p+q\bigl(1+2\mathbb{E}[T]+\mathbb{E}[T^2]\bigr).$$

Substituting $\mathbb{E}[T]=1/p$ and moving the $q\mathbb{E}[T^2]$ term to the left,

$$p\mathbb{E}[T^2]=p+q+\frac{2q}{p}=1+\frac{2q}{p},$$

so $\mathbb{E}[T^2]=1/p+2q/p^2$. Therefore

$$\operatorname{Var}(T)=\frac1p+\frac{2q}{p^2}-\frac1{p^2}
=\frac{p+2q-1}{p^2}=\frac{q}{p^2}.$$

Both routes agree. $\blacksquare$

*Check.* For $p=1/6$: mean $6$, variance $(5/6)\cdot36=30$, matching Example 9.5 ✓.

**27.** *Strategy: expand the variance of the sum of indicators and examine each covariance.*

Let $X=\sum_{i=1}^{n}I_i$ with $I_i=\mathbf{1}_{A_i}$. Each $I_i$ is Bernoulli$(p)$, so
$\operatorname{Var}(I_i)=p(1-p)$, and

$$\operatorname{Var}(X)=\sum_{i=1}^{n}\operatorname{Var}(I_i)
+2\sum_{1\le i<j\le n}\operatorname{Cov}(I_i,I_j).$$

For $i\ne j$,

$$\operatorname{Cov}(I_i,I_j)=\mathbb{E}[I_iI_j]-\mathbb{E}[I_i]\mathbb{E}[I_j]
=\Pr(A_i\cap A_j)-p^2.$$

If the trials are mutually independent, $\Pr(A_i\cap A_j)=p^2$, so every covariance is zero and

$$\operatorname{Var}(X)=\sum_{i=1}^{n}p(1-p)=np(1-p).$$

*Does mutual independence matter?* For **this** computation, no: pairwise independence already gives
$\Pr(A_i\cap A_j)=p^2$ for every pair, which is all that the covariance terms require. The variance
formula therefore holds under the weaker hypothesis of pairwise independence (and even under the
hypothesis that all pairwise covariances vanish).

What does require mutual independence is the *mass function*
$\Pr(X=k)=\binom{n}{k}p^k(1-p)^{n-k}$. Its derivation multiplies the probabilities of a full pattern
of $k$ successes and $n-k$ failures, which is an $n$-fold intersection. Pairwise independence does not
determine that intersection; the two-coin example of §7.5 has pairwise independent events whose triple
intersection has the wrong probability. Without mutual independence, $X$ need not be binomial, even
though its mean and variance may still equal $np$ and $np(1-p)$.

**28.** *Strategy: factor the binomial coefficient into pieces with known limits.*

For $0\le k\le n$,

$$\Pr(X_n=k)=\binom{n}{k}\left(\frac{\lambda}{n}\right)^k
\left(1-\frac{\lambda}{n}\right)^{n-k}.$$

Write the binomial coefficient as
$\binom{n}{k}=\frac{n(n-1)\cdots(n-k+1)}{k!}$ and split:

$$\Pr(X_n=k)=
\underbrace{\prod_{j=0}^{k-1}\left(1-\frac{j}{n}\right)}_{A_n}
\cdot\frac{\lambda^k}{k!}\cdot
\underbrace{\left(1-\frac{\lambda}{n}\right)^{n}}_{B_n}
\cdot
\underbrace{\left(1-\frac{\lambda}{n}\right)^{-k}}_{C_n}.$$

Now take $n\to\infty$ with $k$ and $\lambda$ fixed.

1. $A_n$ has exactly $k$ factors, and for each fixed $j$ the factor $1-j/n\to1$. A product of
   finitely many factors tending to $1$ tends to $1$.
2. $\lambda^k/k!$ does not depend on $n$.
3. $B_n=(1-\lambda/n)^n\to e^{-\lambda}$, the standard limit for the exponential.
4. $C_n=(1-\lambda/n)^{-k}\to1^{-k}=1$, because $\lambda/n\to0$ and the exponent is fixed.

Multiplying the limits,

$$\lim_{n\to\infty}\Pr(X_n=k)=1\cdot\frac{\lambda^k}{k!}\cdot e^{-\lambda}\cdot1
=e^{-\lambda}\frac{\lambda^k}{k!}.$$

The condition that $\lambda$ is fixed is used in steps 1 and 4: it ensures that the number of factors in
$A_n$ is fixed and that $\lambda/n\to0$ at a rate independent of $k$. If $\lambda$ were allowed to grow
with $n$, the limit could be different (for example, the distribution could concentrate away from a
fixed Poisson law). $\blacksquare$

*Remark.* The convergence is pointwise in $k$; it is not a statement that the distributions are equal
for finite $n$. The error is of order $\lambda^2/n$ uniformly over $k$ in a suitable range.

**29.** *Strategy: decompose the collection into independent geometric stages.*

(a) Let $T_k$ be the number of draws needed to go from $k-1$ collected types to $k$ collected types.
When $k-1$ types are collected, $n-k+1$ types are missing, so the probability that the next draw is new
is $p_k=(n-k+1)/n$. Thus $T_k\sim\operatorname{Geom}(p_k)$, and

$$\mathbb{E}[T_k]=\frac1{p_k}=\frac{n}{n-k+1}.$$

The total is $T=T_1+\cdots+T_n$, so

$$\mathbb{E}[T]=\sum_{k=1}^{n}\frac{n}{n-k+1}
=n\sum_{j=1}^{n}\frac1j=nH_n.$$

(b) For a geometric variable with parameter $p_k$,
$\operatorname{Var}(T_k)=(1-p_k)/p_k^2$. Here

$$1-p_k=\frac{k-1}{n},\qquad p_k^2=\frac{(n-k+1)^2}{n^2},$$

so

$$\operatorname{Var}(T_k)=\frac{(k-1)/n}{(n-k+1)^2/n^2}
=\frac{n(k-1)}{(n-k+1)^2}.$$

The stages are independent because the draws are independent, so the variances add:

$$\operatorname{Var}(T)=\sum_{k=1}^{n}\frac{n(k-1)}{(n-k+1)^2}.$$

Put $j=n-k+1$, so $k-1=n-j$ and $j$ runs from $n$ down to $1$:

$$\operatorname{Var}(T)=n\sum_{j=1}^{n}\frac{n-j}{j^2}
=n^2\sum_{j=1}^{n}\frac1{j^2}-n\sum_{j=1}^{n}\frac1j
=n^2H_n^{(2)}-nH_n.$$

(c) For $n=4$, $H_4=1+\frac12+\frac13+\frac14=\frac{25}{12}=2.083333$ and
$H_4^{(2)}=1+\frac14+\frac19+\frac1{16}=\frac{205}{144}=1.423611$. Thus

$$\mathbb{E}[T]=4\cdot\frac{25}{12}=\frac{25}{3}\approx8.3333,$$

and

$$\operatorname{Var}(T)=16\cdot\frac{205}{144}-4\cdot\frac{25}{12}
=\frac{205}{9}-\frac{25}{3}=\frac{205-75}{9}=\frac{130}{9}\approx14.4444.$$

The standard deviation is $\sqrt{130}/3\approx3.8006$.

**30.** *Strategy: reduce the comparison event to the first pivot in an interval.*

(a) Fix $i<j$ and let $S=\{i,i+1,\dots,j\}$, of size $j-i+1$. Until a pivot is chosen from $S$, all
elements of $S$ stay in the same subarray. Pivots are chosen uniformly at random within their current
subarray, so the first element of $S$ to be chosen as a pivot is uniformly distributed over $S$: this
is the standard "first among a symmetric subset" argument, and it can be proved by conditioning on the
sequence of pivot choices and noting that the relative order of the elements of $S$ in that sequence is
uniform.

If the first pivot from $S$ is some $m$ with $i<m<j$, then $i$ goes to the left part and $j$ to the
right part, and they are never compared. If the first pivot is $i$, then $i$ is compared with every
element of its subarray, including $j$; the same happens if the first pivot is $j$. Hence

$$\Pr(i,j\text{ compared})=\Pr(\text{first pivot from }S\text{ is }i\text{ or }j)
=\frac{2}{j-i+1}.$$

(b) By linearity, with $C_n$ the total comparisons,

$$\mathbb{E}[C_n]=\sum_{1\le i<j\le n}\Pr(i,j\text{ compared})
=\sum_{1\le i<j\le n}\frac{2}{j-i+1}.$$

For a fixed distance $d=j-i$, there are $n-d$ pairs, so

$$\mathbb{E}[C_n]=\sum_{d=1}^{n-1}(n-d)\frac{2}{d+1}.$$

Put $k=d+1$:

$$\mathbb{E}[C_n]=2\sum_{k=2}^{n}\frac{n-k+1}{k}
=2\left((n+1)\sum_{k=2}^{n}\frac1k-\sum_{k=2}^{n}1\right)
=2\bigl((n+1)(H_n-1)-(n-1)\bigr).$$

Expanding,

$$2(n+1)H_n-2(n+1)-2(n-1)=2(n+1)H_n-4n.$$

(c) Since $H_n\le1+\ln n$ (compare $\sum_{k=1}^n1/k$ with $1+\int_1^n dx/x$),

$$\mathbb{E}[C_n]\le2(n+1)(1+\ln n)-4n
=2n\ln n+2\ln n+2-2n\le2n\ln n+2n,$$

where the last inequality uses $2\ln n+2\le2n$ for $n\ge1$. The worst case is
$\binom n2=\frac{n(n-1)}2=\Theta(n^2)$, so the expected count is asymptotically much smaller.

**31.** *Strategy: solve the stationarity equations, compute powers, then diagnose periodicity.*

(a) The equations $\pi P=\pi$ are

$$\pi_1=\tfrac12\pi_2,\qquad \pi_2=\pi_1+\pi_3,\qquad \pi_3=\tfrac12\pi_2.$$

Thus $\pi_1=\pi_3$ and $\pi_2=2\pi_1$. With $\pi_1+\pi_2+\pi_3=1$,
$4\pi_1=1$, so $\pi=(1/4,1/2,1/4)$.

(b) Direct matrix multiplication:

$$P^2=\begin{pmatrix}
0.5&0&0.5\\
0&1&0\\
0.5&0&0.5
\end{pmatrix},\qquad
P^3=P^2P=\begin{pmatrix}
0&1&0\\
0.5&0&0.5\\
0&1&0
\end{pmatrix}=P.$$

So $P^n=P$ for odd $n$ and $P^n=P^2$ for even $n\ge2$.

(c) Let $h_i$ be the expected time to reach state $1$, with $h_1=0$. Then

$$h_2=1+\tfrac12h_1+\tfrac12h_3=1+\tfrac12h_3,$$
$$h_3=1+h_2.$$

Substituting the second into the first, $h_2=1+\tfrac12(1+h_2)=\tfrac32+\tfrac12h_2$, so
$h_2=3$ and $h_3=4$.

(d) From state $2$, returns to state $2$ occur only at even times: the chain alternates between the
set $\{1,3\}$ and state $2$. The period is $2$. Consequently $P^n$ alternates between $P$ and $P^2$
and has no limit, although the stationary distribution is unique. For convergence one needs
aperiodicity in addition to irreducibility; the weather chain of §7.12 has both properties, this chain
does not.

*Pitfall.* Uniqueness of $\pi$ does not imply convergence of $P^n$. It implies that if $P^n$ converges,
the limit must have rows $\pi$, but convergence itself is a separate hypothesis.

**32.** *Strategy: group outcomes, then use the definition of expectation twice.*

(a) Group the outcomes by the value of $X$:

$$\mathbb{E}[g(X)]=\sum_{\omega\in\Omega}g(X(\omega))\Pr(\{\omega\})
=\sum_x\sum_{\omega:X(\omega)=x}g(x)\Pr(\{\omega\})
=\sum_x g(x)\Pr(X=x)=\sum_x g(x)p_X(x).$$

The inner sum is $g(x)$ times the total probability of the set $\{X=x\}$.

(b) For each outcome,

$$\mathbb{E}[X+Y]=\sum_\omega(X(\omega)+Y(\omega))p(\omega)
=\sum_\omega X(\omega)p(\omega)+\sum_\omega Y(\omega)p(\omega)
=\mathbb{E}[X]+\mathbb{E}[Y].$$

No property of the joint distribution is used; the identity is termwise.

(c) Let $X$ be uniform on $\{-1,1\}$ and let $Y=X$. Then
$\mathbb{E}[X]=\frac12(-1)+\frac12(1)=0$ and $\mathbb{E}[Y]=0$. But $XY=X^2=1$ always, so
$\mathbb{E}[XY]=1$, while $\mathbb{E}[X]\mathbb{E}[Y]=0$. The variables are perfectly dependent
($Y=X$), and the product expectation is not the product of expectations.

**33.** *Strategy: apply each inequality with the correct threshold, then compute the exact tail.*

For $X\sim\operatorname{Bin}(100,0.5)$, $\mathbb{E}[X]=50$ and $\operatorname{Var}(X)=25$.

(a) Markov, with $X\ge0$ and $a=70$:

$$\Pr(X\ge70)\le\frac{50}{70}=\frac57\approx0.7143.$$

(b) Chebyshev, with $a=20$:

$$\Pr(\lvert X-50\rvert\ge20)\le\frac{25}{400}=\frac1{16}=0.0625.$$

(c) The exact value, from the binomial sum
$2^{-100}\sum_{k=70}^{100}\binom{100}{k}$, is

$$\Pr(X\ge70)=3.925\times10^{-5}.$$

Chebyshev is about $1600$ times larger than the exact value; Markov is about $18000$ times larger.
Both are valid but very loose. Markov uses only the mean and is one-sided; Chebyshev uses the variance
and controls both tails. The binomial is strongly concentrated: $70$ is four standard deviations above
the mean ($z=4$), and Chebyshev's bound at $z=4$ is $1/z^2=1/16$, which cannot capture the exponential
decay of the binomial tail.

*Remark.* The exact tail can be obtained from a normal approximation with a continuity correction as
well, but the exact binomial sum is preferable when it is computable.

## Challenge

**34.** *Strategy: compute the exact product at the two integers around the threshold, then justify the
approximation.*

(a) The collision probability is
$1-\prod_{i=0}^{n-1}(1-i/365)$. Direct computation gives

$$\Pr(\text{collision at }n=22)=1-\prod_{i=0}^{21}\left(1-\frac{i}{365}\right)
=1-0.524305=0.475695,$$

$$\Pr(\text{collision at }n=23)=1-\prod_{i=0}^{22}\left(1-\frac{i}{365}\right)
=1-0.492703=0.507297.$$

The probability is strictly increasing in $n$ for $n\le365$: if $P_n$ is the no-collision probability,

$$P_{n+1}=\left(1-\frac{n}{365}\right)P_n<P_n,$$

so the collision probability $1-P_n$ increases. Hence $n=22$ is below $1/2$, $n=23$ is above, and
$23$ is the smallest integer with the required property.

(b) Take logarithms of the no-collision product:

$$\ln P_n=\sum_{i=0}^{n-1}\ln\left(1-\frac{i}{m}\right)
=-\sum_{i=0}^{n-1}\frac{i}{m}+O\left(\frac{n^3}{m^2}\right)
=-\frac{n(n-1)}{2m}+O\left(\frac{n^3}{m^2}\right).$$

Setting $\ln P_n=\ln(1/2)$ and ignoring the error gives

$$\frac{n(n-1)}{2m}=\ln2,\qquad n(n-1)=2m\ln2.$$

The positive root of $n^2-n-2m\ln2=0$ is
$n=\frac{1+\sqrt{1+8m\ln2}}{2}\approx\sqrt{2m\ln2}$ for large $m$. For $m=365$,
$\sqrt{730\ln2}=\sqrt{505.99}=22.49$. For $m=2^{32}$,
$\sqrt{2\cdot2^{32}\ln2}=\sqrt{5.949\times10^9}=77{,}162.7$, so about $77{,}163$.

(c) The approximation is not exact because $\ln(1-x)=-x-x^2/2-\cdots$ has negative correction terms;
dropping them makes the exponent less negative, hence makes $P_n$ appear larger and the collision
probability appear smaller. Indeed $1-x\le e^{-x}$ gives

$$\Pr(\text{collision})\ge1-\exp\left(-\frac{n(n-1)}{2m}\right),$$

so the approximation is a **lower bound** on the collision probability at every integer $n$. At
$n=22$ it gives $0.4688$ (true $0.4757$), and at $n=23$ it gives $0.5000$ (true $0.5073$). Because it
understates the probability, it can only overstate the number of people needed: the smallest integer
at which the approximation reaches $1/2$ is an upper bound for the true threshold. Here that integer is
$23$, and the exact computation confirms $23$, so the error does not change the answer. One should
still verify the integers adjacent to the approximate threshold rather than trust the approximation
alone.

**35.** *Strategy: express the tail event as a union of "type missing", apply inclusion–exclusion, then
sum over $t$.*

(a) After $t$ draws, let $M_i$ be the event that type $i$ has not appeared. Then
$\{T>t\}=\bigcup_{i=1}^{3}M_i$. For a nonempty set $S$ of types,
$\bigcap_{i\in S}M_i$ is the event that none of the types in $S$ appears in $t$ draws; each draw
avoids $S$ with probability $1-p_S$, where $p_S=\sum_{i\in S}p_i$. By independence across draws,

$$\Pr\left(\bigcap_{i\in S}M_i\right)=(1-p_S)^t.$$

Inclusion–exclusion gives

$$\Pr(T>t)=\sum_{\varnothing\ne S}(-1)^{\lvert S\rvert+1}(1-p_S)^t.$$

Using $\mathbb{E}[T]=\sum_{t\ge0}\Pr(T>t)$ and summing the geometric series in $t$,

$$\mathbb{E}[T]=\sum_{\varnothing\ne S}(-1)^{\lvert S\rvert+1}\sum_{t\ge0}(1-p_S)^t
=\sum_{\varnothing\ne S}\frac{(-1)^{\lvert S\rvert+1}}{p_S}.$$

Here every $p_S>0$, so the series converges.

(b) The nonempty subsets and their probabilities are:

| $S$ | $p_S$ | $1/p_S$ | sign |
|---|---|---|---|
| $\{1\}$ | $1/2$ | $2$ | $+$ |
| $\{2\}$ | $1/3$ | $3$ | $+$ |
| $\{3\}$ | $1/6$ | $6$ | $+$ |
| $\{1,2\}$ | $5/6$ | $6/5=1.2$ | $-$ |
| $\{1,3\}$ | $2/3$ | $3/2=1.5$ | $-$ |
| $\{2,3\}$ | $1/2$ | $2$ | $-$ |
| $\{1,2,3\}$ | $1$ | $1$ | $+$ |

Therefore

$$\mathbb{E}[T]=(2+3+6)-(1.2+1.5+2)+1=11-4.7+1=7.3.$$

(c) Let $E_S$ be the expected additional draws when the set $S$ of types has been collected, with
$E_{\{1,2,3\}}=0$. The first-step equations are
$E_S=1+\sum_i p_iE_{S\cup\{i\}}$, where $S\cup\{i\}=S$ if $i\in S$.

*Singleton missing:*
$E_{\{1,2\}}=1+\frac56E_{\{1,2\}}$, so $E_{\{1,2\}}=6$.
$E_{\{1,3\}}=1+\frac23E_{\{1,3\}}$, so $E_{\{1,3\}}=3$.
$E_{\{2,3\}}=1+\frac12E_{\{2,3\}}$, so $E_{\{2,3\}}=2$.

*Two missing:*

$$E_{\{1\}}=1+\frac12E_{\{1\}}+\frac13E_{\{1,2\}}+\frac16E_{\{1,3\}}
=1+\frac12E_{\{1\}}+2+\frac12,$$

so $\frac12E_{\{1\}}=3.5$ and $E_{\{1\}}=7$.

$$E_{\{2\}}=1+\frac13E_{\{2\}}+\frac12E_{\{1,2\}}+\frac16E_{\{2,3\}}
=1+\frac13E_{\{2\}}+3+\frac13,$$

so $\frac23E_{\{2\}}=\frac{13}{3}$ and $E_{\{2\}}=6.5$.

$$E_{\{3\}}=1+\frac16E_{\{3\}}+\frac12E_{\{1,3\}}+\frac13E_{\{2,3\}}
=1+\frac16E_{\{3\}}+1.5+\frac23,$$

so $\frac56E_{\{3\}}=\frac{19}{6}$ and $E_{\{3\}}=3.8$.

*Nothing collected:*

$$E_{\varnothing}=1+\frac12(7)+\frac13(6.5)+\frac16(3.8)
=1+3.5+2.1667+0.6333=7.3.$$

This matches (b) ✓. The unequal probabilities make the answer larger than the equal-probability value
$3H_3=3\cdot1.8333=5.5$, because the rare type ($p=1/6$) dominates the waiting time.

**36.** *Strategy: indicators for the empty bins; a union bound plus a binomial estimate for the load.*

(a) For each bin $i$, let $E_i$ be the event that bin $i$ is empty. The $n$ balls avoid bin $i$ with
probability $(1-1/n)$ each, independently, so

$$\Pr(E_i)=\left(1-\frac1n\right)^n.$$

The number of empty bins is $\sum_{i=1}^n\mathbf{1}_{E_i}$, hence

$$\mathbb{E}[\text{empty}]=n\left(1-\frac1n\right)^n.$$

For $n=20$ this is $20(19/20)^{20}=20(0.358486)=7.1697$. As $n\to\infty$,
$(1-1/n)^n\to e^{-1}$, so the expected number of empty bins is asymptotic to $n/e$.

(b) Let $L_i$ be the load of bin $i$. Then $L_i\sim\operatorname{Bin}(n,1/n)$, and
$\{L\ge k\}=\bigcup_i\{L_i\ge k\}$. By the union bound,

$$\Pr(L\ge k)\le n\Pr(L_1\ge k).$$

For $k\ge1$,

$$\Pr(L_1\ge k)\le\binom{n}{k}\left(\frac1n\right)^k
\le\left(\frac{en}{k}\right)^k\frac1{n^k}=\left(\frac{e}{k}\right)^k,$$

using $\binom nk\le(en/k)^k$. Hence

$$\Pr(L\ge k)\le n\left(\frac{e}{k}\right)^k.$$

Take $k=\lceil3\ln n\rceil$, so $k\ge3\ln n$. Then

$$\Pr(L\ge k)\le n\left(\frac{e}{3\ln n}\right)^{3\ln n}.$$

Write $L_0=\ln n$. The logarithm of the right-hand side is

$$L_0+3L_0\ln\left(\frac{e}{3L_0}\right)
=L_0\left[1+3(1-\ln3-\ln L_0)\right]
=L_0\left[4-3\ln3-3\ln L_0\right]\to-\infty.$$

Therefore $\Pr(L\ge k)\to0$: with probability tending to $1$, every bin has load less than
$3\ln n$. This is a valid but crude bound; the true maximum load is $\Theta(\log n/\log\log n)$, much
smaller than $3\ln n$ for large $n$.

**37.** *Strategy: compute the joint distribution explicitly, then compare covariance with
independence.*

(a) $X$ is uniform on $\{-1,0,1\}$, so

$$\mathbb{E}[X]=\frac13(-1+0+1)=0,\qquad
\mathbb{E}[Y]=\mathbb{E}[X^2]=\frac13(1+0+1)=\frac23.$$

Also $XY=X^3$, and $X^3$ takes the values $-1,0,1$ with equal probability, so $\mathbb{E}[XY]=0$.
Therefore

$$\operatorname{Cov}(X,Y)=\mathbb{E}[XY]-\mathbb{E}[X]\mathbb{E}[Y]=0-0\cdot\frac23=0.$$

(b) $Y=1$ exactly when $X=\pm1$, so $\Pr(Y=1)=2/3$. Then

$$\Pr(X=1,\,Y=1)=\Pr(X=1)=\frac13,$$

whereas

$$\Pr(X=1)\Pr(Y=1)=\frac13\cdot\frac23=\frac29.$$

Since $\frac13\ne\frac29$, $X$ and $Y$ are not independent. In fact $Y$ is a deterministic function of
$X$, the strongest possible dependence.

(c) The distribution of $X+Y=X+X^2$ is: for $X=-1$, $X+Y=0$; for $X=0$, $X+Y=0$; for $X=1$,
$X+Y=2$. Hence

$$\Pr(X+Y=0)=\frac23,\qquad \Pr(X+Y=2)=\frac13,$$
$$\mathbb{E}[X+Y]=\frac23\cdot0+\frac13\cdot2=\frac23,$$
$$\mathbb{E}[(X+Y)^2]=\frac23\cdot0+\frac13\cdot4=\frac43,$$
$$\operatorname{Var}(X+Y)=\frac43-\left(\frac23\right)^2=\frac43-\frac49=\frac89.$$

From the formula,

$$\operatorname{Var}(X)=\mathbb{E}[X^2]-\mathbb{E}[X]^2=\frac23-0=\frac23,$$
$$\operatorname{Var}(Y)=\mathbb{E}[Y^2]-\mathbb{E}[Y]^2=\mathbb{E}[X^4]-\frac49=\frac23-\frac49=\frac29,$$
$$\operatorname{Var}(X)+\operatorname{Var}(Y)+2\operatorname{Cov}(X,Y)
=\frac23+\frac29+0=\frac69+\frac29=\frac89.$$

The two answers agree because the variance-of-a-sum identity
$\operatorname{Var}(X+Y)=\operatorname{Var}(X)+\operatorname{Var}(Y)+2\operatorname{Cov}(X,Y)$ is an
algebraic identity valid for all random variables, dependent or not. Dependence enters only through the
covariance term; here the covariance happens to be zero, yet $Y$ is a deterministic function of $X$, so
the variables are strongly dependent. This is the precise sense in which "uncorrelated" is weaker than
"independent".

