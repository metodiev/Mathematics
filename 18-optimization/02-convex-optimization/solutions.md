# Convex Optimization — Solutions

> [Tutorial](README.md) · [Exercises](exercises.md) · 38 complete solutions

Each solution states the strategy first, then the argument, then a numerical check where one is possible.
Theorem numbers refer to the [tutorial](README.md).

## Beginner

**1.**

*Strategy.* Use only Definition 5.2: take two points of $C$ and verify the three inequalities for an arbitrary
convex combination.

Let $x=(x_1,x_2),y=(y_1,y_2)\in C$ and $\theta\in[0,1]$, and put $z=\theta x+(1-\theta)y$. Then
$$
z_1=\theta x_1+(1-\theta)y_1\ge0,\qquad z_2=\theta x_2+(1-\theta)y_2\ge0
$$
because both coefficients are nonnegative and $x_i,y_i\ge0$. Also
$$
z_1+z_2=\theta(x_1+x_2)+(1-\theta)(y_1+y_2)\le\theta\cdot1+(1-\theta)\cdot1=1 .
$$
Hence $z\in C$. $\blacksquare$

*Check.* $x=(1,0)$, $y=(0,1)$, $\theta=\tfrac12$ give $z=(\tfrac12,\tfrac12)$ with $z_1+z_2=1$. ✓
Geometrically $C$ is a triangle, an intersection of three halfspaces, so the conclusion also follows from
Lemma 7.1.1.

**2.**

(a) Convexity of $f(x)=3x-5$: for $\theta\in[0,1]$,
$$
\theta f(x)+(1-\theta)f(y)=3(\theta x+(1-\theta)y)-5=f(\theta x+(1-\theta)y),
$$
so the defining inequality holds with equality. Concavity is the same computation with the inequality reversed,
also an equality.

(b) For $f(x)=a^{\mathsf T}x+b$,
$\theta f(x)+(1-\theta)f(y)=a^{\mathsf T}(\theta x+(1-\theta)y)+b=f(\theta x+(1-\theta)y)$.

(c) None exists. If $f$ is both convex and concave then for all $x<y$ and $\theta\in(0,1)$ both $\le$ and $\ge$
hold in the defining inequality, so it is an equality:
$f(\theta x+(1-\theta)y)=\theta f(x)+(1-\theta)f(y)$. Fix $x=0$, $y=1$ and put $t=\theta$; then
$f(t)=(1-t)f(0)+tf(1)$, which is affine in $t$, and the same argument applied to any interval $[x,y]$ gives
affinity. Hence affine functions are exactly the functions that are both convex and concave. $\blacksquare$

**3.**

*Strategy.* Expand both sides and compare; the identity is the standard "second difference" computation.

$$
\theta f(x)+(1-\theta)f(y)-f(\theta x+(1-\theta)y)
=\theta x^2+(1-\theta)y^2-\bigl(\theta x+(1-\theta)y\bigr)^2 .
$$
Expanding the square,
$\bigl(\theta x+(1-\theta)y\bigr)^2=\theta^2x^2+2\theta(1-\theta)xy+(1-\theta)^2y^2$, so the difference is
$$
\theta(1-\theta)x^2-2\theta(1-\theta)xy+(1-\theta)\bigl(1-(1-\theta)\bigr)y^2
=\theta(1-\theta)\bigl(x^2-2xy+y^2\bigr)=\theta(1-\theta)(x-y)^2 .
$$
Since $\theta(1-\theta)\ge0$ and $(x-y)^2\ge0$, the expression is nonnegative: this is a direct proof of
convexity.

*At $x=-1$, $y=3$, $\theta=\tfrac14$:* the right side is $\tfrac14\cdot\tfrac34\cdot16=3$. The left side is
$\tfrac14\cdot1+\tfrac34\cdot9-2^2=\tfrac14+\tfrac{27}{4}-4=7-4=3$. ✓

**4.**

*Strategy.* Use the second-derivative test on each side of the origin, then exhibit an explicit triple that
violates the defining inequality on $\mathbb{R}$.

$f'(x)=3x^2$ and $f''(x)=6x$. By Theorem 7.4.2, $f$ is strictly convex on $(0,\infty)$ (where $f''>0$) and strictly
concave on $(-\infty,0)$ (where $f''<0$).

$f$ is not convex on $\mathbb{R}$: take $x=-2$, $y=1$ and $\theta=\tfrac12$. Then
$$
\tfrac12f(-2)+\tfrac12f(1)=\tfrac12(-8)+\tfrac12(1)=-3.5,
\qquad f\bigl(\tfrac12(-2)+\tfrac12(1)\bigr)=f(-0.5)=-0.125,
$$
and convexity would require $-3.5\ge-0.125$, which is false.

The same diagnosis follows from Lemma 7.4.1: convexity on $\mathbb{R}$ would force $f'$ to be nondecreasing there,
but $f'(-1)=3>0=f'(0)$. $\blacksquare$

**5.**

*Strategy.* Compute the Hessian and apply Sylvester's criterion.

$f_x=2x+4y$, $f_y=4x+10y$, so
$$
H=\begin{pmatrix}2&4\\4&10\end{pmatrix},\qquad \det H=20-16=4>0 .
$$
The leading entry is $2>0$ and the determinant is $4>0$, so $H\succ0$: $f$ is strictly convex by Theorem 7.4.2.
Since $H$ is positive definite everywhere, $f$ has the unique stationary point solving
$2x+4y=0$, $4x+10y=0$, namely $(0,0)$, and $f(0,0)=0$ is the global minimum by Corollary 7.5.3.

*Check.* Along $y=x$: $f=x^2+4x^2+5x^2=10x^2\ge0$; along $y=-x$: $x^2-4x^2+5x^2=2x^2\ge0$. ✓

**6.**

(a) For $\theta\in[0,1]$,
$$
\lvert\theta x+(1-\theta)y\rvert\le\lvert\theta x\rvert+\lvert(1-\theta)y\rvert=\theta\lvert x\rvert+(1-\theta)\lvert y\rvert
$$
by the triangle inequality and $\theta\ge0$. Hence $f$ is convex.

(b) For $x>0$, $f$ is differentiable with $f'(x)=1$, so $\partial f(x)=\{1\}$ by Lemma 7.11.3; similarly
$\partial f(-2)=\{-1\}$. At $0$ the subgradients are the $g$ with $\lvert y\rvert\ge gy$ for all $y$; testing
$y=1$ gives $g\le1$ and $y=-1$ gives $g\ge-1$, so $\partial f(0)=[-1,1]$.

*Check.* $0\in\partial f(0)$, so $0$ is the minimiser by Theorem 7.11.4, and indeed $\lvert x\rvert\ge0$. ✓

**7.**

*Lemma 7.1.1 route.* Each $C_i$ is a halfspace, hence convex (Section 7.1); the intersection of convex sets is
convex.

*Direct route.* Let $x,y\in C_1\cap C_2$ and $\theta\in[0,1]$. Then
$(x_1+x_2)\le1$ and $(y_1+y_2)\le1$, so
$\theta x_1+(1-\theta)y_1+\theta x_2+(1-\theta)y_2=\theta(x_1+x_2)+(1-\theta)(y_1+y_2)\le1$, which says
$z\in C_1$; the same computation with $x_1-x_2$ gives $z\in C_2$. Hence $z\in C_1\cap C_2$. $\blacksquare$

*Check.* The region is the strip $\lvert x_2\rvert$-free band between two lines, $C_1\cap C_2=\{x: x_1\le1+\lvert x_2\rvert\}$;
it is a wedge, visibly convex.

**8.**

Let $x,y\in B(c,r)$ and $\theta\in[0,1]$. Then
$$
\lVert\theta x+(1-\theta)y-c\rVert=\lVert\theta(x-c)+(1-\theta)(y-c)\rVert\le\theta\lVert x-c\rVert+(1-\theta)\lVert y-c\rVert\le\theta r+(1-\theta)r=r,
$$
where the first inequality is the triangle inequality and the second uses $x,y\in B(c,r)$. Hence
$\theta x+(1-\theta)y\in B(c,r)$. $\blacksquare$

**9.**

At $x=0$: $f(y)\ge f(0)+f'(0)(y-0)$, that is $e^y\ge1+y$.

At $x=1$: $e^y\ge e+e(y-1)=ey$. At $y=1.1$ this gives $e^{1.1}\ge1.1e=2.99011$. The true value is
$e^{1.1}=3.00417$, so the tangent bound is valid and its error is about $0.014$. ✓

**10.**

With $f(x)=x^2$, $f(1)=1$, $f'(1)=2$ and $y=3$: the right side of the first-order condition is
$f(1)+f'(1)(3-1)=1+4=5$, while $f(3)=9$. The gap is $4$, which equals $(3-1)^2$ — the squared distance, as it
must for a quadratic with Hessian $2$. The inequality $9\ge5$ holds, and the tangent line $y=2x-1$ lies below the
parabola everywhere, touching it at $x=1$.

**11.**

On $(0,\infty)$, $f''(x)=2/x^3>0$, so $f$ is strictly convex there. On $(-\infty,0)$, $x^3<0$ so $f''<0$ and
$f$ is strictly concave there. It is not convex on $\mathbb{R}\setminus\{0\}$ for two reasons: that set is not
convex (the segment from $-1$ to $1$ passes through $0$), and the defining inequality fails. Take $x=-1$,
$y=1$, $\theta=\tfrac12$: the combination is $0$, where $f$ is undefined, so the inequality cannot even be
stated; take instead $x=-1$, $y=2$, $\theta=\tfrac13$: the combination $\tfrac13(-1)+\tfrac23(2)=1$ lies in the
domain, and
$$
\tfrac13f(-1)+\tfrac23f(2)=-\tfrac13+\tfrac13=0,
\qquad f(1)=1,
$$
so the required inequality $1\le0$ fails. ✓

**12.**

(a) $\{x:x^2\le1\}=[-1,1]$, an interval, hence convex. In general the sublevel set of a convex function is
convex: if $f(x)\le\alpha$ and $f(y)\le\alpha$ then $f(\theta x+(1-\theta)y)\le\theta\alpha+(1-\theta)\alpha=\alpha$.

(b) For $f(x)=x^3$ the sublevel set is $\{x:x^3\le\alpha\}=\{x:x\le\alpha^{1/3}\}$, a half-line, hence convex
for every $\alpha$. Yet $f$ is not convex, as Exercise 4 shows. A function whose sublevel sets are all convex is
called *quasiconvex*; every convex function is quasiconvex, but not conversely.

## Intermediate

**13.**

*Strategy.* Introduce a surplus variable for the $\ge$ constraint and write the problem with equality and
nonnegativity only.

With $s\ge0$ the constraint $x_1+x_2\ge4$ becomes $x_1+x_2-s=4$, so the standard form is
$$
\text{minimise }2x_1+3x_2\quad\text{subject to}\quad x_1+x_2-s=4,\quad x\succeq0,\quad s\ge0 .
$$
The feasible set is a polyhedron; the objective decreases fastest in the $x_1$ direction (coefficient $2<3$), so
put all the surplus into $x_1$: $x^\star=(4,0)$, $s=0$, with value $8$. The other vertex $(0,4)$ has value $12$,
and the ray $s\to\infty$ does not change the objective. Hence $p^\star=8$.

*Check.* $x_1+x_2=4\ge4$ ✓ and $2\cdot4+3\cdot0=8<12$. ✓

**14.**

*Strategy.* Rewrite as a maximum of two affine functions, then use the subdifferential rule for maxima.

$f(x)=\max\{x,1-x\}$: the pieces are equal at $x=\tfrac12$, with $f(\tfrac12)=\tfrac12$. For $x<\tfrac12$,
$f=1-x$ is decreasing; for $x>\tfrac12$, $f=x$ is increasing. Hence $x^\star=\tfrac12$ and $f(x^\star)=\tfrac12$.

At $x=\tfrac12$ both pieces are active, with slopes $1$ and $-1$, so by Lemma 7.11.2
$\partial f(\tfrac12)=\operatorname{conv}\{1,-1\}=[-1,1]$. Since $0\in[-1,1]$, Theorem 7.11.4 certifies
optimality.

*Check.* $f(\tfrac12)=0.5$, $f(0)=1$, $f(1)=1$, $f(0.6)=0.6>0.5$. ✓

**15.**

*Strategy.* $f$ is a quadratic form, so its Hessian is constant; apply Theorem 7.4.2.

Compute $\nabla f(x)=2Ax$ (using $A=A^{\mathsf T}$) and $\nabla^2f(x)=2A$. By Theorem 7.4.2, $f$ is convex if
and only if $2A\succeq0$, that is $A\succeq0$. If $A$ is not symmetric the same argument applies to
$\tfrac12(A+A^{\mathsf T})$, since $x^{\mathsf T}Ax=x^{\mathsf T}\bigl(\tfrac12(A+A^{\mathsf T})\bigr)x$.

*Check.* For $A=\operatorname{diag}(1,-1)$, $f(x)=x_1^2-x_2^2$; along $x_2=0$ it is convex, along $x_1=0$ it is
concave, and $A$ is indefinite. ✓

**16.**

*Strategy.* Bound each piece separately, then take maxima.

For $\theta\in[0,1]$ and $z=\theta x+(1-\theta)y$,
$$
f(z)=\max\{f_1(z),f_2(z)\}\le\max\{\theta f_1(x)+(1-\theta)f_1(y),\ \theta f_2(x)+(1-\theta)f_2(y)\}.
$$
Each argument of the outer maximum is at most $\theta\max\{f_1(x),f_2(x)\}+(1-\theta)\max\{f_1(y),f_2(y)\}$
because $f_i(x)\le f(x)$ and $f_i(y)\le f(y)$. Hence $f(z)\le\theta f(x)+(1-\theta)f(y)$. $\blacksquare$

*Check.* $f_1(x)=x^2$, $f_2(x)=(x-1)^2$, $x=0$, $y=1$, $\theta=\tfrac12$: $f(0)=1$, $f(1)=1$, and
$f(\tfrac12)=\max\{\tfrac14,\tfrac14\}=\tfrac14\le1$. ✓

**17.**

*Strategy.* The infimum over $y$ is not attained in general, so compare with $g(x_i)+\varepsilon$ and let
$\varepsilon\downarrow0$.

Let $x_1,x_2$ be points where $g$ is finite, $\theta\in[0,1]$ and $\varepsilon>0$. Choose $y_1,y_2$ with
$f(x_i,y_i)\le g(x_i)+\varepsilon$. Joint convexity of $f$ gives
$$
g(\theta x_1+(1-\theta)x_2)\le f\bigl(\theta x_1+(1-\theta)x_2,\ \theta y_1+(1-\theta)y_2\bigr)\le\theta f(x_1,y_1)+(1-\theta)f(x_2,y_2)\le\theta g(x_1)+(1-\theta)g(x_2)+\varepsilon .
$$
Since $\varepsilon>0$ is arbitrary, $g(\theta x_1+(1-\theta)x_2)\le\theta g(x_1)+(1-\theta)g(x_2)$. $\blacksquare$
The $\varepsilon$ is needed because the infimum may not be attained; without it one could not choose $y_i$.

**18.**

*Strategy.* Compute the Hessian and test it; a zero determinant means semidefinite, not definite, so convexity
but not strict convexity.

For $f(x,y)=x^2/y$ on $y>0$: $f_x=2x/y$, $f_y=-x^2/y^2$, and
$$
\nabla^2f=\begin{pmatrix}2/y&-2x/y^2\\-2x/y^2&2x^2/y^3\end{pmatrix}.
$$
The $(1,1)$ entry is positive, and the determinant is
$\dfrac{2}{y}\cdot\dfrac{2x^2}{y^3}-\dfrac{4x^2}{y^4}=0$. A symmetric matrix with positive leading entry and zero
determinant is positive semidefinite, so $f$ is convex by Theorem 7.4.2. It is not strictly convex: it is affine
along rays $(x,y)\mapsto(tx,ty)$, since $f(tx,ty)=tf(x,y)$.

*Check.* At $(1,1)$, $H=\begin{pmatrix}2&-2\\-2&2\end{pmatrix}$ with eigenvalues $0$ and $4$. ✓ This is the
perspective of $u\mapsto u^2$, consistent with Theorem 7.6.5.

**19.**

*Strategy.* Express $\lambda_{\max}$ as a supremum of linear functions of $X$ and apply Theorem 7.6.3.

By the spectral theorem, for symmetric $X$,
$$
\lambda_{\max}(X)=\max_{\lVert u\rVert=1}u^{\mathsf T}Xu=\sup_{\lVert u\rVert=1}\langle uu^{\mathsf T},X\rangle .
$$
For each fixed $u$ the map $X\mapsto\langle uu^{\mathsf T},X\rangle$ is linear, hence convex; a supremum of convex
functions is convex by Theorem 7.6.3. (The supremum is a maximum because the unit sphere is compact, but that is
not needed for convexity.)

*Check.* $X=\operatorname{diag}(3,1)$ gives $\lambda_{\max}=3$, attained at $u=e_1$; $X=\operatorname{diag}(1,1)$
gives $1$ for every $u$. ✓

**20.**

*Strategy.* Expand the square: the Hessian is $2A^{\mathsf T}A\succeq0$. Set the gradient to zero to obtain the
normal equations.

(a) $f(x)=\lVert Ax-b\rVert^2=x^{\mathsf T}A^{\mathsf T}Ax-2b^{\mathsf T}Ax+b^{\mathsf T}b$, so
$\nabla f(x)=2A^{\mathsf T}Ax-2A^{\mathsf T}b$ and $\nabla^2f=2A^{\mathsf T}A\succeq0$: convex. The normal
equations $A^{\mathsf T}Ax=A^{\mathsf T}b$ have the unique solution $x=(A^{\mathsf T}A)^{-1}A^{\mathsf T}b$
because $A$ has full rank.

Here $A^{\mathsf T}A=\begin{pmatrix}2&0\\0&2\end{pmatrix}$ and $A^{\mathsf T}b=\begin{pmatrix}2\\2\end{pmatrix}$, so
$x^\star=(1,1)$.

(b) $Ax^\star=(1\cdot1+1\cdot1,\ 1\cdot1-1\cdot1)=(2,0)=b$: the residual is zero, so $f(x^\star)=0$, the global
minimum. ✓

**21.**

*Strategy.* Write the constraints as $b-Ax\le0$ and $-x\le0$, form the Lagrangian, and minimise over $x$.

With $\lambda\ge0$ on $b-Ax\le0$ and $\mu\ge0$ on $-x\le0$,
$$
L=c^{\mathsf T}x+\lambda^{\mathsf T}(b-Ax)-\mu^{\mathsf T}x=b^{\mathsf T}\lambda+(c-A^{\mathsf T}\lambda-\mu)^{\mathsf T}x .
$$
The infimum over $x\in\mathbb{R}^n$ is $b^{\mathsf T}\lambda$ if $c-A^{\mathsf T}\lambda-\mu=0$ and $-\infty$
otherwise. Since $\mu\ge0$ can absorb any slack, the condition is $A^{\mathsf T}\lambda\le c$, and the dual is
$$
\text{maximise }b^{\mathsf T}\lambda\quad\text{subject to}\quad A^{\mathsf T}\lambda\le c,\quad\lambda\ge0 .
$$
*Weak duality on the instance.* With $c=(2,3)$, $A=(1,1)$, $b=1$: the dual is
$\max\{\lambda:\lambda\le2,\ \lambda\le3,\ \lambda\ge0\}$, so $d^\star=2$. The primal is
$\min\{2x_1+3x_2:x_1+x_2\ge1,\ x\succeq0\}$, with optimum $x=(1,0)$ and $p^\star=2$. For any feasible pair,
$c^{\mathsf T}x-b^{\mathsf T}\lambda=(c-A^{\mathsf T}\lambda)^{\mathsf T}x\ge0$ because $c-A^{\mathsf T}\lambda\succeq0$
and $x\succeq0$; hence $b^{\mathsf T}\lambda\le c^{\mathsf T}x$, which is $d^\star\le p^\star$. ✓ Equality here.

**22.**

*Strategy.* One equality constraint, so use a single multiplier and solve the stationarity equations.

With $h(x)=x_1+x_2-1=0$, $L=x_1^2+x_2^2+\nu(x_1+x_2-1)$ and stationarity gives
$2x_1+\nu=0$, $2x_2+\nu=0$, so $x_1=x_2$. The constraint gives $x_1=x_2=\tfrac12$, and $\nu=-1$. The point is
optimal by Theorem 7.10.1 (the problem is convex, the constraint is affine), and $p^\star=\tfrac12$.

*Geometric check.* The point is the orthogonal projection of the origin onto the line $x_1+x_2=1$: the
projection is $\tfrac{1}{2}(1,1)$, and its squared distance from the origin is $\tfrac12$. ✓

**23.**

(a) $\min\{x^2:x\ge0\}$. With $L=x^2-\lambda x$, stationarity gives $2x-\lambda=0$. The optimum is $x^\star=0$
with $\lambda^\star=0$: the constraint is active ($x^\star$ is on the boundary) but the multiplier vanishes. This
is the degenerate case, and it is consistent with complementary slackness $\lambda x=0$.

(b) $\min\{x^2:x\ge1\}$. With $L=x^2+\lambda(1-x)$, stationarity gives $2x-\lambda=0$, so at $x^\star=1$ we get
$\lambda^\star=2>0$. The constraint is active and the multiplier is positive: relaxing it to $x\ge1-\varepsilon$
changes the value at rate $-2\varepsilon$, since the optimum becomes $x=1-\varepsilon$ with value
$(1-\varepsilon)^2\approx1-2\varepsilon$.

*Comparison.* In both cases the constraint is active; only in (b) does it *cost* anything, and exactly then is the
multiplier positive.

## Advanced

**24.**

*Strategy.* Suppose two minimisers and evaluate strong convexity at the midpoint, where the quadratic term is
largest.

Let $x\ne y$ both minimise $f$ over the convex set $\mathcal{F}$, with common value $f^\star$, and put
$z=\tfrac12x+\tfrac12y\in\mathcal{F}$. Strong convexity with $\theta=\tfrac12$ gives
$$
f(z)\le\tfrac12f(x)+\tfrac12f(y)-\frac{\mu}{2}\cdot\tfrac12\cdot\tfrac12\lVert x-y\rVert^2=f^\star-\frac{\mu}{8}\lVert x-y\rVert^2<f^\star,
$$
contradicting the minimality of $f^\star$. Hence at most one minimiser exists. $\blacksquare$

*Check.* $f(x)=x^2$ is $2$-strongly convex; its minimiser $0$ is unique. The bound above would give
$f(z)\le0-\tfrac{2}{8}\lVert x-y\rVert^2<0$ for two purported minimisers, impossible. ✓

**25.**

*Strategy.* Both directions are instances of Theorem 7.3.1.

($\Leftarrow$) If $\nabla f(x^\star)=0$ then for every $y$,
$f(y)\ge f(x^\star)+\nabla f(x^\star)^{\mathsf T}(y-x^\star)=f(x^\star)$, so $x^\star$ is a global minimiser.

($\Rightarrow$) If $x^\star$ is a global minimiser, then for any $y$ and $t\in(0,1]$,
$f(x^\star+t(y-x^\star))\ge f(x^\star)$; subtract, divide by $t$ and let $t\downarrow0$ to get
$\nabla f(x^\star)^{\mathsf T}(y-x^\star)\ge0$. Applying this with $y=x^\star-v$ and with $y=x^\star+v$ gives
$\nabla f(x^\star)^{\mathsf T}v=0$ for all $v$, hence $\nabla f(x^\star)=0$. $\blacksquare$

**26.**

(a) With $L=x^2+\lambda(1-x)$ and $\lambda\ge0$, the infimum over $x$ is attained at $x=\lambda/2$, giving
$$
g(\lambda)=\frac{\lambda^2}{4}+\lambda\Bigl(1-\frac{\lambda}{2}\Bigr)=\lambda-\frac{\lambda^2}{4}.
$$
This concave parabola is maximal at $\lambda=2$, where $g(2)=1$. Hence $d^\star=1$.

(b) Slater: the point $x=2$ satisfies $1-x=-1<0$, so the condition holds.

(c) At $x^\star=1$, $\lambda^\star=2$: primal feasibility $1\ge1$ ✓; dual feasibility $2\ge0$ ✓;
complementary slackness $2\cdot(1-1)=0$ ✓; stationarity $2x-\lambda=0$ gives $2-2=0$ ✓. And $p^\star=1=d^\star$:
the gap is zero, as Theorem 7.9.2 requires.

**27.**

*Strategy.* In the forward direction take $t\downarrow0$ in the defining inequality; in the reverse direction
show that the secant slope $\varphi$ has nonnegative derivative.

($\Rightarrow$) Fix $x,y$ and $t\in(0,1]$. Convexity gives $f(x+t(y-x))\le(1-t)f(x)+tf(y)$; subtract $f(x)$, divide
by $t>0$:
$$
f(y)\ge f(x)+\frac{f(x+t(y-x))-f(x)}{t}.
$$
The fraction tends to $\nabla f(x)^{\mathsf T}(y-x)$ as $t\downarrow0$, and the inequality survives the limit.

($\Leftarrow$) Fix $x,y$, put $g(t)=f(x+t(y-x))$ and apply the hypothesis at $u=x+t(y-x)$ with target $x$:
$f(x)\ge f(u)+\nabla f(u)^{\mathsf T}(x-u)=g(t)-tg'(t)$, hence $g'(t)\ge\bigl(g(t)-g(0)\bigr)/t=\varphi(t)$.
Therefore
$$
\varphi'(t)=\frac{tg'(t)-\bigl(g(t)-g(0)\bigr)}{t^2}=\frac{g'(t)-\varphi(t)}{t}\ge0,
$$
so $\varphi$ is nondecreasing on $(0,1]$ and $\varphi(t)\le\varphi(1)=g(1)-g(0)$. Multiplying by $t>0$ gives
$g(t)-g(0)\le t(g(1)-g(0))$, which rearranges to $f(x+t(y-x))\le(1-t)f(x)+tf(y)$. $\blacksquare$

*Why the monotonicity matters.* Without it, one only knows $\varphi(t)\le\varphi(1)$ for each $t$ separately; the
monotonicity is what lets the single evaluation at $t=1$ dominate every $t\le1$.

**28.**

*Strategy.* Reduce to one variable along a line, apply Lemma 7.4.1 there, and use that a function is convex if
and only if it is convex along every line.

($\Rightarrow$) Fix $x\in C$ and $v\ne0$; choose $\varepsilon>0$ with $x+tv\in C$ for $\lvert t\rvert<\varepsilon$ and
put $g(t)=f(x+tv)$. For $\theta\in[0,1]$,
$g(\theta s+(1-\theta)r)=f(\theta(x+sv)+(1-\theta)(x+rv))\le\theta g(s)+(1-\theta)g(r)$, so $g$ is convex; it is
twice differentiable with $g''(t)=v^{\mathsf T}\nabla^2f(x+tv)v$. Lemma 7.4.1 gives $g''(0)\ge0$, that is
$v^{\mathsf T}\nabla^2f(x)v\ge0$. Since $v$ is arbitrary, $\nabla^2f(x)\succeq0$.

($\Leftarrow$) Assume $\nabla^2f\succeq0$ on $C$. For $x,y\in C$, $g(t)=f(x+t(y-x))$ has
$g''(t)=(y-x)^{\mathsf T}\nabla^2f(x+t(y-x))(y-x)\ge0$ on an open interval containing $[0,1]$, so by Lemma 7.4.1
$g$ is convex; hence $g(\theta)\le(1-\theta)g(0)+\theta g(1)$, which is the defining inequality for $f$ at
$(1-\theta)x+\theta y$. $\blacksquare$

Lemma 7.4.1 is used in both directions: in the forward direction to pass from convexity of $g$ to $g''(0)\ge0$,
and in the reverse direction to pass from $g''\ge0$ to convexity of $g$.

**29.**

*Strategy.* Each direction is a two-line verification using the definition of the epigraph.

($\Rightarrow$) Let $f$ be convex, $(x,s),(y,t)\in\operatorname{epi}f$ and $\theta\in[0,1]$. Then
$f(x)\le s$, $f(y)\le t$, so
$f(\theta x+(1-\theta)y)\le\theta f(x)+(1-\theta)f(y)\le\theta s+(1-\theta)t$; this says
$\theta(x,s)+(1-\theta)(y,t)\in\operatorname{epi}f$.

($\Leftarrow$) Let $\operatorname{epi}f$ be convex and let $x,y\in\operatorname{dom}f$. The points
$(x,f(x))$ and $(y,f(y))$ lie in $\operatorname{epi}f$, so their convex combination
$\bigl(\theta x+(1-\theta)y,\ \theta f(x)+(1-\theta)f(y)\bigr)$ does too, which by definition means
$f(\theta x+(1-\theta)y)\le\theta f(x)+(1-\theta)f(y)$. Moreover $\theta x+(1-\theta)y$ has finite value, so
$\operatorname{dom}f$ is convex. $\blacksquare$

**30.**

*Strategy.* Distribute the weights so that the inner point becomes an explicit convex combination.

Put $T=\theta t_1+(1-\theta)t_2>0$ and define $\alpha=\theta t_1/T\ge0$ and $\beta=(1-\theta)t_2/T\ge0$. Then
$\alpha+\beta=1$ and
$$
\frac{\theta x_1+(1-\theta)x_2}{T}=\alpha\frac{x_1}{t_1}+\beta\frac{x_2}{t_2}.
$$
By convexity of $f$,
$f\bigl(\alpha x_1/t_1+\beta x_2/t_2\bigr)\le\alpha f(x_1/t_1)+\beta f(x_2/t_2)$, and multiplying by $T>0$ gives
$$
g\bigl(\theta x_1+(1-\theta)x_2,\ T\bigr)\le T\Bigl[\frac{\theta t_1}{T}f\Bigl(\frac{x_1}{t_1}\Bigr)+\frac{(1-\theta)t_2}{T}f\Bigl(\frac{x_2}{t_2}\Bigr)\Bigr]=\theta g(x_1,t_1)+(1-\theta)g(x_2,t_2). \ \blacksquare
$$

*Check.* With $f(u)=u^2$, $x_1=1,t_1=1$, $x_2=0,t_2=2$, $\theta=\tfrac12$: $T=1.5$, and the combination is
$\tfrac{0.5\cdot1+0.5\cdot0}{1.5}=\tfrac13$. Then $g(\tfrac13,1.5)=1.5\cdot\tfrac19=0.1\overline{6}$, while
$\theta g(1,1)+(1-\theta)g(0,2)=0.5\cdot1+0.5\cdot0=0.5$. Indeed $0.1\overline6\le0.5$. ✓

**31.**

(a) For fixed $x$, the map $(\lambda,\nu)\mapsto L(x,\lambda,\nu)=f_0(x)+\sum_i\lambda_if_i(x)+\sum_j\nu_jh_j(x)$ is
affine. For $\theta\in[0,1]$,
$$
L(x,\theta\lambda_1+(1-\theta)\lambda_2,\theta\nu_1+(1-\theta)\nu_2)=\theta L(x,\lambda_1,\nu_1)+(1-\theta)L(x,\lambda_2,\nu_2).
$$
Taking the infimum over $x$ on both sides and using that the infimum of a convex combination is at most the convex
combination of infima,
$$
g(\theta\lambda_1+(1-\theta)\lambda_2,\theta\nu_1+(1-\theta)\nu_2)\ge\theta g(\lambda_1,\nu_1)+(1-\theta)g(\lambda_2,\nu_2),
$$
which is concavity of $g$. (Equivalently, apply Theorem 7.6.3 to $-g$, an infimum of affine functions.)

(b) Let $x$ be feasible and $\lambda\succeq0$. Then $\lambda_if_i(x)\le0$ and $h_j(x)=0$, so
$L(x,\lambda,\nu)\le f_0(x)$. Hence $g(\lambda,\nu)=\inf_xL(x,\lambda,\nu)\le f_0(x)$ for every feasible $x$, and
taking the infimum over feasible $x$ gives $g(\lambda,\nu)\le p^\star$. Taking the supremum over dual feasible
points gives $d^\star\le p^\star$. If the primal is infeasible, $p^\star=+\infty$ and the inequality is
automatic; if the dual is infeasible, $d^\star=-\infty$ and it is automatic too. $\blacksquare$

**32.**

*Strategy.* Read each condition off the equality of the displayed chain.

Under strong duality with attained dual optimum, and $x^\star$ optimal,
$$
f_0(x^\star)=g(\lambda^\star,\nu^\star)=\inf_xL(x,\lambda^\star,\nu^\star)\le L(x^\star,\lambda^\star,\nu^\star)=f_0(x^\star)+\sum_i\lambda_i^\star f_i(x^\star)+\sum_j\nu_j^\star h_j(x^\star)\le f_0(x^\star).
$$
The last inequality uses feasibility of $x^\star$ ($f_i\le0$, $h_j=0$) and $\lambda^\star\succeq0$; it is therefore
equality, so every term vanishes: $\lambda_i^\star f_i(x^\star)=0$ (complementary slackness) — and $f_i(x^\star)\le0$,
$h_j(x^\star)=0$ are primal feasibility. The first equality says $g(\lambda^\star,\nu^\star)=L(x^\star,\lambda^\star,\nu^\star)$,
so $x^\star$ attains the infimum of $L(\cdot,\lambda^\star,\nu^\star)$; since $L$ is differentiable in $x$, that
gives $\nabla_xL(x^\star,\lambda^\star,\nu^\star)=0$, which is stationarity. Dual feasibility $\lambda^\star\succeq0$
is part of dual feasibility. $\blacksquare$

**33.**

*Strategy.* Expand the squared distance to the optimum, insert the subgradient inequality, and telescope.

Let $g_k\in\partial f(x_k)$ with $\lVert g_k\rVert\le G$, $R=\lVert x_0-x^\star\rVert$. Then
$$
\lVert x_{k+1}-x^\star\rVert^2=\lVert x_k-x^\star\rVert^2-2\alpha\langle g_k,x_k-x^\star\rangle+\alpha^2\lVert g_k\rVert^2
\le\lVert x_k-x^\star\rVert^2-2\alpha\bigl(f(x_k)-f(x^\star)\bigr)+\alpha^2G^2,
$$
where the inequality uses $\langle g_k,x_k-x^\star\rangle\ge f(x_k)-f(x^\star)$. Rearranging and summing over
$k=0,\dots,K-1$,
$$
2\alpha\sum_{k=0}^{K-1}\bigl(f(x_k)-f(x^\star)\bigr)\le R^2-\lVert x_K-x^\star\rVert^2+K\alpha^2G^2\le R^2+K\alpha^2G^2 .
$$
Since the minimum is at most the average,
$\min_{k<K}\bigl(f(x_k)-f(x^\star)\bigr)\le\frac{R^2}{2\alpha K}+\frac{\alpha G^2}{2}$. $\blacksquare$

*Why it is not a descent method.* Take $f(x)=\lvert x\rvert$, $x_0=2$, $\alpha=0.5$ and the subgradient
$\operatorname{sign}(x_k)$: the iterates are $2,1.5,1,0.5,0$, decreasing. But with $\alpha=1.5$ they are
$2,0.5,-1,0.5,-1,\dots$, and from $0.5$ to $-1$ the value increases from $0.5$ to $1$. The inequality that would
give descent, $f(x_{k+1})\le f(x_k)-\alpha\lVert g_k\rVert^2+\tfrac{L\alpha^2}{2}\lVert g_k\rVert^2$, requires an
$L$-smoothness constant, which $\lvert x\rvert$ does not have. Hence the theorem must bound the best iterate.

## Challenge

**34.**

(a) On $(-1,1)$, $f'(x)=x(1-x^2)^{-1/2}$ and
$$
f''(x)=(1-x^2)^{-1/2}+x\cdot x(1-x^2)^{-3/2}=(1-x^2)^{-3/2}\bigl[(1-x^2)+x^2\bigr]=(1-x^2)^{-3/2}>0 .
$$
By Theorem 7.4.2, $f$ is strictly convex on $(-1,1)$. Convexity extends to the endpoints by continuity: for
$x,y\in[-1,1]$ choose $x_n,y_n\in(-1,1)$ with $x_n\to x$, $y_n\to y$; the inequality
$f(\theta x_n+(1-\theta)y_n)\le\theta f(x_n)+(1-\theta)f(y_n)$ passes to the limit because $f$ is continuous
on $[-1,1]$.

(b) A subgradient at $1$ would be a $g$ with $f(y)\ge f(1)+g(y-1)=g(y-1)$ for all $y\in[-1,1]$, since
$f(1)=0$. For $y<1$, divide by $y-1<0$ to get $g\le\dfrac{-f(y)}{1-y}=\dfrac{\sqrt{1-y^2}}{1-y}=\sqrt{\dfrac{1+y}{1-y}}$,
which tends to $+\infty$ as $y\uparrow1$. No finite $g$ satisfies this, so $\partial f(1)=\varnothing$. By symmetry
$\partial f(-1)=\varnothing$.

(c) The standard theorem says that a proper convex $f$ has $\partial f(x)\ne\varnothing$ at every point of
$\operatorname{ri}\operatorname{dom}f$, the relative interior. Here $\operatorname{dom}f=[-1,1]$ has relative
interior $(-1,1)$, and $\pm1$ are boundary points. The hypothesis that fails is "$x$ lies in the relative
interior"; note also that $f$ is continuous on $[-1,1]$ but not Lipschitz near $\pm1$, since
$\lvert f'(x)\rvert\to\infty$.

**35.**

(a) $e^{-x}$ is convex (composition of $e^t$ with the affine map $t=-x$), and $x^2/y$ is convex on $y>0$ by
Exercise 18. The single feasible $x$ is $x=0$ (as $x^2/y\le0$ forces $x^2\le0$), so the feasible set is
$\{(0,y):y>0\}$ and $p^\star=e^0=1$.

(b) A strictly feasible point would need $f_1(x,y)=x^2/y<0$, impossible; so Slater fails.

(c) With $\lambda\ge0$,
$$
g(\lambda)=\inf_{x,\ y>0}\Bigl[e^{-x}+\lambda\frac{x^2}{y}\Bigr].
$$
For $x\ne0$ fixed, $\lambda x^2/y\downarrow0$ as $y\to\infty$, so $g(\lambda)=\inf_xe^{-x}=0$ for every $\lambda\ge0$.
Hence $d^\star=0$ and the gap is $p^\star-d^\star=1$.

(d) Geometrically the feasible set is a ray that is only met in the limit $y\to\infty$, so no supporting hyperplane
with normal $(\lambda,\nu,1)$ separates the value $1$ from the set $\mathcal{A}$ of achievable constraint/objective
triples.

**36.**

(a) $x^2\le0$ forces $x=0$, so the feasible set is $\{0\}$ and $p^\star=0$. A strictly feasible point would need
$x^2<0$, impossible, so Slater fails.

(b) With $\lambda\ge0$, $g(\lambda)=\inf_x\bigl[x+\lambda x^2\bigr]$. For $\lambda>0$ the minimiser is $x=-1/(2\lambda)$,
giving $g(\lambda)=-\tfrac{1}{4\lambda}$. Hence $\sup_{\lambda\ge0}g(\lambda)=0=p^\star$: strong duality holds, but
the supremum is approached only as $\lambda\to\infty$ and is never attained.

(c) KKT would require $1+2\lambda x^\star=0$ and $\lambda\ge0$ at $x^\star=0$, that is $1=0$: impossible. No
multipliers exist.

(d) Theorem 7.10.1 asserts necessity only under Slater's condition, which fails here. It remains consistent:
strong duality holds (weak duality plus the value $0$) but without attainment, so the chain used to derive KKT
cannot be closed. This shows that "strong duality" and "KKT holds" are different conclusions, and Slater is the
hypothesis that delivers both.

**37.**

(a) With $L=10^4$, $R^2=\lVert x_0\rVert^2=2$ and $\alpha=1/L$, Theorem 7.12.2 gives
$$
f(x_k)\le\frac{L R^2}{2k}=\frac{10^4\cdot2}{2k}=\frac{10^4}{k}.
$$
Requiring $10^4/k\le10^{-6}$ gives $k\ge10^{10}$.

(b) Along the flat eigendirection the factor is $1-10^{-4}$ per step. The condition $(1-10^{-4})^k\le10^{-6}$ gives
$$
k\ge\frac{\ln(10^{-6})}{\ln(1-10^{-4})}=\frac{-13.8155}{-1.00005\times10^{-4}}\approx1.38\times10^{5}.
$$
A careful accounting of the factor $\tfrac12$ in $\tfrac12x_2^2$ and of the square (the function value is
quadratic in the distance) replaces $10^{-6}$ by $\sqrt{2\cdot10^{-6}}$ and halves the count, giving about
$6.6\times10^{4}$ steps.

(c) The bound exceeds the true count by a factor of order $10^{5}$. The bound is worst-case over all convex
$L$-smooth functions, while this particular quadratic is easy along the stiff direction (it is solved almost
immediately) and hard only along the flat one. The condition number $\kappa=10^4$ is what makes the flat direction
slow; the bound does not see $\kappa$ at all, which is precisely the gap that strong convexity and acceleration
address in [Gradient Methods](../04-gradient-methods/README.md).

**38.**

(a) With $x_0=2>0$ we have $x_1=2-\alpha$. Suppose some iterate satisfies $0<x_k<\alpha$; then
$x_{k+1}=x_k-\alpha<0$ and $x_{k+2}=x_{k+1}+\alpha=x_k$. So the sequence is eventually periodic with period
$2$, alternating between the value $x_k$ in the interval $(0,\alpha)$ and the value $x_k-\alpha$, which lies in
$(-\alpha,0)$. Such an iterate always exists: while the iterates stay positive they decrease by $\alpha$ at each
step, so one either lands exactly on $0$ or jumps into the interval $(-\alpha,0)$, and the next iterate is then
positive and smaller than $\alpha$.

(b) All later iterates lie in $[-\alpha,\alpha]$, so $f(x_k)=\lvert x_k\rvert\le\alpha$. The sequence converges to
$0$ only if some iterate is exactly $0$ (after which $\operatorname{sign}(0)=0$ freezes it), which happens only
when $x_0$ is an integer multiple of $\alpha$; otherwise the limit does not exist.

*Example.* With $\alpha=0.7$: $2,\,1.3,\,0.6,\,-0.1,\,0.6,\,-0.1,\dots$, and $f$ alternates between $0.6$ and
$0.1$. ✓

(c) The bound is $\min_kf(x_k)\le R^2/(2\alpha K)+\alpha/2$ with $R=2$, which for large $K$ tends to
$\alpha/2=0.35$. The true best value is $\min(0.6,0.1)=0.1\le0.35$, so the bound holds; it is loose because it is
worst-case over all convex $1$-Lipschitz functions. The theorem bounds the best iterate because the last iterate
is not monotone: here $f(x_{k+1})>f(x_k)$ every other step, so no bound on $f(x_K)$ alone can tend to $0$.
