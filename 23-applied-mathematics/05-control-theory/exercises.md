# Control Theory — Exercises

> [Control Theory](README.md) · 36 problems · Beginner → Challenge · Solutions: [solutions.md](solutions.md)

Work through the problems in order. Each problem states the section of the tutorial where the needed
material is developed. Attempt every problem in writing before opening [solutions.md](solutions.md); the
solutions give complete derivations, not only final answers.

**Conventions.** Continuous time, zero initial conditions unless stated, and negative feedback with unity
sensor gain. "Stable" means asymptotically stable for the zero equilibrium. Matrices are real. A
"second-order system" has characteristic polynomial $s^2+2\zeta\omega_ns+\omega_n^2$.

## Beginner

**1.** *(§7.2)* Write the ODE $\ddot x + 3\dot x + 2x = u$ with output $y=x$ in state-space form using the
phase variables $x_1=x$, $x_2=\dot x$. Give $A$, $B$, $C$ and $D$.

**2.** *(§7.4)* For $A = \begin{bmatrix}0&1\\-2&-3\end{bmatrix}$ compute the eigenvalues and decide whether
the equilibrium is stable.

**3.** *(§7.3)* Solve $\dot x = 2x$ with $x(0)=1$. Is the origin stable?

**4.** *(§7.3)* Compute $e^{At}$ for $A=\operatorname{diag}(-1,-3)$ and the solution with
$x(0)=(1,2)$ and $u=0$.

**5.** *(§7.3)* For $A=\begin{bmatrix}0&1\\-4&0\end{bmatrix}$ compute $e^{At}$ and describe the motion in
the phase plane. Is the origin stable?

**6.** *(§7.5)* Test controllability of $A=\begin{bmatrix}1&0\\0&2\end{bmatrix}$,
$B=\begin{bmatrix}1\\1\end{bmatrix}$.

**7.** *(§7.6)* Test observability of $A=\begin{bmatrix}1&2\\0&3\end{bmatrix}$,
$C=\begin{bmatrix}1&0\end{bmatrix}$.

**8.** *(§7.1, §7.2)* A car of mass $1000\ \mathrm{kg}$ has drag $-50v$ and force input $u$. A proportional
controller $u=450(r-v)$ is used.

(a) Write the closed-loop equation and find its pole.
(b) Compute the steady-state speed for $r=25\ \mathrm{m/s}$ and the steady-state error.

**9.** *(§7.3)* Find the transfer function of $A=-2$, $B=1$, $C=3$, $D=0$.

**10.** *(§7.9)* For $G(s)=1/(s+2)$ in unity feedback, compute the steady-state error to a unit step.

**11.** *(§7.9)* Apply Routh–Hurwitz to $s^3+s^2+2s+8$. Is the polynomial Hurwitz? How many roots lie in
the right half-plane?

**12.** *(§7.7)* For the scalar system $\dot x = x+2u$, find the gain $K$ that places the closed-loop pole
at $-3$ with $u=-Kx$.

**13.** *(§7.10)* For $G(s)=2/(s+1)$ in unity feedback, compute the gain crossover frequency and the phase
margin.

## Intermediate

**14.** *(§7.2, §7.3)* For $\ddot x+2\dot x+5x=3u$ with output $y=x+\dot x$:

(a) Give the state-space matrices.
(b) Compute the transfer function and its poles.
(c) Is the system stable?

**15.** *(§7.3)* Compute $e^{At}$ for $A=\begin{bmatrix}0&1\\-1&-2\end{bmatrix}$. Explain why the answer is
not diagonal times an exponential.

**16.** *(§7.4)* Solve $A^{\mathsf T}P+PA=-I$ for $A=\begin{bmatrix}0&1\\-1&-2\end{bmatrix}$ and verify
$P\succ0$.

**17.** *(§7.7)* For the double integrator $A=\begin{bmatrix}0&1\\0&0\end{bmatrix}$,
$B=\begin{bmatrix}0\\1\end{bmatrix}$, find $K$ placing the closed-loop poles at $-2\pm2j$.

**18.** *(§7.7)* For $A=\begin{bmatrix}0&1\\-6&-5\end{bmatrix}$, $B=\begin{bmatrix}0\\1\end{bmatrix}$, find
$K$ placing the closed-loop poles at $-4$ and $-7$.

**19.** *(§7.8)* For the scalar plant $\dot x=-x+u$ with $Q=4$, $R=1$, solve the Riccati equation, find
$K$, and compute the closed-loop pole.

**20.** *(§7.8)* For the double integrator with $Q=I_2$, $R=1$, solve the Riccati equation, find $K$, and
compute the closed-loop poles.

**21.** *(§7.9)* For $G(s)=1/[(s+1)(s+2)]$ and proportional gain $K_p=8$ in unity feedback:

(a) Compute the steady-state error to a unit step.
(b) What error results if an integral term is added? Explain.

**22.** *(§7.9)* For which values of $K>0$ is $s^3+2s^2+3s+K$ Hurwitz?

**23.** *(§7.2, §7.3)* A DC motor has $J=0.02\ \mathrm{kg\,m^2}$, $b=0.002\ \mathrm{N\,m\,s}$,
$K_t=K_e=0.1$, $R=2\ \Omega$, $L=0.01\ \mathrm{H}$. Take the state $(\omega,i)$ and input the armature
voltage.

(a) Give $A$, $B$, $C$ with $C=[1\ \ 0]$.
(b) Compute the eigenvalues and the DC gain.

**24.** *(§7.10)* For $L(s)=10/[s(s+1)]$, compute the gain crossover, the phase margin and the gain
margin. What is the closed-loop damping ratio?

## Advanced

**25.** *(§7.5)* Prove the necessity of the Kalman rank condition: if
$\operatorname{rank}[B\ AB\ \cdots\ A^{n-1}B]<n$, exhibit a nonzero vector $v$ and a state that cannot be
reached from the origin. State where the Cayley–Hamilton theorem is used.

**26.** *(§7.4)* Prove both directions of the Lyapunov theorem: (a) if $P\succ0$, $Q\succ0$ solve
$A^{\mathsf T}P+PA=-Q$, then $A$ is Hurwitz; (b) if $A$ is Hurwitz and $Q\succ0$, then
$P=\int_0^\infty e^{A^{\mathsf T}t}Qe^{At}dt$ is the unique positive definite solution.

**27.** *(§7.6)* Prove the necessity of the observability rank condition, exhibiting two distinct initial
states that produce the same output for all time.

**28.** *(§7.7)* Suppose $\lambda$ is an eigenvalue of $A$ with a left eigenvector $v$ satisfying
$v^{\mathsf T}B=0$. Show that $\lambda$ is also an eigenvalue of $A-BK$ for every $K$. Deduce that an
unstable uncontrollable mode cannot be moved by state feedback.

**29.** *(§7.8)* Derive the continuous-time algebraic Riccati equation from the Hamilton–Jacobi–Bellman
equation with the ansatz $V(x)=x^{\mathsf T}Px$. Show that the resulting closed loop satisfies
$\dot V<0$ when $Q\succ0$.

**30.** *(§7.9)* Derive the cubic Routh–Hurwitz condition
$a_2a_1>a_3a_0$ (with $a_3,a_2,a_1,a_0>0$) from the Routh array. Apply it to
$s^3+(3+K_d)s^2+(2+K_p)s+K_i$ with $K_p=2$, $K_d=1$ and give the range of $K_i$.

**31.** *(§7.7)* Show that the controllable canonical form

$$A_c=\begin{bmatrix}0&1&0&\cdots&0\\ \vdots&&\ddots&&\vdots\\0&0&\cdots&0&1\\-a_0&-a_1&\cdots&-a_{n-2}&-a_{n-1}\end{bmatrix}, \qquad B_c=\begin{bmatrix}0\\\vdots\\0\\1\end{bmatrix}$$

is controllable for every choice of the coefficients $a_i$.

**32.** *(§7.10)* For $L(s)=K/[s(s+1)]$ in unity feedback:

(a) Find $K>0$ such that the phase margin is exactly $45^\circ$.
(b) Compute the closed-loop damping ratio and compare it with the rule of thumb
$\zeta\approx\mathrm{PM}/100$.

## Challenge

**33.** *(§7.2, §7.7)* A cart of mass $M$ carries a pendulum of mass $m$ and length $l$; a horizontal
force $u$ acts on the cart. Let $x$ be the cart position and $\theta$ the pendulum angle from the upright.

(a) Derive the nonlinear equations, stating the small-angle approximation used for the pendulum torque.
(b) Linearise about the upright equilibrium and give $A$ and $B$ for $M=1\ \mathrm{kg}$,
$m=0.2\ \mathrm{kg}$, $l=0.5\ \mathrm{m}$, $g=9.81\ \mathrm{m/s^2}$.
(c) Test controllability.
(d) Design $K$ placing the closed-loop poles at $-2,-3,-4,-5$.

**34.** *(§7.8)* For the scalar plant $\dot x=ax+bu$ with $Q=q>0$ and $R=r>0$:

(a) Solve the Riccati equation for $P$ and derive $K$.
(b) Show that the closed-loop pole is $a-bK=-\sqrt{a^2+qb^2/r}$.
(c) Show that increasing $q$ always moves the pole further left.
(d) Compute the poles for $a=1$, $b=1$, $r=1$ with $q=1$ and $q=9$.

**35.** *(§7.9)* For $G(s)=1/[(s+1)(s+2)]$ with PID control in unity feedback:

(a) With $K_d=0$, find the exact stability region in the $(K_p,K_i)$ plane.
(b) With $K_d=1$, find the stability region.
(c) Take $K_p=2$, $K_i=10$, $K_d=1$; verify stability and comment on the closed-loop poles.

**36.** *(§7.6, §7.7)* For $A=\begin{bmatrix}0&1\\-2&-3\end{bmatrix}$, $C=\begin{bmatrix}1&0\end{bmatrix}$,
design an observer gain $L$ placing the observer error poles at $-5$ and $-6$. Write the error dynamics,
verify the eigenvalues, and state the separation principle.
