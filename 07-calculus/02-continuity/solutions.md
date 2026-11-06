# Continuity — Solutions

> [Tutorial](README.md) · [Exercises](exercises.md) · 36 worked solutions

Each solution names the definition or theorem used, verifies its hypotheses, and shows every step.
Where a problem asks for a classification, the one-sided data are computed explicitly; where it asks
for an existence proof, the interval and the sign change (or fixed-point inequality) are displayed.

## Beginner

**1.**

*Method: the three conditions.*

1. $f(2)=2^2-3\cdot2+2=4-6+2=0$, so $f$ is defined at $2$.
2. $f$ is a polynomial, hence $\lim_{x\to2}f(x)=f(2)=0$ by Corollary 7.3.2.
3. The limit equals the value.

All three conditions hold, so $f$ is continuous at $2$.

**2.**

*Method: factor and compare.* The function is undefined at $x=1$, so it is not continuous there. For
$x\neq1$,

$$
\frac{x^2-1}{x-1}=\frac{(x-1)(x+1)}{x-1}=x+1\longrightarrow2 .
$$

The limit exists and $f(1)$ is undefined: the discontinuity is removable. Defining $f(1)=2$ gives the
continuous extension $f(x)=x+1$ on $\mathbb{R}$.

**3.**

*Method: one-sided limits.* As $x\to3^-$, the denominator $x-3$ is negative and small, so
$1/(x-3)\to-\infty$. As $x\to3^+$, it is positive and small, so $1/(x-3)\to+\infty$. At least one
one-sided limit is infinite, so the discontinuity is infinite; the line $x=3$ is a vertical asymptote.

**4.**

*Method: one-sided formulas.* For $x>0$, $\lvert x\rvert/x=x/x=1$; for $x<0$,
$\lvert x\rvert/x=(-x)/x=-1$. Hence

$$
\lim_{x\to0^-}f(x)=-1, \qquad \lim_{x\to0^+}f(x)=1 .
$$

Both one-sided limits are finite and different, so the discontinuity is a jump.

**5.**

*Method: one-sided formulas.* For $x\in[1,2)$, $\lfloor x\rfloor=1$; for $x\in[2,3)$,
$\lfloor x\rfloor=2$. Hence

$$
\lim_{x\to2^-}\lfloor x\rfloor=1, \qquad \lim_{x\to2^+}\lfloor x\rfloor=2,
$$

while $\lfloor2\rfloor=2$. The limits differ, so the discontinuity is a jump. The function is
continuous from the right at $2$, because the right limit equals the value.

**6.**

*Method: oscillation and the sequential criterion.* The function is bounded, $\lvert\sin(1/x)\rvert\le1$,
but has no limit at $0$. Indeed, with

$$
x_n=\frac{1}{\pi/2+2\pi n}, \qquad y_n=\frac{1}{2\pi n},
$$

both sequences tend to $0$ and $f(x_n)=1$, $f(y_n)=0$. By the sequential criterion (Theorem 7.2.2),
$f$ is not continuous at $0$; since it is bounded and has no limit, the discontinuity is oscillatory.
The function is undefined at $0$ as written; even if a value is assigned at $0$, the limit still fails.

**7.**

*Method: compare the one-sided limits with the value.* At $x=1$,

$$
\lim_{x\to1^-}f(x)=\lim_{x\to1^-}x^2=1,
\qquad
f(1)=2\cdot1-1=1,
\qquad
\lim_{x\to1^+}f(x)=\lim_{x\to1^+}(2x-1)=1 .
$$

All three numbers coincide, so $f$ is continuous at $1$.

**8.**

*Method: compare one-sided limits with the value.* At $x=0$,

$$
\lim_{x\to0^-}g(x)=\lim_{x\to0^-}(x+2)=2,
\qquad g(0)=0+2=2,
\qquad \lim_{x\to0^+}g(x)=\lim_{x\to0^+}(x^2+2)=2 .
$$

All three agree, so $g$ is continuous at $0$ (and, being piecewise polynomial with matching junction,
on $\mathbb{R}$).

**9.**

*Method: rational functions are continuous where the denominator is nonzero.* The denominator
$x^2-4=(x-2)(x+2)$ vanishes exactly at $x=\pm2$. Hence $f$ is continuous on

$$
(-\infty,-2)\cup(-2,2)\cup(2,\infty).
$$

At $x=\pm2$ the one-sided limits are infinite, so the discontinuities are infinite and the lines
$x=\pm2$ are vertical asymptotes.

**10.**

*Method: composition.* The function $x\mapsto x-5$ is a polynomial, hence continuous on $\mathbb{R}$,
and $\sqrt{\ }$ is continuous on $[0,\infty)$ by Theorem 7.5.1. By the composition theorem, $x\mapsto\sqrt{x-5}$
is continuous wherever $x-5\ge0$, that is, on $[5,\infty)$. At the endpoint $5$ the relevant statement
is continuity from the right, and $\sqrt0=0$.

**11.**

*Method: algebra of continuous functions.* The identity function $x\mapsto x$ is continuous on
$\mathbb{R}$ (given $\varepsilon>0$, take $\delta=\varepsilon$). The product of continuous functions is
continuous by Theorem 7.3.1, so $x\mapsto x^3=x\cdot x\cdot x$ is continuous on $\mathbb{R}$, in
particular at $-1$. Explicitly, $\lvert x^3-(-1)\rvert=\lvert x+1\rvert\,\lvert x^2-x+1\rvert$ and
$x^2-x+1\le3$ for $\lvert x+1\rvert\le1$.

**12.**

*Method: factor.* For $x\neq-2$,

$$
\frac{x^2-4}{x+2}=\frac{(x-2)(x+2)}{x+2}=x-2\longrightarrow-4 \quad (x\to-2).
$$

The limit exists and $f(-2)$ is undefined, so the discontinuity is removable. The continuous extension
is $f(x)=x-2$ with $f(-2)=-4$.

**13.**

*Method: one-sided limits near $\pi/2$.* There, $\sin x\to1$ and $\cos x\to0$. For $x\to(\pi/2)^-$,
$\cos x>0$, so $\tan x\to+\infty$; for $x\to(\pi/2)^+$, $\cos x<0$, so $\tan x\to-\infty$. At least one
one-sided limit is infinite, so the discontinuity is infinite and $x=\pi/2$ is a vertical asymptote.

**14.**

*Method: one-sided behaviour of $e^{1/x}$.* As $x\to0^-$, $1/x\to-\infty$, so $e^{1/x}\to0$. As
$x\to0^+$, $1/x\to+\infty$, so $e^{1/x}\to+\infty$. The left limit is finite ($0$) and the right limit
is infinite, so the discontinuity is infinite. The function is not defined at $0$, and no assignment
at $0$ can make it continuous, because the right-hand limit is not finite.

## Intermediate

**15.**

*Method: compute the limit and set $k$ equal to it.* For $x\neq3$,

$$
\frac{x^2-9}{x-3}=\frac{(x-3)(x+3)}{x-3}=x+3\longrightarrow6 .
$$

Continuity at $3$ requires $k=\lim_{x\to3}f(x)=6$. With $k=6$ the function is the polynomial $x+3$ and
is continuous everywhere.

**16.**

*Method: match the pieces at the junctions.* Continuity is automatic inside each piece; only $x=1$ and
$x=3$ matter.

*At $x=1$:* the left limit is $1+1=2$, and the value and right limit are $a+b$. Hence

$$
a+b=2 .
$$

*At $x=3$:* the left limit and value are $3a+b$, and the right limit is $3^2-1=8$. Hence

$$
3a+b=8 .
$$

Subtracting gives $2a=6$, so $a=3$, and then $b=2-3=-1$. Check: at $x=1$, $3\cdot1-1=2$; at $x=3$,
$3\cdot3-1=8=9-1$. ✓ Hence $f$ is continuous on $\mathbb{R}$ exactly for $a=3$, $b=-1$.

**17.**

*Method: IVT, then bisection.* The polynomial $p(x)=x^3+x-1$ is continuous on $[0,1]$, and

$$
p(0)=-1<0, \qquad p(1)=1>0 .
$$

By Corollary 7.7.2 there is a root in $(0,1)$. (It is unique, because $x\mapsto x^3$ and $x\mapsto x$
are both strictly increasing, so $p$ is strictly increasing.)

*Step 1.* $p(0.5)=0.125+0.5-1=-0.375<0$, so the root lies in $(0.5,1)$.

*Step 2.* $p(0.75)=0.421875+0.75-1=0.171875>0$, so the root lies in $(0.5,0.75)$.

The interval $(0.5,0.75)$ has length $0.25$, so every point in it — in particular its midpoint
$0.625$ — is within $1/4$ of the root. (In fact the midpoint is within $1/8$.)

**18.**

*Method: IVT applied to a rearranged equation.* Define $f(x)=x^3-3x+1$, which is continuous on
$[0,1]$. Then

$$
f(0)=1>0, \qquad f(1)=1-3+1=-1<0 .
$$

The values have opposite signs, so by Corollary 7.7.2 there is $\xi\in(0,1)$ with $f(\xi)=0$, that is,
$\xi^3=3\xi-1$.

**19.**

*Method: IVT.* Let $g(x)=\cos x-x$ on $[0,1]$. Both $\cos x$ and $x$ are continuous, so $g$ is
continuous. Moreover

$$
g(0)=\cos0-0=1>0, \qquad g(1)=\cos1-1<0,
$$

because $\cos1<1$ (the cosine of a nonzero angle in $(0,\pi)$ is strictly less than $1$). By the IVT
there is $\xi\in(0,1)$ with $g(\xi)=0$, that is, $\cos\xi=\xi$.

**20.**

*Method: IVT and one bisection step.* Let $f(x)=x^2-2$ on $[1,2]$; it is continuous, and

$$
f(1)=-1<0, \qquad f(2)=2>0 .
$$

By Corollary 7.7.2 there is a root $\xi\in(1,2)$. The midpoint is $1.5$ and $f(1.5)=2.25-2=0.25>0$,
so $\xi\in(1,1.5)$. This interval has length $0.5$, and its midpoint $1.25$ is within $0.25$ of $\xi$.
(Indeed $\sqrt2\approx1.4142$, and $\lvert1.25-\sqrt2\rvert\approx0.164$.)

**21.**

*Method: direct estimate plus the hypotheses of the EVT.* On $(0,1)$, $f(x)=1/x>0$ and $f$ is
unbounded above: given any $M>0$, choose $x\in(0,1)$ with $x<1/M$; then $f(x)>M$. Hence no value $f(c)$
can be at least as large as all others, and there is no maximum.

The EVT does not apply because its hypothesis on the interval fails: $(0,1)$ is not closed (and not
compact). On the closed interval $[1,2]$, the same function is continuous and attains its maximum
$1$ at $x=1$ and its minimum $1/2$ at $x=2$, in accordance with the EVT.

**22.**

*Method: examine the values and the EVT hypotheses.* On $(-1,1)$, $f(x)=x^2\ge0$ and $f(0)=0$, so the
minimum $0$ is attained at $x=0$. The supremum is $1$, but $x^2<1$ for every $x\in(-1,1)$ and the
endpoints $\pm1$ are excluded, so no maximum is attained.

The EVT does not apply: $(-1,1)$ is bounded but not closed. On $[-1,1]$ the same function attains both
extrema, $0$ at $0$ and $1$ at $\pm1$.

**23.**

*Method: solve, and confirm with the IVT.* A fixed point satisfies $x=(x+1)/2$, equivalently
$2x=x+1$, hence $x=1$, which lies in $[0,1]$. So $x=1$ is the unique fixed point.

*Existence via the IVT:* $f$ maps $[0,1]$ into $[1/2,1]\subseteq[0,1]$ and is continuous. Let
$g(x)=f(x)-x=(1-x)/2$. Then $g(0)=1/2>0$ and $g(1)=0$, so $x=1$ is a fixed point.

**24.**

*Method: Lipschitz estimate.* For all $x,y\in\mathbb{R}$,

$$
\lvert f(x)-f(y)\rvert=\lvert(5x-2)-(5y-2)\rvert=5\lvert x-y\rvert .
$$

Given $\varepsilon>0$, take $\delta=\varepsilon/5$. Then $\lvert x-y\rvert<\delta$ implies
$\lvert f(x)-f(y)\rvert<5\delta=\varepsilon$. Since $\delta$ depends only on $\varepsilon$, $f$ is
uniformly continuous.

**25.**

*Method: bound the denominator away from $0$.* For $x,y\ge2$,

$$
\left\lvert\frac1x-\frac1y\right\rvert=\frac{\lvert x-y\rvert}{xy}\le\frac{\lvert x-y\rvert}{4},
$$

because $xy\ge4$. Given $\varepsilon>0$, take $\delta=4\varepsilon$. Then $\lvert x-y\rvert<\delta$
implies $\lvert1/x-1/y\rvert\le\lvert x-y\rvert/4<\varepsilon$. Uniform continuity follows.

**26.**

*Method: two sequences.* Take $x_n=n$ and $y_n=n+1/n$ for $n\ge1$. Then

$$
\lvert x_n-y_n\rvert=\frac1n\longrightarrow0,
\qquad
\lvert x_n^2-y_n^2\rvert=\left(n+\frac1n\right)^2-n^2=2+\frac{1}{n^2}\ge2 .
$$

With $\varepsilon=1$, every $\delta>0$ admits $n>1/\delta$, for which $\lvert x_n-y_n\rvert<\delta$ and
$\lvert f(x_n)-f(y_n)\rvert\ge2>\varepsilon$. Hence $f$ is not uniformly continuous on $[0,\infty)$.

## Advanced

**27.**

*Method: split $\varepsilon$.* Let $a$ be a limit point of the common domain and let $\varepsilon>0$.
By continuity of $f$ at $a$, there is $\delta_1>0$ such that $\lvert x-a\rvert<\delta_1$ implies
$\lvert f(x)-f(a)\rvert<\varepsilon/2$. By continuity of $g$ at $a$, there is $\delta_2>0$ such that
$\lvert x-a\rvert<\delta_2$ implies $\lvert g(x)-g(a)\rvert<\varepsilon/2$. Set
$\delta=\min(\delta_1,\delta_2)$. For $\lvert x-a\rvert<\delta$,

$$
\lvert(f+g)(x)-(f+g)(a)\rvert\le\lvert f(x)-f(a)\rvert+\lvert g(x)-g(a)\rvert<\frac{\varepsilon}{2}+\frac{\varepsilon}{2}=\varepsilon .
$$

Hence $f+g$ is continuous at $a$.

**28.**

*Method: the $\varepsilon$-$\delta$ chase through two functions.* Let $a$ be in the domain of $g$, with
$g(a)$ in the domain of $f$. Let $\varepsilon>0$.

1. Because $f$ is continuous at $g(a)$, there is $\eta>0$ such that, for $y$ in the domain of $f$,
   $$
   \lvert y-g(a)\rvert<\eta \ \Rightarrow\ \lvert f(y)-f(g(a))\rvert<\varepsilon .
   $$
2. Because $g$ is continuous at $a$, there is $\delta>0$ such that, for $x$ in the domain of $g$,
   $$
   \lvert x-a\rvert<\delta \ \Rightarrow\ \lvert g(x)-g(a)\rvert<\eta .
   $$

For such $x$, set $y=g(x)$; the first step applies and gives $\lvert f(g(x))-f(g(a))\rvert<\varepsilon$.
Hence $f\circ g$ is continuous at $a$.

*Where the hypotheses are used:* continuity of $g$ at $a$ produces the $\eta$-neighbourhood in the
domain of $f$; continuity of $f$ at $g(a)$ converts it into the $\varepsilon$-neighbourhood in the
range. If $f$ is discontinuous at $g(a)$, no $\eta$ exists at step 1; if $g$ is discontinuous at $a$,
no $\delta$ exists at step 2.

**29.**

*Method: EVT.* The function $f$ is continuous on the closed bounded interval $[a,b]$, so by
Theorem 7.9.3 it attains its minimum: there is $c\in[a,b]$ with $f(c)\le f(x)$ for all $x\in[a,b]$.
Set $m=f(c)$. By hypothesis $f(c)>0$, so $m>0$, and $f(x)\ge m$ for every $x\in[a,b]$.

*Why the hypothesis $f>0$ everywhere is needed:* $f(x)=x$ on $(0,1)$ is positive everywhere but has no
positive lower bound. The theorem is a statement about a continuous function on a closed bounded
interval, and the positivity converts the attained minimum into a strictly positive bound.

**30.**

*Method: IVT for each value.* Let $c\in[f(a),f(b)]$. Since $f$ is continuous on $[a,b]$ and $c$ lies
between $f(a)$ and $f(b)$ (endpoints included), Theorem 7.7.1 (with the endpoint cases handled by
$f(a)=c$ or $f(b)=c$) gives $\xi\in[a,b]$ with $f(\xi)=c$. As $c$ was arbitrary, $[f(a),f(b)]$ is
contained in the range of $f$.

*Remark:* the range may be larger; the theorem only guarantees that no value between $f(a)$ and $f(b)$
is skipped.

**31.**

*Method: IVT applied to $g(x)=f(x)-x$.* The function $g$ is continuous on $[0,1]$, being the difference
of continuous functions. Since $f$ maps $[0,1]$ into $[0,1]$,

$$
g(0)=f(0)-0=f(0)\ge0, \qquad g(1)=f(1)-1\le0 .
$$

If $g(0)=0$, then $f(0)=0$ and $0$ is a fixed point. If $g(1)=0$, then $f(1)=1$ and $1$ is a fixed
point. Otherwise $g(0)>0>g(1)$, and the IVT gives $x\in(0,1)$ with $g(x)=0$, that is, $f(x)=x$.

**32.**

*Method: transfer the Cauchy condition through $\delta$.* Let $\varepsilon>0$. By uniform continuity
of $f$, choose $\delta>0$ such that $\lvert x-y\rvert<\delta$ implies $\lvert f(x)-f(y)\rvert<\varepsilon$
for all $x,y\in A$. Since $(x_n)$ is Cauchy, there is $N$ such that $\lvert x_n-x_m\rvert<\delta$ for
all $n,m\ge N$. For such $n,m$, the choice of $\delta$ gives $\lvert f(x_n)-f(x_m)\rvert<\varepsilon$.
Hence $(f(x_n))$ is Cauchy.

*Why mere continuity is not enough:* $f(x)=1/x$ is continuous on $(0,1)$ and $x_n=1/n$ is Cauchy, but
$f(x_n)=n$ is not Cauchy. The single $\delta$ that works for every pair is exactly what fails for
$1/x$ near $0$.

**33.**

*Method: bound the sum of the factors.* For $x,y\in[0,3]$,

$$
\lvert x^2-y^2\rvert=\lvert x-y\rvert\,\lvert x+y\rvert\le 6\lvert x-y\rvert,
$$

because $0\le x+y\le6$. Given $\varepsilon>0$, take $\delta=\varepsilon/6$. Then
$\lvert x-y\rvert<\delta$ implies $\lvert x^2-y^2\rvert\le6\lvert x-y\rvert<\varepsilon$. The constant
$6$ does not depend on $x$ or $y$, so $f$ is uniformly continuous on $[0,3]$.

*Contrast:* on $[0,\infty)$ no such bound exists, because $x+y$ is unbounded; indeed $x^2$ is not
uniformly continuous there (Solution 26).

## Challenge

**34.**

*Method: a difference function with opposite signs at the endpoints.* Define

$$
g(x)=f\left(x+\frac12\right)-f(x), \qquad x\in\left[0,\frac12\right].
$$

Since $f$ is continuous on $[0,1]$, and $x+\frac12\in\left[\frac12,1\right]$, the function $g$ is
continuous on $\left[0,\frac12\right]$. At the endpoints,

$$
g(0)=f\left(\frac12\right)-f(0), \qquad
g\left(\frac12\right)=f(1)-f\left(\frac12\right)=f(0)-f\left(\frac12\right),
$$

where the last equality uses $f(1)=f(0)$. Hence $g\left(\frac12\right)=-g(0)$.

If $g(0)=0$, then $f(1/2)=f(0)$ and $x=0$ works. Otherwise $g(0)$ and $g(1/2)$ have opposite signs,
and the IVT applied to $g$ on $\left[0,\frac12\right]$ gives $x\in\left(0,\frac12\right)$ with $g(x)=0$,
that is, $f(x)=f(x+1/2)$.

*Why continuity is needed:* a function with a jump at $1/2$ can easily violate the conclusion; the IVT
is the only ingredient that produces the point.

**35.**

*Method: betweenness, then monotonicity.* Let $I$ be an interval and $f:I\to\mathbb{R}$ continuous and
injective.

**Step 1 (betweenness).** For any $a<b<c$ in $I$, the value $f(b)$ lies strictly between $f(a)$ and
$f(c)$.

Suppose not. Since $f$ is injective, $f(b)$ is different from $f(a)$ and $f(c)$. If $f(b)$ is smaller
than both, assume without loss of generality that $f(a)<f(c)$. Then $f(b)<f(a)<f(c)$; by the IVT on
$[b,c]$, the value $f(a)$ — which lies between $f(b)$ and $f(c)$ — is attained at some $\xi\in(b,c)$.
Since $\xi\neq a$, this contradicts injectivity. If instead $f(a)>f(c)$, the IVT on $[a,b]$ attains
$f(c)$ twice. The case where $f(b)$ is larger than both is analogous (or apply the argument to $-f$).
Hence $f(b)$ lies strictly between $f(a)$ and $f(c)$.

**Step 2 (monotonicity).** Fix $a<b$ in $I$. Injectivity gives either $f(a)<f(b)$ or $f(a)>f(b)$.
Suppose $f(a)<f(b)$; the other case is symmetric.

Two preliminary facts follow from Step 1.

* For every $x<b$, we have $f(x)<f(b)$. If $x<a$, apply Step 1 to the triple $(x,a,b)$: then $f(a)$
  lies between $f(x)$ and $f(b)$, and since $f(a)<f(b)$ this forces $f(x)<f(a)<f(b)$. If $a<x<b$,
  apply Step 1 to $(a,x,b)$: then $f(x)$ lies between $f(a)$ and $f(b)$, so $f(a)<f(x)<f(b)$.
* For every $x>b$, we have $f(b)<f(x)$. Apply Step 1 to $(a,b,x)$: then $f(b)$ lies between $f(a)$ and
  $f(x)$, and since $f(a)<f(b)$ this forces $f(a)<f(b)<f(x)$.

Now take any $x<y$ in $I$.

* If $y<b$: apply Step 1 to $(x,y,b)$. Then $f(y)$ lies between $f(x)$ and $f(b)$, and the first
  preliminary fact gives $f(y)<f(b)$; hence $f(x)<f(y)$.
* If $x>b$: apply Step 1 to $(b,x,y)$. Then $f(x)$ lies between $f(b)$ and $f(y)$, and the second
  preliminary fact gives $f(b)<f(x)$; hence $f(x)<f(y)$.
* If $x<b<y$: the preliminary facts give $f(x)<f(b)<f(y)$.

The case $x<b$ and $y=b$ is the first preliminary fact, and the case $x=b$ and $y>b$ is the second.
Every pair $x<y$ falls into one of these cases, so $f(x)<f(y)$ for all $x<y$: $f$ is strictly
increasing on $I$. If $f(a)>f(b)$, the same argument with all inequalities reversed shows that $f$ is
strictly decreasing.

Therefore a continuous injective function on an interval is strictly monotone. $\blacksquare$

**36.**

*Method: the IVT forces all values to be equal.* Suppose, for contradiction, that $f$ is not constant.
Then there are $x<y$ in $[a,b]$ with $f(x)\neq f(y)$; say $f(x)<f(y)$.

Choose an irrational number $\rho$ with $f(x)<\rho<f(y)$; such a $\rho$ exists because the irrationals
are dense in $\mathbb{R}$ and the interval $(f(x),f(y))$ is nonempty. Since $f$ is continuous on
$[a,b]$, the IVT (Theorem 7.7.1) gives $\xi$ between $x$ and $y$ with $f(\xi)=\rho$. But $\rho$ is
irrational, contradicting the hypothesis that $f$ takes only rational values.

Hence $f(x)=f(y)$ for all $x,y\in[a,b]$, so $f$ is constant. $\blacksquare$
