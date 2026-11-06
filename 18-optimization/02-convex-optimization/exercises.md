# Convex Optimization — Exercises

> [Tutorial](README.md) · 38 problems · Levels: Beginner, Intermediate, Advanced, Challenge

Every problem asks for a proof, a computation, or both. When you invoke a theorem, name it and check its
hypotheses; when you compute a Hessian, state the test you apply (leading principal minors, eigenvalues, or
completing the square). You may use everything in the [tutorial](README.md).

Full solutions are in [solutions.md](solutions.md). Do not open that file until you have attempted the problems.

## Beginner

**1.** Show from Definition 5.2 that $C=\{(x_1,x_2):x_1\ge0,\ x_2\ge0,\ x_1+x_2\le1\}$ is convex.

**2.** (a) Show that $f(x)=3x-5$ is both convex and concave. (b) Show that every affine function
$f(x)=a^{\mathsf T}x+b$ is both convex and concave. (c) Give a function that is both convex and concave on
$\mathbb{R}$ but not affine, or prove that none exists.

**3.** For $f(x)=x^2$, verify by expansion that
$\theta f(x)+(1-\theta)f(y)-f(\theta x+(1-\theta)y)=\theta(1-\theta)(x-y)^2$ for all $x,y$ and
$\theta\in[0,1]$. Evaluate both sides at $x=-1$, $y=3$, $\theta=\tfrac14$.

**4.** Let $f(x)=x^3$. Determine the largest intervals on which $f$ is convex, and show that $f$ is not convex
on $\mathbb{R}$.

**5.** Compute the Hessian of $f(x,y)=x^2+4xy+5y^2$ and decide whether $f$ is convex, strictly convex, or
neither.

**6.** (a) Prove from the triangle inequality that $f(x)=\lvert x\rvert$ is convex. (b) Compute $\partial f(-2)$,
$\partial f(0)$ and $\partial f(3)$.

**7.** Let $C_1=\{x:x_1+x_2\le1\}$ and $C_2=\{x:x_1-x_2\le1\}$. Prove $C_1\cap C_2$ is convex in two ways: from
Lemma 7.1.1 and directly from the definition.

**8.** Prove that $B(c,r)=\{x:\lVert x-c\rVert\le r\}\subseteq\mathbb{R}^n$ is convex, writing out the triangle
inequality step.

**9.** For $f(x)=e^x$, write the first-order inequality of Theorem 7.3.1 at the base point $x=0$ and at the base
point $x=1$. Use the second to bound $e^{1.1}$ from below.

**10.** For $f(x)=x^2$, check the first-order condition at $x=1$ and $y=3$: compute both sides of
$f(y)\ge f(x)+f'(x)(y-x)$ and state the gap.

**11.** Determine the convexity of $f(x)=1/x$ on $(0,\infty)$ and on $(-\infty,0)$, and explain why $f$ is not
convex on $\mathbb{R}\setminus\{0\}$.

**12.** (a) Show that the sublevel set $\{x\in\mathbb{R}:x^2\le1\}$ is convex. (b) Show that $f(x)=x^3$ has every
sublevel set convex, yet $f$ is not convex. What is the name of the property that $f$ does have?

## Intermediate

**13.** Put the linear program "minimise $2x_1+3x_2$ subject to $x_1+x_2\ge4$, $x_1\ge0$, $x_2\ge0$" into
standard form with slack variables, and state its optimal value and optimal point.

**14.** Let $f(x)=\max\{x,1-x\}$. Find the minimiser, the minimum value, and $\partial f$ at the minimiser.
Verify the optimality condition $0\in\partial f(x^\star)$.

**15.** Let $A$ be a symmetric $n\times n$ matrix and $f(x)=x^{\mathsf T}Ax$. Prove that $f$ is convex if and only
if $A\succeq0$.

**16.** Let $f_1,f_2$ be convex. Prove that $f=\max\{f_1,f_2\}$ is convex, using only Definition 5.3.

**17.** Let $f(x,y)$ be jointly convex. Prove that $g(x)=\inf_yf(x,y)$ is convex, being explicit about the role of
$\varepsilon>0$ in the argument.

**18.** Show that $f(x,y)=x^2/y$ is convex on the set $\{(x,y):y>0\}$ by computing its Hessian.

**19.** Show that $f(X)=\lambda_{\max}(X)$ is convex on the set of symmetric matrices, by exhibiting it as a
supremum of linear functions.

**20.** Let $A=\begin{pmatrix}1&1\\1&-1\end{pmatrix}$ and $b=(2,0)^{\mathsf T}$, and let
$f(x)=\lVert Ax-b\rVert^2$. (a) Show that $f$ is convex and find its unique minimiser using the normal equations.
(b) Verify that the residual at the minimiser is zero.

**21.** Derive the dual of "minimise $c^{\mathsf T}x$ subject to $Ax\ge b$, $x\ge0$" and verify weak duality on
the instance $c=(2,3)$, $A=(1,1)$, $b=1$.

**22.** Solve $\min\{x_1^2+x_2^2:x_1+x_2=1\}$ using the KKT conditions, and check the answer geometrically.

**23.** Solve both problems and compare: (a) $\min\{x^2:x\ge0\}$; (b) $\min\{x^2:x\ge1\}$. In each case give the
multiplier and say whether the constraint is active and whether the multiplier is positive.

## Advanced

**24.** Prove that a $\mu$-strongly convex function on a convex set has at most one minimiser, using the
definition with $\theta=\tfrac12$.

**25.** Let $f$ be convex and differentiable. Prove that $\nabla f(x^\star)=0$ if and only if $x^\star$ is a global
minimiser, quoting the theorem used in each direction.

**26.** Consider $\min\{x^2:x\ge1\}$. (a) Compute the dual function and the dual optimal value. (b) Verify that
Slater's condition holds. (c) Verify that the KKT conditions hold at the optimum.

**27.** Prove Theorem 7.3.1 in both directions. In the second direction, explain why
$\varphi(t)=\bigl(g(t)-g(0)\bigr)/t$ is nondecreasing.

**28.** Prove Theorem 7.4.2 in both directions, stating precisely where Lemma 7.4.1 is used.

**29.** Prove that $f$ is convex if and only if $\operatorname{epi}f$ is convex, taking care that
$\operatorname{dom}f$ is convex in the forward direction and that the reverse direction produces the defining
inequality.

**30.** Prove that the perspective $g(x,t)=tf(x/t)$ of a convex $f$ is convex on $t>0$ by writing
$(\theta x_1+(1-\theta)x_2)/T$ as a convex combination of $x_1/t_1$ and $x_2/t_2$ with the weights explicitly
computed.

**31.** (a) Prove that $g(\lambda,\nu)=\inf_xL(x,\lambda,\nu)$ is concave for any problem. (b) Prove weak duality
$d^\star\le p^\star$, including the cases in which one of the two values is infinite.

**32.** Assuming strong duality and that the dual optimum is attained, derive the four KKT conditions, explaining
which inequality in the chain
$f_0(x^\star)=g(\lambda^\star,\nu^\star)\le L(x^\star,\lambda^\star,\nu^\star)\le f_0(x^\star)$
produces which condition.

**33.** Prove Theorem 7.11.6: for convex $f$ with $\lVert g_k\rVert\le G$ and constant step $\alpha$,
$$
\min_{0\le k\le K-1}f(x_k)-f(x^\star)\le\frac{R^2}{2\alpha K}+\frac{\alpha G^2}{2}.
$$
Then explain why the subgradient method is not a descent method, with the example $f(x)=\lvert x\rvert$.

## Challenge

**34.** Let $f(x)=-\sqrt{1-x^2}$ on $[-1,1]$. (a) Show that $f$ is convex. (b) Show that $\partial f(1)=\varnothing$,
by testing the defining inequality against $y\to1^-$. (c) Explain which hypothesis of the standard theorem
"$\partial f(x)\neq\varnothing$ at every interior point" fails.

**35.** Consider $\min\{e^{-x}:x^2/y\le0,\ y>0\}$. (a) Show that the problem is convex and that $p^\star=1$.
(b) Show that no strictly feasible point exists. (c) Compute the dual function and $d^\star$, and the gap.
(d) Explain in one sentence why no supporting hyperplane certifies the value.

**36.** Consider $\min\{x:x^2\le0\}$. (a) Show that $p^\star=0$ and that Slater's condition fails. (b) Show that
strong duality still holds, but that the dual optimum is not attained. (c) Show that no KKT multipliers exist.
(d) Reconcile (b) and (c) with Theorem 7.10.1.

**37.** Let $f(x)=\tfrac12x^{\mathsf T}Qx$ with $Q=\operatorname{diag}(10^4,1)$ and $x_0=(1,1)$, and run gradient
descent with step $\alpha=1/L$. (a) Use Theorem 7.12.2 to find the smallest $k$ guaranteed to give
$f(x_k)\le10^{-6}$. (b) Compute the exact number of steps needed along the flat eigendirection to reach
$10^{-6}$, using $(1-10^{-4})^k\le10^{-6}$. (c) Comment on the ratio of the two numbers.

**38.** Let $f(x)=\lvert x\rvert$ and run $x_{k+1}=x_k-\alpha\operatorname{sign}(x_k)$ from $x_0=2$ with
$0<\alpha<2$. (a) Show that $x_1=2-\alpha$, and that once some iterate lies in $(0,\alpha)$ the sequence
alternates between that value and the same value minus $\alpha$. (b) Deduce that all later iterates satisfy
$\lvert x_k\rvert\le\alpha$, so $f(x_k)\le\alpha$ for all large $k$, and that the iterates converge to $0$ only
if some iterate lands exactly on $0$. (c) Show that the bound of Theorem 7.11.6 is consistent with this, and
explain why the theorem bounds the best iterate rather than the last one.
