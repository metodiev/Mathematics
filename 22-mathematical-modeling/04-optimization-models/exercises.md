# Optimization Models — Exercises

> [Optimization Models](README.md) · 36 problems · Beginner → Challenge · Solutions: [solutions.md](solutions.md)

Work through the problems in order. Each problem can be solved with the definitions, theorems and techniques of the [tutorial](README.md); the section reference tells you where to look. Attempt every problem in writing before consulting [solutions.md](solutions.md).

**Conventions.** All models are maximisations unless an objective is written with $\min$. Money is in euros unless a problem says otherwise. "Solve" means: give the optimal solution, the optimal value, and a certificate or a check. Numerical answers should be given to four significant figures unless an exact value exists.

## Beginner

**1.** *(§7.1, §5.1)* A bakery must decide how many loaves of three kinds of bread to bake before dawn. It has 40 kg of flour, 6 hours of oven time and one baker. Each loaf of white bread uses 0.4 kg of flour and 4 minutes of oven time and sells for €2.40; wholemeal uses 0.5 kg and 5 minutes and sells for €2.80; rye uses 0.6 kg and 6 minutes and sells for €3.10. Unsold loaves are given away.

(a) List the decision variables, with units and time period.
(b) Write the objective.
(c) Write every constraint you can justify, and say which are "$\le$", "$\ge$" or "$=$".
(d) Name one quantity that is *data* rather than a decision, and one hidden assumption of your model.

**2.** *(§9.1)* Solve graphically and by vertex enumeration:

$$
\max\ 40x + 30y \quad\text{s.t.}\quad 2x + y \le 100,\quad x + 2y \le 80,\quad x, y \ge 0 .
$$

Report the vertices, the optimum and the dual solution, and verify $c^{\mathsf{T}}x^\ast = b^{\mathsf{T}}y^\ast$.

**3.** *(§5.2, §7.6)* Put the problem of Exercise 2 into standard form with slack variables. Then:

(a) List the basic solutions obtained by choosing two of the four columns as a basis, and state which are feasible.
(b) Identify the basic optimal solution.
(c) Explain why the optimal basis gives the dual solution directly.

**4.** *(§7.3)* A feed mill blends two ingredients. Ingredient A costs €4/kg and contains 20 % protein; ingredient B costs €6/kg and contains 40 % protein. A 100 kg batch must contain at least 30 % protein.

(a) Formulate the minimum-cost blending problem.
(b) Solve it, and state the optimal protein percentage.
(c) Compute the shadow price of the protein requirement in € per percentage point.

**5.** *(§7.2, §7.13)* Meridian Instruments (the case study of §7.13) has resource matrix $A = \begin{pmatrix}3&3&2\\1&3&1\\4&1&3\end{pmatrix}$, capacities $(340, 240, 320)$ and contributions $(40, 45, 30)$ per unit of products A, B, C.

Evaluate the plan $x = (10, 40, 60)$: compute each resource's usage, each slack, the total contribution, and state which constraints are binding. Is the plan optimal? How can you tell without solving the model?

**6.** *(§7.4)* Three plants have supplies $(20, 30, 50)$ and three warehouses have demands $(25, 25, 40)$.

(a) Show that the transportation problem is not balanced, and write the balanced version.
(b) Construct an initial basic feasible solution with the north-west corner rule.
(c) Explain why this solution is degenerate, and why degeneracy is not an error.

**7.** *(§7.8, §8.6)* A hiker can carry 10 kg. Three items are available:

| Item | Weight | Value |
|---|---|---|
| A | 6 | 7 |
| B | 5 | 6 |
| C | 4 | 5 |

(a) Apply the ratio-greedy rule and give the value it achieves.
(b) Solve the problem exactly by enumerating the eight subsets.
(c) Explain in one sentence why the greedy rule failed.

**8.** *(§7.5)* Three workers and three jobs have cost matrix

$$
C = \begin{pmatrix} 8 & 4 & 7\\ 5 & 9 & 6\\ 7 & 6 & 9\end{pmatrix} .
$$

(a) How many assignments are there?
(b) Find the optimal assignment by enumeration, and state whether it is unique.
(c) Write the assignment problem as a linear program with $0 \le x_{ij} \le 1$ and explain why no integrality constraint is needed.

**9.** *(§7.10)* Classify each function on the stated domain as convex, concave, or neither, and justify with the Hessian or with composition rules.

(a) $f(x) = x^2$ on $\mathbb{R}$; (b) $f(x) = x^3$ on $\mathbb{R}$; (c) $f(x,y) = xy$ on $\mathbb{R}^2$; (d) $f(x) = e^{x}$ on $\mathbb{R}$; (e) $f(x) = \sqrt{x}$ on $(0,\infty)$; (f) $f(x) = -\ln x$ on $(0,\infty)$; (g) $f(x,y) = x^2 y^2$ on $\mathbb{R}^2$.

**10.** *(§7.11)* A plant can be run in five configurations, with annual cost and emissions (both to be minimised):

| Configuration | Cost (k€) | Emissions (t) |
|---|---|---|
| P | 8 | 60 |
| Q | 10 | 50 |
| R | 11 | 45 |
| S | 12 | 40 |
| T | 13 | 40 |

Find the Pareto-optimal configurations, and say which configuration is dominated and by what.

**11.** *(§7.7, §7.13)* For the case study of §7.13 the dual solution is $(7,7,3)$ with machining range $[330, 370.9]$ hours.

(a) Predict the change in contribution if machining capacity rises from 340 to 360 hours.
(b) Predict it if capacity rises to 400 hours, and explain why the prediction may fail.
(c) The true optimum at 400 machining hours is €5236.36. Compute the error of the linear prediction and comment.

**12.** *(§7.12)* For each model, decide whether it is infeasible, unbounded, or has a finite optimum, without solving it. Justify each answer.

(a) $\max\ x \ \text{s.t.}\ x \le 4,\ x \ge 6$.
(b) $\max\ 2x + 3y \ \text{s.t.}\ x + y \le 5,\ x, y \ge 0$.
(c) $\max\ x - y \ \text{s.t.}\ x \ge 0,\ y \ge 0$.
(d) $\min\ x + y \ \text{s.t.}\ x + y \ge 3,\ x \le 1,\ y \le 1$.

## Intermediate

**13.** *(§9.1, §7.7)* Solve

$$
\max\ 5x + 4y \quad\text{s.t.}\quad 2x + y \le 12,\quad x + 2y \le 12,\quad x + y \le 7,\quad x, y \ge 0 .
$$

Report the optimal solution, the optimal value, the dual solution and the slacks. Then compute (a) the range of the first right-hand side over which the same basis is optimal, and (b) the range of the objective coefficient of $x$.

**14.** *(§7.3)* A 100 kg batch is blended from three ingredients with these data:

| Ingredient | Cost €/kg | Nutrient (% of mass) |
|---|---|---|
| 1 | 5 | 90 |
| 2 | 4 | 60 |
| 3 | 3 | 20 |

The batch must contain at least 40 % nutrient.

(a) Formulate and solve the minimum-cost blend.
(b) Compute the shadow price of the nutrient requirement, and its range of validity.
(c) Explain why the cheapest-per-kilogram ingredient is not the one used, and why the most concentrated ingredient is not used either.

**15.** *(§7.4)* Solve the transportation problem with costs

$$
C = \begin{pmatrix} 13 & 5 & 8\\ 6 & 4 & 15\\ 14 & 8 & 4\end{pmatrix},
\qquad s = (15, 20, 45),\qquad d = (20, 25, 35).
$$

Find an optimal plan, verify optimality with potentials, and state whether the optimal plan is unique.

**16.** *(§9.4)* Four workers and four jobs have cost matrix

$$
C = \begin{pmatrix} 3 & 7 & 12 & 7\\ 11 & 5 & 8 & 4\\ 8 & 9 & 3 & 9\\ 9 & 4 & 1 & 1\end{pmatrix} .
$$

(a) Apply the greedy rule (repeatedly take the cheapest remaining pair) and report its cost.
(b) Find the optimal assignment.
(c) Compute the ratio between the greedy cost and the optimum, and explain the mechanism of the failure.

**17.** *(§9.5)* A knapsack has capacity 12 and four items:

| Item | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| Weight | 7 | 6 | 5 | 4 |
| Value | 14 | 11 | 8 | 6 |

(a) Compute the LP relaxation by the ratio rule.
(b) Run branch and bound, branching on $x_1$, and state which node prunes and why.
(c) Report the integer optimum and the integrality gap both absolutely and as a percentage.

**18.** *(§7.8, §8.6)* Two sites can serve three customers. Fixed costs are $f = (50, 40)$; capacities are $(80, 60)$; demands are $d = (25, 30, 20)$; unit delivery costs are

$$
C = \begin{pmatrix} 3 & 6\\ 5 & 4\\ 7 & 5\end{pmatrix}.
$$

(a) Enumerate the feasible sets of open sites and find the integer optimum.
(b) Write both a big-M linking formulation and an aggregate capacity-linking formulation.
(c) By how much could the fixed cost of site 2 rise before the optimal decision changed? What does this break-even value have to do with the shadow price of the fixed-charge decision?

**19.** *(§7.8)* Three jobs must be processed on a single machine. Processing times are $p = (3, 5, 4)$ and release dates are $r = (0, 2, 4)$; the deadline is 14.

(a) Write a mixed-integer formulation with binary sequencing variables $y_{ij}$ and a constant $M$.
(b) Give a valid value of $M$ and justify it.
(c) Find a feasible sequence and its makespan.

**20.** *(§7.10, §9.7)* Consider

$$
\min\ x^2 + 2y^2 \quad\text{s.t.}\quad x + y \ge 3,\quad x, y \ge 0 .
$$

(a) Verify that the problem is convex.
(b) Solve it by KKT conditions, checking each case of active and inactive constraints.
(c) Confirm the answer by a Cauchy–Schwarz argument.

**21.** *(§7.7)* For the problem of Exercise 13 the optimal basis is formed by the first and third constraints, with

$$
B = \begin{pmatrix} 2 & 1\\ 1 & 1\end{pmatrix},\qquad B^{-1} = \begin{pmatrix} 1 & -1\\ -1 & 2\end{pmatrix},\qquad b = \begin{pmatrix} 12\\ 7\end{pmatrix}.
$$

(a) Compute $x_B$ and $y$.
(b) Compute the range of $b_3$ over which this basis stays optimal.
(c) Explain what happens to the optimal value at the ends of the range.

**22.** *(§7.11)* A workshop chooses $x, y \ge 0$ subject to $x + y \le 10$, $x \le 6$, $y \le 6$. Two criteria are maximised: $f_1 = 3x + 2y$ and $f_2 = x + 3y$.

(a) Compute the images of all vertices in the $(f_1,f_2)$ plane, and identify the Pareto front.
(b) Show that every point of the front is optimal for the weight vector $(w_1,w_2) = (2,1)$.
(c) Explain what a solver using weights $(3,1)$ would return, and why that is not the whole answer.

## Advanced

**23.** *(§8.1, §8.2)* Consider the LP $\min\{c^{\mathsf{T}}x : Ax = b,\ x \ge 0\}$ and its dual.

(a) Prove weak duality.
(b) A colleague claims that $x = (6,0)$ is optimal for the problem of Exercise 13, with value $30$. Refute the claim by exhibiting a dual feasible $y$ with $b^{\mathsf{T}}y > 30$, using the dual of that problem.
(c) State precisely what weak duality does and does not prove.

**24.** *(§8.3, §8.4)* Let $v(b) = \min\{c^{\mathsf{T}}x : Ax = b,\ x \ge 0\}$.

(a) Prove that $v$ is convex.
(b) Prove the subgradient inequality $v(b') \ge v(b) + y^{\mathsf{T}}(b'-b)$ for an optimal dual $y$, and deduce that if $y \ge 0$ then raising $b$ cannot lower $v$.
(c) Deduce that for a minimisation the marginal cost $y_i$ is non-decreasing in $b_i$, and explain the economic content.

**25.** *(§8.6)* Prove the Birkhoff–von Neumann theorem in the form needed for the assignment problem: every vertex of the polytope $\{X \in \mathbb{R}^{n\times n} : X \ge 0,\ X\mathbf{1} = \mathbf{1},\ X^{\mathsf{T}}\mathbf{1} = \mathbf{1}\}$ is a permutation matrix.

**26.** *(§8.6)* For the 0–1 knapsack problem:

(a) Prove that the ratio-greedy rule solves the LP relaxation.
(b) Prove that $z_{\mathrm{LP}} \le z_{\mathrm{IP}} + v_{\max}$.
(c) Prove that $\max\{G, v_{\max}\} \ge \tfrac12 z_{\mathrm{IP}}$, where $G$ is the value of the whole-item greedy solution.
(d) Show that the constant $\tfrac12$ cannot be improved by exhibiting an instance and a value of $\varepsilon$.

**27.** *(§8.7)* Prove that the KKT conditions are sufficient for a convex problem, and use the result to show that $x^\ast = (2,1)$ solves Exercise 20 globally.

**28.** *(§8.8)* Let $f_1, f_2$ be minimised over $\mathcal{F}$.

(a) Prove that a minimiser of $w_1f_1 + w_2f_2$ with $w_1, w_2 > 0$ is Pareto optimal.
(b) Prove that if the attainable set is convex, every Pareto-optimal point minimises some weighted sum with $w \ge 0$, $w \ne 0$.
(c) Give a three-point counterexample showing that (b) fails without convexity.

**29.** *(§7.4, §7.6)* For the balanced transportation problem:

(a) Write the dual and interpret $u_i$, $v_j$.
(b) Prove that if all reduced costs $c_{ij} - u_i - v_j$ are non-negative at a feasible plan, the plan is optimal.
(c) Prove that the dual has a one-dimensional family of optimal solutions, and explain the consequence for interpretation.

**30.** *(§7.8, §7.12)* A facility-location model uses the linking constraints $x_{ij} \le M_i y_i$ with a single constant $M_i$ per site.

(a) Derive the smallest valid value of $M_i$ in terms of the data.
(b) Show that using a smaller value can cut off feasible integer solutions, with a two-customer example.
(c) Show that the choice $M_i = \sum_j d_j$ is valid but dominated by $M_i = \min(\mathrm{cap}_i, \max_j d_j)$ in the sense that the resulting LP bound is no worse.

**31.** *(§8.5)* Prove that if a linear program has two distinct optimal solutions then it has infinitely many, and that the optimal set is a face of the feasible polyhedron. Illustrate with $\max\ x + y$ subject to $x + y \le 4$, $x \le 3$, $y \le 3$, $x, y \ge 0$, and describe the optimal set.

## Challenge

**32.** *(§5.1, §8.5)* Construct a linear program in two variables whose optimal set is exactly the segment from $(1,3)$ to $(3,1)$. Verify optimality by exhibiting a dual solution, and prove that no other point is optimal.

**33.** *(§8.6)* Prove: if $P = \{x : Ax \le b\}$ has a vertex $x^\ast$ with a fractional coordinate, then there is an objective $c$ for which the LP optimum is fractional, although the integer optimum is attained at an integral point with strictly worse objective value. Deduce that the LP relaxation is exact for *every* objective if and only if $P$ has only integral vertices.

**34.** *(§7.7, §8.4)* A modeller adds a constraint that is redundant (it is satisfied by every point already feasible) and observes that the optimal value is unchanged but the reported shadow prices change.

(a) Explain how this is possible.
(b) Prove that a redundant constraint can be binding at an optimum.
(c) Construct a two-variable example where the shadow price of a genuine resource constraint is altered by adding a redundant constraint.

**35.** *(§8.8, §7.11)* Let $\mathcal{F}$ be finite and $f = (f_1,f_2)$.

(a) Prove that if the attainable set is convex then every Pareto-optimal point is supported (a minimiser of some weighted sum with $w > 0$).
(b) Give the three configurations $(1,0)$, $(0,1)$, $(0.4,0.4)$ and verify that $(0.4,0.4)$ is Pareto optimal but is not a minimiser of any weighted sum with positive weights.
(c) Explain how the $\varepsilon$-constraint method finds $(0.4,0.4)$.

**36.** *(§7.1, §7.12)* A student formulates a production problem as follows: "maximise $\sum_j p_j x_j$ subject to $\sum_j a_{ij}x_j \le b_i$ for each resource $i$ and $x_j \ge 0$", where $x_j$ is measured in tonnes, $p_j$ in € per tonne, $a_{ij}$ in hours per tonne and $b_i$ in hours per week. The data include a product whose contribution is negative, and a resource with $b_i = 0$.

(a) Identify at least four modelling errors or hidden assumptions.
(b) Rewrite the model to repair them, stating any extra data you need.
(c) Explain what will happen if the model is solved as written, and why the solver's answer will be "correct" and useless.
