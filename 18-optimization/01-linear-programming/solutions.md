# Linear Programming — Solutions

> [Linear Programming](README.md) · Solutions to [exercises.md](exercises.md) · 36 problems

Every solution below states the strategy, carries out the computation step by step, and ends with a feasibility and objective check. Where a problem has more than one natural method, the second method is indicated. A fraction is an exact answer and should not be replaced by a decimal unless a decimal is requested.

## Beginner

**1.** *Formulating the workshop model*

**Strategy.** Name the two decisions, attach units, write one row per resource, and add the sales cap.

Let $x$ be desks per week and $y$ bookcases per week. Both are measured in units, so both are non-negative.

* Wood: $5x+4y$ units, available 100, hence $5x+4y\le100$.
* Labour: $3x+2y$ hours, available 70, hence $3x+2y\le70$.
* Sales: at most 12 bookcases, hence $y\le12$.
* Profit: $60x+40y$.

The model is

$$\max\ 60x+40y\quad\text{s.t.}\quad 5x+4y\le100,\quad 3x+2y\le70,\quad y\le12,\quad x,y\ge0.$$

**Check.** Every coefficient of the first row is in wood units, every coefficient of the second in hours, and the objective is in money. The model is linear: no product $xy$, no power and no ratio of variables occurs.

**2.** *Graphical solution of a bounded problem*

**Strategy.** Draw the three boundary lines, list the vertices of the polygon, and evaluate $z$ at each.

The boundary lines are $x+y=4$, $x=3$ and $y=2$. Their feasible intersection is the pentagon with vertices:

| Vertex | Where it comes from | $z=2x+y$ |
|---|---|---|
| $(0,0)$ | origin | $0$ |
| $(3,0)$ | $x=3$ with $y=0$ | $6$ |
| $(3,1)$ | $x=3$ with $x+y=4$ | $7$ |
| $(2,2)$ | $x+y=4$ with $y=2$ | $6$ |
| $(0,2)$ | $x=0$ with $y=2$ | $2$ |

The largest value is $7$ at $(3,1)$. At that point $x+y=4$ and $x=3$ are binding, while $y=2$ is slack by one unit.

**Check.** $3+1=4\le4$, $3\le3$, $1\le2$, and $z=2(3)+1=7$. Moving from $(3,1)$ along $x+y=4$ to $(2,2)$ keeps $z=6<7$, and moving along $x=3$ to $(3,0)$ gives $6<7$, so no adjacent vertex improves.

**3.** *Graphical solution with two resource constraints*

**Strategy.** The feasible region is the quadrilateral cut out by the two lines and the axes.

The intercepts are $(4,0)$ and $(0,8)$ for $x+2y=8$, and $(5,0)$ and $(0,10)$ for $2x+y=10$. The two lines meet where

$$x+2y=8,\qquad 2x+y=10.$$

Multiplying the first equation by $2$ gives $2x+4y=16$; subtracting the second gives $3y=6$, so $y=2$ and $x=4$. The feasible vertices and their values are:

| Vertex | $z=3x+2y$ |
|---|---|
| $(0,0)$ | $0$ |
| $(5,0)$ | $15$ |
| $(4,2)$ | $12+4=16$ |
| $(0,4)$ | $8$ |

The maximum is $16$ at $(4,2)$.

**Check.** $4+2(2)=8\le8$ and $2(4)+2=10\le10$; the objective is $3(4)+2(2)=16$. At $(5,0)$ the second constraint is tight but the first gives $5<8$, and the value is only $15$.

**4.** *Conversion to standard form*

**Strategy.** Free variables split, $\le$ constraints gain slacks, $\ge$ constraints gain surpluses, and the objective keeps its direction.

Let $x_2=x_2'-x_2''$ with $x_2',x_2''\ge0$. Add $s_1\ge0$ to the first constraint and subtract $s_2\ge0$ from the second:

$$\max\ 2x_1-x_2'+x_2''+3x_3$$
$$\text{s.t.}\quad x_1+x_2'-x_2''+s_1=5,\qquad 2x_1-x_3-s_2=1,$$
$$x_1,x_2',x_2'',x_3,s_1,s_2\ge0.$$

**Check.** The first equation reproduces $x_1+x_2\le5$ with $s_1=5-x_1-x_2\ge0$. The second reproduces $2x_1-x_3\ge1$ with $s_2=2x_1-x_3-1\ge0$. The objective is unchanged after substituting $x_2=x_2'-x_2''$. The right-hand sides are already non-negative, so no row needs multiplying by $-1$.

**5.** *A minimisation whose optimum is on an axis*

**Strategy.** List the vertices of the unbounded feasible region. Only the vertices that satisfy all constraints count.

The boundary lines are $x+y=3$ and $2x+y=4$. They meet at $x=1$, $y=2$. The axis intersections are:

* $x=0$ with $x+y=3$ gives $(0,3)$, but $2(0)+3=3<4$, so it is infeasible.
* $x=0$ with $2x+y=4$ gives $(0,4)$, which satisfies $0+4=4\ge3$.
* $y=0$ with $x+y=3$ gives $(3,0)$, which satisfies $2(3)+0=6\ge4$.
* $y=0$ with $2x+y=4$ gives $(2,0)$, which violates $x+y=2<3$.

So the vertices are $(3,0)$, $(1,2)$ and $(0,4)$, with values $3$, $5$ and $8$. The minimum is $3$ at $(3,0)$.

**Why not the intersection?** The isocost lines $x+2y=c$ have slope $-1/2$. This is shallower than both boundary slopes ($-1$ and $-2$), so pushing the line toward the origin makes it leave the feasible region through the vertex $(3,0)$ on the $x$-axis, not through $(1,2)$. At $(1,2)$ the value is larger ($5$), and at $(0,4)$ it is larger still ($8$).

**Check.** $(3,0)$: $3+0=3\ge3$ and $2(3)+0=6\ge4$, so it is feasible; $z=3$. The objective is linear and the feasible region is a polyhedron whose recession directions $(1,0)$ and $(0,1)$ both have positive cost, so the minimum is attained at a vertex. All three vertices have been checked, and $3$ is the smallest value.

**6.** *Vertices and boundedness*

**Strategy.** Intersect pairs of boundary lines, keep the points that satisfy the other inequalities, and then use the constraints to bound the coordinates.

The boundary lines are $x+y=2$, $x-y=2$, $x=0$ and $y=0$. The feasible intersections are:

* $(0,0)$: axes.
* $(2,0)$: $x+y=2$ with $y=0$; also $x-y=2$, so it is a second intersection.
* $(0,2)$: $x+y=2$ with $x=0$.

The intersection of $x+y=2$ and $x-y=2$ is $(2,0)$, already listed. The intersection of $x-y=2$ with $x=0$ is $(0,-2)$, infeasible. Hence the region is the triangle with vertices $(0,0)$, $(2,0)$, $(0,2)$.

**Boundedness.** From $x+y\le2$ and $x,y\ge0$ we get $0\le x\le2$ and $0\le y\le2$. A subset of a bounded rectangle is bounded, so the region is bounded. Its vertices are exactly the three listed, and the triangle is their convex hull.

**7.** *Constructing a dual*

**Strategy.** Transpose the constraint matrix, exchange $b$ and $c$, reverse the inequality, and keep the variables non-negative because the primal constraints are $\le$ and the primal is a maximisation.

Primal: $\max 3x_1+2x_2$ subject to $x_1+x_2\le4$, $2x_1+x_2\le6$, $x\ge0$.

Dual:

$$\min\ 4y_1+6y_2\quad\text{s.t.}\quad y_1+2y_2\ge3,\quad y_1+y_2\ge2,\quad y_1,y_2\ge0.$$

**Check.** The dual has one constraint per primal variable (two) and one variable per primal constraint (two). The coefficient of $y_1$ in the constraint for $x_1$ is $A_{11}=1$, and the coefficient of $y_2$ is $A_{21}=2$, matching the column $(1,2)^{T}$ of $A$. The right-hand sides are $c_1=3$ and $c_2=2$.

**8.** *Weak duality and matching optimal values*

**(a) Feasibility.** For $x=(2,2)$: $2(2)+2=6\le8$ and $2+2(2)=6\le8$, so $x$ is primal feasible. For $y=(2,0.5)$: $2(2)+0.5=4.5\ge4$ and $2+2(0.5)=3\ge3$, so $y$ is dual feasible.

**(b) Weak duality.** The primal value is $4(2)+3(2)=14$. The dual value is $8(2)+8(0.5)=16+4=20$. Indeed $14\le20$.

**(c) Optimal pair.** The primal vertices are $(0,0)$, $(4,0)$, $(0,4)$ and the intersection of the two constraints. Solving

$$2x_1+x_2=8,\qquad x_1+2x_2=8$$

gives $x_1=x_2=8/3$, with $z=4(8/3)+3(8/3)=56/3$. The other values are $16$, $12$ and $0$, so the primal optimum is $56/3$ at $(8/3,8/3)$.

At the dual optimum both dual constraints are tight, because both primal variables are positive. Solving

$$2y_1+y_2=4,\qquad y_1+2y_2=3$$

gives $y_1=5/3$ and $y_2=2/3$. The dual value is $8(5/3)+8(2/3)=40/3+16/3=56/3$, equal to the primal value.

**Check.** The dual point is feasible: $2(5/3)+2/3=12/3=4$ and $5/3+4/3=3$. By weak duality and equality of the values, both are optimal.

**9.** *Reading a final tableau*

**(a) Basic solution.** The rows are in canonical form for the basis $\{x_1,x_2\}$; the non-basic variables $s_1,s_2$ are zero. Hence

$$x_1=\frac{10}{3},\qquad x_2=\frac43,\qquad s_1=s_2=0,\qquad z=\frac{76}{3}.$$

**(b) Dual solution.** In a maximisation tableau the coefficients of the slack variables in the $z$ row are the dual variables:

$$y_1=\frac83,\qquad y_2=\frac23.$$

**(c) Verification.** The constraints are $2x_1+x_2\le8$ and $x_1+2x_2\le6$:

$$2\left(\frac{10}{3}\right)+\frac43=\frac{20}{3}+\frac43=\frac{24}{3}=8,$$
$$\frac{10}{3}+2\left(\frac43\right)=\frac{10}{3}+\frac83=\frac{18}{3}=6.$$

Both are tight. The objective is

$$6\left(\frac{10}{3}\right)+4\left(\frac43\right)=20+\frac{16}{3}=\frac{60+16}{3}=\frac{76}{3}.$$

The dual is feasible: $2(8/3)+2/3=18/3=6$ and $8/3+2(2/3)=8/3+4/3=4$, so it satisfies $2y_1+y_2\ge6$, $y_1+2y_2\ge4$ with equality. The dual value is $8(8/3)+6(2/3)=64/3+4=76/3$, matching the primal.

**10.** *A blending formulation*

**Strategy.** The decision variables are fractions of a kilogram, and the composition constraint is an accounting identity.

Let $c,s,l\ge0$ be the kilograms of corn, soy and limestone in one kilogram of feed.

* Total mass: $c+s+l=1$.
* Protein: $0.09c+0.40s+0l\ge0.20$.
* Fat: $0.02c+0.10s+0l\le0.10$.
* Cost: $0.30c+0.60s+0.10l$.

The model is

$$\min\ 0.30c+0.60s+0.10l$$
$$\text{s.t.}\quad c+s+l=1,\quad 0.09c+0.40s\ge0.20,\quad 0.02c+0.10s\le0.10,\quad c,s,l\ge0.$$

**Check.** The mass constraint is an equality because the three ingredients exhaust the kilogram. The protein and fat rows are in kilograms of nutrient per kilogram of feed, so all three constraints have consistent units. The objective is in currency per kilogram.

**11.** *Slacks, binding constraints and optimality*

**At $(2,3)$.** The first slack is $s_1=5-(2+3)=0$; the second is $s_2=8-(2(2)+3)=8-7=1$. The objective is $z=3(2)+4(3)=6+12=18$. The first constraint is binding, the second is not.

**Is it optimal?** No. The vertices of the feasible region are $(0,0)$, $(4,0)$ and $(0,5)$ and the intersection

$$x+y=5,\qquad 2x+y=8,$$

which gives $x=3$, $y=2$ and $z=17$. The values are $0$, $12$, $20$ and $17$, so the maximum is $20$ at $(0,5)$.

**Check.** $(0,5)$ satisfies $0+5=5\le5$ and $0+5=5\le8$; $z=3(0)+4(5)=20>18$. Hence $(2,3)$ is not optimal, even though it lies on the first boundary.

**12.** *Feasible points and basic feasible solutions*

**Strategy.** First test the two equations, then test whether the columns belonging to the positive components are linearly independent. With two equations, any three positive components are automatically dependent.

The points are tested one by one.

**(a) $(0,4,2)$.** Equations: $0+4+2=6$ and $2(0)+4=4$, both true. The support is $\{2,3\}$, and the columns are $A_2=(1,1)^{T}$ and $A_3=(1,0)^{T}$, which are independent. Hence it is a bfs with basis $\{2,3\}$.

**(b) $(2,0,4)$.** Equations: $2+0+4=6$ and $4+0=4$, true. The support is $\{1,3\}$, with columns $A_1=(1,2)^{T}$ and $A_3=(1,0)^{T}$, independent. Hence it is a bfs with basis $\{1,3\}$.

**(c) $(1,2,3)$.** Equations: $1+2+3=6$ and $2+2=4$, true. All three components are positive, and three vectors in $\mathbb{R}^{2}$ are dependent, so this is not a bfs. It is, in fact, the midpoint of the bfs $(0,4,2)$ and $(2,0,4)$.

**(d) $(1,1,4)$.** The first equation holds ($1+1+4=6$) but the second gives $2+1=3\neq4$, so it is infeasible.

**(e) $(1,3,2)$.** The first equation holds ($1+3+2=6$) but the second gives $2+3=5\neq4$, so it is infeasible.

**Check.** The two bfs satisfy both equations and have two positive components with independent columns. The non-basic variable in (a) is $x_1=0$; in (b) it is $x_2=0$. In each case the basis matrix is invertible, so the basic solution is unique for that basis.

## Intermediate

**13.** *A complete simplex solution*

**Strategy.** Add slacks, build the initial tableau, and pivot until every reduced cost is non-negative. The entering variable is the one with the most negative reduced cost; the leaving variable is chosen by the ratio test.

The standard form is

$$\max\ 4x_1+3x_2\quad\text{s.t.}\quad 2x_1+x_2+s_1=10,\quad x_1+2x_2+s_2=8,\quad x,s\ge0.$$

**Tableau 1.**

| Basis | $x_1$ | $x_2$ | $s_1$ | $s_2$ | RHS |
|---|---|---|---|---|---|
| $z$ | $-4$ | $-3$ | $0$ | $0$ | $0$ |
| $s_1$ | $2$ | $1$ | $1$ | $0$ | $10$ |
| $s_2$ | $1$ | $2$ | $0$ | $1$ | $8$ |

Enter $x_1$ (reduced cost $-4$). Ratios: $10/2=5$ and $8/1=8$, so $s_1$ leaves. Pivot on $2$.

**Tableau 2.**

| Basis | $x_1$ | $x_2$ | $s_1$ | $s_2$ | RHS |
|---|---|---|---|---|---|
| $z$ | $0$ | $-1$ | $2$ | $0$ | $20$ |
| $x_1$ | $1$ | $1/2$ | $1/2$ | $0$ | $5$ |
| $s_2$ | $0$ | $3/2$ | $-1/2$ | $1$ | $3$ |

Enter $x_2$ (reduced cost $-1$). Ratios: $5/(1/2)=10$ and $3/(3/2)=2$, so $s_2$ leaves. Pivot on $3/2$.

**Tableau 3.**

| Basis | $x_1$ | $x_2$ | $s_1$ | $s_2$ | RHS |
|---|---|---|---|---|---|
| $z$ | $0$ | $0$ | $5/3$ | $2/3$ | $22$ |
| $x_1$ | $1$ | $0$ | $2/3$ | $-1/3$ | $4$ |
| $x_2$ | $0$ | $1$ | $-1/3$ | $2/3$ | $2$ |

All reduced costs are non-negative, so the tableau is optimal: $x_1=4$, $x_2=2$, $z=22$.

**Check.** $2(4)+2=10$ and $4+2(2)=8$, both tight; $z=4(4)+3(2)=16+6=22$. The dual solution read from the slack columns is $y=(5/3,2/3)$; it satisfies $2y_1+y_2=10/3+2/3=4$ and $y_1+2y_2=5/3+4/3=3$, so the primal and dual values agree: $10(5/3)+8(2/3)=50/3+16/3=66/3=22$.

**14.** *Detecting unboundedness*

**Strategy.** Put the problem in standard form, run the simplex test, and observe that the entering column has no positive entry.

The standard form is

$$\max\ x_1+2x_2\quad\text{s.t.}\quad x_1-x_2+s_1=2,\quad x,s\ge0.$$

The initial tableau is

| Basis | $x_1$ | $x_2$ | $s_1$ | RHS |
|---|---|---|---|---|
| $z$ | $-1$ | $-2$ | $0$ | $0$ |
| $s_1$ | $1$ | $-1$ | $1$ | $2$ |

The most negative reduced cost is $-2$, so $x_2$ enters. Its column has the single entry $-1$ in the constraint row. Since $-1\le0$, there is no positive entry, so the ratio test has no candidate and the LP is unbounded.

**Ray.** Take $x_1=0$ and $x_2=t$ for $t\ge0$. Then $x_1-x_2=-t\le2$ for every $t\ge0$, so every point of the ray is feasible, and $z=2t\to+\infty$. In tableau language, increasing $x_2$ increases $s_1$ as well, so no basic variable is driven negative.

**Check.** The constraint is satisfied for every $t$: $-t\le2$. The objective is unbounded above. The dual of the problem is $\min 2y$ subject to $y\ge1$ and $-y\ge2$, which is infeasible, consistent with weak duality.

**15.** *Two-phase simplex*

**Strategy.** Convert the minimisation to a maximisation of $w=-z$, add surpluses and artificials, minimise the sum of artificials in phase 1, then restore the true objective in phase 2.

The problem is $\min z=2x_1+3x_2$ subject to $x_1+x_2\ge4$, $x_1+3x_2\ge6$. Write $w=-z=-2x_1-3x_2$ and

$$x_1+x_2-s_1+a_1=4,\qquad x_1+3x_2-s_2+a_2=6.$$

**Phase 1.** Maximise $w_1=-a_1-a_2$. Eliminating the artificials gives

$$w_1-2x_1-4x_2+s_1+s_2=-10.$$

| Basis | $x_1$ | $x_2$ | $s_1$ | $s_2$ | $a_1$ | $a_2$ | RHS |
|---|---|---|---|---|---|---|---|
| $w_1$ | $-2$ | $-4$ | $1$ | $1$ | $0$ | $0$ | $-10$ |
| $a_1$ | $1$ | $1$ | $-1$ | $0$ | $1$ | $0$ | $4$ |
| $a_2$ | $1$ | $3$ | $0$ | $-1$ | $0$ | $1$ | $6$ |

Enter $x_2$; ratios $4$ and $2$, so $a_2$ leaves. Pivot on $3$.

| Basis | $x_1$ | $x_2$ | $s_1$ | $s_2$ | $a_1$ | $a_2$ | RHS |
|---|---|---|---|---|---|---|---|
| $w_1$ | $-2/3$ | $0$ | $1$ | $-1/3$ | $0$ | $4/3$ | $-2$ |
| $a_1$ | $2/3$ | $0$ | $-1$ | $1/3$ | $1$ | $-1/3$ | $2$ |
| $x_2$ | $1/3$ | $1$ | $0$ | $-1/3$ | $0$ | $1/3$ | $2$ |

Enter $x_1$; ratios $2/(2/3)=3$ and $2/(1/3)=6$, so $a_1$ leaves. Pivot on $2/3$.

| Basis | $x_1$ | $x_2$ | $s_1$ | $s_2$ | $a_1$ | $a_2$ | RHS |
|---|---|---|---|---|---|---|---|
| $w_1$ | $0$ | $0$ | $0$ | $0$ | $1$ | $1$ | $0$ |
| $x_1$ | $1$ | $0$ | $-3/2$ | $1/2$ | $3/2$ | $-1/2$ | $3$ |
| $x_2$ | $0$ | $1$ | $1/2$ | $-1/2$ | $-1/2$ | $1/2$ | $1$ |

Phase 1 is complete with $w_1=0$, so the artificials are zero and $(x_1,x_2)=(3,1)$ is feasible.

**Phase 2.** Drop the artificial columns and restore $w=-2x_1-3x_2$. The rows are

$$x_1-\tfrac32s_1+\tfrac12s_2=3,\qquad x_2+\tfrac12s_1-\tfrac12s_2=1.$$

Substituting into $w=-2x_1-3x_2$ gives

$$w+\tfrac32s_1+\tfrac12s_2=-9.$$

All reduced costs are non-negative, so this is already optimal: $w^{*}=-9$, $x_1=3$, $x_2=1$, and $z^{*}=9$.

**Check.** $3+1=4$ and $3+3=6$, so both requirements are met with equality; $z=2(3)+3(1)=9$. The feasible vertices are $(3,1)$, $(0,4)$ and $(6,0)$, with costs $9$, $12$ and $12$; the vertex $(3,1)$ is the best of the three.

**16.** *Alternative optima*

**Strategy.** Solve the LP, then look for a zero reduced cost among the non-basic variables. A zero reduced cost means the objective is flat along an edge.

**Tableau 1.**

| Basis | $x_1$ | $x_2$ | $s_1$ | $s_2$ | RHS |
|---|---|---|---|---|---|
| $z$ | $-2$ | $-4$ | $0$ | $0$ | $0$ |
| $s_1$ | $1$ | $2$ | $1$ | $0$ | $8$ |
| $s_2$ | $1$ | $1$ | $0$ | $1$ | $5$ |

Enter $x_2$; ratios $8/2=4$ and $5/1=5$, so $s_1$ leaves. Pivot on $2$.

| Basis | $x_1$ | $x_2$ | $s_1$ | $s_2$ | RHS |
|---|---|---|---|---|---|
| $z$ | $0$ | $0$ | $2$ | $0$ | $16$ |
| $x_2$ | $1/2$ | $1$ | $1/2$ | $0$ | $4$ |
| $s_2$ | $1/2$ | $0$ | $-1/2$ | $1$ | $1$ |

The reduced cost of $x_1$ is $0$, so the optimum is not unique. The current solution is $(0,4)$ with $z=16$. Entering $x_1$ (a zero-cost direction) and pivoting on the $s_2$ row gives

| Basis | $x_1$ | $x_2$ | $s_1$ | $s_2$ | RHS |
|---|---|---|---|---|---|
| $z$ | $0$ | $0$ | $2$ | $0$ | $16$ |
| $x_2$ | $0$ | $1$ | $1$ | $-1$ | $3$ |
| $x_1$ | $1$ | $0$ | $-1$ | $2$ | $2$ |

The second vertex is $(2,3)$, also with $z=16$. Every point of the segment joining them is optimal:

$$(x_1,x_2)=(2-2\lambda,\,3+\lambda),\qquad 0\le\lambda\le1.$$

Indeed $x_1+2x_2=(2-2\lambda)+2(3+\lambda)=8$ and $x_1+x_2=5-\lambda\le5$, and the objective is $2(2-2\lambda)+4(3+\lambda)=16$.

**Check.** At $(0,4)$: $0+8=8$, $0+4=4\le5$, $z=16$. At $(2,3)$: $2+6=8$, $2+3=5$, $z=4+12=16$. The segment stays inside the feasible region because the first constraint is tight along it and the second has slack $1-\lambda\ge0$.

**17.** *Dual solution by complementary slackness*

**(a) The dual.** The primal is $\max 4x_1+3x_2$ subject to $2x_1+x_2\le8$, $x_1+2x_2\le7$, $x\ge0$. Its dual is

$$\min\ 8y_1+7y_2\quad\text{s.t.}\quad 2y_1+y_2\ge4,\quad y_1+2y_2\ge3,\quad y\ge0.$$

**(b) The primal.** The vertices are $(0,0)$, $(4,0)$, $(0,3.5)$ and the intersection

$$2x_1+x_2=8,\qquad x_1+2x_2=7.$$

Doubling the second and subtracting the first gives $3x_2=6$, so $x_2=2$ and $x_1=3$. The values are $0$, $16$, $10.5$ and $18$; the maximum is $18$ at $(3,2)$.

**(c) The dual.** Both primal variables are positive, so both dual constraints are tight:

$$2y_1+y_2=4,\qquad y_1+2y_2=3.$$

Doubling the second and subtracting the first gives $3y_2=2$, so $y_2=2/3$ and $2y_1=4-2/3=10/3$, hence $y_1=5/3$.

**(d) Verification.** The dual value is $8(5/3)+7(2/3)=40/3+14/3=54/3=18$, equal to the primal value. The complementary slackness conditions are:

| Condition | Value |
|---|---|
| $x_1>0\Rightarrow 2y_1+y_2=4$ | $10/3+2/3=4$ ✓ |
| $x_2>0\Rightarrow y_1+2y_2=3$ | $5/3+4/3=3$ ✓ |
| $s_1=0\Rightarrow y_1$ free | $y_1=5/3\ge0$ ✓ |
| $s_2=0\Rightarrow y_2$ free | $y_2=2/3\ge0$ ✓ |

Both slacks are zero because both constraints are tight at $(3,2)$: $2(3)+2=8$ and $3+2(2)=7$. Since the pair is feasible and the values agree, both are optimal by weak duality.

**18.** *Sensitivity ranges for Exercise 17*

**Strategy.** Write $x_B=A_B^{-1}b$, impose $x_B\ge0$ for changes in $b$, and impose $y=c_B^{T}A_B^{-1}\ge0$ for changes in $c$.

The optimal basis is $B=\{x_1,x_2\}$, with

$$A_B=\begin{pmatrix}2&1\\1&2\end{pmatrix},\qquad \det A_B=3,\qquad A_B^{-1}=\frac13\begin{pmatrix}2&-1\\-1&2\end{pmatrix}.$$

Thus

$$x_B=\frac13\begin{pmatrix}2b_1-b_2\\-b_1+2b_2\end{pmatrix}=\begin{pmatrix}(2b_1-b_2)/3\\ (2b_2-b_1)/3\end{pmatrix}.$$

At $(b_1,b_2)=(8,7)$ this gives $(3,2)$, as it should.

**Range of $b_1$.** Feasibility requires

$$\frac{2b_1-7}{3}\ge0,\qquad \frac{14-b_1}{3}\ge0,$$

so $3.5\le b_1\le14$. On that interval

$$z^{*}=4\left(\frac{2b_1-7}{3}\right)+3\left(\frac{14-b_1}{3}\right)=\frac{5b_1+14}{3}.$$

At $b_1=3.5$: $z=10.5$; at $b_1=14$: $z=28$. Both are checked below.

**Range of $b_2$.** Feasibility requires

$$\frac{16-b_2}{3}\ge0,\qquad \frac{2b_2-8}{3}\ge0,$$

so $4\le b_2\le16$. On that interval

$$z^{*}=4\left(\frac{16-b_2}{3}\right)+3\left(\frac{2b_2-8}{3}\right)=\frac{40+2b_2}{3}.$$

At $b_2=4$: $z=16$; at $b_2=16$: $z=24$.

**Range of $c_1$.** With $c_B=(c_1,3)$,

$$y_1=\frac{2c_1-3}{3},\qquad y_2=\frac{6-c_1}{3}.$$

Both must be non-negative, so $1.5\le c_1\le6$. On that interval the vertex $(3,2)$ stays optimal and

$$z^{*}=3c_1+3(2)=3c_1+6.$$

At $c_1=1.5$: $z=10.5$; at $c_1=6$: $z=24$.

**Range of $c_2$.** With $c_B=(4,c_2)$,

$$y_1=\frac{8-c_2}{3},\qquad y_2=\frac{2c_2-4}{3}.$$

Both must be non-negative, so $2\le c_2\le8$. On that interval

$$z^{*}=4(3)+2c_2=12+2c_2.$$

At $c_2=2$: $z=16$; at $c_2=8$: $z=28$.

**Endpoint checks by direct solution.**

* $b_1=3.5$: the optimum is $(0,3.5)$; $2(0)+3.5=3.5\le8$ ✓, $0+7=7$ ✓, and $z=3(3.5)=10.5$ ✓.
* $b_1=14$: the optimum is $(7,0)$; $14\le14$ ✓, $7\le7$ ✓, and $z=4(7)=28$ ✓.
* $b_2=4$: the optimum is $(4,0)$; $8\le8$ ✓, $4\le4$ ✓, and $z=16$ ✓.
* $b_2=16$: the optimum is $(0,8)$; $8\le8$ ✓, $16\le16$ ✓, and $z=24$ ✓.
* $c_1=1.5$: the optimum is $(0,3.5)$; $z=1.5(0)+3(3.5)=10.5$ ✓.
* $c_1=6$: the optimum is $(4,0)$; $z=6(4)=24$ ✓.
* $c_2=2$: the optimum is $(4,0)$; $z=4(4)=16$ ✓.
* $c_2=8$: the optimum is $(0,3.5)$; $z=8(3.5)=28$ ✓.

At each endpoint a different vertex ties with the current one, which is exactly what a zero reduced cost or zero dual variable signals.

**19.** *Branch-and-bound*

**Strategy.** Solve the LP relaxation, branch on a fractional variable, and prune by bound. A node is fathomed if it is infeasible, if its LP bound is no better than the incumbent, or if its LP solution is integral.

**Root LP.** The relaxation is $\max 3x_1+2x_2$ subject to $2x_1+x_2\le6$, $x_1+3x_2\le9$, $x\ge0$. Its vertices are

$$(0,0):0,\qquad (3,0):9,\qquad (0,3):6,\qquad \left(\frac95,\frac{12}{5}\right):\frac{51}{5}=10.2.$$

The last point is the intersection of the two constraints: $2(9/5)+12/5=30/5=6$ and $9/5+36/5=45/5=9$. The LP bound is $51/5$, attained at a fractional point.

**Branch on $x_2$.** Since $x_2=12/5=2.4$, create the subproblems $x_2\le2$ and $x_2\ge3$.

**Node $x_2\le2$.** With $x_2\le2$, the point $(2,2)$ is feasible: $2(2)+2=6$ and $2+6=8\le9$, with value $10$. The LP optimum of this node is exactly $(2,2)$: increasing $x_2$ beyond $2$ is forbidden, and at $x_2=2$ the first constraint gives $x_1\le2$. Hence the node is integral with value $10$, and the incumbent becomes $10$.

**Node $x_2\ge3$.** With $x_2\ge3$, the first constraint gives $2x_1\le0$, so $x_1=0$; the second gives $x_2\le3$, so $x_2=3$. The LP optimum is $(0,3)$ with value $6$. Since $6<10$, the node is fathomed by bound.

**Conclusion.** The incumbent $10$ at $(2,2)$ is optimal. The tree is

* root: bound $51/5=10.2$ at $(9/5,12/5)$;
* left child $x_2\le2$: bound $10$ at $(2,2)$ (integer, incumbent);
* right child $x_2\ge3$: bound $6$ at $(0,3)$ (pruned).

**Check.** The integer points near the optimum are $(2,2)$ with value $10$, $(3,0)$ with $9$, $(1,2)$ with $7$, $(2,1)$ with $8$ and $(0,3)$ with $6$. None exceeds $10$, and $(2,2)$ is feasible. The gap between the root bound $10.2$ and the integer optimum $10$ is $0.2$.

**20.** *A transportation problem*

**(a) Balance.** Supplies: $25+35=60$. Demands: $15+25+20=60$. The problem is balanced, so it is feasible.

**(b) North-west corner.** Fill $(1,1)$ with $\min(25,15)=15$. Supply left at source 1: $10$; demand 1 is met. Move right: $(1,2)=\min(10,25)=10$; source 1 is exhausted. Move down: $(2,2)=\min(35,15)=15$; demand 2 is met. Move right: $(2,3)=\min(20,20)=20$. The basic cells are $(1,1),(1,2),(2,2),(2,3)$, with cost

$$15(4)+10(6)+15(3)+20(7)=60+60+45+140=305.$$

**(c) Optimality test.** With $u_1=0$: from $(1,1)$, $v_1=4$; from $(1,2)$, $v_2=6$; from $(2,2)$, $u_2=3-6=-3$; from $(2,3)$, $v_3=7-(-3)=10$. The non-basic reduced costs are

$$(1,3):\ 8-0-10=-2,\qquad (2,1):\ 5-(-3)-4=4.$$

The negative reduced cost at $(1,3)$ means the solution improves by entering that cell.

**Improving cycle.** The cycle is $(1,3)\to(2,3)\to(2,2)\to(1,2)\to(1,3)$, with signs $+,-,+,-$. The step is

$$\theta=\min(x_{23},x_{12})=\min(20,10)=10.$$

The new solution is

$$x_{11}=15,\quad x_{13}=10,\quad x_{22}=25,\quad x_{23}=10,$$

and $x_{12}=0$. Its cost is

$$15(4)+10(8)+25(3)+10(7)=60+80+75+70=285.$$

**Second test.** With $u_1=0$: $v_1=4$, $v_3=8$, $u_2=7-8=-1$, $v_2=3-(-1)=4$. The non-basic reduced costs are

$$(1,2):\ 6-0-4=2,\qquad (2,1):\ 5-(-1)-4=2.$$

Both are positive, so the solution is optimal with cost $285$.

**(d) Uniqueness.** Every non-basic cell has a strictly positive reduced cost, so no alternative optimal basis exists; the optimal solution is unique.

**Check.** Supplies: $x_{11}+x_{12}+x_{13}=15+0+10=25$ and $x_{21}+x_{22}+x_{23}=0+25+10=35$. Demands: $x_{11}+x_{21}=15$, $x_{12}+x_{22}=0+25=25$, and $x_{13}+x_{23}=10+10=20$. The cost is $285$, lower than the initial $305$.

**21.** *A seven-day shift-scheduling model*

**Strategy.** Index the patterns by the first day of the two-day break. A pattern covers every day except its two break days, so the coverage constraint on day $t$ excludes exactly two patterns.

Let $x_j\ge0$ be the number of employees whose two consecutive days off begin on day $j$, with indices modulo 7. Pattern $j$ has days $j$ and $j+1$ off.

Day $t$ is worked by every pattern except $j=t$ (day $t$ is its first off day) and $j=t-1$ (day $t$ is its second off day). Hence the coverage constraint is

$$\sum_{j=1}^{7}x_j-x_t-x_{t-1}\ge r_t,\qquad t=1,\dots,7,$$

with $x_0=x_7$. The model is

$$\min\ \sum_{j=1}^{7}x_j\quad\text{s.t.}\quad \sum_{j=1}^{7}x_j-x_t-x_{t-1}\ge r_t\ \ (t=1,\dots,7),\quad x_j\ge0\ \text{integer}.$$

**Check.** For $t=1$, the constraint is $x_1+x_2+\dots+x_7-x_1-x_7=x_2+\dots+x_6\ge r_1$, so the employees who work Monday are exactly those whose break does not include Monday, namely patterns $2,3,4,5,6$. This matches the definition. The objective counts every employee exactly once.

**22.** *A blending problem with three nutrients*

**Strategy.** Formulate, draw the three half-planes, list the vertices, and read the dual from the binding constraints.

The model is

$$\min z=3x+2y\quad\text{s.t.}\quad x+2y\ge8,\quad 2x+y\ge10,\quad x+y\ge5,\quad x,y\ge0.$$

**Vertices.** The pairwise intersections are:

* $x+2y=8$ and $2x+y=10$: multiplying the first by $2$ gives $2x+4y=16$; subtracting the second gives $3y=6$, so $y=2$, $x=4$. This satisfies $x+y=6\ge5$.
* $x+2y=8$ and $x+y=5$: $y=3$, $x=2$. This violates $2x+y=7<10$, so it is infeasible.
* $2x+y=10$ and $x+y=5$: $x=5$, $y=0$. This violates $x+2y=5<8$, so it is infeasible.

The axis vertices are $(0,10)$, which satisfies all three constraints ($20\ge8$, $10\ge10$, $10\ge5$), and $(8,0)$, which satisfies $8\ge8$, $16\ge10$ and $8\ge5$. The third axis candidate $(5,0)$ fails the protein constraint, and $(0,8)$ fails the carbohydrate constraint.

| Vertex | $z=3x+2y$ |
|---|---|
| $(0,10)$ | $20$ |
| $(4,2)$ | $12+4=16$ |
| $(8,0)$ | $24$ |

The minimum is $16$ at $(4,2)$. The binding constraints are protein ($4+4=8$) and carbohydrate ($8+2=10$); fibre has slack $6-5=1$.

**Dual.** The dual is

$$\max\ 8u+10v+5w\quad\text{s.t.}\quad u+2v+w\le3,\quad 2u+v+w\le2,\quad u,v,w\ge0.$$

Since $x,y>0$, both dual constraints are tight. Since the fibre constraint is slack, $w=0$. Solving

$$u+2v=3,\qquad 2u+v=2$$

gives $v=4/3$ and $u=1/3$. The dual value is

$$8\left(\frac13\right)+10\left(\frac43\right)+5(0)=\frac83+\frac{40}{3}=\frac{48}{3}=16,$$

matching the primal. Protein is worth $1/3$ per unit, carbohydrate $4/3$ per unit, and fibre nothing at this optimum.

**Check.** $(4,2)$: $4+4=8$, $8+2=10$, $4+2=6\ge5$, and $z=12+4=16$. The dual point is feasible: $(1/3)+2(4/3)=3$ and $2(1/3)+4/3=2$.

## Advanced

**23.** *Proof of the fundamental theorem*

**Statement to prove.** Let $P=\{x\in\mathbb{R}^{n}:Ax=b,\ x\ge0\}$ with $\operatorname{rank}A=m$. If $\max\{c^{T}x:x\in P\}$ has an optimal solution, then it has an optimal basic feasible solution.

**Strategy.** Take an optimal solution with the smallest possible number of positive components. If its support columns were dependent, a null-space direction would let us move to another optimal solution with fewer positive components, contradicting minimality.

**Existence of a minimal-support optimum.** The set $S$ of optimal solutions is non-empty. The map $x\mapsto|\{j:x_j>0\}|$ takes values in the non-negative integers, so it attains a minimum on $S$; choose $x^{*}\in S$ attaining it.

**Suppose the support columns are dependent.** Let $N=\{j:x_j^{*}>0\}$. If the columns $\{A_j:j\in N\}$ are linearly dependent, there is $d\neq0$ with $\sum_{j\in N}d_jA_j=0$. Extend $d$ by zero outside $N$; then $Ad=0$ and $d_j=0$ for $j\notin N$.

For small $\theta>0$, both $x^{*}+\theta d$ and $x^{*}-\theta d$ are non-negative: outside $N$ both equal $x^{*}_j=0$, and on $N$ continuity and $x^{*}_j>0$ keep the entries positive for small $\theta$. Both satisfy $A(x^{*}\pm\theta d)=b$. Since $x^{*}$ is optimal,

$$c^{T}(x^{*}+\theta d)\le c^{T}x^{*},\qquad c^{T}(x^{*}-\theta d)\le c^{T}x^{*}.$$

Dividing by $\theta>0$ gives $c^{T}d\le0$ and $-c^{T}d\le0$, hence $c^{T}d=0$. Therefore every point $x^{*}+\theta d$ is optimal as long as it is feasible.

**Choosing the step.** Since $d\neq0$, either $d$ or $-d$ has a negative component; replace $d$ by $-d$ if necessary so that $d$ has one. Set

$$\bar\theta=\min_{j:\,d_j<0}\frac{x_j^{*}}{-d_j}>0.$$

At $\bar\theta$, every component with $d_j\ge0$ is still non-negative (it was non-negative and increases), and the component attaining the minimum is exactly zero. Components outside $N$ remain zero. Hence $x^{*}+\bar\theta d$ is feasible, optimal, and has strictly fewer positive components than $x^{*}$: at least one component has vanished, and no new positive component has appeared.

This contradicts the choice of $x^{*}$. Hence the support columns are independent, and $x^{*}$ is a basic feasible solution. $\blacksquare$

**Why the argument is complete.** A feasible point whose positive columns are independent is a bfs: the independent set can be extended to a basis of $\mathbb{R}^{m}$ using columns of $A$, and the remaining variables are zero. Conversely every bfs has this property. The theorem therefore reduces the continuous problem to a finite set of candidates.

**Check of the logic.** The proof never uses boundedness of $P$, only that an optimal solution exists. It also does not claim uniqueness: if several vertices are optimal, the minimal-support choice selects one of them.

**24.** *Proof of weak duality*

**Statement.** If $x$ is feasible for $\max\{c^{T}x:Ax\le b,\ x\ge0\}$ and $y$ is feasible for $\min\{b^{T}y:A^{T}y\ge c,\ y\ge0\}$, then $c^{T}x\le b^{T}y$.

**Proof.** Because $x\ge0$ and $A^{T}y\ge c$, multiplying the vector inequality $A^{T}y-c\ge0$ by the non-negative vector $x^{T}$ gives

$$x^{T}(A^{T}y-c)\ge0,\qquad\text{that is,}\qquad x^{T}A^{T}y\ge x^{T}c=c^{T}x.$$

Because $y\ge0$ and $b-Ax\ge0$, multiplying by $y^{T}\ge0$ gives

$$y^{T}(b-Ax)\ge0,\qquad\text{that is,}\qquad b^{T}y\ge y^{T}Ax.$$

Finally $y^{T}Ax=(Ax)^{T}y=x^{T}A^{T}y$. Combining,

$$c^{T}x\le x^{T}A^{T}y\le b^{T}y.$$

$\blacksquare$

**Where each hypothesis is used.** $x\ge0$ is needed to multiply $A^{T}y\ge c$ by $x^{T}$ without reversing the inequality. $y\ge0$ is needed to multiply $Ax\le b$ by $y^{T}$ without reversing it. $Ax\le b$ and $A^{T}y\ge c$ are the feasibility conditions themselves. If any of the four sign conditions fails, the chain breaks and the inequality need not hold.

**Consequence.** Every dual feasible $y$ bounds the primal from above. If the primal is unbounded, no dual feasible $y$ can exist, so the dual is infeasible.

**25.** *Proof of complementary slackness*

**Statement.** Let $x$ be primal feasible and $y$ dual feasible for the symmetric pair. Then both are optimal if and only if

$$y_i(b_i-a_i^{T}x)=0\ \ \forall i,\qquad x_j((A^{T}y)_j-c_j)=0\ \ \forall j.$$

**Proof of the "only if" direction.** Suppose both are optimal. By strong duality $c^{T}x=b^{T}y$. The chain of weak duality is

$$c^{T}x\le x^{T}A^{T}y\le b^{T}y.$$

The two ends are equal, so both intermediate inequalities are equalities. In particular

$$x^{T}(A^{T}y-c)=0,\qquad y^{T}(b-Ax)=0.$$

Every term of the first sum is $x_j((A^{T}y)_j-c_j)$ with $x_j\ge0$ and $(A^{T}y)_j-c_j\ge0$, so each term is non-negative; a sum of non-negative terms is zero only if every term is zero. This gives the second family of conditions. The same argument applied to $y^{T}(b-Ax)$, whose terms are $y_i(b_i-a_i^{T}x)\ge0$, gives the first family.

**Proof of the "if" direction.** Suppose the conditions hold. Then

$$y^{T}(b-Ax)=\sum_i y_i(b_i-a_i^{T}x)=0,\qquad x^{T}(A^{T}y-c)=\sum_j x_j((A^{T}y)_j-c_j)=0.$$

Since $y^{T}(b-Ax)=b^{T}y-y^{T}Ax$ and $x^{T}(A^{T}y-c)=x^{T}A^{T}y-c^{T}x$, and since $y^{T}Ax=x^{T}A^{T}y$, the two equalities give

$$b^{T}y=y^{T}Ax=c^{T}x.$$

By weak duality, no primal feasible value exceeds $c^{T}x$ and no dual feasible value is below $b^{T}y$. Hence both are optimal. $\blacksquare$

**Why strong duality is not needed for "if".** The "if" direction uses only weak duality: equality of the primal and dual objective values sandwiches both between the same two numbers. Strong duality is used only in the "only if" direction, to know that the optimal values agree.

**26.** *The dual of the dual*

**Strategy.** Convert the dual into a maximisation with $\le$ constraints, apply Definition 7.5, and simplify.

The primal is

$$\max\ c^{T}x\quad\text{s.t.}\quad Ax\le b,\quad x\ge0.$$

Its dual is

$$\min\ b^{T}y\quad\text{s.t.}\quad A^{T}y\ge c,\quad y\ge0.$$

Write the dual as a maximisation:

$$\max\ -b^{T}y\quad\text{s.t.}\quad -A^{T}y\le-c,\quad y\ge0.$$

Apply Definition 7.5 with objective vector $-b$, constraint matrix $-A^{T}$ and right-hand side $-c$. The dual of this problem is

$$\min\ (-c)^{T}z\quad\text{s.t.}\quad (-A^{T})^{T}z\ge-b,\quad z\ge0.$$

Since $(-A^{T})^{T}=-A$, this is

$$\min\ -c^{T}z\quad\text{s.t.}\quad -Az\ge-b,\quad z\ge0.$$

Multiplying the constraint by $-1$ reverses it, giving $Az\le b$. Maximising $-c^{T}z$ is the same as minimising $c^{T}z$, so the problem is

$$\max\ c^{T}z\quad\text{s.t.}\quad Az\le b,\quad z\ge0,$$

which is the primal with $z$ renamed $x$. $\blacksquare$

**Check of signs.** The two sign reversals (writing min as max, and multiplying $-Az\ge-b$ by $-1$) cancel. Omitting either one produces the wrong dual, which is why the conversion should be done in explicit steps.

**27.** *Strong duality from the final tableau*

**Setting.** Consider the standard-form primal $\max c^{T}x$ subject to $Ax=b$, $x\ge0$, where $A$ contains the slack columns and the initial basis is feasible. Suppose the simplex method terminates at an optimal basis $B$.

**Dual feasibility.** Define $y^{T}=c_B^{T}B^{-1}$. For every column $A_j$, the reduced cost in the final tableau is

$$\bar c_j=c_B^{T}B^{-1}A_j-c_j=y^{T}A_j-c_j.$$

At optimality $\bar c_j\ge0$ for every non-basic $j$, and $\bar c_j=0$ for every basic $j$ because $A_B^{-1}A_j=e_j$ and $c_B^{T}e_j=c_j$. Hence $A^{T}y\ge c$.

For a slack column $e_i$, the objective coefficient is $0$, so its reduced cost is $\bar c_{e_i}=y^{T}e_i=y_i$. Since the tableau is optimal, $\bar c_{e_i}\ge0$, hence $y\ge0$. Thus $y$ is dual feasible.

**Equality of values.** Since $x_B=B^{-1}b$,

$$b^{T}y=b^{T}(B^{-1})^{T}c_B=(B^{-1}b)^{T}c_B=x_B^{T}c_B=c^{T}x.$$

By weak duality, no dual feasible value is below any primal feasible value; since $y$ attains the primal value, both are optimal and the values are equal. $\blacksquare$

**Why this does not cover the other cases.** The argument presupposes that the simplex method terminates at an optimal basis. If the primal is unbounded, the method instead finds a column with no positive entry and never produces an optimal $B$; if the primal is infeasible, no basis is feasible to begin with. In those cases strong duality is replaced by the case analysis of §7.8: unbounded primal forces the dual to be infeasible (weak duality), and an infeasible primal may have a dual that is unbounded or infeasible. The tableau proof establishes the finite case, and weak duality plus the case table completes the picture.

**28.** *Vertices and bounded polyhedra*

**Statement.** Let $P$ be a non-empty bounded polyhedron. Then every point of $P$ is a convex combination of vertices, and a linear function attains its maximum at a vertex.

**Proof.** By the cited representation theorem for bounded polyhedra, $P$ has at least one vertex and

$$P=\operatorname{conv}\{v_1,\dots,v_k\},$$

where $v_1,\dots,v_k$ are its vertices. Take any $x\in P$. Then there are $\lambda_i\ge0$ with $\sum_i\lambda_i=1$ and $x=\sum_i\lambda_iv_i$. Linearity gives

$$c^{T}x=\sum_i\lambda_i\,c^{T}v_i\le\left(\sum_i\lambda_i\right)\max_i c^{T}v_i=\max_i c^{T}v_i.$$

Hence the maximum of $c^{T}x$ over $P$ equals the maximum over the finite set of vertices, and it is attained at a vertex. By Lemma 7.2 a vertex is a basic feasible solution, so an optimal bfs exists.

**Edge cases.** If $P$ is empty, the statement is vacuous; if $P$ is a single point, that point is the only vertex. Boundedness is essential: on the unbounded half-plane $x\ge0$, the linear function $x$ has no maximum at a vertex because there are no vertices. $\blacksquare$

**29.** *A degenerate basis*

**(a) Three active constraints.** At $(2,2)$, all three constraints are tight:

$$2+2=4,\qquad 2=2,\qquad 2=2.$$

In standard form, $x_1+x_2+s_1=4$, $x_1+s_2=2$, $x_2+s_3=2$, the slacks are $s_1=s_2=s_3=0$. The basis $\{x_1,x_2,s_1\}$ has basic variables $x_1,x_2,s_1$; solving the three equations with $s_2=s_3=0$ gives $x_1=2$, $x_2=2$, $s_1=4-2-2=0$. The basic variable $s_1$ is zero, so the basis is degenerate.

**(b) Tableau.** The rows in canonical form for the basis $\{x_1,x_2,s_1\}$ are

$$x_1+s_2=2,\qquad x_2+s_3=2,\qquad s_1-s_2-s_3=0.$$

The third row comes from $s_1=4-x_1-x_2=4-(2-s_2)-(2-s_3)=s_2+s_3$. The objective is

$$z=2x_1+x_2=2(2-s_2)+(2-s_3)=6-2s_2-s_3,$$

so the $z$ row is $z+2s_2+s_3=6$. The basic solution is $x_1=x_2=2$, $s_1=0$, $s_2=s_3=0$, with $z=6$.

**(c) Zero-length pivots.** If a non-basic variable had a negative reduced cost and a positive entry in the row of a zero basic variable, the ratio for that row would be $0/(\text{positive})=0$. The minimum ratio would then be zero, so the entering variable would increase by zero, the basis would change, and the objective would stay the same. A sequence of such zero-length pivots can return to a basis already visited: that is cycling. Bland's rule (smallest-index entering and leaving variables) prevents it. In the tableau above the reduced costs are already non-negative, so this particular basis is optimal and no pivot is needed; the example exhibits the degeneracy, not a cycle.

**Check.** $x_1=x_2=2$ satisfies all constraints with equality, and $z=2(2)+2=6$. The point is the corner of the square $0\le x_1,x_2\le2$, so it is optimal for the given objective.

**30.** *Total unimodularity implies integral basic solutions*

**Statement.** Let $A$ be totally unimodular, $b$ integral, and consider $Ax\le b$, $x\ge0$. Then every basic feasible solution is integral.

**Proof.** Add slacks to obtain $[A\ \ I]\binom{x}{s}=b$, with $x,s\ge0$. The matrix $[A\ \ I]$ is totally unimodular: appending an identity block preserves total unimodularity, because every square submatrix either lies in $A$ (determinant $0,\pm1$), lies in $I$ (determinant $0$ or $1$), or has a column of the identity, which can be expanded to a smaller determinant of the same type.

Let $B$ be a basis of $[A\ \ I]$. Then $x_B=B^{-1}b$. By Cramer's rule, the $i$-th component is

$$(x_B)_i=\frac{\det B_i}{\det B},$$

where $B_i$ is $B$ with its $i$-th column replaced by $b$. Since $B$ and $b$ are integral, both determinants are integers. Since $B$ is a square submatrix of a totally unimodular matrix, $\det B\in\{0,\pm1\}$; invertibility excludes $0$, so $\det B=\pm1$. Hence $(x_B)_i$ is an integer. $\blacksquare$

**Consequence.** For a transportation problem with integer supplies and demands, the LP optimum is integral without branch-and-bound: the constraint matrix is totally unimodular (Exercise 36) and $b$ is integral.

## Challenge

**31.** *Unbounded primal and infeasible dual*

**(a) Proof.** Suppose the primal is unbounded above and the dual has a feasible $y$. By weak duality, $c^{T}x\le b^{T}y$ for every primal feasible $x$. The right-hand side is a fixed number, so the primal objective is bounded above by $b^{T}y$, contradicting unboundedness. Hence the dual is infeasible. $\blacksquare$

**(b) Example.** Take the primal

$$\max\ x\quad\text{s.t.}\quad -x\le0,\quad x\ge0.$$

It is feasible ($x=0$) and unbounded: $x=t$ gives $z=t\to\infty$. In the symmetric form $A=(-1)$, $b=0$, $c=1$, so the dual is

$$\min\ 0\cdot y\quad\text{s.t.}\quad -y\ge1,\quad y\ge0.$$

The constraints give $y\le-1$ and $y\ge0$, which are incompatible; the dual is infeasible. This is exactly the pattern predicted by (a).

**(c) Why the converse fails.** The implication "primal unbounded $\Rightarrow$ dual infeasible" does not reverse: both problems can be infeasible. Take

$$\max\ 2x_1-x_2\quad\text{s.t.}\quad x_1-x_2\le1,\quad -x_1+x_2\le-2,\quad x\ge0.$$

Adding the two constraints gives $0\le-1$, so the primal is infeasible. The dual is

$$\min\ y_1-2y_2\quad\text{s.t.}\quad y_1-y_2\ge2,\quad -y_1+y_2\ge-1,\quad y\ge0.$$

The constraints say $y_1-y_2\ge2$ and $y_1-y_2\le1$, which are incompatible, so the dual is infeasible too. Hence "dual infeasible" does not force "primal unbounded"; it may mean that both are infeasible.

**Check.** The primal infeasibility is immediate from $0\le-1$; the dual infeasibility is immediate from $2\le y_1-y_2\le1$.

**32.** *The optimal set is a face*

**Setting.** Let $P$ be a polyhedron, $c\neq0$, and $S=\{x\in P:c^{T}x=z^{*}\}$ the set of optimal solutions, assumed non-empty.

**Convexity.** If $u,v\in S$ and $0\le\lambda\le1$, then $\lambda u+(1-\lambda)v\in P$ because $P$ is convex, and

$$c^{T}(\lambda u+(1-\lambda)v)=\lambda c^{T}u+(1-\lambda)c^{T}v=\lambda z^{*}+(1-\lambda)z^{*}=z^{*}.$$

Hence the convex combination belongs to $S$, so $S$ is convex.

**Face property.** A face of $P$ is a convex subset $F\subseteq P$ such that whenever $x,y\in P$ and a point of the open segment $(x,y)$ lies in $F$, both $x$ and $y$ lie in $F$. Let $x,y\in P$ and suppose $z=\lambda x+(1-\lambda)y\in S$ with $0<\lambda<1$. Then

$$z^{*}=c^{T}z=\lambda c^{T}x+(1-\lambda)c^{T}y.$$

Since $c^{T}x\le z^{*}$ and $c^{T}y\le z^{*}$ (by optimality of $z^{*}$), a weighted average can equal $z^{*}$ only if both terms equal $z^{*}$. Hence $x,y\in S$, and $S$ is a face.

**Segment property.** The convexity argument already shows that if $u,v\in S$, the whole segment $[u,v]$ lies in $S$.

**Examples.** For $\max 2x_1+4x_2$ subject to $x_1+2x_2\le8$, $x_1+x_2\le5$, the optimal set is the edge from $(0,4)$ to $(2,3)$ (Exercise 16), a one-dimensional face. For $\max 4x_1+3x_2$ subject to $2x_1+x_2\le8$, $x_1+2x_2\le7$, the optimum $(3,2)$ is the unique optimal vertex (Exercise 17), so $S$ is a single point, a zero-dimensional face. $\blacksquare$

**33.** *A zero shadow price with a one-sided cost*

**The value function.** For the LP of §7.6,

$$\max\ 3x_1+5x_2\quad\text{s.t.}\quad x_1\le b_1,\quad 2x_2\le12,\quad 3x_1+2x_2\le18,\quad x\ge0,$$

the final basis gives the optimal solution for $b_1$ near $4$. For $b_1\ge2$ the basis $\{s_1,x_2,x_1\}$ stays feasible, with $x_1=2$, $x_2=6$, $s_1=b_1-2$, and $z=36$. For $0\le b_1\le2$, the constraint $x_1\le b_1$ binds and the second constraint binds too: $x_1=b_1$, $x_2=6$, with slack in the third constraint. Then

$$z^{*}(b_1)=3b_1+5(6)=3b_1+30.$$

At $b_1=2$ both formulas give $36$, so the value function is continuous.

**Derivatives.** For $b_1>2$ the derivative is $0$; for $b_1<2$ it is $3$. At $b_1=2$ the right derivative is $0$ and the left derivative is $3$. The one-sided derivatives differ, so $z^{*}$ is not differentiable there; the value function is concave, with a kink.

**Interpretation.** The shadow price $y_1=0$ is the *right-hand* derivative: adding capacity to a constraint that already has slack is worthless. But removing capacity below $b_1=2$ forces $x_1$ down and costs $3$ per unit of lost capacity. A zero shadow price therefore does not mean that the constraint can be deleted at no cost; it means only that the constraint is not binding at the current optimum. The full sensitivity statement is the pair of one-sided derivatives, or equivalently the interval of right-hand sides over which the basis stays optimal.

**Check.** At $b_1=0$: $x_1=0$, $x_2=6$, $z=30=3(0)+30$. At $b_1=2$: $x_1=2$, $x_2=6$, $z=36=3(2)+30$. Both satisfy the constraints: for $b_1=0$, $x_1=0\le0$, $2x_2=12$, $3x_1+2x_2=12\le18$; for $b_1=2$, $x_1=2\le2$, $2x_2=12$, $6+12=18$.

**34.** *Termination of branch-and-bound*

**Statement.** Consider an integer program with a bounded feasible region and rational data. Then branch-and-bound, as described in §7.12, examines finitely many nodes and terminates.

**Boundedness gives finite ranges.** Because the feasible region is bounded, there are numbers $l_j,u_j$ with $l_j\le x_j\le u_j$ for every feasible point and every $j$. With rational data, the bounds can be taken rational; the integer values available to $x_j$ form a finite set, and the total number of integer points in the box is finite.

**Each branch shrinks a range.** At a node, if the LP solution has a fractional component $x_j=v$, the two children impose $x_j\le\lfloor v\rfloor$ and $x_j\ge\lceil v\rceil$. In the first child the upper bound on $x_j$ decreases to at most $\lfloor v\rfloor<v$; in the second the lower bound increases to at least $\lceil v\rceil>v$. Both new bounds are integers, and the excluded interval contains the fractional value $v$.

**Finite depth.** Along any path from the root, each branching strictly reduces the integer range of one variable: the upper bound decreases by at least $1$, or the lower bound increases by at least $1$. The quantity

$$\sum_{j=1}^{n}(u_j-l_j)$$

is a non-negative integer and decreases by at least $1$ at each branching, so no path can contain more than $\sum_j(u_j-l_j)+1$ branchings. The tree therefore has finite depth.

**Finite breadth.** Each node has at most two children. A tree of finite depth with at most two children per node has at most $2^{D+1}-1$ nodes, where $D$ is the depth bound. Hence the tree is finite, and the algorithm terminates after examining finitely many nodes.

**Why rationality matters.** With rational data the LP optima are rational (they solve rational linear systems), so the comparisons $\le\lfloor v\rfloor$ and $\ge\lceil v\rceil$ are exact and the branching is well defined. With irrational data, floating-point comparisons can be ambiguous; exact rational arithmetic removes the difficulty.

**Check.** The argument does not claim a small number of nodes; it only proves finiteness. The worst case can indeed be exponential, which is consistent with the NP-hardness of integer programming.

**35.** *Uniqueness of the dual solution*

**Statement.** If the primal optimal basic feasible solution is non-degenerate, then the optimal dual solution is unique.

**Proof.** Let $B$ be an optimal basis and suppose the corresponding bfs is non-degenerate, so every basic variable is strictly positive. Complementary slackness applies to the $m$ basic variables: for each basic $j$, $x_j>0$, hence the $j$-th dual constraint is tight:

$$A_j^{T}y=c_j.$$

Stacking these equations for the $m$ basic columns gives $A_B^{T}y=c_B$. Because $B$ is a basis, $A_B$ is invertible, so

$$y=(A_B^{T})^{-1}c_B=(A_B^{-1})^{T}c_B$$

is the unique solution. Any optimal dual solution must satisfy these $m$ independent equations, so it equals this $y$. $\blacksquare$

**Why the converse fails.** Degeneracy does not force multiple dual solutions. Consider

$$\max\ x_1+x_2\quad\text{s.t.}\quad x_1+x_2\le1,\quad x_1\le1,\quad x_2\le1,\quad x\ge0.$$

At the optimal point $(1,0)$, the basis $\{x_1,s_2,s_3\}$ has basic values $x_1=1$, $s_2=0$, $s_3=1$, so it is degenerate. The dual is

$$\min\ y_1+y_2+y_3\quad\text{s.t.}\quad y_1+y_2\ge1,\quad y_1+y_3\ge1,\quad y\ge0.$$

Complementary slackness gives $y_1+y_2=1$ (because $x_1>0$) and $y_3=0$ (because $s_3>0$). The second dual constraint then reads $y_1\ge1$. Together with $y_1+y_2=1$ and $y_2\ge0$, this forces $y_1=1$ and $y_2=0$. Hence $y=(1,0,0)$ is the unique optimal dual solution, even though the primal optimum is degenerate.

**Check.** The dual point is feasible: $1+0\ge1$ and $1+0\ge1$. Its value is $1$, equal to the primal value $x_1+x_2=1$. Uniqueness follows from the forced equalities.

**36.** *Total unimodularity of the transportation matrix*

**Statement.** The constraint matrix of the transportation problem is totally unimodular.

**Structure of the matrix.** Number the source rows $1,\dots,p$ and the destination rows $1,\dots,q$. The variable $x_{ij}$ has a column with a $1$ in source row $i$ and a $1$ in destination row $j$, and zeros elsewhere. This is the incidence matrix of a bipartite graph whose two parts are the sources and the destinations.

**Proof by induction on the size of a square submatrix.** Let $M$ be a square submatrix. If $M$ has a column with at most one non-zero entry, expand the determinant along that column: the determinant is $\pm$ the determinant of a smaller submatrix of the same type. By induction, that smaller determinant is $0$ or $\pm1$, so $\det M\in\{0,\pm1\}$.

If every column of $M$ has exactly two non-zero entries, both equal to $1$, then each column has one $1$ among the source rows and one $1$ among the destination rows. Summing all source rows gives the same vector as summing all destination rows (each column contributes exactly one $1$ to each sum). Hence the rows of $M$ are linearly dependent, and $\det M=0$.

The base case is a $1\times1$ matrix, whose entry is $0$ or $1$. By induction every square submatrix has determinant $0$, $1$ or $-1$, which is the definition of total unimodularity. $\blacksquare$

**Integrality of optimal solutions.** With integer supplies and demands, the right-hand side $b$ is integral. By Exercise 30, every basic feasible solution of the transportation LP is integral. Hence the continuous optimum is an integer shipping plan, and no branch-and-bound is required. This is why transportation problems are solved as LPs even when the goods are indivisible.
