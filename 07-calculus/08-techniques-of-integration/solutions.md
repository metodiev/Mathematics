# Techniques of Integration — Solutions

> [Techniques of Integration](README.md) · Solutions to the 36 problems in [exercises.md](exercises.md)

Each solution states the strategy, carries out every step, and **checks the answer by differentiating**.
Pitfalls are flagged where the problem is designed to expose them.

## Beginner

### Solution 1

*Strategy: the integrand contains $2x$, the derivative of $x^2+1$; substitute the inside.*

With $u = x^2+1$, $du = 2x\,dx$, so

$$\int 2x\left(x^2+1\right)^5dx = \int u^5\,du = \frac{u^6}{6} + C = \frac{\left(x^2+1\right)^6}{6} + C .$$

*Check:* $\frac{d}{dx}\frac{(x^2+1)^6}{6} = \frac{6(x^2+1)^5\cdot 2x}{6} = 2x(x^2+1)^5$. ✓

### Solution 2

*Strategy: substitute the exponent; the factor $x$ supplies half of $du$.*

With $u = x^2$, $du = 2x\,dx$, so $x\,dx = \frac12 du$ and

$$\int xe^{x^2}dx = \frac12\int e^u\,du = \frac12e^{x^2} + C .$$

*Check:* $\frac{d}{dx}\left(\frac12e^{x^2}\right) = \frac12e^{x^2}\cdot 2x = xe^{x^2}$. ✓

*Pitfall:* the missing factor of $2$ is exactly what makes the integral $\frac12e^{x^2}$ rather than
$e^{x^2}$; the check catches it immediately.

### Solution 3

*Strategy: the argument is $3x$, so the derivative $3$ appears in the differential.*

With $u = 3x$, $du = 3\,dx$, so $dx = \frac13 du$ and

$$\int\cos(3x)\,dx = \frac13\int\cos u\,du = \frac{\sin(3x)}{3} + C .$$

*Check:* $\frac{d}{dx}\frac{\sin 3x}{3} = \frac{3\cos 3x}{3} = \cos 3x$. ✓

### Solution 4

*Strategy: the numerator is half the derivative of the denominator.*

With $u = x^2+1$, $du = 2x\,dx$, so $x\,dx = \frac12du$ and

$$\int\frac{x}{x^2+1}dx = \frac12\int\frac{du}{u} = \frac12\ln\left(x^2+1\right) + C .$$

*Check:* $\frac{d}{dx}\frac12\ln(x^2+1) = \frac12\cdot\frac{2x}{x^2+1} = \frac{x}{x^2+1}$. ✓

*Remark:* the absolute value is unnecessary because $x^2+1>0$ for all $x$.

### Solution 5

*Strategy: a product of a logarithm and a power; integrate by parts with $u = \ln x$.*

Take $u = \ln x$, $dv = x\,dx$. Then $du = \frac{dx}{x}$ and $v = \frac{x^2}{2}$, so

$$\int x\ln x\,dx = \frac{x^2}{2}\ln x - \int\frac{x^2}{2}\cdot\frac{dx}{x}
= \frac{x^2}{2}\ln x - \frac12\int x\,dx = \frac{x^2}{2}\ln x - \frac{x^2}{4} + C .$$

*Check:* differentiating gives $x\ln x + \frac{x^2}{2}\cdot\frac1x - \frac{x}{2} = x\ln x$. ✓

*Why this choice:* differentiating $\ln x$ removes the logarithm, which is the whole difficulty; the
polynomial factor is easy to integrate.

### Solution 6

*Strategy: parts with $u = x$, $dv = \cos x\,dx$.*

Then $du = dx$, $v = \sin x$, and

$$\int x\cos x\,dx = x\sin x - \int\sin x\,dx = x\sin x + \cos x + C .$$

*Check:* $\frac{d}{dx}\left(x\sin x + \cos x\right) = \sin x + x\cos x - \sin x = x\cos x$. ✓

*Pitfall:* the sign of the second term is plus, because $\int\sin x = -\cos x$ and the parts formula has a
minus sign; two minus signs cancel.

### Solution 7

*Strategy: a single even power; use the power-reduction identity.*

$\sin^2x = \frac{1-\cos 2x}{2}$, so

$$\int\sin^2x\,dx = \frac12\int dx - \frac12\int\cos 2x\,dx = \frac{x}{2} - \frac{\sin 2x}{4} + C .$$

*Check:* $\frac12 - \frac{2\cos 2x}{4} = \frac12 - \frac{\cos 2x}{2} = \sin^2x$. ✓

*Pitfall:* substituting $u = \sin x$ fails here, because $du = \cos x\,dx$ is not present; the identity is
the only route for even powers.

### Solution 8

*Strategy: partial fractions. The denominator factors as $(x-1)(x+1)$, so*

$$\frac{1}{x^2-1} = \frac{A}{x-1} + \frac{B}{x+1} .$$

*Determine the constants.* Clearing denominators, $1 = A(x+1) + B(x-1)$. At $x=1$: $1 = 2A$, so
$A = \frac12$. At $x=-1$: $1 = -2B$, so $B = -\frac12$.

*Integrate.*

$$\int\frac{dx}{x^2-1} = \frac12\ln|x-1| - \frac12\ln|x+1| + C
= \frac12\ln\left|\frac{x-1}{x+1}\right| + C .$$

*Check:* $\frac12\left(\frac{1}{x-1} - \frac{1}{x+1}\right) = \frac12\cdot\frac{2}{x^2-1} = \frac{1}{x^2-1}$. ✓

*Remark:* the decomposition is valid on each interval not containing $\pm1$; the absolute values handle
the signs.

### Solution 9

*Strategy: the standard arctangent form with $a = 3$.*

$$\int\frac{dx}{x^2+9} = \frac13\arctan\frac{x}{3} + C .$$

*Check:* the derivative of $\frac13\arctan\frac x3$ is
$\frac13\cdot\frac{1}{1+(x/3)^2}\cdot\frac13 = \frac{1}{9+x^2}$. ✓

### Solution 10

*Strategy: the standard arcsine form with $a = 3$.*

$$\int\frac{dx}{\sqrt{9-x^2}} = \arcsin\frac{x}{3} + C, \qquad |x| < 3 .$$

*Check:* $\frac{d}{dx}\arcsin\frac x3 = \frac{1}{\sqrt{1-(x/3)^2}}\cdot\frac13 = \frac{1}{\sqrt{9-x^2}}$. ✓

*Pitfall:* writing $\arcsin(x/3)$ without noting the domain $|x|<3$ hides the fact that the integrand is
not real outside it.

### Solution 11

*Strategy: recognise the numerator as the derivative of the denominator.*

Since $\frac{d}{dx}\left(x^2+x+1\right) = 2x+1$ and $x^2+x+1 = \left(x+\frac12\right)^2+\frac34>0$,

$$\int\frac{2x+1}{x^2+x+1}dx = \ln\left(x^2+x+1\right) + C .$$

*Check:* $\frac{2x+1}{x^2+x+1}$. ✓

*Remark:* this is a substitution $u = x^2+x+1$ with $du$ exactly the numerator. Had the numerator been
$2x+3$, one would split it as $(2x+1)+2$ and integrate the constant part as an arctangent.

### Solution 12

*Strategy: parts, then evaluate at the limits.*

Take $u = x$, $dv = e^x dx$, so $du = dx$, $v = e^x$:

$$\int_0^1 xe^x\,dx = \Big[xe^x\Big]_0^1 - \int_0^1 e^x\,dx = e - \left(e - 1\right) = 1 .$$

*Check by differentiating the antiderivative.* $xe^x - e^x$ has derivative $e^x + xe^x - e^x = xe^x$. ✓
At the limits: $(1\cdot e - e) - (0 - 1) = 0 + 1 = 1$. ✓

## Intermediate

### Solution 13

*Strategy: both powers are odd, so either substitution works. Save one cosine and use
$\sin^2+\cos^2=1$.*

Write $\sin^3x\cos^3x = \sin^3x\cos^2x\cos x = \sin^3x\left(1-\sin^2x\right)\cos x$ and put
$u = \sin x$, $du = \cos x\,dx$:

$$\int\sin^3x\cos^3x\,dx = \int u^3\left(1-u^2\right)du = \int\left(u^3-u^5\right)du
= \frac{u^4}{4} - \frac{u^6}{6} + C = \frac{\sin^4x}{4} - \frac{\sin^6x}{6} + C .$$

*Check:* differentiating gives
$\sin^3x\cos x - \sin^5x\cos x = \sin^3x\cos x\left(1-\sin^2x\right) = \sin^3x\cos^3x$. ✓

*Alternative:* with $u = \cos x$ the answer is $-\frac{\cos^4x}{4}+\frac{\cos^6x}{6}+C'$, which differs by
a constant, as Theorem 7.6.1 of the companion topic requires.

### Solution 14

*Strategy: an even power of secant; save $\sec^2x$ and convert with $\sec^2 = 1+\tan^2$.*

$$\int\sec^4x\,dx = \int\left(1+\tan^2x\right)\sec^2x\,dx .$$

With $u = \tan x$, $du = \sec^2x\,dx$,

$$\int\left(1+u^2\right)du = u + \frac{u^3}{3} + C = \tan x + \frac{\tan^3x}{3} + C .$$

*Check:* $\sec^2x + \tan^2x\sec^2x = \sec^2x\left(1+\tan^2x\right) = \sec^4x$. ✓

### Solution 15

*Strategy: repeated parts, or the tabular method, differentiating $x^2$ twice.*

Take $u = x^2$, $dv = e^{-x}dx$, so $v = -e^{-x}$ and $du = 2x\,dx$:

$$\int x^2e^{-x}dx = -x^2e^{-x} + 2\int xe^{-x}dx .$$

For the remaining integral, $u = x$, $dv = e^{-x}dx$: $\int xe^{-x}dx = -xe^{-x} + \int e^{-x}dx = -xe^{-x}-e^{-x}$.
Therefore

$$\int x^2e^{-x}dx = -x^2e^{-x} - 2xe^{-x} - 2e^{-x} + C = -e^{-x}\left(x^2+2x+2\right) + C .$$

*Check:* the derivative is $e^{-x}\left(x^2+2x+2\right) - e^{-x}(2x+2) = x^2e^{-x}$. ✓

*Pitfall:* dropping a factor of $2$ from the second application is the usual error; the tabular layout
gives the coefficients $1,2,2$ with alternating signs.

### Solution 16

*Strategy: parts with $u = \arctan x$ and $dv = dx$.*

Then $du = \frac{dx}{1+x^2}$ and $v = x$, so

$$\int\arctan x\,dx = x\arctan x - \int\frac{x}{1+x^2}dx .$$

The remaining integral is $\frac12\ln(1+x^2)$ by Solution 4, hence

$$\int\arctan x\,dx = x\arctan x - \frac12\ln\left(1+x^2\right) + C .$$

*Check:* $\arctan x + \frac{x}{1+x^2} - \frac{x}{1+x^2} = \arctan x$. ✓

### Solution 17

*Strategy: the fraction is improper (degree $3$ over degree $2$), so divide first.*

Polynomial division gives

$$\frac{x^3+x^2+1}{x^2+1} = x + 1 - \frac{x}{x^2+1},$$

because $(x+1)(x^2+1) = x^3+x^2+x+1$ and the remainder is $(x^3+x^2+1)-(x^3+x^2+x+1) = -x$.

Hence

$$\int\frac{x^3+x^2+1}{x^2+1}dx = \frac{x^2}{2} + x - \frac12\ln\left(x^2+1\right) + C .$$

*Check:* $x + 1 - \frac{x}{x^2+1}$, which is the quotient form of the integrand. ✓

*Pitfall:* attempting partial fractions on the original improper fraction produces an inconsistent system
for the unknowns, because the decomposition assumes a proper fraction.

### Solution 18

*Strategy: factor $x^3+x = x(x^2+1)$ and decompose.*

$$\frac{1}{x\left(x^2+1\right)} = \frac{A}{x} + \frac{Bx+C}{x^2+1} .$$

Clearing denominators, $1 = A(x^2+1) + (Bx+C)x = (A+B)x^2 + Cx + A$. Comparing coefficients: $A = 1$,
$C = 0$, $A+B = 0$ so $B = -1$. Hence

$$\int\frac{dx}{x^3+x} = \int\left(\frac1x - \frac{x}{x^2+1}\right)dx
= \ln|x| - \frac12\ln\left(x^2+1\right) + C .$$

*Check:* $\frac1x - \frac{x}{x^2+1} = \frac{x^2+1-x^2}{x(x^2+1)} = \frac{1}{x(x^2+1)}$. ✓

### Solution 19

*Strategy: complete the square; the quadratic has no real roots.*

$x^2+2x+5 = (x+1)^2+4$, so with $u = x+1$ and $a = 2$,

$$\int\frac{dx}{x^2+2x+5} = \int\frac{du}{u^2+4} = \frac12\arctan\frac{u}{2} + C
= \frac12\arctan\frac{x+1}{2} + C .$$

*Check:* $\frac12\cdot\frac{1}{1+((x+1)/2)^2}\cdot\frac12 = \frac{1}{4+(x+1)^2} = \frac{1}{x^2+2x+5}$. ✓

### Solution 20

*Strategy: trigonometric substitution $x = 3\sin\theta$ on $[-\pi/2,\pi/2]$.*

Then $dx = 3\cos\theta\,d\theta$ and $\sqrt{9-x^2} = 3\cos\theta$, so

$$\int\sqrt{9-x^2}\,dx = \int 9\cos^2\theta\,d\theta = 9\left(\frac{\theta}{2}+\frac{\sin 2\theta}{4}\right) + C
= \frac{9}{2}\theta + \frac{9}{2}\sin\theta\cos\theta + C .$$

Back-substitute: $\theta = \arcsin\frac x3$, $\sin\theta = \frac x3$, $\cos\theta = \frac{\sqrt{9-x^2}}{3}$,
so $\frac92\sin\theta\cos\theta = \frac92\cdot\frac{x\sqrt{9-x^2}}{9} = \frac{x\sqrt{9-x^2}}{2}$, and

$$\int\sqrt{9-x^2}\,dx = \frac92\arcsin\frac x3 + \frac{x}{2}\sqrt{9-x^2} + C .$$

*Check by differentiating.* The derivative of $\frac x2\sqrt{9-x^2}$ is
$\frac12\sqrt{9-x^2} - \frac{x^2}{2\sqrt{9-x^2}} = \frac{9-2x^2}{2\sqrt{9-x^2}}$; the derivative of
$\frac92\arcsin\frac x3$ is $\frac{9}{2\sqrt{9-x^2}}$. Sum: $\frac{9-2x^2+9}{2\sqrt{9-x^2}} = \frac{18-2x^2}{2\sqrt{9-x^2}} = \sqrt{9-x^2}$. ✓

*Remark:* the answer is the area of a circular segment plus a triangle, which is why the formula has one
term with a square root and one with an arcsine.

### Solution 21

*Strategy: $x = \sec\theta$ with $0 \le \theta < \pi/2$, since $x>1$ means $\theta \in (0,\pi/2)$.*

Then $dx = \sec\theta\tan\theta\,d\theta$ and $\sqrt{x^2-1} = \tan\theta$ (positive on this range), so

$$\int\frac{dx}{x\sqrt{x^2-1}} = \int\frac{\sec\theta\tan\theta}{\sec\theta\tan\theta}d\theta
= \int d\theta = \theta + C = \operatorname{arcsec}x + C .$$

*Check:* for $x>1$, $\frac{d}{dx}\operatorname{arcsec}x = \frac{1}{x\sqrt{x^2-1}}$. ✓

*Pitfall:* omitting the range lets $\tan\theta$ be negative, which would change the sign. Also the general
antiderivative on $x<-1$ is $-\operatorname{arcsec}x + C$ with the usual convention; here the problem
restricts to $x>1$.

### Solution 22

*Strategy: rationalise with $u = \sqrt x$.*

Then $x = u^2$, $dx = 2u\,du$ and

$$\int\frac{dx}{1+\sqrt x} = \int\frac{2u}{1+u}du = 2\int\left(1 - \frac{1}{1+u}\right)du
= 2u - 2\ln|1+u| + C .$$

Since $u = \sqrt x \ge 0$, $|1+u| = 1+u$, so

$$\int\frac{dx}{1+\sqrt x} = 2\sqrt x - 2\ln\left(1+\sqrt x\right) + C .$$

*Check:* differentiating gives
$\frac{1}{\sqrt x} - \frac{2}{1+\sqrt x}\cdot\frac{1}{2\sqrt x} = \frac{1}{\sqrt x}\left(1-\frac{1}{1+\sqrt x}\right)$,
which equals $\frac{1}{\sqrt x}\cdot\frac{\sqrt x}{1+\sqrt x} = \frac{1}{1+\sqrt x}$. ✓

### Solution 23

*Strategy: apply $S_4$ with $h = \frac14$ and the coefficient pattern $1,4,2,4,1$.*

The values of $f(x) = \frac{1}{1+x^2}$ are

| $x$ | $0$ | $0.25$ | $0.5$ | $0.75$ | $1$ |
|---|---|---|---|---|---|
| $f(x)$ | $1$ | $0.941176$ | $0.8$ | $0.64$ | $0.5$ |

Therefore

$$S_4 = \frac{0.25}{3}\left[1 + 4(0.941176) + 2(0.8) + 4(0.64) + 0.5\right]
= \frac{1}{12}\left(9.424706\right) = 0.785392 .$$

*Error.* The exact value is $\frac{\pi}{4} = 0.785398$, so the error is about $-6\times10^{-6}$. The bound
is

$$|E_S| \le \frac{(b-a)^5}{180n^4}\max\left|f^{(4)}\right| = \frac{1}{180\cdot 256}\cdot 24 = \frac{1}{1920} \approx 5.2\times10^{-4},$$

and the actual error is far inside it. ✓

*Remark:* $f^{(4)}(x) = \frac{24\left(1-10x^2+5x^4\right)}{(1+x^2)^5}$ attains its maximum modulus $24$ at
$x=0$, which is where the bound comes from.

### Solution 24

*Strategy: complete the square and split the numerator into a derivative part and a constant part.*

$x^2+4x+5 = (x+2)^2+1$. With $u = x+2$, $x = u-2$ and $dx = du$, so

$$\int\frac{x}{x^2+4x+5}dx = \int\frac{u-2}{u^2+1}du
= \frac12\ln\left(u^2+1\right) - 2\arctan u + C .$$

Returning to $x$,

$$\int\frac{x}{x^2+4x+5}dx = \frac12\ln\left(x^2+4x+5\right) - 2\arctan(x+2) + C .$$

*Check:* the derivative is
$\frac{2x+4}{2(x^2+4x+5)} - \frac{2}{1+(x+2)^2} = \frac{x+2}{x^2+4x+5} - \frac{2}{x^2+4x+5}$, which equals
$\frac{x}{x^2+4x+5}$. ✓

## Advanced

### Solution 25

*Strategy: factor $x^4-1 = (x^2-1)(x^2+1)$ and split into two simpler fractions.*

$$\frac{1}{x^4-1} = \frac12\left(\frac{1}{x^2-1} - \frac{1}{x^2+1}\right),$$

because $\frac12\left[(x^2+1)-(x^2-1)\right] = 1$ over the common denominator. Using Solutions 8 and 9,

$$\int\frac{dx}{x^4-1} = \frac12\left[\frac12\ln\left|\frac{x-1}{x+1}\right| - \arctan x\right] + C
= \frac14\ln\left|\frac{x-1}{x+1}\right| - \frac12\arctan x + C .$$

*Check:* differentiating gives
$\frac14\left(\frac{1}{x-1}-\frac{1}{x+1}\right) - \frac{1}{2(1+x^2)} = \frac{1}{2(x^2-1)} - \frac{1}{2(x^2+1)}$,
which equals $\frac{(x^2+1)-(x^2-1)}{2(x^4-1)} = \frac{1}{x^4-1}$. ✓

### Solution 26

*Strategy: the substitution $u = \sqrt{x^2+4}$ makes the root the new variable; express $dx/x$ in terms
of $u$.*

From $u^2 = x^2+4$ we get $2u\,du = 2x\,dx$, so $x\,dx = u\,du$ and, since $x^2 = u^2-4$,

$$\frac{dx}{x} = \frac{x\,dx}{x^2} = \frac{u\,du}{u^2-4} .$$

Hence

$$\int\frac{\sqrt{x^2+4}}{x}dx = \int u\cdot\frac{u\,du}{u^2-4} = \int\frac{u^2}{u^2-4}du
= \int\left(1+\frac{4}{u^2-4}\right)du .$$

Using $\frac{4}{u^2-4} = \frac{1}{u-2} - \frac{1}{u+2}$,

$$\int\left(1+\frac{4}{u^2-4}\right)du = u + \ln|u-2| - \ln|u+2| + C
= u + \ln\left|\frac{u-2}{u+2}\right| + C .$$

Therefore

$$\int\frac{\sqrt{x^2+4}}{x}dx = \sqrt{x^2+4} + \ln\left|\frac{\sqrt{x^2+4}-2}{\sqrt{x^2+4}+2}\right| + C .$$

*Check:* with $u = \sqrt{x^2+4}$ and $u' = x/u$, the derivative is
$u' + \left(\frac{1}{u-2}-\frac{1}{u+2}\right)u' = \frac{x}{u}\left(1+\frac{4}{u^2-4}\right)$, which equals
$\frac{x}{u}\cdot\frac{u^2}{u^2-4} = \frac{xu}{x^2} = \frac{\sqrt{x^2+4}}{x}$. ✓

### Solution 27

*Strategy: combine sine and cosine into a single sine with a phase shift.*

$$\sin x+\cos x = \sqrt2\left(\frac{1}{\sqrt2}\sin x+\frac{1}{\sqrt2}\cos x\right)
= \sqrt2\sin\left(x+\frac{\pi}{4}\right).$$

Therefore

$$\int\frac{dx}{\sin x+\cos x} = \frac{1}{\sqrt2}\int\csc\left(x+\frac{\pi}{4}\right)dx
= \frac{1}{\sqrt2}\ln\left|\tan\left(\frac{x}{2}+\frac{\pi}{8}\right)\right| + C,$$

using $\int\csc u\,du = \ln|\tan(u/2)| + C$.

*Check:* since
$\frac{d}{dx}\ln\tan\left(\frac x2+\frac\pi8\right) = \frac{1}{\tan\left(\frac x2+\frac\pi8\right)}\cdot\frac12\sec^2\left(\frac x2+\frac\pi8\right)$,
the derivative of the answer is
$\frac{1}{\sqrt2}\cdot\frac{1}{2\sin\left(\frac x2+\frac\pi8\right)\cos\left(\frac x2+\frac\pi8\right)} = \frac{1}{\sqrt2\sin\left(x+\frac\pi4\right)}$,
which equals $\frac{1}{\sin x+\cos x}$. ✓

*Alternative:* the Weierstrass substitution also works and is carried out in Solution 35 for a similar
integrand.

### Solution 28

*Strategy: substitute $u = x^2$ first; the factor $x^3dx = x^2\cdot x\,dx$ then becomes $u\,du/2$, leaving
a parts integral.*

With $u = x^2$, $du = 2x\,dx$, so $x^3dx = x^2\cdot x\,dx = u\cdot\frac{du}{2}$ and

$$\int x^3e^{x^2}dx = \frac12\int ue^u\,du = \frac12\left(ue^u - e^u\right) + C
= \frac12e^{x^2}\left(x^2-1\right) + C,$$

where $\int ue^u du = ue^u - e^u$ is the basic parts integral.

*Check:* the derivative is
$\frac12\left[2xe^{x^2}\left(x^2-1\right) + e^{x^2}\cdot 2x\right] = xe^{x^2}\left(x^2-1\right) + xe^{x^2} = x^3e^{x^2}$. ✓

*Pitfall:* applying parts directly to $x^3$ and $e^{x^2}$ requires $v = \int e^{x^2}dx$, which is not
elementary; the preliminary substitution avoids this dead end.

### Solution 29

*Strategy: integrate by parts with $u = \sin^{n-1}x$ and $dv = \sin x\,dx$, then recycle the resulting
integral.*

For $n \ge 2$, take $u = \sin^{n-1}x$, $dv = \sin x\,dx$, so $v = -\cos x$ and
$du = (n-1)\sin^{n-2}x\cos x\,dx$. Then

$$I_n = \Big[-\sin^{n-1}x\cos x\Big]_0^{\pi/2} + (n-1)\int_0^{\pi/2}\sin^{n-2}x\cos^2x\,dx .$$

The boundary term vanishes at both ends (at $0$ because $\sin 0 = 0$, at $\pi/2$ because $\cos\frac\pi2 = 0$).
Writing $\cos^2 = 1-\sin^2$,

$$I_n = (n-1)\int_0^{\pi/2}\sin^{n-2}x\,dx - (n-1)\int_0^{\pi/2}\sin^n x\,dx = (n-1)I_{n-2} - (n-1)I_n .$$

Hence $nI_n = (n-1)I_{n-2}$, that is, $I_n = \frac{n-1}{n}I_{n-2}$. $\blacksquare$

*Compute $I_5$.* The base values are $I_0 = \frac{\pi}{2}$ and $I_1 = 1$, so

$$I_5 = \frac45 I_3 = \frac45\cdot\frac23 I_1 = \frac{8}{15}\cdot 1 = \frac{8}{15}.$$

*Check by bounds.* On $[0,\pi/2]$, $0 \le \sin x \le 1$, so $\sin^6x \le \sin^5x \le \sin^4x$ pointwise.
Hence $I_6 \le I_5 \le I_4$, and

$$I_4 = \frac34I_2 = \frac34\cdot\frac12\cdot\frac{\pi}{2} = \frac{3\pi}{16} \approx 0.589, \qquad
I_6 = \frac56I_4 = \frac{5\pi}{32} \approx 0.491 .$$

The value $\frac{8}{15} \approx 0.533$ lies between them. ✓

### Solution 30

*Strategy: the fractional power $x^{1/3}$ suggests $u = x^{1/3}$, so $x = u^3$ and $dx = 3u^2du$.*

$$\int\frac{dx}{1+x^{1/3}} = \int\frac{3u^2}{1+u}du = 3\int\left(u - 1 + \frac{1}{1+u}\right)du,$$

where the division is $\frac{u^2}{1+u} = u-1+\frac{1}{1+u}$ because $u^2 = (u-1)(u+1)+1$. Hence

$$\int\frac{dx}{1+x^{1/3}} = 3\left(\frac{u^2}{2} - u + \ln|1+u|\right) + C
= \frac32x^{2/3} - 3x^{1/3} + 3\ln\left|1+x^{1/3}\right| + C .$$

*Check:* differentiating gives
$x^{-1/3} - x^{-2/3} + \frac{x^{-2/3}}{1+x^{1/3}} = x^{-1/3} - x^{-2/3}\left(1-\frac{1}{1+x^{1/3}}\right)$,
which equals
$x^{-1/3} - x^{-2/3}\cdot\frac{x^{1/3}}{1+x^{1/3}} = x^{-1/3} - \frac{x^{-1/3}}{1+x^{1/3}} = \frac{1}{1+x^{1/3}}$. ✓

### Solution 31

*Strategy: Simpson with $h = \frac14$; then compare with the stated value and the error bound.*

The values of $f(x) = e^{-x^2}$ are

| $x$ | $0$ | $0.25$ | $0.5$ | $0.75$ | $1$ |
|---|---|---|---|---|---|
| $f(x)$ | $1$ | $0.939413$ | $0.778801$ | $0.569783$ | $0.367879$ |

so

$$S_4 = \frac{0.25}{3}\left[1 + 4(0.939413) + 2(0.778801) + 4(0.569783) + 0.367879\right]
= \frac{1}{12}\left(8.962265\right) = 0.746855 .$$

*Comparison.* The stated value is $0.746824$ (six decimals), so the error is about $3.1\times10^{-5}$.

*Bound.* With $\left|f^{(4)}\right|\le 20$ on $[0,1]$,

$$|E_S| \le \frac{1}{180\cdot4^4}\cdot 20 = \frac{20}{46080} = \frac{1}{2304} \approx 4.34\times10^{-4},$$

and the actual error lies well inside it. ✓

*Remark:* $f^{(4)}(x) = e^{-x^2}\left(16x^4-48x^2+12\right)$. Writing $u = x^2 \in [0,1]$, the factor
$16u^2-48u+12$ decreases from $12$ to $-20$, so $\left|f^{(4)}\right|\le20$ on $[0,1]$ — a bound that is
crude but easy to justify. The actual maximum of $\left|f^{(4)}\right|$ is $12$, at $x=0$.

### Solution 32

*Strategy: $x = \tan\theta$ on $(-\pi/2,\pi/2)$; then $(x^2+1)^{3/2} = \sec^3\theta$.*

With $dx = \sec^2\theta\,d\theta$,

$$\int\frac{dx}{\left(x^2+1\right)^{3/2}} = \int\frac{\sec^2\theta}{\sec^3\theta}d\theta
= \int\cos\theta\,d\theta = \sin\theta + C .$$

Since $\tan\theta = x$, a right triangle with opposite $x$ and adjacent $1$ has hypotenuse
$\sqrt{x^2+1}$, so $\sin\theta = \frac{x}{\sqrt{x^2+1}}$ and

$$\int\frac{dx}{\left(x^2+1\right)^{3/2}} = \frac{x}{\sqrt{x^2+1}} + C .$$

*Check:* the derivative is
$\frac{d}{dx}\left[x\left(x^2+1\right)^{-1/2}\right] = \left(x^2+1\right)^{-1/2} - x^2\left(x^2+1\right)^{-3/2} = \frac{x^2+1-x^2}{\left(x^2+1\right)^{3/2}}$,
which equals $\frac{1}{\left(x^2+1\right)^{3/2}}$. ✓

## Challenge

### Solution 33

**Theorem.** Let $\varphi$ be continuously differentiable on $[a,b]$, let $J$ be an interval with
$\varphi([a,b]) \subseteq J$, and let $f$ be continuous on $J$. Then

$$\int_a^b f\big(\varphi(x)\big)\varphi'(x)\,dx = \int_{\varphi(a)}^{\varphi(b)} f(u)\,du .$$

*Proof.* Since $f$ is continuous on the interval $J$, the Fundamental Theorem of Calculus (Part 1) gives
an antiderivative $F$ of $f$ on $J$, namely $F(u) = \int_c^u f(t)\,dt$ for any fixed $c \in J$.

Because $\varphi$ is differentiable with continuous derivative and $F$ is differentiable on $J$, the chain
rule gives, for every $x \in (a,b)$,

$$\frac{d}{dx}F\big(\varphi(x)\big) = F'\big(\varphi(x)\big)\varphi'(x) = f\big(\varphi(x)\big)\varphi'(x).$$

The function $x \mapsto F(\varphi(x))$ is continuous on $[a,b]$ (composition of continuous functions) and
differentiable on $(a,b)$ with the derivative displayed. Its derivative is continuous, because $f$,
$\varphi$ and $\varphi'$ are continuous. Therefore the FTC (Part 2) applies and

$$\int_a^b f\big(\varphi(x)\big)\varphi'(x)\,dx = F\big(\varphi(b)\big) - F\big(\varphi(a)\big).$$

On the other hand, $F$ is an antiderivative of the continuous function $f$ on $J$, and the whole interval
between $\varphi(a)$ and $\varphi(b)$ lies in $J$ because $J$ is an interval containing both points. So
the FTC (Part 2) applied to $f$ on that interval gives

$$\int_{\varphi(a)}^{\varphi(b)} f(u)\,du = F\big(\varphi(b)\big) - F\big(\varphi(a)\big).$$

The two numbers are equal. $\blacksquare$

*Where each hypothesis is used.*

* $\varphi \in C^1$ makes $f(\varphi(x))\varphi'(x)$ continuous, so its integral exists, and makes the
  chain rule applicable.
* $f$ continuous on $J$ produces the antiderivative $F$ and permits FTC Part 2 on the $u$-side.
* $\varphi([a,b]) \subseteq J$ keeps every value $f(\varphi(x))$ and every point between $\varphi(a)$ and
  $\varphi(b)$ inside the domain of $f$.
* $\varphi$ need **not** be injective and need **not** be monotone. If $\varphi$ reverses direction, the
  right-hand integral counts the backward passage with the appropriate sign, which is exactly what the
  left-hand Riemann sums do.

### Solution 34

*Strategy: check the identity on the four functions $1, x, x^2, x^3$, then use linearity.*

On the panel $[-h,h]$ the rule is $S = \frac h3\left[f(-h)+4f(0)+f(h)\right]$.

* $f = 1$: $S = \frac h3(1+4+1) = 2h$ and $\int_{-h}^{h}1\,dx = 2h$. ✓
* $f = x$: $S = \frac h3(-h+0+h) = 0$ and $\int_{-h}^{h}x\,dx = 0$. ✓
* $f = x^2$: $S = \frac h3(h^2+0+h^2) = \frac{2h^3}{3}$ and
  $\int_{-h}^{h}x^2dx = \frac{2h^3}{3}$. ✓
* $f = x^3$: $S = \frac h3(-h^3+0+h^3) = 0$ and $\int_{-h}^{h}x^3dx = 0$. ✓

Now let $f(x) = \alpha x^3+\beta x^2+\gamma x+\delta$ be arbitrary. Both the rule $S$ and the integral
$\int_{-h}^{h}f$ are linear in $f$: for functions $f_1,f_2$ and constants $\lambda,\mu$,
$S[\lambda f_1+\mu f_2] = \lambda S[f_1]+\mu S[f_2]$ and
$\int(\lambda f_1+\mu f_2) = \lambda\int f_1+\mu\int f_2$, because both are finite sums of values times
fixed coefficients. Since the two linear functionals agree on the basis $1,x,x^2,x^3$ of the space of
cubics, they agree on every linear combination of them, that is, on every cubic. $\blacksquare$

*Consequence.* For a cubic, the Simpson error is zero, which is consistent with the error formula
$-\frac{(b-a)h^4}{180}f^{(4)}(\xi)$: the fourth derivative of a cubic vanishes.

### Solution 35

*Strategy: apply $t = \tan(x/2)$ to turn the integrand into a rational function, then complete the
square.*

*Step 1: the substitution.* With $t = \tan(x/2)$,
$\sin x = \frac{2t}{1+t^2}$ and $dx = \frac{2dt}{1+t^2}$, so

$$\int\frac{dx}{2+\sin x} = \int\frac{\frac{2dt}{1+t^2}}{2+\frac{2t}{1+t^2}}
= \int\frac{2\,dt}{2(1+t^2)+2t} = \int\frac{dt}{t^2+t+1}.$$

*Step 2: complete the square.* $t^2+t+1 = \left(t+\frac12\right)^2+\frac34$, so with $u = t+\frac12$ and
$a = \frac{\sqrt3}{2}$,

$$\int\frac{dt}{t^2+t+1} = \frac{2}{\sqrt3}\arctan\left(\frac{2t+1}{\sqrt3}\right) + C_1 .$$

*Step 3: back-substitute.*

$$\int\frac{dx}{2+\sin x} = \frac{2}{\sqrt3}\arctan\left(\frac{2\tan\frac x2+1}{\sqrt3}\right) + C .$$

*Check.* Since $dt/dx = \frac12\sec^2(x/2) = \frac{1+t^2}{2}$ and
$\frac{d}{dt}\left[\frac{2}{\sqrt3}\arctan\frac{2t+1}{\sqrt3}\right] = \frac{1}{t^2+t+1}$, the derivative
in $x$ is $\frac{1+t^2}{2(t^2+t+1)}$. But
$\frac{1}{2+\sin x} = \frac{1}{2+\frac{2t}{1+t^2}} = \frac{1+t^2}{2(1+t^2)+2t} = \frac{1+t^2}{2(t^2+t+1)}$.
✓

*Intervals.* The substitution is defined for $x \ne (2k+1)\pi$, that is, off the odd multiples of $\pi$.
On any open interval not containing such a point it is a bijection onto $\mathbb{R}$ in $t$ and the
formula above is an antiderivative.

*What happens at odd multiples of $\pi$.* As $x\to\pi^-$, $t\to+\infty$ and
$\arctan\left(\frac{2t+1}{\sqrt3}\right)\to\frac{\pi}{2}$; as $x\to\pi^+$, $t\to-\infty$ and the arctangent
tends to $-\frac{\pi}{2}$. The displayed expression therefore jumps by $\frac{2}{\sqrt3}\cdot\pi$ at
$x=\pi$. The *integrand* has no singularity there ($2+\sin x \ge 1$), so it has an antiderivative
continuous on all of $\mathbb{R}$: one adds the constant $\frac{2\pi}{\sqrt3}$ to the right of each odd
multiple of $\pi$. The formula with a single constant is valid on each interval between consecutive odd
multiples of $\pi$, which is exactly what an indefinite integral on an interval means.

### Solution 36

*Strategy: write the integral as $I$, transform it by $x \mapsto \frac{\pi}{2}-x$ to get the same integral
with $\cos$, then combine the two using $\sin x\cos x = \frac{\sin 2x}{2}$.*

*Step 1: convergence.* For $0<x\le\frac{\pi}{2}$,
$\ln(\sin x) = \ln x + \ln\left(\frac{\sin x}{x}\right)$, and $\frac{\sin x}{x}\to1$, so the second
logarithm is bounded near $0$; since $\int_0^{\pi/2}\ln x\,dx$ converges (an antiderivative is
$x\ln x - x$, which tends to $0$ as $x\to0^+$), the improper integral
$I = \int_0^{\pi/2}\ln(\sin x)\,dx$ converges.

*Step 2: the substitution.* With $u = \frac{\pi}{2}-x$, $du = -dx$, and $\sin\left(\frac{\pi}{2}-u\right) = \cos u$:

$$I = \int_0^{\pi/2}\ln(\sin x)\,dx = \int_0^{\pi/2}\ln(\cos u)\,du .$$

(Formally, apply the substitution to $\int_\varepsilon^{\pi/2}$ and let $\varepsilon\to0^+$.)

*Step 3: combine.*

$$2I = \int_0^{\pi/2}\left[\ln(\sin x)+\ln(\cos x)\right]dx = \int_0^{\pi/2}\ln\left(\sin x\cos x\right)dx
= \int_0^{\pi/2}\ln\left(\frac{\sin 2x}{2}\right)dx .$$

By linearity of the integral,

$$2I = \int_0^{\pi/2}\ln(\sin 2x)\,dx - \frac{\pi}{2}\ln 2 .$$

*Step 4: reduce the first term to $I$.* With $v = 2x$, $dx = \frac12dv$,
$\int_0^{\pi/2}\ln(\sin 2x)dx = \frac12\int_0^{\pi}\ln(\sin v)\,dv$. By the symmetry
$\sin(\pi-v) = \sin v$,

$$\int_0^{\pi}\ln(\sin v)\,dv = 2\int_0^{\pi/2}\ln(\sin v)\,dv = 2I .$$

Hence $\int_0^{\pi/2}\ln(\sin 2x)dx = \frac12\cdot2I = I$, and

$$2I = I - \frac{\pi}{2}\ln 2, \qquad\text{so}\qquad I = -\frac{\pi}{2}\ln 2 . \;\blacksquare$$

*Check numerically:* $-\frac{\pi}{2}\ln2 \approx -1.0888$. Numerical integration of $\ln(\sin x)$ over
$[10^{-3},\pi/2]$ gives $\approx -1.0809$, and the omitted tail is
$\int_0^{10^{-3}}\ln(\sin x)\,dx \approx \int_0^{10^{-3}}\ln x\,dx = 10^{-3}\ln 10^{-3}-10^{-3} \approx -0.0079$,
which accounts for the difference exactly as expected. ✓

*Pitfall:* the substitution in Step 2 is applied to an improper integral. It is justified by applying it
to $\int_\varepsilon^{\pi/2}$ and then letting $\varepsilon\to0^+$; the convergence established in Step 1
is what makes the limit legal.