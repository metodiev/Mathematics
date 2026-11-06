# Trigonometric Equations — Solutions

> [Tutorial](README.md) · [Exercises](exercises.md) · 38 worked solutions

Each solution reduces the equation to a basic one, writes every family with $n\in\mathbb{Z}$, checks
a representative value on the unit circle, and — for restricted intervals — states the complete
solution set and its count.

## Beginner

### 1.

**Strategy.** Use the two-family rule for sine with $k=\tfrac12$.

The principal value is $\arcsin\tfrac12=\tfrac{\pi}{6}$, and the reflection is
$\pi-\tfrac{\pi}{6}=\tfrac{5\pi}{6}$.

**Answer.** $\theta=\dfrac{\pi}{6}+2n\pi$ or $\theta=\dfrac{5\pi}{6}+2n\pi$, $n\in\mathbb{Z}$;
compact form $\theta=(-1)^n\dfrac{\pi}{6}+n\pi$.

**Check on the unit circle.** The horizontal line $y=\tfrac12$ meets the circle at
$\left(\frac{\sqrt3}{2},\frac12\right)$ and $\left(-\frac{\sqrt3}{2},\frac12\right)$, at angles
$\tfrac{\pi}{6}$ and $\tfrac{5\pi}{6}$ ✓. At $n=1$ the first family gives $\tfrac{13\pi}{6}$, which is
$\tfrac{\pi}{6}$ after one turn.

### 2.

**Strategy.** Cosine equation with a positive value: two families symmetric about the $x$-axis.

$\arccos\tfrac{\sqrt2}{2}=\tfrac{\pi}{4}$, so

$$\theta=\pm\frac{\pi}{4}+2n\pi,\qquad n\in\mathbb{Z}.$$

**Answer.** $\theta=\dfrac{\pi}{4}+2n\pi$ or $\theta=-\dfrac{\pi}{4}+2n\pi$.

**Check.** The vertical line $x=\tfrac{\sqrt2}{2}$ cuts the circle at angles $\tfrac{\pi}{4}$ and
$-\tfrac{\pi}{4}$ ✓. In $[0,2\pi)$ these are $\tfrac{\pi}{4}$ and $\tfrac{7\pi}{4}$.

### 3.

**Strategy.** Tangent has period $\pi$, so one family suffices.

$\arctan1=\tfrac{\pi}{4}$, hence

$$\theta=\frac{\pi}{4}+n\pi,\qquad n\in\mathbb{Z}.$$

**Answer.** $\theta=\dfrac{\pi}{4}+n\pi$.

**Check.** The ray of slope $1$ and its opposite ray give angles $\tfrac{\pi}{4}$ and
$\tfrac{5\pi}{4}=\tfrac{\pi}{4}+\pi$ ✓.

### 4.

**Strategy.** Sine vanishes on the horizontal diameter.

$$\sin\theta=0\iff\theta=n\pi,\qquad n\in\mathbb{Z}.$$

**Answer.** $\theta=n\pi$.

**Check.** The circle meets the $x$-axis at $(1,0)$ and $(-1,0)$, at angles $0$ and $\pi$; adding
multiples of $\pi$ gives all of them ✓.

### 5.

**Strategy.** Cosine equation with a negative value: $\arccos(-\tfrac12)=\tfrac{2\pi}{3}$, and the two
families are $\pm\tfrac{2\pi}{3}+2n\pi$.

**Answer.** $\theta=\dfrac{2\pi}{3}+2n\pi$ or $\theta=-\dfrac{2\pi}{3}+2n\pi$.

**Check.** The vertical line $x=-\tfrac12$ meets the circle at
$\left(-\frac12,\pm\frac{\sqrt3}{2}\right)$, at angles $\tfrac{2\pi}{3}$ and $\tfrac{4\pi}{3}
=-\tfrac{2\pi}{3}+2\pi$ ✓.

### 6.

**Strategy.** Isolate the sine, then apply the sine rule.

$$2\sin\theta+1=0 \iff \sin\theta=-\frac12.$$

The principal value is $-\tfrac{\pi}{6}$ and the reflection is $\pi+\tfrac{\pi}{6}=\tfrac{7\pi}{6}$.

**Answer.** $\theta=-\dfrac{\pi}{6}+2n\pi$ or $\theta=\dfrac{7\pi}{6}+2n\pi$.

**Check.** In $[0,2\pi)$ the solutions are $\tfrac{11\pi}{6}\left(=-\tfrac{\pi}{6}+2\pi\right)$ and
$\tfrac{7\pi}{6}$; the horizontal line $y=-\tfrac12$ cuts the circle exactly there ✓.

### 7.

**Strategy.** Tangent of a negative value: the principal arctangent is negative, and the family repeats
every $\pi$.

$$\tan\theta=-\sqrt3 \iff \theta=-\frac{\pi}{3}+n\pi,\qquad n\in\mathbb{Z}.$$

**Answer.** $\theta=-\dfrac{\pi}{3}+n\pi$.

**Check.** In $[0,2\pi)$ this gives $\tfrac{2\pi}{3}$ and $\tfrac{5\pi}{3}$, both with tangent
$-\sqrt3$ ✓.

### 8.

**Strategy.** Cosine vanishes on the vertical diameter, at $\tfrac{\pi}{2}$ and $\tfrac{3\pi}{2}$;
these are half a turn apart.

$$\cos\theta=0 \iff \theta=\frac{\pi}{2}+n\pi,\qquad n\in\mathbb{Z}.$$

**Answer.** $\theta=\dfrac{\pi}{2}+n\pi$.

**Check.** Equivalently $\theta=\pm\tfrac{\pi}{2}+2n\pi$; the two descriptions coincide because
$-\tfrac{\pi}{2}+2n\pi=\tfrac{\pi}{2}+(2n-1)\pi$ ✓.

### 9.

**Strategy.** Sine attains $-1$ only at the bottom of the circle, once per turn.

$$\sin\theta=-1 \iff \theta=-\frac{\pi}{2}+2n\pi.$$

**Answer.** $\theta=-\dfrac{\pi}{2}+2n\pi$ (equivalently $\tfrac{3\pi}{2}+2n\pi$).

**Check.** The horizontal line $y=-1$ is tangent at $(0,-1)$, so there is only one family; writing
two families here would double-count the same angles ✓.

### 10.

**Strategy.** Cosine attains $1$ only at $(1,0)$.

$$\cos\theta=1 \iff \theta=2n\pi.$$

**Answer.** $\theta=2n\pi$.

**Check.** The vertical line $x=1$ is tangent at $(1,0)$ ✓.

### 11.

**Strategy.** Tangent vanishes on the horizontal diameter, with period $\pi$.

$$\tan\theta=0 \iff \theta=n\pi.$$

**Answer.** $\theta=n\pi$.

**Check.** The rays of slope $0$ are the positive and negative $x$-axes, at angles $0$ and $\pi$, and
these repeat every $\pi$ ✓.

### 12.

**Strategy.** Isolate the cosine, then restrict to one turn.

$$2\cos\theta=\sqrt3 \iff \cos\theta=\frac{\sqrt3}{2}
\iff \theta=\pm\frac{\pi}{6}+2n\pi.$$

In $[0,2\pi)$: taking $n=0$ gives $\tfrac{\pi}{6}$ and $-\tfrac{\pi}{6}\equiv\tfrac{11\pi}{6}$;
$n=1$ and $n=-1$ leave the interval.

**Answer.** $\theta\in\left\{\dfrac{\pi}{6},\dfrac{11\pi}{6}\right\}$; two solutions.

**Check.** The vertical line $x=\tfrac{\sqrt3}{2}$ meets the circle at
$\left(\frac{\sqrt3}{2},\pm\frac12\right)$, the two angles found ✓.

## Intermediate

### 13.

**Strategy.** Treat $2\theta$ as one angle, solve $\sin(2\theta)=0$, then divide by $2$.

$$2\theta=n\pi \iff \theta=\frac{n\pi}{2},\qquad n\in\mathbb{Z}.$$

**Answer.** $\theta=\dfrac{n\pi}{2}$.

**Check.** In $[0,2\pi)$ the values are $0,\tfrac{\pi}{2},\pi,\tfrac{3\pi}{2}$; each gives
$\sin2\theta=0$ ✓. The solution set has period $\tfrac{\pi}{2}$ in $\theta$, matching the period of
$\sin2\theta$.

### 14.

**Strategy.** Solve for $3\theta$ with the cosine rule, then divide by $3$.

$$3\theta=\pm\frac{\pi}{3}+2n\pi \iff \theta=\pm\frac{\pi}{9}+\frac{2n\pi}{3}.$$

**Answer.** $\theta=\dfrac{\pi}{9}+\dfrac{2n\pi}{3}$ or $\theta=-\dfrac{\pi}{9}+\dfrac{2n\pi}{3}$.

**Check.** At $\theta=\tfrac{\pi}{9}$, $3\theta=\tfrac{\pi}{3}$ and $\cos\tfrac{\pi}{3}=\tfrac12$ ✓.
In $[0,2\pi)$ there are six solutions, as the table of Section 10.2 predicts for $\cos3\theta$
($2B=6$).

### 15.

**Strategy.** Solve for the shifted angle $\theta+\tfrac{\pi}{4}$, then subtract $\tfrac{\pi}{4}$.

$$\theta+\frac{\pi}{4}=\frac{\pi}{3}+2n\pi \quad\text{or}\quad
\theta+\frac{\pi}{4}=\frac{2\pi}{3}+2n\pi,$$

so

$$\theta=\frac{\pi}{12}+2n\pi \quad\text{or}\quad \theta=\frac{5\pi}{12}+2n\pi.$$

**Answer.** $\theta=\dfrac{\pi}{12}+2n\pi$ or $\theta=\dfrac{5\pi}{12}+2n\pi$.

**Check.** At $\theta=\tfrac{\pi}{12}$, $\theta+\tfrac{\pi}{4}=\tfrac{\pi}{3}$ and the sine is
$\tfrac{\sqrt3}{2}$ ✓. At $\theta=\tfrac{5\pi}{12}$ the shifted angle is $\tfrac{2\pi}{3}$, also with
sine $\tfrac{\sqrt3}{2}$ ✓.

### 16.

**Strategy.** Divide by $\cos\theta$ only after proving it is nonzero.

If $\cos\theta=0$, then $\sin\theta=\pm1$, so $\sin\theta=\cos\theta$ would read $\pm1=0$, impossible.
Hence $\cos\theta\neq0$ and division is legitimate:

$$\tan\theta=1 \iff \theta=\frac{\pi}{4}+n\pi,\qquad n\in\mathbb{Z}.$$

**Answer.** $\theta=\dfrac{\pi}{4}+n\pi$.

**Check.** At $\theta=\tfrac{\pi}{4}$ both sides are $\tfrac{\sqrt2}{2}$ ✓; at
$\theta=\tfrac{5\pi}{4}$ both are $-\tfrac{\sqrt2}{2}$ ✓. The two intersection points of the line
$y=x$ with the circle are exactly these.

### 17.

**Strategy.** Substitute $u=\sin\theta$, factor, and keep admissible roots.

$$2u^2-u-1=(2u+1)(u-1)=0,$$

so $u=-\tfrac12$ or $u=1$, both in $[-1,1]$. Then

* $\sin\theta=-\tfrac12$ gives $\theta=-\tfrac{\pi}{6}+2n\pi$ or $\theta=\tfrac{7\pi}{6}+2n\pi$;
* $\sin\theta=1$ gives $\theta=\tfrac{\pi}{2}+2n\pi$.

**Answer.** $\theta=-\dfrac{\pi}{6}+2n\pi$, $\theta=\dfrac{7\pi}{6}+2n\pi$ or
$\theta=\dfrac{\pi}{2}+2n\pi$.

**Check.** At $\theta=\tfrac{\pi}{2}$: $2-1-1=0$ ✓. At $\theta=\tfrac{7\pi}{6}$:
$2\cdot\tfrac14-\left(-\tfrac12\right)-1=\tfrac12+\tfrac12-1=0$ ✓.

### 18.

**Strategy.** Substitute $u=\cos\theta$ and factor.

$$2u^2+u-1=(2u-1)(u+1)=0,$$

so $u=\tfrac12$ or $u=-1$. Hence $\cos\theta=\tfrac12$ gives $\theta=\pm\tfrac{\pi}{3}+2n\pi$, and
$\cos\theta=-1$ gives $\theta=\pi+2n\pi$.

**Answer.** $\theta=\pm\dfrac{\pi}{3}+2n\pi$ or $\theta=\pi+2n\pi$.

**Check.** At $\theta=\pi$: $2-1-1=0$ ✓. At $\theta=\tfrac{\pi}{3}$:
$2\cdot\tfrac14+\tfrac12-1=0$ ✓. The three solutions in $[0,2\pi)$ are $\tfrac{\pi}{3},\pi,\tfrac{5\pi}{3}$.

### 19.

**Strategy.** Take both square roots, then solve two tangent equations.

$$\tan^2\theta=3 \iff \tan\theta=\sqrt3 \ \text{ or }\ \tan\theta=-\sqrt3.$$

The first gives $\theta=\tfrac{\pi}{3}+n\pi$; the second gives $\theta=-\tfrac{\pi}{3}+n\pi$. Together,

$$\theta=\pm\frac{\pi}{3}+n\pi,\qquad n\in\mathbb{Z}.$$

**Answer.** $\theta=\pm\dfrac{\pi}{3}+n\pi$.

**Check.** In $[0,2\pi)$ the solutions are $\tfrac{\pi}{3},\tfrac{2\pi}{3},\tfrac{4\pi}{3},
\tfrac{5\pi}{3}$, four in total, consistent with a squared tangent equation (period $\pi$, two values
per period) ✓.

### 20.

**Strategy.** Factor rather than divide.

$$\sin2\theta=\sin\theta \iff 2\sin\theta\cos\theta-\sin\theta=0
\iff \sin\theta\,(2\cos\theta-1)=0.$$

Thus $\sin\theta=0$, giving $\theta=n\pi$, or $\cos\theta=\tfrac12$, giving
$\theta=\pm\tfrac{\pi}{3}+2n\pi$.

**Why division fails.** Dividing by $\sin\theta$ assumes $\sin\theta\neq0$, yet $\sin\theta=0$ produces
genuine solutions: $\theta=0$ satisfies $\sin0=\sin0$. The division deletes them. This is the general
rule: never divide by an expression containing the unknown unless it has been proved nonzero.

**Answer.** $\theta=n\pi$ or $\theta=\pm\dfrac{\pi}{3}+2n\pi$.

**Check.** $\theta=\pi$: $\sin2\pi=0=\sin\pi$ ✓. $\theta=\tfrac{\pi}{3}$:
$\sin\tfrac{2\pi}{3}=\sin\tfrac{\pi}{3}=\tfrac{\sqrt3}{2}$ ✓. $\theta=\tfrac{\pi}{2}$:
$\sin\pi=0\neq1$ ✓ (correctly excluded).

### 21.

**Strategy.** Write the cosine as a sine of a complementary angle and compare arguments.

$$\sin3\theta=\cos\theta=\sin\left(\frac{\pi}{2}-\theta\right),$$

so $3\theta=\tfrac{\pi}{2}-\theta+2n\pi$ or $3\theta=\pi-\left(\tfrac{\pi}{2}-\theta\right)+2n\pi$.
The first gives $4\theta=\tfrac{\pi}{2}+2n\pi$, so $\theta=\tfrac{\pi}{8}+\tfrac{n\pi}{2}$. The second
gives $2\theta=\tfrac{\pi}{2}+2n\pi$, so $\theta=\tfrac{\pi}{4}+n\pi$.

**Answer.** $\theta=\dfrac{\pi}{8}+\dfrac{n\pi}{2}$ or $\theta=\dfrac{\pi}{4}+n\pi$.

**Check.** $\theta=\tfrac{\pi}{8}$: $\sin\tfrac{3\pi}{8}\approx0.9239=\cos\tfrac{\pi}{8}$ ✓.
$\theta=\tfrac{\pi}{4}$: $\sin\tfrac{3\pi}{4}=\cos\tfrac{\pi}{4}=\tfrac{\sqrt2}{2}$ ✓. Six solutions
in $[0,2\pi)$.

### 22.

**Strategy.** Compare the arguments of two cosines.

$$\cos2\theta=\cos\theta \iff 2\theta=\pm\theta+2n\pi.$$

With the plus sign, $\theta=2n\pi$. With the minus sign, $3\theta=2n\pi$, so
$\theta=\tfrac{2n\pi}{3}$. The first family is contained in the second (take $n$ a multiple of $3$).

**Answer.** $\theta=\dfrac{2n\pi}{3}$.

**Check.** $\theta=\tfrac{2\pi}{3}$: $\cos\tfrac{4\pi}{3}=-\tfrac12=\cos\tfrac{2\pi}{3}$ ✓.
$\theta=\tfrac{\pi}{3}$: $\cos\tfrac{2\pi}{3}=-\tfrac12\neq\cos\tfrac{\pi}{3}$ ✓ (correctly
excluded). The solutions in $[0,2\pi)$ are $0,\tfrac{2\pi}{3},\tfrac{4\pi}{3}$.

### 23.

**Strategy.** Divide by $\cos2\theta$ after checking it cannot vanish, then restrict.

If $\cos2\theta=0$, then $\sin2\theta=\pm1\neq0$, contradicting the equation. Hence
$\cos2\theta\neq0$ and $\tan2\theta=1$:

$$2\theta=\frac{\pi}{4}+n\pi \iff \theta=\frac{\pi}{8}+\frac{n\pi}{2}.$$

In $[0,\pi)$: $n=0$ gives $\tfrac{\pi}{8}$; $n=1$ gives $\tfrac{5\pi}{8}$; $n=2$ gives
$\tfrac{9\pi}{8}>\pi$.

**Answer.** $\theta\in\left\{\dfrac{\pi}{8},\dfrac{5\pi}{8}\right\}$; two solutions.

**Check.** At $\theta=\tfrac{\pi}{8}$, $2\theta=\tfrac{\pi}{4}$ and
$\sin\tfrac{\pi}{4}=\cos\tfrac{\pi}{4}$ ✓. At $\theta=\tfrac{5\pi}{8}$, $2\theta=\tfrac{5\pi}{4}$, where
both sine and cosine equal $-\tfrac{\sqrt2}{2}$ ✓.

### 24.

**Strategy.** Replace $\sin^2\theta$ by $1-\cos^2\theta$ and solve the quadratic in $\cos\theta$.

$$2(1-\cos^2\theta)=3\cos\theta \iff 2\cos^2\theta+3\cos\theta-2=0.$$

Factoring, $(2\cos\theta-1)(\cos\theta+2)=0$. The root $\cos\theta=-2$ is impossible and is discarded;
the root $\cos\theta=\tfrac12$ gives

$$\theta=\pm\frac{\pi}{3}+2n\pi.$$

**Answer.** $\theta=\pm\dfrac{\pi}{3}+2n\pi$.

**Check.** At $\theta=\tfrac{\pi}{3}$: $2\cdot\tfrac34=\tfrac32=3\cdot\tfrac12$ ✓. The discarded root
illustrates the rule that only $-1\le\cos\theta\le1$ is admissible.

## Advanced

### 25.

**Strategy.** Combine the two sines into a product with the sum-to-product identity.

$$\sin2\theta+\sin3\theta=2\sin\frac{5\theta}{2}\cos\left(-\frac{\theta}{2}\right)
=2\sin\frac{5\theta}{2}\cos\frac{\theta}{2}=0.$$

Hence either $\sin\frac{5\theta}{2}=0$, giving $\frac{5\theta}{2}=n\pi$ and
$\theta=\frac{2n\pi}{5}$, or $\cos\frac{\theta}{2}=0$, giving $\frac{\theta}{2}=\frac{\pi}{2}+n\pi$
and $\theta=\pi+2n\pi$.

**Answer.** $\theta=\dfrac{2n\pi}{5}$ or $\theta=\pi+2n\pi$, $n\in\mathbb{Z}$.

**Check.** $\theta=\tfrac{2\pi}{5}$: $\sin\tfrac{4\pi}{5}+\sin\tfrac{6\pi}{5}
=\sin\tfrac{\pi}{5}-\sin\tfrac{\pi}{5}=0$ ✓. $\theta=\pi$: $0+0=0$ ✓. The families are disjoint:
$\tfrac{2n}{5}=1+2m$ would give $2n=5+10m$, impossible.

### 26.

**Strategy.** Two tangents are equal exactly when their arguments differ by a multiple of $\pi$;
record the domains first.

The equation requires $\theta\neq\frac{\pi}{2}+m\pi$ and $2\theta\neq\frac{\pi}{2}+m\pi$. Then

$$\tan2\theta=\tan\theta \iff 2\theta=\theta+n\pi \iff \theta=n\pi.$$

Every $\theta=n\pi$ is admissible: $\tan(n\pi)=0$ and $\tan(2n\pi)=0$ are both defined.

**Answer.** $\theta=n\pi$, $n\in\mathbb{Z}$.

**Check.** $\theta=\pi$: both sides are $0$ ✓. $\theta=\tfrac{\pi}{4}$ is *not* a solution because
$\tan\tfrac{\pi}{2}$ is undefined, even though it is not of the form $n\pi$ ✓. In $[0,2\pi)$ the
solutions are $0$ and $\pi$.

### 27.

**Strategy.** Combine the left side into one sinusoid.

With $a=1$, $b=1$, $R=\sqrt2$ and $\varphi=\tfrac{\pi}{4}$,

$$\sin\theta+\cos\theta=\sqrt2\sin\left(\theta+\frac{\pi}{4}\right)=1,$$

so $\sin\left(\theta+\frac{\pi}{4}\right)=\frac{\sqrt2}{2}$. Therefore

$$\theta+\frac{\pi}{4}=\frac{\pi}{4}+2n\pi \quad\text{or}\quad
\theta+\frac{\pi}{4}=\frac{3\pi}{4}+2n\pi,$$

giving $\theta=2n\pi$ or $\theta=\frac{\pi}{2}+2n\pi$.

**Answer.** $\theta=2n\pi$ or $\theta=\dfrac{\pi}{2}+2n\pi$.

**Check.** $\theta=0$: $0+1=1$ ✓. $\theta=\tfrac{\pi}{2}$: $1+0=1$ ✓. These are the two points where
the line $x+y=1$ meets the unit circle, at $(1,0)$ and $(0,1)$ ✓.

### 28.

**Strategy.** Write the left side as $2\sin\left(\theta-\frac{\pi}{3}\right)$ and solve.

Since $\cos\frac{\pi}{3}=\tfrac12$ and $\sin\frac{\pi}{3}=\tfrac{\sqrt3}{2}$,

$$2\sin\left(\theta-\frac{\pi}{3}\right)=1 \iff \sin\left(\theta-\frac{\pi}{3}\right)=\frac12.$$

Hence $\theta-\frac{\pi}{3}=\frac{\pi}{6}+2n\pi$ or $\theta-\frac{\pi}{3}=\frac{5\pi}{6}+2n\pi$, so
$\theta=\frac{\pi}{2}+2n\pi$ or $\theta=\frac{7\pi}{6}+2n\pi$.

**Answer.** $\theta=\dfrac{\pi}{2}+2n\pi$ or $\theta=\dfrac{7\pi}{6}+2n\pi$.

**Check.** $\theta=\tfrac{\pi}{2}$: $1-0=1$ ✓. $\theta=\tfrac{7\pi}{6}$:
$-\tfrac12-\sqrt3\left(-\tfrac{\sqrt3}{2}\right)=-\tfrac12+\tfrac32=1$ ✓.

### 29.

**Strategy.** Factor the left side and solve each basic equation, keeping only $[0,2\pi)$.

$$2\sin^2\theta+\sin\theta=\sin\theta\,(2\sin\theta+1)=0.$$

* $\sin\theta=0$ gives $\theta=0$ or $\theta=\pi$ in $[0,2\pi)$.
* $\sin\theta=-\tfrac12$ gives $\theta=\tfrac{7\pi}{6}$ or $\theta=\tfrac{11\pi}{6}$.

**Answer.** $\theta\in\left\{0,\pi,\dfrac{7\pi}{6},\dfrac{11\pi}{6}\right\}$; four solutions.

**Check.** At $\theta=\tfrac{7\pi}{6}$: $2\cdot\tfrac14-\tfrac12=0$ ✓. At $\theta=\pi$: $0+0=0$ ✓.
The horizontal lines $y=0$ and $y=-\tfrac12$ meet the circle in two points each, giving four
solutions ✓.

### 30.

**Strategy.** Replace $\cos2\theta$ by $1-2\sin^2\theta$ and solve the resulting quadratic.

$$1-2\sin^2\theta=\sin\theta \iff 2\sin^2\theta+\sin\theta-1=0
\iff (2\sin\theta-1)(\sin\theta+1)=0.$$

Thus $\sin\theta=\tfrac12$, giving $\theta=\tfrac{\pi}{6}$ or $\tfrac{5\pi}{6}$ in $[0,2\pi)$, or
$\sin\theta=-1$, giving $\theta=\tfrac{3\pi}{2}$.

**Answer.** $\theta\in\left\{\dfrac{\pi}{6},\dfrac{5\pi}{6},\dfrac{3\pi}{2}\right\}$; three solutions.

**Check.** $\theta=\tfrac{\pi}{6}$: $\cos\tfrac{\pi}{3}=\tfrac12=\sin\tfrac{\pi}{6}$ ✓.
$\theta=\tfrac{5\pi}{6}$: $\cos\tfrac{5\pi}{3}=\tfrac12=\sin\tfrac{5\pi}{6}$ ✓. $\theta=\tfrac{3\pi}{2}$:
$\cos3\pi=-1=\sin\tfrac{3\pi}{2}$ ✓.

### 31.

**Strategy.** Convert the cotangent to a tangent of a complementary angle, then check the two domains.

The equation requires $2\theta\neq\frac{\pi}{2}+m\pi$ and $\sin\theta\neq0$. Using
$\cot\theta=\tan\left(\frac{\pi}{2}-\theta\right)$,

$$2\theta=\frac{\pi}{2}-\theta+n\pi \iff 3\theta=\frac{\pi}{2}+n\pi
\iff \theta=\frac{\pi}{6}+\frac{n\pi}{3}.$$

* Is $\theta$ ever a multiple of $\pi$? The equation $\frac{1}{6}+\frac{n}{3}=m$ is
  $1+2n=6m$, with odd left side and even right side: impossible.
* Is $2\theta$ ever $\frac{\pi}{2}+m\pi$? The equation $\frac{1}{3}+\frac{2n}{3}=\frac{1}{2}+m$ is
  $2+4n=3+6m$: again odd equals even, impossible.

So every value of the family is admissible.

**Answer.** $\theta=\dfrac{\pi}{6}+\dfrac{n\pi}{3}$, $n\in\mathbb{Z}$; in $[0,2\pi)$:
$\tfrac{\pi}{6},\tfrac{\pi}{2},\tfrac{5\pi}{6},\tfrac{7\pi}{6},\tfrac{3\pi}{2},\tfrac{11\pi}{6}$.

**Check.** $\theta=\tfrac{\pi}{6}$: $\tan\tfrac{\pi}{3}=\sqrt3=\cot\tfrac{\pi}{6}$ ✓.
$\theta=\tfrac{\pi}{2}$: $\tan\pi=0=\cot\tfrac{\pi}{2}$ ✓.

### 32.

**Strategy.** Convert the secant to a cosine, then take both signs of the square root.

$$\sec^2\theta=4 \iff \frac{1}{\cos^2\theta}=4 \iff \cos^2\theta=\frac14
\iff \cos\theta=\frac12 \ \text{ or }\ \cos\theta=-\frac12.$$

The first gives $\theta=\pm\tfrac{\pi}{3}+2n\pi$; the second gives $\theta=\pm\tfrac{2\pi}{3}+2n\pi$.
Combining, the four families reduce to

$$\theta=\pm\frac{\pi}{3}+n\pi,\qquad n\in\mathbb{Z}.$$

**Answer.** $\theta=\pm\dfrac{\pi}{3}+n\pi$.

**Check.** In $[0,2\pi)$ the combined family gives $\tfrac{\pi}{3},\tfrac{2\pi}{3},\tfrac{4\pi}{3},
\tfrac{5\pi}{3}$, and $\cos^2\theta=\tfrac14$ at each ✓. At $\theta=\tfrac{\pi}{3}$, $\sec\theta=2$,
so $\sec^2\theta=4$ ✓.

## Challenge

### 33.

**Strategy.** Convert the difference of the two sines into a product.

$$\sin3\theta-\sin5\theta=2\cos\frac{8\theta}{2}\sin\frac{3\theta-5\theta}{2}
=2\cos4\theta\,\sin(-\theta)=-2\cos4\theta\,\sin\theta.$$

Hence $\sin\theta=0$, giving $\theta=n\pi$, or $\cos4\theta=0$, giving
$4\theta=\frac{\pi}{2}+n\pi$ and $\theta=\frac{\pi}{8}+\frac{n\pi}{4}$.

**Answer.** $\theta=n\pi$ or $\theta=\dfrac{\pi}{8}+\dfrac{n\pi}{4}$, $n\in\mathbb{Z}$.

**Check.** $\theta=\tfrac{\pi}{8}$: $\sin\tfrac{3\pi}{8}\approx0.9239=\sin\tfrac{5\pi}{8}$ ✓.
$\theta=\tfrac{3\pi}{8}$: $\sin\tfrac{9\pi}{8}=\sin\tfrac{15\pi}{8}\approx-0.3827$, both equal ✓.
The families are disjoint: $\tfrac{1}{8}+\tfrac{n}{4}=m$ would give $1+2n=8m$, odd equals even. In
$[0,2\pi)$ there are ten solutions: $0,\pi$ and eight from the second family.

### 34.

**Strategy.** Divide by $\cos^2\theta$ after proving $\cos\theta\neq0$, then solve the quadratic in
$\tan\theta$.

If $\cos\theta=0$ then $\sin\theta=\pm1$ and the left side equals $2\sin^2\theta=2\neq0$, so no
solution has $\cos\theta=0$. Dividing by $\cos^2\theta$ is therefore legitimate and gives

$$2\tan^2\theta+3\tan\theta+1=0 \iff (2\tan\theta+1)(\tan\theta+1)=0.$$

Thus $\tan\theta=-1$, giving $\theta=-\frac{\pi}{4}+n\pi$, or $\tan\theta=-\frac12$, giving
$\theta=\arctan\left(-\frac12\right)+n\pi=-\arctan\frac12+n\pi$.

**Answer.** $\theta=-\dfrac{\pi}{4}+n\pi$ or $\theta=-\arctan\dfrac12+n\pi$, $n\in\mathbb{Z}$.

**Check.** For $\tan\theta=-1$ write $\sin\theta=-\cos\theta$; then
$2\cos^2\theta-3\cos^2\theta+\cos^2\theta=0$ ✓. For $\tan\theta=-\tfrac12$ write
$\sin\theta=-\tfrac12\cos\theta$; then
$2\cdot\tfrac14\cos^2\theta-\tfrac32\cos^2\theta+\cos^2\theta=0$ ✓. Numerically,
$\arctan\frac12\approx0.4636$, and at $\theta=-0.4636$ the expression evaluates to $0$ ✓.

### 35.

**Strategy.** Group the first and third terms, whose sum is a product containing $\cos2\theta$.

$$\cos\theta+\cos3\theta=2\cos2\theta\cos\theta,$$

so

$$\cos\theta+\cos2\theta+\cos3\theta=\cos2\theta\,(2\cos\theta+1)=0.$$

Hence $\cos2\theta=0$, giving $2\theta=\frac{\pi}{2}+n\pi$ and $\theta=\frac{\pi}{4}+\frac{n\pi}{2}$, or
$\cos\theta=-\frac12$, giving $\theta=\pm\frac{2\pi}{3}+2n\pi$.

**Answer.** $\theta=\dfrac{\pi}{4}+\dfrac{n\pi}{2}$ or $\theta=\pm\dfrac{2\pi}{3}+2n\pi$.

**Check.** $\theta=\tfrac{\pi}{4}$: $\tfrac{\sqrt2}{2}+0-\tfrac{\sqrt2}{2}=0$ ✓.
$\theta=\tfrac{2\pi}{3}$: $-\tfrac12-\tfrac12+1=0$ ✓. In $[0,2\pi)$ there are six solutions.

### 36.

**Strategy.** Read the amplitude, mean and period, then solve the two basic sine equations and filter
to $[0,24)$.

Here $A=3$, $D=5$, $B=\frac{\pi}{6}$ and the period is $\frac{2\pi}{B}=12$ hours.

**(a)** The maximum depth is $D+\lvert A\rvert=8$ m, attained when $\sin\frac{\pi t}{6}=1$:

$$\frac{\pi t}{6}=\frac{\pi}{2}+2n\pi \iff t=3+12n.$$

In $[0,24)$ this gives $t=3$ and $t=15$, that is 03:00 and 15:00.

The minimum is $D-\lvert A\rvert=2$ m, attained when $\sin\frac{\pi t}{6}=-1$:

$$\frac{\pi t}{6}=\frac{3\pi}{2}+2n\pi \iff t=9+12n,$$

giving $t=9$ and $t=21$, that is 09:00 and 21:00.

**(b)** Set $d(t)=6.5$:

$$5+3\sin\frac{\pi t}{6}=6.5 \iff \sin\frac{\pi t}{6}=\frac12
\iff \frac{\pi t}{6}=\frac{\pi}{6}+2n\pi \ \text{ or }\ \frac{5\pi}{6}+2n\pi.$$

Hence $t=1+12n$ or $t=5+12n$. In $[0,24)$ the solutions are $t=1,5,13,17$, that is 01:00, 05:00,
13:00 and 17:00.

**Answer.** (a) Maximum $8$ m at 03:00 and 15:00; minimum $2$ m at 09:00 and 21:00. (b) Depth
$6.5$ m at 01:00, 05:00, 13:00 and 17:00.

**Check.** At $t=1$: $\sin\frac{\pi}{6}=\tfrac12$, so $d=5+1.5=6.5$ ✓. At $t=13$:
$\sin\frac{13\pi}{6}=\sin\frac{\pi}{6}=\tfrac12$ ✓. Each level between the minimum and the maximum is
crossed twice per $12$-hour period, so four crossings in $24$ hours is correct.

### 37.

**Strategy.** Fit the four parameters from the minimum and maximum, then solve the resulting cosine
equation.

**(a)** The amplitude is half the range:
$A=\frac{20-8}{2}=6$. The mean is $D=\frac{20+8}{2}=14$. The time from minimum to maximum is $12$
hours, so the period is $24$ hours and $B=\frac{2\pi}{24}=\frac{\pi}{12}$.

**(b)** A maximum at $t=16$ suits the cosine form:
$$T(t)=14+6\cos\frac{\pi(t-16)}{12}.$$

**(c)** Set $T(t)=17$:

$$14+6\cos\frac{\pi(t-16)}{12}=17
\iff \cos\frac{\pi(t-16)}{12}=\frac12
\iff \frac{\pi(t-16)}{12}=\pm\frac{\pi}{3}+2n\pi.$$

Thus $t-16=\pm4+24n$, so $t=20+24n$ or $t=12+24n$. In $[0,24)$ the solutions are $t=12$ and $t=20$,
that is 12:00 and 20:00. The temperature is $17^\circ$C at noon (rising) and at 20:00 (falling).

**(d)** The maximum $20^\circ$C occurs when $\cos\frac{\pi(t-16)}{12}=1$, that is $t=16+24n$: 16:00.
The minimum $8^\circ$C occurs when the cosine is $-1$, that is $t-16=12+24n$ or $t=4+24n$: 04:00.

**Answer.** (a) Amplitude $6^\circ$C, mean $14^\circ$C, period $24$ h, $B=\frac{\pi}{12}$.
(b) $T(t)=14+6\cos\frac{\pi(t-16)}{12}$. (c) 12:00 and 20:00. (d) Maximum at 16:00, minimum at 04:00.

**Check.** At $t=4$: $\cos\frac{\pi(-12)}{12}=\cos(-\pi)=-1$, so $T=8$ ✓. At $t=16$: $\cos0=1$, so
$T=20$ ✓. At $t=12$ and $t=20$ the cosine is $\tfrac12$, so $T=17$ ✓ — the two answers sit
symmetrically four hours before and after the maximum at 16:00.

### 38.

**(a) The error: division by $\sin\theta$.** The step assumes $\sin\theta\neq0$, but $\sin\theta=0$
produces solutions. Correct solution:

$$\sin\theta\cos\theta=\sin\theta \iff \sin\theta(\cos\theta-1)=0.$$

Hence $\sin\theta=0$, giving $\theta=n\pi$, or $\cos\theta=1$, giving $\theta=2n\pi$. The second family
is contained in the first, so the complete answer is $\theta=n\pi$. The student's answer
$\theta=2n\pi$ contains only the even multiples of $\pi$ and loses every odd multiple, such as
$\theta=\pi$, which plainly satisfies $\sin\pi\cos\pi=0=\sin\pi$. The principle violated is: *never
divide by an expression that can be zero; factor instead.*

**(b) The error: using the period of sine or cosine for tangent.** Tangent repeats every $\pi$, not
every $2\pi$. The correct general solution is $\theta=\frac{\pi}{3}+n\pi$; in $[0,2\pi)$ this gives
$\theta=\frac{\pi}{3}$ and $\theta=\frac{4\pi}{3}$. The student reported only the principal value and
lost the solution half a turn later, where $\tan\frac{4\pi}{3}=\sqrt3$ as well.

**(c) The error: losing the second family.** The equation $\sin2\theta=\frac12$ has two families in
one full turn of $2\theta$:
$$2\theta=\frac{\pi}{6}+2n\pi \quad\text{or}\quad 2\theta=\frac{5\pi}{6}+2n\pi.$$
Dividing by $2$ gives
$$\theta=\frac{\pi}{12}+n\pi \quad\text{or}\quad \theta=\frac{5\pi}{12}+n\pi.$$
The student's period $n\pi$ is correct (since $\frac{2n\pi}{2}=n\pi$), but the family beginning at
$\frac{5\pi}{12}$ is missing. On the unit circle, the horizontal line $y=\frac12$ meets the circle
twice, so both families must appear. As a check, $\theta=\frac{5\pi}{12}$ gives
$\sin\frac{5\pi}{6}=\frac12$, which the student's answer omits.

**Check of the corrected answers.** (a) $\theta=\pi$: $\sin\pi\cos\pi=0=\sin\pi$ ✓.
(b) $\tan\frac{4\pi}{3}=\sqrt3$ ✓. (c) $\theta=\frac{5\pi}{12}$: $\sin\frac{5\pi}{6}=\frac12$ ✓.
