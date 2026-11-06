# Mathematical Physics — Solutions

> [Mathematical Physics](README.md) · Solutions to the 36 problems in [exercises.md](exercises.md)

Each solution states the strategy, carries out every significant step, and ends with a check. Numerical
answers are given to four significant figures unless the data justify fewer. Throughout, a dot is a time
derivative and $g=9.81\ \mathrm{m/s^2}$ unless the problem states otherwise.

## Beginner

**1.** *(Strategy: integrate the two decoupled equations of projectile motion.)*

Take the launch point as the origin, $z$ upward, and write $v_0 = 25\ \mathrm{m/s}$,
$\theta = 30^\circ$. Then $v_{0x} = 25\cos30^\circ = 21.65\ \mathrm{m/s}$ and
$v_{0z} = 25\sin30^\circ = 12.50\ \mathrm{m/s}$.

(a) The vertical motion is $z = v_{0z}t - \tfrac12gt^2$. Setting $z=0$ gives
$t_f = 2v_{0z}/g = 2(12.50)/9.8 = 2.551\ \mathrm{s}$.

(b) $R = v_{0x}t_f = (21.65)(2.551) = 55.23\ \mathrm{m}$. The formula
$R = v_0^2\sin2\theta/g = 625\sin60^\circ/9.8 = 55.23\ \mathrm{m}$ agrees.

(c) At the top $v_z=0$, so $H = v_{0z}^2/(2g) = (12.50)^2/19.6 = 7.972\ \mathrm{m}$.

(d) The horizontal component is constant, so the speed at the top is
$v_{0x} = 21.65\ \mathrm{m/s}$.

*Check.* The energy per unit mass is $\tfrac12(25)^2 = 312.5\ \mathrm{J/kg}$ initially. At the top,
$\tfrac12(21.65)^2 + 9.8(7.972) = 234.4 + 78.1 = 312.5\ \mathrm{J/kg}$. ✓

**2.** *(Strategy: read $\omega_0$ off the standard form and use energy for (c).)*

(a) $\omega_0 = \sqrt{k/m} = \sqrt{8/0.5} = 4\ \mathrm{rad/s}$; $T = 2\pi/\omega_0 = 1.571\ \mathrm{s}$.

(b) For $x = A\cos(\omega_0t)$ with $A=0.05\ \mathrm{m}$: $v_{\max} = A\omega_0 = 0.05(4) = 0.20\ \mathrm{m/s}$ and
$a_{\max} = A\omega_0^2 = 0.05(16) = 0.80\ \mathrm{m/s^2}$.

(c) $E = \tfrac12kA^2 = \tfrac12(8)(0.05)^2 = 0.0100\ \mathrm{J}$. Equivalently
$E = \tfrac12mv_{\max}^2 = \tfrac12(0.5)(0.2)^2 = 0.0100\ \mathrm{J}$. ✓

*Check.* $k/m = 16 = \omega_0^2$; the period is independent of amplitude, which is the defining property
of a linear oscillator.

**3.** *(Strategy: match $x = A\cos\omega t$ and differentiate.)*

(a) $A = 0.1\ \mathrm{m}$, $\omega = 6\ \mathrm{rad/s}$, $f = \omega/(2\pi) = 0.9549\ \mathrm{Hz}$,
$T = 1/f = 1.047\ \mathrm{s}$.

(b) $x=0$ when $\cos6t=0$, that is $6t = \pi/2$ for the first positive time:
$t = \pi/12 = 0.2618\ \mathrm{s}$.

(c) $\dot x = -0.6\sin6t$, so $v_{\max} = 0.6\ \mathrm{m/s}$; $\ddot x = -3.6\cos6t$, so
$a_{\max} = 3.6\ \mathrm{m/s^2}$.

*Check.* $a_{\max} = \omega^2A = 36(0.1) = 3.6$ ✓ and $v_{\max} = \omega A = 0.6$ ✓.

**4.** *(Strategy: compute $\zeta$ first; it decides everything else.)*

(a) $\omega_0 = \sqrt{k/m} = \sqrt{32/2} = 4\ \mathrm{rad/s}$ and
$\zeta = \dfrac{c}{2\sqrt{km}} = \dfrac{8}{2\sqrt{64}} = 0.5$. Since $0<\zeta<1$ the system is
underdamped, and $\omega_d = \omega_0\sqrt{1-\zeta^2} = 4\sqrt{0.75} = 3.464\ \mathrm{rad/s}$.

(b) Write $x = e^{-\zeta\omega_0 t}(A\cos\omega_dt + B\sin\omega_dt)$ with $\zeta\omega_0 = 2$. The initial
conditions give $A = 0.02$ and $-\zeta\omega_0A + \omega_dB = 0$, so
$B = (2)(0.02)/3.464 = 0.01155\ \mathrm{m}$. Hence

$$x(t) = e^{-2t}\bigl(0.02\cos 3.464t + 0.01155\sin 3.464t\bigr)\ \mathrm{m}.$$

(c) The envelope is $\sqrt{A^2+B^2}\,e^{-2t} = 0.02310\,e^{-2t}$. Half of the initial envelope is reached
when $e^{-2t} = \tfrac12$, that is $t = \ln2/2 = 0.3466\ \mathrm{s}$.

*Check.* $\dot x(0) = -2(0.02) + 3.464(0.01155) = -0.04 + 0.04 = 0$ ✓. The oscillation period is
$2\pi/3.464 = 1.814\ \mathrm{s}$, longer than the undamped $1.571\ \mathrm{s}$, as it must be.

**5.** *(Strategy: a force depending only on $x$ is conservative; integrate to get $V$.)*

(a) Yes. For a one-dimensional force, $\nabla\times\mathbf{F} = 0$ automatically (the curl of a field with
only an $x$ component depending only on $x$ vanishes), and every such force has a potential. Concretely,
$F = -\dfrac{dV}{dx}$ is an ODE for $V$ that always has a solution.

(b) $-\dfrac{dV}{dx} = 3x^2$, so $V(x) = -x^3 + C$; with $V(0)=0$, $C=0$ and $V(x) = -x^3$.

(c) Directly, $W = \int_0^2 3x^2\,dx = \bigl[x^3\bigr]_0^2 = 8\ \mathrm{J}$. From the potential,
$W = -\Delta V = -(V(2)-V(0)) = -(-8) = 8\ \mathrm{J}$. ✓

*Pitfall.* The potential is $-x^3$, not $+x^3$. The sign comes from $F=-V'$, and it matters: this force
pushes toward larger $x$, so the potential must decrease as $x$ increases.

**6.** *(Strategy: differentiate componentwise; cross product in the plane.)*

(a) $\mathbf{v} = \dot{\mathbf{r}} = (3,\,8t)$, so $\mathbf{v}(1) = (3,8)\ \mathrm{m/s}$;
$\mathbf{a} = (0,8)\ \mathrm{m/s^2}$, constant.

(b) $v^2 = 9+64 = 73$, so $T = \tfrac12(2)(73) = 73\ \mathrm{J}$. Momentum
$\mathbf{p} = m\mathbf{v} = 2(3,8) = (6,16)\ \mathrm{kg\,m/s}$.

(c) $\mathbf{r}(1) = (3,4)$. In two dimensions, $\mathbf{L} = \mathbf{r}\times\mathbf{p} = (x p_y - y p_x)\,\hat{\mathbf{z}} = (3\cdot16 - 4\cdot6)\hat{\mathbf{z}} = 24\,\hat{\mathbf{z}}\ \mathrm{kg\,m^2/s}$.

*Check.* Alternatively $\mathbf{L} = m(x\dot y - y\dot x) = 2(3\cdot8 - 4\cdot3) = 2(12) = 24$ ✓.

**7.** *(Strategy: horizontal and vertical motions are independent; the initial vertical velocity is zero.)*

(a) $45 = \tfrac12(9.81)t^2$ gives $t = \sqrt{2(45)/9.81} = 3.029\ \mathrm{s}$.

(b) $x = 15t = 15(3.029) = 45.43\ \mathrm{m}$.

(c) $v_y = -gt = -29.71\ \mathrm{m/s}$, so the speed is
$\sqrt{15^2 + 29.71^2} = 33.29\ \mathrm{m/s}$.

*Check.* The impact angle below the horizontal is $\arctan(29.71/15) = 63.2^\circ$, steeper than the
launch, as expected when there is no drag but a large drop.

**8.** *(Strategy: $T = 2\pi\sqrt{l/g}$ and solve for $l$.)*

(a) $T = 2\pi\sqrt{0.5/9.81} = 2\pi(0.2258) = 1.4185\ \mathrm{s}$.

(b) Set $2 = 2\pi\sqrt{l/9.81}$. Then $\sqrt{l/9.81} = 1/\pi$, so
$l = 9.81/\pi^2 = 0.9939\ \mathrm{m}$.

*Check.* $2\pi\sqrt{0.9939/9.81} = 2\pi(0.3183) = 2.000\ \mathrm{s}$ ✓. A "seconds pendulum" is about
$0.994\ \mathrm{m}$ long, which is why grandfather clocks are about a metre tall.

**9.** *(Strategy: read off $k$ and $\omega$ from the argument and use $c=\omega/k$.)*

(a) The amplitude is $0.02\ \mathrm{m}$. The wavenumber is $k = 4\pi\ \mathrm{m^{-1}}$, so
$\lambda = 2\pi/k = 0.5\ \mathrm{m}$. The angular frequency is $\omega = 80\pi\ \mathrm{rad/s}$, so
$f = \omega/(2\pi) = 40\ \mathrm{Hz}$. The speed is $c = \omega/k = 80\pi/(4\pi) = 20\ \mathrm{m/s}$.

(b) The argument is $4\pi x - 80\pi t = k(x - ct)$, so the wave travels in the $+x$ direction.

(c) A point on the string moves transversally with $v_y = \partial y/\partial t = -0.02(80\pi)\cos(\cdot)$,
so $v_{\max} = 0.02(80\pi) = 5.027\ \mathrm{m/s}$.

*Check.* $c = \lambda f = 0.5(40) = 20$ ✓.

**10.** *(Strategy: the first mode decays like $e^{-\alpha\pi^2t/L^2}$.)*

(a) The decay rate of the first mode is $\alpha\pi^2/L^2 = (1.1\times10^{-4})(9.870)/1 = 1.0857\times10^{-3}\ \mathrm{s^{-1}}$,
so the decay time is $\tau = 1/(1.0857\times10^{-3}) = 921.1\ \mathrm{s}$, about $15.4$ minutes.

(b) The amplitude is $e^{-t/\tau}$, so $e^{-t/\tau} = 0.01$ gives
$t = \tau\ln100 = 921.1(4.605) = 4242\ \mathrm{s} = 70.7\ \mathrm{min}$.

*Check.* $e^{-4242/921.1} = e^{-4.605} = 0.0100$ ✓. The long time reflects how slowly heat diffuses: the
time scale grows with the *square* of the length, so a rod twice as long takes four times as long.

**11.** *(Strategy: write each quantity in base dimensions $M,L,T$.)*

(a) $[\tfrac12mv^2] = M(LT^{-1})^2 = ML^2T^{-2}$, the dimensions of energy.

(b) $[mgh] = M(LT^{-2})L = ML^2T^{-2}$.

(c) $[GMm/r] = (M^{-1}L^3T^{-2})(M)(M)/L = ML^2T^{-2}$. Here $[G] = M^{-1}L^3T^{-2}$ follows from
$F = GMm/r^2$: $G = Fr^2/(m_1m_2)$, so $[G] = (MLT^{-2})(L^2)/M^2 = M^{-1}L^3T^{-2}$.

(d) $[\tfrac12\rho v^2] = (ML^{-3})(L^2T^{-2}) = ML^{-1}T^{-2}$. Pressure is force per area,
$(MLT^{-2})/L^2 = ML^{-1}T^{-2}$. ✓

*Check.* All three energies agree and $\rho v^2$ is the dynamic pressure of a fluid, which is why it is
added to the static pressure in Bernoulli's equation.

**12.** *(Strategy: circular orbit means gravity supplies the centripetal acceleration.)*

(a) $\dfrac{v^2}{r} = \dfrac{GM_\oplus}{r^2}$ gives
$v = \sqrt{GM_\oplus/r} = \sqrt{3.986\times10^{14}/7.0\times10^6} = 7.546\times10^3\ \mathrm{m/s}$.
The period is $T = 2\pi r/v = 2\pi(7.0\times10^6)/(7.546\times10^3) = 5.829\times10^3\ \mathrm{s}$, that is
$97.14$ minutes.

(b) For $r = 4.2164\times10^7\ \mathrm{m}$,
$v = \sqrt{3.986\times10^{14}/4.2164\times10^7} = 3.075\times10^3\ \mathrm{m/s}$ and
$T = 2\pi r/v = 8.616\times10^4\ \mathrm{s} = 23.93\ \mathrm{h}$. A sidereal day is $86\,164\ \mathrm{s}$, which
agrees to the precision of $GM_\oplus$ and $r$ used here.

*Check.* Kepler's third law in the form $T^2 = 4\pi^2r^3/(GM)$ gives the same numbers. The geostationary
orbit must match the Earth's rotation period, which is why its radius is fixed at about $42\,164\ \mathrm{km}$.

**13.** *(Strategy: the polar basis is time-dependent, so differentiate it carefully.)*

With $\mathbf{r} = r\hat{\mathbf{r}}$ and $\dot{\mathbf{r}} = \dot r\hat{\mathbf{r}} + r\dot\theta\hat{\boldsymbol\theta}$,

$$T = \tfrac12m(\dot r^2 + r^2\dot\theta^2), \qquad L = \tfrac12m(\dot r^2 + r^2\dot\theta^2).$$

The $r$-equation: $\dfrac{\partial L}{\partial\dot r} = m\dot r$, so
$\dfrac{d}{dt}(m\dot r) = \dfrac{\partial L}{\partial r} = mr\dot\theta^2$, that is
$\ddot r = r\dot\theta^2$.

The $\theta$-equation: $\dfrac{\partial L}{\partial\dot\theta} = mr^2\dot\theta$ and
$\dfrac{\partial L}{\partial\theta} = 0$, so $\dfrac{d}{dt}(mr^2\dot\theta) = 0$.

The conserved quantity is $mr^2\dot\theta$, the angular momentum. Geometrically, in time $dt$ the radius
vector sweeps a triangle of area $\tfrac12r^2\,d\theta$; conservation of $mr^2\dot\theta$ says this area is
swept at a constant rate, which is Kepler's second law. Equivalently, the Lagrangian does not depend on
$\theta$, so $\theta$ is cyclic and its conjugate momentum is conserved (Noether).

*Check.* The $r$-equation is the radial component of Newton's law for zero force,
$\ddot r - r\dot\theta^2 = 0$, which is what a straight line looks like in polar coordinates.

## Intermediate

**14.** *(Strategy: use the range formula and solve for $\theta$.)*

(a) With $R = v_0^2\sin2\theta/g$,
$\sin2\theta = gR/v_0^2 = 9.81(80)/900 = 0.8720$. Thus $2\theta = 60.69^\circ$ or $119.31^\circ$, giving
$\theta_1 = 30.35^\circ$ and $\theta_2 = 59.65^\circ$.

(b) $t_f = 2v_0\sin\theta/g$. For $\theta_1$:
$t_1 = 2(30)(0.5052)/9.81 = 3.090\ \mathrm{s}$. For $\theta_2$:
$t_2 = 2(30)(0.8634)/9.81 = 5.278\ \mathrm{s}$.

(c) The two angles sum to $90^\circ$ and are symmetric about $45^\circ$, so they give the same range. But
the steeper shot stays in the air longer: its vertical velocity is larger, and the horizontal velocity is
correspondingly smaller, keeping the product $v_{0x}t_f$ the same. A goalkeeper and a defender care about
the difference; the range formula does not see it.

*Check.* $v_0^2\sin(2\cdot30.35^\circ)/9.81 = 900(0.8720)/9.81 = 80.0\ \mathrm{m}$ and similarly for the
other angle. ✓

**15.** *(Strategy: choose $c$ from the definition of $\zeta$, then read off the decay.)*

(a) $\zeta = c/(2\sqrt{km})$, so $c = 2\zeta\sqrt{km} = 2(0.1)\sqrt{25} = 1.0\ \mathrm{N\,s/m}$.

(b) $\omega_d = \omega_0\sqrt{1-\zeta^2} = 5\sqrt{0.99} = 4.9749\ \mathrm{rad/s}$; the period is
$T = 2\pi/\omega_d = 1.263\ \mathrm{s}$.

(c) $Q = 1/(2\zeta) = 5$.

(d) The amplitude decays by $e^{-\zeta\omega_0T}$ per period. Here
$\zeta\omega_0T = (0.1)(5)(1.263) = 0.6315$, so per period the factor is $e^{-0.6315} = 0.5318$; after three
periods the remaining fraction is $(0.5318)^3 = 0.1504$, that is about $15\%$.

*Check.* $Q=5$ means the energy should fall by roughly $e^{-2\pi/Q} = e^{-1.257} = 0.285$ per period; indeed
$(0.5318)^2 = 0.283$ ✓. The amplitude falls by the square root of the energy factor, as it must.

**16.** *(Strategy: put the equation in standard form, then use the amplitude formula.)*

Divide $\ddot x + \dfrac{c}{m}\dot x + \dfrac{k}{m}x = \dfrac{F_0}{m}\cos\omega t$ by $m$: $\omega_0 = 2$ and
$2\zeta\omega_0 = c/m = 0.4$, so $\zeta = 0.1$.

(a) $\zeta = 0.1$.

(b) $\omega_r = \omega_0\sqrt{1-2\zeta^2} = 2\sqrt{1-0.02} = 1.9799\ \mathrm{rad/s}$.

(c) $X_{\max} = \dfrac{F_0/m}{2\zeta\omega_0^2\sqrt{1-\zeta^2}} = \dfrac{1}{2(0.1)(4)(0.9950)} = 1.256\ \mathrm{m}$.

(d) At $\omega=1$: $(\omega_0^2-\omega^2)^2 = 9$ and $(2\zeta\omega_0\omega)^2 = 0.16$, so
$X = 1/\sqrt{9.16} = 0.3304\ \mathrm{m}$. At $\omega=3$: $(\omega_0^2-\omega^2)^2 = 25$ and
$(2\zeta\omega_0\omega)^2 = 1.44$, so $X = 1/\sqrt{26.44} = 0.1945\ \mathrm{m}$. The response is largest near
$\omega_0$, falls off on both sides, and at $\omega=3$ the phase is nearly $180^\circ$ (the oscillator moves
opposite to the force).

*Check.* The static deflection at $\omega=0$ would be $F_0/k = 0.25\ \mathrm{m}$; the resonant amplitude
$1.256\ \mathrm{m}$ is about $5$ times larger, consistent with $Q\approx5$.

**17.** *(Strategy: work with the effective potential per unit mass.)*

Interpret $U$ as potential energy per unit mass; then
$U_{\text{eff}}(r) = -k/r + h^2/(2r^2)$ and the radial equation is $\ddot r = -U_{\text{eff}}'(r)$.

(a) $U_{\text{eff}}'(r) = k/r^2 - h^2/r^3 = 0$ gives $r_0 = h^2/k$.

(b) $U_{\text{eff}}''(r) = -2k/r^3 + 3h^2/r^4$. At $r_0 = h^2/k$,
$U_{\text{eff}}''(r_0) = -2k^4/h^6 + 3k^4/h^6 = k^4/h^6 > 0$.

(c) Small radial oscillations obey $\delta\ddot r = -U_{\text{eff}}''(r_0)\delta r$, so
$\omega_{\text{rad}}^2 = k^4/h^6$. The orbital angular frequency is
$\dot\theta = h/r_0^2 = h/(h^4/k^2) = k^2/h^3$, so $\dot\theta^2 = k^4/h^6 = \omega_{\text{rad}}^2$. The two
frequencies are equal: the orbit is a closed ellipse, and a small radial kick does not make the particle
drift in angle.

*Check.* For gravity $k = GM$, $r_0 = h^2/(GM)$ and $\omega = GM/r_0^2 \cdot r_0/h$... more simply
$\omega = h/r_0^2 = (GM)^2/h^3$, which agrees with the general formula.

**18.** *(Strategy: reduce to the relative coordinate.)*

(a) $\mu = \dfrac{m_Em_M}{m_E+m_M} = \dfrac{(5.972\times10^{24})(7.348\times10^{22})}{6.0455\times10^{24}} = 7.259\times10^{22}\ \mathrm{kg}$.
The ratio is $\mu/m_M = 0.9878$: the reduced mass is only $1.2\%$ below the Moon's mass, which is why
treating the Moon as a test particle is a good approximation.

(b) For the relative coordinate, $\ddot{\mathbf{r}} = -G(m_E+m_M)\hat{\mathbf{r}}/r^2$, so the
acceleration magnitude is

$$a = \frac{G(m_E+m_M)}{r^2} = \frac{(6.674\times10^{-11})(6.0455\times10^{24})}{(3.844\times10^8)^2} = 2.731\times10^{-3}\ \mathrm{m/s^2}.$$

(c) $T = 2\pi\sqrt{r^3/[G(m_E+m_M)]}$. With $r^3 = 5.681\times10^{25}$ and
$G(m_E+m_M) = 4.035\times10^{14}$,

$$T = 2\pi\sqrt{1.408\times10^{11}} = 2\pi(3.752\times10^5) = 2.358\times10^6\ \mathrm{s} = 27.29\ \mathrm{days}.$$

*Check.* The observed sidereal month is $27.32$ days; the small discrepancy comes from treating the orbit as
circular and ignoring the Sun's tidal perturbation. The synodic month of $29.53$ days is different because
the Earth–Moon system also moves around the Sun.

**19.** *(Strategy: perihelion and aphelion determine $a$ and $e$; the vis-viva equation gives speeds.)*

(a) $a = (r_p+r_a)/2 = (0.5+30)/2 = 15.25\ \mathrm{AU}$ and
$e = (r_a-r_p)/(r_a+r_p) = 29.5/30.5 = 0.9672$.

(b) In solar units $T = a^{3/2} = (15.25)^{3/2} = 59.55$ years.

(c) With $GM_\odot = 1.327\times10^{20}\ \mathrm{m^3/s^2}$ and $1\ \mathrm{AU} = 1.496\times10^{11}\ \mathrm{m}$,

$$v_p = \sqrt{GM_\odot\Bigl(\frac{2}{r_p}-\frac{1}{a}\Bigr)} = \sqrt{\frac{GM_\odot}{\mathrm{AU}}\Bigl(\frac{2}{0.5}-\frac{1}{15.25}\Bigr)} = 29.78\sqrt{4-0.0656} = 59.08\ \mathrm{km/s},$$

$$v_a = \sqrt{\frac{GM_\odot}{\mathrm{AU}}\Bigl(\frac{2}{30}-\frac{1}{15.25}\Bigr)} = 29.78\sqrt{0.06667-0.06557} = 0.985\ \mathrm{km/s}.$$

(d) $r_pv_p = (0.5)(59.08) = 29.54\ \mathrm{AU\,km/s}$ and $r_av_a = (30)(0.985) = 29.54\ \mathrm{AU\,km/s}$.
The product is the specific angular momentum $h$, constant by Kepler's second law.

*Check.* The comet moves about $60$ times faster at perihelion than at aphelion, which is why it spends
almost all of its time near aphelion: the area law forces the angular speed to be tiny when $r$ is large.

**20.** *(Strategy: the Lagrangian is that of a repulsive oscillator.)*

(a) From §7.9, $\ddot r = \Omega^2 r$ with $r(0)=r_0$ and $\dot r(0)=0$, so
$r(t) = r_0\cosh(\Omega t) = 0.1\cosh(3t)\ \mathrm{m}$.

(b) Solve $0.1\cosh(3t) = 1$, so $\cosh(3t) = 10$ and
$3t = \operatorname{arcosh}(10) = \ln(10+\sqrt{99}) = \ln(19.9499) = 2.9932$. Hence $t = 0.9977\ \mathrm{s}$.

(c) Linearising about $r=0$ gives $\ddot r = \Omega^2r$ with a positive coefficient. Small displacements grow
like $e^{\Omega t}$, so the equilibrium is unstable: the further the bead goes, the stronger the
centrifugal force pushing it out. In the rotating frame this is the centrifugal force; in the inertial
frame it is inertia, the bead trying to move in a straight line while the wire turns under it.

*Check.* $\cosh(2.9932) = 10.0$ ✓. The time is almost exactly $\Omega^{-1}$, as expected since
$\operatorname{arcosh}10 \approx 3$.

**21.** *(Strategy: Hamilton's equations are two first-order equations.)*

(a) With $H = p^2/(2m) + \tfrac12kx^2$ and $m=1$, $k=4$: $H = \tfrac12p^2 + 2q^2$, so
$\dot q = p$ and $\dot p = -4q$.

(b) Differentiating $\dot q = p$ gives $\ddot q = -4q$, so $q = A\cos2t + B\sin2t$. With $q(0)=1$ and
$p(0)=\dot q(0)=0$: $q = \cos2t$, $p = \dot q = -2\sin2t$.

(c) $q^2 + p^2/4 = \cos^2 2t + \sin^2 2t = 1$: an ellipse with semi-axis $1$ in $q$ and $2$ in $p$.

(d) $H = \tfrac12(4\sin^22t) + 2\cos^22t = 2(\sin^22t+\cos^22t) = 2$, constant. ✓

*Check.* The initial energy is $\tfrac12kq(0)^2 = 2$, which matches $H$. The phase-space area enclosed by
the orbit is $\pi(1)(2) = 2\pi$; for a harmonic oscillator the area is $2\pi E/\omega$, here
$2\pi(2)/2 = 2\pi$ ✓.

**22.** *(Strategy: use $c=\sqrt{\tau/\rho}$ and the fixed-end mode formula.)*

(a) $c = \sqrt{120/0.02} = \sqrt{6000} = 77.46\ \mathrm{m/s}$.

(b) $f_1 = c/(2L) = 77.46/1.6 = 48.41\ \mathrm{Hz}$.

(c) $f_3 = 3f_1 = 145.2\ \mathrm{Hz}$. The wavelength is $\lambda_3 = c/f_3 = 77.46/145.2 = 0.5333\ \mathrm{m}$,
which is $2L/3$, as a standing wave with three half-wavelengths must be.

*Check.* $\lambda_1 = 2L = 1.6\ \mathrm{m}$ and $f_1 = c/\lambda_1 = 48.41\ \mathrm{Hz}$ ✓. The third harmonic
has three times the frequency and one third the wavelength.

**23.** *(Strategy: steady state means $u_t=0$, so $u_{xx}=0$.)*

(a) $u_{xx}=0$ gives $u = C_1x + C_2$. The boundary conditions give $C_2=0$ and
$C_1 = 100$, so $u(x) = 100x\ ^\circ\mathrm{C}$.

(b) Fourier's law: $q = -k\dfrac{du}{dx} = -400(100) = -4.00\times10^4\ \mathrm{W/m^2}$. The negative sign
means the flux is in the $-x$ direction: heat flows from the hot end at $x=1$ to the cold end at $x=0$.

(c) At steady state, conservation of energy for any slice requires the flux to be the same across every
cross-section; otherwise heat would accumulate somewhere and the temperature would change. Since
$du/dx$ is constant, $q$ is constant.

*Check.* The temperature is linear, the flux is uniform, and the sign agrees with "hot to cold". ✓

**24.** *(Strategy: match the symmetry to the Noether formula $J = p\,\delta q$.)*

(a) Under $q\mapsto q+\varepsilon$, $\delta q = 1$ and $L = \tfrac12m\dot q^2$ is unchanged because $\dot q$
is unchanged. Noether gives $J = \dfrac{\partial L}{\partial\dot q}\delta q = m\dot q$, the momentum. The
coordinate $q$ is cyclic, so its conjugate momentum is conserved: the particle moves uniformly.

(b) $L = \tfrac12m\dot q^2 - mgq$ has $\partial L/\partial t = 0$, so time translation is a symmetry. The
conserved quantity is the Hamiltonian

$$H = p\dot q - L = m\dot q^2 - \bigl(\tfrac12m\dot q^2 - mgq\bigr) = \tfrac12m\dot q^2 + mgq,$$

which is the total mechanical energy (kinetic plus gravitational potential $mgq$, with $q$ measured
upward). Since $H$ does not depend explicitly on time, $\dot H = 0$.

*Check.* Directly, $\dot H = m\dot q\ddot q + mg\dot q = \dot q(m\ddot q + mg) = 0$ by the equation of
motion $m\ddot q = -mg$ ✓.

## Advanced

**25.** *(Strategy: differencing the action and moving the derivative off $\delta\dot q$.)*

Let $q_\varepsilon = q + \varepsilon\,\delta q$ with $\delta q(t_0) = \delta q(t_1) = 0$. Then

$$\frac{d}{d\varepsilon}S[q_\varepsilon]\Big|_{\varepsilon=0}
= \int_{t_0}^{t_1}\Bigl(\frac{\partial L}{\partial q}\delta q + \frac{\partial L}{\partial\dot q}\delta\dot q\Bigr)dt.$$

(a) *Integration by parts.* Since $L$ is smooth and $q$ is twice differentiable, $\dfrac{\partial L}{\partial\dot q}\delta q$
is continuously differentiable on $[t_0,t_1]$, so the fundamental theorem of calculus applies:

$$\int_{t_0}^{t_1}\frac{\partial L}{\partial\dot q}\,\delta\dot q\,dt
= \Bigl[\frac{\partial L}{\partial\dot q}\delta q\Bigr]_{t_0}^{t_1}
- \int_{t_0}^{t_1}\frac{d}{dt}\Bigl(\frac{\partial L}{\partial\dot q}\Bigr)\delta q\,dt.$$

(b) The boundary term vanishes because $\delta q(t_0) = \delta q(t_1) = 0$: the endpoints of the path are
held fixed, so variations are not allowed there.

(c) Hence $\dfrac{dS}{d\varepsilon} = \int_{t_0}^{t_1}\Bigl(\dfrac{\partial L}{\partial q} - \dfrac{d}{dt}\dfrac{\partial L}{\partial\dot q}\Bigr)\delta q\,dt$.
If this is zero for every continuous $\delta q$ vanishing at the endpoints, the bracket must vanish at every
interior point: otherwise choose a variation supported in a small interval where the bracket has a fixed
sign, and the integral would be nonzero (the fundamental lemma of the calculus of variations).

**Adding a total derivative.** If $L' = L + \dfrac{dF(q,t)}{dt}$ with
$\dfrac{dF}{dt} = \dfrac{\partial F}{\partial q}\dot q + \dfrac{\partial F}{\partial t}$, then

$$S' = S + \int_{t_0}^{t_1}\frac{dF}{dt}\,dt = S + F(q(t_1),t_1) - F(q(t_0),t_0).$$

The added term depends only on the endpoints, which are fixed during the variation, so its variation is zero
and $S'$ has the same stationary paths as $S$. Equivalently, the Euler–Lagrange equations of $L'$ and $L$
coincide.

*Check.* For $L = \tfrac12m\dot q^2 - V(q)$ the derivation gives $m\ddot q = -V'(q)$; the signs are
consistent because $\partial L/\partial q = -V'$.

**26.** *(Strategy: compute the area swept and use the relation between $h$, $p$ and $a$.)*

The areal velocity is $\tfrac12r^2\dot\theta = \tfrac12h$, so the period is
$T = \dfrac{\text{area of ellipse}}{\tfrac12h} = \dfrac{\pi ab}{h/2} = \dfrac{2\pi ab}{h}$.

For an ellipse with semi-major axis $a$ and eccentricity $e$, the semi-minor axis is $b = a\sqrt{1-e^2}$. From
Binet's equation the orbit is $r = p/(1+e\cos\theta)$ with $p = h^2/GM$, and the perihelion and aphelion
distances are $p/(1+e)$ and $p/(1-e)$. Therefore

$$a = \frac12\Bigl(\frac{p}{1+e}+\frac{p}{1-e}\Bigr) = \frac{p}{1-e^2}, \qquad p = a(1-e^2).$$

Solving $p = h^2/GM$ for $h$: $h = \sqrt{GMa(1-e^2)}$. Substituting,

$$T = \frac{2\pi a\,a\sqrt{1-e^2}}{\sqrt{GMa(1-e^2)}} = 2\pi\sqrt{\frac{a^3}{GM}}.$$

Squaring gives $T^2 = \dfrac{4\pi^2}{GM}a^3$. For two bodies of masses $m_1,m_2$, the relative equation has
$GM = G(m_1+m_2)$, which gives the stated form.

*Check.* For a circular orbit $e=0$, $a=r$ and $T = 2\pi\sqrt{r^3/(GM)}$, which is exactly the circular-orbit
result of §7.7. The derivation also shows why the constant is $4\pi^2$ and not some other number: it is the
area of a circle divided by the areal velocity.

**27.** *(Strategy: differentiate the energy and use Newton's equations pairwise.)*

Let $\mathbf{F}_{ij} = -\nabla_{\mathbf{r}_i}V_{ij}(\lVert\mathbf{r}_i-\mathbf{r}_j\rVert)$ be the force on $i$
due to $j$, and assume $\mathbf{F}_{ij} = -\mathbf{F}_{ji}$ (which follows from the potential depending only
on $\lVert\mathbf{r}_i-\mathbf{r}_j\rVert$). Newton's equations are
$m_i\ddot{\mathbf{r}}_i = \sum_{j\ne i}\mathbf{F}_{ij}$.

Differentiate the kinetic energy:

$$\frac{d}{dt}\sum_i\tfrac12m_i\lVert\dot{\mathbf{r}}_i\rVert^2
= \sum_i m_i\dot{\mathbf{r}}_i\cdot\ddot{\mathbf{r}}_i
= \sum_i\sum_{j\ne i}\dot{\mathbf{r}}_i\cdot\mathbf{F}_{ij}.$$

Pair the $(i,j)$ and $(j,i)$ terms:

$$\dot{\mathbf{r}}_i\cdot\mathbf{F}_{ij} + \dot{\mathbf{r}}_j\cdot\mathbf{F}_{ji}
= (\dot{\mathbf{r}}_i-\dot{\mathbf{r}}_j)\cdot\mathbf{F}_{ij}.$$

For a central potential $V_{ij}$ depending on $\mathbf{r}_i-\mathbf{r}_j$,

$$\frac{d}{dt}V_{ij}(\lVert\mathbf{r}_i-\mathbf{r}_j\rVert)
= \nabla V_{ij}\cdot(\dot{\mathbf{r}}_i-\dot{\mathbf{r}}_j)
= -\mathbf{F}_{ij}\cdot(\dot{\mathbf{r}}_i-\dot{\mathbf{r}}_j).$$

Hence the rate of change of the total kinetic energy is minus the rate of change of the total potential
energy, so $E$ is constant. The hypotheses used are: (i) no external forces; (ii) each internal force is
conservative with a pair potential depending only on separation; (iii) the potential is symmetric under
exchange, which gives $\mathbf{F}_{ij} = -\mathbf{F}_{ji}$.

*Check.* For two particles with $V = \tfrac12k\lVert\mathbf{r}_1-\mathbf{r}_2\rVert^2$, the result reduces to
the energy of a single oscillator of reduced mass $\mu$ and stiffness $k$, which is conserved.

**28.** *(Strategy: three separate arguments, all using the radial equation.)*

(a) $\dot{\mathbf{L}} = \mathbf{r}\times\mathbf{F} = \mathbf{r}\times f(r)\hat{\mathbf{r}} = \mathbf{0}$
because $\mathbf{r}$ is parallel to $\hat{\mathbf{r}}$. Hence $\mathbf{L}$ is a constant vector. If
$\mathbf{L}\ne\mathbf{0}$, then $\mathbf{r}\cdot\mathbf{L} = 0$ for all time (since $\mathbf{L}$ is
orthogonal to both $\mathbf{r}$ and $\dot{\mathbf{r}}$), so the motion lies in the plane through the origin
perpendicular to $\mathbf{L}$. If $\mathbf{L}=\mathbf{0}$ the motion is along a line through the origin,
which is a degenerate plane.

(b) In polar coordinates the position is $\mathbf{r} = r\hat{\mathbf{r}}$ and the area swept in $dt$ is
$\tfrac12r^2\,d\theta$. Hence $\dfrac{dA}{dt} = \tfrac12r^2\dot\theta = \tfrac12h$, constant because $h$ is
conserved.

(c) The radial equation is $m\ddot r = -U_{\text{eff}}'(r)$ with $U_{\text{eff}} = U + mh^2/(2r^2)$. At a
circular orbit $r_0$, $U_{\text{eff}}'(r_0)=0$. Set $r = r_0+\delta r$ and Taylor expand:
$U_{\text{eff}}'(r) = U_{\text{eff}}''(r_0)\delta r + O(\delta r^2)$, so
$m\,\delta\ddot r = -U_{\text{eff}}''(r_0)\delta r$. The linearised equation has oscillatory solutions
exactly when $U_{\text{eff}}''(r_0)>0$ and exponentially growing ones when it is negative. Therefore the
circular orbit is stable iff $U_{\text{eff}}''(r_0)>0$.

*Check.* For $U=-k/r$, $U_{\text{eff}}''(r_0) = k/r_0^3>0$, so all circular orbits are stable. For a
potential falling faster than $1/r^2$, such as $U=-k/r^3$, a circular orbit still exists (at
$r_0 = 3k/(mh^2)$) but $U_{\text{eff}}''(r_0) = -3k/r_0^5 < 0$, so it is unstable.

**29.** *(Strategy: factor the operator and match the initial data.)*

(a) The wave operator factors:

$$\partial_t^2 - c^2\partial_x^2 = (\partial_t - c\partial_x)(\partial_t + c\partial_x).$$

Let $u = y_t + cy_x$ and $v = y_t - cy_x$. Then $u_t - cu_x = 0$ and $v_t + cv_x = 0$, so $u = u_0(x+ct)$
and $v = v_0(x-ct)$ are travelling waves. Adding and integrating gives
$y(x,t) = f(x-ct) + g(x+ct)$ with $f,g$ twice differentiable.

(b) Let $y(x,t) = \tfrac12[y_0(x-ct)+y_0(x+ct)] + \dfrac{1}{2c}\int_{x-ct}^{x+ct}v_0(s)\,ds$. Differentiate:

$$y_t = \tfrac12[-cy_0'(x-ct)+cy_0'(x+ct)] + \tfrac12[v_0(x+ct)+v_0(x-ct)],$$

$$y_{tt} = \tfrac12[c^2y_0''(x-ct)+c^2y_0''(x+ct)] + \tfrac{c}{2}[v_0'(x+ct)-v_0'(x-ct)],$$

$$y_x = \tfrac12[y_0'(x-ct)+y_0'(x+ct)] + \tfrac{1}{2c}[v_0(x+ct)-v_0(x-ct)],$$

$$y_{xx} = \tfrac12[y_0''(x-ct)+y_0''(x+ct)] + \tfrac{1}{2c}[v_0'(x+ct)-v_0'(x-ct)].$$

Thus $c^2y_{xx}$ equals $y_{tt}$, using $c^2\cdot\tfrac{1}{2c} = \tfrac{c}{2}$. At $t=0$,
$y = \tfrac12[y_0(x)+y_0(x)] = y_0(x)$ and $y_t = \tfrac12[-cy_0'+cy_0'] + \tfrac12[v_0+v_0] = v_0(x)$ ✓.

(c) On a finite string with fixed ends, a right-moving pulse reflects at $x=L$ and returns as a
left-moving pulse with a sign change (the boundary condition $y(L,t)=0$ forces it). The whole-line formula
does not know about the boundary; one handles the problem by extending the initial data oddly about
$x=0$ and $x=L$ (the method of images), so that the odd extension automatically enforces the boundary
conditions at all times.

*Check.* $y = \cos(x-ct)$ solves $y_{tt} = c^2y_{xx}$ and represents a right-moving wave, as expected.

**30.** *(Strategy: substitute the ansatz and reduce to an ODE.)*

(a) Let $u = t^{-1/2}f(\eta)$ with $\eta = x/\sqrt{\alpha t}$. Then

$$u_t = -\tfrac12t^{-3/2}f - t^{-1/2}f'(\eta)\cdot\frac{x}{2\sqrt{\alpha}\,t^{3/2}}
= -t^{-3/2}\bigl(\tfrac12f + \tfrac12\eta f'\bigr),$$

and $u_{xx} = t^{-1/2}f''(\eta)\cdot\dfrac{1}{\alpha t} = \alpha^{-1}t^{-3/2}f''$, so
$\alpha u_{xx} = t^{-3/2}f''$. Equating,

$$f'' + \tfrac12\eta f' + \tfrac12 f = 0.$$

(b) Observe that $f'' + \tfrac12\eta f' + \tfrac12f = \dfrac{d}{d\eta}\bigl(f' + \tfrac12\eta f\bigr)$. Hence
$f' + \tfrac12\eta f = C$; boundedness as $\lvert\eta\rvert\to\infty$ forces $C=0$. Then
$f'/f = -\eta/2$, so $f = A e^{-\eta^2/4}$.

Normalising, $\int u\,dx = t^{-1/2}\sqrt{\alpha t}\int f\,d\eta = \sqrt{\alpha}A\sqrt{4\pi} = 1$, giving
$A = 1/\sqrt{4\pi\alpha}$ and

$$u(x,t) = \frac{1}{\sqrt{4\pi\alpha t}}e^{-x^2/(4\alpha t)}.$$

(c) The width is of order $\sqrt{\alpha t}$ and the height of order $(\alpha t)^{-1/2}$; their product is
constant, which is conservation of the integral. The solution is self-similar: profiles at different times
are the same curve rescaled.

*Check.* $\int u\,dx = 1$ for all $t>0$; as $t\to0^+$, $u\to\delta(x)$ in the distributional sense.

**31.** *(Strategy: the dimension matrix has rank three because mass is present only in $m$.)*

(a) The quantities are $T,l,g,m$ with dimensions $T$, $L$, $LT^{-2}$, $M$. The dimension matrix (rows
$M,L,T$; columns $T,l,g,m$) has rank $3$, so there is $4-3 = 1$ dimensionless group. Solving
$T^al^bg^cm^d$ dimensionless gives $d=0$, $b=-c$, $a=2c$; choosing $c=-\tfrac12$ gives
$\Pi = T^{-1}l^{1/2}g^{-1/2}$. Hence $T\sqrt{g/l} = C$, a dimensionless constant, and $T = C\sqrt{l/g}$.
Mass does not appear because $d=0$: no other quantity contains $M$, so no dimensionless combination can
involve $m$.

(b) At large amplitude the initial angle $\theta_0$ is a dimensionless parameter and the period becomes
$T = \sqrt{l/g}\,\Phi(\theta_0)$. Dimensional analysis cannot determine $\Phi$; the exact result is
$\Phi(\theta_0) = 4K(\sin(\theta_0/2))$, and for small $\theta_0$,
$\Phi = 2\pi(1+\theta_0^2/16+O(\theta_0^4))$, consistent with the $1.7\%$ correction at $30^\circ$.

*Check.* At $\theta_0\to0$, $\Phi\to2\pi$ and the elementary formula is recovered. ✓

**32.** *(Strategy: compare $dH$ from the definition with $dH$ from the chain rule.)*

From $H = \sum_ip_i\dot q_i - L(q,\dot q,t)$,

$$dH = \sum_i\bigl(\dot q_i\,dp_i + p_i\,d\dot q_i\bigr)
- \sum_i\Bigl(\frac{\partial L}{\partial q_i}dq_i + \frac{\partial L}{\partial\dot q_i}d\dot q_i\Bigr)
- \frac{\partial L}{\partial t}dt.$$

The $d\dot q_i$ terms cancel because $p_i = \partial L/\partial\dot q_i$. On a solution,
$\partial L/\partial q_i = \dot p_i$ by the Euler–Lagrange equation, so

$$dH = \sum_i\bigl(\dot q_i\,dp_i - \dot p_i\,dq_i\bigr) - \frac{\partial L}{\partial t}dt.$$

Comparing with $dH = \sum_i\bigl(\frac{\partial H}{\partial q_i}dq_i + \frac{\partial H}{\partial p_i}dp_i\bigr) + \frac{\partial H}{\partial t}dt$
gives $\dot q_i = \partial H/\partial p_i$, $\dot p_i = -\partial H/\partial q_i$ and
$\partial H/\partial t = -\partial L/\partial t$.

Along a solution, $\dfrac{dH}{dt} = \sum_i\Bigl(\frac{\partial H}{\partial q_i}\dot q_i + \frac{\partial H}{\partial p_i}\dot p_i\Bigr) + \frac{\partial H}{\partial t} = \sum_i\Bigl(\frac{\partial H}{\partial q_i}\frac{\partial H}{\partial p_i} - \frac{\partial H}{\partial p_i}\frac{\partial H}{\partial q_i}\Bigr) + \frac{\partial H}{\partial t} = \frac{\partial H}{\partial t}$.

If $L$ has no explicit time dependence then $\partial H/\partial t = -\partial L/\partial t = 0$ and $H$ is
conserved: energy conservation is the Hamiltonian counterpart of the time-translation symmetry of §7.13.

*Check.* For $H = p^2/(2m)+V(q)$, $\dot H = \dot q\dot p + V'(q)\dot q = (p/m)(-V') + V'(p/m) = 0$ ✓.

## Challenge

**33.** *(Strategy: analyse $f(\theta) = \sin\theta(\Omega^2\cos\theta-g/a)$.)*

(a) Equilibria solve $\sin\theta = 0$ or $\cos\theta = g/(a\Omega^2)$. Here
$g/(a\Omega^2) = 9.81/((0.15)(81)) = 0.8074$, so $\theta^* = \pm36.16^\circ$; the other equilibria are
$\theta=0$ and $\theta=\pi$.

(b) Write the equation as $\ddot\theta = f(\theta)$ with $f(\theta) = \sin\theta(\Omega^2\cos\theta-g/a)$.
The linearisation about an equilibrium $\theta_e$ is $\ddot\psi = f'(\theta_e)\psi$, since $f(\theta_e)=0$.

* At $\theta=0$: $f'(0) = \Omega^2-g/a = 81-65.4 = 15.6>0$, so $\ddot\psi = 15.6\,\psi$: unstable.
* At $\theta=\pi$: $f'(\pi) = \cos\pi\,(\Omega^2\cos\pi-g/a) = (-1)(-\Omega^2-g/a) = \Omega^2+g/a > 0$,
  so $\ddot\psi = 146.4\,\psi$: unstable. The top is a maximum of the potential, as expected.
* At $\theta^*$: $f'(\theta^*) = \cos\theta^*\cdot 0 + \sin\theta^*(-\Omega^2\sin\theta^*) = -\Omega^2\sin^2\theta^* = -81(0.3481) = -28.20 < 0$,
  so stable.

(c) $\omega = \sqrt{28.20} = 5.310\ \mathrm{rad/s}$ and $T = 2\pi/\omega = 1.183\ \mathrm{s}$.

(d) As $\Omega$ decreases through $\Omega_c = \sqrt{g/a} = 8.087\ \mathrm{rad/s}$, the two tilted equilibria
merge with $\theta=0$ at the pitchfork bifurcation; below $\Omega_c$ only $\theta=0$ and $\theta=\pi$ remain,
and the bottom becomes stable. The transition is second order: $\theta^*\propto\sqrt{\Omega-\Omega_c}$ near
the threshold.

*Check.* $\cos\theta^* = 0.8074$ gives $\sin\theta^* = 0.5900$ and $\omega = 9(0.5900) = 5.310$, consistent
with (c). ✓

**34.** *(Strategy: reduce to the relative coordinate with $\mu = m/2$.)*

(a) With $M = 2m$ and separation $d$,

$$T = 2\pi\sqrt{\frac{d^3}{G(2m)}} = 2\pi\sqrt{\frac{(1.496\times10^{11})^3}{2(6.674\times10^{-11})(1.989\times10^{30})}} = 2.231\times10^7\ \mathrm{s} = 0.7070\ \mathrm{yr}.$$

(b) Each star moves on a circle of radius $d/2$ about the centre of mass, so its speed is
$v = \pi d/T = \pi(1.496\times10^{11})/(2.231\times10^7) = 2.106\times10^4\ \mathrm{m/s}$.

(c) Total kinetic energy: $2\cdot\tfrac12mv^2 = m v^2 = (1.989\times10^{30})(2.106\times10^4)^2 = 8.825\times10^{38}\ \mathrm{J}$.
The orbital energy is $E = -G(2m)\mu/(2a)$ with $a=d$ and $\mu=m/2$:

$$E = -\frac{G(2m)(m/2)}{2d} = -\frac{Gm^2}{2d} = -8.825\times10^{38}\ \mathrm{J}.$$

So $E = -T$, which is the general virial relation for a circular orbit: $2T + V = 0$ and $E = T+V = -T$.

(d) The relative coordinate obeys $\mu\ddot{\mathbf{r}} = -G(2m)\mu\,\hat{\mathbf{r}}/r^2$, that is
$\ddot{\mathbf{r}} = -G(2m)\hat{\mathbf{r}}/r^2$. This is Kepler's problem with total mass $2m$, so
$T^2 = 4\pi^2d^3/[G(2m)]$, exactly the formula used in (a).

*Check.* $v_{\text{rel}} = 2v = 42.13\ \mathrm{km/s}$; the relative circular speed is
$\sqrt{G(2m)/d} = \sqrt{2(6.674\times10^{-11})(1.989\times10^{30})/(1.496\times10^{11})} = 42.13\ \mathrm{km/s}$ ✓.

**35.** *(Strategy: one dimensionless group, then scale.)*

(a) Seek $R = CE^a\rho^bt^c$. Dimensions: $[R]=L$, $[E]=ML^2T^{-2}$, $[\rho]=ML^{-3}$, $[t]=T$. Matching:
$M$: $a+b=0$; $L$: $2a-3b=1$; $T$: $-2a+c=0$. From $b=-a$, $5a=1$, so $a=1/5$, $b=-1/5$, $c=2/5$, and
$R = C(Et^2/\rho)^{1/5}$.

(b) $(Et^2/\rho)^{1/5}$ with $E=4.184\times10^{13}$, $\rho=1.225$:

| $t$ | $Et^2/\rho$ | $R$ (m) |
|---|---|---|
| $1\ \mathrm{ms}$ | $3.416\times10^7$ | $32.11$ |
| $10\ \mathrm{ms}$ | $3.416\times10^9$ | $80.67$ |
| $0.1\ \mathrm{s}$ | $3.416\times10^{11}$ | $202.6$ |
| $1\ \mathrm{s}$ | $3.416\times10^{13}$ | $509.0$ |

(c) $R(1)/R(0.01) = (100)^{2/5} = 10^{0.8} = 6.310$; indeed $509.0/80.67 = 6.310$ ✓.

(d) At very early times the energy is not released instantaneously and the shock is not yet strong; the
finite size of the explosive and the details of the detonation matter. At very late times the shock
strength falls to the ambient pressure, the sound speed $c_s$ enters, and a second dimensionless group
(the Mach number, or $p_\infty t^2/(\rho R^2)$) is needed. The $t^{2/5}$ law is the intermediate asymptotic
regime, which is precisely the regime in which the idealised assumptions hold.

*Check.* The exponents satisfy the dimensional equations; the numerical ratios are exact powers of $100$.

**36.** *(Strategy: use the Euler–Lagrange equations to reduce the variation to a boundary term.)*

**Statement.** Let $L(q,\dot q,t)$ be invariant under a one-parameter family
$q\mapsto q+\varepsilon\,\delta q$ (that is, $\delta S = 0$ to first order for this family). Then on every
solution of the Euler–Lagrange equations,

$$J = \sum_i\frac{\partial L}{\partial\dot q_i}\,\delta q_i$$

is constant.

**Proof.** For the family, the variation of the action is

$$0 = \frac{d}{d\varepsilon}S\Big|_{\varepsilon=0}
= \int_{t_0}^{t_1}\sum_i\Bigl(\frac{\partial L}{\partial q_i}\delta q_i + \frac{\partial L}{\partial\dot q_i}\delta\dot q_i\Bigr)dt.$$

Integrating the second term by parts,

$$0 = \int_{t_0}^{t_1}\sum_i\Bigl(\frac{\partial L}{\partial q_i} - \frac{d}{dt}\frac{\partial L}{\partial\dot q_i}\Bigr)\delta q_i\,dt
+ \Bigl[\sum_i\frac{\partial L}{\partial\dot q_i}\delta q_i\Bigr]_{t_0}^{t_1}.$$

On a solution the bracket in the integral vanishes, so
$\bigl[J\bigr]_{t_0}^{t_1} = 0$ for every interval. Hence $J$ is constant. $\blacksquare$

(a) *Translation.* $\delta q_i = 1$ for the translated coordinate, $0$ otherwise. Then $J = p_i$, the
conjugate momentum. If $L$ does not depend on $q_i$, the Euler–Lagrange equation already says
$\dot p_i = 0$; Noether explains why.

(b) *Rotation.* For $\delta\mathbf{r} = \boldsymbol{\epsilon}\times\mathbf{r}$,
$J = \mathbf{p}\cdot(\boldsymbol{\epsilon}\times\mathbf{r}) = \boldsymbol{\epsilon}\cdot(\mathbf{r}\times\mathbf{p})$,
so each component of angular momentum is conserved.

(c) *Time translation.* Shifting the whole trajectory in time, $t\mapsto t+\varepsilon$ with
$q(t)\mapsto q(t-\varepsilon)$, is a symmetry when $\partial L/\partial t=0$. In the fixed-time description
the generator is $\delta q_i = -\dot q_i\,\delta t$, and the moving-endpoint contribution to the boundary
term is $L\,\delta t$. Together,

$$J = \sum_i p_i\,\delta q_i + L\,\delta t
= \Bigl(-\sum_i p_i\dot q_i + L\Bigr)\delta t = -H\,\delta t,$$

so the conserved quantity is the Hamiltonian $H = \sum_i p_i\dot q_i - L$. Equivalently,
$\dfrac{dH}{dt} = -\dfrac{\partial L}{\partial t} = 0$ when $L$ has no explicit time dependence. So
time-translation symmetry is conservation of energy.

**Why a cyclic coordinate gives momentum conservation.** If $\partial L/\partial x = 0$, then $x$ does not
appear in $L$, so translating $x$ leaves $L$ unchanged. Noether's theorem with $\delta x = 1$ gives
$J = p_x$, and the Euler–Lagrange equation gives $\dot p_x = \partial L/\partial x = 0$ directly. The two
arguments agree; Noether's is the one that generalises to field theory, where the conserved quantities are
currents and the symmetry may be internal rather than spatial.
