# Fractions — Solutions

> Companion to [the exercises](exercises.md) and [the tutorial](README.md). Each solution gives the
> strategy, every step, and the pitfall the problem is designed to expose.

## Beginner

**1.** *Strategy: count equal parts, then simplify.*

(a) The bar has $12$ equal squares, of which $9$ are gone: $\frac{9}{12}$. Divide numerator and
denominator by $\gcd(9,12) = 3$:

$$
\dfrac{9}{12} = \dfrac{3}{4}.
$$

(b) $5$ of $8$ equal parts is $\frac{5}{8}$, already in lowest terms since $\gcd(5,8) = 1$.

**2.** *Strategy: multiply numerator and denominator by the same factor.*

(a) $24 \div 4 = 6$, so $\frac{3}{4} = \frac{3\cdot 6}{4\cdot 6} = \frac{18}{24}$.
(b) $24 \div 6 = 4$, so $\frac{5}{6} = \frac{20}{24}$.
(c) $24 \div 8 = 3$, so $\frac{7}{8} = \frac{21}{24}$.

Check: $18/24 = 3/4$ after dividing both terms by $6$, and similarly $20/24 = 5/6$ and $21/24 = 7/8$.
The order $18 < 20 < 21$ reflects $\frac34 < \frac56 < \frac78$.

**3.** (a) $\gcd(12,18) = 6$, so $\frac{12}{18} = \frac{2}{3}$.
(b) $\gcd(25,40) = 5$, so $\frac{25}{40} = \frac{5}{8}$.
(c) $\gcd(36,60) = 12$, so $\frac{36}{60} = \frac{3}{5}$.
(d) $\gcd(17,51) = 17$, so $\frac{17}{51} = \frac{1}{3}$.

*Pitfall:* dividing only the numerator, or dividing by a common factor that is not the greatest,
leaves a fraction that is correct but not in lowest terms.

**4.** *Strategy: rewrite over the least common denominator and compare numerators (P8).*

(a) $\operatorname{lcm}(5,8) = 40$:

$$
\dfrac{3}{5} = \dfrac{24}{40}, \qquad \dfrac{5}{8} = \dfrac{25}{40}, \qquad \text{so } \dfrac{3}{5} < \dfrac{5}{8}.
$$

Cross-check: $3 \cdot 8 = 24 < 25 = 5 \cdot 5$.

(b) $\operatorname{lcm}(12,7) = 84$:

$$
\dfrac{7}{12} = \dfrac{49}{84}, \qquad \dfrac{4}{7} = \dfrac{48}{84}, \qquad \text{so } \dfrac{7}{12} > \dfrac{4}{7}.
$$

Cross-check: $7 \cdot 7 = 49 > 48 = 4 \cdot 12$.

**5.** (a) $2\frac{3}{8} = \frac{2 \cdot 8 + 3}{8} = \frac{19}{8}$.
(b) Divide: $19 = 3 \cdot 6 + 1$, so $\frac{19}{6} = 3\frac{1}{6}$.

*Check:* $3\frac{1}{6} = \frac{18+1}{6} = \frac{19}{6}$.

**6.** *Strategy: equal denominators, so add or subtract the numerators only.*

(a) $\frac{3}{8} + \frac{1}{8} = \frac{4}{8} = \frac{1}{2}$.
(b) $\frac{5}{6} - \frac{1}{6} = \frac{4}{6} = \frac{2}{3}$.
(c) $\frac{7}{9} + \frac{2}{9} = \frac{9}{9} = 1$.

*Pitfall:* never add the denominators; $\frac{3}{8} + \frac{1}{8}$ is not $\frac{4}{16}$.

**7.** *Strategy: find the least common denominator.*

(a) $\frac{1}{2} = \frac{2}{4}$, so $\frac{2}{4} + \frac{1}{4} = \frac{3}{4}$.
(b) $\operatorname{lcm}(3,6) = 6$: $\frac{2}{3} = \frac{4}{6}$, so $\frac{4}{6} + \frac{1}{6} = \frac{5}{6}$.
(c) $\operatorname{lcm}(4,3) = 12$: $\frac{3}{4} = \frac{9}{12}$ and $\frac{1}{3} = \frac{4}{12}$, so
$\frac{9}{12} - \frac{4}{12} = \frac{5}{12}$.

**8.** *Strategy: multiply numerators and denominators, cancelling common factors first.*

(a) $\frac{2}{3}\cdot\frac{3}{5} = \frac{6}{15} = \frac{2}{5}$. Cancelling the $3$ first gives
$\frac{2}{1}\cdot\frac{1}{5} = \frac{2}{5}$.
(b) $\frac{4}{7}\cdot\frac{7}{8} = \frac{28}{56} = \frac{1}{2}$; cancelling gives
$\frac{4}{1}\cdot\frac{1}{8} = \frac{4}{8} = \frac{1}{2}$.
(c) $\frac{5}{6}\cdot 12 = \frac{5 \cdot 12}{6} = \frac{60}{6} = 10$. Note that multiplying by $12$
makes the result larger, as it should.

**9.** *Strategy: multiply by the reciprocal of the divisor.*

(a) $\frac{3}{4} \div \frac{1}{2} = \frac{3}{4}\cdot\frac{2}{1} = \frac{6}{4} = \frac{3}{2} = 1\frac{1}{2}$.
Sanity check: there are two quarters in a half, so dividing by one half doubles.
(b) $\frac{2}{5} \div \frac{3}{7} = \frac{2}{5}\cdot\frac{7}{3} = \frac{14}{15}$.
(c) $6 \div \frac{2}{3} = \frac{6}{1}\cdot\frac{3}{2} = \frac{18}{2} = 9$. Sanity check: six contains
nine thirds-of-a-unit portions measured in two-thirds units, since $6 = 9 \cdot \frac{2}{3}$.

**10.** *Strategy: the numerators are equal, so compare the sizes of the pieces.*

Both fractions count $5$ pieces. Sevenths are larger pieces than ninths, so

$$
\dfrac{5}{7} > \dfrac{5}{9}.
$$

Cross-multiplication confirms it: $5 \cdot 9 = 45 > 35 = 5 \cdot 7$, and for positive denominators
$a/b > c/d$ exactly when $ad > bc$.

*Pitfall:* the larger denominator makes the fraction smaller when numerators agree.

**11.** $\frac{9}{24}$, and $\gcd(9,24) = 3$, so

$$
\dfrac{9}{24} = \dfrac{3}{8}.
$$

Three eighths of the class wears glasses.

**12.** *Strategy: addition over the least common denominator.*

$\operatorname{lcm}(4,3) = 12$:

$$
\dfrac{3}{4} + \dfrac{2}{3} = \dfrac{9}{12} + \dfrac{8}{12} = \dfrac{17}{12}.
$$

Since $17 = 1 \cdot 12 + 5$, the answer is $1\frac{5}{12}$ cups.

*Check:* the total must exceed $1$ cup, and $\frac{17}{12} = 1\frac{5}{12}$ lies strictly between $1$
and $2$, as a sum of two proper fractions larger than $\frac{1}{2}$ should.

**13.** Sharing $5$ among $4$ is the quotient $\frac{5}{4}$:

$$
\dfrac{5}{4} = 1\dfrac{1}{4}.
$$

Each person receives $1\frac{1}{4}$ pizzas. Equivalently, give everyone one pizza and share the
remaining one into quarters; each gets one extra quarter.

## Intermediate

**14.** *Strategy: run the Euclidean algorithm, then divide both terms by the gcd.*

$$
147 = 1\cdot 105 + 42, \qquad 105 = 2\cdot 42 + 21, \qquad 42 = 2 \cdot 21 + 0.
$$

The last nonzero remainder is $21$, so $\gcd(105,147) = 21$. Then

$$
\dfrac{105}{147} = \dfrac{105/21}{147/21} = \dfrac{5}{7}.
$$

*Check:* $21 \cdot 5 = 105$ and $21 \cdot 7 = 147$.

**15.**

$$
1071 = 2 \cdot 462 + 147, \qquad 462 = 3 \cdot 147 + 21, \qquad 147 = 7 \cdot 21 + 0.
$$

So $\gcd(1071,462) = 21$. Dividing,

$$
\dfrac{462}{1071} = \dfrac{22}{51}.
$$

Since $22 = 2 \cdot 11$ and $51 = 3 \cdot 17$, the result is in lowest terms.

**16.** *Strategy: convert to improper fractions, then use the least common denominator.*

$$
3\tfrac{1}{4} = \dfrac{13}{4}, \qquad 2\tfrac{5}{6} = \dfrac{17}{6}, \qquad \operatorname{lcm}(4,6) = 12.
$$
$$
\dfrac{13}{4} + \dfrac{17}{6} = \dfrac{39}{12} + \dfrac{34}{12} = \dfrac{73}{12}.
$$

Since $73 = 6 \cdot 12 + 1$, the answer is $6\frac{1}{12}$.

*Pitfall:* adding the whole parts and the fractional parts separately gives
$5 + \frac{1}{4} + \frac{5}{6} = 5 + \frac{13}{12} = 6\frac{1}{12}$, which is correct here — but only
because the fractional sum was carried properly. Skipping the carry gives the wrong
$5\frac{13}{12}$.

**17.** *Strategy: improper fractions; borrow if necessary.*

$$
5\tfrac{1}{3} = \dfrac{16}{3}, \qquad 2\tfrac{3}{4} = \dfrac{11}{4}, \qquad \operatorname{lcm}(3,4) = 12.
$$
$$
\dfrac{16}{3} - \dfrac{11}{4} = \dfrac{64}{12} - \dfrac{33}{12} = \dfrac{31}{12} = 2\tfrac{7}{12}.
$$

*Check:* add the answer back to the subtrahend:
$\frac{31}{12} + \frac{11}{4} = \frac{31}{12} + \frac{33}{12} = \frac{64}{12} = \frac{16}{3} = 5\frac{1}{3}$,
which is the minuend.

**18.** *Strategy: multiply, cancelling aggressively.*

$$
\dfrac{2}{3}\cdot\dfrac{9}{10}\cdot\dfrac{5}{6} = \dfrac{2 \cdot 9 \cdot 5}{3 \cdot 10 \cdot 6} = \dfrac{90}{180} = \dfrac{1}{2}.
$$

With cancellation: $9/3 = 3$, $5/10 = 1/2$, so the product is
$\frac{2 \cdot 3}{6}\cdot\frac{1}{2} = \frac{6}{6}\cdot\frac{1}{2} = \frac{1}{2}$.

**19.** *Strategy: invert the divisor.*

$$
\dfrac{3}{8} \div \dfrac{9}{16} = \dfrac{3}{8}\cdot\dfrac{16}{9} = \dfrac{48}{72} = \dfrac{2}{3}.
$$

*Check:* $\frac{9}{16}\cdot\frac{2}{3} = \frac{18}{48} = \frac{3}{8}$, which is the dividend.

**20.** *Strategy: evaluate both parentheses, then divide.*

$$
\dfrac{1}{2} + \dfrac{1}{3} = \dfrac{3}{6} + \dfrac{2}{6} = \dfrac{5}{6}, \qquad
\dfrac{1}{2} - \dfrac{1}{3} = \dfrac{3}{6} - \dfrac{2}{6} = \dfrac{1}{6}.
$$
$$
\dfrac{5}{6} \div \dfrac{1}{6} = \dfrac{5}{6}\cdot\dfrac{6}{1} = 5.
$$

*Check:* $\frac{1}{6} \cdot 5 = \frac{5}{6}$.

**21.**

$$
\dfrac{2}{5} + \dfrac{1}{4} = \dfrac{8}{20} + \dfrac{5}{20} = \dfrac{13}{20}, \qquad
1 - \dfrac{13}{20} = \dfrac{20}{20} - \dfrac{13}{20} = \dfrac{7}{20}.
$$

**22.** *Strategy: common denominator $12$, then compare numerators.*

$$
\dfrac{3}{4} = \dfrac{9}{12}, \quad \dfrac{2}{3} = \dfrac{8}{12}, \quad \dfrac{7}{12} = \dfrac{7}{12}, \quad \dfrac{5}{6} = \dfrac{10}{12}.
$$

Hence

$$
\dfrac{7}{12} < \dfrac{2}{3} < \dfrac{3}{4} < \dfrac{5}{6}.
$$

*Check:* the numerators $7 < 8 < 9 < 10$ are in increasing order over the common denominator $12$, so
the ordering is correct.

**23.** *Strategy: the scaling factor is the ratio of the yields.*

$$
\text{factor} = \dfrac{10}{6} = \dfrac{5}{3}, \qquad 1\tfrac{1}{2}\cdot\dfrac{5}{3} = \dfrac{3}{2}\cdot\dfrac{5}{3} = \dfrac{15}{6} = \dfrac{5}{2} = 2\tfrac{1}{2}.
$$

Two and a half cups are needed. *Check:* dividing the new amount by the old scaling factor,
$\frac{5}{2} \div \frac{3}{2} = \frac{5}{3}$, recovers the ratio of the yields $\frac{10}{6} = \frac{5}{3}$.

**24.** $\frac{3}{4}$ of $32$ is $\frac{3}{4}\cdot 32 = \frac{96}{4} = 24$ students walking. The
remaining fraction is $1 - \frac{3}{4} = \frac{1}{4}$, and $\frac{1}{4}\cdot 32 = 8$ students do not
walk. Check: $24 + 8 = 32$.

**25.** *Strategy: "how many one-sixths fit into two thirds" is a division.*

$$
\dfrac{2}{3} \div \dfrac{1}{6} = \dfrac{2}{3}\cdot\dfrac{6}{1} = \dfrac{12}{3} = 4.
$$

It takes $4$ minutes. *Check:* in $4$ minutes the pipe delivers $4 \cdot \frac{1}{6} = \frac{4}{6} = \frac{2}{3}$ of the tank.

## Advanced

**26.** *Strategy: apply Definition 5.3, which reduces equality of fractions to a cross-product
identity in $\mathbb{Z}$.*

By Definition 5.3, $\frac{a}{b} = \frac{ak}{bk}$ holds exactly when

$$
a \cdot (bk) = (ak)\cdot b.
$$

Both sides equal $abk$: the left by associativity, the right by associativity and commutativity.
Since the cross-products agree and $b \neq 0$, $bk \neq 0$ (no zero divisors), the fractions are
equal. $\blacksquare$

*Remark:* if $k = 0$ the symbol $\frac{ak}{bk}$ has denominator $0$ and is not a fraction at all,
which is why the hypothesis $k \neq 0$ is part of the statement.

**27.** *Strategy: subtract and show each difference is positive, using P8 to convert the hypothesis
into an inequality between integers.*

Since $\frac{a}{b} < \frac{c}{d}$ and $b, d > 0$, P8 gives $ad < bc$, equivalently $bc - ad > 0$.

*First inequality.* Put the difference over the common denominator $b(b+d)$:

$$
\dfrac{a+c}{b+d} - \dfrac{a}{b} = \dfrac{b(a+c) - a(b+d)}{b(b+d)} = \dfrac{ab + bc - ab - ad}{b(b+d)} = \dfrac{bc - ad}{b(b+d)}.
$$

The numerator is positive and the denominator $b(b+d)$ is positive, so the difference is positive:
$\frac{a}{b} < \frac{a+c}{b+d}$.

*Second inequality.*

$$
\dfrac{c}{d} - \dfrac{a+c}{b+d} = \dfrac{c(b+d) - d(a+c)}{d(b+d)} = \dfrac{bc + cd - ad - cd}{d(b+d)} = \dfrac{bc - ad}{d(b+d)} > 0.
$$

Hence $\frac{a+c}{b+d} < \frac{c}{d}$. Combining the two gives the claim. $\blacksquare$

*Example:* $\frac{1}{2} < \frac{2}{3}$ and the mediant is $\frac{3}{5}$, with
$\frac{1}{2} = \frac{5}{10} < \frac{6}{10} = \frac{3}{5} < \frac{8}{12} = \frac{2}{3}$.

**28.** *Strategy: verify the defining equation of the sum and invoke uniqueness.*

Let $x = \frac{a}{b}$ and $y = \frac{c}{b}$. By the quotient characterization, $bx = a$ and $by = c$.
Then, by distributivity in $\mathbb{Q}$,

$$
b(x+y) = bx + by = a + c.
$$

So $x + y$ is a number whose product with $b$ is $a+c$. The number with that property is
$\frac{a+c}{b}$, and it is **unique**: if $bz_1 = a+c = bz_2$ then $b(z_1 - z_2) = 0$, and since
$b \neq 0$ we get $z_1 = z_2$. Therefore

$$
\dfrac{a}{b} + \dfrac{c}{b} = x + y = \dfrac{a+c}{b}.
$$

$\blacksquare$

*Where uniqueness is used:* without it, $x+y$ would merely be *some* number satisfying the defining
equation, and the notation $\frac{a+c}{b}$ would not be justified. Uniqueness is exactly what makes
"the quotient" well defined.

**29.** *Strategy: turn the division into an equation, then multiply both sides by the reciprocal of
the divisor.*

By Definition 5.4, $x = \frac{a}{b} \div \frac{c}{d}$ is the number satisfying

$$
\dfrac{c}{d}\,x = \dfrac{a}{b}.
$$

Because $c \neq 0$ and $d \neq 0$, the reciprocal $\frac{d}{c}$ exists, and by P5

$$
\dfrac{c}{d}\cdot\dfrac{d}{c} = \dfrac{cd}{dc} = 1.
$$

Multiplying both sides of the equation by $\frac{d}{c}$:

$$
\dfrac{d}{c}\cdot\dfrac{c}{d}\,x = \dfrac{d}{c}\cdot\dfrac{a}{b}, \qquad\text{so}\qquad x = \dfrac{a}{b}\cdot\dfrac{d}{c}.
$$

$\blacksquare$

*Why $c \neq 0$ is needed:* the reciprocal $\frac{d}{c}$ does not exist when $c = 0$, so the
multiplication step is impossible. And indeed the quotient is not defined: if $c = 0$ the divisor
$\frac{c}{d}$ equals $0$, and the equation $0 \cdot x = \frac{a}{b}$ has no solution when
$\frac{a}{b} \neq 0$ and every rational $x$ as a solution when $\frac{a}{b} = 0$. In neither case is
there a unique quotient.

*Direct verification (for completeness):*
$\frac{c}{d}\cdot\frac{ad}{bc} = \frac{acd}{bcd} = \frac{a}{b}$ by P1 with $k = cd \neq 0$.

**30.** (a) Put both fractions over the common denominator $n(n+1)$:

$$
\dfrac{1}{n} - \dfrac{1}{n+1} = \dfrac{n+1}{n(n+1)} - \dfrac{n}{n(n+1)} = \dfrac{(n+1) - n}{n(n+1)} = \dfrac{1}{n(n+1)}.
$$

$\blacksquare$

(b) Each denominator is a product of consecutive integers:

$$
2 = 1\cdot 2, \quad 6 = 2 \cdot 3, \quad 12 = 3\cdot 4, \quad 20 = 4\cdot 5, \quad 30 = 5 \cdot 6.
$$

So by part (a),

$$
\dfrac{1}{2} + \dfrac{1}{6} + \dfrac{1}{12} + \dfrac{1}{20} + \dfrac{1}{30}
= \left(1 - \dfrac{1}{2}\right) + \left(\dfrac{1}{2} - \dfrac{1}{3}\right) + \left(\dfrac{1}{3} - \dfrac{1}{4}\right) + \left(\dfrac{1}{4} - \dfrac{1}{5}\right) + \left(\dfrac{1}{5} - \dfrac{1}{6}\right).
$$

All intermediate terms cancel (a telescoping sum), leaving

$$
1 - \dfrac{1}{6} = \dfrac{5}{6}.
$$

*Check by common denominator $60$:* $\frac{30}{60} + \frac{10}{60} + \frac{5}{60} + \frac{3}{60} + \frac{2}{60} = \frac{50}{60} = \frac{5}{6}$.

**31.** *Strategy: build a strictly decreasing sequence of fractions, all strictly between the two
given ones.*

Let $x < y$ be distinct fractions.

*Claim:* define $m_1 = \frac{x+y}{2}$ and $m_{n+1} = \frac{x + m_n}{2}$. Then

$$
x < \cdots < m_{n+1} < m_n < \cdots < m_1 < y
$$

for every $n \ge 1$, so the $m_n$ are infinitely many distinct fractions in the interval.

*Proof of the claim.* First, $x < y$ implies $2x < x+y < 2y$, hence, dividing by the positive number
$2$, $x < m_1 < y$. Now suppose $x < m_n$. Then $2x < x + m_n < 2m_n$, and dividing by $2$ gives

$$
x < m_{n+1} < m_n.
$$

So each step produces a new fraction strictly between $x$ and the previous one. Since the sequence is
strictly decreasing, all its terms are distinct, and there are infinitely many of them, all inside
$(x, y)$. $\blacksquare$

*Example:* starting from $\frac{1}{2}$ and $\frac{2}{3}$, the construction gives
$\frac{7}{12}, \frac{13}{24}, \frac{25}{48}, \ldots$, all distinct and all strictly between.

**32.** *Strategy: combine known unit-fraction identities, then verify.*

*First decomposition.* $\frac{1}{2} + \frac{1}{3} = \frac{3}{6} + \frac{2}{6} = \frac{5}{6}$.

*Second decomposition.* Using $\frac{1}{3} = \frac{1}{4} + \frac{1}{12}$ (which is P10 with $n = 3$:
$\frac{1}{3} - \frac{1}{4} = \frac{1}{12}$), we get

$$
\dfrac{5}{6} = \dfrac{1}{2} + \dfrac{1}{4} + \dfrac{1}{12}.
$$

*Verification.* Over the common denominator $12$:
$\frac{6}{12} + \frac{3}{12} + \frac{1}{12} = \frac{10}{12} = \frac{5}{6}$.

Both decompositions use distinct unit fractions, and they are different from each other, which shows
that Egyptian representations are not unique.

**33.** (a) The three parts must add to the whole field:

$$
\dfrac{3}{8} + \dfrac{1}{3} = \dfrac{9}{24} + \dfrac{8}{24} = \dfrac{17}{24}, \qquad
1 - \dfrac{17}{24} = \dfrac{24}{24} - \dfrac{17}{24} = \dfrac{7}{24}.
$$

So $\frac{7}{24}$ of the field is oats.

(b) $\frac{7}{24}$ of $48$ hectares is

$$
\dfrac{7}{24}\cdot 48 = 7 \cdot 2 = 14 \text{ hectares}.
$$

*Check:* wheat is $\frac{3}{8}\cdot 48 = 18$ ha, barley is $\frac{1}{3}\cdot 48 = 16$ ha, and
$18 + 16 + 14 = 48$.

## Challenge

**34.** *Strategy: use the cross-product equation and Euclid's lemma in both directions.*

Let $\frac{a}{b} = \frac{c}{d}$ with $b, d > 0$ and both fractions in lowest terms. By Definition 5.3,

$$
ad = bc. \tag{$\ast$}
$$

*Case $a = 0$.* Then $0 = bc$ with $b > 0$, so $c = 0$. Both fractions equal $0$. In lowest terms
with positive denominator the only representation of $0$ is $\frac{0}{1}$: the condition
$\gcd(|a|, b) = 1$ reads $\gcd(0,b) = b = 1$, and similarly $d = 1$. So $a = c = 0$ and $b = d = 1$.

*Case $a \neq 0$.* From $(\ast)$, $b$ divides $ad$. Since $\gcd(a,b) = 1$, Euclid's lemma gives
$b \mid d$. By symmetry, $d$ divides $bc$ and $\gcd(c,d) = 1$, so $d \mid b$. Both $b$ and $d$ are
positive, so $b \mid d$ and $d \mid b$ force $b = d$.

Substituting $b = d$ into $(\ast)$ gives $ad = ac$, and since $d = b > 0$, cancellation yields
$a = c$. $\blacksquare$

*Why this matters:* it justifies speaking of "the" lowest-terms form of a fraction, which the
tutorial uses when it says a rational number has a unique canonical representative.

**35.** *Strategy: contradiction plus parity, exactly as in Exercise 33 of the integers topic.*

Suppose, for contradiction, that $x$ is rational with $x^2 = 2$. Write $x = \frac{a}{b}$ in lowest
terms with $b > 0$; in particular $\gcd(|a|, b) = 1$, and $a \neq 0$ because $x^2 = 2 \neq 0$. Then

$$
\dfrac{a^2}{b^2} = 2, \qquad\text{so}\qquad a^2 = 2b^2.
$$

*Step 1: $a$ is even.* The right-hand side is even, so $a^2$ is even. If $a$ were odd, then
$a = 2k+1$ and $a^2 = 4k^2 + 4k + 1$ would be odd. Hence $a = 2m$ for some integer $m$.

*Step 2: $b$ is even.* Substituting, $4m^2 = 2b^2$, so $b^2 = 2m^2$. The right-hand side is even, so
$b^2$ is even, and by the same parity argument $b = 2n$ for some integer $n$.

*Step 3: contradiction.* Now $2 \mid a$ and $2 \mid b$, so $\gcd(|a|, b) \ge 2 > 1$, contradicting the
assumption that $\frac{a}{b}$ is in lowest terms. Therefore no rational $x$ satisfies $x^2 = 2$.
$\blacksquare$

*Remark.* The same argument shows that $\sqrt{p}$ is irrational for every prime $p$, and it is the
standard first example of a number that is not rational. It also shows that the rationals, despite
having no gaps between any two of their members, still leave holes on the number line.

**36.** (a) *Strategy: at each step take the largest unit fraction not exceeding the remainder.*

*Step 1.* The remainder is $\frac{5}{7}$. The largest unit fraction not exceeding it is
$\frac{1}{2}$: indeed $\frac{1}{1} = 1 > \frac{5}{7}$, while $\frac{1}{2} \le \frac{5}{7}$ because
cross-multiplying gives $7 \le 10$. The remainder is

$$
\dfrac{5}{7} - \dfrac{1}{2} = \dfrac{10}{14} - \dfrac{7}{14} = \dfrac{3}{14}.
$$

*Step 2.* $\frac{3}{14}$ is the current remainder. The largest unit fraction not exceeding it is
$\frac{1}{5}$, because $\frac{1}{4} > \frac{3}{14}$ (cross-multiplying: $14 > 12$) while
$\frac{1}{5} \le \frac{3}{14}$ ($14 \le 15$). The remainder is

$$
\dfrac{3}{14} - \dfrac{1}{5} = \dfrac{15}{70} - \dfrac{14}{70} = \dfrac{1}{70}.
$$

*Step 3.* The remainder is already a unit fraction, so the process stops:

$$
\dfrac{5}{7} = \dfrac{1}{2} + \dfrac{1}{5} + \dfrac{1}{70}.
$$

*Verification.* Over the common denominator $70$:
$\frac{35}{70} + \frac{14}{70} + \frac{1}{70} = \frac{50}{70} = \frac{5}{7}$.

(b) *Strategy: clear denominators and count integers in an interval.*

A fraction with denominator $60$ has the form $\frac{k}{60}$ with $k$ an integer. The condition is

$$
\dfrac{1}{3} < \dfrac{k}{60} < \dfrac{2}{5}.
$$

Multiplying through by the positive number $60$:

$$
20 < k < 24.
$$

So $k \in \{21, 22, 23\}$ and the fractions are

$$
\dfrac{21}{60} = \dfrac{7}{20}, \qquad \dfrac{22}{60} = \dfrac{11}{30}, \qquad \dfrac{23}{60}\ (\text{already in lowest terms}).
$$

*Check:* over the common denominator $60$,
$\frac{7}{20} = \frac{21}{60}$, $\frac{11}{30} = \frac{22}{60}$ and $\frac{23}{60}$ is already over
$60$; and

$$
\dfrac{1}{3} = \dfrac{20}{60} < \dfrac{21}{60} < \dfrac{22}{60} < \dfrac{23}{60} < \dfrac{24}{60} = \dfrac{2}{5}.
$$
