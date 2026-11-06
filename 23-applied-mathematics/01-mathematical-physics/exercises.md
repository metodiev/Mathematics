# Mathematical Physics — Exercises

> [Mathematical Physics](README.md) · 36 problems · Beginner → Challenge · Solutions: [solutions.md](solutions.md)

Work through the problems in order. Each problem names the section of the tutorial where the necessary
material is developed. Attempt every problem in writing before opening [solutions.md](solutions.md);
the solutions contain full derivations, not only answers.

**Conventions.** SI units throughout unless stated. $g = 9.81\ \mathrm{m/s^2}$ except where a problem
specifies $9.8$. "Small oscillations" means the linear approximation about a stable equilibrium. In
orbital problems, $1\ \mathrm{AU} = 1.496\times10^{11}\ \mathrm{m}$ and
$GM_\oplus = 3.986\times10^{14}\ \mathrm{m^3/s^2}$. Angles are in degrees when marked with $^\circ$ and in
radians otherwise.

## Beginner

**1.** *(§7.2)* A stone is thrown from ground level at $25\ \mathrm{m/s}$ at $30^\circ$ above the
horizontal. Use $g = 9.8\ \mathrm{m/s^2}$ and ignore air resistance.

(a) Compute the time of flight.
(b) Compute the horizontal range.
(c) Compute the maximum height.
(d) Compute the speed of the stone at the highest point.

**2.** *(§7.3)* A mass of $0.5\ \mathrm{kg}$ is attached to a spring of stiffness $8\ \mathrm{N/m}$ on a
frictionless horizontal table.

(a) Compute the angular frequency $\omega_0$ and the period.
(b) If the amplitude is $0.05\ \mathrm{m}$, compute the maximum speed and the maximum acceleration.
(c) Compute the total mechanical energy.

**3.** *(§7.3)* A harmonic oscillator has displacement $x(t) = 0.1\cos(6t)\ \mathrm{m}$.

(a) State the amplitude, angular frequency, frequency and period.
(b) Find the first time $t>0$ at which $x = 0$.
(c) Find the maximum speed and the maximum acceleration.

**4.** *(§7.3)* A damped oscillator has $m = 2\ \mathrm{kg}$, $c = 8\ \mathrm{N\,s/m}$ and
$k = 32\ \mathrm{N/m}$.

(a) Compute $\omega_0$, $\zeta$ and $\omega_d$, and classify the damping.
(b) If $x(0) = 0.02\ \mathrm{m}$ and $\dot x(0) = 0$, write $x(t)$ explicitly.
(c) How long does it take for the amplitude envelope to fall to half its initial value?

**5.** *(§7.4, §7.5)* A force field on the line is $F(x) = 3x^2\ \mathrm{N}$, directed along $+x$.

(a) Is the force conservative? Justify.
(b) Find a potential $V(x)$ with $V(0)=0$.
(c) Compute the work done from $x=0$ to $x=2\ \mathrm{m}$ by two methods and check they agree.

**6.** *(§7.4, §7.5)* A particle of mass $2\ \mathrm{kg}$ has position
$\mathbf{r}(t) = (3t,\,4t^2)\ \mathrm{m}$.

(a) Compute the velocity and acceleration at $t=1\ \mathrm{s}$.
(b) Compute the kinetic energy and the momentum at $t=1\ \mathrm{s}$.
(c) Compute the angular momentum about the origin at $t=1\ \mathrm{s}$.

**7.** *(§7.2)* A ball is launched horizontally at $15\ \mathrm{m/s}$ from a cliff of height
$45\ \mathrm{m}$.

(a) Compute the time until it reaches the ground.
(b) Compute the horizontal distance travelled.
(c) Compute the speed on impact.

**8.** *(§7.9)* A simple pendulum has length $0.5\ \mathrm{m}$.

(a) Compute the period of small oscillations.
(b) Find the length that gives a period of exactly $2\ \mathrm{s}$.

**9.** *(§7.11)* A transverse wave on a string is $y(x,t) = 0.02\sin(4\pi x - 80\pi t)\ \mathrm{m}$.

(a) State the amplitude, wavelength, frequency and speed.
(b) State the direction of propagation.
(c) Compute the maximum transverse speed of a point on the string.

**10.** *(§7.12)* A rod of length $1\ \mathrm{m}$ has thermal diffusivity
$\alpha = 1.1\times10^{-4}\ \mathrm{m^2/s}$.

(a) Compute the decay time of the first normal mode.
(b) Compute the time for the first-mode amplitude to fall to $1\%$ of its initial value.

**11.** *(§7.14)* Show that each of the following has dimensions of energy: (a) $\tfrac12mv^2$,
(b) $mgh$, (c) $GMm/r$. Show that $\tfrac12\rho v^2$ has dimensions of pressure.

**12.** *(§7.7)* A satellite is in a circular orbit of radius $r = 7000\ \mathrm{km}$ about the Earth.

(a) Compute its speed and period.
(b) Repeat for a geostationary orbit, $r = 42\,164\ \mathrm{km}$, and explain why your period is
approximately one sidereal day.

**13.** *(§7.4, §7.8)* Write the Lagrangian of a free particle in polar coordinates and derive both
Euler–Lagrange equations. Identify the conserved quantity and explain geometrically why it is conserved.

## Intermediate

**14.** *(§7.2)* A projectile is fired at $30\ \mathrm{m/s}$ and must hit a target on level ground
$80\ \mathrm{m}$ away.

(a) Find the two possible launch angles.
(b) Compute the time of flight for each.
(c) The two angles are symmetric about $45^\circ$; explain why the times of flight nevertheless differ.

**15.** *(§7.3)* A damped oscillator has $m=1\ \mathrm{kg}$ and $k=25\ \mathrm{N/m}$. You want a damping
ratio of exactly $\zeta = 0.1$.

(a) Compute the required $c$.
(b) Compute $\omega_d$ and the period.
(c) Compute the quality factor $Q$.
(d) Compute the fraction of the initial amplitude remaining after three periods.

**16.** *(§7.3)* A driven oscillator has $m=1\ \mathrm{kg}$, $k=4\ \mathrm{N/m}$, $c=0.4\ \mathrm{N\,s/m}$
and a driving force $F_0\cos\omega t$ with $F_0 = 1\ \mathrm{N}$.

(a) Compute $\zeta$.
(b) Compute the resonant frequency $\omega_r = \omega_0\sqrt{1-2\zeta^2}$.
(c) Compute the steady-state amplitude at $\omega = \omega_r$.
(d) Compute the steady-state amplitudes at $\omega = 1$ and $\omega = 3\ \mathrm{rad/s}$, and comment on
the ratio.

**17.** *(§7.4)* For the potential energy per unit mass $U(r) = -k/r$ with $k>0$ and a given specific
angular momentum $h$:

(a) Find the radius $r_0$ of the circular orbit.
(b) Show that $U_{\text{eff}}''(r_0) > 0$.
(c) Show that the frequency of small radial oscillations equals the orbital angular frequency.

**18.** *(§7.6)* The Earth has $m_E = 5.972\times10^{24}\ \mathrm{kg}$ and the Moon
$m_M = 7.348\times10^{22}\ \mathrm{kg}$, separated by $r = 3.844\times10^8\ \mathrm{m}$.

(a) Compute the reduced mass $\mu$ and the ratio $\mu/m_M$.
(b) Compute the gravitational acceleration of the relative coordinate.
(c) Compute the orbital period and compare it with the observed $27.3$ days.

**19.** *(§7.7)* A comet has perihelion $0.5\ \mathrm{AU}$ and aphelion $30\ \mathrm{AU}$.

(a) Compute $a$ and $e$.
(b) Compute the period in years using $T^2 = a^3$ in solar units.
(c) Compute the speeds at perihelion and aphelion.
(d) Verify that the product $r_pv_p$ equals $r_av_a$.

**20.** *(§7.9)* A bead slides on a frictionless horizontal straight wire that rotates with constant
angular velocity $\Omega = 3\ \mathrm{rad/s}$ about a vertical axis through one end. The bead starts at
$r_0 = 0.1\ \mathrm{m}$ with zero radial velocity.

(a) Write $r(t)$.
(b) Compute the time at which the bead is $1\ \mathrm{m}$ from the axis.
(c) Explain why the origin is an unstable equilibrium.

**21.** *(§7.10)* For $H = \dfrac{p^2}{2m} + \dfrac12kx^2$ with $m=1$, $k=4$:

(a) Write Hamilton's equations.
(b) Solve them with $q(0)=1$, $p(0)=0$.
(c) Show that the phase-space orbit is an ellipse and identify its semi-axes.
(d) Verify that $H$ is constant along the solution.

**22.** *(§7.11)* A string of length $L = 0.8\ \mathrm{m}$ has tension $\tau = 120\ \mathrm{N}$ and linear
density $\rho = 0.02\ \mathrm{kg/m}$.

(a) Compute the wave speed.
(b) Compute the fundamental frequency.
(c) Compute the frequency of the third harmonic and its wavelength.

**23.** *(§7.12)* A rod occupies $0<x<1\ \mathrm{m}$ and has reached a steady temperature distribution. The
ends are held at $u(0)=0$ and $u(1)=100\ ^\circ\mathrm{C}$, and the conductivity is
$k = 400\ \mathrm{W/(m\,K)}$.

(a) Solve the steady-state equation and give $u(x)$.
(b) Compute the heat flux and state its direction.
(c) Explain why the flux is independent of $x$.

**24.** *(§7.13)* (a) Show that $L = \tfrac12m\dot q^2$ is invariant under $q\mapsto q+\varepsilon$ and find
the conserved quantity $J$. (b) Show that $L = \tfrac12m\dot q^2 - mgq$ has no explicit time dependence,
find the conserved quantity predicted by Noether's theorem, and identify it.

## Advanced

**25.** *(§7.8)* Starting from $S[q] = \int_{t_0}^{t_1}L(q,\dot q,t)\,dt$ and a variation with fixed
endpoints, derive the Euler–Lagrange equations in full, explaining (a) why the integration by parts is
valid, (b) why the boundary term vanishes, and (c) why the bracket must vanish pointwise. Then show that
$L' = L + \dfrac{dF(q,t)}{dt}$ produces the same equations.

**26.** *(§7.7)* Derive Kepler's third law completely: begin with the area law, express the area of the
ellipse in terms of $a$ and $e$, use $p = h^2/(GM)$ and $p = a(1-e^2)$, and obtain
$T^2 = 4\pi^2a^3/[G(m_1+m_2)]$.

**27.** *(§7.5)* Consider $N$ particles with pairwise central forces and no external forces. Prove that
the total energy
$$E = \sum_i\tfrac12m_i\lVert\dot{\mathbf{r}}_i\rVert^2 + \sum_{i<j}V_{ij}(\lVert\mathbf{r}_i-\mathbf{r}_j\rVert)$$
is conserved. State precisely which properties of the forces you use.

**28.** *(§7.4)* For a central force $f(r)\hat{\mathbf{r}}$:

(a) Prove that $\mathbf{L} = \mathbf{r}\times\mathbf{p}$ is conserved and that the motion lies in a plane.
(b) Prove that the areal velocity is constant.
(c) Prove that a circular orbit at $r_0$ is stable if and only if $U_{\text{eff}}''(r_0) > 0$.

**29.** *(§7.11)* (a) Factor the wave operator and derive d'Alembert's general solution. (b) Verify by
direct differentiation that the initial-value formula satisfies both the PDE and the initial conditions.
(c) Explain, using the formula, why a string of length $L$ with fixed ends needs the method of images
rather than the whole-line formula.

**30.** *(§7.12)* Seek a similarity solution $u(x,t) = t^{-1/2}f(\eta)$ with $\eta = x/\sqrt{\alpha t}$ of
the heat equation $u_t = \alpha u_{xx}$.

(a) Derive the ordinary differential equation for $f$.
(b) Solve it and show that the result is the Gaussian fundamental solution.
(c) Interpret the scaling of the width and the height.

**31.** *(§7.14)* (a) Use the Buckingham Pi theorem to show that the period of a pendulum is
$T = C\sqrt{l/g}$ and explain why the mass does not appear. (b) For large amplitudes, what additional
dimensionless group appears, and how does the period depend on it at small but nonzero amplitude?

**32.** *(§7.10)* Derive Hamilton's equations from $H = \sum_ip_i\dot q_i - L$ by comparing two
expressions for $dH$. Show that $\dfrac{dH}{dt} = \dfrac{\partial H}{\partial t}$, and interpret the result
in terms of energy conservation.

## Challenge

**33.** *(§7.9)* A bead slides on a hoop of radius $a = 0.15\ \mathrm{m}$ rotating about its vertical
diameter at $\Omega = 9\ \mathrm{rad/s}$.

(a) Find all equilibria.
(b) Determine the stability of each.
(c) Compute the frequency and period of small oscillations about the stable tilted equilibrium.
(d) Describe what happens as $\Omega$ is lowered through $\Omega_c$.

**34.** *(§7.6, §7.7)* Two equal stars of mass $m = 1.989\times10^{30}\ \mathrm{kg}$ orbit their common
centre of mass in a circular orbit with separation $d = 1\ \mathrm{AU}$.

(a) Compute the period.
(b) Compute the speed of each star.
(c) Compute the total energy and verify it equals minus the total kinetic energy.
(d) Show that the relative coordinate obeys Kepler's third law with total mass $2m$.

**35.** *(§7.14)* For a strong spherical blast wave, $R = C(Et^2/\rho)^{1/5}$.

(a) Derive the exponent $1/5$ from the Buckingham Pi theorem.
(b) Compute $R$ at $t = 1\ \mathrm{ms}$, $10\ \mathrm{ms}$, $0.1\ \mathrm{s}$ and $1\ \mathrm{s}$ for
$E = 4.184\times10^{13}\ \mathrm{J}$ and $\rho = 1.225\ \mathrm{kg/m^3}$ with $C=1$.
(c) Verify that the ratio $R(1\ \mathrm{s})/R(10\ \mathrm{ms})$ equals $100^{2/5}$.
(d) Explain two physical effects that make the formula fail at very early and very late times.

**36.** *(§7.13)* State and prove Noether's theorem for a one-parameter symmetry. Apply it to
(a) translations, (b) rotations, (c) time translations, and identify the conserved quantity in each case.
Finally, explain why a Lagrangian that does not depend on $x$ implies conservation of $p_x$.
