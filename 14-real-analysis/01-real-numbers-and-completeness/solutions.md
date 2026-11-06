# The Real Numbers and Completeness — Solutions

> [Tutorial](README.md) · [Exercises](exercises.md) · Complete solutions to all 36 problems

Each solution states the strategy first, then carries out every step. Results from the
[tutorial](README.md) are cited by number; the notation $\sup S$, $\inf S$ and "upper bound" is
Definition 5.4–5.5 there.

## Beginner

### Solution 1

*Strategy.* Write the general term as $1 - 1/n$, show that $1$ is an upper bound that cannot be
improved and is not attained, and that $0$ is a lower bound that is attained.

The elements are $1 - 1/n$ for $n \ge 1$: that is $0, \tfrac12, \tfrac23, \tfrac34, \dots$.

*Supremum.* Since $1/n > 0$, every element satisfies $1 - 1/n < 1$; so $1$ is an upper bound and is
not in $S$. Let $\varepsilon > 0$. By Corollary 7.15 there is $n$ with $1/n < \varepsilon$, hence
$1 - 1/n > 1 - \varepsilon$. By Lemma 7.11, $\sup S = 1$. Since $1 \notin S$, $S$ has no maximum
(Lemma 7.12).

*Infimum.* Since $n \ge 1$ gives $1/n \le 1$, every element satisfies $1 - 1/n \ge 0$. And
$0 = 1 - 1/1 \in S$. So $0$ is a lower bound that belongs to $S$, hence $\inf S = \min S = 0$.

*Answer.* $\sup S = 1$ (no maximum), $\inf S = \min S = 0$.

### Solution 2

*Strategy.* Identify the set as the closed interval $[-3,3]$.

We claim
$$
x^2 \le 9 \iff -3 \le x \le 3 .
$$
If $-3 \le x \le 3$ then $\lvert x\rvert \le 3$, so $x^2 = \lvert x\rvert^2 \le 9$. Conversely, if
$x > 3$ then $x^2 > 9$, and if $x < -3$ then $-x > 3$ and $x^2 = (-x)^2 > 9$; so $x^2 \le 9$ forces
$-3 \le x \le 3$.

Hence $S = [-3,3]$. The number $3$ is an upper bound and lies in $S$, so $\sup S = \max S = 3$; the
number $-3$ is a lower bound and lies in $S$, so $\inf S = \min S = -3$.

### Solution 3

*Strategy.* Separate the even and odd cases; there is no limit argument needed because the extreme
values are attained.

For even $n = 2k$ the element is $3 + 1/(2k)$, which is largest when $k = 1$, giving $3 + 1/2 = 7/2$;
for all even $n$, $3 + 1/n \le 7/2$. For odd $n$, $3 - 1/n < 3 < 7/2$. So $7/2$ is an upper bound of
$S$ and belongs to $S$ (at $n = 2$): $\sup S = \max S = 7/2$.

For odd $n$, $3 - 1/n \ge 3 - 1 = 2$ with equality at $n = 1$; for even $n$, $3 + 1/n > 3 > 2$. So $2$
is a lower bound of $S$ and belongs to $S$: $\inf S = \min S = 2$.

### Solution 4

*Strategy.* Show $2$ is the least upper bound by using density to rule out every smaller candidate;
then check membership.

*Upper bound.* Every $q \in S$ satisfies $q < 2$, so $2$ is an upper bound.

*Least.* Let $u < 2$. If $u \le 1$, then $q = 3/2 \in S$ satisfies $q > u$. If $1 < u < 2$, Theorem
7.20 applied to $x = u$ and $y = 2$ gives a rational $q$ with $u < q < 2$, and $q > u > 1$ shows
$q \in S$. In both cases some element of $S$ exceeds $u$, so $u$ is not an upper bound. Hence
$\sup S = 2$ by Lemma 7.11.

*Membership.* $2 \notin S$ because $q < 2$ is required, so there is no maximum. Similarly $1$ is a
lower bound, and for any $v > 1$ density gives $q \in (1, \min\{v,2\}) \subseteq S$ with $q < v$, so
no $v > 1$ is a lower bound; hence $\inf S = 1$, and $1 \notin S$ so there is no minimum.

*Note.* Here the supremum is not a rational number that could be "just above" the set; the hole is at
$2$, which happens to be rational, but the set excludes it. The situation is different from
Theorem 7.6, where the *value* of the supremum is missing from the field.

### Solution 5

*Strategy.* Rewrite $n/(n+1) = 1 - 1/(n+1)$ and copy the structure of Solution 1 with the shift.

For every $n \ge 1$, $1/(n+1) > 0$, so $n/(n+1) = 1 - 1/(n+1) < 1$: $1$ is an upper bound, not
attained. Given $\varepsilon > 0$, choose $n$ with $1/(n+1) < \varepsilon$ (Corollary 7.15 applied to
$\varepsilon$ gives $m$ with $1/m < \varepsilon$; take $n = m$). Then $1 - 1/(n+1) > 1 - \varepsilon$.
So $\sup S = 1$ and there is no maximum.

Also $1/(n+1) \le 1/2$ for $n \ge 1$, so $n/(n+1) \ge 1/2$, with equality exactly at $n = 1$. Hence
$\inf S = \min S = 1/2$.

### Solution 6

*Strategy.* For a finite set the supremum is the largest element and the infimum the smallest, because
a maximum is always an upper bound and no upper bound can be smaller than an element of the set
(Lemma 7.12).

Every element of $A$ is $\le 7$ and $7 \in A$; hence $\sup A = \max A = 7$.
Every element of $A$ is $\ge 2$ and $2 \in A$; hence $\inf A = \min A = 2$.

### Solution 7

*Strategy.* Refute with the simplest open interval and prove that no element can be maximal.

**False.** The set $S = (0,1) = \{x \in \mathbb{R} : 0 < x < 1\}$ is nonempty and bounded above
(every element is $< 1$), but it has no maximum.

*Proof.* Suppose $S$ had a maximum $m$. Then $m \in S$, so $0 < m < 1$, and
$$
m' = \frac{m+1}{2}
$$
satisfies $m < m' < 1$ and $m' > 0$, so $m' \in S$ and $m' > m$ — contradicting that $m$ is an
upper bound of $S$. Hence no maximum exists.

*Moral.* Boundedness above gives an upper bound; a maximum requires a *least* upper bound that
belongs to the set, and an open set has no such element at its edge.

### Solution 8

*Strategy.* Same structure as Solutions 1 and 5, with $2/n$ in place of $1/n$.

Every element satisfies $3 - 2/n < 3$, so $3$ is an upper bound, not attained. Given $\varepsilon>0$,
choose $n$ with $2/n < \varepsilon$ (Archimedean property: choose $n > 2/\varepsilon$). Then
$3 - 2/n > 3 - \varepsilon$; so $\sup S = 3$ and there is no maximum.

Since $2/n \le 2$ for $n \ge 1$, every element is $\ge 3 - 2 = 1$, with equality at $n = 1$. Hence
$\inf S = \min S = 1$.

### Solution 9

*Strategy.* Leastness is proved by comparing with an arbitrary upper bound.

Let $u$ be an upper bound of $S$ with $u \in S$. Let $v$ be any upper bound of $S$. Since $u \in S$,
the definition of upper bound gives $u \le v$. Thus $u$ is an upper bound that is $\le$ every upper
bound, i.e. $u$ is the least upper bound: $u = \sup S$ (which exists, by (LUB), since $S$ is
nonempty and bounded above by $u$). $\blacksquare$

### Solution 10

*Strategy.* Compare the sets of upper bounds.

Let $U_T$ be the set of upper bounds of $T$ and $U_S$ that of $S$. If $u \in U_T$ then $t \le u$ for
all $t \in T$; since $S \subseteq T$, also $s \le u$ for all $s \in S$, so $u \in U_S$. Hence
$U_T \subseteq U_S$.

Both sets are nonempty and $\sup T = \min U_T$, $\sup S = \min U_S$ exist. Since $U_S$ is a larger
set, its least element is at most the least element of $U_T$:
$$
\sup S = \min U_S \le \min U_T = \sup T . \qquad \blacksquare
$$

*Remark.* Intuitively: a bigger set pushes the ceiling higher or leaves it unchanged.

### Solution 11

*Strategy.* Work directly from the definitions, using Solution 1's computations for $S$.

We know $\sup S = 1$ and $\inf S = 0$ (Corollary 7.15).

The set is $-S = \{-1/n : n \in \mathbb{N}\} = \{-1, -\tfrac12, -\tfrac13, \dots\}$.

*$\sup(-S) = 0$.* Every element satisfies $-1/n < 0$, so $0$ is an upper bound. Given $\varepsilon>0$,
choose $n$ with $1/n < \varepsilon$; then $-1/n > -\varepsilon$, so $-1/n$ exceeds $0 - \varepsilon$.
Hence $\sup(-S) = 0 = -\inf S$.

*$\inf(-S) = -1$.* Every element satisfies $-1/n \ge -1$, so $-1$ is a lower bound, and
$-1 = -1/1 \in -S$ is attained. Hence $\inf(-S) = -1 = -\sup S$.

Both identities of Theorem 7.13 hold in this example.

### Solution 12

*Strategy.* Factor $x^3 - 8$ and use the sign of the quadratic factor.

We have
$$
x^3 - 8 = (x-2)(x^2 + 2x + 4), \qquad x^2 + 2x + 4 = (x+1)^2 + 3 > 0 \text{ for all } x .
$$
Since the quadratic factor is always positive, $x^3 - 8$ has the sign of $x - 2$; hence
$$
x^3 < 8 \iff x < 2, \qquad\text{so}\qquad S = (-\infty, 2).
$$

Therefore $\sup S = 2$: $2$ is an upper bound, and for $\varepsilon > 0$ the element $2 - \varepsilon/2$
lies in $S$ and exceeds $2 - \varepsilon$. The supremum is not attained, so there is no maximum.

The set is **not bounded below**: given any $M \in \mathbb{R}$, the number $x = -(\lvert M\rvert + 1)$
satisfies $x < 2$, hence $x \in S$, and $x < M$. So $\inf S = -\infty$ in the extended sense of
Definition 7.55; there is no real infimum.

## Intermediate

### Solution 13

*Strategy.* One direction is Lemma 7.11 with $\varepsilon = 1/n$; the other uses the Archimedean
property to pass from $1/n$ to an arbitrary $\varepsilon$.

*($\Rightarrow$)* Suppose $\alpha = \sup S$. Then $\alpha$ is an upper bound. For $n \in \mathbb{N}$,
the number $\alpha - 1/n$ is strictly smaller than the least upper bound, so it is not an upper bound;
hence there is $s \in S$ with $s > \alpha - 1/n$.

*($\Leftarrow$)* Suppose $\alpha$ is an upper bound with the stated property. Let $\beta < \alpha$ be
any real number. Put $\varepsilon = \alpha - \beta > 0$ and choose $n$ with $1/n < \varepsilon$
(Corollary 7.15). By hypothesis there is $s \in S$ with
$$
s > \alpha - \frac1n > \alpha - \varepsilon = \beta .
$$
So $\beta$ is not an upper bound of $S$. Since every number below $\alpha$ fails to be an upper bound,
$\alpha$ is the least one: $\alpha = \sup S$. $\blacksquare$

*Remark.* The same proof works with $1/n$ replaced by any sequence of positive numbers tending to
$0$; the point of the exercise is that the $\varepsilon$-version and the countable version of the
approximation property are equivalent over $\mathbb{R}$.

### Solution 14

*Strategy.* Complete the square and use the existence of $\sqrt 3$.

$$
x^2 - 4x + 1 = (x-2)^2 - 4 + 1 = (x-2)^2 - 3 .
$$
Hence
$$
x^2 - 4x + 1 < 0 \iff (x-2)^2 < 3 \iff \lvert x - 2\rvert < \sqrt 3 ,
$$
because for $t \ge 0$, $t^2 < 3 \iff t < \sqrt 3$ (if $t \ge \sqrt3$ then $t^2 \ge 3$; if $t < \sqrt3$
then $t^2 < 3$). Here $\sqrt 3$ denotes the positive root constructed by the method of Theorem 7.24
with $3$ in place of $2$; Exercise 23 carries out the details. Therefore
$$
S = \left(2 - \sqrt 3,\ 2 + \sqrt 3\right).
$$

*Supremum.* Every $x \in S$ satisfies $x < 2 + \sqrt3$, so $2 + \sqrt3$ is an upper bound. Let
$\varepsilon > 0$ and put $\delta = \min\{\varepsilon/2, \sqrt 3\}$. Then $x = 2 + \sqrt3 - \delta$
satisfies $x < 2+\sqrt3$ and $x \ge 2 > 2 - \sqrt3$, so $x \in S$, and $x > 2 + \sqrt3 - \varepsilon$.
Hence $\sup S = 2 + \sqrt3$. It is not attained.

*Infimum.* Every $x \in S$ satisfies $x > 2 - \sqrt3$, so $2 - \sqrt3$ is a lower bound. For
$\varepsilon > 0$, $x = 2 - \sqrt3 + \min\{\varepsilon/2, \sqrt3\}$ lies in $S$ and is below
$2 - \sqrt3 + \varepsilon$. Hence $\inf S = 2 - \sqrt3$, not attained.

### Solution 15

*Strategy.* Show $c + \sup S$ is an upper bound, then that nothing smaller is. Translation preserves
order (axiom O3), which is all that is needed.

*Upper bound.* For every $s \in S$, $s \le \sup S$, so $c + s \le c + \sup S$ by O3. Hence
$c + \sup S$ is an upper bound of $c + S$.

*Least.* Let $u$ be an upper bound of $c + S$. For every $s \in S$, $c + s \le u$, so
$s \le u - c$ (subtract $c$, using O3). Thus $u - c$ is an upper bound of $S$, so $\sup S \le u - c$,
i.e. $c + \sup S \le u$.

Therefore $c + \sup S$ is the least upper bound of $c + S$. $\blacksquare$

*Remark.* The analogous statement for infima, $\inf(c+S) = c + \inf S$, has the same proof.

### Solution 16

*Strategy.* Bound above by $\alpha\beta$, then approximate both factors simultaneously. The
approximation needs a division by $\alpha$ and $\beta$, which is where positivity enters.

Let $\alpha = \sup A$ and $\beta = \sup B$. Since $A, B \subseteq (0,\infty)$, every element is
positive; in particular $\alpha \ge a > 0$ and $\beta \ge b > 0$ for any chosen $a \in A$, $b \in B$,
so $\alpha > 0$ and $\beta > 0$.

*Upper bound.* For $a \in A$, $b \in B$: from $a \le \alpha$ and $b > 0$ we get $ab \le \alpha b$, and
from $b \le \beta$ and $\alpha > 0$ we get $\alpha b \le \alpha\beta$. Hence $ab \le \alpha\beta$.

*Least.* Let $\varepsilon > 0$. If $\varepsilon \ge \alpha\beta$ then any $a \in A$, $b \in B$ give
$ab > 0 \ge \alpha\beta - \varepsilon$, so there is nothing to prove. Assume therefore
$\varepsilon < \alpha\beta$. Then
$$
\alpha - \frac{\varepsilon}{2\beta} > \alpha - \frac{\alpha}{2} = \frac{\alpha}{2} > 0,
\qquad
\beta - \frac{\varepsilon}{2\alpha} > \frac{\beta}{2} > 0,
$$
so both factors below are positive and multiplying the two inequalities is legitimate. By
Lemma 7.11 choose $a \in A$ with $a > \alpha - \varepsilon/(2\beta)$ and $b \in B$ with
$b > \beta - \varepsilon/(2\alpha)$. Then
$$
ab > \left(\alpha - \frac{\varepsilon}{2\beta}\right)\left(\beta - \frac{\varepsilon}{2\alpha}\right)
= \alpha\beta - \frac{\varepsilon}{2} - \frac{\varepsilon}{2} + \frac{\varepsilon^2}{4\alpha\beta}
> \alpha\beta - \varepsilon .
$$
So no number below $\alpha\beta$ is an upper bound, and $\sup(AB) = \alpha\beta$. $\blacksquare$

*Where positivity is used.* In dividing by $\beta$ and $\alpha$ (nonzero) and in multiplying
inequalities term by term, which requires nonnegative factors. Without positivity the formula
**fails**: for $A = B = \{-1, 0\}$ we have $\sup A = \sup B = 0$ but $AB = \{1, 0\}$, so
$\sup(AB) = 1 \ne 0 \cdot 0$.

### Solution 17

*Strategy.* (a) is a two-line comparison of upper bounds. (b) needs a strict inclusion that does not
move the supremum: delete a point from the interior.

(a) Since $T \subseteq S$, every upper bound of $S$ is an upper bound of $T$. In particular
$\sup S$ is an upper bound of $T$, so $\sup T \le \sup S$ by definition of supremum.

(b) Take $S = [0,1]$ and $T = (0,1)$. Then $T \subsetneq S$ (for instance $0 \in S \setminus T$).
Both suprema equal $1$: in each case $1$ is an upper bound, and for $\varepsilon > 0$ the element
$1 - \varepsilon/2$ (if positive; for $\varepsilon \ge 2$ any element works) lies in the set and
exceeds $1 - \varepsilon$.

*Remark.* Removing a single point never changes a supremum; removing a *tail* can (compare
$S = \{1/n\}$ and $T = \{1/n : n \ge 2\}$, where $\sup T = 1/2$).

### Solution 18

*Strategy.* Choose the denominator first so that the grid spacing $2^{-k}$ is finer than $y - x$, then
take the first grid point above $x$ using the floor lemma.

Let $x < y$. Since $y - x > 0$, the Archimedean property gives $k \in \mathbb{N}$ with
$$
k > \frac{1}{y-x}, \qquad\text{hence}\qquad 2^k \ge k > \frac{1}{y-x}, \quad\text{so}\quad \frac{1}{2^k} < y - x,
$$
where $2^k \ge k$ is proved by induction. Put $m = \lfloor 2^k x\rfloor + 1 \in \mathbb{Z}$
(Lemma 7.19). Then
$$
m > 2^k x \implies \frac{m}{2^k} > x,
$$
and
$$
m \le 2^k x + 1 < 2^k x + 2^k(y-x) = 2^k y \implies \frac{m}{2^k} < y .
$$
So $d = m/2^k \in D$ lies strictly between $x$ and $y$. $\blacksquare$

*Remark.* The set $D$ is countable (it is a countable union of copies of $\mathbb{Z}$), so this is
another example of a countable set that is spread everywhere.

### Solution 19

*Strategy.* Produce a strictly decreasing sequence of irrationals inside the interval, each time
using Proposition 7.27 on a shorter interval.

Let $x < y$. By Proposition 7.27 there is an irrational $t_1$ with $x < t_1 < y$. Having chosen
irrationals $t_1 > t_2 > \cdots > t_k$ in $(x,y)$, the interval $(x, t_k)$ is nonempty because
$x < t_k$; Proposition 7.27 gives an irrational $t_{k+1}$ with $x < t_{k+1} < t_k$. By induction this
produces infinitely many distinct irrationals $t_1 > t_2 > \cdots$ in $(x,y)$. $\blacksquare$

*Why not simply "apply density infinitely often"?* Because the sequence must be constructed
recursively and each step must keep the interval nonempty; the strict decrease guarantees that.

### Solution 20

*Strategy.* Reduce the ceiling to the floor by reflecting: ceilings of $x$ are negatives of floors
of $-x$.

*Existence.* Apply Lemma 7.19 to $-x$: there is $m \in \mathbb{Z}$ with $m \le -x < m+1$. Multiplying
by $-1$ reverses the inequalities:
$$
-m - 1 < x \le -m .
$$
Put $n = -m$. Then $x \le n$, and $n - 1 < x$ gives $n < x + 1$. Hence $x \le n < x+1$.

*Uniqueness.* Suppose $x \le n < x+1$ and $x \le n' < x+1$ with $n \ne n'$; by symmetry take
$n < n'$. Since $n, n'$ are integers, $n' \ge n+1$. But $n \ge x$ gives $n + 1 \ge x+1 > n'$, so
$n' < n+1$: contradiction. Hence $n = n'$. $\blacksquare$

The number $n$ is written $\lceil x\rceil$.

### Solution 21

*Strategy.* Pick one element and squeeze; then analyse the equality case by squeezing every element.

Since $S \ne \varnothing$, choose $s_0 \in S$. By definition of lower and upper bound,
$$
\inf S \le s_0 \le \sup S ,
$$
so $\inf S \le \sup S \le \sup S$.

*Equality case.* Suppose $\inf S = \sup S = \alpha$.
($\Leftarrow$) If $S = \{s\}$ then $\inf S = \sup S = s$.
($\Rightarrow$) For every $s \in S$ we have $\alpha = \inf S \le s \le \sup S = \alpha$, hence
$s = \alpha$. So every element of $S$ equals $\alpha$; since $S \ne \varnothing$, $S = \{\alpha\}$.
$\blacksquare$

### Solution 22

*Strategy.* Monotonicity of $t \mapsto t^2$ on $[0,\infty)$ gives the upper bound; the lower bound
comes from squaring an approximation to $\alpha$ from below.

Let $\alpha = \sup S \ge 0$ (every element of $S$ is $\ge 0$).

*Upper bound.* If $s \in S$ then $0 \le s \le \alpha$, and squaring preserves the inequality on
$[0,\infty)$: $s^2 \le \alpha^2$. So $\alpha^2$ is an upper bound of $\{s^2 : s \in S\}$.

*Least.* Let $\varepsilon > 0$.

*Case $\alpha = 0$:* then $0 \le s \le 0$ for all $s \in S$, so $S = \{0\}$ and
$\sup\{s^2 : s \in S\} = 0 = \alpha^2$.

*Case $\alpha > 0$:* put $\delta = \min\{\alpha/2, \varepsilon/(2\alpha)\} > 0$ and choose $s \in S$
with $s > \alpha - \delta$ (Lemma 7.11). Then $s > \alpha/2 \ge 0$, so squaring is legitimate:
$$
s^2 > (\alpha - \delta)^2 = \alpha^2 - 2\alpha\delta + \delta^2 \ge \alpha^2 - 2\alpha\delta
\ge \alpha^2 - \varepsilon ,
$$
using $2\alpha\delta \le \varepsilon$. So $\sup\{s^2 : s \in S\} = \alpha^2$. $\blacksquare$

## Advanced

### Solution 23

*Strategy.* Repeat the proof of Theorem 7.24 with $3$ in place of $2$: the supremum of the set of
nonnegative numbers with square below $3$ must have square exactly $3$, because either inequality
can be improved by a small rational step.

Let $S = \{t \in \mathbb{R} : t \ge 0,\ t^2 < 3\}$.

*$S$ is nonempty and bounded above.* $0, 1 \in S$. If $t \ge 2$ then $t^2 \ge 4 > 3$, so $2$ is an
upper bound. By (LUB), $\alpha = \sup S$ exists, and $\alpha \ge 1 > 0$.

*$\alpha^2 < 3$ is impossible.* Put $\eta = 3 - \alpha^2 > 0$ and choose $n \in \mathbb{N}$ with
$1/n < \eta/(2\alpha + 1)$ (Corollary 7.15). Then
$$
\left(\alpha + \frac1n\right)^2 = \alpha^2 + \frac{2\alpha}{n} + \frac{1}{n^2}
\le \alpha^2 + \frac{2\alpha + 1}{n} < \alpha^2 + \eta = 3 ,
$$
so $\alpha + 1/n \in S$, contradicting that $\alpha$ is an upper bound of $S$.

*$\alpha^2 > 3$ is impossible.* Put $\zeta = \alpha^2 - 3 > 0$ and choose $n$ with $2\alpha/n < \zeta$.
Then
$$
\left(\alpha - \frac1n\right)^2 = \alpha^2 - \frac{2\alpha}{n} + \frac{1}{n^2}
> \alpha^2 - \zeta = 3 .
$$
If $t \in S$ and $t \ge \alpha - 1/n > 0$, then $t^2 \ge (\alpha - 1/n)^2 > 3$, contradicting $t \in S$.
So every $t \in S$ satisfies $t < \alpha - 1/n$, i.e. $\alpha - 1/n$ is an upper bound of $S$ strictly
below $\alpha$: contradiction.

Therefore $\alpha^2 = 3$.

*Uniqueness.* If $a, b > 0$ and $a^2 = b^2 = 3$, then $0 = a^2 - b^2 = (a-b)(a+b)$ with $a + b > 0$,
so $a = b$.

*Irrationality.* Suppose $\alpha = p/q$ with $p, q \in \mathbb{Z}$, $q \ge 1$, $\gcd(p,q) = 1$. Then
$p^2 = 3q^2$. Reducing modulo $3$: if $p \equiv 1$ or $2 \pmod 3$ then $p^2 \equiv 1 \pmod 3$, so
$p^2 \equiv 0 \pmod 3$ forces $p \equiv 0 \pmod 3$. Write $p = 3m$; then $9m^2 = 3q^2$, so
$q^2 = 3m^2$, and the same argument gives $3 \mid q$. Hence $3 \mid \gcd(p,q) = 1$, contradiction.
$\blacksquare$

### Solution 24

*Strategy.* (a) is the Archimedean property applied to a hypothetical positive element of the
intersection. (b) shows that closedness is not decorative.

(a) Let $x \in \bigcap_{n\ge1} [0, 1/n]$. Then $x \ge 0$ and $x \le 1/n$ for every $n$. If $x > 0$,
Corollary 7.15 gives $n$ with $1/n < x$, contradicting $x \le 1/n$. Hence $x = 0$. Conversely
$0 \in [0,1/n]$ for every $n$. So the intersection is exactly $\{0\}$.

(b) Take $I_n = (0, 1/n)$. These are nonempty, open, and nested: $I_{n+1} \subseteq I_n$. Their
intersection is empty by the same argument as (a): $x \in \bigcap I_n$ would give $x > 0$ and
$x < 1/n$ for all $n$, hence $n < 1/x$ for all $n$, contradicting the Archimedean property.

The hypothesis that fails is **closedness**: Theorem 7.28 produces the point as $\sup_n a_n$, and
here $\sup_n 0 = 0$ is not an element of any $(0,1/n)$. The lengths shrink to $0$ exactly as in the
theorem; it is the missing endpoints that destroy the conclusion.

### Solution 25

*Strategy.* Mirror the proof of Lemma 7.18: pass to the set of integer upper bounds, which is bounded
below, and take its least element.

Let $\varnothing \ne S \subseteq \mathbb{Z}$ be bounded above by $M \in \mathbb{R}$, and let
$$
T = \{n \in \mathbb{Z} : n \ge s \text{ for every } s \in S\}
$$
be the set of integer upper bounds of $S$.

*$T$ is nonempty.* By Theorem 7.14 choose $k \in \mathbb{N}$ with $k > M$. Then $k > M \ge s$ for
every $s \in S$, so $k \in T$.

*$T$ is bounded below.* Pick $s_0 \in S$. Every $t \in T$ satisfies $t \ge s_0$.

By Lemma 7.18, $T$ has a least element $m$. Since $m \in T$, $m$ is an upper bound of $S$. Since
$m - 1 \notin T$, there is $s_1 \in S$ with $s_1 > m - 1$; as $s_1$ and $m$ are integers,
$s_1 \ge m$. Hence $m \in S$ and $m = \max S$. $\blacksquare$

### Solution 26

*Strategy.* Reduce to subsets of $\mathbb{N}$ via an injection, and use that an infinite subset of
$\mathbb{N}$ is countably infinite (Lemma 7.43).

Let $A$ be countable and $B \subseteq A$.

*Case $A$ finite.* Then $B$ is finite, hence countable.

*Case $A$ countably infinite.* There is a bijection $f : \mathbb{N} \to A$. Then
$B' = f^{-1}(B) \subseteq \mathbb{N}$ and $f$ restricts to a bijection $B' \to B$.

* If $B'$ is finite, then $B$ is finite, hence countable.
* If $B'$ is infinite, Lemma 7.43 gives a bijection $g : \mathbb{N} \to B'$; then $f \circ g$ is a
  bijection $\mathbb{N} \to B$, so $B$ is countably infinite.

In every case $B$ is countable (or finite, which is included in "countable" by Definition 5.7).
$\blacksquare$

### Solution 27

*Strategy.* Write $\mathbb{Q}\times\mathbb{Q}$ as a countable union of countable sets, or as the
image of $\mathbb{N}\times\mathbb{N}$ under a surjection. Both routes use Theorem 7.45.

*Countable.* By Corollary 7.46, $\mathbb{Q}$ is countably infinite, so there is a surjection
$f : \mathbb{N} \to \mathbb{Q}$ (Lemma 7.42). Define
$$
F : \mathbb{N}\times\mathbb{N} \to \mathbb{Q}\times\mathbb{Q}, \qquad F(m,n) = (f(m), f(n)).
$$
For any $(q_1, q_2) \in \mathbb{Q}\times\mathbb{Q}$ choose $m, n$ with $f(m) = q_1$, $f(n) = q_2$;
then $F(m,n) = (q_1,q_2)$. So $F$ is surjective. Since $\mathbb{N}\times\mathbb{N}$ is countable
(Lemma 7.44) and the image of a countable set under a function is countable (Lemma 7.42 applied to
the composite), $\mathbb{Q}\times\mathbb{Q}$ is countable.

*Infinite.* The subset $\mathbb{N}\times\{0\}$ is infinite, so $\mathbb{Q}\times\mathbb{Q}$ is
infinite. A countable infinite set is countably infinite. $\blacksquare$

*Alternative.* $\mathbb{Q}\times\mathbb{Q} = \bigcup_{q\in\mathbb{Q}} \left(\{q\}\times\mathbb{Q}\right)$
is a countable union of countable sets, so Theorem 7.45 applies directly.

### Solution 28

*Strategy.* Cantor's diagonal argument on functions: alter the $n$-th value of the $n$-th function.

*Uncountability.* Suppose $2^{\mathbb{N}} = \{g_1, g_2, g_3, \dots\}$ were a listing. Define
$h : \mathbb{N} \to \{0,1\}$ by
$$
h(n) = 1 - g_n(n).
$$
Then $h \in 2^{\mathbb{N}}$, and for every $n$,
$$
h(n) = 1 - g_n(n) \ne g_n(n),
$$
so $h \ne g_n$. Hence $h$ is not in the list, contradicting that the list contains every element of
$2^{\mathbb{N}}$. Therefore $2^{\mathbb{N}}$ is uncountable.

*Bijection with $\mathcal{P}(\mathbb{N})$.* Define
$$
\Theta : 2^{\mathbb{N}} \to \mathcal{P}(\mathbb{N}), \qquad \Theta(g) = \{n \in \mathbb{N} : g(n) = 1\},
$$
with inverse $A \mapsto \mathbf{1}_A$ (the indicator function). Both maps are well defined:
$\Theta(g) \subseteq \mathbb{N}$, and $\mathbf{1}_A \in 2^{\mathbb{N}}$. Moreover
$\Theta(\mathbf{1}_A) = A$ and $\mathbf{1}_{\Theta(g)} = g$, so the two maps are mutually inverse
bijections. Hence $\lvert 2^{\mathbb{N}}\rvert = \lvert\mathcal{P}(\mathbb{N})\rvert$ and
$\mathcal{P}(\mathbb{N})$ is uncountable — a second proof of Theorem 7.47's corollary in this case.
$\blacksquare$

### Solution 29

*Strategy.* For each degree $n$ the polynomials of degree at most $n$ with integer coefficients form
a countable set, and each contributes finitely many roots. Countable union of finite sets.

*Step 1: polynomial rings are countable.* $\mathbb{Z}^{n+1}$ is countable: $\mathbb{Z}$ is countable
(Corollary 7.46) and a finite product of countable sets is countable (Theorem 7.45 applied by
induction on the number of factors). The set $\mathcal{P}_n$ of polynomials of degree $\le n$ with
integer coefficients is in bijection with $\mathbb{Z}^{n+1}$ via
$(a_0,\dots,a_n) \mapsto a_0 + a_1 t + \cdots + a_n t^n$, so $\mathcal{P}_n$ is countable.

*Step 2: finitely many roots.* A nonzero polynomial of degree $d \ge 1$ has at most $d$ real roots.
(Proof by induction on $d$: if $p(r) = 0$, the factor theorem gives $p(t) = (t - r)q(t)$ with
$\deg q = d - 1$; a root $s \ne r$ of $p$ satisfies $q(s) = 0$, and $q$ has at most $d-1$ roots by
induction.) The zero polynomial is excluded from consideration, and it is the only case in which
infinitely many roots occur.

*Step 3: countable union.* Let $R_n$ be the set of real roots of the nonzero polynomials in
$\mathcal{P}_n$. Each such polynomial contributes at most $n$ roots and there are countably many of
them, so $R_n$ is a countable union of finite sets, hence countable (Theorem 7.45).

*Conclusion.* A real number is algebraic iff it lies in some $R_n$ (a polynomial of degree $d$ lies
in $\mathcal{P}_n$ for every $n \ge d$). Hence the algebraic numbers form
$\bigcup_{n \ge 1} R_n$, a countable union of countable sets, and are countable by Theorem 7.45.
$\blacksquare$

### Solution 30

*Strategy.* Reflect the set: upper bounds of $S$ correspond to lower bounds of $-S$. Reflect back the
infimum.

Let $F$ be an ordered field in which every nonempty set bounded below has a greatest lower bound.
Let $\varnothing \ne S \subseteq F$ be bounded above by $b$. Define
$$
-S = \{-s : s \in S\}.
$$
Then $-S \ne \varnothing$, and $-b$ is a lower bound of $-S$: if $s \le b$ then $-s \ge -b$ (Proposition
7.2(a)). By hypothesis, $-S$ has a greatest lower bound; call it $\gamma$. Put $\alpha = -\gamma$.

*$\alpha$ is an upper bound of $S$.* For $s \in S$ we have $-s \in -S$, so $-s \ge \gamma$, hence
$s \le -\gamma = \alpha$.

*$\alpha$ is least.* Let $u$ be any upper bound of $S$. Then $-u$ is a lower bound of $-S$ (same
computation as above), so $-u \le \gamma$ by definition of greatest lower bound; hence
$u \ge -\gamma = \alpha$.

So $\alpha = \sup S$. Therefore the greatest lower bound property implies the least upper bound
property. $\blacksquare$

## Challenge

### Solution 31

*Strategy.* Compare $[0,1]$ and $(0,1)$: exactly two points must be removed, but infinitely many can
be "absorbed" by a shift along the sequence $1, 1/2, 1/3, \dots$ (Hilbert's hotel).

(a) Define $f : [0,1] \to (0,1)$ by
$$
f(0) = \frac12, \qquad f(1) = \frac13, \qquad f\!\left(\frac1n\right) = \frac{1}{n+2}\ (n \ge 2),
\qquad f(x) = x \ \text{ otherwise}.
$$

*Well defined.* The points $0, 1, 1/2, 1/3, 1/4, \dots$ are distinct, and the formula assigns to each
of them a value in $(0,1)$; every other point is fixed. All values lie in $(0,1)$.

*Injective.* Let $x \ne y$.
* If both are fixed points, $f(x) = x \ne y = f(y)$.
* If $x$ is special and $y$ is fixed, then $f(x) \in \{1/2, 1/3, 1/4, \dots\}$ while $f(y) = y$, and a
  fixed point is by definition neither $0$, nor $1$, nor of the form $1/n$ with $n \ge 2$; so
  $y \notin \{1/2, 1/3, \dots\}$ and $f(x) \ne f(y)$.
* If both are special, the three rules give the distinct values $1/2$, $1/3$ and $1/(n+2)$ for
  $n \ge 2$, i.e. $1/4, 1/5, \dots$; distinct inputs give distinct outputs.

*Surjective.* Let $y \in (0,1)$.
* If $y = 1/2$, then $y = f(0)$.
* If $y = 1/3$, then $y = f(1)$.
* If $y = 1/k$ with $k \ge 4$, then $y = f(1/(k-2))$ and $k - 2 \ge 2$.
* Otherwise $y$ is not of the form $1/k$ ($k \ge 2$) and $y \ne 1/2, 1/3$; then $y$ is a fixed point
  and $y = f(y)$.

Hence $f$ is a bijection.

(b) The inclusion $x \mapsto x$ maps $[0,1]$ into $(0,1)$ but is not surjective, since $0 \mapsto 0$
is outside the codomain; so it is not a bijection. What makes (a) possible is that an infinite set can
be in bijection with a proper subset of itself (here the infinite set $\{0,1,1/2,1/3,\dots\}$ is
shifted onto $\{1/2, 1/3, 1/4, \dots\}$). This is *Dedekind's* definition of infiniteness, and it is
impossible for finite sets: a finite set has more elements than any proper subset. $\blacksquare$

### Solution 32

*Strategy.* Count: there are countably many algebraic numbers and uncountably many reals, so
something must be left over. No specific number is identified.

By Solution 29, the set $A$ of algebraic numbers is countable. By Theorem 7.49 (or Theorem 7.51),
$\mathbb{R}$ is uncountable.

If $\mathbb{R} \setminus A$ were empty, then $\mathbb{R} = A$ would be countable, contradiction.
Hence there is at least one $t \in \mathbb{R} \setminus A$, and such a $t$ is transcendental by
definition.

*Stronger conclusion.* If $\mathbb{R}\setminus A$ were countable, then
$\mathbb{R} = A \cup (\mathbb{R}\setminus A)$ would be a union of two countable sets, hence countable
by Theorem 7.45, contradiction. So there are uncountably many transcendental numbers; the algebraic
numbers are a countable "dust" inside $\mathbb{R}$. $\blacksquare$

*Remark.* This is a pure existence proof. It does not exhibit a transcendental number, and it gives
no information about $e$ or $\pi$; showing those are transcendental requires specific analytic
arguments (Hermite 1873 for $e$, Lindemann 1882 for $\pi$).

### Solution 33

*Strategy.* A cut is determined by its supremum, and every real arises as a supremum of a cut; the
three parts are the existence, the recovery formula, and the two directions of bijectivity.

(a) *Existence of $\sigma(\alpha)$.* Let $\alpha$ be a cut. It is nonempty by (C1). Since
$\alpha \ne \mathbb{Q}$, choose $r \in \mathbb{Q} \setminus \alpha$; then $r$ is an upper bound of
$\alpha$ in $\mathbb{Q}$: if $q \in \alpha$ and $q \ge r$, then (C2) applied to $r \le q$ gives
$r \in \alpha$, contradiction. Hence $\alpha$ is a nonempty subset of $\mathbb{R}$ bounded above, and
$\sigma(\alpha) = \sup\alpha$ exists by (LUB).

(b) *Recovery formula.* Let $x = \sigma(\alpha)$.

($\subseteq$) If $q \in \alpha$ then $q \le x$. If $q = x$, then $x \in \alpha$; but (C3) then gives
$r \in \alpha$ with $r > x$, contradicting that $x$ is an upper bound of $\alpha$. Hence $q < x$.

($\supseteq$) Let $q \in \mathbb{Q}$ with $q < x$. Since $x$ is the *least* upper bound, $q$ is not an
upper bound of $\alpha$; so there is $p \in \alpha$ with $p > q$, and (C2) gives $q \in \alpha$.

Hence $\alpha = \{q \in \mathbb{Q} : q < \sigma(\alpha)\}$.

(c) *$\sigma$ is a bijection.*

*Injectivity.* If $\sigma(\alpha) = \sigma(\beta)$, then by (b)
$$
\alpha = \{q \in \mathbb{Q} : q < \sigma(\alpha)\} = \{q \in \mathbb{Q} : q < \sigma(\beta)\} = \beta .
$$

*Surjectivity.* Let $x \in \mathbb{R}$ and put $\alpha_x = \{q \in \mathbb{Q} : q < x\}$. This is a
cut: it is nonempty (density of $\mathbb{Q}$, Theorem 7.20, applied to $x-1 < x$), it is not all of
$\mathbb{Q}$ (no $q \ge x$ belongs to it), it is downward closed (if $q < x$ and $p < q$ then
$p < x$), and it has no largest element (if $q < x$, density gives $q' \in \mathbb{Q}$ with
$q < q' < x$). Finally $\sigma(\alpha_x) = x$: $x$ is an upper bound, and for $\varepsilon > 0$
density gives $q \in \mathbb{Q}$ with $x - \varepsilon < q < x$, i.e. $q \in \alpha_x$ with
$q > x - \varepsilon$, so no smaller number is an upper bound (Lemma 7.11).

Therefore $\sigma$ is a bijection from cuts onto $\mathbb{R}$. $\blacksquare$

*Remark.* Part (b) says a cut contains exactly the rationals below its supremum, which is why the cut
construction is "the same" as $\mathbb{R}$ once $\mathbb{R}$ is available. In the construction of
$\mathbb{R}$ from $\mathbb{Q}$ the supremum is *not* available, and the union of cuts replaces it
(Theorem 7.38).

### Solution 34

*Strategy.* Positivity of a rational function is an eventual statement about its values, so it is
read off from leading coefficients. Then $t$ beats every natural number.

(a) *Well defined.* Write $f = p/q$ with $p, q \in \mathbb{R}[t]$, $q \ne 0$, and let
$\operatorname{lc}(p)$ denote the leading coefficient (with $\operatorname{lc}(0) = 0$). For real $x$
with $q(x) \ne 0$,
$$
f(x) = \frac{p(x)}{q(x)},
$$
and for all sufficiently large $x$ the sign of $p(x)$ is the sign of $\operatorname{lc}(p)$ and
likewise for $q$. Hence $f(x) > 0$ for all sufficiently large $x$ iff
$\operatorname{lc}(p)\operatorname{lc}(q) > 0$.

This does not depend on the representation: if $p/q = p'/q'$, then $pq' = p'q$ as polynomials, so
comparing leading coefficients, $\operatorname{lc}(p)\operatorname{lc}(q') = \operatorname{lc}(p')\operatorname{lc}(q)$.
Multiplying both sides by $\operatorname{lc}(q)\operatorname{lc}(q')$ gives
$$
\operatorname{lc}(p)\operatorname{lc}(q)\,\operatorname{lc}(q')^2
= \operatorname{lc}(p')\operatorname{lc}(q')\,\operatorname{lc}(q)^2 ,
$$
and since the squares are positive, the two products $\operatorname{lc}(p)\operatorname{lc}(q)$ and
$\operatorname{lc}(p')\operatorname{lc}(q')$ have the same sign.

*Order axioms.* Declare $f > 0$ iff $f(x) > 0$ eventually, and $f < g$ iff $g - f > 0$.

* **O1 (trichotomy).** For $f \ne g$, the function $g - f$ is a nonzero rational function, and
  "eventually positive" holds for exactly one of $g - f$ and $f - g$.
* **O2 (transitivity).** If $f < g$ and $g < h$, then $g - f$ and $h - g$ are eventually positive, so
  their sum $h - f$ is eventually positive.
* **O3 (translation).** $(g + k) - (f + k) = g - f$.
* **O4 (scaling).** If $f < g$ and $0 < h$, then $(g-f)h$ is a product of two eventually positive
  functions, hence eventually positive.

So $F$ is an ordered field with $0 < 1$.

(b) For $n \in \mathbb{N}$, the function $t - n$ satisfies $(t-n)(x) = x - n > 0$ for all $x > n$,
so $t - n > 0$ in the order, i.e. $t > n$. Hence $t$ exceeds every natural number, so $\mathbb{N}$ is
bounded above in $F$ and $F$ is not Archimedean.

(c) The proof of Theorem 7.14 uses only the ordered field axioms and (LUB): if $\mathbb{N}$ were
bounded above, its supremum $\alpha$ would satisfy $n \le \alpha$ for all $n$, hence
$n \le \alpha - 1$ for all $n$, contradicting leastness. Since in $F$ the set $\mathbb{N}$ is bounded
above, $F$ cannot satisfy (LUB). Therefore $F$ is an ordered field that is not complete.

*Moral.* Completeness is not a consequence of the field and order axioms (Proposition 7.9), and it
also forces the Archimedean property; a field with infinitesimals such as $t$ is necessarily
incomplete. $\blacksquare$

### Solution 35

*Strategy.* The numbers $\Phi(S)$ are sums of distinct powers of $1/3$ with digits $0$ or $1$; such
expansions are unique because the tail of the series is too small to make up the difference at the
first differing digit.

*Preliminary estimate.* For every $N \ge 1$,
$$
\sum_{n=1}^{N} 3^{-n} = \frac12\left(1 - 3^{-N}\right) < \frac12 ,
$$
by induction on $N$ (base case $N=1$: $1/3 = \tfrac12(1 - 1/3)$; step: add $3^{-(N+1)}$ to
$\tfrac12(1-3^{-N})$ and simplify). Consequently, for every $n \ge 1$,
$$
\sum_{k=n+1}^{N} 3^{-k} = \frac{1}{2}\left(3^{-n} - 3^{-N}\right) < \frac{3^{-n}}{2} \quad (N > n).
$$

(a) *Existence and bounds.* Let $\mathcal{G}(S)$ be the set of finite subsets of $S$. The value
$\Phi(S)$ is the supremum of the numbers $\sigma(F) := \sum_{n \in F}3^{-n}$ over $F \in \mathcal{G}(S)$.
This set contains $\sigma(\varnothing) = 0$ and is bounded above: if $F \subseteq S$ is finite with
maximum element $N$ (or $F = \varnothing$), then
$$
\sigma(F) \le \sum_{n=1}^{N} 3^{-n} < \frac12 .
$$
So $\Phi(S)$ exists by (LUB) and $0 \le \Phi(S) \le 1/2$.

(b) *Injectivity.* Let $S \ne T$ and let $n = \min(S \triangle T)$, the least index where they differ;
by symmetry assume $n \in S \setminus T$. For $k < n$, membership in $S$ and in $T$ agrees, so
$S \cap \{1,\dots,n-1\} = T \cap \{1,\dots,n-1\}$.

*Lower bound for $\Phi(S)$:* the finite set $F_0 = (S\cap\{1,\dots,n-1\}) \cup \{n\} \subseteq S$ gives
$$
\Phi(S) \ge \sigma(F_0) = \sum_{k \in S,\, k<n} 3^{-k} + 3^{-n}.
$$

*Upper bound for $\Phi(T)$:* for any finite $G \subseteq T$,
$$
\sigma(G) = \sum_{k \in G,\, k<n} 3^{-k} + \sum_{k \in G,\, k>n} 3^{-k}
\le \sum_{k \in T,\, k<n} 3^{-k} + \sum_{k=n+1}^{N_G} 3^{-k}
< \sum_{k \in T,\, k<n} 3^{-k} + \frac{3^{-n}}{2},
$$
where $N_G$ is the largest element of $G$ above $n$ (if there is none, the second sum is $0$), and we
used the preliminary estimate. Taking the supremum over $G$,
$$
\Phi(T) \le \sum_{k \in T,\, k<n} 3^{-k} + \frac{3^{-n}}{2}.
$$

Subtracting, and using $S \cap \{1,\dots,n-1\} = T \cap \{1,\dots,n-1\}$,
$$
\Phi(S) - \Phi(T) \ge 3^{-n} - \frac{3^{-n}}{2} = \frac{3^{-n}}{2} > 0 .
$$
Hence $\Phi(S) \ne \Phi(T)$: the map $\Phi$ is injective.

(c) *Consequences.* An injection $\mathcal{P}(\mathbb{N}) \to \mathbb{R}$ shows
$\lvert\mathcal{P}(\mathbb{N})\rvert \le \lvert\mathbb{R}\rvert$. If $\mathcal{P}(\mathbb{N})$ were
countable, Lemma 7.42 would provide a surjection $\mathbb{N} \to \mathcal{P}(\mathbb{N})$, contradicting
Theorem 7.47. Hence $\mathcal{P}(\mathbb{N})$ is uncountable. $\blacksquare$

*Remark.* The argument is the base-$3$ version of decimal expansion: digits $0$ and $1$ avoid the
ambiguity $0.999\ldots = 1$, which is why base $3$ is used rather than base $2$ with digits $0,1$ and
the number $1$ itself excluded; here $\Phi(S) \le 1/2$, so no ambiguity arises at all.

### Solution 36

*Strategy.* An order isomorphism preserves suprema. But $\mathbb{Q}$ has a bounded nonempty set with
no least upper bound (Theorem 7.6), while $\mathbb{R}$ has none. Transport the bad set across the
isomorphism.

Suppose $f : \mathbb{R} \to \mathbb{Q}$ is a bijection with
$$
x < y \iff f(x) < f(y) \quad \text{for all } x, y \in \mathbb{R}.
$$

*The inverse is order preserving.* If $u, v \in \mathbb{Q}$ with $u < v$, apply the equivalence to
$x = f^{-1}(u)$ and $y = f^{-1}(v)$: $f^{-1}(u) < f^{-1}(v) \iff u < v$. So
$u < v \iff f^{-1}(u) < f^{-1}(v)$.

*Transport the cut.* Let
$$
A = \{q \in \mathbb{Q} : q^2 < 2\}, \qquad B = f^{-1}[A] = \{x \in \mathbb{R} : f(x) \in A\} .
$$
By Theorem 7.6, $A$ is nonempty and bounded above ($2$ is an upper bound) and has no least upper bound
in $\mathbb{Q}$.

$B$ is nonempty (pick $q \in A$ and $x = f^{-1}(q)$) and bounded above: if $b \in B$ then
$f(b) \in A$, so $f(b) < 2$, hence $b < f^{-1}(2)$, using that $f^{-1}$ is order preserving. By
(LUB), $\beta = \sup B$ exists in $\mathbb{R}$.

*$f(\beta)$ is a least upper bound of $A$ in $\mathbb{Q}$.*
* It is an upper bound: for $a \in A$, $f^{-1}(a) \in B$, so $f^{-1}(a) \le \beta$, hence $a \le f(\beta)$.
* It is the least: let $q \in \mathbb{Q}$ be any upper bound of $A$. If $b \in B$ then $f(b) \in A$,
  so $f(b) \le q$, hence $b \le f^{-1}(q)$. Thus $f^{-1}(q)$ is an upper bound of $B$, and
  $\beta \le f^{-1}(q)$, which gives $f(\beta) \le q$.

So $f(\beta) \in \mathbb{Q}$ is the least upper bound of $A$ inside $\mathbb{Q}$, contradicting
Theorem 7.6. Therefore no such order isomorphism exists. $\blacksquare$

*Remark.* The failure is not about cardinality (both sets are infinite, though of different
cardinalities: $\mathbb{R}$ is uncountable, so no bijection exists at all by Theorem 7.49). The
order-theoretic content is stronger: even ignoring cardinality, $\mathbb{Q}$ cannot carry the order
type of $\mathbb{R}$ because a bounded set in $\mathbb{Q}$ may fail to have a least upper bound.

