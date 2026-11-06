# Differential Geometry — Solutions

> [Differential Geometry](README.md) · Solutions to [exercises.md](exercises.md) · 40 problems

Each solution states the strategy, then carries out every significant step. Section references point
into [README.md](README.md). The notation is that of the exercises.

## Beginner

**1.** **Strategy.** Use $L=\int|\gamma'|\,dt$; the speed is constant.

We have $\gamma'(t)=(-2\sin t,2\cos t,3)$, so
$|\gamma'(t)|=\sqrt{4\sin^2t+4\cos^2t+9}=\sqrt{13}$. Hence

$$
L=\int_0^{4\pi}\sqrt{13}\,dt=4\pi\sqrt{13}.
$$

**2.** **Strategy.** For a circle the speed is constant, so $s=Rt$; differentiate the unit tangent with
respect to $s$.

Here $R=7$, $\gamma'(t)=(-7\sin t,7\cos t,0)$ and $|\gamma'|=7$, so $s=7t$ and
$t=s/7$. The unit-speed parametrisation is

$$
\tilde\gamma(s)=\left(7\cos\frac{s}{7},7\sin\frac{s}{7},0\right).
$$

Then

$$
T=\tilde\gamma'(s)=\left(-\sin\frac{s}{7},\cos\frac{s}{7},0\right),\qquad
\frac{dT}{ds}=-\frac17\left(\cos\frac{s}{7},\sin\frac{s}{7},0\right).
$$

Thus $\kappa=|dT/ds|=1/7$ and
$N=-(\cos(s/7),\sin(s/7),0)$. Finally
$B=T\times N=(0,0,1)$, which is constant, so $B'=0$ and $\tau=0$.

**3.** **Strategy.** A line has constant velocity, so all derivatives after the first vanish.

The velocity is $\gamma'=(4,-1,2)$ and the speed is $\sqrt{16+1+4}=\sqrt{21}$. The length over
$0\le t\le 3$ is $3\sqrt{21}$. Since $\gamma''=\mathbf{0}$, $\gamma'\times\gamma''=\mathbf{0}$ and
$\kappa=0$. The unit tangent is $T=(4,-1,2)/\sqrt{21}$. Torsion is defined only when $\kappa>0$,
because the Frenet normal $N=T'/\kappa$ is undefined; a straight line has no distinguished osculating
plane and no Frenet frame.

**4.** **Strategy.** Compute the cross product and the speed, then substitute.

We have $\gamma'=(-\sin t,2\cos t,0)$ and $\gamma''=(-\cos t,-2\sin t,0)$. Hence

$$
\gamma'\times\gamma''=(0,0,2\sin^2t+2\cos^2t)=(0,0,2),
$$

and $|\gamma'|^2=\sin^2t+4\cos^2t=1+3\cos^2t$. Therefore

$$
\kappa(t)=\frac{2}{(1+3\cos^2t)^{3/2}}.
$$

At $t=0$, $\kappa=2/4^{3/2}=2/8=1/4$; at $t=\pi/2$, $\kappa=2/1=2$. Since the curve lies in the
plane $z=0$, its torsion is $0$.

**5.** **Strategy.** Check $X_u\times X_v\ne0$; the tangent plane is the plane through the point with
normal $X_u\times X_v$.

We have $X_u=(1,0,2u)$ and $X_v=(0,1,2v)$, so

$$
X_u\times X_v=(-2u,-2v,1),
$$

whose norm is $\sqrt{1+4u^2+4v^2}>0$. Hence $X$ is regular. At $(u,v)=(1,1)$ the point is
$(1,1,2)$ and the normal is $(-2,-2,1)$. The tangent plane is

$$
-2(x-1)-2(y-1)+(z-2)=0,
\qquad\text{that is,}\qquad
z=2x+2y-2.
$$

**6.** **Strategy.** Use the chart derivatives and the area formula.

For $X(u,v)=(R\cos u,R\sin u,v)$,

$$
X_u=(-R\sin u,R\cos u,0),\quad X_v=(0,0,1),
$$

so $E=R^2$, $F=0$, $G=1$ and $\sqrt{EG-F^2}=R$. The band area is

$$
\int_0^{2\pi}\int_0^h R\,dv\,du=2\pi Rh.
$$

The circle $v=0$ is $u\mapsto(R\cos u,R\sin u,0)$, with length
$\int_0^{2\pi}R\,du=2\pi R$.

**7.** **Strategy.** Differentiate the spherical chart and integrate the area element over the zone.

For $X(\theta,\varphi)=(R\sin\theta\cos\varphi,R\sin\theta\sin\varphi,R\cos\theta)$,

$$
X_\theta=R(\cos\theta\cos\varphi,\cos\theta\sin\varphi,-\sin\theta),\qquad
X_\varphi=R\sin\theta(-\sin\varphi,\cos\varphi,0).
$$

Hence

$$
E=R^2,\qquad F=0,\qquad G=R^2\sin^2\theta,
$$

so $\sqrt{EG-F^2}=R^2\sin\theta$ for $0<\theta<\pi$. The area element is
$R^2\sin\theta\,d\theta\,d\varphi$. The zone $\theta_1\le\theta\le\theta_2$ has area

$$
A=2\pi R^2\int_{\theta_1}^{\theta_2}\sin\theta\,d\theta
=2\pi R^2(\cos\theta_1-\cos\theta_2).
$$

Taking $\theta_1=0$, $\theta_2=\pi$ gives the total area $4\pi R^2$.

**8.** **Strategy.** Normal curvature is $II/I$; in the two coordinate directions it is
$\ell/E$ and $n/G$.

With $X(u,v)=(R\cos u,R\sin u,v)$ and outward normal $\nu=(\cos u,\sin u,0)$,
$X_{uu}=(-R\cos u,-R\sin u,0)=-R\nu$, $X_{uv}=0$ and $X_{vv}=0$. Hence
$\ell=-R$, $m=0$, $n=0$, while $E=R^2$, $F=0$, $G=1$. The normal curvature in the circumferential
direction $X_u$ is $\ell/E=-1/R$; in the axial direction $X_v$ it is $n/G=0$. The principal curvatures
are $-1/R$ and $0$, so

$$
K=\kappa_1\kappa_2=0,\qquad H=\frac{\kappa_1+\kappa_2}{2}=-\frac{1}{2R}.
$$

With the inward normal both curvatures change sign and $H=+1/(2R)$; $K$ remains $0$.

**9.** **Strategy.** A chart is regular where $X_u\times X_v\ne0$. Global injectivity is a separate
requirement.

(a) $X_u=(1,0,2u)$, $X_v=(0,1,2v)$, so $X_u\times X_v=(-2u,-2v,1)\ne0$ everywhere. This is a regular
chart.

(b) $X_u=(2u,0,1)$, $X_v=(0,2v,1)$, so

$$
X_u\times X_v=(-2v,-2u,4uv).
$$

This vanishes exactly at $(u,v)=(0,0)$. Hence $X$ is regular away from the origin but is not a regular
surface chart at $(0,0)$; the image has a singular point there.

(c) $X_u=(-\sin u,\cos u,0)$, $X_v=(0,0,1)$, so $X_u\times X_v=(\cos u,\sin u,0)$, whose norm is $1$.
The map is regular everywhere. However, it is $2\pi$-periodic in $u$, so it is not injective on all of
$\mathbb{R}^2$; it is a chart on any open interval of $u$-length less than $2\pi$, and the cylinder is
covered by two such charts.

**10.** **Strategy.** In spherical coordinates $z=R\cos\theta$; critical points are where $dh=0$.

On the sphere, $h=R\cos\theta$, so $dh=-R\sin\theta\,d\theta$. This vanishes at $\sin\theta=0$, i.e.
$\theta=0$ or $\theta=\pi$: the north pole $(0,0,R)$ and the south pole $(0,0,-R)$. At any other point
$dh\ne0$. Equivalently, $dh_p(v)=\langle\mathbf{e}_3,v\rangle=v_3$, which is zero on the whole tangent
plane exactly when $\mathbf{e}_3$ is normal to the sphere, i.e. $p=\pm R\mathbf{e}_3$.

**11.** **Strategy.** Parametrise the latitude circle, compute $\gamma''$, and subtract its normal
component.

Let $\gamma(\varphi)=(\sin\theta\cos\varphi,\sin\theta\sin\varphi,\cos\theta)$ on the unit sphere. Its
speed is $\sin\theta$, so the unit tangent is $T=(-\sin\varphi,\cos\varphi,0)$. Then

$$
\frac{dT}{ds}=\frac{1}{\sin\theta}(-\cos\varphi,-\sin\varphi,0).
$$

The outward normal is $\nu=\gamma$, so
$\kappa_n=\langle\gamma'',\nu\rangle=-1/\sin\theta$. The tangential part is
$-\cot\theta\,e_\theta$, where $e_\theta=(\cos\theta\cos\varphi,\cos\theta\sin\varphi,-\sin\theta)$.
Since $\nu\times T=-e_\theta$,

$$
\kappa_g=\langle\gamma'',\nu\times T\rangle=\cot\theta.
$$

The equator $\theta=\pi/2$ has $\kappa_g=0$, so it is a geodesic (a great circle). For northern
latitudes $\theta<\pi/2$, $\kappa_g>0$; for southern latitudes it is negative. As $\theta\to0$ or
$\theta\to\pi$, the circle shrinks and $|\kappa_g|\to\infty$, as a very small circle must turn sharply.

**12.** **Strategy.** Use $\int_S K\,dA=2\pi\chi(S)$ and the known Euler characteristics.

For the sphere of radius $R$, $K=1/R^2$ and area $4\pi R^2$, so
$\int K\,dA=4\pi=2\pi\cdot2$, and $\chi(S^2)=2$.

For the torus, the computation of Section 7.8 gives $\int K\,dA=0=2\pi\cdot0$, and $\chi(T^2)=0$.
The vanishing does not mean $K\equiv0$: $K$ is positive on the outer half and negative on the inner half,
and the two contributions cancel.

## Intermediate

**13.** **Strategy.** Use the general curvature and torsion formulas.

For $\gamma(t)=(t,t^2,t^3)$,

$$
\gamma'=(1,2t,3t^2),\quad \gamma''=(0,2,6t),\quad \gamma'''=(0,0,6).
$$

At $t=1$: $\gamma'=(1,2,3)$, $\gamma''=(0,2,6)$, $\gamma'''=(0,0,6)$, and

$$
\gamma'\times\gamma''=(12-6,-6,2)=(6,-6,2),\qquad |\gamma'\times\gamma''|=2\sqrt{19}.
$$

Also $|\gamma'|=\sqrt{14}$, so

$$
\kappa=\frac{2\sqrt{19}}{14\sqrt{14}}=\frac{\sqrt{19}}{7\sqrt{14}}.
$$

Finally $\langle\gamma'\times\gamma'',\gamma'''\rangle=12$ and
$|\gamma'\times\gamma''|^2=76$, so

$$
\tau=\frac{12}{76}=\frac{3}{19}.
$$

**14.** **Strategy.** A unit-speed curve has $\kappa=|T'|$; vanishing curvature forces $T$ constant.

Let $\gamma$ be unit-speed with $\kappa\equiv0$. Then $|T'|=0$, so $T'=0$ and $T$ is a constant unit
vector $c$. Hence

$$
\gamma(s)=\gamma(0)+\int_0^sT(u)\,du=\gamma(0)+sc,
$$

which is a straight line. Conversely, a straight line parametrised by arc length has constant unit
tangent, so $T'=0$ and $\kappa=0$.

**15.** **Strategy.** Use the binormal. A planar curve has a constant normal to its plane, which must be
$\pm B$.

Assume first that $\gamma$ is unit-speed and $\kappa>0$. If $\gamma$ lies in a plane with unit normal
$n$, then $\langle\gamma,n\rangle=c$ is constant. Differentiating gives $\langle T,n\rangle=0$, and
differentiating again gives $\kappa\langle N,n\rangle=0$. Since $\kappa>0$, $\langle N,n\rangle=0$.
Thus $n$ is perpendicular to $T$ and $N$, so $n=\pm B$. Hence $B$ is constant, $B'=0$, and $\tau=0$.

Conversely, if $\tau\equiv0$, then $B'=-\tau N=0$, so $B$ is a constant unit vector. Then

$$
\frac{d}{ds}\langle\gamma,B\rangle=\langle T,B\rangle=0,
$$

so $\langle\gamma,B\rangle$ is constant and $\gamma$ lies in the plane perpendicular to $B$.

**16.** **Strategy.** Differentiate the parametrisation and use the standard surface-of-revolution
identities.

We have

$$
X_u=(-f\sin u,f\cos u,0),\qquad
X_v=(f'\cos u,f'\sin u,h').
$$

Thus

$$
E=f^2,\qquad F=0,\qquad G=f'^2+h'^2.
$$

Moreover

$$
X_u\times X_v=(fh'\cos u,fh'\sin u,-ff'),
\qquad
|X_u\times X_v|=f\sqrt{f'^2+h'^2}.
$$

Since $f>0$, the chart is regular exactly when $(f',h')\ne(0,0)$ at every point; if both derivatives
vanish, the profile has a stationary point and the parametrisation degenerates. The profile $(f,h)$
should also be injective and have no self-intersections for a global surface.

**17.** **Strategy.** Use the graph normal and the second derivatives; then apply the formula.

For $X(x,y)=(x,y,f(x,y))$, we have $X_x=(1,0,f_x)$, $X_y=(0,1,f_y)$, and

$$
E=1+f_x^2,\quad F=f_xf_y,\quad G=1+f_y^2,\quad
EG-F^2=1+f_x^2+f_y^2=W^2.
$$

The unit normal is $\nu=(-f_x,-f_y,1)/W$. Since $X_{xx}=(0,0,f_{xx})$,
$X_{xy}=(0,0,f_{xy})$ and $X_{yy}=(0,0,f_{yy})$,

$$
\ell=\frac{f_{xx}}{W},\qquad m=\frac{f_{xy}}{W},\qquad n=\frac{f_{yy}}{W}.
$$

Therefore

$$
K=\frac{\ell n-m^2}{EG-F^2}
=\frac{f_{xx}f_{yy}-f_{xy}^2}{W^4}
=\frac{f_{xx}f_{yy}-f_{xy}^2}{(1+f_x^2+f_y^2)^2}.
$$

For $z=xy$: $f_x=y$, $f_y=x$, $f_{xx}=f_{yy}=0$, $f_{xy}=1$. At the origin $W=1$, so $K=-1$.

For $z=x^2+2y^2$: $f_{xx}=2$, $f_{yy}=4$, $f_{xy}=0$, so at the origin $K=8$. The first surface is
hyperbolic at the origin, the second elliptic.

**18.** **Strategy.** The angle between coordinate curves is the angle between $X_u$ and $X_v$.

The $u$-curve has velocity $X_u$ and the $v$-curve has velocity $X_v$. Their angle $\theta$ satisfies

$$
\cos\theta=\frac{\langle X_u,X_v\rangle}{|X_u||X_v|}=\frac{F}{\sqrt{EG}}.
$$

Thus $\theta=\pi/2$ exactly when $F=0$. For the torus, a direct computation gives
$F=\langle X_u,X_v\rangle=0$: meridians and parallels are orthogonal. For
$X(u,v)=(u,v,uv)$,

$$
X_u=(1,0,v),\quad X_v=(0,1,u),\quad E=1+v^2,\quad F=uv,\quad G=1+u^2.
$$

At $(u,v)=(1,1)$, $F=1$ and $E=G=2$, so $\cos\theta=1/2$ and $\theta=\pi/3$.

**19.** **Strategy.** Use the graph area formula with polar coordinates.

For $z=x^2+y^2$, $f_x=2x$, $f_y=2y$, so

$$
\sqrt{EG-F^2}=\sqrt{1+4x^2+4y^2}=\sqrt{1+4r^2}.
$$

The area over the unit disk is

$$
A=\int_0^{2\pi}\int_0^1\sqrt{1+4r^2}\,r\,dr\,d\theta
=2\pi\left[\frac{(1+4r^2)^{3/2}}{12}\right]_0^1
=\frac{\pi}{6}\bigl(5^{3/2}-1\bigr).
$$

**20.** **Strategy.** Use the torus coefficients at $v=\pi/4$ and Euler's theorem.

At $v=\pi/4$, $\cos v=\sin v=1/\sqrt2$ and $\rho(v)=R+r/\sqrt2$. From Section 7.8,

$$
E=\rho(v)^2,\quad G=r^2,\quad \ell=-\rho(v)\cos v=-\frac{\rho(v)}{\sqrt2},\quad n=-r,\quad m=0.
$$

The principal curvatures are

$$
\kappa_1=\frac{\ell}{E}=-\frac{1}{\sqrt2\,\rho(v)}
=-\frac{1}{\sqrt2 R+r},\qquad
\kappa_2=\frac{n}{G}=-\frac1r.
$$

For a direction at angle $\pi/4$ to the principal directions, Euler's theorem gives

$$
\kappa_n=\kappa_1\cos^2\frac{\pi}{4}+\kappa_2\sin^2\frac{\pi}{4}
=\frac{\kappa_1+\kappa_2}{2}=H.
$$

Explicitly,

$$
H=-\frac{R+2r/\sqrt2}{2r(R+r/\sqrt2)}
=-\frac{R+\sqrt2\,r}{2r(R+r/\sqrt2)}.
$$

**21.** **Strategy.** Use the orthogonal-chart geodesic equations; here all metric coefficients are
constant, so the equations decouple.

For $X(u,v)=(R\cos u,R\sin u,v)$, $E=R^2$, $F=0$, $G=1$, and all derivatives of the coefficients
vanish. The geodesic equations reduce to

$$
\ddot u=0,\qquad \ddot v=0,
$$

so $u(t)=at+b$ and $v(t)=ct+d$. If $a=0$, the curve is a vertical line; if $c=0$, it is a horizontal
circle; if both are nonzero, it is a helix. Conversely, every such curve satisfies the geodesic
equations. The unit-speed condition is $R^2a^2+c^2=1$. These curves are exactly the images of straight
lines in the plane under the unrolling map $(u,v)\mapsto(Ru,v)$, which is a local isometry.

**22.** **Strategy.** Choose the variation field $V=fT$ in the first variation formula.

Let $\gamma$ be a geodesic and let $f$ be smooth with $f(a)=f(b)=0$. The variation
$\alpha(s,t)=\gamma(t)+sf(t)T(t)$ (projected to the surface if necessary; since $T$ is tangent, the
first-order variation is tangent) has variation field $V=fT$ and fixed endpoints. For the energy,

$$
0=E'(0)=-\int_a^b\langle fT,\gamma''\rangle\,dt
=-\frac12\int_a^b f\,\frac{d}{dt}\langle\gamma',\gamma'\rangle\,dt.
$$

This holds for every such $f$, so $\frac{d}{dt}|\gamma'|^2=0$ on $(a,b)$. Hence $|\gamma'|$ is constant.

Alternatively, differentiate $\langle\gamma',\gamma'\rangle$ directly:
$\frac{d}{dt}|\gamma'|^2=2\langle\gamma'',\gamma'\rangle=2\langle\gamma''{}^\top,\gamma'\rangle=0$,
because $\gamma''{}^\top=0$ and $\gamma'$ is tangent.

**23.** **Strategy.** Write the geodesic equation for the angular coordinate and use constant speed.

For $X(u,v)=(f(v)\cos u,f(v)\sin u,h(v))$, $E=f^2$, $F=0$ and $G=f'^2+h'^2$. The $u$-equation is

$$
\ddot u+\Gamma^1_{12}\dot u\dot v+\Gamma^1_{21}\dot v\dot u=0,
\qquad
\Gamma^1_{12}=\frac{E_v}{2E}=\frac{f'}{f}.
$$

Hence $\ddot u+2(f'/f)\dot u\dot v=0$, which is $(f^2\dot u)'=0$. Thus $f^2\dot u=c$ is constant. If
$\psi$ is the angle between the geodesic and the parallel, then

$$
\cos\psi=\frac{\langle\dot uX_u+\dot vX_v,X_u\rangle}{|\gamma'|\,|X_u|}
=\frac{f^2\dot u}{|\gamma'|f}=\frac{f\dot u}{|\gamma'|}.
$$

Since a geodesic has constant speed, $|\gamma'|$ is constant, so

$$
f\cos\psi=\frac{f^2\dot u}{|\gamma'|}=\frac{c}{|\gamma'|}
$$

is constant. For the sphere, $f=R\sin\theta$ (with $\theta$ the colatitude), so
$R\sin\theta\cos\psi$ is constant; this is the conserved angular momentum of a great circle. For the
cylinder, $f=R$ is constant, so $\cos\psi$ is constant: geodesics meet all parallels at the same angle,
which characterises helices.

**24.** **Strategy.** Use $K=\cos v/[r(R+r\cos v)]$ and
$\sqrt{EG-F^2}=r(R+r\cos v)$.

The product is $K\sqrt{EG-F^2}=\cos v$. Hence

$$
\int_{T^2}K\,dA
=\int_0^{2\pi}\int_0^{2\pi}\cos v\,du\,dv
=\left(\int_0^{2\pi}du\right)\left(\int_0^{2\pi}\cos v\,dv\right)=0.
$$

By Gauss–Bonnet, $\int_{T^2}K\,dA=2\pi\chi(T^2)=2\pi\cdot0=0$, in agreement. The result reflects the
cancellation of the positive curvature on the outer half and the negative curvature on the inner half.

## Advanced

**25.** **Strategy.** Differentiate the energy under the integral, integrate by parts, and use that the
variation field is arbitrary and tangent.

Let $\alpha:(-\varepsilon,\varepsilon)\times[a,b]\to S$ be smooth, with
$\alpha(0,t)=\gamma(t)$, $\alpha(s,a)=p$, $\alpha(s,b)=q$ for all $s$. Put
$V(t)=\alpha_s(0,t)$. Then $V(a)=V(b)=0$ and $V(t)\in T_{\gamma(t)}S$. The energy is

$$
E(s)=\frac12\int_a^b\langle\alpha_t(s,t),\alpha_t(s,t)\rangle\,dt.
$$

Differentiating under the integral sign,

$$
E'(s)=\int_a^b\langle\alpha_{st},\alpha_t\rangle\,dt.
$$

At $s=0$, $\alpha_t(0,t)=\gamma'(t)$, so

$$
E'(0)=\int_a^b\langle V_t,\gamma'\rangle\,dt
=\bigl[\langle V,\gamma'\rangle\bigr]_a^b-\int_a^b\langle V,\gamma''\rangle\,dt
=-\int_a^b\langle V,\gamma''\rangle\,dt,
$$

where the boundary term vanishes because $V(a)=V(b)=0$. Since $V$ is tangent,
$\langle V,\gamma''\rangle=\langle V,\gamma''{}^\top\rangle$, so

$$
E'(0)=-\int_a^b\langle V,\gamma''{}^\top\rangle\,dt.
$$

If $\gamma''{}^\top=0$, then $E'(0)=0$ for every variation. Conversely, if $E'(0)=0$ for every
variation, choose $V=f\gamma''{}^\top$ with $f\ge0$ smooth, positive near a point and zero at the
endpoints. Then

$$
0=-\int_a^b f\,|\gamma''{}^\top|^2\,dt,
$$

so $\gamma''{}^\top=0$ on $(a,b)$. Thus the geodesic equation is exactly the vanishing of the tangential
part of the acceleration.

**26.** **Strategy.** Write $S=G^{-1}II$ in the basis $\{X_u,X_v\}$ and take determinant and trace.

The first fundamental form has matrix
$G=\begin{pmatrix}E&F\\F&G\end{pmatrix}$ and the second has matrix
$II=\begin{pmatrix}\ell&m\\m&n\end{pmatrix}$. Since $II(v,w)=\langle Sv,w\rangle$,

$$
S=G^{-1}II
=\frac{1}{EG-F^2}
\begin{pmatrix}G&-F\\-F&E\end{pmatrix}
\begin{pmatrix}\ell&m\\m&n\end{pmatrix}.
$$

Therefore

$$
\det S=\det(G^{-1})\det(II)=\frac{\ell n-m^2}{EG-F^2}.
$$

For the trace, multiply the matrices:

$$
\operatorname{tr}(G^{-1}II)
=\frac{(G\ell-Fm)+(-Fm+En)}{EG-F^2}
=\frac{\ell G-2mF+nE}{EG-F^2}.
$$

Since $K=\det S$ and $H=\tfrac12\operatorname{tr}S$, the stated formulas follow.

**27.** **Strategy.** Compute the Christoffel symbols for $E=1$, then the single independent component of
the Riemann tensor, and compare with the derivative formula.

For an orthogonal chart with $E=1$, the general formulas give

$$
\Gamma^1_{11}=0,\quad \Gamma^1_{12}=0,\quad \Gamma^1_{22}=-\frac{G_u}{2},\quad
\Gamma^2_{11}=0,\quad \Gamma^2_{12}=\frac{G_u}{2G},\quad \Gamma^2_{22}=\frac{G_v}{2G}.
$$

With the convention $R^l{}_{ijk}=\partial_j\Gamma^l_{ik}-\partial_k\Gamma^l_{ij}+\Gamma^l_{jm}\Gamma^m_{ik}-\Gamma^l_{km}\Gamma^m_{ij}$, the component $R^1{}_{212}$ is

$$
R^1{}_{212}
=\partial_u\Gamma^1_{22}-\partial_v\Gamma^1_{21}
+\Gamma^1_{1m}\Gamma^m_{22}-\Gamma^1_{2m}\Gamma^m_{21}.
$$

The first term is $-G_{uu}/2$; the second vanishes because $\Gamma^1_{21}=0$. The first product
vanishes because $\Gamma^1_{11}=\Gamma^1_{12}=0$. The second product is

$$
\Gamma^1_{21}\Gamma^1_{21}+\Gamma^1_{22}\Gamma^2_{21}
=0+\left(-\frac{G_u}{2}\right)\left(\frac{G_u}{2G}\right)
=-\frac{G_u^2}{4G}.
$$

Hence

$$
R^1{}_{212}=-\frac{G_{uu}}{2}+\frac{G_u^2}{4G}.
$$

Since $E=1$ and $F=0$, $R_{1212}=E R^1{}_{212}=R^1{}_{212}$ and $EG-F^2=G$. Therefore

$$
K=\frac{R_{1212}}{EG-F^2}
=-\frac{G_{uu}}{2G}+\frac{G_u^2}{4G^2}.
$$

On the other hand,

$$
-\frac{1}{2\sqrt G}\frac{\partial}{\partial u}\left(\frac{G_u}{\sqrt G}\right)
=-\frac{1}{2\sqrt G}\left(\frac{G_{uu}}{\sqrt G}-\frac{G_u^2}{2G^{3/2}}\right)
=-\frac{G_{uu}}{2G}+\frac{G_u^2}{4G^2},
$$

which is the same expression. The right-hand side involves only $G$, hence only the metric; this proves
the Theorema Egregium in this normalisation.

**28.** **Strategy.** Use the invariance of $K$ under local isometries; for the cylinder, exhibit an
explicit unrolling map.

The sphere $S^2_R$ has $K=1/R^2$ everywhere, while the plane has $K=0$. A local isometry preserves the
first fundamental form and hence, by the Theorema Egregium, the Gaussian curvature. Since $1/R^2\ne0$,
no local isometry from an open subset of the sphere to the plane can exist.

For the cylinder, define $\Phi:\mathbb{R}^2\to S_R$ by

$$
\Phi(u,v)=(R\cos(u/R),R\sin(u/R),v).
$$

Then $\Phi_u=(-\sin(u/R),\cos(u/R),0)$ and $\Phi_v=(0,0,1)$ are orthonormal, so $\Phi$ is a local
isometry from the Euclidean plane to the cylinder. Equivalently, unrolling the cylinder onto the plane
preserves all lengths and angles. Both surfaces have $K=0$, as required.

**29.** **Strategy.** Apply Gauss–Bonnet to the geodesic triangle and use the hypothesis that $K$ is
constant.

Let $T$ be a geodesic triangle with interior angles $\alpha,\beta,\gamma$. Since the sides are
geodesics, $\kappa_g=0$ along the boundary. The boundary has three corners, and the turning angle at
each corner is $\pi-\alpha_i$. Gauss–Bonnet gives

$$
\int_T K\,dA+\sum_{i=1}^3(\pi-\alpha_i)=2\pi\chi(T).
$$

A triangle is a disc, so $\chi(T)=1$ and

$$
\int_T K\,dA+3\pi-(\alpha+\beta+\gamma)=2\pi,
\qquad
\int_T K\,dA=\alpha+\beta+\gamma-\pi.
$$

If $K$ is constant, $\int_T K\,dA=K\,\text{Area}$, so

$$
\text{Area}=\frac{\alpha+\beta+\gamma-\pi}{K}.
$$

For $K=0$ the equation gives $\alpha+\beta+\gamma=\pi$: geodesic triangles are Euclidean. For $K>0$
the angle sum exceeds $\pi$; for $K<0$ it is less.

**30.** **Strategy.** Use the orthonormal frame $e_\theta,e_\varphi$ along the latitude circle and solve
the parallel-transport ODE.

Let $\gamma(\varphi)=(\sin\theta\cos\varphi,\sin\theta\sin\varphi,\cos\theta)$ on the unit sphere, with
$0<\theta<\pi$, and set

$$
e_\theta=(\cos\theta\cos\varphi,\cos\theta\sin\varphi,-\sin\theta),\qquad
e_\varphi=(-\sin\varphi,\cos\varphi,0).
$$

The unit normal is $\nu=\gamma$. Direct differentiation gives

$$
\partial_\varphi e_\theta=\cos\theta\,e_\varphi,\qquad
\partial_\varphi e_\varphi=-\cos\theta\,e_\theta-\sin\theta\,\nu.
$$

Hence, for the surface covariant derivative,

$$
\nabla_{e_\varphi}e_\theta=\cos\theta\,e_\varphi,\qquad
\nabla_{e_\varphi}e_\varphi=-\cos\theta\,e_\theta.
$$

Write a tangent field along $\gamma$ as $Y=a e_\theta+b e_\varphi$. Since
$\gamma'=\sin\theta\,e_\varphi$,

$$
\nabla_{\gamma'}Y=\sin\theta\,\nabla_{e_\varphi}Y
=\sin\theta\bigl[(a'-b\cos\theta)e_\theta+(b'+a\cos\theta)e_\varphi\bigr].
$$

Thus $Y$ is parallel exactly when

$$
a'=b\cos\theta,\qquad b'=-a\cos\theta.
$$

Differentiating the first equation and substituting the second gives
$a''=-\cos^2\theta\,a$. With the initial condition $a(0)=1$, $b(0)=0$ (a unit vector in the
$e_\theta$ direction),

$$
a(\varphi)=\cos(\varphi\cos\theta),\qquad
b(\varphi)=-\sin(\varphi\cos\theta).
$$

After one full turn $\varphi=2\pi$,

$$
a(2\pi)=\cos(2\pi\cos\theta),\qquad
b(2\pi)=-\sin(2\pi\cos\theta),
$$

which is a rotation by angle $-2\pi\cos\theta$. Modulo $2\pi$ this is the angle
$2\pi(1-\cos\theta)$. Since $K=1$ on the unit sphere, the enclosed cap has area
$2\pi(1-\cos\theta)$, so the holonomy equals the integral of $K$ over the cap, as Gauss–Bonnet predicts.
For the equator $\theta=\pi/2$ the holonomy is $0$; for a small circle near the north pole it is the
small cap area.

**31.** **Strategy.** Decompose ambient derivatives into tangent and normal parts.

Let $X,Y,Z$ be tangent vector fields on $S$ and let $D$ be the Euclidean directional derivative. By
definition, $\nabla_XY=(D_XY)^\top$. Then

$$
X\langle Y,Z\rangle
=\langle D_XY,Z\rangle+\langle Y,D_XZ\rangle.
$$

Write $D_XY=\nabla_XY+\langle D_XY,\nu\rangle\nu$ and similarly for $D_XZ$. Since $Z$ and $Y$ are
tangent, the normal terms vanish in the inner products, so

$$
X\langle Y,Z\rangle
=\langle\nabla_XY,Z\rangle+\langle Y,\nabla_XZ\rangle,
$$

which is metric compatibility.

For torsion-freeness, note that the Euclidean derivative is torsion-free, so
$D_XY-D_YX=[X,Y]$. Projecting,

$$
\nabla_XY-\nabla_YX=(D_XY-D_YX)^\top=[X,Y]^\top.
$$

If $S$ is locally a level set $f^{-1}(a)$, then $Xf=Yf=0$, hence $[X,Y]f=0$, so $[X,Y]$ is tangent to
$S$. Therefore $[X,Y]^\top=[X,Y]$, and $\nabla$ is torsion-free.

**32.** **Strategy.** Apply the coordinate formula for the Lie bracket.

For $X=y\partial_x$ and $Y=x\partial_y$, and any smooth $f$,

$$
[X,Y]f
=X(Yf)-Y(Xf)
=y\partial_x(x\partial_yf)-x\partial_y(y\partial_xf).
$$

Now $\partial_x(x\partial_yf)=\partial_yf+x\partial_x\partial_yf$ and
$\partial_y(y\partial_xf)=\partial_xf+y\partial_y\partial_xf$. Hence

$$
[X,Y]f=y\partial_yf+xy\partial_x\partial_yf-x\partial_xf-xy\partial_y\partial_xf
=y\partial_yf-x\partial_xf,
$$

so $[X,Y]=y\partial_y-x\partial_x$. For the coordinate fields,
$[\partial_x,\partial_y]f=\partial_x\partial_yf-\partial_y\partial_xf=0$ by equality of mixed
partials. The Lie bracket measures the failure of the flows to commute: the flow of $X$ moves in the
$y$-direction with speed $y$, and the flow of $Y$ moves in the $x$-direction with speed $x$, so the
order of the two motions changes the result; for coordinate fields the flows are translations and
commute.

**33.** **Strategy.** Compute the exterior derivative and apply Stokes; check directly using the flux.

For $\omega=x\,dy\wedge dz+y\,dz\wedge dx+z\,dx\wedge dy$,

$$
d\omega=dx\wedge dy\wedge dz+dy\wedge dz\wedge dx+dz\wedge dx\wedge dy=3\,dx\wedge dy\wedge dz,
$$

since each cyclic permutation of $dx,dy,dz$ is positive. By Stokes' theorem on the unit ball $B^3$,

$$
\int_{S^2}\omega=\int_{B^3}d\omega
=3\operatorname{Vol}(B^3)=3\cdot\frac{4\pi}{3}=4\pi.
$$

Directly, $\omega$ is the flux $2$-form of $\mathbf F=(x,y,z)$. On the unit sphere the outward normal is
$\nu=(x,y,z)$ and $\mathbf F\cdot\nu=x^2+y^2+z^2=1$, so the flux is the area $4\pi$. The divergence
theorem gives the same answer because $\nabla\cdot\mathbf F=3$ and
$\iiint_{B^3}3\,dV=4\pi$.

**34.** **Strategy.** Apply Stokes to the $1$-form whose exterior derivative is the flux form of the curl.

Let $\omega=F_1dx+F_2dy+F_3dz$. Then

$$
d\omega=(\partial_yF_3-\partial_zF_2)\,dy\wedge dz
+(\partial_zF_1-\partial_xF_3)\,dz\wedge dx
+(\partial_xF_2-\partial_yF_1)\,dx\wedge dy.
$$

Let $r:U\to S$ be an orientation-preserving parametrisation of an oriented surface $S$ with boundary
$\partial S$. The pullback of $dy\wedge dz$ is
$\frac{\partial(y,z)}{\partial(u,v)}du\wedge dv$, and similarly for the other terms. Therefore

$$
r^*(d\omega)
=\left[(\partial_yF_3-\partial_zF_2)\frac{\partial(y,z)}{\partial(u,v)}
+(\partial_zF_1-\partial_xF_3)\frac{\partial(z,x)}{\partial(u,v)}
+(\partial_xF_2-\partial_yF_1)\frac{\partial(x,y)}{\partial(u,v)}\right]du\wedge dv.
$$

The bracket is exactly $(\nabla\times\mathbf F)\cdot(r_u\times r_v)$, so

$$
r^*(d\omega)=(\nabla\times\mathbf F)\cdot\nu\,dA,
$$

where $\nu$ is the unit normal of the parametrisation. On the boundary, $r^*\omega=\mathbf F\cdot dr$.
Stokes' theorem $\int_S d\omega=\int_{\partial S}\omega$ becomes

$$
\iint_S(\nabla\times\mathbf F)\cdot\nu\,dA=\oint_{\partial S}\mathbf F\cdot d\mathbf r,
$$

which is Kelvin–Stokes' theorem.

## Challenge

**35.** **Strategy.** Solve the Frenet–Serret linear ODE for an orthonormal frame, integrate its tangent,
and prove uniqueness by comparing two solutions.

Let $I$ be an interval, $s_0\in I$, and let $\kappa,\tau:I\to\mathbb{R}$ be continuous with
$\kappa>0$. Choose a right-handed orthonormal basis $(T_0,N_0,B_0)$ of $\mathbb{R}^3$ and consider the
linear initial-value problem

$$
F'(s)=A(s)F(s),\qquad F(s_0)=F_0,
$$

where $F=(T,N,B)$ is the matrix with columns $T,N,B$, $F_0$ has columns $T_0,N_0,B_0$, and

$$
A(s)=\begin{pmatrix}0&\kappa(s)&0\\-\kappa(s)&0&\tau(s)\\0&-\tau(s)&0\end{pmatrix}.
$$

The coefficients are continuous, so the standard existence and uniqueness theorem for linear ODE
systems gives a unique $C^1$ solution on all of $I$.

Because $A$ is skew-symmetric, the frame stays orthonormal:

$$
\frac{d}{ds}\langle F_i,F_j\rangle
=\langle AF_i,F_j\rangle+\langle F_i,AF_j\rangle
=\langle(A+A^{\mathsf T})F_i,F_j\rangle=0,
$$

and the initial frame is orthonormal. The determinant is continuous and takes values $\pm1$; since it
is $+1$ initially, it remains $+1$, so the frame stays right-handed.

Define

$$
\gamma(s)=\gamma_0+\int_{s_0}^sT(u)\,du.
$$

Then $\gamma'=T$, so $\gamma$ is unit-speed, and $\gamma''=T'=\kappa N$. Hence the curvature is
$|T'|=\kappa$ and the Frenet normal is $N$. Since the frame is right-handed, $B=T\times N$, and the
third Frenet equation $B'=-\tau N$ shows that the torsion is $\tau$. This proves existence.

For uniqueness, suppose $\tilde\gamma$ is another unit-speed curve with the same $\kappa,\tau$, and let
$\tilde F$ be its Frenet frame. Writing a frame as the matrix with columns $T,N,B$, the Frenet equations
are $F'=FA^{\mathsf T}$. Since both frames solve this same linear system,

$$
Q'=\tilde F'F^{-1}-\tilde F F^{-1}F'F^{-1}
=\tilde F A^{\mathsf T}F^{-1}-\tilde F A^{\mathsf T}F^{-1}=0.
$$

Thus $Q=\tilde FF^{-1}$ is constant. Then $\tilde F=QF$ with $Q$ a constant orthogonal matrix, and
$\tilde\gamma'=\tilde T=QT=Q\gamma'$. Hence $\tilde\gamma=Q\gamma+c$ for a constant vector $c$: the two
curves differ by a rigid motion.

**36.** **Strategy.** Compute the cone metric, identify it with polar coordinates in a sector, and read
geodesics and holonomy from the unrolling.

(a) For $X(\rho,\varphi)=(\rho\sin\alpha\cos\varphi,\rho\sin\alpha\sin\varphi,\rho\cos\alpha)$,

$$
X_\rho=(\sin\alpha\cos\varphi,\sin\alpha\sin\varphi,\cos\alpha),\qquad
X_\varphi=(-\rho\sin\alpha\sin\varphi,\rho\sin\alpha\cos\varphi,0).
$$

Thus $|X_\rho|=1$, $\langle X_\rho,X_\varphi\rangle=0$ and $|X_\varphi|=\rho\sin\alpha$, so

$$
I=d\rho^2+\rho^2\sin^2\alpha\,d\varphi^2.
$$

Put $\psi=\varphi\sin\alpha$. Then $I=d\rho^2+\rho^2d\psi^2$, the Euclidean metric in polar coordinates.
The map $(\rho,\psi)\mapsto(\rho\cos\psi,\rho\sin\psi)$ is a local isometry from the cone minus the
apex onto the plane sector $0\le\psi\le2\pi\sin\alpha$ with its radial edges identified. Geodesics on
the cone correspond to straight lines in this sector, because straight lines are the geodesics of the
plane and the correspondence preserves the metric.

(b) A straight line not through the apex crosses the two radial edges at equal radius exactly when the
sector angle $\beta=2\pi\sin\alpha$ is less than $\pi$: then the chord joining two points at equal
radius on the edges lies inside the sector and projects to a closed geodesic. If $\beta\ge\pi$, no such
chord joins the two edges at equal radius without passing through the apex. Hence a simple closed
geodesic avoiding the apex exists exactly when

$$
2\pi\sin\alpha<\pi
\quad\Longleftrightarrow\quad
\sin\alpha<\frac12
\quad\Longleftrightarrow\quad
\alpha<\frac{\pi}{6}.
$$

Geodesics through the apex are not smooth at the apex and are not considered here.

(c) The cone is flat away from the apex, but a loop around the apex has holonomy equal to the angle
defect

$$
2\pi-\beta=2\pi(1-\sin\alpha).
$$

This is the integrated curvature concentrated at the apex: Gauss–Bonnet applied to a cone with a
singular point assigns total curvature $2\pi-\beta$ to the apex. As $\alpha\to0$ the cone becomes sharp
and the holonomy tends to $2\pi$; as $\alpha\to\pi/2$ the cone flattens and the holonomy tends to $0$.

**37.** **Strategy.** Maximise the squared distance from a point not on the surface and show that the
second fundamental form is negative definite there.

Choose an origin $O$ not on $S$ and consider $f(p)=|p|^2$ on the compact surface $S$. It attains a
maximum at some $p\in S$, and $p\ne O$ because $O\notin S$. For any tangent vector $w\in T_pS$, choose
a curve $\alpha$ on $S$ with $\alpha(0)=p$ and $\alpha'(0)=w$. The function
$g(t)=|\alpha(t)|^2$ has a maximum at $t=0$, so $g'(0)=0$ and $g''(0)\le0$. Now

$$
g'(0)=2\langle p,w\rangle,\qquad
g''(0)=2|w|^2+2\langle p,\alpha''(0)\rangle.
$$

Thus $\langle p,w\rangle=0$ for every $w\in T_pS$: $p$ is normal to the tangent plane. Let
$\nu=p/|p|$ be the outward unit normal. Then

$$
II_p(w,w)=\langle\nu,\alpha''(0)\rangle
=\frac{1}{|p|}\langle p,\alpha''(0)\rangle
\le-\frac{|w|^2}{|p|}<0
$$

for every $w\ne0$. Hence $II_p$ is negative definite, so both principal curvatures are negative and
$K(p)=\kappa_1\kappa_2>0$. Therefore every compact regular surface in $\mathbb{R}^3$ has a point of
positive Gaussian curvature, and no compact surface in $\mathbb{R}^3$ can have $K\le0$ everywhere.

**38.** **Strategy.** Compare the pulled-back Euclidean metric with the sphere metric; conformality means
the two differ by a positive factor.

Let the sphere have radius $R$, with latitude $\varphi$ and longitude $\lambda$. Its first fundamental
form is

$$
ds^2_{\text{sphere}}=R^2\cos^2\varphi\,d\lambda^2+R^2d\varphi^2.
$$

Mercator's map is $x=R\lambda$, $y=R\ln\tan(\pi/4+\varphi/2)$. Then

$$
dx=R\,d\lambda,\qquad
dy=R\sec\varphi\,d\varphi,
$$

because $\frac{d}{d\varphi}\ln\tan(\pi/4+\varphi/2)=\sec\varphi$. Hence

$$
dx^2+dy^2=R^2d\lambda^2+R^2\sec^2\varphi\,d\varphi^2
=\sec^2\varphi\bigl(R^2\cos^2\varphi\,d\lambda^2+R^2d\varphi^2\bigr)
=\sec^2\varphi\,ds^2_{\text{sphere}}.
$$

The conformal factor is $\sec\varphi>0$ for $|\varphi|<\pi/2$, so the map preserves angles. It stretches
lengths by $\sec\varphi$ and areas by $\sec^2\varphi$, which tends to infinity at the poles. If a
conformal map also preserved area, its conformal factor would have to be $1$ everywhere, making it a
local isometry. By the Theorema Egregium, a local isometry would force the sphere's Gaussian curvature
$1/R^2$ to equal the plane's curvature $0$, a contradiction. Thus no conformal map of the whole sphere
to the plane can preserve area.

**39.** **Strategy.** Use the variational characterisation of geodesics, and test normal curvature on a
plane and a cylinder.

Let $\phi:S_1\to S_2$ be a local isometry and let $\gamma$ be a geodesic on $S_1$. Since $\phi$ preserves
the first fundamental form, it preserves the length and energy of every curve:
$L(\phi\circ\gamma)=L(\gamma)$ and $E(\phi\circ\gamma)=E(\gamma)$. Variations of $\gamma$ with fixed
endpoints correspond under the local diffeomorphism $\phi$ to variations of $\phi\circ\gamma$ with fixed
endpoints, and the derivative of the energy is preserved. Hence $\phi\circ\gamma$ is a critical point of
the energy on $S_2$, i.e. a geodesic. (If $\phi$ is only a local isometry, this is local in the domain.)

Normal curvature is **not** preserved in general, because it is extrinsic. A plane and a cylinder are
locally isometric, but on the plane every normal curvature is $0$, while on the cylinder the normal
curvature in the circumferential direction is $\pm1/R$ (depending on the normal). Thus a local isometry
preserves $K$ and geodesics, but not $II$, $\kappa_n$ or $H$.

**40.** **Strategy.** Apply the Cayley–Hamilton theorem to the shape operator.

The shape operator $S$ is a $2\times2$ linear map, so by Cayley–Hamilton

$$
S^2-(\operatorname{tr}S)S+(\det S)I=0.
$$

Since $\operatorname{tr}S=2H$ and $\det S=K$,

$$
S^2-2HS+KI=0.
$$

For any tangent vector $w$,

$$
0=\bigl\langle(S^2-2HS+KI)w,w\bigr\rangle
=\langle Sw,Sw\rangle-2H\langle Sw,w\rangle+K\langle w,w\rangle.
$$

By the definitions $I(w)=\langle w,w\rangle$, $II(w)=\langle Sw,w\rangle$ and
$III(w)=\langle Sw,Sw\rangle$, this is

$$
III(w)-2H\,II(w)+K\,I(w)=0
$$

for every $w$. Since both sides are quadratic forms in $w$, the identity
$III-2H\,II+K\,I=0$ holds as an identity of quadratic forms.
