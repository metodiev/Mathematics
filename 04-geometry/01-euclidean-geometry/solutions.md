# Solutions: Euclidean Geometry

> [Tutorial](README.md) · [Exercises](exercises.md) · 40 solutions · every step justified

Theorem numbers refer to the tutorial `README.md`. A step justified by "given", "definition", "axiom (A…)" or "Theorem 7.…" is a step that a sceptic can check; a step justified by anything else is not a proof.

## Beginner (1–14)

**1.** (a) $37°$ is acute. Complement $90° - 37° = 53°$; supplement $180° - 37° = 143°$.
(b) $90°$ is right. Its "complement" would be $0°$, which is not an angle in the sense of (A8) (measures are positive), so no complement exists; supplement $180° - 90° = 90°$.
(c) $124°$ is obtuse. The complement would be $90° - 124° = -34°$, impossible, so none exists; supplement $180° - 124° = 56°$.
(d) $15.5°$ is acute; complement $74.5°$; supplement $164.5°$.

All four supplements lie in $(0°, 180°)$, as they must: for an angle of measure $m$, the supplement is $180° - m$, which is positive exactly when $m < 180°$, and every angle satisfies that by (A8).

**2.** (a) Since $\overrightarrow{OB}$ is interior to $\angle AOC$, axiom (A9) gives
$m\angle AOC = m\angle AOB + m\angle BOC = 42° + 31° = 73°$.
(b) The bisector $\overrightarrow{OD}$ satisfies $m\angle AOD = \tfrac12 \cdot 73° = 36.5°$. Both $\overrightarrow{OB}$ and $\overrightarrow{OD}$ lie on the same side of $\overrightarrow{OA}$ (inside the angle), so the angle between them is $42° - 36.5° = 5.5°$. *Check:* $36.5 + 5.5 = 42$ ✓.

**3.** A linear pair is supplementary (Theorem 7.4), so
$$(6x-4) + (3x+13) = 180 \;\Longrightarrow\; 9x + 9 = 180 \;\Longrightarrow\; 9x = 171 \;\Longrightarrow\; x = 19.$$
Then $m\angle 1 = 6(19) - 4 = 110°$ and $m\angle 2 = 3(19) + 13 = 70°$. *Check:* $110 + 70 = 180$ ✓, and both lie in $(0°, 180°)$ ✓.

**4.** Write the four angles as $\angle 1 = 68°$, $\angle 2$, $\angle 3$, $\angle 4$ in cyclic order. By the vertical angle theorem (Theorem 7.5), $\angle 3 = \angle 1 = 68°$. By Theorem 7.4 each of $\angle 2$, $\angle 4$ is supplementary to $\angle 1$, so each is $180° - 68° = 112°$. *Check:* $68 + 112 + 68 + 112 = 360°$, a full turn ✓.

**5.** (a) Since $B$ lies between $A$ and $C$, the rays $\overrightarrow{BA}$ and $\overrightarrow{BC}$ are opposite rays (Definition 5.4): they lie in one line and meet only at $B$.
(b) No. Opposite rays have only their endpoint in common, so $\overrightarrow{BA} \ne \overrightarrow{BC}$ even though the letters share the point $B$.
(c) Four. The line $\overleftrightarrow{AB}$ contains $A$, $B$ and $C$; together with $\overleftrightarrow{AD}$, $\overleftrightarrow{BD}$ and $\overleftrightarrow{CD}$ these are four distinct lines, because $D$ is not on $\overleftrightarrow{AB}$ (so $\overleftrightarrow{AD}$, $\overleftrightarrow{BD}$, $\overleftrightarrow{CD}$ are each different from $\overleftrightarrow{AB}$) and any two of them share a different pair of points — e.g. $\overleftrightarrow{AD}$ and $\overleftrightarrow{BD}$ would coincide only if $D$ were on $\overleftrightarrow{AB}$.
(d) No. Because the sides $\overrightarrow{BA}$ and $\overrightarrow{BC}$ are opposite rays, $\angle ABC$ is a **straight** angle: it measures $180°$ by (A8), and (A8) assigns measures in $(0°, 180°)$ only to the other angles. There is no "interior" in the sense of Definition 5.8, which presupposes two non-opposite sides; the region on one side of the line would be a half-plane, not an angle interior.

**6.** The third angle is $180° - 48° - 67° = 65°$ by the triangle angle-sum theorem (Theorem 7.10). That theorem **does** use the parallel postulate: its proof goes through Theorem 7.9 (parallel lines give equal alternate interior angles), which is where Postulate 5 enters. Without Postulate 5 one can prove only that the sum is at most $180°$, so the value $65°$ is a genuinely Euclidean fact.

**7.** By Corollary 7.10.2 the exterior angle equals the sum of the two remote interior angles: $125° = 62° + x$, so $x = 63°$. The interior angle at $A$ is supplementary to the exterior angle at $A$ (a linear pair, Theorem 7.4), hence $180° - 125° = 55°$. *Check the triangle:* $62 + 63 + 55 = 180$ ✓.

**8.** By Theorem 7.12 (isosceles triangle theorem, from $AB = AC$), $m\angle C = m\angle B = 55°$. By Theorem 7.10, $m\angle A = 180° - 55° - 55° = 70°$. Both theorems are needed: the equality of the base angles is neutral, the angle sum is not.

**9.** With $m\angle 1 = 115°$:

| Angle | Position | Measure | Reason |
|---|---|---|---|
| $1$ | upper-left at $E$ | $115°$ | given |
| $2$ | upper-right at $E$ | $65°$ | linear pair with $1$, Theorem 7.4 |
| $3$ | lower-right at $E$ | $115°$ | vertical to $1$, Theorem 7.5 |
| $4$ | lower-left at $E$ | $65°$ | vertical to $2$, Theorem 7.5 |
| $5$ | upper-left at $F$ | $115°$ | corresponding to $1$, Corollary 7.9.1 |
| $6$ | upper-right at $F$ | $65°$ | corresponding to $2$, Corollary 7.9.1 |
| $7$ | lower-right at $F$ | $115°$ | vertical to $5$, Theorem 7.5 |
| $8$ | lower-left at $F$ | $65°$ | vertical to $6$, Theorem 7.5 |

The alternate interior partner of angle $3$ is angle $5$: both are interior, and $3$ lies on the right of $t$ while $5$ lies on the left. The angle corresponding to $2$ is $6$ (same position, upper-right). *Check:* four angles of $115°$ and four of $65°$, as §9.3 of the tutorial predicts.

**10.** (a) **SAS.** The given angles are $\angle B$ (between $BA$ and $BC$) and $\angle E$ (between $ED$ and $EF$), which are the included angles of the given side pairs, and the correspondence is $A \leftrightarrow D$, $B \leftrightarrow E$, $C \leftrightarrow F$.
(b) **ASA**: the side $AB$ is included between the angles at $A$ and $B$; likewise $DE$ between those at $D$ and $E$.
(c) **SSS**.
(d) **AAS**: the side $BC$ is opposite $\angle A$ and $EF$ is opposite $\angle D$, so the data are two angles and a non-included corresponding side.
(e) **Not enough information.** This is the SSA pattern: two sides and a non-included angle. Two non-congruent triangles can share these data — Exercise 35 constructs an explicit pair with $\angle A = 30°$, $AB = 10$, $BC = 6$.

**11.** The converse is: "if two angles are equal, then they are vertical angles". It is **false**. The simplest reason is that vertical angles share a vertex (Definition 5.10), so two equal angles with *different* vertices — say $m\angle AOB = 40°$ and $m\angle CPD = 40°$ with $O \ne P$ — are equal and not vertical.

A sharper counterexample, in which the two angles even share a vertex, is this: take a ray $\overrightarrow{OB}$; on one side of the line $\overleftrightarrow{OB}$ lay off the ray $\overrightarrow{OA}$ with $m\angle AOB = 40°$, and on the *other* side lay off the ray $\overrightarrow{OC}$ with $m\angle BOC = 40°$ (axiom (A8)). Then $\angle AOB$ and $\angle BOC$ are equal and adjacent, sharing the side $\overrightarrow{OB}$; their other sides $\overrightarrow{OA}$ and $\overrightarrow{OC}$ are not opposite rays, because $40° + 40° = 80° \ne 180°$. So the two angles are equal but not vertical. The error is the one of §11.4: a theorem and its converse are separate statements, and here the converse is simply false.

**12.** (a) Postulate 1. (b) Postulate 2. (c) Postulate 3. (d) Postulate 4. (e) Postulate 5.

**13.** Let the angles be $2k$ and $3k$. They are complementary, so $5k = 90°$, giving $k = 18°$; the angles are $36°$ and $54°$. *Check:* $36 + 54 = 90$ ✓ and $36 : 54 = 2 : 3$ ✓.

**14.** Let one angle be $x$; the other is $2x + 30°$. Supplementary gives $x + 2x + 30° = 180°$, so $3x = 150°$ and $x = 50°$. The angles are $50°$ and $130°$. *Check:* $50 + 130 = 180$ ✓ and $130 = 2(50) + 30$ ✓.

## Intermediate (15–24)

**15.** Since the lines are parallel, same-side interior angles are supplementary (Corollary 7.9.2):
$$(3x+20) + (2x+10) = 180 \;\Longrightarrow\; 5x + 30 = 180 \;\Longrightarrow\; 5x = 150 \;\Longrightarrow\; x = 30.$$
The angles are $3(30) + 20 = 110°$ and $2(30) + 10 = 70°$. *Check:* $110 + 70 = 180$ ✓. A second check: the alternate interior partner of the $110°$ angle is the other interior angle at that vertex, which is $180° - 110° = 70°$ and must equal the $70°$ found.

**16.** Let the angles be $2k$, $3k$, $4k$. By Theorem 7.10, $9k = 180°$, so $k = 20°$ and the angles are $40°$, $60°$, $80°$. All three are less than $90°$, so the triangle is **acute**.

**17.** By Corollary 7.10.2, $4x - 5 = (2x+10) + (x+20)$, so $4x - 5 = 3x + 30$ and $x = 35$. The exterior angle is $4(35) - 5 = 135°$; the remote interiors are $2(35)+10 = 80°$ and $35+20 = 55°$, and $80 + 55 = 135$ ✓. The interior angle at $A$ is $180° - 135° = 45°$ (linear pair). *Check:* $80 + 55 + 45 = 180$ ✓.

**18.** Suppose $\angle 2$ and $\angle 3$ are both supplementary to $\angle 1$. By definition of supplementary,
$$m\angle 2 = 180° - m\angle 1 \quad\text{and}\quad m\angle 3 = 180° - m\angle 1.$$
The two right-hand sides are the same number, so $m\angle 2 = m\angle 3$ by **common notion 1** (things equal to the same thing are equal). The subtraction itself is the arithmetic of real numbers, and it is legitimate because the measures exist by (A8) and the angles are supplementary by hypothesis. (Equivalently, one may say: subtracting equal quantities $m\angle 1$ from equal quantities $180°$ gives equal remainders, which is **common notion 3**.) No geometric axiom beyond (A8) is used, and no parallel postulate.

**19.** Let $ABCD$ be a convex quadrilateral. Draw the diagonal $\overline{AC}$. Because the quadrilateral is convex, $\overline{AC}$ lies inside it, so the ray $\overrightarrow{AC}$ is interior to $\angle DAB$ and the ray $\overrightarrow{CA}$ is interior to $\angle BCD$. Hence, by (A9),
$$m\angle DAB = m\angle DAC + m\angle CAB, \qquad m\angle BCD = m\angle BCA + m\angle ACD.$$
Now apply Theorem 7.10 to the two triangles:
$$m\angle CAB + m\angle ABC + m\angle BCA = 180°, \qquad m\angle DAC + m\angle ACD + m\angle CDA = 180°.$$
Adding and grouping by vertex,
$$m\angle DAB + m\angle ABC + m\angle BCD + m\angle CDA = 360°. \qquad \square$$
Convexity is used exactly twice: to know that the diagonal lies inside the quadrilateral, and hence that the angles at $A$ and at $C$ split additively. Without it, the diagonal may leave the figure and one of the two angle sums must be replaced by a difference. Note also that the whole argument inherits the parallel postulate from Theorem 7.10.

**20.** Let the same-side interior angles be $\alpha$ at $E$ and $\beta$ at $F$, on the same side of the transversal $t$, with $\alpha + \beta = 180°$. Let $\beta'$ be the interior angle at $F$ on the *other* side of $t$. Since $\beta$ and $\beta'$ form a linear pair on the line $m$, Theorem 7.4 gives $\beta' = 180° - \beta$. Substituting $\beta = 180° - \alpha$ from the hypothesis gives $\beta' = \alpha$. So the alternate interior angles $\alpha$ (at $E$) and $\beta'$ (at $F$) are equal, and Theorem 7.7 gives $\ell \parallel m$. $\square$

The converse — parallel lines give supplementary same-side interior angles — is Corollary 7.9.2, and it **does** need the parallel postulate, because it goes through Theorem 7.9. The statement proved here is the neutral direction, and this asymmetry is the content of the table in §7.10.

**21.** Consider $\triangle PMA$ and $\triangle PMB$.

| # | Statement | Reason |
|---|---|---|
| 1 | $MA = MB$ | $M$ is the midpoint of $\overline{AB}$ (Definition 5.6) |
| 2 | $\angle PMA = \angle PMB = 90°$ | $PM \perp \overline{AB}$, so both angles at $M$ are right (Theorem 7.4 gives each is $90°$) |
| 3 | $PM = PM$ | the same segment |
| 4 | $\triangle PMA \cong \triangle PMB$ | SAS (axiom (A10)), with $P \leftrightarrow P$, $M \leftrightarrow M$, $A \leftrightarrow B$ |
| 5 | $PA = PB$ | corresponding sides of congruent triangles |

$\square$ This is the "easy" direction of the perpendicular bisector theorem; the converse is Exercise 27.

**22.** Vertical angles are equal (Theorem 7.5), so $7x - 30 = 4x + 45$, giving $3x = 75$ and $x = 25$. Then $m\angle 1 = m\angle 3 = 7(25) - 30 = 145°$, checking against $4(25)+45 = 145°$ ✓. Each of the other two angles is supplementary to $145°$ (Theorem 7.4), so each is $35°$. *Check:* $2(145) + 2(35) = 360$ ✓.

**23.** *Construction.* Let the angle be $\angle AOB$ with vertex $O$.
1. Draw the circle with centre $O$ and some radius $r$; it meets the ray $\overrightarrow{OA}$ at a point $P$ and the ray $\overrightarrow{OB}$ at a point $Q$ (axiom (A6) gives a unique such point on each ray).
2. Construct an equilateral triangle on $\overline{PQ}$ (Construction I.1) and let $R$ be its third vertex on the side of $\overleftrightarrow{PQ}$ opposite to $O$.
3. Draw the ray $\overrightarrow{OR}$. It is the bisector.

*Proof.* $OP = OQ = r$ because $P$, $Q$ lie on the circle centred at $O$; and $RP = RQ$ because both are sides of the equilateral triangle on $\overline{PQ}$. Therefore, in $\triangle OPR$ and $\triangle OQR$,
$$OP = OQ, \qquad RP = RQ, \qquad OR = OR,$$
so $\triangle OPR \cong \triangle OQR$ by SSS (Theorem 7.14). Under this congruence $\angle POR$ corresponds to $\angle QOR$, so the two angles are equal, and $\overrightarrow{OR}$ bisects $\angle AOB$. The choice of $R$ on the far side of $\overleftrightarrow{PQ}$ from $O$ is what makes $\overrightarrow{OR}$ the *internal* bisector: the line $OR$ is the perpendicular bisector of $\overline{PQ}$ (both $O$ and $R$ are equidistant from $P$ and $Q$), and of its two rays from $O$ one bisects $\angle POQ$ and the other bisects the vertical angle. $\square$

*Remark.* Step 2 uses the existence of the third vertex of an equilateral triangle, i.e. of the intersection of two circles — the point discussed in §7.15 and Exercise 38. The construction is therefore correct *given* the circle-intersection axiom, which the Euclidean plane satisfies.

**24.** By Theorem 7.10 applied to $\triangle ABC$,
$$m\angle ABC + m\angle ACB = 180° - 50° = 130°.$$
Because $BI$ and $CI$ are bisectors (Definition 5.10) and lie inside their angles,
$$m\angle IBC + m\angle ICB = \tfrac12(m\angle ABC + m\angle ACB) = 65°.$$
Applying Theorem 7.10 to $\triangle IBC$,
$$m\angle BIC = 180° - 65° = 115°.$$
*Check:* $115 = 90 + \tfrac12 \cdot 50$, the standard formula for the incenter angle, which is a useful memory aid but not a substitute for the derivation.

## Advanced (25–33)

**25.** (a) *Using the angle sum.* Suppose $\angle A$ and $\angle B$ of $\triangle ABC$ are both right angles. By Theorem 7.10,
$$m\angle C = 180° - 90° - 90° = 0°,$$
which is impossible because (A8) assigns every angle a measure in $(0°, 180°)$. This argument uses Postulate 5 (through Theorem 7.10) and (A8).

(b) *Using the exterior angle inequality only.* Suppose $m\angle A = m\angle B = 90°$. Extend $\overline{BA}$ beyond $A$ to a point $F$, so that $F{-}A{-}B$. Then $\angle CAF$ and $\angle CAB$ form a linear pair, so
$$m\angle CAF = 180° - 90° = 90°$$
(Theorem 7.4). But $\angle CAF$ is an exterior angle of $\triangle ABC$ at $A$, so by Theorem 7.6 it is strictly greater than the remote interior angle $\angle ABC$:
$$90° = m\angle CAF > m\angle ABC = 90°,$$
a contradiction. $\square$

This argument uses only Theorem 7.6, which is neutral: it needs SAS and the order axioms, not Postulate 5. So the statement "no triangle has two right angles" is a theorem of neutral geometry, even though the angle-sum route to it is not. Part (b) also shows why the exterior angle inequality is stated with a strict inequality — with "$\ge$" the argument would fail.

**26.** Let $\ell \parallel m$, with transversal $t$ meeting them at $E$ and $F$. Let $\angle AEF$ at $E$ and $\angle EFD$ at $F$ be a pair of alternate interior angles; by Theorem 7.9 they are equal; write their common measure as $\alpha$. Let $\overrightarrow{EX}$ bisect $\angle AEF$ and $\overrightarrow{FY}$ bisect $\angle EFD$, so that
$$m\angle XEF = \tfrac{\alpha}{2} = m\angle YFE.$$
Now $X$ and $Y$ lie on opposite sides of $t$: indeed $X$ is interior to $\angle AEF$, whose interior lies on one side of $t$, while $Y$ is interior to $\angle EFD$, whose interior lies on the other side. Therefore $\angle XEF$ and $\angle YFE$ are a pair of **alternate interior angles** for the lines $\overleftrightarrow{EX}$ and $\overleftrightarrow{FY}$ with transversal $t$, and they are equal. By Theorem 7.7, $\overleftrightarrow{EX} \parallel \overleftrightarrow{FY}$. $\square$

Note which theorem does the work: the *neutral* criterion (equal alternate interior $\Rightarrow$ parallel). The Euclidean input is only the equality of the bisected angles.

**27.** Write $M$ for the midpoint of $\overline{AB}$ and $p$ for the perpendicular to $\overleftrightarrow{AB}$ at $M$; by Theorem 7.2 there is exactly one such line, and by Definition 5.11 it is the perpendicular bisector.

*($\Leftarrow$)* Suppose $P \in p$. Consider $\triangle PMA$ and $\triangle PMB$: $PM = PM$ (common), $MA = MB$ ($M$ is the midpoint, Definition 5.6), and $\angle PMA = \angle PMB = 90°$ because $PM$ lies in $p \perp \overleftrightarrow{AB}$. By SAS, $\triangle PMA \cong \triangle PMB$, hence $PA = PB$. (If $P = M$ the two triangles are degenerate; then directly $PA = MA = MB = PB$ by Definition 5.6.)

*($\Rightarrow$)* Suppose $PA = PB$. In $\triangle PMA$ and $\triangle PMB$ we have $PA = PB$ (hypothesis), $MA = MB$ (midpoint) and $PM = PM$ (common), so $\triangle PMA \cong \triangle PMB$ by SSS (Theorem 7.14). Under this congruence $\angle PMA$ corresponds to $\angle PMB$, so $m\angle PMA = m\angle PMB$; but $A{-}M{-}B$, so these two angles form a linear pair and sum to $180°$ (Theorem 7.4). Hence each is $90°$, that is, $PM \perp \overleftrightarrow{AB}$, so $P$ lies on the perpendicular to $\overleftrightarrow{AB}$ at the midpoint $M$, which is $p$. $\square$

Both directions are neutral. This theorem is used in Exercise 36 and in the analysis of the classical fallacy of §11.2.

**28.** Let $\ell \parallel m$, transversal $t$ meeting them at $E$ and $F$, and let $\alpha$ at $E$ and $\beta$ at $F$ be a pair of same-side interior angles; by Corollary 7.9.2,
$$\alpha + \beta = 180°.$$
Let $\overrightarrow{EX}$ and $\overrightarrow{FY}$ be the bisectors, meeting at $Z$. First, they do meet: on the side of $t$ containing both interior angles, the angles $\tfrac{\alpha}{2}$ at $E$ and $\tfrac{\beta}{2}$ at $F$ have sum $90° < 180°$, so by Postulate 5 the two bisector lines meet on that side. Now apply Theorem 7.10 to $\triangle EFZ$:
$$m\angle EZF = 180° - \left(\tfrac{\alpha}{2} + \tfrac{\beta}{2}\right) = 180° - 90° = 90°.$$
Hence $\overrightarrow{EX} \perp \overrightarrow{FY}$. $\square$

The parallel postulate is used twice: once through Corollary 7.9.2 (the supplementary relation is false in hyperbolic geometry) and once, explicitly, to ensure the bisectors meet — the same role Postulate 5 plays whenever an intersection must be produced.

**29.** *Step 1: opposite sides are equal.* Consider $\triangle ABC$ and $\triangle CDA$. Since $AB \parallel CD$, the alternate interior angles $\angle BAC$ and $\angle DCA$ are equal (Theorem 7.9); since $BC \parallel AD$, the alternate interior angles $\angle BCA$ and $\angle DAC$ are equal; and $AC = CA$. By ASA (Theorem 7.13),
$$\triangle ABC \cong \triangle CDA, \qquad\text{hence}\qquad AB = CD \ \text{and}\ BC = AD.$$

*Step 2: the diagonals bisect each other.* Because $ABCD$ is convex, the diagonals $AC$ and $BD$ meet at a point $O$ inside the quadrilateral. Consider $\triangle OAB$ and $\triangle OCD$. Since $AB \parallel CD$:
* $\angle OAB = \angle OCD$ (alternate interior angles with transversal $AC$);
* $\angle OBA = \angle ODC$ (alternate interior angles with transversal $BD$);
* $AB = CD$ (Step 1).

By ASA, $\triangle OAB \cong \triangle OCD$, so $OA = OC$ and $OB = OD$. That is, $O$ is the midpoint of both diagonals, which therefore bisect each other. $\square$

**30.** Suppose $AC > AB$. By axiom (A6), on the ray $\overrightarrow{AC}$ there is a point $D$ with $AD = AB$; since $AD = AB < AC$, the point $D$ lies strictly between $A$ and $C$, so $A{-}D{-}C$.

1. $AD = AB$, so $\triangle ABD$ is isosceles with apex $A$; by Theorem 7.12, $m\angle ABD = m\angle ADB$.
2. Because $D$ lies on the segment $AC$, the ray $\overrightarrow{BD}$ lies inside $\angle ABC$ (it separates $BA$ from $BC$; equivalently, $D$ is interior to the angle). Hence, by (A9), $m\angle ABC = m\angle ABD + m\angle DBC > m\angle ABD$.
3. In $\triangle BCD$, the point $A$ lies on the extension of $DC$ beyond $D$ (as $A{-}D{-}C$), so $\angle ADB$ is an exterior angle at $D$. By Theorem 7.6, $m\angle ADB > m\angle BCD = m\angle BCA$.

Chaining: $m\angle ABC > m\angle ABD = m\angle ADB > m\angle BCA$. $\square$

The hypothesis $AC > AB$ was used only to place $D$ strictly inside $\overline{AC}$; that is what makes step 2 strict. The argument is neutral.

**31.** Let $ABCD$ be convex with $AB \parallel CD$ and $AB = CD$. Consider the diagonal $AC$ and the triangles $\triangle ABC$ and $\triangle CDA$.

* $\angle BAC = \angle DCA$: alternate interior angles, since $AB \parallel CD$ and $AC$ is a transversal (Theorem 7.9).
* $AB = CD$: given.
* $AC = CA$: common side.

By SAS (axiom (A10)), $\triangle ABC \cong \triangle CDA$, with correspondence $A \leftrightarrow C$, $B \leftrightarrow D$, $C \leftrightarrow A$. Under this congruence $\angle BCA$ corresponds to $\angle DAC$, so these are equal. But $\angle BCA$ and $\angle DAC$ are alternate interior angles for the lines $BC$ and $AD$ with transversal $AC$ (the points $B$ and $D$ lie on opposite sides of $AC$ because the quadrilateral is convex). By Theorem 7.7, $BC \parallel AD$. $\square$

**32.** Suppose $m\angle B > m\angle C$. We compare the side lengths.

* $AC \ne AB$: if $AC = AB$ then $m\angle B = m\angle C$ by Theorem 7.12, contrary to hypothesis.
* $AB > AC$ is impossible: by Exercise 30 (applied with the roles of the sides exchanged), $AB > AC$ would give $m\angle C > m\angle B$, contrary to hypothesis.
* Segment lengths are totally ordered (they are real numbers by (A6)), and the case $AC = AB$ is excluded, so the remaining possibility is $AC > AB$. $\square$

Note the logical structure: this is a proof by elimination, and it uses the *converse* direction (Exercise 30) as a tool. Euclid's I.19 is exactly this argument.

**33.** Let $ABCD$ be a quadrilateral with four right angles.

*Step 1: opposite sides are parallel.* Both $AB$ and $CD$ are perpendicular to $BC$, so $AB \parallel CD$ by Corollary 7.7.3; likewise $BC \parallel AD$.

*Step 2: $BC = AD$.* Consider $\triangle ABC$ and $\triangle CDA$. Since $AB \parallel CD$, the alternate interior angles $\angle BAC$ and $\angle DCA$ are equal; since $BC \parallel AD$, the alternate interior angles $\angle BCA$ and $\angle DAC$ are equal; and $AC$ is common. By ASA, $\triangle ABC \cong \triangle CDA$, so $BC = AD$.

*Step 3: the diagonals are equal.* Consider $\triangle ABC$ and $\triangle BAD$. We have $AB = BA$ (common), $\angle ABC = \angle BAD = 90°$ (right angles of the rectangle), and $BC = AD$ (Step 2). By SAS, $\triangle ABC \cong \triangle BAD$, with correspondence $A \leftrightarrow B$, $B \leftrightarrow A$, $C \leftrightarrow D$. Under this congruence the side $\overline{AC}$ corresponds to $\overline{BD}$, hence $AC = BD$. $\square$

## Challenge (34–40)

**34.** *Construction.* Let the given lengths be $a$, $b$, $c$.
1. Draw a ray from a point $A$ and lay off $B$ on it with $AB = c$ (axiom (A6)).
2. Draw the circle with centre $A$ and radius $b$.
3. Draw the circle with centre $B$ and radius $a$.
4. Let $C$ be a common point of the two circles. Then $\triangle ABC$ has $AB = c$, $AC = b$, $BC = a$, as required.

*Correctness.* By construction $AC = b$ (C is on the circle centred at $A$) and $BC = a$ (C is on the circle centred at $B$), and $AB = c$; so the triangle has the three required side lengths. Two common points $C$, $C'$ give triangles that are mirror images in $\overleftrightarrow{AB}$, hence congruent (the reflection fixes $A$ and $B$ and swaps $C$ with $C'$), so the triangle is determined up to congruence — which is exactly the content of SSS.

*Where the inequalities enter.* The two circles meet exactly when
$$|a - b| \le c \le a + b .$$
If $c > a + b$, the centres are farther apart than the sum of the radii and the circles are disjoint; if $c < |a - b|$, the smaller circle lies entirely inside the larger. Each of the three given triangle inequalities is one of these conditions with the labels permuted: $a + b > c$ is the upper bound, $b + c > a$ and $c + a > b$ together give $|a - b| < c$. If one inequality is an equality — say $c = a + b$ — the circles touch at a single point of the line $AB$, and the "triangle" is degenerate (all three points collinear), which is why the inequalities in the statement are strict.

*Remark.* Step 4 again invokes the intersection of two circles; §7.15 and Exercise 38 explain why that is an additional continuity assumption and not a consequence of Postulates 1–3.

**35.** Put $A$ at the origin, let the ray $AC$ be the positive $x$-axis, and let $\angle BAC = 30°$ with $AB = 10$. Then
$$B = \bigl(10\cos 30°,\ 10\sin 30°\bigr) = \bigl(5\sqrt3,\ 5\bigr),$$
using the half-equilateral triangle: bisecting an equilateral triangle (Euclid I.1) gives a right triangle with angles $30°$, $60°$, $90°$, in which the side opposite $30°$ is half the hypotenuse, whence $\sin 30° = \tfrac12$ and $\cos 30° = \tfrac{\sqrt3}{2}$.

A point $C$ on the ray has coordinates $(x, 0)$ with $x > 0$. Requiring $BC = 6$:
$$(x - 5\sqrt3)^2 + 5^2 = 6^2 \;\Longrightarrow\; (x-5\sqrt3)^2 = 11 \;\Longrightarrow\; x = 5\sqrt3 \pm \sqrt{11}.$$
Both values are positive, because $5\sqrt3 = \sqrt{75} > \sqrt{11}$; so both candidates lie on the ray. Hence there are exactly two triangles:
$$AC = 5\sqrt3 + \sqrt{11} \approx 11.98 \qquad\text{and}\qquad AC = 5\sqrt3 - \sqrt{11} \approx 5.35,$$
both with $AB = 10$, $BC = 6$ and $m\angle A = 30°$. They are not congruent, since their sides $AC$ differ. So the data "two sides and a non-included angle" do not determine a triangle, and SSA is not a criterion.

*Geometric reading.* The perpendicular distance from $B$ to the line $AC$ is $5$, which is less than $BC = 6$, so the circle of radius $6$ about $B$ meets the line $AC$ in two points symmetric about the foot of the perpendicular; and because that foot is at distance $5\sqrt3 > \sqrt{11}$ from $A$, both points lie on the ray. The case $BC < 5$ would give no triangle, and $BC = 5$ exactly one (a right triangle); the ambiguity is precisely the interval $5 < BC < 10$.

**36.** Let $\triangle ABC$ be given and let $p_{AB}$, $p_{AC}$, $p_{BC}$ be the perpendicular bisectors of the three sides.

*Step 1: $p_{AB}$ and $p_{AC}$ meet.* They cannot be parallel: if $p_{AB} \parallel p_{AC}$, then $AB \perp p_{AB}$ forces $AB \perp p_{AC}$ (a line perpendicular to one of two parallel lines is perpendicular to the other — corresponding angles, Corollary 7.9.1), and $AC \perp p_{AC}$ then gives $AB \parallel AC$ by Corollary 7.7.3, impossible because $A$, $B$, $C$ are not collinear. So let $O = p_{AB} \cap p_{AC}$.

*Step 2: $O$ is equidistant from all three vertices.* Since $O \in p_{AB}$, Exercise 27 gives $OA = OB$. Since $O \in p_{AC}$, Exercise 27 gives $OA = OC$. Hence $OB = OA = OC$ by common notion 1: the three distances are equal.

*Step 3: $O$ lies on the third perpendicular bisector.* Since $OB = OC$, the converse direction of Exercise 27 says that $O$ lies on the perpendicular bisector of $\overline{BC}$, that is, $O \in p_{BC}$.

So all three perpendicular bisectors pass through $O$: they are concurrent, and $O$ is the centre of the circle through $A$, $B$, $C$. $\square$

**37.** Let $S^2 = \{(x,y,z) \in \mathbb{R}^3 : x^2+y^2+z^2 = 1\}$. A *great circle* is the intersection of $S^2$ with a plane through the origin, and a *side* of the spherical triangle is an arc of a great circle. Take
$$N = (0,0,1), \qquad P = (1,0,0), \qquad Q = (0,1,0).$$

*The sides.* $NP$ lies in the plane $y = 0$ (the $xz$-plane); $NQ$ lies in the plane $x = 0$ (the $yz$-plane); $PQ$ lies in the plane $z = 0$ (the equator). Each is an arc of a great circle.

*The angles.* The angle between two arcs at a common endpoint is the angle between their tangent lines there.
* At $N$: the tangent to $NP$ is along the $x$-direction, the tangent to $NQ$ along the $y$-direction; these are perpendicular, so the angle is $90°$.
* At $P$: the tangent to $NP$ is along the $z$-direction and the tangent to $PQ$ along the $y$-direction; again perpendicular, so $90°$.
* At $Q$: the tangent to $NQ$ is along the $z$-direction and the tangent to $PQ$ along the $x$-direction; again $90°$.

So the angle sum is $90° + 90° + 90° = 270°$.

*Which Euclidean assumptions fail.* Several, and it is worth naming them precisely.
* (A3) fails: two distinct great circles always meet, in *two* antipodal points, so "two distinct lines have at most one point in common" is false.
* (A4) fails globally: a great circle is a closed curve, so there is no consistent notion of "between" for three points on it.
* Postulate 2 fails: a side cannot be extended indefinitely along its great circle without returning to its starting point.
* Postulate 5 fails in the strongest possible way: there are **no** parallel great circles, since every two meet. Equivalently, Playfair's axiom fails.

This is why the spherical angle sum $270°$ is no contradiction of Theorem 7.10: that theorem was proved for a plane satisfying the axioms of §5.4, and the sphere satisfies neither the order axioms nor the parallel postulate. The example also shows why the angle-sum theorem cannot be proved without the fifth postulate: a proof from the other axioms would have to hold on the sphere, where the statement is false.

**38.** *The model.* Let $\Pi = \mathbb{Q}^2$, the set of pairs of rational numbers. Take as "lines" the solution sets of equations $ux + vy = w$ with $u, v, w \in \mathbb{Q}$ and $(u,v) \ne (0,0)$, and take betweenness to be the usual affine betweenness.

Then (A1) holds: two distinct rational points determine exactly one such line, with rational coefficients. (A2) and (A3) hold, since two distinct such lines meet in at most one point (solve a $2\times 2$ system). (A4) and (A5) hold, because the rational points are dense and the usual order of the line is inherited. The segment-measure axiom holds in the **weakened** form in which only rational radii must exist on a ray: for rational $r > 0$ the point at distance $r$ along a rational line has rational coordinates. (The full axiom (A6) fails in $\Pi$, since there is no point at rational distance $\sqrt{2}$ from the origin on the $x$-axis; that failure is a different gap, and it is not the one used here.)

*The failure.* Let $A = (0,0)$ and $B = (1,0)$, so $AB = 1$. The circle with centre $A$ through $B$ is the set of rational points with $x^2 + y^2 = 1$; the circle with centre $B$ through $A$ is the set of rational points with $(x-1)^2 + y^2 = 1$. A common point would satisfy, after subtracting the two equations,
$$x^2 - (x-1)^2 = 0 \;\Longrightarrow\; 2x - 1 = 0 \;\Longrightarrow\; x = \tfrac12,$$
and then $y^2 = 1 - \tfrac14 = \tfrac34$, so $y = \pm \tfrac{\sqrt3}{2}$. But $\sqrt3$ is irrational, so no such point has rational coordinates. Thus in $\Pi$ the two circles have **no** common point, and there is no equilateral triangle on $\overline{AB}$ — even though the incidence and order axioms hold.

So the existence of the intersection is **not** a consequence of incidence and order (plus the rational form of segment measure). What repairs it is a continuity axiom: Hilbert's **circle axiom** states that if a circle passes through a point inside and a point outside another circle, the two circles meet; **Dedekind's axiom** (completeness of the line) forces the plane to be isomorphic to $\mathbb{R}^2$, where the intersection points $(1/2, \pm\sqrt3/2)$ exist. Euclid's Construction I.1 is therefore correct in the Euclidean plane, but its correctness rests on a continuity assumption that Postulates 1–3 do not supply.

**39.** The error is in the sentence *"there is only one line through $E$, namely $\ell$"*. As written it is plainly false: infinitely many lines pass through $E$. What the argument needs is the much stronger statement

> there is **at most one** line through $E$ parallel to $m$,

and that is exactly Playfair's axiom (A11), which is equivalent to the parallel postulate by Theorem 7.8. So the "proof" smuggles in the very axiom it is supposed to avoid; it establishes the alternate interior angle theorem only in Euclidean geometry, and it is circular if the goal was a neutral proof.

There is a second, subtler reading. Perhaps the student meant: "there is only one line through $E$ making that particular angle with $t$" — that is true, by the uniqueness part of axiom (A8). But uniqueness of the angle does not identify that line with $\ell$: it only says that the line $n$ constructed is the unique line with the property "makes angle equal to $\angle F$ with $t$". To conclude $n = \ell$ one must already know that $\ell$ has this property — that is, that the alternate interior angle at $E$ equals the angle at $F$, which is exactly the conclusion. So this reading is circular too, in the classical form of assuming what is to be proved.

The correct statement of the situation is the pair of theorems in §7.7 and §7.10: the criterion in the direction "equal alternate interior $\Rightarrow$ parallel" is neutral (Theorem 7.7), while the direction "parallel $\Rightarrow$ equal alternate interior" needs Postulate 5 (Theorem 7.9). A proof of the second direction cannot avoid the postulate, because the statement is false in hyperbolic geometry.

**40.** Suppose, for contradiction, that $Q \ne Q'$ are two points of $\ell$ with $PQ \perp \ell$ and $PQ' \perp \ell$. Consider $\triangle PQQ'$.

1. $m\angle PQQ' = 90°$: this angle is formed by $\overrightarrow{QP}$ and $\overrightarrow{QQ'}$, and $\overrightarrow{QQ'}$ lies in $\ell$ (as $Q$, $Q' \in \ell$), so it is the angle between $QP$ and $\ell$, which is a right angle by hypothesis.
2. $m\angle PQ'Q = 90°$ for the same reason, with $Q$ and $Q'$ exchanged.
3. Extend $\overline{Q'Q}$ beyond $Q$ to a point $S$, so that $Q'{-}Q{-}S$. Then $\angle PQS$ and $\angle PQQ'$ form a linear pair, so by Theorem 7.4
$$m\angle PQS = 180° - 90° = 90°.$$
4. But $\angle PQS$ is an exterior angle of $\triangle PQQ'$ at $Q$, and $\angle PQ'Q$ is a remote interior angle. By Theorem 7.6 (exterior angle inequality), the exterior angle is strictly greater:
$$90° = m\angle PQS > m\angle PQ'Q = 90°,$$
a contradiction. $\square$

So at most one such point exists. The argument uses only the neutral part of the theory (Theorems 7.4 and 7.6), which is why uniqueness of the perpendicular foot holds in hyperbolic geometry as well; *existence* is a separate matter, requiring either a continuity argument or the parallel postulate, and is not claimed here.