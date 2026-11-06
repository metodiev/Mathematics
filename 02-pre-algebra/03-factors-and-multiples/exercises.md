# Factors, Multiples, GCD and LCM — Exercises

> [Tutorial](README.md) · [Solutions](solutions.md)

For computational problems, show the method: a factor tree, a list of divisors, or the divisions of the Euclidean algorithm. For proof problems, state the definition or property you use at each step. Problems 22–28 are proofs; a numerical example is not a proof.

## Beginner

**1.** List all positive divisors of $36$.

**2.** List the first five positive multiples of $7$.

**3.** Is $4{,}572$ divisible by $3$? By $9$? By $6$? Justify each answer.

**4.** Is $7{,}215$ divisible by $5$? By $10$? By $3$? By $9$? Justify each answer.

**5.** Write the prime factorization of $84$.

**6.** Write the prime factorization of $180$.

**7.** Classify each of $51$, $91$ and $97$ as prime or composite, giving a factor for each composite.

**8.** Compute $\gcd(18,24)$.

**9.** Compute $\operatorname{lcm}(6,8)$.

**10.** Compute $\gcd(35,50)$ and $\operatorname{lcm}(35,50)$.

**11.** Are $14$ and $25$ coprime? Explain.

## Intermediate

**12.** Write the prime factorizations of $1{,}000$ and $1{,}001$.

**13.** Compute $\gcd$ and $\operatorname{lcm}$ of $2^3\cdot3^2\cdot5$ and $2^2\cdot3^5$.

**14.** Use the Euclidean algorithm to compute $\gcd(1{,}078,\,546)$. Show every division.

**15.** Use the Euclidean algorithm to compute $\gcd(8,13)$.

**16.** Compute $\operatorname{lcm}(12,18,30)$.

**17.** A rectangular floor measures $48$ cm by $60$ cm. What is the largest square tile that covers it exactly, and how many tiles are needed?

**18.** Two buses leave a terminal at 8:00. One route runs every $15$ minutes and the other every $20$ minutes. When do they next leave together?

**19.** Reduce $\dfrac{84}{126}$ to lowest terms, stating the gcd you used.

**20.** Compute $\dfrac{5}{12}+\dfrac{3}{8}$ using the least common denominator.

**21.** Test $4{,}917$ for divisibility by $3$, $9$ and $11$. Show the digit sums you use.

## Advanced

**22.** Prove the divisibility rule for $9$: an integer is divisible by $9$ exactly when the sum of its digits is.

**23.** Prove the divisibility rule for $4$: an integer is divisible by $4$ exactly when its last two digits form a multiple of $4$.

**24.** Prove that for integers $a,b$ and any integer $q$,
$$\gcd(a,b)=\gcd(b,\,a-qb).$$
Deduce that the Euclidean algorithm preserves the gcd at every step.

**25.** Prove that for positive integers $a$ and $b$,
$$\gcd(a,b)\cdot\operatorname{lcm}(a,b)=ab.$$

**26.** Using Bézout's identity, prove Euclid's lemma: if $p$ is prime and $p\mid ab$, then $p\mid a$ or $p\mid b$.

**27.** Prove that $\sqrt2$ is irrational. (Use the fundamental theorem of arithmetic, or the fact that the square of an odd integer is odd.)

**28.** Compute the number of positive divisors of $360$ and of $1{,}071$, using the formula $\tau(n)=\prod(e_i+1)$, and explain why the formula counts every divisor exactly once.

## Challenge

**29.** Find all positive integers $n<100$ such that $\gcd(n,84)=6$. Explain why there are no others.

**30.** Prove that there are infinitely many primes.

**31.** Find the smallest positive integer that has exactly $10$ positive divisors. Prove that no smaller integer works.

**32.** Explain why, to decide whether $n>1$ is prime, it suffices to test divisors $d$ with $d^2\le n$. Relate your explanation to the loop condition `while d*d <= n` in a trial-division program.
