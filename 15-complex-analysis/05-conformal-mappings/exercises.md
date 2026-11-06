# Conformal Mappings — Exercises

> [Tutorial](README.md) · 36 problems · Levels: Beginner, Intermediate, Advanced, Challenge

Attempt every problem on paper before consulting [solutions.md](solutions.md). You may use any result
proved in the [tutorial](README.md). State the domain on which a map is conformal before using it, and
check every constructed map on the boundary of the region.

## Beginner

**1.** Find $f'$ and the set of points where $f$ fails to be conformal: (a) $z^3-3z$; (b) $e^{z^2}$;
(c) $\sinh z$; (d) $\dfrac{z-1}{z+2}$.

**2.** Show that $z\mapsto\bar z$ preserves the magnitudes of angles but reverses their orientation.
Is it conformal in the sense of Definition 5.1?

**3.** Show that $f(z)=z+\dfrac1z$ is conformal on $\mathbb{C}\setminus\{0,1,-1\}$ and determine what
happens at $z=1$.

**4.** Find the image of the real axis under $T(z)=\dfrac{z-i}{z+i}$, and the image of the point $\infty$.

**5.** Find the Möbius transformation sending $0\mapsto1$, $1\mapsto0$, $\infty\mapsto\infty$.

**6.** Compute the cross-ratios $(0,2;1,3)$ and $(i,0;1,\infty)$.

**7.** Show that $0,1,2,1+i$ do not lie on a common circle or line by computing a cross-ratio.

**8.** Classify $T(z)=\dfrac{3z+2}{z+1}$ and find its fixed points.

**9.** Classify $T(z)=\dfrac1z$ and find its fixed points and multiplier.

**10.** Verify that $T(z)=\dfrac{z-i}{z+i}$ maps $\mathbb{H}$ onto $\mathbb{D}$ and sends $i\mapsto0$.

**11.** Find the image of the first quadrant and of the sector $0<\arg z<\pi/4$ under $z\mapsto z^2$.

**12.** Find the image of the strip $0<\operatorname{Im}z<\pi/2$ under $z\mapsto e^z$.

## Intermediate

**13.** Determine all conformal automorphisms of $\mathbb{D}$ that fix $0$, and prove your answer.

**14.** Construct a conformal map from $\mathbb{D}$ onto the right half-plane, and check it on the
boundary.

**15.** Construct a conformal map from the strip $0<\operatorname{Im}z<1$ onto $\mathbb{D}$.

**16.** Construct a conformal map from the wedge $0<\arg z<\pi/3$ onto $\mathbb{D}$.

**17.** Construct a conformal map from the half-disc $\{\lvert z\rvert<1,\operatorname{Im}z>0\}$ onto
$\mathbb{D}$.

**18.** Classify $T(z)=\dfrac{z+2}{z-1}$, and verify directly that $T$ is an involution.

**19.** Write the Schwarz–Christoffel integral for (a) a rectangle, (b) a triangle with angles
$\pi/2,\pi/6,\pi/3$, and check the exponent sum in each case.

**20.** Using the Poisson formula, show that constant boundary data $u\equiv c$ on the unit circle gives
the constant harmonic function $c$.

**21.** Solve the Dirichlet problem on the strip $0<\operatorname{Im}z<\pi$ with boundary values $0$ on
the lower edge and $1$ on the upper edge.

**22.** Construct a conformal map from $\mathbb{H}$ onto the strip $0<\operatorname{Im}w<1$.

**23.** Describe the image of $\lvert z\rvert>1$ and of $\lvert z\rvert=1$ under $w=z+\dfrac1z$.

## Advanced

**24.** Prove that a bijective holomorphic map has nonzero derivative at every point.

**25.** Prove that the cross-ratio is invariant under Möbius transformations by checking the three
generators of Theorem 7.5.

**26.** Prove the Schwarz–Pick inequality from the Schwarz lemma, and deduce that holomorphic self-maps of
$\mathbb{D}$ do not increase hyperbolic distance.

**27.** Prove that in the Schwarz–Christoffel integral the image of each interval $(x_k,x_{k+1})$ is a
straight segment and that the angle at $w_k$ is $\alpha_k\pi$.

**28.** Prove that on a simply connected domain every harmonic function is the real part of a holomorphic
function, and use this to prove Theorem 7.28.

**29.** Prove that the Poisson kernel is positive, integrates to $2\pi$, and converges to $0$ uniformly
away from $\varphi=0$ as $r\to1^{-}$.

**30.** Prove that there is no conformal map from $\mathbb{D}$ onto $\mathbb{C}$, and none from
$\mathbb{D}$ onto $\mathbb{D}\setminus\{0\}$.

**31.** Prove that a nonconstant holomorphic function is an open map, and deduce that conformal
equivalence preserves simple connectivity.

## Challenge

**32.** Exhibit an explicit conformal map from $\mathbb{C}\setminus(-\infty,0]$ onto $\mathbb{D}$ and
verify that it is a bijection.

**33.** Prove that if $r<R$ and $r'<R'$ and the annuli $r<\lvert z\rvert<R$ and $r'<\lvert z\rvert<R'$ are
conformally equivalent, then $R/r=R'/r'$. (Use the Dirichlet energy of $\log\lvert z\rvert$.)

**34.** Let $c>0$ and consider the Joukowski map $w=z+\dfrac{c^2}{z}$. Show that a circle through $z=c$
with centre off the real axis maps to a curve with a cusp at $w=2c$, and explain how the Kutta condition
fixes the circulation and hence the lift.

**35.** Let $T$ be loxodromic. Prove that $T$ has one attracting and one repelling fixed point, and that
the iterates $T^n(z)$ converge to the attracting fixed point for every $z$ not equal to the repelling one.

**36.** Show that the complex potential $\Phi(z)=U\left(z+\dfrac1z\right)$ on $\lvert z\rvert>1$,
transported by $w=z+\dfrac1z$, describes ideal flow past the flat plate $[-2,2]$ with speed $U$ at
infinity. Identify the streamlines, the stagnation points, and the behaviour of the velocity at the edges.
