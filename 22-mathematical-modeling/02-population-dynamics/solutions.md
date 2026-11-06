# Population Dynamics — Solutions

> [Population Dynamics](README.md) · Solutions to the 38 problems in [exercises.md](exercises.md)

Each solution states the strategy, carries out every significant step, and checks the answer by a second route where one is available. Numerical values are given to a precision justified by the data in the problem.

## Beginner

**1.** *Strategy: $t_d = \ln 2/r$, and the rule of 70 replaces $\ln 2 \approx 0.693$ by $0.70$ and $r$ by $100r$ per cent.*

| $r$ (yr⁻¹) | exact $\ln2/r$ | rule $70/(100r)$ | error |
|---|---|---|---|
| $0.01$ | $69.31$ yr | $70$ yr | $+1.0\%$ |
| $0.03$ | $23.10$ yr | $23.33$ yr | $+1.0\%$ |
| $0.10$ | $6.931$ yr | $7.0$ yr | $+1.0\%$ |

The rule's error is the error in $\ln 2 \approx 0.693$ approximated by $0.700$, i.e. about $1\%$ in every case, because the approximation is to the constant and not to the rate. Using $69.3$ instead of $70$ removes it.

**2.** *Strategy: invert $N(t) = N_0e^{rt}$ at the known ratio.*

Fivefold growth in 20 years gives $e^{20r} = 5$, so

$$r = \frac{\ln 5}{20} = \frac{1.60944}{20} = 0.080472\ \text{yr}^{-1},$$

and
$$t_d = \frac{\ln 2}{0.080472} = 8.613\ \text{yr}.$$

*Check.* In $20/8.613 = 2.322$ doublings the population grows by $2^{2.322} = 5.00$. $\checkmark$

**3.** *Strategy: count doublings, not hours.*

Six hours is $360$ minutes, hence $12$ doubling intervals of $30$ minutes. Starting from $100$ cells:

$$N = 100\cdot 2^{12} = 100\times4096 = 409{,}600 .$$

To exceed one million we need $100\cdot2^n > 10^6$, i.e. $2^n > 10^4$. Since $2^{13} = 8192 < 10^4 < 16384 = 2^{14}$, the count first exceeds one million after $14$ intervals, i.e. after $7$ hours, at $1{,}638{,}400$ cells.

*Remark.* The model is exponential growth with $r = \ln 2/(0.5\ \text{h}) = 1.386$ h⁻¹. It cannot hold for long: a colony of that size exhausts any realistic medium within hours, which is why bacterial growth curves are logistic, not exponential, beyond the early phase.

**4.** *Strategy: put the numbers into the closed form and its derivatives.*

$K/N_0 = 500/20 = 25$, so

$$N(t) = \frac{500}{1 + 24e^{-0.3t}} .$$

(a) At $t=10$: $e^{-3} = 0.049787$, $24\times0.049787 = 1.19489$, denominator $2.19489$, so
$$N(10) = \frac{500}{2.19489} = 227.8 .$$

(b) $t_{\text{infl}} = \frac{1}{r}\ln\frac{K-N_0}{N_0} = \frac{\ln 24}{0.3} = \frac{3.17805}{0.3} = 10.5935$ years, at which $N = K/2 = 250$.

(c) The growth rate is maximal at $N = K/2$ and equals $rK/4 = 0.3\times500/4 = 37.5$ individuals per year.

*Consistency check.* $t = 10$ is just before the inflection, and $N(10) = 227.8$ is just below $250$. It should be: at the inflection time of $10.59$ the population is exactly $250$.

**5.** *Strategy: the logistic solution depends on $K$ only through the dimensionless ratio $K/N_0$.*

With $K = 1000$ and $N_0 = 100$, the constant in the solution is $(K-N_0)/N_0 = 9$, so

$$N(t) = \frac{1000}{1 + 9e^{-rt}} .$$

At $N = 200$: $1 + 9e^{-rt} = 1000/200 = 5$, so $9e^{-rt} = 4$ and

$$e^{-rt} = \frac{4}{9} \quad\Longrightarrow\quad rt = \ln\frac{9}{4} = 0.81093 .$$

The elapsed time from $N=100$ to $N=200$ is therefore $0.811/r$. (At $N=100$ the exponent satisfies $e^{-rt}=1$, i.e. $t=0$, as it must since $100 = N_0$.)

*Why $K$ drops out.* The logistic solution can be written

$$N(t) = \frac{N_0e^{rt}}{1 + \frac{N_0}{K}\left(e^{rt}-1\right)} ,$$

so the effect of $K$ enters only through $\varepsilon = N_0/K$. Doubling from $N_0$ to $2N_0$ while $\varepsilon$ is small is nearly free of $K$: the whole early curve is nearly exponential, and the time to a given *ratio* is $\ln(\text{ratio})/r$. The dependence on $K$ appears only when $N$ becomes comparable with $K$.

**6.** *Strategy: mark the zeros, record the sign of $f$ on each interval, and read the arrows.*

(a) $f(N) = N(1-N)(N-2)$, zeros $0,1,2$.

| Interval | $N$ | $1-N$ | $N-2$ | $f$ | Arrow |
|---|---|---|---|---|---|
| $N<0$ | $-$ | $+$ | $-$ | $+$ | right |
| $0<N<1$ | $+$ | $+$ | $-$ | $-$ | left |
| $1<N<2$ | $+$ | $-$ | $-$ | $+$ | right |
| $N>2$ | $+$ | $-$ | $+$ | $-$ | left |

So $N=0$ is stable (arrows converge from both sides), $N=1$ is unstable, $N=2$ is stable.

(b) $f(N) = (N-1)(3-N)$, zeros $1,3$. For $N<1$: $(-)(+)<0$, arrow left. For $1<N<3$: $(+)(+)>0$, arrow right. For $N>3$: $(+)(-)<0$, arrow left. So $N=1$ is unstable and $N=3$ is stable.

(c) $f(N) = N(2-N)$, zeros $0,2$: negative outside $[0,2]$, positive inside. $N=0$ unstable, $N=2$ stable.

*Derivative check.* For (b), $f'(N) = 4-2N$, so $f'(1) = 2>0$ (unstable) and $f'(3) = -2<0$ (stable), agreeing with the diagram. For (c), $f'(N) = 2-2N$: $f'(0)=2$, $f'(2)=-2$, agreeing.

**7.** *Strategy: use the closed form and take a limit; no differentiation of $f$ is needed.*

The solution with $N_0>0$ is

$$N(t) = \frac{K}{1 + Ce^{-rt}}, \qquad C = \frac{K - N_0}{N_0} > -1 .$$

Since $r>0$, $e^{-rt}\to0$ as $t\to\infty$, so $1 + Ce^{-rt}\to1$ and $N(t)\to K$. The convergence holds for every $N_0>0$:

* if $N_0<K$ then $C>0$ and $N$ increases to $K$;
* if $N_0=K$ then $C=0$ and $N\equiv K$;
* if $N_0>K$ then $-1<C<0$, and $N$ decreases to $K$, because the denominator is positive for all $t$ (it lies between $1+C>0$ and $1$).

So every positive initial population converges to $K$, which is global asymptotic stability on $(0,\infty)$. *Remark.* What this argument does not give is the *rate*; the derivative test supplies it, $\lvert N-K\rvert \sim \text{const}\cdot e^{-rt}$.

**8.** *Strategy: the MSY is the vertex of the growth parabola; the equilibria are its intersections with the horizontal line $H$.*

(a) $Y_{\mathrm{MSY}} = rK/4 = 0.2\times10^4/4 = 500$ individuals per year, attained at $N_{\mathrm{MSY}} = K/2 = 5000$.

(b) With $H = 400$,

$$N^2 - KN + \frac{KH}{r} = N^2 - 10^4N + \frac{10^4\times400}{0.2} = N^2 - 10^4N + 2\times10^7 = 0 .$$

The discriminant is $10^8 - 4(2\times10^7) = 2\times10^7$, whose square root is $4472.14$, so

$$N = \frac{10^4 \pm 4472.14}{2} = 7236.07 \quad\text{or}\quad 2763.93 .$$

*Check.* Sum $= 10^4 = K$ $\checkmark$; product $= 2.0\times10^7 = KH/r$ $\checkmark$. Since $H = 400 < 500 = Y_{\mathrm{MSY}}$, both roots exist and the larger one, $7236$, is stable.

**9.** *Strategy: the sign of the square root.*

Write $\Delta = K^2 - 4KH/r$. For $0<H<rK/4$ we have $0 < \Delta < K^2$, so $0 < \sqrt\Delta < K$. Hence

$$N_+ = \frac{K+\sqrt\Delta}{2} > \frac{K}{2}, \qquad N_- = \frac{K-\sqrt\Delta}{2} < \frac{K}{2} .$$

At $N_+$ we have $2N_+/K > 1$, so $f'(N_+) = r(1-2N_+/K)<0$ and $N_+$ is asymptotically stable; at $N_-$, $2N_-/K<1$, so $f'(N_-)>0$ and $N_-$ is unstable. At $H \to rK/4$, $\Delta\to0$ and both roots tend to $K/2$, where $f' = 0$: the fold.

**10.** *Strategy: solve $F(x)=x$ by factoring out $x$, then iterate.*

(a) $2x(1-x) = x$ gives $x(2 - 2x - 1) = x(1-2x) = 0$, so the nonzero fixed point is $x^* = 1/2$. With $F'(x) = 2-4x$, $F'(1/2) = 0$. A multiplier of zero is the strongest form of attraction: convergence is faster than linear in the neighbourhood (it is quadratic).

(b) Iterating from $0.1$:

| $t$ | $x_t$ |
|---|---|
| $0$ | $0.1000$ |
| $1$ | $0.1800$ |
| $2$ | $0.2952$ |
| $3$ | $0.4161$ |
| $4$ | $0.4859$ |

The sequence increases monotonically toward $0.5$, and the increments grow and then shrink as the fixed point is approached — the signature of a positive, decreasing multiplier (here the multiplier is $2-4x_t$, positive until $x_t = 0.5$). *Check:* $F(0.4161) = 2(0.4161)(0.5839) = 0.4859$ $\checkmark$.

**11.** *Strategy: compute the characteristic polynomial and examine the life-cycle graph.*

(a) $\det(L - \lambda I) = (0-\lambda)(0-\lambda) - 3(0.5) = \lambda^2 - 1.5$, so $\lambda = \pm\sqrt{1.5} = \pm1.22474$.

(b) Both eigenvalues have the same modulus, so $L$ is **not** primitive. The life-cycle graph has one loop, $0\to1\to0$, of length $2$, so the period is $2$.

(c) The population does not converge to a stable age distribution; instead the age structure oscillates with period $2$ for ever. Concretely, from $\mathbf n(0) = (1,0)$: $\mathbf n(1) = (0,0.5)$, $\mathbf n(2) = (1.5,0)$, $\mathbf n(3) = (0,0.75)$. The total is multiplied by $1.5$ every two steps (as $\lambda_1^2 = 1.5$ requires), but the fraction of juveniles alternates between $0$ and $1$.

**12.** *Strategy: set both rates to zero and solve.*

$$\dot x = 0 \Rightarrow x(a - by) = 0, \qquad \dot y = 0 \Rightarrow y(\delta x - c) = 0 .$$

The interior solution is $y^* = a/b = 1/0.02 = 50$ and $x^* = c/\delta = 0.4/0.004 = 100$.

*Check on the nullclines.* The $x$-nullcline is the horizontal line $y = a/b = 50$ (prey do not change there); the $y$-nullcline is the vertical line $x = c/\delta = 100$. Their intersection is $(100,50)$ $\checkmark$. Note that $x^*$ is set by predator parameters and $y^*$ by prey parameters.

**13.** *Strategy: differentiate, solve the stationary conditions, then examine the Hessian.*

(a) $H(x,y) = \delta x - c\ln x + by - a\ln y$, so

$$\frac{\partial H}{\partial x} = \delta - \frac{c}{x}, \qquad \frac{\partial H}{\partial y} = b - \frac{a}{y} .$$

(b) Both partials vanish only at $x = c/\delta$, $y = a/b$ — the interior equilibrium of §7.8. It is the unique stationary point, because each equation has exactly one positive solution.

(c) $H_{xx} = c/x^2 > 0$, $H_{yy} = a/y^2 > 0$ and $H_{xy} = 0$. The Hessian is diagonal with positive entries, hence positive definite everywhere on $x,y>0$; $H$ is strictly convex and the stationary point is the unique global minimum. This is what makes the level sets closed curves.

**14.** *Strategy: evaluate both invasion conditions, then check the interior formula.*

$\alpha K_2 = 0.8\times1500 = 1200 < K_1 = 2000$, so species $x$ has a positive growth rate when rare in a resident $y$ population: $x$ invades.

$\beta K_1 = 0.9\times2000 = 1800 > K_2 = 1500$, so species $y$ has a *negative* growth rate when rare: $y$ does not invade.

This is Case 3: $x$ excludes $y$. The interior formula confirms it — with $1-\alpha\beta = 1 - 0.72 = 0.28$,

$$\hat x = \frac{2000 - 1200}{0.28} = 2857.1, \qquad \hat y = \frac{1500 - 1800}{0.28} = -1071.4 < 0,$$

so there is no coexistence equilibrium in the positive quadrant. $\checkmark$ The equilibrium that is actually approached from any interior start is $(K_1, 0) = (2000,0)$.

## Intermediate

**15.** *Strategy: form the ratio of the logistic solution to the exponential and require it to exceed $0.95$.*

Write the logistic solution as

$$N(t) = \frac{N_0e^{rt}}{1 + \varepsilon\left(e^{rt}-1\right)}, \qquad \varepsilon = \frac{N_0}{K} = 0.01 .$$

The ratio to the exponential curve is

$$\frac{N(t)}{N_0e^{rt}} = \frac{1}{1+\varepsilon\left(e^{rt}-1\right)} .$$

Requiring this to be at least $0.95$:

$$1 + 0.01\left(e^{rt}-1\right) \le \frac{1}{0.95} = 1.05263 \;\Longrightarrow\; e^{rt}-1 \le 5.263 \;\Longrightarrow\; e^{rt} \le 6.263,$$

so $rt \le \ln 6.263 = 1.8348$, i.e. $t \le 1.835/r$.

*Interpretation.* The exponential approximation is accurate to $5\%$ while the population is below about $6.3N_0$ — roughly $2.6$ doublings. This is the quantitative form of the statement that the logistic equation is the exponential equation at low density: the *relative* error in the growth rate is $N/K$, so it stays small while $N \ll K$, but the population can grow by a factor of six before the error reaches $5\%$ when $N_0 = 0.01K$.

**16.** *Strategy: the growth parabola, the quadratic formula, then an inequality.*

(a) $Y_{\mathrm{MSY}} = rK/4 = 0.4\times2000/4 = 200$ per year, at $N = K/2 = 1000$.

(b) With $H = 150$:

$$N^2 - 2000N + \frac{2000\times150}{0.4} = N^2 - 2000N + 750{,}000 = 0 .$$

The discriminant is $4\times10^6 - 3\times10^6 = 10^6$, square root $1000$, so

$$N = \frac{2000 \pm 1000}{2} = 1500 \quad\text{or}\quad 500 .$$

The larger root, $1500$, is stable.

(c) The stable root is $(2000+\sqrt\Delta)/2$, where $\Delta = 4\times10^6 - 20\,000H$. Requiring it to be at least $0.7K = 1400$:

$$\sqrt\Delta \ge 800 \;\Longrightarrow\; 4\times10^6 - 20\,000H \ge 640{,}000 \;\Longrightarrow\; H \le \frac{3{,}360{,}000}{20\,000} = 168 .$$

So the largest quota consistent with a stock of at least $0.7K$ is $168$ per year, which is $84\%$ of the MSY.

**17.** *Strategy: $N^*(E) = K(1-qE/r)$, $Y = qEN^*$, and the critical effort is $r/q$.*

Here $E_c = r/q = 0.8/0.002 = 400$ and $E_{\mathrm{MSY}} = 200$.

| $E$ | $N^* = 5000(1 - 0.002E/0.8)$ | $Y = 0.002\,E\,N^*$ |
|---|---|---|
| $100$ | $3750$ | $750$ |
| $200$ | $2500$ | $1000$ |
| $300$ | $1250$ | $750$ |
| $400$ | $0$ | $0$ |

The symmetry $Y(100) = Y(300) = 750$ is not accidental: $Y(E) = qEK(1-qE/r)$ is a parabola symmetric about $E = r/(2q) = 200$.

*Check.* $Y(200) = 0.002\times200\times2500 = 1000 = rK/4 = 0.8\times5000/4$. $\checkmark$

**18.** *Strategy: zero profit gives the open-access stock directly.*

(a) At open access, profit is zero: $pqEN = cE$, so for $E>0$,

$$N_{oa} = \frac{c}{pq} = \frac{3000}{500\times10^{-4}} = \frac{3000}{0.05} = 60{,}000\ \text{tonnes}.$$

(b) As a fraction of $K$: $\theta = 6\times10^4/2\times10^6 = 0.03$, i.e. $3\%$ of the carrying capacity, against $50\%$ at the MSY. The open-access stock is one-seventeenth of the MSY stock.

*Remark.* The open-access yield here is $Y_{oa} = rK\theta(1-\theta) = rK(0.03)(0.97) = 0.0291\,rK$, against the MSY $0.25\,rK$: less than an eighth of the potential catch, taken from a stock that has been reduced to near-collapse. The example is deliberately extreme and shows why the ratio $c/(pqK)$ is the number that matters.

**19.** *Strategy: fixed point from $F(x)=x$, stability from the multiplier, then iterate.*

(a) $x^* = 1 - 1/2.8 = 0.642857$. The multiplier is

$$F'(x^*) = 2 - R = 2 - 2.8 = -0.8,$$

so $\lvert F'\rvert<1$: the fixed point is asymptotically stable, and the negative sign means the approach oscillates.

(b) Iterating from $0.3$:

| $t$ | $x_t$ |
|---|---|
| $0$ | $0.3000$ |
| $1$ | $0.5880$ |
| $2$ | $0.6783$ |
| $3$ | $0.6109$ |
| $4$ | $0.6656$ |
| $5$ | $0.6231$ |
| $6$ | $0.6576$ |

The odd iterates climb toward $0.6429$ from below and the even from above, with the gap shrinking by roughly the factor $0.8$ each step — exactly the multiplier. *Check:* $F(0.3) = 2.8(0.3)(0.7) = 0.588$ $\checkmark$.

**20.** *Strategy: the 2-cycle formula, then the multiplier formula, then a numerical confirmation.*

With $R = 3.4$, $(R-3)(R+1) = 0.4\times4.4 = 1.76$ and $\sqrt{1.76} = 1.32665$, so

$$x_\pm = \frac{4.4 \pm 1.32665}{6.8} = 0.84215 \quad\text{or}\quad 0.45196 .$$

*Check.* $F(0.84215) = 3.4(0.84215)(0.15785) = 0.45200$, which is $0.45196$ to four decimals. $\checkmark$

The multiplier is

$$\mu = 4 + 2(3.4) - 3.4^2 = 4 + 6.8 - 11.56 = -0.76,$$

so $\lvert\mu\rvert<1$: the cycle is attracting. Since $3.4 < 1+\sqrt6 = 3.44949$, this is the expected regime.

Numerically from $0.84$: $0.45696$, $0.84359$, $0.44860$, $0.83714$, $\dots$ — the oscillations settle onto the pair $\{0.84215, 0.45196\}$, with the error shrinking by about $0.76$ per two steps.

**21.** *Strategy: characteristic polynomial, then eigenvector, then Euler–Lotka as a check.*

(a) $\det(L-\lambda I) = (1.5-\lambda)(-\lambda) - 2(0.4) = \lambda^2 - 1.5\lambda - 0.8$, so

$$\lambda = \frac{1.5 \pm \sqrt{2.25 + 3.2}}{2} = \frac{1.5 \pm 2.33345}{2} = 1.91673 \quad\text{or}\quad -0.41673 .$$

Since $\lambda_1 = 1.91673 > 1$, the population grows by about $92\%$ per census.

(b) The second row of $L - \lambda_1I$ gives $0.4v_0 - \lambda_1v_1 = 0$, so $v_1/v_0 = 0.4/1.91673 = 0.20863$. Normalising,

$$\frac{\mathbf v}{\lVert\mathbf v\rVert_1} = \frac{(1,\ 0.20863)}{1.20863} = (0.82738,\ 0.17262) .$$

(c) Euler–Lotka: $1 = \frac{f_0}{\lambda} + \frac{f_1p_0}{\lambda^2} = \frac{1.5}{1.91673} + \frac{0.8}{3.67385} = 0.78258 + 0.21775 = 1.0003$. The discrepancy is rounding in $\lambda$; solving the equation exactly gives the same $\lambda$ as the characteristic polynomial, as it must.

**22.** *Strategy: solve for the equilibrium, multiply by $qE$, then complete the square.*

At equilibrium, $r(1 - N/K) = qE$, so $N^*(E) = K(1 - qE/r)$ and the sustainable yield is

$$Y(E) = qEN^*(E) = qEK\left(1 - \frac{qE}{r}\right) = qEK - \frac{q^2EK}{r}E .$$

This is a downward parabola in $E$ with roots at $E=0$ and $E = r/q$. Completing the square,

$$Y(E) = \frac{q^2K}{r}\left[\left(\frac{r}{2q}\right)^2 - \left(E - \frac{r}{2q}\right)^2\right],$$

so the maximum is at $E = r/(2q)$ with value

$$Y_{\max} = \frac{q^2K}{r}\cdot\frac{r^2}{4q^2} = \frac{rK}{4},$$

which is the same value as the MSY of §7.4, as it must be: both are the maximum of the growth rate $f(N)$.

**23.** *Strategy: the averages come from integrating the logarithmic rates; the period from the linearisation.*

(a) From $\dot x/x = a - by$, integrating over one period $T$ gives $0 = aT - b\int_0^Ty\,dt$, so $\bar y = a/b = 1/0.02 = 50$. Similarly $\bar x = c/\delta = 0.4/0.004 = 100$.

(b) $\omega = \sqrt{ac} = \sqrt{1\times0.4} = 0.63246$, so $T \to 2\pi/\omega = 9.9346$ time units.

(c) The averages are integrals of $\dot x/x$ and $\dot y/y$ over a closed orbit, and each integral of a total derivative over a period is exactly zero; the amplitude cancels between the two sides. The period, in contrast, is the time taken to traverse the orbit, which depends on the orbit's shape, and that shape changes with amplitude — the nonlinear restoring force is not proportional to displacement. For this system the period *increases* with amplitude.

**24.** *Strategy: solve the modified equilibrium conditions.*

With $\dot x = ax - bxy - hx = x(a - h - by)$ and $\dot y = \delta xy - cy = y(\delta x - c)$, the interior equilibrium is

$$x^* = \frac{c}{\delta} \quad\text{(unchanged)}, \qquad y^* = \frac{a - h}{b} \quad\text{(reduced)},$$

provided $h < a$; if $h \ge a$ the prey's net growth is non-positive and the predator goes extinct.

*Interpretation.* In this model, harvesting the prey harms only the predator: the prey equilibrium is set by the predator's death rate $c$ and conversion $\delta$, not by the prey's own growth rate, so removing prey does not change $x^*$ at all. This is a striking prediction and a **model artefact**: it depends on the absence of prey self-limitation. Add the logistic term to the prey (§7.8 and Exercise 37) and the prey equilibrium becomes $c/\delta$ still, but the prey *abundance trajectory* and the stability change; add a carrying capacity to the predator–prey pair and harvesting prey reduces prey as well. The exercise is a reminder that a counter-intuitive result can be a property of the assumption list rather than of the biology.

## Advanced

**25.** *Strategy: control $f$ by its derivative near the equilibrium, then use a differential inequality.*

**Theorem.** Let $f$ be continuously differentiable on an open interval $I$ containing an equilibrium $N^*$ of $\dot N = f(N)$.

1. If $f'(N^*)<0$ then $N^*$ is asymptotically stable.
2. If $f'(N^*)>0$ then $N^*$ is unstable.

**Proof of (1).** Put $c = -f'(N^*)>0$. *Here continuity of $f'$ is used:* it gives $\rho>0$ such that $\lvert N - N^*\rvert<\rho$ implies $f'(N)\le -c/2$ and $\rho$ is small enough that $(N^*-\rho, N^*+\rho)\subseteq I$.

Let $N_0$ satisfy $\lvert N_0-N^*\rvert<\rho$, and let $[0,T)$ be the maximal interval on which the solution stays inside $(N^*-\rho, N^*+\rho)$.

*Step 1: the solution stays inside.* For $N$ in the interval, the mean value theorem gives $f(N) = f'(\xi)(N-N^*)$ for some $\xi$ between $N$ and $N^*$, so

$$(N-N^*)f(N) = f'(\xi)(N-N^*)^2 \le -\frac{c}{2}(N-N^*)^2 \le 0 .$$

Hence $z(t) := (N(t)-N^*)^2$ is non-increasing on $[0,T)$, so $\lvert N(t)-N^*\rvert \le \lvert N_0-N^*\rvert < \rho$ and the solution can never reach the boundary of the interval. Therefore $T=\infty$: the solution exists for all $t\ge0$ and stays in the interval.

*Step 2: decay.* On $[0,\infty)$,

$$\frac{dz}{dt} = 2(N-N^*)f(N) \le -c\,z .$$

Dividing by $z>0$ (or applying Grönwall's inequality directly) and integrating from $0$ to $t$,

$$z(t) \le z(0)\,e^{-ct}, \qquad\text{i.e.}\qquad \lvert N(t)-N^*\rvert \le \lvert N_0-N^*\rvert\,e^{-ct/2} .$$

This gives both Lyapunov stability (take $\delta = \min(\rho,\varepsilon)$) and attraction. So $N^*$ is asymptotically stable. $\blacksquare$

**Proof of (2).** If $f'(N^*)>0$, continuity gives $\rho>0$ with $f'(N)\ge c/2>0$ on $(N^*-\rho,N^*+\rho)$, where $c = f'(N^*)>0$. For $N$ in that interval, $f(N) = f'(\xi)(N-N^*)$ has the same sign as $N-N^*$. Hence a solution starting at $N_0 \in (N^*, N^*+\rho)$ increases, and one starting in $(N^*-\rho,N^*)$ decreases; in both cases it moves away from $N^*$ and reaches distance $\rho$ in finite time (because $\lvert f\rvert \ge (c/2)\lvert N-N^*\rvert$ forces exponential separation). So for $\varepsilon = \rho/2$ no $\delta>0$ keeps every solution within $\varepsilon$ of $N^*$: the equilibrium is unstable. $\blacksquare$

*Remark.* Part (3) of the theorem in the tutorial is a statement about the *absence* of a conclusion: at $f'(N^*)=0$ the sign of $f$ must be examined directly, and the examples $-N^3$, $N^3$ and $N^2$ show that both stability and instability occur.

**26.** *Strategy: convexity gives the geometry of the level sets; the differential equation gives invariance; Poincaré–Bendixson closes the argument.*

Throughout, work in the open positive quadrant $Q = \{(x,y): x>0, y>0\}$, and let

$$H(x,y) = \delta x - c\ln x + by - a\ln y .$$

*Step 1: $H$ is strictly convex.* $H_{xx} = c/x^2>0$, $H_{yy} = a/y^2>0$, $H_{xy}=0$, so the Hessian is positive definite at every point of $Q$.

*Step 2: unique minimum.* $\nabla H = 0$ means $\delta = c/x$ and $b = a/y$, i.e. $(x,y) = (c/\delta, a/b)$, which lies in $Q$. Since $H$ is strictly convex, a stationary point is the unique global minimum.

*Step 3: level sets are closed curves.* For $m$ the minimum value, the sublevel set $S_\alpha = \{H \le \alpha\}$ for $\alpha>m$ is closed and, by Step 2 and the growth of $H$ at the boundary of $Q$ ($-c\ln x\to+\infty$ as $x\to0^+$, $\delta x\to+\infty$ as $x\to\infty$, and likewise in $y$), bounded and contained in a compact subset of $Q$. Its boundary is $\{H = \alpha\}$.

Now fix a point $p$ on the level set and consider the ray from the minimum $m_0$ through $p$. The function $t\mapsto H(m_0 + t(p-m_0))$ is strictly convex on $[0,1]$, has derivative $0$ at $t=0$ (because the gradient vanishes at $m_0$), and hence is strictly increasing for $t>0$. So the ray meets the level set exactly once: each level set is star-shaped with respect to $m_0$ and closed, i.e. a simple closed curve.

*Step 4: orbits are invariant curves.* Along a solution, $\dot H = 0$ (verified in §7.8). So the orbit starting at any point of the level set $\{H=\alpha\}$ stays on it.

*Step 5: the orbit cannot terminate.* The equilibria in $Q$ are the single point $(c/\delta,a/b)$, which lies strictly inside every level set and not on any of them. A solution in a compact set with no interior equilibrium is defined for all $t$; its $\omega$-limit set is non-empty, compact and invariant, and contains no equilibrium. By the **Poincaré–Bendixson theorem** the $\omega$-limit set is then a periodic orbit. Since the orbit is confined to a single simple closed curve and a periodic orbit is a closed subset of it, the periodic orbit must be the whole level set.

Hence every solution with $x,y>0$ is periodic and its orbit is the level set of $H$ through its initial condition. $\blacksquare$

*Remark.* The proof fails if the prey have self-limitation, because then there is no first integral and no closed level curves; Exercise 37 shows that the equilibrium becomes a stable focus. This is the sense in which the neutral cycles are structurally fragile.

**27.** *Strategy: expand about the tangency.*

Write $N = K/2 + u$ and $H = rK/4 - \mu$, so $\mu$ is the distance of the quota below the MSY. Then

$$rN\left(1-\frac{N}{K}\right) = r\left(\frac{K}{2}+u\right)\left(\frac12 - \frac{u}{K}\right) = r\left(\frac{K}{4} - \frac{u^2}{K}\right),$$

where the two cross terms $\mp u/2$ have cancelled. Hence

$$\dot u = r\left(\frac{K}{4}-\frac{u^2}{K}\right) - \left(\frac{rK}{4}-\mu\right) = \mu - \frac{r}{K}u^2 .$$

*Equilibria.* Setting $\dot u = 0$ gives $u^2 = \mu K/r$: two equilibria $u = \pm\sqrt{\mu K/r}$ when $\mu>0$, one when $\mu=0$, none when $\mu<0$. In the original variables,

$$N = \frac{K}{2} \pm \sqrt{\frac{K}{r}\left(\frac{rK}{4} - H\right)} .$$

*Square-root singularity.* Differentiating,

$$\frac{dN}{dH} = \mp\frac{1}{2}\sqrt{\frac{K}{r}}\cdot\frac{1}{\sqrt{rK/4 - H}} \longrightarrow \infty \quad\text{as } H\uparrow \frac{rK}{4}.$$

*Vanishing return rate.* Linearising at the stable root, $f'(N) = -2ru/K = -2\sqrt{\mu r/K}$, which tends to $0$ as $\mu\downarrow0$. A perturbation $\eta$ from the equilibrium then obeys $\dot\eta \approx -2\sqrt{\mu r/K}\,\eta$, so the decay time diverges. Equivalently, the eigenvalue vanishes at the bifurcation, which is the definition of a saddle-node: the two equilibria exchange no stability (one is always stable, one always unstable) but annihilate.

**28.** *Strategy: sign analysis, then a one-variable maximisation.*

(a) With $r=1$, $K=1000$, $A=200$, $f(N) = \frac{1}{200}N(1-N/1000)(N-200)$. The zeros are $0$, $200$, $1000$. Sign: for $0<N<200$ the factor $(N-200)$ is negative while the others are positive, so $f<0$; for $200<N<1000$ all three factors are positive, so $f>0$; for $N>1000$, $(1-N/K)<0$ and $f<0$.

Derivatives:
$$f'(0) = \frac{1}{200}(1)(-200) = -1 <0 \text{ (stable)},$$
$$f'(200) = \frac{1}{200}(200)(1 - 0.2)(1) = 0.8 > 0 \text{ (unstable)},$$
$$f'(1000) = \frac{1}{200}(1000)\left(-\frac{1}{1000}\right)(800) = -4 <0 \text{ (stable)}.$$
So $0$ and $K$ are stable, $A = 200$ is the threshold. A population at $N = 100$ declines; at $N = 400$ it grows.

(b) The sustainable harvest is $\max f$ on $[A,K]$. Setting the derivative to zero:

$$\frac{1}{200}\left[\left(1-\frac{N}{K}\right)(N-A) + N\left(-\frac1K\right)(N-A) + N\left(1-\frac{N}{K}\right)\right] = 0 .$$

Expanding the bracket gives $2N - A - \frac{3N^2}{K} + \frac{2AN}{K} = 0$, i.e.

$$2N - 200 - 0.003N^2 + 0.4N = 0 \;\Longrightarrow\; 0.003N^2 - 2.4N + 200 = 0 .$$

The roots are

$$N = \frac{2.4 \pm \sqrt{5.76 - 2.4}}{0.006} = \frac{2.4\pm1.8330}{0.006} = 705.5 \quad\text{or}\quad 94.5 .$$

Only $705.5$ lies in $[A,K]$, and there $f$ is maximal. Its value is

$$f(705.5) = \frac{1}{200}(705.5)(0.2945)(505.5) = 525.1\ \text{per year},$$

against the plain-logistic MSY $rK/4 = 250$.

*Comment.* The Allee factor multiplies growth by $(N/A - 1)$, which exceeds $1$ for $N>2A$, so the maximum growth rate is higher than the logistic one. That is not good news for management: the same factor makes growth *negative* below $A$, so the stock must be kept far above $200$, and the harvest that is sustainable at $705$ is catastrophic at $150$.

**29.** *Strategy: multiply the two inequalities.*

*Case 1.* Suppose $K_1 > \alpha K_2$ and $K_2 > \beta K_1$. Multiplying (all quantities positive) gives $K_1K_2 > \alpha\beta K_1K_2$, and dividing by $K_1K_2>0$ gives $\alpha\beta<1$.

*Case 2.* Suppose $K_1 < \alpha K_2$ and $K_2 < \beta K_1$. The same multiplication gives $K_1K_2 < \alpha\beta K_1K_2$, hence $\alpha\beta>1$.

*Positivity of the interior equilibrium.*
$$\hat x = \frac{K_1-\alpha K_2}{1-\alpha\beta}, \qquad \hat y = \frac{K_2-\beta K_1}{1-\alpha\beta}.$$
In Case 1 both numerators are positive and $1-\alpha\beta>0$, so both coordinates are positive. In Case 2 both numerators are negative and $1-\alpha\beta<0$, so both coordinates are again positive. In Cases 3 and 4 one numerator is positive and the other negative with $1-\alpha\beta$ of a definite sign, so one coordinate is negative: no interior equilibrium in the positive quadrant.

*Stability.* $\det J = \frac{r_1r_2\hat x\hat y}{K_1K_2}(1-\alpha\beta)$ and $\operatorname{tr}J<0$. So the interior equilibrium is stable exactly when $\alpha\beta<1$, which by the first part is exactly Case 1. In Case 2, $\det J<0$: a saddle.

*Basins.* In Case 2 the boundary equilibria $(K_1,0)$ and $(0,K_2)$ are both stable (neither species can invade the other). The interior saddle has a one-dimensional stable manifold, which by the stable-manifold theorem is a curve crossing the positive quadrant and separating the two basins: initial conditions on one side converge to $(K_1,0)$ and on the other to $(0,K_2)$. This is **founder control** — the outcome is decided by which species is initially more abundant, not by the parameters alone.

**30.** *Strategy: compute $F^2(x)-x$ and factor out the fixed points.*

(a) With $F(x) = Rx(1-x)$,

$$F(F(x)) = R\,F(x)\left(1-F(x)\right) = R\left[Rx(1-x)\right]\left[1 - Rx(1-x)\right] = R^2x(1-x)\left(1 - Rx + Rx^2\right).$$

So the equation $F^2(x) = x$ is

$$x\left[R^2(1-x)\left(1 - Rx + Rx^2\right) - 1\right] = 0 .$$

The bracket expands to $-R^3x^3 + 2R^3x^2 - R^2(R+1)x + (R^2-1)$. Since $x = 1-1/R$ is a fixed point of $F$ it is a root of the bracket, and dividing by $x - (1 - 1/R)$ gives

$$-R^3x^3 + 2R^3x^2 - R^2(R+1)x + (R^2-1) = -R\left(x - 1 + \frac1R\right)\left(R^2x^2 - R(R+1)x + (R+1)\right).$$

(Check: the leading coefficient is $-R\cdot R^2 = -R^3$ and the constant term is $-R\cdot\left(-1+\frac1R\right)(R+1) = (R-1)(R+1) = R^2-1$, both as required.) The quadratic gives

$$R^2x^2 - R(R+1)x + (R+1) = 0 \;\Longrightarrow\; x = \frac{R(R+1)\pm\sqrt{R^2(R+1)^2 - 4R^2(R+1)}}{2R^2},$$

which simplifies, after dividing numerator and denominator by $R$, to

$$x_\pm = \frac{R+1\pm\sqrt{(R+1)(R-3)}}{2R} .$$

The roots are real exactly when $R\ge3$.

(b) The multiplier is

$$\mu = F'(x_+)F'(x_-) = R^2(1-2x_+)(1-2x_-) = R^2\left[1 - 2(x_++x_-) + 4x_+x_-\right].$$

Using $x_++x_- = (R+1)/R$ and $x_+x_- = (R+1)/R^2$,

$$\mu = R^2 - 2R(R+1) + 4(R+1) = R^2 - 2R^2 - 2R + 4R + 4 = 4 + 2R - R^2 .$$

*Check at $R=3$:* the two roots merge at $x = 2/3$ and $\mu = 4+6-9 = 1$, consistent with the birth of a cycle from a fixed point whose multiplier has just passed $-1$ (the product of multipliers of the newborn cycle equals $1$ at birth).

**31.** *Strategy: write the solution with the inflection time as the origin, then use the addition formula for $\tanh$.*

Put $z = r(t - t_{\text{infl}})$ and $C = (K-N_0)/N_0 > 0$ (the case $N_0<K$). Since $t_{\text{infl}} = \ln C/r$, we have $Ce^{-rt} = e^{-z}$, so

$$N = \frac{K}{1+e^{-z}} .$$

Now use
$$\frac{1}{1+e^{-z}} = \frac{e^{z/2}}{e^{z/2}+e^{-z/2}} = \frac{\cosh(z/2)+\sinh(z/2)}{2\cosh(z/2)} = \frac12\left(1+\tanh\frac z2\right).$$

Substituting,

$$N(t) = \frac{K}{2}\left[1 + \tanh\left(\frac{r}{2}\left(t - t_{\text{infl}}\right)\right)\right].$$

*Antisymmetry.* $\tanh$ is odd, so for any $s$,
$$N(t_{\text{infl}}+s) + N(t_{\text{infl}}-s) = \frac K2\left[2 + \tanh\frac{rs}{2} + \tanh\left(-\frac{rs}{2}\right)\right] = K .$$
So the logistic curve is point-symmetric about $(t_{\text{infl}}, K/2)$: the growth before the inflection mirrors the saturation after it. This is the analytic form of the S-shape, and it also shows that half the total growth from $N_0$ to $K$ happens before $t_{\text{infl}}$ and half after.

**32.** *Strategy: zero profit, then a one-variable inequality.*

At open access, effort enters until profit is zero. Profit at equilibrium is

$$\Pi(E) = pqEK\left(1 - \frac{qE}{r}\right) - cE = E\left[pqK\left(1-\frac{qE}{r}\right) - c\right].$$

For $E>0$, $\Pi=0$ requires

$$pqK\left(1-\frac{qE}{r}\right) = c \;\Longrightarrow\; 1 - \frac{qE_{oa}}{r} = \frac{c}{pqK} =: \theta .$$

Since $N^* = K(1-qE/r)$, the open-access stock is

$$N_{oa} = \theta K = \frac{c}{pq},$$

which depends only on the ratio of cost to price times catchability. The corresponding effort is $E_{oa} = \frac{r}{q}(1-\theta)$, positive because $\theta<1$.

The yield at open access is

$$Y_{oa} = qE_{oa}N_{oa} = r(1-\theta)\cdot\theta K = rK\,\theta(1-\theta).$$

Since $\theta(1-\theta) = \frac14 - \left(\theta-\frac12\right)^2 \le \frac14$ for all real $\theta$, with equality exactly at $\theta = 1/2$,

$$Y_{oa} \le \frac{rK}{4} = Y_{\mathrm{MSY}},$$

with equality if and only if $c/(pqK) = 1/2$. $\blacksquare$

*Interpretation.* Open access never beats the MSY in this model, and it always dissipates the rent, since the sole owner's profit is positive whenever $c>0$. The case $\theta = 1/2$ is the one in which the open-access stock happens to equal the MSY stock; it is a coincidence of parameters, not a design.

## Challenge

**33.** *Strategy: differentiate the stable root and normalise.*

With $r=0.4$ and $K=2000$,

$$N^*(H) = \frac{K+\sqrt{K^2-4KH/r}}{2}, \qquad \frac{dN^*}{dH} = \frac{-K/r}{\sqrt{K^2-4KH/r}} = \frac{-5000}{\sqrt{4\times10^6 - 20\,000H}},$$

and $S_H = \frac{H}{N^*}\frac{dN^*}{dH}$.

| $H$ | $\sqrt{\cdot}$ | $N^*$ | $dN^*/dH$ | $S_H$ |
|---|---|---|---|---|
| $100$ | $1414.21$ | $1707.11$ | $-3.536$ | $-0.207$ |
| $150$ | $1000.00$ | $1500.00$ | $-5.000$ | $-0.500$ |
| $195$ | $316.23$ | $1158.11$ | $-15.811$ | $-2.662$ |

*Pattern.* $\lvert S_H\rvert$ grows without bound as $H\to 200 = Y_{\mathrm{MSY}}$; the growth is like $(200-H)^{-1/2}$, the square-root singularity of §7.4. At $H = 168$ (the quota that keeps the stock at $0.7K$ in Exercise 16) the value is $S_H = -0.75$, so a $1\%$ error in the quota produces $0.75\%$ error in the predicted stock.

*Management conclusion.* The model cannot support a precise prediction of the stock at a quota near the MSY, and no improvement in data quality can repair this, because the sensitivity is a property of the model's structure, not of the estimate. The defensible policy conclusion is to operate with an explicit margin — for instance, at a quota for which $\lvert S_H\rvert \le 1$ — and to state the margin as part of the policy rather than as a concession.

**34.** *Strategy: verify, iterate, interpret, then find the eigenvector.*

(a) Euler–Lotka with $f_0 = 0.2$, $f_1 = 1$, $f_2 = 1.2$, $p_0 = p_1 = 0.5$ and $\lambda = 1$:
$$1 = f_0 + f_1p_0 + f_2p_0p_1 = 0.2 + 0.5 + 0.3 = 1 . \checkmark$$
So $\lambda = 1$ is a root of the characteristic equation, and since the right side of the Euler–Lotka equation is strictly decreasing in $\lambda$, it is *the* positive root: $\lambda_1 = 1$.

(b) Starting from $\mathbf n(0) = (0,100,0)$:

| $t$ | $\mathbf n(t)$ | total |
|---|---|---|
| $0$ | $(0,\ 100,\ 0)$ | $100$ |
| $1$ | $(100,\ 0,\ 50)$ | $150$ |
| $2$ | $(80,\ 50,\ 0)$ | $130$ |
| $3$ | $(66,\ 40,\ 25)$ | $131$ |

*Check on the step from $t=1$ to $t=2$:* $n_0 = 0.2(100) + 1(0) + 1.2(50) = 20 + 60 = 80$; $n_1 = 0.5(100) = 50$; $n_2 = 0.5(0) = 0$. $\checkmark$

(c) The total rises from $100$ to $150$ (a $50\%$ increase) even though $\lambda_1 = 1$, because the initial vector is far from the stable age distribution: it contains no newborns and a large cohort of one-year-olds about to reproduce. The transient is not governed by $\lambda_1$ but by the whole spectrum, and the subdominant eigenvalues here have modulus close to $1$, so the transient is long. This is the discrete form of **population momentum**: a population with an unusually favourable age structure grows for a while even at replacement fertility.

(d) The eigenvector solves $(L-I)\mathbf v = 0$:
$$-0.8v_0 + v_1 + 1.2v_2 = 0,\qquad 0.5v_0 = v_1,\qquad 0.5v_1 = v_2 .$$
From the last two, $v_1 = 0.5v_0$ and $v_2 = 0.25v_0$; the first equation is then $-0.8 + 0.5 + 0.3 = 0$, consistent. So

$$\mathbf v = (1,\ 0.5,\ 0.25), \qquad \frac{\mathbf v}{\lVert\mathbf v\rVert_1} = (0.5714,\ 0.2857,\ 0.1429).$$

*Check.* At $t=3$ the proportions are $(0.504, 0.305, 0.191)$, moving toward $(0.571, 0.286, 0.143)$ — as they should, since the subdominant eigenvalues are complex with modulus below one and the approach oscillates.

**35.** *(open)* *Strategy: list the mechanisms that produce irregular series without chaos, then specify the analyses that would discriminate.*

An answer should contain the following.

*Alternative explanations.* (i) **Environmental noise**: a linear or stable model driven by autocorrelated environmental variation produces irregular series that mimic chaos, and the autocorrelation of the driver is easily mistaken for endogenous nonlinearity. (ii) **Observation error**: census counts of birds are noisy, and measurement error inflates apparent irregularity and can even create the appearance of density dependence where there is none. (iii) **A long transient or a stable cycle**: a damped oscillation with a period comparable to the record length, or a stable limit cycle with an incommensurate period, looks aperiodic in a 40-year window. (iv) **An exogenous driver with its own dynamics** — a predator, a disease, or a weather cycle — rather than endogenous feedback.

*Required analyses.* (1) A **state-space (hidden-process) fit** that separates process noise from observation error; a chaos claim based on a model with no observation-error term is not credible. (2) **Out-of-sample forecast skill**, with nonlinear models compared against a linear null; chaotic dynamics should show short-term predictability that decays exponentially, and the decay rate estimates the Lyapunov exponent. (3) **Nonlinearity tests** — for instance, a likelihood-ratio comparison of a nonlinear autoregression against a linear one, or a test based on the predictability of the sign of the next change. (4) **Sensitivity to record length**: split the series and check whether the conclusion survives. (5) A statement of the **parameter uncertainty**, since the estimate of a Lyapunov exponent from 40 points carries a very wide interval.

*Acceptable verdict.* It is legitimate to say "the data are consistent with a nonlinear model that may be chaotic, but 40 annual observations cannot distinguish chaos from noise"; it is not legitimate to assert chaos from an irregular plot.

**36.** *Strategy: a quota fixes the offtake, so the equilibrium solves the growth equation with $H = Q$.*

(a) With $r = 0.5$, $K = 10^6$ and $Q = 10^5$,

$$N^2 - 10^6N + \frac{10^6\times10^5}{0.5} = N^2 - 10^6N + 2\times10^{11} = 0 .$$

The discriminant is $10^{12} - 8\times10^{11} = 2\times10^{11}$, square root $4.4721\times10^5$, so

$$N = \frac{10^6 \pm 4.4721\times10^5}{2} = 7.236\times10^5 \quad\text{or}\quad 2.764\times10^5 .$$

Since $Q = 10^5 < rK/4 = 1.25\times10^5$, both roots are real; the stable one is $7.236\times10^5$ t.

(b) The ordering is: quota regime $7.24\times10^5$ > sole owner $6\times10^5$ > MSY stock $5\times10^5$ > open access $2\times10^5$. The quota of $10^5$ t is *below* the MSY catch of $1.25\times10^5$, and a quota below the MSY corresponds to *two* stocks; the manager must ensure the stock is on the upper branch, which is the practical content of the "two equilibria" problem.

(c) The two regimes fix different things. A quota fixes the **offtake** — the right-hand side of the growth equation — and the equilibrium stock is then whatever satisfies $f(N) = Q$: a modest quota supports a large stock. Open access fixes the **institutions**, and effort expands until profit vanishes, which pins the stock at $c/(pq)$ regardless of the biology. The same biology therefore produces different equilibria because the two policies constrain different variables; neither is "the" answer, which is why the institutional question is prior to the mathematical one.

**37.** *Strategy: solve for the equilibrium, then compute the Jacobian and its invariants.*

(a) With $\dot x = ax(1-x/K) - bxy = x\left[a(1-x/K) - by\right]$ and $\dot y = y(\delta x - c)$:

$$x^* = \frac{c}{\delta}, \qquad y^* = \frac{a}{b}\left(1 - \frac{x^*}{K}\right) = \frac{a}{b}\left(1 - \frac{c}{\delta K}\right),$$

positive exactly when $c < \delta K$, i.e. when the predator's break-even prey density is below the carrying capacity. If $c \ge \delta K$ the predator cannot persist and the prey settle at $K$.

(b) The Jacobian at $(x^*,y^*)$:

$$J_{11} = a\left(1 - \frac{2x^*}{K}\right) - by^* = a - \frac{2ax^*}{K} - a\left(1 - \frac{x^*}{K}\right) = -\frac{ax^*}{K},$$
$$J_{12} = -bx^* < 0, \qquad J_{21} = \delta y^* > 0, \qquad J_{22} = 0 .$$

Hence

$$\operatorname{tr}J = -\frac{ax^*}{K} < 0, \qquad \det J = -J_{12}J_{21} = bx^*\delta y^* > 0 .$$

Negative trace with positive determinant means both eigenvalues have negative real part, so the equilibrium is asymptotically stable — for every admissible choice of the parameters. (If $4\det J > (\operatorname{tr}J)^2$ the eigenvalues are complex and the approach is a damped oscillation; otherwise it is a stable node.)

(c) So any amount of prey self-limitation, however small, turns the centre into a stable focus: the cycles damp out and the equilibrium is approached. The neutral cycles of the original model are therefore destroyed by an arbitrarily small perturbation of the structure — the technical meaning of **structural instability**. This is the reason ecologists do not expect to see exact Lotka–Volterra cycles in nature, and the reason the observation of persistent cycles is evidence for something else (seasonal forcing, a limit cycle from a nonlinear functional response, or noise).

**38.** *Strategy: the conjugacy converts iteration into arithmetic; count solutions of a congruence.*

(a) With $s = \sin(\pi\theta)$, $c = \cos(\pi\theta)$,
$$4\sin^2(\pi\theta)\cos^2(\pi\theta) = \left(2\sin(\pi\theta)\cos(\pi\theta)\right)^2 = \sin^2(2\pi\theta),$$
using $\sin 2\alpha = 2\sin\alpha\cos\alpha$ with $\alpha = \pi\theta$.

Now let $x = \sin^2(\pi\theta)$ for $\theta\in[0,1]$. Then
$$4x(1-x) = 4\sin^2(\pi\theta)\cos^2(\pi\theta) = \sin^2(2\pi\theta) = \sin^2\left(\pi\,(2\theta)\right),$$
so if $x_t = \sin^2(\pi\theta_t)$ then $x_{t+1} = \sin^2(\pi\theta_{t+1})$ with $\theta_{t+1} \equiv 2\theta_t \pmod 1$. The map $\theta\mapsto\sin^2(\pi\theta)$ is surjective onto $[0,1]$, so the diagram commutes and $f(x) = 4x(1-x)$ is conjugate (semi-conjugate, and a conjugacy after identifying $\theta$ with $1-\theta$) to the doubling map.

(b) $f^n(x) = \sin^2(2^n\pi\theta)$, so $f^n(x) = x$ means
$$\sin^2(2^n\pi\theta) = \sin^2(\pi\theta) \iff 2^n\pi\theta \equiv \pm\pi\theta \pmod{\pi} \iff 2^n\theta \equiv \pm\theta \pmod 1 .$$
*Plus sign:* $(2^n-1)\theta\in\mathbb{Z}$, giving the $2^n-1$ values $\theta = k/(2^n-1)$, $k = 0,\dots,2^n-2$.
*Minus sign:* $(2^n+1)\theta\in\mathbb{Z}$, giving the $2^n+1$ values $\theta = k/(2^n+1)$, $k=0,\dots,2^n$.
The two lists share only $\theta = 0$, and the identification $\theta\leftrightarrow1-\theta$ (which does not change $x$) pairs the remaining points, so the number of distinct fixed points of $f^n$ in $[0,1]$ is
$$\frac{(2^n-1)-1}{2} + \frac{(2^n+1)-1}{2} + 1 = 2^n .$$

*Point counts.* Let $a_n$ be the number of points of exact period $n$. Every point fixed by $f^n$ has exact period dividing $n$, so $2^n = \sum_{d\mid n}a_d$. Hence

$$a_1 = 2^1 = 2, \quad a_2 = 2^2 - a_1 = 2, \quad a_3 = 2^3 - a_1 = 6, \quad a_4 = 2^4 - a_1 - a_2 = 12 .$$

So $f(x) = 4x(1-x)$ has exactly $2$ fixed points ($x=0$ and $x=3/4$), one 2-cycle, two 3-cycles and three 4-cycles.

(c) The periodic points are $\theta = k/(2^n\pm1)$, and a point of exact period $n$ is a fixed point of $f^n$ with least such $n$. For any open interval $I\subseteq[0,1]$ there are integers $n$ large enough and $k$ such that $k/(2^n-1)\in I$ with the corresponding $\theta$ not identified with another point of $I$; hence periodic points lie in every interval, i.e. they are dense. Together with the topological transitivity of the doubling map (every interval is eventually mapped onto $[0,1]$) this gives two of Devaney's three conditions, and sensitivity follows.

