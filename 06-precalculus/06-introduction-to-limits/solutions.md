# Introduction to Limits — Solutions

> [Tutorial](README.md) · [Exercises](exercises.md) · 36 worked solutions

Each solution states the strategy, carries out every step, and ends with an answer and a check. For the
$\varepsilon$-$\delta$ problems the *scratch work* (how $\delta$ is found) is separated from the
*proof* (how $\delta$ is used), because that separation is the skill being tested. Claims that a limit
does not exist always name the mechanism.

## Beginner

**1.**

**Strategy.** Average rate of change is $\dfrac{f(b)-f(a)}{b-a}$.

$$f(1) = 1+1 = 2, \qquad f(3) = 9+1 = 10, \qquad \frac{10-2}{3-1} = \frac{8}{2} = 4.$$

**Answer.** $4$ units of output per unit of input.

**Check.** $f(x)$ increases by $4$ per unit on average; since $f'(x)=2x$ runs from $2$ to $6$ across the interval, an average of $4$ (the value at the midpoint $x=2$) is exactly right for a parabola — symmetry in action ✓.

**2.**

**Strategy.** Same formula, with units tracked.

$$s(1) = 5(1)^{2} = 5, \qquad s(3) = 5(9) = 45, \qquad \frac{45-5}{3-1} = \frac{40}{2} = 20.$$

**Answer.** $20\ \mathrm{m\,s^{-1}}$.

**Check.** The velocity at $t=1$ is $10$ m/s and at $t=3$ it is $30$ m/s (since $v = 10t$); the average of a linear velocity over the interval is its midpoint value, $20$ ✓.

**3.**

**Strategy.** Two graph points: $(2,f(2))$ and $(5,f(5))$.

$$f(2) = 4-6 = -2, \qquad f(5) = 25-15 = 10, \qquad m = \frac{10-(-2)}{5-2} = \frac{12}{3} = 4.$$

**Answer.** Slope $4$.

**Check.** The secant line is $y = 4(x-2)-2 = 4x-10$; at $x=5$ it gives $10$ ✓, and $f(x)-(4x-10) = x^{2}-7x+10 = (x-2)(x-5)$ vanishes exactly at the two points ✓.

**4.**

**Strategy.** Substitute, conjecture, then factor — in that order, because the table tells you what to prove.

| $x$ | $2.9$ | $2.99$ | $3.01$ | $3.1$ |
|---|---|---|---|---|
| $\dfrac{x^{2}-9}{x-3}$ | $5.9$ | $5.99$ | $6.01$ | $6.1$ |

Conjecture: the limit is $6$.

**Proof.** For $x\ne3$,

$$\frac{x^{2}-9}{x-3} = \frac{(x-3)(x+3)}{x-3} = x+3.$$

The cancellation is valid because $x\ne3$, which is exactly the condition $0<|x-3|$ in the definition of
the limit. Then

$$\lim_{x\to3}\frac{x^{2}-9}{x-3} = \lim_{x\to3}(x+3) = 6,$$

by direct substitution (Property 8.6), since $x+3$ is a polynomial.

**Answer.** $6$.

**Check.** The table's values straddle $6$ symmetrically ($5.99$ and $6.01$) ✓. Note that the *table*
only suggested the answer; the factorisation is what establishes it — and the factorisation explains why
the values approach from below on one side and above on the other, which the table alone cannot explain.

**5.**

**Strategy.** $3x^{2}-2x+4$ is a polynomial, so substitute.

$$3(1)^{2}-2(1)+4 = 3-2+4 = 5.$$

**Answer.** $5$.

**Check.** Evaluate at $x=1.001$: $3(1.002001)-2.002+4 = 3.006003-2.002+4 = 5.005...$ hmm, recompute: $3(1.002001) = 3.006003$; minus $2.002$ gives $1.004003$; plus $4$ gives $5.004003$. The value is $5 + 4(0.001)$ approximately, since the derivative at $1$ is $6(1)-2 = 4$ — consistent with a limit of $5$ ✓.

**6.**

**Strategy.** Polynomial: substitute.

$$(-2)^{3}+4(-2) = -8-8 = -16.$$

**Answer.** $-16$.

**Check.** At $x=-2.01$: $-8.120601 - 8.04 = -16.160601$, close to $-16$ with a change of about $0.16$ for a change of $0.01$ in $x$ — slope $16$ at that point, as expected from $3x^{2}+4 = 16$ ✓.

**7.**

**Strategy.** Substitution gives $0/0$. Factor the numerator.

$$\frac{x^{2}+2x}{x} = \frac{x(x+2)}{x} = x+2 \quad (x\ne0), \qquad \lim_{x\to0}(x+2) = 2.$$

**Answer.** $2$.

**Check.** At $x=0.001$: $\frac{0.000001+0.002}{0.001} = \frac{0.002001}{0.001} = 2.001$ ✓.

**8.**

**Strategy.** Each piece governs one side; substitute into the relevant formula.

Left ($x<2$): $\displaystyle\lim_{x\to2^{-}}(2x+1) = 5$.

Right ($x\ge2$): $\displaystyle\lim_{x\to2^{+}}(x^{2}-1) = 4-1 = 3$.

Since $5\ne3$, the one-sided limits disagree, so by Property 8.7 the two-sided limit does not exist.

**Answer.** Left limit $5$; right limit $3$; the two-sided limit DNE (a jump of $2$).

**Check.** $f(1.999) = 4.998$ and $f(2.001) = 4.004001-1 = 3.004001$ — the values do not meet ✓. Note that $f(2) = 3$ coincides with the right limit but cannot repair the disagreement.

**9.**

**Strategy.** $0/0$; difference of squares.

$$\frac{x^{2}-16}{x-4} = \frac{(x-4)(x+4)}{x-4} = x+4 \quad (x\ne4), \qquad \lim_{x\to4}(x+4) = 8.$$

**Answer.** $8$.

**Check.** At $x=4.01$: $(16.0801-16)/0.01 = 8.01$ ✓.

**10.**

**Strategy.** Expand and cancel; this is a difference quotient with $f(x)=x^{2}$ at $a=3$.

$$\frac{(3+h)^{2}-9}{h} = \frac{9+6h+h^{2}-9}{h} = \frac{h(6+h)}{h} = 6+h \quad (h\ne0).$$

As $h\to0$, $6+h\to6$.

**Answer.** $6$ — which is $f'(3) = 2(3)$ for $f(x)=x^{2}$ ✓.

**Check.** $h=0.01$: $6.01$; $h=0.001$: $6.001$ ✓.

**11.**

**Strategy.** $0/0$; difference of squares with $a=-1$.

$$\frac{x^{2}-1}{x+1} = \frac{(x-1)(x+1)}{x+1} = x-1 \quad (x\ne-1), \qquad \lim_{x\to-1}(x-1) = -2.$$

**Answer.** $-2$.

**Check.** At $x=-0.99$: $(-0.99-1) = -1.99$ ✓.

**12.**

**Strategy.** Compute each separately; the first is a limit of values, the second of one-sided quotients.

$\lim_{x\to0}|x| = 0$: given $\varepsilon>0$, take $\delta = \varepsilon$; then $0<|x|<\delta$ gives $||x|-0| = |x| < \varepsilon$.

For $\dfrac{|x|}{x}$: for $x>0$ the quotient is $x/x = 1$; for $x<0$ it is $(-x)/x = -1$. So

$$\lim_{x\to0^{+}}\frac{|x|}{x} = 1, \qquad \lim_{x\to0^{-}}\frac{|x|}{x} = -1.$$

The one-sided limits differ, so the two-sided limit does not exist.

**Answer.** $|x|\to0$; $|x|/x$ has no limit at $0$ (a jump).

**Check.** Values at $x=\pm0.001$: $|x| = 0.001$ and $|x|/x = \pm1$ ✓. The first function is continuous at $0$ (indeed $|0| = 0$); the second is undefined at $0$ and jumps.

**13.**

**Strategy.** Separate the three questions: the limit, the value, continuity.

$$\lim_{x\to3}\frac{x^{2}-9}{x-3} = \lim_{x\to3}(x+3) = 6.$$

But $f(3)$ is undefined, since substitution gives $0/0$. Since continuity at $3$ requires
$\lim_{x\to3}f(x) = f(3)$, and $f(3)$ does not exist, $f$ is not continuous at $3$.

**Answer.** Limit $6$; $f(3)$ undefined; not continuous; a **removable** discontinuity (a hole at
$(3,6)$).

**Check.** The graph is the line $y = x+3$ with the single point $(3,6)$ removed ✓. Defining $f(3)=6$
would make $f$ continuous there — the definition of "removable": the discontinuity can be removed by
supplying one value.

## Intermediate

**14.**

**Strategy.** Substitution gives $0/0$, and both numerator and denominator factor.

$$x^{2}-5x+6 = (x-2)(x-3), \qquad x^{2}-4 = (x-2)(x+2).$$

$$\frac{(x-2)(x-3)}{(x-2)(x+2)} = \frac{x-3}{x+2} \quad (x\ne2).$$

Now the denominator at $x=2$ is $4\ne0$, so the quotient law applies:

$$\lim_{x\to2}\frac{x-3}{x+2} = \frac{2-3}{2+2} = -\frac14.$$

**Answer.** $-\dfrac14$.

**Check.** At $x=2.01$: numerator $-0.99$, denominator $4.01$, ratio $-0.2469$ ✓. Also the sign is right: near $x=2$ the numerator is negative and the denominator positive.

**15.**

**Strategy.** $0/0$ with a square root: multiply by the conjugate.

$$\frac{\sqrt{4+x}-2}{x}\cdot\frac{\sqrt{4+x}+2}{\sqrt{4+x}+2} = \frac{(4+x)-4}{x\left(\sqrt{4+x}+2\right)} = \frac{x}{x\left(\sqrt{4+x}+2\right)} = \frac{1}{\sqrt{4+x}+2}.$$

The last equality holds for $x\ne0$. Now substitute:

$$\lim_{x\to0}\frac{1}{\sqrt{4+x}+2} = \frac{1}{2+2} = \frac14.$$

**Answer.** $\dfrac14$ — which is $\dfrac{d}{dx}\sqrt{x}$ evaluated at $x=4$ ✓.

**Check.** $x=0.01$: $(\sqrt{4.01}-2)/0.01 = (2.0024984-2)/0.01 = 0.24984$ ✓.

**16.**

**Strategy.** Same conjugate trick, but the denominator is $x-3$, so use the conjugate of $\sqrt{x+1}-2$.

$$\frac{\sqrt{x+1}-2}{x-3}\cdot\frac{\sqrt{x+1}+2}{\sqrt{x+1}+2} = \frac{(x+1)-4}{(x-3)\left(\sqrt{x+1}+2\right)} = \frac{x-3}{(x-3)\left(\sqrt{x+1}+2\right)} = \frac{1}{\sqrt{x+1}+2}.$$

Then

$$\lim_{x\to3}\frac{1}{\sqrt{x+1}+2} = \frac{1}{2+2} = \frac14.$$

**Answer.** $\dfrac14$ — the derivative of $\sqrt{x+1}$ at $x=3$, i.e. $\frac{1}{2\sqrt4}$ ✓.

**Check.** $x=3.01$: $\sqrt{4.01} = 2.0024984$, difference $0.0024984$, divided by $0.01$ gives $0.24984$ ✓.

**17.**

**Strategy.** Expand the cube using $(a+h)^{3} = a^{3}+3a^{2}h+3ah^{2}+h^{3}$ with $a=2$.

$$(2+h)^{3} = 8+12h+6h^{2}+h^{3},$$

$$\frac{(2+h)^{3}-8}{h} = \frac{12h+6h^{2}+h^{3}}{h} = 12+6h+h^{2} \quad (h\ne0).$$

As $h\to0$, $12+6h+h^{2}\to12$.

**Answer.** $12$ — the value of $3a^{2} = 3(4)$ for the derivative of $x^{3}$ at $a=2$ ✓.

**Check.** $h=0.01$: $12+0.06+0.0001 = 12.0601$ ✓.

**18.**

**Strategy.** Two standard factorisations, then cancel $x-1$.

$$x^{3}-1 = (x-1)(x^{2}+x+1), \qquad x^{2}-1 = (x-1)(x+1).$$

$$\frac{x^{3}-1}{x^{2}-1} = \frac{x^{2}+x+1}{x+1} \quad (x\ne1).$$

Then

$$\lim_{x\to1}\frac{x^{2}+x+1}{x+1} = \frac{3}{2}.$$

**Answer.** $\dfrac32$.

**Check.** At $x=1.001$: numerator $3.003001$, denominator $2.001$, ratio $1.50075$ ✓.

**Remark.** After the cancellation, substitution is legitimate because the new denominator
$x+1$ equals $2\ne0$ at $x=1$; that is exactly the hypothesis of Property 8.6. (The ratio of the
derivatives at $x=1$, $\frac{3x^{2}}{2x} = \frac32$, agrees — that is L'Hôpital's rule, a theorem of
calculus, and here it is at best a check on the answer, never a derivation.)

**19.**

**Strategy.** Write the difference quotient, combine the fractions, cancel $h$.

$$f(2+h)-f(2) = \frac{1}{2+h}-\frac12 = \frac{2-(2+h)}{2(2+h)} = \frac{-h}{2(2+h)}.$$

Divide by $h$:

$$\frac{1}{h}\cdot\frac{-h}{2(2+h)} = \frac{-1}{2(2+h)} \quad (h\ne0).$$

As $h\to0$, this tends to $\dfrac{-1}{2(2+0)} = -\dfrac14$.

**Answer.** $f'(2) = -\dfrac14$.

**Check.** $h=0.01$: $-1/(2(2.01)) = -0.24876$ ✓. And the formula gives $f'(a) = -1/a^{2}$, so $f'(2) = -1/4$ ✓.

**20.**

**Strategy.** Difference quotient at $a=9$, then rationalise.

$$\frac{\sqrt{9+h}-3}{h}\cdot\frac{\sqrt{9+h}+3}{\sqrt{9+h}+3} = \frac{(9+h)-9}{h\left(\sqrt{9+h}+3\right)} = \frac{1}{\sqrt{9+h}+3}.$$

As $h\to0$: $\dfrac{1}{3+3} = \dfrac16$.

**Answer.** Slope $\dfrac16$.

**Check.** The derivative of $\sqrt x$ is $\frac{1}{2\sqrt x}$, which at $9$ is $\frac16$ ✓.

**21.**

**Strategy.** Compute both one-sided limits in terms of $a$, then impose equality.

Left: $\displaystyle\lim_{x\to1^{-}}(ax+1) = a+1$. Right: $\displaystyle\lim_{x\to1^{+}}(x^{2}+2) = 3$.

The two-sided limit exists exactly when $a+1 = 3$, i.e. $a = 2$, and then the common limit is $3$.

**Answer.** $a = 2$; the limit is $3$.

**Check.** With $a=2$: left limit $2(1)+1 = 3$, right limit $3$ ✓. With $a=1$ the left limit is $2$ and the function would jump by $1$.

**22.**

**Strategy.** Compute the limit at the bad point and compare with the value.

(a) $\dfrac{x^{2}-4}{x-2} = x+2\to4$ as $x\to2$. The limit exists; $f(2)$ is undefined. **Removable.**

(b) $1/(x-3)$: as $x\to3^{+}$ the values tend to $+\infty$, as $x\to3^{-}$ to $-\infty$. No finite limit; the graph has a vertical asymptote. **Infinite (essential).**

(c) $\dfrac{|x-1|}{x-1}$ equals $1$ for $x>1$ and $-1$ for $x<1$. Both one-sided limits exist and differ. **Jump.**

**Answer.** (a) removable, (b) infinite, (c) jump.

**Check.** For (a), supplying $f(2)=4$ would make the function continuous; for (b) no single value could help, since the values are unbounded; for (c) no single value can equal both $-1$ and $1$ ✓.

**23.**

**Strategy.** Combine the numerator into a single fraction first — do not split the limit.

$$\frac{1}{x+2}-\frac12 = \frac{2-(x+2)}{2(x+2)} = \frac{-x}{2(x+2)}.$$

Divide by $x$:

$$\frac{1}{x}\cdot\frac{-x}{2(x+2)} = \frac{-1}{2(x+2)} \quad (x\ne0).$$

As $x\to0$: $\dfrac{-1}{2(2)} = -\dfrac14$.

**Answer.** $-\dfrac14$.

**Check.** $x=0.01$: $\left(\frac{1}{2.01}-\frac12\right)/0.01 = (0.4975124-0.5)/0.01 = -0.24876$ ✓.

**Remark.** This is the derivative of $g(x) = \dfrac{1}{x+2}$ at $x=0$, which is $-\dfrac{1}{(x+2)^{2}} = -\dfrac14$ ✓.

**24.**

**Strategy.** Find the domain first; continuity then holds everywhere on the domain except at points where the denominator vanishes.

The square root requires $x-3\ge0$, so $x\ge3$. The denominator requires $x\ne5$. So the domain is $[3,5)\cup(5,\infty)$.

On that domain the function is a quotient of continuous functions with a nonzero denominator, so it is continuous at every point of $(3,5)$ and $(5,\infty)$. At the endpoint $x=3$ it is right-continuous, since $\lim_{x\to3^{+}}f(x) = \frac{0}{-2} = 0 = f(3)$.

**Answer.** Continuous on $[3,5)$ and on $(5,\infty)$; the largest intervals are these two. There is a vertical asymptote at $x=5$ (infinite discontinuity).

**Check.** $f(4) = 1/(-1) = -1$ and $f(6) = \sqrt3/1 = 1.732$; approaching $5$ from the left, $f\to-\infty$; from the right, $f\to+\infty$ ✓.

## Advanced

**25.**

**Strategy.** Compute $f(2+h)$, subtract $f(2)$, divide by $h$, and only then let $h\to0$.

$$f(2) = 4-6 = -2,$$
$$f(2+h) = (2+h)^{2}-3(2+h) = 4+4h+h^{2}-6-3h = h^{2}+h-2.$$

Difference: $(h^{2}+h-2)-(-2) = h^{2}+h$. Quotient:

$$\frac{h^{2}+h}{h} = h+1 \quad (h\ne0).$$

$$\lim_{h\to0}(h+1) = 1.$$

**Answer.** Slope $1$, so the tangent at $(2,-2)$ is $y+2 = 1(x-2)$, i.e. $y = x-4$.

**Check.** The derivative is $f'(x) = 2x-3$, and $f'(2) = 1$ ✓. The tangent $y=x-4$ meets the parabola where $x^{2}-3x = x-4$, i.e. $x^{2}-4x+4 = (x-2)^{2} = 0$ — a double root, so the line touches exactly at $x=2$ ✓.

**26.**

**Strategy.** Difference quotient at $a=4$, rationalised (as in Exercise 15 with $4$ replaced by $4$... here the point is $4$, so the conjugate is $\sqrt{4+h}+2$).

$$\frac{\sqrt{4+h}-2}{h} = \frac{1}{\sqrt{4+h}+2} \longrightarrow \frac{1}{4}.$$

**Answer.** Slope $\dfrac14$; the point is $(4,2)$, so the tangent is $y-2 = \tfrac14(x-4)$, i.e. $y = \tfrac{x}{4}+1$.

**Check.** The derivative of $\sqrt x$ is $\frac{1}{2\sqrt x}$, which at $x=4$ is $\frac{1}{4}$ ✓. The tangent at $x=9$ has slope $\frac16 < \frac14$ — the curve is flattening, as it must ✓.

**27.**

**Strategy.** *Scratch work:* $|(4x-3)-1| = |4x-4| = 4|x-1|$, so $4|x-1|<\varepsilon$ if $|x-1|<\varepsilon/4$.

*Proof.* Let $\varepsilon>0$ and take $\delta = \varepsilon/4$. If $0<|x-1|<\delta$ then

$$|(4x-3)-1| = |4x-4| = 4|x-1| < 4\delta = \varepsilon. \qquad \blacksquare$$

**Answer.** $\delta = \varepsilon/4$ works.

**Check.** For $\varepsilon = 0.08$, $\delta = 0.02$: any $x\in(0.98,1.02)$, $x\ne1$, gives $4x-3\in(0.92,1.08)$, within $0.08$ of $1$ ✓.

**28.**

**Strategy.** *Scratch work:* $|(3x+5)-(-1)| = |3x+6| = 3|x+2|$.

*Proof.* Let $\varepsilon>0$ and set $\delta = \varepsilon/3$. If $0<|x+2|<\delta$ then

$$|(3x+5)+1| = 3|x+2| < 3\delta = \varepsilon. \qquad \blacksquare$$

**Answer.** $\delta = \varepsilon/3$.

**Check.** $\varepsilon = 0.03$, $\delta = 0.01$: $x\in(-2.01,-1.99)$ gives $3x+5\in(-1.03,0.97)$, within $0.03$ of $-1$ ✓.

**29.**

**Strategy.** *Scratch work:* $|x^{2}-9| = |x-3||x+3|$. Control the second factor by requiring $|x-3|<1$, which gives $2<x<4$ and hence $|x+3|<7$. Then $|x^{2}-9|<7|x-3|$, so $|x-3|<\varepsilon/7$ suffices.

*Proof.* Let $\varepsilon>0$ and set $\delta = \min\left(1,\dfrac{\varepsilon}{7}\right)$. Suppose $0<|x-3|<\delta$. Then $|x-3|<1$, so $2<x<4$ and therefore

$$|x+3| = x+3 < 7.$$

Hence

$$|x^{2}-9| = |x-3|\cdot|x+3| < \delta\cdot 7 \le \frac{\varepsilon}{7}\cdot7 = \varepsilon. \qquad \blacksquare$$

**Answer.** $\delta = \min(1,\varepsilon/7)$.

**Check.** $\varepsilon = 0.14$ gives $\delta = 0.02$; at $x = 3.02$, $x^{2} = 9.1204$, and $|9.1204-9| = 0.1204<0.14$ ✓.

**Why $\min(1,\cdot)$ is needed.** With $\delta = \varepsilon/7$ alone and $\varepsilon = 70$, we would get $\delta = 10$, permitting $x = 13$ where $x^{2}-9 = 160 \not< 70$. The restriction $|x-3|<1$ makes the bound $|x+3|<7$ valid; the outer $\min$ enforces it.

**30.**

**Strategy.** Exhibit two sequences $x_n\to0$, $y_n\to0$ along which $\cos(1/x)$ has different limits. If a limit existed, all sequences would have to give the same value.

Take $x_n = \dfrac{1}{2n\pi}$ and $y_n = \dfrac{1}{(2n+1)\pi}$, for $n\ge1$. Both are positive and tend to $0$, since the denominators tend to $+\infty$.

Then
$$\cos\frac{1}{x_n} = \cos(2n\pi) = 1, \qquad \cos\frac{1}{y_n} = \cos\bigl((2n+1)\pi\bigr) = -1.$$

Suppose $\lim_{x\to0}\cos(1/x) = L$. Take $\varepsilon = \tfrac12$. There would be $\delta>0$ such that $0<|x|<\delta$ implies $|\cos(1/x)-L|<\tfrac12$. But for all large $n$, both $x_n$ and $y_n$ lie in $(0,\delta)$, so $|1-L|<\tfrac12$ and $|-1-L|<\tfrac12$. Then

$$2 = |1-(-1)| \le |1-L| + |L-(-1)| < \tfrac12+\tfrac12 = 1,$$

a contradiction. Hence no such $L$ exists. $\blacksquare$

**Answer.** The limit does not exist (oscillation).

**Check.** Numerically, $\cos(1/x)$ at $x = 1/(2\pi) \approx 0.159$ is $1$, and at $x = 1/\pi\approx0.318$ is $-1$; between those two points it completes a full period. As $x\to0$ the oscillations become infinitely dense, and no value is approached ✓.

**31.**

**Strategy.** Choose $\varepsilon$ small enough that the whole $\varepsilon$-interval around $L$ is positive.

Let $\varepsilon = \dfrac{L}{2}>0$ (possible since $L>0$). By the definition there is $\delta>0$ such that
$0<|x-a|<\delta$ implies $|f(x)-L|<\dfrac{L}{2}$. For such $x$,

$$f(x) > L - \frac{L}{2} = \frac{L}{2} > 0. \qquad \blacksquare$$

**Answer.** With $\delta$ corresponding to $\varepsilon = L/2$, $f(x)>L/2>0$ on the punctured
$\delta$-neighbourhood.

**Check.** If $L = 4$ and $f(x) = 4 - 10(x-1)$, then at $a=1$ the claim says $f>0$ near $1$. Indeed $f(x)>2$ whenever $x<1.2$, and $\delta = L/2/10 = 0.2$ is exactly the value the proof produces ✓.

**Remark.** The same argument with $\varepsilon = |L|/2$ shows that a *negative* limit forces $f<0$
nearby, and that a limit cannot be positive at a point where $f\le0$ throughout a neighbourhood. Sign
preservation is the key ingredient in many later theorems (for example, that a positive derivative
implies an increasing function).

## Challenge

**32.**

**Strategy.** *Scratch work.* With $f(x) = x^{2}+3x$ and $f(2) = 10$,

$$|f(x)-10| = |x^{2}+3x-10| = |x-2||x+5|.$$

The factor $|x-2|$ is controlled by $\delta$; the factor $|x+5|$ is not. Restrict to $|x-2|<1$: then $1<x<3$, so $6<x+5<8$ and $|x+5|<8$. Hence $|f(x)-10|<8|x-2|$, and $8|x-2|<\varepsilon$ if $|x-2|<\varepsilon/8$. Take the smaller of the two bounds.

*Proof.* Let $\varepsilon>0$ and set

$$\delta = \min\left(1,\frac{\varepsilon}{8}\right).$$

Suppose $0<|x-2|<\delta$. Then $|x-2|<1$, which gives $1<x<3$ and hence

$$|x+5| = x+5 < 8. \tag{$\ast$}$$

Also $|x-2|<\delta\le\varepsilon/8$. Multiplying the two positive inequalities $|x-2|<\varepsilon/8$ and $(\ast)$,

$$|f(x)-10| = |x-2|\cdot|x+5| < \frac{\varepsilon}{8}\cdot 8 = \varepsilon. \qquad \blacksquare$$

**Where $|x-2|<1$ is used.** Only in establishing $(\ast)$: without a bound on $x$, the factor
$|x+5|$ is unbounded and no single choice of $\delta$ proportional to $\varepsilon$ would control the
product. The restriction converts an unbounded factor into a constant, and the constant then determines
the coefficient $1/8$ in $\delta$.

**Answer.** $\delta = \min(1,\varepsilon/8)$.

**Check.** $\varepsilon = 0.1$ gives $\delta = 0.0125$; at $x = 2.0125$, $f(x) = 4.050156+6.0375 = 10.087656$, so $|f-10| = 0.0877<0.1$ ✓. The bound is a little wasteful (the true error is smaller), which is normal and harmless: $\varepsilon$-$\delta$ proofs need a $\delta$, not the best $\delta$.

**33.**

**Strategy.** Use $n$ equal subintervals of $[0,b]$, width $\Delta x = b/n$, with right endpoints $x_k = kb/n$.

$$S_n = \sum_{k=1}^{n}\left(\frac{kb}{n}\right)^{2}\frac{b}{n} = \frac{b^{3}}{n^{3}}\sum_{k=1}^{n}k^{2} = \frac{b^{3}}{n^{3}}\cdot\frac{n(n+1)(2n+1)}{6} = \frac{b^{3}(n+1)(2n+1)}{6n^{2}}.$$

Now divide out:

$$\frac{(n+1)(2n+1)}{6n^{2}} = \frac{2n^{2}+3n+1}{6n^{2}} = \frac13 + \frac{1}{2n} + \frac{1}{6n^{2}}.$$

As $n\to\infty$ the last two terms vanish, so

$$\lim_{n\to\infty}S_n = \frac{b^{3}}{3}.$$

**Check for $b=2$.** The formula gives $\dfrac{8}{3} = 2.6667$. Directly: $S_n = \frac{8(n+1)(2n+1)}{6n^{2}}$. At $n=10$: $\frac{8(11)(21)}{600} = \frac{1848}{600} = 3.08$; at $n=100$: $\frac{8(101)(201)}{60000} = \frac{162408}{60000} = 2.7068$; at $n=1000$: $2.67067$. The values decrease towards $2.6667$ ✓ — they must, since $f$ is increasing and right sums overestimate.

**Answer.** Area $= \dfrac{b^{3}}{3}$, verified at $b=2$ by three numerical sums.

**Remark.** Setting $b=1$ recovers the $\frac13$ of the tutorial's Example 9.9; the general-$b$ computation shows that the result scales as $b^{3}$, which is exactly what a change of variable predicts.

**34.**

**Strategy.** Suppose two limits and derive a contradiction, using $\varepsilon$ half the distance between them.

Suppose $\lim_{x\to a}f(x) = L$ and $\lim_{x\to a}f(x) = M$ with $L\ne M$. Let

$$\varepsilon = \frac{|L-M|}{2} > 0.$$

By the definition applied to $L$, there is $\delta_1>0$ such that $0<|x-a|<\delta_1$ implies
$|f(x)-L|<\varepsilon$. Applied to $M$, there is $\delta_2>0$ such that $0<|x-a|<\delta_2$ implies
$|f(x)-M|<\varepsilon$.

Set $\delta = \min(\delta_1,\delta_2)$. **Choose** any $x$ with $0<|x-a|<\delta$ — such an $x$ exists
because a limit is only ever taken at a point that has other domain points arbitrarily close to it (in
this topic, $f$ is defined on an interval around $a$). For that $x$, both inequalities hold, so by the
triangle inequality

$$|L-M| = |L-f(x)+f(x)-M| \le |L-f(x)| + |f(x)-M| < \varepsilon + \varepsilon = 2\varepsilon = |L-M|.$$

That is $|L-M|<|L-M|$, which is impossible. Hence $L = M$. $\blacksquare$

**Answer.** Limits are unique.

**Check.** The contradiction is strict: we obtain $c<c$ rather than $c\le c$, because both inequalities
are strict. If the definition used $\le$ instead of $<$, the argument would fail at exactly this point —
which is why the strict inequality in Definition 5.2 matters.

**Where the existence of nearby points is used.** At the word "choose". If $a$ were an isolated point of
the domain, there would be no $x$ with $0<|x-a|<\delta$, both statements would be vacuously true for
every $L$, and uniqueness would fail. Limits are only meaningful at points of accumulation, which is why
the definition presupposes that $f$ is defined on an interval around $a$ (except possibly at $a$).

**35.**

**Strategy.** For the squeeze, use the same $\delta$ for both bounds. For the example, bound $|x\sin(1/x)|$.

*Squeeze theorem.* Let $\varepsilon>0$. Since $\lim_{x\to a}g(x) = L$, there is $\delta_1>0$ with
$0<|x-a|<\delta_1 \Rightarrow L-\varepsilon<g(x)<L+\varepsilon$. Since $\lim_{x\to a}h(x) = L$, there is
$\delta_2>0$ with $0<|x-a|<\delta_2 \Rightarrow L-\varepsilon<h(x)<L+\varepsilon$. Let
$\delta = \min(\delta_1,\delta_2,\delta_3)$, where $\delta_3>0$ is any radius on which the inequality
$g\le f\le h$ holds. Then for $0<|x-a|<\delta$,

$$L-\varepsilon < g(x) \le f(x) \le h(x) < L+\varepsilon,$$

so $|f(x)-L|<\varepsilon$. Hence $\lim_{x\to a}f(x) = L$. $\blacksquare$

*Application.* Since $\left|\sin(1/x)\right|\le1$ for all $x\ne0$,

$$-|x| \le x\sin\frac1x \le |x| \qquad (x\ne0).$$

Both outer functions tend to $0$ as $x\to0$ (they are $\pm|x|$, and $|x|\to0$ by Exercise 12). By the
squeeze theorem with $L=0$,

$$\lim_{x\to0}x\sin\frac1x = 0.$$

*Why the same argument fails for $\dfrac1x\sin\dfrac1x$.* There the natural bound is
$\left|\frac1x\sin\frac1x\right|\le\frac1x$, and $\frac1x$ does not tend to a finite limit as $x\to0$: it
is unbounded above and below. The squeeze theorem requires *both* outer functions to converge to the
same finite $L$; here there is no such $L$, and indeed the function has no limit. A table would show
values like $0, \pm 10, \pm 100, \ldots$ depending on the sampling points — the same trap as
$\sin(1/x)$ in the tutorial.

**Answer.** Squeeze theorem proved; $x\sin(1/x)\to0$; $\frac1x\sin\frac1x$ has no limit (unbounded
oscillation), and the squeeze does not apply because there is no finite bounding limit.

**Check.** For $x = 0.001$, $|x\sin(1/x)|\le0.001$; the actual value is $0.001\sin(1000) = 0.000827$ ✓ —
small, as predicted. For $\frac1x\sin\frac1x$ at the same $x$ the value is $827$, not small at all ✓.

**36.**

**Strategy.** Distinguish three questions: what the arithmetic does, what the table shows, and what the
definition requires.

(a) The true error is $1-\dfrac{\sin x}{x} = \dfrac{x^{2}}{6} - \dfrac{x^{4}}{120}+\cdots$, so at
$x = 0.001$ the error is about $1.67\times10^{-7}$ and at $x=0.0001$ about $1.67\times10^{-9}$. Both are
far below $5\times10^{-7}$, the rounding threshold at six decimal places, so both print as $1.000000$.
The entry is not evidence that the value *is* $1$; it is evidence that the difference has fallen below
the display precision. (With even smaller $x$ the computation itself degrades: $\sin x$ then differs
from $x$ by less than one unit in the last place, and the quotient is computed as exactly $1$ — a
floating-point artefact, not a mathematical fact.)

(b) To convert the conjecture into a proof one needs a *bound* valid for all $x$ in a punctured
neighbourhood, not a sample. In a first calculus course this is done geometrically: for $0<x<\pi/2$,
compare the areas of a triangle, a sector and a triangle to get $\cos x<\dfrac{\sin x}{x}<1$, then
squeeze (Exercise 35) as $x\to0$. Alongside, one needs the one-sided argument for $x<0$ (where the
quotient is even, so the left limit equals the right) — the table's symmetry is suggestive but is not a
substitute for it.

(c) Every entry is reported to six decimal places, so a limit of $1.0000004$ would produce the same
displayed column: the reported digits are identical. Numerical evidence therefore cannot separate
hypotheses that differ below its resolution, and it can never establish a limit in the sense of
Definition 5.2, which quantifies over *all* $\varepsilon>0$ — including tolerances far smaller than any
display. Its role is to suggest the answer, to catch blunders, and to indicate the rate of convergence
(the error here is $O(x^{2})$, so each factor of $10$ in $x$ buys two decimal places).

**Answer.** (a) The error is below the display precision ($\approx x^{2}/6$); (b) a uniform bound and a
squeeze argument; (c) the table's resolution cannot distinguish limits that differ by less than
$10^{-6}$, and the definition demands a statement for every $\varepsilon$.

**Check.** $1-\sin(0.001)/0.001 = 1.667\times10^{-7}$ and $1-\sin(10^{-4})/10^{-4} = 1.667\times10^{-9}$
✓ — both below $5\times10^{-7}$, confirming why the printed entries are $1.000000$.

**Remark.** This is the honest status of numerical work in analysis: it is indispensable for discovering
theorems and for detecting errors, and it is never a proof of a limit statement. The two activities
complement each other, and confusing them is the most common way to be confidently wrong.
