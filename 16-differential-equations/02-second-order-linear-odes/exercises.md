# Second-Order Linear ODEs — Exercises

> [Second-Order Linear ODEs](README.md) · 34 problems · Beginner → Challenge · Solutions: [solutions.md](solutions.md)

Work through the problems in order; each cites the section of the tutorial it draws on. Problems 1–12
build fluency with the characteristic equation and the basic particular-solution shapes; 13–22 combine
a method with an initial condition, a resonance case or a change of variable; 23–30 are derivations and
modelling problems; 31–34 extend the theory and are marked as challenge.

Attempt every problem before opening [solutions.md](solutions.md), and **verify every solution by
substitution**: differentiate twice, collect coefficients, and confirm that the equation and the
initial conditions both hold. In this topic the check is mechanical and it catches almost every error.

Conventions: $x$ or $t$ is the independent variable, primes denote derivatives with respect to it,
$\ln$ is natural and angles are in radians. Unless a domain is given, state the largest interval on
which your solution is defined.

## Beginner

**1.** *(§5.1)* For each equation state the order, whether it is linear, whether it is homogeneous, and whether the coefficients are constant or variable: (a) $y'' + 3y' + 2y = 0$; (b) $y'' + y^{2} = 0$; (c) $x^{2}y'' + xy' + y = 0$; (d) $y'' + y = \sin x$.

**2.** *(§7.2)* Solve $y'' - 5y' + 6y = 0$.

**3.** *(§7.2)* Solve $y'' + 9y = 0$.

**4.** *(§7.2)* Solve $y'' - 4y' + 4y = 0$.

**5.** *(§7.2)* Solve $y'' + y = 0$ with $y(0) = 2$, $y'(0) = -1$.

**6.** *(§7.2)* Solve $y'' - y' - 2y = 0$ with $y(0) = 0$, $y'(0) = 3$.

**7.** *(§5.1, §7.1)* Compute the Wronskians and say whether the pair is a fundamental set, naming the equation when it is: (a) $e^{2x}$, $e^{3x}$; (b) $x$, $2x$; (c) $\cos 2x$, $\sin 2x$.

**8.** *(§7.2)* Verify that $y_{1} = e^{x}$ and $y_{2} = xe^{x}$ solve $y'' - 2y' + y = 0$ and that they are linearly independent. Which theorem guarantees that they span the whole solution space?

**9.** *(§7.3)* Solve $y'' - 3y' + 2y = 4x$.

**10.** *(§7.3)* Solve $y'' + 4y = 8$.

**11.** *(§7.3)* Solve $y'' - y = e^{2x}$.

**12.** *(§7.6)* Solve $x^{2}y'' - 3xy' + 4y = 0$ for $x > 0$.

## Intermediate

**13.** *(§7.3)* Solve $y'' - 3y' + 2y = e^{3x}$.

**14.** *(§7.3)* Solve $y'' + 9y = 6\cos 3x$.

**15.** *(§7.4)* Solve $y'' + 4y = \csc 2x$ on an interval where $\sin 2x > 0$.

**16.** *(§7.4)* Solve $y'' + y = \sec x$ on $\left(-\tfrac{\pi}{2},\tfrac{\pi}{2}\right)$.

**17.** *(§7.7)* Given that $y_{1} = x^{2}$ solves $x^{2}y'' - 3xy' + 4y = 0$ for $x > 0$, find a second independent solution.

**18.** *(§7.6)* Solve $x^{2}y'' + xy' - y = x$ for $x > 0$.

**19.** *(§7.5)* Solve $y'' + 2y' + 5y = 0$, state the damping ratio and damping regime, and give the amplitude–phase form of the general solution.

**20.** *(§7.3)* Solve $y'' + 2y' + y = 4\cos x$.

**21.** *(§7.3, §7.5)* Solve $y'' + 4y' + 5y = 10\cos t$ and identify the steady-state amplitude and phase lag.

**22.** *(§7.3)* Solve $y'' + 9y = 5\sin 2t$ with $y(0) = y'(0) = 0$. Sketch why the result looks like a fast oscillation inside a slow one.

## Advanced

**23.** *(§7.1)* Prove that the solution space of $y'' + p(x)y' + q(x)y = 0$, with $p, q$ continuous on an interval $I$, is a vector space of dimension exactly $2$.

**24.** *(§7.1)* Prove Abel's identity $W(x) = W(x_{0})e^{-\int_{x_{0}}^{x}p}$ and deduce that $W$ is either identically zero or never zero. Use it to show that two solutions of the same homogeneous equation which vanish at a common point are linearly dependent.

**25.** *(§7.5)* For $m\ddot{y} + c\dot{y} + ky = F_{0}\cos\omega t$, derive the steady-state amplitude $A(\omega)$ and the resonance frequency $\omega_{r}$, and evaluate both for $m = 1\ \mathrm{kg}$, $k = 25\ \mathrm{N/m}$, $c = 4\ \mathrm{N{\cdot}s/m}$, $F_{0} = 10\ \mathrm{N}$ and $\omega = 4\ \mathrm{rad/s}$.

**26.** *(§7.6)* Solve $x^{2}y'' + 3xy' + 5y = 0$ for $x > 0$.

**27.** *(§7.8)* A simply supported beam of length $L = 4\ \mathrm{m}$ carries a uniform load $w_{0} = 15\ \mathrm{kN/m}$. With $E = 200\ \mathrm{GPa}$ and $I = 8\times10^{-5}\ \mathrm{m^{4}}$, derive the deflection curve from $EI\,y'' = -M$ and compute $y_{\max}$.

**28.** *(§7.5, §7.8)* A $2\ \mathrm{kg}$ mass on a spring of stiffness $10\ \mathrm{N/m}$ with damping $4\ \mathrm{N{\cdot}s/m}$ is released from $y(0) = 0.05\ \mathrm{m}$ at rest. Solve the initial value problem, compute the damped frequency, the damping ratio and the logarithmic decrement, and state the amplitude ratio between consecutive cycles.

**29.** *(§7.8)* A series circuit has $L = 2\ \mathrm{H}$, $R = 8\ \Omega$, $C = 0.02\ \mathrm{F}$ and no source. The capacitor carries $q(0) = 10^{-3}\ \mathrm{C}$ and the current is zero. Find $q(t)$ and the first time at which the charge is zero.

**30.** *(§7.7)* Derive the reduction-of-order formula $y_{2} = y_{1}\int e^{-\int p\,dx}/y_{1}^{2}\,dx$, and apply it to $y'' + y = 0$ with $y_{1} = \cos x$ to recover $y_{2} = \sin x$.

## Challenge

**31.** *(§7.3, §7.5)* Solve the undamped forced problem $y'' + \omega_{0}^{2}y = F_{0}\cos\omega t$ with $y(0) = y'(0) = 0$ for $\omega \ne \omega_{0}$. Show that the solution can be written as a product of a slow envelope and a fast oscillation (beats), and take the limit $\omega \to \omega_{0}$ to obtain the resonant solution. Why is the limit legitimate?

**32.** *(§7.7, §7.1)* **Sturm comparison.** Let $q$ be continuous with $q(x) \ge m^{2} > 0$ and let $y \not\equiv 0$ solve $y'' + q(x)y = 0$. Prove that between any two consecutive zeros $a < b$ of $y$ one has $b - a \le \pi/m$, by comparing $y$ with $u(x) = \sin m(x-a)$ through the Wronskian $W = uy' - u'y$.

**33.** *(§7.5)* For $\ddot{y} + 2\zeta\omega_{0}\dot{y} + \omega_{0}^{2}y = 0$ with $\zeta \ge 0$, define the energy $E = \tfrac12\left(\dot{y}^{2} + \omega_{0}^{2}y^{2}\right)$. Show that $\dot{E} = -2\zeta\omega_{0}\dot{y}^{2} \le 0$, and deduce that the zero solution is stable for every $\zeta \ge 0$ and asymptotically stable exactly when $\zeta > 0$.

**34.** *(§7.6)* Solve $x^{2}y'' - 3xy' + 4y = x^{2}\ln x$ for $x > 0$. (The forcing is resonant: $\ln x$ appears where the indicial equation has a double root.)
