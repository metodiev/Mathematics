# Conformal Mappings — Solutions

> [Tutorial](README.md) · [Exercises](exercises.md) · 36 worked solutions

Each solution states the strategy, carries out every step, names the theorem used with its hypotheses,
and verifies the map on the boundary where one is constructed.

## Beginner

**1.** *Strategy: compute $f'$ and locate its zeros inside the domain.*
(a) $f'=3z^2-3=3(z-1)(z+1)$, so $f$ is conformal on $\mathbb{C}\setminus\{1,-1\}$ and fails at both
points, where angles are doubled.
(b) $f'=2ze^{z^2}$, and $e^{z^2}$ never vanishes, so the only critical point is $0$: conformal on
$\mathbb{C}\setminus\{0\}$.
(c) $f'=\cosh z$, which vanishes exactly where $e^z=-e^{-z}$, i.e. $e^{2z}=-1$, i.e.
$z=\frac{i\pi}{2}+ik\pi$, $k\in\mathbb{Z}$: conformal on the complement of that set.
(d) $f'=\dfrac{(z+2)-(z-1)}{(z+2)^2}=\dfrac{3}{(z+2)^2}$, never zero; $f$ is undefined at $-2$, so it is
conformal on $\mathbb{C}\setminus\{-2\}$.

**2.** Write $z=x+iy$ and $\bar z=x-iy$. The map is real-linear with Jacobian
$\begin{pmatrix}1&0\\0&-1\end{pmatrix}$, of determinant $-1\ne0$, so it is invertible everywhere. For a
curve $\gamma$ with tangent $\gamma'(0)=re^{i\theta}$, the image has tangent
$\overline{\gamma'(0)}=re^{-i\theta}$: lengths are preserved and arguments change sign. Hence the
magnitude of every angle is preserved but the orientation is reversed, so the map is *not* conformal in
the sense of Definition 5.1, which requires oriented angles to be preserved. It is antiholomorphic, and
the Cauchy–Riemann equations hold for $\bar f$ rather than $f$.

**3.** $f'(z)=1-\dfrac{1}{z^2}=\dfrac{z^2-1}{z^2}$, which vanishes exactly at $z=\pm1$ and is undefined at
$z=0$; hence $f$ is conformal on $\mathbb{C}\setminus\{0,1,-1\}$. Near $z=1$,
$$f(z)-2=z+\frac1z-2=\frac{(z-1)^2}{z},$$
so $z=1$ is a double zero of $f-2$: the map is locally two-to-one there and doubles angles, mapping a
right angle to a straight angle. The point $z=-1$ behaves the same way by symmetry, and $z=0$ is a pole,
not a point of the domain.

**4.** For real $x$, $\lvert T(x)\rvert^2=\dfrac{x^2+1}{x^2+1}=1$, so the real axis is mapped into the
unit circle; since $T$ is injective on $\widehat{\mathbb{C}}$ and $\mathbb{R}\cup\{\infty\}$ is a
generalised circle, the image is exactly the unit circle. Moreover $T(\infty)=1$, and the pole
$z=-i\notin\mathbb{R}$, so no point of the real axis is sent to $\infty$: the image is the circle
$\lvert w\rvert=1$ with the point $1$ corresponding to $\infty$.

**5.** *Strategy: fit a Möbius map to three points.* The map $T(z)=1-z$ has matrix
$\begin{pmatrix}-1&1\\0&1\end{pmatrix}$ of determinant $-1\ne0$, and $T(0)=1$, $T(1)=0$,
$T(\infty)=\infty$. By Theorem 7.7 it is the unique such map.

**6.** With $z_1=0$, $z_2=2$, $z_3=1$, $z_4=3$:
$$(0,2;1,3)=\frac{(1-0)(3-2)}{(1-2)(3-0)}=\frac{1}{-3}=-\frac13 .$$
With $z_4=\infty$ the definition by continuity gives $(z_1,z_2;z_3,\infty)=\dfrac{z_3-z_1}{z_3-z_2}$, so
$(i,0;1,\infty)=\dfrac{1-i}{1-0}=1-i .$

**7.** *Strategy: Corollary 7.8.*
$$(0,1;2,1+i)=\frac{(2-0)(1+i-1)}{(2-1)(1+i-0)}=\frac{2i}{1+i}=\frac{2i(1-i)}{2}=1+i,$$
which is not real, so the four points are not concyclic and not collinear.

**8.** The matrix $\begin{pmatrix}3&2\\1&1\end{pmatrix}$ has determinant $1$ and trace $4$, so
$\tau=16>4$ and $T$ is hyperbolic. Fixed points: $z=\dfrac{3z+2}{z+1}$ gives $z^2+z=3z+2$, i.e.
$z^2-2z-2=0$, so $z=1\pm\sqrt3$, both real. The multiplier at $1+\sqrt3$ is $\lambda=(z+1)^{-2}$ with
$z+1=2+\sqrt3$, so $\lambda=(2+\sqrt3)^{-2}=7-4\sqrt3\approx0.072$, and
$\lambda+\lambda^{-1}=14=\tau-2$, as Theorem 7.11 requires.

**9.** $T(z)=1/z$ has matrix $\begin{pmatrix}0&1\\1&0\end{pmatrix}$ of determinant $-1$, so
$\tau=\operatorname{tr}^2/\det=0$: elliptic. Fixed points solve $z=1/z$, i.e. $z^2=1$, so $z=\pm1$ (note
$\infty\mapsto0$, so $\infty$ is not fixed). The multiplier is $T'(1)=-1/(1)^2=-1$, a rotation by $\pi$:
$T$ is an involution.

**10.** For $z=x+iy$,
$$\lvert z-i\rvert^2=x^2+(y-1)^2,\qquad \lvert z+i\rvert^2=x^2+(y+1)^2,$$
so $\lvert T(z)\rvert<1\iff y>0$: $T$ maps $\mathbb{H}$ into $\mathbb{D}$. It is Möbius with
$T(i)=0$, and $\mathbb{R}$ maps onto the unit circle, so the image is all of $\mathbb{D}$; $T$ is
biholomorphic on $\mathbb{H}$ because its denominator never vanishes there.

**11.** If $z=re^{i\theta}$ then $z^2=r^2e^{2i\theta}$: moduli are squared and arguments doubled. The
first quadrant $0<\theta<\pi/2$ maps onto $0<2\theta<\pi$, i.e. $\mathbb{H}$. The sector
$0<\theta<\pi/4$ maps onto $0<2\theta<\pi/2$, the first quadrant. Both maps are bijective on their
sectors.

**12.** For $z=x+iy$ with $0<y<\pi/2$, $e^z=e^xe^{iy}$ has modulus $e^x\in(0,\infty)$ and argument
$y\in(0,\pi/2)$; conversely every $w$ with $0<\arg w<\pi/2$ is $e^z$ for $z=\log w$ with
$\operatorname{Im}\log w\in(0,\pi/2)$. So the image is the first quadrant.

## Intermediate

**13.** By Theorem 7.25 every automorphism is $\varphi(z)=e^{i\theta}\dfrac{z-a}{1-\bar az}$. The
condition $\varphi(0)=0$ gives $-ae^{i\theta}=0$, hence $a=0$, and $\varphi(z)=e^{i\theta}z$. Conversely
every rotation is an automorphism fixing $0$. So the stabiliser of $0$ is the circle group of rotations.

**14.** *Strategy: send the boundary circle to the imaginary axis.* Let $G(z)=\dfrac{1+z}{1-z}$, a Möbius
map with poles at $z=1\notin\mathbb{D}$. For $\lvert z\rvert<1$,
$$\operatorname{Re}G(z)=\operatorname{Re}\frac{(1+z)(1-\bar z)}{\lvert1-z\rvert^2}
=\frac{1-\lvert z\rvert^2}{\lvert1-z\rvert^2}>0,$$
so $G$ maps $\mathbb{D}$ into the right half-plane; for $\lvert z\rvert=1$, $z\ne1$, we have
$\lvert1+z\rvert=\lvert1-z\rvert$, so $G(z)$ is purely imaginary. The image is therefore the open right
half-plane, and $G$ is biholomorphic onto it because it is Möbius and its image is exactly that
half-plane.

**15.** $z\mapsto e^{\pi z}$ maps $0<\operatorname{Im}z<1$ bijectively onto $\mathbb{H}$ (the imaginary
part of $\pi z$ runs over $(0,\pi)$, and the exponential converts it to the argument). Composing with the
Cayley transform gives
$$F(z)=\frac{e^{\pi z}-i}{e^{\pi z}+i},$$
which is conformal from the strip onto $\mathbb{D}$.

**16.** The wedge $0<\arg z<\pi/3$ is sent bijectively onto $\mathbb{H}$ by $z^3$ (arguments triple), so
$$F(z)=\frac{z^3-i}{z^3+i}$$
maps the wedge conformally onto $\mathbb{D}$; $z=0$ is a boundary point of the wedge, not of its interior.

**17.** By Example 7.15, $h(z)=\left(\dfrac{1+z}{1-z}\right)^2$ maps the half-disc onto $\mathbb{H}$.
Composing with the Cayley transform,
$$F(z)=\frac{h(z)-i}{h(z)+i}$$
is the required map onto $\mathbb{D}$; on the arc $h$ is negative real, on the diameter positive real, so
$F$ sends the boundary of the half-disc to the unit circle.

**18.** The matrix $\begin{pmatrix}1&2\\1&-1\end{pmatrix}$ has determinant $-3$ and trace $0$, so
$\tau=0$: elliptic. Directly,
$$T(T(z))=\frac{\frac{z+2}{z-1}+2}{\frac{z+2}{z-1}-1}=\frac{z+2+2z-2}{z+2-z+1}=\frac{3z}{3}=z,$$
so $T$ is an involution, i.e. conjugate to $z\mapsto-z$. Its fixed points solve $z^2-2z-2=0$, namely
$1\pm\sqrt3$.

**19.** (a) For a rectangle the four interior angles are $\pi/2$, so $\alpha_k=\frac12$, $\beta_k=-\frac12$
and $\sum\beta_k=-2$:
$$f(z)=\int^z\prod_{k=1}^{4}(\zeta-x_k)^{-1/2}\,d\zeta .$$
The integral is elliptic; the side lengths are complete elliptic integrals.
(b) For angles $\pi/2,\pi/6,\pi/3$ we have $\alpha=\frac12,\frac16,\frac13$ and
$\beta=-\frac12,-\frac56,-\frac23$, whose sum is $-\frac{3+5+4}{6}=-2$, as the rule requires:
$$f(z)=\int^z(\zeta+1)^{-1/2}\zeta^{-5/6}(\zeta-1)^{-2/3}\,d\zeta .$$

**20.** With $u\equiv c$ on the circle,
$$u(re^{i\theta})=\frac{c}{2\pi}\int_0^{2\pi}P_r(\theta-t)\,dt=\frac{c}{2\pi}\cdot2\pi=c,$$
using the translation invariance of the integral and $\int_0^{2\pi}P_r=2\pi$ (Exercise 29). So the
harmonic extension of a constant is that constant, consistent with the maximum principle.

**21.** *Strategy: guess a function of $y$ alone.* Every $u=u(y)$ is harmonic, since $u_{xx}=0=u_{yy}$.
The linear function $u(x,y)=y/\pi$ takes the values $0$ at $y=0$ and $1$ at $y=\pi$, so it solves the
problem; uniqueness follows because the difference of two solutions is harmonic, continuous on the closed
strip and zero on the boundary, hence zero by the maximum principle (applied on truncated strips
$0<y<\pi$, $|x|\le R$, and then letting $R\to\infty$).

**22.** $w=\dfrac{1}{\pi}\log z$ with the principal logarithm: for $z\in\mathbb{H}$,
$\log z=\ln\lvert z\rvert+i\arg z$ with $0<\arg z<\pi$, so $0<\operatorname{Im}w<1$; the map is
holomorphic with $w'=1/(\pi z)\ne0$ and is bijective onto the strip.

**23.** For $z=e^{i\theta}$, $w=z+1/z=2\cos\theta\in[-2,2]$: the unit circle maps onto the segment
$[-2,2]$, with $\theta$ and $-\theta$ giving the same point, so it is traversed twice. For
$\lvert z\rvert>1$ the map is injective. Indeed $w=z+1/z$ is equivalent to $z^2-wz+1=0$; the two roots
have product $1$, so exactly one of them satisfies $\lvert z\rvert>1$ unless both lie on the unit circle,
which happens exactly when $w\in[-2,2]$. Hence the image of $\lvert z\rvert>1$ is
$\mathbb{C}\setminus[-2,2]$.

## Advanced

**24.** *Strategy: the local normal form at a critical point.* Suppose $f$ is holomorphic and injective
on a domain and $f'(z_0)=0$. Then $m\ge2$ is the order of the zero of $f(z)-f(z_0)$ at $z_0$, so
$$f(z)-f(z_0)=(z-z_0)^m h(z)$$
with $h$ holomorphic and $h(z_0)\ne0$. Choose $\rho>0$ so that $h\ne0$ on $\lvert z-z_0\rvert\le\rho$.
For small $w\ne0$ the equation $f(z)=f(z_0)+w$ is, by Rouché's theorem applied to
$(z-z_0)^mh(z)-w$ and $(z-z_0)^mh(z)$, satisfied by exactly $m$ values of $z$ inside the disc
$\lvert z-z_0\rvert<\rho$ (counting multiplicity). For $m\ge2$ these give at least two distinct
preimages of the same value, contradicting injectivity. Hence $f'(z_0)\ne0$ everywhere.

**25.** *Strategy: verify on generators, then use Theorem 7.5.*
Translation $z\mapsto z+b$: all differences are unchanged, so the cross-ratio is unchanged.
Scaling $z\mapsto az$ with $a\ne0$: numerator and denominator are both multiplied by $a^2$.
Inversion $z\mapsto1/z$: writing $\zeta_j=1/z_j$,
$$(\zeta_1,\zeta_2;\zeta_3,\zeta_4)=\frac{\left(\frac1{z_3}-\frac1{z_1}\right)\left(\frac1{z_4}-\frac1{z_2}\right)}
{\left(\frac1{z_3}-\frac1{z_2}\right)\left(\frac1{z_4}-\frac1{z_1}\right)}
=\frac{(z_1-z_3)(z_2-z_4)}{(z_2-z_3)(z_1-z_4)}=(z_1,z_2;z_3,z_4),$$
because each of the four differences is replaced by the corresponding difference divided by a product of
two $z$'s, and the four denominators cancel in pairs. Since every Möbius map is a composition of these
generators, the cross-ratio is invariant.

**26.** *Strategy: reduce to the Schwarz lemma by moving the base point to $0$.* Let
$\varphi_a(z)=\dfrac{z-a}{1-\bar az}$ and $g=\varphi_{f(a)}\circ f\circ\varphi_{-a}$. Then
$g:\mathbb{D}\to\mathbb{D}$ is holomorphic and $g(0)=0$, so $\lvert g(\zeta)\rvert\le\lvert\zeta\rvert$.
Putting $\zeta=\varphi_a(z)$ gives
$$\left\lvert\frac{f(z)-f(a)}{1-\overline{f(a)}f(z)}\right\rvert\le\left\lvert\frac{z-a}{1-\bar az}\right\rvert .$$
Dividing by $\lvert z-a\rvert$ and letting $z\to a$ gives the derivative form
$\lvert f'(a)\rvert\le\dfrac{1-\lvert f(a)\rvert^2}{1-\lvert a\rvert^2}$.

For the metric statement: the hyperbolic length element is $2\lvert dz\rvert/(1-\lvert z\rvert^2)$, so
$$2\frac{\lvert f'(z)\rvert\,\lvert dz\rvert}{1-\lvert f(z)\rvert^2}\le\frac{2\lvert dz\rvert}{1-\lvert z\rvert^2}$$
at every point; integrating along a curve and taking the infimum over curves gives
$d_{\mathbb{D}}(f(z_1),f(z_2))\le d_{\mathbb{D}}(z_1,z_2)$.

**27.** On $(x_k,x_{k+1})$ every factor $\zeta-x_j$ is real and nonzero, with constant sign; hence the
product $\prod_j(\zeta-x_j)^{\beta_j}$ has constant argument, and so does $f'$. A curve with constant
tangent direction is a straight line, so the image of the interval is a segment. Near $x_k$ write
$\zeta=x_k+r e^{i\varphi}$; the product behaves like $r^{\beta_k}$ times a nonzero constant, so
$$f(z)-f(x_k)\sim C'\,(z-x_k)^{\beta_k+1}=C'\,(z-x_k)^{\alpha_k},$$
which maps the half-disc of arguments $(\pi,2\pi)$ — the angle between the two sides, measured inside
$\mathbb{H}$ — onto an angle $\alpha_k\pi$. This is the interior angle of the polygon at $w_k$.

**28.** *Strategy: integrate a closed $1$-form.* Let $u$ be harmonic on a simply connected domain
$\Omega$. Consider $\omega=-u_y\,dx+u_x\,dy$. Its integrability condition is
$\frac{\partial(-u_y)}{\partial y}=\frac{\partial u_x}{\partial x}$, i.e. $-u_{yy}=u_{xx}$, which is
Laplace's equation. Hence $\omega$ is closed, and on a simply connected domain every closed $1$-form is
exact: there is $v$ with $v_x=-u_y$, $v_y=u_x$. Then $u+iv$ satisfies the Cauchy–Riemann equations with
continuous partial derivatives, so it is holomorphic and $u=\operatorname{Re}(u+iv)$.

Now let $f:\Omega'\to\Omega$ be holomorphic. Around each point of $\Omega'$ choose a disc whose image lies
in $\Omega$ and write $u=\operatorname{Re}h$ there; then $u\circ f=\operatorname{Re}(h\circ f)$ is the
real part of a holomorphic function on that disc, hence harmonic. Harmonicity is local, so $u\circ f$ is
harmonic on all of $\Omega'$.

**29.** Positivity: $1-2r\cos\varphi+r^2=(1-r)^2+2r(1-\cos\varphi)\ge(1-r)^2>0$ for $0\le r<1$, so
$P_r>0$. Integral: $P_r$ is the real part of $\dfrac{1+re^{i\varphi}}{1-re^{i\varphi}}$, and expanding
the geometric series gives $P_r(\varphi)=1+2\sum_{n\ge1}r^n\cos(n\varphi)$, hence
$$\int_0^{2\pi}P_r(\varphi)\,d\varphi=2\pi+2\sum_{n\ge1}r^n\int_0^{2\pi}\cos(n\varphi)\,d\varphi=2\pi .$$
Uniform convergence away from $0$: for $\delta\le\lvert\varphi\rvert\le\pi$,
$$0<P_r(\varphi)\le\frac{1-r^2}{1-2r\cos\delta+r^2}\longrightarrow\frac{0}{2(1-\cos\delta)}=0
\quad(r\to1^-),$$
and the bound is independent of $\varphi$, giving uniform convergence.

**30.** (a) If $f:\mathbb{D}\to\mathbb{C}$ were a conformal equivalence, its inverse
$f^{-1}:\mathbb{C}\to\mathbb{D}$ would be holomorphic and bounded, hence constant by Liouville, and a
constant map is not injective. Contradiction.
(b) A conformal equivalence is a homeomorphism, and homeomorphisms preserve simple connectivity. But
$\mathbb{D}\setminus\{0\}$ is not simply connected: the loop $\gamma(t)=\frac12e^{2\pi it}$ has winding
number $1$ about $0$, and the winding number is invariant under homotopy within $\mathbb{C}\setminus\{0\}$
(it is $\frac{1}{2\pi i}\oint dz/z$, a continuous integer-valued function of the loop). A loop that were
null-homotopic would have winding number $0$ about every point it avoids. Contradiction.

**31.** *Strategy: prove openness locally at every point.* Let $f$ be holomorphic and nonconstant on a
domain $\Omega$ and $z_0\in\Omega$. If $f'(z_0)\ne0$, the inverse function theorem for holomorphic maps
gives a holomorphic inverse on a neighbourhood of $f(z_0)$, in particular a homeomorphism onto an open
set. If $f'(z_0)=0$, write $f(z)-f(z_0)=(z-z_0)^mh(z)$ with $m\ge2$ and $h(z_0)\ne0$; on a small disc
$h$ has a holomorphic $m$-th root, and $z\mapsto(z-z_0)h(z)^{1/m}$ is a biholomorphism of a neighbourhood
of $z_0$ onto a disc sending $z_0$ to $0$. Composing with $\zeta\mapsto\zeta^m$ shows that the image of a
small disc is a disc around $f(z_0)$: $f$ is open. Hence every point has an open neighbourhood with open
image, so $f$ is an open map.

If $\varphi:\Omega_1\to\Omega_2$ is a conformal equivalence, then $\varphi$ and $\varphi^{-1}$ are
continuous, so $\varphi$ is a homeomorphism; a homeomorphism induces an isomorphism of fundamental groups,
so $\Omega_2$ is simply connected whenever $\Omega_1$ is.

## Challenge

**32.** *Strategy: remove the slit by a square root, then use a Möbius map.* Let
$\sqrt{\ }$ denote the principal branch on $\mathbb{C}\setminus(-\infty,0]$. It maps this slit plane
biholomorphically onto the right half-plane $\{w:\operatorname{Re}w>0\}$: if $z=re^{i\theta}$ with
$-\pi<\theta<\pi$, then $\sqrt z=\sqrt r\,e^{i\theta/2}$ has argument in $(-\pi/2,\pi/2)$, and every point
of the right half-plane arises uniquely. Then $G(w)=\dfrac{w-1}{w+1}$ maps $\{w:\operatorname{Re}w>0\}$
onto $\mathbb{D}$ biholomorphically: for $\operatorname{Re}w>0$,
$$\lvert w-1\rvert^2-\lvert w+1\rvert^2=-4\operatorname{Re}w<0,$$
and the imaginary axis maps onto the unit circle minus $1$, with $w=1\mapsto0$, $w=\infty\mapsto1$.
Therefore
$$F(z)=\frac{\sqrt z-1}{\sqrt z+1}$$
is a conformal bijection of $\mathbb{C}\setminus(-\infty,0]$ onto $\mathbb{D}$; its inverse is
$z=\left(\dfrac{1+w}{1-w}\right)^2$.

**33.** *Strategy: a conformal invariant computed from a Dirichlet problem.* Let $A(r,R)$ be the annulus
and let $u(z)=\dfrac{\log(\lvert z\rvert/r)}{\log(R/r)}$; then $u$ is harmonic on $A(r,R)$ with boundary
values $0$ on $\lvert z\rvert=r$ and $1$ on $\lvert z\rvert=R$. Its Dirichlet energy is
$$E(u)=\iint_{A(r,R)}\lvert\nabla u\rvert^2\,dA
=\int_0^{2\pi}\int_r^R\frac{1}{\rho^2(\log(R/r))^2}\,\rho\,d\rho\,d\theta
=\frac{2\pi}{\log(R/r)} .$$

Now let $f:A(r,R)\to A(r',R')$ be conformal and set
$$v(w)=\frac{\log(\lvert w\rvert/r')}{\log(R'/r')},$$
the harmonic function on the target annulus with boundary values $0$ and $1$. Then $v\circ f$ is
harmonic (Theorem 7.28) and has boundary values $0$ on $\lvert z\rvert=r$ and $1$ on $\lvert z\rvert=R$,
because $f$ is a homeomorphism of the closures and therefore carries boundary circles to boundary circles.
By uniqueness of the solution of the Dirichlet problem (maximum principle), $v\circ f=u$. Finally, energy
is conformally invariant: for holomorphic $f$,
$\lvert\nabla(v\circ f)\rvert^2=\lvert(\nabla v)\circ f\rvert^2\lvert f'\rvert^2$ and the area element
transforms by the same factor $\lvert f'\rvert^2$, so
$$E(v\circ f)=\iint_{A(r,R)}\lvert(\nabla v)\circ f\rvert^2\lvert f'\rvert^2\,dA=\iint_{A(r',R')}\lvert\nabla v\rvert^2\,dA=E(v).$$
Since $v\circ f=u$, the two expressions computed above are equal:
$$\frac{2\pi}{\log(R/r)}=\frac{2\pi}{\log(R'/r')},$$
hence $\log(R/r)=\log(R'/r')$ and $R/r=R'/r'$.

**34.** *Strategy: locate the critical point.* For $w=z+\dfrac{c^2}{z}$,
$$w'(z)=1-\frac{c^2}{z^2},$$
which vanishes exactly at $z=\pm c$, and $w(\pm c)=\pm2c$. Let $C$ be a circle through $z=c$ with centre
$z_0\ne c$ off the real axis and radius $R=\lvert c-z_0\rvert$; suppose $C$ encloses $-c$. The map is
conformal on and inside $C$ except at $z=c$, so the image is a closed curve with a corner at $w=2c$.
Since $w$ behaves near $c$ like $2c+\tfrac12w''(c)(z-c)^2$ with $w''(c)=2/c\ne0$, the image of a small
disc centred at $c$ covers a half-disc at $2c$: the interior angle at the corner is doubled from $\pi$ to
$2\pi$, i.e. the boundary has a **cusp** of zero angle at $w=2c$ — the trailing edge of the aerofoil. The
rest of the circle maps to a smooth closed curve joining the two sides of the cusp, producing the
aerofoil shape.

For the flow, the potential in the $z$-plane is that of a cylinder of radius $R$ with circulation
$\Gamma$; the flow at infinity has speed $U$ at angle of attack $\alpha$. The image flow has a stagnation
point at the trailing edge exactly when
$$\Gamma=4\pi UR\sin(\alpha+\beta),\qquad \beta=\arcsin\!\left(\frac{\operatorname{Im}z_0}{R}\right),$$
which is the **Kutta condition**. Then $L=\rho U\Gamma$ by Kutta–Joukowski. Without the condition $\Gamma$
would be free and the lift undetermined; the sharp trailing edge selects the observed value.

**35.** *Strategy: put the fixed points at $0$ and $\infty$.* A loxodromic $T$ has two fixed points
$\zeta_+,\zeta_-$ and multiplier $\lambda$ with $\lvert\lambda\rvert\ne1$ and
$\lambda\notin\mathbb{R}_{>0}$. Let $M$ be a Möbius map with $M(\zeta_+)=\infty$ and $M(\zeta_-)=0$; then
$S=MTM^{-1}$ fixes $0$ and $\infty$, so $S(z)=\mu z$ for some $\mu\ne0$, and $\mu$ is the multiplier at
$0$, hence $\lvert\mu\rvert\ne1$. Replacing $M$ by $z\mapsto1/M(z)$ if necessary (which swaps the two
fixed points and replaces $\mu$ by $1/\mu$), assume $\lvert\mu\rvert>1$.

Then $S^n(z)=\mu^nz\to\infty$ for every $z\ne0$, and $S^n(0)=0$. So $\infty$ is attracting and $0$ is
repelling for $S$, and consequently $\zeta_+$ is attracting and $\zeta_-$ repelling for $T$. The
convergence $S^n\to\infty$ is uniform on compact subsets of $\mathbb{C}\setminus\{0\}$ because
$\lvert\mu^n z\rvert\ge\lvert\mu\rvert^n\min\lvert z\rvert\to\infty$, and transferring back through the
homeomorphism $M$ gives $T^n(z)\to\zeta_+$ locally uniformly on $\widehat{\mathbb{C}}\setminus\{\zeta_-\}$.
The name "loxodromic" refers to the spiral paths: in the normal form $\mu=re^{i\theta}$ with $r\ne1$ and
$\theta\notin2\pi\mathbb{Z}$, the orbits spiral.

**36.** *Strategy: transport streamlines through a conformal map.* Let $\Phi(z)=U\left(z+\dfrac1z\right)$
on $\lvert z\rvert>1$ and let $w=J(z)=z+\dfrac1z$, which is conformal and injective on $\lvert z\rvert>1$
(Exercise 23) with image $\mathbb{C}\setminus[-2,2]$. Set $\Psi(w)=\Phi(J^{-1}(w))$; then $\Psi$ is
holomorphic on the image and
$$\Psi'(w)=\frac{\Phi'(z)}{J'(z)}=\frac{U(1-1/z^2)}{1-1/z^2}=U .$$
So $\Psi(w)=Uw+\text{const}$: the transported flow is uniform flow of speed $U$ along the real axis, as it
must be, because $J(z)\sim z$ at infinity.

Streamlines are level sets of $\operatorname{Im}\Phi$, and composition with a holomorphic map preserves
level sets, so they map to streamlines of $\Psi$. On $\lvert z\rvert=1$ we have
$z+1/z=2\cos\theta\in\mathbb{R}$, so $\operatorname{Im}\Phi=0$ there: the unit circle is a streamline, and
its image $[-2,2]$ is a streamline of the flow in the $w$-plane. Since $[-2,2]$ is precisely the boundary
of the domain, the normal velocity on the plate vanishes: this is the flow past a flat plate.

Stagnation points are where $\Phi'=0$, i.e. $U(1-1/z^2)=0$, namely $z=\pm1$, which map to $w=\pm2$: the
two edges of the plate are stagnation points. Near $z=1$ write $z=1+\zeta$; then
$\Phi'(z)\approx2U\zeta$ while $w-2=J(z)-2\approx\zeta^2$ (since $J''(1)=2$), so
$$\lvert\Psi'(w)\rvert=\lvert\Phi'(z)\rvert\approx2U\lvert\zeta\rvert\approx2U\lvert w-2\rvert^{1/2}\to0 .$$
The velocity therefore vanishes like the square root of the distance from the edge, the classical
edge behaviour of potential flow; adding circulation as in Example 9.7 moves the stagnation points away
from the edges and produces a lift $L=\rho U\Gamma$ on the plate.
