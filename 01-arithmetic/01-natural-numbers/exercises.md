# Natural Numbers — Exercises

> Part of [Natural Numbers](README.md) · 33 problems · Full solutions: [solutions.md](solutions.md)

Work on paper. For every computation, write the intermediate steps, not only the answer; several
solutions reward the method as much as the result.

---

## Beginner

**1.** Write $47{,}305$ in expanded form. State the value contributed by the digit $3$ and by the
digit $7$.

**2.** Insert $<$, $>$, or $=$ between each pair:

(a) $5{,}099$ and $5{,}100$;

(b) $12{,}345$ and $12{,}354$;

(c) $999$ and $1{,}000$;

(d) $7{,}070$ and $7{,}007$.

**3.** Compute $3{,}478 + 2{,}946$, showing the carry in each column. Check the result by rounding
both numbers to the nearest hundred.

**4.** Compute $5{,}002 - 1{,}847$, explaining every borrow. Verify your answer by adding.

**5.** Compute $34 \times 26$ using partial products, and again using the area of a rectangle.
Confirm that both methods agree.

**6.** Carry out $9{,}375 \div 25$. State the quotient and the remainder, and verify that
$a = qb + r$ with $0 \le r < b$.

**7.** (a) List all factors of $48$. (b) List the first six multiples of $7$. (c) Explain why every
nonzero natural number is a factor of $0$, and why $0$ therefore has infinitely many factors while
every positive number has only finitely many.

**8.** Decide whether each of the following is prime or composite, giving a divisor for each
composite: $51$, $57$, $61$, $67$, $87$, $91$.

**9.** Find the prime factorisation of $180$ and of $84$, and write each in canonical form.

**10.** Compute $\gcd(36, 60)$ and $\operatorname{lcm}(36, 60)$ from prime factorisations. Verify
that $\gcd(36,60) \cdot \operatorname{lcm}(36,60) = 36 \cdot 60$.

**11.** Convert $(1011)_2$ and $(11010)_2$ to base ten.

**12.** Convert $19$ and $42$ to binary.

---

## Intermediate

**13.** Run the sieve of Eratosthenes far enough to list every prime below $60$. State the largest
prime you need to use as a "crossing-out prime", and explain why no larger one is needed.

**14.** Use the Euclidean algorithm to compute $\gcd(252, 198)$. Show every division.

**15.** (a) Use the Euclidean algorithm to compute $\gcd(391, 357)$.

(b) Use it to compute $\gcd(2024, 168)$, then find $\operatorname{lcm}(2024, 168)$ using
$\gcd \cdot \operatorname{lcm} = ab$.

**16.** Apply the division algorithm to find $q$ and $r$:

(a) $a = 4{,}387$, $b = 17$;

(b) $a = 1{,}000$, $b = 7$.

In each case verify $0 \le r < b$ and $a = qb + r$.

**17.** Find every natural number $n$ with $0 \le n < 24$ such that $n$ leaves remainder $2$ on
division by $3$ and remainder $3$ on division by $4$. Show how you narrowed the search.

**18.** (a) State the digit-sum test for divisibility by $3$ and by $9$. (b) Apply it to $4{,}728$
and to $1{,}234{,}567$, and confirm the conclusions by direct division where the test is positive.

**19.** Work in binary, showing the carries:

(a) $1011_2 + 1101_2$;

(b) $1101_2 - 1011_2$;

(c) $1101_2 \times 101_2$.

Check each answer by converting to base ten.

**20.** Convert (a) $250$ to base $7$; (b) $100$ to base $3$. Verify each by expanding back to base
ten.

**21.** Find the prime factorisation of $1{,}001$, of $1{,}024$, and of $5{,}040$.

**22.** Using prime factorisations, compute $\gcd(1{,}800, 2{,}520)$ and
$\operatorname{lcm}(1{,}800, 2{,}520)$.

---

## Advanced

**23.** Let $a, b, c, x, y \in \mathbb{Z}$ with $a \ne 0$.

(a) Prove that if $a \mid b$ and $b \mid c$, then $a \mid c$.

(b) Prove that if $a \mid b$ and $a \mid c$, then $a \mid (bx + cy)$.

(c) Show by example that $a \mid bc$ does **not** imply $a \mid b$ or $a \mid c$.

**24.** Prove that the square of every integer is of the form $3k$ or $3k + 1$ for some integer $k$.
Deduce that no integer square is of the form $3k + 2$.

**25.** Use the extended Euclidean algorithm to write each gcd as a whole-number combination of the
two inputs:

(a) $\gcd(1071, 462)$;

(b) $\gcd(391, 357)$.

In each case verify your combination by direct arithmetic.

**26.** Prove: if $a \mid c$ and $b \mid c$ and $\gcd(a,b) = 1$, then $ab \mid c$. (You may use
Bézout's identity.)

**27.** (a) Prove that if $n = p_1^{e_1} \cdots p_k^{e_k}$ with distinct primes $p_i$, then the
number of positive divisors of $n$ is $(e_1+1)(e_2+1)\cdots(e_k+1)$.

(b) Use the formula to compute the number of divisors of $360$ and of $1{,}000$.

**28.** Prove the digit-sum rule: a natural number is divisible by $9$ exactly when the sum of its
decimal digits is divisible by $9$, and the same with $9$ replaced by $3$. Use the base-ten
expansion.

**29.** Prove that for every $n \ge 1$ there exist $n$ consecutive natural numbers, each of which is
composite. (Hint: look at $(n+1)! + 2, (n+1)! + 3, \dots$.)

---

## Challenge

**30.** Prove carefully that $\sqrt{2}$ is irrational. Your proof must explain why a fraction can be
assumed to be in lowest terms, and why the conclusion contradicts that assumption.

**31.** (a) Prove: if $n \ge 2$ is composite, then $n$ has a prime divisor $p$ with
$p \le \sqrt{n}$.

(b) Use part (a) to decide whether $127$, $149$, and $221$ are prime. List the primes you had to
test in each case and say why you could stop when you did.

**32.** Prove that $n^4 + 4$ is composite for every integer $n \ge 2$. (Hint: complete the square in
a clever way.) What happens for $n = 1$?

**33.** The Fermat numbers are $F_n = 2^{2^n} + 1$ for $n \ge 0$, so $F_0 = 3$, $F_1 = 5$,
$F_2 = 17$.

(a) Prove that $F_0 F_1 \cdots F_{n-1} = F_n - 2$ for every $n \ge 1$.

(b) Deduce that $F_m$ and $F_n$ are coprime whenever $m \ne n$.

(c) Deduce that there are infinitely many primes.
