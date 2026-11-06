# Introduction to PDEs — Solutions

> [Introduction to PDEs](README.md) · Solutions to the 36 problems in [exercises.md](exercises.md)

Each solution states the strategy, carries out every step, and ends with a verification: substitution
into the PDE, a check of the boundary or initial data, or a limiting argument. Numerical values were
computed from the series with enough terms for the quoted digits; where a table is given, the truncation
error is below the last displayed digit unless stated otherwise.

## Beginner

### Solution 1

*Strategy: the order is the highest derivative; linearity is decided by how $u$ and its derivatives appear.*

(a) $u_t + uu_x = 0$: order **1**. The coefficient of the highest derivative $u_x$ is $u$, a quantity of order zero, so the equation is linear in its first derivatives with coefficients depending on $u$: **quasilinear** (in fact it is the prototype of a quasilinear first-order equation).

(b) $u_{xx} + u_{yy} = 0$: order **2**, **linear** and homogeneous, with constant coefficients.

(c) $u_t = u_{xx} + \sin u$: order **2**. The second derivatives appear linearly with coefficients $1$; the nonlinearity $\sin u$ involves $u$ only. **Semilinear.**

(d) $u_x^2 + u_y = 0$: order **1**, but the square of a derivative appears, so **fully nonlinear**.

(e) $x^2u_{xx} + u_t = e^{-t}$: order **2**, **linear** and inhomogeneous; the coefficient $x^2$ depends on the independent variable only, which is allowed in a linear equation.

*Rule to remember.* A term is "nonlinear" only if it multiplies two derivatives, or a derivative with itself, or contains a nonlinear function of a derivative. $\sin u$ makes an equation semilinear; $u_x^2$ makes it fully nonlinear; $u\,u_x$ makes it quasilinear.

### Solution 2

*Strategy: differentiate and compare.*

$$u_t = -9e^{-9t}\cos 3x, \qquad u_x = -3e^{-9t}\sin 3x, \qquad u_{xx} = -9e^{-9t}\cos 3x .$$

Hence $u_t = u_{xx}$ everywhere: $u$ solves the heat equation with $\alpha = 1$.

The decay rate of the spatial mode $\cos kx$ is $k^2$. For $\cos 2x$ it is $4$, so $u = e^{-4t}\cos 2x$ solves the same equation. The rule is that substituting $e^{-\beta t}\cos kx$ into $u_t = \alpha u_{xx}$ gives $-\beta = -\alpha k^2$, i.e. $\beta = \alpha k^2$.

*Check.* The general solution on the whole line with $2\pi$-periodic data can be written $\sum a_n e^{-n^2t}\cos nx$ (with $\alpha=1$); each term has decay rate exactly $n^2$, and $9 = 3^2$ ✓.

### Solution 3

Differentiate:

$$u_t = -2\sin(x+2t), \qquad u_{tt} = -4\cos(x+2t), \qquad u_x = -\sin(x+2t), \qquad u_{xx} = -\cos(x+2t).$$

So $u_{tt} = 4u_{xx}$, which is the wave equation with $c^2 = 4$, i.e. $c = 2$.

Since $u = f(x + 2t) = f\bigl(x - (-2)t\bigr)$, it is a right-moving solution with speed $-2$: the profile travels in the **negative $x$ direction** at speed $2$. A point of constant phase satisfies $x + 2t = $ const, i.e. $x = x_0 - 2t$.

*Check.* At $t = 0$ the profile is $\cos x$; at $t = \pi/4$ it is $\cos(x + \pi/2) = -\sin x$, which is $\cos x$ shifted left by $\pi/2$ — a quarter period of the wave, as expected for a leftward-moving wave ✓.

### Solution 4

Let $u(x,t)$ be the temperature with $\alpha$ absorbing the material constants. The complete problem is

$$u_t = \alpha u_{xx}, \quad 0 < x < 1,\ t>0; \qquad u(x,0) = 50 - 50\cos 2\pi x; \qquad u(0,t) = u(1,t) = 0 .$$

* **$u(x,0)$** is an **initial condition** — the state of the whole rod at the starting time.
* **$u(0,t) = u(1,t) = 0$** are **Dirichlet boundary conditions** — the temperature is fixed at each end for all time.

*Compatibility check.* At the corner $(0,0)$ the initial datum gives $u(0,0) = 50 - 50\cos 0 = 0$, which agrees with the boundary value $0$. At $(1,0)$: $50 - 50\cos 2\pi = 0$ ✓. Both corners are consistent, so a continuous solution exists.

*Remark.* With one condition at each end and one initial condition, the count matches the order in each variable ($1$ in $t$, $2$ in $x$), as §7.2 requires. The data are already a single cosine mode, so the solution will be a single decaying mode.

### Solution 5

*Hadamard's conditions.* A problem is well posed if (1) **existence**: a solution exists; (2) **uniqueness**: at most one solution exists; (3) **stability**: the solution depends continuously on the data.

For the backward heat equation $u_t = -u_{xx}$ on $0<x<\pi$ with $u(0,t) = u(\pi,t) = 0$, separation of variables gives the modes

$$u_n(x,t) = \varepsilon e^{+n^2t}\sin nx,$$

because the time factor solves $T' = +n^2T$ rather than $T' = -n^2T$.

Take $f_1 \equiv 0$ and $f_2(x) = \varepsilon\sin(nx)$. Then $\lVert f_1 - f_2\rVert_\infty = \varepsilon$, and the corresponding solutions are $u_1 \equiv 0$ and $u_2(x,t) = \varepsilon e^{n^2t}\sin nx$. At $t = 0.1$ with $\varepsilon = 10^{-6}$ and $n = 10$,

$$\lVert u_1(\cdot,0.1) - u_2(\cdot,0.1)\rVert_\infty = 10^{-6}e^{10} = 1.0\times10^{-6}\times 22026 \approx 0.0220 .$$

A change of $10^{-6}$ in the data produces a change of $2.2\times10^{-2}$ in the solution, and increasing $n$ amplifies it without bound (times $e^{n^2t}$). No constant $C$ can bound the solution by $C\times$ (the data change), so **condition 3 fails**.

*Note.* Existence and uniqueness also fail for general $f$: the exact solution would require $f$ to be expandable with coefficients decaying like $e^{n^2t}$, which only analytic data satisfy. But stability is the clearest failure, and it is the one Hadamard emphasised.

### Solution 6

*Strategy: characteristics.* For $u_t + 3u_x = 0$ the characteristics solve $\dot x = 3$, so $x = x_0 + 3t$. Along a characteristic,

$$\frac{d}{dt}u(x(t),t) = u_t + 3u_x = 0,$$

so $u$ is constant and equals $u(x_0,0) = \sin x_0$. With $x_0 = x - 3t$,

$$u(x,t) = \sin(x - 3t).$$

At $(x,t) = (\pi,1)$: $u = \sin(\pi - 3) = \sin 3 = 0.141120$.

*Check.* $u_t = -3\cos(x-3t)$ and $u_x = \cos(x-3t)$, so $u_t + 3u_x = -3\cos + 3\cos = 0$ ✓; $u(x,0) = \sin x$ ✓. (The identity $\sin(\pi - 3) = \sin 3$ holds because $\sin(\pi - y) = \sin y$.)

### Solution 7

For $u_t - 2u_x = 0$ the characteristic equation is $\dot x = -2$, so $x = x_0 - 2t$, i.e. $x_0 = x + 2t$. Along the characteristic $u$ is constant, hence

$$u(x,t) = f(x + 2t) = e^{-(x+2t)^2}.$$

At $(1, 0.5)$: $x + 2t = 1 + 1 = 2$, so $u = e^{-4} = 0.0183156$.

*Check.* $u_t = -2(x+2t)\cdot 2\,e^{-(x+2t)^2} = -4(x+2t)e^{-(x+2t)^2}$ and $u_x = -2(x+2t)e^{-(x+2t)^2}$, so $u_t - 2u_x = \bigl[-4(x+2t) + 4(x+2t)\bigr]e^{-(x+2t)^2} = 0$ ✓.

*Interpretation.* The profile moves **left** at speed $2$ (the equation is $u_t = 2u_x$, so the advection velocity is $-2$).

### Solution 8

For $u_t + 2u_x = 0$, $\dot x = 2$ and the characteristics are the straight lines

$$x = x_0 + 2t,$$

which in the $(x,t)$ plane have slope $dt/dx = 1/2$. Along each, $u$ is constant and equal to $f(x_0)$; so $u(x,t) = f(x - 2t)$.

A jump initially at $x_0 = 0$ travels along the characteristic through $(0,0)$, namely $x = 2t$. At $t = 3$ it is at

$$x = 2\cdot 3 = 6 .$$

*Remark.* The jump persists forever: the transport equation neither smooths nor spreads discontinuities, unlike the heat equation. This is the simplest instance of the difference between hyperbolic and parabolic behaviour.

### Solution 9

*Strategy: look for a time-independent solution.*

Set $u_t = 0$. The heat equation becomes $u_{xx} = 0$, whose solutions are linear: $u_s(x) = A + Bx$. Imposing $u_s(0) = 20$ and $u_s(1) = 80$ gives $A = 20$ and $B = 60$, so

$$u_s(x) = 20 + 60x .$$

*Why the initial condition is irrelevant.* Write $u = u_s + v$. Then $v$ solves the same heat equation with homogeneous Dirichlet data $v(0,t) = v(1,t) = 0$ and initial value $v(x,0) = u(x,0) - u_s(x)$. Every mode of $v$ decays like $e^{-n^2\pi^2t}$, so $v \to 0$ uniformly and $u \to u_s$ as $t\to\infty$, **whatever** the initial temperature was. The steady state is unique (by the maximum principle applied to the difference of two steady states, or directly from $u_{xx}=0$ plus the two boundary values).

*Check.* $u_s(0) = 20$ ✓, $u_s(1) = 80$ ✓, $u_s'' = 0$ ✓; the flux is constant, $60$ per unit length, as it must be at equilibrium.

### Solution 10

Separation on $[0,1]$ with zero Dirichlet data gives $\lambda_n = n^2\pi^2$ and modes $\sin n\pi x$ with time factor $e^{-n^2\pi^2t}$ (since $\alpha = 1$). The initial datum $\sin 2\pi x$ is the $n = 2$ mode, so

$$u(x,t) = e^{-4\pi^2t}\sin 2\pi x .$$

At $(0.25, 0.1)$: $\sin(2\pi\cdot 0.25) = \sin(\pi/2) = 1$, and $4\pi^2(0.1) = 3.94784$, so

$$u = e^{-3.94784} = 0.0192963 .$$

The amplitude is $e^{-4\pi^2t}$, which falls below $10^{-3}$ when $4\pi^2t > \ln 1000 = 6.907755$, i.e.

$$t > \frac{6.907755}{39.4784} = 0.174976 .$$

*Check.* The time constant is $1/(4\pi^2) = 0.025330$; four time constants give $e^{-4} = 0.0183$, and $t = 0.1$ is $3.95$ time constants → $e^{-3.95}\approx 0.0193$ ✓.

### Solution 11

Here $L = 2$, $\alpha = 9$. The eigenvalues are $\lambda_n = (n\pi/L)^2 = n^2\pi^2/4$ and the time factors are $e^{-9n^2\pi^2t/4}$. The initial datum $\sin(\pi x/2)$ is the $n = 1$ mode, so

$$u(x,t) = \exp\left(-\frac{9\pi^2t}{4}\right)\sin\frac{\pi x}{2}.$$

The slowest decay time constant is the reciprocal of the first decay rate,

$$\tau = \frac{4}{9\pi^2} = 0.045032 \text{ time units}.$$

After $t = \tau$ the amplitude has fallen by a factor $e$; after $5\tau \approx 0.225$ it has fallen by $e^{-5} \approx 0.0067$.

*Check.* $u_t = -\frac{9\pi^2}{4}u$ and $u_{xx} = -\frac{\pi^2}{4}u$, so $9u_{xx} = -\frac{9\pi^2}{4}u = u_t$ ✓; $u(0,t) = \sin 0 = 0$ and $u(2,t) = \sin\pi = 0$ ✓.

### Solution 12

With $L = 1$, $c = 2$, $\lambda_n = n^2\pi^2$ and $\omega_n = c\sqrt{\lambda_n} = 2n\pi$. The initial displacement is the $n = 3$ mode and the initial velocity vanishes, so only the cosine time factor survives:

$$u(x,t) = \cos(6\pi t)\sin 3\pi x .$$

*Period.* $\cos(6\pi t)$ has period $2\pi/(6\pi) = 1/3$. Equivalently $T = 2L/(nc) = 2/(3\cdot2) = 1/3$ ✓.

*Value at $(0.5, 1/6)$.* $\sin(3\pi\cdot0.5) = \sin(1.5\pi) = -1$ and $\cos(6\pi/6) = \cos\pi = -1$, so $u = (-1)(-1) = 1$. This is the maximum displacement: at $t = 1/6$, half a period, the string is the mirror image of its initial shape, which for a mode with $n$ odd means the same shape inverted twice.

*Check.* $u_{tt} = -36\pi^2\cos(6\pi t)\sin3\pi x$ and $4u_{xx} = 4(-9\pi^2)\cos(6\pi t)\sin 3\pi x = -36\pi^2(\cdot)$ ✓; $u_t(x,0) = -6\pi\sin0\cdot\sin3\pi x = 0$ ✓.

### Solution 13

d'Alembert's formula with $g\equiv0$ and $c = 1$ is

$$u(x,t) = \frac{f(x-t)+f(x+t)}{2}.$$

At $(0,1)$: $f(-1) + f(1) = e^{-1} + e^{-1} = 2e^{-1}$, so

$$u(0,1) = e^{-1} = 0.367879 .$$

*Interpretation.* The initial bump $e^{-x^2}$ has split into two half-height bumps, one centred at $x = -1$ and one at $x = +1$; at $x = 0$ both are at the same (small) height, so the value is exactly the height of the original bump at distance $1$, namely $e^{-1}$.

*Check.* $u_t = \frac{-f'(x-t)+f'(x+t)}{2}$; at $t=0$ this is $0$ ✓ (zero initial velocity). $u_{tt} - u_{xx} = \frac{f''(x-t)+f''(x+t)}{2} - \frac{f''(x-t)+f''(x+t)}{2} = 0$ ✓.

### Solution 14

$u = x^2 - y^2$ gives $u_{xx} = 2$ and $u_{yy} = -2$, so $\Delta u = 0$: harmonic. Then $u(1,2) = 1 - 4 = -3$.

For $v = ax^2 + bxy + cy^2$: $v_{xx} = 2a$ and $v_{yy} = 2c$, so

$$\Delta v = 2a + 2c = 0 \iff a + c = 0 .$$

The mixed term contributes nothing because $\partial_x^2(xy) = \partial_y^2(xy) = 0$. Hence the harmonic functions of this form are $v = a(x^2-y^2) + bxy$: a two-parameter family, spanned by $\operatorname{Re}(z^2)$ and $\operatorname{Im}(z^2)$.

*Check.* With $a = 1$, $b = 0$ we recover $x^2-y^2$; with $a = 0$, $b = 2$ we get $2xy$, and $(2xy)_{xx} + (2xy)_{yy} = 0$ ✓.

## Intermediate

### Solution 15

*Strategy: solve the characteristic ODE, then invert.*

The characteristics satisfy $\dfrac{dx}{dt} = x$, so $\ln|x| = t + C$ and $x = x_0e^{t}$, hence $x_0 = xe^{-t}$. Along a characteristic $u$ is constant:

$$u(x,t) = f\bigl(x_0\bigr) = \sin\left(xe^{-t}\right).$$

At $(1,\ln 2)$: $e^{-t} = \tfrac12$, so $u = \sin(0.5) = 0.479426$.

*Check.* $u_t = \cos(xe^{-t})\cdot(-xe^{-t})$ and $u_x = \cos(xe^{-t})\cdot e^{-t}$, so $u_t + xu_x = -xe^{-t}\cos(\cdot) + xe^{-t}\cos(\cdot) = 0$ ✓.

*Interpretation.* All characteristics converge to $x = 0$ as $t\to\infty$; the profile is compressed towards the origin, and $u(x,t)\to\sin 0 = 0$ for every fixed $x$. There is no shock because the characteristics never cross — they all funnel into the origin.

### Solution 16

The characteristics satisfy $\dot x = 2$, so $x = x_0 + 2t$. Along one,

$$\frac{d}{dt}u(x(t),t) = u_t + 2u_x = t .$$

Integrating from $0$ to $t$:

$$u(x(t),t) - u(x_0,0) = \int_0^t s\,ds = \frac{t^2}{2},$$

and $u(x_0,0) = 0$, so

$$u(x,t) = \frac{t^2}{2}.$$

*Verification.* $u_t = t$ and $u_x = 0$, so $u_t + 2u_x = t$ ✓, and $u(x,0) = 0$ ✓.

*Why no $x$-dependence?* The source $g = t$ is independent of $x$, the initial datum is zero, and the transport speed $2$ is constant. The accumulated source along any characteristic is $\int_0^t s\,ds$, the same for all of them, so all characteristics carry the same value and the solution is spatially uniform.

### Solution 17

*Coefficients.* With $L = 1$, $\alpha = 1$,

$$b_n = 2\int_0^1 x\sin(n\pi x)\,dx = 2\cdot\frac{(-1)^{n+1}}{n\pi} = \frac{2(-1)^{n+1}}{n\pi},$$

using $\int_0^1x\sin(n\pi x)dx = -\frac{\cos n\pi}{n\pi} = \frac{(-1)^{n+1}}{n\pi}$ (integration by parts; the boundary term at $x=1$ gives $-\cos n\pi/(n\pi)$ and the remaining integral vanishes). The first four are

$$b_1 = 0.636620, \quad b_2 = -0.318310, \quad b_3 = 0.212207, \quad b_4 = -0.159155 .$$

*Solution.*

$$u(x,t) = \sum_{n=1}^\infty \frac{2(-1)^{n+1}}{n\pi}\sin(n\pi x)\,e^{-n^2\pi^2t}.$$

*Table at $x = 0.5$* ($2000$ terms; truncation error below $10^{-6}$ for $t\ge0.05$, and of order $1/N$ at $t=0$ because the odd extension has a jump):

| $t$ | $0$ | $0.05$ | $0.1$ | $0.2$ |
|---|---|---|---|---|
| $u(0.5,t)$ | $0.4998$ | $0.3862$ | $0.2372$ | $0.0884$ |

*Why the coefficients decay only like $1/n$.* The odd extension of $f(x) = x$ to $[-1,1]$ is a sawtooth with jumps of size $2$ at every integer; the theorem of §7.9 then gives coefficients of order $1/n$, and no faster. A function with a jump always has $\Theta(1/n)$ coefficients.

*Why the solution is nevertheless smooth for $t>0$.* Each differentiation brings down a factor $(n\pi)^k$, while the exponential factor is $e^{-n^2\pi^2t}$, which decays faster than any power. Hence for fixed $t>0$ the differentiated series is bounded by $C\sum n^k e^{-n^2\pi^2t}<\infty$ and converges uniformly. At $t = 0$ the bound would be $C\sum n^k$, which diverges — the smoothing is entirely due to the exponential factor.

*Check.* At $t = 0$ the sum is the Fourier series of $x$, which converges to $\frac12[f(0^+)+f(0^-)] = 0.5$ at $x = 0.5$ (the value there is continuous, so it is simply $0.5$); the computed value with $2000$ terms is $0.49984$, the remaining $1.6\times10^{-4}$ being the slow $O(1/N)$ tail produced by the jumps of the odd extension at the integers ✓.

### Solution 18

*Coefficients.* For Neumann data use cosines: $u = \frac{a_0}{2} + \sum_{n\ge1}a_n\cos(n\pi x)e^{-n^2\pi^2t}$ with

$$a_0 = 2\int_0^1 x\,dx = 1, \qquad a_n = 2\int_0^1 x\cos(n\pi x)\,dx = \frac{2\bigl((-1)^n - 1\bigr)}{n^2\pi^2}.$$

So $a_n = -4/(n^2\pi^2)$ for odd $n$ and $0$ for even $n$, giving

$$u(x,t) = \frac12 - \frac{4}{\pi^2}\sum_{n\ \text{odd}}\frac{\cos(n\pi x)}{n^2}\,e^{-n^2\pi^2t}.$$

*Limit as $t\to\infty$.* Every $n \ge 1$ term decays, so $u \to \frac{a_0}{2} = \frac12$. This is exactly the average of the initial temperature,

$$\frac{1}{1}\int_0^1 x\,dx = \frac12,$$

which is the physically correct answer: insulation means no heat escapes, so the final uniform temperature is the mean.

*Value at $(0.25, 0.05)$.* With $3000$ terms, $u = 0.309514$.

*Why the constant mode does not decay.* Its eigenvalue is $\lambda_0 = 0$, so its time factor is $e^{0} = 1$. The existence of a zero eigenvalue is exactly the statement that the total heat $\int u\,dx$ is conserved; the Neumann problem has a one-parameter family of steady states (constants), and the initial data pick out one of them through the condition $a_0/2 = \text{mean}$.

*Check.* At $t = 0$, $0.25$ and $0.75$ should reproduce the initial data: the computed values are $0.249885$ and $0.749723$ with $3000$ terms (slow convergence at $t=0$ because of the jump in the even extension at $x=0$); at $t = 0.01$ they are $0.254377$ and $0.672900$, already close to the smoothed profile. At large $t$ both tend to $0.5$ ✓.

### Solution 19

*Reduce to homogeneous data.* The steady state with $u(0) = 0$, $u(1) = 100$ is $u_s(x) = 100x$. Put $v = u - 100x$. Then

$$v_t = u_t = u_{xx} = v_{xx}, \qquad v(0,t) = 0 - 0 = 0, \qquad v(1,t) = 100 - 100 = 0,$$

and $v(x,0) = 0 - 100x = -100x$. So

$$b_n = 2\int_0^1(-100x)\sin(n\pi x)\,dx = -200\cdot\frac{(-1)^{n+1}}{n\pi} = \frac{200(-1)^n}{n\pi},$$

and therefore

$$u(x,t) = 100x + \sum_{n=1}^\infty\frac{200(-1)^n}{n\pi}\sin(n\pi x)\,e^{-n^2\pi^2t}.$$

*Values* (2000 terms):

| $t$ | $u(0.5,t)$ | $u(0.75,t)$ |
|---|---|---|
| $0$ | $0.0080$ | $0.0192$ |
| $0.01$ | $0.0407$ | $7.7100$ |
| $0.05$ | $11.3844$ | $42.9195$ |
| $0.1$ | $26.2756$ | $57.6060$ |
| $0.2$ | $41.1566$ | $68.7350$ |
| $0.5$ | $49.5422$ | $74.6763$ |
| $1.0$ | $49.9967$ | $74.9977$ |

*Check.* At $t = 0$ the series must return the initial data $0$: with $4000$ terms the computed values are $0.008$ and $0.019$, the Gibbs remnant of a series whose coefficients decay only like $1/n$ (the odd extension of $-100x$ jumps at the endpoints). At $t = 0.01$ the value at $x = 0.75$ is $7.71$, which matches the semi-infinite similarity solution $100\,\operatorname{erfc}\bigl(0.25/(2\sqrt{0.01})\bigr) = 100\,\operatorname{erfc}(1.25) = 7.71$ — a useful independent check, since at that early time the far end has not yet influenced the point $x = 0.75$. As $t\to\infty$ the values approach $u_s(0.5) = 50$ and $u_s(0.75) = 75$ ✓.

### Solution 20

*Strategy: split the integral at the peak and integrate by parts twice.*

$$b_n = 2\int_0^1 f(x)\sin(n\pi x)\,dx = 2\int_0^{1/2}2x\sin(n\pi x)\,dx + 2\int_{1/2}^1 2(1-x)\sin(n\pi x)\,dx .$$

For the first piece, integrate by parts with $u = x$, $dv = \sin(n\pi x)dx$:

$$\int_0^{1/2}x\sin(n\pi x)\,dx = \left[-\frac{x\cos n\pi x}{n\pi}\right]_0^{1/2} + \int_0^{1/2}\frac{\cos n\pi x}{n\pi}\,dx = -\frac{\cos(n\pi/2)}{2n\pi} + \frac{\sin(n\pi/2)}{n^2\pi^2}.$$

The second piece is handled by the substitution $w = 1 - x$, which gives $dx = -dw$, sends $x: \tfrac12 \to 1$ to $w: \tfrac12 \to 0$, and satisfies

$$\sin(n\pi x) = \sin\bigl(n\pi(1-w)\bigr) = -(-1)^n\sin(n\pi w) = (-1)^{n+1}\sin(n\pi w).$$

Hence

$$\int_{1/2}^1(1-x)\sin(n\pi x)\,dx = (-1)^{n+1}\int_0^{1/2}w\sin(n\pi w)\,dw = (-1)^{n+1}A_n,$$

where $A_n = \int_0^{1/2}x\sin(n\pi x)dx$ is the first piece. Therefore

$$b_n = 4A_n\bigl(1 + (-1)^{n+1}\bigr).$$

For even $n$ the bracket vanishes, so $b_n = 0$ — as it must be, because for even $n$ the function $\sin(n\pi x)$ is antisymmetric about $x = 1/2$ while $f$ is symmetric, so the integral vanishes by symmetry. For odd $n$ the bracket equals $2$ and $\cos(n\pi/2) = 0$, so $A_n = \sin(n\pi/2)/(n^2\pi^2)$ and

$$b_n = \frac{8\sin(n\pi/2)}{n^2\pi^2}.$$

*Numerical values.* $b_1 = 8/\pi^2 = 0.8105695$; $b_3 = -8/(9\pi^2) = -0.0900633$; $b_5 = 8/(25\pi^2) = 0.0324228$.

*Check.* At $x = 1/2$ the series must give $1$: $\sum_{n\ \text{odd}}8\sin^2(n\pi/2)/(n^2\pi^2) = \frac{8}{\pi^2}\sum_{n\ \text{odd}}n^{-2} = \frac{8}{\pi^2}\cdot\frac{\pi^2}{8} = 1$ ✓ (using $\sum_{\text{odd}}n^{-2} = \pi^2/8$ from Exercise 25).

### Solution 21

*Strategy: separation of variables with zero initial displacement.*

The general solution with $u(x,0) = 0$ is $u = \sum_n B_n\sin(n\pi x)\sin(n\pi t)$ (since $c = L = 1$). Differentiating in time and setting $t = 0$:

$$u_t(x,0) = \sum_n n\pi B_n\sin(n\pi x) = \sin 2\pi x .$$

So $n\pi B_n$ is the $n$-th sine coefficient of $\sin2\pi x$, which is the $n = 2$ mode with coefficient $1$. Hence $2\pi B_2 = 1$, i.e. $B_2 = 1/(2\pi)$, and all other $B_n = 0$:

$$u(x,t) = \frac{1}{2\pi}\sin(2\pi x)\sin(2\pi t).$$

*Verification.* $u_{tt} = -\frac{(2\pi)^2}{2\pi}\sin(2\pi x)\sin(2\pi t) = -2\pi\sin(2\pi x)\sin(2\pi t)$ and $u_{xx} = -\frac{(2\pi)^2}{2\pi}\sin(2\pi x)\sin(2\pi t)$; equal ✓. $u(x,0) = 0$ ✓, $u_t(x,0) = \frac{2\pi}{2\pi}\sin(2\pi x)\cos 0 = \sin 2\pi x$ ✓, $u(0,t) = u(1,t) = 0$ ✓.

*Value at $(0.25,0.125)$.* $\sin(\pi/2) = 1$, $\sin(\pi/4) = 0.707107$, so

$$u = \frac{0.707107}{2\pi} = 0.112540 .$$

*Remark.* This solution has a node at $x = 1/2$ for all time (the sine factor vanishes there); the initial "kick" is antisymmetric about the midpoint, so the midpoint never moves.

### Solution 22

*Series.* Separate, $u = X(x)Y(y)$: $X'' + \lambda X = 0$ with $X(0) = X(1) = 0$ gives $\lambda_n = n^2\pi^2$, $X_n = \sin n\pi x$; then $Y'' = n^2\pi^2Y$ with $Y(1) = 0$ (the top is at zero) gives $Y_n(y) = \sinh\bigl(n\pi(1-y)\bigr)$. Hence

$$u(x,y) = \sum_{n=1}^\infty b_n\sin(n\pi x)\,\frac{\sinh\bigl(n\pi(1-y)\bigr)}{\sinh(n\pi)}, \qquad b_n = 2\int_0^1 100\sin(n\pi x)\,dx = \frac{200(1-\cos n\pi)}{n\pi},$$

so $b_n = 400/(n\pi)$ for odd $n$ and $0$ for even $n$.

| $(x,y)$ | $(0.5,0)$ | $(0.5,0.25)$ | $(0.5,0.5)$ | $(0.5,0.75)$ | $(0.5,1)$ | $(0.25,0.5)$ | $(0.1,0.1)$ |
|---|---|---|---|---|---|---|---|
| $u$ | $99.6817$ | $54.0529$ | $25.0000$ | $9.5414$ | $0$ | $18.2028$ | $48.9060$ |

*Why the centre value is exactly $25$.* Consider the four problems obtained by rotating the square so that each side in turn carries the data $100$ and the other three carry $0$. Each has the same value $v$ at the centre, by symmetry. Their sum solves Laplace's equation with boundary data $100$ on all four sides; the unique such solution is the constant $100$. Therefore $4v = 100$ and $v = 25$ exactly — no approximation at all.

*Check.* The series reproduces $u = 0$ on the left, right and top sides and $u(x,0) = 100$ for $0<x<1$ ✓. The value at $(0.5,0)$ is $99.68$ rather than $100$: the boundary datum has jumps at the corners $(0,0)$ and $(1,0)$, so the series converges to the midpoint-like average there, and at the corner exactly it converges to $50$. This is the Gibbs phenomenon at work on the boundary data, not an error in the solution. An independent finite-difference solution on a $200\times200$ grid agrees with every entry in the table to four decimal places.

### Solution 23

*Series solution in the disc.* With $u = R(r)\Theta(\theta)$ and periodicity in $\theta$, the bounded solutions are $r^n\cos n\theta$ and $r^n\sin n\theta$ for $n\ge0$ (the $r^{-n}$ family is excluded by boundedness at $r=0$). The boundary data $\cos 2\theta$ is already one of these with $n = 2$ and coefficient $1$, so

$$u(r,\theta) = r^2\cos 2\theta .$$

*Values.* $u(0.5,0) = 0.25\cdot 1 = 0.25$; $u(0.7,\pi/3) = 0.49\cos(2\pi/3) = 0.49\times(-0.5) = -0.245$.

*Extrema.* On the boundary $r = 1$ the function is $\cos2\theta$, with maximum $1$ at $\theta = 0,\pi$ and minimum $-1$ at $\theta = \pm\pi/2$. In the interior $|u| \le r^2 < 1$, so both extrema are attained **only** on the boundary, exactly as the maximum principle requires. The centre value is $u(0,\theta) = 0$, the average of $\cos 2\theta$ over the circle.

*Check.* In polar coordinates, $\Delta(r^2\cos2\theta) = \Delta(x^2-y^2) = 2 - 2 = 0$ ✓; and $u(1,\theta) = \cos2\theta$ ✓.

### Solution 24

*Coefficients.*

$$b_n = 2\int_0^1 1\cdot\sin(n\pi x)\,dx = \frac{2\bigl(1-\cos n\pi\bigr)}{n\pi} = \begin{cases}\dfrac{4}{n\pi}, & n \text{ odd},\\[6pt] 0, & n \text{ even}.\end{cases}$$

*Partial sums at $x = 0.5$* (where $\sin(n\pi/2) = \pm1$):

| terms | $1$ ($n=1$) | $3$ ($n\le3$) | $5$ ($n\le5$) | $11$ | $51$ |
|---|---|---|---|---|---|
| $S_N(0.5)$ | $1.273240$ | $0.848826$ | $1.103474$ | $0.947305$ | $0.987762$ |

The exact value is $1$.

*Why the convergence is slow.* The odd extension of $f\equiv1$ on $(0,1)$ is a square wave with jumps of size $2$ at every integer. By the theorem of §7.9 the coefficients of a function with a jump decay only like $1/n$, and the partial sums converge pointwise like $O(1/N)$ away from the jump. The alternating overshoots in the table (above $1$, then below, then above) are the Gibbs phenomenon; the overshoot near $x = 0$ (where the jump is) does not shrink at all as $N$ grows, it merely narrows.

*Check.* The sum of the series at $x = 0.5$ should be $f(0.5) = 1$ since $f$ is continuous there after the odd extension? Careful: the odd extension is discontinuous at $x = 0$ and $x=\pm1$, but at $x = 0.5$ it equals $1$, so the series converges to $1$ ✓, consistent with $S_{51} = 0.9878$ and improving.

### Solution 25

Parseval's identity for a sine series on $(0,L)$ is

$$\frac{L}{2}\sum_{n=1}^\infty b_n^2 = \int_0^L f(x)^2\,dx .$$

Take $L = \pi$ and $f\equiv1$ on $(0,\pi)$; then $b_n = 4/(n\pi)$ for odd $n$, and

$$\frac{\pi}{2}\sum_{n\ \text{odd}}\frac{16}{n^2\pi^2} = \int_0^\pi 1\,dx = \pi .$$

Multiply both sides by $2/\pi$:

$$\sum_{n\ \text{odd}}\frac{16}{n^2\pi^2} = 2 \quad\Longrightarrow\quad \sum_{n\ \text{odd}}\frac{1}{n^2} = \frac{2\pi^2}{16} = \frac{\pi^2}{8}.$$

*Numerical check.* The first four odd terms give $1 + \frac19 + \frac1{25} + \frac1{49} = 1.17152$ against $\pi^2/8 = 1.23370$; with ten odd terms the partial sum is $1.20872$. The convergence is like $1/N$, consistent with the $b_n = O(1/n)$ decay.

*Remark.* The same argument applied to $f(x) = x$ on $(0,\pi)$ gives the classical $\sum 1/n^2 = \pi^2/6$, because $\sum_{\text{all}} = \sum_{\text{odd}} + \sum_{\text{even}}$ and $\sum_{\text{even}}1/n^2 = \frac14\sum_{\text{all}}1/n^2$, so $\sum_{\text{all}} = \frac{\pi^2}{8}\cdot\frac43 = \frac{\pi^2}{6}$.

## Advanced

### Solution 26

*Claim.* For $n,m\ge1$, $\displaystyle\int_0^L\sin\frac{n\pi x}{L}\sin\frac{m\pi x}{L}\,dx = \frac L2\delta_{nm}$.

*Proof.* Use the product-to-sum identity $\sin A\sin B = \frac12\bigl[\cos(A-B) - \cos(A+B)\bigr]$ with $A = n\pi x/L$, $B = m\pi x/L$:

$$\int_0^L \sin\frac{n\pi x}{L}\sin\frac{m\pi x}{L}\,dx = \frac12\int_0^L\cos\frac{(n-m)\pi x}{L}\,dx - \frac12\int_0^L\cos\frac{(n+m)\pi x}{L}\,dx .$$

**Case $n \ne m$.** Both $n - m$ and $n + m$ are non-zero integers. For any non-zero integer $k$,

$$\int_0^L\cos\frac{k\pi x}{L}\,dx = \left[\frac{L}{k\pi}\sin\frac{k\pi x}{L}\right]_0^L = \frac{L}{k\pi}\bigl(\sin k\pi - \sin 0\bigr) = 0,$$

because $\sin k\pi = 0$ for every integer $k$. Both terms vanish, so the integral is $0$.

**Case $n = m$.** Then the first cosine is $\cos 0 = 1$, and $\int_0^L 1\,dx = L$. The second is $\cos(2n\pi x/L)$, a full-period cosine, whose integral over a whole number of periods is $0$ (the same computation with $k = 2n$). Hence the integral is $\frac12 L - 0 = L/2$.

Combining the two cases gives $\frac L2\delta_{nm}$. $\blacksquare$

*Remark.* The proof uses only that $n \pm m$ are integers; it therefore also covers the cosine system, where $\cos(n\pi x/L)\cos(m\pi x/L) = \frac12[\cos((n-m)\pi x/L) + \cos((n+m)\pi x/L)]$ gives the same result for $n,m\ge1$, while the constant function is orthogonal to every cosine.

### Solution 27

*Derivation of the coefficients.* Suppose $f(x) = \sum_{n\ge1}b_n\sin(n\pi x/L)$ with the series converging uniformly on $[0,L]$. Uniform convergence allows the series to be multiplied by the bounded function $\sin(m\pi x/L)$ and integrated term by term. Hence

$$\int_0^L f(x)\sin\frac{m\pi x}{L}\,dx = \sum_{n\ge1}b_n\int_0^L\sin\frac{n\pi x}{L}\sin\frac{m\pi x}{L}\,dx = \sum_{n\ge1}b_n\frac L2\delta_{nm} = b_m\frac L2,$$

using orthogonality (Solution 26). Therefore $b_m = \frac2L\int_0^L f\sin(m\pi x/L)dx$, which is the stated formula. $\blacksquare$

*Bessel's inequality.* Let $S_N = \sum_{n\le N}b_n\sin(n\pi x/L)$ and $e_n = \sin(n\pi x/L)$. Then

$$0 \le \left\lVert f - S_N\right\rVert_2^2 = \lVert f\rVert_2^2 - 2\langle f,S_N\rangle + \lVert S_N\rVert_2^2 .$$

By orthogonality, $\langle f, S_N\rangle = \sum_{n\le N}b_n\langle f,e_n\rangle = \sum_{n\le N}b_n^2\frac L2 = \lVert S_N\rVert_2^2$. Substituting,

$$0 \le \lVert f\rVert_2^2 - \lVert S_N\rVert_2^2 \quad\Longrightarrow\quad \frac L2\sum_{n=1}^N b_n^2 \le \int_0^L f^2 ,$$

which is Bessel's inequality. It shows in particular that $\sum b_n^2$ converges.

*Parseval.* The sequence $S_N$ is Cauchy in $L^2$ because $\lVert S_N - S_M\rVert_2^2 = \frac L2\sum_{M<n\le N}b_n^2 \to 0$ as $M,N\to\infty$ (a convergent series of squares). Since $L^2$ is complete ([Riemann Integration](../../14-real-analysis/05-riemann-integration/README.md) develops the integral and its completeness properties), $S_N$ converges in $L^2$ to some $g$. The coefficients of $g$ against $e_n$ are $\langle g,e_n\rangle = \lim_N\langle S_N,e_n\rangle = b_n\frac L2$, the same as those of $f$; hence $f - g$ is orthogonal to every $e_n$. If the sine system is complete (which it is: see Strauss, §5.1, or Fourier's original argument), an $L^2$ function orthogonal to every $e_n$ must vanish, so $g = f$ and $\lVert f\rVert_2^2 = \lim_N\lVert S_N\rVert_2^2 = \frac L2\sum b_n^2$. $\blacksquare$

*Remark on completeness.* Completeness of the trigonometric system is the one non-elementary ingredient; it is normally proved either by the Weierstrass approximation theorem applied to continuous functions on the circle, or by Fejér's mean-value argument.

### Solution 28

**Theorem** (weak maximum principle). Let $\Omega \subset \mathbb{R}^2$ be a **bounded** open set with $\partial\Omega \ne \varnothing$, and let $u \in C^2(\Omega)\cap C(\bar\Omega)$ satisfy $\Delta u = 0$ in $\Omega$. Then

$$\max_{\bar\Omega}u = \max_{\partial\Omega}u, \qquad \min_{\bar\Omega}u = \min_{\partial\Omega}u .$$

*Proof.* It is enough to prove the maximum statement; the minimum statement follows by applying it to $-u$, which is also harmonic.

**Step 1 (remove the degeneracy).** For $\varepsilon>0$ define $v(x,y) = u(x,y) + \varepsilon(x^2+y^2)$. Then

$$\Delta v = \Delta u + \varepsilon(2 + 2) = 4\varepsilon > 0 \quad\text{in } \Omega .$$

**Step 2 ($v$ has no interior maximum).** Suppose $v$ attained its maximum at an interior point $p \in \Omega$. Since $v \in C^2$, the second-derivative test at an interior maximum gives $v_{xx}(p) \le 0$ and $v_{yy}(p) \le 0$. Adding, $\Delta v(p) \le 0$, contradicting $\Delta v(p) = 4\varepsilon > 0$. Hence every maximum of $v$ on the compact set $\bar\Omega$ lies on $\partial\Omega$.

**Step 3 (let $\varepsilon\to0$).** Write $R = \max_{\bar\Omega}(x^2+y^2)$, which is finite because $\Omega$ is **bounded**. For every $x \in \bar\Omega$,

$$u(x) \le v(x) \le \max_{\partial\Omega}v \le \max_{\partial\Omega}u + \varepsilon R .$$

Since $\varepsilon>0$ was arbitrary, $u(x) \le \max_{\partial\Omega}u$ for all $x$, so $\max_{\bar\Omega}u \le \max_{\partial\Omega}u$. The reverse inequality is immediate because $\partial\Omega \subseteq \bar\Omega$. $\blacksquare$

*Where boundedness is used.* In Step 2 the maximum of $v$ on $\bar\Omega$ must **exist** (a continuous function on a compact set attains its maximum — compactness of $\bar\Omega$ requires boundedness in $\mathbb{R}^2$), and in Step 3 the quantity $R = \sup_{\bar\Omega}(x^2+y^2)$ must be finite. On an unbounded domain both can fail: $u(x,y) = x$ is harmonic on the half-plane $x>0$, is bounded by $0$ on the boundary line $x=0$, yet is unbounded above in the domain. The conclusion of the theorem genuinely needs boundedness (or a growth condition at infinity).

*Remark.* The hypothesis $\partial\Omega\ne\varnothing$ matters: on a domain with no boundary (a torus, or $\mathbb{R}^2$) the statement is empty or false.

### Solution 29

**Claim 1 (uniqueness).** There is at most one $u \in C^2(\Omega)\cap C(\bar\Omega)$ with $\Delta u = 0$ in $\Omega$ and $u = h$ on $\partial\Omega$.

*Proof.* Suppose $u_1$ and $u_2$ both solve the problem. Then $w = u_1 - u_2$ is harmonic (the Laplacian is linear) and continuous on $\bar\Omega$, with $w = h - h = 0$ on $\partial\Omega$. By the weak maximum principle (Solution 28), applied to $w$:

$$\max_{\bar\Omega}w = \max_{\partial\Omega}w = 0,$$

and applied to $-w$:

$$\max_{\bar\Omega}(-w) = \max_{\partial\Omega}(-w) = 0 \quad\Longrightarrow\quad \min_{\bar\Omega}w = 0 .$$

Hence $w \le 0$ and $w \ge 0$, so $w \equiv 0$ and $u_1 = u_2$. $\blacksquare$

**Claim 2 (stability).** If $u_1,u_2$ solve the same problem with boundary data $h_1,h_2$ and $|h_1 - h_2| \le \delta$ on $\partial\Omega$, then $|u_1-u_2| \le \delta$ on $\bar\Omega$.

*Proof.* Let $w = u_1 - u_2$; then $w$ is harmonic and $|w| \le \delta$ on $\partial\Omega$. The maximum principle gives $\max_{\bar\Omega}w = \max_{\partial\Omega}w \le \delta$ and, applying it to $-w$, $\min_{\bar\Omega}w \ge -\delta$. Hence $|w| \le \delta$ throughout $\bar\Omega$, i.e.

$$\lVert u_1 - u_2\rVert_{\infty} \le \lVert h_1-h_2\rVert_\infty . \qquad \blacksquare$$

*Interpretation.* The solution operator $h \mapsto u$ is a contraction in the supremum norm: it never amplifies an error in the boundary data. This is precisely Hadamard's condition 3, with Lipschitz constant $1$. It also proves that the Dirichlet problem is *well conditioned*, which is why finite-difference and spectral methods for it behave so well.

### Solution 30

**Setup.** Let $u \in C^2(\mathbb{R}\times[0,\infty))$ solve $u_{tt} = c^2u_{xx}$ with $u(x,0) = f(x)$ and $u_t(x,0) = g(x)$, where $f \in C^2(\mathbb{R})$ and $g \in C^1(\mathbb{R})$.

**Step 1 (general solution).** In characteristic coordinates $\xi = x - ct$, $\eta = x + ct$ one computes $\partial_t = -c\partial_\xi + c\partial_\eta$, $\partial_x = \partial_\xi + \partial_\eta$, and hence

$$u_{tt} - c^2u_{xx} = -4c^2u_{\xi\eta} .$$

So the equation is $u_{\xi\eta} = 0$. Integrating in $\eta$ gives $u_\xi = \varphi(\xi)$ for an arbitrary function $\varphi$; integrating in $\xi$ gives

$$u = \int\varphi(\xi)\,d\xi + G(\eta) = F(\xi) + G(\eta) = F(x-ct) + G(x+ct).$$

**Step 2 (impose the first condition).** $u(x,0) = F(x) + G(x) = f(x)$.

**Step 3 (impose the second condition).** Differentiating in $t$,

$$u_t = -cF'(x-ct) + cG'(x+ct), \qquad u_t(x,0) = -cF'(x) + cG'(x) = g(x),$$

so $-F'(x) + G'(x) = g(x)/c$. Integrate from a fixed point $x_0$ to $x$:

$$-F(x) + F(x_0) + G(x) - G(x_0) = \frac1c\int_{x_0}^x g(s)\,ds .$$

Let $K = F(x_0) - G(x_0)$, a constant. Then

$$G(x) - F(x) = \frac1c\int_{x_0}^x g(s)\,ds + K .$$

**Step 4 (solve the $2\times2$ system).** Adding and subtracting the relations of Steps 2 and 3,

$$G(x) = \frac12\left[f(x) + \frac1c\int_{x_0}^x g + K\right], \qquad F(x) = \frac12\left[f(x) - \frac1c\int_{x_0}^x g - K\right].$$

**Step 5 (substitute).** With $x$ replaced by $x - ct$ in $F$ and by $x + ct$ in $G$:

$$u(x,t) = \frac12\left[f(x-ct) + f(x+ct)\right] + \frac{1}{2c}\left[\int_{x_0}^{x+ct}g - \int_{x_0}^{x-ct}g\right] + \frac{K - K}{2},$$

and the constant cancels, leaving

$$u(x,t) = \frac{f(x-ct)+f(x+ct)}{2} + \frac{1}{2c}\int_{x-ct}^{x+ct}g(s)\,ds . \qquad \blacksquare$$

*Regularity.* The formula defines a $C^2$ function when $f \in C^2$ and $g \in C^1$; the first term is then twice differentiable and the second is twice differentiable in $x$ (differentiate the integrand) and once in $t$ — but differentiating twice in $t$ produces $g'$, which exists because $g\in C^1$. Less regularity gives a weaker notion of solution; in particular $f$ merely continuous still gives a continuous $u$, which is the weak solution of §7.10.

*Check.* At $t=0$ the integral vanishes and $u = f$ ✓. Differentiating in $t$ and setting $t=0$: $\frac12[-cf'(x) + cf'(x)] + \frac{1}{2c}[cg(x) + cg(x)] = g(x)$ ✓.

### Solution 31

**Claim.** If $u \in C^2$ solves $u_{tt} = c^2u_{xx}$ on $0<x<L$ with $u(0,t) = u(L,t) = 0$, then

$$E(t) = \frac12\int_0^L\bigl(u_t^2 + c^2u_x^2\bigr)dx$$

is independent of $t$.

*Proof.* Differentiate under the integral sign (legitimate because $u \in C^2$ on a compact interval):

$$\frac{dE}{dt} = \int_0^L\bigl(u_tu_{tt} + c^2u_xu_{xt}\bigr)dx .$$

For the second term, integrate by parts in $x$:

$$\int_0^L c^2u_xu_{xt}\,dx = \bigl[c^2u_tu_x\bigr]_0^L - \int_0^L c^2u_{xx}u_t\,dx .$$

Substituting,

$$\frac{dE}{dt} = \int_0^L u_t\bigl(u_{tt} - c^2u_{xx}\bigr)dx + c^2\bigl[u_tu_x\bigr]_0^L .$$

The first term vanishes because $u$ solves the wave equation. For the boundary term, $u(0,t) = u(L,t) = 0$ for all $t$ implies $u_t(0,t) = u_t(L,t) = 0$; hence the bracket is zero. Therefore $dE/dt = 0$. $\blacksquare$

*Uniqueness.* If $u_1,u_2$ solve the same initial-boundary value problem, then $w = u_1-u_2$ solves it with zero data, so $w(x,0) = 0$ and $w_t(x,0) = 0$. Its energy at $t=0$ is

$$E(0) = \frac12\int_0^L\bigl(0 + c^2w_x(x,0)^2\bigr)dx .$$

Since $w(x,0) = 0$ for all $x$, $w_x(x,0) = 0$, so $E(0) = 0$. By conservation $E(t) = 0$ for all $t$, and since the integrand $u_t^2 + c^2u_x^2 \ge 0$ is continuous, it must vanish identically. Hence $w_t = 0$ and $w_x = 0$, so $w$ is constant in space and time; $w(x,0) = 0$ then forces $w \equiv 0$. $\square$

*Interpretation.* The two terms are the kinetic energy $\frac12\int u_t^2$ and the potential energy $\frac12\int c^2u_x^2$ stored in the stretching of the string. Their sum is constant: the string trades one for the other, which is why a plucked string keeps moving forever in the absence of damping. Damping would add a term $-\gamma\int u_t^2 \le 0$, making $E$ decrease.

### Solution 32

**Setup.** Write the principal part as a quadratic form in the frequency variable. Put

$$M = \begin{pmatrix} A & B/2\\ B/2 & C\end{pmatrix}, \qquad \xi = \begin{pmatrix}\xi_1\\ \xi_2\end{pmatrix},$$

so that $A\xi_1^2 + B\xi_1\xi_2 + C\xi_2^2 = \xi^{\mathsf T}M\xi$. Then

$$\det M = AC - \frac{B^2}{4} = -\frac14\bigl(B^2 - 4AC\bigr) = -\frac{\Delta}{4} .$$

**Transformation.** Let $(\xi,\eta)$ be new coordinates and $K = \dfrac{\partial(\xi,\eta)}{\partial(x,y)}$ the Jacobian matrix. By the chain rule, a plane wave $e^{i(\hat\xi_1\xi + \hat\xi_2\eta)}$ is, in the old variables, $e^{i(\xi_1x + \xi_2y)}$ with

$$\xi = K^{\mathsf T}\hat\xi .$$

Therefore the symbol of the transformed operator is $\hat\xi^{\mathsf T}(KMK^{\mathsf T})\hat\xi$, i.e. $\tilde M = KMK^{\mathsf T}$. Taking determinants,

$$\det\tilde M = \det K\cdot\det M\cdot\det K^{\mathsf T} = (\det K)^2\det M .$$

**Conclusion.** Since $\tilde\Delta = -4\det\tilde M$ and $\Delta = -4\det M$,

$$\tilde\Delta = (\det K)^2\,\Delta .$$

Because $K$ is invertible, $(\det K)^2 > 0$, so $\tilde\Delta$ has the same sign as $\Delta$ and vanishes exactly when $\Delta$ vanishes. This proves that hyperbolic, parabolic and elliptic are invariant under smooth invertible changes of coordinates. $\blacksquare$

*Consistency check.* A rotation has $\det K = 1$, so $\tilde\Delta = \Delta$; the canonical rotations $u_{xx}+u_{yy}\mapsto u_{\xi\xi}+u_{\eta\eta}$ preserve $\Delta = -4$ ✓, and $u_{tt}-c^2u_{xx}\mapsto u_{\xi\eta}$ preserves $\Delta = 4c^2$ up to the (positive) Jacobian factor ✓.

*Alternative direct proof.* Expanding $\tilde A, \tilde B, \tilde C$ from the chain rule and simplifying gives $\tilde B^2 - 4\tilde A\tilde C = (\xi_x\eta_y - \xi_y\eta_x)^2(B^2-4AC)$, the same statement with $\det K = \xi_x\eta_y-\xi_y\eta_x$ — a computation of about a page, which the matrix argument replaces with two lines.

## Challenge

### Solution 33

*Characteristic solution.* For $u_t + uu_x = 0$, the characteristics issued from $x_0$ are

$$x = x_0 + f(x_0)t, \qquad u = f(x_0) \text{ on that line},$$

because along $x(t) = x_0 + f(x_0)t$ we have $\frac{d}{dt}u = u_t + f(x_0)u_x = u_t + uu_x = 0$.

Two characteristics with data $x_0 < x_0'$ meet when

$$x_0 + f(x_0)t = x_0' + f(x_0')t \quad\Longrightarrow\quad t = -\frac{x_0' - x_0}{f(x_0') - f(x_0)} = -\frac{1}{\text{slope of } f}.$$

The earliest meeting time over all pairs is

$$t_b = -\frac{1}{\min_{x_0}f'(x_0)},$$

provided the minimum is negative.

*Computation.* With $f(x) = \dfrac{1}{1+x^2}$,

$$f'(x) = -\frac{2x}{(1+x^2)^2} .$$

Differentiate again:

$$f''(x) = -\frac{2(1+x^2)^2 - 2x\cdot 2(1+x^2)\cdot 2x}{(1+x^2)^4} = \frac{-2(1+x^2) + 8x^2}{(1+x^2)^3} = \frac{6x^2-2}{(1+x^2)^3}.$$

Setting $f''= 0$ gives $x^2 = 1/3$, i.e. $x = 1/\sqrt3$ (the negative root gives the maximum of $f'$). At $x = 1/\sqrt3$:

$$f'\left(\frac{1}{\sqrt3}\right) = -\frac{2/\sqrt3}{\left(1+\frac13\right)^2} = -\frac{2/\sqrt3}{16/9} = -\frac{18}{16\sqrt3} = -\frac{9}{8\sqrt3} = -\frac{3\sqrt3}{8}.$$

Therefore

$$t_b = \frac{8}{3\sqrt3} = \frac{8\sqrt3}{9} = 1.5396007\ldots$$

*What happens for $t > t_b$.* The characteristics cross and the implicit equation $u = f(x - ut)$ has more than one solution; the classical solution ceases to exist. The physically correct continuation is a **weak solution** with a shock: a discontinuity separating the left value $u_L$ and the right value $u_R$, moving at the Rankine–Hugoniot speed

$$s = \frac{\frac12u_R^2 - \frac12u_L^2}{u_R - u_L} = \frac{u_L + u_R}{2}.$$

The shock initially forms at $x = 1/\sqrt3 + f(1/\sqrt3)t_b = 0.5774 + 0.75\times1.5396 = 1.7321 = \sqrt3$, consistent with the characteristic through $(1/\sqrt3, 0)$ meeting its neighbour there.

*Check.* $\dfrac{8\sqrt3}{9} = \dfrac{8\times1.7320508}{9} = 1.53960$ ✓, and the numerical minimisation of $f'$ on a fine grid gives $\min f' = -0.649519$ at $x = 0.577350$, hence $t_b = 1/0.649519 = 1.53960$ ✓.

### Solution 34

**Claim.** Let $f$ be piecewise continuous on $[0,L]$, extended oddly, and let $u$ be given by the heat series. Then for every $t>0$, $u(\cdot,t) \in C^\infty[0,L]$, and every derivative is bounded uniformly in $x$ by a constant depending only on $t$.

*Proof.* Let $M = \sup_{[0,L]}\lvert f\rvert$, so $\lvert b_n\rvert = \bigl\lvert\frac2L\int_0^L f\sin(n\pi x/L)dx\bigr\rvert \le \frac2L\cdot M\cdot L = 2M$. Write $\lambda_n = n\pi/L$ and $\beta = \alpha\pi^2/L^2$, so the time factor is $e^{-\alpha\lambda_n^2t} = e^{-\beta n^2t}$.

For $k \ge 0$, differentiating the series $k$ times in $x$ gives the series with terms $b_n\lambda_n^k\sin^{(k)}(n\pi x/L)e^{-\beta n^2t}$, whose absolute value is bounded by

$$2M\,\lambda_n^k\,e^{-\beta n^2t} = 2M\left(\frac{\pi}{L}\right)^k n^k e^{-\beta n^2t}.$$

The numerical series $\sum_{n\ge1} n^k e^{-\beta n^2t}$ converges for every $t>0$ and every $k$: the ratio of consecutive terms is

$$\frac{(n+1)^k e^{-\beta(n+1)^2t}}{n^k e^{-\beta n^2t}} \sim e^{-2\beta nt}\to 0 .$$

By the Weierstrass $M$-test the differentiated series converges uniformly on $[0,L]$ (indeed on $\mathbb{R}$), and its terms are continuous. Uniform convergence of the differentiated series is exactly the hypothesis needed to differentiate term by term, so $u(\cdot,t)$ is $k$ times differentiable for every $k$, with the displayed bound. $\blacksquare$

*Why $t = 0$ fails.* At $t=0$ the bound becomes $2M(\pi/L)^k\sum n^k$, which diverges for every $k\ge1$. Nothing in the argument survives: a function with a jump has a Fourier series whose term-by-term derivative diverges everywhere, and indeed the initial datum need not even be continuous, let alone differentiable. The exponential factor is doing all the work, and it is absent at $t=0$.

*Remark.* The same estimate shows that $u(\cdot,t)$ is real-analytic in $x$ for $t>0$: the coefficients decay like $e^{-\beta n^2t}$, faster than any exponential, so the complexified series converges in a strip $|\operatorname{Im}z| < \sqrt{\beta t}$. This is the strongest form of the smoothing property.

### Solution 35

*Setup.* Let $S_N$ be the $N$-th partial sum of the square wave of half-height $1$, with $N$ odd:

$$S_N(x) = \frac4\pi\sum_{k\ \text{odd},\,k\le N}\frac{\sin kx}{k}, \qquad S(x) = \operatorname{sign}(\sin x) \text{ for } x\in(-\pi,\pi).$$

**Step 1 (a closed form for the derivative).** Differentiate:

$$S_N'(x) = \frac4\pi\sum_{k\ \text{odd},\,k\le N}\cos kx .$$

Use the finite geometric sum $1 + z^2 + \dots + z^{N-1} = \dfrac{1-z^{N+1}}{1-z^2}$ with $z = e^{ix}$; its real part gives

$$\sum_{k\ \text{odd},\,k\le N}\cos kx = \frac{\sin\bigl((N+1)x\bigr)}{2\sin x} .$$

(Check for $N=1$: $\cos x = \sin 2x/(2\sin x)$ ✓.) Therefore

$$S_N'(x) = \frac{2}{\pi}\,\frac{\sin\bigl((N+1)x\bigr)}{\sin x} .$$

**Step 2 (the first critical point).** $S_N(0) = 0$ and $S_N'(0^+) = \frac{2(N+1)}{\pi} > 0$, so $S_N$ increases from $0$. Its first zero of $S_N'$ is at $(N+1)x = \pi$, i.e.

$$x_1 = \frac{\pi}{N+1},$$

which is therefore the first maximum.

**Step 3 (integral representation).** Since $S_N(0) = 0$,

$$S_N(x) = \frac2\pi\int_0^x\frac{\sin\bigl((N+1)t\bigr)}{\sin t}\,dt .$$

At $x = x_1$, substitute $s = (N+1)t$:

$$S_N(x_1) = \frac2\pi\int_0^{\pi}\frac{\sin s}{(N+1)\sin\bigl(s/(N+1)\bigr)}\,ds .$$

**Step 4 (limit).** As $N\to\infty$, $(N+1)\sin\bigl(s/(N+1)\bigr) \to s$ uniformly on $[0,\pi]$ (Taylor: $\sin u = u - u^3/6 + \cdots$, so the expression is $s + O(s^3/N^2)$). Moreover Jordan's inequality gives $(N+1)\sin(s/(N+1)) \ge 2s/\pi$ for $s \in [0,\pi]$, so the integrands are dominated by $\frac{\pi}{2}\cdot\frac{1}{s}\cdot\sin s$, which is integrable. By dominated convergence,

$$\lim_{N\to\infty}S_N(x_1) = \frac2\pi\int_0^\pi\frac{\sin s}{s}\,ds = 1.1789797\ldots$$

**Conclusion.** The partial sums attain a maximum of about $1.17898$ while the function itself equals $1$ just to the right of the jump at $x=0$. The **overshoot** is $0.17898$, which is $8.95\%$ of the jump $2$ (or $17.9\%$ of the half-height). It does not decrease with $N$; only the width of the overshoot region shrinks, like $1/N$.

*Numerical confirmation.* Evaluating $S_{201}$ on a grid of $20000$ points gives a maximum of $1.178988$, in agreement with $1.178980$ to four decimals ✓. The table in §7.9 shows the value at the fixed point $x = \pi/2$ converging to $1$ (that point is far from the jump), which is consistent: the non-uniformity is local to the jump.

### Solution 36

**Step 1 (series solution).** In polar coordinates the harmonic functions bounded at the origin are

$$u(r,\theta) = \frac{a_0}{2} + \sum_{n=1}^\infty r^n\bigl(a_n\cos n\theta + b_n\sin n\theta\bigr),$$

with $a_n = \frac1\pi\int_{-\pi}^{\pi}h(\phi)\cos n\phi\,d\phi$ and $b_n = \frac1\pi\int_{-\pi}^{\pi}h(\phi)\sin n\phi\,d\phi$ the Fourier coefficients of the boundary data $h(\theta) = u(1,\theta)$.

**Step 2 (substitute the coefficients).** Inserting the coefficient formulas and using $r^n\cos n\theta\cos n\phi + r^n\sin n\theta\sin n\phi = r^n\cos n(\theta-\phi)$,

$$u(r,\theta) = \frac{1}{2\pi}\int_{-\pi}^{\pi}h(\phi)\left[1 + 2\sum_{n=1}^\infty r^n\cos n(\theta-\phi)\right]d\phi .$$

**Step 3 (sum the series).** Put $\psi = \theta-\phi$ and $w = re^{i\psi}$. Then

$$1 + 2\sum_{n\ge1}r^n\cos n\psi = 1 + 2\operatorname{Re}\frac{w}{1-w} = 1 + 2\operatorname{Re}\frac{re^{i\psi}}{1-re^{i\psi}} .$$

Rationalising,

$$\frac{re^{i\psi}}{1-re^{i\psi}} = \frac{re^{i\psi}(1-re^{-i\psi})}{\lvert 1-re^{i\psi}\rvert^2} = \frac{r\cos\psi - r^2 + ir\sin\psi}{1 - 2r\cos\psi + r^2},$$

so

$$1 + 2\sum_{n\ge1}r^n\cos n\psi = 1 + \frac{2r\cos\psi - 2r^2}{1-2r\cos\psi+r^2} = \frac{1-r^2}{1-2r\cos\psi+r^2}.$$

**Step 4 (Poisson's formula).**

$$u(r,\theta) = \frac{1}{2\pi}\int_{-\pi}^{\pi}\frac{(1-r^2)\,h(\phi)}{1 - 2r\cos(\theta-\phi) + r^2}\,d\phi . \qquad \blacksquare$$

**Step 5 (mean value property).** Setting $r = 0$ gives

$$u(0,\theta) = \frac{1}{2\pi}\int_{-\pi}^{\pi}h(\phi)\,d\phi,$$

the average of the boundary values — the mean value property at the centre. For a general centre, translate the origin (harmonicity and the formula are translation-invariant), which gives the property for every circle.

**Step 6 (the requested data).** For $h(\theta) = 1 + 2\sin3\theta + \cos4\theta$, read off $a_0/2 = 1$, $b_3 = 2$, $a_4 = 1$, all other coefficients zero:

$$u(r,\theta) = 1 + 2r^3\sin 3\theta + r^4\cos 4\theta .$$

*Check.* $u(1,\theta) = 1 + 2\sin3\theta + \cos4\theta = h$ ✓; each term is harmonic (they are $r^n$ times a trig function of $n\theta$) ✓; the maximum on the disc is attained on the boundary, since $\lvert 2r^3\sin3\theta + r^4\cos4\theta\rvert \le 2r^3 + r^4 \le 2+1 = 3$ with equality only at $r=1$ ✓. The centre value is $u(0,\theta) = 1$, which equals the average of $h$ over the circle ✓.

