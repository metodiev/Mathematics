# Complex Integration — Solutions

> [Tutorial](README.md) · [Exercises](exercises.md) · 38 worked solutions

Each solution states the strategy, carries out every step, and ends with an independent check where one
is available. Alternative approaches are indicated where they are instructive.

## Beginner

**1.** *Strategy: use the definition, then compare with a primitive.* The segment is
$\gamma(t) = (1-i)+t(2+3i)$ for $0\le t\le1$, so $\gamma'(t) = 2+3i$ and $dz = (2+3i)dt$. Hence

$$\int_\gamma z\,dz = \int_0^1\Bigl[(1-i)+t(2+3i)\Bigr]\,(2+3i)\,dt = (1-i)(2+3i)+(2+3i)^2\int_0^1 t\,dt .$$

Now $(1-i)(2+3i) = 2+3i-2i-3i^2 = 5+i$ and $(2+3i)^2 = 4+12i+9i^2 = -5+12i$, so

$$\int_\gamma z\,dz = (5+i)+\tfrac12(-5+12i) = \tfrac52+7i .$$

**Check.** The primitive $F(z) = z^2/2$ gives $\bigl[(3+2i)^2-(1-i)^2\bigr]/2$. Here $(3+2i)^2 = 5+12i$ and $(1-i)^2 = -2i$, so the answer is $(5+14i)/2 = \tfrac52+7i$. $\checkmark$

**2.** *Strategy: a constant integrand.* The function $f(z) = 1$ has the primitive $F(z) = z$, so by Theorem 7.11,
$$\int_\gamma dz = \gamma(b)-\gamma(a) = (2-i)-0 = 2-i .$$
The answer is independent of the contour because $f\equiv1$ is entire and $\mathbb{C}$ is simply connected; equivalently, $\int_\gamma dz$ is the total displacement of the path, which depends only on its endpoints.

**Check.** Along the straight segment $\gamma(t) = t(2-i)$, $0\le t\le1$, the integral is $\int_0^1(2-i)dt = 2-i$. $\checkmark$

**3.** *Strategy: split and use Example 7.10.*
$$\oint_{\lvert z\rvert=2}\Bigl(z^3+\frac1z\Bigr)dz = \oint_{\lvert z\rvert=2}z^3\,dz+\oint_{\lvert z\rvert=2}\frac{dz}{z} = 0+2\pi i = 2\pi i .$$
The first integral vanishes because $z^3$ has the primitive $z^4/4$ (Theorem 7.11); the second is $2\pi i$ by Example 7.10 with $n=-1$.

**Check.** Parametrise $z = 2e^{i\theta}$: the first integrand contributes $16e^{4i\theta}\cdot2ie^{i\theta}$, whose integral over a period is $0$; the second contributes $i\,d\theta$, giving $2\pi i$. $\checkmark$

**4.** *Strategy: parametrise.* With $z = e^{i\theta}$ and $\bar z = e^{-i\theta}$, $dz = ie^{i\theta}d\theta$, so
$$\oint_{\lvert z\rvert=1}\bar z\,dz = \int_0^{2\pi}e^{-i\theta}\,ie^{i\theta}d\theta = i\int_0^{2\pi}d\theta = 2\pi i .$$
The integrand $\bar z = x-iy$ is not holomorphic: with $u = x$, $v = -y$ we get $u_x = 1$ and $v_y = -1$, so the Cauchy–Riemann equation $u_x = v_y$ fails everywhere. Hence Cauchy's theorem does not apply, and the integral may be — and is — nonzero.

**Check.** The answer is purely imaginary and has modulus $2\pi$, equal to the length of the circle, which is the largest value the ML inequality permits. $\checkmark$

**5.** (a) $\ell = 2\pi\cdot3 = 6\pi$.

(b) $\ell = \lvert -1-2i\rvert = \sqrt{1+4} = \sqrt5$.

(c) The path consists of the segment from $0$ to $1$, of length $1$, and the segment from $1$ to $1+i$, of length $1$. Total $\ell = 2$.

**Check (c).** The direct distance from $0$ to $1+i$ is $\sqrt2<2$, consistent with the triangle inequality: a broken path is longer than the straight one. $\checkmark$

**6.** *Strategy: primitive.* Since $z^2 = (z^3/3)'$, Theorem 7.11 gives
$$\int_\gamma z^2\,dz = \frac{1^3-i^3}{3} = \frac{1-(-i)}{3} = \frac{1+i}{3}.$$

**Check by parametrisation.** On the segment $z = i+t(1-i)$, $0\le t\le1$, with $dz = (1-i)dt$, the integrand is a cubic in $t$; the computation is longer but gives the same value. The modulus is $\sqrt2/3\approx0.471$, while the ML bound is $\max\lvert z^2\rvert\cdot\lvert 1-i\rvert = 1\cdot\sqrt2\approx1.414$, consistent. $\checkmark$

**7.** *Strategy: primitive.* The integrand $2z+3$ has the primitive $z^2+3z$, which is entire, so the path is irrelevant:
$$\int_\gamma(2z+3)\,dz = \bigl[z^2+3z\bigr]_{0}^{1+i} = (2i)+3(1+i) = 3+5i .$$

**Check.** On the parabola $z = t+it^2$, $0\le t\le1$, $dz = (1+2it)dt$; a direct expansion gives the same total. The endpoint formula is far shorter, which is the point of the exercise. $\checkmark$

**8.** *Strategy: integral formula versus Cauchy's theorem.* For the first integral the singularity $z=2$ is the centre of the circle and lies inside, so
$$\oint_{\lvert z-2\rvert=1}\frac{dz}{z-2} = 2\pi i .$$
For the second, the singularity $z=5$ is at distance $3$ from the centre, hence outside the closed disc $\lvert z-2\rvert\le1$. The integrand is holomorphic there, so by Theorem 7.16
$$\oint_{\lvert z-2\rvert=1}\frac{dz}{z-5} = 0 .$$
The shape of the integrand is identical; only the position of the singularity relative to the contour matters.

**Check.** With $z = 2+e^{i\theta}$ the first integral is $\int_0^{2\pi}i\,d\theta = 2\pi i$, and the second is $\int_0^{2\pi}ie^{i\theta}/(e^{i\theta}-3)d\theta$, whose integrand has the primitive $\log(e^{i\theta}-3)$ (the point $3$ lies outside the unit circle traced by $e^{i\theta}$), so the integral over a period vanishes. $\checkmark$

**9.** *Strategy: locate the singularities.* The integrand is $1/\bigl((z-1)(z+1)\bigr)$. The circle $\lvert z-1\rvert=1$ has centre $1$ and radius $1$: the pole $z=1$ is the centre (inside), while $z=-1$ is at distance $2$ (outside). The point $z=0$ lies on the contour, but it is not a singularity of the integrand, so it causes no difficulty. By the integral formula with $f(z) = 1/(z+1)$ and $z_0=1$,
$$\oint_{\lvert z-1\rvert=1}\frac{dz}{z^2-1} = 2\pi i\,f(1) = 2\pi i\cdot\frac{1}{1+1} = \pi i .$$

**Check.** Partial fractions give $\tfrac12\oint dz/(z-1)-\tfrac12\oint dz/(z+1)$; the first integral is $2\pi i$ and the second is $0$, so the total is $\pi i$. $\checkmark$

**10.** *Strategy: ML.* On $\lvert z\rvert=1$ we have $\lvert e^z\rvert = e^{\operatorname{Re}z}\le e^{1} = e$, and $\lvert z^2+3\rvert\ge3-\lvert z\rvert^2 = 2$. Since $\ell(\gamma) = 2\pi$,
$$\left\lvert\oint_{\lvert z\rvert=1}\frac{e^z}{z^2+3}\,dz\right\rvert\le e\cdot\frac12\cdot2\pi = \pi e\approx8.54 .$$
The maximum used is $M = e/2$, the product of the two bounds; strictly, $M = \max\lvert e^z/(z^2+3)\rvert\le e/2$.

**Check.** The integrand is holomorphic inside the circle (the zeros of $z^2+3$ are at $\pm i\sqrt3$, of modulus $1.732>1$), so the integral is actually $0$ by Cauchy's theorem. The bound is valid but far from sharp — a reminder that ML gives an inequality. $\checkmark$

**11.** *Strategy: split, using linearity.*
$$\oint_{\lvert z\rvert=1}\Bigl(2\bar z+\frac3z\Bigr)dz = 2\oint\bar z\,dz+3\oint\frac{dz}{z} = 2(2\pi i)+3(2\pi i) = 10\pi i ,$$
using Exercise 4 for the first integral and Example 7.10 for the second.

**Check.** Parametrising $z = e^{i\theta}$ gives $\int_0^{2\pi}(2e^{-i\theta}+3e^{-i\theta})ie^{i\theta}d\theta = 5i\int_0^{2\pi}d\theta = 10\pi i$. $\checkmark$

**12.** *Strategy: compute both and compare.* On $\gamma_1$, $z = t(1+i)$ and $\operatorname{Re}z = t$, $dz = (1+i)dt$:
$$\int_{\gamma_1}\operatorname{Re}z\,dz = (1+i)\int_0^1t\,dt = \frac{1+i}{2} .$$
On $\gamma_2$ the horizontal piece has $z=t$, $dz=dt$, $\operatorname{Re}z = t$ and contributes $\tfrac12$. The vertical piece has $z = 1+it$, $dz = i\,dt$, $\operatorname{Re}z = 1$ and contributes $i$. Hence
$$\int_{\gamma_2}\operatorname{Re}z\,dz = \frac12+i .$$
The values differ ($\tfrac12+\tfrac i2$ versus $\tfrac12+i$), so by Theorem 7.12 the function $\operatorname{Re}z$ has no primitive on $\mathbb{C}$. This is consistent with the Cauchy–Riemann equations: $u = x$, $v=0$ gives $u_x = 1\ne0 = v_y$.

**Check.** The difference between the two integrals is $\tfrac i2$, which equals $\int_{\gamma_2-\gamma_1}\operatorname{Re}z\,dz$ over the closed triangular contour; a nonzero value over a closed contour is exactly the failure of path independence. $\checkmark$

## Intermediate

**13.** *Strategy: integral formula with the singularity at $1$.* The function $f(z) = z^2+1$ is entire and $z_0=1$ lies inside $\lvert z\rvert=2$, so
$$\oint_{\lvert z\rvert=2}\frac{z^2+1}{z-1}\,dz = 2\pi i\,f(1) = 2\pi i\cdot2 = 4\pi i .$$

**Check by series.** Write $z = 1+w$: then $z^2+1 = 2+2w+w^2$, and $(z^2+1)/(z-1) = 2/w+2+w$. Only the $2/w$ term contributes to the integral around $w=0$, giving $2\pi i\cdot2 = 4\pi i$. $\checkmark$

**14.** *Strategy: integral formula with $f=\cos$.* The cosine is entire and $0$ is inside the unit circle:
$$\oint_{\lvert z\rvert=1}\frac{\cos z}{z}\,dz = 2\pi i\cos0 = 2\pi i .$$

**Check by series.** $\cos z/z = 1/z-z/2+\cdots$, and only the $1/z$ term contributes, giving $2\pi i$. $\checkmark$

**15.** *Strategy one: partial fractions.*
$$\frac{z+1}{z^2+4} = \frac{z}{z^2+4}+\frac{1}{z^2+4},\qquad \frac{z}{z^2+4} = \frac12\Bigl(\frac{1}{z-2i}+\frac{1}{z+2i}\Bigr),\qquad \frac{1}{z^2+4} = \frac{1}{4i}\Bigl(\frac{1}{z-2i}-\frac{1}{z+2i}\Bigr).$$
Both $\pm2i$ lie inside $\lvert z\rvert=3$. Each of $\oint dz/(z-2i)$ and $\oint dz/(z+2i)$ equals $2\pi i$, so
$$\oint\frac{z\,dz}{z^2+4} = \frac12(2\pi i+2\pi i) = 2\pi i,\qquad \oint\frac{dz}{z^2+4} = \frac{1}{4i}(2\pi i-2\pi i) = 0 .$$
The total is $2\pi i$.

*Strategy two: two applications of the integral formula.* For the pole at $2i$,
$$\frac{z+1}{z^2+4} = \frac{1}{z-2i}\cdot\frac{z+1}{z+2i}\quad\Longrightarrow\quad 2\pi i\left[\frac{z+1}{z+2i}\right]_{z=2i} = 2\pi i\cdot\frac{1+2i}{4i} = 2\pi i\cdot\frac{2-i}{4}.$$
For the pole at $-2i$,
$$\frac{z+1}{z^2+4} = \frac{1}{z+2i}\cdot\frac{z+1}{z-2i}\quad\Longrightarrow\quad 2\pi i\left[\frac{z+1}{z-2i}\right]_{z=-2i} = 2\pi i\cdot\frac{1-2i}{-4i} = 2\pi i\cdot\frac{2+i}{4}.$$
Adding, the bracket is $\dfrac{(2-i)+(2+i)}{4} = 1$, so the integral is $2\pi i$.

**Check.** The values $\dfrac{2-i}{4}$ and $\dfrac{2+i}{4}$ were obtained by rationalising: $\dfrac{1+2i}{4i}\cdot\dfrac{-i}{-i} = \dfrac{2-i}{4}$ and $\dfrac{1-2i}{-4i}\cdot\dfrac{i}{i} = \dfrac{2+i}{4}$. Their sum is $1$, consistent with the partial-fraction computation, and the ML bound on $\lvert z\rvert=3$ is at most $\dfrac{4}{5}\cdot6\pi\approx15.1$, which comfortably exceeds $\lvert2\pi i\rvert = 2\pi$. $\checkmark$

**16.** *Strategy: differentiation formula with $n=1$.* With $f(z) = e^z$ and $z_0=0$,
$$\oint_{\lvert z\rvert=1}\frac{e^z}{z^2}\,dz = \frac{2\pi i}{1!}f'(0) = 2\pi i .$$

**Check by series.** $e^z/z^2 = z^{-2}+z^{-1}+\tfrac12+\cdots$, and only $z^{-1}$ contributes: $2\pi i$. $\checkmark$

**17.** *Strategy: differentiation formula with $n=3$.* Here $f(z) = \sin z$, $z_0=0$, and $f'''(z) = -\cos z$, so $f'''(0) = -1$. Since $0$ is inside $\lvert z\rvert=2$,
$$\oint_{\lvert z\rvert=2}\frac{\sin z}{z^4}\,dz = \frac{2\pi i}{3!}f'''(0) = \frac{2\pi i}{6}\cdot(-1) = -\frac{\pi i}{3}.$$

**Check by series.** $\sin z/z^4 = \bigl(z-z^3/6+z^5/120-\cdots\bigr)/z^4 = z^{-3}-\tfrac16z^{-1}+\cdots$, so the integral is $2\pi i\cdot(-\tfrac16) = -\pi i/3$. $\checkmark$

**18.** *Strategy: partial fractions.* Since
$$\frac{1}{z^2-1} = \frac12\Bigl(\frac{1}{z-1}-\frac{1}{z+1}\Bigr),\qquad \frac{z}{z^2-1} = \frac12\Bigl(\frac{1}{z-1}+\frac{1}{z+1}\Bigr),$$
and both $\pm1$ lie inside $\lvert z\rvert=2$,
$$\oint\frac{dz}{z^2-1} = \frac12(2\pi i-2\pi i) = 0,\qquad \oint\frac{z\,dz}{z^2-1} = \frac12(2\pi i+2\pi i) = 2\pi i .$$

**Check.** The first integrand is odd under $z\mapsto-z$ while the contour is invariant, so its integral must vanish; the second is even, and its integral need not. The symmetry argument confirms the zero without computation. $\checkmark$

**19.** *Strategy: partial fractions and interpretation.*
$$\Omega'(z) = \frac{z}{z^2-1} = \frac12\Bigl(\frac{1}{z-1}+\frac{1}{z+1}\Bigr).$$
Both $1$ and $-1$ lie inside $\lvert z\rvert=2$, so
$$\oint_{\lvert z\rvert=2}\Omega'(z)\,dz = \frac12(2\pi i)+\frac12(2\pi i) = 2\pi i .$$
Each logarithmic singularity of $\Omega$ contributes $\tfrac12\cdot2\pi i = \pi i$: a vortex of strength $\tfrac12$ at $1$ and one of strength $\tfrac12$ at $-1$. The circulation is additive because circulation is the integral of a linear combination, and each term is a logarithm whose period is $2\pi i$ multiplied by its coefficient.

**Check.** By the residue theorem of [Power Series and Residues](../04-power-series-and-residues/README.md) the integral is $2\pi i$ times the sum of the coefficients $1$ at each pole, i.e. $2\pi i$. $\checkmark$

**20.** *Strategy: ML plus partial fractions.* On $\lvert z\rvert=R$ we have $\lvert z^2+1\rvert\ge R^2-1$ and $\lvert z\rvert = R$, so the integrand is bounded by $R/(R^2-1)$ and
$$\left\lvert\oint_{\gamma_R}\frac{z}{z^2+1}\,dz\right\rvert\le\frac{R}{R^2-1}\cdot2\pi R = \frac{2\pi R^2}{R^2-1}.$$
Exactly, partial fractions give
$$\oint_{\gamma_R}\frac{z\,dz}{z^2+1} = \frac12(2\pi i+2\pi i) = 2\pi i$$
for $R>1$. The bound tends to $2\pi$, which equals $\lvert2\pi i\rvert$, so the estimate is asymptotically sharp: as $R\to\infty$ the integrand behaves like $1/z$ on the circle, with modulus $1/R$ and length $2\pi R$.

**Check.** For $R=2$ the bound is $8\pi/3\approx8.38$ and the true modulus is $2\pi\approx6.28$, so the bound holds with about $33\%$ slack, consistent with sharpness in the limit. $\checkmark$

**21.** *Strategy: a primitive on a suitable branch.* The upper semicircle from $1$ to $-1$ lies in the slit plane $\mathbb{C}\setminus\{-it : t\ge0\}$ (the plane cut along the negative imaginary axis), on which the branch of the logarithm with arguments in $(-\pi/2,\,3\pi/2)$ is holomorphic with derivative $1/z$. On that branch $\operatorname{Log}(1) = 0$ and $\operatorname{Log}(-1) = i\pi$, so by Theorem 7.11
$$\int_\gamma\frac{dz}{z} = \operatorname{Log}(-1)-\operatorname{Log}(1) = i\pi .$$

**Check by parametrisation.** $\gamma(\theta) = e^{i\theta}$, $0\le\theta\le\pi$, gives $\int_0^\pi(i e^{i\theta}/e^{i\theta})d\theta = i\pi$. $\checkmark$

A remark on the branch: the principal logarithm is *not* holomorphic on the upper semicircle, because the endpoint $-1$ lies on the negative real axis, which is removed from its domain. The branch cut must be moved away from the path — here, into the lower half-plane. Choosing a branch is choosing a cut that the contour avoids; this is the first appearance of the theme of Section 11.

**22.** *Strategy: two applications of the integral formula.* Write
$$\frac{z+2}{z^2+1} = \frac{1}{z-i}\cdot\frac{z+2}{z+i} = \frac{1}{z+i}\cdot\frac{z+2}{z-i}.$$
Both poles $\pm i$ lie inside $\lvert z\rvert=3$. Applying Theorem 7.21 at each pole,
$$\oint_{\lvert z\rvert=3}\frac{z+2}{z^2+1}\,dz = 2\pi i\left[\frac{2+i}{2i}\right]+2\pi i\left[\frac{2-i}{-2i}\right] = 2\pi i\left[\frac{1-2i}{2}+\frac{1+2i}{2}\right] = 2\pi i .$$

**Check.** The brackets are $\dfrac{2+i}{2i}\cdot\dfrac{-i}{-i} = \dfrac{1-2i}{2}$ and $\dfrac{2-i}{-2i}\cdot\dfrac{i}{i} = \dfrac{1+2i}{2}$; their sum is $1$. Alternatively, partial fractions give $\dfrac{z+2}{z^2+1} = \dfrac{1}{2}\Bigl[\dfrac{2+i}{z-i}+\dfrac{2-i}{z+i}\Bigr]$ after matching coefficients, and the two coefficients sum to $1$ as well. The ML bound on $\lvert z\rvert=3$ is at most $\dfrac{5}{8}\cdot6\pi\approx11.8$, which exceeds $2\pi$. $\checkmark$

## Advanced

**23.** *Strategy: differentiate the constraint and use Cauchy–Riemann.* Write $f = u+iv$ and suppose $u^2+v^2 = c^2$ on $\Omega$. If $c=0$ then $f\equiv0$. Otherwise differentiating gives
$$uu_x+vv_x = 0,\qquad uu_y+vv_y = 0 .$$
Substituting $v_x = -u_y$ and $v_y = u_x$ from the Cauchy–Riemann equations,
$$uu_x-vu_y = 0,\qquad vu_x+uu_y = 0 .$$
This is the linear system
$$\begin{pmatrix}u & -v\\ v & u\end{pmatrix}\begin{pmatrix}u_x\\ u_y\end{pmatrix} = \begin{pmatrix}0\\0\end{pmatrix},$$
whose determinant is $u^2+v^2 = c^2\ne0$. Hence $u_x = u_y = 0$, and then $v_x = v_y = 0$. Therefore $f' = u_x+iv_x = 0$ on $\Omega$. A domain is path-connected (open and connected subsets of $\mathbb{R}^2$ are polygonally connected), so Theorem 7.11 applied along polygonal paths gives $f$ constant.

**Check.** An alternative proof: $\lvert f\rvert$ constant means $f(\Omega)$ lies on a circle; the open mapping theorem forbids this for non-constant $f$. The CR proof is elementary and does not need the open mapping theorem. $\checkmark$

**24.** *Strategy: reduce to the maximum principle.* Since $f$ never vanishes, $g := 1/f$ is holomorphic on $\Omega$. If $\lvert f\rvert$ has a local minimum at $z_0$, then $\lvert g\rvert = 1/\lvert f\rvert$ has a local maximum at $z_0$. By Theorem 7.34, $g$ is constant on $\Omega$, hence so is $f$.

**Check.** The hypothesis $f\ne0$ is essential: $f(z) = z$ on the unit disc has $\lvert f\rvert$ minimal at $0$, and $f$ is not constant; $1/f$ has a pole there, so the maximum principle does not apply. $\checkmark$

**25.** *Strategy: exponentiate to get boundedness.* Let $g := e^{f}$, which is entire. Then
$$\lvert g(z)\rvert = e^{\operatorname{Re}f(z)}\le e^{M}$$
for all $z$. By Liouville's theorem $g$ is constant, say $g\equiv c\ne0$. Then $f(z)\in\{\log\lvert c\rvert+i(\arg c+2\pi k) : k\in\mathbb{Z}\}$ for every $z$. The set on the right is discrete and $f$ is continuous on the connected set $\mathbb{C}$, so $f$ is constant.

**Check.** The conclusion fails without the one-sided bound: $f(z) = iz$ has $\operatorname{Re}f = -\operatorname{Im}z$, which is neither bounded above nor below, and $e^{iz}$ is not constant. $\checkmark$

**26.** *Strategy: invert.* If $\lvert f(z)\rvert\ge1$ everywhere, then $g = 1/f$ is entire and $\lvert g\rvert\le1$; by Liouville $g$ is constant, hence $f = 1/g$ is constant.

The hypothesis cannot be relaxed to "$\lvert f\rvert\ge c$ outside a compact set". Counterexample: $f(z) = z$ is entire and non-constant, and for every $c>0$ one has $\lvert f(z)\rvert\ge c$ whenever $\lvert z\rvert\ge c$. The compact set is the disc $\lvert z\rvert\le c$; inside it, $f$ has a zero. Thus a lower bound away from a compact set permits zeros, and zeros are exactly what force $f$ to be non-constant here.

**Check.** The proof of the first part uses boundedness of $1/f$ on all of $\mathbb{C}$, not merely outside a compact set, so nothing is lost in the argument; the second part shows the hypothesis is exactly what the proof uses. $\checkmark$

**27.** *Strategy: multiply by $(z-z_0)^2$ and use Morera.* Let $r>0$ be such that $\overline{D}(z_0,r)\subset\Omega$ and $\lvert f\rvert\le M$ on $D(z_0,r)\setminus\{z_0\}$. Define
$$g(z) := \begin{cases}(z-z_0)^2f(z), & z\ne z_0,\\ 0, & z = z_0 .\end{cases}$$
Then $g$ is continuous on $D(z_0,r)$, because $\lvert g(z)\rvert\le M\lvert z-z_0\rvert^2\to0 = g(z_0)$, and holomorphic off $z_0$. For a triangle $T\subset D(z_0,r)$: if $z_0\notin T$ then $\oint_{\partial T}g = 0$ by Goursat; if $z_0\in T$, cut $T$ into finitely many triangles avoiding $z_0$ plus a small triangle $T_\varepsilon$ containing $z_0$ of perimeter $<\varepsilon$. The integral over $T$ equals the integral over $T_\varepsilon$, bounded by $\max_{T_\varepsilon}\lvert g\rvert\cdot\varepsilon\le M\varepsilon^3\to0$. Hence $\oint_{\partial T}g = 0$ for all triangles, and Morera's theorem makes $g$ holomorphic on $D(z_0,r)$.

Since $g(z_0) = 0$ and $g'(z_0) = \lim_{z\to z_0}(z-z_0)f(z) = 0$, the power series of $g$ at $z_0$ starts with a term of order at least $2$: $g(z) = (z-z_0)^2h(z)$ with $h$ holomorphic on $D(z_0,r)$ (divide the series by $(z-z_0)^2$). On the punctured disc, $f(z) = g(z)/(z-z_0)^2 = h(z)$. Defining $f(z_0) := h(z_0)$ gives the required holomorphic extension.

**Check.** For $f(z) = \sin z/z$ at $z_0=0$ the extension is $\sin z/z\to1$; for $f(z) = 1/z$ the hypothesis fails because $f$ is unbounded near $0$, and indeed no extension exists. $\checkmark$

**28.** *Strategy: iterated Schwarz.* By Theorem 7.25, $f$ has a power series $f(z) = a_0+a_1z+a_2z^2+\cdots$ on the unit disc. The conditions $f(0)=0$ and $f'(0)=0$ give $a_0=a_1=0$, so $f(z) = z^2g(z)$ with $g$ holomorphic on the disc. For $0<r<1$ and $\lvert z\rvert=r$,
$$\lvert g(z)\rvert = \frac{\lvert f(z)\rvert}{r^2}\le\frac{1}{r^2}.$$
By the maximum principle (Corollary 7.35) the same bound holds on $\lvert z\rvert\le r$, so $\lvert f(z)\rvert\le\lvert z\rvert^2/r^2$. Letting $r\to1$ gives $\lvert f(z)\rvert\le\lvert z\rvert^2$.

**Check.** The function $f(z) = z^2$ attains the bound, so the constant $1$ is optimal. $\checkmark$

**29.** *Strategy: factor out $z^n$ and apply the maximum principle.* By Theorem 7.25, $f(z) = z^ng(z)$ with $g$ holomorphic on $D(0,R)$, because the first $n$ Taylor coefficients vanish. For $0<r<R$ and $\lvert z\rvert = r$,
$$\lvert g(z)\rvert = \frac{\lvert f(z)\rvert}{r^n}\le\frac{M}{r^n}.$$
The maximum principle gives $\lvert g(z)\rvert\le M/r^n$ on $\lvert z\rvert\le r$, hence $\lvert f(z)\rvert\le M(\lvert z\rvert/r)^n$. Letting $r\uparrow R$ gives the stated inequality.

**Check.** For $f(z) = z^n$ and $M = R^n$ the bound reads $\lvert z\rvert^n\le R^n(\lvert z\rvert/R)^n = \lvert z\rvert^n$, an equality; the estimate is sharp. $\checkmark$

**30.** *Strategy: integrate the derivative.* Let $a,b\in\Omega$. Since $\Omega$ is open and connected, it is polygonally connected: there is a polygonal path $\gamma$ in $\Omega$ from $a$ to $b$. Then, by Theorem 7.11 applied to the primitive $f$ of $f'$,
$$f(b)-f(a) = \int_\gamma f'(z)\,dz = 0 .$$
Hence $f(a) = f(b)$ for all $a,b$, and $f$ is constant. Connectedness is used twice: to guarantee that a path exists inside $\Omega$, and to conclude that equal values at two points propagate everywhere. On a disconnected open set the conclusion fails: the function equal to $0$ on $D(0,1)$ and to $1$ on $D(3,1)$ is holomorphic with zero derivative but not constant.

**Check.** The same argument shows that a holomorphic function with $f'\equiv0$ on a domain is constant, which is the uniqueness half of the fundamental theorem of calculus in the complex setting. $\checkmark$

## Challenge

**31.** *Strategy: close in the upper half-plane and split by partial fractions.* Let $\Gamma_R$ be the boundary of the upper half-disc of radius $R>2$, and
$$f(z) = \frac{1}{(z^2+1)(z^2+4)} = \frac13\left(\frac{1}{z^2+1}-\frac{1}{z^2+4}\right).$$
Both poles $\pm i$ and $\pm2i$ lie inside $\Gamma_R$. By the integral formula, with the factor $1/(z+i)$ evaluated at $i$ and $1/(z+2i)$ evaluated at $2i$,
$$\oint_{\Gamma_R}\frac{dz}{z^2+1} = 2\pi i\cdot\frac{1}{2i} = \pi,\qquad \oint_{\Gamma_R}\frac{dz}{z^2+4} = 2\pi i\cdot\frac{1}{4i} = \frac{\pi}{2}.$$
Hence $\oint_{\Gamma_R}f\,dz = \tfrac13\bigl(\pi-\tfrac\pi2\bigr) = \tfrac{\pi}{6}$. On $C_R$ we have $\lvert f\rvert\le1/\bigl((R^2-1)(R^2-4)\bigr)$ and $\ell(C_R) = \pi R$, so the arc contributes at most $\pi R/\bigl((R^2-1)(R^2-4)\bigr)\to0$. Therefore
$$\int_{-\infty}^{\infty}\frac{dx}{(x^2+1)(x^2+4)} = \frac{\pi}{6},\qquad \int_0^\infty\frac{dx}{(x^2+1)(x^2+4)} = \frac{\pi}{12},$$
the last step by evenness.

**Check.** Elementary partial fractions give $\dfrac{1}{(x^2+1)(x^2+4)} = \dfrac13\Bigl(\dfrac{1}{x^2+1}-\dfrac{1}{x^2+4}\Bigr)$, and
$$\int_0^\infty = \frac13\left(\frac{\pi}{2}-\frac{\pi}{4}\right) = \frac{\pi}{12}\approx0.2618 .$$
A numerical quadrature gives $0.261799\ldots$, in agreement. $\checkmark$

**32.** *Strategy: the substitution $z = e^{i\theta}$.* With $\cos\theta = \tfrac12(z+z^{-1})$ and $d\theta = dz/(iz)$,
$$5+4\cos\theta = 5+2(z+z^{-1}) = \frac{2z^2+5z+2}{z},$$
so
$$I = \oint_{\lvert z\rvert=1}\frac{dz}{iz}\cdot\frac{z}{2z^2+5z+2} = \frac1i\oint_{\lvert z\rvert=1}\frac{dz}{2z^2+5z+2}.$$
The denominator factors as $2z^2+5z+2 = 2(z+\tfrac12)(z+2)$, so the only pole inside the unit circle is $z=-\tfrac12$. With $g(z) = 1/\bigl(2(z+2)\bigr)$,
$$I = \frac1i\cdot2\pi i\,g\bigl(-\tfrac12\bigr) = 2\pi\cdot\frac{1}{2\cdot\tfrac32} = \frac{2\pi}{3}.$$

**Check.** The general formula $\int_0^{2\pi}d\theta/(a+b\cos\theta) = 2\pi/\sqrt{a^2-b^2}$ for $a>\lvert b\rvert$ gives $2\pi/\sqrt{25-16} = 2\pi/3\approx2.094$, and a numerical quadrature agrees. $\checkmark$

**33.** *Strategy: reduce to two integrals over a period.* Since $\cos^2\theta = \tfrac12(1+\cos2\theta)$,
$$\int_0^{2\pi}\frac{\cos^2\theta}{5+4\cos\theta}\,d\theta = \frac12\left(I_0+I_2\right),\qquad I_0 = \int_0^{2\pi}\frac{d\theta}{5+4\cos\theta},\quad I_2 = \int_0^{2\pi}\frac{\cos2\theta}{5+4\cos\theta}\,d\theta .$$
Exercise 32 gives $I_0 = 2\pi/3$. For $I_2$, use $\cos2\theta = \tfrac12(z^2+z^{-2})$ and $d\theta = dz/(iz)$ with $2z^2+5z+2 = 2(z+\tfrac12)(z+2)$:
$$I_2 = \oint_{\lvert z\rvert=1}\frac{z^2+z^{-2}}{2}\cdot\frac{dz}{iz\cdot\frac{2z^2+5z+2}{z}} = \oint_{\lvert z\rvert=1}\frac{z^4+1}{2i\,z^2\,(2z^2+5z+2)}\,dz .$$
The integrand has a double pole at $z=0$ and a simple pole at $z=-\tfrac12$ inside the circle (the pole at $-2$ is outside). Write the integrand as $G(z)/z^2$ with $G(z) = (z^4+1)/\bigl(2i(2z^2+5z+2)\bigr)$, holomorphic near $0$; the differentiation formula contributes $2\pi i\,G'(0)$, and the simple pole contributes $2\pi i\,\operatorname{Res}$.

Compute $G'(0)$. With $N = z^4+1$ and $D = 2i(2z^2+5z+2)$: $N(0)=1$, $N'(0)=0$, $D(0) = 4i$, $D'(0) = 10i$, so
$$G'(0) = \frac{N'(0)D(0)-N(0)D'(0)}{D(0)^2} = \frac{0-10i}{(4i)^2} = \frac{-10i}{-16} = \frac{5i}{8}.$$
For the simple pole, write $2z^2+5z+2 = 2(z+\tfrac12)(z+2)$ and evaluate at $z=-\tfrac12$:
$$\operatorname{Res} = \frac{z^4+1}{2i\,z^2\cdot2(z+2)}\Bigg\rvert_{z=-1/2} = \frac{1+\tfrac1{16}}{4i\cdot\tfrac14\cdot\tfrac32} = \frac{\tfrac{17}{16}}{\tfrac{3i}{2}} = -\frac{17i}{24}.$$
Hence
$$I_2 = 2\pi i\left(\frac{5i}{8}-\frac{17i}{24}\right) = 2\pi i\cdot\frac{15i-17i}{24} = 2\pi i\cdot\left(-\frac{i}{12}\right) = \frac{\pi}{6}.$$
Therefore
$$\int_0^{2\pi}\frac{\cos^2\theta}{5+4\cos\theta}\,d\theta = \frac12\left(\frac{2\pi}{3}+\frac{\pi}{6}\right) = \frac12\cdot\frac{5\pi}{6} = \frac{5\pi}{12}.$$

**Check.** Numerically $5\pi/12\approx1.3090$, and a quadrature gives $1.308997\ldots$. As a sanity bound, $\cos^2\theta/(5+4\cos\theta)\le1/(1) $ and the average of $\cos^2$ is $\tfrac12$, so a value near $1.3$ is reasonable. $\checkmark$

**34.** *Strategy: insert $e^{2iz}$ and close upwards.* Let $f(z) = e^{2iz}/(1+z^2)$ and let $\Gamma_R$ be the boundary of the upper half-disc. The only pole inside is $z=i$, and
$$\oint_{\Gamma_R}\frac{e^{2iz}}{1+z^2}\,dz = 2\pi i\cdot\frac{e^{2i\cdot i}}{2i} = \pi e^{-2}.$$
On $C_R$, $\lvert e^{2iz}\rvert = e^{-2\operatorname{Im}z}\le1$ and $\lvert 1+z^2\rvert\ge R^2-1$, so the arc contributes at most $\pi R/(R^2-1)\to0$. Hence
$$\int_{-\infty}^{\infty}\frac{e^{2ix}}{1+x^2}\,dx = \pi e^{-2},$$
and taking real parts gives the stated result.

**Check.** For $a=0$ the formula would give $\pi$, which is Exercise 7.39; the value $\pi e^{-2}\approx0.4252$ is what a numerical quadrature produces ($0.424998$ with a coarse rule, improving on refinement). The integrand is even, so $\int_0^\infty$ is half, $\approx0.2126$. $\checkmark$

**35.** *Strategy: close upwards, but estimate with the oscillation, not with ML alone.* Let $f(z) = ze^{iz}/(z^2+1)$ and let $\Gamma_R$ be the upper half-disc boundary. The only pole inside is $z=i$, and since $z^2+1 = (z-i)(z+i)$,
$$\oint_{\Gamma_R}\frac{ze^{iz}}{z^2+1}\,dz = 2\pi i\cdot\frac{ie^{i\cdot i}}{2i} = \frac{\pi i}{e}.$$
Hence $\int_{-R}^{R}xe^{ix}/(x^2+1)\,dx = \pi i/e - \int_{C_R}f\,dz$. The naive ML bound on the arc is
$$\max_{C_R}\lvert f\rvert\cdot\pi R\le\frac{R}{R^2-1}\cdot\pi R = \frac{\pi R^2}{R^2-1}\longrightarrow\pi\ne0,$$
which proves nothing. Use instead $\lvert e^{iz}\rvert = e^{-R\sin\theta}$ and $\lvert dz\rvert = R\,d\theta$:
$$\left\lvert\int_{C_R}f\,dz\right\rvert\le\frac{R^2}{R^2-1}\int_0^{\pi}e^{-R\sin\theta}\,d\theta\le\frac{R^2}{R^2-1}\cdot\frac{\pi}{R} = \frac{\pi R}{R^2-1}\longrightarrow0,$$
where the middle inequality uses $\sin\theta\ge2\theta/\pi$ on $[0,\pi/2]$ and the symmetry of $\sin$ about $\pi/2$. Therefore
$$\int_{-\infty}^{\infty}\frac{xe^{ix}}{x^2+1}\,dx = \frac{\pi i}{e}.$$
The real part is $\int x\cos x/(x^2+1)\,dx = 0$, as it must be by oddness; the imaginary part is $\int x\sin x/(x^2+1)\,dx = \pi/e$, and by evenness
$$\int_0^\infty\frac{x\sin x}{x^2+1}\,dx = \frac{\pi}{2e}.$$

**Check.** $\pi/(2e)\approx0.5779$. The integrand is positive on $(0,\pi)$, negative on $(\pi,2\pi)$, and decays like $(\sin x)/x$; a damped quadrature with $e^{-\varepsilon x}$ and $\varepsilon\downarrow0$ converges to $0.5755$ over $[0,200]$, the remaining tail contributing about $0.0024$, for a total of $0.5779$. $\checkmark$

**36.** *Strategy: shift the contour by a rectangle.* Let $R>0$ and let $\gamma$ be the rectangle with vertices $-R$, $R$, $R+ia$, $-R+ia$, traversed counterclockwise. The function $e^{-z^2}$ is entire, so $\oint_\gamma e^{-z^2}dz = 0$ by Cauchy's theorem.

*Vertical sides.* On $z = \pm R+iy$ with $0\le y\le a$, $\lvert e^{-z^2}\rvert = e^{-R^2+y^2}\le e^{-R^2+a^2}$, and the length is $a$, so each vertical side contributes at most $a\,e^{-R^2+a^2}\to0$.

*Horizontal sides.* The bottom gives $\int_{-R}^{R}e^{-x^2}dx$; the top, traversed from right to left, gives $-\int_{-R}^{R}e^{-(x+ia)^2}dx$. Hence, in the limit,
$$\int_{-\infty}^{\infty}e^{-(x+ia)^2}dx = \int_{-\infty}^{\infty}e^{-x^2}dx = \sqrt{\pi}.$$
Now $-(x+ia)^2 = -x^2-2iax+a^2$, so $e^{-(x+ia)^2} = e^{a^2}e^{-x^2}e^{-2iax}$ and therefore
$$\int_{-\infty}^{\infty}e^{-x^2}e^{-2iax}\,dx = \sqrt{\pi}\,e^{-a^2}.$$
Taking real parts,
$$\int_{-\infty}^{\infty}e^{-x^2}\cos(2ax)\,dx = \sqrt{\pi}\,e^{-a^2}.$$

**Check.** For $a=0$ this is the Gaussian integral $\sqrt\pi$. Differentiating the identity with respect to $a$ at $a=0$ gives $0 = 0$ by oddness; differentiating twice gives $-4\int x^2e^{-x^2}dx = 2\sqrt\pi$, i.e. $\int x^2e^{-x^2}dx = \sqrt\pi/2$, which is the known value. $\checkmark$

**37.** *Strategy: a keyhole contour and a branch of the power.* For $0<a<1$ define $f(z) = z^{a-1}/(1+z)$ using the branch
$$z^{a-1} = e^{(a-1)(\ln\lvert z\rvert+i\arg z)},\qquad 0<\arg z<2\pi,$$
which is holomorphic on $\mathbb{C}$ slit along the positive real axis, and satisfies $z^{a-1} = \lvert z\rvert^{a-1}$ on the upper side of the slit and $z^{a-1} = \lvert z\rvert^{a-1}e^{2\pi i(a-1)}$ on the lower side.

Let $\gamma$ be the keyhole contour: the segment from $\varepsilon$ to $R$ just above the positive axis, a counterclockwise circle of radius $R$, the segment from $R$ back to $\varepsilon$ just below the axis, and a clockwise circle of radius $\varepsilon$. The only singularity of $f$ enclosed is $z=-1 = e^{i\pi}$, and near it $f(z) = z^{a-1}/(z+1)$ with $z^{a-1}$ holomorphic and equal to $e^{i\pi(a-1)}$ at $-1$. By the integral formula,
$$\oint_\gamma f\,dz = 2\pi i\,e^{i\pi(a-1)} .$$

*The two segments.* On the upper side the integral is $\int_\varepsilon^R x^{a-1}/(1+x)\,dx$; on the lower side (traversed from $R$ to $\varepsilon$) it is $-e^{2\pi i(a-1)}\int_\varepsilon^R x^{a-1}/(1+x)\,dx$. Together they give $\bigl(1-e^{2\pi i(a-1)}\bigr)J_{\varepsilon,R}$, where $J_{\varepsilon,R} := \int_\varepsilon^R x^{a-1}/(1+x)dx$.

*The circles.* On $\lvert z\rvert=\varepsilon$, $\lvert z^{a-1}\rvert = \varepsilon^{a-1}$ and $\lvert 1+z\rvert\ge1-\varepsilon$, so the integral is at most $2\pi\varepsilon^a/(1-\varepsilon)\to0$ because $a>0$. On $\lvert z\rvert=R$, $\lvert z^{a-1}\rvert = R^{a-1}$ and $\lvert 1+z\rvert\ge R-1$, so the integral is at most $2\pi R^a/(R-1)\to0$ because $a<1$.

Letting $\varepsilon\to0$ and $R\to\infty$,
$$\bigl(1-e^{2\pi i(a-1)}\bigr)\int_0^\infty\frac{x^{a-1}}{1+x}\,dx = 2\pi i\,e^{i\pi(a-1)} .$$
Put $\theta := \pi(a-1)$, so that $1-e^{2i\theta} = e^{i\theta}(e^{-i\theta}-e^{i\theta}) = -2i\,e^{i\theta}\sin\theta$. Then
$$\int_0^\infty\frac{x^{a-1}}{1+x}\,dx = \frac{2\pi i\,e^{i\theta}}{-2i\,e^{i\theta}\sin\theta} = -\frac{\pi}{\sin\theta} = -\frac{\pi}{\sin(\pi(a-1))} = \frac{\pi}{\sin(\pi a)},$$
because $\sin(\pi(a-1)) = -\sin(\pi a)$.

**Check.** For $a=\tfrac12$ the formula gives $\pi/\sin(\pi/2) = \pi$. Independently, substituting $x = t^2$ gives
$$\int_0^\infty\frac{x^{-1/2}}{1+x}\,dx = \int_0^\infty\frac{2\,dt}{1+t^2} = 2\cdot\frac{\pi}{2} = \pi .$$
For $a\to0^+$ and $a\to1^-$ the formula diverges, reflecting the divergence of the integral at $0$ and at $\infty$ respectively — the two ends of the range $0<a<1$ are exactly where the two circle estimates fail. $\checkmark$

**38.** *Strategy: a sector of angle $\pi/4$, with no singularities at all.* The function $e^{iz^2}$ is entire, so its integral around the boundary of the sector $S_R = \{re^{i\theta} : 0\le r\le R,\ 0\le\theta\le\pi/4\}$ vanishes.

*The arc.* On $z = Re^{i\theta}$ with $0\le\theta\le\pi/4$ we have $\lvert e^{iz^2}\rvert = e^{-R^2\sin2\theta}$, and $\sin2\theta\ge4\theta/\pi$ on that range (the chord bound $\sin\varphi\ge2\varphi/\pi$ for $0\le\varphi\le\pi/2$, applied to $\varphi = 2\theta$). Hence
$$\left\lvert\int_{\text{arc}}e^{iz^2}dz\right\rvert\le R\int_0^{\pi/4}e^{-4R^2\theta/\pi}\,d\theta = R\cdot\frac{\pi}{4R^2}\bigl(1-e^{-R^2}\bigr)\longrightarrow0 .$$

*The two radii.* Along the real axis the integral is $\int_0^R e^{ix^2}dx$. Along the ray $\theta = \pi/4$, put $z = re^{i\pi/4}$; then $z^2 = ir^2$ and $dz = e^{i\pi/4}dr$, so the integral *from the outer end back to the origin* is $-e^{i\pi/4}\int_0^R e^{-r^2}dr$.

Adding the three pieces and letting $R\to\infty$,
$$\int_0^\infty e^{ix^2}dx - e^{i\pi/4}\int_0^\infty e^{-r^2}dr = 0,$$
that is
$$\int_0^\infty e^{ix^2}dx = e^{i\pi/4}\cdot\frac{\sqrt\pi}{2} = \frac{\sqrt2}{2}(1+i)\frac{\sqrt\pi}{2} = \frac{\sqrt{2\pi}}{4}(1+i).$$
Taking real and imaginary parts,
$$\int_0^\infty\cos(x^2)\,dx = \int_0^\infty\sin(x^2)\,dx = \frac{\sqrt{2\pi}}{4}.$$

**Check.** $\sqrt{2\pi}/4\approx0.6267$. A quadrature of $\cos(x^2)$ over $[0,50]$ gives $0.620$, with the slow tail contributing the remaining $0.007$; splitting the integral at the zeros of $x^2$ and summing the alternating humps converges to $0.6267$. The two Fresnel integrals being equal is also forced by the identity $\int_0^\infty e^{ix^2}dx = e^{i\pi/4}\cdot\tfrac{\sqrt\pi}{2}$, whose real and imaginary parts are equal because $e^{i\pi/4}$ has equal components. $\checkmark$

