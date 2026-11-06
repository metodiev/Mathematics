# Connectedness — Solutions

> [Connectedness](README.md) · Solutions to the 36 problems in [exercises.md](exercises.md)

Each solution states the strategy first, then carries out every step. For "decide" problems the answer is
stated explicitly and justified either by the interval theorem or by an exhibited separation; for proof
problems every hypothesis is used explicitly, and where a result of the tutorial is quoted its number is
given.

## Beginner

**1.** *Strategy: by Theorem 7.3.3 a subset of $\mathbb{R}$ is connected exactly when it is an interval; so in
each case look for a triple $a < c < b$ with $a,b \in A$ and $c \notin A$.*

(a) $\{0,1\}$: not an interval ($0<\tfrac12<1$, $\tfrac12 \notin A$), so **disconnected**; indeed the two
singletons are the components.
(b) $[0,1]\cup[2,3]$: not an interval ($1<\tfrac32<2$), **disconnected**; separation
$A\cap(-\infty,\tfrac32)$, $A\cap(\tfrac32,\infty)$.
(c) $[0,2]\setminus\{1\}$: not an interval ($0<1<2$ with $1 \notin A$), **disconnected**.
(d) $\mathbb{Q}\cap(0,1)$: not an interval, because $\tfrac25$ and $\tfrac35$ lie in it while
$\tfrac{\sqrt2}{2} \approx 0.7071$ does not ($\tfrac25 < 0.7071 < \tfrac35$ and $\tfrac{\sqrt2}{2}$ is
irrational), so **disconnected**.
(e) $\mathbb{Z}$: not an interval ($0<\tfrac12<1$), **disconnected**; each $\{n\}$ is clopen in $\mathbb{Z}$.
(f) $(0,1)\cup\{2\}$: not an interval ($\tfrac12<1.5<2$ with $1.5 \notin A$), **disconnected**.
(g) $\mathbb{R}\setminus\mathbb{Z}$: not an interval (take $a = -\tfrac12$, $c = 0$, $b = \tfrac12$: then
$a,b \in A$ but $c = 0 \notin A$), so **disconnected**.
(h) $\{1/n : n\in\mathbb{N}\}$: not an interval ($0 < \tfrac1{100} < \tfrac12$ with $0 \notin A$),
**disconnected**.
(i) $[0,\infty)$: an interval, hence **connected** (and path connected, being convex).
(j) $\mathbb{R}\setminus\mathbb{Q}$: not an interval: $\sqrt2 \approx 1.414$ and $\sqrt2 + 1 \approx 2.414$ are
irrational, and $2$ lies between them but is rational, so $2 \notin A$; **disconnected**.

Only (i) is connected.

**2.** *Strategy: use the definition; a separation requires two non-empty sets, so a space with at most one
point cannot have one.*

If $X = \varnothing$, the only subset is $\varnothing$, so no separation exists. If $X = \{x\}$, the only
subsets are $\varnothing$ and $X$; a separation would need both parts non-empty and disjoint, with union $X$,
which is impossible. For the indiscrete topology the only open sets are $\varnothing$ and $X$, so a separation
(a pair of non-empty open sets) cannot exist. For a discrete space with distinct points $x \neq y$, the set
$\{x\}$ is open (discrete) and closed, and is neither $\varnothing$ nor $X$, so $(\{x\}, X\setminus\{x\})$ is
a separation; a discrete space with at most one point was already treated. $\blacksquare$

**3.** *Strategy: a topology on a two-point set is determined by which singletons are open; the possibilities
are "neither", "both", "$a$ only", "$b$ only".*

The topologies are:

1. $\mathcal{T}_1 = \{\varnothing, X\}$ (indiscrete): **connected**, by Exercise 2.
2. $\mathcal{T}_2 = \{\varnothing,\{a\},\{b\},X\}$ (discrete): **disconnected**, $(\{a\},\{b\})$ is a
   separation.
3. $\mathcal{T}_3 = \{\varnothing,\{a\},X\}$: the clopen sets are $\varnothing$ and $X$, since $\{a\}$ is open
   but not closed (its complement $\{b\}$ is not open) and $\{b\}$ is not open; **connected**.
4. $\mathcal{T}_4 = \{\varnothing,\{b\},X\}$: similarly **connected**.

So exactly one topology on a two-point set is disconnected. $\blacksquare$

**4.** *Strategy: turn $A$ and its complement into a separation.*

Suppose $A \neq X$. Since $A$ is clopen and non-empty, $X\setminus A$ is non-empty (as $A \neq X$), open (as
$A$ is closed) and disjoint from $A$, and $A\cup(X\setminus A) = X$; moreover $A$ is open. Thus
$(A, X\setminus A)$ is a separation of $X$, contradicting connectedness. Hence $A = X$. $\blacksquare$

**5.** *Strategy: list the open and the closed sets and intersect the two lists; then determine path
connectedness by trying to write down paths explicitly.*

The open sets are $\varnothing,\{a\},\{b\},\{a,b\},X$. Their complements give the closed sets:
$X, \{b,c\}, \{a,c\}, \{c\}, \varnothing$. The sets that are both open and closed are therefore only
$\varnothing$ and $X$. By Theorem 7.2.1, $X$ is **connected**, and its only component is $X$.

*Path components.* $X$ is in fact path connected: define $\gamma : [0,1] \to X$ by
$\gamma(t) = a$ for $t \in [0,\tfrac14)$, $\gamma(t) = c$ for $t \in [\tfrac14,\tfrac34]$, and
$\gamma(t) = b$ for $t \in (\tfrac34,1]$. Continuity is checked by pulling back the five open sets:

$$\gamma^{-1}[\{a\}] = [0,\tfrac14), \quad \gamma^{-1}[\{b\}] = (\tfrac34,1], \quad
\gamma^{-1}[\{a,b\}] = [0,\tfrac14)\cup(\tfrac34,1], \quad \gamma^{-1}[X] = [0,1], \quad
\gamma^{-1}[\varnothing] = \varnothing,$$

all of which are open in $[0,1]$. Since every non-empty open set has open preimage, $\gamma$ is continuous,
and it joins $a$ to $b$; the same formula (with the middle value $c$) joins any two distinct points, so $X$
is path connected and has one path component, namely $X$.

*Remark.* Note the role of the non-Hausdorff topology: the path "jumps" to the third point at no cost, because
the only neighbourhood of $c$ is $X$. $\blacksquare$

**6.** *Strategy: $A$ is a finite union of separated intervals; each interval is connected, and distinct
intervals are separated by gaps.*

Each of $[0,1]$, $[2,3]$ and $\{5\}$ is an interval of $\mathbb{R}$, hence connected, and each is path
connected (it is convex). They are pairwise disjoint, so no connected set can meet two of them (Lemma 7.1.2
applied to a separation by a gap), and each is maximal: for instance $[0,1]$ is a component because
$A\cap(-\infty,\tfrac32)$ is clopen in $A$ and equals $[0,1]$. Hence both the components and the path
components are

$$[0,1], \qquad [2,3], \qquad \{5\}.$$

There are three of each. $\blacksquare$

**7.** (a) *Strategy: remove the origin and look at the two signs.*

$\mathbb{R}\setminus\{0\} = (-\infty,0)\cup(0,\infty)$; both sets are open in $\mathbb{R}$ hence in the
subspace, non-empty, disjoint, and their union is the whole space. So $((-\infty,0),(0,\infty))$ is a
separation and $\mathbb{R}\setminus\{0\}$ is **disconnected**, with components $(-\infty,0)$ and $(0,\infty)$.

(b) *Strategy: push radially to the unit circle, then rotate along the circle.*

Fix $z \neq 0$ and let $\rho = \lvert z\rvert > 0$. Define

$$\gamma(t) = z\Bigl((1-t) + \frac{t}{\rho}\Bigr), \qquad 0 \le t \le 1 .$$

The scalar factor $(1-t) + t/\rho$ is a convex combination of $1$ and $1/\rho$, both positive, hence is
positive for every $t$; therefore $\gamma(t) \neq 0$. The path is continuous, starts at $z$ and ends at
$z/\rho = u \in S^1$. Write $u = e^{i\varphi}$ with $\varphi \in [0,2\pi)$ and put
$\delta(s) = e^{i(1-s)\varphi}$, which is continuous, has modulus $1$ (so never vanishes), and joins $u$ to
$1$. The concatenation $\gamma * \delta$ is a path in $\mathbb{C}\setminus\{0\}$ from $z$ to $1$. Since $z$ was
arbitrary and every point can be joined to $1$, $\mathbb{C}\setminus\{0\}$ is **path connected** (Proposition
7.6.3), hence connected. $\blacksquare$

**8.** *Strategy: the fibres of $f$ are clopen, and a connected space cannot be split by a clopen set.*

For $n \in \mathbb{Z}$ the set $f^{-1}[\{n\}]$ is open (continuity, $\{n\}$ open in the discrete topology) and
closed (continuity, $\{n\}$ closed). Suppose $f$ is not constant. Then there are $m \neq n$ in the image, so
$f^{-1}[\{m\}]$ is a non-empty clopen set different from $X$ (it does not contain any point mapping to $n$).
By Proposition 7.1.3, $X$ is disconnected — contradiction. Hence $f$ is constant. $\blacksquare$

**9.** *Strategy: a separation of $Y$ pulls back to one of $X$.*

Let $(U,V)$ be a separation of $Y$. Then $f^{-1}[U]$ and $f^{-1}[V]$ are open in $X$, they are non-empty
(surjectivity: pick $u\in U$, $u = f(x)$ for some $x$, so $x \in f^{-1}[U]$; similarly for $V$), they are
disjoint, and their union is $f^{-1}[Y] = X$. This is a separation of $X$, contradiction. Alternatively quote
Theorem 7.4.1 with $A = X$. $\blacksquare$

**10.** (a) *Strategy: exhibit $S^1$ as a continuous image of $\mathbb{R}$.*

The map $p(t) = e^{2\pi i t} = (\cos 2\pi t, \sin 2\pi t)$ is continuous and surjective onto $S^1$; since
$\mathbb{R}$ is connected (Corollary 7.3.4), $S^1$ is **connected** (Theorem 7.4.1). It is **path connected**:
given $u, v \in S^1$, write $u = e^{2\pi i a}$, $v = e^{2\pi i b}$ and use
$t \mapsto e^{2\pi i((1-t)a + tb)}$.

(b) $S^0 = \{-1\}\cup\{1\}$ is a two-point discrete space, hence **not connected** (Exercise 2) and not path
connected: any path $[0,1]\to S^0$ would have connected image.

(c) $S^1\cup\{0\}$ is **disconnected**: the set $\{0\}$ equals $(S^1\cup\{0\})\cap\{z : \lvert z\rvert < 1\}$,
so it is open in the subspace, and it is also closed (its complement $S^1$ is closed). It is a non-trivial
clopen set, so $(S^1,\{0\})$ is a separation. The space is not path connected either, and its components are
$S^1$ and $\{0\}$. $\blacksquare$

**11.** *Strategy: two connected sets meeting at a point.*

Let $X_0 = \{(x,0) : x \in \mathbb{R}\}$ and $Y_0 = \{(0,y) : y\in\mathbb{R}\}$. Each is homeomorphic to
$\mathbb{R}$ (via $(x,0)\mapsto x$ and $(0,y)\mapsto y$, both continuous with continuous inverse), hence
connected; and $X_0 \cap Y_0 = \{(0,0)\} \neq \varnothing$. By Corollary 7.5.2, $A = X_0\cup Y_0$ is
**connected**. It is path connected: to join $(x,0)$ to $(0,y)$, concatenate the straight segments
$(x,0)\to(0,0)$ and $(0,0)\to(0,y)$, both of which lie in $A$ and are continuous images of $[0,1]$.
$\blacksquare$

## Intermediate

**12.** *Strategy: take a clopen subset of $B$ and show that its trace on $A$ forces it to be $\varnothing$ or
$B$; the hypothesis $B\subseteq\overline A$ enters when we pass from $A$ to $B$.*

Let $C \subseteq B$ be non-empty, open in $B$ and closed in $B$. Then $C\cap A$ is open in $A$ and closed in
$A$, so by the connectedness of $A$ either $C\cap A = \varnothing$ or $C \cap A = A$.

*Case 1: $C\cap A = \varnothing$.* Since $C$ is closed in $B$, there is a closed set $F \subseteq X$ with
$C = B\cap F$. From $C\cap A = \varnothing$ we get $A \subseteq X\setminus F$, and $X\setminus F$ is closed in
$X$, so $\overline A \subseteq X\setminus F$. **Here the hypothesis is used:** $B \subseteq \overline A$, hence
$B \subseteq X\setminus F$ and therefore $C = B\cap F = \varnothing$, contrary to the assumption that $C$ is
non-empty.

*Case 2: $C\cap A = A$.* Then $A \subseteq C \subseteq F$ with $F$ closed, so
$\overline A \subseteq F$; using $B\subseteq\overline A$ again, $B \subseteq F$, hence
$C = B\cap F = B$.

Therefore $B$ has no non-trivial clopen subset and is connected (Theorem 7.2.1). Without the hypothesis the
statement fails: $A = (0,1)$ is connected and $B = (0,1)\cup\{2\}$ has $A \subseteq B$ but $B$ is disconnected.
$\blacksquare$

**13.** (a) *Strategy: a separation puts each piece entirely on one side; a common point forces one side to be
empty.*

Let $A = \bigcup_{i\in I}A_i$ and let $(U,V)$ be a separation of $A$. Each $A_i$ is connected, so by Lemma
7.1.2 $A_i \subseteq U$ or $A_i\subseteq V$. Choose $p \in \bigcap_i A_i$; say $p\in U$. Every $A_i$ contains
$p$, so no $A_i$ is contained in $V$ (as $U\cap V = \varnothing$), hence every $A_i \subseteq U$. Then
$A \subseteq U$, so $V = \varnothing$, contradicting the definition of a separation. Hence $A$ is connected.

(b) *Example.* In $\mathbb{R}$ take $A = \{0\}$ and $B = \{1\}$. Both are connected (singletons), and
$A\cup B = \{0,1\}$ is a two-point discrete space, hence disconnected by Exercise 2. The hypothesis
$A\cap B \neq \varnothing$ in Corollary 7.5.2 is therefore indispensable.

(c) *Strategy: induction, applying (a) or Corollary 7.5.2 at each stage.*

For $n = 1$ there is nothing to prove. Assume the claim for $n-1$ and let $A_1,\dots,A_n$ be connected with
$A_i\cap A_{i+1}\neq\varnothing$. By the induction hypothesis $D = A_1\cup\cdots\cup A_{n-1}$ is connected, and
$D \cap A_n \supseteq A_{n-1}\cap A_n \neq \varnothing$; by Corollary 7.5.2, $D\cup A_n$ is connected.
$\blacksquare$

**14.** *Strategy: for the non-trivial direction, fix one point and use that $X$ is the union of connected sets
all containing it.*

Suppose first that $X$ is connected. Given $x,y\in X$, take $C = X$: it is connected and contains both.

Conversely, suppose that every two points of $X$ lie in a common connected subset. If $X = \varnothing$ it is
connected, so assume $X \neq \varnothing$ and fix $x_0\in X$. For each $y \in X$ let $C_y$ be a connected set
containing $x_0$ and $y$ (it exists by hypothesis). Then $x_0 \in \bigcap_{y}C_y$, so
$X = \bigcup_{y\in X}C_y$ is connected by Theorem 7.5.1.

*Why this is not path connectedness.* The hypothesis gives, for each pair, *some* connected set containing
both — not a continuous path. In the topologist's sine curve every two points do lie in a connected set (the
whole space), yet no path joins the vertical segment to the graph. Path connectedness demands a continuous
image of $[0,1]$, a much stronger and more rigid requirement. $\blacksquare$

**15.** *Strategy: quotients are continuous images; and $\mathbb{R}/\mathbb{Z}$ receives a continuous
surjection from the connected space $\mathbb{R}$.*

A quotient map $q : X \to Y$ is continuous and surjective by definition, so $Y = q[X]$ is a continuous image
of the connected space $X$ and is connected by Theorem 7.4.1 (equivalently Corollary 7.5.5).

For $\mathbb{R}/\mathbb{Z}$: this is the quotient of $\mathbb{R}$ by the equivalence relation $x\sim y$ iff
$x - y \in \mathbb{Z}$, with the quotient topology. The quotient map $q$ is continuous and surjective, so
$\mathbb{R}/\mathbb{Z}$ is connected. (In fact $t \mapsto e^{2\pi i t}$ induces a homeomorphism
$\mathbb{R}/\mathbb{Z}\to S^1$.) $\blacksquare$

**16.** *Strategy: continuous images of connected sets are connected, and connected subsets of $\mathbb{R}$ are
intervals.*

$X$ is connected, so $f[X]$ is connected (Theorem 7.4.1); being a subset of $\mathbb{R}$, it is an interval
(Theorem 7.3.3). If $y$ lies between $f(a)$ and $f(b)$, both of which are elements of the interval $f[X]$,
then $y \in f[X]$, i.e. $y = f(x)$ for some $x \in X$. $\blacksquare$

**17.** *Strategy: show that every fibre is clopen; a connected space cannot be partitioned by a non-trivial
clopen set.*

For $y \in Y$ let $F_y = f^{-1}[\{y\}]$. If $x \in F_y$, local constancy gives an open neighbourhood $U_x$ of
$x$ with $f$ constant on $U_x$; that constant must be $f(x) = y$, so $U_x \subseteq F_y$. Hence
$F_y = \bigcup_{x\in F_y}U_x$ is open. The fibres $\{F_y\}_{y\in Y}$ form a partition of $X$ into disjoint open
sets, so each $F_y$ is also closed (its complement is the union of the other fibres, all open). If $f$ took two
distinct values, some $F_y$ would be a non-trivial clopen set and $X$ would be disconnected. Hence exactly one
fibre is non-empty and $f$ is constant. $\blacksquare$

**18.** *Strategy: define a continuous function on $[0,\tfrac12]$ that changes sign.*

Let $g(t) = f(e^{2\pi i t}) - f(e^{2\pi i(t+1/2)})$ for $t \in [0,\tfrac12]$. It is continuous (composition of
$f$ with continuous maps), and

$$g(0) = f(1) - f(-1), \qquad g(\tfrac12) = f(-1) - f(1) = -g(0).$$

If $g(0) = 0$, take $x = 1$ (then $f(1) = f(-1)$, the antipodal pair $\{1,-1\}$). Otherwise $g(0)$ and
$g(\tfrac12)$ have opposite signs, so by the intermediate value theorem (Corollary 7.4.2) there is
$t_0 \in (0,\tfrac12)$ with $g(t_0) = 0$. Put $x = e^{2\pi i t_0}$; then $-x = e^{2\pi i(t_0 + 1/2)}$ and
$f(x) = f(-x)$. $\blacksquare$

**19.** *Strategy: join two unit vectors by a normalised straight line when they are not antipodal, and route
through an auxiliary vector when they are.*

Let $u, v \in S^n$ with $n \ge 1$. If $v \neq -u$, define
$\gamma(t) = \dfrac{(1-t)u + tv}{\lVert (1-t)u + tv\rVert}$. The denominator is non-zero: if
$(1-t)u + tv = 0$, then taking norms (and using $\lVert u\rVert = \lVert v\rVert = 1$, $0\le t\le 1$) gives
$1 - t = t$, so $t = \tfrac12$ and $u = -v$, excluded. Hence $\gamma$ is continuous (quotient of continuous
functions with non-vanishing denominator), takes values in $S^n$, and joins $u$ to $v$.

If $v = -u$, choose a unit vector $w$ orthogonal to $u$ (possible because $n \ge 1$; e.g. rotate any
$e_i$, $i \ge 2$, into a unit vector orthogonal to $u$). Then $w \neq \pm u$, so the previous construction
joins $u$ to $w$ and $w$ to $-u$; concatenating gives a path from $u$ to $v$. Hence $S^n$ is path connected,
therefore connected (Theorem 7.6.1).

$S^0 = \{-1,1\}$ is a two-point discrete space and is not connected (Exercise 2). $\blacksquare$

**20.** *Strategy: the only obstruction to the straight segment between two points of $\mathbb{R}^n\setminus\{0\}$
is that the points are on opposite rays; then detour through a point off the line.*

Let $x, y \in \mathbb{R}^n\setminus\{0\}$, $n \ge 2$.

*Case 1: $y \notin \{-\lambda x : \lambda \ge 0\}$.* Then the segment $\gamma(t) = (1-t)x + ty$ avoids $0$:
if $(1-t)x + ty = 0$ with $t \in [0,1]$, then $y = -\frac{1-t}{t}x$ for $t>0$ (and $y = -x$ for $t$ ... note
$t=1$ gives $y=0$, excluded; $t=0$ gives $x=0$, excluded), so $y$ is a non-positive multiple of $x$, contrary
to the case assumption.

*Case 2: $y = -\lambda x$ with $\lambda > 0$.* Choose $z \neq 0$ with $z \perp x$ (exists since $n\ge2$ and
the orthogonal complement of a line has dimension $n-1 \ge 1$). Then the segment from $x$ to $z$ avoids $0$
(a point of that segment lying in $\mathbb{R} x$ forces $z \in \mathbb{R}x$, false), and the segment from $z$
to $y$ avoids $0$ (a point of it lying in $\mathbb{R} z$ forces $y \in \mathbb{R} z$, false since
$y\in\mathbb{R}x$ and $z \perp x$, $y \neq 0$). Concatenate the two segments.

Hence $\mathbb{R}^n\setminus\{0\}$ is path connected for $n \ge 2$, and therefore connected.

For $n = 1$: $\mathbb{R}\setminus\{0\} = (-\infty,0)\cup(0,\infty)$ is disconnected (Exercise 7(a)).

*Invariance of dimension.* Suppose $h : \mathbb{R} \to \mathbb{R}^n$ were a homeomorphism, $n \ge 2$, and put
$p = h(0)$. Then $h$ restricts to a homeomorphism $\mathbb{R}\setminus\{0\} \to \mathbb{R}^n\setminus\{p\}$.
But a homeomorphism carries components onto components, and the two spaces have $2$ and $1$ components
respectively (translation is a homeomorphism, so $\mathbb{R}^n\setminus\{p\}\cong\mathbb{R}^n\setminus\{0\}$,
which is path connected). Contradiction. $\blacksquare$

**21.** *Strategy: pair the two paths coordinatewise.*

Let $(x_1,y_1), (x_2,y_2) \in X\times Y$. Choose paths $\gamma$ in $X$ from $x_1$ to $x_2$ and $\delta$ in $Y$
from $y_1$ to $y_2$. Then $\eta(t) = (\gamma(t),\delta(t))$ is continuous (a map into a product is continuous
iff its components are) and joins $(x_1,y_1)$ to $(x_2,y_2)$. So $X\times Y$ is path connected.

Since $S^1$ is path connected (Exercise 10) and $[0,1]$ and $\mathbb{R}$ are path connected (convex),
$T^2 = S^1\times S^1$, $S^1\times[0,1]$ and $\mathbb{R}^n = \mathbb{R}\times\cdots\times\mathbb{R}$ are path
connected, by induction on the number of factors. $\blacksquare$

## Advanced

**22.** *Strategy: $T$ is the closure of a connected set; and any path leaving the vertical segment would force
$\sin(1/x)$ to have two different limits at the same time.*

*Connectedness.* The interval $(0,1]$ is connected (Theorem 7.3.3) and $x\mapsto(x,\sin\frac1x)$ is continuous
there, so $G$ is connected (Theorem 7.4.1). Every point $(0,y)$ with $y \in [-1,1]$ is a limit of points of
$G$: taking $x_k = 1/(\arcsin y + 2\pi k) \to 0^+$ gives $(x_k, \sin\frac1{x_k}) = (x_k,y) \to (0,y)$. Hence
$G \subseteq T \subseteq \overline G$, and $T$ is connected by Theorem 7.5.3.

*$T$ is not path connected.* Suppose $\gamma = (\gamma_1,\gamma_2) : [0,1] \to T$ is a path with
$\gamma(0) \in \{0\}\times[-1,1]$ and $\gamma(1) \in G$. Put $Z = \{t : \gamma_1(t) = 0\}$; it is closed
(preimage of $\{0\}$ under the continuous map $\gamma_1$), it contains $0$ and it does not contain $1$. Let
$t_0 = \max Z < 1$. For $t \in (t_0,1]$ we have $\gamma_1(t) \neq 0$; since $\gamma_1$ is continuous on the
connected interval $[t_0,1]$ and $\gamma_1(1) > 0$, its image lies in $(0,\infty)$; hence
$\gamma_1(t) > 0$ and $\gamma(t) \in G$, so $\gamma_2(t) = \sin\frac{1}{\gamma_1(t)}$ for all $t \in (t_0,1]$.

Let $a_k = 1/(\tfrac\pi2 + 2\pi k)$ and $b_k = 1/(\tfrac{3\pi}2 + 2\pi k)$; then $a_k,b_k \to 0^+$ and
$\sin\frac1{a_k} = 1$, $\sin\frac1{b_k} = -1$. For large $k$, $a_k < \gamma_1(1)$ and $b_k < \gamma_1(1)$, so by
the intermediate value theorem applied to $\gamma_1$ on $[t_0,1]$ there are $t_k, s_k \in (t_0,1)$ with
$\gamma_1(t_k) = a_k$ and $\gamma_1(s_k) = b_k$; then $\gamma_2(t_k) = 1$ and $\gamma_2(s_k) = -1$.

We claim $t_k \to t_0$ and $s_k \to t_0$. If not, there is $\delta>0$ and a subsequence with
$t_{k_j} \ge t_0+\delta$; by compactness a further subsequence converges to some $t^* \in [t_0+\delta,1]$, and
continuity of $\gamma_1$ gives $\gamma_1(t^*) = \lim_j a_{k_j} = 0$, contradicting $\gamma_1 > 0$ on
$(t_0,1]$. The same holds for $(s_k)$.

Continuity of $\gamma_2$ at $t_0$ now gives $\gamma_2(t_0) = \lim\gamma_2(t_k) = 1$ and simultaneously
$\gamma_2(t_0) = \lim \gamma_2(s_k) = -1$: impossibility. Hence no such path exists and $T$ is not path
connected. $\blacksquare$

**23.** *Strategy: identify the closure, then use Exercise 22 to separate the two obvious path connected
pieces.*

*Compact.* $T$ is closed in $\mathbb{R}^2$: if $(x_k,y_k)\in T \to (x,y)$, then either $x>0$, in which case
$y = \sin(1/x)$ and $(x,y)\in G$, or $x = 0$, in which case $y\in[-1,1]$ because all $y_k\in[-1,1]$; the case
$x<0$ is impossible since all $x_k\ge0$. It is bounded (contained in $[0,1]\times[-1,1]$). A closed bounded
subset of $\mathbb{R}^2$ is compact.

*Components.* $T$ is connected (Exercise 22), so its only component is $T$.

*Path components.* The set $V = \{0\}\times[-1,1]$ is homeomorphic to the interval $[-1,1]$, hence path
connected; and $G$ is path connected, being the continuous image of the interval $(0,1]$ under
$x\mapsto(x,\sin\frac1x)$. By Exercise 22 there is no path in $T$ joining a point of $V$ to a point of $G$, so
$V$ and $G$ are the two path components.

*Closedness.* $V$ is closed in $T$ (it is closed in $\mathbb{R}^2$). $G$ is not closed in $T$: its closure in
$\mathbb{R}^2$ is $T \neq G$. This shows that path components need not be closed, in contrast with components.
$\blacksquare$

**24.** *Strategy: in a locally path connected space the path components are open; a partition of a connected
space into open sets has one member.*

Let $X$ be connected and locally path connected. For $x\in X$, let $P$ be the path component of $x$. If
$y \in P$, local path connectedness gives a path connected neighbourhood $V$ of $y$; a path connected set
containing $y$ lies in the path component of $y$, which is $P$ (path components are the equivalence classes of
"joined by a path"). Hence $P$ contains a neighbourhood of each of its points, i.e. $P$ is open. The path
components partition $X$, so $X\setminus P$ is a union of open sets and is open; hence $P$ is also closed. As
$P$ is non-empty, clopen and $X$ is connected, $P = X$. Therefore any two points are joined by a path.

*Neither hypothesis can be dropped.* The topologist's sine curve is connected but not locally path connected
(it is not even locally connected, Exercise 34) and is not path connected. The space
$\mathbb{R}\setminus\{0\}$ is locally path connected (it is open in $\mathbb{R}$) but not connected, and is
not path connected. $\blacksquare$

**25.** *Strategy: one direction shrinks a connected neighbourhood inside a component, the other takes the
component of an open set as the required neighbourhood.*

($\Rightarrow$) Let $X$ be locally connected, $U\subseteq X$ open, $C$ a component of $U$, and $x\in C$. Since
$U$ is a neighbourhood of $x$, local connectedness provides a connected neighbourhood $V$ of $x$ with
$V\subseteq U$. As $V$ is connected and contains $x\in U$, maximality of the component $C$ gives
$V\subseteq C$. Since $V$ is a neighbourhood of $x$, there is an open $W$ with $x\in W\subseteq V\subseteq C$;
hence $C$ is open.

($\Leftarrow$) Let $x \in X$ and let $U$ be an open neighbourhood of $x$. Let $C$ be the component of $x$ in
$U$. By hypothesis $C$ is open, so $C$ is a neighbourhood of $x$; it is connected and $C\subseteq U$. Hence
every neighbourhood of $x$ contains a connected neighbourhood of $x$, i.e. $X$ is locally connected at $x$.
Since $x$ was arbitrary, $X$ is locally connected. $\blacksquare$

**26.** *Strategy: balls are convex, so every open set is locally path connected; then components are path
components and are open.*

Let $U\subseteq\mathbb{R}^n$ be open. For $x\in U$ choose $r>0$ with $B_r(x)\subseteq U$; the ball $B_r(x)$ is
convex, hence path connected (Proposition 7.6.4). Therefore $U$ is locally path connected (indeed the balls
form a base of path connected neighbourhoods).

By Theorem 7.9.3, the components of $U$ are exactly its path components, and each is open and closed in $U$.
If $U$ is connected, it has one component, hence one path component: $U$ is path connected.

*The word "open" cannot be replaced by "closed".* The topologist's sine curve $T$ is closed in $\mathbb{R}^2$
and connected, but it is not path connected (Exercise 22). $\blacksquare$

**27.** *Strategy: components of an open set in $\mathbb{R}$ are open intervals; each contains a rational, which
gives countability.*

Let $U\subseteq\mathbb{R}$ be non-empty and open. For $x \in U$ there is $\varepsilon>0$ with
$(x-\varepsilon,x+\varepsilon)\subseteq U$, and that interval is connected; so the component $C_x$ of $x$ in
$U$ contains a neighbourhood of $x$ and is therefore open. A component is connected, hence an interval
(Theorem 7.3.3); an open interval of $\mathbb{R}$ (possibly unbounded, possibly all of $\mathbb{R}$). So the
components are pairwise disjoint open intervals whose union is $U$.

Every non-empty open interval contains a rational number (density of $\mathbb{Q}$). Choosing one rational
$q_C \in C$ for each component gives an injection from the set of components into $\mathbb{Q}$: distinct
components are disjoint, so the chosen rationals are distinct. Since $\mathbb{Q}$ is countable, there are only
countably many components. Hence $U$ is a countable disjoint union of open intervals. $\blacksquare$

**28.** *Strategy: slices through a fixed point; every slice meets a fixed vertical copy of one factor.*

Assume $X, Y$ connected and non-empty, and fix $(x_0,y_0)\in X\times Y$. For $y\in Y$ put

$$T_y = (X\times\{y\})\cup(\{x_0\}\times Y).$$

$X\times\{y\}$ is homeomorphic to $X$ (via $x\mapsto(x,y)$), hence connected; $\{x_0\}\times Y$ is homeomorphic
to $Y$, hence connected; and $(x_0,y)$ lies in both. By Corollary 7.5.2, $T_y$ is connected. Each $T_y$
contains $(x_0,y_0)$, so $\bigcup_{y\in Y}T_y$ is connected by Theorem 7.5.1. Finally
$\bigcup_{y\in Y}T_y = X\times Y$: any $(x,y)$ lies in $T_y$.

For finitely many factors, induct: $X_1\times\cdots\times X_n = (X_1\times\cdots\times X_{n-1})\times X_n$ and
the first factor is connected by the induction hypothesis.

*Where non-emptiness is used.* It is needed to choose $(x_0,y_0)$ and to know that the slices are non-empty.
If a factor is empty the product is empty, and $\varnothing$ is connected, so the theorem remains true; the
hypothesis only matters for the slice argument. $\blacksquare$

**29.** *Strategy: the finitely-supported points form a connected dense subset.*

Let $\{X_i\}_{i\in I}$ be non-empty connected spaces and $P = \prod_{i\in I}X_i$. Fix $a = (a_i)\in P$. For each
finite $J\subseteq I$ put

$$B_J = \{x \in P : x_i = a_i \text{ for every } i \notin J\}.$$

The map $B_J \to \prod_{i\in J}X_i$ deleting the constant coordinates is a homeomorphism, so $B_J$ is
connected by Corollary 7.10.2 (for $J = \varnothing$, $B_J = \{a\}$ is a singleton). Every $B_J$ contains $a$,
so $F := \bigcup_{J\ \text{finite}} B_J$ is connected by Theorem 7.5.1.

$F$ is dense. A basic open set of the product topology has the form $W = \prod_i U_i$ with each $U_i$ open in
$X_i$ and $U_i = X_i$ for all $i$ outside a finite set $J$. Non-emptiness of the factors gives $u_i\in U_i$ for
$i\in J$; define $u_i = a_i$ for $i\notin J$. Then $u\in W\cap F$.

Therefore $P = \overline F$ is connected by Theorem 7.5.3. $\blacksquare$

**30.** *Strategy: a continuous real-valued function on $X$ takes two distinct values, so its image is an
interval with more than one point, and such an interval is uncountable.*

Let $(X,d)$ be connected with $p \neq q$ in $X$, and put $f(x) = d(x,p)$. Then $f$ is continuous,
$f(p) = 0$ and $f(q) = d(p,q) > 0$. The image $f[X]$ is connected (Theorem 7.4.1), hence an interval
(Theorem 7.3.3), and it contains $0$ and $d(p,q)$; therefore $[0,d(p,q)] \subseteq f[X]$. That interval is
uncountable (it is in bijection with $[0,1]$ via $t\mapsto t/d(p,q)$), so $f[X]$ is uncountable, and since $f$
maps $X$ onto $f[X]$, $X$ is uncountable.

Consequently no countable space with the usual metric and at least two points is connected. $\mathbb{Q}$ is
countable, so it is not connected (in accordance with Proposition 7.8.3).

*The irrationals.* $\mathbb{R}\setminus\mathbb{Q}$ is uncountable, so the argument above does not apply. But
between any two distinct irrationals there is a rational $c$; then
$(\mathbb{R}\setminus\mathbb{Q})\cap(-\infty,c)$ and $(\mathbb{R}\setminus\mathbb{Q})\cap(c,\infty)$ are non-empty,
disjoint, open in $\mathbb{R}\setminus\mathbb{Q}$ and cover it. So $\mathbb{R}\setminus\mathbb{Q}$ is
disconnected — indeed totally disconnected, by the same argument applied to any subset with two points.
$\blacksquare$

## Challenge

**31.** *Strategy: the comb without its tip is path connected, and the tip lies in its closure; but a path
leaving the tip cannot cross the gaps between the spikes.*

Write
$B = \bigl([0,1]\times\{0\}\bigr)\cup\bigcup_{n\ge1}\bigl(\{1/n\}\times[0,1]\bigr)$ for the comb space and
$p = (0,1)$, so that $C = B\cup\{p\}$ is the deleted comb space.

*$C$ is connected.* $B$ is path connected: any point of $B$ can be joined to $(0,0)$ by going down its spike
(if it lies on one) and then along the base, and $[0,1]\times\{0\}$ and each spike are convex. Hence $B$ is
connected. Moreover $p \in \overline B$, because $(1/n,1)\in B$ and $(1/n,1)\to(0,1)$. So
$B \subseteq C \subseteq \overline B$ with $B$ connected, and $C$ is connected by Theorem 7.5.3.

*$C$ is not path connected.* Suppose $\gamma = (\gamma_1,\gamma_2):[0,1]\to C$ is a path with $\gamma(0) = p$
and $\gamma(1) \in B$. (If a path reached a spike point $(1/n,y)$ instead, concatenating it with the vertical
segment down to $(1/n,0)$ would give a path to $B$, so this loss of generality is harmless.)

*The only point of $C$ with first coordinate $0$ is $p$*, and *the points of $C$ with positive second
coordinate are $p$ and the spike points $(1/n,y)$ with $0<y\le 1$*.

Let $t_1 = \min\{t : \gamma_2(t) = 0\}$; the set is closed and non-empty (it contains $1$) and $t_1>0$. For
$t<t_1$ we have $\gamma_2(t)>0$, so $\gamma(t) = p$ or $\gamma(t)$ is a spike point.

Let $Z = \{t\in[0,t_1] : \gamma_1(t) = 0\}$; it is closed and non-empty, and by the observation above
$Z = \{t : \gamma(t) = p\}$. Put $T = \max Z$; then $T<t_1$ (as $\gamma_2(t_1) = 0$ while $\gamma_2 = 1$ on
$Z$), and $\gamma_1(t)>0$ for $t\in(T,t_1]$.

For $t\in(T,t_1)$ we have $\gamma_2(t)>0$ and $\gamma(t)\neq p$, so $\gamma(t)$ is a spike point, i.e.
$\gamma_1(t) = 1/n(t)$ for some $n(t)\in\mathbb{N}$. Thus $\gamma_1\bigl((T,t_1)\bigr)\subseteq\{1/n : n\in
\mathbb{N}\}$. The image of the connected interval $(T,t_1)$ under the continuous map $\gamma_1$ is connected,
and a connected subset of the discrete set $\{1/n\}$ is a single point; hence $\gamma_1(t) = 1/N$ for all
$t\in(T,t_1)$, for some fixed $N$.

But $\gamma_1(T) = 0$ and $\gamma_1$ is continuous, so $\gamma_1(t)\to 0$ as $t\to T^+$, contradicting
$\gamma_1 \equiv 1/N \neq 0$ on $(T,t_1)$. Therefore no path joins $p$ to $B$, and $C$ is connected but not
path connected. $\blacksquare$

**32.** *Strategy: the image would be a closed interval, and deleting its midpoint would split it, whereas
deleting a point from $S^1$ leaves it connected.*

Suppose $f:S^1\to\mathbb{R}$ is continuous and injective. $S^1$ is compact and $\mathbb{R}$ is Hausdorff, so
$f$ is a homeomorphism onto its image: if $F\subseteq S^1$ is closed then $F$ is compact, so $f[F]$ is compact,
hence closed in $\mathbb{R}$; a continuous bijection that is a closed map is a homeomorphism onto its image.

The image $f[S^1]$ is connected (Theorem 7.4.1) and compact, so it is a closed interval $[a,b]$ with $a<b$
(injectivity and $S^1$ having more than one point). Let $m = \tfrac{a+b}2 \in (a,b)$ and $z = f^{-1}(m)$. Then

$$f\bigl[S^1\setminus\{z\}\bigr] = [a,b]\setminus\{m\} = [a,m)\cup(m,b],$$

which is disconnected (the two halves are non-empty, disjoint, and both open in $[a,b]\setminus\{m\}$).

On the other hand $S^1\setminus\{z\}$ is connected: the map
$\varphi(t) = \bigl(\tfrac{1-t^2}{1+t^2},\tfrac{2t}{1+t^2}\bigr)$ is a continuous bijection from $\mathbb{R}$
onto $S^1\setminus\{(1,0)\}$ with continuous inverse $t = y/(1-x)$, and a rotation carries
$S^1\setminus\{(1,0)\}$ onto $S^1\setminus\{z\}$; being homeomorphic to the connected space $\mathbb{R}$, the
set $S^1\setminus\{z\}$ is connected.

A homeomorphism cannot map a connected space onto a disconnected one, so no such $f$ exists.

*Consequences.* A homeomorphism $S^1\to[0,1]$ would compose with the inclusion $[0,1]\hookrightarrow\mathbb{R}$
to give a continuous injection $S^1\to\mathbb{R}$; and a homeomorphism $S^1 \to \mathbb{R}$ is impossible
outright because $S^1$ is compact and $\mathbb{R}$ is not. $\blacksquare$

**33.** *Strategy: a homeomorphism restricts to a homeomorphism of the complements of a point, and
homeomorphisms preserve the number of components.*

Suppose $h:\mathbb{R}\to\mathbb{R}^n$ is a homeomorphism, $n\ge2$, and put $p = h(0)$. Then $h$ restricts to a
homeomorphism $\mathbb{R}\setminus\{0\} \to \mathbb{R}^n\setminus\{p\}$. Now
$\mathbb{R}\setminus\{0\} = (-\infty,0)\cup(0,\infty)$ has exactly two components, while
$\mathbb{R}^n\setminus\{p\}$ is homeomorphic (by translation) to $\mathbb{R}^n\setminus\{0\}$, which is path
connected for $n\ge2$ (Exercise 20) and therefore has exactly one component. A homeomorphism carries
components onto components, so the two spaces must have the same number of components — contradiction. Hence
$\mathbb{R}\not\cong\mathbb{R}^n$ for $n\ge2$.

*Why the method stops there.* For $m,n\ge2$ both punctured spaces $\mathbb{R}^m\setminus\{0\}$ and
$\mathbb{R}^n\setminus\{0\}$ are path connected, so counting components of punctured spaces gives no
information. One must compute a finer invariant: for $n\ge3$, $\mathbb{R}^n\setminus\{0\}$ is simply connected
(it deformation retracts onto $S^{n-1}$, and $S^{n-1}$ is simply connected for $n-1\ge2$), whereas
$\mathbb{R}^2\setminus\{0\}$ deformation retracts onto $S^1$, whose fundamental group is $\mathbb{Z}$. Thus
$\mathbb{R}^2 \not\cong \mathbb{R}^n$ for $n\ge3$, and in general $\mathbb{R}^m\not\cong\mathbb{R}^n$ for
$m\neq n$ requires homology: $H_{n-1}(\mathbb{R}^n\setminus\{0\}) \cong \mathbb{Z}$ while
$H_{m-1}(\mathbb{R}^n\setminus\{0\}) = 0$ when $m-1\neq n-1$. This is the programme of
[Introduction to Algebraic Topology](../05-algebraic-topology/README.md). $\blacksquare$

**34.** *Strategy: a connected set containing a point of the segment and a point of the graph must contain
points at heights $\pm1$, which are far away; so small balls contain no connected neighbourhood.*

Let $p = (0,y)$ with $y\in[-1,1]$. Choose $\varepsilon>0$ smaller than the distance from $p$ to both horizontal
lines $y=\pm1$: if $-1<y<1$ take $\varepsilon = \tfrac12\min\{|1-y|,|1+y|\}$, and if $y = 1$ or $y = -1$ take
$\varepsilon = 1$ (then the line at the other height is at distance $\ge2$).

Let $U = T\cap B_\varepsilon(p)$, an open neighbourhood of $p$ in $T$. We show that every connected set
$C\subseteq U$ with $p\in C$ equals $\{p\}$.

Suppose $C$ contains a point $q = (x,\sin\tfrac1x) \in G$ with $0<x<1$. The first coordinate is continuous on
the connected set $C$ and takes the values $0$ at $p$ and $x$ at $q$, so $\gamma_1[C]\supseteq[0,x]$. Every
point of $T$ with first coordinate $u\in(0,1]$ lies on $G$ and has second coordinate $\sin\tfrac1u$; hence
$C$ contains points of the form $(u,\sin\frac1u)$ for every $u\in(0,x]$. Choose $u_+, u_- \in (0,x]$ with
$\sin\frac1{u_+} = 1$ and $\sin\frac1{u_-} = -1$ (for instance $u_\pm = 1/(\pm\tfrac\pi2 + 2\pi k)$ with $k$
large). Then $(u_+,1), (u_-,-1)\in C$, and

$$\bigl\lVert (u_+,1) - (0,y)\bigr\rVert \ge |1-y| \ge 2\varepsilon, \qquad
\bigl\lVert (u_-,-1) - (0,y)\bigr\rVert \ge |1+y| \ge 2\varepsilon$$

(with the obvious modification when $y = \pm1$: the relevant distance is then $\ge 2 > \varepsilon$). So at
least one of these points has distance $\ge \varepsilon$ from $p$, contradicting $C \subseteq B_\varepsilon(p)$.

Hence the component of $p$ in $U$ is $\{p\}$. But $\{p\}$ is not a neighbourhood of $p$ in $T$: for every
$\delta>0$ there is $k$ with $0 < 1/(\arcsin y + 2\pi k) < \delta$, and the corresponding point
$(u,\sin\frac1u) = (u,y)$ of $G$ lies in $B_\delta(p)$. So no connected neighbourhood of $p$ is contained in
$U$, and $T$ is not locally connected at $p$. $\blacksquare$

**35.** *Strategy: the Cantor set contains no interval (so any two of its points can be separated by a gap),
and its points are limits of endpoints of the removed intervals.*

*Construction.* Let $K_0 = [0,1]$ and let $K_{n+1}$ be obtained from $K_n$ by removing the open middle third
of each of its $2^n$ component intervals; thus $K_n$ is a union of $2^n$ closed intervals of length $3^{-n}$.
Put $K = \bigcap_{n\ge0}K_n$. Each $K_n$ is closed, so $K$ is closed; $K$ is bounded, hence compact; and
$K\neq\varnothing$ (it contains $0$, $1$ and all endpoints of the removed intervals).

*$K$ contains no non-degenerate interval.* Suppose $[u,v]\subseteq K$ with $u<v$. Then
$[u,v]\subseteq K_n$ for every $n$. A connected subset of $K_n$ lies inside one component interval of $K_n$,
and those have length $3^{-n}$; choosing $n$ with $3^{-n} < v-u$ contradicts $[u,v]\subseteq K_n$.

*$K$ is totally disconnected.* Let $x<y$ be points of $K$. By the previous paragraph $[x,y]\not\subseteq K$,
so there is $c\in(x,y)$ with $c\notin K$. Then $K\cap(-\infty,c)$ is a subset of $K$ that is open in $K$
(its complement in $K$ is $K\cap[c,\infty)$, closed in $K$ because $[c,\infty)$ is closed) and closed in $K$
(because $K$ and $(-\infty,c]$ are closed in $\mathbb{R}$); it contains $x$ and not $y$. Hence $K$ is
disconnected, and by the same argument every subset of $K$ with two points is disconnected. So the components
of $K$ are its points.

*$K$ has no isolated points.* Let $x\in K$ and $n\ge0$. Then $x$ lies in a unique component interval $I_n$ of
$K_n$, of length $3^{-n}$; both endpoints of $I_n$ belong to $K$ (removed sets are open middles, so endpoints
are never removed), and at least one of them differs from $x$. Hence there is a point of $K\setminus\{x\}$
within distance $3^{-n}$ of $x$. As $n$ is arbitrary, $x$ is not isolated.

*$K$ is not locally connected.* Let $x\in K$. A connected subset of $K$ containing $x$ is $\{x\}$ (total
disconnectedness). If $K$ were locally connected at $x$, some neighbourhood of $x$ would be connected, hence
equal to $\{x\}$, which would make $\{x\}$ open in $K$, i.e. $x$ isolated — contradiction. So $K$ is not
locally connected at any of its points.

*Deductions.* $K$ is totally disconnected but not discrete, since none of its points is isolated. And $K$ is
compact and totally disconnected but not locally connected. $\blacksquare$

**36.** *Strategy: an interval with two points contains an interval affinely homeomorphic to $(0,1)$, and
$|(0,1)| = 2^{\aleph_0}$.*

First, $\lvert(0,1)\rvert = 2^{\aleph_0}$. Indeed $x\mapsto\tan\bigl(\pi(x-\tfrac12)\bigr)$ is a bijection
$(0,1)\to\mathbb{R}$, so $\lvert(0,1)\rvert = \lvert\mathbb{R}\rvert$, and $\lvert\mathbb{R}\rvert =
2^{\aleph_0}$ by binary expansions together with Cantor–Bernstein (the set of $0$–$1$ sequences injects into
$[0,1]$, and $\mathbb{R}$ injects into the power set of $\mathbb{Q}$).

Now let $I\subseteq\mathbb{R}$ be an interval with at least two points. Then $I$ contains a closed interval
$[a,b]$ with $a<b$: if $I$ is non-degenerate it contains two points $u<v$, and $[u,v]\subseteq I$ by the
interval property. The affine map $t\mapsto a + (b-a)t$ is a bijection $[0,1]\to[a,b]$, so
$2^{\aleph_0} = \lvert[0,1]\rvert = \lvert[a,b]\rvert \le \lvert I\rvert$; and $\lvert I\rvert \le
\lvert\mathbb{R}\rvert = 2^{\aleph_0}$. Hence $\lvert I\rvert = 2^{\aleph_0}$.

Finally, a connected subset of $\mathbb{R}$ is an interval (Theorem 7.3.3), so any connected subset with at
least two points has cardinality $2^{\aleph_0}$. This sharpens Exercise 30: a connected metric space with two
points is not merely uncountable, and for subsets of $\mathbb{R}$ the exact cardinality is the cardinality of
the continuum. $\blacksquare$
