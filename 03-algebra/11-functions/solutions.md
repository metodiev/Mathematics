# Functions — Solutions

> [Tutorial](README.md) · [Exercises](exercises.md) · 37 worked solutions

Each solution states the strategy, carries out every significant step, and checks the result — by
substitution, by a numerical spot check, or by verifying that the two compositions return the identity.
Where a problem admits a second approach, that approach is indicated.

## Beginner

**1.**

Substitute the whole input for $x$:

$$\begin{aligned}
f(0) &= 3(0)^2-2(0)+1 = 1,\\
f(-1) &= 3(-1)^2-2(-1)+1 = 3+2+1 = 6,\\
f(2) &= 3(4)-4+1 = 9,\\
f(a) &= 3a^2-2a+1.
\end{aligned}$$

The last line is the point of the exercise: $f(a)$ is not a number but the same rule applied to the
symbol $a$. In particular $f(-1)$ uses $(-1)^2=1$, not $-1$.

**2.**

$$\begin{aligned}
g(0) &= \frac{0+1}{0-4} = -\frac14,\\
g(5) &= \frac{5+1}{5-4} = 6,\\
g(-1) &= \frac{-1+1}{-1-4} = \frac{0}{-5} = 0.
\end{aligned}$$

A zero numerator with a nonzero denominator gives $0$, so $g(-1)=0$ is legitimate. The function is
undefined exactly where the denominator vanishes: $x-4=0$, i.e. $x=4$. Note that $g(4)$ would require
division by zero; nothing can be salvaged by cancelling, since the numerator $x+1$ is not zero at
$x=4$.

**3.**

The square root of a real number exists only when the number under the root is non-negative, so we
require

$$x-5 \ge 0 \quad\Longrightarrow\quad x \ge 5 .$$

Hence $\operatorname{dom} f = [5,\infty)$. The endpoint $5$ is included because $\sqrt{0}=0$ is a
legitimate output; writing $(5,\infty)$ would wrongly discard the value $f(5)=0$.

**4.**

The only restriction is the denominator:

$$x^2-9 \ne 0 \quad\Longrightarrow\quad x^2 \ne 9 \quad\Longrightarrow\quad x \ne 3 \text{ and }
x \ne -3 .$$

Hence

$$\operatorname{dom} h = \mathbb{R}\setminus\{-3,3\} = (-\infty,-3)\cup(-3,3)\cup(3,\infty).$$

At $x=3$ the numerator is $6 \ne 0$, so the graph has a vertical asymptote there; there is no
cancellation.

**5.**

**Domain.** $x^2-4$ is a polynomial, so it is defined for every real $x$:
$\operatorname{dom} f = \mathbb{R} = (-\infty,\infty)$.

**Range.** For every real $x$, $x^2 \ge 0$, so $x^2-4 \ge -4$. The value $-4$ is attained at $x=0$.
Every value $y \ge -4$ is attained, because $x^2 = y+4$ has the real solution $x=\sqrt{y+4}$ when
$y \ge -4$. Therefore

$$\operatorname{ran} f = [-4,\infty).$$

**Check.** $f(0)=-4$, $f(3)=5$, $f(-3)=5$: the graph is a parabola opening upward with vertex
$(0,-4)$, consistent with both the range and the failure of injectivity.

**6.**

No. Solve for $y$:

$$y^2 = x \quad\Longrightarrow\quad y = \pm\sqrt{x}\quad (\text{for } x \ge 0).$$

For instance $x=4$ gives both $y=2$ and $y=-2$. Geometrically, the curve is the parabola opening to the
right, and the vertical line $x=4$ meets it at $(4,2)$ and $(4,-2)$ — two points, so the vertical line
test fails. For $x<0$ the curve has no points at all with real $y$, so those $x$ are outside any
possible domain.

The equation does define $x$ as a function of $y$ ($x=y^2$): the roles are exchanged, and that function
is one-to-one only on a restricted domain.

**7.**

Yes. Two arguments, both worth knowing.

*Analytic.* Suppose $x_1^3=x_2^3$. Then

$$x_1^3-x_2^3 = (x_1-x_2)(x_1^2+x_1x_2+x_2^2) = 0 .$$

The second factor is non-negative, since

$$x_1^2+x_1x_2+x_2^2 = \left(x_1+\tfrac{x_2}{2}\right)^2 + \tfrac34 x_2^2 \ge 0,$$

and it vanishes only when $x_1=x_2=0$. In that case $x_1=x_2$ anyway. So $x_1=x_2$.

*Monotonicity.* The function $x\mapsto x^3$ is strictly increasing (Solution 31 proves this), and a
strictly increasing function is one-to-one.

*Geometric.* Every horizontal line $y=c$ meets the curve $y=x^3$ exactly once, at $x=\sqrt[3]{c}$.

**8.**

Compute $f(-x)$:

$$f(-x) = (-x)^4 - 3(-x)^2 = x^4 - 3x^2 = f(x).$$

Since $f(-x)=f(x)$ for every $x$, and the domain $\mathbb{R}$ is symmetric about $0$, the function is
**even**. Its graph is symmetric about the $y$-axis. (It is not odd: $f(-1)=1-3=-2 \ne -f(1)$ is
actually equal here, but $f(-2)=16-12=4$ while $-f(2)=-4$, so oddness fails.)

**9.**

$$f(-x) = (-x)^3 + (-x) = -x^3 - x = -(x^3+x) = -f(x).$$

Hence $f$ is **odd**, and its graph is symmetric about the origin. Consequently $f(0)=0$, which is
consistent with $f(0)=0$.

**10.**

Composition applies the right-hand function first.

$$(f\circ g)(x) = f(g(x)) = f(x^2) = 2x^2-5,$$

$$(g\circ f)(x) = g(f(x)) = g(2x-5) = (2x-5)^2 = 4x^2-20x+25.$$

The two results differ: $f\circ g \ne g\circ f$. Check with $x=1$: $(f\circ g)(1) = -3$ but
$(g\circ f)(1) = 9$. Both functions are defined for all real $x$, so both domains are $\mathbb{R}$.

**11.**

Write $y=4x-7$ and solve for $x$:

$$\begin{aligned}
y &= 4x-7\\
y+7 &= 4x\\
x &= \frac{y+7}{4}.
\end{aligned}$$

Hence $f^{-1}(x) = \dfrac{x+7}{4}$.

**Verification of both directions.**

$$f\big(f^{-1}(x)\big) = 4\cdot\frac{x+7}{4}-7 = (x+7)-7 = x,$$

$$f^{-1}\big(f(x)\big) = \frac{(4x-7)+7}{4} = \frac{4x}{4} = x.$$

Since $f$ is linear with nonzero slope, it is a bijection $\mathbb{R}\to\mathbb{R}$, so the inverse is
defined on all of $\mathbb{R}$.

**12.**

**Values.**

$$C(32) = \tfrac59(32-32) = 0, \qquad C(212) = \tfrac59(212-32) = \tfrac59\cdot 180 = 100.$$

These are the familiar freezing and boiling points of water.

**Inverse.** Solve $y = \tfrac59(x-32)$ for $x$:

$$\begin{aligned}
\tfrac95 y &= x-32\\
x &= \tfrac95 y + 32 .
\end{aligned}$$

Hence $C^{-1}(x) = \tfrac95 x + 32$, a linear function with positive slope $\tfrac95 = 1.8$: each
additional Celsius degree is $1.8$ Fahrenheit degrees.

**Application.** $37\,^\circ\text{C}$ is

$$C^{-1}(37) = \tfrac95\cdot 37 + 32 = 66.6 + 32 = 98.6\,^\circ\text{F},$$

the standard human body temperature. Check: $C(98.6) = \tfrac59(66.6) = 37$. ✓

## Intermediate

**13.**

**Domain.** We require $16-x^2 \ge 0$, i.e. $x^2 \le 16$, i.e. $\lvert x\rvert \le 4$:

$$\operatorname{dom} g = [-4,4].$$

**Range.** For $x \in [-4,4]$ we have $0 \le x^2 \le 16$, so $0 \le 16-x^2 \le 16$, and therefore
$0 \le \sqrt{16-x^2} \le 4$. Each value $c \in [0,4]$ is attained: take $x = \sqrt{16-c^2}$, which
lies in $[0,4]$. Hence

$$\operatorname{ran} g = [0,4].$$

**Check.** $g(0)=4$ (maximum), $g(\pm4)=0$ (minimum), $g(\pm3)=\sqrt7\approx 2.65$.

**14.**

Two conditions must hold simultaneously.

* The radicand must be non-negative: $x+3 \ge 0$, i.e. $x \ge -3$.
* The denominator must not vanish: $x-2 \ne 0$, i.e. $x \ne 2$.

Intersecting,

$$\operatorname{dom} f = [-3,2)\cup(2,\infty).$$

The left endpoint $-3$ is included because $\sqrt{0}/\!(-5) = 0$ is defined. Had the numerator been
$\sqrt{x+3}-5$, the extra condition $x+3 \ne 25$ would also appear — always check numerators, not only
denominators.

**15.**

$$\begin{aligned}
f(x+h) &= (x+h)^2 + 5(x+h) = x^2 + 2xh + h^2 + 5x + 5h,\\
f(x+h)-f(x) &= \big(x^2+2xh+h^2+5x+5h\big) - \big(x^2+5x\big) = 2xh + h^2 + 5h,\\
\frac{f(x+h)-f(x)}{h} &= \frac{h(2x+h+5)}{h} = 2x + h + 5 \qquad (h \ne 0).
\end{aligned}$$

**Check with numbers.** Let $x=1$, $h=0.1$: $f(1.1)-f(1) = (1.21+5.5)-(1+5) = 6.71-6 = 0.71$, and
$0.71/0.1 = 7.1$, while $2(1)+0.1+5 = 7.1$. ✓

The factorisation is the essential step; cancelling $h$ before factoring is the usual error.

**16.**

$$\operatorname{ARC}_{[1,3]}(f) = \frac{f(3)-f(1)}{3-1} = \frac{27-1}{2} = 13 .$$

**Interpretation.** Between $x=1$ and $x=3$ the function grows on average by $13$ units per unit of
$x$. This is the slope of the secant line through $(1,1)$ and $(3,27)$:

$$m = \frac{27-1}{3-1} = 13 .$$

For comparison, the average rate on $[1,2]$ is $7$, and on $[1,1.1]$ it is $3.31$; the averages
decrease toward $3$, the slope of the tangent at $x=1$. A nonlinear function has no single rate of
change.

**17.**

**Transformations, in order.**

1. Shift **right** $3$: $y=(x-3)^2$ (inside change acts in reverse).
2. Stretch vertically by a factor of $2$: $y=2(x-3)^2$.
3. Reflect in the $x$-axis: $y=-2(x-3)^2$ (the factor $-2$ combines steps 2 and 3).
4. Shift **up** $1$: $y=-2(x-3)^2+1$.

**Readings.**

* Vertex: the parent parabola has vertex $(0,0)$; the point map is $(t,t^2)\mapsto(t+3,-2t^2+1)$, so
  the vertex moves to $(3,1)$.
* Axis of symmetry: $x=3$.
* Domain: $\mathbb{R}$ — no restriction is introduced.
* Range: since $(x-3)^2 \ge 0$, we have $-2(x-3)^2 \le 0$, so $y \le 1$, with equality at $x=3$. Hence
  $\operatorname{ran} = (-\infty,1]$.

**Check.** At $x=3$, $y=1$ ✓. At $x=4$, $y=-2+1=-1$; at $x=2$, $y=-1$ — symmetric about $x=3$ ✓. At
$x=0$, $y=-18+1=-17$, a steep downward value consistent with the vertical stretch by $2$.

**18.**

**Rewrite the inside.** $4-x = -(x-4)$, so

$$y = \tfrac12\sqrt{4-x} = \tfrac12\sqrt{-(x-4)} .$$

**Transformations from $y=\sqrt{x}$.**

1. Replace $x$ by $-x$: $y=\sqrt{-x}$ — reflect in the $y$-axis.
2. Replace $x$ by $x-4$: $y=\sqrt{-(x-4)}$ — shift **right** $4$.
3. Multiply by $\tfrac12$: vertical compression by a factor of $2$ (each height is halved).

**Domain.** $\sqrt{4-x}$ requires $4-x \ge 0$, i.e. $x \le 4$:
$\operatorname{dom} = (-\infty,4]$.

**Range.** $\sqrt{4-x} \ge 0$ and it takes every non-negative value (as $x$ runs over $(-\infty,4]$, the
radicand runs over $[0,\infty)$). Multiplying by $\tfrac12$ gives
$\operatorname{ran} = [0,\infty)$.

**Check.** $x=4$: $y=0$ ✓. $x=0$: $y=\tfrac12\sqrt4 = 1$. $x=-5$: $y=\tfrac12\cdot 3 = 1.5$ — the graph
rises without bound as $x\to-\infty$, as expected from the $y$-axis reflection.

**19.**

**First order.**

$$(f\circ g)(x) = f(x+2) = \sqrt{x+2}.$$

Domain: $g$ is defined everywhere, and $f$ requires its input to be non-negative, so $x+2 \ge 0$:

$$\operatorname{dom}(f\circ g) = [-2,\infty).$$

**Second order.**

$$(g\circ f)(x) = g(\sqrt{x}) = \sqrt{x}+2 .$$

Domain: $f$ requires $x \ge 0$; then $\sqrt{x}+2$ is automatically defined. So
$\operatorname{dom}(g\circ f) = [0,\infty)$.

The formulas differ by the position of the $2$, and the domains differ by the position of the shift.
Note also that the range of $f\circ g$ is $[0,\infty)$ while the range of $g\circ f$ is $[2,\infty)$.

**20.**

**First order.**

$$(f\circ g)(x) = f(x^2-4) = \frac{1}{(x^2-4)-2} = \frac{1}{x^2-6}.$$

Conditions: $x \in \operatorname{dom} g = \mathbb{R}$ and $g(x) \in \operatorname{dom} f$, i.e.
$x^2-4 \ne 2$, i.e. $x^2 \ne 6$. Hence

$$\operatorname{dom}(f\circ g) = \mathbb{R}\setminus\{-\sqrt6,\sqrt6\}
= (-\infty,-\sqrt6)\cup(-\sqrt6,\sqrt6)\cup(\sqrt6,\infty).$$

The formula $\dfrac{1}{x^2-6}$ shows the same exclusions, which is a useful cross-check — but only
because no cancellation occurred.

**Second order.**

$$(g\circ f)(x) = \left(\frac{1}{x-2}\right)^2 - 4 = \frac{1}{(x-2)^2}-4 .$$

Conditions: $x \ne 2$ (from $\operatorname{dom} f$) and $\dfrac{1}{x-2}$ must lie in
$\operatorname{dom} g = \mathbb{R}$, which is automatic. Hence $\operatorname{dom}(g\circ f) =
\mathbb{R}\setminus\{2\}$.

**Check.** With $x=0$: $(f\circ g)(0) = -1/6$ and $(g\circ f)(0) = 1/4-4 = -15/4$. Both are defined, as
predicted.

**21.**

**Inverse.** Write $y=\dfrac{3x-1}{x+2}$ and solve for $x$:

$$\begin{aligned}
y(x+2) &= 3x-1\\
xy+2y &= 3x-1\\
xy-3x &= -1-2y\\
x(y-3) &= -(1+2y)\\
x &= \frac{2y+1}{3-y}.
\end{aligned}$$

Therefore

$$f^{-1}(x) = \frac{2x+1}{3-x}.$$

**Domains and ranges.**

* $\operatorname{dom} f = \mathbb{R}\setminus\{-2\}$, because $x+2 \ne 0$.
* The solved equation shows that $x$ exists for every $y \ne 3$; also $f$ can never equal $3$, since
  $\dfrac{3x-1}{x+2}=3$ would give $3x-1=3x+6$, i.e. $-1=6$, impossible. So
  $\operatorname{ran} f = \mathbb{R}\setminus\{3\}$.
* Consequently $\operatorname{dom} f^{-1} = \mathbb{R}\setminus\{3\}$ and
  $\operatorname{ran} f^{-1} = \mathbb{R}\setminus\{-2\}$, as domain and range swap.

**Check.** $f(0)=-\tfrac12$; then $f^{-1}\!\left(-\tfrac12\right) = \dfrac{-1+1}{3+\tfrac12}=0$ ✓. Also
$f(1)=\tfrac23$ and $f^{-1}\!\left(\tfrac23\right) = \dfrac{\tfrac43+1}{3-\tfrac23} =
\dfrac{7/3}{7/3} = 1$ ✓.

**22.**

**Values.**

* $f(-3)$: $-3<0$, so use $x+2$: $f(-3) = -1$.
* $f(0)$: $0 \le 0 \le 2$, so use $x^2$: $f(0)=0$.
* $f(2)$: $2$ is in $[0,2]$, so use $x^2$: $f(2)=4$.
* $f(4)$: $4>2$, so use $5$: $f(4)=5$.

**Range, piece by piece.**

* On $x<0$: $x+2$ takes the values $(-\infty,2)$.
* On $0 \le x \le 2$: $x^2$ takes the values $[0,4]$.
* On $x>2$: the constant $5$ gives $\{5\}$.

The range is the union:

$$\operatorname{ran} f = (-\infty,2)\cup[0,4]\cup\{5\} = (-\infty,4]\cup\{5\}.$$

**Remarks.** The value $4$ is attained (at $x=2$), the value $5$ is attained (for every $x>2$), but no
value strictly between $4$ and $5$ is attained, and no value greater than $5$. The graph jumps from
height $4$ at $x=2$ to height $5$ for $x>2$.

**23.**

Use the decomposition of Proposition 8.9. First compute $f(-x)$:

$$f(-x) = (-x)^3-2(-x)^2+(-x)-5 = -x^3-2x^2-x-5 .$$

**Even part.**

$$E(x) = \frac{f(x)+f(-x)}{2} = \frac{\big(x^3-2x^2+x-5\big)+\big(-x^3-2x^2-x-5\big)}{2} =
\frac{-4x^2-10}{2} = -2x^2-5 .$$

**Odd part.**

$$O(x) = \frac{f(x)-f(-x)}{2} = \frac{\big(x^3-2x^2+x-5\big)-\big(-x^3-2x^2-x-5\big)}{2} =
\frac{2x^3+2x}{2} = x^3+x .$$

**Verification.** $E(x)+O(x) = -2x^2-5+x^3+x = x^3-2x^2+x-5$ ✓. Also $E(-x)=-2x^2-5=E(x)$ ✓ and
$O(-x)=-x^3-x=-O(x)$ ✓. The decomposition is unique by Proposition 8.9, so no other answer is
possible.

**24.**

**Breakpoints.** $\lvert x-2\rvert$ changes behaviour at $x=2$ and $\lvert x+2\rvert$ at $x=-2$.

* If $x<-2$: both $x-2$ and $x+2$ are negative, so $h(x)=-(x-2)-(x+2) = -2x$.
* If $-2 \le x < 2$: $x+2 \ge 0$ but $x-2<0$, so $h(x) = -(x-2)+(x+2) = 4$.
* If $x \ge 2$: both are non-negative, so $h(x) = (x-2)+(x+2) = 2x$.

$$h(x) = \begin{cases}
-2x, & x<-2,\\
4, & -2 \le x < 2,\\
2x, & x \ge 2.
\end{cases}$$

**Graph.** Two rays of slope $-2$ (on the left) and $+2$ (on the right), joined by a horizontal segment
of height $4$ from $x=-2$ to $x=2$. The pieces agree at the joins: at $x=-2$, $-2(-2)=4$ and the
middle value is $4$; at $x=2$, $2(2)=4$ and the middle value is $4$. The graph is continuous, with
corners at $(-2,4)$ and $(2,4)$.

**Minimum and range.** On $x<-2$, $-2x>4$; on $x\ge 2$, $2x\ge4$; on $[-2,2]$ the value is exactly
$4$. Hence the minimum is $4$, attained exactly on $[-2,2]$, and
$\operatorname{ran} h = [4,\infty)$.

**Interpretation.** $\lvert x-2\rvert$ is the distance from $x$ to $2$ and $\lvert x+2\rvert$ the
distance from $x$ to $-2$; the two points are $4$ apart. For $x$ between them the distances add to
$4$; outside, the sum exceeds $4$ by twice the overshoot.

## Advanced

**25.**

**Injectivity.** Suppose $f(x_1)=f(x_2)$, i.e. $x_1^3+x_1 = x_2^3+x_2$. Rearrange and factor:

$$\big(x_1^3-x_2^3\big) + (x_1-x_2) = 0 .$$

Using $a^3-b^3=(a-b)(a^2+ab+b^2)$ with $a=x_1$, $b=x_2$:

$$(x_1-x_2)\big(x_1^2+x_1x_2+x_2^2\big) + (x_1-x_2) = (x_1-x_2)\big(x_1^2+x_1x_2+x_2^2+1\big) = 0 .$$

The second factor is strictly positive for all real $x_1,x_2$, because

$$x_1^2+x_1x_2+x_2^2 = \left(x_1+\tfrac{x_2}{2}\right)^2 + \tfrac34x_2^2 \ge 0,$$

so the whole factor is at least $1$. Hence $x_1-x_2=0$, i.e. $x_1=x_2$. Therefore $f$ is one-to-one.

**Evaluating the inverse.** $f(2) = 8+2 = 10$, so $f^{-1}(10)=2$. Because $f$ is one-to-one, this is the
*only* preimage of $10$ — the injectivity is what licenses writing "$=$" rather than "$\ni$".

**Remark.** $f$ is also onto $\mathbb{R}$ (it is continuous, $f(x)\to\pm\infty$ as $x\to\pm\infty$), so
$f$ is a bijection of $\mathbb{R}$. Its inverse cannot be written with elementary operations; the
existence proof here is enough for every purpose in this chapter.

**26.**

Throughout, $x$ ranges over a domain symmetric about $0$, so $-x$ is always admissible.

**(a) odd $\circ$ odd.** $(f\circ g)(-x) = f(g(-x)) = f(-g(x))$. Since $f$ is odd, $f(-t)=-f(t)$ for
every $t$; take $t=g(x)$:

$$f(-g(x)) = -f(g(x)) = -(f\circ g)(x).$$

So $f\circ g$ is odd.

**(b) even $\circ$ odd.** $(f\circ g)(-x) = f(g(-x)) = f(-g(x))$, and now $f$ is even, so
$f(-g(x)) = f(g(x)) = (f\circ g)(x)$. So $f\circ g$ is even.

**(c) odd $\circ$ even.** Here $g(-x)=g(x)$, so

$$(f\circ g)(-x) = f(g(-x)) = f(g(x)) = (f\circ g)(x),$$

regardless of whether $f$ is even or odd. So $f\circ g$ is even.

**(d) even $\circ$ even.** The same computation as (c): $(f\circ g)(-x)=f(g(x))$. Even.

**Summary.** A composition of two odd functions is odd; every other combination in which at least one
of the two is even gives an even composition. Intuition: the inner function decides which points are
paired, and an even inner function already pairs $x$ with $-x$ before the outer function acts.

**27.**

**(a)** Suppose $(f\circ g)(x_1)=(f\circ g)(x_2)$, i.e. $f(g(x_1))=f(g(x_2))$.

* Because $f$ is one-to-one, $f(u)=f(v) \Rightarrow u=v$. Apply with $u=g(x_1)$, $v=g(x_2)$: $g(x_1)=g(x_2)$.
* Because $g$ is one-to-one, $g(x_1)=g(x_2) \Rightarrow x_1=x_2$.

Hence $(f\circ g)(x_1)=(f\circ g)(x_2) \Rightarrow x_1=x_2$, so $f\circ g$ is one-to-one.

**(b)** Let $g:[0,\infty)\to[0,\infty)$ be $g(x)=\sqrt{x}$ and let $f:\mathbb{R}\to\mathbb{R}$ be
$f(x)=x^2$. Then

$$(f\circ g)(x) = f(\sqrt{x}) = (\sqrt{x})^2 = x \quad (x \ge 0),$$

which is one-to-one on $[0,\infty)$. But $f$ is **not** one-to-one on $\mathbb{R}$, since
$f(-1)=1=f(1)$.

**Lesson.** Injectivity of a composition forces injectivity of the *first-applied* function only. The
outer function can be as non-injective as it likes, provided the inner function's range avoids the
collisions.

**28.**

**Complete the square.**

$$x^2-6x+5 = (x-3)^2-9+5 = (x-3)^2-4 .$$

**Injectivity on $[3,\infty)$.** Suppose $x_1,x_2 \ge 3$ and $(x_1-3)^2=(x_2-3)^2$. Then
$x_1-3 = \pm(x_2-3)$. The minus sign gives $x_1+x_2=6$; with both $\ge 3$ this forces $x_1=x_2=3$. The
plus sign gives $x_1=x_2$. So $f$ is one-to-one on $[3,\infty)$.

**Range.** For $x \ge 3$, $(x-3)^2$ runs over $[0,\infty)$, so $f(x)$ runs over $[-4,\infty)$.

**Inverse.** Solve $y=(x-3)^2-4$:

$$(x-3)^2 = y+4 \quad\Longrightarrow\quad x-3 = \pm\sqrt{y+4}.$$

Since $x \ge 3$, take the plus sign: $x = 3+\sqrt{y+4}$. Hence

$$f^{-1}(x) = 3+\sqrt{x+4}, \qquad \operatorname{dom} f^{-1} = [-4,\infty), \quad
\operatorname{ran} f^{-1} = [3,\infty).$$

**Checks.** $f(3)=-4$ and $f^{-1}(-4)=3$ ✓. $f(5)=25-30+5=0$ and $f^{-1}(0)=3+2=5$ ✓. And

$$f\big(f^{-1}(x)\big) = \Big(3+\sqrt{x+4}-3\Big)^2-4 = (x+4)-4 = x .$$

**29.**

**Algebra first.** Factor the inside:

$$f(2x-6) = f\big(2(x-3)\big).$$

**Comparison of the three graphs.**

* $y=f(2x)$: horizontal compression toward the $y$-axis by a factor of $2$. A feature at $x=t$ moves
  to $x=t/2$.
* $y=f(x-6)$: shift right by $6$.
* $y=f(2x-6)$: **both**, in the order "compress, then shift right $3$". A feature at $x=t$ moves to
  $x = 3+t/2$.

Equivalently, by the identity $2x-6 = 2(x-3)$, one may first shift right by $6$ and then compress by
$2$: a feature at $t$ moves to $6+t$, then to $3+t/2$. Both orders give the same graph.

What does **not** work is shifting right by $3$ and then compressing the shifted graph: that produces
$f(2x-3)$, whose features sit at $x=\tfrac32 + t/2$.

**Domain.** We need $2x-6 \in [-1,5]$:

$$-1 \le 2x-6 \le 5 \;\Longrightarrow\; 5 \le 2x \le 11 \;\Longrightarrow\;
\tfrac52 \le x \le \tfrac{11}{2}.$$

So $\operatorname{dom} = [2.5,\,5.5]$, an interval of length $3$ — exactly half the original length
$6$, as a compression by $2$ demands. Its midpoint $4$ is the midpoint $2$ of $[-1,5]$ moved right by
$3$, consistent with the "compress then shift right $3$" reading.

**30.**

$$\begin{aligned}
\frac{f(1+h)-f(1)}{h}
&= \frac{1}{h}\left(\frac{1}{1+h}-1\right)\\[2pt]
&= \frac{1}{h}\cdot\frac{1-(1+h)}{1+h}\\[2pt]
&= \frac{1}{h}\cdot\frac{-h}{1+h}\\[2pt]
&= -\frac{1}{1+h}\qquad (h>0).
\end{aligned}$$

**Check.** With $h=1$: the left side is $\dfrac{1/2-1}{1} = -0.5$ and the formula gives
$-\tfrac12$ ✓. With $h=0.25$: $\dfrac{1/1.25-1}{0.25} = \dfrac{-0.2}{0.25} = -0.8$ and
$-\dfrac{1}{1.25} = -0.8$ ✓.

**Interpretation.** The average rate of change is negative for every $h>0$, so $1/x$ decreases on
$[1,\infty)$. As $h\to 0^+$ the average tends to $-1$, the slope of the tangent at $x=1$; the secant
slopes approach a limit, which is the derivative $-1/x^2$ evaluated at $x=1$.

**31.**

**Part 1: strict monotonicity implies injectivity.** Let $f$ be strictly increasing on an interval $I$,
and let $x_1,x_2 \in I$ with $x_1 \ne x_2$. Then either $x_1<x_2$, which gives $f(x_1)<f(x_2)$, or
$x_2<x_1$, which gives $f(x_2)<f(x_1)$. In both cases $f(x_1) \ne f(x_2)$. Therefore distinct inputs
give distinct outputs: $f$ is one-to-one on $I$. $\blacksquare$

(Contrapositive form, often quicker: if $f(x_1)=f(x_2)$ then $x_1<x_2$ and $x_2<x_1$ are both
impossible, so $x_1=x_2$.)

**Part 2: $x\mapsto x^3$ is strictly increasing.** Let $a<b$. Then

$$b^3-a^3 = (b-a)\big(b^2+ab+a^2\big).$$

The first factor is positive by $a<b$. For the second,

$$b^2+ab+a^2 = \left(b+\tfrac{a}{2}\right)^2+\tfrac34a^2 \ge 0,$$

with equality only when $a=b=0$. Since $a<b$, we cannot have $a=b=0$; if $a=0$ then $b>0$ and the
factor equals $b^2>0$. Hence the second factor is positive, and so $b^3-a^3>0$, i.e. $a^3<b^3$.
$\blacksquare$

Combining the two parts: $x^3$ is one-to-one on $\mathbb{R}$, and its inverse is $\sqrt[3]{x}$.

**32.**

**$g$ is one-to-one on $[0,\infty)$.** If $x_1,x_2 \ge 0$ and $x_1^2+2 = x_2^2+2$, then
$x_1^2=x_2^2$, so $x_1=\pm x_2$; since both are non-negative, $x_1=x_2$.

**$g^{-1}$.** Solve $y=x^2+2$ with $x\ge0$: $x^2=y-2$, so $x=\sqrt{y-2}$. Thus
$g^{-1}(x)=\sqrt{x-2}$ with $\operatorname{dom} g^{-1}=[2,\infty)$ (the range of $g$) and
$\operatorname{ran} g^{-1}=[0,\infty)$.

**$f\circ g$.**

$$(f\circ g)(x) = f(x^2+2) = \sqrt{x^2+2-1} = \sqrt{x^2+1}.$$

Domain: $x \ge 0$ and $x^2+1 \ge 0$ (always true), so $\operatorname{dom}(f\circ g)=[0,\infty)$.
Range: $x^2+1 \ge 1$, so $(f\circ g)(x)\ge1$, and every value $\ge1$ occurs; range $[1,\infty)$.

**Inverse, directly.** For $y \ge 1$, solve $y=\sqrt{x^2+1}$ with $x \ge 0$:

$$y^2 = x^2+1 \;\Longrightarrow\; x^2 = y^2-1 \;\Longrightarrow\; x = \sqrt{y^2-1}.$$

So $(f\circ g)^{-1}(x) = \sqrt{x^2-1}$ with domain $[1,\infty)$.

**Inverse, via the formula.** On $[0,\infty)$, $f(x)=\sqrt{x-1}$ solves to $f^{-1}(x)=x^2+1$ (domain
$[0,\infty)$, since the range of $f$ is $[0,\infty)$). Then

$$g^{-1}\big(f^{-1}(x)\big) = g^{-1}(x^2+1) = \sqrt{(x^2+1)-2} = \sqrt{x^2-1},$$

defined when $x \ge 0$ and $x^2+1 \ge 2$, i.e. $x \ge 1$. This is exactly the domain found directly,
and the formulas agree. ✓

**33.**

**Domain.** A length must be positive, and the fencing constrains the other side to $20-x$:

$$x>0, \qquad 20-x>0 \;\Longrightarrow\; \operatorname{dom} A = (0,20).$$

**Range.** Complete the square:

$$A(x) = x(20-x) = 20x-x^2 = 100-(x-10)^2 .$$

Hence $A(x) \le 100$, with equality at $x=10$, and $A(x)>0$ on $(0,20)$. Every value in $(0,100]$ is
attained because $(x-10)^2$ takes every value in $[0,100)$ as $x$ ranges over $(0,20)$. So

$$\operatorname{ran} A = (0,100] \text{ square metres}.$$

**Average rate of change on $[2,6]$.**

$$A(2) = 2\cdot 18 = 36, \qquad A(6) = 6\cdot 14 = 84,$$

$$\operatorname{ARC}_{[2,6]}(A) = \frac{84-36}{6-2} = \frac{48}{4} = 12 .$$

**Interpretation.** On this interval the enclosed area grows by $12\ \text{m}^2$ per metre of side
length. The sign is positive because both endpoints lie below the optimal $x=10$; on an interval
entirely above $10$ the average rate would be negative.

## Challenge

**34.**

**(a) Domain.** If $c \ne 0$, the denominator vanishes at $x=-d/c$, so
$\operatorname{dom} f = \mathbb{R}\setminus\{-d/c\}$. If $c=0$ then $f(x)=(ax+b)/d$ with $d\ne0$
(because $ad-bc=ad\ne0$ forces $a\ne0$ and $d\ne0$), so $\operatorname{dom} f=\mathbb{R}$.

**(b) Injectivity.** Suppose $f(x_1)=f(x_2)$ with both $x_i$ in the domain, so $cx_i+d\ne0$. Then

$$\frac{ax_1+b}{cx_1+d} = \frac{ax_2+b}{cx_2+d}
\;\Longrightarrow\;
(ax_1+b)(cx_2+d) = (ax_2+b)(cx_1+d).$$

Expand both sides:

$$acx_1x_2 + adx_1 + bcx_2 + bd = acx_1x_2 + adx_2 + bcx_1 + bd .$$

The terms $acx_1x_2$ and $bd$ cancel; collect the rest:

$$ad(x_1-x_2) - bc(x_1-x_2) = (ad-bc)(x_1-x_2) = 0 .$$

Since $ad-bc\ne0$, $x_1=x_2$. Hence $f$ is one-to-one. $\blacksquare$

**(c) The inverse.** Let $y=f(x)$:

$$\begin{aligned}
y(cx+d) &= ax+b\\
cxy+dy &= ax+b\\
x(cy-a) &= b-dy\\
x &= \frac{b-dy}{cy-a}.
\end{aligned}$$

The denominator $cy-a$ cannot vanish at a value $y$ in the range: $cy=a$ would mean $y=a/c$, but
$f(x)=a/c$ implies $ax+b = a(x+d/c) = ax+ad/c$, i.e. $bc=ad$, contradicting $ad-bc\ne0$. Hence

$$f^{-1}(x) = \frac{-dx+b}{cx-a},$$

which is again of the form $\dfrac{a'x+b'}{c'x+d'}$ with $(a',b',c',d')=(-d,\,b,\,c,\,-a)$, and
$a'd'-b'c' = (-d)(-a)-bc = ad-bc \ne 0$, so the same hypotheses hold.

**Verification.** Write $u = \dfrac{b-dx}{cx-a}$. Then

$$au+b = \frac{a(b-dx)+b(cx-a)}{cx-a} = \frac{ab-adx+bcx-ab}{cx-a} = \frac{x(bc-ad)}{cx-a},$$

$$cu+d = \frac{c(b-dx)+d(cx-a)}{cx-a} = \frac{bc-cdx+cdx-ad}{cx-a} = \frac{bc-ad}{cx-a}.$$

The ratio is $\dfrac{x(bc-ad)}{bc-ad} = x$ ✓.

**Example.** For $f(x)=\dfrac{3x-1}{x+2}$ we have $a=3$, $b=-1$, $c=1$, $d=2$, and
$ad-bc=6+1=7\ne0$. The formula gives $f^{-1}(x) = \dfrac{-2x-1}{x-3} = \dfrac{2x+1}{3-x}$, matching
Solution 21. ✓

**(d) The case $c=0$.** Then $f(x) = \dfrac{ax+b}{d} = \dfrac ad x + \dfrac bd$ is linear with slope
$a/d \ne 0$: a bijection of $\mathbb{R}$, its graph a straight line with no vertical asymptote. The
formula of part (c) specialises consistently:

$$f^{-1}(x) = \frac{-0\cdot x + b}{0\cdot x - a} = -\frac{b}{a} + \frac{d}{a}x = \frac{dx-b}{a},$$

which is the inverse of the linear function, and the excluded point $x=a/c$ "at infinity" simply
disappears. So $c=0$ is the degenerate case in which the excluded point is absent and the graph is a
line.

**35.**

**(a)** Assume $f\circ g$ is one-to-one. Let $g(x_1)=g(x_2)$ for some $x_1,x_2 \in A$. Applying $f$ to
both sides gives $f(g(x_1))=f(g(x_2))$, and injectivity of $f\circ g$ yields $x_1=x_2$. Hence $g$ is
one-to-one. $\blacksquare$

**(b)** Assume $f\circ g$ is onto $C$. Let $c \in C$. By surjectivity there is $a \in A$ with
$f(g(a))=c$. Put $b=g(a) \in B$; then $f(b)=c$. Since $c$ was arbitrary, $f$ is onto $C$.
$\blacksquare$

**(c) Converse of (a) fails.** Let $g(x)=x+1$ (injective on $\mathbb{R}$) and $f(x)=x^2$. Then
$(f\circ g)(x)=(x+1)^2$, and $(f\circ g)(-2)=1=(f\circ g)(0)$ with $-2\ne0$: the composition is not
injective although $g$ is. The failure comes entirely from $f$, which is not injective.

**Converse of (b) fails.** Let $f(x)=x$ from $\mathbb{R}$ to $\mathbb{R}$, which is onto, and let
$g(x)=\dfrac{x}{1+\lvert x\rvert}$. For $x \ge 0$, $g(x)=\dfrac{x}{1+x}\in[0,1)$; for $x<0$,
$g(x)=\dfrac{x}{1-x}\in(-1,0)$. So $\operatorname{ran} g=(-1,1)$, and
$(f\circ g)(x)=g(x)$ never reaches $2$. Thus $f\circ g$ is not onto even though $f$ is.

**(d)** Let $f:A\to B$ be a bijection, so $f^{-1}:B\to A$ is a bijection too. For $a \in A$, put
$b=f(a)$. By definition of the inverse, $f^{-1}(b)=a$. Applying the definition again — this time to
the function $f^{-1}$, whose inverse assigns to $a$ the unique element $b$ with $f^{-1}(b)=a$ — gives
$(f^{-1})^{-1}(a)=b=f(a)$. As $a$ was arbitrary, $(f^{-1})^{-1}=f$. $\blacksquare$

Alternatively: $f$ is a two-sided inverse of $f^{-1}$, since $f^{-1}\circ f=\operatorname{id}_A$ and
$f\circ f^{-1}=\operatorname{id}_B$; by uniqueness of inverses (Theorem 8.4), $f$ is *the* inverse of
$f^{-1}$.

**36.**

**(a) Geometric descriptions and proofs.**

*$\boldsymbol{y=\lvert f(x)\rvert}$. For each $x$, the new height is $\lvert f(x)\rvert$. If
$f(x)\ge0$ then $\lvert f(x)\rvert=f(x)$, so the point $(x,f(x))$ is unchanged. If $f(x)<0$ then
$\lvert f(x)\rvert=-f(x)$, and the new point $(x,-f(x))$ is the reflection of $(x,f(x))$ in the
$x$-axis. Therefore the graph keeps the parts on or above the axis and reflects the parts below it
upward. Points where $f(x)=0$ are fixed, and they typically become corners.*

*$\boldsymbol{y=f(\lvert x\rvert)}$. For $x\ge0$, $\lvert x\rvert=x$, so the right half of the new
graph coincides with the right half of the old graph. For $x<0$, $\lvert x\rvert=-x>0$, so the point
$\big(x, f(-x)\big)$ has the same height as the point $(-x, f(-x))$ on the old graph, and its
$x$-coordinate is the negative of that point's. Hence every point of the right half is reflected in
the $y$-axis to produce the left half; the original left half is discarded.*

**(b) Evenness.** Let $F(x)=f(\lvert x\rvert)$. Then

$$F(-x) = f(\lvert -x\rvert) = f(\lvert x\rvert) = F(x),$$

so $F$ is even. Its domain is $\{x : \lvert x\rvert \in \operatorname{dom} f\}$, which is symmetric
about $0$ because $\lvert -x\rvert=\lvert x\rvert$. $\blacksquare$

**(c) Applied to $f(x)=x^2-2x$.** Complete the square: $f(x)=(x-1)^2-1$, a parabola with vertex
$(1,-1)$ and zeros at $x=0$ and $x=2$.

*$y=\lvert x^2-2x\rvert$.* Zeros at $0$ and $2$. On $(-\infty,0]$ and $[2,\infty)$ the function is
non-negative, so it is unchanged; on $(0,2)$ it is negative and is reflected upward, turning the bottom
of the parabola into a hump with maximum at $(1,1)$. Range: $[0,\infty)$.

*$y=x^2-2\lvert x\rvert$.* This equals $\lvert x\rvert^2-2\lvert x\rvert$, which is even. For $x\ge0$
it coincides with $f$, giving a vertex at $(1,-1)$; the reflection produces a second vertex at
$(-1,-1)$. Zeros at $x=0$ and $x=\pm2$. Range: $[-1,\infty)$.

**Checks.** $f(\lvert -2\rvert)=f(2)=0$ ✓; $f(\lvert-1\rvert)=f(1)=-1$ ✓; $\lvert f(1)\rvert=1$ ✓.

**37.**

**Injectivity.** Let $x_1,x_2 \in (0,1)$ with $\dfrac{x_1}{1-x_1}=\dfrac{x_2}{1-x_2}$. Since the
denominators are positive, cross-multiplying is legitimate:

$$x_1(1-x_2) = x_2(1-x_1) \;\Longrightarrow\; x_1 - x_1x_2 = x_2 - x_1x_2
\;\Longrightarrow\; x_1=x_2 .$$

So $f$ is one-to-one.

**Surjectivity onto $(0,\infty)$.** Let $y>0$ and set $x = \dfrac{y}{1+y}$. Then:

* $x>0$, because $y>0$ and $1+y>0$;
* $x<1$, because $y<1+y$;
* and
  $$f(x) = \frac{\frac{y}{1+y}}{1-\frac{y}{1+y}} = \frac{\frac{y}{1+y}}{\frac{1}{1+y}} = y .$$

So every $y>0$ is attained by an $x \in (0,1)$. Hence $f$ is a bijection $(0,1)\to(0,\infty)$.

**Inverse.** The computation above *is* the inverse: $f^{-1}(y)=\dfrac{y}{1+y}$, defined for $y>0$.

**Checks.** $f\!\left(\tfrac12\right) = \dfrac{1/2}{1/2}=1$ and $f^{-1}(1)=\tfrac12$ ✓.
$f\!\left(\tfrac34\right)=\dfrac{3/4}{1/4}=3$ and $f^{-1}(3)=\tfrac34$ ✓. As $x\to1^-$, $f(x)\to+\infty$;
as $x\to0^+$, $f(x)\to0^+$, matching the behaviour of the inverse.

**Why this matters.** The interval $(0,1)$ has length $1$ and the interval $(0,\infty)$ is unbounded,
yet there is a perfect one-to-one pairing of their points. This is the first example of *cardinality*
rather than length as a measure of size: two sets have the same cardinality exactly when a bijection
exists between them. The same idea, pushed one step further, shows that $\mathbb{R}$ and $(0,1)$ have
the same cardinality — every interval, however short, contains as many points as the whole line.
