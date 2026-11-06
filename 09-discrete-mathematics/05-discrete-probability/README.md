# Discrete Probability

> [Mathematics](../../README.md) › [Discrete Mathematics](../README.md) › Discrete Probability · Level: Intermediate · Prerequisites: [Set Theory](../../00-foundations/03-set-theory/README.md), [Proof Techniques](../../00-foundations/04-proof-techniques/README.md), [Mathematical Induction](../01-mathematical-induction/README.md), [Recurrence Relations](../02-recurrence-relations/README.md), [Exponential and Logarithmic Functions](../../03-algebra/12-exponential-and-logarithmic-functions/README.md) · Estimated time: 480 min

## 1. Introduction

A finite probability space is the one place in probability where nothing can hide. The sample space
is a finite set, every subset is an event, and a probability is just a list of numbers — one mass per
outcome — that adds up to $1$. Every probability is a finite sum, every expectation is a finite sum,
and every theorem is a theorem about finite sums. This makes discrete probability the right place to
learn *why* the rules of probability work, before analysis introduces limits, measures and the
technical machinery needed for continuous models.

The subject is also the working language of computer science. A randomised algorithm has a running
time that is a random variable; a hash table has a collision probability; a network has a load
distribution; a machine-learning model has an error rate estimated from a finite test set. In each
case the question is not "what happens?" but "with what probability, and what is the average over the
randomness?". Many of those questions reduce to counting and to one surprisingly strong identity,
linearity of expectation.

Four ideas organise this tutorial.

**The model comes first.** A probability space is a *choice*. Saying that a die is fair is a modelling
assumption, not a theorem, and the same physical die can be modelled by many different measures. Most
elementary errors come from silently switching models — treating the three outcomes "no heads", "one
head", "two heads" of two coin tosses as equally likely because they are listed as three things.

**Counting gives probabilities only under a uniform model.** The formula $\Pr(A)=\lvert A\rvert/\lvert\Omega\rvert$
is a theorem about the uniform measure, not a definition of probability. Every use of it needs a
symmetry argument: the outcomes must be indistinguishable except for their labels.

**Expectation is linear even when the variables are dependent.** $\mathbb{E}[X+Y]=\mathbb{E}[X]+\mathbb{E}[Y]$
has no hypotheses beyond integrability, which is automatic on a finite space. This single fact proves
the expected number of comparisons in quicksort, the expected time to collect all coupons, and the
expected number of fixed points of a random permutation, without ever computing a joint distribution.

**Randomness is a resource.** Randomised quicksort avoids the worst case of deterministic quicksort
not by being smarter but by making the bad input unlikely. The analysis of expected running time is
therefore a genuine correctness argument about an algorithm, not an approximation.

The tutorial treats finite spaces only. The general theory, including countable additivity, algebras
of events and continuous distributions, is developed in [Probability Foundations](../../10-probability/01-probability-foundations/README.md);
the statistical use of these ideas begins in [Statistics](../../11-statistics/README.md).

## 2. Prerequisites

| Prerequisite | Why it is needed here |
|---|---|
| [Set Theory](../../00-foundations/03-set-theory/README.md) | Events are subsets; unions, intersections, complements, Cartesian products and cardinality are used constantly. |
| [Proof Techniques](../../00-foundations/04-proof-techniques/README.md) | Direct proof, proof by contradiction and proof by contrapositive appear in the theorems on independence and conditioning. |
| [Mathematical Induction](../01-mathematical-induction/README.md) | Finite additivity is extended to $n$ events by induction; the binomial theorem and the Chapman–Kolmogorov identity are also proved by induction. |
| [Recurrence Relations](../02-recurrence-relations/README.md) | The geometric distribution and the coupon-collector analysis produce first-order recurrences; solving them is assumed. |
| [Exponential and Logarithmic Functions](../../03-algebra/12-exponential-and-logarithmic-functions/README.md) | The Poisson limit uses $(1-\lambda/n)^n\to e^{-\lambda}$, and the birthday approximation uses $\ln(1-x)\approx -x$. |
| [Limits](../../07-calculus/01-limits/README.md) | Only for the Poisson limit theorem, where a sequence of probabilities is computed as $n\to\infty$. |

Counting is **not** assumed. Section 7.2 develops the multiplication principle, permutations and
binomial coefficients from scratch, because every one of them is used in the probability calculations.
A fuller treatment, including inclusion–exclusion and the pigeonhole principle, is in
[Counting Principles](../../20-combinatorics/01-counting-principles/README.md); that topic appears later
in the curriculum and can be read afterwards without loss.

## 3. Learning Objectives

By the end of this tutorial you will be able to:

1. Write down a finite probability space for a word problem and justify why a particular measure is
   appropriate.
2. Derive the complement rule, monotonicity and inclusion–exclusion from the axioms.
3. Count outcomes using the multiplication principle, permutations and binomial coefficients, and
   explain why a count is valid only under a symmetry assumption.
4. Compute conditional probabilities, apply the multiplication rule, the total probability theorem
   and Bayes' theorem in finite settings.
5. Decide whether events are independent, pairwise independent or mutually independent, and give
   counterexamples separating the notions.
6. Define a random variable, its mass function and its expectation, and compute expectations by
   grouping outcomes.
7. Prove and use linearity of expectation, including the indicator-variable method.
8. Derive the mean and variance of the Bernoulli, binomial, geometric and Poisson distributions.
9. Derive the birthday-collision formula and the $n^2/(2m)$ heuristic, with an honest error bound.
10. Analyse the expected number of comparisons in randomised quicksort and the expected time of the
    coupon collector.
11. Set up and solve the first-step equations for a finite Markov chain, and find a stationary
    distribution.

## 4. Intuition

**Tickets in a bag.** Imagine a bag containing one ticket per outcome $\omega\in\Omega$. Ticket
$\omega$ has weight $p(\omega)$, and the weights sum to $1$. An event $A$ is a collection of tickets;
its probability is the total weight of the collection. This picture is exact: a finite probability
space *is* a weighted bag of tickets.

**Conditioning is throwing tickets away.** To condition on $B$, remove every ticket not in $B$, then
rescale the remaining weights so that they again sum to $1$. The rescaling is the division by
$\Pr(B)$ in the definition. Nothing else changes, which is why conditional probability satisfies the
same axioms as unconditional probability.

**Independence is invariance under conditioning.** Events $A$ and $B$ are independent when throwing
away the tickets outside $B$ does not change the *fraction* of the remaining weight that lies in $A$.
Equivalently, knowing that $B$ happened tells you nothing about whether $A$ happened. Independence is
a property of the pair of events and the measure, not a causal statement.

**A random variable is a number printed on each ticket.** $X$ assigns a real number to every outcome.
Many tickets may carry the same number; the probability that $X=x$ is the total weight of the tickets
printed with $x$. The mass function is the bag regrouped by printed number.

**Expectation is the balance point.** Put the tickets on a number line at positions $X(\omega)$, with
weight $p(\omega)$ at each position. The expectation is the point where the line balances. It need
not coincide with any printed number, and it is not the "most likely" value.

**Variance is the moment of inertia.** It measures how far the weight is spread from the balance
point, in squared units. Taking a square root returns to the original units.

**Indicators are light switches.** The indicator $\mathbf{1}_A$ is $1$ on the tickets in $A$ and $0$
elsewhere. Its expectation is exactly $\Pr(A)$. Summing indicators counts how many of a list of events
occur, so the expectation of a complicated count becomes a sum of simple probabilities. This is the
most useful computational trick in the subject.

**Randomness in algorithms.** When quicksort chooses a pivot uniformly at random, the pivot is a
random variable on the finite space of pivot choices. The number of comparisons is then a random
variable, and "expected running time" is its expectation. The input is fixed; only the algorithm's
internal coin tosses are random. This distinction matters: a randomised algorithm has no bad inputs,
only unlucky coin tosses.

## 5. Formal Definition

Throughout, $\Omega$ is a nonempty finite set and $2^\Omega$ denotes its power set.

**Definition 5.1 (finite probability space).** A *probability measure* on $\Omega$ is a function
$\Pr:2^\Omega\to[0,1]$ such that

1. $\Pr(\Omega)=1$;
2. for all disjoint $A,B\subseteq\Omega$,
   $$\Pr(A\cup B)=\Pr(A)+\Pr(B).$$

The pair $(\Omega,\Pr)$ is a *finite probability space*. Elements of $\Omega$ are *outcomes*,
subsets of $\Omega$ are *events*, and $\Pr(A)$ is the *probability* of $A$.

Because $\Omega$ is finite, condition 2 extends by induction to any finite family of pairwise disjoint
events. Countable additivity — the extra axiom needed for infinite spaces — is therefore automatic
here and never has to be checked.

**Definition 5.2 (uniform measure).** If $\lvert\Omega\rvert=N$ and $\Pr(\{\omega\})=1/N$ for every
$\omega$, the space is *uniform*. In a uniform space, for every event $A$,

$$\Pr(A)=\frac{\lvert A\rvert}{\lvert\Omega\rvert}.$$

This formula is a consequence of the axioms, not an independent definition, and it is valid only in
the uniform case.

**Definition 5.3 (complement).** For an event $A$, the *complement* is $A^{\complement}=\Omega\setminus A$.

**Definition 5.4 (conditional probability).** Let $A,B\subseteq\Omega$ with $\Pr(B)>0$. The
*conditional probability of $A$ given $B$* is

$$\Pr(A\mid B)=\frac{\Pr(A\cap B)}{\Pr(B)}.$$

If $\Pr(B)=0$, the expression is undefined; there is no canonical value to assign.

**Definition 5.5 (independence).** Events $A$ and $B$ are *independent* if

$$\Pr(A\cap B)=\Pr(A)\Pr(B).$$

A finite family $A_1,\dots,A_n$ is *mutually independent* if for every subset
$\{i_1,\dots,i_k\}\subseteq\{1,\dots,n\}$ with $k\ge2$,

$$\Pr(A_{i_1}\cap\cdots\cap A_{i_k})=\Pr(A_{i_1})\cdots\Pr(A_{i_k}).$$

The family is *pairwise independent* if the identity holds for every pair. Mutual independence implies
pairwise independence, and not conversely (Example 7.5.3).

**Definition 5.6 (random variable and mass function).** A *random variable* on $\Omega$ is a function
$X:\Omega\to\mathbb{R}$. Its *probability mass function* (PMF) is

$$p_X(x)=\Pr(X=x)=\Pr\bigl(\{\omega\in\Omega:X(\omega)=x\}\bigr),$$

and its *cumulative distribution function* (CDF) is $F_X(x)=\Pr(X\le x)$.

The PMF is a nonnegative function with finite support and $\sum_x p_X(x)=1$. Conversely, any such
function is the PMF of some random variable on a suitable finite space.

**Definition 5.7 (expectation).** For a random variable $X$ on a finite space,

$$\mathbb{E}[X]=\sum_{\omega\in\Omega}X(\omega)\Pr(\{\omega\}).$$

Equivalently, $\mathbb{E}[X]=\sum_x x\,p_X(x)$, where the sum runs over the finite set of values
attained by $X$. The equivalence is proved in §8.2.

**Definition 5.8 (variance and standard deviation).** With $\mu=\mathbb{E}[X]$,

$$\operatorname{Var}(X)=\mathbb{E}\bigl[(X-\mu)^2\bigr], \qquad
\sigma_X=\sqrt{\operatorname{Var}(X)}.$$

**Definition 5.9 (covariance and correlation).** For random variables $X,Y$,

$$\operatorname{Cov}(X,Y)=\mathbb{E}\bigl[(X-\mathbb{E}[X])(Y-\mathbb{E}[Y])\bigr], \qquad
\rho(X,Y)=\frac{\operatorname{Cov}(X,Y)}{\sigma_X\sigma_Y}$$

whenever $\sigma_X\sigma_Y>0$.

**Definition 5.10 (the four distributions).** Let $p\in[0,1]$ and $\lambda>0$.

| Name | Parameters | Support | PMF |
|---|---|---|---|
| Bernoulli | $p$ | $\{0,1\}$ | $p(0)=1-p$, $p(1)=p$ |
| Binomial | $n\in\mathbb{N}$, $p$ | $\{0,1,\dots,n\}$ | $\Pr(X=k)=\binom{n}{k}p^k(1-p)^{n-k}$ |
| Geometric | $p\in(0,1]$ | $\{1,2,3,\dots\}$ | $\Pr(T=k)=(1-p)^{k-1}p$ |
| Poisson | $\lambda>0$ | $\{0,1,2,\dots\}$ | $\Pr(X=k)=e^{-\lambda}\dfrac{\lambda^k}{k!}$ |

The binomial is the distribution of the number of successes in $n$ independent Bernoulli trials with
success probability $p$. The geometric is the distribution of the trial on which the first success
occurs. The Poisson is not supported on a finite set; it is included here because it arises as the
limit of binomial distributions and because its algebra is entirely discrete.

**Definition 5.11 (finite Markov chain).** Let $S$ be a finite set of *states*. A *Markov chain* is a
sequence of random variables $X_0,X_1,\dots$ taking values in $S$ such that for all $n\ge0$ and all
$i,j\in S$,

$$\Pr(X_{n+1}=j\mid X_n=i,\,X_{n-1}=i_{n-1},\dots,X_0=i_0)=\Pr(X_{n+1}=j\mid X_n=i)=P_{ij}.$$

The matrix $P=(P_{ij})$ is the *transition matrix*. It has nonnegative entries and each row sums
to $1$; such a matrix is called *stochastic*. A probability vector $\pi$ is *stationary* if
$\pi P=\pi$.

**Remark 5.12 (what the finite theory avoids).** On a general space one must specify a $\sigma$-algebra
of events and require countable additivity; not every subset need be an event, and not every function
need be measurable. On a finite space the power set is the only sensible $\sigma$-algebra, every
function is measurable, and every sum is finite. The general definitions are in
[Probability Foundations](../../10-probability/01-probability-foundations/README.md); nothing in this
tutorial depends on them.

## 6. Mathematical Notation

| Symbol | Read as | Meaning |
|---|---|---|
| $\Omega$ | omega, the sample space | the finite set of all outcomes |
| $\omega$ | omega | a single outcome |
| $\lvert A\rvert$ | cardinality of $A$ | the number of elements of $A$ |
| $A^{\complement}$ | $A$ complement | $\Omega\setminus A$ |
| $\Pr(A)$ | probability of $A$ | a number in $[0,1]$ |
| $\Pr(A\mid B)$ | probability of $A$ given $B$ | $\Pr(A\cap B)/\Pr(B)$ when $\Pr(B)>0$ |
| $X,Y,Z$ | random variables | functions $\Omega\to\mathbb{R}$ |
| $p_X$ | mass function of $X$ | $p_X(x)=\Pr(X=x)$ |
| $F_X$ | distribution function of $X$ | $F_X(x)=\Pr(X\le x)$ |
| $\mathbb{E}[X]$ | expectation of $X$ | weighted average of $X$ |
| $\operatorname{Var}(X)$ | variance of $X$ | $\mathbb{E}[(X-\mathbb{E}X)^2]$ |
| $\sigma_X$ | standard deviation of $X$ | $\sqrt{\operatorname{Var}(X)}$ |
| $\operatorname{Cov}(X,Y)$ | covariance | $\mathbb{E}[XY]-\mathbb{E}[X]\mathbb{E}[Y]$ |
| $\rho(X,Y)$ | correlation | covariance divided by $\sigma_X\sigma_Y$ |
| $\mathbf{1}_A$ | indicator of $A$ | $1$ on $A$, $0$ outside $A$ |
| $\perp\!\!\!\perp$ | independent | $X\perp\!\!\!\perp Y$ means independent |
| $X\sim\operatorname{Bin}(n,p)$ | $X$ is binomial | $n$ trials, success probability $p$ |
| $X\sim\operatorname{Geom}(p)$ | $X$ is geometric | first-success trial number |
| $X\sim\operatorname{Pois}(\lambda)$ | $X$ is Poisson | rate $\lambda$ |
| $H_n$ | $n$-th harmonic number | $\sum_{k=1}^{n}1/k$ |
| $H_n^{(2)}$ | second harmonic number | $\sum_{k=1}^{n}1/k^2$ |
| $P$ | transition matrix | $P_{ij}=\Pr(X_{n+1}=j\mid X_n=i)$ |
| $\pi$ | stationary distribution | a probability vector with $\pi P=\pi$ |

Read $\Pr(A\mid B)$ aloud as "probability of $A$ given $B$". Read $X\sim\operatorname{Bin}(n,p)$ as
"$X$ is distributed as binomial with $n$ trials and success probability $p$".

<!-- CHUNK -->
