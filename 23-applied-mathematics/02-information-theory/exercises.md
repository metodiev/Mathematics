# Information Theory — Exercises

> [Information Theory](README.md) · 36 problems · Beginner → Challenge · Solutions: [solutions.md](solutions.md)

Work through the problems in order. Every problem is solvable with the definitions and theorems of the
tutorial, and the section reference tells you where to look. Attempt each problem in writing before
consulting [solutions.md](solutions.md).

**Conventions.** All logarithms are base $2$ and all entropies are in bits unless a problem says
otherwise. $H_b(p) = -p\log_2 p - (1-p)\log_2(1-p)$ with $H_b(0)=H_b(1)=0$. Random variables have
finite range, $0\log_2 0$ is $0$, and "independent" means mutually independent where several variables
are involved. Give numerical answers to four decimal places unless the problem asks for an exact
value.

## Beginner

**1.** *(§5, Definition 5.3; §7.3)* A source takes four values with probabilities $0.5$, $0.2$, $0.2$, $0.1$.

(a) Compute $H(X)$.
(b) Compute $\log_2 4$ and explain why $H(X)$ is smaller.
(c) Which outcome contributes the largest term $-p\log_2 p$ to the entropy, and which the smallest?
    Explain the answer without recomputing.

**2.** *(§5, Definition 5.2)* Compute the self-information $i(x) = -\log_2 p(x)$ for $p(x) = 1$, $p(x) = 0.4$,
$p(x) = 0.01$ and $p(x) = 2^{-10}$. State in words what each number means.

**3.** *(§7.6)* Let $X \sim \operatorname{Bernoulli}(p)$.

(a) Compute $H_b(0.2)$, $H_b(0.8)$, $H_b(0.25)$, $H_b(0)$ and $H_b(1)$.
(b) Prove algebraically that $H_b(p) = H_b(1-p)$.
(c) State the maximum of $H_b$ and where it is attained.

**4.** *(§7.6)* A die is loaded so that face $1$ has probability $\tfrac12$ and each of the other five
faces has probability $\tfrac1{10}$.

(a) Compute the entropy of one roll.
(b) Compare with the entropy $\log_2 6$ of a fair die and explain the direction of the inequality.
(c) Compute the expected self-information of the outcome and confirm it equals the entropy of (a).

**5.** *(§7.6)* Compute $\log_2 3$, $\log_2 5$, $\log_2 26$ and $\log_2 365$ to four decimal places.
Interpret each as the entropy of a uniform source: a fair three-sided die, a fair five-sided die, a
uniform letter of the English alphabet, and a uniformly random day of a non-leap year.

**6.** *(§7.4, §7.5)* The pair $(X,Y)$ has joint probabilities

| $p(x,y)$ | $y=0$ | $y=1$ |
|---|---|---|
| $x=0$ | $0.3$ | $0.2$ |
| $x=1$ | $0.1$ | $0.4$ |

Compute the marginals, $H(X)$, $H(Y)$, $H(X,Y)$, $H(Y\mid X)$ and $I(X;Y)$. Verify
$I(X;Y) = H(Y)-H(Y\mid X)$ and $I(X;Y) = H(X)+H(Y)-H(X,Y)$.

**7.** *(§7.4)* Compute $H(X,Y)$ in each case, using only the data given.

(a) $X$ and $Y$ are independent with $H(X) = 1.5$ and $H(Y) = 0.8$.
(b) $X = Y$ with $H(X) = 1.5$.
(c) $Y = f(X)$ for a function $f$, with $H(X) = 1.5$ and $H(Y) = 0.6$.
(d) $X$ and $Y$ are independent, $H(X)=1$, $H(Y)=1$, and $Z$ is the pair $(X,Y)$; compute $H(Z)$.

**8.** *(§7.8)* A source has probabilities $(0.5, 0.25, 0.125, 0.125)$.

(a) Assign Shannon lengths $l_i = \lceil\log_2(1/p_i)\rceil$ and verify Kraft's inequality.
(b) Compute the expected length $L$ and compare it with $H(X)$.
(c) Explain why the two numbers coincide here.

**9.** *(§7.8)* For each of the following length sets, decide whether a binary prefix code with those
lengths exists, and justify the answer with Kraft's inequality: $(1,2,3,3)$, $(1,1,2)$, $(2,2,2,2)$,
$(1,2,2,3)$, $(2,2,2,3,3)$, $(1,1,2,4)$.

**10.** *(§7.11)* For the binary symmetric channel with crossover probability $\varepsilon$, compute
$C$ when $\varepsilon = 0$, $\varepsilon = 0.1$, $\varepsilon = 0.25$ and $\varepsilon = 0.5$.
Interpret each value.

**11.** *(§7.12)* Let $p = (0.5,0.5)$ and $q = (0.25,0.75)$.

(a) Compute $D(p\|q)$ and $D(q\|p)$.
(b) Explain why the two numbers differ and which errors each one penalises.
(c) Is either number a distance? Justify.

**12.** *(§7.12)* Let $p = (0.5,0.3,0.2)$ and $q = (\tfrac13,\tfrac13,\tfrac13)$.

(a) Compute $H(p)$ and the cross-entropy $H(p,q)$.
(b) Compute $D(p\|q)$ and verify Theorem 7.29.
(c) Which of the three numbers is the smallest, and must it be the entropy?

## Intermediate

**13.** *(§7.6)* Let $X$ be geometric: $\Pr(X=k) = (1-p)^{k-1}p$ for $k = 1,2,\dots$, with $p = 0.2$.

(a) Compute $\mathbb{E}[X]$ and $H(X)$ using the closed forms.
(b) Compare $H(X)$ with $\log_2 \mathbb{E}[X]$, the entropy of a uniform distribution on
    $\{1,\dots,\mathbb{E}[X]\}$, and explain why the geometric entropy is larger.
(c) For which value of $p$ is $H(X) = 2$ bits?

**14.** *(§7.6)* Let $X\sim\operatorname{Bin}(5,0.4)$.

(a) Compute the probability mass function at $k = 0,\dots,5$.
(b) Compute $H(X)$ exactly from the definition.
(c) Compute the Stirling approximation $\tfrac12\log_2(2\pi e\,np(1-p))$ and compare.

**15.** *(§7.6)* Let $X\sim\operatorname{Pois}(4)$.

(a) Compute $H(X)$ from the series $\sum_{k\ge0}p_k\log_2(1/p_k)$, summing enough terms to be sure of
    four decimal places. (You may state the tail is negligible below $10^{-6}$.)
(b) Compare with $\tfrac12\log_2(2\pi e\lambda)$.
(c) Explain why the approximation improves as $\lambda$ grows.

**16.** *(§7.4, §7.5)* The pair $(X,Y)$ has joint probabilities $p(0,0) = 0.25$, $p(0,1) = 0.25$,
$p(1,1) = 0.125$, $p(1,2) = 0.375$, and $0$ elsewhere. Compute $H(X)$, $H(Y)$, $H(X,Y)$,
$H(Y\mid X)$, $H(X\mid Y)$ and $I(X;Y)$, and check the chain rule in both directions.

**17.** *(§7.5)* A binary source $X$ with $\Pr(X=0)=\Pr(X=1)=\tfrac12$ is sent through two binary
symmetric channels in series: $X\to Y$ with crossover probability $0.1$, then $Y\to Z$ with crossover
probability $0.2$.

(a) Compute the effective crossover probability of the composition $X\to Z$.
(b) Using the chain rule, compute $H(X,Y,Z)$.
(c) Compute $I(X;Y)$, $I(X;Z)$ and $I(X;Y\mid Z)$, and verify the data processing inequality.

**18.** *(§7.4)* Prove that $H(X,Y) = H(X)+H(Y)$ if and only if $X$ and $Y$ are independent. (One
direction is Corollary 7.11; for the other, use the proof of Theorem 7.10.)

**19.** *(§7.5)* Prove carefully that $I(X;Y) = 0$ if and only if $X$ and $Y$ are independent. State
which theorem you use at each step.

**20.** *(§7.11)* A binary symmetric channel has $\varepsilon = 0.2$ and the input satisfies
$\Pr(X=1) = 0.3$.

(a) Compute $\Pr(Y=1)$, $H(Y)$ and $H(Y\mid X)$.
(b) Compute $I(X;Y)$ and compare with the capacity $C$.
(c) Explain in words why the skewed input loses information.

**21.** *(§7.9)* Construct a Huffman code for the probabilities $(0.45, 0.20, 0.15, 0.10, 0.06, 0.04)$.

(a) List the merges in order.
(b) Give the codewords and their lengths.
(c) Compute $H$, $L$ and the redundancy $L-H$.
(d) Verify Kraft's inequality and check that it holds with equality.

**22.** *(§7.8, §7.9)* A source has probabilities $(0.4, 0.3, 0.2, 0.1)$.

(a) Write down the Shannon lengths and compute $L$, verifying $H \le L < H+1$.
(b) Construct a Huffman code and compute its expected length.
(c) How much does Huffman save per symbol, and why is the Shannon code not optimal here?

## Advanced

**23.** *(§7.3)* Prove Proposition 7.5(b): for a finite random variable supported on $n$ points,
$H(X) \le \log_2 n$ with equality if and only if $X$ is uniform on its support. Give the proof in full,
stating clearly where strict concavity is used.

**24.** *(§7.3)* Prove that $H(p) = -\sum_i p_i\log_2 p_i$ is a concave function of $p$ on the simplex,
and deduce that for distributions $p,q$ and $0\le\lambda\le1$,

$$H(\lambda p+(1-\lambda)q) \ge \lambda H(p)+(1-\lambda)H(q).$$ Interpret the result: what happens to
uncertainty when two sources are mixed?

**25.** *(§7.5)* Prove the mutual information chain rule

$$I(X;Y,Z) = I(X;Z)+I(X;Y\mid Z),$$ and use it, together with the Markov property, to prove the data
processing inequality $I(X;Z)\le I(X;Y)$ for $X\to Y\to Z$. Explain exactly where each hypothesis is
used.

**26.** *(§7.4)* Let $f$ be a function whose domain contains the support of $X$. Prove that
$H(f(X)) \le H(X)$, with equality if and only if $f$ is injective on $\operatorname{supp}p_X$.
Deduce that relabelling a finite alphabet never changes entropy.

**27.** *(§7.4)* Prove Corollary 7.11 in full: $H(X,Y)\le H(X)+H(Y)$, with equality if and only if $X$
and $Y$ are independent. Do not quote Theorem 7.10; prove the inequality directly from the definition
and the elementary inequality $\ln t\le t-1$.

**28.** *(§7.7)* Prove that among all densities on $[0,\infty)$ with finite mean $\mu$, the exponential
density with rate $1/\mu$ uniquely maximises differential entropy, and compute that maximum. State
carefully which inequality replaces the Gibbs argument of Theorem 7.18.

**29.** *(§7.12)* Prove the chain rule for the Kullback–Leibler divergence:

$$D\big(p(x,y)\,\|\,q(x,y)\big) = D\big(p(x)\,\|\,q(x)\big)+\sum_x p(x)\,D\big(p(y\mid x)\,\|\,q(y\mid x)\big).$$
State the conventions needed when some conditional probabilities vanish.

**30.** *(§7.12)* Prove Gibbs' inequality $D(p\|q)\ge0$ for probability mass functions on a finite
alphabet, with equality if and only if $p=q$. Then deduce that the cross-entropy satisfies
$H(p,q)\ge H(p)$ for every $q$, and characterise the case of equality.

## Challenge

**31.** *(§7.11)* **Fano's inequality.** Let $X$ be a finite random variable, $\hat X = g(Y)$ a
decoder, and $P_e = \Pr(\hat X \ne X)$ the error probability. Prove that

$$H(X\mid Y) \le H_b(P_e) + P_e\log_2(\lvert\mathcal{X}\rvert-1).$$
*Hint.* Introduce the error indicator $E = \mathbf{1}\{\hat X \ne X\}$ and use the chain rule together
with $H(X\mid Y) \le H(X,E\mid Y)$.

**32.** *(§7.8)* **Redundancy of a complete prefix code.** Let $c$ be a binary prefix code whose Kraft
sum equals $1$, and put $q_i = 2^{-l_i}$. Prove that $q$ is a probability distribution and that

$$L - H(p) = D(p\,\|\,q).$$ Deduce that $L = H(p)$ if and only if $p_i = 2^{-l_i}$ for every $i$, and
explain why this can only happen when every $p_i$ is a negative power of $2$.

**33.** *(§7.4)* Let $X$ and $Y$ be independent integer-valued random variables. Prove that

$$H(X+Y) \ge \max\{H(X),H(Y)\}.$$
Give an example where equality holds and an example where the inequality is strict. Does the result
survive if $X$ and $Y$ are not independent?

**34.** *(§7.12)* **Joint convexity of the divergence.** Prove first the log-sum inequality: for
non-negative $a_i,b_i$ with $\sum_i a_i = A$ and $\sum_i b_i = B$,

$$\sum_i a_i\log_2\frac{a_i}{b_i} \ge A\log_2\frac{A}{B}.$$
Then prove that $(p,q)\mapsto D(p\|q)$ is jointly convex, that is,

$$D\big(\lambda p_1+(1-\lambda)p_2\,\big\|\,\lambda q_1+(1-\lambda)q_2\big) \le \lambda D(p_1\|q_1)+(1-\lambda)D(p_2\|q_2)$$
for $0\le\lambda\le1$. Indicate clearly the convention needed when some entries vanish.

**35.** *(§7.9)* Prove that the Huffman algorithm produces an optimal binary prefix code. Your proof
must contain: (i) a proof that some optimal tree has the two least probable symbols as siblings at
maximum depth; (ii) the contraction argument relating the optimal lengths for $n$ symbols to those for
$n-1$; (iii) an induction that concludes optimality.

**36.** *(§7.10)* **Asymptotic equipartition.** Let $X_1,X_2,\dots$ be i.i.d. with finite alphabet and
entropy $H$. For $\varepsilon>0$ define the typical set

$$\mathcal{T}_n(\varepsilon) = \Big\{(x_1,\dots,x_n) : \Big\lvert -\tfrac1n\log_2 p(x_1,\dots,x_n) - H\Big\rvert \le \varepsilon\Big\}.$$
Using the weak law of large numbers, prove that for all sufficiently large $n$:

(a) $\Pr\big((X_1,\dots,X_n)\in\mathcal{T}_n(\varepsilon)\big) \ge 1-\varepsilon$;
(b) every sequence in $\mathcal{T}_n(\varepsilon)$ has probability between $2^{-n(H+\varepsilon)}$ and
    $2^{-n(H-\varepsilon)}$;
(c) $(1-\varepsilon)2^{n(H-\varepsilon)} \le \lvert\mathcal{T}_n(\varepsilon)\rvert \le 2^{n(H+\varepsilon)}$.

Explain in two sentences how (c) yields the source coding theorem.
