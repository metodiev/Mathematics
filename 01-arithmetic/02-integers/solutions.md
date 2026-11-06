# Integers and Negative Numbers — Solutions

> Companion to [the exercises](exercises.md) and [the tutorial](README.md). Each solution states the
> strategy first, then every step. Numbers match the exercise numbers.

## Beginner

**1.** *Strategy: sort by sign first — negatives, then zero, then positives.*

Negatives, ordered by decreasing absolute value: $-7 < -3 < -1$ (since $7 > 3 > 1$). Then $0$, then
the positives $2 < 5$. Hence

$$
-7 < -3 < -1 < 0 < 2 < 5.
$$

Absolute values: $|-3| = 3$, $|5| = 5$, $|-7| = 7$, $|0| = 0$, $|2| = 2$, $|-1| = 1$. These six
numbers are all different, so **no two listed integers have the same absolute value**.

*Pitfall:* reading $-7$ as "bigger" than $-3$ because $7 > 3$. Position on the line decides order.

**2.** Apply Definition 5.4: for a negative argument, $|a| = -a$.

(a) $|-8| = 8$.
(b) $|12| = 12$.
(c) $|0| = 0$; note that an absolute value may be zero.
(d) $-|-5| = -(5) = -5$: the outer minus is applied after the absolute value.
(e) $|-5| + |3| = 5 + 3 = 8$.

**3.** The distance is $|a - b|$ (Section 7.2).

(a) $|7 - (-4)| = |7 + 4| = 11$.
(b) $|-2 - (-9)| = |-2 + 9| = 7$.
(c) $|6 - 6| = 0$: a point is at distance zero from itself.

**4.** *Strategy: same signs add the sizes and keep the sign; opposite signs subtract the sizes and
take the sign of the larger absolute value.*

(a) $-7 + 3$: opposite signs, $7 - 3 = 4$, sign of $-7$, so $-4$.
(b) $-5 + (-9)$: same sign, $5 + 9 = 14$, keep $-$, so $-14$.
(c) $8 + (-14)$: opposite signs, $14 - 8 = 6$, sign of $-14$, so $-6$.
(d) $-6 + 6 = 0$: opposites.

**5.** *Strategy: rewrite each subtraction as addition of the opposite.*

(a) $4 - 9 = 4 + (-9) = -5$.
(b) $-3 - 7 = -3 + (-7) = -10$.
(c) $-5 - (-8) = -5 + 8 = 3$: subtracting a negative adds.
(d) $2 - (-6) = 2 + 6 = 8$.

*Pitfall:* in (c) and (d), two minus signs in a row do not "make a minus".

**6.** *Strategy: compute the magnitude by ordinary multiplication or division, then attach the sign
by the rule "same signs positive, different signs negative".*

(a) $(-6)(7) = -(6 \cdot 7) = -42$.
(b) $(-4)(-9) = +(4 \cdot 9) = 36$.
(c) $8 \div (-2) = -4$, because $(-2)(-4) = 8$.
(d) $-45 \div (-5) = 9$, because $(-5)(9) = -45$.

**7.** *Strategy: powers first, and check whether the minus sign is inside or outside the
parentheses.*

(a) $(-2)^5 = -(2^5) = -32$: five factors, odd, so negative.
(b) $(-3)^3 = -(3^3) = -27$.
(c) $(-1)^{100} = 1$: $100$ is even, so the factors pair up into $+1$s.
(d) $-5^2 = -(5^2) = -25$: exponentiation binds more tightly than unary minus.
(e) $(-5)^2 = 25$.

*Pitfall:* (d) and (e) differ. Always parenthesize a negative base.

**8.** Multiplication and division come before addition and subtraction.

(a) $6 - 3 \cdot 4 = 6 - 12 = -6$.
(b) $-2 + 4 \cdot (-3) = -2 + (-12) = -14$.
(c) $20 \div (-4) + 3 = -5 + 3 = -2$.

**9.** *Strategy: innermost parentheses first; the leading minus acts on the whole bracket.*

(a) $2 - (3 - 8) = 2 - (-5) = 2 + 5 = 7$.
(b) $-(4 - 9) + 2 = -(-5) + 2 = 5 + 2 = 7$.

*Pitfall:* $-(4-9)$ is $+5$, not $-4-9$ or $-4+9$.

**10.** A drop of $10$ °C is a contribution of $-10$; a rise of $13$ °C is $+13$.

$$
3 - 10 = -7 \ \text{°C}, \qquad -8 + 13 = 5 \ \text{°C}.
$$

**11.** Withdrawal is negative:

$$
45 - 80 = -35.
$$

The balance is $-\$35$: the account is overdrawn — it owes \$35 more than it holds.

**12.** Rising means adding, descending means subtracting.

Diver: $-18 + 7 = -11$, so $11$ m below the surface.
Hiker: $1200 - 1500 = -300$, so $300$ m **below** sea level (not above). The sign flip is the whole
point of the exercise: the hiker walked down past sea level.

## Intermediate

**13.** *Strategy: addition only, then group positives and negatives separately.*

$$
-3 + 7 - 5 + 2 - 8 = (-3) + 7 + (-5) + 2 + (-8).
$$

Positives: $7 + 2 = 9$. Negatives: $-(3 + 5 + 8) = -16$. Total: $9 - 16 = -7$.

*Alternative:* $(-3+7) = 4$, $4 - 5 = -1$, $-1 + 2 = 1$, $1 - 8 = -7$. Both routes agree.

**14.** Exponents first, then the product, then the subtraction of a negative.

$$
(-2)^3 = -8, \qquad (-3)^2 = 9, \qquad (-8)\cdot 9 = -72,
$$
$$
-72 - (-4) = -72 + 4 = -68.
$$

**15.** Numerator and denominator of each fraction are grouped by the fraction bar, so each is
computed before the division.

$$
\dfrac{(-6)(-4)}{-3} = \dfrac{24}{-3} = -8, \qquad \dfrac{18}{-6} = -3,
$$
$$
-8 + (-3) = -11.
$$

**16.**

$$
7 - 12 = -5, \qquad (-5)^2 = 25, \qquad 3(-5) = -15,
$$
$$
\dfrac{-15}{-3} = 5, \qquad 25 - 5 = 20.
$$

*Pitfall:* computing $3(7-12) \div (-3)$ as $3 \cdot \bigl((7-12)\div(-3)\bigr)$ gives the same value
here because multiplication and division associate in this case, but the safe order is left to
right: the product $3(-5)$ is formed first.

**17.** *Strategy: handle the two terms independently, then add.*

First term: $2 - 6 = -4$, so $(-4)^2 = 16$ and the leading minus gives $-16$.

Second term: $(-3)^3 = -27$, and $-27 \div 9 = -3$.

Total: $-16 + (-3) = -19$.

**18.** Substitute with parentheses around each negative value.

$$
a^2b = (-2)^2 \cdot 6 = 4 \cdot 6 = 24, \qquad ab^2 = (-2)\cdot 6^2 = (-2)\cdot 36 = -72.
$$
$$
a^2b - ab^2 = 24 - (-72) = 96.
$$

Check by factoring: $a^2b - ab^2 = ab(a - b) = (-2)(6)(-2 - 6) = (-12)(-8) = 96$. Both routes agree.

**19.** *Strategy: use P10, which says that multiplying an inequality by a negative number reverses
it.*

Since $11 < 12$ and $-7 < 0$,

$$
-7 \cdot 11 > -7 \cdot 12.
$$

Numerically, $-77 > -84$, which is consistent: $-77$ lies to the right of $-84$.

*Pitfall:* "multiplying makes numbers bigger" is false for negative multipliers.

**20.** *Strategy: choose the largest multiple of $6$ that does not exceed $-47$.*

Multiples: $\dots, (-7)\cdot 6 = -42$, $(-8)\cdot 6 = -48$. Since $-48 \le -47 < -42$, take $q = -8$.
Then

$$
r = -47 - 6(-8) = -47 + 48 = 1, \qquad 0 \le 1 < 6.
$$

So $q = -8$, $r = 1$, and indeed $6(-8) + 1 = -47$.

C truncates toward zero. Since $-47$ lies strictly between $-48 = 6(-8)$ and $-42 = 6(-7)$, the exact
quotient $-47/6$ lies between $-8$ and $-7$, so truncation toward zero gives $-7$. The remainder is
$-47 - 6(-7) = -47 + 42 = -5$. So `-47 / 6` is `-7` and `-47 % 6` is `-5`. Both pairs
satisfy $6q + r = -47$; they differ in which remainder is reported.

**21.** *Strategy: each step down in $n$ adds $5$, because removing one copy of $-5$ is the same as
adding $5$.*

| $n$ | $4$ | $3$ | $2$ | $1$ | $0$ | $-1$ | $-2$ | $-3$ |
|---|---|---|---|---|---|---|---|---|
| $n \cdot (-5)$ | $-20$ | $-15$ | $-10$ | $-5$ | $0$ | $5$ | $10$ | $15$ |

Rule: $(-a)(-5) = 5a$; more generally the product of two negative integers is positive (P5).

The pattern cannot continue otherwise, because the step from $n$ to $n-1$ is forced by
distributivity:

$$
(n-1)(-5) = n(-5) + (-1)(-5) = n(-5) + 5.
$$

So consecutive entries necessarily differ by exactly $5$, and $(-1)(-5)$ is determined by the entry
at $n = 0$, which is $0$.

**22.** (a) **False.** Take $a = -4$; then $-a = 4 > 0$. The symbol $-a$ means "the opposite of $a$",
which is negative only when $a$ is positive.

(b) **True.** If $a \ge 0$ then $-a \le 0$, so $|-a| = -(-a) = a = |a|$. If $a < 0$ then $-a > 0$, so
$|-a| = -a = |a|$. Both cases agree.

(c) **False.** Take $a = -5$, $b = 2$: then $a < b$ but $a^2 = 25 > 4 = b^2$. Squaring preserves
order only on non-negative numbers.

(d) **False.** Take $a = -3$, $b = 5$: $|a+b| = |2| = 2$, while $|a| + |b| = 8$. The correct general
statement is $|a+b| \le |a|+|b|$, with equality when $ab \ge 0$.

**23.** Descending $35$ m changes the depth by $-35$; rising at $12$ m/min for $5$ min changes it by
$+60$.

$$
-120 - 35 + 60 = -155 + 60 = -95.
$$

The submarine is at $-95$ m, that is $95$ m below the surface. Note that "descends" and "rises" carry
their own signs; attaching them correctly is the whole problem.

**24.** Debits are negative, the deposit positive:

$$
250 - 90 - 90 - 150 + 60 = 250 - 330 + 60 = -20.
$$

The balance is $-\$20$, i.e. overdrawn by \$20. The fee is another debit:

$$
-20 - 35 = -55.
$$

Final balance $-\$55$.

*Pitfall:* stopping at "$\$250 - \$330$" and dropping the deposit.

## Advanced

**25.** *Strategy: mimic the proof of P1, and use Lemma 8.1 to turn "$x + x = x$" into "$x = 0$".*

Let $a$ be any integer. By (Z4), $0 + 0 = 0$, so

$$
0 \cdot a = (0 + 0)\cdot a.
$$

By distributivity (Z6), applied to the right factor after using commutativity (Z3),

$$
(0 + 0)\cdot a = 0 \cdot a + 0 \cdot a.
$$

Hence $0 \cdot a = 0 \cdot a + 0 \cdot a$. By (Z5) the element $-(0\cdot a)$ exists; adding it to
both sides and using associativity (Z2):

$$
0 = (0\cdot a + 0\cdot a) + \bigl(-(0\cdot a)\bigr) = 0\cdot a + \bigl(0\cdot a + -(0\cdot a)\bigr) = 0\cdot a + 0 = 0\cdot a.
$$

Therefore $0 \cdot a = 0$. $\blacksquare$

Axioms used: (Z3) commutativity, (Z4) identity, (Z6) distributivity, (Z5) inverses, (Z2)
associativity. No ordering axiom is needed.

**26.** *Strategy: show that $ab + (-a)b = 0$ and quote uniqueness of the additive inverse
(Lemma 8.1).*

Compute

$$
ab + (-a)b = \bigl(a + (-a)\bigr)b = 0 \cdot b = 0,
$$

using distributivity (Z6), the inverse axiom (Z5), and P1 ($0 \cdot b = 0$). By Lemma 8.1, the
element $(-a)b$ is the additive inverse of $ab$:

$$
(-a)b = -(ab).
$$

For the second claim, apply the first with $b$ replaced by $-b$:

$$
(-a)(-b) = -\bigl(a(-b)\bigr).
$$

By the first claim with the roles of the factors exchanged (commutativity), $a(-b) = -(ab)$. Hence

$$
(-a)(-b) = -\bigl(-(ab)\bigr) = ab,
$$

using P3, $-(-x) = x$. $\blacksquare$

**27.** *Strategy: evaluate the product $(-1)\bigl((-1)+1\bigr)$ in two ways — once using
$(-1)+1 = 0$, once using distributivity — and equate the results.*

Since $(-1) + 1 = 0$ by (Z5),

$$
(-1)\bigl((-1) + 1\bigr) = (-1)\cdot 0 = 0
$$

by P1. On the other hand, distributivity (Z6) gives

$$
(-1)\bigl((-1) + 1\bigr) = (-1)(-1) + (-1)\cdot 1 = (-1)(-1) + (-1),
$$

because $(-1)\cdot 1 = -1$ by (Z4). Equating the two evaluations,

$$
(-1)(-1) + (-1) = 0.
$$

By Lemma 8.1 (with $a = -1$, $b = (-1)(-1)$), $(-1)(-1)$ is the additive inverse of $-1$:

$$
(-1)(-1) = -(-1) = 1,
$$

using P3. $\blacksquare$

If instead we assumed $(-1)(-1) = -1$, then the same expression would evaluate to
$-1 + (-1) = -2$, while the other route gives $0$. The assumption contradicts distributivity, so no
number system with distributivity can have $(-1)(-1) = -1$. One of the two laws would have to be
abandoned, and it is distributivity that makes algebra possible.

**28.** (a) Let $n$ be odd, so $n = 2k + 1$ for some integer $k$. Then

$$
n^2 = (2k+1)^2 = 4k^2 + 4k + 1 = 2(2k^2 + 2k) + 1.
$$

Since $2k^2 + 2k$ is an integer, $n^2$ is odd. $\blacksquare$

(b) *Strategy: factor.* For every integer $n$,

$$
n^2 + n = n(n+1).
$$

If $n$ is even, the first factor is even, so the product is even. If $n$ is odd, then $n+1$ is even,
so the product is even. These two cases exhaust all integers, hence $n(n+1)$ is even in every case.
$\blacksquare$

*Alternative:* $n^2$ has the same parity as $n$, and even $+$ even $=$ even, odd $+$ odd $=$ even.
Both arguments are valid; the factorization is shorter.

**29.** (a) *Strategy: four cases on the signs.*

Let $a, b$ be integers.

* $a \ge 0$, $b \ge 0$: then $ab \ge 0$, so $|ab| = ab = |a||b|$.
* $a \ge 0$, $b < 0$: then $ab \le 0$, so $|ab| = -ab = a(-b) = |a||b|$.
* $a < 0$, $b \ge 0$: symmetric to the previous case.
* $a < 0$, $b < 0$: then $ab > 0$ by P5, so $|ab| = ab = (-a)(-b) = |a||b|$.

All cases agree. $\blacksquare$

(b) *Strategy: reduce to a product with a negative factor and use the definition of order.*

From $c < 0$ and (Z8) applied to $c + (-c) < 0 + (-c)$, we get $0 < -c$. Since $a < b$ and $-c > 0$,
axiom (Z8) gives

$$
a(-c) < b(-c), \qquad \text{i.e.} \qquad -ac < -bc.
$$

Adding $ac + bc$ to both sides (order is preserved by addition):

$$
bc < ac, \qquad \text{i.e.} \qquad ac > bc.
$$

$\blacksquare$

*Pitfall:* the conclusion reverses the inequality. Checking with numbers: $-2 < 5$ and $c = -3$ give
$6 > -15$.

**30.** *Strategy: squeeze $a+b$ between $-(|a|+|b|)$ and $|a|+|b|$, then translate.*

For any integer $x$, $-|x| \le x \le |x|$. Applying this to $a$ and to $b$ gives four inequalities,
and adding them pairwise (valid by (Z8), since addition preserves order) yields

$$
-|a| - |b| \le a + b \le |a| + |b|,
$$

that is

$$
-\bigl(|a| + |b|\bigr) \le a + b \le |a| + |b|.
$$

For $c \ge 0$, the pair of inequalities $-c \le x \le c$ is equivalent to $|x| \le c$: if $x \ge 0$,
the right inequality is the claim; if $x < 0$, the left one is. Taking $x = a+b$ and
$c = |a|+|b|$ gives $|a+b| \le |a|+|b|$. $\blacksquare$

*Equality.* Equality requires $a = |a|$ or $a = -|a|$ simultaneously with $b = |b|$ or $b = -|b|$ in
the same direction, that is $a$ and $b$ have the same sign, or one of them is zero. In that case
$|a+b| = |a|+|b|$; when the signs are opposite and both nonzero, the inequality is strict. For
example $|3 + 4| = 7 = |3|+|4|$, while $|{-3} + 4| = 1 < 7$.

**31.** (a) Let the integers be $n$ and $n+1$. If $n$ is even then $n = 2k$ and the product is
$2k(n+1)$, even. If $n$ is odd then $n+1$ is even, say $n+1 = 2k$, and the product is $2kn$, even.
The two cases exhaust all integers. $\blacksquare$

(b) *Strategy: prove divisibility by $2$ and by $3$ separately, then combine.*

Let $P = n(n+1)(n+2)$.

*Divisibility by $2$:* by part (a), $n(n+1)$ is even, and multiplying an even number by $n+2$ keeps
it even. So $2 \mid P$.

*Divisibility by $3$:* write $n = 3k$, $n = 3k+1$ or $n = 3k+2$ — these exhaust all integers, since
the remainder on division by $3$ is $0$, $1$ or $2$.
* If $n = 3k$, then $3 \mid n$, hence $3 \mid P$.
* If $n = 3k+1$, then $n + 2 = 3k + 3 = 3(k+1)$, so $3 \mid n+2$, hence $3 \mid P$.
* If $n = 3k+2$, then $n + 1 = 3k + 3 = 3(k+1)$, so $3 \mid n+1$, hence $3 \mid P$.

In every case $3 \mid P$.

*Combining:* since $P = 3m$ for some integer $m$ and $P$ is even, $3m$ is even; as $3$ is odd, $m$
must be even, $m = 2c$. Then $P = 3 \cdot 2c = 6c$, so $6 \mid P$. $\blacksquare$

*Check:* $4 \cdot 5 \cdot 6 = 120 = 6 \cdot 20$; $7 \cdot 8 \cdot 9 = 504 = 6 \cdot 84$;
$1 \cdot 2 \cdot 3 = 6$.

**32.** The range is $-128 \le x \le 127$; a result outside the range is reduced modulo $256$ and
then reinterpreted.

(a) $100 + 50 = 150 > 127$. Subtract $256$: $150 - 256 = -106$.

(b) $-120 - 20 = -140 < -128$. Add $256$: $-140 + 256 = 116$.

(c) $127$ is stored as `01111111`. Adding $1$ produces `10000000`, which is the pattern for $-128$:
the leading bit is $1$, so the value is $128 - 256 = -128$. In arithmetic terms, $127 + 1 = 128$,
which lies outside the range, so it is reduced to $128 - 256 = -128$.

(d) $-128$ is stored as `10000000`. Negating means taking the two's complement, which for this pattern
returns `10000000` again. The reason is that the true answer $+128$ is not representable: the
representable values stop at $127$. So the machine reports $-128$, the "wrap-around" value. In C,
negating the most negative value of a signed type is undefined behaviour, precisely because no
correct result exists.

## Challenge

**33.** *Strategy: suppose a solution exists, show that both $a$ and $b$ are even, divide by $2$, and
repeat. The repetition cannot terminate, which contradicts the well-ordering of the positive
integers.*

Suppose, for contradiction, that $a^2 = 2b^2$ with $b \neq 0$.

*Step 1: $a$ is even.* Since $a^2 = 2b^2$, the number $a^2$ is even. If $a$ were odd, then by
Exercise 28(a) $a^2$ would be odd. Hence $a$ is even; write $a = 2c$ with $c$ an integer.

*Step 2: $b$ is even.* Substituting, $4c^2 = 2b^2$, so $b^2 = 2c^2$. Thus $b^2$ is even, and by the
same parity argument $b$ is even; write $b = 2d$ with $d$ an integer.

*Step 3: a smaller solution.* Substituting $b = 2d$ into $b^2 = 2c^2$ gives $4d^2 = 2c^2$, that is

$$
c^2 = 2d^2.
$$

So $(c, d)$ is another integer solution, and $0 < |d| = |b|/2 < |b|$ because $b \neq 0$.

*Step 4: descent.* Repeating Steps 1–3 produces a sequence of positive integers
$|b| > |d| > |d'| > \cdots$, each a positive integer. An infinite strictly decreasing sequence of
positive integers cannot exist, since the positive integers are well ordered: any nonempty set of
them has a least element, so the descent must stop, contradicting the fact that each step produces a
smaller positive second coordinate.

Therefore no such pair $(a,b)$ with $b \neq 0$ exists. $\blacksquare$

*Remark.* If $b = 0$, the equation forces $a = 0$, which is why the statement excludes the trivial
zero solution. The same argument, phrased with fractions, proves that $\sqrt{2}$ is not rational:
a rational solution would give integers $a, b$ with $b \neq 0$ and $a^2 = 2b^2$.

**34.** *Strategy: factor the difference of squares and analyse the factor pairs.*

$$
a^2 - b^2 = (a-b)(a+b) = 12.
$$

Put $u = a - b$ and $v = a + b$. Then $uv = 12$, and

$$
u + v = 2a
$$

is even. If $u$ and $v$ were of opposite parity, their sum would be odd, so $u$ and $v$ have the same
parity. Since $uv = 12$ is even, they cannot both be odd; hence **both are even**.

The factor pairs of $12$ with both factors even are

$$
(2, 6), \quad (6, 2), \quad (-2, -6), \quad (-6, -2).
$$

(The pairs $(1,12)$, $(3,4)$, $(12,1)$, $(4,3)$ and their negatives are excluded because the factors
have different parity and would give $a = (u+v)/2$ non-integral.)

Solving $a = (u+v)/2$, $b = (v-u)/2$:

| $(u,v)$ | $a$ | $b$ |
|---|---|---|
| $(2,6)$ | $4$ | $2$ |
| $(6,2)$ | $4$ | $-2$ |
| $(-2,-6)$ | $-4$ | $-2$ |
| $(-6,-2)$ | $-4$ | $2$ |

Verification: $4^2 - 2^2 = 16 - 4 = 12$; $4^2 - (-2)^2 = 12$; $(-4)^2 - (-2)^2 = 12$;
$(-4)^2 - 2^2 = 12$. All four pairs work, and the analysis shows there are no others.

**35.** *Strategy: pigeonhole on the four possible remainders.*

By division with remainder, every integer $a$ can be written uniquely as

$$
a = 4q + r, \qquad r \in \{0, 1, 2, 3\}.
$$

Given five integers $a_1, \dots, a_5$, each has one of the four possible remainders. Five objects in
four classes force two of them into the same class: there exist $i \neq j$ with $r_i = r_j = r$.

Then

$$
a_i - a_j = (4q_i + r) - (4q_j + r) = 4(q_i - q_j),
$$

which is divisible by $4$. $\blacksquare$

*The requested example for modulus $5$:* take $0, 1, 2, 3, 4$. The differences between distinct
members are $1, 2, 3$ or $4$ in absolute value, none of which is a multiple of $5$. So five integers
are not enough to force a multiple of $5$; six are, by the same pigeonhole argument.
