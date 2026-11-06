# Analytic Functions — Exercises

> [Tutorial](README.md) · 36 problems · Levels: Beginner, Intermediate, Advanced, Challenge

Attempt every problem on paper before consulting [solutions.md](solutions.md). You may use any result
proved in the [tutorial](README.md). Where a derivative is requested "from the definition", do not use
the differentiation rules.

## Beginner

**1.** Use Definition 5.1 to differentiate $f(z) = 3z+2$ at $z_0 = 1+i$.

**2.** Using the differentiation rules, find $f'(z)$ for $f(z) = z^2-z$ and evaluate it at $z = 2-i$.

**3.** For $f(z) = z^2$, write $f = u+iv$ and verify the Cauchy–Riemann equations.

**4.** Determine all points at which $f(z) = \bar z^2$ is complex-differentiable, and find the derivative
at those points.

**5.** For $f(z) = e^z$, write $u = e^x\cos y$, $v = e^x\sin y$ and verify the Cauchy–Riemann equations.

**6.** For $f(z) = 1/z$, write $u$ and $v$ in terms of $x$ and $y$, verify the Cauchy–Riemann equations,
and show that $f'(z) = -1/z^2$.

**7.** Determine all points at which $f(z) = z\lvert z\rvert^2$ is complex-differentiable.

**8.** Determine whether $u(x,y) = x^2+y^2$ is harmonic.

**9.** Show that $u(x,y) = x^3-3xy^2$ is harmonic and find a harmonic conjugate $v$. Express $u+iv$ in
terms of $z$.

**10.** Compute the principal logarithms $\operatorname{Log}(1+i)$ and $\operatorname{Log}(-\sqrt3+i)$.

**11.** Compute $e^{i\pi/3}$, $e^{1+i\pi/2}$ and $e^{2\pi i}$.

**12.** Compute $\sin(i\ln 2)$ and $\cos(i\ln 2)$ exactly, and verify $\sin^2+\cos^2 = 1$ for these values.

## Intermediate

**13.** Show that $f(z) = x^2+iy^2$ satisfies the Cauchy–Riemann equations exactly on the line $x = y$,
and conclude that $f$ is differentiable exactly on that line but holomorphic nowhere.

**14.** Find every entire function of the form $f(z) = u(x)+iv(y)$ with $u,v$ real differentiable.

**15.** Show that $u = xy$ is harmonic, find its harmonic conjugate, and express $u+iv$ as a polynomial in
$z$.

**16.** Determine the image of the strip $0<\operatorname{Im}z<\pi$ under $z\mapsto e^z$, and the image of
the strip $0<\operatorname{Im}z<2\pi$.

**17.** Solve $e^z = 1+i$ for $z\in\mathbb{C}$.

**18.** Show that $\operatorname{Log}(zw) = \operatorname{Log}z+\operatorname{Log}w$ is false in general,
and state the correct relation.

**19.** Solve $\sin z = 2$ for $z\in\mathbb{C}$.

**20.** Prove that $\lvert\cos z\rvert^2 = \cos^2x+\sinh^2y$ and $\lvert\sin z\rvert^2 = \sin^2x+\sinh^2y$
for $z = x+iy$.

**21.** Show that $f(z) = e^z$ is conformal at $z_0 = i\pi/4$, stating the local scaling and rotation.
Describe the images of the horizontal line $y = \pi/4$ and the vertical line $x = 0$.

**22.** Find the radius of convergence of each series: $\sum z^n/n!$, $\sum n!\,z^n$, $\sum z^n/2^n$.

**23.** Find the power series of $1/(1-z)$ about $0$ and its radius of convergence; differentiate term by
term to obtain the series of $1/(1-z)^2$.

**24.** Show that $f(z) = (z-1)/(z+1)$ is conformal at $z = i$ and compute its derivative there.

## Advanced

**25.** Let $f$ be holomorphic on a domain $\Omega$ and suppose $f'(z)\in\mathbb{R}$ for every
$z\in\Omega$. Prove that $f(z) = az+b$ with $a\in\mathbb{R}$.

**26.** Let $f$ be holomorphic on a domain $\Omega$ and suppose $\lvert f\rvert$ is constant on $\Omega$.
Prove that $f$ is constant.

**27.** Let $f = u+iv$ be holomorphic with $f'(z)\ne0$ on a domain $\Omega$. Prove that the level curves
$u = \text{const}$ and $v = \text{const}$ meet orthogonally wherever they cross.

**28.** Let $u$ be harmonic on a domain $\Omega$ and suppose $u^2$ is also harmonic. Prove that $u$ is
constant.

**29.** Let $f(z) = u(r,\theta)+iv(r,\theta)$ be holomorphic, written in polar coordinates. Prove that
$f_\theta = irf_r$, where $f_r = u_r+iv_r$ and $f_\theta = u_\theta+iv_\theta$.

**30.** For $f(z) = \sum_{n\ge1}z^n/n^2$, prove that the radius of convergence is $1$, that the series
converges uniformly on the closed unit disc, and that the derivative series has radius $1$ but diverges
at $z = 1$.

**31.** Let $f$ be entire and suppose $f(1/n) = 0$ for every $n\in\mathbb{N}$. Prove that $f\equiv0$,
using the identity theorem stated in Remark 7.14.

## Challenge

**32.** Define $f(0) := 0$ and $f(z) := z^3/\bar z^2$ for $z\ne0$. Show that $f$ satisfies the
Cauchy–Riemann equations at $0$ but is not complex-differentiable there. Explain which hypothesis of
Theorem 7.7 fails.

**33.** Let $f$ be holomorphic near $z_0$ and suppose its Taylor expansion begins
$f(z)-f(z_0) = a_k(z-z_0)^k+O((z-z_0)^{k+1})$ with $a_k\ne0$ and $k\ge1$. Prove that $f$ multiplies
oriented angles at $z_0$ by $k$. Deduce that $f$ is conformal at $z_0$ exactly when $f'(z_0)\ne0$.

**34.** Prove that $\exp$ is injective on the open strip $S = \{z : \lvert\operatorname{Im}z\rvert<\pi\}$
and maps $S$ onto $\mathbb{C}\setminus(-\infty,0]$. Describe the images of vertical lines and horizontal
lines in $S$.

**35.** Prove that there is no continuous function $g:\mathbb{C}\setminus\{0\}\to\mathbb{C}$ with
$g(z)^2 = z$ for all $z\ne0$. Deduce that there is no holomorphic square-root branch on the punctured
plane.

**36.** Let $f$ be holomorphic on a domain $\Omega$ and suppose $f(\Omega)$ is contained in a straight
line. Prove that $f$ is constant.
