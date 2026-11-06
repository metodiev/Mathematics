# Formula Reference

A formula is a statement, not a spell. Every entry on this page is printed beside the conditions
under which it is true, because almost every classical formula fails the moment a hypothesis is
dropped: $\sqrt{x^2}=x$ only for $x\ge0$, $\ln(xy)=\ln x+\ln y$ only for $x,y>0$, and
$\int x^{-1}\,dx=\ln\lvert x\rvert+C$ only on an interval that does not contain $0$. Read the
conditions column first; it is part of the formula.

Conventions: angles are in radians unless a degree sign appears; $\ln$ is the natural logarithm;
$a>0$, $a\ne1$ for every logarithm or exponential with a real exponent; $n$ is a positive integer
unless stated otherwise; $C$ is an arbitrary constant. Symbols follow
[MATHEMATICAL_NOTATION.md](../../MATHEMATICAL_NOTATION.md), and the derivations behind these formulas
live in the tutorials linked from each section.

## 1. How to Read the Tables

| Column | Meaning |
|---|---|
| **Name** | What the formula computes, in the words a problem would use |
| **Formula** | The statement itself, in LaTeX |
| **Conditions** | Everything that must be true before the formula may be applied; an empty entry means "for all values for which both sides are defined" |

A dash in the conditions column means no restriction beyond the obvious one that all expressions
involved are defined. When a formula has several equivalent forms, the form most often needed in
practice is the one printed.

## 2. Arithmetic and Percentages

| Name | Formula | Conditions |
|---|---|---|
| Percentage of a quantity | $p\%\text{ of }N=\dfrac{p}{100}\,N$ | — |
| Fraction as a percentage | $\dfrac{a}{b}\times100\%$ | $b\ne0$ |
| Percentage change | $\dfrac{\text{new}-\text{old}}{\text{old}}$ | $\text{old}\ne0$; multiply by $100$ to express it as a percentage |
| Increase or decrease by $p\%$ | $\text{new}=\text{old}\left(1\pm\dfrac{p}{100}\right)$ | use $+$ for an increase and $-$ for a decrease |
| Successive changes | multiply the factors $\left(1+\dfrac{p_1}{100}\right)\left(1+\dfrac{p_2}{100}\right)$ | the changes are applied one after the other to the running amount |
| Reverse a percentage change | $\text{old}=\dfrac{\text{new}}{1+p/100}$ | $p\ne-100$ |
| Percentage points | difference of two percentages | a change from $20\%$ to $25\%$ is $5$ percentage points, i.e. a $25\%$ relative increase |
| Ratio equality | $a:b=c:d \iff ad=bc$ | $b,d\ne0$ |
| Direct proportion | $y=kx$ | $k\ne0$ constant |
| Inverse proportion | $y=\dfrac{k}{x}$ | $k\ne0$, $x\ne0$ |
| Weighted mean | $\bar{x}=\dfrac{\sum_{i=1}^{n}w_ix_i}{\sum_{i=1}^{n}w_i}$ | $\sum w_i\ne0$ |
| Percent error | $\dfrac{\lvert\text{approx}-\text{exact}\rvert}{\lvert\text{exact}\rvert}\cdot100\%$ | $\text{exact}\ne0$ |
| Simple interest | $I=Prt$ | $r$ is the annual rate as a decimal, $t$ the time in years |
| Compound interest | $A=P\left(1+\dfrac{r}{n}\right)^{nt}$ | $n$ periods per year, $1+\dfrac{r}{n}>0$ |
| Continuous compounding | $A=Pe^{rt}$ | $r$ the nominal annual rate, $t$ in years |
| Effective annual rate | $\left(1+\dfrac{r}{n}\right)^{n}-1$ | $n\ge1$ |
| Doubling time at rate $r$ | $t=\dfrac{\ln 2}{\ln(1+r)}$ | $r>-1$, $r\ne0$ |
| Compound annual growth rate | $\left(\dfrac{V_f}{V_i}\right)^{1/t}-1$ | $V_i>0$, $t>0$ |
| Average speed | $\bar{v}=\dfrac{\text{total distance}}{\text{total time}}$ | total time $>0$ |

> **Percentage points versus percent.** A rise from $20\%$ to $25\%$ is $5$ percentage points and a
> $25\%$ relative increase, because $25/20-1=0.25$. The two numbers answer different questions and
> are routinely confused in reporting.

## 3. Algebra

### 3.1 Products and factorisations

Every identity in this table holds for all real or complex $a$ and $b$; all but the last hold in any
commutative ring, since they are consequences of distributivity alone.

| Identity | Factorised or expanded form |
|---|---|
| Difference of squares | $a^2-b^2=(a-b)(a+b)$ |
| Perfect square | $a^2\pm2ab+b^2=(a\pm b)^2$ |
| Perfect cube | $a^3\pm3a^2b+3ab^2\pm b^3=(a\pm b)^3$ |
| Difference of cubes | $a^3-b^3=(a-b)(a^2+ab+b^2)$ |
| Sum of cubes | $a^3+b^3=(a+b)(a^2-ab+b^2)$ |
| Difference of $n$-th powers | $a^n-b^n=(a-b)\left(a^{n-1}+a^{n-2}b+\cdots+ab^{n-2}+b^{n-1}\right)$ |
| Sum of odd powers | $a^n+b^n=(a+b)\left(a^{n-1}-a^{n-2}b+\cdots-ab^{n-2}+b^{n-1}\right)$ for odd $n$ |
| Sophie Germain | $a^4+4b^4=\left(a^2-2ab+2b^2\right)\left(a^2+2ab+2b^2\right)$ |
| Trinomial square | $(a+b+c)^2=a^2+b^2+c^2+2ab+2bc+2ca$ |
| Cubic symmetric identity | $a^3+b^3+c^3-3abc=(a+b+c)\left(a^2+b^2+c^2-ab-bc-ca\right)$ |
| Geometric sum | $1+x+\cdots+x^{n-1}=\dfrac{x^n-1}{x-1}$ for $x\ne1$, and $=n$ for $x=1$ |
| Rationalising a difference | $\left(\sqrt a-\sqrt b\right)\left(\sqrt a+\sqrt b\right)=a-b$ |

Note that $a^2+b^2$ does not factor over the reals; it factors only over $\mathbb{C}$, as
$(a+bi)(a-bi)$.

### 3.2 Exponents

| Name | Formula | Conditions |
|---|---|---|
| Product rule | $a^{m}a^{n}=a^{m+n}$ | $a>0$ for real $m,n$ |
| Quotient rule | $\dfrac{a^m}{a^n}=a^{m-n}$ | $a>0$, or $a\ne0$ with integer exponents |
| Power of a power | $\left(a^m\right)^{n}=a^{mn}$ | $a>0$ for real $m,n$ |
| Power of a product | $(ab)^n=a^nb^n$ | $a,b>0$ for real $n$ |
| Power of a quotient | $\left(\dfrac ab\right)^n=\dfrac{a^n}{b^n}$ | $a>0$, $b>0$ for real $n$ |
| Zero exponent | $a^0=1$ | $a\ne0$ (the expression $0^0$ is left undefined) |
| Negative exponent | $a^{-n}=\dfrac{1}{a^n}$ | $a\ne0$ |
| Fractional exponent | $a^{m/n}=\left(\sqrt[n]{a}\right)^m$ | $a>0$; for odd $n$ any real $a$ |
| Square root of a square | $\sqrt{a^2}=\lvert a\rvert$ | — |
| Product of roots | $\sqrt a\,\sqrt b=\sqrt{ab}$ | $a\ge0$, $b\ge0$ |
| Sum of roots | $\sqrt a+\sqrt b=\sqrt{a+b+2\sqrt{ab}}$ | $a\ge0$, $b\ge0$ |

### 3.3 Logarithms

| Name | Formula | Conditions |
|---|---|---|
| Product rule | $\log_a(xy)=\log_a x+\log_a y$ | $x>0$, $y>0$, $a>0$, $a\ne1$ |
| Quotient rule | $\log_a\!\left(\dfrac xy\right)=\log_a x-\log_a y$ | $x>0$, $y>0$, $a>0$, $a\ne1$ |
| Power rule | $\log_a(x^r)=r\log_a x$ | $x>0$, $a>0$, $a\ne1$, $r\in\mathbb{R}$ |
| Base change | $\log_a x=\dfrac{\log_b x}{\log_b a}$ | $x>0$, $a,b>0$, $a,b\ne1$ |
| Reciprocal base | $\log_a b=\dfrac{1}{\log_b a}$ | $a,b>0$, $a,b\ne1$ |
| Power base | $\log_{a^n}x=\dfrac1n\log_a x$ | $x>0$, $a>0$, $a\ne1$, $n\ne0$ |
| Inverse pair | $a^{\log_a x}=x$ | $x>0$, $a>0$, $a\ne1$ |
| Inverse pair | $\log_a\left(a^x\right)=x$ | all real $x$, $a>0$, $a\ne1$ |
| Bases of one | $\log_a1=0$, $\log_a a=1$ | $a>0$, $a\ne1$ |

There is no rule for $\log_a(x+y)$: a sum inside a logarithm cannot be simplified.

### 3.4 Quadratics and polynomials

| Name | Formula | Conditions |
|---|---|---|
| Quadratic formula | $x=\dfrac{-b\pm\sqrt{b^2-4ac}}{2a}$ | $a\ne0$; real roots only when $b^2-4ac\ge0$ |
| Discriminant | $\Delta=b^2-4ac$: two distinct real roots if $\Delta>0$, one double root if $\Delta=0$, a conjugate pair if $\Delta<0$ | $a,b,c\in\mathbb{R}$, $a\ne0$ |
| Vertex form | $ax^2+bx+c=a\left(x+\dfrac{b}{2a}\right)^2+\dfrac{4ac-b^2}{4a}$ | $a\ne0$ |
| Vertex | $\left(-\dfrac{b}{2a},\ c-\dfrac{b^2}{4a}\right)$ | $a\ne0$ |
| Vieta, quadratic | $x_1+x_2=-\dfrac ba$, $x_1x_2=\dfrac ca$ | $a\ne0$; $x_1,x_2$ counted with multiplicity over $\mathbb{C}$ |
| Vieta, cubic | $x_1+x_2+x_3=-\dfrac ba$, $x_1x_2+x_2x_3+x_3x_1=\dfrac ca$, $x_1x_2x_3=-\dfrac da$ | for $ax^3+bx^2+cx+d$ with $a\ne0$; roots counted with multiplicity over $\mathbb{C}$ |
| Division algorithm for polynomials | $p(x)=d(x)q(x)+r(x)$ | $d\ne0$; $\deg r<\deg d$ |
| Remainder theorem | $p(x)=(x-r)q(x)+p(r)$ | $p$ a polynomial over a commutative ring |
| Factor theorem | $x-r$ divides $p(x)$ $\iff$ $p(r)=0$ | $p$ a polynomial |
| Rational root theorem | a rational root $u/v$ in lowest terms satisfies $u\mid a_0$ and $v\mid a_n$ | $f(x)=a_nx^n+\cdots+a_0$ has integer coefficients with $a_n\ne0$ |
| Fundamental theorem of algebra | a polynomial of degree $n\ge1$ over $\mathbb{C}$ has exactly $n$ roots counted with multiplicity | coefficients in $\mathbb{C}$ |
| Binomial expansion | $(a+b)^n=\sum_{k=0}^{n}\dbinom{n}{k}a^{n-k}b^{k}$ | $n\in\mathbb{N}_0$, commutative ring |

## 4. Geometry

### 4.1 Plane figures

In this table $s$ is a side, $l$ and $w$ are length and width, $b$ a base, $h$ the perpendicular
height, $r$ a radius, $d$ a diameter, $\theta$ an angle in radians, and $a,b$ the semi-axes of an
ellipse. Letters are reused from row to row; the meaning is the one stated in that row.

| Figure | Perimeter, arc or chord | Area | Conditions |
|---|---|---|---|
| Square | $P=4s$ | $A=s^2$ | — |
| Rectangle | $P=2(l+w)$ | $A=lw$ | — |
| Parallelogram | $P=2(a+b)$ | $A=bh$ | $a,b$ the side lengths; $h$ perpendicular to the base $b$ |
| Triangle, base and height | — | $A=\dfrac12 bh$ | $h$ perpendicular to $b$ |
| Triangle, two sides and included angle | — | $A=\dfrac12 ab\sin C$ | $a,b$ adjacent to angle $C$ |
| Triangle, Heron | — | $A=\sqrt{s(s-a)(s-b)(s-c)}$ with $s=\dfrac{a+b+c}{2}$ | side lengths satisfy the triangle inequality |
| Equilateral triangle | $P=3a$ | $A=\dfrac{\sqrt3}{4}a^2$ | — |
| Trapezoid | — | $A=\dfrac12(a+b)h$ | $a,b$ the parallel sides, $h$ their separation |
| Circle | $C=2\pi r=\pi d$ | $A=\pi r^2$ | — |
| Sector | arc $=r\theta$, perimeter $=2r+r\theta$ | $A=\dfrac12 r^2\theta=\dfrac12 r\,(\text{arc})$ | $\theta$ in radians, $0\le\theta\le2\pi$ |
| Segment | chord $=2r\sin\dfrac\theta2$ | $A=\dfrac12r^2(\theta-\sin\theta)$ | $\theta$ in radians; the region between the chord subtending $\theta$ and its arc (minor when $\theta\le\pi$) |
| Annulus | — | $A=\pi\left(R^2-r^2\right)$ | $R\ge r\ge0$ |
| Ellipse | no elementary closed form | $A=\pi ab$ | $a,b>0$ semi-axes |
| Regular $n$-gon | $P=ns$ | $A=\dfrac12 P a_p=\dfrac14ns^2\cot\dfrac{\pi}{n}$ | $a_p$ the apothem, $n\ge3$ |

The ellipse has no closed-form perimeter in elementary functions; its perimeter is a complete
elliptic integral, not $2\pi\sqrt{ab}$.

### 4.2 Triangles and circles

| Name | Formula | Conditions |
|---|---|---|
| Angle sum | $A+B+C=\pi$ | Euclidean triangle |
| Exterior angle | an exterior angle equals the sum of the two opposite interior angles | Euclidean triangle |
| Pythagorean theorem | $a^2+b^2=c^2$ | $c$ the hypotenuse of a right triangle |
| Converse of Pythagoras | if $a^2+b^2=c^2$ then the angle opposite $c$ is right | $a,b,c>0$ side lengths |
| Law of sines | $\dfrac{a}{\sin A}=\dfrac{b}{\sin B}=\dfrac{c}{\sin C}=2R$ | $R$ the circumradius; angles in radians |
| Law of cosines | $c^2=a^2+b^2-2ab\cos C$ | included angle $C$; reduces to Pythagoras when $C=\pi/2$ |
| Inradius | $r=\dfrac{A}{s}$, $s=\dfrac{a+b+c}{2}$ | $A$ the area of the triangle |
| Circumradius | $R=\dfrac{abc}{4A}$ | $A$ the area of the triangle |
| Similar triangles | areas scale as $k^2$ when lengths scale as $k$ | $k>0$ |
| Chord length | $\ell=2r\sin\dfrac\theta2$ | $\theta$ the central angle in radians, $0\le\theta\le2\pi$ |
| Tangent length | $t=\sqrt{d^2-r^2}$ | external point at distance $d>r$ from the centre |
| Inscribed angle | the inscribed angle is half the central angle on the same arc | both angles subtend the same arc |
| Circle equation | $(x-h)^2+(y-k)^2=r^2$ | centre $(h,k)$, radius $r>0$ |

For the law of sines, the case "two sides and a non-included angle" (SSA) can produce zero, one or two
triangles; the law of cosines has no such ambiguity and is the safer tool.

### 4.3 Solids

Here $B$ is the area of a base, $h$ the perpendicular height, $r$ a radius, $l$ the slant height of a
cone, and $R\ge r$ the radii of a frustum.

| Solid | Volume | Surface area | Conditions |
|---|---|---|---|
| Cube | $V=s^3$ | $S=6s^2$ | — |
| Rectangular box | $V=lwh$ | $S=2(lw+lh+wh)$ | — |
| Prism | $V=Bh$ | $S=2B+Ph$ with $P$ the base perimeter | $h$ perpendicular to the base |
| Cylinder | $V=\pi r^2h$ | lateral $2\pi rh$; total $2\pi r(r+h)$ | right circular cylinder |
| Pyramid | $V=\dfrac13 Bh$ | depends on the base | $h$ perpendicular height |
| Cone | $V=\dfrac13\pi r^2h$ | lateral $\pi rl$; total $\pi r(r+l)$, $l=\sqrt{r^2+h^2}$ | right circular cone |
| Sphere | $V=\dfrac43\pi r^3$ | $S=4\pi r^2$ | — |
| Frustum of a cone | $V=\dfrac{\pi h}{3}\left(R^2+Rr+r^2\right)$ | lateral $\pi(R+r)l$ | parallel circular bases, $l$ the slant height |

## 5. Trigonometry

| Name | Formula | Conditions |
|---|---|---|
| Degree–radian conversion | $\theta_{\text{rad}}=\dfrac{\pi}{180}\,\theta_{\text{deg}}$ | — |
| Right-triangle definitions | $\sin\theta=\dfrac{\text{opposite}}{\text{hypotenuse}}$, $\cos\theta=\dfrac{\text{adjacent}}{\text{hypotenuse}}$, $\tan\theta=\dfrac{\text{opposite}}{\text{adjacent}}$ | acute angle in a right triangle |
| Pythagorean identity | $\sin^2\theta+\cos^2\theta=1$ | all real $\theta$ |
| Related identities | $1+\tan^2\theta=\sec^2\theta$, $1+\cot^2\theta=\csc^2\theta$ | $\cos\theta\ne0$, respectively $\sin\theta\ne0$ |
| Double angle | $\sin2\theta=2\sin\theta\cos\theta$, $\cos2\theta=\cos^2\theta-\sin^2\theta=2\cos^2\theta-1=1-2\sin^2\theta$ | all real $\theta$ |
| Half angle | $\sin\dfrac\theta2=\pm\sqrt{\dfrac{1-\cos\theta}{2}}$, $\cos\dfrac\theta2=\pm\sqrt{\dfrac{1+\cos\theta}{2}}$ | the sign is that of the half-angle's quadrant |
| Half angle, tangent without a sign | $\tan\dfrac\theta2=\dfrac{\sin\theta}{1+\cos\theta}=\dfrac{1-\cos\theta}{\sin\theta}$ | $\cos\theta\ne-1$, respectively $\sin\theta\ne0$ |
| Auxiliary angle | $a\sin x+b\cos x=R\sin(x+\varphi)$ with $R=\sqrt{a^2+b^2}$, $\cos\varphi=\dfrac aR$, $\sin\varphi=\dfrac bR$ | $a,b$ not both zero |
| Triple angle | $\sin3\theta=3\sin\theta-4\sin^3\theta$, $\cos3\theta=4\cos^3\theta-3\cos\theta$ | all real $\theta$ |
| Small-angle approximation | $\sin x\approx x$, $\tan x\approx x$, $\cos x\approx1-\dfrac{x^2}{2}$ | $x$ in radians and small; errors are $O(x^3)$ and $O(x^4)$ |
| Sine rule | $\dfrac{a}{\sin A}=\dfrac{b}{\sin B}=\dfrac{c}{\sin C}$ | angles in radians; see the SSA caveat above |
| Cosine rule | $a^2=b^2+c^2-2bc\cos A$ | angles in radians |

The full set of trigonometric identities, with notes on when each is useful, is in the
[Identity Reference](../identities/README.md). Key values:

| $\theta$ | $0$ | $\dfrac{\pi}{6}$ | $\dfrac{\pi}{4}$ | $\dfrac{\pi}{3}$ | $\dfrac{\pi}{2}$ |
|---|---|---|---|---|---|
| $\sin\theta$ | $0$ | $\dfrac12$ | $\dfrac{\sqrt2}{2}$ | $\dfrac{\sqrt3}{2}$ | $1$ |
| $\cos\theta$ | $1$ | $\dfrac{\sqrt3}{2}$ | $\dfrac{\sqrt2}{2}$ | $\dfrac12$ | $0$ |
| $\tan\theta$ | $0$ | $\dfrac{\sqrt3}{3}$ | $1$ | $\sqrt3$ | undefined |

## 6. Sequences and Series

| Name | Formula | Conditions |
|---|---|---|
| Arithmetic sequence | $a_n=a_1+(n-1)d$ | common difference $d$ |
| Arithmetic sum | $S_n=\dfrac n2\left(a_1+a_n\right)=\dfrac n2\left(2a_1+(n-1)d\right)$ | $n\ge1$ |
| Geometric sequence | $a_n=a_1r^{\,n-1}$ | common ratio $r$ |
| Geometric sum | $S_n=a_1\dfrac{1-r^n}{1-r}$ | $r\ne1$; for $r=1$, $S_n=na_1$ |
| Infinite geometric series | $\sum_{k=0}^{\infty}ar^{k}=\dfrac{a}{1-r}$ | $\lvert r\rvert<1$; diverges for $\lvert r\rvert\ge1$ unless $a=0$ |
| Sum of the first $n$ integers | $\sum_{k=1}^{n}k=\dfrac{n(n+1)}{2}$ | $n\ge1$ |
| Sum of squares | $\sum_{k=1}^{n}k^2=\dfrac{n(n+1)(2n+1)}{6}$ | $n\ge1$ |
| Sum of cubes | $\sum_{k=1}^{n}k^3=\left(\dfrac{n(n+1)}{2}\right)^2$ | $n\ge1$ |
| Sum of odd numbers | $\sum_{k=1}^{n}(2k-1)=n^2$ | $n\ge1$ |
| Telescoping | $\sum_{k=1}^{n}\left(\dfrac{1}{k}-\dfrac{1}{k+1}\right)=1-\dfrac{1}{n+1}$ | $n\ge1$ |
| $p$-series | $\sum_{n=1}^{\infty}\dfrac{1}{n^p}$ converges | $p>1$; diverges for $p\le1$ |
| Harmonic series | $\sum_{n=1}^{\infty}\dfrac1n$ diverges | — |
| Binomial series | $(1+x)^{\alpha}=\sum_{k=0}^{\infty}\dbinom{\alpha}{k}x^{k}$ | $\lvert x\rvert<1$, $\alpha\in\mathbb{R}$, $\dbinom{\alpha}{k}=\dfrac{\alpha(\alpha-1)\cdots(\alpha-k+1)}{k!}$ |

## 7. Calculus

### 7.1 Limits

| Name | Formula | Conditions |
|---|---|---|
| Sum, product, quotient | limits add, multiply and (for quotients) divide | the individual limits exist and the denominator's limit is not $0$ |
| $\sin$ over $x$ | $\lim_{x\to0}\dfrac{\sin x}{x}=1$ | radians |
| Cosine defect | $\lim_{x\to0}\dfrac{1-\cos x}{x^2}=\dfrac12$ | radians |
| Exponential limit | $\lim_{x\to0}\dfrac{e^x-1}{x}=1$ | — |
| Logarithmic limit | $\lim_{x\to0}\dfrac{\ln(1+x)}{x}=1$ | $x>-1$ near $0$ |
| $e$ as a limit | $\lim_{n\to\infty}\left(1+\dfrac1n\right)^n=e$ | — |
| $e$ as a power | $\lim_{x\to0}(1+x)^{1/x}=e$ | $x>-1$, $x\ne0$ |
| L'Hôpital's rule | $\lim_{x\to a}\dfrac{f(x)}{g(x)}=\lim_{x\to a}\dfrac{f'(x)}{g'(x)}$ | $f,g$ differentiable near $a$ (perhaps not at $a$), $g(x)\ne0$ and $g'(x)\ne0$ for $x\ne a$ near $a$, $\lim f=\lim g=0$ **or** both limits infinite, and the right-hand limit exists or is infinite |

L'Hôpital's rule requires an indeterminate form. Applying it to $\dfrac{x+2}{x+1}$ at $0$ is wrong:
the limit is $2$, while the ratio of derivatives is $1$. The rule says nothing when the form is not
indeterminate.

### 7.2 Differentiation rules and derivatives

| Rule | Formula | Conditions |
|---|---|---|
| Sum | $(f+g)'=f'+g'$ | both differentiable |
| Constant multiple | $(cf)'=cf'$ | $c$ constant |
| Product | $(fg)'=f'g+fg'$ | both differentiable |
| Quotient | $\left(\dfrac fg\right)'=\dfrac{f'g-fg'}{g^2}$ | $g\ne0$ |
| Chain | $(f\circ g)'(x)=f'(g(x))\,g'(x)$ | $g$ differentiable at $x$, $f$ differentiable at $g(x)$ |
| Inverse function | $\left(f^{-1}\right)'(y)=\dfrac{1}{f'(x)}$ where $y=f(x)$ | $f'\ne0$; $f$ injective and continuously differentiable near $x$ |
| Implicit | $\dfrac{dy}{dx}=-\dfrac{F_x}{F_y}$ | $F(x,y)=0$ with $F$ continuously differentiable and $F_y\ne0$ |

| Function | Derivative | Conditions |
|---|---|---|
| $c$ | $0$ | constant |
| $x^n$ | $nx^{n-1}$ | all $x$ for $n\in\mathbb{N}_0$; $x\ne0$ for negative integers; $x>0$ for non-integer $n$ |
| $e^x$ | $e^x$ | all $x$ |
| $a^x$ | $a^x\ln a$ | $a>0$ |
| $\ln x$ | $\dfrac1x$ | $x>0$ |
| $\ln\lvert x\rvert$ | $\dfrac1x$ | $x\ne0$ |
| $\log_a x$ | $\dfrac{1}{x\ln a}$ | $x>0$, $a>0$, $a\ne1$ |
| $\sin x$ | $\cos x$ | radians |
| $\cos x$ | $-\sin x$ | radians |
| $\tan x$ | $\sec^2x$ | $\cos x\ne0$ |
| $\cot x$ | $-\csc^2x$ | $\sin x\ne0$ |
| $\sec x$ | $\sec x\tan x$ | $\cos x\ne0$ |
| $\csc x$ | $-\csc x\cot x$ | $\sin x\ne0$ |
| $\arcsin x$ | $\dfrac{1}{\sqrt{1-x^2}}$ | $\lvert x\rvert<1$ |
| $\arccos x$ | $-\dfrac{1}{\sqrt{1-x^2}}$ | $\lvert x\rvert<1$ |
| $\arctan x$ | $\dfrac{1}{1+x^2}$ | all $x$ |
| $\sinh x$ | $\cosh x$ | all $x$ |
| $\cosh x$ | $\sinh x$ | all $x$ |
| $\tanh x$ | $\operatorname{sech}^2x$ | all $x$ |
| $\operatorname{arsinh}x$ | $\dfrac{1}{\sqrt{x^2+1}}$ | all $x$ |
| $\operatorname{arcosh}x$ | $\dfrac{1}{\sqrt{x^2-1}}$ | $x>1$ |
| $\operatorname{artanh}x$ | $\dfrac{1}{1-x^2}$ | $\lvert x\rvert<1$ |

### 7.3 Integration

| Integral | Value | Conditions |
|---|---|---|
| Power rule | $\displaystyle\int x^n\,dx=\dfrac{x^{n+1}}{n+1}+C$ | $n\ne-1$; on an interval avoiding $0$ if $n<0$ |
| Reciprocal | $\displaystyle\int\dfrac{dx}{x}=\ln\lvert x\rvert+C$ | $x\ne0$; the formula holds separately on $(0,\infty)$ and $(-\infty,0)$ |
| Exponential | $\displaystyle\int e^x\,dx=e^x+C$ | — |
| General exponential | $\displaystyle\int a^x\,dx=\dfrac{a^x}{\ln a}+C$ | $a>0$, $a\ne1$ |
| Sine | $\displaystyle\int\sin x\,dx=-\cos x+C$ | radians |
| Cosine | $\displaystyle\int\cos x\,dx=\sin x+C$ | radians |
| Secant squared | $\displaystyle\int\sec^2x\,dx=\tan x+C$ | $\cos x\ne0$ |
| Cosecant squared | $\displaystyle\int\csc^2x\,dx=-\cot x+C$ | $\sin x\ne0$ |
| Tangent | $\displaystyle\int\tan x\,dx=-\ln\lvert\cos x\rvert+C$ | $\cos x\ne0$ |
| Cotangent | $\displaystyle\int\cot x\,dx=\ln\lvert\sin x\rvert+C$ | $\sin x\ne0$ |
| Secant | $\displaystyle\int\sec x\,dx=\ln\lvert\sec x+\tan x\rvert+C$ | $\cos x\ne0$ |
| Cosecant | $\displaystyle\int\csc x\,dx=-\ln\lvert\csc x+\cot x\rvert+C$ | $\sin x\ne0$ |
| Arctangent form | $\displaystyle\int\dfrac{dx}{1+x^2}=\arctan x+C$ | — |
| Arcsine form | $\displaystyle\int\dfrac{dx}{\sqrt{1-x^2}}=\arcsin x+C$ | $\lvert x\rvert<1$ |
| Scaled arctangent | $\displaystyle\int\dfrac{dx}{x^2+a^2}=\dfrac1a\arctan\dfrac xa+C$ | $a\ne0$ |
| Scaled arcsine | $\displaystyle\int\dfrac{dx}{\sqrt{a^2-x^2}}=\arcsin\dfrac xa+C$ | $a>0$, $\lvert x\rvert<a$ |
| Difference of squares | $\displaystyle\int\dfrac{dx}{x^2-a^2}=\dfrac{1}{2a}\ln\left\lvert\dfrac{x-a}{x+a}\right\rvert+C$ | $a\ne0$, $x\ne\pm a$ |
| Logarithm | $\displaystyle\int\ln x\,dx=x\ln x-x+C$ | $x>0$ |
| Exponential times polynomial | $\displaystyle\int xe^x\,dx=e^x(x-1)+C$ | — |
| Sine squared | $\displaystyle\int\sin^2x\,dx=\dfrac x2-\dfrac{\sin2x}{4}+C$ | radians |
| Cosine squared | $\displaystyle\int\cos^2x\,dx=\dfrac x2+\dfrac{\sin2x}{4}+C$ | radians |
| Hyperbolic sine | $\displaystyle\int\sinh x\,dx=\cosh x+C$ | — |
| Hyperbolic cosine | $\displaystyle\int\cosh x\,dx=\sinh x+C$ | — |

| Method | Formula | Conditions |
|---|---|---|
| Substitution | $\displaystyle\int f(g(x))\,g'(x)\,dx=\int f(u)\,du$ with $u=g(x)$ | $g$ continuously differentiable |
| Integration by parts | $\displaystyle\int u\,dv=uv-\int v\,du$ | $u,v$ continuously differentiable |
| Fundamental theorem, first part | $\dfrac{d}{dx}\displaystyle\int_a^x f(t)\,dt=f(x)$ | $f$ continuous on an interval containing $a$ and $x$ |
| Fundamental theorem, second part | $\displaystyle\int_a^b F'(x)\,dx=F(b)-F(a)$ | $F$ differentiable on $[a,b]$ with $F'$ Riemann integrable |
| Partial fractions | decompose a proper rational function into terms $\dfrac{A}{(x-r)^k}$ and $\dfrac{Bx+C}{(x^2+px+q)^k}$ | numerator degree below denominator degree; denominator factored over $\mathbb{R}$ |

### 7.4 Taylor and Maclaurin series

Taylor's theorem with the Lagrange form of the remainder:

$$
f(x)=\sum_{k=0}^{n}\frac{f^{(k)}(a)}{k!}\,(x-a)^k+R_n(x),
\qquad
R_n(x)=\frac{f^{(n+1)}(\xi)}{(n+1)!}\,(x-a)^{n+1},
$$

where $\xi$ lies strictly between $a$ and $x$. The hypothesis is that $f$ is $n+1$ times
differentiable on an open interval containing both points.

| Series | Expansion | Convergence |
|---|---|---|
| Exponential | $e^x=\displaystyle\sum_{k=0}^{\infty}\dfrac{x^k}{k!}$ | all real $x$ |
| Sine | $\sin x=\displaystyle\sum_{k=0}^{\infty}\dfrac{(-1)^kx^{2k+1}}{(2k+1)!}$ | all real $x$ |
| Cosine | $\cos x=\displaystyle\sum_{k=0}^{\infty}\dfrac{(-1)^kx^{2k}}{(2k)!}$ | all real $x$ |
| Logarithm | $\ln(1+x)=\displaystyle\sum_{k=1}^{\infty}\dfrac{(-1)^{k+1}x^k}{k}$ | $-1<x\le1$ |
| Geometric | $\dfrac{1}{1-x}=\displaystyle\sum_{k=0}^{\infty}x^k$ | $\lvert x\rvert<1$ |
| Binomial | $(1+x)^{\alpha}=\displaystyle\sum_{k=0}^{\infty}\dbinom{\alpha}{k}x^k$ | $\lvert x\rvert<1$ for general $\alpha$; the endpoints depend on $\alpha$ |
| Arctangent | $\arctan x=\displaystyle\sum_{k=0}^{\infty}\dfrac{(-1)^kx^{2k+1}}{2k+1}$ | $\lvert x\rvert\le1$ (the endpoint values converge to $\pm\pi/4$) |
| Tangent | $\tan x=x+\dfrac{x^3}{3}+\dfrac{2x^5}{15}+\dfrac{17x^7}{315}+\cdots$ | $\lvert x\rvert<\pi/2$ |
| Hyperbolic sine | $\sinh x=\displaystyle\sum_{k=0}^{\infty}\dfrac{x^{2k+1}}{(2k+1)!}$ | all real $x$ |
| Hyperbolic cosine | $\cosh x=\displaystyle\sum_{k=0}^{\infty}\dfrac{x^{2k}}{(2k)!}$ | all real $x$ |

### 7.5 Applications of the derivative and integral

| Name | Formula | Conditions |
|---|---|---|
| Linearisation | $f(a+h)\approx f(a)+f'(a)h$ | $f$ twice differentiable near $a$; error $O(h^2)$ |
| Newton's method | $x_{n+1}=x_n-\dfrac{f(x_n)}{f'(x_n)}$ | $f$ differentiable, $f'(x_n)\ne0$, $x_0$ close to a simple root |
| Mean value theorem | $f(b)-f(a)=f'(c)(b-a)$ for some $c\in(a,b)$ | $f$ continuous on $[a,b]$, differentiable on $(a,b)$ |
| Second derivative test | $f'(c)=0$ and $f''(c)>0$ gives a local minimum; $f''(c)<0$ gives a local maximum | $f''$ exists and is continuous near $c$ |
| Average value | $\bar{f}=\dfrac{1}{b-a}\displaystyle\int_a^b f(x)\,dx$ | $f$ integrable on $[a,b]$ |
| Arc length | $L=\displaystyle\int_a^b\sqrt{1+\left(f'(x)\right)^2}\,dx$ | $f$ continuously differentiable |
| Surface of revolution | $S=2\pi\displaystyle\int_a^b f(x)\sqrt{1+\left(f'(x)\right)^2}\,dx$ | $f\ge0$ and continuously differentiable |
| Volume, discs | $V=\pi\displaystyle\int_a^b\left(f(x)\right)^2dx$ | $f$ continuous; rotation about the $x$-axis |
| Volume, washers | $V=\pi\displaystyle\int_a^b\left(R(x)^2-r(x)^2\right)dx$ | $R\ge r\ge0$ continuous |
| Volume, shells | $V=2\pi\displaystyle\int_a^b x\,f(x)\,dx$ | $0\le a<b$, $f\ge0$ continuous; rotation about the $y$-axis |
| Curvature of a graph | $\kappa=\dfrac{\lvert f''(x)\rvert}{\left(1+\left(f'(x)\right)^2\right)^{3/2}}$ | $f$ twice differentiable |

## 8. Linear Algebra

| Name | Formula | Conditions |
|---|---|---|
| Matrix product | $(AB)_{ij}=\sum_{k=1}^{n}a_{ik}b_{kj}$ | $A$ is $m\times n$ and $B$ is $n\times p$ |
| Transpose of a product | $(AB)^{\mathsf T}=B^{\mathsf T}A^{\mathsf T}$ | conformable |
| Inverse of a product | $(AB)^{-1}=B^{-1}A^{-1}$ | $A,B$ invertible |
| Determinant of a product | $\det(AB)=\det A\,\det B$ | square matrices of the same size |
| Determinant of a transpose | $\det\left(A^{\mathsf T}\right)=\det A$ | square |
| Determinant of an inverse | $\det\left(A^{-1}\right)=\dfrac{1}{\det A}$ | $\det A\ne0$ |
| Scaling the determinant | $\det(cA)=c^n\det A$ | $A$ is $n\times n$ |
| Determinant by expansion | $\det A=\sum_{j=1}^{n}(-1)^{i+j}a_{ij}M_{ij}$ | any fixed row $i$; $M_{ij}$ the minor |
| $2\times2$ determinant | $\det\begin{pmatrix}a&b\\c&d\end{pmatrix}=ad-bc$ | — |
| Triangular determinant | the determinant equals the product of the diagonal entries | upper or lower triangular |
| $2\times2$ inverse | $\begin{pmatrix}a&b\\c&d\end{pmatrix}^{-1}=\dfrac{1}{ad-bc}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}$ | $ad-bc\ne0$ |
| General inverse | $A^{-1}=\dfrac{1}{\det A}\operatorname{adj}A$ | $\det A\ne0$ |
| Cramer's rule | $x_i=\dfrac{\det A_i}{\det A}$ | $\det A\ne0$; $A_i$ is $A$ with column $i$ replaced by $b$ |
| Invertibility criterion | $A$ invertible $\iff$ $\det A\ne0$ $\iff$ $\operatorname{rank}A=n$ $\iff$ $\ker A=\{0\}$ | $A$ is $n\times n$ |
| Rank–nullity | $\dim\ker T+\dim\operatorname{im}T=\dim V$ | $V$ finite-dimensional, $T:V\to W$ linear |
| Eigenvalue equation | $\det(A-\lambda I)=0$ | square $A$ over $\mathbb{C}$ for the full set of roots |
| Trace and determinant | $\operatorname{tr}A=\sum_i\lambda_i$, $\det A=\prod_i\lambda_i$ | eigenvalues counted with algebraic multiplicity |
| $2\times2$ eigenvalues | $\lambda=\dfrac{\operatorname{tr}A\pm\sqrt{\left(\operatorname{tr}A\right)^2-4\det A}}{2}$ | $2\times2$ matrix |
| Diagonalisation | $A=PDP^{-1}$ with $D$ diagonal | $A$ has $n$ linearly independent eigenvectors |
| Orthogonal diagonalisation | $A=Q\Lambda Q^{\mathsf T}$ with $Q$ orthogonal and $\Lambda$ diagonal real | $A$ real symmetric |
| Cayley–Hamilton | $p_A(A)=0$ where $p_A(\lambda)=\det(\lambda I-A)$ | square matrix |
| Dot product and angle | $\mathbf u\cdot\mathbf v=\lVert\mathbf u\rVert\lVert\mathbf v\rVert\cos\theta$ | $\mathbf u,\mathbf v\ne\mathbf 0$ |
| Norm | $\lVert\mathbf u\rVert=\sqrt{\mathbf u\cdot\mathbf u}$ | — |
| Cauchy–Schwarz | $\lvert\mathbf u\cdot\mathbf v\rvert\le\lVert\mathbf u\rVert\lVert\mathbf v\rVert$ | any inner product space |
| Projection | $\operatorname{proj}_{\mathbf v}\mathbf u=\dfrac{\mathbf u\cdot\mathbf v}{\mathbf v\cdot\mathbf v}\,\mathbf v$ | $\mathbf v\ne\mathbf 0$ |
| Cross product | $\mathbf u\times\mathbf v=\left(u_2v_3-u_3v_2,\ u_3v_1-u_1v_3,\ u_1v_2-u_2v_1\right)$ | vectors in $\mathbb{R}^3$ |
| Cross product length | $\lVert\mathbf u\times\mathbf v\rVert=\lVert\mathbf u\rVert\lVert\mathbf v\rVert\sin\theta$ | $\theta$ the angle between them |
| Rotation matrix | $R_\theta=\begin{pmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{pmatrix}$ | $\theta$ in radians; rotates counter-clockwise |

## 9. Probability and Statistics

### 9.1 Probability rules

| Name | Formula | Conditions |
|---|---|---|
| Complement | $\Pr(A^{\complement})=1-\Pr(A)$ | — |
| Addition rule | $\Pr(A\cup B)=\Pr(A)+\Pr(B)-\Pr(A\cap B)$ | — |
| Disjoint events | $\Pr(A\cup B)=\Pr(A)+\Pr(B)$ | $A\cap B=\varnothing$ |
| Difference | $\Pr(A\setminus B)=\Pr(A)-\Pr(A\cap B)$ | — |
| Monotonicity | $\Pr(A)\le\Pr(B)$ | $A\subseteq B$ |
| Conditional probability | $\Pr(A\mid B)=\dfrac{\Pr(A\cap B)}{\Pr(B)}$ | $\Pr(B)>0$ |
| Multiplication rule | $\Pr(A\cap B)=\Pr(A\mid B)\Pr(B)$ | $\Pr(B)>0$ |
| Independence | $\Pr(A\cap B)=\Pr(A)\Pr(B)$ | definition of independence |
| Law of total probability | $\Pr(A)=\sum_i\Pr(A\mid B_i)\Pr(B_i)$ | $\{B_i\}$ a finite or countable partition of the sample space with $\Pr(B_i)>0$ |
| Bayes' theorem | $\Pr(B_k\mid A)=\dfrac{\Pr(A\mid B_k)\Pr(B_k)}{\sum_i\Pr(A\mid B_i)\Pr(B_i)}$ | the same partition and $\Pr(A)>0$ |
| Markov's inequality | $\Pr(X\ge a)\le\dfrac{\mathbb{E}[X]}{a}$ | $X\ge0$ almost surely, $a>0$ |
| Chebyshev's inequality | $\Pr\left(\lvert X-\mu\rvert\ge a\right)\le\dfrac{\sigma^2}{a^2}$ | $\mathbb{E}[X]=\mu$, $\operatorname{Var}(X)=\sigma^2<\infty$, $a>0$ |

### 9.2 Expectation, variance and covariance

| Name | Formula | Conditions |
|---|---|---|
| Expectation of a function | $\mathbb{E}[g(X)]=\sum_x g(x)\Pr(X=x)$ or $\displaystyle\int g(x)f_X(x)\,dx$ | the sum or integral converges absolutely |
| Linearity | $\mathbb{E}[aX+b]=a\mathbb{E}[X]+b$, $\mathbb{E}[X+Y]=\mathbb{E}[X]+\mathbb{E}[Y]$ | expectations exist |
| Product rule for expectation | $\mathbb{E}[XY]=\mathbb{E}[X]\mathbb{E}[Y]$ | $X,Y$ independent and integrable |
| Variance | $\operatorname{Var}(X)=\mathbb{E}\left[(X-\mu)^2\right]=\mathbb{E}\left[X^2\right]-\mu^2$ | $\mathbb{E}[X^2]<\infty$ |
| Scaling the variance | $\operatorname{Var}(aX+b)=a^2\operatorname{Var}(X)$ | variance exists |
| Variance of a sum | $\operatorname{Var}(X+Y)=\operatorname{Var}(X)+\operatorname{Var}(Y)+2\operatorname{Cov}(X,Y)$ | variances exist |
| Covariance | $\operatorname{Cov}(X,Y)=\mathbb{E}[(X-\mu_X)(Y-\mu_Y)]=\mathbb{E}[XY]-\mu_X\mu_Y$ | second moments exist |
| Covariance under scaling | $\operatorname{Cov}(aX+b,\ cY+d)=ac\operatorname{Cov}(X,Y)$ | — |
| Correlation | $\rho=\dfrac{\operatorname{Cov}(X,Y)}{\sigma_X\sigma_Y}$ | $\sigma_X,\sigma_Y>0$; $\lvert\rho\rvert\le1$ |
| Standardisation | $Z=\dfrac{X-\mu}{\sigma}$ | $\sigma>0$ |

### 9.3 Standard distributions

| Distribution | Probability function or density | Mean | Variance | Conditions |
|---|---|---|---|---|
| Bernoulli$(p)$ | $\Pr(X=1)=p$, $\Pr(X=0)=1-p$ | $p$ | $p(1-p)$ | $0\le p\le1$ |
| Binomial$(n,p)$ | $\Pr(X=k)=\dbinom{n}{k}p^k(1-p)^{n-k}$ | $np$ | $np(1-p)$ | $n\in\mathbb{N}$, $0\le p\le1$, $k=0,\ldots,n$ |
| Geometric$(p)$ | $\Pr(X=k)=(1-p)^{k-1}p$ | $\dfrac1p$ | $\dfrac{1-p}{p^2}$ | $0<p\le1$, $k\in\mathbb{N}$; $X$ counts trials up to the first success |
| Poisson$(\lambda)$ | $\Pr(X=k)=\dfrac{e^{-\lambda}\lambda^k}{k!}$ | $\lambda$ | $\lambda$ | $\lambda>0$, $k\in\mathbb{N}_0$ |
| Uniform$(a,b)$ | $f(x)=\dfrac{1}{b-a}$ | $\dfrac{a+b}{2}$ | $\dfrac{(b-a)^2}{12}$ | $a<b$, density on $[a,b]$ |
| Exponential$(\lambda)$ | $f(x)=\lambda e^{-\lambda x}$ | $\dfrac1\lambda$ | $\dfrac{1}{\lambda^2}$ | $\lambda>0$, $x\ge0$ |
| Normal$(\mu,\sigma^2)$ | $f(x)=\dfrac{1}{\sigma\sqrt{2\pi}}\exp\left(-\dfrac{(x-\mu)^2}{2\sigma^2}\right)$ | $\mu$ | $\sigma^2$ | $\sigma>0$ |

### 9.4 Statistics

| Name | Formula | Conditions |
|---|---|---|
| Sample mean | $\bar{x}=\dfrac1n\sum_{i=1}^{n}x_i$ | $n\ge1$ |
| Sample variance | $s^2=\dfrac{1}{n-1}\sum_{i=1}^{n}\left(x_i-\bar{x}\right)^2$ | $n\ge2$; the divisor $n-1$ makes $s^2$ unbiased for $\sigma^2$ |
| Population variance | $\sigma^2=\dfrac1N\sum_{i=1}^{N}\left(x_i-\mu\right)^2$ | the whole population of size $N$ is known |
| Standard error of the mean | $\operatorname{SE}=\dfrac{\sigma}{\sqrt{n}}$, estimated by $\dfrac{s}{\sqrt{n}}$ | independent observations; $\sigma$ known or $n$ large |
| Central limit theorem | $\dfrac{\bar{X}-\mu}{\sigma/\sqrt{n}}\xrightarrow{d}\mathcal{N}(0,1)$ | $X_i$ independent and identically distributed with $0<\sigma^2<\infty$ |
| Confidence interval for a mean, $\sigma$ known | $\bar{x}\pm z_{\alpha/2}\dfrac{\sigma}{\sqrt{n}}$ | normal population, or $n$ large; observations independent |
| Confidence interval for a mean, $\sigma$ unknown | $\bar{x}\pm t_{n-1,\alpha/2}\dfrac{s}{\sqrt{n}}$ | normal population; observations independent |
| Regression slope | $\hat\beta_1=\dfrac{\sum_i\left(x_i-\bar{x}\right)\left(y_i-\bar{y}\right)}{\sum_i\left(x_i-\bar{x}\right)^2}$ | $\sum_i(x_i-\bar{x})^2\ne0$ |
| Regression intercept | $\hat\beta_0=\bar{y}-\hat\beta_1\bar{x}$ | as above |
| Coefficient of determination | $r^2=\dfrac{\left[\sum_i(x_i-\bar{x})(y_i-\bar{y})\right]^2}{\sum_i(x_i-\bar{x})^2\sum_i(y_i-\bar{y})^2}$ | both sums of squares positive |
| Permutations | ${}_nP_k=\dfrac{n!}{(n-k)!}$ | $0\le k\le n$ |
| Combinations | $\dbinom{n}{k}=\dfrac{n!}{k!\,(n-k)!}$ | $0\le k\le n$ |
| Arrangements with repetition | $n^{k}$ | $k$ positions, $n$ choices each |
| Multisets | $\dbinom{n+k-1}{k}$ | choosing $k$ from $n$ types with repetition, order irrelevant |

---

*Part of the [Reference Library](../README.md). Notation follows
[MATHEMATICAL_NOTATION.md](../../MATHEMATICAL_NOTATION.md); terms are defined in
[GLOSSARY.md](../../GLOSSARY.md); the curriculum itself begins at [README.md](../../README.md).*
