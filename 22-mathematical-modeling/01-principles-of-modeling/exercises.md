# Principles of Modeling — Exercises

> [Principles of Modeling](README.md) · 36 problems · Beginner → Challenge · Solutions: [solutions.md](solutions.md)

Attempt every problem in writing before consulting [solutions.md](solutions.md). Each problem names the section of the tutorial that supplies the technique. Problems marked *(open)* have a defensible answer rather than a unique one; the solution gives a model answer and the criteria for judging one.

**Notation.** $[q]$ is the dimension of $q$; the fundamental dimensions are $M$ (mass), $L$ (length), $T$ (time) and $\Theta$ (temperature). $A$ is the dimension matrix, $k = \operatorname{rank} A$, $n$ the number of quantities and $m = n-k$ the number of dimensionless groups. $S_p(y) = \partial \ln y/\partial \ln p$ is the normalised sensitivity. $\Phi$ denotes a function that dimensional analysis leaves undetermined, and $C$ an undetermined constant.

## Beginner

**1.** *(§7.4)* Find the dimension of (a) linear momentum $p = mv$; (b) torque $\tau = Fr$; (c) angular momentum $L = mvr$; (d) the gravitational constant $G$ in $F = GmM/r^2$; (e) the Stefan–Boltzmann constant $\sigma$ in $E = \sigma T^4$, where $E$ is power per unit area and $T$ is a thermodynamic temperature.

**2.** *(§7.4)* Decide which of the following are dimensionally homogeneous. For each that is not, say which side has the wrong dimension. (a) $v^2 = 2as$; (b) $s = \tfrac12 at^3$; (c) $P = \rho g h Q$ with $Q$ a volume flow rate; (d) $F = \mu A v/L$ for a viscous shear force; (e) $T = 2\pi\sqrt{L/g}$; (f) $E = \tfrac12 m v^2 + m g h$.

**3.** *(§7.4)* Convert (a) $100$ km/h to m/s; (b) $1$ g/cm³ to kg/m³; (c) $1$ kWh to joules; (d) $1$ bar to pascals; (e) a fuel economy of $30$ miles per US gallon to litres per $100$ km. State which of these are dimensionless ratios and which are unit conversions.

**4.** *(§7.3)* An account holds balance $B(t)$, earns interest at continuous rate $r$, and is drawn down at constant rate $w$. (a) Identify the state variable and the rate terms, and write the balance law. (b) Solve it with $B(0) = B_0$. (c) Find the equilibrium and decide whether it is stable. (d) Compute $B(10)$ for $B_0 = 1000$, $r = 0.05$ yr⁻¹, $w = 100$ per year.

**5.** *(§7.5)* For each variable list, state $n$, $k = \operatorname{rank} A$ and $m = n-k$, and say what the theorem concludes. (a) $(F, m, a)$; (b) $(T, L, g)$; (c) $(T, L, g, m)$; (d) $(v, g, h)$; (e) $(p, \rho, v)$ with $p$ a pressure.

**6.** *(§7.5)* (a) Use the π theorem to show that the period of a mass–spring oscillator obeys $T = C\sqrt{m/k}$. (b) Given that the exact answer is $T = 2\pi\sqrt{m/k}$, compute $T$ for $m = 0.5$ kg and $k = 200$ N/m. (c) Explain why the mass does *not* cancel here, although it does for a pendulum.

**7.** *(§7.5)* The period of a pendulum is $T = 2\pi\sqrt{L/g}$. A pendulum of fixed length is taken from Earth ($g = 9.81$ m/s²) to the Moon ($g = 1.62$ m/s²). By what factor does its period change, and does the period increase or decrease?

**8.** *(§7.6)* A 2 m tall statue is reproduced at four times the scale, in the same material. Compute the ratios (new : old) of (a) surface area, (b) volume, (c) mass, (d) the compressive stress in a geometrically similar leg.

**9.** *(§7.6)* For a geometrically similar family with $M \propto L^3$ at constant density, find the exponent $b$ in $y \propto M^b$ for (a) skin area; (b) density; (c) buoyancy force; (d) the terminal speed of a body falling with quadratic drag, $v = \sqrt{2mg/(\rho C_D A)}$, where $A$ is the frontal area.

**10.** *(§7.8)* (a) For the model $y = abx$, explain why no data can determine $a$ and $b$ separately. (b) Given the data $(1,3)$, $(2,6)$, $(3,9)$, find the identifiable combination. (c) Repeat for the model $y = a + b$, using the same data.

**11.** *(§7.9)* For $y = a^2 b^{-1/2} c$, compute $S_a$, $S_b$ and $S_c$. If each of $a$, $b$, $c$ is uncertain by $\pm 3\%$, estimate the relative uncertainty of $y$ (i) in the worst case and (ii) assuming independent, equally likely errors.

**12.** *(§7.14, open)* A clinic wants to know how long patients wait before seeing a triage nurse. Write a model specification using the checklist of §7.14: the question and tolerance, the boundary, the state variables, the rate laws, at least four assumptions with their kind, the outputs, and one validation test that would actually be feasible.

## Intermediate

**13.** *(§7.5)* A projectile is launched at speed $v$ and elevation $\theta$; the range is $R$, and gravity $g$ acts. (a) Show that the only dimensionless group containing $R$ is $Rg/v^2$, so $R = (v^2/g)\Phi(\theta)$. (b) Given the exact result $R = (v^2/g)\sin 2\theta$, evaluate the range at $15°$, $45°$ and $75°$ for $v = 20$ m/s, and verify the symmetry $\Phi(15°) = \Phi(75°)$. (c) State precisely what dimensional analysis contributed and what it did not.

**14.** *(§7.5)* A solute diffuses with coefficient $D = 10^{-9}$ m²/s. (a) Derive the estimate $\tau \sim L^2/D$ for the time to diffuse a distance $L$. (b) Compute $\tau$ for $L = 1$ mm, $1$ cm and $1$ m. (c) Compute the distance diffused in one hour. (d) Explain why a cell can rely on diffusion but a large animal cannot.

**15.** *(§7.6)* A harbour is modelled at $1{:}25$ scale. (a) If the prototype has a wave period of $8$ s, what period must the model reproduce under Froude scaling? (b) If a prototype current is $2$ m/s, what model speed corresponds? (c) Explain why the same model cannot simultaneously match the Reynolds number if the same fluid is used, and quantify the discrepancy.

**16.** *(§7.6)* Kleiber's law is $B = B_0 M^{3/4}$ for basal metabolic rate. (a) Show that the specific metabolic rate $B/M$ scales as $M^{-1/4}$. (b) Compute the ratio of specific metabolic rates of a $30$ g mouse and a $5000$ kg elephant. (c) If heart rate scales as $M^{-1/4}$, predict the ratio of heart rates for the same two animals and comment on the product (heart rate) × (lifespan) if lifespan scales as $M^{1/4}$.

**17.** *(§7.9)* For $y = a/(b-c)$ with $a = 10$, $b = 5$: (a) compute $S_c$ as a function of $c$; (b) evaluate it at $c = 4$ and $c = 4.9$; (c) compute $y$ at both points and reconcile the change in $y$ with the product of sensitivity and relative change in $c$. (d) Explain what a model with such a structure would be useless for.

**18.** *(§7.5)* For a pendulum released from rest at amplitude $\theta_0$, dimensional analysis gives $T\sqrt{g/L} = \Phi(\theta_0)$ with $\Phi(0) = 2\pi$ and $\Phi(\pi/2) \approx 7.416$. (a) Explain why $\theta_0$ does not appear as a group. (b) Compute the period of a $1$ m pendulum released from the horizontal, and compare with the small-angle period. (c) State the general lesson about dimensionless inputs.

**19.** *(§7.9)* A population with proportional harvesting obeys $\dot N = rN(1 - N/K) - hN$, so the stable equilibrium is $N^* = K(1 - h/r)$ for $h < r$. (a) Show that $S_h(N^*) = -h/(r-h)$. (b) Evaluate at $h = 0.5r$ and $h = 0.9r$. (c) Interpret the divergence as $h \to r$.

**20.** *(§7.11)* For the Lotka–Volterra model of §7.11 with $a, b, \delta, c > 0$: (a) verify that $H = \delta x - c\ln x + by - a\ln y$ satisfies $\dot H = 0$ along solutions; (b) state two predictions of the model that are genuine and two that are artefacts; (c) design an observation or experiment that would distinguish the model's claim about amplitudes from an alternative in which the cycles are damped.

**21.** *(§7.3)* A lake of volume $V = 10^7$ m³ receives a pollutant at inflow $q = 5$ m³/s. The pollutant decays in the lake at rate constant $k = 2\times10^{-7}$ s⁻¹, and the inflow is clean. (a) Write the balance law and identify state and rates. (b) Solve with $C(0) = C_0$. (c) Compute the time for the concentration to fall to $10\%$ of $C_0$. (d) Give the residence time and explain the difference from the hydraulic residence time $V/q$.

**22.** *(§7.12)* A road obeys $v(\rho) = v_{\max}(1 - \rho/\rho_{\max})$ with $v_{\max} = 100$ km/h and $\rho_{\max} = 140$ veh/km. (a) Compute the capacity and the density at which it occurs. (b) Compute the kinematic wave speed at $0.3\rho_{\max}$, $0.5\rho_{\max}$ and $0.8\rho_{\max}$. (c) Compute the shock speed for a jump from $50$ to $90$ veh/km and interpret. (d) Why does the linear fundamental diagram overestimate capacity?

## Advanced

**23.** *(§7.5)* Prove Theorem 7.5.1: if $f$ is invariant under every rescaling of units in the sense of the theorem, then $f(q) = F(\pi_1,\dots,\pi_{n-k})$. Your proof must state where the hypothesis $\operatorname{rank} A = k$ is used.

**24.** *(§7.5)* (a) Show that if $\mathbf e^{(1)},\dots,\mathbf e^{(m)}$ and $\mathbf f^{(1)},\dots,\mathbf f^{(m)}$ are two bases of $\ker A$, then $\mathbf f^{(i)} = \sum_j M_{ji}\mathbf e^{(j)}$ for an invertible $m \times m$ matrix $M$. (b) Deduce that the two corresponding sets of groups satisfy $\pi'_i = \prod_j \pi_j^{M_{ij}}$ and that either set determines the other. (c) Illustrate with the drag problem of Example 9.4, where the basis $\{(-1,2,2,1,0),(-1,1,1,0,1)\}$ and the basis $\{(-1,2,2,1,0),(-2,3,3,1,1)\}$ give different but equivalent pairs.

**25.** *(§7.9)* Prove, for differentiable positive functions and a positive parameter $p$, that (a) $S_p(fg) = S_p(f) + S_p(g)$; (b) $S_p(f/g) = S_p(f) - S_p(g)$; (c) $S_p(f^{\alpha}) = \alpha S_p(f)$ for constant $\alpha$; and (d) $S_p(f\circ g) = S_p(g)\cdot S_g(f)$ when $g$ depends on $p$. Then prove the first-order error bound $\lvert\delta y/y\rvert \le \sum_i \lvert S_i\rvert\lvert\delta p_i/p_i\rvert$.

**26.** *(§7.6)* (a) Show that under geometric similarity at constant density the compressive stress in a supporting member is proportional to body length. (b) Suppose instead that the *fraction of body mass devoted to bone* is allowed to vary, and that it is chosen so as to keep the stress constant. Show that this fraction must grow in proportion to body length. (c) Compute the factor by which a $10$ m animal's bone fraction must exceed a $1$ m animal's, and comment on the biological implication.

**27.** *(§7.8)* (a) Prove that for $N$ distinct points $(x_1,y_1),\dots,(x_N,y_N)$ there is exactly one polynomial of degree at most $N-1$ passing through all of them. (b) Deduce that the calibration error of a model in this class can always be made exactly zero. (c) Using three points, exhibit a one-parameter family of models with zero error on the data and arbitrary predictions at a fourth point. (d) State the moral for model selection.

**28.** *(§7.12)* (a) Derive the shock (Rankine–Hugoniot) speed $s = (q(\rho_2) - q(\rho_1))/(\rho_2 - \rho_1)$ by applying conservation of cars to a window containing the discontinuity. (b) Show that for $q = v_{\max}\rho(1 - \rho/\rho_{\max})$ this becomes $s = v_{\max}(1 - (\rho_1+\rho_2)/\rho_{\max})$. (c) Determine when the shock is stationary and when it propagates upstream.

**29.** *(§7.13)* (a) Prove by an interchange argument that shortest-processing-time first minimises $\sum C_j$ on one machine with all jobs available at time $0$. (b) For $p = (7,2,5,1)$ compute the objective for the SPT order, for the given order, and for the order of decreasing processing time. (c) Explain in one sentence why the result does not survive adding release dates.

**30.** *(§7.5)* Non-dimensionalise the logistic equation $\dot N = rN(1 - N/K)$. (a) Show that with $x = N/K$ and $\tau = rt$ it becomes $x' = x(1-x)$, independent of both parameters. (b) Deduce that all logistic populations follow the *same* trajectory in scaled variables. (c) Compute the time for a population with $r = 0.05$ yr⁻¹ to grow from $5\%$ to $95\%$ of its carrying capacity, and explain why the answer depends only on $r$.

## Challenge

**31.** *(§7.5)* (a) Prove that if every quantity in the list is already dimensionless, then $k = 0$, the theorem yields $m = n$ groups, and it imposes no constraint on $f$. (b) Prove that if $k = n$ the theorem forces $f$ to be constant on each orbit, so that the law reduces to a single dimensionless constant. (c) Apply (a) to the pendulum with amplitude and explain why no dimensional argument can produce $\Phi(\pi/2) \approx 7.416$.

**32.** *(§7.9)* Let $y = \max(p - p_0, 0)$ with $p_0 = 10$. (a) Compute $S_p$ for $p < 10$ and for $p > 10$. (b) Show that $S_p \to +\infty$ as $p \downarrow 10$ and explain why a local analysis at $p = 10$ is meaningless. (c) Compute the exact range of $y$ for $p \in [5,15]$ and compare it with the range predicted by linearising each side separately. (d) State the general lesson for sensitivity analysis of models with thresholds.

**33.** *(§7.8)* The logistic solution can be written
$$N(t) = \frac{N_0 e^{rt}}{1 + \frac{N_0}{K}\left(e^{rt} - 1\right)} .$$
(a) Verify this identity. (b) Put $\varepsilon = N_0/K$ and expand in $\varepsilon$ to show $N(t) = N_0e^{rt}\left[1 - \varepsilon(e^{rt}-1) + O(\varepsilon^2)\right]$. (c) Deduce that $\partial N/\partial K = O(K^{-2})$ and that $S_K(N) \approx \varepsilon(e^{rt}-1)$. (d) Explain what this implies for the practical problem of estimating $K$ from data on the early, exponential phase of a growth curve, and confirm your claim by computing $S_K$ at the time when $N = 10N_0$, given $N_0/K = 0.01$.

**34.** *(§7.10)* A score $s$ is used to select candidates when $s \ge \tau$. In group A, $s \sim \mathcal{N}(1,1)$; in group B, $s \sim \mathcal{N}(0,1)$; the threshold is $\tau = 1$. (a) Compute the selection rate in each group and their ratio, using $\Phi(1) = 0.8413$ and $\Phi(-1) = 0.1587$. (b) Show that removing the group label from the model does not remove the disparity, and explain the mechanism in one sentence. (c) Compute the threshold in group B that would equalise selection rates. (d) State two procedural responses that do not require the model to be discarded, and one that does.

**35.** *(§7.12)* A bottleneck has capacity $1500$ veh/h. Demand is $1800$ veh/h for $30$ minutes, then $1200$ veh/h until the queue clears. (a) Compute the queue at the end of the overload. (b) Compute the time to clear after the overload ends. (c) Compute the total delay in vehicle-hours. (d) Compute the average delay per affected vehicle. (e) Compute the maximum delay experienced by any one vehicle.

**36.** *(§7.5)* A force $F$ acts on a body of size $L$ moving at speed $v$ in a compressible fluid of density $\rho$, viscosity $\mu$ and sound speed $c_s$. (a) Show that $k = 3$ and $m = 3$. (b) Find three dimensionless groups. (c) Identify them physically. (d) Explain what extra information is needed before the theorem says anything numerical.
