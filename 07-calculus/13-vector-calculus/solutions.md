# Vector Calculus — Solutions

> [Vector Calculus](README.md) · Solutions to the 36 problems in [exercises.md](exercises.md)

Every solution states the strategy, carries out each step, and checks the orientation and the sign. Where a
second method exists, it is shown or indicated.

## Beginner

**1.**

*Strategy: solve the ODE system componentwise and look for a conserved quantity.*

(a) For $\mathbf F = (x,y)$ the system is $x' = x$, $y' = y$. Separating, $x(t) = x_0e^t$ and
$y(t) = y_0e^t$, so $y(t)/x(t) = y_0/x_0$ is constant along the flow. The field lines are therefore the rays
from the origin (the half-lines in the quadrant determined by the signs of $x_0,y_0$), traversed away from
the origin because both coordinates grow. The origin itself is a critical point.

(b) For $\mathbf F = (-y,x)$ the system is $x' = -y$, $y' = x$. Differentiating the first equation and
substituting the second gives $x'' = -y' = -x$, so $x(t) = A\cos t+B\sin t$ and
$y(t) = -x'(t) = A\sin t-B\cos t$; then $x^2+y^2 = A^2+B^2$. The field lines are circles centred at the
origin. At $(1,0)$ the velocity is $(0,1)$, which points upward, so the traversal is counterclockwise.

*Check:* differentiating $x^2+y^2$ along the flow gives $2xx'+2yy' = 2x(-y)+2y(x) = 0$. ✓

**2.**

*Strategy: apply the coordinate definitions; differentiate each component in the stated variable.*

With $P = x^2y$, $Q = yz$, $R = xz^2$:

$$\nabla\cdot\mathbf F = P_x+Q_y+R_z = 2xy+z+2xz ,$$

and

$$\nabla\times\mathbf F = (R_y-Q_z,\ P_z-R_x,\ Q_x-P_y) = (0-y,\ 0-z^2,\ 0-x^2)
= (-y,\ -z^2,\ -x^2).$$

*Check at $(1,1,1)$:* $\nabla\cdot\mathbf F = 2+1+2 = 5$ and $\nabla\times\mathbf F = (-1,-1,-1)$; direct
differentiation of the components at that point gives the same values.

**3.**

*Strategy: test $P_y = Q_x$ on the simply connected plane, then integrate.*

$P = y\cos(xy)$ gives $P_y = \cos(xy)-xy\sin(xy)$; $Q = x\cos(xy)$ gives
$Q_x = \cos(xy)-xy\sin(xy)$. The two agree everywhere, and $\mathbb{R}^2$ is simply connected, so a potential
exists.

Integrating $P$ in $x$ (with $y$ fixed): $\phi = \int y\cos(xy)\,dx = \sin(xy)+g(y)$. Then
$\phi_y = x\cos(xy)+g'(y)$, which must equal $Q = x\cos(xy)$, so $g'(y) = 0$ and $g$ is constant. Hence

$$\phi(x,y) = \sin(xy)+C .$$

*Check:* $\phi_x = y\cos(xy) = P$ and $\phi_y = x\cos(xy) = Q$. ✓

**4.**

*Strategy: parametrise the segment and use $ds = \lVert\mathbf r'\rVert\,dt$.*

$\mathbf r(t) = (t,2t)$, $0\le t\le1$, so $\mathbf r'(t) = (1,2)$ and
$\lVert\mathbf r'(t)\rVert = \sqrt{1+4} = \sqrt5$. On the segment $x+y = t+2t = 3t$. Therefore

$$\int_C(x+y)\,ds = \int_0^1 3t\sqrt5\,dt = 3\sqrt5\left[\frac{t^2}{2}\right]_0^1 = \frac{3\sqrt5}{2}.$$

*Check:* the segment has length $\sqrt5$, and the average of $x+y$ over it is $\frac12(0+3) = \frac32$ (the
integrand is linear), so the integral is $\sqrt5\cdot\frac32$. ✓

**5.**

*Strategy: parametrise by $x$ and compute the dot product.*

$\mathbf r(t) = (t,t^2)$, $0\le t\le1$, so $\mathbf r'(t) = (1,2t)$ and
$\mathbf F(\mathbf r(t)) = (t,t^2)$. Hence
$\mathbf F\cdot\mathbf r' = t\cdot1+t^2\cdot2t = t+2t^3$ and

$$\int_C\mathbf F\cdot d\mathbf r = \int_0^1(t+2t^3)\,dt = \frac12+\frac12 = 1 .$$

*Check by potential:* $\mathbf F = \nabla\bigl(\tfrac12(x^2+y^2)\bigr)$, so the integral is
$\tfrac12(1+1)-\tfrac12(0+0) = 1$. ✓

**6.**

*Strategy: parametrise the circle of radius $3$ and integrate.*

$\mathbf r(t) = 3(\cos t,\sin t)$, $0\le t\le2\pi$, so $\mathbf r'(t) = 3(-\sin t,\cos t)$ and
$\mathbf F(\mathbf r(t)) = 3(-\sin t,\cos t)$. Then
$\mathbf F\cdot\mathbf r' = 9(\sin^2t+\cos^2t) = 9$, so

$$\oint_C\mathbf F\cdot d\mathbf r = \int_0^{2\pi}9\,dt = 18\pi .$$

*Check:* the field $(-y,x)$ has curl $2$, and by Green's theorem the circulation around a circle is
$2\cdot\pi\cdot3^2 = 18\pi$. ✓

**7.**

*Strategy: use the graph area formula.*

$g(x,y) = x+2y$, so $g_x = 1$, $g_y = 2$ and
$\sqrt{1+g_x^2+g_y^2} = \sqrt{1+1+4} = \sqrt6$. The region is the unit square of area $1$, so

$$\operatorname{area} = \iint_D\sqrt6\,dA = \sqrt6 .$$

*Check:* the graph is a tilted plane; its area over a unit square is the area of the square times the
secant of the tilt, which is $\sqrt6$. ✓

**8.**

*Strategy: compute $\mathbf r_\phi\times\mathbf r_\theta$ and integrate its norm.*

$\mathbf r_\phi = R(\cos\phi\cos\theta,\cos\phi\sin\theta,-\sin\phi)$ and
$\mathbf r_\theta = R(-\sin\phi\sin\theta,\sin\phi\cos\theta,0)$. The cross product is

$$\mathbf r_\phi\times\mathbf r_\theta
= R^2\sin\phi\,(\sin\phi\cos\theta,\ \sin\phi\sin\theta,\ \cos\phi),$$

whose norm is $R^2\sin\phi$ (the bracket is a unit vector). Hence

$$\operatorname{area} = \int_0^{2\pi}\int_0^\pi R^2\sin\phi\,d\phi\,d\theta
= 2\pi R^2\left[-\cos\phi\right]_0^\pi = 4\pi R^2 .$$

*Check:* for $R=1$ this is the familiar $4\pi$. The normal points outward, since the bracket is $\mathbf x/R$.

**9.**

*Strategy: use the spherical parametrisation of the radius-$2$ sphere and integrate $z\,dS$.*

With $\mathbf r(\phi,\theta) = 2(\sin\phi\cos\theta,\sin\phi\sin\theta,\cos\phi)$ and
$0\le\phi\le\pi/2$, the area element is $dS = 4\sin\phi\,d\phi\,d\theta$ and $z = 2\cos\phi$. Hence

$$\iint_S z\,dS = \int_0^{2\pi}\int_0^{\pi/2}(2\cos\phi)(4\sin\phi)\,d\phi\,d\theta
= 8\cdot2\pi\int_0^{\pi/2}\sin\phi\cos\phi\,d\phi .$$

Since $\int_0^{\pi/2}\sin\phi\cos\phi\,d\phi = \frac12$,

$$\iint_S z\,dS = 16\pi\cdot\frac12 = 8\pi .$$

*Check:* the hemisphere has area $8\pi$, and by symmetry its centroid has $\bar z = 1$ (the radius times
$\frac12$), so $\iint z\,dS = \bar z\cdot\operatorname{area} = 8\pi$. ✓

**10.**

*Strategy: on this surface $x=1$ and the normal is constant.*

The surface is $S = \{(1,y,z): 0\le y,z\le1\}$ with $\mathbf n = \mathbf i$ and $dS = dy\,dz$. On $S$,
$\mathbf F = (1,0,0)$, so $\mathbf F\cdot\mathbf n = 1$ and

$$\iint_S\mathbf F\cdot d\mathbf S = \int_0^1\int_0^1 1\,dy\,dz = 1 .$$

*Check:* the flux of $(x,0,0)$ through a unit square perpendicular to the $x$-axis is the field strength $1$
times the area $1$. ✓

**11.**

*Strategy: test the plane curl, integrate, then use the fundamental theorem.*

$P = 2xy$ and $Q = x^2$, so $P_y = 2x = Q_x$: the field is conservative on the simply connected plane.

Integrating, $\phi = \int 2xy\,dx = x^2y+g(y)$; then $\phi_y = x^2+g'(y) = x^2$, so $g' = 0$ and
$\phi = x^2y$ (up to a constant). By the fundamental theorem,

$$\int_{(0,0)}^{(1,3)}\mathbf F\cdot d\mathbf r = \phi(1,3)-\phi(0,0) = 3 .$$

*Check along the straight line:* $\mathbf r(t) = (t,3t)$, $\mathbf F = (6t^2,t^2)$, $\mathbf r' = (1,3)$,
$\mathbf F\cdot\mathbf r' = 9t^2$, and $\int_0^1 9t^2\,dt = 3$. ✓

**12.**

*Strategy: identify $P,Q$ and apply Green's theorem.*

Here $P = 0$ and $Q = x$, so $Q_x-P_y = 1$ and

$$\oint_C x\,dy = \iint_D 1\,dA = \operatorname{area}(D) = 1 .$$

*Check directly:* the right side $x=1$, $0\le y\le1$, contributes $\int_0^1 1\,dy = 1$; the top and bottom
contribute nothing because $dy = 0$ there; the left side has $x=0$. Total $1$. ✓

## Intermediate

**13.**

*Strategy: compute all three and use the agreement as a check of the fundamental theorem.*

$\mathbf F = (y^2,2xy)$ satisfies $P_y = 2y = Q_x$, so it is conservative on $\mathbb{R}^2$.

(a) *Straight segment.* $\mathbf r(t) = (2t,t)$, $0\le t\le1$, so $\mathbf r' = (2,1)$ and
$\mathbf F = (t^2,4t^2)$. Then $\mathbf F\cdot\mathbf r' = 2t^2+4t^2 = 6t^2$ and
$\int_0^1 6t^2\,dt = 2$.

(b) *Two-segment path.* On $(0,0)\to(2,0)$ we have $y=0$, hence $\mathbf F = (0,0)$ and the integral is $0$.
On $(2,0)\to(2,1)$ we have $x=2$, $d\mathbf r = (0,dy)$, and $\mathbf F = (y^2,4y)$, so the integral is
$\int_0^1 4y\,dy = 2$. Total $2$.

(c) *Potential.* $\phi = \int y^2\,dx = xy^2+g(y)$, and $\phi_y = 2xy+g'(y) = 2xy$ gives $g'=0$. Hence
$\phi = xy^2$ and $\phi(2,1)-\phi(0,0) = 2$.

All three agree, as the fundamental theorem requires. ✓

**14.**

*Strategy: the circle has constant radius, so the integrand is constant and only the length matters.*

$\mathbf r(t) = a(\cos t,\sin t)$, $0\le t\le2\pi$, gives $\lVert\mathbf r'\rVert = a$ and
$x^2+y^2 = a^2$. Hence

$$\int_C(x^2+y^2)\,ds = \int_0^{2\pi}a^2\cdot a\,dt = 2\pi a^3 .$$

*Check:* the length of the circle is $2\pi a$, and the integrand is the constant $a^2$, so the integral is
$a^2\cdot2\pi a$. ✓

**15.**

*Strategy: parametrise the segment and use the constant speed.*

$\mathbf r(t) = (1-t,t)$, $0\le t\le1$, so $\mathbf r' = (-1,1)$ and $\lVert\mathbf r'\rVert = \sqrt2$. On the
segment, $2x+3y = 2(1-t)+3t = 2+t$. Hence

$$\int_C(2x+3y)\,ds = \sqrt2\int_0^1(2+t)\,dt = \sqrt2\left(2+\frac12\right) = \frac{5\sqrt2}{2}.$$

*Check:* the length is $\sqrt2$ and the average of the linear integrand over the segment is
$\frac12\bigl((2\cdot1+3\cdot0)+(2\cdot0+3\cdot1)\bigr) = \frac52$. ✓

**16.**

*Strategy: Green's theorem for the value, then a direct computation as an independent check.*

$P = x^2-y$ gives $P_y = -1$; $Q = x+y^2$ gives $Q_x = 1$. Hence $Q_x-P_y = 2$ and, since the square has
area $1$,

$$\oint_C(x^2-y)\,dx+(x+y^2)\,dy = \iint_D 2\,dA = 2 .$$

*Direct check.* On the bottom ($y=0$, $dy=0$): $\int_0^1x^2\,dx = \frac13$. On the right ($x=1$, $dx=0$):
$\int_0^1(1+y^2)\,dy = 1+\frac13 = \frac43$. On the top ($y=1$, traversed right to left, $dy=0$):
$\int_1^0(x^2-1)\,dx = -\left[\frac{x^3}{3}-x\right]_0^1 = \frac23$. On the left ($x=0$, $dx=0$):
$\int_1^0y^2\,dy = -\frac13$. Sum: $\frac13+\frac43+\frac23-\frac13 = 2$. ✓

**17.**

*Strategy: divergence theorem; then check with a direct surface integral.*

$\mathbf F = \mathbf x$ has $\nabla\cdot\mathbf F = 1+1+1 = 3$. The ball of radius $R$ has volume
$\frac43\pi R^3$, so

$$\iint_S\mathbf F\cdot d\mathbf S = \iiint_V 3\,dV = 4\pi R^3 .$$

*Direct check:* on the sphere, $\mathbf n = \mathbf x/R$, so
$\mathbf F\cdot\mathbf n = (\mathbf x\cdot\mathbf x)/R = R^2/R = R$; the area is $4\pi R^2$, giving
$4\pi R^3$. ✓

**18.**

*Strategy: compute both sides of Stokes' theorem and compare.*

*Curl:* $\mathbf F = (z,x,y)$, so
$\nabla\times\mathbf F = (R_y-Q_z,\ P_z-R_x,\ Q_x-P_y) = (1-0,\ 1-0,\ 1-0) = (1,1,1)$.

*Surface side:* with $g(x,y) = 1-x^2-y^2$, the upward vector area element is
$(-g_x,-g_y,1)\,dx\,dy = (2x,2y,1)\,dx\,dy$. Hence

$$\iint_S(\nabla\times\mathbf F)\cdot d\mathbf S = \iint_{x^2+y^2\le1}(2x+2y+1)\,dA .$$

The integrals of $2x$ and $2y$ over the disk vanish by symmetry, so the value is the area $\pi$.

*Boundary side:* the boundary is the unit circle at $z=0$. With the upward normal, the induced orientation is
counterclockwise: $\mathbf r(t) = (\cos t,\sin t,0)$, $\mathbf r' = (-\sin t,\cos t,0)$, and
$\mathbf F = (z,x,y) = (0,\cos t,\sin t)$. Then $\mathbf F\cdot\mathbf r' = \cos^2t$ and
$\int_0^{2\pi}\cos^2t\,dt = \pi$. ✓

*Pitfall:* with the downward normal the boundary is clockwise and both sides become $-\pi$.

**19.**

*Strategy: divergence theorem, with a face-by-face check.*

$\nabla\cdot\mathbf F = 2x+2y+2z$, so

$$\iiint_V\nabla\cdot\mathbf F\,dV = 2\int_0^1\int_0^1\int_0^1(x+y+z)\,dz\,dy\,dx
= 2\left(\frac12+\frac12+\frac12\right) = 3 .$$

*Check on the faces:* on $x=1$ the flux is $\int_0^1\int_0^1 1\,dy\,dz = 1$, and on $x=0$ it is $0$; the
$y$-faces and $z$-faces contribute $1$ each in the same way. Total $1+1+1 = 3$. ✓

**20.**

*Strategy: verify the three curl conditions, integrate, and use the fundamental theorem.*

With $P = 2xy+z^2$, $Q = x^2+2yz$, $R = y^2+2zx$:

$$R_y-Q_z = 2y-2y = 0,\qquad P_z-R_x = 2z-2z = 0,\qquad Q_x-P_y = 2x-2x = 0 .$$

So the field is curl-free, and $\mathbb{R}^3$ is star-shaped, so a potential exists.

Integrate $P$ in $x$: $\phi = x^2y+z^2x+g(y,z)$. Then $\phi_y = x^2+g_y = Q = x^2+2yz$, so
$g_y = 2yz$ and $g = y^2z+h(z)$. Finally $\phi_z = 2zx+y^2+h'(z) = R = y^2+2zx$, so $h' = 0$. Hence

$$\phi = x^2y+y^2z+z^2x .$$

*Check:* $\phi_x = 2xy+z^2$, $\phi_y = x^2+2yz$, $\phi_z = y^2+2zx$. ✓ The work from the origin to
$(1,1,1)$ is $\phi(1,1,1)-\phi(0,0,0) = 1+1+1 = 3$.

**21.**

*Strategy: the cone is a graph over the unit disk; use the graph area element.*

$g(x,y) = \sqrt{x^2+y^2}$ gives $g_x = x/\sqrt{x^2+y^2}$ and $g_y = y/\sqrt{x^2+y^2}$, so
$g_x^2+g_y^2 = 1$ and $dS = \sqrt2\,dx\,dy$. Hence, in polar coordinates over $0\le r\le1$,

$$\iint_S(x^2+y^2)\,dS = \sqrt2\int_0^{2\pi}\int_0^1 r^2\cdot r\,dr\,d\theta
= \sqrt2\cdot2\pi\cdot\frac14 = \frac{\pi\sqrt2}{2}.$$

*Check:* the cone has lateral area $\pi\sqrt2$ (Solution 23), and the average value of $x^2+y^2$ over it is
$\frac12$ by symmetry, giving $\frac{\pi\sqrt2}{2}$. ✓

**22.**

*Strategy: differentiate carefully, compute the circulation on the unit circle, and examine the hypotheses
of Green's theorem.*

$P = -y/(x^2+y^2)$, so by the quotient rule

$$P_y = \frac{-(x^2+y^2)+y\cdot2y}{(x^2+y^2)^2} = \frac{y^2-x^2}{(x^2+y^2)^2}.$$

$Q = x/(x^2+y^2)$, so

$$Q_x = \frac{(x^2+y^2)-x\cdot2x}{(x^2+y^2)^2} = \frac{y^2-x^2}{(x^2+y^2)^2}.$$

Hence $P_y = Q_x$ on the whole domain $\mathbb{R}^2\setminus\{(0,0)\}$.

On the unit circle, $\mathbf F = (-\sin t,\cos t)$ and $\mathbf r' = (-\sin t,\cos t)$, so
$\mathbf F\cdot\mathbf r' = 1$ and the circulation is $\int_0^{2\pi}dt = 2\pi$.

The curl test gives only a *necessary* condition on a general domain. Green's theorem would require $P,Q$ to
be $C^1$ on an open set containing the disk bounded by the circle, and they are not defined at the origin.
The domain is not simply connected, so the sufficient condition of §7.2 does not apply. The obstruction is
the hole: the multivalued angle $\theta = \arg(x,y)$ satisfies $\nabla\theta = \mathbf F$ locally, but it is
not a single-valued function on the punctured plane.

**23.**

*Strategy: compute the cross product and its norm.*

$\mathbf r_u = (\cos\theta,\sin\theta,1)$ and $\mathbf r_\theta = (-u\sin\theta,u\cos\theta,0)$. Then

$$\mathbf r_u\times\mathbf r_\theta
= \left(0-u\cos\theta,\ -u\sin\theta-0,\ u\cos^2\theta+u\sin^2\theta\right)
= (-u\cos\theta,\ -u\sin\theta,\ u),$$

whose norm is $\sqrt{u^2\cos^2\theta+u^2\sin^2\theta+u^2} = u\sqrt2$. Hence

$$\operatorname{area} = \int_0^{2\pi}\int_0^1 u\sqrt2\,du\,d\theta = \sqrt2\cdot2\pi\cdot\frac12
= \pi\sqrt2 .$$

*Check:* the cone has base radius $1$ and slant height $\sqrt2$, so its lateral area is
$\pi r\ell = \pi\sqrt2$. ✓

**24.**

*Strategy: divergence theorem plus the spherical volume integral.*

$\nabla\cdot\mathbf F = 3x^2+3y^2+3z^2 = 3r^2$. In spherical coordinates over the unit ball,

$$\iiint_V 3r^2\,dV = 3\int_0^{2\pi}\int_0^\pi\int_0^1 r^2\cdot r^2\sin\phi\,dr\,d\phi\,d\theta
= 3\cdot4\pi\cdot\frac15 = \frac{12\pi}{5}.$$

*Check by direct integration:* on the unit sphere $\mathbf F\cdot\mathbf n = x^4+y^4+z^4$, and each of
$\iint x^4\,dS$, $\iint y^4\,dS$, $\iint z^4\,dS$ equals $\frac{4\pi}{5}$ by symmetry, so the total is
$\frac{12\pi}{5}$. ✓

## Advanced

**25.**

*Strategy: differentiate the potential for the direct implication; use the circulation to disprove the
converse; locate the precise step that fails.*

Suppose $\mathbf F = \nabla\phi$ with $\phi$ of class $C^2$ on an open set. Then
$P = \phi_x$, $Q = \phi_y$, $R = \phi_z$, and by equality of mixed partial derivatives

$$R_y-Q_z = \phi_{zy}-\phi_{yz} = 0,\qquad
P_z-R_x = \phi_{xz}-\phi_{zx} = 0,\qquad
Q_x-P_y = \phi_{yx}-\phi_{xy} = 0 ,$$

so $\nabla\times\mathbf F = \mathbf 0$.

For the converse, consider the vortex field of Solution 22. It satisfies $P_y = Q_x$ everywhere on
$\mathbb{R}^2\setminus\{(0,0)\}$, yet its circulation around the unit circle is $2\pi$. If it were a
gradient, the fundamental theorem for line integrals would give circulation
$\phi(A)-\phi(A) = 0$ around every closed curve, a contradiction. Hence it is not conservative.

The usual proof of the converse constructs $\phi(\mathbf x) = \int_{\mathbf x_0}^{\mathbf x}\mathbf F\cdot
d\mathbf r$. This definition presupposes that the integral is independent of the path. On a simply connected
(or star-shaped) domain that can be proved — for instance by Green's theorem applied to a closed loop, or by
the construction of Exercise 35. On the punctured plane a loop around the origin cannot be contracted, the
integral around it is $2\pi$, and the construction produces the multivalued angle rather than a function.
The failure is therefore topological, not differentiability: the field is perfectly smooth where it is
defined.

**26.**

*Strategy: use the area formula $A = \frac12\oint(x\,dy-y\,dx)$ with the given parametrisation.*

$x = \cos^3t$ gives $dx = -3\cos^2t\sin t\,dt$, and $y = \sin^3t$ gives $dy = 3\sin^2t\cos t\,dt$. Then

$$x\,dy = \cos^3t\cdot3\sin^2t\cos t = 3\cos^4t\sin^2t,\qquad
y\,dx = \sin^3t\cdot(-3\cos^2t\sin t) = -3\cos^2t\sin^4t ,$$

so

$$x\,dy-y\,dx = 3\cos^2t\sin^2t\left(\cos^2t+\sin^2t\right) = 3\cos^2t\sin^2t .$$

Therefore

$$A = \frac12\int_0^{2\pi}3\cos^2t\sin^2t\,dt
= \frac32\int_0^{2\pi}\frac{\sin^2 2t}{4}\,dt .$$

Since $\int_0^{2\pi}\sin^2(2t)\,dt = \pi$,

$$A = \frac32\cdot\frac{\pi}{4} = \frac{3\pi}{8}.$$

*Check:* the astroid lies inside the unit disk (area $\pi$) and is visibly smaller; $\frac{3\pi}{8}\approx1.18$
against $\pi\approx3.14$. The known formula for the astroid $x = a\cos^3t$, $y = a\sin^3t$ is
$\frac{3\pi a^2}{8}$, which agrees with $a=1$. ✓

**27.**

*Strategy: Stokes' theorem, then the boundary integral as an independent check.*

*Curl:* with $P = y$, $Q = z$, $R = x$,
$\nabla\times\mathbf F = (R_y-Q_z,\ P_z-R_x,\ Q_x-P_y) = (-1,-1,-1)$.

*Surface side:* on the unit upper hemisphere the outward unit normal is $\mathbf n = (x,y,z)$, so
$(\nabla\times\mathbf F)\cdot\mathbf n = -(x+y+z)$ and

$$\iint_S(\nabla\times\mathbf F)\cdot d\mathbf S = -\iint_S(x+y+z)\,dS .$$

The integrals of $x$ and $y$ vanish by symmetry (the hemisphere is symmetric under $x\mapsto-x$ and
$y\mapsto-y$). For the $z$-term,

$$\iint_S z\,dS = \int_0^{2\pi}\int_0^{\pi/2}\cos\phi\sin\phi\,d\phi\,d\theta
= 2\pi\cdot\frac12 = \pi .$$

Hence the flux is $-\pi$.

*Boundary side:* the boundary is the unit circle in $z=0$, oriented counterclockwise when viewed from above.
With $\mathbf r(t) = (\cos t,\sin t,0)$, $\mathbf r' = (-\sin t,\cos t,0)$ and
$\mathbf F = (\sin t,0,\cos t)$, so $\mathbf F\cdot\mathbf r' = -\sin^2t$ and
$\int_0^{2\pi}(-\sin^2t)\,dt = -\pi$. ✓

**28.**

*Strategy: compute directly on the sphere, then verify with the divergence theorem and the flux through the
flat disk.*

*Direct.* On the unit sphere $\mathbf n = (x,y,z)$ and $\mathbf F = (0,0,z^2)$, so
$\mathbf F\cdot\mathbf n = z^3$. With $z = \cos\phi$ and $dS = \sin\phi\,d\phi\,d\theta$ on the upper
hemisphere,

$$\iint_S\mathbf F\cdot d\mathbf S = \int_0^{2\pi}\int_0^{\pi/2}\cos^3\phi\sin\phi\,d\phi\,d\theta
= 2\pi\left[-\frac{\cos^4\phi}{4}\right]_0^{\pi/2} = \frac{\pi}{2}.$$

*Divergence theorem.* $\nabla\cdot\mathbf F = 2z$, and the half-ball has $z = r\cos\phi$, $dV =
r^2\sin\phi\,dr\,d\phi\,d\theta$:

$$\iiint_V 2z\,dV = 2\int_0^{2\pi}\int_0^{\pi/2}\int_0^1 r\cos\phi\cdot r^2\sin\phi\,dr\,d\phi\,d\theta
= 2\cdot2\pi\cdot\frac14\cdot\frac12 = \frac{\pi}{2}.$$

The boundary of the half-ball is the hemisphere together with the disk $z=0$. On the disk the outward normal
is $-\mathbf k$ and $\mathbf F = (0,0,0)$, so its flux is $0$; hence the whole flux crosses the hemisphere,
matching the direct computation. ✓

**29.**

*Strategy: test the curl in all three components, then integrate.*

With $P = 2xy$, $Q = x^2+2yz$, $R = y^2$:

$$R_y-Q_z = 2y-2y = 0,\qquad P_z-R_x = 0-0 = 0,\qquad Q_x-P_y = 2x-2x = 0 .$$

The domain is $\mathbb{R}^3$, which is star-shaped, so the field is conservative. Integrating,

$$\phi = \int 2xy\,dx = x^2y+g(y,z).$$

Then $\phi_y = x^2+g_y = x^2+2yz$ gives $g_y = 2yz$, so $g = y^2z+h(z)$, and
$\phi_z = y^2+h'(z) = y^2$ gives $h' = 0$. Hence

$$\phi = x^2y+y^2z .$$

*Check:* $\phi_x = 2xy$, $\phi_y = x^2+2yz$, $\phi_z = y^2$. ✓ The work from $(0,0,0)$ to $(1,2,3)$ is
$\phi(1,2,3)-\phi(0,0,0) = 1\cdot2+4\cdot3 = 14$.

**30.**

*Strategy: compute the two tangent vectors, show they are orthogonal, and integrate the area element.*

$\mathbf r_u = \bigl(-(R+r\cos v)\sin u,\ (R+r\cos v)\cos u,\ 0\bigr)$ has norm $R+r\cos v$ (positive for
$R>r$), and $\mathbf r_v = (-r\sin v\cos u,\ -r\sin v\sin u,\ r\cos v)$ has norm $r$. Their dot product is

$$\mathbf r_u\cdot\mathbf r_v = (R+r\cos v)(r\sin v\sin u\cos u - r\sin v\sin u\cos u) + 0 = 0 .$$

Hence $\lVert\mathbf r_u\times\mathbf r_v\rVert = r(R+r\cos v)$ and

$$\operatorname{area} = \int_0^{2\pi}\int_0^{2\pi} r(R+r\cos v)\,du\,dv
= r\left(2\pi R\cdot2\pi + r\int_0^{2\pi}\cos v\,dv\cdot2\pi\right) = 4\pi^2Rr ,$$

because $\int_0^{2\pi}\cos v\,dv = 0$.

*Check:* Pappus's theorem gives area $= (2\pi R)(2\pi r) = 4\pi^2Rr$, the circumference of the circle traced
by the centre times the circumference of the tube. ✓

**31.**

*Strategy: write everything in components and use equality of mixed partials.*

(a) Let $\mathbf G = \nabla\times\mathbf F = (R_y-Q_z,\ P_z-R_x,\ Q_x-P_y)$. Then

$$\nabla\cdot\mathbf G = (R_y-Q_z)_x+(P_z-R_x)_y+(Q_x-P_y)_z
= R_{yx}-R_{xy}+P_{zy}-P_{yz}+Q_{xz}-Q_{zx} = 0$$

by Clairaut's theorem, since $\mathbf F$ is $C^2$.

(b) $\nabla\times\nabla f = (f_{zy}-f_{yz},\ f_{xz}-f_{zx},\ f_{yx}-f_{xy}) = (0,0,0)$.

(c) $\nabla\cdot(f\mathbf F) = (fP)_x+(fQ)_y+(fR)_z = f_xP+fP_x+f_yQ+fQ_y+f_zR+fR_z$, which is
$f(P_x+Q_y+R_z)+(P,Q,R)\cdot(f_x,f_y,f_z) = f\,\nabla\cdot\mathbf F+\mathbf F\cdot\nabla f$. $\blacksquare$

**32.**

*Strategy: apply Green's theorem to the annulus between $C$ and a small circle, where the field is $C^1$.*

Let $D_\varepsilon$ be the region between $C$ and the circle $C_\varepsilon$ of radius $\varepsilon$ centred
at the origin, with $\varepsilon$ so small that $C_\varepsilon$ lies inside $C$. On $D_\varepsilon$ the field
components $P = -y/(x^2+y^2)$ and $Q = x/(x^2+y^2)$ are $C^1$, and $Q_x-P_y = 0$ (Solution 22). Green's
theorem gives

$$\oint_{\partial D_\varepsilon}P\,dx+Q\,dy = \iint_{D_\varepsilon}0\,dA = 0 .$$

The boundary $\partial D_\varepsilon$, oriented with the region on the left, consists of $C$ traversed
counterclockwise and $C_\varepsilon$ traversed **clockwise**. Hence

$$\oint_C-\oint_{C_\varepsilon}=0,\qquad\text{so}\qquad \oint_C=\oint_{C_\varepsilon} .$$

On $C_\varepsilon$ use $\mathbf r(t) = \varepsilon(\cos t,\sin t)$: $dx = -\varepsilon\sin t\,dt$,
$dy = \varepsilon\cos t\,dt$, and $x^2+y^2 = \varepsilon^2$, so

$$\frac{-y\,dx+x\,dy}{x^2+y^2}
= \frac{\varepsilon^2\sin^2t+\varepsilon^2\cos^2t}{\varepsilon^2}\,dt = dt .$$

Therefore $\oint_C = \int_0^{2\pi}dt = 2\pi$, independent of the shape of $C$ and of $\varepsilon$.
$\blacksquare$

## Challenge

**33.**

*Strategy: differentiate, integrate over a sphere, then handle the singularity by excision.*

(a) Write $r = \lVert\mathbf x\rVert$ and $\mathbf F = (x,y,z)/r^3$. For the $x$-component,
$\partial_x(x/r^3) = 1/r^3-3x^2/r^5$. Summing the three components,

$$\nabla\cdot\mathbf F = \frac{3}{r^3}-\frac{3(x^2+y^2+z^2)}{r^5}
= \frac{3}{r^3}-\frac{3r^2}{r^5} = 0 \qquad (r>0).$$

(b) On the sphere of radius $R$, $\mathbf n = \mathbf x/R$ and $\mathbf F = \mathbf x/R^3$, so
$\mathbf F\cdot\mathbf n = (\mathbf x\cdot\mathbf x)/(R^4) = R^2/R^4 = 1/R^2$. The area is $4\pi R^2$, hence

$$\iint_S\mathbf F\cdot d\mathbf S = \frac{1}{R^2}\cdot4\pi R^2 = 4\pi ,$$

independent of $R$.

(c) The divergence theorem requires $\mathbf F$ to be $C^1$ on an open set containing the ball, and
$\mathbf F$ is not even defined at the origin. Applying the theorem formally would give
$\iint_S = \iiint_B 0 = 0$, which contradicts (b). To justify the value, remove the ball of radius
$\varepsilon<R$ and apply the theorem to the shell $V_\varepsilon = \{\varepsilon\le r\le R\}$. There
$\nabla\cdot\mathbf F = 0$, so

$$0 = \iiint_{V_\varepsilon}0\,dV
= \iint_{r=R}\mathbf F\cdot d\mathbf S+\iint_{r=\varepsilon}\mathbf F\cdot d\mathbf S ,$$

where both normals are outward from the shell: the outer normal is $\mathbf x/R$ on the outer sphere, but the
inner normal is $-\mathbf x/\varepsilon$ on the inner sphere. The second integral is therefore
$-4\pi$, and the first is $4\pi$ — the same value as (b). For a general closed surface enclosing the origin,
apply the same argument to the region between the surface and a small sphere; the two fluxes are equal, so
every such surface has flux $4\pi$. $\blacksquare$

**34.**

*Strategy: apply the divergence theorem to the vector field $f\nabla g$.*

By the product rule, $\nabla\cdot(f\nabla g) = f\,\nabla\cdot\nabla g+\nabla f\cdot\nabla g
= f\,\nabla^2g+\nabla f\cdot\nabla g$. Applying the divergence theorem to $f\nabla g$ on $V$ gives

$$\iiint_V\left(f\,\nabla^2g+\nabla f\cdot\nabla g\right)dV
= \iint_{\partial V} f\,\nabla g\cdot\mathbf n\,dS ,$$

which is the first identity. Interchanging $f$ and $g$ gives

$$\iiint_V\left(g\,\nabla^2f+\nabla g\cdot\nabla f\right)dV
= \iint_{\partial V} g\,\nabla f\cdot\mathbf n\,dS .$$

Subtracting the second display from the first cancels $\nabla f\cdot\nabla g$ and yields

$$\iiint_V\left(f\,\nabla^2g-g\,\nabla^2f\right)dV
= \iint_{\partial V}\left(f\,\partial_ng-g\,\partial_nf\right)dS ,$$

with $\partial_ng = \nabla g\cdot\mathbf n$. $\blacksquare$

**35.**

*Strategy: differentiate under the integral sign and recognise a total derivative.*

Since $D$ is star-shaped about $\mathbf 0$, the point $t\mathbf x$ lies in $D$ for $0\le t\le1$, so the
integrand is defined. Write $\phi(\mathbf x) = \int_0^1\sum_iF_i(t\mathbf x)x_i\,dt$ and differentiate with
respect to $x_j$ (the integrand and its derivative are continuous, so differentiation under the integral is
permitted):

$$\frac{\partial\phi}{\partial x_j}
= \int_0^1\left[F_j(t\mathbf x)+t\sum_i\frac{\partial F_i}{\partial x_j}(t\mathbf x)\,x_i\right]dt .$$

On the other hand, the total derivative of $t\mapsto tF_j(t\mathbf x)$ is

$$\frac{d}{dt}\left[tF_j(t\mathbf x)\right]
= F_j(t\mathbf x)+t\sum_i\frac{\partial F_j}{\partial x_i}(t\mathbf x)\,x_i .$$

Integrating from $0$ to $1$ and using the Fundamental Theorem of Calculus,

$$F_j(\mathbf x) = \left[tF_j(t\mathbf x)\right]_{t=0}^{t=1}
= \int_0^1F_j(t\mathbf x)\,dt+\int_0^1t\sum_i\frac{\partial F_j}{\partial x_i}(t\mathbf x)\,x_i\,dt .$$

Subtracting this from the expression for $\partial\phi/\partial x_j$ gives

$$\frac{\partial\phi}{\partial x_j}-F_j(\mathbf x)
= \int_0^1t\sum_i\left[\frac{\partial F_i}{\partial x_j}-\frac{\partial F_j}{\partial x_i}\right](t\mathbf x)\,x_i\,dt .$$

The curl-free condition says exactly $\partial F_i/\partial x_j = \partial F_j/\partial x_i$ for all $i,j$,
so every bracket vanishes and $\partial\phi/\partial x_j = F_j$. As $j$ was arbitrary, $\nabla\phi = \mathbf F$.
$\blacksquare$

**36.**

*Strategy: compute the flux, differentiate, then apply Stokes' theorem to a circle.*

(a) The loop bounds the disk of radius $a$ in the plane $z=0$, with normal $\mathbf k$. Since
$\mathbf B = (0,0,B_0t)$ is constant on the disk,

$$\Phi(t) = \iint_S\mathbf B\cdot d\mathbf S = B_0t\cdot\pi a^2 .$$

(b) The electromotive force is

$$\mathcal{E} = -\frac{d\Phi}{dt} = -\pi a^2B_0 .$$

(c) Faraday's law in integral form is $\oint_{\partial S}\mathbf E\cdot d\mathbf r = \mathcal{E}$. By
rotational symmetry the induced field is azimuthal and has constant magnitude $E_\theta$ on the loop, so
$\oint\mathbf E\cdot d\mathbf r = E_\theta\cdot2\pi a$. Hence

$$E_\theta = \frac{-\pi a^2B_0}{2\pi a} = -\frac{aB_0}{2}.$$

(d) Lenz's law: for $B_0>0$ the flux in the $+\mathbf k$ direction is increasing, so the induced current must
produce a magnetic field in the $-\mathbf k$ direction, which means it circulates clockwise when viewed from
$+z$. Since $\mathbf e_\theta$ is the counterclockwise direction, the induced field must have
$E_\theta<0$, consistent with (c). ✓
