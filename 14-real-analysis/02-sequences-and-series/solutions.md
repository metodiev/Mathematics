# Sequences and Series of Real Numbers — Solutions

> [Tutorial](README.md) · [Exercises](exercises.md) · Complete solutions to all 38 problems

Results are cited by their numbers in the [tutorial](README.md). Every limit proof either exhibits
an $N(\varepsilon)$ or names a theorem and checks its hypotheses.

## Beginner

### Solution 1

*Strategy.* Subtract the candidate limit and simplify, exactly as in Example 9.1.

$$
\frac{4n+1}{n+2} - 4 = \frac{4n + 1 - 4n - 8}{n+2} = \frac{-7}{n+2}, \qquad
\left\lvert\frac{4n+1}{n+2} - 4\right\rvert = \frac{7}{n+2} \le \frac7n .
$$
Let $\varepsilon > 0$ and choose $N \in \mathbb{N}$ with $N > 7/\varepsilon$ (Archimedean property). For
$n \ge N$,
$$
\left\lvert \frac{4n+1}{n+2} - 4\right\rvert \le \frac7n \le \frac7N < \varepsilon .
$$
So the limit is $4$. $\blacksquare$

### Solution 2

*Strategy.* Bound the denominator from below to get a bound in terms of $1/n$.

Since $n^2 + 1 > n^2$,
$$
\left\lvert\frac{1}{n^2+1} - 0\right\rvert = \frac{1}{n^2+1} < \frac{1}{n^2} \le \frac1n .
$$
Given $\varepsilon > 0$, take $N > 1/\varepsilon$; for $n \ge N$, $\lvert a_n\rvert \le 1/n \le 1/N < \varepsilon$. $\blacksquare$

### Solution 3

*Strategy.* The sign alternates, but the absolute value does not.

$$
\left\lvert \frac{(-1)^n}{n} - 0\right\rvert = \frac1n .
$$
Given $\varepsilon > 0$, choose $N > 1/\varepsilon$; then for $n \ge N$, $\lvert a_n\rvert = 1/n \le 1/N < \varepsilon$. $\blacksquare$

### Solution 4

*Strategy.* The distance is *zero*, so any $N$ works.

For every $n$, $\lvert a_n - c\rvert = \lvert c - c\rvert = 0 < \varepsilon$ for every $\varepsilon > 0$.
Taking $N = 1$ satisfies Definition 5.2. $\blacksquare$

### Solution 5

*Strategy.* Negate the definition with $\varepsilon = 1$ and show no candidate $L$ survives.

Suppose $a_n = n \to L$. Take $\varepsilon = 1$; there is $N$ with $\lvert n - L\rvert < 1$ for all
$n \ge N$. Choose the integer $n = N + \lceil \lvert L\rvert\rceil + 1 \ge N$. Then
$$
\lvert n - L\rvert \ge n - \lvert L\rvert = N + \lceil\lvert L\rvert\rceil + 1 - \lvert L\rvert \ge N + 1 \ge 1 ,
$$
contradicting $\lvert n - L\rvert < 1$. So the sequence diverges. $\blacksquare$

*Remark.* This is the same content as "a convergent sequence is bounded" (Theorem 7.5), but the
exercise asks for the definition to be used directly; both arguments have the same shape.

### Solution 6

*Strategy.* Divide numerator and denominator by $n^2$ and apply the algebra of limits, checking that
the denominator's limit is nonzero.

For $n \ge 3$ (so $n^2 - 4 \ne 0$),
$$
\frac{3n^2+5n}{n^2-4} = \frac{3 + \frac5n}{1 - \frac{4}{n^2}} .
$$
Now $1/n \to 0$ (Example 7.1), so $5/n \to 0$ (scalar rule) and $3 + 5/n \to 3$ (sum rule).
Similarly $1/n^2 = (1/n)(1/n) \to 0$ by the product rule, so $4/n^2 \to 0$ and $1 - 4/n^2 \to 1$.
Since the denominator has nonzero limit $1$, the quotient rule (Theorem 7.9) gives
$$
\frac{3n^2+5n}{n^2-4} \to \frac{3}{1} = 3 . \qquad \blacksquare
$$

### Solution 7

*Strategy.* Compare with $1/\sqrt n$ and squeeze.

For $n \ge 1$, $\sqrt n \le n$, hence
$$
0 \le \frac{\sqrt n}{n+1} \le \frac{\sqrt n}{n} = \frac{1}{\sqrt n} .
$$
Given $\varepsilon > 0$, choose $N > 1/\varepsilon^2$; for $n \ge N$, $1/\sqrt n \le 1/\sqrt N < \varepsilon$.
By the squeeze theorem (Theorem 7.10) the limit is $0$. $\blacksquare$

### Solution 8

*Strategy.* Exhibit two subsequences with different limits.

The values are periodic with period $4$:
$$
\cos\frac{\pi}{2} = 0,\quad \cos\pi = -1,\quad \cos\frac{3\pi}{2} = 0,\quad \cos 2\pi = 1,\quad \cos\frac{5\pi}{2} = 0,\ \dots
$$
Hence $a_{4k} = \cos(2k\pi) = 1 \to 1$ and $a_{4k+2} = \cos((2k+1)\pi) = -1 \to -1$. Two subsequences
have different limits, so the sequence diverges (if it converged to $L$, Theorem 7.18 would force
both subsequences to converge to $L$). $\blacksquare$

### Solution 9

*Strategy.* The partial sums are $1, 0, 1, 0, \dots$, which has no limit.

$$
S_1 = 1,\quad S_2 = 1 - 1 = 0,\quad S_3 = 1,\quad S_4 = 0 .
$$
In general $S_N = 1$ for odd $N$ and $S_N = 0$ for even $N$. The even partial sums converge to $0$ and
the odd ones to $1$; by Theorem 7.18 the sequence $(S_N)$ diverges, so the series diverges. (Equivalently:
the terms $(-1)^{n+1}$ do not tend to $0$, so the term test, Corollary 7.34, applies.) $\blacksquare$

### Solution 10

*Strategy.* Geometric series, Example 7.32.

For $\lvert q\rvert < 1$, $\sum_{n=0}^{\infty}q^n = 1/(1-q)$. With $q = 2/3$: $\sum_{n\ge0}(2/3)^n = 1/(1/3) = 3$.
With $q = 1/3$ but starting at $n = 1$:
$$
\sum_{n=1}^{\infty}\left(\frac13\right)^n = \frac{1/3}{1 - 1/3} = \frac{1/3}{2/3} = \frac12 . \qquad \blacksquare
$$

### Solution 11

*Strategy.* Factor out the constant and use the divergence of the harmonic series.

The partial sums satisfy $\sum_{n=1}^{N}\frac{1}{3n} = \frac13\sum_{n=1}^N\frac1n = \frac13 H_N$. If the
series converged, then $(H_N) = 3\cdot(\frac13 H_N)$ would converge by the scalar rule (Theorem 7.7),
contradicting Theorem 7.38. Hence $\sum 1/(3n)$ diverges. $\blacksquare$

### Solution 12

*Strategy.* Split into two geometric series and add the sums.

Both series converge (Example 7.32 with $q = 1/2$ and $q = 1/3$), so the sum rule for series
(partial sums of a sum are sums of partial sums) gives
$$
\sum_{n=1}^{\infty}\left(\frac{1}{2^n} + \frac{1}{3^n}\right)
= \sum_{n=1}^{\infty}\frac{1}{2^n} + \sum_{n=1}^{\infty}\frac{1}{3^n}
= 1 + \frac12 = \frac32 ,
$$
using $\sum_{n\ge1}2^{-n} = (1/2)/(1-1/2) = 1$ and Solution 10. $\blacksquare$

### Solution 13

*Strategy.* A convergent sequence is bounded (Theorem 7.5).

Suppose $(a_n)$ converges. By Theorem 7.5 there is $M$ with $\lvert a_n\rvert \le M$ for all $n$, i.e.
$(a_n)$ is bounded. Hence an unbounded sequence cannot converge. $\blacksquare$

## Intermediate

### Solution 14

*Strategy.* Split the average into an initial finite block, which is killed by dividing by $n$, and a
tail block, which is small because $a_n$ is close to $L$.

Let $\varepsilon > 0$. Choose $N_1$ with $\lvert a_k - L\rvert < \varepsilon/2$ for all $k \ge N_1$. Put
$C = \sum_{k=1}^{N_1-1}\lvert a_k - L\rvert \ge 0$ (a finite sum, hence a finite number). For $n > N_1$,
$$
\left\lvert \frac{a_1 + \cdots + a_n}{n} - L\right\rvert
= \frac{1}{n}\left\lvert \sum_{k=1}^{n}(a_k - L)\right\rvert
\le \frac{1}{n}\sum_{k=1}^{N_1-1}\lvert a_k - L\rvert + \frac{1}{n}\sum_{k=N_1}^{n}\lvert a_k - L\rvert
\le \frac{C}{n} + \frac{\varepsilon}{2}.
$$
Choose $N \ge N_1$ with $C/N < \varepsilon/2$ (Archimedean property). For $n \ge N$ the left side is
$< \varepsilon$. Hence the Cesàro means converge to $L$. $\blacksquare$

*Remark.* The converse fails: $a_n = (-1)^n$ has means converging to $0$ while $(a_n)$ diverges. So
taking averages genuinely regularises an oscillating sequence.

### Solution 15

*Strategy.* Boundedness converts the product into a constant multiple of $\lvert a_n\rvert$.

Let $M \ge 0$ with $\lvert b_n\rvert \le M$ for all $n$. Then
$$
0 \le \lvert a_nb_n\rvert \le M\lvert a_n\rvert \longrightarrow 0 ,
$$
by the scalar rule and Theorem 7.12, so the squeeze theorem (Theorem 7.10) gives $a_nb_n \to 0$.
$\blacksquare$

### Solution 16

*Strategy.* Monotone convergence: prove by induction that $a_n < 2$ and $a_n < a_{n+1}$, then pass to
the limit in the recursion.

*Bounded above.* $a_1 = \sqrt2 < 2$. If $a_n < 2$ then $2a_n < 4$, so $a_{n+1} = \sqrt{2a_n} < 2$.

*Increasing.* Since $0 < a_n < 2$,
$$
a_{n+1} \ge a_n \iff \sqrt{2a_n} \ge a_n \iff 2a_n \ge a_n^2 \iff a_n(2 - a_n) \ge 0 ,
$$
which holds. So $(a_n)$ is nondecreasing and bounded above by $2$; by Theorem 7.13 it converges. Let
$L = \lim a_n$. Then $L \ge a_1 = \sqrt 2 > 0$ (Theorem 7.11) and, by the root rule (Theorem 7.12)
applied to $2a_n \to 2L$,
$$
L = \sqrt{2L} \implies L^2 = 2L \implies L(L-2) = 0 .
$$
Since $L \ge \sqrt2 > 0$, $L = 2$. $\blacksquare$

### Solution 17

*Strategy.* Compute the first terms, guess, and prove by induction; convergence then follows from
$1/n \to 0$.

*Claim:* $a_n = 1/n$. For $n = 1$: $a_1 = 1 = 1/1$. If $a_n = 1/n$ then
$$
a_{n+1} = \frac{1/n}{1 + 1/n} = \frac{1/n}{(n+1)/n} = \frac{1}{n+1} .
$$
By induction $a_n = 1/n$ for all $n$, and $a_n \to 0$ by Example 7.1. $\blacksquare$

### Solution 18

*Strategy.* Separate the two parities; the sequence is unbounded above but bounded below by $0$.

For odd $n$, $1 + (-1)^n = 0$, so $a_n = 0$. For even $n = 2k$, $1 + (-1)^n = 2$, so $a_n = n = 2k$.

*$\limsup = +\infty$.* The tail set $\{a_m : m \ge n\}$ contains the even numbers $\ge n$, which are
arbitrarily large, so $s_n = \sup\{a_m : m \ge n\} = +\infty$ for every $n$; hence $\limsup a_n = +\infty$
in the extended sense.

*$\liminf = 0$.* Every term is $\ge 0$ and odd terms equal $0$, so $i_n = \inf\{a_m : m \ge n\} = 0$
for every $n$, and $\liminf a_n = 0$. $\blacksquare$

*Remark.* The subsequences $a_{2k} = 2k$ and $a_{2k-1} = 0$ show the divergence directly.

### Solution 19

*Strategy.* The values form the periodic pattern $1, 0, -1, 0, 1, \dots$

$$
\sin\frac{\pi}{2} = 1,\quad \sin\pi = 0,\quad \sin\frac{3\pi}{2} = -1,\quad \sin 2\pi = 0,
$$
and the pattern repeats with period $4$. Hence the set of values is $\{1, 0, -1\}$, and each value
occurs infinitely often. For every $n$ the tail contains all three values, so
$$
s_n = 1, \qquad i_n = -1 \quad \text{for all } n ,
$$
and therefore $\limsup a_n = 1$, $\liminf a_n = -1$. The subsequences $a_{4k} \to 1$ and
$a_{4k+2} \to -1$ confirm the divergence. $\blacksquare$

### Solution 20

*Strategy.* Compare tail suprema, then exhibit a case where the two sides differ.

*Proof of the inequality.* Put $s_n = \sup_{k\ge n}a_k$, $t_n = \sup_{k \ge n}b_k$. For $k \ge n$,
$a_k + b_k \le s_n + t_n$, so $s_n + t_n$ is an upper bound of the tail of $(a_n + b_n)$ and therefore
$$
\sup_{k\ge n}(a_k + b_k) \le s_n + t_n .
$$
Letting $n \to \infty$ and using the sum rule and Theorem 7.11,
$$
\limsup(a_n+b_n) = \lim_n \sup_{k\ge n}(a_k+b_k) \le \lim_n s_n + \lim_n t_n = \limsup a_n + \limsup b_n .
$$

*Strict example.* Take $a_n = (-1)^n$ and $b_n = (-1)^{n+1} = -a_n$. Then $a_n + b_n = 0$ for all $n$, so
$\limsup(a_n+b_n) = 0$, while $\limsup a_n = 1$ and $\limsup b_n = 1$, so the right side is $2$. Hence
$$
0 = \limsup(a_n+b_n) < 2 = \limsup a_n + \limsup b_n . \qquad \blacksquare
$$
The failure is caused by the two sequences peaking at different indices.

### Solution 21

*Strategy.* Absolute convergence by comparison, then Theorem 7.35.

Let $M$ with $\lvert b_n\rvert \le M$ for all $n$. Then $\lvert a_nb_n\rvert \le M\lvert a_n\rvert$, and
$\sum M\lvert a_n\rvert$ converges by the scalar rule for series. By the comparison test (Theorem 7.36),
$\sum\lvert a_nb_n\rvert$ converges. By Theorem 7.35, $\sum a_nb_n$ converges. $\blacksquare$

### Solution 22

*Strategy.* Compare with $1/n^2$.

For $n \ge 1$,
$$
0 \le \frac{n+1}{n^3+2} \le \frac{n+1}{n^3} \le \frac{2n}{n^3} = \frac{2}{n^2}.
$$
Since $\sum 2/n^2$ converges ($p$-series with $p = 2 > 1$, Corollary 7.43), the comparison test
(Theorem 7.36) gives convergence. $\blacksquare$

### Solution 23

*Strategy.* The ratio test, since the terms grow like $(2+\varepsilon)^n$ against a polynomial.

With $a_n = 2^n/n^2 > 0$,
$$
\frac{a_{n+1}}{a_n} = \frac{2^{n+1}}{(n+1)^2}\cdot\frac{n^2}{2^n} = 2\left(\frac{n}{n+1}\right)^2 \longrightarrow 2 \cdot 1 = 2 > 1 .
$$
By the ratio test (Theorem 7.39) the series diverges. (Directly: $a_n = 2^n/n^2 \to \infty$, so the terms
do not tend to $0$.) $\blacksquare$

### Solution 24

*Strategy.* Alternating series test for convergence; comparison with the harmonic series for the
failure of absolute convergence.

Let $b_n = 1/(2n+1)$. Then $b_n > 0$, $b_{n+1} < b_n$, and $b_n \to 0$ (quotient rule and
$1/(2n+1) \le 1/n \to 0$, squeeze). By Theorem 7.44 the series converges. Its sum lies between
$S_1 = -1/3$ and $S_2 = -1/3 + 1/5 = -2/15$, and the error after $N$ terms is at most $1/(2N+3)$.

*Not absolutely convergent.* For $n \ge 1$, $2n + 1 \le 3n$, so
$$
\frac{1}{2n+1} \ge \frac{1}{3n},
$$
and $\sum 1/(3n)$ diverges (Solution 11). By the comparison test, $\sum 1/(2n+1)$ diverges. So the
series converges conditionally. $\blacksquare$

## Advanced

### Solution 25

*Strategy.* (a) Absolute convergence forces the terms to be small, and small numbers have small squares.
(b) A single counterexample suffices.

(a) Since $\sum\lvert a_n\rvert$ converges, the term test (Corollary 7.34) gives $a_n \to 0$. Hence there
is $N$ with $\lvert a_n\rvert \le 1$ for all $n \ge N$. For such $n$,
$$
0 \le a_n^2 = \lvert a_n\rvert^2 \le \lvert a_n\rvert .
$$
By the comparison test (Theorem 7.36), $\sum a_n^2$ converges.

(b) Take $a_n = 1/n$. Then $\sum a_n^2 = \sum 1/n^2$ converges ($p = 2 > 1$), while $\sum a_n = \sum 1/n$
diverges (Theorem 7.38). So the converse fails. $\blacksquare$

*Remark.* The hypothesis "eventually $\lvert a_n\rvert \le 1$" is what makes (a) work; for a merely
convergent series the terms can oscillate in sign and the squares need not be comparable.

### Solution 26

*Strategy.* The arithmetic–geometric mean inequality splits the product $\sqrt{a_n}\cdot\frac1n$ into
the two convergent pieces $a_n$ and $1/n^2$.

For every $n \ge 1$, by AM–GM applied to $x = a_n$ and $y = 1/n^2$,
$$
\frac{\sqrt{a_n}}{n} = \sqrt{a_n\cdot\frac{1}{n^2}} \le \frac{1}{2}\left(a_n + \frac{1}{n^2}\right).
$$
The series $\sum \tfrac12 a_n$ converges by hypothesis and $\sum \tfrac{1}{2n^2}$ converges by the
$p$-series test. By the comparison test (Theorem 7.36) applied to nonnegative terms,
$\sum \sqrt{a_n}/n$ converges. $\blacksquare$

*Remark.* The same device proves that $\sum a_n^{p}$ converges for every $p > 1$ when $\sum a_n$
converges and $a_n \ge 0$: eventually $a_n \le 1$, so $a_n^p \le a_n$.

### Solution 27

*Strategy.* Iterate the ratio bound to compare $a_n$ with geometric sequences, then take $n$-th roots;
the fixed factor $a_N$ disappears because $a_N^{1/n} \to 1$.

*Lemma.* For every fixed $c > 0$, $c^{1/n} \to 1$.
*Proof.* If $c \ge 1$, write $c^{1/n} = 1 + h_n$ with $h_n \ge 0$. By Bernoulli's inequality
$$
c = (1+h_n)^n \ge 1 + n h_n, \quad\text{so}\quad 0 \le h_n \le \frac{c-1}{n} \to 0 .
$$
If $0 < c < 1$, apply the result to $1/c$ and use the quotient rule.

*Case $0 < L < \infty$.* Let $0 < \varepsilon < L$. Choose $N$ with
$$
L - \varepsilon < \frac{a_{n+1}}{a_n} < L + \varepsilon \qquad (n \ge N).
$$
Iterating from $N$ to $n > N$,
$$
a_N (L-\varepsilon)^{n-N} \le a_n \le a_N (L+\varepsilon)^{n-N},
$$
because $a_n = a_N\prod_{k=N}^{n-1}\frac{a_{k+1}}{a_k}$ and each factor lies between $L-\varepsilon$ and
$L+\varepsilon$. Taking $n$-th roots,
$$
a_N^{1/n}\,(L-\varepsilon)^{1 - N/n} \le a_n^{1/n} \le a_N^{1/n}\,(L+\varepsilon)^{1 - N/n}.
$$
As $n \to \infty$: $a_N^{1/n} \to 1$ by the lemma, and
$$
(L\pm\varepsilon)^{1-N/n} = (L\pm\varepsilon)\cdot\bigl((L\pm\varepsilon)^{N}\bigr)^{-1/n} \longrightarrow L \pm \varepsilon ,
$$
again by the lemma applied to the fixed positive number $(L\pm\varepsilon)^N$. Hence
$$
L - \varepsilon \le \liminf a_n^{1/n} \le \limsup a_n^{1/n} \le L + \varepsilon .
$$
Since $\varepsilon \in (0,L)$ is arbitrary, $a_n^{1/n} \to L$.

*Case $L = 0$.* Let $\varepsilon > 0$ and choose $N$ with $a_{n+1}/a_n < \varepsilon$ for $n \ge N$. Then
$a_n \le a_N\varepsilon^{n-N}$ for $n \ge N$, so
$$
a_n^{1/n} \le a_N^{1/n}\,\varepsilon^{1-N/n} \longrightarrow \varepsilon .
$$
Hence $\limsup a_n^{1/n} \le \varepsilon$ for every $\varepsilon > 0$, so $a_n^{1/n} \to 0$. $\blacksquare$

### Solution 28

*Strategy.* Group the terms between consecutive powers of $2$: each block has $2^k$ terms, all
comparable to $a_{2^k}$.

Write $S_N = \sum_{n=1}^{N}a_n$ and $T_K = \sum_{k=0}^{K}2^k a_{2^k}$; both are nondecreasing sequences
(all terms are $\ge 0$).

*Block estimate.* For $k \ge 0$ the block $\{2^k, 2^k+1, \dots, 2^{k+1}-1\}$ has $2^k$ terms. Since
$(a_n)$ is nonincreasing, each term of the block is at most $a_{2^k}$ and at least $a_{2^{k+1}-1} \ge a_{2^{k+1}}$. Hence
$$
2^k a_{2^{k+1}} \le \sum_{n=2^k}^{2^{k+1}-1} a_n \le 2^k a_{2^k}.
$$

*Summing the blocks.* Summing the left inequality for $k = 0, \dots, K$,
$$
\tfrac12\left(T_{K+1} - a_1\right) = \sum_{k=0}^{K}2^k a_{2^{k+1}} \le \sum_{n=1}^{2^{K+1}-1} a_n = S_{2^{K+1}-1},
$$
where $T_{K+1} - a_1 = \sum_{k=1}^{K+1}2^k a_{2^k}$. Summing the right inequality,
$$
S_{2^{K+1}-1} \le \sum_{k=0}^{K} 2^k a_{2^k} = T_K .
$$
So for all $K$,
$$
\frac{T_{K+1} - a_1}{2} \le S_{2^{K+1}-1} \le T_K .
$$

*Conclusion.* If $(T_K)$ is bounded then $(S_N)$ is bounded (the subsequence $(S_{2^{K+1}-1})$ is
bounded and $(S_N)$ is nondecreasing, so $S_N \le S_{2^{K+1}-1}$ for the first $K$ with $N \le 2^{K+1}-1$);
by the monotone convergence theorem $\sum a_n$ converges. Conversely, if $(S_N)$ is bounded by $B$,
then $T_{K+1} \le 2B + a_1$, so $(T_K)$ is bounded and $\sum 2^k a_{2^k}$ converges. $\blacksquare$

### Solution 29

*Strategy.* Bound $\lvert a_m - a_n\rvert$ by a geometric tail and apply the Cauchy criterion.

For $m > n \ge 1$, by the triangle inequality and the hypothesis,
$$
\lvert a_m - a_n\rvert \le \sum_{k=n}^{m-1}\lvert a_{k+1} - a_k\rvert \le \sum_{k=n}^{m-1}2^{-k} \le \frac{2^{-n}}{1 - 1/2} = 2^{1-n}.
$$
Given $\varepsilon > 0$, choose $N$ with $2^{1-N} < \varepsilon$ (Archimedean property). Then for all
$m > n \ge N$, $\lvert a_m - a_n\rvert \le 2^{1-n} \le 2^{1-N} < \varepsilon$, so $(a_n)$ is Cauchy. By
Cauchy completeness (Theorem 7.27) it converges. $\blacksquare$

### Solution 30

*Strategy.* Boundedness supplies subsequential limits (Bolzano–Weierstrass) and non-convergence means
those limits cannot all agree.

Let $(a_n)$ be bounded and divergent. By Corollary 7.22, $\limsup a_n = s$ and $\liminf a_n = i$ are
finite, and there are subsequences $(a_{n_k})$ with $a_{n_k} \to s$ and $(a_{m_k})$ with $a_{m_k} \to i$.
If $s = i$, then by the criterion in Corollary 7.22 the sequence would converge to $s$, contradicting
divergence. Hence $s \ne i$, and the two subsequences have different limits. $\blacksquare$

### Solution 31

*Strategy.* Translate the definition $\limsup a_n = \inf_n s_n$ (with $s_n = \sup_{k\ge n}a_k$) into
eventual and frequent statements.

Let $s_n = \sup\{a_k : k \ge n\}$, so that $s_n \downarrow M$ and $s_n \ge M$ for every $n$.

(a) Suppose that for some $\varepsilon > 0$ only finitely many $n$ satisfy $a_n > M - \varepsilon$. Then
there is $N$ with $a_n \le M - \varepsilon$ for all $n \ge N$, hence $s_N \le M - \varepsilon$. Since
$(s_n)$ is nonincreasing, $M = \inf_n s_n \le s_N \le M - \varepsilon$, a contradiction. So infinitely
many $n$ satisfy $a_n > M - \varepsilon$.

(b) Let $\varepsilon > 0$. Since $M = \inf_n s_n$, there is $N$ with $s_N < M + \varepsilon$ (otherwise
all $s_n \ge M + \varepsilon$ and $M \ge M + \varepsilon$). For $n \ge N$,
$$
a_n \le s_N < M + \varepsilon ,
$$
as required. $\blacksquare$

*Remark.* In the language of real analysis, (a) says the sequence exceeds $M - \varepsilon$
*infinitely often*, and (b) says it stays below $M + \varepsilon$ *eventually*.

### Solution 32

*Strategy.* Make $b_n$ grow along blocks on which the tail of $\sum a_n$ is geometrically small.

Since the tails of a convergent series tend to $0$, choose integers
$$
1 = N_0 < N_1 < N_2 < \cdots
$$
such that
$$
\sum_{n > N_k} a_n < 2^{-k} \qquad (k \ge 1);
$$
possible because $\sum_{n>N}a_n \to 0$ as $N \to \infty$ (the tail is the difference between the sum and
a partial sum). Define
$$
b_n = k \quad \text{for } N_{k-1} < n \le N_k, \ k \ge 1 .
$$
Then $b_n \to +\infty$ (it is nondecreasing and unbounded). Moreover
$$
\sum_{n=1}^{\infty}a_nb_n = \sum_{k=1}^{\infty} k\!\!\sum_{N_{k-1} < n \le N_k}\!\! a_n
\le \sum_{k=1}^{\infty} k \sum_{n > N_{k-1}} a_n < \sum_{k=1}^{\infty} k\,2^{-(k-1)} < \infty ,
$$
where the first inequality uses $a_n \ge 0$ and the second the choice of $N_k$. The last series converges
by the ratio test ($(k+1)2^{-k}/(k2^{-(k-1)}) = (k+1)/(2k) \to 1/2 < 1$). By the comparison test,
$\sum a_nb_n$ converges. $\blacksquare$

## Challenge

### Solution 33

*Strategy.* Summation by parts (Abel's lemma): rewrite $\sum a_kb_k$ in terms of the partial sums $A_k$
and the differences $b_k - b_{k+1}$, whose total variation is controlled by monotonicity.

Put $A_0 = 0$ and $A_k = a_1 + \cdots + a_k$, so $a_k = A_k - A_{k-1}$ and $\lvert A_k\rvert \le K$ for all
$k$. For $n > m \ge 0$,
$$
\sum_{k=m+1}^{n} a_kb_k = \sum_{k=m+1}^{n}(A_k - A_{k-1})b_k
= \sum_{k=m+1}^{n} A_kb_k - \sum_{k=m}^{n-1}A_kb_{k+1}
= A_nb_n - A_mb_{m+1} + \sum_{k=m+1}^{n-1}A_k(b_k - b_{k+1}).
$$
Take absolute values, using $\lvert A_k\rvert \le K$, $b_k \ge 0$ and $b_k - b_{k+1} \ge 0$:
$$
\left\lvert\sum_{k=m+1}^{n} a_kb_k\right\rvert
\le Kb_n + Kb_{m+1} + K\sum_{k=m+1}^{n-1}(b_k - b_{k+1})
= Kb_n + Kb_{m+1} + K(b_{m+1} - b_n)
= 2Kb_{m+1}.
$$
Since $b_{m+1} \to 0$, given $\varepsilon > 0$ there is $N$ with $2Kb_{N+1} < \varepsilon$; then for all
$n > m \ge N$,
$$
\left\lvert\sum_{k=m+1}^{n}a_kb_k\right\rvert \le 2Kb_{m+1} \le 2Kb_{N+1} < \varepsilon .
$$
By the Cauchy criterion for series (Theorem 7.33), $\sum a_nb_n$ converges. $\blacksquare$

*Check.* Taking $a_n = (-1)^{n+1}$ (partial sums in $\{0,1\}$, so $K = 1$) and $b_n = 1/n$ recovers the
alternating series test.

### Solution 34

*Strategy.* Because the positive and negative parts of the alternating harmonic series both diverge,
the partial sums can be pushed past any level in either direction; doing so with thresholds $L \pm \delta$
and letting $\delta \to 0$ gives convergence to $L$.

Write the positive terms as
$$
p_1 = 1,\ p_2 = \frac13,\ p_3 = \frac15,\ \dots, \qquad p_k = \frac{1}{2k-1},
$$
and the negative terms as $-q_j$ with $q_j = 1/(2j)$, $j \ge 1$. Both $\sum p_k$ and $\sum q_j$ diverge:
$$
\sum_{k=1}^{K} p_k \ge \sum_{k=1}^{K}\frac{1}{2k} = \frac12 H_K \to \infty, \qquad \sum_{j=1}^{J} q_j = \frac12 H_J \to \infty .
$$

*Construction.* Fix $L \in \mathbb{R}$. Define $\sigma$ in stages, using each term exactly once:
*Stage $2r-1$ (up):* append the next unused positive terms $p_{k}, p_{k+1}, \dots$ until the partial sum
first exceeds $L$; this terminates because $\sum p_k$ diverges.
*Stage $2r$ (down):* append the next unused negative terms $-q_{j}, -q_{j+1}, \dots$ until the partial sum
first drops below $L$; this terminates because $\sum q_j$ diverges.

*Convergence to $L$.* Let $\delta > 0$. Since $a_n \to 0$, only finitely many terms have magnitude
$\ge \delta$; let $S^{*}$ be the partial sum at the moment the last such term has been used. We claim
that every later partial sum lies in $(L - \delta, L + \delta)$. Indeed, at the start of each later stage
the partial sum is on one side of $L$ and inside the interval (by induction); during an "up" stage the
partial sums increase and the stage stops the first time they exceed $L$, so the overshoot is less than
the last term added, which has magnitude $< \delta$; hence all partial sums of that stage lie between
$L - \delta$ and $L + \delta$. The "down" stages are symmetric. Since $\delta > 0$ is arbitrary, the
rearranged partial sums converge to $L$. $\blacksquare$

*Remark.* The same construction with thresholds $L \pm \delta$ replaced by a single threshold produces
divergence to $+\infty$ (never take negative terms) or an oscillating divergence (take a bounded
number of terms in each direction). This is the concrete content of Theorem 7.47.

### Solution 35

*Strategy.* Assume convergence, so that the primes larger than some $N$ have total reciprocal $< 1/2$.
Then split the harmonic sum into integers all of whose prime factors are $\le N$ (bounded contribution)
and the rest (bounded by $(1/2)H_M$), and let $M \to \infty$.

Suppose, for contradiction, that $\sum_{p}1/p$ converges. Choose $N$ so large that
$$
\sum_{p > N}\frac1p < \frac12 ,
$$
and let $p_1 < p_2 < \cdots < p_k$ be the primes $\le N$. Let $A$ be the set of positive integers all of
whose prime factors lie in $\{p_1, \dots, p_k\}$.

*Step 1: $\sum_{n \in A}1/n$ is finite.* Since every $n \in A$ has a unique factorisation
$n = p_1^{e_1}\cdots p_k^{e_k}$ with $e_i \ge 0$, expanding the finite product of geometric series gives
$$
\sum_{n \in A}\frac1n = \prod_{i=1}^{k}\left(1 - \frac{1}{p_i}\right)^{-1} =: C < \infty .
$$
The expansion is legitimate because all terms are nonnegative (the partial products are increasing and
bounded by the product of the sums, and conversely every finite partial sum of the left side is dominated
by a partial product).

*Step 2: bound the harmonic sums.* Let $M \ge 1$ and $H_M = \sum_{n=1}^{M}1/n$. Every $n \le M$ either
lies in $A$, or has a prime factor $p > N$. Hence
$$
H_M \le \sum_{n\in A}\frac1n + \sum_{p>N}\ \sum_{\substack{n \le M\\ p \mid n}}\frac1n
\le C + \sum_{p>N}\frac1p\,H_M
\le C + \frac12 H_M ,
$$
where we used $\sum_{n\le M,\,p\mid n}1/n \le \frac1p\sum_{j \le M/p}1/j \le \frac1p H_M$ and then the
choice of $N$.

*Step 3: contradiction.* The inequality gives $H_M \le 2C$ for every $M$, so the harmonic sums are
bounded — contradicting Theorem 7.38. Therefore $\sum_p 1/p$ diverges. $\blacksquare$

### Solution 36

(a) *Strategy.* The grouped partial sums are a subsequence of the original partial sums.

With $c_k = a_{N_{k-1}+1} + \cdots + a_{N_k}$ we have, by additivity of finite sums,
$$
C_K := \sum_{k=1}^{K} c_k = \sum_{n=1}^{N_K} a_n = S_{N_K} .
$$
So $(C_K)$ is the subsequence $(S_{N_K})$ of $(S_N)$. If $\sum a_n$ converges, then $S_N \to S$, hence by
Theorem 7.18 every subsequence converges to $S$, so $C_K \to S$. Absolute convergence is not needed:
the argument only uses that a subsequence of a convergent sequence converges.

(b) *Example.* Take $a_n = (-1)^{n+1}$, whose partial sums are $1, 0, 1, 0, \dots$ and which diverges
(Solution 9). Group in pairs: $c_k = a_{2k-1} + a_{2k} = 1 - 1 = 0$. The grouped series is
$\sum 0 = 0$, which converges.

*Why the converse of (a) fails.* The grouped partial sums form only a subsequence of $(S_N)$; a
subsequence can converge while the whole sequence does not (here the subsequence of *even* partial sums
is constantly $0$ while the odd ones are constantly $1$). Grouping discards information about the
behaviour inside each block. $\blacksquare$

### Solution 37

*Strategy.* Compute both quantities from the explicit formula; the parity of $n$ controls the exponent.

Write
$$
a_n = 2^{-n-(-1)^n} = \begin{cases} 2^{-(n+1)}, & n \text{ even},\\ 2^{-(n-1)}, & n \text{ odd}.\end{cases}
$$

*Ratio.* For even $n$,
$$
\frac{a_{n+1}}{a_n} = \frac{2^{-n}}{2^{-(n+1)}} = 2 ,
$$
while for odd $n$,
$$
\frac{a_{n+1}}{a_n} = \frac{2^{-(n+2)}}{2^{-(n-1)}} = 2^{-3} = \frac18 .
$$
So the ratio takes the values $2$ and $1/8$ alternately and does not converge. The ratio test (in the form
"if the limit exists and is $<1$") therefore does not apply, and neither does the divergence form: the
ratio is not eventually $\ge 1$.

*Root.*
$$
a_n^{1/n} = 2^{-\frac{n + (-1)^n}{n}} = 2^{-1}\cdot 2^{-(-1)^n/n} .
$$
Now $2^{-1/n} \to 1$ and $2^{1/n} \to 1$ (the lemma of Solution 27 applied to $c = 2$), and
$2^{-(-1)^n/n}$ equals one of these two quantities according to the parity of $n$; hence
$$
0 \le \left\lvert 2^{-(-1)^n/n} - 1\right\rvert \le \max\left\{2^{1/n} - 1,\ 1 - 2^{-1/n}\right\} \longrightarrow 0
$$
by the squeeze theorem. So $2^{-(-1)^n/n} \to 1$ and $a_n^{1/n} \to \tfrac12$.

*Conclusion.* $\lim a_n^{1/n} = \tfrac12 < 1$, so by the root test (Theorem 7.41) the series $\sum a_n$
converges. The ratio test is inconclusive here even though the ratio test would have succeeded had the
ratios converged to $\tfrac12$; this example shows the root test is strictly stronger. $\blacksquare$

### Solution 38

*Strategy.* Convergence at $x_0$ makes the terms bounded; a bounded geometric factor $q^n$ then gives
absolute convergence for smaller $\lvert x\rvert$.

Suppose $\sum c_nx_0^n$ converges, with $x_0 \ne 0$. By the term test (Corollary 7.34),
$c_nx_0^n \to 0$; a convergent sequence is bounded (Theorem 7.5), so there is $M \ge 0$ with
$$
\lvert c_nx_0^n\rvert \le M \qquad \text{for all } n .
$$
Now let $\lvert x\rvert < \lvert x_0\rvert$ and put $q = \lvert x/x_0\rvert \in [0,1)$. Then
$$
\lvert c_nx^n\rvert = \lvert c_nx_0^n\rvert\cdot\left\lvert\frac{x}{x_0}\right\rvert^{n} \le M q^n .
$$
Since $\sum q^n$ converges (Example 7.32), the comparison test (Theorem 7.36) shows that
$\sum\lvert c_nx^n\rvert$ converges, i.e. $\sum c_nx^n$ converges absolutely. $\blacksquare$

*Remark.* This proves that the set of points of convergence of a power series is an interval centred at
$0$: absolute convergence holds strictly inside the radius determined by the point of convergence.
Theorem 7.50 identifies that radius exactly as $1/\limsup\lvert c_n\rvert^{1/n}$.

