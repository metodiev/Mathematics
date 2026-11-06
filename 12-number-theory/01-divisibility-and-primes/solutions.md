# Divisibility and Primes — Solutions

> [Divisibility and Primes](README.md) · Solutions to the 36 problems in [exercises.md](exercises.md)

Each solution states the strategy, then carries out every significant step. Computational answers are cross-checked by a second method; proof answers are complete, with the definition or theorem used at each stage named explicitly. Section references point into the [tutorial](README.md).

## Beginner

**1.** *Strategy: the quotient is the number of full multiples of $b$ not exceeding $a$; when $a < 0$ this is more negative than naive division suggests.*

(a) $11 \cdot 12 = 132$ and $137 - 132 = 5 < 11$, so
$$137 = 12 \cdot 11 + 5, \qquad 0 \le 5 < 11 .$$
*Check:* $132 + 5 = 137$ ✓.

(b) The multiples of $11$ near $-137$ are $-132$ and $-143$. Since $-143 \le -137$, the correct quotient is $-13$:
$$-137 = (-13)\cdot 11 + 6, \qquad 0 \le 6 < 11 .$$
*Check:* $-143 + 6 = -137$ ✓. Note that $-137 / 11 \approx -12.45$, and rounding toward zero would give $q = -12$, $r = -5$ — not allowed, because $r$ must be non-negative.

(c) By Theorem 7.2.1 the remainder satisfies $0 \le r < 7$, so $r \in \{0, 1, 2, 3, 4, 5, 6\}$.

(d) Uniqueness is the content of the second half of the proof of Theorem 7.2.1. Suppose $-137 = 11q + r = 11q' + r'$ with $0 \le r, r' < 11$. Then $11(q - q') = r' - r$, so $11 \mid (r' - r)$, while $-11 < r' - r < 11$. The only multiple of $11$ in that open interval is $0$ (property D5: a nonzero multiple of $11$ has absolute value at least $11$). Hence $r' = r$, and then $11(q - q') = 0$ with $11 \ne 0$ gives $q = q'$.

**2.** *Strategy: unpack each divisibility into a witness equation; when a statement is false, look for the smallest counterexample.*

(a) **True.** Suppose $b = ak$ and $d = cm$ with $k, m \in \mathbb{Z}$. Then
$$bd = (ak)(cm) = (ac)(km),$$
and $km \in \mathbb{Z}$, so $ac \mid bd$.

(b) **True.** If $b = ak$ then $b^2 = a^2k^2$ and $k^2 \in \mathbb{Z}$.

(c) **False.** $3 \mid (1 + 2) = 3$, but $3 \nmid 1$ and $3 \nmid 2$. The property D3 runs in the other direction: divisibility of both summands implies divisibility of the sum, not conversely.

(d) **True.** From $a \mid b$ and $b \mid a$, property D6 gives $a = \pm b$ — provided $a, b \ne 0$; and if $a = 0$ then $0 \mid b$ forces $b = 0$, whence $b \mid c$ forces $c = 0$, and all three absolute values are equal. Similarly $b \mid c$ and $c \mid b$ give $b = \pm c$ (or $b = c = 0$). Hence $\lvert a\rvert = \lvert b \rvert$ and $\lvert b \rvert = \lvert c \rvert$.

**3.** *Strategy: divide the larger by the smaller, then replace the pair by (divisor, remainder) until the remainder is zero. The last nonzero remainder is the gcd.*

(a) $391$ and $299$:
$$\begin{aligned}
391 &= 1 \cdot 299 + 92 \\
299 &= 3 \cdot 92 + 23 \\
92 &= 4 \cdot 23 + 0
\end{aligned}$$
Last nonzero remainder: $\gcd(391, 299) = 23$.
*Check by factoring:* $391 = 17 \cdot 23$ and $299 = 13 \cdot 23$ ✓.

(b) $847$ and $385$:
$$\begin{aligned}
847 &= 2 \cdot 385 + 77 \\
385 &= 5 \cdot 77 + 0
\end{aligned}$$
Last nonzero remainder: $\gcd(847, 385) = 77$.
*Check:* $847 = 7 \cdot 11^2$ and $385 = 5 \cdot 7 \cdot 11$, common part $7 \cdot 11 = 77$ ✓.

(c) $1309$ and $1001$:
$$\begin{aligned}
1309 &= 1 \cdot 1001 + 308 \\
1001 &= 3 \cdot 308 + 77 \\
308 &= 4 \cdot 77 + 0
\end{aligned}$$
Last nonzero remainder: $\gcd(1309, 1001) = 77$.
*Check:* $1309 = 7 \cdot 11 \cdot 17$ and $1001 = 7 \cdot 11 \cdot 13$ ✓.

**4.**

(a) $\gcd(0, 25) = 25$ by Theorem 7.5.1(2): the common divisors of $0$ and $25$ are exactly the divisors of $25$, whose maximum is $25$. *Note:* every integer divides $0$, so the condition is no restriction.

(b) $\gcd(-48, 18) = \gcd(48, 18)$ by Theorem 7.5.1(1). Euclid: $48 = 2\cdot 18 + 12$, $18 = 1 \cdot 12 + 6$, $12 = 2 \cdot 6 + 0$, so the gcd is $6$. *Check:* $48 = 2^4 \cdot 3$, $18 = 2 \cdot 3^2$, common part $2 \cdot 3 = 6$ ✓.

(c) $\gcd(a, 1) = 1$: the only positive divisor of $1$ is $1$, so $1$ is a common divisor and is the largest possible positive integer that divides $1$.

(d) $\gcd(0,0)$ is **undefined**. Every positive integer divides $0 = 0 \cdot d$, so the set of positive common divisors is all of $\mathbb{N}$, which has no maximum. This is exactly the hypothesis $(a,b) \ne (0,0)$ in Definition 5.3.1.

**5.**

(a) $5040 = 504 \cdot 10 = (2^3 \cdot 3^2 \cdot 7)(2 \cdot 5) = 2^4 \cdot 3^2 \cdot 5 \cdot 7$.
*Check:* $16 \cdot 9 = 144$, $144 \cdot 35 = 5040$ ✓. (Indeed $5040 = 7!$.)

(b) $4158 = 2 \cdot 2079 = 2 \cdot 3 \cdot 693 = 2 \cdot 3 \cdot 3 \cdot 231 = 2 \cdot 3^3 \cdot 77 = 2 \cdot 3^3 \cdot 7 \cdot 11$.
*Check:* $2 \cdot 27 = 54$, $54 \cdot 77 = 4158$ ✓.

(c) $3024 = 2 \cdot 1512 = 4 \cdot 756 = 8 \cdot 378 = 16 \cdot 189 = 2^4 \cdot 3^3 \cdot 7$.
*Check:* $16 \cdot 27 \cdot 7 = 432 \cdot 7 = 3024$ ✓.

**6.** *Strategy: Corollary 7.9.4 — the gcd takes the minimum exponent, the lcm the maximum, prime by prime.*

Write both numbers with all primes visible, including exponent $0$:
$$5040 = 2^4 \cdot 3^2 \cdot 5^1 \cdot 7^1 \cdot 11^0, \qquad 4158 = 2^1 \cdot 3^3 \cdot 5^0 \cdot 7^1 \cdot 11^1 .$$
Taking minima and maxima:
$$\gcd = 2^1 \cdot 3^2 \cdot 7^1 = 2 \cdot 9 \cdot 7 = 126, \qquad \operatorname{lcm} = 2^4 \cdot 3^3 \cdot 5^1 \cdot 7^1 \cdot 11^1 = 166320 .$$
*Check the lcm by multiplication:* $16 \cdot 27 = 432$; $\;432 \cdot 5 = 2160$; $\;2160 \cdot 7 = 15120$; $\;15120 \cdot 11 = 166320$ ✓.

*Verify the identity:*
$$\gcd \cdot \operatorname{lcm} = 126 \cdot 166320 = 20{,}956{,}320, \qquad 5040 \cdot 4158 = 20{,}956{,}320 \ \checkmark$$
The equality is forced: for each prime, $\min(e,f) + \max(e,f) = e + f$.

**7.**

(a) $1001 = 7 \cdot 143 = 7 \cdot 11 \cdot 13$. *Check:* $7 \cdot 11 = 77$, $77 \cdot 13 = 1001$ ✓.

(b) $\sqrt{1009} \approx 31.76$, so by Problem 31 it suffices to test the primes $2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31$. Compute the remainders:

| $p$ | $2$ | $3$ | $5$ | $7$ | $11$ | $13$ | $17$ | $19$ | $23$ | $29$ | $31$ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| $1009 \bmod p$ | $1$ | $1$ | $4$ | $1$ | $8$ | $8$ | $6$ | $2$ | $20$ | $23$ | $17$ |

None is $0$, so $1009$ is prime. (Quick checks: $1009$ is odd; $1+0+0+9 = 10$ is not a multiple of $3$; $7 \cdot 144 = 1008$; $11 \cdot 91 = 1001$; $13 \cdot 77 = 1001$; $17 \cdot 59 = 1003$; $19 \cdot 53 = 1007$; $23 \cdot 43 = 989$; $29 \cdot 34 = 986$; $31 \cdot 32 = 992$.)

The list stops at $31$ because if $1009 = ab$ with $1 < a \le b < 1009$ then $a \le \sqrt{1009} < 32$, and $a$ has a prime divisor $\le a < 32$. A prime divisor would therefore already have appeared in the table.

**8.** *Strategy: run the Euclidean algorithm, then substitute backwards, replacing each remainder by the expression that produced it.*

The divisions are
$$\begin{aligned}
29 &= 1 \cdot 17 + 12 \\
17 &= 1 \cdot 12 + 5 \\
12 &= 2 \cdot 5 + 2 \\
5 &= 2 \cdot 2 + 1 \\
2 &= 2 \cdot 1 + 0
\end{aligned}$$
so $\gcd(29,17) = 1$ and a Bézout pair exists by Theorem 7.5.2. Back-substituting from the second-to-last line:
$$\begin{aligned}
1 &= 5 - 2 \cdot 2 \\
  &= 5 - 2(12 - 2 \cdot 5) = 5 \cdot 5 - 2 \cdot 12 \\
  &= 5(17 - 12) - 2 \cdot 12 = 5 \cdot 17 - 7 \cdot 12 \\
  &= 5 \cdot 17 - 7(29 - 17) = 12 \cdot 17 - 7 \cdot 29
\end{aligned}$$
So $x = -7$ and $y = 12$. *Check:* $29 \cdot (-7) + 17 \cdot 12 = -203 + 204 = 1$ ✓.

**9.** *Strategy: multiply the two witness equations.*

Suppose $b = ak$ and $d = cm$ with $k, m \in \mathbb{Z}$. Then
$$bd = (ak)(cm) = (ac)(km),$$
and $km$ is an integer, so $ac \mid bd$ by Definition 5.1.1.

Applying this with $a = 6$, $b = 12$, $c = 10$, $d = 30$: from $6 \mid 12$ and $10 \mid 30$ we get $60 \mid 360$. Indeed $360 = 60 \cdot 6$ ✓.

*Warning:* the converse is false. $6 \mid 12 \cdot 10 = 120$, but $6 \nmid 10$; divisibility of a product does not pass to the factors without a primality or coprimality hypothesis.

**10.** *Strategy: exhibit the gcd as a linear combination equal to $1$ (Corollary 7.5.3), or show that any common divisor divides $1$.*

$\gcd(n, n+1) = 1$: indeed $(n+1) - n = 1$, so any common divisor $d$ of $n$ and $n+1$ divides $1$ by D3, hence $d = 1$. Equivalently, the Bézout identity is $(n+1)\cdot 1 + n \cdot (-1) = 1$.

$\gcd(n, n+2)$: subtract, $(n+2) - n = 2$, so any common divisor divides $2$; hence the gcd is $1$ or $2$. Both cases occur and are decided by parity:

* If $n$ is even, then $n$ and $n+2$ are both even, so $2$ is a common divisor, and since no common divisor exceeds $2$, $\gcd = 2$.
* If $n$ is odd, then $n$ and $n+2$ are odd, so $2$ is not a common divisor; the only remaining possibility is $1$, hence $\gcd = 1$.

*Check:* $n = 7$: $\gcd(7,9) = 1$ ✓; $n = 8$: $\gcd(8,10) = 2$ ✓.

**11.** *Strategy: Euclid's argument guarantees that every prime divisor of $N$ is new, but $N$ itself may be composite.*

(a) $N = 2 \cdot 3 \cdot 5 + 1 = 31$, which is prime. The new prime is $31$.

(b) $N = 2\cdot3\cdot5\cdot7 + 1 = 211$. Testing the primes up to $\sqrt{211} \approx 14.5$: $211$ is odd, digit sum $4$, not ending in $0$ or $5$; $211 = 7 \cdot 30 + 1$; $211 = 11 \cdot 19 + 2$; $211 = 13 \cdot 16 + 3$. So $211$ is prime, and the new prime is $211$.

(c) $N = 2\cdot3\cdot5\cdot7\cdot11\cdot13 + 1 = 30030 + 1 = 30031$. This is **not** prime:
$$30031 = 59 \cdot 509 .$$
*Check:* $59 \cdot 509 = 59 \cdot 500 + 59 \cdot 9 = 29500 + 531 = 30031$ ✓. Both $59$ and $509$ are outside the original list, so the argument still produces new primes — two of them, in fact.

**12.** *Strategy: factor, read off minima and maxima, then verify the identity.*

$45 = 3^2 \cdot 5$ and $60 = 2^2 \cdot 3 \cdot 5$. Hence
$$\gcd(45,60) = 3 \cdot 5 = 15, \qquad \operatorname{lcm}(45,60) = 2^2 \cdot 3^2 \cdot 5 = 180 .$$
*Check the identity:* $15 \cdot 180 = 2700 = 45 \cdot 60$ ✓.

The lcm is *not* the product because the factor $3 \cdot 5 = 15$ is common to both numbers and would be counted twice in $45 \cdot 60$. The product counts each prime with exponent $e + f$, while the lcm correctly uses $\max(e,f) = e + f - \min(e,f)$; the discrepancy is exactly the gcd. Concretely, $45 \cdot 60 = (15 \cdot 3)(15 \cdot 4) = 15^2 \cdot 12$, whereas the lcm is $15 \cdot 12$.

## Intermediate

**13.** *Strategy: extended Euclidean algorithm, then describe the full solution set by the standard divisibility argument.*

(a) The divisions:
$$\begin{aligned}
47 &= 1 \cdot 31 + 16 \\
31 &= 1 \cdot 16 + 15 \\
16 &= 1 \cdot 15 + 1 \\
15 &= 15 \cdot 1 + 0
\end{aligned}$$
so $\gcd(47, 31) = 1$. Back-substituting:
$$\begin{aligned}
1 &= 16 - 15 \\
  &= 16 - (31 - 16) = 2 \cdot 16 - 31 \\
  &= 2(47 - 31) - 31 = 2 \cdot 47 - 3 \cdot 31
\end{aligned}$$
Hence $x = 2$, $y = -3$. *Check:* $2 \cdot 47 - 3 \cdot 31 = 94 - 93 = 1$ ✓.

(b) **Claim: all integer solutions are** $x = 2 + 31t$, $y = -3 - 47t$ with $t \in \mathbb{Z}$.

*They are solutions.* Substituting,
$$47(2 + 31t) + 31(-3 - 47t) = (2 \cdot 47 - 3 \cdot 31) + (47 \cdot 31 - 31 \cdot 47)t = 1 + 0 = 1 .$$

*There are no others.* Suppose $47x + 31y = 1$. Subtracting the known solution,
$$47(x - 2) = -31(y + 3).$$
So $31 \mid 47(x-2)$; since $\gcd(31, 47) = 1$, property D8 gives $31 \mid (x - 2)$. Write $x - 2 = 31t$ with $t \in \mathbb{Z}$. Then $47 \cdot 31 t = -31(y+3)$, so $y + 3 = -47t$, that is $y = -3 - 47t$. $\blacksquare$

**14.** *Strategy: an inverse modulo $100$ is a Bézout coefficient for the pair $(17, 100)$.*

The divisions:
$$\begin{aligned}
100 &= 5 \cdot 17 + 15 \\
17 &= 1 \cdot 15 + 2 \\
15 &= 7 \cdot 2 + 1 \\
2 &= 2 \cdot 1 + 0
\end{aligned}$$
so $\gcd(17, 100) = 1$ and the inverse exists. Back-substituting:
$$\begin{aligned}
1 &= 15 - 7 \cdot 2 \\
  &= 15 - 7(17 - 15) = 8 \cdot 15 - 7 \cdot 17 \\
  &= 8(100 - 5 \cdot 17) - 7 \cdot 17 = 8 \cdot 100 - 47 \cdot 17
\end{aligned}$$
So $-47 \cdot 17 \equiv 1 \pmod{100}$, and the representative in $\{0, \dots, 99\}$ is $x = 100 - 47 = 53$. *Check:* $17 \cdot 53 = 901 = 9 \cdot 100 + 1$ ✓.

*Second check.* $17 \cdot 6 = 102 \equiv 2$, and $2 \cdot 27 = 54 \equiv -46$... rather: $17 \cdot 53 = 17(50 + 3) = 850 + 51 = 901$ ✓. The inverse is unique modulo $100$ because if $17x \equiv 17x' \equiv 1$ then $17(x - x') \equiv 0$, and $17$ is invertible, so $x \equiv x'$ (cancellation with a unit).

**15.** *Strategy: reduce to positive integers, then compare exponents in the canonical form.*

If $b = 0$ then $a^2 \mid 0$ is automatic and $a \mid 0$ is also automatic, so the claim holds. If $a = 0$ then $0 \mid b^2$ forces $b^2 = 0$, hence $b = 0$, and again both divisibilities hold. So assume $a, b \ne 0$; replacing both by their absolute values does not change either divisibility (property D1), so assume $a, b \ge 1$, and write them in canonical form.

Let $e_p$ denote the exponent of the prime $p$. Then $e_p(a^2) = 2e_p(a)$ and $e_p(b^2) = 2e_p(b)$. The hypothesis $a^2 \mid b^2$, read through Corollary 7.9.3, says
$$2e_p(a) \le 2e_p(b) \quad \text{for every prime } p,$$
which is equivalent to $e_p(a) \le e_p(b)$ for every $p$. By Corollary 7.9.3 again, $a \mid b$. $\blacksquare$

*Remark.* The same argument shows $a^n \mid b^n \Rightarrow a \mid b$ for every $n \ge 1$. It is *not* true that $a \mid b$ follows from $a^2 \mid b^3$: take $a = 4$, $b = 2$; then $16 \mid 8$ is false, so try $a = 8$, $b = 4$: $64 \mid 64$ ✓ but $8 \nmid 4$. So $a^2 \mid b^3$ does not imply $a \mid b$.

**16.** *Strategy: mimic the classical proof for $\sqrt 2$, using the fundamental theorem of arithmetic to compare exponents.*

Let $p$ be prime and suppose $\sqrt p = a/b$ with $a, b \in \mathbb{N}$ and $\gcd(a,b) = 1$. Then
$$a^2 = p\,b^2 .$$
Compare the exponent of $p$ on both sides. The left side has exponent $2e_p(a)$, an even number; the right side has exponent $2e_p(b) + 1$, an odd number. Since the canonical form is unique (Corollary 7.9.2), these exponents must be equal — and an even number cannot equal an odd number. Contradiction. $\blacksquare$

*Remark.* The hypothesis $\gcd(a,b)=1$ is not actually needed with this argument, because the parity obstruction already contradicts uniqueness. The classical proof of $\sqrt 2 \notin \mathbb{Q}$ uses coprimality instead; both are valid, and the parity argument shows the real content: a prime occurs to an odd power in $p b^2$, so it cannot be a square.

**17.** *Strategy: a common divisor of $a^n$ and $b^m$ would produce a prime dividing both $a$ and $b$.*

Suppose a prime $q$ divides both $a^n$ and $b^m$. By Corollary 7.8.4, $q \mid a$ and $q \mid b$, so $q$ is a common divisor of $a$ and $b$ and $q \ge 2$, contradicting $\gcd(a,b) = 1$. Hence $a^n$ and $b^m$ have no common prime divisor, so their only positive common divisor is $1$. $\blacksquare$

*Second approach, purely algebraic.* By Bézout, $ax + by = 1$ for some $x, y$. Raise to the power $n + m - 1$: every term of the binomial expansion contains $a^i b^j$ with $i + j = n+m-1$, so either $i \ge n$ or $j \ge m$. Hence every term is divisible by $a^n$ or by $b^m$. This is not quite enough; the clean algebraic route is to note $\gcd(a^n, b) = 1$ by the first approach and apply it twice. The prime-based proof above is the shortest.

**18.** *Strategy: any common divisor of $a+b$ and $a-b$ divides their sum $2a$ and their difference $2b$, hence divides $2g$; and $g$ itself divides both.*

Let $g = \gcd(a,b)$ and $d = \gcd(a+b,\, a-b)$.

*$g \mid d$.* Since $g \mid a$ and $g \mid b$, we have $g \mid (a+b)$ and $g \mid (a-b)$ by D3. So $g$ is a positive common divisor of $a+b$ and $a-b$, hence $g \le d$ and $g \mid d$ (Corollary 7.5.4).

*$d \mid 2g$.* Since $d \mid (a+b)$ and $d \mid (a-b)$, D3 gives
$$d \mid \bigl((a+b) + (a-b)\bigr) = 2a, \qquad d \mid \bigl((a+b) - (a-b)\bigr) = 2b .$$
Write $a = ga'$, $b = gb'$ with $\gcd(a',b') = 1$. Then $d \mid 2ga'$ and $d \mid 2gb'$. Put $h = d/g$, which is an integer by the first part. From $hg \mid 2ga'$ we get $h \mid 2a'$, and similarly $h \mid 2b'$. Now let $q$ be an odd prime dividing $h$: then $q \mid 2a'$ forces $q \mid a'$, and $q \mid 2b'$ forces $q \mid b'$, contradicting $\gcd(a',b')=1$. So $h$ has no odd prime divisor, i.e. $h = 2^s$ for some $s \ge 0$. If $s \ge 2$ then $2^{s-1} \mid a'$ and $2^{s-1} \mid b'$, again contradicting coprimality; hence $s \le 1$ and $h \in \{1, 2\}$.

Since $g \mid d$ and $d = gh$ with $h \in \{1,2\}$, we get $d = g$ or $d = 2g$. $\blacksquare$

*Examples.* $a = 6$, $b = 3$: $g = 3$, $\gcd(9, 3) = 3 = g$. $\;a = 6$, $b = 2$: $g = 2$, $\gcd(8, 4) = 4 = 2g$. Both cases occur, so the statement cannot be sharpened without further hypotheses. (Note that $a$ and $b$ must both be nonzero for $d$ to be defined via $\gcd$; take $a, b \in \mathbb{N}$ as stated.)

**19.** *Strategy: cross out multiples of $p$ starting at $p^2$, for each prime $p \le \sqrt{120} \approx 10.95$.*

The sieving primes are $2, 3, 5, 7$: those are exactly the primes not exceeding $\sqrt{120} \approx 10.95$. By Theorem 7.11.2 every composite $n \le 120$ has a prime factor $\le \sqrt{n} \le \sqrt{120}$, so these four passes remove all composites.

Removing even numbers, multiples of $3$ (from $9$), multiples of $5$ (from $25$) and multiples of $7$ (from $49$) leaves the $30$ primes below $120$:
$$2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113 .$$
*Check the count another way:* $\pi(100) = 25$ (verified in the table of Section 7.12) and the primes strictly between $100$ and $120$ are $101, 103, 107, 109, 113$ — five of them. Total $25 + 5 = 30$ ✓.

**20.** *Strategy: the answer is $\lfloor\sqrt{1000}\rfloor = 31$, and the four squares quoted locate that bound precisely.*

$$\sqrt{1000} \approx 31.62 .$$
Compare squares: $23^2 = 529$, $29^2 = 841$, $31^2 = 961$, all at most $1000$; while $37^2 = 1369 > 1000$. Hence the primes up to $31$ are the sieving primes:
$$2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31,$$
eleven of them.

The justification is Theorem 7.11.2: a composite $n \le 1000$ has a prime factor $\le \sqrt n \le \sqrt{1000} < 32$, so it is removed by one of these eleven passes. Conversely no prime above $31$ is needed, since any composite not caught by then would have all prime factors exceeding $31$ and hence exceed $31^2 = 961$... more precisely would exceed $31 \cdot 37 = 1147 > 1000$, so no such composite exists below $1000$. That is why $37$ is one too many.

**21.** *Strategy: test the smallest numbers first; then read the correct inequality off the canonical forms.*

*Counterexample.* Take $a = b = c = 2$. Then $\gcd(2,2,2) = 2$ and $\operatorname{lcm}(2,2,2) = 2$, so the left side is $4$ while $abc = 8$. The claimed identity fails.

*The correct statement.* For positive $a, b, c$,
$$\gcd(a,b,c) \cdot \operatorname{lcm}(a,b,c) \ \le\ abc .$$
*Proof.* Write $e_p$ for the exponent of the prime $p$ in the canonical form, and put $\alpha = e_p(a)$, $\beta = e_p(b)$, $\gamma = e_p(c)$. The exponent of $p$ in $\gcd(a,b,c)$ is $\min(\alpha,\beta,\gamma)$ and in the lcm is $\max(\alpha,\beta,\gamma)$. In $abc$ it is $\alpha + \beta + \gamma$. Since $\min \le \max \le \alpha + \beta + \gamma - \min$ trivially, we have
$$\min(\alpha,\beta,\gamma) + \max(\alpha,\beta,\gamma) \le \alpha + \beta + \gamma,$$
because both the min and the max are among the three values and they are distinct slots when the values are not all equal; if all are equal, the left side is $2\alpha \le 3\alpha$. Comparing exponent by exponent gives the inequality. $\blacksquare$

Equality holds exactly when, for every prime, at most two of $\alpha, \beta, \gamma$ are nonzero — for instance $a = 4$, $b = 3$, $c = 5$: $\gcd = 1$, $\operatorname{lcm} = 60 = abc$ ✓.

**22.** *Strategy: apply Lemma 7.6.1 — the gcd is unchanged when $n^2+n+1$ is replaced by its remainder on division by $n-1$.*

Perform the division:
$$n^2 + n + 1 = (n-1)(n+2) + 3,$$
since $(n-1)(n+2) = n^2 + n - 2$. The remainder is $3$, so
$$\gcd(n^2+n+1,\ n-1) = \gcd(n-1,\ 3) = \gcd(3,\, n-1).$$
Now $\gcd(3, n-1)$ is $3$ if $3 \mid (n-1)$ and $1$ otherwise, because the only positive divisors of $3$ are $1$ and $3$. Therefore
$$\gcd(n^2+n+1,\ n-1) = \begin{cases} 3, & n \equiv 1 \pmod 3,\\ 1, & \text{otherwise.}\end{cases}$$

*Checks.* $n = 2$: $\gcd(7, 1) = 1$ ✓ ($2 \not\equiv 1 \bmod 3$). $n = 4$: $\gcd(21, 3) = 3$ ✓ ($4 \equiv 1 \bmod 3$). $n = 7$: $\gcd(57, 6) = 3$ ✓. $n = 5$: $\gcd(31, 4) = 1$ ✓.

## Advanced

**23.** *Strategy: if $n$ has an odd factor $d > 1$, the expression factors as $x^d + 1$ with $x = 2^{n/d}$.*

Suppose $n = 2^k m$ with $m$ odd. We show that $m = 1$ is forced.

Assume $m > 1$. Put $x = 2^{2^k}$, so $2^n = x^m$ and
$$2^n + 1 = x^m + 1 = (x + 1)\bigl(x^{m-1} - x^{m-2} + \cdots - x + 1\bigr),$$
the factorisation valid because $m$ is odd (multiply out: the product telescopes to $x^m + 1$). Both factors are greater than $1$: $x + 1 \ge 3$, and the second factor is a sum of $m$ terms of alternating sign whose value is positive — explicitly, grouping as $(x^{m-1} - x^{m-2}) + (x^{m-3} - x^{m-4}) + \cdots + (x^2 - x) + 1$, each bracket is at least $1$ when $x \ge 1$. So $2^n+1$ is composite, contradiction. Hence $m = 1$ and $n = 2^k$ is a power of $2$. $\blacksquare$

*The converse fails.* $n = 8 = 2^3$ gives $2^8 + 1 = 257$, which is prime, so the implication survives this test — but $n = 32$ gives
$$2^{32} + 1 = 4294967297 = 641 \cdot 6700417,$$
composite. So "power of $2$" is necessary but not sufficient.

Here is the classical verification that $641 \mid 2^{32}+1$. Note that $641 = 5\cdot 2^7 + 1 = 5^4 + 2^4$. From $5 \cdot 2^7 \equiv -1$ we get $5^4 \cdot 2^{28} \equiv 1$; and from $5^4 + 2^4 = 641$ we get $5^4 \equiv -2^4$. Combining, $-2^4 \cdot 2^{28} \equiv 1$, that is $2^{32} \equiv -1 \pmod{641}$. Hence $641 \mid 2^{32}+1$, and the cofactor is $6700417$, itself prime.

**24.** *Strategy: look for a factorisation into a quadratic and a cubic; the exponents $5, 4, 0$ suggest pairing $n^2 + n + 1$ with a cubic.*

**Claim.**
$$n^5 + n^4 + 1 = (n^2 + n + 1)(n^3 - n + 1).$$

*Verification by expansion:*
$$\begin{aligned}
(n^2+n+1)(n^3-n+1) &= n^5 - n^3 + n^2 + n^4 - n^2 + n + n^3 - n + 1 \\
&= n^5 + n^4 + (-n^3 + n^3) + (n^2 - n^2) + (n - n) + 1 = n^5 + n^4 + 1 . \ \checkmark
\end{aligned}$$

For $n \ge 2$ both factors are integers greater than $1$: $\;n^2 + n + 1 \ge 4 + 2 + 1 = 7$ and $n^3 - n + 1 \ge 8 - 2 + 1 = 7$. Neither factor equals $n^5+n^4+1$ (each is far smaller), so the number is composite. $\blacksquare$

*Check at $n = 2$:* $32 + 16 + 1 = 49 = 7 \cdot 7$, and indeed $n^2+n+1 = 7$, $n^3-n+1 = 7$ ✓.

**25.** *Strategy 1: induction with the algebraic identity $4^{n+1} = 4 \cdot 4^n$.*

**Claim.** $9 \mid 4^n + 15n - 1$ for all $n \ge 1$.

*Base case* $n = 1$: $4 + 15 - 1 = 18 = 2 \cdot 9$ ✓.

*Inductive step.* Assume $9 \mid 4^n + 15n - 1$. Multiply by $4$: $9 \mid 4^{n+1} + 60n - 4$. Now
$$4^{n+1} + 15(n+1) - 1 = \bigl(4^{n+1} + 60n - 4\bigr) - 45n + 18 = \bigl(4^{n+1} + 60n - 4\bigr) - 9(5n - 2).$$
Both terms on the right are divisible by $9$ (the first by the inductive hypothesis scaled, the second visibly), so by D3 their difference is divisible by $9$. $\blacksquare$

*Checks:* $n = 2$: $16 + 30 - 1 = 45 = 5 \cdot 9$ ✓; $n = 3$: $64 + 45 - 1 = 108 = 12 \cdot 9$ ✓.

*Strategy 2: the binomial theorem.* Expand $(1+3)^n$:
$$4^n = \sum_{k=0}^{n} \binom{n}{k} 3^k = 1 + 3n + \sum_{k=2}^{n} \binom{n}{k}3^k .$$
For $k \ge 2$ the term $\binom{n}{k}3^k$ is divisible by $3^2 = 9$. Hence $4^n \equiv 1 + 3n \pmod 9$, and
$$4^n + 15n - 1 \equiv (1 + 3n) + 15n - 1 = 18n \equiv 0 \pmod 9 .$$
$\blacksquare$ (This route is shorter but uses the binomial theorem and congruence notation from [Congruences](../02-congruences/README.md).)

**26.** *Strategy: the product equals $k!$ times a binomial coefficient, and binomial coefficients are integers — but that last fact must itself be proved without assuming the divisibility. Pascal's identity gives a clean induction.*

**Claim.** For $n \ge k \ge 1$, $\;k! \mid n(n-1)\cdots(n-k+1)$.

*Proof.* It suffices to show that $\binom{n}{k} := \dfrac{n(n-1)\cdots(n-k+1)}{k!}$ is an integer for all $0 \le k \le n$, since then the product is $k!\binom{n}{k}$.

Proceed by induction on $n$. For $n = 0$ the only coefficient is $\binom{0}{0} = 1$. Assume all $\binom{n-1}{j}$ are integers for $j \le n-1$. For $1 \le k \le n-1$, Pascal's identity
$$\binom{n}{k} = \binom{n-1}{k} + \binom{n-1}{k-1}$$
expresses $\binom{n}{k}$ as a sum of two integers, hence is an integer; and $\binom{n}{0} = \binom{n}{n} = 1$. This completes the induction. $\blacksquare$

*Check:* five consecutive integers $7, 8, 9, 10, 11$ have product $55440$; and $55440 / 5! = 55440/120 = 462$, an integer ✓. Here $n = 11$, $k = 5$, and indeed $\binom{11}{5} = 462$.

**27.** *Strategy: among three consecutive odd integers, exactly one is divisible by $3$ — count residues modulo $3$.*

Let the three integers be $n$, $n+2$, $n+4$ with $n$ odd. Their residues on division by $3$ are the three values
$$n \bmod 3, \quad (n+2) \bmod 3, \quad (n+4) \bmod 3 = (n+1) \bmod 3,$$
which are $n$, $n+2$ and $n+1$ modulo $3$ — that is, all three residues $0, 1, 2$ in some order. So exactly one of the three is divisible by $3$. Call it $m$.

If all three were prime, then $m$ would be a prime divisible by $3$, so $m = 3$. Since the triple consists of odd numbers greater than $3$, we would have $m > 3$, contradiction. Hence not all three are prime. $\blacksquare$

*Sharpness:* $3, 5, 7$ are all prime, and $m = 3$ is the exceptional case the argument allows.

*Checks of nearby triples:* $5, 7, 9$ — $9 = 3^2$ ✗; $11, 13, 15$ — $15 = 3 \cdot 5$ ✗; $101, 103, 105$ — $105 = 3 \cdot 5 \cdot 7$ ✗ ✓.

**28.** *Strategy: if $d$ divides both numbers, then $d$ divides the combination $(n+1)(n!+1) - \bigl((n+1)!+1\bigr)$, which is small.*

Let $d = \gcd(n!+1,\ (n+1)!+1)$. Compute
$$(n+1)(n! + 1) - \bigl((n+1)! + 1\bigr) = (n+1)n! + (n+1) - (n+1)! - 1 = (n+1)! - (n+1)! + n = n .$$
So $d \mid n$ by D3.

On the other hand $d \mid (n!+1)$. Since $n \mid n!$, we have $n! \equiv 0$... in divisibility language: $n \mid n!$, so $n \mid (n! + 1) - n! = 1$ would follow if $n \mid (n!+1)$; but we do not know that. Instead argue directly: from $d \mid n$ we get $d \mid n!$ (as $d \le n$ and $d$ is one of the factors... careful: $d \mid n$ implies $d \mid n!$, since $n! = n \cdot (n-1)!$ and $d \mid n$). Combined with $d \mid (n!+1)$ this gives
$$d \mid (n! + 1) - n! = 1 .$$
Hence $d = 1$. $\blacksquare$

*Check:* $n = 3$: $\gcd(7, 25) = 1$ ✓. $n = 4$: $\gcd(25, 121) = 1$ ✓. $n = 5$: $\gcd(121, 721) = 1$ ✓ ($721 = 7 \cdot 103$, $121 = 11^2$).

**29.** *Strategy: the Fermat numbers are pairwise coprime (Theorem 7.10.2), so $n+1$ of them supply $n+1$ distinct primes; then bound those primes.*

The numbers $F_0, F_1, \dots, F_n$ are $n+1$ integers, each at least $3$. By Lemma 7.8.1 each has a prime divisor, and by Theorem 7.10.2(2) no prime divides two of them. Choosing one prime divisor $q_k$ of each $F_k$ therefore gives $n+1$ **distinct** primes.

Each $F_k$ is at most $F_n$ (the sequence is increasing), so each $q_k \le F_k \le F_n = 2^{2^n} + 1$. Hence all $n+1$ primes lie in the range up to $2^{2^n}+1$, which means
$$\pi\bigl(2^{2^n}+1\bigr) \ge n+1 . \ \blacksquare$$

*Checks:* $n = 0$: $\pi(3) = 2 \ge 1$ ✓. $n = 1$: $\pi(5) = 3 \ge 2$ ✓. $n = 2$: $\pi(17) = 7 \ge 3$ ✓. $n = 3$: $\pi(257) = 55 \ge 4$ ✓. The bound is very weak — it grows logarithmically, whereas $\pi$ grows like $x/\ln x$ — but it is proved, which the prime number theorem is not at this point.

**30.** *Strategy: if a prime divides both $a+b$ and $ab$, then it divides one of $a, b$ and hence both.*

Let $d = \gcd(a+b,\, ab)$. Suppose $d > 1$; then $d$ has a prime divisor $p$ (Lemma 7.8.1), and $p \mid (a+b)$ and $p \mid ab$. By Euclid's lemma (Theorem 7.8.2), $p \mid a$ or $p \mid b$.

* If $p \mid a$, then from $p \mid (a+b)$ we get $p \mid b$.
* If $p \mid b$, then from $p \mid (a+b)$ we get $p \mid a$.

Either way $p$ is a common divisor of $a$ and $b$ with $p \ge 2$, contradicting $\gcd(a,b) = 1$. So no such $p$ exists, and $d = 1$. $\blacksquare$

*Check:* $a = 5$, $b = 7$: $a+b = 12$, $ab = 35$, $\gcd = 1$ ✓. $a = 8$, $b = 9$: $17$ and $72$, $\gcd = 1$ ✓.

*Remark.* The coprimality hypothesis is essential: $a = 2$, $b = 4$ are not coprime, and $\gcd(6, 8) = 2 \ne 1$.

**31.** *Strategy: if $n$ is composite, its smallest divisor above $1$ is a prime and is at most $\sqrt n$.*

Let $n \ge 2$.

*($\Leftarrow$) Suppose no prime $p \le \sqrt n$ divides $n$, and suppose for contradiction that $n$ is composite.* Then $n = ab$ with $1 < a \le b < n$. From $a \le b$ we get $a^2 \le ab = n$, so $a \le \sqrt n$. By Lemma 7.8.1, $a$ has a prime divisor $p$; then $p \le a \le \sqrt n$ and $p \mid a \mid n$, contradicting the hypothesis. So $n$ is prime.

*($\Rightarrow$) Suppose $n$ is prime and let $p \le \sqrt n$ be a prime. If $p \mid n$ then $p = 1$ or $p = n$ (the only positive divisors of a prime); $p \ge 2 > 1$ rules out $p = 1$, and $p \le \sqrt n < n$ (valid since $n \ge 2$) rules out $p = n$. So no such $p$ divides $n$. $\blacksquare$

*Why testing primes suffices.* If a composite $d \le \sqrt n$ divides $n$, then any prime divisor $p$ of $d$ satisfies $p \le d \le \sqrt n$ and $p \mid n$ by D2. So the hypothesis "no prime $\le \sqrt n$ divides $n$" is automatically violated in that case; testing composites adds no information, only work. Conversely, testing only primes loses nothing.

*Example.* $n = 97$: $\sqrt{97} \approx 9.85$, so test $2, 3, 5, 7$. None divides $97$: $97$ is odd, $9+7 = 16$ is not a multiple of $3$, $97$ does not end in $0$ or $5$, and $97 = 7 \cdot 13 + 6$. Hence $97$ is prime ✓.

**32.** *Strategy: write $\binom pk = \frac{p!}{k!(p-k)!}$ as an identity between integers, then use Euclid's lemma.*

(a) From the definition,
$$k!\,(p-k)!\,\binom{p}{k} = p! = p \cdot (p-1)! .$$
Since $p \mid p!$, we have $p \mid k!(p-k)!\binom pk$.

Now $p \nmid k!$ and $p \nmid (p-k)!$: every factor of $k!$ is an integer between $1$ and $k \le p-1$, hence not divisible by $p$; and every factor of $(p-k)!$ is between $1$ and $p-k \le p-1$, likewise. A product of integers none of which is divisible by the prime $p$ is not divisible by $p$ — this follows from Euclid's lemma by induction (Corollary 7.8.3 applied to the contrapositive... more directly, if $p \mid x_1\cdots x_r$ then $p \mid x_j$ for some $j$ by Corollary 7.8.3). Hence $p \nmid k!(p-k)!$.

Applying Euclid's lemma to the product $k!(p-k)! \cdot \binom pk$ and the prime $p$, and knowing $p$ does not divide the first factor, we conclude $p \mid \binom pk$. $\blacksquare$

*Check:* $p = 7$: $\binom71 = 7$, $\binom72 = 21 = 3\cdot 7$, $\binom73 = 35 = 5 \cdot 7$ ✓. $p = 5$: $5, 10, 10, 5$ ✓.

(b) By the binomial theorem,
$$(a+1)^p = \sum_{k=0}^{p} \binom{p}{k} a^k = a^p + 1 + \sum_{k=1}^{p-1}\binom pk a^k .$$
By part (a), $p$ divides each $\binom pk$ with $1 \le k \le p-1$; hence $p$ divides the whole sum $\sum_{k=1}^{p-1}\binom pk a^k$, and therefore
$$(a+1)^p \equiv a^p + 1 \pmod p . \ \blacksquare$$

## Challenge

**33.** *Strategy: two factorisations, one for a composite base and one for a composite exponent.*

Suppose $a, n \ge 2$ and $a^n - 1$ is prime.

*Step 1: $a = 2$.* Factor
$$a^n - 1 = (a-1)\bigl(a^{n-1} + a^{n-2} + \cdots + a + 1\bigr).$$
The first factor satisfies $a - 1 \ge 1$; the second is a sum of $n \ge 2$ positive terms, so it is at least $a + 1 \ge 3 > 1$. If $a \ge 3$ then $a - 1 \ge 2 > 1$, so both factors exceed $1$ and $a^n-1$ is composite. Hence $a - 1 = 1$, that is $a = 2$.

*Step 2: $n$ is prime.* Suppose $n = bc$ with $1 < b, c < n$. Then $2^n - 1 = (2^b)^c - 1$, which factors as
$$(2^b - 1)\bigl(2^{b(c-1)} + 2^{b(c-2)} + \cdots + 2^b + 1\bigr).$$
The first factor is at least $2^2 - 1 = 3 > 1$ (as $b \ge 2$), and the second is a sum of $c \ge 2$ positive terms, so it exceeds $1$. Hence $2^n - 1$ is composite, contradicting primality. Therefore $n$ has no proper factorisation, i.e. $n$ is prime. $\blacksquare$

*Why $n \ge 2$ is needed.* With $n = 1$ the number is $a - 1$, which is prime for $a = 3, 4, 6, 8, \dots$ — for instance $a = 4$, $n = 1$ gives $4^1 - 1 = 3$, prime, with $a \ne 2$. So the conclusion "$a = 2$" genuinely uses $n \ge 2$.

*Check of the conclusion:* $a = 2$, $n = 5$ gives $31$, prime ✓; $n = 11$ gives $2047 = 23 \cdot 89$, composite even though $n$ is prime — so primality of $n$ is necessary, not sufficient.

**34.** *Strategy: the quotient at the last step is at least $2$ (otherwise the algorithm would have stopped earlier), and each earlier quotient is at least $1$; then run the inequality $r_{i-2} \ge r_{i-1} + r_i$ backwards.*

Throughout, the algorithm is $r_{i-2} = q_i r_{i-1} + r_i$ for $i = 1, \dots, k$, with
$$r_{-1} = a,\quad r_0 = b,\quad r_k = 0,\quad r_{k-1} = \gcd(a,b) \ge 1 .$$

(a) For $1 \le i \le k-1$ the division is exact in the sense that $r_{i-1} > r_i > 0$, so $q_i = \lfloor r_{i-1}/r_i \rfloor \ge 1$. At the last step $r_{k-2} > r_{k-1} > 0$ and $r_k = 0$, so $r_{k-2} = q_k r_{k-1}$ with $q_k \ge 2$ (if $q_k$ were $1$ then $r_{k-2} = r_{k-1}$, contradicting the strict decrease).

(b) **Claim: $r_{k-j} \ge F_{j+1}$ for $j = 1, \dots, k$.**

*Base $j = 1$:* $r_{k-1} \ge 1 = F_2$ ✓.

*Base $j = 2$:* $r_{k-2} = q_k r_{k-1} \ge 2 \cdot 1 = 2 = F_3$ ✓ (here $q_k \ge 2$ is used).

*Inductive step.* Let $j \ge 3$ and assume $r_{k-i} \ge F_{i+1}$ for all $i < j$. From the division at index $i = k-j+2$,
$$r_{k-j} = q_{k-j+2}\,r_{k-j+1} + r_{k-j+2} \ \ge\ r_{k-j+1} + r_{k-j+2} \ \ge\ F_{j} + F_{j-1} = F_{j+1},$$
where the first inequality uses $q \ge 1$ and the second the inductive hypothesis with $i = j-1$ and $i = j-2$. This completes the downward induction.

Taking $j = k$ gives $r_0 = b \ge F_{k+1}$, and taking $j = k$ with the outer step $a = r_{-1} = q_1 r_0 + r_1 \ge r_0 + r_1 \ge F_{k+1} + F_k = F_{k+2}$ gives $a \ge F_{k+2}$. $\blacksquare$

(c) The classical closed form gives $F_m \ge \varphi^{m-2}$ for $m \ge 1$: check $F_1 = 1 \ge \varphi^{-1} \approx 0.618$ ✓ and $F_2 = 1 \ge \varphi^0 = 1$ ✓, and then induction with $F_{m} = F_{m-1} + F_{m-2} \ge \varphi^{m-3} + \varphi^{m-4} = \varphi^{m-4}(\varphi + 1) = \varphi^{m-4}\varphi^2 = \varphi^{m-2}$, using $\varphi^2 = \varphi + 1$.

From $a \ge F_{k+2} \ge \varphi^{k}$ we get $k \le \log_\varphi a$, and adding a constant for small cases gives $k \le \log_\varphi(a) + 2$. $\blacksquare$

(d) Change of base: $\log_\varphi a = \log_{10} a / \log_{10}\varphi = \log_{10} a / 0.208988 \approx 4.785 \log_{10} a$. Since $\log_{10} a$ is essentially the number of decimal digits $d$ of $a$, this gives
$$k \le 4.785\, d + 2,$$
so the number of divisions is at most about $4.8$ times the number of decimal digits — Lamé's bound. $\blacksquare$

*Verification on the worst case.* For $a = F_{n+1}$, $b = F_n$ every quotient equals $1$ except the last, and the algorithm takes $n-1$ divisions. With $n = 20$: $a = F_{21} = 10946$, $b = F_{20} = 6765$, $d = 5$ digits, and the bound predicts $4.785 \cdot 5 + 2 \approx 25.9$, while the actual count is $19$ ✓.

**35.** *Strategy: Euclid's construction gives $p_n \le p_1\cdots p_{n-1} + 1$; then dominate the product by a tower of $2$s.*

*Step 1: the Euclid bound.* Let $P = p_1 p_2 \cdots p_{n-1} + 1$. Then $P \ge 3$, so $P$ has a prime divisor $q$ (Lemma 7.8.1). No $p_i$ with $i \le n-1$ divides $P$, since $p_i \mid p_1\cdots p_{n-1}$ and $p_i \mid P$ would give $p_i \mid 1$. So $q$ is a prime different from $p_1, \dots, p_{n-1}$, hence $q \ge p_n$ (the $n$-th prime is the smallest prime not among the first $n-1$). And $q \le P$. Therefore
$$p_n \le p_1 p_2 \cdots p_{n-1} + 1 .$$

*Step 2: induction on $n$ for the bound $p_n \le 2^{2^{n-1}}$.*

*Base $n = 1$:* $p_1 = 2 = 2^{2^0}$ ✓.

*Inductive step.* Assume $p_i \le 2^{2^{i-1}}$ for $i = 1, \dots, n-1$. Then
$$p_1 \cdots p_{n-1} \le 2^{\,1 + 2 + 4 + \cdots + 2^{n-2}} = 2^{\,2^{n-1} - 1},$$
because $1 + 2 + \cdots + 2^{n-2} = 2^{n-1} - 1$ (geometric sum). Hence
$$p_n \le 2^{\,2^{n-1}-1} + 1 \le 2^{\,2^{n-1}},$$
the last step because $1 + 2^{m-1} \le 2^m$ for $m \ge 1$. $\blacksquare$

*Checks.* $n = 1$: $2 \le 2^1 = 2$ ✓ (equality). $n = 2$: $3 \le 2^2 = 4$ ✓. $n = 3$: $5 \le 2^4 = 16$ ✓. $n = 4$: $7 \le 2^8 = 256$ ✓. The bound is enormously wasteful — $p_{10} = 29$ while $2^{2^9} \approx 10^{154}$ — but it proves infinitude constructively and shows the primes grow at most doubly exponentially.

**36.** *Strategy: $\tau$ is read off the canonical form, and the inequality is a term-by-term estimate on exponents.*

Write $a = \prod_p p^{\alpha_p}$ and $b = \prod_p p^{\beta_p}$, with only finitely many nonzero exponents; then $ab = \prod_p p^{\alpha_p + \beta_p}$ and, by Corollary 7.9.5,
$$\tau(a) = \prod_p (\alpha_p + 1), \qquad \tau(b) = \prod_p (\beta_p + 1), \qquad \tau(ab) = \prod_p (\alpha_p + \beta_p + 1).$$

(a) For each prime and each pair of non-negative integers,
$$(\alpha + 1)(\beta + 1) = \alpha\beta + \alpha + \beta + 1 \ \ge\ \alpha + \beta + 1 .$$
Multiplying these inequalities over all primes (finitely many nontrivial factors, and factors equal to $1$ elsewhere) gives
$$\tau(a)\tau(b) = \prod_p (\alpha_p+1)(\beta_p+1) \ \ge\ \prod_p(\alpha_p+\beta_p+1) = \tau(ab). \ \blacksquare$$

(b) Equality holds in the product exactly when equality holds in every factor. The difference is
$$(\alpha+1)(\beta+1) - (\alpha+\beta+1) = \alpha\beta,$$
so equality at the prime $p$ holds exactly when $\alpha_p \beta_p = 0$, i.e. exactly when $p$ does not divide both $a$ and $b$. Hence
$$\tau(ab) = \tau(a)\tau(b) \iff \text{no prime divides both } a \text{ and } b \iff \gcd(a,b) = 1 .$$

(c) Part (b) is precisely the statement that $\tau$ is multiplicative on coprime arguments: $\gcd(a,b)=1 \Rightarrow \tau(ab) = \tau(a)\tau(b)$.

*Numerical check.* $6 = 2 \cdot 3$ so $\tau(6) = 4$; $35 = 5 \cdot 7$ so $\tau(35) = 4$. Since $\gcd(6,35)=1$, the formula predicts $\tau(210) = 4 \cdot 4 = 16$. Directly, $210 = 2\cdot3\cdot5\cdot7$ has $2^4 = 16$ divisors — the numbers $1, 2, 3, 5, 6, 7, 10, 14, 15, 21, 30, 35, 42, 70, 105, 210$ ✓.

*Contrast.* $\gcd(4, 2) = 2 \ne 1$, and indeed $\tau(8) = 4 < \tau(4)\tau(2) = 3 \cdot 2 = 6$; the gap is exactly $\alpha\beta = 2 \cdot 1 = 2$ at the prime $2$, and $6 - 2 = 4$ ✓.
