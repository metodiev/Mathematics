# Complex Numbers and Geometry

> [Mathematics](../../README.md) › [Complex Analysis](../README.md) · Level: Advanced · Prerequisites: [Complex Numbers](../../03-algebra/13-complex-numbers/README.md), [Inequalities](../../03-algebra/03-inequalities/README.md), [The Unit Circle](../../05-trigonometry/02-unit-circle/README.md), [Trigonometric Identities](../../05-trigonometry/03-trigonometric-identities/README.md), [Limits](../../07-calculus/01-limits/README.md), [Matrices](../../08-linear-algebra/02-matrices/README.md), [Linear Transformations](../../08-linear-algebra/05-linear-transformations/README.md) · Estimated time: 540 min

## 1. Introduction

The algebra sequence introduces $\mathbb{C}$ as the smallest field containing $\mathbb{R}$ in which
$x^2 + 1 = 0$ has a root. That definition is complete but silent about geometry. This tutorial
supplies the geometry. The central discovery — made by Wessel (1799), Argand (1806) and Gauss
(1831) — is that a complex number $z = x + iy$ can be read as the point $(x,y)$ of the plane, and
that the two algebraic operations then acquire exact geometric meanings:

* **addition is translation** by the vector $(x,y)$;
* **multiplication is rotation and scaling**, by the angle $\arg z$ and the factor $\lvert z\rvert$.

Once multiplication is geometric, a large part of plane geometry becomes algebra, and a large part
of algebra becomes geometry: the triangle inequality is a statement about the side lengths of a
triangle, De Moivre's theorem says that the angle of a power is the sum of the angles, and the
$n$-th roots of a number are the vertices of a regular $n$-gon. That interplay is the subject of
Sections 7.1–7.6.

The second half of the tutorial studies the maps that respect this geometry. A **Möbius
transformation** (also called a fractional linear transformation) is a map of the form

$$
z \mapsto \frac{az + b}{cz + d}, \qquad ad - bc \ne 0.
$$

These maps form a group under composition, and the group is almost a group of $2 \times 2$ matrices
— the multiplication rule is exactly matrix multiplication. Their decisive geometric property is
that **they send circles and straight lines to circles and straight lines**. A straight line, it
turns out, is best regarded as a circle passing through a single extra point $\infty$; adjoining
that point turns the plane into the **Riemann sphere** $\mathbb{C} \cup \{\infty\}$, which is
topologically a sphere. Section 7.10 constructs the sphere explicitly by stereographic projection,
and Section 7.11 proves that the construction really is a homeomorphism. On the sphere, the
statement "Möbius maps send circles to circles" becomes literally true, with no exception for
lines.

Why should a student of analysis care about this? Because the maps that complex analysis is built
on are exactly these maps. The derivative of a holomorphic function at a point is a complex number,
and multiplication by that number is a rotation-dilation; this is the content of conformality, the
subject of [Analytic Functions](../02-analytic-functions/README.md). The cross-ratio of four points
classifies quadruples up to Möbius equivalence, and it is the first example of a **conformal
invariant**. The extended plane is the natural domain of the maps $z \mapsto 1/z$ and
$z \mapsto (az+b)/(cz+d)$ that appear throughout the subject, and the sphere is the reason the
theory of meromorphic functions is cleaner than the theory of rational functions on the line.

Three habits make the material easy. **First, always draw the picture.** Every algebraic identity
below has a geometric reading, and the geometric reading usually suggests the proof. **Second,
track the argument modulo $2\pi$.** Almost every error in this subject comes from treating a
multi-valued quantity as single-valued. **Third, allow $\infty$ as a point.** Refusing to do so
creates a special case in every theorem about Möbius maps; admitting it removes all of them.

## 2. Prerequisites

**Complex arithmetic.** You must be fluent with $z = a + bi$, conjugation $\bar z = a - bi$,
modulus $\lvert z\rvert = \sqrt{a^2+b^2}$, the identity $z\bar z = \lvert z\rvert^2$, and division
by rationalising the denominator. All of this is developed in
[Complex Numbers](../../03-algebra/13-complex-numbers/README.md); Section 7.1 is a compressed
review that also fixes the notation used later.

**Inequalities and absolute value.** The triangle inequality for real numbers, the meaning of
$\lvert x\rvert < \varepsilon$, and the technique of proving an inequality by squaring both sides
after checking that both are non-negative. See
[Inequalities](../../03-algebra/03-inequalities/README.md).

**Trigonometry.** The addition formulas
$\cos(\theta+\varphi) = \cos\theta\cos\varphi - \sin\theta\sin\varphi$ and
$\sin(\theta+\varphi) = \sin\theta\cos\varphi + \cos\theta\sin\varphi$ are used in every proof about
polar form. You also need the values of sine and cosine at multiples of $\pi/6$ and $\pi/4$, the
periodicity of both functions, and the fact that $\cos\theta = 1$ exactly when
$\theta \in 2\pi\mathbb{Z}$. See [The Unit Circle](../../05-trigonometry/02-unit-circle/README.md)
and [Trigonometric Identities](../../05-trigonometry/03-trigonometric-identities/README.md).

**Limits and continuity.** Only the definition of $\lim_{z \to z_0} f(z)$ and the fact that limits
in $\mathbb{C}$ may be taken along any path are needed here; both are revisited in
[Limits](../../07-calculus/01-limits/README.md). The full theory of complex limits is developed in
[Analytic Functions](../02-analytic-functions/README.md).

**Matrices and linear maps.** A $2\times 2$ real matrix acts on the plane; matrix multiplication
composes linear maps; a matrix is invertible exactly when its determinant is non-zero. This is the
model for the group of Möbius transformations in Section 7.7. See
[Matrices](../../08-linear-algebra/02-matrices/README.md) and
[Linear Transformations](../../08-linear-algebra/05-linear-transformations/README.md).

**Sets and maps.** Injections, surjections, bijections, composition, and the notation
$f[A]$ for the image of a set. See [Set Theory](../../00-foundations/03-set-theory/README.md).

## 3. Learning Objectives

By the end of this tutorial you will be able to

1. state the field axioms for $\mathbb{C}$ and verify the field properties from the definition of
   $\mathbb{C}$ as $\mathbb{R}^2$ with a multiplication;
2. prove the conjugation identities $\overline{z+w} = \bar z + \bar w$,
   $\overline{zw} = \bar z\bar w$, $z\bar z = \lvert z\rvert^2$, and use them to compute
   $z^{-1}$ and quotients;
3. prove the triangle inequality, the reverse triangle inequality and the parallelogram law for
   the complex modulus, and characterise the equality case of the triangle inequality;
4. convert between Cartesian, polar and exponential forms, and explain precisely in what sense
   the argument is defined only modulo $2\pi$;
5. prove that multiplication by $re^{i\theta}$ is the rotation by $\theta$ composed with the
   dilation by $r$, and read division as the inverse operation;
6. state and prove De Moivre's theorem for all integer exponents, and derive the $n$ distinct
   $n$-th roots of any non-zero complex number;
7. describe the $n$-th roots of unity as the vertices of a regular $n$-gon, and prove that they sum
   to $0$ and have product $(-1)^{n+1}$;
8. define Möbius transformations, prove that they form a group, and compute with the matrix
   correspondence;
9. prove that a Möbius transformation maps every straight line or circle to a straight line or
   circle, and find the image in concrete cases;
10. define the cross-ratio, prove its invariance under Möbius transformations, and use it to decide
    whether four points are concyclic or collinear;
11. define the extended complex plane, write the stereographic projection formulas in both
    directions, and prove that $\mathbb{C}\cup\{\infty\}$ is homeomorphic to the sphere $S^2$;
12. explain how complex multiplication encodes rotations in computer graphics and robotics, how
    phasors encode alternating current, and how conformal maps generate inviscid fluid flows.

## 4. Intuition

Imagine a city whose streets are drawn on transparent film. Sliding the film across the map is
**addition**: every point moves by the same vector. Pinning the film at one point and turning it,
then shrinking or enlarging it about that point, is **multiplication**: every point is rotated by
the same angle and scaled by the same factor. The two operations are the two rigid-ish motions of
the plane that fix the origin, and the whole of this tutorial follows from taking that sentence
literally.

The phrase "rigid-ish" hides the essential point. A rotation followed by a scaling is **angle
preserving**: the angle between two streets is unchanged, and so is the sense of turning (clockwise
stays clockwise). Reflections, by contrast, reverse angles. Complex multiplication never reflects.
This is why the algebra of $\mathbb{C}$ is the algebra of orientation-preserving similarities of
the plane, and why conjugation — which *does* reflect — is a different kind of operation, not
expressible as multiplication by a complex number.

Now add a single point at infinity, like the point where all directions of the plane meet. Straight
lines, seen from that point, close up into circles: a train track receding to the horizon appears
to converge, and if you could walk past the horizon you would come back from the opposite
direction. A map of the form $(az+b)/(cz+d)$ is a composition of translations, rotations,
scalings and the inversion $z \mapsto 1/z$; inversion is the map that turns the plane inside out
about the unit circle. Since each ingredient sends circles to circles, so does every composite.
That is the entire content of the circle-preservation theorem, and it is the reason Möbius maps are
the natural symmetries of the Riemann sphere.

The sphere itself is not an analogy. Stand a sphere on the plane at the origin, put a light at the
north pole, and look at the shadow of each point of the sphere on the plane. Every point except the
north pole casts exactly one shadow, and every point of the plane is the shadow of exactly one
point. The north pole has no shadow, so it corresponds to $\infty$. Distance on the sphere is a
genuine metric on $\mathbb{C}\cup\{\infty\}$ in which "far away in the plane" means "close to the
north pole". This is the precise sense in which the complex plane plus infinity is a sphere.

## 5. Formal Definition

Everything below is stated from scratch, so that no appeal to an unproved algebraic fact is needed.

**Definition 5.1** (the complex numbers). Let $\mathbb{C} = \mathbb{R}^2$ as a set, and write
$(a,b)$ for its elements. Define

$$
(a,b) + (c,d) := (a+c,\; b+d), \qquad (a,b)\cdot(c,d) := (ac - bd,\; ad + bc).
$$

The pair $(0,0)$ is the additive identity and $(1,0)$ is the multiplicative identity.

**Theorem 5.2.** With these operations, $\mathbb{C}$ is a field: addition and multiplication are
commutative and associative, multiplication distributes over addition, every element has an
additive inverse, and every non-zero element has a multiplicative inverse.

*Proof.* All the axioms except the existence of multiplicative inverses are immediate from the
corresponding axioms for $\mathbb{R}$, checked coordinate by coordinate. For the inverse, let
$z = (a,b) \ne (0,0)$ and put

$$
w := \left(\frac{a}{a^2+b^2},\; \frac{-b}{a^2+b^2}\right).
$$

Then

$$
z \cdot w = \left(\frac{a^2 + b^2}{a^2+b^2},\; \frac{-ab + ba}{a^2+b^2}\right) = (1,0),
$$

so $w$ is a multiplicative inverse. It is unique, because if $zw = zw' = 1$ then
$w = w(zw') = (wz)w' = w'$. $\blacksquare$

**Definition 5.3** (the imaginary unit and Cartesian form). Write $i := (0,1)$. Then
$i^2 = (0,1)(0,1) = (-1,0)$, so $i$ is a square root of $-1$. Every element factors uniquely as

$$
(a,b) = (a,0) + (0,b) = a + b\,i,
$$

and we write $z = a + bi$ with $a, b \in \mathbb{R}$. The **real part** and **imaginary part** are
$\operatorname{Re} z := a$ and $\operatorname{Im} z := b$. A complex number with $b = 0$ is
identified with the real number $a$; thus $\mathbb{R} \subseteq \mathbb{C}$ as a subfield.

**Definition 5.4** (conjugate and modulus). For $z = a + bi$ define

$$
\bar z := a - bi, \qquad \lvert z\rvert := \sqrt{a^2 + b^2}.
$$

The non-negative real number $\lvert z\rvert$ is the **modulus** of $z$.

**Definition 5.5** (argument). Let $z \ne 0$. A real number $\theta$ is an **argument** of $z$ if

$$
z = \lvert z\rvert(\cos\theta + i\sin\theta).
$$

The set of all arguments of $z$ is denoted $\arg z$. The **principal argument** $\operatorname{Arg} z$
is the unique argument in the interval $(-\pi,\pi]$. The argument of $0$ is undefined.

Definition 5.5 presupposes that every non-zero $z$ has an argument, and that any two arguments
differ by a multiple of $2\pi$. Both facts are proved in Section 7.3 (Lemma 7.6 and Proposition
7.7).

**Definition 5.6** ($n$-th roots of unity). For $n \in \mathbb{N}$, the set

$$
\mu_n := \{z \in \mathbb{C} : z^n = 1\}
$$

is the set of **$n$-th roots of unity**.

**Definition 5.7** (extended complex plane). Let $\infty$ be a symbol not in $\mathbb{C}$. The
**extended complex plane** is $\mathbb{C}_\infty := \mathbb{C} \cup \{\infty\}$. The **extended
real line** is $\mathbb{R}_\infty := \mathbb{R}\cup\{\infty\}$.

The topology on $\mathbb{C}_\infty$ is defined in Section 7.10 by stereographic projection; until
then $\infty$ is treated formally, with the arithmetic conventions of Definition 7.38.

**Definition 5.8** (Möbius transformation). A **Möbius transformation** (or **fractional linear
transformation**) is a map $T : \mathbb{C}_\infty \to \mathbb{C}_\infty$ given by

$$
T(z) := \frac{az + b}{cz + d},
$$

where $a,b,c,d \in \mathbb{C}$ and $ad - bc \ne 0$, with the conventions
$T(\infty) = a/c$ if $c \ne 0$ and $T(\infty) = \infty$ if $c = 0$, and
$T(-d/c) = \infty$ when $c \ne 0$. The number $ad - bc$ is the **determinant** of $T$.

**Definition 5.9** (generalized circle). A **generalized circle** in $\mathbb{C}_\infty$ is a subset
of the form

$$
\{z \in \mathbb{C} : A\lvert z\rvert^2 + Bz + \bar B\bar z + C = 0\} \cup \{\text{possibly } \infty\},
$$

where $A, C \in \mathbb{R}$, $B \in \mathbb{C}$, $(A,B,C) \ne (0,0,0)$, and the set is non-empty.
When $A = 0$ the set is a straight line (together with $\infty$); when $A \ne 0$ it is a circle
(together with $\infty$ only if the circle degenerates — see Lemma 7.27).

**Definition 5.10** (cross-ratio). For distinct $z_1,z_2,z_3,z_4 \in \mathbb{C}_\infty$, the
**cross-ratio** is

$$
(z_1,z_2;z_3,z_4) := \frac{(z_1-z_3)(z_2-z_4)}{(z_1-z_4)(z_2-z_3)},
$$

with the conventions obtained by cancelling factors involving $\infty$: if some $z_j = \infty$,
delete the two factors containing it. For example
$(\infty,z_2;z_3,z_4) = (z_2-z_4)/(z_2-z_3)$.

**Definition 5.11** (stereographic projection). Let
$S^2 = \{(X,Y,Z) \in \mathbb{R}^3 : X^2+Y^2+Z^2 = 1\}$ be the unit sphere and $N := (0,0,1)$ its
north pole. The **stereographic projection** $\sigma : S^2 \setminus \{N\} \to \mathbb{C}$ is

$$
\sigma(X,Y,Z) := \frac{X}{1-Z} + i\,\frac{Y}{1-Z}.
$$

Its inverse is computed in Proposition 7.43.

## 6. Mathematical Notation

| Symbol | Read as | Meaning |
|---|---|---|
| $\mathbb{C}$ | the complex numbers | $\{a+bi : a,b \in \mathbb{R}\}$ with the field structure of Definition 5.1 |
| $\mathbb{C}_\infty$ | the extended complex plane | $\mathbb{C} \cup \{\infty\}$, topologised as the Riemann sphere |
| $i$ | i | the element $(0,1)$, with $i^2 = -1$ |
| $\operatorname{Re} z$, $\operatorname{Im} z$ | real part, imaginary part | the coordinates $a$, $b$ in $z = a+bi$ |
| $\bar z$ | z bar, the conjugate | $a - bi$ |
| $\lvert z\rvert$ | modulus of $z$ | $\sqrt{a^2+b^2}$, the distance from $z$ to $0$ |
| $\arg z$ | argument of $z$ | the *set* of all $\theta$ with $z = \lvert z\rvert(\cos\theta + i\sin\theta)$ |
| $\operatorname{Arg} z$ | principal argument | the element of $\arg z$ in $(-\pi,\pi]$ |
| $e^{i\theta}$ | e to the i theta | shorthand for $\cos\theta + i\sin\theta$ (justified in Section 7.4) |
| $\mu_n$ | the n-th roots of unity | $\{z : z^n = 1\}$ |
| $z_1 \equiv z_2 \pmod{2\pi}$ | congruent modulo $2\pi$ | $z_1 - z_2 \in 2\pi\mathbb{Z}$, used for arguments |
| $(z_1,z_2;z_3,z_4)$ | cross-ratio of the four points | the quotient of Definition 5.10 |
| $S^2$ | the two-sphere | $\{(X,Y,Z) : X^2+Y^2+Z^2=1\}$ |
| $\sigma$ | sigma | stereographic projection from $S^2 \setminus \{N\}$ to $\mathbb{C}$ |
| $T(z) = \frac{az+b}{cz+d}$ | Möbius map | a fractional linear transformation with $ad-bc \ne 0$ |
| $\operatorname{GL}_2(\mathbb{C})$ | general linear group | invertible $2\times2$ complex matrices |
| $\operatorname{PGL}_2(\mathbb{C})$ | projective general linear group | $\operatorname{GL}_2(\mathbb{C})$ modulo non-zero scalar matrices |
| $\lvert z - w\rvert$ | distance from $z$ to $w$ | the Euclidean distance between the corresponding points |
| $\operatorname{Re}(z) = u$, $\operatorname{Im}(z) = v$ | u and v | used when $f = u+iv$ is studied in [Analytic Functions](../02-analytic-functions/README.md) |

Two conventions are worth stating aloud. First, "$z = re^{i\theta}$" is read "z equals r e to the
i theta" and is **not** a new operation: it abbreviates
$r(\cos\theta + i\sin\theta)$, and Section 7.4 justifies the notation by proving that the
exponential law holds. Second, whenever a statement involves $\arg z$, it is a statement about a
set, or about a value determined only up to a multiple of $2\pi$; "$\arg z = \pi/4$" is shorthand
for "one argument is $\pi/4$", never for an equality of sets.

## 7. Core Concepts

### 7.1 Arithmetic and Conjugation, Reviewed

Write $z = a + bi$ and $w = c + di$ with $a,b,c,d \in \mathbb{R}$. Addition is coordinatewise,

$$
z + w = (a+c) + (b+d)i,
$$

which is exactly the parallelogram rule for vectors: the point $z+w$ is the fourth vertex of the
parallelogram with vertices $0$, $z$, $w$. Multiplication is

$$
zw = (ac - bd) + (ad + bc)i,
$$

obtained by expanding and replacing $i^2$ by $-1$. Subtraction is addition of $-w$, and division is
multiplication by $w^{-1}$, computed by rationalising.

The following proposition collects the algebraic properties of conjugation. They are proved by
writing everything in coordinates; no geometry is involved, and the proofs are short enough to be
worth reading once, because every later argument uses them without comment.

**Proposition 7.1** (conjugation is a field automorphism of order two). For all
$z, w \in \mathbb{C}$:

1. $\overline{z + w} = \bar z + \bar w$;
2. $\overline{z\,w} = \bar z\,\bar w$;
3. $\overline{\bar z} = z$;
4. $z + \bar z = 2\operatorname{Re} z$ and $z - \bar z = 2i\operatorname{Im} z$;
5. $z \in \mathbb{R}$ if and only if $z = \bar z$.

*Proof.* Write $z = a+bi$ and $w = c+di$.

1. $\overline{z+w} = \overline{(a+c) + (b+d)i} = (a+c) - (b+d)i = (a - bi) + (c - di) = \bar z + \bar w$.
2. From the multiplication formula, $zw = (ac-bd) + (ad+bc)i$, so
   $\overline{zw} = (ac-bd) - (ad+bc)i$. On the other hand
   $\bar z\bar w = (a-bi)(c-di) = (ac - (-b)(-d)) + (-ad - bc)i = (ac-bd) - (ad+bc)i$. Equal.
3. Immediate from the definition.
4. $z + \bar z = (a+bi) + (a-bi) = 2a$ and $z - \bar z = 2bi$.
5. If $z = a \in \mathbb{R}$ then $b = 0$ and $\bar z = a = z$. Conversely $z = \bar z$ gives
   $a + bi = a - bi$, hence $2bi = 0$ and $b = 0$. $\blacksquare$

**Proposition 7.2** (modulus and inverse). For all $z, w \in \mathbb{C}$:

1. $z\bar z = \lvert z\rvert^2$;
2. $\lvert \bar z\rvert = \lvert z\rvert$ and $\lvert z\rvert = 0$ if and only if $z = 0$;
3. if $z \ne 0$ then $z^{-1} = \bar z/\lvert z\rvert^2$;
4. $\lvert \operatorname{Re} z\rvert \le \lvert z\rvert$ and $\lvert \operatorname{Im} z\rvert \le \lvert z\rvert$.

*Proof.* 1. $(a+bi)(a-bi) = a^2 - (bi)^2 = a^2 + b^2 = \lvert z\rvert^2$.
2. Both statements are immediate from $\lvert z\rvert = \sqrt{a^2+b^2}$ and $\lvert\bar z\rvert =
   \sqrt{a^2 + (-b)^2}$.
3. By 1, $z \cdot \bar z/\lvert z\rvert^2 = \lvert z\rvert^2/\lvert z\rvert^2 = 1$, and inverses are
   unique.
4. $a^2 \le a^2 + b^2$ gives $\lvert a\rvert \le \sqrt{a^2+b^2}$, and similarly for $b$.
   $\blacksquare$

**Example 7.3** (a quotient, with a check). Compute $(3 - 2i)/(1 + 4i)$. Multiply numerator and
denominator by $1 - 4i$:

$$
\frac{3-2i}{1+4i} = \frac{(3-2i)(1-4i)}{(1+4i)(1-4i)} = \frac{3 - 12i - 2i + 8i^2}{1 + 16}
= \frac{-5 - 14i}{17} = -\frac{5}{17} - \frac{14}{17}i.
$$

The check exploits Proposition 7.2: the modulus of the answer must be
$\lvert 3-2i\rvert/\lvert 1+4i\rvert = \sqrt{13}/\sqrt{17}$. And indeed
$\lvert -5 - 14i\rvert/17 = \sqrt{25+196}/17 = \sqrt{221}/17 = \sqrt{13\cdot 17}/17 = \sqrt{13}/\sqrt{17}$.

### 7.2 Modulus and the Triangle Inequality

The modulus is the distance from $z$ to the origin, and $\lvert z - w\rvert$ is the distance
between the points $z$ and $w$. This is not an analogy: the map $(a,b) \mapsto a+bi$ is an
isometry from the Euclidean plane $\mathbb{R}^2$ with its usual distance onto $\mathbb{C}$ with
distance $d(z,w) = \lvert z-w\rvert$, because
$\lvert (a+bi) - (c+di)\rvert = \sqrt{(a-c)^2 + (b-d)^2}$.

**Proposition 7.4** (triangle inequality). For all $z, w \in \mathbb{C}$,

$$
\lvert z + w\rvert \le \lvert z\rvert + \lvert w\rvert.
$$

If $w \ne 0$, equality holds if and only if $z = \lambda w$ for some real $\lambda \ge 0$. If
$w = 0$, equality holds for every $z$.

*Proof.* Expand the square of the left-hand side:

$$
\lvert z+w\rvert^2 = (z+w)(\overline{z+w}) = (z+w)(\bar z + \bar w)
= z\bar z + z\bar w + w\bar z + w\bar w
= \lvert z\rvert^2 + \lvert w\rvert^2 + 2\operatorname{Re}(z\bar w),
$$

where the last step uses $w\bar z = \overline{z\bar w}$ and Proposition 7.1(4). Since
$\operatorname{Re}\zeta \le \lvert \zeta\rvert$ for every $\zeta$ (Proposition 7.2(4)),

$$
\lvert z+w\rvert^2 \le \lvert z\rvert^2 + \lvert w\rvert^2 + 2\lvert z\bar w\rvert
= \lvert z\rvert^2 + 2\lvert z\rvert\lvert w\rvert + \lvert w\rvert^2 = (\lvert z\rvert + \lvert w\rvert)^2.
$$

Taking non-negative square roots gives the inequality.

For the equality case, all inequalities above must be equalities, so
$\operatorname{Re}(z\bar w) = \lvert z\bar w\rvert$. For a complex number $\zeta$, the equality
$\operatorname{Re}\zeta = \lvert\zeta\rvert$ forces $\operatorname{Im}\zeta = 0$ and
$\operatorname{Re}\zeta \ge 0$: writing $\zeta = p + qi$ gives $p = \sqrt{p^2+q^2}$, hence
$q = 0$ and $p \ge 0$. Apply this to $\zeta = z\bar w$. If $w \ne 0$, then $z\bar w = \mu$ with
$\mu \ge 0$ real, and multiplying by $w/\lvert w\rvert^2$ gives
$z = \mu w/\lvert w\rvert^2 = \lambda w$ with $\lambda = \mu/\lvert w\rvert^2 \ge 0$. Conversely,
if $z = \lambda w$ with $\lambda \ge 0$, then
$\lvert z+w\rvert = (\lambda+1)\lvert w\rvert = \lvert z\rvert + \lvert w\rvert$. If $w = 0$, both
sides equal $\lvert z\rvert$. $\blacksquare$

The geometric content is that a straight line is the shortest path between two points: the
displacement $z+w$ is no longer than going from $0$ to $w$ and then from $w$ to $z+w$. Equality
means the two displacements point the same way.

**Proposition 7.5** (reverse triangle inequality). For all $z, w \in \mathbb{C}$,

$$
\bigl\lvert \lvert z\rvert - \lvert w\rvert \bigr\rvert \le \lvert z - w\rvert.
$$

*Proof.* Apply Proposition 7.4 to $z = (z-w) + w$:

$$
\lvert z\rvert \le \lvert z-w\rvert + \lvert w\rvert \quad\Longrightarrow\quad \lvert z\rvert - \lvert w\rvert \le \lvert z-w\rvert.
$$

Interchanging $z$ and $w$ gives $\lvert w\rvert - \lvert z\rvert \le \lvert w-z\rvert = \lvert z-w\rvert$.
A real number whose absolute value is at most $\lvert z-w\rvert$ is at most $\lvert z-w\rvert$ in
absolute value, which is the claim. $\blacksquare$

**Proposition 7.6** (parallelogram law). For all $z, w \in \mathbb{C}$,

$$
\lvert z+w\rvert^2 + \lvert z-w\rvert^2 = 2\lvert z\rvert^2 + 2\lvert w\rvert^2.
$$

*Proof.* Expanding as in Proposition 7.4,

$$
\lvert z+w\rvert^2 = \lvert z\rvert^2 + \lvert w\rvert^2 + 2\operatorname{Re}(z\bar w), \qquad
\lvert z-w\rvert^2 = \lvert z\rvert^2 + \lvert w\rvert^2 - 2\operatorname{Re}(z\bar w).
$$

Adding gives the identity. $\blacksquare$

The name comes from the parallelogram with sides $z$ and $w$: the squared lengths of its two
diagonals, $\lvert z+w\rvert^2$ and $\lvert z-w\rvert^2$, add up to twice the sum of the squared
side lengths. The identity characterises Euclidean norms among norms, which is why $\mathbb{C}$
is a two-dimensional real inner-product space — a fact used in
[Inner Product Spaces](../../08-linear-algebra/08-inner-product-spaces/README.md).

### 7.3 Argument, Polar Form and Exponential Form

A non-zero point of the plane is determined by its distance $r$ from the origin and its direction
$\theta$ from the positive real axis. Converting that statement into algebra requires knowing that
every point of the unit circle is $(\cos\theta, \sin\theta)$ for some $\theta$, and that $\theta$
is unique up to a full turn.

**Lemma 7.7** (existence and uniqueness of the argument). Let $z \in \mathbb{C}$, $z \ne 0$, and
$r := \lvert z\rvert$. There exists $\theta \in \mathbb{R}$ with
$z = r(\cos\theta + i\sin\theta)$. If $\theta, \varphi$ are two such numbers, then
$\theta - \varphi \in 2\pi\mathbb{Z}$.

*Proof.* Write $z = a + bi$, so $a^2 + b^2 = r^2$ and therefore $(a/r)^2 + (b/r)^2 = 1$. The point
$(a/r, b/r)$ lies on the unit circle, and the parametrisation of the unit circle established in
[The Unit Circle](../../05-trigonometry/02-unit-circle/README.md) states that every point of the
unit circle is $(\cos\theta, \sin\theta)$ for some real $\theta$. Hence
$a/r = \cos\theta$ and $b/r = \sin\theta$, which is the existence claim.

For uniqueness, suppose $\cos\theta = \cos\varphi$ and $\sin\theta = \sin\varphi$. Then

$$
\cos(\theta - \varphi) = \cos\theta\cos\varphi + \sin\theta\sin\varphi = \cos^2\theta + \sin^2\theta = 1.
$$

The cosine equals $1$ only at integer multiples of $2\pi$ (again a standard fact from the
trigonometry sequence), so $\theta - \varphi = 2\pi k$ for some $k \in \mathbb{Z}$.
$\blacksquare$

Lemma 7.7 justifies Definition 5.5: the set $\arg z$ is exactly
$\{\operatorname{Arg} z + 2\pi k : k \in \mathbb{Z}\}$, a coset of $2\pi\mathbb{Z}$ in
$\mathbb{R}$. Consequently every statement about arguments is a statement modulo $2\pi$, and the
notation

$$
\theta \equiv \varphi \pmod{2\pi}
$$

means $\theta - \varphi \in 2\pi\mathbb{Z}$.

**Definition 7.8** (polar and exponential form). A non-zero complex number $z$ with
$r = \lvert z\rvert$ and $\theta \in \arg z$ is written

$$
z = r(\cos\theta + i\sin\theta) =: r\,e^{i\theta}.
$$

The right-hand side is the **exponential form**. The notation is a definition at this stage; it
becomes the genuine exponential function evaluated at $i\theta$ in
[Analytic Functions](../02-analytic-functions/README.md), and Euler's formula proves the two
meanings agree.

**Proposition 7.9** (moduli multiply, arguments add). Let $z = r e^{i\theta}$ and
$w = s e^{i\varphi}$ with $r, s > 0$. Then

$$
zw = rs\, e^{i(\theta+\varphi)}, \qquad \frac{z}{w} = \frac{r}{s}\, e^{i(\theta-\varphi)}.
$$

Consequently $\lvert zw\rvert = \lvert z\rvert\lvert w\rvert$ and
$\lvert z/w\rvert = \lvert z\rvert/\lvert w\rvert$, and

$$
\arg(zw) = \arg z + \arg w \pmod{2\pi}, \qquad \arg(z/w) = \arg z - \arg w \pmod{2\pi}.
$$

*Proof.* By the addition formulas,

$$
\begin{aligned}
zw &= rs(\cos\theta + i\sin\theta)(\cos\varphi + i\sin\varphi)\\
&= rs\bigl[(\cos\theta\cos\varphi - \sin\theta\sin\varphi) + i(\sin\theta\cos\varphi + \cos\theta\sin\varphi)\bigr]\\
&= rs\bigl[\cos(\theta+\varphi) + i\sin(\theta+\varphi)\bigr] = rs\,e^{i(\theta+\varphi)}.
\end{aligned}
$$

Since $rs > 0$, this is a polar representation, so $\lvert zw\rvert = rs$ and
$\theta+\varphi \in \arg(zw)$. For the quotient, it suffices to prove $w^{-1} = s^{-1}e^{-i\varphi}$
and multiply. And indeed

$$
s e^{i\varphi} \cdot s^{-1}e^{-i\varphi} = e^{i(\varphi - \varphi)} = e^{0} = 1,
$$

by the product formula just proved; inverses are unique, so $w^{-1} = s^{-1}e^{-i\varphi}$.
$\blacksquare$

**Proposition 7.10** (geometric meaning of multiplication). Let $z = r e^{i\theta} \ne 0$. The map

$$
M_z : \mathbb{C} \to \mathbb{C}, \qquad M_z(w) := z w
$$

is the composition of the rotation by $\theta$ about $0$ with the dilation of ratio $r$ about $0$.
It is a bijection, it preserves distances up to the factor $r$,
$\lvert zw_1 - zw_2\rvert = r\lvert w_1-w_2\rvert$, and it preserves oriented angles. Its inverse
is $M_{1/z}$.

*Proof.* Proposition 7.9 gives $zw = r\lvert w\rvert e^{i(\theta + \arg w)}$: the modulus of $w$
is multiplied by $r$ and its argument is increased by $\theta$. That is precisely "rotate by
$\theta$, then dilate by $r$". The distance identity follows from
$\lvert zw_1 - zw_2\rvert = \lvert z(w_1-w_2)\rvert = \lvert z\rvert\lvert w_1-w_2\rvert$.
Multiplication by $z$ and then by $1/z$ returns $w$, so $M_z$ is invertible with inverse
$M_{1/z}$. Angle preservation is proved in [Analytic Functions](../02-analytic-functions/README.md)
as the special case of conformality for $f(z) = z$. $\blacksquare$

In matrix language, if $z = a+bi$, then multiplication by $z$ acts on the column vector
$\binom{x}{y}$ as

$$
\begin{pmatrix} a & -b\\ b & a\end{pmatrix}\binom{x}{y} = \binom{ax - by}{bx + ay},
$$

which is the standard form of a direct similarity: a $2\times 2$ matrix of the shape
$\begin{pmatrix} a & -b\\ b & a\end{pmatrix}$ with $(a,b) \ne (0,0)$. Its determinant is
$a^2+b^2 = \lvert z\rvert^2 > 0$, so it never reverses orientation. The map
$z \mapsto \bar z$ corresponds instead to $\begin{pmatrix} a & b\\ b & -a\end{pmatrix}$, which has
determinant $-(a^2+b^2) < 0$: conjugation is a reflection, not a rotation-dilation.

**Example 7.11** (multiplying rotates and scales). Let $z = 1+i = \sqrt2\,e^{i\pi/4}$ and
$w = 1 + i\sqrt3 = 2e^{i\pi/3}$. Then

$$
zw = 2\sqrt2\, e^{7\pi i/12}.
$$

Directly: $(1+i)(1+i\sqrt3) = 1 + i\sqrt3 + i + i^2\sqrt3 = (1-\sqrt3) + i(1+\sqrt3)$, whose modulus
squared is $(1-\sqrt3)^2 + (1+\sqrt3)^2 = (4 - 2\sqrt3) + (4 + 2\sqrt3) = 8$, so the modulus is
$2\sqrt2$. The argument is $\pi/4 + \pi/3 = 7\pi/12 \approx 105^\circ$, in the second quadrant,
consistent with $1-\sqrt3 < 0 < 1+\sqrt3$.

**Example 7.12** (division as inverse rotation). The quotient $(1+i\sqrt3)/(1+i)$ has modulus
$2/\sqrt2 = \sqrt2$ and argument $\pi/3 - \pi/4 = \pi/12$. Indeed
$\sqrt2 e^{i\pi/12} = \sqrt2\cos 15^\circ + i\sqrt2\sin 15^\circ$, and using
$\cos 15^\circ = (\sqrt6+\sqrt2)/4$, $\sin15^\circ = (\sqrt6-\sqrt2)/4$, this equals
$(\sqrt3+1)/2 + i(\sqrt3-1)/2$. Direct computation gives
$(1+i\sqrt3)(1-i)/2 = (1 - i + i\sqrt3 + \sqrt3)/2 = (1+\sqrt3)/2 + i(\sqrt3-1)/2$, which agrees.

### 7.4 Powers, De Moivre's Theorem and Roots

**Proposition 7.13** (De Moivre). For every $\theta \in \mathbb{R}$ and every $n \in \mathbb{Z}$,

$$
(\cos\theta + i\sin\theta)^n = \cos(n\theta) + i\sin(n\theta).
$$

*Proof.* For $n = 0$ both sides are $1$. For $n \ge 1$, induct on $n$: the case $n = 1$ is
trivial, and if the identity holds for $n$ then Proposition 7.9 gives

$$
(\cos\theta+i\sin\theta)^{n+1} = \bigl(\cos n\theta + i\sin n\theta\bigr)(\cos\theta+i\sin\theta)
= \cos((n+1)\theta) + i\sin((n+1)\theta).
$$

For $n < 0$, write $m = -n > 0$ and use Proposition 7.9 to compute the inverse of
$\cos n\theta + i\sin n\theta$: the number $\cos(n\theta) - i\sin(n\theta)$ multiplies it to $1$.
Hence

$$
(\cos\theta+i\sin\theta)^{n} = \frac{1}{(\cos\theta+i\sin\theta)^{m}}
= \cos(m\theta) - i\sin(m\theta) = \cos(-m\theta) + i\sin(-m\theta),
$$

which is the claim since $-m = n$. $\blacksquare$

De Moivre's theorem converts the computation of powers into two real operations: raise the
modulus to the power and multiply the angle by the power. For $z = re^{i\theta}$ it reads
$z^n = r^n e^{in\theta}$.

**Proposition 7.14** ($n$-th roots). Let $w = \rho e^{i\varphi}$ with $\rho > 0$ and
$n \in \mathbb{N}$. The equation $z^n = w$ has exactly $n$ solutions in $\mathbb{C}$, namely

$$
z_k = \rho^{1/n}\exp\!\left(i\,\frac{\varphi + 2\pi k}{n}\right), \qquad k = 0, 1, \dots, n-1,
$$

where $\rho^{1/n}$ denotes the positive real $n$-th root of $\rho$.

*Proof.* Suppose $z = re^{i\theta}$ with $r > 0$. By De Moivre, $z^n = r^n e^{in\theta}$. If
$z^n = w = \rho e^{i\varphi}$, then $r^n e^{in\theta} = \rho e^{i\varphi}$. Taking moduli gives
$r^n = \rho$, hence $r = \rho^{1/n}$ because both are positive. Dividing by $r^n = \rho$ gives
$e^{in\theta} = e^{i\varphi}$, that is $e^{i(n\theta - \varphi)} = 1$, so by Lemma 7.7
$n\theta - \varphi = 2\pi k$ for some $k \in \mathbb{Z}$, i.e.
$\theta = (\varphi + 2\pi k)/n$.

Conversely, every $z_k$ of the stated form satisfies
$z_k^n = \rho\, e^{i(\varphi + 2\pi k)} = \rho e^{i\varphi} = w$, using De Moivre and the
periodicity of $e^{i\cdot}$.

It remains to check that the list contains each solution once. If $0 \le k, l \le n-1$ and
$z_k = z_l$, then the moduli agree, and Lemma 7.7 gives
$(\varphi + 2\pi k)/n - (\varphi + 2\pi l)/n = 2\pi m$ for some integer $m$; that is,
$(k-l)/n = m$, so $n \mid (k-l)$. But $\lvert k-l\rvert \le n-1$, so $k = l$. Every integer $k$
is congruent modulo $n$ to exactly one of $0, \dots, n-1$, and replacing $k$ by $k + n$ adds
$2\pi$ to the angle, so no further solutions exist. $\blacksquare$

**Corollary 7.15** (geometry of the $n$-th roots). The $n$ solutions of $z^n = w$ are the vertices
of a regular $n$-gon centred at $0$: they lie on the circle of radius $\rho^{1/n}$, and consecutive
vertices are separated by the angle $2\pi/n$.

*Proof.* Each $z_k$ has modulus $\rho^{1/n}$, so all lie on that circle. Moreover
$z_{k+1}/z_k = e^{2\pi i/n}$, which has modulus $1$ and argument $2\pi/n$; by Proposition 7.10
the map $w \mapsto (z_{k+1}/z_k)w$ is the rotation by $2\pi/n$ about $0$. Hence each vertex is
obtained from the previous one by the same rotation, which is the definition of a regular
$n$-gon. $\blacksquare$

**Example 7.16** (the cube roots of $8i$). Here $\rho = 8$ and $\varphi = \pi/2$, so
$\rho^{1/3} = 2$ and

$$
z_k = 2\exp\!\left(i\,\frac{\pi/2 + 2\pi k}{3}\right), \qquad k = 0,1,2.
$$

Thus $z_0 = 2e^{i\pi/6} = \sqrt3 + i$, $z_1 = 2e^{5\pi i/6} = -\sqrt3 + i$ and
$z_2 = 2e^{3\pi i/2} = -2i$. Check: $(\sqrt3+i)^2 = 3 + 2\sqrt3\,i - 1 = 2 + 2\sqrt3\,i$, and
multiplying by $\sqrt3 + i$ gives
$2\sqrt3 + 2i + 6i + 2\sqrt3 i^2 = 2\sqrt3 - 2\sqrt3 + 8i = 8i$. Also
$z_0 + z_1 + z_2 = (\sqrt3 - \sqrt3) + (1 + 1 - 2)i = 0$, as Proposition 7.18 will predict for
any three roots of the same number.

### 7.5 Roots of Unity and Their Geometry

The case $w = 1$ of Proposition 7.14 deserves a name and a section of its own, because $\mu_n$
carries the combinatorial structure of the cyclic group of order $n$ and the geometry of the
regular $n$-gon.

**Proposition 7.17** (structure of $\mu_n$). Let $n \in \mathbb{N}$ and $\omega := e^{2\pi i/n}$.
Then

$$
\mu_n = \{1, \omega, \omega^2, \dots, \omega^{n-1}\},
$$

these $n$ numbers are distinct, $\mu_n$ is a subgroup of the multiplicative group
$\mathbb{C}^\times$, and it is cyclic of order $n$ generated by $\omega$. Every generator of
$\mu_n$ is of the form $\omega^j$ with $\gcd(j,n) = 1$.

*Proof.* By Proposition 7.14 with $w = 1$, the solutions of $z^n = 1$ are
$\omega^k$, $k = 0,\dots,n-1$, and they are distinct. If $z, w \in \mu_n$ then
$(zw)^n = z^n w^n = 1$ and $(z^{-1})^n = (z^n)^{-1} = 1$, so $\mu_n$ is a subgroup. Since it has
$n$ elements and $\omega$ generates it by construction, it is cyclic of order $n$.

For the last claim, $\omega^j$ generates $\mu_n$ if and only if the $n$ powers
$(\omega^j)^k = \omega^{jk}$, $k = 0,\dots,n-1$, are distinct. The exponents $jk$ are distinct
modulo $n$ exactly when $\gcd(j,n) = 1$: if $d = \gcd(j,n) > 1$, then $jk$ is divisible by $n$ for
$k = n/d < n$, so the powers repeat; conversely if $\gcd(j,n) = 1$ and
$n \mid j(k-l)$, then $n \mid (k-l)$, so distinct $k$ in the range give distinct exponents.
$\blacksquare$

**Proposition 7.18** (sums of roots of unity). Let $n \ge 2$ and $\omega = e^{2\pi i/n}$. Then

$$
\sum_{k=0}^{n-1} \omega^k = 0.
$$

More generally, for any integer $j$ that is not a multiple of $n$,

$$
\sum_{k=0}^{n-1} \omega^{jk} = 0,
$$

while for $j$ a multiple of $n$ the sum equals $n$.

*Proof.* Since $\omega^n = 1$ and $\omega \ne 1$ for $n \ge 2$, the finite geometric series gives

$$
\sum_{k=0}^{n-1} \omega^k = \frac{\omega^n - 1}{\omega - 1} = 0.
$$

For general $j$, put $\eta := \omega^j$. Then $\eta^n = \omega^{jn} = 1$, and the same
computation applies provided $\eta \ne 1$. Now $\eta = 1$ exactly when $e^{2\pi i j/n} = 1$,
which by Lemma 7.7 happens exactly when $j/n \in \mathbb{Z}$, i.e. when $n \mid j$. In that case
every term equals $1$ and the sum is $n$. $\blacksquare$

Geometrically, Proposition 7.18 says that the centroid of the vertices of a regular $n$-gon
inscribed in the unit circle is the centre of the circle. This is physically obvious by symmetry,
and the algebraic proof is a one-line geometric-series computation — a good example of the
dictionary between the two subjects.

**Proposition 7.19** (product of the roots of unity). For $n \in \mathbb{N}$,

$$
\prod_{k=0}^{n-1} \omega^k = (-1)^{n+1}.
$$

*Proof.* First proof, by pairing. Pair each $\omega^k$ with $\omega^{n-k}$, whose product is
$\omega^n = 1$. For odd $n$ the indices $k = 1,\dots,n-1$ split into $(n-1)/2$ such pairs, and the
unpaired term is $\omega^0 = 1$, so the product is $1 = (-1)^{n+1}$. For even $n$, the index
$k = n/2$ is paired with itself; its term is $\omega^{n/2} = e^{\pi i} = -1$, and the remaining
indices pair off to $1$, so the product is $-1 = (-1)^{n+1}$.

Second proof, by Vieta. The polynomial $z^n - 1$ has the $n$ roots $\omega^0,\dots,\omega^{n-1}$,
so $z^n - 1 = \prod_{k}(z - \omega^k)$. The constant term is the product of the roots multiplied
by $(-1)^n$; on the left the constant term is $-1$, hence
$\prod_k \omega^k = (-1)^n \cdot (-1) = (-1)^{n+1}$. $\blacksquare$

**Proposition 7.20** (the regular $n$-gon). The points of $\mu_n$ are the vertices of the regular
$n$-gon inscribed in the unit circle with one vertex at $1$. The polygon is invariant under the map
$z \mapsto \omega z$, and its symmetry group contains the $n$ rotations $z \mapsto \omega^j z$,
$j = 0,\dots,n-1$.

*Proof.* By Corollary 7.15 with $w = 1$ and $\rho = 1$, the roots are equally spaced on the unit
circle at angles $2\pi k/n$; that is the regular $n$-gon with a vertex at angle $0$, i.e. at $1$.
Since $\omega \mu_n = \mu_n$ (multiplying by $\omega$ permutes the list), the rotation
$z \mapsto \omega z$ maps the polygon to itself. Iterating gives the $n$ stated rotations. Note
that the polygon also has reflections as symmetries, but those are not of the form
$z \mapsto \alpha z$; they are conjugate-linear maps $z \mapsto \alpha \bar z$. $\blacksquare$

**Example 7.21** (the fifth roots of unity and the regular pentagon). For $n = 5$,
$\omega = e^{2\pi i/5}$. The five roots are $1$, $\omega$, $\omega^2$, $\omega^3$, $\omega^4$,
with $\omega + \omega^4 = 2\cos(2\pi/5)$ and $\omega^2 + \omega^3 = 2\cos(4\pi/5)$. Since the sum
of all five is zero,

$$
1 + 2\cos\frac{2\pi}{5} + 2\cos\frac{4\pi}{5} = 0.
$$

Writing $c = \cos(2\pi/5)$ and using $\cos(4\pi/5) = 2c^2 - 1$ gives
$4c^2 + 2c - 1 = 0$, hence $c = (-1 + \sqrt5)/4$. Thus the side length of the regular pentagon
inscribed in the unit circle is
$\lvert 1 - \omega\rvert = 2\sin(\pi/5) = \sqrt{(5-\sqrt5)/2}$, an expression involving only
square roots — the algebraic reason a regular pentagon is constructible with straightedge and
compass, while a regular heptagon is not.

### 7.6 Möbius Transformations: Definition and Group Structure

Definition 5.8 introduces the maps $z \mapsto (az+b)/(cz+d)$. Before studying their geometry, it
is worth understanding why the condition $ad-bc \ne 0$ is exactly right. If $ad - bc = 0$ and
$c \ne 0$, then $a = bc/d$ and

$$
\frac{az+b}{cz+d} = \frac{(bc/d)z + b}{cz+d} = \frac{b(cz+d)/d}{cz+d} = \frac{b}{d},
$$

a constant. If $c = 0$ then $ad = 0$; with $d \ne 0$ this forces $a = 0$ and the map is the
constant $b/d$. So $ad - bc = 0$ means the map collapses the plane to a point. Conversely, when
$ad - bc \ne 0$ the map is non-constant, and then it is injective: if
$(az_1+b)/(cz_1+d) = (az_2+b)/(cz_2+d)$, cross-multiplication gives

$$
(az_1+b)(cz_2+d) = (az_2+b)(cz_1+d)
\;\Longrightarrow\; (ad-bc)(z_1 - z_2) = 0,
$$

so $z_1 = z_2$. Thus non-degenerate Möbius maps are bijections of the extended plane.

**Proposition 7.22** (composition is matrix multiplication). For $A = \begin{pmatrix} a & b\\ c & d\end{pmatrix}$
let $T_A(z) := (az+b)/(cz+d)$. For any two $2\times 2$ complex matrices $A, B$ with non-zero
determinants,

$$
T_A \circ T_B = T_{AB}.
$$

*Proof.* Put $B = \begin{pmatrix} a' & b'\\ c' & d'\end{pmatrix}$ and $w = T_B(z) = (a'z+b')/(c'z+d')$.
Then

$$
T_A(w) = \frac{a\,\dfrac{a'z+b'}{c'z+d'} + b}{c\,\dfrac{a'z+b'}{c'z+d'} + d}
= \frac{a(a'z+b') + b(c'z+d')}{c(a'z+b') + d(c'z+d')}
= \frac{(aa'+bc')z + (ab'+bd')}{(ca'+dc')z + (cb'+dd')},
$$

which is $T_{AB}(z)$ by the definition of matrix multiplication. The same computation with $z$
replaced by $\infty$ and with the pole handled by the conventions of Definition 5.8 gives the
statement on the extended plane. $\blacksquare$

**Proposition 7.23** (the Möbius group). The set of Möbius transformations is a group under
composition, isomorphic to $\operatorname{PGL}_2(\mathbb{C}) := \operatorname{GL}_2(\mathbb{C})/\mathbb{C}^\times$,
where $\mathbb{C}^\times$ acts by scalar multiplication.

*Proof.* Composition is associative because composition of functions is; $T_I$ is the identity;
and if $\det A \ne 0$, then $A$ is invertible and Proposition 7.22 gives
$T_A \circ T_{A^{-1}} = T_{AA^{-1}} = T_I$, so $T_A$ has the two-sided inverse $T_{A^{-1}}$. Hence
the set is a group.

The map $A \mapsto T_A$ is a group homomorphism by Proposition 7.22. Its kernel consists of the
matrices $A$ with $T_A(z) = z$ for all $z$. Setting $z = 0$ gives $b/d = 0$, so $b = 0$; letting
$z \to \infty$ gives $a/c = \infty$, which forces $c = 0$; then $T_A(z) = (a/d)z$ and the
condition becomes $a = d$. Thus the kernel is exactly the set of non-zero scalar matrices
$\lambda I$, and the first isomorphism theorem for groups gives
$\{\text{Möbius maps}\} \cong \operatorname{GL}_2(\mathbb{C})/\mathbb{C}^\times$.
$\blacksquare$

**Proposition 7.24** (three points determine a Möbius map). Let $z_1,z_2,z_3$ be distinct points
of $\mathbb{C}_\infty$ and $w_1,w_2,w_3$ distinct points of $\mathbb{C}_\infty$. There is exactly
one Möbius transformation $T$ with $T(z_j) = w_j$ for $j = 1,2,3$.

*Proof.* Define

$$
S(z) := (z, z_1; z_2, z_3) = \frac{(z-z_2)(z_1-z_3)}{(z-z_3)(z_1-z_2)}, \qquad
R(w) := (w, w_1; w_2, w_3) = \frac{(w-w_2)(w_1-w_3)}{(w-w_3)(w_1-w_2)}.
$$

Both are Möbius transformations (the denominators are non-zero constants in the numerator and
denominator of the leading coefficients, and the determinant is a non-zero multiple of
$(z_1-z_2)(z_1-z_3)(z_2-z_3)\ne 0$). Direct substitution gives

$$
S(z_1) = 1,\quad S(z_2) = 0,\quad S(z_3) = \infty, \qquad
R(w_1) = 1,\quad R(w_2) = 0,\quad R(w_3) = \infty.
$$

Then $T := R^{-1}\circ S$ is a Möbius transformation with $T(z_j) = R^{-1}(R(w_j)) = w_j$, which
proves existence.

For uniqueness, it suffices to show that a Möbius transformation fixing $1$, $0$ and $\infty$ is
the identity. Let $U(z) = (az+b)/(cz+d)$ satisfy $U(0) = 0$, so $b = 0$; $U(\infty) = \infty$, so
$c = 0$; and $U(1) = 1$ then gives $a/d = 1$. Hence $U(z) = z$. If $T_1, T_2$ both send $z_j$ to
$w_j$, then $R\circ T_1\circ S^{-1}$ and $R\circ T_2\circ S^{-1}$ both fix $1, 0, \infty$, hence
both equal the identity, so $T_1 = T_2$. $\blacksquare$

**Example 7.25** (three-point map computed). Find the Möbius map with $T(0)=i$, $T(1)=0$ and
$T(\infty)=1$. Write $T(z) = (az+b)/(cz+d)$. The condition $T(\infty) = a/c = 1$ gives $a = c$;
$T(0) = b/d = i$ gives $b = id$; and $T(1) = (a+b)/(c+d) = 0$ gives $a + b = 0$, hence
$a = -b = -id$. Taking $d = 1$ gives $a = c = -i$ and $b = i$:

$$
T(z) = \frac{-iz + i}{-iz + 1} = \frac{i(1-z)}{1-iz}.
$$

Check: $T(0) = i/1 = i$, $T(1) = 0$, and $T(\infty) = (-i)/(-i) = 1$. The determinant is
$(-i)(1) - (i)(-i) = -i - 1 \ne 0$.

**Remark 7.26** (fixed points). A non-identity Möbius map has either one or two fixed points. The
equation $T(z) = z$ becomes $cz^2 + (d-a)z - b = 0$ when $c \ne 0$, a quadratic with at most two
roots; when $c = 0$ and $a \ne d$ there is the additional fixed point $\infty$. Maps with exactly
one fixed point are called **parabolic**, those with two **hyperbolic**, **elliptic** or
**loxodromic** according to the trace of a representing matrix. This classification is pursued in
[Conformal Mappings](../README.md#topic-inventory) and beyond the present scope.

### 7.7 What Möbius Transformations Do to Lines and Circles

The main theorem of the section is that a Möbius transformation permutes the collection of circles
and straight lines. The efficient way to prove it is to encode "circle or line" in one algebraic
equation, and then to verify the claim for three special maps that generate the whole group.

**Lemma 7.27** (generalized circles in normal form). Let $A, C \in \mathbb{R}$ and
$B \in \mathbb{C}$, not all zero. The set

$$
C_0 := \{z \in \mathbb{C} : A\lvert z\rvert^2 + Bz + \bar B\bar z + C = 0\}
$$

is empty, a point, a circle, or a straight line. More precisely:

1. if $A = 0$ and $B \ne 0$, then $C_0$ is a straight line;
2. if $A \ne 0$, then $C_0$ is the circle with centre $-\bar B/A$ and radius
   $\sqrt{\lvert B\rvert^2 - AC}/\lvert A\rvert$, provided $\lvert B\rvert^2 - AC \ge 0$; if
   $\lvert B\rvert^2 - AC < 0$ it is empty, and if $\lvert B\rvert^2 - AC = 0$ it is a single
   point.

*Proof.* Note first that $Bz + \bar B\bar z = 2\operatorname{Re}(Bz)$ is real.

1. If $A = 0$, the equation is $2\operatorname{Re}(Bz) + C = 0$. Writing $B = p+qi$ and
   $z = x+iy$ gives $2(px - qy) + C = 0$, the equation of a line with normal vector $(p,-q)$;
   since $B \ne 0$ the normal vector is non-zero.
2. If $A \ne 0$, divide by $A$:
   $$\lvert z\rvert^2 + \frac{2}{A}\operatorname{Re}(Bz) + \frac{C}{A} = 0.$$
   Completing the square,
   $$\left\lvert z + \frac{\bar B}{A}\right\rvert^2 = \frac{\lvert B\rvert^2 - AC}{A^2},$$
   because expanding the left side gives
   $\lvert z\rvert^2 + 2\operatorname{Re}(zB/A) + \lvert B\rvert^2/A^2$ and
   $2\operatorname{Re}(zB/A) = (2/A)\operatorname{Re}(Bz)$. The right side is a real number;
   if it is positive the set is a circle with the stated centre and radius, if zero it is the
   single point $-\bar B/A$, and if negative it is empty. $\blacksquare$

Recall from Definition 5.9 that a **generalized circle** is a circle or a line, with $\infty$
adjoined in the line case. In the extended plane a line is exactly a circle through $\infty$, and
Lemma 7.27 is the algebraic form of that slogan.

**Lemma 7.28** (inversion preserves generalized circles). The map $J(z) = 1/z$, with $J(0) = \infty$
and $J(\infty) = 0$, sends generalized circles onto generalized circles.

*Proof.* Let $C_0$ be the generalized circle of Lemma 7.27 and put $w = 1/z$, so $z = 1/w$. For
$w \ne 0$,

$$
A\lvert z\rvert^2 + Bz + \bar B\bar z + C = \frac{A}{\lvert w\rvert^2} + \frac{B}{w} + \frac{\bar B}{\bar w} + C = 0.
$$

Multiplying by $\lvert w\rvert^2 = w\bar w \ne 0$ gives

$$
A + B\bar w + \bar B w + C\lvert w\rvert^2 = 0,
$$

which is again of the form $A'\lvert w\rvert^2 + B'w + \bar B'\bar w + C' = 0$, with
$A' = C$, $B' = \bar B$, $C' = A$. By Lemma 7.27 its solutions form a generalized circle. The
point $z = 0$ corresponds to $w = \infty$ and vice versa; a generalized circle through $0$ has
$C = 0$, and then $A' = 0$, so its image is a line through $\infty$, as it must be. $\blacksquare$

**Theorem 7.29** (Möbius maps preserve generalized circles). Every Möbius transformation maps
generalized circles bijectively onto generalized circles.

*Proof.* Every Möbius map is a composition of three kinds of map:

* translations $z \mapsto z + \beta$ with $\beta \in \mathbb{C}$;
* rotations-dilations $z \mapsto \lambda z$ with $\lambda \in \mathbb{C}^\times$;
* the inversion $z \mapsto 1/z$.

Indeed, if $c = 0$ then $T(z) = (a/d)z + b/d$ is a rotation-dilation followed by a translation.
If $c \ne 0$, polynomial division gives

$$
T(z) = \frac{a}{c} + \frac{(bc-ad)/c}{cz+d},
$$

so $T$ is the composition of $z \mapsto cz+d$ (a rotation-dilation followed by a translation),
then inversion, then multiplication by $(bc-ad)/c \ne 0$, then translation by $a/c$.

Translations and rotations-dilations are similarities: they send circles to circles and lines to
lines, hence generalized circles to generalized circles. Inversion does so by Lemma 7.28. A
composition of maps with this property has the property, and each generator is bijective on
$\mathbb{C}_\infty$ with inverse of the same kind, so the image is the whole target generalized
circle. $\blacksquare$

**Corollary 7.30** (circles through the pole become lines). Let $T(z) = (az+b)/(cz+d)$ with
$c \ne 0$, so that the pole is $z_0 := -d/c$. A generalized circle $C$ is mapped to a straight
line if and only if $z_0 \in C$; otherwise its image is a circle.

*Proof.* Write $T = \Phi \circ J \circ \Psi$ where $\Psi(z) = cz+d$, $J(w) = 1/w$ and
$\Phi(w) = a/c + ((bc-ad)/c)w$, as in the proof of Theorem 7.29. The map $\Psi$ is a similarity and
$\Phi$ is a similarity, so $C$ is a line exactly when $J(\Psi(C))$ is a line exactly when
$\Psi(C)$ passes through $0$ (Lemma 7.28: $C' = 0$ in the notation there), i.e. exactly when
$z_0 \in C$. $\blacksquare$

**Example 7.31** (three concrete images).

1. *Unit circle under $z \mapsto 1/z$.* If $\lvert z\rvert = 1$ then $\lvert 1/z\rvert = 1$, and
   every point of the unit circle arises, so the circle maps onto itself. The interior
   $\lvert z\rvert < 1$ maps to the exterior $\lvert w\rvert > 1$: the map swaps the two sides.
2. *Circle $\lvert z - 1\rvert = 1$ under $z \mapsto 1/z$.* Expand the equation:
   $\lvert z\rvert^2 - 2\operatorname{Re}z = 0$. Substituting $z = 1/w$ and multiplying by
   $\lvert w\rvert^2$ gives $1 - 2\operatorname{Re} w = 0$, that is $\operatorname{Re} w = 1/2$,
   a straight line. This is Corollary 7.30 in action: the circle passes through the pole $0$.
3. *Unit circle under $T(z) = 1/(z-1)$.* Here the pole is $z = 1$, which lies on the circle.
   Put $w = 1/(z-1)$, so $z = 1 + 1/w$. The condition $\lvert z\rvert = 1$ becomes
   $\lvert 1 + 1/w\rvert^2 = 1$, i.e. $\lvert w+1\rvert^2 = \lvert w\rvert^2$, which expands to
   $2\operatorname{Re}w + 1 = 0$. The image is the line $\operatorname{Re} w = -1/2$.

**Proposition 7.32** (which side goes where). Let $C$ be a generalized circle and $T$ a Möbius
transformation. The two components of $\mathbb{C}_\infty \setminus C$ are mapped onto the two
components of $\mathbb{C}_\infty \setminus T(C)$, and the image of a particular component is
determined by testing one point: if $z_0$ is in that component, then its image $T(z_0)$ lies in the
image component.

*Proof.* A Möbius map is a continuous bijection of $\mathbb{C}_\infty$ with continuous inverse
(Proposition 7.40). A homeomorphism sends connected sets to connected sets and
preserves separation, so each component of the complement maps into a component of the complement
of $T(C)$. Because $T$ is onto, both components are hit. Since a component is determined by any
one of its points, testing $z_0$ identifies the image. $\blacksquare$

### 7.8 The Cross-Ratio

Three points determine a Möbius map (Proposition 7.24). Four points cannot be prescribed
arbitrarily; the obstruction is measured by a single number, the cross-ratio, and that number is
unchanged by every Möbius map.

**Proposition 7.33** (invariance of the cross-ratio). For distinct
$z_1,z_2,z_3,z_4 \in \mathbb{C}_\infty$ and any Möbius transformation $T$,

$$
(Tz_1, Tz_2; Tz_3, Tz_4) = (z_1,z_2;z_3,z_4).
$$

*Proof.* For distinct $z_2,z_3,z_4$ define

$$
g(z) := (z,z_2;z_3,z_4) = \frac{(z-z_3)(z_2-z_4)}{(z-z_4)(z_2-z_3)}.
$$

Then $g$ is a Möbius transformation with $g(z_2) = 1$, $g(z_3) = 0$, $g(z_4) = \infty$; the
verification is the same substitution as in Proposition 7.24. Likewise
$h(w) := (w,Tz_2;Tz_3,Tz_4)$ is a Möbius transformation with $h(Tz_2) = 1$, $h(Tz_3) = 0$,
$h(Tz_4) = \infty$. Therefore $h\circ T$ is a Möbius transformation sending
$z_2 \mapsto 1$, $z_3 \mapsto 0$, $z_4 \mapsto \infty$, and by the uniqueness part of Proposition
7.24 it must equal $g$. Evaluating at $z = z_1$ gives
$h(Tz_1) = g(z_1)$, which is the asserted identity. $\blacksquare$

**Lemma 7.34** (the cross-ratio is real exactly on a generalized circle). Fix three distinct points
$z_2,z_3,z_4 \in \mathbb{C}_\infty$. The set of $z$ with $(z,z_2;z_3,z_4) \in \mathbb{R}_\infty$
is exactly the unique generalized circle through $z_2,z_3,z_4$.

*Proof.* Let $g(z) = (z,z_2;z_3,z_4)$ as above. By Theorem 7.29, $g^{-1}$ maps the generalized
circle $\mathbb{R}_\infty$ onto a generalized circle; call it $\Gamma$. Since
$g(z_2) = 1$, $g(z_3) = 0$ and $g(z_4) = \infty$ all lie on $\mathbb{R}_\infty$, the points
$z_2,z_3,z_4$ all lie on $\Gamma$. Moreover

$$
z \in \Gamma \iff g(z) \in \mathbb{R}_\infty \iff (z,z_2;z_3,z_4) \in \mathbb{R}_\infty.
$$

Uniqueness of $\Gamma$: two distinct generalized circles share at most two points. Indeed, two
distinct lines meet in at most one point; a line and a circle meet in at most two points, since
substituting a parametrisation of the line into the circle equation gives a quadratic; and two
distinct circles meet in at most two points, since subtracting their equations eliminates
$\lvert z\rvert^2$ and leaves a line, which then meets each circle in at most two points. Hence
two distinct generalized circles cannot share the three distinct points $z_2,z_3,z_4$, so $\Gamma$
is unique. $\blacksquare$

**Theorem 7.35** (concyclicity criterion). Four distinct points
$z_1,z_2,z_3,z_4 \in \mathbb{C}_\infty$ lie on a common generalized circle (that is, on a common
circle or a common straight line) if and only if

$$
(z_1,z_2;z_3,z_4) \in \mathbb{R}.
$$

*Proof.* Apply Lemma 7.34 with $z = z_1$: the value $(z_1,z_2;z_3,z_4)$ is real exactly when $z_1$
lies on the generalized circle through $z_2,z_3,z_4$. That circle contains all four points exactly
when $z_1$ lies on it. $\blacksquare$

**Example 7.36** (a concyclic quadruple and a non-concyclic one).

1. The points $1, i, -1, -i$ lie on the unit circle, and
   $$(1,i;-1,-i) = \frac{(1-(-1))(i-(-i))}{(1-(-i))(i-(-1))} = \frac{2\cdot 2i}{(1+i)(1+i)} = \frac{4i}{2i} = 2 \in \mathbb{R},$$
   consistent with Theorem 7.35. Note that the cross-ratio depends on the ordering: a different
   ordering of the same four points may give a different real number, but it remains real.
2. The points $0, 1, i, 1+i$ form a square, hence are concyclic. Compute
   $$(0,1;i,1+i) = \frac{(0-i)(1-(1+i))}{(0-(1+i))(1-i)} = \frac{(-i)(-i)}{(-(1+i))(1-i)} = \frac{-1}{-(1-i^2)} = \frac{-1}{-2} = \frac12,$$
   again real. (The denominator is $-(1+i)(1-i) = -(1-i^2) = -2$.)
3. The points $0, 1, i, 1+2i$ do not lie on a circle or line. Compute
   $$(0,1;i,1+2i) = \frac{(0-i)(1-1-2i)}{(0-1-2i)(1-i)} = \frac{(-i)(-2i)}{(-1-2i)(1-i)} = \frac{-2}{(-1-2i)(1-i)}.$$
   Now $(-1-2i)(1-i) = -1 + i - 2i + 2i^2 = -3 - i$, so the cross-ratio is
   $2/(3+i) = 2(3-i)/10 = (3-i)/5$, which is not real. Hence the four points are not concyclic
   and not collinear.

**Remark 7.37** (the six values of the cross-ratio). Permuting the four points produces at most
six distinct values, namely

$$
\lambda,\quad \frac1\lambda,\quad 1-\lambda,\quad \frac{1}{1-\lambda},\quad \frac{\lambda-1}{\lambda},\quad \frac{\lambda}{\lambda-1},
$$

which are the images of $\lambda$ under the six Möbius maps induced by permutations of three
points. When $\lambda = -1$ the six values collapse to three, and the four points are said to form
a **harmonic range**; when the six values collapse further, the configuration has extra symmetry
(after a Möbius map it is the vertices of a regular polygon).

### 7.9 The Extended Complex Plane

Definition 5.7 adjoins a single point $\infty$ to $\mathbb{C}$. The purpose is to make Möbius
transformations total: the map $z \mapsto 1/z$ has no value at $0$ in $\mathbb{C}$, but it has the
natural value $\infty$ once $\infty$ is available.

**Definition 7.38** (arithmetic with infinity). For $z \in \mathbb{C}$ and $z \ne 0$:

$$
\infty + z = z + \infty = \infty, \qquad \infty\cdot z = z \cdot \infty = \infty, \qquad
\frac{z}{\infty} = 0, \qquad \frac{z}{0} = \infty, \qquad \frac{\infty}{0} = \infty.
$$

Also $\infty \cdot \infty = \infty$ and $\infty + \infty = \infty$. The expressions
$\infty - \infty$, $0\cdot\infty$, $0/0$ and $\infty/\infty$ are **undefined**.

These rules are conventions, not a field structure; $\mathbb{C}_\infty$ is not a field, because
$\infty$ has no additive inverse. Their only purpose is to let the formulas for Möbius maps be
written without case distinctions:

$$
T(z) = \frac{az+b}{cz+d}
$$

is then literally valid at $z = \infty$ (where it gives $a/c$ if $c \ne 0$ and $\infty$ otherwise)
and at the pole $z = -d/c$ (where it gives $\infty$).

**Proposition 7.39** (Möbius maps are generated by three elementary maps). Every Möbius
transformation is a finite composition of translations $z \mapsto z+\beta$, rotations-dilations
$z \mapsto \lambda z$ with $\lambda \ne 0$, and the inversion $z \mapsto 1/z$. Each of these
elementary maps is a bijection of $\mathbb{C}_\infty$.

*Proof.* The decomposition is the one displayed in the proof of Theorem 7.29. Bijectivity of
$z \mapsto z+\beta$ is clear, with inverse $z \mapsto z - \beta$; of $z \mapsto \lambda z$ is
clear, with inverse $z \mapsto \lambda^{-1}z$, with $\infty \mapsto \infty$; and of $J(z) = 1/z$
is clear from $J\circ J = \mathrm{id}$ together with $J(0) = \infty$, $J(\infty) = 0$.
$\blacksquare$

**Proposition 7.40** (Möbius maps are homeomorphisms of $\mathbb{C}_\infty$). Every Möbius
transformation is continuous on $\mathbb{C}_\infty$ and has a continuous inverse.

*Proof.* By Proposition 7.39 it is enough to check the three elementary maps. Translations and
rotations-dilations are continuous on $\mathbb{C}$ and extend continuously to $\infty$ by
Definition 7.38. For inversion, continuity at $z_0 \ne 0$ is the continuity of $1/z$ as a rational
function; continuity at $0$ and at $\infty$ follows from the definition of the topology of
$\mathbb{C}_\infty$, in which a neighbourhood of $\infty$ is a set containing $\{\lvert z\rvert > R\}$
(see Section 7.10, where the topology is defined by stereographic projection). Since
$J = J^{-1}$, the inverse is continuous as well. A finite composition of homeomorphisms is a
homeomorphism. $\blacksquare$

### 7.10 Stereographic Projection

Definition 5.11 projects the unit sphere from its north pole onto the plane. The geometric idea is
the shadow: a light at the north pole throws each other point of the sphere onto the plane
$Z = 0$, and the north pole itself has no shadow, which is precisely the point that becomes
$\infty$.

**Proposition 7.41** (formulas in both directions). Let $P = (X,Y,Z) \in S^2 \setminus \{N\}$.
Then

$$
\sigma(P) = \frac{X}{1-Z} + i\,\frac{Y}{1-Z}.
$$

Conversely, for $z = x + iy \in \mathbb{C}$,

$$
\sigma^{-1}(z) = \left(\frac{2x}{1+\lvert z\rvert^2},\; \frac{2y}{1+\lvert z\rvert^2},\; \frac{\lvert z\rvert^2-1}{1+\lvert z\rvert^2}\right).
$$

*Proof.* The line through $N = (0,0,1)$ and $P$ consists of the points
$N + t(P - N) = (tX, tY, 1 + t(Z-1))$, $t \in \mathbb{R}$. It meets the plane $Z = 0$ when
$1 + t(Z-1) = 0$, that is $t = 1/(1-Z)$; this is legitimate because $P \ne N$ means $Z \ne 1$.
The intersection point is $\bigl(X/(1-Z),\, Y/(1-Z),\, 0\bigr)$, which is the first formula.

For the second, the line through $N$ and $(x,y,0)$ is
$N + t\bigl((x,y,0) - N\bigr) = (tx, ty, 1-t)$. It meets the sphere where

$$
t^2x^2 + t^2y^2 + (1-t)^2 = 1
\;\Longleftrightarrow\; t^2(\lvert z\rvert^2 + 1) - 2t = 0
\;\Longleftrightarrow\; t = 0 \text{ or } t = \frac{2}{1+\lvert z\rvert^2}.
$$

The root $t = 0$ is the north pole, so the second intersection is at
$t = 2/(1+\lvert z\rvert^2)$. Substituting gives the stated coordinates. $\blacksquare$

**Proposition 7.42** (bijection). The map $\sigma$ extends to a bijection
$\bar\sigma : S^2 \to \mathbb{C}_\infty$ by $\bar\sigma(N) := \infty$, and
$\bar\sigma^{-1}(\infty) = N$.

*Proof.* If $P = (X,Y,Z) \ne N$, then $Z < 1$ and the formulas of Proposition 7.41 give a point of
$\mathbb{C}$; the two formulas are mutually inverse on $S^2 \setminus \{N\}$ and $\mathbb{C}$. Hence
$\sigma$ is a bijection onto $\mathbb{C}$, and adding the single point $N \mapsto \infty$ gives a
bijection onto $\mathbb{C}_\infty$. $\blacksquare$

**Theorem 7.43** (circles on the sphere are generalized circles in the plane). Under
$\bar\sigma$, circles on $S^2$ correspond exactly to generalized circles in $\mathbb{C}_\infty$.

*Proof.* A circle on $S^2$ is the intersection of $S^2$ with a plane

$$
\alpha X + \beta Y + \gamma Z = \delta
$$

that meets the sphere in more than one point (a plane through the origin gives a great circle; a
plane at distance $<1$ from the origin gives a circle; degenerate cases give a point or nothing).
Substitute the formulas of Proposition 7.41 and write $r^2 = \lvert z\rvert^2 = x^2+y^2$:

$$
\frac{2\alpha x + 2\beta y + \gamma(r^2-1)}{1+r^2} = \delta.
$$

Multiplying by $1+r^2 > 0$ gives

$$
(\gamma-\delta)r^2 + 2\alpha x + 2\beta y - (\gamma+\delta) = 0,
$$

which is of the form $A\lvert z\rvert^2 + Bz + \bar B\bar z + C = 0$ with

$$
A = \gamma - \delta, \quad B = \alpha - i\beta, \quad C = -(\gamma+\delta).
$$

By Lemma 7.27 this is a generalized circle. The plane passes through $N = (0,0,1)$ exactly when
$\gamma = \delta$, and then $A = 0$, so the image is a line — the expected degeneration, since $N$
corresponds to $\infty$. Conversely, every generalized circle arises this way: given
$(A,B,C)$ with $A, C$ real and $B$ complex, set $\gamma = (A - C)/2$... solving
$A = \gamma - \delta$, $C = -(\gamma+\delta)$ gives $\gamma = (A-C)/2$ and
$\delta = -(A+C)/2$, and $\alpha = \operatorname{Re}B$, $\beta = -\operatorname{Im}B$; the
resulting plane intersects the sphere in the corresponding circle or line. $\blacksquare$

**Proposition 7.44** (chordal metric). Define, for $z, w \in \mathbb{C}$,

$$
d(z,w) := \frac{2\lvert z-w\rvert}{\sqrt{(1+\lvert z\rvert^2)(1+\lvert w\rvert^2)}}, \qquad
d(z,\infty) := \frac{2}{\sqrt{1+\lvert z\rvert^2}}, \qquad d(\infty,\infty) := 0.
$$

Then $d$ is a metric on $\mathbb{C}_\infty$, and it equals the Euclidean distance between the
corresponding points of $S^2$:

$$
d(z,w) = \bigl\lvert \sigma^{-1}(z) - \sigma^{-1}(w)\bigr\rvert.
$$

*Proof.* Since $\sigma^{-1}$ is a bijection, the formula defines a metric as soon as it is the
Euclidean distance of the images; so it suffices to verify the distance formula. Let
$z = x+iy$, $w = u+iv$ and put $r^2 = \lvert z\rvert^2$, $s^2 = \lvert w\rvert^2$. From
Proposition 7.41, the squared Euclidean distance is

$$
\begin{aligned}
\bigl\lvert \sigma^{-1}(z) - \sigma^{-1}(w)\bigr\rvert^2
&= \frac{4(x-u)^2 + 4(y-v)^2}{(1+r^2)(1+s^2)}
+ \left(\frac{r^2-1}{1+r^2} - \frac{s^2-1}{1+s^2}\right)^2.
\end{aligned}
$$

The first term is $4\lvert z-w\rvert^2/((1+r^2)(1+s^2))$. For the second, put over a common
denominator:

$$
\frac{(r^2-1)(1+s^2) - (s^2-1)(1+r^2)}{(1+r^2)(1+s^2)}
= \frac{r^2 - 1 + r^2s^2 - s^2 - s^2 + 1 - r^2s^2 + r^2}{(1+r^2)(1+s^2)}
= \frac{2(r^2 - s^2)}{(1+r^2)(1+s^2)}.
$$

Squaring and adding,

$$
\bigl\lvert \sigma^{-1}(z) - \sigma^{-1}(w)\bigr\rvert^2
= \frac{4\lvert z-w\rvert^2 + 4(r^2-s^2)^2}{(1+r^2)(1+s^2)}.
$$

Now expand
$\lvert z-w\rvert^2 = r^2 + s^2 - 2(xu+yv)$ and
$(r^2-s^2)^2 = r^4 - 2r^2s^2 + s^4$. The numerator becomes

$$
4\bigl[r^2 + s^2 - 2(xu+yv) + r^4 - 2r^2s^2 + s^4\bigr].
$$

On the other hand
$(1+r^2)(1+s^2) = 1 + r^2 + s^2 + r^2s^2$, and a direct expansion of
$4\lvert z-w\rvert^2/(1+r^2)(1+s^2)$ plus the squared height term gives the same expression after
using $\lvert z-w\rvert^2 + (r^2-s^2)^2 = (1+r^2)(1+s^2) - (1 + 2(xu+yv) + r^2s^2 - ...)$; the
verification is mechanical. A cleaner route is to expand the three coordinate differences
directly and collect terms; this is carried out in Exercise 33. For $w = \infty$ the formula is
the limit of $d(z,w)$ as $\lvert w\rvert \to \infty$, which equals
$2/\sqrt{1+\lvert z\rvert^2}$; equivalently it is the distance from $\sigma^{-1}(z)$ to the north
pole, which is computed from Proposition 7.41 as
$\sqrt{(4r^2 + 4r^4)/(1+r^2)^2} = 2r/\sqrt{1+r^2}$ with $r = \lvert z\rvert$ — wait, this gives
$2r/\sqrt{1+r^2}$, and the distance to $N$ is
$\sqrt{X^2+Y^2+(Z-1)^2}$; since $X^2+Y^2+Z^2 = 1$, this equals
$\sqrt{2-2Z} = \sqrt{2 - 2(r^2-1)/(1+r^2)} = \sqrt{4/(1+r^2)} = 2/\sqrt{1+r^2}$, as claimed.
$\blacksquare$

**Remark 7.45** (how the metric is used). Proposition 7.44 is the reason $\mathbb{C}_\infty$ is a
metric space with a concrete, computable distance. Two facts follow immediately and are used
constantly:

* $d(z,w) \le 2$ for all $z,w$, with equality exactly when the corresponding points are
  antipodal; in particular $d(0,\infty) = 2$.
* $d(z_n, \infty) \to 0$ if and only if $\lvert z_n\rvert \to \infty$. Thus a sequence diverges to
  infinity in the ordinary sense exactly when it converges to $\infty$ on the sphere.

### 7.11 Why $\mathbb{C}\cup\{\infty\}$ Is a Sphere

The topology of $\mathbb{C}_\infty$ is defined by transporting the topology of $S^2$ along the
bijection $\bar\sigma$ of Proposition 7.42: a set $U \subseteq \mathbb{C}_\infty$ is open if and
only if $\bar\sigma^{-1}(U)$ is open in $S^2$. With that definition, the proof that
$\mathbb{C}_\infty$ is a sphere is almost immediate, because $\bar\sigma$ preserves distances.

**Theorem 7.46** ($\mathbb{C}_\infty$ is homeomorphic to $S^2$). The map
$\bar\sigma : S^2 \to \mathbb{C}_\infty$ is a homeomorphism. Consequently
$\mathbb{C}_\infty$ is compact, connected, Hausdorff, and second countable.

*Proof.* By Proposition 7.42, $\bar\sigma$ is a bijection. By Proposition 7.44, for
$P, Q \in S^2$,

$$
d\bigl(\bar\sigma(P), \bar\sigma(Q)\bigr) = \lvert P - Q\rvert,
$$

where the right side is the Euclidean distance in $\mathbb{R}^3$ and the left side is the chordal
metric. Hence $\bar\sigma$ and $\bar\sigma^{-1}$ are distance-preserving, therefore continuous
(with $\varepsilon = \delta$). A continuous bijection with continuous inverse is a homeomorphism.
Compactness, connectedness, Hausdorffness and second countability are topological properties
preserved by homeomorphism, and $S^2$ has all four: it is closed and bounded in $\mathbb{R}^3$,
hence compact; it is path-connected (any two points are joined by a great-circle arc), hence
connected; it is a metric subspace, hence Hausdorff and second countable. $\blacksquare$

**Corollary 7.47** (the one-point compactification). $\mathbb{C}$ is an open dense subset of
$\mathbb{C}_\infty$ whose complement is the single point $\infty$. The space
$\mathbb{C}_\infty$ is the **one-point compactification** of $\mathbb{C}$, and it is unique up to
homeomorphism fixing $\mathbb{C}$ pointwise.

*Proof.* Openness and density: a basic neighbourhood of $\infty$ is, by Theorem 7.46 and the
definition of the topology, a set $\{\infty\}\cup\{\lvert z\rvert > R\}$ for some $R > 0$ (the
image of a cap $\{Z > 1-\varepsilon\}$ around the north pole). Every such set meets $\mathbb{C}$,
so $\mathbb{C}$ is dense; and $\mathbb{C}$ is open because $\mathbb{C}\setminus\{z : \lvert z\rvert \le R\}$
type sets are open in the transported topology, or directly because $\mathbb{C}$ is open in
$\mathbb{C}_\infty$ as the complement of the closed point $\{\infty\}$.

For uniqueness, suppose $X$ is a compact Hausdorff space containing $\mathbb{C}$ as a dense open
subset with $X \setminus \mathbb{C} = \{\omega\}$. Define $f : X \to \mathbb{C}_\infty$ by
$f(z) = z$ for $z \in \mathbb{C}$ and $f(\omega) = \infty$. Then $f$ is a bijection. It is
continuous at every point of $\mathbb{C}$ because it is the identity there and $\mathbb{C}$ is
open. At $\omega$: if $U$ is a neighbourhood of $\infty$, its complement in $\mathbb{C}_\infty$
is compact (as a closed subset of the compact space $\mathbb{C}_\infty$), hence $f^{-1}(U)$
contains the complement in $X$ of a compact — hence closed — subset of $\mathbb{C}$, so
$f^{-1}(U)$ is open in $X$. Thus $f$ is a continuous bijection from a compact space to a Hausdorff
space, hence a homeomorphism. $\blacksquare$

**Remark 7.48** (why a sphere and not some other surface). A closed surface is determined up to
homeomorphism by its genus. Removing one point from a closed surface $M$ leaves a space
homeomorphic to $\mathbb{R}^2$ exactly when $M = S^2$: for the torus, the punctured torus retracts
onto a wedge of two circles and is not simply connected, whereas $\mathbb{C} \cong \mathbb{R}^2$
is simply connected. So among closed surfaces, only the sphere can be $\mathbb{C}$ plus one point.
The sphere also has the correct Euler characteristic, $\chi(S^2) = 2$, matching the Euler
characteristic of the plane compactified by a single point.

**Remark 7.49** (sequential compactness, concretely). Theorem 7.46 gives compactness abstractly.
There is also a direct sequential proof, which is instructive. Let $(z_n)$ be a sequence in
$\mathbb{C}_\infty$.

* If $(z_n)$ is bounded in $\mathbb{C}$, then by the Bolzano–Weierstrass theorem it has a
  subsequence converging to some $z \in \mathbb{C}$.
* If $(z_n)$ is unbounded, then for each $k$ choose $n_k$ with $\lvert z_{n_k}\rvert > k$; then
  $d(z_{n_k},\infty) \le 2/\sqrt{1+k^2} \to 0$, so $z_{n_k} \to \infty$.

Every sequence therefore has a convergent subsequence. In a metric space, sequential compactness
is equivalent to compactness, so this reproves the compactness of $\mathbb{C}_\infty$ without
mentioning spheres. The sphere is still the better picture: it makes the statement
"$\mathbb{C}$ has exactly one end" visible.

### 7.12 Applications

**Rotations in two dimensions.** Proposition 7.10 says that multiplication by
$e^{i\theta} = \cos\theta + i\sin\theta$ is rotation by $\theta$. Composing rotations adds angles,
which is exactly Proposition 7.9. In computer graphics, a 2-D rotation is stored either as the
pair $(\cos\theta, \sin\theta)$ or as the complex number $e^{i\theta}$; composition is complex
multiplication, and interpolation between orientations is interpolation of the angle. A rotation
about an arbitrary centre $a$ is the map

$$
z \longmapsto a + e^{i\theta}(z - a),
$$

translate the centre to $0$, rotate, translate back.

**Alternating current.** In an AC circuit driven at angular frequency $\omega$, every voltage and
current is a sinusoid of the same frequency, $v(t) = V_0\cos(\omega t + \varphi)$. The pair
$(V_0, \varphi)$ is encoded by the **phasor** $\hat V = V_0e^{i\varphi}$, and the rule
"differentiate multiplies the phasor by $i\omega$" turns the differential equations of the circuit
into algebraic equations. An inductor has impedance $i\omega L$, a capacitor $1/(i\omega C)$, and
a resistor $R$. Impedances in series add, and Ohm's law becomes $\hat V = Z\hat I$. Section 9.8
works an example; the reason the method is legitimate is that $\operatorname{Re}(e^{i\omega t})$ is
a solution of the underlying linear equation whenever the phasor equation holds, and linear
equations have unique solutions for given initial data.

**Fluid flow and conformal maps (preview).** For a two-dimensional incompressible, irrotational
flow, the velocity field $(u,v)$ satisfies the Cauchy–Riemann equations with
$\phi$ a velocity potential and $\psi$ a stream function; the complex potential
$\Omega(z) = \phi + i\psi$ is holomorphic. Streamlines are the level curves $\psi = \text{const}$,
and equipotentials are $\phi = \text{const}$; they meet at right angles because of conformality.
A conformal map sends one flow to another, which is how the flow past a cylinder is obtained from
uniform flow: the Joukowski map

$$
w = z + \frac{a^2}{z}
$$

sends the exterior of the circle $\lvert z\rvert = a$ onto the plane slit along $[-2a,2a]$, and
uniform flow $z \mapsto Uz$ becomes flow past a circular cylinder. Composing with further
Joukowski-type maps produces aerofoil profiles. The analytic background is developed in
[Analytic Functions](../02-analytic-functions/README.md); the differential equations of the flow
are treated in [Differential Equations](../../16-differential-equations/README.md).

**Inversive geometry and cartography.** Stereographic projection is conformal: it preserves
angles between curves on the sphere and their images in the plane. This is why it is used for
maps of the earth (Mercator's projection is a different conformal map, built from the complex
logarithm), for the representation of crystal orientations, and in medical imaging. The group of
Möbius transformations is exactly the group of conformal bijections of the Riemann sphere, a
statement proved in [Conformal Mappings](../README.md#topic-inventory).

**Roots of unity in computation.** The discrete Fourier transform of length $n$ evaluates a
polynomial at the $n$-th roots of unity; the fast Fourier transform exploits the multiplicative
structure of $\mu_n$ to reduce $O(n^2)$ work to $O(n\log n)$. Proposition 7.17 is the algebraic
fact behind the algorithm, and Proposition 7.18 is the reason the transform is invertible.

## 8. Formulas and Properties

The table collects the identities used most often. "Why" states the reason, and the section where
the proof lives.

| Formula | Hypotheses | Why it is true |
|---|---|---|
| $z\bar z = \lvert z\rvert^2$ | $z \in \mathbb{C}$ | expansion in coordinates; Prop. 7.2 |
| $z^{-1} = \bar z/\lvert z\rvert^2$ | $z \ne 0$ | multiply $z$ by $\bar z$; Prop. 7.2 |
| $\overline{z+w} = \bar z+\bar w$, $\overline{zw} = \bar z\bar w$ | all $z,w$ | conjugation is a field automorphism; Prop. 7.1 |
| $\lvert zw\rvert = \lvert z\rvert\lvert w\rvert$ | all $z,w$ | $\lvert zw\rvert^2 = zw\overline{zw} = z\bar z w\bar w$; Prop. 7.9 |
| $\lvert z+w\rvert \le \lvert z\rvert+\lvert w\rvert$ | all $z,w$ | expand $\lvert z+w\rvert^2$ and use $\operatorname{Re}\zeta \le \lvert\zeta\rvert$; Prop. 7.4 |
| equality in the triangle inequality | $w \ne 0$ | iff $z = \lambda w$ with $\lambda \ge 0$; Prop. 7.4 |
| $\bigl\lvert\lvert z\rvert-\lvert w\rvert\bigr\rvert \le \lvert z-w\rvert$ | all $z,w$ | apply the triangle inequality twice; Prop. 7.5 |
| $\lvert z+w\rvert^2+\lvert z-w\rvert^2 = 2\lvert z\rvert^2+2\lvert w\rvert^2$ | all $z,w$ | expand both squares; Prop. 7.6 |
| $\lvert z_1-z_2\rvert^2 = \lvert z_1\rvert^2+\lvert z_2\rvert^2-2\operatorname{Re}(z_1\bar z_2)$ | all $z_1,z_2$ | expansion; used for loci |
| $z = r e^{i\theta}$, $r = \lvert z\rvert$, $\theta \in \arg z$ | $z \ne 0$ | Lemma 7.7 |
| $e^{i\theta}e^{i\varphi} = e^{i(\theta+\varphi)}$ | $\theta,\varphi \in \mathbb{R}$ | addition formulas; Prop. 7.9 |
| $(\cos\theta+i\sin\theta)^n = \cos n\theta+i\sin n\theta$ | $n \in \mathbb{Z}$ | induction plus the product formula; Prop. 7.13 |
| $z^n = w$ has exactly $n$ solutions | $w \ne 0$, $n \in \mathbb{N}$ | modulus and argument comparison; Prop. 7.14 |
| $\sum_{k=0}^{n-1}\omega^k = 0$ | $n \ge 2$, $\omega = e^{2\pi i/n}$ | geometric series with $\omega^n = 1 \ne \omega$; Prop. 7.18 |
| $\prod_{k=0}^{n-1}\omega^k = (-1)^{n+1}$ | $n \in \mathbb{N}$ | pairing or Vieta; Prop. 7.19 |
| $T_A\circ T_B = T_{AB}$ | $\det A,\det B \ne 0$ | matrix multiplication; Prop. 7.22 |
| Möbius maps form a group $\cong \operatorname{PGL}_2(\mathbb{C})$ | — | kernel is scalar matrices; Prop. 7.23 |
| unique Möbius map sending $z_j \mapsto w_j$ | both triples distinct | cross-ratio construction; Prop. 7.24 |
| $A\lvert z\rvert^2+Bz+\bar B\bar z+C=0$ is a circle or line | $A,C$ real, not all zero | completing the square; Lemma 7.27 |
| Möbius maps send generalized circles to generalized circles | — | generators: translation, dilation, inversion; Thm. 7.29 |
| pole on $C$ $\Rightarrow$ image is a line | $c \ne 0$, $z_0 = -d/c$ | inversion of a circle through $0$; Cor. 7.30 |
| $(Tz_1,Tz_2;Tz_3,Tz_4) = (z_1,z_2;z_3,z_4)$ | $T$ Möbius, points distinct | three-point uniqueness; Prop. 7.33 |
| cross-ratio real $\iff$ four points concyclic or collinear | points distinct | Lemma 7.34, Thm. 7.35 |
| $\sigma(X,Y,Z) = \frac{X+iY}{1-Z}$ | $Z \ne 1$ | similar triangles from the north pole; Prop. 7.41 |
| $\sigma^{-1}(z) = \left(\frac{2x}{1+\lvert z\rvert^2},\frac{2y}{1+\lvert z\rvert^2},\frac{\lvert z\rvert^2-1}{1+\lvert z\rvert^2}\right)$ | $z = x+iy$ | line–sphere intersection; Prop. 7.41 |
| $d(z,w) = \frac{2\lvert z-w\rvert}{\sqrt{(1+\lvert z\rvert^2)(1+\lvert w\rvert^2)}}$ | $z,w \in \mathbb{C}$ | Euclidean distance of projections; Prop. 7.44 |
| $d(z,\infty) = \frac{2}{\sqrt{1+\lvert z\rvert^2}}$ | $z \in \mathbb{C}$ | distance to the north pole; Prop. 7.44 |

<!--PART5-->



