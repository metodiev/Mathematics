# Discrete Probability — Exercises

> [Discrete Probability](README.md) · 37 problems · Beginner → Challenge · Solutions: [solutions.md](solutions.md)

Attempt every problem in writing before looking at [solutions.md](solutions.md). Each problem names
the section of the tutorial that supplies the method. A calculator is useful for the numerical parts;
where a decimal is requested, four significant figures are enough unless the problem says otherwise.
"Verify" means "check the value against an independent computation", not "state that it is true".

Notation: $\Pr$ is a probability measure on a finite space; $H_n=\sum_{k=1}^{n}1/k$; a standard deck
has $52$ cards in four suits of $13$; "without replacement" means distinct items are drawn.

## Beginner

**1.** *(§5, §7.1)* A fair six-sided die is rolled once. Let $A=\{2,4,6\}$ and $B=\{2,3,5\}$.
Compute $\Pr(A)$, $\Pr(B)$, $\Pr(A\cup B)$ and $\Pr(A\cap B)$. Verify the addition rule numerically,
and decide whether $A$ and $B$ are independent.

**2.** *(§7.2)* Two fair coins are tossed. List the sample space of ordered outcomes and compute the
probability of exactly one head and of at least one head. Then explain what goes wrong if one takes
$\{0,1,2\}$ (the possible numbers of heads) as a uniform sample space.

**3.** *(§7.2, §7.3)* One card is drawn from a standard deck. Compute $\Pr(\text{heart or king})$,
$\Pr(\text{face card}\mid\text{heart})$, and $\Pr(\text{king}\mid\text{face card})$. A face card is a
jack, queen or king.

**4.** *(§7.2, §7.3)* Two fair dice are rolled. Compute $\Pr(\text{sum}\le4)$,
$\Pr(\text{product is even})$, and $\Pr(\text{sum}=7\mid\text{sum is odd})$.

**5.** *(§7.2)* (a) Compute the probability of at least one six in four rolls of a fair die.
(b) Compute the probability of at least one double-six in $24$ rolls of two fair dice. Compare the
two answers and comment on the historical significance of the comparison.

**6.** *(§7.2)* A five-card hand is dealt from a standard deck. Compute the probability that (a) all
five cards are hearts, and (b) the hand contains exactly one ace.

**7.** *(§7.3, §7.5)* In a group of $100$ people, $60$ drink coffee, $45$ drink tea, and $25$ drink
both. Compute $\Pr(\text{coffee}\mid\text{tea})$, $\Pr(\text{tea}\mid\text{coffee})$ and
$\Pr(\text{coffee}\cup\text{tea})$. Are the two habits independent?

**8.** *(§7.4)* Urn A contains $3$ red and $2$ blue balls; urn B contains $1$ red and $4$ blue balls.
An urn is chosen at random and one ball is drawn. Compute $\Pr(\text{red})$ and
$\Pr(\text{urn A}\mid\text{red})$.

**9.** *(§7.9)* Let $X\sim\operatorname{Bin}(5,0.3)$. Compute $\Pr(X=2)$, $\Pr(X\ge1)$, the mean, the
variance and the standard deviation.

**10.** *(§7.9)* Let $T\sim\operatorname{Geom}(0.2)$ on $\{1,2,\dots\}$. Compute $\Pr(T=3)$,
$\Pr(T\le3)$, $\Pr(T>5)$, the mean and the standard deviation.

**11.** *(§7.6, §7.7, §7.8)* A random variable $X$ has the following distribution.

| $x$ | $0$ | $1$ | $2$ | $3$ |
|---|---|---|---|---|
| $\Pr(X=x)$ | $0.1$ | $0.3$ | $0.4$ | $0.2$ |

Compute $\mathbb{E}[X]$, $\mathbb{E}[X^2]$, $\operatorname{Var}(X)$ and $\sigma_X$. Then compute
$\mathbb{E}[2X+1]$ and $\operatorname{Var}(2X+1)$.

**12.** *(§7.8)* Prove that $\operatorname{Var}(X)=\mathbb{E}[X^2]-\mathbb{E}[X]^2$ for a random
variable on a finite space. Apply the identity to a Bernoulli$(p)$ variable, computing
$\mathbb{E}[X]$ and $\mathbb{E}[X^2]$ from the definition.

**13.** *(§7.7, §7.8)* Ten fair dice are rolled. Let $S$ be their sum and $N$ the number of sixes.
Compute $\mathbb{E}[S]$, $\operatorname{Var}(S)$, $\sigma_S$, $\mathbb{E}[N]$ and
$\operatorname{Var}(N)$. Which of these computations uses independence?

## Intermediate

**14.** *(§7.1, §8.3)* In a class of $100$ students, $50$ study mathematics, $40$ study physics and
$30$ study chemistry. Moreover $20$ study mathematics and physics, $15$ study mathematics and
chemistry, $10$ study physics and chemistry, and $5$ study all three. Compute the probability that a
student studies at least one of the three subjects, the probability that a student studies none, and
the probability that a student studies exactly one. Verify that the "exactly one" total is consistent
with the three pairwise intersections.

**15.** *(§7.4)* A disease has prevalence $0.5\%$. A test has sensitivity $98\%$ and specificity
$96\%$. Compute the positive predictive value $\Pr(\text{disease}\mid+)$ and the negative predictive
value $\Pr(\text{healthy}\mid-)$. Comment on the relative sizes of the two.

**16.** *(§7.5)* Two fair coins are tossed. Let $A$ be "the first coin is heads", $B$ be "the second
coin is heads", and $C$ be "the two coins match". Show that $A,B,C$ are pairwise independent but not
mutually independent. Then state which of the product identities fail.

**17.** *(§7.6, §7.7)* A random variable $X$ takes the values $-1,0,1,2$ with probabilities
$0.2,0.3,0.3,0.2$ respectively. Let $Y=\lvert X\rvert$. Compute the mass function of $Y$, then
$\mathbb{E}[X]$, $\operatorname{Var}(X)$, $\mathbb{E}[Y]$ and $\mathbb{E}[Y^2]$. Explain why
$\mathbb{E}[Y^2]=\mathbb{E}[X^2]$ without recomputing both from scratch.

**18.** *(§7.2, §7.9)* A lot contains $20$ items, of which $5$ are defective. Four items are drawn
without replacement. Compute the exact probability of exactly two defective items. Then compute the
binomial probability with $n=4$ and $p=1/4$ that would result from pretending the draws are with
replacement, and explain the direction of the discrepancy.

**19.** *(§7.7)* A uniformly random permutation of $n$ objects is chosen. Let $F$ be the number of
fixed points (objects that stay in their original position). Use indicator variables to show that
$\mathbb{E}[F]=1$ for every $n\ge1$. For $n=5$, also compute $\Pr(F\ge1)$ using the derangement
count $!5=44$.

**20.** *(§8.4)* (a) Prove the tail-sum formula: if $X$ takes values in $\{0,1,2,\dots\}$, then
$\mathbb{E}[X]=\sum_{k\ge1}\Pr(X\ge k)$. (b) Apply it to $T\sim\operatorname{Geom}(p)$, using
$\Pr(T>k)=(1-p)^k$, to obtain $\mathbb{E}[T]=1/p$. (c) Apply it to $X$ uniform on $\{1,\dots,n\}$ and
check that the result is $(n+1)/2$.

**21.** *(§7.9)* Let $X\sim\operatorname{Pois}(2.5)$. Compute $\Pr(X=0)$, $\Pr(X\ge1)$,
$\Pr(X=3)$ and $\Pr(X\le3)$. State the mean and variance.

**22.** *(§7.10)* There are $m=1000$ buckets and $n=50$ items, each placed independently and
uniformly. Compute the exact probability of at least one collision and the exponential approximation
$1-\exp(-n(n-1)/(2m))$. Explain, using the inequality in §7.10, whether the approximation is a lower
or an upper bound on the true collision probability.

**23.** *(§7.11)* For randomised quicksort on $n$ distinct keys, compute the expected number of
comparisons for $n=1,2,3,4,5$ from the formula $2(n+1)H_n-4n$. Check the value for $n=5$ against the
direct sum $\sum_{d=1}^{4}(5-d)\cdot2/(d+1)$, and compare with the worst case $\binom{5}{2}$.

**24.** *(§7.11)* In the coupon collector with $n$ equally likely types, compute the expected number
of draws to collect all types for $n=5$ and $n=10$. For $n=10$, how many draws give a $90\%$ chance
of completion according to the bound $\Pr(T>t)\le ne^{-t/n}$? (The bound is not exact; state that
clearly.)

**25.** *(§7.12)* A two-state Markov chain has transition matrix
$P=\begin{pmatrix}0.9&0.1\\0.4&0.6\end{pmatrix}$, with states $1$ and $2$. Find the stationary
distribution. Compute the expected time to reach state $2$ from state $1$, and the mean return time
to state $1$. Verify the return time with a first-step computation.

## Advanced

**26.** *(§7.9, §8.5)* Derive the mean and variance of $T\sim\operatorname{Geom}(p)$ in two ways:
(a) using the tail-sum formula for the mean and the factorial moment for the variance; (b) using the
first-step equation $\mathbb{E}[T]=1+(1-p)\mathbb{E}[T]$ for the mean, and the identity
$\mathbb{E}[T^2]=p\cdot1^2+(1-p)\mathbb{E}[(T+1)^2]$ for the second moment. Confirm that both routes
give $\operatorname{Var}(T)=(1-p)/p^2$.

**27.** *(§7.9)* Derive $\operatorname{Var}(X)=np(1-p)$ for $X\sim\operatorname{Bin}(n,p)$ in full:
write $X=\sum_{i=1}^n\mathbf{1}_{A_i}$, compute $\operatorname{Var}(\mathbf{1}_{A_i})$, and justify
why every covariance term vanishes. Then explain carefully whether mutual independence is actually
needed for this variance computation, and identify which part of the binomial derivation *does*
require the full product rule.

**28.** *(§7.9)* Prove the Poisson limit theorem in detail: for fixed $\lambda>0$ and fixed
$k\ge0$, show that
$\binom{n}{k}(\lambda/n)^k(1-\lambda/n)^{n-k}\to e^{-\lambda}\lambda^k/k!$ as $n\to\infty$. Identify
each factor and its limit, and explain where the condition "$\lambda$ fixed" is used.

**29.** *(§7.11)* (a) Prove that the coupon collector satisfies $\mathbb{E}[T]=nH_n$ by writing
$T=T_1+\cdots+T_n$ and computing the mean of each geometric stage. (b) Show that
$\operatorname{Var}(T)=n^2H_n^{(2)}-nH_n$, where $H_n^{(2)}=\sum_{k=1}^n1/k^2$. (c) Evaluate the mean
and variance for $n=4$.

**30.** *(§7.11)* In randomised quicksort, let $i<j$ be two keys in sorted order.
(a) Prove that they are compared with probability $2/(j-i+1)$ by considering the first pivot chosen
from $\{i,i+1,\dots,j\}$. (b) Sum over all pairs to derive
$\mathbb{E}[C_n]=\sum_{d=1}^{n-1}(n-d)\cdot2/(d+1)$ and then $2(n+1)H_n-4n$. (c) Show that
$\mathbb{E}[C_n]\le2n\ln n+2n$ and compare with the worst case.

**31.** *(§7.12)* Consider the three-state chain on $\{1,2,3\}$ with

$$P=\begin{pmatrix}0&1&0\\0.5&0&0.5\\0&1&0\end{pmatrix}.$$

(a) Find the stationary distribution. (b) Compute $P^2$ and $P^3$. (c) Compute the expected hitting
time from state $2$ to state $1$, and from state $3$ to state $1$. (d) Explain why $P^n$ does not
converge, even though the stationary distribution is unique.

**32.** *(§8.2)* (a) Prove the law of the unconscious statistician for a finite space:
$\mathbb{E}[g(X)]=\sum_x g(x)p_X(x)$. (b) Prove that
$\mathbb{E}[X+Y]=\mathbb{E}[X]+\mathbb{E}[Y]$ without assuming independence. (c) Give an explicit
example of random variables on a finite space with $\mathbb{E}[XY]\ne\mathbb{E}[X]\mathbb{E}[Y]$, and
compute both sides.

**33.** *(§8.6)* Let $X\sim\operatorname{Bin}(100,0.5)$.
(a) Use Markov's inequality to bound $\Pr(X\ge70)$.
(b) Use Chebyshev's inequality to bound $\Pr(\lvert X-50\rvert\ge20)$.
(c) Compute the exact value of $\Pr(X\ge70)$ and compare. Which bound is tighter, and why?

## Challenge

**34.** *(§7.10)* (a) Show that the smallest $n$ for which the birthday collision probability with
$m=365$ exceeds $1/2$ is $n=23$, by computing the exact probabilities for $n=22$ and $n=23$.
(b) Derive the approximation $n\approx\sqrt{2m\ln2}$ and evaluate it for $m=365$ and $m=2^{32}$.
(c) Explain why the approximation is not exact, and whether it overestimates or underestimates the
threshold in the case $m=365$.

**35.** *(§7.11, §8.3)* A collector faces three coupon types with probabilities
$p_1=1/2$, $p_2=1/3$, $p_3=1/6$ on each independent draw. (a) Show that the expected time to collect
all three is

$$\mathbb{E}[T]=\sum_{\varnothing\ne S\subseteq\{1,2,3\}}\frac{(-1)^{\lvert S\rvert+1}}{\sum_{i\in S}p_i}.$$

(b) Evaluate the formula to obtain $\mathbb{E}[T]=7.3$. (c) Verify the result by solving the
first-step equations for the expected time from each subset of collected types.

**36.** *(§7.7, §8.6)* Throw $n$ balls independently and uniformly into $n$ bins.
(a) Use indicators to show that the expected number of empty bins is $n(1-1/n)^n$, and evaluate it
for $n=20$. (b) Let $L$ be the maximum load. Use the union bound and the bound
$\binom{n}{k}\le(en/k)^k$ to show that $\Pr(L\ge k)\le n(en/k)^k\cdot n^{-k}=n(e/k)^k$. Deduce that
for $k=\lceil3\ln n\rceil$ the probability tends to $0$ as $n\to\infty$.

**37.** *(§7.8)* Let $X$ be uniform on $\{-1,0,1\}$ and let $Y=X^2$. (a) Show that
$\operatorname{Cov}(X,Y)=0$, so $X$ and $Y$ are uncorrelated. (b) Show that $X$ and $Y$ are not
independent by comparing $\Pr(X=1,Y=1)$ with $\Pr(X=1)\Pr(Y=1)$. (c) Compute
$\operatorname{Var}(X+Y)$ directly from the distribution of $X+Y$, and again from
$\operatorname{Var}(X)+\operatorname{Var}(Y)+2\operatorname{Cov}(X,Y)$. Explain why the two answers
agree even though $X$ and $Y$ are dependent.
