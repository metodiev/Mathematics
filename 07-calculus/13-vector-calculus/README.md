# Vector Calculus

> [Calculus](../README.md) · Level: Advanced · Prerequisites: [Differentiation Rules](../04-differentiation-rules/README.md), [Integrals](../06-integrals/README.md), [The Fundamental Theorem of Calculus](../07-fundamental-theorem-of-calculus/README.md), [Techniques of Integration](../08-techniques-of-integration/README.md), [Linear Algebra](../../08-linear-algebra/README.md), and the partial-derivative and multiple-integral material listed in the [Calculus index](../README.md) · Estimated time: 12 h

## 1. Introduction

Single-variable calculus integrates a function over an interval, and the Fundamental Theorem of Calculus
says that this integral equals a difference of values at the two endpoints:

$$\int_a^b f'(x)\,dx = f(b)-f(a).$$

Read geometrically, the interval $[a,b]$ is a one-dimensional region whose boundary is the two-point set
$\{a,b\}$, and the theorem says *the integral of a derivative over the region equals a sum of the field
over the boundary*. Vector calculus is what happens when the interval is replaced by a curve, a surface,
or a solid body. The derivative is replaced by the gradient, the curl, or the divergence; the integral by
a line, surface, or volume integral; and the one theorem becomes four:

* the **fundamental theorem for line integrals**, for a curve and its two endpoints;
* **Green's theorem**, for a plane region and its boundary curve;
* **Stokes' theorem**, for a surface and its boundary curve;
* the **divergence theorem**, for a solid and its boundary surface.

Each has exactly the shape above: an integral of a derivative over a region equals an integral of the
original field over the boundary. The last section of the theory (§7.12) shows that they are not four
theorems but one — the generalised Stokes theorem $\int_{\partial M}\omega = \int_M d\omega$ — seen in four
languages.

The subject exists because nature is written in fields. The velocity of a fluid assigns a vector to every
point; the electric and magnetic fields do the same; temperature and pressure assign a *number* to every
point. Three questions recur, and each has a name:

* **How much work does a field do along a path?** — the line integral of the field along the path.
* **How much fluid crosses a surface?** — the flux, the surface integral of the field's normal component.
* **Is the flow locally a source, a sink, or a swirl?** — divergence and curl measure exactly these.

The computational content is a small set of recipes (parametrise, substitute, integrate) and three
identities that convert a hard integral into an easy one. The conceptual content is **orientation**. Every
theorem in this topic compares two integrals whose signs depend on a choice — the direction of a curve,
the side of a surface, the outside of a solid — and the theorems are true only when the two choices are
made *consistently*. Choosing the wrong normal, or traversing the boundary backwards, produces a correct
computation of the negative of the right answer. That is why §11 begins with orientation, and why every
worked example states its orientation explicitly.

A second theme is **hypothesis tracking**. Each theorem needs a field that is continuously differentiable,
a region of a certain shape, and a boundary with a certain regularity. The two most important hypotheses
are *simple connectivity*, which decides whether a curl-free field is a gradient, and *the absence of
singularities inside the region*, which decides whether the divergence theorem may be applied at all.

**Roadmap.** §4 gives the physical picture without symbols. §5 fixes the definitions: fields, field lines,
conservative fields, line and surface integrals, curl and divergence. §7 develops the theory and proves
what can be proved in a first course; §8 collects the formulas with their hypotheses; §9 works eight
examples from routine to subtle; §10 draws the dependency of the theorems; §11 lists the errors that
actually occur; §12 shows where the theory is used.

## 2. Prerequisites

**From single-variable calculus**

* All differentiation rules, especially the chain rule, and the ability to differentiate an expression
  such as $\phi(x(t),y(t),z(t))$ in $t$.
* The Fundamental Theorem of Calculus in both parts
  ([The Fundamental Theorem of Calculus](../07-fundamental-theorem-of-calculus/README.md)).
* Substitution in definite integrals, and the standard trigonometric integrals
  ([Techniques of Integration](../08-techniques-of-integration/README.md)).

**From multivariable calculus** (the planned *Multivariable Calculus* topic of the
[Calculus index](../README.md); every fact used below is restated here)

* Partial derivatives, the gradient $\nabla f = (f_x,f_y,f_z)$, and the chain rule for a composite
  $t\mapsto f(\mathbf r(t))$:
  $\dfrac{d}{dt}f(\mathbf r(t)) = \nabla f(\mathbf r(t))\cdot\mathbf r'(t)$.
* Level sets $f = c$ and the fact that $\nabla f$ is orthogonal to them.
* Double and triple integrals, and the area and volume elements in polar and spherical coordinates:
  $dA = r\,dr\,d\theta$ and $dV = \rho^2\sin\phi\,d\rho\,d\phi\,d\theta$.
* Parametrised curves: the circle $\mathbf r(t) = (a\cos t, a\sin t)$, the helix, and the line segment
  $\mathbf r(t) = \mathbf a + t(\mathbf b-\mathbf a)$.

**From linear algebra** ([Linear Algebra](../../08-linear-algebra/README.md))

* The dot product $\mathbf u\cdot\mathbf v = u_1v_1+u_2v_2+u_3v_3$, its bilinearity, and the identity
  $\mathbf u\cdot\mathbf v = \lVert\mathbf u\rVert\,\lVert\mathbf v\rVert\cos\theta$.
* The cross product $\mathbf u\times\mathbf v$: it is orthogonal to both factors, its direction obeys the
  right-hand rule, and $\lVert\mathbf u\times\mathbf v\rVert$ is the area of the parallelogram spanned by
  $\mathbf u$ and $\mathbf v$.
* Determinants, including the $3\times3$ determinant used as a mnemonic for the curl.

**From trigonometry** ([Trigonometry](../../05-trigonometry/README.md))

* $\sin^2\theta+\cos^2\theta = 1$, the double-angle formulas, and the parametrisations of the circle,
  the sphere, the cylinder, the cone and the torus.

**Notation warning.** This topic uses $\mathbf F$ for a field, $\mathbf r$ for a position vector, $C$ for a
curve, $S$ for a surface, $D$ for a plane region, $V$ for a solid, and $\partial$ for "boundary of". The
symbol $\partial$ is also used for partial derivatives; context — $\partial D$ versus $\partial P/\partial x$
— always disambiguates.

## 3. Learning Objectives

After working through this tutorial you will be able to:

1. Recognise a vector field in a formula, a picture, or a physical description, and sketch its field
   lines by solving $\mathbf r'(t) = \mathbf F(\mathbf r(t))$ in simple cases.
2. Decide whether a field is conservative, find a potential by integration, and use the fundamental
   theorem for line integrals to replace a line integral by a difference of potentials.
3. State and prove that a conservative field is path independent, and explain why the converse needs a
   hypothesis on the shape of the domain.
4. Set up and evaluate line integrals of scalar fields (mass, arc length, average) and of vector fields
   (work, circulation), choosing and tracking the orientation correctly.
5. Compute curl and divergence, state their geometric meanings as circulation density and flux density,
   and use the identities $\nabla\times\nabla f = \mathbf 0$ and $\nabla\cdot(\nabla\times\mathbf F)=0$.
6. State Green's theorem with its hypotheses and orientation, prove it for a simple region, and use both
   its circulation form and its flux form, including the area formula.
7. Parametrise a surface, compute its area element $|\mathbf r_u\times\mathbf r_v|\,du\,dv$, and evaluate
   surface integrals of scalar functions.
8. Orient a surface, compute flux, and apply Stokes' theorem and the divergence theorem, including
   problems where a surface must be completed before the divergence theorem applies.
9. Explain in what sense Green, Stokes, the divergence theorem and the Fundamental Theorem of Calculus
   are one theorem, and translate between vector fields and differential forms.
10. Apply the theorems to fluid flow and to Maxwell's equations, and interpret circulation and flux
    physically.

## 4. Intuition

**A field is a vector attached to every point.** Imagine a river. At every point of the water there is a
velocity: a speed and a direction. A leaf dropped on the surface is carried along a curve — a **field
line** (or streamline). If the water flows in closed circles, the leaf goes round and round; if it flows
out of a spring, the field lines radiate away; if it drains into a hole, they converge. Nothing about the
field requires a formula: a picture of arrows already carries the information.

**Work is "push times displacement", accumulated.** To move a particle along a path against a force, you
pay at every instant the component of the force along the direction of motion, multiplied by the small
displacement. Summing gives a line integral. If the force is the gradient of a potential — gravity,
electrostatics — the total cost depends only on the starting and ending heights, not on the route. That is
the content of the fundamental theorem for line integrals, and it is exactly the statement that
*gravitational work is $mgh$*.

**Circulation measures swirl.** Walk once around a closed loop, adding up the component of the field along
your direction of travel. If the field is a swirl about an axis, the sum is large; if it is a gradient, the
sum is zero, because you return to the same height. The circulation per unit area, in the limit of a tiny
loop, is the component of the **curl** about that loop's normal. Curl is therefore *local swirliness*: a
paddle wheel placed in the flow spins fastest about the axis of the curl, at a rate of half its magnitude.

**Flux measures through-flow.** Hold a small net in the river. The volume of water crossing it per second
is the component of velocity perpendicular to the net, summed over its surface — the **flux**. For a tiny
closed box, the net outflow per unit volume is the **divergence**. Positive divergence means a source
inside; negative means a sink; zero means the fluid is incompressible and whatever enters must leave.

**The boundary knows the interior.** The four theorems all say the same thing in different dimensions:
*the total of a derivative over a region is what the field does at the boundary.* The reason is
cancellation. Cut a region into tiny cells. On every internal face two neighbouring cells contribute equal
and opposite fluxes, or traversals in opposite directions, so the internal contribution cancels. What
survives is the outer boundary. The derivative (gradient, curl, divergence) is precisely the quantity whose
cell-by-cell sum telescopes in this way. This single idea, made precise, is the generalised Stokes
theorem, and it explains why the same proof pattern — cut, cancel, sum — appears in every dimension.

**Orientation is bookkeeping for "which side".** A curve can be walked in two directions; a surface has two
sides; a solid has an inside and an outside. A boundary orientation is not a convention imposed by
mathematicians for their convenience — it is what makes the cancellation above happen with consistent
signs. Change the direction of the walk and every term changes sign; change the normal and the same. The
theorems are equalities between *oriented* integrals.

## 5. Formal Definition

### 5.1 Domains, curves and regions

A set $D\subseteq\mathbb{R}^n$ is **open** if for every $\mathbf x\in D$ there is $r>0$ with the ball
$B_r(\mathbf x)\subseteq D$. It is **connected** if it is not the union of two disjoint non-empty open
sets, and **path-connected** if any two of its points can be joined by a curve inside $D$; for open subsets
of $\mathbb{R}^n$ the two notions coincide, and we simply say **connected**.

$D$ is **star-shaped** if there is $\mathbf x_0\in D$ such that for every $\mathbf x\in D$ the segment
$[\mathbf x_0,\mathbf x]$ lies in $D$. Every convex set is star-shaped. A plane domain $D$ is
**simply connected** if every simple closed curve in $D$ encloses only points of $D$; equivalently, $D$
has no holes. A star-shaped domain is simply connected.

A **curve** is a continuous map $\mathbf r:[a,b]\to\mathbb{R}^n$ that is piecewise $C^1$ and **regular**:
$\mathbf r'(t)\ne\mathbf 0$ wherever the derivative exists. The curve is **simple** if $\mathbf r$ is
injective on $[a,b]$; it is **closed** if $\mathbf r(a)=\mathbf r(b)$; and it is a **simple closed curve**
if it is closed and injective on $[a,b)$. The image $C=\mathbf r([a,b])$ is also called the curve, and the
map is a **parametrisation**.

Two regular parametrisations of the same oriented curve differ by a reparametrisation
$\mathbf r_2 = \mathbf r_1\circ\varphi$ with $\varphi'>0$; if $\varphi'<0$ the orientation is reversed.
The reversed curve is written $-C$.

A plane region $D$ is **$x$-simple** (also called of type II) if
$D = \{(x,y) : c\le y\le d,\ g_1(y)\le x\le g_2(y)\}$ for continuous $g_1\le g_2$, and **$y$-simple**
(type I) if $D = \{(x,y) : a\le x\le b,\ f_1(x)\le y\le f_2(x)\}$. A **simple region** is one that is
both. Squares, disks, triangles and the region under a graph are simple; an annulus is not, but it is a
union of simple regions after a cut.

### 5.2 Vector fields

Let $D\subseteq\mathbb{R}^n$ be open. A **vector field** on $D$ is a map
$\mathbf F:D\to\mathbb{R}^n$, written in components as

$$\mathbf F(x,y,z) = P(x,y,z)\,\mathbf i + Q(x,y,z)\,\mathbf j + R(x,y,z)\,\mathbf k
= \bigl(P(x,y,z),\,Q(x,y,z),\,R(x,y,z)\bigr).$$

It is **continuous**, or of class $C^k$, when each component is. A **scalar field** is a map
$f:D\to\mathbb{R}$. Examples: the velocity field of a fluid; the electric field of a charge distribution;
the gradient $\nabla f$ of a scalar field; the position field $\mathbf F(\mathbf x)=\mathbf x$; the vortex
field $\mathbf F(x,y) = (-y,x)/(x^2+y^2)$ on $\mathbb{R}^2\setminus\{(0,0)\}$.

A vector field is **tangent** to a curve $C$ if $\mathbf F$ is parallel to a tangent of $C$ at every point
of $C$, and **normal** to a surface $S$ if $\mathbf F$ is parallel to a normal of $S$ at every point of $S$.

### 5.3 Field lines

Let $\mathbf F$ be a continuous vector field on $D$. A **field line** (streamline, integral curve) of
$\mathbf F$ is a $C^1$ curve $\mathbf r:I\to D$ on an interval $I$ such that

$$\mathbf r'(t) = \mathbf F\bigl(\mathbf r(t)\bigr) \qquad\text{for all } t\in I .$$

This is a system of ordinary differential equations, one per coordinate. If $\mathbf F$ is $C^1$ and
$\mathbf F(\mathbf x_0)\ne\mathbf 0$, the standard existence and uniqueness theorem for ODEs gives a unique
maximal field line through $\mathbf x_0$; distinct field lines are therefore disjoint, and they can meet
only at points where $\mathbf F=\mathbf 0$ (a **critical point** or stagnation point). A field line is a
*set*; its parametrisation is not unique, because any increasing reparametrisation is again a field line.

### 5.4 Conservative fields and potentials

A vector field $\mathbf F$ on an open connected $D\subseteq\mathbb{R}^n$ is **conservative** if there is a
$C^1$ scalar field $\phi$ on $D$ with

$$\mathbf F = \nabla\phi .$$

The function $\phi$ is a **potential** (scalar potential) for $\mathbf F$. It is determined only up to an
additive constant: if $\phi$ works, so does $\phi+c$, and on a connected domain any two potentials differ
by a constant, because a $C^1$ function with zero gradient on a connected open set is constant.

> **Sign convention.** Physicists usually write $\mathbf F = -\nabla U$ and call $U$ the potential energy,
> so $U = -\phi$. With this convention the gravitational field of a mass $M$ is
> $\mathbf F = -GMm\,\mathbf r/\lVert\mathbf r\rVert^3 = -\nabla(-GMm/\lVert\mathbf r\rVert)$. This topic
> uses the mathematical convention $\mathbf F = \nabla\phi$; every formula below can be translated by
> replacing $\phi$ with $-U$.

Examples of conservative fields: constant fields; $\mathbf F = (2xy, x^2)$ with $\phi = x^2y$; every
central field $\mathbf F(\mathbf x) = f(r)\,\mathbf x$ with $r = \lVert\mathbf x\rVert$ and continuous $f$,
whose potential is $\phi(\mathbf x) = \int_0^{r} f(s)s\,ds$; in particular the inverse-square field
$\mathbf r/\lVert\mathbf r\rVert^3 = -\nabla(1/\lVert\mathbf r\rVert)$.

### 5.5 Line integrals

Let $C$ be a piecewise $C^1$ curve with regular parametrisation $\mathbf r:[a,b]\to\mathbb{R}^n$, and let
$f$ be continuous on $C$. Partition $[a,b]$ by $a=t_0<t_1<\dots<t_N=b$ and let $\Delta s_i$ be the arc
length of the subarc from $\mathbf r(t_{i-1})$ to $\mathbf r(t_i)$. The **line integral of a scalar field**
is

$$\int_C f\,ds := \lim_{\max_i(t_i-t_{i-1})\to 0}\ \sum_{i=1}^{N} f\bigl(\mathbf r(t_i^*)\bigr)\,\Delta s_i ,$$

where $t_i^*\in[t_{i-1},t_i]$ is arbitrary. The limit exists when $f$ is continuous and $C$ is piecewise
$C^1$, and it equals

$$\int_C f\,ds = \int_a^b f\bigl(\mathbf r(t)\bigr)\,\lVert\mathbf r'(t)\rVert\,dt .$$

Here $ds = \lVert\mathbf r'(t)\rVert\,dt$ is the **arc length element**, so $\int_C 1\,ds$ is the length
of $C$.

Let $\mathbf F$ be a continuous vector field on an open set containing $C$. The **line integral of a vector
field** (or **circulation integral**) is

$$\int_C \mathbf F\cdot d\mathbf r
:= \lim_{\max_i\lVert\mathbf r(t_i)-\mathbf r(t_{i-1})\rVert\to0}\ \sum_{i=1}^{N}
\mathbf F\bigl(\mathbf r(t_i^*)\bigr)\cdot\bigl(\mathbf r(t_i)-\mathbf r(t_{i-1})\bigr) ,$$

and it equals

$$\int_C \mathbf F\cdot d\mathbf r = \int_a^b \mathbf F\bigl(\mathbf r(t)\bigr)\cdot\mathbf r'(t)\,dt
= \int_C (P\,dx + Q\,dy + R\,dz).$$

Writing $\mathbf T = \mathbf r'/\lVert\mathbf r'\rVert$ for the unit tangent in the direction of
orientation gives the identity $\int_C \mathbf F\cdot d\mathbf r = \int_C (\mathbf F\cdot\mathbf T)\,ds$,
which is the exact sense in which the vector line integral is a scalar line integral of the tangential
component.

Both definitions extend to piecewise $C^1$ curves by summing over the smooth pieces. A curve is **closed**
if its endpoints coincide, and then the integral is written $\oint_C$ and called the **circulation** when
$\mathbf F$ is a velocity or force field.

### 5.6 Curl and divergence

Let $\mathbf F = (P,Q,R)$ be a $C^1$ vector field on an open set in $\mathbb{R}^3$. The **curl** is the
vector field

$$\nabla\times\mathbf F
= \left(\frac{\partial R}{\partial y}-\frac{\partial Q}{\partial z}\right)\mathbf i
+ \left(\frac{\partial P}{\partial z}-\frac{\partial R}{\partial x}\right)\mathbf j
+ \left(\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}\right)\mathbf k ,$$

and the **divergence** is the scalar field

$$\nabla\cdot\mathbf F = \frac{\partial P}{\partial x}+\frac{\partial Q}{\partial y}
+\frac{\partial R}{\partial z} .$$

For a plane field $\mathbf F(x,y) = (P,Q)$ one sets $R=0$ and treats the plane as $z=0$; then
$\nabla\times\mathbf F = (0,0,Q_x-P_y)$ and $\nabla\cdot\mathbf F = P_x+Q_y$. We write $P_y$ for
$\partial P/\partial y$ when no confusion is possible.

The mnemonic for the curl is the formal determinant

$$\nabla\times\mathbf F =
\begin{vmatrix}
\mathbf i & \mathbf j & \mathbf k\\[2pt]
\partial_x & \partial_y & \partial_z\\[2pt]
P & Q & R
\end{vmatrix},$$

expanded along the first row, with the middle term negated as the determinant rule requires.

### 5.7 Parametrised surfaces

Let $D\subseteq\mathbb{R}^2$ be a region with piecewise smooth boundary. A **parametrised surface** is a
$C^1$ map $\mathbf r:D\to\mathbb{R}^3$, $\mathbf r(u,v) = (x(u,v),y(u,v),z(u,v))$, whose image is the
surface $S$. It is **regular** at $(u,v)$ if

$$\mathbf r_u\times\mathbf r_v \ne \mathbf 0 ,$$

and regular on $D$ if this holds at every interior point. At a regular point the vectors $\mathbf r_u$ and
$\mathbf r_v$ span the **tangent plane**, and

$$\mathbf n = \frac{\mathbf r_u\times\mathbf r_v}{\lVert\mathbf r_u\times\mathbf r_v\rVert}$$

is a unit normal. The surface is **smooth** if it has a regular parametrisation, and **piecewise smooth**
if it is a finite union of smooth pieces meeting along curves.

A **graph** $z = g(x,y)$ over a plane region $D$ is parametrised by
$\mathbf r(x,y) = (x,y,g(x,y))$, and then $\mathbf r_x\times\mathbf r_y = (-g_x,-g_y,1)$.

An **orientation** of a smooth surface is a continuous choice of unit normal $\mathbf n$. A surface that
admits one is **orientable**; it then admits exactly two, $\mathbf n$ and $-\mathbf n$. A **closed
surface** is the boundary of a solid region; its **outward orientation** is the one pointing away from the
solid.

### 5.8 Surface integrals

Let $S$ be a piecewise smooth surface with regular parametrisation $\mathbf r:D\to\mathbb{R}^3$ and let $f$
be continuous on $S$. The **surface integral of a scalar field** is

$$\iint_S f\,dS = \iint_D f\bigl(\mathbf r(u,v)\bigr)\,\lVert\mathbf r_u\times\mathbf r_v\rVert\,du\,dv ,$$

so that $\iint_S 1\,dS$ is the **surface area** of $S$. The quantity
$dS = \lVert\mathbf r_u\times\mathbf r_v\rVert\,du\,dv$ is the **area element**.

Let $\mathbf F$ be a continuous vector field on an open set containing the oriented surface $S$ with unit
normal $\mathbf n$. The **surface integral of a vector field**, or **flux**, is

$$\iint_S \mathbf F\cdot d\mathbf S
= \iint_S \mathbf F\cdot\mathbf n\,dS
= \iint_D \mathbf F\bigl(\mathbf r(u,v)\bigr)\cdot\bigl(\mathbf r_u\times\mathbf r_v\bigr)\,du\,dv ,$$

where the last expression uses the orientation induced by the parametrisation. Reversing the normal, or
swapping $u$ and $v$, changes the sign. The vector area element is
$d\mathbf S = \mathbf n\,dS = (\mathbf r_u\times\mathbf r_v)\,du\,dv$; it is *not* a unit vector.

For a graph $z=g(x,y)$ with the **upward** orientation,
$d\mathbf S = (-g_x,-g_y,1)\,dx\,dy$; with the downward orientation the sign is reversed. For a closed
surface the default is the outward normal.

## 6. Mathematical Notation

| Symbol | Read as | Meaning |
|---|---|---|
| $\mathbf F$, $\mathbf G$ | field $F$ | vector field, usually $C^1$ |
| $f$, $\phi$ | scalar field $f$, potential phi | real-valued functions |
| $\mathbf r(t)$ | position vector | parametrisation of a curve |
| $\mathbf r(u,v)$ | position on a surface | parametrisation of a surface |
| $C$, $-C$ | curve $C$, reversed curve | oriented curve and its reverse |
| $\partial D$ | boundary of $D$ | the boundary curve of a plane region |
| $\partial S$ | boundary of $S$ | the boundary curve of a surface |
| $\partial V$ | boundary of $V$ | the boundary surface of a solid |
| $ds$ | arc length element | $\lVert\mathbf r'(t)\rVert\,dt$ |
| $d\mathbf r$ | vector line element | $\mathbf r'(t)\,dt$ |
| $dS$ | area element | $\lVert\mathbf r_u\times\mathbf r_v\rVert\,du\,dv$ |
| $d\mathbf S$ | vector area element | $\mathbf n\,dS$, not a unit vector |
| $\mathbf T$ | unit tangent | $\mathbf r'/\lVert\mathbf r'\rVert$ |
| $\mathbf n$ | unit normal | chosen orientation of a surface |
| $\int_C f\,ds$ | integral of $f$ over $C$ with respect to arc length | scalar line integral |
| $\int_C \mathbf F\cdot d\mathbf r$ | line integral of $\mathbf F$ along $C$ | work or circulation |
| $\oint_C$ | integral around a closed curve | circulation |
| $\iint_S \mathbf F\cdot d\mathbf S$ | flux of $\mathbf F$ through $S$ | vector surface integral |
| $\nabla f$ | gradient of $f$ | $(f_x,f_y,f_z)$ |
| $\nabla\cdot\mathbf F$ | divergence of $\mathbf F$ | scalar, $P_x+Q_y+R_z$ |
| $\nabla\times\mathbf F$ | curl of $\mathbf F$ | vector, $(\nabla\times\mathbf F)$ above |
| $\nabla^2 f$ | Laplacian | $\nabla\cdot\nabla f = f_{xx}+f_{yy}+f_{zz}$ |
| $\mathbf i,\mathbf j,\mathbf k$ | standard basis | $\mathbf e_1,\mathbf e_2,\mathbf e_3$ |
| $P_x$, $P_y$, $P_z$ | partial derivatives | $\partial P/\partial x$, etc. |
| $\lVert\mathbf v\rVert$ | norm of $\mathbf v$ | Euclidean length |
| $D$ | plane region | integration domain for double integrals |
| $V$ | solid region | integration domain for triple integrals |
| $\mathbf x_0$ | base point | fixed point in a domain, used to define a potential |
| $r$ | distance from the origin | $r=\lVert\mathbf x\rVert$ in $\mathbb{R}^3$ |
| $\rho,\phi,\theta$ | spherical coordinates | radius, polar angle, azimuth |
| $u,v$ | surface parameters | coordinates on a parametrised surface |
| $d\omega$ | exterior derivative | differential-form generalisation of grad, curl, div |
