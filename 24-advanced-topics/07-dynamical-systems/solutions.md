# Dynamical Systems and Chaos — Solutions

> [Dynamical Systems and Chaos](README.md) · Solutions to the 36 problems in [exercises.md](exercises.md)

Each solution gives the strategy, every significant step, and a check where one is available.

## Beginner

**1.** *(Strategy: solve $f(x)=0$, then read the sign of $f'$ at each root.)*

(a) $x^2-4=0$ gives $x=\pm2$; $f'(x)=2x$, so $f'(-2)=-4<0$ (stable) and $f'(2)=4>0$ (unstable).
Between $-2$ and $2$ we have $\dot x<0$, so orbits move left; outside they move right: arrows point into
$-2$ from both sides and away from $2$.

(b) $\sin x = 0$ gives $x = n\pi$; $f'(n\pi) = \cos n\pi = (-1)^n$. Even multiples of $\pi$ are stable,
odd multiples unstable. The basin of $2k\pi$ is $\bigl((2k-1)\pi,(2k+1)\pi\bigr)$.

(c) $x^3-x = x(x-1)(x+1)=0$ gives $x=0,\pm1$; $f'(x) = 3x^2-1$, so $f'(0) = -1$ (stable) and
$f'(\pm1) = 2>0$ (unstable). All three are hyperbolic.

**2.** *(Strategy: separate variables; the partial-fraction identity is
$\frac{1}{x(1-x)} = \frac1x + \frac{1}{1-x}$.)*

Integrating $\frac{dx}{x(1-x)} = dt$ gives $\ln\lvert x\rvert - \ln\lvert 1-x\rvert = t + C$, i.e.
$\frac{x}{1-x} = Ae^t$, and imposing $x(0)=x_0$ gives

$$x(t) = \frac{x_0e^{t}}{1-x_0+x_0e^{t}}.$$

For $0<x_0<1$ the solution increases to $1$; for $x_0=0$ it is identically $0$; for $x_0>1$ or $x_0<0$
the denominator vanishes at $t = \ln\frac{x_0}{x_0-1} > 0$, so the solution blows up in finite time. The
linearisation agrees: $f'(0) = 1>0$ (unstable) and $f'(1) = -1<0$ (stable), and the exponential rate near
$1$ is $e^{-t}$, visible in the formula after writing $x - 1 \propto e^{-t}$.

**3.** *(Strategy: compute $\tau$ and $\Delta$; the discriminant $\tau^2-4\Delta$ separates node and
focus.)*

(a) $\tau=-4$, $\Delta=3$, eigenvalues $-1,-3$: stable node.
(b) $\tau=0$, $\Delta=-1<0$: saddle, eigenvalues $\pm1$.
(c) $\tau=0$, $\Delta=1$, eigenvalues $\pm i$: centre — stable but not asymptotically stable.
(d) $\tau=-2$, $\Delta=1$, $\tau^2-4\Delta=0$: a repeated eigenvalue $-1$ with a single eigenvector (the
matrix is a Jordan block), an *improper* stable node: orbits approach the origin tangentially to the
eigendirection $(1,0)$.

**4.** *(Strategy: the product structure makes the Jacobian diagonal.)*

Fixed points: $x-x^3 = 0$ gives $x = 0, \pm1$, and $y=0$, so $(0,0),(\pm1,0)$. The Jacobian is
$\begin{pmatrix}1-3x^2&0\\0&-1\end{pmatrix}$. At $(0,0)$ the eigenvalues are $1$ and $-1$: a saddle. At
$(\pm1,0)$ they are $-2$ and $-1$: stable nodes. All three are hyperbolic, so by Theorem 7.1 and
Hartman–Grobman these conclusions are reliable and complete: the phase portrait is a saddle at the origin
with separatrices along both axes, and two attracting nodes at $(\pm1,0)$.

**5.** *(Strategy: find the two equilibria, then look for a conserved quantity because the linearisation
degenerates at the interesting one.)*

Fixed points: $x(2-y)=0$ and $y(x-1)=0$ give $(0,0)$ and $(1,2)$. The Jacobian is
$\begin{pmatrix}2-y&-x\\ y&x-1\end{pmatrix}$, so at $(0,0)$ it is $\begin{pmatrix}2&0\\0&-1\end{pmatrix}$:
a saddle (eigenvalues $2,-1$). At $(1,2)$ it is $\begin{pmatrix}0&-1\\2&0\end{pmatrix}$, with eigenvalues
$\pm i\sqrt2$: a centre, hence *not* hyperbolic, and the linearisation decides nothing.

The actual behaviour is found from $H(x,y) = x - \ln x + y - 2\ln y$, for which

$$\dot H = (1-\tfrac1x)\,x(2-y) + (1-\tfrac2y)\,y(x-1) = (x-1)(2-y) + (y-2)(x-1) = 0 .$$

So $H$ is conserved: every orbit is a level curve of $H$, closed around $(1,2)$ because $H$ has a strict
minimum there. The equilibrium is a nonlinear centre with a one-parameter family of periodic orbits — the
predator–prey cycle.

**6.** *(Strategy: multipliers decide; then iterate to confirm.)*

For $\mu=2$: fixed points $0$ and $1-1/2 = 0.5$; multipliers $f'(0)=\mu = 2$ (unstable) and
$f'(0.5) = 2-\mu = 0$ (superstable — the fixed point coincides with the critical point of the parabola).
Iterating from $0.1$: $0.18$, $0.2952$, $0.41611$, $0.48593$, and thereafter $0.4996$, $0.49999$, so the
orbit converges to $0.5$. Superstable convergence is quadratic, which is why four steps already give two
correct digits.

**7.** *(Strategy: compose the two linear pieces; the breakpoints are $1/4, 1/2, 3/4$.)*

$$T^2(x) = \begin{cases}4x, & 0\le x\le\tfrac14,\\ 2-4x, & \tfrac14<x\le\tfrac12,\\ 4x-2, & \tfrac12<x\le\tfrac34,\\ 4-4x, & \tfrac34<x\le1.\end{cases}$$

Solving $T^2(x)=x$ on each piece: $4x=x$ gives $x=0$; $2-4x=x$ gives $x=2/5$; $4x-2=x$ gives $x=2/3$;
$4-4x=x$ gives $x=4/5$. The fixed points of $T$ are $0$ and $2/3$, so the 2-cycle is $\{2/5,\,4/5\}$.
Check: $T(2/5)=4/5$ and $T(4/5)=2-8/5=2/5$. ✓

**8.** *(Strategy: compute $\dot V$ and compare the decay with an exponential.)*

With $V=x^2$: $\dot V = 2x(-x^3) = -2x^4 = -2V^2\le0$, strictly negative off $x=0$, so the origin is
asymptotically stable. Solving, $x^{-2} = x_0^{-2}+2t$, hence $x(t) = x_0/\sqrt{1+2x_0^2t}$, which decays
like $t^{-1/2}$. Exponential stability would require $x(t)\le Cx_0e^{-\lambda t}$ with $\lambda>0$ fixed;
taking $t = 1/x_0^2$ gives $x(t)/x_0 = 1/\sqrt3$ while $Ce^{-\lambda/x_0^2}\to0$ as $x_0\to0$, a
contradiction. Equivalently, $\dot V = -2V^2$ is not $\le -cV$ for any $c>0$ near $0$.

**9.** *(Strategy: linearise first, then bound the nonlinear terms.)*

The Jacobian is $\begin{pmatrix}-1&2y\\2x&-1\end{pmatrix}$, which at the origin is $-I$: eigenvalues
$-1,-1$, so the origin is asymptotically stable for the linearisation. With $V = x^2+y^2 = r^2$,

$$\dot V = 2x(-x+y^2) + 2y(-y+x^2) = -2r^2 + 2xy(x+y).$$

Since $\lvert xy\rvert\le r^2/2$ and $\lvert x+y\rvert\le\sqrt2\,r$, we get $\lvert2xy(x+y)\rvert\le\sqrt2\,r^3$,
so $\dot V \le -2r^2+\sqrt2r^3 = -r^2(2-\sqrt2 r)<0$ for $0<r<\sqrt2$. Hence the origin is asymptotically
stable, with basin containing the disc of radius $\sqrt2$ *at least*. The result is local because the
estimate on the cubic term is only useful while $r$ is small; nothing prevents orbits outside that disc
from escaping.

**10.** *(Strategy: complete the square in $x$.)*

$x^2-2x+\mu = (x-1)^2 + (\mu-1)$, so fixed points are $x = 1\pm\sqrt{1-\mu}$, real for $\mu\le1$. Since
$f'(x) = 2x-2$, at $x = 1+\sqrt{1-\mu}$ we get $+2\sqrt{1-\mu}>0$ (unstable) and at $x=1-\sqrt{1-\mu}$ we
get $-2\sqrt{1-\mu}<0$ (stable), for $\mu<1$. At $\mu=1$ the two collide at $x=1$ with $f'=0$: a
saddle-node. The bifurcation diagram is a parabola opening to the left: two branches, stable below and
unstable above, meeting at $(\mu,x) = (1,1)$.

**11.** *(Strategy: $D^n$ multiplies by $2^n$; count fixed points by solving a congruence.)*

$D^n(x) = 2^nx \bmod 1$, so $D^n(x)=x$ iff $(2^n-1)x\in\mathbb{Z}$, giving $x = k/(2^n-1)$ for
$k = 0,\dots,2^n-2$: exactly $2^n-1$ fixed points of $D^n$. Since $D'(x) = 2$ for every $x$,
$\lambda = \lim\frac1n\sum\ln2 = \ln2$ at every point.

**12.** *(Strategy: iterate explicitly and average $\ln\lvert f'\rvert$.)*

(a) $x_k = r^kx_0$, $f'(x_k) = r$, so $\lambda = \frac1n\sum_{k<n}\ln r = \ln r$.

(b) $x_k = x_0^{2^k}$, and $f'(x_k) = 2x_k$, so $\frac1n\sum_{k<n}\ln(2x_k)$. The terms grow doubly
exponentially, so the average diverges: $\lambda = +\infty$. The orbit reaches infinity in finite time
(the solution of $\dot x = x^2$ in discrete form), which is why the finite average never settles. Both
examples show that a positive exponent measures separation of nearby orbits per step, not the size of the
domain.

## Intermediate

**13.** *(Strategy: linearise, then solve the invariance equation for a graph.)*

The Jacobian at the origin is diagonal with entries $-2$ and $3$: hyperbolic, with $E^s = \{y=0\}$ and
$E^u = \{x=0\}$, so the origin is a saddle. For the stable manifold write $y = h(x) = ax^2+bx^3+\cdots$;
invariance requires $h'(x)(-2x) = 3h(x)+x^2$, i.e.

$$-2ax^2 - 3bx^3 = 3ax^2 + 3bx^3 + x^2 + \cdots,$$

so $-2a = 3a+1$ gives $a = -1/7$ and $-3b = 3b$ gives $b=0$. Indeed $h(x) = -x^2/7$ solves the equation
exactly: $-2x\cdot(-2x/7) = 4x^2/7$ and $3(-x^2/7)+x^2 = 4x^2/7$. ✓

Hartman–Grobman gives a homeomorphism carrying the flow to that of the linear saddle, hence it guarantees
the correct *topology*: one stable and one unstable direction, orbits hyperbolic in shape. It does not
give a smooth change of coordinates, and it does not say that the stable manifold is the $x$-axis: here it
is a parabola, tangent to it at the origin.

**14.** *(Strategy: (a) compute $\dot V$ and note it is strictly negative off the origin; (b) examine what
the proof of Theorem 7.5(3) uses.)*

(a) $\dot V = x(y-x^3) + y(-x-y^3) = -(x^4+y^4)\le0$, with equality only at the origin. $V$ is positive
definite and radially unbounded, so Theorem 7.5(3) gives global asymptotic stability.

(b) $V(x) = x^2/(1+x^2)$ is positive definite but $V\to1$ as $\lvert x\rvert\to\infty$, so its sublevel
sets are unbounded and the argument that makes orbits bounded fails. Concretely, a flow such as
$\dot x = x(1+x^2)$ has $V$ decreasing near the origin yet orbits escape to infinity: boundedness of $V$
does not bound $x$.

**15.** *(Strategy: implicit function theorem for the curve, continuity of eigenvalues for
hyperbolicity.)*

Define $F(x,\mu) = f(x,\mu)$. Then $F(p_0,\mu_0)=0$ and $D_xF(p_0,\mu_0)$ is invertible (its eigenvalues
are nonzero), so the implicit function theorem gives neighbourhoods and a unique $C^1$ map $p$ with
$f(p(\mu),\mu)=0$ and $p(\mu_0)=p_0$. The eigenvalues of $D_xf(p(\mu),\mu)$ are the roots of the
characteristic polynomial, whose coefficients depend continuously on the entries of the matrix; roots of
polynomials depend continuously on coefficients (Hurwitz's theorem), so each eigenvalue is a continuous
function of $\mu$. Since none is purely imaginary at $\mu_0$, a neighbourhood of $\mu_0$ keeps them away
from the imaginary axis.

**16.** *(Strategy: factor $f_c^2(x)-x$ by the fixed-point polynomial, then use the product of the roots
for the multiplier.)*

$f_c(x) = x^2+c$ has fixed points solving $x^2-x+c=0$. Now

$$f_c^2(x)-x = (x^2+c)^2+c-x = (x^2-x+c)(x^2+x+c+1),$$

so the 2-cycle solves $x^2+x+c+1 = 0$:

$$x_\pm = \frac{-1\pm\sqrt{1-4(c+1)}}{2} = \frac{-1\pm\sqrt{-4c-3}}{2},$$

real for $c\le-3/4$. Its multiplier is
$(f_c^2)'(x_+) = 4x_+x_- = 4(c+1)$, using that the product of the roots is $c+1$. The cycle attracts iff
$\lvert4(c+1)\rvert<1$, i.e. $-\tfrac54<c<-\tfrac34$. At $c=-\tfrac34$ it is born from the fixed point
(multiplier $+1$); at $c=-\tfrac54$ its multiplier reaches $-1$ and the cycle doubles.

**17.** *(Strategy: apply the definition of $\delta$ to successive ratios.)*

$$\frac{\mu_2-\mu_1}{\mu_3-\mu_2} = \frac{0.449490}{0.094600} = 4.7514, \qquad
\frac{\mu_3-\mu_2}{\mu_4-\mu_3} = \frac{0.094600}{0.020317} = 4.6562, \qquad
\frac{\mu_4-\mu_3}{\mu_5-\mu_4} = \frac{0.020317}{0.004352} = 4.6684 .$$

The ratios approach $4.6692$ with errors $8.2\times10^{-2}$, $-1.3\times10^{-2}$, $-8\times10^{-4}$;
because the convergence is geometric with ratio $\approx\delta^{-1}$, each extra period gains about one
decimal digit. This is the universal behaviour of all unimodal families with a quadratic maximum.

**18.** *(Strategy: $T^n$ has $2^n$ monotone branches, each meeting the diagonal once.)*

Fixed points of $T^3$ number $2^3 = 8$; of these, $2$ are the fixed points of $T$ itself ($0$ and $2/3$).
So $6$ points have exact period $3$, forming $6/3 = 2$ orbits. Explicitly, using the branch inverses
$f_0(y)=y/2$, $f_1(y)=1-y/2$: the itinerary $\overline{001}$ gives $x=2/9$ with cycle
$\{2/9,\,4/9,\,8/9\}$, and the itinerary $\overline{011}$ gives $x = 2/7$ with cycle
$\{2/7,\,4/7,\,6/7\}$.

**19.** *(Strategy: invert each branch; on a periodic itinerary the composition reduces to a linear
equation.)*

(a) On the branch with digit $s$ the inverse of $T$ is $f_0(y) = y/2$ (for $s=0$) and $f_1(y) = 1-y/2$
(for $s=1$). Reading the itinerary backwards, a point with itinerary $\overline{001}$ satisfies
$x = f_0\bigl(f_0(f_1(x))\bigr)$. Compute $f_1(x) = 1-x/2$, then $f_0(f_1(x)) = \tfrac12 - x/4$, then
$f_0(\cdot) = \tfrac14 - x/8$. Hence $x = \tfrac14 - x/8$, giving $\tfrac98x = \tfrac14$ and $x = 2/9$.

(b) $T(2/9) = 4/9$, $T(4/9) = 8/9$, $T(8/9) = 2 - 16/9 = 2/9$. ✓ The digits are
$0$ (since $2/9\le\tfrac12$), $0$ ($4/9\le\tfrac12$), $1$ ($8/9>\tfrac12$), as required.

**20.** *(Strategy: solve the radial equation, then evaluate at $t = 2\pi$.)*

With $u = r^{-2}$, $\dot u = -2r^{-3}\dot r = -2u + 2$, so $u(t) = 1+(u_0-1)e^{-2t}$ and

$$P(r_0) = \frac{r_0}{\sqrt{r_0^2+(1-r_0^2)e^{-4\pi}}} .$$

$P(1)=1$; the cycle $r=1$ is the fixed point of $P$. Differentiating, $P'(1) = e^{-4\pi}\approx3.5\times10^{-6}$
(compute $\frac{d}{dr_0}$ at $r_0=1$ using the quotient rule, or linearise $s = r-1$: $\dot s = -2s$, so
after time $2\pi$ the perturbation is multiplied by $e^{-4\pi}$). Since $0<P'(1)<1$, the limit cycle is
asymptotically stable. Also $P'(0) = e^{2\pi}>1$, so the origin is unstable, consistent with
$\dot r\approx r$ near $0$.

**21.** *(Strategy: solve the algebraic fixed-point equations, then read the spectrum.)*

From $\dot x = 0$: $y=x$. From $\dot z = 0$: $z = xy/\beta = x^2/\beta$. From $\dot y = 0$:
$x(\rho-z) = y = x$, so either $x=0$ (the origin) or $z = \rho-1$, giving $x^2 = \beta(\rho-1)$ and the
pair $C^\pm = (\pm\sqrt{\beta(\rho-1)},\pm\sqrt{\beta(\rho-1)},\rho-1)$, real for $\rho\ge1$.

At the origin the Jacobian is block triangular with the $2\times2$ block
$\begin{pmatrix}-\sigma&\sigma\\ \rho&-1\end{pmatrix}$; the eigenvalues are $-\beta$ and the roots of
$\lambda^2+(\sigma+1)\lambda+\sigma(1-\rho)=0$. For $\sigma=10,\beta=8/3$: stable for $\rho<1$, and at
$\rho=1$ a zero eigenvalue appears with the other root $-(1+\sigma)<0$: a pitchfork.

At $C^\pm$ the characteristic polynomial is
$\lambda^3+(\sigma+\beta+1)\lambda^2+\beta(\rho+\sigma)\lambda+2\sigma\beta(\rho-1)$. Substituting
$\lambda=i\omega$ gives $\omega^2 = \beta(\sigma+\rho)$ and
$\rho_H = \frac{\sigma(\sigma+\beta+3)}{\sigma-\beta-1} = \frac{10\cdot15.6667}{6.3333} = 24.7368$.

**22.** *(Strategy: differentiate the flow in the initial condition and split off the flow direction.)*

Let $\gamma$ have period $T$ and let $p\in\gamma\cap\Sigma$. The return map is defined implicitly by
$\Phi(x,t) = \varphi_t(x) - x\in T\Sigma$ being zero with $t$ near $T$; since
$\partial_t\Phi = f(\varphi_t(x))\notin T\Sigma$ and $\partial_x\Phi$ is invertible transversally, the
implicit function theorem gives a $C^1$ map $x\mapsto (\text{return time } \tau(x), P(x))$.

Differentiating $\varphi_{\tau(x)}(x)\in\Sigma$ with respect to $x$ along $\Sigma$ shows that $DP(p)$ is
the restriction of $D\varphi_T(p)$ to a complement of the flow direction modulo $T_p\Sigma$. The
eigenvalues of $D\varphi_T(p)$ — the Floquet multipliers — therefore consist of $1$ (eigenvector $f(p)$,
since $\varphi_T$ fixes the whole orbit) together with the eigenvalues of $DP(p)$. Consequently the
periodic orbit is asymptotically stable iff all eigenvalues of $DP(p)$ lie inside the unit disc, i.e. iff
$p$ is an asymptotically stable fixed point of $P$.

**23.** *(Strategy: encode a point by its binary expansion; then $D$ is a shift.)*

Write $x = 0.b_1b_2b_3\dots$ in base $2$. Then $D(x) = 0.b_2b_3\dots$: multiplication by $2$ shifts the
binary point, and the integer part is discarded by the mod $1$. So $D$ is the shift on binary sequences,
with the usual ambiguity at dyadic rationals (a countable set, irrelevant for density and transitivity
arguments).

*Transitivity:* given open $U,V$ pick $x\in U$ and $n$ with the cylinder of points sharing the first $n$
binary digits with $x$ contained in $U$; $D^n$ of that cylinder is the whole circle, so $D^n(U)\cap V\ne\varnothing$.

*Dense periodic points:* points with eventually periodic binary expansions are dense, and they are periodic
for $D$.

*Sensitivity:* two points agreeing in the first $n$ digits are within $2^{-n}$, but after $n$ shifts they
differ in the first digit, hence are at distance at least $\tfrac12$.

Finally, $\sin^2(\pi\theta)$ semiconjugates $D$ to $f_4$ (since $\sin^2(2\pi\theta) = 4\sin^2(\pi\theta)\cos^2(\pi\theta)$),
and $h(x) = \sin^2(\pi x/2)$ conjugates $f_4$ to the tent map (Exercise 36). Transitivity and density of
periodic points pass to continuous images of dense sets and of open preimages, so the tent map inherits
them; its sensitivity was proved directly in Theorem 7.11.

**24.** *(Strategy: Green's theorem converts the divergence over the interior into a boundary integral
that vanishes on a closed orbit.)*

Suppose $\gamma$ is a closed orbit bounding a region $R\subseteq D$. On $\gamma$ the velocity $(f_1,f_2)$
is tangent to the curve, so with $\gamma(t) = (x(t),y(t))$,

$$0 = \oint_\gamma (f_1\,dy - f_2\,dx) = \oint_\gamma \bigl(f_1\dot y - f_2\dot x\bigr)dt = \oint_\gamma (f_1f_2 - f_2f_1)dt .$$

By Green's theorem the same integral equals $\iint_R \operatorname{div}f\,dA$. If $\operatorname{div}f$
has constant sign and is not identically zero, the double integral is strictly positive or strictly
negative, a contradiction. So no closed orbit exists in $D$.

For $\dot x = -y+x^3$, $\dot y = x+y^3$: $\operatorname{div}f = 3x^2+3y^2\ge0$, and it vanishes only at
the origin, so it is positive on every region with nonempty interior not equal to $\{0\}$. Taking
$D = \mathbb{R}^2$ (simply connected), there is no closed orbit at all. Note the origin is a fixed point
with eigenvalues $\pm i$ (a linear centre), so this is exactly the case where the linearisation would
suggest oscillation: the nonlinear terms destroy every closed orbit.

## Advanced

**25.** *(Strategy: compare $V$ on a sphere with $V$ near the origin.)*

Let $\varepsilon>0$ be small enough that $\overline{B_\varepsilon(p)}\subseteq U$, and let
$S_\varepsilon = \{\lVert x-p\rVert = \varepsilon\}$. $S_\varepsilon$ is compact and $V>0$ on it, so
$m := \min_{S_\varepsilon}V>0$ exists and is attained. Since $V$ is continuous at $p$ and $V(p)=0$, there
is $\delta\in(0,\varepsilon)$ such that $\lVert x-p\rVert<\delta$ implies $V(x)<m$.

Now take any $x_0$ with $\lVert x_0-p\rVert<\delta$ and suppose, for contradiction, that
$\lVert\varphi_t(x_0)-p\rVert\ge\varepsilon$ for some $t>0$. Let $t_1$ be the first such time (it exists
by continuity of $t\mapsto\varphi_t(x_0)$). Then $\varphi_{t_1}(x_0)\in S_\varepsilon$, so
$V(\varphi_{t_1}(x_0))\ge m$. But $\frac{d}{dt}V(\varphi_t(x_0)) = \dot V\le0$, so $V$ is non-increasing
along the orbit and $V(\varphi_{t_1}(x_0))\le V(x_0)<m$. Contradiction. Hence the orbit stays in
$B_\varepsilon(p)$ for all $t\ge0$: this is Lyapunov stability. Compactness of $S_\varepsilon$ was used
to make the minimum exist and be positive; continuity of $V$ was used to find $\delta$.

**26.** *(Strategy: the $\omega$-limit set is nonempty, compact, invariant, and $V$ is constant on it.)*

Let $x\in\Omega$ and $\omega = \omega(x)$. Since the orbit stays in the compact set $\Omega$, $\omega$ is
nonempty, compact, and invariant (a standard fact: if $y = \lim\varphi_{t_k}(x)$ then
$\varphi_t(y) = \lim\varphi_{t_k+t}(x)$). Moreover $V(\varphi_t(x))$ is non-increasing, so it has a limit
$\ell$, and by continuity $V\equiv\ell$ on $\omega$. Hence $\dot V = 0$ on $\omega$, i.e.
$\omega\subseteq E$; since $\omega$ is invariant, $\omega\subseteq M$, the largest invariant subset of
$E$.

It remains to pass from $\omega(x)\subseteq M$ to $\operatorname{dist}(\varphi_t(x),M)\to0$. If not,
there are $t_k\to\infty$ and $\eta>0$ with $\operatorname{dist}(\varphi_{t_k}(x),M)\ge\eta$. By
compactness of $\Omega$ a subsequence converges to some $y\in\omega(x)\subseteq M$, contradicting
$\operatorname{dist}(y,M)\ge\eta$ (distance to a closed set is continuous). So every orbit approaches $M$.

**27.** *(Strategy: integrate the derivative of $e^{A^{\mathsf T}t}e^{At}$; the rest is estimates.)*

The integrand decays exponentially because $\lVert e^{At}\rVert\le Ce^{-\alpha t}$ with $\alpha>0$, so
$P$ is well defined and $\lVert P\rVert\le C^2/(2\alpha)<\infty$. It is symmetric since
$(e^{A^{\mathsf T}t}e^{At})^{\mathsf T} = e^{A^{\mathsf T}t}e^{At}$, and positive definite because
$x^{\mathsf T}Px = \int_0^\infty\lVert e^{At}x\rVert^2dt>0$ for $x\ne0$ ($e^{At}$ is invertible).

For the equation, use $\frac{d}{dt}\left(e^{A^{\mathsf T}t}e^{At}\right) = A^{\mathsf T}e^{A^{\mathsf T}t}e^{At} + e^{A^{\mathsf T}t}e^{At}A$
and integrate:

$$e^{A^{\mathsf T}t}e^{At}\Big|_0^\infty = A^{\mathsf T}P + PA \ \Rightarrow\ -I = A^{\mathsf T}P + PA .$$

Let $\mu$ and $M$ be the smallest and largest eigenvalues of $P$. Then
$\mu\lVert x\rVert^2\le V(x)\le M\lVert x\rVert^2$ and $\dot V = -x^{\mathsf T}x = -\lVert x\rVert^2\le -V/M$.
Hence $V(\varphi_t)\le V(x_0)e^{-t/M}$, so $\lVert\varphi_t(x_0)\rVert^2\le \frac{M}{\mu}e^{-t/M}\lVert x_0\rVert^2$:
exponential stability with rate $1/(2M)$ in the norm and constant $\sqrt{M/\mu}$.

**28.** *(Strategy: the fixed point moves continuously and the spectrum cannot jump.)*

Let $p$ be a hyperbolic fixed point of $f$. Since $\lvert\lambda_j\rvert\ne1$, the distance
$\eta := \min_j\bigl\lvert\lvert\lambda_j\rvert-1\bigr\rvert>0$. Choose $r>0$ so small that the closed
ball $\overline{B_r(p)}$ contains no other fixed point and $Df$ is close to $Df(p)$ there. For $g$ close
to $f$ in $C^1$, the map $g$ has a unique fixed point $p_g$ in $B_r(p)$: this follows from the contraction
mapping principle applied to $x\mapsto p + (I - Df(p))^{-1}(\,p - x + g(x)\,)$-type formulation, or from
the implicit function theorem applied to $F(p,\epsilon) = p - f(p) - \epsilon(g-f)(p)$ continued from
$\epsilon = 0$ to $\epsilon = 1$. Continuity of eigenvalues then gives $\lvert\lambda_j(Dg(p_g))\rvert$
within $\eta/2$ of $\lvert\lambda_j(Df(p))\rvert$, hence still different from $1$.

**29.** *(Strategy: prove the three properties for the shift, then transfer along the itinerary
bijection.)*

Transitivity, dense periodic points and sensitivity for $\sigma$ were proved in Theorem 7.12.

For the tent map, let $S:[0,1]\to\Sigma_2$ be the itinerary map, which satisfies $S\circ T = \sigma\circ S$
and is a bijection (§7.9). If $U\subseteq[0,1]$ is open, then $S(U)$ is a union of cylinders up to the
countable ambiguity set, so it contains a cylinder; applying transitivity of $\sigma$ to two such
cylinders and pulling back gives $T^n(U)\cap V\ne\varnothing$. A periodic sequence corresponds under
$S^{-1}$ to a periodic point of $T$; since periodic sequences are dense and $S^{-1}$ maps cylinders to
intervals, periodic points of $T$ are dense. Sensitivity was proved directly in Theorem 7.11; alternatively
it follows from transitivity plus density of periodic points by the theorem of Banks et al. quoted in
§7.8.

**30.** *(Strategy: count fixed points on the $2^n$ monotone branches, then apply Möbius inversion.)*

Each cylinder $C_w$ of length $2^{-n}$ is mapped by $T^n$ affinely onto $[0,1]$ with slope $\pm2^n$, so
the equation $T^n(x)=x$ has exactly one solution in each cylinder and none elsewhere: $\#\mathrm{Fix}(T^n) = 2^n$.
Let $a_n$ be the number of points of exact period $n$, so $2^n = \sum_{d\mid n}a_d$ (each point of period
$d\mid n$ is fixed by $T^n$). Möbius inversion gives $a_n = \sum_{d\mid n}\mu(d)2^{n/d}$, and each orbit
contributes $n$ points, so the number of orbits of exact period $n$ is $\frac1n\sum_{d\mid n}\mu(d)2^{n/d}$.
For $n = 3$: $\frac13(2^3 - 2) = 2$, in agreement with Exercise 18.

**31.** *(Strategy: apply the implicit function theorem to the return condition.)*

Let $p\in\gamma$, $T$ the period, and $\Sigma$ a small disc transverse to $f(p)$ at $p$. Define
$F(x,t) = \varphi_t(x) - x$. Then $F(p,T) = 0$ and $\partial_tF(p,T) = f(\varphi_T(p)) = f(p)$, which is
transverse to $\Sigma$; also $\partial_xF$ restricted to $T\Sigma$ is invertible modulo the flow direction.
The implicit function theorem therefore gives $C^1$ functions $\tau(x)$ (return time) and $P(x)$ with
$P(p) = p$.

For stability: a nearby orbit returns to $\Sigma$ at $P(x)$ and the segment between returns stays close to
$\gamma$ by continuous dependence on initial data. Hence orbits converge to $\gamma$ iff the iterates
$P^n(x)\to p$, which is the definition of asymptotic stability of the fixed point of $P$. In the linear
approximation the return map is $DP(p)$, whose eigenvalues are the nontrivial Floquet multipliers
(Exercise 22).

**32.** *(Strategy: construct the conjugacy by matching the time-one maps, then differentiate.)*

For $\dot x = -x$, $\phi_t(x) = e^{-t}x$, so $\phi_1(x) = e^{-1}x$. For $\dot x = -x^3$,
$\psi_t(x) = x/\sqrt{1+2x^2t}$, so $\psi_1(x) = x/\sqrt{1+2x^2}$.

Define $h(x) = \operatorname{sgn}(x)\exp\left(-\frac{1}{2x^2}\right)$ for $x\ne0$ and $h(0)=0$. This is
odd, strictly increasing, with limits $\pm1$ at $\pm\infty$; hence a homeomorphism of $\mathbb{R}$.
Compute $h(e^{-1}x) = \exp\left(-\frac{1}{2e^{-2}x^2}\right)\operatorname{sgn}x = e^{-1}h(x)$, and

$$h\bigl(\psi_1(x)\bigr) = \exp\left(-\frac{1+2x^2}{2x^2}\right)\operatorname{sgn}x = e^{-1}h(x) = h\bigl(\phi_1(x)\bigr).$$

So $h$ conjugates the time-one maps; since the flows are determined by their time-one maps, $h$ conjugates
the flows.

Now suppose $h$ were $C^1$ with $h'(0)\ne0$ (necessary for a diffeomorphism). Differentiating
$h(\varphi_t(x)) = \psi_t(h(x))$ in $t$ at $t=0$ gives $h'(x)\cdot(-x) = -h(x)^3$, i.e. $h'(x) = h(x)^3/x$ for
$x\ne0$. If $h(x) = ax + o(x)$ with $a\ne0$, the right side behaves like $a^3x^3/x = a^3x^2\to0$, so
$h'(0)=0$, contradicting $a\ne0$. Hence no $C^1$ conjugacy exists.

This is exactly the sharpness of Hartman–Grobman: it gives a topological conjugacy and nothing more, even
between two systems with the same linear part.

## Challenge

**33.** *(Strategy: differentiate the candidate and complete the square.)*

With $V = \rho x^2+\sigma y^2+\sigma(z-2\rho)^2$,

$$\tfrac12\dot V = \rho x\,\sigma(y-x) + \sigma y\bigl(x(\rho-z)-y\bigr) + \sigma(z-2\rho)(xy-\beta z).$$

Expanding each term,

$$\tfrac12\dot V = \bigl(\rho\sigma xy - \rho\sigma x^2\bigr) + \bigl(\sigma\rho xy - \sigma xyz - \sigma y^2\bigr) + \bigl(\sigma xyz - 2\rho\sigma xy - \sigma\beta z^2 + 2\sigma\beta\rho z\bigr).$$

The $xy$ terms sum to $\rho\sigma + \sigma\rho - 2\rho\sigma = 0$ and the $xyz$ terms to $-\sigma+\sigma = 0$, so

$$\dot V = -2\sigma\rho x^2 - 2\sigma y^2 - 2\sigma\beta z^2 + 4\sigma\beta\rho z
= -2\sigma\rho x^2 - 2\sigma y^2 - 2\sigma\beta(z-\rho)^2 + 2\sigma\beta\rho^2 .$$

Hence $\dot V<0$ wherever $2\sigma\rho x^2 + 2\sigma y^2 + 2\sigma\beta(z-\rho)^2 > 2\sigma\beta\rho^2$,
which is the exterior of a fixed ellipsoid. Every orbit therefore enters the ellipsoid
$\{V\le \text{const}\}$ and remains in a bounded absorbing set, so $\omega$-limit sets are nonempty,
compact and invariant.

Volumes: $\operatorname{div}f = -(\sigma+1+\beta)<0$ is constant, so a region of volume $W_0$ has volume
$W_0e^{-(\sigma+1+\beta)t}$ at time $t$ (Liouville's formula). An invariant compact attractor inside the
absorbing region must therefore have zero volume. Combined with the positive Lyapunov exponent, this is
the "strange" geometry of §7.10.

**34.** *(Strategy: divide $f_c^3(x)-x$ by the fixed-point polynomial, then recognise a perfect square.)*

(a) $f_c(x) = x^2+c$ has fixed points solving $x^2-x+c=0$; dividing $f_c^3(x)-x$ (a polynomial of degree
$8$) by that quadratic leaves a degree-$6$ polynomial. At $c = -\tfrac74$ the division gives

$$f_{-7/4}^3(x)-x = \frac{1}{256}\left(4x^2-4x-7\right)\left(8x^3+4x^2-18x-1\right)^2 .$$

The squared factor is the signature of a *tangency*: $f^3(x)-x$ has a double root, so the graph of $f^3$
touches the diagonal without crossing it.

(b) The double root is a root of $8x^3+4x^2-18x-1=0$, whose roots are approximately
$1.30194$, $-0.054958$ and $-1.74698$. These three form the 3-cycle at birth:

$$1.30194 \mapsto -0.054958 \mapsto -1.74698 \mapsto 1.30194 .$$

At $c=-\tfrac74$ the cycle has multiplier exactly $+1$; it is a saddle-node (tangent) bifurcation of the
third iterate.

(c) For $c$ slightly less than $-\tfrac74$ the double root splits into two simple roots: a stable 3-cycle
and an unstable 3-cycle, born together. Almost every orbit is then attracted to the stable 3-cycle, so the
visible dynamics is periodic with period 3 — this is the "period-3 window" of the logistic family,
translated to the quadratic family. As $c$ decreases further, the stable 3-cycle undergoes its own
period-doubling cascade.

**35.** *(Strategy: the covering lemma produces periodic orbits from any cyclic chain of intervals.)*

**Lemma (covering).** Let $J_0,\dots,J_{n-1}$ be closed intervals with $f(J_k)\supseteq J_{k+1}$ for
$k<n-1$ and $f(J_{n-1})\supseteq J_0$. Then there is $x\in J_0$ with $f^k(x)\in J_k$ for $k<n$ and
$f^n(x) = x$.

*Proof.* For each $k$ choose a closed subinterval $K_k\subseteq J_k$ with $f(K_k) = J_{k+1}$ (possible
because $f(J_k)\supseteq J_{k+1}$: take a component of $f^{-1}(J_{k+1})$ inside $J_k$ whose image is all of
$J_{k+1}$). Then $f^n(K_0) = f^{n-1}(J_1)\supseteq\cdots\supseteq J_0\supseteq K_0$. So $f^n$ maps $K_0$
continuously into a set containing $K_0$; the function $x\mapsto f^n(x)-x$ is then $\le0$ at one endpoint
of $K_0$ and $\ge0$ at the other (or vice versa), so it vanishes somewhere in $K_0$ by the intermediate
value theorem. That point is the required periodic point, and $f^k(x)\in J_k$ by construction. $\blacksquare$

Now let $x_1<x_2<x_3$ with $f(x_1)=x_2$, $f(x_2)=x_3$, $f(x_3)=x_1$, and put
$I_1 = [x_1,x_2]$, $I_2 = [x_2,x_3]$. On $I_1$ the values go from $x_2$ to $x_3$, so
$f(I_1)\supseteq[x_2,x_3] = I_2$. On $I_2$ the values go from $x_3$ to $x_1$, so
$f(I_2)\supseteq[x_1,x_3]\supseteq I_1\cup I_2$.

Fix $n\ge2$ and take the word $J_0 = I_1$, $J_1 = I_2$, $J_k = I_1$ for $2\le k\le n-1$. Each covering
condition holds, so the lemma gives $x\in I_1$ with $f(x)\in I_2$, $f^k(x)\in I_1$ for $2\le k\le n$ and
$f^n(x)=x$.

*Exact period.* Record the *address* of a point by the interval $I_1$ or $I_2$ containing it, counting the
common endpoint $x_2$ as belonging to $I_2$. The orbit segment $x, f(x),\dots,f^{n-1}(x)$ then has the
address word $I_1, I_2, I_1, \dots, I_1$, which contains exactly one $I_2$. If the period were a proper
divisor $d<n$ of $n$, the address word would be $d$-periodic, hence would contain $n/d\ge2$ copies of
$I_2$ — contradiction. (If $d$ does not divide $n$, a periodic point of period $d$ satisfies $f^n(x)=x$
only when $d\mid n$, so no other case arises.) Therefore $x$ has exact period $n$.

Since $n\ge2$ was arbitrary and the 3-cycle supplies the hypothesis, $f$ has points of every period. (The
period-1 case is the fixed point given by the intermediate value theorem on $[x_1,x_3]$, since $f$ maps
that interval across itself.)

**36.** *(Strategy: verify the conjugacy on each branch, then transfer chaos and compute the exponent.)*

*Conjugacy.* Let $h(x) = \sin^2(\pi x/2)$, a strictly increasing homeomorphism of $[0,1]$ onto itself.
For $0\le x\le\tfrac12$: $h(Tx) = h(2x) = \sin^2(\pi x)$, and
$f_4(h(x)) = 4\sin^2(\pi x/2)\cos^2(\pi x/2) = \sin^2(\pi x)$. For $\tfrac12<x\le1$:
$h(Tx) = h(2-2x) = \sin^2(\pi-\pi x) = \sin^2(\pi x)$, the same. Hence
$h\circ T = f_4\circ h$ on all of $[0,1]$.

*Chaos.* A conjugacy preserves all three properties of Definition 5.9: it carries open sets to open sets,
periodic points to periodic points and distances are controlled in both directions by compactness and
continuity. Since $T$ is chaotic (Theorem 7.11), so is $f_4$ on $[0,1]$.

*Lyapunov exponent.* Differentiate $h\circ T = f_4\circ h$:
$h'(T x)T'(x) = f_4'(h(x))h'(x)$. Taking logarithms and summing along an orbit of $T$ (a.e. avoiding the
countable set where $h'$ vanishes or $T$ is not differentiable),

$$\sum_{k<n}\ln\lvert f_4'(y_k)\rvert = \sum_{k<n}\ln\lvert T'(x_k)\rvert + \ln\lvert h'(x_n)\rvert - \ln\lvert h'(x_0)\rvert,$$

with $y_k = h(x_k)$. The first sum equals $n\ln2$. Since $\ln\lvert h'\rvert = \ln\left(\frac{\pi}{2}\lvert\sin\pi x\rvert\right)$
is integrable on $[0,1]$ and Lebesgue measure is invariant and ergodic for $T$, Birkhoff's ergodic theorem
gives $\frac1n\ln\lvert h'(x_n)\rvert\to0$ for almost every $x$; the last term is $O(1/n)$. Hence
$\lambda = \ln 2$ for Lebesgue-almost every $y$, matching the tent map.

*Why not $C^1$.* $h'(x) = \frac{\pi}{2}\sin(\pi x)$ vanishes at $x=0$ and $x=1$, so $h$ is not a local
diffeomorphism at the endpoints. This does not affect the conclusions: chaos is a topological property,
and it is preserved by homeomorphisms; and the Lyapunov exponent is unaffected because the correction term
is $o(n)$ along almost every orbit. A homeomorphism that is not a diffeomorphism can distort a metric, but
it cannot change whether orbits separate exponentially in the limit.
