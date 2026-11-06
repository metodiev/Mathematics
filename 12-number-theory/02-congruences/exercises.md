# Congruences — Exercises

> [Congruences](README.md) · 36 problems · Beginner → Challenge · Solutions: [solutions.md](solutions.md)

Attempt every problem in writing before looking at [solutions.md](solutions.md). Each problem names the section of the tutorial that supplies the technique.

Notation: $n \ge 2$ is the modulus unless stated otherwise; $a \equiv b \pmod n$ means $n \mid (a-b)$; $\varphi$ is Euler's totient; the *order* of $a$ modulo $n$ (written $\operatorname{ord}_n(a)$) is the least $d \ge 1$ with $a^d \equiv 1 \pmod n$, which exists exactly when $\gcd(a,n)=1$. Whenever you cancel a factor from a congruence, say which theorem licenses it.

## Beginner

**1.** *(§5.1)* Decide whether each congruence is true, and justify by exhibiting the quotient of the difference.

(a) $47 \equiv 5 \pmod 7$
(b) $-3 \equiv 4 \pmod 7$
(c) $100 \equiv 1 \pmod 9$
(d) $2^{10} \equiv 1 \pmod{11}$
(e) $3^{4} \equiv 1 \pmod{10}$

**2.** *(§5.2)* Give the canonical representative (in $\{0, 1, \dots, n-1\}$) of each integer modulo the stated modulus.

(a) $-1 \pmod 4$
(b) $7 \pmod 4$
(c) $-100 \pmod 4$
(d) $-1 \pmod{13}$
(e) $1000 \pmod 7$

**3.** *(§7.2)* Compute, showing every reduction.

(a) $7^{100} \bmod 5$
(b) $3^{50} \bmod 7$
(c) $2^{100} \bmod 13$
(d) $97 \cdot 98 \cdot 99 \bmod 100$ (use negative representatives)

**4.** *(§5.2, §7.2)* Find all solutions in the stated range.

(a) $x^2 \equiv 4 \pmod{12}$, with $0 \le x \le 11$.
(b) $x^2 \equiv 1 \pmod 8$, with $0 \le x \le 7$.
(c) $x^2 \equiv 2 \pmod 4$, with $0 \le x \le 3$.

**5.** *(§7.6)* Solve each linear congruence, or explain why there is no solution.

(a) $3x \equiv 5 \pmod 7$
(b) $5x \equiv 1 \pmod{12}$
(c) $9x \equiv 6 \pmod{12}$
(d) $6x \equiv 5 \pmod 9$

**6.** *(§7.5)* Find the inverse, in the range $\{0, \dots, n-1\}$.

(a) $3^{-1} \bmod 11$
(b) $7^{-1} \bmod 13$
(c) $8^{-1} \bmod 15$
(d) $5^{-1} \bmod 12$

**7.** *(§7.7)* Solve the system
$$x \equiv 1 \pmod 3, \qquad x \equiv 2 \pmod 5,$$
giving the answer as a single congruence modulo $15$, and check it in both congruences.

**8.** *(§7.9)* Compute $\varphi(n)$ for $n = 8, 12, 15, 36, 100$, using the product formula and verifying each answer by a second method.

**9.** *(§7.10)* Verify Wilson's theorem directly for $p = 5$, $p = 7$ and $p = 11$ by computing $(p-1)!$ and reducing it modulo $p$.

**10.** *(§7.11)* Compute $5^{13} \bmod 11$ by square-and-multiply, showing the table of squarings, and check the answer using Fermat's little theorem.

**11.** *(§7.12)* (a) Is $4{,}813{,}296$ divisible by $9$? By $3$? (b) Is $8{,}745{,}231$ divisible by $11$? (c) Explain which congruence underlies each test.

**12.** *(§7.2)* Prove that if $a \equiv b \pmod n$ then $a^2 + 3a \equiv b^2 + 3b \pmod n$. Then use this to compute $1001^2 + 3 \cdot 1001 \pmod 7$ without multiplying large numbers.

## Intermediate

**13.** *(§7.6)* Solve $21x \equiv 14 \pmod{35}$. State how many solutions there are, list them all, and verify two of them by direct substitution.

**14.** *(§7.6)* For the congruence $8x \equiv b \pmod{12}$, determine exactly which values of $b \in \{0, 1, \dots, 11\}$ make it solvable, and how many solutions there are in each case.

**15.** *(§7.7)* Solve the system
$$x \equiv 3 \pmod 5, \qquad x \equiv 4 \pmod 7, \qquad x \equiv 2 \pmod{11},$$
giving the answer modulo $385$. Show the step-by-step elimination and check all three congruences.

**16.** *(§7.7)* Solve $x \equiv 3 \pmod 8$, $x \equiv 7 \pmod{12}$, or show that no solution exists. State the modulus modulo which the answer is unique.

**17.** *(§7.9, §7.4)* Find the last digit of $7^{2024}$, and prove your answer using the cycle of powers modulo $10$.

**18.** *(§7.4, §7.9)* Prove that $a^{12} \equiv 1 \pmod{91}$ for every integer $a$ with $\gcd(a, 91) = 1$. (Note $\varphi(91) = 72$, so Euler's theorem alone does not give this; use the factorisation $91 = 7 \cdot 13$.)

**19.** *(§7.9)* Compute $\varphi(1000)$ in two ways: from the prime factorisation, and by counting the integers in $1, \dots, 1000$ that are coprime to $1000$.

**20.** *(§7.10)* Using Wilson's theorem for $p = 53$, compute $50! \bmod 53$. Justify the steps that pass from $(52)!$ to $(50)!$.

**21.** *(§7.11)* Compute $7^{222} \bmod 13$ by square-and-multiply, and verify the result by reducing the exponent modulo $12$.

**22.** *(§7.12)* (a) Check whether $0\text{-}306\text{-}40615\text{-}2$ is a valid ISBN-10. (b) Compute the check digit for the nine digits $0, 2, 0, 1, 5, 3, 0, 8, 2$. (c) Explain why the modulus $11$ detects every single-digit error, while modulus $10$ would not.

## Advanced

**23.** *(§7.1, §7.5)* Prove that if $a \equiv b \pmod n$ then $\gcd(a,n) = \gcd(b,n)$. Deduce that a residue class modulo $n$ consists either entirely of units or entirely of non-units.

**24.** *(§7.8)* Let $p$ be prime. Prove that $a^2 \equiv b^2 \pmod p$ if and only if $a \equiv b \pmod p$ or $a \equiv -b \pmod p$. Show by example that the statement fails modulo $8$.

**25.** *(§7.10, §7.8)* Prove that $x^2 \equiv -1 \pmod p$ has a solution if and only if $p = 2$ or $p \equiv 1 \pmod 4$. The direction $p \equiv 3 \pmod 4$ is Example 9 of the tutorial; for the converse use Wilson's theorem with $\left(\frac{p-1}{2}\right)!$.

**26.** *(§7.9)* Let $\gcd(a,n)=1$ and let $d = \operatorname{ord}_n(a)$. Prove that $d \mid \varphi(n)$. Deduce that $a^{100} \equiv 1 \pmod{101}$ for every $a \in \{1, \dots, 100\}$.

**27.** *(§7.8)* Let $p$ be prime. Prove that
$$\sum_{k=1}^{p-1} k^{p-1} \equiv -1 \pmod p .$$
Check the identity for $p = 5$.

**28.** *(§7.10, §7.7)* Prove that $x^2 \equiv 1 \pmod{2^k}$ has exactly four solutions for every $k \ge 3$, namely $x \equiv \pm 1$ and $x \equiv \pm(1 + 2^{k-1}) \pmod{2^k}$.

**29.** *(§7.12)* Prove the joint divisibility test for $7$, $11$ and $13$: if the decimal digits of $N$ are grouped into blocks of three from the right, then each of $7, 11, 13$ divides $N$ if and only if it divides the alternating sum of those blocks.

**30.** *(§7.8, §7.11)* Prove, using congruences and fast exponentiation, that $641 \mid 2^{32} + 1$. (You may use $641 = 5 \cdot 2^7 + 1 = 5^4 + 2^4$.)

**31.** *(§7.5)* Prove that the map $f : \mathbb{Z}/n\mathbb{Z} \to \mathbb{Z}/n\mathbb{Z}$, $f([x]) = [ax]$, is a bijection if and only if $\gcd(a,n) = 1$. What happens when $\gcd(a,n) = g > 1$ — how large is the image?

**32.** *(§7.2, §7.8)* Prove that $n^7 \equiv n \pmod{42}$ for every integer $n$.

## Challenge

**33.** *(§7.7)* Prove that for every $n \in \mathbb{N}$ there exist $n$ consecutive integers each of which is divisible by a perfect square greater than $1$. (Use the Chinese remainder theorem with moduli $p_i^2$ and a sufficiently large starting point.)

**34.** *(§7.8)* Let $p$ be an odd prime and let $a, b \in \mathbb{Z}$ with $\gcd(a,b) = 1$. Prove that if $p \mid (a^2 + b^2)$ then $p \equiv 1 \pmod 4$.

**35.** *(§7.10, §7.8)* Prove that there are infinitely many primes congruent to $1$ modulo $4$. (Suppose $p_1, \dots, p_n$ are all of them and consider $N = (2p_1p_2\cdots p_n)^2 + 1$; use Problem 34.)

**36.** *(§7.7, §7.10)* Let $n$ be odd, with exactly $\omega$ distinct prime factors. Prove that $x^2 \equiv 1 \pmod n$ has exactly $2^{\omega}$ solutions modulo $n$. Check the formula for $n = 15$ and $n = 45$.
