# Metric Spaces — Solutions

> [Metric Spaces](README.md) · Solutions to the 36 problems in [exercises.md](exercises.md)

Each solution begins with the strategy, then verifies every axiom, quantifier and hypothesis. Descriptions of
sets are justified with balls rather than with pictures, and where a statement is false a counterexample is
given with proof.

## Beginner

**1.** *Strategy: check (M1)–(M3) using the corresponding facts for the absolute value, then solve the
inequality $3\lvert x-y\rvert<r$.*

**(M1)** $d(x,y) = 3\lvert x-y\rvert = 0 \iff \lvert x-y\rvert = 0 \iff x=y$.
**(M2)** $d(x,y) = 3\lvert x-y\rvert = 3\lvert y-x\rvert = d(y,x)$.
**(M3)** $d(x,z) = 3\lvert x-z\rvert = 3\lvert (x-y)+(y-z)\rvert \le 3\lvert x-y\rvert + 3\lvert y-z\rvert = d(x,y)+d(y,z)$.

So $d$ is a metric. Its balls are

$$B_r(x) = \{y : 3\lvert x-y\rvert < r\} = \Bigl(x - \frac r3,\ x + \frac r3\Bigr).$$

*Lipschitz equivalence.* Yes: for all $x,y$,

$$\lvert x-y\rvert = \frac13\,d(x,y) \le d(x,y) \le 3\lvert x-y\rvert,$$

so the two metrics control each other with constants $1/3$ and $3$. Consequently they have the same open
sets, the same convergent sequences and the same Cauchy sequences; the map $x\mapsto 3x$ is an isometry from
$(\mathbb{R},\lvert\cdot\rvert)$ onto $(\mathbb{R},d)$.

**2.** *Strategy: reduce the two-coordinate inequality to two scalar triangle inequalities.*

**(M1)** $d_1(x,y) = \lvert x_1-y_1\rvert+\lvert x_2-y_2\rvert = 0$ forces both terms to vanish (they are
non-negative), i.e. $x_1=y_1$ and $x_2=y_2$. The converse is clear. **(M2)** is immediate from
$\lvert a-b\rvert = \lvert b-a\rvert$.

**(M3)** For each coordinate and each choice of points,

$$\lvert x_i - z_i\rvert = \lvert (x_i-y_i)+(y_i-z_i)\rvert \le \lvert x_i-y_i\rvert + \lvert y_i-z_i\rvert .$$

Adding the two inequalities for $i=1,2$ gives $d_1(x,z)\le d_1(x,y)+d_1(y,z)$.

*Ball.* $B_1((0,0)) = \{(x,y) : \lvert x\rvert+\lvert y\rvert < 1\}$, the open diamond with vertices
$(\pm1,0)$, $(0,\pm1)$. It contains $(1/2,1/2)$ but not $(1,0)$ or $(0.6,0.6)$.

**3.** *Strategy: the maximum of two quantities is controlled by their sum and controls each of them.*

**(M1)** $d_\infty(x,y)=0$ iff $\lvert x_i-y_i\rvert=0$ for both $i$ iff $x=y$. **(M2)** immediate.

**(M3)** For each $i$, $\lvert x_i-z_i\rvert\le\lvert x_i-y_i\rvert+\lvert y_i-z_i\rvert\le d_\infty(x,y)+d_\infty(y,z)$.
The right-hand side is an upper bound for both coordinates, so it bounds their maximum:
$d_\infty(x,z)\le d_\infty(x,y)+d_\infty(y,z)$.

*Comparisons.* For each $i$, $\lvert x_i-y_i\rvert^2\le\sum_j\lvert x_j-y_j\rvert^2$, so
$\lvert x_i-y_i\rvert\le d_2(x,y)$ and hence $d_\infty\le d_2$. Conversely
$d_2(x,y)^2 = \sum_i\lvert x_i-y_i\rvert^2 \le 2\,d_\infty(x,y)^2$, so $d_2\le\sqrt2\,d_\infty$.

*Ball.* $B_1((0,0)) = \{(x,y) : \max\{\lvert x\rvert,\lvert y\rvert\}<1\} = (-1,1)\times(-1,1)$, the open
square. Note that $B^{d_2}_1 \subseteq B^{d_\infty}_1 \subseteq B^{d_1}_1$, consistent with the metric
inequalities.

**4.** *Strategy: with the discrete metric every pair of distinct points is at distance $1$, so every ball of
radius $\le1$ is a singleton.*

*Balls.* For $0<r\le1$: $B_r(a) = \{a\}$, $B_r(b)=\{b\}$, $B_r(c)=\{c\}$. For $r>1$: $B_r(a) = X$ (and
likewise for $b,c$), because all distances are at most $1<r$.

*Open sets.* Every singleton is open, since $\{a\} = B_{1/2}(a)$. By (O2), every union of singletons is open,
so all $2^3 = 8$ subsets are open:
$\varnothing$, $\{a\},\{b\},\{c\},\{a,b\},\{a,c\},\{b,c\},X$.

*Closed sets.* A set is closed iff its complement is open; since every subset is open, **every** subset is
closed as well.

*Clopen.* All eight subsets are clopen. In particular this space is disconnected, and it is the standard
example showing that "open" and "closed" are not opposites.

**5.** *Strategy: an open set must contain a ball around each of its points; a closed set must contain the
limit of every convergent sequence inside it.*

| Set | Status | Justification |
|---|---|---|
| $(0,1)$ | open, not closed | every $x\in(0,1)$ has $B_r(x)\subseteq(0,1)$ for $r=\min(x,1-x)$; $1/n\to0\notin(0,1)$, so not closed |
| $[0,1]$ | closed, not open | its complement $(-\infty,0)\cup(1,\infty)$ is open; no ball around $0$ lies in $[0,1]$ |
| $[0,1)$ | neither | no ball around $0$ lies inside; $1-1/n\to1\notin[0,1)$ |
| $\{1/n\}$ | neither | $1/n\to0\notin$ the set, so not closed; no ball around $1/2$ stays inside, so not open |
| $\mathbb{Z}$ | closed, not open | complement $=\bigcup_{n\in\mathbb{Z}}(n,n+1)$ is open; $B_r(0)\not\subseteq\mathbb{Z}$ for any $r>0$ |
| $\mathbb{Q}$ | neither | any ball contains irrationals, so $\mathbb{Q}^{\circ}=\varnothing$; $\overline{\mathbb{Q}}=\mathbb{R}$ by density |
| $\mathbb{R}\setminus\mathbb{Q}$ | neither | balls contain rationals, so the interior is empty; the closure is $\mathbb{R}$ |

**6.** *Strategy: use the subspace criterion — a set is open in $X$ iff it is the intersection of $X$ with an
open set of $\mathbb{R}$.*

$[0,1] = X\cap(-\tfrac12,\tfrac32)$ and $(-\tfrac12,\tfrac32)$ is open in $\mathbb{R}$, so $[0,1]$ is open in
$X$. Similarly $\{2\} = X\cap(\tfrac32,\tfrac52)$, so $\{2\}$ is open in $X$. Directly: in $X$,
$B_{1/2}(2) = \{y\in X : \lvert y-2\rvert<1/2\} = \{2\}$ because $1$ is at distance $1>\tfrac12$; and for
$x\in[0,1]$, $B_{1/2}(x)\cap X\subseteq[0,1]$ (points of $X$ outside $[0,1]$ are exactly $2$, at distance at
least $1$).

Neither is open in $\mathbb{R}$: $B_r(0) = (-r,r)\not\subseteq[0,1]$ for every $r>0$, and $B_r(2)$ contains
points $\ne2$. So **openness is relative to the ambient space**.

**7.** *Strategy: compute the ball and the closed ball from the definition, remembering that the only points
available are those of $X$.*

$B_1(1) = \{y\in X : \lvert y-1\rvert<1\}$. Points of $[0,1]$ satisfying this are those with $y>0$, i.e.
$(0,1]$; the point $2$ has $\lvert 2-1\rvert = 1\not<1$. Hence $B_1(1) = (0,1]$.

*Closure in $X$.* The point $0$ is a limit of points of $(0,1]$ (e.g. $1/n$), so $0\in\overline{B_1(1)}$.
The point $2$ is not: $d(2, (0,1]) = 1$, so $B_{1/2}(2)\cap B_1(1) = \varnothing$. Hence
$\overline{B_1(1)} = [0,1]$.

*Closed ball.* $\overline{B}_1(1) = \{y\in X : \lvert y-1\rvert\le1\} = [0,1]\cup\{2\}$, because
$\lvert 2-1\rvert = 1\le1$.

So $\overline{B_1(1)} = [0,1]\subsetneq[0,1]\cup\{2\} = \overline{B}_1(1)$: **the closure of an open ball can
be a proper subset of the closed ball of the same radius.** In $\mathbb{R}^n$ the two always coincide, which
is why the distinction is easy to miss.

**8.** *Strategy: use the Hausdorff property (Theorem 7.5) for uniqueness; use the definition for
subsequences.*

*Uniqueness.* Suppose $x_n\to x$ and $x_n\to y$ with $x\ne y$. Let $r = d(x,y)/3>0$. The balls $B_r(x)$ and
$B_r(y)$ are disjoint. Convergence gives $N_1$ with $x_n\in B_r(x)$ for $n\ge N_1$ and $N_2$ with
$x_n\in B_r(y)$ for $n\ge N_2$. For $n = \max\{N_1,N_2\}$ the point $x_n$ would lie in both balls, which is
impossible. Hence $x=y$.

*Subsequences.* Let $x_n\to x$ and let $(x_{n_k})_k$ be a subsequence with $n_1<n_2<\cdots$. Given
$\varepsilon>0$, choose $N$ with $d(x_n,x)<\varepsilon$ for $n\ge N$. Then $n_k\ge k$, so for $k\ge N$ we have
$n_k\ge N$ and $d(x_{n_k},x)<\varepsilon$. Hence $x_{n_k}\to x$.

**9.** *Strategy: use the characterisations of the closure as the smallest closed superset and of the
interior as the largest open subset.*

Let $A\subseteq B$.

*Closure.* $B\subseteq\overline B$ and $\overline B$ is closed, so $A\subseteq\overline B$; thus
$\overline B$ is a closed set containing $A$, and by Proposition 7.6(2) the closure $\overline A$ is contained
in every such set. Hence $\overline A\subseteq\overline B$.

*Interior.* $A^{\circ}\subseteq A\subseteq B$ and $A^{\circ}$ is open, so $A^{\circ}$ is an open subset of
$B$; by Proposition 7.6(1), $B^{\circ}$ contains every open subset of $B$. Hence $A^{\circ}\subseteq B^{\circ}$.

*Remark.* The corresponding statements for unions and intersections are not both true in the naive form; see
Exercises 14 and 15.

**10.** *Strategy: use $\partial A = \overline A\setminus A^{\circ}$.*

* $\partial(a,b) = [a,b]\setminus(a,b) = \{a,b\}$.
* $\partial[a,b] = [a,b]\setminus(a,b) = \{a,b\}$.
* $\partial\mathbb{Q} = \mathbb{R}\setminus\varnothing = \mathbb{R}$.
* For $A = \{1/n\}$: $\overline A = A\cup\{0\}$ (Exercise 11) and $A^{\circ} = \varnothing$ (no ball is
 contained in a countable set), so $\partial A = A\cup\{0\}$.

In particular the boundary of a set can be finite, countably infinite, or the entire space, and a set can
equal its own boundary (Exercise 11).

**11.** *Strategy: decide which points have balls inside $A$, and which are limits of sequences in $A$.*

$A = \{1/n : n\in\mathbb{N}\}\cup\{0\}$.

*Interior.* $A^{\circ} = \varnothing$. Indeed, if $x\in A$ and $r>0$, the ball $B_r(x)$ is an interval of
positive length and therefore uncountable, while $A$ is countable; so $B_r(x)\not\subseteq A$.

*Closure.* $\overline A = A$. The complement $\mathbb{R}\setminus A$ is open: if $x\notin A$ and $x\ne0$,
then either $x<0$ (take $r = \lvert x\rvert$) or $x>0$; in the second case $x$ lies strictly between two
consecutive elements $1/(n+1)<x<1/n$ (or above $1$), and the distance to the nearest element of $A$ is
positive, so a ball around $x$ misses $A$. Hence $A$ is closed, i.e. $\overline A = A$.

*Derived set.* $A' = \{0\}$: every ball $B_r(0)$ contains $1/n$ for all large $n$, so $0\in A'$; and no
other point is a limit point, because each $1/n$ is isolated (the ball of radius
$\tfrac12\min\{1/n - 1/(n+1),\, 1/(n-1)-1/n\}$ around $1/n$ meets $A$ only at $1/n$).

*Boundary.* $\partial A = \overline A\setminus A^{\circ} = A$. So $A$ equals its own boundary: it is closed
with empty interior.

**12.** *Strategy: bound each set from a common base point; for the counterexample use the discrete metric,
where small balls are singletons.*

*Finite unions.* Let $A_1,\dots,A_k$ be bounded and fix $x_0\in X$. For each $i$ choose $R_i$ with
$d(x_0,y)\le R_i$ for all $y\in A_i$ (possible because $A_i$ is bounded: pick $y_i\in A_i$ and use
$d(x_0,y)\le d(x_0,y_i)+\operatorname{diam}A_i$; if $A_i=\varnothing$ take $R_i=0$). Then for
$y\in\bigcup_i A_i$, $d(x_0,y)\le\max_i R_i$, so the union is bounded, with diameter at most
$2\max_i R_i$.

*Counterexample.* Let $X$ be an infinite set with the discrete metric. Then $X$ is bounded:
$d(x,y)\le1$ for all $x,y$, so $\operatorname{diam}X = 1$. But $X$ is not totally bounded: take
$\varepsilon = 1/2$. For any $x$, $B_{1/2}(x) = \{x\}$, so a finite union of such balls is a finite set and
cannot equal the infinite set $X$. Hence no finite $\varepsilon$-net exists.

## Intermediate

**13.** *Strategy: for the union, use that a point of the union lies in one member; for the intersection of
closed sets, take complements and use De Morgan.*

*Unions of open sets.* Let $\{U_i\}_{i\in I}$ be open and $U = \bigcup_i U_i$. If $x\in U$ then $x\in U_j$
for some $j$; since $U_j$ is open there is $r>0$ with $B_r(x)\subseteq U_j\subseteq U$. Hence $U$ is open.

*Intersections of closed sets.* Let $\{F_i\}_{i\in I}$ be closed, $F = \bigcap_i F_i$. Then
$X\setminus F = \bigcup_i (X\setminus F_i)$ is a union of open sets, hence open by the previous part; so $F$
is closed.

*Examples.* $\bigcap_{n\ge1}(-1/n,1/n) = \{0\}$ is not open, though each factor is. And
$\bigcup_{n\ge1}[1/n,1] = (0,1]$ is not closed, though each term is closed: the sequence $1/n$ lies in the
union and converges to $0$, which is not in it.

**14.** *Strategy: for the closure identity prove both inclusions, using that the right side is closed; for
the interior, use that $A^{\circ}\cup B^{\circ}$ is an open subset of $A\cup B$.*

*Closure.* Since $A\subseteq A\cup B$, Exercise 9 gives $\overline A\subseteq\overline{A\cup B}$, and likewise
$\overline B\subseteq\overline{A\cup B}$. Hence $\overline A\cup\overline B\subseteq\overline{A\cup B}$.
Conversely, $\overline A\cup\overline B$ is a finite union of closed sets, hence closed (Theorem 7.5), and it
contains $A\cup B$; being a closed superset of $A\cup B$ it contains the smallest one:
$\overline{A\cup B}\subseteq\overline A\cup\overline B$. Therefore equality holds.

*Interior.* $A^{\circ}$ and $B^{\circ}$ are open, so $A^{\circ}\cup B^{\circ}$ is open, and it is contained in
$A\cup B$; by Proposition 7.6(1) it is contained in the largest open subset, namely $(A\cup B)^{\circ}$.

*Strict example.* In $\mathbb{R}$ take $A = [0,1]$, $B = [1,2]$. Then $A\cup B = [0,2]$ and
$(A\cup B)^{\circ} = (0,2)$, while $A^{\circ}\cup B^{\circ} = (0,1)\cup(1,2) = (0,2)\setminus\{1\}$. The
point $1$ shows the inclusion is strict: it is interior to the union but interior to neither piece.

**15.** *Strategy: both inclusions of the interior identity come from "largest open subset"; the closure
inclusion follows from monotonicity.*

*Interior.* $A\cap B\subseteq A$, so $(A\cap B)^{\circ}\subseteq A^{\circ}$ by Exercise 9, and similarly
$(A\cap B)^{\circ}\subseteq B^{\circ}$; hence $(A\cap B)^{\circ}\subseteq A^{\circ}\cap B^{\circ}$.
Conversely $A^{\circ}\cap B^{\circ}$ is open (finite intersection of open sets) and is contained in $A\cap B$,
so it is contained in the interior. Hence equality.

*Closure.* $A\cap B\subseteq A$ gives $\overline{A\cap B}\subseteq\overline A$ and likewise
$\overline{A\cap B}\subseteq\overline B$, so $\overline{A\cap B}\subseteq\overline A\cap\overline B$.

*Strict example.* In $\mathbb{R}$ take $A = \mathbb{Q}$, $B = \mathbb{R}\setminus\mathbb{Q}$. Then
$A\cap B = \varnothing$, so $\overline{A\cap B} = \varnothing$, while
$\overline A\cap\overline B = \mathbb{R}\cap\mathbb{R} = \mathbb{R}$.

*Moral.* Interior behaves well under finite intersections, closure under finite unions; the other two
combinations only give one inclusion.

**16.** *Strategy: use closedness of closures, and the symmetry of the definition in $A$ and its complement.*

*Closed.* $\partial A = \overline A\cap\overline{X\setminus A}$ is an intersection of two closed sets, hence
closed (Theorem 7.5).

*Symmetry.* The definition is symmetric in $A$ and $X\setminus A$, since
$X\setminus(X\setminus A) = A$. Hence $\partial(X\setminus A) = \partial A$ for every $A$. (Equivalently,
$\partial A = \overline A\setminus A^{\circ}$ and $X\setminus A$ has closure $\overline{X\setminus A}$ and
interior $X\setminus\overline A$, which gives the same set.)

*The proposed implication is false.* Take $A = (0,1)$ and $B = (0,2)$, both open in $\mathbb{R}$, with
$A\subseteq B$. Then $\partial A = \{0,1\}$ but $\partial B = \{0,2\}$, so $1\in\partial A$ while
$1\notin\partial B$. What is true is the weaker statement $\partial A\subseteq\overline A\subseteq\overline B$,
and also $\partial A\subseteq \overline B$; the boundary of a smaller set can sit strictly inside a larger one.

**17.** *Strategy: use $\overline A = A\cup A'$ (Proposition 7.7) and the definition of closedness.*

*Limit points.* Suppose $A$ is closed, so $A = \overline A$. If $x\in A'$, then $x\in\overline A = A$ by
Proposition 7.7. Hence $A'\subseteq A$. Conversely, suppose $A'\subseteq A$. Then
$\overline A = A\cup A'\subseteq A$, and since $A\subseteq\overline A$ always, $A = \overline A$, so $A$ is
closed.

*Complements.* By Definition 5.4, $A$ is closed iff $X\setminus A$ is open. Applying this to $X\setminus A$
in place of $A$: $X\setminus A$ is closed iff $X\setminus(X\setminus A) = A$ is open. Combining the two, $A$
is open iff $X\setminus A$ is closed, and $A$ is closed iff $X\setminus A$ is open.

**18.** *Strategy: (⇒) if a ball contained only finitely many points, shrink the radius below all their
distances; (⇐) is immediate.*

**(⇐)** If every ball around $x$ contains infinitely many points of $A$, then in particular each ball contains
a point of $A$ different from $x$ (indeed infinitely many), so $x$ is a limit point.

**(⇒)** Suppose $x$ is a limit point and let $r>0$. Assume for contradiction that $B_r(x)\cap A$ is finite,
say equal to $\{a_1,\dots,a_m\}$ with $a_i\ne x$ for all $i$ (points equal to $x$ may also be in the ball but
are irrelevant). Put

$$s = \min\bigl(\{r\}\cup\{d(x,a_i) : i = 1,\dots,m\}\bigr) > 0 .$$

Then $B_s(x)\cap A = \varnothing$ if $m=0$, and otherwise contains no $a_i$ since $d(x,a_i)\ge s$; in either
case $B_s(x)\cap(A\setminus\{x\}) = \varnothing$, contradicting that $x$ is a limit point. Hence the
intersection is infinite.

The metric hypothesis is used through the strict inequality $d(x,a_i)>0$ for $a_i\ne x$; in a general
topological space the statement can fail.

**19.** *Strategy: bound $\lvert f(x)\rvert\le\lvert x\rvert$ near $0$; elsewhere use a sequence of the other
type of number.*

*At $0$.* For every $x$, $f(x)$ is either $0$ or $x$, so $\lvert f(x)\rvert\le\lvert x\rvert = \lvert x-0\rvert$.
If $x_n\to0$ then $f(x_n)\to0 = f(0)$; by Theorem 7.11(4), $f$ is continuous at $0$.

*At $x_0\ne0$, $x_0\in\mathbb{Q}$.* Choose irrationals $y_n\to x_0$ (density of $\mathbb{R}\setminus\mathbb{Q}$).
Then $f(y_n) = y_n\to x_0 \ne 0 = f(x_0)$, so $f$ is not continuous at $x_0$.

*At $x_0\notin\mathbb{Q}$.* Choose rationals $q_n\to x_0$. Then $f(q_n) = 0\to0\ne x_0 = f(x_0)$, so $f$ is
not continuous at $x_0$.

Hence the set of continuity points of $f$ is exactly $\{0\}$ — a set that is not open. (Compare: the set of
continuity points of a function is always a $G_\delta$; here $\{0\} = \bigcap_n(-1/n,1/n)$ ✓.)

**20.** *Strategy: the inclusion preserves distances, so continuity is immediate; for openness use the
subspace criterion.*

*Continuity.* $d(i(a),i(a')) = d(a,a')$, so $i$ is an isometry and hence continuous (Proposition 7.12);
indeed $\delta = \varepsilon$ works.

*Not open in $X$.* Let $X = \mathbb{R}$, $A = [0,1]$, $U = [0,\tfrac12)$. Then
$U = A\cap(-\tfrac12,\tfrac12)$, so $U$ is open in $A$ by the criterion below; but $U$ is not open in
$\mathbb{R}$, since every ball $B_r(0) = (-r,r)$ contains negative numbers.

*The precise relationship.* For $U\subseteq A$:

$$U \text{ is open in } A \iff \exists\, V\subseteq X \text{ open with } U = A\cap V .$$

(⇒) For each $a\in U$ choose $r_a>0$ with $B^X_{r_a}(a)\cap A\subseteq U$ (possible since $U$ is open in the
subspace metric). Let $V = \bigcup_{a\in U}B^X_{r_a}(a)$, which is open in $X$. Then
$A\cap V = \bigcup_a\bigl(A\cap B^X_{r_a}(a)\bigr)\subseteq U$, and $U\subseteq A\cap V$ because
$a\in A\cap B^X_{r_a}(a)$ for each $a\in U$. Hence $U = A\cap V$.

(⇐) If $U = A\cap V$ with $V$ open and $a\in U$, then $B^X_r(a)\subseteq V$ for some $r>0$, so
$B^A_r(a) = A\cap B^X_r(a)\subseteq A\cap V = U$, proving that $U$ is open in $A$.

**21.** *Strategy: pass to sequences and use the limit laws in $\mathbb{R}$.*

*Sums and products.* Let $x_n\to x$ in $X$. By continuity, $f(x_n)\to f(x)$ and $g(x_n)\to g(x)$ in
$\mathbb{R}$. The limit laws for real sequences give

$$(f+g)(x_n) = f(x_n)+g(x_n)\longrightarrow f(x)+g(x) = (f+g)(x),$$

and similarly $(fg)(x_n) = f(x_n)g(x_n)\to f(x)g(x) = (fg)(x)$. Since this holds for every sequence
$x_n\to x$, Theorem 7.11(4) gives continuity of $f+g$ and $fg$ at every $x$.

*Zero set.* $\{x : f(x)=0\} = f^{-1}\bigl[\{0\}\bigr]$. The set $\{0\}$ is closed in $\mathbb{R}$, so by
Theorem 7.11(3) its preimage under the continuous map $f$ is closed in $X$.

**22.** *Strategy: an isometry preserves distances exactly, so distinctness and invertibility are immediate;
for the counterexample change the topology on one side only.*

*Injectivity.* If $f(x)=f(y)$ then $d(x,y) = \rho(f(x),f(y)) = 0$, so $x=y$ by (M1).

*Inverse.* Let $g = f^{-1}:f(X)\to X$. For $u,v\in f(X)$ write $u=f(x)$, $v=f(y)$; then
$d\bigl(g(u),g(v)\bigr) = d(x,y) = \rho(u,v)$, so $g$ is an isometry, in particular continuous. Hence $f$ is
a homeomorphism onto its image.

*Counterexample.* Let $X_d$ be $\mathbb{R}$ with the discrete metric and $X_u$ be $\mathbb{R}$ with the usual
metric, and let $f = \mathrm{id}$. Then $f$ is continuous: every subset of $X_d$ is open, so every preimage is
open. It is a bijection. But $f^{-1}:X_u\to X_d$ is not continuous, because $\{0\}$ is open in $X_d$ while
$(f^{-1})^{-1}[\{0\}] = \{0\}$ is not open in $X_u$. So a continuous bijection need not be a homeomorphism.

**23.** *Strategy: show that $d(x_n,y_n)$ is a Cauchy sequence in $\mathbb{R}$ by inserting cross terms.*

For $m,n\ge1$, two applications of the triangle inequality give

$$d(x_n,y_n)\le d(x_n,x_m)+d(x_m,y_m)+d(y_m,y_n),$$

so $d(x_n,y_n)-d(x_m,y_m)\le d(x_n,x_m)+d(y_n,y_m)$. Interchanging $m$ and $n$,

$$\bigl\lvert d(x_n,y_n)-d(x_m,y_m)\bigr\rvert\le d(x_n,x_m)+d(y_n,y_m).$$

Let $\varepsilon>0$. Since $(x_n)$ and $(y_n)$ are Cauchy, there is $N$ with $d(x_n,x_m)<\varepsilon/2$ and
$d(y_n,y_m)<\varepsilon/2$ for $m,n\ge N$. Then the left side is $<\varepsilon$ for $m,n\ge N$, so
$(d(x_n,y_n))_n$ is Cauchy in $\mathbb{R}$ and therefore convergent, since $\mathbb{R}$ is complete.

**24.** *Strategy: one direction uses closedness in $X$, the other the uniqueness of limits.*

**(⇒)** Suppose $(A,d)$ is complete. Let $(x_n)$ be a sequence in $A$ converging in $X$ to $x$. Then $(x_n)$ is
Cauchy in $X$, hence Cauchy in $A$ (the metric is the same), so by completeness it converges in $A$ to some
$a\in A$. Limits in $X$ are unique (Exercise 8), so $a = x\in A$. Thus $A$ contains the limit of every
convergent sequence from $A$, i.e. $A$ is closed by Corollary 7.10.

**(⇐)** Suppose $A$ is closed and let $(x_n)$ be Cauchy in $A$. It is Cauchy in $X$, so it converges in $X$ to
some $x$ by completeness of $X$. A convergent sequence's terms lie in $A$, so $x\in\overline A = A$ by
Corollary 7.10. Hence $(x_n)$ converges in $A$. $\blacksquare$

*Remark.* This gives a cheap way to see that $(0,1)$ is not complete: it is not closed in $\mathbb{R}$.

## Advanced

**25.** *Strategy: build a nested sequence of closed balls with radii tending to $0$, sitting inside
$W\cap U_1\cap\cdots\cap U_n$; completeness supplies a point, and closedness keeps it inside each $U_n$.*

Let $(X,d)$ be complete and nonempty and let $U_n$ be open and dense for $n\ge1$. Let $W\subseteq X$ be
nonempty and open; it suffices to produce a point of $W\cap\bigcap_n U_n$.

**Construction.** Since $U_1$ is dense, $U_1\cap W$ is nonempty; it is open. Choose $x_1\in U_1\cap W$ and
$r_1\in(0,1)$ with

$$\overline{B}_{r_1}(x_1)\subseteq U_1\cap W$$

(possible because $U_1\cap W$ is open and nonempty: pick a ball around a point of it and halve the radius).

Given $x_n$ and $r_n$, the set $U_{n+1}\cap B_{r_n}(x_n)$ is nonempty (density of $U_{n+1}$ and the ball is a
nonempty open set) and open. Choose $x_{n+1}$ in it and $r_{n+1}\in(0,r_n/2)$ with

$$\overline{B}_{r_{n+1}}(x_{n+1})\subseteq U_{n+1}\cap B_{r_n}(x_n).$$

**The sequence is Cauchy.** For $m>n$ we have $x_m\in B_{r_n}(x_n)$, so $d(x_m,x_n)<r_n<2^{1-n}$. Given
$\varepsilon>0$, take $n$ with $2^{1-n}<\varepsilon$; then $d(x_m,x_n)<\varepsilon$ for all $m>n\ge n_0$.

**The limit lies in every set.** By completeness, $x_n\to x$ for some $x\in X$. Fix $n\ge1$. For every
$m\ge n+1$ we have $x_m\in\overline{B}_{r_n}(x_n)$, and closed balls are closed (Proposition 7.4), so
$x\in\overline{B}_{r_n}(x_n)\subseteq U_n\cap W$ for $n\ge1$; also $x\in\overline{B}_{r_1}(x_1)\subseteq W$.
Hence $x\in W\cap\bigcap_n U_n$.

Since every nonempty open $W$ meets $\bigcap_n U_n$, that intersection is dense. $\blacksquare$

*Remark.* The hypothesis that the $U_n$ are *open* is used to fit a closed ball inside $U_n\cap W$; the
hypothesis that the balls are *closed* is used when passing to the limit. Dropping either breaks the proof,
and dropping completeness breaks the theorem (in $\mathbb{Q}$ the sets $\mathbb{Q}\setminus\{q_n\}$ are open
and dense with empty intersection).

**26.** *Strategy: if $\mathbb{Q}$ were $G_\delta$, then $\mathbb{R}$ would be the union of two meagre sets,
contradicting Baire.*

Suppose $\mathbb{Q} = \bigcap_{n} U_n$ with each $U_n$ open in $\mathbb{R}$. Since $U_n\supseteq\mathbb{Q}$ and
$\mathbb{Q}$ is dense, each $U_n$ is dense. Hence its complement $F_n = \mathbb{R}\setminus U_n$ is closed with
empty interior, i.e. nowhere dense. Now

$$\mathbb{R}\setminus\mathbb{Q} = \mathbb{R}\setminus\bigcap_n U_n = \bigcup_n(\mathbb{R}\setminus U_n) = \bigcup_n F_n,$$

a countable union of nowhere dense sets, so $\mathbb{R}\setminus\mathbb{Q}$ is meagre. On the other hand
$\mathbb{Q} = \bigcup_{q\in\mathbb{Q}}\{q\}$ is a countable union of singletons, and a singleton is nowhere
dense in $\mathbb{R}$ (its closure is itself, with empty interior), so $\mathbb{Q}$ is meagre. Therefore

$$\mathbb{R} = \mathbb{Q}\cup(\mathbb{R}\setminus\mathbb{Q})$$

is a countable union of nowhere dense sets, i.e. $\mathbb{R}$ is meagre in itself. But $\mathbb{R}$ is
complete and nonempty, so Theorem 7.18 forbids this. Contradiction.

*Deduction.* If $\mathbb{R}\setminus\mathbb{Q} = \bigcup_n F_n$ with each $F_n$ closed, then
$\mathbb{Q} = \bigcap_n(\mathbb{R}\setminus F_n)$ would be a countable intersection of open sets, contradicting
what was just proved. So the irrationals are not an $F_\sigma$.

**27.** *Strategy: if a sequence had no convergent subsequence, every point would have a ball containing only
finitely many of its terms; that gives an open cover with no finite subcover.*

**Theorem.** A compact metric space is sequentially compact.

*Proof.* Let $(x_n)$ be a sequence in the compact space $X$ and suppose it has no convergent subsequence.

*Claim:* for every $x\in X$ there is $r_x>0$ such that $B_{r_x}(x)$ contains $x_n$ for only finitely many $n$.
If not, some $x$ has $B_{1/k}(x)$ containing infinitely many terms for every $k$; choose $n_1$ with
$x_{n_1}\in B_1(x)$, then $n_2>n_1$ with $x_{n_2}\in B_{1/2}(x)$, and so on. The resulting subsequence
satisfies $d(x_{n_k},x)<1/k\to0$, so $x_{n_k}\to x$ — a convergent subsequence, contrary to the assumption.
This proves the claim.

The family $\{B_{r_x}(x)\}_{x\in X}$ is an open cover of $X$ (each $x$ lies in its own ball). By compactness it
has a finite subcover $B_{r_{x_1}}(x_1),\dots,B_{r_{x_m}}(x_m)$. Each member contains only finitely many terms
$x_n$, so their union — which is all of $X$ — contains only finitely many terms. But the sequence has
infinitely many terms, each in $X$. Contradiction. $\blacksquare$

**Counterexample to the converse implication "closed and bounded $\Rightarrow$ compact".** Let $X$ be an
infinite set with the discrete metric. $X$ is bounded ($\operatorname{diam}X=1$) and closed (in itself). Yet
the open cover $\{\{x\}\}_{x\in X}$ consists of open sets (each singleton is a ball of radius $1/2$) and has no
finite subcover: a finite union of singletons is finite, while $X$ is infinite. Hence $X$ is not compact,
though it is closed and bounded. (It is also complete, but not totally bounded — the correct obstruction.)

**28.** *Strategy: if every $1/n$ fails, a sequence of offending points converges to a point of some $U_i$, and
then openness of $U_i$ gives a contradiction.*

**Lemma (Lebesgue number).** Let $X$ be sequentially compact and let $\{U_i\}_{i\in I}$ be an open cover. Then
there is $\varepsilon>0$ such that every ball $B_\varepsilon(x)$ is contained in some $U_i$.

*Proof.* Suppose not. Then for each $n$ there is $x_n$ such that $B_{1/n}(x_n)\nsubseteq U_i$ for every $i$. By
sequential compactness, a subsequence $x_{n_k}$ converges to some $x$. Since $\{U_i\}$ covers, $x\in U_j$;
since $U_j$ is open, $B_r(x)\subseteq U_j$ for some $r>0$. Choose $k$ with $d(x_{n_k},x)<r/2$ and
$1/n_k<r/2$. If $d(y,x_{n_k})<1/n_k$ then

$$d(y,x)\le d(y,x_{n_k})+d(x_{n_k},x)<\frac r2+\frac r2 = r,$$

so $B_{1/n_k}(x_{n_k})\subseteq B_r(x)\subseteq U_j$, contradicting the choice of $x_{n_k}$. $\blacksquare$

**Theorem.** A sequentially compact metric space is compact.

*Proof.* Let $\{U_i\}$ be an open cover with Lebesgue number $\varepsilon>0$ (Lemma). By Theorem 7.21, $X$ is
totally bounded, so there are $y_1,\dots,y_m$ with $X = \bigcup_j B_{\varepsilon/2}(y_j)$. For each $j$, the
ball $B_\varepsilon(y_j)$ is contained in some $U_{i(j)}$ by the Lebesgue property applied at the point $y_j$.
Then

$$X = \bigcup_{j=1}^m B_{\varepsilon/2}(y_j)\subseteq\bigcup_{j=1}^m B_{\varepsilon}(y_j)\subseteq\bigcup_{j=1}^m U_{i(j)},$$

a finite subcover. $\blacksquare$

**29.** *Strategy: extract successively finer subsequences, each contained in a ball of radius $1/k$, and take
the diagonal.*

Let $X$ be complete and totally bounded and let $(x_n)$ be a sequence in $X$.

*Construction.* Set $\bigl(x^{(0)}_n\bigr) = (x_n)$. Given the subsequence $\bigl(x^{(k-1)}_n\bigr)$, cover $X$
by finitely many balls of radius $1/k$; since the subsequence has infinitely many terms, some ball
$B_{1/k}(y_k)$ contains infinitely many of them. Let $\bigl(x^{(k)}_n\bigr)$ list those terms in increasing
order of index — a subsequence of $\bigl(x^{(k-1)}_n\bigr)$.

*The diagonal is Cauchy.* Put $z_k = x^{(k)}_k$. For $m,n\ge k$, both $z_m$ and $z_n$ are terms of
$\bigl(x^{(k)}_n\bigr)$, hence both lie in $B_{1/k}(y_k)$; therefore

$$d(z_m,z_n)\le d(z_m,y_k)+d(y_k,z_n)<\frac2k .$$

Given $\varepsilon>0$, choose $k>2/\varepsilon$; then $d(z_m,z_n)<\varepsilon$ for all $m,n\ge k$. So $(z_k)$
is Cauchy, and by completeness it converges. Hence $(x_n)$ has a convergent subsequence. $\blacksquare$

**30.** *Strategy: prove the theorem via the geometric series, then verify that $T$ is a contraction on the
complete space $\mathbb{R}$ and compute.*

**Theorem (contraction mapping principle).** Let $(X,d)$ be complete and nonempty and $T:X\to X$ satisfy
$d(Tx,Ty)\le q\,d(x,y)$ with $q<1$. Then $T$ has exactly one fixed point $x^{*}$; for every $x_0$ the iterates
$x_{n+1}=Tx_n$ converge to $x^{*}$; and

$$d(x_n,x^{*})\le\frac{q^n}{1-q}\,d(x_1,x_0), \qquad d(x_n,x^{*})\le\frac{q}{1-q}\,d(x_n,x_{n-1}).$$

*Proof.* Uniqueness: if $Tx=x$, $Ty=y$ then $d(x,y)\le q\,d(x,y)$, so $d(x,y)=0$. Existence: by induction
$d(x_{n+1},x_n)\le q^n d(x_1,x_0)$, so for $m>n$

$$d(x_m,x_n)\le\sum_{k=n}^{m-1}d(x_{k+1},x_k)\le\frac{q^n}{1-q}d(x_1,x_0)\longrightarrow0,$$

so $(x_n)$ is Cauchy and converges to some $x^{*}$; then $Tx^{*} = \lim Tx_n = \lim x_{n+1} = x^{*}$ by
continuity of $T$. Letting $m\to\infty$ gives the first estimate; the second follows from
$d(x_{n+1},x^{*})\le q\,d(x_n,x^{*})$. $\blacksquare$

**Application.** Let $T(x) = 1+\tfrac12\sin x$ on $X=\mathbb{R}$, which is complete.

*$T$ is a contraction with $q=\tfrac12$:* by the mean value theorem,
$\lvert\sin x-\sin y\rvert\le\lvert x-y\rvert$, so
$\lvert Tx-Ty\rvert = \tfrac12\lvert\sin x-\sin y\rvert\le\tfrac12\lvert x-y\rvert$.

By the theorem there is exactly one solution of $x = 1+\tfrac12\sin x$, reached from any start. Starting at
$x_0 = 1$:

$$x_1 = 1+\tfrac12\sin 1 \approx 1.420735, \quad
x_2 = 1+\tfrac12\sin x_1 \approx 1.494385, \quad
x_3 = 1+\tfrac12\sin x_2 \approx 1.498541 .$$

*Error bound.* Using the second estimate with $q = \tfrac12$:
$d(x_3,x^{*})\le\frac{1/2}{1/2}\lvert x_3-x_2\rvert = \lvert x_3-x_2\rvert \approx 0.00416$. The true value is
$x^{*}\approx1.49870$, so the actual error $\approx0.00016$ is well inside the certified bound. Using the first
estimate from $x_0=1$: $d(x_3,x^{*})\le\frac{(1/2)^3}{1/2}\cdot\tfrac12\sin1 = \tfrac14\cdot0.4207\approx0.105$,
also valid but much weaker.

**31.** *Strategy: for $\mathbb{R}$, take the supremum of the part of an interval lying in one side of a
separation; for $\mathbb{Q}$, cut between two points at an irrational.*

**$\mathbb{R}$ is connected.** Suppose $\mathbb{R} = U\cup V$ with $U,V$ nonempty, disjoint and open. Pick
$u\in U$, $v\in V$; relabel so that $u<v$. Let $S = [u,v]\cap U$, which is nonempty (it contains $u$) and
bounded above (by $v$), and put $s = \sup S\in[u,v]$.

Since $U$ is closed in $\mathbb{R}$ (its complement $V$ is open) and $s$ is a limit of points of $S\subseteq U$
(namely, points of $S$ tending to the supremum), we get $s\in U$. Hence $s\ne v$ (as $v\in V$), so $s<v$. But
$U$ is open, so there is $r>0$ with $(s-r,s+r)\subseteq U$; then $s+\min(r/2,(v-s)/2)$ belongs to $S$ and
exceeds $s$, contradicting the definition of a supremum. Hence no separation exists.

*Intervals.* If $J$ is an interval and $J = U\cup V$ a separation, apply the same argument with
$S = [u,v]\cap U\cap J$; since $J$ is an interval and $u,v\in J$, the interval $[u,v]\subseteq J$, and the
computation is unchanged.

**Intermediate value theorem.** If $f:[a,b]\to\mathbb{R}$ is continuous and $f(a)<\gamma<f(b)$, then $[a,b]$ is
connected, so $f([a,b])$ is connected by Theorem 7.34; a connected subset of $\mathbb{R}$ is an interval
(because if it contained $p<r$ and a point $q$ between them were missing, the two halves would separate it),
and an interval containing $f(a)$ and $f(b)$ contains $\gamma$. Hence $\gamma = f(c)$ for some $c$.

**$\mathbb{Q}$ is totally disconnected.** Let $C\subseteq\mathbb{Q}$ contain two distinct points $p<q$. Choose
an irrational $r$ with $p<r<q$ (density of the irrationals). Then

$$C\cap(-\infty,r) \quad\text{and}\quad C\cap(r,\infty)$$

are nonempty (they contain $p$ and $q$), disjoint, open in the subspace $C$ (they are $C\cap$ an open set of
$\mathbb{R}$), and their union is $C$ because no point of $C\subseteq\mathbb{Q}$ equals $r$. That is a
separation of $C$. Hence no subset with two or more points is connected, and the only connected subsets are
the singletons.

## Challenge

**32.** *Strategy: $S$ is the closure of the graph $G$ of a continuous function; closures and continuous
images of connected sets are connected. Path-connectedness fails because the oscillation near
$x=0$ is unbounded.*

**(a) $S$ is connected.** Let $G = \{(x,\sin(1/x)) : 0<x\le1\}$. The map $\Phi:(0,1]\to\mathbb{R}^2$,
$\Phi(x) = (x,\sin(1/x))$, is continuous and $(0,1]$ is connected (Proposition 7.33), so $G = \Phi[(0,1]]$ is
connected by Theorem 7.34.

*$S = \overline G$.* First, $S$ is closed: its complement consists of points with $x<0$ (positive distance from
$S$) and points $(x,y)$ with $x>0$ and $y\ne\sin(1/x)$, which have a neighbourhood missing $S$ by continuity of
$\sin(1/x)$ on $(0,1]$. Second, every point $(0,y)$ with $\lvert y\rvert\le1$ is a limit of points of $G$: given
$r>0$, choose $k$ so large that $x_k := 1/(\pi/2 + 2\pi k) < r$; then $(x_k,1)\in G$ and
$\lVert(x_k,1)-(0,y)\rVert<r$ provided $\lvert 1-y\rvert<r$. If $\lvert 1-y\rvert\ge r$, choose instead the
value of $x$ where $\sin(1/x) = y$ — such an $x$ can be found arbitrarily small because $\sin(1/x)$ attains
every value in $[-1,1]$ on each interval where $1/x$ runs through a full period. Hence $(0,y)\in\overline G$,
and $S = G\cup(\{0\}\times[-1,1])\subseteq\overline G\subseteq S$.

*Conclusion.* The closure of a connected set is connected: if $\overline G = U\cup V$ were a separation, then
$G\cap U$ and $G\cap V$ would be disjoint, relatively open in $G$, and nonempty (each of $U,V$ is a nonempty
open set meeting the dense subset $G$), and they would cover $G$ — a separation of $G$, contradiction. Hence
$S$ is connected.

**(b) $S$ is not path-connected.** Suppose $\gamma = (\gamma_1,\gamma_2):[0,1]\to S$ is continuous with
$\gamma(0) = (0,0)$ and $\gamma(1) = (1,\sin1)$; in particular $\gamma_1(1) = 1>0$.

Let $A = \{t\in[0,1] : \gamma_1(t)>0\}$. Then $A$ is nonempty (it contains $1$) and relatively open, and
$t_0 := \inf A$ satisfies $t_0<1$. By continuity, $\gamma_1(t_0) = 0$, and $\gamma_1(t)>0$ for $t\in(t_0,1]$.
For such $t$ the point $\gamma(t)$ must lie in the graph part of $S$ (the only points of $S$ with first
coordinate $>0$ are those of $G$), so

$$\gamma_2(t) = \sin\frac{1}{\gamma_1(t)}, \qquad t\in(t_0,1].$$

Fix $k$ large and put $a_k = 1/(\pi/2+2\pi k)$, $b_k = 1/(3\pi/2+2\pi k)$. The continuous function $\gamma_1$
takes the value $0$ at $t_0$ and the value $1$ at $1$, so by the intermediate value theorem there are
$s_k, t_k\in[t_0,1]$ with $\gamma_1(s_k) = a_k$ and $\gamma_1(t_k) = b_k$. Then

$$\gamma_2(s_k) = \sin(\pi/2+2\pi k) = 1, \qquad \gamma_2(t_k) = \sin(3\pi/2+2\pi k) = -1 .$$

As $k\to\infty$ we have $a_k,b_k\to0$. We claim $s_k,t_k\to t_0$. Indeed, if a subsequence of $(s_k)$ converged
to some $s$, then by continuity of $\gamma_1$ at $s$ we would have $\gamma_1(s) = \lim a_{k} = 0$; but
$\gamma_1>0$ on $(t_0,1]$, so $s = t_0$. Hence every convergent subsequence of $(s_k)$ tends to $t_0$, and
since $(s_k)$ lies in the compact interval $[t_0,1]$, this forces $s_k\to t_0$. The same argument gives
$t_k\to t_0$.

Now $\gamma_2$ is continuous at $t_0$, so $\gamma_2(s_k)\to\gamma_2(t_0)$ and
$\gamma_2(t_k)\to\gamma_2(t_0)$. But $\gamma_2(s_k) = 1$ and $\gamma_2(t_k) = -1$ for all $k$, so the limit
would have to be both $1$ and $-1$. Contradiction.

Hence no continuous path joins $(0,0)$ to $(1,\sin1)$, and $S$ is connected but not path-connected.

**33.** *Strategy: a sequence of continuous functions climbing from $0$ to $1$ on intervals shrinking to
$1/2$; the $L^1$-limit would have to be the step function, which is not continuous.*

For $n\ge2$ define $f_n:[0,1]\to\mathbb{R}$ by

$$f_n(t) = \begin{cases}0, & 0\le t\le\frac12-\frac1n,\\[1mm] \frac n2\bigl(t-\frac12+\frac1n\bigr), & \frac12-\frac1n\le t\le\frac12,\\[1mm] 1, & \frac12\le t\le1.\end{cases}$$

Each $f_n$ is continuous (piecewise linear with matching endpoint values) and $0\le f_n\le1$.

*Cauchy.* For $2\le n<m$, the functions $f_n$ and $f_m$ differ only on $[\tfrac12-\tfrac1n,\tfrac12]$, a set of
length $\tfrac1n$, where the difference is at most $1$. Hence

$$d_1(f_n,f_m) = \int_0^1\lvert f_n-f_m\rvert\le\frac1n\longrightarrow0 .$$

*No continuous limit.* Let $g = \mathbf{1}_{[1/2,1]}$. Since $\lvert g-f_n\rvert\le1$ and the integrand vanishes
off $[\tfrac12-\tfrac1n,\tfrac12]$,

$$d_1(f_n,g)\le\frac1n\longrightarrow0 .$$

Suppose $d_1(f_n,f)\to0$ for some $f\in C[0,1]$. Then
$d_1(f,g)\le d_1(f,f_n)+d_1(f_n,g)\to0$, so $\int_0^1\lvert f-g\rvert = 0$.

For $0<x<\tfrac12$ we have $\lvert f\rvert = \lvert f-g\rvert$ on $[0,x]$, so
$0\le\int_0^x\lvert f\rvert\le\int_0^1\lvert f-g\rvert = 0$; since $\lvert f\rvert$ is continuous, this forces
$f = 0$ on $[0,x]$, hence on $[0,\tfrac12)$. Symmetrically, for $x>\tfrac12$,
$\int_x^1\lvert f-1\rvert = 0$ forces $f = 1$ on $(\tfrac12,1]$. Then
$\lim_{t\to1/2^-}f(t) = 0\ne1 = \lim_{t\to1/2^+}f(t)$, contradicting continuity at $\tfrac12$.

So the Cauchy sequence has no limit in $(C[0,1],d_1)$: the space is not complete. $\blacksquare$

**34.** *Strategy: complementation turns an open cover into a family of closed sets, and "finite subcover" into
"some finite intersection is empty".*

Let $X$ be a metric space.

**(⇒)** Suppose $X$ is compact, and let $\mathcal{F}$ be a family of closed sets with the finite intersection
property. Suppose $\bigcap_{F\in\mathcal{F}}F = \varnothing$. Then the sets $U_F := X\setminus F$, $F\in
\mathcal{F}$, are open and cover $X$ (their union is $X\setminus\bigcap F$). By compactness, finitely many
cover: $X = \bigcup_{j=1}^k U_{F_j}$, which means $\bigcap_{j=1}^k F_j = \varnothing$ — contradicting the
finite intersection property. Hence $\bigcap_{F\in\mathcal{F}}F\ne\varnothing$.

**(⇐)** Suppose every family of closed sets with the finite intersection property has nonempty intersection, and
let $\{U_i\}_{i\in I}$ be an open cover. If it had no finite subcover, then for every finite $J\subseteq I$,
$\bigcup_{i\in J}U_i\ne X$, i.e. $\bigcap_{i\in J}F_i\ne\varnothing$ where $F_i = X\setminus U_i$ are closed.
So $\{F_i\}$ has the finite intersection property; by hypothesis $\bigcap_{i\in I}F_i\ne\varnothing$, i.e.
there is $x\in X$ with $x\notin U_i$ for every $i$ — contradicting that $\{U_i\}$ covers $X$. Hence a finite
subcover exists and $X$ is compact. $\blacksquare$

**35.** *Strategy: take Cauchy sequences as points, quotient by "distance tends to $0$", and define the
distance as a limit; verify well-definedness, the axioms, density of the copy of $X$, and completeness.*

Let $\mathcal{C}$ be the set of Cauchy sequences in $(X,d)$ and define $(x_n)\sim(y_n)$ iff
$d(x_n,y_n)\to0$; this is an equivalence relation (given). Let $\tilde X = \mathcal{C}/\!\sim$ and write
$[x_n]$ for the class, and $\hat d$ for the candidate distance

$$\hat d\bigl([x_n],[y_n]\bigr) = \lim_{n\to\infty}d(x_n,y_n).$$

*The limit exists.* By Exercise 23, $d(x_n,y_n)$ is a Cauchy sequence in $\mathbb{R}$, hence convergent.

*Well defined.* If $x_n\sim x'_n$ and $y_n\sim y'_n$, then
$\lvert d(x_n,y_n)-d(x'_n,y'_n)\rvert\le d(x_n,x'_n)+d(y_n,y'_n)\to0$ (the same estimate as in Exercise 23),
so the limit does not depend on the representatives.

*Metric axioms.* (M1): $\hat d([x_n],[y_n]) = 0$ iff $d(x_n,y_n)\to0$ iff $[x_n]=[y_n]$. (M2) is clear from the
symmetry of $d$. (M3): $d(x_n,z_n)\le d(x_n,y_n)+d(y_n,z_n)$ for each $n$; passing to the limit,
$\hat d([x],[z])\le\hat d([x],[y])+\hat d([y],[z])$.

*Isometric embedding.* For $x\in X$ let $\iota(x)$ be the class of the constant sequence $x,x,\dots$. Then
$\hat d(\iota(x),\iota(y)) = d(x,y)$, so $\iota$ is an isometry onto its image.

*Density.* Let $\alpha = [x_n]$ and $\varepsilon>0$. Since $(x_n)$ is Cauchy, there is $N$ with
$d(x_n,x_N)<\varepsilon$ for $n\ge N$; then $\hat d(\alpha,\iota(x_N)) = \lim_n d(x_n,x_N)\le\varepsilon$. So
$\iota[X]$ is dense in $\tilde X$.

*Completeness.* Let $(\alpha_k)$ be Cauchy in $\tilde X$. By density, choose $y_k\in X$ with
$\hat d(\alpha_k,\iota(y_k))<1/k$. Then

$$d(y_k,y_\ell) = \hat d(\iota(y_k),\iota(y_\ell))\le\hat d(\iota(y_k),\alpha_k)+\hat d(\alpha_k,\alpha_\ell)+\hat d(\alpha_\ell,\iota(y_\ell))<\frac1k+\hat d(\alpha_k,\alpha_\ell)+\frac1\ell,$$

so $(y_k)$ is Cauchy in $X$ and defines a class $\alpha = [y_k]$. Finally,
$\hat d(\alpha_k,\alpha)\le\hat d(\alpha_k,\iota(y_k))+\hat d(\iota(y_k),\alpha)<1/k+\lim_\ell d(y_k,y_\ell)$,
and the second term tends to $0$ as $k\to\infty$ because $(y_k)$ is Cauchy. Hence $\alpha_k\to\alpha$ and
$\tilde X$ is complete.

Therefore $\tilde X$ is a complete metric space containing an isometric dense copy of $X$: the *completion* of
$X$. $\blacksquare$

**36.** *Strategy: apply the contraction principle to $S = T^n$, then transfer the fixed point back to $T$
using the commutation $T\circ T^n = T^n\circ T$; finally show that the full orbit converges by splitting
indices into blocks of length $n$.*

**Uniqueness.** Let $S = T^n$ be a contraction; by Theorem 7.31 it has exactly one fixed point $z$. If
$Tx = x$ then $Sx = T^n x = x$, so $x = z$. Hence $T$ has at most one fixed point.

**Existence.** Let $z$ be the fixed point of $S$. Then
$S(Tz) = T^n(Tz) = T(T^n z) = Tz$, so $Tz$ is also a fixed point of $S$; by uniqueness of the fixed point of
$S$, $Tz = z$. Hence $z$ is a fixed point of $T$, and it is the only one.

**Convergence of the orbit.** Let $x_0\in X$ and $x_k = T^k(x_0)$. The subsequence
$x_{kn} = S^k(x_0)\to z$ by Theorem 7.31. For a general index $k = mn + r$ with $0\le r<n$, we have
$x_{mn+r} = T^{r}(x_{mn})$, and $T^r$ is continuous (a composition of continuous maps, Proposition 7.12), so

$$x_{mn+r} = T^r(x_{mn})\longrightarrow T^r(z) = z .$$

Since every $k$ has the form $mn+r$ with $0\le r<n$ and $mn\to\infty$ as $k\to\infty$, the whole sequence
$x_k\to z$. $\blacksquare$

**$T$ need not be a contraction.** On $X=[0,1]$ (complete) let

$$T(x) = \frac{1}{1+x} .$$

Then $T$ maps $[0,1]$ into $[\tfrac12,1]\subseteq[0,1]$ and is continuous. $T$ is not a contraction:
$T'(x) = -1/(1+x)^2$ satisfies $\lvert T'(0)\rvert = 1$, and for small $\varepsilon>0$,

$$\frac{\lvert T(0)-T(\varepsilon)\rvert}{\lvert 0-\varepsilon\rvert} = \frac{1-\frac{1}{1+\varepsilon}}{\varepsilon} = \frac{1}{1+\varepsilon}\longrightarrow1,$$

so no $q<1$ works. But

$$T^2(x) = \frac{1}{1+\frac{1}{1+x}} = \frac{1+x}{2+x}, \qquad (T^2)'(x) = \frac{1}{(2+x)^2}\le\frac14,$$

so $T^2$ is a contraction with constant $q = \tfrac14$ (by the mean value theorem). Its unique fixed point
solves $x = \frac{1+x}{2+x}$, i.e. $x^2+x-1 = 0$, so $x = \tfrac{\sqrt5-1}{2}\approx0.618$ — the golden ratio
conjugate, which is indeed the fixed point of $T$ since $x = 1/(1+x)$ is the same equation. Theorem 7.31 gives
$\lvert (T^2)^k(x_0)-x^{*}\rvert\le \frac{(1/4)^k}{3/4}\lvert T^2(x_0)-x_0\rvert$, so the even and odd
subsequences converge at a geometric rate, consistent with the conclusion above.
