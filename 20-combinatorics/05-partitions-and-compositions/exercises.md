# Partitions and Compositions — Exercises

> [Partitions and Compositions](README.md) · 36 problems · Beginner → Challenge · Solutions: [solutions.md](solutions.md)

Attempt every problem in writing before looking at [solutions.md](solutions.md). Each problem names the section of the tutorial that supplies the technique.

Notation: $\mathbb{N} = \{1,2,\dots\}$, $\mathbb{N}_0 = \{0,1,2,\dots\}$; $p(n)$ is the number of partitions of $n$, $p(n,k)$ the number with exactly $k$ parts, $p_{\le k}(n)$ the number with at most $k$ parts, $q(n)$ the number into distinct parts, $c(n)$ the number of compositions of $n$; $\lambda'$ is the conjugate of $\lambda$; $g_k = k(3k-1)/2$ for $k \in \mathbb{Z}$ are the generalised pentagonal numbers. "Verify" means: compute by a second method and check that the two answers agree.

## Beginner

**1.** *(§7.1, §7.2)* List all compositions of $4$ and all partitions of $4$. Count each list and check the counts against $2^{4-1}$ and $p(4) = 5$.

**2.** *(§7.1)* How many compositions of $10$ have exactly $4$ parts? Give the formula and the number.

**3.** *(§7.1)* How many compositions of $7$ have exactly $2$ parts? List them and check your count.

**4.** *(§5.2)* Write $3+3+2+1+1+1$ in multiplicity notation, and compute its size and its length. Then do the same for $1^3 2^1 3^2$.

**5.** *(§7.2)* List all partitions of $8$ and verify $p(8) = 22$. How many of them have exactly three parts? Check the answer against $p(n,3) = p_{\le3}(n-3)$.

**6.** *(§7.4)* Compute the conjugate of $\lambda = (6,3,1)$, draw both diagrams, and verify that $\ell(\lambda) = \lambda'_1$ and $\lambda_1 = \ell(\lambda')$.

**7.** *(§7.4)* Is $(4,2,1)$ self-conjugate? Compute its conjugate, and decide which of the two partitions $(4,3,2,1)$ and $(4,2,1)$ are self-conjugate.

**8.** *(§7.8)* Prove that the number of partitions of $10$ with all parts even is $p(5) = 7$, by exhibiting a bijection, and list the seven partitions.

**9.** *(§7.8)* Using $p(10) = 42$ and $p(11) = 56$, compute the number of partitions of $11$ with no part equal to $1$, and list them.

**10.** *(§7.5)* For $n = 5$, list the partitions into odd parts and the partitions into distinct parts; check that both lists have the same size and state the Glaisher image of each odd-part partition.

**11.** *(§7.6)* Using the pentagonal recurrence and the values $p(0),\dots,p(11)$ from the table, compute $p(12)$.

**12.** *(§7.8)* Compute $p_{\le2}(13)$ from the formula $\lfloor n/2\rfloor + 1$ and list the partitions with at most two parts.

## Intermediate

**13.** *(§7.1)* Compute the number of compositions of $9$ whose parts are all odd, using the Fibonacci recurrence, and verify by listing.

**14.** *(§7.1)* Prove that the number of compositions of $n$ into parts all at least $2$ equals $F_{n-1}$, where $F_1 = F_2 = 1$.

**15.** *(§7.4, §7.6)* Prove that $p(n,k)$ equals the number of partitions of $n$ whose largest part is exactly $k$.

**16.** *(§7.8, §7.9)* Find the coefficient of $x^9$ in $\dfrac{1}{(1-x)(1-x^2)(1-x^3)}$ and verify the answer by listing the relevant partitions.

**17.** *(§7.5, §7.8)* Prove that the number of partitions of $n$ in which every part occurs at most twice equals the number of partitions of $n$ into parts not divisible by $3$.

**18.** *(§7.6)* Compute $p(18)$ from the pentagonal recurrence, showing every term and its sign.

**19.** *(§7.1)* Prove that a composition of $n$ into exactly $k$ odd parts exists only when $n \equiv k \pmod 2$, and that in that case the number of them is $\binom{(n-k)/2 + k - 1}{k-1}$. Evaluate this for $n = 11$, $k = 3$.

**20.** *(§7.8)* Expand $\prod_{i=1}^{3}(1+x^i)$ and explain what each coefficient counts. What is the coefficient of $x^5$?

**21.** *(§7.8)* Prove that the number of partitions of $n$ into exactly two parts is $\lfloor n/2\rfloor$, in two ways: directly, and with Ferrers diagrams via conjugation.

**22.** *(§7.1)* Compute the number of compositions of $12$ into parts all at least $2$.

**23.** *(§7.8)* Prove that the number of partitions of $n$ into parts all at least $3$ equals
$$p(n) - p(n-1) - p(n-2) + p(n-3),$$
and check the formula at $n = 10$ by listing the partitions of $10$ with all parts $\ge 3$.

## Advanced

**24.** *(§7.6)* Prove Corollary 7.12: if $\prod_{k\ge1}(1-x^k) = \sum_{k\in\mathbb{Z}}(-1)^k x^{g_k}$, then for $n \ge 1$
$$p(n) = \sum_{k\ge1}(-1)^{k-1}\big[p(n-g_k) + p(n-g_{-k})\big],$$
with $p(m) = 0$ for $m<0$. State precisely where each hypothesis is used.

**25.** *(§7.6)* Compute $p(25)$ with the pentagonal recurrence, listing the pentagonal numbers used, their signs, and each substitution.

**26.** *(§7.9)* Starting from the partial fraction decomposition
$$\frac{1}{(1-x)(1-x^2)(1-x^3)} = \frac{1}{6(1-x)^3} + \frac{1}{4(1-x)^2} + \frac{1}{4(1-x^2)} + \frac{1}{3(1-x^3)},$$
prove that $p_{\le 3}(n)$ is the nearest integer to $(n+3)^2/12$. (Organise the proof as a check of the six residue classes of $n$ modulo $6$.)

**27.** *(§7.10)* Prove that
$$\binom{n}{k}_q = q^{k(n-k)}\binom{n}{k}_{q^{-1}},$$
and deduce that the coefficients of $\binom{n}{k}_q$ form a palindromic sequence. Check the claim on $\binom{4}{2}_q = 1+q+2q^2+q^3+q^4$.

**28.** *(§7.6)* Let $J(n) = \left\lfloor \dfrac{\sqrt{24n+1}-1}{6}\right\rfloor$. Prove that the pentagonal recurrence for $p(n)$ has exactly $2J(n)$ or $2J(n)+1$ nonzero terms, and deduce that the number of terms is $O(\sqrt n)$. Compute $J(n)$ and the exact number of terms for $n = 25$ and for $n = 100$.

**29.** *(§7.1)* Let $a_n$ be the number of compositions of $n$ into parts from $\{1,2,3\}$. Prove $a_n = a_{n-1}+a_{n-2}+a_{n-3}$ with $a_0 = 1$, $a_1 = 1$, $a_2 = 2$, and compute $a_{10}$.

**30.** *(§7.5)* Prove Glaisher's generalisation of Euler's identity: for $d \ge 1$, the number of partitions of $n$ in which every part occurs at most $d$ times equals the number of partitions of $n$ into parts not divisible by $d+1$.

**31.** *(§7.8)* Prove the Euler-transform identity
$$\prod_{k\ge1}\frac{1}{1-x^k} = \exp\left(\sum_{m\ge1}\frac{\sigma(m)}{m}\,x^m\right),$$
where $\sigma(m)$ is the sum of the positive divisors of $m$, and deduce the recurrence
$$n\,p(n) = \sum_{m=1}^{n}\sigma(m)\,p(n-m).$$
Verify the recurrence at $n = 6$.

## Challenge

**32.** *(§7.4, §7.5)* Prove that the number of self-conjugate partitions of $n$ equals the number of partitions of $n$ into distinct odd parts, by constructing an explicit bijection. Illustrate it at $n = 10$, where both counts equal $2$.

**33.** *(§7.9)* Prove that for each fixed $k \ge 1$,
$$p_{\le k}(n) = \frac{n^{k-1}}{k!\,(k-1)!} + O(n^{k-2}) \qquad (n \to \infty),$$
and check the leading term against the exact value at $k = 3$, $n = 100$.

**34.** *(§7.10)* Prove the $q$-binomial theorem
$$\prod_{i=0}^{n-1}(1+xq^i) = \sum_{k=0}^{n} q^{k(k-1)/2}\binom{n}{k}_q x^k$$
by induction on $n$. You will need a $q$-Pascal recurrence; show that
$$\binom{n}{k}_q = \binom{n-1}{k}_q + q^{n-k}\binom{n-1}{k-1}_q$$
follows from the product formula, and use it. Check the case $n = 3$ by expanding both sides.

**35.** *(§7.8)* Determine, with proof, the generating function for partitions of $n$ into exactly $k$ distinct parts, and deduce the formula $p_{\le k}\big(n - k(k+1)/2\big)$ for their number. Evaluate for $n = 12$, $k = 3$.

**36.** *(§7.8, §7.7)* Prove that $\sum_{n\ge0} p(n)x^n$ is not a rational function, and deduce that $p(n)$ does not satisfy any linear recurrence with constant coefficients.
