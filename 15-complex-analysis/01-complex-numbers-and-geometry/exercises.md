# Complex Numbers and Geometry — Exercises

> [Tutorial](README.md) · 36 problems · Levels: Beginner, Intermediate, Advanced, Challenge

Attempt every problem on paper before consulting [solutions.md](solutions.md). You may use any result
proved in the [tutorial](README.md). Computations should be checked independently where a check is
available: substitution, comparison of moduli, or a special value.

## Beginner

**1.** Write $(3+4i)(1-2i)$ in Cartesian form.

**2.** Find the modulus and the principal argument of $z = -1+i\sqrt3$.

**3.** Express $z = 1-i$ in polar form and in exponential form.

**4.** Solve $z^2 = -16$ for $z \in \mathbb{C}$.

**5.** Compute $i^{2025}$ and $i^{2026}$.

**6.** For $z = 2+3i$, compute $\bar z$, $\lvert z\rvert^2$ and $1/z$.

**7.** Compute $(1+i)^8$ using polar form.

**8.** Find the real and imaginary parts of $(1+i)/(2-i)$.

**9.** For $z = 5-2i$, verify that $z+\bar z = 2\operatorname{Re}z$ and $z-\bar z = 2i\operatorname{Im}z$.

**10.** Describe geometrically the sets $\lvert z-(2+i)\rvert = 3$ and $\lvert z-(2+i)\rvert \le 3$.

**11.** Describe geometrically the set of $z$ with $\lvert z-1\rvert = \lvert z+1\rvert$.

**12.** List the cube roots of unity, verify that each cubes to $1$, and verify that their sum is $0$.

## Intermediate

**13.** For $z = 3+4i$ and $w = 5-12i$, compute $\lvert z+w\rvert$ and $\lvert z\rvert+\lvert w\rvert$, and
verify the triangle inequality in this case.

**14.** Prove from the Cartesian formula for multiplication that $\lvert zw\rvert = \lvert z\rvert\lvert w\rvert$
for all $z,w\in\mathbb{C}$, and deduce $\lvert z^n\rvert = \lvert z\rvert^n$ for $n\in\mathbb{N}$.

**15.** Two complex numbers satisfy $\lvert z\rvert = 3$, $\lvert w\rvert = 5$ and $\lvert z-w\rvert = 7$.
Find $\lvert z+w\rvert$.

**16.** Find all fourth roots of $-4$ in Cartesian form.

**17.** Solve $z^2+2z+5 = 0$.

**18.** Find all $z$ with $z^2 = 3+4i$ by writing $z = x+iy$.

**19.** Find the image of the line $y = x$ under the map $z\mapsto iz$, and describe the result geometrically.

**20.** Find the image of the unit circle $\lvert z\rvert = 1$ and of the real axis under $z\mapsto 1/z$.

**21.** Find the Möbius transformation with $T(0) = 1$, $T(1) = \infty$ and $T(\infty) = 0$.

**22.** Compute the cross-ratio $(1,-1;i,-i)$ and decide whether the four points are concyclic.

**23.** Find the stereographic projection of $z = 1+i$ and verify that the point lies on $S^2$.

**24.** Using Proposition 7.39, compute $d(0,\infty)$ and $d(1,-1)$.

## Advanced

**25.** Prove that for all $z,w\in\mathbb{C}$,
$$\lvert 1-z\bar w\rvert^2-\lvert z-w\rvert^2 = (1-\lvert z\rvert^2)(1-\lvert w\rvert^2).$$
Deduce that if $\lvert z\rvert<1$ and $\lvert w\rvert<1$, then $\left\lvert\dfrac{z-w}{1-\bar z w}\right\rvert<1$.

**26.** Prove that a Möbius transformation with real coefficients maps $\mathbb{R}_\infty$ onto itself.
Deduce that the cross-ratio of four distinct real points is real.

**27.** Let $C$ be the circle $\lvert z-c\rvert = r$ with $r>0$ and $\lvert c\rvert\ne r$ (so $C$ does not
pass through $0$). Show that its image under $z\mapsto 1/z$ is the circle with centre $\bar c/(\lvert c\rvert^2-r^2)$
and radius $r/\bigl\lvert\lvert c\rvert^2-r^2\bigr\rvert$.

**28.** Let $R_{a,\theta}(z) := a+e^{i\theta}(z-a)$ be rotation by $\theta$ about $a$. Prove that
$R_{b,\varphi}\circ R_{a,\theta}$ is a rotation by $\theta+\varphi$ about some point when
$e^{i(\theta+\varphi)}\ne1$, and a translation when $e^{i(\theta+\varphi)} = 1$. Find the centre in the
rotation case.

**29.** A **direct similarity** of the plane is a map $f:\mathbb{R}^2\to\mathbb{R}^2$ such that
$\lvert f(x)-f(y)\rvert = \lambda\lvert x-y\rvert$ for a fixed $\lambda>0$ and all $x,y$, and $f$ preserves
orientation. Prove that every direct similarity has the form $f(z) = az+b$ with $a\ne0$.

**30.** Prove that a non-identity Möbius transformation has at most two fixed points in
$\mathbb{C}_\infty$, and that a Möbius transformation with three distinct fixed points is the identity.

**31.** Prove that two ordered quadruples $(z_1,z_2,z_3,z_4)$ and $(w_1,w_2,w_3,w_4)$ of distinct points are
related by a Möbius transformation $T$ with $T(z_j) = w_j$ for all $j$ if and only if their cross-ratios are
equal.

## Challenge

**32.** Prove, using oriented angles and the inscribed-angle theorem rather than Theorem 7.27, that four
distinct points $z_1,z_2,z_3,z_4\in\mathbb{C}$ are concyclic or collinear if and only if
$(z_1,z_2;z_3,z_4)\in\mathbb{R}$.

**33.** Determine all Möbius transformations that map the open unit disc onto itself. Show that they are exactly
$$T(z) = e^{i\theta}\frac{z-a}{1-\bar a z}, \qquad \lvert a\rvert<1,\ \theta\in\mathbb{R}.$$

**34.** Prove that a Möbius transformation maps $\mathbb{R}_\infty$ onto itself if and only if it has real
coefficients up to a common factor, and that it maps the upper half-plane onto itself if and only if those
coefficients satisfy $ad-bc>0$.

**35.** Let $\Pi$ be the plane $\alpha X+\beta Y+\gamma Z = \delta$ in $\mathbb{R}^3$, meeting $S^2$ in a circle
that does not pass through the north pole (so $\gamma\ne\delta$). Show that the stereographic image of that circle
is the circle with centre $-(\alpha+i\beta)/(\gamma-\delta)$ and radius
$\sqrt{\alpha^2+\beta^2+\gamma^2-\delta^2}/\lvert\gamma-\delta\rvert$.

**36.** Prove that for every integer $n\ge2$,
$$\prod_{k=1}^{n-1}\sin\frac{k\pi}{n} = \frac{n}{2^{n-1}}.$$
