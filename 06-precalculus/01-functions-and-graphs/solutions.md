# Functions and Graphs — Solutions

> [Tutorial](README.md) · [Exercises](exercises.md) · 38 worked solutions

Each solution states the strategy, shows every significant step, and checks the answer where a check is
possible. Domain and range answers are given in interval notation, with the excluded points named.

## Beginner

### Solution 1

**(a)** Not a function. The input $1$ appears twice, with outputs $2$ and $5$; uniqueness of the output
fails.

**(b)** A function: each of $1,2,3$ appears exactly once. Domain $\{1,2,3\}$; range $\{2,5\}$.

**(c)** A function: every input in the table has exactly one output. Domain $\{-1,0,1,2\}$; range
$\{0,1,4\}$. Note that the repeated output $4$ is allowed — a function may reuse values, but may not
reuse inputs.

**(d)** Not a function when $x$ is the input. For $x=4$ both $y=2$ and $y=-2$ satisfy $y^2=4$, so the
input $4$ has two outputs. (Read the other way round, $x=y^2$ *is* a function of $y$: each $y$ determines
the single value $x=y^2$.)

**Principle.** A relation is a function precisely when no input occurs twice in the list of pairs.

### Solution 2

$$\begin{aligned}
f(-2) &= 2(-2)^2-3(-2)+1 = 8+6+1 = 15,\\
f(0) &= 2(0)^2-3(0)+1 = 1,\\
f(3) &= 2(3)^2-3(3)+1 = 18-9+1 = 10.
\end{aligned}$$

For $f(a+1)$, substitute the whole expression $a+1$ for $x$:

$$\begin{aligned}
f(a+1) &= 2(a+1)^2-3(a+1)+1\\
&= 2(a^2+2a+1)-3a-3+1\\
&= 2a^2+4a+2-3a-3+1\\
&= 2a^2+a .
\end{aligned}$$

**Check** with $a=2$: $f(3)=10$ from the first computation, and $2(2)^2+2=8+2=10$ ✓.

The substitution is the whole point: $f(a+1)$ means "the value of $f$ at the input $a+1$", so every
occurrence of $x$ is replaced by the entire expression $a+1$ in brackets.

### Solution 3

**(a)** An even root needs a non-negative radicand: $4-3x \ge 0 \Rightarrow -3x \ge -4 \Rightarrow
x \le \tfrac43$. Domain $\left(-\infty,\tfrac43\right]$.

**(b)** Factor the denominator: $x^2-x-6=(x-3)(x+2)$. The function is undefined where the denominator
vanishes, so the domain is $\mathbb{R}\setminus\{-2,3\}$.

**(c)** Two conditions: the radicand must be positive (it is in a denominator, so it cannot be zero), so
$x-5>0$, giving $x>5$. Domain $(5,\infty)$.

**(d)** $x^2-9 \ge 0 \Rightarrow (x-3)(x+3) \ge 0$. The product is non-negative outside the roots:
$x \le -3$ or $x \ge 3$. Domain $(-\infty,-3]\cup[3,\infty)$.

**Method.** Collect every restriction, solve each, then intersect. In (c) the intersection of $x \ge 5$
(from the root) with $x \ne 5$ (from the denominator) is $x>5$.

### Solution 4

**(a)** Complete the square: $x^2-8x+11=(x-4)^2-5$. A square is at least $0$, so $f(x) \ge -5$, with
equality at $x=4$. Range $[-5,\infty)$.

**(b)** The square root is at least $0$, so $3-\sqrt{x+1} \le 3$; the value $3$ is approached as
$x \to -1^+$ and is attained at $x=-1$ (since $\sqrt0=0$). As $x$ grows the expression decreases without
bound. Range $(-\infty,3]$.

**(c)** Solve $y=\dfrac{2}{x-1}$ for $x$: $y(x-1)=2$, so $x=1+\dfrac2y$. This is defined for every
$y \ne 0$, and each such $y$ produces a legal input $x \ne 1$. Range $\mathbb{R}\setminus\{0\}$.

**Check.** In (a), $f(4)=16-32+11=-5$ ✓. In (b), $f(-1)=3$ ✓ and $f(0)=2$ ✓. In (c), $x=3$ gives
$y=1$, and the formula $x=1+2/1=3$ recovers the input ✓.

### Solution 5

**(a)** $f(-x)=(-x)^4-2(-x)^2=x^4-2x^2=f(x)$: even.

**(b)** $g(-x)=(-x)^5-(-x)=-x^5+x=-(x^5-x)=-g(x)$: odd.

**(c)** $h(-x)=x^2-x+1$, which is neither $x^2+x+1$ nor $-x^2-x-1$. A counterexample certifies "neither":
$h(1)=3$ but $h(-1)=1$, and neither $1=3$ nor $1=-3$ holds.

**(d)** $k(-x)=\dfrac{-x}{(-x)^2+4}=-\dfrac{x}{x^2+4}=-k(x)$: odd, with domain $\mathbb{R}$.

**Method.** Substitute $-x$, simplify, compare with $f(x)$ and $-f(x)$. Only the algebraic identity
proves a symmetry; single values can only refute one.

### Solution 6

Completing the square: $f(x)=x^2+6x+2=(x+3)^2-7$. Hence the vertex is $(-3,-7)$, the axis of symmetry is
$x=-3$, and the range is $[-7,\infty)$.

For monotonicity, take $x_1<x_2$. Then

$$f(x_2)-f(x_1)=(x_2+3)^2-(x_1+3)^2=(x_2-x_1)(x_1+x_2+6).$$

If $x_2 \le -3$ then $x_1+x_2< -6$, so the second factor is negative and $f(x_2)<f(x_1)$: $f$ is strictly
decreasing on $(-\infty,-3]$. If $x_1 \ge -3$ then $x_1+x_2>-6$, so $f(x_2)>f(x_1)$: $f$ is strictly
increasing on $[-3,\infty)$.

**Check.** $f(-3)=9-18+2=-7$ ✓; the vertex value is the minimum.

### Solution 7

First, $f(1)=1-3=-2$ and $f(4)=16-12=4$, so

$$\operatorname{ARC}(1,4)=\frac{4-(-2)}{4-1}=\frac63=2 .$$

Next, $f(2)=4-6=-2$ and

$$f(2+h)=(2+h)^2-3(2+h)=4+4h+h^2-6-3h=h^2+h-2 .$$

Therefore

$$\frac{f(2+h)-f(2)}{h}=\frac{(h^2+h-2)-(-2)}{h}=\frac{h^2+h}{h}=h+1 \quad (h \ne 0).$$

As $h \to 0$ this tends to $1$, the instantaneous rate of change at $x=2$.

**Check.** With $h=2$ the formula gives $3$, and direct computation over $[2,4]$ gives
$\operatorname{ARC}=\dfrac{4-(-2)}{2}=3$ ✓.

### Solution 8

**(a)** $y=(x-2)^2+5$: shift the parabola $y=x^2$ right by $2$ and up by $5$.

**(b)** $y=-\sqrt{x+1}$: shift $y=\sqrt{x}$ left by $1$, then reflect in the $x$-axis. (Equivalently,
reflect first and then shift left by $1$; the two operations commute here because the shift is
horizontal and the reflection vertical.)

**(c)** $y=2\lvert x\rvert-3$: stretch $y=\lvert x\rvert$ vertically by $2$, then shift down by $3$.

**(d)** $y=\dfrac{1}{x-3}$: shift $y=\dfrac1x$ right by $3$.

**Check (b).** At $x=0$ the formula gives $-1$; starting from $(0,0)$ on $y=\sqrt x$, shifting left by
$1$ gives $(-1,0)$, and reflecting gives $(-1,0)$ — the reflected branch passes through $(0,-1)$ ✓.

### Solution 9

**Domain.** $x+2 \ge 0 \Rightarrow x \ge -2$, so $[-2,\infty)$.

**Range.** The square root takes values in $[0,\infty)$, so $y \ge -3$: range $[-3,\infty)$.

**Intercepts.** $x=0$ gives $y=\sqrt2-3\approx-1.59$, so the $y$-intercept is $(0,\sqrt2-3)$. Setting
$y=0$ gives $\sqrt{x+2}=3$, hence $x+2=9$ and $x=7$: the $x$-intercept is $(7,0)$.

**Transformation.** Shift $y=\sqrt{x}$ left by $2$ and down by $3$; the starting point $(0,0)$ of the
base graph moves to $(-2,-3)$.

**Check.** $y(7)=\sqrt9-3=0$ ✓ and $y(-2)=-3$ ✓.

### Solution 10

$$(f\circ g)(x)=f(2x-3)=(2x-3)^2+1=4x^2-12x+10,$$
$$(g\circ f)(x)=g(x^2+1)=2(x^2+1)-3=2x^2-1 .$$

At $x=1$: $(f\circ g)(1)=f(-1)=(-1)^2+1=2$ and $(g\circ f)(1)=g(2)=2(2)-3=1$.

**Check.** Substituting $x=1$ into $4x^2-12x+10$ gives $4-12+10=2$ ✓. The values differ, which is
expected: composition is not commutative.

### Solution 11

**(a)** Inner $g(x)=3x-5$, outer $f(u)=u^4$: $h=f\circ g$.

**(b)** Inner $g(x)=x^2+1$, outer $f(u)=\sqrt u$: $h=f\circ g$.

**(c)** Inner $g(x)=x+2$, outer $f(u)=\dfrac{1}{u^3}$: $h=f\circ g$.

**Comment.** Decompositions are not unique. For (c) one could also take $g(x)=(x+2)^3$ and
$f(u)=\dfrac1u$. The useful decomposition is the one whose inner function is the "argument" of the
outer operation.

### Solution 12

Write $y=5x-2$ and solve for $x$: $5x=y+2$, so $x=\dfrac{y+2}{5}$. Hence
$f^{-1}(x)=\dfrac{x+2}{5}$.

Verify:

$$f^{-1}\bigl(f(x)\bigr)=\frac{(5x-2)+2}{5}=\frac{5x}{5}=x, \qquad
f\bigl(f^{-1}(x)\bigr)=5\cdot\frac{x+2}{5}-2=(x+2)-2=x .$$

**Check** numerically: $f(3)=13$ and $f^{-1}(13)=15/5=3$ ✓.

### Solution 13

The table shows $g(2)=5$ and $g(3)=5$ with $2 \ne 3$. A function with an inverse must be injective
(Theorem 8.4 of the tutorial): if $g^{-1}$ existed, then

$$2 = g^{-1}\bigl(g(2)\bigr) = g^{-1}(5) = g^{-1}\bigl(g(3)\bigr) = 3,$$

a contradiction. So the failure is **injectivity**: two distinct inputs share the output $5$. The domain
is $\{1,2,3,4\}$ and the range is $\{3,5,7\}$; on the smaller domain $\{1,2,4\}$ the function would be
injective, and an inverse could be defined there.

## Intermediate

### Solution 14

**(a)** $(f\circ g)(x)=f\!\left(\dfrac{1}{x-4}\right)=\sqrt{\dfrac{1}{x-4}}$.

Domain: $x \ne 4$ (from $g$) and $\dfrac{1}{x-4} \ge 0$. A reciprocal is non-negative exactly when its
denominator is positive, so $x>4$. Domain $(4,\infty)$.

**(b)** $(g\circ f)(x)=g(\sqrt x)=\dfrac{1}{\sqrt x-4}$.

Domain: $x \ge 0$ (from $f$), and $\sqrt x - 4 \ne 0$, i.e. $x \ne 16$. Domain
$[0,16)\cup(16,\infty)$.

**Check (a).** At $x=5$, $g(5)=1$ and $f(1)=1$; the composite formula gives $\sqrt{1}=1$ ✓.

**Remark.** In (b) the inner function is defined at $x=0$, and the composite is defined there too
($\sqrt0-4=-4 \ne 0$); the exclusion is caused by the *outer* function's denominator, not by the square
root.

### Solution 15

**Inverse.** Write $y=\dfrac{4x+1}{x-2}$ and solve:

$$y(x-2)=4x+1 \;\Longrightarrow\; xy-4x=2y+1 \;\Longrightarrow\; x(y-4)=2y+1
\;\Longrightarrow\; x=\frac{2y+1}{y-4}.$$

Hence $f^{-1}(x)=\dfrac{2x+1}{x-4}$.

**Domains and ranges.** $f$ is undefined at $x=2$, so its domain is $\mathbb{R}\setminus\{2\}$. The value
$4$ is never attained by $f$ (it would require $4x+1=4x-8$, i.e. $1=-8$), and every other value is
attained, so the range of $f$ is $\mathbb{R}\setminus\{4\}$. By the inverse relation, the domain of
$f^{-1}$ is $\mathbb{R}\setminus\{4\}$ and its range is $\mathbb{R}\setminus\{2\}$.

**Asymptotes.** For $f$: vertical $x=2$ (denominator zero, numerator $9 \ne 0$), horizontal $y=4$. For
$f^{-1}$: vertical $x=4$, horizontal $y=2$. The two pairs are swapped, as reflection in $y=x$ requires.

**Check.** $f(3)=13$; $f^{-1}(13)=\dfrac{27}{9}=3$ ✓. Also $f(0)=-\tfrac12$ and
$f^{-1}\!\left(-\tfrac12\right)=\dfrac{0}{-4.5}=0$ ✓.

### Solution 16

**Injectivity.** Complete the square: $f(x)=(x-2)^2-1$. On $[2,\infty)$ the function $x \mapsto (x-2)^2$
is strictly increasing (if $2 \le x_1<x_2$ then $0 \le x_1-2<x_2-2$, and squaring preserves the strict
inequality), so $f$ is strictly increasing and therefore injective.

**Range.** At $x=2$, $f(2)=-1$; as $x \to \infty$, $f(x) \to \infty$. Since $f$ is continuous and
increasing, the range is $[-1,\infty)$.

**Inverse.** From $y=(x-2)^2-1$ we get $(x-2)^2=y+1$, so $x-2=\pm\sqrt{y+1}$. The condition $x \ge 2$
forces the plus sign: $x=2+\sqrt{y+1}$. Hence $f^{-1}(x)=2+\sqrt{x+1}$ with domain $[-1,\infty)$.

**Check.** $f(3)=9-12+3=0$ and $f^{-1}(0)=2+1=3$ ✓; $f(2)=-1$ and $f^{-1}(-1)=2$ ✓.

### Solution 17

Domain: $x^2-4 \ne 0$, so $x \ne \pm2$; the domain $\mathbb{R}\setminus\{-2,2\}$ is symmetric about $0$.
For $x$ in the domain,

$$f(-x)=\frac{(-x)^3}{(-x)^2-4}=\frac{-x^3}{x^2-4}=-f(x).$$

Hence $f$ is odd. Its graph is unchanged by a half-turn about the origin, and the vertical asymptotes
$x=\pm2$ are mapped to one another by that half-turn, as they must be.

### Solution 18

Combine the fractions before dividing:

$$\begin{aligned}
\frac{f(x+h)-f(x)}{h}
&= \frac{1}{h}\left(\frac{1}{x+h}-\frac{1}{x}\right)\\
&= \frac{1}{h}\cdot\frac{x-(x+h)}{x(x+h)}\\
&= \frac{1}{h}\cdot\frac{-h}{x(x+h)}\\
&= -\frac{1}{x(x+h)} .
\end{aligned}$$

The cancellation of $h$ is legal because $h \ne 0$. As $h \to 0$ the expression tends to
$-\dfrac{1}{x^2}$, the derivative of $1/x$ — a result proved in
[Calculus](../../07-calculus/README.md).

**Check** with $x=1$, $h=1$: the original is $\dfrac{1/2-1}{1}=-\tfrac12$, and the formula gives
$-\dfrac{1}{1\cdot2}=-\tfrac12$ ✓.

### Solution 19

**Monotonicity.** Let $-1<x_1<x_2$. Then both denominators are positive, and

$$f(x_2)-f(x_1)=\frac{x_2}{x_2+1}-\frac{x_1}{x_1+1}
=\frac{x_2(x_1+1)-x_1(x_2+1)}{(x_1+1)(x_2+1)}
=\frac{x_2-x_1}{(x_1+1)(x_2+1)} .$$

The numerator is positive and the denominator is a product of positive numbers, so $f(x_2)>f(x_1)$:
$f$ is strictly increasing on $(-1,\infty)$.

**Failure on the whole domain.** Take $x_1=-1.1$ and $x_2=-0.9$, so $x_1<x_2$. Then

$$f(x_1)=\frac{-1.1}{-0.1}=11, \qquad f(x_2)=\frac{-0.9}{0.1}=-9,$$

and $f(x_1)=11>-9=f(x_2)$: the function is not increasing on $\mathbb{R}\setminus\{-1\}$. The vertical
asymptote at $x=-1$ lets the graph jump from $+\infty$ to $-\infty$, which a single monotone function
cannot do.

### Solution 20

**Parameters.** Write the inside in factored form: $2x+8=2(x+4)$, so $y=-3\lvert 2(x-(-4))\rvert+1$.
Hence $a=-3$, $b=2$, $h=-4$, $k=1$.

**Vertex.** The base vertex $(0,0)$ maps to $\left(\frac{0}{2}-4,\;-3\cdot0+1\right)=(-4,1)$.

**Intercepts.** $y$-intercept: $x=0$ gives $y=-3\lvert8\rvert+1=-23$. $x$-intercepts: solve
$-3\lvert2x+8\rvert+1=0$, i.e. $\lvert2x+8\rvert=\tfrac13$; then $2x+8=\pm\tfrac13$, so
$x=-4\pm\tfrac16$, giving $x=-\tfrac{25}{6}$ and $x=-\tfrac{23}{6}$.

**Range.** Since $-3\lvert2x+8\rvert \le 0$, we have $y \le 1$, and $1$ is attained at the vertex. Range
$(-\infty,1]$.

**Check.** $x=-4$: $y=-3\lvert0\rvert+1=1$ ✓; $x=-\tfrac{25}{6}$: $2x+8=\tfrac13$, so
$y=-3\cdot\tfrac13+1=0$ ✓.

### Solution 21

Compute the values: $h(0)=0$, $h(1)=-5+20=15$, $h(2)=-20+40=20$, $h(3)=-45+60=15$, $h(4)=-80+80=0$.

$$\operatorname{ARC}(0,2)=\frac{20-0}{2}=10,\qquad
\operatorname{ARC}(1,3)=\frac{15-15}{2}=0,\qquad
\operatorname{ARC}(2,4)=\frac{0-20}{2}=-10 .$$

All in metres per second. On $[0,2]$ the ball is still rising on average, so the average velocity is
positive. On $[1,3]$ the rise from $t=1$ to the peak at $t=2$ is exactly cancelled by the fall from the
peak back to the same height, so the average velocity is zero. On $[2,4]$ the ball descends throughout,
so the average velocity is negative. The three averages differ because the motion is not linear.

### Solution 22

$$(f\circ g)(x)=f\bigl(\sqrt{2-x}\bigr)=\sqrt{\sqrt{2-x}+3}.$$

Domain: the inner root requires $2-x \ge 0$, i.e. $x \le 2$. For such $x$ we have $\sqrt{2-x} \ge 0$,
hence $\sqrt{2-x}+3 \ge 3>0$, so the outer root imposes no extra condition. Domain $(-\infty,2]$.

**Check.** At $x=2$: $g(2)=0$ and $(f\circ g)(2)=\sqrt3$ ✓. At $x=-2$: $g(-2)=2$ and
$(f\circ g)(-2)=\sqrt{2+3}=\sqrt5$ ✓.

### Solution 23

The pieces apply on the stated intervals, with the middle piece owning both endpoints $0$ and $2$.

$$f(-3)=(-3)+2=-1,\quad f(0)=0^2=0,\quad f(1)=1^2=1,\quad f(2)=2^2=4,\quad f(3)=2(3)-1=5 .$$

**Domain.** Every real $x$ falls into exactly one piece, so the domain is $\mathbb{R}$.

**Range.** On $(-\infty,0)$ the values are $(-\infty,2)$; on $[0,2]$ they are $[0,4]$; on $(2,\infty)$
they are $(3,\infty)$. The union is
$(-\infty,2)\cup[0,4]\cup(3,\infty)=\mathbb{R}$, because $[0,4]$ already covers $[0,4]$ and
$(-\infty,2)$ covers everything below $2$.

**Check.** $f(2.001)=2(2.001)-1=3.002$, continuing the middle piece's endpoint value $4$ downward — the
function has a jump at $x=2$; piecewise functions need not be continuous.

### Solution 24

**For $P$:** consecutive differences are $11-6=5$, $16-11=5$, $21-16=5$, constant. Constant differences
mean constant average rate of change, so $P$ is linear. The slope is $5$ and $P(0)=6$, hence
$P(x)=5x+6$ and $P(5)=31$.

**For $Q$:** consecutive ratios are $18/6=3$, $54/18=3$, $162/54=3$, constant. Constant ratios mean
multiplication by a fixed factor per unit, so $Q$ is exponential: $Q(x)=6\cdot3^x$. Then
$Q(5)=6\cdot243=1458$.

**Comment.** Four points can never prove a family; they only support it. Here the constant differences
and ratios are decisive enough for the intended answer, and the predictions differ by a factor of about
$47$, so the choice matters.

### Solution 25

$$f\bigl(g(x)\bigr)=\bigl(\sqrt[3]{x-1}\bigr)^3+1=(x-1)+1=x,$$
$$g\bigl(f(x)\bigr)=\sqrt[3]{(x^3+1)-1}=\sqrt[3]{x^3}=x .$$

Both identities hold for every real $x$, so $f$ and $g$ are inverse functions.

**Domains and ranges.** $f(x)=x^3+1$ has domain $\mathbb{R}$ and range $\mathbb{R}$ (the cube is
surjective and strictly increasing). $g(x)=\sqrt[3]{x-1}$ also has domain $\mathbb{R}$ and range
$\mathbb{R}$, consistent with the swap of domain and range under inversion.

**Check.** $f(2)=9$ and $g(9)=\sqrt[3]{8}=2$ ✓.

### Solution 26

**Inverse.** Write $y=\dfrac{x-3}{x+2}$ and solve:

$$y(x+2)=x-3 \;\Longrightarrow\; xy-x=-3-2y \;\Longrightarrow\; x(y-1)=-(3+2y)
\;\Longrightarrow\; x=\frac{2y+3}{1-y}.$$

Hence $f^{-1}(x)=\dfrac{2x+3}{1-x}$.

**Domain and range.** $f$ is undefined at $x=-2$, so its domain is $\mathbb{R}\setminus\{-2\}$. The
value $1$ is never attained by $f$: $x-3=x+2$ would give $-3=2$. Every other value is attained, because
the formula for $f^{-1}$ is defined for every $x \ne 1$. Hence the range of $f$ is
$\mathbb{R}\setminus\{1\}$, the domain of $f^{-1}$ is $\mathbb{R}\setminus\{1\}$, and the range of
$f^{-1}$ is $\mathbb{R}\setminus\{-2\}$, matching the swap of domain and range under inversion.

**Verification.** $f^{-1}(0)=\dfrac{3}{1}=3$ and $f(3)=\dfrac{0}{5}=0$ ✓.

## Advanced

### Solution 27

Let $a_1,a_2 \in A$ and suppose $(f\circ g)(a_1)=(f\circ g)(a_2)$. By definition of composition,
$f\bigl(g(a_1)\bigr)=f\bigl(g(a_2)\bigr)$. Since $f$ is injective, this implies $g(a_1)=g(a_2)$. Since
$g$ is injective, this implies $a_1=a_2$. Therefore $(f\circ g)(a_1)=(f\circ g)(a_2)$ forces
$a_1=a_2$, which is precisely injectivity of $f\circ g$. $\blacksquare$

**Remark.** Both hypotheses are used, in that order, and neither can be dropped: if $g$ is not injective
the composite can identify two inputs, and if $f$ is not injective it can merge two distinct values of
$g$.

### Solution 28

**(a)** Suppose $f(a_1)=f(a_2)$. Applying $g$ to both sides gives
$g\bigl(f(a_1)\bigr)=g\bigl(f(a_2)\bigr)$, and the hypothesis $g(f(a))=a$ turns this into $a_1=a_2$.
Hence $f$ is injective. $\blacksquare$

**(b)** Let $g:B\to A$ be an inverse of $f$. Injectivity is part (a). For surjectivity, let $b \in B$.
Then $f\bigl(g(b)\bigr)=b$ by the second inverse identity, so $b$ is the image of $g(b) \in A$. Hence $f$
is surjective. Being injective and surjective, $f$ is bijective. $\blacksquare$

**Remark.** Part (a) shows that a *left* inverse already forces injectivity; a right inverse forces
surjectivity. Only an inverse on both sides forces both.

### Solution 29

Let $g,h:B\to A$ both satisfy the two inverse identities for $f:A\to B$. Fix $b \in B$. Since $f$ has the
inverse $g$, it is surjective, so there exists $a \in A$ with $f(a)=b$ (indeed $a=g(b)$). Then

$$g(b)=g\bigl(f(a)\bigr)=a \quad\text{and}\quad h(b)=h\bigl(f(a)\bigr)=a,$$

where the first equality uses $g\circ f=\operatorname{id}_A$ and the second uses
$h\circ f=\operatorname{id}_A$. Hence $g(b)=h(b)$. Since $b$ was arbitrary, $g=h$. $\blacksquare$

**Remark.** The proof has the standard shape of a uniqueness argument: two candidates, one arbitrary
point, and a structural fact (surjectivity) that lets both candidates be evaluated at the same place.

### Solution 30

By Theorem 8.3 of the tutorial, $f\circ g$ is a bijection, so it has an inverse. Compute

$$(g^{-1}\circ f^{-1})\circ(f\circ g)=g^{-1}\circ\bigl(f^{-1}\circ f\bigr)\circ g
=g^{-1}\circ\operatorname{id}_B\circ g=g^{-1}\circ g=\operatorname{id}_A,$$

where associativity of composition and the inverse identities for $f$ and $g$ were used. Similarly,

$$(f\circ g)\circ(g^{-1}\circ f^{-1})=f\circ\bigl(g\circ g^{-1}\bigr)\circ f^{-1}
=f\circ\operatorname{id}_B\circ f^{-1}=f\circ f^{-1}=\operatorname{id}_C .$$

Both identities hold, so $g^{-1}\circ f^{-1}$ is the inverse of $f\circ g$. By uniqueness of inverses
(Solution 29), $(f\circ g)^{-1}=g^{-1}\circ f^{-1}$. $\blacksquare$

### Solution 31

**(a)** Suppose $g(a_1)=g(a_2)$ for some $a_1,a_2 \in A$. Applying $f$ gives
$f\bigl(g(a_1)\bigr)=f\bigl(g(a_2)\bigr)$, i.e. $(f\circ g)(a_1)=(f\circ g)(a_2)$. Since $f\circ g$ is
injective, $a_1=a_2$. Hence $g$ is injective. $\blacksquare$

**(b)** Take $g(x)=e^x$ (injective, with values in $(0,\infty)$) and $f(x)=x^2$. Then
$(f\circ g)(x)=e^{2x}$, which is injective, while $f$ is not injective on $\mathbb{R}$ because
$f(-1)=f(1)=1$.

**Why no contradiction.** Part (a) concludes that the *inner* function is injective, and here $g=e^x$ is
injective. The outer function is never forced to be injective, because $g$'s values may lie entirely in a
region where $f$ happens to be injective — here $(0,\infty)$, where $x^2$ is strictly increasing. The
composite is injective because it never visits the ambiguous part of $f$'s domain.

### Solution 32

**(a)** Suppose $f$ is strictly increasing on the interval $I$, and let $x_1 \ne x_2$ in $I$. One of them
is smaller; say $x_1<x_2$. Strict increase gives $f(x_1)<f(x_2)$, so $f(x_1) \ne f(x_2)$. The decreasing
case is identical with the inequality reversed. Hence distinct inputs have distinct outputs, i.e. $f$ is
injective. $\blacksquare$

**(b)** Let $f(x)=\dfrac1x$ with domain $\mathbb{R}\setminus\{0\}$. It is injective: if
$\dfrac{1}{x_1}=\dfrac{1}{x_2}$ then $x_1=x_2$. It is not monotone on its domain: $f(-1)=-1$,
$f(1)=1$, so the function increases across the gap; but on $(-1,-\tfrac12)$ it takes the values $-1$ and
$-2$, so it decreases there. The interval hypothesis of (a) fails: $\mathbb{R}\setminus\{0\}$ is not an
interval, and the two branches can move in different directions without ever taking the same value.

### Solution 33

Expand the difference, collecting the linear and quadratic terms:

$$\begin{aligned}
f(u+h)-f(u)
&= a(u+h)^2+b(u+h)+c-\bigl(au^2+bu+c\bigr)\\
&= a\bigl(u^2+2uh+h^2-u^2\bigr)+b(u+h-u)\\
&= 2auh+ah^2+bh\\
&= h(2au+ah+b).
\end{aligned}$$

Dividing by $h \ne 0$ gives $\dfrac{f(u+h)-f(u)}{h}=2au+ah+b$. As $h \to 0$, this tends to $2au+b$, the
instantaneous rate of change at $x=u$.

**Check.** For $f(x)=x^2-3x$ (so $a=1$, $b=-3$) at $u=2$: $2au+b=4-3=1$, agreeing with the limit found
in Solution 7 ✓.

### Solution 34

Expand both sides. First $V(x)=x(12-2x)^2=x(144-48x+4x^2)=4x^3-48x^2+144x$. Then

$$\begin{aligned}
128-V(x) &= 128-4x^3+48x^2-144x\\
&= -4\bigl(x^3-12x^2+36x-32\bigr).
\end{aligned}$$

Now factor the cubic by grouping or by inspection of the root $x=2$: since
$2^3-12(4)+36(2)-32=8-48+72-32=0$, the factor theorem gives a factor $x-2$. Dividing,

$$x^3-12x^2+36x-32=(x-2)(x^2-10x+16)=(x-2)(x-2)(x-8)=(x-2)^2(x-8).$$

Hence $128-V(x)=-4(x-2)^2(x-8)$.

For $0<x<6$ we have $x-8<0$ and $(x-2)^2 \ge 0$, so the product $-4(x-2)^2(x-8) \ge 0$. Therefore
$V(x) \le 128$, with equality exactly when $x=2$. The maximum volume is $128\ \text{cm}^3$ at
$x=2$, giving a $2\times8\times8$ box.

**Check.** $V(2)=2\cdot8^2=128$ ✓; $V(1)=1\cdot10^2=100<128$ ✓; $V(4)=4\cdot4^2=64<128$ ✓.

## Challenge

### Solution 35

**(a)** On $(0,1)$ the denominator $1-x$ is positive, so $f(x)>0$: the formula maps $(0,1)$ into
$(0,\infty)$. Let $y>0$ and solve $y=\dfrac{x}{1-x}$:

$$y(1-x)=x \;\Longrightarrow\; y=x+xy \;\Longrightarrow\; x(1+y)=y
\;\Longrightarrow\; x=\frac{y}{1+y}.$$

Since $y>0$, the number $x=\dfrac{y}{1+y}$ lies in $(0,1)$: it is positive, and
$x<1 \iff y<1+y$, which is true. Now check both identities:

$$f\bigl(f^{-1}(y)\bigr)=\frac{\frac{y}{1+y}}{1-\frac{y}{1+y}}
=\frac{\frac{y}{1+y}}{\frac{1}{1+y}}=y, \qquad
f^{-1}\bigl(f(x)\bigr)=\frac{\frac{x}{1-x}}{1+\frac{x}{1-x}}
=\frac{\frac{x}{1-x}}{\frac{1}{1-x}}=x .$$

So $f$ is a bijection with $f^{-1}(y)=\dfrac{y}{1+y}$.

**(b)** On $\mathbb{R}$ the formula has a pole at $x=1$: it is undefined there, so its natural domain is
$\mathbb{R}\setminus\{1\}$, not $\mathbb{R}$. Moreover, the formula cannot be extended to $x=1$ by any
finite value; $f(x) \to +\infty$ as $x \to 1^-$ and $f(x) \to -\infty$ as $x \to 1^+$.

### Solution 36

**(a)** Define, on the symmetric domain $D$,

$$E(x)=\frac{f(x)+f(-x)}{2}, \qquad O(x)=\frac{f(x)-f(-x)}{2}.$$

Both are defined on $D$ because $-x \in D$ whenever $x \in D$. Compute $E(-x)=\dfrac{f(-x)+f(x)}{2}=E(x)$,
so $E$ is even, and $O(-x)=\dfrac{f(-x)-f(x)}{2}=-O(x)$, so $O$ is odd. Clearly $E(x)+O(x)=f(x)$.

For uniqueness, suppose $f=E_1+O_1=E_2+O_2$ with $E_i$ even and $O_i$ odd. Then
$E_1-E_2=O_2-O_1$ is both even and odd (a difference of even functions is even, of odd functions is odd),
so for every $x$,

$$E_1(x)-E_2(x)=-\bigl(E_1(x)-E_2(x)\bigr) \;\Longrightarrow\; E_1(x)-E_2(x)=0 .$$

Hence $E_1=E_2$ and then $O_1=O_2$. $\blacksquare$

**(b)** For $f(x)=2^x$,

$$E(x)=\frac{2^x+2^{-x}}{2}, \qquad O(x)=\frac{2^x-2^{-x}}{2},$$

and indeed $E+O=2^x$. These are the hyperbolic cosine and sine of $x\ln 2$; the decomposition separates
the "symmetric" and "antisymmetric" parts of the exponential.

### Solution 37

Let $y \in \mathbb{R}$ be arbitrary and write $x=f^{-1}(y)$, so $f(x)=y$. Using the oddness of $f$,

$$f(-x)=-f(x)=-y .$$

Thus $-x$ is an input that $f$ maps to $-y$. Since $f$ is injective, it is the *only* such input, so by
the definition of the inverse,

$$f^{-1}(-y)=-x=-f^{-1}(y).$$

As $y$ was arbitrary, $f^{-1}$ is odd. $\blacksquare$

**Remark.** Strict increase was not used; only bijectivity and oddness. Strict increase would be needed
to know that $f^{-1}$ is increasing (its graph is the reflection of an increasing graph).

### Solution 38

**(a)** The graph of $f$ is the set $G=\{(x,f(x)) : x \in \mathbb{R}\}$. Symmetry about the $y$-axis
means that $(x,y) \in G \iff (-x,y) \in G$.

*If $f$ is even:* let $(x,f(x)) \in G$. Then $f(-x)=f(x)$, so $(-x,f(x))=(-x,f(-x)) \in G$. Conversely,
if $(-x,y) \in G$ then $y=f(-x)$, and evenness gives $y=f(x)$, so $(x,y) \in G$. Hence $G$ is symmetric
about the $y$-axis.

*If $G$ is symmetric about the $y$-axis:* for any $x$, the point $(x,f(x))$ lies on $G$, so
$(-x,f(x))$ lies on $G$; but the only point of $G$ with abscissa $-x$ is $(-x,f(-x))$. Hence
$f(-x)=f(x)$ and $f$ is even. $\blacksquare$

**(b)** If $f$ is both even and odd then for every $x$,
$f(x)=f(-x)=-f(x)$, so $2f(x)=0$ and $f(x)=0$. Hence $f$ is the zero function. $\blacksquare$

**(c)** Suppose $f$ is even. Then $f(-1)=f(1)$, and $-1 \ne 1$. An injective function would force
$-1=1$, which is false. Hence $f$ is not injective. $\blacksquare$

**Remark.** Parts (b) and (c) explain why an even function can never be inverted on a symmetric domain:
its graph is a mirror image, so every horizontal line meets it twice (or not at all).
