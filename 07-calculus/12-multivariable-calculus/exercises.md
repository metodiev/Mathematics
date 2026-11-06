# Exercises: Multivariable Calculus

> Companion to the [tutorial](README.md). Solutions are in [solutions.md](solutions.md).

Attempt every problem before opening the [solutions](solutions.md). The problems are grouped by
level and numbered continuously, so that the solution file mirrors the numbering exactly. Problems
marked *proof* require a complete written argument, not a computation.

## Beginner

**1.** Find the domain and the range of $f(x,y) = \ln(4-x^2-y^2)$. Describe the level curves
$f = \ln 3$ and $f = \ln 4$.

**2.** Find and sketch the domain of $g(x,y,z) = \sqrt{1-x^2-y^2-z^2} + \ln(x+y)$.

**3.** Describe the level curves of $f(x,y) = x^2+9y^2$ at levels $c = 0$, $c = 9$ and $c = 36$, and
identify each curve.

**4.** Compute $\partial f/\partial x$ and $\partial f/\partial y$ for
$f(x,y) = x^3y^2 - 2xy + 5y$, and evaluate both at $(1,-1)$.

**5.** For $f(x,y) = e^{x^2y}$, compute $f_x$ and $f_y$, and evaluate them at $(1,2)$.

**6.** Compute $f_x$ and $f_y$ for $f(x,y) = \sin(x/y)$.

**7.** Evaluate $\displaystyle\lim_{(x,y)\to(0,0)} \frac{x^2y}{x^2+y^2}$.

**8.** Show that $\displaystyle\lim_{(x,y)\to(0,0)} \frac{x^2-y^2}{x^2+y^2}$ does not exist.

**9.** Find the tangent plane and the normal line to the surface $z = x^2+y^2$ at the point
$(1,2,5)$.

**10.** For $f(x,y) = x^2-y^2$ at the point $(1,1)$, find the directional derivative in the direction
of $\mathbf{v} = (3,4)$, and then in the direction of $\mathbf{w} = (1,1)$.

**11.** Let $z = e^{x}\sin y$ with $x = t^2$ and $y = 3t$. Find $dz/dt$ by the chain rule.

**12.** Evaluate $\displaystyle\int_0^1\!\!\int_0^2 (x+y)\,dy\,dx$.

**13.** Using polar coordinates, evaluate $\displaystyle\iint_D (x^2+y^2)\,dA$, where $D$ is the disk
$x^2+y^2\le 4$.

## Intermediate

**14.** For $f(x,y) = x^2y^3 + \sin(xy)$, compute $f_{xy}$ and $f_{yx}$ and verify that they agree.
Which theorem guarantees the equality, and are its hypotheses satisfied?

**15.** Find the tangent plane and the normal line to the ellipsoid $x^2+2y^2+3z^2 = 6$ at the point
$(1,1,1)$.

**16.** Let $z = \ln(x^2+y^2)$ with $x = st$ and $y = s/t$. Compute $\partial z/\partial s$ and
$\partial z/\partial t$ at $(s,t) = (1,2)$ by the chain rule, then verify the answers by substituting
first.

**17.** The surface $x^2+y^2+z^2 = 6$ passes through $P = (1,1,2)$. Find $\partial z/\partial x$ and
$\partial z/\partial y$ at $P$ by implicit differentiation, and write down the tangent plane at $P$.

**18.** For $f(x,y) = x^2y+y^3$ at the point $(1,1)$, find the direction and rate of steepest ascent,
the direction of steepest descent, and the directional derivative in the direction $(1,-1)$.

**19.** Find and classify all critical points of $f(x,y) = 4xy - x^4 - y^4$.

**20.** Evaluate $\displaystyle\iint_T e^{x^2}\,dA$, where $T$ is the triangle
$0\le y\le x\le 1$. (Integrate in $y$ first.)

**21.** Find the volume of the solid bounded below by the paraboloid $z = x^2+y^2$ and above by the
plane $z = 4$.

**22.** Use cylindrical coordinates to find the volume of the cone
$z\ge\sqrt{x^2+y^2}$, $0\le z\le 1$.

**23.** Find the maximum and the minimum of $f(x,y) = x^2y$ on the circle $x^2+y^2 = 3$.

**24.** Find the shortest distance from the origin to the plane $x+2y+3z = 14$, and the point of the
plane at which it is attained.

## Advanced

**25.** *(proof)* Let $U\subseteq\mathbb{R}^n$ be open and let $f:U\to\mathbb{R}$ be differentiable at
$\mathbf{a}\in U$. Prove that $f$ is continuous at $\mathbf{a}$.

**26.** *(proof)* Let $f$ be defined on an open set containing $(a,b)$, and suppose $f_x$ and $f_y$
exist on a neighbourhood of $(a,b)$ and are continuous at $(a,b)$. Prove that $f$ is differentiable at
$(a,b)$.

**27.** *(proof)* Let $f$ be differentiable, let $c\in\mathbb{R}$, and let $\gamma$ be a differentiable
curve lying in the level set $f = c$, with $\gamma(0) = \mathbf{a}$ and $\gamma'(0)\ne\mathbf{0}$.
Prove that $\nabla f(\mathbf{a})\cdot\gamma'(0) = 0$, and explain why this says that the gradient is
normal to the level curve.

**28.** *(proof)* Let $f$ be $C^2$ on a neighbourhood of a critical point $(a,b)$, and set
$A = f_{xx}(a,b)$, $B = f_{xy}(a,b)$, $C = f_{yy}(a,b)$, $D = AC-B^2$ (with $A\ne0$). Prove:
(a) if $D>0$ and $A>0$, then $(a,b)$ is a strict local minimum; (b) if $D<0$, then $(a,b)$ is not a
local extremum.

**29.** For
$$f(x,y) = \begin{cases} xy\,\dfrac{x^2-y^2}{x^2+y^2}, & (x,y)\ne(0,0),\\ 0, & (x,y)=(0,0),\end{cases}$$
compute $f_x(0,y)$ for $y\ne0$ and $f_y(x,0)$ for $x\ne0$, and deduce $f_{xy}(0,0)$ and $f_{yx}(0,0)$.
Explain why Clairaut's theorem does not apply.

**30.** Show that the two iterated integrals of
$$f(x,y) = \frac{x^2-y^2}{(x^2+y^2)^2}$$
over the unit square differ, and explain why Fubini's theorem does not apply.

**31.** *(proof)* State and derive the chain rule for $z = f(x(t),y(t))$, and identify precisely the
point at which differentiability of $f$ — rather than the mere existence of its partial derivatives —
is used.

**32.** Find the $z$-coordinate of the centre of mass of the upper unit hemisphere
$x^2+y^2+z^2\le 1$, $z\ge0$, with constant density.

**33.** Maximise and minimise $f(x,y,z) = x+y+z$ subject to the two constraints $x^2+y^2 = 1$ and
$y+z = 1$.

**34.** Find the area of the region in the first quadrant bounded by the curves $xy = 1$, $xy = 4$,
$y = x$ and $y = 4x$, using the substitution $u = xy$, $v = y/x$.

## Challenge

**35.** Let
$$f(x,y) = \begin{cases} (x^2+y^2)\sin\dfrac{1}{x^2+y^2}, & (x,y)\ne(0,0),\\ 0, & (x,y)=(0,0).\end{cases}$$
(a) Show that $f$ is differentiable at the origin and find its derivative there. (b) Show that $f_x$
is unbounded in every neighbourhood of the origin. (c) What does this example show about the converse
of the theorem "continuous partials imply differentiability"?

**36.** Find the volume of the solid inside the sphere $x^2+y^2+z^2 = 4$ and above the cone
$z = \sqrt{x^2+y^2}$.

**37.** *(proof)* Use Lagrange multipliers to prove the weighted AM–GM inequality: for positive
$a,b,c,x,y,z$,
$$\frac{ax+by+cz}{a+b+c} \ge x^{a/(a+b+c)}\,y^{b/(a+b+c)}\,z^{c/(a+b+c)} .$$

**38.** Show that the second-derivative test is inconclusive when $D=0$ by giving three $C^2$
functions whose Hessian discriminant vanishes at the origin and which have, respectively, a strict
local minimum, a strict local maximum, and neither.

**39.** *(proof)* Prove that $\displaystyle\int_{-\infty}^{\infty} e^{-x^2}\,dx = \sqrt{\pi}$ by
squaring the integral, using polar coordinates, and justifying the limits.

**40.** Evaluate $\displaystyle\int_0^{\sqrt{\pi}}\!\!\int_y^{\sqrt{\pi}} \sin(x^2)\,dx\,dy$ by
reversing the order of integration.
