# Natural Numbers — Solutions

> Part of [Natural Numbers](README.md) · Solutions to [exercises.md](exercises.md)

Every solution states the strategy first, then every significant step. Arithmetic checks are given
where they catch the most common errors.

---

## Beginner

**1.** *Strategy: read the digits against their place values.*

The places, from the right, are $10^0, 10^1, 10^2, 10^3, 10^4$. Hence

$$47{,}305 = 4 \cdot 10^4 + 7 \cdot 10^3 + 3 \cdot 10^2 + 0 \cdot 10^1 + 5 \cdot 10^0.$$

The digit $3$ sits in the hundreds place and contributes $3 \cdot 100 = 300$. The digit $7$ sits in
the thousands place and contributes $7 \cdot 1{,}000 = 7{,}000$. The digit $0$ contributes nothing
but keeps the $3$ in the hundreds place: writing $4{,}735$ would move the $3$ into the tens place.

**2.** *Strategy: compare the number of digits first; if they agree, compare digits from the left.*

(a) Both have four digits. The thousands digits are equal ($5 = 5$), and the hundreds digits satisfy
$0 < 1$. Hence $5{,}099 < 5{,}100$.

(b) Both have five digits, and the first three digits agree ($1, 2, 3$). The thousands digits are
$4 < 5$, so $12{,}345 < 12{,}354$.

(c) $999$ has three digits and $1{,}000$ has four, so $999 < 1{,}000$.

(d) Both have four digits. Compare: $7 = 7$, then $0 = 0$, then tens digits $7 > 0$. Hence
$7{,}070 > 7{,}007$.

**3.** *Strategy: column addition from the right, carrying one ten for every ten units.*

| column | digits | sum | written | carried |
|---|---|---|---|---|
| units | $8 + 6$ | $14$ | $4$ | $1$ |
| tens | $7 + 4 + 1$ | $12$ | $2$ | $1$ |
| hundreds | $4 + 9 + 1$ | $14$ | $4$ | $1$ |
| thousands | $3 + 2 + 1$ | $6$ | $6$ | $0$ |

So $3{,}478 + 2{,}946 = 6{,}424$.

*Check.* Rounding to the nearest hundred: $3{,}478 \approx 3{,}500$ and $2{,}946 \approx 2{,}900$,
whose sum is $6{,}400$. The exact answer $6{,}424$ is within $100$ of the estimate, as it must be,
since the two rounding errors are $+22$ and $-46$.

**4.** *Strategy: borrow one thousand and cascade it down to the units.*

Because the tens and hundreds digits of $5{,}002$ are zero, decompose it as

$$5{,}002 = 4 \cdot 10^3 + 9 \cdot 10^2 + 9 \cdot 10 + 12.$$

Then subtract column by column:

* units: $12 - 7 = 5$;
* tens: $9 - 4 = 5$;
* hundreds: $9 - 8 = 1$;
* thousands: $4 - 1 = 3$.

Hence $5{,}002 - 1{,}847 = 3{,}155$.

*Check.* $3{,}155 + 1{,}847 = 5{,}002$: units $5+7 = 12$ (write $2$, carry $1$), tens
$5+4+1 = 10$ (write $0$, carry $1$), hundreds $1+8+1 = 10$ (write $0$, carry $1$), thousands
$3+1+1 = 5$. ✓

**5.** *Strategy: split one factor by place value, multiply each part, add.*

$$34 \cdot 26 = 34 \cdot (20 + 6) = 34 \cdot 20 + 34 \cdot 6 = 680 + 204 = 884.$$

The area picture: a $34 \times 26$ rectangle is cut into four rectangles with sides $30$ or $4$ and
$20$ or $6$, with areas

$$30 \cdot 20 = 600, \qquad 30 \cdot 6 = 180, \qquad 4 \cdot 20 = 80, \qquad 4 \cdot 6 = 24.$$

Their sum is $600 + 180 + 80 + 24 = 884$, the same answer. The two methods agree because both are
the distributive law applied to the same decomposition.

**6.** *Strategy: long division, digit by digit, with a running remainder.*

* $93 \div 25 = 3$ with remainder $93 - 75 = 18$: write $3$;
* bring down $7$ to get $187$; $187 \div 25 = 7$ with remainder $187 - 175 = 12$: write $7$;
* bring down $5$ to get $125$; $125 \div 25 = 5$ with remainder $0$: write $5$.

Therefore $9{,}375 = 25 \cdot 375 + 0$: quotient $375$, remainder $0$.

*Check.* $25 \cdot 375 = 25 \cdot 300 + 25 \cdot 75 = 7{,}500 + 1{,}875 = 9{,}375$ and
$0 \le 0 < 25$. ✓

**7.** (a) Factor $48 = 2^4 \cdot 3$. The divisors are

$$1,\ 2,\ 3,\ 4,\ 6,\ 8,\ 12,\ 16,\ 24,\ 48,$$

ten in all, or $5 \cdot 2 = 10$ by the exponent formula.

(b) The first six multiples of $7$ are $7, 14, 21, 28, 35, 42$.

(c) For any $d \ne 0$, the equation $0 = d \cdot 0$ exhibits $0$ as a multiple of $d$; equivalently
$d \mid 0$. So every nonzero natural number is a factor of $0$, and $0$ has infinitely many factors.
By contrast, if $n \ge 1$ and $d \mid n$, then $n = dk$ with $k \ge 1$, so $d \le n$; a positive
number has at most $n$ possible factors and therefore only finitely many.

**8.** *Strategy: test primes up to $\sqrt{n}$.*

* $51 = 3 \cdot 17$ — composite.
* $57 = 3 \cdot 19$ — composite.
* $61$: $\sqrt{61} \approx 7.8$, so test $2, 3, 5, 7$. It is odd, its digit sum is $7$, it does not
  end in $0$ or $5$, and $7 \cdot 8 = 56$, $7 \cdot 9 = 63$. Hence prime.
* $67$: $\sqrt{67} \approx 8.2$, test $2, 3, 5, 7$. It is odd, digit sum $13$, not ending in
  $0$ or $5$, and $7 \cdot 9 = 63$, $7 \cdot 10 = 70$. Hence prime.
* $87 = 3 \cdot 29$ — composite.
* $91 = 7 \cdot 13$ — composite (this is the classic trap: $91$ "looks" prime).

**9.** *Strategy: divide repeatedly by the smallest prime that divides the current number.*

For $180$:

$$180 \div 2 = 90, \quad 90 \div 2 = 45, \quad 45 \div 3 = 15, \quad 15 \div 3 = 5, \quad 5 \div 5 = 1.$$

So $180 = 2^2 \cdot 3^2 \cdot 5$; check $4 \cdot 9 \cdot 5 = 180$. ✓

For $84$:

$$84 \div 2 = 42, \quad 42 \div 2 = 21, \quad 21 \div 3 = 7, \quad 7 \div 7 = 1.$$

So $84 = 2^2 \cdot 3 \cdot 7$; check $4 \cdot 3 \cdot 7 = 84$. ✓

Both are in canonical form: primes increasing, exponents positive.

**10.** *Strategy: use $\min$ and $\max$ of exponents.*

$$36 = 2^2 \cdot 3^2, \qquad 60 = 2^2 \cdot 3 \cdot 5.$$

So

$$\gcd(36,60) = 2^2 \cdot 3 = 12, \qquad \operatorname{lcm}(36,60) = 2^2 \cdot 3^2 \cdot 5 = 180.$$

Check: $12 \cdot 180 = 2{,}160$ and $36 \cdot 60 = 2{,}160$. ✓

*Sanity check.* $\gcd \le 36$ ✓ and $\operatorname{lcm} \ge 60$ ✓; also $\gcd$ divides both numbers
($12 \mid 36$, $12 \mid 60$) and both divide the lcm ($36 \mid 180$, $60 \mid 180$).

**11.** *Strategy: evaluate the expansion.*

$$(1011)_2 = 1 \cdot 2^3 + 0 \cdot 2^2 + 1 \cdot 2^1 + 1 \cdot 2^0 = 8 + 0 + 2 + 1 = 11,$$

$$(11010)_2 = 1 \cdot 2^4 + 1 \cdot 2^3 + 0 \cdot 2^2 + 1 \cdot 2^1 + 0 \cdot 2^0 = 16 + 8 + 2 = 26.$$

**12.** *Strategy: subtract the largest power of $2$ repeatedly, or divide by $2$ repeatedly.*

For $19$: the largest power of $2$ not exceeding $19$ is $16$, and $19 - 16 = 3 = 2 + 1$. Hence

$$19 = 16 + 2 + 1 = (10011)_2.$$

For $42$: $42 = 32 + 10 = 32 + 8 + 2$, so

$$42 = (101010)_2.$$

*Check by division.* $42 \div 2 = 21$ r $0$; $21 \div 2 = 10$ r $1$; $10 \div 2 = 5$ r $0$;
$5 \div 2 = 2$ r $1$; $2 \div 2 = 1$ r $0$; $1 \div 2 = 0$ r $1$; reading up: $101010$. ✓

---

## Intermediate

**13.** *Strategy: cross out multiples of every prime $p$ with $p \le \sqrt{59}$.*

Since $\sqrt{59} \approx 7.68$, it is enough to cross out multiples of $2, 3, 5, 7$. (If
$n < 60$ were composite with all prime factors exceeding $7$, then $n \ge 11 \cdot 11 = 121 > 60$.)

After removing $1$ and crossing out multiples of $2$, then $3$, then $5$, then $7$, the survivors
below $60$ are

$$2,\ 3,\ 5,\ 7,\ 11,\ 13,\ 17,\ 19,\ 23,\ 29,\ 31,\ 37,\ 41,\ 43,\ 47,\ 53,\ 59,$$

seventeen primes. The largest crossing-out prime needed is $7$; using $11$ would be harmless but
unnecessary, since $11^2 = 121 > 59$ and every multiple of $11$ below $60$ already has a smaller
prime factor ($22, 33, 44, 55$ have $2, 3, 2, 5$ respectively).

**14.** *Strategy: apply $\gcd(a,b) = \gcd(b,r)$ until the remainder is $0$.*

$$252 = 1 \cdot 198 + 54,$$
$$198 = 3 \cdot 54 + 36,$$
$$54 = 1 \cdot 36 + 18,$$
$$36 = 2 \cdot 18 + 0.$$

The last nonzero remainder is $18$, so $\gcd(252,198) = 18$.

*Check by factorisation.* $252 = 2^2 \cdot 3^2 \cdot 7$ and $198 = 2 \cdot 3^2 \cdot 11$, so the gcd
is $2 \cdot 3^2 = 18$. ✓

**15.** (a)

$$391 = 1 \cdot 357 + 34,$$
$$357 = 10 \cdot 34 + 17,$$
$$34 = 2 \cdot 17 + 0.$$

Hence $\gcd(391,357) = 17$. Check: $391 = 17 \cdot 23$ and $357 = 17 \cdot 21$. ✓

(b)

$$2024 = 12 \cdot 168 + 8,$$
$$168 = 21 \cdot 8 + 0.$$

Hence $\gcd(2024,168) = 8$. For the lcm,

$$\operatorname{lcm}(2024,168) = \dfrac{2024 \cdot 168}{8} = 2024 \cdot 21 = 42{,}504.$$

*Check.* $2024 = 8 \cdot 253 = 2^3 \cdot 11 \cdot 23$ and $168 = 2^3 \cdot 3 \cdot 7$, so the lcm is
$2^3 \cdot 3 \cdot 7 \cdot 11 \cdot 23 = 8 \cdot 5313 = 42{,}504$. ✓

**16.** (a) Estimate: $17 \cdot 250 = 4{,}250$, leaving $4{,}387 - 4{,}250 = 137$; and
$17 \cdot 8 = 136$. So $4{,}387 = 17 \cdot 258 + 1$. Thus $q = 258$, $r = 1$. Check:
$0 \le 1 < 17$ ✓ and $17 \cdot 258 + 1 = 4{,}386 + 1 = 4{,}387$ ✓.

(b) The largest multiple of $7$ not exceeding $1{,}000$ is $7 \cdot 142 = 994$. Hence
$1{,}000 = 7 \cdot 142 + 6$, so $q = 142$, $r = 6$. Check: $0 \le 6 < 7$ ✓ and
$994 + 6 = 1{,}000$ ✓.

**17.** *Strategy: one of the two conditions is more restrictive, so enumerate its solutions and
test the other.*

The numbers in $[0, 24)$ leaving remainder $3$ on division by $4$ are

$$3,\ 7,\ 11,\ 15,\ 19,\ 23.$$

Test each modulo $3$:

| $n$ | $3$ | $7$ | $11$ | $15$ | $19$ | $23$ |
|---|---|---|---|---|---|---|
| $n \bmod 3$ | $0$ | $1$ | $2$ | $0$ | $1$ | $2$ |

The survivors are $n = 11$ and $n = 23$.

*Why these are all.* Both conditions are preserved when $12$ is added, because $12$ is divisible by
both $3$ and $4$. Since $11$ is a solution and $11 + 12 = 23 < 24 \le 11 + 24$, the complete list in
the range is $\{11, 23\}$.

*Check.* $11 = 3 \cdot 3 + 2$ ✓ and $11 = 4 \cdot 2 + 3$ ✓; $23 = 3 \cdot 7 + 2$ ✓ and
$23 = 4 \cdot 5 + 3$ ✓.

**18.** (a) **Digit-sum test.** A number is divisible by $3$ exactly when the sum of its decimal
digits is divisible by $3$; it is divisible by $9$ exactly when the digit sum is divisible by $9$.
The proof is in Exercise 28.

(b) For $4{,}728$: $4 + 7 + 2 + 8 = 21$. Since $21 = 3 \cdot 7$, the number is divisible by $3$;
since $21$ is not a multiple of $9$, it is not divisible by $9$. Direct check: $4728/3 = 1576$
exactly ✓; $4728/9 = 525$ remainder $3$ ✓.

For $1{,}234{,}567$: $1+2+3+4+5+6+7 = 28$, which is not a multiple of $3$ (or of $9$). So the number
is divisible by neither $3$ nor $9$.

*Pitfall.* The test says nothing about divisibility by $2$, $5$ or $7$; those need their own rules.

**19.** (a) Column addition in base $2$, carrying when a column reaches $2$:

$$1011_2 + 1101_2 = 11000_2.$$

Units: $1+1 = 10_2$ (write $0$, carry $1$). Twos: $1+0+1 = 10_2$ (write $0$, carry $1$). Fours:
$0+1+1 = 10_2$ (write $0$, carry $1$). Eights: $1+1+1 = 11_2$ (write $1$, carry $1$). Sixteens:
$1$. Result $11000_2$. Check: $11 + 13 = 24 = 16 + 8$ ✓.

(b) $1101_2 - 1011_2 = 0010_2 = 10_2$. Check: $13 - 11 = 2$ ✓.

(c) $1101_2 \times 101_2$: multiply by each bit and shift,

$$1101 \cdot 1 = 1101, \qquad 1101 \cdot 0 = 0000 \text{ (shifted one place)}, \qquad
1101 \cdot 1 = 1101 \text{ (shifted two places)}.$$

Adding $1101_2 + 110100_2$:

$$1101 + 110100 = 1000001_2.$$

Check: $13 \cdot 5 = 65 = 64 + 1$ ✓.

**20.** (a) Repeated division by $7$:

$$250 = 35 \cdot 7 + 5, \qquad 35 = 5 \cdot 7 + 0, \qquad 5 = 0 \cdot 7 + 5.$$

Reading remainders from the last division to the first: $250 = (505)_7$. Check:
$5 \cdot 49 + 0 \cdot 7 + 5 = 245 + 5 = 250$ ✓.

(b) Repeated division by $3$:

$$100 = 33 \cdot 3 + 1, \quad 33 = 11 \cdot 3 + 0, \quad 11 = 3 \cdot 3 + 2, \quad
3 = 1 \cdot 3 + 0, \quad 1 = 0 \cdot 3 + 1.$$

Reading upwards: $100 = (10201)_3$. Check:
$1 \cdot 81 + 0 \cdot 27 + 2 \cdot 9 + 0 \cdot 3 + 1 = 81 + 18 + 1 = 100$ ✓.

**21.** (a) $1{,}001 = 7 \cdot 143 = 7 \cdot 11 \cdot 13$. Check: $7 \cdot 11 = 77$ and
$77 \cdot 13 = 1{,}001$ ✓.

(b) $1{,}024 = 2^{10}$, since $1{,}024 = 2 \cdot 512 = 2 \cdot 2^9$.

(c) $5{,}040 = 504 \cdot 10 = (2^3 \cdot 3^2 \cdot 7)(2 \cdot 5) = 2^4 \cdot 3^2 \cdot 5 \cdot 7$.
Check: $16 \cdot 9 = 144$, $144 \cdot 35 = 5{,}040$ ✓.

**22.** Factor:

$$1{,}800 = 2^3 \cdot 3^2 \cdot 5^2, \qquad 2{,}520 = 2^3 \cdot 3^2 \cdot 5 \cdot 7.$$

Take minimum exponents for the gcd and maximum exponents for the lcm:

$$\gcd(1{,}800, 2{,}520) = 2^3 \cdot 3^2 \cdot 5 = 360,$$
$$\operatorname{lcm}(1{,}800, 2{,}520) = 2^3 \cdot 3^2 \cdot 5^2 \cdot 7 = 12{,}600.$$

*Check.* $360 \cdot 12{,}600 = 4{,}536{,}000$ and $1{,}800 \cdot 2{,}520 = 4{,}536{,}000$ ✓.

---

## Advanced

**23.** Throughout, divisibility in $\mathbb{Z}$ means: $a \mid b$ if and only if $b = ak$ for some
$k \in \mathbb{Z}$.

(a) Suppose $a \mid b$ and $b \mid c$. Then there are $k, l \in \mathbb{Z}$ with $b = ak$ and
$c = bl$. Substituting,

$$c = bl = (ak)l = a(kl).$$

Since $kl \in \mathbb{Z}$, this says $a \mid c$. $\blacksquare$

(b) Suppose $a \mid b$ and $a \mid c$, say $b = am$ and $c = an$. Then for any $x, y \in \mathbb{Z}$,

$$bx + cy = (am)x + (an)y = a(mx + ny),$$

and $mx + ny \in \mathbb{Z}$, so $a \mid (bx + cy)$. $\blacksquare$

Part (b) says: a divisor of $b$ and $c$ divides every integer combination of $b$ and $c$. This is the
property that makes the Euclidean algorithm and Bézout's identity work.

(c) Take $a = 6$, $b = 4$, $c = 3$. Then $bc = 12$ and $6 \mid 12$, but $6 \nmid 4$ and $6 \nmid 3$.
So divisibility of a product does not pass to the factors. What *is* true is Euclid's lemma: if $p$
is prime and $p \mid bc$, then $p \mid b$ or $p \mid c$. The example fails because $6$ is not prime.

**24.** *Strategy: write the integer by the division algorithm and square it.*

Let $n \in \mathbb{Z}$. Apply Theorem 8.4 to $|n|$: there are $q \ge 0$ and $r \in \{0, 1, 2\}$ with
$|n| = 3q + r$. Since $n^2 = |n|^2$,

$$n^2 = (3q + r)^2 = 9q^2 + 6qr + r^2 = 3(3q^2 + 2qr) + r^2.$$

Now examine the three cases:

* $r = 0$: $n^2 = 3(3q^2)$, of the form $3k$.
* $r = 1$: $n^2 = 3(3q^2 + 2q) + 1$, of the form $3k + 1$.
* $r = 2$: $r^2 = 4 = 3 + 1$, so $n^2 = 3(3q^2 + 4q) + 3 + 1 = 3(3q^2 + 4q + 1) + 1$, again of the
  form $3k + 1$.

In every case $n^2$ is $3k$ or $3k+1$. Since a number cannot be congruent to both $1$ and $2$
modulo $3$ (trichotomy), no square is of the form $3k + 2$. $\blacksquare$

*Example check.* $7^2 = 49 = 3 \cdot 16 + 1$ ✓; $6^2 = 36 = 3 \cdot 12$ ✓; $5^2 = 25 = 3 \cdot 8 + 1$ ✓.

**25.** (a) From Exercise 15-style steps,

$$1071 = 2 \cdot 462 + 147, \qquad 462 = 3 \cdot 147 + 21, \qquad 147 = 7 \cdot 21 + 0,$$

so $\gcd(1071,462) = 21$. Work upwards from the second-to-last division:

$$21 = 462 - 3 \cdot 147.$$

Replace $147 = 1071 - 2 \cdot 462$:

$$21 = 462 - 3(1071 - 2 \cdot 462) = 462 - 3 \cdot 1071 + 6 \cdot 462 = 7 \cdot 462 - 3 \cdot 1071.$$

Hence $21 = (-3) \cdot 1071 + 7 \cdot 462$. *Check:* $7 \cdot 462 = 3{,}234$ and
$3 \cdot 1071 = 3{,}213$, and $3{,}234 - 3{,}213 = 21$ ✓.

(b)

$$391 = 1 \cdot 357 + 34, \qquad 357 = 10 \cdot 34 + 17, \qquad 34 = 2 \cdot 17 + 0,$$

so $\gcd(391,357) = 17$. Then

$$17 = 357 - 10 \cdot 34,$$

and replacing $34 = 391 - 357$ gives

$$17 = 357 - 10(391 - 357) = 357 - 10 \cdot 391 + 10 \cdot 357 = 11 \cdot 357 - 10 \cdot 391.$$

*Check:* $11 \cdot 357 = 3{,}927$ and $10 \cdot 391 = 3{,}910$, and $3{,}927 - 3{,}910 = 17$ ✓.

**26.** *Strategy: Bézout converts the coprimality hypothesis into an equation, and that equation
lets us move a factor.*

Suppose $a \mid c$ and $b \mid c$, and $\gcd(a,b) = 1$. Write $c = am$ with $m \in \mathbb{Z}$.

Because $\gcd(a,b) = 1$, Bézout's identity (Theorem 8.6) gives integers $x, y$ with

$$ax + by = 1.$$

Multiply by $m$:

$$m = amx + bmy.$$

Now $b$ divides $amx = cx$ (since $b \mid c$) and $b$ divides $bmy$. Hence $b$ divides
$m = amx + bmy$. Write $m = bn$ with $n \in \mathbb{Z}$. Then

$$c = am = a(bn) = (ab)n,$$

so $ab \mid c$. $\blacksquare$

*Second approach.* From $b \mid am$ and $\gcd(a,b) = 1$, Euclid's lemma applied to the prime
factorisation of $b$ gives $b \mid m$ directly; the rest is identical. The Bézout proof is shorter
because it does not pass through prime factorisation.

*Why the coprimality hypothesis is needed.* $6 \mid 12$ and $4 \mid 12$, but $24 \nmid 12$. Here
$\gcd(6,4) = 2 \ne 1$.

**27.** (a) Let $n = p_1^{e_1} \cdots p_k^{e_k}$ with the $p_i$ distinct primes.

*Every* divisor $d$ of $n$ has the form $d = p_1^{f_1} \cdots p_k^{f_k}$ with $0 \le f_i \le e_i$.
Indeed, by the fundamental theorem of arithmetic, the primes dividing $d$ form a sub-multiset of the
primes dividing $n$; hence $d$ uses only the primes $p_i$, and the exponent of $p_i$ in $d$ cannot
exceed its exponent in $n$ (if $f_i > e_i$, then $p_i^{e_i+1}$ would divide $n$, impossible).

Conversely, every choice of exponents $f_i$ with $0 \le f_i \le e_i$ gives a divisor, and different
choices give different numbers by uniqueness of prime factorisation.

The number of choices is the product $(e_1+1)(e_2+1)\cdots(e_k+1)$, since the choice of $f_i$ is
independent for each $i$. $\blacksquare$

(b) $360 = 2^3 \cdot 3^2 \cdot 5$, so

$$d(360) = (3+1)(2+1)(1+1) = 4 \cdot 3 \cdot 2 = 24.$$

$1{,}000 = 2^3 \cdot 5^3$, so

$$d(1{,}000) = (3+1)(3+1) = 16.$$

The sixteen divisors are $1, 2, 4, 8, 5, 10, 20, 40, 25, 50, 100, 200, 125, 250, 500, 1{,}000$.

**28.** *Strategy: compare $n$ with its digit sum; the difference is a sum of multiples of $9$.*

Let $n$ have decimal digits $d_k, \dots, d_0$, so

$$n = d_k 10^k + \cdots + d_1 \cdot 10 + d_0.$$

Subtract the digit sum:

$$n - (d_k + \cdots + d_1 + d_0) = d_k(10^k - 1) + \cdots + d_1(10 - 1) + d_0(1 - 1).$$

For each $i \ge 1$,

$$10^i - 1 = \underbrace{99\cdots 9}_{i \text{ nines}} = 9 \cdot \underbrace{11\cdots 1}_{i \text{ ones}},$$

which is divisible by $9$ and hence by $3$. Therefore $n - (\text{digit sum})$ is divisible by $9$
and by $3$.

Now use the elementary fact that if $m \mid (n - s)$, then $m \mid n$ exactly when $m \mid s$. (Proof:
$n = (n - s) + s$, so $m$ divides $n$ if and only if it divides $s$.) Applying this with $m = 9$ and
with $m = 3$, and with $s$ the digit sum, gives:

$$9 \mid n \iff 9 \mid (\text{digit sum}), \qquad 3 \mid n \iff 3 \mid (\text{digit sum}).$$

$\blacksquare$

*Example.* $4{,}728$: the digit sum is $21$, so $3 \mid 4{,}728$ but $9 \nmid 4{,}728$. Indeed
$4{,}728 = 3 \cdot 1{,}576$ and $4{,}728 = 9 \cdot 525 + 3$.

**29.** *Strategy: build the numbers so that each has a known divisor.*

Let $M = (n+1)!$ and consider the $n$ consecutive numbers

$$M + 2,\ M + 3,\ \dots,\ M + (n+1).$$

For each $k$ with $2 \le k \le n+1$, the number $k$ divides $M$ (because $k$ is one of the factors of
$(n+1)!$). Hence $k$ divides $M + k$. Moreover

$$M + k > k,$$

so $M + k$ has a divisor $k$ with $1 < k < M+k$, which is exactly what it means to be composite.

The numbers are consecutive (each is one more than the previous) and there are exactly $n$ of them
($k$ runs from $2$ to $n+1$). $\blacksquare$

*Example* $n = 4$: $(5)! = 120$, and $122, 123, 124, 125$ are four consecutive composites, divisible
by $2, 3, 4, 5$ respectively. (Smaller runs exist, of course; the construction is not meant to be
optimal.)

---

## Challenge

**30.** *Strategy: assume the contrary, write the fraction in lowest terms, and show the lowest-terms
assumption is violated.*

Suppose $\sqrt{2}$ is rational. Then there exist $p, q \in \mathbb{N}^{+}$ with

$$\sqrt{2} = \dfrac{p}{q}.$$

*Why we may assume $\gcd(p,q) = 1$.* Among all representations of the same rational number, choose
one with the smallest denominator $q$. If $p$ and $q$ had a common divisor $d > 1$, then
$p/d$ and $q/d$ would be natural numbers and $p/q = (p/d)/(q/d)$ would be a representation with the
smaller denominator $q/d$, contradicting minimality. (Equivalently, cancel common factors until none
remain; the process terminates because the denominator strictly decreases.) So $\gcd(p,q) = 1$.

Squaring both sides gives $2 = p^2/q^2$, hence

$$p^2 = 2q^2.$$

So $2 \mid p^2$. Since $2$ is prime, Euclid's lemma (Lemma 8.7) gives $2 \mid p$. Write $p = 2r$ with
$r \in \mathbb{N}^{+}$. Substituting into the displayed equation above:

$$(2r)^2 = 2q^2 \implies 4r^2 = 2q^2 \implies q^2 = 2r^2.$$

So $2 \mid q^2$, and again Euclid's lemma gives $2 \mid q$.

Thus $2$ divides both $p$ and $q$, contradicting $\gcd(p,q) = 1$ (a common divisor $2$ would make the
gcd at least $2$). The assumption that $\sqrt2$ is rational is therefore false. $\blacksquare$

*Remark.* The same argument, with $2$ replaced by any prime $p$, shows that $\sqrt{p}$ is irrational.
The proof uses only the fundamental theorem of arithmetic and the definition of a rational number.

**31.** (a) Let $n \ge 2$ be composite. Then $n = ab$ with integers $1 < a, b < n$. Suppose, for
contradiction, that both $a > \sqrt{n}$ and $b > \sqrt{n}$. Multiplying these inequalities (both
sides positive) gives

$$n = ab > \sqrt{n}\cdot\sqrt{n} = n,$$

which is impossible. Hence at least one of $a, b$ is at most $\sqrt n$; assume it is $a$.

Now $a > 1$, so $a$ has a prime divisor $p$ (Theorem 8.8, existence of a prime factorisation). Since
$p \le a$ and $a \le \sqrt n$, we get $p \le \sqrt n$, and $p \mid a$, $a \mid n$ give $p \mid n$.
$\blacksquare$

(b) **$127$.** $\sqrt{127} \approx 11.27$, so test the primes $2, 3, 5, 7, 11$. Now $127$ is odd, its
digit sum is $1+2+7 = 10$ (not divisible by $3$), it does not end in $0$ or $5$, and
$7 \cdot 18 = 126$ (remainder $1$), $11 \cdot 11 = 121$ (remainder $6$). No prime up to
$\sqrt{127}$ divides it, so $127$ is prime.

**$149$.** $\sqrt{149} \approx 12.21$, so test $2, 3, 5, 7, 11$ (the next prime, $13$, already
exceeds $\sqrt{149}$). Digit sum $1+4+9 = 14$; odd; not ending in $5$; $7 \cdot 21 = 147$
(remainder $2$); $11 \cdot 13 = 143$ (remainder $6$). Hence $149$ is prime.

**$221$.** $\sqrt{221} \approx 14.87$, so test $2, 3, 5, 7, 11, 13$. Digit sum $5$; odd; not ending
in $5$; $7 \cdot 31 = 217$ (remainder $4$); $11 \cdot 20 = 220$ (remainder $1$); $13 \cdot 17 = 221$
exactly. Hence $221$ is composite, with $221 = 13 \cdot 17$.

*Why we may stop at $\sqrt n$.* If no prime $p \le \sqrt n$ divides $n$, then part (a) says $n$ cannot
be composite; since $n \ge 2$, it must be prime.

**32.** *Strategy: force a difference of two squares.*

Complete the square and then subtract:

$$n^4 + 4 = n^4 + 4n^2 + 4 - 4n^2 = (n^2 + 2)^2 - (2n)^2.$$

This is a difference of squares $A^2 - B^2 = (A - B)(A + B)$ with $A = n^2 + 2$ and $B = 2n$:

$$n^4 + 4 = (n^2 - 2n + 2)(n^2 + 2n + 2).$$

Now rewrite the factors to see their size:

$$n^2 - 2n + 2 = (n-1)^2 + 1, \qquad n^2 + 2n + 2 = (n+1)^2 + 1.$$

For $n \ge 2$ both factors are integers at least $2$: the first is at least $(1)^2 + 1 = 2$ and the
second at least $3^2 + 1 = 10$. A product $AB$ with $A \ge 2$ and $B \ge 2$ is strictly larger than
each factor, so $n^4 + 4$ has a proper factorisation with both factors greater than $1$. Hence it is
composite. $\blacksquare$

For $n = 1$ the identity gives $1 + 4 = (1)(5) = 5$, a prime; the hypothesis $n \ge 2$ is exactly
what makes both factors exceed $1$. For $n = 0$ the value is $4 = 2 \cdot 2$, composite.

**33.** (a) *Strategy: induction on $n$, using $(x-1)(x+1) = x^2 - 1$.*

*Base case* $n = 1$: $F_0 = 3$ and $F_1 - 2 = 5 - 2 = 3$. ✓

*Induction step.* Assume $F_0 F_1 \cdots F_{n-1} = F_n - 2$. Then

$$F_0 \cdots F_{n-1} F_n = (F_n - 2)F_n = \left(2^{2^n} - 1\right)\left(2^{2^n} + 1\right)
= \left(2^{2^n}\right)^2 - 1 = 2^{2^{n+1}} - 1 = F_{n+1} - 2.$$

That is the statement for $n+1$. By induction the identity holds for every $n \ge 1$.
$\blacksquare$

(b) Let $m < n$ and suppose $d$ divides both $F_m$ and $F_n$. Since $F_m$ is one of the factors of
$F_0 F_1 \cdots F_{n-1}$, the identity of part (a) shows that $F_m$ divides $F_n - 2$. Hence $d$
divides $F_n - 2$ as well as $F_n$, so

$$d \mid F_n - (F_n - 2) = 2.$$

Every Fermat number is odd, because $2^{2^n}$ is even and adding $1$ gives an odd number. Therefore
$d$, being a divisor of the odd number $F_m$, is odd. The only odd divisor of $2$ is $1$, so $d = 1$.
Hence $\gcd(F_m, F_n) = 1$. $\blacksquare$

(c) Each $F_n \ge 3$ has at least one prime divisor $p_n$, by Theorem 8.8 applied to $F_n$. By part
(b), $F_m$ and $F_n$ share no prime divisor when $m \ne n$, so the primes $p_0, p_1, p_2, \dots$ are
pairwise distinct. A set containing infinitely many distinct primes is infinite, so there are
infinitely many primes. $\blacksquare$

*Remark.* The Fermat numbers therefore give a second proof of Theorem 8.11, quite different from
Euclid's. Historically, Fermat conjectured that every $F_n$ is prime; this fails at $n = 5$, where
$F_5 = 4{,}294{,}967{,}297 = 641 \cdot 6{,}700{,}417$.

