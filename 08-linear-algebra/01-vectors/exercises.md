# Vectors — Exercises

> Companion to the [tutorial](README.md). Solutions are in [solutions.md](solutions.md).

Work on paper, not in your head. For each problem write down (i) what is given, (ii) what is asked, and
(iii) which of the four operations — addition, scaling, dot product, cross product — is relevant, before
you compute anything. If you are stuck for more than twenty minutes, read only the first line of the
corresponding solution and continue on your own.

Problems are numbered continuously so that the solutions file mirrors them exactly. The level labels
indicate the amount of synthesis required, not the length of the answer. All vectors are in
$\mathbb{R}^3$ unless the problem says otherwise.

## Beginner

**1.** Let $\mathbf{a}=(3,-1,2)$ and $\mathbf{b}=(-2,4,1)$. Compute (a) $\mathbf{a}+\mathbf{b}$,
(b) $\mathbf{a}-\mathbf{b}$, (c) $2\mathbf{a}+3\mathbf{b}$, (d) $\lVert\mathbf{a}\rVert$.

**2.** Find the unit vector in the direction of $\mathbf{v}=(6,-2,3)$ and the unit vector in the opposite
direction. Verify that both have length $1$.

**3.** Compute (a) $(2,-1,3)\cdot(4,2,-2)$ and (b) $(1,2)\cdot(3,4)$. In each case state whether the two
vectors are perpendicular, and why the answer to (b) is compatible with the sign of the cosine.

**4.** Find the angle between (a) $(1,1,0)$ and $(1,0,1)$; (b) $(1,2,2)$ and $(2,1,-2)$. Give exact
values in degrees.

**5.** Decide which pairs are parallel, using cross products to justify each answer:
(a) $(1,-2,3)$ and $(-2,4,-6)$; (b) $(1,2,3)$ and $(2,3,4)$; (c) $(0,0,1)$ and $(0,0,-5)$.

**6.** Compute (a) $(1,2,3)\times(4,5,6)$ and (b) $(2,-1,0)\times(1,0,3)$. Verify that the answer to (a)
is perpendicular to both factors.

**7.** A parallelogram has consecutive vertices $A(1,1)$, $B(4,2)$ and $C(5,5)$. Find the fourth vertex
$D$, and verify that $\overrightarrow{AB}=\overrightarrow{DC}$.

**8.** For the segment from $P(1,-2,3)$ to $Q(7,4,-3)$, find (a) the midpoint and (b) the point one third
of the way from $P$ to $Q$.

**9.** Write the equation of the plane through $(1,2,3)$ with normal $(2,-1,4)$, and find where it meets
the $z$-axis.

**10.** A line passes through $(2,-1,4)$ with direction $(1,3,-2)$. (a) Write its parametric equations.
(b) Find the point with $t=2$. (c) Decide whether $(5,8,-2)$ lies on the line.

**11.** A force $\mathbf{F}=(2,-3,1)$ acts through a displacement $\mathbf{d}=(4,1,-2)$. Compute the work
done, and state what sign the answer has and why.

**12.** For $\mathbf{u}=(3,1,0)$ and $\mathbf{v}=(1,2,-1)$, compute $\lVert\mathbf{u}+\mathbf{v}\rVert$
and $\lVert\mathbf{u}-\mathbf{v}\rVert$, then verify the parallelogram law
$\lVert\mathbf{u}+\mathbf{v}\rVert^2+\lVert\mathbf{u}-\mathbf{v}\rVert^2=2\lVert\mathbf{u}\rVert^2+2\lVert\mathbf{v}\rVert^2$.

## Intermediate

**13.** Let $\lVert\mathbf{u}\rVert=2$, $\lVert\mathbf{v}\rVert=3$ and let the angle between them be
$60^\circ$. Find (a) $\mathbf{u}\cdot\mathbf{v}$, (b) $\lVert\mathbf{u}+\mathbf{v}\rVert$,
(c) $\lVert\mathbf{u}-\mathbf{v}\rVert$, (d) $\cos\varphi$ where $\varphi$ is the angle between
$\mathbf{u}+\mathbf{v}$ and $\mathbf{u}-\mathbf{v}$.

**14.** Project $\mathbf{u}=(3,1,-2)$ onto $\mathbf{v}=(1,2,2)$. Write the orthogonal decomposition, and
verify that the remainder is perpendicular to $\mathbf{v}$.

**15.** Find the value of $\lambda$ for which $(2,\lambda,3)$ is perpendicular to $(1,-2,4)$.

**16.** A cube has edges of length $1$. Show that the angle between two space diagonals of the cube is
$\arccos(1/3)$, and give the angle in degrees.

**17.** Find the area of the triangle with vertices $A(1,0,0)$, $B(0,1,0)$, $C(0,0,1)$.

**18.** Find the equation of the plane through $P(1,0,0)$, $Q(0,2,0)$ and $R(0,0,3)$.

**19.** Find the distance from $(2,-1,3)$ to the plane $2x-y+2z=4$.

**20.** Find the intersection of the line $\mathbf{r}(t)=(1,2,0)+t(2,-1,1)$ with the plane
$x+y+z=5$.

**21.** Find (a) the acute angle between the planes $x+2y+2z=1$ and $x=1$; (b) the angle between the line
with direction $(2,1,2)$ and the plane with normal $(1,1,0)$.

**22.** A force $\mathbf{F}=(1,2,3)$ acts at the point $(2,0,-1)$. Find its torque about the origin, and
verify that the torque is perpendicular to both the lever arm and the force.

**23.** Find all vectors of length $5$ that are orthogonal to both $(1,0,1)$ and $(0,1,1)$.

## Advanced

**24.** Prove that for all $\mathbf{u},\mathbf{v}\in\mathbb{R}^n$,
$\lVert\mathbf{u}+\mathbf{v}\rVert^2+\lVert\mathbf{u}-\mathbf{v}\rVert^2=2\lVert\mathbf{u}\rVert^2+2\lVert\mathbf{v}\rVert^2$.
Deduce the polarization identity, and explain in one sentence what it says about the norm and the dot
product.

**25.** Prove the Cauchy–Schwarz inequality and deduce the triangle inequality. State exactly when
equality holds in each, and explain why the angle formula needs Cauchy–Schwarz.

**26.** Prove Lagrange's identity
$\lVert\mathbf{u}\times\mathbf{v}\rVert^2=\lVert\mathbf{u}\rVert^2\lVert\mathbf{v}\rVert^2-(\mathbf{u}\cdot\mathbf{v})^2$,
and deduce that $\lVert\mathbf{u}\times\mathbf{v}\rVert=\lVert\mathbf{u}\rVert\lVert\mathbf{v}\rVert\sin\theta$.

**27.** Prove that $[\mathbf{u},\mathbf{v},\mathbf{w}]=[\mathbf{v},\mathbf{w},\mathbf{u}]=[\mathbf{w},\mathbf{u},\mathbf{v}]$
and that swapping any two entries changes the sign. Interpret both statements geometrically.

**28.** Let $ABCD$ be a parallelogram. Prove with vectors that its diagonals are perpendicular if and only
if it is a rhombus (all four sides equal).

**29.** Derive the formula for the distance from a point $\mathbf{q}$ to the plane
$\mathbf{n}\cdot\mathbf{x}=d$, and explain where the hypothesis $\mathbf{n}\ne\mathbf{0}$ is used.

**30.** Let $A,B,C$ be a triangle with position vectors $\mathbf{a},\mathbf{b},\mathbf{c}$. Prove that the
three medians meet at the point $\mathbf{g}=(\mathbf{a}+\mathbf{b}+\mathbf{c})/3$, and that this point
divides each median in the ratio $2:1$ from the vertex.

**31.** (a) Prove that if $\mathbf{u}\cdot\mathbf{x}=0$ for every $\mathbf{x}\in\mathbb{R}^3$, then
$\mathbf{u}=\mathbf{0}$. (b) Use this to show that the normal direction of a plane is unique up to a
non-zero scalar multiple.

## Challenge

**32.** Prove the vector triple product identity
$\mathbf{u}\times(\mathbf{v}\times\mathbf{w})=(\mathbf{u}\cdot\mathbf{w})\mathbf{v}-(\mathbf{u}\cdot\mathbf{v})\mathbf{w}$
by expanding in components, and deduce the Jacobi identity
$\mathbf{u}\times(\mathbf{v}\times\mathbf{w})+\mathbf{v}\times(\mathbf{w}\times\mathbf{u})+\mathbf{w}\times(\mathbf{u}\times\mathbf{v})=\mathbf{0}$.

**33.** Derive the formula for the distance between two skew lines, then apply it to
$L_1=\{(1,2,3)+t(1,0,1)\}$ and $L_2=\{(0,1,2)+s(0,1,1)\}$ after verifying that they are skew.

**34.** Suppose $\mathbf{u}+\mathbf{v}+\mathbf{w}=\mathbf{0}$. Prove that
$\mathbf{u}\times\mathbf{v}=\mathbf{v}\times\mathbf{w}=\mathbf{w}\times\mathbf{u}$, and interpret the
common length as twice the area of a triangle.

**35.** Prove that the dihedral angle between two faces of a regular tetrahedron satisfies
$\cos\theta=1/3$, and give the angle in degrees.

**36.** (a) Prove that the volume of the tetrahedron with vertices $O,\mathbf{a},\mathbf{b},\mathbf{c}$ is
$\tfrac16\lvert[\mathbf{a},\mathbf{b},\mathbf{c}]\rvert$. (b) Compute this volume for $A(1,0,0)$,
$B(0,1,0)$, $C(0,0,1)$, $D(1,1,1)$. (c) Find $k$ such that $D=(1,1,k)$ makes $A,B,C,D$ coplanar.
