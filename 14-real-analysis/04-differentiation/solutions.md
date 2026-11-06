# Differentiation — Solutions

> [Tutorial](README.md) · [Exercises](exercises.md) · 36 complete solutions

Every solution names the theorem or rule used. For the computational problems the derivative is
computed twice where that is feasible — once with the rules, once from the definition or by expansion —
because agreement is the cheapest check on algebra.

## Beginner

**1.**

With $f(x) = x^2$ and $a = 3$,
$$
\frac{f(x)-f(3)}{x-3} = \frac{x^2-9}{x-3} = \frac{(x-3)(x+3)}{x-3} = x+3 \qquad (x \ne 3),
$$
and $x \mapsto x+3$ is continuous at $3$ (a polynomial), so
$$
f'(3) = \lim_{x\to 3}(x+3) = 6 .
$$
The tangent line at $(3,9)$ has slope $6$:
$$
y = 9 + 6(x-3) = 6x - 9 .
$$
$\blacksquare$

*Check.* $(x^2)' = 2x$ gives $2\cdot 3 = 6$, and $6\cdot 3 - 9 = 9$. 

**2.**

Let $a \ne 0$. For $x \ne a$ with $x \ne 0$,
$$
\frac{1/x - 1/a}{x-a}
= \frac{\dfrac{a-x}{xa}}{x-a}
= \frac{a-x}{xa(x-a)}
= -\frac{1}{xa}.
$$
The last expression is a rational function of $x$ whose denominator is nonzero at $x = a$, hence
continuous at $a$ (Corollary 7.11(b) of [Continuity and Limits of Functions](../03-continuity-and-limits/README.md)),
so
$$
f'(a) = \lim_{x\to a}\Bigl(-\frac{1}{xa}\Bigr) = -\frac{1}{a^2}.
$$
$\blacksquare$

*Why the cancellation is legitimate.* $x \ne a$ is exactly the punctured condition in Definition 5.1; the
value at $x = a$ never enters a limit.

**3.**

At $a = 4$, $f(4) = 2$. For $x \ge 0$, $x \ne 4$, rationalise:
$$
\frac{\sqrt x - 2}{x-4}
= \frac{\sqrt x - 2}{(\sqrt x - 2)(\sqrt x + 2)}
= \frac{1}{\sqrt x + 2}.
$$
The denominator is $\ge 2$ near $x = 4$, so the expression is continuous at $4$ and
$$
f'(4) = \lim_{x\to 4}\frac{1}{\sqrt x + 2} = \frac{1}{4}.
$$
$\blacksquare$

*Check.* $(\sqrt x)' = \dfrac{1}{2\sqrt x}$, evaluated at $4$: $\dfrac{1}{2\cdot 2} = \dfrac14$. 

**4.**

**Product rule.** With $u(x) = x^2+1$ and $v(x) = x^3-2x$,
$$
u' = 2x, \qquad v' = 3x^2 - 2,
$$
so
$$
f' = u'v + uv' = 2x(x^3-2x) + (x^2+1)(3x^2-2).
$$
Expanding,
$$
2x(x^3-2x) = 2x^4 - 4x^2, \qquad (x^2+1)(3x^2-2) = 3x^4 + x^2 - 2,
$$
hence
$$
f'(x) = 5x^4 - 3x^2 - 2 .
$$
**Expansion check.** $f = x^5 - 2x^3 + x^3 - 2x = x^5 - x^3 - 2x$, whose derivative is
$5x^4 - 3x^2 - 2$. The two answers agree. $\blacksquare$

**5.**

With numerator $u = 2x+1$, $u' = 2$, and denominator $v = x^2+1$, $v' = 2x$:
$$
f'(x) = \frac{u'v - uv'}{v^2} = \frac{2(x^2+1) - (2x+1)(2x)}{(x^2+1)^2}.
$$
Expand the numerator:
$$
2x^2 + 2 - (4x^2 + 2x) = -2x^2 - 2x + 2 = -2(x^2 + x - 1).
$$
Hence
$$
f'(x) = -\frac{2(x^2+x-1)}{(x^2+1)^2}.
$$
$\blacksquare$

*Check at $x = 0$:* the formula gives $-2(-1)/1 = 2$. From the definition, $f(h) - f(0) = (2h+1)/(h^2+1) - 1 = (2h - h^2)/(h^2+1)$, so the quotient tends to $2$. ✓

**6.**

**(a)** Write $f(x) = (3x^2+1)^5 = \varphi(g(x))$ with $g(x) = 3x^2+1$ and $\varphi(y) = y^5$. Then $g'(x) = 6x$ and $\varphi'(y) = 5y^4$, so the chain rule gives
$$
f'(x) = 5(3x^2+1)^4\cdot 6x = 30x(3x^2+1)^4 .
$$
**(b)** With $g(x) = x^3$, $f(x) = \sin(g(x))$: $g'(x) = 3x^2$ and $(\sin)' = \cos$, so
$$
f'(x) = \cos(x^3)\cdot 3x^2 = 3x^2\cos(x^3).
$$
**(c)** With $g(x) = x^2+3$, $f = \sqrt{g}$: $g'(x) = 2x$ and $(\sqrt y)' = 1/(2\sqrt y)$ for $y>0$ (here $g \ge 3$), so
$$
f'(x) = \frac{1}{2\sqrt{x^2+3}}\cdot 2x = \frac{x}{\sqrt{x^2+3}} .
$$
$\blacksquare$

**7.**

$f(x) = x^4 - 2x^3 + x$. Then
$$
f'(x) = 4x^3 - 6x^2 + 1, \qquad f''(x) = 12x^2 - 12x, \qquad f'''(x) = 24x - 12 .
$$
At $x = 1$:
$$
f'(1) = 4 - 6 + 1 = -1, \qquad f''(1) = 12 - 12 = 0, \qquad f'''(1) = 24 - 12 = 12 .
$$
$\blacksquare$

*Remark.* $f''(1) = 0$ with $f'''(1) = 12 \ne 0$; at $x=1$ the function has an inflection point (the
second derivative changes sign there, since $f''(x) = 12x(x-1)$).

**8.**

At $x = 2$ the two one-sided quotients are
$$
f'_-(2) = \lim_{h\to 0^-}\frac{\lvert 2+h-2\rvert - 0}{h} = \lim_{h\to 0^-}\frac{-h}{h} = -1,
$$
because $\lvert h\rvert = -h$ for $h < 0$, and
$$
f'_+(2) = \lim_{h\to 0^+}\frac{\lvert h\rvert}{h} = \lim_{h\to 0^+}\frac{h}{h} = 1 .
$$
The one-sided derivatives exist and are different, so $f$ is not differentiable at $2$ (Definition 5.2
together with Theorem 7.7 of the previous chapter).

For $x > 2$ we have $f(x) = x-2$, so $f'(x) = 1$; for $x < 2$ we have $f(x) = 2-x$, so $f'(x) = -1$.
Hence $f$ is differentiable exactly on $\mathbb{R}\setminus\{2\}$. $\blacksquare$

**9.**

Let $a \ne 0$. Write $u := x^{1/3}$ and $v := a^{1/3}$, so that $u^3 - v^3 = x - a$ and
$$
\frac{x^{1/3}-a^{1/3}}{x-a} = \frac{u-v}{u^3-v^3} = \frac{u-v}{(u-v)(u^2+uv+v^2)} = \frac{1}{u^2+uv+v^2},
$$
for $x \ne a$ (so $u \ne v$). As $x \to a$, $u \to v$ by continuity of the cube root (the inverse of the
continuous strictly increasing $t \mapsto t^3$; or directly, $\lvert u^3 - v^3\rvert = \lvert x-a\rvert$).
Hence
$$
f'(a) = \frac{1}{3a^{2/3}} = \frac{1}{3\sqrt[3]{a^2}} .
$$
At $a = 0$ the difference quotient is
$$
\frac{f(h)-f(0)}{h} = \frac{h^{1/3}}{h} = \frac{1}{h^{2/3}} = \frac{1}{\lvert h\rvert^{2/3}} \longrightarrow +\infty,
$$
which is not a finite limit; by Definition 5.1, $f$ is not differentiable at $0$. $\blacksquare$

*Geometrically*, the graph of $x^{1/3}$ has a vertical tangent at the origin.

**10.**

Write
$$
f(x) = x\lvert x\rvert = \begin{cases} x^2, & x \ge 0,\\ -x^2, & x < 0.\end{cases}
$$
*At $0$:*
$$
\frac{f(h)-f(0)}{h} = \frac{h\lvert h\rvert}{h} = \lvert h\rvert \longrightarrow 0,
$$
so $f'(0) = 0$.

*At $x > 0$:* $f = x^2$ near $x$, so $f'(x) = 2x$. *At $x < 0$:* $f = -x^2$ near $x$, so $f'(x) = -2x$.

Hence $f$ is differentiable everywhere, with
$$
f'(x) = 2\lvert x\rvert \qquad (x \in \mathbb{R}),
$$
which is consistent with $f'(0) = 0$. $\blacksquare$

*Remark.* $f$ is actually continuously differentiable: $2\lvert x\rvert$ is continuous. This is a case in
which a piecewise formula has a derivative at the junction even though the two pieces are different
polynomials, because the *slopes* agree there.

**11.**

$y = x^3-3x$, so $y' = 3x^2-3$. At $x = 2$: $y(2) = 8-6 = 2$ and $y'(2) = 12-3 = 9$. The tangent line is
$$
y = 2 + 9(x-2) = 9x - 16 .
$$
The tangent is horizontal where $y' = 0$, i.e. $3x^2 = 3$, $x = \pm 1$. The corresponding points are
$$
(1,\ 1-3) = (1,-2), \qquad (-1,\ -1+3) = (-1,2).
$$
$\blacksquare$

*Interpretation.* At a horizontal tangent the function has a critical point; by Fermat's lemma these are
the only candidates for local extrema of a differentiable function. Here $f' = 3(x-1)(x+1)$ changes sign
from $+$ to $-$ at $-1$ (local maximum) and from $-$ to $+$ at $1$ (local minimum).

**12.**

$A(r) = \pi r^2$, so $A'(r) = 2\pi r$ and
$$
A'(3) = 6\pi .
$$
The derivative is the rate of change of area with respect to radius: for a small increase $\Delta r$, the
area increases by approximately $6\pi\,\Delta r$.

Geometrically, the extra area is a thin annulus of radius about $3$ and width $\Delta r$; its area is
approximately (circumference at radius $3$) $\times$ (width) $= 2\pi\cdot 3\cdot \Delta r = 6\pi\,\Delta r$,
and the error is $\pi(\Delta r)^2$, which is smaller than linear in $\Delta r$. This is the geometric
content of differentiability: the increment is linear to first order, with a quadratic error. $\blacksquare$

## Intermediate

**13.**

Write $\tan x = \dfrac{\sin x}{\cos x}$. The functions $\sin$ and $\cos$ are differentiable on
$\mathbb{R}$, and $\cos x \ne 0$ on the domain under consideration; by Corollary 7.14 of
[Continuity and Limits of Functions](../03-continuity-and-limits/README.md) (a continuous nonvanishing
function is bounded away from $0$ near each point), the denominator does not vanish on a neighbourhood
of $x$, so the quotient rule (Theorem 7.4) applies:
$$
(\tan)' = \frac{(\sin)'\cos - \sin(\cos)'}{\cos^2}
= \frac{\cos x\cos x - \sin x(-\sin x)}{\cos^2 x}
= \frac{\cos^2 x + \sin^2 x}{\cos^2 x}
= \frac{1}{\cos^2 x}
= \sec^2 x .
$$
$\blacksquare$

*Note.* The identity $\cos^2 x + \sin^2 x = 1$ is the Pythagorean identity of elementary trigonometry.
The chain rule and product rule were used in computing $(\sin)' = \cos$ and $(\cos)' = -\sin$, which are
assumed from the table in Section 8.

**14.**

**(a) $f$ even.** For every $x$ and every $h \ne 0$,
$$
\frac{f(-x+h)-f(-x)}{h} = \frac{f(x-h)-f(x)}{h},
$$
because $-x + h = -(x - h)$ and $f$ is even. Put $k := -h$; as $h \to 0$, $k \to 0$ and
$$
\frac{f(x-h)-f(x)}{h} = \frac{f(x+k)-f(x)}{-k} = -\frac{f(x+k)-f(x)}{k} \longrightarrow -f'(x).
$$
Hence $f'(-x)$ exists and equals $-f'(x)$: $f'$ is odd. $\blacksquare$

**(b) $f$ odd.** For every $x$ and $h \ne 0$,
$$
\frac{f(-x+h)-f(-x)}{h} = \frac{-f(x-h)+f(x)}{h} = \frac{f(x)-f(x-h)}{h},
$$
using $f(-x) = -f(x)$ and $f(-(x-h)) = -f(x-h)$. With $k := -h$,
$$
\frac{f(x)-f(x-h)}{h} = \frac{f(x)-f(x+k)}{-k} = \frac{f(x+k)-f(x)}{k} \longrightarrow f'(x).
$$
Hence $f'(-x) = f'(x)$: $f'$ is even. $\blacksquare$

*Check.* $\sin$ is odd and $(\sin)' = \cos$ is even; $\cos$ is even and $(\cos)' = -\sin$ is odd.
Both are consistent with the exercise.

**15.**

By the product rule (Theorem 7.3), $(fg)' = f'g + fg'$ wherever $f$ and $g$ are differentiable. Since
$f$ and $g$ are twice differentiable at $a$, the functions $f'$ and $g'$ are differentiable at $a$, and so
each term of $f'g + fg'$ is a product of functions differentiable at $a$. Apply the product rule twice
more:
$$
(fg)'' = \bigl(f'g\bigr)' + \bigl(fg'\bigr)' = \bigl(f''g + f'g'\bigr) + \bigl(f'g' + fg''\bigr)
= f''g + 2f'g' + fg'' .
$$
Evaluating at $a$ gives the stated formula. $\blacksquare$

*Remark.* The general Leibniz rule is $(fg)^{(n)} = \sum_{k=0}^{n}\binom nk f^{(k)}g^{(n-k)}$, proved by
induction using the same "differentiate each product" step. For $n = 2$ it reads
$\binom20 f''g + \binom21 f'g' + \binom22 fg''$, which is the formula above.

**16.**

Since $f(a) = 0$, the difference quotient of $\lvert f\rvert$ at $a$ is
$$
\frac{\lvert f\rvert(a+h)-\lvert f\rvert(a)}{h} = \frac{\lvert f(a+h)\rvert - 0}{h} = \frac{\lvert f(a+h)\rvert}{h}, \qquad h \ne 0 .
$$

**If $f'(a) = 0$.** Then for $h \ne 0$,
$$
\left\lvert \frac{\lvert f(a+h)\rvert}{h}\right\rvert = \frac{\lvert f(a+h)-f(a)\rvert}{\lvert h\rvert} \longrightarrow 0,
$$
because the difference quotient of $f$ tends to $0$ and the absolute value of the quotient tends to the
absolute value of the limit (Solution 13 of the previous chapter). Hence $\lvert f\rvert'(a) = 0$.

**If $f'(a) = L \ne 0$.** Then
$$
\frac{\lvert f(a+h)\rvert}{\lvert h\rvert} \longrightarrow \lvert L\rvert > 0,
$$
and $\dfrac{\lvert f(a+h)\rvert}{h} = \operatorname{sign}(h)\cdot\dfrac{\lvert f(a+h)\rvert}{\lvert h\rvert}$.
Hence the right-hand limit is $\lvert L\rvert$ and the left-hand limit is $-\lvert L\rvert$. Since
$\lvert L\rvert \ne 0$, the two one-sided limits differ, so $\lvert f\rvert$ is not differentiable at $a$.

Therefore $\lvert f\rvert$ is differentiable at $a$ exactly when $f'(a) = 0$, and then the derivative is
$0$. $\blacksquare$

*Example.* $f(x) = x$ at $a = 0$: $\lvert f\rvert(x) = \lvert x\rvert$ is not differentiable at $0$, and
$f'(0) = 1 \ne 0$. $f(x) = x^2$ at $a = 0$: $\lvert f\rvert = f$ is differentiable with derivative $0$,
and $f'(0) = 0$.

**17.**

**At $0$.** For $h \ne 0$,
$$
\left\lvert \frac{f(h)-f(0)}{h}\right\rvert \le \frac{\lvert f(h)\rvert}{\lvert h\rvert} \le \frac{h^2}{\lvert h\rvert} = \lvert h\rvert,
$$
because $f(h) = h^2$ if $h$ is rational and $f(h) = 0$ otherwise, so in either case $\lvert f(h)\rvert \le h^2$.
The squeeze theorem gives $f(h)/h \to 0$, hence $f'(0) = 0$.

**At $a \ne 0$ rational.** Then $f(a) = a^2 \ne 0$. By density of the irrationals there are irrational
$t_n \to a$ with $t_n \ne a$. For these,
$$
\frac{f(t_n)-f(a)}{t_n-a} = \frac{0 - a^2}{t_n - a} = -\frac{a^2}{t_n-a},
$$
whose absolute value tends to $+\infty$ because the numerator tends to $a^2 > 0$ and the denominator
tends to $0$. If $f$ were differentiable at $a$, the difference quotient would converge along every
sequence (Theorem 7.3 of the previous chapter) to a finite value; it does not. So $f$ is not
differentiable at $a$.

**At $a$ irrational.** Then $f(a) = 0$. By density of $\mathbb{Q}$ there are rationals $q_n \to a$ with
$q_n \ne a$. For these,
$$
\frac{f(q_n)-f(a)}{q_n-a} = \frac{q_n^2}{q_n-a} ,
$$
and $\lvert q_n^2/(q_n-a)\rvert \to +\infty$, since $q_n^2 \to a^2 > 0$ and $q_n - a \to 0$. Again the
difference quotient is unbounded along a sequence tending to $a$, so $f$ is not differentiable there.

Hence $f$ is differentiable exactly at $0$. $\blacksquare$

*Remark.* Compare Example 9.7 of the previous chapter: $x \mapsto x$ on $\mathbb{Q}$ and $0$ elsewhere is
*continuous* only at $0$; the present function is *differentiable* only at $0$. Multiplying the rational
branch by $x$ supplies the extra cancellation needed for differentiability.

**18.**

Let $x > 0$ and define
$$
h(t) := \ln(1+t) - t, \qquad k(t) := \ln(1+t) - \frac{t}{1+t}, \qquad t \ge 0 .
$$
Both are differentiable on $[0,\infty)$ (sums of differentiable functions; $\ln(1+t)$ is differentiable
for $t > -1$ with derivative $1/(1+t)$ by the inverse-function formula, Exercise 22 or the table of
Section 8).

*Right inequality.*
$$
h'(t) = \frac{1}{1+t} - 1 = -\frac{t}{1+t} < 0 \qquad (t > 0).
$$
By Theorem 7.9(iii), $h$ is strictly decreasing on $[0,x]$, so $h(x) < h(0) = \ln 1 - 0 = 0$, i.e.
$$
\ln(1+x) < x .
$$

*Left inequality.*
$$
k'(t) = \frac{1}{1+t} - \frac{(1+t) - t}{(1+t)^2} = \frac{1}{1+t} - \frac{1}{(1+t)^2} = \frac{(1+t)-1}{(1+t)^2} = \frac{t}{(1+t)^2} > 0
$$
for $t > 0$. Hence $k$ is strictly increasing on $[0,x]$, so $k(x) > k(0) = 0$, i.e.
$$
\ln(1+x) > \frac{x}{1+x} .
$$
Combining, $\dfrac{x}{1+x} < \ln(1+x) < x$ for every $x > 0$. $\blacksquare$

*Remark.* Both inequalities are strict for $x>0$ and become equalities at $x=0$. The right-hand one is
the case $n=1$ of $\ln(1+x) \le x$; the left-hand one is used to prove that $(1+1/n)^n$ increases to $e$.

**19.**

**(a)** Let $f(x) = e^x - 1 - x$ and $g(x) = x^2$ on $(-1,1)$. Both are differentiable; $f(0) = 1-1-0 = 0$
and $g(0) = 0$; $g'(x) = 2x \ne 0$ for $x \ne 0$. Theorem 7.14 applies if the limit of $f'/g'$ exists:
$$
\frac{f'(x)}{g'(x)} = \frac{e^x - 1}{2x}.
$$
This is again of type $0/0$ at $0$ (numerator $e^0 - 1 = 0$, denominator $0$), with derivative of the
denominator $2 \ne 0$. A second application gives
$$
\frac{(e^x-1)'}{(2x)'} = \frac{e^x}{2} \longrightarrow \frac12 \qquad (x\to 0)
$$
by continuity of $\exp$. Working backwards through the two applications,
$$
\lim_{x\to 0}\frac{e^x-1-x}{x^2} = \frac12 .
$$

**(b)** Let $f(x) = \tan x - x$ and $g(x) = x^3$ near $0$. Both are differentiable on $(-\pi/2,\pi/2)$;
$f(0) = 0 - 0 = 0$, $g(0) = 0$; $g'(x) = 3x^2 \ne 0$ for $x\ne 0$. Then
$$
\frac{f'(x)}{g'(x)} = \frac{\sec^2 x - 1}{3x^2} = \frac{\tan^2 x}{3x^2},
$$
using $\sec^2 x - 1 = \tan^2 x$. This is again $0/0$ at $0$; apply the rule once more with
$f_1 = \tan^2 x$, $g_1 = 3x^2$, $g_1'(x) = 6x \ne 0$:
$$
\frac{f_1'(x)}{g_1'(x)} = \frac{2\tan x\,\sec^2 x}{6x} = \frac{1}{3}\cdot\frac{\tan x}{x}\cdot\sec^2 x .
$$
As $x \to 0$, $\tan x/x = (\sin x/x)\cdot(1/\cos x) \to 1\cdot 1 = 1$ (using the standard limit
$\sin x/x \to 1$), and $\sec^2 x \to 1$. Hence the last quotient tends to $1/3$, and so does $f'/g'$, and
therefore
$$
\lim_{x\to 0}\frac{\tan x - x}{x^3} = \frac13 .
$$
$\blacksquare$

*Check.* The Taylor expansions $\tan x = x + x^3/3 + O(x^5)$ and $e^x = 1 + x + x^2/2 + O(x^3)$ give the
same answers, $1/3$ and $1/2$.

**20.**

**(a)** Write $x\ln x = \dfrac{\ln x}{1/x}$ for $x \in (0,1)$. Let $f(x) = \ln x$ and $g(x) = 1/x$. Both
are differentiable on $(0,1)$; $g'(x) = -1/x^2 \ne 0$; and $g(x) \to +\infty$ as $x \to 0^+$, so the
$\infty/\infty$ form of L'Hôpital's rule (Theorem 7.15) applies if $f'/g'$ has a limit. Compute
$$
\frac{f'(x)}{g'(x)} = \frac{1/x}{-1/x^2} = -x \longrightarrow 0 \qquad (x\to 0^+).
$$
Hence $\lim_{x\to 0^+} x\ln x = 0$.

**(b)** For $x > 0$ write $x^{1/x} = e^{(\ln x)/x}$. By part (a) applied to the substitution $x = 1/t$
(or directly), $\dfrac{\ln x}{x} \to 0$ as $x \to \infty$: indeed this is an $\infty/\infty$ form, and
$$
\frac{(\ln x)'}{(x)'} = \frac{1/x}{1} = \frac1x \longrightarrow 0 .
$$
By continuity of $\exp$ at $0$, $e^{(\ln x)/x} \to e^0 = 1$. Hence
$$
\lim_{x\to\infty} x^{1/x} = 1 .
$$
$\blacksquare$

**21.**

If $a = b$ both inequalities are trivial. Assume $a < b$. The function $\sin$ is continuous on $[a,b]$
and differentiable on $(a,b)$, so the mean value theorem (Theorem 7.8) gives $c \in (a,b)$ with
$$
\sin b - \sin a = \cos c\,(b-a).
$$
Taking absolute values and using $\lvert\cos c\rvert \le 1$,
$$
\lvert\sin b - \sin a\rvert = \lvert\cos c\rvert\,\lvert b-a\rvert \le \lvert b-a\rvert .
$$
If $a > b$, swap the roles. The same argument with $\cos$ in place of $\sin$ gives
$\lvert\cos b - \cos a\rvert \le \lvert b-a\rvert$, since $(\cos)' = -\sin$ and $\lvert-\sin c\rvert \le 1$.
$\blacksquare$

*Remark.* The inequalities say that $\sin$ and $\cos$ are $1$-Lipschitz on $\mathbb{R}$; by Corollary 7.10
this is a consequence of their derivatives being bounded by $1$, and it gives another proof that they are
uniformly continuous on $\mathbb{R}$.

**22.**

**Additivity.** Fix $y > 0$ and define
$$
G(x) := f(xy) - f(x) - f(y), \qquad x > 0 .
$$
The function $x \mapsto f(xy)$ is differentiable on $(0,\infty)$ by the chain rule, with derivative
$y\,f'(xy)$; hence $G$ is differentiable and
$$
G'(x) = y\,f'(xy) - f'(x) = y\cdot\frac{1}{xy} - \frac1x = \frac1x - \frac1x = 0 .
$$
By Theorem 7.9(i), $G$ is constant on the interval $(0,\infty)$. Evaluating at $x = 1$,
$$
G(1) = f(y) - f(1) - f(y) = -f(1) = 0,
$$
because $f(1) = 0$ by hypothesis. Hence $G(x) = 0$ for all $x$, i.e. $f(xy) = f(x)+f(y)$.

**Monotonicity.** On $(0,\infty)$, $f'(x) = 1/x > 0$, so $f$ is strictly increasing by Theorem 7.9(ii).
$\blacksquare$

*Remark.* Together with $f(1) = 0$, the two properties characterise the natural logarithm: $f(xy) = f(x)+f(y)$
and $f'(x) = 1/x$ force $f = \ln$. The exercise shows how differentiability plus a functional equation
determines a function; the same technique proves $f(x+y) = f(x)+f(y)$ and $f' = c$ imply $f(x) = cx$.

## Advanced

**23.**

Put
$$
g(x) := f(x) - \lambda x, \qquad x \in [a,b].
$$
Then $g$ is continuous on $[a,b]$ (it is a difference of differentiable, hence continuous, functions) and
differentiable on $(a,b)$, with
$$
g'(x) = f'(x) - \lambda .
$$
In particular
$$
g'(a) = f'(a) - \lambda < 0, \qquad g'(b) = f'(b) - \lambda > 0 .
$$

**The minimum is not attained at $a$.** Since $g'(a) < 0$, the right-hand difference quotient satisfies
$$
\frac{g(a+h)-g(a)}{h} \longrightarrow g'(a) < 0 \qquad (h \to 0^+).
$$
Choose $\varepsilon := -g'(a)/2 > 0$. There is $\delta > 0$ such that for $0 < h < \delta$,
$$
\frac{g(a+h)-g(a)}{h} < g'(a) + \varepsilon = \frac{g'(a)}{2} < 0,
$$
so $g(a+h) < g(a)$. Hence $a$ is not a point of minimum of $g$ on $[a,b]$.

**The minimum is not attained at $b$.** Since $g'(b) > 0$, for $h \to 0^-$,
$$
\frac{g(b+h)-g(b)}{h} \longrightarrow g'(b) > 0 .
$$
Choose $\delta > 0$ such that for $-\delta < h < 0$ the quotient exceeds $g'(b)/2 > 0$. Since $h < 0$,
multiplying by $h$ reverses the inequality: $g(b+h) - g(b) < 0$, i.e. $g(b+h) < g(b)$. Hence $b$ is not a
point of minimum either.

**Conclusion.** By the extreme value theorem (Theorem 7.17 of [Continuity and Limits of Functions](../03-continuity-and-limits/README.md)),
$g$ attains its minimum on $[a,b]$ at some point $c$. By the two paragraphs above, $c \in (a,b)$. Since $g$
is differentiable at the interior point $c$ and has a local (indeed global) minimum there, Fermat's lemma
(Theorem 7.6) gives $g'(c) = 0$, that is $f'(c) = \lambda$. $\blacksquare$

*Remark.* The same argument proves the general form: if $f'(a) > \lambda > f'(b)$, apply the result to
$-f$ and $-\lambda$. Darboux's theorem therefore says that the image of an interval under a derivative is
an interval — the intermediate value property — even when the derivative is not continuous.

**24.**

**(a)** Let $x < y$ be points of $I$. By the mean value theorem on $[x,y]$ there is $c \in (x,y)$ with
$$
f(y) - f(x) = f'(c)(y-x),
$$
hence $\lvert f(y)-f(x)\rvert \le M\lvert y-x\rvert$. Thus $f$ is $M$-Lipschitz, and Lipschitz functions
are uniformly continuous: given $\varepsilon > 0$, take $\delta := \varepsilon/M$ if $M > 0$ (any $\delta$
if $M = 0$); then $\lvert x-y\rvert < \delta$ implies $\lvert f(x)-f(y)\rvert < \varepsilon$, with $\delta$
independent of the point. $\blacksquare$

**(b)** Let
$$
f(x) := \begin{cases} x^2\sin\dfrac{1}{x^2}, & x \ne 0,\\[4pt] 0, & x = 0,\end{cases}
\qquad x \in [-1,1].
$$
*Continuous:* on $[-1,1]\setminus\{0\}$ it is a product and composition of continuous functions, and at $0$
we have $\lvert f(x)\rvert \le x^2 \to 0 = f(0)$. Hence $f$ is continuous on the compact interval
$[-1,1]$, so it is uniformly continuous there by Theorem 7.18 of
[Continuity and Limits of Functions](../03-continuity-and-limits/README.md).

*Differentiable everywhere:* at $x \ne 0$ the product and chain rules give
$$
f'(x) = 2x\sin\frac{1}{x^2} - \frac{2}{x}\cos\frac{1}{x^2},
$$
and at $0$,
$$
\frac{f(h)-f(0)}{h} = h\sin\frac{1}{h^2} \longrightarrow 0
$$
by the squeeze theorem, so $f'(0) = 0$.

*Derivative unbounded:* at $x_n := 1/\sqrt{2n\pi}$ we have $\sin(1/x_n^2) = \sin(2n\pi) = 0$ and
$\cos(1/x_n^2) = 1$, so
$$
f'(x_n) = -\frac{2}{x_n} = -2\sqrt{2n\pi} \longrightarrow -\infty .
$$
Hence $\lvert f'\rvert$ is unbounded on $[-1,1]$, although $f$ is uniformly continuous there. $\blacksquare$

*Moral.* Uniform continuity controls the *size* of increments, not the *rate of change* at a point. The
hypothesis $\lvert f'\rvert \le M$ is sufficient for Lipschitz continuity but far from necessary.

**25.**

Let $n \in \mathbb{N}$ and define
$$
g(t) := (1+t)^n - 1 - nt, \qquad t \ge -1 .
$$
Then $g$ is differentiable on $(-1,\infty)$ with
$$
g'(t) = n(1+t)^{n-1} - n = n\bigl[(1+t)^{n-1} - 1\bigr].
$$

*Case $x \ge 0$.* For $t \ge 0$ we have $1+t \ge 1$, hence $(1+t)^{n-1} \ge 1$ and $g'(t) \ge 0$. By
Theorem 7.9(ii), $g$ is nondecreasing on $[0,x]$, so $g(x) \ge g(0) = 1 - 1 - 0 = 0$. This is
$(1+x)^n \ge 1+nx$.

*Case $-1 \le x < 0$.* For $t \in (x,0)$ we have $0 \le 1+t \le 1$; if $n \ge 2$ then $(1+t)^{n-1} \le 1$,
and if $n = 1$ then $g \equiv 0$. Hence $g'(t) \le 0$ on $(x,0)$, so $g$ is nonincreasing on $[x,0]$.
Therefore $g(x) \ge g(0) = 0$ (moving left from $0$ can only increase a nonincreasing function). Again
$(1+x)^n \ge 1+nx$.

The case $x = -1$ gives $0 \ge 1 - n$, which is true for all $n \ge 1$. $\blacksquare$

*Remark.* For $n \ge 2$ and $x > -1$, $x \ne 0$, the inequality is strict, because $g'$ has the sign of
$t$ and vanishes only at $t = 0$.

**26.**

We prove first that $f = 0$ on $[0,1/2]$. By the extreme value theorem, $\lvert f\rvert$ attains a maximum
$M \ge 0$ on $[0,1/2]$, at some point $c$.

If $c = 0$, then $M = \lvert f(0)\rvert = 0$ and we are done.

If $c > 0$, the mean value theorem on $[0,c]$ gives $\xi \in (0,c)$ with
$$
f(c) - f(0) = f'(\xi)\,c .
$$
Since $f(0) = 0$ and $c \le 1/2$,
$$
M = \lvert f(c)\rvert = \lvert f'(\xi)\rvert\,c \le \lvert f(\xi)\rvert\cdot\frac12 \le \frac{M}{2},
$$
where the middle inequality is the hypothesis $\lvert f'\rvert \le \lvert f\rvert$ and the last is the
maximality of $M$. Hence $M \le M/2$, so $M = 0$ and $f \equiv 0$ on $[0,1/2]$.

**Induction.** Suppose $f \equiv 0$ on $[0, n/2]$ for some $n \ge 1$; we prove $f \equiv 0$ on
$[n/2, (n+1)/2]$. Let $M$ be the maximum of $\lvert f\rvert$ on that interval, attained at $c$. If
$c = n/2$ then $M = 0$ by the induction hypothesis. Otherwise $c > n/2$, and the MVT on $[n/2, c]$ (where
$f(n/2) = 0$) gives $\xi \in (n/2, c)$ with
$$
M = \lvert f(c)\rvert = \lvert f'(\xi)\rvert\,\Bigl(c - \frac n2\Bigr) \le \lvert f(\xi)\rvert\cdot\frac12 \le \frac M2,
$$
so $M = 0$. Hence $f \equiv 0$ on $[n/2,(n+1)/2]$.

By induction, $f \equiv 0$ on $[0, \infty)$. $\blacksquare$

*Remark.* This is a one-dimensional Gronwall argument. The inequality $\lvert f'\rvert \le \lvert f\rvert$
forces $f$ to vanish because, on an interval of length $\le 1/2$, the mean value inequality gains a factor
$\le 1/2$; iterating drives the bound to $0$. On an interval of length $> 1/2$ the same argument would give
$M \le M$ and no information, which is why the proof is done in steps.

**27.**

Apply Theorem 7.16 to $f(x) = e^x$ with $a = 0$ and $n = 2$. Since $f^{(k)}(x) = e^x$ for every $k$,
$$
f(0) = f'(0) = f''(0) = 1,
$$
so the Taylor polynomial is $P_2(x) = 1 + x + \dfrac{x^2}{2}$ and, for each $x \in (0,1]$, there is
$c \in (0,x)$ with
$$
e^x = 1 + x + \frac{x^2}{2} + \frac{e^c}{6}x^3 .
$$
Because $0 < c < x \le 1$, we have $1 < e^c < e$; hence
$$
0 < e^x - \Bigl(1+x+\frac{x^2}{2}\Bigr) = \frac{e^c}{6}x^3 \le \frac{e}{6}x^3 .
$$
Taking absolute values (the quantity is positive) gives the stated bound. For $x = 0$ both sides are $0$.
$\blacksquare$

*Numerical content.* $e^1 = 2.71828\ldots$, $1 + 1 + 1/2 = 2.5$, and the actual error is $0.218\ldots$,
below the bound $e/6 \approx 0.453$.

**28.**

By Corollary 7.20, $f'' > 0$ on $(0,1)$ implies that $f$ is strictly convex on $[0,1]$: for all
$x, y \in [0,1]$, $t \in (0,1)$ with $x \ne y$,
$$
f\bigl((1-t)x+ty\bigr) < (1-t)f(x) + tf(y) .
$$
Let $x \in (0,1)$ and take $y := 1$, $t := x$, so that $(1-t)\cdot 0 + t\cdot 1 = x$ and $1 - t = 1-x$:
$$
f(x) < (1-x)f(0) + x f(1) = (1-x)\cdot 0 + x\cdot 0 = 0 .
$$
Hence $f(x) < 0$ for every $x \in (0,1)$. $\blacksquare$

*Remark.* Strict convexity is where the strict inequality comes from: a convex function with $f(0)=f(1)=0$
can be zero on all of $[0,1]$ (take $f \equiv 0$), but if $f''>0$ it cannot. Geometrically, the graph lies
strictly below a chord whose endpoints are both at height $0$.

**29.**

Fix $x \in I$. Since $f$ is convex and differentiable on $I$, Theorem 7.19 shows that $f'$ is
nondecreasing.

*If $y > x$*, the MVT on $[x,y]$ gives $\xi \in (x,y)$ with $f(y)-f(x) = f'(\xi)(y-x)$. Since $\xi > x$,
$f'(\xi) \ge f'(x)$, and $y - x > 0$, so
$$
f(y) - f(x) = f'(\xi)(y-x) \ge f'(x)(y-x),
$$
i.e. $f(y) \ge f(x) + f'(x)(y-x)$.

*If $y < x$*, the MVT on $[y,x]$ gives $\xi \in (y,x)$ with $f(y)-f(x) = f'(\xi)(y-x)$. Now $\xi < x$, so
$f'(\xi) \le f'(x)$, and $y - x < 0$; multiplying the inequality by the negative number $y-x$ reverses it:
$$
f(y)-f(x) = f'(\xi)(y-x) \ge f'(x)(y-x).
$$
Again $f(y) \ge f(x) + f'(x)(y-x)$. *If $y = x$*, both sides equal $f(x)$. $\blacksquare$

*Remark.* The inequality says that the tangent line at $x$ lies below the graph — the "supporting
hyperplane" property of convex functions. It is the key to the analysis of convex optimisation, where it
converts a local first-order condition into a global optimality certificate.

**30.**

**(a)** *Injectivity.* If $x < x'$, the MVT on $[x,x']$ gives $\xi$ with
$$
f(x') - f(x) = f'(\xi)(x'-x) \ge m(x'-x) > 0,
$$
so $f(x') > f(x)$ and $f$ is strictly increasing, hence injective.

*Surjectivity.* For $x > 0$, the MVT on $[0,x]$ gives $f(x) - f(0) \ge mx$, so $f(x) \ge f(0)+mx \to +\infty$;
for $x < 0$, $f(x) - f(0) = f'(\xi)x \le mx$ (multiplying the inequality $f'(\xi)\ge m$ by the negative
number $x$ reverses it), so $f(x) \le f(0)+mx \to -\infty$. Since $f$ is continuous, the intermediate value
theorem applied on $[x,0]$ or $[0,x]$ shows that every $y \in \mathbb{R}$ is attained. Hence $f$ is a
bijection of $\mathbb{R}$ onto $\mathbb{R}$.

**(b)** Write $g := f^{-1}$ and fix $y_0$, $x_0 := g(y_0)$. For all $y, y'$,
$$
\lvert y - y'\rvert = \lvert f(g(y)) - f(g(y'))\rvert \ge m\,\lvert g(y)-g(y')\rvert,
$$
by the MVT applied to $f$ on the interval with endpoints $g(y), g(y')$. Hence
$$
\lvert g(y)-g(y')\rvert \le \frac{1}{m}\lvert y-y'\rvert,
$$
so $g$ is continuous (given $\varepsilon>0$, take $\delta := m\varepsilon$).

Now for $y \ne y_0$, with $x := g(y) \ne x_0 := g(y_0)$,
$$
\frac{g(y)-g(y_0)}{y-y_0} = \frac{x-x_0}{f(x)-f(x_0)} = \frac{1}{\dfrac{f(x)-f(x_0)}{x-x_0}} .
$$
As $y \to y_0$, the displayed Lipschitz estimate gives $x \to x_0$. The difference quotient of $f$ at $x_0$ tends to
$f'(x_0) \ge m > 0$, so by the quotient rule for limits (Theorem 7.5(d) of
[Continuity and Limits of Functions](../03-continuity-and-limits/README.md)) the reciprocal tends to
$1/f'(x_0)$. Hence
$$
g'(y_0) = \frac{1}{f'(g(y_0))} .
$$
No continuity of $f'$ is needed: only the existence of $f'(x_0)$ and the lower bound $m > 0$.

**(c)** This is the displayed Lipschitz estimate. $\blacksquare$

## Challenge

**31.**

**Differentiability at $0$.** For $h \ne 0$,
$$
\frac{f(h)-f(0)}{h} = \frac{h^2\sin(1/h)}{h} = h\sin\frac1h ,
$$
and $\lvert h\sin(1/h)\rvert \le \lvert h\rvert \to 0$, so $f'(0) = 0$ by the squeeze theorem.

**Differentiability off $0$.** On $\mathbb{R}\setminus\{0\}$, $f$ is a product of $x^2$ and
$\sin(1/x)$; both are differentiable, and the chain rule gives
$$
f'(x) = 2x\sin\frac1x + x^2\cos\frac1x\cdot\Bigl(-\frac{1}{x^2}\Bigr) = 2x\sin\frac1x - \cos\frac1x .
$$
Hence $f$ is differentiable on all of $\mathbb{R}$.

**Discontinuity of $f'$ at $0$.** Let $x_n := \dfrac{1}{2n\pi}$ and $y_n := \dfrac{1}{(2n+1)\pi}$. Then
$x_n, y_n \to 0$, and
$$
f'(x_n) = 2x_n\sin(2n\pi) - \cos(2n\pi) = 0 - 1 = -1,
\qquad
f'(y_n) = 0 - \cos((2n+1)\pi) = 1 .
$$
Both sequences tend to $0$ but the images tend to $-1$ and $1$ respectively, so $\lim_{x\to 0} f'(x)$ does
not exist. Since $f'(0) = 0$, $f'$ is discontinuous at $0$.

**Non-monotonicity near $0$.** Let $\delta > 0$. Choose $n$ so large that $x_n < \delta$ and $y_n < \delta$.
Then $x_n, y_n \in (0,\delta)$ and $f'(x_n) = -1 < 0$, $f'(y_n) = 1 > 0$.

Suppose $f$ were nondecreasing on $(-\delta,\delta)$. Then for every $t$ in that interval and every $h > 0$
small, $(f(t+h)-f(t))/h \ge 0$, so letting $h \to 0^+$ gives $f'(t) \ge 0$; this contradicts $f'(x_n) < 0$.
Suppose $f$ were nonincreasing. Then the difference quotients are $\le 0$, giving $f'(t) \le 0$ for all
$t$, contradicting $f'(y_n) > 0$. Hence $f$ is monotone on no open interval containing $0$. $\blacksquare$

*Remark.* The derivative of this function is bounded ($\lvert f'\rvert \le 3$) and discontinuous; the
derivative of $x^2\sin(1/x^2)$ is unbounded and also discontinuous. Neither function is $C^1$ at $0$, and
both illustrate why the inverse function theorem requires $f'$ continuous rather than merely existing and
nonzero.

**32.**

Suppose such an $f$ exists. It is differentiable on $\mathbb{R}$, hence continuous, so Darboux's theorem
(Theorem 7.11, or Exercise 23) applies on the interval $[0,1]$. We have
$$
f'(0) = 0 < \frac12 < 1 = f'(1).
$$
By Darboux's theorem there is $c \in (0,1)$ with $f'(c) = 1/2$. But $c \ne 0$, so the hypothesis says
$f'(c) = 1$, a contradiction. Hence no such function exists. $\blacksquare$

*Remark.* This is the standard demonstration that derivatives are not arbitrary functions: a derivative
cannot jump. Without Darboux's theorem it is still possible to see the obstruction by considering
$g(x) = f(x) - x$ on $(0,1)$, which has $g' \equiv 0$ there, hence is constant; then $f'(0)$ would have to
equal the constant $1$ by continuity of the difference quotients at $0$ — but the cleanest proof is
Darboux's.

**33.**

Let $\varepsilon > 0$. Since $f'(x) \to L$, there is $M \ge M_0$ such that
$$
\lvert f'(t) - L\rvert < \varepsilon \qquad \text{for all } t > M .
$$
Let $x > M$. The mean value theorem on $[M,x]$ gives $c \in (M,x)$ with
$$
f(x) - f(M) = f'(c)(x-M).
$$
Divide by $x > 0$:
$$
\frac{f(x)}{x} = \frac{f(M)}{x} + f'(c)\,\frac{x-M}{x} .
$$
Since $L - \varepsilon < f'(c) < L + \varepsilon$ and $0 < \dfrac{x-M}{x} < 1$,
$$
\frac{f(M)}{x} + (L-\varepsilon)\frac{x-M}{x} < \frac{f(x)}{x} < \frac{f(M)}{x} + (L+\varepsilon)\frac{x-M}{x}.
$$
As $x \to \infty$, $\dfrac{f(M)}{x} \to 0$ and $\dfrac{x-M}{x} \to 1$. Hence there is $X \ge M$ such that
for $x > X$ the left-hand side exceeds $L - 2\varepsilon$ and the right-hand side is below $L + 2\varepsilon$.
Therefore $\lvert f(x)/x - L\rvert < 2\varepsilon$ for $x > X$, which is the definition of
$\lim_{x\to\infty} f(x)/x = L$. $\blacksquare$

*Remark.* The converse is false: $f(x) = \sin(x^2)/x$ has $f(x)/x \to 0$ while $f'(x) = 2\cos(x^2) - \sin(x^2)/x^2$
has no limit. A bounded derivative is a *sufficient* condition for the asymptotic slope to be $L$, not a
necessary one.

**34.**

By Theorem 7.16 with $n = 1$ applied on the interval with endpoints $a$ and $x$, there is $c_x$ strictly
between $a$ and $x$ with
$$
f(x) = f(a) + f'(a)(x-a) + \frac{f''(c_x)}{2}(x-a)^2 .
$$
(Here $f'$ is continuous on the closed interval and $f''$ exists in its interior, as required.) Subtract
the claimed approximation and divide by $(x-a)^2$:
$$
\frac{f(x)-f(a)-f'(a)(x-a)-\frac12 f''(a)(x-a)^2}{(x-a)^2}
= \frac12\bigl(f''(c_x) - f''(a)\bigr).
$$
Since $\lvert c_x - a\rvert < \lvert x-a\rvert$, we have $c_x \to a$ as $x \to a$. Continuity of $f''$ at
$a$ gives $f''(c_x) \to f''(a)$, hence the displayed expression tends to $0$. Therefore
$$
f(x) = f(a) + f'(a)(x-a) + \frac{f''(a)}{2}(x-a)^2 + o\bigl((x-a)^2\bigr) \qquad (x\to a).
$$
$\blacksquare$

*Remark.* The Lagrange form gives a *quantitative* error (a specific point $c_x$), while the Young form
gives only a qualitative statement ($o((x-a)^2)$); the latter needs no more than continuity of $f''$ at
the single point $a$, which is why it is useful in multivariable settings where the Lagrange form is not
available.

**35.**

Define
$$
g(x) := e^{-x}f(x), \qquad x \ge 0 .
$$
By the product and chain rules, $g$ is differentiable on $[0,\infty)$ with
$$
g'(x) = -e^{-x}f(x) + e^{-x}f'(x) = e^{-x}\bigl(f'(x)-f(x)\bigr) \le 0,
$$
because $e^{-x} > 0$ and $f'(x) \le f(x)$ by hypothesis. Hence $g$ is nonincreasing on $[0,\infty)$
(Theorem 7.9(iii)). Since $g(0) = e^0 f(0) = 0$, we have
$$
g(x) \le g(0) = 0 \qquad \text{for all } x \ge 0 .
$$
Finally $e^{-x} > 0$, so $g(x) \le 0$ gives $f(x) \le 0$ for all $x \ge 0$. $\blacksquare$

*Remark.* The integrating factor $e^{-x}$ is chosen so that the derivative of $e^{-x}f$ reproduces the
combination $f' - f$. This is the one-dimensional prototype of the integrating-factor method for linear
differential equations, and it shows that the differential inequality $f' \le f$ with zero initial data
forces $f \le 0$ — a comparison principle.

**36.**

Let $u < v$ be any two points of $I$. By Darboux's theorem (Theorem 7.11, or Exercise 23), $f'$ has the
intermediate value property on $[u,v]$: for every $\lambda$ strictly between $f'(u)$ and $f'(v)$ there is
$c \in (u,v)$ with $f'(c) = \lambda$.

Hence the image $f'[I]$ is an interval: given any two values $f'(u), f'(v)$ in it, every intermediate
value is also attained. But $f'[I] \subseteq \mathbb{Z}$ by hypothesis, and the only intervals contained in
$\mathbb{Z}$ are single points. Therefore $f'$ is constant on $I$: there is $A \in \mathbb{Z}$ with
$f'(x) = A$ for all $x \in I$.

Now let $h(x) := f(x) - Ax$. Then $h$ is differentiable on $I$ with $h'(x) = f'(x) - A = 0$ for all $x$.
By Theorem 7.9(i), $h$ is constant on $I$: there is $B \in \mathbb{R}$ with $h(x) = B$. Hence
$$
f(x) = Ax + B \qquad \text{for all } x \in I .
$$
$\blacksquare$

*Remark.* The result can fail without the intermediate value property: a function that agrees with $0$ on
$(-\infty,0)$ and with $x$ on $[0,\infty)$ is not differentiable at $0$, and any attempt to smooth the
transition produces non-integer derivatives by Darboux. The hypothesis "$f'(x) \in \mathbb{Z}$" is much
stronger than "$f'(x)$ is bounded", and the discreteness of $\mathbb{Z}$ is what converts the
intermediate value property into constancy.
