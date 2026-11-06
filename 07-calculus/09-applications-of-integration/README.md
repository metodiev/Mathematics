# Applications of Integration

> [Calculus](../README.md) · Level: Advanced · Prerequisites: [The Fundamental Theorem of Calculus](../07-fundamental-theorem-of-calculus/README.md), [Techniques of Integration](../08-techniques-of-integration/README.md), [Applications of Derivatives](../05-applications-of-derivatives/README.md), [Trigonometry](../../05-trigonometry/README.md) · Estimated time: 9 h

## 1. Introduction

Integration is a machine for adding up infinitely many small contributions. In
[Integrals](../06-integrals/README.md) the contributions were rectangles under a graph and the machine
produced signed area. In this topic the same machine produces lengths, volumes, masses, forces, work,
centres of mass, moments of inertia and probabilities. The integrand changes; the architecture does not.

Every application in this topic is built from four decisions:

1. **What is the small quantity?** A thin strip of area, a flat slice of volume, a lamina of mass, a
   horizontal strip of a submerged plate, a slice of time, a small interval of probability.
2. **Which variable indexes it?** The variable of integration is chosen so that the slice is described by
   one formula. Sometimes that is $x$, sometimes $y$, sometimes $t$, sometimes the depth $h$.
3. **What is the element?** The small quantity expressed as (a density) $\times$ (a differential):
   $dA=(f-g)\,dx$, $dV=A(x)\,dx$, $dW=F(x)\,dx$, $dF=\rho g h\,w(h)\,dh$, $dP=f(x)\,dx$.
4. **What are the limits?** They come from the geometry — the intersections of the curves, the endpoints
   of the plate, the depth of the tank — and they are values of the *chosen* variable.

Almost every error students make in this topic happens in steps 2–4, not in the integration. The
integral $\int_0^1(x-x^2)\,dx=\frac16$ takes ten seconds; deciding that the limits are $0$ and $1$, that
the top curve is $y=x$, and that the variable is $x$ takes the thought. This tutorial therefore spends
most of its space on **setting up** integrals, and treats the evaluation as the routine step it is.

The unity behind the formulas is worth stating at the outset. Area, volume, mass, work, hydrostatic
force, probability and expectation are all of the form

$$Q=\int_a^b q(x)\,dx,$$

where $q(x)$ is a *density*: quantity per unit of the variable $x$. Area has density $f-g$ (height per
unit width), volume has density $A(x)$ (area per unit length), mass has density $\rho A(x)$,
probability has density $f_X(x)$, and so on. The only thing that changes from section to section is what
the density is and which variable it is measured in.

This topic assumes that definite integrals exist and that the Fundamental Theorem computes them. It does
not assume any physics beyond $F=ma$, $W=Fd$, $p=F/A$ and "mass $=$ density $\times$ volume"; each
physical formula used is stated and explained where it first appears.

## 2. Prerequisites

**From the integral** ([Integrals](../06-integrals/README.md))

* The Riemann integral as the limit of Riemann sums, and the fact that continuous functions are
  integrable.
* Linearity, additivity over intervals, monotonicity, and the estimate
  $m(b-a)\le\int_a^b f\le M(b-a)$.
* The Mean Value Theorem for integrals: if $f$ is continuous on $[a,b]$, there is $c\in[a,b]$ with
  $f(c)=\dfrac{1}{b-a}\int_a^b f$.
* Area between curves as $\int_a^b(\text{top}-\text{bot})\,dx$ — the simplest case of this topic.

**From the Fundamental Theorem** ([The Fundamental Theorem of Calculus](../07-fundamental-theorem-of-calculus/README.md))

* Both parts of the FTC, and the fact that a continuous function has an antiderivative.
* The net change theorem, and the use of integrals to accumulate a rate.
* Differentiation of integrals with variable limits.

**From differentiation** ([Applications of Derivatives](../05-applications-of-derivatives/README.md))

* The Mean Value Theorem: if $f$ is continuous on $[a,b]$ and differentiable on $(a,b)$, there is
  $c\in(a,b)$ with $f'(c)=\dfrac{f(b)-f(a)}{b-a}$. This is the engine behind the arc-length formula.
* The derivative as the slope of the tangent, and the chain rule.

**From techniques** ([Techniques of Integration](../08-techniques-of-integration/README.md))

* Substitution, integration by parts, trigonometric integrals and substitutions, partial fractions.
* The standard antiderivatives, in particular
  $\int\sec x\,dx=\ln|\sec x+\tan x|+C$ and
  $\int\dfrac{dx}{x^2+a^2}=\dfrac1a\arctan\dfrac xa+C$.

**From geometry and trigonometry**

* Areas of rectangles, triangles and circles; volumes of prisms, cylinders, cones, pyramids and spheres
  ([Solid Geometry](../../04-geometry/05-solid-geometry/README.md)).
* Similar triangles, which convert a width at one height into a width at another.
* The identities $\cos^2\theta+\sin^2\theta=1$, $\sec^2\theta=1+\tan^2\theta$, and the half-angle
  formulas ([Trigonometric Identities](../../05-trigonometry/03-trigonometric-identities/README.md)).

**From algebra**

* Solving polynomial equations for intersection points, completing the square, and the equation of a
  circle ([Exponential and Logarithmic Functions](../../03-algebra/12-exponential-and-logarithmic-functions/README.md)
  covers the exponential manipulation used in the probability examples).

No prior knowledge of physics, probability or economics is assumed: the needed definitions are given in
§5 and repeated in the relevant subsections of §7.

## 3. Learning Objectives

After working through this tutorial you will be able to:

1. State the slice principle precisely and use it to justify every formula in the topic as a limit of
   Riemann sums.
2. Set up and evaluate the area between two curves, choosing vertical or horizontal strips according to
   which description gives a single integral.
3. Derive and apply the disk and washer formulas for volumes of revolution, including about axes other
   than the coordinate axes.
4. Derive the cylindrical-shell formula from the exact volume of a thin shell, and choose between shells
   and washers on the basis of the region, not on habit.
5. Derive the arc-length formula from the distance formula and the Mean Value Theorem, and compute arc
   lengths of graphs and simple parametric curves.
6. State the surface-of-revolution formulas, derive them from the frustum area, and explain why the
   factor $\sqrt{1+(f')^2}$ must not be omitted.
7. Compute average values, and distinguish the arithmetic mean of a function from the mean of its
   values at finitely many sample points.
8. Set up work integrals for variable forces, springs, pumping fluids and lifting cables, with correct
   limits and distances.
9. Compute the centroid of a lamina or region by the moment formulas, and use Pappus's theorem as a
   consistency check.
10. Define moments of inertia and compute them for rods, laminae and solids of revolution, using the
    parallel-axis theorem.
11. Compute the hydrostatic force on a vertical plate as an integral of pressure over depth.
12. Use a probability density function to compute probabilities and expectations as integrals, and
    interpret expectation as a centroid.
13. Compute consumer and producer surplus from linear or quadratic demand and supply curves.

## 4. Intuition

**The loaf.** A loaf of bread is not uniform: its cross-section changes along its length. To find its
volume, cut it into thin slices perpendicular to its length. Each slice is almost a flat slab of area
$A(x)$ and thickness $\Delta x$, so its volume is almost $A(x)\Delta x$. The total volume is the sum of
the slab volumes, and refining the slices makes the approximation exact. The integral is the instruction
"add $A(x)\,dx$ from one end to the other".

**The onion.** A solid of revolution can also be peeled. A thin cylindrical shell at radius $r$ has
circumference $2\pi r$, height $h(r)$ and thickness $\Delta r$, so its volume is almost
$2\pi r\,h(r)\,\Delta r$. Summing over radii gives the shell formula. Slicing and peeling are two ways
of chopping the same solid; both give its volume, and choosing the cheaper chop is the art.

**The surveyor.** A surveyor measures the width of a winding river at many positions along its bank. The
area is the sum of widths times spacings — a Riemann sum. Replacing the spacings by $dx$ and the sum by
an integral is exactly the passage from a table of measurements to a formula.

**The rope and the pulley.** Lifting a rope of uniform weight is not the same as lifting a compact mass
of the same weight: the bottom of the rope moves farther than the top. Slice the rope into pieces, and
each piece is lifted through its own distance. The integral adds up the different distances. Every
"pumping" or "lifting" problem is this observation in disguise.

**The choice of variable.** A region can be described by vertical strips or by horizontal strips. The
area is the same number; one description may take one integral and the other two. A region can be
revolved about the $x$-axis and computed with disks (integrating in $x$) or with shells (integrating in
$y$). The geometry does not change when the variable changes, but the algebra does. **Choose the
variable that makes the slice a single formula.**

**Why the surface-area formula is not the volume formula.** Volume by shells is
$\int 2\pi r h\,dr$; surface area is $\int 2\pi r\,ds$, where $ds=\sqrt{1+(f')^2}\,dx$ is the *slant*
length of the slice. A thin strip of a surface is tilted, and its area depends on the tilt. Dropping the
slant factor computes the area of the projection, not of the surface. This is the single most common
formula error in the topic.

**Probability as area.** A probability density $f$ is a curve whose total area is $1$. The probability
that $X$ lies between $a$ and $b$ is the area under $f$ over $[a,b]$. The mean is the $x$-coordinate of
the centroid of that area. Thus §7.10 and §7.13 are the same calculation in different language.

## 5. Formal Definition

### 5.1 The slice principle

Let $[a,b]$ be an interval and let $Q$ be a quantity that is accumulated over it. Suppose that for each
subinterval $[u,v]\subseteq[a,b]$ the contribution $\Delta Q$ of that subinterval can be written

$$\Delta Q=q(\xi)(v-u)+e(u,v),$$

where $\xi\in[u,v]$, $q$ is a function continuous on $[a,b]$, and the errors satisfy

$$\sum_{k=1}^{n}\lvert e(x_{k-1},x_k)\rvert\longrightarrow0
\qquad\text{as the mesh }\max_k(x_k-x_{k-1})\to0.$$

Then $Q=\displaystyle\int_a^b q(x)\,dx$.

*Why.* For a partition $a=x_0<x_1<\cdots<x_n=b$ with sample points $\xi_k$, the total is
$Q=\sum_k q(\xi_k)\Delta x_k+\sum_k e(x_{k-1},x_k)$. The first sum is a Riemann sum for the continuous
function $q$, which converges to $\int_a^b q$; the second tends to $0$ by hypothesis. Hence
$Q=\int_a^b q$. $\blacksquare$

In practice the error is $O((\Delta x)^2)$ per slice, so the total error is $O(\Delta x)$ and vanishes.
Every formula below is obtained by identifying $q$. The notation $dQ=q(x)\,dx$ is shorthand for this
limiting statement; it is **not** a licence to treat $dx$ as a number.

### 5.2 Volume by slicing

Let a solid $S$ lie between the planes $x=a$ and $x=b$. For each $x\in[a,b]$ let $A(x)$ be the area of
the cross-section of $S$ by the plane through $x$ perpendicular to the $x$-axis. If $A$ is continuous,
the **volume** of $S$ is defined to be

$$V=\int_a^b A(x)\,dx.$$

For a solid of revolution about the $x$-axis generated by $0\le g(x)\le f(x)$, the cross-section at $x$
is the annulus with outer radius $f(x)$ and inner radius $g(x)$, so
$A(x)=\pi\bigl(f(x)^2-g(x)^2\bigr)$ and the washer formula follows. When $g=0$ the annulus is a disk.

The definition is forced by the slice principle: a slab between $x$ and $x+\Delta x$ has volume
approximately $A(x)\Delta x$, with error bounded by (variation of $A$) $\times\Delta x$, which is
negligible after summation. This is Cavalieri's principle in integral form.

### 5.3 Mass, centre of mass and centroid

Let a lamina occupy a region $R$ in the plane and have **area density** $\rho(x,y)$ (mass per unit
area), assumed continuous. Its **mass** is

$$M=\iint_R \rho\,dA,$$

which in this topic is always evaluated as a single integral by slicing: for a region between
$y=g(x)$ and $y=f(x)$,

$$M=\int_a^b\rho(x)\bigl(f(x)-g(x)\bigr)\,dx$$

when $\rho$ depends only on $x$, and the double integral is not needed. The **moments** about the
coordinate axes are

$$M_y=\iint_R x\rho\,dA,\qquad M_x=\iint_R y\rho\,dA,$$

and the **centre of mass** is $(\bar x,\bar y)=(M_y/M,\,M_x/M)$. When $\rho$ is constant the centre of
mass depends only on the shape and is called the **centroid**; the constant cancels.

For a one-dimensional object (a rod or wire) on the $x$-axis with linear density $\lambda(x)$, the same
definitions read

$$M=\int_a^b\lambda(x)\,dx,\qquad \bar x=\frac{1}{M}\int_a^b x\lambda(x)\,dx.$$

### 5.4 Average value

If $f$ is continuous on $[a,b]$, its **average value** is

$$\bar f=\frac{1}{b-a}\int_a^b f(x)\,dx.$$

The Mean Value Theorem for integrals says that a continuous $f$ attains this value somewhere on
$[a,b]$; the average is therefore a value of the function, not merely a formal quotient. If the
"importance" of each point is given by a weight $w(x)>0$, the **weighted average** is
$\int f w/\int w$.

### 5.5 Work

If a force $F(x)$ acts along a straight line in the direction of motion, the **work** done in moving an
object from $x=a$ to $x=b$ is

$$W=\int_a^b F(x)\,dx.$$

The definition is the slice principle applied to $dW=F(x)\,dx$: over a short displacement the force is
approximately constant, and work is force times displacement. Work has the dimensions of force times
length (joules, in SI).

### 5.6 Hydrostatic pressure and force

At depth $h$ below the surface of a fluid at rest, the **gauge pressure** is

$$p=\rho g h,$$

where $\rho$ is the fluid density and $g$ the acceleration due to gravity. The pressure acts equally in
all directions and perpendicular to any surface. On a thin horizontal strip of a vertical plate, of
width $w(h)$ and height $dh$, at depth $h$, the force is therefore

$$dF=p\,dA=\rho g h\,w(h)\,dh,\qquad F=\int_{h_1}^{h_2}\rho g h\,w(h)\,dh.$$

The limits are the shallowest and deepest depths of the submerged part of the plate.

### 5.7 Probability density functions

A **probability density function** (PDF) on $\mathbb{R}$ is a function $f_X\ge0$ with

$$\int_{-\infty}^{\infty}f_X(x)\,dx=1.$$

For $a\le b$,

$$\Pr(a\le X\le b)=\int_a^b f_X(x)\,dx,$$

and for a function $g$ for which the integral exists,

$$\mathbb{E}[g(X)]=\int_{-\infty}^{\infty}g(x)f_X(x)\,dx.$$

The integrals over unbounded intervals are improper and are defined as limits; a full treatment is in
[Improper Integrals](../10-improper-integrals/README.md). In this topic they are computed as limits of
proper integrals over $[-R,R]$ or $[0,R]$ as $R\to\infty$. The **expectation** is
$\mu=\mathbb{E}[X]$, and the **variance** is
$\operatorname{Var}(X)=\mathbb{E}[(X-\mu)^2]=\mathbb{E}[X^2]-\mu^2$.

### 5.8 Consumer and producer surplus

Let $D(q)$ be the price at which consumers will buy quantity $q$ (the inverse demand curve, decreasing)
and $S(q)$ the price at which producers will supply quantity $q$ (the inverse supply curve, increasing).
The **equilibrium** $(q^*,p^*)$ satisfies $D(q^*)=S(q^*)=p^*$. The **consumer surplus** is

$$CS=\int_0^{q^*}\bigl(D(q)-p^*\bigr)\,dq,$$

and the **producer surplus** is

$$PS=\int_0^{q^*}\bigl(p^*-S(q)\bigr)\,dq.$$

Each is the area between a curve and the horizontal line at the equilibrium price; economically it is the
total gain from trade that the corresponding side of the market enjoys.

## 6. Mathematical Notation

| Symbol | Read as | Meaning in this topic |
|---|---|---|
| $dA$ | element of area | area of a thin strip or patch |
| $dV$ | element of volume | volume of a thin slice or shell |
| $dm$ | element of mass | $\rho\,dV$ |
| $dW$ | element of work | $F\,dx$ |
| $dF$ | element of force | $p\,dA$ for a fluid |
| $dP$ | element of probability | $f_X(x)\,dx$ |
| $A(x)$ | cross-sectional area | area of the slice at $x$ |
| $S$ | surface area | area of a surface of revolution |
| $L$ | arc length | length of a curve |
| $\bar f$ | average value of $f$ | $\frac{1}{b-a}\int_a^b f$ |
| $\bar x,\bar y$ | centroid coordinates | $M_y/M$, $M_x/M$ |
| $M_x,M_y$ | moments about the axes | $\int y\,dm$, $\int x\,dm$ |
| $I_x,I_y$ | moments of inertia | $\int y^2\,dm$, $\int x^2\,dm$ |
| $k$ | radius of gyration | $\sqrt{I/M}$ |
| $\rho$ | rho | mass density (mass per volume or area) |
| $\gamma$ | gamma | weight density $\rho g$ (weight per volume) |
| $\lambda$ | lambda | linear density (mass per length); also an exponential rate |
| $p$ | pressure | force per unit area; also a price |
| $h$ | depth | distance below the fluid surface |
| $f_X$ | density of $X$ | probability density function |
| $\mathbb{E}[X]$ | expectation of $X$ | $\int x f_X(x)\,dx$ |
| $\operatorname{Var}(X)$ | variance of $X$ | $\mathbb{E}[X^2]-\mu^2$ |
| $D(q),S(q)$ | demand, supply | inverse demand and supply curves |
| $q^*,p^*$ | equilibrium quantity, price | where $D(q^*)=S(q^*)=p^*$ |
| $CS,PS$ | consumer, producer surplus | areas defined in §5.8 |

**Reading aloud.** "$V=\int_a^b A(x)\,dx$" is read "the volume is the integral from $a$ to $b$ of the
cross-sectional area at $x$ with respect to $x$". "$dF=\rho g h\,w(h)\,dh$" is read "the element of force
is rho times g times the depth times the width at that depth, times the element of depth". The symbol
$\rho g$ is often written $\gamma$ and called the *weight density*; for water,
$\gamma\approx9800\ \mathrm{N/m^3}$ in SI.

## 7. Core Concepts

### 7.1 The set-up ritual

Every problem in this topic is solved in the same five steps. Doing them in this order prevents most
errors.

1. **Draw.** Sketch the curves, shade the region or draw the solid, and draw the axis of revolution or
   the fluid surface. Mark the intersection points with their coordinates.
2. **Choose the variable.** Decide the direction in which you will slice. A slice must have *one*
   formula for its size across the whole range; if it does not, split the integral.
3. **Write the element.** Express the size of a typical slice in terms of the variable and its
   differential. For an area, the element has the form (length)$\,dx$; for a volume,
   (area)$\,dx$; for a force, (pressure $\times$ width)$\,dh$.
4. **Find the limits.** Solve for the intersections, read off the endpoints, or project the solid onto
   the axis. The limits are values of the chosen variable; if you change the variable you must change the
   limits (or substitute back).
5. **Integrate and sanity-check.** Check the sign, the dimensions (a volume must be a length cubed; a
   force must be a mass times an acceleration), and one limiting case (a radius going to zero, a height
   going to zero, a density equal to a constant). If a known formula is available — a cone, a sphere, a
   rectangle — compare.

**A note on $dx$ and $dy$.** In this topic $dx$ and $dy$ are bookkeeping devices for the slice
thickness, not numbers. The precise meaning is the slice principle of §5.1: the integral is a limit of
Riemann sums, and the element is the term of the sum. Writing $dV=2\pi xh\,dx$ is shorthand for "the
volume of the slice between $x$ and $x+\Delta x$ is $2\pi xh\,\Delta x$ plus a negligible error". The
error is what the derivation checks.

### 7.2 Area between curves

Let $f$ and $g$ be continuous on $[a,b]$ with $f(x)\ge g(x)$ there. Partition $[a,b]$ and erect on the
$k$-th subinterval a rectangle of height $f(\xi_k)-g(\xi_k)$ and width $\Delta x_k$. Its area is
$(f(\xi_k)-g(\xi_k))\Delta x_k$. The union of the rectangles approximates the region between the graphs,
and the sum is a Riemann sum for $f-g$. Therefore

$$A=\int_a^b\bigl(f(x)-g(x)\bigr)\,dx. \tag{7.2.1}$$

If the curves cross, $f-g$ changes sign and the integral gives *net* area. The geometric area is
$\int_a^b\lvert f-g\rvert\,dx$, computed by splitting at the crossing points. If the region is described
more naturally by horizontal strips, with $x=R(y)$ on the right and $x=L(y)$ on the left for
$c\le y\le d$, then

$$A=\int_c^d\bigl(R(y)-L(y)\bigr)\,dy. \tag{7.2.2}$$

**Choosing the variable.** Vertical strips require the top and bottom to be single functions of $x$;
horizontal strips require the right and left to be single functions of $y$. For the region between
$x=y^2$ and $x=2-y^2$, vertical strips need two integrals (the "top" changes at the intersections), while
horizontal strips need one. The area is the same; the work differs.

### 7.3 Volumes by slicing

Let a solid lie between $x=a$ and $x=b$, and let $A(x)$ be the area of its cross-section by the plane
perpendicular to the $x$-axis at $x$. The slab between $x$ and $x+\Delta x$ is almost a prism of base
$A(x)$ and thickness $\Delta x$, so its volume is $A(x)\Delta x$ up to an error that is smaller than
(constant)$\times(\Delta x)^2$. Summing and passing to the limit,

$$V=\int_a^b A(x)\,dx. \tag{7.3.1}$$

This is the most general volume formula in the topic; the disk, washer and shell formulas are special
cases. It also handles solids that are not surfaces of revolution: if the base is a region in the
$xy$-plane and the cross-sections perpendicular to the $x$-axis are squares of side $s(x)$, then
$A(x)=s(x)^2$; if they are equilateral triangles, $A(x)=\frac{\sqrt3}{4}s(x)^2$; if they are semicircles
with diameter $s(x)$, $A(x)=\frac{\pi}{8}s(x)^2$. The hard part is always expressing $s(x)$ from the
base.

### 7.4 Disks and washers

Let $0\le g(x)\le f(x)$ on $[a,b]$, and revolve the region between the graphs about the $x$-axis. The
cross-section at $x$ is an annulus (a washer) with outer radius $f(x)$ and inner radius $g(x)$, so

$$A(x)=\pi f(x)^2-\pi g(x)^2,$$

and therefore

$$V=\pi\int_a^b\Bigl(f(x)^2-g(x)^2\Bigr)\,dx. \tag{7.4.1}$$

When $g=0$ the washer is a disk and $V=\pi\int_a^b f(x)^2\,dx$. When the axis of revolution is the
horizontal line $y=k$, the radii are the *distances* to the axis, $\lvert f(x)-k\rvert$ and
$\lvert g(x)-k\rvert$, and

$$V=\pi\int_a^b\Bigl(\bigl(f(x)-k\bigr)^2-\bigl(g(x)-k\bigr)^2\Bigr)\,dx. \tag{7.4.2}$$

The squares make the absolute values unnecessary, but the region must lie entirely on one side of the
axis for the washer to have a hole of the stated inner radius; if the region straddles the axis, split
the region or use shells.

If the region is described as $L(y)\le x\le R(y)$ for $c\le y\le d$ and is revolved about the $y$-axis,
the same argument with horizontal slices gives

$$V=\pi\int_c^d\Bigl(R(y)^2-L(y)^2\Bigr)\,dy. \tag{7.4.3}$$

**Derivation of (7.4.1).** The cross-section is the set of points at distance between $g(x)$ and $f(x)$
from the axis, which is an annulus of area $\pi f(x)^2-\pi g(x)^2$. Substituting in (7.3.1) gives the
formula. $\blacksquare$

### 7.5 Cylindrical shells

Let $0\le a\le x\le b$ and $0\le g(x)\le f(x)$, and revolve the region between the graphs about the
$y$-axis. Write $h(x)=f(x)-g(x)$ for the height of the region at $x$. The part of the solid between radii
$x$ and $x+\Delta x$ is a cylindrical shell of thickness $\Delta x$ and height varying between $h(x)$ and
$h(x+\Delta x)$. By the Mean Value Theorem for integrals applied to the continuous function $h$ on
$[x,x+\Delta x]$, its exact volume is

$$\Delta V=\pi\Bigl((x+\Delta x)^2-x^2\Bigr)h(\xi)
=2\pi x\,h(\xi)\,\Delta x+\pi h(\xi)(\Delta x)^2 \tag{7.5.1}$$

for some $\xi\in[x,x+\Delta x]$. The first term is a Riemann-sum term for $2\pi xh(x)$; the second is
$O((\Delta x)^2)$ per slice and contributes $O(\Delta x)$ in total. Hence

$$V=2\pi\int_a^b x\,h(x)\,dx
=2\pi\int_a^b x\bigl(f(x)-g(x)\bigr)\,dx. \tag{7.5.2}$$

The factor $x$ is the **radius** of the shell, not a height and not an area. It must be the distance from
the slice to the axis of revolution. About the vertical line $x=c$,

$$V=2\pi\int_a^b\lvert x-c\rvert\,h(x)\,dx. \tag{7.5.3}$$

For revolution about the $x$-axis with the region described as $L(y)\le x\le R(y)$, the horizontal slice
at height $y$ has radius $y$ and height $R(y)-L(y)$, so

$$V=2\pi\int_c^d y\bigl(R(y)-L(y)\bigr)\,dy. \tag{7.5.4}$$

**Why the middle circumference is exact in the limit.** The exact shell volume in (7.5.1) uses the
circumference at the inner radius $x$, not at the midpoint $x+\Delta x/2$; the difference is the
second-order term $\pi h(\Delta x)^2$. In the limit both choices give the same integral. This is why
"circumference $\times$ height $\times$ thickness" is legitimate: the error is quadratic per slice, and
quadratic errors disappear when summed against $n$ slices of size $1/n$.

**Choosing between washers and shells.** The two methods compute the same volume; choose the one whose
slice is easier to describe.

| Region given as | Axis of revolution | Convenient method |
|---|---|---|
| $y=f(x)$ over $x\in[a,b]$ | horizontal ($y=0$ or $y=k$) | washers, integrate in $x$ |
| $y=f(x)$ over $x\in[a,b]$ | vertical ($x=0$ or $x=c$) | shells, integrate in $x$ |
| $x=R(y)$ over $y\in[c,d]$ | vertical | washers, integrate in $y$ |
| $x=R(y)$ over $y\in[c,d]$ | horizontal | shells, integrate in $y$ |

If the region touches the axis, the washer has no hole; if the region is far from the axis, shells often
give a simpler integrand.

### 7.6 Arc length

Let $f$ be continuously differentiable on $[a,b]$. Partition $[a,b]$ at
$a=x_0<x_1<\cdots<x_n=b$ and join consecutive points on the graph by straight segments. The $k$-th chord
has length

$$\sqrt{(\Delta x_k)^2+(\Delta y_k)^2}
=\sqrt{1+\left(\frac{\Delta y_k}{\Delta x_k}\right)^2}\Delta x_k .$$

By the Mean Value Theorem applied to $f$ on $[x_{k-1},x_k]$, there is $\xi_k\in(x_{k-1},x_k)$ with
$\Delta y_k/\Delta x_k=f'(\xi_k)$. Hence the polygonal length is

$$\sum_{k=1}^n\sqrt{1+f'(\xi_k)^2}\,\Delta x_k,$$

which is a Riemann sum for the continuous function $\sqrt{1+f'^2}$. Therefore

$$L=\int_a^b\sqrt{1+f'(x)^2}\,dx. \tag{7.6.1}$$

If the curve is given as $x=g(y)$ for $c\le y\le d$, the same argument with the roles of $x$ and $y$
exchanged gives

$$L=\int_c^d\sqrt{1+g'(y)^2}\,dy. \tag{7.6.2}$$

For a parametric curve $(x(t),y(t))$ with continuous derivatives on $[\alpha,\beta]$, the chord between
$t$ and $t+\Delta t$ has length approximately
$\sqrt{x'(t)^2+y'(t)^2}\,\Delta t$, so

$$L=\int_\alpha^\beta\sqrt{x'(t)^2+y'(t)^2}\,dt. \tag{7.6.3}$$

Formula (7.6.3) is stated here for reference; its derivation is the same distance-formula argument, with
the Mean Value Theorem applied to each coordinate. The hypothesis that the derivative be continuous (or
at least that the curve be rectifiable with the integral finite) matters: the formula can fail for
pathological curves, which is a theme of real analysis.

**Why the Mean Value Theorem is needed.** Without it, the chord length would involve
$(\Delta y/\Delta x)^2$ evaluated at an unknown point, and the sum would not be a Riemann sum of a
known function. The MVT replaces the secant slope by a derivative at an interior point, converting the
polygonal length into a Riemann sum.

### 7.7 Area of a surface of revolution

Let $f\ge0$ be continuously differentiable on $[a,b]$, and revolve its graph about the $x$-axis. On the
subinterval $[x_{k-1},x_k]$, the surface is approximated by the frustum of a cone with slant height
$\ell_k=\sqrt{(\Delta x_k)^2+(\Delta y_k)^2}$ and radii $f(x_{k-1})$ and $f(x_k)$. The lateral area of a
frustum is $\pi(r_1+r_2)\ell$ (the average circumference $2\pi\frac{r_1+r_2}{2}$ times the slant height).
By the Mean Value Theorem, $\ell_k=\sqrt{1+f'(\xi_k)^2}\,\Delta x_k$, and by continuity
$f(x_{k-1})+f(x_k)\to2f(x)$. Summing gives

$$S=2\pi\int_a^b f(x)\sqrt{1+f'(x)^2}\,dx. \tag{7.7.1}$$

For revolution about the $y$-axis, the radius of the typical band is $x$ rather than $f(x)$:

$$S=2\pi\int_a^b x\sqrt{1+f'(x)^2}\,dx. \tag{7.7.2}$$

**Derivation sketch of the frustum formula.** A cone of base radius $r$ and slant height $\ell$ has lateral
area $\pi r\ell$; a frustum is the difference of two similar cones, and the similar-triangle ratio gives
lateral area $\pi(r_1+r_2)\ell$ where $\ell$ is the slant height of the frustum. Substituting the
first-order approximations $r_1+r_2\approx2f(x)$ and
$\ell\approx\sqrt{1+f'(x)^2}\,\Delta x$, then summing and passing to the limit, gives (7.7.1).
$\blacksquare$

**The classic error.** The area is **not** $\int2\pi f(x)\,dx$. The latter is the area of the projection
of the surface onto the cylinder of radius $f(x)$; it omits the tilt factor
$\sqrt{1+f'(x)^2}\ge1$. For a vertical line segment ($f$ constant) the two agree, which is why the error
can survive simple checks. For a sphere the correct formula gives $4\pi R^2$; the incorrect one gives
$2\pi R\cdot2R=4\pi R^2$ as well — a coincidence (the sphere is the one surface for which the two
integrals agree), and a dangerous one to generalise from. For a cone they disagree.

### 7.8 Average value

The average of $n$ numbers is their sum divided by $n$. For a continuous function on an interval, the
analogue is the integral divided by the length:

$$\bar f=\frac{1}{b-a}\int_a^b f(x)\,dx. \tag{7.8.1}$$

The interpretation: the horizontal line $y=\bar f$ has the same area under it over $[a,b]$ as $f$ does.
A continuous $f$ attains $\bar f$ somewhere (Mean Value Theorem for integrals), so the average is a
genuine value of the function.

Two refinements are common. The **root-mean-square** value is

$$f_{\mathrm{rms}}=\sqrt{\frac{1}{b-a}\int_a^b f(x)^2\,dx}, \tag{7.8.2}$$

which is the average value of $f^2$ followed by a square root; it is the quantity that appears in the
power of an alternating current. The **weighted average** with weight $w>0$ is

$$\bar f_w=\frac{\int_a^b f(x)w(x)\,dx}{\int_a^b w(x)\,dx}. \tag{7.8.3}$$

When $w$ is a probability density, this is the expectation of $f(X)$.

### 7.9 Work

Work is force times displacement when the force is constant. When the force varies along the path, slice
the path: over a displacement $dx$ the force is approximately $F(x)$, so the element of work is
$dW=F(x)\,dx$ and

$$W=\int_a^b F(x)\,dx. \tag{7.9.1}$$

**Springs.** Hooke's law says that the force needed to hold a spring stretched $x$ beyond its natural
length is $F(x)=kx$, with $k$ the spring constant. The work to stretch it from $x=a$ to $x=b$ is
therefore

$$W=\int_a^b kx\,dx=\frac{k}{2}\left(b^2-a^2\right). \tag{7.9.2}$$

Stretching from rest ($a=0$) to $b$ costs $\frac12kb^2$; doubling the stretch costs four times the work.

**Pumping fluids.** Consider a tank whose horizontal cross-section at height $y$ has area $A(y)$, filled
with a fluid of weight density $\gamma=\rho g$ to height $H$, and emptied over the top. The slice of
fluid between $y$ and $y+dy$ has weight $\gamma A(y)\,dy$ and must be lifted a distance $H-y$, so

$$W=\int_0^H\gamma A(y)(H-y)\,dy. \tag{7.9.3}$$

If the fluid is pumped to a point at height $H_0$ above the top, replace $H-y$ by $H_0-y$. If the tank is
only filled to height $h<H$, the upper limit is $h$. The most common error is to use the depth of the
slice below the *surface* in one term and its height above the *bottom* in another; choose one coordinate
system and stay in it.

**Lifting a hanging rope.** A rope of length $L$ and linear weight density $\lambda g$ hangs vertically
with its lower end at the origin and is wound up by its top end. When the top has been raised a distance
$y$, the length still hanging is $L-y$ and its weight is $\lambda g(L-y)$; the work for the next $dy$ is
$\lambda g(L-y)\,dy$. Hence

$$W=\int_0^L\lambda g(L-y)\,dy=\frac{\lambda gL^2}{2}. \tag{7.9.4}$$

Equivalently, the element of rope at distance $z$ below the top is lifted through $z$, and
$\int_0^L\lambda g z\,dz=\lambda gL^2/2$. The two descriptions agree.

**Gravitation.** The force between masses $M$ and $m$ separated by $r$ is $GMm/r^2$. The work needed to
move $m$ from the surface of a body of radius $R$ to infinity is

$$W=\int_R^{\infty}\frac{GMm}{r^2}\,dr=\frac{GMm}{R}, \tag{7.9.5}$$

the escape energy. This is an improper integral, a preview of
[Improper Integrals](../10-improper-integrals/README.md).

### 7.10 Centres of mass and centroids

**Discrete case.** For masses $m_1,\dots,m_n$ at positions $x_1,\dots,x_n$ on a line, the centre of mass
is $\bar x=\sum m_ix_i/\sum m_i$. It is the point at which the system balances: the total moment
$\sum m_i(x_i-\bar x)$ is zero.

**Rod.** For a rod on $[a,b]$ with linear density $\lambda(x)$, the element of mass is
$dm=\lambda(x)\,dx$ and the element of moment about the origin is $x\,dm$. Hence

$$M=\int_a^b\lambda(x)\,dx,\qquad
\bar x=\frac{1}{M}\int_a^b x\lambda(x)\,dx. \tag{7.10.1}$$

**Lamina between two curves.** Let $0\le g(x)\le f(x)$ on $[a,b]$ and let the area density be a constant
$\rho$. The vertical strip at $x$ has area $(f-g)\,dx$, so its mass is $\rho(f-g)\,dx$ and its moment
about the $y$-axis is $x\rho(f-g)\,dx$. The strip's own centroid has $y$-coordinate
$\frac12(f+g)$, so its moment about the $x$-axis is $\frac12(f+g)\rho(f-g)\,dx$. Therefore

$$A=\int_a^b(f-g)\,dx, \tag{7.10.2}$$
$$\bar x=\frac{1}{A}\int_a^b x\bigl(f(x)-g(x)\bigr)\,dx, \tag{7.10.3}$$
$$\bar y=\frac{1}{A}\int_a^b\frac{f(x)^2-g(x)^2}{2}\,dx
=\frac{1}{2A}\int_a^b\bigl(f(x)^2-g(x)^2\bigr)\,dx. \tag{7.10.4}$$

The density $\rho$ cancels throughout; that is why the centroid depends only on the shape. For a region
described by horizontal strips, $L(y)\le x\le R(y)$,

$$A=\int_c^d(R-L)\,dy,\qquad
\bar x=\frac{1}{2A}\int_c^d\bigl(R^2-L^2\bigr)\,dy,\qquad
\bar y=\frac{1}{A}\int_c^d y(R-L)\,dy. \tag{7.10.5}$$

**Checks.** For the rectangle $[0,a]\times[0,b]$, (7.10.2)–(7.10.4) give
$A=ab$, $\bar x=a/2$, $\bar y=b/2$, as expected. For a region symmetric about the line $x=c$, the
formula must give $\bar x=c$; this is a quick check on the algebra.

**Pappus's first theorem.** If a plane region of area $A$ is revolved about an external axis in its plane
(an axis that does not cross the region), the volume of the solid is

$$V=2\pi dA, \tag{7.10.6}$$

where $d$ is the distance from the centroid to the axis. Pappus's second theorem says the area of the
surface generated by a plane curve of length $L$ is $S=2\pi dL$. Both follow from the slice formulas:
for revolution about the $y$-axis, $V=2\pi\int xh\,dx=2\pi A\bar x$. They are excellent consistency
checks, and they turn some difficult integrals into arithmetic.

### 7.11 Moments of inertia

The **moment of inertia** of a mass distribution about an axis is

$$I=\int r^2\,dm, \tag{7.11.1}$$

where $r$ is the distance from the element $dm$ to the axis. It is the rotational analogue of mass: the
kinetic energy of rotation is $\frac12I\omega^2$, and the equation of motion is $I\alpha=\tau$.

**Lamina.** For a uniform lamina between $y=g(x)$ and $y=f(x)$ on $[a,b]$:

* about the $y$-axis, the strip at $x$ is at distance $x$, so
  $$I_y=\int_a^b x^2\bigl(f(x)-g(x)\bigr)\,dx; \tag{7.11.2}$$
* about the $x$-axis, the strip is a vertical segment from $g(x)$ to $f(x)$, and
  $$dI_x=\int_{g(x)}^{f(x)}y^2\,dy\,dx
  =\frac13\Bigl(f(x)^3-g(x)^3\Bigr)dx,$$
  so
  $$I_x=\frac13\int_a^b\Bigl(f(x)^3-g(x)^3\Bigr)dx. \tag{7.11.3}$$

**Solid of revolution about the $x$-axis.** The disk at $x$ has radius $f(x)$, thickness $dx$, mass
$dm=\rho\pi f(x)^2dx$, and moment of inertia about its own diameter (the $x$-axis) equal to
$\frac12dm\,f(x)^2$. Hence

$$I_x=\frac{\pi\rho}{2}\int_a^b f(x)^4\,dx. \tag{7.11.4}$$

**Theorems.** The **parallel-axis theorem** says that for an axis parallel to an axis through the centre
of mass at distance $d$,

$$I=I_{\mathrm{cm}}+Md^2. \tag{7.11.5}$$

The **perpendicular-axis theorem** says that for a thin lamina in the $xy$-plane,

$$I_z=I_x+I_y. \tag{7.11.6}$$

The **radius of gyration** is $k=\sqrt{I/M}$, the distance at which a point mass $M$ would have the same
moment of inertia.

**Example checks.** A uniform rod of length $L$ and mass $M$ about one end:
$I=\int_0^L(M/L)x^2dx=ML^2/3$. About its centre: $ML^2/12$. The parallel-axis theorem gives
$ML^2/12+M(L/2)^2=ML^2/3$, consistent.

### 7.12 Hydrostatic force

At depth $h$ in a fluid at rest, the pressure is $p=\rho gh$. On a vertical plate, consider a horizontal
strip at depth $h$ of width $w(h)$ and height $dh$. Its area is $w(h)\,dh$, the pressure is essentially
constant across it, and the force on it is

$$dF=p\,dA=\rho g h\,w(h)\,dh. \tag{7.12.1}$$

Therefore

$$F=\rho g\int_{h_1}^{h_2}h\,w(h)\,dh, \tag{7.12.2}$$

where $h_1$ and $h_2$ are the shallowest and deepest depths of the plate. The width $w(h)$ must be the
width *at that depth*, which is where the geometry of the plate enters.

**The centroid shortcut.** Since $\int h\,w(h)\,dh=A\bar h$, where $A$ is the plate area and $\bar h$ the
depth of its centroid,

$$F=\rho gA\bar h. \tag{7.12.3}$$

The force on a submerged plane region equals the pressure at its centroid times its area. This is a
theorem, not an approximation, and it is a useful check on an integral. It does **not** say the force acts
at the centroid: the centre of pressure is generally deeper, and for a rectangle with its top at the
surface it is at $\frac23$ of the height.

### 7.13 Probability density functions and expectation

A probability density $f_X$ is a non-negative function whose total integral is $1$. The probability of an
interval is the area under the density over that interval. In this topic we use densities on bounded
intervals (where the integrals are proper) and on half-lines (where they are limits).

**Uniform density on $[a,b]$.** $f_X(x)=1/(b-a)$ there and $0$ elsewhere. Then
$\Pr(c\le X\le d)=(d-c)/(b-a)$ for $a\le c\le d\le b$, and

$$\mathbb{E}[X]=\frac{1}{b-a}\int_a^b x\,dx=\frac{a+b}{2}.$$

The expectation is the midpoint, which is also the centroid of the rectangle under the density.

**Exponential density.** For $\lambda>0$, $f_X(x)=\lambda e^{-\lambda x}$ for $x\ge0$ and $0$ otherwise.
The normalization is

$$\int_0^{\infty}\lambda e^{-\lambda x}dx=\lim_{R\to\infty}\left[-e^{-\lambda x}\right]_0^R
=\lim_{R\to\infty}\left(1-e^{-\lambda R}\right)=1.$$

The mean is

$$\mathbb{E}[X]=\int_0^{\infty}x\lambda e^{-\lambda x}dx
=\lim_{R\to\infty}\left[-xe^{-\lambda x}-\frac1\lambda e^{-\lambda x}\right]_0^R=\frac1\lambda,$$

where the antiderivative is checked by differentiating:
$\frac{d}{dx}\left(-xe^{-\lambda x}-\frac1\lambda e^{-\lambda x}\right)
=\lambda xe^{-\lambda x}$. The second moment is
$\mathbb{E}[X^2]=2/\lambda^2$ (two integrations by parts, or the gamma-function formula of
[Improper Integrals](../10-improper-integrals/README.md)), so
$\operatorname{Var}(X)=2/\lambda^2-1/\lambda^2=1/\lambda^2$.

**General facts.** For any density, $\mathbb{E}[aX+b]=a\mathbb{E}[X]+b$ and
$\operatorname{Var}(aX+b)=a^2\operatorname{Var}(X)$, both immediate from the integral. The expectation of
$g(X)$ is $\int g(x)f_X(x)\,dx$; this is not a definition to be memorised separately, but the same slice
principle: group the values of $X$ near $x$, each group having probability $f_X(x)\,dx$.

**Geometric interpretation.** The expectation is the $x$-coordinate of the centroid of the region between
the density curve and the $x$-axis. Indeed, the region has area $1$, and
$\bar x=\int x f_X(x)\,dx/\int f_X(x)\,dx=\mathbb{E}[X]$. This is why the centroid formulas of §7.10 and
the expectation formulas here are the same formulas.

### 7.14 Consumer and producer surplus

A demand curve $p=D(q)$ gives the price consumers are willing to pay for the $q$-th unit (more precisely,
the marginal willingness to pay). If the market clears at quantity $q^*$ and price $p^*$, consumers pay
$p^*$ for every unit, but they would have paid more for the earlier units. The gain on the unit at
quantity $q$ is $D(q)-p^*$, and summing over $q\in[0,q^*]$ gives

$$CS=\int_0^{q^*}\bigl(D(q)-p^*\bigr)\,dq. \tag{7.14.1}$$

Similarly, producers would have supplied earlier units at prices below $p^*$, so their gain is

$$PS=\int_0^{q^*}\bigl(p^*-S(q)\bigr)\,dq. \tag{7.14.2}$$

The sum $CS+PS$ is the total surplus, the area between the demand and supply curves up to the
intersection.

**Present value.** A payment stream $C(t)$ (currency per unit time) discounted at a continuous rate $r$
has present value

$$PV=\int_0^T e^{-rt}C(t)\,dt. \tag{7.14.3}$$

The element $C(t)\,dt$ is the payment in a short interval, and $e^{-rt}$ is its discount factor. If the
stream continues forever, the integral is improper; for constant $C$,
$PV=C/r$, a formula every finance course uses.

## 8. Formulas and Properties

This section collects the formulas with their hypotheses and gives the derivations that are not already
complete in §7. Every formula is an instance of the slice principle, and every derivation ends by
identifying the Riemann sum.

### 8.1 Summary of formulas

| Quantity | Formula | Hypotheses | Element |
|---|---|---|---|
| Area, vertical strips | $\displaystyle\int_a^b(f-g)\,dx$ | $f,g$ continuous, $f\ge g$ | $(f-g)\,dx$ |
| Area, horizontal strips | $\displaystyle\int_c^d(R-L)\,dy$ | $R,L$ continuous, $R\ge L$ | $(R-L)\,dy$ |
| Volume, slicing | $\displaystyle\int_a^b A(x)\,dx$ | $A$ continuous | $A(x)\,dx$ |
| Volume, washers about $x$-axis | $\displaystyle\pi\int_a^b(f^2-g^2)\,dx$ | $0\le g\le f$ | $\pi(f^2-g^2)\,dx$ |
| Volume, washers about $y$-axis | $\displaystyle\pi\int_c^d(R^2-L^2)\,dy$ | $0\le L\le R$ | $\pi(R^2-L^2)\,dy$ |
| Volume, shells about $y$-axis | $\displaystyle2\pi\int_a^b x(f-g)\,dx$ | $x\ge0$, $f\ge g$ | $2\pi x(f-g)\,dx$ |
| Volume, shells about $x$-axis | $\displaystyle2\pi\int_c^d y(R-L)\,dy$ | $y\ge0$, $R\ge L$ | $2\pi y(R-L)\,dy$ |
| Arc length | $\displaystyle\int_a^b\sqrt{1+f'^2}\,dx$ | $f\in C^1$ | $\sqrt{1+f'^2}\,dx$ |
| Surface about $x$-axis | $\displaystyle2\pi\int_a^b f\sqrt{1+f'^2}\,dx$ | $f\in C^1$, $f\ge0$ | $2\pi f\,ds$ |
| Surface about $y$-axis | $\displaystyle2\pi\int_a^b x\sqrt{1+f'^2}\,dx$ | $f\in C^1$, $x\ge0$ | $2\pi x\,ds$ |
| Average value | $\displaystyle\frac{1}{b-a}\int_a^b f\,dx$ | $f$ continuous | — |
| Work, variable force | $\displaystyle\int_a^b F(x)\,dx$ | $F$ continuous | $F\,dx$ |
| Work, pumping | $\displaystyle\gamma\int_0^H A(y)(H-y)\,dy$ | $A$ continuous | $\gamma A(y)(H-y)\,dy$ |
| Centroid $\bar x$ | $\displaystyle\frac{1}{A}\int_a^b x(f-g)\,dx$ | uniform density | $x\,dA$ |
| Centroid $\bar y$ | $\displaystyle\frac{1}{2A}\int_a^b(f^2-g^2)\,dx$ | uniform density | $\tfrac12(f+g)\,dA$ |
| Moment of inertia $I_y$ | $\displaystyle\int_a^b x^2(f-g)\,dx$ | uniform lamina | $x^2\,dA$ |
| Moment of inertia $I_x$ | $\displaystyle\frac13\int_a^b(f^3-g^3)\,dx$ | uniform lamina | $y^2\,dA$ |
| Hydrostatic force | $\displaystyle\rho g\int_{h_1}^{h_2}h\,w(h)\,dh$ | fluid at rest | $\rho gh\,w\,dh$ |
| Expectation | $\displaystyle\int x f_X(x)\,dx$ | $\int f_X=1$ | $x\,f_X\,dx$ |
| Consumer surplus | $\displaystyle\int_0^{q^*}(D(q)-p^*)\,dq$ | equilibrium | $(D-p^*)\,dq$ |

The rest of §8 justifies the rows that involve a genuine limiting argument: shells, arc length, surface
area, centroids, moments of inertia, hydrostatic force and expectation.

### 8.2 Area and the crossing case

**Proposition 1.** If $f$ and $g$ are continuous on $[a,b]$, then the area of the region between their
graphs is $\int_a^b\lvert f-g\rvert\,dx$.

*Proof.* On a partition, the vertical strip at $\xi_k$ has height $\lvert f(\xi_k)-g(\xi_k)\rvert$, so
the rectangle area is $\lvert f(\xi_k)-g(\xi_k)\rvert\Delta x_k$. These are Riemann sums for the
continuous function $\lvert f-g\rvert$, hence converge to its integral. If $f-g$ has constant sign this
is $\pm\int(f-g)$; the absolute value removes the sign. $\blacksquare$

In practice one finds the zeros of $f-g$, splits the interval, and on each piece uses top minus bottom.
A common error is to integrate $f-g$ across a crossing and report a number smaller than the true area (or
zero, for a symmetric region).

### 8.3 Volume by washers and shells

**Theorem 2 (washers).** Let $0\le g(x)\le f(x)$ on $[a,b]$. The volume of the solid obtained by
revolving the region between the graphs about the $x$-axis is

$$V=\pi\int_a^b\bigl(f(x)^2-g(x)^2\bigr)dx.$$

*Proof.* The cross-section at $x$ is the annulus $\{y:g(x)\le\lvert y\rvert\le f(x)\}$, whose area is
$\pi f(x)^2-\pi g(x)^2$. The slicing formula (7.3.1) gives the result. $\blacksquare$

**Lemma 3 (exact shell volume).** Let $h$ be continuous on $[x,x+\Delta x]$. The volume of the shell
obtained by revolving the region $x\le r\le x+\Delta x$, $0\le z\le h(r)$ about the $z$-axis is
$\pi((x+\Delta x)^2-x^2)h(\xi)$ for some $\xi\in[x,x+\Delta x]$.

*Proof.* By the Mean Value Theorem for integrals applied to $h$ on $[x,x+\Delta x]$, there is $\xi$ with
$h(\xi)=\frac{1}{\Delta x}\int_x^{x+\Delta x}h(r)\,dr$. The shell volume, computed in cylindrical
coordinates or as the difference of two cylinders of the same varying height, is
$\pi((x+\Delta x)^2-x^2)$ times the average height, which is $h(\xi)$. $\blacksquare$

**Theorem 4 (shells).** Under the hypotheses of Theorem 2, the volume of the solid obtained by revolving
the region about the $y$-axis is

$$V=2\pi\int_a^b x\bigl(f(x)-g(x)\bigr)dx.$$

*Proof.* Put $h=f-g$ and let $x_k=a+k\Delta x$ be a uniform partition. By Lemma 3, the volume of the
$k$-th shell is

$$\Delta V_k=2\pi x_kh(\xi_k)\Delta x+\pi h(\xi_k)(\Delta x)^2 .$$

The first terms form a Riemann sum for $2\pi xh(x)$ up to an error bounded by
$2\pi\max\lvert h\rvert\,(b-a)\,\Delta x$ (because $\lvert\xi_k-x_k\rvert\le\Delta x$ and $xh(x)$ is
uniformly continuous); the second terms sum to at most
$\pi\max\lvert h\rvert(b-a)\Delta x$. Both errors tend to $0$, so
$V=2\pi\int_a^bxh(x)\,dx$. $\blacksquare$

### 8.4 Arc length

**Theorem 5.** Let $f$ be continuously differentiable on $[a,b]$. The length of the graph $y=f(x)$,
$a\le x\le b$, is

$$L=\int_a^b\sqrt{1+f'(x)^2}\,dx.$$

*Proof.* For a partition $P$, the inscribed polygonal line has length

$$L(P)=\sum_{k=1}^{n}\sqrt{(\Delta x_k)^2+(\Delta y_k)^2}.$$

The Mean Value Theorem gives $\xi_k\in(x_{k-1},x_k)$ with
$\Delta y_k=f'(\xi_k)\Delta x_k$, so

$$L(P)=\sum_{k=1}^{n}\sqrt{1+f'(\xi_k)^2}\,\Delta x_k .$$

Since $f'$ is continuous, so is $\sqrt{1+f'^2}$, and the sum is a Riemann sum. As the mesh tends to $0$
it converges to $\int_a^b\sqrt{1+f'^2}\,dx$. The arc length is the supremum of the lengths of inscribed
polygonal lines over all partitions; for a $C^1$ curve this supremum equals the limit of the polygonal
lengths along a sequence of partitions with mesh tending to $0$. Hence the formula. $\blacksquare$

*Remark.* The hypothesis $f\in C^1$ can be weakened to "$f$ is absolutely continuous", in which case
$f'$ exists almost everywhere and the formula still holds; this belongs to real analysis. For a curve
that is only continuous, the length may be infinite (the Koch curve is the standard example).

### 8.5 Surface of revolution

**Lemma 6 (frustum area).** The lateral area of a right circular frustum with base radii $r_1,r_2$ and
slant height $\ell$ is $\pi(r_1+r_2)\ell$.

*Proof.* Complete the frustum to a cone. If the smaller cone has slant height $\ell_1$ and base radius
$r_1$, and the larger has slant height $\ell_1+\ell$ and radius $r_2$, similarity gives
$\ell_1/r_1=(\ell_1+\ell)/r_2$, hence $\ell_1=\ell r_1/(r_2-r_1)$. The lateral area is the difference
$\pi r_2(\ell_1+\ell)-\pi r_1\ell_1$, which simplifies to $\pi(r_1+r_2)\ell$. $\blacksquare$

**Theorem 7.** Let $f\ge0$ be continuously differentiable on $[a,b]$. The area of the surface obtained by
revolving the graph about the $x$-axis is

$$S=2\pi\int_a^b f(x)\sqrt{1+f'(x)^2}\,dx.$$

*Derivation sketch.* On $[x_{k-1},x_k]$ the surface is approximated by a frustum with
$r_1=f(x_{k-1})$, $r_2=f(x_k)$ and, by the Mean Value Theorem,
$\ell_k=\sqrt{1+f'(\xi_k)^2}\,\Delta x_k$. Its area is
$\pi(f(x_{k-1})+f(x_k))\sqrt{1+f'(\xi_k)^2}\Delta x_k$. Since $f$ is continuous,
$f(x_{k-1})+f(x_k)=2f(\xi_k)+o(1)$ uniformly, so the sum is a Riemann sum for
$2\pi f(x)\sqrt{1+f'(x)^2}$ plus a uniformly small error. Passing to the limit gives the formula.
$\blacksquare$

The statement is "derivation sketch" rather than a full proof because the surface area is being defined
as the limit of areas of inscribed frusta; a complete treatment requires the theory of surface area,
which is beyond this course. The formula is the standard one and is exact for $C^1$ functions.

### 8.6 Centroids and Pappus

**Theorem 8.** Let $0\le g(x)\le f(x)$ on $[a,b]$ and let the region have uniform density. Then its
centroid is given by (7.10.2)–(7.10.4).

*Proof.* Partition the interval. The strip at $\xi_k$ has area $(f-g)\Delta x$ and centroid
$\bigl(\xi_k,\frac12(f(\xi_k)+g(\xi_k))\bigr)$, so its moments are
$\xi_k(f-g)\Delta x$ about the $y$-axis and
$\frac12(f+g)(f-g)\Delta x=\frac12(f^2-g^2)\Delta x$ about the $x$-axis. Summing gives Riemann sums for
the integrals in (7.10.3)–(7.10.4); dividing by the area gives the centroid. $\blacksquare$

**Corollary 9 (Pappus).** If the region does not cross the axis of revolution,
$V=2\pi dA$ where $d$ is the distance from the centroid to the axis.

*Proof for a vertical axis $x=c$.* By Theorem 4,

$$V=2\pi\int_a^b\lvert x-c\rvert h(x)\,dx .$$

If the region lies to the right of the axis, $\lvert x-c\rvert=x-c$, and

$$V=2\pi\left(\int_a^bxh\,dx-c\int_a^bh\,dx\right)=2\pi A(\bar x-c)=2\pi dA,$$

because $\bar x=\frac1A\int xh\,dx$ and $d=\bar x-c$. The case to the left is the same with signs
reversed. $\blacksquare$

### 8.7 Moments of inertia

**Theorem 10.** For a uniform lamina between $g$ and $f$ on $[a,b]$, the moments of inertia about the
coordinate axes are (7.11.2) and (7.11.3).

*Proof.* For $I_y$, the element at $(\xi,y)$ has mass $\rho\,dy\,d\xi$ and distance $\xi$ from the
$y$-axis, so $dI_y=\xi^2\rho\,dy\,d\xi$; integrating $y$ from $g(\xi)$ to $f(\xi)$ and summing gives
$\rho\int x^2(f-g)\,dx$. The density cancels if the lamina is uniform (set $\rho=1$). For $I_x$, the
element has distance $\lvert y\rvert$ from the $x$-axis, so
$dI_x=\rho y^2\,dy\,d\xi$; integrating in $y$ gives $\frac{\rho}{3}(f^3-g^3)d\xi$, and summing gives
(7.11.3). $\blacksquare$

**Theorem 11 (parallel axis).** For any rigid body of mass $M$ and any axis at distance $d$ from a
parallel axis through the centre of mass, $I=I_{\mathrm{cm}}+Md^2$.

*Proof.* Write $r=r_{\mathrm{cm}}+r'$, where $r'$ is measured from the centre of mass. Then
$I=\int\lvert r_{\mathrm{cm}}+r'\rvert^2dm
=\int\lvert r_{\mathrm{cm}}\rvert^2dm+2r_{\mathrm{cm}}\cdot\int r'\,dm+\int\lvert r'\rvert^2dm$.
The middle term vanishes because $\int r'\,dm=0$ is the definition of the centre of mass, and the first
term is $Md^2$. $\blacksquare$

**Solid of revolution.** Formula (7.11.4) follows from the disk's moment of inertia
$\frac12m r^2$ about a diameter. If the axis of revolution is the $z$-axis instead, the disk's moment
about its own axis is $\frac12mr^2$, and the formula is the same with $f^4$.

### 8.8 Hydrostatic force

**Theorem 12.** For a vertical plate whose width at depth $h$ is $w(h)$, submerged between depths $h_1$
and $h_2$ in a fluid of density $\rho$,

$$F=\rho g\int_{h_1}^{h_2}h\,w(h)\,dh=\rho gA\bar h .$$

*Proof.* The first equality is the slice principle applied to $dF=p\,dA=\rho gh\,w(h)\,dh$. For the
second, $A=\int w\,dh$ and the centroid depth is
$\bar h=\frac1A\int h\,w(h)\,dh$ by (7.10.4) applied with the roles of $x$ and $y$ exchanged; substituting
gives $F=\rho gA\bar h$. $\blacksquare$

### 8.9 Expectation and variance

**Proposition 13.** For a density $f_X$ and constants $a,b$,
$\mathbb{E}[aX+b]=a\mathbb{E}[X]+b$ and
$\operatorname{Var}(aX+b)=a^2\operatorname{Var}(X)$.

*Proof.* The first follows from linearity of the integral and $\int f_X=1$:

$$\mathbb{E}[aX+b]=\int(ax+b)f_X(x)\,dx=a\int xf_X(x)\,dx+b\int f_X(x)\,dx=a\mathbb{E}[X]+b .$$

For the second, let $\mu=\mathbb{E}[X]$. Then
$\mathbb{E}[(aX+b)-(a\mu+b)]^2=\mathbb{E}[a^2(X-\mu)^2]=a^2\operatorname{Var}(X)$ by the first part
applied to the function $(X-\mu)^2$. $\blacksquare$

### 8.10 Work formulas

**Proposition 14.** The work to stretch a spring from $x=a$ to $x=b$ against $F=kx$ is
$\frac{k}{2}(b^2-a^2)$; the work to empty a tank of cross-section $A(y)$ and height $H$ over its top is
$\gamma\int_0^HA(y)(H-y)\,dy$.

*Proof.* Both are (7.9.1) with the stated force. For the spring, $F=kx$ and
$\int_a^bkx\,dx=\frac{k}{2}(b^2-a^2)$. For the tank, the slice at height $y$ has weight
$\gamma A(y)\,dy$ and is lifted $H-y$, so $dW=\gamma A(y)(H-y)\,dy$. $\blacksquare$

### 8.11 Standard integrals used in this topic

All are checked by differentiating the right-hand side; $C$ is an arbitrary constant and $a>0$.

| Integral | Antiderivative |
|---|---|
| $\int x^n\,dx$ | $\dfrac{x^{n+1}}{n+1}+C$, $n\ne-1$ |
| $\int\dfrac{dx}{x}$ | $\ln\lvert x\rvert+C$ |
| $\int e^{ax}dx$ | $\dfrac{e^{ax}}{a}+C$ |
| $\int xe^{ax}dx$ | $e^{ax}\left(\dfrac{x}{a}-\dfrac{1}{a^2}\right)+C$ |
| $\int x^2e^{ax}dx$ | $e^{ax}\left(\dfrac{x^2}{a}-\dfrac{2x}{a^2}+\dfrac{2}{a^3}\right)+C$ |
| $\int\ln x\,dx$ | $x\ln x-x+C$ |
| $\int x\ln x\,dx$ | $\dfrac{x^2}{2}\ln x-\dfrac{x^2}{4}+C$ |
| $\int\dfrac{dx}{x^2+a^2}$ | $\dfrac1a\arctan\dfrac xa+C$ |
| $\int\dfrac{dx}{\sqrt{a^2-x^2}}$ | $\arcsin\dfrac xa+C$ |
| $\int\sqrt{a^2-x^2}\,dx$ | $\dfrac{x}{2}\sqrt{a^2-x^2}+\dfrac{a^2}{2}\arcsin\dfrac xa+C$ |
| $\int\sqrt{x^2+a^2}\,dx$ | $\dfrac{x}{2}\sqrt{x^2+a^2}+\dfrac{a^2}{2}\ln\left(x+\sqrt{x^2+a^2}\right)+C$ |
| $\int\sec x\,dx$ | $\ln\lvert\sec x+\tan x\rvert+C$ |
| $\int\sec^2x\,dx$ | $\tan x+C$ |
| $\int\tan x\,dx$ | $-\ln\lvert\cos x\rvert+C$ |
| $\int\sinh x\,dx$ | $\cosh x+C$ |
| $\int\cosh x\,dx$ | $\sinh x+C$ |
| $\int\dfrac{dx}{x^2-a^2}$ | $\dfrac{1}{2a}\ln\left\lvert\dfrac{x-a}{x+a}\right\rvert+C$ |

The last formula is used only for $x>a$ or $x<-a$; the absolute value handles both signs. The
half-angle identities $\sin^2x=\frac{1-\cos2x}{2}$ and $\cos^2x=\frac{1+\cos2x}{2}$ are used in the
examples and exercises.

### 8.12 Dimensions and units

| Quantity | SI unit | Dimension |
|---|---|---|
| Length | m | $\mathsf{L}$ |
| Area | m$^2$ | $\mathsf{L}^2$ |
| Volume | m$^3$ | $\mathsf{L}^3$ |
| Mass | kg | $\mathsf{M}$ |
| Density | kg/m$^3$ | $\mathsf{M}\mathsf{L}^{-3}$ |
| Force | N | $\mathsf{M}\mathsf{L}\mathsf{T}^{-2}$ |
| Pressure | Pa $=$ N/m$^2$ | $\mathsf{M}\mathsf{L}^{-1}\mathsf{T}^{-2}$ |
| Work, energy | J $=$ N·m | $\mathsf{M}\mathsf{L}^2\mathsf{T}^{-2}$ |
| Moment of inertia | kg·m$^2$ | $\mathsf{M}\mathsf{L}^2$ |

A dimension check catches the most common set-up error: an integrand for a volume must have dimension
$\mathsf{L}^2$ (since it is multiplied by $dx$ of dimension $\mathsf{L}$), and an integrand for a force
must have dimension $\mathsf{M}\mathsf{L}\mathsf{T}^{-2}$. If the units of the integrand are wrong, no
amount of correct integration will fix the answer.

### 8.13 A note on improper integrals in applications

Several formulas in this topic are naturally improper: the tail of a probability density, the work to
escape to infinity, the present value of a perpetual stream, the total mass of an unbounded region. In
every case the definition is a limit:

$$\int_a^{\infty}q(x)\,dx=\lim_{R\to\infty}\int_a^Rq(x)\,dx .$$

The applications in this topic use such integrals only when the limit is evidently finite (for example,
an exponential tail). The systematic treatment — convergence tests, the $p$-test, comparison — is the
subject of [Improper Integrals](../10-improper-integrals/README.md), which follows this topic.

<!--APPEND-->


