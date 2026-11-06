# Identity Reference

An **identity** is an equation that is true for every value of its variables for which both sides are
defined; an **equation**, by contrast, is true only for some values and is a problem to solve. This
page collects the identities worth knowing, groups them by the kind of expression they transform, and
records beside each one the situation in which it earns its keep. Every identity is written in
display math so that the structure is visible at a glance.

Identities are not magic, and they are not independent facts to be memorised in bulk: almost all of
the trigonometric and hyperbolic ones follow from the definitions on the unit circle or from the
exponential function, and the combinatorial ones follow from counting a single set in two ways.
Section 7 shows how the derivations go, so that an identity you forget can be rebuilt rather than
looked up.

Notation follows [MATHEMATICAL_NOTATION.md](../../MATHEMATICAL_NOTATION.md); all angles are in
radians. Where an identity has a restricted domain, the restriction is stated. For example,
$\tan(A+B)=\dfrac{\tan A+\tan B}{1-\tan A\tan B}$ does not apply at $A=B=\pi/2$, because neither
side is defined there, and $\sin\frac\theta2=\sqrt{\frac{1-\cos\theta}{2}}$ fails for
$\theta\in(2\pi,4\pi)$, where the left side is negative and the right side is not.

## 1. What an Identity Is

Three statements look alike and are not:

| Kind | Example | What it asserts |
|---|---|---|
| Definition | $\tan\theta:=\dfrac{\sin\theta}{\cos\theta}$ | a name is being introduced |
| Identity | $\sin^2\theta+\cos^2\theta=1$ for all $\theta$ | the two sides agree everywhere they are defined |
| Equation | $\sin\theta=\tfrac12$ | the two sides agree at certain values only; solving finds them |

To *verify* an identity, transform one side into the other, or show that the difference simplifies to
$0$, using identities that are already known. To *disprove* one, a single numerical counterexample
suffices. Every step must preserve the domain: multiplying both sides by $\sin\theta$ loses the case
$\sin\theta=0$ unless that case is treated separately.

## 2. Trigonometric Identities

### 2.1 Pythagorean identities

$$
\sin^2\theta+\cos^2\theta=1
$$

The identity behind almost every simplification in trigonometry; it removes either $\sin^2$ or
$\cos^2$ from an expression.

$$
1+\tan^2\theta=\sec^2\theta \qquad (\cos\theta\ne0),
\qquad
1+\cot^2\theta=\csc^2\theta \qquad (\sin\theta\ne0)
$$

Use these when a sum of a square and $1$ appears, typically after dividing the Pythagorean identity
by $\cos^2\theta$ or $\sin^2\theta$.

### 2.2 Reciprocal and quotient identities

$$
\sec\theta=\frac{1}{\cos\theta},\qquad
\csc\theta=\frac{1}{\sin\theta},\qquad
\cot\theta=\frac{1}{\tan\theta}=\frac{\cos\theta}{\sin\theta}
\qquad
\tan\theta=\frac{\sin\theta}{\cos\theta}
$$

with $\cos\theta\ne0$ for $\sec$ and $\tan$, and $\sin\theta\ne0$ for $\csc$ and $\cot$. Use them to
convert a stray secant or cosecant into sines and cosines, which is usually the fastest route to a
common denominator.

### 2.3 Parity and periodicity

$$
\sin(-\theta)=-\sin\theta,\qquad
\cos(-\theta)=\cos\theta,\qquad
\tan(-\theta)=-\tan\theta
$$

Sine and tangent are odd, cosine is even; this halves the work when a negative angle or a symmetric
interval appears.

$$
\sin(\theta+2\pi)=\sin\theta,\qquad
\cos(\theta+2\pi)=\cos\theta,\qquad
\tan(\theta+\pi)=\tan\theta
$$

The period of sine and cosine is $2\pi$, of tangent is $\pi$; use it to move an angle into a standard
range before evaluating.

### 2.4 Sum and difference formulas

$$
\sin(A\pm B)=\sin A\cos B\pm\cos A\sin B
$$

Expands a sine of a sum; the standard first step when two angles are combined.

$$
\cos(A\pm B)=\cos A\cos B\mp\sin A\sin B
$$

Note the sign reversal: the cosine of a sum subtracts the product of sines.

$$
\tan(A\pm B)=\frac{\tan A\pm\tan B}{1\mp\tan A\tan B}
$$

Valid when $A$, $B$ and $A\pm B$ are not odd multiples of $\pi/2$, and the denominator is nonzero;
used to combine two tangents into one.

The corresponding formulas for cotangent and secant are never needed in practice: convert to sine and
cosine first.

### 2.5 Double-angle formulas

$$
\sin2\theta=2\sin\theta\cos\theta
$$

Turns a product into a single sine; the reverse direction is what makes $\int\sin\theta\cos\theta\,d\theta$
easy.

$$
\cos2\theta=\cos^2\theta-\sin^2\theta=2\cos^2\theta-1=1-2\sin^2\theta
$$

Three forms of one identity; choose the form that eliminates the function you want to remove.

$$
\tan2\theta=\frac{2\tan\theta}{1-\tan^2\theta}
$$

Valid when $\theta$ and $2\theta$ avoid odd multiples of $\pi/2$ and $\tan^2\theta\ne1$.

### 2.6 Half-angle formulas

$$
\sin\frac\theta2=\pm\sqrt{\frac{1-\cos\theta}{2}},
\qquad
\cos\frac\theta2=\pm\sqrt{\frac{1+\cos\theta}{2}}
$$

The sign is not arbitrary: it is the sign of the half-angle, so it depends on the quadrant of
$\theta/2$, not on the sign of $\cos\theta$. These are the standard way to lower a power before
integrating.

$$
\tan\frac\theta2=\frac{1-\cos\theta}{\sin\theta}=\frac{\sin\theta}{1+\cos\theta}
$$

These two forms carry no sign ambiguity; the first needs $\sin\theta\ne0$ and the second needs
$\cos\theta\ne-1$. They are the basis of the Weierstrass substitution $t=\tan\frac\theta2$.

### 2.7 Product-to-sum formulas

$$
\sin A\sin B=\frac12\left[\cos(A-B)-\cos(A+B)\right]
$$

$$
\cos A\cos B=\frac12\left[\cos(A-B)+\cos(A+B)\right]
$$

$$
\sin A\cos B=\frac12\left[\sin(A+B)+\sin(A-B)\right]
$$

Products become sums, which is exactly what integration and Fourier analysis want; all three hold
for all real $A,B$.

### 2.8 Sum-to-product formulas

$$
\sin A+\sin B=2\sin\frac{A+B}{2}\cos\frac{A-B}{2}
$$

$$
\sin A-\sin B=2\cos\frac{A+B}{2}\sin\frac{A-B}{2}
$$

$$
\cos A+\cos B=2\cos\frac{A+B}{2}\cos\frac{A-B}{2}
$$

$$
\cos A-\cos B=-2\sin\frac{A+B}{2}\sin\frac{A-B}{2}
$$

Sums become products, which is what solving $\sin A+\sin B=0$ or finding zeros of a signal wants.
Note the minus sign in the last identity.

### 2.9 Auxiliary-angle identity

$$
a\sin x+b\cos x=R\sin(x+\varphi),
\qquad
R=\sqrt{a^2+b^2},\quad
\cos\varphi=\frac aR,\quad
\sin\varphi=\frac bR
$$

Valid whenever $a,b$ are not both zero. It collapses a linear combination of sine and cosine into a
single wave with amplitude $R$, which is how the amplitude and phase of a sum of oscillations are
computed.

### 2.10 Triple-angle formulas

$$
\sin3\theta=3\sin\theta-4\sin^3\theta,\qquad
\cos3\theta=4\cos^3\theta-3\cos\theta
$$

Useful when a cubic in $\sin\theta$ or $\cos\theta$ has to be recognised as a triple angle.

## 3. Algebraic Identities

### 3.1 Differences and sums of powers

$$
a^2-b^2=(a-b)(a+b)
$$

The most-used factorisation in algebra; it converts a difference of squares into a product and is the
reason rationalising denominators works.

$$
a^3-b^3=(a-b)\left(a^2+ab+b^2\right),
\qquad
a^3+b^3=(a+b)\left(a^2-ab+b^2\right)
$$

The two cube factorisations; note that the quadratic factor is irreducible over the reals.

$$
a^n-b^n=(a-b)\left(a^{n-1}+a^{n-2}b+\cdots+ab^{n-2}+b^{n-1}\right)
$$

Valid for every integer $n\ge1$; it says $a-b$ always divides $a^n-b^n$, which is why the geometric
series has the form it does.

$$
a^n+b^n=(a+b)\left(a^{n-1}-a^{n-2}b+\cdots-ab^{n-2}+b^{n-1}\right)
$$

Valid for odd $n$ only; for even $n$, $a^n+b^n$ has no factor $a+b$ (take $a=1,b=-1$).

$$
a^4+4b^4=\left(a^2-2ab+2b^2\right)\left(a^2+2ab+2b^2\right)
$$

Sophie Germain's identity; it shows that a sum of a fourth power and four times a fourth power always
factors, even though a sum of two squares generally does not.

### 3.2 Binomial expansions

$$
(a+b)^2=a^2+2ab+b^2,\qquad
(a-b)^2=a^2-2ab+b^2
$$

$$
(a+b)^3=a^3+3a^2b+3ab^2+b^3,\qquad
(a-b)^3=a^3-3a^2b+3ab^2-b^3
$$

The small cases of the binomial theorem, worth recognising instantly in both directions.

$$
(a+b)^n=\sum_{k=0}^{n}\binom{n}{k}a^{n-k}b^{k}
$$

Valid for $n\in\mathbb{N}_0$ in any commutative ring; the coefficient $\binom nk$ counts how many
ways $k$ factors of $b$ can be chosen from $n$ factors.

$$
(a+b+c)^2=a^2+b^2+c^2+2ab+2bc+2ca
$$

The trinomial square; the cross terms are the pairwise products, each doubled.

### 3.3 Symmetric sums

Writing $e_1=a+b+c$, $e_2=ab+bc+ca$, $e_3=abc$ for the elementary symmetric polynomials, the power
sums satisfy

$$
a^2+b^2+c^2=e_1^2-2e_2
$$

$$
a^3+b^3+c^3=e_1^3-3e_1e_2+3e_3
$$

which is the special case of Newton's identities. The classical form of the second is

$$
a^3+b^3+c^3-3abc=(a+b+c)\left(a^2+b^2+c^2-ab-bc-ca\right)
$$

Use it when a problem says "$a+b+c=0$": then $a^3+b^3+c^3=3abc$.

### 3.4 Vieta's formulas

For $ax^2+bx+c=a(x-x_1)(x-x_2)$ with $a\ne0$,

$$
x_1+x_2=-\frac ba,\qquad x_1x_2=\frac ca
$$

For $ax^3+bx^2+cx+d=a(x-x_1)(x-x_2)(x-x_3)$ with $a\ne0$,

$$
x_1+x_2+x_3=-\frac ba,\qquad
x_1x_2+x_2x_3+x_3x_1=\frac ca,\qquad
x_1x_2x_3=-\frac da
$$

These express symmetric functions of the roots without solving for the roots; the alternating signs
come from multiplying out the factors. Roots are counted with multiplicity over $\mathbb{C}$.

## 4. Exponential and Logarithmic Identities

For $a>0$ and real $x,y$,

$$
a^{x+y}=a^xa^y,\qquad
a^{x-y}=\frac{a^x}{a^y},\qquad
\left(a^x\right)^y=a^{xy}
$$

The defining functional equations of the exponential; the third fails for $a<0$, which is why real
exponentials are only defined for positive bases.

$$
a^0=1,\qquad a^{-x}=\frac{1}{a^x}
$$

For $a>0$, $a\ne1$, and $x,y>0$,

$$
\log_a(xy)=\log_a x+\log_a y
$$

The product rule: multiplication inside becomes addition outside, which is the historical reason
logarithms were used for computation.

$$
\log_a\!\left(\frac xy\right)=\log_a x-\log_a y,
\qquad
\log_a\left(x^{r}\right)=r\log_a x
$$

The quotient and power rules; the power rule requires $x>0$ because $\log_a x$ does.

$$
\log_a x=\frac{\ln x}{\ln a}=\frac{\log_b x}{\log_b a}
$$

Change of base; also $\log_a b=\dfrac{1}{\log_b a}$ and $\log_a b\cdot\log_b a=1$.

$$
a^{\log_a x}=x\quad(x>0),
\qquad
\log_a\left(a^{x}\right)=x\quad(x\in\mathbb{R})
$$

The inverse-function pair. There is **no** identity for $\log_a(x+y)$: a sum inside a logarithm
cannot be split.

## 5. Hyperbolic Identities

The hyperbolic functions are defined by

$$
\cosh x=\frac{e^x+e^{-x}}{2},\qquad
\sinh x=\frac{e^x-e^{-x}}{2},\qquad
\tanh x=\frac{\sinh x}{\cosh x}
$$

so every identity below is a statement about exponentials.

$$
\cosh^2x-\sinh^2x=1
$$

The hyperbolic analogue of the Pythagorean identity, and the reason $(\cosh t,\sinh t)$ parametrises
the hyperbola $u^2-v^2=1$.

$$
1-\tanh^2x=\operatorname{sech}^2x,\qquad
\coth^2x-1=\operatorname{csch}^2x
$$

Obtained from the previous identity by dividing by $\cosh^2x$ and $\sinh^2x$ respectively.

$$
\sinh(x\pm y)=\sinh x\cosh y\pm\cosh x\sinh y
$$

$$
\cosh(x\pm y)=\cosh x\cosh y\pm\sinh x\sinh y
$$

$$
\tanh(x\pm y)=\frac{\tanh x\pm\tanh y}{1\pm\tanh x\tanh y}
$$

The addition formulas; note the plus sign in the denominator of the tangent formula, opposite to the
circular case.

$$
\sinh2x=2\sinh x\cosh x,\qquad
\cosh2x=\cosh^2x+\sinh^2x=2\cosh^2x-1=1+2\sinh^2x
$$

$$
\sinh^2x=\frac{\cosh2x-1}{2},\qquad
\cosh^2x=\frac{\cosh2x+1}{2}
$$

The double-angle and power-reduction identities, which mirror the circular ones.

$$
\sinh x\sinh y=\frac12\left[\cosh(x+y)-\cosh(x-y)\right]
$$

$$
\cosh x\cosh y=\frac12\left[\cosh(x+y)+\cosh(x-y)\right]
$$

$$
\sinh x\cosh y=\frac12\left[\sinh(x+y)+\sinh(x-y)\right]
$$

Product-to-sum for hyperbolic functions, useful in solving wave-like equations with exponential
profiles.

$$
\operatorname{arsinh}x=\ln\left(x+\sqrt{x^2+1}\right)\ (x\in\mathbb{R}),
\qquad
\operatorname{arcosh}x=\ln\left(x+\sqrt{x^2-1}\right)\ (x\ge1)
$$

$$
\operatorname{artanh}x=\frac12\ln\frac{1+x}{1-x}\qquad(\lvert x\rvert<1)
$$

The inverse functions in logarithmic form; the domains are exactly the ranges of the corresponding
hyperbolic functions.

The link to the circular functions is

$$
\cosh(ix)=\cos x,\qquad
\sinh(ix)=i\sin x,\qquad
\tanh(ix)=i\tan x
$$

so every circular identity has a hyperbolic twin, obtained by the rule "replace $\sin$ by $i\sinh$
and use $\cosh^2-\sinh^2=1$".

## 6. Combinatorial Identities

$$
\binom{n}{k}=\binom{n}{n-k}\qquad(0\le k\le n)
$$

Symmetry: choosing $k$ elements to keep is the same as choosing $n-k$ to discard.

$$
\binom{n}{k}=\binom{n-1}{k-1}+\binom{n-1}{k}\qquad(1\le k\le n-1)
$$

Pascal's rule: split the $k$-subsets by whether they contain a fixed element. This is the identity
behind Pascal's triangle and every induction on binomial coefficients.

$$
\binom{n}{k}=\frac{n}{k}\binom{n-1}{k-1}\qquad(1\le k\le n)
$$

The absorption identity; it moves a factor of $k$ or $n$ out of a binomial coefficient and is the
standard tool for summing $k\binom nk$.

$$
(x+y)^n=\sum_{k=0}^{n}\binom{n}{k}x^{n-k}y^{k}\qquad(n\in\mathbb{N}_0)
$$

The binomial theorem: expand by choosing $y$ from $k$ of the $n$ factors.

$$
\sum_{k=0}^{n}\binom{m}{k}\binom{n}{r-k}=\binom{m+n}{r}\qquad(r\le m+n)
$$

Vandermonde's identity: count the $r$-subsets of an $(m+n)$-element set by how many elements they
take from the first $m$.

$$
\sum_{i=r}^{n}\binom{i}{r}=\binom{n+1}{r+1}\qquad(0\le r\le n)
$$

The hockey-stick identity: a sum down a diagonal of Pascal's triangle equals the entry at the end of
the next diagonal.

$$
\sum_{k=0}^{n}\binom{n}{k}=2^n
$$

Counting all subsets of an $n$-element set, or setting $x=y=1$ in the binomial theorem.

$$
\sum_{k=0}^{n}(-1)^k\binom{n}{k}=0\qquad(n\ge1),
\qquad
\sum_{k=0}^{n}k\binom{n}{k}=n2^{n-1}
$$

The alternating sum counts subsets of even size minus those of odd size; the second identity is the
absorption identity applied term by term, or the derivative of $(1+x)^n$ at $x=1$.

$$
\sum_{k=0}^{n}\binom{n}{k}^{2}=\binom{2n}{n}
$$

The special case $m=n$, $r=n$ of Vandermonde; it counts the $n$-subsets of a $2n$-element set.

$$
\binom{-n}{k}=(-1)^k\binom{n+k-1}{k}
$$

Upper negation, for $n>0$; it converts a negative upper index into an ordinary binomial coefficient
and underlies the negative-binomial series.

$$
\left(x_1+x_2+\cdots+x_m\right)^n
=\sum_{k_1+\cdots+k_m=n}\frac{n!}{k_1!\,k_2!\cdots k_m!}\,x_1^{k_1}x_2^{k_2}\cdots x_m^{k_m}
$$

The multinomial theorem, for $n\in\mathbb{N}_0$; the binomial theorem is the case $m=2$.

## 7. How Identities Are Proved

Every identity on this page is a theorem, and every theorem has a proof. Three techniques cover
almost all of them.

**From the definitions.** The Pythagorean identity is the statement that the point
$(\cos\theta,\sin\theta)$ lies on the unit circle $x^2+y^2=1$. The hyperbolic identities are
statements about $e^x$ and $e^{-x}$: expanding $\cosh^2x-\sinh^2x$ gives
$\frac14\left(e^{2x}+2+e^{-2x}\right)-\frac14\left(e^{2x}-2+e^{-2x}\right)=1$. The logarithmic
product rule follows from $a^{u}a^{v}=a^{u+v}$ by writing $x=a^u$, $y=a^v$.

**By a transformation that is already known.** The sum formula for sine follows from the rotation
matrices: applying a rotation by $B$ and then by $A$ is a rotation by $A+B$, and comparing the
top-right entries of $R_AR_B$ and $R_{A+B}$ gives
$\sin(A+B)=\sin A\cos B+\cos A\sin B$. The double-angle formulas are the case $A=B$. De Moivre's
theorem, $(\cos\theta+i\sin\theta)^n=\cos n\theta+i\sin n\theta$, generates the multiple-angle
identities by expanding the left side.

**By counting one set in two ways.** Vandermonde's identity counts $r$-subsets of $\{1,\dots,m+n\}$
by the number taken from the first block. The hockey-stick identity counts the $(r+1)$-subsets of
$\{1,\dots,n+1\}$ by their largest element. Pascal's rule counts $k$-subsets by whether they contain
a fixed element. When both sides of a proposed identity count the same objects, the identity is
proved — this is the standard *double-counting* argument.

**By induction.** Pascal's rule gives $\binom{n}{k}$ from the previous row, so every sum identity in
$n$ can be proved by induction once the base case is checked. The binomial theorem itself is proved
this way, or by the counting argument above.

## 8. Which Identity to Reach For

| If the expression contains | Reach for | Because |
|---|---|---|
| $\sin^2\theta$ and $\cos^2\theta$ together | Pythagorean identity | it eliminates one of them |
| a product $\sin A\cos B$ or $\sin A\sin B$ | product-to-sum | a sum is easier to integrate or to bound |
| a sum $\sin A+\sin B$ | sum-to-product | a product reveals the zeros and the amplitude |
| $2\theta$ | double-angle identity | it lowers the angle |
| $\theta/2$ or a square root of $1\pm\cos\theta$ | half-angle identity | it removes the square root, at the cost of a sign |
| $a\sin x+b\cos x$ | auxiliary angle | one wave with amplitude $\sqrt{a^2+b^2}$ |
| $a^3\pm b^3$ | sum or difference of cubes | it factorises over the reals |
| $a^n-b^n$ | geometric factorisation | $a-b$ is always a factor |
| $\log(xy)$ or $\log(x/y)$ | product and quotient rules | it splits a product into a sum |
| $\sum_k\binom{n}{k}\binom{m}{r-k}$ | Vandermonde | the sum collapses to one coefficient |
| $\sum_{i=r}^{n}\binom{i}{r}$ | hockey stick | the sum collapses to one coefficient |
| the same finite set described in two ways | double counting | the two counts are equal |

---

*Part of the [Reference Library](../README.md). Notation follows
[MATHEMATICAL_NOTATION.md](../../MATHEMATICAL_NOTATION.md); terms are defined in
[GLOSSARY.md](../../GLOSSARY.md); the curriculum itself begins at [README.md](../../README.md).*
