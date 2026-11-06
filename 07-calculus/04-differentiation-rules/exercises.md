# Differentiation Rules — Exercises

> [Tutorial](README.md) · [Solutions](solutions.md)

State which rule you are using before you use it; that habit alone prevents most errors. Simplify before
differentiating when the algebra allows it (a quotient with a constant denominator, a product that expands
neatly), and check at least a few answers by differentiating a second way or by substituting a number.
Problems 27–32 are proofs or multi-step computations; 33–38 are challenge problems, where a complete answer
includes the reasoning.

## Beginner

**1.** Differentiate $f(x) = 3x^5 - 7x^2 + 4x - 11$.

**2.** Differentiate $f(x) = x^3 + \dfrac1x$.

**3.** Differentiate $f(x) = \sqrt{x} + \dfrac{1}{\sqrt{x}}$ for $x>0$.

**4.** Differentiate $f(x) = (x^2+1)(x^3-2x)$ by the product rule, then verify by expanding first.

**5.** Differentiate $f(x) = \dfrac{2x+1}{x-3}$.

**6.** Differentiate $f(x) = (3x+2)^5$.

**7.** Differentiate $f(x) = \sin(5x)$.

**8.** Differentiate $f(x) = e^{3x}$.

**9.** Differentiate $f(x) = \ln(4x+1)$ for $x > -\tfrac14$.

**10.** Differentiate $f(x) = \cos(x^2)$.

**11.** Differentiate $f(x) = \sqrt{x^2+9}$.

**12.** Differentiate $f(x) = \tan x$ by writing it as $\dfrac{\sin x}{\cos x}$ and using the quotient rule.
Simplify the numerator using $\sin^2x+\cos^2x=1$.

**13.** Differentiate $f(x) = 2^x$.

**14.** Differentiate $f(x) = \log_{10}x + \ln x$ for $x>0$.

## Intermediate

**15.** Differentiate $f(x) = x^2e^x$.

**16.** Differentiate $f(x) = x\ln x$ for $x>0$.

**17.** Differentiate $f(x) = \dfrac{\sin x}{x}$ for $x\ne0$.

**18.** Differentiate $f(x) = e^x\sin x$.

**19.** Differentiate $f(x) = \ln(\sin x)$ on $(0,\pi)$.

**20.** Differentiate $f(x) = (x^2+1)^{10}$.

**21.** Differentiate $f(x) = \arctan(3x)$.

**22.** Differentiate $f(x) = \arcsin\dfrac{x}{2}$ for $\lvert x\rvert<2$.

**23.** The circle $x^2+y^2=25$ passes through $(3,4)$. Find $\dfrac{dy}{dx}$ by implicit differentiation and
the tangent line at that point.

**24.** The curve $x^2+xy+y^2=7$ passes through $(1,2)$. Find $\dfrac{dy}{dx}$ and its value there.

**25.** Differentiate $y = x^x$ for $x>0$ by logarithmic differentiation.

**26.** Differentiate $y = (\sin x)^x$ for $0<x<\pi$.

## Advanced

**27.** Prove the reciprocal rule $\left(\dfrac1g\right)' = -\dfrac{g'}{g^2}$ from the limit definition, and
deduce the quotient rule from the reciprocal rule and the product rule. (This gives a second, independent
proof of Theorem 7.6.)

**28.** Prove that $\left(\operatorname{arcsec}x\right)' = \dfrac{1}{\lvert x\rvert\sqrt{x^2-1}}$ for
$\lvert x\rvert>1$, explaining where the absolute value comes from.

**29.** For the circle $x^2+y^2=25$, show that $y'' = -\dfrac{25}{y^3}$ and use the sign of $y''$ to describe
the concavity of the upper and lower semicircles.

**30.** Differentiate $y = x^{\sqrt x}$ for $x>0$.

**31.** For $f(x) = x^{2/3}$, find $f'(x)$ on each side of $0$ using Theorem 7.16, and explain why no
derivative exists at $0$. Does the formula $f'(x) = \tfrac23x^{-1/3}$ correctly describe the one-sided
behaviour?

**32.** Suppose $f$ and $g$ are differentiable, with $f(2) = 3$, $f'(2) = -1$, $g(3) = 2$ and $g'(3) = 4$.
Compute $(f\circ g)'(3)$ and $(g\circ f)'(2)$. Explain why the two answers are necessarily equal.

## Challenge

**33.** Differentiate $y = x^{x^x}$ for $x>0$. (Take logarithms twice, or once and simplify carefully.)

**34.** Give a complete proof of the inverse-function rule, assuming that the inverse of a continuous strictly
monotone function on an interval is continuous. Then use the rule to derive $(\arctan x)' = \dfrac{1}{1+x^2}$
from the derivative of $\tan$.

**35.** Derive $(\arcsin x)' = \dfrac{1}{\sqrt{1-x^2}}$ by implicit differentiation of $\sin y = x$, stating
the branch of $y$ used and justifying the sign of $\cos y$. What happens at $x = \pm1$?

**36.** Find all tangent lines to the ellipse $\dfrac{x^2}{9}+\dfrac{y^2}{4} = 1$ that have slope $-1$, and
give the points of tangency exactly.

**37.** The naive proof of the chain rule divides by $g(a+h)-g(a)$. Give an explicit function $g$ and point
$a$ for which this quantity is zero for infinitely many $h$ arbitrarily close to $0$, and explain how the
Carathéodory proof avoids the division. Verify that the chain rule still gives the correct answer in your
example.

**38.** Prove the three-factor product rule $(uvw)' = u'vw+uv'w+uvw'$ from the two-factor rule, and show by
example that it is not $u'v'w'$. Then prove by induction that the derivative of $u_1u_2\cdots u_n$ is the sum
of $n$ terms, each differentiating exactly one factor.
