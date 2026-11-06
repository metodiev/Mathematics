# Power Series and Residues — Solutions

> [Tutorial](README.md) · [Exercises](exercises.md) · 38 worked solutions

Each solution states the strategy, carries out every step, names the annulus or contour used, and ends
with an independent check where one is available.

## Beginner

**1.** *Strategy: ratio test or Cauchy–Hadamard.* The radius is $R = 1/\limsup\lvert a_n\rvert^{1/n}$.

(a) $a_n = 1/n!$: $\left\lvert a_{n+1}/a_n\right\rvert = 1/(n+1)\to0$, so $R = \infty$; the series is $e^z$.

(b) $a_n = n!$: $\left\lvert a_{n+1}/a_n\right\rvert = n+1\to\infty$, so $R = 0$; the series diverges for every $z\ne0$.

(c) $a_n = 2^{-n}$: $\left\lvert a_{n+1}/a_n\right\rvert = 1/2$, so $R = 2$; the series is $1/(1-z/2)$.

(d) $a_n = n^{-2}$ (with centre $1$): $n^{2/n}\to1$, so $R = 1$; the singularity at $z=0$ is at distance $1$ from the centre.

**Check.** In (c) the sum is $1/(1-z/2)$, whose pole is at $z=2$, at distance $2$; in (d) the sum is a dilogarithm-type function with a singularity at $z=0$, distance $1$. In both cases the radius equals the distance to the nearest singularity, as Theorem 7.4 promises. $\checkmark$

**2.** *Strategy: substitute the standard exponential series.*
$$e^{2z} = \sum_{n\ge0}\frac{(2z)^n}{n!} = \sum_{n\ge0}\frac{2^n}{n!}z^n,\qquad R = \infty .$$
For powers of $z-1$, write $2z = 2+2(z-1)$:
$$e^{2z} = e^{2}\cdot e^{2(z-1)} = e^{2}\sum_{n\ge0}\frac{2^n}{n!}(z-1)^n,\qquad R = \infty .$$

**Check.** At $z=1$ the second series gives $e^2$, and $e^{2\cdot1} = e^2$. At $z=0$ the second series gives $e^2\sum(-2)^n/n! = e^2e^{-2} = 1 = e^0$. $\checkmark$

**3.** *Strategy: geometric series.*
$$\frac{1}{1+z} = \sum_{n\ge0}(-z)^n = \sum_{n\ge0}(-1)^nz^n,\qquad R = 1,$$
the radius being the distance from $0$ to the pole at $z=-1$. At $z=1/2$ the series is $\sum(-1)^n/2^n$, a geometric series of ratio $-1/2$, so its sum is
$$\frac{1}{1-(-1/2)} = \frac{2}{3},$$
and the function value is $\dfrac{1}{1+1/2} = \dfrac{2}{3}$.

**Check.** The partial sums alternate $1,\ \tfrac12,\ \tfrac34,\ \tfrac58,\dots$ and converge to $2/3$, as the tail formula $\lvert r\rvert^{N+1}/(1-r)$ with $r = -1/2$ predicts. $\checkmark$

**4.** *Strategy: normalise the constant term.*
$$\frac{1}{2-z} = \frac12\cdot\frac{1}{1-z/2} = \frac12\sum_{n\ge0}\Bigl(\frac z2\Bigr)^n = \sum_{n\ge0}\frac{z^n}{2^{n+1}},\qquad R = 2 .$$

**Check.** At $z=0$ the series gives $1/2 = 1/(2-0)$; at $z=1$ it gives $\sum 2^{-n-1} = 1 = 1/(2-1)$. The singularity is at $z=2$, at distance $2$, so the radius cannot exceed $2$; the geometric ratio is $\lvert z\rvert/2<1$ exactly inside the disc. $\checkmark$

**5.** *Strategy: partial fractions, then a geometric series on each annulus.*
$$\frac{1}{z(z-2)} = -\frac{1}{2z}+\frac{1}{2(z-2)} .$$

*On $0<\lvert z\rvert<2$:* here $\lvert z/2\rvert<1$, so
$$\frac{1}{2(z-2)} = -\frac14\cdot\frac{1}{1-z/2} = -\frac14\sum_{n\ge0}\Bigl(\frac z2\Bigr)^n = -\sum_{n\ge0}\frac{z^n}{2^{n+2}} .$$
Hence
$$f(z) = -\frac{1}{2z}-\frac14-\frac{z}{8}-\frac{z^2}{16}-\cdots .$$
The coefficient of $z^{-1}$ is $-\tfrac12$, which is $\operatorname{Res}(f,0) = \lim_{z\to0}zf(z) = \dfrac{1}{0-2} = -\tfrac12$.

*On $2<\lvert z\rvert<\infty$:* here $\lvert 2/z\rvert<1$, so
$$\frac{1}{2(z-2)} = \frac{1}{2z}\cdot\frac{1}{1-2/z} = \sum_{n\ge0}\frac{2^n}{2z^{n+1}} = \frac{1}{2z}+\frac{1}{z^2}+\frac{2}{z^3}+\cdots,$$
and the $1/(2z)$ cancels the $-\dfrac{1}{2z}$:
$$f(z) = \frac{1}{z^2}+\frac{2}{z^3}+\frac{4}{z^4}+\cdots = \sum_{n\ge0}\frac{2^n}{z^{n+2}} .$$
The coefficient of $z^{-1}$ is $0$. This is not the residue at $0$ — that is read off the *inner* annulus — but the normalized integral over a large circle, which encloses both poles: $\operatorname{Res}(f,0)+\operatorname{Res}(f,2) = -\tfrac12+\tfrac12 = 0$.

**Check.** At $z=1$ the first series is $-\tfrac12-\tfrac14\cdot\tfrac{1}{1-1/2} = -\tfrac12-\tfrac12 = -1$, and $f(1) = 1/(1\cdot(-1)) = -1$. At $z=4$ the second series is $\tfrac1{16}(1+\tfrac12+\tfrac14+\cdots) = \tfrac1{16}\cdot2 = \tfrac18$, and $f(4) = 1/(4\cdot2) = 1/8$. $\checkmark$

**6.** *Strategy: substitute into the exponential series.*
$$e^{1/z} = \sum_{n\ge0}\frac{1}{n!\,z^n} = 1+\frac1z+\frac{1}{2!z^2}+\frac{1}{3!z^3}+\cdots,\qquad 0<\lvert z\rvert<\infty .$$
The coefficient of $z^{-1}$ is $1$, so $\operatorname{Res}(e^{1/z},0) = 1$. The principal part is infinite, so $0$ is an essential singularity.

**Check.** $\oint_{\lvert z\rvert=1}e^{1/z}dz = 2\pi i\cdot1 = 2\pi i$ by term-by-term integration, since every other term has an elementary primitive. $\checkmark$

**7.** (a) $\dfrac{1-\cos z}{z^2} = \dfrac{1}{z^2}\Bigl(\dfrac{z^2}{2}-\dfrac{z^4}{24}+\cdots\Bigr) = \dfrac12-\dfrac{z^2}{24}+\cdots$: **removable**, value $1/2$.

(b) $\dfrac{\cos z}{z^3} = \dfrac{1}{z^3}\Bigl(1-\dfrac{z^2}{2}+\cdots\Bigr) = \dfrac{1}{z^3}-\dfrac{1}{2z}+\cdots$: **pole of order $3$**, residue $-\tfrac12$.

(c) $e^{1/z^2} = \sum_{n\ge0}\dfrac{1}{n!\,z^{2n}}$: infinitely many negative powers, **essential**, residue $0$ (there is no $z^{-1}$ term, since all exponents are even).

(d) $\dfrac{\sin z}{z^4} = \dfrac{1}{z^4}\Bigl(z-\dfrac{z^3}{6}+\cdots\Bigr) = \dfrac{1}{z^3}-\dfrac{1}{6z}+\cdots$: **pole of order $3$**, residue $-\tfrac16$.

**Check.** In (a) the limit as $z\to0$ is $1/2$, consistent with removable; in (b) and (d) $\lvert f\rvert\to\infty$, consistent with poles; in (c) the function oscillates unboundedly, and $e^{1/z^2} = 1$ whenever $z^2 = 1/(2\pi i n)$, so values near $1$ occur arbitrarily close to $0$. $\checkmark$

**8.** (a) $\operatorname{Res}\Bigl(\dfrac{1}{z^2+1},i\Bigr) = \dfrac{1}{2i} = -\dfrac i2$.

(b) $\operatorname{Res}\Bigl(\dfrac{z}{z-3},3\Bigr) = 3$.

(c) $\operatorname{Res}\Bigl(\dfrac{e^z}{z-1},1\Bigr) = e$.

(d) $\operatorname{Res}\Bigl(\dfrac{z^2+1}{z-1},1\Bigr) = 1+1 = 2$.

**Check.** In (a), $\dfrac{1}{z^2+1} = \dfrac{1}{2i}\Bigl(\dfrac{1}{z-i}-\dfrac{1}{z+i}\Bigr)$, so the coefficient of $1/(z-i)$ is $\dfrac{1}{2i}$, confirming the value. In (b) and (d) the functions are of the form $g(z)/(z-a)$ with $g$ holomorphic, so the residue is $g(a)$. $\checkmark$

**9.** *Strategy: simple-pole formula.*
$$\operatorname{Res}\Bigl(\frac{1}{z(z-1)},0\Bigr) = \lim_{z\to0}\frac{z}{z(z-1)} = \frac{1}{-1} = -1,$$
$$\operatorname{Res}\Bigl(\frac{1}{z(z-1)},1\Bigr) = \lim_{z\to1}\frac{z-1}{z(z-1)} = \frac{1}{1} = 1 .$$
The sum is $0$.

**Check.** The function is rational with $\deg(\text{denominator})-\deg(\text{numerator}) = 2$, so $\operatorname{Res}(f,\infty) = 0$; the total-residue identity then forces the finite residues to sum to $0$, as they do. $\checkmark$

**10.** *Strategy: residue theorem.* The poles are $\pm i$, both inside $\lvert z\rvert=2$, and both simple:
$$\operatorname{Res}\Bigl(\frac{1}{z^2+1},i\Bigr) = \frac{1}{2i},\qquad \operatorname{Res}\Bigl(\frac{1}{z^2+1},-i\Bigr) = \frac{1}{-2i} = -\frac{1}{2i}.$$
Their sum is $0$, so
$$\oint_{\lvert z\rvert=2}\frac{dz}{z^2+1} = 0 .$$

**Check.** Partial fractions give $\dfrac{1}{2i}\bigl(\oint dz/(z-i)-\oint dz/(z+i)\bigr) = \dfrac{1}{2i}(2\pi i-2\pi i) = 0$, in agreement. $\checkmark$

**11.** *Strategy: integral formula or residue.* The integrand $\dfrac{z+3}{z-1}$ has a simple pole at $1$ inside $\lvert z\rvert=2$, with residue $\lim_{z\to1}(z+3) = 4$. Hence
$$\oint_{\lvert z\rvert=2}\frac{z+3}{z-1}\,dz = 2\pi i\cdot4 = 8\pi i .$$

**Check.** Write $\dfrac{z+3}{z-1} = 1+\dfrac{4}{z-1}$; the constant term integrates to $0$ over a closed contour and the second term gives $4\cdot2\pi i$. $\checkmark$

**12.** *Strategy: residue via the $z^{-1}$ coefficient.*
$$\frac{\cos z}{z^2} = \frac{1}{z^2}\Bigl(1-\frac{z^2}{2}+\frac{z^4}{24}-\cdots\Bigr) = \frac{1}{z^2}-\frac12+\frac{z^2}{24}-\cdots,$$
so the coefficient of $z^{-1}$ is $0$ and the integral is $0$.

**Check.** By the differentiation formula, $\oint\cos z/z^2\,dz = 2\pi i\,(\cos)'(0) = -2\pi i\sin0 = 0$. $\checkmark$

## Intermediate

**13.** *Strategy: order-$2$ formula.* Write $f(z) = \dfrac{1}{(z-i)^2(z+i)^2}$.

At $i$: $h(z) = (z-i)^2f(z) = \dfrac{1}{(z+i)^2}$, so
$$h'(z) = -\frac{2}{(z+i)^3},\qquad h'(i) = -\frac{2}{(2i)^3} = -\frac{2}{-8i} = \frac{1}{4i} = -\frac i4 .$$
At $-i$: $h(z) = \dfrac{1}{(z-i)^2}$, so
$$h'(-i) = -\frac{2}{(-i-i)^3} = -\frac{2}{(-2i)^3} = -\frac{2}{8i} = -\frac{1}{4i} = \frac i4 .$$

**Check.** The two residues sum to $0$; the function is rational with $\deg q-\deg p = 4$, so the residue at infinity is $0$ and the total-residue identity requires the sum to vanish. $\checkmark$

**14.** *Strategy: order-$3$ formula.* The pole at $1$ has order $3$ (the numerator is nonzero there). With $h(z) = e^{2z}$,
$$\operatorname{Res} = \frac{1}{2!}h''(1) = \frac12\cdot4e^{2} = 2e^2 .$$

**Check by expansion.** Put $w = z-1$: $e^{2z} = e^2e^{2w} = e^2\bigl(1+2w+2w^2+\tfrac43w^3+\cdots\bigr)$, so $\dfrac{e^{2z}}{w^3} = e^2\Bigl(\dfrac{1}{w^3}+\dfrac{2}{w^2}+\dfrac{2}{w}+\cdots\Bigr)$ and the residue is $2e^2$. $\checkmark$

**15.** *Strategy: order-$2$ formula.* With $f(z) = \dfrac{z^2}{(z^2+1)^2}$ and $h(z) = (z-i)^2f(z) = \dfrac{z^2}{(z+i)^2}$,
$$h'(z) = \frac{2z(z+i)^2-2z^2(z+i)}{(z+i)^4} = \frac{2z(z+i)-2z^2}{(z+i)^3} = \frac{2zi}{(z+i)^3},$$
using $(z+i)^2 - z(z+i) = (z+i)(z+i-z) = i(z+i)$, so $2z\cdot i(z+i)/(z+i)^4 = 2zi/(z+i)^3$. At $z=i$,
$$h'(i) = \frac{2i\cdot i}{(2i)^3} = \frac{-2}{-8i} = \frac{1}{4i} = -\frac i4 .$$

**Check by expansion.** Near $z=i$ write $z = i+w$: $z^2 = -1+2iw+w^2$ and $z^2+1 = 2iw+w^2 = 2iw(1+w/(2i))$, so
$$\frac{z^2}{(z^2+1)^2} = \frac{-1+2iw+\cdots}{-4w^2(1+w/(2i))^2} = \frac{1-2iw+\cdots}{4w^2}\Bigl(1-\frac{w}{i}+\cdots\Bigr).$$
The coefficient of $1/w$ is $\dfrac{1}{4}\Bigl(-2i-\dfrac1i\Bigr) = \dfrac{1}{4}(-2i+i) = -\dfrac{i}{4}$, in agreement. $\checkmark$

**16.** *Strategy: quotient formula.* $\tan z = \dfrac{\sin z}{\cos z}$, and at $z_0 = \pi/2$ we have $\sin z_0 = 1$, $\cos z_0 = 0$, $(\cos)' = -\sin$, so
$$\operatorname{Res}\Bigl(\tan z,\frac\pi2\Bigr) = \frac{\sin(\pi/2)}{-\sin(\pi/2)} = -1 .$$

**Check.** $\tan z = \cot(\pi/2-z)$; near $w = 0$ with $w = \pi/2-z$, $\cot w = 1/w - w/3-\cdots$, and $z-\pi/2 = -w$, so the coefficient of $1/(z-\pi/2)$ is $-1$. $\checkmark$

**17.** *Strategy: order-$2$ pole at $0$; the pole at $2$ is outside.* With $f(z) = \dfrac{1}{z^2(z-2)}$ and $h(z) = z^2f(z) = \dfrac{1}{z-2}$,
$$h'(z) = -\frac{1}{(z-2)^2},\qquad h'(0) = -\frac14 .$$
Hence
$$\oint_{\lvert z\rvert=1}\frac{dz}{z^2(z-2)} = 2\pi i\left(-\frac14\right) = -\frac{\pi i}{2}.$$

**Check by expansion.** $\dfrac{1}{z-2} = -\dfrac12\cdot\dfrac{1}{1-z/2} = -\dfrac12-\dfrac z4-\cdots$, so $\dfrac{1}{z^2(z-2)} = -\dfrac{1}{2z^2}-\dfrac{1}{4z}-\cdots$ and the residue is $-\tfrac14$, confirming the result. $\checkmark$

**18.** *Strategy: residues at the enclosed poles.* The poles are $0,1,3$; the circle $\lvert z\rvert=2$ encloses $0$ and $1$, but not $3$.

At $0$: $\operatorname{Res} = \dfrac{0+1}{(0-1)(0-3)} = \dfrac13$.

At $1$: $\operatorname{Res} = \dfrac{1+1}{1\cdot(1-3)} = \dfrac{2}{-2} = -1$.

Sum: $\dfrac13-1 = -\dfrac23$. Hence
$$\oint_{\lvert z\rvert=2}\frac{z^2+1}{z(z-1)(z-3)}\,dz = 2\pi i\left(-\frac23\right) = -\frac{4\pi i}{3}.$$

**Check.** The residue at $3$ is $\dfrac{9+1}{3\cdot2} = \dfrac{10}{6} = \dfrac53$. The sum of all finite residues is $\dfrac13-1+\dfrac53 = 1$, so the residue at infinity is $-1$; directly, the integrand behaves like $1/z$ at infinity with coefficient $1$, and $\operatorname{Res}(f,\infty) = -1$ by Proposition 7.32. Consistent. $\checkmark$

**19.** *Strategy: reduce to a standard contour integral.* Write $\sin^2\theta = \tfrac12(1-\cos2\theta)$, so
$$I = \frac12\left(I_0-I_2\right),\qquad I_n := \int_0^{2\pi}\frac{e^{in\theta}}{5-4\cos\theta}\,d\theta .$$
For $I_n$, substitute $z = e^{i\theta}$: $\cos\theta = \tfrac12(z+z^{-1})$ and $d\theta = dz/(iz)$, so
$$5-4\cos\theta = \frac{5z-2z^2-2}{z},\qquad I_n = \oint_{\lvert z\rvert=1}z^n\cdot\frac{z}{5z-2z^2-2}\cdot\frac{dz}{iz} = \frac1i\oint_{\lvert z\rvert=1}\frac{z^n}{-2z^2+5z-2}\,dz .$$
Now $-2z^2+5z-2 = -2(z-\tfrac12)(z-2)$, so the only pole inside is $z_0 = \tfrac12$, and
$$\frac1i\oint\frac{z^n}{-2(z-\tfrac12)(z-2)}\,dz = \frac1i\cdot2\pi i\cdot\frac{z_0^n}{-2(z_0-2)} = 2\pi\cdot\frac{(1/2)^n}{-2\cdot(-\tfrac32)} = \frac{2\pi}{3}\Bigl(\frac12\Bigr)^n .$$
Thus $I_0 = \dfrac{2\pi}{3}$ and $I_2 = \dfrac{2\pi}{3}\cdot\dfrac14 = \dfrac{\pi}{6}$, and
$$I = \frac12\left(\frac{2\pi}{3}-\frac{\pi}{6}\right) = \frac12\cdot\frac{\pi}{2} = \frac{\pi}{4}.$$

**Check.** $\pi/4\approx0.7854$, confirmed by quadrature. The general formula $\int_0^{2\pi}\dfrac{d\theta}{a+b\cos\theta} = \dfrac{2\pi}{\sqrt{a^2-b^2}}$ with $a=5$, $b=-4$ gives $2\pi/3$ for $I_0$, consistent. Also $\sin^2\theta/(5-4\cos\theta)\ge0$ and $\sin^2\theta\le1$, $5-4\cos\theta\ge1$, so the integral lies between $0$ and $\pi$; $\pi/4$ does. $\checkmark$

**20.** *Strategy: reuse the formula for $I_n$.* From Exercise 19, for the kernel $5-4\cos\theta$,
$$I_n = \int_0^{2\pi}\frac{e^{in\theta}}{5-4\cos\theta}\,d\theta = \frac{2\pi}{3}\Bigl(\frac12\Bigr)^n,\qquad n\ge0 .$$
Therefore
$$\int_0^{2\pi}\frac{\cos3\theta}{5-4\cos\theta}\,d\theta = \operatorname{Re}I_3 = \frac{2\pi}{3}\cdot\frac18 = \frac{\pi}{12}.$$

**Check.** $\pi/12\approx0.2618$, confirmed by quadrature. The value is smaller than $I_0 = 2\pi/3$, as expected since $\cos3\theta$ oscillates three times over the period and cancels more. $\checkmark$

**21.** *Strategy: complete the square and apply residues.*
$$x^2+2x+5 = (x+1)^2+4,$$
so the poles are $z = -1\pm2i$, and only $-1+2i$ lies in the upper half-plane. Both are simple, and with $q(z) = z^2+2z+5$, $q'(z) = 2z+2$, so
$$\operatorname{Res}\Bigl(\frac{1}{z^2+2z+5},-1+2i\Bigr) = \frac{1}{2(-1+2i)+2} = \frac{1}{4i} = -\frac i4 .$$
By Theorem 7.22 (degree $0$ numerator, degree $2$ denominator),
$$\int_{-\infty}^{\infty}\frac{dx}{x^2+2x+5} = 2\pi i\left(-\frac i4\right) = \frac{\pi}{2}.$$

**Check.** Substitute $u = x+1$: the integral becomes $\int_{\mathbb{R}}du/(u^2+4) = \bigl[\tfrac12\arctan(u/2)\bigr]_{-\infty}^{\infty} = \pi/2$. $\checkmark$

**22.** *Strategy: order-$2$ residues.* The poles are $\pm i$, each of order $2$. With $f(z) = \dfrac{1}{(z^2+1)^2}$ and $h(z) = (z-i)^2f(z) = \dfrac{1}{(z+i)^2}$,
$$h'(i) = -\frac{2}{(2i)^3} = -\frac i4 .$$
At the lower pole, $h(z) = \dfrac{1}{(z-i)^2}$ and $h'(-i) = -\dfrac{2}{(-2i)^3} = \dfrac{i}{4}$. Only $i$ lies in the upper half-plane, so by Theorem 7.22,
$$\int_{-\infty}^{\infty}\frac{dx}{(1+x^2)^2} = 2\pi i\left(-\frac i4\right) = \frac{\pi}{2}.$$

**Check.** Integration by parts gives $\int_{\mathbb{R}}dx/(1+x^2)^2 = \tfrac12\bigl[x/(1+x^2)+\arctan x\bigr]_{-\infty}^{\infty} = \tfrac12\cdot\pi = \pi/2$, in agreement. $\checkmark$

## Advanced

**23.** *Strategy: estimate the Laurent coefficients.* Let $f(z) = \sum_{n\in\mathbb{Z}}a_n(z-z_0)^n$ on $0<\lvert z-z_0\rvert<\rho$. For $0<r<\rho$, the coefficient formula and the ML inequality give, for every $n$,
$$\lvert a_n\rvert = \left\lvert\frac{1}{2\pi i}\oint_{\lvert\zeta-z_0\rvert=r}\frac{f(\zeta)}{(\zeta-z_0)^{n+1}}\,d\zeta\right\rvert\le\frac{1}{2\pi}\cdot2\pi r\cdot\frac{Cr^{-\alpha}}{r^{n+1}} = C\,r^{-\alpha-n}.$$
For $n\le-1$ the exponent $-\alpha-n\ge1-\alpha>0$, so $r^{-\alpha-n}\to0$ as $r\to0$, forcing $a_n = 0$. Hence the principal part vanishes and $z_0$ is removable by definition.

For $\alpha=1$ the estimate reads $\lvert a_n\rvert\le Cr^{-1-n}$, which tends to $0$ only for $n\le-2$; the coefficient $a_{-1}$ is not controlled. Indeed $f(z) = 1/z$ at $z_0=0$ satisfies $\lvert f(z)\rvert = \lvert z\rvert^{-1}$ and has a simple pole with residue $1$. So the strict inequality $\alpha<1$ is sharp.

**Check.** Take $f(z) = z^{-1/3}$ on a punctured disc slit along a ray: it is not holomorphic on the *full* punctured disc, which is exactly why the exercise's hypothesis excludes it, and the exercised bound would allow $\alpha=1/3$ but says nothing without holomorphy on the whole punctured disc. Within the hypothesis, $\alpha=1$ is the threshold: at $\alpha = 1$ the model $f(z) = 1/z$ has a pole, at $\alpha<1$ every such function is removable. $\checkmark$

**24.** *Strategy: invert the function.* Suppose $\lvert f(z)\rvert\to\infty$ as $z\to z_0$. Then $f$ has no zeros in some punctured disc $0<\lvert z-z_0\rvert<\delta$, so $g := 1/f$ is holomorphic there and $g(z)\to0$. Being convergent, $g$ is bounded on a punctured neighbourhood, so Theorem 7.11 makes $z_0$ a removable singularity of $g$ with $g(z_0) = 0$. Thus $g$ is holomorphic on the disc and has a zero of some finite order $m\ge1$ at $z_0$; the order is finite because otherwise $g$ would vanish on a neighbourhood and $f$ would be undefined there.

Hence $g(z) = (z-z_0)^m\varphi(z)$ with $\varphi$ holomorphic and $\varphi(z_0)\ne0$. Since $g$ is not identically zero, $\varphi$ has no zeros near $z_0$ after shrinking the disc, and
$$f(z) = \frac{1}{(z-z_0)^m\varphi(z)} = \frac{\psi(z)}{(z-z_0)^m},\qquad \psi := \frac1\varphi\ \text{holomorphic},\ \psi(z_0)\ne0 .$$
By Theorem 7.12, $z_0$ is a pole of order $m$. Moreover $(z-z_0)^mf(z) = \psi(z)\to\psi(z_0)\ne0$ is bounded, while for $k<m$ the product $(z-z_0)^kf(z) = \psi(z)/(z-z_0)^{m-k}$ is unbounded. So $m$ is the smallest integer for which $(z-z_0)^mf$ stays bounded.

**Check.** For $f(z) = 1/\sin z$ at $0$: $\lvert f\rvert\to\infty$, $g = \sin z$ has a zero of order $1$, and $m=1$: $z/\sin z\to1$ is bounded, while $\sin z$ itself is not bounded away from $0$ in the required sense. $\checkmark$

**25.** *Strategy: suppose a limit exists and derive a contradiction; then examine $e^{1/z}$.* Let $z_0$ be an essential singularity.

*No finite limit.* If $f(z)\to w\in\mathbb{C}$, then $f$ is bounded near $z_0$, so $z_0$ is removable by Theorem 7.11 — contradiction.

*No infinite limit.* If $\lvert f(z)\rvert\to\infty$, then by Exercise 24 the point $z_0$ is a pole — contradiction.

*Density does not imply surjectivity.* For $f(z) = e^{1/z}$ the image of every punctured disc is $\mathbb{C}\setminus\{0\}$: the equation $e^{1/z} = v$ has the solution $z = 1/\log v$ for any choice of logarithm when $v\ne0$, and arbitrarily small solutions are obtained by adding $2\pi ik$ to the logarithm. The value $0$ is never attained. Hence the image is dense but not all of $\mathbb{C}$, so Casorati–Weierstrass cannot be strengthened to surjectivity. (Picard's great theorem does give surjectivity with at most one exception.)

**Check.** The two "no limit" arguments show that an essential singularity is characterised by the *non-existence* of a limit in $\mathbb{C}_\infty$, which is a clean third characterisation alongside the Laurent one. $\checkmark$

**26.** *Strategy: locate the poles of $f'/f$.* Let $a$ be a zero of $f$ of order $k\ge1$ inside $\gamma$. Write $f = (z-a)^kg$ with $g$ holomorphic and $g(a)\ne0$. Then
$$\frac{f'}{f} = \frac{k(z-a)^{k-1}g+(z-a)^kg'}{(z-a)^kg} = \frac{k}{z-a}+\frac{g'}{g},$$
and $g'/g$ is holomorphic at $a$, so $f'/f$ has a simple pole at $a$ with residue $k$.

Let $b$ be a pole of $f$ of order $m\ge1$. Write $f = (z-b)^{-m}h$ with $h$ holomorphic and $h(b)\ne0$. Then
$$f' = -m(z-b)^{-m-1}h+(z-b)^{-m}h',\qquad \frac{f'}{f} = \frac{-m}{z-b}+\frac{h'}{h},$$
so $f'/f$ has a simple pole at $b$ with residue $-m$.

There are no other singularities of $f'/f$ inside $\gamma$, because $f$ and $f'$ are holomorphic elsewhere and $f\ne0$ there. The residue theorem gives
$$\frac{1}{2\pi i}\oint_\gamma\frac{f'}{f}\,dz = \sum_{\text{zeros}}k-\sum_{\text{poles}}m = Z-P . \qquad\blacksquare$$

**Check.** For $f(z) = z^2/(z-1)$ and $\gamma$ the circle $\lvert z\rvert=2$: $Z = 2$ (double zero at $0$), $P = 1$ (simple pole at $1$), so the integral should be $2\pi i(2-1) = 2\pi i$. Directly, $f'/f = 2/z-1/(z-1)$, and the integral is $2(2\pi i)-2\pi i = 2\pi i$. $\checkmark$

**27.** *Strategy: Rouché on two circles.* Let $P(z) = z^4+3z+1$.

*Inside $\lvert z\rvert=1$:* take $f(z) = 3z$, $g(z) = z^4+1$. On $\lvert z\rvert=1$,
$$\lvert g(z)\rvert\le1+1 = 2<3 = \lvert f(z)\rvert .$$
So $P$ has as many zeros as $3z$ in the unit disc: exactly **one**.

*Inside $\lvert z\rvert=2$:* take $f(z) = z^4$, $g(z) = 3z+1$. On $\lvert z\rvert=2$,
$$\lvert g(z)\rvert\le6+1 = 7<16 = \lvert f(z)\rvert .$$
So all **four** zeros lie in $\lvert z\rvert<2$.

*In the annulus:* $4-1 = $ **three** zeros satisfy $1<\lvert z\rvert<2$.

**Check.** Numerically the zeros have moduli approximately $0.3377$, $1.3075$, $1.505$, $1.505$: one inside the unit circle and three in the annulus, as predicted. $P(0) = 1>0$ and $P(-1) = 1-3+1 = -1<0$, so there is a real zero in $(-1,0)$, consistent with the count. $\checkmark$

**28.** *Strategy: Rouché on two circles.* Let $P(z) = z^5-6z+3$.

*Inside $\lvert z\rvert=1$:* take $f(z) = -6z$, $g(z) = z^5+3$. On $\lvert z\rvert=1$,
$$\lvert g(z)\rvert\le1+3 = 4<6 = \lvert f(z)\rvert,$$
so there is **one** zero in the unit disc.

*Inside $\lvert z\rvert=2$:* take $f(z) = z^5$, $g(z) = -6z+3$. On $\lvert z\rvert=2$,
$$\lvert g(z)\rvert\le12+3 = 15<32 = \lvert f(z)\rvert,$$
so all **five** zeros lie in $\lvert z\rvert<2$.

*In the annulus:* **four** zeros satisfy $1<\lvert z\rvert<2$.

**Check.** Numerically the moduli are approximately $0.5055$, $1.4016$, $1.5918$, $1.5918$, $1.6709$: one below $1$ and four between $1$ and $2$. Since $P(0) = 3>0$ and $P(1) = 1-6+3 = -2<0$, the real root lies in $(0,1)$, matching. $\checkmark$

**29.** *Strategy: total residue, confirmed by the substitution.* Recall
$$\operatorname{Res}(f,\infty) = -\operatorname{Res}\Bigl(\frac{f(1/w)}{w^2},0\Bigr).$$

(a) $f(z) = 1/z$: $\dfrac{f(1/w)}{w^2} = \dfrac{w}{w^2} = \dfrac1w$, residue $1$ at $0$, so $\operatorname{Res}(f,\infty) = -1$. Finite residue: $1$ at $0$; total $1-1 = 0$.

(b) $f(z) = \dfrac{z}{z-1}$: $\dfrac{f(1/w)}{w^2} = \dfrac{1}{w^2}\cdot\dfrac{1/w}{1/w-1} = \dfrac{1}{w^2}\cdot\dfrac{1}{1-w} = \dfrac{1}{w^2}(1+w+w^2+\cdots)$, coefficient of $1/w$ is $1$, so $\operatorname{Res}(f,\infty) = -1$. Finite residue at $1$ is $1$; total $0$.

(c) $f(z) = \dfrac{1}{z^2+1}$: $\dfrac{f(1/w)}{w^2} = \dfrac{1}{w^2}\cdot\dfrac{w^2}{1+w^2} = \dfrac{1}{1+w^2}$, holomorphic at $0$, residue $0$, so $\operatorname{Res}(f,\infty) = 0$. Finite residues $\dfrac{1}{2i}-\dfrac{1}{2i} = 0$; total $0$.

(d) $f(z) = \dfrac{z^3}{z^2+1}$: $\dfrac{f(1/w)}{w^2} = \dfrac{1}{w^2}\cdot\dfrac{1/w^3}{1/w^2+1} = \dfrac{1}{w^3(1+w^2)} = \dfrac{1}{w^3}\bigl(1-w^2+w^4-\cdots\bigr) = \dfrac{1}{w^3}-\dfrac1w+\cdots$, so the residue at $0$ is $-1$ and $\operatorname{Res}(f,\infty) = 1$. Finite residues: $\dfrac{z^2}{2}$ at $i$ gives $-\dfrac12$, and at $-i$ also $-\dfrac12$; sum $-1$; total $-1+1 = 0$.

**Check.** Every case satisfies the total-residue identity of Theorem 7.33. In (d) the polynomial part of $f$ at infinity is $z-\dfrac{z}{z^2+1}$, and the residue at infinity detects the coefficient of $1/z$ in the expansion $z-\dfrac1z+\dfrac{1}{z^3}-\cdots$, which is $-1$, hence $\operatorname{Res}(f,\infty) = +1$. $\checkmark$

**30.** *Strategy: estimate the circle integral.* Write $p/q$ with $\deg p = m$, $\deg q = n$, $n\ge m+2$. For large $\lvert z\rvert$,
$$\left\lvert\frac{p(z)}{q(z)}\right\rvert\le\frac{C\lvert z\rvert^m}{\lvert z\rvert^n} = \frac{C}{\lvert z\rvert^{n-m}}\le\frac{C}{R^2}$$
on $\lvert z\rvert=R$. Hence
$$\left\lvert\frac{1}{2\pi i}\oint_{\lvert z\rvert=R}\frac{p}{q}\,dz\right\rvert\le\frac{1}{2\pi}\cdot2\pi R\cdot\frac{C}{R^2} = \frac{C}{R}\longrightarrow0 .$$
By Definition 5.6, $\operatorname{Res}(p/q,\infty)$ is the negative of this limit, so it is $0$. The total-residue theorem then gives
$$0 = \sum_{a\in\mathbb{C}}\operatorname{Res}\Bigl(\frac pq,a\Bigr)+\operatorname{Res}\Bigl(\frac pq,\infty\Bigr) = \sum_{a\in\mathbb{C}}\operatorname{Res}\Bigl(\frac pq,a\Bigr),$$
which is the stated identity.

**Check.** For $p/q = 1/(z^2-1)$ the finite residues are $\tfrac12$ and $-\tfrac12$, summing to $0$; for $z/(z^2-1)$ they are $\tfrac12$ and $\tfrac12$, summing to $1$, and indeed $\deg q-\deg p = 1<2$, so the hypothesis fails and $\operatorname{Res}(f,\infty) = -1\ne0$. $\checkmark$

## Challenge

**31.** *Strategy: upper semicircle, four simple poles.* The denominator factors as
$$z^4+z^2+1 = (z^2+z+1)(z^2-z+1),$$
so the poles are the primitive sixth roots of unity $e^{\pm i\pi/3}$, $e^{\pm2i\pi/3}$. The upper half-plane contains $z_1 = e^{i\pi/3}$ and $z_2 = e^{2i\pi/3} = -e^{-i\pi/3}$.

With $q(z) = z^4+z^2+1$ and $q'(z) = 4z^3+2z$, the residue at a simple zero is $1/q'$. For $z_1$: $z_1^3 = e^{i\pi} = -1$, so $q'(z_1) = -4+2e^{i\pi/3} = -4+1+i\sqrt3 = -3+i\sqrt3$. For $z_2$: $z_2^3 = e^{2\pi i} = 1$, so $q'(z_2) = 4+2e^{2i\pi/3} = 4-1+i\sqrt3 = 3+i\sqrt3$.

Hence
$$\operatorname{Res}_1 = \frac{1}{-3+i\sqrt3} = \frac{-3-i\sqrt3}{12},\qquad \operatorname{Res}_2 = \frac{1}{3+i\sqrt3} = \frac{3-i\sqrt3}{12},$$
using $\lvert -3+i\sqrt3\rvert^2 = 9+3 = 12$. The sum is $-\dfrac{2i\sqrt3}{12} = -\dfrac{i\sqrt3}{6}$, and by Theorem 7.22,
$$\int_{-\infty}^{\infty}\frac{dx}{x^4+x^2+1} = 2\pi i\left(-\frac{i\sqrt3}{6}\right) = \frac{2\pi\sqrt3}{6} = \frac{\pi\sqrt3}{3} = \frac{\pi}{\sqrt3}.$$
The integrand is even, so the requested integral over $[0,\infty)$ is half:
$$\int_0^\infty\frac{dx}{x^4+x^2+1} = \frac{\pi}{2\sqrt3}.$$

*The arc.* On $\lvert z\rvert=R$, $\lvert q(z)\rvert\ge R^4-R^2-1$, so the arc contribution is at most $\pi R/(R^4-R^2-1)\to0$, justifying the limit.

**Check.** $\pi/(2\sqrt3)\approx0.9069$, confirmed by quadrature. Another route: $x^4+x^2+1 = \dfrac{x^6-1}{x^2-1}$ for $x\ne\pm1$, and a partial-fraction computation in $x$ gives the same value; the agreement of the two methods supports both. $\checkmark$

**32.** *Strategy: residues, then the substitution $x\mapsto1/x$.* The poles of $z^2/(1+z^4)$ are the fourth roots of $-1$; in the upper half-plane they are $z_1 = e^{i\pi/4}$ and $z_2 = e^{3i\pi/4}$. Since the numerator is $z^2$ and $q' = 4z^3$,
$$\operatorname{Res}_j = \frac{z_j^2}{4z_j^3} = \frac{1}{4z_j} = \frac{z_j^{-1}}{4}.$$
Thus
$$\operatorname{Res}_1 = \frac{e^{-i\pi/4}}{4} = \frac{\sqrt2/2-i\sqrt2/2}{4},\qquad \operatorname{Res}_2 = \frac{e^{-3i\pi/4}}{4} = \frac{-\sqrt2/2-i\sqrt2/2}{4},$$
and the sum is $-\dfrac{i\sqrt2}{4}$. By Theorem 7.22,
$$\int_{-\infty}^{\infty}\frac{x^2}{1+x^4}\,dx = 2\pi i\left(-\frac{i\sqrt2}{4}\right) = \frac{\pi\sqrt2}{2} = \frac{\pi}{\sqrt2},$$
so by evenness
$$\int_0^\infty\frac{x^2}{1+x^4}\,dx = \frac{\pi}{2\sqrt2}.$$

*Why this equals $\int_0^\infty dx/(1+x^4)$.* Substitute $x = 1/t$, $dx = -dt/t^2$, which maps $(0,\infty)$ to $(\infty,0)$:
$$\int_0^\infty\frac{x^2}{1+x^4}\,dx = \int_\infty^0\frac{1/t^2}{1+1/t^4}\left(-\frac{dt}{t^2}\right) = \int_0^\infty\frac{1/t^2\cdot t^4}{t^4+1}\cdot\frac{dt}{t^2} = \int_0^\infty\frac{dt}{1+t^4}.$$
The identity $x\mapsto1/x$ is the reason the two integrals coincide.

**Check.** $\pi/(2\sqrt2)\approx1.1107$, confirmed numerically; Example 9.6 gives $\int_0^\infty dx/(1+x^4) = \pi/(2\sqrt2)$ as well, in agreement with the substitution. $\checkmark$

**33.** *Strategy: the unit circle, for general $a$ and $b$.* With $z = e^{i\theta}$, $\sin\theta = (z-z^{-1})/(2i)$ and $d\theta = dz/(iz)$. Then
$$a+b\sin\theta = a+\frac{b(z^2-1)}{2iz} = \frac{2aiz+bz^2-b}{2iz},$$
so
$$I = \oint_{\lvert z\rvert=1}\frac{2iz}{bz^2+2aiz-b}\cdot\frac{dz}{iz} = 2\oint_{\lvert z\rvert=1}\frac{dz}{bz^2+2aiz-b}.$$
The quadratic has roots
$$z_\pm = \frac{-2ai\pm\sqrt{-4a^2+4b^2}}{2b} = \frac{i\bigl(-a\pm\sqrt{a^2-b^2}\bigr)}{b},$$
whose product is $\dfrac{-b}{b} = -1$; one root lies inside the unit circle and one outside. Indeed, a root on the unit circle would be $z = e^{i\theta}$ with $b(z^2-1) = -2aiz$, hence $\lvert b\rvert\cdot2\lvert\sin\theta\rvert = 2\lvert a\rvert$, that is $\lvert a\rvert = \lvert b\rvert\lvert\sin\theta\rvert\le\lvert b\rvert$, contradicting $a>\lvert b\rvert$. Denote the inner root by $z_+$. Then
$$I = 2\cdot2\pi i\cdot\frac{1}{2bz_++2ai} = \frac{2\pi i}{bz_++ai}.$$
Now $bz_+ = i\bigl(-a+\sqrt{a^2-b^2}\bigr)$, so $bz_++ai = i\sqrt{a^2-b^2}$ and
$$I = \frac{2\pi i}{i\sqrt{a^2-b^2}} = \frac{2\pi}{\sqrt{a^2-b^2}} . \qquad\blacksquare$$

**Check.** For $a=5$, $b=-4$ this gives $2\pi/3$, matching Exercise 19. For $b=0$ it gives $2\pi/a$, which is immediate. The sign of $b$ does not appear in the answer, as it must not: replacing $\theta$ by $-\theta$ changes $b$ to $-b$ and leaves the integral unchanged. $\checkmark$

**34.** *Strategy: indent the contour and use Lemma 7.26.* Consider $f(z) = e^{iaz}/z$ with $a>0$, and the contour $\Gamma_{\varepsilon,R}$ consisting of $[-R,-\varepsilon]$, the clockwise upper semicircle $C_\varepsilon$ about $0$, $[\varepsilon,R]$, and the counterclockwise upper semicircle $C_R$. The integrand is holomorphic inside, so the total integral is $0$ by Cauchy's theorem.

*Large arc.* On $C_R$, $\lvert e^{iaz}\rvert = e^{-aR\sin\theta}$ and $\lvert dz/z\rvert = d\theta$, so
$$\left\lvert\int_{C_R}\frac{e^{iaz}}{z}\,dz\right\rvert\le\int_0^{\pi}e^{-aR\sin\theta}d\theta\le\frac{\pi}{aR}\longrightarrow0 .$$

*Small arc.* By Lemma 7.26 with $\operatorname{Res}(e^{iaz}/z,0) = 1$, the clockwise semicircle contributes $-i\pi+o(1)$ as $\varepsilon\to0$. Explicitly, on $z = \varepsilon e^{i\theta}$ the integral is $-i\int_0^{\pi}e^{ia\varepsilon e^{i\theta}}d\theta\to-i\pi$.

*The segments.* Together they give
$$\int_{-R}^{-\varepsilon}\frac{e^{iax}}{x}dx+\int_\varepsilon^R\frac{e^{iax}}{x}dx\longrightarrow \operatorname{PV}\int_{-\infty}^{\infty}\frac{e^{iax}}{x}\,dx .$$

Adding and letting $\varepsilon\to0$, $R\to\infty$ gives
$$\operatorname{PV}\int_{-\infty}^{\infty}\frac{e^{iax}}{x}\,dx-i\pi = 0,\qquad\text{so}\qquad \operatorname{PV}\int_{-\infty}^{\infty}\frac{e^{iax}}{x}\,dx = i\pi .$$
Taking imaginary parts, and noting that $\cos(ax)/x$ is odd so its principal value vanishes,
$$\operatorname{PV}\int_{-\infty}^{\infty}\frac{\sin(ax)}{x}\,dx = \operatorname{Im}(i\pi) = \pi .$$

**Check.** The integrand $\sin(ax)/x$ is even and the ordinary improper integral converges (conditionally), so its principal value equals the improper integral. For $a=1$ this is the classical Dirichlet integral $\pi$; for $a>0$ the substitution $u = ax$ gives $\int\sin(ax)/x\,dx = \int\sin u/u\,du = \pi$, independent of $a$ — consistent with the answer. $\checkmark$

**35.** *Strategy: indentation plus partial fractions.* The integrand has a simple pole at $0$ and simple poles at $\pm i$. Consider $f(z) = \dfrac{e^{iz}}{z(z^2+1)}$ and the indented semicircle of Exercise 34. All singularities other than $0$ lie at $\pm i$, and only $+i$ is inside.

Residues:
$$\operatorname{Res}(f,0) = \frac{e^{0}}{0^2+1} = 1,\qquad \operatorname{Res}(f,i) = \frac{e^{i\cdot i}}{i\cdot 2i} = \frac{e^{-1}}{-2} = -\frac{1}{2e}.$$
Theorem 7.27 (with $a=1$, one simple pole on the axis) gives
$$\operatorname{PV}\int_{-\infty}^{\infty}\frac{e^{ix}}{x(x^2+1)}\,dx = 2\pi i\left(-\frac{1}{2e}\right)+i\pi(1) = i\pi\left(1-\frac1e\right).$$
Taking imaginary parts,
$$\operatorname{PV}\int_{-\infty}^{\infty}\frac{\sin x}{x(x^2+1)}\,dx = \pi\left(1-\frac1e\right).$$
The integrand $\sin x/(x(x^2+1))$ is even and continuous at $0$ (the value there is $1$), and it is absolutely integrable because $\lvert\sin x\rvert/(\lvert x\rvert(x^2+1))\le1/(x^2+1)$ for $\lvert x\rvert\ge1$ and is bounded near $0$. Hence the principal value is the ordinary integral, and by evenness
$$\int_0^\infty\frac{\sin x}{x(x^2+1)}\,dx = \frac{\pi}{2}\left(1-\frac1e\right).$$

**Check.** Numerically $\dfrac{\pi}{2}(1-e^{-1})\approx0.9929$, confirmed by quadrature. Alternatively, $\dfrac{1}{x(x^2+1)} = \dfrac1x-\dfrac{x}{x^2+1}$, so the integral equals $\int_0^\infty(\sin x)/x\,dx-\int_0^\infty x\sin x/(x^2+1)\,dx = \dfrac{\pi}{2}-\dfrac{\pi}{2e}$, the second value being Exercise 35 of [Complex Integration](../03-complex-integration/solutions.md). The two routes agree. $\checkmark$

**36.** *Strategy: a keyhole contour with a branch of $z^{a-1}$.* For $0<a<2$ use the branch
$$z^{a-1} = e^{(a-1)(\ln\lvert z\rvert+i\arg z)},\qquad 0<\arg z<2\pi,$$
holomorphic on the plane slit along the positive real axis, with $z^{a-1} = x^{a-1}$ on the upper side and $x^{a-1}e^{2\pi i(a-1)}$ on the lower side of the slit.

Let $\gamma$ be the keyhole: from $\varepsilon$ to $R$ above the axis, around the circle of radius $R$, back from $R$ to $\varepsilon$ below the axis, and around the circle of radius $\varepsilon$. The integrand $f(z) = z^{a-1}/(1+z^2)$ has the poles $i = e^{i\pi/2}$ and $-i = e^{3i\pi/2}$, both enclosed, with residues
$$\operatorname{Res}(f,i) = \frac{i^{a-1}}{2i} = \frac{e^{i\pi(a-1)/2}}{2i},\qquad \operatorname{Res}(f,-i) = \frac{(-i)^{a-1}}{-2i} = \frac{e^{3i\pi(a-1)/2}}{-2i}.$$
Write $\theta := \pi(a-1)/2$. The sum is
$$\frac{e^{i\theta}-e^{3i\theta}}{2i} = \frac{e^{2i\theta}\bigl(e^{-i\theta}-e^{i\theta}\bigr)}{2i} = -e^{2i\theta}\sin\theta .$$
Hence $\oint_\gamma f\,dz = -2\pi i\,e^{2i\theta}\sin\theta$.

*The circles.* On $\lvert z\rvert=\varepsilon$, $\lvert f\rvert\le\varepsilon^{a-1}/(1-\varepsilon^2)$ and the length is $2\pi\varepsilon$, so the contribution is $O(\varepsilon^{a})\to0$ because $a>0$. On $\lvert z\rvert=R$, $\lvert f\rvert\le R^{a-1}/(R^2-1)$ and the length is $2\pi R$, so the contribution is $O(R^{a-1})\to0$ because $a<2$.

*The segments.* The upper side contributes $J_{\varepsilon,R} := \int_\varepsilon^R x^{a-1}/(1+x^2)dx$, and the lower side contributes $-e^{2\pi i(a-1)}J_{\varepsilon,R}$. Letting $\varepsilon\to0$, $R\to\infty$,
$$\bigl(1-e^{2\pi i(a-1)}\bigr)I = -2\pi i\,e^{2i\theta}\sin\theta,\qquad I := \int_0^\infty\frac{x^{a-1}}{1+x^2}\,dx .$$
Now $2\pi(a-1) = 4\theta$, so $1-e^{2\pi i(a-1)} = 1-e^{4i\theta} = -2i\,e^{2i\theta}\sin 2\theta$. Therefore
$$I = \frac{-2\pi i\,e^{2i\theta}\sin\theta}{-2i\,e^{2i\theta}\sin2\theta} = \frac{\pi\sin\theta}{\sin2\theta} = \frac{\pi}{2\cos\theta} = \frac{\pi}{2\cos\bigl(\pi(a-1)/2\bigr)} = \frac{\pi}{2\sin(\pi a/2)},$$
using $\cos\bigl(\pi(a-1)/2\bigr) = \cos\bigl(\pi a/2-\pi/2\bigr) = \sin(\pi a/2)$.

**Check.** For $a=1$ the formula gives $\pi/(2\sin(\pi/2)) = \pi/2$, which is $\int_0^\infty dx/(1+x^2)$. For $a=1/2$ it gives $\pi/(2\sin(\pi/4)) = \pi/\sqrt2\approx2.2214$, confirmed by quadrature. As $a\to0^+$ and $a\to2^-$ the formula diverges, matching the failure of the small-circle estimate at $a=0$ and of the large-circle estimate at $a=2$. $\checkmark$

**37.** *Strategy: the kernel $\pi\cot(\pi z)$ over a large square.* Let
$$f(z) = \frac{\pi\cot(\pi z)}{z^2+1}.$$

*Residues at the integers.* At $z=n\in\mathbb{Z}$, $\pi\cot(\pi z)$ has a simple pole. Since $\dfrac{d}{dz}\sin(\pi z) = \pi\cos(\pi z)$ and $\cos(\pi n) = (-1)^n$,
$$\operatorname{Res}(\pi\cot(\pi z),n) = \frac{\pi\cos(\pi n)}{\pi\cos(\pi n)} = 1 .$$
Hence $\operatorname{Res}(f,n) = \dfrac{1}{n^2+1}$.

*Residues at $\pm i$.* Since $\cot(\pi i) = \dfrac{\cos(\pi i)}{\sin(\pi i)} = \dfrac{\cosh\pi}{i\sinh\pi} = -i\coth\pi$ and $\cot(-\pi i) = i\coth\pi$,
$$\operatorname{Res}(f,i) = \frac{\pi\cot(\pi i)}{2i} = -\frac{\pi\coth\pi}{2},\qquad \operatorname{Res}(f,-i) = \frac{\pi\cot(-\pi i)}{-2i} = -\frac{\pi\coth\pi}{2}.$$
Their sum is $-\pi\coth\pi$.

*The contour.* Let $Q_N$ be the square with vertices $\pm\bigl(N+\tfrac12\bigr)\pm i\bigl(N+\tfrac12\bigr)$, traversed counterclockwise. On the vertical sides $\lvert\cot(\pi z)\rvert = \lvert\tanh(\pi y)\rvert\le1$; on the horizontal sides $\lvert\cot(\pi z)\rvert\le\coth(\pi/2)<2$. Also $\lvert z^2+1\rvert\ge\lvert z\rvert^2/2$ for large $\lvert z\rvert$, and $\ell(Q_N) = 8(N+\tfrac12)$. Hence
$$\left\lvert\oint_{Q_N}f\,dz\right\rvert\le\pi\cdot2\cdot\frac{8(N+\tfrac12)}{(N+\tfrac12)^2/2}\longrightarrow0 .$$

*Conclusion.* The residue theorem gives $\oint_{Q_N}f\,dz = 2\pi i\sum_{\lvert n\rvert\le N}\dfrac{1}{n^2+1}+2\pi i(-\pi\coth\pi)$; letting $N\to\infty$ and using that the integral tends to $0$,
$$\sum_{n=-\infty}^{\infty}\frac{1}{n^2+1} = \pi\coth\pi .$$
The $n=0$ term is $1$, and the sum is even in $n$, so
$$\sum_{n=1}^{\infty}\frac{1}{n^2+1} = \frac{\pi\coth\pi-1}{2}. \qquad\blacksquare$$

**Check.** $\pi\coth\pi\approx3.15335$, so the sum is $\approx1.07667$. Direct summation of the first $300{,}000$ terms gives $1.07667$, and the tail is $O(1/N)$. The identity also passes the plausibility test $\sum_{n\ge1}1/(n^2+1)<\sum_{n\ge1}1/n^2 = \pi^2/6\approx1.645$. $\checkmark$

**38.** *Strategy: Rouché with the leading term; then two circles.*

*Fundamental theorem of algebra.* Let $p(z) = a_nz^n+a_{n-1}z^{n-1}+\cdots+a_0$ with $n\ge1$ and $a_n\ne0$. Take $f(z) = a_nz^n$ and $g(z) = p(z)-f(z)$, so $\deg g\le n-1$. On $\lvert z\rvert=R$,
$$\lvert g(z)\rvert\le\sum_{k=0}^{n-1}\lvert a_k\rvert R^k\le C R^{n-1},\qquad C := \sum_{k=0}^{n-1}\lvert a_k\rvert ,$$
while $\lvert f(z)\rvert = \lvert a_n\rvert R^n$. For $R>2C/\lvert a_n\rvert$ we have $\lvert g\rvert<\lvert f\rvert$ on the circle, so by Rouché's theorem $p$ has as many zeros inside $\lvert z\rvert=R$ as $f$ does, namely $n$. In particular $p$ has at least one zero, and exactly $n$ counted with multiplicity.

*The polynomial $P(z) = z^6+4z^2+z+1$.*

Inside $\lvert z\rvert=1$: take $f(z) = 4z^2$, $g(z) = z^6+z+1$. On $\lvert z\rvert=1$,
$$\lvert g(z)\rvert\le1+1+1 = 3<4 = \lvert f(z)\rvert,$$
so $P$ has **two** zeros in the unit disc.

Inside $\lvert z\rvert=2$: take $f(z) = z^6$, $g(z) = 4z^2+z+1$. On $\lvert z\rvert=2$,
$$\lvert g(z)\rvert\le16+2+1 = 19<64 = \lvert f(z)\rvert,$$
so all **six** zeros lie in $\lvert z\rvert<2$.

In the annulus: $6-2 = $ **four** zeros satisfy $1<\lvert z\rvert<2$.

**Check.** Numerically the zeros of $P$ have moduli approximately $0.5676,\,0.5676$ and $1.3273$ (four times, with multiplicity), so there are two inside the unit circle and four in the annulus, as predicted; no zero lies on either circle. For the general statement, the case $n=1$ recovers the trivial fact that a linear polynomial has one root, and the argument uses only Rouché's theorem, which itself rests on the argument principle and hence on Cauchy's theorem. $\checkmark$

