# Divisibility and Primes — Exercises

> [Divisibility and Primes](README.md) · 36 problems · Beginner → Challenge · Solutions: [solutions.md](solutions.md)

Attempt every problem in writing before looking at [solutions.md](solutions.md). Each problem names the section of the tutorial that supplies the technique, so that a stuck reader knows where to reread.

Notation: $\mathbb{N} = \{1,2,3,\dots\}$ and $\mathbb{N}_0 = \{0,1,2,3,\dots\}$; $a \mid b$ means $b = ak$ for some $k \in \mathbb{Z}$; $p$ always denotes a prime; $\pi(x)$ is the number of primes $\le x$. For computational problems, show the algorithm — the divisions of the Euclidean algorithm, the factor tree, or the sieve — and not only the answer; for proof problems, state the definition or theorem used at each step. A numerical check is not a proof.

## Beginner

**1.** *(§7.2, §7.3)* Apply the division algorithm.

(a) Write $137 = 11q + r$ with $0 \le r < 11$.
(b) Write $-137 = 11q + r$ with $0 \le r < 11$.
(c) List all possible remainders when an integer is divided by $7$.
(d) Explain why there is no pair $(q,r)$ with $-137 = 11q + r$ and $0 \le r < 11$ other than the one you found in (b).

**2.** *(§7.4)* Decide whether each statement is true for all integers $a,b,c,d$. Prove the true ones from Definition 5.1.1 and give a counterexample for the false ones.

(a) If $a \mid b$ and $c \mid d$ then $ac \mid bd$.
(b) If $a \mid b$ then $a^2 \mid b^2$.
(c) If $a \mid (b+c)$ then $a \mid b$ and $a \mid c$.
(d) If $a \mid b$, $b \mid c$ and $c \mid a$ then $\lvert a \rvert = \lvert b \rvert = \lvert c\rvert$.

**3.** *(§7.6)* Use the Euclidean algorithm to compute each gcd, displaying every division and naming the last nonzero remainder.

(a) $\gcd(391, 299)$
(b) $\gcd(847, 385)$
(c) $\gcd(1309, 1001)$

**4.** *(§7.5)* Compute, or explain why the quantity is undefined.

(a) $\gcd(0, 25)$
(b) $\gcd(-48, 18)$
(c) $\gcd(a, 1)$ for $a \in \mathbb{Z}$
(d) $\gcd(0,0)$

**5.** *(§7.9)* Write each number in canonical form $p_1^{e_1}\cdots p_k^{e_k}$ with the primes increasing.

(a) $5040$
(b) $4158$
(c) $3024$

**6.** *(§7.9, §7.13)* Using the canonical forms from Problem 5, compute $\gcd(5040, 4158)$ and $\operatorname{lcm}(5040, 4158)$. Verify that your two answers satisfy $\gcd \cdot \operatorname{lcm} = 5040 \cdot 4158$.

**7.** *(§5.2, §7.11)* (a) Show that $1001$ is composite by exhibiting a factorisation into primes. (b) Show that $1009$ is prime. State which primes must be tested and why the list may stop where it does.

**8.** *(§7.6, §7.7)* Find integers $x, y$ with
$$29x + 17y = 1,$$
displaying the divisions of the Euclidean algorithm and the back-substitution. Check your answer by multiplication.

**9.** *(§7.4)* Prove that if $a \mid b$ and $c \mid d$ then $ac \mid bd$. Then explain, using this result, why $6 \mid 12$ and $10 \mid 30$ together imply $60 \mid 360$.

**10.** *(§7.5, §7.4)* Prove that $\gcd(n, n+1) = 1$ for every $n \in \mathbb{N}$. Then compute $\gcd(n, n+2)$ for even $n$ and for odd $n$, and prove both answers are correct.

**11.** *(§7.10)* For each list of primes below, form Euclid's number $N = p_1p_2\cdots p_n + 1$, factor $N$ completely, and identify a prime that is not in the list.

(a) $2, 3, 5$
(b) $2, 3, 5, 7$
(c) $2, 3, 5, 7, 11, 13$

**12.** *(§7.13)* Compute $\gcd(45, 60)$ and $\operatorname{lcm}(45, 60)$ by prime factorisation, and verify the identity $\gcd(a,b)\operatorname{lcm}(a,b) = \lvert ab\rvert$ for this pair. Then explain why $\operatorname{lcm}(45,60) \neq 45 \cdot 60$.

## Intermediate

**13.** *(§7.7)* (a) Find one solution of $47x + 31y = 1$ in integers. (b) Describe **all** integer solutions and prove that your description is complete.

**14.** *(§7.7)* Find the inverse of $17$ modulo $100$, that is, the unique $x \in \{0, 1, \dots, 99\}$ with $17x \equiv 1 \pmod{100}$. Use the extended Euclidean algorithm and check the result by multiplication.

**15.** *(§7.9)* Prove that if $a^2 \mid b^2$ for integers $a, b$, then $a \mid b$. Handle the cases in which $a$ or $b$ is zero.

**16.** *(§7.9)* Prove that $\sqrt p$ is irrational for every prime $p$.

**17.** *(§7.4, §7.8)* Prove that if $\gcd(a,b) = 1$ then $\gcd(a^n, b^m) = 1$ for all $m, n \in \mathbb{N}$.

**18.** *(§7.6)* Let $a, b \in \mathbb{N}$ and $g = \gcd(a,b)$. Prove that $\gcd(a+b,\, a-b)$ is equal to either $g$ or $2g$. Give one example of each case.

**19.** *(§7.11)* Sieve the integers up to $120$. List all primes below $120$ and count them. State exactly which primes you used as sieving primes and why no others were needed.

**20.** *(§7.11)* To sieve all primes below $1000$, up to which prime must you cross out multiples? How many sieving primes is that? Justify the bound using $23^2$, $29^2$, $31^2$ and $37^2$.

**21.** *(§7.13)* Show by example that
$$\gcd(a,b,c) \cdot \operatorname{lcm}(a,b,c) = abc$$
is **false** in general. Then state which inequality relating $\gcd(a,b,c)\operatorname{lcm}(a,b,c)$ and $\lvert abc\rvert$ does hold for positive $a,b,c$, and prove it.

**22.** *(§7.6)* Compute $\gcd(n^2 + n + 1,\ n - 1)$ for every integer $n \ge 2$, giving the answer as a function of $n$. (*Hint:* divide $n^2+n+1$ by $n-1$.)

## Advanced

**23.** *(§7.9)* Prove: if $2^n + 1$ is prime and $n \ge 1$, then $n$ is a power of $2$. Explain why the converse fails, using $n = 32$ (note that $n = 8$ gives $2^8+1 = 257$, which *is* prime).

**24.** *(§7.9)* Prove that $n^5 + n^4 + 1$ is composite for every integer $n \ge 2$, by exhibiting an explicit factorisation.

**25.** *(§7.4, §7.9)* Prove that $9 \mid 4^n + 15n - 1$ for every integer $n \ge 1$. Give an induction proof and a second proof using the binomial expansion of $(1+3)^n$.

**26.** *(§7.9)* Prove that the product of any $k$ consecutive integers is divisible by $k!$.

**27.** *(§7.9)* Prove that there are no three consecutive odd integers greater than $3$ that are all prime. (The triple $3, 5, 7$ shows that the bound $3$ cannot be improved.)

**28.** *(§7.4, §7.8)* Prove that $\gcd(n! + 1,\ (n+1)! + 1) = 1$ for every $n \in \mathbb{N}$.

**29.** *(§7.10)* Using the Fermat numbers $F_k = 2^{2^k} + 1$, prove that $\pi\left(2^{2^n} + 1\right) \ge n + 1$ for every $n \ge 0$.

**30.** *(§7.4)* Prove that if $\gcd(a,b) = 1$ then $\gcd(a + b,\ ab) = 1$.

**31.** *(§5.2, §7.11)* Prove that an integer $n \ge 2$ is prime if and only if no prime $p \le \sqrt n$ divides $n$. Explain carefully why it is enough to test *primes* rather than all integers up to $\sqrt n$.

**32.** *(§7.4, §7.8)* (a) Prove that for a prime $p$ and an integer $k$ with $1 \le k \le p-1$, the binomial coefficient $\binom{p}{k}$ is divisible by $p$. (b) Deduce that $(a+1)^p \equiv a^p + 1 \pmod p$ for every integer $a$. *(This is the key step in the second proof of Fermat's little theorem, given in [Congruences](../02-congruences/README.md).)*

## Challenge

**33.** *(§7.9)* Prove: if $a, n \ge 2$ and $a^n - 1$ is prime, then $a = 2$ and $n$ is prime. Show, by an example with $n = 1$, that the hypothesis $n \ge 2$ is necessary.

**34.** *(§7.6)* Lamé's theorem. Suppose $a > b \ge 1$ and the Euclidean algorithm applied to $(a,b)$ performs $k$ divisions, with remainders $r_0 = b > r_1 > \cdots > r_k = 0$ and $r_{k-1} = \gcd(a,b)$.

(a) Prove that $q_k \ge 2$ and that $q_i \ge 1$ for $1 \le i \le k-1$.
(b) Prove by downward induction that $r_{k-j} \ge F_{j+1}$ for $j = 1, \dots, k$, where $F_1 = F_2 = 1$; conclude $b \ge F_{k+1}$ and $a \ge F_{k+2}$.
(c) Using $F_{m} \ge \varphi^{m-2}$ for $m \ge 1$, where $\varphi = (1+\sqrt5)/2$, deduce that $k \le \log_\varphi(a) + 2$.
(d) Using $\log_{10}\varphi \approx 0.208988$, conclude that the number of divisions is at most about $4.8$ times the number of decimal digits of $a$. (This is the sharp form of Theorem 7.6.3.)

**35.** *(§7.10)* Let $p_n$ be the $n$-th prime. Prove that
$$p_n \le 2^{\,2^{\,n-1}}$$
for every $n \ge 1$, by induction using Euclid's construction. Check the bound for $n = 1, 2, 3, 4$ against the actual primes $2, 3, 5, 7$.

**36.** *(§7.9)* Let $\tau(m)$ denote the number of positive divisors of $m \ge 1$.

(a) Prove that $\tau(ab) \le \tau(a)\tau(b)$ for all $a, b \ge 1$.
(b) Determine exactly when equality holds.
(c) Use (b) to prove that $\tau$ is multiplicative on coprime arguments, and check the claim $\tau(6 \cdot 35) = \tau(6)\tau(35)$ numerically.
