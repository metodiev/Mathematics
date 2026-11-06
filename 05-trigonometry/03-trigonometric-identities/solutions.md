# Trigonometric Identities — Solutions

> [Tutorial](README.md) · [Exercises](exercises.md) · 38 worked solutions

Each solution states the strategy first, then carries out every step, then checks the result. Where a
problem asks for a proof, the domain is stated explicitly. Decimal values are given to four places and
are checks, not substitutes for the exact answers.

## Beginner

### 1.

**Strategy.** The Pythagorean identity gives the magnitude of the missing function; the quadrant gives
its sign.

$$\cos^2\theta=1-\sin^2\theta=1-\frac{49}{625}=\frac{576}{625}.$$

Since $\theta$ is acute, $\cos\theta>0$, so $\cos\theta=\dfrac{24}{25}$. Then

$$\tan\theta=\frac{\sin\theta}{\cos\theta}=\frac{7/25}{24/25}=\frac{7}{24}.$$

**Answer.** $\cos\theta=\dfrac{24}{25}$, $\tan\theta=\dfrac{7}{24}$. Check: $7^2+24^2=625=25^2$.

### 2.

**Strategy.** The same as Problem 1, with the sign taken from the third quadrant.

$$\sin^2\theta=1-\cos^2\theta=1-\frac{64}{289}=\frac{225}{289}.$$

In the third quadrant both coordinates are negative, so $\sin\theta=-\dfrac{15}{17}$. Hence

$$\tan\theta=\frac{\sin\theta}{\cos\theta}=\frac{-15/17}{-8/17}=\frac{15}{8}.$$

**Answer.** $\sin\theta=-\dfrac{15}{17}$, $\tan\theta=\dfrac{15}{8}$. Both are consistent with the
third quadrant, where tangent is positive.

### 3.

**Strategy.** Write the secant as a reciprocal, then cancel.

$$\sec\theta\cos\theta=\frac{1}{\cos\theta}\cdot\cos\theta=1.$$

**Answer.** $1$, for $\cos\theta\neq0$, that is $\theta\neq\dfrac{\pi}{2}+k\pi$ for $k\in\mathbb{Z}$.
The cancellation is legitimate precisely because $\cos\theta\neq0$ on the stated domain.

### 4.

**Strategy.** Convert the numerator with the Pythagorean identity, then write the result as a single
function.

$$\frac{1-\sin^2\theta}{\sin^2\theta}=\frac{\cos^2\theta}{\sin^2\theta}=\cot^2\theta.$$

**Answer.** $\cot^2\theta$, defined for $\sin\theta\neq0$, that is $\theta\neq k\pi$.

### 5.

**Strategy.** Convert both functions to sine and cosine.

$$\frac{\tan\theta}{\sec\theta}
=\frac{\sin\theta/\cos\theta}{1/\cos\theta}
=\frac{\sin\theta}{\cos\theta}\cdot\frac{\cos\theta}{1}
=\sin\theta.$$

**Answer.** $\sin\theta$, for $\cos\theta\neq0$. Note that the result is defined even at points where
the original expression is not (for example $\cos\theta=0$), which is why the domain must be carried
along: the simplification is an identity only on the original domain.

### 6.

**Strategy.** Use the quotient identity for cotangent.

$$\sin\theta\cot\theta=\sin\theta\cdot\frac{\cos\theta}{\sin\theta}=\cos\theta.$$

**Answer.** $\cos\theta$, for $\sin\theta\neq0$.

### 7.

**Strategy.** Invert the cosecant first, then use the companion Pythagorean identity.

$$\sin\theta=\frac{1}{\csc\theta}=\frac35.$$

Since $\theta$ is acute, $\cos\theta=\sqrt{1-\tfrac{9}{25}}=\dfrac45$, and

$$\cot\theta=\frac{\cos\theta}{\sin\theta}=\frac{4/5}{3/5}=\frac43.$$

Equivalently, $\cot^2\theta=\csc^2\theta-1=\dfrac{25}{9}-1=\dfrac{16}{9}$ and $\cot\theta>0$.

**Answer.** $\cot\theta=\dfrac43$.

### 8.

**Strategy.** Write $15^\circ=45^\circ-30^\circ$ and use the sine difference formula.

$$\begin{aligned}
\sin15^\circ&=\sin(45^\circ-30^\circ)\\
&=\sin45^\circ\cos30^\circ-\cos45^\circ\sin30^\circ\\
&=\frac{\sqrt2}{2}\cdot\frac{\sqrt3}{2}-\frac{\sqrt2}{2}\cdot\frac12
=\frac{\sqrt6-\sqrt2}{4}.
\end{aligned}$$

**Answer.** $\dfrac{\sqrt6-\sqrt2}{4}\approx0.2588$. Since $15^\circ$ is in the first quadrant, the
answer must be positive, and $\sqrt6>\sqrt2$ confirms it.

### 9.

**Strategy.** Write $75^\circ=45^\circ+30^\circ$ and use the cosine sum formula; alternatively use
$\cos75^\circ=\sin15^\circ$.

$$\begin{aligned}
\cos75^\circ&=\cos(45^\circ+30^\circ)\\
&=\cos45^\circ\cos30^\circ-\sin45^\circ\sin30^\circ\\
&=\frac{\sqrt2}{2}\cdot\frac{\sqrt3}{2}-\frac{\sqrt2}{2}\cdot\frac12
=\frac{\sqrt6-\sqrt2}{4}.
\end{aligned}$$

**Answer.** $\dfrac{\sqrt6-\sqrt2}{4}\approx0.2588$. The cofunction identity
$\cos75^\circ=\sin(90^\circ-75^\circ)=\sin15^\circ$ gives the same value, as it must.

### 10.

**Strategy.** Write $105^\circ=60^\circ+45^\circ$ and use the tangent sum formula. The angle is in the
second quadrant, so the answer must be negative.

$$\tan105^\circ=\frac{\tan60^\circ+\tan45^\circ}{1-\tan60^\circ\tan45^\circ}
=\frac{\sqrt3+1}{1-\sqrt3}.$$

Rationalise by multiplying numerator and denominator by $1+\sqrt3$:

$$\frac{(\sqrt3+1)(1+\sqrt3)}{(1-\sqrt3)(1+\sqrt3)}
=\frac{(\sqrt3+1)^2}{1-3}
=\frac{4+2\sqrt3}{-2}=-(2+\sqrt3).$$

**Answer.** $-(2+\sqrt3)\approx-3.7321$, negative as required for a second-quadrant angle.

### 11.

**Strategy.** Find the missing sine and cosine from the Pythagorean identity, then apply the sine sum
formula.

$\sin\alpha=\dfrac{5}{13}$ with $\alpha$ acute gives $\cos\alpha=\dfrac{12}{13}$.
$\cos\beta=\dfrac45$ with $\beta$ acute gives $\sin\beta=\dfrac35$.

$$\begin{aligned}
\sin(\alpha+\beta)&=\sin\alpha\cos\beta+\cos\alpha\sin\beta\\
&=\frac{5}{13}\cdot\frac45+\frac{12}{13}\cdot\frac35
=\frac{20}{65}+\frac{36}{65}=\frac{56}{65}.
\end{aligned}$$

**Answer.** $\dfrac{56}{65}\approx0.8615$. Check: $\alpha\approx22.62^\circ$,
$\beta\approx36.87^\circ$, and $\sin59.49^\circ\approx0.8615$.

### 12.

**Strategy.** The double-angle formulas need both $\sin\theta$ and $\cos\theta$.

$\cos\theta=\dfrac35$ with $\theta$ acute gives $\sin\theta=\dfrac45$. Then

$$\sin2\theta=2\sin\theta\cos\theta=2\cdot\frac45\cdot\frac35=\frac{24}{25},$$

$$\cos2\theta=\cos^2\theta-\sin^2\theta=\frac{9}{25}-\frac{16}{25}=-\frac{7}{25}.$$

**Answer.** $\sin2\theta=\dfrac{24}{25}$, $\cos2\theta=-\dfrac{7}{25}$. Check:
$\left(\tfrac{24}{25}\right)^2+\left(\tfrac{7}{25}\right)^2=\dfrac{576+49}{625}=1$. The angle
$2\theta\approx106.3^\circ$ is in the second quadrant, so a negative cosine is correct.

## Intermediate

### 13.

**Strategy.** Expand the square; the cross term is the only non-obvious piece, and the two squares
combine by the Pythagorean identity.

$$\begin{aligned}
(\sin x+\cos x)^2
&=\sin^2x+2\sin x\cos x+\cos^2x\\
&=(\sin^2x+\cos^2x)+2\sin x\cos x\\
&=1+2\sin x\cos x.
\end{aligned}$$

**Domain.** All real $x$. No division occurs, so no value is excluded.

### 14.

**Strategy.** Convert each factor separately into a single trigonometric square, then multiply.

$$1-\cos^2x=\sin^2x,\qquad 1+\cot^2x=\csc^2x.$$

Therefore

$$(1-\cos^2x)(1+\cot^2x)=\sin^2x\cdot\frac{1}{\sin^2x}=1.$$

**Domain.** $\sin x\neq0$ (the cotangent and cosecant are undefined there), that is
$x\neq k\pi$. At $x=k\pi$ the left side is $0\cdot(\text{undefined})$, so the expression is not
defined and nothing is claimed there.

### 15.

**Strategy.** Convert both terms to sine and cosine, then add the fractions with common denominator
$\sin x\cos x$.

$$\begin{aligned}
\tan x+\cot x
&=\frac{\sin x}{\cos x}+\frac{\cos x}{\sin x}\\
&=\frac{\sin^2x+\cos^2x}{\sin x\cos x}
=\frac{1}{\sin x\cos x}\\
&=\frac{1}{\cos x}\cdot\frac{1}{\sin x}=\sec x\csc x.
\end{aligned}$$

**Domain.** $\sin x\neq0$ and $\cos x\neq0$.

### 16.

**Strategy.** Recognise a difference of squares and then use the companion Pythagorean identity.

$$(\sec x-\tan x)(\sec x+\tan x)=\sec^2x-\tan^2x.$$

Since $1+\tan^2x=\sec^2x$, the right side equals $1$.

**Domain.** $\cos x\neq0$, that is $x\neq\dfrac{\pi}{2}+k\pi$.

**Remark.** This identity shows that $\sec x-\tan x$ and $\sec x+\tan x$ are reciprocals. The same
fact appears again in Problem 34.

### 17.

**Strategy.** Factor $\sin x$ out of the numerator; the remaining factor is the Pythagorean identity.

$$\frac{\sin^3x+\sin x\cos^2x}{\cos x}
=\frac{\sin x(\sin^2x+\cos^2x)}{\cos x}
=\frac{\sin x}{\cos x}=\tan x.$$

**Domain.** $\cos x\neq0$.

### 18.

**Strategy.** Use the product-to-sum formula
$\sin\alpha\cos\beta=\tfrac12[\sin(\alpha+\beta)+\sin(\alpha-\beta)]$ with $\alpha=4x$ and
$\beta=2x$.

$$\sin4x\cos2x=\tfrac12\bigl[\sin6x+\sin2x\bigr].$$

**Check.** At $x=0.37$: $\sin(6x)=\sin2.22=0.79657$ and $\sin(2x)=\sin0.74=0.67429$, so the right
side is $\tfrac12(1.47086)=0.73543$; the left side is $\sin1.48\cos0.74=0.99600\cdot0.73847=0.73543$.

### 19.

**Strategy.** Use
$\cos\alpha\cos\beta=\tfrac12[\cos(\alpha+\beta)+\cos(\alpha-\beta)]$ with $\alpha=5\theta$ and
$\beta=3\theta$.

$$\cos5\theta\cos3\theta=\tfrac12\bigl[\cos8\theta+\cos2\theta\bigr].$$

**Check.** At $\theta=0.5$: $\cos2.5=-0.80114$ and $\cos1.5=0.07074$, so the left side is
$-0.05667$; the right side is $\tfrac12[\cos4+\cos1]=\tfrac12[-0.65364+0.54030]=-0.05667$.

### 20.

**Strategy.** Use
$\sin u+\sin v=2\sin\dfrac{u+v}{2}\cos\dfrac{u-v}{2}$ with $u=7x$, $v=3x$.

$$\sin7x+\sin3x=2\sin5x\cos2x.$$

**Check.** At $x=0.31$: $\sin2.17=0.82578$ and $\sin0.93=0.80162$, so the left side is $1.62740$;
the right side is $2\sin1.55\cos0.62=2\cdot0.99978\cdot0.81388=1.62740$.

### 21.

**Strategy.** Use
$\cos u-\cos v=-2\sin\dfrac{u+v}{2}\sin\dfrac{u-v}{2}$ with $u=4x$, $v=2x$. The minus sign is part
of the formula.

$$\cos4x-\cos2x=-2\sin3x\sin x.$$

**Check.** At $x=0.4$: $\cos1.6=-0.02920$, $\cos0.8=0.69671$, difference $=-0.72591$; the right side
is $-2\sin1.2\sin0.4=-2(0.93204)(0.38942)=-0.72591$.

### 22.

**Strategy.** Use the half-angle formula for cosine with $x=45^\circ$, so that $x/2=22.5^\circ$. The
angle $22.5^\circ$ is in the first quadrant, so the positive root is taken.

$$\cos^222.5^\circ=\frac{1+\cos45^\circ}{2}=\frac{1+\tfrac{\sqrt2}{2}}{2}
=\frac{2+\sqrt2}{4}.$$

Therefore

$$\cos22.5^\circ=\frac{\sqrt{2+\sqrt2}}{2}.$$

**Answer.** $\dfrac{\sqrt{2+\sqrt2}}{2}\approx0.9239$. Check:
$\cos^222.5^\circ=\dfrac{2+\sqrt2}{4}=0.85355$ and $0.9239^2=0.85359$.

### 23.

**Strategy.** Convert the tangent into a point on the unit circle, then double the angle.

Since $\tan\theta=\dfrac34$ and $\theta$ is in the third quadrant, the reference triangle has
opposite $3$, adjacent $4$, hypotenuse $5$, and both coordinates are negative:
$\sin\theta=-\dfrac35$, $\cos\theta=-\dfrac45$. Then

$$\sin2\theta=2\sin\theta\cos\theta=2\left(-\frac35\right)\left(-\frac45\right)=\frac{24}{25}.$$

**Answer.** $\dfrac{24}{25}=0.96$. Since $\theta\approx216.87^\circ$, $2\theta\approx433.74^\circ$,
which is coterminal with $73.74^\circ$ in the first quadrant; the sine is positive and close to $1$,
as the answer indicates.

### 24.

**Strategy.** Use the rational half-angle form $\tan\dfrac{\theta}{2}=\dfrac{1-\cos\theta}{\sin\theta}$,
which needs no sign decision.

$\sin\theta=\dfrac{8}{17}$ with $\theta$ in the second quadrant gives
$\cos\theta=-\dfrac{15}{17}$. Hence

$$\tan\frac{\theta}{2}=\frac{1-\left(-\dfrac{15}{17}\right)}{\dfrac{8}{17}}
=\frac{\dfrac{32}{17}}{\dfrac{8}{17}}=4.$$

**Answer.** $4$. Check: $\theta\approx151.93^\circ$, so $\theta/2\approx75.97^\circ$ and
$\tan75.97^\circ\approx3.999$. The result is positive, consistent with $\theta/2$ in the first
quadrant.

## Advanced

### 25.

**Strategy.** Expand the double angle in the numerator and in the denominator, both in terms of
$\cos x$ and $\sin x$, then cancel.

$$\frac{1+\cos2x}{\sin2x}
=\frac{1+(2\cos^2x-1)}{2\sin x\cos x}
=\frac{2\cos^2x}{2\sin x\cos x}
=\frac{\cos x}{\sin x}=\cot x.$$

**Domain.** $\sin2x\neq0$, that is $x\neq\dfrac{k\pi}{2}$. At those points either $\sin x=0$ (where
$\cot x$ is undefined) or $\cos x=0$ (where the fraction is undefined).

### 26.

**Strategy.** Split $3x$ as $2x+x$, apply the sine sum formula, then convert the double-angle terms so
that everything is a power of $\sin x$.

$$\begin{aligned}
\sin3x&=\sin(2x+x)\\
&=\sin2x\cos x+\cos2x\sin x\\
&=(2\sin x\cos x)\cos x+(1-2\sin^2x)\sin x\\
&=2\sin x\cos^2x+\sin x-2\sin^3x\\
&=2\sin x(1-\sin^2x)+\sin x-2\sin^3x\\
&=2\sin x-2\sin^3x+\sin x-2\sin^3x\\
&=3\sin x-4\sin^3x.
\end{aligned}$$

**Domain.** All real $x$.

**Check.** At $x=\pi/6$: $\sin(\pi/2)=1$ and $3\cdot\tfrac12-4\cdot\tfrac18=1.5-0.5=1$.

### 27.

**Strategy.** Apply the tangent addition formula with $\alpha=x$ and $\beta=\pi/4$, using
$\tan\dfrac{\pi}{4}=1$.

$$\tan\left(x+\frac{\pi}{4}\right)
=\frac{\tan x+\tan\frac{\pi}{4}}{1-\tan x\tan\frac{\pi}{4}}
=\frac{\tan x+1}{1-\tan x}.$$

**Domain.** $\cos x\neq0$, $\cos\left(x+\dfrac{\pi}{4}\right)\neq0$ (that is
$x\neq\dfrac{\pi}{4}+k\pi$), and $\tan x\neq1$.

### 28.

**Strategy.** Expand both double angles with $1-\cos2x=2\sin^2x$ and $1+\cos2x=2\cos^2x$.

$$\frac{1-\cos2x}{1+\cos2x}=\frac{2\sin^2x}{2\cos^2x}=\tan^2x.$$

**Domain.** $\cos x\neq0$, that is $x\neq\dfrac{\pi}{2}+k\pi$; at those points the denominator
$1+\cos2x=2\cos^2x$ vanishes and neither side is defined.

### 29.

**Strategy.** Factor the difference of squares, then use the Pythagorean identity.

$$\cos^4x-\sin^4x=(\cos^2x-\sin^2x)(\cos^2x+\sin^2x)=\cos2x\cdot1=\cos2x.$$

**Domain.** All real $x$.

**Check.** At $x=1$: $\cos1=0.54030$, so $\cos^41=0.08522$; $\sin1=0.84147$, so $\sin^41=0.50137$.
The difference is $-0.41615$, and $\cos2=-0.41615$. At $x=\pi/4$ both sides are $0$.

### 30.

**Strategy.** Eliminate $C$ with $C=\pi-(A+B)$, then convert everything to the elementary symmetric
quantities $\cos A\cos B$ and $\sin A\sin B$.

Since $\cos C=-\cos(A+B)$ and $\cos(A+B)=\cos A\cos B-\sin A\sin B$, write
$x=\cos A$, $y=\cos B$, $p=\sin A$, $q=\sin B$. Then

$$\begin{aligned}
&\cos^2A+\cos^2B+\cos^2C+2\cos A\cos B\cos C\\
&\quad=x^2+y^2+(xy-pq)^2-2xy(xy-pq)\\
&\quad=x^2+y^2+x^2y^2-2xypq+p^2q^2-2x^2y^2+2xypq\\
&\quad=x^2+y^2-x^2y^2+p^2q^2.
\end{aligned}$$

Now $p^2=1-x^2$ and $q^2=1-y^2$, so

$$p^2q^2=(1-x^2)(1-y^2)=1-x^2-y^2+x^2y^2.$$

Substituting,

$$x^2+y^2-x^2y^2+1-x^2-y^2+x^2y^2=1.$$

**Domain.** All triangles, including degenerate limiting cases where an angle tends to $0$ or $\pi$;
the algebra uses no division.

**Check.** Equilateral triangle: $3\left(\tfrac12\right)^2+2\left(\tfrac12\right)^3=0.75+0.25=1$.

### 31.

**Strategy.** Use the tangent addition formula on $A+B$ and replace $\tan(A+B)$ by $-\tan C$. The
hypothesis that no angle is a right angle is what makes all three tangents exist.

$$\tan(A+B)=\frac{\tan A+\tan B}{1-\tan A\tan B}.$$

Because $A+B=\pi-C$ and $\tan(\pi-C)=-\tan C$,

$$\frac{\tan A+\tan B}{1-\tan A\tan B}=-\tan C.$$

Multiplying by $1-\tan A\tan B$ (nonzero, since $\tan(A+B)$ is defined),

$$\tan A+\tan B=-\tan C+\tan A\tan B\tan C,$$

and rearranging gives

$$\tan A+\tan B+\tan C=\tan A\tan B\tan C.$$

**Check.** $A=B=C=60^\circ$: the left side is $3\sqrt3=5.19615$; the right side is
$(\sqrt3)^3=3\sqrt3=5.19615$.

### 32.

**Strategy.** Take the tangent of both sides of $A+B=\dfrac{\pi}{4}$ and rearrange.

$$\tan(A+B)=\tan\frac{\pi}{4}=1,$$

so

$$\frac{\tan A+\tan B}{1-\tan A\tan B}=1.$$

Multiplying by the denominator (nonzero because $\tan(A+B)$ is defined),

$$\tan A+\tan B=1-\tan A\tan B,$$

hence

$$\tan A+\tan B+\tan A\tan B=1.$$

Adding $1$ to both sides,

$$1+\tan A+\tan B+\tan A\tan B=2,$$

and the left side factors as $(1+\tan A)(1+\tan B)$. Therefore
$(1+\tan A)(1+\tan B)=2$.

**Check.** $A=20^\circ$, $B=25^\circ$: $\tan20^\circ=0.36397$, $\tan25^\circ=0.46631$, and
$1.36397\cdot1.46631=2.0000$.

### 33.

**Strategy.** First combine the two factors whose angles differ, using
$\sin(A-B)\sin(A+B)=\sin^2A-\sin^2B$ with $A=60^\circ$, $B=x$. Then recognise the triple-angle
formula from Problem 26.

**Step 1: the product of the two sines.** By product-to-sum,

$$\sin(60^\circ-x)\sin(60^\circ+x)
=\tfrac12\bigl[\cos(2x)-\cos120^\circ\bigr].$$

Since $\cos120^\circ=-\tfrac12$ and $\cos2x=1-2\sin^2x$,

$$=\tfrac12\left[1-2\sin^2x+\tfrac12\right]=\tfrac34-\sin^2x.$$

Equivalently, $\sin^2 60^\circ-\sin^2x=\tfrac34-\sin^2x$.

**Step 2: multiply by $\sin x$.**

$$\sin x\left(\tfrac34-\sin^2x\right)=\tfrac34\sin x-\sin^3x
=\tfrac14\left(3\sin x-4\sin^3x\right)=\tfrac14\sin3x,$$

using Problem 26 in the last step.

**Domain.** All real $x$.

**Check.** At $x=10^\circ$: the left side is
$\sin10^\circ\sin50^\circ\sin70^\circ=0.17365\cdot0.76604\cdot0.93969=0.12500$; the right side is
$\tfrac14\sin30^\circ=0.125$.

## Challenge

### 34.

**Strategy.** The right side contains $\sec x+\tan x$, which is $\dfrac{1+\sin x}{\cos x}$. Square it
and simplify; the Pythagorean identity then produces the left side.

$$\begin{aligned}
(\sec x+\tan x)^2
&=\left(\frac{1}{\cos x}+\frac{\sin x}{\cos x}\right)^2\\
&=\left(\frac{1+\sin x}{\cos x}\right)^2
=\frac{(1+\sin x)^2}{\cos^2x}\\
&=\frac{(1+\sin x)^2}{1-\sin^2x}
=\frac{(1+\sin x)^2}{(1-\sin x)(1+\sin x)}\\
&=\frac{1+\sin x}{1-\sin x}.
\end{aligned}$$

**Domain.** $\cos x\neq0$ (for $\sec x$ and $\tan x$) and $\sin x\neq1$ (for the left side and for the
cancellation). Both conditions say $x\neq\dfrac{\pi}{2}+k\pi$, so the domain is
$\mathbb{R}\setminus\left\{\dfrac{\pi}{2}+k\pi:k\in\mathbb{Z}\right\}$.

**Second approach.** Multiply the left side by $\dfrac{\cos^2x}{\cos^2x}$ and observe that
$\dfrac{1+\sin x}{\cos x}=\sec x+\tan x$; squaring recovers the right side. The approach above is
preferable because it never assumes the result.

### 35.

**(a) Strategy.** Use the factorisation $s^3+c^3=(s+c)(s^2-sc+c^2)$ with $s=\sin x$, $c=\cos x$,
and express $sc$ through $k^2=(s+c)^2=1+2sc$.

From $k^2=1+2\sin x\cos x$ we get

$$\sin x\cos x=\frac{k^2-1}{2}.$$

Also $s^2-sc+c^2=1-sc$. Therefore

$$\begin{aligned}
\sin^3x+\cos^3x
&=k\left(1-\frac{k^2-1}{2}\right)
=k\cdot\frac{2-k^2+1}{2}
=\frac{k(3-k^2)}{2}.
\end{aligned}$$

**Answer (a).** $\sin^3x+\cos^3x=\dfrac{k(3-k^2)}{2}$.

**(b)** Since $k=\sin x+\cos x=\sqrt2\sin\left(x+\dfrac{\pi}{4}\right)$ and sine takes every value in
$[-1,1]$, the possible values of $k$ are exactly the interval $[-\sqrt2,\sqrt2]$. Equivalently,
$k^2=1+2\sin x\cos x\in[0,2]$ because $\sin x\cos x=\tfrac12\sin2x\in\left[-\tfrac12,\tfrac12\right]$.

For $k\in[-\sqrt2,\sqrt2]$ we have $k^2\le2$, hence $3-k^2\ge1>0$, so the expression in part (a) is
real. Its values fill the interval $[-1,1]$: the bound
$\lvert\sin^3x+\cos^3x\rvert\le\lvert\sin x\rvert^3+\lvert\cos x\rvert^3\le\sin^2x+\cos^2x=1$
holds for every $x$, and the values $\pm1$ are attained at $x=0$ and $x=\pi$. In terms of $k$, the
function $\tfrac12k(3-k^2)$ has maximum $1$ at $k=1$ and minimum $-1$ at $k=-1$.

**Check.** $x=\dfrac{\pi}{4}$: $k=\sqrt2$, $\sin^3+\cos^3=2\left(\dfrac{\sqrt2}{2}\right)^3=\dfrac{\sqrt2}{2}$,
and $\dfrac{\sqrt2(3-2)}{2}=\dfrac{\sqrt2}{2}$. $x=\pi$: $k=-1$,
$\sin^3+\cos^3=-1$, and $\dfrac{-1(3-1)}{2}=-1$.

### 36.

**Strategy.** Multiply by a sine that turns each cosine into a double-angle sine, starting with
$2\sin36^\circ\cos36^\circ=\sin72^\circ$. The product telescopes.

Let $P=\cos36^\circ\cos72^\circ$. Since $\sin36^\circ\neq0$, multiply by $4\sin36^\circ$:

$$\begin{aligned}
4\sin36^\circ\,P
&=4\sin36^\circ\cos36^\circ\cos72^\circ\\
&=2\sin72^\circ\cos72^\circ\\
&=\sin144^\circ\\
&=\sin36^\circ.
\end{aligned}$$

The last equality uses $\sin144^\circ=\sin(180^\circ-36^\circ)=\sin36^\circ$. Dividing by the nonzero
number $\sin36^\circ$ gives $4P=1$, so $P=\dfrac14$.

**Check.** $\cos36^\circ=0.80902$ and $\cos72^\circ=0.30902$; the product is $0.25000$.

**Remark.** The same telescoping trick gives
$\cos20^\circ\cos40^\circ\cos80^\circ=\tfrac18$ (Problem 38) and, in general,
$$\prod_{k=1}^{n}\cos\frac{\theta}{2^k}=\frac{\sin\theta}{2^n\sin(\theta/2^n)}.$$
For Problem 38 take $\theta=160^\circ$ and $n=3$: the product is
$\dfrac{\sin160^\circ}{8\sin20^\circ}=\dfrac18$.

### 37.

**Strategy.** Combine the two factors with angles $60^\circ\pm\theta$ by the tangent addition and
subtraction formulas; their product has a difference of squares in both numerator and denominator.
Then multiply by $\tan\theta$ and recognise the triple-angle formula.

Put $t=\tan\theta$. By Theorem 7.8 and its difference form,

$$\tan(60^\circ-\theta)=\frac{\sqrt3-t}{1+\sqrt3t},\qquad
\tan(60^\circ+\theta)=\frac{\sqrt3+t}{1-\sqrt3t}.$$

Multiplying,

$$\tan(60^\circ-\theta)\tan(60^\circ+\theta)
=\frac{(\sqrt3-t)(\sqrt3+t)}{(1+\sqrt3t)(1-\sqrt3t)}
=\frac{3-t^2}{1-3t^2}.$$

Therefore

$$\tan\theta\,\tan(60^\circ-\theta)\tan(60^\circ+\theta)
=t\cdot\frac{3-t^2}{1-3t^2}
=\frac{3t-t^3}{1-3t^2}.$$

By the triple-angle formula proved in Example 9.6 (and in Problem 26 via the sine version), the last
expression equals $\tan3\theta$.

**Domain.** All three tangents on the left must be defined, and no denominator may vanish:
$\theta\neq\dfrac{\pi}{2}+k\pi$, $60^\circ-\theta\neq90^\circ+180^\circ k$,
$60^\circ+\theta\neq90^\circ+180^\circ k$, and $1-3t^2\neq0$ (the last is the condition
$\cos3\theta\neq0$).

**Check.** $\theta=10^\circ$: $0.17633\cdot1.19175\cdot2.74748=0.57735=\tan30^\circ$.

### 38.

**Strategy.** The same telescoping device as Problem 36, with the factor $8\sin20^\circ$.

Let $P=\cos20^\circ\cos40^\circ\cos80^\circ$. Multiply by $8\sin20^\circ$ and apply
$2\sin\alpha\cos\alpha=\sin2\alpha$ three times:

$$\begin{aligned}
8\sin20^\circ\,P
&=8\sin20^\circ\cos20^\circ\cos40^\circ\cos80^\circ\\
&=4\sin40^\circ\cos40^\circ\cos80^\circ\\
&=2\sin80^\circ\cos80^\circ\\
&=\sin160^\circ\\
&=\sin20^\circ.
\end{aligned}$$

The last equality uses $\sin160^\circ=\sin(180^\circ-20^\circ)=\sin20^\circ$. Since
$\sin20^\circ\neq0$, division gives $8P=1$, so $P=\dfrac18$.

**Check.** $0.93969\cdot0.76604\cdot0.17365=0.12500$.

**Remark.** The identity is a special case of the general product formula quoted in Problem 36.
