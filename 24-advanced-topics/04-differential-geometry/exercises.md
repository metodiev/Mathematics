# Differential Geometry — Exercises

> [Differential Geometry](README.md) · 40 problems · Beginner → Challenge · Solutions: [solutions.md](solutions.md)

Attempt every problem in writing before looking at [solutions.md](solutions.md). Section references
point into [README.md](README.md). Problems marked *(proof)* require a complete argument with all
hypotheses stated.

**Notation.** $\gamma$ is a regular curve; $T,N,B$ is its Frenet frame where $\kappa>0$; $s$ is arc
length. For a surface chart $X(u,v)$, $E=\langle X_u,X_u\rangle$, $F=\langle X_u,X_v\rangle$,
$G=\langle X_v,X_v\rangle$, and $\ell=\langle X_{uu},\nu\rangle$, $m=\langle X_{uv},\nu\rangle$,
$n=\langle X_{vv},\nu\rangle$ for a chosen unit normal $\nu$. The shape operator is $S_p=-d\nu_p$;
$K=\det S_p$ and $H=\tfrac12\operatorname{tr}S_p$. All surfaces are regular and oriented.

## Beginner

**1.** Compute the arc length of the helix $\gamma(t)=(2\cos t,2\sin t,3t)$ for $0\le t\le 4\pi$.

**2.** For the circle $\gamma(t)=(7\cos t,7\sin t,0)$, find the arc-length parameter, the unit-speed
parametrisation, the Frenet frame, the curvature and the torsion.

**3.** For the line $\gamma(t)=(1,2,3)+t(4,-1,2)$, compute the speed, the arc length for
$0\le t\le 3$, the curvature, and the unit tangent. Explain why the torsion is not defined.

**4.** For the ellipse $\gamma(t)=(\cos t,2\sin t,0)$, compute $\kappa(t)$ using
$\kappa=|\gamma'\times\gamma''|/|\gamma'|^3$, and evaluate it at $t=0$ and $t=\pi/2$.

**5.** Show that $X(u,v)=(u,v,u^2+v^2)$ is a regular surface chart and find the tangent plane at the
point $(1,1,2)$.

**6.** For the cylinder $X(u,v)=(R\cos u,R\sin u,v)$ with $R>0$, compute $E,F,G$. Find the area of the
band $0\le u\le 2\pi$, $0\le v\le h$, and the length of the circle $v=0$.

**7.** For the sphere
$X(\theta,\varphi)=(R\sin\theta\cos\varphi,R\sin\theta\sin\varphi,R\cos\theta)$, compute $E,F,G$ and
the area of the zone $\theta_1\le\theta\le\theta_2$. Deduce the total area.

**8.** For the cylinder of Problem 6 with outward normal, compute the normal curvature in the
circumferential direction and in the axial direction. Deduce the principal curvatures, $K$ and $H$.

**9.** Decide which of the following are regular charts, and where they fail:
(a) $X(u,v)=(u,v,u^2+v^2)$;
(b) $X(u,v)=(u^2,v^2,u+v)$;
(c) $X(u,v)=(\cos u,\sin u,v)$.

**10.** Let $h(x,y,z)=z$ be the height function on the sphere $S^2_R$. Compute $dh_p$ and find its
critical points on the sphere.

**11.** For the latitude circle $\theta=\theta_0$ on the unit sphere, compute its geodesic curvature
$\kappa_g$. Interpret the sign and the limiting cases.

**12.** State the total Gaussian curvature of the sphere $S^2_R$ and of the torus of revolution, and
verify each with the Gauss–Bonnet theorem.

## Intermediate

**13.** For the twisted cubic $\gamma(t)=(t,t^2,t^3)$, compute $\kappa$ and $\tau$ at $t=1$.

**14.** *(proof)* Let $\gamma$ be a unit-speed curve. Prove that $\kappa\equiv0$ if and only if
$\gamma$ is a straight line.

**15.** *(proof)* Prove that a curve with $\kappa>0$ lies in a plane if and only if $\tau\equiv0$.

**16.** For the surface of revolution
$X(u,v)=(f(v)\cos u,f(v)\sin u,h(v))$ with $f>0$, compute $E,F,G$ and state the condition for
regularity.

**17.** For a graph $z=f(x,y)$, derive the formula

$$
K=\frac{f_{xx}f_{yy}-f_{xy}^2}{(1+f_x^2+f_y^2)^2}.
$$

Apply it to $z=xy$ and to $z=x^2+2y^2$ at the origin.

**18.** *(proof)* Prove that the coordinate curves of a chart are orthogonal exactly when $F=0$.
Illustrate with the torus and with the chart $X(u,v)=(u,v,uv)$ at $(u,v)=(1,1)$.

**19.** Compute the area of the part of the paraboloid $z=x^2+y^2$ lying over the unit disk
$x^2+y^2\le 1$.

**20.** For the torus at $v=\pi/4$, compute the principal curvatures and the normal curvature in a
direction making angle $\pi/4$ with a principal direction. Verify Euler's theorem.

**21.** Solve the geodesic equations on the cylinder $X(u,v)=(R\cos u,R\sin u,v)$ and classify the
geodesics. Include vertical lines and horizontal circles as special cases.

**22.** *(proof)* Prove that every geodesic has constant speed, starting from the first variation of
the energy functional.

**23.** *(proof)* Derive Clairaut's relation $f(v)\cos\psi=\text{constant}$ for geodesics on a surface
of revolution, where $\psi$ is the angle with the parallel. Check it for the sphere and the cylinder.

**24.** Compute $\int_{T^2}K\,dA$ for the torus directly from the parametrisation of Section 7.8, and
explain the result using Gauss–Bonnet.

## Advanced

**25.** *(proof)* Derive the geodesic equation $\gamma''{}^\top=0$ from the first variation of the
energy. Show carefully that the boundary terms vanish and that the condition holds for every
admissible variation.

**26.** *(proof)* Derive
$K=(\ell n-m^2)/(EG-F^2)$ and $H=(\ell G-2mF+nE)/(2(EG-F^2))$ from the shape operator
$S_p=G^{-1}II$.

**27.** *(proof)* Suppose a surface has orthogonal coordinates with $E=1$. Using the Christoffel
symbols, derive

$$
K=-\frac{1}{2\sqrt G}\frac{\partial}{\partial u}\left(\frac{G_u}{\sqrt G}\right).
$$

Explain why this proves the Theorema Egregium in this case.

**28.** *(proof)* Prove that the sphere $S^2_R$ is not locally isometric to the plane, while the
cylinder is. Use the Theorema Egregium and, for the cylinder, an explicit local isometry.

**29.** *(proof)* For a geodesic triangle on a surface of constant Gaussian curvature $K$, prove that

$$
\text{Area}=\frac{\alpha+\beta+\gamma-\pi}{K}.
$$

What happens when $K=0$?

**30.** Parallel-transport a tangent vector once around the latitude circle $\theta=\theta_0$ on the
unit sphere. Solve the transport ODE and show that the resulting rotation is
$2\pi(1-\cos\theta_0)$ modulo $2\pi$. Relate this to Gauss–Bonnet.

**31.** *(proof)* For the covariant derivative $\nabla_XY=(D_XY)^\top$ on a surface, prove metric
compatibility and torsion-freeness.

**32.** On $\mathbb{R}^2$, compute $[X,Y]$ for $X=y\partial_x$ and $Y=x\partial_y$. Show that
$[\partial_x,\partial_y]=0$, and explain why the Lie bracket measures the non-commutativity of flows.

**33.** For $\omega=x\,dy\wedge dz+y\,dz\wedge dx+z\,dx\wedge dy$, compute $d\omega$ and evaluate
$\int_{S^2}\omega$, where $S^2$ is the unit sphere with outward orientation. Check the result with
the divergence theorem.

**34.** *(proof)* Derive Kelvin–Stokes' theorem from the generalised Stokes theorem by choosing
$\omega=F_1dx+F_2dy+F_3dz$ and integrating over a parametrised surface.

## Challenge

**35.** *(proof)* Prove the fundamental theorem of curves: given continuous functions $\kappa(s)>0$
and $\tau(s)$ on an interval, there is a unit-speed curve whose curvature and torsion are $\kappa$ and
$\tau$, and it is unique up to a rigid motion. State the ODE existence theorem you use.

**36.** A cone with half-angle $\alpha$ is parametrised by
$X(\rho,\varphi)=(\rho\sin\alpha\cos\varphi,\rho\sin\alpha\sin\varphi,\rho\cos\alpha)$.
(a) Show that the cone minus its apex is locally isometric to a plane sector, and describe its
geodesics. (b) Determine when a simple closed geodesic avoiding the apex exists. (c) Compute the holonomy of
parallel transport around the apex and explain it as an angle defect.

**37.** *(proof)* Prove that every compact regular surface in $\mathbb{R}^3$ has a point with
$K>0$. Deduce that no compact surface in $\mathbb{R}^3$ can have $K\le0$ everywhere.

**38.** For Mercator's projection of the sphere of radius $R$,
$x=R\lambda$, $y=R\ln\tan(\pi/4+\varphi/2)$, where $\lambda$ is longitude and $\varphi$ is latitude,
show that the map is conformal. Compute the area distortion factor and explain why no conformal map of
the whole sphere to the plane can preserve area.

**39.** *(proof)* Prove that a local isometry maps geodesics to geodesics. Does it preserve normal
curvature? Justify your answer.

**40.** *(proof)* For an oriented surface with shape operator $S$, define
$I(w)=\langle w,w\rangle$, $II(w)=\langle Sw,w\rangle$ and $III(w)=\langle Sw,Sw\rangle$. Prove the
identity

$$
III-2H\,II+K\,I=0.
$$
