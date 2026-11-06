# Continuity and Homeomorphisms — Solutions

> [Tutorial](README.md) · [Exercises](exercises.md) · 36 complete solutions

Each solution states the strategy first, then carries it out. Theorems from the
[tutorial](README.md) are cited by number; results from [Topological Spaces](../01-topological-spaces/README.md)
are cited by their topic-1 numbering.

## Beginner

### Solution 1

Let $(a,b)\subseteq\mathbb{R}$ be an open interval. Then

$$
x\in f^{-1}\big[(a,b)\big] \iff a < 3x-2 < b \iff \frac{a+2}{3} < x < \frac{b+2}{3},
$$

so $f^{-1}[(a,b)] = \big(\tfrac{a+2}{3},\tfrac{b+2}{3}\big)$, an open interval. Open intervals form a base
for the usual topology, so by Corollary 7.1.3 the map $f$ is continuous. (Equivalently, the preimage of an
arbitrary open set is a union of such intervals.)

### Solution 2

**(a)** A constant map $f\equiv y_0$ satisfies $f^{-1}[V] = X$ if $y_0\in V$ and $f^{-1}[V] = \varnothing$
otherwise. Both are open, so $f$ is continuous.

**(b)** $\mathrm{id}_X^{-1}[V] = V$ is open for every open $V$.

**(c)** For the inclusion $i : A\hookrightarrow X$ and open $V\subseteq X$, $i^{-1}[V] = V\cap A$, which is
open in the subspace topology by definition. So $i$ is continuous. (By Theorem 7.6.3 of topic 1 it is the
coarsest topology with this property.)

### Solution 3

Let $F\subseteq\mathbb{R}$ be closed. We must show that $f^{-1}[F] = \{x : x^2\in F\}$ is closed, i.e. that
its complement is open. Since $F$ is closed, $\mathbb{R}\setminus F$ is a union of open intervals
$\bigcup_i(a_i,b_i)$. Then

$$
\mathbb{R}\setminus f^{-1}[F] = \{x : x^2\notin F\} = \{x : x^2\in\textstyle\bigcup_i(a_i,b_i)\} = \bigcup_i f^{-1}\big[(a_i,b_i)\big].
$$

By Example 9.1 each $f^{-1}[(a_i,b_i)]$ is open, so the union is open and $f^{-1}[F]$ is closed. Since
this holds for every closed $F$, the closed-set formulation (Theorem 7.1.1) gives continuity.

### Solution 4

**(a)** Let $x\in\overline A$ and let $V$ be an open neighbourhood of $f(x)$. By continuity $f^{-1}[V]$ is an
open neighbourhood of $x$, so it meets $A$. For $a\in A\cap f^{-1}[V]$ we have $f(a)\in V\cap f[A]$, so
every neighbourhood of $f(x)$ meets $f[A]$; hence $f(x)\in\overline{f[A]}$.

**(b)** Let $f = \arctan : \mathbb{R}\to\mathbb{R}$ and $A = \mathbb{R}$. Then $\overline A = \mathbb{R}$ and
$f[\overline A] = (-\pi/2,\pi/2)$, while $\overline{f[A]} = [-\pi/2,\pi/2]$. The endpoints belong to the
closure but are not attained, so the inclusion is strict.

### Solution 5

**(a)** $B^{\circ}$ is open, so $f^{-1}[B^{\circ}]$ is open by continuity; it is contained in $f^{-1}[B]$
because $B^{\circ}\subseteq B$. Since $\big(f^{-1}[B]\big)^{\circ}$ is the largest open subset of
$f^{-1}[B]$ (Theorem 7.9.2 of topic 1), the inclusion follows.

**(b)** Let $f(x) = x^2$ and $B = [0,1]$. Then $B^{\circ} = (0,1)$ and
$f^{-1}[B^{\circ}] = \{x : 0<x^2<1\} = (-1,0)\cup(0,1)$, while
$f^{-1}[B] = [-1,1]$ has interior $(-1,1)$. The inclusion is strict: $0$ is interior to $f^{-1}[B]$ but
$f(0) = 0\notin B^{\circ}$.

### Solution 6

*Claim: $f$ is continuous at every $x_0\ne1$, and discontinuous at $1$.*

If $x_0<1$, then $f = 0$ on the neighbourhood $(-\infty,1)$ of $x_0$, and a constant map is continuous; by
Proposition 7.2.2 (locality), $f$ is continuous at $x_0$. If $x_0>1$, then $f = 1$ on $(1,\infty)$ and the
same argument applies.

At $x_0 = 1$: the open set $V = (\tfrac12,\tfrac32)$ contains $f(1) = 1$, and
$f^{-1}[V] = \{x : f(x) = 1\} = [1,\infty)$, which is not open in $\mathbb{R}$ (the point $1$ is not
interior). So $f$ is discontinuous at $1$ by Definition 5.2.

### Solution 7

**(a)** Let $Y$ have the indiscrete topology, whose only open sets are $\varnothing$ and $Y$. For any
$f : X\to Y$, $f^{-1}[\varnothing] = \varnothing$ and $f^{-1}[Y] = X$ are open in $X$; so $f$ is continuous.

**(b)** Let $X$ be discrete. Every subset of $X$ is open, so $f^{-1}[V]$ is open for every $V\subseteq Y$;
hence $f$ is continuous.

### Solution 8

$\mathrm{id}^{-1}[V] = V$ for every $V\subseteq X$. Hence $\mathrm{id} : (X,\tau_1)\to(X,\tau_2)$ is
continuous iff $V\in\tau_1$ for every $V\in\tau_2$, i.e. iff $\tau_2\subseteq\tau_1$. In words: refining the
domain or coarsening the codomain helps continuity.

### Solution 9

Use the identity $f^{-1}[Y\setminus F] = X\setminus f^{-1}[F]$, valid because $f(x)\in Y\setminus F$ iff
$f(x)\notin F$.

Suppose $f$ is continuous and $F\subseteq Y$ is closed. Then $Y\setminus F$ is open, so
$f^{-1}[Y\setminus F] = X\setminus f^{-1}[F]$ is open, so $f^{-1}[F]$ is closed. Conversely, suppose
preimages of closed sets are closed and let $V\subseteq Y$ be open. Then $Y\setminus V$ is closed, so
$f^{-1}[Y\setminus V] = X\setminus f^{-1}[V]$ is closed, so $f^{-1}[V]$ is open.

### Solution 10

$f$ is injective (if $3x = 3y$ then $x = y$), surjective onto $(0,3)$ (for $t\in(0,3)$ the preimage is
$t/3\in(0,1)$), and continuous (a linear map, or by Solution 1). Its inverse $g(t) = t/3$ is continuous for
the same reason. Hence $f$ is a homeomorphism.

## Intermediate

### Solution 11

**(a) Continuity $\Rightarrow$ closure condition.** This is Solution 4(a).

**Closure condition $\Rightarrow$ continuity.** Assume $f[\overline A]\subseteq\overline{f[A]}$ for all
$A\subseteq X$. By Solution 9 it suffices to show that preimages of closed sets are closed. Let $F\subseteq Y$
be closed and put $A = f^{-1}[F]$. Then

$$
f\big[\overline A\big]\subseteq\overline{f[A]}\subseteq\overline F = F,
$$

so every point of $\overline A$ maps into $F$, i.e. $\overline A\subseteq f^{-1}[F] = A$. Since
$A\subseteq\overline A$ always, $A = \overline A$ is closed.

**(b)** Let $H$ be the step function of Example 9.3 and $A = (-1,0)$. Then $\overline A = [-1,0]$ and
$H[\overline A] = \{H(-1),H(0)\} = \{0,1\}$, while $H[A] = \{0\}$ and $\overline{\{0\}} = \{0\}$. So
$H[\overline A]\not\subseteq\overline{H[A]}$, confirming $H$ is not continuous.

### Solution 12

**Base.** Let $\mathcal{B}$ be a base for $Y$ and suppose $f^{-1}[B]$ is open for every $B\in\mathcal{B}$.
An open $V\subseteq Y$ is a union $\bigcup_i B_i$ of base elements, so
$f^{-1}[V] = \bigcup_i f^{-1}[B_i]$ is a union of open sets.

**Subbase.** Let $\mathcal{S}$ generate the topology with $\bigcup\mathcal{S} = Y$ and suppose $f^{-1}[S]$ is
open for every $S\in\mathcal{S}$. Every open set is a union of finite intersections of members of
$\mathcal{S}$. For $B = S_1\cap\cdots\cap S_k$,

$$
f^{-1}[B] = f^{-1}[S_1]\cap\cdots\cap f^{-1}[S_k]
$$

is a finite intersection of open sets, hence open, and a union of such preimages is open.

### Solution 13

(i) $\Rightarrow$ (ii): an open $V$ containing $f(x_0)$ is a neighbourhood of $f(x_0)$, so (i) gives a
neighbourhood $U$ of $x_0$ with $f[U]\subseteq V$; choose an open $U'\subseteq U$ containing $x_0$, then
$f[U']\subseteq V$.

(ii) $\Rightarrow$ (iii): a basic open set is open.

(iii) $\Rightarrow$ (ii): given open $V\ni f(x_0)$, choose a basic $B$ with $f(x_0)\in B\subseteq V$; by
(iii) there is open $U\ni x_0$ with $f[U]\subseteq B\subseteq V$.

(ii) $\Rightarrow$ (i): a neighbourhood of $f(x_0)$ contains an open one, and (ii) applies to the smaller
set.

For the deduction: $f$ continuous at every point implies continuous by Theorem 7.2.1, and continuous implies
continuous at every point because (i) holds with $U = f^{-1}[V]$.

### Solution 14

**(a)** Suppose $f$ is continuous and let $B\subseteq Y$. By Theorem 7.1.1(c), applied with $A = f^{-1}[B]$,

$$
f\big[\overline{f^{-1}[B]}\big]\subseteq\overline{f\big[f^{-1}[B]\big]}\subseteq\overline B,
$$

so $\overline{f^{-1}[B]}\subseteq f^{-1}[\overline B]$. Conversely, suppose the inequality holds for every
$B$ and let $F\subseteq Y$ be closed. Then $\overline{f^{-1}[F]}\subseteq f^{-1}[\overline F] = f^{-1}[F]$,
so $f^{-1}[F]$ is closed; by Solution 9, $f$ is continuous.

**(b)** Let $H$ be the step function and $B = \{0\}$. Then $f^{-1}[B] = (-\infty,0)$, whose closure is
$(-\infty,0]$, while $f^{-1}[\overline B] = f^{-1}[\{0\}] = (-\infty,0)$. So the inclusion is strict.

### Solution 15

**Lemma.** If $A\subseteq X$ is closed and $G\subseteq A$ is closed in $A$, then $G$ is closed in $X$.
*Proof.* $G = A\cap H$ with $H\subseteq X$ closed, and an intersection of two closed sets is closed.

Now let $F\subseteq Y$ be closed. Then

$$
f^{-1}[F] = \big(f^{-1}[F]\cap A\big)\cup\big(f^{-1}[F]\cap B\big) = (f|_A)^{-1}[F]\cup(f|_B)^{-1}[F].
$$

Since $f|_A$ is continuous, $(f|_A)^{-1}[F]$ is closed in $A$, hence closed in $X$ by the lemma; similarly
$(f|_B)^{-1}[F]$ is closed in $X$. A union of two closed sets is closed, so $f^{-1}[F]$ is closed. As $F$
was arbitrary, $f$ is continuous by Theorem 7.1.1.

### Solution 16

**(a)** Let $X = \bigcup_i U_i$ with $U_i$ open and all $f|_{U_i}$ continuous. For open $V\subseteq Y$,

$$
f^{-1}[V]\cap U_i = (f|_{U_i})^{-1}[V]
$$

is open in $U_i$, hence open in $X$ because $U_i$ is open. Therefore $f^{-1}[V] = \bigcup_i(f^{-1}[V]\cap U_i)$
is open. (No finiteness is used.)

**(b)** On $\mathbb{R}$ put $F_0 = (-\infty,0]$ and $F_n = [1/n,\infty)$ for $n\ge1$. Each $F_n$ is closed
and $\bigcup_{n\ge0}F_n = \mathbb{R}$: indeed every $x>0$ lies in some $F_n$ (take $n>1/x$), and every
$x\le0$ lies in $F_0$. Define $f = 0$ on $F_0$ and $f = 1$ on each $F_n$ with $n\ge1$; this is well defined
because $F_0\cap F_n = \varnothing$ for all $n\ge1$, and the $F_n$ with $n\ge1$ agree on their overlaps.
Every restriction $f|_{F_n}$ is constant, hence continuous, but $f$ is the step function with a jump at $0$,
which is discontinuous (Example 9.3).

### Solution 17

(i) $\Rightarrow$ (ii): if $f$ is a homeomorphism then $f = (f^{-1})^{-1}$ with $f^{-1}$ continuous, so $f$
carries open sets to open sets, i.e. $f$ is open.

(ii) $\Rightarrow$ (i): if $f$ is a continuous open bijection then for open $U\subseteq X$,
$(f^{-1})^{-1}[U] = f[U]$ is open, so $f^{-1}$ is continuous.

(i) $\Rightarrow$ (iii): for closed $F\subseteq X$, $f[F] = (f^{-1})^{-1}[F]$ is closed because $f^{-1}$ is
continuous.

(iii) $\Rightarrow$ (i): if $f$ is a continuous closed bijection then for closed $F\subseteq X$,
$(f^{-1})^{-1}[F] = f[F]$ is closed, so $f^{-1}$ is continuous by Theorem 7.1.1(b).

### Solution 18

**(a)** Let $f : X\to Y$ be continuous and injective, $X$ compact, $Y$ Hausdorff. Then $f[X]$ is a subspace
of a Hausdorff space, hence Hausdorff. The map $f : X\to f[X]$ is a continuous bijection from a compact
space onto a Hausdorff space, so it is a homeomorphism by Theorem 7.6.4. Hence $f$ is an embedding.

**(b)** *Compactness of the domain is needed:* $[0,1)\to S^1$, $t\mapsto e^{2\pi i t}$, is a continuous
injection which is not an embedding (Example 7.6.1); here the domain is not compact.

*Hausdorffness of the codomain is needed:* let $X = \{0,1\}$ be discrete and $Y = \{0,1\}$ indiscrete. The
identity $X\to Y$ is a continuous bijection and $X$ is compact, but it is not a homeomorphism, because
$\{0\}$ is open in $X$ and not in $Y$; the codomain is not Hausdorff.

### Solution 19

**(a)** $[0,1)$ is not compact: the open cover $\{[0,1-1/n) : n\ge2\}$ (open in $[0,1)$ as traces of
$(-1,1-1/n)$) has no finite subcover, since any finite subfamily is contained in some $[0,1-1/N)$. The
circle $S^1$ is compact (it is closed and bounded in $\mathbb{R}^2$, so Heine–Borel applies). Compactness is
a topological invariant, so the two are not homeomorphic.

**(b)** $[0,1]$ is compact and $[0,1)$ is not, by (a).

**(c)** $[0,1]$ is compact and $\mathbb{R}$ is not: the cover $\{(-n,n) : n\in\mathbb{N}\}$ has no finite
subcover.

**(d)** In $\mathbb{N}$ every singleton is open ($\{n\} = \mathbb{N}\cap(n-\tfrac12,n+\tfrac12)$), so every
point is isolated; in $\mathbb{Q}$ no point is isolated, since every interval $(q-\varepsilon,q+\varepsilon)$
contains rationals other than $q$. "Every point is isolated" is a topological property, so the spaces are
not homeomorphic.

### Solution 20

**(a)** Every ray $(-\infty,a)$ and $(a,\infty)$ is usual-open, so the order topology is contained in the
usual topology. Conversely, for $a<b$ the interval $(a,b) = (-\infty,b)\cap(a,\infty)$ is a finite
intersection of subbasic order-open sets, hence order-open; since every usual-open set is a union of open
intervals, the usual topology is contained in the order topology. Hence they are equal.

**(b)** On $\mathbb{Z}$: for $n\in\mathbb{Z}$ the interval $(n-1,n+1)$ equals $\{n\}$, so every singleton is
order-open and the order topology is discrete. On $\mathbb{Q}$: the same argument as in (a) applies, since
rational intervals are the basic sets of the subspace topology and are also order intervals.

### Solution 21

**Statement.** Let $\{(Y_i,\sigma_i)\}_{i\in I}$ be a nonempty family of spaces and $f_i : X\to Y_i$. The
initial topology $\tau$ has subbase $\mathcal{S} = \{f_i^{-1}[V] : i\in I,\ V\in\sigma_i\}$ and satisfies:
for every space $Z$ and map $g : Z\to X$, $g$ is continuous iff every $f_i\circ g$ is continuous.

**Existence.** $\bigcup\mathcal{S} = X$ because $f_i^{-1}[Y_i] = X$ for every $i$, so by the subbase
theorem $\mathcal{S}$ generates a topology $\tau$; each $f_i$ is continuous for it, and any topology making
all $f_i$ continuous contains $\mathcal{S}$, hence contains $\tau$.

**Property.** If $g$ is continuous then each $f_i\circ g$ is a composite of continuous maps. Conversely,
if all $f_i\circ g$ are continuous and $S = f_i^{-1}[V]$ is subbasic, then
$g^{-1}[S] = (f_i\circ g)^{-1}[V]$ is open; by the subbase test (Solution 12), $g$ is continuous.

## Advanced

### Solution 22

**(a)** *Lemma 1.* A closed subset $F$ of a compact space $X$ is compact: given an open cover $\{V_i\}$ of
$F$, add $X\setminus F$ to obtain an open cover of $X$, extract a finite subcover, and discard
$X\setminus F$.

*Lemma 2.* A compact subset $K$ of a Hausdorff space $Y$ is closed: for $y\notin K$ and $x\in K$ choose
disjoint open $U_x\ni x$, $V_x\ni y$; finitely many $U_x$ cover $K$, and the intersection of the
corresponding $V_x$ is an open neighbourhood of $y$ disjoint from $K$.

*Lemma 3.* The continuous image of a compact space is compact: pull an open cover back along $f$, extract a
finite subcover, and push it forward.

Now let $f : X\to Y$ be a continuous bijection with $X$ compact and $Y$ Hausdorff. For closed $F\subseteq X$:
$F$ is compact (Lemma 1), so $f[F]$ is compact (Lemma 3), so $f[F]$ is closed (Lemma 2). Hence $f$ is a
closed map, and a continuous bijection that is closed has continuous inverse: for closed $F\subseteq X$,
$(f^{-1})^{-1}[F] = f[F]$ is closed.

**(b)** *Compactness of $X$:* the map $[0,1)\to S^1$, $t\mapsto e^{2\pi i t}$, is a continuous bijection
which is not a homeomorphism (Example 7.6.1).

*Hausdorffness of $Y$:* the identity from a two-point discrete space to a two-point indiscrete space is a
continuous bijection from a compact space which is not a homeomorphism.

### Solution 23

Suppose $h : \mathbb{R}\to\mathbb{R}^2$ is a homeomorphism and let $x_0 = h^{-1}(0,0)$. Then $h$ restricts
to a homeomorphism $\mathbb{R}\setminus\{x_0\}\to\mathbb{R}^2\setminus\{(0,0)\}$ (the restriction of a
homeomorphism to a subspace and its image is a homeomorphism).

The left-hand space is disconnected: $(-\infty,x_0)$ and $(x_0,\infty)$ are nonempty, disjoint, open in
$\mathbb{R}\setminus\{x_0\}$ and cover it.

The right-hand space is path-connected: given $p,q\ne(0,0)$, if the segment $[p,q]$ does not contain the
origin it is a path from $p$ to $q$; if it does, choose a point $r$ not on the line through $p$ and $q$
(possible since the plane is not a line). Then the segment $[p,r]$ meets the line through $p,q$ only at
$p\ne0$, and $[r,q]$ meets it only at $q\ne0$; so the polygonal path $p\to r\to q$ avoids the origin.

Finally, a path-connected space is connected: if $X = U\cup V$ were a separation and $\gamma$ a path from
$p\in U$ to $q\in V$, then $\gamma^{-1}[U]$ and $\gamma^{-1}[V]$ would be a separation of the connected
interval $[0,1]$.

Connectedness is a topological invariant, so a disconnected space cannot be homeomorphic to a connected
one. Contradiction.

### Solution 24

**(a)** Define $\varphi : X\times Y\to Y\times Y$ by $\varphi(x,y) = (f(x),y)$; it is continuous because both
components are continuous (Proposition 7.1.4). Since $Y$ is Hausdorff, the diagonal $\Delta_Y$ is closed in
$Y\times Y$ (Proposition 7.10.5 of topic 1). Now

$$
\Gamma_f = \{(x,y) : y = f(x)\} = \varphi^{-1}[\Delta_Y],
$$

a closed set.

**(b)** Let $\sigma : X\to X\times Y$, $\sigma(x) = (x,f(x))$. It is continuous (components $\mathrm{id}_X$
and $f$) and its image is $\Gamma_f$. Its inverse is the restriction $\pi_1|_{\Gamma_f}$, which is continuous
as the restriction of a continuous map. Hence $\sigma$ is a homeomorphism onto $\Gamma_f$.

**(c)** Let $f(x) = 1/x$ for $x\ne0$ and $f(0) = 0$. This $f$ is discontinuous at $0$: if it were
continuous there, then taking $\varepsilon = 1$ in the definition of continuity at $0$ would give
$\delta>0$ with $\lvert f(x)\rvert<1$ for $\lvert x\rvert<\delta$, but $\lvert f(x)\rvert = 1/\lvert x\rvert$
is arbitrarily large for small $\lvert x\rvert\ne0$.

Its graph is $\Gamma = \{(x,1/x) : x\ne0\}\cup\{(0,0)\}$, and $\Gamma$ is closed. Indeed, take a point
$(u,v)\notin\Gamma$. If $u\ne0$ and $v\ne1/u$, continuity of $x\mapsto1/x$ near $u$ gives a neighbourhood of
$(u,v)$ meeting $\Gamma$ only possibly at points with $x = u$, i.e. at $(u,1/u)\ne(u,v)$, so a smaller
neighbourhood misses $\Gamma$. If $u = 0$ and $v\ne0$, then $\lvert xy\rvert = 1$ forces
$\lvert y\rvert = 1/\lvert x\rvert>2/\lvert v\rvert$ whenever $\lvert x\rvert<\lvert v\rvert/2$, so the ball
of radius $\lvert v\rvert/2$ about $(0,v)$ misses $\Gamma$. If $(u,v) = (0,0)$, the
open unit ball about the origin meets $\Gamma$ only at points with $\lvert xy\rvert = 1$ and $\lvert x\rvert<1$,
which forces $\lvert y\rvert>1$; so the unit ball misses $\Gamma$. Hence $\Gamma$ is closed although $f$ is
discontinuous, and the converse of (a) fails.

### Solution 25

**(a) Connected.** Let $f : X\to Y$ be continuous and surjective onto $f[X]$. If $f[X] = U\cup V$ were a
separation with $U,V$ nonempty, disjoint and open in $f[X]$, then $f^{-1}[U]$ and $f^{-1}[V]$ would be
nonempty (surjectivity), disjoint, open in $X$ and would cover $X$ — a separation of $X$, contradiction.

**Path-connected.** If $\gamma$ joins $p$ to $q$ in $X$, then $f\circ\gamma$ joins $f(p)$ to $f(q)$ in
$f[X]$.

**(b)** The interval $[a,b]$ is connected, so $f[[a,b]]$ is a connected subset of $\mathbb{R}$ containing
$f(a)$ and $f(b)$. A connected subset of $\mathbb{R}$ that contains two points contains every point
between them: if $c$ lies between $f(a)$ and $f(b)$ but $c\notin f[[a,b]]$, then
$f[[a,b]]\cap(-\infty,c)$ and $f[[a,b]]\cap(c,\infty)$ would be nonempty disjoint open sets covering
$f[[a,b]]$. Hence $c\in f[[a,b]]$, which is the intermediate value theorem.

### Solution 26

**(a)** Suppose $f(x)\ne g(x)$ for some $x\in X$. Choose disjoint open $U\ni f(x)$ and $V\ni g(x)$, which is
possible because $Y$ is Hausdorff. Then $W = f^{-1}[U]\cap g^{-1}[V]$ is an open neighbourhood of $x$, so
$W\cap D\ne\varnothing$ because $D$ is dense. At $d\in W\cap D$ we have $f(d)\in U$ and $g(d)\in V$, but
$f(d) = g(d)$, contradicting $U\cap V = \varnothing$.

**(b)** Let $S = \{0,1\}$ be the Sierpiński space with open sets $\varnothing,\{1\},S$, and let $D = \{1\}$,
which is dense in $S$ (its only closed superset is $S$). Define $f = \mathrm{id}_S$ and $g\equiv1$. Both are
continuous: the identity always is, and constants are continuous. They agree on $D$, but $f(0) = 0\ne1 = g(0)$.
So uniqueness of continuous extensions fails when the target is not Hausdorff.

### Solution 27

**Step 1: $f$ is strictly monotone.** First note that for $x<y<z$ the value $f(y)$ lies strictly between
$f(x)$ and $f(z)$: if, say, $f(x)<f(z)<f(y)$, the intermediate value theorem on $[x,y]$ gives $c\in(x,y)$
with $f(c) = f(z)$, and $c\ne z$, contradicting injectivity; the other orderings are analogous.

Now let $x<y$ and $u<v$ be two pairs of points. Put the four points in increasing order
$x_1\le x_2\le x_3\le x_4$ (if two coincide, the corresponding pair is trivial). Applying the betweenness
property to the consecutive triples $x_1<x_2<x_3$ and $x_2<x_3<x_4$ shows that the three consecutive
differences $f(x_2)-f(x_1)$, $f(x_3)-f(x_2)$, $f(x_4)-f(x_3)$ all have the same sign. Hence
$\operatorname{sign}(f(y)-f(x)) = \operatorname{sign}(f(v)-f(u))$ for any two pairs whose four points are
distinct, and the same conclusion holds when the pairs share a point or one pair contains the other, by
inserting one further point beyond both and comparing consecutive differences along the resulting chain.
Hence all pairs have the same sign: $f$ is either strictly increasing or strictly decreasing.

**Step 2: the inverse is continuous.** Suppose $f$ is strictly increasing (the decreasing case is similar).
Let $y = f(x)$ and $\varepsilon>0$. Put $a = f(x-\varepsilon)$ and $b = f(x+\varepsilon)$; by strict
monotonicity $a<y<b$. By the intermediate value theorem, $f$ maps $[x-\varepsilon,x+\varepsilon]$ onto
$[a,b]$, so

$$
(f^{-1})^{-1}\big[(x-\varepsilon,x+\varepsilon)\big]\supseteq (a,b),
$$

i.e. $f^{-1}[(a,b)]\subseteq(x-\varepsilon,x+\varepsilon)$. Hence $f^{-1}$ is continuous at $y$ (using the
basic-open criterion of Solution 13). As $y$ was arbitrary, $f^{-1}$ is continuous, and $f$ is a
homeomorphism.

### Solution 28

**(a)** Define $w : S^1\setminus\{1\}\to\mathbb{R}$ by $w(z) = i\dfrac{1+z}{1-z}$. For $\lvert z\rvert = 1$,
$z\ne1$,

$$
\overline{w(z)} = -i\frac{1+\bar z}{1-\bar z} = -i\frac{1+1/z}{1-1/z} = -i\frac{z+1}{z-1} = i\frac{1+z}{1-z} = w(z),
$$

so $w(z)\in\mathbb{R}$. Conversely, for $w\in\mathbb{R}$ the formula $z = \dfrac{w-i}{w+i}$ gives a point of
$S^1\setminus\{1\}$ (it has modulus $1$ because $\lvert w-i\rvert = \lvert w+i\rvert$ for real $w$, and it
is not $1$ because $w-i\ne w+i$), and the two formulas are mutually inverse. Both are continuous rational
functions with nonvanishing denominators, so $w$ is a homeomorphism.

**(b)** For $z\in S^1$, the space $S^1\setminus\{z\}$ is homeomorphic to $S^1\setminus\{1\}\cong\mathbb{R}$
(rotation), hence connected. So $S^1$ has no cut points. In $[0,1]$ every interior point $t$ is a cut point:
$[0,1]\setminus\{t\} = [0,t)\cup(t,1]$ is a separation into nonempty open (in the subspace) sets. Since
homeomorphisms carry cut points to cut points, $[0,1]$ and $S^1$ are not homeomorphic.

### Solution 29

Let $p : S^1\to S^1/{\sim}$ be the quotient map and $q(z) = z^2$. Since $q(z) = q(z')$ iff $z' = \pm z$, the
map $q$ is constant on fibres of $p$, so there is a well-defined map $\bar q : S^1/{\sim}\to S^1$ with
$\bar q\circ p = q$.

*$\bar q$ is continuous.* By the characteristic property of the quotient topology (Theorem 7.8.3),
$\bar q$ is continuous iff $\bar q\circ p = q$ is, and $q$ is continuous (a polynomial in $z$).

*$\bar q$ is bijective.* Surjective because $q$ is; injective because $q(z) = q(z')$ forces $z' = \pm z$,
i.e. $[z'] = [z]$.

*Conclusion.* $S^1/{\sim}$ is compact, being the continuous image of the compact space $S^1$ under $p$; $S^1$
is Hausdorff. By Theorem 7.6.4 the continuous bijection $\bar q$ is a homeomorphism.

### Solution 30

Let $\tau,\tau'$ both satisfy the stated property. Since $\tau$ is an initial topology for the family
$(f_i)$, each $f_i : (X,\tau)\to Y_i$ is continuous; likewise for $\tau'$.

Consider $g = \mathrm{id}_X$ as a map $(X,\tau')\to(X,\tau)$. Each composite $f_i\circ g = f_i$ is continuous
as a map $(X,\tau')\to Y_i$. By the property of $\tau$, $g$ is continuous; by Solution 8, continuity of the
identity means $\tau\subseteq\tau'$.

Interchanging the roles of $\tau$ and $\tau'$ gives $\tau'\subseteq\tau$. Hence $\tau = \tau'$. The same
argument, with the arrows reversed, proves uniqueness of a topology satisfying the characteristic property
of a final topology.

### Solution 31

Let $F\subseteq Y$ be closed. We show that $X\setminus f^{-1}[F]$ is open. Let $x\in X\setminus f^{-1}[F]$.
By local finiteness choose an open neighbourhood $W$ of $x$ and a finite set $I_x\subseteq I$ such that
$W\cap F_i = \varnothing$ for $i\notin I_x$.

Since $x\in X = \bigcup_i F_i$, some $F_j$ with $j\in I_x$ contains $x$; in particular the set
$K = \{i\in I_x : x\in F_i\}$ is nonempty. For each $i\in K$, the set $F_i\setminus f^{-1}[F]$ is open in the
subspace $F_i$ (it is $(f|_{F_i})^{-1}[Y\setminus F]$), so there is an open $O_i\subseteq X$ with
$O_i\cap F_i = F_i\setminus f^{-1}[F]$; in particular $x\in O_i$.

Put $O = W\cap\bigcap_{i\in K}O_i$, an open neighbourhood of $x$. We claim $O\cap f^{-1}[F] = \varnothing$.
If $y\in O\cap f^{-1}[F]$, then $y\in F_j$ for some $j$. Since $y\in W$ and $W$ meets only the $F_i$ with
$i\in I_x$, we have $j\in I_x$. Then $y\in O_j\cap F_j = F_j\setminus f^{-1}[F]$, contradicting
$y\in f^{-1}[F]$. So $O\subseteq X\setminus f^{-1}[F]$, which is therefore open. Hence $f^{-1}[F]$ is closed
for every closed $F$, and $f$ is continuous.

## Challenge

### Solution 32

Let $(A,<_A)$ and $(B,<_B)$ be countable dense linear orders without endpoints, enumerated as
$a_0,a_1,\dots$ and $b_0,b_1,\dots$.

**Construction.** We build finite partial order isomorphisms $p_0\subseteq p_1\subseteq\cdots$, each a
bijection between a finite subset of $A$ and a finite subset of $B$, preserving $<$ in both directions.
Start with $p_0 = \varnothing$. At stage $2n$, if $a_n$ is already in the domain of $p_{2n}$, set
$p_{2n+1} = p_{2n}$; otherwise set $p_{2n+1} = p_{2n}\cup\{(a_n,b)\}$ where $b\in B$ is chosen so that
$p_{2n+1}$ is order preserving. Such a $b$ exists: the finite set $\operatorname{dom}(p_{2n})$ splits into
those elements below $a_n$ and those above; their images under $p_{2n}$ have, respectively, a maximum $b^-$
and a minimum $b^+$ (or are empty). Density of $B$ and the absence of endpoints provide an element $b$ with
$b^-<_B b<_B b^+$ (with the obvious interpretation when one side is empty). At stage $2n+1$, symmetrically,
ensure that $b_n$ lies in the range by adding a suitable preimage in $A$.

**Conclusion.** The union $p = \bigcup_n p_n$ is a well-defined function $A\to B$: each stage extends the
previous one, and every $a_n$ enters the domain at stage $2n$ and every $b_n$ enters the range at stage
$2n+1$. It preserves the order in both directions because each $p_n$ does and any two elements appear
together at some finite stage. Hence $p$ is an order isomorphism.

**Deduction.** Two countable dense subsets $A,B\subseteq\mathbb{R}$ without endpoints are countable dense
linear orders without endpoints, so they are order-isomorphic; by Remark 7.7.4 an order isomorphism is a
homeomorphism for the order topologies. For a dense $A\subseteq\mathbb{R}$ the order topology and the
subspace topology agree: a subspace-basic set $A\cap(a,b)$ is a union of order intervals $(a',b')\cap A$ with
$a',b'\in A$ (choose $a',b'\in A$ with $a<a'<x<b'<b$ for each $x\in A\cap(a,b)$, using density), and
conversely every order interval is a trace of an open interval of $\mathbb{R}$. So $A$ and $B$ are
homeomorphic as subspaces of $\mathbb{R}$.

### Solution 33

Let $X$ be compact and $f : X\to\mathbb{R}$ continuous.

*$f[X]$ is compact:* the continuous image of a compact space is compact (Lemma 7.6.7).

*$f[X]$ is bounded:* the open cover $\{(-n,n) : n\in\mathbb{N}\}$ of $\mathbb{R}$ pulls back to an open cover
of $f[X]$; a finite subcover gives $f[X]\subseteq(-N,N)$ for some $N$.

*$f[X]$ is closed:* $\mathbb{R}$ is Hausdorff and compact subsets of Hausdorff spaces are closed
(Lemma 7.6.6).

Since $f[X]$ is nonempty (if $X\ne\varnothing$), bounded and closed, the supremum $M = \sup f[X]$ exists by
completeness. For every $\varepsilon>0$ there is $y\in f[X]$ with $M-\varepsilon<y\le M$, so
$M\in\overline{f[X]} = f[X]$. Hence $M = f(x_0)$ for some $x_0\in X$: the maximum is attained. Applying the
same argument to $-f$ gives the minimum. (If $X = \varnothing$ the statement is vacuous.)

### Solution 34

**(a)** *$\mathbb{R}$:* for $p,q\in\mathbb{R}$ the translation $h(x) = x+(q-p)$ is a homeomorphism with
$h(p) = q$ (its inverse is $x\mapsto x-(q-p)$).

*$S^1$:* for $p,q\in S^1$ the rotation $h(z) = (q/p)z$ is continuous with continuous inverse
$z\mapsto(p/q)z$, and $h(p) = q$.

*$\mathbb{Q}$:* the translation $h(x) = x+(q-p)$ maps $\mathbb{Q}$ to $\mathbb{Q}$ bijectively and is a
homeomorphism for the subspace topology.

**(b)** In $[0,1]$ the point $\tfrac12$ is a cut point, since $[0,1]\setminus\{\tfrac12\} =
[0,\tfrac12)\cup(\tfrac12,1]$ is a separation; the point $0$ is not a cut point, since
$[0,1]\setminus\{0\} = (0,1]$ is connected. Cut points are preserved by homeomorphisms, so no homeomorphism
of $[0,1]$ can send $0$ to $\tfrac12$; the space is not homogeneous.

**(c)** By the classification of $1$-manifolds (Theorem 7.9.2), a connected $1$-manifold without boundary is
homeomorphic to $\mathbb{R}$ or to $S^1$, both of which are homogeneous by (a). Homogeneity is a topological
property: if $h : M\to N$ is a homeomorphism and $N$ is homogeneous, then for $p,q\in M$ choose a
homeomorphism $k$ of $N$ with $k(h(p)) = h(q)$, and then $h^{-1}\circ k\circ h$ is a homeomorphism of $M$
carrying $p$ to $q$.

### Solution 35

Suppose $f : S^1\to\mathbb{R}$ is continuous and injective. The circle is compact and $\mathbb{R}$ is
Hausdorff, so by Corollary 7.6.8 the map $f$ is an embedding; hence $f[S^1]$ is homeomorphic to $S^1$.

Now $f[S^1]$ is compact (continuous image of a compact space) and connected (continuous image of a connected
space), and it has more than one point. A nonempty compact connected subset $K\subseteq\mathbb{R}$ is a
closed interval: the identity map on $K$ attains its maximum $b$ and minimum $a$ by the extreme value
theorem, and for $a<c<b$ we must have $c\in K$, since otherwise $K\cap(-\infty,c)$ and $K\cap(c,\infty)$
would be a separation. So $f[S^1] = [a,b]$ with $a<b$.

But $[a,b]$ has cut points: every $c$ with $a<c<b$ gives a separation $[a,c)\cup(c,b]$ of $[a,b]\setminus\{c\}$.
By Solution 28(b), $S^1$ has no cut points. A homeomorphism preserves cut points, so $S^1\not\cong[a,b]$.
Contradiction. Hence no such injection exists.

### Solution 36

Let $\tau$ be the initial topology with respect to the evaluations $\mathrm{ev}_t : C[0,1]\to\mathbb{R}$. A
basic neighbourhood of the zero function has the form

$$
B(t_1,\dots,t_n;\varepsilon) = \{g : \lvert g(t_i)\rvert<\varepsilon \text{ for } i = 1,\dots,n\}
$$

for finitely many points $t_i$ and some $\varepsilon>0$; these sets form a base at $0$ by Theorem 7.8.1.

Suppose, for contradiction, that $\{U_k\}_{k\in\mathbb{N}}$ is a countable neighbourhood base at the zero
function. For each $k$ choose a basic set $B_k = B(t_1^{(k)},\dots,t_{n_k}^{(k)};\varepsilon_k)\subseteq U_k$
and let $F = \bigcup_k\{t_1^{(k)},\dots,t_{n_k}^{(k)}\}$, a countable subset of $[0,1]$. Since $[0,1]$ is
uncountable, choose $t\in[0,1]\setminus F$.

Let $W = \{g : \lvert g(t)\rvert<1\}$, an open neighbourhood of $0$. If some $U_k\subseteq W$, then
$B_k\subseteq W$. But $B_k$ constrains only the points of the finite set
$\{t_1^{(k)},\dots,t_{n_k}^{(k)}\}\subseteq F$, none of which equals $t$. Choose a continuous $g$ with
$g = 0$ on that finite set and $g(t) = 2$: since $t$ is outside the finite set, a piecewise-linear "tent"
peaking at $(t,2)$ and vanishing at the constrained points does the job. Then $g\in B_k$ but $g\notin W$,
contradiction.

So no countable family is a base at $0$, the topology is not first countable, and since every metrisable
space is first countable, it is not metrisable.
