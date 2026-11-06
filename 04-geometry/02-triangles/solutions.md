# Triangles — Solutions

> Companion to [the exercises](exercises.md) and [the tutorial](README.md). Each solution states the strategy
> first, then every step. Numbers match the exercise numbers.

## Beginner

**1.** *Strategy: compare the sides, then test the largest angle by comparing $a^2+b^2$ with $c^2$.*

(a) $7 = 7 = 7$: **equilateral**, hence equiangular with three $60^\circ$ angles by Theorem 7.10, so **acute**.

(b) All sides different: **scalene**. And $6^2+8^2 = 36+64 = 100 = 10^2$, so by the converse of Pythagoras
(Theorem 7.33) the angle opposite $10$ is a right angle: **right**.

(c) $5 = 5 \ne 8$: **isosceles**. Here $5^2+5^2 = 50 < 64 = 8^2$, so the angle opposite the side $8$ is
obtuse (the three cases of Remark 7.35): **obtuse**.

(d) All sides different: **scalene**. And $9^2+11^2 = 81+121 = 202 > 169 = 13^2$, so the angle opposite
$13$ is acute, and being the largest angle the other two are smaller still: **acute**.

*Pitfall:* deciding the angle type from the *lengths* without comparing $a^2+b^2$ with $c^2$ — for instance
guessing that $5,5,8$ is acute because the sides are "close".

**2.** Use Theorem 7.3, $C = 180^\circ - A - B$.

(a) $180^\circ - 37^\circ - 58^\circ = 85^\circ$; all angles are less than $90^\circ$: **acute**.
(b) $180^\circ - 90^\circ - 45^\circ = 45^\circ$; one angle is $90^\circ$: **right** (and isosceles, since the
other two angles are equal).
(c) $180^\circ - 110^\circ - 25^\circ = 45^\circ$; one angle exceeds $90^\circ$: **obtuse**.
(d) $180^\circ - 60^\circ - 60^\circ = 60^\circ$; all angles equal, so by Theorem 7.10 the triangle is
**equilateral**, in particular acute.

**3.** The two base angles are equal (Theorem 7.6) and the three angles sum to $180^\circ$ (Theorem 7.3).

(a) The two base angles sum to $180^\circ - 40^\circ = 140^\circ$, so each is $70^\circ$.
(b) The vertex angle is $180^\circ - 2\cdot 65^\circ = 50^\circ$.
(c) The vertex angle is $180^\circ - 2\cdot 80^\circ = 20^\circ$.

**4.** *Strategy: only the largest side needs testing (Theorem 7.11 and the remark after it); equality gives a
degenerate triangle.*

(a) $3+4 = 7$, equal to the largest side: **no** (degenerate, zero area).
(b) $5+6 = 11 > 10$: **yes**; the other two inequalities hold automatically since $10$ is largest.
(c) $2+2 = 4 < 5$: **no**.
(d) $7+9 = 16 > 13$: **yes**.
(e) $1+2 = 3$, equal to the largest side: **no**.

**5.** Pythagoras, $c^2 = a^2+b^2$ (Theorem 7.31); when the hypotenuse is given, $a^2 = c^2-b^2$.

(a) $\sqrt{25+144} = \sqrt{169} = 13$.
(b) $\sqrt{49+576} = \sqrt{625} = 25$.
(c) $\sqrt{676-100} = \sqrt{576} = 24$.
(d) $\sqrt{1+1} = \sqrt2 \approx 1.414$.

*Pitfall:* in (c) subtracting the squares is correct because $26$ is the hypotenuse; subtracting the sides
themselves would give $16$, which is wrong.

**6.** The two exact triangles of Theorems 7.37 and 7.38.

(a) $45^\circ$–$45^\circ$–$90^\circ$ with leg $l = 9$: hypotenuse $l\sqrt2 = 9\sqrt2 \approx 12.73$.
(b) $30^\circ$–$60^\circ$–$90^\circ$ with shortest side $x = 4$: hypotenuse $2x = 8$ and the other leg
$x\sqrt3 = 4\sqrt3 \approx 6.93$.
(c) $45^\circ$–$45^\circ$–$90^\circ$ with hypotenuse $c = 12$: legs $c/\sqrt2 = 6\sqrt2 \approx 8.49$.
(d) $30^\circ$–$60^\circ$–$90^\circ$ with hypotenuse $18$: legs $9$ (opposite $30^\circ$) and $9\sqrt3 \approx
15.59$ (opposite $60^\circ$).

**7.** $K = \tfrac12 bh$ (Theorem 7.21).

(a) $\tfrac12\cdot 14\cdot 9 = 63$.
(b) $\tfrac12\cdot 6.4\cdot 2.5 = 8$.
(c) The legs of a right triangle are perpendicular, so one is the base and the other the height:
$\tfrac12 \cdot 9 \cdot 12 = 54$.

**8.** Let the angles be $2x$, $3x$, $4x$. Theorem 7.3 gives $9x = 180^\circ$, so $x = 20^\circ$ and the angles
are $40^\circ$, $60^\circ$, $80^\circ$. All are less than $90^\circ$ and all are different, so the triangle is
**acute and scalene**.

**9.** (a) $C = 180^\circ - 52^\circ - 71^\circ = 57^\circ$.
(b) By Corollary 7.4 the exterior angle at $C$ equals $A + B = 52^\circ + 71^\circ = 123^\circ$. Check:
$123^\circ + 57^\circ = 180^\circ$, as an exterior and interior angle at the same vertex must be.

**10.** Match the given parts against Definition 7.14, checking whether the angle is *included*.

(a) Two sides and the angle between them: **SAS**.
(b) Two angles and a side that is not between them ($BC$ is opposite $A$, not between the angles $A$ and
$B$): **AAS**.
(c) Three sides: **SSS**.
(d) Right angle, hypotenuse $AC = DF$ and leg $AB = DE$: **RHS**.
(e) Two sides and the angle at $B$, which is *not* included between $AB$ and $AC$: **none** — this is the SSA
pattern of Example 7.19, and it does not force congruence.

**11.** Perimeter $= 3\cdot 10 = 30$. The altitude of an equilateral triangle bisects the base (Theorem 7.38
and its proof), so it is the leg of a right triangle with hypotenuse $10$ and other leg $5$:
$h = \sqrt{100-25} = 5\sqrt3 \approx 8.66$. Area $= \tfrac12\cdot 10\cdot 5\sqrt3 = 25\sqrt3 \approx 43.30$.

**12.** (a) **Circumcentre** $O$ — Theorem 7.42 characterises the perpendicular bisectors, and Theorem 7.43
shows the three meet there.
(b) **Incentre** $I$ — Theorem 7.44 and Theorem 7.45.
(c) **Centroid** $G$ — Theorem 7.47.
(d) **Orthocentre** $H$ — Theorem 7.48.

## Intermediate

**13.** Heron's formula (Theorem 7.40), $K = \sqrt{s(s-a)(s-b)(s-c)}$.

(a) $s = \tfrac12(7+8+9) = 12$, so
$K = \sqrt{12\cdot 5\cdot 4\cdot 3} = \sqrt{720} = 12\sqrt5 \approx 26.83$.
(b) $s = \tfrac12(5+5+6) = 8$, so $K = \sqrt{8\cdot 3\cdot 3\cdot 2} = \sqrt{144} = 12$.

*Check for (b):* the altitude to the side $6$ is $\sqrt{25-9} = 4$, so $K = \tfrac12\cdot 6\cdot 4 = 12$. ✓

**14.** (a) The triangle is right-angled because $6^2+8^2 = 100 = 10^2$ (Theorem 7.33), so the legs $6$ and $8$
are perpendicular and $K = \tfrac12\cdot 6\cdot 8 = 24$. Heron's formula: $s = 12$ and
$K = \sqrt{12\cdot 6\cdot 4\cdot 2} = \sqrt{576} = 24$. ✓
(b) $s = 12$, and by Theorem 7.46, $r = K/s = 24/12 = 2$.

**15.** By Theorem 7.23 (basic proportionality), $AD/DB = AE/EC$ and $DE/BC = AD/AB$.

(a) $\tfrac{3}{5} = \tfrac{4}{EC}$, so $EC = \tfrac{20}{3} \approx 6.67$.
(b) $AB = AD + DB = 8$, so $DE/BC = 3/8$.
(c) $\tfrac{6}{BC} = \tfrac38$, hence $BC = \tfrac{6\cdot 8}{3} = 16$.

*Pitfall:* using $AD/DB$ where $AD/AB$ is needed. The two ratios differ by the factor $\tfrac{8}{5}$ here.

**16.** Similarity multiplies lengths by $k$ and areas by $k^2$ (Theorem 7.29).

With $k = \tfrac34$ the area ratio is $\left(\tfrac34\right)^2 = \tfrac{9}{16}$, so
$\tfrac{45}{A} = \tfrac{9}{16}$ and $A = 45\cdot\tfrac{16}{9} = 80$. Perimeters are lengths, so they are in the
ratio $3:4$.

**17.** The centroid divides every median in the ratio $2:1$ from the vertex (Theorem 7.47).

(a) $AG = \tfrac23\cdot 18 = 12$ and $GM = \tfrac13\cdot 18 = 6$.
(b) If $AG = 10$ then $10 = \tfrac23 m$, so $m = 15$.

**18.** $K = \tfrac12 ab\sin C$ (Theorem 7.39), with $\sin 30^\circ = \tfrac12$ and
$\sin 150^\circ = \sin 30^\circ = \tfrac12$ (Definition 7.36).

(a) $K = \tfrac12\cdot 8\cdot 11\cdot \tfrac12 = 22$.
(b) $K = \tfrac12\cdot 6\cdot 10\cdot \tfrac12 = 15$.

*Pitfall:* using $\sin 150^\circ$ as negative or as $\sin 60^\circ$. The supplementary-angle rule of
Definition 7.36 keeps the sine positive.

**19.** *Strategy: fix $AB = 10$ as the base and compute the altitude; the foot of the altitude can lie on
either side of $A$.*

The area is $56 = \tfrac12\cdot 10\cdot h$, so $h = 11.2$. In the right triangle formed by the altitude from
$C$ and the side $AC = 14$,

$$
AH = \sqrt{14^2 - 11.2^2} = \sqrt{196-125.44} = \sqrt{70.56} = 8.4 .
$$

The foot $H$ can lie on either side of $A$, so the signed distance from $B$ to $H$ is
$BH = 10 + 8.4 = 18.4$ or $BH = 10 - 8.4 = 1.6$. In each case Pythagoras in the right triangle $BCH$ gives

$$
BC = \sqrt{11.2^2 + 18.4^2} = \sqrt{125.44+338.56} = \sqrt{464} = 4\sqrt{29} \approx 21.54,
$$
$$
BC = \sqrt{11.2^2 + 1.6^2} = \sqrt{125.44+2.56} = \sqrt{128} = 8\sqrt2 \approx 11.31 .
$$

Both are genuine triangles: $4\sqrt{29}$ needs $10 + 14 > 21.54$, true; $8\sqrt2$ needs $10+8\sqrt2 > 14$,
that is $21.31 > 14$, true. So the third side is $8\sqrt2$ or $4\sqrt{29}$.

*Pitfall:* reporting only one answer. The data (two sides and an area) do not fix the triangle, exactly as in
the SSA example.

**20.** *Strategy: find congruent triangles sharing the median.*

In triangles $ABD$ and $ACD$: $AB = AC$ (given), $BD = DC$ ($D$ is the midpoint) and $AD$ is common. So
$\triangle ABD \cong \triangle ACD$ by SSS (Theorem 7.17). Hence $\angle ADB = \angle ADC$. These two angles are
supplementary by Theorem 7.1 and equal, so each is $90^\circ$: $AD \perp BC$.

**21.** Draw the diagonal $AC$. In triangles $ABC$ and $CDA$: $AB = CD$, $BC = DA$ (given) and $AC$ is common,
so $\triangle ABC \cong \triangle CDA$ by SSS.

Corresponding angles give $\angle BAC = \angle DCA$. These are alternate interior angles for the lines $AB$
and $CD$ with transversal $AC$; being equal, the lines are parallel by the converse part of Theorem 7.2, so
$AB \parallel CD$. Likewise $\angle BCA = \angle DAC$ shows $BC \parallel AD$.

**22.** *Strategy: two right triangles with the same ladder.*

Initially $13^2 = 5^2 + h^2$, so $h = \sqrt{169-25} = 12$ m. Afterwards $13^2 = 12^2 + h'^2$, so
$h' = \sqrt{169-144} = 5$ m. The top slides down $12 - 5 = 7$ m.

*Remark:* the two heights $12$ and $5$ are the legs of a $5$–$12$–$13$ triangle; the ladder is the same
length in both positions, which is why the same triple appears twice with the legs exchanged.

## Advanced

**23.** *Strategy: bound each median by the two adjacent sides.*

Let $AM = m_a$ and extend $AM$ beyond $M$ to $D$ with $MD = AM$. Triangles $AMB$ and $DMC$ are congruent by SAS
(equal vertical angles at $M$, $BM = MC$), so $BD = AB = c$. In triangle $ABD$ the triangle inequality
(Theorem 7.11) gives

$$
c + b = AB + BD > AD = 2m_a, \qquad\text{so}\qquad m_a < \frac{b+c}{2}.
$$

Adding the three such inequalities,

$$
m_a + m_b + m_c < \frac{b+c}{2} + \frac{c+a}{2} + \frac{a+b}{2} = a+b+c. \qquad \blacksquare
$$

**24.** *Strategy: use the centroid, which lies inside the triangle, and compare each of $AG$, $BG$, $CG$ with
a side.*

The centroid $G$ is not on any side, so $A, B, G$ form a genuine triangle and Theorem 7.11 gives
$AG + BG > AB = c$; similarly $BG + CG > a$ and $CG + AG > b$. Adding,

$$
2\,(AG+BG+CG) > a+b+c .
$$

By Theorem 7.47, $AG = \tfrac23 m_a$, $BG = \tfrac23 m_b$ and $CG = \tfrac23 m_c$, so
$AG+BG+CG = \tfrac23(m_a+m_b+m_c)$ and

$$
\tfrac43 (m_a+m_b+m_c) > a+b+c, \qquad\text{that is}\qquad m_a+m_b+m_c > \tfrac34 (a+b+c). \qquad \blacksquare
$$

**25.** *Strategy: work with the centroid, which divides the equal medians into equal pieces.*

Let $BE$ and $CF$ be the equal medians, with $E$ the midpoint of $AC$ and $F$ that of $AB$, and let $G$ be the
centroid. By Theorem 7.47, $BG = \tfrac23 BE = \tfrac23 CF = CG$ and $GE = \tfrac13 BE = \tfrac13 CF = GF$.

In triangles $BGF$ and $CGE$: $BG = CG$, $GF = GE$, and $\angle BGF = \angle CGE$ (vertical angles, hence
equal by Theorem 7.1 applied twice). So the triangles are congruent by SAS, and $BF = CE$. Doubling both sides
gives $AB = 2BF = 2CE = AC$. $\blacksquare$

**26.** *Strategy: two isosceles triangles sharing the vertex $A$.*

Since $MA = MB$, triangle $AMB$ is isosceles and $\angle MAB = \angle ABM = B$ (Theorem 7.6). Since
$MA = MC$, triangle $AMC$ is isosceles and $\angle MAC = \angle ACM = C$.

The ray $AM$ lies inside $\angle BAC$ (as $M$ is on $BC$), so

$$
A = \angle MAB + \angle MAC = B + C .
$$

By Theorem 7.3, $A + B + C = 180^\circ$, so $A + A = 180^\circ$ and $A = 90^\circ$. $\blacksquare$

This is the converse of the standard fact that the midpoint of the hypotenuse of a right triangle is
equidistant from all three vertices.

**27.** *Strategy: create a triangle in which the bisector is parallel to a side.*

Draw through $C$ the line parallel to $AD$; let it meet the line $AB$ at $E$ (it meets the extension of $AB$
beyond $A$, because $AD$ enters the triangle).

*First step: a ratio.* In triangle $BCE$ the line $AD$ is parallel to $CE$ and meets $BC$ at $D$, $BE$ at $A$.
By Theorem 7.23,

$$
\frac{BD}{DC} = \frac{BA}{AE}. \tag{1}
$$

*Second step: $AE = AC$.* Since $AD \parallel CE$, the alternate interior angles with transversal $AC$ give
$\angle ACE = \angle CAD$, and the corresponding angles with transversal $BE$ give
$\angle AEC = \angle BAD$ (the angle $\angle BAD$ and $\angle AEC$ are in corresponding positions). Because
$AD$ bisects $\angle A$, $\angle BAD = \angle CAD$; hence $\angle AEC = \angle ACE$, and triangle $ACE$ is
isosceles with $AE = AC$ by Theorem 7.7.

Substituting $AE = AC$ into (1) gives $BD/DC = AB/AC$. $\blacksquare$

*Pitfall:* placing $E$ on the segment $AB$ instead of its extension; then the ratio in (1) would involve
$BE$ rather than $BA$ and the argument breaks.

**28.** *Strategy: introduce the altitude from $A$ and use Pythagoras three times.*

Let $H$ be the foot of the altitude from $A$ to the line $BC$, and put $h = AH$ and $x = MH$ as a *signed*
length, positive when $H$ lies on the side of $C$ from $M$. Write $a = BC$, so $BM = MC = \tfrac{a}{2}$. Then
the signed distances from $H$ to $B$ and to $C$ are

$$
BH = \tfrac{a}{2} + x, \qquad CH = \tfrac{a}{2} - x .
$$

Pythagoras in the three right triangles $ABH$, $ACH$, $AMH$ gives

$$
AB^2 = h^2 + \left(\tfrac{a}{2}+x\right)^2, \quad
AC^2 = h^2 + \left(\tfrac{a}{2}-x\right)^2, \quad
AM^2 = h^2 + x^2 .
$$

Adding the first two and expanding the squares,

$$
AB^2 + AC^2 = 2h^2 + 2\cdot\frac{a^2}{4} + 2x^2 = 2\,(h^2+x^2) + \frac{a^2}{2}
= 2\,AM^2 + 2\left(\frac{a}{2}\right)^2 = 2\,AM^2 + 2\,BM^2 . \qquad \blacksquare
$$

The signed $x$ is what makes the computation cover the case in which $H$ falls outside the segment $BC$.

**29.** *Strategy: find two similar right triangles and read off a proportion.*

Let the right angle be at $C$ and let $CD = h$ be the altitude to the hypotenuse $AB$, with $AD = x$ and
$DB = y$. Triangles $ACD$ and $CBD$ are both right-angled at $D$.

Moreover $\angle ACD = 90^\circ - \angle A$ (from the right triangle $ACD$) and $\angle CBD = 90^\circ -
\angle A$ (from the right triangle $ABC$, whose angle sum is $180^\circ$). Hence
$\angle ACD = \angle CBD$, and the two triangles are similar by AA (Theorem 7.26) with the correspondence
$A \leftrightarrow C$, $C \leftrightarrow B$, $D \leftrightarrow D$. Therefore

$$
\frac{AD}{CD} = \frac{CD}{DB}, \qquad\text{that is}\qquad \frac{x}{h} = \frac{h}{y},
$$

and cross-multiplying gives $h^2 = xy$. $\blacksquare$

*Remark:* this is the standard geometric-mean relation for the altitude to the hypotenuse; the same pair of
similar triangles appears in the proof of Theorem 7.31 of [the tutorial](README.md), where it yields
$AC^2 = AB\cdot AD$ and $BC^2 = AB\cdot BD$.

**30.** *Strategy: prove the contrapositive. If the angle at $C$ is right or obtuse, then $a^2+b^2 \le c^2$.*

Let the angle at $C$ be right first. Then $c$ is the hypotenuse and $a^2+b^2 = c^2$ by Theorem 7.31.

Now suppose the angle at $C$ is obtuse. Let $H$ be the foot of the altitude from $A$ to the line $BC$. Since
the angle at $C$ is obtuse, $H$ lies on the line $BC$ beyond $C$, on the far side from $B$. Put $h = AH$ and
$u = CH > 0$. Then $BH = a + u$, and Pythagoras in the right triangles $ACH$ and $ABH$ gives

$$
b^2 = h^2 + u^2, \qquad c^2 = h^2 + (a+u)^2 = h^2 + a^2 + 2au + u^2 .
$$

Subtracting the first identity from the second,

$$
c^2 - b^2 = a^2 + 2au > a^2, \qquad\text{so}\qquad c^2 > a^2+b^2 .
$$

Thus "angle at $C$ right or obtuse" implies $a^2+b^2 \le c^2$, and its contrapositive is the statement to be
proved: if $a^2+b^2 > c^2$, the angle at $C$ is acute. $\blacksquare$

## Challenge

**31.** *Strategy: push the broken path $B \to P \to C$ inside the triangle.*

Since $P$ is strictly inside the triangle, the ray from $B$ through $P$ meets the opposite side $AC$ at a point
$D$ strictly between $A$ and $C$.

Apply Theorem 7.11 twice:

* in triangle $PDC$: $PC < PD + DC$;
* in triangle $ABD$: $BD < AB + AD$.

Adding these inequalities and using $BD = BP + PD$,

$$
PB + PC < PB + PD + DC = BD + DC < AB + AD + DC = AB + AC . \qquad \blacksquare
$$

*Pitfall:* applying the triangle inequality directly to $PBC$ gives $PB + PC > BC$, which is the wrong
direction. The detour through $D$ is what converts the broken path into the two sides $AB$ and $AC$.

**32.** *Strategy: pair $P$ with each side in turn.*

Because $P$ is inside, the three triangles $PAB$, $PBC$, $PCA$ exist, and Theorem 7.11 gives

$$
PA + PB > AB = c, \qquad PB + PC > BC = a, \qquad PC + PA > CA = b .
$$

Adding, $2(PA+PB+PC) > a+b+c$, and dividing by $2$ gives $PA + PB + PC > s$. $\blacksquare$

*Remark:* by Exercise 31 the sum is also less than $AB + AC$ plus a similar bound, so the sum of the distances
to the vertices is trapped between $s$ and the perimeter; both bounds are sharp for triangles degenerating
towards a segment.

**33.** *Strategy: fix the perimeter, write the area by Heron's formula, and maximise the product with the
given inequality.*

Let the perimeter be $2s$, so $a+b+c = 2s$ and the three numbers $s-a$, $s-b$, $s-c$ are positive (Theorem
7.11) with sum

$$
(s-a)+(s-b)+(s-c) = 3s - (a+b+c) = s .
$$

By Heron's formula (Theorem 7.40), $K^2 = s\,(s-a)(s-b)(s-c)$. Applying the given inequality to the three
positive numbers $s-a$, $s-b$, $s-c$,

$$
(s-a)(s-b)(s-c) \le \left(\frac{s}{3}\right)^3,
$$

with equality exactly when $s-a = s-b = s-c$, that is $a = b = c$. Hence

$$
K^2 \le s\cdot\frac{s^3}{27} = \frac{s^4}{27}, \qquad K \le \frac{s^2}{3\sqrt3},
$$

and equality holds precisely for the equilateral triangle, whose area is
$\tfrac{\sqrt3}{4}\left(\tfrac{2s}{3}\right)^2 = \tfrac{s^2}{3\sqrt3}$. $\blacksquare$

**34.** *Strategy: cut the equilateral triangle into three triangles with apex $P$ and compute the area twice.*

Let $d_1$, $d_2$, $d_3$ be the perpendicular distances from $P$ to the three sides, and let $h$ be the altitude
of the equilateral triangle. Since $P$ is inside, the segments $PA$, $PB$, $PC$ cut the triangle into $PBC$,
$PCA$, $PAB$ with bases $a$ and heights $d_1$, $d_2$, $d_3$. By additivity of area (A2) and Theorem 7.21,

$$
K = \tfrac12 a d_1 + \tfrac12 a d_2 + \tfrac12 a d_3 = \tfrac12 a\,(d_1+d_2+d_3).
$$

But also $K = \tfrac12 a h$ (Theorem 7.21 again), so $\tfrac12 a(d_1+d_2+d_3) = \tfrac12 ah$ and therefore
$d_1+d_2+d_3 = h$. Since $h = \tfrac{\sqrt3}{2}a$ depends only on the triangle, the sum is independent of
$P$. $\blacksquare$

**35.** *Strategy: drop the altitude from $A$; it bisects $BC$.*

Since $AB = AC$, the altitude $AH$ from $A$ meets $BC$ at its midpoint (Theorem 7.6 applied twice, as in
Exercise 20), so $BH = CH$.

Pythagoras in the right triangles $ABH$ and $APH$ gives

$$
AB^2 = AH^2 + BH^2, \qquad AP^2 = AH^2 + PH^2,
$$

hence $AB^2 - AP^2 = BH^2 - PH^2 = (BH - PH)(BH + PH)$.

If $P$ lies between $B$ and $H$, then $BH - PH = BP$ and $BH + PH = CH + PH = PC$; if $P$ lies between $H$ and
$C$, the same two products appear with the roles of $P$ exchanged. In both cases

$$
AB^2 - AP^2 = BP \cdot PC . \qquad \blacksquare
$$

*Check:* with $AB = AC = 13$, $BC = 10$ and $P$ the midpoint of $BC$, the altitude is $12$ and
$169 - 144 = 25 = 5\cdot 5$. ✓

**36.** *Strategy: express each median through the sides with Exercise 28, then compare.*

*(Only if.)* Assume $m_a = m_b = m_c$. Applying Exercise 28 to the median from $A$, with $BM = \tfrac{a}{2}$,

$$
b^2 + c^2 = 2m_a^2 + 2\left(\frac{a}{2}\right)^2 = 2m_a^2 + \frac{a^2}{2},
\qquad\text{so}\qquad m_a^2 = \frac{b^2+c^2}{2} - \frac{a^2}{4}.
$$

Cyclically, $m_b^2 = \tfrac{c^2+a^2}{2} - \tfrac{b^2}{4}$ and $m_c^2 = \tfrac{a^2+b^2}{2} - \tfrac{c^2}{4}$.
From $m_a^2 = m_b^2$,

$$
\frac{b^2+c^2}{2} - \frac{a^2}{4} = \frac{c^2+a^2}{2} - \frac{b^2}{4}
\;\Longrightarrow\;
\frac{3b^2}{4} = \frac{3a^2}{4}
\;\Longrightarrow\;
a = b .
$$

Similarly $m_b^2 = m_c^2$ gives $b = c$. Hence $a = b = c$ and the triangle is equilateral.

*(If.)* If $a = b = c$, then the formula above gives the same value for $m_a^2$, $m_b^2$, $m_c^2$, so the three
medians are equal. (Directly: each median is also an altitude (Theorem 7.47 and the symmetry of the figure),
and the three altitudes of an equilateral triangle are equal by congruence.) $\blacksquare$
