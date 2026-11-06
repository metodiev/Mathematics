# Circles — Solutions

> Companion to [the exercises](exercises.md) and [the tutorial](README.md). Each solution states the strategy
> first, then every step. Numbers match the exercise numbers.

## Beginner

**1.** *Strategy: use $C = 2\pi r$ and $K = \pi r^2$.*

$C = 2\pi\cdot 7 = 14\pi \approx 43.98$ and $K = \pi\cdot 7^2 = 49\pi \approx 153.94$.

**2.** The diameter is twice the radius, so $r = 10$. Then $C = 2\pi\cdot 10 = 20\pi \approx 62.83$ and
$K = \pi\cdot 100 = 100\pi \approx 314.16$.

**3.** From $2\pi r = 36\pi$ we get $r = 18$, and then $K = \pi\cdot 18^2 = 324\pi \approx 1017.88$.

**4.** From $\pi r^2 = 64\pi$ we get $r^2 = 64$ and $r = 8$ (positive), so $C = 2\pi\cdot 8 = 16\pi \approx
50.27$.

**5.** Use $180^\circ = \pi$ radians, that is multiply degrees by $\pi/180$ and radians by $180/\pi$.

(a) $30^\circ = \tfrac{\pi}{6}$; (b) $45^\circ = \tfrac{\pi}{4}$; (c) $120^\circ = \tfrac{2\pi}{3}$;
(d) $270^\circ = \tfrac{3\pi}{2}$; (e) $\tfrac{\pi}{6} = 30^\circ$; (f) $\tfrac{3\pi}{4} = 135^\circ$;
(g) $\tfrac{5\pi}{3} = 300^\circ$.

**6.** In radians $\theta = 60^\circ = \tfrac{\pi}{3}$. By Theorem 7.8, $s = 6\cdot\tfrac{\pi}{3} = 2\pi \approx
6.28$; by Theorem 7.9, $K = \tfrac12\cdot 36\cdot\tfrac{\pi}{3} = 6\pi \approx 18.85$.

**7.** Here $\theta = 120^\circ = \tfrac{2\pi}{3}$. Then $s = 9\cdot\tfrac{2\pi}{3} = 6\pi \approx 18.85$ and
$K = \tfrac12\cdot 81\cdot\tfrac{2\pi}{3} = 27\pi \approx 84.82$.

*Pitfall:* feeding $120$ instead of $\tfrac{2\pi}{3}$ into the formulas gives an answer about $57$ times too
large.

**8.** Let $M$ be the midpoint of the chord. By Theorem 7.4, $OM \perp AB$, and $AM = 12$. Pythagoras in the
right triangle $OMA$ gives $OM = \sqrt{13^2-12^2} = \sqrt{169-144} = 5$.

**9.** Half the chord is $\sqrt{10^2-6^2} = \sqrt{100-36} = 8$, so the chord has length $2\cdot 8 = 16$
(Corollary 7.5).

**10.** (a) The inscribed angle is half the central angle on the same arc: $100^\circ/2 = 50^\circ$.
(b) The two arcs make a full circle, so the other arc measures $360^\circ-100^\circ = 260^\circ$ and the
inscribed angle standing on it is $130^\circ$. Check: the four points form a cyclic quadrilateral, and
$50^\circ + 130^\circ = 180^\circ$ by Theorem 7.15.

**11.** Label the angles in order $A = 100^\circ$, $B = 65^\circ$, $C = 80^\circ$, $D$. By Theorem 7.15,
$\angle B + \angle D = 180^\circ$, so $D = 115^\circ$. The other pair checks:
$\angle A + \angle C = 100^\circ + 80^\circ = 180^\circ$. Both conditions hold, so the data are consistent.

**12.** The radius to the point of contact is perpendicular to the tangent (Theorem 7.18), so $OPT$ is right
angled at $T$ with hypotenuse $OP = 13$ and leg $OT = 5$. Hence
$PT = \sqrt{13^2-5^2} = \sqrt{169-25} = 12$.

## Intermediate

**13.** *Strategy: use the two-tangent theorem to split the $90^\circ$ angle, then a $45^\circ$ right
triangle.*

By Theorem 7.19, $PA = PB$ and $OP$ bisects $\angle APB$, so $\angle APO = 45^\circ$. Also $OA \perp PA$
(Theorem 7.18), so triangle $OAP$ is right-angled at $A$ with a $45^\circ$ angle at $P$; hence its other acute
angle is $45^\circ$ and the triangle is isosceles (Theorem 7.7 of [Triangles](../02-triangles/README.md)).
Therefore $OA = AP = 9$, that is $r = 9$, and

$$
OP = \sqrt{OA^2+AP^2} = \sqrt{81+81} = 9\sqrt2 \approx 12.73 .
$$

**14.** By Theorem 7.23, $6\cdot 8 = 3\cdot y$, so $y = 16$.

**15.** Theorem 7.23 gives $x(x+4) = 5\cdot 9 = 45$, that is $x^2+4x-45 = 0$. Factorising,
$(x+9)(x-5) = 0$, so $x = 5$ (a length is positive). The chord is cut into pieces $5$ and $9$, like the other.

**16.** By Theorem 7.24, $PA\cdot PB = PC\cdot PD$, so $5\cdot 20 = 4\cdot PD$ and $PD = 25$.

**17.** By Theorem 7.25, $PT^2 = PA\cdot PB$, so $144 = 9\cdot PB$ and $PB = 16$. Since $A$ lies between $P$
and $B$, $AB = PB - PA = 16 - 9 = 7$.

**18.** (a) By Theorem 7.27, $(x-3)^2 + (y+4)^2 = 5^2 = 25$.
(b) Complete the squares: $x^2-6x = (x-3)^2-9$ and $y^2+8y = (y+4)^2-16$, so the equation becomes
$(x-3)^2 + (y+4)^2 = 9+16+11 = 36$. The centre is $(3,-4)$ and the radius is $6$.

*Pitfall:* reading the centre as $(-3,4)$ — the signs in $(x-h)^2+(y-k)^2$ are reversed relative to the
coordinates of the centre.

**19.** Compute $x^2+y^2$ and compare with $61$.
(a) $25+36 = 61$: the point lies **on** the circle.
(b) $4+49 = 53 < 61$: the point is **inside**.
(c) $0 < 61$: the centre is **inside** (as it must be).

**20.** $AB$ is a diameter, so by Thales' theorem (Corollary 7.13) $\angle ACB = 90^\circ$. Then
$\angle BAC = 180^\circ - 90^\circ - 35^\circ = 55^\circ$ by the angle sum of the triangle.

**21.** *Strategy: combine the parallelogram property with the cyclic property.*

In a parallelogram opposite angles are equal (proved by splitting it into two congruent triangles along a
diagonal). In a cyclic quadrilateral opposite angles are supplementary (Theorem 7.15). Hence at a vertex $A$
with opposite angle $C$,

$$
\angle A = \angle C \quad\text{and}\quad \angle A + \angle C = 180^\circ,
$$

so $2\angle A = 180^\circ$ and $\angle A = 90^\circ$. Every angle of the parallelogram is then $90^\circ$, so it
is a rectangle. $\blacksquare$

**22.** *Strategy: compute each chord's distance from the centre, then compare.*

Half of the chord of length $12$ is $6$, so its distance from the centre is $\sqrt{10^2-6^2} = 8$. Half of the
chord of length $16$ is $8$, so its distance is $\sqrt{10^2-8^2} = 6$. Both chords are on the same side of the
centre, so the distance between them is $8-6 = 2$.

## Advanced

**23.** Half-chords are $5$ and $12$, so the distances from the centre are

$$
\sqrt{13^2-5^2} = 12, \qquad \sqrt{13^2-12^2} = 5 .
$$

If the chords are on *opposite* sides of the centre the distance between them is $12+5 = 17$; if they are on
the *same* side it is $12-5 = 7$. Both configurations exist, so the problem has two answers.

*Pitfall:* quoting only $17$, the configuration that the usual picture suggests.

**24.** Half the chord is $8$, so $r^2 = 8^2+6^2 = 64+36 = 100$ and $r = 10$ (Corollary 7.5). The chord at
distance $8$ from the centre has half-length $\sqrt{100-64} = 6$, hence length $12$.

**25.** From $s = r\theta$ we get $\theta = s/r = 15/10 = 1.5$ radians (about $85.94^\circ$). The area is
$K = \tfrac12 r^2\theta = \tfrac12\cdot 100\cdot 1.5 = 75$.

**26.** By Theorem 7.23, $PA\cdot PB = PC\cdot PD$. Since $P$ is the midpoint of $CD$, $PC = PD$, so
$PC^2 = 3\cdot 8 = 24$ and $PC = 2\sqrt6$. Hence $CD = 2\,PC = 4\sqrt6 \approx 9.80$.

**27.** Let $AB = CD$ be chords of a circle with centre $O$. By Theorem 7.6, equal chords subtend equal central
angles, so $\angle AOB = \angle COD$ and therefore the minor arcs $AB$ and $CD$ have equal measure. The major
arcs are the complements of the minor arcs in the full circle, so each measures $360^\circ$ minus the minor
arc; equal minor arcs therefore give equal major arcs. Conversely, equal minor arcs give equal central angles
and hence equal chords. $\blacksquare$

**28.** *Strategy: put the angle inside a triangle whose other two angles are inscribed.*

In triangle $APC$, the angle $\angle APB$ is an exterior angle at $P$, because $A$, $P$, $B$ are collinear.
Hence, by the exterior angle theorem (Corollary 7.4 of [Triangles](../02-triangles/README.md)),

$$
\angle APB = \angle PAC + \angle PCA .
$$

Now $\angle PAC = \angle BAC$, since the ray $AP$ is the ray $AB$; this inscribed angle subtends the arc $BC$, so
$\angle PAC = \tfrac12\, m(\text{arc } BC)$ by Theorem 7.11. Likewise $\angle PCA = \angle DCA$ subtends the arc
$AD$, so $\angle PCA = \tfrac12\, m(\text{arc } AD)$. Adding,

$$
\angle APB = \tfrac12\left(m(\text{arc } BC) + m(\text{arc } AD)\right). \qquad \blacksquare
$$

**29.** Let $AB \parallel DC$ in the cyclic quadrilateral $ABCD$. Since $AB \parallel DC$, the same-side interior
angles at $A$ and $D$ sum to $180^\circ$ (Theorem 7.2 of
[Triangles](../02-triangles/README.md)). Since $ABCD$ is cyclic, $\angle A + \angle C = 180^\circ$ by
Theorem 7.15. Comparing, $\angle D = \angle C$: the angles at the ends of the base $DC$ are equal.

Drop perpendiculars from $A$ and $B$ to the line $DC$, meeting it at $A'$ and $B'$. The right triangles $AA'D$
and $BB'C$ have $\angle D = \angle C$ (just proved), right angles at $A'$ and $B'$, and $AA' = BB'$ (the
distance between the parallel lines $AB$ and $DC$). So the triangles are congruent by AAS, and $AD = BC$. A
trapezium with equal legs is isosceles. $\blacksquare$

**30.** *Strategy: translate "parallel" into equal alternate angles, and use the alternate segment theorem.*

Suppose first that the tangent at $P$ is parallel to $AB$. Since $AP$ is a transversal of the parallel lines,
the angle between the tangent and $PA$ equals $\angle PAB$ (alternate interior angles). By the alternate
segment theorem (Theorem 7.21) the same angle equals $\angle PBA$. Hence $\angle PAB = \angle PBA$, so
$PA = PB$ by Theorem 7.7 of [Triangles](../02-triangles/README.md), and equal chords cut off equal arcs
(Theorem 7.6); that is, $P$ is the midpoint of the arc $AB$ on which it lies.

Conversely, if $P$ is that midpoint, then $PA = PB$, so $\angle PAB = \angle PBA$. By Theorem 7.21 the angle
between the tangent at $P$ and $PA$ equals $\angle PBA = \angle PAB$; the tangent therefore makes with $PA$ the
same angle as $AB$ does, on the alternate side, so the tangent is parallel to $AB$ (converse of the alternate
angle theorem, Theorem 7.2 of [Triangles](../02-triangles/README.md)). $\blacksquare$

## Challenge

**31.** *Strategy: use tangent lengths from the three vertices and the fact that the incentre is at distance
$r$ from both legs.*

Let the incircle touch $BC$, $CA$, $AB$ at $X$, $Y$, $Z$. Tangent segments from one exterior point are equal
(Theorem 7.19), so write

$$
AZ = AY = x, \qquad BZ = BX = y, \qquad CX = CY = z .
$$

Since the sides are the sums of these pieces, $x+y = c$, $y+z = a$ and $z+x = b$. Adding the last two
equations and subtracting the first gives

$$
2z = (a+b) - c, \qquad\text{so}\qquad z = \tfrac12(a+b-c).
$$

Now take the right angle at $C$. The quadrilateral $CX I Y$ has a right angle at $C$ (given), at $X$ (the radius
to the point of contact is perpendicular to $BC$) and at $Y$ (similarly), so it is a rectangle; and $IX = IY =
r$, so it is a square. Therefore $CX = CY = r$, and since $CX = z$,

$$
r = z = \tfrac12(a+b-c). \qquad \blacksquare
$$

*Check:* in the $3$–$4$–$5$ triangle, $r = \tfrac12(3+4-5) = 1$; the area is $6$ and the semiperimeter $6$, and
$r = K/s = 1$ by Theorem 7.46 of [Triangles](../02-triangles/README.md). ✓

**32.** *Strategy: split $AC$ by a point $E$ chosen so that two pairs of triangles are similar.*

Let $ABCD$ be cyclic with $A$, $B$, $C$, $D$ in that order. Choose $E$ on the segment $AC$ such that
$\angle ABE = \angle CBD$.

*First pair.* In triangles $ABE$ and $DBC$: $\angle ABE = \angle DBC$ by construction, and
$\angle BAE = \angle BAC = \angle BDC$ because both subtend the arc $BC$ (Corollary 7.12). So the triangles are
similar by AA, and

$$
\frac{AB}{DB} = \frac{AE}{DC}, \qquad\text{that is}\qquad AE = \frac{AB\cdot DC}{BD}. \tag{1}
$$

*Second pair.* Consider triangles $ABD$ and $EBC$. Since $\angle ABE = \angle CBD$, adding $\angle EBD$ to both
gives $\angle ABD = \angle EBC$. Also $\angle ADB = \angle ACB = \angle ECB$, both subtending the arc $AB$. So
the triangles are similar by AA, and

$$
\frac{AD}{EC} = \frac{BD}{BC}, \qquad\text{that is}\qquad EC = \frac{AD\cdot BC}{BD}. \tag{2}
$$

*Conclusion.* Since $E$ lies on $AC$, $AC = AE + EC$. Adding (1) and (2),

$$
AC = \frac{AB\cdot DC + AD\cdot BC}{BD}, \qquad\text{so}\qquad
AC\cdot BD = AB\cdot CD + BC\cdot AD. \qquad \blacksquare
$$

*Remark:* for a rectangle with sides $p$ and $q$ we have $AC = BD$, and Ptolemy reads $AC^2 = p^2+q^2$, which
is Pythagoras. For a square of side $s$ it reads $s\sqrt2\cdot s\sqrt2 = s^2+s^2$, the same identity.

**33.** *Strategy: express one side by the inscribed angle theorem, then eliminate $\sin C$ using the area
formula.*

Let $R$ be the circumradius and consider the side $AB = c$ and the angle $\angle C$ opposite it. Let $M$ be the
midpoint of $AB$ and $O$ the centre. By Theorem 7.4, $OM \perp AB$; and $\angle AOB = 2\angle C$ by the
inscribed angle theorem (Theorem 7.11), so in the right triangle $OMA$ the angle at $O$ is $C$. Therefore

$$
AM = R\sin C, \qquad\text{so}\qquad c = 2R\sin C . \tag{3}
$$

On the other hand, the area is $K = \tfrac12 ab\sin C$ (Theorem 7.39 of
[Triangles](../02-triangles/README.md)), so $\sin C = \dfrac{2K}{ab}$. Substituting into (3),

$$
c = 2R\cdot\frac{2K}{ab}, \qquad\text{hence}\qquad R = \frac{abc}{4K}. \qquad \blacksquare
$$

*Check:* for the $13$–$14$–$15$ triangle, $K = 84$ and $R = \tfrac{13\cdot 14\cdot 15}{4\cdot 84} = 8.125$. ✓

**34.** *Strategy: the half-chord is the leg of a right triangle with hypotenuse $R$ and other leg $r$.*

Let the outer circle have radius $R$, the inner one radius $r$, and let the chord of the outer circle be
tangent to the inner circle at $T$. The tangent is perpendicular to the radius at $T$ (Theorem 7.18), so the
distance from the common centre to the chord is $r$. Half the chord is

$$
\frac{d}{2} = \sqrt{R^2-r^2}
$$

by Corollary 7.5 applied to the outer circle. Squaring, $\left(\tfrac{d}{2}\right)^2 = R^2-r^2$, and the area
of the annulus is

$$
\pi R^2 - \pi r^2 = \pi\left(R^2-r^2\right) = \pi\left(\frac{d}{2}\right)^2 . \qquad \blacksquare
$$

For $d = 8$ this is $\pi\cdot 16 = 16\pi \approx 50.27$.

**35.** *Strategy: Thales gives the right angle, and the altitude splits the right triangle into similar
triangles.*

Since $AB$ is a diameter, $\angle ACB = 90^\circ$ by Thales' theorem (Corollary 7.13). So $ABC$ is right-angled
at $C$ and $CD$ is the altitude to the hypotenuse $AB$.

Triangles $ACD$ and $CBD$ are both right-angled at $D$, and $\angle ACD = 90^\circ-\angle A = \angle CBD$,
since $\angle A+\angle B = 90^\circ$ in the right triangle $ABC$. So $ACD \sim CBD$ by AA, with the
correspondence $A \leftrightarrow C$, $C \leftrightarrow B$, $D \leftrightarrow D$, giving

$$
\frac{AD}{CD} = \frac{CD}{DB}, \qquad\text{that is}\qquad CD^2 = AD\cdot DB .
$$

Likewise $ACD \sim ABC$ (common angle at $A$, right angles at $D$ and $C$), so
$\dfrac{AC}{AB} = \dfrac{AD}{AC}$ and $AC^2 = AD\cdot AB$. $\blacksquare$

**36.** *Strategy: two circles tangent at $T$ share the point, and the centres are determined by distances to
it.*

Let $O_1$ be the centre of the larger circle (radius $R$) and $O_2$ that of the smaller (radius $r$), with
$r < R$. Since the circles are internally tangent at $T$, the point $T$ lies on both circles and is their only
common point. For internal tangency the distance between the centres is the difference of the radii — the
triangle inequality gives $O_1O_2 \ge R-r$, and equality is exactly the tangent case, because a strictly
greater distance leaves the two circles crossing in two points. Hence

$$
O_1T = R, \qquad O_2T = r, \qquad O_1O_2 = R - r,
$$

and therefore $O_1O_2 + O_2T = (R-r) + r = R = O_1T$. This says that $O_2$ lies on the segment $O_1T$, so the
three points are collinear, in the order $O_1$, $O_2$, $T$.

The tangent to the larger circle at $T$ is perpendicular to $O_1T$ (Theorem 7.18). Since $O_1$, $O_2$, $T$ are
collinear, $O_2T$ is the same line as $O_1T$, so that tangent is also perpendicular to $O_2T$; by Theorem 7.18
again, it is tangent to the smaller circle at $T$. $\blacksquare$
