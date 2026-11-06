# Interpolation and Approximation — Solutions

> [Interpolation and Approximation](README.md) · Solutions to the 36 problems in [exercises.md](exercises.md)

Each solution states the strategy first, then carries out every step and closes computations with a
check. Bounds are derived from the theorems of the [tutorial](README.md); where a bound is much larger
than the actual error, that is remarked on rather than hidden. Common pitfalls are flagged where they
are likely.

## Beginner

**1.** *Strategy: compute the three Lagrange basis polynomials, combine them with the data values, then
expand and verify.*

With nodes $0,1,3$,

$$\ell_0=\frac{(x-1)(x-3)}{(0-1)(0-3)}=\frac{x^2-4x+3}{3},\qquad
\ell_1=\frac{x(x-3)}{(1)(1-3)}=-\frac{x^2-3x}{2},\qquad
\ell_2=\frac{x(x-1)}{(3)(2)}=\frac{x^2-x}{6}.$$

Therefore

$$
p=2\ell_0+3\ell_1+\ell_2
=\Bigl(\tfrac23-\tfrac32+\tfrac16\Bigr)x^2+\Bigl(-\tfrac83+\tfrac92-\tfrac16\Bigr)x+2
=-\tfrac23x^2+\tfrac53x+2 .
$$

Check: $p(0)=2$; $p(1)=-\tfrac23+\tfrac53+2=3$; $p(3)=-6+5+2=1$. The degree is $2$, as it must be for
three nodes unless the leading coefficient happens to vanish (it does not here). A useful guard: the
coefficients of the three basis polynomials sum to $1$, and indeed $\tfrac23-\tfrac32+\tfrac16=0$ for
$x^2$ and the constant term is $2=2\ell_0(0)$.

**2.** *Strategy: write each basis polynomial from its roots, then verify the identities algebraically.*

$$\ell_0=\frac{(x-1)(x-2)}{(0-1)(0-2)}=\frac{x^2-3x+2}{2},\qquad
\ell_1=\frac{x(x-2)}{(1)(-1)}=-x^2+2x,\qquad
\ell_2=\frac{x(x-1)}{(2)(1)}=\frac{x^2-x}{2}.$$

Sum: the $x^2$ coefficients are $\tfrac12-1+\tfrac12=0$, the $x$ coefficients are
$-\tfrac32+2-\tfrac12=0$, and the constant is $1$. Hence $\sum\ell_i=1$ identically. Next,

$$\sum_i x_i\ell_i=0\cdot\ell_0+1\cdot(-x^2+2x)+2\cdot\frac{x^2-x}{2}=-x^2+2x+x^2-x=x .$$

At $x=3$ the values are $\ell_0(3)=1$, $\ell_1(3)=-3$, $\ell_2(3)=3$; they sum to $1$, and
$0\cdot1+1\cdot(-3)+2\cdot3=3$, as required. This is Proposition 7.2 in action.

**3.** *Strategy: build the table, read the top row as Newton coefficients, and expand.*

| $x_i$ | $f[x_i]$ | first | second |
|---|---|---|---|
| $1$ | $1$ | | |
| $2$ | $4$ | $3$ | |
| $4$ | $16$ | $6$ | $1$ |

The first differences are $(4-1)/(2-1)=3$ and $(16-4)/(4-2)=6$; the second is $(6-3)/(4-1)=1$. Hence

$$p_2(x)=1+3(x-1)+1\,(x-1)(x-2)=1+3x-3+x^2-3x+2=x^2 .$$

The reduction to $x^2$ is not an accident: the data lie on a quadratic, and interpolation reproduces
polynomials of degree at most $2$ exactly. The next divided difference would involve a fourth node
$x_3$ and the three second differences; since every second difference of a quadratic is the constant
leading coefficient $1$ (and here it is already constant), the third difference is $0$. In general the
$k$-th divided difference of a polynomial of degree $d$ vanishes for $k>d$.

**4.** *Strategy: use Newton's form, which is the fastest route from three values to the polynomial.*

The divided differences are $f[x_0]=1$, $f[x_0,x_1]=(0-1)/(1-0)=-1$,
$f[x_1,x_2]=(3-0)/(2-1)=3$, and
$f[x_0,x_1,x_2]=(3-(-1))/(2-0)=2$. Therefore

$$p(x)=1+(-1)(x-0)+2(x-0)(x-1)=1-x+2x^2-2x=2x^2-3x+1 .$$

Check: $p(0)=1$, $p(1)=2-3+1=0$, $p(2)=8-6+1=3$. All three conditions hold.

**5.** *Strategy: apply the linear interpolation error formula on $[1,2]$, then locate the actual maximum
by differentiating the error.*

Here $n=1$, $h=1$, $f''(x)=-1/x^2$, so $\lVert f''\rVert_\infty=1$ on $[1,2]$ and

$$\lvert\ln x-p_1(x)\rvert\le\frac{1^2}{8}\cdot1=0.125 .$$

The actual error is $e(x)=\ln x-(x-1)\ln2$, whose derivative is $1/x-\ln2$. It vanishes at
$x=1/\ln2=1.442695$, where

$$e=\ln(1.442695)-0.442695\cdot0.693147=0.366513-0.306853=0.059660 .$$

So the true maximum is about $0.0597$, roughly half the bound. The bound is not sharp because
$\lvert f''\rvert$ attains its maximum $1$ only at the left endpoint, where $\lvert\omega\rvert=0$; the
two factors of the error formula peak at different points.

**6.** *Strategy: count conditions, compare with the dimension of $\Pi_{2n+1}$, and quote the Hermite
error theorem.*

Four nodes, each contributing a value and a derivative, impose $2\cdot4=8$ conditions. The space
$\Pi_7$ has dimension $8$, so the interpolant has degree at most $7=2n+1$ with $n+1=4$. Uniqueness holds
because a polynomial satisfying the homogeneous conditions has each node as a double root, hence is
divisible by $\prod_i(x-x_i)^2$ of degree $8$, which forces it to be zero. The error is

$$f(x)-H(x)=\frac{f^{(8)}(\xi)}{8!}\prod_{i=0}^{3}(x-x_i)^2,$$

with $\xi$ in the hull of $x$ and the four nodes, valid for $f\in C^8$.

**7.** *Strategy: quote Theorem 7.8 with $h=\tfrac12$ and $f''=e^x$, then compute the actual maxima from
$e'(x)=0$ on each panel.*

The bound is

$$\lvert e^x-S_1(x)\rvert\le\frac{h^2}{8}\lVert f''\rVert_\infty=\frac{0.25}{8}\,e=0.084946 .$$

On a panel $[a,b]$ the error is $e^x-p(x)$ with $p$ the chord; its derivative is $e^x-\frac{e^b-e^a}{b-a}$,
which vanishes at $x^\ast=\ln\frac{e^b-e^a}{b-a}$. On $[0,0.5]$ the slope is $2(e^{0.5}-1)=1.297443$,
so $x^\ast=0.260395$ and the error magnitude is
$\lvert e^{x^\ast}-1-1.297443x^\ast\rvert=0.040405$. On $[0.5,1]$ the slope is $2(e-e^{0.5})=2.139121$,
$x^\ast=0.760395$, and the error magnitude is
$\lvert 2.139121-2.139121(0.760395-0.5)-e^{0.5}\rvert=0.066617$.
Both lie below the bound. The second panel is worse because both $e^x$ and the chord slope are larger
there; the error scales with $f''=e^x$, which increases across the interval.

**8.** *Strategy: $x_k=\cos\frac{(2k+1)\pi}{2(n+1)}$ with $n=2$; then compute $\omega$ and its extrema.*

The nodes are $x_0=\cos\frac{\pi}{6}=\frac{\sqrt3}{2}$, $x_1=\cos\frac{\pi}{2}=0$,
$x_2=\cos\frac{5\pi}{6}=-\frac{\sqrt3}{2}$. Hence

$$\omega(x)=x\Bigl(x^2-\frac34\Bigr)=x^3-\frac34x .$$

Differentiating, $\omega'=3x^2-\tfrac34$, so the interior extrema are at $x=\pm\tfrac12$, where
$\omega=\pm(\tfrac18-\tfrac38)=\mp\tfrac14$; at $x=\pm1$, $\omega=\pm\tfrac14$. Thus
$\max\lvert\omega\rvert=\tfrac14=2^{-2}$, consistent with Corollary 7.7.

For the equispaced nodes $-1,0,1$, $\omega=x(x^2-1)=x^3-x$, and $\omega'=3x^2-1$ vanishes at
$x=\pm1/\sqrt3$, where $\lvert\omega\rvert=2/(3\sqrt3)=0.384900$. So the equispaced maximum is about
$1.54$ times the Chebyshev one, and this ratio grows with $n$.

**9.** *Strategy: insert the four data into the cubic Hermite basis with $t=x$, $h=1$.*

$$H=1\cdot(1+2x)(1-x)^2+0\cdot x(1-x)^2+2\cdot x^2(3-2x)+1\cdot x^2(x-1).$$

Expanding: $(1+2x)(1-x)^2=1-3x^2+2x^3$; $2x^2(3-2x)=6x^2-4x^3$; $x^2(x-1)=x^3-x^2$. Summing,

$$H=1+( -3+6-1)x^2+(2-4+1)x^3=1+2x^2-x^3 .$$

Checks: $H(0)=1$; $H(1)=1+2-1=2$; $H'(x)=4x-3x^2$, so $H'(0)=0$ and $H'(1)=4-3=1$. If the data came
from $f\in C^4$, the error would be $f(x)-H(x)=\frac{f^{(4)}(\xi)}{24}x^2(x-1)^2$.

**10.** *Strategy: one interior moment, solve the scalar moment equation, then write the two pieces.*

For three knots the only unknown is $M_1$. With $h_0=h_1=1$ and $y=(0,1,0)$,

$$\frac16M_0+\frac23M_1+\frac16M_2=(0-1)-(1-0)=-2,$$

and $M_0=M_2=0$ gives $M_1=-3$. On $[0,1]$,

$$S=-\frac{x^3}{2}+\frac32x,$$

and on $[1,2]$, with the local formula,

$$S=-\frac{(2-x)^3}{2}+\frac32(2-x).$$

Checks: $S(0)=0$, $S(1)=1$, $S(2)=0$; $S'(1^-)=-\tfrac32+\tfrac32=0$ and $S'(1^+)=\tfrac32-\tfrac32=0$;
$S''(1^-)=-3=S''(1^+)$; $S''(0)=0=S''(2)$. The curvature energy is
$\int_0^1 9x^2dx+\int_1^2 9(2-x)^2dx=3+3=6$, the minimum by Theorem 7.10.

**11.** *Strategy: form $\sum1,\sum t,\sum t^2,\sum b,\sum tb$, solve the $2\times2$ system, then compute
the residuals.*

With $t=(0,1,2,3)$ and $b=(0,1,3,4)$: $\sum1=4$, $\sum t=6$, $\sum t^2=14$, $\sum b=8$,
$\sum tb=0+1+6+12=19$. The normal equations are

$$4c_1+6c_2=8,\qquad 6c_1+14c_2=19 .$$

Multiplying the first by $3$ and dividing by $2$ is not needed: from the first,
$c_1=2-\tfrac32c_2$; substituting, $12-9c_2+14c_2=19$, so $5c_2=7$, $c_2=1.4$ and $c_1=2-2.1=-0.1$.
The fit is $\hat b=1.4t-0.1$. Predictions: $-0.1,1.3,2.7,4.1$; residuals $0.1,-0.3,0.3,-0.1$; sum of
squares $0.01+0.09+0.09+0.01=0.2$. The residuals sum to zero and $\sum t_jr_j=0$, as the normal
equations require.

**12.** *Strategy: use $c_k=\frac14\sum_jy_je^{-2\pi ijk/4}$ and simplify using $e^{-\pi i}=-1$.*

$c_0=\frac14(2+0+2+0)=1$. $c_1=\frac14(2+2e^{-2\pi i\cdot2/4})=\frac14(2+2e^{-\pi i})=0$.
$c_2=\frac14(2+2e^{-2\pi i})=1$. $c_3=\frac14(2+2e^{-3\pi i})=0$. Hence
$p(x)=1+e^{2ix}$. At $x_j=0,\tfrac\pi2,\pi,\tfrac{3\pi}2$, $e^{2ix_j}=1,-1,1,-1$, so
$p=2,0,2,0$, exactly the data. On the grid $e^{2ix_j}=\cos2x_j$, so the real function is
$1+\cos2x$.

## Intermediate

**13.** *Strategy: build the table, evaluate by Horner, then apply the error formula with the fourth
derivative and the node polynomial.*

| $x_i$ | $f[x_i]$ | first | second | third |
|---|---|---|---|---|
| $1$ | $1$ | | | |
| $2$ | $1/2$ | $-1/2$ | | |
| $3$ | $1/3$ | $-1/6$ | $1/6$ | |
| $4$ | $1/4$ | $-1/12$ | $1/24$ | $-1/24$ |

So

$$p_3(x)=1-\tfrac12(x-1)+\tfrac16(x-1)(x-2)-\tfrac1{24}(x-1)(x-2)(x-3).$$

At $x=2.5$: $1-0.75+\tfrac16(1.5)(0.5)-\tfrac1{24}(1.5)(0.5)(-0.5)
=0.25+0.125+0.015625=0.390625$. The true value is $0.4$, so the error is $0.009375$.

For the bound, $f^{(4)}=24/x^5$ has maximum $24$ on $[1,4]$, and
$\omega(2.5)=(1.5)(0.5)(-0.5)(-1.5)=0.5625$. Hence
$\lvert f-p\rvert\le\frac{24}{24}(0.5625)=0.5625$, which is sixty times the actual error. The exact
$\xi$ satisfies $f^{(4)}(\xi)=24(0.009375)/0.5625=0.4$, so $\xi^5=60$ and $\xi=2.268\in[1,4]$: the
formula is consistent, the bound is simply pessimistic because $\lvert\omega\rvert$ peaks at $x=2.5$
while $\lvert f^{(4)}\rvert$ peaks at $x=1$.

**14.** *Strategy: compute the chord, differentiate the error, and compare the maximum with the bound.*

The chord is $p(x)=1+\frac{\cos(\pi/4)-1}{\pi/4}x=1-0.372923x$. The error
$e(x)=\cos x-1+0.372923x$ has derivative $-\sin x+0.372923$, which vanishes at
$x^\ast=\arcsin(0.372923)=0.382158$. There

$$e=\cos(0.382158)-(1-0.372923\cdot0.382158)=0.927862-0.857485=0.070378 .$$

The bound is $h^2\lVert f''\rVert_\infty/8=(\pi/4)^2/8=0.077106$, so the actual error is about $91\%$ of
the bound — reasonably sharp here because $\lvert f''\rvert=\cos x$ varies only between $0.707$ and $1$
on this short interval. It is not exactly attained, since $\lvert f''\rvert$ is largest at $x=0$ where
$\lvert\omega\rvert=0$.

**15.** *Strategy: compute both node polynomials, apply Corollary 7.5 with $\lVert f^{(5)}\rVert_\infty=e$,
then compare with a numerical evaluation.*

Equispaced nodes $-1,-\tfrac12,0,\tfrac12,1$: the node polynomial is
$\omega_{\mathrm{eq}}=x(x^2-1)(x^2-\tfrac14)$, whose maximum on $[-1,1]$ is $0.113482$.

Chebyshev nodes $x_k=\cos\frac{(2k+1)\pi}{10}$: $\max\lvert\omega_{\mathrm{ch}}\rvert=2^{-4}=0.0625$.

Since $f^{(5)}=-e^{-x}$ and $\lvert f^{(5)}\rvert\le e$ on $[-1,1]$, the bounds are

$$\text{equispaced: }\frac{e}{120}(0.113482)=0.002571,\qquad
\text{Chebyshev: }\frac{e}{120}(0.0625)=0.001416 .$$

Evaluating both interpolants on a fine grid gives maximum errors $1.1244\times10^{-3}$ and
$6.3970\times10^{-4}$. Both bounds hold, and Chebyshev is better by a factor $1.758$ at this degree.

**16.** *Strategy: use uniqueness of the interpolant of the constant function, then bound.*

The constant polynomial $1$ lies in $\Pi_n$ and interpolates the data $y_i=1$ at the $n+1$ nodes, so by
Theorem 7.1 it equals its own Lagrange form: $\sum_i1\cdot\ell_i(x)=1$ for all $x$. Then for every $x$,

$$\sum_i\lvert\ell_i(x)\rvert\ge\Bigl\lvert\sum_i\ell_i(x)\Bigr\rvert=1,$$

so $\Lambda_n=\max_x\sum_i\lvert\ell_i(x)\rvert\ge1$. Equality holds exactly when no $\ell_i$ changes
sign on $[a,b]$. For $n=0$ (one node) $\ell_0\equiv1$ and $\Lambda_0=1$. For $n\ge1$ and more than one
node, each $\ell_i$ has zeros at the other nodes while $\ell_i(x_i)=1$, so it takes both signs and
$\sum_i\lvert\ell_i\rvert>1$ strictly at some points; hence $\Lambda_n>1$.

**17.** *Strategy: the error bound depends on $h=\pi/n$; solve the inequality and round up.*

On $[0,\pi]$, $\lvert f''\rvert=\lvert\sin x\rvert\le1$. The bound is $h^2/8\le10^{-4}$, so
$h\le\sqrt{8\times10^{-4}}=0.0282843$ and $n\ge\pi/0.0282843=111.07$. The smallest admissible number is
$n=112$, giving $h=\pi/112=0.0280502$ and bound $h^2/8=9.835\times10^{-5}\le10^{-4}$. (With $n=111$ the
bound would be $1.0007\times10^{-4}$, just over the tolerance.)

**18.** *Strategy: two unknowns, two equations; solve in fractions by elimination, then write the three
pieces and differentiate.*

The right-hand sides are $r_1=y_2-2y_1+y_0=-2$ and $r_2=y_3-2y_2+y_1=1$. With all $h_i=1$ the system is

$$\frac46M_1+\frac16M_2=-2,\qquad \frac16M_1+\frac46M_2=1,$$

that is $4M_1+M_2=-12$, $M_1+4M_2=6$. From the second $M_1=6-4M_2$; substituting,
$24-16M_2+M_2=-12$, so $M_2=\tfrac{12}{5}$ and $M_1=-\tfrac{18}{5}$.

The pieces are

$$S_1=-\frac35x^3+\frac85x\quad[0,1],$$

$$S_2=-\frac35(2-x)^3+\frac25(x-1)^3+\frac85(2-x)-\frac25(x-1)\quad[1,2],$$

$$S_3=\frac25(3-x)^3-\frac25(3-x)\quad[2,3].$$

Values: $S_1(1)=1$, $S_2(1)=-\tfrac35+\tfrac85=1$, $S_2(2)=\tfrac25-\tfrac25=0$, $S_3(2)=\tfrac25-\tfrac25=0$,
$S_3(3)=0$. First derivatives: $S_1'=-\tfrac95x^2+\tfrac85$, $S_1'(1)=-\tfrac15$;
$S_2'=\tfrac95(2-x)^2+\tfrac65(x-1)^2-2$, $S_2'(1)=\tfrac95-2=-\tfrac15$ and $S_2'(2)=\tfrac65-2=-\tfrac45$;
$S_3'=-\tfrac65(3-x)^2+\tfrac25$, $S_3'(2)=-\tfrac65+\tfrac25=-\tfrac45$. Second derivatives:
$S_1''=-\tfrac95x$, $S_1''(1)=-\tfrac95$; $S_2''=-\tfrac95(2-x)+\tfrac{12}{5}(x-1)$, $S_2''(1)=-\tfrac95$,
$S_2''(2)=\tfrac{12}{5}$; $S_3''=\tfrac{12}{5}(3-x)$, $S_3''(2)=\tfrac{12}{5}$, $S_3''(3)=0$. Both $S'$
and $S''$ are continuous, and the natural conditions hold at both ends.

**19.** *Strategy: use $t=x-1$, $h=1$, and the four Hermite basis functions with $f(0)=0$, $f'(0)=1$,
$f(1)=\ln2$, $f'(1)=\tfrac12$.*

$$H=t(1-t)^2+(\ln2)t^2(3-2t)+\tfrac12t^2(t-1).$$

Expanding, $t(1-t)^2=t-2t^2+t^3$; $(\ln2)(3t^2-2t^3)$; and $\tfrac12(t^3-t^2)$. So

$$H=\Bigl(1-2\ln2+\tfrac12\Bigr)t^3+\Bigl(-2+3\ln2-\tfrac12\Bigr)t^2+t
=0.113706\,t^3-0.420558\,t^2+t .$$

At $t=0.5$: $0.014213-0.105139+0.5=0.409074$, while $\ln1.5=0.405465$; the error is $0.003609$.
The bound is $\frac{6}{24}\cdot\frac{1}{16}=\frac1{64}=0.015625$, since $\lvert f^{(4)}\rvert=6/x^4\le6$
on $[1,2]$ and $\max t^2(1-t)^2=\tfrac1{16}$. The error is comfortably inside the bound.

**20.** *Strategy: form the sums, solve the $3\times3$ system, and verify orthogonality of the residual.*

The data give $\sum1=4$, $\sum x=6$, $\sum x^2=14$, $\sum x^3=36$, $\sum x^4=98$, $\sum b=15$,
$\sum xb=32$, $\sum x^2b=82$. Hence

$$\begin{pmatrix}4&6&14\\6&14&36\\14&36&98\end{pmatrix}c=\begin{pmatrix}15\\32\\82\end{pmatrix}.$$

Solving (Gaussian elimination or substitution) gives $c_1=1.15$, $c_2=1.15$, $c_3=0.25$; check row 1:
$4(1.15)+6(1.15)+14(0.25)=4.6+6.9+3.5=15$; row 2: $6.9+16.1+9=32$; row 3: $16.1+41.4+24.5=82$.

The fit is $\hat b=1.15+1.15x+0.25x^2$, with values at $0,1,2,3$ equal to $1.15,2.55,4.45,6.85$ and
residuals $-0.15,0.45,-0.45,0.15$. The residual sum of squares is
$0.0225+0.2025+0.2025+0.0225=0.45$. Orthogonality: $\sum r=0$;
$\sum xr=0+0.45-0.9+0.45=0$; $\sum x^2r=0+0.45-1.8+1.35=0$.

**21.** *Strategy: compute the two Legendre coefficients and use the error formula.*

$c_0=\frac{\langle f,P_0\rangle}{\langle P_0,P_0\rangle}=\frac12\int_{-1}^1e^xdx=\frac{e-e^{-1}}{2}=1.175201$.
$c_1=\frac{\langle f,P_1\rangle}{\langle P_1,P_1\rangle}=\frac32\int_{-1}^1xe^xdx$. Integrating by parts,
$\int_{-1}^1xe^xdx=[(x-1)e^x]_{-1}^{1}=0-(-2)e^{-1}=2/e$, so $c_1=3/e=1.103638$. Thus
$p^\ast=1.175201+1.103638x$.

The error formula gives
$\lVert e^x-p^\ast\rVert_2^2=\lVert e^x\rVert_2^2-c_0^2\cdot2-c_1^2\cdot\tfrac23$. Now
$\lVert e^x\rVert_2^2=\frac{e^2-e^{-2}}{2}=3.626860$, $2c_0^2=2.762196$ and
$\tfrac23c_1^2=0.812011$, so the squared error is $0.052653$ and the norm is $0.229463$.

**22.** *Strategy: compute $c_0$ and $c_1$; the odd integral for $c_1$ vanishes.*

$c_0=\frac12\int_{-1}^1x^2dx=\frac12\cdot\frac23=\frac13$.
$c_1=\frac32\int_{-1}^1x^3dx=0$ because the integrand is odd. Hence $p^\ast=\frac13$: the best linear
approximation to $x^2$ is constant, since $x^2$ is even and the only even linear function is a constant.
The squared error is
$\int_{-1}^1(x^2-\tfrac13)^2dx=\int_{-1}^1(x^4-\tfrac23x^2+\tfrac19)dx=\frac25-\frac29+\frac29=\frac25-\frac29=\frac{8}{45}=0.177778$.

**23.** *Strategy: apply the DFT definition, then invert term by term.*

$$c_k=\frac14\sum_{j=0}^{3}y_je^{-2\pi ijk/4},\qquad y=(1,2,3,4).$$

$c_0=\frac14(1+2+3+4)=2.5$. $c_1=\frac14(1+2(-i)+3(-1)+4(i))=\frac14(-2+2i)=-0.5+0.5i$.
$c_2=\frac14(1+2(-1)+3(1)+4(-1))=\frac14(1-2+3-4)=-0.5$.
$c_3=\frac14(1+2(i)+3(-1)+4(-i))=\frac14(-2-2i)=-0.5-0.5i$.

Inverse check at $j=1$: $\sum_kc_ke^{2\pi ik/4}=2.5+(-0.5+0.5i)i+(-0.5)(-1)+(-0.5-0.5i)(-i)
=2.5+(-0.5i-0.5)+0.5+(0.5i-0.5)=2$. The other $j$ are similar. Conjugate symmetry holds:
$c_3=\overline{c_1}$ and $c_2$ is real (its imaginary part is zero), as it must be for real data.

**24.** *Strategy: write the three basis polynomials, remove the absolute values piecewise on $[0,1]$,
and maximise.*

$\ell_0=\frac{x(x-1)}{2}$, $\ell_1=1-x^2$, $\ell_2=\frac{x(x+1)}{2}$. On $[0,1]$,
$\ell_0\le0$, $\ell_1\ge0$, $\ell_2\ge0$, so

$$\Lambda(x)=-\frac{x(x-1)}{2}+(1-x^2)+\frac{x(x+1)}{2}
=\frac{-x^2+x+x^2+x}{2}+1-x^2=x+1-x^2 .$$

This concave quadratic has its maximum where $1-2x=0$, that is $x=\tfrac12$, and
$\Lambda(\tfrac12)=\tfrac12+1-\tfrac14=\tfrac54$. On $[-1,0]$ the computation is symmetric, giving the
same value at $x=-\tfrac12$. Hence $\Lambda_2=\tfrac54=1.25$. (At the nodes themselves
$\Lambda=1$; the maximum is attained strictly between nodes, which is typical.)

## Advanced

**25.** *Strategy: row operations followed by induction on the size.*

Let $V_n$ be the $(n+1)\times(n+1)$ matrix with entries $x_i^{k}$, $0\le i,k\le n$. Subtract row $0$
from rows $1,\dots,n$. For $k\ge1$ the new entry in row $i$ is
$x_i^{k}-x_0^{k}=(x_i-x_0)\sum_{m=0}^{k-1}x_i^{k-1-m}x_0^{m}$, and the first column becomes
$(1,0,\dots,0)^{\mathsf T}$. Expanding along the first column,

$$\det V_n=\det\bigl[(x_i-x_0)q_{k}(x_i)\bigr]_{i,k=1}^{n},\qquad q_k(x)=x^{k-1}+x^{k-2}x_0+\dots+x_0^{k-1}.$$

Factor $x_i-x_0$ from each row: $\det V_n=\prod_{i=1}^{n}(x_i-x_0)\det[q_k(x_i)]$. The matrix $[q_k(x_i)]$
has the same determinant as the Vandermonde matrix on $x_1,\dots,x_n$, because each $q_k$ is a monic
polynomial of degree $k-1$ and adding multiples of earlier columns to later ones does not change the
determinant. By induction,
$\det V_n=\prod_{i=1}^{n}(x_i-x_0)\prod_{1\le i<j\le n}(x_j-x_i)=\prod_{0\le i<j\le n}(x_j-x_i)$.

For distinct nodes every factor is nonzero, so $V$ is invertible and $Va=y$ has the unique solution
$a=V^{-1}y$ for every $y$. This proves existence and uniqueness of the interpolating polynomial
(Theorem 7.1). The hypothesis "distinct" is used exactly at the last step.

**26.** *Strategy: construct an auxiliary function with as many zeros as possible and apply Rolle's
theorem repeatedly.*

If $x$ is a node, both sides vanish, so assume $x\notin\{x_0,\dots,x_n\}$ and define

$$g(t)=f(t)-p_n(t)-\bigl(f(x)-p_n(x)\bigr)\frac{\omega(t)}{\omega(x)} .$$

Then $g$ is $n+1$ times differentiable on $[a,b]$. At $t=x_i$, $f(x_i)=p_n(x_i)$ and $\omega(x_i)=0$, so
$g(x_i)=0$; at $t=x$, $\omega(x)=\omega(x)$ and $g(x)=0$. Thus $g$ has the $n+2$ distinct zeros
$x_0,\dots,x_n,x$. Let $I$ be the smallest interval containing them. By Rolle's theorem, between any two
zeros of $g$ there is a zero of $g'$, so $g'$ has at least $n+1$ zeros in $I$; iterating, $g^{(j)}$ has
at least $n+2-j$ zeros in $I$ for $j\le n+1$. In particular $g^{(n+1)}$ has a zero $\xi\in I$.

Now $\deg p_n\le n$ gives $p_n^{(n+1)}\equiv0$, and $\omega$ is monic of degree $n+1$, so
$\omega^{(n+1)}\equiv(n+1)!$. Differentiating $g$ $n+1$ times,

$$0=g^{(n+1)}(\xi)=f^{(n+1)}(\xi)-\bigl(f(x)-p_n(x)\bigr)\frac{(n+1)!}{\omega(x)},$$

which rearranges to $f(x)-p_n(x)=f^{(n+1)}(\xi)\omega(x)/(n+1)!$. The point $\xi$ lies in the hull of
$x$ and all the nodes because that is where the zeros of $g$ are.

**27.** *Strategy: exhibit one polynomial attaining $2^{1-m}$ and show no other monic polynomial can beat
it, using the alternating extrema of $T_m$.*

$q^\ast=2^{1-m}T_m$ is monic of degree $m$ (the leading coefficient of $T_m$ is $2^{m-1}$) and
$\lvert q^\ast\rvert\le2^{1-m}$ on $[-1,1]$, so the minimum is at most $2^{1-m}$.

Let $q$ be monic of degree $m$ with $\max_{[-1,1]}\lvert q\rvert<2^{1-m}$. At $t_k=\cos(k\pi/m)$,
$k=0,\dots,m$, we have $T_m(t_k)=\cos(k\pi)=(-1)^k$, so $q(t_k)-2^{1-m}T_m(t_k)=q(t_k)-2^{1-m}(-1)^k$.
Since $\lvert q(t_k)\rvert<2^{1-m}$, the sign of this quantity is the sign of $-(-1)^k$, which alternates
with $k$. Hence $q-2^{1-m}T_m$ changes sign on each of the $m$ intervals $(t_k,t_{k+1})$ and therefore
has at least one zero in each. But $q$ and $2^{1-m}T_m$ are both monic of degree $m$, so their difference
has degree at most $m-1$ unless it is identically zero. A nonzero polynomial of degree at most $m-1$ has
at most $m-1$ zeros, a contradiction. Therefore $q=2^{1-m}T_m$, for which
$\lvert q(t_k)\rvert=2^{1-m}$, contradicting the strict inequality. So no monic $q$ has maximum
strictly below $2^{1-m}$, and the minimum is attained exactly by $q^\ast$.

**28.** *Strategy: prove the explicit symmetric formula by induction, then identify the Newton
coefficients as leading coefficients.*

Define $D_k=\sum_{i=0}^{k}f(x_i)\big/\prod_{j\ne i}(x_i-x_j)$ on distinct nodes. We show
$f[x_0,\dots,x_k]=D_k$ by induction on $k$; the right side is manifestly symmetric, so this proves
symmetry.

For $k=0$, $D_0=f(x_0)=f[x_0]$. Assume the claim for $k-1$ and use
$f[x_0,\dots,x_k]=\bigl(f[x_1,\dots,x_k]-f[x_0,\dots,x_{k-1}]\bigr)/(x_k-x_0)$. For $1\le i\le k-1$,
the $i$-th terms of the two sums, after division by $x_k-x_0$, combine to

$$\frac{f(x_i)}{x_k-x_0}\Bigl[\frac{1}{(x_i-x_k)D_i}-\frac{1}{(x_i-x_0)D_i}\Bigr]
=\frac{f(x_i)}{(x_i-x_0)(x_i-x_k)D_i},\qquad D_i=\prod_{j=1,j\ne i}^{k-1}(x_i-x_j),$$

because the bracket is $(x_k-x_0)/\bigl((x_i-x_k)(x_i-x_0)\bigr)$. The $i=k$ term of the first sum and
the $i=0$ term of the second are already the $i=k$ and $i=0$ terms of $D_k$. This proves the formula.

For the Newton form, let $q_k=q_{k-1}+f[x_0,\dots,x_k]\prod_{j<k}(x-x_j)$ with $q_0=f[x_0]$. By
induction $q_{k-1}$ interpolates $f$ at $x_0,\dots,x_{k-1}$, and the added term vanishes there, so $q_k$
does too. The coefficient of $x^k$ in $q_k$ is $f[x_0,\dots,x_k]$; by the Lagrange formula and the
explicit formula, the coefficient of $x^k$ in the interpolant $p_k$ is the same. Hence $q_k-p_k$ has
degree at most $k-1$ and vanishes at $x_0,\dots,x_{k-1}$, so it is zero and $q_k=p_k$. The hypotheses
used are that the nodes are distinct (so all denominators are nonzero) and that $f$ is defined at them.

**29.** *Strategy: represent $S''$ linearly on each panel, integrate twice, then impose continuity of
$S'$.*

Let $M_i=S''(x_i)$ and $h_i=x_{i+1}-x_i$. Since $S$ is cubic on $[x_i,x_{i+1}]$, $S''$ is linear there,
so $S''(x)=M_i(x_{i+1}-x)/h_i+M_{i+1}(x-x_i)/h_i$. Integrating twice and imposing the endpoint values
$S(x_i)=y_i$, $S(x_{i+1})=y_{i+1}$ gives the representation in Section 7.8 of the tutorial.

Differentiating it, the left derivative at $x_i$ (from the panel $[x_{i-1},x_i]$) is

$$S'(x_i^-)=\frac{h_{i-1}}{2}M_i+\frac{y_i-y_{i-1}}{h_{i-1}}-\frac{h_{i-1}}{6}(M_i-M_{i-1}),$$

and the right derivative at $x_i$ (from $[x_i,x_{i+1}]$) is

$$S'(x_i^+)=-\frac{h_i}{2}M_i+\frac{y_{i+1}-y_i}{h_i}-\frac{h_i}{6}(M_{i+1}-M_i).$$

Equating the two and collecting terms gives

$$\frac{h_{i-1}}{6}M_{i-1}+\frac{h_{i-1}+h_i}{3}M_i+\frac{h_i}{6}M_{i+1}
=\frac{y_{i+1}-y_i}{h_i}-\frac{y_i-y_{i-1}}{h_{i-1}} .$$

With the natural conditions $M_0=M_n=0$ this is an $(n-1)\times(n-1)$ tridiagonal system. In row $i$ the
diagonal entry is $(h_{i-1}+h_i)/3>0$ and the sum of the absolute off-diagonal entries is
$(h_{i-1}+h_i)/6$, strictly less. Hence the matrix is strictly diagonally dominant: if $Av=0$ and
$v_j$ is a component of maximal modulus, then
$\lvert a_{jj}\rvert\lvert v_j\rvert\le\sum_{k\ne j}\lvert a_{jk}\rvert\lvert v_k\rvert
\le\bigl(\sum_{k\ne j}\lvert a_{jk}\rvert\bigr)\lvert v_j\rvert<\lvert a_{jj}\rvert\lvert v_j\rvert$,
a contradiction unless $v=0$. So the system is nonsingular, the moments are uniquely determined, and
each cubic piece is fixed by its endpoint values and second derivatives.

**30.** *Strategy: two independent derivations, then a positive-definiteness argument for uniqueness.*

Write $\Phi(c)=\lVert Ac-b\rVert_2^2=(Ac-b)^{\mathsf T}(Ac-b)=c^{\mathsf T}A^{\mathsf T}Ac-2c^{\mathsf T}A^{\mathsf T}b+b^{\mathsf T}b$.
The gradient is $\nabla\Phi=2A^{\mathsf T}Ac-2A^{\mathsf T}b$ and the Hessian is $2A^{\mathsf T}A$,
positive semidefinite; hence $\Phi$ is convex and a stationary point is a global minimum. Setting the
gradient to zero gives $A^{\mathsf T}Ac=A^{\mathsf T}b$.

For the orthogonality route, let $r=b-Ac$ and consider $\Phi(c+sv)=\lVert r-sAv\rVert^2
=\lVert r\rVert^2-2s\langle r,Av\rangle+s^2\lVert Av\rVert^2$. If $c$ minimises, the derivative at
$s=0$ vanishes for every $v$, so $\langle r,Av\rangle=0$ for all $v$, that is $A^{\mathsf T}r=0$.
Conversely, if $A^{\mathsf T}r=0$ then $\lVert r-Av\rVert^2=\lVert r\rVert^2+\lVert Av\rVert^2\ge\lVert r\rVert^2$,
so $c$ is a global minimiser.

If the columns of $A$ are independent, $Av\ne0$ for $v\ne0$, so $v^{\mathsf T}A^{\mathsf T}Av=\lVert Av\rVert^2>0$
for $v\ne0$: $A^{\mathsf T}A$ is positive definite and invertible, the minimiser is unique and the
inequality above is strict for $v\ne0$. If the columns are dependent, some $v\ne0$ has $Av=0$, so adding
$v$ to $c$ does not change $Ac$ and the minimiser is not unique.

**31.** *Strategy: expand $\lVert f-q\rVert^2$ in the orthogonal basis and complete the square.*

Write $q=\sum_{k=0}^{n}d_kP_k$ (every element of $\Pi_n$ has such an expansion because the $P_k$ form a
basis). Then

$$\lVert f-q\rVert_2^2=\langle f,f\rangle-2\sum_kd_k\langle f,P_k\rangle+\sum_kd_k^2\langle P_k,P_k\rangle
=\lVert f\rVert_2^2+\sum_k\Bigl[(d_k-c_k)^2-c_k^2\Bigr]\langle P_k,P_k\rangle,$$

using $\langle f,P_k\rangle=c_k\langle P_k,P_k\rangle$. The only terms depending on $q$ are the squares
$(d_k-c_k)^2$, each non-negative and each vanishing exactly when $d_k=c_k$. Hence the minimum is
attained at $p^\ast$, uniquely because the coefficients of $q$ are uniquely determined, and the minimum
value is $\lVert f\rVert_2^2-\sum_kc_k^2\langle P_k,P_k\rangle$, which is the stated error formula.
Orthogonality of the error to $\Pi_n$ follows by setting $q=p^\ast+sv$ and differentiating at $s=0$.

## Challenge

**32.** *Strategy: run the experiment, tabulate, estimate growth factors, then interpret them through
the error formula and the pole location.*

Computing the maximum error on a grid of $20001$ points gives:

| $n$ | equispaced | Chebyshev | equispaced at $x=0.95$ |
|---|---|---|---|
| $4$ | $0.4384$ | $0.4020$ | $0.2020$ |
| $8$ | $1.0452$ | $0.1708$ | $0.9341$ |
| $12$ | $3.6634$ | $0.0692$ | $3.6567$ |
| $16$ | $14.3939$ | $0.0326$ | $12.687$ |

The equispaced error grows by factors $2.38$, $3.51$, $3.93$ as $n$ increases by $4$, approaching about
$4=2^2$: the growth is exponential, roughly doubling every two added nodes. The Chebyshev error decays
by factors $2.35$, $2.47$, $2.12$, about $2.3$ per four nodes, that is a factor $1.23$ per node —
precisely the Bernstein ellipse parameter $\rho=(1+\sqrt{26})/5=1.2198$ computed from the poles at
$\pm i/5$.

The error formula explains both. For this function $f^{(2k)}(0)=(-1)^k(2k)!25^k$, so
$\lVert f^{(n+1)}\rVert_\infty/(n+1)!$ grows like $5^{n+1}$. At equispaced nodes $\max\lvert\omega\rvert$
decays only like $2^{-n}$ times a slowly varying factor (values in Section 7.6), so the product grows
like $(5/2)^n$. At Chebyshev nodes $\lvert\omega\rvert$ is exponentially smaller near the endpoints, and
the analyticity of $f$ in the Bernstein ellipse converts the bound into the geometric rate $\rho^{-n}$.

**33.** *Strategy: reduce $Nx_j$ modulo $2\pi$ and use the addition formulas.*

Since $Nx_j=2\pi j$, we have $(N-k)x_j=2\pi j-kx_j$. Therefore
$\cos((N-k)x_j)=\cos(2\pi j-kx_j)=\cos(kx_j)$ and
$\sin((N-k)x_j)=\sin(2\pi j-kx_j)=-\sin(kx_j)$, using $\cos(2\pi j-\theta)=\cos\theta$ and
$\sin(2\pi j-\theta)=-\sin\theta$.

Consequently the samples of $e^{i(N-k)x}$ and $e^{-ikx}$ coincide on the grid, so the frequency $N-k$
carries exactly the same information as $-k$. Any real trigonometric polynomial can be written

$$p(x)=a_0+\sum_{k=1}^{m}\bigl(a_k\cos kx+b_k\sin kx\bigr)+a_{N/2}\cos(\tfrac N2x)$$

when $N=2m$; this has $1+2(m-1)+1=N$ real coefficients. Frequency $N/2$ is its own alias (the Nyquist
term), and every frequency above $N/2$ aliases onto one below it. Hence $N$ samples can determine at
most $N$ independent real coefficients — those of degree at most $N/2$ — and higher frequencies are
indistinguishable from lower ones, which is why they cannot be recovered from the samples.

**34.** *Strategy: for the minimax part, bound the error at three points; for the $L^2$ part, compute the
Legendre coefficients.*

Let $q(x)=ax+b$ and let $E=\max_{[-1,1]}\lvert\lvert x\rvert-q(x)\rvert$. At $x=0$, $E\ge\lvert b\rvert$.
At $x=1$, $E\ge\lvert1-a-b\rvert$; at $x=-1$, $E\ge\lvert1+a-b\rvert$. If $\lvert b\rvert\ge\tfrac12$
then $E\ge\tfrac12$. Otherwise $b<\tfrac12$, so $1-b>\tfrac12$, and
$\max(\lvert1-b-a\rvert,\lvert1-b+a\rvert)\ge1-b>\tfrac12$ because one of $\pm a$ is non-negative.
Hence $E\ge\tfrac12$ for every line. The constant $q=\tfrac12$ gives
$\lvert\lvert x\rvert-\tfrac12\rvert\le\tfrac12$ on $[-1,1]$ with equality at $x=0,\pm1$, so it is
optimal and the minimax error is $\tfrac12$.

For $L^2$, $c_0=\tfrac12\int_{-1}^1\lvert x\rvert dx=\tfrac12$ and
$c_1=\tfrac32\int_{-1}^1x\lvert x\rvert dx=0$ (odd integrand), so the best linear approximation is again
$\tfrac12$. Its squared error is $\int_{-1}^1(\lvert x\rvert-\tfrac12)^2dx=2\int_0^1(x-\tfrac12)^2dx
=2\cdot\tfrac1{12}=\tfrac16$. In this example the minimax and least-squares answers coincide, which is
not typical; for $\lvert x\rvert$ approximated by higher-degree polynomials they differ.

**35.** *Strategy: factor $\omega$ out of each Lagrange basis, then divide by the partition of unity.*

Since $\ell_i(x)=\prod_{j\ne i}\frac{x-x_j}{x_i-x_j}=\omega(x)\frac{w_i}{x-x_i}$ with
$w_i=1/\prod_{j\ne i}(x_i-x_j)$, the Lagrange formula reads
$p(x)=\omega(x)\sum_i\frac{w_iy_i}{x-x_i}$. Applying the same identity to the constant function with
data $y_i=1$ gives $1=\omega(x)\sum_i\frac{w_i}{x-x_i}$. Dividing,

$$p(x)=\frac{\sum_i\dfrac{w_i}{x-x_i}y_i}{\sum_i\dfrac{w_i}{x-x_i}} .$$

For nodes $0,1,2,3$:
$w_0=1/\bigl((-1)(-2)(-3)\bigr)=-\tfrac16$,
$w_1=1/\bigl((1)(-1)(-2)\bigr)=\tfrac12$,
$w_2=1/\bigl((2)(1)(-1)\bigr)=-\tfrac12$,
$w_3=1/\bigl((3)(2)(1)\bigr)=\tfrac16$.

With data $(0,1,4,9)$ and $x=1.5$, the numerators are
$0$, $\tfrac12\cdot1/0.5=1$, $-\tfrac12\cdot4/(-0.5)=4$, $\tfrac16\cdot9/(-1.5)=-1$, summing to $4$.
The denominators are $-\tfrac16/1.5=-\tfrac19$, $\tfrac12/0.5=1$, $-\tfrac12/(-0.5)=1$,
$\tfrac16/(-1.5)=-\tfrac19$, summing to $\tfrac{16}{9}$. The ratio is $4/(16/9)=2.25$, which is
$1.5^2$, as expected for data from $x^2$.

The formula is stable because it evaluates a convex-type combination of the data: the denominator is
$\sum_i w_i/(x-x_i)$, and each term is computed from differences of nearby numbers rather than from
large alternating monomial coefficients. Expanding the polynomial in powers of $x$ requires coefficients
that may be enormous and that cancel catastrophically; the barycentric form never forms them.

**36.** *Strategy: compare the interpolant of $f$ with $f$ itself, and read off the leading coefficient
from the Newton form.*

Let $f$ be a polynomial of degree $n$ with leading coefficient $a_n$, and let $x_0,\dots,x_n$ be distinct.
The interpolant $p_n\in\Pi_n$ agrees with $f$ at $n+1$ points; $f-p_n$ has degree at most $n$ and $n+1$
roots, so $f=p_n$. By the Lagrange formula the coefficient of $x^n$ in $p_n$ is
$\sum_if(x_i)/\prod_{j\ne i}(x_i-x_j)$, which by Proposition 7.2 equals $f[x_0,\dots,x_n]$. Hence
$f[x_0,\dots,x_n]=a_n$.

For order $n+1$, add a further distinct node $x_{n+1}$ and interpolate at all $n+2$ points. The Newton
coefficient of $\prod_{j=0}^{n}(x-x_j)$ is $f[x_0,\dots,x_{n+1}]$, and since $f=p_n$ has degree $n$, that
coefficient must be zero: every divided difference of order $n+1$ of a degree-$n$ polynomial vanishes.
(Equivalently, the $(n+1)$-st difference is the divided difference of the zero function.)

For a cubic $f$ and five distinct nodes, the fourth divided difference is therefore zero, so the Newton
form has no $x^4$ term and the interpolant is the cubic itself. If the five data do not lie on a cubic,
the fourth divided difference is nonzero and measures exactly the coefficient of $x^4$ needed to pass
through the fifth point; that coefficient is the discrete analogue of $f^{(4)}/4!$.
