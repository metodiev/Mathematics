# Solutions: Mathematical Thinking and Problem Solving

> Companion to [exercises.md](exercises.md) and the [tutorial](README.md).

Every problem is solved in full. The strategy is stated first, because the strategy is the part worth
learning; the arithmetic is written out because skipped steps hide errors.

## Beginner

### Solution 1

**Strategy.** Pair the first term with the last, the second with the second-to-last, and so on.

There are $60$ terms, hence $30$ pairs. Each pair has the same sum:

$$
1 + 60 = 61,\quad 2 + 59 = 61,\quad \dots,\quad 30 + 31 = 61.
$$

Therefore

$$
1 + 2 + \cdots + 60 = 30 \times 61 = 1830.
$$

The pairing is legitimate because addition of integers is commutative and associative: the $k$-th term
from the left and the $k$-th term from the right can be added first without changing the total of a
finite sum. The check from Theorem 1 is $\frac{60 \cdot 61}{2} = 30 \cdot 61 = 1830$.

**Pitfall.** There are $30$ pairs, not $60$: each pair consumes two terms.

### Solution 2

**Strategy.** Split into the two possible parities of $n$; in each case exhibit the even factor.

Let $n \in \mathbb{Z}$.

* If $n$ is even, write $n = 2k$. Then $n(n+1) = 2k(n+1) = 2\bigl(k(n+1)\bigr)$, which is even by the
  definition of even (the witness is $k(n+1) \in \mathbb{Z}$).
* If $n$ is odd, write $n = 2k+1$. Then $n+1 = 2k+2 = 2(k+1)$, so $n(n+1) = 2\bigl(n(k+1)\bigr)$ is
  even.

Every integer is even or odd, so in all cases $n(n+1)$ is even. $\blacksquare$

**Second approach.** Each case is an instance of the lemma "even $\times$ any integer $=$ even"
(Theorem 3, part 4): in the first case the even factor is $n$, in the second it is $n+1$.

### Solution 3

**Strategy.** Test the smallest values in order; the first failure is the smallest counterexample.

The values are $2^2 - 1 = 3$ (prime), $2^3 - 1 = 7$ (prime), and $2^4 - 1 = 16 - 1 = 15 = 3 \cdot 5$
(composite). Hence $n = 4$ is the smallest counterexample, and the statement is false.

**Remark.** Larger failures are easy to produce: at $n = 6$, $2^6 - 1 = 63 = 3^2 \cdot 7$. Primes of
the form $2^p - 1$ are called Mersenne primes and exist only for prime $p$, but not for every prime
$p$: $p = 11$ gives $2^{11} - 1 = 2047 = 23 \cdot 89$.

### Solution 4

**Strategy.** Each operation is invertible on the reals, so undo the operations in reverse order.

The forward chain is $x \mapsto 3x \mapsto 3x+5 \mapsto 2(3x+5) \mapsto 2(3x+5) - 4$, and the output is
$30$. Undo:

$$
30 + 4 = 34,\qquad \frac{34}{2} = 17,\qquad 17 - 5 = 12,\qquad \frac{12}{3} = 4.
$$

**Verification.** $4 \times 3 = 12$; $12 + 5 = 17$; $17 \times 2 = 34$; $34 - 4 = 30$. Correct.

**Second approach.** Solve $2(3x+5) - 4 = 30$: then $2(3x+5) = 34$, $3x + 5 = 17$, $3x = 12$,
$x = 4$. Same answer, same operations; the backwards chain simply performs the algebra in the
convenient order.

### Solution 5

**Strategy.** Compute the first values directly; for the failure cases, look for a common factor rather
than testing primality.

(a) $0^2 + 0 + 41 = 41$, $1 + 1 + 41 = 43$, $4 + 2 + 41 = 47$, $9 + 3 + 41 = 53$: all prime.

(b) At $n = 40$:

$$
40^2 + 40 + 41 = 1600 + 40 + 41 = 1681 = 41^2.
$$

So the claim fails at $n = 40$, which is a counterexample.

(c) At $n = 41$:

$$
41^2 + 41 + 41 = 41(41 + 1 + 1) = 41 \cdot 43,
$$

a product of two integers greater than $1$, hence composite. The pattern is the same as in (b): the
polynomial has the form $n^2 + n + 41 = n(n+1) + 41$, so at $n = 41$ the first term is divisible by
$41$; at $n = 40$ the value equals $41^2$ because $40 \cdot 41 + 41 = 41(40+1)$.

**Lesson.** Forty consecutive successes do not make a theorem; the counterexample is one line away.

### Solution 6

**Strategy.** Recognize the sum as the first $n$ odd numbers, with $2n - 1 = 49$.

From $2n - 1 = 49$ we get $n = 25$. By Theorem 2,

$$
1 + 3 + \cdots + 49 = 25^2 = 625.
$$

**Second method.** There are $25$ terms; their average is $(1 + 49)/2 = 25$; hence the sum is
$25 \times 25 = 625$. The average of an arithmetic progression equals the average of its first and
last terms, which is another way of saying "pair the extremes".

### Solution 7

**Strategy.** Compare powers with the same exponent, using $2^{10} = 1024 > 1000 = 10^3$.

Since $2^{10} = 1024 > 10^3$, raising both sides to the tenth power (the function $t \mapsto t^{10}$ is
strictly increasing for $t > 0$) gives

$$
2^{100} = \left(2^{10}\right)^{10} > \left(10^3\right)^{10} = 10^{30}.
$$

More precisely, $2^{100} = 1.024^{10} \times 10^{30} \approx 1.268 \times 10^{30}$, so $2^{100}$ is
larger by about $27\%$.

**Pitfall.** Citing "about $10^{30}$" is not enough for a strict comparison; the strict inequality
comes from $1.024 > 1$.

### Solution 8

**Strategy.** Recognize a difference of squares: $49 \cdot 51 = (50-1)(50+1)$.

$$
49 \cdot 51 = (50 - 1)(50 + 1) = 50^2 - 1^2 = 2500 - 1 = 2499.
$$

The student's $2399$ is wrong by $100$.

**Last-digit test.** $49 \cdot 51$ ends in $9 \cdot 1 = 9$, and $2399$ also ends in $9$, so the
last-digit test does *not* detect the error. This is the point of the exercise: a cheap test can pass
while the answer is wrong, so several independent checks are needed. A second check: $2399$ is odd and
not divisible by $3$ ($2+3+9+9=23$), while $2499$ is divisible by $3$ ($2+4+9+9 = 24$), and indeed
$49 \cdot 51 = 7^2 \cdot 3 \cdot 17$ is divisible by $3$.

### Solution 9

**Strategy.** Reduce both questions to the parity lemmas; the answer cannot depend on which odd
integers are chosen, only on how many there are.

(a) **Odd.** Proof by pairing: group the seven odd integers into three pairs plus one leftover. Each
pair has even sum (odd + odd = even, Theorem 3 part 2), so the three pairs contribute an even total;
adding the remaining odd integer gives an odd total (even + odd = odd, part 3). More generally, a sum
of $k$ odd integers has the parity of $k$: $k$ even gives an even sum, $k$ odd gives an odd sum.

(b) **Odd.** Each factor is odd, and the product of two odd integers is odd (part 5); applying this
six times to the seven factors gives an odd product.

Neither answer depends on the particular integers: only the count and the parities enter the proof.
$\blacksquare$

### Solution 10

**Strategy.** Write each statement in the form $P \Rightarrow Q$ and apply the definitions of converse
and contrapositive.

Let $P(n)$ be "$4 \mid n$" and $Q(n)$ be "$n$ is even".

* Original: $P \Rightarrow Q$, i.e. "$4 \mid n \Rightarrow n$ is even". **True**: if $n = 4k$ then
  $n = 2(2k)$, so $n$ is even.
* Converse: $Q \Rightarrow P$, i.e. "$n$ even $\Rightarrow 4 \mid n$". **False**: $n = 2$ is even but
  $4 \nmid 2$; also $n = 6$.
* Contrapositive: $\neg Q \Rightarrow \neg P$, i.e. "$n$ odd $\Rightarrow 4 \nmid n$". **True**: if
  $4 \mid n$ then $n$ is even, and an integer cannot be both even and odd. This is the original
  statement in contrapositive form, so it must have the same truth value.

**Remark.** The inverse "$4 \nmid n \Rightarrow n$ odd" is the converse of the contrapositive; it is
false ($n = 6$).

### Solution 11

**Strategy.** Count colours. A domino covers one square of each colour, so equal counts are necessary.

Colour cell $(i,j)$ black when $i+j$ is even. In a $5 \times 5$ board there are $13$ black and $12$
white squares: the black cells are those with $i, j$ both odd ($3 \cdot 3 = 9$) or both even
($2 \cdot 2 = 4$), giving $13$.

If a tiling by $D$ dominoes existed, each domino would cover exactly one black and one white square,
so the board would need $D$ black and $D$ white squares, i.e. equal counts. Since $13 \neq 12$ and the
board has $25$ squares (odd, so equality is impossible anyway), no tiling exists.

The invariant is the difference "(number of black squares) − (number of white squares)": placing a
domino removes one of each, so the difference is unchanged. Initially it is $1$; a completely tiled
board would have difference $0$. $\blacksquare$

### Solution 12

**Strategy.** Multiply a chain of rough factors, keeping one significant figure.

$$
365 \times 24 \times 3600 \approx 400 \times 25 \times 3600 = 400 \times 90{,}000
= 3.6 \times 10^{7}.
$$

A more careful computation: $365 \times 86{,}400 = 31{,}536{,}000 \approx 3.2 \times 10^{7}$ seconds.

Now $\pi \times 10^{7} \approx 3.14 \times 10^{7}$, so the two values agree to about one part in $500$.
The agreement is a numerical coincidence (since $1$ year $\approx 3.156 \times 10^7$ s and
$\pi \approx 3.14159$), useful as a memory aid but not a theorem.

**Sanity check.** $10^{7}$ seconds is about $115$ days; multiplying by $\pi \approx 3.14$ gives about
$362$ days, which is the right order. An answer of $10^{9}$ seconds would be absurd ($\sim 30$ years).

## Intermediate

### Solution 13

**Strategy.** Method 1 factors out the constant $2$ and quotes Theorem 1. Method 2 pairs terms
directly, which avoids quoting any sum formula.

**Method 1.**

$$
\sum_{k=1}^{n} 2k = 2 \sum_{k=1}^{n} k = 2 \cdot \frac{n(n+1)}{2} = n(n+1).
$$

**Method 2 (pairing).** Let $S = \sum_{k=1}^{n} 2k$ and write it forwards and backwards:

$$
S = 2 + 4 + \cdots + 2n, \qquad S = 2n + (2n-2) + \cdots + 2.
$$

The $k$-th term from the left in the first line is $2k$; the $k$-th term from the left in the second
line is $2(n+1-k)$. Their sum is $2n + 2$, independent of $k$. Adding the $n$ pairs,
$2S = n(2n+2) = 2n(n+1)$, so $S = n(n+1)$.

**Method 3 (induction, for comparison).** The case $n = 1$ is $2 = 1 \cdot 2$. If
$\sum_{k=1}^{n} 2k = n(n+1)$, then $\sum_{k=1}^{n+1} 2k = n(n+1) + 2(n+1) = (n+1)(n+2)$, as required.

### Solution 14

**Strategy.** Write the odd integer as $2k+1$, factor $n^2 - 1$, and find an even factor inside.

Let $n = 2k + 1$ with $k \in \mathbb{Z}$. Then

$$
n^2 - 1 = (2k+1)^2 - 1 = 4k^2 + 4k + 1 - 1 = 4k(k+1).
$$

Among the consecutive integers $k$ and $k+1$, exactly one is even, so $k(k+1) = 2m$ for some
$m \in \mathbb{Z}$ (Solution 2). Therefore

$$
n^2 - 1 = 4 \cdot 2m = 8m,
$$

so $8 \mid (n^2 - 1)$. $\blacksquare$

**Check.** $n = 3$: $9 - 1 = 8$; $n = 5$: $25 - 1 = 24 = 3 \cdot 8$; $n = 7$: $49 - 1 = 48 = 6 \cdot 8$.

**Pitfall.** It is not enough to note that $4 \mid (n^2-1)$; the evenness of $k(k+1)$ is what upgrades
$4$ to $8$. For $n$ even the statement fails: $n = 2$ gives $3$, not divisible by $8$.

### Solution 15

**Strategy.** Undo the operations in reverse order, keeping track of the domain of the square root.

The forward chain is $x \mapsto 2x \mapsto 2x + 7 \mapsto \sqrt{2x+7} \mapsto \sqrt{2x+7} - 1 = 4$.
Hence

$$
\sqrt{2x+7} = 5.
$$

Squaring gives $2x + 7 = 25$, so $2x = 18$ and $x = 9$.

**Verification.** $2 \cdot 9 + 7 = 25$ and $\sqrt{25} = 5$, so $5 - 1 = 4$. Correct.

**Why no extraneous solution.** The square root function is injective on $[0, \infty)$: if
$\sqrt{u} = \sqrt{v}$ with $u, v \ge 0$, then $u = v$. Applying the *inverse* operation "square" is
legitimate here because the value $5$ is non-negative, so $5$ lies in the range of the square root. In
general, the equation $\sqrt{u} = c$ is equivalent to "$u = c^2$ and $c \ge 0$"; the condition
$c \ge 0$ is what prevents extraneous roots. If the equation had been $\sqrt{2x+7} = -3$, squaring
would give a candidate, but no solution would exist.

**Contrast.** For $\sqrt{x} = x - 2$, squaring gives $x = (x-2)^2$, so $x^2 - 5x + 4 = 0$ and $x = 1$
or $x = 4$; the value $x = 1$ makes the right side $-1 < 0$, so it must be discarded.

### Solution 16

(a) **Strategy.** Find a quantity that no move changes.

The total sum $T$ of all numbers on the board is unchanged: erasing $a$ and $b$ and writing $a+b$
changes the sum by $-a-b+(a+b) = 0$. Initially $T = 1 + 2 + \cdots + 10 = 55$. When one number
remains, the total is that number, so the final number is $55$, independent of the order of the moves.
$\blacksquare$

(b) **Strategy.** For the move $|a-b|$, find what is preserved modulo $2$.

Let $T$ be the total sum. A move changes it by

$$
-(a+b) + |a-b| = -2\min(a,b),
$$

an even number. Hence the parity of $T$ is invariant. Initially $T = 55$ is odd, so the final number is
odd.

The final number is **not** determined. Two sequences:

*Sequence A.* Replace $(10,9)$ by $1$, then $(8,7)$ by $1$, $(6,5)$ by $1$, $(4,3)$ by $1$, $(2,1)$ by
$1$. The board now holds $\{1,1,1,1,1\}$; replacing pairs of $1$s by $0$ and then $(0,1)$ by $1$ twice
leaves $\{1\}$.

*Sequence B.* Replace $(8,7)$ by $1$, then $(1,1)$ by $0$, $(3,2)$ by $1$, $(4,1)$ by $3$, $(5,3)$ by
$2$, $(6,2)$ by $4$, $(4,0)$ by $4$, $(10,4)$ by $6$, $(9,6)$ by $3$. The board ends with $\{3\}$.

Both finals are odd, as the invariant requires, but $1 \neq 3$, so no invariant of this kind determines
the final value. $\blacksquare$

### Solution 17

**Strategy.** Compute modulo $4$, where squares take only two values.

By Theorem 4, every square is congruent to $0$ or $1$ modulo $4$. Hence for integers $x, y$,

$$
x^2 + y^2 \equiv 0,\ 1,\ \text{or}\ 2 \pmod 4.
$$

Now $1234567 = 4 \cdot 308641 + 3$, so $1234567 \equiv 3 \pmod 4$. Since $3$ is not among
$\{0, 1, 2\}$, the equation has no integer solutions. $\blacksquare$

**Pitfall.** Checking modulo $4$ is enough here; checking modulo $2$ is not, because
$3 \equiv 1 \pmod 2$ and both sides could be odd.

### Solution 18

**Strategy.** Use the handshake lemma (Theorem 5) and check its hypotheses: finitely many people,
acquaintance symmetric, no self-acquaintance.

Suppose nine people each shook hands with exactly three others. Let $E$ be the number of handshakes.
Counting the pairs (person, handshake involving that person) in two ways gives

$$
\sum_{v} \deg(v) = 2E.
$$

The left side is $9 \cdot 3 = 27$, which is odd; the right side is even. This is a contradiction, so
the situation is impossible. $\blacksquare$

The theorem's hypotheses hold: the group is finite, and "shook hands with" is a symmetric relation
between distinct people.

**General statement.** In any finite group, the number of people who shook hands an odd number of
times is even. Nine is odd, so nine people with degree $3$ cannot occur.

### Solution 19

(a) **Strategy.** Prove the contrapositive, which is a direct computation.

Claim: if $n$ is not even, then $n^2$ is not even, i.e. if $n$ is odd then $n^2$ is odd. Let
$n = 2k+1$; then

$$
n^2 = 4k^2 + 4k + 1 = 2(2k^2 + 2k) + 1,
$$

which is odd. Since every integer is even or odd, the contrapositive gives: $n^2$ even $\Rightarrow n$
even. $\blacksquare$

(b) In Step 3 of the proof that $\sqrt{2}$ is irrational, we know $p^2 = 2q^2$, so $p^2$ is even, and
we conclude $p$ is even. That step *is* part (a). Without it, the argument would stop: an even square
would not force an even root, and no contradiction could be derived. The statement is a genuine
theorem about integers, relying on the fact that an integer is exactly one of even or odd. (In a
different algebraic setting, such as the Gaussian integers, the analogous statement needs a different
proof, and the failure of unique factorization in some rings is exactly what makes analogous
irrationality arguments delicate.)

### Solution 20

**Strategy.** Trap $n^2+n+1$ between consecutive squares. The gap between $n^2$ and $(n+1)^2$ is
$2n+1$, and $n^2+n+1$ lies strictly inside that gap when $n \ge 1$.

**Case $n \ge 1$.** We have

$$
n^2 < n^2 + n + 1 < n^2 + 2n + 1 = (n+1)^2,
$$

where the left inequality uses $n + 1 > 0$ and the right uses $n > 0$. A perfect square strictly
between two consecutive squares cannot exist, so no $n \ge 1$ works.

**Case $n = 0$.** $0 + 0 + 1 = 1 = 1^2$. Works.

**Case $n \le -1$.** Write $m = -n \ge 1$. Then $n^2 + n + 1 = m^2 - m + 1$. For $m = 1$ this is
$1 = 1^2$. For $m \ge 2$,

$$
(m-1)^2 = m^2 - 2m + 1 < m^2 - m + 1 < m^2,
$$

because $m^2 - m + 1 - (m^2 - 2m + 1) = m > 0$ and $m^2 - (m^2 - m + 1) = m - 1 > 0$. Again the
number lies strictly between consecutive squares, so no $m \ge 2$ works.

Therefore the only solutions are $n = 0$ and $n = -1$, both giving $1$. $\blacksquare$

**Check.** $n = 2$: $7$, not a square; $n = -2$: $3$, not a square; $n = 3$: $13$, not a square.

### Solution 21

**Strategy.** Track the one step where a quantity that could be zero is used as a divisor.

The flaw is the division by $a - b$. The hypothesis is $a = b$, so $a - b = 0$, and division by zero
is undefined. Up to that point the argument is valid:

$$
a^2 = ab \;\Longrightarrow\; a^2 - b^2 = ab - b^2 \;\Longrightarrow\; (a-b)(a+b) = b(a-b),
$$

and the last equation is true (both sides are $0$). Cancelling $a-b$ requires $a - b \neq 0$, which the
hypotheses contradict.

A correct statement would be: *if $a \neq b$ and $a^2 = ab$, then $a + b = b$.* Substituting $a^2 = ab$
gives $a(a-b) = b(a-b)$, and cancelling the nonzero factor $a-b$ gives $a = b$, contradicting
$a \neq b$. So there is no such pair with $a \neq b$.

**Lesson.** Before dividing by an expression, prove it is nonzero. "Divide by $a-b$" silently adds the
hypothesis $a \neq b$; if that hypothesis is false, the conclusion is void.

### Solution 22

**Strategy.** Decompose into a chain of estimates, each of which can be bounded above and below.

| Quantity | Low | Central | High |
|---|---|---|---|
| Households (people per household $4$ / $2.5$ / $2$) | $0.75 \times 10^6$ | $1.2 \times 10^6$ | $1.5 \times 10^6$ |
| Fraction owning a piano | $1/40$ | $1/20$ | $1/10$ |
| Tunings per piano per year | $0.5$ | $1$ | $2$ |
| Tunings per tuner per year ($4$/day, $250$ days) | $500$ | $1000$ | $1500$ |

Central estimate:

$$
\frac{1.2 \times 10^6 \times \frac{1}{20} \times 1}{1000}
= \frac{6 \times 10^4}{10^3} = 60.
$$

Low bound: $\dfrac{0.75 \times 10^6 \times \frac{1}{40} \times 0.5}{1500} = \dfrac{9375}{1500} \approx 6$.
High bound: $\dfrac{1.5 \times 10^6 \times \frac{1}{10} \times 2}{500} = \dfrac{3 \times 10^5}{500} = 600$.

So the answer lies roughly between $6$ and $600$, with a central value near $60$. The dominant
uncertainty is the fraction of households owning a piano, which enters linearly and is the least
constrained assumption; the tuner's annual capacity matters equally but is easier to pin down.

**Why this is useful.** The estimate rules out answers of $10^{4}$ or more; a business plan assuming
$5000$ tuners in a city of three million would be rejected before any detailed market study.

## Advanced

### Solution 23

**Strategy.** Reduce to residues modulo $3$ and split according to how the five integers are
distributed among the three classes.

Let the integers be $a_1, \dots, a_5$ and let $r_i$ be the residue of $a_i$ modulo $3$, so
$r_i \in \{0, 1, 2\}$. Only the residues matter, because the sum of three integers is divisible by $3$
exactly when the sum of their residues is.

**Case 1: some residue class contains at least three of the $a_i$.** Choose three from that class. Their
residues are all equal to some $r$, so their sum is congruent to $3r \equiv 0 \pmod 3$.

**Case 2: no class contains three.** With five elements in three classes and each class of size at most
$2$, each class must in fact contain at least one element (if some class were empty, five elements
would be distributed over two classes and the pigeonhole principle would put three in one of them,
contradicting the case hypothesis). So each class has exactly one or two elements, and in particular
there is at least one element in each class. Choose one integer from each class; the sum of the three
residues is $0 + 1 + 2 = 3 \equiv 0 \pmod 3$.

In both cases three of the five integers have a sum divisible by $3$. $\blacksquare$

**Remark.** Five is sharp: the four integers $1, 2, 4, 5$ have no three whose sum is divisible by
$3$. Their residues are $1, 2, 1, 2$, and a three-element sum is either $1+2+1 \equiv 1$ or
$1+2+2 \equiv 2$ modulo $3$; neither is $0$.

### Solution 24

**Strategy.** Find a colouring with four colours such that every $1 \times 4$ bar covers exactly one
cell of each colour, then count the colours on the board.

Colour cell $(i,j)$ with colour $(i+j) \bmod 4$, for $1 \le i, j \le 6$. A horizontal bar occupies
$(i,j), (i,j+1), (i,j+2), (i,j+3)$, whose colours are four consecutive residues, hence all four
colours exactly once. A vertical bar is the same with $i$ varying, again giving all four colours.

Now count the cells of each colour. The residues of $i$ modulo $4$ for $i = 1, \dots, 6$ are
$1, 2, 3, 0, 1, 2$: residue $1$ and residue $2$ occur twice each, residues $3$ and $0$ once each. Writing
$r_0 = 1, r_1 = 2, r_2 = 2, r_3 = 1$ for these multiplicities, the number of cells with colour $c$
(that is, with $i + j \equiv c$) is the cyclic convolution

$$
n_c = \sum_{a=0}^{3} r_a\, r_{c-a \bmod 4}.
$$

Computing: $n_0 = 1 + 2 + 4 + 2 = 9$; $n_1 = 2 + 2 + 2 + 2 = 8$; $n_2 = 2 + 4 + 2 + 1 = 9$;
$n_3 = 1 + 4 + 4 + 1 = 10$. The total is $9 + 8 + 9 + 10 = 36$, as it must be.

If a tiling by $1 \times 4$ bars existed, each of the $36/4 = 9$ bars would cover exactly one cell of
each colour, so the board would contain $9$ cells of every colour. But the counts are $8, 9, 9, 10$,
which are not equal. Contradiction; no tiling exists. $\blacksquare$

**Pitfall.** The colouring must be chosen so that *both* orientations of a bar cover all four colours;
$(i+j) \bmod 4$ has this property, while $(i + 2j) \bmod 4$ does not.

### Solution 25

**Strategy.** Imitate the $\sqrt{2}$ proof, replacing parity by divisibility by $3$. The needed lemma
is: if $3 \mid m^2$ then $3 \mid m$.

*Lemma.* For every integer $m$, if $3 \nmid m$ then $3 \nmid m^2$. If $m = 3k+1$ then
$m^2 = 9k^2 + 6k + 1 = 3(3k^2+2k) + 1$; if $m = 3k+2$ then $m^2 = 9k^2 + 12k + 4 = 3(3k^2+4k+1) + 1$.
In both cases $m^2 \equiv 1 \pmod 3$, so $3$ does not divide $m^2$. Taking the contrapositive,
$3 \mid m^2 \Rightarrow 3 \mid m$. $\blacksquare$

*Proof of irrationality.* Suppose $\sqrt{3} = p/q$ with $p, q \in \mathbb{Z}$, $q \neq 0$, and
$\gcd(p,q) = 1$. Squaring gives $p^2 = 3q^2$.

Since $3 \mid 3q^2$, we get $3 \mid p^2$, and by the lemma $3 \mid p$. Write $p = 3r$. Then

$$
9r^2 = 3q^2 \quad\Longrightarrow\quad q^2 = 3r^2,
$$

so $3 \mid q^2$ and hence $3 \mid q$ by the lemma again. Thus $3$ divides both $p$ and $q$,
contradicting $\gcd(p,q) = 1$. Therefore $\sqrt{3}$ is irrational. $\blacksquare$

**Where the argument fails for $\sqrt{4}$.** The lemma for $4$ would say "$4 \mid m^2 \Rightarrow 4 \mid m$",
which is false: $m = 2$ gives $m^2 = 4$ but $4 \nmid 2$. The argument correctly refuses to prove a false
statement.

### Solution 26

**Strategy.** Factor into three consecutive integers and check divisibility by $2$ and by $3$
separately.

For every integer $n$,

$$
n^3 - n = n(n^2 - 1) = n(n-1)(n+1) = (n-1)\,n\,(n+1).
$$

* **Divisibility by $2$.** Among the consecutive integers $n-1$ and $n$, exactly one is even, so $2$
  divides the product.
* **Divisibility by $3$.** Among the three consecutive integers $n-1, n, n+1$, exactly one is congruent
  to $0$ modulo $3$ (the residues cycle $0,1,2$), so $3$ divides the product.

Since $2$ and $3$ are coprime and both divide the product, $6 \mid (n^3 - n)$. $\blacksquare$

**Check.** $n = 2$: $8 - 2 = 6$; $n = 4$: $64 - 4 = 60$; $n = -3$: $-27 + 3 = -24$, divisible by $6$.

**Remark.** The coprimality of $2$ and $3$ is essential: from $2 \mid m$ and $3 \mid m$ we may conclude
$6 \mid m$ because $\gcd(2,3) = 1$. The same inference with $4$ and $6$ would be invalid
($4 \mid 12$ and $6 \mid 12$, but $24 \nmid 12$).

### Solution 27

**Strategy.** Pigeonhole on the *odd part*. Every positive integer can be written uniquely as
$2^a m$ with $a \ge 0$ and $m$ odd.

Let $A$ be a set of $n+1$ integers chosen from $\{1, 2, \dots, 2n\}$. Write each $x \in A$ as
$x = 2^{a(x)} m(x)$ with $m(x)$ odd. Since $x \le 2n$, its odd part satisfies $m(x) \le 2n$; the odd
numbers in $\{1, \dots, 2n\}$ are exactly $1, 3, 5, \dots, 2n-1$, and there are $n$ of them.

Define $f : A \to \{1, 3, \dots, 2n-1\}$ by $f(x) = m(x)$. The domain has $n+1$ elements and the
codomain has $n$; by the pigeonhole principle, two distinct elements $x, y \in A$ have $m(x) = m(y) = m$.

Then $x = 2^a m$ and $y = 2^b m$ with $a \neq b$ (since $x \neq y$). If $a < b$ then
$y = 2^{b-a} x$, so $x \mid y$; if $b < a$ then $x = 2^{a-b} y$, so $y \mid x$. Either way, one of the
two divides the other. $\blacksquare$

**Check for small $n$.** With $n = 3$, the set is $\{1, \dots, 6\}$ and any $4$ elements contain a
dividing pair; for example $\{4, 5, 6, 1\}$ contains $1 \mid 4$. The bound is sharp: $\{n+1, \dots, 2n\}$
has $n$ elements and contains no dividing pair when $n \ge 1$, since $2(n+1) > 2n$.

### Solution 28

**Strategy.** Replace each term by a larger telescoping term, then sum.

For $k \ge 2$ we have $k^2 > k(k-1) > 0$, so

$$
\frac{1}{k^2} < \frac{1}{k(k-1)} = \frac{1}{k-1} - \frac{1}{k}.
$$

Therefore

$$
\sum_{k=2}^{n} \frac{1}{k^2}
< \sum_{k=2}^{n} \left(\frac{1}{k-1} - \frac{1}{k}\right)
= 1 - \frac{1}{n}.
$$

Adding the $k = 1$ term,

$$
\sum_{k=1}^{n} \frac{1}{k^2} = 1 + \sum_{k=2}^{n} \frac{1}{k^2} < 1 + \left(1 - \frac{1}{n}\right) = 2 - \frac{1}{n} < 2.
$$

$\blacksquare$

**Why the inequality is strict.** Each term was replaced by a strictly larger one ($k^2 > k(k-1)$ for
$k \ge 2$), so the partial sum is strictly less than the telescoping total; and $2 - 1/n < 2$ for
$n \ge 1$.

**Remark.** As $n \to \infty$ the sum increases to $\pi^2/6 \approx 1.645 < 2$, so the bound is not
sharp, but it is enough to prove convergence. The argument generalizes: $\sum 1/k^p$ converges for
every real $p > 1$ by comparison with $\sum 1/(k(k-1))$.

### Solution 29

**Strategy.** Choose the largest power of $2$ not exceeding $n$ and use its $2$-adic valuation to make
exactly one term odd after clearing denominators.

Let $n \ge 2$ and let $m \ge 1$ be such that $2^m \le n < 2^{m+1}$. Put
$L = \operatorname{lcm}(1, 2, \dots, n)$; then $v_2(L) = m$, meaning $2^m \mid L$ but
$2^{m+1} \nmid L$. Multiply:

$$
L \cdot H_n = \sum_{k=1}^{n} \frac{L}{k}.
$$

Each term $L/k$ is an integer, since $k \le n$ divides $L$. Examine the power of $2$ dividing each
term.

* For $k = 2^m$: $v_2(L/k) = m - m = 0$, so $L/2^m$ is odd.
* For $k \neq 2^m$ with $k \le n$: we have $v_2(k) \le m - 1$. Indeed, if $v_2(k) \ge m$ then $k$ is a
  positive multiple of $2^m$ not exceeding $n < 2^{m+1}$, so $k = 2^m$, contrary to $k \neq 2^m$.
  Hence $v_2(L/k) = m - v_2(k) \ge 1$, so $L/k$ is even.

Therefore $L \cdot H_n$ is a sum of one odd integer and several even integers, hence is odd.

Now suppose, for contradiction, that $H_n$ is an integer $t$. Then $L \cdot H_n = L t$ is divisible by
$L$, and since $n \ge 2$ the number $L$ is even ($2 \mid L$), so $Lt$ is even. But $L \cdot H_n$ was
shown to be odd. Contradiction. Hence $H_n \notin \mathbb{Z}$. $\blacksquare$

**Check.** $n = 3$: $H_3 = 11/6$; $L = 6$, $L H_3 = 11$, odd, and $6 \nmid 11$. $n = 4$: $H_4 = 25/12$;
$L = 12$, $L H_4 = 25$, odd.

**Second approach.** One may also argue with the single term having the *largest* $2$-adic valuation in
the sum $\sum L/k$: it is unique, so the sum is odd. This is the same argument organized around
$v_2$ rather than around a case split.

## Challenge

### Solution 30

**Strategy.** Work modulo $3$: a sum of two squares is $0$ modulo $3$ only if both squares are
$0$ modulo $3$. Then divide out the common factor and iterate — an infinite descent.

*Step 1: squares modulo $3$.* For any integer $u$: if $u \equiv 0$ then $u^2 \equiv 0$; if $u \equiv 1$
then $u^2 \equiv 1$; if $u \equiv 2 \equiv -1$ then $u^2 \equiv 1$. So $u^2 \equiv 0$ or $1 \pmod 3$.

*Step 2: both $x$ and $y$ are divisible by $3$.* Suppose $x^2 + y^2 = 3z^2$. Reducing modulo $3$,
$x^2 + y^2 \equiv 0 \pmod 3$. The possible sums of two elements of $\{0, 1\}$ are $0, 1, 2$, and only
$0+0$ gives $0$ modulo $3$. Hence $x^2 \equiv y^2 \equiv 0 \pmod 3$, so $3 \mid x$ and $3 \mid y$.

*Step 3: $z$ is divisible by $3$.* Write $x = 3x_1$, $y = 3y_1$. Then
$9x_1^2 + 9y_1^2 = 3z^2$, so $3(x_1^2 + y_1^2) = z^2$. Hence $3 \mid z^2$; by the lemma of Solution 25
(or directly from the residue computation), $3 \mid z$. Write $z = 3z_1$.

*Step 4: a smaller solution.* Substituting gives $9x_1^2 + 9y_1^2 = 27z_1^2$, hence
$x_1^2 + y_1^2 = 3z_1^2$. So $(x_1, y_1, z_1)$ is another integer solution.

*Step 5: descent.* Suppose a nonzero solution exists. Among all nonzero solutions choose one with
$|x| + |y| + |z|$ minimal (the set of positive values of this quantity is a nonempty subset of
$\mathbb{N}$, so it has a least element). Step 4 produces a solution with
$|x_1| + |y_1| + |z_1| = \frac{1}{3}(|x| + |y| + |z|)$, which is strictly smaller and still positive,
contradicting minimality. Therefore no nonzero integer solution exists. $\blacksquare$

**Pitfall.** It is not enough to observe that $3 \mid x$ and $3 \mid y$; one must also show $3 \mid z$
and that the divided triple is again a solution. That is what turns a local observation into a global
contradiction.

### Solution 31

**Strategy.** Compute small cases, identify the mechanism, then prove by induction using the
recurrence the mechanism provides.

(a) The values are $P(0) = 1$, $P(1) = 2$, $P(2) = 4$, $P(3) = 7$, $P(4) = 11$. (Draw a circle and add
lines; each new line must cross all previous ones.)

(b) The $n$-th line meets each of the previous $n-1$ lines exactly once: they are not parallel, and no
three lines pass through one point, so the $n-1$ intersection points are distinct. These points divide
the new line into $n-1+1 = n$ segments. Each segment lies inside one existing region and cuts it into
two, so each segment increases the piece count by exactly $1$. The increase is therefore $n$.

Note that the two rays of the line outside the pancake do not create pieces; only the segments inside
count. Since the pancake is large enough to contain all intersections (or the lines are chords of a
large circle), the count is $n$ new pieces per line.

(c) From (b), $P(n) = P(n-1) + n$ for $n \ge 1$, with $P(0) = 1$. We prove
$P(n) = \frac{n^2+n+2}{2}$ by induction.

*Base.* $n = 0$: $\frac{0+0+2}{2} = 1 = P(0)$.

*Step.* Assume $P(n-1) = \frac{(n-1)^2 + (n-1) + 2}{2}$. Then

$$
P(n) = P(n-1) + n = \frac{n^2 - 2n + 1 + n - 1 + 2}{2} + n
= \frac{n^2 - n + 2 + 2n}{2} = \frac{n^2 + n + 2}{2}.
$$

So the formula holds for $n$. By induction it holds for all $n \ge 0$. $\blacksquare$

**Check.** $n = 4$: $(16 + 4 + 2)/2 = 11$, matching the drawing. The sequence
$1, 2, 4, 7, 11, 16, \dots$ is the lazy caterer's sequence.

**Remark.** The same recurrence with a different initial condition would give a different formula; the
mechanism, not the sequence, is what makes the proof work.

### Solution 32

**Strategy.** Pick one person and use the pigeonhole principle on the other five; among three people
related to the first in the same way, either a pair is related in the same way or all three are
unrelated.

Let $A$ be one of the six people. Each of the other five is either acquainted with $A$ or a stranger to
$A$. By the pigeonhole principle, at least $\lceil 5/2 \rceil = 3$ of them fall into the same category.
Call three of them $B, C, D$, and suppose first that all three are acquainted with $A$.

**Case 1: some two of $B, C, D$ are acquainted.** Say $B$ and $C$ are acquainted. Then $A, B, C$ are
pairwise acquainted: $A$ knows $B$ and $C$ by assumption, and $B$ knows $C$. Three mutual
acquaintances.

**Case 2: no two of $B, C, D$ are acquainted.** Then $B, C, D$ are pairwise strangers: three mutual
strangers.

If instead the three chosen people were all strangers to $A$, the same argument with "acquainted" and
"stranger" exchanged gives either three mutual strangers (if two of $B,C,D$ are strangers) or three
mutual acquaintances (if no two are strangers, i.e. all pairs among $B,C,D$ are acquaintances). In every
case, one of the two desired configurations occurs. $\blacksquare$

**Sharpness.** Five people are not enough: arrange five people in a cycle, each acquainted with exactly
its two neighbours. There is no triangle of acquaintances (the graph is a $5$-cycle) and no triangle of
strangers (the complement of a $5$-cycle is another $5$-cycle). So $R(3,3) = 6$.

### Solution 33

**Strategy.** Group the terms of $H_{2^m}$ into blocks whose lengths double, and bound each block
below by a constant.

For $m \ge 0$ write

$$
H_{2^m} = 1 + \frac{1}{2} + \left(\frac{1}{3} + \frac{1}{4}\right)
+ \left(\frac{1}{5} + \cdots + \frac{1}{8}\right) + \cdots
+ \left(\frac{1}{2^{m-1}+1} + \cdots + \frac{1}{2^m}\right).
$$

For $j = 1, \dots, m$, the $j$-th block contains the terms $1/k$ with $2^{j-1} < k \le 2^j$. It has
$2^j - 2^{j-1} = 2^{j-1}$ terms, and each term satisfies $1/k \ge 1/2^j$ because $k \le 2^j$. Hence

$$
\sum_{k=2^{j-1}+1}^{2^j} \frac{1}{k} \ge 2^{j-1} \cdot \frac{1}{2^j} = \frac{1}{2}.
$$

There are $m$ blocks, so

$$
H_{2^m} \ge 1 + \underbrace{\frac{1}{2} + \cdots + \frac{1}{2}}_{m \text{ terms}} = 1 + \frac{m}{2}.
$$

$\blacksquare$

**Divergence.** Let $B$ be any real number. Choose an integer $m > 2(B-1)$, so that $1 + m/2 > B$.
Then $H_{2^m} \ge 1 + m/2 > B$, and the sequence $(H_n)$ is increasing, so it is unbounded. The harmonic
series diverges. $\blacksquare$

**Second approach.** Compare with an integral:

$$
H_n = 1 + \sum_{k=2}^{n} \frac{1}{k} \ge 1 + \int_{1}^{n} \frac{dx}{x} = 1 + \ln n,
$$

which also tends to infinity, and is sharper (it shows $H_n \sim \ln n$). The block argument has the
advantage of needing no calculus.

**Check.** $m = 3$: $H_8 = 1 + 1/2 + 1/3 + \cdots + 1/8 = 761/280 \approx 2.718$, and
$1 + 3/2 = 2.5$, so the bound holds.
