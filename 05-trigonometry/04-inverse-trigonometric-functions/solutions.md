# Inverse Trigonometric Functions — Solutions

> [Tutorial](README.md) · [Exercises](exercises.md) · 36 worked solutions

Each solution states the strategy, carries out every step, records the domain, and checks the result
on the unit circle or numerically. Decimal values are checks, not substitutes for exact answers.

## Beginner

### 1.

**Strategy.** Find the angle in the principal range $[-\pi/2,\pi/2]$ whose sine is $\tfrac12$.

The reference angle with sine $\tfrac12$ is $\pi/6$, and $\pi/6\in[-\pi/2,\pi/2]$.

**Answer.** $\arcsin\dfrac12=\dfrac{\pi}{6}$.

**Check on the unit circle.** The point at angle $\pi/6$ is
$\left(\cos\frac{\pi}{6},\sin\frac{\pi}{6}\right)=\left(\frac{\sqrt3}{2},\frac12\right)$; its height
is $\tfrac12$, as required.

### 2.

**Strategy.** Find the angle in $[0,\pi]$ whose cosine is $-\tfrac{\sqrt3}{2}$.

The reference angle with cosine $\tfrac{\sqrt3}{2}$ is $\pi/6$. Cosine is negative in the second
quadrant of the principal range, and $\cos(\pi-\pi/6)=\cos(5\pi/6)=-\tfrac{\sqrt3}{2}$. Since
$5\pi/6\in[0,\pi]$, this is the value.

**Answer.** $\arccos\left(-\dfrac{\sqrt3}{2}\right)=\dfrac{5\pi}{6}$.

**Check.** The point at angle $5\pi/6$ is $\left(-\frac{\sqrt3}{2},\frac12\right)$, with width
$-\frac{\sqrt3}{2}$ ✓. Numerically, $5\pi/6\approx2.6180$ lies in $[0,\pi]$.

### 3.

**Strategy.** Tangent is odd and $\arctan1=\pi/4$.

$$\arctan(-1)=-\arctan1=-\frac{\pi}{4}.$$

**Answer.** $-\dfrac{\pi}{4}$.

**Check.** $\tan(-\pi/4)=-1$ and $-\pi/4\in(-\pi/2,\pi/2)$ ✓.

### 4.

**Strategy.** The reference angle with sine $\tfrac{\sqrt2}{2}$ is $\pi/4$; sine is odd on the
principal interval.

$$\arcsin\left(-\frac{\sqrt2}{2}\right)=-\arcsin\frac{\sqrt2}{2}=-\frac{\pi}{4}.$$

**Answer.** $-\dfrac{\pi}{4}$.

**Check.** $\sin(-\pi/4)=-\tfrac{\sqrt2}{2}$ and $-\pi/4\in[-\pi/2,\pi/2]$ ✓.

### 5.

**Strategy.** Find the angle in $[0,\pi]$ with cosine $0$.

$\cos(\pi/2)=0$ and $\pi/2\in[0,\pi]$. No other angle in the principal range has cosine $0$, because
cosine is strictly decreasing there.

**Answer.** $\arccos0=\dfrac{\pi}{2}$.

**Check.** The point at angle $\pi/2$ is $(0,1)$; its width is $0$ ✓.

### 6.

**Strategy.** Find the angle in $(-\pi/2,\pi/2)$ with tangent $\sqrt3$.

$\tan(\pi/3)=\dfrac{\sin(\pi/3)}{\cos(\pi/3)}=\dfrac{\sqrt3/2}{1/2}=\sqrt3$, and
$\pi/3\in(-\pi/2,\pi/2)$.

**Answer.** $\arctan\sqrt3=\dfrac{\pi}{3}$.

**Check.** Numerically $\tan(\pi/3)\approx1.7321=\sqrt3$ ✓.

### 7.

**Strategy.** Read the domain and range from Definition 5.3 and the graph from the monotonicity of
cosine.

* **Domain:** $[-1,1]$, the range of cosine.
* **Range:** $[0,\pi]$, the chosen principal interval.
* **Graph:** decreasing from $(-1,\pi)$ through $(0,\pi/2)$ to $(1,0)$; it has vertical tangents at
  $x=\pm1$, an inflection at $(0,\pi/2)$, and the symmetry $\arccos(-x)=\pi-\arccos x$.

**Answer.** Domain $[-1,1]$, range $[0,\pi]$, strictly decreasing, with endpoint values
$\arccos(-1)=\pi$ and $\arccos1=0$.

**Check on the unit circle.** The points $(-1,\pi)$, $(0,\pi/2)$ and $(1,0)$ lie on the graph, matching
$\cos\pi=-1$, $\cos(\pi/2)=0$ and $\cos0=1$; between them the curve decreases monotonically ✓.

### 8.

**Strategy.** Name the angle, note that $\arccos\frac35\in(0,\pi/2)$, and use the Pythagorean identity
with a positive sine.

Let $\theta=\arccos\tfrac35$. Then $\cos\theta=\tfrac35$ and $\theta$ is acute, so

$$\sin\theta=+\sqrt{1-\frac{9}{25}}=\sqrt{\frac{16}{25}}=\frac45.$$

**Answer.** $\sin\left(\arccos\dfrac35\right)=\dfrac45$.

**Check.** The point at angle $\theta$ has coordinates $\left(\frac35,\frac45\right)$, which lies on
the unit circle because $9+16=25$ ✓.

### 9.

**Strategy.** Use $\cos(\arcsin x)=+\sqrt{1-x^2}$, since the arcsine lies where cosine is
non-negative.

With $x=-\tfrac{5}{13}$,

$$\cos\left(\arcsin\left(-\frac{5}{13}\right)\right)
=\sqrt{1-\frac{25}{169}}=\sqrt{\frac{144}{169}}=\frac{12}{13}.$$

**Answer.** $\dfrac{12}{13}$.

**Check.** The angle $\arcsin(-5/13)$ lies in the fourth quadrant of the principal interval, where
the point is $\left(\frac{12}{13},-\frac{5}{13}\right)$; the width is $\frac{12}{13}$ ✓.

### 10.

**Strategy.** Evaluate the inner function first, then the tangent.

$\arccos\tfrac12=\tfrac{\pi}{3}$, since $\cos\tfrac{\pi}{3}=\tfrac12$ and $\tfrac{\pi}{3}\in[0,\pi]$.
Therefore

$$\tan\left(\arccos\frac12\right)=\tan\frac{\pi}{3}=\sqrt3.$$

**Answer.** $\sqrt3$.

**Check.** The point at $\pi/3$ is $\left(\frac12,\frac{\sqrt3}{2}\right)$, and the ratio
height/width is $\sqrt3$ ✓.

### 11.

**Strategy.** The angle $\tfrac{5\pi}{6}$ already lies in the principal range $[0,\pi]$, so the
arccosine returns it unchanged.

**Answer.** $\dfrac{5\pi}{6}$.

**Check.** $\cos\frac{5\pi}{6}=-\frac{\sqrt3}{2}$ and $\frac{5\pi}{6}\in[0,\pi]$ ✓. On the circle
this is the second-quadrant point with width $-\frac{\sqrt3}{2}$.

### 12.

**Strategy.** The angle $\tfrac{5\pi}{6}$ is outside $[-\pi/2,\pi/2]$, so reflect it into the right
half of the circle: $\pi-\tfrac{5\pi}{6}=\tfrac{\pi}{6}$.

$$\arcsin\left(\sin\frac{5\pi}{6}\right)=\arcsin\frac12=\frac{\pi}{6}.$$

**Answer.** $\dfrac{\pi}{6}$.

**Check.** Both angles have height $\tfrac12$; the arcsine reports the one in $[-\pi/2,\pi/2]$,
namely $\pi/6$ ✓.

## Intermediate

### 13.

**Strategy.** $\tfrac{2\pi}{3}$ is in the second quadrant, outside the arcsine's principal range.
Reflect across the $y$-axis: $\pi-\tfrac{2\pi}{3}=\tfrac{\pi}{3}$.

$$\sin\frac{2\pi}{3}=\sin\frac{\pi}{3}=\frac{\sqrt3}{2},\qquad
\arcsin\frac{\sqrt3}{2}=\frac{\pi}{3}.$$

**Answer.** $\dfrac{\pi}{3}$.

**Check.** $\sin(2\pi/3)\approx0.8660=\sin(\pi/3)$, and $\pi/3\in[-\pi/2,\pi/2]$ ✓.

### 14.

**Strategy.** Tangent has period $\pi$, so subtract $\pi$ to enter the principal interval:
$\tfrac{3\pi}{4}-\pi=-\tfrac{\pi}{4}$.

$$\arctan\left(\tan\frac{3\pi}{4}\right)=\arctan(-1)=-\frac{\pi}{4}.$$

**Answer.** $-\dfrac{\pi}{4}$.

**Check.** $\tan(3\pi/4)=-1=\tan(-\pi/4)$ and $-\pi/4\in(-\pi/2,\pi/2)$ ✓.

### 15.

**Strategy.** Cosine is even, so $\cos(-\pi/5)=\cos(\pi/5)$; and $\pi/5\in[0,\pi]$.

**Answer.** $\dfrac{\pi}{5}$.

**Check.** $\cos(-\pi/5)=\cos36^\circ\approx0.8090=\cos(\pi/5)$, and $\pi/5$ lies in the arccosine's
range ✓.

### 16.

**Strategy.** $\tfrac{7\pi}{6}$ is in the third quadrant, outside $[-\pi/2,\pi/2]$. Its sine is
$-\tfrac12$, and the arcsine of $-\tfrac12$ is $-\tfrac{\pi}{6}$.

$$\sin\frac{7\pi}{6}=-\frac12,\qquad \arcsin\left(-\frac12\right)=-\frac{\pi}{6}.$$

**Answer.** $-\dfrac{\pi}{6}$.

**Check.** On the circle the point at $7\pi/6$ is
$\left(-\frac{\sqrt3}{2},-\frac12\right)$, the same height as the point at $-\pi/6$ ✓.

### 17.

**Strategy.** Use uniqueness: exhibit an angle in $[0,\pi]$ whose cosine is $x$.

Let $\theta=\arcsin x\in[-\pi/2,\pi/2]$. Then $\sin\theta=x$ and

$$\cos\left(\frac{\pi}{2}-\theta\right)=\sin\theta=x.$$

Moreover $\theta\in[-\pi/2,\pi/2]$ implies $\frac{\pi}{2}-\theta\in[0,\pi]$, which is exactly the
arccosine's principal range. By the uniqueness in Definition 5.3,

$$\arccos x=\frac{\pi}{2}-\theta=\frac{\pi}{2}-\arcsin x,$$

which is the claim.

**Answer.** The identity holds for every $x\in[-1,1]$.

**Check.** At $x=0$: $\arcsin0+\arccos0=0+\pi/2=\pi/2$ ✓. At $x=1$: $\pi/2+0=\pi/2$ ✓.

### 18.

**Strategy.** For $x>0$, both angles are acute and the tangent addition formula has a vanishing
denominator. For $x<0$, use oddness.

Let $\alpha=\arctan x$ and $\beta=\arctan\tfrac1x$. If $x>0$ then
$\alpha,\beta\in(0,\pi/2)$, so $\alpha+\beta\in(0,\pi)$, and

$$\tan(\alpha+\beta)=\frac{x+\frac1x}{1-x\cdot\frac1x},$$

whose denominator is $0$. A sum in $(0,\pi)$ whose tangent is undefined must be $\pi/2$. Hence
$\arctan x+\arctan\frac1x=\frac{\pi}{2}$.

If $x<0$, let $t=-x>0$. Then $\arctan x=-\arctan t$ and
$\arctan\frac1x=\arctan\left(-\frac1t\right)=-\arctan\frac1t$, so

$$\arctan x+\arctan\frac1x=-\left(\arctan t+\arctan\frac1t\right)=-\frac{\pi}{2}.$$

**Answer.** $\dfrac{\pi}{2}$ for $x>0$ and $-\dfrac{\pi}{2}$ for $x<0$; the expression is undefined at
$x=0$.

**Check.** $x=1$: $\pi/4+\pi/4=\pi/2$ ✓. $x=-1$: $-\pi/4-\pi/4=-\pi/2$ ✓.

### 19.

**Strategy.** Let $\theta=\arcsin x$ and use the double-angle formula.

With $\theta\in[-\pi/2,\pi/2]$, $\sin\theta=x$ and $\cos\theta=+\sqrt{1-x^2}$. Then

$$\sin2\theta=2\sin\theta\cos\theta=2x\sqrt{1-x^2}.$$

**Answer.** $\sin(2\arcsin x)=2x\sqrt{1-x^2}$ for $x\in[-1,1]$.

**Check.** At $x=\tfrac12$: $\arcsin\tfrac12=\pi/6$, and $\sin(\pi/3)=\tfrac{\sqrt3}{2}$, while
$2\cdot\tfrac12\cdot\tfrac{\sqrt3}{2}=\tfrac{\sqrt3}{2}$ ✓.

### 20.

**Strategy.** Use the double-angle formula in the form $\cos2\theta=2\cos^2\theta-1=\frac{1-\tan^2\theta}{1+\tan^2\theta}$.

Let $\theta=\arctan x$, so $\tan\theta=x$ and $\cos^2\theta=\dfrac{1}{1+x^2}$. Then

$$\cos2\theta=2\cos^2\theta-1=\frac{2}{1+x^2}-1=\frac{1-x^2}{1+x^2}.$$

**Answer.** $\cos(2\arctan x)=\dfrac{1-x^2}{1+x^2}$ for $x\in\mathbb{R}$.

**Check.** At $x=1$: $2\arctan1=\pi/2$ and $\cos(\pi/2)=0$, while $\frac{1-1}{2}=0$ ✓. At $x=0$: both
sides equal $1$ ✓.

### 21.

**Strategy.** Compute the tangent of the sum; the two angles are acute, so the sum lies in $(0,\pi)$.

$$\tan(\alpha+\beta)
=\frac{\tfrac12+\tfrac13}{1-\tfrac12\cdot\tfrac13}
=\frac{\tfrac56}{\tfrac56}=1,$$

where $\alpha=\arctan\tfrac12$ and $\beta=\arctan\tfrac13$. Since $\alpha,\beta\in(0,\pi/2)$, the sum
lies in $(0,\pi)$; the only angle there with tangent $1$ is $\pi/4$.

**Answer.** The sum is $\dfrac{\pi}{4}$.

**Check.** $\arctan0.5\approx0.4636$ and $\arctan(1/3)\approx0.3218$; the sum is $0.7854=\pi/4$ ✓.
Theorem 7.1 applies directly because $xy=\tfrac16<1$.

### 22.

**Strategy.** Use the arctangent addition formula in the case $xy>1$.

Let $\alpha=\arctan2$ and $\beta=\arctan3$. Both are in $(0,\pi/2)$ and $xy=6>1$, so
$\alpha+\beta\in(\pi/2,\pi)$. The addition formula gives

$$\alpha+\beta=\arctan\frac{2+3}{1-6}+\pi=\arctan(-1)+\pi=-\frac{\pi}{4}+\pi=\frac{3\pi}{4}.$$

**Answer.** $\dfrac{3\pi}{4}$.

**Check.** $\arctan2\approx1.1071$ and $\arctan3\approx1.2490$; their sum is $2.3562=3\pi/4$ ✓. Note
that ignoring the correction and writing $\arctan\frac{5}{-5}=-\pi/4$ is the standard error.

### 23.

**Strategy.** Use $\sin(\arccos x)=\sqrt{1-x^2}$ and $\cos(\arccos x)=x$, then divide.

Let $\theta=\arccos x\in[0,\pi]$. Then

$$\tan\theta=\frac{\sin\theta}{\cos\theta}=\frac{\sqrt{1-x^2}}{x}.$$

The formula requires $x\neq0$, since the tangent of $\pi/2$ is undefined. The sign is automatic: for
$x<0$, the angle is obtuse and the tangent is negative, matching the negative denominator.

**Answer.** $\tan(\arccos x)=\dfrac{\sqrt{1-x^2}}{x}$ for $x\in[-1,1]\setminus\{0\}$.

**Check.** $x=\tfrac12$: $\arccos\tfrac12=\pi/3$ and $\tan(\pi/3)=\sqrt3$, while
$\frac{\sqrt3/2}{1/2}=\sqrt3$ ✓.

### 24.

**Strategy.** Use the product formula for the cosine of a sum of arctangents,
$\cos(\alpha+\beta)=\frac{1-xy}{\sqrt{(1+x^2)(1+y^2)}}$.

With $x=\tfrac34$ and $y=\tfrac{5}{12}$,

$$1-xy=1-\frac{15}{48}=\frac{33}{48},\qquad
\sqrt{(1+x^2)(1+y^2)}=\sqrt{\frac{25}{16}\cdot\frac{169}{144}}
=\frac{5}{4}\cdot\frac{13}{12}=\frac{65}{48}.$$

Therefore

$$\cos\left(\arctan\frac34+\arctan\frac{5}{12}\right)=\frac{33/48}{65/48}=\frac{33}{65}.$$

**Answer.** $\dfrac{33}{65}$.

**Check.** $\arctan0.75\approx0.6435$ and $\arctan(5/12)\approx0.3948$; the sum is $1.0383$ radians
and its cosine is $0.5077\approx\frac{33}{65}$ ✓. Both angles are acute and their product is
$\frac{15}{48}<1$, so the sum is acute and the positive sign is correct.

## Advanced

### 25.

**Strategy.** Use the complement identity: the two sides sum to $\pi/2$ whenever both are defined.

The equation $\arcsin x=\arccos x$, together with $\arcsin x+\arccos x=\frac{\pi}{2}$ (Problem 17),
gives

$$2\arcsin x=\frac{\pi}{2}\quad\Longrightarrow\quad \arcsin x=\frac{\pi}{4}
\quad\Longrightarrow\quad x=\sin\frac{\pi}{4}=\frac{\sqrt2}{2}.$$

**Answer.** $x=\dfrac{\sqrt2}{2}$.

**Check.** $\arcsin\frac{\sqrt2}{2}=\frac{\pi}{4}$ and $\arccos\frac{\sqrt2}{2}=\frac{\pi}{4}$ ✓.
On the circle, the point at $\pi/4$ is $\left(\frac{\sqrt2}{2},\frac{\sqrt2}{2}\right)$, the unique
point whose two coordinates are equal and positive; equality of arcsine and arccosine is exactly
equality of those coordinates.

### 26.

**Strategy.** Apply the tangent to both sides, solve the resulting quadratic, then test each root in
the original equation, because the tangent addition formula requires $uv<1$ for its uncorrected form.

Let $\alpha=\arctan(2x)$ and $\beta=\arctan(3x)$, so $\alpha+\beta=\frac{\pi}{4}$ and
$\tan(\alpha+\beta)=1$. If $1-6x^2\neq0$, the addition formula gives

$$\frac{2x+3x}{1-6x^2}=1\quad\Longrightarrow\quad 5x=1-6x^2
\quad\Longrightarrow\quad 6x^2+5x-1=0.$$

Factoring, $(6x-1)(x+1)=0$, so $x=\tfrac16$ or $x=-1$.

* $x=\tfrac16$: then $uv=6\cdot\frac{1}{36}=\frac16<1$, so the formula used is legitimate, and
  $\arctan\frac13+\arctan\frac12=\frac{\pi}{4}$ by Problem 21. Valid.
* $x=-1$: then $uv=6>1$, so the uncorrected formula does not apply. Directly,
  $\arctan(-2)+\arctan(-3)=-\left(\arctan2+\arctan3\right)=-\frac{3\pi}{4}\neq\frac{\pi}{4}$ by
  Problem 22. Rejected.

The remaining possibility $1-6x^2=0$, i.e. $x=\pm\frac{1}{\sqrt6}$, makes the tangent of the sum
undefined; then $\alpha$ and $\beta$ have the same sign and the sum is $\pm\frac{\pi}{2}$, never
$\frac{\pi}{4}$.

**Answer.** $x=\dfrac16$.

**Check.** $\arctan\frac13\approx0.3218$ and $\arctan\frac12\approx0.4636$ sum to $0.7854=\frac{\pi}{4}$ ✓.

### 27.

**Strategy.** Compute the tangent of the sum and then bound the sum, using the hypothesis $x>-1$ to
keep the second arctangent defined and to place both angles in a known interval.

Define

$$u=\arctan x,\qquad v=\arctan\frac{1-x}{1+x}.$$

The second expression is defined because $x>-1$ makes $1+x>0$. Compute

$$x+\frac{1-x}{1+x}=\frac{x(1+x)+1-x}{1+x}=\frac{1+x^2}{1+x},$$

$$1-x\cdot\frac{1-x}{1+x}=\frac{(1+x)-x(1-x)}{1+x}=\frac{1+x^2}{1+x}.$$

Both are equal and nonzero, so

$$\tan(u+v)=\frac{\frac{1+x^2}{1+x}}{\frac{1+x^2}{1+x}}=1.$$

Now bound the sum. Because $x>-1$ and arctangent is increasing,
$u>\arctan(-1)=-\frac{\pi}{4}$, and also $u<\frac{\pi}{2}$. Since $v\in\left(-\frac{\pi}{2},\frac{\pi}{2}\right)$,

$$-\frac{3\pi}{4}<u+v<\pi.$$

The only angle in that interval with tangent $1$ is $\frac{\pi}{4}$ (the other solutions
$-\frac{3\pi}{4}$ and $\frac{5\pi}{4}$ lie outside the open interval). Hence $u+v=\frac{\pi}{4}$.

**Answer.** The identity holds for every $x>-1$.

**Check.** $x=0$: $\arctan0+\arctan1=\frac{\pi}{4}$ ✓. $x=1$: $\arctan1+\arctan0=\frac{\pi}{4}$ ✓.
$x=-\frac12$: $\arctan(-\frac12)\approx-0.4636$ and the second argument is
$\frac{3/2}{1/2}=3$, so $\arctan3\approx1.2490$; the sum is $0.7854=\frac{\pi}{4}$ ✓.

### 28.

**Strategy.** Use uniqueness of the principal value: exhibit an angle in the correct range with the
required cosine or tangent.

*For the arccosine.* Let $y=\arccos x\in[0,\pi]$. Then $\cos(\pi-y)=-\cos y=-x$ and
$\pi-y\in[0,\pi]$, which is the principal range. By the uniqueness clause of Definition 5.3,
$\arccos(-x)=\pi-y=\pi-\arccos x$.

*For the arctangent.* Let $z=\arctan x\in(-\pi/2,\pi/2)$. Then $\tan(-z)=-\tan z=-x$ and
$-z\in(-\pi/2,\pi/2)$, so by Definition 5.4, $\arctan(-x)=-z=-\arctan x$.

**Answer.** Both identities hold on the stated domains, $x\in[-1,1]$ and $x\in\mathbb{R}$
respectively.

**Check.** $x=\frac12$: $\arccos(-\frac12)=\frac{2\pi}{3}$ and
$\pi-\arccos\frac12=\pi-\frac{\pi}{3}=\frac{2\pi}{3}$ ✓. $x=1$: $\arctan(-1)=-\frac{\pi}{4}$ ✓.

### 29.

**Strategy.** Apply the chain rule with the derivative formulas of Section 7.10.

(a) With $u=2x$, $u'=2$,

$$f'(x)=\frac{2}{\sqrt{1-(2x)^2}}=\frac{2}{\sqrt{1-4x^2}},$$

valid when $\lvert2x\rvert<1$, that is $\lvert x\rvert<\frac12$.

(b) With $u=x^2$, $u'=2x$,

$$g'(x)=\frac{2x}{1+(x^2)^2}=\frac{2x}{1+x^4},$$

valid for all real $x$.

**Answer.** $f'(x)=\dfrac{2}{\sqrt{1-4x^2}}$ on $\left(-\frac12,\frac12\right)$;
$g'(x)=\dfrac{2x}{1+x^4}$ on $\mathbb{R}$.

**Check.** At $x=0$ we have $g'(0)=0$, matching the flat minimum of $\arctan(x^2)$, and $f'(0)=2$.
Numerically,
$\frac{\arcsin(0.4)-\arcsin0}{0.2}=\frac{0.41152}{0.2}\approx2.058$, close to $2$; the remaining gap
is the curvature of the arcsine ✓.

### 30.

**Strategy.** Recognise the standard antiderivatives and apply the fundamental theorem of calculus.

(a)

$$\int_0^1\frac{dx}{1+x^2}=\left[\arctan x\right]_0^1=\arctan1-\arctan0=\frac{\pi}{4}-0=\frac{\pi}{4}.$$

(b)

$$\int_0^{1/2}\frac{dx}{\sqrt{1-x^2}}=\left[\arcsin x\right]_0^{1/2}
=\arcsin\frac12-\arcsin0=\frac{\pi}{6}.$$

**Answer.** (a) $\dfrac{\pi}{4}\approx0.7854$; (b) $\dfrac{\pi}{6}\approx0.5236$.

**Check.** Both integrands are positive and bounded by $1$ on intervals of length $1$ and $\frac12$,
so the answers must lie in $(0,1)$ and $(0,\frac12)$ respectively; they do. A numerical Simpson
evaluation reproduces $0.7854$ and $0.5236$ ✓.

### 31.

**Strategy.** Match coefficients in $R\sin(\theta+\varphi)=R\cos\varphi\sin\theta+R\sin\varphi\cos\theta$.

We need $R\cos\varphi=3$ and $R\sin\varphi=4$. Squaring and adding,

$$R^2=9+16=25\quad\Longrightarrow\quad R=5.$$

Then $\cos\varphi=\frac35>0$ and $\sin\varphi=\frac45>0$, so $\varphi$ is in the first quadrant:

$$\varphi=\arctan\frac43\approx0.9273\in(-\pi,\pi].$$

**Answer.** $3\sin\theta+4\cos\theta=5\sin\left(\theta+\arctan\dfrac43\right)$, with maximum $5$.

**Check.** At $\theta=0$ the left side is $4$, while $5\sin(0.9273)\approx5(0.8)=4$ ✓. At
$\theta=\frac{\pi}{2}$ the left side is $3$, and $5\sin\left(\frac{\pi}{2}+0.9273\right)
=5\cos(0.9273)=5\cdot\frac35=3$ ✓.

### 32.

**Strategy.** Compute the hypotenuse, then use $\arctan(\text{opposite}/\text{adjacent})$ for each
acute angle; verify the sum with the reciprocal law for arctangents.

The hypotenuse is $\sqrt{7^2+24^2}=\sqrt{625}=25$. The angle opposite the side of length $7$ is

$$A=\arctan\frac{7}{24}\approx16.26^\circ,$$

and the angle opposite the side of length $24$ is

$$B=\arctan\frac{24}{7}\approx73.74^\circ.$$

Since $\frac{24}{7}=\frac{1}{7/24}$ and $\frac{7}{24}>0$, the reciprocal law gives

$$A+B=\arctan\frac{7}{24}+\arctan\frac{24}{7}=\frac{\pi}{2}=90^\circ.$$

**Answer.** $A\approx16.26^\circ$ and $B\approx73.74^\circ$, summing to $90^\circ$.

**Check.** The point $\left(\frac{7}{25},\frac{24}{25}\right)$ lies on the unit circle because
$49+576=625$; its angle has tangent $\frac{24/25}{7/25}=\frac{24}{7}$, so it is $B$, and the
complementary angle $A$ has tangent $\frac{7}{24}$ ✓.

## Challenge

### 33.

**Strategy.** Combine the first two arctangents with Theorem 7.1, then combine the result with the
third. Each product is below $1$, so no correction term is needed.

First,

$$\arctan\frac12+\arctan\frac15=\arctan\frac{\frac12+\frac15}{1-\frac12\cdot\frac15}
=\arctan\frac{\frac{7}{10}}{\frac{9}{10}}=\arctan\frac79,$$

because $\frac12\cdot\frac15=\frac{1}{10}<1$. Now combine with $\arctan\frac18$: the product is
$\frac79\cdot\frac18=\frac{7}{72}<1$, so

$$\arctan\frac79+\arctan\frac18
=\arctan\frac{\frac79+\frac18}{1-\frac{7}{72}}
=\arctan\frac{\frac{56+9}{72}}{\frac{65}{72}}
=\arctan\frac{65}{65}=\arctan1=\frac{\pi}{4}.$$

Every application of the formula had a product below $1$ and both arguments positive, so each partial
sum lies in $(0,\frac{\pi}{2})$ and no $\pm\pi$ correction arises.

**Answer.** The sum is $\dfrac{\pi}{4}$.

**Check.** $0.46365+0.19740+0.12435=0.78540=\frac{\pi}{4}$ ✓.

### 34.

**Strategy.** Use the double-angle formula twice to express $4\arctan\frac15$ as a single
arctangent, then subtract the small arctangent with Theorem 7.1.

Let $a=\arctan\frac15$, so $\tan a=\frac15$ and $a\approx0.1974\in(0,\frac{\pi}{4})$. Then

$$\tan2a=\frac{2\tan a}{1-\tan^2a}
=\frac{\frac25}{1-\frac1{25}}
=\frac{\frac25}{\frac{24}{25}}=\frac{5}{12}.$$

Since $2a\in(0,\frac{\pi}{2})$, it follows that $2a=\arctan\frac{5}{12}$. Applying the doubling
formula again,

$$\tan4a=\frac{2\cdot\frac{5}{12}}{1-\frac{25}{144}}
=\frac{\frac56}{\frac{119}{144}}=\frac{120}{119}.$$

Since $4a\approx0.7896\in(0,\frac{\pi}{2})$, $4a=\arctan\frac{120}{119}$.

Now $\frac{120}{119}\cdot\frac{1}{239}=\frac{120}{28441}<1$, so Theorem 7.1 gives

$$4a-\arctan\frac{1}{239}
=\arctan\frac{\frac{120}{119}-\frac{1}{239}}{1+\frac{120}{119}\cdot\frac{1}{239}}
=\arctan\frac{\frac{28680-119}{28441}}{\frac{28441+120}{28441}}
=\arctan\frac{28561}{28561}=\arctan1=\frac{\pi}{4}.$$

**Answer.** $4\arctan\dfrac15-\arctan\dfrac{1}{239}=\dfrac{\pi}{4}$.

**Check.** $4(0.1973956)-0.0041841=0.7895822-0.0041841=0.7853981=\frac{\pi}{4}$ ✓. Machin used this
identity in 1706 to compute one hundred digits of $\pi$, because both arctangent arguments are small
and the series for $\arctan$ converges quickly.

### 35.

**Strategy.** Name the angle, compute its tangent, and use the fact that the angle already lies in the
arctangent's principal range.

Let $\theta=\arcsin x$ with $\lvert x\rvert<1$. Then $\theta\in(-\pi/2,\pi/2)$, $\sin\theta=x$, and

$$\cos\theta=+\sqrt{1-x^2}>0,\qquad \tan\theta=\frac{\sin\theta}{\cos\theta}=\frac{x}{\sqrt{1-x^2}}.$$

Because $\theta\in(-\pi/2,\pi/2)$, the arctangent returns $\theta$ itself:

$$\theta=\arctan(\tan\theta)=\arctan\frac{x}{\sqrt{1-x^2}}.$$

**Answer.** $\arcsin x=\arctan\dfrac{x}{\sqrt{1-x^2}}$ for $\lvert x\rvert<1$.

**Check.** $x=\frac12$: the right side is $\arctan\frac{1/2}{\sqrt3/2}=\arctan\frac{1}{\sqrt3}
=\frac{\pi}{6}=\arcsin\frac12$ ✓. $x=0$: both sides are $0$ ✓. For $x=-0.37$ both sides equal
$-0.3790$ ✓.

### 36.

**Strategy.** Show that the right-hand side is an angle in $[0,\pi]$ whose cosine is $x$, then invoke
uniqueness of the arccosine.

Let $x\in[-1,1]$. Then $\frac{1-x}{2}\in[0,1]$, so
$\theta=\arcsin\sqrt{\frac{1-x}{2}}$ is defined and lies in $[0,\frac{\pi}{2}]$. Hence
$2\theta\in[0,\pi]$. Moreover

$$\sin^2\theta=\frac{1-x}{2},$$

so the double-angle formula for cosine gives

$$\cos2\theta=1-2\sin^2\theta=1-2\cdot\frac{1-x}{2}=1-(1-x)=x.$$

Thus $2\theta$ is an angle in $[0,\pi]$ with cosine $x$. By Definition 5.3, that angle is unique, so
$\arccos x=2\theta$.

**Answer.** $\arccos x=2\arcsin\sqrt{\dfrac{1-x}{2}}$ for $x\in[-1,1]$.

**Check.** $x=0$: the right side is $2\arcsin\sqrt{\frac12}=2\cdot\frac{\pi}{4}=\frac{\pi}{2}
=\arccos0$ ✓. $x=1$: $2\arcsin0=0=\arccos1$ ✓. $x=-1$: $2\arcsin1=\pi=\arccos(-1)$ ✓. For
$x=-0.42$, both sides equal $2.0042$ ✓.
