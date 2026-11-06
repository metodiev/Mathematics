# Principles of Modeling — Solutions

> [Principles of Modeling](README.md) · Solutions to the 36 problems in [exercises.md](exercises.md)

Each solution states the strategy, then carries out every significant step. Proofs are complete. Numerical answers are checked, usually by a second route. Where several approaches exist, a remark names the alternative.

## Beginner

**1.** *Strategy: express each quantity in the definitions and read off the exponents of $M, L, T$.*

(a) $p = mv$ has dimension $M\cdot LT^{-1} = MLT^{-1}$.

(b) Torque is force times a perpendicular distance: $MLT^{-2}\cdot L = ML^2T^{-2}$. That is the same dimension as energy, which is why torque is measured in N·m rather than J: the dimensions agree but the quantities are different, and the distinction lives in the geometry, not in the units.

(c) Angular momentum $L = mvr$: $M\cdot LT^{-1}\cdot L = ML^2T^{-1}$.

(d) From $F = GmM/r^2$, solve: $G = Fr^2/(mM)$, so
$$[G] = \frac{MLT^{-2}\cdot L^2}{M^2} = L^3M^{-1}T^{-2}.$$
*Check.* In SI, $G = 6.674\times10^{-11}\ \mathrm{m^3\,kg^{-1}s^{-2}}$, matching.

(e) $E$ is power per area, so $[E] = ML^2T^{-3}/L^2 = MT^{-3}$. From $E = \sigma T^4$,
$$[\sigma] = \frac{MT^{-3}}{\Theta^4} = MT^{-3}\Theta^{-4}.$$
*Check.* $\sigma = 5.670\times10^{-8}\ \mathrm{W\,m^{-2}K^{-4}}$, and $1\ \mathrm{W} = 1\ \mathrm{kg\,m^2\,s^{-3}}$, so the units are $\mathrm{kg\,s^{-3}K^{-4}} = MT^{-3}\Theta^{-4}$.

**2.** *Strategy: reduce both sides to exponent vectors in $(M,L,T)$ and compare component by component.*

| | Left | Right | Homogeneous? |
|---|---|---|---|
| (a) | $L^2T^{-2}$ | $LT^{-2}\cdot L = L^2T^{-2}$ | yes |
| (b) | $L$ | $LT^{-2}\cdot T^3 = LT$ | **no** |
| (c) | $ML^2T^{-3}$ | $ML^{-3}\cdot LT^{-2}\cdot L\cdot L^3T^{-1} = ML^2T^{-3}$ | yes |
| (d) | $MLT^{-2}$ | $ML^{-1}T^{-1}\cdot L^2\cdot LT^{-1}/L = MLT^{-2}$ | yes |
| (e) | $T$ | $\sqrt{L/(LT^{-2})} = \sqrt{T^2} = T$ | yes |
| (f) | $ML^2T^{-2}$ | $M(LT^{-1})^2 = ML^2T^{-2}$; $M\cdot LT^{-2}\cdot L = ML^2T^{-2}$ | yes |

Only (b) fails: its right-hand side has an extra factor of $T$. The formula $\tfrac12at^3$ would be a *jerk* term integrated twice, i.e. a displacement only if the acceleration were a rate of change of acceleration.

**3.** *Strategy: multiply by conversion factors written as fractions equal to one, so units cancel.*

(a) $100\ \mathrm{km\,h^{-1}} = 100\times\dfrac{1000\ \mathrm{m}}{3600\ \mathrm{s}} = \dfrac{100}{3.6} = 27.8\ \mathrm{m\,s^{-1}}$.

(b) $1\ \mathrm{g\,cm^{-3}} = \dfrac{10^{-3}\ \mathrm{kg}}{(10^{-2}\ \mathrm{m})^3} = \dfrac{10^{-3}}{10^{-6}} = 1000\ \mathrm{kg\,m^{-3}}$.

(c) $1\ \mathrm{kWh} = 10^3\ \mathrm{W}\times3.6\times10^3\ \mathrm{s} = 3.6\times10^6\ \mathrm{J}$.

(d) $1\ \mathrm{bar} = 10^5\ \mathrm{Pa}$ (by definition).

(e) $30$ miles per US gallon $= 30\times\dfrac{1.609344\ \mathrm{km}}{3.785412\ \mathrm{L}} = 12.754\ \mathrm{km\,L^{-1}}$, hence $100/12.754 = 7.84\ \mathrm{L\,per\ 100\ km}$.

All five are unit conversions of dimensional quantities. None is a dimensionless ratio; the corresponding dimensionless quantity in (b) would be specific gravity, the ratio of a density to that of water, which is $1$ in these units and is unchanged by any conversion. *Remark:* (e) is not a linear rescaling of the *number* in the way (a)–(d) are, because fuel economy per volume and fuel per distance are reciprocal; a factor applied to one is applied inversely to the other.

**4.** *Strategy: one state, two fluxes.*

(a) The state variable is $B$, the balance in the account. The rate terms are the interest $rB$ (inflow, proportional to the state) and the withdrawal $w$ (outflow, constant). The balance law is
$$\dot B = rB - w .$$

(b) This is linear and non-homogeneous. Rewrite $\dot B - rB = -w$ and multiply by the integrating factor $e^{-rt}$:
$$\frac{d}{dt}\left(Be^{-rt}\right) = -we^{-rt} \;\Longrightarrow\; Be^{-rt} = \frac{w}{r}e^{-rt} + K .$$
Hence
$$B(t) = \frac{w}{r} + Ke^{rt}, \qquad B(0) = B_0 \;\Longrightarrow\; K = B_0 - \frac{w}{r},$$
so
$$B(t) = \left(B_0 - \frac{w}{r}\right)e^{rt} + \frac{w}{r}.$$

(c) Setting $\dot B = 0$ gives $B^* = w/r$. Since $\dfrac{\partial}{\partial B}(rB - w) = r > 0$, the equilibrium is **unstable**: any balance above $w/r$ grows without bound, and any below declines without bound. An account whose interest does not cover its withdrawals eventually empties — here, exponentially.

(d) With $B_0 = 1000$, $r = 0.05$, $w = 100$: $w/r = 2000$, so
$$B(10) = (1000 - 2000)e^{0.5} + 2000 = -1000(1.64872) + 2000 = 351.28 .$$
*Check.* $\dot B = 0.05(351.28) - 100 = 17.56 - 100 = -82.44$, and differentiating the solution gives $-1000(0.05)e^{0.5} = -82.44$, matching. The account reaches zero when $(B_0 - w/r)e^{rt} = -w/r$, i.e. $e^{rt} = 2$, at $t = \ln 2/0.05 = 13.86$ years.

**5.** *Strategy: $m = n - \operatorname{rank} A$, and $m=0$ means "a relation with no free argument", i.e. a constant.*

(a) $(F, m, a)$: $n = 3$, the dimensions used are $M, L, T$, and the three columns are independent, so $k = 3$ and $m = 0$. The theorem gives one relation among the three quantities with no free group: $F/(ma)$ is a dimensionless constant. Newton's law supplies the value $1$.

(b) $(T, L, g)$: $k = 2$ (only $L$ and $T$ occur), $n = 3$, $m = 1$: $T\sqrt{g/L} = C$.

(c) $(T, L, g, m)$: the mass column is $M$-only and independent, so $k = 3$, $n = 4$, $m = 1$. The single group is again $T\sqrt{g/L}$; the exponent of $m$ in it is forced to be zero, which is the formal reason the period is independent of the mass.

(d) $(v, g, h)$: $k = 2$, $n = 3$, $m = 1$: $v/\sqrt{gh} = C$.

(e) $(p, \rho, v)$: $k = 3$ (all of $M, L, T$ are used and the three columns are independent), $n = 3$, $m = 0$: the quantities must satisfy $p/(\rho v^2) = C$. This is the origin of the "dynamic pressure" $\tfrac12\rho v^2$: the group exists, and only its numerical value requires physics.

**6.** *Strategy: build the dimension matrix, find the null space, then substitute the exact constant.*

(a) With rows $(M, T)$ and columns $(T, m, k)$, using $[k] = MT^{-2}$:
$$A = \begin{pmatrix}0&1&1\\ 1&0&-2\end{pmatrix}.$$
The rank is $2$, so $m = 3-2 = 1$. Solving $A\mathbf e = 0$ gives $e_m + e_k = 0$ and $e_T - 2e_k = 0$, so $\mathbf e \propto (1,-\tfrac12,-\tfrac12)$ and
$$\pi = T\sqrt{\frac{k}{m}} \;\Longrightarrow\; T = C\sqrt{\frac{m}{k}} .$$

(b) For $m = 0.5$ kg and $k = 200$ N/m,
$$T = 2\pi\sqrt{\frac{0.5}{200}} = 2\pi\sqrt{0.0025} = 2\pi(0.05) = 0.3142\ \mathrm{s}.$$
*Check.* $\omega = \sqrt{k/m} = \sqrt{400} = 20$ rad/s, and $T = 2\pi/\omega = 0.3142$ s.

(c) In the pendulum, the only quantity carrying mass is $m$ itself, so every dimensionless group must have exponent $e_m = 0$: mass cancels between the inertial term $m\ddot\theta$ and the weight $mg$. In the oscillator the restoring force $kx$ does not involve $m$, so the ratio of restoring force to inertia does involve $m$, and $m$ cannot cancel. Formally, the mass column $(1,0)$ is independent of the columns of $L$ and $T$ in the spring problem's augmented matrix, and it is the only mass column in the pendulum problem, which forces its exponent to vanish.

**7.** *Strategy: $T \propto g^{-1/2}$.*

$$\frac{T_{\text{Moon}}}{T_{\text{Earth}}} = \sqrt{\frac{g_{\text{Earth}}}{g_{\text{Moon}}}} = \sqrt{\frac{9.81}{1.62}} = \sqrt{6.0556} = 2.461 .$$
The period is $2.46$ times longer, i.e. the pendulum swings more slowly, because the restoring force is weaker while the inertia is unchanged.

**8.** *Strategy: lengths by $\lambda = 4$, areas by $\lambda^2$, volumes and masses by $\lambda^3$; stress by $\lambda$ at constant density.*

| Quantity | Ratio |
|---|---|
| surface area | $4^2 = 16$ |
| volume | $4^3 = 64$ |
| mass (same material) | $64$ |
| compressive stress in a leg | $4$ |

The stress ratio follows from $\sigma = Mg/A$: the numerator grows like $\lambda^3$ and the denominator like $\lambda^2$, leaving $\lambda = 4$. A statue four times taller, in the same stone, carries four times the stress at the base.

**9.** *Strategy: replace $L$ by $M^{1/3}$ in each scaling law.*

(a) area $\propto L^2 = (M^{1/3})^2$: exponent $2/3$.

(b) density is constant: exponent $0$.

(c) buoyancy $= \rho_f V g \propto L^3$: exponent $1$.

(d) $v \propto \sqrt{mg/(\rho C_DA)}$, with $m \propto L^3$ and $A \propto L^2$: $v^2 \propto L^3/L^2 = L$, so $v \propto L^{1/2} = M^{1/6}$. Larger bodies fall (in the quadratic-drag regime) faster, but only as the sixth root of mass — a $64$-fold mass increase raises terminal speed by only $2$.

**10.** *Strategy: count the combinations that actually appear.*

(a) Substituting $(a,b) \to (ta, b/t)$ for any $t \ne 0$ leaves $ab$ unchanged and hence leaves every prediction unchanged. The map from parameters to predictions is not injective, so no data — however plentiful — can separate $a$ from $b$. There is a one-dimensional *non-identifiability*.

(b) The identifiable parameter is $ab$. From the data, $y/x = 3/1 = 3$, $6/2 = 3$, $9/3 = 3$, so $ab = 3$, and the fit is exact for every pair with product $3$.

(c) The model $y = a+b$ is a constant. The data are $3, 6, 9$, not constant, so no choice of $(a,b)$ fits. Calibration would return the least-squares constant, the mean $6$, with residuals $-3, 0, +3$, and the identifiable combination $a+b = 6$ would be all the data determine — the split between $a$ and $b$ being arbitrary. The example shows the difference between a model that is unidentified (a, b) and one that is wrong (c).

**11.** *Strategy: $y$ is a product of powers, so the sensitivities are the exponents.*

Since $\ln y = 2\ln a - \tfrac12\ln b + \ln c$,
$$S_a = 2, \qquad S_b = -\tfrac12, \qquad S_c = 1 .$$

(i) **Worst case**, all errors aligned and of the same sign in the exponent:
$$\left\lvert\frac{\delta y}{y}\right\rvert \le (2 + 0.5 + 1)(3\%) = 10.5\%.$$

(ii) **Independent errors**, added in quadrature:
$$\frac{\delta y}{y} \approx \sqrt{(2\cdot3)^2 + (0.5\cdot3)^2 + (1\cdot3)^2}\% = \sqrt{36 + 2.25 + 9}\% = \sqrt{47.25}\% = 6.87\%.$$

The worst-case bound is half as large again as the quadrature estimate; reporting the larger one is conservative, reporting the smaller one requires the independence assumption to be stated.

**12.** *(open)* *Strategy: apply the checklist of §7.14 in order and make every item falsifiable.*

A model answer follows; any answer meeting the criteria in the final paragraph is acceptable.

*Question and tolerance.* "What is the median waiting time from arrival to triage, and how does it vary by hour of day? Tolerance: ±5 minutes on the median."

*Boundary.* The waiting room and the triage station. Arrivals enter; triaged patients leave. Staff breaks and shift changes are inside the model as capacity changes.

*State variables.* Number of patients waiting $n(t)$; the number of nurses on duty $c(t)$ (a scheduled, hence known, function of time).

*Rate laws.* Arrivals: a non-homogeneous Poisson process with rate $\lambda(t)$ estimated in 15-minute bins. Service: each nurse sees patients at rate $\mu$, so the total service rate is $\mu\min(n,c)$ (work-conserving, no idling while a queue exists).

*Assumptions, with kind.* (structural) patients are homogeneous — no priority classes; (structural) single pooled queue, first-come-first-served; (constitutive) exponential service times with constant $\mu$, i.e. no complexity-dependent triage; (parametric) $\lambda(t)$ and $\mu$ constant within each bin and stable across weeks; (domain) the model is claimed valid for $n \le 30$ and $c \ge 1$, where blocking and corridor crowding are absent.

*Outputs.* Time series of $n(t)$; median and 90th percentile wait by hour.

*Validation test.* Hold out the most recent four weeks. Predict the median wait per hour from the arrival and staffing data alone, and compare with the recorded waits. The test is feasible because both the inputs and the observed waits are already recorded by the triage system; it is meaningful because it is out of sample in time, which is the regime in which a queueing model typically fails.

*What makes an answer acceptable.* It must (i) contain at least one assumption of each of the four kinds, (ii) state a tolerance numerically, (iii) specify a validation that uses data not used in calibration, and (iv) state at least one condition under which the model is not claimed to hold.

## Intermediate

**13.** *Strategy: build the group containing $R$, then check the exact solution.*

(a) With rows $(L,T)$ and columns $(R,v,g)$:
$$A = \begin{pmatrix}1&1&1\\ 0&-1&-2\end{pmatrix}, \qquad k = 2,\quad n = 3,\quad m = 1 .$$
The null space: $e_R + e_v + e_g = 0$ and $-e_v - 2e_g = 0$, so $e_v = -2e_g$ and $e_R = e_g$. With $e_g = -1$, $\mathbf e = (-1,2,-1)$ and
$$\pi = \frac{v^2}{gR} \;\Longrightarrow\; R = \frac{v^2}{g}\Phi(\theta).$$
The angle $\theta$ is dimensionless, contributes no rank, and appears as an argument of $\Phi$ — it is not eliminated.

(b) With $v = 20$ m/s and $g = 9.81$ m/s²: $v^2/g = 400/9.81 = 40.77$ m.

| $\theta$ | $\sin 2\theta$ | $R$ (m) |
|---|---|---|
| $15°$ | $\sin 30° = 0.5$ | $20.39$ |
| $45°$ | $\sin 90° = 1$ | $40.77$ |
| $75°$ | $\sin 150° = 0.5$ | $20.39$ |

The symmetry $\Phi(15°) = \Phi(75°)$ holds.

(c) Dimensional analysis supplied the *form*: the range is proportional to $v^2$, inversely proportional to $g$, and equal to $v^2/g$ times a function of the angle only. It did not supply $\Phi$; it did not predict that the maximum is at $45°$ (that needs the identity $\max\sin2\theta = 1$); and it did not predict the symmetry — all three facts come from the exact solution.

**14.** *Strategy: one group from $D$, $L$, $\tau$; then arithmetic.*

(a) $[D] = L^2T^{-1}$. The three quantities $D, L, \tau$ have dimensions spanning $L$ and $T$ with rank $2$, so $m = 3-2 = 1$; the group is $D\tau/L^2$. Since a dimensionless group must be a constant of order one for a diffusive process,
$$\frac{D\tau}{L^2} \sim 1 \;\Longrightarrow\; \tau \sim \frac{L^2}{D}.$$

(b) With $D = 10^{-9}$ m²/s:

| $L$ | $\tau = L^2/D$ | in familiar units |
|---|---|---|
| $10^{-3}$ m | $10^{3}$ s | $16.7$ min |
| $10^{-2}$ m | $10^{4}$ s | $2.78$ h |
| $1$ m | $10^{9}$ s | $31.7$ yr |

(c) $L = \sqrt{D\tau} = \sqrt{10^{-9}\times3600} = \sqrt{3.6\times10^{-6}} = 1.90\times10^{-3}$ m, about $1.9$ mm in an hour.

(d) A cell is about $10$ µm $=10^{-5}$ m across, so $\tau \sim 10^{-10}/10^{-9} = 0.1$ s: diffusion is fast enough. A metre-scale organism would need decades, so it must move the solute itself — which is why large animals have circulatory systems and why plants have vascular tissue. The crossover, at $L \approx \sqrt{D\times(\text{a few seconds})} \approx 10^{-4}$ m, is roughly the size of a small organism.

**15.** *Strategy: Froude matching gives $v_m = v_p\sqrt{\lambda}$ and hence $t_m = t_p\sqrt{\lambda}$; Reynolds matching gives $v_m = v_p/\lambda$.*

(a) Velocity scales as $\sqrt{\lambda}$ and length as $\lambda$, so time scales as $\lambda/\sqrt{\lambda} = \sqrt{\lambda}$. With $\lambda = 1/25$:
$$T_m = T_p\sqrt{\lambda} = 8\times\frac15 = 1.6\ \mathrm{s}.$$

(b) $v_m = v_p\sqrt{\lambda} = 2\times\tfrac15 = 0.4$ m/s.

(c) Reynolds matching requires $v_m = v_p/\lambda = 2\times25 = 50$ m/s. The ratio of the two required speeds is $50/0.4 = 125 = \lambda^{-3/2} = 25^{3/2}$, so no single test speed satisfies both conditions with the same fluid. The physical reason is that gravity and viscosity scale differently with size: wave-making resistance is governed by a balance of inertia and weight, skin friction by a balance of inertia and viscosity, and shrinking the model changes the two ratios differently.

**16.** *Strategy: divide by $M$; then take ratios of the scaling law.*

(a) $\dfrac{B}{M} = B_0M^{3/4-1} = B_0M^{-1/4}$.

(b) The ratio for mouse : elephant is
$$\left(\frac{M_{\text{elephant}}}{M_{\text{mouse}}}\right)^{1/4} = \left(\frac{5000}{0.030}\right)^{1/4} = (1.6667\times10^{5})^{1/4} = 20.2 .$$
The mouse burns about twenty times as much energy per gram per day.

(c) With $f \propto M^{-1/4}$ the heart-rate ratio is also $20.2$: the mouse's heart beats about twenty times faster. Lifespan $\propto M^{1/4}$ gives the reciprocal factor, so the product
$$f\times(\text{lifespan}) \propto M^{-1/4}\cdot M^{1/4} = M^0$$
is predicted to be independent of body mass. Measurements across mammals give roughly $1$–$2\times10^{9}$ heartbeats for most species, which is the empirical content of the prediction. *Caution:* this is a scaling regularity with large scatter, not a law; it does not hold across all vertebrates, and it does not explain anything by itself.

**17.** *Strategy: differentiate logarithmically, then check against exact values.*

(a) Write $\ln y = \ln a - \ln(b-c)$. Then
$$\frac{\partial \ln y}{\partial \ln c} = c\,\frac{\partial}{\partial c}\left[-\ln(b-c)\right] = c\cdot\frac{1}{b-c} = \frac{c}{b-c},$$
where the middle step uses $\dfrac{d}{dc}\ln(b-c) = \dfrac{-1}{b-c}$. So
$$S_c = \frac{c}{b-c}.$$
*Check by direct differentiation:* $\dfrac{\partial y}{\partial c} = \dfrac{a}{(b-c)^2}$, and $\dfrac{a}{(b-c)^2}\cdot\dfrac{c}{a/(b-c)} = \dfrac{c}{b-c}$, matching.

(b) At $c = 4$: $S_c = 4/(5-4) = 4$. At $c = 4.9$: $S_c = 4.9/0.1 = 49$.

(c) $y(4) = 10/1 = 10$; $y(4.9) = 10/0.1 = 100$. The relative change in $c$ is $0.9/4 = 22.5\%$, and the relative change in $y$ is $900\%$ — a factor of $40$, not the factor of $4\times22.5\% = 90\%$ that the sensitivity at $c = 4$ would predict. The reason is that the sensitivity is not constant: it is itself growing as $c \to b$, so a linear extrapolation over a finite interval fails badly.

(d) The model is useless for *prediction* whenever $b - c$ is a small difference of two large quantities, because the difference is what carries all the information. An error of $1\%$ in either $b$ or $c$ alters the difference by an amount comparable to the difference itself. This structure appears physically whenever a small net quantity is the difference of large opposing terms — a net growth rate $r - h$, a net reproduction number $R_0 - 1$, a net profit — and it is the reason such quantities are hard to measure.

**18.** *Strategy: use the given numerical values and keep the dimensionless argument explicit.*

(a) An angle is a ratio of two lengths and is dimensionless, so its dimension vector is zero and it contributes no column to $A$. It cannot appear in any group; instead it is an extra argument of the undetermined function. Formally, the list $(T, L, g, \theta_0)$ has $n = 4$, $k = 2$, $m = 2$, with groups $T\sqrt{g/L}$ and $\theta_0$.

(b) $T\sqrt{g/L} = \Phi(\pi/2) = 7.416$, and $\sqrt{L/g} = \sqrt{1/9.81} = 0.31928$ s. So
$$T = 7.416\times0.31928 = 2.368\ \mathrm{s},$$
against the small-angle value $2\pi\times0.31928 = 2.006$ s. The large-amplitude period is $18.0\%$ longer.

(c) A dimensionless input is invisible to the dimensional argument: it is neither eliminated nor determined. Dimensional analysis therefore cannot predict any quantity that depends on a dimensionless parameter — the amplitude here, a Reynolds number in fluid mechanics, a ratio of rates in population biology. For such quantities, only a model or a measurement can supply the value.

**19.** *Strategy: differentiate $N^*$ and normalise.*

(a) $N^* = K(1 - h/r)$, so $\partial N^*/\partial h = -K/r$ and
$$S_h = \frac{\partial N^*}{\partial h}\cdot\frac{h}{N^*} = -\frac{K}{r}\cdot\frac{h}{K(1-h/r)} = -\frac{h}{r-h}.$$

(b) At $h = 0.5r$: $S_h = -0.5r/0.5r = -1$. At $h = 0.9r$: $S_h = -0.9r/0.1r = -9$.

(c) As $h \uparrow r$ the denominator tends to zero and $S_h \to -\infty$: the predicted equilibrium becomes arbitrarily sensitive to the harvest rate, and at $h = r$ the positive equilibrium ceases to exist. This is a **transcritical bifurcation**: the equilibrium $N^* = K(1-h/r)$ crosses the always-present equilibrium $N = 0$ and exchanges stability with it. A management policy set at $h$ close to $r$ is therefore a policy whose predicted outcome cannot be relied on, however accurate the estimate of $r$.

**20.** *Strategy: differentiate $H$ along a solution, then classify claims as predictions or artefacts.*

(a) With $H(x,y) = \delta x - c\ln x + by - a\ln y$,
$$\frac{\partial H}{\partial x} = \delta - \frac{c}{x}, \qquad \frac{\partial H}{\partial y} = b - \frac{a}{y}.$$
Then
$$\dot H = \left(\delta - \frac{c}{x}\right)(ax - bxy) + \left(b - \frac{a}{y}\right)(\delta xy - cy).$$
Factor the first bracket as $\dfrac{\delta x - c}{x}$ and the first rate as $x(a - by)$; factor the second bracket as $\dfrac{by-a}{y}$ and the second rate as $y(\delta x - c)$. Then
$$\dot H = (\delta x - c)(a - by) + (by - a)(\delta x - c) = (\delta x - c)\bigl[(a-by) + (by-a)\bigr] = 0 .$$
So $H$ is constant along every solution, and each orbit lies in a level set of $H$.

(b) *Genuine predictions.* (i) The populations oscillate indefinitely rather than settling; (ii) the long-run averages satisfy $\bar x = c/\delta$ and $\bar y = a/b$, independently of the initial condition — a statement that can be checked against a long time series even though the cycle amplitude is not predicted.

*Artefacts.* (i) The amplitude and period are fixed by the initial condition and never decay: a centre is structurally fragile, and any small additional mechanism (predator satiation, prey self-limitation, seasonal forcing) destroys it. (ii) The predator has no extinction threshold and no satiation, so the model predicts predators persist at arbitrarily low prey density and that enriching the prey always helps the predator.

(c) *Design.* Take replicate systems started from different initial abundances. Under the model, the cycle amplitude is a permanent memory of the start; under any damped alternative, all replicates converge to the same attractor. Equivalently, perturb a single system by removing a fixed fraction of each species and observe whether the subsequent amplitude returns to its previous value (a genuine centre, as the model asserts) or decays toward a common cycle or equilibrium. The test is decisive because it distinguishes *neutral* from *stable* recurrence, which is precisely the property at issue.

**21.** *Strategy: one state, two removal rates, both proportional to the state.*

(a) The state is the concentration $C$. With inflow concentration $C_{in} = 0$,
$$V\frac{dC}{dt} = q(C_{in} - C) - kVC \;\Longrightarrow\; \frac{dC}{dt} = -\left(\frac{q}{V} + k\right)C .$$
The two rate terms are dilution at rate $q/V$ (the pollutant leaves with the outflow) and decay at rate $k$.

(b) Separating, $\ln C = -(q/V + k)t + \text{const}$, so
$$C(t) = C_0e^{-(q/V + k)t}.$$

(c) $q/V = 5/10^{7} = 5\times10^{-7}$ s⁻¹ and $k = 2\times10^{-7}$ s⁻¹, so the total rate is $7\times10^{-7}$ s⁻¹ and
$$t_{10\%} = \frac{\ln 10}{7\times10^{-7}} = \frac{2.3026}{7\times10^{-7}} = 3.29\times10^{6}\ \mathrm{s} = 38.1\ \mathrm{days}.$$

(d) The pollutant's residence time is $1/(q/V + k) = 1.43\times10^{6}$ s $= 16.5$ days. The hydraulic residence time is $V/q = 2\times10^{6}$ s $= 23.1$ days. The pollutant's residence is shorter because two independent removal mechanisms act: it is flushed out at the hydraulic rate and it also decays. When $k \ll q/V$ the two coincide, which is the check that the algebra is right.

**22.** *Strategy: maximise the flux parabola; differentiate it for the wave speeds; average for the shock.*

(a) $q(\rho) = v_{\max}\rho(1 - \rho/\rho_{\max})$ is a downward parabola with roots at $0$ and $\rho_{\max}$, so its maximum is at the midpoint:
$$\rho_c = \frac{\rho_{\max}}{2} = 70\ \mathrm{veh/km}, \qquad q_{\max} = v_{\max}\frac{\rho_{\max}}{4} = 100\times\frac{140}{4} = 3500\ \mathrm{veh/h}.$$

(b) $c(\rho) = q'(\rho) = v_{\max}(1 - 2\rho/\rho_{\max})$:
$$c(42) = 100(1-0.6) = +40\ \mathrm{km/h},\quad c(70) = 0,\quad c(112) = 100(1-1.6) = -60\ \mathrm{km/h}.$$
At low density disturbances travel downstream with the traffic; at capacity they stand still; above capacity they travel upstream, which is the direction jams propagate.

(c) $s = v_{\max}\left(1 - \dfrac{\rho_1+\rho_2}{\rho_{\max}}\right) = 100\left(1 - \dfrac{140}{140}\right) = 0$. The shock is stationary. *Check by direct computation:* $q(50) = 100\cdot50(1 - 50/140) = 5000\times0.6429 = 3214$ veh/h and $q(90) = 9000(1 - 90/140) = 9000\times0.3571 = 3214$ veh/h; equal fluxes across the jump mean no net accumulation, so the interface does not move.

(d) The linear speed–density law is a crude fit: real data show speed nearly constant at low density, then falling sharply near jam density, and the measured capacity per lane is about $2000$–$2400$ veh/h, well below the $3500$ this parabola predicts. A triangular or Newell fundamental diagram fits better; the qualitative conclusions about wave direction survive the change, which is why the model is useful despite the poor capacity estimate.

## Advanced

**23.** *Strategy: pass to logarithms, where the unit-scaling group becomes a translation, and use rank–nullity to quotient it out.*

**Theorem.** Let $q_1,\dots,q_n > 0$ have dimension matrix $A = (a_{ij}) \in \mathbb{Z}^{k\times n}$ of rank $k$, and let $f:\mathbb{R}_{>0}^n\to\mathbb{R}$ satisfy
$$f\left(\lambda_1^{a_{11}}\cdots\lambda_k^{a_{k1}}q_1,\ \dots,\ \lambda_1^{a_{1n}}\cdots\lambda_k^{a_{kn}}q_n\right) = f(q_1,\dots,q_n)$$
for all $\lambda \in \mathbb{R}_{>0}^k$. Then there are $m = n-k$ dimensionless groups $\pi_1,\dots,\pi_m$ and a function $F$ of $m$ variables with $f(q) = F(\pi_1(q),\dots,\pi_m(q))$.

**Proof.** Define $u_j = \ln q_j$ and $g(u) = f(e^{u_1},\dots,e^{u_n})$. The substitution $q_j \mapsto \lambda_1^{a_{1j}}\cdots\lambda_k^{a_{kj}}q_j$ becomes, in logarithms,
$$u_j \longmapsto u_j + \sum_{i=1}^{k}a_{ij}\ln\lambda_i = \left(u + A^{\mathsf T}w\right)_j, \qquad w := (\ln\lambda_1,\dots,\ln\lambda_k),$$
so the hypothesis is equivalent to
$$g(u + A^{\mathsf T}w) = g(u)\quad\text{for all } u\in\mathbb{R}^n,\ w\in\mathbb{R}^k. \tag{$*$}$$

*Where the rank hypothesis enters.* Since $\operatorname{rank}A = k$, the columns of $A$ span $\mathbb{R}^k$, so we may permute the quantities (which relabels the coordinates of $u$ and the columns of $A$) so that the first $k$ columns are linearly independent. Write $A = (A_1\ \ A_2)$ with $A_1$ a $k\times k$ invertible block and $A_2$ of size $k\times m$. Split $u = (u_I, u_{II})$ accordingly. Then $A_1^{\mathsf T}$ is invertible, so for each $u$ there is exactly one $w$ with
$$A_1^{\mathsf T}w = -u_I, \qquad\text{namely}\qquad w = -(A_1^{\mathsf T})^{-1}u_I .$$
For this $w$,
$$\left(u + A^{\mathsf T}w\right)_I = u_I + A_1^{\mathsf T}w = 0, \qquad \left(u + A^{\mathsf T}w\right)_{II} = u_{II} + A_2^{\mathsf T}w = u_{II} - A_2^{\mathsf T}(A_1^{\mathsf T})^{-1}u_I .$$
Applying $(*)$ with this $w$,
$$g(u) = g\left(0,\ u_{II} - Cu_I\right), \qquad C := A_2^{\mathsf T}(A_1^{\mathsf T})^{-1} \in \mathbb{R}^{m\times k}.$$
So $g$ depends only on the $m$ numbers $(u_{II} - Cu_I)_i = u_{k+i} - \sum_{j\le k}c_{ij}u_j$. Exponentiating,
$$f(q) = g(\ln q) = G\left(\ln q_{k+1} - \sum_{j\le k}c_{1j}\ln q_j,\ \dots,\ \ln q_{n} - \sum_{j\le k}c_{mj}\ln q_j\right) = F(\pi_1,\dots,\pi_m)$$
with
$$\pi_i = q_{k+i}\prod_{j=1}^{k}q_j^{-c_{ij}}, \qquad i = 1,\dots,m,$$
and $F$ the function of $m$ variables $F(z) = G(e^{z_1},\dots,e^{z_m})$. Each $\pi_i$ is dimensionless because the exponent vector $(-c_{i1},\dots,-c_{ik},\,0,\dots,1,\dots,0)$ lies in $\ker A$: for every row $r$,
$$\sum_{j\le k}a_{rj}(-c_{ij}) + a_{r,k+i} = -\sum_{j\le k}(A_1)_{rj}\sum_s a_{s,k+i}(A_1^{-1})_{js} + a_{r,k+i} = -a_{r,k+i} + a_{r,k+i} = 0,$$
using $c_{ij} = \sum_s a_{s,k+i}(A_1^{-1})_{js}$. The groups are independent because their logarithms are the coordinates of the invertible linear map $u \mapsto (0, u_{II} - Cu_I)$, and there are exactly $m = n-k$ of them, which is $\dim\ker A$. $\blacksquare$

*Remark.* The proof is constructive: it says "express $m$ of the quantities in terms of the other $k$", which is exactly Gaussian elimination on the dimension matrix. It also shows the theorem is sharp — the function $F$ is an arbitrary function of $m$ variables and the argument gives no information about it.

**24.** *Strategy: every statement about bases of a single subspace is a statement about invertible matrices.*

(a) Two bases $\{\mathbf e^{(j)}\}$ and $\{\mathbf f^{(i)}\}$ of the same $m$-dimensional subspace $\ker A$ are related by a change of basis. Concretely, expanding each $\mathbf f^{(i)}$ in the first basis gives $\mathbf f^{(i)} = \sum_j M_{ji}\mathbf e^{(j)}$, and the matrix $M$ is invertible because the reverse expansion exists (it is the coordinate matrix of a basis in a basis).

(b) With $\pi_j = \prod_k q_k^{e^{(j)}_k}$ and $\pi'_i = \prod_k q_k^{f^{(i)}_k}$,
$$\pi'_i = \prod_k q_k^{\sum_j M_{ji}e^{(j)}_k} = \prod_j\left(\prod_k q_k^{e^{(j)}_k}\right)^{M_{ji}} = \prod_j \pi_j^{M_{ji}} .$$
The map $\pi \mapsto \pi'$ given by these monomials is invertible, with inverse given by $M^{-1}$, so either set of groups determines the other and hence either can be substituted into $F$. The *pair* of conditions "$\mathrm{Re}$ matches" and "$F$'s value matches" is the same statement in either basis.

(c) Take $\mathbf e^{(1)} = (-1,2,2,1,0)$ and $\mathbf e^{(2)} = (-1,1,1,0,1)$, giving
$$\pi_1 = \frac{\rho v^2R^2}{F}, \qquad \pi_2 = \frac{\mu Rv}{F}.$$
Now take $\mathbf f^{(1)} = \mathbf e^{(1)}$ and $\mathbf f^{(2)} = \mathbf e^{(1)} - \mathbf e^{(2)} = (0,1,1,1,-1)$, so
$$M = \begin{pmatrix}1&1\\0&-1\end{pmatrix}, \qquad \mathbf f^{(2)} = \mathbf e^{(1)} - \mathbf e^{(2)} .$$
Then
$$\pi'_2 = \pi_1\pi_2^{-1} = \frac{\rho v^2R^2/F}{\mu Rv/F} = \frac{\rho vR}{\mu} = \mathrm{Re},$$
and the pair becomes $(\rho v^2R^2/F,\ \mathrm{Re})$ — the same physical content, expressed in the variables engineers name. This is the practical reason the freedom matters: a good basis turns an unintelligible group into a named dimensionless number.

**25.** *Strategy: each identity is the logarithm of a product, differentiated with respect to $\ln p$.*

Throughout, all quantities are positive and differentiable, and $S_p(\cdot)$ means $\dfrac{\partial}{\partial \ln p}\ln(\cdot)$.

(a) $\ln(fg) = \ln f + \ln g$, and $\dfrac{\partial}{\partial\ln p}$ is linear, so $S_p(fg) = S_p(f) + S_p(g)$.

(b) $\ln(f/g) = \ln f - \ln g$ gives $S_p(f/g) = S_p(f) - S_p(g)$.

(c) $\ln(f^{\alpha}) = \alpha\ln f$ gives $S_p(f^\alpha) = \alpha S_p(f)$.

(d) Let $y = f(g(p))$. By the chain rule in the form $\dfrac{d}{dt} = \dfrac{d}{d\ln g}\cdot\dfrac{d\ln g}{d\ln p}$,
$$S_p(y) = \frac{d\ln y}{d\ln p} = \frac{d\ln y}{d\ln g}\cdot\frac{d\ln g}{d\ln p} = S_g(f)\cdot S_p(g).$$

(e) *Error bound.* The total differential of $y = f(p_1,\dots,p_m)$ is $dy = \sum_i \dfrac{\partial y}{\partial p_i}dp_i$. Divide by $y$ and multiply each term by $p_i/p_i$:
$$\frac{dy}{y} = \sum_i \frac{\partial y}{\partial p_i}\cdot\frac{p_i}{y}\cdot\frac{dp_i}{p_i} = \sum_i S_i\,\frac{dp_i}{p_i} .$$
Replacing differentials by finite but small differences and applying the triangle inequality,
$$\left\lvert\frac{\delta y}{y}\right\rvert \le \sum_i \lvert S_i\rvert\left\lvert\frac{\delta p_i}{p_i}\right\rvert .$$
*Remark.* If the $\delta p_i/p_i$ are independent random variables with mean $0$ and variance $\sigma_i^2$, the variance of $\delta y/y$ is $\sum_i S_i^2\sigma_i^2$ to first order, by the standard variance of a linear combination. The two expressions answer different questions — a guarantee against the worst case, and an estimate under a probabilistic model — and both should carry their hypotheses when reported.

**26.** *Strategy: write the stress in terms of $L$, then impose constancy and see what must vary.*

(a) Let body mass be $M = \rho L^3$ with $\rho$ constant, and let the supporting member have cross-section $A \propto L^2$. Then
$$\sigma = \frac{Mg}{A} \propto \frac{L^3}{L^2} = L .$$
Compressive stress is proportional to the linear size.

(b) Require $\sigma$ constant. Then $A \propto M \propto L^3$, so the cross-section must grow as the *volume*, not the area. The member's volume is $\propto AL \propto L^4$, while body volume is $\propto L^3$, so the fraction
$$f = \frac{\text{member mass}}{\text{body mass}} \propto \frac{AL}{L^3} \propto \frac{L^4}{L^3} = L .$$
The fraction must grow linearly with body length.

(c) A $10$ m animal needs ten times the bone-mass fraction of a $1$ m animal. If the small animal spends $5\%$ of its mass on bone, the large one needs $50\%$ — and at that point the bones are carrying themselves, the available muscle mass collapses, and the geometric-similarity framework has long since failed. This is the cleanest quantitative argument for a maximum land-animal size, and it agrees with the observed trend that larger mammals have proportionally heavier skeletons.

**27.** *Strategy: existence by an explicit formula, uniqueness by counting roots.*

(a) *Existence.* The Lagrange polynomial
$$p(x) = \sum_{i=1}^{N}y_i\prod_{\substack{j=1\\ j\ne i}}^{N}\frac{x - x_j}{x_i - x_j}$$
has degree at most $N-1$ and satisfies $p(x_i) = y_i$ for every $i$, since every term but the $i$-th vanishes at $x_i$ and the $i$-th equals $y_i$.

*Uniqueness.* If $p$ and $q$ both interpolate, then $r = p - q$ has degree at most $N-1$ and $r(x_i) = 0$ for $N$ distinct points. A nonzero polynomial of degree $d$ has at most $d$ roots — otherwise, factoring out each root, it would have degree at least $d+1$ — so $r$ has at most $N-1$ roots unless $r \equiv 0$. Since it has $N$, $r \equiv 0$ and $p = q$.

(b) Applying (a) shows that for any data whatsoever the calibration error $\sum_k(y_k - p(x_k))^2$ can be made exactly zero. This is a statement about the *model class*, not about the data: the class of polynomials of degree $\le N-1$ has $N$ free coefficients, exactly enough to match $N$ observations.

(c) For the three points $(0,1), (1,2), (2,5)$ of Example 9.6, the unique interpolant in the class is $p(x) = 1+x^2$. The one-parameter family
$$p_k(x) = 1 + x^2 + k\,x(x-1)(x-2)$$
consists of cubics, which lie *outside* the degree-$\le 2$ class; each member has zero error at the three points and $p_k(3) = 10 + 6k$, so the prediction at $x = 3$ is arbitrary. The pair of statements — uniqueness inside the class, arbitrariness outside it — is the precise sense in which a good fit does not select a model.

(d) *Moral.* Model selection must use information not contained in the calibration residuals: prior structural knowledge, a penalty on the size of the class (regularisation, information criteria), or held-out data. The last is the only one that directly measures predictive performance, which is why it is the minimum credible standard of §7.8.

**28.** *Strategy: integrate the conservation law across a moving discontinuity.*

(a) Suppose $\rho$ takes the value $\rho_1$ for $x < x_s(t)$ and $\rho_2$ for $x > x_s(t)$, with the jump moving at speed $s = \dot x_s$. Consider a fixed window $[a,b]$ containing $x_s$. The number of cars in the window is
$$N(t) = \rho_1\left(x_s(t) - a\right) + \rho_2\left(b - x_s(t)\right),$$
so
$$\dot N = \rho_1 s - \rho_2 s = (\rho_1 - \rho_2)s .$$
Conservation of cars says $\dot N = q(a) - q(b) = q_1 - q_2$, the flux in minus the flux out. Equating,
$$(\rho_1 - \rho_2)s = q_1 - q_2 \;\Longrightarrow\; s = \frac{q_1 - q_2}{\rho_1 - \rho_2} = \frac{q(\rho_2) - q(\rho_1)}{\rho_2 - \rho_1}.$$

(b) With $q(\rho) = v_{\max}\rho(1 - \rho/\rho_{\max})$,
$$q(\rho_2) - q(\rho_1) = v_{\max}\left[\rho_2 - \frac{\rho_2^2}{\rho_{\max}} - \rho_1 + \frac{\rho_1^2}{\rho_{\max}}\right] = v_{\max}(\rho_2-\rho_1)\left[1 - \frac{\rho_1+\rho_2}{\rho_{\max}}\right],$$
using $\rho_2^2 - \rho_1^2 = (\rho_2-\rho_1)(\rho_2+\rho_1)$. Dividing,
$$s = v_{\max}\left(1 - \frac{\rho_1+\rho_2}{\rho_{\max}}\right).$$

(c) The shock is stationary when $\rho_1 + \rho_2 = \rho_{\max}$, i.e. when the two states carry equal flux — the two sides of the parabola in the $(\rho,q)$ plane at the same height. It propagates upstream ($s<0$) when $\rho_1+\rho_2 > \rho_{\max}$, both densities in the congested half of the diagram, and downstream ($s>0$) when the average density is below $\rho_{\max}/2$. *Check* against the direct formula with $\rho_1 = 60$, $\rho_2 = 100$, $\rho_{\max} = 120$, $v_{\max} = 80$: $s = 80(1 - 160/120) = -26.67$ km/h; directly, $q(60) = 2400$ and $q(100) = 80\cdot100\cdot(1/6) = 1333.3$, so $s = (1333.3-2400)/(100-60) = -26.67$. Agreement.

**29.** *Strategy: any schedule with an adjacent inversion can be improved, and repeated improvement must terminate at the SPT order.*

(a) Let two adjacent jobs $A$, $B$ start at time $t$ and let $S$ be the sum of completion times of all other jobs. If $A$ runs first, the pair contributes
$$C_A + C_B = (t+p_A) + (t+p_A+p_B) = 2t + 2p_A + p_B .$$
If $B$ runs first, the pair contributes $2t + 2p_B + p_A$. The rest is unchanged, because the completion time of every job after the pair is the same in either ordering. The difference is
$$\left(2t + 2p_A + p_B\right) - \left(2t + 2p_B + p_A\right) = p_A - p_B .$$
So if $p_A > p_B$ the first ordering is strictly worse, and swapping an adjacent inverted pair strictly decreases the objective.

Now take any schedule that is not SPT. It contains at least one adjacent pair with $p_A > p_B$ (if every adjacent pair were in non-decreasing order, the whole list would be sorted). Swapping strictly reduces $\sum C_j$; because there are finitely many schedules, repeated swapping cannot continue forever and must reach a schedule with no adjacent inversion, which is the SPT order. Every step strictly decreases the objective, so the SPT order is strictly better than any non-SPT schedule. $\blacksquare$

(b) SPT order $1,2,5,7$: completion times $1, 3, 8, 15$, sum $27$.
Given order $7,2,5,1$: $7, 9, 14, 15$, sum $45$.
Decreasing order $7,5,2,1$: $7, 12, 14, 15$, sum $48$.
*Check* with the identity $\sum_j C_j = \sum_j (n - j + 1)p_{(j)}$ for the sorted order: $4(1) + 3(2) + 2(5) + 1(7) = 4+6+10+7 = 27$, matching.

(c) With release dates the machine may profitably *idle*, so the completion time of a job is no longer the sum of the processing times of the jobs before it, the interchange computation above becomes invalid, and the problem is in fact NP-hard.

**30.** *Strategy: choose scales that make the coefficients one.*

(a) Set $N = Kx$ and $t = \tau/r$, so $\dfrac{dN}{dt} = K\dfrac{dx}{d\tau}\dfrac{d\tau}{dt} = Kr\,x'(\tau)$. The right side is $rKx(1-x)$. Equating and dividing by $Kr$,
$$x' = x(1-x).$$
Both parameters have disappeared.

(b) The general solution with $x(0) = x_0$ is
$$x(\tau) = \frac{1}{1 + \left(\frac{1-x_0}{x_0}\right)e^{-\tau}},$$
which contains no $r$ and no $K$. Hence every logistic population follows the same curve in scaled variables: the parameters only set the units of the axes. This is the simplest example of the reduction the π theorem promises.

(c) With $x_0 = 0.05$ and $x = 0.95$, start from $x = \dfrac{1}{1 + 19e^{-\tau}}$, which follows from $\dfrac{1-x_0}{x_0} = 19$. Then
$$1 + 19e^{-\tau} = \frac{1}{0.95} = 1.05263, \qquad e^{-\tau} = \frac{0.05263}{19} = 0.0027701,$$
so
$$\tau = -\ln(0.0027701) = 5.8889 .$$
With $r = 0.05$ yr⁻¹, $t = \tau/r = 117.8$ years. The answer depends only on $r$ because $K$ has been absorbed into the scale of $N$: changing $K$ stretches the vertical axis, not the clock.

## Challenge

**31.** *Strategy: apply the theorem in the degenerate cases $k=0$ and $k=n$.*

(a) If every $q_j$ is dimensionless then every column of $A$ is zero, so $A = 0$, $k = 0$ and $m = n$. The construction of Theorem 7.5.1 with the empty block $A_1$ gives $\pi_i = q_i$, so the conclusion is $f(q) = F(q_1,\dots,q_n)$ — a restatement of the hypothesis and no constraint at all. The theorem's content is proportional to the rank: it eliminates exactly as many arguments as there are independent dimensions.

(b) If $k = n$ then $A$ is square and invertible, so $\ker A = \{0\}$ and $m = 0$. The proof's step "$g(u) = g(0, u_{II} - Cu_I)$" now has an empty second block, giving $g(u) = g(0)$, a constant. Equivalently: with $A$ invertible, for any two points $q, q'$ in the positive orthant there is a $\lambda$ with $q' = \lambda\cdot q$, so invariance forces $f(q') = f(q)$ and $f$ is constant. Physically, a list in which every quantity is needed to fix the dimensions determines nothing but a single number, and that number must come from theory or experiment.

(c) The pendulum with amplitude has the list $(T, L, g, m, \theta_0)$: $n = 5$, $k = 3$, $m = 2$, with groups $\pi_1 = T\sqrt{g/L}$ and $\pi_2 = \theta_0$. Since $\theta_0$ is one of the groups, the law reads
$$T\sqrt{\frac{L}{g}} = \Phi(\theta_0),$$
and $\Phi$ is a function of a dimensionless argument. Case (a) applies to the sub-list consisting of $\theta_0$ alone: there $k = 0$, $m = 1$, and no constraint follows. The number $7.416 = \Phi(\pi/2)$ is therefore invisible to dimensional analysis, and can be obtained only by solving the equation of motion or by measuring.

**32.** *Strategy: compute the two branches separately, then examine the behaviour at the join.*

(a) For $p < 10$: $y = 0$, so $\ln y$ is undefined and $y$ is locally constant with value $0$; the natural statement is that $y$ does not change with $p$, i.e. $S_p = 0$ in the sense of zero absolute derivative. For $p>10$: $y = p-10$, so
$$S_p = \frac{p}{y}\cdot\frac{dy}{dp} = \frac{p}{p-10}.$$

(b) As $p \downarrow 10$ from above, $p/(p-10)\to+\infty$: a one per cent change in $p$ produces an unbounded *relative* change in $y$, because $y$ itself tends to zero. At $p = 10$ the derivative $dy/dp$ does not exist (the left and right derivatives are $0$ and $1$), so the model is not differentiable there and no linearisation exists. A local analysis evaluated at the kink is meaningless, and one evaluated nearby reports either "insensitive" or "infinitely sensitive" depending on the side.

(c) Over $p\in[5,15]$, $y$ runs from $0$ to $5$: an absolute range of $5$ and an unbounded relative range. Linearising on the upper branch at $p = 15$, where $S_p = 3$ and $dy/dp = 1$: the absolute prediction is exact (the branch is linear), so $\delta y = \delta p$ for any $\delta p \le 5$, giving $y=0$ at $p=10$. The relative-sensitivity formula $\delta y/y \approx S_p\,\delta p/p$ also gives the right answer at the endpoint, but for the accidental reason that $S_p\,y/p = 1$ identically on this branch. Just above the kink the same formula is worthless: at $p = 10.1$, $y = 0.1$ and $S_p = 101$, so a $1\%$ change in $p$ changes $y$ by $101\%$ — in absolute terms by $0.101$, which is negligible in whatever units $p$ carries.

(d) *Lesson.* Where an output can vanish or where the model has a threshold, relative sensitivity is the wrong instrument: report the *absolute* sensitivity $\partial y/\partial p$, the location of the threshold, and the region in which the output is identically zero. A relative sensitivity of $101$ sounds alarming and may correspond to a change of no practical consequence.

**33.** *Strategy: verify the algebra, expand in the small parameter, then interpret the conditioning of the inverse problem.*

(a) Starting from the standard form,
$$N = \frac{K}{1 + \frac{K-N_0}{N_0}e^{-rt}} = \frac{N_0}{\frac{N_0}{K} + \left(1 - \frac{N_0}{K}\right)e^{-rt}} .$$
Multiply numerator and denominator by $e^{rt}$:
$$N = \frac{N_0e^{rt}}{\frac{N_0}{K}e^{rt} + 1 - \frac{N_0}{K}} = \frac{N_0e^{rt}}{1 + \frac{N_0}{K}\left(e^{rt}-1\right)} .$$
At $t=0$ this is $N_0/1 = N_0$; as $t\to\infty$ it tends to $N_0e^{rt}/(\varepsilon e^{rt}) = K$. Both limits are right.

(b) With $\varepsilon = N_0/K$ and $\lvert\varepsilon(e^{rt}-1)\rvert < 1$,
$$\frac{1}{1+z} = 1 - z + O(z^2), \qquad z = \varepsilon(e^{rt}-1),$$
so
$$N(t) = N_0e^{rt}\left[1 - \varepsilon(e^{rt}-1) + O(\varepsilon^2)\right].$$

(c) Differentiating the leading correction with respect to $K$, and using $\partial\varepsilon/\partial K = -\varepsilon/K$:
$$\frac{\partial N}{\partial K} \approx N_0e^{rt}(e^{rt}-1)\frac{\varepsilon}{K} = O(K^{-2}),$$
because $\varepsilon/K = N_0/K^2$. Then
$$S_K = \frac{K}{N}\frac{\partial N}{\partial K} \approx \frac{K}{N_0e^{rt}}\cdot N_0e^{rt}(e^{rt}-1)\frac{\varepsilon}{K} = \varepsilon(e^{rt}-1).$$
The sign is positive, as it must be: raising the carrying capacity raises the population at any fixed time.

(d) *Interpretation.* When $N_0 \ll K$, the data from the exponential phase determine $r$ accurately (the slope of $\ln N$) and $K$ hardly at all, since $\lvert S_K\rvert = \varepsilon(e^{rt}-1)$ is small while the population is small compared with $K$. The inverse problem inherits this: if the data have relative precision $\eta$, the relative precision of $\hat K$ is about $\eta/\lvert S_K\rvert$, which can be far worse. With $\varepsilon = 0.01$ and $N = 10N_0$, solving $10 = e^{rt}/(1+0.01(e^{rt}-1))$ gives $e^{rt} = 11$, hence
$$S_K \approx 0.01\times(11-1) = 0.1 .$$
A $1\%$ error in $N$ consequently gives about $10\%$ error in $\hat K$, and a growth curve observed only to $10N_0$ cannot pin down the carrying capacity at all. This is the quantitative form of the warning in §7.8 about extrapolation and identifiability: the parameter that governs the *saturation* is not determined by data taken far from saturation.

**34.** *Strategy: standardise, read the tail probabilities from the given table, then vary the threshold.*

(a) Group A, mean $1$ and unit variance: $\Pr(s\ge1) = 1 - \Phi(0) = 0.5$. Group B, mean $0$: $\Pr(s\ge1) = 1 - \Phi(1) = 1 - 0.8413 = 0.1587$. The ratio is
$$\frac{0.1587}{0.5} = 0.317,$$
well below the conventional four-fifths ($0.8$) screening threshold.

(b) Removing the group label does not remove the disparity because the score remains a function of the inputs, and the inputs retain their association with group membership. The selection rate is $\Pr(s\ge\tau)$, a property of the *distribution* of $s$ in each group; if those distributions differ — for any reason, including a proxy — the rates differ. This is the failure of "fairness through unawareness": omitting a variable is not the same as removing its influence.

(c) Equal selection rates require $\Pr(s\ge\tau_B) = 0.5$ in group B, i.e. $\tau_B = \mu_B = 0$. That is a full standard deviation below the threshold applied to group A, and it is a policy choice with real consequences: it changes who is selected, and it may conflict with the predictive purpose of the score.

(d) Responses that keep the model: publish selection rates by group and audit them; apply a documented post-processing rule (group-specific thresholds, or randomisation at the boundary) chosen to meet a stated criterion; provide an individual appeal route with a human decision-maker. A response that requires discarding the model: using the score as the sole basis of an adverse decision that the affected person cannot contest, especially where the score's error rates differ by group. Which of these is appropriate is a policy and legal question, not a mathematical one; the mathematics supplies the numbers, and the numbers are what make the choice explicit.

**35.** *Strategy: cumulative counts. The queue is the difference between cumulative arrivals and cumulative departures, and the total delay is the area between those two curves.*

(a) During the overload the excess demand is $1800 - 1500 = 300$ veh/h for $0.5$ h, so the queue grows to
$$Q = 300\times0.5 = 150\ \text{vehicles}.$$

(b) After the overload, demand $1200$ veh/h is served at $1500$ veh/h, so the queue shrinks at $300$ veh/h and disappears after
$$t_{\text{clear}} = \frac{150}{300} = 0.5\ \text{h}.$$
So the *episode* lasts $1$ h in total, with the queue positive throughout.

(c) The queue profile is a triangle with base $1$ h and height $150$ vehicles, so the delay is its area:
$$\text{total delay} = \tfrac12\times150\times1.0 = 75\ \text{veh}\cdot\text{h}.$$
*Check by integration.* Cumulative arrivals minus departures is $300t$ for $0\le t\le 0.5$ and $300(1-t)$ for $0.5\le t\le 1$; integrating gives $300(0.125) + 300(0.125) = 75$. $\checkmark$

(d) Every vehicle arriving in $[0,1]$ joins a queue, so the affected cohort is $1800(0.5) + 1200(0.5) = 900 + 600 = 1500$ vehicles. The average delay is
$$\frac{75}{1500} = 0.05\ \text{h} = 3\ \text{min}.$$

(e) The longest wait is not the queue-clearance time. A vehicle arriving at $t = 0.5$ finds $150$ vehicles ahead of it; service at $1500$ veh/h clears that backlog in
$$W_{\max} = \frac{150}{1500} = 0.1\ \text{h} = 6\ \text{min}.$$
The queue survives until $t = 1$ only because new arrivals keep replacing the vehicles served, not because any one vehicle waits that long.

*Remark on (b) versus (e).* The distinction is a standard source of error in traffic reporting: "the queue took 30 minutes to clear" and "the worst delay was 6 minutes" are both true and describe different quantities. A model report that gives only one of them invites the reader to infer the other.

**36.** *Strategy: one column per quantity, then read off the rank.*

(a) With rows $(M,L,T)$ and columns $(F, v, L, \rho, \mu, c_s)$:
$$A = \begin{pmatrix}1&0&0&1&1&0\\ 1&1&1&-3&-1&1\\ -2&-1&0&0&-1&-1\end{pmatrix}.$$
The $3\times3$ block of the columns $F, v, \rho$ has determinant
$$1\cdot\bigl(1\cdot0 - (-3)(-1)\bigr) - 0 + 1\cdot\bigl(1\cdot(-1) - 1\cdot(-3)\bigr) = -3 + 2 = -1 \ne 0,$$
so the rank is $3$. With $n = 6$, $m = 6-3 = 3$.

(b) Three independent groups are
$$\pi_1 = \frac{F}{\rho v^2L^2}, \qquad \pi_2 = \frac{\rho vL}{\mu}, \qquad \pi_3 = \frac{v}{c_s},$$
with exponent vectors $(-1,2,2,1,0,0)$, $(-1,1,1,1,-1,0)$ and $(0,1,0,0,0,-1)$. *Check each:* the first was verified in Example 9.4; the second has $[\rho vL/\mu] = 1$ (Example 9.4 again); the third is a ratio of two speeds. Independence: the exponent of $F$ is nonzero only in the first, the exponent of $\mu$ is nonzero only in the second, and the exponent of $c_s$ is nonzero only in the third, so no nontrivial combination vanishes.

(c) $\pi_1$ is $1/C_D$ up to a factor: the drag coefficient. $\pi_2$ is the Reynolds number: inertia over viscosity. $\pi_3$ is the Mach number: flow speed over sound speed.

(d) The theorem yields only
$$\frac{F}{\rho v^2L^2} = \Phi\left(\mathrm{Re},\ \mathrm{Ma}\right),$$
i.e. a drag coefficient that depends on two dimensionless arguments. The function $\Phi$ — the entire content of compressible aerodynamics — must be measured in a wind tunnel or computed by solving the flow equations. What the theorem contributes is the knowledge that only two arguments can matter, which is what makes a wind-tunnel campaign finite: for each $(\mathrm{Re},\mathrm{Ma})$ pair one number is needed, and no other combination of the six variables can enter.

