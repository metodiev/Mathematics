# Algebraic Geometry — Solutions

> [Algebraic Geometry](README.md) · Solutions to [exercises.md](exercises.md) · 36 problems

Each solution states the strategy, then carries out every step. Section references point into
[README.md](README.md). Notation is that of the exercises: $k$ is a field, $V(S)$ and $I(X)$ are the zero set and
the ideal of a set, and $A(X) = k[x_1,\dots,x_n]/I(X)$.

## Beginner

**1.** **Strategy.** Substitute the linear equation into the quadratic one; the number of solutions is the number
of roots, and the field matters only if the roots fail to exist.

**Computation.** On the line $y = x$ the circle equation becomes
$$x^2 + x^2 - 1 = 0 \iff 2x^2 = 1 \iff x^2 = \tfrac12.$$
Over $\mathbb{R}$ the two solutions are $x = \pm 1/\sqrt2$, giving the points
$$\Bigl(\tfrac{1}{\sqrt2}, \tfrac{1}{\sqrt2}\Bigr), \qquad \Bigl(-\tfrac{1}{\sqrt2}, -\tfrac{1}{\sqrt2}\Bigr).$$
Over $\mathbb{C}$ the equation $x^2 = 1/2$ has exactly the same two roots, so $V(x^2+y^2-1, y-x)$ consists of
the same two points. **Check.** $(1/\sqrt2)^2 + (1/\sqrt2)^2 = 1/2 + 1/2 = 1$ ✓.

**Comment.** This is Bézout's theorem in its simplest form: a line and a conic meet in $1 \cdot 2 = 2$ points. Over
$\mathbb{R}$ the count could have failed (a line can miss a real circle), which is exactly why the theorem is
stated over an algebraically closed field.

**2.** **Strategy.** Solve $y^2 = 0$ first.

**Zero set.** If $(a,b) \in V(xy,y^2)$ then $b^2 = 0$, so $b = 0$ because $k$ is a field; then $ab = 0$ holds
automatically. Hence $V(xy,y^2) = \{(a,0) : a \in k\} = V(y)$.

**Properness.** Every element of $I = (xy,y^2)$ has the form $xy\,p + y^2 q = y(xp + yq)$, so every element is
divisible by $y$. If $y \in I$ then $y = y(xp+yq)$, hence $1 = xp + yq$ after dividing by $y$ in the domain
$k[x,y]$; evaluating at $(0,0)$ gives $1 = 0$, a contradiction. So $y \notin I$ and $I \subsetneq (y)$.

**Radical?** No: $y^2 \in I$ but $y \notin I$.

**Nullstellensatz.** The theorem says $I(V(I)) = \sqrt I$, and here $\sqrt I = (y) \ne I$; there is no
contradiction because $I$ is not radical. Over an algebraically closed field the radical is exactly the largest
ideal with the given zero set, and $I$ is strictly smaller.

**3.** **Strategy.** Use the isomorphism $k[x]/(f) \cong k[\alpha]$ for a root $\alpha$ of $f$.

**Over $\mathbb{R}$.** The map $\mathbb{R}[x] \to \mathbb{C}$, $x \mapsto i$, is a surjective ring homomorphism
with kernel $(x^2+1)$; hence $\mathbb{R}[x]/(x^2+1) \cong \mathbb{C}$, which is a field, so $(x^2+1)$ is maximal.
But $a^2 + 1 \ge 1 > 0$ for every real $a$, so $V(x^2+1) = \varnothing$ in $\mathbb{A}^1(\mathbb{R})$.

**Over $\mathbb{C}$.** Now $x^2+1 = (x-i)(x+i)$ is a product of two non-units, so the principal ideal is not
prime, hence not maximal; and $V(x^2+1) = \{i, -i\}$.

**Moral.** The weak Nullstellensatz requires $k$ algebraically closed; over $\mathbb{R}$ a maximal ideal can have
empty zero set. Note also that the *same polynomial* defines a nonempty variety after extending scalars: the
geometry lives over $\bar k$, while the ideal lives over $k$.

**4.** **Strategy.** Both statements are immediate from the definitions; the only care needed is with finite sums.

**(a) $V(S) = V(\langle S\rangle)$.** Since $S \subseteq \langle S\rangle$, every point vanishing on $\langle
S\rangle$ vanishes on $S$, so $V(\langle S\rangle) \subseteq V(S)$. Conversely let $P \in V(S)$ and
$f = \sum_{i=1}^{m} h_i f_i \in \langle S \rangle$ with $f_i \in S$. Then $f(P) = \sum h_i(P) f_i(P) = 0$, so
$P \in V(\langle S\rangle)$.

**(b) $I(X)$ is radical.** Clearly $I(X)$ is an ideal: constant multiples and sums of functions vanishing on $X$
vanish on $X$. Let $f^m \in I(X)$ with $m \ge 1$. For $P \in X$, $f(P)^m = 0$; a field has no nonzero nilpotents,
so $f(P) = 0$. Hence $f \in I(X)$.

**Remark.** Part (b) is where the field hypothesis is used: over a ring with nilpotents it fails, and this is
precisely the phenomenon that schemes are designed to remember.

**5.** **Strategy.** A one-variable polynomial has at most $\deg f$ roots, and every finite set is cut out by a
product of linear factors.

**Closed sets.** If $S \subseteq k[x]$ contains a nonzero polynomial $f$, then $V(S) \subseteq V(f)$, which has at
most $\deg f$ elements; so every proper closed set is finite. Conversely, for a finite set $\{a_1,\dots,a_m\}$ the
polynomial $\prod_{j}(x-a_j)$ vanishes exactly on it, so $\{a_1,\dots,a_m\}$ is closed. Also $\varnothing =
V(1)$ and $\mathbb{A}^1 = V(0)$.

**The finite field case.** For $k = \mathbb{F}_2$ the polynomial $x^2 - x = x(x-1)$ vanishes at both points of
$\mathbb{A}^1$, so $V(x^2-x) = \mathbb{A}^1$ although $x^2 - x \ne 0$. The topology is the discrete one (every
subset of a finite space is finite, hence closed), so the description "finite or everything" degenerates. The
general phenomenon: over a finite field $\mathbb{F}_q$, the polynomial $x^q - x$ vanishes identically, so
distinct polynomials can define the same function.

**6.** **Strategy.** In a UFD a principal ideal $(f)$ is radical if and only if $f$ is squarefree, i.e. a product
of distinct irreducibles. For non-principal ideals, test directly.

* $(xy)$: radical. If $(xy) \mid f^m$ then $x \mid f^m$ and $y \mid f^m$; since $x, y$ are prime, $x \mid f$ and
  $y \mid f$, so $xy \mid f$ (coprime factors).
* $(x^2)$: not radical, since $x^2 \in (x^2)$ but $x \notin (x^2)$.
* $(x^2-y^2) = ((x-y)(x+y))$: radical for $\operatorname{char} k \ne 2$, because $x-y$ and $x+y$ are distinct
  irreducibles. In characteristic $2$, $x^2-y^2 = (x-y)^2$, and the ideal is not radical.
* $(x^2+y^2)$: over an algebraically closed field of characteristic $\ne 2$, $x^2+y^2 = (x+iy)(x-iy)$ with
  distinct factors (if $i = -i$ then $\operatorname{char} k = 2$), so the ideal is radical. In characteristic $2$ it
  equals $(x+y)^2$ and is not radical.
* $(x^2, xy)$: not radical. Every element is divisible by $x$, so $x \notin (x^2,xy)$ (as in Exercise 2), while
  $x^2 \in (x^2,xy)$.

**7.** **Strategy.** A polynomial vanishes at both points iff $f(x,0)$ is divisible by $x(x-1)$.

**Ideal.** Let $f \in I(X)$ and divide by $y$: $f = yq(x,y) + r(x)$ (the division algorithm in $y$ gives a
remainder in $k[x]$). Then $0 = f(0,0) = r(0)$ and $0 = f(1,0) = r(1)$, so $r$ is divisible by $x$ and by $x-1$,
hence by $x(x-1)$ because these are coprime. Therefore $f \in (y, x(x-1))$; the reverse inclusion is clear. So
$I(X) = (y, x(x-1))$.

**Coordinate ring.** $A(X) = k[x,y]/(y, x(x-1)) \cong k[x]/(x(x-1))$.

**Decomposition.** In $k[x]$ the ideals $(x)$ and $(x-1)$ are comaximal, $(x) + (x-1) = (1)$, and their
intersection is $(x(x-1))$. The Chinese remainder theorem gives
$$k[x]/(x(x-1)) \xrightarrow{\ \sim\ } k[x]/(x) \times k[x]/(x-1), \qquad \bar g \mapsto (g(0), g(1)).$$
Hence $A(X) \cong k \times k$. The idempotents $(1,0)$ and $(0,1)$ correspond to the two points: they are the
indicator functions of the two connected components, and each is a polynomial function on $X$ because a finite set
of points can be interpolated.

**8.** **Strategy.** Use the computations of the tutorial: two nonempty open sets in an irreducible space always
meet, and $\mathbb{A}^n$ is irreducible over an infinite field.

**Closedness.** $\{0\} = V(x,y)$, so it is closed. Its complement $U = \mathbb{A}^2 \setminus \{0\}$ is therefore
open (and not closed, since a proper closed subset of $\mathbb{A}^2$ is either a finite set or a curve, never the
complement of a point).

**Intersection of opens.** Let $U = \mathbb{A}^2 \setminus V(I)$ and $W = \mathbb{A}^2 \setminus V(J)$ be nonempty,
with $I, J \trianglelefteq k[x,y]$. Then $V(I) \ne \mathbb{A}^2$, so $I \ne (0)$ (a nonzero ideal has a nonzero
element, and a nonzero polynomial does not vanish on all of $\mathbb{A}^2$ when $k$ is infinite — although here we
may also argue with a specific nonzero element). If $U \cap W = \varnothing$, then $\mathbb{A}^2 = V(I) \cup V(J)
= V(IJ)$, so every element of $IJ$ vanishes everywhere, i.e. $IJ = (0)$. But $k[x,y]$ is a domain, so $IJ = (0)$
forces $I = (0)$ or $J = (0)$, contradicting nonemptiness. Hence $U \cap W \ne \varnothing$.

**Not Hausdorff.** The points $(0,0)$ and $(1,0)$ cannot be separated by disjoint open neighbourhoods, because
every neighbourhood of a point is a nonempty open set, and any two of those meet. A Hausdorff space would admit
disjoint neighbourhoods, so the Zariski topology is not Hausdorff.

**9.** **Strategy.** Compute the image equation, then compare coordinate rings.

**Image.** For $t \in k$, $y^2 = t^{10} = (t^2)^5 = x^5$, so $\psi(t) \in V(y^2-x^5)$. Conversely let
$(a,b) \in V(y^2-x^5)$. If $a = 0$ then $b^2 = 0$, so $b = 0$ and $(a,b) = \psi(0)$. If $a \ne 0$, set
$t = b/a^2$; then
$$t^2 = \frac{b^2}{a^4} = \frac{a^5}{a^4} = a, \qquad t^5 = t\cdot t^4 = t\,a^2 = \frac{b}{a^2}\,a^2 = b,$$
so $(a,b) = \psi(t)$. Hence the image is exactly $V(y^2-x^5)$ and $\psi$ is bijective onto it.

**Not an isomorphism.** The induced map is
$$\psi^* : k[x,y]/(y^2-x^5) \to k[t], \qquad x \mapsto t^2,\ y \mapsto t^5.$$
Its image is $k[t^2,t^5]$, the span of the monomials $t^m$ with $m = 2a + 5b$, i.e. $m \in \{0,2,4,5,6,7,\dots\}$;
in particular $t \notin k[t^2,t^5]$ (there is no monomial of degree $1$ or $3$). If $\psi$ were an isomorphism onto
its image, Theorem 7.25 and Corollary 7.26 would make $\psi^*$ an isomorphism onto $A(\mathbb{A}^1) = k[t]$, in
particular surjective. It is not, so $\psi$ is not an isomorphism. Geometrically, the image curve is a cusp of
higher order at the origin, where the parametrisation is not invertible by a regular map.

**10.** **Strategy.** Irreducibility is equivalent to: the product of two nonzero elements of the coordinate ring
is nonzero.

**$\mathbb{A}^1$.** Let $\mathbb{A}^1 = V(I) \cup V(J)$ with $I, J \trianglelefteq k[x]$. Then
$\mathbb{A}^1 = V(IJ)$, so $IJ \subseteq I(\mathbb{A}^1) = (0)$. Since $k[x]$ is a domain, $I = (0)$ or $J = (0)$,
i.e. one of the closed sets is all of $\mathbb{A}^1$. Hence $\mathbb{A}^1$ is irreducible, over any field.

**$\mathbb{A}^n$ for infinite $k$.** The same argument, provided we know that $IJ = (0)$ forces $I = (0)$ or
$J = (0)$ (true in any domain), and that $V(I) = \mathbb{A}^n$ implies $I = (0)$. The latter uses that a nonzero
polynomial does not vanish at every point of $\mathbb{A}^n$ when $k$ is infinite: prove this by induction on $n$,
writing $f = \sum_{j=0}^{d} f_j(x_1,\dots,x_{n-1}) x_n^j$ and choosing $x_1,\dots,x_{n-1}$ so that not all $f_j$
vanish, then using the one-variable case.

**Consequence.** $I(\mathbb{A}^n) = (0)$ and $A(\mathbb{A}^n) = k[x_1,\dots,x_n]$ has no zero divisors, consistent
with Proposition 7.4.

**11.** **Strategy.** The two equations say $x(y,z) = (0,0)$.

**Description.** A point $(a,b,c)$ satisfies $ab = 0$ and $ac = 0$ iff $a = 0$ or ($b = 0$ and $c = 0$). Hence
$$V(xy,xz) = V(x) \cup V(y,z):$$
the plane $x = 0$ together with the line $y = z = 0$.

**Ideal.** $I(V(xy,xz)) = I(V(x)) \cap I(V(y,z)) = (x) \cap (y,z) = (xy, xz)$. For the last equality: every element
of $(x)\cap(y,z)$ is $xg$ with $xg \in (y,z)$; since $(y,z)$ is prime and $x \notin (y,z)$, $g \in (y,z)$, so
$xg \in x(y,z) = (xy,xz)$. The ideal is an intersection of primes, hence radical.

**Components.** $V(x)$ is a plane, irreducible of dimension $2$; $V(y,z)$ is a line, irreducible of dimension $1$.
Neither contains the other, so both are irreducible components, and $\dim V(xy,xz) = 2$.

**12.** **Strategy.** Homogenise the defining equation with a new variable $Z$ and set $Z = 0$.

**Homogenisation.** With affine coordinates $x = X/Z$, $y = Y/Z$, the equation $y^2 = x^3 - x$ becomes
$$Y^2Z = X^3 - XZ^2, \qquad \text{i.e.} \qquad F = Y^2Z - X^3 + XZ^2 = 0.$$
Indeed, multiplying $y^2 = x^3 - x$ by $Z^3$ gives $Y^2Z = X^3 - XZ^2$.

**Points at infinity.** Set $Z = 0$: $-X^3 = 0$, so $X = 0$, and then $Y \ne 0$. There is exactly one point at
infinity, $[0:1:0]$.

**Smoothness there.** $\partial F/\partial Z = Y^2 + 2XZ$ equals $1 \ne 0$ at $[0:1:0]$, so the projective closure
is smooth at infinity. The affine curve is smooth too: $\nabla(y^2-x^3+x) = (1-3x^2, 2y)$ vanishes only if $y = 0$
and $x^2 = 1/3$, but then $y^2 = 0 \ne x^3 - x = x(1/3 - 1) \ne 0$ for $x = \pm 1/\sqrt3$ (in characteristic
$\ne 2,3$). So the projective closure is a smooth cubic, i.e. an elliptic curve.

## Intermediate

**13.** **Strategy.** One inclusion is "a point killing a product kills a factor" (using that the base ring is a
domain); the other is bookkeeping of inclusions.

**Proof of $V(I) \cup V(J) = V(IJ)$.** If $P \in V(I)$, then every element of $IJ$ is a sum of products $fg$ with
$f \in I$, $g \in J$, and $f(P) = 0$, so $P \in V(IJ)$; similarly for $V(J)$. Conversely suppose $P \notin V(I)$ and
$P \notin V(J)$: there are $f \in I$, $g \in J$ with $f(P) \ne 0 \ne g(P)$, so $(fg)(P) \ne 0$ and $fg \in IJ$,
hence $P \notin V(IJ)$.

**Proof of $V(IJ) = V(I\cap J)$.** Since $IJ \subseteq I \cap J \subseteq I$, the inclusions
$V(I) \subseteq V(I\cap J) \subseteq V(IJ)$ hold by Lemma 7.1(1), and the first part gives equality.

**Example.** In $k[x,y]$ take $I = (x)$ and $J = (y)$. Then $V(I) \cup V(J)$ is the union of the two coordinate
axes, a curve, whereas $V(I+J) = V(x,y) = \{(0,0)\}$ is a single point. So the union is *not* $V(I+J)$; geometrically,
adding ideals corresponds to intersecting varieties.

**14.** **Strategy.** Translate irreducibility into the statement "a product of two nonzero functions is nonzero".

**Irreducible $\Rightarrow$ domain.** Suppose $fg = 0$ in $A(X)$, represented by polynomials $\tilde f, \tilde g$.
Then $X \subseteq V(\tilde f \tilde g) = V(\tilde f) \cup V(\tilde g)$, so
$$X = (X \cap V(\tilde f)) \cup (X \cap V(\tilde g))$$
is a union of two closed subsets of $X$. Irreducibility gives $X = X \cap V(\tilde f)$ or $X = X\cap V(\tilde g)$,
i.e. $\tilde f \in I(X)$ or $\tilde g \in I(X)$, i.e. $f = 0$ or $g = 0$.

**Domain $\Rightarrow$ irreducible.** Suppose $X = X_1 \cup X_2$ with $X_i$ closed and proper. Choose $f \in
I(X_1) \setminus I(X)$ and $g \in I(X_2)\setminus I(X)$; these exist because $I(X_i) \supsetneq I(X)$ (if
$I(X_1) = I(X)$ then $X_1 = V(I(X_1)) = V(I(X)) = X$). Then $fg$ vanishes on $X_1 \cup X_2 = X$, so $fg = 0$ in
$A(X)$ with neither factor zero — contradiction.

**Disjoint closed pieces.** Let $X = X_1 \cup X_2$ with $X_1 \cap X_2 = \varnothing$. Put $I_i = I(X_i)$. Then
$V(I_1 + I_2) = X_1 \cap X_2 = \varnothing$, so by the Nullstellensatz $I(V(I_1+I_2)) = \sqrt{I_1+I_2} =
k[x_1,\dots,x_n]$, hence $1 \in I_1 + I_2$: the ideals are comaximal. Also $I(X) = I(X_1 \cup X_2) = I_1 \cap I_2$.
Chinese remainder gives
$$A(X) = k[x]/(I_1\cap I_2) \cong k[x]/I_1 \times k[x]/I_2 = A(X_1)\times A(X_2).$$
The element $(1,0)$ is an idempotent different from $0$ and $1$; it is a polynomial function that equals $1$ on
$X_1$ and $0$ on $X_2$.

**15.** **Strategy.** Every element of $J$ is divisible by $x$, and $x^2 \in J$ forces $x \in \sqrt J$.

**Radical.** Clearly $J \subseteq (x)$. Conversely, $\sqrt J$ is the intersection of all prime ideals containing $J$
(standard commutative algebra: the radical is the intersection of the primes above the ideal). Every prime $\mathfrak
p \supseteq J$ contains $x^2$, hence contains $x$; so $(x) \subseteq \mathfrak p$ for every such $\mathfrak p$, and
$\sqrt J \supseteq (x)$. Since $(x)$ is itself prime and contains $J$, $\sqrt J \subseteq (x)$. Therefore
$\sqrt J = (x)$.

**Zero set.** Elements of $J$ are $x^2 a + xy b = x(xa + yb)$, so $V(J) = V(x)$: the $y$-axis.

**Nullstellensatz.** $I(V(J)) = I(V(x)) = (x) = \sqrt J$ ✓. Note that $I(V(J)) \ne J$: the ideal $J$ is not
radical, and the Nullstellensatz replaces it by its radical.

**16.** **Strategy.** Dimension: $k[x,y]$ has dimension $2$ and a nonzero nonunit cuts it down by one (Corollary
7.43). Singularities: solve $\nabla f = 0$ and keep only the solutions on the curve.

**Dimension.** $k[x,y]$ is a domain of dimension $2$, and $f$ is nonzero and not a unit (it is nonconstant). Hence
every irreducible component of $V(f)$ has dimension $1$, and $V(f)$ is nonempty, so $\dim V(f) = 1$.

**Singular points.** Write $f = y^2 - x^2(x+1) = y^2 - x^3 - x^2$. Then
$$\frac{\partial f}{\partial x} = -3x^2-2x = -x(3x+2), \qquad \frac{\partial f}{\partial y} = 2y.$$
Both vanish iff $x \in \{0, -2/3\}$ (in characteristic $\ne 3$) and $y = 0$. Whether these points lie on $C$:
* $x = 0$, $y = 0$: $0 = 0 - 0$ ✓, so $(0,0) \in C$ and is singular.
* $x = -2/3$, $y = 0$: the curve requires $0 = x^2(x+1) = \frac49 \cdot \frac13 = \frac{4}{27} \ne 0$ (characteristic
  $\ne 2,3$), so this point is not on $C$.

Therefore $C_{\mathrm{sing}} = \{(0,0)\}$. At the origin the lowest-degree part of $f$ is $y^2 - x^2 = (y-x)(y+x)$,
two distinct lines: a node. The parametrisation $t \mapsto (t^2-1, t(t^2-1))$ shows the two branches meeting at the
origin, for $t = \pm 1$.

**17.** **Strategy.** Pull back a closed set and use that composition of polynomials is polynomial.

**Proof.** Let $Z \subseteq Y$ be closed, say $Z = V(g_1,\dots,g_r)$ with $g_j \in k[y_1,\dots,y_m]$. A point $P \in
X$ lies in $\varphi^{-1}(Z)$ iff $g_j(\varphi(P)) = 0$ for all $j$. Since $\varphi$ is a morphism, $\varphi$ is
given by polynomials $f_1,\dots,f_m$, so $g_j \circ \varphi = g_j(f_1,\dots,f_m) \in k[x_1,\dots,x_n]$. Therefore
$$\varphi^{-1}(Z) = V\bigl(g_1\circ\varphi, \dots, g_r\circ\varphi\bigr),$$
a Zariski closed subset of $X$. As closed sets pull back to closed sets, $\varphi$ is continuous.

**Remark.** The map $\varphi^* : A(Y) \to A(X)$ is exactly the pullback on regular functions, and the computation
above shows that $\varphi^{-1}(Z)$ is the zero set of the ideal generated by $\varphi^*(I(Z))$; this is the
geometric meaning of the algebra homomorphism.

**18.** **Strategy.** Substitute the line equation and count roots with multiplicity; check transversality at each
root.

**Solving.** On $L$ we have $Z = X+Y$. Substituting into $X^2+Y^2 = Z^2$:
$$X^2+Y^2 = (X+Y)^2 = X^2 + 2XY + Y^2 \iff 2XY = 0 \iff X = 0 \ \text{or}\ Y = 0.$$
If $X = 0$ then $Z = Y$, giving $[0:1:1]$; if $Y = 0$ then $Z = X$, giving $[1:0:1]$. These are two distinct
points, and neither is on $Z = 0$ (indeed $Z \ne 0$ at both).

**Multiplicities.** At $P = [0:1:1]$, chart $Y = 1$: the conic is $x^2 + 1 - z^2$ and the line is $x + 1 - z$, i.e.
$z = x+1$. Substituting: $x^2 + 1 - (x+1)^2 = x^2+1-x^2-2x-1 = -2x$, a polynomial with a simple root at $x = 0$.
So $I_P = 1$ (characteristic $\ne 2$). At $Q = [1:0:1]$, chart $X = 1$: the conic is $1 + y^2 - z^2$, the line is
$1 + y - z$, i.e. $z = 1+y$; substituting gives $1 + y^2 - (1+y)^2 = -2y$, again a simple root. So $I_Q = 1$.

**Bézout.** $\sum I_P = 1 + 1 = 2 = 1\cdot 2 = \deg L \cdot \deg C$ ✓.

**19.** **Strategy.** Verify that the map is given by quadratic monomials satisfying the conic equation, then
exhibit an inverse on two charts.

**Well defined and morphism.** For $[S:T] \in \mathbb{P}^1$ the triple $(S^2, ST, T^2)$ is nonzero (if $S = T = 0$
it would not be a point of $\mathbb{P}^1$) and satisfies
$$XZ - Y^2 = S^2T^2 - (ST)^2 = 0,$$
so $\nu$ lands in $C$. Rescaling $[S:T]$ rescales all three coordinates by $\lambda^2$, so $\nu$ is well defined. On
the chart $S \ne 0$ of $\mathbb{P}^1$ put $t = T/S$; then $\nu = [1: t: t^2]$ with polynomial coordinates, and on
the chart $T \ne 0$ put $s = S/T$; then $\nu = [s^2 : s : 1]$. Hence $\nu$ is a morphism.

**Bijectivity.** Let $[X:Y:Z] \in C$, so $XZ = Y^2$. If $X \ne 0$, then $Z = Y^2/X$ and
$$[X:Y:Z] = [X^2 : XY : Y^2] = \nu([X:Y]).$$
If $X = 0$ then $Y^2 = 0$, so $Y = 0$ and the point is $[0:0:1] = \nu([0:1])$. Hence $\nu$ is surjective. For
injectivity, note that $\nu([S:T]) = [S^2:ST:T^2]$ determines $[S:T]$: if $S \ne 0$ then $[X:Y] = [S^2:ST] =
[S:T]$, and if $S = 0$ then the point is $[0:0:1]$ and $[S:T] = [0:1]$.

**Inverse morphisms.** Define $\pi_1 : C \cap \{X \ne 0\} \to \mathbb{P}^1$ by $[X:Y:Z]\mapsto [X:Y]$ and
$\pi_2 : C\cap\{Z \ne 0\}\to\mathbb{P}^1$ by $[X:Y:Z]\mapsto [Y:Z]$; both are given by linear forms with no common
zero on their domains, hence are morphisms. On the overlap $XZ \ne 0$ they agree because $XZ = Y^2$ gives
$$[X:Y] = [XY : Y^2] = [XY : XZ] = [Y:Z].$$
So they glue to a morphism $\pi : C \to \mathbb{P}^1$. Finally $\pi\nu([S:T]) = [S:T]$ by the computation above, and
$\nu\pi = \operatorname{id}_C$ because $\nu$ is surjective. Hence $C \cong \mathbb{P}^1$.

**20.** **Strategy.** Show that $x^2-yz$ is irreducible, hence prime (a UFD is a GCD domain, and in a UFD
irreducible elements generate prime ideals), then compute the dimension by Corollary 7.43.

**Irreducibility.** Suppose $x^2 - yz = FG$ with $F, G \in k[x,y,z]$ non-units. Since $x^2-yz$ has degree $2$, both
factors have degree $1$: $F = az + b$, $G = cz + d$ with $a,b,c,d \in k[x,y]$ (the polynomial is linear in $z$). The
$z^2$-coefficient of $FG$ is $ac = 0$, so say $a = 0$. Then $FG = b(cz+d)$, and comparing the coefficient of $z$
gives $bc = -y$, while the constant term gives $bd = x^2$. Since $bc = -y$ is irreducible in $k[x,y]$, either $b$ or
$c$ is a unit. If $c$ is a unit then $b = -y/c$ and $d = x^2/b = -x^2c/y$ must lie in $k[x,y]$, which is impossible
because $y \nmid x^2$. If $b$ is a unit then $F = b$ is a unit, contradicting the choice. So $x^2-yz$ is irreducible,
hence prime.

**Coordinate ring and dimension.** $A(X) = k[x,y,z]/(x^2-yz)$ is a domain. Since $k[x,y,z]$ has dimension $3$ and
$x^2 - yz$ is nonzero with no repeated factor, every irreducible component of $X$ has dimension $2$ by Corollary
7.43; irreducibility gives $\dim X = 2$. Concretely, the map $k[u,v] \to A(X)$, $u \mapsto x$, $v \mapsto y$, is
injective with fraction field of transcendence degree $2$.

**21.** **Strategy.** A global regular function restricts to a polynomial on each chart; compatibility on the
overlap forces it to be constant.

**Computation.** Cover $\mathbb{P}^1 = U_0 \cup U_1$ with $U_0 = \{[1:t]\} \cong \mathbb{A}^1$ and $U_1 =
\{[s:1]\}\cong\mathbb{A}^1$; on the overlap $U_0\cap U_1$, $s = 1/t$. Let $f \in \mathcal O(\mathbb{P}^1)$. Then
$f|_{U_0} = p(t)$ for a polynomial $p$, and $f|_{U_1} = q(s)$ for a polynomial $q$. On the overlap,
$$p(t) = q(1/t) \qquad \text{for all } t \ne 0.$$
Write $p(t) = \sum_{i=0}^{d} a_i t^i$ and $q(s) = \sum_{j=0}^{e} b_j s^j$. Multiplying by $t^e$ gives
$\sum_i a_i t^{i+e} = \sum_j b_j t^{e-j}$, an identity of polynomials in $t$. If $d > 0$ then the left side has a
term $a_d t^{d+e}$ of degree $d+e > e$, while the right side has degree $\le e$: contradiction unless $a_d = 0$.
Hence $p$ is constant, and $f$ is constant. So $\mathcal O(\mathbb{P}^1) = k$.

**Not affine.** If $\mathbb{P}^1$ were isomorphic to an affine variety $X$, then $A(X) \cong \mathcal
O(\mathbb{P}^1) = k$. But an affine variety with coordinate ring $k$ is a single point: the functor $X \mapsto A(X)$
is an anti-equivalence (Corollary 7.26), and $\operatorname{Hom}_{k\text{-alg}}(k,k)$ has one element, so $X =
\operatorname{Spec} k$ is a point. This contradicts $|\mathbb{P}^1| > 1$.

**22.** **Strategy.** Density comes from irreducibility; injectivity from the fact that a regular function vanishing
on a dense set vanishes everywhere.

**Density.** $X$ is irreducible, hence any nonempty open subset is dense (Proposition 7.22(2)). Alternative direct
argument: if $U \ne \varnothing$ and $\overline U \ne X$, then $X = \overline U \cup (X\setminus U)$ writes $X$ as a
union of two proper closed sets.

**Injectivity.** Let $f \in A(X)$ restrict to $0$ on $U$. The zero set $V(f) \subseteq X$ is closed and contains
$U$, hence contains $\overline U = X$; so $f$ vanishes on $X$, i.e. $f = 0$ in $A(X)$. Therefore the restriction
map $A(X)\to \mathcal O_X(U)$ is injective.

**Remark.** The map need not be surjective: for $X = \mathbb{A}^1$ and $U = \mathbb{A}^1\setminus\{0\}$ we have
$\mathcal O_X(U) = k[t,t^{-1}] \supsetneq k[t]$.

**23.** **Strategy.** Direct verification from the definition.

**(a) $\sqrt J$ is an ideal.** If $f^m \in J$ and $g^n \in J$, then $(f+g)^{m+n}$ is a sum of terms each containing
$f^m$ or $g^n$, hence lies in $J$; so $f + g \in \sqrt J$. If $r \in R$ and $f^m \in J$, then $(rf)^m = r^m
f^m \in J$, so $rf \in \sqrt J$. Clearly $J \subseteq \sqrt J$ (take $m = 1$).

**(b) Idempotence.** $f \in \sqrt{\sqrt J}$ means $f^m \in \sqrt J$ for some $m$, so $(f^m)^n = f^{mn} \in J$ for
some $n$, hence $f \in \sqrt J$. The reverse inclusion is clear.

**(c) $V(\sqrt J) = V(J)$.** Since $J \subseteq \sqrt J$, $V(\sqrt J)\subseteq V(J)$. Conversely, if $P \in V(J)$
and $f \in \sqrt J$ with $f^m \in J$, then $f(P)^m = 0$, so $f(P) = 0$; hence $P \in V(\sqrt J)$.

**(d) Example.** In $k[x,y]$, $J = (x^2)$ satisfies $\sqrt J = (x) \supsetneq J$. More interestingly,
$(x^2, xy) \subsetneq (x)$ as in Exercise 15.

**24.** **Strategy.** The whole theorem is the strong Nullstellensatz plus the translation of containment into
inclusion reversal; the "prime" and "maximal" statements are Proposition 7.4 and the weak Nullstellensatz.

**Bijection.** Let $\mathcal{R}$ be the set of radical ideals and $\mathcal{A}$ the set of algebraic sets. For
$J \in \mathcal R$, $I(V(J)) = \sqrt J = J$ by Theorem 7.18. For $X \in \mathcal A$, $V(I(X)) = X$ by Lemma 7.1(3).
Hence $V$ and $I$ are mutually inverse bijections.

**Inclusion reversal.** If $J_1 \subseteq J_2$ and $P \in V(J_2)$, then $P$ kills $J_2 \supseteq J_1$, so
$V(J_2)\subseteq V(J_1)$. Dually for $I$.

**Prime $\leftrightarrow$ irreducible.** This is Proposition 7.4 (valid over any field).

**Maximal $\leftrightarrow$ point.** A maximal ideal $\mathfrak m$ is radical, and $V(\mathfrak m) \ne \varnothing$
by Theorem 7.17. If $V(\mathfrak m)$ contained two distinct points $P \ne Q$, then $I(V(\mathfrak m)) = \mathfrak m
\subseteq \mathfrak m_P \cap \mathfrak m_Q$, contradicting maximality (a maximal ideal contained in a proper ideal
must equal it). So $V(\mathfrak m) = \{P\}$, and conversely $I(\{P\}) = \mathfrak m_P$ is maximal because
$k[x]/\mathfrak m_P \cong k$.

**Where algebraic closure is used.** Only in Theorem 7.18, whose proof uses the weak Nullstellensatz (Theorem
7.17), which uses Zariski's lemma and the fact that an algebraic extension of an algebraically closed field is
trivial. Everything else — inclusion reversal, the union/intersection formulae, prime $\leftrightarrow$ irreducible
— holds over any field. Over $\mathbb{R}$ the map $J \mapsto V(J)$ is not injective on radical ideals: the
maximal ideals $(x^2+1)$ and $(x^2+2)$ both have empty zero set.

**25.** **Strategy.** Reduce to the Nullstellensatz by comparing zero sets.

**Reduction.** Write $f = u\,p_1^{e_1}\cdots p_r^{e_r}$ with $u \in k^\times$, the $p_i$ distinct irreducibles and
$e_i \ge 1$ (unique by unique factorisation in $k[x,y]$). Then $f_{\mathrm{red}} = p_1\cdots p_r$ and
$V(f) = V(f_{\mathrm{red}})$, because $f$ and $f_{\mathrm{red}}$ have the same zero set (a power of a polynomial
vanishes exactly where the polynomial does).

**The ideal.** Clearly $(f_{\mathrm{red}}) \subseteq I(V(f_{\mathrm{red}}))$. Conversely, by Theorem 7.18,
$$I(V(f_{\mathrm{red}})) = \sqrt{(f_{\mathrm{red}})}.$$
The polynomial $f_{\mathrm{red}}$ is a product of distinct irreducibles, so $(f_{\mathrm{red}})$ is radical: if
$g^m \in (f_{\mathrm{red}})$ then $p_i \mid g^m$ for each $i$, hence $p_i \mid g$ as $p_i$ is prime, hence
$f_{\mathrm{red}} \mid g$. Therefore $\sqrt{(f_{\mathrm{red}})} = (f_{\mathrm{red}})$ and
$$I(V(f)) = I(V(f_{\mathrm{red}})) = (f_{\mathrm{red}}).$$

**Irreducibility criterion.** $V(f)$ is irreducible iff $I(V(f))$ is prime (Proposition 7.4) iff $(f_{\mathrm{red}})$
is prime iff $f_{\mathrm{red}}$ is irreducible (in a UFD, a principal ideal is prime iff its generator is
irreducible) iff $r = 1$, i.e. $f = u p_1^{e_1}$ is a power of an irreducible polynomial.

**26.** **Strategy.** Identify both rings with a quotient of $k[x_1,\dots,x_n,y_1,\dots,y_m]$ and use the
Nullstellensatz to identify the kernels. The only input is that $A(X)\otimes_k A(Y)$ is a domain, which is the
standard geometric-integrality lemma over an algebraically closed field.

**Map.** Let $A = k[x_1,\dots,x_n]$, $B = k[y_1,\dots,y_m]$ and let $I = I(X)\cdot k[x,y]$, $J = I(Y)\cdot
k[x,y]$ be the extended ideals. There is a surjective $k$-algebra homomorphism
$$\Psi : k[x,y] \longrightarrow A(X)\otimes_k A(Y), \qquad x_i \mapsto \bar x_i \otimes 1, \quad y_j \mapsto 1
\otimes \bar y_j,$$
with kernel $I + J$. Hence $k[x,y]/(I+J) \cong A(X)\otimes_k A(Y)$.

**Reducedness.** Over an algebraically closed field the tensor product of two finitely generated domains is a
domain (both are geometrically integral over $k$). Hence $I + J$ is prime, in particular radical.

**Kernel identified.** On the one hand $V(I+J) = V(I)\cap V(J) = X\times Y$. On the other hand, since $I+J$ is
radical, the Nullstellensatz gives $I+J = I(V(I+J)) = I(X\times Y)$. Therefore
$$A(X\times Y) = k[x,y]/I(X\times Y) = k[x,y]/(I+J) \cong A(X)\otimes_k A(Y).$$

**Irreducibility.** $I(X\times Y)$ is prime because $A(X)\otimes A(Y)$ is a domain; by Proposition 7.4, $X\times Y$
is irreducible. One can also see this directly: if $X\times Y = Z_1\cup Z_2$ with $Z_i$ closed, put $Y_i = \{y :
X\times\{y\}\subseteq Z_i\}$; each $Y_i$ is closed (it is $\bigcap_{x\in X}\{y : (x,y)\in Z_i\}$), and $Y = Y_1\cup
Y_2$ because each fibre $X\times\{y\}$ is irreducible and hence lies in one of the $Z_i$. Since $Y$ is irreducible,
$Y = Y_1$ or $Y = Y_2$, so $X\times Y \subseteq Z_1$ or $Z_2$.

## Advanced

**27.** **Strategy.** Write down mutually inverse morphisms, then distinguish the two coordinate rings by their
groups of units.

**Isomorphism.** Let $U = \mathbb{A}^1\setminus\{0\}$ and $H = V(xy-1)$. The maps
$$\alpha : U \to H,\ t\mapsto (t,1/t), \qquad \beta : H \to U,\ (x,y)\mapsto x$$
are morphisms on their domains: $\alpha$ is given by the rational functions $t$ and $1/t$, regular because $t \ne 0$
on $U$; $\beta$ is a projection, hence polynomial. Moreover $\beta\alpha(t) = t$ and $\alpha\beta(x,y) = (x, 1/x) =
(x,y)$ using $xy = 1$ on $H$. So $U \cong H$.

**Coordinate ring.** $A(H) = k[x,y]/(xy-1)$. The homomorphism $k[x,y] \to k[t,t^{-1}]$ with $x\mapsto t$,
$y\mapsto t^{-1}$ is surjective with kernel $(xy-1)$: if $f(x,y)\mapsto 0$, then $f(t,t^{-1}) = 0$; multiplying by a
suitable power of $t$ and using the relation $xy = 1$ shows $f \in (xy-1)$ (equivalently, $k[x,y]/(xy-1) \cong
k[x]_x = k[x,x^{-1}]$ by the universal property of localisation). Hence $A(H)\cong k[t,t^{-1}]$.

**Not isomorphic to $\mathbb{A}^1$.** The units of $k[t]$ are exactly $k^\times$, whereas $t \in k[t,t^{-1}]$ is a
unit that is not a constant, so $k[t,t^{-1}]^\times \supsetneq k^\times$. A $k$-algebra isomorphism $\phi : k[t] \to
k[t,t^{-1}]$ would send $k[t]^\times = k^\times$ onto $k[t,t^{-1}]^\times$ and would fix $k$; hence
$k[t,t^{-1}]^\times = k^\times$, a contradiction. By Corollary 7.26, $U \not\cong \mathbb{A}^1$.

**28.** **Strategy.** Use the resultant in one variable: a nonzero polynomial of degree $\le mn$ cannot have more
than $mn$ roots, and a generic projection makes distinct points have distinct images.

**Step 1: finiteness.** Let $F, G$ be the defining homogeneous polynomials, of degrees $m, n$. After a generic
linear change of coordinates we may assume that the coefficient of $Z^m$ in $F$ and of $Z^n$ in $G$ are nonzero, and
that $F, G$ are coprime in $k(X,Y)[Z]$ (they have no common factor, since a common factor of positive degree would
define a common component). Then
$$R(X,Y) := \operatorname{Res}_Z(F,G) \in k[X,Y]$$
is a nonzero homogeneous polynomial of degree $mn$. For a point $[a:b:c] \in C\cap D$, the value $R(a,b)$ vanishes:
indeed $Z = c$ is a common root of $F(a,b,Z)$ and $G(a,b,Z)$, and a resultant vanishes when its two arguments have
a common root (the leading coefficients do not both vanish by our genericity). Since $R \ne 0$ has finitely many
projective zeros, and for each fixed $[a:b]$ the possible $c$ are roots of a nonzero polynomial of degree $\le m$,
the set $C\cap D$ is finite.

**Step 2: a good projection.** Since $C \cap D$ is finite, choose a point $Q \in \mathbb{P}^2$ that lies on no line
through two distinct points of $C\cap D$ and outside $C\cup D$ (finitely many forbidden lines, and $k$ is infinite).
Project from $Q$ onto a line: distinct points of $C\cap D$ then have distinct images. After a further linear change
of coordinates, this projection is $[X:Y:Z]\mapsto [X:Y]$, so distinct points of $C\cap D$ have distinct $[X:Y]$.

**Step 3: count.** Each point of $C\cap D$ gives a distinct projective root $[a:b]$ of the nonzero form $R$ of degree
$mn$. A nonzero homogeneous polynomial of degree $mn$ in two variables has at most $mn$ distinct projective zeros
(over an algebraically closed field it factors into $mn$ linear forms). Therefore
$$\#(C\cap D) \le \deg R = mn. \qquad \blacksquare$$

**Remark.** Bézout's theorem strengthens "$\le$" to "with multiplicity exactly $mn$"; the argument above shows that
the multiplicities account for the difference.

**29.** **Strategy.** Derive the formulas by substituting the line equation and using Vieta's formulas; then check
each axiom from the definition.

**Derivation.** Let $P_1 = (x_1,y_1)$, $P_2 = (x_2,y_2)$ with $x_1 \ne x_2$. The line through them is $y = \lambda x
+ \nu$ with
$$\lambda = \frac{y_2-y_1}{x_2-x_1}, \qquad \nu = y_1 - \lambda x_1.$$
Substituting into $y^2 = x^3+ax+b$ gives $(\lambda x+\nu)^2 = x^3+ax+b$, i.e.
$$x^3 - \lambda^2x^2 + (a-2\lambda\nu)x + (b-\nu^2) = 0.$$
The three roots are $x_1, x_2, x_3$, where $x_3$ is the third intersection; by Vieta $x_1+x_2+x_3 = \lambda^2$, so
$x_3 = \lambda^2 - x_1 - x_2$. The third point is $S = (x_3, \lambda x_3+\nu)$ and $P_1+P_2 = -S$, so
$$y_3 = -(\lambda x_3+\nu) = -\lambda x_3 - y_1 + \lambda x_1 = \lambda(x_1-x_3) - y_1.$$
For $P_1 = P_2$ the line is the tangent, whose slope is obtained by implicit differentiation of $y^2 = x^3+ax+b$:
$2y\,y' = 3x^2+a$, so $\lambda = (3x_1^2+a)/(2y_1)$ when $y_1 \ne 0$.

**(i) Identity.** By definition $P + O = O + P = P$ and $O + O = O$.

**(ii) Inverses.** For $P = (x_1,y_1)$, the line through $P$ and $-P = (x_1,-y_1)$ is the vertical line $x = x_1$,
whose third intersection with $E$ is $O$; hence $P + (-P) = -O = O$. Also $-O = O$ and $O + O = O$.

**(iii) Commutativity.** The line through $P$ and $Q$ is the line through $Q$ and $P$, so the construction of
$P+Q$ and $Q+P$ is identical. (For $P = Q$ both sides are the tangent construction.)

**(iv) $2P = O$.** The tangent at $P$ has slope $\lambda = (3x_1^2+a)/(2y_1)$ if $y_1 \ne 0$; it is vertical exactly
when $2y_1 = 0$, i.e. $y_1 = 0$ (characteristic $\ne 2$). A vertical line through $P$ meets $E$ at $P$, at $-P$, and
at $O$; hence the third point is $O$ and $2P = O$. Conversely if $y_1 = 0$ then the tangent is vertical (the
gradient of $y^2 - x^3-ax-b$ at $P$ is $(-3x_1^2-a, 0)$, so the tangent is $x = x_1$), giving $2P = O$.

**(v) $3P = O$.** $2P = -S$ where $S$ is the third point of the tangent at $P$. Then $3P = O$ iff $2P = -P$ iff
$-S = -P$ iff $S = P$ iff the tangent meets $E$ only at $P$, with multiplicity $3$ — the definition of an inflection
point.

**Note.** Associativity is the only axiom not covered here; it is proved in Exercise 33.

**30.** **Strategy.** Sum the Legendre symbols of $f(x) = x^3+x+1$ over $\mathbb{F}_{11}$, then compute multiples of
$P$ until the group law returns $O$.

**The sum.** The nonzero squares modulo $11$ are $\{1,3,4,5,9\}$. Evaluating $f$:

| $x$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| $f(x) \bmod 11$ | 1 | 3 | 0 | 9 | 3 | 10 | 3 | 10 | 4 | 2 | 10 |
| $\left(\frac{f(x)}{11}\right)$ | $+1$ | $+1$ | $0$ | $+1$ | $+1$ | $-1$ | $+1$ | $-1$ | $+1$ | $-1$ | $-1$ |

(For example $f(2) = 8+2+1 = 11 \equiv 0$, and $f(3) = 27+3+1 = 31 \equiv 9 = 3^2$.) The sum is
$1+1+0+1+1-1+1-1+1-1-1 = 2$, so
$$\#E(\mathbb{F}_{11}) = 11 + 1 + 2 = 14.$$
Each $x$ with $f(x) \ne 0$ contributes two points (two square roots of $f(x)$), and $x = 2$ contributes one
(the point $(2,0)$ of order $2$); together with $O$ this gives $2\cdot 6 + 1 + 1 = 14$ ✓.

**Hasse.** $|14 - 12| = 2 \le 2\sqrt{11} \approx 6.63$ ✓.

**Order of $P = (0,1)$.** First $2P$: $\lambda = (3\cdot 0 + 1)/(2\cdot 1) = 1/2 \equiv 6 \pmod{11}$ (as
$2\cdot 6 = 12 \equiv 1$), so
$$x_3 = 6^2 - 0 = 36 \equiv 3, \qquad y_3 = 6(0-3) - 1 = -19 \equiv 3,$$
hence $2P = (3,3)$, which is on $E$ since $27+3+1 = 31 \equiv 9 = 3^2$ ✓. Next $4P = 2(2P)$: the slope is
$(3\cdot 9+1)/(2\cdot 3) = 28/6 = 28\cdot 2 = 56 \equiv 1$, so
$$x_4 = 1 - 6 = -5 \equiv 6, \qquad y_4 = 1\cdot(3-6) - 3 = -6 \equiv 5.$$
Thus $4P = (6,5)$; check $216 + 6 + 1 = 223 \equiv 3 = 25 \equiv 5^2$ ✓. Then $6P = 4P + 2P$: with
$P_1 = (6,5)$, $P_2 = (3,3)$,
$$\lambda = \frac{3-5}{3-6} = \frac{-2}{-3} = \frac23 \equiv 8, \quad x = 64 - 9 = 55 \equiv 0, \quad y = 8(6-0) - 5 = 43 \equiv 10,$$
so $6P = (0,10) = -P$ ✓. Hence $7P = 6P + P = O$, and since $P \ne O$ and no smaller multiple vanishes (orders $1$
and $2$ are excluded because $y_1 = 1 \ne 0$), the order of $P$ is exactly $7$.

**Group structure.** $\#E(\mathbb{F}_{11}) = 14 = 2\cdot 7$, so $E(\mathbb{F}_{11})$ is either $\mathbb{Z}/14$ or
$\mathbb{Z}/2\times\mathbb{Z}/7$; the point $P$ generates a subgroup of order $7$ of index $2$.

**31.** **Strategy.** The singular locus is the common zero set of $f$ and its partials; it is proper because
otherwise the partials would lie in the principal ideal $(f)$, which is impossible by degree.

**Closedness.** By the Jacobian criterion (Theorem 7.45), $P \in X$ is singular iff $\nabla f(P) = 0$, so
$$X_{\mathrm{sing}} = X \cap V(\partial_1 f,\dots,\partial_n f) = V(f, \partial_1 f, \dots, \partial_n f),$$
an intersection of closed sets, hence closed.

**Properness.** Suppose $X \subseteq V(\partial_i f)$ for all $i$. Since $f$ has no repeated factor, $(f)$ is radical
(Exercise 25), and $X = V(f)$ is irreducible, so $I(X) = (f)$. Hence $\partial_i f \in (f)$, say $\partial_i f =
g_i f$. If $\partial_i f \ne 0$ then $\deg \partial_i f = \deg f - 1 < \deg f \le \deg(g_i f)$, a contradiction;
therefore $\partial_i f = 0$ for all $i$. In characteristic $0$ a polynomial with all partial derivatives zero is
constant (each variable occurs with exponent $e > 0$ only if $\partial_i f \ne 0$), contradicting the hypothesis that
$f$ is nonconstant. Hence $X_{\mathrm{sing}} \subsetneq X$.

**Example.** For $f = y^2 - x^3$ the singular locus is $V(y^2-x^3, -3x^2, 2y) = \{(0,0)\}$, a proper closed
subset of the cuspidal cubic ✓.

## Challenge

**32.** **Strategy.** Noether normalisation exhibits a finitely generated field as a finite extension of a
polynomial ring; a polynomial ring that is a field must be a field of constants.

**Zariski's lemma.** Let $A$ be a field and a finitely generated $k$-algebra. By Noether normalisation (Theorem
7.14), there are $y_1,\dots,y_d \in A$, algebraically independent over $k$, with $A$ integral over $k[y_1,\dots,y_d]$.
Since $A$ is a field, Lemma 7.15 shows that $k[y_1,\dots,y_d]$ is a field. For $d \ge 1$ this is impossible: $y_1$
would have an inverse $h$ with $y_1 h = 1$, but the left side has degree $1+\deg h > 0$ while the right side has
degree $0$. Hence $d = 0$ and $A$ is integral, i.e. algebraic, over $k$.

**Weak Nullstellensatz.** Let $k$ be algebraically closed and let $I \subsetneq k[x_1,\dots,x_n]$. Choose a maximal
ideal $\mathfrak m \supseteq I$. Then $K = k[x]/\mathfrak m$ is a field and a finitely generated $k$-algebra, so it is
algebraic over $k$ by Zariski's lemma; since $k$ is algebraically closed, $K = k$. Let $a_i$ be the image of $x_i$;
then $\mathfrak m = (x_1-a_1,\dots,x_n-a_n)$ and $V(\mathfrak m) = \{(a_1,\dots,a_n)\} \subseteq V(I)$, so $V(I) \ne
\varnothing$.

**Where $\mathbb{R}$ fails.** The argument uses algebraic closure exactly once: to conclude $K = k$ from "$K$ is
algebraic over $k$". Over $\mathbb{R}$ the algebraic closure is $\mathbb{C} \ne \mathbb{R}$, and indeed $K =
\mathbb{R}[x]/(x^2+1) \cong \mathbb{C}$ is a genuine algebraic extension. Correspondingly the maximal ideal
$(x^2+1)$ has empty real zero set, so the weak Nullstellensatz fails over $\mathbb{R}$ — unless one replaces it by
the real Nullstellensatz, which also allows sums of squares in the ideal.

**33.** **Strategy.** Use Riemann–Roch to show that every degree-zero divisor class on a genus-one curve has a
unique representative of the form $(P)-(O)$; then transport the group structure and identify the operation.

**Injectivity of $\Phi$.** Suppose $(P)-(Q) = \operatorname{div}(h)$ for a rational function $h$. If $h$ is
constant then $P = Q$. If $h$ is nonconstant, then $h$ has exactly one zero (at $P$) and one pole (at $Q$), both
simple, so $h$ defines a morphism $E \to \mathbb{P}^1$ of degree $1$; a degree-$1$ morphism between smooth
projective curves is an isomorphism, forcing $E \cong \mathbb{P}^1$ and hence $g(E) = 0$, contradicting $g(E) = 1$.
So $P = Q$.

**Surjectivity of $\Phi$.** Let $D_0$ be a divisor of degree $0$ and put $D := D_0 + (O)$, of degree $1$. By
Riemann–Roch $\ell(D) = \deg D = 1$, so there is a nonzero rational function $h$ with $\operatorname{div}(h) + D \ge
0$. The divisor $\operatorname{div}(h) + D$ has degree $0$ and is effective, hence is zero:
$\operatorname{div}(h) = -D$. Then $-\operatorname{div}(h) = D_0 + (O)$ is an effective divisor of degree $1$, hence
of the form $(P)$ for a unique point $P$, and $D_0 = (P)-(O) = \Phi(P)$.

**The transported law is chord–tangent.** Since $\Phi$ is a bijection and $\operatorname{Pic}^0(E)$ is an abelian
group, $E(k)$ inherits an abelian group structure with identity $\Phi^{-1}(0) = O$. Let $P, Q \in E(k)$, let $L$ be
the line through $P$ and $Q$ (the tangent if $P = Q$), and let $S$ be the third intersection of $L$ with $E$; let $M$
be the line through $O$ and $S$, meeting $E$ at $O, S, R$. As functions on $E$ (restrictions of linear forms on
$\mathbb{P}^2$),
$$\operatorname{div}\Bigl(\frac{L}{M}\Bigr) = (P)+(Q)+(S) - \bigl((O)+(S)+(R)\bigr) = (P)+(Q)-(O)-(R).$$
Hence $(P)-(O) + (Q)-(O) = (R)-(O)$ in $\operatorname{Pic}^0(E)$, i.e. $\Phi(P) + \Phi(Q) = \Phi(R)$ and the
transported sum is $R$. Finally $R = -S$, because the line through $O = [0:1:0]$ and $S = (x_S,y_S)$ is $x = x_S$,
which meets $E$ again at $(x_S,-y_S)$; so $R$ is the reflection of $S$ in the $x$-axis, exactly the definition of
$P + Q$ in Definition 7.52.

**Associativity.** The group law of $\operatorname{Pic}^0(E)$ is associative (addition of divisor classes), and
$\Phi$ is a bijection, so the transported operation is associative. Explicitly, for $P, Q, R \in E(k)$,
$$\Phi((P+Q)+R) = \bigl(\Phi(P)+\Phi(Q)\bigr)+\Phi(R) = \Phi(P)+\bigl(\Phi(Q)+\Phi(R)\bigr) = \Phi(P+(Q+R)),$$
and injectivity of $\Phi$ gives $(P+Q)+R = P+(Q+R)$. $\blacksquare$

**34.** **Strategy.** A morphism $\mathbb{P}^1\to\mathbb{P}^1$ is given by two homogeneous forms of the same degree
with no common zero; injectivity forces that degree to be $1$.

**Step 1: form of a morphism.** Let $\varphi:\mathbb{P}^1\to\mathbb{P}^1$ be a morphism. On the chart $U_0$ with
coordinate $t = T/S$ write $\varphi = [p(t):q(t)]$ with $p, q \in k[t]$ having no common zero; on the chart $U_1$
with coordinate $s = S/T$ write $\varphi = [r(s):u(s)]$. On the overlap $t \ne 0$, $s = 1/t$ and
$$[p(t):q(t)] = [r(1/t):u(1/t)],$$
so $p(t)u(1/t) = q(t)r(1/t)$. Multiplying by a large power of $t$ shows that $p$ and $q$ have the same degree $d$
(after cancelling common factors), and that
$$\varphi([S:T]) = [P(S,T):Q(S,T)]$$
for homogeneous forms $P, Q$ of degree $d$ with no common zero.

**Step 2: injectivity forces $d = 1$.** For a point $[a:b]\in\mathbb{P}^1$, the fibre is the zero set of the binary
form $bP - aQ$ of degree $d$. A nonzero binary form of degree $d$ over an algebraically closed field has exactly $d$
zeros counted with multiplicity. If $d \ge 2$, choose $[a:b]$ not of the form $\varphi(\text{point})$; then $bP -
aQ$ is not the zero form and has at least one zero, and the fibre has $d \ge 2$ points counted with multiplicity, so
$\varphi$ is not injective. Since an automorphism is injective, $d = 1$.

**Step 3: Möbius form.** For $d = 1$ we have $P = aS+bT$, $Q = cS+dT$ with $(a,b) \ne (0,0) \ne (c,d)$ and no common
zero, i.e. $ad - bc \ne 0$. Hence
$$\varphi([S:T]) = [aS+bT : cS+dT],$$
which is the Möbius transformation of the matrix $\begin{pmatrix} a & b\\ c & d\end{pmatrix}\in
\mathrm{GL}_2(k)$. Conversely, any such matrix with $ad-bc \ne 0$ defines a morphism with inverse given by the
inverse matrix, hence an automorphism.

**Conclusion.** $\operatorname{Aut}(\mathbb{P}^1) \cong \mathrm{PGL}_2(k)$.

**35.** **Strategy.** A regular function on the punctured plane is a rational function whose only possible pole is
the origin; a pole of a rational function is a hypersurface, and a hypersurface in $\mathbb{A}^2$ is infinite.

**Step 1: $f$ is rational.** The open set $U = \mathbb{A}^2\setminus\{0\}$ is dense in $\mathbb{A}^2$, so the field
of rational functions of $U$ is $k(x,y)$. A regular function $f$ on $U$ is a rational function: locally it is a
quotient of polynomials, and these local expressions agree on overlaps by density.

**Step 2: write $f = p/q$ in lowest terms.** Since $k[x,y]$ is a UFD, write $f = p/q$ with $p, q$ coprime. On the
open set where $q \ne 0$, $f$ is given by this quotient. If $q$ is nonconstant, then $V(q) \cap U$ is a nonempty
open subset of the curve $V(q)$ on which $f$ is not regular (the denominator vanishes). More precisely, $f$ is
regular at a point $P$ only if $q(P) \ne 0$ or the factor cancels; since $p, q$ are coprime, a point of $V(q)$ with
$p \ne 0$ is a pole, and such points exist because $V(p) \cap V(q)$ is finite (coprime) while $V(q)$ is infinite
(it is a curve, by Corollary 7.43). Hence $V(q) \subseteq \{0\}$, which is impossible for a nonconstant $q$ because
$V(q)$ has dimension $1$ and hence infinitely many points. Therefore $q$ is a nonzero constant and $f \in k[x,y]$.

**Step 3: not affine.** Suppose $U$ were an affine variety. Then the inclusion $\iota : U \hookrightarrow
\mathbb{A}^2$ would correspond to $\iota^* : A(\mathbb{A}^2) = k[x,y] \to A(U) = \mathcal O(U) = k[x,y]$, which is
the identity (every polynomial restricts to itself, and by Step 2 there is nothing else). An isomorphism of
coordinate rings gives an isomorphism of varieties (Corollary 7.26), so $\iota$ would be an isomorphism, in
particular surjective — false, since $0 \notin U$. Hence $U$ is not affine.

**36.** **Strategy.** The group law is given by rational functions with denominators $x_2-x_1$ and $2y_1$; reduction
is compatible with these formulas whenever the denominators remain units, and the degenerate cases reduce to the
statement that a point of good reduction reducing to $O$ is $O$ itself.

**Good reduction.** Let $E$ be given by $y^2 = x^3+ax+b$ with $a,b \in \mathbb{Z}$ and $p \nmid 2\Delta$. Write a
rational point in the standard form $P = (u/w^2, v/w^3)$ with $u,v,w \in \mathbb{Z}$, $w > 0$, and $\gcd(u,w) =
\gcd(v,w) = 1$. Say $P$ has **good reduction** at $p$ if $p \nmid w$; then
$$\tilde P := (\tilde u \tilde w^{-2}, \tilde v \tilde w^{-3}) \in E(\mathbb{F}_p)$$
is well defined, because the pair $(u/w^2, v/w^3)$ is unique and $p \nmid 2\Delta$ ensures the reduced curve is
smooth.

**Homomorphism.** Let $P, Q$ have good reduction. If $x_1 \ne x_2$ in $\mathbb{Q}$ and $\tilde x_1 \ne \tilde x_2$
in $\mathbb{F}_p$, then every quantity in the formulas of Theorem 7.53 ($\lambda$, $x_3$, $y_3$) is a rational
function with denominator a product of $x_2-x_1$ and (for the doubling case) $2y_1$, both of which reduce to units;
hence $\widetilde{P+Q} = \tilde P + \tilde Q$. If $\tilde x_1 = \tilde x_2$ then $\tilde Q = \pm\tilde P$; in the
case $\tilde Q = -\tilde P$ both sides equal $O$; in the case $\tilde Q = \tilde P$ the doubling formula applies,
and its denominator $2y_1$ reduces to $2\tilde y_1$, which is either a unit or $0$; in the latter case $\tilde P$ is
a point of order $2$ and both sides again give $O$. Thus reduction is a homomorphism wherever it is defined, with
the degenerate cases matching the group law on $\tilde E$.

**Torsion of order prime to $p$.** Let $P$ have finite order $N$ with $p \nmid N$. Then $N\tilde P = \widetilde{NP}
= \tilde O = O$. If $d$ were the order of $\tilde P$ with $d < N$, then $\widetilde{dP} = d\tilde P = O$, so $dP$
is a point of good reduction (a multiple of a good point) reducing to $O$; but a point of good reduction reducing
to $O$ must be $O$ itself (such a point has $v_p(x) < 0$, contradicting $p \nmid w$). Hence $dP = O$, so $N \mid d$
and $d = N$ (as $d \le N$). Therefore reduction is injective on the $N$-torsion for $p \nmid N$.
