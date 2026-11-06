# Lagrange Multipliers — Exercises

> [Lagrange Multipliers](README.md) · 36 problems · Beginner → Challenge · Solutions: [solutions.md](solutions.md)

Work through the problems in order. Problems 1–12 build fluency with the Lagrange equations and the geometry; 13–22 apply the method to economics, engineering and KKT problems; 23–30 are proofs of the main theorems; 31–36 are challenge problems on degeneracy, uniqueness of multipliers and global classification. Attempt every problem before opening [solutions.md](solutions.md), and **check every candidate against the constraints and the second-order conditions** — in constrained optimisation the constraint check is decisive.

Conventions: all functions are at least $C^{1}$, and $C^{2}$ where second-order conditions are used. "Extremise" means find all local maxima and minima and classify them; "optimise" means find the global optimum on the stated feasible set. Unless a problem says otherwise, variables may take either sign, and the constraint set is the one displayed.

## Beginner

**1.** *(§7.2, §7.4)* Find the point of the line $5x+12y=26$ closest to the origin. Use the Lagrange multiplier method, state the multiplier, and verify that it equals the derivative of the squared distance with respect to the right-hand side.

**2.** *(§7.3)* Maximise $f(x,y)=xy$ subject to $x+2y=4$, $x,y\ge0$. Find the multiplier and verify that the point is feasible.

**3.** *(§7.3)* Maximise $f(x,y)=x+y$ subject to $x^{2}+y^{2}=2$.

**4.** *(§7.3)* Minimise $f(x,y,z)=x^{2}+y^{2}+z^{2}$ subject to $x+2y+2z=9$.

**5.** *(§7.3)* Maximise $f(x,y,z)=xyz$ subject to $x+y+z=6$ and $x,y,z\ge0$. Explain why the boundary cases $x=0$, $y=0$ or $z=0$ cannot give the maximum.

**6.** *(§7.3)* Extremise $f(x,y)=x^{2}+y^{2}$ subject to $xy=1$. Does a maximum exist?

**7.** *(§7.3)* Write the Lagrangian and the first-order conditions for maximising $f(x,y)=x^{2}y$ subject to $x+y=1$. Do not solve the system.

**8.** *(§7.3)* Find all stationary points of $f(x,y)=x+y$ subject to $x^{2}+y^{2}=4$ and classify them.

**9.** *(§7.6)* Use the KKT conditions to minimise $f(x,y)=(x-2)^{2}+(y-2)^{2}$ subject to $x+y\le2$. State the multiplier and verify its sign.

**10.** *(§7.6)* Use the KKT conditions to minimise $f(x,y)=(x-4)^{2}+(y-1)^{2}$ subject to $x+y\le3$. State the multiplier and verify its sign.

**11.** *(§7.4)* For the problem $\max xy$ subject to $x+y=b$, $x,y\ge0$, show that the optimal value is $V(b)=b^{2}/4$ and the multiplier is $\lambda=b/2$. Verify the shadow-price formula numerically at $b=6$ and $b=6.2$.

**12.** *(§7.4, §7.6)* Explain the sign of the multiplier in each of the following cases, using the value function: (a) maximisation with a resource constraint $h(x)\le b$; (b) minimisation with a capacity constraint $h(x)\le b$. Give a one-sentence economic interpretation of each sign.

## Intermediate

**13.** *(§7.3, §7.4)* Maximise the utility $U(x,y)=x^{1/2}y^{1/2}$ subject to the budget $2x+3y=60$. Find the optimal bundle, the utility, and the multiplier. Verify that $\lambda=U/60$.

**14.** *(§7.3, §7.4)* Minimise the cost $C=2L+4K$ subject to the production constraint $L^{1/3}K^{2/3}=8$. Find $L$, $K$, the minimum cost and the multiplier. Verify that the multiplier equals the marginal cost.

**15.** *(§7.8)* Maximise the volume of a closed rectangular box with surface area $54$. Find the dimensions, the volume and the multiplier, and check the result by the AM–GM inequality.

**16.** *(§7.5)* Maximise $f(x,y,z)=x+y+z$ subject to $x^{2}+y^{2}+z^{2}=4$ and $x+y=0$. Find the multipliers $\lambda$ and $\mu$ and classify the candidate points.

**17.** *(§7.6)* Minimise $f(x,y)=(x-4)^{2}+(y-4)^{2}$ subject to $x+y\le4$ and $x\le1$. Write the KKT conditions with two inequality multipliers, solve them, and identify the active constraints.

**18.** *(§7.8)* Extremise $f(x,y)=xy$ subject to $x^{2}+y^{2}=4$. Find all stationary points and classify each with the bordered Hessian.

**19.** *(§7.9)* Consider the problem of maximising $f(x,y)=y$ subject to $x^{2}=y^{3}$. Show that the origin is a local minimum of $f$ on the constraint and that the Lagrange condition fails there. Explain which hypothesis of the theorem fails.

**20.** *(§7.4, §7.6)* For the problem of minimising $(x-1)^{2}+(y-1)^{2}$ subject to $x+y\le1+b$, compute the value function $V(b)$ for $b<1$, find $V'(0)$, and verify that $V'(0)=-\mu$, where $\mu$ is the KKT multiplier at $b=0$.

**21.** *(§7.4)* Prove the shadow-price theorem for one equality constraint: if $x(b)$ and $\lambda(b)$ are $C^{1}$ and $x(b)$ is optimal for $g(x)=b$, then $V'(b)=\lambda(b)$.

**22.** *(§7.5, §7.8)* A rectangular box is inscribed in a sphere of radius $R$: maximise $8xyz$ subject to $x^{2}+y^{2}+z^{2}=R^{2}$, $x,y,z>0$. Show that the optimal box is a cube, find its volume, and interpret the multiplier.

## Advanced

**23.** *(§7.2)* Prove the Lagrange necessary condition for one equality constraint: if $x^{*}$ is a local extremum of $f$ subject to $g(x)=0$ and $\nabla g(x^{*})\neq0$, then $\nabla f(x^{*})=\lambda\nabla g(x^{*})$ for some $\lambda$. Use the implicit function theorem to justify the tangent-space argument.

**24.** *(§7.2, §7.5)* Prove the multiple-constraint version: if $x^{*}$ is a local extremum of $f$ subject to $g_i(x)=0$ for $i=1,\dots,m$, the gradients $\nabla g_i(x^{*})$ are linearly independent, then there are $\lambda_1,\dots,\lambda_m$ with $\nabla f(x^{*})=\sum_i\lambda_i\nabla g_i(x^{*})$.

**25.** *(§7.6)* Prove that for a convex minimisation problem, every KKT point is a global minimiser. State precisely which convexity assumptions are used at each step.

**26.** *(§7.8)* Prove the second-order necessary condition: if $x^{*}$ is a local maximum of $f$ subject to $g(x)=b$, with multiplier $\lambda$, then $v^{T}H_{\mathcal L}v\le0$ for every $v$ with $\nabla g(x^{*})^{T}v=0$.

**27.** *(§8.5)* Prove the envelope theorem for $\max\{f(x):g(x)=b\}$: if $x(b)$ is a differentiable optimal solution with multiplier $\lambda(b)$, then $V'(b)=\lambda(b)$.

**28.** *(§8.5)* Prove the reparametrisation rule: if the constraint $g=0$ is replaced by $\tilde g=\varphi\circ g=0$ with $\varphi'(0)\neq0$, then the multiplier changes from $\lambda$ to $\tilde\lambda=\lambda/\varphi'(0)$, while the optimal point is unchanged.

**29.** *(§7.9)* Consider the constraints $g_1(x,y)=x+y-1=0$ and $g_2(x,y)=2x+2y-2=0$. Show that LICQ fails everywhere on the feasible set, and show that the multipliers for maximising $f(x,y)=xy$ are not unique. Does the optimum still exist?

**30.** *(§7.8)* Let $A$ be a symmetric $n\times n$ matrix and consider maximising the quadratic form $f(x)=x^{T}Ax$ subject to $x^{T}x=1$. Show that the stationary points are the unit eigenvectors of $A$, that the multipliers are the corresponding eigenvalues, and that the global maximum is the largest eigenvalue.

## Challenge

**31.** *(§7.9)* Consider maximising $f(x,y)=-x$ subject to $y^{2}=x^{5}$.
(a) Show that $(0,0)$ is a global maximum of $f$ on the constraint.
(b) Show that the Lagrange condition fails at $(0,0)$.
(c) Show that the value function $V(b)$ for the constraint $y^{2}=x^{5}$ and $x\le b$ has a finite right derivative at $b=0$ but no two-sided derivative there, and explain the connection with the failure of the multiplier.

**32.** *(§7.5, §7.9)* Prove that if LICQ holds at a KKT point, the multipliers are unique. Then give an example with dependent constraints where the multipliers are not unique, and an example where LICQ fails but the multipliers are still unique.

**33.** *(§7.8, §8.5)* A closed cylindrical can of volume $V$ is to minimise surface area. Derive $h=2r$, check the second-order condition, and interpret the multiplier $\lambda=2/r$ as the marginal surface area per unit volume. Evaluate for $V=500$.

**34.** *(§8.5)* Let $U(x)$ be positively homogeneous of degree one and consider $\max U(x)$ subject to $p\cdot x=m$, $x\ge0$. Prove that at an interior optimum the multiplier satisfies $\lambda=U(x^{*})/m$. Illustrate with $U=x^{1/2}y^{1/2}$ and $p=(2,3)$, $m=60$.

**35.** *(§7.6, §7.9)* Let $S$ be the set of optimal multiplier vectors at a KKT point.
(a) Prove that $S$ is convex.
(b) Show by example that $S$ can be a singleton, a line, or a ray.
(c) Explain the role of LICQ in determining which case occurs.

**36.** *(§7.8)* Extremise $f(x,y)=x^{2}+y^{2}$ subject to $x^{4}+y^{4}=1$. Find all stationary points, classify them, and identify the global maximum and minimum. (This problem requires separating the cases $x=0$, $y=0$ and $xy\neq0$.)
