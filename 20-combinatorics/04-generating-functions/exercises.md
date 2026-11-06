# Generating Functions — Exercises

> [Generating Functions](README.md) · 36 problems · Beginner → Challenge · Solutions: [solutions.md](solutions.md)

Attempt every problem in writing before looking at [solutions.md](solutions.md). Each problem names, in italics, the section of the tutorial that supplies the technique.

Notation: $[x^n]A(x)$ is the coefficient of $x^n$; $C_n$ are the Catalan numbers $\frac{1}{n+1}\binom{2n}{n}$; $F_n$ are the Fibonacci numbers with $F_0=0$, $F_1=1$; $p(n)$ is the number of integer partitions of $n$; $B_n$ is the Bell number (set partitions of $[n]$); $S(n,k)$ is a Stirling number of the second kind; $D_n$ is the number of derangements of $[n]$. All identities are identities of formal power series, so no convergence hypothesis is needed unless a problem explicitly asks for one.

Every answer must be checked against the first three or four terms computed directly.

## Beginner

**1.** *(§7.4)* Compute $[x^6]\dfrac{1}{1-2x}$, $[x^5]\dfrac{1}{1+3x}$ and $[x^0]\dfrac{1}{1-5x}$.

**2.** *(§7.5)* Compute $[x^4](1+x)^{10}$, $[x^4]\dfrac{1}{(1-x)^3}$ and $[x^2]\dfrac{1}{1+x}$.

**3.** *(§7.4)* Compute $[x^3]\dfrac{1}{(1-x)^2}$, and find a formula for $[x^n]\dfrac{x^3}{(1-x)^2}$ valid for $n \ge 3$.

**4.** *(§7.4)* Compute $[x^5]\dfrac{1}{1-x^2}$, $[x^6]\dfrac{1}{1-x^2}$ and $[x^7]\dfrac{x}{1-x^2}$.

**5.** *(§7.2)* Using the convolution rule, compute $[x^3]\dfrac{1}{(1-x)(1-2x)}$ and check the answer by multiplying out the first four terms of each factor.

**6.** *(§7.2)* Multiply the series $\sum_nx^n$ and $\sum_n(-1)^nx^n$ and describe the result. What are the coefficients of $x^0,x^1,x^2,x^3$?

**7.** *(§7.6)* Compute $F_{10}$ and $F_{12}$ from Binet's formula $F_n = (\varphi^n-\psi^n)/\sqrt5$, using $\varphi = 1.6180339887\ldots$ and $\psi = -0.6180339887\ldots$, and confirm with the recurrence.

**8.** *(§7.7)* Write down $C_0,\dots,C_6$. Verify $C_5 = 42$ from the recurrence $C_n = \sum_{k=0}^{n-1}C_kC_{n-1-k}$ and from the closed form.

**9.** *(§7.11)* Compute $B_0,\dots,B_5$ from $B_n = \sum_kS(n,k)$, and verify $B_4 = 15$ and $B_5 = 52$ against the EGF $\exp(e^x-1)$ evaluated at low order.

**10.** *(§7.9)* Write down $p(0),\dots,p(8)$. Use the pentagonal recurrence to compute $p(9)$ and $p(10)$.

**11.** *(§7.10)* Show that the exponential generating function of $a_n = n^2$ is $e^x(x+x^2)$, and check that the coefficient of $x^3$, multiplied by $3!$, equals $9$.

**12.** *(§7.6)* Solve $a_n = 3a_{n-1}$ with $a_0 = 2$ by the generating-function method, and state both the series and the closed form.

## Intermediate

**13.** *(§7.6)* Solve $a_n = 5a_{n-1} - 6a_{n-2}$ with $a_0 = 1$, $a_1 = 3$.

**14.** *(§7.4)* Derive the identities $\sum_{n\ge0}n\,x^n = \dfrac{x}{(1-x)^2}$ and $\sum_{n\ge0}n^2x^n = \dfrac{x(1+x)}{(1-x)^3}$ from the geometric series, and check both at $n = 3$.

**15.** *(§7.6)* Solve $a_n = 2a_{n-1} + 3$ with $a_0 = 1$.

**16.** *(§7.5)* Let $A(x) = \sum_{n\ge0}a_nx^n$ satisfy $A(0) = 1$ and the differential equation $(1-4x)A'(x) = 2A(x)$. Prove coefficient-wise that $a_{n+1} = \frac{2(2n+1)}{n+1}a_n$, deduce $a_n = \dbinom{2n}{n}$, and conclude $A(x) = (1-4x)^{-1/2}$. Compute $a_4$.

**17.** *(§7.12)* Use the snake-oil method to evaluate $\sum_k\dbinom nk2^k$.

**18.** *(§7.10)* Show that the EGF of cyclic arrangements is $-\ln(1-x)$, and check that the coefficient of $x^4$ times $4!$ equals the number of cyclic arrangements of four labels.

**19.** *(§7.7)* Compute $C_5$ from the recurrence and compare with $\frac16\binom{10}{5}$.

**20.** *(§7.2)* Find the generating function for compositions of $n$ into parts from $\{1,2,3\}$, and compute the number of such compositions of $6$ directly and from the series.

**21.** *(§7.9)* Write down the generating function for partitions into **distinct** parts. Compute the number of partitions of $8$ into distinct parts and the number of partitions of $8$ into odd parts, and comment.

**22.** *(§7.6)* Show that $[x^n]\dfrac{1}{1-x-x^2} = F_{n+1}$, and check at $n = 5$.

**23.** *(§7.11)* How many partitions of $[6]$ into exactly two blocks are there? Derive the general formula for exactly two blocks and check it at $n = 6$.

**24.** *(§7.10)* Compute $D_5$ by extracting $5![x^5]\dfrac{e^{-x}}{1-x}$, and compare with the value from the derangement formula.

## Advanced

**25.** *(§8.3)* Solve $a_n = 4a_{n-1} - 4a_{n-2}$ with $a_0 = 1$, $a_1 = 4$. (The characteristic equation has a double root; the generating function will show a squared denominator.)

**26.** *(§7.6)* The **Lucas numbers** are $L_0 = 2$, $L_1 = 1$ and $L_n = L_{n-1}+L_{n-2}$ for $n \ge 2$. Derive $L(x) = \dfrac{2-x}{1-x-x^2}$, decompose it by partial fractions, and deduce $L_n = \varphi^n+\psi^n$. Verify $L_{10} = 123$.

**27.** *(§7.2, §7.6)* Let $a_n$ be the number of ways to tile a $2\times n$ rectangle with $1\times2$ dominoes. Derive a recurrence from the leftmost column, find the generating function, and prove $a_n = F_{n+1}$. Check $a_{10} = 89$.

**28.** *(§7.12)* Use the snake-oil method to prove $\sum_k k(k-1)\dbinom nk = n(n-1)2^{n-2}$ for $n \ge 2$, and check at $n = 4$.

**29.** *(§7.2)* Prove that the number of compositions of $n$ into parts belonging to a set $S \subseteq \mathbb{N}$ is $[x^n]\dfrac{1}{1-\sum_{s\in S}x^s}$. Compute the number of compositions of $10$ into parts $2$ and $3$.

**30.** *(§7.11)* Derive the EGF $\exp(e^x-1)$ for the Bell numbers, and compute $B_6$ from it.

**31.** *(§7.10)* Derive $\hat D(x) = e^{-x}/(1-x)$ in two ways — from the inclusion–exclusion formula and from the combinatorial decomposition of a permutation into fixed points and a derangement — and extract $D_n$.

**32.** *(§7.4)* Prove by induction that $[x^n]\,(1-x)^{-k} = \binom{n+k-1}{k-1}$ for $k \ge 1$, and use it to count the weak compositions $e_1+\cdots+e_5 = 7$ in non-negative integers.

## Challenge

**33.** *(§7.9)* Prove Euler's theorem that the number of partitions of $n$ into distinct parts equals the number of partitions of $n$ into odd parts, using generating functions. Verify the equality at $n = 8$ by listing both families.

**34.** *(§7.7)* Use Lagrange inversion to derive $C_n = \frac1n\binom{2n-2}{n-1}$ from $C = 1+xC^2$, and check that this agrees with $\frac{1}{n+1}\binom{2n}{n}$.

**35.** *(§7.7, §7.13)* Prove that $C_n \sim \dfrac{4^n}{n^{3/2}\sqrt\pi}$, using Stirling's formula $n! \sim \sqrt{2\pi n}\,(n/e)^n$.

**36.** *(§7.10)* Prove that the EGF for permutations all of whose cycles have odd length is $\sqrt{\dfrac{1+x}{1-x}}$, and compute the numbers of such permutations of $[n]$ for $n = 0,1,\dots,6$.
