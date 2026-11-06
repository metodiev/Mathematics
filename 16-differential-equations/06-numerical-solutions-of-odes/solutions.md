# Numerical Solutions of ODEs — Solutions

> [Numerical Solutions of ODEs](README.md) · Solutions to the 36 problems in [exercises.md](exercises.md)

Every solution shows the strategy, the arithmetic step by step, and a check — comparison with the exact
solution, a Taylor prediction, or an observed-order estimate. Numerical values were computed from the
recursions as written; where a value is quoted to eight decimals it is the double-precision result of
the stated formula.

## Beginner

### Solution 1

*Strategy: apply $y_{n+1} = y_n + h(t_n-y_n)$ with $h=0.1$.*

* $n=0$: $t_0 = 0$, $y_0 = 0$, slope $= 0-0 = 0$, so $y_1 = 0 + 0.1(0) = 0$.
* $n=1$: $t_1 = 0.1$, $y_1 = 0$, slope $= 0.1-0 = 0.1$, so $y_2 = 0 + 0.1(0.1) = 0.010000$.

Exact: $y(0.2) = 0.2 - 1 + e^{-0.2} = -0.8 + 0.81873075 = 0.01873075$. The error after two steps is

$$0.010000 - 0.01873075 = -8.73075\times10^{-3}.$$

*Check.* With $h=0.2$ (Solution 9.1 of the tutorial) the first two values are $0$ and $0.04$; with $h=0.1$ the second value is $0.01$. Both are first-order approximations, and the $h=0.1$ value is roughly twice as accurate at $t=0.2$ — consistent with $O(h)$ ✓.

### Solution 2

$h=0.1$, $f(t,y) = y-t^2+1$.

* $n=0$: $f = 0.5-0+1 = 1.5$, $y_1 = 0.5+0.1(1.5) = 0.6500$.
* $n=1$: $t=0.1$, $f = 0.65-0.01+1 = 1.64$, $y_2 = 0.65+0.1(1.64) = 0.8140$.
* $n=2$: $t=0.2$, $f = 0.814-0.04+1 = 1.774$, $y_3 = 0.814+0.1(1.774) = 0.9914$.

Exact at $t=0.3$: $(1.3)^2 - 0.5e^{0.3} = 1.69 - 0.6749290 = 1.0150710$. Error:

$$0.9914 - 1.015071 = -2.3671\times10^{-2}.$$

*Check.* The local error of the first step is $0.65 - 0.6574145 = -7.4145\times10^{-3}$, and three such errors accumulate to about $-2.2\times10^{-2}$ — the observed $-2.37\times10^{-2}$ is consistent ✓.

### Solution 3

$y'=2y$ gives $y_{n+1} = y_n + 0.25(2y_n) = 1.5\,y_n$. Starting from $y_0=1$:

| $t$ | $0.25$ | $0.50$ | $0.75$ | $1.00$ |
|---|---|---|---|---|
| $y_n$ | $1.500000$ | $2.250000$ | $3.375000$ | $5.062500$ |

Exact: $e^{2} = 7.3890561$. Error at $t=1$: $5.0625 - 7.3890561 = -2.3265561$.

*Why it underestimates.* The solution $e^{2t}$ is convex and increasing, so every tangent lies below the curve; Euler follows the tangent at the left end of each step and therefore always lags. The factor per step is $1+2h = 1.5$, whereas the exact factor is $e^{2h} = e^{0.5} = 1.6487213$. Since $(1+2h) < e^{2h}$ for every $h>0$ (the inequality $\ln(1+x)<x$ with $x = 2h$), Euler's method *always* underestimates this problem, for every step size ✓.

### Solution 4

Implicit Euler: $y_{n+1} = y_n + h(-5y_{n+1})$, so

$$y_{n+1}(1+5h) = y_n \quad\Longrightarrow\quad y_{n+1} = \frac{y_n}{1+5h} = \frac{1}{1+2} = 0.333333 .$$

Comparisons: exact $e^{-2} = 0.135335$; explicit Euler would give $y_1 = 1 + 0.4(-5) = -1$.

*Interpretation.* Both one-step answers are poor — $h=0.4$ is a large step for a rate of $5$ — but they are poor in different ways. Explicit Euler produces a **negative** temperature-like quantity (impossible for a decaying solution) and is outside its stability interval ($h<0.4$ is required, and $h=0.4$ is exactly the boundary). Implicit Euler stays positive and inside $(0,1)$, which is the qualitative behaviour the equation demands. That is the practical advantage of A-stability: the answer may be inaccurate, but it is never absurd.

*Check.* With $h=0.1$ implicit Euler gives $(1/1.5)^4 = 0.19753$ at $t=0.4$, against the exact $e^{-2}=0.13534$; the error is $+0.062$, first order ✓.

### Solution 5

Heun: $k_1 = f(t_n,y_n)$, $k_2 = f(t_n+h, y_n+hk_1)$, $y_{n+1} = y_n+\frac h2(k_1+k_2)$, $h=0.2$.

* $n=0$: $t=0$, $y=0$; $k_1 = 0$; predictor $0+0.2(0)=0$; $k_2 = 0.2-0 = 0.2$; $y_1 = 0+0.1(0.2) = 0.020000$.
* $n=1$: $t=0.2$, $y=0.02$; $k_1 = 0.2-0.02 = 0.18$; predictor $0.02+0.2(0.18) = 0.056$; $k_2 = 0.4-0.056 = 0.344$; $y_2 = 0.02+0.1(0.18+0.344) = 0.072400$.

Exact at $t=0.4$: $0.4-1+e^{-0.4} = 0.0703200$. Error: $+2.0800\times10^{-3}$.

*Check.* The error is one order smaller than Euler's at the same step ($-0.0303$) and has the opposite sign — for a second-order method the local error is $O(h^3)$ and its sign is governed by the third derivative of the solution, whereas Euler's is governed by the second. There is no general rule fixing the sign; it must be checked problem by problem ✓.

### Solution 6

Midpoint: $k_1 = f(t_n,y_n) = 0$; $k_2 = f(t_n+h/2,\, y_n+\frac h2 k_1) = f(0.1,0) = 0.1 - 0 = 0.1$; $y_1 = y_0 + hk_2 = 0.2(0.1) = 0.020000$.

The value equals Heun's, and that is not an accident. For $f(t,y) = t-y$,

$$\text{Heun} = y + \frac h2\bigl[k_1 + (k_1 + h(1-k_1))\bigr] = y + hk_1 + \frac{h^2}{2}(1-k_1),$$
$$\text{Midpoint} = y + h\Bigl(k_1 + \frac h2(1-k_1)\Bigr) = y + hk_1 + \frac{h^2}{2}(1-k_1),$$

because the exact solution of the auxiliary relation $k_2 = k_1 + \frac h2(1-k_1)$ is the same in both cases. The agreement is a special feature of an **affine** $f$ with constant coefficients; for $f = y-t^2+1$ the two methods differ (README §7.9) ✓.

### Solution 7

Exact from $y(0)=1$: $y(0.1) = e^{-0.2} = 0.8187307531$. One Euler step:

$$y_1 = 1 + 0.1(-2\cdot1) = 0.8 .$$

So

$$h\tau_1 = y(0.1)-y_1 = 0.0187307531, \qquad \tau_1 = 0.187307531 .$$

Taylor prediction: $y'' = -2y' = 4y$, so $y''(0) = 4$ and $h\tau_1 \approx \frac{h^2}{2}y''(0) = \frac{0.01}{2}(4) = 0.020000$. The computed $0.018731$ is $6.3\%$ below the prediction; the next term is $\frac{h^3}{6}y'''(0)$ with $y''' = -8$, giving $-0.001333$, and $0.02 - 0.00133 = 0.018667$ — within $0.3\%$ of the computed value ✓.

*Note the sign:* the local error is **positive** here even though the global error of Euler is negative — the two are different objects.

### Solution 8

$f = y$, so all stages are easy: $k_1 = 1$, $k_2 = 1 + \frac12(1) = 1.5$, $k_3 = 1+\frac12(1.5) = 1.75$, $k_4 = 1 + 1(1.75) = 2.75$. Then

$$y_1 = 1 + \frac16\bigl(1 + 2(1.5) + 2(1.75) + 2.75\bigr) = 1 + \frac16(9.25) = 2.7083333 .$$

Exact $e = 2.7182818$; error $-9.9485\times10^{-3}$. One Euler step with $h=1$ gives $2$, with error $-0.7183$ — a factor $72$ worse for the same step ✓.

*Check.* For $f = y$ the RK4 result must be the fourth Taylor polynomial of $e^h$: $1+1+\frac12+\frac16+\frac1{24} = 2.7083333$ ✓.

### Solution 9

$f(t,y) = t-y$, $t_0 = 0$, $y_0 = 0$, $h = 0.2$:

$$k_1 = f(0,0) = 0,$$
$$k_2 = f(0.1,\ 0+0.1\cdot0) = 0.1 - 0 = 0.1,$$
$$k_3 = f(0.1,\ 0+0.1\cdot0.1) = 0.1 - 0.01 = 0.09,$$
$$k_4 = f(0.2,\ 0+0.2\cdot0.09) = 0.2 - 0.018 = 0.182,$$
$$y_1 = 0 + \frac{0.2}{6}\bigl(0 + 0.2 + 0.18 + 0.182\bigr) = \frac{0.2}{6}(0.562) = 0.0187333 .$$

Exact $y(0.2) = 0.01873075$; error $+2.58\times10^{-6}$.

*Check.* Euler's one step gives $0$ (error $-0.0187$), Heun gives $0.02$ (error $+1.27\times10^{-3}$), RK4 gives $0.0187333$ (error $+2.6\times10^{-6}$) — each order buys roughly two more correct digits at this step ✓.

### Solution 10

$y_{n+1} = y_n + 0.1y_n = 1.1y_n$, so $y_{10} = 1.1^{10} = 2.59374246$.

$e = 2.71828183$, error $-0.12453937$, relative error

$$\frac{0.12453937}{2.71828183} = 4.58\times10^{-2} .$$

*Check.* The exact amplification over $[0,1]$ is $e^{1}$; the numerical one is $(1+0.1)^{10}$. Since $\ln(1.1) = 0.0953102 < 0.1$, the numerical growth rate is smaller, hence the underestimate. The relative error $0.0458$ is consistent with $\frac h2 = 0.05$ for a first-order method ✓.

### Solution 11

The amplification factor is $1-25h$, so stability requires

$$\lvert 1-25h\rvert < 1 \iff 0 < h < \frac{2}{25} = 0.08 .$$

At $h = 0.08$ the factor is $-1$ (persistent oscillation); beyond it the solution grows.

For RK4 the condition is $25h \le 2.7852936$, i.e.

$$h \le 0.11141174 .$$

*Check.* The ratio of the two limits is $2.7853/2 = 1.3927$, exactly the ratio of the stability boundaries $2.7853$ and $2$ ✓. Notice that the accuracy requirement is far stricter here: to resolve $e^{-25t}$ to three digits one needs $h\sim10^{-3}$, some hundred times smaller than the stability limit.

### Solution 12

$R(z) = 1+z$ is the stability function of **explicit Euler**: applying $y_{n+1} = y_n+h\lambda y_n$ to $y'=\lambda y$ gives the factor $1+h\lambda = 1+z$.

* Order: the Taylor expansion $1+z$ matches $e^z$ through the constant and linear terms only, so the local order is $2$ and the **global order is $1$**.
* Real stability interval: $\lvert 1+x\rvert<1$ for real $x$ gives $-2<x<0$, i.e. $(-2,0)$.
* On $y' = iy$ (a pure oscillator) $z = ih$ is purely imaginary, and $\lvert 1+ih\rvert = \sqrt{1+h^2} > 1$ for every $h>0$. The computed solution grows like $(1+h^2)^{n/2}\to\infty$: Euler cannot integrate an oscillator at all, no matter how small the step ✓.

*Remark.* This is why the real stability interval is not enough to characterise a method: for oscillatory problems the relevant set is the intersection of the stability region with the imaginary axis, which for Euler is just $\{0\}$.

### Solution 13

Heun's method in Butcher form:

$$\begin{array}{c|cc} 0 & 0 & 0\\ 1 & 1 & 0\\ \hline & \tfrac12 & \tfrac12 \end{array}$$

So $c_1 = 0$, $c_2 = 1$, $a_{21} = 1$, $b_1 = b_2 = \frac12$.

*Condition 1:* $b_1+b_2 = \frac12+\frac12 = 1$ ✓.
*Condition 2:* $b_2c_2 = \frac12\cdot1 = \frac12$ ✓.

Both order-2 conditions hold, so the method is second order. (Consistency alone would only require $b_1+b_2=1$.)

*Check on the tableau convention.* The row sums must equal $c_i$: row 2 has $a_{21} = 1 = c_2$ ✓; row 1 is empty and $c_1 = 0$ ✓. Explicit methods have zeros on and above the diagonal ✓.

## Intermediate

### Solution 14

Problem: $y' = -2ty^2$, $y(0)=1$, exact $y = 1/(1+t^2)$, so $y(1) = 0.5$. With $h=0.2$:

| Method | $y_1$ | $y_2$ | $y_3$ | $y_4$ | $y_5$ | error at $t=1$ |
|---|---|---|---|---|---|---|
| Euler | $1.000000$ | $0.920000$ | $0.784576$ | $0.636842$ | $0.507060$ | $+7.060\times10^{-3}$ |
| Heun | $1.000000$ | $0.960000$ | $0.860298$ | $0.735043$ | $0.611572$ | $+3.338\times10^{-3}$ |
| RK4 | $1.000000$ | $0.961533$ | $0.862052$ | $0.735278$ | $0.609752$ | $+7.203\times10^{-6}$ |

(The five numeric columns are $y$ at $t = 0.2, 0.4, 0.6, 0.8, 1.0$; the last column is the error at $t=1$.)

*Arithmetic for the first Euler step:* $f(0,1) = 0$, so $y_1 = 1$. Second step: $f(0.2,1) = -2(0.2)(1) = -0.4$, so $y_2 = 1 + 0.2(-0.4) = 0.92$ ✓.

*Ranking.* RK4 is far the best ($7\times10^{-6}$), Heun is about twice as accurate as Euler at this coarse step, and all three errors are positive (the numerical solutions decay too slowly). At $h=0.2$ the asymptotic regime has not been reached for the second-order methods, which is why the ratio Euler/Heun is only about $2$ rather than $h^{-1}$.

### Solution 15

The ratios of successive errors are

$$\frac{3.338\times10^{-3}}{9.186\times10^{-4}} = 3.634, \qquad \frac{9.186\times10^{-4}}{2.363\times10^{-4}} = 3.887, \qquad \frac{2.363\times10^{-4}}{5.976\times10^{-5}} = 3.954 .$$

Observed order: $\log_2 3.954 = 1.983$ for the finest pair. The theoretical order is $2$, and the sequence is converging to $2$ from below as $h\to0$ ✓. The estimate is reliable only for the finest pair, which is the practical rule: use the two smallest steps.

### Solution 16

Ratios: $0.4397/0.2420 = 1.817$; $0.2420/0.1275 = 1.898$; $0.1275/0.0655 = 1.947$. Observed orders: $0.861$, $0.924$, $0.961$.

*Why so slow.* The error bound is $\frac{M}{2L}(e^{L(t_n-t_0)}-1)h$ with $L = 1$ (here $f = y-t^2+1$ has $f_y = 1$) and $M = \max_{[0,2]}\lvert y''\rvert$. Since $y'' = 2-\frac12e^t$, one has $M = \lvert 2-\frac12e^2\rvert = 1.694$, so the bound's constant is $\frac{1.694}{2}(e^2-1) = 5.41$. The observed error at $h=0.2$ is $0.4397 = 2.2h$, comfortably inside the bound but a factor $2.5$ below it. The ratio only approaches $2$ once $hL\ll1$; halving from $0.2$ to $0.025$ improves the ratio from $1.82$ to $1.95$, and three further halvings give $1.99$ ✓.

*Moral.* An order estimate from a coarse table is a lower bound on the order, never a contradiction of the theory.

### Solution 17

The Jacobian is $-100$, so explicit Euler is stable only for

$$h < \frac{2}{100} = 0.02 .$$

Implicit Euler with $h=0.1$:

$$y_1 = \frac{y_0 + 100h\cos t_1 - h\sin t_1}{1+100h} = \frac{0 + 10\cos(0.1) - 0.1\sin(0.1)}{11} .$$

Numerically, $\cos(0.1) = 0.99500417$, $\sin(0.1) = 0.09983342$, so

$$y_1 = \frac{9.9500417 - 0.0099833}{11} = \frac{9.9400584}{11} = 0.9036417 .$$

Exact: $0.9949586$ (that is $\cos 0.1 - e^{-10}$). Error: $-9.13\times10^{-2}$.

*Interpretation.* The first step is inaccurate because the fast transient $e^{-100t}$ is not resolved — the exact solution has already fallen to $4.5\times10^{-5}$ by $t = 0.1$, while the numerical solution is still near $1$. But the error is *damped* by the factor $1/11$ per step, so by $t=0.5$ the value is $0.877128$ against $0.877583$ — four correct digits. Explicit Euler at this step would give $|y|\sim10^{19}$.

### Solution 18

$R(z) = 1+z+\frac{z^2}{2}+\frac{z^3}{6}+\frac{z^4}{24}$. Take $z = -5$ (negative real, so $\operatorname{Re}z<0$):

$$R(-5) = 1 - 5 + 12.5 - 20.833333 + 26.041667 = 13.708333 .$$

Since $\lvert R(-5)\rvert = 13.708333 > 1$, the point $z=-5$ lies outside the stability region $\mathcal{S} = \{z:\lvert R(z)\rvert<1\}$, even though $-5$ is in the left half-plane. Hence RK4 is not A-stable ✓.

Even more simply, for $z = -10$: $R = 1-10+50-166.667+416.667 = 291$, growing like $z^4/24$ as $\lvert z\rvert\to\infty$.

*Moral.* The real stability interval $(-2.785,0)$ says exactly the same thing: any $z<-2.785$ is outside. A-stability would require the interval to be $(-\infty,0)$.

### Solution 19

The two results are $y^{(1)} = 0.8292933333$ (one step of $h=0.2$) and $y^{(2)} = 0.8292982760$ (two steps of $h=0.1$). For RK4, $p=4$, so

$$\eta = \frac{y^{(2)}-y^{(1)}}{2^4-1} = \frac{4.9427\times10^{-6}}{15} = 3.295\times10^{-7}.$$

The true error of the fine result is

$$0.8292982760 - 0.8292986209 = -3.449\times10^{-7}.$$

The estimate $3.295\times10^{-7}$ is within $5\%$ of the true value ✓ — an excellent estimate, which is why step doubling is used in practice.

*Why it works.* The two errors are in the ratio $2^4 = 16$, so their difference is $15$ times the smaller one. The ratio of the actual errors is $5.288\times10^{-6}/3.449\times10^{-7} = 15.33$, close to $16$ ✓.

### Solution 20

AB2: $y_{n+1} = y_n + \frac h2(3f_n - f_{n-1})$ with $h=0.2$, $t_0 = 0$, $y_0 = 0.5$, $y_1 = 0.82929333$.

Compute the slopes: $f_0 = f(0,0.5) = 0.5-0+1 = 1.5$; $f_1 = f(0.2,0.82929333) = 0.82929333 - 0.04 + 1 = 1.78929333$. Then

$$y_2 = 0.82929333 + 0.1\bigl(3(1.78929333) - 1.5\bigr) = 0.82929333 + 0.1(3.86788000) = 1.21608133 .$$

Exact $y(0.4) = 1.21408765$; error $+1.994\times10^{-3}$.

*Comparison.* The RK4 value used as a start was accurate to $10^{-5}$, so the error is almost entirely AB2's. Compare with Heun at the same step: error $-7.2\times10^{-3}$; AB2 is better here because its error constant $5/12$ is smaller than Heun's ✓.

### Solution 21

AB4: $y_{n+1} = y_n + \frac{h}{24}\bigl(55f_n - 59f_{n-1} + 37f_{n-2} - 9f_{n-3}\bigr)$ with $h=0.2$ and $n=3$ (so $t_n = 0.6$, target $t=0.8$).

Slopes: $f_3 = f(0.6,1.64892202) = 1.64892202 - 0.36 + 1 = 2.28892202$; $f_2 = f(0.4,1.21407621) = 2.05407621$; $f_1 = f(0.2,0.82929333) = 1.78929333$; $f_0 = 1.5$.

$$y_4 = 1.64892202 + \frac{0.2}{24}\bigl(55(2.28892202) - 59(2.05407621) + 37(1.78929333) - 9(1.5)\bigr).$$

The bracket is $125.890711 - 121.190496 + 66.203853 - 13.5 = 57.404068$, so

$$y_4 = 1.64892202 + \frac{0.2}{24}(57.404068) = 1.64892202 + 0.47836723 = 2.12728925 .$$

Exact $y(0.8) = 2.12722954$; error $+5.97\times10^{-5}$.

*Remark.* The start-up values were themselves accurate to about $10^{-6}$, so this error is genuinely AB4's; it is thirty times smaller than AB2's at the same step, consistent with the higher order.

### Solution 22

The AB4 prediction is $\tilde y_4 = 2.12728925$. Evaluate the slope there:

$$f_4 = f(0.8, 2.12728925) = 2.12728925 - 0.64 + 1 = 2.48728925 .$$

AM4: $y_4 = y_3 + \frac{h}{24}\bigl(9f_4 + 19f_3 - 5f_2 + f_1\bigr)$:

$$y_4 = 1.64892202 + \frac{0.2}{24}\bigl(9(2.48728925) + 19(2.28892202) - 5(2.05407621) + 1.78929333\bigr).$$

The bracket is $22.385603 + 43.489518 - 10.270381 + 1.789293 = 57.394033$, so

$$y_4 = 1.64892202 + \frac{0.2}{24}(57.394033) = 1.64892202 + 0.47828361 = 2.12720563 .$$

Exact $y(0.8) = 2.12722954$; error $-2.39\times10^{-5}$.

*Comparison.* The correction moved the value from $+5.97\times10^{-5}$ to $-2.39\times10^{-5}$ — a factor $2.5$ improvement for one extra function evaluation. The error changed sign because AM4's error constant ($-19/720$) has the opposite sign to AB4's ($+251/720$) ✓.

### Solution 23

For a linear problem $u_1(1;s)$ is an affine function of $s$, so two shots determine it exactly and no iteration is needed:

$$s = s_0 + (s_1-s_0)\frac{\beta - u_1(1;s_0)}{u_1(1;s_1)-u_1(1;s_0)} = 0 + 1\cdot\frac{2.71828183 - 1.54305207}{2.71820994 - 1.54305207} .$$

The numerator is $1.17522976$ and the denominator is $1.17515787$, so

$$s = 1.00006117 .$$

One more interpolation is unnecessary: for a linear BVP the secant method converges in one step (the residual is linear in $s$), and indeed $u_1(1;s) = e$ by construction.

*Important caveat.* The fact that $u_1(1;s) = e$ exactly is a consequence of the interpolation, not of accuracy. The interior errors are those of the RK4 integration, about $10^{-5}$ (README §9.7). A residual of zero at the far end is therefore not evidence that the solution is accurate.

### Solution 24

With $N=4$, $h = 0.25$, $h^2 = 0.0625$, the unknowns are $y_1,y_2,y_3$ at $t = 0.25, 0.5, 0.75$. The scheme $y_{i-1}-(2+h^2)y_i+y_{i+1} = 0$ becomes

$$y_1 - 2.0625y_2 + y_3 = 0, \qquad y_0 - 2.0625y_1 + y_2 = 0, \qquad y_2 - 2.0625y_3 + y_4 = 0,$$

with $y_0 = 1$, $y_4 = e = 2.71828183$. In matrix form:

$$\begin{pmatrix}-2.0625 & 1 & 0\\ 1 & -2.0625 & 1\\ 0 & 1 & -2.0625\end{pmatrix}\begin{pmatrix}y_1\\y_2\\y_3\end{pmatrix} = \begin{pmatrix}-1\\0\\-2.71828183\end{pmatrix}.$$

Solving (Gaussian elimination or the Thomas algorithm):

$$y_1 = 1.28470576, \qquad y_2 = 1.64970563, \qquad y_3 = 2.11781210 .$$

| $t$ | $0.25$ | $0.50$ | $0.75$ |
|---|---|---|---|
| $y_h$ | $1.28470576$ | $1.64970563$ | $2.11781210$ |
| $e^t$ | $1.28402542$ | $1.64872127$ | $2.11700002$ |
| error | $6.80\times10^{-4}$ | $9.84\times10^{-4}$ | $8.12\times10^{-4}$ |

*Check.* The errors are all of the same size and decrease by a factor $4$ when $h$ is halved (README §7.8), confirming second-order accuracy ✓. Note that a shooting solution of the same problem (Solution 23) has errors of order $10^{-5}$ — the finite-difference scheme at $N=4$ is much coarser.

### Solution 25

**Claim.** If $y \in C^2[t_0,T]$ and $f$ is continuous, then Euler's local truncation error

$$\tau_{n+1} = \frac{y(t_{n+1})-y(t_n)}{h} - f\bigl(t_n,y(t_n)\bigr)$$

satisfies $\max_n\lvert\tau_{n+1}\rvert \le \frac h2\max\lvert y''\rvert \to 0$ as $h\to0$.

*Proof.* Taylor's theorem with Lagrange remainder gives, for some $\xi_n \in (t_n,t_{n+1})$,

$$y(t_{n+1}) = y(t_n) + hy'(t_n) + \frac{h^2}{2}y''(\xi_n) .$$

Since $y$ solves the ODE, $y'(t_n) = f(t_n,y(t_n))$. Substituting and dividing by $h$:

$$\tau_{n+1} = \frac{1}{h}\Bigl[h f(t_n,y(t_n)) + \frac{h^2}{2}y''(\xi_n)\Bigr] - f(t_n,y(t_n)) = \frac h2 y''(\xi_n) .$$

Hence $\lvert\tau_{n+1}\rvert \le \frac h2 M$ with $M = \max_{[t_0,T]}\lvert y''\rvert$, which is finite because $y''$ is continuous on a compact interval. The bound is independent of $n$, so $\max_n\lvert\tau_{n+1}\rvert \le \frac h2M\to0$. $\blacksquare$

*Regularity required.* $y\in C^2$ (so that Taylor's theorem applies with a second-order remainder). Since $y'' = f_t + ff_y$ along the solution, it suffices that $f$ be $C^1$; for merely continuous $f$ the solution may not be twice differentiable and the estimate must be replaced by a weaker one.

## Advanced

### Solution 26

**Setup.** A two-stage explicit Runge–Kutta method is

$$k_1 = f(t_n,y_n), \qquad k_2 = f\bigl(t_n+c_2h,\ y_n+a_{21}hk_1\bigr), \qquad y_{n+1} = y_n + h(b_1k_1+b_2k_2).$$

The row-sum convention requires $a_{21} = c_2$ (the second stage is evaluated at $t_n+c_2h$ because the argument of $f$ in $t$ is advanced by $c_2h$). Write $f$, $f_t$, $f_y$ for their values at $(t_n,y(t_n))$.

**Expansion of the method.** From $k_1 = f$ and a first-order Taylor expansion in two variables,

$$k_2 = f + c_2hf_t + a_{21}hk_1f_y + O(h^2) = f + h\bigl(c_2f_t + c_2ff_y\bigr) + O(h^2).$$

Therefore

$$y_{n+1} = y_n + h\bigl[b_1f + b_2\bigl(f + hc_2(f_t+ff_y) + O(h^2)\bigr)\bigr] = y_n + h(b_1+b_2)f + h^2b_2c_2\bigl(f_t+ff_y\bigr) + O(h^3).$$

**Expansion of the exact solution.** With $y' = f$ and $y'' = f_t + ff_y$ (total derivative along the solution),

$$y(t_{n+1}) = y(t_n) + hf + \frac{h^2}{2}\bigl(f_t+ff_y\bigr) + O(h^3).$$

**Matching.** Comparing coefficients of $h$ and $h^2$:

$$b_1+b_2 = 1, \qquad b_2c_2 = \frac12 . \qquad \blacksquare$$

**The two natural choices.** Taking $c_2 = 1$ gives $b_2 = \frac12$, $b_1 = \frac12$: Heun's method, which is the trapezoidal rule with the right-hand slope predicted by Euler. Taking $c_2 = \frac12$ gives $b_2 = 1$, $b_1 = 0$: the midpoint method, which samples the slope at the midpoint of the interval. Any pair with $b_2c_2 = \frac12$ works, so there is a one-parameter family of second-order two-stage methods, but only these two have all coefficients in $[0,1]$ and a natural geometric interpretation.

*Remark.* The third-order conditions cannot be satisfied by any two-stage explicit method — see Solution 35.

### Solution 27

**Lemma (discrete Gronwall).** Let $a_n \ge 0$ satisfy $a_{n+1}\le(1+A)a_n + B$ for $n\ge0$, with $A,B\ge0$. Then

$$a_n \le (1+A)^n a_0 + \frac{B}{A}\bigl[(1+A)^n-1\bigr] \le e^{nA}a_0 + \frac BA\bigl(e^{nA}-1\bigr).$$

*Proof.* Iterate the inequality:

$$a_1 \le (1+A)a_0 + B,$$
$$a_2 \le (1+A)^2a_0 + (1+A)B + B,$$
$$\vdots$$
$$a_n \le (1+A)^na_0 + B\sum_{k=0}^{n-1}(1+A)^k = (1+A)^na_0 + B\,\frac{(1+A)^n-1}{(1+A)-1} .$$

The geometric sum is exact. Finally $(1+A)^n \le e^{nA}$ because $\ln(1+A)\le A$ for $A\ge0$. $\blacksquare$

**Theorem (Euler's global error).** Let $f$ be continuous and Lipschitz in $y$ with constant $L$, let $y\in C^2[t_0,T]$ solve the IVP, and put $M = \max\lvert y''\rvert$. Then for a uniform mesh with $nh = t_n-t_0$,

$$\lvert y(t_n)-y_n\rvert \le \frac{M}{2L}\bigl(e^{L(t_n-t_0)}-1\bigr)h .$$

*Proof.* Write $e_n = y(t_n)-y_n$. Taylor's theorem and the ODE give

$$y(t_{n+1}) = y(t_n) + hf\bigl(t_n,y(t_n)\bigr) + \frac{h^2}{2}y''(\xi_n),$$

while $y_{n+1} = y_n + hf(t_n,y_n)$. Subtracting,

$$e_{n+1} = e_n + h\bigl[f(t_n,y(t_n)) - f(t_n,y_n)\bigr] + \frac{h^2}{2}y''(\xi_n).$$

Taking absolute values and using the Lipschitz condition and $\lvert y''\rvert\le M$:

$$\lvert e_{n+1}\rvert \le \lvert e_n\rvert + hL\lvert e_n\rvert + \frac{h^2M}{2} = (1+hL)\lvert e_n\rvert + \frac{h^2M}{2}.$$

Apply the lemma with $A = hL$, $B = h^2M/2$, $a_n = \lvert e_n\rvert$, $a_0 = 0$:

$$\lvert e_n\rvert \le \frac{h^2M/2}{hL}\bigl(e^{nhL}-1\bigr) = \frac{M}{2L}\bigl(e^{L(t_n-t_0)}-1\bigr)h . \qquad \blacksquare$$

*Consequences.* The bound is $O(h)$, so Euler is first order. It also explains why the error grows with $L$: a large Lipschitz constant means the equation amplifies perturbations, and the exponential factor is the amplification over the whole interval. When $L\to0$ the bound must be read in the limit, $\lvert e_n\rvert \le \frac{M}{2}(t_n-t_0)h$, obtained by expanding the exponential.

### Solution 28

**AB2 is zero-stable.** Write AB2 as $\alpha_2y_{n+2}+\alpha_1y_{n+1}+\alpha_0y_n = h(\beta_2f_{n+2}+\beta_1f_{n+1}+\beta_0f_n)$. From $y_{n+1} = y_n+\frac h2(3f_n-f_{n-1})$, shifting the index to $n+2$:

$$y_{n+2} - y_{n+1} = \frac h2\bigl(3f_{n+1} - f_n\bigr),$$

so $\alpha_2 = 1$, $\alpha_1 = -1$, $\alpha_0 = 0$ and

$$\rho(\zeta) = \zeta^2-\zeta = \zeta(\zeta-1).$$

The roots are $\zeta = 0$ and $\zeta = 1$: both inside or on the unit circle, and both simple. Hence AB2 satisfies the root condition and is zero-stable ✓.

**The other method is not zero-stable.** For $y_{n+2} = 2y_{n+1}-y_n+hf_n$ we read off $\alpha_2 = 1$, $\alpha_1 = -2$, $\alpha_0 = 1$, so

$$\rho(\zeta) = \zeta^2-2\zeta+1 = (\zeta-1)^2 .$$

There is a **double** root at $\zeta = 1$, which violates the root condition. The consequence is visible directly: on $y' = 0$ the recursion is $y_{n+2} = 2y_{n+1}-y_n$, whose solutions are $y_n = A + Bn$ — an arbitrary linear drift that grows without bound. Round-off of size $\varepsilon$ at one step produces a final error of order $n\varepsilon = (T/h)\varepsilon\to\infty$ as $h\to0$. The method cannot converge, no matter how small the step.

**Zero-stability and convergence.** The Dahlquist equivalence theorem states that a linear multistep method converges for all sufficiently smooth IVPs if and only if it is **consistent** and **zero-stable**. The two conditions play different roles: consistency makes the method approximate the equation locally, and zero-stability prevents the *difference equation* from having solutions that grow for reasons unrelated to the differential equation. A method lacking either fails: an inconsistent method converges to the wrong solution, and a zero-unstable one diverges even on $y'=0$.

### Solution 29

**Setup.** AB2 is $y_{n+1} = y_n + \frac h2\bigl(3f_n - f_{n-1}\bigr)$. Let $y$ be the exact solution and write $f(t) := f(t,y(t))$, with $\dot f := \frac{d}{dt}f(t,y(t)) = f_t+ff_y$ and so on. Taylor expansion about $t_n$:

$$f_{n-1} = f(t_n-h) = f_n - h\dot f_n + \frac{h^2}{2}\ddot f_n - \frac{h^3}{6}\dddot f_n + O(h^4).$$

Hence

$$3f_n - f_{n-1} = 3f_n - f_n + h\dot f_n - \frac{h^2}{2}\ddot f_n + \frac{h^3}{6}\dddot f_n + O(h^4) = 2f_n + h\dot f_n - \frac{h^2}{2}\ddot f_n + \frac{h^3}{6}\dddot f_n + O(h^4).$$

Substituting:

$$y_n + \frac h2\bigl(3f_n-f_{n-1}\bigr) = y_n + hf_n + \frac{h^2}{2}\dot f_n - \frac{h^3}{4}\ddot f_n + \frac{h^4}{12}\dddot f_n + O(h^5).$$

**Exact expansion.** Since $y' = f$, $y'' = \dot f$, $y''' = \ddot f$, $y^{(4)} = \dddot f$:

$$y(t_{n+1}) = y_n + hf_n + \frac{h^2}{2}\dot f_n + \frac{h^3}{6}\ddot f_n + \frac{h^4}{24}\dddot f_n + O(h^5).$$

**Difference.** Subtracting the numerical from the exact:

$$y(t_{n+1}) - \Bigl[y_n+\frac h2(3f_n-f_{n-1})\Bigr] = h^3\Bigl(\frac16+\frac14\Bigr)\ddot f_n + O(h^4) = \frac{5}{12}h^3y'''(t_n) + O(h^4).$$

So the local truncation error is $\frac{5}{12}h^2y''' + O(h^3)$ in the $\tau$ convention, i.e. the local error is $\frac{5}{12}h^3y'''$, and the method has order $2$: the $h$ and $h^2$ terms match exactly, the $h^3$ term does not. $\blacksquare$

*Check against the table.* The local error constant $5/12 \approx 0.417$ is smaller than Euler's $1/2$ but larger than Heun's (whose local error is $-\frac{1}{12}h^3y'''$ times a combination) — consistent with AB2 being comparable to, but slightly worse than, a good second-order one-step method at the same step.

### Solution 30

**Stability function.** Apply $y_{n+1} = y_n + \frac h2\bigl(\lambda y_n + \lambda y_{n+1}\bigr)$:

$$y_{n+1}\Bigl(1-\frac z2\Bigr) = y_n\Bigl(1+\frac z2\Bigr) \quad\Longrightarrow\quad R(z) = \frac{1+z/2}{1-z/2}, \qquad z = h\lambda .$$

**A-stability.** For $z = x+iy$ with $x = \operatorname{Re}z$,

$$\lvert 1+z/2\rvert^2 = \Bigl(1+\frac x2\Bigr)^2 + \frac{y^2}{4}, \qquad \lvert 1-z/2\rvert^2 = \Bigl(1-\frac x2\Bigr)^2 + \frac{y^2}{4}.$$

The difference is $\bigl(1+x+\frac{x^2}{4}\bigr) - \bigl(1-x+\frac{x^2}{4}\bigr) = 2x$. Hence

$$\lvert R(z)\rvert \le 1 \iff 2x \le 0 \iff \operatorname{Re}z \le 0 .$$

The stability region is exactly the closed left half-plane, so the trapezoidal rule is A-stable ✓. (The denominator vanishes only at $z=2$, which is outside the left half-plane, so $R$ is analytic there.)

**The imaginary axis.** If $z = iy$ then $\lvert1+iy/2\rvert = \sqrt{1+y^2/4} = \lvert1-iy/2\rvert$, so $\lvert R(iy)\rvert = 1$ for every real $y$: the method is **neutrally stable** for oscillations. Numerically this is a double-edged property:

* Good: a conservative system (a harmonic oscillator, a wave equation) is integrated without artificial damping, so the energy does not drift.
* Bad: a stiff problem whose fast mode has died has no mechanism to damp the numerical ringing; the trapezoidal rule can leave a spurious oscillating component that never decays, which is why stiff solvers often switch to a damped method such as implicit Euler or a BDF formula after a step that follows a discontinuity.

*Check.* $R(z)$ is the [1/1] Padé approximant of $e^z$: its Taylor expansion is $1+z+\frac{z^2}{2}+\frac{z^3}{4}+\cdots$, matching $e^z$ through the $z^2$ term — which is exactly the statement that the method is second order ✓.

### Solution 31

**Claim.** No explicit Runge–Kutta method is A-stable.

*Proof.* For an explicit Runge–Kutta method the stability function is a polynomial: applying the method to $y'=\lambda y$ gives

$$y_{n+1} = R(z)y_n, \qquad R(z) = 1 + z\sum_i b_i + z^2\sum_{i,j}b_ia_{ij} + \cdots + z^s\sum b_i a_{ij}a_{jk}\cdots,$$

a polynomial of degree at most $s$ with $R(0) = 1$. Consistency requires $\sum_i b_i = 1$, so the coefficient of $z$ is $1$ and $R$ is **not** the constant polynomial $1$: it has degree $d\ge1$ and leading coefficient $c_d \ne 0$.

Now let $z = -x$ with $x>0$ real and let $x\to+\infty$. Then

$$R(-x) = c_d(-x)^d + O(x^{d-1}) \quad\Longrightarrow\quad \lvert R(-x)\rvert \to \infty .$$

So there exist arbitrarily large $x>0$ with $\lvert R(-x)\rvert>1$. Since $-x$ lies in the left half-plane, the stability region does not contain the left half-plane, and the method is not A-stable. $\blacksquare$

*Where polynomiality is used.* In the growth statement $\lvert R(-x)\rvert\to\infty$. A rational $R$ can stay bounded (implicit Euler: $R = 1/(1-z)\to0$; trapezoidal: $R\to-1$). A polynomial cannot, because its leading term dominates.

*Remark.* The argument shows slightly more: for an explicit method the stability region is bounded (it lies inside the disc $\lvert z\rvert\le\max\{x : \lvert R(-x)\rvert\le1\}$ plus a bounded set), so it cannot even contain a large sector of the left half-plane.

### Solution 32

**Truncation error of the central second difference.** Let $y$ be four times continuously differentiable. Taylor's theorem gives

$$y(t+h) = y + hy' + \frac{h^2}{2}y'' + \frac{h^3}{6}y''' + \frac{h^4}{24}y^{(4)} + O(h^5),$$
$$y(t-h) = y - hy' + \frac{h^2}{2}y'' - \frac{h^3}{6}y''' + \frac{h^4}{24}y^{(4)} + O(h^5).$$

Adding, the odd-order terms cancel:

$$y(t+h) + y(t-h) = 2y + h^2y'' + \frac{h^4}{12}y^{(4)} + O(h^6).$$

Therefore

$$\frac{y(t+h) - 2y(t) + y(t-h)}{h^2} = y''(t) + \frac{h^2}{12}y^{(4)}(t) + O(h^4),$$

so the approximation is second order, with truncation error $\frac{h^2}{12}y^{(4)}$.

**Consequence for the BVP scheme.** Substituting $y'' = p y' + q y + r$ and using central differences for $y'$ (also second order) gives a local residual of $O(h^2)$ at every interior node. The discrete solution therefore satisfies a perturbed difference equation whose forcing is $O(h^2)$; the discrete maximum principle (the coefficient matrix is an M-matrix when $q\le0$) converts that into a solution error of the same order. Hence the scheme is second-order accurate ✓ — as the table in README §7.8 confirms, with errors falling by a factor $4$ at each halving.

*Exactness for cubics.* If $y$ is a cubic then $y^{(4)} = 0$, so the formula is exact. This is why $y''=2$ with $y=t^2$ is solved to round-off (README §7.8) — a useful unit test for an implementation.

## Challenge

### Solution 33

**Setup.** Put $s = (t-t_n)/h$, so the nodes $t_n, t_{n-1}, t_{n-2}$ correspond to $s = 0, -1, -2$, and the target interval $[t_n,t_{n+1}]$ to $s\in[0,1]$. The Lagrange basis polynomials on the three nodes are

$$L_0(s) = \frac{(s+1)(s+2)}{(0+1)(0+2)} = \frac{(s+1)(s+2)}{2}, \qquad L_{-1}(s) = \frac{s(s+2)}{(-1)(1)} = -s(s+2),$$
$$L_{-2}(s) = \frac{s(s+1)}{(-2)(-1)} = \frac{s(s+1)}{2}.$$

Each has the value $1$ at its own node and $0$ at the other two.

**Integration.** With $f$ replaced by its interpolant, $\int_{t_n}^{t_{n+1}}f\,dt \approx h\int_0^1\sum_j L_j(s)f_j\,ds$, and the weights are

$$\beta_0 = \int_0^1\frac{(s+1)(s+2)}{2}\,ds = \frac12\int_0^1\bigl(s^2+3s+2\bigr)ds = \frac12\Bigl(\frac13+\frac32+2\Bigr) = \frac{23}{12},$$
$$\beta_{-1} = -\int_0^1\bigl(s^2+2s\bigr)ds = -\Bigl(\frac13+1\Bigr) = -\frac43 = -\frac{16}{12},$$
$$\beta_{-2} = \int_0^1\frac{s^2+s}{2}\,ds = \frac12\Bigl(\frac13+\frac12\Bigr) = \frac{5}{12}.$$

Hence

$$y_{n+1} = y_n + \frac h{12}\bigl(23f_n - 16f_{n-1} + 5f_{n-2}\bigr). \qquad \blacksquare$$

**Exactness checks.** Write $t = t_n+sh$ and test $f = 1, t, t^2$; the integral $\int_0^1 f\,ds$ multiplied by $h$ must equal the weighted sum.

* $f = 1$: exact $h$; numerical $h\frac{23-16+5}{12} = h$ ✓.
* $f = t_n+sh$: exact $h\bigl(t_n+\frac h2\bigr)$; numerical $h\frac{23t_n - 16(t_n-h) + 5(t_n-2h)}{12} = h\bigl(t_n + \frac{6h}{12}\bigr) = h\bigl(t_n+\frac h2\bigr)$ ✓.
* $f = (t_n+sh)^2$: exact $h\bigl(t_n^2+t_nh+\frac{h^2}{3}\bigr)$; numerical $\frac h{12}\bigl[23t_n^2 - 16(t_n-h)^2 + 5(t_n-2h)^2\bigr]$. The coefficients give $t_n^2(23-16+5)/12 = t_n^2$, $t_nh(32-20)/12 = t_nh$, $h^2(-16+20)/12 = h^2/3$ ✓.

Exactness for polynomials of degree $\le2$ with three nodes is the signature of a third-order method: the leading error involves $f'''$.

### Solution 34

**Model.** With truncation error $Ch$ (first order for Euler) and round-off accumulating as $\varepsilon/h$ over $1/h$ steps (each step contributes a relative round-off $\varepsilon$, and the errors add incoherently; the worst case gives $\varepsilon/h$, the root-sum-square case gives $\varepsilon/\sqrt h$; take the worst case as stated), the total error is

$$E(h) = Ch + \frac{\varepsilon}{h} .$$

**Minimum.** $E'(h) = C - \varepsilon/h^2 = 0$ gives

$$h_* = \sqrt{\frac{\varepsilon}{C}}, \qquad E(h_*) = 2\sqrt{C\varepsilon} .$$

**Numbers.** With $C = 2.6$ and $\varepsilon = 10^{-16}$:

$$h_* = \sqrt{\frac{10^{-16}}{2.6}} = \sqrt{3.846\times10^{-17}} = 6.20\times10^{-9}, \qquad E_{\min} = 2\sqrt{2.6\times10^{-16}} = 3.22\times10^{-8} .$$

*Interpretation.* No first-order method can do better than about $3\times10^{-8}$ on this problem in double precision, no matter how small the step. Pushing $h$ below $6\times10^{-9}$ makes the answer *worse*. The cure is a higher-order method: for order $p$ the truncation term is $C h^p$ and the optimum is $h_* = (\varepsilon/(pC))^{1/(p+1)}$, so RK4 ($p=4$) reaches $h_*\approx(\varepsilon/(4C))^{1/5}$ and an error of order $\varepsilon^{4/5}\sim10^{-13}$.

*Check.* At $h = h_*$ the two terms are equal: $2.6\times6.20\times10^{-9} = 1.61\times10^{-8}$ and $10^{-16}/6.20\times10^{-9} = 1.61\times10^{-8}$ ✓.

### Solution 35

**Claim.** No two-stage explicit Runge–Kutta method has order $3$.

*Proof.* A two-stage explicit method has $c_1 = 0$, $c_2 = a_{21}$, and the three order-3 conditions of README §7.3 are

$$\text{(i) } b_1+b_2 = 1, \qquad \text{(ii) } b_2c_2 = \frac12, \qquad \text{(iii) } \sum_i b_ic_i^2 = \frac13, \qquad \text{(iv) } \sum_{i,j}b_ia_{ij}c_j = \frac16 .$$

From (iii), since $c_1 = 0$: $b_2c_2^2 = \frac13$. Dividing by (ii): $c_2 = \frac{1/3}{1/2} = \frac23$, whence $b_2 = \frac{1/2}{2/3} = \frac34$ and $b_1 = \frac14$.

Now evaluate (iv). The double sum is

$$\sum_{i,j}b_ia_{ij}c_j = b_1\bigl(a_{11}c_1 + a_{12}c_2\bigr) + b_2\bigl(a_{21}c_1 + a_{22}c_2\bigr) = 0 + 0 + b_2a_{21}c_1 + 0 = 0,$$

because $a_{11} = a_{12} = a_{22} = 0$ (explicit method) and $c_1 = 0$. Condition (iv) requires $1/6 \ne 0$ — a contradiction. Hence no such method exists. $\blacksquare$

*The general barrier.* The same argument generalises: an explicit $s$-stage method has $c_i$ built from $i-1$ previous stages, and the order conditions of order $s+1$ involve a chain of $s$ matrix entries $a_{ij}$ that must vanish for an explicit method, forcing $0 = $ a nonzero constant. This is the Butcher barrier: order $p$ requires $s\ge p$, and for $p\ge5$ strictly more stages than $p$.

### Solution 36

**The theta method.** $y_{n+1} = y_n + h\bigl[\theta f(t_{n+1},y_{n+1}) + (1-\theta)f(t_n,y_n)\bigr]$, with $\theta\in[0,1]$.

**Stability function.** On $y'=\lambda y$, $z = h\lambda$:

$$y_{n+1} = y_n + z\bigl[\theta y_{n+1} + (1-\theta)y_n\bigr] \;\Longrightarrow\; y_{n+1}(1-\theta z) = y_n\bigl(1+(1-\theta)z\bigr),$$

$$R(z) = \frac{1+(1-\theta)z}{1-\theta z}.$$

**Order.** Expand for small $z$:

$$R(z) = \bigl(1+(1-\theta)z\bigr)\bigl(1+\theta z+\theta^2z^2+\cdots\bigr) = 1 + z + \theta z^2 + O(z^3).$$

Compare with $e^z = 1+z+\frac{z^2}{2}+O(z^3)$. The $z^0$ and $z^1$ terms always match (the method is at least first order); the $z^2$ term matches exactly when

$$\theta = \frac12 .$$

So the method has order $2$ for $\theta = \frac12$ and order $1$ otherwise.

**A-stability.** Compute

$$\lvert 1+(1-\theta)z\rvert^2 - \lvert 1-\theta z\rvert^2 \quad\text{with } z = x+iy .$$

Expanding, the $y^2$ terms give $\bigl((1-\theta)^2-\theta^2\bigr)y^2 = (1-2\theta)y^2$ and the rest gives $2x + (1-2\theta)x^2$. Hence

$$\lvert R(z)\rvert \le 1 \iff 2x + (1-2\theta)\lvert z\rvert^2 \le 0 .$$

* If $\theta \ge \frac12$: the second term is $\le0$ and $2x<0$ throughout the left half-plane, so the inequality holds: **A-stable**.
* If $\theta < \frac12$: take $z = -x$ real with $x>0$ small; then $2(-x)+(1-2\theta)x^2 = -2x + O(x^2) > 0$ for sufficiently small $x$, so $\lvert R\rvert>1$: **not A-stable**.

Therefore the theta method is A-stable exactly for $\theta\in[\frac12,1]$ ✓.

**The three classical cases.**

| $\theta$ | Method | Order | A-stable |
|---|---|---|---|
| $0$ | explicit Euler | $1$ | no |
| $\frac12$ | trapezoidal rule (Crank–Nicolson) | $2$ | yes |
| $1$ | implicit Euler | $1$ | yes |

*Summary.* Among the theta methods, $\theta = \frac12$ is the only one that is both second order and A-stable — consistent with Dahlquist's first barrier, which allows A-stable multistep methods of order at most $2$. Values $\theta>\frac12$ are A-stable but only first order (and increasingly damped, approaching implicit Euler as $\theta\to1$), which is the usual reason for choosing a slightly larger $\theta$ in practice: the extra damping suppresses numerical ringing at the cost of order.

