# Congruences — Solutions

> [Congruences](README.md) · Solutions to the 36 problems in [exercises.md](exercises.md)

Every solution names the theorem used and displays the arithmetic. Numerical answers are checked by a second method. Section references point into the [tutorial](README.md).

## Beginner

**1.** *Strategy: unpack $a \equiv b \pmod n$ as $n \mid (a-b)$ and exhibit the quotient.*

(a) $47 - 5 = 42 = 6 \cdot 7$, so $47 \equiv 5 \pmod 7$ ✓.

(b) $-3 - 4 = -7 = (-1)\cdot 7$, so $-3 \equiv 4 \pmod 7$ ✓. (Equivalently $-3 + 7 = 4$: on a $7$-hour dial, $-3$ and $4$ coincide.)

(c) $100 - 1 = 99 = 11 \cdot 9$, so $100 \equiv 1 \pmod 9$ ✓.

(d) $2^{10} - 1 = 1024 - 1 = 1023 = 93 \cdot 11$, so $2^{10} \equiv 1 \pmod{11}$ ✓. (This is Fermat's little theorem with $p = 11$, $a = 2$.)

(e) $3^4 - 1 = 81 - 1 = 80 = 8 \cdot 10$, so $3^4 \equiv 1 \pmod{10}$ ✓.

**2.** *Strategy: the canonical representative is the remainder on division by $n$ (Proposition 5.2.2); for negative numbers, add multiples of $n$ until the value lies in range.*

(a) $-1 + 4 = 3$, so $-1 \equiv 3 \pmod 4$.

(b) $7 - 4 = 3$, so $7 \equiv 3 \pmod 4$. (Same class as (a), as it must be: $7 - (-1) = 8$ is divisible by $4$.)

(c) $-100 + 25 \cdot 4 = -100 + 100 = 0$, so $-100 \equiv 0 \pmod 4$.

(d) $-1 + 13 = 12$, so $-1 \equiv 12 \pmod{13}$.

(e) $7 \cdot 142 = 994$ and $1000 - 994 = 6$, so $1000 \equiv 6 \pmod 7$. (Check: $1001 = 7\cdot11\cdot13$, so $1000 \equiv -1 \equiv 6$ ✓.)

**3.** *Strategy: find a small power congruent to $1$, then reduce the exponent modulo its period.*

(a) $7 \equiv 2 \pmod 5$ and $2^4 = 16 \equiv 1 \pmod 5$. Since $100 = 4 \cdot 25$,
$$7^{100} \equiv 2^{100} = (2^4)^{25} \equiv 1^{25} = 1 \pmod 5 .$$
*Check:* $7^{100}$ ends in $01$, and any number ending in $01$ is $\equiv 1 \pmod 5$ ✓.

(b) $3^2 = 9 \equiv 2$, $3^3 \equiv 6 \equiv -1$, so $3^6 \equiv 1 \pmod 7$. With $50 = 6 \cdot 8 + 2$,
$$3^{50} = (3^6)^8 \cdot 3^2 \equiv 1 \cdot 9 \equiv 2 \pmod 7 .$$
*Check:* $50 \equiv 2 \pmod 6$ and $3^{50} \equiv 3^2 = 2$ ✓ (consistent with Fermat's little theorem, which permits reducing the exponent modulo $6$).

(c) $2^4 = 16 \equiv 3$, $2^8 \equiv 9$, $2^{12} \equiv 27 \equiv 1 \pmod{13}$ (consistent with $\varphi(13) = 12$). Since $100 = 12 \cdot 8 + 4$,
$$2^{100} \equiv 2^4 = 16 \equiv 3 \pmod{13} .$$

(d) Use $-3$, $-2$, $-1$ for $97$, $98$, $99$ modulo $100$:
$$97 \cdot 98 \cdot 99 \equiv (-3)(-2)(-1) = -6 \equiv 94 \pmod{100} .$$
*Check:* $97 \cdot 98 = 9506$; $9506 \cdot 99 = 941094$; and $941094 = 9410 \cdot 100 + 94$ ✓.

**4.** *Strategy: squares modulo a small number form a short list; compute the list and read off.*

(a) The squares modulo $12$ are
$$0^2 = 0,\ 1^2 = 1,\ 2^2 = 4,\ 3^2 = 9,\ 4^2 = 16 \equiv 4,\ 5^2 = 25 \equiv 1,\ 6^2 = 36 \equiv 0,$$
and then the pattern repeats ($(12 - k)^2 \equiv k^2$). So $x^2 \equiv 4 \pmod{12}$ has the solutions $x \in \{2, 4, 8, 10\}$.
*Note:* there are four solutions, not two — modulo a composite, a quadratic can have more roots than its degree.

(b) For odd $x$, $x^2 \equiv 1 \pmod 8$: indeed $1^2 = 1$, $3^2 = 9 \equiv 1$, $5^2 = 25 \equiv 1$, $7^2 = 49 \equiv 1$; for even $x$, $x^2 \equiv 0$ or $4$. So the solutions are $x \in \{1, 3, 5, 7\}$ — every odd residue.

(c) The squares modulo $4$ are $0$ and $1$ only, so $x^2 \equiv 2 \pmod 4$ has **no** solution.

**5.** *Strategy: Theorem 7.6.1 — compute $g = \gcd(a,n)$, test $g \mid b$, divide through, invert.*

(a) $3x \equiv 5 \pmod 7$: $g = 1$, unique solution. $3 \cdot 5 = 15 \equiv 1 \pmod 7$, so $3^{-1} \equiv 5$ and $x \equiv 5 \cdot 5 = 25 \equiv 4 \pmod 7$.
*Check:* $3 \cdot 4 = 12 \equiv 5 \pmod 7$ ✓.

(b) $5x \equiv 1 \pmod{12}$: $g = 1$. Since $5 \cdot 5 = 25 = 2 \cdot 12 + 1$, $5^{-1} \equiv 5$, so $x \equiv 5 \pmod{12}$.
*Check:* $5 \cdot 5 = 25 \equiv 1 \pmod{12}$ ✓.

(c) $9x \equiv 6 \pmod{12}$: $g = \gcd(9,12) = 3$ and $3 \mid 6$ ✓, so there are three solutions. Divide by $3$: $3x \equiv 2 \pmod 4$. Since $3^{-1} \equiv 3 \pmod 4$, $x \equiv 6 \equiv 2 \pmod 4$. Lifting: $x \in \{2, 6, 10\}$.
*Check all three:* $9 \cdot 2 = 18 = 12 + 6$ ✓; $9 \cdot 6 = 54 = 4 \cdot 12 + 6$ ✓; $9 \cdot 10 = 90 = 7 \cdot 12 + 6$ ✓.

(d) $6x \equiv 5 \pmod 9$: $g = \gcd(6,9) = 3$ and $3 \nmid 5$, so there is **no solution**. (Direct check: $6x \bmod 9$ takes only the values $0, 6, 3$.)

**6.** *Strategy: run the extended Euclidean algorithm, or spot a small multiple.*

(a) $3 \cdot 4 = 12 = 11 + 1$, so $3^{-1} \equiv 4 \pmod{11}$.

(b) $7 \cdot 2 = 14 = 13 + 1$, so $7^{-1} \equiv 2 \pmod{13}$.

(c) $8 \cdot 2 = 16 = 15 + 1$, so $8^{-1} \equiv 2 \pmod{15}$.

(d) $5 \cdot 5 = 25 = 2 \cdot 12 + 1$, so $5^{-1} \equiv 5 \pmod{12}$ — the inverse is the number itself.

*Check of the criterion:* in each case $\gcd(a,n) = 1$, as Proposition 7.5.1 requires. For contrast, $6$ has no inverse modulo $15$ because $\gcd(6,15) = 3$, and indeed $6x \bmod 15 \in \{0, 6, 12, 3, 9\}$ never equals $1$.

**7.** *Strategy: Theorem 7.7.1 with $m = 3$, $n = 5$, using $2 \cdot 3 + (-1)\cdot 5 = 1$.*

List the numbers congruent to $1$ modulo $3$ and reduce modulo $5$:
$$1 \mapsto 1, \qquad 4 \mapsto 4, \qquad 7 \mapsto 2 \ \checkmark$$
The period is $5$ since $\gcd(3,5)=1$, so the solution is
$$x \equiv 7 \pmod{15} .$$
*Check:* $7 = 2\cdot 3 + 1$ ✓ and $7 = 1 \cdot 5 + 2$ ✓.

*By the Bézout construction:* with $u = 2$, $v = -1$ satisfying $2\cdot3 + (-1)\cdot5 = 1$, Theorem 7.7.1 gives $x = a v n + b u m = 1\cdot(-1)\cdot 5 + 2\cdot 2\cdot 3 = -5 + 12 = 7$ ✓.

**8.** *Strategy: Theorem 7.9.4 — factor, apply $\varphi(p^k) = p^k - p^{k-1}$, multiply.*

| $n$ | factorisation | $\varphi(n)$ | independent check |
|---|---|---|---|
| $8 = 2^3$ | — | $2^3 - 2^2 = 4$ | coprime residues $\{1,3,5,7\}$ |
| $12 = 2^2\cdot3$ | $\varphi(4)\varphi(3) = 2\cdot2$ | $4$ | $\{1,5,7,11\}$ |
| $15 = 3\cdot5$ | $\varphi(3)\varphi(5) = 2\cdot4$ | $8$ | $\{1,2,4,7,8,11,13,14\}$ |
| $36 = 2^2\cdot3^2$ | $\varphi(4)\varphi(9) = 2\cdot6$ | $12$ | $36(1-\tfrac12)(1-\tfrac13) = 36\cdot\tfrac13 = 12$ |
| $100 = 2^2\cdot5^2$ | $\varphi(4)\varphi(25) = 2\cdot20$ | $40$ | $100\cdot\tfrac12\cdot\tfrac45 = 40$ |

All five agree with the product formula $\varphi(n) = n\prod_{p\mid n}(1 - 1/p)$.

**9.** *Strategy: compute the factorial and divide by $p$.*

*$p = 5$:* $4! = 24 = 5 \cdot 4 + 4$, so $4! \equiv 4 \equiv -1 \pmod 5$ ✓.

*$p = 7$:* $6! = 720 = 102 \cdot 7 + 6$, so $6! \equiv 6 \equiv -1 \pmod 7$ ✓.

*$p = 11$:* $10! = 3628800$; dividing, $3628800 = 329890 \cdot 11 + 10$, so $10! \equiv 10 \equiv -1 \pmod{11}$ ✓.

The pattern visible in the small cases is Theorem 7.10.1: the residues other than $1$ and $p-1$ cancel in inverse pairs.

**10.** *Strategy: Algorithm 7.11.1 with $b = 5$, $e = 13$, $m = 11$.*

Powers of $5$ modulo $11$: $\;5^1 = 5$, $\;5^2 = 25 \equiv 3$, $\;5^4 \equiv 3^2 = 9$, $\;5^8 \equiv 9^2 = 81 \equiv 4$.

| Step | $e$ | `result` | `base` |
|---|---|---|---|
| start | $13$ | $1$ | $5$ |
| odd | $13$ | $5$ | $25 \equiv 3$ |
| halve | $6$ | $5$ | $3$ |
| even | $6$ | $5$ | $9$ |
| halve | $3$ | $5$ | $9$ |
| odd | $3$ | $45 \equiv 1$ | $81 \equiv 4$ |
| halve | $1$ | $1$ | $4$ |
| odd | $1$ | $4$ | $16 \equiv 5$ |
| halve | $0$ | $4$ | — |

So $5^{13} \equiv 4 \pmod{11}$.

*Independent check by Fermat:* $5^{10} \equiv 1 \pmod{11}$ and $13 = 10 + 3$, so $5^{13} \equiv 5^3 = 125 = 11 \cdot 11 + 4 \equiv 4$ ✓.

**11.**

(a) The digit sum is $4 + 8 + 1 + 3 + 2 + 9 + 6 = 33$. Since $33 \equiv 6 \not\equiv 0 \pmod 9$, the number is **not** divisible by $9$. Since $33 \equiv 0 \pmod 3$, it **is** divisible by $3$. *Check by division:* $4813296 = 3 \cdot 1604432$, and $1604432$ has digit sum $20$, not divisible by $3$ ✓.

(b) The alternating sum of the digits, from the right, is
$$1 - 3 + 2 - 5 + 4 - 7 + 8 = 0 .$$
Since $0$ is divisible by $11$, the number **is** divisible by $11$. *Check:* $8745231 = 11 \cdot 795021$ ✓.

(c) Both rest on $10 \equiv -1 \pmod{11}$ and $10 \equiv 1 \pmod 9$. Writing $N = \sum_i d_i10^i$:
* modulo $9$ (and hence modulo $3$, since $3 \mid 9$): $N \equiv \sum_i d_i \cdot 1^i = \sum_i d_i$, the digit sum;
* modulo $11$: $N \equiv \sum_i d_i(-1)^i$, the alternating digit sum.

**12.** *Strategy: apply Theorem 7.2.1(5) with the polynomial $P(x) = x^2 + 3x$.*

By Theorem 7.2.1(4), $a \equiv b$ implies $a^2 \equiv b^2$; by 7.2.1(3), $3a \equiv 3b$; by 7.2.1(1), the sums are congruent:
$$a^2 + 3a \equiv b^2 + 3b \pmod n .$$
(This is exactly part (5) of the theorem with $P(x) = x^2+3x$, whose coefficients $1$ and $3$ are integers.)

Apply with $a = 1001$, $b = 0$, $n = 7$: since $1001 = 7 \cdot 143$, we have $1001 \equiv 0 \pmod 7$, hence
$$1001^2 + 3\cdot1001 \equiv 0^2 + 3\cdot 0 = 0 \pmod 7 .$$
So $7$ divides $1001^2 + 3\cdot 1001$. *Check:* $1001^2 = 1002001$ and $3 \cdot 1001 = 3003$; the sum is $1005004 = 7 \cdot 143572$ ✓.

## Intermediate

**13.** *Strategy: Theorem 7.6.1 — $g = \gcd(21,35) = 7$, and $7 \mid 14$, so seven solutions.*

Divide $a$, $b$ and $n$ by $g = 7$:
$$3x \equiv 2 \pmod 5 .$$
Since $3 \cdot 2 = 6 \equiv 1 \pmod 5$, $\;3^{-1} \equiv 2$, so $x \equiv 4 \pmod 5$.

Lift by steps of $n/g = 5$ modulo $35$:
$$x \in \{4,\ 9,\ 14,\ 19,\ 24,\ 29,\ 34\},$$
seven values as predicted.

*Checks:* $21 \cdot 4 = 84 = 2\cdot 35 + 14$ ✓; $21 \cdot 34 = 714 = 20 \cdot 35 + 14$ ✓. Also $21 \cdot 19 = 399 = 11\cdot35 + 14$ ✓.

**14.** *Strategy: the criterion $g \mid b$ with $g = \gcd(8,12) = 4$.*

Solvable exactly when $4 \mid b$, i.e. $b \in \{0, 4, 8\}$. In each solvable case there are exactly $g = 4$ solutions modulo $12$.

* $b = 0$: $8x \equiv 0 \pmod{12} \iff 12 \mid 8x \iff 3 \mid 2x \iff 3 \mid x$. Solutions $\{0, 3, 6, 9\}$ — four ✓.
* $b = 4$: divide by $4$: $2x \equiv 1 \pmod 3$, so $x \equiv 2 \pmod 3$. Solutions $\{2, 5, 8, 11\}$ — four ✓.
* $b = 8$: divide by $4$: $2x \equiv 2 \pmod 3$, so $x \equiv 1 \pmod 3$. Solutions $\{1, 4, 7, 10\}$ — four ✓.

For $b \in \{1,2,3,5,6,7,9,10,11\}$ there is no solution: $8x \bmod 12$ only ever equals $0, 4$ or $8$.

**15.** *Strategy: solve two congruences at a time, replacing the pair by a single congruence modulo the product.*

*Step 1 (moduli $5$ and $7$).* Solve $x \equiv 3 \pmod 5$, $x \equiv 4 \pmod 7$. Write $x = 3 + 5j$; then $3 + 5j \equiv 4 \pmod 7$, i.e. $5j \equiv 1 \pmod 7$. Since $5 \cdot 3 = 15 \equiv 1 \pmod 7$, $\;j \equiv 3$, so $x = 3 + 15 = 18$. Hence
$$x \equiv 18 \pmod{35} .$$
*Check:* $18 \bmod 5 = 3$ ✓, $18 \bmod 7 = 4$ ✓.

*Step 2 (moduli $35$ and $11$).* Solve $x \equiv 18 \pmod{35}$, $x \equiv 2 \pmod{11}$. Write $x = 18 + 35t$; then $18 + 35t \equiv 2 \pmod{11}$. Since $18 \equiv 7$ and $35 \equiv 2 \pmod{11}$,
$$7 + 2t \equiv 2 \pmod{11} \implies 2t \equiv -5 \equiv 6 \pmod{11} \implies t \equiv 3 \pmod{11},$$
using $2^{-1} \equiv 6 \pmod{11}$ (as $2 \cdot 6 = 12 \equiv 1$). Hence
$$x = 18 + 35 \cdot 3 = 123, \qquad x \equiv 123 \pmod{385} .$$

*Check all three:* $123 = 24\cdot5 + 3$ ✓; $123 = 17\cdot7 + 4$ ✓; $123 = 11\cdot11 + 2$ ✓.

**16.** *Strategy: Theorem 7.7.4 — compatibility modulo $\gcd(8,12) = 4$.*

$3 - 7 = -4$ is divisible by $4$ ✓, so the system is solvable and the solution is unique modulo $\operatorname{lcm}(8,12) = 24$.

From $x \equiv 3 \pmod 8$: $x \in \{3, 11, 19, 27, \dots\}$. Reducing modulo $12$: $3 \mapsto 3$, $11 \mapsto 11$, $19 \mapsto 7$ ✓. So
$$x \equiv 19 \pmod{24} .$$
*Check:* $19 = 2\cdot8 + 3$ ✓ and $19 = 12 + 7$ ✓.

**17.** *Strategy: the last digit is the residue modulo $10$; find the cycle of powers of $7$.*

$$7^1 = 7, \quad 7^2 = 49 \equiv 9, \quad 7^3 \equiv 9 \cdot 7 = 63 \equiv 3, \quad 7^4 \equiv 3 \cdot 7 = 21 \equiv 1 \pmod{10},$$
and then the cycle $7, 9, 3, 1$ repeats with period $4$ because $7^4 \equiv 1$ and the powers of a unit multiply.

Since $2024 = 4 \cdot 506$ (check: $4 \cdot 500 = 2000$, $4 \cdot 6 = 24$ ✓),
$$7^{2024} = (7^4)^{506} \equiv 1^{506} = 1 \pmod{10} .$$
So the last digit is $1$.

*Note:* Euler's theorem is not available in the form "reduce the exponent modulo $\varphi(10) = 4$" unless $\gcd(7,10)=1$, which holds ✓; and $7^4 = 2401$ indeed ends in $1$.

**18.** *Strategy: prove the congruence modulo $7$ and modulo $13$ separately, then combine by the Chinese remainder theorem (as in Corollary 7.13.4 of the previous topic, coprimality of the moduli permits multiplying them).*

*Modulo $7$:* $\gcd(a,7)=1$ (since $\gcd(a,91)=1$), so Fermat gives $a^6 \equiv 1 \pmod 7$. Then $a^{12} = (a^6)^2 \equiv 1 \pmod 7$.

*Modulo $13$:* $\gcd(a,13)=1$, so Fermat gives $a^{12} \equiv 1 \pmod{13}$ directly.

So $7 \mid (a^{12} - 1)$ and $13 \mid (a^{12} - 1)$; since $\gcd(7,13) = 1$, their product $91$ divides $a^{12}-1$. Hence $a^{12} \equiv 1 \pmod{91}$. $\blacksquare$

*Check:* $a = 2$: $2^{12} = 4096$; and $4096 - 1 = 4095 = 45 \cdot 91$ ✓. Euler's theorem gives only $a^{72} \equiv 1 \pmod{91}$, because $\varphi(91) = 6 \cdot 12 = 72$; the universal exponent can be smaller than $\varphi(n)$, and here it is $\operatorname{lcm}(6,12) = 12$.

**19.** *Strategy: $\varphi$ is multiplicative on coprime factors, and $\varphi(p^k) = p^k - p^{k-1}$.*

*By the formula:* $1000 = 2^3 \cdot 5^3$, so
$$\varphi(1000) = \varphi(8)\varphi(125) = (8 - 4)(125 - 25) = 4 \cdot 100 = 400 .$$
Equivalently $1000\bigl(1 - \tfrac12\bigr)\bigl(1 - \tfrac15\bigr) = 1000 \cdot \tfrac12 \cdot \tfrac45 = 400$.

*By counting:* among $1, \dots, 1000$ the integers **not** coprime to $1000$ are those divisible by $2$ or by $5$. There are $500$ multiples of $2$ and $200$ multiples of $5$; the multiples of both are the multiples of $10$, of which there are $100$. By inclusion–exclusion the bad count is
$$500 + 200 - 100 = 600,$$
so the good count is $1000 - 600 = 400$ ✓.

**20.** *Strategy: Wilson gives $52! \equiv -1 \pmod{53}$; strip the last two factors by division.*

$53$ is prime ($\sqrt{53} \approx 7.3$, and none of $2, 3, 5, 7$ divides $53$). By Wilson's theorem,
$$52! \equiv -1 \pmod{53} .$$
Now $52! = 50! \cdot 51 \cdot 52$, and modulo $53$ we have $51 \equiv -2$ and $52 \equiv -1$, so
$$50! \cdot (-2)(-1) = 2 \cdot 50! \equiv -1 \pmod{53} .$$
The factor $2$ is a unit modulo $53$ (as $53$ is prime and $2 \not\equiv 0$), with inverse $27$ because $2 \cdot 27 = 54 \equiv 1$. Hence
$$50! \equiv -1 \cdot 27 = -27 \equiv 26 \pmod{53} .$$
*Check:* $26 \cdot 2 = 52 \equiv -1 \pmod{53}$ ✓, so this is consistent with $2 \cdot 50! \equiv -1$.

**21.** *Strategy 1: square-and-multiply.* Powers of $7$ modulo $13$: $7^2 = 49 \equiv 10$; $7^4 \equiv 10^2 = 100 \equiv 9$; $7^8 \equiv 81 \equiv 3$; $7^{16} \equiv 9$; $7^{32} \equiv 81 \equiv 3$; $7^{64} \equiv 9$; $7^{128} \equiv 3$.

The binary expansion is $222 = 128 + 64 + 16 + 8 + 4 + 2$ (check: $128+64 = 192$, $+16 = 208$, $+8 = 216$, $+4 = 220$, $+2 = 222$ ✓). So
$$7^{222} \equiv 3 \cdot 9 \cdot 9 \cdot 3 \cdot 9 \cdot 10 \pmod{13} .$$
Multiply step by step, reducing each time:
$$3 \cdot 9 = 27 \equiv 1; \quad 1 \cdot 9 = 9; \quad 9 \cdot 3 = 27 \equiv 1; \quad 1 \cdot 9 = 9; \quad 9 \cdot 10 = 90 \equiv 90 - 78 = 12 .$$

*Strategy 2: reduce the exponent modulo $12 = \varphi(13)$.* $222 = 12 \cdot 18 + 6$, so $7^{222} \equiv 7^6 \pmod{13}$; and $7^6 = 7^4 \cdot 7^2 \equiv 9 \cdot 10 = 90 \equiv 12 \pmod{13}$ ✓.

So $7^{222} \equiv 12 \equiv -1 \pmod{13}$.

*Check:* $7^{222} \equiv 12$ means $7^{222} + 1$ is divisible by $13$. Since $7^6 \equiv -1$, indeed $7^{222} = (7^6)^{37} \equiv (-1)^{37} = -1$ ✓ (using $222 = 6 \cdot 37$).

**22.**

(a) The digits of $0\text{-}306\text{-}40615\text{-}2$ are $0,3,0,6,4,0,6,1,5,2$. The weighted sum is
$$1\cdot0 + 2\cdot3 + 3\cdot0 + 4\cdot6 + 5\cdot4 + 6\cdot0 + 7\cdot6 + 8\cdot1 + 9\cdot5 + 10\cdot2$$
$$= 0 + 6 + 0 + 24 + 20 + 0 + 42 + 8 + 45 + 20 = 165 = 15 \cdot 11 .$$
Since $165 \equiv 0 \pmod{11}$, the ISBN is **valid** ✓.

(b) For the nine digits $d_1,\dots,d_9 = 0,2,0,1,5,3,0,8,2$, the condition $-\!d_{10} + \sum_{i\le9} i\,d_i \equiv 0 \pmod{11}$ (using $10 \equiv -1$) gives
$$d_{10} \equiv \sum_{i=1}^{9} i\,d_i = 1\cdot0 + 2\cdot2 + 3\cdot0 + 4\cdot1 + 5\cdot5 + 6\cdot3 + 7\cdot0 + 8\cdot8 + 9\cdot2 = 0+4+0+4+25+18+0+64+18 = 133 .$$
Now $133 = 12 \cdot 11 + 1$, so $d_{10} = 1$ and the full ISBN is $0\text{-}201\text{-}53082\text{-}1$.

(c) With modulus $11$ and weights $1, 2, \dots, 10$, a single-digit error at position $i$ changes the weighted sum by $i\,(d_i' - d_i)$. Since $11$ is prime, $11 \nmid i$ for $1 \le i \le 10$, and $0 < \lvert d_i' - d_i\rvert \le 10$, the product is nonzero modulo $11$ — the error is always caught. With modulus $10$ the same reasoning fails: the weight $5$ and the digit change $2$ give $5 \cdot 2 = 10 \equiv 0$, so changing a digit in position $5$ by $2$ would go undetected. Primality of the modulus is exactly what removes this failure.

## Advanced

**23.** *Strategy: $a$ and $b$ differ by a multiple of $n$, so the common divisors of $(a,n)$ and of $(b,n)$ are the same set.*

Since $a \equiv b \pmod n$, there is $k \in \mathbb{Z}$ with $a = b + kn$.

If $d \mid b$ and $d \mid n$ then $d \mid (b + kn) = a$ by D3, so $d$ is a common divisor of $a$ and $n$. Conversely, if $d \mid a$ and $d \mid n$ then $d \mid (a - kn) = b$, so $d$ is a common divisor of $b$ and $n$. Hence the two sets of positive common divisors coincide, and their maxima coincide:
$$\gcd(a,n) = \gcd(b,n) . \ \blacksquare$$

*Deduction.* By Proposition 7.5.1 a class is a unit exactly when its representative is coprime to $n$. Since coprimality to $n$ is constant on the class, the class is either entirely composed of units or entirely composed of non-units; equivalently, every residue class is either a unit or a non-unit. For example, modulo $15$ the classes $[1],[2],[4],[7],[8],[11],[13],[14]$ are units and the other seven are not — exactly $\varphi(15) = 8$ of them.

**24.** *Strategy: factor the difference of squares and apply Euclid's lemma with a prime modulus.*

*($\Leftarrow$)* If $a \equiv b$ then $a^2 \equiv b^2$ by Theorem 7.2.1(4). If $a \equiv -b$ then $a^2 \equiv (-b)^2 = b^2$. Either way $a^2 \equiv b^2 \pmod p$.

*($\Rightarrow$)* Suppose $p \mid (a^2 - b^2) = (a-b)(a+b)$. Since $p$ is prime, Euclid's lemma gives $p \mid (a-b)$ or $p \mid (a+b)$, that is $a \equiv b$ or $a \equiv -b \pmod p$. $\blacksquare$

*Why primality is essential.* Modulo $8$: $1^2 = 1$ and $3^2 = 9 \equiv 1 \pmod 8$, so $1^2 \equiv 3^2$, yet $3 \not\equiv 1$ and $3 \not\equiv -1 \equiv 7 \pmod 8$. The failure is exactly the failure of Euclid's lemma modulo $8$: $8 \mid (3-1)(3+1) = 2 \cdot 4$ although $8$ divides neither $2$ nor $4$.

**25.** *Strategy: three cases — $p = 2$, $p \equiv 3 \pmod 4$ (tutorial Example 9), $p \equiv 1 \pmod 4$ (Wilson).*

*Case $p = 2$:* $x = 1$ satisfies $1^2 = 1 \equiv -1 \pmod 2$ ✓.

*Case $p \equiv 3 \pmod 4$:* this is Example 9 of the tutorial — assuming $x^2 \equiv -1$ forces $x^{p-1} \equiv (-1)^{(p-1)/2} = -1$, contradicting Fermat's little theorem.

*Case $p \equiv 1 \pmod 4$:* let $m = (p-1)/2$, which is even. By Wilson's theorem,
$$(p-1)! \equiv -1 \pmod p .$$
Now split the factorial. For $1 \le j \le m$ we have $p - j \equiv -j \pmod p$, so
$$(p-1)! = \prod_{j=1}^{m} j \cdot \prod_{j=1}^{m}(p-j) \equiv m! \cdot (-1)^m\, m! = (m!)^2 ,$$
because $m$ is even. Hence $(m!)^2 \equiv -1 \pmod p$, and $x = m!$ is a solution. $\blacksquare$

*Checks.* $p = 5$: $m = 2$, $\;2! = 2$, $\;2^2 = 4 \equiv -1 \pmod 5$ ✓. $p = 13$: $m = 6$, $\;6! = 720 \equiv 5$, $\;5^2 = 25 \equiv 12 \equiv -1 \pmod{13}$ ✓. $p = 7 \equiv 3 \pmod 4$: the squares modulo $7$ are $0,1,2,4$, and $-1 \equiv 6$ is absent ✓.

**26.** *Strategy: divide $\varphi(n)$ by $d$ with remainder and use minimality of $d$.*

By Euler's theorem (Theorem 7.9.1), $a^{\varphi(n)} \equiv 1 \pmod n$, since $\gcd(a,n)=1$. Divide:
$$\varphi(n) = qd + r, \qquad 0 \le r < d .$$
Then
$$1 \equiv a^{\varphi(n)} = (a^d)^q \cdot a^r \equiv 1^q \cdot a^r = a^r \pmod n .$$
If $r > 0$ this contradicts the definition of $d$ as the *least* positive exponent with $a^d \equiv 1$. Hence $r = 0$, i.e. $d \mid \varphi(n)$. $\blacksquare$

*Deduction.* For $n = 101$ (prime, so $\varphi(101) = 100$) and $a \in \{1,\dots,100\}$ we have $\gcd(a,101)=1$; the order $d$ divides $100$, so $a^{100} = (a^d)^{100/d} \equiv 1 \pmod{101}$. (This is also Fermat's little theorem directly; the order argument explains *why* the exponent $100$ works even when a smaller one would do.)

**27.** *Strategy: every term is congruent to $1$ by Fermat's little theorem, so the sum is a count of terms.*

For $1 \le k \le p-1$ we have $p \nmid k$, so Fermat's little theorem gives $k^{p-1} \equiv 1 \pmod p$. Summing over the $p-1$ values of $k$:
$$\sum_{k=1}^{p-1} k^{p-1} \equiv \sum_{k=1}^{p-1} 1 = p - 1 \equiv -1 \pmod p . \ \blacksquare$$

*Check for $p = 5$:* $1^4 + 2^4 + 3^4 + 4^4 = 1 + 16 + 81 + 256 = 354 = 70 \cdot 5 + 4$, and $4 \equiv -1 \pmod 5$ ✓.

*Remark.* The analogous sum $\sum_{k=1}^{p-1} k^{e}$ with $(p-1) \nmid e$ is congruent to $0$, not $-1$; the proof needs a primitive root, and the result is used in the construction of finite fields.

**28.** *Strategy: analyse the $2$-adic valuation of $x^2 - 1 = (x-1)(x+1)$, whose two factors differ by $2$.*

Let $k \ge 3$ and suppose $x^2 \equiv 1 \pmod{2^k}$, i.e. $2^k \mid (x-1)(x+1)$.

*$x$ is odd.* If $x$ were even then $x - 1$ and $x + 1$ would both be odd, so $(x-1)(x+1)$ would be odd and could not be divisible by $4 \mid 2^k$.

So write $x$ odd. Then $x - 1$ and $x + 1$ are consecutive even numbers, and
$$\gcd(x-1,\, x+1) = \gcd(x-1,\, 2) = 2,$$
so exactly one of them is divisible by $4$; in particular one of them has exact $2$-adic valuation $1$, and all the factors of $2$ in the product come from the other one. Therefore
$$2^k \mid (x-1)(x+1) \iff 2^{k-1} \mid (x - 1) \ \text{ or } \ 2^{k-1} \mid (x+1),$$
that is, $x \equiv \pm 1 \pmod{2^{k-1}}$.

The four classes modulo $2^k$ that are $\pm 1$ modulo $2^{k-1}$ are
$$x \equiv 1, \quad x \equiv -1, \quad x \equiv 1 + 2^{k-1}, \quad x \equiv -1 + 2^{k-1} \pmod{2^k},$$
the last two being $\pm(1 + 2^{k-1})$ because $-1 + 2^{k-1} = -(1 - 2^{k-1}) \equiv -(1 + 2^{k-1}) \pmod{2^k}$. These are pairwise distinct modulo $2^k$ for $k \ge 3$. Every solution is one of them, so there are exactly four. $\blacksquare$

*Checks.* $k = 3$: $\{1, 7, 3, 5\} = \{1,3,5,7\}$, all four odd residues ✓ (consistent with Problem 4(b)). $k = 4$: $\{1, 15, 7, 9\}$; direct check $7^2 = 49 = 3\cdot 16 + 1$ ✓ and $9^2 = 81 = 5\cdot16 + 1$ ✓, while $3^2 = 9 \not\equiv 1 \pmod{16}$ ✓.

**29.** *Strategy: $1000 \equiv -1$ modulo each of $7$, $11$ and $13$, because $1001 = 7 \cdot 11 \cdot 13$.*

Write the decimal expansion in base $1000$: if the digits are grouped into blocks of three from the right, then
$$N = b_0 + b_1\cdot 1000 + b_2 \cdot 1000^2 + \cdots + b_s \cdot 1000^s,$$
where $0 \le b_i \le 999$ and $b_s \ne 0$. (For example $1234567 = 567 + 234 \cdot 1000 + 1\cdot 1000^2$, so $b_0 = 567$, $b_1 = 234$, $b_2 = 1$.)

Since $1000 = 1001 - 1$ and $1001 = 7 \cdot 11 \cdot 13$, for each $m \in \{7, 11, 13\}$ we have $1000 \equiv -1 \pmod m$, hence $1000^i \equiv (-1)^i \pmod m$ and therefore
$$N \equiv \sum_{i=0}^{s} (-1)^i b_i \pmod m .$$
So $m \mid N$ if and only if $m$ divides the alternating sum of the blocks. $\blacksquare$

*Check.* $N = 1234567$: alternating sum $567 - 234 + 1 = 334$. Since $334 = 7 \cdot 47 + 5$, $7 \nmid N$ ✓; since $334 = 30 \cdot 11 + 4$, $11 \nmid N$ ✓; since $334 = 25 \cdot 13 + 9$, $13 \nmid N$ ✓. Direct check for $7$: $1234567 = 7 \cdot 176366 + 5$ ✓.

**30.** *Strategy: express $2^{32}$ in terms of $5$ and $2^7$, using the two given identities.*

We work modulo $641$, where the two identities become congruences:
$$5 \cdot 2^7 = 641 - 1 \equiv -1, \qquad 5^4 + 2^4 = 641 \equiv 0 \ \text{ so } \ 5^4 \equiv -2^4 .$$

Raise the first congruence to the fourth power:
$$(5 \cdot 2^7)^4 \equiv (-1)^4 = 1 \pmod{641}, \qquad \text{i.e.} \qquad 5^4 \cdot 2^{28} \equiv 1 .$$
Substitute $5^4 \equiv -2^4$:
$$-2^4 \cdot 2^{28} \equiv 1 \pmod{641}, \qquad \text{i.e.} \qquad -2^{32} \equiv 1 \pmod{641} .$$
Therefore
$$2^{32} \equiv -1 \pmod{641}, \qquad \text{so} \qquad 641 \mid 2^{32} + 1 . \ \blacksquare$$

*Check of the cofactor:* $2^{32} + 1 = 4294967297 = 641 \cdot 6700417$ ✓, and $641 \cdot 6700417 = 4294967297$ exactly.

*Point of the exercise.* This is the cheapest possible refutation of Fermat's conjecture that all $F_n = 2^{2^n}+1$ are prime; the congruence argument replaces the computation of a ten-digit number by four modular multiplications, which is precisely the economy that Section 7.11 formalises.

**31.** *Strategy: if $\gcd(a,n)=1$ then $a$ is a unit and $x \mapsto ax$ is invertible; if $g > 1$ then count the fibres.*

$f$ is well defined by Theorem 7.2.1(3): if $[x] = [x']$ then $[ax] = [ax']$.

*($\Leftarrow$) Suppose $\gcd(a,n)=1$.* Then $a$ has an inverse $a^{-1}$ modulo $n$ (Proposition 7.5.1), and the map $[y] \mapsto [a^{-1}y]$ is an inverse function for $f$: indeed $f(a^{-1}y) = [a a^{-1} y] = [y]$ and $a^{-1}(ay) = [y]$. A map with a two-sided inverse is a bijection.

*($\Rightarrow$) Suppose $f$ is a bijection.* Then $f$ is surjective, so there is $[x]$ with $[ax] = [1]$, i.e. $ax \equiv 1 \pmod n$; by Proposition 7.5.1, $\gcd(a,n) = 1$.

*The case $g > 1$.* Let $g = \gcd(a,n)$. Then
$$f([x]) = f([x']) \iff n \mid a(x-x') \iff \frac{n}{g} \mid (x - x'),$$
by Theorem 7.4.1. So each value is attained on a full class modulo $n/g$, which contains exactly $g$ classes modulo $n$. Hence the image has
$$\frac{n}{g}$$
elements, and every fibre has $g$ elements. For instance $a = 4$, $n = 6$: $g = 2$, the image is $\{0, 2, 4\}$ (three $= 6/2$ elements), and indeed $4x \bmod 6 \in \{0,4,2\}$ ✓.

**32.** *Strategy: prove the congruence modulo each prime factor of $42$ and combine, since $42 = 2\cdot3\cdot7$ is squarefree.*

*Modulo $2$:* $n^7 \equiv n \pmod 2$ because both sides have the parity of $n$ (if $n$ is even both are $0$, if odd both are $1$).

*Modulo $3$:* by Fermat's little theorem $n^3 \equiv n \pmod 3$. Then
$$n^7 = n^3 \cdot n^3 \cdot n \equiv n \cdot n \cdot n = n^3 \equiv n \pmod 3 .$$

*Modulo $7$:* by Fermat's little theorem with $p = 7$, $\;n^7 \equiv n \pmod 7$ directly (valid for all $n$, including $n \equiv 0$).

So $2$, $3$ and $7$ each divide $n^7 - n$. They are pairwise coprime, so their product divides it:
$$42 \mid (n^7 - n) . \ \blacksquare$$

*Check:* $n = 2$: $128 - 2 = 126 = 3 \cdot 42$ ✓. $n = 5$: $78125 - 5 = 78120 = 1860 \cdot 42$ ✓.

## Challenge

**33.** *Strategy: solve $n$ congruences at once by the Chinese remainder theorem, using square moduli so that coprimality is automatic.*

Let $p_1, p_2, \dots, p_n$ be any $n$ distinct primes (for instance the first $n$ primes). The moduli $p_1^2, \dots, p_n^2$ are pairwise coprime, since distinct primes are coprime and hence so are their squares. By the Chinese remainder theorem (Theorem 7.7.2) the system
$$x \equiv -1 \pmod{p_1^2}, \quad x \equiv -2 \pmod{p_2^2}, \quad \dots, \quad x \equiv -n \pmod{p_n^2}$$
has a solution, unique modulo $M = p_1^2p_2^2\cdots p_n^2$. Choose the representative $x_0$ with $0 \le x_0 < M$, and then any $x = x_0 + tM$.

Consider the $n$ consecutive integers
$$x_0 + 1,\ x_0 + 2,\ \dots,\ x_0 + n .$$
For each $i$, the congruence gives $x_0 + i \equiv 0 \pmod{p_i^2}$, so $p_i^2$ divides $x_0 + i$. Since $p_i^2 \ge 4 > 1$, each of the $n$ numbers is divisible by a perfect square greater than $1$ — either it is $0$ (impossible, as $x_0 + i \ge 1$) or it is a nonzero multiple of $p_i^2$. $\blacksquare$

*Example for $n = 3$.* Take $p_1,p_2,p_3 = 2,3,5$ and moduli $4, 9, 25$. Solve $x \equiv 3 \pmod 4$, $x \equiv 7 \pmod 9$, $x \equiv 22 \pmod{25}$. From $x = 3 + 4j$: $3 + 4j \equiv 7 \pmod 9$ gives $4j \equiv 4$, $j \equiv 1 \pmod 9$, so $x \equiv 7 \pmod{36}$. Then $7 + 36t \equiv 22 \pmod{25}$: $\;7 + 11t \equiv 22$, $11t \equiv 15$, and $11^{-1} \equiv 16 \pmod{25}$ (as $11\cdot16 = 176 = 7\cdot25+1$), so $t \equiv 240 \equiv 15 \pmod{25}$ and $x = 7 + 540 = 547$. Then $548 = 4 \cdot 137$, $549 = 9 \cdot 61$, $550 = 25 \cdot 22$ ✓ — three consecutive numbers, each divisible by a square.

**34.** *Strategy: turn $p \mid a^2+b^2$ into a square root of $-1$ modulo $p$, then apply Problem 25.*

Let $p$ be an odd prime with $p \mid (a^2 + b^2)$ and $\gcd(a,b)=1$.

*$p \nmid b$.* If $p \mid b$, then $p \mid a^2$ (since $a^2 = (a^2+b^2) - b^2$ is a difference of two multiples of $p$), hence $p \mid a$; but then $p \mid \gcd(a,b) = 1$, absurd.

Since $p \nmid b$ and $p$ is prime, $b$ is a unit modulo $p$ (Proposition 7.5.1) with inverse $b^{-1}$. From $a^2 \equiv -b^2 \pmod p$, multiply by $(b^{-1})^2$:
$$\bigl(a\,b^{-1}\bigr)^2 \equiv -b^2(b^{-1})^2 = -1 \pmod p .$$
So $x = ab^{-1}$ is a square root of $-1$ modulo $p$. By Problem 25, a solution exists only when $p = 2$ or $p \equiv 1 \pmod 4$; as $p$ is odd, $p \equiv 1 \pmod 4$. $\blacksquare$

*Checks.* $p = 5$: $5 \mid 1^2 + 2^2 = 5$ ✓ and $5 \equiv 1 \pmod 4$ ✓. $p = 13$: $13 \mid 2^2 + 3^2 = 13$ ✓ and $13 \equiv 1 \pmod 4$ ✓. $p = 3$: $a^2 + b^2 \equiv a^2 + b^2$ with squares $\in\{0,1\}$; the only way to get $0 \pmod 3$ is both $\equiv 0$, contradicting coprimality ✓ — consistent with $3 \equiv 3 \pmod 4$.

**35.** *Strategy: Euclid-style construction, where the new prime is forced to be $\equiv 1 \pmod 4$ by Problem 34.*

Suppose, for contradiction, that $p_1, \dots, p_n$ are **all** the primes congruent to $1$ modulo $4$ (there is at least one, namely $5$, so the list is not empty). Put
$$P = p_1p_2\cdots p_n, \qquad N = (2P)^2 + 1 = 4P^2 + 1 .$$
Then $N \ge 5$ and $N$ is odd, so by Lemma 7.8.1 of [Divisibility and Primes](../01-divisibility-and-primes/README.md) it has an odd prime divisor $q$.

Now $q \mid N$ means $(2P)^2 \equiv -1 \pmod q$. Apply Problem 34 with $a = 2P$ and $b = 1$: these are coprime (any common divisor divides $1$), so $q \equiv 1 \pmod 4$. (Problem 34 requires $q$ odd, which holds.)

By the assumption, $q = p_i$ for some $i$. But then $p_i \mid P$, so $p_i \mid 4P^2$, and since $p_i \mid N = 4P^2+1$ we get $p_i \mid 1$ by D3 — impossible. Hence the list cannot be complete, and there are infinitely many primes $\equiv 1 \pmod 4$. $\blacksquare$

*Remark.* The same shape of argument proves infinitude of the primes $\equiv 3 \pmod 4$ using $N = 4P - 1$ (see Example 9 of [Divisibility and Primes](../01-divisibility-and-primes/README.md)); the two together give another proof of Euclid's theorem.

**36.** *Strategy: solve the congruence modulo each prime power, then multiply the counts using the Chinese remainder theorem.*

Let $n = p_1^{e_1}\cdots p_\omega^{e_\omega}$ with the $p_i$ distinct odd primes.

*Step 1: modulo an odd prime power, $x^2 \equiv 1$ has exactly two solutions.* Suppose $p^e \mid (x^2-1) = (x-1)(x+1)$. Any common divisor of $x-1$ and $x+1$ divides their difference $2$; since $p$ is odd, $p \nmid 2$, so $p$ cannot divide both factors. As $p$ is prime, $p^e \mid (x-1)$ or $p^e \mid (x+1)$ (Euclid's lemma applied to the prime $p$ repeatedly, or Corollary 7.9.3 of the previous topic). Hence
$$x \equiv 1 \pmod{p^e} \quad \text{or} \quad x \equiv -1 \pmod{p^e},$$
exactly two classes.

*Step 2: combine.* By the Chinese remainder theorem,
$$\mathbb{Z}/n\mathbb{Z} \;\cong\; \mathbb{Z}/p_1^{e_1}\mathbb{Z} \times \cdots \times \mathbb{Z}/p_\omega^{e_\omega}\mathbb{Z},$$
and $x^2 \equiv 1 \pmod n$ holds if and only if $x^2 \equiv 1$ modulo every $p_i^{e_i}$ (because $p_i^{e_i} \mid n$ one way, and the product divides $n$ the other way). So the solutions modulo $n$ correspond bijectively to the $\omega$-tuples of choices "$\pm 1$", one choice per prime. There are
$$2 \cdot 2 \cdots 2 = 2^{\omega}$$
such tuples, hence exactly $2^\omega$ solutions modulo $n$. $\blacksquare$

*Check for $n = 15$.* $\omega = 2$, so four solutions: combining $\pm1 \pmod 3$ with $\pm 1 \pmod 5$,
$$x \equiv 1,\ 4,\ 11,\ 14 \pmod{15},$$
and indeed $4^2 = 16 \equiv 1$, $11^2 = 121 = 8\cdot15 + 1$ ✓, $14^2 = 196 = 13\cdot15+1$ ✓.

*Check for $n = 45 = 3^2 \cdot 5$.* $\omega = 2$ again, so four solutions. The solutions of $x^2 \equiv 1 \pmod 9$ are $1$ and $8$; modulo $5$ they are $1$ and $4$. Combining:
$$(1,1)\mapsto 1, \quad (1,4) \mapsto 19, \quad (8,1) \mapsto 26, \quad (8,4) \mapsto 44,$$
and indeed $19^2 = 361 = 8\cdot45 + 1$ ✓, $26^2 = 676 = 15\cdot45+1$ ✓, $44^2 = 1936 = 43\cdot45+1$ ✓. Note that the count depends on the number of *distinct* primes, not on their exponents: $n = 45$ and $n = 15$ both give four.
