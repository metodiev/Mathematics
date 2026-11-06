# Numerical Integration — Solutions

> [Numerical Integration](README.md) · Solutions to the 36 problems in [exercises.md](exercises.md)

Each solution states the strategy first, then carries out every step and closes with a check. The error
of a rule is $I-Q$ throughout. Where a bound is much larger than the actual error, that is noted.

## Beginner

**1.** *Strategy: apply the one-panel rule, then the two-panel composite rule, and compare each error with
the corresponding bound.*

One panel, $h=1$: $T=\tfrac12(0+1)=0.5$, and $I=\tfrac13$, so $I-T=-\tfrac16=-0.166667$. The bound of
Theorem 7.1 is $\frac{(b-a)^3}{12}\lVert f''\rVert_\infty=\frac{1}{12}\cdot2=\frac16$, exactly the error,
because $f''=2$ is constant so the point $\eta$ is irrelevant.

Two panels, $h=\tfrac12$: $T_2=\tfrac{0.5}{2}\bigl(0+2\cdot\tfrac14+1\bigr)=0.375$, and
$I-T_2=\tfrac13-\tfrac38=-\tfrac1{24}=-0.041667$. The composite bound is
$\frac{(b-a)h^2}{12}\lVert f''\rVert_\infty=\frac{0.25}{12}\cdot2=\frac1{24}$, again sharp. Halving $h$
reduced the error by exactly $4$, as the order $2$ predicts.

**2.** *Strategy: insert the values into Simpson's formula and compare with the antiderivative.*

For $f=x^3$ on $[0,2]$, $h=1$: $S=\tfrac13(0+4\cdot1+8)=\tfrac{12}{3}=4$, and
$I=\bigl[\tfrac{x^4}{4}\bigr]_0^2=4$. Exact, as Theorem 7.2 guarantees for cubics.

For $f=x^2$ on $[0,2]$: $S=\tfrac13(0+4\cdot1+4)=\tfrac83$, and $I=\tfrac83$. Exact again; Simpson is
exact for all polynomials of degree at most $3$, and both tests are consistent with its degree of
exactness $3$.

**3.** *Strategy: evaluate at the midpoint and compare with the exact integral and the bound.*

$M=1\cdot e^{-0.5}=0.606531$, $I=1-e^{-1}=0.632121$, so $I-M=+0.025590$: the rule underestimates.
The bound is $\frac{(b-a)^3}{24}\lVert f''\rVert_\infty=\frac{1}{24}=0.041667$, and the actual error is
$61\%$ of it. The sign is positive because $f''=e^{-x}>0$ and the midpoint rule underestimates a convex
function — the opposite of the trapezoid rule's sign.

**4.** *Strategy: write the two basis polynomials and integrate.*

With nodes $a,b$ and $h=b-a$, $\ell_0(x)=\frac{b-x}{h}$ and $\ell_1(x)=\frac{x-a}{h}$. Then

$$w_0=\frac1h\int_a^b(b-x)\,dx=\frac1h\Bigl[bx-\frac{x^2}{2}\Bigr]_a^b
=\frac1h\cdot\frac{(b-a)^2}{2}=\frac h2,$$

because $\bigl[bx-\tfrac{x^2}{2}\bigr]_a^b=b^2-\tfrac{b^2}{2}-ab+\tfrac{a^2}{2}=\tfrac{(b-a)^2}{2}$.
Similarly $\int_a^b(x-a)\,dx=\tfrac{(b-a)^2}{2}$, so $w_1=\tfrac h2$. The weights are equal and sum to
$h=b-a$.

**5.** *Strategy: integrate each Lagrange basis on $[0,1]$ with nodes $0,\tfrac12,1$.*

$\ell_0=\frac{(x-\frac12)(x-1)}{(0-\frac12)(0-1)}=2(x-\tfrac12)(x-1)=2x^2-3x+1$, whose integral is
$\tfrac23-\tfrac32+1=\tfrac16$. $\ell_1=\frac{x(x-1)}{(\frac12)(-\frac12)}=-4x(x-1)=-4x^2+4x$, with
integral $-\tfrac43+2=\tfrac23$. $\ell_2=\frac{x(x-\frac12)}{(1)(\frac12)}=2x^2-x$, with integral
$\tfrac23-\tfrac12=\tfrac16$. The weights $\tfrac16,\tfrac23,\tfrac16$ sum to $1$, and
$Q=\tfrac16f(0)+\tfrac23f(\tfrac12)+\tfrac16f(1)=\tfrac{h}{3}(f_0+4f_1+f_2)$ with $h=\tfrac12$.

**6.** *Strategy: test $1,x,x^2$ and compare with the error term.*

The trapezoid rule integrates $1$ exactly ($T=b-a$) and $x$ exactly (both sides equal $\tfrac{b^2-a^2}{2}$).
For $x^2$ on $[0,1]$: $T=\tfrac12$ and $I=\tfrac13$, so $I-T=-\tfrac16\neq0$. The error term gives
$-\frac{1}{12}f''=-\frac{2}{12}=-\frac16$, in agreement. Hence the degree of exactness is $1$.

**7.** *Strategy: evaluate $f=1/(1+x)$ at $x=0,\tfrac14,\tfrac12,\tfrac34,1$ and apply the composite
formula.*

$f$ values: $1,\ 0.8,\ 0.666667,\ 0.571429,\ 0.5$. Then

$$T_4=\frac{0.25}{2}\bigl(1+2(0.8)+2(0.666667)+2(0.571429)+0.5\bigr)
=0.125(5.576190)=0.697024 .$$

Since $\ln2=0.693147$, $I-T_4=-0.003877$. The bound is
$\frac{(b-a)h^2}{12}\lVert f''\rVert_\infty=\frac{0.0625}{12}\cdot2=0.010417$; note $\lVert f''\rVert_\infty=2$
at $x=0$. The error is negative (overestimate) because $f''=2/(1+x)^3>0$.

**8.** *Strategy: use the composite Simpson formula with $m=4$, $h=\tfrac14$, and compare.*

$$S_4=\frac{0.25}{3}\bigl(1+4(0.8)+2(0.666667)+4(0.571429)+0.5\bigr)
=\frac{0.25}{3}(8.319048)=0.693254 .$$

$I-S_4=-0.000107$ (more precisely $-1.07\times10^{-4}$), about $36$ times smaller than the trapezoid
error for the same $h$. The bound is $\frac{(b-a)h^4}{180}\lVert f^{(4)}\rVert_\infty
=\frac{0.00390625}{180}\cdot24=5.208\times10^{-4}$, and the error is $21\%$ of it.

**9.** *Strategy: substitute the nodes and weights into the moments and compare with $\int_{-1}^1x^kdx$.*

With $x_1=-\tfrac{1}{\sqrt3}$, $x_2=\tfrac{1}{\sqrt3}$, $w_1=w_2=1$:

* $k=0$: $1+1=2=\int_{-1}^11\,dx$.
* $k=1$: $-\tfrac{1}{\sqrt3}+\tfrac{1}{\sqrt3}=0$.
* $k=2$: $\tfrac13+\tfrac13=\tfrac23=\int_{-1}^1x^2dx$.
* $k=3$: $-\tfrac{1}{3\sqrt3}+\tfrac{1}{3\sqrt3}=0$.
* $k=4$: $\tfrac19+\tfrac19=\tfrac29$, but $\int_{-1}^1x^4dx=\tfrac25$. Not exact.

Hence the rule has degree of exactness $3=2n-1$ for $n=2$.

**10.** *Strategy: apply Richardson with $p=2$, so the factor is $4^1-1=3$.*

$R_{1,1}=T(0.5)+\frac{T(0.5)-T(1)}{4-1}=3.1+\frac{0.1}{3}=3.133333$. The exact value is
$\pi=3.141593$, so the extrapolated value is off by $8.259\times10^{-3}$, better than $T(0.5)$ by a
factor $5$.

**11.** *Strategy: the composite trapezoid error is $ch^2+\dots$, so the Richardson combination with
$p=2$ cancels the leading term.*

$T_8-T_4=0.694122-0.697024=-0.002902$. The estimate is

$$I\approx T_8+\frac{T_8-T_4}{4-1}=0.694122-0.000967=0.693155 .$$

The exact value is $\ln2=0.693147$, so the error is $+7.4\times10^{-6}$, a factor $132$ better than the
$9.75\times10^{-4}$ error of $T_8$ alone.

**12.** *Strategy: the local error is estimated by $(S_2-S_1)/15$, and the corrected value adds it back.*

The estimate is $\lvert S_2-S_1\rvert/15=0.018455/15=1.230\times10^{-3}$, and the corrected value is

$$S_2+\frac{S_2-S_1}{15}=0.656526+0.001230=0.657757 .$$

Since $1.230\times10^{-3}\le10^{-2}$, the panel would be accepted at tolerance $10^{-2}$. The corrected
value is still far from $\tfrac23$ because the estimate measures the error of the *two-panel* rule; the
true error is $8.910\times10^{-3}$, which is within $10^{-2}$ but only just.

## Intermediate

**13.** *Strategy: apply composite Simpson with $h=\pi/6$ and compare with the exact integral.*

$h=\tfrac{\pi}{6}=0.523599$, and the values of $\sin$ at the nodes $0,\tfrac\pi6,\tfrac\pi3,\tfrac\pi2,
\tfrac{2\pi}3,\tfrac{5\pi}6,\pi$ are $0,0.5,0.866025,1,0.866025,0.5,0$. Hence

$$S_6=\frac{0.523599}{3}\bigl(0+4(0.5)+2(0.866025)+4(1)+2(0.866025)+4(0.5)+0\bigr)
=0.174533(11.464102)=2.000863 .$$

The error is $2-2.000863=-8.632\times10^{-4}$. The bound is
$\frac{(b-a)h^4}{180}\lVert f^{(4)}\rVert_\infty=\frac{\pi(0.523599)^4}{180}=1.312\times10^{-3}$, so the
error is $66\%$ of the bound — reasonable for a function whose fourth derivative is bounded by $1$ and
varies over the interval.

**14.** *Strategy: solve $\frac{(b-a)h^2}{12}M_2\le10^{-6}$ with $h=1/m$.*

Here $b-a=1$, $M_2=e$, so the condition is $\frac{e}{12m^2}\le10^{-6}$, that is
$m^2\ge\frac{e}{12}\cdot10^6=226523$ and $m\ge475.94$. The smallest admissible number is $m=476$, for
which the bound is $\frac{e}{12\cdot476^2}=9.998\times10^{-7}$. With $m=475$ the bound would be
$1.004\times10^{-6}$, just above the tolerance.

**15.** *Strategy: solve $\frac{(b-a)h^4}{180}M_4\le10^{-6}$ with $h=1/m$.*

The condition is $\frac{e}{180m^4}\le10^{-6}$, so $m^4\ge\frac{e}{180}\cdot10^6=15101.5$ and
$m\ge11.085$. Composite Simpson also needs $m$ even, so the smallest admissible number is $m=12$, with
bound $\frac{e}{180\cdot12^4}=7.283\times10^{-7}$. The comparison is dramatic: $476$ trapezoid panels
versus $12$ Simpson panels, $477$ evaluations versus $25$. The factor is about $19$ in favour of Simpson,
which is the practical value of two extra orders.

**16.** *Strategy: compute the trapezoid values at $h=1,\tfrac12,\tfrac14$ and apply
$R_{k,j}=R_{k,j-1}+(R_{k,j-1}-R_{k-1,j-1})/(4^j-1)$.*

| $k$ | $R_{k,0}$ | $R_{k,1}$ | $R_{k,2}$ |
|---|---|---|---|
| $0$ | $1.859140914$ | | |
| $1$ | $1.753931092$ | $1.718861152$ | |
| $2$ | $1.727221905$ | $1.718318842$ | $1.718282688$ |

The exact value is $e-1=1.718281828$. The diagonal errors are $1.41\times10^{-1}$,
$5.79\times10^{-4}$ and $8.59\times10^{-7}$, so each row gains about three digits. Note that $R_{1,1}$
equals Simpson with two panels, as it must.

**17.** *Strategy: integrate the four basis polynomials on $[0,3]$ with nodes $0,1,2,3$.*

For equispaced nodes the Lagrange basis is $\ell_i(x)=\prod_{j\ne i}\frac{x-j}{i-j}$, and the weights are
$w_i=\int_0^3\ell_i$. Computing (each $\ell_i$ is a cubic, integrated termwise) gives
$w_0=w_3=\tfrac38$ and $w_1=w_2=\tfrac98$. The weights sum to $\tfrac38+\tfrac98+\tfrac98+\tfrac38=3$,
and with $h=1$ the rule is $\frac{3h}{8}(f_0+3f_1+3f_2+f_3)$.

For $x^3$: $I=\tfrac{81}{4}=20.25$ and $Q=\tfrac38(0+3+24+27)=\tfrac38(54)=20.25$: exact.
For $x^4$: $I=\tfrac{243}{5}=48.6$ and $Q=\tfrac38(0+3+48+81)=\tfrac38(132)=49.5$, so
$I-Q=-0.9$. The error term gives $-\frac{3h^5}{80}f^{(4)}=-\frac{3}{80}\cdot24=-0.9$, in agreement.

**18.** *Strategy: integrate the five basis polynomials on $[0,4]$, then test on $x^5$ and $x^6$.*

The weights are $w_0=w_4=\tfrac{14}{45}$, $w_1=w_3=\tfrac{64}{45}$, $w_2=\tfrac{24}{45}=\tfrac{8}{15}$.
They sum to $\frac{14+64+24+64+14}{45}=\frac{180}{45}=4$, and with $h=1$ the rule is
$\frac{2h}{45}(7f_0+32f_1+12f_2+32f_3+7f_4)$.

For $x^5$: $I=\frac{4^6}{6}=682.667$ and $Q=\frac{2}{45}(0+32+384+7776+7168)=\frac{2}{45}(15360)=682.667$:
exact. For $x^6$: $I=\frac{4^7}{7}=2340.571$ and
$Q=\frac{2}{45}(0+32+768+23328+28672)=\frac{2}{45}(52800)=2346.667$, so $I-Q=-6.095$. The error term
gives $-\frac{8h^7}{945}f^{(6)}=-\frac{8}{945}\cdot720=-6.095$, in agreement.

**19.** *Strategy: use nodes $0,\pm\sqrt{3/5}$ and weights $\tfrac89,\tfrac59,\tfrac59$.*

For $x^6$: $I=\int_{-1}^1x^6dx=\tfrac27=0.285714$. The rule gives
$Q=\tfrac59\bigl(-\sqrt{3/5}\bigr)^6+\tfrac89(0)+\tfrac59\bigl(\sqrt{3/5}\bigr)^6
=\tfrac{10}{9}\cdot\tfrac{27}{125}=\tfrac{30}{125}=0.24$. The error is $0.045714=\tfrac{8}{175}$. The rule
is exact through degree $5$: for $x^4$ it gives $\tfrac{10}{9}\cdot\tfrac{9}{25}=\tfrac25$, which is
$\int_{-1}^1x^4dx$. Hence the degree of exactness is $5$.

**20.** *Strategy: transform the nodes and weights to $[0,1]$ and evaluate $\sqrt x$.*

The nodes are $x=\tfrac12\pm\tfrac{1}{2\sqrt3}$, that is $0.211325$ and $0.788675$, with weights
$\tfrac12,\tfrac12$. Then $\sqrt{0.211325}=0.459701$ and $\sqrt{0.788675}=0.888074$, so

$$Q=\tfrac12(0.459701+0.888074)=0.673887 .$$

The exact value is $\tfrac23=0.666667$, so $I-Q=-0.007221$: the rule overestimates. Simpson with three
evaluations gives $0.638071$ with error $0.028596$, four times worse. Gauss is more accurate here even
though $\sqrt x$ has an infinite derivative at $0$, because the two Gauss nodes avoid the endpoint.

**21.** *Strategy: compute each rule with its own number of evaluations and compare errors.*

* Trapezoid, $m=4$ ($5$ evaluations): $3.131176$, error $1.0416\times10^{-2}$.
* Simpson, $m=4$ ($5$ evaluations): $3.141569$, error $2.4026\times10^{-5}$.
* Gauss–2 with two panels ($4$ evaluations): $3.141610$, error $1.724\times10^{-5}$.
* Gauss–3, one panel ($3$ evaluations): $3.141068$, error $5.245\times10^{-4}$.

Ranked by accuracy per evaluation: Gauss–2 (two panels) best, then Simpson $m=4$, then Gauss–3, then
trapezoid. Gauss–3 is theoretically of order $6$, but on a single panel the constant involves
$f^{(6)}(0)=2880$, so it loses to Simpson at this coarse resolution. This is the practical warning
behind the order table: order is asymptotic, and a single high-order panel can be beaten by a few
low-order panels.

**22.** *Strategy: run adaptive Simpson with the Richardson estimate and a tolerance of $10^{-8}$.*

The algorithm returns $0.746824132823$, using $29$ panels. The exact value is
$\frac{\sqrt\pi}{2}\operatorname{erf}(1)=0.746824132812$, so the error is $1.1\times10^{-11}$, well
inside the tolerance. The panels are concentrated near $0$ and $1$, because $e^{-x^2}$ has large higher
derivatives there; the middle of the interval is covered by a few large panels.

**23.** *Strategy: read the signs off the error terms.*

For the trapezoid rule, $I-T=-\frac{(b-a)^3}{12}f''(\eta)$. If $f$ is convex, $f''\ge0$, so $I-T\le0$,
that is $T\ge I$: the rule overestimates. For the midpoint rule, $I-M=+\frac{(b-a)^3}{24}f''(\eta)$, so
for convex $f$ we get $I-M\ge0$, that is $M\le I$: it underestimates. For a concave function both
inequalities reverse. The midpoint error is half the trapezoid error in magnitude for the same interval,
which is why the midpoint rule is preferred when the integrand is smooth and interior nodes are allowed.

**24.** *Strategy: sum panel errors and use the intermediate value theorem.*

Let $m$ be even, $h=(b-a)/m$ and let $[a+2kh,a+2(k+1)h]$, $k=0,\dots,m/2-1$, be the Simpson panels of
length $2h$. By Theorem 7.2 each panel contributes
$-\frac{(2h)^5}{2880}f^{(4)}(\eta_k)=-\frac{h^5}{90}f^{(4)}(\eta_k)$ with $\eta_k$ in that panel. Hence

$$I-S_m=-\frac{h^5}{90}\sum_{k=0}^{m/2-1}f^{(4)}(\eta_k)
=-\frac{(m/2)h^5}{90}f^{(4)}(\eta)$$

for some $\eta\in(a,b)$, by the intermediate value theorem applied to the average of the $m/2$ values of
$f^{(4)}$. Since $mh=b-a$, this is $-\frac{(b-a)h^4}{180}f^{(4)}(\eta)$. The hypotheses are $f\in C^4[a,b]$
and $m$ even; without the evenness the $4,2,4,\dots$ pattern does not close.

## Advanced

**25.** *Strategy: integrate the linear interpolation error against a sign-definite weight.*

On $[a,b]$ the linear interpolant is $p_1(x)=f(a)+\frac{f(b)-f(a)}{b-a}(x-a)$, and Theorem 7.4 of
[Interpolation and Approximation](../03-interpolation-and-approximation/README.md) gives

$$f(x)-p_1(x)=f[a,b,x]\,(x-a)(x-b),$$

where the divided difference $f[a,b,x]$ is continuous in $x$ because $f\in C^2$. Integrating,

$$I-T=\int_a^bf[a,b,x]\,(x-a)(x-b)\,dx .$$

The weight $(x-a)(x-b)$ is continuous and non-positive on $[a,b]$ and not identically zero, so the
weighted mean value theorem for integrals supplies $\eta\in(a,b)$ with
$I-T=f[a,b,\eta]\int_a^b(x-a)(x-b)dx$. The integral is $-\frac{(b-a)^3}{6}$, and
$f[a,b,\eta]=\frac12f''(\eta)$ by the mean value theorem for divided differences. Hence
$I-T=-\frac{(b-a)^3}{12}f''(\eta)$, as claimed. The sign is negative for $f''>0$, corresponding to the
trapezoid overestimating a convex function.

**26.** *Strategy: show that Simpson's rule is the integral of the cubic Hermite interpolant, then
integrate the Hermite error.*

Let $H$ be the cubic with $H(a)=f(a)$, $H(m)=f(m)$, $H(b)=f(b)$ and $H'(m)=f'(m)$. Simpson's rule uses only
$f(a),f(m),f(b)$, which equal $H(a),H(m),H(b)$; and Simpson's rule is exact for cubics, so
$S[f]=S[H]=\int_a^bH$. Therefore

$$I-S=\int_a^b(f-H)\,dx .$$

By Theorem 7.12 of [Interpolation and Approximation](../03-interpolation-and-approximation/README.md),

$$f(x)-H(x)=\frac{f^{(4)}(\xi(x))}{4!}(x-a)(x-m)^2(x-b).$$

The weight $(x-a)(x-m)^2(x-b)$ is continuous and non-positive on $[a,b]$, so the weighted mean value
theorem gives

$$I-S=\frac{f^{(4)}(\eta)}{24}\int_a^b(x-a)(x-m)^2(x-b)\,dx .$$

Substituting $x=a+ht$ with $h=\tfrac{b-a}{2}$ turns the integral into
$h^5\int_0^2t(t-1)^2(t-2)dt=-\tfrac{4}{15}h^5=-\tfrac{(b-a)^5}{120}$. Hence
$I-S=-\frac{(b-a)^5}{2880}f^{(4)}(\eta)$, which is the stated panel form since $b-a=2h$.

**27.** *Strategy: use the properties of the Lagrange basis and of the interpolant.*

The weights are $w_i=\int_a^b\ell_i$, so $\sum_iw_i=\int_a^b\sum_i\ell_i=\int_a^b1\,dx=b-a$ by the
partition of unity. If $f\in\Pi_n$, then the interpolant $p_n$ equals $f$ (uniqueness), so
$Q[f]=\int_a^bp_n=\int_a^bf$: the degree of exactness is at least $n$. Finally,
$E[f]=I-Q=\int_a^bf-\int_a^bp_n=\int_a^b(f-p_n)dx$, which is the integral of the interpolation error.
Substituting the interpolation error formula gives
$E[f]=\frac{1}{(n+1)!}\int_a^bf^{(n+1)}(\xi(x))\omega(x)dx$, which is the starting point for every error
term in this chapter.

**28.** *Strategy: divide by $P_n$, use orthogonality, then exhibit a polynomial of degree $2n$ that every
rule must fail.*

For the existence of weights exact on $\Pi_{n-1}$: the $n$ moment equations
$\sum_iw_ix_i^k=\int_{-1}^1x^kdx$, $k=0,\dots,n-1$, form a Vandermonde system in the weights with
distinct nodes, hence a unique solution.

For exactness on $\Pi_{2n-1}$: given $p\in\Pi_{2n-1}$, divide by $P_n$ to get $p=qP_n+r$ with
$\deg q\le n-1$ and $\deg r\le n-1$. Orthogonality gives $\int p=\int r$, and since $P_n(x_i)=0$,
$Q[p]=Q[r]=\int r$. Hence $Q[p]=\int p$.

For the upper bound: for any $n$-point rule and $p(x)=\prod_{i=1}^n(x-x_i)^2$, we have $p\ge0$, $p\not\equiv0$
and $\deg p=2n$, so $\int p>0$ while $Q[p]=\sum_iw_ip(x_i)=0$. Hence no $n$-point rule is exact at
degree $2n$, and the maximal degree of exactness is $2n-1$, attained by Gauss.

**29.** *Strategy: solve the four moment equations in general, then show the degree-4 moment cannot also
hold.*

The equations are

$$w_1+w_2=2,\quad w_1x_1+w_2x_2=0,\quad w_1x_1^2+w_2x_2^2=\frac23,\quad w_1x_1^3+w_2x_2^3=0 .$$

From the first and second, $w_2=2-w_1$ and $w_1x_1=(w_1-2)x_2$. If $x_1=x_2$ the rule has one distinct
node and cannot satisfy the $x^2$ equation with the $x$ equation; so $x_1\neq x_2$. Solving the first
three equations (for example by eliminating $w_2$ and using the identity
$w_1x_1^2+w_2x_2^2=\frac{(w_1x_1+w_2x_2)^2}{w_1+w_2}+w_1w_2\frac{(x_1-x_2)^2}{w_1+w_2}$) gives
$x_1+x_2=0$, $w_1=w_2=1$ and $x_1^2=x_2^2=\tfrac13$. The fourth equation is then automatic, and the
solution is $x=\pm1/\sqrt3$, $w=1$. For degree $4$ the rule would need
$w_1x_1^4+w_2x_2^4=\tfrac{2}{9}$ to equal $\tfrac25$, which fails. Hence the maximal degree for two
nodes is $3$, as Theorem 7.8 states in general.

**30.** *Strategy: induction on $j$, using $h_{k-1}=2h_k$.*

The Euler–Maclaurin expansion gives $R_{k,0}=T(h_k)=I+c_2h_k^2+c_4h_k^4+\dots$, which is the case $j=0$.
Suppose $R_{k,j-1}=I+c\,h_k^{2j}+O(h_k^{2j+2})$ for every $k$. Then, since $h_{k-1}=2h_k$,

$$R_{k-1,j-1}=I+c(2h_k)^{2j}+O(h_k^{2j+2})=I+4^jc\,h_k^{2j}+O(h_k^{2j+2}).$$

Therefore

$$R_{k,j}=R_{k,j-1}+\frac{R_{k,j-1}-R_{k-1,j-1}}{4^j-1}
=I+c h_k^{2j}+\frac{c h_k^{2j}-4^jc h_k^{2j}}{4^j-1}+O(h_k^{2j+2})=I+O(h_k^{2j+2}),$$

because $1+\frac{1-4^j}{4^j-1}=0$. Induction gives the claim for all $j\le k$. The hypothesis is that
the Euler–Maclaurin expansion is valid to order $2j+2$, which holds for $f\in C^{2j+2}[a,b]$.

**31.** *Strategy: compute the Peano kernel explicitly on the three subintervals and show it has one sign.*

For a rule of degree of exactness $3$, $E[f]=\frac{1}{3!}\int_0^3K(t)f^{(4)}(t)dt$ with
$K(t)=E[(x-t)_+^3]$. On $[0,3]$ with nodes $0,1,2,3$ and weights $\tfrac38,\tfrac98,\tfrac98,\tfrac38$,

$$K(t)=\frac{(3-t)^4}{4}-\sum_{i=0}^{3}w_i\,(x_i-t)_+^3 .$$

Because the rule is exact for cubics, the Peano kernel is $C^2$ and vanishes, together with its first two
derivatives, at each node; in particular $K(3)=K'(3)=K''(3)=0$. Evaluating the sum on the three
subintervals gives the factorisations

$$K(t)=\begin{cases}
\dfrac{t^3(2t-3)}{8}, & 0\le t\le1,\\[4pt]
\dfrac{(t^2-3t+3)(2t^2-6t+3)}{8}, & 1\le t\le2,\\[4pt]
\dfrac{(t-3)^3(2t-3)}{8}, & 2\le t\le3 .
\end{cases}$$

On $[0,1]$, $t^3\ge0$ and $2t-3<0$, so $K\le0$. On $[2,3]$, $(t-3)^3\le0$ and $2t-3>0$, so $K\le0$.
On $[1,2]$, $t^2-3t+3=(t-\tfrac32)^2+\tfrac34>0$ while
$2t^2-6t+3=2(t-\tfrac32)^2-\tfrac32\le-\tfrac12<0$, so $K<0$ there as well. Hence $K\le0$ on $[0,3]$,
with minimum $K(\tfrac32)=-\tfrac{9}{64}$ and $K(0)=K(1)=K(3)=0$.

Finally $\int_0^3K(t)\,dt=-\tfrac{9}{40}$, so the weighted mean value theorem gives

$$E[f]=\frac16\int_0^3K(t)f^{(4)}(t)dt=\frac{f^{(4)}(\eta)}{6}\Bigl(-\frac{9}{40}\Bigr)
=-\frac{3}{80}f^{(4)}(\eta),$$

which is $-\tfrac{3h^5}{80}f^{(4)}(\eta)$ with $h=1$. The numerical check on $x^4$ gave $I-Q=-0.9$,
in agreement with $-\tfrac{3}{80}\cdot24$.

## Challenge

**32.** *Strategy: sum the panel error with the exact fourth derivative, which is constant for $x^4$.*

For $f\in C^4$, Theorem 7.4 gives $I-S_m=-\frac{(b-a)h^4}{180}f^{(4)}(\eta)$ with $h=(b-a)/m$, so the
error is $O(h^4)$ and the constant is bounded by $\lVert f^{(4)}\rVert_\infty/180$.

For $f=x^4$ on $[0,1]$, $f^{(4)}=24$ is constant, so the mean value theorem is exact and

$$I-S_m=-\frac{1\cdot h^4}{180}\cdot24=-\frac{2h^4}{15}=-\frac{2}{15m^4}.$$

Check with $m=2$: $-\frac{2}{15\cdot16}=-\frac{1}{120}=-0.008333$, which is the value computed in
Section 7.3 of the tutorial for the three-point rule on $[0,1]$. The constant is therefore sharp: no
better power of $h$ and no smaller constant (for this $f$) is possible, because the error formula is an
equality with $f^{(4)}$ constant.

**33.** *Strategy: compute $K$ explicitly and verify its sign piecewise.*

For the two-point Gauss rule, $K(t)=\int_{-1}^1(x-t)_+^3dx-\sum_i(x_i-t)_+^3$ with
$x_i=\pm s=\pm1/\sqrt3$. The first term is $\frac{(1-t)^4}{4}$. Hence

$$K(t)=\begin{cases}
\dfrac{(1-t)^4}{4}, & s\le t\le1,\\[6pt]
\dfrac{(1-t)^4}{4}-(s-t)^3, & -s\le t\le s,\\[6pt]
\dfrac{(1-t)^4}{4}-(s-t)^3-(-s-t)^3, & -1\le t\le -s.
\end{cases}$$

* On $[s,1]$: $K\ge0$, with $K(1)=0$.
* On $[-s,s]$: $K''=3(1-t)^2-6(s-t)$ and $K'=-(1-t)^3+3(s-t)^2$; at the endpoints $K'>0$ at $-s$ and
  $K'<0$ at $s$, and the only interior zero of $K'$ is $t=0$, a maximum. Hence the minimum on the
  interval is at an endpoint, where $K=\tfrac79-\tfrac{4\sqrt3}{9}=0.007977>0$.
* On $[-1,-s]$: $K(-1)=0$, and $K''''=6>0$ with $K'(-1)=K''(-1)=K'''(-1)=0$, so $K$ increases from $0$
  and is positive inside.

Thus $K\ge0$ on $[-1,1]$. Its integral is $\int_{-1}^1K\,dt=\frac{2}{45}$, so

$$E[f]=\frac{1}{6}\int_{-1}^1K(t)f^{(4)}(t)dt=\frac{f^{(4)}(\xi)}{6}\cdot\frac{2}{45}
=\frac{f^{(4)}(\xi)}{135},$$

which is the stated constant $C_2$.

**34.** *Strategy: use the $h^4$ scaling of the Simpson error on a panel and solve for the correction.*

Let $S_1=S[a,b]$ and $S_2=S[a,m]+S[m,b]$ with $m=\tfrac{a+b}{2}$. For a smooth $f$,
$S_1=I+c(b-a)^5+O((b-a)^6)$ and $S_2=I+2c\bigl(\tfrac{b-a}{2}\bigr)^5+O((b-a)^6)
=I+\tfrac{c}{16}(b-a)^5+O((b-a)^6)$. Subtracting,

$$S_2-S_1=-\frac{15}{16}c(b-a)^5+O((b-a)^6),\qquad
I-S_2=-\frac{c}{16}(b-a)^5+O((b-a)^6)=\frac{S_2-S_1}{15}+O((b-a)^6).$$

Hence $(S_2-S_1)/15$ estimates the error of $S_2$, and

$$S:=S_2+\frac{S_2-S_1}{15}=I+O((b-a)^6),$$

because the $O((b-a)^5)$ term has been removed. The corrected value is therefore locally of order $6$,
although it is built from order-$4$ rules. The estimate is the basis of the adaptive acceptance test:
accept when $\lvert S_2-S_1\rvert/15\le\varepsilon$.

**35.** *Strategy: integrate by parts once against the parabolic kernel $B(x)=\tfrac12x(h-x)$.*

On a panel $[0,h]$ let $I=\int_0^hf$ and $T=\frac h2(f(0)+f(h))$. Define $B(x)=\tfrac12x(h-x)$, so
$B(0)=B(h)=0$ and $B\ge0$. Two integrations by parts give

$$\int_0^hB(x)f''(x)dx=\bigl[Bf'\bigr]_0^h-\int_0^hB'f'
=-\int_0^h\frac{h-2x}{2}f'(x)dx .$$

Integrating the last term by parts,

$$-\int_0^h\frac{h-2x}{2}f'=\Bigl[-\frac{h-2x}{2}f\Bigr]_0^h-\int_0^h f
=\frac h2f(h)+\frac h2f(0)-I=T-I .$$

Hence $T-I=\int_0^h\tfrac12x(h-x)f''(x)dx$. Since the kernel is non-negative and
$\int_0^hB\,dx=\frac{h^3}{12}$, the weighted mean value theorem gives
$T-I=\frac{h^3}{12}f''(\eta)$, that is $I-T=-\frac{h^3}{12}f''(\eta)$. Summing over panels recovers the
composite formula with $h=(b-a)/m$.

For $\int_0^1e^xdx$ with $h=1$: $T-I=0.140859$, so $f''(\eta)=12(0.140859)=1.690309$ and
$\eta=\ln1.690309=0.524911$, consistent with $f''=e^x$ and $\eta\in(0,1)$.

**36.** *Strategy: map $[0,\infty)$ to $(0,1)$ by $x=t/(1-t)$, then apply Gauss–Legendre with many
nodes.*

With $x=\frac{t}{1-t}$, $dx=\frac{dt}{(1-t)^2}$, so

$$\int_0^\infty e^{-x^2}dx=\int_0^1\frac{1}{(1-t)^2}\exp\Bigl(-\frac{t^2}{(1-t)^2}\Bigr)dt .$$

The transformed integrand tends to $0$ faster than any power as $t\to1$, so it is smooth on $[0,1]$ and
Gauss–Legendre converges rapidly. Applying the rule with $n$ nodes scaled to $[0,1]$ gives

| $n$ | value | error against $\sqrt\pi/2=0.8862269255$ |
|---|---|---|
| $10$ | $0.8870584163$ | $8.31\times10^{-4}$ |
| $20$ | $0.8862261838$ | $-7.42\times10^{-7}$ |
| $32$ | $0.8862269271$ | $1.64\times10^{-9}$ |
| $40$ | $0.8862269254$ | $-9.1\times10^{-12}$ |

Successive doubling of $n$ reduces the error by many orders, as expected for an analytic integrand. The
value agrees with $\frac{\sqrt\pi}{2}\operatorname{erf}(\infty)=\frac{\sqrt\pi}{2}$. The substitution is
the important step: applying Gauss directly to $[0,R]$ for large $R$ would waste nodes on the region where
the integrand is negligible, and truncating at finite $R$ would introduce a truncation error of order
$e^{-R^2}/(2R)$.
