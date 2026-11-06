# Non-Euclidean Geometry

> [Mathematics](../../README.md) › [Geometry](../README.md) · Level: Advanced · Prerequisites: [Euclidean Geometry](../01-euclidean-geometry/README.md), [Triangles](../02-triangles/README.md), [Circles](../03-circles/README.md), [Geometric Transformations](../06-transformations/README.md), [Trigonometry](../../05-trigonometry/README.md), [Metric Spaces](../../14-real-analysis/06-metric-spaces/README.md) · Estimated time: 8 h

## 1. Introduction

For more than two thousand years, one sentence in Euclid's *Elements* was regarded as a blemish. It is the
**fifth postulate**: two straight lines must meet if a transversal makes the interior angles on one side add
to less than two right angles. Compared with the other four postulates it is long, awkward, and it asserts an
intersection that may lie arbitrarily far away. Generations of geometers tried to *prove* it from the other
four. Every attempt failed, and the reason turned out to be far more interesting than the postulate itself:
the sentence is **independent** of the other axioms. It can be replaced by its negation, and the result is not
a contradiction but a different, equally consistent geometry.

This chapter tells that story in three parts.

1. **The logical story.** What the parallel postulate says, what it is equivalent to, why two millennia of
   proofs failed, and what "independence" means. The decisive tool is a **model**: an interpretation of the
   undefined terms in which all the axioms hold. A model of the other axioms in which the parallel postulate
   *fails* proves that no proof of it can exist.
2. **The two new geometries.** On a sphere the "lines" are great circles, any two of them meet, and the angles
   of a triangle add to **more** than $\pi$. In the hyperbolic plane, through a point not on a line there are
   **infinitely many** lines that miss it, and the angles of a triangle add to **less** than $\pi$. Both
   geometries have trigonometry, area formulas, coordinates and applications.
3. **The unifying idea.** All three are the constant-curvature cases of one theory. Gauss curvature $K$ is
   positive on the sphere, zero on the plane and negative in the hyperbolic plane, and the angle sum of a
   geodesic triangle differs from $\pi$ by exactly the integral of $K$ over the triangle.

The story is also the story of how mathematics became modern. Euclid presented geometry as a deductive
science, but his axioms were never a complete formal system. Saccheri, Lambert and Legendre worked inside an
informal tradition and could always find a reason to reject the conclusions they did not like. Bolyai and
Lobachevsky accepted them. Beltrami, Klein and Poincaré supplied the missing ingredient — models built
inside Euclidean geometry — which turned a philosophical dispute into a theorem of mathematics. Hilbert's
*Grundlagen der Geometrie* (1899) then rewrote the axioms themselves, so that "independence" became a precise
statement rather than a matter of taste.

The chapter assumes Euclidean geometry and a willingness to follow a proof. It does not assume differential
geometry: the spherical case is proved in full, the hyperbolic formulas are derived from explicit models, and
the curvature statements are stated precisely with proofs or cited sources. "Non-Euclidean geometry" here
means the two classical alternatives — **spherical** (with its quotient, **elliptic**) and **hyperbolic** —
together with the logical analysis that shows they are alternatives to Euclid's fifth postulate. It does not
mean "any geometry that is not the Euclidean plane"; projective and affine geometry are different subjects,
although they are related.

## 2. Prerequisites

* **Euclid's axioms and the deductive method**, including the first 28 propositions of Book I — from
  [Euclidean Geometry](../01-euclidean-geometry/README.md).
* **Triangles:** congruence criteria, the exterior angle theorem, and the Euclidean angle sum — from
  [Triangles](../02-triangles/README.md).
* **Circles:** chords, tangents, inscribed angles, and the perpendicularity of a tangent to its radius — from
  [Circles](../03-circles/README.md).
* **Coordinates, transformations and complex numbers:** Cartesian coordinates, rotations, reflections,
  translations, distance-preserving maps, and Möbius transformations — from
  [Coordinate Geometry](../04-coordinate-geometry/README.md),
  [Geometric Transformations](../06-transformations/README.md) and
  [Complex Numbers](../../03-algebra/13-complex-numbers/README.md).
* **Trigonometry:** the identities for $\sin$, $\cos$, $\tan$, radian measure, and the Euclidean law of
  cosines — from [Trigonometry](../../05-trigonometry/README.md).
* **Metric spaces, isometries and calculus:** distance functions, completeness, integration of rational
  functions, and the derivatives of $\operatorname{artanh}$, $\sinh$ and $\cosh$ — from
  [Metric Spaces](../../14-real-analysis/06-metric-spaces/README.md) and [Calculus](../../07-calculus/README.md).

## 3. Learning Objectives

After this tutorial you will be able to:

1. State Euclid's fifth postulate and Playfair's axiom, and prove their equivalence in neutral geometry.
2. Explain what neutral geometry is, and why the parallel postulate is independent of it.
3. Describe the Saccheri and Lambert quadrilaterals and the three hypotheses on their summit angles.
4. Distinguish a model from a proof, and explain how the Klein and Poincaré models give relative consistency.
5. Compute with great circles: distances, angles, lune areas, and spherical triangles.
6. Prove Girard's theorem and compute the area of a spherical triangle from its angles.
7. State and use the spherical law of cosines and the spherical sine law.
8. Work in the Poincaré disk and upper half-plane: identify geodesics, compute distances, and compute areas.
9. Prove that hyperbolic triangles have angle sum less than $\pi$, and state the defect–area relation.
10. Explain the role of Gaussian curvature and the Theorema Egregium, and state Gauss–Bonnet.
11. Compare the three geometries in a table, with correct hypotheses and proof notes.
12. Explain how non-Euclidean geometry enters general relativity, cartography, navigation and art.

## 4. Intuition

### 4.1 The flat map and the globe

A triangle on a flat sheet of paper has angles adding to $180^\circ$. Now draw a large triangle on the Earth:
start at the North Pole, go south along the prime meridian to the equator, turn east and follow the equator a
quarter of the way around the world, then turn north and return to the pole along the meridian at longitude
$90^\circ$ east. Each turn is a right angle. The "triangle" has three angles of $90^\circ$, whose sum is
$270^\circ$.

Nothing is wrong with the arithmetic. The sides are not Euclidean straight lines; they are **great circles**
on a sphere. A great circle is the intersection of the sphere with a plane through its centre. It is the
straightest path an ant can walk on the surface, and the shortest path between any two of its points that are
not antipodal. On a sphere the shortest-path "lines" bend around the surface, and the angle sum records how
much the surface curves.

Now imagine a saddle. Draw a triangle whose sides are shortest paths on the saddle. Its angles add to *less*
than $180^\circ$. A surface curved like a sphere is **positively curved**; a plane has **zero curvature**; a
saddle has **negative curvature**. The angle sum of a geodesic triangle measures curvature, and the three
geometries of this chapter are the simplest surfaces of constant positive, zero and negative curvature.

### 4.2 Three answers to one question

Fix a line $\ell$ and a point $P$ not on it. Ask: *how many lines through $P$ never meet $\ell$?*

* **Euclidean geometry:** exactly one. This is Playfair's form of the fifth postulate.
* **Spherical geometry:** none. Every two great circles meet, twice, in antipodal points.
* **Hyperbolic geometry:** infinitely many. Two are special **limiting parallels** that approach $\ell$
  asymptotically; the rest recede from it.

That single question organises the subject. The Euclidean answer is not a logical necessity; it is a choice
of axiom. Each choice produces a different theory of line, angle, area and triangle, and each theory is
internally consistent.

### 4.3 Curvature is intrinsic

Curvature is not a property of a surface as seen from outside; it is a property the inhabitants can measure.
Gauss's **Theorema Egregium** says that the Gaussian curvature $K$ of a surface is intrinsic: it can be
computed from measurements of lengths and angles on the surface alone. An ant on a sphere can detect the
curvature by drawing a large circle and comparing its circumference with $2\pi r$, or by drawing a large
triangle and measuring its angles. A flat sheet of paper and a cylinder both have $K=0$; that is why paper
can be rolled into a cylinder without stretching. A sphere has $K=1/R^2>0$, and no rolling turns paper into a
sphere without tearing. This is why every flat map of the Earth distorts something: area, angle, or distance.

For a surface of constant curvature, the angle sum of a geodesic triangle is

$$\text{angle sum}=\pi+K\cdot(\text{area of the triangle}).$$

For the sphere of radius $R$, $K=1/R^2$ and the excess is positive. For the hyperbolic plane with
$K=-1/R^2$, the excess is negative and the angle sum is less than $\pi$. For the plane, $K=0$ and the sum is
exactly $\pi$. This is a special case of the Gauss–Bonnet theorem and the most useful fact in the chapter.

### 4.4 Why models matter

"The parallel postulate cannot be proved from the other axioms" is a statement about *all possible proofs*.
To prove a negative statement of that kind, one uses a **model**: a concrete object in which the other axioms
are true and the parallel postulate is false. If such an object exists, then any proof of the parallel
postulate from the other axioms would have to be valid in that object; but the conclusion is false there.
Hence no such proof exists.

The object must be built from something already trusted. The Poincaré disk and the Klein model are built
from Euclidean geometry: their points are ordinary points of a disk, their lines are ordinary chords or
circular arcs, and their distances are explicit formulas. Every axiom of hyperbolic geometry becomes a
theorem of Euclidean geometry about these objects. This is a **relative consistency proof**: if Euclidean
geometry is consistent, then so is hyperbolic geometry. It is the model, not the picture, that settles the
two-thousand-year question.

## 5. Formal Definition

### 5.1 Euclid's postulates

Euclid's five postulates, in the standard English rendering, are:

1. A straight line segment can be drawn joining any two points.
2. Any straight line segment can be extended indefinitely in a straight line.
3. Given any straight line segment, a circle can be drawn having the segment as radius and one endpoint as
   centre.
4. All right angles are congruent.
5. If a straight line falling on two straight lines makes the interior angles on the same side less than two
   right angles, then the two straight lines, if produced indefinitely, meet on that side on which the angles
   are less than two right angles.

The fifth postulate is the only one that asserts an intersection at an unspecified distance; Euclid needs it
first at Proposition I.29.

### 5.2 Neutral geometry

**Definition 5.1 (Neutral or absolute geometry).** *Neutral geometry* is the theory obtained from Hilbert's
axioms of incidence, order, congruence and continuity, **without** any parallel axiom. Its theorems hold in
every geometry satisfying those axioms, Euclidean, hyperbolic or otherwise. When the Archimedean axiom is
included, we speak of *Archimedean neutral geometry*.

Neutral geometry is the right setting for the historical question, because it isolates exactly what the
parallel postulate adds. It contains all of Euclid's propositions before I.29: congruence criteria, the
existence of perpendiculars, the exterior angle theorem, and the fact that through an exterior point there
is *at least* one parallel (drop a perpendicular from $P$ to $\ell$, then erect another at $P$).

**Definition 5.2 (Parallel lines).** Two coplanar lines are **parallel** if they do not meet. In hyperbolic
geometry, two disjoint lines are **ultraparallel** if they have a common perpendicular and **limiting
parallel** if they approach each other asymptotically; both are parallel in the sense of being disjoint.

**Definition 5.3 (Playfair's axiom).** *For every line $\ell$ and every point $P\notin\ell$, there is at most
one line through $P$ parallel to $\ell$.* Since existence is a theorem of neutral geometry, Playfair is
equivalent to "exactly one". Its equivalence with Euclid V is proved in §8.1.

### 5.3 The three geometries

**Definition 5.4 (Euclidean geometry).** Neutral geometry together with Playfair's axiom (equivalently,
Euclid's fifth postulate).

**Definition 5.5 (Hyperbolic geometry).** Neutral geometry together with the negation of Playfair's axiom:
for every line $\ell$ and every point $P\notin\ell$, there are at least two distinct lines through $P$ that
do not meet $\ell$. In the standard models there are infinitely many; two already imply infinitely many in
neutral geometry.

**Definition 5.6 (Spherical geometry).** Let $S^2_R=\{x\in\mathbb{R}^3:\lVert x\rVert=R\}$. A **great circle**
is the intersection of $S^2_R$ with a plane through the origin. The **spherical distance** is
$$d_S(P,Q)=R\arccos\!\left(\frac{\langle P,Q\rangle}{R^2}\right),$$
the length of the shorter great-circle arc. A **spherical line** is a great circle; a **spherical triangle**
is a region bounded by three minor great-circle arcs, with angles measured between tangent vectors.

Spherical geometry is not a model of neutral geometry. Two antipodal points lie on infinitely many great
circles, so "two points determine a line" fails; a great circle is closed and has finite length; and the
order axioms fail. It is nevertheless a metric geometry and the easiest model of the *negation of Playfair*.
The distinction between "a model of $\neg$Playfair" and "a model of neutral geometry plus $\neg$Playfair" is
essential, and is discussed in §7.3.

**Definition 5.7 (Elliptic geometry).** Identify antipodal points of $S^2_R$. The quotient $S^2_R/\!\sim$ is
the real projective plane $\mathbb{RP}^2$. Great circles become projective lines, any two meet in exactly one
point, and there are no parallels. This is **elliptic geometry**; its total area is $2\pi R^2$.

### 5.4 Geodesics and curvature

**Definition 5.8 (Geodesic).** On a smooth surface $S$ with a Riemannian metric, a **geodesic** is a curve
that is locally length-minimising: every sufficiently short subarc is the shortest curve on $S$ between its
endpoints. Equivalently, its acceleration is normal to the surface, so it has no component tangential to
$S$. Geodesics are the surface analogue of straight lines.

**Definition 5.9 (Gaussian curvature).** For a smooth orientable surface $S\subset\mathbb{R}^3$, let
$\kappa_1(p),\kappa_2(p)$ be the maximum and minimum normal curvatures of curves through $p$. The **Gaussian
curvature** is $K(p)=\kappa_1(p)\kappa_2(p)$. A sphere of radius $R$ has $K=1/R^2$; a plane has $K=0$; a
saddle has $K<0$. The **Theorema Egregium** (Gauss, 1827) states that $K$ is intrinsic: it is unchanged by
local isometries and can be computed from the first fundamental form alone.

### 5.5 Models and consistency

**Definition 5.10 (Model).** A **model** of an axiom system is an interpretation of its primitive terms
(points, lines, incidence, betweenness, congruence, ...) as concrete mathematical objects, together with a
proof that every axiom becomes a true statement about those objects.

**Definition 5.11 (Relative consistency).** A theory $T_2$ is **consistent relative to** $T_1$ if
$\operatorname{Con}(T_1)\Rightarrow\operatorname{Con}(T_2)$; typically this is proved by interpreting $T_2$
inside a model of $T_1$.

The Poincaré disk and the Klein model are models of hyperbolic geometry built inside Euclidean geometry.
They prove: *if Euclidean geometry is consistent, then hyperbolic geometry is consistent*. This is the
precise sense in which hyperbolic geometry is as real as Euclidean geometry.

## 6. Mathematical Notation

| Symbol | Read as | Meaning |
|---|---|---|
| $S^2_R$ | sphere of radius $R$ | $\{x\in\mathbb{R}^3:\lVert x\rVert=R\}$ |
| $d_S(P,Q)$ | spherical distance | $R\arccos(\langle P,Q\rangle/R^2)$ |
| $\mathbb{D}$ | the disk | $\{z\in\mathbb{C}:\lvert z\rvert<1\}$ |
| $\mathbb{H}$ | upper half-plane | $\{z\in\mathbb{C}:\operatorname{Im}z>0\}$ |
| $d_{\mathbb{D}}(z,w)$ | Poincaré distance | $2\operatorname{artanh}\left\lvert\dfrac{z-w}{1-\bar z w}\right\rvert$ |
| $d_{\mathbb{H}}(z,w)$ | hyperbolic distance | $\operatorname{arcosh}\left(1+\dfrac{\lvert z-w\rvert^2}{2\operatorname{Im}z\operatorname{Im}w}\right)$ |
| $K$ | curvature | Gaussian curvature, in $\text{length}^{-2}$ |
| $A+B+C-\pi$ | spherical excess | positive for spherical triangles, in radians |
| $\pi-(A+B+C)$ | hyperbolic defect | positive for hyperbolic triangles, in radians |
| $\Pi(d)$ | angle of parallelism | angle between the perpendicular and a limiting parallel at distance $d$ |
| $[P,A;B,Q]$ | cross ratio | $\dfrac{(p-a)(q-b)}{(p-b)(q-a)}$ for parameters $p,a,b,q$ |

Angles are in **radians** in every formula involving $\pi$. When degrees are used, the conversion is
explicit. The symbol $\parallel$ between two lines means "parallel"; between a point and a line it is
shorthand for "the line through the point is parallel to the given line", with the intended line clear from
context.

## 7. Core Concepts

### 7.1 The parallel postulate and its equivalents

Euclid's fifth postulate is not an isolated curiosity. In Archimedean neutral geometry it is equivalent to
each of the following:

* the angle sum of every triangle is $\pi$;
* the angle sum of *one* triangle is $\pi$ (and then it is $\pi$ for all);
* there exist two triangles that are similar but not congruent;
* there exists a rectangle (a quadrilateral with four right angles);
* the Pythagorean theorem holds for every right triangle.

The first equivalence is the one used in school, but it is not a definition: in neutral geometry the angle
sum of a triangle is always **at most** $\pi$ (Legendre's theorem, under the Archimedean axiom), and it can
be strictly less. The statement that it is exactly $\pi$ is a genuine additional assumption about the plane.

**Definition 7.1 (Saccheri quadrilateral).** A **Saccheri quadrilateral** is a quadrilateral $ABCD$ with
base $AB$, legs $AD$ and $BC$ perpendicular to $AB$, and $AD=BC$. The side $CD$ is the **summit**, and the
angles at $C$ and $D$ are the **summit angles**.

In neutral geometry the summit angles are equal (the two-step congruence proof is in §8.2). There are then
exactly three possibilities:

| Hypothesis | Summit angles | Geometry it signals |
|---|---|---|
| Right | $90^\circ$ | Euclidean |
| Obtuse | $>90^\circ$ | spherical-type (excluded in neutral geometry by line infinitude) |
| Acute | $<90^\circ$ | hyperbolic |

Saccheri called these the *right*, *obtuse* and *acute* hypotheses. He showed that the obtuse hypothesis
contradicts the assumption that a straight line is infinite, and he developed many theorems under the acute
hypothesis — the theorems of hyperbolic geometry. He then rejected them as "repugnant to the nature of a
straight line". That was a philosophical judgement, not a contradiction, and it delayed the subject by nearly
a century. A **Lambert quadrilateral** is the related figure with three right angles; its fourth angle is
right, obtuse or acute according to the same three hypotheses.

### 7.2 Two millennia of attempts

| Date | Mathematician | Contribution |
|---|---|---|
| c. 300 BC | Euclid | States the fifth postulate |
| 5th–13th century | Proclus, Khayyam, al-Tusi | Attempted proofs; Saccheri-type quadrilaterals; three hypotheses |
| 1733 | Giovanni Saccheri | Systematic study; rejects the acute case |
| 1766 | Johann Lambert | Hyperbolic trigonometry; notes the spherical analogy |
| 1794–1833 | Adrien-Marie Legendre | Angle-sum theorem; many attempted proofs |
| c. 1813–1830s | Carl Friedrich Gauss | Develops hyperbolic geometry privately; does not publish |
| 1829 | Nikolai Lobachevsky | Publishes "On the Foundations of Geometry" |
| 1832 | János Bolyai | Publishes the "Appendix" |
| 1868 | Eugenio Beltrami | Pseudosphere and projective model; relative consistency |
| 1871 | Felix Klein | Projective (Klein) model |
| 1882 | Henri Poincaré | Disk and half-plane models |
| 1899 | David Hilbert | Rigorous axioms and independence proofs |

Three features deserve emphasis. First, the results were discovered before they were justified: Bolyai and
Lobachevsky published consistent developments of hyperbolic geometry, but neither had a model inside
Euclidean geometry; Beltrami supplied one in 1868, turning consistency into a theorem relative to Euclidean
geometry. Second, Gauss's silence is not a mystery: he had the ideas, and his work on intrinsic curvature
contains the tools that make the subject inevitable, but he avoided the philosophical controversy. His
geodetic measurement of the triangle Hohenhagen–Brocken–Inselsberg in the 1820s found a deviation from $\pi$
within observational error; a local measurement cannot decide the global geometry of space anyway. Third,
the names are not the whole story: Omar Khayyam and Nasir al-Din al-Tusi studied the same configurations as
Saccheri, and their work was known in Europe. The conventional "discovery in the nineteenth century"
narrative is about publication and rigour, not about the first people to notice the alternatives.

### 7.3 The independence of the parallel postulate

**Definition 7.2 (Independence).** Let $T$ be an axiom system and $S$ a statement in its language. $S$ is
**independent** of $T$ if neither $S$ nor its negation is provable from $T$. Equivalently, there is a model
of $T$ in which $S$ is true and a model of $T$ in which $S$ is false.

Take $T$ to be neutral geometry. The ordinary Euclidean plane is a model of $T$ plus Playfair, so Playfair is
not refutable from $T$. The Poincaré disk of §7.5 is a model of $T$ plus the negation of Playfair, so
Playfair is not provable from $T$. Therefore Playfair, and hence Euclid's fifth postulate, is independent of
the other axioms of neutral geometry. There is no proof of it and no disproof of it from those axioms alone.

The argument has a subtle structure. The Poincaré disk is built *inside* Euclidean geometry: its points are
ordinary points of a disk, its lines are ordinary circular arcs, and its distance is an ordinary integral.
Every axiom of neutral geometry, translated into this model, becomes a theorem of Euclidean geometry. If
hyperbolic geometry contained a contradiction, that contradiction would translate into a contradiction in
Euclidean geometry. Hence
$$\operatorname{Con}(\text{Euclidean geometry})\Longrightarrow\operatorname{Con}(\text{hyperbolic geometry}).$$
This is a **relative consistency** result. It does not prove absolute consistency — that would require a
consistency proof for the ambient set theory, which Gödel's second incompleteness theorem rules out for
sufficiently strong systems. It proves that hyperbolic geometry is no more dangerous than Euclidean geometry,
and that the parallel postulate cannot be recovered from the other axioms.

**Why spherical geometry is not enough.** The sphere has no parallels, but it does not satisfy neutral
geometry: two antipodal points lie on infinitely many great circles, a great circle is closed and has finite
length, and the order axioms fail. In particular, neutral geometry proves that through a point not on a line
there is *at least one* parallel, and the sphere has none. A model of $T+\neg$Playfair must satisfy *all* of
$T$, not merely the negation of the parallel postulate. The Poincaré disk is such a model; the sphere is not.
This distinction is a common source of confusion.

**What independence does not mean.** It does not mean that the parallel postulate is false, or that Euclidean
geometry is wrong. It does not mean that the postulate is independent of *every* conceivable axiom system;
independence is always relative to a specified list of axioms. Nor is it a statement about the physical
universe: whether space is Euclidean, spherical or hyperbolic on cosmological scales is an empirical question.

### 7.4 Spherical geometry

A sphere is the simplest curved surface, and its geometry is the easiest non-Euclidean geometry to see.
Throughout, $S^2_R$ is the sphere of radius $R$ centred at the origin in $\mathbb{R}^3$.

**Lines and distance.** A great circle is the intersection of $S^2_R$ with a plane through the origin. It is a
circle of radius $R$, hence has length $2\pi R$. Two distinct great circles meet in exactly two antipodal
points. The spherical distance is the length of the shorter arc of the great circle through $P$ and $Q$:
$$d_S(P,Q)=R\arccos\!\left(\frac{\langle P,Q\rangle}{R^2}\right)\in[0,\pi R].$$
The distance is $\pi R$ exactly when $P$ and $Q$ are antipodal; then there is no unique shortest path, since
every great circle through $P$ also passes through $Q$.

**Triangles and angles.** A spherical triangle is bounded by three minor arcs of great circles. Its angles
are the angles between tangent vectors to the arcs, equivalently the dihedral angles between the planes of
the great circles. We consider nondegenerate triangles with sides shorter than $\pi R$ and vertices not
collinear on a great circle.

The fundamental theorem is **Girard's theorem**:
$$\operatorname{area}(T)=R^2\bigl(A+B+C-\pi\bigr),$$
where $A,B,C$ are in radians. The quantity $A+B+C-\pi$ is the **spherical excess**. It is positive, so every
spherical triangle has angle sum greater than $\pi$. The proof is in §8.4: a lune of angle $\theta$ has area
$2R^2\theta$ (it is the fraction $\theta/(2\pi)$ of the sphere), and counting the three lunes determined by
the sides gives the formula.

**Consequences.** (i) There are no parallel lines. (ii) Angle sums exceed $\pi$; a triangle with three right
angles has excess $\pi/2$ and area $\pi R^2/2$. (iii) Since each angle is less than $\pi$, the excess is less
than $2\pi$, so a triangle has area less than $2\pi R^2$. (iv) The angles determine the area and, by AAA, the
triangle up to congruence, so there are no similar non-congruent spherical triangles. (v) If $C=\pi/2$, then
$\cos c=\cos a\cos b$; for small sides $c^2\approx a^2+b^2$, so Pythagoras is the local limit.

**Spherical trigonometry.** For a triangle on the unit sphere, with sides $a,b,c$ as central angles and
opposite angles $A,B,C$,
$$\cos c=\cos a\cos b+\sin a\sin b\cos C,\qquad
\frac{\sin A}{\sin a}=\frac{\sin B}{\sin b}=\frac{\sin C}{\sin c}.$$
For a sphere of radius $R$, replace $a,b,c$ by $a/R,b/R,c/R$. Both formulas are proved in §8.5 by vector
algebra: the vertices are unit vectors, and dot and cross products compute the relevant cosines and sines.

**What fails.** Spherical geometry is a metric geometry with a rich trigonometry, but it is not a model of
neutral geometry. Two antipodal points determine infinitely many great circles; a great circle has finite
length and closes up; the order axioms fail; and through a point not on a great circle there is no parallel
at all, whereas neutral geometry proves that at least one exists. The last point matters: the sphere models
the negation of Playfair but not neutral geometry, so it cannot replace the Poincaré disk.

**Elliptic geometry.** Identifying antipodal points removes the first and third failures: the quotient
$\mathbb{RP}^2=S^2_R/\!\sim$ has unique lines through any two points, any two lines meet in exactly one point,
and there are no parallels. Angles are unchanged, angle sums still exceed $\pi$, and the total area is
$2\pi R^2$. Elliptic geometry is the positive-curvature geometry with unique lines; spherical geometry is
its double cover.

### 7.5 Hyperbolic geometry

Hyperbolic geometry is neutral geometry plus the negation of Playfair: through a point not on a line there
are at least two lines that never meet it. In the standard models there are infinitely many; two are
**limiting parallels** that approach the given line asymptotically, and the rest are **ultraparallel** and
have a common perpendicular.

**The Poincaré disk.** Let $\mathbb{D}=\{z\in\mathbb{C}:|z|<1\}$ and
$$ds^2=\frac{4\,(dx^2+dy^2)}{(1-x^2-y^2)^2},\qquad
d_{\mathbb{D}}(z,w)=2\operatorname{artanh}\left|\frac{z-w}{1-\bar z w}\right|.$$
This metric has constant curvature $K=-1$. Its geodesics are the diameters of the disk and the arcs of circles
that meet the boundary circle at right angles. The model is **conformal**: hyperbolic angles equal Euclidean
angles, because the metric is a positive scalar multiple of the Euclidean metric at every point. This is why
pictures of the disk look like ordinary circles and arcs, even though distances and areas are wild.

**The upper half-plane.** Let $\mathbb{H}=\{z\in\mathbb{C}:\operatorname{Im}z>0\}$ and
$$ds^2=\frac{dx^2+dy^2}{y^2},\qquad
d_{\mathbb{H}}(z,w)=\operatorname{arcosh}\!\left(1+\frac{|z-w|^2}{2\operatorname{Im}z\operatorname{Im}w}\right).$$
This metric also has curvature $K=-1$. Its geodesics are the vertical half-lines $x=\text{constant}$ and the
semicircles centred on the real axis. The map
$$z\longmapsto i\,\frac{1+z}{1-z}$$
is an isometry $\mathbb{D}\to\mathbb{H}$; it sends the boundary circle to the real line and $0$ to $i$. The two
models are the same geometry in different coordinates.

**Why the geodesics look like that.** The geodesic equations are given in §8.10. Vertical lines and
semicircles centred on the real axis satisfy them, and through every point and direction there is exactly one
such curve, so these are *all* the geodesics; the disk case follows from the isometry.

**Angle sums and area.** Hyperbolic triangles have angle sum **less than** $\pi$. The difference
$\delta=\pi-(A+B+C)$ is the **hyperbolic defect**. For curvature $K=-1$, Gauss–Bonnet gives
$$\operatorname{area}(T)=\pi-(A+B+C).$$
For curvature $K=-1/R^2$, the area is $R^2$ times the defect. Unlike the sphere, there is no upper bound on
the side lengths, and the area of a triangle is bounded by $\pi R^2$: as the vertices move apart, the angles
tend to $0$ and the area tends to $\pi R^2$. The limiting object is an **ideal triangle**, with vertices on
the boundary circle and all three angles zero.

**Growth of area.** In the hyperbolic plane, a disk of radius $r$ has circumference and area
$$C(r)=2\pi\sinh r,\qquad A(r)=2\pi(\cosh r-1)$$
for $K=-1$. Both grow like $\pi e^r$ as $r\to\infty$. This exponential growth is the most important
qualitative difference from the Euclidean plane, where $C=2\pi r$ and $A=\pi r^2$. Hyperbolic space has
"more room": the number of distinguishable directions grows exponentially with distance, and the boundary at
infinity is a circle of ideal points rather than a single point. For comparison, on a sphere of radius $R$,
$$C(r)=2\pi R\sin\frac rR,\qquad A(r)=2\pi R^2\left(1-\cos\frac rR\right),$$
and both tend to $0$ as $r\to\pi R$: the circle shrinks to the antipodal point and the disk covers the sphere.

**Hyperbolic trigonometry.** For sides $a,b,c$ and opposite angles $A,B,C$ in the unit-curvature hyperbolic
plane,
$$\cosh c=\cosh a\cosh b-\sinh a\sinh b\cos C,\qquad
\frac{\sinh a}{\sin A}=\frac{\sinh b}{\sin B}=\frac{\sinh c}{\sin C}.$$
They are derived in §8.8 from the hyperboloid model.

**The angle of parallelism.** Let $\ell$ be a line, $P$ a point at distance $d$ from $\ell$, and $Q$ the foot
of the perpendicular. Among the lines through $P$ missing $\ell$, two are limiting parallels; let $\Pi(d)$
be the angle between $PQ$ and either of them. For $K=-1$,
$$\tan\frac{\Pi(d)}{2}=e^{-d}.$$
As $d\to0$, $\Pi(d)\to\pi/2$; as $d\to\infty$, $\Pi(d)\to0$. The formula is proved in §8.9. It quantifies the
abundance of parallels: every angle between $0$ and $\Pi(d)$ gives a distinct line through $P$ missing $\ell$.

**Hyperboloid model.** For computations, the cleanest model is
$$\mathbb{H}^2=\{x=(x_0,x_1,x_2)\in\mathbb{R}^{2,1}:\langle x,x\rangle_{2,1}=-1,\ x_0>0\},$$
with $\langle x,y\rangle_{2,1}=x_1y_1+x_2y_2-x_0y_0$ and induced metric satisfying
$$\cosh d(x,y)=-\langle x,y\rangle_{2,1}.$$
The isometry group is the identity component of $O(2,1)$; this model makes the hyperbolic law of cosines a
one-line computation (§8.8).

**No smooth global embedding in $\mathbb{R}^3$.** The pseudosphere has constant negative curvature but is
incomplete, and Hilbert's theorem (1901) says no complete smooth surface of constant negative curvature
exists in $\mathbb{R}^3$. The models above are therefore abstract Riemannian manifolds; the pseudosphere is
only a local model.

### 7.6 Models and consistency via the Klein model

The **Klein model** (Beltrami–Klein model) is the unit disk with points the interior points, **lines** the open
chords, and **ideal points** the boundary circle. Two chords that do not meet inside the disk are parallel;
through a point not on a chord there are infinitely many chords that miss it.

**Distance.** Let $A,B$ be distinct interior points and $P,Q$ the ideal endpoints of the chord through them,
ordered $P,A,B,Q$. Choose a linear coordinate $t$ on the chord and write $p,a,b,q$ for the coordinates. Define
$$d_K(A,B)=\frac12\left|\ln\frac{(p-a)(q-b)}{(p-b)(q-a)}\right|.$$
The expression inside the logarithm is a cross ratio; it is independent of the coordinate. For a point at
Euclidean distance $r$ from the centre along a diameter, $p=-1$, $a=0$, $b=r$, $q=1$, so
$$d_K(0,r)=\frac12\ln\frac{1+r}{1-r}=\operatorname{artanh}r.$$
The metric has curvature $K=-1$; its geodesics are the chords, which are straight in the Euclidean sense. The
model is **not conformal**: hyperbolic angles are not the Euclidean angles between chords, except at the
centre. That is the price for having straight lines.

**Relation to the Poincaré disk.** The models share the same underlying disk but use different radial
calibrations. If a point has hyperbolic distance $d$ from the centre, its Euclidean radius is
$$r_K=\tanh d\quad\text{in the Klein model},\qquad r_P=\tanh\frac d2\quad\text{in the Poincaré model},$$
so $r_K=2r_P/(1+r_P^2)$. The same Euclidean point $r=1/2$ therefore represents different hyperbolic points:
$d_K=\operatorname{artanh}(1/2)\approx0.549$ and $d_P=2\operatorname{artanh}(1/2)\approx1.099$.

**Why the Klein model proves consistency.** Every axiom of hyperbolic geometry is a theorem about chords of a
disk. Incidence: two interior points lie on a unique chord. Order: order along a chord is the ordinary order
of real numbers. Congruence: congruent segments are defined as segments of equal cross-ratio distance, and
the congruence axioms are calculations with cross ratios. Continuity: the disk is complete in the
cross-ratio metric. Parallel property: through an interior point not on a chord there are infinitely many
chords that miss it. Each is a theorem of Euclidean geometry, so the Klein model is a model of hyperbolic
geometry inside Euclidean geometry; the relative consistency argument of §7.3 applies. Beltrami's 1868 paper
used a projective construction of this kind, and Klein's 1871 papers gave the model its modern form. The
Poincaré disk is obtained from it by the radial map above and is conformal, which makes it better for drawing
angles; the Klein model is better for drawing lines.

**Elliptic model.** The same projective method gives elliptic geometry: points are the points of
$\mathbb{RP}^2$, lines are projective lines, and distance is defined by a cross ratio with respect to the two
circular points at infinity. Elliptic geometry has no parallels, angle sums greater than $\pi$, and is the
quotient of spherical geometry by the antipodal map.

### 7.7 Curvature as the unifying idea

The three geometries are not isolated subjects. They are the constant-curvature cases of Riemannian
geometry, and the curvature determines the angle sum.

**Gauss–Bonnet for geodesic triangles.** For a geodesic triangle $T$ on a smooth surface, with interior angles
$A,B,C$,
$$A+B+C-\pi=\iint_T K\,dA.$$
For constant curvature $K$, $A+B+C-\pi=K\cdot\operatorname{area}(T)$. The theorem is proved in differential
geometry; the spherical case is Girard's theorem (§8.4), and the plane case $K=0$ is the classical angle sum.

| Curvature | Geometry | Angle sum | Area of a triangle |
|---|---|---|---|
| $K=1/R^2>0$ | sphere of radius $R$ | $>\pi$ | $R^2(A+B+C-\pi)$ |
| $K=0$ | Euclidean plane | $=\pi$ | no constraint from angles |
| $K=-1/R^2<0$ | hyperbolic plane | $<\pi$ | $R^2(\pi-A-B-C)$ |

Each row is a complete geometry with its own trigonometry, area formulas and models; each is the unique
simply connected complete surface of its constant curvature, up to isometry and scaling (the Killing–Hopf
classification theorem for surfaces, building on Minding's 1839 work).

**Scale and units.** Curvature has units of inverse length squared. A sphere of radius $R$ has $K=1/R^2$; a
hyperbolic plane of "radius" $R$ has $K=-1/R^2$. Rescaling the metric by $\lambda$ multiplies lengths by
$\lambda$, areas by $\lambda^2$, and divides curvature by $\lambda^2$. Angle sums are dimensionless and
unchanged by scaling, which is why $A+B+C-\pi=K\cdot\text{area}$ is consistent. In the unit-curvature
normalization $K=\pm1$, and the excess or defect equals the area.

**Intrinsic versus extrinsic.** Gaussian curvature was defined as a product of principal curvatures in
$\mathbb{R}^3$, but the Theorema Egregium says it is intrinsic: an ant can measure $K$ by measuring the angle
sum of a large geodesic triangle or the circumference of a circle of radius $r$:
$$C_K(r)=\begin{cases}
2\pi\dfrac{\sin(r\sqrt K)}{\sqrt K}, & K>0,\\[6pt]
2\pi r, & K=0,\\[4pt]
2\pi\dfrac{\sinh(r\sqrt{-K})}{\sqrt{-K}}, & K<0.
\end{cases}$$
Expanding for small $r$ gives $C_K(r)=2\pi r-\frac{\pi K}{3}r^3+O(r^5)$: the first deviation from $2\pi r$
is cubic, with sign opposite to the sign of $K$. This is why curvature is invisible on small scales, and why
Gauss's terrestrial triangle could not settle the geometry of space.

**Total curvature.** On a compact surface, the global Gauss–Bonnet theorem says
$$\iint_S K\,dA=2\pi\chi(S),$$
where $\chi(S)$ is the Euler characteristic. For the sphere $\chi=2$ and the total curvature is $4\pi$,
independent of the radius; for a torus $\chi=0$ and the total curvature is zero. This is a topological
constraint on any metric a surface can carry, and the beginning of the interaction between curvature and
topology.

### 7.8 Consequences for physics

**General relativity.** In Einstein's theory, spacetime is a four-dimensional **Lorentzian** manifold: at each
point the tangent space carries a Minkowski inner product rather than a Euclidean one. Curvature is encoded in
the Riemann tensor, and the Einstein field equations $G_{\mu\nu}=8\pi G\,T_{\mu\nu}$ relate curvature to
energy and momentum. Freely falling particles follow timelike geodesics; the convergence or divergence of
nearby geodesics is tidal gravity. The precession of Mercury's perihelion, the bending of light by the Sun,
gravitational lensing, the Shapiro delay, black holes and gravitational waves are consequences of this
geometric picture.

The relation to this chapter is indirect: the hyperbolic plane is a two-dimensional Riemannian manifold of
constant negative curvature, while a spacetime is a four-dimensional Lorentzian manifold with variable
curvature. What carries over is the *method*: geometry is encoded in a metric, straight lines become
geodesics, and curvature is measured by comparison with a flat model. The Milne, de Sitter and anti-de Sitter
models are the simplest exact cosmological solutions and illustrate the roles of spatial curvature and the
cosmological constant.

**Cosmology.** The Friedmann–Lemaître–Robertson–Walker models describe a homogeneous, isotropic universe whose
spatial slices have constant curvature with sign $k\in\{+1,0,-1\}$. The curvature parameter $\Omega_k$
measures the departure from flatness; observations of the cosmic microwave background (Planck 2018) are
consistent with $\Omega_k=0$ within about $0.002$. This is an empirical statement, not a theorem, and it is
the modern version of Gauss's question about the geometry of space. Curvature is a second-order effect, which
is why the Earth looks flat from a garden.

**GPS and geodesy.** Satellite navigation combines great-circle geometry, ellipsoidal geodesy, and
relativistic clock corrections, a practical confirmation that spacetime is not Newtonian.

### 7.9 Consequences for art

**Escher's *Circle Limit* prints.** Between 1958 and 1960, M. C. Escher made four prints — *Circle Limit I–IV*
— in which infinitely many congruent figures fit inside a finite circle, becoming smaller toward the
boundary. They are accurate drawings of tessellations of the Poincaré disk, inspired by his correspondence
with the geometer H. S. M. Coxeter. The visual paradox is the exponential growth of hyperbolic area: a disk
of finite hyperbolic radius has area $2\pi(\cosh r-1)$, and the boundary is at infinite distance.

**Perspective and projective geometry.** Renaissance perspective is not non-Euclidean geometry, but it is its
historical gateway. In a perspective drawing, parallel lines meet at vanishing points; the geometry of the
picture plane is projective geometry, where the Euclidean parallel postulate is replaced by the statement that
any two lines meet at a point at infinity. Klein later classified geometries by their transformation groups:
Euclidean geometry is the geometry of rigid motions, affine geometry of affine transformations, projective
geometry of projectivities, and hyperbolic geometry of projectivities preserving a conic.

**Hyperbolic crochet and architecture.** Daina Taimina's crocheted models of the hyperbolic plane (from 1997)
made the exponential growth of area tangible: each ring of stitches must be larger than the last, and the
model frills uncontrollably. Saddle-shaped tensile roofs, hyperbolic paraboloid shells and some cooling towers
are negatively curved surfaces; they are not the hyperbolic plane, but they share its local geometry.
Spherical domes, geodesic domes and planetariums realise positive curvature. Architecture has used
non-Euclidean geometry for centuries, often without naming it.

**Literature and philosophy.** Before the nineteenth century, axioms were often regarded as self-evident
truths about the world; afterwards they became hypotheses that define a structure. This shift is reflected
in conventionalism (Poincaré, Duhem) and in the philosophy of science, and it is why modern geometry begins
with axioms and a definition of "model" rather than with a picture.

### 7.10 Comparison table

| Feature | Euclidean | Spherical | Hyperbolic |
|---|---|---|---|
| Curvature | $K=0$ | $K=1/R^2$ | $K=-1/R^2$ |
| Lines | straight lines | great circles | geodesics (diameters and orthogonal arcs) |
| Parallels through $P\notin\ell$ | exactly one | none | infinitely many |
| Angle sum of a triangle | $\pi$ | $> \pi$ | $< \pi$ |
| Excess/defect | $0$ | $A+B+C-\pi=\operatorname{area}/R^2$ | $\pi-(A+B+C)=\operatorname{area}/R^2$ |
| Triangle area | unbounded | $<2\pi R^2$ | $< \pi R^2$ (ideal limit) |
| Circle circumference | $2\pi r$ | $2\pi R\sin(r/R)$ | $2\pi R\sinh(r/R)$ |
| Disk area | $\pi r^2$ | $2\pi R^2(1-\cos(r/R))$ | $2\pi R^2(\cosh(r/R)-1)$ |
| Similar non-congruent triangles | yes | no | no |
| Law of cosines | $c^2=a^2+b^2-2ab\cos C$ | $\cos(c/R)=\cos(a/R)\cos(b/R)+\sin(a/R)\sin(b/R)\cos C$ | $\cosh(c/R)=\cosh(a/R)\cosh(b/R)-\sinh(a/R)\sinh(b/R)\cos C$ |
| Standard model | $\mathbb{R}^2$ | $S^2_R$ | Poincaré disk, upper half-plane, Klein disk, hyperboloid |
| Consistency | assumed | relative to Euclidean (embedded in $\mathbb{R}^3$) | relative to Euclidean (Klein/Poincaré models) |
| Physical realisation | local approximation | Earth, planets, domes | saddle surfaces, crochet, cosmology |

**Proof notes.** The Euclidean angle sum is Proposition I.32 and is equivalent to the parallel postulate. The
spherical excess formula is Girard's theorem, proved in §8.4; the area bound follows because each angle is
less than $\pi$. The hyperbolic defect formula is Gauss–Bonnet for $K=-1$, stated in §7.7 and §8.11; the
bound $\pi R^2$ is approached by ideal triangles. The circumference and area formulas are obtained by
integrating the metric in geodesic polar coordinates; the hyperbolic case is derived in §8.10. The laws of
cosines are proved in §8.5 (spherical) and §8.8 (hyperbolic); the Euclidean case is the ordinary law of
cosines. The consistency column is a statement about relative consistency, not physical existence: the
spherical model is a subset of $\mathbb{R}^3$, and the hyperbolic models are built from Euclidean objects.

## 8. Formulas and Properties

### 8.1 Playfair's axiom and Euclid V are equivalent

**Theorem 8.1.** In Archimedean neutral geometry, Playfair's axiom is equivalent to Euclid's fifth postulate.

*Proof.* Assume Euclid V and suppose two distinct lines $m,m'$ through $P$ are both parallel to $\ell$. Let
$t$ be a line through $P$ meeting $\ell$ at $Q$. In the half-plane of $t$ containing a chosen ray of $\ell$,
let $\alpha$ be the interior angle at $Q$ and $\beta,\beta'$ the interior angles at $P$ made by $m,m'$. Since
$m\parallel\ell$, the same-side interior angles are supplementary: $\alpha+\beta=\pi$; similarly
$\alpha+\beta'=\pi$. Hence $\beta=\beta'$, so $m$ and $m'$ have the same ray from $P$ on that side of $t$ and
coincide, a contradiction. Thus at most one parallel exists.

Conversely, assume Playfair and suppose a transversal $t$ meets lines $\ell$ at $Q$ and $m$ at $P$, with
interior angles $\alpha$ at $Q$ and $\beta$ at $P$ on one side satisfying $\alpha+\beta<\pi$. Construct
through $P$ the line $m'$ making angle $\beta'=\pi-\alpha$ with $t$ on that side. Then $\alpha+\beta'=\pi$, so
the alternate interior angles are equal and $m'\parallel\ell$ by Proposition I.27. Since $\beta<\beta'$, the
line $m$ is not $m'$; by Playfair, $m$ meets $\ell$. If the intersection were on the other side of $t$, the
same-side interior angles there, $\pi-\alpha$ and $\pi-\beta$, would sum to $2\pi-(\alpha+\beta)>\pi$; but
two lines that meet on a side of a transversal form a triangle there, whose two interior angles have sum less
than $\pi$ (exterior angle theorem together with Legendre's bound). So the meeting is on the side where the
sum is less than $\pi$, which is Euclid V. ∎

### 8.2 Saccheri's theorem

**Theorem 8.2.** In neutral geometry the summit angles of a Saccheri quadrilateral are equal.

*Proof.* Let $ABCD$ have base $AB$, right angles at $A,B$, and $AD=BC$. Triangles $ABD$ and $BAC$ have
$AD=BC$, $AB=BA$, and included right angles equal, so $BD=AC$ by SAS. Triangles $ADC$ and $BCD$ have
$AD=BC$, $AC=BD$, and $DC=CD$, so they are congruent by SSS. Hence $\angle ADC=\angle BCD$. ∎

If the summit angles are right, the quadrilateral is a rectangle and the angle sum of each of the two
triangles cut by a diagonal is $\pi$, so Playfair holds. If they are acute, the defect is positive and the
geometry is hyperbolic. If they are obtuse, the angle sum of a triangle exceeds $\pi$; Saccheri showed this
contradicts the infinitude of the line, and it is realised only by spherical-type geometries.

### 8.3 Area of a lune

A **lune** is the region between two half great circles with common endpoints. If the angle between the half
circles is $\theta$ (radians), the lune is the fraction $\theta/(2\pi)$ of the sphere: rotating the lune about
the axis through its endpoints sweeps the sphere, and the area is proportional to $\theta$. Since the whole
sphere has area $4\pi R^2$, the lune has area
$$\operatorname{area}(\text{lune})=\frac{\theta}{2\pi}\cdot4\pi R^2=2R^2\theta .$$

### 8.4 Girard's theorem

**Theorem 8.3 (Girard).** For a nondegenerate spherical triangle $T$ on $S^2_R$ with angles $A,B,C$ in
radians,
$$\operatorname{area}(T)=R^2(A+B+C-\pi).$$

*Proof.* The three great circles containing the sides divide the sphere into eight spherical triangles: $T$,
its antipodal image $T'$, and six others forming three antipodal pairs $U,U'$, $V,V'$, $W,W'$, where $U$ is
adjacent to $T$ across the side opposite $A$, and similarly for $V,W$. The lune at $A$ of angle $A$ is
$T\cup U$, so by §8.3
$$\operatorname{area}(T)+\operatorname{area}(U)=2R^2A,$$
and similarly for $B$ and $C$. Adding,
$$2R^2(A+B+C)=3\operatorname{area}(T)+\operatorname{area}(U)+\operatorname{area}(V)+\operatorname{area}(W).$$
The eight triangles partition the sphere, and the antipodal map is an isometry, so
$$4\pi R^2=2\operatorname{area}(T)+2\bigl(\operatorname{area}(U)+\operatorname{area}(V)+\operatorname{area}(W)\bigr),$$
hence $\operatorname{area}(U)+\operatorname{area}(V)+\operatorname{area}(W)=2\pi R^2-\operatorname{area}(T)$.
Substituting,
$$2R^2(A+B+C)=2\operatorname{area}(T)+2\pi R^2,$$
which gives $\operatorname{area}(T)=R^2(A+B+C-\pi)$. ∎

### 8.5 Spherical law of cosines and sine law

**Theorem 8.4.** On the unit sphere, with sides $a,b,c$ (central angles) and opposite angles $A,B,C$,
$$\cos c=\cos a\cos b+\sin a\sin b\cos C.$$

*Proof.* Place the vertices at unit vectors $w=(0,0,1)$, $u=(\sin b,0,\cos b)$ (so the angle between $u$ and
$w$ is $b$), and $v=(\sin a\cos C,\sin a\sin C,\cos a)$ (so the angle between $v$ and $w$ is $a$, and the
dihedral angle at $w$ is $C$). Then
$$\cos c=u\cdot v=\sin b\sin a\cos C+\cos b\cos a. \qquad\square$$
For radius $R$, apply the formula to $a/R,b/R,c/R$.

**Theorem 8.5 (spherical sine law).** On the unit sphere,
$$\frac{\sin A}{\sin a}=\frac{\sin B}{\sin b}=\frac{\sin C}{\sin c}.$$

*Proof.* For unit vectors $u,v,w$, the identity $(u\times v)\times(u\times w)=[u\cdot(v\times w)]\,u$ holds.
The left side has magnitude $|u\times v|\,|u\times w|\sin A=\sin c\,\sin b\,\sin A$, since the angle between
the normals to the planes $uv$ and $uw$ is $A$ (or $\pi-A$, which has the same sine). The right side has
magnitude $|u\cdot(v\times w)|$, which is symmetric in $u,v,w$; computing it as $\sin a\,\sin b\,\sin C$
gives $\sin b\,\sin c\,\sin A=\sin a\,\sin b\,\sin C$, hence $\sin A/\sin a=\sin C/\sin c$. ∎

### 8.6 Spherical excess, area bound, and AAA

By Girard the excess $A+B+C-\pi$ is positive and equals $\operatorname{area}/R^2$. Since each angle is less
than $\pi$, the excess is less than $2\pi$, so $\operatorname{area}(T)<2\pi R^2$.

For AAA, use the **polar triangle** $T^*$: its vertices are the unit normals to the sides of $T$ (oriented
consistently), its side lengths are $\pi-A,\pi-B,\pi-C$, and its angles are $\pi-a,\pi-b,\pi-c$. Applying the
spherical law of cosines to $T^*$ gives the **dual law**
$$\cos A=-\cos B\cos C+\sin B\sin C\cos a,$$
and its cyclic permutations. Thus the angles $A,B,C$ determine $\cos a,\cos b,\cos c$, hence the side lengths.
Two spherical triangles with the same angles are therefore congruent.

### 8.7 Hyperbolic triangles have angle sum less than $\pi$

**Theorem 8.6.** Every nondegenerate hyperbolic triangle has angle sum strictly less than $\pi$.

*Proof.* Work in the Poincaré disk and use an isometry to send a vertex $A$ to the centre $O$. Isometries
preserve angles and geodesics, so it suffices to consider the triangle $OBC$ with $O$ the centre. The sides
$OB,OC$ are Euclidean radii; the side $BC$ is an arc of a circle $\gamma$ orthogonal to $\partial\mathbb{D}$.
We claim that this arc lies inside the Euclidean triangle $OBC$.

Let $P$ be the centre of $\gamma$ and $\rho$ its radius. Orthogonality gives $|P|^2=\rho^2+1$, so $|P|>1$. Each
ray from $O$ meets $\gamma$ in at most one point of $\mathbb{D}$: substituting $tX$ with $|X|=1$ gives
$t^2-2t(X\cdot P)+1=0$, whose roots have product $1$. Hence the arc, which is connected and joins $B$ to $C$,
stays inside the cone spanned by $OB$ and $OC$. The point of $\gamma$ farthest from $O$ is
$P(1+\rho/|P|)$, which lies outside $\mathbb{D}$; the arc inside $\mathbb{D}$ is the other arc between $B$ and
$C$, so it lies on the side of the chord $BC$ opposite that point. Since the chord lies in $\mathbb{D}$ and
$|P|>1$, the centre $P$ and the farthest point are on the same side of the chord; hence the inside arc is on
the $O$ side of $BC$. A connected arc in the cone and on the $O$ side of $BC$ is contained in the triangle
$OBC$.

Therefore the tangent to the arc at $B$ points into the Euclidean angle $\angle OBC$, so the hyperbolic angle
at $B$ is strictly smaller than the Euclidean angle at $B$; similarly at $C$. The angle at $O$ is unchanged.
The hyperbolic angle sum is therefore strictly less than the Euclidean angle sum $\pi$. ∎

### 8.8 Hyperbolic law of cosines and sine law

Use the hyperboloid model $\mathbb{H}^2=\{x\in\mathbb{R}^{2,1}:\langle x,x\rangle_{2,1}=-1,\ x_0>0\}$ with
$\langle x,y\rangle_{2,1}=x_1y_1+x_2y_2-x_0y_0$ and $\cosh d(x,y)=-\langle x,y\rangle_{2,1}$.

**Theorem 8.7.** For a hyperbolic triangle with sides $a,b,c$ and opposite angles $A,B,C$ in the
unit-curvature plane,
$$\cosh c=\cosh a\cosh b-\sinh a\sinh b\cos C.$$

*Proof.* Put $C=(1,0,0)$, $A=(\cosh b,\sinh b,0)$, and
$B=(\cosh a,\sinh a\cos C,\sinh a\sin C)$. Then
$$-\langle A,B\rangle_{2,1}=\cosh a\cosh b-\sinh a\sinh b\cos C.$$
Since $d(A,B)=c$, this is $\cosh c$. ∎

The **hyperbolic sine law** follows by substituting $\cos C=(\cosh a\cosh b-\cosh c)/(\sinh a\sinh b)$ into
$\sin^2C=1-\cos^2C$:
$$\sin^2C=\frac{1+2\cosh a\cosh b\cosh c-\cosh^2a-\cosh^2b-\cosh^2c}{\sinh^2a\sinh^2b},$$
whose numerator is symmetric in $a,b,c$; dividing by $\sinh^2c$ gives the common value, so
$$\frac{\sinh a}{\sin A}=\frac{\sinh b}{\sin B}=\frac{\sinh c}{\sin C}.$$
The **dual law** $\cos C=-\cos A\cos B+\sin A\sin B\cosh c$ follows from the side law by algebraic elimination;
it shows that the angles determine the sides, so AAA is a congruence criterion in hyperbolic geometry.

### 8.9 The angle of parallelism

Put $\ell$ on the imaginary axis of $\mathbb{H}$ and let $P=(x_0,y_0)$ with $x_0>0$. Let
$r=\sqrt{x_0^2+y_0^2}$. The geodesic through $P$ perpendicular to $\ell$ is the circle centred at $0$ of
radius $r$; it meets $\ell$ at $(0,r)$. By the distance formula,
$$\cosh d=\frac{r}{y_0},\qquad \sinh d=\frac{x_0}{y_0},\qquad \tanh d=\frac{x_0}{r}.$$
The limiting parallel through $P$ asymptotic to $\ell$ at infinity is the vertical line $x=x_0$. The tangent
to the perpendicular at $P$ has direction $(-y_0,x_0)$, and the vertical direction is $(0,1)$; the angle
$\Pi=\Pi(d)$ between them satisfies
$$\cos\Pi=\frac{x_0}{r}=\tanh d,\qquad \sin\Pi=\frac{y_0}{r}=\operatorname{sech}d.$$
Therefore
$$\tan\frac{\Pi}{2}=\frac{\sin\Pi}{1+\cos\Pi}
=\frac{\operatorname{sech}d}{1+\tanh d}
=\frac{1}{\cosh d+\sinh d}=e^{-d}. \qquad\square$$
For curvature $K=-1/R^2$, scaling gives $\tan(\Pi/2)=e^{-d/R}$.

### 8.10 Geodesics, distance, circumference and area

**Geodesics in $\mathbb{H}$.** For $ds^2=(dx^2+dy^2)/y^2$, the geodesic equations are
$$x''-\frac{2}{y}x'y'=0,\qquad y''+\frac{1}{y}\bigl((x')^2-(y')^2\bigr)=0.$$
Vertical lines satisfy them with $x'=0$. A semicircle $(x-a)^2+y^2=r^2$, parametrised by
$(x,y)=(a+r\cos\theta,r\sin\theta)$ with $\theta'=\sin\theta$, satisfies both equations (substitute and
simplify). Through each point and unit direction there is a unique such curve, so these are all the
geodesics. The Cayley isometry carries them to the orthogonal circles and diameters of the disk.

**Distance in $\mathbb{H}$.** Let
$$F(z,w)=1+\frac{|z-w|^2}{2\operatorname{Im}z\operatorname{Im}w}.$$
$F$ is invariant under translations $z\mapsto z+b$, dilations $z\mapsto\lambda z$ ($\lambda>0$), and the
inversion $z\mapsto-1/z$; these generate the isometry group. An isometry maps the geodesic through $z,w$ to a
vertical line and $z$ to $i$, so $w$ becomes $iy$. Then
$$F(i,iy)=1+\frac{(y-1)^2}{2y}=\frac{y^2+1}{2y}=\cosh(\ln y),$$
and the distance along the vertical geodesic is $|\ln y|$. Hence $d(z,w)=\operatorname{arcosh}F(z,w)$, which
is the formula of §7.5. The disk formula follows from the Cayley isometry.

**Circumference and area.** In the disk, let $r=d_{\mathbb{D}}(0,z)$; then $|z|=\rho=\tanh(r/2)$. The
hyperbolic area element is $4\rho\,d\rho\,d\theta/(1-\rho^2)^2$. Since
$d\rho/dr=\frac12\operatorname{sech}^2(r/2)$ and $1-\rho^2=\operatorname{sech}^2(r/2)$,
$$\frac{4\rho}{(1-\rho^2)^2}\,d\rho
=4\tanh\frac r2\cosh^4\frac r2\cdot\frac12\operatorname{sech}^2\frac r2\,dr
=\sinh r\,dr.$$
Thus the area element in geodesic polar coordinates is $\sinh r\,dr\,d\theta$, so
$$C(r)=\int_0^{2\pi}\sinh r\,d\theta=2\pi\sinh r,\qquad
A(r)=\int_0^r 2\pi\sinh s\,ds=2\pi(\cosh r-1). \qquad\square$$

### 8.11 Gauss–Bonnet and the defect–area relation

**Theorem 8.8 (Gauss–Bonnet for geodesic triangles).** If $T$ is a geodesic triangle on a smooth surface with
interior angles $A,B,C$, then
$$A+B+C-\pi=\iint_T K\,dA.$$
The theorem is proved in differential geometry (see the references in §16). The spherical case is Theorem 8.3;
the Euclidean case is the classical angle sum; the hyperbolic case with $K=-1$ gives
$\operatorname{area}(T)=\pi-(A+B+C)$. An ideal triangle (three vertices on the boundary circle, all angles
$0$) has area $\pi$, and a hyperbolic $n$-gon with interior angle sum $\Sigma$ has area
$(n-2)\pi-\Sigma$.

## 9. Step-by-Step Examples

**Example 9.1 (An octant).** On $S^2_R$, the triangle with vertices $(R,0,0),(0,R,0),(0,0,R)$ has three right
angles. Girard gives area $R^2(3\pi/2-\pi)=\pi R^2/2$, exactly one eighth of $4\pi R^2$. ✓

**Example 9.2 (Lune and a $72^\circ$ triangle).** A lune of angle $72^\circ=2\pi/5$ has area
$2R^2(2\pi/5)=4\pi R^2/5$. An equilateral spherical triangle with angles $72^\circ$ has excess
$3(2\pi/5)-\pi=\pi/5$ and area $\pi R^2/5$; twenty congruent copies tile the sphere, since
$20\cdot\pi R^2/5=4\pi R^2$. ✓

**Example 9.3 (Spherical law of cosines).** For $a=60^\circ$, $b=45^\circ$, $C=60^\circ$ on the unit sphere,
$$\cos c=\cos60^\circ\cos45^\circ+\sin60^\circ\sin45^\circ\cos60^\circ
=0.3536+0.3062=0.6598,$$
so $c=48.72^\circ$. Check the triangle inequality: $15^\circ<48.72^\circ<105^\circ$. ✓

**Example 9.4 (London to New York).** With $\varphi_1=51.5^\circ$, $\lambda_1=-0.1^\circ$,
$\varphi_2=40.7^\circ$, $\lambda_2=-74^\circ$, the great-circle formula
$\cos c=\sin\varphi_1\sin\varphi_2+\cos\varphi_1\cos\varphi_2\cos(\lambda_1-\lambda_2)$ gives
$c=50.12^\circ=0.8748$ rad. At $R=6371$ km the distance is $6371\times0.8748\approx5573$ km. ✓

**Example 9.5 (Poincaré and upper half-plane distances).**
$d_{\mathbb D}(0,\tfrac12)=2\operatorname{artanh}\tfrac12=\ln3\approx1.0986$; the midpoint is at Euclidean
radius $\tanh(\ln3/4)\approx0.268$, not $0.25$. In the upper half-plane, $d_{\mathbb H}(i,4i)=\ln4\approx1.386$
along the vertical geodesic, and $\cosh\ln4=(4+1/4)/2=17/8$. ✓

**Example 9.6 (Hyperbolic defect).** A hyperbolic triangle with angles $50^\circ,60^\circ,50^\circ$ has sum
$160^\circ$, defect $20^\circ=\pi/9$, and area $\pi/9\approx0.349$ for $K=-1$. For curvature $-1/R^2$ the area
is $R^2\pi/9$. ✓

**Example 9.7 (Hyperbolic right triangle and angle of parallelism).** With legs $a=b=1$ and $C=90^\circ$,
$\cosh c=\cosh^2 1\approx2.3811$, so $c=\operatorname{arcosh}2.3811\approx1.5134$, larger than the Euclidean
hypotenuse $\sqrt2\approx1.4142$. At distance $d=1$ the angle of parallelism is
$\Pi=2\arctan(e^{-1})\approx40.40^\circ$, far below the Euclidean $90^\circ$. ✓

## 10. Visual Explanations

The logical relations are summarised in the table. The row on spherical geometry records the trap: it models
the negation of Playfair but not the rest of neutral geometry, so it cannot be used for the independence
proof.

| Starting point | Operation | Result |
|---|---|---|
| Neutral geometry | add Playfair or its negation | Euclidean ($\mathbb{R}^2$) or hyperbolic ($\mathbb{D},\mathbb{H}$, Klein, hyperboloid) |
| Spherical geometry | fails neutral axioms | models $\neg$Playfair only; not a consistency model |
| Hyperbolic geometry | Klein or Poincaré model | consistent relative to Euclidean geometry |

The Cayley transform identifies the disk with the upper half-plane, the radial map identifies it with the
Klein disk, and central projection identifies it with the hyperboloid.

## 11. Common Mistakes

* **"Non-Euclidean means no parallels."** Hyperbolic geometry has infinitely many parallels through an
  exterior point; spherical geometry has none; elliptic geometry has none. The three cases are distinct.
* **"The sphere proves the parallel postulate is independent."** It does not: the sphere fails neutral
  geometry (antipodal points, closed lines, order axioms). Only a model of neutral geometry plus $\neg$Playfair
  proves independence, and that is the Poincaré/Klein model.
* **Using Euclidean formulas in a curved space.** Pythagoras, the area formula $\frac12ab\sin C$, and the
  Euclidean law of cosines are false on a sphere or in the hyperbolic plane; use the curved law of cosines.
* **Confusing a sphere's radius with its curvature.** $K=1/R^2$, not $R$: a large sphere has small curvature.
* **Forgetting radians.** Girard's formula and all the trigonometric formulas assume radians.
* **Thinking Poincaré "lines" are Euclidean lines.** Only the diameters are straight; every other geodesic is
  a circular arc orthogonal to the boundary. Likewise, the Klein model's chords are straight but its angles
  are not Euclidean.
* **Believing Gauss's measurement settled the geometry of space.** The deviation was within observational
  error, and curvature is a second-order effect; the question is cosmological.

## 12. Applications

* **Navigation, geodesy and cartography.** Great-circle routes, spherical trigonometry, ellipsoidal
  corrections, and the Theorema Egregium's explanation of why every flat map distorts something.
* **Astronomy, cosmology and GPS.** Celestial-sphere positions, gravitational lensing, Friedmann–Lemaître
  models with $k=+1,0,-1$, and relativistic clock corrections.
* **Art and architecture.** Escher's *Circle Limit* prints, perspective, saddle-shaped roofs, domes, and
  hyperbolic crochet models.

## 13. Exercises

The problem set is in [exercises.md](exercises.md): 36 problems, graded Beginner to Challenge, with
computations, proofs and applications.

## 14. Solutions

Complete worked solutions for every problem are in [solutions.md](solutions.md).

## 15. Summary

* Euclid's fifth postulate is independent of the other axioms of neutral geometry; Playfair's axiom is an
  equivalent form.
* Saccheri and Lambert reduced the question to the three hypotheses on the summit angles of a quadrilateral;
  Bolyai, Lobachevsky and (privately) Gauss accepted the acute case as a new geometry.
* Spherical geometry has great circles as lines, no parallels, angle sums greater than $\pi$, and
  $\operatorname{area}=R^2(A+B+C-\pi)$ (Girard).
* Hyperbolic geometry has infinitely many parallels, angle sums less than $\pi$,
  $\operatorname{area}=R^2(\pi-A-B-C)$, and exponential area growth $2\pi R^2(\cosh(r/R)-1)$.
* The Poincaré disk, upper half-plane, Klein disk and hyperboloid model hyperbolic geometry; the Klein model
  proves relative consistency with Euclidean geometry.
* Curvature unifies the three geometries: $A+B+C-\pi=\iint_T K\,dA$ (Gauss–Bonnet), with $K>0$, $K=0$ and
  $K<0$ giving the three cases.

## 16. Further Learning

Within this repository, continue with [Topology](../../17-topology/README.md) and
[Topological Spaces](../../17-topology/01-topological-spaces/README.md) for the point-set framework behind
"space", and with [Metric Spaces](../../14-real-analysis/06-metric-spaces/README.md) for distance and
isometries; [Calculus](../../07-calculus/README.md) supplies the integration used in the models.

Standard references: Marvin Greenberg, *Euclidean and Non-Euclidean Geometries*; David Hilbert and Stephan
Cohn-Vossen, *Geometry and the Imagination*; John Stillwell, *The Four Pillars of Geometry*; Manfredo do
Carmo, *Differential Geometry of Curves and Surfaces*; Tristan Needham, *Visual Complex Analysis*.

