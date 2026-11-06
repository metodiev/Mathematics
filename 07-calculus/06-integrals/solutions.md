# Solutions: Integrals

> Companion to [exercises.md](exercises.md) and the [tutorial](README.md).

Each solution names the strategy, then carries out every step. Theorem and proposition numbers refer to
Section 8 of the tutorial; property names refer to the table in Section 7.7.

## Beginner

**1.** (a) By linearity and Proposition 1,
$\sum_{k=1}^{10}(2k+1)=2\cdot\frac{10\cdot11}{2}+10=110+10=120$.

(b) $\sum_{k=1}^{5}k^2=\frac{5\cdot6\cdot11}{6}=55$.

(c) $\sum_{k=1}^{4}k^3=\left(\frac{4\cdot5}{2}\right)^2=100$ and $\sum_{k=1}^{4}k=10$, so
$\sum_{k=1}^{4}(k^3-k)=100-10=90$.

**2.** The terms form an arithmetic progression with difference $4$ and first term $3$, so the $k$-th term
is $4k-1$. The last term satisfies $4k-1=99$, hence $k=25$. Therefore

$$\sum_{k=1}^{25}(4k-1)=4\cdot\frac{25\cdot26}{2}-25=1300-25=1275 .$$

*Check.* The sum of an arithmetic progression is the number of terms times the average of the first and
last: $25\cdot\frac{3+99}{2}=25\cdot51=1275$.

**3.** $\displaystyle\sum_{k=1}^{n}(4k-1)=4\cdot\frac{n(n+1)}{2}-n=2n^2+2n-n=2n^2+n$. At $n=3$ the sum is
$3+7+11=21$, and the formula gives $2\cdot9+3=21$.

**4.** For $n\ge1$,

$$\sum_{k=1}^{n}(k^2-k)=\frac{n(n+1)(2n+1)}{6}-\frac{n(n+1)}{2}
=\frac{n(n+1)\bigl((2n+1)-3\bigr)}{6}=\frac{n(n+1)(2n-2)}{6}=\frac{n(n+1)(n-1)}{3}.$$

At $n=4$ the terms are $0,2,6,12$, whose sum is $20$; the formula gives $\frac{4\cdot5\cdot3}{3}=20$.

**5.** With $n=4$ on $[0,2]$ we have $\Delta x=\frac{2}{4}=\frac12$, so the partition points are
$0,\frac12,1,\frac32,2$ and the midpoints are $\frac14,\frac34,\frac54,\frac74$. Hence

$$M_4=\frac12\left[\left(\frac14\right)^2+\left(\frac34\right)^2+\left(\frac54\right)^2+\left(\frac74\right)^2\right]
=\frac12\left[\frac{1+9+25+49}{16}\right]=\frac12\cdot\frac{84}{16}=\frac{21}{8}=2.625 .$$

The exact value is $\frac83\approx2.667$, so the midpoint sum is an underestimate; this is expected,
because $x^2$ is concave up and the midpoint rectangle lies below the graph on each strip.

**6.** The left endpoints are $0,\frac12,1,\frac32$ and the right endpoints $\frac12,1,\frac32,2$, so

$$L_4=\frac12\left[0+\frac14+1+\frac94\right]=\frac12\cdot\frac{14}{4}=\frac74=1.75,$$
$$R_4=\frac12\left[\frac14+1+\frac94+4\right]=\frac12\cdot\frac{30}{4}=\frac{15}{4}=3.75 .$$

Since $1.75<\frac83=2.667<3.75$, the inequality $L_4\le\int_0^2x^2\,dx\le R_4$ holds. It must, because
$x^2$ is increasing, so on each strip the left endpoint gives the minimum and the right endpoint the
maximum.

**7.** With $\Delta x=1$ on $[1,4]$, $L_3=\frac11+\frac12+\frac13=\frac{11}{6}\approx1.833$ and
$R_3=\frac12+\frac13+\frac14=\frac{13}{12}\approx1.083$. Here $L_3>R_3$ because $f(x)=1/x$ is
**decreasing**: the largest value on each strip is at its left endpoint.

**8.** With $\Delta x=\frac2n$ and $x_k=\frac{2k}{n}$,

$$R_n=\sum_{k=1}^{n}\frac{2k}{n}\cdot\frac2n=\frac{4}{n^2}\sum_{k=1}^{n}k
=\frac{4}{n^2}\cdot\frac{n(n+1)}{2}=2\left(1+\frac1n\right)\longrightarrow2 .$$

The left sums are $2\left(1-\frac1n\right)$, with the same limit, and every other choice of sample points
lies between them. Hence $\int_0^2x\,dx=2$.

**9.** (a) By the constant property, $\int_1^3 5\,dx=5(3-1)=10$.
(b) By the zero-length property, $\int_2^2x^3\,dx=0$, since every Riemann sum is empty.

**10.** (a) Additivity: $\int_0^5f=\int_0^2f+\int_2^5f$, so $\int_2^5f=12-3=9$.
(b) Reversal: $\int_5^0f=-\int_0^5f=-12$.
(c) Linearity: $\int_0^5(2f-3g)=2\cdot12-3\cdot7=24-21=3$.
(d) Reversal and (a): $\int_5^2f=-\int_2^5f=-9$.

**11.** With $h=\frac12$ the sample points are $0,\frac12,1,\frac32,2$ and

$$T_4=\frac{1}{4}\Bigl[0+2\cdot\tfrac12+2\cdot1+2\cdot\tfrac32+2\Bigr]=\frac14\bigl[0+1+2+3+2\bigr]=2 .$$

The exact value is $\int_0^2x\,dx=\frac{2^2}{2}=2$, so the approximation is exact. The reason is that on
each strip the graph of a linear function is itself the chord, so the trapezoid coincides with the region
under the graph; the trapezoidal rule is exact for every linear function.

**12.** For $f(x)=x^3$ we have $f''(x)=6x$, so $\lvert f''\rvert\le6$ on $[0,1]$. With $h=\frac14$,

$$T_4=\frac18\Bigl[0+2\cdot\frac1{64}+2\cdot\frac18+2\cdot\frac{27}{64}+1\Bigr]
=\frac18\cdot\frac{68}{32}=\frac{17}{64}=0.265625 .$$

The exact value is $\frac14=0.25$, so the error is $\frac{17}{64}-\frac{16}{64}=\frac{1}{64}=0.015625$.

The bound of Theorem 5 with $M=6$, $b-a=1$, $n=4$ is
$\frac{6\cdot1}{12\cdot16}=\frac{1}{32}=0.03125$, which comfortably exceeds the actual error. The
estimate is an overestimate because $x^3$ is concave up on $(0,1)$, so each chord lies above the graph.

## Intermediate

**13.** With $\Delta x=\frac1n$ and $x_k=\frac kn$,

$$R_n=\sum_{k=1}^{n}\left[\left(\frac kn\right)^2+\frac kn\right]\frac1n
=\frac{1}{n^3}\sum_{k=1}^{n}k^2+\frac{1}{n^2}\sum_{k=1}^{n}k
=\frac{(n+1)(2n+1)}{6n^2}+\frac{n+1}{2n}.$$

The first term tends to $\frac{2}{6}=\frac13$ and the second to $\frac12$, so the limit is $\frac56$.
The left sums give the same limit, hence $\int_0^1(x^2+x)\,dx=\frac56$.

**14.** By additivity, $\int_0^2x^2\,dx=\int_0^1x^2\,dx+\int_1^2x^2\,dx$, so

$$\int_1^2x^2\,dx=\frac{2^3}{3}-\frac{1^3}{3}=\frac83-\frac13=\frac73 .$$

**15.** Use the symmetry $f(-x)=-f(x)$ with a symmetric partition $x_k=-1+\frac{2k}{n}$, so that
$x_{n-k}=-x_k$. The right-endpoint sum is

$$R_n=\sum_{k=1}^{n}\left(-1+\frac{2k}{n}\right)^3\frac2n .$$

Substituting $j=n-k$ turns this into

$$R_n=\sum_{j=0}^{n-1}\left(-1+\frac{2(n-j)}{n}\right)^3\frac2n=\sum_{j=0}^{n-1}\left(1-\frac{2j}{n}\right)^3\frac2n=-L_n,$$

because $\left(1-\frac{2j}{n}\right)^3=-\left(-1+\frac{2j}{n}\right)^3$. Since $x^3$ is a polynomial it is
integrable, so $R_n\to I$ and $L_n\to I$; the identity $R_n=-L_n$ gives $I=-I$, hence $I=0$. The same
cancellation occurs in every symmetric Riemann sum, and the conclusion is
$\int_{-1}^1x^3\,dx=0$: the signed areas above and below the axis are equal in magnitude.

**16.** Set the curves equal: $x^2=x+2$, that is $x^2-x-2=(x-2)(x+1)=0$, so the intersections are at
$x=-1$ and $x=2$. On $(-1,2)$ the line is above the parabola because $x+2-x^2=-(x-2)(x+1)>0$. Therefore

$$A=\int_{-1}^{2}(x+2-x^2)\,dx=\int_{-1}^{2}x\,dx+2\int_{-1}^{2}dx-\int_{-1}^{2}x^2\,dx .$$

Using $\int_a^bx\,dx=\frac{b^2-a^2}{2}$, $\int_a^bc\,dx=c(b-a)$ and
$\int_a^bx^2\,dx=\frac{b^3-a^3}{3}$:

$$A=\frac{4-1}{2}+2\cdot3-\frac{8-(-1)}{3}=\frac32+6-3=\frac{9}{2}.$$

**17.** The average value is

$$\frac{1}{2-0}\int_0^2x^3\,dx=\frac12\cdot\frac{2^4}{4}=\frac12\cdot4=2 .$$

The mean value theorem for integrals promises $c\in[0,2]$ with $c^3=2$, that is $c=\sqrt[3]{2}\approx1.26$.
The average lies below the value at the right endpoint, $f(2)=8$, as it must, and above $f(1)=1$.

**18.** The average value is

$$\frac{1}{b-a}\int_a^bx\,dx=\frac{1}{b-a}\cdot\frac{b^2-a^2}{2}
=\frac{(b-a)(b+a)}{2(b-a)}=\frac{a+b}{2}.$$

The average is attained at the point $c$ with $c=\frac{a+b}{2}$, the midpoint of the interval. This says
that for the linear function $f(x)=x$ the value at the midpoint equals the average, and since the
midpoint rectangle on each strip then has exactly the average height, the midpoint rule is exact for every
linear function.

**19.** With $h=\frac12$ on $[0,2]$, the points are $0,\frac12,1,\frac32,2$ and

$$T_4=\frac14\Bigl[0+2\cdot\frac14+2\cdot1+2\cdot\frac94+4\Bigr]=\frac14\bigl[0+\tfrac12+2+\tfrac92+4\bigr].$$

The bracket is $\frac12+2+\frac92+4=\frac{1+4+9+8}{2}=\frac{22}{2}=11$, so
$T_4=\frac{11}{4}=2.75$. The exact value is $\frac83\approx2.667$, so the error is
$\frac{11}{4}-\frac83=\frac{33-32}{12}=\frac{1}{12}$. The bound with $M=2$ (since $\lvert f''\rvert=2$),
$b-a=2$, $n=4$ is $\frac{2\cdot8}{12\cdot16}=\frac{16}{192}=\frac{1}{12}$, attained exactly: for a
quadratic the bound is sharp.

**20.** With equal time steps $h=10$ s,

$$T=\frac{10}{2}\Bigl[v(0)+2\bigl(v(10)+v(20)+v(30)\bigr)+v(40)\Bigr]
=5\bigl[0+2(5+12+20)+25\bigr]=5\bigl[0+74+25\bigr]=495 .$$

The car travelled approximately $495$ metres. The trapezoidal rule is the natural choice here because the
data are equally spaced and the speed between samples is unknown but plausibly close to linear; the
estimate is a sum of trapezia in the velocity–time graph, that is, of distances.

**21.** The volume is the integral of the rate over the interval:

$$V=\int_0^2(4-t^2)\,dt=4\cdot2-\frac{2^3}{3}=8-\frac83=\frac{16}{3}\approx5.33\ \text{litres}.$$

The rate is positive on $[0,2)$, so no cancellation occurs and the integral is a plain area.

**22.** On $(0,1)$ we have $0<x^3<x^2<x$, so by monotonicity
$\int_0^1x^3<\int_0^1x^2<\int_0^1x$. Computing: $\int_0^1x=\frac12$, $\int_0^1x^2=\frac13$,
$\int_0^1x^3=\frac14$. Indeed $\frac14<\frac13<\frac12$. Note this is not a general rule — larger
exponents do not always give smaller integrals — but it is true on $(0,1)$ because all powers are below
$1$ there.

## Advanced

**23.** Let $\alpha\ge0$. On each subinterval, multiplying by the positive number $\alpha$ preserves
order, so $\sup(\alpha f)=\alpha\sup f$ and $\inf(\alpha f)=\alpha\inf f$. Hence
$U(\alpha f,P)=\alpha U(f,P)$ and $L(\alpha f,P)=\alpha L(f,P)$ for every partition $P$. Since
$U(f,P)-L(f,P)\to0$, the same holds for $\alpha f$, and the common limit is $\alpha\int_a^bf$; therefore
$\int_a^b\alpha f=\alpha\int_a^bf$.

Let $\alpha<0$. Multiplying by a negative number reverses order, so $\sup(\alpha f)=\alpha\inf f$ and
$\inf(\alpha f)=\alpha\sup f$. Hence $U(\alpha f,P)=\alpha L(f,P)$ and $L(\alpha f,P)=\alpha U(f,P)$. As
the mesh tends to zero, both $U(f,P)$ and $L(f,P)$ tend to $\int_a^bf$, so both bounds for $\alpha f$
tend to $\alpha\int_a^bf$, and the integral equals that number. In particular $\alpha=-1$ gives
$\int_a^b(-f)=-\int_a^bf$. $\blacksquare$

**24.** Let $P_1=\{a=x_0<\cdots<x_m=b\}$ and $P_2=\{b=y_0<\cdots<y_r=c\}$. Their union
$P=P_1\cup P_2$ is a partition of $[a,c]$, and every Riemann sum for $P$ splits:

$$\sum_{k}f(\xi_k)\Delta x_k=\sum_{k=1}^{m}f(\xi_k)\Delta x_k+\sum_{j=1}^{r}f(\eta_j)\Delta y_j,$$

because the subintervals of $P$ are exactly those of $P_1$ followed by those of $P_2$. Letting the mesh
tend to zero gives $\int_a^cf=\int_a^bf+\int_b^cf$ for partitions that contain $b$ as a division point.

For a general partition $Q$ of $[a,c]$, put $Q'=Q\cup\{b\}$. The two sums differ only on the one
subinterval of $Q$ that contains $b$: the single term $f(\xi)\Delta x$ is replaced by two terms
$f(\xi_1)\Delta x_1+f(\xi_2)\Delta x_2$ with $\Delta x_1+\Delta x_2=\Delta x$. Hence
$\lvert S(Q)-S(Q')\rvert\le2\sup\lvert f\rvert\cdot\Delta x\le2\sup\lvert f\rvert\cdot\lVert Q\rVert$,
which tends to $0$ with the mesh. So the general sums have the same limit as those containing $b$, and the
identity holds for all partitions. $\blacksquare$

**25.** Suppose $f\le g$ on $[a,b]$ and let $P$ be any partition. Since $f(x)\le g(x)$ for every $x$ in
each subinterval $[x_{k-1},x_k]$, every lower bound for $g$ there is a lower bound for $f$, hence
$\inf f\le\inf g$ and therefore

$$L(f,P)=\sum_k\inf_{[x_{k-1},x_k]}f\,\Delta x_k\le\sum_k\inf_{[x_{k-1},x_k]}g\,\Delta x_k=L(g,P).$$

The integral is the supremum of the lower sums over all partitions (the Darboux characterisation), so
$\int_a^bf=\sup_PL(f,P)\le\sup_PL(g,P)=\int_a^bg$. $\blacksquare$

**26.** First, the oscillation inequality
$\bigl\lvert\lvert f(x)\rvert-\lvert f(y)\rvert\bigr\rvert\le\lvert f(x)-f(y)\rvert$ holds for all
$x,y$, by the triangle inequality applied to $\lvert f(x)\rvert\le\lvert f(x)-f(y)\rvert+\lvert f(y)\rvert$
and its symmetric partner. Hence, on every subinterval,
$M_k(\lvert f\rvert)-m_k(\lvert f\rvert)\le M_k(f)-m_k(f)$, so
$U(\lvert f\rvert,P)-L(\lvert f\rvert,P)\le U(f,P)-L(f,P)$. Since $f$ is integrable the right-hand side
can be made arbitrarily small, so $\lvert f\rvert$ is integrable by the Darboux criterion.

Second, for any partition and any choice of sample points, the triangle inequality for finite sums gives

$$\left\lvert\sum_k f(\xi_k)\Delta x_k\right\rvert\le\sum_k\lvert f(\xi_k)\rvert\Delta x_k .$$

Letting the mesh tend to zero yields $\left\lvert\int_a^bf\right\rvert\le\int_a^b\lvert f\rvert$.
$\blacksquare$

**27.** Let $f$ be increasing on $[a,b]$, and take the uniform partition with $h=\frac{b-a}{n}$. On
$[x_{k-1},x_k]$ the infimum is $f(x_{k-1})$ (attained at the left endpoint) and the supremum is
$f(x_k)$. Hence

$$U(f,P)-L(f,P)=h\sum_{k=1}^{n}\bigl(f(x_k)-f(x_{k-1})\bigr)=h\bigl(f(b)-f(a)\bigr),$$

because the sum telescopes: every interior value appears once with a plus sign and once with a minus
sign. Since $h=\frac{b-a}{n}$,

$$U(f,P)-L(f,P)=\frac{(b-a)\bigl(f(b)-f(a)\bigr)}{n}\longrightarrow0 .$$

Given $\varepsilon>0$, choose $n$ large enough that this is below $\varepsilon$; the Darboux criterion
then gives integrability. The decreasing case follows by applying the result to $-f$. $\blacksquare$

**28.** Orient the interval from $b$ down to $a$: take points $b=y_0>y_1>\cdots>y_n=a$ and define the
*signed* widths $\Delta y_j=y_j-y_{j-1}<0$. A Riemann sum for this oriented partition is
$\sum_jf(\eta_j)\Delta y_j$. Writing $x_k=y_{n-k}$ gives an ordinary partition
$a=x_0<\cdots<x_n=b$, and each term corresponds: $\eta_j=\xi_{n-j+1}$ and
$\Delta y_j=y_j-y_{j-1}=x_{n-j}-x_{n-j+1}=-(x_{n-j+1}-x_{n-j})=-\Delta x_{n-j+1}$. So the oriented sum
equals $-\sum_kf(\xi_k)\Delta x_k$, the negative of an ordinary Riemann sum.

As the mesh tends to zero, the ordinary sums tend to $\int_a^bf$, so the oriented sums tend to
$-\int_a^bf$. Taking this as the definition of the integral from $b$ to $a$ gives
$\int_b^af=-\int_a^bf$. The convention is exactly what is needed to make additivity hold without
ordering hypotheses. $\blacksquare$

**29.** Let $P$ be any partition of $[0,1]$. Every subinterval $[x_{k-1},x_k]$ has positive length and
contains both rational and irrational points, so $f$ takes the value $1$ and the value $0$ on it. Hence
$M_k=1$ and $m_k=0$ for every $k$, and

$$U(f,P)=\sum_{k=1}^{n}1\cdot\Delta x_k=1,\qquad L(f,P)=\sum_{k=1}^{n}0\cdot\Delta x_k=0 .$$

Thus $U(f,P)-L(f,P)=1$ for every partition, so the Darboux criterion fails (take $\varepsilon=\frac12$);
the function is not Riemann integrable. Equivalently, choosing all sample points rational gives sums
equal to $1$, and choosing them all irrational gives sums equal to $0$, so the sums cannot settle on a
single limit. This is the standard example that separates "bounded" from "integrable".

**30.** Suppose for contradiction that $f(c)>0$ for some $c\in[a,b]$. By continuity at $c$ there is
$\delta>0$ such that $\lvert x-c\rvert<\delta$ implies $\lvert f(x)-f(c)\rvert<\frac{f(c)}{2}$, hence
$f(x)>\frac{f(c)}{2}$ for such $x$. Choose $u<v$ in $[a,b]$ with $u,v\in(c-\delta,c+\delta)$; such
points exist because $c$ is not isolated, and $f>\frac{f(c)}{2}$ on $[u,v]$.

By additivity, $\int_a^bf=\int_a^uf+\int_u^vf+\int_v^bf$. The first and third terms are $\ge0$ because
$f\ge0$, and monotonicity applied to the constant $\frac{f(c)}{2}$ gives
$\int_u^vf\ge\frac{f(c)}{2}(v-u)>0$. Hence $\int_a^bf>0$, contradicting $\int_a^bf=0$. Therefore
$f(c)=0$ for every $c$, as claimed. $\blacksquare$

## Challenge

**31.** With $\Delta x=\frac1n$ and $x_k=\frac kn$,

$$R_n=\sum_{k=1}^{n}\frac kn\left(1-\frac kn\right)\frac1n=\frac{1}{n^2}\sum_{k=1}^{n}k-\frac{1}{n^3}\sum_{k=1}^{n}k^2 .$$

Substituting the sums of powers,

$$R_n=\frac{1}{n^2}\cdot\frac{n(n+1)}{2}-\frac{1}{n^3}\cdot\frac{n(n+1)(2n+1)}{6}
=\frac{n+1}{2n}-\frac{(n+1)(2n+1)}{6n^2}.$$

As $n\to\infty$ the first term tends to $\frac12$ and the second to $\frac{2}{6}=\frac13$, so
$R_n\to\frac12-\frac13=\frac16$. Since the integrand is continuous the integral exists, and therefore
$\int_0^1x(1-x)\,dx=\frac16$.

*Check.* The region is a parabolic cap of base $1$ and height $\frac14$, and $\frac16$ is two-thirds of
the enclosing rectangle $\frac14\cdot1$; this is the classical fact that a parabolic segment has area
two-thirds of its bounding rectangle.

**32.** Suppose $f$ is unbounded on $[a,b]$ and let $P=\{x_0,\dots,x_n\}$ be any partition. If $f$ were
bounded on every subinterval $[x_{k-1},x_k]$, say $\lvert f\rvert\le B_k$ there, then
$\lvert f\rvert\le\max_kB_k$ on all of $[a,b]$, contradicting unboundedness. So $f$ is unbounded on at
least one subinterval, say $[x_{j-1},x_j]$, whose length $\Delta x_j$ is positive.

Fix all sample points except $\xi_j$, and consider the Riemann sum as a function of $\xi_j$:
$S=f(\xi_j)\Delta x_j+C$ with $C$ fixed. Since $f$ is unbounded on that subinterval, $\lvert S\rvert$ can
be made arbitrarily large. Hence, for this single partition, the set of Riemann sums is unbounded, so it
cannot be contained in any interval $\left(I-\varepsilon,I+\varepsilon\right)$. Therefore no $I$ can
satisfy the definition of integrability, and an integrable function must be bounded. $\blacksquare$

**33.** Suppose $f(c)\ne0$ for some $c$. Replacing $f$ by $-f$ if necessary, assume $f(c)>0$. By
continuity there is $\delta>0$ with $f(x)>\frac{f(c)}{2}$ whenever $\lvert x-c\rvert<\delta$ and
$x\in[a,b]$. Choose $u<v$ in $[a,b]\cap(c-\delta,c+\delta)$. Then

$$0=\int_a^vf-\int_a^uf=\int_u^vf\ge\frac{f(c)}{2}(v-u)>0,$$

using additivity and monotonicity; the contradiction shows $f(c)=0$. Since $c$ was arbitrary, $f\equiv0$.
$\blacksquare$

*Remark.* The hypothesis "for every $x$" is essential. Knowing only $\int_a^bf=0$ does not force
$f\equiv0$: the function $f(x)=x$ on $[-1,1]$ has zero integral and is not identically zero.

**34.** (a) Let $f(x)=mx+c$. On a subinterval $[u,v]$ the trapezoid has area
$\frac{v-u}{2}\bigl(f(u)+f(v)\bigr)$, while the exact area under the line is the same trapezoid, since
the graph is the chord. Summing over the subintervals, $T_n=\int_a^bf$ for every $n$. Algebraically,

$$T_n=\frac{h}{2}\Bigl[f(a)+2\sum_{k=1}^{n-1}(m x_k+c)+f(b)\Bigr]=\int_a^b(mx+c)\,dx,$$

because the expression is just the area of one large trapezium with parallel sides $f(a)$ and $f(b)$.

(b) For $f(x)=x^2$ on $[0,b]$ with $h=\frac bn$,

$$T_n=h\Bigl[\tfrac12f(0)+\sum_{k=1}^{n-1}f(kh)+\tfrac12f(b)\Bigr]
=h\Bigl[h^2\sum_{k=1}^{n-1}k^2+\tfrac{b^2}{2}\Bigr].$$

Now $\sum_{k=1}^{n-1}k^2=\frac{(n-1)n(2n-1)}{6}$ and $h=\frac bn$, so

$$T_n=\frac{b^3}{n}\left[\frac{(n-1)(2n-1)}{6n}+\frac12\right]
=\frac{b^3}{n}\cdot\frac{(2n^2-3n+1)+3n}{6n}=\frac{b^3(2n^2+1)}{6n^2}=\frac{b^3}{3}+\frac{b^3}{6n^2}.$$

(c) The error is $T_n-\int_0^bx^2\,dx=\frac{b^3}{6n^2}$. For $f(x)=x^2$ we have $f''=2$, so $M=2$ and the
bound of Theorem 5 reads $\frac{2b^3}{12n^2}=\frac{b^3}{6n^2}$. The error equals the bound, so the bound
is sharp for quadratics.

**35.** For $f(x)=x^2$ on $[0,1]$ with $x_k=\frac kn$ and $\Delta x=\frac1n$, the function is increasing,
so on each subinterval the minimum is at the left endpoint and the maximum at the right:

$$L_n=\sum_{k=1}^{n}\left(\frac{k-1}{n}\right)^2\frac1n=\frac{1}{n^3}\sum_{j=0}^{n-1}j^2
=\frac{(n-1)n(2n-1)}{6n^3}=\frac{(n-1)(2n-1)}{6n^2},$$
$$U_n=\sum_{k=1}^{n}\left(\frac kn\right)^2\frac1n=\frac{1}{n^3}\sum_{k=1}^{n}k^2
=\frac{n(n+1)(2n+1)}{6n^3}=\frac{(n+1)(2n+1)}{6n^2}.$$

Subtracting,

$$U_n-L_n=\frac{(n+1)(2n+1)-(n-1)(2n-1)}{6n^2}=\frac{(2n^2+3n+1)-(2n^2-3n+1)}{6n^2}=\frac{6n}{6n^2}=\frac1n .$$

Given $\varepsilon>0$, choose $n>\frac1\varepsilon$; then $U_n-L_n<\varepsilon$, so the Darboux criterion
is satisfied and $f$ is integrable. Moreover both bounds have the same limit:

$$L_n=\frac{2n^2-3n+1}{6n^2}\longrightarrow\frac13,\qquad U_n=\frac{2n^2+3n+1}{6n^2}\longrightarrow\frac13,$$

so $\int_0^1x^2\,dx=\frac13$. The argument also shows that the gap decreases exactly like $1/n$, which is
the rate at which the left and right sums converge for this function.

**36.** With $h=\frac bn$ and midpoints $m_k=\left(k-\frac12\right)h$,

$$M_n=h\sum_{k=1}^{n}\left(k-\tfrac12\right)^2h^2=h^3\sum_{k=1}^{n}\left(k^2-k+\tfrac14\right)
=h^3\left[\frac{n(n+1)(2n+1)}{6}-\frac{n(n+1)}{2}+\frac n4\right].$$

The bracket simplifies to $\frac{n(n^2-1)}{3}+\frac n4$, so

$$M_n=\frac{b^3}{n^3}\left[\frac{n(n^2-1)}{3}+\frac n4\right]
=b^3\left[\frac{n^2-1}{3n^2}+\frac{1}{4n^2}\right]=\frac{b^3}{3}-\frac{b^3}{12n^2},$$

using $-\frac{1}{3n^2}+\frac{1}{4n^2}=-\frac{1}{12n^2}$.

Comparing with $T_n=\frac{b^3}{3}+\frac{b^3}{6n^2}$: the midpoint error is negative, the trapezoidal error
is positive, and the trapezoidal error is exactly twice the magnitude of the midpoint error.

The signs follow from concavity. For a convex (concave up) function the chord joining two points of the
graph lies above the graph, so each trapezoid contains the corresponding slice and $T_n$ overestimates.
The midpoint height is the value at the centre, which for a convex function lies below the average of the
two endpoint heights, so the midpoint rectangle misses part of each slice and $M_n$ underestimates. For a
concave down function both signs reverse. This is the geometric content of the error term, and it is why
the two errors can be combined — Simpson's rule is the weighted average
$\frac23M_n+\frac13T_n$, which cancels the leading error term.
