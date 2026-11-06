# Analytic Functions — Solutions

> [Tutorial](README.md) · [Exercises](exercises.md) · 36 worked solutions

Each solution states the strategy, carries out every step, and ends with a check where one is
available.

## Beginner

**1.** By Definition 5.1, with $z_0 = 1+i$,

$$\frac{f(z_0+h)-f(z_0)}{h} = \frac{(3(z_0+h)+2)-(3z_0+2)}{h} = \frac{3h}{h} = 3.$$

The quotient equals $3$ for every $h\ne0$, so the limit is $3$ and $f'(1+i) = 3$.

**Check.** The function is $f(z) = 3z+2$, a polynomial with derivative $3$ everywhere.

**2.** By the power rule and linearity, $f'(z) = 2z-1$. At $z = 2-i$,

$$f'(2-i) = 2(2-i)-1 = 4-2i-1 = 3-2i.$$

**Check.** Using the definition at $z_0 = 2-i$ would give $2z_0-1$ by the same algebra as Example 7.3; the value is $3-2i$.

**3.** For $z = x+iy$, $z^2 = (x^2-y^2)+2xyi$, so $u = x^2-y^2$ and $v = 2xy$. Then

$$u_x = 2x = v_y, \qquad u_y = -2y = -v_x,$$

so the Cauchy–Riemann equations hold for every $z$. Since the partials are polynomials, they are continuous, and Theorem 7.7 gives $f'(z) = u_x+iv_x = 2x+2yi = 2z$.

**4.** Compute $\bar z^2 = (x-iy)^2 = (x^2-y^2)-2xyi$, so $u = x^2-y^2$ and $v = -2xy$. The Cauchy–Riemann equations are

$$u_x = 2x = v_y = -2x \iff x = 0, \qquad u_y = -2y = -v_x = 2y \iff y = 0.$$

Both hold only at $z = 0$. The partial derivatives are continuous, so Theorem 7.7 applies: $f$ is differentiable at $0$ and nowhere else, with

$$f'(0) = u_x(0,0)+iv_x(0,0) = 0+0 = 0.$$

**5.** $u = e^x\cos y$ and $v = e^x\sin y$, so

$$u_x = e^x\cos y = v_y, \qquad u_y = -e^x\sin y = -v_x.$$

The partials are continuous everywhere, so $e^z$ is entire, with $f' = u_x+iv_x = e^x\cos y+ie^x\sin y = e^z$.

**6.** For $z = x+iy\ne0$, multiply numerator and denominator by $\bar z$:

$$\frac1z = \frac{x-iy}{x^2+y^2} = \frac{x}{x^2+y^2}-i\frac{y}{x^2+y^2},$$

so $u = x/r^2$ and $v = -y/r^2$ with $r^2 = x^2+y^2$. Then

$$u_x = \frac{r^2-x(2x)}{r^4} = \frac{y^2-x^2}{r^4}, \qquad v_y = \frac{-r^2+y(2y)}{r^4} = \frac{y^2-x^2}{r^4},$$

and

$$u_y = \frac{-x(2y)}{r^4} = -\frac{2xy}{r^4}, \qquad v_x = \frac{y(2x)}{r^4} = \frac{2xy}{r^4}.$$

Thus $u_x = v_y$ and $u_y = -v_x$. Hence

$$f'(z) = u_x+iv_x = \frac{y^2-x^2}{r^4}+i\frac{2xy}{r^4} = -\frac{(x^2-y^2)-2xyi}{(x^2+y^2)^2} = -\frac{\bar z^2}{z^2\bar z^2} = -\frac1{z^2}.$$

**7.** Write $f(z) = z\lvert z\rvert^2 = (x+iy)(x^2+y^2)$, so

$$u = x^3+xy^2, \qquad v = x^2y+y^3.$$

Then $u_x = 3x^2+y^2$, $v_y = x^2+3y^2$, $u_y = 2xy$, $v_x = 2xy$. The equations are

$$3x^2+y^2 = x^2+3y^2 \iff x^2 = y^2, \qquad 2xy = -2xy \iff xy = 0.$$

Together these force $x = y = 0$. So $f$ is differentiable only at $0$, with $f'(0) = u_x(0)+iv_x(0) = 0$; the partials are polynomials, hence continuous, so Theorem 7.7 applies.

**8.** $u_x = 2x$, $u_{xx} = 2$; $u_y = 2y$, $u_{yy} = 2$. Hence $u_{xx}+u_{yy} = 4\ne0$, so $u$ is not harmonic.

**9.** $u_x = 3x^2-3y^2$, $u_{xx} = 6x$; $u_y = -6xy$, $u_{yy} = -6x$; hence $u_{xx}+u_{yy} = 0$, so $u$ is harmonic. For a conjugate, $v_y = u_x = 3x^2-3y^2$, so $v = 3x^2y-y^3+g(x)$. Then $v_x = 6xy+g'(x) = -u_y = 6xy$, so $g' = 0$ and $g$ is constant. Thus

$$v = 3x^2y-y^3+C, \qquad u+iv = (x^3-3xy^2)+i(3x^2y-y^3)+iC = z^3+iC.$$

**Check.** $z^3 = (x+iy)^3 = (x^3-3xy^2)+i(3x^2y-y^3)$ by direct expansion.

**10.** $\lvert1+i\rvert = \sqrt2$ and $\operatorname{Arg}(1+i) = \pi/4$, so $\operatorname{Log}(1+i) = \tfrac12\ln2+i\pi/4$. For $-\sqrt3+i$, the modulus is $\sqrt{3+1} = 2$ and the point is in the second quadrant with reference angle $\pi/6$, so $\operatorname{Arg} = 5\pi/6$ and

$$\operatorname{Log}(-\sqrt3+i) = \ln2+\frac{5\pi i}{6}.$$

**Check.** $e^{\ln2+5\pi i/6} = 2(\cos(5\pi/6)+i\sin(5\pi/6)) = 2(-\sqrt3/2+i/2) = -\sqrt3+i$.

**11.** By Euler's formula,

$$e^{i\pi/3} = \cos\frac\pi3+i\sin\frac\pi3 = \frac12+i\frac{\sqrt3}{2}, \qquad e^{1+i\pi/2} = e\,e^{i\pi/2} = ei, \qquad e^{2\pi i} = 1.$$

**12.** Using $\sin(iz) = i\sinh z$ and $\cos(iz) = \cosh z$,

$$\sin(i\ln2) = i\sinh(\ln2) = i\,\frac{2-\tfrac12}{2} = \frac{3i}{4}, \qquad \cos(i\ln2) = \cosh(\ln2) = \frac{2+\tfrac12}{2} = \frac54.$$

Then $\sin^2+\cos^2 = (3i/4)^2+(5/4)^2 = -9/16+25/16 = 1$.

## Intermediate

**13.** For $f(z) = x^2+iy^2$ we have $u = x^2$, $v = y^2$, so $u_x = 2x$, $u_y = 0$, $v_x = 0$, $v_y = 2y$. The Cauchy–Riemann equations reduce to $2x = 2y$ and $0 = 0$, i.e. $x = y$. The partials are continuous, so Theorem 7.7 gives differentiability exactly on the line $x = y$, where $f'(z) = u_x+iv_x = 2x$. No open disc is contained in that line, so $f$ is holomorphic on no open set.

**14.** Let $f(z) = u(x)+iv(y)$ with $u,v$ real differentiable. Then $u_x = u'(x)$, $u_y = 0$, $v_x = 0$, $v_y = v'(y)$, and the Cauchy–Riemann equations read

$$u'(x) = v'(y), \qquad 0 = 0.$$

The left side depends only on $x$ and the right side only on $y$, so both equal a common constant $c$. Hence $u = cx+\alpha$ and $v = cy+\beta$, and

$$f(z) = c(x+iy)+(\alpha+i\beta) = cz+b, \qquad c\in\mathbb{R},\ b\in\mathbb{C}.$$

Conversely, every map of this form is entire and of the required separable type.

**15.** $u = xy$ gives $u_x = y$, $u_y = x$, $u_{xx} = 0$, $u_{yy} = 0$, so $u$ is harmonic. A conjugate satisfies $v_y = u_x = y$ and $v_x = -u_y = -x$. Integrating the first in $y$ gives $v = y^2/2+g(x)$; then $v_x = g'(x) = -x$, so $g = -x^2/2+C$. Hence

$$v = \frac{y^2-x^2}{2}+C, \qquad u+iv = xy+i\frac{y^2-x^2}{2}+iC.$$

Now $z^2 = (x^2-y^2)+2xyi$, so $-\tfrac i2z^2 = xy-\tfrac i2(x^2-y^2) = xy+i\tfrac{y^2-x^2}{2}$. Therefore

$$u+iv = -\frac i2z^2+iC.$$

**16.** For $z = x+iy$, $e^z = e^x(\cos y+i\sin y)$ has argument $y$ and modulus $e^x>0$.

For $0<y<\pi$: every point with positive imaginary part arises, choosing $x = \ln\lvert w\rvert$ and $y = \arg w\in(0,\pi)$. Since $y$ never equals $0$ or $\pi$, the image is the open upper half-plane.

For $0<y<2\pi$: the argument ranges over $(0,2\pi)$, so every $w\ne0$ except those with argument $0$ arises; that is, the image is $\mathbb{C}$ minus the non-negative real axis $[0,\infty)$.

**17.** $1+i = \sqrt2\,e^{i\pi/4}$, so by Proposition 7.23,

$$z = \ln\sqrt2+i\left(\frac\pi4+2\pi k\right) = \frac12\ln2+i\left(\frac\pi4+2\pi k\right), \qquad k\in\mathbb{Z}.$$

**Check.** $e^{\frac12\ln2} = \sqrt2$ and $e^{i(\pi/4+2\pi k)} = e^{i\pi/4}$, so the product is $\sqrt2e^{i\pi/4} = 1+i$.

**18.** Take $z = w = -1$. Then $zw = 1$, so $\operatorname{Log}(zw) = 0$, while

$$\operatorname{Log}(-1)+\operatorname{Log}(-1) = i\pi+i\pi = 2\pi i.$$

The two sides differ. The correct relation is

$$\operatorname{Log}(zw) = \operatorname{Log}z+\operatorname{Log}w+2\pi i k$$

for some integer $k\in\{-1,0,1\}$ chosen so that the right side lies in the strip $-\pi<\operatorname{Im}\le\pi$. If $\operatorname{Re}z>0$ and $\operatorname{Re}w>0$, then $\operatorname{Arg}z,\operatorname{Arg}w\in(-\pi/2,\pi/2)$, their sum lies in $(-\pi,\pi)$, and $k = 0$; in that case the naive identity does hold.

**19.** Using $\sin z = (e^{iz}-e^{-iz})/(2i)$ and putting $t = e^{iz}$,

$$\frac{t-t^{-1}}{2i} = 2 \iff t-\frac1t = 4i \iff t^2-4it-1 = 0.$$

The quadratic has roots $t = 2i\pm\sqrt{-4+1} = 2i\pm i\sqrt3 = i(2\pm\sqrt3)$. Both are of the form $i\rho$ with $\rho>0$, so

$$e^{iz} = (2\pm\sqrt3)e^{i\pi/2} \implies iz = \ln(2\pm\sqrt3)+i\left(\frac\pi2+2\pi k\right),$$

hence

$$z = \frac\pi2+2\pi k-i\ln(2\pm\sqrt3) = \frac\pi2+2\pi k\pm i\ln(2+\sqrt3),$$

using $\ln(2-\sqrt3) = -\ln(2+\sqrt3)$.

**Check.** For $z = \pi/2+i\ln(2+\sqrt3)$, $\sin z = \cos(i\ln(2+\sqrt3)) = \cosh(\ln(2+\sqrt3)) = 2$ by the computation in Exercise 12 with $2+\sqrt3$ in place of $2$.

**20.** By the addition formulas and $\cos(iy) = \cosh y$, $\sin(iy) = i\sinh y$,

$$\cos(x+iy) = \cos x\cosh y-i\sin x\sinh y, \qquad \sin(x+iy) = \sin x\cosh y+i\cos x\sinh y.$$

Taking squared moduli and using $\cosh^2y = 1+\sinh^2y$,

$$\lvert\cos z\rvert^2 = \cos^2x\cosh^2y+\sin^2x\sinh^2y = \cos^2x+\sinh^2y,$$

$$\lvert\sin z\rvert^2 = \sin^2x\cosh^2y+\cos^2x\sinh^2y = \sin^2x+\sinh^2y.$$

**21.** $f'(z) = e^z$, so $f'(i\pi/4) = e^{i\pi/4}$, of modulus $1$ and argument $\pi/4$. Thus $f$ is conformal at $z_0$, with local scaling $1$ (lengths are preserved to first order) and local rotation $\pi/4$.

The horizontal line $y = \pi/4$ is $\{x+i\pi/4\}$; its image is $\{e^xe^{i\pi/4}:x\in\mathbb{R}\}$, the open ray from $0$ at angle $\pi/4$. The vertical line $x = 0$ is $\{iy\}$; its image is $\{e^{iy}:y\in\mathbb{R}\}$, the unit circle.

**22.** (i) $a_n = 1/n!$: $\lvert a_{n+1}/a_n\rvert = 1/(n+1)\to0$, so $R = \infty$.

(ii) $a_n = n!$: $\lvert a_{n+1}/a_n\rvert = n+1\to\infty$, so $R = 0$.

(iii) $a_n = 2^{-n}$: $R = 1/\limsup 2^{-1} = 2$.

**23.** The geometric series gives

$$\frac{1}{1-z} = \sum_{n=0}^{\infty}z^n, \qquad \lvert z\rvert<1,$$

with radius $R = 1$ since $\limsup\lvert1\rvert^{1/n} = 1$. Differentiating term by term (Theorem 7.20),

$$\frac{1}{(1-z)^2} = \sum_{n=1}^{\infty}nz^{n-1} = \sum_{m=0}^{\infty}(m+1)z^m, \qquad \lvert z\rvert<1.$$

**24.** By the quotient rule,

$$f'(z) = \frac{(z+1)-(z-1)}{(z+1)^2} = \frac{2}{(z+1)^2}.$$

At $z = i$: $f'(i) = 2/(1+i)^2 = 2/(2i) = 1/i = -i$. This is non-zero, so $f$ is conformal at $i$, with local scaling $\lvert -i\rvert = 1$ and local rotation $-\pi/2$.

## Advanced

**25.** Write $f = u+iv$. The derivative is $f' = u_x+iv_x$ (Theorem 7.5), so the hypothesis that $f'$ is real means $v_x = 0$ on $\Omega$. The Cauchy–Riemann equations then give $u_y = -v_x = 0$ and $v_y = u_x$. Since $v_x = 0$, $v$ depends only on $y$; since $u_y = 0$, $u$ depends only on $x$. Hence

$$u'(x) = u_x = v_y = v'(y)$$

for all $(x,y)\in\Omega$. The left side depends only on $x$ and the right side only on $y$, so both equal a constant $c\in\mathbb{R}$. Integrating, $u = cx+\alpha$ and $v = cy+\beta$, so

$$f(z) = c(x+iy)+(\alpha+i\beta) = cz+b, \qquad c\in\mathbb{R}.$$

Conversely, $f = cz+b$ with $c$ real has $f' = c\in\mathbb{R}$.

**26.** If the constant is $0$, then $f\equiv0$. Otherwise $u^2+v^2 = c^2>0$ with $c = \lvert f\rvert$. Differentiating with respect to $x$ and $y$,

$$uu_x+vv_x = 0, \qquad uu_y+vv_y = 0.$$

Using the Cauchy–Riemann equations $u_y = -v_x$ and $v_y = u_x$, the second equation becomes $-uv_x+vu_x = 0$. Thus

$$\begin{pmatrix}u & v\\ v & -u\end{pmatrix}\begin{pmatrix}u_x\\ v_x\end{pmatrix} = \begin{pmatrix}0\\0\end{pmatrix}.$$

The determinant is $-u^2-v^2 = -c^2\ne0$, so the matrix is invertible and $u_x = v_x = 0$. Then $f' = u_x+iv_x = 0$ on $\Omega$, and Proposition 7.13 gives that $f$ is constant.

**27.** The gradients are $\nabla u = (u_x,u_y)$ and $\nabla v = (v_x,v_y)$. By the Cauchy–Riemann equations, $v_x = -u_y$ and $v_y = u_x$, so

$$\nabla u\cdot\nabla v = u_xv_x+u_yv_y = u_x(-u_y)+u_yu_x = 0.$$

Also $\lvert\nabla u\rvert^2 = u_x^2+u_y^2 = \lvert f'\rvert^2\ne0$ and $\lvert\nabla v\rvert^2 = v_x^2+v_y^2 = \lvert f'\rvert^2\ne0$, so both gradients are non-zero. A non-zero gradient is perpendicular to its level curve, so the two level curves meet at right angles.

**28.** Since $u$ is $C^2$,

$$\Delta(u^2) = (2uu_x)_x+(2uu_y)_y = 2(u_x^2+u_y^2)+2u(u_{xx}+u_{yy}) = 2\lvert\nabla u\rvert^2,$$

because $u$ is harmonic. If $u^2$ is harmonic, then $\Delta(u^2) = 0$, hence $\nabla u = 0$ on $\Omega$. A function with zero gradient on a connected open set is constant (argue as in Proposition 7.13: it is locally constant and $\Omega$ is connected).

**29.** From Proposition 7.6, $u_r = \frac1r v_\theta$ and $v_r = -\frac1r u_\theta$. Hence

$$f_\theta = u_\theta+iv_\theta = -rv_r+iru_r = ir(u_r+iv_r) = irf_r.$$

**Check.** For $f(z) = z^2 = r^2e^{2i\theta}$: $f_r = 2re^{2i\theta}$ and $f_\theta = 2ir^2e^{2i\theta} = ir\cdot2re^{2i\theta} = irf_r$. Agrees.

**30.** Here $a_n = 1/n^2$, and

$$\limsup_{n}\lvert a_n\rvert^{1/n} = \lim_{n}\exp\!\left(-\frac{2\ln n}{n}\right) = e^0 = 1,$$

so $R = 1$. On the closed unit disc, $\lvert z^n/n^2\rvert\le1/n^2$ and $\sum1/n^2$ converges, so the Weierstrass M-test gives uniform convergence. The derivative series is

$$\sum_{n\ge1}\frac{nz^{n-1}}{n^2} = \sum_{n\ge1}\frac{z^{n-1}}{n},$$

whose coefficients $1/n$ satisfy $\limsup(1/n)^{1/n} = 1$, so its radius is also $1$. At $z = 1$ it becomes the harmonic series $\sum1/n$, which diverges. This shows that the derivative of a power series can fail to converge at a boundary point where the original series converges.

**31.** The points $1/n$ are distinct and converge to $0$, which lies in the domain $\mathbb{C}$ of the entire function $f$. Thus the zeros of $f$ have an accumulation point in the domain, so the identity theorem (Remark 7.14) gives $f\equiv0$ on $\mathbb{C}$.

## Challenge

**32.** In polar form $z = re^{i\theta}$,

$$f(z) = \frac{z^3}{\bar z^2} = \frac{r^3e^{3i\theta}}{r^2e^{-2i\theta}} = re^{5i\theta} = r\cos5\theta+ir\sin5\theta,$$

so $u = r\cos5\theta$, $v = r\sin5\theta$, and $f(0) = 0$. Along the real axis, $f(x) = x$, so $u(x,0) = x$ and $v(x,0) = 0$; hence $u_x(0,0) = 1$ and $v_x(0,0) = 0$. Along the imaginary axis, $z = iy$ gives $z^3 = -iy^3$ and $\bar z^2 = -y^2$, so $f(iy) = iy$; hence $u(0,y) = 0$, $v(0,y) = y$, and $u_y(0,0) = 0$, $v_y(0,0) = 1$. Therefore

$$u_x(0) = 1 = v_y(0), \qquad u_y(0) = 0 = -v_x(0),$$

so the Cauchy–Riemann equations hold at $0$. But for $h = re^{i\theta}\ne0$,

$$\frac{f(h)-f(0)}{h} = \frac{h^3/\bar h^2}{h} = \frac{h^2}{\bar h^2} = e^{4i\theta},$$

which depends on the direction of approach and has no limit as $h\to0$. Hence $f$ is not differentiable at $0$. The hypothesis of Theorem 7.7 that fails is the continuity of the partial derivatives at $0$: for example, $u_x = \cos5\theta\cos\theta+5\sin5\theta\sin\theta$ oscillates as $r\to0$ with $\theta$ fixed, and does not tend to $u_x(0) = 1$ as $(x,y)\to(0,0)$ along suitable directions.

**33.** By Theorem 7.22, $f$ has a Taylor expansion at $z_0$; the hypothesis says

$$f(z_0+h)-f(z_0) = a_kh^k+O(h^{k+1}) = a_kh^k\bigl(1+O(h)\bigr),$$

with $a_k\ne0$. Let $\gamma_j(t) = z_0+tv_j+o(t)$ be two curves through $z_0$ with tangent directions $v_j\ne0$, $j = 1,2$. Then

$$f(\gamma_j(t))-f(z_0) = a_k\bigl(tv_j+o(t)\bigr)^k\bigl(1+O(t)\bigr) = a_kt^k\bigl(v_j^k+o(1)\bigr),$$

so the tangent direction of the image curve is $a_kv_j^k$. The oriented angle between the images is therefore

$$\arg\frac{a_kv_2^k}{a_kv_1^k} = k\arg\frac{v_2}{v_1},$$

which is $k$ times the oriented angle between $v_1$ and $v_2$. Hence angles at $z_0$ are multiplied by $k$.

If $f'(z_0)\ne0$, then $k = 1$ and angles are preserved, so $f$ is conformal (Theorem 7.18). If $f'(z_0) = 0$, then $k\ge2$; taking two curves whose angle is $\pi/k$ gives an image angle $\pi\ne\pi/k$, so angles are not preserved and $f$ is not conformal. This proves the equivalence.

**34.** If $e^{z_1} = e^{z_2}$ then $e^{z_1-z_2} = 1$, so $z_1-z_2 = 2\pi ik$ for some integer $k$. Since both imaginary parts lie in $(-\pi,\pi)$, the imaginary part of $z_1-z_2$ lies in $(-2\pi,2\pi)$; the only multiple of $2\pi$ in that open interval is $0$, so $k = 0$ and $z_1 = z_2$. Hence $\exp$ is injective on $S$.

For surjectivity, let $w\ne0$ and write $w = \lvert w\rvert e^{i\varphi}$ with $\varphi = \operatorname{Arg}w\in(-\pi,\pi)$. Then $z := \ln\lvert w\rvert+i\varphi\in S$ and $e^z = w$. Conversely, if $z\in S$ then $\operatorname{Im}z\in(-\pi,\pi)$, so $e^z$ has argument in $(-\pi,\pi)$ and is not a negative real number or zero. Hence the image is $\mathbb{C}\setminus(-\infty,0]$.

Vertical line $\operatorname{Re}z = c$: points are $c+iy$ with $\lvert y\rvert<\pi$, and $e^{c+iy} = e^ce^{iy}$. The image is the circle $\lvert w\rvert = e^c$ with the single point $-e^c$ (where the argument equals $\pi$ or $-\pi$) removed. Horizontal line $\operatorname{Im}z = \theta_0$ with $\theta_0\in(-\pi,\pi)$: points are $x+i\theta_0$, mapping to $e^xe^{i\theta_0}$, which is the open ray from $0$ at angle $\theta_0$.

**35.** Suppose $g:\mathbb{C}\setminus\{0\}\to\mathbb{C}$ is continuous and $g(z)^2 = z$. Define

$$h(\theta) := \frac{g(e^{i\theta})}{e^{i\theta/2}}, \qquad \theta\in[0,2\pi].$$

Then $h(\theta)^2 = g(e^{i\theta})^2/e^{i\theta} = 1$, so $h(\theta)\in\{1,-1\}$ for every $\theta$. Since $g$ and the exponential are continuous, $h$ is continuous; a continuous function on the connected interval $[0,2\pi]$ taking values in $\{1,-1\}$ is constant. Hence

$$h(0) = h(2\pi), \qquad\text{i.e.}\qquad g(1) = \frac{g(e^{2\pi i})}{e^{i\pi}} = \frac{g(1)}{-1} = -g(1),$$

so $g(1) = 0$. But then $g(1)^2 = 0\ne1$, a contradiction. Therefore no such continuous $g$ exists. A holomorphic branch would be continuous, so there is no holomorphic square root on $\mathbb{C}\setminus\{0\}$ either.

**36.** Let the line be $L = \{c+te^{i\alpha} : t\in\mathbb{R}\}$ with $c\in\mathbb{C}$ and $\alpha\in\mathbb{R}$. Define

$$g(z) := e^{-i\alpha}\bigl(f(z)-c\bigr).$$

Then $g$ is holomorphic on $\Omega$ (a composition of holomorphic maps) and takes values in $e^{-i\alpha}(L-c) = \mathbb{R}$. Write $g = U+iV$; the condition $g(\Omega)\subseteq\mathbb{R}$ means $V\equiv0$ on $\Omega$. Then $V_x = V_y = 0$, and the Cauchy–Riemann equations for $g$ give $U_x = V_y = 0$ and $U_y = -V_x = 0$. Hence $g' = U_x+iV_x = 0$ on the domain $\Omega$, so $g$ is constant by Proposition 7.13. Therefore $f = e^{i\alpha}g+c$ is constant as well.
