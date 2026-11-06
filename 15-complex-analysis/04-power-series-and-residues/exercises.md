# Power Series and Residues — Exercises

> [Tutorial](README.md) · 38 problems · Levels: Beginner, Intermediate, Advanced, Challenge

Attempt every problem on paper before consulting [solutions.md](solutions.md). You may use any result
proved in the [tutorial](README.md). Before computing any residue, state the singularity, its type and
its order; before any contour integral, state the contour, its orientation and which singularities it
encloses. Where a numerical answer is a familiar constant, check it against an independent computation.

## Beginner

**1.** Find the radius of convergence of (a) $\sum z^n/n!$; (b) $\sum n!\,z^n$; (c) $\sum z^n/2^n$; (d) $\sum (z-1)^n/n^2$.

**2.** Expand $e^{2z}$ in powers of $z$, and then in powers of $z-1$. State the radius of each series.

**3.** Expand $\dfrac{1}{1+z}$ in powers of $z$ and state the radius. Use the series to compute $\sum_{n\ge0}(-1)^n/2^n$ and compare with the value of the function at $z=1/2$.

**4.** Expand $\dfrac{1}{2-z}$ in powers of $z$ and state the radius.

**5.** Let $f(z) = \dfrac{1}{z(z-2)}$. Expand $f$ in powers of $z$ on the annuli $0<\lvert z\rvert<2$ and $2<\lvert z\rvert<\infty$. In each case state the coefficient of $z^{-1}$ and explain its meaning in terms of residues.

**6.** Expand $e^{1/z}$ on $0<\lvert z\rvert<\infty$ and read off $\operatorname{Res}(e^{1/z},0)$.

**7.** Classify the singularity at $0$: (a) $\dfrac{1-\cos z}{z^2}$; (b) $\dfrac{\cos z}{z^3}$; (c) $e^{1/z^2}$; (d) $\dfrac{\sin z}{z^4}$.

**8.** Compute the residues: (a) $\dfrac{1}{z^2+1}$ at $i$; (b) $\dfrac{z}{z-3}$ at $3$; (c) $\dfrac{e^z}{z-1}$ at $1$; (d) $\dfrac{z^2+1}{z-1}$ at $1$.

**9.** Compute $\operatorname{Res}\Bigl(\dfrac{1}{z(z-1)},0\Bigr)$ and $\operatorname{Res}\Bigl(\dfrac{1}{z(z-1)},1\Bigr)$, and verify that their sum is $0$.

**10.** Compute $\displaystyle\oint_{\lvert z\rvert=2}\frac{dz}{z^2+1}$ using residues.

**11.** Compute $\displaystyle\oint_{\lvert z\rvert=2}\frac{z+3}{z-1}\,dz$.

**12.** Compute $\displaystyle\oint_{\lvert z\rvert=1}\frac{\cos z}{z^2}\,dz$.

## Intermediate

**13.** Compute the residues of $\dfrac{1}{(z^2+1)^2}$ at $i$ and at $-i$.

**14.** Compute $\operatorname{Res}\Bigl(\dfrac{e^{2z}}{(z-1)^3},1\Bigr)$.

**15.** Compute $\operatorname{Res}\Bigl(\dfrac{z^2}{(z^2+1)^2},i\Bigr)$.

**16.** Compute the residues of $\tan z$ at $z=\pi/2$.

**17.** Compute $\displaystyle\oint_{\lvert z\rvert=1}\frac{dz}{z^2(z-2)}$.

**18.** Compute $\displaystyle\oint_{\lvert z\rvert=2}\frac{z^2+1}{z(z-1)(z-3)}\,dz$.

**19.** Evaluate $\displaystyle\int_0^{2\pi}\frac{\sin^2\theta}{5-4\cos\theta}\,d\theta$.

**20.** Evaluate $\displaystyle\int_0^{2\pi}\frac{\cos 3\theta}{5-4\cos\theta}\,d\theta$.

**21.** Evaluate $\displaystyle\int_{-\infty}^{\infty}\frac{dx}{x^2+2x+5}$.

**22.** Evaluate $\displaystyle\int_{-\infty}^{\infty}\frac{dx}{(1+x^2)^2}$.

## Advanced

**23.** Let $f$ be holomorphic on $0<\lvert z-z_0\rvert<\rho$ and suppose that for some constants $C>0$ and $0\le\alpha<1$,
$$\lvert f(z)\rvert\le C\lvert z-z_0\rvert^{-\alpha}$$
on that punctured disc. Prove that $z_0$ is a removable singularity. Show that the conclusion fails for $\alpha=1$ by exhibiting $f(z) = 1/z$ at $z_0=0$.

**24.** Let $f$ be holomorphic on $0<\lvert z-z_0\rvert<\rho$ and suppose $\lvert f(z)\rvert\to\infty$ as $z\to z_0$. Prove that $z_0$ is a pole, and prove that its order is the smallest integer $m$ for which $(z-z_0)^mf(z)$ remains bounded near $z_0$.

**25.** Prove the Casorati–Weierstrass theorem: if $z_0$ is an essential singularity of $f$, then for every $\delta>0$ the set $f(\{0<\lvert z-z_0\rvert<\delta\})$ is dense in $\mathbb{C}$.

**26.** Prove the argument principle: for $f$ meromorphic inside and on a positively oriented simple closed contour $\gamma$, with no zeros or poles on $\gamma$,
$$\frac{1}{2\pi i}\oint_\gamma\frac{f'(z)}{f(z)}\,dz = Z-P .$$

**27.** Determine the number of zeros of $P(z) = z^4+3z+1$ in $\lvert z\rvert<1$, in $\lvert z\rvert<2$, and in the annulus $1<\lvert z\rvert<2$.

**28.** Determine the number of zeros of $P(z) = z^5-6z+3$ in $\lvert z\rvert<1$, in $\lvert z\rvert<2$, and in the annulus $1<\lvert z\rvert<2$.

**29.** Compute the residue at infinity of (a) $\dfrac{1}{z}$; (b) $\dfrac{z}{z-1}$; (c) $\dfrac{1}{z^2+1}$; (d) $\dfrac{z^3}{z^2+1}$. Check each answer against the total-residue identity.

**30.** Let $p/q$ be a rational function with $\deg q\ge\deg p+2$. Prove that $\operatorname{Res}(p/q,\infty) = 0$, and deduce from the total-residue theorem that the sum of the residues at the finite poles is $0$.

## Challenge

**31.** Evaluate $\displaystyle\int_0^\infty\frac{dx}{x^4+x^2+1}$ by residues.

**32.** Evaluate $\displaystyle\int_0^\infty\frac{x^2}{x^4+1}\,dx$ by residues, and explain why the answer equals $\displaystyle\int_0^\infty\frac{dx}{x^4+1}$.

**33.** For real $a>\lvert b\rvert$, prove that
$$\int_0^{2\pi}\frac{d\theta}{a+b\sin\theta} = \frac{2\pi}{\sqrt{a^2-b^2}} .$$

**34.** For $a>0$, prove that
$$\operatorname{PV}\int_{-\infty}^{\infty}\frac{\sin(ax)}{x}\,dx = \pi,$$
by indenting the contour around the pole at $0$.

**35.** Evaluate $\displaystyle\int_0^\infty\frac{\sin x}{x(x^2+1)}\,dx$.

**36.** For $0<a<2$, prove that
$$\int_0^\infty\frac{x^{a-1}}{1+x^2}\,dx = \frac{\pi}{2\sin(\pi a/2)} .$$

**37.** Prove that
$$\sum_{n=1}^{\infty}\frac{1}{n^2+1} = \frac{\pi\coth\pi-1}{2},$$
by applying the residue theorem to $\dfrac{\pi\cot(\pi z)}{z^2+1}$ over a large square.

**38.** Prove the fundamental theorem of algebra using Rouché's theorem, and then determine the number of zeros of $P(z) = z^6+4z^2+z+1$ in $\lvert z\rvert<1$, in $\lvert z\rvert<2$, and in the annulus $1<\lvert z\rvert<2$.
