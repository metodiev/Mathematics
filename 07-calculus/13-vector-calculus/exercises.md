# Vector Calculus — Exercises

> [Vector Calculus](README.md) · 36 problems · Beginner → Challenge · Solutions: [solutions.md](solutions.md)

Work through the problems in order; each cites the section of the tutorial it draws on. Every problem that
asks for an integral over a curve or surface specifies its orientation, and you should state yours before
computing. A sign error is the most common failure in this topic, so check the orientation of every answer.

Notation: $\mathbf i,\mathbf j,\mathbf k$ is the standard basis, $\mathbf r$ is a position vector, and all
curves and surfaces are oriented as stated.

## Beginner

**1.** *(§5.3, §7.1)* Describe the field lines of (a) $\mathbf F(x,y) = (x,y)$ and (b) $\mathbf F(x,y) =
(-y,x)$ by solving $\mathbf r'(t) = \mathbf F(\mathbf r(t))$. Sketch both families.

**2.** *(§5.6)* Compute the divergence and the curl of
$\mathbf F(x,y,z) = \bigl(x^2y,\ yz,\ xz^2\bigr)$.

**3.** *(§7.2)* Show that $\mathbf F(x,y) = \bigl(y\cos(xy),\ x\cos(xy)\bigr)$ is conservative and find a
potential.

**4.** *(§5.5)* Evaluate $\displaystyle\int_C (x+y)\,ds$, where $C$ is the straight segment from $(0,0)$ to
$(1,2)$.

**5.** *(§7.4)* Evaluate $\displaystyle\int_C \mathbf F\cdot d\mathbf r$ for $\mathbf F(x,y) = (x,y)$ along
the parabola $y = x^2$ from $(0,0)$ to $(1,1)$.

**6.** *(§7.4)* Compute the circulation of $\mathbf F(x,y) = (-y,x)$ around the circle of radius $3$ centred
at the origin, traversed counterclockwise.

**7.** *(§7.8)* Find the surface area of the graph $z = x+2y$ over the unit square $0\le x,y\le1$.

**8.** *(§7.8)* Derive the surface area of the sphere of radius $R$ from the parametrisation
$\mathbf r(\phi,\theta) = R(\sin\phi\cos\theta,\sin\phi\sin\theta,\cos\phi)$.

**9.** *(§7.8)* Evaluate $\displaystyle\iint_S z\,dS$, where $S$ is the upper hemisphere of radius $2$
centred at the origin.

**10.** *(§7.9)* Compute the flux of $\mathbf F(x,y,z) = (x,0,0)$ through the unit square in the plane $x=1$
given by $0\le y\le1$, $0\le z\le1$, with normal $+\mathbf i$.

**11.** *(§7.2)* Determine whether $\mathbf F(x,y) = (2xy,\ x^2)$ is conservative. If it is, find a
potential and evaluate $\int_C\mathbf F\cdot d\mathbf r$ from $(0,0)$ to $(1,3)$.

**12.** *(§7.7)* Use Green's theorem to evaluate $\displaystyle\oint_C x\,dy$, where $C$ is the boundary of
the unit square $[0,1]^2$ traversed counterclockwise.

## Intermediate

**13.** *(§7.5)* Let $\mathbf F(x,y) = (y^2,\ 2xy)$ and let $A = (0,0)$, $B = (2,1)$. Evaluate
$\int_C\mathbf F\cdot d\mathbf r$ (a) along the straight segment from $A$ to $B$, (b) along the path
$A\to(2,0)\to B$, and (c) using a potential. Compare.

**14.** *(§7.3)* Evaluate $\displaystyle\int_C (x^2+y^2)\,ds$, where $C$ is the circle of radius $a$ centred
at the origin.

**15.** *(§7.3)* Evaluate $\displaystyle\int_C (2x+3y)\,ds$, where $C$ is the segment from $(1,0)$ to
$(0,1)$.

**16.** *(§7.7)* Use Green's theorem to evaluate
$\displaystyle\oint_C (x^2-y)\,dx+(x+y^2)\,dy$, where $C$ is the boundary of the square $[0,1]^2$ traversed
counterclockwise. Verify the answer by computing the line integral directly along the four sides.

**17.** *(§7.11)* Use the divergence theorem to compute the flux of $\mathbf F(\mathbf x) = \mathbf x$ through
the sphere of radius $R$ centred at the origin, with the outward normal.

**18.** *(§7.10)* Verify Stokes' theorem for $\mathbf F(x,y,z) = (z,x,y)$ on the paraboloid
$z = 1-x^2-y^2$, $z\ge0$, with the upward normal.

**19.** *(§7.11)* Use the divergence theorem to compute the flux of
$\mathbf F(x,y,z) = (x^2,y^2,z^2)$ through the boundary of the unit cube $[0,1]^3$, with the outward normal.

**20.** *(§7.2)* Show that $\mathbf F(x,y,z) = \bigl(2xy+z^2,\ x^2+2yz,\ y^2+2zx\bigr)$ is conservative, find a
potential, and compute the work done from $(0,0,0)$ to $(1,1,1)$.

**21.** *(§7.8)* Evaluate $\displaystyle\iint_S (x^2+y^2)\,dS$, where $S$ is the part of the cone
$z = \sqrt{x^2+y^2}$ with $0\le z\le1$.

**22.** *(§7.2, §7.6)* For the vortex field
$\mathbf F(x,y) = \bigl(-y/(x^2+y^2),\ x/(x^2+y^2)\bigr)$ on $\mathbb{R}^2\setminus\{(0,0)\}$: show that
$P_y = Q_x$, compute the circulation around the unit circle traversed counterclockwise, and explain why the
result does not contradict the curl test.

**23.** *(§7.8)* Compute the area of the surface parametrised by
$\mathbf r(u,\theta) = (u\cos\theta,\ u\sin\theta,\ u)$ for $0\le u\le1$, $0\le\theta<2\pi$.

**24.** *(§7.11)* Use the divergence theorem to compute the flux of
$\mathbf F(x,y,z) = (x^3,y^3,z^3)$ through the unit sphere with the outward normal.

## Advanced

**25.** *(§7.5)* Prove that a conservative field with a $C^2$ potential is curl-free. Then explain, using the
vortex field, why the converse fails on the punctured plane, and identify exactly where the usual proof of
the converse breaks down.

**26.** *(§7.7)* Use Green's theorem to compute the area enclosed by the astroid
$x(t) = \cos^3 t$, $y(t) = \sin^3 t$, $0\le t\le2\pi$.

**27.** *(§7.10)* Use Stokes' theorem to evaluate $\displaystyle\iint_S(\nabla\times\mathbf F)\cdot d\mathbf S$
for $\mathbf F(x,y,z) = (y,z,x)$ and $S$ the upper unit hemisphere $z\ge0$, with the upward normal. Verify
the answer by computing the boundary integral.

**28.** *(§7.11)* Compute the flux of $\mathbf F(x,y,z) = (0,0,z^2)$ through the upper unit hemisphere with
the upward normal, both directly and by the divergence theorem.

**29.** *(§7.2)* Test $\mathbf F(x,y,z) = \bigl(2xy,\ x^2+2yz,\ y^2\bigr)$ for conservativeness; if it is
conservative, find a potential and evaluate the work from $(0,0,0)$ to $(1,2,3)$.

**30.** *(§7.8)* Show that the area of the torus
$\mathbf r(u,v) = \bigl((R+r\cos v)\cos u,\ (R+r\cos v)\sin u,\ r\sin v\bigr)$, $0\le u,v<2\pi$, is
$4\pi^2Rr$.

**31.** *(§5.6)* Using components, prove that (a) $\nabla\cdot(\nabla\times\mathbf F) = 0$ for every $C^2$
field, (b) $\nabla\times(\nabla f) = \mathbf 0$ for every $C^2$ function, and (c)
$\nabla\cdot(f\mathbf F) = f\,\nabla\cdot\mathbf F+\mathbf F\cdot\nabla f$.

**32.** *(§7.7)* Let $C$ be a positively oriented simple closed curve whose interior contains the origin.
Using Green's theorem on the region between $C$ and a small circle centred at the origin, show that

$$\oint_C \frac{-y\,dx+x\,dy}{x^2+y^2} = 2\pi .$$

## Challenge

**33.** *(§7.11)* Let $\mathbf F(\mathbf x) = \mathbf x/\lVert\mathbf x\rVert^3$ on
$\mathbb{R}^3\setminus\{\mathbf 0\}$. (a) Show that $\nabla\cdot\mathbf F = 0$ away from the origin.
(b) Compute the flux of $\mathbf F$ through the sphere of radius $R$ centred at the origin. (c) Explain why
the divergence theorem applied to the solid ball would give the wrong answer, and show that the flux through
any closed surface enclosing the origin is $4\pi$.

**34.** *(§7.11)* Prove Green's first identity

$$\iiint_V \left(f\,\nabla^2 g+\nabla f\cdot\nabla g\right)dV
= \iint_{\partial V} f\,\nabla g\cdot\mathbf n\,dS ,$$

and deduce Green's second identity
$\iiint_V(f\nabla^2g-g\nabla^2f)\,dV = \iint_{\partial V}(f\,\partial_n g-g\,\partial_n f)\,dS$, where
$\partial_n g = \nabla g\cdot\mathbf n$.

**35.** *(§7.5)* Let $D$ be a star-shaped open set with centre $\mathbf 0$, and let $\mathbf F$ be a $C^1$
curl-free field on $D$. Define

$$\phi(\mathbf x) = \int_0^1 \mathbf F(t\mathbf x)\cdot\mathbf x\,dt .$$

Show that $\nabla\phi = \mathbf F$, filling in every step: differentiate under the integral sign, use
$\frac{d}{dt}\left[tF_j(t\mathbf x)\right] = F_j(t\mathbf x)+t\sum_i\partial_iF_j(t\mathbf x)x_i$, and use
the curl-free conditions.

**36.** *(§7.10, §7.11)* A uniform magnetic field $\mathbf B(t) = (0,0,B_0t)$ passes through a circular loop
of radius $a$ lying in the plane $z=0$ and centred at the origin. (a) Compute the magnetic flux through the
loop with the normal $+\mathbf k$. (b) Compute the electromotive force
$\mathcal{E} = -\dfrac{d\Phi}{dt}$. (c) Assuming the induced electric field is azimuthal,
$\mathbf E = E_\theta(a)\,\mathbf e_\theta$ on the loop, use Stokes' theorem to find $E_\theta$. (d) Check
the sign with Lenz's law.
