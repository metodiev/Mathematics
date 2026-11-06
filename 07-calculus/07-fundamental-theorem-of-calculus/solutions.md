# The Fundamental Theorem of Calculus — Solutions

> [The Fundamental Theorem of Calculus](README.md) · Solutions to the 36 problems in [exercises.md](exercises.md)

Each solution begins with the strategy, then carries out every step. Every antiderivative obtained is
checked by differentiation, and for proof problems the proof is complete. Pitfalls are flagged where
they occur.

## Beginner

### Solution 1

*Strategy: find one antiderivative by the power rule, check it, then apply Part 2.*

An antiderivative of $3x^2 - 4x + 1$ is

$$G(x) = 3\cdot\frac{x^3}{3} - 4\cdot\frac{x^2}{2} + x = x^3 - 2x^2 + x .$$

*Check:* $G'(x) = 3x^2 - 4x + 1$. ✓

By Theorem 7.4.1,

$$\int_0^2\left(3x^2-4x+1\right)dx = G(2) - G(0) = \left(8 - 8 + 2\right) - 0 = 2 .$$

*Sanity check:* the integrand equals $1$ at $x=0$ and $5$ at $x=2$, so the integral lies between $2\cdot1$
and $2\cdot5$; the value $2$ is at the lower end, which is plausible because the integrand is below $2$
on most of the interval. Indeed $3x^2 - 4x + 1 = (3x-1)(x-1)$ is positive on $[0,1/3)$, negative on
$(1/3,1)$, and positive on $(1,2]$, so cancellation occurs.

### Solution 2

*Strategy: rewrite the integrand as a power and use the power rule with $n = -\frac12$.*

$$\int_1^4 t^{-1/2}\,dt = \left[\frac{t^{1/2}}{1/2}\right]_1^4 = \left[2\sqrt{t}\right]_1^4 = 2\cdot 2 - 2\cdot 1 = 2 .$$

*Check:* $\frac{d}{dt}\left(2\sqrt t\right) = 2\cdot\frac{1}{2\sqrt t} = t^{-1/2}$. ✓

*Remark:* the answer is positive, as it must be, because $t^{-1/2} > 0$ on $[1,4]$.

### Solution 3

*Strategy: an antiderivative of $\cos x$ is $\sin x$.*

$$\int_0^{\pi/2}\cos x\,dx = \left[\sin x\right]_0^{\pi/2} = \sin\frac{\pi}{2} - \sin 0 = 1 - 0 = 1 .$$

*Check:* $\frac{d}{dx}\sin x = \cos x$. ✓ The value is positive because $\cos x \ge 0$ on $[0,\pi/2]$.

### Solution 4

*Strategy: compute from an antiderivative, then confirm by a symmetry argument; the two must agree.*

*First method.* An antiderivative of $x^3 + x$ is $\frac{x^4}{4} + \frac{x^2}{2}$, so

$$\int_{-1}^{1}\left(x^3+x\right)dx = \left[\frac{x^4}{4} + \frac{x^2}{2}\right]_{-1}^{1}
= \left(\frac14 + \frac12\right) - \left(\frac14 + \frac12\right) = 0 .$$

*Check:* $\frac{d}{dx}\left(\frac{x^4}{4}+\frac{x^2}{2}\right) = x^3 + x$. ✓

*Second method.* The integrand $g(x) = x^3 + x$ is odd: $g(-x) = -x^3 - x = -g(x)$. Substituting
$t = -x$ in $\int_{-1}^0 g$ shows it equals $-\int_0^1 g$, so the two halves cancel. (This is the
two-line justification of the rule "the integral of an odd function over a symmetric interval is
zero".)

*Pitfall:* the vanishing is a cancellation of signed areas, not an absence of area. The geometric area
$\int_{-1}^1|x^3+x|\,dx$ is positive.

### Solution 5

*Strategy: Part 1 with a constant lower limit; the integrand is continuous on $\mathbb{R}$ because
$t^2+2 \ge 2 > 0$.*

$$F'(x) = \frac{x^2+1}{x^2+2} .$$

The lower limit $0$ does not appear: by Lemma 7.1.1 it only shifts $F$ by a constant.

### Solution 6

*Strategy: Part 1, after identifying where the integrand is real and continuous.*

The integrand $\sqrt{t^3+1}$ is defined and continuous for $t \ge -1$. For $x \ge -1$ the interval
$[2,x]$ (or $[x,2]$) lies in $[-1,\infty)$, so

$$G'(x) = \sqrt{x^3+1}, \qquad x \ge -1 .$$

*Check at a point:* $G'(0) = 1$. Numerically, $G(h) - G(0) = \int_0^h\sqrt{1+t^3}\,dt \approx h$ for small
$h$, so the difference quotient is about $1$. ✓

*Pitfall:* writing the formula for $x < -1$ is meaningless, because the integrand is not real there.

### Solution 7

*Strategy: chain rule in the upper limit (Theorem 7.8.1) with $g(x) = x^2$.*

The integrand $\sin t$ is continuous everywhere, so

$$H'(x) = \sin\left(x^2\right)\cdot\frac{d}{dx}\left(x^2\right) = 2x\sin\left(x^2\right).$$

*Check at $x = \sqrt{\pi}$:* the formula gives $2\sqrt\pi\sin\pi = 0$. Plausible: $H(x) = 1 - \cos(x^2)$,
whose derivative is $2x\sin(x^2)$. ✓ (Here the integral can be computed exactly, which is a luxury.)

### Solution 8

*Strategy: the variable limit is the lower one. Reverse the limits to turn it into an upper limit.*

$$K(x) = \int_x^5\cos\left(t^2\right)dt = -\int_5^x \cos\left(t^2\right)dt,$$

so by Part 1, since $\cos(t^2)$ is continuous everywhere,

$$K'(x) = -\cos\left(x^2\right).$$

*Check at $x=0$:* $K'(0) = -1$; for small positive $h$, $K(h) - K(0) = -\int_0^h\cos(t^2)dt \approx -h$,
so the quotient is about $-1$. ✓

*Pitfall:* forgetting the minus sign. The upper limit $5$ is constant and contributes nothing; the
lower limit does, with a minus sign.

### Solution 9

*Strategy: integrate term by term; on $x>0$ the antiderivative of $1/x$ is $\ln x$.*

$$\int\left(3x^2 - \frac{2}{x}\right)dx = x^3 - 2\ln x + C, \qquad x > 0 .$$

*Check:* $\frac{d}{dx}\left(x^3 - 2\ln x + C\right) = 3x^2 - \frac{2}{x}$. ✓

*Pitfall:* on the larger domain $x \ne 0$ the constant would have to be written separately on each
side of $0$ (Example 7.6.2), and the antiderivative would involve $\ln|x|$. Since the problem restricts
to $x>0$, $\ln x$ is correct and no absolute value is needed.

### Solution 10

*Strategy: find the general antiderivative, then impose the condition.*

$F(x) = x^4 + C$ because $\frac{d}{dx}x^4 = 4x^3$. The condition gives $F(1) = 1 + C = 5$, so $C = 4$
and

$$F(x) = x^4 + 4 .$$

*Check:* $F'(x) = 4x^3$ and $F(1) = 5$. ✓ Equivalently, $F(x) = 5 + \int_1^x 4t^3\,dt = 5 + x^4 - 1$.

### Solution 11

*Strategy: compute the average, then solve $f(c) = f_{\mathrm{avg}}$ and check that $c$ lies in the
interval.*

$$\frac{1}{4-0}\int_0^4 x\,dx = \frac14\cdot\left[\frac{x^2}{2}\right]_0^4 = \frac14\cdot 8 = 2 .$$

Solve $c = 2$: the only solution is $c = 2 \in [0,4]$. ✓

*Remark:* $f$ is strictly increasing, so the solution is unique; in general there may be several
(§9.6).

### Solution 12

*Strategy: the net change of $Q$ is the integral of its rate (Theorem 7.7.1).*

$$Q(3) - Q(0) = \int_0^3(2t+1)\,dt = \left[t^2 + t\right]_0^3 = 9 + 3 = 12 .$$

*Check:* $\frac{d}{dt}(t^2+t) = 2t+1$. ✓ The answer is positive because the rate is positive; there is
no cancellation.

## Intermediate

### Solution 13

*Strategy: split the integral at a constant so that both limits become upper limits, then apply the
chain rule.*

$$F(x) = \int_x^{x^2}\sqrt{1+t^3}\,dt = \int_0^{x^2}\sqrt{1+t^3}\,dt - \int_0^x\sqrt{1+t^3}\,dt .$$

With $G(u) = \int_0^u\sqrt{1+t^3}\,dt$ and $G'(u) = \sqrt{1+u^3}$,

$$F'(x) = G'(x^2)\cdot 2x - G'(x)\cdot 1 = 2x\sqrt{1+x^6} - \sqrt{1+x^3} .$$

*Interval of validity.* The integrand must be real on the interval between $x$ and $x^2$, which requires
$t \ge -1$ there. If $x \ge -1$ then both $x$ and $x^2$ lie in $[-1,\infty)$ and so does the whole
interval between them; if $x<-1$ then $x<-1<x^2$ and the interval contains values $t<-1$, where
$1+t^3<0$. So the formula holds for $x \ge -1$.

*Value at $x=1$:* $F'(1) = 2\sqrt2 - \sqrt2 = \sqrt2 \approx 1.414$.

*Sanity check at $x=1$:* for small $h$, both limits move, the upper at speed $2$ and the lower at speed
$1$; the integrand is $\sqrt2$ at both ends, so the leading change is
$\sqrt2(2h) - \sqrt2(h) = \sqrt2\,h$. ✓

### Solution 14

*Strategy: both limits variable (Theorem 7.8.2), with the integrand continuous everywhere.*

The upper limit is $\cos x$ and the lower is $\sin x$, so

$$G'(x) = e^{(\cos x)^2}\cdot(-\sin x) - e^{(\sin x)^2}\cdot(\cos x)
= -\sin x\,e^{\cos^2 x} - \cos x\,e^{\sin^2 x} .$$

*Check at $x=0$:* $G'(0) = 0\cdot e - 1\cdot e^0 = -1$. Plausible: near $0$, the interval is
$[\sin x, \cos x] \approx [x, 1]$, which *shrinks* as $x$ increases because the lower limit rises, so
the integral decreases at rate about $-e^{0} = -1$. ✓

*Pitfall:* the two terms are not symmetric, because the derivatives of $\sin$ and $\cos$ differ in sign.

### Solution 15

*Strategy: the variable $x$ appears both in the limit and inside the integrand. Expand the integrand so
that $x$ multiplies a plain integral, then differentiate.*

Write

$$\int_0^x (x-t)f(t)\,dt = x\int_0^x f(t)\,dt - \int_0^x t\,f(t)\,dt .$$

Both integrands are continuous (products of continuous functions), so Part 1 and the product rule give

$$\frac{d}{dx}\left[x\int_0^x f(t)\,dt\right] = \int_0^x f(t)\,dt + x f(x), \qquad
\frac{d}{dx}\int_0^x t f(t)\,dt = x f(x) .$$

Subtracting, the terms $x f(x)$ cancel:

$$\frac{d}{dx}\int_0^x (x-t)f(t)\,dt = \int_0^x f(t)\,dt .$$

Differentiating once more with Part 1 gives $\frac{d^2}{dx^2}\int_0^x (x-t)f(t)\,dt = f(x)$.

*Check with $f \equiv 1$:* the left side is $\int_0^x (x-t)dt = x^2/2$, whose first derivative is $x$,
and $\int_0^x 1\,dt = x$. ✓

### Solution 16

*Strategy: Part 1 gives $F'$ explicitly; the sign of $F'$ determines monotonicity.*

The integrand is continuous on $\mathbb{R}$, so

$$F'(x) = \frac{x^2-4}{x^2+1} = \frac{(x-2)(x+2)}{x^2+1} .$$

The denominator is positive, so the sign of $F'$ is the sign of $(x-2)(x+2)$.

| Interval | sign of $F'$ | behaviour of $F$ |
|---|---|---|
| $(-\infty,-2)$ | $+$ | increasing |
| $(-2,2)$ | $-$ | decreasing |
| $(2,\infty)$ | $+$ | increasing |

At $x=-2$, $F$ changes from increasing to decreasing: local maximum. At $x=2$, from decreasing to
increasing: local minimum. Since $F'$ is continuous and vanishes exactly at $\pm2$, these are the only
critical points.

*Remark:* the values can be computed from
$F(x) = \int_1^x\left(1 - \frac{5}{t^2+1}\right)dt = (x-1) - 5\left(\arctan x - \frac{\pi}{4}\right)$, but
they are not required.

### Solution 17

*Strategy: compute the average, then solve $c^3 = f_{\mathrm{avg}}$ and keep the root in $[0,2]$.*

$$f_{\mathrm{avg}} = \frac{1}{2-0}\int_0^2 x^3\,dx = \frac12\cdot\left[\frac{x^4}{4}\right]_0^2
= \frac12\cdot\frac{16}{4} = \frac12\cdot 4 = 2 .$$

Solve $c^3 = 2$: since $x \mapsto x^3$ is strictly increasing on $\mathbb{R}$, there is exactly one real
solution, $c = \sqrt[3]{2} \approx 1.260$. It lies in $[0,2]$. ✓

### Solution 18

*Strategy: compute the average, solve $1/c = f_{\mathrm{avg}}$, and verify the interval condition.*

$$f_{\mathrm{avg}} = \frac{1}{3-1}\int_1^3\frac{dx}{x} = \frac{\ln 3 - \ln 1}{2} = \frac{\ln 3}{2} .$$

Solve $1/c = \frac{\ln 3}{2}$, that is, $c = \frac{2}{\ln 3}$. Numerically,
$\ln 3 \approx 1.0986$, so $c \approx 1.8205$, and $1 \le 1.8205 \le 3$. ✓

*Check:* $f(c) = \frac{\ln 3}{2} \approx 0.5493$, and $f_{\mathrm{avg}} \approx 0.5493$. ✓

*Pitfall:* the point is not the midpoint $c=2$; there $f(2) = \frac12 \ne \frac{\ln 3}{2}$.

### Solution 19

*Strategy: displacement is the integral of velocity; distance is the integral of speed, so split at the
zeros of $v$.*

$v(t) = t^2-2t = t(t-2)$, so $v \le 0$ on $[0,2]$ and $v \ge 0$ on $[2,3]$.

*Displacement.* An antiderivative is $s(t) = \frac{t^3}{3} - t^2$:

$$\int_0^3 v(t)\,dt = s(3) - s(0) = (9-9) - 0 = 0 .$$

*Distance.* On $[0,2]$ the speed is $-v$; on $[2,3]$ it is $v$. Now $s(2) = \frac83 - 4 = -\frac43$, so

$$\int_0^2 |v| = -\left(s(2)-s(0)\right) = \frac43, \qquad
\int_2^3 |v| = s(3)-s(2) = 0 + \frac43 = \frac43 .$$

Total distance $= \frac43 + \frac43 = \frac83 \approx 2.667$ m. Displacement $= 0$ m.

*Interpretation:* the particle moves left for two seconds and returns to its starting point after three
seconds, having travelled $\frac83$ m in total.

### Solution 20

*Strategy: average value, then solve $3c^2 = f_{\mathrm{avg}}$.*

$$v_{\mathrm{avg}} = \frac12\int_0^2 3t^2\,dt = \frac12\left[t^3\right]_0^2 = \frac12\cdot 8 = 4 .$$

Solve $3c^2 = 4$: $c = \pm\frac{2}{\sqrt3}$, and only $+\frac{2}{\sqrt3} \approx 1.1547$ lies in $[0,2]$.
✓

### Solution 21

*Strategy: differentiate both sides of the identity; then verify.*

**(a)** Differentiating $\int_0^x f = x^3+x$ with respect to $x$ gives $f(x) = 3x^2+1$ by Part 1 (the
left side is differentiable because $f$ is continuous). *Verification:*
$\int_0^x(3t^2+1)dt = x^3 + x$. ✓ So $f(x) = 3x^2+1$ is the unique solution.

**(b)** Differentiating $\int_1^x f = \ln x$ for $x>0$ gives $f(x) = \frac1x$. *Verification:*
$\int_1^x \frac{dt}{t} = \ln x - \ln 1 = \ln x$. ✓

*Pitfall:* differentiating an identity produces a *necessary* condition. Here it is also sufficient,
because the candidate is verified by substituting back; that verification is part of the solution, not
an optional extra.

### Solution 22

*Strategy: recognise a $0/0$ form and differentiate the numerator with Part 1.*

As $x\to0$, the numerator $\int_0^x\cos(t^2)dt \to 0$ and the denominator $x \to 0$. By Part 1 the
numerator has derivative $\cos(x^2)$, which is continuous, so l'Hôpital's rule applies:

$$\lim_{x\to0}\frac{\int_0^x\cos(t^2)dt}{x} = \lim_{x\to0}\frac{\cos(x^2)}{1} = \cos 0 = 1 .$$

*Check:* for small $x$ the integrand is about $1$, so the integral is about $x$ and the quotient about
$1$. ✓

*Remark:* this limit is exactly the statement $F'(0) = f(0)$ for $F(x) = \int_0^x\cos(t^2)dt$.

### Solution 23

*Strategy: $0/0$ form; one application of l'Hôpital reduces it to a standard limit.*

$$\lim_{x\to0}\frac{\int_0^x(e^t-1)dt}{x^2}
\overset{\text{l'H}}{=} \lim_{x\to0}\frac{e^x-1}{2x}
\overset{\text{l'H}}{=} \lim_{x\to0}\frac{e^x}{2} = \frac12 .$$

The first step differentiates the numerator with Part 1 (the integrand $e^t-1$ is continuous) and the
denominator with the power rule; the second step is again a $0/0$ form, and both new derivatives are
continuous.

*Check by expansion:* $e^t - 1 = t + t^2/2 + O(t^3)$, so the integral is $x^2/2 + O(x^3)$ and the
quotient tends to $\frac12$. ✓

### Solution 24

*Strategy: integrate piecewise. On each piece $f$ is a polynomial, so the accumulation function is a
polynomial; at the break points the pieces must be joined continuously.*

*Values.* On $[0,1]$, $F(x) = \int_0^x t\,dt = \frac{x^2}{2}$, so $F(1) = \frac12$.

For $1 \le x \le 2$,

$$F(x) = \frac12 + \int_1^x (3-t)\,dt = \frac12 + \left[3t - \frac{t^2}{2}\right]_1^x
= \frac12 + \left(3x - \frac{x^2}{2}\right) - \left(3 - \frac12\right) = 3x - \frac{x^2}{2} - 2 .$$

Check: at $x=1$ this gives $3 - \frac12 - 2 = \frac12$ ✓ (the pieces agree at the break point).

Hence $F\left(\frac32\right) = \frac92 - \frac98 - 2 = \frac{36 - 9 - 16}{8} = \frac{11}{8}$, and
$F(2) = 6 - 2 - 2 = 2$. For $x \ge 2$, $f = 0$, so $F(x) = 2$; in particular $F(3) = 2$.

*Where $F' = f$ fails.* The integrand is continuous at $0$ (both one-sided values are $0$), so
$F'(0) = f(0) = 0$. At $x=1$ the left limit of $f$ is $1$ but $f(1) = 2$: a jump, so $F'(1)$ does not
exist. At $x=2$ the left limit of $f$ is $1$ but $f(2) = 0$: another jump, so $F'(2)$ does not exist.
The identity $F'(x) = f(x)$ therefore holds on $[0,1)$, on $(1,2)$, and on $(2,\infty)$, and fails at
$x = 1$ and $x = 2$.

*Pitfall:* the failure is at the jumps of $f$, not at every break point of the *formula* for $F$. At
$x=0$ the formula changes but $f$ is continuous, so $F$ is differentiable there.

## Advanced

### Solution 25

*Strategy: differentiate the given identity, using Part 1.*

Let $F(x) = \int_a^x f(t)\,dt$. Since $f$ is continuous, Part 1 applies and $F'(x) = f(x)$ for
$x \in (a,b)$, with one-sided derivatives $f(a)$ and $f(b)$ at the endpoints. The hypothesis says
$F(x) = 0$ for all $x \in [a,b]$, so $F$ is constant and $F' = 0$ everywhere. Hence $f(x) = 0$ for
$x \in (a,b)$, and by continuity of $f$ at the endpoints, $f(a) = \lim_{x\to a^+}f(x) = 0$ and
$f(b) = 0$. So $f \equiv 0$ on $[a,b]$. $\blacksquare$

*Remark:* continuity is essential. If $f$ is $1$ at a single point and $0$ elsewhere, the integral
$\int_a^x f$ is $0$ for every $x$, but $f$ is not identically zero.

### Solution 26

*Strategy: use the estimate of §8.10 for the absolute difference, then translate it into the
$\varepsilon$–$\delta$ definition of uniform continuity.*

Since $f$ is continuous on the closed bounded interval $[a,b]$, it is bounded and attains its maximum
(Extreme Value Theorem), so $M = \max_{[a,b]}|f|$ is finite.

For $x < y$ in $[a,b]$,

$$F(y) - F(x) = \int_x^y f(t)\,dt, \qquad
|F(y)-F(x)| \le \int_x^y|f(t)|\,dt \le M(y-x) = M|y-x| .$$

The case $y < x$ is the same after swapping, and $x = y$ is trivial. Hence the Lipschitz estimate holds
for all $x,y$.

*Uniform continuity.* Let $\varepsilon > 0$. If $M > 0$, take $\delta = \varepsilon/M$; then
$|y-x| < \delta$ implies $|F(y)-F(x)| \le M|y-x| < \varepsilon$. If $M = 0$ then $F$ is constant, so any
$\delta$ works. Since $\delta$ depends only on $\varepsilon$ and not on the point, $F$ is uniformly
continuous on $[a,b]$. $\blacksquare$

### Solution 27

*Strategy: define the difference of the two halves as a continuous function of the cut point, and apply
the Intermediate Value Theorem.*

Define

$$H(x) = \int_a^x f(t)\,dt - \int_x^b f(t)\,dt, \qquad x \in [a,b] .$$

Both terms are continuous in $x$ (Lemma 7.1.2), so $H$ is continuous on $[a,b]$. Moreover

$$H(a) = 0 - \int_a^b f = -I, \qquad H(b) = I - 0 = I, \qquad I := \int_a^b f .$$

If $I = 0$, take $c = a$: then $\int_a^c f = 0 = \int_a^b f = \int_c^b f$. If $I \ne 0$, then $H(a)$ and
$H(b)$ have opposite signs, so by the Intermediate Value Theorem there is $c \in (a,b)$ with
$H(c) = 0$, that is, $\int_a^c f = \int_c^b f$. $\blacksquare$

*Remark:* the equality says the cut point bisects the *signed* area, not necessarily the geometric area.
For $f(x) = x$ on $[-1,1]$, every $c$ works, since both halves of a symmetric integral cancel.

### Solution 28

*Strategy: suppose $f$ is positive somewhere and use continuity to find an interval on which $f$ is
bounded below by a positive number; then the integral is positive.*

Suppose, for contradiction, that $f(x_0) > 0$ for some $x_0 \in [a,b]$. By continuity at $x_0$ with
$\varepsilon = f(x_0)/2 > 0$ there is $\delta > 0$ such that $|x - x_0| < \delta$ implies
$f(x) > f(x_0)/2$.

Let $I = [a,b] \cap (x_0-\delta, x_0+\delta)$. This interval has positive length $\ell$ — if $x_0$ is an
endpoint, take the half of the neighbourhood inside $[a,b]$. Since $f \ge 0$ everywhere and
$f > f(x_0)/2$ on $I$, monotonicity of the integral gives

$$\int_a^b f \ge \int_I f \ge \frac{f(x_0)}{2}\,\ell > 0,$$

contradicting $\int_a^b f = 0$. Hence no such $x_0$ exists and $f \equiv 0$. $\blacksquare$

*Continuity is needed.* On $[0,1]$ let $f(0) = 1$ and $f(x) = 0$ for $x>0$. Then $f \ge 0$ and
$\int_0^1 f = 0$, because the integral is unchanged by altering the value at a single point, yet $f$ is
not identically zero. The function is not continuous at $0$.

### Solution 29

*Strategy: this is the second Mean Value Theorem for integrals (Theorem 7.2.2) with $g(x) = x^2$.*

The function $f$ is continuous on $[0,1]$ and $g(x) = x^2$ is continuous and non-negative there, hence
integrable. By Theorem 7.2.2 there is $c \in [0,1]$ with

$$\int_0^1 x^2 f(x)\,dx = f(c)\int_0^1 x^2\,dx = f(c)\cdot\frac13 . \;\blacksquare$$

*Remark:* the weight $x^2$ is not uniform, so $c$ is a weighted average point, not the ordinary average
point. If $f(x) = x$, then $\int_0^1 x^3dx = \frac14$ and $\frac{f(c)}{3} = \frac{c}{3}$ give
$c = \frac34$, which indeed lies in $[0,1]$.

### Solution 30

*Strategy: define the integral as a function of the lower limit and show that its derivative is zero.*

Define $H(a) = \int_a^{a+p} f(t)\,dt$ for $a \in \mathbb{R}$. The integrand is continuous, so by
Theorem 7.8.2

$$H'(a) = f(a+p)\cdot 1 - f(a)\cdot 1 = f(a+p) - f(a) = 0,$$

using periodicity. Since $H' = 0$ on the interval $\mathbb{R}$, Theorem 7.6.1 gives that $H$ is constant.
At $a = 0$, $H(0) = \int_0^p f$. Hence $H(a) = \int_0^p f$ for every $a$. $\blacksquare$

*Check with an example:* for $f(t) = \sin t$ and $p = 2\pi$, $\int_a^{a+2\pi}\sin t\,dt = 0 = \int_0^{2\pi}\sin t\,dt$ for every $a$. ✓

### Solution 31

*Strategy: transform $F(-x)$ into an integral from $0$ to $x$ by the substitution $t = -u$, then compare
with $F(x)$ and differentiate the resulting identity.*

First compute, for $x > 0$,

$$F(-x) = \int_0^{-x} f(t)\,dt = -\int_{-x}^{0} f(t)\,dt .$$

In $\int_{-x}^0 f(t)\,dt$ substitute $t = -u$, $dt = -du$; the limits $t=-x$ and $t=0$ become $u=x$ and
$u=0$, so

$$\int_{-x}^{0} f(t)\,dt = \int_{x}^{0} f(-u)(-du) = \int_0^x f(-u)\,du .$$

Hence $F(-x) = -\int_0^x f(-u)\,du$. The same identity holds for $x<0$ by a symmetric argument, and at
$x=0$ both sides are $0$.

**(i) $F$ even $\Leftrightarrow$ $f$ odd.**
If $f$ is odd, then $f(-u) = -f(u)$ and $F(-x) = -\int_0^x(-f(u))du = \int_0^x f = F(x)$, so $F$ is even.
Conversely, if $F$ is even then for all $x$,
$-\int_0^x f(-u)du = \int_0^x f(u)du$, that is, $\int_0^x\left[f(-u)+f(u)\right]du = 0$. The integrand is
continuous, so by the argument of Solution 25 it vanishes identically: $f(-x) + f(x) = 0$ for all $x$,
i.e. $f$ is odd.

**(ii) $F$ odd $\Leftrightarrow$ $f$ even.**
If $f$ is even, $f(-u) = f(u)$ and $F(-x) = -\int_0^x f = -F(x)$, so $F$ is odd. Conversely, if $F$ is
odd then $-\int_0^x f(-u)du = -\int_0^x f(u)du$, so
$\int_0^x\left[f(-u)-f(u)\right]du = 0$ for all $x$, and differentiation gives $f(-x) = f(x)$. $\blacksquare$

*Check:* $f(t) = t$ is odd and $F(x) = x^2/2$ is even ✓; $f(t) = t^2$ is even and $F(x) = x^3/3$ is odd ✓.

### Solution 32

*Strategy: compute the derivative on each side of $0$, examine the one-sided limits at $0$, and compare
with the requirement of Theorem 7.4.1.*

*Derivative for $x \ne 0$.* By the chain rule,

$$G'(x) = -\frac{d}{dx}\arctan\left(\frac1x\right)
= -\frac{1}{1 + (1/x)^2}\cdot\left(-\frac{1}{x^2}\right) = \frac{1}{x^2+1} .$$

So $G$ is an antiderivative of $\frac{1}{1+x^2}$ on each of $(-\infty,0)$ and $(0,\infty)$.

*Behaviour at $0$.* As $x\to 0^+$, $\frac1x \to +\infty$, so $\arctan\frac1x \to \frac{\pi}{2}$ and
$G(x) \to -\frac{\pi}{2}$. As $x \to 0^-$, $\frac1x \to -\infty$, so $\arctan\frac1x \to -\frac{\pi}{2}$
and $G(x) \to +\frac{\pi}{2}$. The one-sided limits differ, so $G$ has a jump discontinuity at $0$ and
$G(0) = 0$ is irrelevant to them.

*The wrong sign.* $G(1) = -\arctan 1 = -\frac{\pi}{4}$ and $G(-1) = -\arctan(-1) = \frac{\pi}{4}$, so

$$G(1) - G(-1) = -\frac{\pi}{4} - \frac{\pi}{4} = -\frac{\pi}{2},$$

whereas the integrand $\frac{1}{1+x^2}$ is positive, so the integral must be positive; indeed
$\int_{-1}^{1}\frac{dx}{1+x^2} = \left[\arctan x\right]_{-1}^{1} = \frac{\pi}{2}$.

*Which hypothesis fails.* Theorem 7.4.1 requires $G$ to be an antiderivative **on $[a,b]$**, which
includes being continuous on $[-1,1]$. $G$ fails to be continuous at the interior point $0$; its
derivative exists only on $[-1,0)\cup(0,1]$. The theorem does not apply, and the correct antiderivative
$\arctan x$ (continuous on all of $\mathbb{R}$) must be used instead. $\blacksquare$

## Challenge

### Solution 33

*Strategy: differentiate the identity, which is legitimate because $f$ is continuous, and then solve the
resulting pointwise equation.*

Let $F(x) = \int_0^x f$ and $J(x) = \int_x^1 f$. The hypothesis is $F(x) = J(x)$ for all $x \in [0,1]$.

By Part 1, $F'(x) = f(x)$ for $x \in (0,1)$, with one-sided derivatives at the endpoints. By Theorem
7.8.2 (or by writing $J(x) = \int_0^1 f - \int_0^x f$), $J'(x) = -f(x)$. Differentiating the identity
$F = J$ gives

$$f(x) = -f(x) \quad \text{for } 0 < x < 1, \qquad \text{so } f(x) = 0 .$$

At the endpoints, continuity gives $f(0) = \lim_{x\to0^+}f(x) = 0$ and $f(1) = \lim_{x\to1^-}f(x) = 0$.
Hence $f \equiv 0$ on $[0,1]$.

*Verification:* if $f \equiv 0$ then both sides are $0$ for every $x$, so the hypothesis holds. Hence
the unique solution is $f \equiv 0$. $\blacksquare$

*Pitfall:* one might try to conclude only that $f$ is zero on $(0,1)$; continuity extends the result to
the endpoints, and the problem asks for all of $[0,1]$.

### Solution 34

**(a) Differentiability.** For $x>0$ the function is a composition of differentiable functions, so

$$F'(x) = 2x\sin\left(\frac{1}{x^2}\right) + x^2\cos\left(\frac{1}{x^2}\right)\cdot\left(-\frac{2}{x^3}\right)
= 2x\sin\left(\frac{1}{x^2}\right) - \frac{2}{x}\cos\left(\frac{1}{x^2}\right).$$

At $0$ use the definition:

$$\frac{F(h)-F(0)}{h} = \frac{h^2\sin\left(1/h^2\right)}{h} = h\sin\left(\frac{1}{h^2}\right),$$

and $\left|h\sin(1/h^2)\right| \le |h| \to 0$, so the quotient tends to $0$ and $F'(0) = 0$. Hence $F$ is
differentiable on $[0,1]$.

**(b) Unboundedness.** Take $x_k = \frac{1}{\sqrt{2\pi k}} \in (0,1]$ for $k \ge 1$. Then
$\frac{1}{x_k^2} = 2\pi k$, so $\sin\left(1/x_k^2\right) = 0$ and $\cos\left(1/x_k^2\right) = 1$, giving

$$F'(x_k) = 0 - \frac{2}{x_k} = -2\sqrt{2\pi k} \to -\infty .$$

So $F'$ is unbounded on $[0,1]$. The Riemann integral is defined only for bounded functions on bounded
intervals (§5.1), so $F'$ is not Riemann integrable on $[0,1]$. Consequently the Net Change Theorem, in
the form "$\int_0^1 F' = F(1)-F(0)$", has no meaning: the integral on the left does not exist. The
hypothesis $F \in C^1$ also fails, since $F'$ has no finite limit at $0$ and is not continuous there.

**(c) Extended sense.** For $0 < \varepsilon < 1$, the theorem applies on $[\varepsilon,1]$, where $F'$ is
continuous, so

$$\int_\varepsilon^1 F'(t)\,dt = F(1) - F(\varepsilon) = \sin 1 - \varepsilon^2\sin\left(\frac{1}{\varepsilon^2}\right).$$

As $\varepsilon \to 0^+$, the second term tends to $0$ because $\left|\varepsilon^2\sin(1/\varepsilon^2)\right| \le \varepsilon^2$.
Hence the **improper** integral exists and, in the improper sense,

$$\int_0^1 F'(t)\,dt = \lim_{\varepsilon\to0^+}\int_\varepsilon^1 F'(t)\,dt = \sin 1 = F(1) - F(0).$$

So the conclusion does hold in the improper sense, even though $F'$ is unbounded near $0$. What fails is
the *Riemann* integrability of $F'$, not the identity itself — a hint of the absolute-continuity
condition of §7.9(c).

### Solution 35

*Strategy: choose the test function $g = f$, converting the hypothesis into a statement about an
integral of a non-negative continuous function.*

Take $g = f$, which is continuous on $[a,b]$, so it is an admissible test function. The hypothesis gives

$$\int_a^b f(x)^2\,dx = 0 .$$

The function $f^2$ is continuous and non-negative on $[a,b]$, so Solution 28 applies and $f^2 \equiv 0$,
hence $f \equiv 0$. $\blacksquare$

*Alternative.* Suppose $f(x_0) \ne 0$. By continuity, $f^2 > f(x_0)^2/2$ on some interval of positive
length around $x_0$ inside $[a,b]$, making $\int_a^b f^2 > 0$, a contradiction.

*Remark:* the hypothesis that the identity holds for *every* continuous $g$ is what allows the choice
$g = f$. If it held only for one particular $g$, no conclusion about $f$ would follow.

### Solution 36

*Strategy: split $[0,1]$ at a point where $x^n$ becomes small. On the left piece, continuity at $0$ makes
$f(x^n)$ close to $f(0)$; on the right piece, the length shrinks to $0$.*

Let $M = \max_{[0,1]}|f|$, which is finite by the Extreme Value Theorem. Let $\varepsilon > 0$. By
continuity of $f$ at $0$ there is $\delta > 0$ such that $|u| < \delta$ implies
$|f(u) - f(0)| < \varepsilon$. We may assume $\delta < 1$.

For $n \ge 1$ put $r_n = \delta^{1/n} \in (0,1)$. Then $x^n < \delta$ exactly when $x < r_n$. Hence

$$\left|\int_0^1 f(x^n)\,dx - f(0)\right|
= \left|\int_0^1\left(f(x^n)-f(0)\right)dx\right|
\le \int_0^1\left|f(x^n)-f(0)\right|dx .$$

Split the last integral at $r_n$. On $[0,r_n)$ we have $x^n < \delta$, so the integrand is at most
$\varepsilon$ and that piece contributes at most $\varepsilon r_n \le \varepsilon$. On $[r_n,1]$ the
integrand is at most $2M$, and the length of that interval is $1-r_n$, so

$$\left|\int_0^1 f(x^n)\,dx - f(0)\right| \le \varepsilon + 2M\left(1 - \delta^{1/n}\right).$$

Since $\delta^{1/n} \to 1$ as $n \to \infty$ (for fixed $\delta \in (0,1)$), the second term tends to $0$.
Choose $N$ such that $2M\left(1-\delta^{1/n}\right) < \varepsilon$ for $n \ge N$; then the left side is
less than $2\varepsilon$ for all $n \ge N$. Since $\varepsilon > 0$ was arbitrary,

$$\lim_{n\to\infty}\int_0^1 f\left(x^n\right)dx = f(0). \;\blacksquare$$

*Check with $f \equiv 1$:* every integral equals $1 = f(0)$ ✓. *Check with $f(u) = u$:* the integral is
$\int_0^1 x^n dx = \frac{1}{n+1} \to 0 = f(0)$ ✓. *Check with $f(u) = u^2$:* the integral is
$\frac{1}{2n+1} \to 0$ ✓.

*Pitfall:* it is tempting to argue that $x^n \to 0$ for each $x \in [0,1)$ and "pass the limit inside the
integral". That step requires a theorem about interchanging limits and integrals (dominated convergence),
which is not available here; the $\varepsilon$–$\delta$ split above is the elementary substitute, and it
uses continuity of $f$ at the single point $0$, not uniform continuity on $[0,1]$.