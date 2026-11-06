# First-Order Differential Equations — Solutions

> [First-Order Differential Equations](README.md) · Solutions to the 34 problems in [exercises.md](exercises.md)

Each solution states the strategy, carries out every step, and verifies the answer by substituting it
back into the equation. Where a division occurred, the lost solutions are listed explicitly; where an
interval is part of the answer, it is given.

## Beginner

**1.** *(a)* $y' + x^{2}y = e^{x}$: highest derivative $y'$, so **order 1**; $y$ and $y'$ appear linearly with coefficients depending on $x$, so **linear**; $x$ appears explicitly, so **not autonomous**.

*(b)* $y' = y^{2} - t$: **order 1**; the term $y^{2}$ makes it **nonlinear**; $t$ appears explicitly, so **not autonomous**. (It is autonomous in neither variable: the right side depends on $t$, and the unknown is $y$.)

*(c)* $t\,y' + y = \sin t$: **order 1**; dividing by $t$ (on $t \ne 0$) gives $y' + \frac{1}{t}y = \frac{\sin t}{t}$, so it is **linear**; $t$ appears explicitly, so **not autonomous**.

*(d)* $y'' - y = 0$: **order 2**; **linear**; no $t$ appears, so **autonomous**.

The point of the exercise is that "order", "linear" and "autonomous" are independent labels: an equation can be linear and non-autonomous (a, c), nonlinear and non-autonomous (b), or linear and autonomous of second order (d).

*Check of the labels by the superposition test.* A linear operator must satisfy $L[2y] = 2L[y]$. For (a), $L[y] = y' + x^{2}y$: $L[2y] = 2y' + 2x^{2}y = 2L[y]$ ✓. For (b), $L[y] = y'' + y^{2}$: with $y \equiv 1$ we get $L[1] = 1$, but $L[2] = 4 \ne 2\cdot1$ ✗ — exactly the failure of linearity. For (d), $L[y] = y'' - y$ satisfies $L[c_{1}y_{1} + c_{2}y_{2}] = c_{1}L[y_{1}] + c_{2}L[y_{2}]$ ✓, so linearity is independent of whether the right side vanishes.

**2.** *Strategy: the right side factors as $3x^{2} \cdot y$, so the equation is separable.*

The factor $h(y) = y$ vanishes at $y = 0$, giving the constant solution $y \equiv 0$, which does not meet the initial condition $y(0) = 2$. For $y \ne 0$,

$$\frac{dy}{y} = 3x^{2}\,dx \;\Longrightarrow\; \ln|y| = x^{3} + C \;\Longrightarrow\; |y| = e^{C}e^{x^{3}} .$$

Since $y(0) = 2 > 0$ and a solution cannot cross $0$ without violating uniqueness, $y > 0$ everywhere and $y = e^{C}e^{x^{3}}$. The initial condition gives $e^{C} = 2$, so

$$y = 2e^{x^{3}}, \qquad x \in \mathbb{R}.$$

*Check:* $y' = 2\cdot 3x^{2}e^{x^{3}} = 3x^{2}y$ ✓ and $y(0) = 2$ ✓. The formula is defined for every $x$ and never vanishes, so the maximal interval is $\mathbb{R}$.

**3.** *Strategy: the equation is separable; separate and integrate both sides.*

$$y\,\frac{dy}{dx} = x \;\Longrightarrow\; y\,dy = x\,dx \;\Longrightarrow\; \frac{y^{2}}{2} = \frac{x^{2}}{2} + C \;\Longrightarrow\; y^{2} - x^{2} = K .$$

The initial condition $y(0) = -2$ gives $4 - 0 = K$, so $y^{2} = x^{2} + 4$ and $y = \pm\sqrt{x^{2}+4}$.

*Why the lower branch:* the right side is at least $2$, so $y$ never vanishes; by continuity it keeps the sign of $y(0) = -2$. Hence

$$y = -\sqrt{x^{2}+4}, \qquad x \in \mathbb{R}.$$

*Check:* $y' = -\dfrac{x}{\sqrt{x^{2}+4}} = \dfrac{x}{y}$ ✓ and $y(0) = -2$ ✓.

*Remark:* the separated form contains no factor that can vanish, so no solution is lost; the sign ambiguity is resolved by the initial condition alone.

**4.** *Strategy: $e^{x-y} = e^{x}e^{-y}$ is a product of an $x$-part and a $y$-part, so separate.*

$$e^{y}\,\frac{dy}{dx} = e^{x} \;\Longrightarrow\; e^{y}\,dy = e^{x}\,dx \;\Longrightarrow\; e^{y} = e^{x} + C .$$

The initial condition $y(0) = \ln 2$ gives $e^{y(0)} = 2 = 1 + C$, so $C = 1$ and $e^{y} = e^{x} + 1$. Since $e^{x} + 1 > 0$ for all $x$, taking logarithms is legitimate for every $x$:

$$y = \ln\left(e^{x} + 1\right), \qquad x \in \mathbb{R}.$$

*Check:* $y' = \dfrac{e^{x}}{e^{x}+1}$ and $e^{x-y} = \dfrac{e^{x}}{e^{y}} = \dfrac{e^{x}}{e^{x}+1}$ ✓. Also $y(0) = \ln 2$ ✓.

*Remark:* had the initial condition been $y(0) = 0$, the constant would be $C = 0$ and the solution would be $y = \ln(e^{x}) = x$ — a useful sanity check, because $y' = 1$ and $e^{x-y} = e^{0} = 1$ agree.

**5.** *Strategy: separable with $h(y) = y^{2}$.*

$h$ vanishes only at $y = 0$, giving $y \equiv 0$, which does not satisfy $y(0) = 1$. For $y \ne 0$,

$$\frac{dy}{y^{2}} = \sin x\,dx \;\Longrightarrow\; -\frac{1}{y} = -\cos x + C \;\Longrightarrow\; \frac{1}{y} = \cos x + K .$$

The initial condition $1 = 1 + K$ gives $K = 0$, so $y = \sec x$. Because $\sec x$ is defined and nonzero exactly where $\cos x \ne 0$, and the initial point is $x = 0$, the interval is $\left(-\tfrac{\pi}{2},\,\tfrac{\pi}{2}\right)$:

$$y = \sec x, \qquad -\frac{\pi}{2} < x < \frac{\pi}{2}.$$

*Check:* $y' = \sec x\tan x$ and $y^{2}\sin x = \sec^{2}x\sin x = \dfrac{\sin x}{\cos^{2}x} = \sec x \cdot \dfrac{\sin x}{\cos x} = \sec x\tan x$ ✓. Also $y(0) = 1$ ✓.

*Remark:* at $x = \pm\pi/2$ the solution tends to $\pm\infty$, so it cannot be continued past the endpoints: the maximal interval is exactly the one stated.

**6.** *Strategy: factor out the $y$-dependence and record the zero of $h(y) = y^{3}$.*

The constant solution $y \equiv 0$ solves the equation. For $y \ne 0$,

$$\frac{dy}{y^{3}} = dx \;\Longrightarrow\; -\frac{1}{2y^{2}} = x + C \;\Longrightarrow\; y^{2} = -\frac{1}{2(x+C)},$$

which requires $x + C < 0$. Hence

$$y = \pm\frac{1}{\sqrt{-2(x+C)}}, \qquad x < -C,$$

and the complete solution set is these two branches together with $y \equiv 0$.

*Check:* for $y = \varepsilon\left(-2(x+C)\right)^{-1/2}$ with $\varepsilon = \pm 1$,

$$y' = \varepsilon\cdot\left(-\tfrac12\right)\left(-2(x+C)\right)^{-3/2}\cdot(-2) = \varepsilon\left(-2(x+C)\right)^{-3/2},$$

and $y^{3} = \varepsilon^{3}\left(-2(x+C)\right)^{-3/2} = \varepsilon\left(-2(x+C)\right)^{-3/2}$ ✓.

*Remark:* $y \equiv 0$ is a singular solution: no finite $C$ produces it, and the branches approach it only as $x \to -\infty$ with $C \to -\infty$ in a linked way. Note also that the branches are defined on a half-line, not on $\mathbb{R}$.

**7.** *Strategy: standard linear form with $P = 2$ and $Q = 6$, so $\mu = e^{2t}$.*

Multiplying by $e^{2t}$,

$$\left(ye^{2t}\right)' = 6e^{2t} \;\Longrightarrow\; ye^{2t} = 3e^{2t} + C \;\Longrightarrow\; y = 3 + Ce^{-2t}.$$

The initial condition gives $1 = 3 + C$, so $C = -2$ and

$$y = 3 - 2e^{-2t}, \qquad t \in \mathbb{R}.$$

As $t \to \infty$, $e^{-2t} \to 0$ and $y \to 3$: the solution approaches the equilibrium $y = 3$ of the autonomous equation $y' = 2(3-y)$, which is asymptotically stable because the coefficient of $y$ is $-2 < 0$.

*Check:* $y' = 4e^{-2t}$ and $y' + 2y = 4e^{-2t} + 6 - 4e^{-2t} = 6$ ✓; $y(0) = 1$ ✓.

**8.** *Strategy: standard form with $P(x) = 1/x$, so $\mu = e^{\ln x} = x$ on $x > 0$.*

$$xy' + y = x^{2} \;\Longrightarrow\; (xy)' = x^{2} \;\Longrightarrow\; xy = \frac{x^{3}}{3} + C \;\Longrightarrow\; y = \frac{x^{2}}{3} + \frac{C}{x}, \qquad x > 0 .$$

*Check:* $y' = \dfrac{2x}{3} - \dfrac{C}{x^{2}}$ and $\dfrac{y}{x} = \dfrac{x}{3} + \dfrac{C}{x^{2}}$, so $y' + \dfrac{y}{x} = x$ ✓.

*Remark:* the solution has a singularity at $x = 0$ unless $C = 0$; since the interval of continuity of $P$ and $Q$ is $(0,\infty)$, Theorem 8.3 guarantees the solution on that whole interval and says nothing about $x < 0$, where the equation would have to be treated separately.

**9.** *Strategy: factor first, then read the sign of $f$ on each interval between consecutive zeros, then confirm with $f'$.*

Write $f(y) = y(1-y)(2-y)$, with zeros $y = 0, 1, 2$. The sign of each factor is constant between zeros, so the sign of the product is determined by counting negative factors:

| Interval | $y$ | $1-y$ | $2-y$ | $f$ | Motion |
|---|---|---|---|---|---|
| $(-\infty,0)$ | $-$ | $+$ | $+$ | $-$ | decreasing, away from $0$ |
| $(0,1)$ | $+$ | $+$ | $+$ | $+$ | increasing, towards $1$ |
| $(1,2)$ | $+$ | $-$ | $+$ | $-$ | decreasing, towards $1$ |
| $(2,\infty)$ | $+$ | $-$ | $-$ | $+$ | increasing, away from $2$ |

Hence $y = 0$ is a source (**unstable**), $y = 1$ is a sink (**asymptotically stable**), and $y = 2$ is a source (**unstable**).

*Confirmation by the linearisation test.* Differentiate the product:

$$f'(y) = (1-y)(2-y) + y(-1)(2-y) + y(1-y)(-1).$$

At $y = 0$: $f'(0) = (1)(2) = 2 > 0$, unstable ✓. At $y = 1$: $f'(1) = 0 + (1)(-1)(1) + 0 = -1 < 0$, asymptotically stable ✓. At $y = 2$: $f'(2) = 0 + 0 + (2)(-1)(-1) = 2 > 0$, unstable ✓.

*Remark:* because no derivative vanishes except at the equilibria themselves, the phase line is exhaustive: every solution converges to $1$ if it starts in $(0,2)$, and diverges if it starts outside $[0,2]$ — to $-\infty$ below $0$ and to $+\infty$ above $2$, both in finite time.

**10.** *(a)* The isocline of slope $c$ is the set $y - x = c$, that is the line $y = x + c$. Hence slope $-1$: the line $y = x - 1$; slope $0$: the line $y = x$; slope $1$: the line $y = x + 1$. All isoclines are parallel, so the direction field is a sheared copy of a one-dimensional field.

*(b)* On $y = x + 1$ we have $y' = 1$ and $y - x = 1$; the two sides agree at every point of the line, so $y = x+1$ is a solution (and, being defined for all $x$, it is a maximal one).

*(c)* Differentiate $y' = f(x,y) = y - x$:

$$y'' = f_x + f_y\,y' = -1 + 1\cdot(y-x) = y - x = y' .$$

So $y'' > 0$ exactly where $y' > 0$, that is where $y > x$: solutions are concave up above the line $y = x$ and concave down below it. In particular an inflection point can occur only on $y = x$.

*Consistency check:* the general solution is $y = x + 1 + Ce^{x}$, for which $y'' = Ce^{x} = y - x - 1 + 1 = y - x$ ✓.

**11.** *Model.* With $T$ in $^{\circ}\mathrm{C}$ and $t$ in minutes, Newton's law of cooling is

$$\frac{dT}{dt} = -k(T - T_m), \qquad T(0) = 80, \quad T_m = 25, \quad k = 0.02\ \mathrm{min}^{-1}.$$

*Solution.* Separation gives $T = T_m + Ae^{-kt}$ and the initial condition gives $A = 80 - 25 = 55$:

$$T(t) = 25 + 55e^{-0.02t} .$$

*After 30 minutes:* $T(30) = 25 + 55e^{-0.6} \approx 25 + 55(0.5488) \approx 55.2\,^{\circ}\mathrm{C}$.

*Time to $35\,^{\circ}\mathrm{C}$:* $55e^{-0.02t} = 10$, so $e^{-0.02t} = 2/11$ and

$$t = -\frac{\ln(2/11)}{0.02} = 50\ln\frac{11}{2} \approx 50(1.7047) \approx 85.2\ \mathrm{min}.$$

*Checks:* the units of $kt$ are dimensionless ✓; $T(0) = 80$ ✓; $T$ decreases towards $25$ ✓; the time to fall from $80$ to $35$ (a drop of $45$ of the $55$ excess) is larger than the $34.7$ minutes needed to halve the excess, as it must be ✓.

**12.** *Model.* $N = N_0e^{kt}$ with $k < 0$, and $k = -\ln 2/T_{1/2}$.

*(a)* $k = -\dfrac{\ln 2}{5730} = -1.2097\times10^{-4}\ \mathrm{yr}^{-1}$.

*(b)* The fraction remaining after $t$ years is $e^{kt}$, so after $2000$ years

$$\frac{N}{N_0} = e^{-1.2097\times10^{-4}\times 2000} = e^{-0.24194} \approx 0.785 .$$

*(c)* Solving $0.45 = e^{kt}$ gives

$$t = \frac{\ln 0.45}{k} = -\frac{0.79851}{1.2097\times10^{-4}} \approx 6.60\times10^{3}\ \mathrm{yr}.$$

*Checks:* the half-life appears correctly as $t = \ln 0.5/k = 5730$ ✓; the fraction in (b) lies between $0.5$ and $1$, as it must for an age between zero and one half-life ✓; in (c) less than half the carbon remains, so the age must exceed $5730$ years, and $6600$ does ✓.

## Intermediate

**13.** *Strategy: $y^{2} - 1 = (y-1)(y+1)$ is separable; record the two zeros before dividing.*

The constant solutions are $y \equiv 1$ and $y \equiv -1$. For $y \ne \pm 1$,

$$\frac{dy}{y^{2}-1} = dx, \qquad \frac{1}{y^{2}-1} = \frac{1}{2}\left(\frac{1}{y-1} - \frac{1}{y+1}\right),$$

so

$$\frac{1}{2}\ln\left\lvert\frac{y-1}{y+1}\right\rvert = x + C \;\Longrightarrow\; \frac{y-1}{y+1} = Ae^{2x}, \quad A \in \mathbb{R},$$

and solving for $y$,

$$y - 1 = Ae^{2x}(y+1) \;\Longrightarrow\; y\left(1 - Ae^{2x}\right) = 1 + Ae^{2x} \;\Longrightarrow\; y = \frac{1 + Ae^{2x}}{1 - Ae^{2x}} .$$

*Lost solutions.* $A = 0$ gives $y \equiv 1$, so that one is recovered; $y \equiv -1$ corresponds to the limit $A \to \pm\infty$ and is **not** attained, so it must be listed separately. The complete solution set is therefore $y = \frac{1+Ae^{2x}}{1-Ae^{2x}}$ together with $y \equiv -1$.

*Check:* differentiating,

$$y' = \frac{2Ae^{2x}\left(1-Ae^{2x}\right) + 2Ae^{2x}\left(1+Ae^{2x}\right)}{\left(1-Ae^{2x}\right)^{2}} = \frac{4Ae^{2x}}{\left(1-Ae^{2x}\right)^{2}},$$

while

$$y^{2} - 1 = \frac{\left(1+Ae^{2x}\right)^{2} - \left(1-Ae^{2x}\right)^{2}}{\left(1-Ae^{2x}\right)^{2}} = \frac{4Ae^{2x}}{\left(1-Ae^{2x}\right)^{2}} \;\checkmark$$

*Structure:* the formula has a vertical asymptote where $Ae^{2x} = 1$, so each solution is defined on one side of that point — one branch in $(-\infty, -\ln A/2)$ and one in $(-\ln A/2, \infty)$ when $A > 0$.

**14.** *Strategy: divide by $x$ to reach standard form, then use $\mu = e^{\int 2/x\,dx} = x^{2}$.*

$$y' + \frac{2}{x}y = 4x \;\Longrightarrow\; x^{2}y' + 2xy = 4x^{3} \;\Longrightarrow\; \left(x^{2}y\right)' = 4x^{3} .$$

Integrating, $x^{2}y = x^{4} + C$, so

$$y = x^{2} + \frac{C}{x^{2}}, \qquad x > 0 .$$

The condition $y(1) = 1$ gives $1 = 1 + C$, hence $C = 0$ and

$$y = x^{2}, \qquad x > 0 .$$

*Check:* $xy' + 2y = x(2x) + 2x^{2} = 4x^{2}$ ✓ and $y(1) = 1$ ✓.

*Remark:* the cancellation $C = 0$ is not an accident of the data — the forcing $4x^{2}$ is exactly the term produced by $y = x^{2}$ — but it must still be verified by substitution.

**15.** *Strategy: separate, then determine the maximal interval from the formula.*

$$\frac{dy}{y^{2}} = dx \;\Longrightarrow\; -\frac{1}{y} = x + C \;\Longrightarrow\; y = -\frac{1}{x+C} .$$

The initial condition $y(0) = 2$ gives $2 = -1/C$, so $C = -\tfrac{1}{2}$ and

$$y = \frac{2}{1 - 2x}, \qquad x < \frac{1}{2}.$$

*The maximal interval.* The formula is defined and differentiable for every $x \ne \tfrac{1}{2}$, giving two candidate intervals. The one containing the initial point $x = 0$ is $\left(-\infty,\tfrac12\right)$, and on it the solution never leaves the domain of $f(x,y) = y^{2}$, which is all of $\mathbb{R}^{2}$. Hence the maximal interval is $\left(-\infty,\tfrac12\right)$.

*Behaviour at the endpoint.* As $x \to \tfrac12^{-}$, $1 - 2x \to 0^{+}$ and $y \to +\infty$: the solution **blows up in finite time**. It cannot be continued past $x = \tfrac12$ because it is unbounded there, and beyond that point the other branch of the formula, $y = 2/(1-2x)$ on $\left(\tfrac12,\infty\right)$, is a different solution, not an extension.

*Check:* $y' = \dfrac{4}{(1-2x)^{2}}$ and $y^{2} = \dfrac{4}{(1-2x)^{2}}$ ✓; $y(0) = 2$ ✓.

*Remark:* this is the concrete content of the warning in §7.6 — Picard–Lindelöf promises a solution on *some* interval about $0$, here $(-1/2, 1/2)$ at best, and finite-time blow-up is a genuine feature of the equation, not a failure of the method.

**16.** *Strategy: test for exactness, then reconstruct the potential.*

$$M = 2xy + 3x^{2}, \qquad N = x^{2} - 2y, \qquad M_y = 2x, \qquad N_x = 2x .$$

The test passes everywhere, so the equation is exact (the plane is simply connected).

*Potential.* Integrate $M$ with respect to $x$ at fixed $y$:

$$F = \int\left(2xy + 3x^{2}\right)dx = x^{2}y + x^{3} + g(y).$$

Then

$$F_y = x^{2} + g'(y) \overset{!}{=} N = x^{2} - 2y \;\Longrightarrow\; g'(y) = -2y \;\Longrightarrow\; g(y) = -y^{2} .$$

The solutions are the level curves

$$x^{2}y + x^{3} - y^{2} = C .$$

*Check by implicit differentiation:* differentiating gives

$$\left(2xy + 3x^{2}\right) + \left(x^{2} - 2y\right)y' = 0,$$

which is the original equation ✓. Note that $g'$ came out free of $x$ — the signature, guaranteed by the exactness test, that the construction is consistent.

**17.** *Strategy: look for an integrating factor depending on $x$ alone, using the quotient $(M_y - N_x)/N$.*

$$M = 3x^{2} + y, \qquad N = x^{2}y - x, \qquad M_y = 1, \qquad N_x = 2xy - 1 .$$

The equation is not exact. Compute

$$\frac{M_y - N_x}{N} = \frac{1 - (2xy-1)}{x^{2}y - x} = \frac{2 - 2xy}{x(xy-1)} = \frac{-2(xy-1)}{x(xy-1)} = -\frac{2}{x},$$

which depends on $x$ alone (for $xy \ne 1$). Hence

$$\mu(x) = \exp\!\left(\int -\frac{2}{x}\,dx\right) = x^{-2} .$$

*Retest.* Multiplying by $x^{-2}$,

$$\left(3 + \frac{y}{x^{2}}\right)dx + \left(y - \frac{1}{x}\right)dy = 0, \qquad \tilde M_y = \frac{1}{x^{2}} = \tilde N_x ,$$

so it is exact. Integrating,

$$F = \int\left(3 + \frac{y}{x^{2}}\right)dx = 3x - \frac{y}{x} + g(y), \qquad F_y = -\frac{1}{x} + g'(y) = y - \frac{1}{x} \;\Longrightarrow\; g'(y) = y .$$

Therefore $g = \tfrac{1}{2}y^{2}$ and the solutions are

$$3x - \frac{y}{x} + \frac{y^{2}}{2} = C .$$

*Check:* $F_x = 3 + \dfrac{y}{x^{2}} = \dfrac{M}{x^{2}}$ and $F_y = -\dfrac{1}{x} + y = \dfrac{N}{x^{2}}$ ✓, so $F_x + F_y y' = 0$ is the original equation divided by the positive factor $x^{2}$ — the same solution set.

*Remark:* the quotient is undefined on the hyperbola $xy = 1$, where the integrating factor was derived by cancellation. That curve is not a solution of the original equation (substituting $y = 1/x$ leaves $3x^{2} + 1/x \ne 0$), so no solution is lost.

**18.** *Strategy: Bernoulli with $n = 2$; substitute $v = y^{-1}$.*

Divide by $y^{2}$: $y^{-2}y' + \dfrac{y^{-1}}{x} = 1$. With $v = y^{-1}$ and $v' = -y^{-2}y'$ this is

$$-v' + \frac{v}{x} = 1 \quad\Longleftrightarrow\quad v' - \frac{v}{x} = -1 .$$

*Integrating factor.* With $P = -1/x$, $\mu = e^{-\ln x} = 1/x$ on $x > 0$, so

$$\left(\frac{v}{x}\right)' = -\frac{1}{x} \;\Longrightarrow\; \frac{v}{x} = -\ln x + C \;\Longrightarrow\; v = x\left(C - \ln x\right).$$

Therefore

$$y = \frac{1}{v} = \frac{1}{x\left(C - \ln x\right)},$$

and the lost solution $y \equiv 0$ (removed by the division by $y^{2}$) must be added.

*Interval.* The solution is defined where $x > 0$ and $C - \ln x \ne 0$, that is $x \ne e^{C}$; the maximal interval containing a given initial point is whichever of $(0, e^{C})$ or $(e^{C},\infty)$ contains it.

*Check:* with $L = C - \ln x$ and $y = 1/(xL)$,

$$y' = -\frac{L + x\cdot(-1/x)}{x^{2}L^{2}} = -\frac{L - 1}{x^{2}L^{2}}, \qquad \frac{y}{x} = \frac{1}{x^{2}L}, \qquad y^{2} = \frac{1}{x^{2}L^{2}},$$

and $-\dfrac{L-1}{x^{2}L^{2}} + \dfrac{1}{x^{2}L} = \dfrac{-(L-1) + L}{x^{2}L^{2}} = \dfrac{1}{x^{2}L^{2}} = y^{2}$ ✓

**19.** *Strategy: the right side depends on $y/x$ only, so the equation is homogeneous; substitute $v = y/x$.*

With $y = xv$ and $y' = v + xv'$,

$$v + xv' = v^{2} + v \;\Longrightarrow\; xv' = v^{2} \;\Longrightarrow\; \frac{dv}{v^{2}} = \frac{dx}{x} .$$

Integrating, $-\dfrac{1}{v} = \ln x + C$, so $v = -\dfrac{1}{\ln x + C}$ and

$$y = xv = -\frac{x}{\ln x + C}, \qquad x > 0 .$$

*Lost solution.* The division by $v^{2}$ removes $v \equiv 0$, that is $y \equiv 0$, which does solve the equation (both sides vanish) and must be added.

*Interval.* The solution is defined where $\ln x + C \ne 0$; with $x_0$ the initial point, the maximal interval is the component of $\{x > 0 : x \ne e^{-C}\}$ containing $x_0$.

*Check:* with $L = \ln x + C$ and $y = -x/L$,

$$y' = -\frac{1}{L} + \frac{x}{L^{2}}\cdot\frac{1}{x} = -\frac{1}{L} + \frac{1}{L^{2}}, \qquad \frac{y^{2}}{x^{2}} = \frac{1}{L^{2}}, \qquad \frac{y}{x} = -\frac{1}{L},$$

so $\dfrac{y^{2}}{x^{2}} + \dfrac{y}{x} = \dfrac{1}{L^{2}} - \dfrac{1}{L} = y'$ ✓

**20.** *Strategy: the logistic equation is separable; the solution formula is derived in §9.9 and is quoted here, then specialised.*

The general solution is

$$P(t) = \frac{K}{1 + \left(\dfrac{K-P_0}{P_0}\right)e^{-rt}}$$

with $K = 500$, $r = 0.8$ and $P_0 = 50$, so $\dfrac{K - P_0}{P_0} = \dfrac{450}{50} = 9$ and

$$P(t) = \frac{500}{1 + 9e^{-0.8t}} \quad (\text{thousands}), \qquad t \ge 0 .$$

*Limit.* As $t \to \infty$, $e^{-0.8t} \to 0$, so $P \to 500$: the carrying capacity, consistent with §7.7, where $P = 500$ was found asymptotically stable and $P = 0$ unstable.

*Time to $P = 250$.* Setting $250 = \dfrac{500}{1 + 9e^{-0.8t}}$ gives $1 + 9e^{-0.8t} = 2$, hence $e^{-0.8t} = \tfrac19$ and

$$t = \frac{\ln 9}{0.8} = \frac{2.1972}{0.8} \approx 2.75\ \mathrm{yr}.$$

*Check:* $P(0) = 500/10 = 50$ ✓. For the differential equation,

$$P' = \frac{500\cdot 0.8\cdot 9e^{-0.8t}}{\left(1+9e^{-0.8t}\right)^{2}} = \frac{3600e^{-0.8t}}{\left(1+9e^{-0.8t}\right)^{2}},$$

and

$$0.8\,P\left(1 - \frac{P}{500}\right) = 0.8\cdot\frac{500}{1+9e^{-0.8t}}\cdot\frac{9e^{-0.8t}}{1+9e^{-0.8t}} = \frac{3600e^{-0.8t}}{\left(1+9e^{-0.8t}\right)^{2}} \;\checkmark$$

*Remark:* the halfway population is reached at $2.75$ years, but the second half takes indefinitely long — the classic signature of the logistic curve, which approaches its asymptote exponentially rather than in finite time.

**21.** *Setup.* Inflow and outflow are equal, so the volume stays at $V = 500\ \mathrm{L}$ and the concentration at time $t$ is $S(t)/500$ kilograms per litre. The rate balance in $\mathrm{kg/min}$ is

$$\frac{dS}{dt} = \underbrace{5 \times 0.04}_{\text{in}} - \underbrace{5\cdot\frac{S}{500}}_{\text{out}} = 0.2 - 0.01S, \qquad S(0) = 0 .$$

*Solve.* The equation is linear (and separable). Separating,

$$\frac{dS}{0.2 - 0.01S} = dt \;\Longrightarrow\; -\frac{1}{0.01}\ln\left(0.2 - 0.01S\right) = t + c,$$

so $0.2 - 0.01S = Ae^{-0.01t}$ and $S = 20 - 100Ae^{-0.01t}$. The initial condition gives $0 = 20 - 100A$, so $A = 0.2$ and

$$S(t) = 20\left(1 - e^{-0.01t}\right)\ \mathrm{kg}, \qquad t \ge 0 .$$

*Time to $10\ \mathrm{kg}$.* $20\left(1 - e^{-0.01t}\right) = 10$ gives $e^{-0.01t} = \tfrac12$, so

$$t = 100\ln 2 \approx 69.3\ \mathrm{min}.$$

*Checks:* $S(0) = 0$ ✓; $S \to 20\ \mathrm{kg}$ as $t\to\infty$, and $20\ \mathrm{kg} / 500\ \mathrm{L} = 0.04\ \mathrm{kg/L}$, the inflow concentration ✓ — the only steady state in which what leaves has the same concentration as what enters. Differentiating the formula gives $S' = 0.2e^{-0.01t} = 0.2 - 0.01S$ ✓.

**22.** *Model.* Taking downward as positive, with $m = 70\ \mathrm{kg}$, $k = 20\ \mathrm{kg/s}$, $g = 9.8\ \mathrm{m/s^{2}}$,

$$m\frac{dv}{dt} = mg - kv, \qquad v(0) = 0 .$$

*Solve.* The equation is linear with constant coefficients: $v' + \dfrac{k}{m}v = g$, so $\mu = e^{kt/m}$ and

$$v = \frac{mg}{k} + Ce^{-kt/m} .$$

The initial condition $v(0) = 0$ gives $C = -\dfrac{mg}{k}$, hence

$$v(t) = \frac{mg}{k}\left(1 - e^{-kt/m}\right) = \frac{686}{20}\left(1 - e^{-t/3.5}\right) = 34.3\left(1 - e^{-t/3.5}\right)\ \mathrm{m/s}.$$

*Terminal velocity.* $v_\infty = \dfrac{mg}{k} = 34.3\ \mathrm{m/s}$ (about $123\ \mathrm{km/h}$).

*Time to $90\%$ of terminal velocity.* $e^{-t/3.5} = 0.1$ gives

$$t = 3.5\ln 10 \approx 8.06\ \mathrm{s}.$$

*Checks:* the units are right — $\dfrac{mg}{k}$ is $\dfrac{\mathrm{kg}\cdot\mathrm{m/s^{2}}}{\mathrm{kg/s}} = \mathrm{m/s}$ and $\dfrac{m}{k}$ is $\mathrm{s}$ ✓; $v(0) = 0$ ✓; $v$ increases and is concave down, since $v' = g - \dfrac{k}{m}v$ decreases as $v$ grows ✓; substituting, $v' = \dfrac{mg}{k}\cdot\dfrac{k}{m}e^{-kt/m} = ge^{-kt/m}$ and $mg - kv = mg - mg\left(1 - e^{-kt/m}\right) = mge^{-kt/m}$, so $v' = (mg-kv)/m$ ✓.

## Advanced

**23.** *Strategy: check the three pieces of $y_c$ separately, with particular care at the junction, where differentiability must be proved.*

Let $c \ge 0$ and let $y_c$ be $0$ for $x \le c$ and $(x-c)^{3}$ for $x \ge c$.

*Piece 1, $x < c$:* $y_c = 0$, so $y_c' = 0$ and $3y_c^{2/3} = 0$; the equation holds.

*Piece 2, $x > c$:* $y_c' = 3(x-c)^{2}$ and $y_c^{2/3} = \left((x-c)^{3}\right)^{2/3} = (x-c)^{2}$, since $x - c > 0$; hence $3y_c^{2/3} = 3(x-c)^{2} = y_c'$.

*At $x = c$:* the two pieces agree in value, giving $y_c(c) = 0$. The left derivative is $0$ and the right derivative is $\lim_{h\to0^{+}}\frac{h^{3}}{h} = \lim h^{2} = 0$, so $y_c$ is differentiable at $c$ with $y_c'(c) = 0$. Then $3y_c(c)^{2/3} = 0 = y_c'(c)$.

Hence $y_c$ is differentiable on $\mathbb{R}$ and satisfies the equation everywhere, and $y_c(0) = 0$ for every $c \ge 0$ because $0 \le c$ puts the initial point in the flat piece. Distinct values of $c$ give distinct functions (they differ at $x > \max(c_1,c_2)$), so the IVP has **infinitely many solutions**.

*Why Picard–Lindelöf does not apply.* Theorem 7.2 requires $f(y) = 3y^{2/3}$ to be locally Lipschitz at $y_0 = 0$. But

$$\frac{\left\lvert f(y) - f(0)\right\rvert}{\lvert y - 0\rvert} = \frac{3\lvert y\rvert^{2/3}}{\lvert y\rvert} = 3\lvert y\rvert^{-1/3} \longrightarrow \infty \quad (y \to 0),$$

so no constant $L$ works on any neighbourhood of $0$. The hypothesis fails exactly where the field is vertical in the $y$-direction, and uniqueness fails with it — the theorem is sharp, not merely convenient.

*Remark:* the sign-reversed family, equal to $(x-c)^{3}$ for $x \le c$ and $0$ for $x \ge c$ with $c \le 0$, gives further solutions through the origin; the point of the exercise is not to enumerate them but to see the mechanism — a solution can wait at an equilibrium and leave it later.

**24.** *Strategy: Bernoulli with $n = \tfrac12$; substitute $v = y^{1/2} = \sqrt{y}$.*

With $y = v^{2}$ and $y' = 2vv'$, the equation becomes $2vv' + v^{2} = v$. On the region $v > 0$ divide by $v$:

$$2v' + v = 1 \quad\Longleftrightarrow\quad v' + \tfrac{1}{2}v = \tfrac{1}{2} .$$

*Integrating factor.* $\mu = e^{x/2}$, so

$$\left(ve^{x/2}\right)' = \tfrac{1}{2}e^{x/2} \;\Longrightarrow\; ve^{x/2} = e^{x/2} + C \;\Longrightarrow\; v = 1 + Ce^{-x/2} .$$

The initial condition $y(0) = 4$ means $v(0) = 2$, so $2 = 1 + C$ and $C = 1$. Therefore

$$y = v^{2} = \left(1 + e^{-x/2}\right)^{2}, \qquad x \in \mathbb{R}.$$

*Missed solutions.* The division by $v = \sqrt{y}$ removes $y \equiv 0$, which is a solution of the original equation (both sides vanish). It is not part of this family, whose members satisfy $y = (1 + Ce^{-x/2})^{2} > 0$ whenever $C > 0$; for $C < 0$ the formula vanishes at $x = -2\ln(-C)$, and there the solution must be matched with the zero solution on one side, exactly as in problem 23. Negative $y$ is not in the domain of $\sqrt{y}$.

*Check:* $y' = 2\left(1+e^{-x/2}\right)\left(-\tfrac{1}{2}e^{-x/2}\right) = -e^{-x/2}\left(1+e^{-x/2}\right)$, so

$$y' + y = -e^{-x/2}\left(1+e^{-x/2}\right) + \left(1+e^{-x/2}\right)^{2} = \left(1+e^{-x/2}\right)\left(1 + e^{-x/2} - e^{-x/2}\right) = 1 + e^{-x/2} = \sqrt{y} \;\checkmark$$

and $y(0) = (1+1)^{2} = 4$ ✓.

**25.** *Equilibria.* They solve $ry\left(1 - \frac{y}{K}\right) = h$, that is

$$y^{2} - Ky + \frac{hK}{r} = 0 \quad\Longrightarrow\quad y = \frac{K \pm \sqrt{K^{2} - \dfrac{4hK}{r}}}{2} = \frac{K}{2} \pm \sqrt{\frac{K^{2}}{4} - \frac{hK}{r}} .$$

Real roots exist exactly when $\dfrac{K^{2}}{4} \ge \dfrac{hK}{r}$, that is $h \le \dfrac{rK}{4}$. Hence

$$h_c = \frac{rK}{4},$$

and for $0 < h < h_c$ there are two equilibria

$$y_{\pm} = \frac{K}{2} \pm \sqrt{\frac{K^{2}}{4} - \frac{hK}{r}}, \qquad y_{-} < \frac{K}{2} < y_{+} .$$

*Classification.* With $f(y) = ry\left(1-\frac{y}{K}\right) - h$,

$$f'(y) = r - \frac{2ry}{K} = -\frac{2r}{K}\left(y - \frac{K}{2}\right).$$

Hence $f'(y_{-}) > 0$, so $y_{-}$ is **unstable**, and $f'(y_{+}) < 0$, so $y_{+}$ is **asymptotically stable**.

*Interpretation.* $y_{+}$ is the sustainable stock: harvesting at rate $h$ leaves a stable population that absorbs small shocks. $y_{-}$ is a threshold: below it the harvest exceeds reproduction and the stock collapses. At $h = h_c$ the two merge at $y = K/2$, and for $h > h_c$ no equilibrium remains.

*Check of the formula against the unharvested case:* at $h = 0$ we get $y_{-} = 0$ and $y_{+} = K$, matching §7.7 ✓; and $f'(0) = r > 0$, $f'(K) = -r < 0$ ✓.

**26.** *Strategy: the equation is not of any standard type, but $x+y$ appears as a block; put $v = x+y$.*

Then $v' = 1 + y' = 1 + \dfrac{1}{v} = \dfrac{v+1}{v}$, so the equation is separable:

$$\frac{v}{v+1}\,dv = dx \;\Longrightarrow\; \int\left(1 - \frac{1}{v+1}\right)dv = x + C \;\Longrightarrow\; v - \ln|v + 1| = x + C .$$

Substituting back $v = x + y$ and cancelling $x$ from both sides,

$$y - \ln\left\lvert x + y + 1\right\rvert = C .$$

*Check by implicit differentiation.* Let $F(x,y) = y - \ln|x+y+1|$. Then

$$F_x = -\frac{1}{x+y+1}, \qquad F_y = 1 - \frac{1}{x+y+1} = \frac{x+y}{x+y+1},$$

and $F_x + F_y y' = 0$ gives $y' = \dfrac{1/(x+y+1)}{(x+y)/(x+y+1)} = \dfrac{1}{x+y}$ ✓, the original equation.

*Remarks.* The implicit form is the natural answer; solving for $y$ would require inverting $y - \ln|x+y+1|$, which is not an elementary inversion. The solution is defined on any interval where $x + y + 1 \ne 0$ and the implicit function theorem applies, that is $F_y \ne 0$, which fails exactly where $x + y = 0$ — consistent with the original equation being singular at $x+y = 0$.

**27.** *Setup.* The volume grows because inflow exceeds outflow:

$$V(t) = 100 + (3-2)t = 100 + t \quad \text{litres}, \qquad \frac{dS}{dt} = 3(0.2) - 2\cdot\frac{S}{100+t} = 0.6 - \frac{2S}{100+t}, \quad S(0) = 0 .$$

*Solve.* This is linear with variable coefficients: $S' + \dfrac{2}{100+t}S = 0.6$, and

$$\mu = \exp\!\left(\int\frac{2}{100+t}\,dt\right) = (100+t)^{2} .$$

Multiplying, $\left((100+t)^{2}S\right)' = 0.6(100+t)^{2}$, so

$$(100+t)^{2}S = 0.2(100+t)^{3} + C \;\Longrightarrow\; S(t) = 0.2(100+t) + \frac{C}{(100+t)^{2}} .$$

The initial condition gives $0 = 20 + \dfrac{C}{10000}$, so $C = -200000$ and

$$S(t) = 0.2(100+t) - \frac{2\times10^{5}}{(100+t)^{2}}\ \mathrm{kg}, \qquad t \ge 0 .$$

*Long-run concentration.* Dividing by $V = 100+t$,

$$\frac{S(t)}{V(t)} = 0.2 - \frac{2\times10^{5}}{(100+t)^{3}} \longrightarrow 0.2\ \mathrm{kg/L} \quad (t\to\infty),$$

which is the inflow concentration: asymptotically the tank is flushed, and what leaves has the same composition as what enters.

*Check:* $S(0) = 20 - 20 = 0$ ✓. Differentiating the formula,

$$S' = 0.2 + \frac{4\times10^{5}}{(100+t)^{3}},$$

while

$$0.6 - \frac{2S}{100+t} = 0.6 - 0.4 + \frac{4\times10^{5}}{(100+t)^{3}} = 0.2 + \frac{4\times10^{5}}{(100+t)^{3}} \;\checkmark$$

*Remark:* the units balance — $0.2(100+t)$ is $\mathrm{kg/L}\times\mathrm{L} = \mathrm{kg}$ and $2\times10^{5}/(100+t)^{2}$ is $\mathrm{kg\,L^{2}/L^{2}} = \mathrm{kg}$.

**28.** *The iteration.* With $y_0(x) \equiv 0$ and $y_{n+1}(x) = \displaystyle\int_0^{x}\left(s + y_n(s)\right)ds$:

$$y_1(x) = \int_0^{x}s\,ds = \frac{x^{2}}{2}, \qquad y_2(x) = \int_0^{x}\left(s + \frac{s^{2}}{2}\right)ds = \frac{x^{2}}{2} + \frac{x^{3}}{6},$$

$$y_3(x) = \int_0^{x}\left(s + \frac{s^{2}}{2} + \frac{s^{3}}{6}\right)ds = \frac{x^{2}}{2} + \frac{x^{3}}{6} + \frac{x^{4}}{24} .$$

*General iterate.* Claim $y_n(x) = \displaystyle\sum_{k=2}^{n+1}\frac{x^{k}}{k!}$. It holds for $n = 1$; if it holds for $n$, then

$$y_{n+1}(x) = \int_0^{x}\left(s + \sum_{k=2}^{n+1}\frac{s^{k}}{k!}\right)ds = \frac{x^{2}}{2} + \sum_{k=2}^{n+1}\frac{x^{k+1}}{(k+1)k!} = \frac{x^{2}}{2} + \sum_{k=3}^{n+2}\frac{x^{k}}{k!} = \sum_{k=2}^{n+2}\frac{x^{k}}{k!},$$

which is the claim with $n+1$. By induction the formula holds for all $n$.

*Limit.* The partial sums converge for every $x$ to

$$y(x) = \sum_{k=2}^{\infty}\frac{x^{k}}{k!} = e^{x} - 1 - x .$$

*Verification.* $y(0) = 1 - 1 - 0 = 0$ ✓ and $y' = e^{x} - 1 = x + \left(e^{x} - 1 - x\right) = x + y$ ✓. Since the series converges on all of $\mathbb{R}$ and the right side is entire, the solution is defined for every $x$.

*Consistency with the contraction estimate.* Each iterate adds one power of $x$ and one factorial in the denominator, so the error after $n$ steps is bounded by the tail $\sum_{k>n+1}\lvert x\rvert^{k}/k!$, which decays faster than any power — far better than the geometric rate guaranteed in general by §7.6.

**29.** *Strategy: a strictly increasing $f$ pushes solutions away from the equilibrium; the only point to prove is that they leave every neighbourhood, not merely move away infinitesimally.*

Suppose $f(y^{*}) = 0$ and $f'(y^{*}) > 0$. Choose $m > 0$ and $\delta > 0$ such that $f'(y) \ge m$ for $\lvert y - y^{*}\rvert < \delta$; this is possible because $f'$ is continuous and positive at $y^{*}$. For $y \in (y^{*}, y^{*}+\delta)$,

$$f(y) = \int_{y^{*}}^{y}f'(s)\,ds \ge m(y - y^{*}) > 0 .$$

Let $y$ be the solution with $y(x_0) = y^{*} + \varepsilon$, where $0 < \varepsilon < \delta$. Define
$T = \sup\{x \ge x_0 : y(s) > y^{*} \text{ for all } s \in [x_0,x]\}$.

On $[x_0,T)$ we have $y > y^{*}$, hence $y' = f(y) > 0$: the solution is strictly increasing. It cannot reach $y^{*}$: if $y(x_1) = y^{*}$ for some $x_1$, then $y$ and the constant solution $y^{*}$ solve the same IVP at $x_1$, so by uniqueness they coincide, contradicting $y(x_0) > y^{*}$.

Suppose, for contradiction, that $y$ stays below $y^{*} + \delta$ for all $x \ge x_0$. Then $y$ is increasing and bounded, so $L = \lim_{x\to\infty}y(x) \in (y^{*}, y^{*}+\delta]$ exists, and Lemma 7.1 gives $f(L) = 0$. But $f > 0$ on $(y^{*}, y^{*}+\delta]$, contradiction. Hence for some finite $x_1$ we have $y(x_1) \ge y^{*}+\delta$.

Now let $\delta' \in (0,\delta)$ be arbitrary and take $\varepsilon < \min(\delta', \delta)/2$. The same argument shows the solution starting at $y^{*}+\varepsilon$ eventually exceeds $y^{*}+\delta > y^{*}+\delta'$. Thus solutions starting arbitrarily close to $y^{*}$ do not stay within $\delta'$ of it, so the equilibrium is not stable, i.e. it is **unstable**. The case of initial values below $y^{*}$ is symmetric (there $f < 0$, so the solution decreases away). $\blacksquare$

*Remark:* the estimate $f(y) \ge m(y-y^{*})$ is what rules out the "asymptotic" escape; without it one could only conclude that the solution moves away initially. The flat case $f'(y^{*}) = 0$ is where this estimate fails, and there all three behaviours occur (§7.7).

*Check against an example.* Take $f(y) = y$ and $y^{*} = 0$, so $f'(0) = 1 > 0$. The solution starting at $y(0) = \varepsilon$ is $y = \varepsilon e^{x}$, which exceeds any $\delta'$ once $x > \ln(\delta'/\varepsilon)$ — finite for every $\varepsilon > 0$, exactly as the proof asserts ✓. The estimate of the proof is $f(y) = y \ge 1\cdot y$ with $m = 1$, sharp in this case.

**30.** *Strategy: look for $\mu = \mu(x)$ using the quotient $(M_y - N_x)/N$.*

$$M = 2y^{2} + 3x, \qquad N = 2xy, \qquad M_y = 4y, \qquad N_x = 2y .$$

The equation is not exact. Since

$$\frac{M_y - N_x}{N} = \frac{4y - 2y}{2xy} = \frac{1}{x}$$

depends on $x$ alone (for $xy \ne 0$), the factor is

$$\mu(x) = \exp\!\left(\int\frac{dx}{x}\right) = x .$$

*Retest.* Multiplying by $x$ gives

$$\left(2xy^{2} + 3x^{2}\right)dx + 2x^{2}y\,dy = 0, \qquad \tilde M_y = 4xy = \tilde N_x ,$$

so it is exact. Integrating,

$$F = \int\left(2xy^{2} + 3x^{2}\right)dx = x^{2}y^{2} + x^{3} + g(y), \qquad F_y = 2x^{2}y + g'(y) = 2x^{2}y \;\Longrightarrow\; g'(y) = 0 .$$

Hence the solutions are

$$x^{2}y^{2} + x^{3} = C .$$

*Check:* $F_x = 2xy^{2} + 3x^{2} = xM$ and $F_y = 2x^{2}y = xN$ ✓, so $F_x + F_y y' = 0$ is the original equation multiplied by $x$; and $x = 0$ is not a solution curve of the original equation, so no solutions are lost.

## Challenge

**31.** *The differentiation.* Write $p = y'$ and differentiate $y = xp - p^{2}$ with respect to $x$, remembering that $p$ is a function of $x$:

$$p = \frac{dy}{dx} = p + x\frac{dp}{dx} - 2p\frac{dp}{dx} \;\Longrightarrow\; 0 = \left(x - 2p\right)\frac{dp}{dx} .$$

*Case 1: $\dfrac{dp}{dx} = 0$.* Then $p = C$ is constant and $y = Cx - C^{2}$. This is a one-parameter family of straight lines, and each is a solution:

$$y' = C, \qquad xy' - (y')^{2} = Cx - C^{2} = y \;\checkmark$$

*Case 2: $x = 2p$.* Then $p = x/2$ and

$$y = x\cdot\frac{x}{2} - \frac{x^{2}}{4} = \frac{x^{2}}{4},$$

the **singular solution**. It is not a member of the family for any $C$: $Cx - C^{2} = x^{2}/4$ would require $C = x/2$ for every $x$, which is impossible. Substituting verifies it directly:

$$y' = \frac{x}{2}, \qquad xy' - (y')^{2} = \frac{x^{2}}{2} - \frac{x^{2}}{4} = \frac{x^{2}}{4} = y \;\checkmark$$

*Geometry: the parabola is the envelope.* For fixed $x$, the value of the family at $x$ is the function
$\Phi(C) = Cx - C^{2}$, a downward parabola in $C$ maximised at $C = x/2$ with value $\Phi(x/2) = x^{2}/4$. So
the singular solution records, at each $x$, the highest point reached by the family — the envelope. Equivalently, the members with parameters $C_{1} \ne C_{2}$ meet where $C_{1}x - C_{1}^{2} = C_{2}x - C_{2}^{2}$, that is at $x = C_{1} + C_{2}$, $y = C_{1}C_{2}$; letting $C_{2} \to C_{1} = C$ gives $x = 2C$, $y = C^{2} = x^{2}/4$. The envelope is the locus of intersections of infinitesimally close members.

*Remark:* this is the general phenomenon behind singular solutions — a family of curves has an envelope exactly where the derivative with respect to the parameter vanishes, and the envelope is a solution of the differential equation but not a member of the family.

**32.** *The count of equilibria.* As in problem 25, the equilibria solve $y^{2} - Ky + \dfrac{hK}{r} = 0$, whose discriminant is

$$\Delta(h) = K^{2} - \frac{4hK}{r} = \frac{4K}{r}\left(\frac{rK}{4} - h\right) = \frac{4K}{r}\left(h_c - h\right).$$

Hence $\Delta > 0$ for $h < h_c$ (two equilibria), $\Delta = 0$ at $h = h_c$ (one, namely $y = K/2$), and $\Delta < 0$ for $h > h_c$ (none). As $h$ increases through $h_c$ the two branches $y_{\pm}$ approach each other, merge at $K/2$, and disappear: a **fold** (saddle-node) bifurcation.

*Behaviour for $h > h_c$.* Since $ry\left(1 - \frac{y}{K}\right) \le \dfrac{rK}{4} < h$ for every $y$, we have

$$f(y) = ry\left(1 - \frac{y}{K}\right) - h < 0$$

for all $y$: every solution is strictly decreasing. A decreasing solution cannot converge to a finite limit $L$, because Lemma 7.1 would then force $f(L) = 0$, and $f$ has no zeros. So $y \to -\infty$. Moreover the divergence happens in finite time: for $y < 0$,

$$f(y) = -\frac{r}{K}y^{2} + ry - h \le -\frac{r}{2K}y^{2}$$

once $\lvert y\rvert$ is large (the quadratic term dominates), so $y' \le -\dfrac{r}{2K}y^{2}$ and comparison with the solution of $z' = -\dfrac{r}{2K}z^{2}$, $z(0) = y(0) < 0$, which reaches $-\infty$ in finite time, shows that $y$ does too.

*Interpretation.* Beyond $h_c$ the harvest exceeds the maximum sustainable yield $rK/4$, and the population collapses to extinction in finite time. The model is only valid while $y \ge 0$; the collapse time is when $y$ reaches $0$, after which the differential equation no longer describes the situation. The lesson of the fold is that the sustainable yield cannot be pushed past $rK/4$: at exactly $h_c$ the equilibrium is semistable (approached from above, repelling below), so any downward perturbation is fatal.

*Check with numbers.* Take $r = 1$, $K = 100$, so $h_c = 25$. With $h = 20$ the equilibria are $y = 50 \pm \sqrt{2500 - 2000} = 50 \pm 22.36$, that is $27.64$ and $72.36$. Since $f'(y) = 1 - 0.02y$, we get $f'(27.64) = 0.447 > 0$ (unstable) and $f'(72.36) = -0.447 < 0$ (stable) ✓. The maximum of $ry(1-y/K) = y - y^{2}/100$ is $25$ at $y = 50$, confirming $h_c = 25$ independently ✓. With $h = 30 > h_c$ the quadratic $y^{2} - 100y + 3000$ has discriminant $10^{4} - 1.2\times10^{4} < 0$: no equilibria ✓.

**33.** *The reduction.* Let $y = y_{1} + \dfrac{1}{v}$, so that $y' = y_{1}' - \dfrac{v'}{v^{2}}$. Substitute into the Riccati equation and use $y_{1}' = q_{0} + q_{1}y_{1} + q_{2}y_{1}^{2}$:

$$q_{0} + q_{1}\left(y_{1} + \frac{1}{v}\right) + q_{2}\left(y_{1} + \frac{1}{v}\right)^{2} = q_{0} + q_{1}y_{1} + q_{2}y_{1}^{2} + \frac{q_{1} + 2q_{2}y_{1}}{v} + \frac{q_{2}}{v^{2}} = y_{1}' + \frac{q_{1} + 2q_{2}y_{1}}{v} + \frac{q_{2}}{v^{2}} .$$

Equating with $y_{1}' - \dfrac{v'}{v^{2}}$ and cancelling $y_{1}'$,

$$-\frac{v'}{v^{2}} = \frac{q_{1} + 2q_{2}y_{1}}{v} + \frac{q_{2}}{v^{2}} \;\Longrightarrow\; v' + \left(q_{1} + 2q_{2}y_{1}\right)v = -q_{2},$$

multiplying by $-v^{2}$. This is linear in $v$, as claimed.

*Application to $y' = y^{2} - 1$.* Here $q_{0} = -1$, $q_{1} = 0$, $q_{2} = 1$, and $y_{1}(x) \equiv 1$ is a solution since $0 = 1 - 1$. The reduction gives

$$v' + 2v = -1 .$$

With $\mu = e^{2x}$, $\left(ve^{2x}\right)' = -e^{2x}$, so $ve^{2x} = -\tfrac{1}{2}e^{2x} + C$ and

$$v = -\frac{1}{2} + Ce^{-2x}, \qquad y = 1 + \frac{1}{-\tfrac12 + Ce^{-2x}} .$$

*Checks.* For $C = 0$, $v = -\tfrac12$ and $y = 1 - 2 = -1$: the second equilibrium, which the general family recovers in this parametrisation ✓. Differentiating the general formula,

$$y' = -\frac{-2Ce^{-2x}}{\left(-\tfrac12 + Ce^{-2x}\right)^{2}} = \frac{2Ce^{-2x}}{\left(-\tfrac12 + Ce^{-2x}\right)^{2}},$$

and, writing $w = -\tfrac12 + Ce^{-2x}$ so that $y = 1 + 1/w$,

$$y^{2} - 1 = \left(1 + \frac{1}{w}\right)^{2} - 1 = \frac{2}{w} + \frac{1}{w^{2}} = \frac{2w + 1}{w^{2}} .$$

Since $w + \tfrac12 = Ce^{-2x}$, we get $2w + 1 = 2Ce^{-2x}$, so $y^{2} - 1 = \dfrac{2Ce^{-2x}}{w^{2}} = y'$ ✓.

*Remark:* the same device, with the roles of $y$ and $v$ exchanged, is the standard route from a known solution of a Riccati equation to its general solution; the linear equation produced is exactly the one that governs the difference of two solutions.

**34.** *(a) No crossing.* Let $y_{1}, y_{2}$ solve $y' = f(y)$ on a common interval $I$, with $f$ locally Lipschitz, and suppose $y_{1}(x_{0}) < y_{2}(x_{0})$ for some $x_{0} \in I$. If there were $x_{1} \in I$ with $y_{1}(x_{1}) = y_{2}(x_{1})$, then both functions would solve the initial value problem

$$y' = f(y), \qquad y(x_{1}) = y_{1}(x_{1}),$$

and Picard–Lindelöf (Theorem 7.2, applicable because $f$ is locally Lipschitz) would give $y_{1} = y_{2}$ on $I$, contradicting $y_{1}(x_{0}) < y_{2}(x_{0})$. Therefore the continuous function $y_{2} - y_{1}$ never vanishes on $I$; being positive at $x_{0}$, it is positive everywhere. $\blacksquare$

*(b) The maximal interval for $y' = y^{2}$, $y(0) = y_{0} > 0$.* The function

$$y(x) = \frac{1}{\dfrac{1}{y_{0}} - x} = \frac{y_{0}}{1 - y_{0}x}$$

is defined and differentiable for $x \ne 1/y_{0}$, satisfies $y(0) = y_{0}$, and

$$y' = \frac{y_{0}^{2}}{\left(1 - y_{0}x\right)^{2}} = y^{2} \;\checkmark$$

so by uniqueness it is *the* solution on the component of $\mathbb{R}\setminus\{1/y_{0}\}$ containing $0$, namely $\left(-\infty, 1/y_{0}\right)$.

*Why the right end is finite.* As $x \to 1/y_{0}^{-}$, $1 - y_{0}x \to 0^{+}$ and $y \to +\infty$: the solution is unbounded, so it cannot be extended past $1/y_{0}$ as a differentiable function. Nothing before $1/y_{0}$ obstructs extension, so the maximal interval ends exactly there.

*Why the left end is $-\infty$.* For $x \to -\infty$, $y \to 0^{+}$ and the formula remains valid for every $x < 1/y_{0}$, so the solution is defined on the whole half-line. By part (a) it can never reach the equilibrium $y = 0$ (it stays above it), and it tends to $0$ as $x \to -\infty$ — the trajectory approaches an equilibrium in infinite (negative) time, which is exactly the behaviour the phase line predicts for a solution above the unstable equilibrium $0$.

*Remark:* the asymmetry has a structural cause. Forward in time, $y$ grows and the quadratic self-interaction produces blow-up in finite time; backward in time, $y$ decays and the nonlinearity weakens, so the solution can be continued indefinitely. In the language of §7.6, the maximal interval is the largest interval on which the solution stays inside the domain of $f$ with bounded values — and here the domain is all of $\mathbb{R}$, so only the blow-up limits it.


