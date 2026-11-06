# Numerical Solutions of ODEs — Exercises

> [Numerical Solutions of ODEs](README.md) · 36 problems · Beginner → Challenge · Solutions: [solutions.md](solutions.md)

Work through the problems in order; each cites the section of the tutorial it draws on. Problems 1–13
are hand computations of a few steps and direct use of the definitions; 14–25 compare methods, analyse
stability, run multistep formulas and set up boundary value problems; 26–32 are proofs; 33–36 are
challenge problems. Attempt every problem before opening [solutions.md](solutions.md), and finish each
one by checking the order of the error or by substituting back into the equation.

Conventions: $f_n = f(t_n,y_n)$; $h$ is the step size and $t_n = t_0+nh$; a method's **order** refers to
the global order unless "local" is stated; $\Delta$ is not used for anything else in this set.

## Beginner

**1.** *(§7.2)* Apply Euler's method to $y' = t - y$, $y(0)=0$, with $h=0.1$ and compute $y_1$ and $y_2$. Compare with the exact solution $y = t-1+e^{-t}$.

**2.** *(§7.2)* Apply Euler's method to $y' = y-t^2+1$, $y(0)=0.5$, with $h=0.1$ and compute three steps. The exact solution at $t=0.3$ is $1.015071$; state the error.

**3.** *(§7.2)* Apply Euler's method to $y'=2y$, $y(0)=1$, with $h=0.25$ and compute four steps. Compare with $e^2$ and explain why the method underestimates.

**4.** *(§7.5)* Apply **implicit** Euler to $y'=-5y$, $y(0)=1$, with $h=0.4$, and compute $y_1$. Compare with $e^{-2}$ and with what explicit Euler would give.

**5.** *(§7.3)* Apply Heun's method to $y'=t-y$, $y(0)=0$, with $h=0.2$ and compute two steps.

**6.** *(§7.3)* Apply the midpoint method to the same problem with $h=0.2$ and compute one step. Why is the answer the same as Heun's for this particular $f$?

**7.** *(§7.2)* For $y'=-2y$, $y(0)=1$, compute the local truncation error of one Euler step with $h=0.1$ from the exact starting value, and compare with the Taylor prediction $\frac h2y''(0)$.

**8.** *(§7.3)* Perform one step of RK4 on $y'=y$, $y(0)=1$, with $h=1$. Compare with $e$ and with the result of one Euler step.

**9.** *(§7.3)* Perform one step of RK4 on $y'=t-y$, $y(0)=0$, with $h=0.2$, listing $k_1,k_2,k_3,k_4$ explicitly.

**10.** *(§7.2)* Apply Euler's method to $y'=y$, $y(0)=1$, with $h=0.1$ for ten steps, and compare with $e$. What is the relative error?

**11.** *(§7.5)* For which $h$ is explicit Euler absolutely stable on $y'=-25y$? What is the corresponding limit for RK4?

**12.** *(§7.5)* A method has stability function $R(z)=1+z$. Identify the method, state its order and its real stability interval, and explain why it cannot integrate $y'=iy$ accurately.

**13.** *(§7.3)* Write the Butcher tableau of Heun's method and verify the two order-2 conditions.

## Intermediate

**14.** *(§7.2, §7.9)* For $y'=-2ty^2$, $y(0)=1$ (exact $y=1/(1+t^2)$), compute the approximations at $t=1$ by Euler, Heun and RK4 with $h=0.2$. Rank them and compute the errors.

**15.** *(§7.4)* Heun's method applied to $y'=-2ty^2$ to $t=1$ gives errors $3.338\times10^{-3}$, $9.186\times10^{-4}$, $2.363\times10^{-4}$, $5.976\times10^{-5}$ for $h=0.2,0.1,0.05,0.025$. Estimate the observed order and compare with the theory.

**16.** *(§7.2)* For $y'=y-t^2+1$, $y(0)=0.5$ on $[0,2]$, the Euler errors at $t=2$ are $0.4397$, $0.2420$, $0.1275$, $0.0655$ for $h=0.2,0.1,0.05,0.025$. Compute the ratios and explain why they approach $2$ slowly.

**17.** *(§7.5)* For $y'=100(\cos t-y)-\sin t$, $y(0)=0$: find the largest $h$ for which explicit Euler is stable, and compute one implicit Euler step with $h=0.1$. Compare with the exact value $0.994959$ at $t=0.1$.

**18.** *(§7.5)* Show that RK4 is **not** A-stable by exhibiting $z$ with $\operatorname{Re}z<0$ and $\lvert R(z)\rvert>1$. Give the numerical value of $R(z)$.

**19.** *(§7.6)* One RK4 step of $h=0.2$ on $y'=y-t^2+1$ from $(0,0.5)$ gives $0.8292933$; two steps of $h=0.1$ give $0.8292983$. Estimate the local error of the fine result and compare with the exact value $0.8292986209$.

**20.** *(§7.7)* With the RK4 value $y_1 = 0.82929333$ at $t=0.2$, perform one AB2 step to $t=0.4$ for $y'=y-t^2+1$ and compare with the exact value $1.21408765$.

**21.** *(§7.7)* Using the starting values $y(0)=0.5$, $y(0.2)=0.82929333$, $y(0.4)=1.21407621$, $y(0.6)=1.64892202$, perform one AB4 step to $t=0.8$ and compare with $2.12722954$.

**22.** *(§7.7)* Continue Problem 21: take the AB4 prediction at $t=0.8$ and apply one AM4 correction. Compare the corrected value with the exact one.

**23.** *(§7.8)* For the boundary value problem $y''=y$, $y(0)=1$, $y(1)=e$, two shooting integrations with RK4 and $h=0.25$ give $u_1(1;0)=1.5430521$ and $u_1(1;1)=2.7182099$. Find the shooting parameter $s$ and state whether more iterations are needed.

**24.** *(§7.8)* Set up the finite-difference system for $y''=y$, $y(0)=1$, $y(1)=e$, with $N=4$, and solve it. Compare with $e^t$ at the interior points.

**25.** *(§7.4)* Prove that Euler's method is consistent: show that the local truncation error tends to zero uniformly as $h\to0$, stating the regularity required of $y$.

## Advanced

**26.** *(§7.3)* Derive the order-2 conditions $b_1+b_2=1$ and $b_2c_2=\frac12$ for a two-stage explicit Runge–Kutta method by matching the Taylor expansion. Show that Heun and midpoint are the two natural choices.

**27.** *(§7.2)* Prove the global error bound for Euler's method: if $f$ is Lipschitz with constant $L$ and $\lvert y''\rvert\le M$, then $\lvert y(t_n)-y_n\rvert \le \frac{M}{2L}\bigl(e^{L(t_n-t_0)}-1\bigr)h$. State and prove the discrete Gronwall lemma used.

**28.** *(§7.7)* Show that AB2 is zero-stable and that the method $y_{n+2}=2y_{n+1}-y_n+hf_n$ is not. What does zero-stability have to do with convergence?

**29.** *(§7.7)* Show that AB2 has order 2 by substituting the Taylor expansion into its formula, and identify its leading error term.

**30.** *(§7.5)* Derive the stability function of the trapezoidal rule and prove that it is A-stable. Explain why $|R(iy)|=1$ for all real $y$ and what this implies numerically.

**31.** *(§7.5)* Prove that no explicit Runge–Kutta method is A-stable. Where exactly is the polynomial nature of $R$ used?

**32.** *(§7.8)* Derive the truncation error of the central-difference approximation to $y''$ and hence show that the finite-difference BVP scheme is second-order accurate.

## Challenge

**33.** *(§7.7)* Derive AB3, $y_{n+1}=y_n+\frac{h}{12}\bigl(23f_n-16f_{n-1}+5f_{n-2}\bigr)$, by integrating the Lagrange interpolant of $f$ on the three nodes $t_n,t_{n-1},t_{n-2}$ over $[t_n,t_{n+1}]$. Verify the weights by checking that the method is exact for $f=1,t,t^2$.

**34.** *(§7.10)* For Euler's method with round-off of size $\varepsilon$ per step, model the total error as $Ch+\varepsilon/h$ and find the optimal step size and the resulting minimal error. Evaluate both for $C=2.6$ and $\varepsilon=10^{-16}$.

**35.** *(§7.3)* Prove that a two-stage explicit Runge–Kutta method cannot have order 3. (This is the first case of the Butcher barrier.)

**36.** *(§7.5)* Analyse the **theta method** $y_{n+1}=y_n+h\bigl[\theta f_{n+1}+(1-\theta)f_n\bigr]$. Find its stability function, its order as a function of $\theta$, and the exact range of $\theta$ for which it is A-stable. Identify the three classical methods it reduces to.

## Notes on difficulty

* **Beginner (1–13)** — one formula, a few arithmetic steps. A calculator is enough.
* **Intermediate (14–25)** — comparisons, tables and setup of systems; each takes 15–30 minutes.
* **Advanced (26–32)** — complete proofs, each requiring a careful Taylor expansion or a compactness argument.
* **Challenge (33–36)** — substantial derivations; Problem 35 needs the order conditions in full.
