# Gradient Methods — Exercises

> [Tutorial](README.md) · 36 problems · Levels: Beginner, Intermediate, Advanced, Challenge

Every problem asks for a computation with justification or for a proof. When you quote a theorem, name it and
check its hypotheses; when you run an iteration by hand, keep four significant figures and state the closed form
if one exists. You may use everything in the [tutorial](README.md).

Full solutions are in [solutions.md](solutions.md). Do not open that file until you have attempted the problems.

## Beginner

**1.** Derive the gradient descent update for $f(x)=x^2-4x$ from the quadratic model of Definition 5.4, then run
two steps from $x_0=0$ with $\alpha=0.2$ and compare with the minimiser.

**2.** For $f(x)=x^2$, run three steps of gradient descent from $x_0=1$ with $\alpha=0.1$, give the closed form for
$x_k$, and compute $f(x_3)$.

**3.** Let $f(x)=\tfrac12\cdot3x^2$. Compute $L$ and $\mu$, then describe the behaviour of the iteration for
$\alpha=\tfrac13$ and for $\alpha=\tfrac23$.

**4.** For $f(x)=\tfrac12x^2$ (so $L=1$), decide which of $\alpha=0.05$, $0.5$, $1$, $2$ give convergence, and
give the factor $1-\alpha$ in each case.

**5.** Let $A=\begin{pmatrix}1&0\\0&2\end{pmatrix}$, $b=(1,1)^{\mathsf T}$ and $f(x)=\tfrac12\lVert Ax-b\rVert^2$.
Compute $\nabla f$, $\nabla^2f$, $L$, $\mu$ and $\kappa$.

**6.** Show that $f(x)=x^4$ has no global smoothness constant $L$. Then run gradient descent from $x_0=1$ with
$\alpha=0.5$ for three steps and describe the behaviour.

**7.** Let $f(x)=\lvert x\rvert$ and run $x_{k+1}=x_k-0.3\operatorname{sign}(x_k)$ from $x_0=2$ for six steps.
Explain why no $L$ exists and what the iterates do.

**8.** Write one AdaGrad update with $\alpha=0.5$, $\varepsilon=0$, $x_0=(0,0)$ and $g_1=(1,-2)$.

**9.** Write one RMSProp update with $\rho=0.9$, $\alpha=0.1$, $v_0=(0,0)$, $x_0=(0,0)$ and $g_1=(1,2)$.

**10.** Write one Adam update with $\beta_1=0.9$, $\beta_2=0.999$, $\varepsilon=0$, $\alpha=0.01$, $m_0=v_0=0$,
$x_0=(0,0)$ and $g_1=(1,1)$. Explain why the answer does not depend on the magnitude of $g_1$.

**11.** Suppose the gradient were constantly $g$. Prove by induction that $m_k=(1-\beta_1^k)g$ and
$v_k=(1-\beta_2^k)g^2$, and deduce that the bias-corrected quantities equal $g$ and $g^2$.

**12.** A gradient estimator has variance $\sigma^2=3.2$. Compute the variance and the standard deviation of a
mini-batch average with $B=1$, $B=8$ and $B=64$.

## Intermediate

**13.** Let $Q=\operatorname{diag}(1,4,9)$ and $f(x)=\tfrac12x^{\mathsf T}Qx$. Compute $\kappa$, the optimal step
$2/(L+\mu)$, the contraction factor, and the number of iterations needed to reduce the error norm by $10^{-6}$.

**14.** Prove Lemma 7.5.1: for $\mu$-strongly convex differentiable $f$,
$\lVert\nabla f(x)\rVert^2\ge2\mu\bigl(f(x)-f^\star\bigr)$.

**15.** Prove the descent lemma from the integral form of Taylor's theorem, stating where Cauchy–Schwarz is used.

**16.** For a quadratic, show that the exact line-search step from $x$ is
$\alpha=\dfrac{g^{\mathsf T}g}{g^{\mathsf T}Qg}$ with $g=\nabla f(x)$. Evaluate it at $x=(1,1)$ for
$Q=\operatorname{diag}(1,4)$ and compare with $1/L$ and with $2/(L+\mu)$.

**17.** For the heavy ball on a one-dimensional quadratic with curvature $\lambda$, derive the characteristic
polynomial of the error recursion and the stability conditions $\beta<1$ and $\alpha<2(1+\beta)/\lambda$.

**18.** For $Q=\operatorname{diag}(4,1)$ and $x_0=(1,1)$, compute the first three Nesterov iterates by hand with
$L=4$, and compare $f(x_k)$ with the bound $2L\lVert x_0\rVert^2/(k+1)^2$.

**19.** Let $f(x)=\tfrac12x^2$ and suppose the gradient estimate is $g=x+0.2$ (a constant bias). Find the fixed
point of the iteration, the suboptimality there, and explain why the bias does not average out.

**20.** A single-sample gradient has standard deviation $4$. Compute the standard deviation of the mini-batch
average for $B=16$ and the batch size needed for a standard deviation of $0.5$.

**21.** AdaGrad on a sparse problem: coordinate $1$ has gradient $1$ at every step and coordinate $2$ has gradient
$1$ only at the first step and $0$ afterwards. Compute $G_{k,1}$ and $G_{k,2}$ after $k$ steps and the effective
steps, and explain why the rare coordinate keeps moving while the frequent one slows down.

**22.** Show that the RMSProp update with $\varepsilon=0$ is invariant to multiplying all gradients by a positive
constant $c$, and that plain gradient descent is not. What does this say about step-size transfer between models
with different loss scales?

**23.** Show that Adam with $\beta_1=\beta_2=0$ reduces to $x_{k+1}=x_k-\alpha\,g_k/(\lvert g_k\rvert+\varepsilon)$
elementwise, and describe the behaviour in one dimension when $\lvert g_k\rvert\gg\varepsilon$.

## Advanced

**24.** Prove Theorem 7.4.1 (the $O(1/k)$ rate) in full, including the telescoping step and the use of
monotonicity.

**25.** Prove Theorem 7.5.2 (the $(1-\mu/L)^k$ rate) in full.

**26.** Prove Theorem 7.3.1 for a quadratic: with $\alpha=2/(L+\mu)$ the error obeys
$\lVert x_k-x^\star\rVert\le\bigl(\tfrac{\kappa-1}{\kappa+1}\bigr)^k\lVert x_0-x^\star\rVert$. Explain why the
same factor is attained for *both* extreme eigenvalues.

**27.** Prove Theorem 7.7.3: the smooth convex SGD bound with variance $\sigma^2$, including the use of the
descent lemma and the substitution of the gradient bound into the distance recursion.

**28.** Analyse SGD with the diminishing step $\alpha_k=\alpha/\sqrt k$. Starting from the telescoping identity
$2\sum_k\alpha_k\bigl(f(x_k)-f^\star\bigr)\le R^2+G^2\sum_k\alpha_k^2$, show that the best iterate satisfies a
bound of order $\ln(K)/\sqrt K$, and state which terms produce the logarithm.

**29.** Derive the heavy-ball stability conditions of Exercise 17 using the criterion that both roots of
$r^2-ar+b$ lie inside the unit disc if and only if $\lvert b\rvert<1$ and $\lvert a\rvert<1+b$.

**30.** Let $U$ be orthogonal and define $g(z)=f(U^{\mathsf T}z)$. Show by induction that gradient descent on $g$
starting from $z_0=Ux_0$ produces $z_k=Ux_k$, where $x_k$ are the gradient descent iterates for $f$. Then show
that for a general invertible $A$ the substitution $z=Ax$ turns gradient descent into preconditioned gradient
descent with preconditioner $A^{-1}A^{-\mathsf T}$, and explain the consequence for preconditioning.

**31.** Prove that for convex $L$-smooth $f$ with $0<\alpha\le1/L$ the squared gradients are summable,
$\sum_{k\ge0}\lVert\nabla f(x_k)\rVert^2<+\infty$, and deduce $\nabla f(x_k)\to0$.

## Challenge

**32.** Adam is not a descent method. Take $\alpha=0.1$, $\beta_1=0.9$, $\beta_2=0.999$, $m_0=v_0=0$, and suppose
the sampled gradients are $g_k=+1$ for $k=1,\dots,10$ and $g_{11}=-1$. Compute $\hat m_{11}$, $\hat v_{11}$ and the
step, and show that the step at $k=11$ points opposite to the current descent direction. By how much does a
locally linear objective with gradient $-1$ increase at that step?

**33.** A mini-batch iteration costs $c=5$ ms of overhead plus $m=0.05$ ms per sample, and the number of iterations
needed is $K(B)=K_1/B$ with $K_1=2\times10^5$. Compute the total time $T(B)$ for $B=1,10,100,1000,10^4$, find
$\lim_{B\to\infty}T(B)$, and identify the smallest $B$ within $5\%$ of the limit.

**34.** You are told that a model's loss has smoothness $L=50$ near the current parameters. Design a
learning-rate sweep: state the grid, the threshold above which you expect divergence, and what you will look for
in the curves. Then explain how the plan changes if the loss also has a large noise floor.

**35.** For a $\mu$-strongly convex, $L$-smooth problem with $\kappa=10^4$, estimate the iterations needed to
reduce $f-f^\star$ by a factor $\varepsilon$ with (a) gradient descent with step $1/L$ and (b) an accelerated
method with rate $(1-1/\sqrt\kappa)^k$. Tabulate for $\varepsilon=10^{-3},10^{-6},10^{-9}$ and give the ratio.

**36.** Three runs report the loss at steps $1,10,100,1000$: run A $(2.0,1.6,1.55,1.54)$, run B
$(2.0,0.9,0.4,0.39)$, run C $(2.0,3.1,`nan`,`nan`)$. Diagnose each run, say what you would change, and say which
extra measurement would separate "noise floor" from "model limitation".
