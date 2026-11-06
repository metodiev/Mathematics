# Improper Integrals — Solutions

> [Improper Integrals](README.md) · Solutions to the 36 problems in [exercises.md](exercises.md)

Every solution identifies the type of improper integral, writes the defining limit, justifies convergence
by a named test, and checks the value by differentiating the antiderivative or by an independent argument.
Pitfalls are flagged where the problem is built around one.

## Beginner

### Solution 1

*Type and limit.* First kind at infinity. For $R>1$,

$$\int_1^R x^{-3}dx=\left[-\frac{1}{2x^2}\right]_1^R
=-\frac{1}{2R^2}+\frac12\longrightarrow\frac12 .$$

*Check.* The $p$-test with $p=3>1$ gives $1/(p-1)=1/2$, in agreement. Differentiating $-1/(2x^2)$ gives
$x^{-3}$. ✓

### Solution 2

*Type and limit.* First kind at infinity. For $R>1$,

$$\int_1^R x^{-1/2}dx=\left[2\sqrt x\right]_1^R=2\sqrt R-2\longrightarrow+\infty .$$

Hence the integral diverges. *Check.* The $p$-test with $p=1/2\le1$ predicts divergence. The integrand tends
to $0$, but too slowly: the area of each unit interval $[n,n+1]$ is at least $1/\sqrt{n+1}$, and these
terms do not sum.

### Solution 3

*Type and limit.* Second kind at $0$. For $0<\varepsilon<1$,

$$\int_\varepsilon^1x^{-1/3}dx=\left[\frac32x^{2/3}\right]_\varepsilon^1
=\frac32\left(1-\varepsilon^{2/3}\right)\longrightarrow\frac32 .$$

*Check.* The $p$-test at zero with $p=1/3<1$ gives $1/(1-p)=3/2$, in agreement. The integrand is unbounded
at $0$, but the spike has finite area. Differentiating $\frac32x^{2/3}$ gives $x^{-1/3}$. ✓

### Solution 4

*Type and limit.* Second kind at $0$. For $0<\varepsilon<1$,

$$\int_\varepsilon^1x^{-2}dx=\left[-\frac1x\right]_\varepsilon^1=\frac1\varepsilon-1\longrightarrow+\infty .$$

The integral diverges. *Check.* The $p$-test at zero requires $p<1$; here $p=2$, so divergence is predicted.
The spike is too fat: for every $\varepsilon\in(0,1)$, the area from $\varepsilon$ to $1$ is
$1/\varepsilon-1$, which grows without bound as $\varepsilon\to0^+$.

### Solution 5

*Type and limit.* First kind at infinity. For $R>1$,

$$\int_1^Re^{-2x}dx=\left[-\frac12e^{-2x}\right]_1^R
=\frac12\left(e^{-2}-e^{-2R}\right)\longrightarrow\frac{e^{-2}}{2}.$$

*Check.* Differentiating $-\frac12e^{-2x}$ gives $e^{-2x}$. ✓ The value is positive and about $0.0677$.

### Solution 6

*Type and limit.* First kind at infinity. For $R>0$,

$$\int_0^Re^{-x/3}dx=\left[-3e^{-x/3}\right]_0^R=3\left(1-e^{-R/3}\right)\longrightarrow3 .$$

*Check.* This is $\int_0^\infty e^{-ax}dx=1/a$ with $a=1/3$, giving $3$. ✓

### Solution 7

*Type and limit.* First kind at $-\infty$. For $R<-1$,

$$\int_R^{-1}x^{-2}dx=\left[-\frac1x\right]_R^{-1}=1+\frac1R\longrightarrow1 .$$

*Check.* By symmetry $x\mapsto-x$, the integral equals $\int_1^{\infty}x^{-2}dx=1$. ✓

### Solution 8

*Type and limit.* First kind at infinity. For $R>1$,

$$\int_1^Rx^{-3/2}dx=\left[-2x^{-1/2}\right]_1^R=-\frac{2}{\sqrt R}+2\longrightarrow2 .$$

*Check.* The $p$-test with $p=3/2>1$ gives $1/(3/2-1)=2$. ✓

### Solution 9

*Type and limit.* Second kind at $4$. For $0<t<4$,

$$\int_0^t(4-x)^{-1/2}dx=\left[-2(4-x)^{1/2}\right]_0^t
=4-2\sqrt{4-t}\longrightarrow4 .$$

*Check.* The substitution $u=4-x$ turns the integral into $\int_0^4u^{-1/2}du=2\sqrt4=4$. ✓

### Solution 10

*Type and limit.* First kind at infinity. For $R>0$,

$$\int_0^R\frac{dx}{x^2+1}=\left[\arctan x\right]_0^R=\arctan R\longrightarrow\frac{\pi}{2}.$$

*Check.* Differentiating $\arctan x$ gives $1/(1+x^2)$. ✓ The area is finite because the integrand decays
like $x^{-2}$.

### Solution 11

*Type and limit.* First kind at infinity. For $R>0$, substitute $u=x^2$, $du=2x\,dx$:

$$\int_0^Rxe^{-x^2}dx=\frac12\int_0^{R^2}e^{-u}du
=\frac12\left(1-e^{-R^2}\right)\longrightarrow\frac12 .$$

*Check.* Differentiating $-\frac12e^{-x^2}$ gives $xe^{-x^2}$. ✓

### Solution 12

*Type and limit.* First kind at infinity. For $R>2$,

$$\int_2^Rx^{-5/2}dx=\left[-\frac23x^{-3/2}\right]_2^R
=0+\frac23\cdot2^{-3/2}=\frac{2}{3\cdot2\sqrt2}=\frac{1}{3\sqrt2}=\frac{\sqrt2}{6}.$$

*Check.* The $p$-test with $p=5/2>1$ predicts convergence and value
$\frac{2^{1-p}}{p-1}=\frac{2^{-3/2}}{3/2}=\frac{\sqrt2}{6}$. ✓

## Intermediate

### Solution 13

*Type and limit.* First kind at infinity. With $a=2$,

$$\int_0^R\frac{dx}{x^2+4}=\frac12\arctan\frac x2\Big|_0^R
=\frac12\arctan\frac R2\longrightarrow\frac12\cdot\frac\pi2=\frac\pi4 .$$

*Check.* Differentiating $\frac12\arctan(x/2)$ gives
$\frac12\cdot\frac{1/2}{1+x^2/4}=\frac{1}{x^2+4}$. ✓

### Solution 14

*Type and limit.* First kind at infinity. Substitute $u=x^2+1$, $du=2x\,dx$:

$$\int_0^R\frac{x}{(x^2+1)^2}dx=\frac12\int_1^{R^2+1}u^{-2}du
=\frac12\left(1-\frac{1}{R^2+1}\right)\longrightarrow\frac12 .$$

*Check.* Differentiating $-\frac{1}{2(x^2+1)}$ gives $x/(x^2+1)^2$. ✓

### Solution 15

*Type and limit.* First kind at infinity. Integrate by parts twice, or use $\Gamma(3)=2!=2$. Directly,
with $u=x^2$, $dv=e^{-x}dx$:

$$\int_0^Rx^2e^{-x}dx=\left[-x^2e^{-x}\right]_0^R+2\int_0^Rxe^{-x}dx .$$

The boundary term tends to $0$; by Solution 4 of Example 4 (or one more integration by parts),
$\int_0^\infty xe^{-x}dx=1$. Hence the integral is $2$.

*Check.* The general formula $\int_0^\infty x^ne^{-x}dx=n!$ gives $2!=2$. ✓

### Solution 16

*Type and limit.* Second kind at $0$ (because of $\ln x$). For $0<\varepsilon<1$, integrate by parts with
$u=\ln x$, $dv=\sqrt x\,dx$: $du=dx/x$, $v=\frac23x^{3/2}$,

$$\int_\varepsilon^1\sqrt x\,\ln x\,dx
=\left[\frac23x^{3/2}\ln x\right]_\varepsilon^1-\frac23\int_\varepsilon^1x^{1/2}dx
=-\frac23\varepsilon^{3/2}\ln\varepsilon-\frac23\cdot\frac23\left(1-\varepsilon^{3/2}\right).$$

As $\varepsilon\to0^+$, $\varepsilon^{3/2}\ln\varepsilon\to0$ (L'Hôpital), so the limit is $-\frac49$.

*Check.* Differentiate $\frac23x^{3/2}\ln x-\frac49x^{3/2}$:
$x^{1/2}\ln x+\frac23x^{1/2}-\frac23x^{1/2}=\sqrt x\ln x$. ✓ The value is negative because $\ln x<0$ on
$(0,1)$.

### Solution 17

*Type and limit.* Second kind at $0$. Integrate by parts with $u=\ln x$, $dv=x\,dx$: $du=dx/x$,
$v=x^2/2$,

$$\int_\varepsilon^1x\ln x\,dx
=\left[\frac{x^2}{2}\ln x\right]_\varepsilon^1-\frac12\int_\varepsilon^1x\,dx
=-\frac{\varepsilon^2}{2}\ln\varepsilon-\frac12\left(\frac12-\frac{\varepsilon^2}{2}\right).$$

As $\varepsilon\to0^+$, $\varepsilon^2\ln\varepsilon\to0$, so the limit is $-\frac14$.

*Check.* Differentiate $\frac{x^2}{2}\ln x-\frac{x^2}{4}$:
$x\ln x+\frac x2-\frac x2=x\ln x$. ✓

### Solution 18

*Type and limit.* First kind at infinity. Integrate by parts with $u=\ln x$, $dv=x^{-2}dx$: $du=dx/x$,
$v=-1/x$,

$$\int_1^R\frac{\ln x}{x^2}dx
=\left[-\frac{\ln x}{x}\right]_1^R+\int_1^R\frac{dx}{x^2}
=-\frac{\ln R}{R}+0+\left(1-\frac1R\right)\longrightarrow1 .$$

*Check.* $\ln R/R\to0$ by L'Hôpital. The integrand is positive on $(1,\infty)$? For $x>1$, $\ln x>0$, so
yes, and the value $1$ is positive. Differentiating $-\frac{\ln x}{x}-\frac1x$ gives
$\frac{\ln x}{x^2}$; verify:
$\frac{d}{dx}(-\frac{\ln x}{x}-\frac1x)=-\frac{1-\ln x}{x^2}+\frac1{x^2}=\frac{\ln x}{x^2}$. ✓

### Solution 19

*Type and limit.* First kind at infinity. Substitute $t=\sqrt x$, so $x=t^2$ and $dx=2t\,dt$:

$$\int_0^\infty e^{-\sqrt x}dx=\int_0^\infty e^{-t}2t\,dt=2\int_0^\infty te^{-t}dt=2 .$$

*Check.* $\int_0^\infty te^{-t}dt=1$ (the case $n=1$ of $\int_0^\infty t^ne^{-t}dt=n!$, or Example 4), so
the value is $2$. ✓

### Solution 20

*Type and limit.* First kind at infinity. Complete the square:
$x^2+x+1=(x+\frac12)^2+\frac34$, so with $a=\frac{\sqrt3}{2}$,

$$\int_0^R\frac{dx}{(x+\frac12)^2+\frac34}
=\frac{2}{\sqrt3}\arctan\left(\frac{2x+1}{\sqrt3}\right)\Bigg|_0^R
\longrightarrow\frac{2}{\sqrt3}\left(\frac\pi2-\frac\pi6\right)
=\frac{2}{\sqrt3}\cdot\frac\pi3=\frac{2\pi}{3\sqrt3}.$$

*Check.* Differentiating $\frac{2}{\sqrt3}\arctan((2x+1)/\sqrt3)$ gives
$\frac{2}{\sqrt3}\cdot\frac{2/\sqrt3}{1+(2x+1)^2/3}=\frac{4}{3+(2x+1)^2}=\frac{1}{x^2+x+1}$. ✓

### Solution 21

*Type and test.* First kind at infinity. Since $0\le\sin^2x\le1$,

$$0\le\frac{\sin^2x}{x^2}\le\frac{1}{x^2}\qquad(x\ge1).$$

The integral $\int_1^\infty x^{-2}dx=1$ converges, so the comparison test gives convergence of the given
integral.

*Check.* The integrand is non-negative, so no cancellation can occur; absolute convergence and convergence
coincide here. The value is not elementary, but convergence does not require it.

### Solution 22

*Type and test.* First kind at infinity. Since $e^x>0$ and $x>0$,
$x+e^x\ge e^x$, hence

$$0\le\frac{1}{x+e^x}\le e^{-x}\qquad(x\ge0).$$

The integral $\int_1^\infty e^{-x}dx=e^{-1}$ converges, so comparison gives convergence.

*Check.* The integrand decays like $e^{-x}$, faster than any power, so convergence is expected. The
integral is not elementary, but its convergence is decided.

## Advanced

### Solution 23

*Set-up.* The lower limit is $2$, so $\ln x\ge\ln2>0$ and $(\ln x)^p$ is continuous and bounded on
$[2,e]$ for every real $p$. There is no finite singularity; only the behaviour at infinity matters.

*At infinity.* For any $p\in\mathbb{R}$, $(\ln x)^p=o(x^{1/2})$ as $x\to\infty$, by the growth hierarchy
$\ln x\ll x^\varepsilon$. Hence there is $C$ with $0\le(\ln x)^p\le Cx^{1/2}$ for $x\ge2$, and

$$0\le\frac{(\ln x)^p}{x^2}\le\frac{Cx^{1/2}}{x^2}=\frac{C}{x^{3/2}}.$$

The integral $\int_2^\infty Cx^{-3/2}dx$ converges by the $p$-test with $p=3/2>1$. Comparison gives
convergence for every real $p$.

*Check.* For $p=0$ the integral is $\int_2^\infty x^{-2}dx=1/2$. For $p>0$ the logarithm grows, but slower
than any positive power, so it cannot destroy the $x^{-2}$ decay. For $p<0$ the logarithmic factor actually
decays, which only helps. ✓

### Solution 24

*Convergence.* Split at $1$.

Near $0$: $e^{-x}\to1$, so $x^ae^{-x}\sim x^a$. The integral $\int_0^1x^adx$ converges iff $a>-1$ by the
$p$-test at zero with $p=-a<1$.

At infinity: since polynomial growth is dominated by exponential decay, there is $C$ with
$x^ae^{-x}\le Ce^{-x/2}$ for $x\ge1$. The integral $\int_1^\infty e^{-x/2}dx=2e^{-1/2}$ converges, so
comparison gives convergence for every $a$.

Hence the integral converges exactly when $a>-1$.

*Value.* By the definition of the gamma function,
$$\int_0^\infty x^ae^{-x}dx=\Gamma(a+1)\qquad(a>-1).$$

*Check.* For $a=n\in\mathbb{N}_0$, this is $\Gamma(n+1)=n!$, the standard factorial integral. For
$a=-1/2$, it is $\Gamma(1/2)=\sqrt\pi$.

### Solution 25

*Near zero.* For $p>0$, $x^p\to0$, so $1/(1+x^p)\to1$; for $p=0$ it is $1/2$; for $p<0$, $x^p\to\infty$ and
the integrand tends to $0$. In every case the integrand is bounded near $0$, so there is no singularity at
$0$. Only infinity matters.

*At infinity, $p>1$.* For $x\ge1$, $1+x^p\ge x^p$, so
$0\le1/(1+x^p)\le x^{-p}$. Since $\int_1^\infty x^{-p}dx$ converges for $p>1$, comparison gives
convergence.

*At infinity, $p\le1$.* If $0<p\le1$, then for $x\ge1$, $1+x^p\le2x^p$, so
$1/(1+x^p)\ge\frac{1}{2}x^{-p}$. Since $\int_1^\infty x^{-p}dx$ diverges for $p\le1$, comparison gives
divergence. If $p=0$ the integrand is $1/2$, which diverges. If $p<0$, then $x^p\le1$ for $x\ge1$, so
$1/(1+x^p)\ge1/2$, and the integral diverges.

Hence convergence exactly for $p>1$. *Check.* For $p=2$, the value is $\pi/2$ (Solution 13 with $a=1$); for
$p=1$, the integrand is $1/(1+x)$, whose integral is $\ln(1+R)\to\infty$, consistent with divergence.

### Solution 26

*Convergence.* For $R>1$, integrate by parts with $u=1/x$, $dv=\cos x\,dx$: $du=-dx/x^2$, $v=\sin x$,

$$\int_1^R\frac{\cos x}{x}dx
=\left[\frac{\sin x}{x}\right]_1^R+\int_1^R\frac{\sin x}{x^2}dx
=\frac{\sin R}{R}-\sin1+\int_1^R\frac{\sin x}{x^2}dx .$$

The boundary term tends to $0$, and the last integral converges absolutely because
$\lvert\sin x/x^2\rvert\le1/x^2$ and $\int_1^\infty x^{-2}dx$ converges. Hence the limit exists and the
integral converges.

*Absolute divergence.* Use $\lvert\cos x\rvert\ge\cos^2x$ and $\cos^2x=(1+\cos2x)/2$:

$$\frac{\lvert\cos x\rvert}{x}\ge\frac{\cos^2x}{x}
=\frac{1}{2x}+\frac{\cos2x}{2x}.$$

Now $\int_1^R dx/(2x)=\frac12\ln R\to\infty$, while $\int_1^\infty\cos(2x)/(2x)dx$ converges by the same
integration-by-parts argument (with $2x$ in place of $x$). A divergent term plus a convergent term
diverges, so $\int_1^\infty\lvert\cos x\rvert/x\,dx$ diverges.

Therefore $\int_1^\infty\cos x/x\,dx$ converges conditionally. *Check.* The value is not elementary; the
convergence comes from cancellation between the positive and negative humps.

### Solution 27

*Set-up.* The integrand tends to $-\infty$ at $0$ and is finite at $1$ ($\ln\sin1<0$). For $0<x\le\pi/2$,
concavity of sine gives $\sin x\ge\frac{2}{\pi}x$ (the chord from $(0,0)$ to $(\pi/2,1)$ lies below the
graph). Hence for $0<x\le1$,

$$\ln(\sin x)\ge\ln\left(\frac{2x}{\pi}\right)=\ln x+\ln\frac2\pi .$$

*Comparison.* Put $g(x)=-\ln(\sin x)$ and $h(x)=-\ln x-\ln(2/\pi)$. Both are non-negative for
$0<x\le\pi/2$ (for $h$, this holds for $x\le\pi/2$), and $0\le g\le h$. Since
$\int_0^1(-\ln x)dx=1$ (Solution 16) and $\int_0^1\ln(2/\pi)dx$ is finite, $\int_0^1h<\infty$. Comparison
gives $\int_0^1g<\infty$, so $\int_0^1\ln(\sin x)dx=-\int_0^1g$ converges.

*Check.* The singularity is logarithmic, not a power; logarithmic singularities are always integrable, as
the substitution $u=-\ln x$ shows. The exact value is $-\frac{\pi}{2}\ln2$, but convergence does not require
it.

### Solution 28

*Set-up.* Split at $1$: $\int_0^1+\int_1^\infty$.

*Near $0$.* For $0<x\le1$, $0<e^{-x}\le1$, so $0\le e^{-x}(-\ln x)\le-\ln x$. Since
$\int_0^1(-\ln x)dx=1$, comparison gives convergence of $\int_0^1e^{-x}\ln x\,dx$ (the integrand is
negative, but its absolute value is bounded by $-\ln x$).

*At infinity.* For $x\ge1$, $\ln x\le C e^{x/2}$ for a suitable constant $C$ (exponential growth dominates
logarithmic growth). Hence
$0\le e^{-x}\ln x\le Ce^{-x/2}$, and $\int_1^\infty e^{-x/2}dx$ converges. Comparison gives convergence.

Therefore the whole integral converges. *Check.* The value is $-\gamma$, where $\gamma\approx0.5772$ is the
Euler–Mascheroni constant; this is $\Gamma'(1)$. The convergence argument does not require the value.

### Solution 29

*Set-up.* First kind at infinity; no finite singularity because $x\ge1$. Substitute $u=\sqrt{x+1}$, so
$x=u^2-1$, $dx=2u\,du$. When $x=1$, $u=\sqrt2$; as $x\to\infty$, $u\to\infty$. Then

$$\int_1^\infty\frac{dx}{x\sqrt{x+1}}
=\int_{\sqrt2}^{\infty}\frac{2u\,du}{(u^2-1)u}
=2\int_{\sqrt2}^{\infty}\frac{du}{u^2-1}.$$

Using $\int du/(u^2-1)=\frac12\ln\left\lvert\frac{u-1}{u+1}\right\rvert$,

$$2\int_{\sqrt2}^{\infty}\frac{du}{u^2-1}
=\left[\ln\left\lvert\frac{u-1}{u+1}\right\rvert\right]_{\sqrt2}^{\infty}
=0-\ln\frac{\sqrt2-1}{\sqrt2+1}
=\ln\frac{\sqrt2+1}{\sqrt2-1}.$$

Since $\frac{\sqrt2+1}{\sqrt2-1}=(\sqrt2+1)^2$, the value is $2\ln(1+\sqrt2)\approx1.763$.

*Check.* The value is a constant, so differentiate the antiderivative in $x$ directly: with $u=\sqrt{x+1}$, $\frac{d}{dx}\ln\frac{u-1}{u+1} =\frac{2}{u^2-1}\cdot\frac{du}{dx} =\frac{2}{x}\cdot\frac{1}{2\sqrt{x+1}}=\frac{1}{x\sqrt{x+1}}$. ✓

### Solution 30

*Set-up.* For $s>0$, let $J=\int_0^\infty e^{-st}\cos\omega t\,dt$. Integrate by parts with
$u=\cos\omega t$, $dv=e^{-st}dt$: $du=-\omega\sin\omega t\,dt$, $v=-e^{-st}/s$,

$$J=\left[-\frac{e^{-st}\cos\omega t}{s}\right]_0^\infty
-\frac{\omega}{s}\int_0^\infty e^{-st}\sin\omega t\,dt
=\frac1s-\frac{\omega}{s}I,$$

where $I=\int_0^\infty e^{-st}\sin\omega t\,dt$. From Example 11,
$I=\omega/(s^2+\omega^2)$. Therefore

$$J=\frac1s-\frac{\omega}{s}\cdot\frac{\omega}{s^2+\omega^2}
=\frac{s^2+\omega^2-\omega^2}{s(s^2+\omega^2)}
=\frac{s}{s^2+\omega^2}.$$

*Check.* Setting $\omega=0$ gives $J=1/s$, the transform of $1$. ✓ As $s\to\infty$, $J\to0$. ✓
Differentiating $J$ with respect to $t$ would give the sine transform relation.

### Solution 31

*Set-up.* The integral is improper at $0$ (because of $\sqrt x$) and at infinity. Substitute $x=t^2$, so
$dx=2t\,dt$ and $\sqrt x=t$; the limits $x=0,1,\infty$ become $t=0,1,\infty$:

$$\int_0^\infty\frac{dx}{\sqrt x(1+x)}
=\int_0^\infty\frac{2t\,dt}{t(1+t^2)}
=2\int_0^\infty\frac{dt}{1+t^2}=2\cdot\frac\pi2=\pi .$$

*Check.* Differentiating $2\arctan t$ with respect to $t$ gives $2/(1+t^2)$; in the $x$ variable the
antiderivative is $2\arctan\sqrt x$, whose derivative is
$2\cdot\frac{1}{1+x}\cdot\frac{1}{2\sqrt x}=\frac{1}{\sqrt x(1+x)}$. ✓ The substitution also shows the
convergence: the transformed integral is a standard convergent arctangent integral.

## Challenge

### Solution 32

**Theorem.** Let $f,g>0$ on $[a,\infty)$ and integrable on $[a,R]$ for every $R>a$, and suppose
$\lim_{x\to\infty}f(x)/g(x)=L$.

1. If $0<L<\infty$, then $\int f$ and $\int g$ either both converge or both diverge.
2. If $L=0$ and $\int g$ converges, then $\int f$ converges.
3. If $L=\infty$ and $\int g$ diverges, then $\int f$ diverges.

*Proof of (1).* Take $\varepsilon=L/2>0$. There is $X\ge a$ such that for $x\ge X$,
$\lvert f(x)/g(x)-L\rvert<L/2$, hence
$\frac{L}{2}g(x)<f(x)<\frac{3L}{2}g(x)$. Apply the comparison test on $[X,\infty)$:
if $\int g$ converges, then $\int\frac{3L}{2}g$ converges, so $\int f$ converges;
if $\int f$ converges, then $\int\frac{L}{2}g$ converges, so $\int g$ converges.
The finite interval $[a,X]$ does not affect convergence (Proposition 1), so the conclusion holds on
$[a,\infty)$.

*Proof of (2).* With $L=0$, take $\varepsilon=1$; there is $X$ with $f(x)<g(x)$ for $x\ge X$. If
$\int g$ converges, comparison gives convergence of $\int f$.

*Proof of (3).* With $L=\infty$, take $M=1$; there is $X$ with $f(x)>g(x)$ for $x\ge X$. If $\int g$
diverges, comparison (in the divergence direction) gives divergence of $\int f$.

*No-information example for $L=0$.* Let $f(x)=1/x^2$, $g(x)=1/x$. Then $f/g=1/x\to0$, and $\int_1^\infty g$
diverges, but $\int_1^\infty f$ converges. So $L=0$ plus a divergent comparison integral tells you nothing
about $\int f$. Similarly, $L=\infty$ plus a convergent comparison integral tells you nothing: take
$f=1/x$, $g=1/x^2$, then $f/g=x\to\infty$, $\int g$ converges, but $\int f$ diverges.

*Why the hypotheses.* Positivity ensures the comparison test applies without sign issues; local
integrability ensures the proper integrals exist on each $[a,R]$. If $g$ vanishes infinitely often, the
ratio $f/g$ is undefined; the test requires $g>0$.

### Solution 33

**Convergence.** Write $\Gamma(1/2)=\int_0^\infty x^{-1/2}e^{-x}dx$ and split at $1$.

On $(0,1]$: $e^{-x}\le1$, so $0\le x^{-1/2}e^{-x}\le x^{-1/2}$; the integral $\int_0^1x^{-1/2}dx$ converges
by the $p$-test at zero with $p=1/2<1$ (value $2$). Comparison gives convergence near $0$.

On $[1,\infty)$: $x^{-1/2}\le1$, so $0\le x^{-1/2}e^{-x}\le e^{-x}$, and $\int_1^\infty e^{-x}dx=e^{-1}$.
Comparison gives convergence at infinity.

Hence $\Gamma(1/2)$ converges.

**Substitution.** Put $x=t^2$, $dx=2t\,dt$, $x^{-1/2}=1/t$; the limits $x=0,1,\infty$ correspond to
$t=0,1,\infty$:

$$\Gamma\left(\frac12\right)=\int_0^\infty x^{-1/2}e^{-x}dx
=\int_0^\infty\frac{1}{t}e^{-t^2}2t\,dt
=2\int_0^\infty e^{-t^2}dt .$$

**Gaussian value.** Let $I=\int_0^\infty e^{-t^2}dt$. Since the integrand is positive and continuous, and
the integral converges (comparison with $e^{-t}$ on $[1,\infty)$, as in §7.11), Tonelli's theorem allows us
to write

$$I^2=\int_0^\infty\int_0^\infty e^{-(x^2+y^2)}dx\,dy .$$

In polar coordinates $x=r\cos\theta$, $y=r\sin\theta$, the first quadrant is $0\le r<\infty$,
$0\le\theta\le\pi/2$, and $dx\,dy=r\,dr\,d\theta$:

$$I^2=\int_0^{\pi/2}\int_0^\infty e^{-r^2}r\,dr\,d\theta
=\left(\int_0^{\pi/2}d\theta\right)\left(\int_0^\infty e^{-r^2}r\,dr\right)
=\frac{\pi}{2}\cdot\frac12=\frac{\pi}{4}.$$

Hence $I=\sqrt\pi/2$ (positive square root because $I>0$), and
$\Gamma(1/2)=2I=\sqrt\pi$. $\blacksquare$

*Check.* Numerically $\sqrt\pi\approx1.77245$, and $2\int_0^\infty e^{-t^2}dt\approx2(0.8862)=1.7724$, in
agreement. Also $\Gamma(1/2)\Gamma(3/2)=\frac12\Gamma(1/2)^2=\pi/2$, which is consistent with the beta
identity $\Gamma(a)\Gamma(1-a)=\pi/\sin(\pi a)$ at $a=1/2$. ✓

### Solution 34

**Construction.** For each integer $n\ge2$, let $w_n=2^{-n-1}$ and define the triangular spike

$$f_n(x)=\max\left(0,\,1-\frac{\lvert x-n\rvert}{w_n}\right).$$

Thus $f_n(n)=1$, $f_n=0$ outside $(n-w_n,n+w_n)$, and $f_n$ is continuous and piecewise linear. Define
$f(x)=e^{-x}+\sum_{n=2}^{\infty}f_n(x)$; the exponential background makes $f$ strictly positive everywhere.

**Well-defined and continuous.** The intervals $(n-w_n,n+w_n)$ are pairwise disjoint: the distance between
consecutive centres is $1$, while $w_n+w_{n+1}\le2^{-3}+2^{-4}=3/16<1$. At each point at most one $f_n$ is
nonzero, and each $f_n$ is continuous; hence the sum is continuous (a finite sum locally). Also $f>0$,
and $f(n)\ge1$ for every $n\ge2$.

**Finite integral.** The area of the $n$-th spike is $\frac12(2w_n)(1)=w_n=2^{-n-1}$, and the background
has area $1$. Therefore

$$\int_0^\infty f(x)\,dx=1+\sum_{n=2}^{\infty}2^{-n-1}=1+\frac14=\frac54<\infty .$$

**No limit at infinity.** $f(n)=1$ for every integer $n\ge2$, so $f(x)\not\to0$ as $x\to\infty$; in fact
$f$ attains the value $1$ on an unbounded set.

*Why this does not contradict Theorem 6 or the comparison test.* $f$ is non-negative and integrable; the
theorem does not claim that an integrable positive function tends to $0$. The function is continuous but not
uniformly continuous: the slopes of the spikes are $1/w_n=2^{n+1}$, which are unbounded, and
$f(n)=1$ while $f(n+w_n)=0$ with $w_n\to0$. This is exactly the hypothesis in Exercise 35.

### Solution 35

**Theorem.** Let $f$ be uniformly continuous on $[0,\infty)$ and suppose $\int_0^\infty f(x)\,dx$ converges.
Then $f(x)\to0$ as $x\to\infty$.

*Proof.* Let $F(R)=\int_0^Rf(x)\,dx$. By hypothesis $F(R)\to L$ for some finite $L$. Suppose, for
contradiction, that $f(x)\not\to0$. Then there are $\varepsilon>0$ and a sequence $x_n\to\infty$ with
$\lvert f(x_n)\rvert\ge\varepsilon$ for all $n$.

By uniform continuity, there is $\delta>0$ such that $\lvert x-y\rvert<\delta$ implies
$\lvert f(x)-f(y)\rvert<\varepsilon/2$. Then for every $x\in(x_n-\delta,x_n+\delta)$,
$\lvert f(x)\rvert>\varepsilon/2$. In particular $f$ has no zero on that interval, so it has constant sign
there (a continuous function that changes sign must vanish). Hence

$$\left\lvert\int_{x_n-\delta}^{x_n+\delta}f(x)\,dx\right\rvert
=\int_{x_n-\delta}^{x_n+\delta}\lvert f(x)\rvert\,dx
\ge\frac{\varepsilon}{2}\cdot2\delta=\varepsilon\delta .$$

But

$$\int_{x_n-\delta}^{x_n+\delta}f(x)\,dx=F(x_n+\delta)-F(x_n-\delta)\longrightarrow L-L=0,$$

because both arguments tend to infinity. This contradicts the lower bound $\varepsilon\delta>0$ for large
$n$. Therefore $f(x)\to0$. $\blacksquare$

*Uniform continuity cannot be dropped.* The function of Solution 34 is continuous, has
$\int_0^\infty f<\infty$, and does not tend to $0$. It is not uniformly continuous because its spikes have
arbitrarily large slopes. Another example is $\sin(x^2)$: its improper integral $\int_0^\infty\sin(x^2)dx$
converges (by the substitution $u=x^2$ and Dirichlet's test), but $\sin(x^2)$ does not tend to $0$, and it
is not uniformly continuous because consecutive zeros and maxima get arbitrarily close.

### Solution 36

**Convergence.** Split at $1$.

Near $0$: $\dfrac{x^{p-1}}{1+x}\sim x^{p-1}$, and $\int_0^1x^{p-1}dx$ converges iff $p-1>-1$, that is
$p>0$.

At infinity: $\dfrac{x^{p-1}}{1+x}\sim x^{p-2}$, and $\int_1^\infty x^{p-2}dx$ converges iff $p-2<-1$, that
is $p<1$.

Therefore the integral converges exactly for $0<p<1$. (At $p=0$ and $p=1$, the two ends give logarithmic
divergence.)

**The case $p=1/2$.** Then

$$\int_0^\infty\frac{x^{-1/2}}{1+x}dx .$$

Substitute $x=t^2$, $dx=2t\,dt$, $x^{-1/2}=1/t$:

$$\int_0^\infty\frac{x^{-1/2}}{1+x}dx
=\int_0^\infty\frac{1}{t(1+t^2)}2t\,dt
=2\int_0^\infty\frac{dt}{1+t^2}=2\cdot\frac\pi2=\pi .$$

*Check.* The integrand is positive, and the two endpoint behaviours are $x^{-1/2}$ at $0$ and $x^{-3/2}$ at
infinity, both integrable; the value $\pi\approx3.1416$ is positive. Differentiating $2\arctan\sqrt x$ gives
the integrand, as in Solution 31.
