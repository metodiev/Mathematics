# Solutions: Applications of Derivatives

> Companion to [exercises.md](exercises.md) and the [tutorial](README.md).

Each solution names the strategy, then carries out every step. Where a problem is designed around a
pitfall, the pitfall is identified explicitly. All references to theorems are to Section 8 of the
tutorial.

## Beginner

**1.** $f'(x)=2x-6=2(x-3)$, which vanishes only at $x=3$; the derivative exists everywhere, so $3$ is
the only critical point. For $x<3$ the factor $x-3<0$, so $f'<0$; for $x>3$, $f'>0$. The sign changes
from $-$ to $+$, so $f$ has a local (indeed absolute) minimum at $x=3$, with value
$f(3)=9-18+5=-4$.

**2.** $f'(x)=3x^2-12=3(x-2)(x+2)$, with zeros $x=\pm2$. The sign chart for the product of the two
factors gives:

| Interval | $(-\infty,-2)$ | $(-2,2)$ | $(2,\infty)$ |
|---|---|---|---|
| $f'$ | $+$ | $-$ | $+$ |

So $f$ is increasing on $(-\infty,-2)$ and on $(2,\infty)$, decreasing on $(-2,2)$. The sign change
$+\to-$ at $-2$ gives a local maximum $f(-2)=-8+24=16$; the change $-\to+$ at $2$ gives a local minimum
$f(2)=8-24=-16$.

**3.** $f''(x)=6x-12=6(x-2)$. Hence $f''<0$ on $(-\infty,2)$, so $f$ is concave down there, and
$f''>0$ on $(2,\infty)$, so $f$ is concave up there. The second derivative changes sign at $x=2$, so
$(2,f(2))=(2,-6)$ is an inflection point, since $f(2)=8-24+10=-6$.

**4.** $f'(x)=3x^2+6x-9=3(x^2+2x-3)=3(x+3)(x-1)$, so the critical points are $x=-3$ and $x=1$. Also
$f''(x)=6x+6$. At $x=-3$: $f''(-3)=-12<0$, so $f$ has a local maximum there, with value
$f(-3)=-27+27+27=27$. At $x=1$: $f''(1)=12>0$, so $f$ has a local minimum, with value
$f(1)=1+3-9=-5$.

**5.** $f'(x)=4x^3-12x^2=4x^2(x-3)$, so the critical points are $x=0$ (a double root of $f'$) and
$x=3$. Next, $f''(x)=12x^2-24x=12x(x-2)$. At $x=3$: $f''(3)=36>0$, so $f(3)=81-108=-27$ is a local
minimum. At $x=0$: $f''(0)=0$, so the second derivative test is *inconclusive*. Decide with the sign
chart: $4x^2\ge0$ always, so the sign of $f'$ is the sign of $x-3$ (except at $x=0$, where $f'=0$
without changing sign). Thus $f'<0$ on $(-\infty,0)$, on $(0,3)$, and $f'>0$ on $(3,\infty)$. There is
**no sign change at $0$**, so $0$ is neither a maximum nor a minimum: it is a terrace point where the
graph flattens and continues downward.

**6.** $f'(x)=2x-4=2(x-2)$, so the only critical point is $x=2$, which lies in $(0,3)$. The candidates
are the critical point and the two endpoints:

| $x$ | $0$ | $2$ | $3$ |
|---|---|---|---|
| $f(x)$ | $3$ | $-1$ | $0$ |

The absolute maximum is $3$ at $x=0$ (an endpoint); the absolute minimum is $-1$ at $x=2$.

**7.** $f'(x)=3x^2-3=3(x-1)(x+1)$, so the critical points are $\pm1$, both interior. Evaluate at all
four candidates:

| $x$ | $-2$ | $-1$ | $1$ | $2$ |
|---|---|---|---|---|
| $f(x)$ | $-2$ | $2$ | $-2$ | $2$ |

The absolute maximum is $2$, attained at $x=-1$ and $x=2$; the absolute minimum is $-2$, attained at
$x=-2$ and $x=1$. The derivative alone would have found only $\pm1$ and missed the fact that the
minimum value also occurs at the endpoint $-2$.

**8.** $f'(x)=-1/x^2$, which is never zero on $[1,4]$; moreover $f'$ exists at every point of the
interval, so there is **no critical point**. The closed interval method nevertheless applies: $f$ is
continuous on the closed bounded interval, so the extreme value theorem guarantees both extrema, and
Theorem 10 says they occur at endpoints (there being no interior candidate). Since $f'<0$, $f$ is
strictly decreasing, so the maximum is $f(1)=1$ and the minimum is $f(4)=\tfrac14$. This is the point
of the exercise: a function can attain its extrema with no critical point at all.

**9.** As $x\to0$ both $\sin 3x\to0$ and $x\to0$, so the form is $0/0$ and L'Hôpital's rule applies
(with $g(x)=x$, $g'=1\ne0$). Differentiating,

$$\lim_{x\to0}\frac{\sin 3x}{x}=\lim_{x\to0}\frac{3\cos 3x}{1}=3.$$

Equivalently, write $\dfrac{\sin 3x}{x}=3\cdot\dfrac{\sin 3x}{3x}\to3\cdot1=3$ using the standard limit
$\frac{\sin u}{u}\to1$ with $u=3x$.

**10.** The form is $0/0$. First application: $\dfrac{e^x-1}{2x}$, still $0/0$ at $0$. Second
application: $\dfrac{e^x}{2}\to\dfrac12$. Hence the limit is $\dfrac12$.

**11.** As $x\to\infty$, $\ln x\to\infty$ and $x\to\infty$: form $\infty/\infty$. One application gives
$\dfrac{1/x}{1}=\dfrac1x\to0$. Hence the limit is $0$. No second application is needed, and applying
the rule again would be an error because $\frac{1/x}{1}$ is not indeterminate.

**12.** The area is $A=\pi r^2$, so by the chain rule

$$\frac{dA}{dt}=2\pi r\frac{dr}{dt}=2\pi(5)(2)=20\pi\ \text{cm}^2/\text{s}\approx62.83\ \text{cm}^2/\text{s}.$$

The rate is positive because the circle is growing.

## Intermediate

**13.** *Domain.* $f$ is a polynomial, so the domain is $\mathbb{R}$. *Intercepts.*
$f(x)=x^2(x-3)=0$ gives $x=0$ (double root, so the graph is tangent to the axis there) and $x=3$;
$f(0)=0$. *Derivative.* $f'(x)=3x^2-6x=3x(x-2)$, zero at $0$ and $2$. Sign chart: $f'>0$ on
$(-\infty,0)\cup(2,\infty)$ and $f'<0$ on $(0,2)$. Hence $f(0)=0$ is a local maximum and $f(2)=-4$ is a
local minimum, and $f$ increases, decreases, increases. *Second derivative.* $f''(x)=6x-6=6(x-1)$, so
$f$ is concave down on $(-\infty,1)$, concave up on $(1,\infty)$, with an inflection point at
$(1,-2)$. *Ends.* As $x\to-\infty$, $f(x)\to-\infty$ (the leading term $x^3$ dominates); as
$x\to\infty$, $f(x)\to\infty$. *Sketch.* Coming from the lower left, the graph rises to a local
maximum at the origin where it is tangent to the $x$-axis, falls to $(2,-4)$, then rises through $(3,0)$
and away to $+\infty$; it is concave down until $x=1$ and concave up afterwards.

**14.** $f(x)=\sqrt x$ is continuous on $[1,4]$ and differentiable on $(1,4)$ with
$f'(x)=\dfrac{1}{2\sqrt x}$, so the MVT applies. The chord slope is

$$\frac{f(4)-f(1)}{4-1}=\frac{2-1}{3}=\frac13.$$

Setting $f'(c)=\dfrac13$ gives $\dfrac{1}{2\sqrt c}=\dfrac13$, hence $2\sqrt c=3$, $\sqrt c=\dfrac32$
and $c=\dfrac94=2.25$. This lies in $(1,4)$, as the theorem promises. (The theorem guarantees at least
one such $c$; here it is unique because $f'$ is strictly decreasing.)

**15.** Let $f(x)=x^3+3x-1$. Then $f'(x)=3x^2+3\ge3>0$ for every $x$, so by the monotonicity
criterion $f$ is strictly increasing on $\mathbb{R}$. A strictly increasing function takes each value at
most once, so $f$ has **at most one** zero.

For existence, note $f(0)=-1<0$ and $f(1)=1+3-1=3>0$. Since $f$ is continuous, the intermediate value
theorem gives a zero in $(0,1)$. Combining existence with uniqueness, the equation has exactly one real
solution. (Numerically it is $x\approx0.322$.)

**16.** *First proof.* Let $g(x)=e^x-1-x$. Then $g'(x)=e^x-1$, which is negative for $x<0$ and
positive for $x>0$. By the monotonicity criterion $g$ decreases on $(-\infty,0]$ and increases on
$[0,\infty)$, so $g$ has its absolute minimum at $x=0$, where $g(0)=0$. Hence $g(x)\ge0$, that is
$e^x\ge1+x$, with equality **only** at $x=0$.

*Second proof.* For $x>0$, the MVT on $[0,x]$ applied to $e^t$ gives $e^x-1=e^c x$ for some
$c\in(0,x)$; since $e^c>1$, $e^x-1>x$. For $x<0$, the same theorem gives $e^x-1=e^c x$ with $c<0$; now
$e^c<1$ and multiplying the inequality $e^c<1$ by the negative number $x$ reverses it, giving
$e^c x>x$, so $e^x-1>x$. At $x=0$ both sides equal $1$.

**17.** (a) The form is $0/0$; one application gives
$\displaystyle\lim_{x\to0}\frac{\sin x}{2x}=\frac12\lim_{x\to0}\frac{\sin x}{x}=\frac12$.

(b) The form is $0/0$. Differentiate numerator and denominator:

$$\lim_{x\to0}\frac{\tan x-x}{x^3}=\lim_{x\to0}\frac{\sec^2x-1}{3x^2}.$$

Using $\sec^2x-1=\tan^2x$ and the standard limit $\frac{\tan x}{x}\to1$,

$$\lim_{x\to0}\frac{\tan^2x}{3x^2}=\frac13\left(\lim_{x\to0}\frac{\tan x}{x}\right)^2=\frac13.$$

(A second application of L'Hôpital would also work: $\frac{2\sec^2x\tan x}{6x}=\frac13\sec^2x\cdot\frac{\tan x}{x}\to\frac13$.)

**18.** For $x\ne0$ the quotient is $\dfrac{x^2\sin(1/x)}{x}=x\sin(1/x)$, so the limit is $0$ by the
squeeze theorem, since $0\le\lvert x\sin(1/x)\rvert\le\lvert x\rvert\to0$.

The derivative, however, is

$$f'(x)=2x\sin\frac1x+x^2\cos\frac1x\cdot\left(-\frac1{x^2}\right)=2x\sin\frac1x-\cos\frac1x .$$

As $x\to0$ the first term tends to $0$, but $\cos(1/x)$ oscillates between $-1$ and $1$ and has no limit.
Hence $\lim_{x\to0}f'(x)$ does not exist, and with $g(x)=x$ (so $g'=1$) the ratio $f'/g'$ has no limit.
L'Hôpital's rule requires that limit to exist, so it **cannot** be applied; the rule is silent, and the
squeeze argument settles the problem. Note also that $f$ *is* differentiable at $0$, with
$f'(0)=\lim_{h\to0}h\sin(1/h)=0$; the failure is that $f'$ is not continuous at $0$.

**19.** Let $x$ be the distance of the foot from the wall and $y$ the height of the top, so that
$x^2+y^2=100$. Differentiating with respect to $t$,

$$2x\dot x+2y\dot y=0\quad\Longrightarrow\quad \dot x=-\frac{y}{x}\dot y .$$

When $y=6$ we have $x=\sqrt{100-36}=8$, and $\dot y=-1$ m/s (the top descends). Therefore
$\dot x=-\dfrac{6}{8}(-1)=0.75$ m/s: the foot moves away from the wall at $0.75$ m/s.

**20.** Let $h$ be the depth and $r$ the radius of the water surface. By similar triangles
$\dfrac{r}{h}=\dfrac{2}{4}$, so $r=\dfrac h2$. The volume is

$$V=\frac13\pi r^2h=\frac13\pi\cdot\frac{h^2}{4}\cdot h=\frac{\pi h^3}{12}.$$

Differentiating with respect to $t$, $\dfrac{dV}{dt}=\dfrac{\pi h^2}{4}\dfrac{dh}{dt}$, hence

$$\frac{dh}{dt}=\frac{4}{\pi h^2}\frac{dV}{dt}=\frac{4\cdot2}{\pi\cdot4}=\frac{2}{\pi}\approx0.637\ \text{m/min}$$

when $h=2$. The level rises more slowly as the tank widens, which is visible in the factor $1/h^2$.

**21.** Let $x$ be the length of each side perpendicular to the river and $y$ the length parallel to it.
The fencing constraint is $2x+y=100$, so $y=100-2x$ and, since lengths are positive, $0<x<50$. The area
is

$$A(x)=x(100-2x)=100x-2x^2,\qquad A'(x)=100-4x .$$

$A'=0$ gives $x=25$, hence $y=50$. Since $A''=-4<0$, this is a local maximum; and since $A(0)=A(50)=0$
while $A(25)=25\cdot50=1250$, it is the global maximum on the closed feasible interval. The pen should
be $25$ m deep and $50$ m wide, with area $1250\ \text{m}^2$. Note that the optimal rectangle is twice as
long as it is deep — the river replaces one of the two long fences.

**22.** Let $2x$ and $2y$ be the side lengths, so $x^2+y^2=25$ with $x,y>0$. The area is
$A=4xy=4x\sqrt{25-x^2}$ for $0<x<5$. Differentiating,

$$A'(x)=4\sqrt{25-x^2}+4x\cdot\frac{-x}{\sqrt{25-x^2}}=\frac{4(25-x^2)-4x^2}{\sqrt{25-x^2}}=\frac{4(25-2x^2)}{\sqrt{25-x^2}}.$$

$A'=0$ when $x^2=\dfrac{25}{2}$, i.e. $x=y=\dfrac{5}{\sqrt2}$. Then $A=4\cdot\dfrac{25}{2}=50$. As
$x\to0^+$ or $x\to5^-$ the area tends to $0$, so this interior critical point is the global maximum. The
optimal rectangle is the square with side $2x=5\sqrt2$ and area $50$.

## Advanced

**23.** Let $x$ be the base side and $h$ the height. The volume constraint $x^2h=8$ gives
$h=8/x^2$, and the cost is

$$C(x)=2x^2+4xh=2x^2+4x\cdot\frac{8}{x^2}=2x^2+\frac{32}{x},\qquad x>0 .$$

Differentiating,

$$C'(x)=4x-\frac{32}{x^2}=\frac{4x^3-32}{x^2},$$

so $C'=0$ exactly when $x^3=8$, that is $x=2$. Then $h=\dfrac{8}{4}=2$ and $C=2(4)+4(2)(2)=8+16=24$.
Since $C''(x)=4+\dfrac{64}{x^3}>0$ for $x>0$, the critical point is a local minimum, and because
$C(x)\to+\infty$ as $x\to0^+$ and as $x\to+\infty$, it is the global minimum. The optimal box is a
$2\times2\times2$ cube with cost $24$. (Equal costs per unit area force equal dimensions; contrast
Example 7 of the tutorial, where the open top broke the symmetry.)

**24.** A point on the parabola has the form $(x,x^2)$, so the squared distance to $(0,3)$ is

$$D(x)=x^2+(x^2-3)^2 .$$

With $u=x^2\ge0$, $D=u+(u-3)^2=u^2-5u+9$, a parabola in $u$ with vertex at $u=\dfrac52$; since
$\dfrac52\ge0$ this value is attainable. Then $D=\dfrac{25}{4}-\dfrac{25}{2}+9=\dfrac{25-50+36}{4}=\dfrac{11}{4}$,
so the distance is $\dfrac{\sqrt{11}}{2}\approx1.658$. The closest points are
$\left(\pm\sqrt{\tfrac52},\tfrac52\right)=(\pm1.5811,\,2.5)$.

Check by differentiating in $x$: $D'(x)=2x+2(x^2-3)(2x)=2x(2x^2-5)$, whose zeros are $x=0$ and
$x=\pm\sqrt{5/2}$. At $x=0$, $D=9$; at $x^2=\tfrac52$, $D=\tfrac{11}{4}=2.75$. So $x=0$ is a local
maximum of $D$ and the other two points give the global minimum.

**25.** Let $x$ be the horizontal distance from the station and $s$ the straight-line distance, so
$s^2=x^2+9$ (altitude $3$ km). Then

$$2s\dot s=2x\dot x\quad\Longrightarrow\quad \dot s=\frac{x}{s}\dot x .$$

When $x=4$ we have $s=\sqrt{16+9}=5$, and $\dot x=400$ km/h, so $\dot s=\dfrac45(400)=320$ km/h. The
sign is positive: the aircraft is flying away from the station, so the distance is increasing at
$320$ km/h. (Had it been approaching, $\dot x=-400$ and the distance would be decreasing at the same
rate.)

**26.** Revenue is $R(q)=qp=120q-3q^2$, so

$$P(q)=R(q)-C(q)=120q-3q^2-30q-500=-3q^2+90q-500 .$$

Then $P'(q)=-6q+90$, which vanishes at $q=15$, and $P''=-6<0$, so this is a local maximum. The feasible
interval is $[0,40]$; the endpoint values are $P(0)=-500$ and $P(40)=-4800+3600-500=-1700$, both smaller
than $P(15)=-675+1350-500=175$. Hence $q=15$ is optimal, with price $p=120-45=75$ and profit
$\$175$.

*Marginal check.* $R'(q)=120-6q$ and $C'(q)=30$. At $q=15$, $R'(15)=120-90=30=C'(15)$, so marginal
revenue equals marginal cost, as it must at an interior optimum. Note the fixed cost $500$ does not
affect the optimal quantity (its derivative is zero) but does determine whether the firm is profitable.

**27.** Let $a\le x_1<x_2\le b$. The function $f$ is continuous on $[x_1,x_2]$ and differentiable on
$(x_1,x_2)$, because those properties hold on the larger interval $[a,b]$; hence the mean value theorem
applies on $[x_1,x_2]$ and supplies $c\in(x_1,x_2)$ with

$$f(x_2)-f(x_1)=f'(c)(x_2-x_1).$$

By hypothesis $f'(c)>0$, and $x_2-x_1>0$, so $f(x_2)-f(x_1)>0$, i.e. $f(x_1)<f(x_2)$. Since $x_1<x_2$
were arbitrary, $f$ is strictly increasing on $[a,b]$. $\blacksquare$

*Remark.* Continuity at the endpoints is used to apply the MVT on $[x_1,x_2]$ when $x_1=a$ or $x_2=b$;
differentiability is needed only on the open interval. If the hypothesis is weakened to $f'\ge0$, only
non-strict increase is guaranteed (a constant function attains equality throughout), although strict
increase may still occur, as $f(x)=x^3$ shows.

**28.** Let $x_1<x_2$ be any two points of $I$. Since $f$ is differentiable on $I$, it is continuous on
$[x_1,x_2]$ and differentiable on $(x_1,x_2)$, so the MVT gives $c\in(x_1,x_2)$ with

$$f(x_2)-f(x_1)=f'(c)(x_2-x_1)=0\cdot(x_2-x_1)=0 .$$

Hence $f(x_1)=f(x_2)$ for all $x_1<x_2$ in $I$, which is precisely the statement that $f$ is constant
on $I$. $\blacksquare$

For the deduction, put $h=f-g$. Then $h'=f'-g'=0$ on $I$, so $h$ is constant, i.e. $f-g=C$ on $I$.
This is the general form of the "$+C$" that appears in every antiderivative.

**29.** Let $a<b$ (the case $a=b$ is trivial and the case $a>b$ follows by symmetry). The function
$\sin$ is continuous and differentiable everywhere, so the MVT on $[a,b]$ gives $c\in(a,b)$ with

$$\sin b-\sin a=\cos c\,(b-a).$$

Taking absolute values, $\lvert\sin b-\sin a\rvert=\lvert\cos c\rvert\,\lvert b-a\rvert\le\lvert b-a\rvert$,
because $\lvert\cos c\rvert\le1$. $\blacksquare$

For the deduction, take $a=0$ and $b=x>0$: the inequality gives $\lvert\sin x\rvert\le x$, hence
$\sin x\le x$. Strictness: if $x>1$ then $\sin x\le1<x$; if $0<x\le1$, the MVT supplies $c\in(0,x)$ with
$\sin x=x\cos c$, and $c<1<\dfrac{\pi}{2}$, so $\cos c<1$ and therefore $\sin x<x$. In both cases
$\sin x<x$ for $x>0$.

**30.** (a) Write $x\ln x=\dfrac{\ln x}{1/x}$. As $x\to0^+$, $\ln x\to-\infty$ and $1/x\to+\infty$, so
the form is $-\infty/\infty$ and L'Hôpital applies:

$$\lim_{x\to0^+}\frac{\ln x}{1/x}=\lim_{x\to0^+}\frac{1/x}{-1/x^2}=\lim_{x\to0^+}(-x)=0 .$$

(b) The form is $\infty-\infty$, which is not covered by the rule. Combine over a common denominator:

$$\frac{1}{\sin x}-\frac{1}{x}=\frac{x-\sin x}{x\sin x},$$

a $0/0$ form. Differentiating numerator and denominator gives
$\dfrac{1-\cos x}{\sin x+x\cos x}$, still $0/0$ at $0$. A second application gives

$$\frac{\sin x}{\cos x+\cos x-x\sin x}=\frac{\sin x}{2\cos x-x\sin x}\longrightarrow\frac{0}{2}=0 .$$

Hence the limit is $0$. (Equivalently, $x-\sin x=O(x^3)$ while $x\sin x=O(x^2)$, so the quotient is
$O(x)$.)

## Challenge

**31.** (a) *Failure of continuity at an endpoint.* Define $f(x)=x$ for $0\le x<1$ and $f(1)=0$. Then
$f(0)=0=f(1)$, so the hypothesis $f(a)=f(b)$ holds, and $f$ is differentiable on $(0,1)$ with
$f'(x)=1$ everywhere. But $f$ is not continuous at $1$ (the left limit is $1$, the value is $0$), and
there is no $c\in(0,1)$ with $f'(c)=0$. Rolle's theorem genuinely needs continuity on the closed
interval.

(b) *Failure of differentiability at an interior point.* Take $f(x)=\lvert x\rvert$ on $[-1,1]$. It is
continuous and $f(-1)=1=f(1)$, but $f$ is not differentiable at $0$. For $x>0$, $f'(x)=1$; for $x<0$,
$f'(x)=-1$; at $0$ the derivative does not exist. So there is no interior point with $f'=0$. This does
not contradict Rolle's theorem, whose hypothesis includes differentiability on the whole open interval.

(c) *Failure of continuity at the right endpoint for the MVT.* Define $f(x)=0$ for $0\le x<1$ and
$f(1)=1$. It is differentiable on $(0,1)$ with $f'=0$ there, but the chord slope is
$\dfrac{f(1)-f(0)}{1-0}=1$, so the MVT would require $f'(c)=1$, which never happens. Again the missing
hypothesis — continuity at $1$ — is exactly what the theorem needs.

**32.** Suppose, for contradiction, that $f$ has two distinct zeros $u<v$ in $(a,b)$. Then $f$ is
continuous on $[u,v]$ and differentiable on $(u,v)$, and $f(u)=f(v)=0$; Rolle's theorem produces
$c\in(u,v)$ with $f'(c)=0$, contradicting the hypothesis $f'\ne0$ everywhere on $(a,b)$. Hence at most
one zero exists. $\blacksquare$

The hypothesis does not force a zero. On $I=(0,\infty)$, $f(x)=e^x$ satisfies $f'(x)=e^x\ne0$ for all
$x$, and $e^x>0$ never vanishes. On $\mathbb{R}$ the same example works. Another is $f(x)=1/x$ on
$(0,\infty)$, with $f'(x)=-1/x^2\ne0$.

**33.** Define $g(x)=\dfrac{f(x)}{e^x}$, which is defined and differentiable on $I$ because $e^x\ne0$.
By the quotient rule,

$$g'(x)=\frac{f'(x)e^x-f(x)e^x}{(e^x)^2}=\frac{(f(x)-f(x))e^x}{e^{2x}}=0 .$$

By the zero-derivative theorem (Theorem 5), $g$ is constant on $I$: $g(x)=C$. Therefore
$f(x)=Ce^x$ for all $x\in I$. $\blacksquare$

*Remark.* The constant is $C=f(0)$ when $0\in I$. This is the uniqueness half of the theory of the
differential equation $y'=y$; existence is exhibited by $f(x)=e^x$ itself.

**34.** Here $f'(x)=3x^2$, so the iteration is

$$x_{n+1}=x_n-\frac{x_n^3-2}{3x_n^2}=\frac{3x_n^3-x_n^3+2}{3x_n^2}=\frac{2x_n^3+2}{3x_n^2}=\frac23\left(x_n+\frac{1}{x_n^2}\right).$$

From $x_0=1$:

* $x_1=\dfrac23(1+1)=\dfrac43=1.333333\ldots$;
* $x_2=\dfrac23\left(\dfrac43+\dfrac{9}{16}\right)=\dfrac23\cdot\dfrac{64+27}{48}=\dfrac23\cdot\dfrac{91}{48}=\dfrac{91}{72}=1.263888\ldots$;
* $x_3=\dfrac23\left(\dfrac{91}{72}+\dfrac{5184}{8281}\right)$. With $\dfrac{91}{72}\approx1.263889$ and
  $\dfrac{5184}{8281}\approx0.626012$, the bracket is $1.889901$, so $x_3\approx1.259934$.

Since $r=\sqrt[3]{2}\approx1.259921$, the errors are

| $n$ | $x_n$ | $e_n=x_n-r$ | $e_n^2$ | $e_{n+1}/e_n^2$ |
|---|---|---|---|---|
| $1$ | $1.333333$ | $7.34\times10^{-2}$ | $5.39\times10^{-3}$ | $0.736$ |
| $2$ | $1.263889$ | $3.97\times10^{-3}$ | $1.57\times10^{-5}$ | $0.80$ |
| $3$ | $1.259934$ | $1.3\times10^{-5}$ | — | — |

The predicted constant is
$\dfrac{f''(r)}{2f'(r)}=\dfrac{6r}{2\cdot3r^2}=\dfrac1r\approx0.7937$, and the last ratio in the table
agrees with it to two digits; the first is slightly smaller because $x_1$ is not yet close to $r$ and
the asymptotic formula is only a limit statement. The number of correct digits grows from about $1$ to
$3$ to $5$, which is the quadratic convergence described in Section 7.12. Note that every $x_n$ is rational
while $r$ is irrational: the convergence is genuine but never exact at a finite step.

**35.** Let $x$ be the distance downstream from the point on the far bank directly opposite $A$, with
$0\le x\le6$. The underwater length is $\sqrt{2^2+x^2}$ and the overland length is $6-x$, so the cost
is

$$C(x)=5\sqrt{4+x^2}+3(6-x).$$

Differentiating,

$$C'(x)=\frac{5x}{\sqrt{4+x^2}}-3 .$$

Setting $C'=0$: $5x=3\sqrt{4+x^2}$, so $25x^2=9(4+x^2)$, $16x^2=36$, $x^2=\dfrac94$, $x=\dfrac32$.
Since $C''(x)=\dfrac{5\cdot4}{(4+x^2)^{3/2}}>0$, this critical point is a minimum. Compare the three
candidates:

| $x$ | $0$ | $1.5$ | $6$ |
|---|---|---|---|
| $C(x)$ | $5\cdot2+18=28$ | $5\cdot2.5+13.5=26$ | $5\sqrt{40}\approx31.62$ |

The minimum cost is $26$ units, attained by coming ashore $1.5$ km downstream of the opposite point. The
two extreme strategies (straight across then overland, or straight to the destination) cost $28$ and
$31.62$, so the optimum genuinely lies in the interior. The optimum is characterised by
$\cos\theta=\dfrac35$, where $\theta$ is the angle between the underwater pipe and the bank: the ratio of
the two costs equals the cosine of the entry angle, which is Snell's law in disguise.

**36.** Let $x_1<x_2<x_3$ be the three zeros. Since $f$ is twice differentiable it is continuous and
differentiable everywhere on the interval, so Rolle's theorem applies on $[x_1,x_2]$ and on
$[x_2,x_3]$. It gives $c_1\in(x_1,x_2)$ and $c_2\in(x_2,x_3)$ with $f'(c_1)=0=f'(c_2)$. Now $c_1<c_2$,
and $f'$ is differentiable (because $f$ is twice differentiable), hence continuous on $[c_1,c_2]$ and
differentiable on $(c_1,c_2)$. Rolle's theorem applied to $f'$ gives $c\in(c_1,c_2)$ with
$f''(c)=0$. $\blacksquare$

The converse fails: $f(x)=x^3$ is twice differentiable on $\mathbb{R}$, has exactly one zero (at $0$),
and $f''(x)=6x$ vanishes at $0$. So $f''$ can have a zero without $f$ having three zeros. What the
theorem really says is that *three* zeros of $f$ force at least *one* zero of $f''$ — a counting
statement in the spirit of Rolle's theorem rather than an equivalence.
