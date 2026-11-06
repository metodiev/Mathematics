# Optimization Models — Solutions

> [Optimization Models](README.md) · Solutions to the 36 problems in [exercises.md](exercises.md)

Each solution states the strategy, carries out the significant steps and ends with a check where one is available. Section references point into the [tutorial](README.md).

## Beginner

**1.** *(Strategy: separate decisions from data, then write one sentence per constraint.)*

(a) $x_W, x_M, x_R$ = number of loaves of white, wholemeal and rye baked for the day's sale. They are non-negative integers in reality, but the aggregate model can treat them as continuous and round at the end.

(b) The objective is daily revenue, because no costs are given:

$$
\max\ 2.40\,x_W + 2.80\,x_M + 3.10\,x_R \quad (\text{€ per day}).
$$

(c) Flour, in kg per day: $0.4x_W + 0.5x_M + 0.6x_R \le 40$. Oven, in minutes per day: $4x_W + 5x_M + 6x_R \le 360$ (6 hours). Labour: if one baker works 480 minutes, the oven is the tighter limit; if mixing and shaping take time per loaf, a second constraint $\alpha_W x_W + \alpha_M x_M + \alpha_R x_R \le 480$ is needed, with the $\alpha$'s measured. Demand caps: $x_j \le d_j$, with $d_j$ estimated from sales records — this is a "$\le$", not an "$=$", because unsold bread is given away rather than sold.

(d) The selling prices are data. Hidden assumptions: that every loaf baked is sold at the listed price up to the cap $d_j$, that flour is the only material cost, that resource use per loaf is constant, and that the day is independent of the next (no carry-over of flour or goodwill).

*Comment.* Without demand caps the model bakes until the oven or the flour runs out, which is exactly the unbounded-demand error of §7.2. With caps it is a small LP (or, with whole loaves, an integer program).

**2.** *(Strategy: the optimum of a two-variable LP is at a vertex; enumerate the intersections.)*

The constraints are $2x + y \le 100$, $x + 2y \le 80$, $x, y \ge 0$. Vertices:

| Vertex | Where from | $40x + 30y$ |
|---|---|---|
| $(0,0)$ | axes | $0$ |
| $(50,0)$ | $2x = 100$ | $2000$ |
| $(0,40)$ | $2y = 80$ | $1200$ |
| $(40,20)$ | $2x + y = 100$, $x + 2y = 80$ | $2200$ |

The intersection: subtracting twice the second equation from the first gives $2x + y - 2x - 4y = 100 - 160$, i.e. $-3y = -60$, so $y = 20$ and then $x = (100 - 20)/2 = 40$. The optimum is $x^\ast = (40,20)$ with value $2200$.

Dual: $2y_1 + y_2 \ge 40$ and $y_1 + 2y_2 \ge 30$, both tight at the optimum. Subtracting twice the second from the first: $2y_1 + y_2 - 2y_1 - 4y_2 = 40 - 60$, i.e. $-3y_2 = -20$, so $y_2 = 20/3$ and $y_1 = 30 - 40/3 = 50/3$. Both are non-negative, and

$$
b^{\mathsf{T}}y = 100\cdot\tfrac{50}{3} + 80\cdot\tfrac{20}{3} = \frac{5000 + 1600}{3} = 2200 = c^{\mathsf{T}}x^\ast .
$$

*Check.* By Theorem 8.1 the matching values certify optimality, so no further vertex needs to be examined.

**3.** *(Strategy: add one slack per inequality; a basis is a choice of two columns.)*

$$
\max\ 40x + 30y \quad\text{s.t.}\quad 2x + y + s_1 = 100,\quad x + 2y + s_2 = 80,\quad x, y, s_1, s_2 \ge 0 .
$$

(a) The six bases, with $B$ the selected columns:

| Basis | Solution | Feasible? |
|---|---|---|
| $\{x,y\}$ | $x = 40$, $y = 20$, $s = 0$ | yes |
| $\{x,s_1\}$ | $x = 80$, $s_1 = -60$ | no |
| $\{x,s_2\}$ | $x = 50$, $s_2 = 30$, $s_1 = 0$ | yes |
| $\{y,s_1\}$ | $y = 40$, $s_1 = 60$, $s_2 = 0$ | yes |
| $\{y,s_2\}$ | $y = 100$, $s_2 = -120$ | no |
| $\{s_1,s_2\}$ | $s = (100, 80)$, $x = y = 0$ | yes |

The feasible basic solutions are exactly the four vertices of Exercise 2.

(b) Evaluating gives $(40,20)$ with value $2200$ as the best basic feasible solution, hence the optimum (Theorem 8.6).

(c) The dual solution is read off as $y = c_B^{\mathsf{T}}B^{-1}$, and the reduced cost of slack $i$ is exactly $y_i$: a slack variable represents "not using resource $i$", so its opportunity cost is the price of the resource. Here $B^{-1} = \frac13\begin{pmatrix}2&-1\\-1&2\end{pmatrix}$ and $y = \frac13(40,30)\begin{pmatrix}2&-1\\-1&2\end{pmatrix} = \frac13(80-30,\ -40+60) = (50/3, 20/3)$ ✓.

**4.** *(Strategy: one equality for the batch, one inequality for quality.)*

(a) With $A, B$ in kg,

$$
\min\ 4A + 6B \quad\text{s.t.}\quad A + B = 100,\quad 0.2A + 0.4B \ge 30,\quad A, B \ge 0 .
$$

(b) Substitute $B = 100 - A$: the quality constraint becomes $0.2A + 40 - 0.4A \ge 30$, i.e. $0.2A \le 10$, i.e. $A \le 50$. The cost is $4A + 6(100 - A) = 600 - 2A$, decreasing in $A$, so $A = 50$, $B = 50$ and the cost is $€500$. The protein percentage is $0.2(50) + 0.4(50) = 30\,\%$, exactly on the specification.

(c) Raise the requirement to $30 + \delta$ percent: then $0.2A + 0.4(100 - A) \ge 30 + \delta$ gives $A \le 50 - 5\delta$ and the cost is $600 - 2(50 - 5\delta) = 500 + 10\delta$. The shadow price is €10 per percentage point per 100 kg batch, i.e. €0.10 per kg per percentage point.

*Check.* At $\delta = 2$: $A = 40$, $B = 60$, cost $160 + 360 = €520 = 500 + 20$ ✓.

**5.** *(Strategy: evaluate the plan against each constraint; a plan with all slacks positive cannot be optimal.)*

$$
Ax = \begin{pmatrix}3&3&2\\1&3&1\\4&1&3\end{pmatrix}\begin{pmatrix}10\\40\\60\end{pmatrix} = \begin{pmatrix}270\\190\\260\end{pmatrix},
\qquad
s = b - Ax = \begin{pmatrix}70\\50\\60\end{pmatrix}.
$$

All three slacks are positive, so no resource is exhausted. The contribution is $40(10) + 45(40) + 30(60) = 400 + 1800 + 1800 = €4000$.

The plan is **not** optimal: because every constraint is slack at $x$, the point $(1+\varepsilon)x$ is feasible for small $\varepsilon > 0$ and earns $(1+\varepsilon)4000$. The largest feasible $\varepsilon$ is $\min\{340/270,\ 240/190,\ 320/260\} = 320/260 = 1.2308$, giving $x = (12.31, 49.23, 73.85)$ and a contribution of $€4923.08$.

*Check.* At that point testing is exactly saturated: $4(12.31) + 49.23 + 3(73.85) = 49.23 + 49.23 + 221.54 = 320$ ✓. The lesson: a solution with all slacks positive is never optimal for a maximisation with positive objective coefficients.

**6.** *(Strategy: balance first, then fill from the north-west.)*

(a) Total supply $20 + 30 + 50 = 100$; total demand $25 + 25 + 40 = 90$. Supply exceeds demand by $10$, so add a dummy warehouse with demand $10$ and zero shipping cost. The balanced problem has $m + n - 1 = 3 + 4 - 1 = 6$ basic variables.

(b) North-west corner: give W1 as much as possible from P1, $x_{11} = 20$ (P1 exhausted). W1 still needs $5$, so $x_{21} = 5$ (W1 satisfied). W2 needs $25$, all from P2: $x_{22} = 25$ (P2 exhausted, $5 + 25 = 30$). W3 needs $40$, all from P3: $x_{33} = 40$; the dummy needs $10$, also from P3: $x_{34} = 10$ (P3: $40 + 10 = 50$ ✓). The degenerate cell $x_{32} = 0$ completes the basis of six.

(c) The solution has only five positive entries but six basic variables, so one basic variable is zero: it is **degenerate**. Degeneracy means the basis is not uniquely determined — a small amount of flow can be moved around the cycle (P3,W2)–(P3,W3)–(P2,W3)–(P2,W2) without changing any row or column sum. It is not an error; it only complicates the bookkeeping of the transportation simplex (a zero step length in a pivot).

**7.** *(Strategy: greedy, then exact enumeration.)*

(a) Ratios: A $7/6 \approx 1.167$, B $6/5 = 1.2$, C $5/4 = 1.25$. Take C (weight 4, value 5), then B (weight 5; total 9; value 6; total 11); A needs 6 and only 1 kg remains. Greedy value $= 11$.

(b) The eight subsets, with infeasible ones struck out: $\varnothing \to 0$; $\{A\} \to 7$; $\{B\} \to 6$; $\{C\} \to 5$; $\{A,B\} \to$ weight $11 > 10$; $\{A,C\} \to$ weight $10$, value $12$; $\{B,C\} \to$ weight $9$, value $11$; $\{A,B,C\} \to$ weight $15 > 10$. The optimum is $\{A,C\}$ with value $12$.

(c) C has the highest ratio, so greedy takes C first (4 kg, 5). With 6 kg left it takes B (5 kg, ratio 1.2) rather than A (6 kg, ratio 1.167), leaving 1 kg unused. Taking A together with C would fill the bag exactly. Ratios compare value per kilogram, but they say nothing about whether the *residual* capacity can be filled — the integrality of what is left over.

*Check.* $12 > 11$ ✓, and no feasible subset exceeds 12 by the enumeration ✓.

**8.** *(Strategy: there are only $3! = 6$ assignments, so enumerate.)*

(a) $3! = 6$.

(b) The six costs: $(j_1,j_2,j_3)$ orderings — $(1,2,3)$: $8 + 9 + 9 = 26$; $(1,3,2)$: $8 + 6 + 6 = 20$; $(2,1,3)$: $4 + 5 + 9 = 18$; $(2,3,1)$: $4 + 6 + 7 = 17$; $(3,1,2)$: $7 + 5 + 6 = 18$; $(3,2,1)$: $7 + 9 + 7 = 23$. The minimum is $17$, attained only by worker 1→job 2, worker 2→job 3, worker 3→job 1.

(c) With $x_{ij} \in [0,1]$ and the row and column sums equal to $1$, the constraint matrix is the incidence matrix of a bipartite graph, which is totally unimodular; equivalently, by Birkhoff–von Neumann every doubly stochastic matrix is a convex combination of permutation matrices, so every vertex is a permutation matrix. A fractional relaxation therefore has an integral optimum, and $x_{ij} \in \{0,1\}$ can be dropped.

**9.** *(Strategy: second derivatives in one variable, Hessians in several.)*

(a) $f'' = 2 > 0$: convex.
(b) $f'' = 6x$ changes sign: neither.
(c) Hessian $\begin{pmatrix}0&1\\1&0\end{pmatrix}$ has eigenvalues $\pm 1$: neither.
(d) $f'' = e^x > 0$: convex.
(e) $f'' = -\tfrac14 x^{-3/2} < 0$ on $x > 0$: concave.
(f) $f'' = 1/x^2 > 0$: convex.
(g) $f(x,y) = x^2y^2$: Hessian $\begin{pmatrix}2y^2 & 4xy\\ 4xy & 2x^2\end{pmatrix}$ with determinant $4x^2y^2 - 16x^2y^2 = -12x^2y^2 < 0$ whenever $xy \ne 0$, so the Hessian is indefinite and $f$ is neither convex nor concave. (On the axes it is only positive semidefinite, which is not enough.)

*Comment.* Part (g) matters in practice: it is exactly the kind of term that appears when a model multiplies two decision variables, and it destroys convexity even though each variable enters quadratically.

**10.** *(Strategy: eliminate anything dominated.)*

Comparing S $(12,40)$ with T $(13,40)$: same emissions, higher cost, so T is dominated by S. Checking the rest: P $(8,60)$ has the lowest cost; Q $(10,50)$ improves emissions by 10 for 2 k€; R $(11,45)$ improves by 5 for 1 k€; S $(12,40)$ improves by 5 for 1 k€. No other pair dominates. The Pareto front is $\{P, Q, R, S\}$.

*Comment.* The marginal cost of emissions abatement rises: €0.2k per tonne from P to Q, €0.2k per tonne from Q to R, €0.2k per tonne from R to S — actually constant here, which is why all four points are on a straight line in objective space. With a constant trade-off the choice between them is entirely a value judgement, and the weighted-sum method will return whichever endpoint the weights favour.

**11.** *(Strategy: a shadow price is a derivative — valid only inside its range.)*

(a) $20$ hours lie inside $[330, 370.9]$, so the linear prediction applies: $€5020 + 20 \times 7 = €5160$.

(b) $400 > 370.9$, so the basis changes; the price of €7 no longer applies. For a maximisation the value function is concave in capacity, so marginal values *decrease* as capacity grows, and the true increase will be smaller than $60 \times 7 = 420$.

(c) The true value is $€5236.36$, so the linear prediction of $€5440$ overstates it by $203.64$, i.e. $3.9\%$. At $400$ hours the optimal duals are $(0, 12.73, 6.82)$: machining has become free at the margin (it is no longer fully used at the new optimum, where $x = (65.45, 58.18, 0)$) while assembly and testing have become more valuable.

*Moral.* Quoting a shadow price without its range is not a rounding error; it is a different model's answer.

**12.** *(Strategy: look for a contradiction or for a feasible direction of unlimited improvement.)*

(a) **Infeasible**: $x \le 4$ and $x \ge 6$ cannot both hold.

(b) **Finite optimum**: the region is a bounded triangle with vertices $(0,0)$, $(5,0)$, $(0,5)$; the best is $(0,5)$ with value $15$.

(c) **Unbounded**: set $y = 0$ and let $x \to \infty$; every constraint stays satisfied and the objective grows without limit. There is no missing constraint in the formal sense, but the model is missing a capacity on $x$ — the economic defect.

(d) **Infeasible**: $x + y \ge 3$ while $x \le 1$ and $y \le 1$ give $x + y \le 2$.

*Comment.* In (c) the recession direction is $d = (1,0)$, which satisfies $Ad \le 0$ and $c^{\mathsf{T}}d = 1 > 0$; in (a) and (d) the infeasibility is visible as an inconsistent pair of bounds.

## Intermediate

**13.** *(Strategy: vertices, then duality, then the basis inverse.)*

The three constraints are $2x + y \le 12$ (1), $x + 2y \le 12$ (2), $x + y \le 7$ (3), with $x, y \ge 0$. Vertices: $(0,0)$; $(6,0)$ from (1); $(0,6)$ from (2); (1)∩(3): $y = 12 - 2x$ and $x + y = 7$ give $x = 5$, $y = 2$; (2)∩(3): $x = 2$, $y = 5$; (1)∩(2): $x = 4$, $y = 4$ but $x + y = 8 > 7$, infeasible.

Values: $5(6) = 30$; $4(6) = 24$; $5(5) + 4(2) = 33$; $5(2) + 4(5) = 30$. The optimum is $(5,2)$ with value $33$; slacks are $s_1 = 0$, $s_2 = 12 - 9 = 3$, $s_3 = 0$.

Dual: $2y_1 + y_2 + y_3 \ge 5$, $y_1 + 2y_2 + y_3 \ge 4$, $y \ge 0$. Since $s_2 > 0$, complementary slackness forces $y_2 = 0$. Then $2y_1 + y_3 = 5$ and $y_1 + y_3 = 4$, so $y_1 = 1$, $y_3 = 3$. Check: $b^{\mathsf{T}}y = 12 + 0 + 21 = 33$ ✓.

(a) **Range of $b_1$.** With $B$ the columns of (1) and (3), $x_B = B^{-1}(b_1, b_3)$ where $B = \begin{pmatrix}2&1\\1&1\end{pmatrix}$, $B^{-1} = \begin{pmatrix}1&-1\\-1&2\end{pmatrix}$. So $x = (b_1 - 7,\ -b_1 + 14)$, which is non-negative for $7 \le b_1 \le 14$. The third requirement is that constraint (2) stays satisfied: $x + 2y = (b_1 - 7) + 2(14 - b_1) = 21 - b_1 \le 12$, i.e. $b_1 \ge 9$. Hence $b_1 \in [9, 14]$.

(b) **Range of $c_x$.** With $c_y = 4$ fixed, $y = (c_x - 4,\ 0,\ -c_x + 8)$, so $y \ge 0$ requires $4 \le c_x \le 8$.

*Check.* At $b_1 = 14$ the plan is $(7,0)$ with value $35 = 33 + 2(7)$ ✓ — the two extra hours are worth $2 \times 1$ each. At $c_x = 8$ the value would be $8(5) + 4(2) = 48$, and indeed the dual gives $12(4) + 0 + 7(0) = 48$ ✓.

**14.** *(Strategy: express everything relative to the cheapest ingredient.)*

(a) With $x_i$ in kg,

$$
\min\ 5x_1 + 4x_2 + 3x_3 \quad\text{s.t.}\quad x_1 + x_2 + x_3 = 100,\quad 0.9x_1 + 0.6x_2 + 0.2x_3 \ge 40,\quad x \ge 0 .
$$

Substituting $x_3 = 100 - x_1 - x_2$:

$$
\text{cost} = 300 + 2x_1 + x_2, \qquad \text{nutrient excess} = 0.7x_1 + 0.4x_2 \ge 20 .
$$

Each unit of $x_1$ buys $0.7$ nutrient for €2 (€2.857 per nutrient unit); each unit of $x_2$ buys $0.4$ for €1 (€2.50 per nutrient unit). Ingredient 2 is cheaper per unit of nutrient, so use it: $x_2 = 20/0.4 = 50$, $x_1 = 0$, $x_3 = 50$. Cost $= 4(50) + 3(50) = €350$.

(b) Perturb the requirement to $40 + \delta$: $x_2 = (20 + \delta)/0.4 = 50 + 2.5\delta$, so the cost is $350 + 2.5\delta$. The shadow price is €2.50 per percentage point per 100 kg. It is valid while $x_2 \le 100$, i.e. $\delta \le 20$, and while $x_2 \ge 0$, i.e. $\delta \ge -20$: so for a requirement in $[20\,\%, 60\,\%]$. Above $60\,\%$ the blend must also use ingredient 1, and each further point costs $€3.33$ (one unit of $x_2$ replaced by $x_1$ gains $0.3$ nutrient for €1).

(c) Ingredient 3 is the cheapest per kg but contributes the least nutrient, so it is the filler. Ingredient 1 is the most concentrated but its *extra* cost over the filler per extra nutrient unit, $(5-3)/0.7 = €2.857$, exceeds that of ingredient 2, $(4-3)/0.4 = €2.50$. The right comparison is always net of the displaced alternative, not price per kilogram and not concentration.

*Check.* At $\delta = 10$: $x_2 = 75$, $x_3 = 25$; nutrient $= 0.6(75) + 0.2(25) = 45 + 5 = 50\,\%$ ✓; cost $= 300 + 75 = 375 = 350 + 25$ ✓.

**15.** *(Strategy: propose a plan from the cheapest routes, then certify it with potentials.)*

Proposed plan: $x_{12} = 15$, $x_{21} = 20$, $x_{32} = 10$, $x_{33} = 35$, all other flows zero. Row sums: $15$, $20$, $10 + 35 = 45$ ✓. Column sums: $20$, $15 + 10 = 25$, $35$ ✓. Cost:

$$
5(15) + 6(20) + 8(10) + 4(35) = 75 + 120 + 80 + 140 = 415 .
$$

Potentials: these four cells plus the zero cell $(2,2)$ form a spanning tree. Set $u_1 = 0$. From $(1,2)$: $v_2 = 5$. From $(3,2)$: $u_3 = 3$. From $(3,3)$: $v_3 = 4 - 3 = 1$. From $(2,1)$: $u_2 = 6 - v_1$; and from the zero basic cell $(2,2)$: $u_2 = 4 - 5 = -1$, hence $v_1 = 7$.

Reduced costs of the non-basic cells: $(1,1)$: $13 - (0 + 7) = 6$; $(1,3)$: $8 - (0+1) = 7$; $(2,3)$: $15 - (-1 + 1) = 15$. All are positive, so by complementary slackness the plan is optimal. The dual value is $15(0) + 20(-1) + 45(3) + 20(7) + 25(5) + 35(1) = -20 + 135 + 140 + 125 + 35 = 415$ ✓.

**Not unique.** The zero basic cell $(2,2)$ has reduced cost $0$, so a perturbation that sends flow around the cycle $(2,1)$–$(2,2)$–$(3,2)$–$(3,1)$ changes no cost: there is a second optimal plan. The optimal *value* is unique; the plan is not.

*Comment.* The negative potential $u_2 = -1$ is not a pathology: in a transportation model the individual potentials are determined only up to an additive constant (§7.4), so only the sums $u_i + v_j$ and the reduced costs carry meaning.

**16.** *(Strategy: run greedy, then compare with a structured alternative.)*

(a) Greedy: the cheapest pair overall is $(4,3)$ at cost $1$, then $(4,4)$ is unavailable, so the cheapest remaining is $(1,1)$ at $3$, then $(2,4)$ at $4$, then $(3,2)$ at $9$. Total $1 + 3 + 4 + 9 = 17$.

(b) The diagonal assignment — worker $i$ to job $i$ — costs $3 + 5 + 3 + 1 = 12$, which beats $17$. Enumerating all $24$ permutations confirms that $12$ is minimal.

(c) The ratio is $17/12 \approx 1.417$: greedy costs $41.7\,\%$ more. The mechanism: greedy spends its cheapest pair $(4,3) = 1$ on worker 4, which then cannot take job 4 at cost $1$; the true cost of that choice is $1 + 9 - (1 + 1) = 8$ relative to the diagonal, because job 2 must be covered by the expensive worker 3.

*Check.* $12$ is achieved by a permutation, and no permutation is cheaper by the enumeration ✓.

**17.** *(Strategy: ratio LP, then branch on the variable that is fixed at 1 to split the problem.)*

(a) Ratios: $14/7 = 2$, $11/6 \approx 1.833$, $8/5 = 1.6$, $6/4 = 1.5$. The LP takes item 1 (weight 7, value 14), then item 2 partially: capacity 5 remains and the item weighs 6, so $x_2 = 5/6$. Thus

$$
z_{\mathrm{LP}} = 14 + \tfrac56(11) = 14 + 9.1667 = 23.1667 .
$$

(b) **Branch $x_1 = 0$.** Items 2, 3, 4 with capacity 12: the LP takes item 2 (6), item 3 (5) — total 11 — and a quarter of item 4, giving $11 + 8 + 1.5 = 20.5$. Its best integer point is $\{2,3\}$ with value $19$.

**Branch $x_1 = 1$.** Capacity 5 remains; item 2 (weight 6) cannot fit, so branch on $x_2$: $x_2 = 0$ leaves capacity 5, which item 3 fills exactly, giving $14 + 8 = 22$; this is integral, so it becomes the incumbent. ($x_2 = 1$ is infeasible: weight $13 > 12$.)

Now the node $x_1 = 0$ has bound $20.5 < 22$, so it is pruned by bound. The optimum is $22$, from items 1 and 3 (weight $7 + 5 = 12$).

(c) The integrality gap is $23.1667 - 22 = 1.1667$, i.e. $5.3\,\%$ of the optimum. Note that the root bound alone cannot certify $22$; branching is what closes the gap.

*Check.* Enumerating the 16 subsets: $\{1,3\}$ has weight 12 and value 22; $\{1,4\}$ is 20; $\{2,3\}$ is 19; $\{2,4\}$ is 17; $\{1,2\}$ is infeasible ($13$); $\{3,4\}$ is 14; every three-item set exceeds the capacity except $\{2,3,4\}$? — weight $6+5+4 = 15 > 12$, infeasible. So 22 is maximal ✓.

**18.** *(Strategy: enumerate open sets; only three are feasible.)*

(a) Capacities: site 1 has 80, site 2 has 60, total demand 75. So $\{2\}$ alone is infeasible (60 < 75), while $\{1\}$ and $\{1,2\}$ are feasible.

| Open sites | Fixed | Delivery | Total |
|---|---|---|---|
| $\{1\}$ | 50 | $3(25) + 5(30) + 7(20) = 365$ | 415 |
| $\{2\}$ | — | capacity insufficient | infeasible |
| $\{1,2\}$ | 90 | $3(25) + 4(30) + 5(20) = 295$ | 385 |

The optimum is $\{1,2\}$ at $385$: customer 1 from site 1, customers 2 and 3 from site 2 (site 2 loads $50$ of its $60$).

(b) **Big-M linking:** with $x_{ij} \ge 0$ and $y_i \in \{0,1\}$,

$$
\min\ \sum_i f_iy_i + \sum_{i,j} c_{ij}x_{ij}
\quad\text{s.t.}\quad
\sum_i x_{ij} = d_j,\ \
x_{ij} \le \min(\mathrm{cap}_i, d_j)\, y_i,\ \
\sum_j x_{ij} \le \mathrm{cap}_i .
$$

**Aggregate linking:** replace the per-link rows by $\sum_j x_{ij} \le \mathrm{cap}_i y_i$ and keep the demand rows; the separate capacity row is then implied.

(c) Opening site 2 costs $40$ and saves $365 - 295 = 70$ in delivery, so it is worth $30$ net. The break-even fixed cost is therefore $f_2 = 70$: above that, site 2 stays closed. Equivalently, the fixed-charge decision has a "shadow price" of $30$ — the most the firm would pay for the right to open site 2, given the rest of the network.

*Check.* $90 + 295 = 385 < 415$ ✓, and at $f_2 = 70$ the two plans tie at $415$ ✓.

**19.** *(Strategy: a disjunction per pair, with a horizon-based big-M.)*

(a) Variables: start times $t_j \ge 0$ and $y_{ij} \in \{0,1\}$ for $i < j$, with $y_{ij} = 1$ meaning job $i$ precedes job $j$.

$$
\begin{aligned}
t_j &\ge r_j && \text{for each } j,\\
t_j &\ge t_i + p_i - M(1 - y_{ij}) && \text{for each } i \ne j,\\
t_i &\ge t_j + p_j - M y_{ij} && \text{for each } i \ne j,\\
t_j + p_j &\le 14 && \text{for each } j .
\end{aligned}
$$

For each ordered pair only one of the two disjunctive constraints is active; the other is relaxed by $M$.

(b) A valid $M$ follows from the deadline: every job finishes by 14 and starts at or after 0, so $t_i + p_i - t_j \le 14 - 0 = 14$ for any pair. Hence $M = 14$ is valid (any larger value is also valid but weaker, because a larger $M$ relaxes the disjunction more). The essential point is that $M$ must be *derived* from the horizon: a value chosen for convenience can forbid feasible schedules.

(c) Sequence 1, 2, 3: $t_1 = 0$ (release 0), job 1 finishes at $3 \ge r_2 = 2$, so $t_2 = 3$; job 2 finishes at $8 \ge r_3 = 4$, so $t_3 = 8$; job 3 finishes at $12 \le 14$ ✓. Makespan $12$.

*Check.* $p_1 + p_2 + p_3 = 12$, so no schedule can finish before $12$; the sequence is optimal in makespan as well as feasible.

**20.** *(Strategy: convex, so KKT is sufficient; try the interior case first.)*

(a) The Hessian of $f(x,y) = x^2 + 2y^2$ is $\begin{pmatrix}2&0\\0&4\end{pmatrix} \succ 0$, so $f$ is strictly convex; the constraint $x + y \ge 3$ is linear, so the feasible set is convex. Hence any KKT point is a global minimum.

(b) Write the constraint as $3 - x - y \le 0$ with multiplier $\lambda \ge 0$ and the non-negativity constraints with $\mu_x, \mu_y \ge 0$. Stationarity: $2x - \lambda - \mu_x = 0$, $4y - \lambda - \mu_y = 0$. Suppose $x, y > 0$, so $\mu = 0$: then $2x = \lambda = 4y$, so $x = 2y$; with the constraint active, $3y = 3$, hence $y = 1$, $x = 2$, $\lambda = 4 > 0$. This is KKT, hence optimal, with value $4 + 2 = 6$.

Checking the alternatives confirms uniqueness: with $x = 0$, the minimum of $2y^2$ subject to $y \ge 3$ is $18$; with $y = 0$, the minimum of $x^2$ subject to $x \ge 3$ is $9$; both exceed $6$.

(c) By Cauchy–Schwarz, $(x + y)^2 \le (x^2 + 2y^2)(1 + \tfrac12)$, so $x^2 + 2y^2 \ge \frac{2}{3}(x+y)^2 \ge \frac{2}{3}(9) = 6$, with equality when $(x, y)$ is proportional to $(1, \tfrac12)$, i.e. $x = 2y$, together with $x + y = 3$ — the same point ✓.

**21.** *(Strategy: the basis inverse gives everything.)*

(a) $x_B = B^{-1}b = \begin{pmatrix}1&-1\\-1&2\end{pmatrix}\begin{pmatrix}12\\7\end{pmatrix} = \begin{pmatrix}5\\2\end{pmatrix}$ ✓. The dual is $y = c_B^{\mathsf{T}}B^{-1} = (5, 4)\begin{pmatrix}1&-1\\-1&2\end{pmatrix} = (1, 3)$, with $y_2 = 0$ for the slack second constraint.

(b) Write $b_3 = 7 + \Delta$. Then $x_B = (12 - b_3,\ -12 + 2b_3) = (5 - \Delta,\ 2 + 2\Delta)$, non-negative for $-1 \le \Delta \le 5$. The second constraint must stay satisfied: $x + 2y = (5 - \Delta) + 2(2 + 2\Delta) = 9 + 3\Delta \le 12$, i.e. $\Delta \le 1$. So the basis stays optimal for $b_3 \in [6, 8]$.

(c) At $b_3 = 8$ the second constraint becomes tight as well and the basis becomes degenerate; beyond it, a different basis is optimal and the value grows at a different rate. At $b_3 = 6$ the plan is $(6,0)$ and the basis is still optimal but degenerate.

*Check.* At $b_3 = 8$: $x = (4,4)$, value $20 + 16 = 36$, and the dual gives $12(2) + 12(1) + 8(0) = 36$ ✓ — the duals have changed from $(1,0,3)$ to $(2,1,0)$, which is exactly the kink.

**22.** *(Strategy: map the vertices into objective space, then look for the north-east boundary.)*

(a) Vertices of the feasible hexagon and their images:

| $(x,y)$ | $f_1 = 3x + 2y$ | $f_2 = x + 3y$ |
|---|---|---|
| $(0,0)$ | 0 | 0 |
| $(6,0)$ | 18 | 6 |
| $(6,4)$ | 26 | 18 |
| $(4,6)$ | 24 | 22 |
| $(0,6)$ | 12 | 18 |

$(6,0)$ is dominated by $(6,4)$, and $(0,6)$ is dominated by $(4,6)$. The Pareto front is the segment joining $(26,18)$ and $(24,22)$: all its points are attainable, since averaging the plans $(6,4)$ and $(4,6)$ gives $(6-2t, 4+2t)$ with images $(26-2t, 18+4t)$, which is exactly that segment.

(b) With $w = (2,1)$, $2f_1 + f_2 = 2(3x+2y) + (x+3y) = 7x + 7y$, which is constant on the line $x + y = 10$. Every feasible point with $x + y = 10$ therefore attains the maximum $70$, i.e. the whole front is optimal for this weight vector.

(c) With weights $(3,1)$ the objective is $10x + 9y$, maximised at $(6,4)$: the solver returns $(26,18)$. That is correct for those weights but it is only one endpoint of the front; the choice between $(26,18)$ and $(24,22)$ — an extra 4 units of $f_2$ for 2 units of $f_1$ — is a value judgement that the weights have already made implicitly.

## Advanced

**23.** *(Strategy: weak duality is a two-line inequality; use it as a refutation tool.)*

(a) For feasible $x$ and $y$, with $x \ge 0$ and $c - A^{\mathsf{T}}y \ge 0$,

$$
c^{\mathsf{T}}x = (c - A^{\mathsf{T}}y)^{\mathsf{T}}x + y^{\mathsf{T}}Ax \ge y^{\mathsf{T}}Ax = y^{\mathsf{T}}b . \qquad \blacksquare
$$

(b) The claim is that $x = (6,0)$ is optimal with value $30$. It is feasible: $2(6) + 0 = 12 \le 12$, $6 + 0 = 6 \le 12$, $6 \le 7$. Take $y = (1, 0, 3)$, which is dual feasible because $2(1) + 0 + 3 = 5 \ge 5$ and $1 + 0 + 3 = 4 \ge 4$. Then $b^{\mathsf{T}}y = 12 + 0 + 21 = 33 > 30$, so by weak duality $x$ cannot be optimal. (In fact $(5,2)$ attains $33$.)

(c) Weak duality proves that *no* feasible primal can beat any feasible dual; hence a dual point is a certificate of an upper bound (for a maximisation), and a matched pair certifies optimality. It does **not** prove that a primal point is optimal unless a matching dual is exhibited, it does not by itself guarantee that the bound is attained, and it has no analogue for integer programs — the LP bound may be attained only fractionally.

**24.** *(Strategy: average two optimal solutions; then use the dual.)*

(a) Let $b^1, b^2$ have optimal solutions $x^1, x^2$ and let $\lambda \in [0,1]$. Then $x = \lambda x^1 + (1-\lambda)x^2 \ge 0$ and $Ax = \lambda b^1 + (1-\lambda)b^2$, so $x$ is feasible for the averaged right-hand side and

$$
v(\lambda b^1 + (1-\lambda)b^2) \le c^{\mathsf{T}}x = \lambda v(b^1) + (1-\lambda)v(b^2).
$$

(b) Let $y$ be optimal for the dual at $b$ and let $x'$ be feasible for $b'$. Then $v(b') = c^{\mathsf{T}}x' \ge y^{\mathsf{T}}Ax' = y^{\mathsf{T}}b' = v(b) + y^{\mathsf{T}}(b' - b)$. If $y \ge 0$ and $b' \ge b$ then $v(b') \ge v(b)$.

(c) Write $g_i(b) = \partial v/\partial b_i$ where it exists. Convexity of $v$ makes the subdifferential monotone: if $b' \ge b$ then every $y' \in \partial v(b')$ satisfies $y'_i \ge y_i$ for every $y \in \partial v(b)$ in the sense of the one-sided derivatives. Economically: the first units of a scarce resource are cheap to substitute, later units are dearer, because the cheapest substitutions are used first. Equivalently, in a maximisation the value is concave in capacity and marginal values diminish.

**25.** *(Strategy: a fractional vertex contains a cycle of fractional entries; perturb along it.)*

Let $P = \{X \ge 0 : X\mathbf{1} = \mathbf{1},\ X^{\mathsf{T}}\mathbf{1} = \mathbf{1}\}$ and let $X \in P$ be a vertex. Suppose some entry is fractional. Consider the bipartite graph on rows and columns whose edges are the fractional entries $0 < x_{ij} < 1$. Every node of this graph has degree at least $2$: if row $i$ had exactly one fractional entry $x_{ij}$, then the row sum $1 = x_{ij} + (\text{sum of the } 0/1 \text{ entries})$ would make $x_{ij}$ an integer, a contradiction, and the same argument applies to columns. A finite graph with minimum degree at least $2$ contains a cycle, say rows $i_1,\dots,i_k$ and columns $j_1,\dots,j_k$ with $x_{i_r j_r} > 0$ and $x_{i_r j_{r-1}} > 0$ (indices mod $k$) and all these entries strictly between $0$ and $1$.

Define $D$ by $+1$ at $(i_r, j_r)$, $-1$ at $(i_r, j_{r-1})$, and $0$ elsewhere. Every row sum and every column sum of $D$ is $1 - 1 = 0$, so $X \pm \varepsilon D \in P$ for all sufficiently small $\varepsilon > 0$. Since $D \ne 0$, this writes $X = \tfrac12(X + \varepsilon D) + \tfrac12(X - \varepsilon D)$ as a convex combination of two distinct points of $P$, contradicting that $X$ is a vertex. Hence every vertex has all entries in $\{0,1\}$; the row and column sums then force exactly one $1$ per row and column, i.e. a permutation matrix. $\blacksquare$

*Consequence.* The LP relaxation of the assignment problem has integral vertices, so it is exact.

**26.** *(Strategy: exchange argument, then bounding.)*

(a) Sort so that $v_1/w_1 \ge v_2/w_2 \ge \dots \ge v_n/w_n$. Suppose a feasible LP solution has $x_i < 1$ and $x_j > 0$ with $i < j$ (so item $i$ has the better ratio). Move mass out of $j$ and into $i$ while keeping the total weight constant: reduce $x_j$ by $\delta$ and increase $x_i$ by $\delta w_j/w_i$. For small $\delta > 0$ the result is feasible, and the change in objective is

$$
\delta\frac{w_j}{w_i}v_i - \delta v_j = \delta w_j\left(\frac{v_i}{w_i} - \frac{v_j}{w_j}\right) \ge 0 .
$$

Repeating pushes any LP optimum into the greedy form: items in ratio order at $1$, one fractional item, the rest at $0$.

(b) The greedy LP solution has value $P + f v_k$ where $P$ is the value of the integral prefix and $f < 1$. Since the prefix alone is an integer feasible solution, $z_{\mathrm{IP}} \ge P$; hence

$$
z_{\mathrm{LP}} = P + f v_k \le P + v_{\max} \le z_{\mathrm{IP}} + v_{\max}.
$$

(c) Let $G$ be the value of the whole-item greedy solution. Every prefix item is taken, so $G \ge P$. Then

$$
\max\{G, v_{\max}\} \ge \max\{P, v_{\max}\} \ge \frac{P + v_{\max}}{2} \ge \frac{P + f v_k}{2} = \frac{z_{\mathrm{LP}}}{2} \ge \frac{z_{\mathrm{IP}}}{2},
$$

where the last inequality uses $z_{\mathrm{LP}} \ge z_{\mathrm{IP}}$ for a maximisation.

(d) Capacity $2$, items $(w,v) = (1, 1+\varepsilon)$ and $(2, 2)$. Ratios: $1+\varepsilon > 1$, so greedy takes the first item and cannot take the second: $G = 1 + \varepsilon$. The optimum is $2$ (the single heavy item). The ratio is $(1+\varepsilon)/2 \to \tfrac12$. Since $\varepsilon$ is arbitrary, no constant larger than $\tfrac12$ can be guaranteed.

**27.** *(Strategy: the KKT proof is a chain of convexity inequalities.)*

Let $f, g_i$ be convex and differentiable, $h_j$ affine, and suppose $(x^\ast, \lambda, \mu)$ satisfies stationarity $\nabla f(x^\ast) + \sum_i \lambda_i\nabla g_i(x^\ast) + \sum_j \mu_j\nabla h_j(x^\ast) = 0$, $\lambda \ge 0$, $\lambda_ig_i(x^\ast) = 0$, primal feasibility. For any feasible $y$: convexity gives $\nabla g_i(x^\ast)^{\mathsf{T}}(y - x^\ast) \le g_i(y) - g_i(x^\ast) \le -g_i(x^\ast)$ and, for affine $h_j$, $\nabla h_j(x^\ast)^{\mathsf{T}}(y-x^\ast) = 0$. Hence

$$
f(y) \ge f(x^\ast) + \nabla f(x^\ast)^{\mathsf{T}}(y-x^\ast)
= f(x^\ast) - \sum_i \lambda_i \nabla g_i(x^\ast)^{\mathsf{T}}(y - x^\ast) \ge f(x^\ast) + \sum_i \lambda_i g_i(x^\ast) = f(x^\ast),
$$

so $x^\ast$ is a global minimiser. $\blacksquare$

Applying it to Exercise 20: $f = x^2 + 2y^2$ is convex, $g = 3 - x - y \le 0$ is affine, and $(x,y,\lambda) = (2,1,4)$ satisfies $2x - \lambda = 0$, $4y - \lambda = 0$, $\lambda(3 - x - y) = 0$ and $\lambda > 0$ with the constraint active. All KKT conditions hold, so $(2,1)$ is global.

**28.** *(Strategy: (a) is a two-line contradiction; (b) is a separating hyperplane.)*

(a) Suppose $w_1, w_2 > 0$ and $x^\ast$ minimises $w_1f_1 + w_2f_2$, but some $y$ dominates $x^\ast$: $f_i(y) \le f_i(x^\ast)$ with strict inequality for at least one $i$. Then $w_1f_1(y) + w_2f_2(y) < w_1f_1(x^\ast) + w_2f_2(x^\ast)$, contradicting minimality.

(b) Let $S = \{f(x) + r : x \in \mathcal{F},\ r \ge 0\}$, which is convex by hypothesis, and let $x^\ast$ be Pareto optimal, so $f(x^\ast)$ is on the boundary of $S$. By the supporting hyperplane theorem there is $w \ne 0$ with $w^{\mathsf{T}}f(x^\ast) \le w^{\mathsf{T}}s$ for all $s \in S$. Taking $s = f(x) + r$ and letting $r_i \to \infty$ in each coordinate forces $w \ge 0$. Hence $w^{\mathsf{T}}f(x^\ast) \le w^{\mathsf{T}}f(x)$ for every feasible $x$.

(c) Take $\mathcal{F} = \{A, B, C\}$ with $f(A) = (1,0)$, $f(B) = (0,1)$, $f(C) = (0.4,0.4)$, all minimised. $A$ and $B$ are Pareto optimal. $C$ is also Pareto optimal: $A$ has the smaller $f_1$ but $f_2(A) = 0 < 0.4$, so $A$ does not dominate $C$; similarly $B$ does not, and $C$ dominates neither. For any weights $w_1, w_2 > 0$,

$$
w^{\mathsf{T}}f(C) = 0.4(w_1 + w_2) < \max\{w_1, w_2\} = \min\{w^{\mathsf{T}}f(A),\ w^{\mathsf{T}}f(B)\},
$$

so $C$ is never the minimiser of a positive weighted sum. The attainable set is non-convex, so (b) does not apply.

**29.** *(Strategy: write the dual, then use complementary slackness.)*

(a) With $x_{ij} \ge 0$ and equality constraints on rows and columns, the dual is

$$
\max\ \sum_i s_i u_i + \sum_j d_j v_j \quad\text{s.t.}\quad u_i + v_j \le c_{ij}\ \ \forall i,j,
$$

with $u, v$ free. $u_i$ is the marginal cost of supply at plant $i$ and $v_j$ the marginal cost of demand at warehouse $j$.

(b) If $x$ is feasible and $u_i + v_j \le c_{ij}$ for all $i,j$ with equality on the used routes $x_{ij} > 0$, then

$$
\sum_{i,j} c_{ij}x_{ij} = \sum_{i,j}(u_i + v_j)x_{ij} = \sum_i u_i s_i + \sum_j v_j d_j ,
$$

using the row and column sums. The common value is the primal cost and the dual objective, so by weak duality both are optimal.

(c) If $(u,v)$ is dual feasible, so is $(u + t\mathbf{1}, v - t\mathbf{1})$ for any $t \in \mathbb{R}$, with the same objective and the same reduced costs. Hence the dual optimal set, if non-empty, is at least one-dimensional, and individual potentials are not identified: only sums $u_i + v_j$ and reduced costs are. The practical consequence is that "the shadow price of demand at warehouse $j$" is not well defined without a normalisation; a rate of change must be quoted for a *pair* (supply, demand) or for a normalised dual.

**30.** *(Strategy: derive the bound, then compare formulations.)*

(a) A link flow satisfies $x_{ij} \le \min(\mathrm{cap}_i, d_j)$ for every feasible integer solution, since it cannot exceed the site's capacity nor the customer's demand. Hence the smallest valid constant is $M_i = \max_j \min(\mathrm{cap}_i, d_j) = \min(\mathrm{cap}_i, \max_j d_j)$.

(b) Take one site with capacity 100, two customers with demands 40 each, and use $M = 30$ (smaller than the largest link flow). The constraint $x_{ij} \le 30y_i$ caps each link at 30, so the site can ship at most 60 of the 80 required, and the model reports infeasibility although the true problem is feasible (ship 40 to each). A valid $M$ here is 40.

(c) Since $\min(\mathrm{cap}_i, \max_j d_j) \le \sum_j d_j$, the feasible region with the smaller constant is contained in the one with the larger, so its LP minimum is at least as large — a bound no worse for a minimisation. For the instance of §9.6 the improvement was from $450.56$ to $585.56$ when moving from the total-demand constant to the per-demand constant, and to $611.43$ when the aggregate linking was added as well.

**31.** *(Strategy: convexity of the optimal set.)*

Let $x^1 \ne x^2$ both be optimal with value $v$. For $\lambda \in [0,1]$, $x = \lambda x^1 + (1 - \lambda)x^2$ is feasible (the feasible set is convex) and $c^{\mathsf{T}}x = \lambda v + (1-\lambda)v = v$, so $x$ is optimal. Since $\lambda$ is arbitrary, there are infinitely many optimal solutions. The optimal set is $\{x \in P : c^{\mathsf{T}}x = v\} = P \cap \{x : c^{\mathsf{T}}x \ge v\}$, the intersection of the polyhedron with a half-space — a face of $P$.

For the instance: $\max\ x + y$ subject to $x + y \le 4$, $x \le 3$, $y \le 3$, $x, y \ge 0$. The value is $4$, attained exactly where $x + y = 4$, $1 \le x \le 3$: the segment from $(1,3)$ to $(3,1)$, a one-dimensional face. Every point of it is optimal and $c^{\mathsf{T}}x = 4$ there.

## Challenge

**32.** *(Strategy: force $x + y = 4$ and bound both variables.)*

Consider

$$
\max\ x + y \quad\text{s.t.}\quad x + y \le 4,\quad x \ge 1,\quad y \ge 1,\quad x \le 3,\quad y \le 3 .
$$

Every feasible point satisfies $x + y \le 4$ with equality exactly when $x + y = 4$; together with $1 \le x \le 3$ and $y = 4 - x \in [1,3]$, the optimal set is precisely the segment from $(1,3)$ to $(3,1)$.

**Certificate.** The dual of the maximisation with constraints written as $x + y \le 4$, $-x \le -1$, $-y \le -1$, $x \le 3$, $y \le 3$ is, with multipliers $u \ge 0$,

$$
\min\ 4u_1 - u_2 - u_3 + 3u_4 + 3u_5 \quad\text{s.t.}\quad u_1 - u_2 + u_4 \ge 1,\quad u_1 - u_3 + u_5 \ge 1 .
$$

Taking $u = (1,0,0,0,0)$ is dual feasible and gives value $4$, equal to the primal value at $(2,2)$, so the optimum is $4$ by Theorem 8.1.

**No other point is optimal.** Any feasible point with $x + y < 4$ has objective strictly less than $4$; and any point with $x + y = 4$ and $x \notin [1,3]$ violates $x \ge 1$ or $x \le 3$. Hence the optimal set is exactly the segment.

**33.** *(Strategy: the normal cone of a vertex is full-dimensional.)*

Let $x^\ast$ be a vertex of $P = \{x : Ax \le b\}$, so that $n$ linearly independent constraints are tight at $x^\ast$; write their normals as $a_1,\dots,a_n$ with $a_i^{\mathsf{T}}x^\ast = b_i$. Define $c = \sum_{i=1}^{n} a_i$. For any $x \in P$ with $x \ne x^\ast$:

$$
c^{\mathsf{T}}(x - x^\ast) = \sum_i a_i^{\mathsf{T}}(x - x^\ast) \le 0,
$$

because $a_i^{\mathsf{T}}x \le b_i = a_i^{\mathsf{T}}x^\ast$ for each $i$. Moreover the inequality is strict: if all $n$ were equalities, then $x$ would satisfy the $n$ independent equations $a_i^{\mathsf{T}}x = b_i$, forcing $x = x^\ast$. Hence $x^\ast$ is the *unique* maximiser of $c^{\mathsf{T}}x$ over $P$.

If $x^\ast$ has a fractional coordinate, the LP optimum is $x^\ast$, which is fractional. The integer optimum is attained at some integral $x^{\mathrm{I}} \in P$ (assuming one exists), and it satisfies $c^{\mathsf{T}}x^{\mathrm{I}} < c^{\mathsf{T}}x^\ast$ strictly. Hence the LP relaxation fails for this objective.

Conversely, if every vertex of $P$ is integral, then the LP optimum — which is attained at a vertex by Theorem 8.6 — is integral for every $c$, so the relaxation is exact for every objective. $\blacksquare$

*Remark.* This is why "the LP relaxation is exact" is a property of the polyhedron, not of a particular objective: a single fractional vertex is enough to produce an objective for which the relaxation is wrong.

**34.** *(Strategy: separate the value from the prices.)*

(a) A redundant constraint does not change the feasible set, so it cannot change the optimal value. It does change the *dual* problem (an extra dual variable) and can make the optimal dual set larger, so the reported prices—which are one element of that set—can change.

(b) Redundant does not mean inactive: a constraint implied by the others may still be tight at an optimum. If it is tight, it can be part of a dual optimal solution.

(c) Take $\max\ x + y$ subject to $x \le 1$, $y \le 1$, $x, y \ge 0$: optimum $(1,1)$, value $2$, duals $(1,1)$ — each capacity is worth $1$ per unit. Now add the redundant constraint $x + y \le 2$, which is implied by the first two and is tight at $(1,1)$. The dual becomes: maximise $u_1 + u_2 + 2u_3$ subject to $u_1 + u_3 \ge 1$, $u_2 + u_3 \ge 1$, $u \ge 0$. Every $u = (1 - t, 1 - t, t)$ with $t \in [0,1]$ is optimal, so the shadow price reported for $x \le 1$ can be anything in $[0,1]$ — in particular $0.5$, not $1$.

*Lesson.* The optimal *value* is a property of the model; individual shadow prices are properties of a chosen dual solution, and adding a redundant constraint widens the set of admissible prices without changing anything real.

**35.** *(Strategy: support the convex set; then break convexity.)*

(a) If the attainable set $S = \{f(x) + r\}$ is convex and $x^\ast$ is Pareto optimal, then $f(x^\ast)$ is on the boundary and the supporting hyperplane theorem gives $w \ge 0$, $w \ne 0$, with $w^{\mathsf{T}}f(x^\ast) \le w^{\mathsf{T}}f(x)$ for all feasible $x$ (Theorem 8.8). So every Pareto point is supported.

(b) With $f(A) = (1,0)$, $f(B) = (0,1)$, $f(C) = (0.4,0.4)$ (all minimised), $A$ and $B$ are Pareto optimal, and so is $C$: $A$ has $f_1 = 1 > 0.4$ and $B$ has $f_2 = 1 > 0.4$, so neither dominates $C$, and $C$ does not dominate either. For any $w_1, w_2 > 0$,

$$
w^{\mathsf{T}}f(C) = 0.4(w_1 + w_2) < \max\{w_1, w_2\} = \min\{w^{\mathsf{T}}f(A),\ w^{\mathsf{T}}f(B)\},
$$

because $0.4(w_1+w_2) < \max$ reduces to $0.4\min < 0.6\max$, which holds. Hence $C$ is never a weighted-sum minimiser: it is an unsupported Pareto point.

(c) The $\varepsilon$-constraint method minimises $f_2$ subject to $f_1 \le \varepsilon$. For $\varepsilon = 1$ it returns $A$; for $\varepsilon = 0.4$ it returns $C$ (the only point with $f_1 \le 0.4$ is $C$, with $f_2 = 0.4$); for $\varepsilon = 0$ it returns $B$. Sweeping $\varepsilon$ discovers $C$ exactly.

**36.** *(Strategy: read the model as a plan and ask what each symbol means.)*

(a) Errors and hidden assumptions:

1. **Negative contribution product.** With $p_j < 0$ and no lower bound, the model sets $x_j = 0$ — correct if the product is optional, wrong if it is contractually required or needed to absorb a by-product. The model does not know the difference.
2. **A resource with $b_i = 0$.** The constraint $\sum_j a_{ij}x_j \le 0$ with $a_{ij} > 0$ forces every $x_j = 0$: the whole model collapses, and every shadow price becomes meaningless. This is almost certainly a data error (a missing value entered as zero) rather than a real "no capacity".
3. **Unbounded demand.** There is no $x_j \le d_j$, so the model produces unlimited quantities of any product whose resource usage does not exhaust a constraint.
4. **Mixed units not checked.** $a_{ij}$ in hours per tonne times $x_j$ in tonnes gives hours per week, which matches $b_i$ — the units happen to be consistent here, but the *time period* of $a_{ij}$ is not stated: is it hours per tonne in the same week? If $a_{ij}$ was measured over a month, the constraint is off by a factor of four.
5. **Divisibility and integrality.** Tonnes are divisible, so the LP is acceptable, but if $b_i$ is in whole machine-hours and set-ups consume hours, the linear model overstates capacity.

(b) Repaired model: add demand caps $0 \le x_j \le d_j$; either drop the negative-contribution product with an explicit argument or add a contractual lower bound $x_j \ge \ell_j$ and treat the deficit as a cost; correct $b_i$ for the zero entry and record its source; state the time unit of every coefficient; and, if set-ups matter, introduce binaries with fixed charges. Formally,

$$
\max\ \sum_j p_j x_j \quad\text{s.t.}\quad \sum_j a_{ij}x_j \le b_i\ (\text{hours per week}),\quad \ell_j \le x_j \le d_j .
$$

(c) As written, the solver returns $x = 0$ for every product (because of the zero resource) or, if that resource is removed, an unbounded or absurdly large plan for the product with the best margin. In both cases the answer is "correct": it is the optimum of the model that was written. It is useless because the model does not describe the factory.

*Lesson.* A solver cannot detect a units error, a missing demand cap, or a zero that should have been a thousand. Only the modeller can, and only by reading the optimal solution as a plan and asking whether it is physically sensible.
