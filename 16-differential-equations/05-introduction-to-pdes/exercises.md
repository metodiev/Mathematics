# Introduction to PDEs — Exercises

> [Introduction to PDEs](README.md) · 36 problems · Beginner → Challenge · Solutions: [solutions.md](solutions.md)

Work through the problems in order; each cites the section of the tutorial it draws on. Problems 1–14
build fluency with definitions, verification, characteristics and the three model problems; 15–25 solve
complete boundary and initial value problems; 26–32 are proofs; 33–36 are challenge problems.
Attempt every problem before opening [solutions.md](solutions.md), and finish each one by **substituting
the answer back** into the PDE and checking the data.

Conventions: $u_t = \partial u/\partial t$; the heat equation is $u_t = \alpha u_{xx}$; the wave equation
is $u_{tt} = c^2u_{xx}$; the discriminant of $Au_{xx} + Bu_{xy} + Cu_{yy} + \dots = 0$ is
$\Delta = B^2 - 4AC$; $L$ is the length of the interval and $c$ the wave (or transport) speed.

## Beginner

**1.** *(§7.1)* For each equation state the order, and say whether it is linear, semilinear, quasilinear or fully nonlinear: (a) $u_t + uu_x = 0$; (b) $u_{xx} + u_{yy} = 0$; (c) $u_t = u_{xx} + \sin u$; (d) $u_x^2 + u_y = 0$; (e) $x^2u_{xx} + u_t = e^{-t}$.

**2.** *(§7.1)* Verify that $u(x,t) = e^{-9t}\cos 3x$ solves the heat equation and state the value of $\alpha$. What is the decay rate of the mode $\cos 2x$, and what is the rule?

**3.** *(§7.1)* Verify that $u(x,t) = \cos(x + 2t)$ solves a wave equation, and state the speed $c$. Which direction is it travelling in?

**4.** *(§7.2)* A rod of length $1$ is held at $0^\circ$ at both ends, and its initial temperature is $50 - 50\cos(2\pi x)$. Write down the complete set of conditions (initial and boundary) and say which type each one is.

**5.** *(§7.3)* State Hadamard's three conditions for a well-posed problem. Which one fails for the backward heat equation $u_t = -u_{xx}$ with $u(0,t) = u(\pi,t) = 0$? Justify your answer with an explicit pair of data.

**6.** *(§7.4)* Solve $u_t + 3u_x = 0$ on $\mathbb{R}$ with $u(x,0) = \sin x$. Evaluate $u(\pi,1)$ numerically.

**7.** *(§7.4)* Solve $u_t - 2u_x = 0$ with $u(x,0) = e^{-x^2}$. Evaluate $u(1,0.5)$.

**8.** *(§7.4)* For $u_t + 2u_x = 0$, describe the characteristic curves and state what is constant along each. If $u(x,0) = f(x)$ has a jump at $x = 0$, where is the jump at time $t = 3$?

**9.** *(§7.5)* Find the steady-state temperature of the rod $u_t = u_{xx}$ on $0 < x < 1$ with $u(0,t) = 20$ and $u(1,t) = 80$. Explain why it does not depend on the initial condition.

**10.** *(§7.5)* Solve $u_t = u_{xx}$ on $0<x<1$ with $u(0,t)=u(1,t)=0$ and $u(x,0) = \sin 2\pi x$. Evaluate $u(0.25,0.1)$ and state the time at which the amplitude falls below $10^{-3}$.

**11.** *(§7.5)* Solve $u_t = 9u_{xx}$ on $0<x<2$ with $u(0,t)=u(2,t)=0$ and $u(x,0) = \sin\frac{\pi x}{2}$. What is the slowest decay time constant?

**12.** *(§7.6)* Solve $u_{tt} = 4u_{xx}$ on $0<x<1$ with $u(0,t)=u(1,t)=0$, $u(x,0) = \sin 3\pi x$ and $u_t(x,0)=0$. State the period of the motion and evaluate $u(0.5,1/6)$.

**13.** *(§7.6)* Use d'Alembert's formula with $c = 1$, $f(x) = e^{-x^2}$ and $g \equiv 0$ to evaluate $u(0,1)$.

**14.** *(§7.7)* Verify that $u(x,y) = x^2 - y^2$ is harmonic and evaluate $u(1,2)$. Find all harmonic functions of the form $ax^2 + bxy + cy^2$ and state the condition relating $a$ and $c$.

## Intermediate

**15.** *(§7.4)* Solve $u_t + x u_x = 0$ with $u(x,0) = \sin x$, and evaluate $u(1,\ln 2)$.

**16.** *(§7.4)* Solve $u_t + 2u_x = t$ with $u(x,0) = 0$ by integrating along characteristics. Verify your answer by differentiation. Why does the solution not depend on $x$?

**17.** *(§7.5)* Solve $u_t = u_{xx}$ on $0<x<1$, $u(0,t)=u(1,t)=0$, $u(x,0) = x$. Compute the first four coefficients and tabulate $u(0.5,t)$ for $t = 0, 0.05, 0.1, 0.2$. Explain why the coefficients decay only like $1/n$ and yet the solution is smooth for $t>0$.

**18.** *(§7.5)* Solve the insulated rod $u_t = u_{xx}$ on $0<x<1$ with $u_x(0,t) = u_x(1,t) = 0$ and $u(x,0) = x$. Show that $u \to \tfrac12$ as $t\to\infty$ and compute $u(0.25, 0.05)$. Why is there no decay of the constant mode?

**19.** *(§7.5)* A rod has ends at $0^\circ$ and $100^\circ$ and initial temperature $0^\circ$. Reduce the problem to one with homogeneous boundary conditions, solve it, and compute $u(0.5,0.1)$ and $u(0.75,0.1)$.

**20.** *(§7.6)* For the triangular initial displacement $f(x) = 2x$ on $[0,\tfrac12]$ and $2(1-x)$ on $[\tfrac12,1]$, evaluate the sine coefficients $b_n = 2\int_0^1 f(x)\sin(n\pi x)\,dx$ in closed form and check $n = 1, 3, 5$ numerically.

**21.** *(§7.6)* Solve the string problem with $u(x,0) = 0$ and $u_t(x,0) = \sin 2\pi x$ on $0<x<1$ with fixed ends and $c=1$. Verify the answer by differentiation and evaluate at $(0.25, 0.125)$.

**22.** *(§7.7)* Solve Laplace's equation on the unit square with $u(x,0) = 100$ and $u = 0$ on the other three sides. Use the symmetry to write the series, and compute the centre value. (The answer is an exact integer — explain why.)

**23.** *(§7.7)* Solve Laplace's equation on the unit disc with boundary data $u(1,\theta) = \cos 2\theta$. Evaluate $u(0.5,0)$ and $u(0.7,\pi/3)$, and confirm that the maximum and minimum occur on the boundary.

**24.** *(§7.9)* Expand $f(x) = 1$ on $(0,1)$ in a sine series. Compute the partial sums at $x = 0.5$ with $1, 3, 5$ terms and compare with the exact value. Explain the slow convergence.

**25.** *(§7.9)* Using the square-wave coefficients $b_n = 4/(n\pi)$ for odd $n$, apply Parseval's identity on $(0,\pi)$ and deduce $\sum_{n\ \text{odd}} n^{-2} = \pi^2/8$.

## Advanced

**26.** *(§7.9)* Prove the orthogonality relation $\int_0^L\sin(n\pi x/L)\sin(m\pi x/L)\,dx = \frac L2\delta_{nm}$ for all $n,m \ge 1$, including the case $n = m$.

**27.** *(§7.9)* Assuming the sine series converges uniformly, derive the coefficient formula $b_n = \frac2L\int_0^L f\sin(n\pi x/L)dx$ and prove Bessel's inequality. Give the argument for Parseval's identity.

**28.** *(§7.7)* Prove the weak maximum principle for harmonic functions on a bounded domain, with every hypothesis stated. Where exactly is the hypothesis that $\Omega$ is bounded used?

**29.** *(§7.7)* Use the maximum principle to prove that the Dirichlet problem $\Delta u = 0$ in $\Omega$, $u = h$ on $\partial\Omega$ has at most one solution, and that it depends continuously on $h$ in the supremum norm.

**30.** *(§7.6)* Derive d'Alembert's formula from the general solution $u = F(x-ct)+G(x+ct)$, including the step where the initial velocity is integrated. State the regularity needed.

**31.** *(§7.6)* Prove that the energy $E(t) = \frac12\int_0^L(u_t^2 + c^2u_x^2)\,dx$ of a string with fixed ends is constant in time. Deduce uniqueness of the solution with given data.

**32.** *(§7.8)* Show that the discriminant transforms as $\tilde B^2 - 4\tilde A\tilde C = J^2(B^2 - 4AC)$ under a change of variables with Jacobian $J \ne 0$. Deduce that the type of a second-order equation is invariant.

## Challenge

**33.** *(§7.4)* For the conservation law $u_t + uu_x = 0$ with $u(x,0) = \dfrac{1}{1+x^2}$, find the breaking time $t_b$ exactly and show $t_b = 8\sqrt3/9$. Describe what happens for $t > t_b$.

**34.** *(§7.5)* Using the series solution, prove that for any $t > 0$ the solution of the heat equation on $[0,L]$ with piecewise continuous $f$ is $C^\infty$ in $x$, and that all its derivatives are bounded uniformly in $x$. Explain why the same argument fails at $t = 0$.

**35.** *(§7.9)* For the square wave of half-height $1$, show that the maximum of the $N$-th partial sum tends to $\frac{2}{\pi}\int_0^\pi\frac{\sin t}{t}\,dt \approx 1.17898$, i.e. an overshoot of about $9\%$ of the jump. (You may use that the maximum occurs near $x = \pi/(2N)$ and that $\sum_{k\le N}\frac{\sin(k u)}{k} \to \int_0^{Nu}\frac{\sin t}{t}dt$.)

**36.** *(§7.7)* Derive the Poisson integral formula for the disc from the series solution, and use it to prove the mean value property and to solve the Dirichlet problem with boundary data $h(\theta) = 1 + 2\sin 3\theta + \cos 4\theta$.

## Notes on difficulty

* **Beginner (1–14)** — one idea per problem; the answer should follow directly from a definition or one formula.
* **Intermediate (15–25)** — two or three steps, and a choice of method (characteristics or separation, sine or cosine series, homogeneous or inhomogeneous boundary data).
* **Advanced (26–32)** — complete proofs; every hypothesis must appear in the statement and be used in the proof.
* **Challenge (33–36)** — substantial arguments that combine several sections. These are meant to take an hour or more each.
