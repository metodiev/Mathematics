# Complex Integration — Exercises

> [Tutorial](README.md) · 38 problems · Levels: Beginner, Intermediate, Advanced, Challenge

Attempt every problem on paper before consulting [solutions.md](solutions.md). You may use any result
proved in the [tutorial](README.md). For every integral, look for a primitive, for a closed contour, or
for an application of Cauchy's integral formula *before* parametrising; a parametrisation is the last
resort, not the first. Where a numerical answer is a familiar constant, check it against an independent
computation (a real antiderivative, a symmetry, or an estimate).

## Beginner

**1.** Parametrise the segment $\gamma$ from $1-i$ to $3+2i$ and compute $\displaystyle\int_\gamma z\,dz$ from the definition. Then recompute it using a primitive.

**2.** Compute $\displaystyle\int_\gamma dz$ where $\gamma$ is any contour from $0$ to $2-i$. Explain why the answer does not depend on the contour.

**3.** Compute $\displaystyle\oint_{\lvert z\rvert=2}\left(z^3+\frac1z\right)dz$.

**4.** Compute $\displaystyle\oint_{\lvert z\rvert=1}\bar z\,dz$, where the circle is traversed counterclockwise. Is the integrand holomorphic?

**5.** Compute the lengths of (a) the circle $\lvert z-1\rvert=3$; (b) the segment from $2i$ to $-1$; (c) the polygonal path $0\to1\to1+i$.

**6.** Compute $\displaystyle\int_\gamma z^2\,dz$ where $\gamma$ is the straight segment from $i$ to $1$.

**7.** Compute $\displaystyle\int_\gamma(2z+3)\,dz$ where $\gamma$ is the arc of the parabola $y=x^2$ from $0$ to $1+i$.

**8.** Compute $\displaystyle\oint_{\lvert z-2\rvert=1}\frac{dz}{z-2}$ and $\displaystyle\oint_{\lvert z-2\rvert=1}\frac{dz}{z-5}$. Explain the difference.

**9.** Compute $\displaystyle\oint_{\lvert z-1\rvert=1}\frac{dz}{z^2-1}$. Before computing, decide which poles lie inside the contour.

**10.** Use the ML inequality to bound $\displaystyle\left\lvert\oint_{\lvert z\rvert=1}\frac{e^z}{z^2+3}\,dz\right\rvert$. State the maximum and the length you used.

**11.** Compute $\displaystyle\oint_{\lvert z\rvert=1}\left(2\bar z+\frac3z\right)dz$.

**12.** Let $\gamma_1$ be the segment from $0$ to $1+i$ and let $\gamma_2$ be the path $0\to1\to1+i$. Compute $\int_{\gamma_1}\operatorname{Re}z\,dz$ and $\int_{\gamma_2}\operatorname{Re}z\,dz$. What do you conclude about the existence of a primitive of $\operatorname{Re}z$?

## Intermediate

**13.** Compute $\displaystyle\oint_{\lvert z\rvert=2}\frac{z^2+1}{z-1}\,dz$.

**14.** Compute $\displaystyle\oint_{\lvert z\rvert=1}\frac{\cos z}{z}\,dz$.

**15.** Compute $\displaystyle\oint_{\lvert z\rvert=3}\frac{z+1}{z^2+4}\,dz$ in two ways: by partial fractions, and by writing the integrand as a sum of two terms each handled by the integral formula.

**16.** Compute $\displaystyle\oint_{\lvert z\rvert=1}\frac{e^z}{z^2}\,dz$.

**17.** Compute $\displaystyle\oint_{\lvert z\rvert=2}\frac{\sin z}{z^4}\,dz$.

**18.** Compute $\displaystyle\oint_{\lvert z\rvert=2}\frac{dz}{z^2-1}$ and $\displaystyle\oint_{\lvert z\rvert=2}\frac{z\,dz}{z^2-1}$.

**19.** In a two-dimensional flow the complex potential is $\Omega(z)=\tfrac12\log(z^2-1)$, whose derivative is $\Omega'(z)=z/(z^2-1)$. Compute the circulation $\oint_{\lvert z\rvert=2}\Omega'(z)\,dz$ and explain why the two logarithmic singularities contribute equally.

**20.** For $R>1$ let $\gamma_R$ be the circle $\lvert z\rvert=R$. Show that
$$\left\lvert\oint_{\gamma_R}\frac{z}{z^2+1}\,dz\right\rvert\le\frac{2\pi R^2}{R^2-1},$$
and compute the integral exactly. Is the bound sharp as $R\to\infty$?

**21.** Compute $\displaystyle\int_\gamma\frac{dz}{z}$ where $\gamma$ is the upper semicircle of radius $1$ from $1$ to $-1$. Justify the use of a logarithm, and check the answer by parametrising.

**22.** Compute $\displaystyle\oint_{\lvert z\rvert=3}\frac{z+2}{z^2+1}\,dz$.

## Advanced

**23.** Let $f$ be holomorphic on a domain $\Omega$ and suppose $\lvert f\rvert$ is constant on $\Omega$. Prove that $f$ is constant. (Use the Cauchy–Riemann equations, not Liouville's theorem.)

**24.** Let $f$ be holomorphic and nowhere zero on a domain $\Omega$. Suppose $\lvert f\rvert$ attains a local minimum at an interior point. Prove that $f$ is constant.

**25.** Let $f$ be entire and suppose there is a real constant $M$ with $\operatorname{Re}f(z)\le M$ for all $z$. Prove that $f$ is constant.

**26.** Let $f$ be entire and suppose $\lvert f(z)\rvert\ge1$ for all $z$. Prove that $f$ is constant. Then explain — with a counterexample — why the condition cannot be relaxed to "$\lvert f(z)\rvert\ge c>0$ for all $z$ outside some compact set".

**27.** Let $\Omega$ be a domain, $z_0\in\Omega$, and let $f$ be holomorphic on $\Omega\setminus\{z_0\}$. Suppose there is $M$ with $\lvert f(z)\rvert\le M$ for all $z\ne z_0$ in a neighbourhood of $z_0$. Prove, using Morera's theorem, that $f$ extends to a holomorphic function on $\Omega$.

**28.** Let $f:D(0,1)\to D(0,1)$ be holomorphic with $f(0)=0=f'(0)$. Prove that $\lvert f(z)\rvert\le\lvert z\rvert^2$ for $\lvert z\rvert<1$.

**29.** Let $f$ be holomorphic on $D(0,R)$ with $\lvert f(z)\rvert\le M$ there, and suppose $f(0)=f'(0)=\cdots=f^{(n-1)}(0)=0$. Prove that
$$\lvert f(z)\rvert\le M\left(\frac{\lvert z\rvert}{R}\right)^{n},\qquad \lvert z\rvert<R .$$

**30.** Let $\Omega$ be a domain and let $f$ be holomorphic on $\Omega$ with $f'\equiv0$. Prove from Theorem 7.11 that $f$ is constant, and explain where connectedness of $\Omega$ is used.

## Challenge

**31.** Evaluate $\displaystyle\int_0^\infty\frac{dx}{(x^2+1)(x^2+4)}$ by a contour integral, and check the answer by partial fractions.

**32.** Evaluate $\displaystyle\int_0^{2\pi}\frac{d\theta}{5+4\cos\theta}$.

**33.** Evaluate $\displaystyle\int_0^{2\pi}\frac{\cos^2\theta}{5+4\cos\theta}\,d\theta$.

**34.** Evaluate $\displaystyle\int_{-\infty}^{\infty}\frac{\cos 2x}{x^2+1}\,dx$.

**35.** Evaluate $\displaystyle\int_0^\infty\frac{x\sin x}{x^2+1}\,dx$. Beware: the integrand is not absolutely integrable, so the justification of the arc estimate needs care.

**36.** Let $a\in\mathbb{R}$. By integrating $e^{-z^2}$ around the rectangle with vertices $-R,\ R,\ R+ia,\ -R+ia$ and letting $R\to\infty$, prove that
$$\int_{-\infty}^{\infty}e^{-x^2}\cos(2ax)\,dx=\sqrt{\pi}\,e^{-a^2},$$
taking the real Gaussian integral $\int_{-\infty}^{\infty}e^{-x^2}dx=\sqrt{\pi}$ as known.

**37.** For $0<a<1$, prove that
$$\int_0^\infty\frac{x^{a-1}}{1+x}\,dx=\frac{\pi}{\sin(\pi a)} .$$
Use a keyhole contour around the positive real axis and the branch $z^{a-1}=e^{(a-1)(\ln\lvert z\rvert+i\arg z)}$ with $0<\arg z<2\pi$.

**38.** Using the sector of angle $\pi/4$ and the fact that $e^{iz^2}$ is entire, prove that
$$\int_0^\infty\cos(x^2)\,dx=\int_0^\infty\sin(x^2)\,dx=\frac{\sqrt{2\pi}}{4},$$
taking $\int_0^\infty e^{-r^2}dr=\sqrt{\pi}/2$ as known.
