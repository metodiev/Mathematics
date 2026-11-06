# Linear Programming — Exercises

> [Linear Programming](README.md) · 36 problems · Beginner → Challenge · Solutions: [solutions.md](solutions.md)

Work through the problems in order. Each problem cites the section of the tutorial it draws on. Problems 1–12 build fluency with formulations, graphics and the dictionary; 13–22 combine the simplex method with duality, sensitivity and applications; 23–30 are proof problems; 31–36 are challenge problems on the boundaries of the theory. Attempt every problem before opening [solutions.md](solutions.md), and **substitute every answer back into the constraints** — in linear programming that check is decisive.

Conventions: all variables are non-negative unless a problem says otherwise. "Solve" means find an optimal solution and the optimal value. "Formulate" means write the objective, every constraint and the non-negativity conditions, but do not solve unless asked. All data are exact; fractions are acceptable and often preferable to decimals.

## Beginner

**1.** *(§7.1)* A workshop makes desks $x$ and bookcases $y$. A desk uses 5 units of wood and 3 hours of labour and earns 60; a bookcase uses 4 units of wood and 2 hours of labour and earns 40. There are 100 units of wood and 70 hours of labour, and at most 12 bookcases can be sold. Formulate the profit-maximising linear program. Do not solve it.

**2.** *(§7.2)* Solve graphically:
$$\max z=2x+y\quad\text{s.t.}\quad x+y\le4,\quad x\le3,\quad y\le2,\quad x,y\ge0.$$
List every vertex, evaluate $z$ at each, and state which constraints are binding at the optimum.

**3.** *(§7.2)* Solve graphically:
$$\max z=3x+2y\quad\text{s.t.}\quad x+2y\le8,\quad 2x+y\le10,\quad x,y\ge0.$$
Verify the optimum by substituting it into both constraints.

**4.** *(§7.4)* Put the following LP in standard form:
$$\max\ 2x_1-x_2+3x_3\quad\text{s.t.}\quad x_1+x_2\le5,\quad 2x_1-x_3\ge1,\quad x_2\ \text{free},\quad x_1,x_3\ge0.$$
State the objective, the equations and the non-negativity conditions.

**5.** *(§7.2)* Solve graphically:
$$\min z=x+2y\quad\text{s.t.}\quad x+y\ge3,\quad 2x+y\ge4,\quad x,y\ge0.$$
Explain why the optimum is not at the intersection of the two boundary lines.

**6.** *(§7.2)* For the region
$$x+y\le2,\qquad x-y\le2,\qquad x\ge0,\quad y\ge0,$$
list all vertices and decide whether the region is bounded. Justify the boundedness answer from the vertices.

**7.** *(§7.8)* Write the dual of
$$\max z=3x_1+2x_2\quad\text{s.t.}\quad x_1+x_2\le4,\quad 2x_1+x_2\le6,\quad x_1,x_2\ge0.$$
State the dual objective, both dual constraints and the signs of $y_1,y_2$.

**8.** *(§7.8)* For the primal
$$\max\ 4x_1+3x_2\quad\text{s.t.}\quad 2x_1+x_2\le8,\quad x_1+2x_2\le8,\quad x\ge0,$$
the dual is $\min 8y_1+8y_2$ subject to $2y_1+y_2\ge4$, $y_1+2y_2\ge3$, $y\ge0$.
(a) Check that $x=(2,2)$ is primal feasible and $y=(2,0.5)$ is dual feasible.
(b) Verify weak duality numerically for this pair.
(c) Find the optimal primal and dual solutions and check that the two optimal values agree.

**9.** *(§7.5)* A simplex tableau for a maximisation problem has rows
$$x_1+\tfrac23s_1-\tfrac13s_2=\tfrac{10}{3},\qquad x_2-\tfrac13s_1+\tfrac23s_2=\tfrac43,\qquad z+\tfrac83s_1+\tfrac23s_2=\tfrac{76}{3}.$$
(a) Read off the basic solution, the basis and the objective value.
(b) Read off the dual solution.
(c) Verify that the basic solution is feasible for $2x_1+x_2\le8$, $x_1+2x_2\le6$ and that its objective equals $76/3$.

**10.** *(§7.1)* A feed mill blends corn, soy and limestone. Per kilogram, corn contains 0.09 kg protein and 0.02 kg fat and costs 0.30; soy contains 0.40 kg protein and 0.10 kg fat and costs 0.60; limestone contains no protein or fat and costs 0.10. One kilogram of feed must contain at least 0.20 kg protein and at most 0.10 kg fat. Formulate the cost-minimising LP. Do not solve.

**11.** *(§7.2, §7.9)* For the LP
$$\max z=3x+4y\quad\text{s.t.}\quad x+y\le5,\quad 2x+y\le8,\quad x,y\ge0,$$
consider the point $(2,3)$. Compute the slacks, the objective value, and determine which constraints are binding. Is the point optimal? Justify your answer by finding the optimum.

**12.** *(§5, §7.4)* For the system
$$x_1+x_2+x_3=6,\qquad 2x_1+x_2=4,\qquad x\ge0,$$
decide which of the following points are feasible and which are basic feasible solutions:
(a) $(0,4,2)$; (b) $(2,0,4)$; (c) $(1,2,3)$; (d) $(1,1,4)$; (e) $(1,3,2)$.
For each bfs, identify a basis.

## Intermediate

**13.** *(§7.5)* Solve by the simplex method, showing every tableau:
$$\max z=4x_1+3x_2\quad\text{s.t.}\quad 2x_1+x_2\le10,\quad x_1+2x_2\le8,\quad x_1,x_2\ge0.$$
State the entering and leaving variable at each pivot and verify the final tableau's optimality.

**14.** *(§7.5)* Consider
$$\max z=x_1+2x_2\quad\text{s.t.}\quad x_1-x_2\le2,\quad x_1,x_2\ge0.$$
Run the simplex method until it detects unboundedness. Explain which ratio test fails, and exhibit a feasible ray along which $z\to\infty$.

**15.** *(§7.5)* Use the two-phase simplex method to solve
$$\min z=2x_1+3x_2\quad\text{s.t.}\quad x_1+x_2\ge4,\quad x_1+3x_2\ge6,\quad x_1,x_2\ge0.$$
Convert to a maximisation first, show the phase-1 tableaus, and then solve phase 2.

**16.** *(§7.3, §7.9)* Solve
$$\max z=2x_1+4x_2\quad\text{s.t.}\quad x_1+2x_2\le8,\quad x_1+x_2\le5,\quad x_1,x_2\ge0.$$
Show that the optimum is not unique, describe the entire optimal set, and explain how a zero reduced cost signals the second optimal vertex.

**17.** *(§7.8, §7.9)* For the primal
$$\max z=4x_1+3x_2\quad\text{s.t.}\quad 2x_1+x_2\le8,\quad x_1+2x_2\le7,\quad x\ge0,$$
(a) write the dual; (b) solve the primal; (c) use complementary slackness to find the dual optimum; (d) verify that the two optimal values agree and that every complementary-slackness condition holds.

**18.** *(§7.11)* For the LP of Exercise 17, use the final basis to compute the individual allowable range of each of $b_1=8$, $b_2=7$, $c_1=4$ and $c_2=3$. On each range give $z^{*}$ as a function of the changing coefficient, and check both endpoints by solving the LP directly.

**19.** *(§7.12)* Solve the integer program
$$\max\ 3x_1+2x_2\quad\text{s.t.}\quad 2x_1+x_2\le6,\quad x_1+3x_2\le9,\quad x_1,x_2\in\mathbb{Z}_{\ge0}$$
by branch-and-bound. Solve the LP relaxation, choose a fractional variable, branch, and draw the tree. State the incumbent and the bound at each node.

**20.** *(§7.13)* Two warehouses have supplies 25 and 35; three shops have demands 15, 25 and 20. The unit costs are
$$C=\begin{pmatrix}4&6&8\\5&3&7\end{pmatrix}.$$
(a) Verify that the problem is balanced. (b) Find an initial basic feasible solution by the north-west corner rule and its cost. (c) Compute the potentials and the reduced costs, carry out one improving cycle, and find the optimal cost. (d) Is the optimal solution unique?

**21.** *(§7.13)* A seven-day operation needs at least $r_t$ employees on day $t$, where $t=1,\dots,7$ and $r=(10,12,8,14,16,12,6)$. Each employee works five consecutive days and then has two consecutive days off. Let $x_j$ be the number of employees whose two-day break begins after day $j$ (with indices taken modulo 7). Formulate the LP that minimises the total workforce. Do not solve.

**22.** *(§7.2, §7.13)* A blend must contain at least 8 units of protein, 10 units of carbohydrate and 5 units of fibre. Ingredient $A$ supplies 1 unit of protein, 2 of carbohydrate and 1 of fibre per kg and costs 3; ingredient $B$ supplies 2, 1 and 1 per kg and costs 2. Formulate the cost-minimising blend and solve it graphically. Identify the binding constraints and give the dual prices.

## Advanced

**23.** *(§7.3)* Prove the fundamental theorem of linear programming: if the standard-form LP $\max\{c^{T}x:Ax=b,\ x\ge0\}$ has an optimal solution, then it has an optimal basic feasible solution. Structure the proof as follows: choose an optimal solution with the fewest positive components; if its support columns are dependent, construct a direction $d$ with $Ad=0$ and show that $x^{*}\pm\theta d$ is optimal for small $\theta$; then choose the largest feasible step in the direction that makes a component vanish and obtain a contradiction.

**24.** *(§7.8)* Prove weak duality for the pair
$$\max\{c^{T}x:Ax\le b,\ x\ge0\},\qquad \min\{b^{T}y:A^{T}y\ge c,\ y\ge0\}.$$
State exactly where each hypothesis ($x\ge0$, $y\ge0$, $Ax\le b$, $A^{T}y\ge c$) is used.

**25.** *(§7.9)* Prove the complementary slackness theorem: feasible $x,y$ are both optimal if and only if $y_i(b_i-a_i^{T}x)=0$ for every $i$ and $x_j((A^{T}y)_j-c_j)=0$ for every $j$. Prove both directions, and explain why the "if" direction does not need strong duality.

**26.** *(§7.8)* Prove that the dual of the dual is the primal for the symmetric pair. Carry out the conversion carefully, including the sign changes needed to write the dual as a maximisation.

**27.** *(§7.5, §7.8)* Suppose the simplex method has terminated at an optimal basis $B$ for a standard-form maximisation with $\le$ constraints. Define $y^{T}=c_B^{T}B^{-1}$ and prove directly from the final tableau that $y$ is dual feasible and that $b^{T}y=c_B^{T}x_B$. Conclude strong duality for this case. Explain why this argument does not by itself cover the case in which the primal is infeasible or unbounded, and how weak duality settles those cases.

**28.** *(§7.3)* Let $P$ be a non-empty bounded polyhedron. Using the fact that every point of a bounded polyhedron is a convex combination of its vertices, prove that a linear function $c^{T}x$ attains its maximum on $P$ at a vertex. Deduce that an optimal basic feasible solution exists whenever the feasible region is bounded and non-empty.

**29.** *(§7.7)* Consider
$$\max z=2x_1+x_2\quad\text{s.t.}\quad x_1+x_2\le4,\quad x_1\le2,\quad x_2\le2,\quad x\ge0.$$
(a) Show that the vertex $(2,2)$ has three active constraints, and that the basis consisting of $x_1$, $x_2$ and the slack of $x_1+x_2\le4$ is degenerate. (b) Write the tableau for that basis and read off the basic solution. (c) Explain why a negative reduced cost together with a zero basic variable would produce a zero-length pivot, why the objective would not change, and why a sequence of such pivots can cycle.

**30.** *(§7.12)* Prove that if $A$ is totally unimodular and $b$ is integral, then every basic feasible solution of $Ax\le b$, $x\ge0$ is integral. You may use Cramer's rule and the fact that the determinant of an integer matrix is an integer.

## Challenge

**31.** *(§7.8)* (a) Prove that if the primal is unbounded above, then the dual is infeasible. (b) Give a concrete primal-dual pair illustrating the statement, and verify both claims directly. (c) Explain why the converse ("dual infeasible implies primal unbounded") is false.

**32.** *(§7.3)* Let $P$ be a polyhedron and let $S$ be the set of optimal solutions of $\max\{c^{T}x:x\in P\}$. Prove that $S$ is convex, that it is a face of $P$, and that if $S$ contains two distinct points then it contains the whole segment between them. Give an example in which $S$ is an edge and an example in which $S$ is a single vertex.

**33.** *(§7.10, §7.11)* For the LP of §7.6,
$$\max\ 3x_1+5x_2\quad\text{s.t.}\quad x_1\le4,\quad 2x_2\le12,\quad 3x_1+2x_2\le18,\quad x\ge0,$$
the final tableau gives $y_1=0$. Compute $z^{*}(b_1)$ for all $b_1\ge0$, find the left and right derivatives at $b_1=2$, and explain why a zero shadow price does not mean that the constraint can be removed without cost.

**34.** *(§7.12)* Prove that branch-and-bound terminates when the feasible region of the integer program is bounded and all data are rational. Be precise about what "bounded" gives, why the branching tree has finite depth, and why there are only finitely many nodes.

**35.** *(§7.11)* Prove that if the optimal basic feasible solution of the primal is non-degenerate, then the optimal dual solution is unique. Give an example showing that the converse fails: a degenerate primal optimum can still have a unique dual solution.

**36.** *(§7.13)* Prove that the constraint matrix of the transportation problem,
$$\sum_jx_{ij}=s_i,\qquad \sum_ix_{ij}=d_j,$$
is totally unimodular. Use the fact that every column has at most two non-zero entries, both equal to $1$, and that the rows can be split into two groups (sources and destinations) with one $1$ in each group. Explain why this implies integral optimal solutions for integer supplies and demands.
