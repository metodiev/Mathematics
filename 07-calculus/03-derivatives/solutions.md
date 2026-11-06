# Derivatives — Solutions

> [Tutorial](README.md) · [Exercises](exercises.md)

Each solution gives the strategy first, then every significant algebraic step, then a check where one is
available. Decimals appear only when the problem asks for them, and are marked $\approx$. In this topic an
error is almost always either a miscancelled factor of $h$ or a missing minus sign — compare the intermediate
lines, not the final answers.

## Beginner

**1.** Strategy: the average rate of change is a quotient of the *whole* interval; the derivative is a limit at
a *point*.

$$\text{average} = \frac{f(3)-f(1)}{3-1} = \frac{9-1}{2} = 4.$$

From the definition, with $f(1+h) = (1+h)^2 = 1+2h+h^2$,

$$\frac{f(1+h)-f(1)}{h} = \frac{1+2h+h^2-1}{h} = \frac{h(2+h)}{h} = 2+h \longrightarrow 2.$$

So $f'(1) = 2$. The numbers differ because the parabola steepens as $x$ grows: the average over $[1,3]$
blends slopes between $2$ (at $x=1$) and $6$ (at $x=3$). *Check:* $f'(x) = 2x$, so $f'(1)=2$; the average of
$2x$ over $[1,3]$ is $4$. ✓

**2.** Strategy: a linear function has a constant difference quotient.

$$\frac{f(x+h)-f(x)}{h} = \frac{4-5(x+h)-(4-5x)}{h} = \frac{-5h}{h} = -5 \longrightarrow -5.$$

So $f'(x) = -5$ for every $x$: the graph is a straight line of slope $-5$, decreasing, and its tangent is the
line itself. The average rate on $[0,2]$ is $\frac{f(2)-f(0)}{2} = \frac{-6-4}{2} = -5$, the same number —
for a line, average and instantaneous rates agree everywhere.

**3.** Strategy: expand $f(x+h)$, subtract, factor out $h$.

$$f(x+h) = 2(x+h)^2 - 3(x+h) + 1 = 2x^2+4xh+2h^2-3x-3h+1,$$

$$f(x+h)-f(x) = 4xh+2h^2-3h = h(4x+2h-3), \qquad \frac{f(x+h)-f(x)}{h} = 4x+2h-3.$$

Letting $h\to0$: $f'(x) = 4x-3$, hence $f'(2) = 5$. *Check:* the vertex of the parabola is at $x = 3/4$, where
the slope should vanish, and indeed $4(3/4)-3 = 0$. ✓

**4.** Strategy: combine the two fractions before dividing by $h$.

$$f(3+h)-f(3) = \frac{1}{3+h}-\frac13 = \frac{3-(3+h)}{3(3+h)} = \frac{-h}{3(3+h)}, \qquad \frac{f(3+h)-f(3)}{h} = \frac{-1}{3(3+h)}.$$

As $h\to0$ this tends to $-\dfrac{1}{3\cdot3} = -\dfrac19$. *Check:* $\left(\frac1x\right)' = -\frac1{x^2}$, and
$-1/9$ at $x=3$. ✓

**5.** Strategy: rationalise the numerator, which removes the square roots from the difference.

$$\frac{\sqrt{25+h}-5}{h}\cdot\frac{\sqrt{25+h}+5}{\sqrt{25+h}+5} = \frac{(25+h)-25}{h\left(\sqrt{25+h}+5\right)} = \frac{1}{\sqrt{25+h}+5} \longrightarrow \frac{1}{10}.$$

So $f'(25) = \tfrac1{10}$. *Check:* $f'(x) = \frac{1}{2\sqrt x}$ gives $\frac{1}{2\cdot5} = \frac1{10}$. ✓ The
small slope is right: $\sqrt x$ is very flat at $25$.

**6.** By the power rule with $n=4$, $f'(x) = 4x^3$. Hence $f'(-2) = 4(-8) = -32$.

*Check by the definition:* $(x+h)^4 - x^4 = 4x^3h+6x^2h^2+4xh^3+h^4$, so the quotient is
$4x^3+6x^2h+4xh^2+h^3 \to 4x^3$. ✓ The cube is negative at a negative input, consistent with a negative
slope there.

**7.** Strategy: a tangent needs a point and a slope.

$f(x) = x^2-4x$, so $f'(x) = 2x-4$ and $f'(3) = 2$. The point is $f(3) = 9-12 = -3$. Hence

$$y = -3+2(x-3) = 2x-9.$$

*Multiplicity check:* $x^2-4x = 2x-9 \iff x^2-6x+9 = 0 \iff (x-3)^2 = 0$. The root $x=3$ has multiplicity
two, which is exactly the condition for tangency; a transverse crossing would give multiplicity one.

**8.** Strategy: compute both one-sided difference quotients at $a = -1$.

$f(-1) = 0$ and $f(-1+h) = \lvert -1+h+1\rvert = \lvert h\rvert$, so

$$\frac{f(-1+h)-f(-1)}{h} = \frac{\lvert h\rvert}{h} = \begin{cases} 1, & h>0,\\ -1, & h<0.\end{cases}$$

Hence $f'_+(-1) = 1$ and $f'_-(-1) = -1$. They are unequal, so by the one-sided test $f'(-1)$ does not
exist. Geometrically the graph has a corner at $(-1,0)$: the right branch rises with slope $1$, the left
branch falls with slope $-1$.

**9.** $f'(x) = 3x^2$, so $f'(-1) = 3$ and $f(-1) = -1$. The tangent is

$$y = -1+3(x+1) = 3x+2.$$

*Check:* $x^3-(3x+2) = x^3-3x-2 = (x+1)^2(x-2)$, so $x=-1$ is a double root (tangency) and the line crosses
the cubic at $x=2$. ✓

**10.** $f'(x) = \cos x$, so

$$f'\!\left(\frac{\pi}{3}\right) = \frac12, \qquad f'\!\left(\frac{\pi}{2}\right) = 0, \qquad f'(\pi) = -1.$$

These describe the sine graph correctly: rising at $60^\circ$ with slope $\tfrac12$, flat at the crest, falling
with slope $-1$ at $x=\pi$.

**11.** $f'(x) = e^x$, so $f'(0) = e^0 = 1$ and $f'(\ln 5) = e^{\ln 5} = 5$. The point at $x=0$ is $(0,1)$ and
the tangent is

$$y = 1+x.$$

Since $(e^x)' = e^x$, the slope at a point always equals the height there: the graph of $e^x$ has the
property that the tangent at any point cuts the $x$-axis one unit to the left of the point's $x$-coordinate.

**12.** $f'(x) = \dfrac1x$ for $x > 0$ — the formula and the function share the domain $(0,\infty)$. Then
$f'(1) = 1$ and $f'(e^2) = e^{-2}$. At $x=1$ the point is $(1,0)$, so the tangent is

$$y = x-1.$$

*Check:* $e^2 \approx 7.389$, and $e^{-2} \approx 0.1353$, a small positive slope, as the slowly rising
logarithm requires.

## Intermediate

**13.** Strategy: the numerator of the difference is a difference of fractions; combine it over the common
denominator $(1+h+1)\cdot(1+1) = (2+h)\cdot2$.

$$f(1+h)-f(1) = \frac{1+h}{2+h}-\frac12 = \frac{2(1+h)-(2+h)}{2(2+h)} = \frac{2+2h-2-h}{2(2+h)} = \frac{h}{2(2+h)}.$$

Dividing by $h$:

$$\frac{f(1+h)-f(1)}{h} = \frac{1}{2(2+h)} \longrightarrow \frac14.$$

So $f'(1) = \frac14$. *Check:* the general quotient rule (next topic) gives
$\left(\frac{x}{x+1}\right)' = \frac{(x+1)-x}{(x+1)^2} = \frac{1}{(x+1)^2}$, which is $\frac14$ at $x=1$. ✓

**14.** Strategy: differentiability at a join requires two conditions — the values must agree (continuity) and
the one-sided slopes must agree.

*Continuity at $2$:* $\lim_{x\to2^-} f(x) = 4$ and $\lim_{x\to2^+} f(x) = 2m+c$, so

$$2m+c = 4.$$

*Slopes at $2$:* the left branch has derivative $2x$, so $f'_-(2) = 4$; the right branch is a line of slope
$m$, so $f'_+(2) = m$. Equality gives $m = 4$, and then $c = 4-8 = -4$.

So $f(x) = 4x-4$ for $x>2$. *Check:* $4(2)-4 = 4 = 2^2$ and the slopes both equal $4$. ✓ Continuity alone
would allow any $(m,c)$ with $c = 4-2m$; the slope condition fixes $m$, and hence $c$.

**15.** Strategy: compute the difference quotient at $0$ directly.

$$f(0) = 0, \qquad \frac{f(h)-f(0)}{h} = \frac{h^{2/3}}{h} = h^{-1/3} = \frac{1}{\sqrt[3]{h}}.$$

For $h>0$ this is positive and tends to $+\infty$; for $h<0$ it is negative and tends to $-\infty$. So both
one-sided derivatives are infinite and of opposite sign: no finite derivative exists, though the function is
continuous at $0$ because $h^{2/3}\to0$. The graph has a **cusp** at the origin: it descends vertically,
turns, and rises vertically. Since $x^{2/3} = \sqrt[3]{x^2} \ge 0$, the curve touches the $x$-axis at $0$ from
above.

**16.** Differentiate repeatedly, using the power rule at each step:

$$f'(x) = 5x^4-9x^2+2, \qquad f''(x) = 20x^3-18x, \qquad f'''(x) = 60x^2-18,$$
$$f^{(4)}(x) = 120x, \qquad f^{(5)}(x) = 120, \qquad f^{(6)}(x) = 0.$$

*Check:* the fifth derivative is constant and the sixth vanishes, as it must for a polynomial of degree $5$
(Example 7.8 in the tutorial). The coefficients follow the pattern $5\cdot4\cdot3\cdot2\cdot1 = 120$.

**17.** Differentiate:

$$v(t) = 3t^2-12t+9 = 3(t^2-4t+3) = 3(t-1)(t-3), \qquad a(t) = 6t-12.$$

At $t=2$: $v(2) = 3(1)(-1) = -3$ m/s and $a(2) = 0$ m/s². The velocity vanishes at $t=1$ and $t=3$, where
the factorisation shows the sign changes: the particle moves forward, briefly stops at $t=1$, moves backward,
stops at $t=3$ and moves forward again. At $t=2$ the acceleration is zero, so the velocity has its minimum
there — the particle is momentarily moving at constant speed.

**18.** Strategy: differentiate the height, then solve for the impact time.

$$v(t) = h'(t) = -9.8t \ \text{m/s}, \qquad v(1) = -9.8 \ \text{m/s}.$$

The negative sign means downward. Impact when $h(t) = 0$:

$$45-4.9t^2 = 0 \Longrightarrow t^2 = \frac{45}{4.9} = 9.1837\ldots \Longrightarrow t \approx 3.03\ \text{s}.$$

The speed at impact is $\lvert v(3.0305)\rvert = 9.8(3.0305) \approx 29.70$ m/s (about $107$ km/h). *Check:*
the same answer follows from $v = \sqrt{2gh} = \sqrt{2\cdot9.8\cdot45} = \sqrt{882} \approx 29.70$. ✓

**19.** Strategy: linearise $f(x) = \sqrt x$ at the nearby perfect square $100$.

$$f(100) = 10, \qquad f'(x) = \frac{1}{2\sqrt x}, \quad f'(100) = \frac{1}{20}, \qquad L(x) = 10+\frac{x-100}{20}.$$

So $\sqrt{101} \approx 10+\frac{1}{20} = 10.05$. The true value is $10.04987562\ldots$, so the error is
$+0.0001244$: the estimate is too large, because the graph of $\sqrt x$ is concave down and therefore lies
below its tangent. The relative error is about $1.2\times10^{-5}$, i.e. one part in eighty thousand.

**20.** The tangent to $\sin x$ at $0$ is $y = x$, since $\sin 0 = 0$ and $\cos 0 = 1$. Hence
$\sin(0.1)\approx 0.1$ and $\sin(0.5)\approx 0.5$.

True values: $\sin(0.1) = 0.09983342$ (error $1.67\times10^{-4}$, about $0.17\%$) and $\sin(0.5) = 0.47942554$
(error $0.0206$, about $4.3\%$). The second estimate is far worse because $0.5$ is ten times farther from the
point of tangency, and the graph bends away from the tangent. The leading error term for sine is
$-\frac{x^3}{6}$: at $x = 0.5$ this is $-0.0208$, which accounts for essentially all of the observed error.

**21.** With $V = x^3$ and $x = 5$, $dx = 0.05$:

$$dV = 3x^2\,dx = 3(25)(0.05) = 3.75\ \text{cm}^3, \qquad \frac{dV}{V} = 3\frac{dx}{x} = 3\cdot\frac{0.05}{5} = 0.03.$$

So the volume error is at most about $3.75$ cm³, i.e. $3\%$. The exact change is

$$5.05^3-125 = 128.787625-125 = 3.787625\ \text{cm}^3,$$

so the differential underestimates by about $0.038$ cm³ (roughly $1\%$ of the change). The underestimate is
expected: $V = x^3$ is convex, so its graph lies above the tangent, and the true increment exceeds the linear
one. For a *negative* error $dx = -0.05$ the same convexity reverses the direction of the error in the
magnitude: the true volume is $4.95^3 = 121.287375$ cm³, a drop of $3.712625$ cm³, while the differential
predicts a drop of $3.75$ cm³ — so there the differential *overestimates* the decrease by about $0.037$ cm³.

**22.** Marginal cost is the derivative:

$$C'(q) = 0.06q^2-q+40, \qquad C'(10) = 6-10+40 = 36\ \text{dollars per unit}.$$

The actual cost of the eleventh unit is

$$C(11)-C(10) = 506.12-470 = 36.12,$$

since $C(11) = 26.62-60.5+440+100 = 506.12$ and $C(10) = 20-50+400+100 = 470$. So $C'(10) = 36$ predicts the
increment $36.12$ to within $0.12$ — the usual first-order accuracy of a marginal quantity.

**23.** Average rate of change:

$$\frac{A(2.1)-A(2)}{0.1} = \frac{4\pi(2.1^2-2^2)}{0.1} = \frac{4\pi(0.41)}{0.1} = 16.4\pi \approx 51.52.$$

Instantaneous rate: $A'(r) = 8\pi r$, so $A'(2) = 16\pi \approx 50.27$. The average exceeds the instantaneous
value at the left endpoint because the area grows faster at larger radii; $A'$ itself is increasing. Both
numbers carry units cm² per cm, i.e. cm.

**24.** At $0$, with $f(0) = 0$ and $f(h) = h\lvert h\rvert$:

$$\frac{f(h)-f(0)}{h} = \frac{h\lvert h\rvert}{h} = \lvert h\rvert \longrightarrow 0,$$

so $f'(0) = 0$ exists. (Note $\lvert h\rvert \to 0$ from both sides, so no one-sided subtlety arises.) For
$x>0$, $f(x) = x^2$ and $f'(x) = 2x = 2\lvert x\rvert$; for $x<0$, $f(x) = -x^2$ and $f'(x) = -2x = 2\lvert
x\rvert$. Hence $f'(x) = 2\lvert x\rvert$ for all $x$, which is continuous but not differentiable at $0$ —
another instance of the corner phenomenon of Section 7.5(a).

## Advanced

**25.** Strategy: expand $\cos(x+h)$ with the addition formula, split into two quotients, and handle each limit
separately.

$$\cos(x+h)-\cos x = \cos x\cos h-\sin x\sin h-\cos x = \cos x(\cos h-1)-\sin x\sin h,$$

so

$$\frac{\cos(x+h)-\cos x}{h} = \cos x\cdot\frac{\cos h-1}{h} - \sin x\cdot\frac{\sin h}{h}.$$

*The limit $\frac{\cos h-1}{h}\to0$.* Use $1-\cos h = 2\sin^2(h/2)$, valid for all $h$:

$$\frac{\cos h-1}{h} = \frac{-2\sin^2(h/2)}{h} = -\sin\frac h2\cdot\frac{\sin(h/2)}{h/2}.$$

As $h\to0$, $\sin(h/2)\to0$ and $\frac{\sin(h/2)}{h/2}\to1$ by Lemma 7.1 applied to $u = h/2$. The product
tends to $0\cdot1 = 0$.

*Conclusion.* By Lemma 7.1, $\frac{\sin h}{h}\to1$, so

$$\frac{\cos(x+h)-\cos x}{h} \longrightarrow \cos x\cdot0 - \sin x\cdot1 = -\sin x.$$

Therefore $(\cos x)' = -\sin x$ for every $x$. *Check at $x=0$:* the formula gives slope $0$ at the maximum of
the cosine, correct. At $x=\pi/2$ it gives $-1$, and indeed the cosine is falling most steeply there. ✓

**26.** Strategy: handle $x=0$ and $x\ne0$ separately; a piecewise definition needs its own argument at the
junction.

*At $0$:*

$$\frac{g(h)-g(0)}{h} = \frac{h^3\sin(1/h)}{h} = h^2\sin\frac1h, \qquad \left\lvert h^2\sin\frac1h\right\rvert \le h^2 \longrightarrow 0,$$

so $g'(0) = 0$ exists.

*For $x\ne0$* use the product rule and chain rule (proved in the next topic; here they may be checked by the
definition):

$$g'(x) = 3x^2\sin\frac1x + x^3\cos\frac1x\cdot\left(-\frac{1}{x^2}\right) = 3x^2\sin\frac1x - x\cos\frac1x.$$

*Continuity of $g'$ at $0$:* from the displayed formula,

$$\lvert g'(x)\rvert \le 3x^2 + \lvert x\rvert \longrightarrow 0 = g'(0),$$

so $g'$ is continuous at $0$ (and elsewhere, since the formula is continuous for $x \ne 0$).

*Second derivative at $0$:*

$$g''(0) = \lim_{h\to0}\frac{g'(h)-g'(0)}{h} = \lim_{h\to0}\left(3h\sin\frac1h - \cos\frac1h\right).$$

The first term tends to $0$, but $\cos(1/h)$ oscillates between $-1$ and $1$ without limit. Hence the limit
does not exist and $g''(0)$ is undefined. Note what the example shows: $g'$ exists everywhere and is
continuous, yet $g'$ is not differentiable at $0$ — continuity of the derivative does not give a second
derivative.

**27.** Strategy: read a quantitative bound out of the definition of the limit, taking $\varepsilon = 1$.

Since $\lim_{x\to a}\frac{f(x)-f(a)}{x-a} = f'(a)$, for $\varepsilon = 1$ there is a $\delta>0$ such that

$$0 < \lvert x-a\rvert < \delta \Longrightarrow \left\lvert\frac{f(x)-f(a)}{x-a}-f'(a)\right\rvert < 1.$$

By the triangle inequality, $\left\lvert\frac{f(x)-f(a)}{x-a}\right\rvert < \lvert f'(a)\rvert+1$. Put
$M = \lvert f'(a)\rvert+1 > 0$. Then for $0<\lvert x-a\rvert<\delta$,

$$\lvert f(x)-f(a)\rvert = \left\lvert\frac{f(x)-f(a)}{x-a}\right\rvert\lvert x-a\rvert \le M\lvert x-a\rvert,$$

and at $x=a$ both sides are $0$. So the bound holds on the whole interval $(a-\delta, a+\delta)$. $\blacksquare$

*Remark.* The converse is false: $f(x) = \lvert x\rvert$ satisfies such a bound at $a=0$ with $M=1$ but is not
differentiable there. So a local Lipschitz bound is necessary, not sufficient.

**28.** Strategy: avoid the chain rule (not yet available) by substituting $h = -k$ in the difference
quotient.

Suppose $f$ is even, $f(-x) = f(x)$. Then for any $a$,

$$f'(-a) = \lim_{h\to0}\frac{f(-a+h)-f(-a)}{h}.$$

Put $h = -k$, so $k\to0$ as $h\to0$ and $-a+h = -(a+k)$:

$$f'(-a) = \lim_{k\to0}\frac{f(-(a+k))-f(-a)}{-k} = \lim_{k\to0}\frac{f(a+k)-f(a)}{-k} = -\lim_{k\to0}\frac{f(a+k)-f(a)}{k} = -f'(a).$$

This holds for every $a$, so $f'(-a) = -f'(a)$: $f'$ is **odd**. $\blacksquare$

For an **odd** $f$, with $f(-x) = -f(x)$, the same substitution gives

$$f'(-a) = \lim_{k\to0}\frac{f(-(a+k))-f(-a)}{-k} = \lim_{k\to0}\frac{-f(a+k)+f(a)}{-k} = \lim_{k\to0}\frac{f(a+k)-f(a)}{k} = f'(a),$$

so $f'$ is **even**. $\blacksquare$ *Example:* $f(x) = x^2$ even gives $f'(x) = 2x$ odd; $f(x) = x^3$ odd
gives $f'(x) = 3x^2$ even.

**29.** Strategy: a tangent line is determined by its point of tangency $t$; impose the condition that the
line passes through $(1,-3)$ and solve for $t$.

The tangent at $x=t$ has slope $2t$ and equation

$$y = t^2+2t(x-t) = 2tx-t^2.$$

Passing through $(1,-3)$ means

$$2t-t^2 = -3 \Longleftrightarrow t^2-2t-3 = 0 \Longleftrightarrow (t-3)(t+1) = 0,$$

so $t = 3$ or $t = -1$. The two tangents are

$$y = 6x-9 \quad (t=3), \qquad y = -2x-1 \quad (t=-1).$$

*Check both.* At $x=1$: $6-9 = -3$ ✓ and $-2-1 = -3$ ✓. Tangency: $x^2-(6x-9) = (x-3)^2$ and
$x^2-(-2x-1) = (x+1)^2$, both perfect squares. ✓ The point $(1,-3)$ lies below the parabola (since
$1^2 = 1 > -3$), which is why two tangents pass through it.

**30.** Strategy: the sign of the difference quotient is what controls $f(x)-f(a)$; choose $\varepsilon$ small
enough to keep the quotient positive.

Let $\varepsilon = \frac{f'(a)}{2} > 0$. By the definition of the limit there is $\delta>0$ such that

$$0<\lvert x-a\rvert<\delta \Longrightarrow \left\lvert\frac{f(x)-f(a)}{x-a}-f'(a)\right\rvert < \frac{f'(a)}{2},$$

so in particular $\frac{f(x)-f(a)}{x-a} > \frac{f'(a)}{2} > 0$ on that punctured interval.

*If $a<x<a+\delta$* then $x-a>0$, so $f(x)-f(a) = (x-a)\cdot\frac{f(x)-f(a)}{x-a} > 0$.

*If $a-\delta<x<a$* then $x-a<0$, so the same product is negative: $f(x)-f(a) < 0$. $\blacksquare$

*Why this is not monotonicity.* Monotonicity on $(a-\delta,a+\delta)$ would compare $f(x)$ and $f(y)$ for two
points *both different from $a$*, and the argument above says nothing about such pairs. Indeed the function
$x+2x^2\sin(1/x)$ (Section 11 of the tutorial) has $f'(0)=1>0$ and is not increasing on any interval around
$0$: the derivative oscillates and takes negative values arbitrarily close to $0$.

**31.** Strategy: remove the absolute values on each interval; continuity is inherited from the summands.

*Continuity.* Both $\lvert x\rvert$ and $\lvert x-1\rvert$ are continuous everywhere, so their sum is.

*Piecewise formula.*

$$\lvert x\rvert = \begin{cases}-x,&x<0\\ x,&x\ge0\end{cases}, \qquad \lvert x-1\rvert = \begin{cases}-(x-1),&x<1\\ x-1,&x\ge1\end{cases}.$$

Hence

$$f(x) = \begin{cases} 1-2x, & x<0,\\ 1, & 0<x<1,\\ 2x-1, & x>1.\end{cases}$$

*Derivatives on the open intervals:* $-2$, $0$, $2$.

*At $x=0$:* $f'_-(0) = -2$ and $f'_+(0) = 0$; unequal, so not differentiable.
*At $x=1$:* $f'_-(1) = 0$ and $f'_+(1) = 2$; unequal, so not differentiable.

So $f$ is continuous everywhere and differentiable exactly on $\mathbb{R}\setminus\{0,1\}$. *Check:* the graph
is a flat plateau of height $1$ between $0$ and $1$, with two rising/falling rays outside; corners at both
ends of the plateau. The minimum value is $1$.

## Challenge

**32.** Strategy: at $0$ the factor $x^2$ beats the oscillation; away from $0$ differentiate mechanically. To
show unboundedness, evaluate $f'$ at a sequence where $\cos(1/x^2) = 1$.

*At $0$:*

$$\frac{f(h)-f(0)}{h} = \frac{h^2\sin(1/h^2)}{h} = h\sin\frac{1}{h^2}, \qquad \left\lvert h\sin\frac{1}{h^2}\right\rvert \le \lvert h\rvert \longrightarrow 0,$$

so $f'(0) = 0$.

*For $x\ne0$:*

$$f'(x) = 2x\sin\frac{1}{x^2} + x^2\cos\frac{1}{x^2}\cdot\left(-\frac{2}{x^3}\right) = 2x\sin\frac{1}{x^2} - \frac{2}{x}\cos\frac{1}{x^2}.$$

So $f$ is differentiable at every point.

*Unboundedness.* Let $x_n = 1/\sqrt{2\pi n}$, so that $1/x_n^2 = 2\pi n$ and $\cos(1/x_n^2) = 1$. Then

$$f'(x_n) = 2x_n\sin(2\pi n) - \frac{2}{x_n} = 0 - 2\sqrt{2\pi n} \longrightarrow -\infty.$$

Given any $\delta>0$, all sufficiently large $n$ have $x_n<\delta$, so $\lvert f'\rvert$ exceeds any bound on
$(-\delta,\delta)$. Hence $f'$ is unbounded on every interval containing $0$. $\blacksquare$

*Remark.* Compare Exercise 26: there $g'$ was continuous. Here $f'$ exists everywhere but is not merely
discontinuous — it is unbounded near $0$.

**33.** Strategy: bound $W$ to handle $0$; use the differentiability of $x^2$ and $1/x^2$ away from $0$ to
transfer non-differentiability from $W$ to $F$.

*Boundedness of $W$.* Since $\lvert\cos\rvert\le1$ and $0<a<1$,

$$\lvert W(x)\rvert \le \sum_{n=0}^{\infty}a^n = \frac{1}{1-a} =: B \quad\text{for all } x.$$

*Continuity of $F$.* At $x\ne0$ it is the product of the continuous functions $x^2$ and $W$. At $0$,
$\lvert F(x)\rvert = x^2\lvert W(x)\rvert \le Bx^2\to0 = F(0)$, so $F$ is continuous at $0$ as well.

*Differentiability at $0$.*

$$\frac{F(h)-F(0)}{h} = \frac{h^2W(h)}{h} = hW(h), \qquad \lvert hW(h)\rvert \le B\lvert h\rvert \longrightarrow 0,$$

so $F'(0) = 0$.

*No other point.* Suppose $a\ne0$ and $F'(a)$ exists. On a neighbourhood of $a$ the function $1/x^2$ is
defined and differentiable (its derivative $-2/x^3$ exists for $x\ne0$). Then

$$W(x) = F(x)\cdot\frac{1}{x^2}$$

would be a product of functions differentiable at $a$, hence differentiable at $a$ — contradicting the
theorem that $W$ is differentiable nowhere. Therefore $F$ is differentiable only at $0$. $\blacksquare$

*Remark.* This is a standard way to manufacture a function that is continuous everywhere and differentiable
at exactly one point.

**34.** Strategy: at a zero of $f$, the quotient of $\lvert f\rvert$ is the quotient of $f$ with a sign that
depends on the side; compare the two one-sided limits.

Suppose first that $f(a) = 0$, so $\lvert f\rvert(a) = 0$ and

$$Q(h) := \frac{\lvert f(a+h)\rvert-\lvert f(a)\rvert}{h} = \frac{\lvert f(a+h)\rvert}{h}.$$

Write $L = f'(a)$.

*If $L>0$:* taking $\varepsilon = L/2$ in the definition of $f'(a)$ gives a $\delta>0$ with

$$\frac{f(a+h)}{h} > \frac{L}{2} > 0 \quad\text{for } 0<\lvert h\rvert<\delta.$$

This forces $f(a+h)$ and $h$ to have the same sign. Hence for $0<h<\delta$,
$Q(h) = \frac{f(a+h)}{h}\to L$; for $-\delta<h<0$, $f(a+h)<0$ so $\lvert f(a+h)\rvert = -f(a+h)$ and
$Q(h) = -\frac{f(a+h)}{h}\to -L$. The one-sided limits are $-L$ and $L$, equal only if $L = 0$ — impossible
here. So $\lvert f\rvert$ is not differentiable at $a$.

*If $L<0$:* the same computation with the signs reversed gives one-sided limits $-L$ and $L$ again, which
differ. So again not differentiable.

*If $L = 0$:* $\left\lvert Q(h)\right\rvert = \left\lvert\frac{f(a+h)}{h}\right\rvert \to 0$, so
$Q(h)\to0$ and $(\lvert f\rvert)'(a) = 0$.

Therefore, when $f(a)=0$ and $f'(a)$ exists, $\lvert f\rvert$ is differentiable at $a$ **iff** $f'(a)=0$, and
the derivative is then $0$. $\blacksquare$

*If $f(a)\ne0$:* let $c = f(a)$. By continuity of $f$ at $a$ there is $\delta>0$ with
$\lvert f(x)-c\rvert < \lvert c\rvert/2$, hence $f(x)$ has the sign of $c$ on $(a-\delta,a+\delta)$ and never
vanishes there. On that interval either $\lvert f\rvert = f$ (if $c>0$) or $\lvert f\rvert = -f$ (if $c<0$),
so $\lvert f\rvert$ is differentiable at $a$ with derivative $f'(a)$ or $-f'(a)$ respectively. $\blacksquare$

**35.** Strategy: the tangent line at a guess is the linear model of $f$; its zero is the next guess.

At $x_n$ the tangent is $y = f(x_n)+f'(x_n)(x-x_n)$. Setting $y = 0$ and solving (legitimately, since
$f'(x_n)\ne0$ for the method to make sense):

$$0 = f(x_n)+f'(x_n)(x-x_n) \Longrightarrow x-x_n = -\frac{f(x_n)}{f'(x_n)} \Longrightarrow x_{n+1} = x_n-\frac{f(x_n)}{f'(x_n)}.$$

For $f(x) = x^2-2$, $f'(x) = 2x$, so

$$x_{n+1} = x_n - \frac{x_n^2-2}{2x_n} = \frac{2x_n^2-x_n^2+2}{2x_n} = \frac{x_n^2+2}{2x_n}.$$

Starting from $x_0 = 1$:

$$x_1 = \frac{1+2}{2} = \frac32 = 1.5, \qquad x_2 = \frac{\frac94+2}{3} = \frac{17}{12} \approx 1.4166667,$$

$$x_3 = \frac{\left(\frac{17}{12}\right)^2+2}{2\cdot\frac{17}{12}} = \frac{\frac{289}{144}+2}{\frac{17}{6}} = \frac{577}{144}\cdot\frac{6}{17} = \frac{577}{408} \approx 1.4142156863.$$

Compare $\sqrt2 = 1.4142135624$. The error is $\lvert x_3-\sqrt2\rvert \approx 2.1\times10^{-6}$, so $x_3$ is
correct to five decimal places. The errors roughly square at each step ($1.7\times10^{-1}$, then
$2.5\times10^{-3}$, then $2.1\times10^{-6}$), which is the quadratic convergence of Newton's method.

**36.** Strategy: split the symmetric quotient into two ordinary difference quotients.

$$\frac{f(a+h)-f(a-h)}{2h} = \frac12\left(\frac{f(a+h)-f(a)}{h} + \frac{f(a-h)-f(a)}{-h}\right).$$

As $h\to0$, the first bracket tends to $f'(a)$. In the second bracket, put $k = -h$; then $k\to0$ and the
bracket equals $\frac{f(a+k)-f(a)}{k}\to f'(a)$. Hence the whole expression tends to
$\frac12\left(f'(a)+f'(a)\right) = f'(a)$. $\blacksquare$

*The converse fails.* For $f(x) = \lvert x\rvert$ and $a = 0$,

$$\frac{f(h)-f(-h)}{2h} = \frac{\lvert h\rvert-\lvert -h\rvert}{2h} = \frac{0}{2h} = 0 \quad (h\ne0),$$

so the symmetric quotient has limit $0$ — although $f'(0)$ does not exist, since the one-sided derivatives are
$1$ and $-1$.

*Warning.* A numerical central difference can therefore return a plausible slope at a corner. The symmetric
quotient tests "is the function approximately odd about $a$", not "is the function differentiable at $a$". Any
numerical differentiation should be checked against a one-sided difference or against knowledge of the
function's structure.
