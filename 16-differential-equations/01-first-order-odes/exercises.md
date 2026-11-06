# First-Order Differential Equations — Exercises

> [First-Order Differential Equations](README.md) · 34 problems · Beginner → Challenge · Solutions: [solutions.md](solutions.md)

Work through the problems in order; each cites the section of the tutorial it draws on. Problems 1–12
build fluency with the four techniques; 13–22 combine a technique with a modelling or interval
question; 23–30 are proofs and multi-step constructions; 31–34 extend the theory and are marked as
challenge. Attempt every problem before opening [solutions.md](solutions.md), and **substitute your
answer back into the equation** — in this topic that check is decisive.

Conventions: logarithms are natural, $x$ or $t$ denotes the independent variable, and every answer
must include the interval on which the solution is defined whenever the equation has one.

## Beginner

**1.** *(§5.1)* For each equation state the order, whether it is linear, and whether it is autonomous:
(a) $y' + x^{2}y = e^{x}$; (b) $y' = y^{2} - t$; (c) $t\,y' + y = \sin t$; (d) $y'' - y = 0$.

**2.** *(§7.2)* Solve $\dfrac{dy}{dx} = 3x^{2}y$ with $y(0) = 2$.

**3.** *(§7.2)* Solve $\dfrac{dy}{dx} = \dfrac{x}{y}$ with $y(0) = -2$. Why must the solution stay on the lower branch?

**4.** *(§7.2)* Solve $\dfrac{dy}{dx} = e^{x-y}$ with $y(0) = \ln 2$.

**5.** *(§7.2)* Solve $y' = y^{2}\sin x$ with $y(0) = 1$, and state where the solution is defined.

**6.** *(§7.2)* Find **all** solutions of $y' = y^{3}$, including any that the separation loses.

**7.** *(§7.3)* Solve $y' + 2y = 6$ with $y(0) = 1$ and describe the behaviour as $t \to \infty$.

**8.** *(§7.3)* Solve $y' + \dfrac{y}{x} = x$ for $x > 0$.

**9.** *(§7.7)* Find the equilibria of $y' = y(1-y)(2-y)$ and classify each as stable, asymptotically stable or unstable, first from the signs of $f$ and then from $f'$.

**10.** *(§7.1)* For $y' = y - x$: (a) find the isoclines of slope $-1$, $0$ and $1$; (b) verify that $y = x+1$ is a solution; (c) describe where solutions are concave up.

**11.** *(§12.2)* A body at $80\,^{\circ}\mathrm{C}$ cools in a room at $25\,^{\circ}\mathrm{C}$ with $k = 0.02\ \mathrm{min}^{-1}$. Find its temperature after $30$ minutes and the time at which it reaches $35\,^{\circ}\mathrm{C}$.

**12.** *(§12.1)* Carbon-14 has half-life $5730$ years. (a) Find the decay constant. (b) What fraction remains after $2000$ years? (c) How old is a sample with $45\%$ of its original carbon-14?

## Intermediate

**13.** *(§7.2)* Solve $y' = y^{2} - 1$ and identify every solution lost in the separation.

**14.** *(§7.3)* Solve $x y' + 2y = 4x^{2}$ for $x > 0$ with $y(1) = 1$.

**15.** *(§5.2, §7.6)* Solve $y' = y^{2}$ with $y(0) = 2$ and give the maximal interval of definition. What happens as $x$ approaches its right endpoint?

**16.** *(§7.4)* Solve $(2xy + 3x^{2})\,dx + (x^{2} - 2y)\,dy = 0$.

**17.** *(§7.4)* Solve $(3x^{2} + y)\,dx + (x^{2}y - x)\,dy = 0$ by finding an integrating factor that depends on $x$ alone.

**18.** *(§7.5)* Solve $y' + \dfrac{y}{x} = y^{2}$ for $x > 0$.

**19.** *(§7.5)* Solve $y' = \dfrac{y^{2}}{x^{2}} + \dfrac{y}{x}$ for $x > 0$.

**20.** *(§12.4)* A population obeys $P' = 0.8\,P\left(1 - \dfrac{P}{500}\right)$ with $P(0) = 50$ (thousands). Find $P(t)$, the limiting population, and the time at which $P = 250$.

**21.** *(§12.3)* A tank holds $500\ \mathrm{L}$ of water with $0\ \mathrm{kg}$ of salt. Brine containing $0.04\ \mathrm{kg/L}$ flows in at $5\ \mathrm{L/min}$ and the well-mixed solution flows out at the same rate. Find the salt content $S(t)$ and the time at which $S = 10\ \mathrm{kg}$.

**22.** *(§12.5)* A $70\ \mathrm{kg}$ skydiver falls from rest with linear air resistance $k = 20\ \mathrm{kg/s}$ (take $g = 9.8\ \mathrm{m/s^{2}}$). Find $v(t)$, the terminal velocity, and the time to reach $90\%$ of it.

## Advanced

**23.** *(§7.6)* For $y' = 3y^{2/3}$ with $y(0) = 0$, show that for every $c \ge 0$ the function
$$y_c(x) = \begin{cases} 0, & x \le c,\\ (x-c)^{3}, & x \ge c \end{cases}$$
is a solution, and conclude that the initial value problem has infinitely many solutions. Why does this not contradict Picard–Lindelöf?

**24.** *(§7.5)* Solve $y' + y = \sqrt{y}$ with $y(0) = 4$, stating which solutions the substitution can miss.

**25.** *(§7.7)* A population with logistic growth is harvested at the constant rate $h > 0$:
$$y' = ry\left(1 - \frac{y}{K}\right) - h .$$
Find the equilibria as functions of $h$, determine the critical value $h_c$ beyond which no positive equilibrium exists, and classify the equilibria when $0 < h < h_c$.

**26.** *(§7.5)* Solve $y' = \dfrac{1}{x+y}$ by substituting $v = x + y$.

**27.** *(§12.3)* A tank initially holds $100\ \mathrm{L}$ of pure water. Brine with $0.2\ \mathrm{kg/L}$ enters at $3\ \mathrm{L/min}$, and the mixture leaves at $2\ \mathrm{L/min}$. Find $S(t)$ and $\lim_{t\to\infty} S(t)/V(t)$.

**28.** *(§7.6)* Compute the first three Picard iterates for $y' = x + y$, $y(0) = 0$, identify the general iterate, and show that the limit solves the problem on all of $\mathbb{R}$.

**29.** *(§7.7)* Prove that if $f$ is continuously differentiable, $f(y^{*}) = 0$ and $f'(y^{*}) > 0$, then $y^{*}$ is unstable.

**30.** *(§7.4)* Solve $(2y^{2} + 3x)\,dx + 2xy\,dy = 0$ by finding an integrating factor depending on $x$ alone.

## Challenge

**31.** *(§7.5)* The Clairaut equation $y = x y' - (y')^{2}$ is solved by differentiating. Find its general solution and its singular solution, and explain geometrically why the latter is the envelope of the former.

**32.** *(§7.7)* For the harvested logistic equation of problem 25, prove that the number of equilibria changes from two to zero as $h$ passes through $h_c = rK/4$, and describe the behaviour of every solution when $h > h_c$. (This is a fold bifurcation.)

**33.** *(§7.5)* **Riccati reduction.** Suppose $y_1$ solves $y' = q_0(x) + q_1(x)y + q_2(x)y^{2}$ with $q_2 \not\equiv 0$. Show that the substitution $y = y_1 + \dfrac{1}{v}$ gives the linear equation
$$v' + \left(q_1 + 2q_2y_1\right)v = -q_2,$$
and use it with $y_1(x) \equiv 1$ to solve $y' = y^{2} - 1$.

**34.** *(§7.6, §7.7)* (a) Prove the **no-crossing** property: if $f$ is locally Lipschitz, $y_1, y_2$ solve $y' = f(y)$ on a common interval and $y_1(x_0) < y_2(x_0)$ at one point, then $y_1(x) < y_2(x)$ throughout. (b) Deduce that the maximal interval of $y' = y^{2}$ with $y(0) = y_0 > 0$ is $\left(-\infty,\,1/y_0\right)$, and explain why it is bounded on the right but not on the left.
