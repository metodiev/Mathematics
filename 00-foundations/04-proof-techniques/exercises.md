# Proof Techniques — Exercises

> [Proof Techniques](README.md) · 34 problems · Beginner → Challenge · Solutions: [solutions.md](solutions.md)

Attempt every problem in writing before looking at [solutions.md](solutions.md). A proof that you have
only thought through is a proof you cannot yet check. Each problem names the section of the tutorial
that supplies the technique.

Notation: $\mathbb{N} = \{0,1,2,\dots\}$; "prime" means a positive integer $p > 1$ whose only positive
divisors are $1$ and $p$; $a \mid b$ means that $b = ak$ for some integer $k$; $a \equiv b \pmod n$
means $n \mid (a - b)$.

## Beginner

**1.** *(§7.1)* For each statement, rewrite it in the form "for all …, if … then …" and identify the
hypothesis and the conclusion.
(a) If $n$ is divisible by $6$, then $n$ is divisible by $3$.
(b) Every prime greater than $2$ is odd.
(c) The sum of two rational numbers is rational.

**2.** *(§7.4, §8.1)* For each statement, write down its converse, its contrapositive and its negation.
Say which of the three is logically equivalent to the original.
(a) If it rains, then the ground is wet.
(b) If a number is divisible by $9$, then it is divisible by $3$.

**3.** *(§7.3)* Prove directly that the sum of two odd integers is even.

**4.** *(§7.3)* Prove that for all integers $a, b, c$: if $a \mid b$ and $a \mid c$, then $a \mid (b+c)$
and $a \mid (b-c)$.

**5.** *(§7.3, §7.8)* Prove that the product of two consecutive integers is even.

**6.** *(§8.2)* Write the negation of each statement, without using the word "not" in front of a
quantifier. Then say whether the original statement is true, false, or depends on the unspecified
function $f$.
(a) $\forall x \in \mathbb{R},\ x^2 \ge 0$.
(b) $\exists n \in \mathbb{N},\ n^2 = 2$.
(c) $\forall \varepsilon > 0\ \exists \delta > 0\ \forall x\ \bigl(|x| < \delta \Rightarrow |f(x)| < \varepsilon\bigr)$.

**7.** *(§7.11)* For each statement, say whether it could be settled by a single example, by a single
counterexample, or by neither, and explain what would be required.
(a) There exists an even prime.
(b) All primes are odd.
(c) Every even integer greater than $2$ is a sum of two primes.
(d) For all real $x$, $x^2 > 0$.

**8.** *(§7.11)* Find a counterexample to each statement.
(a) If $n$ is prime, then $n$ is odd.
(b) If $x^2 > x$, then $x > 1$.
(c) Every positive integer is a sum of two squares of integers.

**9.** *(§7.6, §7.7)* Prove that there exist integers $x$ and $y$ with $13x + 7y = 1$. Is your proof
constructive?

**10.** *(§7.8)* Prove that for every integer $n$, $n^2$ has the same parity as $n$.

**11.** *(§7.13)* The following is a classical bogus proof. Identify every invalid step.
> **Claim:** $1 = 2$.
> **Proof:** Let $a = b$. Then $a^2 = ab$, so $a^2 - b^2 = ab - b^2$, hence
> $(a-b)(a+b) = b(a-b)$. Dividing by $a - b$ gives $a + b = b$. Since $a = b$, this is $2b = b$.
> Dividing by $b$ gives $2 = 1$. $\square$

## Intermediate

**12.** *(§7.5)* Prove that $\sqrt{3}$ is irrational.

**13.** *(§7.4)* Prove by contrapositive: for every integer $n$, if $5n + 3$ is odd, then $n$ is even.

**14.** *(§7.4)* Prove that for all real numbers $x$ and $y$: if $x + y > 2$, then $x > 1$ or $y > 1$.

**15.** *(§7.8)* Prove by cases that for every integer $n$, $n^2 \equiv 0$ or $1 \pmod 3$.

**16.** *(§7.6)* Prove that there is exactly one pair $(x,y)$ of integers satisfying
$$x + 2y = 5, \qquad 3x - y = 1.$$

**17.** *(§7.9)* Prove that for every integer $n$,
$$4 \mid n^2 \quad \Longleftrightarrow \quad n \text{ is even}.$$

**18.** *(§7.9)* Prove that for all sets $A$ and $B$,
$$A \cap B = A \cup B \quad \Longleftrightarrow \quad A = B.$$

**19.** *(§7.7)*
(a) Construct explicit irrational numbers $x, y$ with $x + y$ rational, proving that both are
irrational.
(b) Construct explicit irrational numbers $x, y$ with $xy$ rational, again proving irrationality.
(c) Theorem 7.12 proves the existence of irrational $x, y$ with $x^y$ rational without identifying
them. Explain why this proof is non-constructive and why it is nevertheless a complete proof.

**20.** *(§7.5)* Prove that for every positive integer $n$ there exists a prime $p$ with
$$n < p \le n! + 1.$$

**21.** *(§7.6)* Prove that the only positive integer that divides every integer is $1$.

## Advanced

**22.** *(§7.5)* Let $p$ be prime and $a$ an integer. Prove that if $p \mid a^2$, then $p \mid a$.
(You may use the fundamental theorem of arithmetic: every integer $> 1$ has a unique factorisation
into primes.)

**23.** *(§7.5)* Prove that $\sqrt{2} + \sqrt{3}$ is irrational. State clearly which earlier results
about irrationality you use.

**24.** *(§7.11)* Show that the statement "for every $n \in \mathbb{N}$, $n^2 + n + 41$ is prime" is
false, and show that it fails for infinitely many $n$.

**25.** *(§7.7)* Prove that for every integer $n \ge 2$ there exist $n$ consecutive positive integers,
none of which is prime.

**26.** *(§7.5, §7.3)*
(a) Prove that $x^2 - y^2 = 1$ has no solution in positive integers $x, y$.
(b) Prove that $x^2 - y^2 = 2$ has no solution in integers $x, y$ at all.

**27.** *(§7.5)*
(a) Prove that the sum of a rational number and an irrational number is irrational.
(b) Prove that the product of a nonzero rational number and an irrational number is irrational.

**28.** *(§7.6)* Prove that if $x > 0$ and $y > 0$ are real numbers with $x^2 = y^2$, then $x = y$.

**29.** *(§7.5)* Prove that $\log_2 3$ is irrational.

**30.** *(§7.3, §7.8)* Prove that for every real number $x > 0$,
$$x + \frac{1}{x} \ge 2.$$
For which $x$ does equality hold?

## Challenge

**31.** *(§7.5)* Prove that there are infinitely many primes congruent to $3$ modulo $4$.

**32.** *(§7.7)* Prove that every open interval $(a,b)$ with $a < b$ contains infinitely many
irrational numbers.

**33.** *(§7.5)* Prove that if $n \ge 1$ is an integer and $2^n - 1$ is prime, then $n$ is prime.

**34.** *(§7.12)* Consider the following argument.
> **Claim:** every odd integer has a square congruent to $1$ modulo $8$.
> **Proof:** Let $n$ be odd, $n = 2k + 1$. Then
> $$n^2 = 4k^2 + 4k + 1 = 4k(k+1) + 1.$$
> Since $k(k+1)$ is even, $k(k+1) = 2m$ for some integer $m$. Hence $n^2 = 8m + 1$. $\square$

(a) Is the argument correct? If it has a gap, fill it.
(b) Does the same method prove that every odd square is congruent to $1$ modulo $16$? Test $n = 3$,
and explain exactly what goes wrong.
