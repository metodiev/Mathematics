# Iterative Methods for Linear Systems — Exercises

> [Iterative Methods for Linear Systems](README.md) · 36 problems · Beginner → Challenge · Solutions: [solutions.md](solutions.md)

Each problem names the section of the [tutorial](README.md) that supplies the method. Norms are induced
matrix norms unless stated; $\kappa(A) = \lVert A\rVert\lVert A^{-1}\rVert$; $\rho$ is the spectral
radius; $A = D - L - U$ is the splitting of Section 6, so $B_J = D^{-1}(L+U)$ and $B_{GS} = (D-L)^{-1}U$.
"Converges" always means "for every initial vector". Do not open [solutions.md](solutions.md) before
writing an attempt.

## Beginner

**1.** *(§7.2)* For $x = (3,-4,1)$, compute $\lVert x\rVert_1$, $\lVert x\rVert_2$ and
$\lVert x\rVert_\infty$, and check every inequality of Proposition 7.1 numerically.

**2.** *(§7.3)* For $A = \begin{pmatrix}1&-2\\3&0\end{pmatrix}$ compute $\lVert A\rVert_1$,
$\lVert A\rVert_\infty$, $\lVert A\rVert_F$ and $\lVert A\rVert_2$, and verify
$\lVert A\rVert_2\le\sqrt{\lVert A\rVert_1\lVert A\rVert_\infty}$.

**3.** *(§7.4)* For $A = \begin{pmatrix}4&1\\1&3\end{pmatrix}$ compute $\kappa_1(A)$ and
$\kappa_\infty(A)$ by hand.

**4.** *(§7.5)* For $A = \begin{pmatrix}4&1\\1&3\end{pmatrix}$ write down $B_J$ and $B_{GS}$, and compute
their eigenvalues and spectral radii.

**5.** *(§7.6)* Let $B = \begin{pmatrix}0.5&3\\0&0.5\end{pmatrix}$. Compute $\rho(B)$ and
$\lVert B\rVert_\infty$, and explain why the iteration $x_{k+1} = Bx_k+c$ converges although
$\lVert B\rVert_\infty>1$.

**6.** *(§7.7)* For $A = \begin{pmatrix}2&-1\\-1&2\end{pmatrix}$ and $b = (1,1)$, carry out three Jacobi
iterations from $x_0 = 0$. Compute $\rho(B_J)$ and check that the error ratios approach it.

**7.** *(§7.8)* For the same system carry out three Gauss–Seidel iterations from $x_0 = 0$, compute
$\rho(B_{GS})$, and compare the error ratios with those of Problem 6.

**8.** *(§7.4)* For $A = \begin{pmatrix}4&1\\1&3\end{pmatrix}$ and $b = (1,2)$, perturb the right-hand
side by $\delta b = (0.01,0)$. Compute the exact relative error of $x$ and compare it with the bound of
Theorem 7.6 in the $\infty$-norm.

**9.** *(§7.2)* Prove that $\lVert x\rVert_2\le\lVert x\rVert_1$ for every $x\in\mathbb{R}^{n}$, and
determine when equality holds.

**10.** *(§7.3)* Show that the spectral radius is not a norm, by exhibiting a nonzero matrix with
$\rho(A) = 0$ and a pair with $\rho(A+B) > \rho(A)+\rho(B)$.

**11.** *(§7.5)* For Richardson's iteration $x_{k+1} = x_k+\omega(b-Ax_k)$, write the splitting and the
iteration matrix. For $A = \operatorname{diag}(2,3)$, determine exactly the range of $\omega$ for which the
iteration converges.

**12.** *(§7.16)* For the one-dimensional Poisson matrix with $N = 4$ interior points, write down $A$,
compute its eigenvalues and $\kappa_2(A)$, and compare with the formula $4(N+1)^{2}/\pi^{2}$.

## Intermediate

**13.** *(§7.4)* Prove that $\kappa_2(A)\ge1$ for every nonsingular $A$, with equality if and only if
$A$ is a scalar multiple of an orthogonal matrix.

**14.** *(§7.3)* Prove that $\lVert A\rVert_2\le\lVert A\rVert_F\le\sqrt n\,\lVert A\rVert_2$ for every
$A\in\mathbb{R}^{n\times n}$, and show that both inequalities are sharp.

**15.** *(§7.8)* For $A = \begin{pmatrix}1&2\\3&1\end{pmatrix}$ compute $B_J$ and $B_{GS}$ and their
spectral radii. Deduce that both methods diverge, and explain why this does not contradict Theorem 7.20.

**16.** *(§7.9)* For $A = \begin{pmatrix}4&1\\1&3\end{pmatrix}$ compute $\omega_{\mathrm{opt}}$ from the
formula of Section 7.9, and verify numerically that $\rho(B_{\omega_{\mathrm{opt}}}) =
\omega_{\mathrm{opt}}-1$.

**17.** *(§7.6)* Prove: if $\lVert B\rVert<1$ in some induced norm, then the iteration converges and
$\lVert e_k\rVert\le\lVert B\rVert^{k}\lVert e_0\rVert$.

**18.** *(§7.11)* Derive the step length $\alpha_k = r_{k-1}^{\mathsf{T}}p_k/(p_k^{\mathsf{T}}Ap_k)$ by
minimising $\varphi(x_{k-1}+\alpha p_k)$ over $\alpha$, and show that exactness of the previous step gives
$r_{k-1}^{\mathsf{T}}p_{k-1} = 0$.

**19.** *(§7.12)* Suppose $A$ has exactly $m$ distinct eigenvalues. Prove that conjugate gradients
terminates in at most $m$ steps in exact arithmetic.

**20.** *(§7.13)* Show that preconditioned CG with $M = A$ produces the exact solution in one iteration,
and that with $M = \alpha I$ the preconditioned system has the same condition number as the original.

**21.** *(§7.4)* Derive the error bound of Theorem 7.7 for a perturbation of the matrix as well as the
right-hand side.

**22.** *(§7.14)* Let $m$ be the degree of the minimal polynomial of $A$ with respect to $r_0$ (the
smallest $m$ such that $A^{m}r_0\in\operatorname{span}\{r_0,\dots,A^{m-1}r_0\}$). Prove that GMRES finds
the exact solution in at most $m$ steps.

**23.** *(§7.10)* Prove that $\mathcal{K}_k(A,r_0)\subseteq\mathcal{K}_{k+1}(A,r_0)$ and
$\dim\mathcal{K}_k\le k$. Give an example in which $\dim\mathcal{K}_k = 1$ for every $k\ge1$.

**24.** *(§7.16)* Form the five-point Laplacian for a $3\times3$ interior grid ($n = 9$), compute
$\kappa_2$, and compare with the asymptotic value $4(m+1)^{2}/\pi^{2}$ for $m = 3$.

## Advanced

**25.** *(§7.6)* Prove that for every induced norm, $\rho(B) = \lim_{k\to\infty}\lVert B^{k}
\rVert^{1/k}$.

**26.** *(§7.8)* **Householder–John theorem.** Let $A$ and $M$ be symmetric positive definite with
$2M-A$ symmetric positive definite. Prove that the iteration with matrix $B = I-M^{-1}A$ converges, and
deduce that Jacobi converges for an SPD matrix $A$ with $2D-A$ positive definite.

**27.** *(§7.11)* Let $A = I+uu^{\mathsf{T}}$ with $u\ne0$. Show that conjugate gradients solves $Ax = b$
in at most two iterations, whatever $b$ is, and exhibit the case in which one iteration suffices.

**28.** *(§7.13)* Prove that if all diagonal entries of $A$ equal the same number $c>0$, then the
diagonally preconditioned matrix $D^{-1/2}AD^{-1/2} = A/c$ has the same spectral condition number as $A$.
Deduce that diagonal preconditioning does not help the Poisson matrix of Section 7.16, and explain what a
preconditioner would have to capture instead.

**29.** *(§7.4)* For symmetric positive definite $A$ prove $\kappa_2(A) = \lambda_{\max}/\lambda_{\min}$,
show that $\kappa_2(A)\ge1$ with equality if and only if $A = \alpha I$, and deduce that the condition
number is unchanged by an orthogonal change of basis.

**30.** *(§7.16)* Derive the eigenvalues $2-2\cos(k\pi h)$ of the one-dimensional Poisson matrix and prove

$$\kappa_2(A) = \frac{1+\cos(\pi h)}{1-\cos(\pi h)} = \cot^{2}\frac{\pi h}{2},
\qquad h = \frac{1}{N+1},$$

then show $\kappa_2(A)\sim 4/(\pi^{2}h^{2})$.

**31.** *(§7.3)* Prove $\lVert A\rVert_2\le\sqrt{\lVert A\rVert_1\lVert A\rVert_\infty}$ for every square
matrix, and give an example where equality holds.

**32.** *(§7.9)* **Young's relation.** For a consistently ordered matrix whose Jacobi matrix has real
eigenvalues $\mu$, the SOR eigenvalues satisfy

$$(\lambda+\omega-1)^{2} = \lambda\,\omega^{2}\mu^{2}.$$

Assuming this relation, prove that $\rho(B_\omega)$ is minimised at
$\omega_{\mathrm{opt}} = 2/(1+\sqrt{1-\rho_J^{2}})$ with
$\rho(B_{\omega_{\mathrm{opt}}}) = \omega_{\mathrm{opt}}-1$.

## Challenge

**33.** *(§7.12, §7.4)* Let $A = H_4$ be the $4\times4$ Hilbert matrix and $b = (1,1,1,1)$. Compute
$\kappa_2(A)$, run conjugate gradients to a relative residual $10^{-10}$, and compare the measured
iteration count with the bound of Theorem 7.28. Explain the discrepancy.

**34.** *(§7.16)* For the five-point Laplacian on an $m\times m$ interior grid, use the eigenvalue
formulas to show that Jacobi needs $\Theta(m^{2}) = \Theta(n)$ iterations and conjugate gradients
$\Theta(m) = \Theta(\sqrt n)$ to reduce the error by a fixed factor. Check the prediction against the
measured counts $10, 18, 25$ for $m = 8, 12, 16$.

**35.** *(§7.6)* Construct a $2\times2$ matrix $B$ with $\rho(B) = \tfrac12$ but $\lVert B\rVert_2>1$, and
an initial vector whose error **grows** for two iterations before decaying. Explain why this does not
contradict Theorem 7.14.

**36.** *(§7.12, §12)* In the PageRank iteration $x_{k+1} = \alpha P^{\mathsf{T}}x_k+(1-\alpha)v$ with
$\alpha\in(0,1)$, show that the iteration matrix has spectral radius $\alpha$, and compute how many
iterations are needed to reduce the error by $10^{-6}$ for $\alpha = 0.85$ and $\alpha = 0.99$. Why does
the condition number of $I-\alpha P^{\mathsf{T}}$ grow as $\alpha\to1$?
