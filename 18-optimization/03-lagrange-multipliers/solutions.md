# Lagrange Multipliers — Solutions

> [Lagrange Multipliers](README.md) · Solutions to [exercises.md](exercises.md) · 36 problems

Every solution states the Lagrangian, solves the first-order conditions, checks feasibility, and classifies the candidates. Where a multiplier has an interpretation, the interpretation is verified numerically. The convention is stated in each solution: for equality constraints the chapter uses $\mathcal{L}=f-\lambda(g-b)$, for which $\lambda=V'(b)$; for inequality constraints the KKT sign convention is stated explicitly.

## Beginner

**1.** *The closest point on a line*

**Strategy.** Minimise the squared distance $f=x^{2}+y^{2}$; the square is easier and has the same minimiser as the distance.

**Lagrangian.** $\mathcal{L}=x^{2}+y^{2}-\lambda(5x+12y-26)$.

**First-order conditions.**

$$2x=5\lambda,\qquad 2y=12\lambda,\qquad 5x+12y=26.$$

Hence $x=5\lambda/2$ and $y=6\lambda$. Substituting into the constraint,

$$5\left(\frac{5\lambda}{2}\right)+12(6\lambda)=\frac{25\lambda}{2}+72\lambda=\frac{169\lambda}{2}=26,$$

so $\lambda=52/169=4/13$. Then

$$x=\frac52\cdot\frac{4}{13}=\frac{10}{13},\qquad y=6\cdot\frac{4}{13}=\frac{24}{13}.$$

**Distance.** $f=(10/13)^{2}+(24/13)^{2}=(100+576)/169=676/169=4$, so the distance is $2$.

**Shadow price.** The distance from the origin to $5x+12y=b$ is $|b|/13$, so the squared distance is $V(b)=b^{2}/169$ and $V'(b)=2b/169$. At $b=26$, $V'=52/169=4/13=\lambda$, as the theorem predicts.

**Check.** $5(10/13)+12(24/13)=50/13+288/13=338/13=26$, so the point is on the line. The vector from the origin to $(10/13,24/13)$ is $(10,24)/13$, which is parallel to the normal $(5,12)$, so the point is the perpendicular foot.

**2.** *A product with a linear constraint*

**Lagrangian.** $\mathcal{L}=xy-\lambda(x+2y-4)$.

**First-order conditions.**

$$y=\lambda,\qquad x=2\lambda,\qquad x+2y=4.$$

Substituting gives $2\lambda+2\lambda=4$, so $\lambda=1$, $x=2$, $y=1$, and $f=2$.

**Boundary check.** If $x=0$ then $y=2$ and $f=0$; if $y=0$ then $x=4$ and $f=0$. Both are smaller than $2$, so the interior candidate is the maximum.

**Shadow price.** With $b$ in place of $4$, the optimum is $x=b/2$, $y=b/4$, so $V(b)=b^{2}/8$ and $V'(b)=b/4$. At $b=4$, $V'=1=\lambda$.

**Check.** $x+2y=2+2=4$ and $xy=2$. The multiplier is positive here: relaxing the constraint raises the maximum.

**3.** *A linear objective on a circle*

**Lagrangian.** $\mathcal{L}=x+y-\lambda(x^{2}+y^{2}-2)$.

**First-order conditions.**

$$1=2\lambda x,\qquad 1=2\lambda y,\qquad x^{2}+y^{2}=2.$$

The first two equations give $x=y=1/(2\lambda)$ and $\lambda\neq0$. The constraint gives $2x^{2}=2$, so $x=\pm1$. Hence the candidates are $(1,1)$ with $f=2$ and $(-1,-1)$ with $f=-2$.

**Classification.** The circle is compact, so the extrema exist and are among the candidates. The maximum is $2$ at $(1,1)$ (with $\lambda=1/2$); the minimum is $-2$ at $(-1,-1)$ (with $\lambda=-1/2$).

**Check.** $1^{2}+1^{2}=2$ and $1+1=2$. The level line $x+y=2$ is tangent to the circle at $(1,1)$.

**4.** *Distance to a plane*

**Lagrangian.** $\mathcal{L}=x^{2}+y^{2}+z^{2}-\lambda(x+2y+2z-9)$.

**First-order conditions.**

$$2x=\lambda,\qquad 2y=2\lambda,\qquad 2z=2\lambda,\qquad x+2y+2z=9.$$

Hence $x=\lambda/2$, $y=\lambda$, $z=\lambda$. Substituting,

$$\frac{\lambda}{2}+2\lambda+2\lambda=\frac{9\lambda}{2}=9,$$

so $\lambda=2$, $x=1$, $y=2$, $z=2$, and $f=1+4+4=9$. The distance to the plane is $3$.

**Shadow price.** The squared distance from the origin to $x+2y+2z=b$ is $b^{2}/9$, so $V'(b)=2b/9$; at $b=9$, $V'=2=\lambda$.

**Check.** $1+2(2)+2(2)=9$, and the point $(1,2,2)$ is parallel to the normal $(1,2,2)$, so it is the perpendicular foot.

**5.** *A product with a sum constraint*

**Strategy.** Solve the interior problem and show that the boundary cannot compete.

**Lagrangian.** $\mathcal{L}=xyz-\lambda(x+y+z-6)$.

**First-order conditions.**

$$yz=\lambda,\qquad xz=\lambda,\qquad xy=\lambda,\qquad x+y+z=6.$$

Subtracting the first two gives $z(y-x)=0$. Since the boundary will be checked separately, assume $x,y,z>0$; then $y=x$. Similarly $z=x$. The constraint gives $3x=6$, so $x=y=z=2$, and $f=8$. The multiplier is $\lambda=yz=4$.

**Boundary.** If one variable is zero, the product is zero, which is less than $8$. Hence the maximum is $8$ at $(2,2,2)$.

**Global check.** The AM–GM inequality gives

$$xyz\le\left(\frac{x+y+z}{3}\right)^{3}=2^{3}=8,$$

with equality exactly when $x=y=z=2$. This confirms the global maximum.

**Check.** $2+2+2=6$ and $2\cdot2\cdot2=8$.

**6.** *Extremising a sum of squares on a hyperbola*

**Lagrangian.** $\mathcal{L}=x^{2}+y^{2}-\lambda(xy-1)$.

**First-order conditions.**

$$2x=\lambda y,\qquad 2y=\lambda x,\qquad xy=1.$$

Multiplying the first by $x$ and the second by $y$ gives $2x^{2}=\lambda xy=\lambda$ and $2y^{2}=\lambda xy=\lambda$, so $x^{2}=y^{2}$. Since $xy=1>0$, $x$ and $y$ have the same sign; the alternative $y=-x$ would give $xy=-x^{2}<0$, so $x=y$. Then $x^{2}=1$, hence $x=y=1$ or $x=y=-1$.

**Candidates and values.** $(1,1)$ and $(-1,-1)$, both with $f=2$ and $\lambda=2$.

**Classification.** By AM–GM, $x^{2}+y^{2}\ge2|xy|=2$, with equality at both candidates. Hence both are global minima. There is no maximum: along $xy=1$ with $x\to\infty$, $y\to0$ and $f=x^{2}+y^{2}\to\infty$.

**Check.** $1\cdot1=1$ and $1+1=2$; $(-1)(-1)=1$ and $1+1=2$.

**7.** *Writing the Lagrangian only*

**Lagrangian.** $\mathcal{L}=x^{2}y-\lambda(x+y-1)$.

**First-order conditions.**

$$\frac{\partial\mathcal{L}}{\partial x}=2xy-\lambda=0,\qquad \frac{\partial\mathcal{L}}{\partial y}=x^{2}-\lambda=0,\qquad \frac{\partial\mathcal{L}}{\partial\lambda}=-(x+y-1)=0.$$

Thus

$$2xy=\lambda,\qquad x^{2}=\lambda,\qquad x+y=1.$$

**Check.** The system has three equations in three unknowns $(x,y,\lambda)$. Subtracting gives $x(2y-x)=0$, so the cases $x=0$ and $x=2y$ must be separated before dividing; this is the point of the exercise.

**8.** *Stationary points on a circle*

**Lagrangian.** $\mathcal{L}=x+y-\lambda(x^{2}+y^{2}-4)$.

**First-order conditions.**

$$1=2\lambda x,\qquad 1=2\lambda y,\qquad x^{2}+y^{2}=4.$$

Hence $x=y=1/(2\lambda)$ and $\lambda\neq0$. The constraint gives $2x^{2}=4$, so $x=\pm\sqrt2$. The candidates are $(\sqrt2,\sqrt2)$ with $f=2\sqrt2$ and $(-\sqrt2,-\sqrt2)$ with $f=-2\sqrt2$.

**Classification.** The circle is compact, so these are the global maximum and minimum: the maximum is $2\sqrt2$ at $(\sqrt2,\sqrt2)$ with $\lambda=1/(2\sqrt2)=\sqrt2/4$, and the minimum is $-2\sqrt2$ at $(-\sqrt2,-\sqrt2)$ with $\lambda=-\sqrt2/4$.

**Check.** $(\sqrt2)^{2}+(\sqrt2)^{2}=4$ and $\sqrt2+\sqrt2=2\sqrt2$. The level line $x+y=2\sqrt2$ touches the circle at exactly one point.

**9.** *KKT for a projection onto a half-plane*

**Lagrangian.** $\mathcal{L}=(x-2)^{2}+(y-2)^{2}+\mu(x+y-2)$, $\mu\ge0$.

**KKT conditions.**

$$2(x-2)+\mu=0,\qquad 2(y-2)+\mu=0,\qquad \mu(x+y-2)=0,\qquad \mu\ge0.$$

If $\mu=0$, then $x=y=2$, but $x+y=4>2$, so the constraint is violated. Hence $\mu>0$ and $x+y=2$. The first two equations give $x=y=2-\mu/2$, so

$$4-\mu=2\ \Longrightarrow\ \mu=2.$$

Thus $x=y=1$ and $f=1+1=2$.

**Check.** $1+1=2$ (active), $\mu=2\ge0$, and $f=2$. The unconstrained minimum is $0$ at $(2,2)$, which is infeasible; the constrained minimum is the projection of $(2,2)$ onto $x+y=2$, namely $(1,1)$.

**Shadow price.** For the constraint $x+y\le2+b$, the value is $V(b)=(2-b)^{2}/2$ for $b<2$ and $0$ for $b\ge2$. At $b=0$, $V'(0)=-2=-\mu$, consistent with the sign rule for a minimisation.

**10.** *KKT with an active constraint*

**Lagrangian.** $\mathcal{L}=(x-4)^{2}+(y-1)^{2}+\mu(x+y-3)$, $\mu\ge0$.

**KKT conditions.**

$$2(x-4)+\mu=0,\qquad 2(y-1)+\mu=0,\qquad \mu(x+y-3)=0.$$

If $\mu=0$, then $x=4$, $y=1$ and $x+y=5>3$, infeasible. Hence $\mu>0$ and $x+y=3$. The first two equations give

$$x=4-\frac{\mu}{2},\qquad y=1-\frac{\mu}{2},$$

so

$$5-\mu=3\ \Longrightarrow\ \mu=2.$$

Then $x=3$, $y=0$ and $f=(3-4)^{2}+(0-1)^{2}=1+1=2$.

**Check.** $3+0=3$ (active), $\mu=2\ge0$. The unconstrained point $(4,1)$ has sum $5>3$; the constrained optimum is the projection onto the line.

**Shadow price.** With right-hand side $3+b$, the value is $V(b)=(2-b)^{2}/2$ for $b<2$; $V'(0)=-2=-\mu$.

**11.** *A shadow-price identity*

**Lagrangian.** $\mathcal{L}=xy-\lambda(x+y-b)$.

**First-order conditions.**

$$y=\lambda,\qquad x=\lambda,\qquad x+y=b.$$

Hence $x=y=b/2$, $V(b)=b^{2}/4$, and $\lambda=b/2$.

**Numerical check.** At $b=6$: $x=y=3$, $V=9$, $\lambda=3$. At $b=6.2$: $x=y=3.1$, $V=9.61$. The exact change is $0.61$, while the first-order approximation is $\lambda\Delta b=3(0.2)=0.6$. The difference $0.01$ is the second-order term $\frac12V''(\Delta b)^{2}$; since $V''=1/2$, this is $\frac12\cdot\frac12\cdot(0.2)^{2}=0.01$, matching.

**Check.** $3+3=6$ and $3\cdot3=9$; the formula $V'(b)=b/2$ gives $3$ at $b=6$.

**12.** *Signs of multipliers*

**(a) Maximisation with $h(x)\le b$.** Write the Lagrangian in the max convention $\mathcal{L}=f-\mu(h-b)$ with $\mu\ge0$. Increasing $b$ enlarges the feasible set, so $V$ cannot decrease: $V'(b)\ge0$. The shadow-price theorem gives $V'(b)=\mu$, so the multiplier is non-negative. Economic reading: the shadow price of capacity; extra capacity is worth $\mu$ per unit.

**(b) Minimisation with $h(x)\le b$.** Write $\mathcal{L}=f+\mu(h-b)$ with $\mu\ge0$. Increasing $b$ enlarges the feasible set, so the minimum cannot increase: $V'(b)\le0$. The shadow-price theorem gives $V'(b)=-\mu$, so the multiplier is non-negative while the value derivative is non-positive. Economic reading: the marginal saving from extra capacity; each extra unit lowers the cost by $\mu$.

**Check.** In both cases the multiplier itself is non-negative; the sign of $V'$ differs because relaxing the constraint helps in a maximisation and helps (lowers cost) in a minimisation, and "helps" means opposite signs for the value.

## Intermediate

**13.** *Cobb–Douglas utility with equal weights*

**Lagrangian.** $\mathcal{L}=x^{1/2}y^{1/2}-\lambda(2x+3y-60)$.

**First-order conditions.**

$$\frac12x^{-1/2}y^{1/2}=2\lambda,\qquad \frac12x^{1/2}y^{-1/2}=3\lambda.$$

Dividing the first by the second gives

$$\frac{y}{x}=\frac{2}{3},$$

so $y=2x/3$. The budget gives

$$2x+3\left(\frac{2x}{3}\right)=2x+2x=4x=60,$$

hence $x=15$ and $y=10$.

**Utility and multiplier.** $U=\sqrt{15\cdot10}=\sqrt{150}=5\sqrt6\approx12.247$. From the first equation,

$$\lambda=\frac12\sqrt{\frac{y}{x}}\cdot\frac{1}{2}=\frac14\sqrt{\frac{2}{3}}\approx0.2041.$$

Since $U$ is homogeneous of degree one, $U/60=12.247/60\approx0.2041$, in agreement.

**Shadow price.** The indirect utility is $U(m)=m/\sqrt{24}$, so $U'(m)=1/\sqrt{24}\approx0.2041=\lambda$. An extra unit of budget raises utility by about $0.204$.

**Check.** $2(15)+3(10)=30+30=60$; the utility is positive and the budget is exhausted.

**14.** *Cost minimisation with a Cobb–Douglas technology*

**Lagrangian.** $\mathcal{L}=2L+4K-\lambda(L^{1/3}K^{2/3}-8)$.

**First-order conditions.**

$$2=\lambda\cdot\frac13L^{-2/3}K^{2/3},\qquad 4=\lambda\cdot\frac23L^{1/3}K^{-1/3}.$$

Dividing the first by the second gives

$$\frac{2}{4}=\frac{1}{2}\cdot\frac{K}{L},$$

so $K=L$. The production constraint gives $L^{1/3}L^{2/3}=L=8$, hence $L=K=8$.

**Cost and multiplier.** $C=2(8)+4(8)=16+32=48$. From the first equation,

$$2=\lambda\cdot\frac13\left(\frac{K}{L}\right)^{2/3}=\frac{\lambda}{3},$$

so $\lambda=6$.

**Marginal cost.** With $L=K=Q$, the cost is $C(Q)=2Q+4Q=6Q$, so $C'(Q)=6=\lambda$.

**Check.** $8^{1/3}8^{2/3}=8$ and $C=48$. If output rises to $8.1$, the cost is $48.6$, an increase of $0.6=\lambda(0.1)$.

**15.** *A box with surface area 54*

**Lagrangian.** $\mathcal{L}=xyz-\lambda(2xy+2yz+2zx-54)$.

**First-order conditions.**

$$yz=2\lambda(y+z),\qquad xz=2\lambda(x+z),\qquad xy=2\lambda(x+y).$$

Multiplying by $x,y,z$ respectively gives

$$xyz=2\lambda(xy+xz)=2\lambda(xy+yz)=2\lambda(xz+yz),$$

so $xz=yz$ and $xy=xz$. For positive $x,y,z$ this gives $x=y=z$. The constraint becomes $6x^{2}=54$, so $x=3$ and $V=27$.

**Multiplier.** From $yz=2\lambda(y+z)$: $9=2\lambda(6)=12\lambda$, so $\lambda=3/4$.

**Shadow price.** $V(S)=(S/6)^{3/2}$, so $V'(S)=\frac14\sqrt{S/6}$. At $S=54$ this is $\frac14\sqrt9=\frac34=\lambda$.

**AM–GM check.** For positive $x,y,z$,

$$xy+yz+zx\ge3(xyz)^{2/3},$$

so $xyz\le(S/6)^{3/2}=27$, with equality exactly when $xy=yz=zx$, that is $x=y=z=3$.

**Check.** The cube has surface $6(9)=54$ and volume $27$.

**16.** *Two constraints: sphere and a plane*

**Lagrangian.** $\mathcal{L}=x+y+z-\lambda(x^{2}+y^{2}+z^{2}-4)-\mu(x+y)$.

**First-order conditions.**

$$1=2\lambda x+\mu,\qquad 1=2\lambda y+\mu,\qquad 1=2\lambda z,\qquad x+y=0,\quad x^{2}+y^{2}+z^{2}=4.$$

Subtracting the first two equations gives $0=2\lambda(x-y)$. Since $y=-x$, this is $4\lambda x=0$, so either $x=0$ or $\lambda=0$.

* If $x=0$, then $y=0$ and $z^{2}=4$, so $z=\pm2$. The first equation gives $\mu=1$, and the third gives $\lambda=1/(2z)=\pm1/4$.
* If $\lambda=0$, the third equation gives $1=0$, which is impossible.

**Candidates.** $(0,0,2)$ with $f=2$, and $(0,0,-2)$ with $f=-2$. The multipliers are $\lambda=1/4$, $\mu=1$ at the first, and $\lambda=-1/4$, $\mu=1$ at the second.

**Classification.** The feasible set is the circle cut from the sphere by the plane $x+y=0$, hence compact; the maximum is $2$ and the minimum is $-2$.

**LICQ check.** The gradients are $(2x,2y,2z)$ and $(1,1,0)$; at $(0,0,\pm2)$ they are $(0,0,\pm4)$ and $(1,1,0)$, which are independent.

**Check.** $0+0+4=4$ and $0+0=0$; the objective values are $\pm2$.

**17.** *Two inequality constraints*

**Lagrangian.** $\mathcal{L}=(x-4)^{2}+(y-4)^{2}+\lambda_1(x+y-4)+\lambda_2(x-1)$, with $\lambda_1,\lambda_2\ge0$.

**KKT conditions.**

$$2(x-4)+\lambda_1+\lambda_2=0,\qquad 2(y-4)+\lambda_1=0,$$
$$\lambda_1(x+y-4)=0,\qquad \lambda_2(x-1)=0,\qquad \lambda_1,\lambda_2\ge0.$$

**Guess both active.** Then $x=1$ and $y=3$. The second equation gives $2(3-4)+\lambda_1=0$, so $\lambda_1=2$. The first gives $2(1-4)+2+\lambda_2=0$, so $-6+2+\lambda_2=0$ and $\lambda_2=4$. Both multipliers are non-negative, and $f=(1-4)^{2}+(3-4)^{2}=9+1=10$.

**Check that no other active set works.** If only $x+y=4$ is active, then $\lambda_2=0$ and the first two equations give $x=y=2$, which violates $x\le1$. If only $x=1$ is active, then $\lambda_1=0$ and the second equation gives $y=4$, but then $x+y=5>4$. If neither is active, the unconstrained point $(4,4)$ is infeasible. Hence the solution is $(1,3)$ with $f=10$.

**Check.** $1+3=4$ and $1\le1$, both active; $\lambda_1=2\ge0$, $\lambda_2=4\ge0$.

**18.** *A product on a circle of radius 2*

**Lagrangian.** $\mathcal{L}=xy-\lambda(x^{2}+y^{2}-4)$.

**First-order conditions.**

$$y=2\lambda x,\qquad x=2\lambda y.$$

Multiplying the first by $y$ and the second by $x$ gives $y^{2}=x^{2}$, so $y=\pm x$. On the circle $x^{2}+y^{2}=4$:

* $y=x$: $2x^{2}=4$, so $x=y=\pm\sqrt2$, with $f=2$ and $\lambda=1/2$;
* $y=-x$: $2x^{2}=4$, so $x=-y=\pm\sqrt2$, with $f=-2$ and $\lambda=-1/2$.

**Bordered Hessian at $(\sqrt2,\sqrt2)$.** $H_{\mathcal L}=\begin{pmatrix}-1&1\\1&-1\end{pmatrix}$ and

$$\overline{H}=\begin{pmatrix}0&2\sqrt2&2\sqrt2\\2\sqrt2&-1&1\\2\sqrt2&1&-1\end{pmatrix}.$$

Expanding, $\det\overline{H}=32>0$, so the point is a local maximum; the same holds at $(-\sqrt2,-\sqrt2)$.

**Bordered Hessian at $(\sqrt2,-\sqrt2)$.** $H_{\mathcal L}=\begin{pmatrix}1&1\\1&1\end{pmatrix}$ and

$$\overline{H}=\begin{pmatrix}0&2\sqrt2&-2\sqrt2\\2\sqrt2&1&1\\-2\sqrt2&1&1\end{pmatrix}.$$

Expanding, $\det\overline{H}=-16<0$, so the point is a local minimum; the same holds at $(-\sqrt2,\sqrt2)$.

**Global check.** The circle is compact, so the local extrema found are global: maximum $2$ and minimum $-2$.

**19.** *A cusp with a failing multiplier*

**Constraint geometry.** The constraint $x^{2}=y^{3}$ forces $y\ge0$, and then $x=\pm y^{3/2}$. The feasible set is a cusped curve through the origin.

**Origin is a local minimum.** On the constraint, $f=y\ge0$ and $f(0,0)=0$. Hence $(0,0)$ is a global minimum of $f$ on the feasible set.

**Lagrange condition.** $\nabla f=(0,1)$ and $\nabla g=(2x,-3y^{2})$. At the origin $\nabla g=(0,0)$, so the equation $(0,1)=\lambda(0,0)$ has no solution. The condition fails.

**Which hypothesis fails.** The Lagrange theorem requires $\nabla g(x^{*})\neq0$. At the cusp, the gradient vanishes and the constraint set has no well-defined tangent line; the implicit function theorem does not apply.

**Direct check.** Parameterising $x=t^{3}$, $y=t^{2}$ (with $t\in\mathbb{R}$) gives $f=t^{2}$, whose minimum is $0$ at $t=0$. The parameterisation also shows that $f$ is unbounded above, so the problem has no maximum.

**20.** *Shadow price of an inequality*

**Problem.** Minimise $(x-1)^{2}+(y-1)^{2}$ subject to $x+y\le1+b$, with $b<1$.

**Solution.** The unconstrained point is $(1,1)$, with sum $2>1+b$. The projection onto the line $x+y=1+b$ is

$$x=y=\frac{1+b}{2}.$$

The value is

$$V(b)=2\left(1-\frac{1+b}{2}\right)^{2}=2\left(\frac{1-b}{2}\right)^{2}=\frac{(1-b)^{2}}{2}.$$

**Derivative.** $V'(b)=-(1-b)=b-1$; at $b=0$, $V'(0)=-1$.

**KKT at $b=0$.** $\mathcal{L}=(x-1)^{2}+(y-1)^{2}+\mu(x+y-1)$ with $\mu\ge0$. The first-order equations give $x=y=1-\mu/2$ and the active constraint gives $2-\mu=1$, so $\mu=1$. Then $V'(0)=-1=-\mu$, verifying the sign rule for a minimisation with a $\le$ constraint.

**Check.** At $b=0$ the point is $(1/2,1/2)$, with $f=1/4+1/4=1/2$, and $x+y=1$.

**21.** *Proof of the shadow-price theorem*

**Statement.** Let $x(b)$ be a $C^{1}$ optimal solution of $\max f(x)$ subject to $g(x)=b$, with multiplier $\lambda(b)$, and let $V(b)=f(x(b))$. Then $V'(b)=\lambda(b)$.

**Proof.** The first-order condition is $\nabla f(x(b))=\lambda(b)\nabla g(x(b))$. Differentiating the constraint identity $g(x(b))=b$ gives

$$\nabla g(x(b))^{T}x'(b)=1.$$

Differentiating the value,

$$V'(b)=\nabla f(x(b))^{T}x'(b)=\lambda(b)\nabla g(x(b))^{T}x'(b)=\lambda(b).$$

$\blacksquare$

**Hypotheses.** Differentiability of $x(b)$ and $\lambda(b)$ is the substantive assumption; it follows from the implicit function theorem when the Jacobian of the system $\nabla f-\lambda\nabla g=0$, $g=b$ with respect to $(x,\lambda)$ is invertible. The proof also shows why the result is local: a change in the active set changes the system.

**Check.** In Exercise 1, $V(b)=b^{2}/25$ and $\lambda=2b/25$; indeed $V'=2b/25=\lambda$, and at $b=10$ both are $0.8$.

**22.** *A box inscribed in a sphere*

**Lagrangian.** Maximise $8xyz$ subject to $x^{2}+y^{2}+z^{2}=R^{2}$:

$$\mathcal{L}=8xyz-\lambda(x^{2}+y^{2}+z^{2}-R^{2}).$$

**First-order conditions.**

$$8yz=2\lambda x,\qquad 8xz=2\lambda y,\qquad 8xy=2\lambda z.$$

Multiplying by $x,y,z$ respectively gives

$$8xyz=2\lambda x^{2}=2\lambda y^{2}=2\lambda z^{2},$$

so $x^{2}=y^{2}=z^{2}$. For positive coordinates, $x=y=z=R/\sqrt3$.

**Volume and multiplier.** The volume is

$$8\left(\frac{R}{\sqrt3}\right)^{3}=\frac{8R^{3}}{3\sqrt3}.$$

From $8yz=2\lambda x$: $8(R^{2}/3)=2\lambda R/\sqrt3$, so $\lambda=4R/\sqrt3$.

**Interpretation.** The constraint level is $b=R^{2}$, and $V(b)=8b^{3/2}/(3\sqrt3)$. Then

$$V'(b)=\frac{8}{3\sqrt3}\cdot\frac32b^{1/2}=\frac{4\sqrt b}{\sqrt3}=\frac{4R}{\sqrt3}=\lambda.$$

**Check.** $3(R^{2}/3)=R^{2}$, and the volume is positive. For $R=2$, $x=y=z=2/\sqrt3$ and $V=64/(3\sqrt3)\approx12.317$.

## Advanced

**23.** *Proof of the Lagrange necessary condition*

**Statement.** Let $f,g:\mathbb{R}^{n}\to\mathbb{R}$ be $C^{1}$. If $x^{*}$ is a local extremum of $f$ subject to $g(x)=0$ and $\nabla g(x^{*})\neq0$, then there is $\lambda$ with $\nabla f(x^{*})=\lambda\nabla g(x^{*})$.

**Proof.** Since $\nabla g(x^{*})\neq0$, some partial derivative is non-zero; relabel so that $\partial g/\partial x_n(x^{*})\neq0$. By the implicit function theorem (Theorem 7.2), there is a $C^{1}$ function $\varphi$ on a neighbourhood $U\subseteq\mathbb{R}^{n-1}$ of $x^{*}_{1:n-1}$ such that, near $x^{*}$,

$$\{x:g(x)=0\}=\{(u,\varphi(u)):u\in U\}.$$

Let $T=\{v\in\mathbb{R}^{n}:\nabla g(x^{*})^{T}v=0\}$.

**Every $v\in T$ is a velocity.** Write $v=(v',v_n)$ with $v'\in\mathbb{R}^{n-1}$. Define

$$c(t)=(x^{*}_{1:n-1}+tv',\ \varphi(x^{*}_{1:n-1}+tv')).$$

Then $c(0)=x^{*}$, $g(c(t))=0$ for small $t$, and by the chain rule

$$c'(0)=\left(v',\ \nabla\varphi(x^{*}_{1:n-1})^{T}v'\right).$$

Differentiating $g(u,\varphi(u))=0$ gives $\partial_ig+\partial_ng\,\partial_i\varphi=0$, so $\partial_i\varphi=-g_i/g_n$ and

$$\nabla\varphi^{T}v'=-\frac{1}{g_n}\sum_{i<n}g_i v_i.$$

The condition $\nabla g^{T}v=0$ reads $\sum_{i<n}g_iv_i+g_nv_n=0$, so $v_n=-\frac{1}{g_n}\sum_{i<n}g_iv_i=\nabla\varphi^{T}v'$. Hence $c'(0)=v$.

**Derivative of $f$ along the curve.** Let $\phi(t)=f(c(t))$. Since $x^{*}$ is a local extremum on the constraint set and $c(t)$ stays on it, $t=0$ is a local extremum of $\phi$. Therefore

$$0=\phi'(0)=\nabla f(c(0))^{T}c'(0)=\nabla f(x^{*})^{T}v.$$

**Conclusion.** Thus $\nabla f(x^{*})$ is orthogonal to $T=\ker\nabla g(x^{*})^{T}$. Since $T$ has dimension $n-1$ and its orthogonal complement is the line spanned by $\nabla g(x^{*})$,

$$\nabla f(x^{*})=\lambda\nabla g(x^{*})$$

for some $\lambda\in\mathbb{R}$. $\blacksquare$

**Where regularity is used.** It gives both the graph representation and the dimension count. Without $\nabla g\neq0$, the set $T$ can be all of $\mathbb{R}^{n}$, and the conclusion would force $\nabla f=0$, which is false in general.

**24.** *Proof for several equality constraints*

**Statement.** Let $g:\mathbb{R}^{n}\to\mathbb{R}^{m}$ be $C^{1}$, $m<n$. If $x^{*}$ is a local extremum of $f$ subject to $g(x)=0$ and the gradients $\nabla g_1(x^{*}),\dots,\nabla g_m(x^{*})$ are linearly independent, then there are $\lambda_1,\dots,\lambda_m$ with $\nabla f(x^{*})=\sum_i\lambda_i\nabla g_i(x^{*})$.

**Proof.** The derivative $Dg(x^{*})$ is an $m\times n$ matrix of rank $m$. By the rank theorem (the vector form of the implicit function theorem), the level set $S=\{g=0\}$ is locally a $C^{1}$ surface of dimension $n-m$, and its tangent space is

$$T=\ker Dg(x^{*})=\{v:Dg(x^{*})v=0\}=\bigcap_{i=1}^{m}\{v:\nabla g_i(x^{*})^{T}v=0\}.$$

For every $v\in T$ there is a $C^{1}$ curve $c$ on $S$ with $c(0)=x^{*}$ and $c'(0)=v$: choose local coordinates in which $S$ is a graph, as in Theorem 7.2, and lift the straight line.

Let $\phi(t)=f(c(t))$. Since $x^{*}$ is a local extremum on $S$, $\phi'(0)=0$, hence $\nabla f(x^{*})^{T}v=0$ for every $v\in T$. Therefore $\nabla f(x^{*})\in T^{\perp}$.

By linear algebra, $T^{\perp}=(\ker Dg(x^{*}))^{\perp}=\operatorname{row}(Dg(x^{*}))=\operatorname{span}\{\nabla g_1(x^{*}),\dots,\nabla g_m(x^{*})\}$. Hence

$$\nabla f(x^{*})=\sum_{i=1}^{m}\lambda_i\nabla g_i(x^{*})$$

for some coefficients $\lambda_i$. $\blacksquare$

**Role of independence.** If the gradients are dependent, $Dg$ has rank $r<m$ and the row space has dimension $r$; the representation may fail, or the coefficients may be non-unique. This is the LICQ hypothesis.

**25.** *KKT sufficiency for convex problems*

**Statement.** Consider $\min f(x)$ subject to $g_i(x)=0$ and $h_j(x)\le0$. Assume $f$ and every $h_j$ are convex and every $g_i$ is affine. If $x^{*}$ is a KKT point, then $x^{*}$ is a global minimiser.

**Proof.** Let $x$ be any feasible point. Convexity of $f$ gives

$$f(x)\ge f(x^{*})+\nabla f(x^{*})^{T}(x-x^{*}).$$

Convexity of $h_j$ gives

$$h_j(x)\ge h_j(x^{*})+\nabla h_j(x^{*})^{T}(x-x^{*}).$$

If $h_j$ is active, $h_j(x^{*})=0$ and $h_j(x)\le0$, so $\nabla h_j(x^{*})^{T}(x-x^{*})\le0$. If $h_j$ is inactive, complementary slackness gives $\mu_j=0$.

Affineness of $g_i$ gives $g_i(x)-g_i(x^{*})=\nabla g_i(x^{*})^{T}(x-x^{*})$; both sides are zero because both points are feasible.

Stationarity reads $\nabla f(x^{*})=-\sum_i\lambda_i\nabla g_i(x^{*})-\sum_j\mu_j\nabla h_j(x^{*})$. Therefore

$$\nabla f(x^{*})^{T}(x-x^{*})=-\sum_i\lambda_i\underbrace{\nabla g_i(x^{*})^{T}(x-x^{*})}_{=0}-\sum_j\mu_j\underbrace{\nabla h_j(x^{*})^{T}(x-x^{*})}_{\le0\ \text{for active},\ =0\ \text{for inactive}}\ge0.$$

Hence $f(x)\ge f(x^{*})$, so $x^{*}$ is a global minimiser. $\blacksquare$

**Which assumptions are used.** Convexity of $f$ gives the first inequality; convexity of $h_j$ gives the second and the sign on active constraints; affineness of $g_i$ makes the equality term vanish. If $f$ is not convex, the first inequality can fail and a KKT point need not be a minimum.

**26.** *Proof of the second-order necessary condition*

**Statement.** If $x^{*}$ is a local maximum of $f$ subject to $g(x)=b$, with multiplier $\lambda$, then $v^{T}H_{\mathcal L}v\le0$ for every $v$ with $\nabla g(x^{*})^{T}v=0$.

**Proof.** Fix such a $v$. As in Exercise 23, there is a $C^{2}$ curve $c$ with $c(0)=x^{*}$, $c'(0)=v$ and $g(c(t))=b$. Let $\phi(t)=f(c(t))$. Since $x^{*}$ is a local maximum, $t=0$ is a local maximum of $\phi$, so $\phi'(0)=0$ and $\phi''(0)\le0$.

Compute $\phi''(0)$. First,

$$\phi'(t)=\nabla f(c(t))^{T}c'(t),$$
$$\phi''(t)=c'(t)^{T}\nabla^{2}f(c(t))c'(t)+\nabla f(c(t))^{T}c''(t).$$

Differentiate $g(c(t))=b$ twice:

$$\nabla g(c(t))^{T}c'(t)=0,\qquad c'(t)^{T}\nabla^{2}g(c(t))c'(t)+\nabla g(c(t))^{T}c''(t)=0.$$

At $t=0$, $\nabla f(x^{*})=\lambda\nabla g(x^{*})$, so

$$\phi''(0)=v^{T}\nabla^{2}f(x^{*})v+\lambda\nabla g(x^{*})^{T}c''(0).$$

From the second derivative of the constraint, $\nabla g(x^{*})^{T}c''(0)=-v^{T}\nabla^{2}g(x^{*})v$. Substituting,

$$\phi''(0)=v^{T}\bigl(\nabla^{2}f(x^{*})-\lambda\nabla^{2}g(x^{*})\bigr)v=v^{T}H_{\mathcal L}v.$$

Since $\phi''(0)\le0$, the result follows. For a local minimum, reverse the inequality. $\blacksquare$

**Why the tangent space.** The vector $v$ is $c'(0)$ for a feasible curve, so it satisfies $\nabla g^{T}v=0$. Directions that violate the constraint are not velocities of feasible curves and play no role.

**27.** *Proof of the envelope theorem*

**Statement.** For $\max\{f(x):g(x)=b\}$ with value $V(b)$, if $x(b)$ is differentiable and optimal with multiplier $\lambda(b)$, then $V'(b)=\lambda(b)$.

**Proof.** Let $\mathcal{L}(x,\lambda,b)=f(x)-\lambda(g(x)-b)$. At the optimum,

$$\frac{\partial\mathcal{L}}{\partial x}=\nabla f(x(b))-\lambda(b)\nabla g(x(b))=0,\qquad \frac{\partial\mathcal{L}}{\partial\lambda}=-(g(x(b))-b)=0.$$

Since $g(x(b))=b$, $\mathcal{L}(x(b),\lambda(b),b)=f(x(b))=V(b)$. Differentiating with respect to $b$,

$$V'(b)=\frac{\partial\mathcal{L}}{\partial x}\,x'(b)+\frac{\partial\mathcal{L}}{\partial\lambda}\,\lambda'(b)+\frac{\partial\mathcal{L}}{\partial b}.$$

The first two terms vanish by the first-order conditions, and $\partial\mathcal{L}/\partial b=\lambda$. Hence $V'(b)=\lambda(b)$. $\blacksquare$

**Interpretation.** The envelope theorem says that, to first order, the effect of changing $b$ is the partial derivative of the Lagrangian, because the optimal choices of $x$ and $\lambda$ are already at a stationary point. This is why the multiplier is the shadow price.

**28.** *Reparametrising a constraint*

**Statement.** If $g=0$ is replaced by $\tilde g=\varphi\circ g=0$ with $\varphi(0)=0$ and $\varphi'(0)\neq0$, then the optimal point is unchanged and the multiplier becomes $\tilde\lambda=\lambda/\varphi'(0)$.

**Proof.** The feasible set is unchanged near $x^{*}$ because $\varphi$ is locally invertible and $\varphi(0)=0$: $\varphi(g(x))=0$ if and only if $g(x)=0$. The chain rule gives

$$\nabla\tilde g(x^{*})=\varphi'(0)\nabla g(x^{*}).$$

The Lagrange condition for the new constraint is $\nabla f=\tilde\lambda\nabla\tilde g$. Substituting $\nabla f=\lambda\nabla g$ and $\nabla\tilde g=\varphi'(0)\nabla g$,

$$\lambda\nabla g=\tilde\lambda\,\varphi'(0)\nabla g,$$

so $\tilde\lambda=\lambda/\varphi'(0)$ (the gradients are non-zero by regularity). $\blacksquare$

**Consequence.** Multipliers are not attached to the geometry alone; they depend on the units in which the constraint is measured. Measuring a budget in cents rather than dollars multiplies $g$ by $100$ and divides $\lambda$ by $100$, which is exactly what a change of units should do.

**29.** *Dependent constraints and non-unique multipliers*

**LICQ fails.** $g_1(x,y)=x+y-1$, $g_2(x,y)=2x+2y-2$. The gradients are $(1,1)$ and $(2,2)$, which are dependent everywhere; indeed $g_2=2g_1$, so the second constraint is redundant and LICQ fails at every feasible point.

**The optimum.** The feasible set is the line $x+y=1$. On it,

$$f(x,y)=xy=x(1-x)=\frac14-\left(x-\frac12\right)^{2},$$

whose maximum is $1/4$ at $x=y=1/2$. The optimum exists and is unique.

**Multipliers.** The Lagrangian is

$$\mathcal{L}=xy-\lambda_1(x+y-1)-\lambda_2(2x+2y-2).$$

Stationarity gives

$$y=\lambda_1+2\lambda_2,\qquad x=\lambda_1+2\lambda_2.$$

Thus $x=y$, and the constraint gives $x=y=1/2$. The only condition on the multipliers is

$$\lambda_1+2\lambda_2=\frac12.$$

For every $t\in\mathbb{R}$, $(\lambda_1,\lambda_2)=(1/2-2t,t)$ is a solution, so the multipliers are not unique: they form a line.

**Check.** $1/2+1/2=1$ and $xy=1/4$. The non-uniqueness is exactly the one-dimensional ambiguity left by the dependent gradients; the optimum itself is unaffected.

**30.** *Quadratic forms on the unit sphere*

**Lagrangian.** $\mathcal{L}=x^{T}Ax-\lambda(x^{T}x-1)$ with $A$ symmetric.

**First-order conditions.**

$$\nabla(x^{T}Ax)=2Ax,\qquad \nabla(x^{T}x)=2x,$$

so $2Ax-2\lambda x=0$, that is

$$Ax=\lambda x,\qquad x^{T}x=1.$$

Hence the stationary points are the unit eigenvectors of $A$, and the multipliers are the corresponding eigenvalues.

**Global maximum.** Since $A$ is symmetric, it has an orthonormal eigenbasis $q_1,\dots,q_n$ with eigenvalues $\lambda_1\le\dots\le\lambda_n$. Write $x=\sum_iy_iq_i$; then $x^{T}x=\sum_iy_i^{2}=1$ and

$$x^{T}Ax=\sum_i\lambda_iy_i^{2}\le\lambda_n\sum_iy_i^{2}=\lambda_n.$$

Equality holds at $x=\pm q_n$. Hence the global maximum is the largest eigenvalue, attained at the corresponding unit eigenvector; the global minimum is the smallest eigenvalue.

**Check.** For $A=\begin{pmatrix}2&1\\1&3\end{pmatrix}$ the eigenvalues are $(5\pm\sqrt5)/2$, approximately $1.382$ and $3.618$. The maximum of $x^{T}Ax$ on the unit circle is $3.618$, attained at the eigenvector for the larger eigenvalue. This is the Rayleigh-quotient principle.

## Challenge

**31.** *A cusp, a missing multiplier and a non-differentiable value*

**(a) The origin is a global maximum of $f=-x$.** The constraint $y^{2}=x^{5}$ forces $x\ge0$, and $x=t^{2}$, $y=t^{5}$ parametrises the whole curve. Then $f=-x=-t^{2}\le0$, with equality only at $t=0$. Hence $(0,0)$ is the global maximum, with value $0$.

**(b) The Lagrange condition fails.** $\nabla f=(-1,0)$ and $\nabla g=(-5x^{4},2y)$. At $(0,0)$, $\nabla g=(0,0)$, and $(-1,0)=\lambda(0,0)$ has no solution.

**(c) The value function.** For the constraint $y^{2}=x^{5}$ together with $x\le b$:

* if $b\ge0$, the maximum of $-x$ is at $x=b$ (with $y=\pm b^{5/2}$), so $V(b)=-b$;
* if $b<0$, there is no feasible point, because $x\ge0$ and $x\le b<0$ are incompatible.

Thus $V$ is defined on $[0,\infty)$ and has right derivative $-1$ at $0$; it has no two-sided derivative at $0$ because it is not defined for $b<0$ (where the problem is infeasible). The one-sided shadow price is finite ($-1$), but no Lagrange multiplier exists. The connection is that the shadow-price theorem assumes regularity; at the cusp the constraint gradient vanishes and the conclusion fails.

**Check.** At $b=1$, $V(1)=-1$ and the point is $(1,\pm1)$; at $b=0$, $V(0)=0$ and the point is $(0,0)$. Both satisfy the constraint, and the values decrease linearly with slope $-1$.

**32.** *Uniqueness of multipliers under LICQ*

**(a) Proof.** Suppose $\lambda$ and $\lambda'$ are two multiplier vectors at a KKT point, using the same convention. Subtract the stationarity equations:

$$\sum_i(\lambda_i-\lambda_i')\nabla g_i(x^{*})+\sum_{j\in A}(\mu_j-\mu_j')\nabla h_j(x^{*})=0,$$

where $A$ is the active set. LICQ says the gradients in this sum are linearly independent, so every coefficient is zero: $\lambda_i=\lambda_i'$ and $\mu_j=\mu_j'$ for active $j$. For inactive $j$, complementary slackness gives $\mu_j=\mu_j'=0$. Hence the multiplier vector is unique. $\blacksquare$

**(b) A line of multipliers.** Exercise 29: $\lambda_1+2\lambda_2=1/2$ with dependent constraint gradients; the solution set is a line.

**A ray of multipliers.** Minimise $f=x^{2}+y^{2}$ subject to $h_1=x\le0$ and $h_2=-x\le0$. The feasible set is the line $x=0$; the minimum is at $(0,0)$ with value $0$. The gradients are $(1,0)$ and $(-1,0)$, dependent. Stationarity gives

$$(0,0)+\mu_1(1,0)+\mu_2(-1,0)=0\ \Longrightarrow\ \mu_1=\mu_2=t,$$

with $t\ge0$. The multiplier set is the ray $\{(\mu_1,\mu_2)=(t,t):t\ge0\}$.

**A singleton.** Exercise 1 has LICQ at the optimum, so its multiplier is unique; the same is true of any regular, non-degenerate equality problem.

**(c) The role of LICQ.** Under LICQ the stationarity equations have a unique solution for the multipliers. Without LICQ the gradients span a proper subspace, so the homogeneous system has a non-trivial solution and the multiplier set is an affine subspace intersected with the orthant; it can be a line, a ray or a higher-dimensional set.

**33.** *A cylindrical can of volume 500*

**Problem.** Minimise $C=2\pi r^{2}+2\pi rh$ subject to $\pi r^{2}h=500$.

**Lagrangian.** $\mathcal{L}=2\pi r^{2}+2\pi rh-\lambda(\pi r^{2}h-500)$.

**First-order conditions.**

$$4\pi r+2\pi h=\lambda\,2\pi rh,\qquad 2\pi r=\lambda\,\pi r^{2}.$$

The second gives $\lambda=2/r$. Substituting into the first,

$$4\pi r+2\pi h=\frac{2}{r}(2\pi rh)=4\pi h,$$

so $h=2r$. The volume gives $2\pi r^{3}=500$, hence

$$r=\left(\frac{250}{\pi}\right)^{1/3}\approx4.301,\qquad h\approx8.602.$$

The surface is $C=6\pi r^{2}\approx348.7$, and $\lambda=2/r\approx0.465$.

**Second-order condition.** $C(r)=2\pi r^{2}+2V/r$ with $V=500$, so

$$C''(r)=4\pi+\frac{4V}{r^{3}}>0,$$

and the stationary point is the global minimum.

**Interpretation.** $C(V)=6\pi(V/(2\pi))^{2/3}$, so

$$C'(V)=\frac{2}{r}=\lambda.$$

One more unit of volume requires about $0.465$ more units of surface area.

**Check.** $\pi(4.301)^{2}(8.602)\approx500$, and $h=2r$.

**34.** *Homogeneity and the multiplier*

**Statement.** Let $U$ be positively homogeneous of degree one: $U(tx)=tU(x)$ for $t>0$. For $\max U(x)$ subject to $p\cdot x=m$, $x\ge0$, an interior optimum satisfies $\lambda=U(x^{*})/m$.

**Proof.** Euler's theorem for a $C^{1}$ homogeneous function of degree one gives

$$\sum_{i=1}^{n}x_i\frac{\partial U}{\partial x_i}=U(x).$$

At an interior optimum, the Lagrange condition is $\partial U/\partial x_i=\lambda p_i$ for every $i$. Multiplying by $x_i$ and summing,

$$\sum_ix_i\lambda p_i=\lambda\,p\cdot x=\lambda m=U(x^{*}).$$

Hence $\lambda=U(x^{*})/m$. $\blacksquare$

**Example.** $U=x^{1/2}y^{1/2}$, $p=(2,3)$, $m=60$. The first-order conditions give $y/x=2/3$, and the budget gives $x=15$, $y=10$. Then $U=\sqrt{150}\approx12.247$, and

$$\lambda=\frac{U}{60}\approx0.2041.$$

The direct computation in Exercise 13 gives the same value.

**Check.** $2(15)+3(10)=60$; the multiplier is positive, and the value is homogeneous of degree one, so doubling the budget doubles the utility and leaves $\lambda$ unchanged.

**35.** *The set of optimal multipliers*

**(a) Convexity.** Let $\mu$ and $\nu$ be two optimal multiplier vectors for the same KKT point. For $t\in[0,1]$, set $\rho=t\mu+(1-t)\nu$. Stationarity is linear in the multipliers, so $\rho$ satisfies it. Complementary slackness: if constraint $j$ is inactive, $\mu_j=\nu_j=0$, hence $\rho_j=0$; if it is active, the condition is vacuous. Non-negativity is preserved. Hence $\rho$ is also an optimal multiplier vector, and $S$ is convex.

**(b) Examples.**

* **Singleton:** Exercise 1, where LICQ holds and the multiplier is unique.
* **Line:** Exercise 29, where the dependent equality constraints leave $\lambda_1+2\lambda_2=1/2$.
* **Ray:** minimise $x^{2}+y^{2}$ subject to $x\le0$ and $-x\le0$. The feasible set is $x=0$, the optimum is $(0,0)$, and the multipliers satisfy $\mu_1=\mu_2=t\ge0$, a ray.

**(c) The role of LICQ.** LICQ makes the stationarity equations uniquely solvable for the multipliers (Exercise 32). Without it, the linear system has a non-trivial null space and the solution set is an affine subspace intersected with the orthant: a point, a line, a ray, or a higher-dimensional polyhedron.

**36.** *A quartic constraint*

**Lagrangian.** $\mathcal{L}=x^{2}+y^{2}-\lambda(x^{4}+y^{4}-1)$.

**First-order conditions.**

$$2x=4\lambda x^{3},\qquad 2y=4\lambda y^{3},\qquad x^{4}+y^{4}=1.$$

Equivalently,

$$x(1-2\lambda x^{2})=0,\qquad y(1-2\lambda y^{2})=0.$$

**Case 1: $x=0$.** Then $y^{4}=1$, so $y=\pm1$, with $f=1$ and $\lambda=1/2$ (from $2y=4\lambda y^{3}$).

**Case 2: $y=0$.** Then $x=\pm1$, with $f=1$ and $\lambda=1/2$.

**Case 3: $x,y\neq0$.** Then $x^{2}=y^{2}=1/(2\lambda)$, so $x^{2}=y^{2}$. The constraint gives $2x^{4}=1$, hence $x^{2}=1/\sqrt2$ and

$$f=x^{2}+y^{2}=\frac{2}{\sqrt2}=\sqrt2,\qquad \lambda=\frac{1}{2x^{2}}=\frac{\sqrt2}{2}.$$

The points are $(\pm2^{-1/4},\pm2^{-1/4})$ with all four sign combinations.

**Classification.** The constraint set is compact, so the global extrema are among the candidates. The values are $1$ in Cases 1 and 2 and $\sqrt2\approx1.414$ in Case 3. Hence the global maximum is $\sqrt2$ at the four diagonal points, and the global minimum is $1$ at $(\pm1,0)$ and $(0,\pm1)$.

**Check.** At $(2^{-1/4},2^{-1/4})$: $x^{4}+y^{4}=2(2^{-1})=1$ ✓ and $x^{2}+y^{2}=2(2^{-1/2})=\sqrt2$ ✓. At $(0,1)$: $0+1=1$ ✓ and $x^{2}+y^{2}=1$ ✓, with $\lambda=1/2$.
