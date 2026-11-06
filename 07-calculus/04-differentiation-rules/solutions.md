# Differentiation Rules — Solutions

> [Tutorial](README.md) · [Exercises](exercises.md)

Each solution names the rule used, shows the intermediate algebra, and gives a check where one is available.
The checks are not decoration: a missing chain factor or a reversed quotient numerator often produces an
answer that looks plausible but fails a single numerical substitution.

## Beginner

**1.** Strategy: linearity plus the power rule, term by term.

$$f'(x) = 3\cdot5x^4 - 7\cdot2x + 4 - 0 = 15x^4-14x+4.$$

The constant $-11$ contributes nothing because its graph is horizontal. *Check at $x=1$:* the formula gives
$15-14+4 = 5$; numerically $f(1.001)-f(1)\approx0.005$, so the slope is about $5$. ✓

**2.** Strategy: write the reciprocal as a power, then use the power rule.

$$f(x) = x^3+x^{-1} \Longrightarrow f'(x) = 3x^2 - x^{-2} = 3x^2-\frac{1}{x^2}.$$

*Check at $x=1$:* $f'(1) = 2$; numerically $f(1.001)-f(1) = (1.001^3 + 1/1.001) - 2 \approx 0.002$, so the
slope is about $2$. ✓ The formula is valid for $x\ne0$, the domain of $f$.

**3.** Strategy: both terms are powers of $x$.

$$f(x) = x^{1/2}+x^{-1/2} \Longrightarrow f'(x) = \tfrac12x^{-1/2}-\tfrac12x^{-3/2} = \frac{1}{2\sqrt x}-\frac{1}{2x\sqrt x}.$$

Both terms are defined for $x>0$. *Check at $x=1$:* $f'(1) = \tfrac12-\tfrac12 = 0$. Indeed $f(x) = \sqrt x +
1/\sqrt x$ has a minimum at $x=1$ (by AM–GM, $\sqrt x + 1/\sqrt x\ge2$ with equality at $x=1$), so the
derivative vanishes there. ✓

**4.** Strategy: product rule first; then expand to verify.

*Product rule*, with $u = x^2+1$ and $v = x^3-2x$:

$$f'(x) = 2x\left(x^3-2x\right) + \left(x^2+1\right)\left(3x^2-2\right) = 2x^4-4x^2+3x^4+3x^2-2x^2-2 = 5x^4-3x^2-2.$$

*Expansion.* $f(x) = x^5+x^3-2x^3-2x = x^5-x^3-2x$, so $f'(x) = 5x^4-3x^2-2$. ✓ Both routes agree, as they
must.

**5.** Strategy: quotient rule with $u = 2x+1$, $v = x-3$.

$$f'(x) = \frac{2(x-3)-(2x+1)\cdot1}{(x-3)^2} = \frac{2x-6-2x-1}{(x-3)^2} = -\frac{7}{(x-3)^2}.$$

*Check.* $f(x) = \frac{2x+1}{x-3} = 2+\frac{7}{x-3}$, so $f'(x) = -\frac{7}{(x-3)^2}$ by the reciprocal rule.
✓ The derivative is negative everywhere it is defined: both branches of the hyperbola decrease.

**6.** Strategy: chain rule, outer function $u^5$, inner $3x+2$.

$$f'(x) = 5(3x+2)^4\cdot3 = 15(3x+2)^4.$$

*Check at $x=0$:* the formula gives $15\cdot16 = 240$. Numerically $f(0.001)-f(0) = 2.003^5-32 \approx 0.2407$,
so the slope is about $240.7$. ✓ A missing factor $3$ would give $80$, which the numerical check rejects.

**7.** Outer $\sin$, inner $5x$:

$$f'(x) = \cos(5x)\cdot5 = 5\cos(5x).$$

*Check at $x=0$:* $f'(0) = 5$; numerically $\sin(0.005)/0.001 \approx 5$. ✓

**8.** Outer $\exp$, inner $3x$: $f'(x) = e^{3x}\cdot3 = 3e^{3x}$.

*Check.* $f'(x)/f(x) = 3$, the constant relative growth rate of an exponential with rate $3$. ✓

**9.** Outer $\ln$, inner $4x+1$, whose derivative is $4$:

$$f'(x) = \frac{1}{4x+1}\cdot4 = \frac{4}{4x+1}.$$

*Check.* $\ln(4x+1) = \ln4+\ln\left(x+\tfrac14\right)$, whose derivative is $1/\left(x+\tfrac14\right) =
4/(4x+1)$. ✓ The constant $\ln4$ disappears, as it must.

**10.** Outer $\cos$, inner $x^2$:

$$f'(x) = -\sin(x^2)\cdot2x = -2x\sin(x^2).$$

*Check at $x=0$:* the formula gives $0$, and $x=0$ is where $\cos(x^2)$ attains its maximum value $1$. ✓

**11.** Outer square root, inner $x^2+9$:

$$f'(x) = \frac{1}{2\sqrt{x^2+9}}\cdot2x = \frac{x}{\sqrt{x^2+9}}.$$

*Check.* The derivative is negative for $x<0$ and positive for $x>0$, and $\sqrt{x^2+9}$ is a symmetric
U-shaped curve with its minimum at $0$. ✓ Note $\lvert f'\rvert<1$ always, so the curve never rises faster than
$45^\circ$ — it approaches the lines $y = \pm x$ as asymptotes.

**12.** With $u = \sin x$, $v = \cos x$:

$$\frac{d}{dx}\tan x = \frac{\cos x\cdot\cos x-\sin x\cdot(-\sin x)}{\cos^2x} = \frac{\cos^2x+\sin^2x}{\cos^2x} = \frac{1}{\cos^2x} = \sec^2x.$$

*Check at $x=\pi/4$:* $\sec^2(\pi/4) = 2$; the tangent graph is rising with slope $2$ there, consistent with
$\tan$ increasing from $0$ to $1$ over an interval of length $\pi/4\approx0.785$. ✓

**13.** Write $2^x = e^{x\ln2}$; the inner derivative is the constant $\ln2$:

$$f'(x) = e^{x\ln2}\cdot\ln2 = 2^x\ln2.$$

*Check at $x=0$:* $f'(0) = \ln2\approx0.6931$; numerically $(2^{0.001}-1)/0.001 \approx 0.6934$. ✓

**14.** Strategy: differentiate each term with its own base.

$$\frac{d}{dx}\log_{10}x = \frac{1}{x\ln10}, \qquad \frac{d}{dx}\ln x = \frac1x, \qquad f'(x) = \frac{1}{x\ln10}+\frac1x.$$

*Check.* $\frac{1}{\ln10}\approx0.4343$, so the first term dominates slightly; both terms are positive because
both functions increase. ✓

## Intermediate

**15.** Product rule with $u = x^2$, $v = e^x$:

$$f'(x) = 2x\,e^x + x^2e^x = x(x+2)e^x.$$

*Check.* The derivative vanishes at $x=0$ and $x=-2$, which are the two stationary points; for $x>0$ both
factors are positive, so $f$ increases there. ✓

**16.** Product rule with $u = x$, $v = \ln x$:

$$f'(x) = 1\cdot\ln x + x\cdot\frac1x = \ln x+1.$$

*Check.* $f'(x)=0$ at $x = e^{-1}$, where $x\ln x = -e^{-1}\approx-0.368$ is the minimum of $x\ln x$ on
$(0,\infty)$. ✓

**17.** Quotient rule with $u = \sin x$, $v = x$:

$$f'(x) = \frac{\cos x\cdot x-\sin x\cdot1}{x^2} = \frac{x\cos x-\sin x}{x^2}.$$

*Check as $x\to0$.* Using $\sin x\approx x-x^3/6$ and $\cos x\approx1-x^2/2$, the numerator is
$x-x^3/2-x+x^3/6 = -x^3/3$, so $f'(x)\approx-x/3\to0$: the sinc function is flat at $0$, as its graph shows.
✓

**18.** Product rule with $u = e^x$, $v = \sin x$:

$$f'(x) = e^x\sin x + e^x\cos x = e^x(\sin x+\cos x).$$

*Check.* The derivative vanishes where $\tan x = -1$, i.e. $x = -\pi/4+k\pi$; those are the extrema of
$e^x\sin x$. ✓

**19.** Chain rule with outer $\ln$ and inner $\sin x$:

$$f'(x) = \frac{1}{\sin x}\cdot\cos x = \cot x.$$

This is valid where $\sin x>0$, i.e. on $(0,\pi)$. *Check:* on $\left(0,\frac\pi2\right)$ the sine increases, so
$\ln(\sin x)$ increases and $\cot x>0$; on $\left(\frac\pi2,\pi\right)$ both signs reverse. ✓

**20.** Outer $u^{10}$, inner $x^2+1$:

$$f'(x) = 10\left(x^2+1\right)^9\cdot2x = 20x\left(x^2+1\right)^9.$$

*Check at $x=0$:* the formula gives $0$; $x=0$ is the minimum of $\left(x^2+1\right)^{10}$. ✓

**21.** Outer $\arctan$, inner $3x$:

$$f'(x) = \frac{1}{1+(3x)^2}\cdot3 = \frac{3}{1+9x^2}.$$

The trap is writing $1/(1+3x^2)$: the argument of the arctangent is squared as a whole, so $1+9x^2$ is
correct. *Check at $x=0$:* slope $3$, the steepest point of the graph. ✓

**22.** Outer $\arcsin$, inner $x/2$:

$$f'(x) = \frac{1}{\sqrt{1-\left(\frac x2\right)^2}}\cdot\frac12 = \frac{1}{2\sqrt{1-\frac{x^2}{4}}} = \frac{1}{\sqrt{4-x^2}}.$$

*Check at $x=0$:* slope $\tfrac12$, which is $\cos(0)^{-1}\cdot\tfrac12$ as expected since $\arcsin(x/2)$ has
inner derivative $\tfrac12$. ✓ At $x=\pm2$ the derivative is infinite: vertical tangents at the ends of the
domain.

**23.** Strategy: differentiate the equation, remembering $y = y(x)$.

$$2x+2y\,y' = 0 \Longrightarrow y' = -\frac xy.$$

At $(3,4)$: $y' = -\tfrac34$. The tangent is

$$y = 4-\tfrac34(x-3) = -\tfrac34x+\tfrac{25}{4}.$$

*Check.* The radius to $(3,4)$ has slope $\tfrac43$, and the tangent should be perpendicular to it:
$-\tfrac34\cdot\tfrac43 = -1$. ✓ Also the tangent meets the circle only at $(3,4)$, since substituting gives a
double root.

**24.** Differentiate term by term, attaching $y'$ to every $y$-term:

$$2x + \left(y+xy'\right) + 2y\,y' = 0.$$

Collect: $\left(x+2y\right)y' = -(2x+y)$, so

$$y' = -\frac{2x+y}{x+2y}.$$

At $(1,2)$: $y' = -\frac{2+2}{1+4} = -\frac45$. *Check the point:* $1+2+4 = 7$ ✓. The denominator $x+2y = 5$
is nonzero, so the implicit function theorem applies and the tangent is not vertical.

**25.** Strategy: take logarithms, expand, differentiate implicitly, multiply by $y$.

$$\ln y = x\ln x \Longrightarrow \frac{y'}{y} = \ln x + x\cdot\frac1x = \ln x+1 \Longrightarrow y' = x^x(\ln x+1).$$

*Check.* At $x=1$: $y = 1$ and $y' = 1$; a numerical difference gives $(1.001^{1.001}-1)/0.001\approx1.001$. ✓
The formula is valid for $x>0$, the domain of $x^x$ as a real function.

**26.** $\ln y = x\ln(\sin x)$, hence

$$\frac{y'}{y} = \ln(\sin x) + x\cdot\frac{\cos x}{\sin x}, \qquad y' = (\sin x)^x\left(\ln(\sin x)+x\cot x\right).$$

This requires $\sin x>0$, true on $(0,\pi)$. *Check at $x=\frac\pi2$:* $\ln 1+(\frac\pi2)(0) = 0$, so the
derivative vanishes; indeed $1^x = 1$ has a minimum there, since $(\sin x)^x\le1$. ✓

## Advanced

**27.** Strategy: prove the reciprocal rule from the definition by a common denominator, then combine it with
the product rule.

*Reciprocal rule.* Let $G = 1/g$ with $g(a)\ne0$. For $h\ne0$ small enough that $g(a+h)\ne0$ (possible by
continuity of $g$),

$$\frac{G(a+h)-G(a)}{h} = \frac{1}{h}\left(\frac{1}{g(a+h)}-\frac{1}{g(a)}\right) = \frac{g(a)-g(a+h)}{h\,g(a+h)g(a)} = -\frac{g(a+h)-g(a)}{h}\cdot\frac{1}{g(a+h)g(a)}.$$

As $h\to0$ the first factor tends to $-g'(a)$, and the second to $1/g(a)^2$ because $g$ is continuous at $a$ and
$g(a)\ne0$. Hence $G'(a) = -g'(a)/g(a)^2$. $\blacksquare$

*Quotient rule.* Write $f/g = f\cdot G$ with $G = 1/g$. The product rule (Theorem 7.4) gives

$$\left(f\cdot G\right)' = f'G+fG' = \frac{f'}{g} + f\left(-\frac{g'}{g^2}\right) = \frac{f'g-fg'}{g^2}. \qquad\blacksquare$$

This is a genuinely independent proof of Theorem 7.6: it uses only the product rule and a direct limit
computation.

**28.** Strategy: apply the inverse rule to $f(y) = \sec y$ on the branch $[0,\pi]\setminus\left\{\frac\pi2\right\}$,
where $\sec$ is strictly monotone on each piece.

Let $y = \operatorname{arcsec}x$ with $\lvert x\rvert\ge1$, so $\sec y = x$ and $y\in\left[0,\frac\pi2\right)$
when $x\ge1$, $y\in\left(\frac\pi2,\pi\right]$ when $x\le-1$. On that branch,

$$f'(y) = \sec y\tan y, \qquad \left(\operatorname{arcsec}\right)'(x) = \frac{1}{\sec y\tan y}.$$

Now $\tan^2y = \sec^2y-1 = x^2-1$, so $\lvert\tan y\rvert = \sqrt{x^2-1}$. It remains to determine the sign of
the product. If $x\ge1$ then $y\in\left[0,\frac\pi2\right)$ and both $\sec y = x>0$ and $\tan y\ge0$ are
non-negative, so the product is positive. If $x\le-1$ then $y\in\left(\frac\pi2,\pi\right]$ and *both*
$\sec y = x<0$ and $\tan y\le0$ are negative, so the product is again positive. Therefore

$$\sec y\tan y = \lvert x\rvert\sqrt{x^2-1}, \qquad \left(\operatorname{arcsec}\right)'(x) = \frac{1}{\lvert x\rvert\sqrt{x^2-1}}.$$

The absolute value is essential: the product is positive on both branches even though $x$ changes sign, so
$1/(x\sqrt{x^2-1})$ would be negative for $x<-1$, which is impossible since $\operatorname{arcsec}$ is
increasing on both branches. $\blacksquare$

**29.** Strategy: differentiate $y' = -x/y$ implicitly, then use the equation of the circle to simplify.

$$y'' = \frac{d}{dx}\left(-\frac xy\right) = -\frac{1\cdot y - x\,y'}{y^2}.$$

Substituting $y' = -x/y$:

$$y'' = -\frac{y+\frac{x^2}{y}}{y^2} = -\frac{y^2+x^2}{y^3} = -\frac{25}{y^3}.$$

*Concavity.* On the upper semicircle $y>0$, so $y''<0$: the graph is concave down, as the picture of a
semicircle requires. On the lower semicircle $y<0$, so $y''>0$: concave up (equivalently, concave down when
viewed from below). At $y=\pm5$ the formula is undefined, consistent with the vertical tangents at $(\pm5,0)$.
✓

**30.** Strategy: logarithmic differentiation, since both base and exponent vary.

$$\ln y = \sqrt x\ln x, \qquad \frac{y'}{y} = \frac{1}{2\sqrt x}\ln x + \sqrt x\cdot\frac1x = \frac{\ln x}{2\sqrt x}+\frac{1}{\sqrt x} = \frac{\ln x+2}{2\sqrt x}.$$

Hence

$$y' = x^{\sqrt x}\,\frac{\ln x+2}{2\sqrt x}.$$

*Check at $x=1$:* $y = 1$, and the formula gives $2/2 = 1$; numerically
$\left(1.001^{\sqrt{1.001}}-1\right)/0.001 \approx 1.0005$, so the slope is $1$ to three decimal places. ✓

**31.** *Away from $0$.* By Theorem 7.16 with $r = \tfrac23$,

$$f'(x) = \tfrac23x^{-1/3} = \frac{2}{3\sqrt[3]{x}}, \qquad x\ne0.$$

For $x>0$ this is positive; for $x<0$, $\sqrt[3]{x}<0$ so the derivative is negative. This matches the graph:
$x^{2/3}$ increases for $x>0$ and decreases for $x<0$, with a cusp at the origin.

*At $0$.* The difference quotient is $h^{2/3}/h = h^{-1/3}$, which tends to $+\infty$ as $h\to0^+$ and to
$-\infty$ as $h\to0^-$. So $f'(0)$ does not exist.

*Does the formula describe the one-sided behaviour?* Yes. As $x\to0^+$, $\tfrac23x^{-1/3}\to+\infty$, matching
the right-hand difference quotients; as $x\to0^-$, $\tfrac23x^{-1/3}\to-\infty$, matching the left-hand ones.
The formula is therefore correct on the whole punctured domain and signals the cusp by its divergence. ✓

**32.** By the chain rule,

$$(f\circ g)'(3) = f'\left(g(3)\right)g'(3) = f'(2)\cdot4 = (-1)\cdot4 = -4,$$

$$(g\circ f)'(2) = g'\left(f(2)\right)f'(2) = g'(3)\cdot(-1) = 4\cdot(-1) = -4.$$

They are equal *of necessity*, not by coincidence: both equal the product $f'(2)\,g'(3)$ of the same two
numbers, written in the opposite order. In general, for $a$ with all compositions defined,
$(f\circ g)'(a)$ and $(g\circ f)'(g(a))$ need not be equal — the evaluations occur at different points — but
in this problem the two expressions collapse to the same product. *Moral:* the chain rule multiplies the
"outer derivative at the inner value" by the "inner derivative"; the order of multiplication is irrelevant, but
the points of evaluation are not.

## Challenge

**33.** Strategy: take logarithms of $y = x^{x^x}$; the right side still contains a variable exponent, so it
must be differentiated by logarithmic differentiation again — or handled as $x^x = e^{x\ln x}$.

$$\ln y = x^x\ln x.$$

Differentiate both sides in $x$, using the product rule and the known derivative $(x^x)' = x^x(\ln x+1)$:

$$\frac{y'}{y} = \left(x^x\right)'\ln x + x^x\cdot\frac1x = x^x(\ln x+1)\ln x + x^{x-1},$$

since $x^x/x = x^{x-1}$. Hence

$$y' = x^{x^x}\left[x^x(\ln x+1)\ln x + x^{x-1}\right], \qquad x>0.$$

*Check at $x=1$:* $y = 1^{1} = 1$ and the bracket is $1\cdot(0+1)\cdot0+1 = 1$. Numerically,
$\left(1.001^{1.001^{1.001}}-1\right)/0.001\approx1.001$, so the slope is about $1$. ✓

**34.** Strategy: invert the difference quotient, as in Theorem 7.9, and be explicit about every hypothesis.

*Statement.* Let $f$ be continuous and strictly monotone on an open interval $I$, differentiable at $a\in I$
with $f'(a)\ne0$, and put $b = f(a)$. Then $f^{-1}$ is differentiable at $b$ and
$(f^{-1})'(b) = 1/f'(a)$.

*Proof.* Strict monotonicity makes $f$ injective, so $f^{-1}$ is defined on $f(I)$; by hypothesis $f^{-1}$ is
continuous. Take $x\in f(I)$, $x\ne b$, and put $y = f^{-1}(x)$, so $y\ne a$ and $f(y) = x$. Then

$$\frac{f^{-1}(x)-f^{-1}(b)}{x-b} = \frac{y-a}{f(y)-f(a)} = \frac{1}{\dfrac{f(y)-f(a)}{y-a}}.$$

As $x\to b$, continuity of $f^{-1}$ at $b$ gives $y\to a$. The denominator therefore tends to $f'(a)\ne0$, so
the quotient tends to $1/f'(a)$ by the quotient law. Hence the limit exists and equals $1/f'(a)$.
$\blacksquare$

*Application.* Take $f(y) = \tan y$ on $\left(-\frac\pi2,\frac\pi2\right)$, which is continuous, strictly
increasing, and $f'(y) = \sec^2y = 1+\tan^2y\ne0$. With $x = \tan y$,

$$\left(\arctan\right)'(x) = \frac{1}{1+\tan^2y} = \frac{1}{1+x^2}.$$

*Check at $x=1$:* the formula gives $\tfrac12$, and the arctangent graph rises from $0$ to $\pi/4\approx0.785$
over $[0,1]$, an average slope of $0.785$; at the upper end the slope $\tfrac12$ is smaller, consistent with
the curve flattening. ✓

**35.** Strategy: differentiate $\sin y = x$ implicitly, then fix the sign of $\cos y$ from the branch.

*Branch.* Restrict $\sin$ to $\left[-\frac\pi2,\frac\pi2\right]$ so that $\arcsin:[-1,1]\to\left[-\frac\pi2,
\frac\pi2\right]$. For $x\in(-1,1)$ put $y = \arcsin x$, so $\sin y = x$ and $y\in\left(-\frac\pi2,\frac\pi2\right)$.

*Differentiate.* Both sides are differentiable in $x$ (the left because $y$ is differentiable — this is what
Theorem 7.9 supplies — and the right trivially):

$$\cos y\cdot y' = 1 \Longrightarrow y' = \frac{1}{\cos y}.$$

*Sign of $\cos y$.* On the open interval $\left(-\frac\pi2,\frac\pi2\right)$ the cosine is strictly positive.
Therefore $\cos y = +\sqrt{1-\sin^2y} = \sqrt{1-x^2}$ and

$$y' = \frac{1}{\sqrt{1-x^2}}, \qquad \lvert x\rvert<1.$$

*Endpoints.* At $x = \pm1$ we have $\cos y = 0$, so the formula's denominator vanishes: the arcsine graph has
vertical tangents at $\left(\pm1,\pm\frac\pi2\right)$ and the derivative is infinite (not finite), hence
$\arcsin$ is not differentiable at $\pm1$. This is exactly the case $f'(a)=0$ excluded by the inverse rule,
with $f = \sin$ at $a = \pm\frac\pi2$. ✓

**36.** Strategy: get the slope from implicit differentiation, impose the required slope, and use the ellipse
equation to locate the points.

*Slope.* Differentiate $\frac{x^2}{9}+\frac{y^2}{4} = 1$:

$$\frac{2x}{9}+\frac{2y\,y'}{4} = 0 \Longrightarrow \frac{x}{9}+\frac{y\,y'}{2} = 0 \Longrightarrow y' = -\frac{2x}{9}\cdot\frac{2}{y} = -\frac{4x}{9y}.$$

*Impose $y' = -1$:* $\dfrac{4x}{9y} = 1$, so $4x = 9y$ and $y = \dfrac{4x}{9}$.

*Substitute into the ellipse.*

$$\frac{x^2}{9}+\frac{1}{4}\cdot\frac{16x^2}{81} = 1 \Longrightarrow \frac{x^2}{9}+\frac{4x^2}{81} = 1 \Longrightarrow \frac{9x^2+4x^2}{81} = 1 \Longrightarrow 13x^2 = 81.$$

So $x = \pm\dfrac{9}{\sqrt{13}}$ and, since $y$ has the same sign as $x$, $y = \pm\dfrac{4}{\sqrt{13}}$.

*Tangents.* With slope $-1$ through $\left(\frac{9}{\sqrt{13}},\frac{4}{\sqrt{13}}\right)$, the intercept is
$y+x = \frac{13}{\sqrt{13}} = \sqrt{13}$; for the opposite point it is $-\sqrt{13}$. Hence

$$y = -x+\sqrt{13} \qquad\text{and}\qquad y = -x-\sqrt{13}.$$

*Check.* The tangent line $y = -x+\sqrt{13}$ meets the ellipse where $\frac{x^2}{9}+\frac{( -x+\sqrt{13})^2}{4}
= 1$; this quadratic in $x$ has discriminant zero, so the line touches at exactly one point — as a tangent must.
$\sqrt{13}\approx3.606$ exceeds the semi-axis $3$, so the line is outside the ellipse except at the tangency
point. ✓

**37.** Strategy: exhibit the failure, then explain which ingredient of the Carathéodory proof replaces the
division.

*The failure.* Take $g(x) = 0$ for all $x$ and $a = 0$. Then $g(a+h)-g(a) = 0$ for every $h$, so the naive
argument would require the fraction $\frac{f(g(a+h))-f(g(a))}{g(a+h)-g(a)} = \frac{0}{0}$, undefined for every
$h\ne0$.

A subtler example: $g(0) = 0$ and $g(x) = x^2\sin(1/x)$ for $x\ne0$. At $a = 0$, $g(a+h) - g(a) = h^2\sin(1/h)$,
which equals $0$ whenever $1/h = n\pi$, i.e. for the sequence $h_n = 1/(n\pi)\to0$. So the denominator vanishes
infinitely often in every neighbourhood of $0$, and no amount of care with a single $h$ repairs the argument.
(Here $g'(0) = 0$, as the bound $\lvert g(h)/h\rvert\le\lvert h\rvert$ shows.)

*How Carathéodory avoids it.* The proof writes $f(g(x))-f(g(a)) = \varphi(g(x))\,[g(x)-g(a)]$ with $\varphi$
continuous, and then $g(x)-g(a) = \psi(x)(x-a)$. Multiplying,

$$f(g(x))-f(g(a)) = \varphi(g(x))\psi(x)(x-a),$$

and no quotient by $g(x)-g(a)$ ever appears: the factor $g(x)-g(a)$ is *replaced*, not divided. When
$g(x) = g(a)$ the identity remains true (both sides are $0$), and the product $\varphi(g(x))\psi(x)$ is still
continuous at $a$.

*Verification.* For $g\equiv0$, $f\circ g$ is the constant $f(0)$, whose derivative is $0$, and the chain rule
predicts $f'(g(0))\,g'(0) = f'(0)\cdot0 = 0$. ✓ For $g(x) = x^2\sin(1/x)$, the rule predicts
$f'(0)\cdot0 = 0$, and indeed $\frac{f(g(h))-f(g(0))}{h} = \frac{f(g(h))-f(0)}{h}$, which is bounded by a
constant times $\lvert g(h)/h\rvert \le \lvert h\rvert\to0$ when $f$ is locally Lipschitz at $0$ — in
particular when $f$ is differentiable there. So the conclusion holds in both examples even though the naive
proof does not apply. $\blacksquare$

**38.** *Three factors.* Apply the product rule to the product $(uv)$ and $w$:

$$(uvw)' = \left[(uv)w\right]' = (uv)'w + (uv)w' = \left(u'v+uv'\right)w + uvw' = u'vw+uv'w+uvw'. \qquad\blacksquare$$

*Not $u'v'w'$.* Take $u = v = w = x$. The correct derivative is $(x^3)' = 3x^2$, while $u'v'w' = 1\cdot1\cdot1
= 1$. The two differ for every $x\ne0$, so the "all primes" guess is not merely imprecise but wrong.

*Induction.* Let $P_n$ be the statement
$\left(u_1\cdots u_n\right)' = \sum_{k=1}^{n}u_1\cdots u_{k-1}u_k'u_{k+1}\cdots u_n$.

*Base $n=1$:* the sum has the single term $u_1'$, and $(u_1)' = u_1'$. ✓

*Step.* Assume $P_{n-1}$ and write $U = u_1\cdots u_{n-1}$. By the product rule,

$$\left(Uu_n\right)' = U'u_n + Uu_n'.$$

By $P_{n-1}$, $U' = \sum_{k=1}^{n-1}u_1\cdots u_k'\cdots u_{n-1}$, so

$$\left(Uu_n\right)' = \sum_{k=1}^{n-1}u_1\cdots u_k'\cdots u_{n-1}u_n + u_1\cdots u_{n-1}u_n',$$

which is exactly the $n$-term sum of $P_n$: the first $n-1$ terms differentiate one of the first $n-1$
factors, and the last differentiates $u_n$. Hence $P_n$ holds for all $n\ge1$. $\blacksquare$

*Remark.* The formula requires all $n$ factors to be differentiable at the point. It also explains the
combinatorial shape of the product rule's iterates: the $m$-th derivative of a product is
$\sum_k\binom{m}{k}u^{(k)}v^{(m-k)}$ (Leibniz's formula), which is the binomial theorem for differentiation.
