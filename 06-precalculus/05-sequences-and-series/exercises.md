# Sequences and Series — Exercises

> [Tutorial](README.md) · 34 problems · Levels: Beginner, Intermediate, Advanced, Challenge

Work each problem completely, and check every numerical answer by a second method — a small case, a
substitution, or a direct addition. Proofs must state the statement, the base case, the inductive
hypothesis (where relevant) and the conclusion. Do not open [solutions.md](solutions.md) until you have
attempted the problems.

## Beginner

**1.** Write the first five terms of the sequence $a_n = 3n-1$.

**2.** Find the 20th term of the arithmetic sequence $5,\ 9,\ 13,\ 17,\ \dots$.

**3.** Find the sum of the first 30 terms of $2+5+8+11+\cdots$.

**4.** For the geometric sequence $3,\ 6,\ 12,\ 24,\ \dots$ find the 8th term and the sum of the first
8 terms.

**5.** Evaluate $\displaystyle\sum_{k=1}^{10} k$.

**6.** Evaluate $\displaystyle\sum_{k=1}^{10}(3k+2)$.

**7.** Evaluate $\displaystyle\sum_{k=1}^{6}2^{k}$.

**8.** Evaluate $\displaystyle\sum_{k=1}^{20}k^{2}$.

**9.** Compute $\dbinom{7}{3}$ and $\dbinom{7}{4}$, and explain why the two answers agree.

**10.** Expand $(x+2)^3$ using the binomial theorem.

**11.** Find the term in $x^4$ in the expansion of $(1+2x)^6$.

**12.** Write the repeating decimal $0.\overline{5} = 0.5555\dots$ as a fraction in lowest terms.

## Intermediate

**13.** Rewrite $\displaystyle\sum_{k=3}^{n+2}(4k-1)$ with the index running from $1$, and evaluate it
in closed form. Check your formula at $n=10$ by direct addition.

**14.** Evaluate $\displaystyle\sum_{k=1}^{n}(2k-1)$ and show that the result is a perfect square.

**15.** Evaluate $\displaystyle\sum_{k=1}^{50}\left(k^2-k\right)$.

**16.** Evaluate $\displaystyle\sum_{k=1}^{n}\left(\frac{1}{k+1}-\frac{1}{k+2}\right)$ and find its
limit as $n\to\infty$.

**17.** Evaluate $\displaystyle\sum_{k=1}^{\infty}3\left(\frac14\right)^{k-1}$.

**18.** A geometric series has first term $8$ and sum to infinity $12$. Find its common ratio, and
explain why the condition $|r|<1$ is satisfied.

**19.** Find the sum of the first $15$ positive multiples of $7$.

**20.** Prove by induction that $\displaystyle\sum_{k=1}^{n}(2k-1) = n^2$ for every $n\ge1$.

**21.** Find the coefficient of $x^{5}$ in the expansion of $(2x-3)^{7}$.

**22.** Find the term independent of $x$ in the expansion of $\left(x^2+\dfrac{2}{x}\right)^{6}$.

## Advanced

**23.** Prove by induction that $\displaystyle\sum_{k=1}^{n}k(k+1) = \frac{n(n+1)(n+2)}{3}$ for every
$n\ge1$.

**24.** Prove that $\displaystyle\sum_{k=1}^{n}\frac{1}{(2k-1)(2k+1)} = \frac{n}{2n+1}$ for every
$n\ge1$, and state the sum of the infinite series.

**25.** Prove that $\displaystyle\sum_{k=0}^{n}\binom{n}{k} = 2^{n}$ in two ways: by the binomial
theorem, and by a counting argument. Then prove $\displaystyle\sum_{k=0}^{n}(-1)^k\binom{n}{k} = 0$ for
$n\ge1$.

**26.** Prove that $\displaystyle\sum_{k=1}^{\infty}\frac{1}{2^{k}+1}$ converges, and show that its sum
$S$ satisfies $\frac13 < S < 1$. (You may use the convergence of the geometric series.)

**27.** Find the smallest $n$ for which $\displaystyle\sum_{k=1}^{n}2(1.05)^{k-1} > 50$. Justify the
answer by computing both neighbouring partial sums.

**28.** Prove Pascal's rule $\dbinom{n}{k} = \dbinom{n-1}{k-1}+\dbinom{n-1}{k}$ from the factorial
formula, stating the range of $k$ for which it holds.

**29.** Prove by a counting argument that $\displaystyle\sum_{k=0}^{n}k\binom{n}{k} = n\,2^{n-1}$ for
$n\ge1$.

**30.** Prove that the harmonic series $\displaystyle\sum_{k=1}^{\infty}\frac1k$ diverges, using the
grouping $1+\frac12+\left(\frac13+\frac14\right)+\left(\frac15+\cdots+\frac18\right)+\cdots$.

## Challenge

**31.** Evaluate $\displaystyle\sum_{k=1}^{\infty}\frac{1}{k(k+1)(k+2)}$ by writing the summand as a
difference of two consecutive terms of a simpler sequence.

**32.** Evaluate $\displaystyle\sum_{k=1}^{n}\frac{1}{k(k+3)}$ in closed form, find its limit as
$n\to\infty$, and explain why exactly six terms survive the cancellation.

**33.** A loan of $\$150{,}000$ is repaid over $15$ years by equal monthly payments at a nominal annual
rate of $4.8\%$ compounded monthly. Starting from the balance recurrence $B_n = (1+i)B_{n-1}-M$,
derive the payment formula and compute the monthly payment, the total repaid and the total interest.

**34.** Prove Vandermonde's identity $\displaystyle\sum_{k=0}^{n}\binom{n}{k}^{2} = \binom{2n}{n}$ by a
counting argument. (Consider a set of $n$ women and $n$ men, and count the $n$-person committees.)
