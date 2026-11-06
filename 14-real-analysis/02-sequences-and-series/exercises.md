# Sequences and Series of Real Numbers — Exercises

> [Tutorial](README.md) · 38 problems · Levels: Beginner, Intermediate, Advanced, Challenge

Every problem is a proof or a justified computation. For limits, either produce an explicit $N$ as a
function of $\varepsilon$, or name the theorem you use and verify its hypotheses. A numerical table is
never a proof. You may use any result from the [tutorial](README.md). Full solutions are in
[solutions.md](solutions.md).

## Beginner

**1.** Prove from the $\varepsilon$-$N$ definition that $\dfrac{4n+1}{n+2} \to 4$.

**2.** Prove from the $\varepsilon$-$N$ definition that $\dfrac{1}{n^2+1} \to 0$.

**3.** Prove from the $\varepsilon$-$N$ definition that $\dfrac{(-1)^n}{n} \to 0$.

**4.** Prove that the constant sequence $a_n = c$ converges to $c$.

**5.** Prove directly from the definition (without quoting "unbounded sequences diverge") that $a_n = n$ diverges.

**6.** Compute $\displaystyle\lim_{n\to\infty}\frac{3n^2+5n}{n^2-4}$, justifying each step by a theorem from the tutorial.

**7.** Compute $\displaystyle\lim_{n\to\infty}\frac{\sqrt n}{n+1}$.

**8.** Determine whether $a_n = \cos\dfrac{n\pi}{2}$ converges, and justify your answer.

**9.** Write the first four partial sums of $\sum_{n\ge1}(-1)^{n+1}$ and prove that the series diverges.

**10.** Compute $\displaystyle\sum_{n=0}^{\infty}\left(\frac23\right)^n$ and $\displaystyle\sum_{n=1}^{\infty}\left(\frac13\right)^n$.

**11.** Prove that $\displaystyle\sum_{n=1}^{\infty}\frac{1}{3n}$ diverges.

**12.** Determine whether $\displaystyle\sum_{n=1}^{\infty}\left(\frac{1}{2^n}+\frac{1}{3^n}\right)$ converges, and if so compute its sum.

**13.** Prove that no unbounded sequence converges.

## Intermediate

**14.** (Cesàro means) Let $a_n \to L$. Prove that
$$
\frac{a_1 + a_2 + \cdots + a_n}{n} \to L .
$$

**15.** Let $a_n \to 0$ and let $(b_n)$ be bounded. Prove that $a_nb_n \to 0$.

**16.** Let $a_1 = \sqrt 2$ and $a_{n+1} = \sqrt{2a_n}$. Prove that $(a_n)$ converges and find the limit.

**17.** Let $a_1 = 1$ and $a_{n+1} = \dfrac{a_n}{1 + a_n}$. Prove by induction that $a_n = 1/n$, and deduce the limit.

**18.** Compute $\limsup a_n$ and $\liminf a_n$ for $a_n = \dfrac{n\left(1+(-1)^n\right)}{2}$ (thus $a_n = 0$ for odd $n$ and $a_n = n$ for even $n$), working in the extended real line.

**19.** Compute $\limsup a_n$ and $\liminf a_n$ for $a_n = \sin\dfrac{n\pi}{2}$.

**20.** Prove that $\limsup(a_n+b_n) \le \limsup a_n + \limsup b_n$ for bounded sequences, and give an example in which the inequality is strict.

**21.** Let $\sum\lvert a_n\rvert$ converge and let $(b_n)$ be bounded. Prove that $\sum a_nb_n$ converges.

**22.** Determine whether $\displaystyle\sum_{n=1}^{\infty}\frac{n+1}{n^3+2}$ converges.

**23.** Determine whether $\displaystyle\sum_{n=1}^{\infty}\frac{2^n}{n^2}$ converges.

**24.** Determine whether $\displaystyle\sum_{n=1}^{\infty}\frac{(-1)^n}{2n+1}$ converges, and whether the convergence is absolute.

## Advanced

**25.** (a) Prove that if $\sum a_n$ converges absolutely, then $\sum a_n^2$ converges.
(b) Show that the converse fails.

**26.** Let $a_n > 0$ and suppose $\sum a_n$ converges. Prove that $\displaystyle\sum_{n=1}^{\infty}\frac{\sqrt{a_n}}{n}$ converges.

**27.** Suppose $a_n > 0$ and $\displaystyle\lim_{n\to\infty}\frac{a_{n+1}}{a_n} = L$. Prove that $\displaystyle\lim_{n\to\infty} a_n^{1/n} = L$.

**28.** (Cauchy's condensation test) Let $(a_n)$ be nonincreasing with $a_n \ge 0$. Prove that
$$
\sum_{n=1}^{\infty} a_n \ \text{converges} \iff \sum_{k=0}^{\infty} 2^k a_{2^k} \ \text{converges}.
$$

**29.** Let $(a_n)$ be a sequence with $\lvert a_{n+1} - a_n\rvert \le 2^{-n}$ for all $n$. Prove that $(a_n)$ converges.

**30.** Let $(a_n)$ be a bounded sequence that does not converge. Prove that there are two subsequences with different limits.

**31.** Let $(a_n)$ be bounded and let $M = \limsup a_n$. Prove:
(a) for every $\varepsilon > 0$ there are infinitely many $n$ with $a_n > M - \varepsilon$;
(b) for every $\varepsilon > 0$ there is $N$ with $a_n < M + \varepsilon$ for all $n \ge N$.

**32.** Let $a_n > 0$ with $\sum a_n$ convergent. Prove that there exists a sequence $(b_n)$ with $b_n \to +\infty$ such that $\sum a_nb_n$ still converges.

## Challenge

**33.** (Dirichlet's test) Let $(A_N)$ be the partial sums of $\sum a_n$, and suppose there is $K$ with $\lvert A_N\rvert \le K$ for all $N$. Let $(b_n)$ be nonincreasing with $b_n \to 0$. Prove that $\sum a_nb_n$ converges.

**34.** Let $\sum a_n$ be the alternating harmonic series. Given $L \in \mathbb{R}$, prove that there is a rearrangement of $\sum a_n$ converging to $L$.

**35.** Prove that $\displaystyle\sum_{p \text{ prime}} \frac1p$ diverges.

**36.** (Grouping) Given a series $\sum a_n$ and a strictly increasing sequence $0 = N_0 < N_1 < N_2 < \cdots$, the **grouped** series has terms $c_k = a_{N_{k-1}+1} + \cdots + a_{N_k}$.
(a) Prove that if $\sum a_n$ converges, then the grouped series converges to the same sum. (In particular absolute convergence is not needed — explain why.)
(b) Give an example of a *divergent* series and a grouping whose grouped series converges, and explain why the converse of (a) fails.

**37.** Let $a_n = 2^{-n-(-1)^n}$. Prove that $\displaystyle\lim_{n\to\infty}\frac{a_{n+1}}{a_n}$ does not exist, but that $\displaystyle\lim_{n\to\infty} a_n^{1/n} = \frac12$; deduce that the root test applies and the ratio test does not.

**38.** Let $\sum c_nx^n$ be a power series. Suppose it converges at some $x_0 \ne 0$. Prove that it converges absolutely for every $x$ with $\lvert x\rvert < \lvert x_0\rvert$.
