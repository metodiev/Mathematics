# Iterative Methods for Linear Systems — Solutions

> [Iterative Methods for Linear Systems](README.md) · Solutions to the 36 problems in [exercises.md](exercises.md)

Each solution begins with the strategy, shows the computation or proof, and closes with a check. Numbers
quoted as "measured" were produced by computation with the stated method and tolerance.

## Beginner

**1.** *Strategy: evaluate the three definitions and substitute into the chain of inequalities.*

$\lVert x\rVert_1 = 3+4+1 = 8$, $\lVert x\rVert_2 = \sqrt{9+16+1} = \sqrt{26} = 5.09902$, and
$\lVert x\rVert_\infty = \max(3,4,1) = 4$. The chain of Proposition 7.1 reads

$$4 \le 5.09902 \le 8 \le \sqrt3\cdot5.09902 = 8.83176 \le 3\cdot4 = 12, \qquad
5.09902\le\sqrt3\cdot4 = 6.92820,$$

and every inequality holds ✓. Note that none of the constants is attained, because $x$ is neither a
coordinate vector nor a multiple of $(1,1,1)$.

**2.** *Strategy: use Theorem 7.3 for the induced norms and compute the singular values for the
$2$-norm.*

Column sums: $\lvert1\rvert+\lvert3\rvert = 4$ and $\lvert-2\rvert+\lvert0\rvert = 2$, so
$\lVert A\rVert_1 = 4$. Row sums: $1+2 = 3$ and $3+0 = 3$, so $\lVert A\rVert_\infty = 3$. Frobenius:
$\lVert A\rVert_F = \sqrt{1+4+9+0} = \sqrt{14} = 3.74166$.

For the spectral norm, $A^{\mathsf{T}}A = \begin{pmatrix}10&-2\\-2&4\end{pmatrix}$, with trace $14$ and
determinant $40-4 = 36$; hence $\lambda = 7\pm\sqrt{49-36} = 7\pm\sqrt{13}$, i.e.
$\lambda_{\max} = 10.60555$, and $\lVert A\rVert_2 = \sqrt{10.60555} = 3.25662$.

Check: $\sqrt{\lVert A\rVert_1\lVert A\rVert_\infty} = \sqrt{12} = 3.46410\ge3.25662$ ✓, and
$\lVert A\rVert_2\le\lVert A\rVert_F$ ✓ (3.25662 ≤ 3.74166).

**3.** *Strategy: invert the $2\times2$ matrix and compute the row and column sums of both factors.*

$A^{-1} = \frac{1}{4\cdot3-1}\begin{pmatrix}3&-1\\-1&4\end{pmatrix}
= \frac{1}{11}\begin{pmatrix}3&-1\\-1&4\end{pmatrix}$.

Column sums of $A$: $4+1 = 5$ and $1+3 = 4$, so $\lVert A\rVert_1 = 5$; column sums of $A^{-1}$:
$\frac{3+1}{11} = \frac{4}{11}$ and $\frac{1+4}{11} = \frac{5}{11}$, so
$\lVert A^{-1}\rVert_1 = \frac{5}{11}$. Hence $\kappa_1(A) = 5\cdot\frac{5}{11} = \frac{25}{11} = 2.27273$.

Row sums give the same numbers because $A$ is symmetric: $\lVert A\rVert_\infty = 5$ and
$\lVert A^{-1}\rVert_\infty = \frac{5}{11}$, so $\kappa_\infty(A) = \frac{25}{11}$ as well. Both exceed
$1$ ✓, and $\kappa_2(A) = \frac{7+\sqrt5}{7-\sqrt5} = 8.236$ is larger, as it must be for a symmetric
matrix with these entries.

**4.** *Strategy: form $D$, $L$, $U$ and carry out the two matrix products.*

$D = \operatorname{diag}(4,3)$, $L = \begin{pmatrix}0&0\\-1&0\end{pmatrix}$,
$U = \begin{pmatrix}0&-1\\0&0\end{pmatrix}$.

Jacobi: $B_J = D^{-1}(L+U) = \begin{pmatrix}0&-\frac14\\-\frac13&0\end{pmatrix}$, whose characteristic
polynomial is $\lambda^{2}-\frac{1}{12}$, so the eigenvalues are $\pm\frac{1}{2\sqrt3} = \pm0.288675$ and
$\rho(B_J) = 0.288675$.

Gauss–Seidel: $D-L = \begin{pmatrix}4&0\\1&3\end{pmatrix}$ has inverse
$\frac{1}{12}\begin{pmatrix}3&0\\-1&4\end{pmatrix}$, so

$$B_{GS} = (D-L)^{-1}U = \frac{1}{12}\begin{pmatrix}3&0\\-1&4\end{pmatrix}
\begin{pmatrix}0&-1\\0&0\end{pmatrix}
= \begin{pmatrix}0&-\frac14\\0&\frac{1}{12}\end{pmatrix}.$$

This is triangular, so $\rho(B_{GS}) = \frac{1}{12} = 0.083333 = \rho(B_J)^{2}$ ✓, confirming Theorem 7.20
for this tridiagonal matrix.

**5.** *Strategy: eigenvalues of a triangular matrix are its diagonal entries; then compare with the norm
bound.*

$B$ is upper triangular, so both eigenvalues equal $0.5$ and $\rho(B) = 0.5<1$; by Theorem 7.14 the
iteration converges for every $x_0$. The $\infty$-norm is
$\lVert B\rVert_\infty = \max(0.5+3,\ 0+0.5) = 3.5>1$. There is no contradiction: $\lVert B\rVert<1$ is a
*sufficient* condition (Proposition 7.5), never necessary. The bound $\lVert B^k\rVert\le\lVert
B\rVert^{k}$ is useless here, but $B^{k} = \begin{pmatrix}0.5^{k}&3k\,0.5^{k-1}\\0&0.5^{k}\end{pmatrix}$
shows explicitly that the off-diagonal term grows for one step ($3k0.5^{k-1}$ is maximal at $k = 1$) and
then decays geometrically. This transient growth is exactly the phenomenon discussed in Problem 35.

**6.** *Strategy: iterate the two scalar formulas and compare the error ratios with $\rho(B_J)$.*

$x_1 = \bigl(\frac{1+0}{2},\frac{1+0}{2}\bigr) = (0.5,0.5)$,
$x_2 = \bigl(\frac{1+0.5}{2},\frac{1+0.5}{2}\bigr) = (0.75,0.75)$,
$x_3 = (0.875,0.875)$. The exact solution is $(1,1)$ (check: $2-1 = 1$ ✓). Sup-norm errors: $0.5$, $0.25$,
$0.125$, with ratios $0.5$ and $0.5$. Here
$B_J = \begin{pmatrix}0&\frac12\\\frac12&0\end{pmatrix}$ has eigenvalues $\pm\frac12$, so
$\rho(B_J) = 0.5$ and the ratios attain it exactly.

**7.** *Strategy: use each updated component immediately.*

$x_1 = \bigl(\frac{1+0}{2},\ \frac{1+0.5}{2}\bigr) = (0.5,0.75)$;
$x_2 = \bigl(\frac{1+0.75}{2},\ \frac{1+0.875}{2}\bigr) = (0.875,0.9375)$;
$x_3 = (0.96875,0.984375)$. Errors: $0.5$, $0.125$, $0.03125$ — ratios $0.25$ each, matching
$\rho(B_{GS}) = \frac14 = \rho(B_J)^{2}$ ✓. One Gauss–Seidel step is already as good as two Jacobi steps,
the practical content of Theorem 7.20.

**8.** *Strategy: solve exactly, perturb, and compare the measured ratio with $\kappa_\infty\lVert\delta
b\rVert_\infty/\lVert b\rVert_\infty$.*

$x = A^{-1}b = \frac{1}{11}(3-2,\ -1+8) = (0.090909,\ 0.636364)$, and
$\delta x = A^{-1}\delta b = \frac{1}{11}(0.03,\ -0.01) = (0.0027273,\ -0.00090909)$.

$$\frac{\lVert\delta x\rVert_\infty}{\lVert x\rVert_\infty} = \frac{0.0027273}{0.636364} = 0.0042857,
\qquad \frac{\lVert\delta b\rVert_\infty}{\lVert b\rVert_\infty} = \frac{0.01}{2} = 0.005 .$$

The bound is $\kappa_\infty(A)\cdot0.005 = 2.27273\cdot0.005 = 0.011364$, so the measured amplification
($0.857$ times the relative data change) is below the worst case by a factor $0.377$ — as expected, since
the bound is attained only for specially aligned data.

**9.** *Strategy: square both sides.*

$\bigl(\sum_i\lvert x_i\rvert\bigr)^{2} = \sum_i x_i^{2}+2\sum_{i<j}\lvert x_i\rvert\lvert x_j\rvert
\ge\sum_i x_i^{2}$, so $\lVert x\rVert_1\ge\lVert x\rVert_2$; taking square roots gives the claim.
Equality holds exactly when every cross term vanishes, i.e. when at most one component of $x$ is nonzero.
(If exactly one is nonzero, both norms equal $\lvert x_i\rvert$.)

**10.** *Strategy: nilpotent matrices have zero spectral radius.*

Let $A = \begin{pmatrix}0&1\\0&0\end{pmatrix}\ne0$. Then $A^{2} = 0$, so both eigenvalues are $0$ and
$\rho(A) = 0$: positive definiteness fails, so $\rho$ is not a norm. For the triangle inequality, take
$B = \begin{pmatrix}0&0\\1&0\end{pmatrix}$, also nilpotent with $\rho(B) = 0$. Then
$A+B = \begin{pmatrix}0&1\\1&0\end{pmatrix}$ has eigenvalues $\pm1$, so
$\rho(A+B) = 1>0 = \rho(A)+\rho(B)$. (Homogeneity $\rho(\alpha A) = \lvert\alpha\rvert\rho(A)$ does hold;
it is the only norm axiom the spectral radius satisfies.)

**11.** *Strategy: write the iteration in the standard form and read off $B$.*

$x_{k+1} = (I-\omega A)x_k+\omega b$, so $M = \frac1\omega I$, $N = \frac1\omega I - A$, and
$B = M^{-1}N = I-\omega A$, consistent with $B = I-M^{-1}A$ ✓.

For $A = \operatorname{diag}(2,3)$ the eigenvalues of $B$ are $1-2\omega$ and $1-3\omega$. Convergence
requires $\lvert1-2\omega\rvert<1$, i.e. $0<\omega<1$, and $\lvert1-3\omega\rvert<1$, i.e.
$0<\omega<\frac23$. The intersection is $0<\omega<\frac23$.

The best choice minimises $\max(\lvert1-2\omega\rvert,\lvert1-3\omega\rvert)$. Balance the two:
$1-2\omega = -(1-3\omega)$ gives $\omega = \frac25$, at which both are $\pm\frac15$ and
$\rho(B) = \frac15 = 0.2$. (Richardson's method is a one-parameter Chebyshev-type acceleration; with two
eigenvalues it can place both $1-\omega\lambda_i$ at equal modulus.)

**12.** *Strategy: write the matrix, use the eigenvalue formula of Section 7.16, and compare.*

$A = \begin{pmatrix}2&-1&0&0\\-1&2&-1&0\\0&-1&2&-1\\0&0&-1&2\end{pmatrix}$, with eigenvalues
$2-2\cos(k\pi/5)$:

$$0.381966,\quad 1.381966,\quad 2.618034,\quad 3.618034 .$$

Hence $\kappa_2(A) = 3.618034/0.381966 = 9.47214$. The asymptotic formula gives
$4(N+1)^{2}/\pi^{2} = 100/\pi^{2} = 10.132$, an overestimate by $7\%$; the exact expression is
$\cot^{2}(\pi h/2)$ with $h = \frac15$, i.e. $\cot^{2}(\pi/10) = 9.47214$ ✓ (Problem 30).

## Intermediate

**13.** *Strategy: use the singular value characterisation.*

$\kappa_2(A) = \sigma_{\max}/\sigma_{\min}$ with $\sigma_{\min}>0$ for nonsingular $A$, so
$\kappa_2\ge1$. Equality means $\sigma_{\max} = \sigma_{\min} = \sigma$, i.e. $A = U\Sigma V^{\mathsf{T}}
= \sigma(UV^{\mathsf{T}})$ with $UV^{\mathsf{T}}$ orthogonal; conversely such an $A$ has all singular
values equal to $\sigma$ and $\kappa_2 = 1$. $\square$

**14.** *Strategy: write both norms in terms of singular values.*

Let $\sigma_1\ge\cdots\ge\sigma_n\ge0$. Then $\lVert A\rVert_2 = \sigma_1$ and
$\lVert A\rVert_F^{2} = \sum_i\sigma_i^{2}$, so $\sigma_1^{2}\le\sum_i\sigma_i^{2}\le n\sigma_1^{2}$,
which is the claim after taking square roots. Sharpness: $A = \operatorname{diag}(1,0,\dots,0)$ gives
$\sigma_1 = 1$ and $\lVert A\rVert_F = 1$ (equality on the left); $A = I$ gives $\lVert A\rVert_2 = 1$ and
$\lVert A\rVert_F = \sqrt n$ (equality on the right). $\square$

**15.** *Strategy: compute both iteration matrices, then reconcile with Theorem 7.20.*

$B_J = \begin{pmatrix}0&-2\\-3&0\end{pmatrix}$ has eigenvalues $\pm\sqrt6$, so
$\rho(B_J) = 2.44949>1$. Next, $D+L = \begin{pmatrix}1&0\\3&1\end{pmatrix}$ has inverse
$\begin{pmatrix}1&0\\-3&1\end{pmatrix}$ and $U = \begin{pmatrix}0&2\\0&0\end{pmatrix}$, so

$$B_{GS} = -(D+L)^{-1}U = -\begin{pmatrix}0&2\\0&-6\end{pmatrix}
= \begin{pmatrix}0&-2\\0&6\end{pmatrix},$$

with eigenvalues $0$ and $6$: $\rho(B_{GS}) = 6>1$. Both methods diverge.

There is no contradiction with Theorem 7.20, which asserts the *relation* $\rho(B_{GS}) = \rho(B_J)^{2}$,
not convergence: indeed $6 = (\sqrt6)^{2}$ ✓. The theorem is silent about whether the common value is
below $1$. Note also that $A$ is not diagonally dominant ($\lvert1\rvert<2$ in the first row) and not
symmetric, so neither Theorem 7.15 nor Theorem 7.19 applies.

**16.** *Strategy: insert $\rho_J$ into the formulas of Section 7.9 and check against a computation.*

From Problem 4, $\rho_J = \frac{1}{\sqrt{12}} = 0.2886751$. Then
$\sqrt{1-\rho_J^{2}} = \sqrt{11/12} = 0.9574271$ and

$$\omega_{\mathrm{opt}} = \frac{2}{1+0.9574271} = 1.0217494,\qquad
\rho(B_{\omega_{\mathrm{opt}}}) = \omega_{\mathrm{opt}}-1 = 0.0217494 .$$

A direct computation of the eigenvalues of $B_\omega = (D-\omega L)^{-1}((1-\omega)D+\omega U)$ at this
$\omega$ gives $0.0217494$ ✓, confirming the formula. The improvement over Gauss–Seidel
($\rho = 0.0833$) is a factor four in iteration count — modest, because this matrix is small and already
well conditioned.

**17.** *Strategy: use submultiplicativity.*

$e_k = B^{k}e_0$, so $\lVert e_k\rVert\le\lVert B^{k}\rVert\lVert e_0\rVert\le\lVert B\rVert^{k}
\lVert e_0\rVert$ by Proposition 7.4. If $\lVert B\rVert<1$, the right side tends to $0$ for every $e_0$,
hence $x_k\to x$ ✓. This proves the "if" direction of Theorem 7.14 using only Proposition 7.5, without
Lemma 7.13; the lemma is needed only for the sharp characterisation.

**18.** *Strategy: differentiate the quadratic and use the stationarity of the previous line search.*

With $x(\alpha) = x_{k-1}+\alpha p_k$,

$$\varphi(x(\alpha)) = \tfrac12x(\alpha)^{\mathsf{T}}Ax(\alpha)-b^{\mathsf{T}}x(\alpha),\qquad
\frac{d\varphi}{d\alpha} = p_k^{\mathsf{T}}\bigl(Ax(\alpha)-b\bigr)
= \alpha p_k^{\mathsf{T}}Ap_k - p_k^{\mathsf{T}}r_{k-1}.$$

Setting the derivative to zero gives $\alpha_k = p_k^{\mathsf{T}}r_{k-1}/(p_k^{\mathsf{T}}Ap_k)$. Since
$\frac{d^{2}\varphi}{d\alpha^{2}} = p_k^{\mathsf{T}}Ap_k>0$ for $A$ positive definite, this stationary point
is the unique minimum.

For the previous step, $x_{k-1}$ minimises $\varphi$ along the line $x_{k-2}+\alpha p_{k-1}$, so the
derivative there vanishes:
$p_{k-1}^{\mathsf{T}}(Ax_{k-1}-b) = -p_{k-1}^{\mathsf{T}}r_{k-1} = 0$ ✓. That is exactly the orthogonality
$r_{k-1}\perp p_{k-1}$ used to simplify $\alpha_k$ to $r_{k-1}^{\mathsf{T}}r_{k-1}/(p_k^{\mathsf{T}}
Ap_k)$ when $p_k = r_{k-1}+\beta_kp_{k-1}$.

**19.** *Strategy: exhibit a polynomial of degree $m$ that annihilates the error.*

Let $\lambda_1,\dots,\lambda_m$ be the distinct eigenvalues and put

$$q(\lambda) = \prod_{j=1}^{m}\frac{\lambda-\lambda_j}{0-\lambda_j} .$$

Then $q(0) = 1$, $\deg q = m$, and $q(A) = 0$ because $A$ is diagonalisable and $q$ vanishes on every
eigenvalue. By Theorem 7.27,
$\lVert e_m\rVert_A = \min_{p(0)=1,\ \deg p\le m}\lVert p(A)e_0\rVert_A\le\lVert q(A)e_0\rVert_A = 0$.
(Equivalently, the minimal polynomial of $A$ with respect to any $r_0$ divides $\prod(\lambda-\lambda_j)$
and hence has degree $\le m$.) $\square$

Applied to $A = I+uu^{\mathsf{T}}$: eigenvalues $1$ and $1+\lVert u\rVert^{2}$, so CG takes at most two
steps.

**20.** *Strategy: compute the first step of preconditioned CG explicitly.*

With $M = A$: $z_0 = A^{-1}r_0$ and $p_1 = z_0$; then
$\gamma_0 = r_0^{\mathsf{T}}A^{-1}r_0$ and

$$\alpha_1 = \frac{\gamma_0}{p_1^{\mathsf{T}}Ap_1}
= \frac{r_0^{\mathsf{T}}A^{-1}r_0}{(A^{-1}r_0)^{\mathsf{T}}A(A^{-1}r_0)}
= \frac{r_0^{\mathsf{T}}A^{-1}r_0}{r_0^{\mathsf{T}}A^{-1}r_0} = 1,$$

so $x_1 = x_0+A^{-1}r_0 = x$: convergence in one step ✓.

With $M = \alpha I$: $M^{-1/2}AM^{-1/2} = A/\alpha$, and every singular value is scaled by $1/\alpha$, so
$\kappa_2 = \sigma_{\max}/\sigma_{\min}$ is unchanged ✓. Only a preconditioner that changes the *relative*
spread of the spectrum helps.

**21.** *Strategy: expand, take norms and absorb the term in $\delta x$.*

From $(A+\delta A)(x+\delta x) = b+\delta b$ and $Ax = b$,
$A\,\delta x = \delta b - \delta A(x+\delta x)$, hence

$$\lVert\delta x\rVert\le\lVert A^{-1}\rVert\lVert\delta b\rVert
+\lVert A^{-1}\rVert\lVert\delta A\rVert\bigl(\lVert x\rVert+\lVert\delta x\rVert\bigr).$$

Rearranging,

$$\lVert\delta x\rVert\bigl(1-\lVert A^{-1}\rVert\lVert\delta A\rVert\bigr)
\le\lVert A^{-1}\rVert\bigl(\lVert\delta b\rVert+\lVert\delta A\rVert\lVert x\rVert\bigr).$$

Divide by $\lVert x\rVert$ and by the bracket, and use
$\lVert\delta b\rVert/\lVert x\rVert\le\lVert A\rVert\lVert\delta b\rVert/\lVert b\rVert$ (from
$\lVert b\rVert\le\lVert A\rVert\lVert x\rVert$):

$$\frac{\lVert\delta x\rVert}{\lVert x\rVert}\le
\frac{\kappa(A)}{1-\kappa(A)\lVert\delta A\rVert/\lVert A\rVert}
\Bigl(\frac{\lVert\delta A\rVert}{\lVert A\rVert}+\frac{\lVert\delta b\rVert}{\lVert b\rVert}\Bigr),$$

as claimed. The hypothesis $\kappa\lVert\delta A\rVert/\lVert A\rVert<1$ guarantees the bracket is
positive. $\square$

**22.** *Strategy: an invariant Krylov space contains the solution.*

Write $m$ for the degree of the minimal polynomial of $A$ with respect to $r_0$; then
$A^{m}r_0\in\mathcal{K}_m(A,r_0)$, so $\mathcal{K}_{m+1} = \mathcal{K}_m$ and $\mathcal{K}_m$ is
$A$-invariant. Since $r_0\in\mathcal{K}_m$ and $\mathcal{K}_m$ is $A$-invariant, also
$x - x_0 = A^{-1}r_0\in\mathcal{K}_m$. Hence the GMRES candidate set $x_0+\mathcal{K}_m$ contains the exact
solution, and the minimiser of $\lVert b-Ax\rVert_2$ over that set has zero residual. $\square$

**23.** *Strategy: read the definitions.*

$\mathcal{K}_k$ is by definition spanned by $k$ vectors, so $\dim\mathcal{K}_k\le k$; and
$\mathcal{K}_k\subseteq\mathcal{K}_{k+1}$ because every generator of the first is a generator of the
second. If $A = I$ and $r_0\ne0$, then $A^{j}r_0 = r_0$ for all $j$, so
$\mathcal{K}_k = \operatorname{span}\{r_0\}$ for every $k\ge1$: dimension $1$ throughout, which is
exactly the case of immediate termination in one step.

**24.** *Strategy: use the Kronecker-sum eigenvalue formula.*

With $T = \operatorname{tridiag}(-1,2,-1)$ of order $3$, $A = I\otimes T+T\otimes I$, so the eigenvalues
are $\mu_j+\mu_k$ where $\mu_j = 2-2\cos(j\pi/4)$, $j = 1,2,3$. Since $\cos(\pi/4) = \frac{\sqrt2}{2}$,
$\cos(\pi/2) = 0$ and $\cos(3\pi/4) = -\frac{\sqrt2}{2}$, the sums are

$$1.1716,\ 2.5858,\ 4,\ 2.5858,\ 4,\ 5.4142,\ 4,\ 5.4142,\ 6.8284 .$$

Hence $\kappa_2 = 6.8284/1.1716 = 5.8284$, which matches a direct computation of
$\operatorname{cond}(A)$ for $n = 9$ ✓. The asymptotic value $4(m+1)^{2}/\pi^{2} = 64/\pi^{2} = 6.4846$
overestimates by $11\%$: for $m = 3$ the grid is far too coarse for the continuum approximation.

## Advanced

**25.** *Strategy: sandwich $\lVert B^{k}\rVert^{1/k}$ between $\rho(B)$ and $\rho(B)+\varepsilon$.*

Lower bound: $\rho(B)^{k} = \rho(B^{k})\le\lVert B^{k}\rVert$ by Proposition 7.5, so
$\rho(B)\le\lVert B^{k}\rVert^{1/k}$ for every $k$ and hence $\rho(B)\le\liminf_k\lVert B^{k}
\rVert^{1/k}$.

Upper bound: fix $\varepsilon>0$ and let $\lVert\cdot\rVert_\varepsilon$ be the norm of Lemma 7.13, in
which $\lVert B\rVert_\varepsilon\le\rho(B)+\varepsilon$. By Theorem 7.2 there is $C$ with
$\lVert X\rVert\le C\lVert X\rVert_\varepsilon$ for all $X$. Then

$$\lVert B^{k}\rVert\le C\lVert B^{k}\rVert_\varepsilon\le C(\rho(B)+\varepsilon)^{k}
\;\Longrightarrow\;\limsup_k\lVert B^{k}\rVert^{1/k}\le\rho(B)+\varepsilon .$$

Letting $\varepsilon\downarrow0$ and combining the two bounds gives
$\lim_k\lVert B^{k}\rVert^{1/k} = \rho(B)$ ✓. The identity explains both the name "spectral radius" and why
the asymptotic rate of a stationary iteration is $\rho(B)$: the average factor per step is exactly
$\rho(B)$ in the limit. $\square$

**26.** *Strategy: compare $\lVert Bx\rVert_A$ with $\lVert x\rVert_A$ using
$y = M^{-1}Ax$.*

Let $A$, $M$, $2M-A$ be symmetric positive definite and $B = I-M^{-1}A$. For $x\ne0$ put
$y = M^{-1}Ax\ne0$. Since $M$ is symmetric, $x = A^{-1}My$ and $x^{\mathsf{T}}A = y^{\mathsf{T}}M$, so

$$x^{\mathsf{T}}AM^{-1}Ax = (Ax)^{\mathsf{T}}M^{-1}(Ax) = (My)^{\mathsf{T}}M^{-1}(My) = y^{\mathsf{T}}My,$$

$$x^{\mathsf{T}}AM^{-1}AM^{-1}Ax = (M^{-1}Ax)^{\mathsf{T}}A(M^{-1}Ax) = y^{\mathsf{T}}Ay .$$

Now expand $\lVert Bx\rVert_A^{2} = (x-M^{-1}Ax)^{\mathsf{T}}A(x-M^{-1}Ax)$:

$$\lVert x\rVert_A^{2}-\lVert Bx\rVert_A^{2}
= 2x^{\mathsf{T}}AM^{-1}Ax - x^{\mathsf{T}}AM^{-1}AM^{-1}Ax = 2y^{\mathsf{T}}My-y^{\mathsf{T}}Ay
= y^{\mathsf{T}}(2M-A)y>0 .$$

So $\lVert Bx\rVert_A<\lVert x\rVert_A$ for every $x\ne0$, i.e. $\lVert B\rVert_A<1$, and by Proposition
7.5 $\rho(B)<1$: the iteration converges. $\square$

For Jacobi, $M = D$; the hypothesis becomes "$A$ and $2D-A$ are SPD". For the Poisson matrix,
$2D-A = 4I-A$ has eigenvalues $4-(2-2\cos(k\pi h)) = 2+2\cos(k\pi h)>0$, so Jacobi converges — as Theorem
7.15 also shows, since Poisson is strictly diagonally dominant. The theorem is more general: it gives
convergence for any SPD $A$ whose diagonal dominates in the quadratic-form sense, without requiring strict
row dominance.

**27.** *Strategy: count distinct eigenvalues, then examine the degenerate case.*

$A = I+uu^{\mathsf{T}}$ has eigenvalues $1$ (on $u^{\perp}$, multiplicity $n-1$) and $1+\lVert u
\rVert^{2}$ (on $\operatorname{span}\{u\}$). Two distinct eigenvalues, so by Problem 19 conjugate gradients
terminates in at most two steps ✓.

If $u^{\mathsf{T}}r_0 = 0$ then $Ar_0 = r_0$ and $\mathcal{K}_1 = \operatorname{span}\{r_0\}$ is invariant;
moreover $A^{-1}r_0 = r_0 - u(u^{\mathsf{T}}r_0)/(1+\lVert u\rVert^{2}) = r_0$, so the solution lies in
$x_0+\mathcal{K}_1$ and one step suffices. A numerical run with $u\propto(1,2,-1)$, $b = (1,0,0)$ (for
which $u^{\mathsf{T}}r_0\ne0$) took exactly $2$ iterations to reach $10^{-14}$ ✓.

**28.** *Strategy: diagonal preconditioning with a constant diagonal is scalar scaling.*

If $a_{ii} = c>0$ for all $i$ then $D = cI$ and $D^{-1/2}AD^{-1/2} = A/c$. Scaling by $1/c$ multiplies
every singular value by $1/c$, so $\kappa_2(A/c) = \kappa_2(A)$ ✓. For the Poisson matrix $c = 2$, hence
diagonal preconditioning changes nothing: measured iteration counts for $N = 31$ were $31$ with and
without the preconditioner.

A useful preconditioner must reduce the *relative spread* of the spectrum, which here comes from the
coupling between neighbouring grid points. Incomplete Cholesky, SSOR and multigrid all do this; the
multigrid V-cycle reduces $\kappa$ to $O(1)$ and the iteration count to a handful, independent of $h$.

**29.** *Strategy: use the spectral theorem and the definition of the $2$-norm.*

For symmetric positive definite $A$ there is an orthonormal basis of eigenvectors with eigenvalues
$0<\lambda_{\min} = \lambda_1\le\cdots\le\lambda_n = \lambda_{\max}$. Then
$\lVert A\rVert_2 = \max_{\lVert x\rVert=1}\lVert Ax\rVert = \lambda_{\max}$ (attained at an eigenvector)
and $\lVert A^{-1}\rVert_2 = 1/\lambda_{\min}$, so $\kappa_2 = \lambda_{\max}/\lambda_{\min}\ge1$ ✓.

Equality holds iff $\lambda_{\max} = \lambda_{\min}$, i.e. $A = \lambda I$ ✓. Finally, if $Q$ is orthogonal
then $(Q^{\mathsf{T}}AQ)$ is symmetric positive definite with the same eigenvalues, and the $2$-norm is
orthogonally invariant ($\lVert Q^{\mathsf{T}}AQ\rVert_2 = \lVert A\rVert_2$ because the singular values
are unchanged); hence $\kappa_2(Q^{\mathsf{T}}AQ) = \kappa_2(A)$: the condition number is a
basis-independent property of the linear map. $\square$

**30.** *Strategy: verify the eigenvector ansatz, then simplify with double-angle identities.*

Let $h = 1/(N+1)$ and $v_j = \sin(jk\pi h)$ for $j = 1,\dots,N$. Then $v_0 = 0 = v_{N+1}$, so the boundary
conditions hold, and using $\sin((j-1)\theta)+\sin((j+1)\theta) = 2\sin(j\theta)\cos\theta$ with
$\theta = k\pi h$,

$$(Av)_j = 2v_j - v_{j-1}-v_{j+1} = \bigl(2-2\cos(k\pi h)\bigr)v_j .$$

Hence $\lambda_k = 2-2\cos(k\pi h)$, $k = 1,\dots,N$, and

$$\lambda_{\min} = 2-2\cos(\pi h),\qquad \lambda_{\max} = 2-2\cos(N\pi h) = 2 + 2\cos(\pi h),$$

because $N\pi h = \pi-\pi h$ and $\cos(\pi-\theta) = -\cos\theta$. Therefore

$$\kappa_2 = \frac{1+\cos(\pi h)}{1-\cos(\pi h)}
= \frac{2\cos^{2}(\pi h/2)}{2\sin^{2}(\pi h/2)} = \cot^{2}\frac{\pi h}{2} .$$

As $h\to0$, $\cos(\pi h) = 1-\frac{\pi^{2}h^{2}}{2}+O(h^{4})$, so
$\kappa_2 = \frac{2+O(h^{2})}{\pi^{2}h^{2}/2+O(h^{4})}\sim\frac{4}{\pi^{2}h^{2}}$ ✓. Check for $N = 4$
($h = 1/5$): $\cot^{2}(\pi/10) = 9.47214$, matching the computed value in Problem 12 ✓.

**31.** *Strategy: bound $\rho(A^{\mathsf{T}}A)$ by a matrix norm and apply submultiplicativity.*

$\lVert A\rVert_2^{2} = \rho(A^{\mathsf{T}}A)\le\lVert A^{\mathsf{T}}A\rVert_\infty\le
\lVert A^{\mathsf{T}}\rVert_\infty\lVert A\rVert_\infty$. Since $\lVert A^{\mathsf{T}}\rVert_\infty =
\lVert A\rVert_1$ (the largest row sum of $A^{\mathsf{T}}$ is the largest column sum of $A$), this is
$\lVert A\rVert_1\lVert A\rVert_\infty$ ✓.

Equality: let $J$ be the $n\times n$ matrix of all ones. Then $\lVert J\rVert_1 = \lVert J\rVert_\infty = n$
and $\lVert J\rVert_2 = n$ (its only nonzero eigenvalue is $n$, with eigenvector $(1,\dots,1)$), so
$n = \sqrt{n\cdot n}$ ✓ — equality holds.

**32.** *Strategy: solve the quadratic in $\sqrt\lambda$ and impose the double-root condition.*

Put $s = \sqrt\lambda$. Young's relation becomes $s^{2}-\omega\mu s+(\omega-1) = 0$, so

$$s = \frac{\omega\mu\pm\sqrt{\omega^{2}\mu^{2}-4(\omega-1)}}{2},
\qquad \lambda = s^{2}.$$

For fixed $\omega$ the largest modulus occurs at the largest $\lvert\mu\rvert = \rho_J$. If the
discriminant is positive, $\lvert s\rvert$ increases with $\mu$; the spectral radius as a function of
$\omega$ is minimised where the discriminant vanishes, since for smaller $\omega$ the quadratic has real
roots of larger modulus and for larger $\omega$ the roots become complex with modulus
$\sqrt{\omega-1}$ (constant in $\mu$ but increasing in $\omega$). Setting
$\omega^{2}\rho_J^{2} = 4(\omega-1)$ gives

$$\omega = \frac{2\bigl(1\pm\sqrt{1-\rho_J^{2}}\bigr)}{\rho_J^{2}},$$

and the root below $2$ is $\omega_{\mathrm{opt}} = 2/\bigl(1+\sqrt{1-\rho_J^{2}}\bigr)$ (rationalise the
numerator). At the double root $s = \omega\rho_J/2$, so
$\lambda_{\max} = s^{2} = \omega^{2}\rho_J^{2}/4 = \omega-1$ by the discriminant equation, i.e.
$\rho(B_{\omega_{\mathrm{opt}}}) = \omega_{\mathrm{opt}}-1$ ✓. $\square$

## Challenge

**33.** *Strategy: compute $\kappa$, run CG, and compare with the bound.*

The Hilbert matrix $H_4$ has $\kappa_2(H_4) = 1.5514\times10^{4}$, so the bound of Theorem 7.28 predicts

$$\tfrac12\sqrt{\kappa}\ln\frac{2}{\varepsilon} = \tfrac12\cdot124.55\cdot23.72 \approx 1477
\ \text{iterations}$$

for a relative residual $10^{-10}$. Measured: CG finished in $5$ iterations, with relative residuals
$1.0$, $4.0\times10^{-1}$, $8.7\times10^{-2}$, $1.1\times10^{-2}$, $1.1\times10^{-9}$,
$1.2\times10^{-12}$.

The explanation is finite termination: $H_4$ is $4\times4$ and has four distinct eigenvalues, so by
Problem 19 the exact answer is reached in at most four steps. The fifth iteration appears only because
roundoff prevents the fourth residual from reaching exactly zero. The $\kappa$-bound is a worst-case bound
*uniform over all matrices with that condition number and all right-hand sides*; it cannot see that $n$
is tiny. For a large ill-conditioned matrix (a discretised PDE, say) the bound becomes meaningful and the
$\sqrt\kappa$ growth is observed.

**34.** *Strategy: use the two-dimensional eigenvalue formula and expand for small $h$.*

On an $m\times m$ interior grid with $h = 1/(m+1)$, the five-point Laplacian has eigenvalues
$\lambda_{jk} = 4-2\cos(j\pi h)-2\cos(k\pi h)$, so

$$\lambda_{\min} = 4-4\cos(\pi h)\approx 2\pi^{2}h^{2},\qquad
\lambda_{\max} = 4+4\cos(\pi h)\approx 8,$$

giving $\kappa_2\approx 4/(\pi^{2}h^{2})$ as claimed in Section 7.16.

*Jacobi:* $D = 4I$, so $\rho(B_J) = 1-\lambda_{\min}/4\approx1-\pi^{2}h^{2}/2$, and the number of
iterations per factor $e$ is about $1/(1-\rho_J)\approx2/(\pi^{2}h^{2}) = \Theta(m^{2}) = \Theta(n)$.

*Conjugate gradients:* the asymptotic rate is $1-2/\sqrt\kappa = 1-\pi h$, so iterations per factor $e$
are $\Theta(1/h) = \Theta(m) = \Theta(\sqrt n)$.

*Measured* (tolerance $10^{-6}$, constant right-hand side):

| $m$ | $n$ | $\kappa_2$ | Jacobi | Gauss–Seidel | CG |
|---|---|---|---|---|---|
| 8 | 64 | 32.2 | 221 | 112 | 10 |
| 12 | 144 | 67.8 | 464 | 233 | 18 |
| 16 | 256 | 116.5 | 796 | 399 | 25 |

Jacobi grows by factors $2.10$ and $1.72$ when $m$ grows by $1.5$ and $1.33$ (the squares would be $2.25$
and $1.78$): consistent with $\Theta(m^{2})$. CG grows by $1.80$ and $1.39$, consistent with
$\Theta(m)$. The measured counts are smaller than the asymptotic constants suggest — 25 rather than ~40
at $m = 16$ — because the bound is a worst case, not a prediction.

**35.** *Strategy: take an upper triangular matrix with a large off-diagonal entry.*

Let $B = \begin{pmatrix}0&2\\0&\frac12\end{pmatrix}$. Its eigenvalues are $0$ and $\frac12$, so
$\rho(B) = \frac12<1$. But

$$B^{\mathsf{T}}B = \begin{pmatrix}0&0\\0&4+\tfrac14\end{pmatrix}
\Longrightarrow \lVert B\rVert_2 = \sqrt{4.25} = 2.06155>1 .$$

With $e_0 = (0,1)$: $e_1 = (2,\tfrac12)$ of norm $2.06155$, $e_2 = (1,\tfrac14)$ of norm $1.03078$,
$e_3 = (\tfrac12,\tfrac18)$ of norm $0.51539$. The error grows for two iterations and then decays
geometrically at rate $\tfrac12$.

This does not contradict Theorem 7.14: convergence is a statement about $k\to\infty$, and the theorem's
quantitative form uses the special norm of Lemma 7.13, in which $B$ is already a contraction. In the
$2$-norm the growth is transient: $B^{k} = \begin{pmatrix}0&2\cdot0.5^{k-1}\\0&0.5^{k}\end{pmatrix}$ has
norm $2\cdot0.5^{k-1}$, which exceeds $1$ only for $k\le2$. Non-normal iteration matrices routinely show
such transients, and they are the reason a short run of iterations can look worse than the asymptotic
rate.

**36.** *Strategy: bound the spectrum by the stochasticity of $P$, then compute the geometric decay.*

$B = \alpha P^{\mathsf{T}}$, and the eigenvalues of $P^{\mathsf{T}}$ are those of the stochastic matrix $P$,
all of modulus at most $1$ (if $Pv = \mu v$ and $v\ne0$, take a component of maximal modulus:
$\lvert\mu\rvert\lvert v_i\rvert\le\sum_j p_{ij}\lvert v_j\rvert\le\lvert v_i\rvert$). Also $\mu = 1$ is
an eigenvalue, with left eigenvector the stationary distribution. Hence $\rho(B) = \alpha$, and the error
decays like $\alpha^{k}$.

Iterations to reduce the error by $10^{-6}$: $k = \ln(10^{-6})/\ln\alpha$, giving

$$\alpha = 0.85:\quad k = \frac{-13.8155}{-0.16252} = 85.0\ \Rightarrow\ 86, \qquad
\alpha = 0.99:\quad k = \frac{-13.8155}{-0.01005} = 1374.6\ \Rightarrow\ 1375 .$$

So the damping factor $\alpha$ alone determines the cost — remarkably, independently of the size of the
web, since the rate is $\alpha$ and not a function of $n$.

The condition number of $I-\alpha P^{\mathsf{T}}$ blows up as $\alpha\to1$: at $\alpha = 1$ the matrix is
singular, because $P^{\mathsf{T}}\pi = \pi$ for the stationary vector $\pi$, so $(I-P^{\mathsf{T}})\pi = 0$.
For $\alpha<1$ the smallest singular value is of order $(1-\alpha)$ times a constant depending on the
spectral gap of $P$, hence $\kappa(I-\alpha P^{\mathsf{T}}) = O(1/(1-\alpha))$: the price of the fast
geometric rate for the *iteration* is a badly conditioned *linear system*. This is why PageRank is computed
by the power iteration rather than by a direct solve.

