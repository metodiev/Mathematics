# Random Variables — Solutions

> [Random Variables](README.md) · Solutions to the 36 problems in [exercises.md](exercises.md)

Each solution states the strategy, carries out every significant step and ends with a check. Proofs are
complete. Pitfalls are flagged where the problem is designed to expose one.

## Beginner

**1.** *(Strategy: a mass function is a list of non-negative numbers summing to $1$; read every probability off
the list.)*

(a) $0.2+0.5+0.3=1$ and all values are non-negative, so this is a mass function.

(b) $\Pr(X\le1)=p(0)+p(1)=0.2+0.5=0.7$; $\Pr(X\ge1)=p(1)+p(2)=0.5+0.3=0.8$;
$\Pr(0<X<2)=p(1)=0.5$, since $1$ is the only support point strictly inside $(0,2)$; $\Pr(X=2)=0.3$.

(c) $F(1.5)=\Pr(X\le1.5)=p(0)+p(1)=0.7$ and $F(2)=1$.

(d) $F$ is a staircase: $F=0$ on $(-\infty,0)$, $0.2$ on $[0,1)$, $0.7$ on $[1,2)$, $1$ on $[2,\infty)$, with jumps
of size $0.2,0.5,0.3$ at $0,1,2$.

*Check:* the jumps sum to $1$, and $F$ is right-continuous with $F(1)=0.7$, the value on $[1,2)$. ✓

**2.** *(Strategy: normalise, integrate to get $F$, then solve $F(x)=p$.)*

(a) $\int_0^1cx^2dx=c/3$, so $c=3$.

(b) $F(x)=0$ for $x<0$; $F(x)=\int_0^x3t^2dt=x^3$ for $0\le x<1$; $F(x)=1$ for $x\ge1$.

(c) $\Pr(X>1/2)=1-F(1/2)=1-\tfrac18=\tfrac78$.

(d) By (b), $F$ is continuous and strictly increasing on $[0,1]$, so $Q(1/2)$ solves $x^3=\tfrac12$, i.e.
$Q(1/2)=2^{-1/3}=1/\sqrt[3]{2}\approx0.7937$.

*Check:* $F(1)=1$ and $F(0)=0$; $\Pr(X\le1/2)=1/8$ and $\Pr(X>1/2)=7/8$ sum to $1$. ✓

**3.** *(Strategy: the uniform density is the reciprocal of the interval length.)*

(a) $f(x)=\tfrac14$ on $(2,6)$ and $0$ elsewhere; $F(x)=0$ for $x<2$, $F(x)=(x-2)/4$ for $2\le x<6$, $F(x)=1$
for $x\ge6$.

(b) $\Pr(2.5<X<4)=F(4^{-})-F(2.5)=\tfrac{4-2}{4}-\tfrac{2.5-2}{4}=\tfrac{2}{4}-\tfrac{0.5}{4}=\tfrac{1.5}{4}=0.375$.

(c) $(m-2)/4=\tfrac12$ gives $m=4$ — the midpoint, as symmetry demands.

(d) $\Pr(X=3)=0$: $X$ has a density, so every point has probability zero (Proposition 8.4).

*Check:* $\Pr(X<2.5)=\Pr(X>5.5)=0.125$ by symmetry, and $0.125+0.375+0.25+0.125=1$ for the four quarters. ✓

**4.** *(Strategy: integrate the density or use $\Pr(X>t)=e^{-\lambda t}$.)*

(a) $\int_0^\infty2e^{-2x}dx=\bigl[-e^{-2x}\bigr]_0^\infty=0-(-1)=1$, and the integrand is non-negative.

(b) $\Pr(X>1)=e^{-2}\approx0.1353$; $\Pr(X\le0.5)=1-e^{-1}\approx0.6321$.

(c) $1-e^{-2m}=\tfrac12$ gives $e^{-2m}=\tfrac12$, so $m=\tfrac{\ln2}{2}\approx0.3466$.

(d) $\Pr(X=1)=0$, again by Proposition 8.4.

*Check:* $\Pr(X>1)+\Pr(X\le1)=e^{-2}+(1-e^{-2})=1$. ✓

**5.** *(Strategy: read masses off the jumps of the staircase, remembering that a CDF is right-continuous.)*

(a) $F$ is nondecreasing with values in $[0,1]$; at $x=0$, $F(0)=0.2$ equals the right limit; at $x=1$,
$F(1)=0.7$ equals the right limit; at $x=3$, $F(3)=1$. Limits at $\pm\infty$ are $0$ and $1$. So $F$ satisfies
Theorem 8.2.

(b) The jumps are $F(0)-F(0^{-})=0.2-0=0.2$, $F(1)-F(1^{-})=0.7-0.2=0.5$, $F(3)-F(3^{-})=1-0.7=0.3$. Hence
$p(0)=0.2$, $p(1)=0.5$, $p(3)=0.3$.

(c) $\Pr(0.5<X\le2.5)=F(2.5)-F(0.5)=0.7-0.2=0.5$ — this counts the atom at $1$ and nothing else.
$\Pr(X=1.5)=0$ because $F$ is constant in a neighbourhood of $1.5$.

(d) $F(0)=0.2<0.5\le0.7=F(1)$, so $Q(0.5)=1$; $F(1)=0.7<0.8\le1=F(3)$, so $Q(0.8)=3$.

*Check:* masses $0.2+0.5+0.3=1$; $\Pr(0.5<X\le2.5)=0.5$ equals $p(1)$ because $1$ is the only atom in the
interval. ✓

**6.** *(Strategy: differentiate the CDF inside the smooth piece.)*

(a) $x^3$ is nondecreasing on $[0,1]$ with $0^3=0$ and $1^3=1$, so $F$ is continuous at $1$ and at $0$;
$F$ is right-continuous everywhere and has the required limits.

(b) For $0<x<1$, $f(x)=F'(x)=3x^2$.

(c) $\Pr(X\le0.5)=F(0.5)=0.125$ and $\Pr(0.5<X<1)=F(1^{-})-F(0.5)=1-0.125=0.875$.

(d) $x^3=\tfrac12$ gives $Q(1/2)=2^{-1/3}\approx0.7937$.

*Check:* $\int_0^13x^2dx=1$, so $f$ is a density; $\Pr(X\le0.5)=1/8$ matches $F(0.5)$. ✓

**7.** *(Strategy: the density is the derivative of the CDF; its size is not a probability.)*

(a) $\int_0^12x\,dx=\bigl[x^2\bigr]_0^1=1$ and $f\ge0$.

(b) $F(x)=x^2$ on $[0,1]$, with $0$ and $1$ outside. Then $\Pr(0.2<X<0.6)=F(0.6)-F(0.2)=0.36-0.04=0.32$.

(c) The supremum of $f$ is $2$, approached as $x\to1$ (not attained on the open interval). A density may exceed
$1$: it is a rate per unit length, and the support has length $1$, so the total is $\int_0^12x\,dx=1$.

(d) $\Pr(X=0.5)=0$.

*Check:* $\Pr(0<X<0.5)=0.25$ and $\Pr(0.5<X<1)=0.75$; they sum to $1$. ✓

**8.** *(Strategy: verify normalisation, then interpret the density as a rate.)*

(a) $\int_0^{1/2}2\,dx=1$, so $f$ is a density. The value $2$ is a probability *per unit length*: a short
interval of length $h$ inside the support carries probability $2h$, which is at most $1$ because
$h\le\tfrac12$.

(b) $F(x)=0$ for $x<0$, $F(x)=2x$ for $0\le x<\tfrac12$, $F(x)=1$ for $x\ge\tfrac12$.

(c) $\Pr(X=0.25)=0$; $\Pr(0.25<X<0.5)=2(0.5-0.25)=0.5$; $\Pr(0.24<X<0.26)=2(0.02)=0.04$.

(d) The comparison is meaningful only for *intervals*: on a small window around $0.25$, $X$ is exactly twice as
likely as a uniform variable on $(0,1)$ — not "more than twice". The phrase "X is more than twice as likely to be
near 0.25" is loose; the precise statement is that the density ratio is $2/1=2$.

*Check:* $2(0.26-0.24)=0.04$, and $0.04\to0$ as the window shrinks, consistent with $\Pr(X=0.25)=0$. ✓

**9.** *(Strategy: work from events, then confirm with the formula.)*

(a) $F_Y(y)=\Pr(3X+1\le y)=\Pr\bigl(X\le\tfrac{y-1}{3}\bigr)$ equals $0$ for $y<1$, $\tfrac{y-1}{3}$ for
$1\le y<4$, and $1$ for $y\ge4$. Differentiating, $f_Y(y)=\tfrac13$ on $(1,4)$.

(b) With $a=3$, $b=1$: $f_Y(y)=\tfrac13f_X\bigl(\tfrac{y-1}{3}\bigr)=\tfrac13$ for $y\in(1,4)$, since the argument
lies in $(0,1)$. Agrees.

(c) $Q_Y(p)=3p+1$ because $F_Y(y)=p\iff(y-1)/3=p$; and $Q_X(p)=p$, so $3Q_X(p)+1=3p+1$. ✓

*Check:* $\int_1^4\tfrac13dy=1$; $\Pr(2<Y<3)=\tfrac13$ equals $\Pr\bigl(\tfrac13<X<\tfrac23\bigr)=\tfrac13$. ✓

**10.** *(Strategy: sum over preimages — but only those in the support.)*

(a) For $y\in(0,1)$ the equation $x^2=y$ has solutions $\pm\sqrt y$, but only $+\sqrt y$ lies in $(0,1)$, the
support of $X$. So the sum has one term:
$f_Y(y)=f_X(\sqrt y)/\lvert2\sqrt y\rvert=1/(2\sqrt y)$ on $(0,1)$, and $0$ elsewhere.

(b) For $0\le y\le1$, $F_Y(y)=\Pr(X^2\le y)=\Pr(0<X\le\sqrt y)=\sqrt y$; differentiating gives $1/(2\sqrt y)$,
matching (a).

(c) $Y$ is not uniform: its density $1/(2\sqrt y)$ grows without bound as $y\downarrow0$, so small values are
much more likely per unit length. It still integrates to $1$: $\int_0^1(2\sqrt y)^{-1}dy=\bigl[\sqrt y\bigr]_0^1=1$.

*Check:* $\Pr(Y\le0.25)=\sqrt{0.25}=0.5$, and indeed $\Pr(X\le0.5)=0.5$. ✓ *Pitfall:* including $-\sqrt y$ would
double the density and produce total mass $2$.

**11.** *(Strategy: marginalise by summing rows and columns; test independence at one cell.)*

(a) $p_X(0)=0.1+0.2=0.3$, $p_X(1)=0.3+0.4=0.7$; $p_Y(0)=0.1+0.3=0.4$, $p_Y(1)=0.2+0.4=0.6$.

(b) $\Pr(Y=1\mid X=0)=\dfrac{p(0,1)}{p_X(0)}=\dfrac{0.2}{0.3}=\dfrac23$.

(c) $p_X(0)p_Y(0)=0.3\cdot0.4=0.12\ne0.1=p(0,0)$, so $X$ and $Y$ are **not** independent.

(d) $\Pr(X=Y)=p(0,0)+p(1,1)=0.1+0.4=0.5$.

*Check:* the four joint masses sum to $1$, and the marginals sum to $1$ each. ✓

**12.** *(Strategy: integrate out one variable at a time; a product density in a rectangular support factorises.)*

(a) $\int_0^1\!\int_0^14xy\,dy\,dx=4\bigl(\tfrac12\bigr)\bigl(\tfrac12\bigr)=1$ and $4xy\ge0$ on the square.

(b) $f_X(x)=\int_0^14xy\,dy=4x\cdot\tfrac12=2x$ on $[0,1]$; by symmetry $f_Y(y)=2y$.

(c) $f_X(x)f_Y(y)=2x\cdot2y=4xy=f_{X,Y}(x,y)$ for all $(x,y)$, so the variables are independent
(Proposition 8.8(ii)).

(d) By symmetry of the joint density under swapping coordinates, $\Pr(X<Y)=\Pr(Y<X)$, and
$\Pr(X=Y)=0$ because the pair has a density. So $\Pr(X<Y)=\tfrac12$.

*Check:* direct computation, $\int_0^1\!\int_x^14xy\,dy\,dx=\int_0^12x(1-x^2)dx=2\bigl(\tfrac12-\tfrac14\bigr)=\tfrac12$.
✓

## Intermediate

**13.** *(Strategy: continuity of $F$ means no atom; a jump means an atom.)*

(a) $x^2/2$ is nondecreasing and continuous on $[0,1)$, with limit $\tfrac12$ at $x=1$; the value at $1$ is $1$, and
$F$ is constant $1$ afterwards. Limits at $\pm\infty$ are $0$ and $1$, and $F$ is right-continuous. So $F$ is a CDF.

(b) $F$ has one jump, at $x=1$, of size $1-\tfrac12=\tfrac12$: an atom of mass $\tfrac12$ at $1$. On $(0,1)$,
$F'=x$, so the density part is $x$, whose integral is $\int_0^1x\,dx=\tfrac12$. Total mass $\tfrac12+\tfrac12=1$. ✓

(c) $\Pr(0.5<X<1)=F(1^{-})-F(0.5)=\tfrac12-\tfrac18=\tfrac38$; $\Pr(X=1)=\tfrac12$.

(d) For $x<1$, $F(x)=x^2/2<\tfrac12$; $F(1)=1\ge\tfrac12$. So $Q(\tfrac12)=1$.

*Check:* $\Pr(X<1)=\tfrac38+\Pr(X\le0.5)=\tfrac38+\tfrac18=\tfrac12$, and adding $\Pr(X=1)=\tfrac12$ gives $1$. ✓

**14.** *(Strategy: solve $F(x)=u$; a continuous strictly increasing $F$ has an honest inverse.)*

(a) $1-e^{-x}=u\iff e^{-x}=1-u\iff x=-\ln(1-u)$, so $Q(u)=-\ln(1-u)$.

(b) $Q(\tfrac14)=\ln\tfrac43\approx0.2877$, $Q(\tfrac12)=\ln2\approx0.6931$, $Q(\tfrac34)=\ln4\approx1.3863$;
$\operatorname{IQR}=\ln4-\ln\tfrac43=\ln3\approx1.0986$.

(c) $F(Q(\tfrac14))=1-e^{-\ln(4/3)}=1-\tfrac34=\tfrac14$.

(d) $\Pr(X>x)=e^{-x}=0.1$ gives $x=\ln10\approx2.3026$.

*Check:* $Q$ is increasing and $F(Q(0.75))=\tfrac34$; the median is between the quartiles. ✓

**15.** *(Strategy: two preimages, each contributing $f_X/(2\lvert x\rvert)$.)*

(a) The support of $X$ is $(-2,2)$ with $f_X=\tfrac14$. For $0<y<4$ both $\pm\sqrt y$ lie in $(-2,2)$, so

$$
f_Y(y)=\frac{\tfrac14+\tfrac14}{2\sqrt y}=\frac{1}{4\sqrt y},
$$

and $f_Y(y)=0$ for $y\le0$ or $y\ge4$.

(b) $\int_0^4\dfrac{dy}{4\sqrt y}=\dfrac{1}{4}\bigl[2\sqrt y\bigr]_0^4=\dfrac{1}{4}\cdot4=1$.

(c) From the density: $\int_0^1\dfrac{dy}{4\sqrt y}=\dfrac{2}{4}=\dfrac12$. Directly:
$\Pr(X^2\le1)=\Pr(-1\le X\le1)=\dfrac{2}{4}=\dfrac12$. ✓

*Check:* the CDF route gives $F_Y(y)=\Pr(-\sqrt y\le X\le\sqrt y)=\sqrt y/2$ for $0\le y\le4$, whose derivative is
$1/(4\sqrt y)$. ✓

**16.** *(Strategy: two routes to the same law.)*

(a) For $0<y<1$, $F_Y(y)=\Pr(e^{-X}\le y)=\Pr(-X\le\ln y)=\Pr(X\ge-\ln y)=e^{-(-\ln y)}=y$, using
$\Pr(X\ge t)=e^{-t}$ for $t\ge0$. For $y\le0$, $F_Y=0$; for $y\ge1$, $F_Y=1$.

(b) $F_Y(y)=y$ on $(0,1)$, so $f_Y(y)=1$ there: $Y\sim\text{Uniform}(0,1)$.

(c) With $h(y)=-\ln y$ and $\lvert h'(y)\rvert=1/y$, and $f_X(-\ln y)=e^{-(-\ln y)}=y$,
$f_Y(y)=y\cdot\tfrac1y=1$. Agrees. ✓

*Check:* $\int_0^11\,dy=1$; the transformation reverses the exponential into a uniform, which is inverse transform
sampling with $Q(u)=-\ln(1-u)$. ✓

**17.** *(Strategy: mixture density is the weighted sum; the two variance formulas must agree.)*

(a) $f(x)=\tfrac12$ on $(0,1)$ and on $(2,3)$, and $f(x)=0$ between $1$ and $2$. The density has two separate
blocks of equal height.

(b) $\mathbb{E}[X]=\tfrac12(0.5)+\tfrac12(2.5)=1.5$. Then
$\mathbb{E}[X^2]=\tfrac12\bigl(\tfrac1{12}+\tfrac14\bigr)+\tfrac12\bigl(\tfrac1{12}+\tfrac{25}4\bigr)
=\tfrac12\cdot\tfrac13+\tfrac12\cdot\tfrac{19}3=\tfrac{10}3$, so
$\operatorname{Var}(X)=\tfrac{10}3-\tfrac94=\tfrac{13}{12}\approx1.0833$.

(c) Directly, $\mathbb{E}[X]=\int_0^1\tfrac{x}2dx+\int_2^3\tfrac{x}2dx=\tfrac14+\tfrac54=1.5$; and
$\mathbb{E}[X^2]=\tfrac12\cdot\tfrac13+\tfrac12\cdot\tfrac{19}3=\tfrac{10}3$, as above. Agrees.

(d) The density is constant on each of two disjoint intervals and zero between them, so it has two modes (each a
whole interval of maximisers). The variance decomposition shows why: the within-component variance is only
$\tfrac12\cdot\tfrac1{12}+\tfrac12\cdot\tfrac1{12}=\tfrac1{12}$, while the between-component term is
$\tfrac12(0.5-1.5)^2+\tfrac12(2.5-1.5)^2=1$, and $\tfrac1{12}+1=\tfrac{13}{12}$. ✓

*Check:* $\int_0^1\tfrac12+\int_2^3\tfrac12=1$. ✓

**18.** *(Strategy: the support is a triangle; integrate with the correct limits.)*

(a) $\int_0^1\!\int_0^{1-x}24xy\,dy\,dx=\int_0^112x(1-x)^2dx=12\bigl(\tfrac12-\tfrac23+\tfrac14\bigr)=12\cdot\tfrac1{12}=1$.

(b) $f_X(x)=\int_0^{1-x}24xy\,dy=12x(1-x)^2$ for $0\le x\le1$; by symmetry $f_Y(y)=12y(1-y)^2$.

(c) $f_{Y\mid X}(y\mid x)=\dfrac{24xy}{12x(1-x)^2}=\dfrac{2y}{(1-x)^2}$ for $0\le y\le1-x$. Then
$\int_0^{1-x}\dfrac{2y}{(1-x)^2}dy=\dfrac{(1-x)^2}{(1-x)^2}=1$, and the CDF is $\bigl(y/(1-x)\bigr)^2$ — the
conditional law is that of $(1-X)U$ with $U\sim\text{Uniform}(0,1)$, i.e. a triangular law on $[0,1-x]$.

(d) Put $x=\tfrac12$: $f_{Y\mid X}(y\mid\tfrac12)=8y$ on $[0,\tfrac12]$, so
$\Pr\bigl(Y\le\tfrac14\mid X=\tfrac12\bigr)=\int_0^{1/4}8y\,dy=4\cdot\tfrac1{16}=\tfrac14$.

(e) $f_Xf_Y=144xy(1-x)^2(1-y)^2\ne24xy$ (for instance at $x=y=\tfrac12$: $2.25$ versus $6$), so the variables are
dependent.

*Check:* $f_X$ integrates to $1$ by part (a); the value $f_X(0.5)=1.5$ is a density value, not a mass, and the
conditional density integrates to $1$ for each $x$ by part (c). ✓

**19.** *(Strategy: a product density on a rectangle means independence.)*

(a) $\int_0^1\!\int_0^16xy^2\,dy\,dx=6\cdot\tfrac12\cdot\tfrac13=1$. Then
$f_X(x)=\int_0^16xy^2dy=2x$ and $f_Y(y)=\int_0^16xy^2dx=3y^2$.

(b) $2x\cdot3y^2=6xy^2$ everywhere, so $X\perp\!\!\!\perp Y$.

(c) $\Pr(X<Y)=\int_0^1\!\int_x^16xy^2dy\,dx=\int_0^12x(1-x^3)dx=2\bigl(\tfrac12-\tfrac15\bigr)=\tfrac35$.

(d) $f_{X\mid Y}(x\mid y)=\dfrac{6xy^2}{3y^2}=2x$ on $[0,1]$, and $\int_0^12x\,dx=1$. ✓

*Check:* since $X$ and $Y$ are independent, $f_{X\mid Y}=f_X=2x$, as computed. ✓

**20.** *(Strategy: compute the CDF of the transformed variable; use $F(X)=X^2$ here.)*

(a) For $0\le u\le1$, $\Pr(F(X)\le u)=\Pr(X^2\le u)=\Pr(X\le\sqrt u)=(\sqrt u)^2=u$. So $F(X)\sim\text{Uniform}(0,1)$.

(b) $X^2=F(X)$ is uniform on $(0,1)$.

(c) For $Y=-\ln X$ and $y\ge0$: $\Pr(Y\le y)=\Pr(X\ge e^{-y})=1-F(e^{-y})=1-e^{-2y}$, so $Y\sim\text{Exp}(2)$ with
density $2e^{-2y}$.

(d) With $f_X(x)=2x$ on $(0,1)$ and the single preimage $\sqrt y$,
$f_Y(y)=f_X(\sqrt y)/(2\sqrt y)=2\sqrt y/(2\sqrt y)=1$ on $(0,1)$: uniform, consistent with (b). ✓

*Check:* $\int_0^12e^{-2y}dy=1$; the three answers form the chain $X\mapsto X^2\mapsto-\ln X^2$, an exponential. ✓

**21.** *(Strategy: the density of $e^X$ carries the factor $1/y$ from the inverse.)*

(a) $h(y)=\ln y$, $\lvert h'(y)\rvert=1/y$, so $f_Y(y)=\dfrac{\varphi(\ln y)}{y}
=\dfrac{1}{y\sqrt{2\pi}}\exp\!\bigl(-\tfrac{(\ln y)^2}{2}\bigr)$ for $y>0$.

(b) With $y=e^x$, $dy=e^xdx$ and $\int_0^\infty\dfrac{\varphi(\ln y)}{y}dy=\int_{-\infty}^{\infty}\varphi(x)dx=1$.

(c) $\Pr(Y\le1)=\Pr(X\le0)=\tfrac12$; $\Pr(1<Y<e)=\Pr(0<X<1)=\Phi(1)-\Phi(0)\approx0.8413-0.5=0.3413$.

(d) $X\mapsto e^X$ stretches the right half-line and compresses the left, so equal-length intervals in $x$ become
intervals of very different lengths in $y$; the density $\varphi(\ln y)/y$ is therefore asymmetric, with a long
right tail, and $Y>0$ always.

*Check:* $f_Y(y)\to0$ as $y\to0^+$ (because $\varphi(\ln y)\to0$ faster than $1/y$ grows) and as $y\to\infty$. ✓

**22.** *(Strategy: use independence to multiply CDFs.)*

(a) $F_Z(z)=\Pr(X\le z,\,Y\le z)=z\cdot z=z^2$ for $0\le z\le1$, so $f_Z(z)=2z$ there.

(b) $\Pr(Z>0.5)=1-F_Z(0.5)=1-\tfrac14=\tfrac34$.

(c) $z^2=\tfrac12$ gives the median $1/\sqrt2\approx0.7071$.

(d) Given $Z=z$, one of $X,Y$ equals $z$ and the other is uniform on $(0,z)$; each possibility has "weight
$\tfrac12$" in the limit. Hence
$\Pr\bigl(X\le z/2\mid Z=z\bigr)=\tfrac12\cdot\Pr(U\le z/2)+\tfrac12\cdot1=\tfrac12\cdot\tfrac12+\tfrac12=\tfrac34$.
This is delicate because $\{Z=z\}$ has probability zero; the conditional law is obtained as a limit of
$\Pr(\cdot\mid z<Z\le z+h)$, i.e. from the conditional density (Definition in §7.8), not from
$\Pr(A\cap\{Z=z\})/\Pr(Z=z)$.

*Check:* $\int_0^12z\,dz=1$, and $\Pr(Z\le0.5)=0.25$ matches $z^2$ at $z=0.5$. ✓

## Advanced

**23.** *(Strategy: use only the definition $Q(p)=\inf S_p$ with $S_p=\{x:F(x)\ge p\}$, plus the fact that $S_p$
is upward closed.)*

(a) Suppose first that $t<x$ and $F(t)\ge p$. Then $t\in S_p$, so $Q(p)\le t<x$. Conversely, if $Q(p)<x$, put
$\varepsilon=x-Q(p)>0$. A greatest lower bound is exceeded by no smaller bound, so $Q(p)+\varepsilon=x$ is not a
lower bound for $S_p$: some $t\in S_p$ satisfies $t<x$. Then $F(t)\ge p$, as required. Hence
$Q(p)<x\iff\exists t<x$ with $F(t)\ge p$.

(b) $S_p$ is upward closed: if $t\in S_p$ and $s\ge t$, then $F(s)\ge F(t)\ge p$, so $s\in S_p$. Hence
$Q(p)+1/n\in S_p$ for every $n$, and right-continuity gives
$F(Q(p))=\lim_nF(Q(p)+1/n)\ge p$. Therefore $Q(p)\in S_p$, and as $Q(p)$ is a lower bound for $S_p$ it is the
least element: $Q(p)=\min S_p$.

(c) If $F$ is continuous and strictly increasing where the mass sits, $F$ is a bijection from that interval onto
$(0,1)$ and $Q=F^{-1}$ with $F(Q(p))=p$. Then for any $x$ in the interval,
$$
Q(p)<x\iff F(Q(p))<F(x)\iff p<F(x),
$$
using strict monotonicity in both directions. The strict inequality comes from strict monotonicity alone: if $F$
is merely nondecreasing, $Q(p)<x$ can hold together with $p=F(x)$.

(d) *First example* (discrete). Let $\Pr(X=0)=\Pr(X=1)=\tfrac12$, take $p=\tfrac12$ and $x=1$. Then
$F(1^{-})=\tfrac12=p$ and $Q(\tfrac12)=0<1$: here $Q(p)<x$ holds together with $p=F(x^{-})$.

*Second example* (continuous). Let $X\sim\text{Uniform}(0,1)$, take $p=\tfrac12$ and $x=\tfrac12$. Then
$F(x^{-})=F(x)=\tfrac12=p$, but $Q(\tfrac12)=\tfrac12=x$, so $Q(p)<x$ is **false** although $p\le F(x^{-})$ is
**true**. So the identity $Q(p)<x\iff p\le F(x^{-})$ fails, and the reason is visible: at a level $p$ that $F$
reaches exactly at $x$ and not before, the infimum $Q(p)$ equals $x$ rather than being strictly below it. The
correct statements are (a) for the strict inequality and $Q(p)\le x\iff p\le F(x)$ (Proposition 8.6(ii)) for the
non-strict one.

*Check:* in the second example, $F$ is continuous and strictly increasing, so by part (c) $Q(p)<x\iff p<F(x)$;
with $p=F(x)$ the strict inequality fails exactly as predicted. ✓

**24.** *(Strategy: integrals cannot see sets of length zero.)*

(a) On $(0,1)$, $g=f+\mathbf{1}_{\mathbb{Q}}$ equals $2$ at rational points and $1$ at irrational points; outside
$(0,1)$ it equals $\mathbf{1}_{\mathbb{Q}}$ (plus $0$). It is non-negative. Since $\mathbb{Q}$ is countable, it
has length zero, so $\int_{\mathbb{R}}g=\int_{\mathbb{R}}f+0=1$: $g$ is a density. Moreover for every Borel $B$,
$\int_Bg=\int_Bf+\int_{B\cap\mathbb{Q}}1=\int_Bf$, because $B\cap\mathbb{Q}$ is countable and hence has length
zero. So $g$ defines exactly the same distribution as $f$.

(b) At any $x\in(0,1)$ and any $\delta>0$, the interval $(x-\delta,x+\delta)$ contains rationals (where $g=2$) and
irrationals (where $g=1$), so $g$ oscillates between $1$ and $2$ in every neighbourhood of $x$: it is
discontinuous at every point of $(0,1)$. And $g\ne f$ exactly on $\mathbb{Q}\cap(0,1)$, which is countable and
dense.

(c) A density is therefore determined only up to equality almost everywhere; "the density at a point" is not a
well-defined notion. The CDF, however, is defined as $F(x)=\Pr(X\le x)$ without reference to any density, so it is
unique, and so is the distribution.

(d) No. If $f$ and $g$ are both continuous and define the same distribution, then $\int_0^x(f-g)=0$ for every $x$;
the function $x\mapsto\int_0^x(f-g)$ has derivative $f-g$ by the fundamental theorem (the integrand is
continuous), so $f(x)-g(x)=0$ for every $x$. Continuity is what upgrades "almost everywhere" to "everywhere".

*Check:* an indicator of a countable set integrates to zero yet is not the zero function — exactly the
phenomenon exploited here. ✓

**25.** *(Strategy: the CDF of $X^2$ is a difference of two values of $F_X$; differentiate with the chain rule.)*

(a) For $y\le0$, $\{X^2\le y\}=\varnothing$, so $F_Y(y)=0$ and $f_Y(y)=0$. For $y>0$,
$$
F_Y(y)=\Pr(-\sqrt y\le X\le\sqrt y)=F_X(\sqrt y)-F_X(-\sqrt y),
$$
where the endpoints contribute nothing because $X$ has a density (Proposition 8.4). Differentiating with the chain
rule, $(\sqrt y)'=1/(2\sqrt y)$ and $(-\sqrt y)'=-1/(2\sqrt y)$, gives
$$
f_Y(y)=f_X(\sqrt y)\frac{1}{2\sqrt y}+f_X(-\sqrt y)\frac{1}{2\sqrt y}
=\frac{f_X(\sqrt y)+f_X(-\sqrt y)}{2\sqrt y}.
$$

(b) With $f_X=\varphi$ and $\varphi(-z)=\varphi(z)$,
$$
f_Y(y)=\frac{2\varphi(\sqrt y)}{2\sqrt y}=\frac{\varphi(\sqrt y)}{\sqrt y}
=\frac{e^{-y/2}}{\sqrt{2\pi y}},\qquad y>0.
$$

(c) Substitute $y=2u$, so $dy=2\,du$ and $y^{-1/2}=(2u)^{-1/2}$:
$$
\int_0^\infty\frac{e^{-y/2}}{\sqrt{2\pi y}}dy
=\frac{1}{\sqrt{2\pi}}\int_0^\infty(2u)^{-1/2}e^{-u}2\,du
=\frac{\sqrt2}{\sqrt{2\pi}}\int_0^\infty u^{-1/2}e^{-u}du
=\frac{\sqrt2\,\Gamma(\tfrac12)}{\sqrt{2\pi}}
=\frac{\sqrt2\sqrt\pi}{\sqrt{2\pi}}=1 .
$$

(d) Writing $f_X(\sqrt y)/(2\sqrt y)$ omits the branch $x=-\sqrt y$, which carries half the mass of a symmetric
$X$: the result would integrate to $\tfrac12$, not $1$, and would not be a density.

*Check:* the answer is the density of the chi-squared law with one degree of freedom, as it must be, since the
square of a standard normal is $\chi^2_1$ (next topic). ✓

**26.** *(Strategy: an atom is a jump, and jumps are bounded by the total mass.)*

(a) By Theorem 8.2(f), $\Pr(X=x)=F(x)-F(x^{-})$. Hence $\Pr(X=x)=0\iff F(x^{-})=F(x)\iff F$ is continuous at $x$.

(b) $F_d(x)=\sum_{a\in A,\,a\le x}p(a)$ with $p(a)=\Pr(X=a)\ge0$. It is nondecreasing, since adding non-negative
terms as $x$ increases. It is right-continuous: for $x_n\downarrow x$ the sets $\{a\in A:a\le x_n\}$ decrease to
$\{a\in A:a\le x\}$, and the series of non-negative terms converges (it is bounded by $1$), so the sums converge
to the sum over the intersection. It is a step function, constant between consecutive atoms and jumping by $p(a)$
at $a$. Its limits are $0$ at $-\infty$ and $\sum_{a\in A}p(a)=\Pr(X\in A)$ at $+\infty$. Countability of $A$ is
Proposition 8.3.

(c) For the CDF of Exercise 13 the only atom is $a=1$ with $p(1)=\tfrac12$. Writing $F_d(x)=\mathbf{1}_{x\ge1}$
for the unit mass at $1$ and $F_c(x)=x^2$ on $[0,1]$ (extended by $0$ below and $1$ above), the decomposition is
$$
F(x)=\tfrac12F_d(x)+\tfrac12F_c(x).
$$
Check: for $0\le x<1$ this is $\tfrac12\cdot0+\tfrac12x^2=x^2/2$, and for $x\ge1$ it is
$\tfrac12\cdot1+\tfrac12\cdot1=1$. ✓ The weights are the masses of the two parts, and each component is
normalised.

(d) There can be infinitely many atoms, one at each positive integer for instance, because the jumps of size at
least $1/n$ number at most $n$: the atom set is a countable union of finite sets. Uncountably many atoms would
require uncountably many jumps of some positive total size, contradicting that the masses sum to $1$.

*Check:* in (c), the jump of $F$ at $1$ is $1-\tfrac12=\tfrac12$, matching the weight of $F_d$. ✓

**27.** *(Strategy: independence is a statement about preimages.)*

(a) For Borel $C,D$,
$$
\Pr\bigl(g(X)\in C,\ h(Y)\in D\bigr)
=\Pr\bigl(X\in g^{-1}[C],\ Y\in h^{-1}[D]\bigr)
=\Pr\bigl(X\in g^{-1}[C]\bigr)\Pr\bigl(Y\in h^{-1}[D]\bigr),
$$
using independence for the Borel sets $g^{-1}[C]$ and $h^{-1}[D]$, and the last product is
$\Pr(g(X)\in C)\Pr(h(Y)\in D)$.

(b) Take any dependent pair, for instance $Y=X$ with $X\sim\text{Uniform}(0,1)$, and let $g\equiv0$, $h\equiv1$ be
constant. Then $g(X)=0$ and $h(Y)=1$ are constants.

(c) For constants, $\Pr(g(X)\in C)$ is $0$ or $1$; if it is $0$ then the joint event has probability $0$ and the
product is $0$; if it is $1$ then the joint event is $\{h(Y)\in D\}$ up to a null set and the product is
$\Pr(h(Y)\in D)$. So the product rule holds. A degenerate variable carries no information, so it cannot be
informative about anything else.

*Check:* the example satisfies all hypotheses of (a) with the roles reversed — dependence is not preserved by
functions, only independence is. ✓

**28.** *(Strategy: compute the conditional means; covariance only sees means.)*

(a) By symmetry of the conditional laws, $\mathbb{E}[Y\mid X=0]=0$ and $\mathbb{E}[Y\mid X=1]=0$. Hence
$\mathbb{E}[Y]=\tfrac12\cdot0+\tfrac12\cdot0=0$.

(b) Given $X=0$, $XY=0$; given $X=1$, $XY=Y$ with conditional mean $0$. So $\mathbb{E}[XY]=0$. Since
$\mathbb{E}[X]=\tfrac12$ and $\mathbb{E}[Y]=0$,
$$
\operatorname{Cov}(X,Y)=\mathbb{E}[XY]-\mathbb{E}[X]\mathbb{E}[Y]=0-0=0 .
$$
So the variables are uncorrelated.

(c) $\Pr(Y=1\mid X=0)=\tfrac12$, while
$\Pr(Y=1)=\Pr(X=0)\Pr(Y=1\mid X=0)+\Pr(X=1)\Pr(Y=1\mid X=1)=\tfrac12\cdot\tfrac12+0=\tfrac14$. These differ, so
$X$ and $Y$ are dependent: knowing $X=0$ doubles the chance that $Y=1$.

(d) If both $X$ and $Y$ are two-valued with $\Pr(X=1)=q\in(0,1)$, then
$$
\operatorname{Cov}(X,Y)=q(1-q)\bigl(\mathbb{E}[Y\mid X=1]-\mathbb{E}[Y\mid X=0]\bigr),
$$
so zero covariance forces $\mathbb{E}[Y\mid X=1]=\mathbb{E}[Y\mid X=0]$. For a two-valued $Y$ the conditional
mean determines the conditional law, hence $\Pr(Y=1\mid X=0)=\Pr(Y=1\mid X=1)$ and the variables are independent.
Dependence with zero covariance therefore needs at least three values of $Y$ (or a continuous $Y$), as in the
example.

*Check:* the identity in (d) is verified by expanding
$\mathbb{E}[Y]=(1-q)\mathbb{E}[Y\mid X=0]+q\mathbb{E}[Y\mid X=1]$ and $\mathbb{E}[XY]=q\mathbb{E}[Y\mid X=1]$. ✓

**29.** *(Strategy: divide the joint density by each marginal in turn.)*

(a) For $f_X(x)>0$ and $f_Y(y)>0$,
$$
f_{X\mid Y}(x\mid y)f_Y(y)=\frac{f_{X,Y}(x,y)}{f_Y(y)}f_Y(y)=f_{X,Y}(x,y)
=\frac{f_{X,Y}(x,y)}{f_X(x)}f_X(x)=f_{Y\mid X}(y\mid x)f_X(x).
$$

(b) The marginals are $f_X(x)=2x$ and $f_Y(y)=2(1-y)$ (§9.8), so for $0<y<1$,
$$
f_{X\mid Y}(x\mid y)=\frac{2}{2(1-y)}=\frac{1}{1-y},\qquad y\le x\le1 .
$$
This is the uniform density on $[y,1]$, and $\int_y^1\frac{dx}{1-y}=1$: a density in $x$ for each $y$.

(c) $\Pr\bigl(X\le\tfrac34\mid Y=\tfrac12\bigr)=\int_{1/2}^{3/4}\frac{dx}{1/2}=2\cdot\tfrac14=\tfrac12$.

(d) Unconditionally $\Pr(X\le\tfrac34)=F_X(\tfrac34)=(\tfrac34)^2=\tfrac{9}{16}\approx0.5625>\tfrac12$.
Conditioning on $Y=\tfrac12$ forces $X\ge\tfrac12$, shifting $X$ upward, so the probability of being at most
$\tfrac34$ must drop. The conditional density $1/(1-y)$ is uniform on $[y,1]$, whose mean $(1+y)/2=\tfrac34$ exceeds
the marginal mean $\mathbb{E}[X]=\tfrac23$ — the same phenomenon.

*Check:* both parts are consistent with the joint density: integrating $2$ over $x\in[1/2,3/4]$ and dividing by
the length $1-y=\tfrac12$ of the slice gives $2\cdot\tfrac14/\tfrac12=\tfrac12$. ✓

**30.** *(Strategy: atoms are the obstruction; continuity is necessary and sufficient.)*

(a) Let $q=\Pr(X=x)>0$. On $\{X=x\}$ we have $F(X)=F(x)$, so
$\Pr\bigl(F(X)=F(x)\bigr)\ge\Pr(X=x)=q>0$: $F(X)$ has an atom at $F(x)$, of mass at least $q$.

(b) The uniform law on $(0,1)$ has no atoms. If $F(X)\sim\text{Uniform}(0,1)$ then (a) forces $q=0$ for every $x$,
so $F$ has no atoms; by Theorem 8.2(f), $F$ is continuous.

(c) Suppose $F$ is continuous. For $0<u<1$ let $b_u=\max\{x:F(x)=u\}$; the maximum exists because $F$ is
continuous with the right limits. Since $F$ is nondecreasing, $\{x:F(x)\le u\}=(-\infty,b_u]$, so
$$
\Pr\bigl(F(X)\le u\bigr)=\Pr(X\le b_u)=F(b_u)=u,
$$
and the cases $u\le0$, $u\ge1$ are immediate. Hence $F(X)\sim\text{Uniform}(0,1)$.

(d) With $\Pr(X=0)=\Pr(X=1)=\tfrac12$, $F(0)=\tfrac12$ and $F(1)=1$. So $F(X)=\tfrac12$ with probability
$\tfrac12$ and $F(X)=1$ with probability $\tfrac12$: a two-point law, not uniform, consistent with (b).

(e) Take $F(x)=x^2$ on $[0,1]$, the CDF of Exercise 6. Then $F(X)=X^2$ and, as in Exercise 20,
$\Pr(X^2\le u)=\Pr(X\le\sqrt u)=u$ for $0\le u\le1$: uniform. Any continuous strictly increasing $F$ works.

*Check:* (a) and (c) together give the exact criterion: $F(X)$ is uniform if and only if $F$ is continuous. ✓

## Challenge

**31.** *(Strategy: uniform limits of continuous functions are continuous; derivatives see only the complement of
the Cantor set.)*

(a) Let $C_n$ be the union of the $2^n$ closed intervals of length $3^{-n}$ remaining after $n$ stages. Define
$F_n$ to be continuous, to take the value $k/2^n$ at the right endpoint of the $k$-th interval, and to be linear
between consecutive such points. On each interval removed at stage $n$, the two neighbouring remaining intervals
carry consecutive values $(k-1)/2^n$ and $k/2^n$, so $F_n$ is constant equal to $(2k-1)/2^{n+1}$ there. Then
$\lvert F_n-F_{n+1}\rvert\le2^{-n-1}$ everywhere, so $(F_n)$ is uniformly Cauchy and $F=\lim_nF_n$ is continuous.
On every removed interval $F_n$ is eventually constant, hence $F$ is constant there.

(b) At every point of a removed interval $F$ is constant on a neighbourhood, so $F'=0$ there. The removed set has
length $\sum_{n\ge1}2^{n-1}3^{-n}=1$, so its complement, the Cantor set, has length $0$. Hence $F'=0$ almost
everywhere.

(c) $F$ is continuous, so by Theorem 8.2(f) every jump $F(x)-F(x^{-})$ is zero: $\Pr(X=x)=0$ for all $x$.

(d) Suppose $X$ had a density $f$. Then $F(x)=\int_{-\infty}^xf$ would make $F$ absolutely continuous, and
$f=F'$ almost everywhere. But $F'=0$ almost everywhere, so $f=0$ almost everywhere, whence $F\equiv0$,
contradicting $F(1)=1$. So no density exists.

(e) $F$ is constant equal to $\tfrac12$ on $(\tfrac13,\tfrac23)$, so by continuity $F(\tfrac13)=F(\tfrac23)=\tfrac12$
and
$$
\Pr\bigl(X\in[0,\tfrac13]\bigr)=\tfrac12,\qquad
\Pr\bigl(X\in[\tfrac13,\tfrac23]\bigr)=F(\tfrac23)-F(\tfrac13^{-})=\tfrac12-\tfrac12=0 .
$$
The complement of the Cantor set is a countable union of removed intervals on which $F$ is constant, so it carries
probability $0$; hence $\Pr(X\in C)=1$. A set of length zero can carry probability $1$: this is a purely singular
law, the third branch of the Lebesgue decomposition.

*Check:* $\tfrac12+0+\tfrac12=1$ for the two outer thirds and the middle third, and the masses on $C$ sum to $1$. ✓

**32.** *(Strategy: differentiate the mixture and use $\varphi'(z)=-z\varphi(z)$, $\varphi''(z)=(z^2-1)\varphi(z)$.)*

Write $f(x)=\sum_iw_i\sigma^{-1}\varphi\bigl((x-\mu_i)/\sigma\bigr)$ and $z_i=(x-\mu_i)/\sigma$. Then
$f'(x)=\sigma^{-2}\sum_iw_i\varphi'(z_i)$ and $f''(x)=\sigma^{-3}\sum_iw_i\varphi''(z_i)$.

(a) At $x=m$, $z_1=\Delta/(2\sigma)$ and $z_2=-\Delta/(2\sigma)$, so $\varphi'(z_1)=-\frac{\Delta}{2\sigma}\varphi$
and $\varphi'(z_2)=+\frac{\Delta}{2\sigma}\varphi$ where $\varphi=\varphi\bigl(\Delta/(2\sigma)\bigr)$. Hence
$$
f'(m)=\frac{1}{\sigma^2}\Bigl[-w_1\frac{\Delta}{2\sigma}\varphi+w_2\frac{\Delta}{2\sigma}\varphi\Bigr]
=\frac{w_2-w_1}{\sigma^2}\cdot\frac{\Delta}{2\sigma}\varphi\Bigl(\frac{\Delta}{2\sigma}\Bigr),
$$
which vanishes when $w_1=w_2$.

(b) With $w_1=w_2=\tfrac12$ and $z_1^2=z_2^2=\Delta^2/(4\sigma^2)$,
$$
f''(m)=\frac{1}{\sigma^3}\Bigl(\frac{\Delta^2}{4\sigma^2}-1\Bigr)\varphi\Bigl(\frac{\Delta}{2\sigma}\Bigr).
$$

(c) If $\Delta>2\sigma$ then $\Delta^2/(4\sigma^2)>1$, so $f''(m)>0$: since also $f'(m)=0$, the midpoint is a
strict local minimum.

(d) At $x=\mu_1$ we have $z_1=0$ and $z_2=-\Delta/\sigma$, so
$f'(\mu_1)=\sigma^{-2}w_2\varphi'(-\Delta/\sigma)=\sigma^{-2}w_2(\Delta/\sigma)\varphi(\Delta/\sigma)>0$, and
similarly $f'(\mu_2)=-\sigma^{-2}w_1(\Delta/\sigma)\varphi(\Delta/\sigma)<0$. Since $m$ is a strict local minimum,
$f'<0$ on $(m-\varepsilon,m)$ and $f'>0$ on $(m,m+\varepsilon)$ for some $\varepsilon>0$.

On the compact interval $[\mu_1,m]$, the continuous function $f$ attains its maximum. It is not attained at $\mu_1$
(because $f'>0$ just to the right of $\mu_1$, so $f$ is larger nearby) and not at $m$ (because $f'<0$ just to the
left of $m$, so $f$ decreases into $m$). Hence the maximum is attained at an interior point $c_1$, where
$f'(c_1)=0$: a local maximum. The same argument on $[m,\mu_2]$ produces an interior local maximum $c_2$, since
$f'>0$ just right of $m$ and $f'(\mu_2)<0$. Because $c_1<m<c_2$, the two maxima are distinct: $f$ is bimodal.

(e) The converse needs a proof that $f'$ has exactly one zero when $\Delta\le2\sigma$, which is an algebraic
exercise with no shortcut: one must show that the equation $f'(x)=0$ reduces to a single-root condition after
taking logarithms. At the threshold $\sigma=1$, $\Delta=2$,
$f''(m)=\bigl(4/4-1\bigr)\varphi(1)=0$, so the midpoint is degenerate (an inflection with horizontal tangent) and
the mixture is still unimodal; for $\Delta>2$ it splits into two peaks.

*Check:* at $\sigma=1,\Delta=3$: $f''(m)=(9/4-1)\varphi(1.5)=1.25(0.1295)=0.1619>0$, a local minimum, hence
bimodal. ✓

**33.** *(Strategy: condition on $X_3$ and use the known triangular density of $X_1+X_2$.)*

(a) Write $T=X_1+X_2$, whose density is $t(u)=u$ on $(0,1)$ and $2-u$ on $(1,2)$ (§9.9). Then
$$
f_Z(z)=\int_0^1t(z-x)\,dx .
$$
For $0<z<1$: $z-x\in(0,1)$ exactly when $x<z$, so $f_Z(z)=\int_0^z(z-x)dx=z^2/2$.
For $1<z<2$: for $x\in(0,z-1)$ we have $z-x\in(1,2)$ and the integrand is $2-(z-x)=2-z+x$; for
$x\in(z-1,1)$ it is $z-x$. So
$$
f_Z(z)=\int_0^{z-1}(2-z+x)dx+\int_{z-1}^{1}(z-x)dx
=\Bigl[(2-z)x+\frac{x^2}{2}\Bigr]_0^{z-1}+\Bigl[zx-\frac{x^2}{2}\Bigr]_{z-1}^{1},
$$
and simplifying (or expanding) gives $-z^2+3z-\tfrac32$.
For $2<z<3$: $z-x\in(1,2)$ requires $x>z-2$, so
$$
f_Z(z)=\int_{z-2}^{1}(2-z+x)dx=\Bigl[(2-z)x+\frac{x^2}{2}\Bigr]_{z-2}^{1}=\frac{(3-z)^2}{2}.
$$

(b) At $z=1$: left piece gives $\tfrac12$, middle piece gives $-1+3-\tfrac32=\tfrac12$. At $z=2$: middle gives
$-4+6-\tfrac32=\tfrac12$, right piece gives $\tfrac12$. Continuous.

(c) $\int_0^1\tfrac{z^2}{2}dz=\tfrac16$. For the middle piece,
$$
\int_1^2\Bigl(-z^2+3z-\frac32\Bigr)dz=\Bigl[-\frac{z^3}{3}+\frac{3z^2}{2}-\frac{3z}{2}\Bigr]_1^2
=\Bigl(-\frac83+6-3\Bigr)-\Bigl(-\frac13+\frac32-\frac32\Bigr)=\frac13+\frac13=\frac23 .
$$
And $\int_2^3\tfrac{(3-z)^2}{2}dz=\tfrac16$. The total is $\tfrac16+\tfrac23+\tfrac16=1$.

(d) Each $X_i$ has the same law as $1-X_i$, so $Z$ has the same law as $3-Z$: $f_Z(z)=f_Z(3-z)$.

(e) The density is symmetric about $z=\tfrac32$ and there are no atoms, so $\Pr(Z\le\tfrac32)=\tfrac12$; hence
$\Pr(Z\le1.5)=\tfrac12$.

*Check:* the value at $z=1.5$ is $-2.25+4.5-1.5=0.75$, the maximum, and $\Pr(1.5<Z<2)=0.5-\int_2^3\frac{(3-z)^2}{2}dz
=0.5-\tfrac16=\tfrac13$. ✓

**34.** *(Strategy: integrate the inequality over the interval.)*

(a) If $f\ge c>0$ on an interval $A$ of length $L$, then
$1=\int_{\mathbb{R}}f\ge\int_Af\ge cL$, so $cL\le1$.

(b) With $c=1$ this gives $L\le1$: a density cannot be at least $1$ throughout an interval longer than $1$.

(c) $X\sim\text{Uniform}(0,\tfrac12)$ has $f\equiv2$ on its support, a set of length $\tfrac12$, and
$cL=2\cdot\tfrac12=1$: equality in (a).

(d) $f(x)=e^{-x}$ on $(0,\infty)$ satisfies $f\le1$ everywhere, $\int_0^\infty e^{-x}dx=1$, and is not uniform. An
unbounded density is $f(x)=1/\bigl(\pi\sqrt{x(1-x)}\bigr)$ on $(0,1)$, the Beta$(\tfrac12,\tfrac12)$ density, which
tends to $+\infty$ at both endpoints and integrates to $1$ (substitute $x=\sin^2\theta$).

(e) The two errors are: (i) $f(x)$ is a density, not a probability — only $f(x)dx$ approximates a probability, so
the bound "probabilities are at most $1$" does not apply to it; (ii) densities have no upper bound at all, the only
constraint being $\int f=1$, so a tall narrow density and a short wide one are equally legitimate.

*Check:* the bound in (a) is sharp, as (c) shows. ✓

**35.** *(Strategy: the identity $Q(p)\le x\iff p\le F(x)$ holds for every CDF, jumps or not.)*

(a) If $Q(U)\le x$ then $F(Q(U))\le F(x)$ by monotonicity, and $U\le F(Q(U))$ by Proposition 8.6(i); hence
$U\le F(x)$. Conversely, if $U\le F(x)$ then $Q(U)\le Q(F(x))\le x$ by Proposition 8.6(iii) and monotonicity of
$Q$. So $\{Q(U)\le x\}=\{U\le F(x)\}$ as events. If $F(x)=0$ both events are empty up to null sets; if $F(x)=1$
both are all of $(0,1)$ up to null sets.

(b) Taking probabilities and using that $U$ is uniform,
$\Pr(Q(U)\le x)=\Pr(U\le F(x))=F(x)$ for every $x$. Hence $Q(U)$ has CDF $F$, exactly.

(c) The CDF is a staircase with jumps $0.2,0.5,0.3$ at $0,1,2$, so
$$
Q(u)=\begin{cases}0,&0<u\le0.2,\\ 1,&0.2<u\le0.7,\\ 2,&0.7<u<1.\end{cases}
$$

(d) $U$ uniform gives $\Pr(Q(U)=0)=\Pr(0<U\le0.2)=0.2$, $\Pr(Q(U)=1)=\Pr(0.2<U\le0.7)=0.5$ and
$\Pr(Q(U)=2)=\Pr(0.7<U<1)=0.3$ — exactly the masses.

(e) Because (b) is an identity for every $x$, not a limit; the flat pieces of $Q$ are chosen precisely so that the
uniform measure of each level set equals the mass at that level. This is why inverse transform sampling is exact
for discrete laws, unlike rejection or rounding schemes.

*Check:* the intervals in (c) have lengths $0.2,0.5,0.3$, summing to $1$. ✓

**36.** *(Strategy: $F\succeq G$ means the level sets satisfy $S^F_p\subseteq S^G_p$.)*

(a) Suppose $F(x)\ge G(x)$ for all $x$ and fix $p\in(0,1)$. Put $x=Q_G(p)$; then $G(x)\ge p$ by Proposition
8.6(i), so $F(x)\ge G(x)\ge p$, i.e. $x\in S^F_p$. Hence $Q_F(p)=\inf S^F_p\le x=Q_G(p)$.

(b) Suppose $Q_F(p)\le Q_G(p)$ for all $p$. Fix $x$ and put $p=F(x)$. Then $Q_F(p)\le x$ by Proposition 8.6(iii),
so $Q_G(p)\le Q_F(p)\le x$, and Proposition 8.6(ii) gives $p\le G(x)$, i.e. $F(x)\le G(x)$. As $x$ was arbitrary,
$F\preceq G$ in the sense that $G(x)\ge F(x)$ for all $x$.

(c) Parts (a) and (b) show that $F(x)\ge G(x)$ for all $x$ if and only if $Q_F(p)\le Q_G(p)$ for all $p$. Since the
quantile function determines the law, stochastic ordering can be checked either on CDFs or on quantiles.

(d) For $X\sim\text{Exp}(\lambda_1)$ and $Y\sim\text{Exp}(\lambda_2)$ with $\lambda_1<\lambda_2$:
$F_{\lambda}(x)=1-e^{-\lambda x}$ is increasing in $\lambda$, so $F_{\lambda_1}(x)\le F_{\lambda_2}(x)$: $Y$ is
stochastically smaller than $X$, as expected since a larger rate means faster decay. Quantiles are
$Q_\lambda(p)=-\ln(1-p)/\lambda$, decreasing in $\lambda$, so $Q_{\lambda_2}(p)\le Q_{\lambda_1}(p)$, consistent
with (a). For example at $p=\tfrac12$: $\ln2/\lambda_2<\ln2/\lambda_1$ when $\lambda_1<\lambda_2$ ✓.

*Check:* with $\lambda_1=1$, $\lambda_2=2$ and $x=1$: $F_1(1)=0.632$ and $F_2(1)=0.865$, so $F_1\le F_2$ as
claimed, and $Q_1(\tfrac12)=\ln2\approx0.693$ while $Q_2(\tfrac12)\approx0.347$. ✓

