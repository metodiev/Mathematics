# Sequences and Series

> [Mathematics](../../README.md) › [Calculus](../README.md) · Level: Advanced · Prerequisites: [Limits](../01-limits/README.md), [Derivatives](../03-derivatives/README.md), [Differentiation Rules](../04-differentiation-rules/README.md), [Integrals](../06-integrals/README.md), [The Fundamental Theorem of Calculus](../07-fundamental-theorem-of-calculus/README.md), [Techniques of Integration](../08-techniques-of-integration/README.md), [Sequences and Series (elementary)](../../06-precalculus/05-sequences-and-series/README.md) · Estimated time: 12 h

## 1. Introduction

The [elementary treatment of sequences and series](../../06-precalculus/05-sequences-and-series/README.md)
answers one question exactly: *when does a geometric series converge, and to what?* It also introduces
sigma notation, arithmetic and geometric sequences, telescoping sums and the binomial theorem. That is
the arithmetic of infinite sums. This topic is the analysis of infinite sums.

Two separate limiting processes are at work, and confusing them is the single most common source of
error in the subject:

1. A **sequence** $(a_n)$ is an ordered list. It has a limit when its terms eventually stay close to a
   number $L$.
2. A **series** $\sum a_n$ is a limit of *partial sums* $S_N = a_1 + a_2 + \cdots + a_N$. It converges
   when the **sequence of partial sums** converges.

Everything else in the topic is a tool for deciding the second question without computing the first.
A typical series has no closed-form sum: nobody knows a formula for $\sum 1/n^3$ in elementary terms.
But the question "does it converge?" is usually answerable by a *test* — a theorem that compares the
unknown series with a series whose behaviour is known. This topic builds that toolkit from scratch:

* **§7.1–7.2** treat sequences: limits, boundedness, monotonicity, and the theorem that a bounded
  monotone sequence must converge. That theorem is the engine behind almost every convergence proof
  in the topic.
* **§7.3–7.9** treat series of numbers. The **divergence test**, the **integral test**, **comparison**,
  the **limit comparison test**, the **ratio test**, the **root test** and the **alternating series
  test** are stated with their exact hypotheses and proved.
* **§7.10–7.12** upgrade sums of numbers to sums of *functions*: power series, their radius and
  interval of convergence, term-by-term differentiation and integration, and Taylor's theorem with the
  Lagrange remainder.
* **§7.13** derives the six standard series and the binomial series, and states the interval on which
  each is valid.
* **§7.14** points forward to Fourier series, which expand a function in a *different basis* and show
  that "Taylor series" is one choice among many.

The subject has a reputation for being a list of tests to memorise. That reputation is undeserved. Each
test is a comparison with a geometric series, an integral, or a monotone bounded sequence, and once the
proofs are understood the tests become predictions: factorials in the coefficients point to the ratio
test, $n$-th powers point to the root test, a decreasing factor in a denominator points to the integral
test, and alternating signs point to the alternating series test.

## 2. Prerequisites

**From [Limits](../01-limits/README.md)** — the $\varepsilon$–$N$ definition of the limit of a sequence,
limit laws, the squeeze theorem, and the standard limits $\lim (1+1/n)^n = e$ and
$\lim_{x\to0}\ln(1+x)/x = 1$. Every proof below uses at least one of these.

**From [Sequences and Series (elementary)](../../06-precalculus/05-sequences-and-series/README.md)** —
sigma notation and its manipulation rules, the finite and infinite geometric series, telescoping sums,
arithmetic and geometric sequences, and the binomial theorem. Those are used constantly and are not
re-derived here.

**From [Derivatives](../03-derivatives/README.md) and
[Differentiation Rules](../04-differentiation-rules/README.md)** — the derivatives of $e^x$, $\sin x$,
$\cos x$, $\ln x$, $\arctan x$ and $(1+x)^\alpha$; the product, quotient and chain rules; the mean value
theorem (used in the proof of Taylor's theorem and in monotonicity arguments).

**From [Integrals](../06-integrals/README.md) and
[The Fundamental Theorem of Calculus](../07-fundamental-theorem-of-calculus/README.md)** — the definite
integral as a limit of Riemann sums, its monotonicity in the integrand, and the fundamental theorem in
both directions. The integral test is a comparison between a sum and an integral, and the derivation of
the series for $\ln(1+x)$ and $\arctan x$ is an application of the fundamental theorem.

**From [Techniques of Integration](../08-techniques-of-integration/README.md)** — partial fractions (for
telescoping series), substitution (for integrals such as $\int dx/(x\ln^2 x)$), and the fact that some
integrals have no elementary antiderivative. That last fact is why series are needed to compute things
like $\int_0^1 e^{-t^2}dt$.

**From algebra and proof** — inequalities, induction, the binomial theorem, and the completeness axiom
of $\mathbb{R}$: every non-empty set of real numbers bounded above has a least upper bound. That axiom
is the source of the monotone convergence theorem, and therefore of the whole subject.

## 3. Learning Objectives

After working through this topic you will be able to:

1. Decide whether a given sequence converges, and compute the limit using limit laws, the squeeze
   theorem, or the monotone convergence theorem.
2. State the monotone convergence theorem with its hypotheses and use it to prove that a recursively
   defined sequence converges (for example $a_{n+1} = \sqrt{2+a_n}$).
3. Write the partial sums of a series, decide convergence from their behaviour, and compute the sum of
   a geometric or telescoping series exactly.
4. Apply the divergence test correctly in one direction only, and explain with a counterexample why the
   converse fails.
5. Apply the integral test, the $p$-series test, direct comparison, and the limit comparison test, and
   verify each hypothesis before using it.
6. Prove and use the ratio test and the root test, identify when each is inconclusive, and give examples
   showing that neither implies the other in general (the root test is stronger).
7. Prove the alternating series test, estimate the error of a truncated alternating series by
   $b_{N+1}$, and distinguish absolute from conditional convergence.
8. Compute the radius of convergence of a power series with the ratio or root formula, and determine the
   interval of convergence **including both endpoints**.
9. Differentiate and integrate a power series term by term inside its interval, and justify the
   operation by uniform convergence.
10. Derive the Maclaurin series of $e^x$, $\sin x$, $\cos x$, $\ln(1+x)$, $1/(1-x)$, $\arctan x$ and
    $(1+x)^\alpha$, state each interval of validity, and use them to compute limits and values.
11. Write Taylor's theorem with the Lagrange remainder, and use it to bound the error of a Taylor
    approximation.
12. Solve a linear ODE with a power-series ansatz and recognise the solution as a known series.

## 4. Intuition

**A series is a journey with a destination.** The partial sums $S_1, S_2, S_3, \dots$ are the positions
of a traveller who takes step $a_1$, then $a_2$, then $a_3$, and so on. The series converges exactly when
the traveller's positions settle down at a point. The individual steps may be large at the beginning; what
matters is that the *remaining journey* becomes arbitrarily small. This is why convergence is a statement
about **tails**: $\sum a_n$ converges if and only if $\sum_{n>N} a_n$ can be made as small as we like by
choosing $N$ large.

**The divergence test is a speed check, not a destination check.** If the steps do not shrink to nothing,
the traveller cannot settle anywhere. But tiny steps are not enough: the harmonic series takes steps
$1, 1/2, 1/3, 1/4, \dots$, each shrinking to zero, and still travels forever. A walker who takes a step of
length $1/n$ at stage $n$ covers infinite ground, because $\sum 1/n$ diverges like $\ln N$.

**Comparisons are measurements against a ruler.** Since all terms of a positive series are non-negative,
the partial sums only increase; the question is whether they are *bounded*. To show boundedness it
suffices to dominate the series by one known to converge; to show unboundedness it suffices to be
dominated *from below* by one known to diverge. Most tests are refined rulers: the integral test uses
$\int f$ as the ruler, the ratio test uses a geometric series with ratio $L<1$, and the root test uses
the $n$-th root to extract that ratio directly.

**Power series are polynomials of infinite degree, and they are rigid.** A power series
$\sum c_n(x-a)^n$ converges on an interval centred at $a$ and diverges outside it; inside, it behaves
like a polynomial — you may differentiate and integrate it term by term — but its coefficients are
locked to its values: $c_n = f^{(n)}(a)/n!$. That rigidity is what makes Taylor series both powerful
(one formula determines the whole function locally) and fragile (a function may be infinitely
differentiable and still not equal its Taylor series).

**Signs change everything.** For a series with terms of both signs, cancellation can rescue a series
whose absolute values diverge: $\sum (-1)^{n+1}/n$ converges although $\sum 1/n$ does not. But
cancellation is delicate: it depends on the *order* of the terms. Rearranging a conditionally convergent
series can change its sum — a fact with no analogue for finite sums.

## 5. Formal Definition

### 5.1 Sequences

**Definition 5.1 (sequence).** A *sequence of real numbers* is a function $a : \mathbb{N} \to \mathbb{R}$.
We write $a_n$ instead of $a(n)$ and denote the sequence by $(a_n)_{n \ge 1}$.

**Definition 5.2 (convergence of a sequence).** A sequence $(a_n)$ *converges* to $L \in \mathbb{R}$ if

$$\forall \varepsilon > 0\ \exists N \in \mathbb{N}\ \forall n \ge N : \quad |a_n - L| < \varepsilon .$$

We then write $\lim_{n\to\infty} a_n = L$, or $a_n \to L$. A sequence that does not converge *diverges*.
It *diverges to $+\infty$*, written $a_n \to +\infty$, if
$\forall M \in \mathbb{R}\ \exists N\ \forall n \ge N : a_n > M$; divergence to $-\infty$ is defined
symmetrically.

**Definition 5.3 (boundedness).** $(a_n)$ is *bounded above* if there is $M$ with $a_n \le M$ for all $n$;
*bounded below* if there is $m$ with $a_n \ge m$ for all $n$; *bounded* if both.

**Definition 5.4 (monotonicity).** $(a_n)$ is *increasing* if $a_{n+1} \ge a_n$ for all $n$, *decreasing*
if $a_{n+1} \le a_n$ for all $n$, and *monotone* if it is one of these. It is *strictly* increasing or
decreasing when the inequalities are strict. A property that holds *eventually* means that it holds for
all $n \ge N$ for some $N$.

**Definition 5.5 (subsequence).** If $n_1 < n_2 < n_3 < \cdots$ are natural numbers, then
$(a_{n_k})_{k\ge1}$ is a *subsequence* of $(a_n)$.

### 5.2 Series

**Definition 5.6 (series and sum).** Given a sequence $(a_n)$, define the *partial sums*

$$S_N := \sum_{n=1}^{N} a_n = a_1 + a_2 + \cdots + a_N .$$

The *series* $\sum_{n=1}^{\infty} a_n$ *converges* if the sequence $(S_N)$ converges to some
$S \in \mathbb{R}$; then $S$ is called the *sum* of the series and we write
$\sum_{n=1}^{\infty} a_n = S$. If $(S_N)$ diverges, the series *diverges*. When $S$ exists, the
*remainder* after $N$ terms is

$$R_N := S - S_N = \sum_{n=N+1}^{\infty} a_n ,$$

and $R_N \to 0$ because $S_N \to S$.

**Definition 5.7 (absolute and conditional convergence).** The series $\sum a_n$ *converges absolutely*
if $\sum |a_n|$ converges. It *converges conditionally* if $\sum a_n$ converges but $\sum |a_n|$
diverges.

**Definition 5.8 (power series, radius and interval of convergence).** A *power series about $a$* is a
series of the form

$$\sum_{n=0}^{\infty} c_n (x-a)^n ,$$

where $c_n \in \mathbb{R}$ are the *coefficients*, $a \in \mathbb{R}$ is the *centre*, and $x$ is a real
variable. The set of $x$ for which it converges is its *interval of convergence*, and the number
$R \in [0, +\infty]$ such that the interval is $(a-R, a+R)$ together with a subset of the two endpoints
is its *radius of convergence*. That this shape always occurs is Theorem 7.16.

**Definition 5.9 (Taylor polynomial and Taylor series).** Let $f$ have $n$ derivatives at $a$. The
*Taylor polynomial of degree $n$ of $f$ at $a$* is

$$T_n(x) := \sum_{k=0}^{n} \frac{f^{(k)}(a)}{k!}(x-a)^k ,$$

and the *Taylor series of $f$ at $a$* is $\sum_{k=0}^{\infty} \frac{f^{(k)}(a)}{k!}(x-a)^k$. When $a = 0$
the series is called a *Maclaurin series*. The function $f$ is *analytic at $a$* if there is $\rho > 0$
with $f(x) = T(x)$ for all $|x-a| < \rho$, where $T$ is its Taylor series at $a$.

## 6. Mathematical Notation

| Symbol | Read aloud | Meaning |
|---|---|---|
| $(a_n)_{n\ge1}$ | "the sequence a-n" | the list $a_1, a_2, a_3, \dots$ |
| $a_n \to L$ | "a-n tends to L" | the sequence converges to $L$ |
| $\lim_{n\to\infty} a_n$ | "the limit as n tends to infinity" | the limit of the sequence |
| $\sum_{n=1}^{\infty} a_n$ | "the sum from n equals one to infinity" | the series, i.e. the limit of partial sums |
| $S_N$ | "S-sub-N" | the $N$-th partial sum |
| $R_N$ | "R-sub-N" | the remainder (tail) after $N$ terms |
| $\lvert a_n\rvert$ | "absolute value of a-n" | magnitude of $a_n$ |
| $\varepsilon$ | "epsilon" | an arbitrary positive tolerance |
| $N$ | "capital N" | a threshold index, usually depending on $\varepsilon$ |
| $\limsup_{n\to\infty} \lvert a_n\rvert^{1/n}$ | "limit superior of the n-th root" | largest subsequential limit; used in the root test and Hadamard's formula |
| $R$ | "radius" | radius of convergence |
| $c_n$ | "c-sub-n" | coefficient of a power series |
| $n!$ | "n factorial" | $n(n-1)\cdots 2\cdot 1$, with $0! = 1$ |
| $\binom{\alpha}{n}$ | "alpha choose n" | $\dfrac{\alpha(\alpha-1)\cdots(\alpha-n+1)}{n!}$ |
| $f^{(n)}$ | "f n-th derivative" | the $n$-th derivative of $f$; $f^{(0)} = f$ |
| $T_n(x)$ | "T-sub-n of x" | Taylor polynomial of degree $n$ |
| $o(1)$, $O(g)$ | "little-oh", "big-oh" | a quantity tending to $0$; a quantity bounded by a multiple of $g$ |
| $a_n \sim b_n$ | "a-n is asymptotic to b-n" | $a_n/b_n \to 1$ |
| $[a,b]$, $(a,b)$ | "closed / open interval" | endpoints included / excluded |
| $\#A$ | "cardinality of A" | number of elements of a finite set |

Two conventions are worth stating because they differ between textbooks. First, this repository uses
$\mathbb{N} = \{1,2,3,\dots\}$; when a series starts at $n=0$ the index range is written explicitly.
Second, $\sum a_n$ without limits means $\sum_{n=1}^{\infty} a_n$ unless the context (for instance a power
series) fixes another starting point. Changing finitely many terms never affects convergence, only the
sum, so the starting index is a bookkeeping matter — but it does affect the value of $S_N$ and hence any
error bound, so the index is always stated when a numerical estimate is asked for.

## 7. Core Concepts

### 7.1 Sequences and their limits

A sequence is a function on $\mathbb{N}$, so the limit theory of functions applies with one change: the
variable only marches forward. Everything in this subsection is a restatement of facts from
[Limits](../01-limits/README.md), collected because the rest of the topic depends on them.

**Theorem 7.1 (limit laws for sequences).** Suppose $a_n \to A$ and $b_n \to B$. Then

$$a_n + b_n \to A + B, \qquad a_n b_n \to AB, \qquad \frac{a_n}{b_n} \to \frac{A}{B}\ \text{ if } B \ne 0
\text{ and } b_n \ne 0 ,$$

and $c\,a_n \to cA$ for every constant $c$.

*Proof.* These are the limit laws of [Limits](../01-limits/README.md) specialised to sequences; the
proofs use one inequality each. For the sum, $|(a_n + b_n) - (A+B)| \le |a_n - A| + |b_n - B|$, and each
term can be made smaller than $\varepsilon/2$ beyond a threshold. For the product, write
$a_nb_n - AB = (a_n - A)b_n + A(b_n - B)$ and use that a convergent sequence is bounded (§7.1 below).
The quotient follows from the product once $1/b_n \to 1/B$, which holds because eventually
$|b_n| \ge |B|/2$, so $|1/b_n - 1/B| = |B - b_n|/(|b_n||B|) \le 2|b_n - B|/B^2$. $\blacksquare$

**Theorem 7.2 (squeeze theorem).** If $a_n \le c_n \le b_n$ eventually and $a_n \to L$, $b_n \to L$, then
$c_n \to L$.

*Proof.* Given $\varepsilon > 0$, choose $N$ so that $|a_n - L| < \varepsilon$ and $|b_n - L| < \varepsilon$
for $n \ge N$; then $L - \varepsilon < a_n \le c_n \le b_n < L + \varepsilon$. $\blacksquare$

**Proposition 7.3 (convergent implies bounded).** Every convergent sequence is bounded. The converse is
false: $a_n = (-1)^n$ is bounded and divergent.

*Proof.* Let $a_n \to L$ and take $\varepsilon = 1$. There is $N$ with $|a_n - L| < 1$, hence
$|a_n| < |L| + 1$, for all $n \ge N$. Let $M = \max\{|a_1|, \dots, |a_{N-1}|, |L|+1\}$; then
$|a_n| \le M$ for every $n$. For the counterexample, $(-1)^n$ alternates between $1$ and $-1$, so it
cannot stay within $\tfrac12$ of any single number. $\blacksquare$

**Theorem 7.4 (monotone convergence).** Let $(a_n)$ be increasing and bounded above. Then $(a_n)$
converges, and $\lim a_n = \sup\{a_n : n \ge 1\}$. Dually, a decreasing sequence bounded below converges
to its infimum.

*Proof.* Let $L = \sup\{a_n\}$, which exists by the completeness axiom of $\mathbb{R}$ because the set is
non-empty and bounded above. Let $\varepsilon > 0$. Since $L - \varepsilon$ is not an upper bound, there
is $N$ with $a_N > L - \varepsilon$. For $n \ge N$ monotonicity gives
$L - \varepsilon < a_N \le a_n \le L$, so $|a_n - L| < \varepsilon$. The decreasing case follows by
applying the increasing case to $(-a_n)$, or directly with the infimum. $\blacksquare$

This theorem is the workhorse of the whole topic. It converts *boundedness* — a statement about all $n$
at once — into *convergence*, without any need to guess the limit. It is also equivalent to the
completeness axiom: any proof of convergence that does not use completeness is either a comparison with
an explicit limit or incomplete.

**Example 7.5 ($n$-th roots tend to $1$).** $\lim_{n\to\infty} n^{1/n} = 1$.

*Proof.* Write $n^{1/n} = 1 + h_n$ with $h_n \ge 0$. For $n \ge 2$ the binomial theorem gives

$$n = (1+h_n)^n \ge 1 + \binom{n}{2}h_n^2 = 1 + \frac{n(n-1)}{2}h_n^2 ,$$

so $h_n^2 \le \dfrac{2(n-1)}{n(n-1)} = \dfrac{2}{n}$ after dropping the $1$ and dividing by
$\tfrac{n(n-1)}{2}$. Thus $0 \le h_n \le \sqrt{2/n} \to 0$ by the squeeze theorem, and $n^{1/n} \to 1$.
$\blacksquare$

**Example 7.6 (the number $e$).** The sequence $a_n = \left(1 + \frac1n\right)^n$ is increasing and bounded
above by $3$, so it converges; its limit is by definition $e \approx 2.71828$.

*Sketch.* Expanding by the binomial theorem,

$$a_n = \sum_{k=0}^{n}\binom{n}{k}\frac{1}{n^k} = \sum_{k=0}^{n}\frac{1}{k!}\prod_{j=1}^{k-1}\left(1-\frac{j}{n}\right).$$

Each factor $\left(1-\frac{j}{n}\right)$ increases with $n$, and the sum gains a new positive term when $n$
increases, so $a_n$ increases. Bounding each product by $1$ gives
$a_n \le \sum_{k=0}^{n} 1/k! \le 1 + 1 + \sum_{k=2}^{n} 2^{-k+1} < 3$. By Theorem 7.4 the sequence
converges. $\blacksquare$

**Example 7.7 (a recursive sequence).** Let $a_1 = 1$ and $a_{n+1} = \sqrt{2 + a_n}$. Then
$a_n \to 2$.

*Solution.* First, $1 \le a_n \le 2$ for all $n$ by induction: $a_1 = 1$, and if $1 \le a_n \le 2$ then
$2 \le 2+a_n \le 4$, so $1 \le \sqrt2 \le a_{n+1} \le 2$. Second, $(a_n)$ is increasing:
$a_{n+1} \ge a_n \iff 2 + a_n \ge a_n^2 \iff (a_n - 2)(a_n + 1) \le 0$, which holds because
$a_n \le 2$. Hence $L = \lim a_n$ exists by Theorem 7.4, and passing to the limit in the recursion
(using continuity of the square root) gives $L = \sqrt{2+L}$, so $L^2 - L - 2 = 0$, i.e.
$(L-2)(L+1) = 0$. Since $L \ge 1$, $L = 2$. $\blacksquare$

### 7.2 Series, geometric series, and telescoping

The definition of a series has already been given (Definition 5.6). Two remarks make it usable.

**Proposition 7.8 (linearity).** If $\sum a_n$ and $\sum b_n$ converge, then for all constants
$\alpha, \beta$ the series $\sum(\alpha a_n + \beta b_n)$ converges and

$$\sum_{n=1}^{\infty}(\alpha a_n + \beta b_n) = \alpha\sum_{n=1}^{\infty} a_n + \beta\sum_{n=1}^{\infty} b_n .$$

*Proof.* The partial sums satisfy $\sum_{n\le N}(\alpha a_n + \beta b_n) = \alpha S_N^{(a)} + \beta S_N^{(b)}$;
apply Theorem 7.1. $\blacksquare$

Note that linearity says nothing when one of the series diverges: the sum of a convergent and a divergent
series always diverges, because if it converged, subtracting the convergent part would make the divergent
part converge.

**Theorem 7.9 (geometric series).** For $a \ne 0$ and $r \in \mathbb{R}$,

$$\sum_{n=0}^{\infty} a r^n = \frac{a}{1-r}\quad\text{if } |r| < 1,$$

and the series diverges if $|r| \ge 1$.

*Proof.* The finite identity $\sum_{n=0}^{N-1} ar^n = a\dfrac{1-r^N}{1-r}$ (for $r \ne 1$) is proved by
multiplying by $1-r$ and cancelling. If $|r|<1$ then $r^N \to 0$, so the partial sums tend to
$a/(1-r)$. If $r = 1$ the partial sums are $Na \to \pm\infty$. If $r = -1$ they alternate between $a$ and
$0$. If $|r|>1$ then $|ar^n| = |a||r|^n \to \infty$, so the terms do not tend to $0$ and the series
diverges by Theorem 7.10 below. $\blacksquare$

**Theorem 7.10 (divergence test).** If $\sum a_n$ converges, then $a_n \to 0$. Equivalently, if $a_n$ does
not tend to $0$, then $\sum a_n$ diverges.

*Proof.* Let $S_N \to S$. Then $a_N = S_N - S_{N-1}$ for $N \ge 2$, and by Theorem 7.1
$a_N \to S - S = 0$. $\blacksquare$

The divergence test is **one-directional**. Its converse is false, and the standard counterexample is the
harmonic series.

**Theorem 7.11 (harmonic series diverges).** $\displaystyle\sum_{n=1}^{\infty}\frac1n = \infty$.

*Proof (grouping).* Group the terms into blocks whose lengths double:

$$S_{2^m} = 1 + \frac12 + \left(\frac13+\frac14\right) + \left(\frac15+\cdots+\frac18\right) + \cdots
+ \left(\frac{1}{2^{m-1}+1}+\cdots+\frac{1}{2^m}\right).$$

The $k$-th block, from $2^{k-1}+1$ to $2^k$, contains $2^{k-1}$ terms, each at least $1/2^k$, so its sum is
at least $2^{k-1}/2^k = 1/2$. Hence $S_{2^m} \ge 1 + \frac{m}{2} \to \infty$. Since the partial sums are
increasing, they are unbounded and the series diverges. $\blacksquare$

**Theorem 7.12 (telescoping series).** If $(b_n)$ is a sequence with $b_n \to b$, then
$\sum_{n=1}^{\infty}(b_n - b_{n+1}) = b_1 - b$; if $b_n \to \pm\infty$ the series diverges to
$\mp\infty$ respectively.

*Proof.* $S_N = \sum_{n=1}^{N}(b_n - b_{n+1}) = b_1 - b_{N+1}$ by cancellation. $\blacksquare$

**Proposition 7.13 (tails).** For any $N_0$, the series $\sum_{n\ge1} a_n$ converges if and only if
$\sum_{n>N_0} a_n$ converges, and then
$\sum_{n\ge1}a_n = S_{N_0} + \sum_{n>N_0}a_n$.

*Proof.* For $N > N_0$ the partial sums of the tail equal $S_N - S_{N_0}$; adding the constant $S_{N_0}$
does not affect convergence. $\blacksquare$

Proposition 7.13 is what allows every test below to ignore finitely many terms: hypotheses such as
"$f$ is decreasing" or "$a_n > 0$" only need to hold *eventually*.

### 7.3 Series with non-negative terms

Almost every convergence test reduces to the following observation.

**Theorem 7.14 (bounded partial sums).** If $a_n \ge 0$ for all $n$, then $\sum a_n$ converges if and only
if the sequence of partial sums $(S_N)$ is bounded above. In that case
$\sum a_n = \sup_N S_N$.

*Proof.* With non-negative terms, $S_{N+1} = S_N + a_{N+1} \ge S_N$, so $(S_N)$ is increasing. By Theorem
7.4 it converges if and only if it is bounded above, and its limit is the supremum. $\blacksquare$

Consequently, for a series of non-negative terms there are only two possibilities: it converges, or it
diverges to $+\infty$. There is no oscillation and no conditional convergence. Every test in §7.5–7.8 is a
device for deciding boundedness of $(S_N)$ without computing $S_N$.

### 7.4 The integral test

**Theorem 7.15 (integral test).** Let $f : [1, \infty) \to \mathbb{R}$ be continuous, positive and
decreasing, and let $a_n = f(n)$. Then

$$\sum_{n=1}^{\infty} a_n \ \text{converges} \iff \int_1^{\infty} f(x)\,dx \ \text{converges},$$

where the improper integral converges means that $\lim_{R\to\infty}\int_1^R f(x)\,dx$ exists and is finite.

*Proof.* For $k \ge 1$ and $x \in [k, k+1]$ monotonicity gives $f(k+1) \le f(x) \le f(k)$. Integrating
over $[k,k+1]$ preserves the inequalities because the interval has length $1$:

$$f(k+1) \le \int_k^{k+1} f(x)\,dx \le f(k).$$

Summing for $k = 1, \dots, N-1$,

$$\sum_{k=2}^{N} f(k) \ \le\ \int_1^{N} f(x)\,dx \ \le\ \sum_{k=1}^{N-1} f(k),$$

that is, $A_N - a_1 \le I_N \le A_{N-1}$, where $A_N = S_N$ and $I_N = \int_1^N f$. Hence

$$A_N \le a_1 + I_N \qquad\text{and}\qquad A_{N-1} \ge I_N .$$

Both $(A_N)$ and $(I_N)$ are non-decreasing, since $f > 0$. If $I_N \to I < \infty$, then $A_N \le a_1 + I$
for all $N$, so the partial sums are bounded and the series converges by Theorem 7.14. If $I_N \to \infty$,
then $A_{N-1} \ge I_N \to \infty$, so the series diverges. $\blacksquare$

**Corollary 7.15.1 ($p$-series).** $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n^p}$ converges if and only if
$p > 1$.

*Proof.* For $p \le 0$ the terms $n^{-p}$ do not tend to $0$, so the series diverges by Theorem 7.10. For
$p > 0$ apply Theorem 7.15 to $f(x) = x^{-p}$, which is continuous, positive and decreasing on
$[1,\infty)$. If $p \ne 1$,

$$\int_1^{R} x^{-p}\,dx = \frac{R^{1-p} - 1}{1-p},$$

which has a finite limit as $R \to \infty$ exactly when $1 - p < 0$, i.e. $p > 1$. For $p = 1$,
$\int_1^R x^{-1}dx = \ln R \to \infty$. $\blacksquare$

The two boundary cases deserve names: $\sum 1/n$ (the harmonic series) diverges, and $\sum 1/n^2$
converges. The $p$-series is the reference ruler for the comparison tests.

**Example 7.15.2.** $\displaystyle\sum_{n=2}^{\infty}\frac{1}{n\ln n}$ diverges, while
$\displaystyle\sum_{n=2}^{\infty}\frac{1}{n(\ln n)^2}$ converges.

*Solution.* With $u = \ln x$, $du = dx/x$,

$$\int_2^{R}\frac{dx}{x(\ln x)^p} = \int_{\ln 2}^{\ln R}\frac{du}{u^p}.$$

For $p = 1$ this is $\ln\ln R - \ln\ln 2 \to \infty$; for $p = 2$ it is
$\dfrac{1}{\ln 2} - \dfrac{1}{\ln R} \to \dfrac{1}{\ln 2} \approx 1.4427$. The integrands are positive and
decreasing for $x \ge 2$, so Theorem 7.15 applies. In particular the second series converges — but *not*
to $1/\ln 2$: the integral is only a comparison object, not the sum. Numerically the sum is about
$1.94$, comfortably between $\int_2^\infty f = 1.4427$ and $f(2) + \int_2^\infty f \approx 2.48$, exactly
as the proof of Theorem 7.15 predicts. $\blacksquare$

<!--NEXT-->
