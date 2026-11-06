# Solutions: Multivariable Calculus

> Companion to [exercises.md](exercises.md) and the [tutorial](README.md).

Each solution states the strategy first, then carries out every significant step. Alternative
approaches and common pitfalls are noted where they matter.

## Beginner

**1.** *Strategy: the logarithm is defined on positive arguments; then describe the level sets from
the equation $4-x^2-y^2 = e^c$.*

The argument must be positive: $4-x^2-y^2>0$, i.e. $x^2+y^2<4$. The domain is the open disk of
radius $2$ centred at the origin.

For the range, $r^2 = x^2+y^2$ ranges over $[0,4)$, so $4-r^2$ ranges over $(0,4]$ and
$f = \ln(4-r^2)$ ranges over $(-\infty,\ln 4]$. The value $\ln 4$ is attained only at the origin, and
values tend to $-\infty$ as $r\to2^-$.

Level curves: $\ln(4-r^2) = c$ means $r^2 = 4-e^c$, which requires $e^c\le4$, i.e. $c\le\ln4$.

* $c = \ln 3$: $r^2 = 4-3 = 1$, the circle of radius $1$ centred at the origin.
* $c = \ln 4$: $r^2 = 0$, the single point $(0,0)$ — the level set degenerates because $\ln4$ is the
  maximum of $f$.

**2.** *Strategy: two conditions, one from the square root (closed) and one from the logarithm (open).*

The square root requires $1-x^2-y^2-z^2\ge0$, that is $x^2+y^2+z^2\le1$: the closed unit ball. The
logarithm requires $x+y>0$: the open half-space on one side of the plane $x+y=0$. Hence
$$\operatorname{dom} g = \{(x,y,z) : x^2+y^2+z^2\le1,\ x+y>0\}.$$
It is the part of the closed ball lying strictly on the side $x+y>0$ of the plane. Its boundary
consists of the spherical cap $\{x^2+y^2+z^2 = 1,\ x+y\ge0\}$ together with the closed disk
$\{x^2+y^2+z^2\le1,\ x+y = 0\}$. For example the north pole $(0,0,1)$ has $x+y = 0$ and does not
belong to the domain.

**3.** *Strategy: complete the squares / divide by $c$ to recognise a conic.*

The level set is $x^2+9y^2 = c$.

* $c = 0$: $x^2+9y^2 = 0$ forces $x = y = 0$; the level set is the single point $(0,0)$.
* $c = 9$: $x^2/9 + y^2 = 1$, an ellipse with semi-axis $3$ in the $x$-direction and $1$ in the
  $y$-direction.
* $c = 36$: $x^2/36 + y^2/4 = 1$, an ellipse with semi-axes $6$ and $2$.

For $c<0$ the level set is empty. The level curves are ellipses whose axes grow like $\sqrt c$, all
with the same eccentricity — the contour map of an elliptic paraboloid stretched in the $y$-direction.

**4.** *Strategy: differentiate in one variable, treating the other as a constant.*

With $y$ constant,
$$f_x = \frac{\partial}{\partial x}\left(x^3y^2-2xy+5y\right) = 3x^2y^2-2y .$$
With $x$ constant,
$$f_y = \frac{\partial}{\partial y}\left(x^3y^2-2xy+5y\right) = 2x^3y-2x+5 .$$
At $(1,-1)$: $f_x(1,-1) = 3\cdot1\cdot1 - 2(-1) = 3+2 = 5$ and
$f_y(1,-1) = 2\cdot1\cdot(-1) - 2 + 5 = 1$. The term $5y$ contributes $5$ to $f_y$ and nothing to
$f_x$, which is the point of the exercise.

**5.** *Strategy: chain rule in the varying variable, constant multiple in the other.*

$f_x = e^{x^2y}\cdot\frac{\partial}{\partial x}(x^2y) = 2xy\,e^{x^2y}$, and
$f_y = e^{x^2y}\cdot\frac{\partial}{\partial y}(x^2y) = x^2e^{x^2y}$.
At $(1,2)$: $f_x(1,2) = 2\cdot1\cdot2\,e^{2} = 4e^2$ and $f_y(1,2) = 1^2e^{2} = e^2$.

**6.** *Strategy: chain rule with inner function $x/y$.*

$$f_x = \cos\!\left(\frac xy\right)\cdot\frac{\partial}{\partial x}\left(\frac xy\right)
= \frac{1}{y}\cos\!\left(\frac xy\right),$$
$$f_y = \cos\!\left(\frac xy\right)\cdot\frac{\partial}{\partial y}\left(\frac xy\right)
= -\frac{x}{y^2}\cos\!\left(\frac xy\right).$$
Both formulas require $y\ne0$, which is the domain of $f$.

**7.** *Strategy: bound the absolute value by a function of $y$ alone.*

Since $x^2\le x^2+y^2$,
$$0\le\left\lvert\frac{x^2y}{x^2+y^2}\right\rvert = \frac{x^2}{x^2+y^2}\lvert y\rvert \le \lvert y\rvert
\longrightarrow 0 .$$
By the squeeze theorem the limit is $0$. In polar coordinates the same bound reads
$\lvert f\rvert = \lvert r\cos^2\theta\sin\theta\rvert\le r\to0$. This function therefore has a
continuous extension to the origin with value $0$; contrast Exercise 8.

**8.** *Strategy: exhibit two paths with different limits.*

Along the $x$-axis ($y=0$, $x\ne0$):
$$f(x,0) = \frac{x^2-0}{x^2+0} = 1 \longrightarrow 1 .$$
Along the $y$-axis ($x=0$, $y\ne0$):
$$f(0,y) = \frac{0-y^2}{0+y^2} = -1 \longrightarrow -1 .$$
Two paths to the origin give different limits, so the limit does not exist. (Along $y=x$ the value is
$0$ for every $x\ne0$, a third value.) Consequently $f$ has no continuous extension to the origin.

**9.** *Strategy: tangent plane $z = f(a,b)+f_x(a,b)(x-a)+f_y(a,b)(y-b)$.*

$f(x,y) = x^2+y^2$ gives $f(1,2) = 5$, $f_x = 2x$ so $f_x(1,2) = 2$, and $f_y = 2y$ so
$f_y(1,2) = 4$. The tangent plane is
$$z = 5 + 2(x-1) + 4(y-2) = 2x+4y-5 .$$
The upward normal is $(-f_x,-f_y,1) = (-2,-4,1)$, so the normal line is
$$(x,y,z) = (1,2,5) + t\,(-2,-4,1), \qquad t\in\mathbb{R}.$$
*Check:* at $(x,y)=(1,2)$ the plane gives $z = 2+8-5 = 5 = f(1,2)$; the coefficients of $x-1$ and
$y-2$ are the two partial derivatives, as they must be.

**10.** *Strategy: normalise the direction vectors before using $D_{\mathbf{u}}f = \nabla f\cdot\mathbf{u}$.*

$\nabla f = (2x,-2y)$, so $\nabla f(1,1) = (2,-2)$.

For $\mathbf{v} = (3,4)$, $\lVert\mathbf{v}\rVert = 5$ and
$\mathbf{u} = (3/5,4/5)$. Then
$$D_{\mathbf{u}}f(1,1) = (2,-2)\cdot\left(\tfrac35,\tfrac45\right) = \frac{6-8}{5} = -\frac25 .$$
For $\mathbf{w} = (1,1)$, $\lVert\mathbf{w}\rVert = \sqrt2$ and
$$D_{\mathbf{u}}f(1,1) = (2,-2)\cdot\frac{(1,1)}{\sqrt2} = \frac{2-2}{\sqrt2} = 0 .$$
The second answer is zero because $(1,1)$ is orthogonal to the gradient, i.e. tangent to the level
curve $x^2-y^2 = 0$ through $(1,1)$. Using the unnormalised vector $(3,4)$ would have given $-2$
instead of $-2/5$.

**11.** *Strategy: tree diagram $z \leftarrow (x,y) \leftarrow t$.*

$$\frac{dz}{dt} = \frac{\partial z}{\partial x}\frac{dx}{dt}
+ \frac{\partial z}{\partial y}\frac{dy}{dt}
= \left(e^x\sin y\right)(2t) + \left(e^x\cos y\right)(3).$$
Substituting $x = t^2$, $y = 3t$:
$$\frac{dz}{dt} = e^{t^2}\left(2t\sin 3t + 3\cos 3t\right).$$
*Check at $t=0$:* the formula gives $e^0(0+3) = 3$. Directly, $z(t) = e^{t^2}\sin 3t$, so
$z'(0) = 1\cdot 3 = 3$, since the derivative is $2t e^{t^2}\sin3t + 3e^{t^2}\cos3t$. Both agree.

**12.** *Strategy: Fubini on a rectangle — integrate in $y$, then in $x$.*

$$\int_0^1\!\!\int_0^2 (x+y)\,dy\,dx
= \int_0^1\left[xy+\frac{y^2}{2}\right]_{y=0}^{y=2}dx
= \int_0^1\left(2x+2\right)dx
= \left[x^2+2x\right]_0^1 = 3 .$$
*Check:* the integral of $x$ over the rectangle is $\left(\int_0^1x\,dx\right)(2) = 1$, and the integral
of $y$ is $(1)\left(\int_0^2 y\,dy\right) = 2$; the sum is $3$, as found.

**13.** *Strategy: polar coordinates, $dA = r\,dr\,d\theta$.*

On the disk, $x^2+y^2 = r^2$ and the limits are $0\le r\le2$, $0\le\theta<2\pi$:
$$\iint_D (x^2+y^2)\,dA = \int_0^{2\pi}\!\!\int_0^2 r^2\cdot r\,dr\,d\theta
= 2\pi\left[\frac{r^4}{4}\right]_0^2 = 2\pi\cdot4 = 8\pi .$$
The factor $r$ is the Jacobian; omitting it would give
$\int_0^{2\pi}\int_0^2 r^2\,dr\,d\theta = \frac{16\pi}{3}$, which is wrong by a factor $\frac32$. A
quick dimensional check: the integrand is a length squared and the area element a length squared, so
the answer must have units of length to the fourth; $8\pi = 2\pi\cdot 2^4/4$ is consistent with the
disk of radius $2$.

## Intermediate

**14.** *Strategy: differentiate twice, in both orders, and compare.*

With $f = x^2y^3+\sin(xy)$:
$$f_x = 2xy^3 + y\cos(xy), \qquad f_y = 3x^2y^2 + x\cos(xy).$$
Differentiating $f_x$ in $y$:
$$f_{xy} = 6xy^2 + \cos(xy) - xy\sin(xy),$$
where the derivative of $y\cos(xy)$ is $\cos(xy) - xy\sin(xy)$ (product rule, then chain rule).
Differentiating $f_y$ in $x$:
$$f_{yx} = 6xy^2 + \cos(xy) - xy\sin(xy),$$
since the derivative of $x\cos(xy)$ is $\cos(xy) - xy\sin(xy)$. The two agree.

The theorem is Clairaut–Schwarz. Its hypotheses — existence of $f_x,f_y,f_{xy},f_{yx}$ near the point
and continuity of $f_{xy},f_{yx}$ there — hold at every point: $f$ is a sum of a polynomial and of
$\sin(xy)$, and all its partial derivatives of every order are continuous on $\mathbb{R}^2$.

**15.** *Strategy: the level surface $F = 6$ has normal $\nabla F$.*

With $F(x,y,z) = x^2+2y^2+3z^2$, $\nabla F = (2x,4y,6z)$ and $\nabla F(1,1,1) = (2,4,6)$, parallel to
$(1,2,3)$. The tangent plane is
$$2(x-1)+4(y-1)+6(z-1) = 0, \quad\text{equivalently}\quad x+2y+3z = 6 .$$
The normal line is $(x,y,z) = (1,1,1)+t(1,2,3)$.
*Check:* $P = (1,1,1)$ satisfies the plane, since $1+2+3 = 6$. The plane meets the ellipsoid in a
single point — it is the tangent plane — which is consistent with the ellipsoid lying on one side of
it.

**16.** *Strategy: chain rule with $z = \ln(x^2+y^2)$, then verify by substitution.*

$z_x = \dfrac{2x}{x^2+y^2}$ and $z_y = \dfrac{2y}{x^2+y^2}$. The coordinate derivatives are
$x_s = t$, $y_s = 1/t$, $x_t = s$, $y_t = -s/t^2$. At $(s,t) = (1,2)$: $x = 2$, $y = 1/2$ and
$x^2+y^2 = 4+\frac14 = \frac{17}{4}$.

$$\frac{\partial z}{\partial s} = z_x x_s + z_y y_s
= \frac{2\cdot2}{17/4}\cdot2 + \frac{2\cdot(1/2)}{17/4}\cdot\frac12
= \frac{8+1/2}{17/4} = \frac{17/2}{17/4} = 2 .$$
$$\frac{\partial z}{\partial t} = z_x x_t + z_y y_t
= \frac{4}{17/4}\cdot1 + \frac{1}{17/4}\cdot\left(-\frac14\right)
= \frac{4-1/4}{17/4} = \frac{15}{17} .$$
*Verification by substitution:* $x^2+y^2 = s^2t^2 + s^2/t^2$, so
$z = \ln(s^2(t^2+t^{-2})) = 2\ln s + \ln(t^2+t^{-2})$. Hence $z_s = 2/s$, which is $2$ at $s=1$, and
$$z_t = \frac{2t-2t^{-3}}{t^2+t^{-2}} = \frac{4-\frac14}{4+\frac14} = \frac{15/4}{17/4} = \frac{15}{17}.$$
Both routes agree.

**17.** *Strategy: differentiate $F(x,y,z(x,y)) = 6$ implicitly, or use $z_x = -F_x/F_z$.*

$F = x^2+y^2+z^2-6$ gives $F_x = 2x$, $F_y = 2y$, $F_z = 2z$, so
$$z_x = -\frac{F_x}{F_z} = -\frac{x}{z}, \qquad z_y = -\frac{y}{z}.$$
At $P = (1,1,2)$: $z_x = -\frac12$ and $z_y = -\frac12$. The tangent plane is
$$z-2 = -\frac12(x-1) - \frac12(y-1),$$
which rearranges to $2z-4 = -x+1-y+1$, i.e. $x+y+2z = 6$. Its normal $(1,1,2)$ is parallel to
$\nabla F(P) = (2,2,4)$, as it should be. *Check:* $1+1+4 = 6$, so $P$ lies on the plane.

**18.** *Strategy: the gradient gives both the direction and the maximal rate.*

$\nabla f = (2xy,\,x^2+3y^2)$, so $\nabla f(1,1) = (2,4)$. The rate of steepest ascent is
$\lVert(2,4)\rVert = \sqrt{20} = 2\sqrt5$, in the direction
$\dfrac{(2,4)}{\sqrt{20}} = \dfrac{(1,2)}{\sqrt5}$. The steepest descent is in the opposite direction
$-\dfrac{(1,2)}{\sqrt5}$, with rate $-2\sqrt5$.

The unit vector in the direction $(1,-1)$ is $(1,-1)/\sqrt2$, so
$$D_{\mathbf{u}}f(1,1) = (2,4)\cdot\frac{(1,-1)}{\sqrt2} = \frac{2-4}{\sqrt2} = -\sqrt2 .$$
Since this is negative, $f$ decreases in the direction $(1,-1)$.

**19.** *Strategy: solve $\nabla f = \mathbf{0}$, then apply the second-derivative test.*

$f_x = 4y-4x^3$ and $f_y = 4x-4y^3$. Setting both to zero gives $y = x^3$ and $x = y^3$; substituting
gives $x = x^9$, i.e. $x(x^8-1) = 0$. The real solutions are $x = 0$, $x = 1$ and $x = -1$, giving the
critical points $(0,0)$, $(1,1)$ and $(-1,-1)$.

The second derivatives are $f_{xx} = -12x^2$, $f_{yy} = -12y^2$ and $f_{xy} = 4$, so
$$D = f_{xx}f_{yy} - f_{xy}^2 = 144x^2y^2 - 16 .$$
At $(0,0)$: $D = -16<0$, a saddle point. At $(1,1)$ and at $(-1,-1)$: $D = 144-16 = 128>0$ and
$f_{xx} = -12<0$, so both are strict local maxima, with value $f(\pm1,\pm1) = 4-1-1 = 2$.

These maxima are not global: along $y=0$, $f(x,0) = -x^4\to-\infty$, so $f$ is unbounded below. The
saddle at the origin is visible from $f(x,x) = 4x^2-2x^4>0$ for small $x\ne0$ and
$f(x,-x) = -4x^2-2x^4<0$.

**20.** *Strategy: the region is vertically simple; integrate in $y$ first, which produces a factor
$x$ and makes $e^{x^2}$ integrable.*

The triangle is $0\le x\le1$, $0\le y\le x$. Hence
$$\iint_T e^{x^2}\,dA = \int_0^1\!\!\int_0^{x} e^{x^2}\,dy\,dx
= \int_0^1 x\,e^{x^2}\,dx .$$
Substituting $u = x^2$, $du = 2x\,dx$:
$$\int_0^1 x e^{x^2}dx = \frac12\left[e^{u}\right]_0^1 = \frac{e-1}{2}.$$
The order matters: integrating in $x$ first would require $\int e^{x^2}dx$, which has no elementary
antiderivative. The numerical value is about $0.859$.

**21.** *Strategy: the solid is between two graphs over the disk of radius $2$; use polar coordinates.*

The intersection $x^2+y^2 = 4$ gives the disk $D$ of radius $2$, and the height at $(x,y)$ is
$4-(x^2+y^2) = 4-r^2$. Hence
$$V = \iint_D (4-x^2-y^2)\,dA = \int_0^{2\pi}\!\!\int_0^2 (4-r^2)\,r\,dr\,d\theta
= 2\pi\left[2r^2-\frac{r^4}{4}\right]_0^2 .$$
The bracket equals $8-4 = 4$, so $V = 8\pi$. *Check by a volume formula:* the solid is a paraboloid
of revolution of height $4$; the cylinder of the same base and height has volume $16\pi$, and the
paraboloid fills exactly half of it — a standard fact consistent with $8\pi$.

**22.** *Strategy: cylindrical coordinates with $z$ between the cone and the plane.*

The cone is $z = r$ and the top is $z = 1$; the shadow on the $xy$-plane is the disk $0\le r\le1$.
$$V = \int_0^{2\pi}\!\!\int_0^1\!\!\int_r^1 r\,dz\,dr\,d\theta
= 2\pi\int_0^1 r(1-r)\,dr = 2\pi\left(\frac12-\frac13\right) = \frac{\pi}{3}.$$
*Check:* the cone has base radius $1$ and height $1$, and $\frac13\pi r^2h = \frac{\pi}{3}$.

**23.** *Strategy: Lagrange multipliers, treating the case $x=0$ separately so as not to divide by
$x$.*

Let $g = x^2+y^2-3$. The equations are
$$2xy = 2\lambda x, \qquad x^2 = 2\lambda y, \qquad x^2+y^2 = 3 .$$
*Case $x = 0$:* then $y^2 = 3$, so $y = \pm\sqrt3$, and the second equation gives $0 = 2\lambda y$,
hence $\lambda = 0$; the first equation is then $0=0$. Candidates $(0,\pm\sqrt3)$, with $f = 0$.

*Case $x\ne0$:* the first equation gives $\lambda = y$. Substituting into the second gives
$x^2 = 2y^2$. Together with $x^2+y^2 = 3$ this gives $3y^2 = 3$, so $y = \pm1$ and $x^2 = 2$, i.e.
$x = \pm\sqrt2$. The candidates are $(\pm\sqrt2,1)$ with
$f = x^2y = 2$, and $(\pm\sqrt2,-1)$ with $f = -2$.

The circle is closed and bounded, so the maximum and minimum are among these values. Hence the maximum
is $2$, attained at $(\sqrt2,1)$ and $(-\sqrt2,1)$, and the minimum is $-2$, attained at
$(\pm\sqrt2,-1)$. *Check by parametrising:* with $x = \sqrt3\cos\theta$, $y = \sqrt3\sin\theta$,
$f = 3\sqrt3\cos^2\theta\sin\theta$, whose extreme values are indeed $\pm2$ (at
$\sin\theta = \pm1/\sqrt3$).

**24.** *Strategy: minimise the squared distance, a smooth function, subject to the plane constraint.*

Minimise $f = x^2+y^2+z^2$ subject to $x+2y+3z = 14$ (minimising the square is equivalent, since the
distance is non-negative). Lagrange:
$$2x = \lambda, \qquad 2y = 2\lambda, \qquad 2z = 3\lambda, \qquad x+2y+3z = 14 .$$
Hence $x = \lambda/2$, $y = \lambda$, $z = 3\lambda/2$, and the constraint gives
$\lambda\left(\frac12+2+\frac92\right) = 7\lambda = 14$, so $\lambda = 2$. The closest point is
$(1,2,3)$, and the distance is $\sqrt{1+4+9} = \sqrt{14}$.

*Check:* the distance from the origin to the plane $ax+by+cz = d$ is
$\lvert d\rvert/\sqrt{a^2+b^2+c^2} = 14/\sqrt{14} = \sqrt{14}$. Uniqueness of the stationary point,
together with the fact that the distance tends to infinity at infinity on the plane, shows that it is
the minimum.

## Advanced

**25.** *Strategy: the defining limit of differentiability gives an explicit bound on
$\lvert f(\mathbf{a}+\mathbf{h})-f(\mathbf{a})\rvert$.*

Since $f$ is differentiable at $\mathbf{a}$, there is a linear map $L:\mathbb{R}^n\to\mathbb{R}$ with
$$f(\mathbf{a}+\mathbf{h}) = f(\mathbf{a}) + L(\mathbf{h}) + \varepsilon(\mathbf{h})\lVert\mathbf{h}\rVert,
\qquad \varepsilon(\mathbf{h})\to0 \text{ as } \mathbf{h}\to\mathbf{0}.$$
Every linear map on $\mathbb{R}^n$ is bounded: writing $M = \left(\sum_i L(\mathbf{e}_i)^2\right)^{1/2}$,
Cauchy–Schwarz gives
$\lvert L(\mathbf{h})\rvert = \left\lvert\sum_i h_iL(\mathbf{e}_i)\right\rvert \le M\lVert\mathbf{h}\rVert$. Therefore
$$\lvert f(\mathbf{a}+\mathbf{h})-f(\mathbf{a})\rvert
\le M\lVert\mathbf{h}\rVert + \lvert\varepsilon(\mathbf{h})\rvert\lVert\mathbf{h}\rVert
= \big(M+\lvert\varepsilon(\mathbf{h})\rvert\big)\lVert\mathbf{h}\rVert \longrightarrow 0 .$$
Given $\eta>0$, choose $\delta>0$ so that $\lvert\varepsilon(\mathbf{h})\rvert<1$ and
$(M+1)\lVert\mathbf{h}\rVert<\eta$ whenever $\lVert\mathbf{h}\rVert<\delta$; then
$\lvert f(\mathbf{a}+\mathbf{h})-f(\mathbf{a})\rvert<\eta$, which is continuity at $\mathbf{a}$.

**26.** *Strategy: split the increment into a horizontal and a vertical step and apply the
one-variable mean value theorem to each.*

Let $h,k$ be small enough that the relevant segments stay in the neighbourhood where $f_x,f_y$ exist.
Define $\varphi(t) = f(a+th,\,b+k)$ for $t\in[0,1]$. By the chain rule (or directly, since the other
variable is fixed) $\varphi'(t) = f_x(a+th,b+k)\,h$, so the mean value theorem gives a
$\xi\in(a,a+h)$ with
$$f(a+h,b+k)-f(a,b+k) = f_x(\xi,b+k)\,h .$$
Similarly, $\psi(t) = f(a,b+tk)$ satisfies $\psi'(t) = f_y(a,b+tk)\,k$, so for some
$\eta\in(b,b+k)$,
$$f(a,b+k)-f(a,b) = f_y(a,\eta)\,k .$$
Adding,
$$f(a+h,b+k)-f(a,b) = f_x(a,b)\,h + f_y(a,b)\,k
+ \underbrace{\left[f_x(\xi,b+k)-f_x(a,b)\right]}_{\alpha(h,k)}h
+ \underbrace{\left[f_y(a,\eta)-f_y(a,b)\right]}_{\beta(h,k)}k .$$
As $(h,k)\to(0,0)$ we have $(\xi,b+k)\to(a,b)$ and $(a,\eta)\to(a,b)$, so continuity of the partials
at $(a,b)$ gives $\alpha,\beta\to0$. Since $\lvert h\rvert,\lvert k\rvert\le\lVert(h,k)\rVert$,
$$\lvert\alpha h+\beta k\rvert \le \big(\lvert\alpha\rvert+\lvert\beta\rvert\big)\lVert(h,k)\rVert
= o(\lVert(h,k)\rVert).$$
Hence $f$ is differentiable at $(a,b)$ with $\nabla f(a,b) = (f_x(a,b),f_y(a,b))$.

**27.** *Strategy: differentiate the constant identity $f(\gamma(t)) = c$.*

Since $\gamma$ lies in the level set, $f(\gamma(t)) = c$ for all $t$ near $0$. The composition is
differentiable (chain rule, Theorem 8.3) and constant, so
$$0 = \left.\frac{d}{dt}\right|_{t=0} f(\gamma(t)) = \nabla f(\gamma(0))\cdot\gamma'(0)
= \nabla f(\mathbf{a})\cdot\gamma'(0).$$
Thus $\nabla f(\mathbf{a})$ is orthogonal to the tangent vector $\gamma'(0)$ of every differentiable
curve through $\mathbf{a}$ lying in the level set. If $\nabla f(\mathbf{a})\ne\mathbf{0}$, the tangent
line to the level curve at $\mathbf{a}$ is the line through $\mathbf{a}$ perpendicular to
$\nabla f(\mathbf{a})$; equivalently, the gradient is a normal vector to the level set. This is the
statement used to write the tangent plane to a level surface as
$\nabla F(P)\cdot(\mathbf{x}-P)=0$ and to justify the tangency condition in Lagrange multipliers.

**28.** *Strategy: Taylor's theorem reduces the question to the sign of a quadratic form; complete the
square.*

Since $(a,b)$ is a critical point, $\nabla f(a,b) = \mathbf{0}$, and Taylor's theorem with Peano
remainder gives
$$f(a+h,b+k)-f(a,b) = \tfrac12\left(Ah^2+2Bhk+Ck^2\right) + o(h^2+k^2).$$
For $A\ne0$,
$$Ah^2+2Bhk+Ck^2 = \frac1A\left[(Ah+Bk)^2 + Dk^2\right],$$
as one checks by expanding the right-hand side:
$\frac1A\left(A^2h^2+2ABhk+B^2k^2+Dk^2\right) = Ah^2+2Bhk+\frac{B^2+D}{A}k^2$, and
$\frac{B^2+D}{A} = \frac{AC}{A} = C$.

(a) Let $D>0$ and $A>0$. The bracket is a sum of two squares, so the form $q(h,k)$ is non-negative,
and $q(h,k)=0$ forces $k=0$ (from $Dk^2=0$) and then $Ah=0$, so $h=0$. On the unit circle
$h^2+k^2=1$, the continuous function $q$ is positive everywhere and attains a minimum $\lambda>0$.
By homogeneity, $q(h,k)\ge\lambda(h^2+k^2)$ for all $(h,k)$. Therefore
$$f(a+h,b+k)-f(a,b) \ge \tfrac12\lambda(h^2+k^2) + o(h^2+k^2)
\ge \tfrac14\lambda(h^2+k^2) > 0$$
for all sufficiently small non-zero $(h,k)$, which is a strict local minimum.

(b) Let $D<0$ and $A>0$. Take $k=0$, $h\ne0$: $q = Ah^2>0$. Take $h = -Bk/A$ with $k\ne0$:
$q = \frac{D}{A}k^2<0$. Hence there are directions $\mathbf{v},\mathbf{w}$ with $q(\mathbf{v})>0$ and
$q(\mathbf{w})<0$. Along the line $t\mapsto(a,b)+t\mathbf{v}$,
$$f\big((a,b)+t\mathbf{v}\big) - f(a,b) = \tfrac12t^2q(\mathbf{v}) + o(t^2) > 0$$
for all small $t\ne0$, while along $t\mathbf{w}$ the same expression is negative. A neighbourhood of
$(a,b)$ therefore contains points where $f>f(a,b)$ and points where $f<f(a,b)$: the point is not a
local extremum. (If $A<0$, the same argument with the signs reversed, or applied to $-f$, gives the
same conclusion; if $A=0$ then $D = -B^2\le0$, and when $D<0$ one has $B\ne0$ and the form
$k(2Bh+Ck)$ plainly takes both signs.)

**29.** *Strategy: compute the partial derivatives along the axes from the definition, then
differentiate in the other variable.*

For $y\ne0$, $f(0,y) = 0$ (the numerator contains the factor $x = 0$), so
$$f_x(0,y) = \lim_{h\to0}\frac{f(h,y)-f(0,y)}{h}
= \lim_{h\to0}\frac{hy(h^2-y^2)}{h(h^2+y^2)}
= \lim_{h\to0}\frac{y(h^2-y^2)}{h^2+y^2} = \frac{y(0-y^2)}{y^2} = -y .$$
Hence
$$f_{xy}(0,0) = \left.\frac{d}{dy}\big(-y\big)\right|_{y=0} = -1 .$$
Similarly, for $x\ne0$, $f(x,0) = 0$ and
$$f_y(x,0) = \lim_{k\to0}\frac{f(x,k)-f(x,0)}{k}
= \lim_{k\to0}\frac{xk(x^2-k^2)}{k(x^2+k^2)} = x,$$
so
$$f_{yx}(0,0) = \left.\frac{d}{dx}\big(x\big)\right|_{x=0} = 1 .$$
Thus $f_{xy}(0,0) = -1\ne1 = f_{yx}(0,0)$.

Clairaut's theorem requires $f_{xy}$ and $f_{yx}$ to be continuous at $(0,0)$. They are not: for
$x\ne0$, differentiating $f_x$ in $y$ at $y=0$ gives $f_{xy}(x,0) = 1$, while
$f_{xy}(0,0) = -1$, so $f_{xy}$ has no limit at the origin (and $f_{xy}(0,y) = -1$ along the
$y$-axis). The hypothesis fails, so the theorem says nothing — and indeed the conclusion is false here.
This is the standard example showing that continuity of the mixed partials cannot be dropped.

**30.** *Strategy: recognise each inner integrand as an exact derivative in the integration variable.*

Let $f(x,y) = \dfrac{x^2-y^2}{(x^2+y^2)^2}$. Observe that
$$\frac{\partial}{\partial x}\left(\frac{x}{x^2+y^2}\right)
= \frac{(x^2+y^2)-x(2x)}{(x^2+y^2)^2} = \frac{y^2-x^2}{(x^2+y^2)^2} = -f(x,y).$$
Therefore, for $y\ne0$,
$$\int_0^1 f(x,y)\,dx = \left[-\frac{x}{x^2+y^2}\right]_{x=0}^{x=1}
= -\frac{1}{1+y^2},$$
and
$$\int_0^1\!\!\int_0^1 f(x,y)\,dx\,dy = \int_0^1\left(-\frac{1}{1+y^2}\right)dy
= \left[-\arctan y\right]_0^1 = -\frac{\pi}{4}.$$
In the other order, use
$$\frac{\partial}{\partial y}\left(\frac{y}{x^2+y^2}\right)
= \frac{(x^2+y^2)-y(2y)}{(x^2+y^2)^2} = \frac{x^2-y^2}{(x^2+y^2)^2} = f(x,y),$$
so for $x\ne0$
$$\int_0^1 f(x,y)\,dy = \left[\frac{y}{x^2+y^2}\right]_{y=0}^{y=1} = \frac{1}{x^2+1},$$
and
$$\int_0^1\!\!\int_0^1 f(x,y)\,dy\,dx = \int_0^1\frac{dx}{1+x^2} = \frac{\pi}{4}.$$
The two iterated integrals differ, so the double integral does not exist as an absolutely convergent
integral.

Fubini's theorem is not contradicted: its hypothesis fails. In polar coordinates
$f = \cos 2\theta/r^2$, so $\lvert f\rvert = \lvert\cos2\theta\rvert/r^2$. On the sector
$0\le\theta\le\pi/6$ (which lies inside the unit square for $0\le r\le1$) we have
$\cos2\theta\ge\frac12$, hence $\lvert f\rvert\ge 1/(2r^2)$ and
$$\iint_{[0,1]^2}\lvert f\rvert\,dA \ge \int_0^{\pi/6}\!\!\int_0^1
\frac{1}{2r^2}\,r\,dr\,d\theta = \frac{\pi}{12}\int_0^1\frac{dr}{r} = \infty .$$
The function is unbounded and not integrable over the square; the Fubini hypothesis that
$\iint\lvert f\rvert<\infty$ is exactly what rules out this phenomenon.

**31.** *Strategy: expand $\Delta z$ using differentiability of $f$ and divide by $\Delta t$.*

**Statement.** Let $x,y$ be differentiable at $t_0$ and let $f$ be differentiable at
$(x(t_0),y(t_0))$. Then $t\mapsto z(t) = f(x(t),y(t))$ is differentiable at $t_0$, and
$$\frac{dz}{dt}(t_0) = f_x(x(t_0),y(t_0))\,x'(t_0) + f_y(x(t_0),y(t_0))\,y'(t_0).$$

**Derivation.** Write $\Delta x = x(t_0+\Delta t)-x(t_0)$, $\Delta y = y(t_0+\Delta t)-y(t_0)$ and
$\Delta z = f(x(t_0)+\Delta x, y(t_0)+\Delta y)-f(x(t_0),y(t_0))$. Differentiability of $f$ at
$(x(t_0),y(t_0))$ means precisely that
$$\Delta z = f_x\,\Delta x + f_y\,\Delta y + \varepsilon_1\Delta x + \varepsilon_2\Delta y,$$
where $f_x,f_y$ are evaluated at $(x(t_0),y(t_0))$ and $\varepsilon_1,\varepsilon_2\to0$ as
$(\Delta x,\Delta y)\to(0,0)$. Dividing by $\Delta t\ne0$,
$$\frac{\Delta z}{\Delta t}
= f_x\frac{\Delta x}{\Delta t} + f_y\frac{\Delta y}{\Delta t}
+ \varepsilon_1\frac{\Delta x}{\Delta t} + \varepsilon_2\frac{\Delta y}{\Delta t}.$$
Because $x,y$ are differentiable at $t_0$, they are continuous there, so $\Delta x,\Delta y\to0$ and hence
$\varepsilon_1,\varepsilon_2\to0$ as $\Delta t\to0$. Also $\Delta x/\Delta t\to x'(t_0)$ and
$\Delta y/\Delta t\to y'(t_0)$, both finite. Therefore the last two terms tend to $0\cdot x'(t_0) = 0$
and $0\cdot y'(t_0) = 0$, and the formula follows.

**Where differentiability of $f$ is used.** The decomposition of $\Delta z$ into a linear part plus a
remainder that is $o(\lVert(\Delta x,\Delta y)\rVert)$ is exactly the differentiability hypothesis.
Mere existence of $f_x,f_y$ gives no such decomposition: for $f = x^2y/(x^2+y^2)$ at the origin the
partials exist but the remainder along the diagonal is of the order of the displacement, not smaller,
and the chain rule can fail. Differentiability of $x$ and $y$ is used to convert
$\Delta x,\Delta y\to0$ and to make the difference quotients converge.

**32.** *Strategy: spherical coordinates; the denominator is the volume of the hemisphere, the
numerator is $\iiint z\,dV$.*

The upper unit hemisphere is $0\le\rho\le1$, $0\le\varphi\le\pi/2$, $0\le\theta<2\pi$. Its volume is
$$V = \int_0^{2\pi}\!\!\int_0^{\pi/2}\!\!\int_0^1 \rho^2\sin\varphi\,d\rho\,d\varphi\,d\theta
= 2\pi\cdot\frac13\cdot\left[-\cos\varphi\right]_0^{\pi/2} = 2\pi\cdot\frac13 = \frac{2\pi}{3}.$$
The first moment is
$$\iiint_E z\,dV = \int_0^{2\pi}\!\!\int_0^{\pi/2}\!\!\int_0^1
(\rho\cos\varphi)\,\rho^2\sin\varphi\,d\rho\,d\varphi\,d\theta
= 2\pi\cdot\frac14\int_0^{\pi/2}\sin\varphi\cos\varphi\,d\varphi .$$
Since $\int_0^{\pi/2}\sin\varphi\cos\varphi\,d\varphi = \frac12$,
$$\iiint_E z\,dV = 2\pi\cdot\frac14\cdot\frac12 = \frac{\pi}{4}.$$
Therefore
$$\bar z = \frac{\pi/4}{2\pi/3} = \frac{3}{8}.$$
*Check:* the centroid of a solid hemisphere lies on the axis of symmetry at height $\frac38R$ above
the base; for $R=1$ this is $\frac38$, as computed. The value is less than $\frac12$ because most of
the volume is near the base.

**33.** *Strategy: two constraints, hence two multipliers; then verify on the whole constraint set.*

Write $g = x^2+y^2-1$ and $h = y+z-1$. The equations $\nabla f = \lambda\nabla g + \mu\nabla h$ are
$$1 = 2\lambda x, \qquad 1 = 2\lambda y + \mu, \qquad 1 = \mu, \qquad x^2+y^2 = 1, \qquad y+z = 1 .$$
From $\mu = 1$, the second equation gives $2\lambda y = 0$. If $\lambda = 0$ the first equation would
give $1 = 0$, so $\lambda\ne0$ and therefore $y = 0$. Then $x^2 = 1$, so $x = \pm1$, and
$z = 1-y = 1$. The candidates are $(1,0,1)$ and $(-1,0,1)$.

The constraint set is the intersection of the cylinder $x^2+y^2=1$ with the plane $y+z=1$, an ellipse,
which is closed and bounded; the extrema exist and are among the candidates. Evaluating,
$f(1,0,1) = 2$ and $f(-1,0,1) = 0$, so the maximum is $2$ and the minimum is $0$.

*Direct check:* on the constraint set $z = 1-y$, so $f = x+y+1-y = x+1$ with $x\in[-1,1]$; its maximum
is $2$ at $x=1$ and its minimum $0$ at $x=-1$, in agreement. The two constraint gradients
$(2x,2y,0)$ and $(0,1,1)$ are linearly independent at both candidates, so the constraint qualification
holds.

**34.** *Strategy: the substitution straightens the region into a rectangle; compute the Jacobian
determinant.*

Let $u = xy$ and $v = y/x$. The four bounding curves become $u = 1$, $u = 4$, $v = 1$, $v = 4$, so the
region in the $(u,v)$-plane is the square $[1,4]\times[1,4]$. Solving for $x,y$: from $y = vx$ and
$u = xy = vx^2$ we get
$$x = \sqrt{\frac uv}, \qquad y = \sqrt{uv}.$$
The Jacobian determinant is
$$\frac{\partial(x,y)}{\partial(u,v)}
= \begin{vmatrix}
\dfrac{1}{2\sqrt{uv}} & -\dfrac{\sqrt{u}}{2v^{3/2}}\\[6pt]
\dfrac{\sqrt{v}}{2\sqrt{u}} & \dfrac{\sqrt{u}}{2\sqrt{v}}
\end{vmatrix}
= \frac{1}{4v}+\frac{1}{4v} = \frac{1}{2v} .$$
Hence
$$\text{area} = \int_1^4\!\!\int_1^4 \frac{1}{2v}\,du\,dv
= \left(\int_1^4 du\right)\left(\int_1^4\frac{dv}{2v}\right)
= 3\cdot\frac12\ln 4 = 3\ln 2 .$$
*Check:* $3\ln2\approx2.08$. The region lies inside the sector between the rays $y=x$ and $y=4x$
(whose angle is $\arctan4-\arctan1\approx0.540$ rad) and between the hyperbolas $xy=1$ and $xy=4$; a
rough estimate of its area from these dimensions is consistent.

## Challenge

**35.** *(a) Strategy: bound $\lvert f(\mathbf{h})\rvert$ by $\lVert\mathbf{h}\rVert^2$.*

For $(x,y)\ne(0,0)$, $\lvert f(x,y)\rvert\le x^2+y^2$ because $\lvert\sin t\rvert\le1$. Therefore
$$\frac{\lvert f(h,k)-f(0,0)-0\rvert}{\sqrt{h^2+k^2}}
\le \frac{h^2+k^2}{\sqrt{h^2+k^2}} = \sqrt{h^2+k^2}\longrightarrow 0 ,$$
so $f$ is differentiable at the origin with derivative the zero map, $\nabla f(0,0) = (0,0)$.

*(b) Strategy: differentiate for $(x,y)\ne(0,0)$ and evaluate along a sequence where the oscillating
term is favourable.*

Let $r^2 = x^2+y^2$. For $(x,y)\ne(0,0)$,
$$f_x = 2x\sin\frac{1}{r^2} + r^2\cos\frac{1}{r^2}\cdot\left(-\frac{2x}{r^4}\right)
= 2x\sin\frac{1}{r^2} - \frac{2x}{r^2}\cos\frac{1}{r^2}.$$
On the $x$-axis ($y=0$, $x\ne0$) this is
$$f_x(x,0) = 2x\sin\frac{1}{x^2} - \frac{2}{x}\cos\frac{1}{x^2}.$$
Choose $x_n = 1/\sqrt{2\pi n}$, so that $1/x_n^2 = 2\pi n$; then $\sin(2\pi n) = 0$ and
$\cos(2\pi n) = 1$, and
$$f_x(x_n,0) = -\frac{2}{x_n} = -2\sqrt{2\pi n}\longrightarrow-\infty .$$
Since $x_n\to0$, every neighbourhood of the origin contains points where $f_x$ is arbitrarily negative:
$f_x$ is unbounded (and in particular not continuous) at the origin.

*(c)* This shows that the converse of "$C^1$ implies differentiable" is false. Continuous partials are
a *sufficient* condition for differentiability, not a necessary one: here $f$ is differentiable at the
origin — indeed with derivative zero — while its partial derivatives do not even stay bounded near the
origin. Continuity of the partials is a convenient practical test, but differentiability is the
stronger and more fundamental notion.

**36.** *Strategy: the solid is described in spherical coordinates by $\rho\le2$ and
$\varphi\le\pi/4$.*

The cone $z = \sqrt{x^2+y^2}$ is $\varphi = \pi/4$, and "above the cone" means $0\le\varphi\le\pi/4$.
The sphere of radius $2$ is $\rho = 2$. Hence
$$V = \int_0^{2\pi}\!\!\int_0^{\pi/4}\!\!\int_0^{2}
\rho^2\sin\varphi\,d\rho\,d\varphi\,d\theta
= 2\pi\cdot\frac{8}{3}\cdot\left[-\cos\varphi\right]_0^{\pi/4} .$$
Since $\cos(\pi/4) = \sqrt2/2$,
$$V = \frac{16\pi}{3}\left(1-\frac{\sqrt2}{2}\right) = \frac{8\pi}{3}\left(2-\sqrt2\right).$$
*Check:* the value is $\approx 4.91$. The ball of radius $2$ has volume $32\pi/3\approx33.5$, and the
spherical cone with half-angle $45^\circ$ occupies the fraction
$\frac{1}{2}(1-\cos 45^\circ)\approx0.146$ of the ball; $0.146\times33.5\approx4.9$, consistent.

**37.** *Strategy: maximise $F = x^ay^bz^c$ on the simplex $x+y+z=S$; the maximum gives the
inequality after a change of variables.*

Fix $S>0$ and let $T = a+b+c$. Consider $F = x^ay^bz^c$ on the closed simplex
$\{x,y,z\ge0,\ x+y+z=S\}$. This set is compact and $F$ is continuous; on the boundary $F = 0$ (since
$a,b,c>0$), while $F>0$ in the interior, so the maximum is attained at an interior critical point.

By Lagrange multipliers with constraint $g = x+y+z-S = 0$,
$$\frac{\partial F}{\partial x} = \frac{aF}{x} = \lambda, \qquad
\frac{\partial F}{\partial y} = \frac{bF}{y} = \lambda, \qquad
\frac{\partial F}{\partial z} = \frac{cF}{z} = \lambda .$$
(Here $F_x = a x^{a-1}y^bz^c = aF/x$, and similarly.) Hence
$$x = \frac{aF}{\lambda}, \qquad y = \frac{bF}{\lambda}, \qquad z = \frac{cF}{\lambda},$$
and summing, $S = \frac{TF}{\lambda}$, so $\lambda = TF/S$ and
$$x = \frac{aS}{T}, \qquad y = \frac{bS}{T}, \qquad z = \frac{cS}{T}.$$
The maximum value is therefore
$$F_{\max} = \left(\frac{aS}{T}\right)^a\left(\frac{bS}{T}\right)^b\left(\frac{cS}{T}\right)^c
= S^{T}\left(\frac aT\right)^a\left(\frac bT\right)^b\left(\frac cT\right)^c .$$
Consequently, for all $x,y,z\ge0$ with $x+y+z = S$,
$$x^ay^bz^c \le S^T\left(\frac aT\right)^a\left(\frac bT\right)^b\left(\frac cT\right)^c .$$

Now let $X,Y,Z>0$ be arbitrary and put $x = aX$, $y = bY$, $z = cZ$, so that
$x+y+z = aX+bY+cZ =: S$. Substituting,
$$a^ab^bc^c\,X^aY^bZ^c \le (aX+bY+cZ)^T\left(\frac aT\right)^a\left(\frac bT\right)^b\left(\frac cT\right)^c .$$
Dividing by $a^ab^bc^c = T^T\left(\frac aT\right)^a\left(\frac bT\right)^b\left(\frac cT\right)^c$ gives
$$X^aY^bZ^c \le \left(\frac{aX+bY+cZ}{T}\right)^T .$$
Taking the $T$-th root (all quantities are positive) yields
$$X^{a/T}Y^{b/T}Z^{c/T} \le \frac{aX+bY+cZ}{T},$$
which is the weighted AM–GM inequality. Equality holds exactly when $x = aX$, $y = bY$, $z = cZ$ are
the optimal point, i.e. when $aX : bY : cZ = a:b:c$, or $X = Y = Z$; for the unweighted case
$a=b=c=1$ this reduces to the usual AM–GM inequality for three numbers.

**38.** *Strategy: three functions with vanishing Hessian determinant at the origin but different local
behaviour.*

1. $f_1(x,y) = x^4+y^4$. Here $f_{xx} = 12x^2$, $f_{yy} = 12y^2$, $f_{xy} = 0$, so
   $D = 144x^2y^2$ and $D(0,0) = 0$. Since $f_1\ge0 = f_1(0,0)$, the origin is a strict local
   (indeed global) minimum.
2. $f_2(x,y) = -x^4-y^4$. The second derivatives are the negatives of those of $f_1$, so again
   $D(0,0) = 0$. Since $f_2\le0 = f_2(0,0)$, the origin is a strict local maximum.
3. $f_3(x,y) = x^3+y^3$. Here $f_{xx} = 6x$, $f_{yy} = 6y$, $f_{xy} = 0$, so $D = 36xy$ and
   $D(0,0) = 0$. On the $x$-axis, $f_3(x,0) = x^3$ is positive for $x>0$ and negative for $x<0$, and
   the same is true on the $y$-axis. Hence every neighbourhood of the origin contains points with
   $f_3>0$ and points with $f_3<0$: the origin is neither a maximum nor a minimum.

Since all three functions satisfy $D = 0$ at the origin but have different behaviour there, the value
$D=0$ carries no information: the second-derivative test is inconclusive and a separate argument is
needed. (In each case the failure is that the quadratic term of the Taylor expansion vanishes
identically, so the higher-order terms decide.)

**39.** *Strategy: square the integral, interpret the square as a double integral over a square, and
trap the square between two disks.*

Let $I_R = \int_{-R}^{R}e^{-x^2}dx$ for $R>0$, and $I = \lim_{R\to\infty}I_R$, which exists in
$[0,\infty]$ because the integrand is positive and $I_R$ increases with $R$. By Fubini's theorem
applied to the continuous integrand $e^{-(x^2+y^2)}$ on the square,
$$I_R^2 = \left(\int_{-R}^{R}e^{-x^2}dx\right)\left(\int_{-R}^{R}e^{-y^2}dy\right)
= \iint_{[-R,R]^2} e^{-(x^2+y^2)}\,dA .$$
The disk $D_R$ of radius $R$ is contained in the square $[-R,R]^2$, which is contained in the disk
$D_{R\sqrt2}$ of radius $R\sqrt2$. Since the integrand is positive,
$$\iint_{D_R} e^{-(x^2+y^2)}dA \le I_R^2 \le \iint_{D_{R\sqrt2}} e^{-(x^2+y^2)}dA .$$
In polar coordinates, with $dA = r\,dr\,d\theta$,
$$\iint_{D_s} e^{-(x^2+y^2)}dA = \int_0^{2\pi}\!\!\int_0^{s} e^{-r^2}r\,dr\,d\theta
= 2\pi\left[-\frac12e^{-r^2}\right]_0^{s} = \pi\left(1-e^{-s^2}\right).$$
Hence
$$\pi\left(1-e^{-R^2}\right) \le I_R^2 \le \pi\left(1-e^{-2R^2}\right).$$
As $R\to\infty$ both bounds tend to $\pi$, so by the squeeze theorem $I_R^2\to\pi$, and therefore
$I = \sqrt\pi$ (the positive square root, since $I>0$).

Every step is justified: Fubini applies to a continuous function on a rectangle; the comparison of the
disk, square and larger disk uses positivity of the integrand; the polar computation uses the
change-of-variables formula with the Jacobian $r$; and the limits are ordinary limits of convergent
bounded quantities.

**40.** *Strategy: the inner integral $\int\sin(x^2)dx$ is not elementary; reverse the order.*

The region of integration is
$$R = \{(x,y) : 0\le y\le\sqrt\pi,\ y\le x\le\sqrt\pi\},$$
a triangle with vertices $(0,0)$, $(\sqrt\pi,0)$ and $(\sqrt\pi,\sqrt\pi)$. Describing it with $x$ as
the outer variable: $0\le x\le\sqrt\pi$ and, for fixed $x$, $0\le y\le x$. Hence
$$\int_0^{\sqrt\pi}\!\!\int_y^{\sqrt\pi}\sin(x^2)\,dx\,dy
= \int_0^{\sqrt\pi}\!\!\int_0^{x}\sin(x^2)\,dy\,dx
= \int_0^{\sqrt\pi} x\sin(x^2)\,dx .$$
Substituting $u = x^2$, $du = 2x\,dx$,
$$\int_0^{\sqrt\pi}x\sin(x^2)\,dx = \frac12\int_0^{\pi}\sin u\,du
= \frac12\left[-\cos u\right]_0^{\pi} = \frac12(1+1) = 1 .$$
The reversed order is essential: $\int\sin(x^2)\,dx$ has no elementary antiderivative (it is a
Fresnel-type integral), so the original order cannot be computed directly.
