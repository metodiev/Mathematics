# Inner Product Spaces — Exercises

> [Tutorial](README.md) · [Solutions](solutions.md) · Level: Advanced

Thirty-five problems, numbered continuously. Levels are cumulative, and the proofs of the Advanced
section use techniques practised in the Beginner computations.

**How to use this set.**

* Attempt each problem before opening [solutions.md](solutions.md).
* Verify every orthogonality claim by computing the inner product, and every norm claim by squaring it.
* Unless stated otherwise the inner product on $\mathbb{R}^n$ is the dot product, and on $\mathbb{C}^n$ it
  is $\langle\mathbf{z},\mathbf{w}\rangle = \sum_j z_j\overline{w_j}$; on function spaces
  $\langle f,g\rangle = \int_a^b f\bar g$.
* "Orthonormalise" means: run Gram–Schmidt, then divide by the norms.
* Proofs need complete sentences and explicit use of the axioms or theorems.

## Beginner

**1.** For $\mathbf{u} = (3,4,0)$ and $\mathbf{v} = (1,2,2)$ in $\mathbb{R}^3$, compute
$\langle\mathbf{u},\mathbf{v}\rangle$, $\lVert\mathbf{u}\rVert$, $\lVert\mathbf{v}\rVert$ and
$\cos\theta$, where $\theta$ is the angle between them. Verify Cauchy–Schwarz numerically.

**2.** For $\mathbf{u} = (1,-2,2)$ and $\mathbf{v} = (2,1,-2)$, compute the inner product and both norms,
verify Cauchy–Schwarz, and verify the triangle inequality for $\lVert\mathbf{u}+\mathbf{v}\rVert$.

**3.** Decide which of the following pairs are orthogonal.

(a) $(1,2,3)$ and $(2,-1,0)$ in $\mathbb{R}^3$;
(b) $(1,1,0)$ and $(1,-1,1)$ in $\mathbb{R}^3$;
(c) $(1,2)$ and $(2,1)$ in $\mathbb{R}^2$;
(d) $(1,i)$ and $(i,1)$ in $\mathbb{C}^2$.

**4.** Normalise each vector: (a) $(3,4)$; (b) $(1,1,1)$; (c) $(1,-2,2)$; (d) $(1,i)$ in $\mathbb{C}^2$.

**5.** For $\mathbf{u} = (1,0,1)$, $\mathbf{v} = (0,1,1)$, $\mathbf{w} = (1,1,1)$, compute
$d(\mathbf{u},\mathbf{v})$, $d(\mathbf{u},\mathbf{w})$ and $d(\mathbf{w},\mathbf{v})$, and verify the
triangle inequality $d(\mathbf{u},\mathbf{v}) \le d(\mathbf{u},\mathbf{w}) + d(\mathbf{w},\mathbf{v})$.

**6.** In $\mathbb{C}^2$ let $\mathbf{z} = (1+i,\ i)$ and $\mathbf{w} = (1-i,\ 2)$. Compute
$\langle\mathbf{z},\mathbf{w}\rangle$ and $\langle\mathbf{w},\mathbf{z}\rangle$, verify conjugate symmetry,
compute both norms, and check Cauchy–Schwarz.

**7.** Is $\left\{(1,0,0),\ \tfrac{1}{\sqrt2}(0,1,1),\ \tfrac{1}{\sqrt2}(0,1,-1)\right\}$ orthonormal in
$\mathbb{R}^3$? Justify each of the three conditions.

**8.** Find the orthogonal projection of $\mathbf{b} = (3,4)$ onto $W = \operatorname{span}\{(1,1)\}$ and
verify that the residual is orthogonal to $(1,1)$. What is the distance from $\mathbf{b}$ to the line?

**9.** Compute the integrals, which are orthogonality statements for the trigonometric system:
(a) $\int_{-\pi}^{\pi}\sin x\cos x\,dx$; (b) $\int_{-\pi}^{\pi}\sin^2x\,dx$;
(c) $\int_{-\pi}^{\pi}\cos^2x\,dx$; (d) $\int_{-\pi}^{\pi}\sin x\sin 2x\,dx$.

**10.** For $Q = \dfrac{1}{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}$, verify $Q^{\mathsf{T}}Q = I$, compute
$\det Q$, describe the linear map geometrically, and check that it preserves the norms of $(1,0)$ and
$(1,1)$.

**11.** On $C[0,1]$ with $\langle f,g\rangle = \int_0^1fg$, compute $\langle 1,x\rangle$, $\lVert 1\rVert$,
$\lVert x\rVert$ and the angle between the constant function $1$ and $x$.

**12.** Orthonormalise $\{(1,1),(1,0)\}$ in $\mathbb{R}^2$ by Gram–Schmidt, and verify that the result is
orthonormal.

## Intermediate

**13.** Orthonormalise $\mathbf{a}_1 = (1,1,1)$, $\mathbf{a}_2 = (1,1,0)$, $\mathbf{a}_3 = (1,0,0)$ by
Gram–Schmidt. Verify all three orthogonality relations.

**14.** Compute the QR decomposition of $A = \begin{pmatrix}1&2\\1&0\\0&1\end{pmatrix}$ and verify both
$Q^{\mathsf{T}}Q = I$ and $QR = A$.

**15.** Fit a line $y = a+bx$ to the data $(1,1)$, $(2,3)$, $(3,4)$, $(4,6)$ by least squares, using the
normal equations. Verify that both components of the residual are orthogonal to the columns of the design
matrix.

**16.** Fit a quadratic $y = a+bx+cx^2$ to the data $(-1,2)$, $(0,1)$, $(1,3)$, $(2,5)$ by least squares.
Verify $A^{\mathsf{T}}(\mathbf{y}-A\mathbf{x}) = \mathbf{0}$.

**17.** Project $\mathbf{b} = (2,1,3)$ onto $W = \operatorname{span}\{(1,1,0),(0,1,1)\}$ and verify that
the residual is orthogonal to both spanning vectors.

**18.** Find $W^{\perp}$ for $W = \operatorname{span}\{(1,1,1)\} \subseteq \mathbb{R}^3$: give its
dimension, a basis, and verify $\dim W + \dim W^{\perp} = 3$.

**19.** Compute the Fourier coefficients $a_0, a_1, a_2, a_3$ and $b_1,b_2,b_3$ of $f(x) = x^2$ on
$[-\pi,\pi]$, and state the general formula for $a_k$.

**20.** Using Parseval's identity for $f(x) = x^2$ on $[-\pi,\pi]$, prove that
$\sum_{k\ge1}\frac{1}{k^4} = \frac{\pi^4}{90}$.

**21.** Orthogonally diagonalise $A = \begin{pmatrix}3&1\\1&3\end{pmatrix}$: find $Q$ orthogonal and $D$
diagonal with $Q^{\mathsf{T}}AQ = D$.

**22.** For $A = \begin{pmatrix}3&1\\1&3\end{pmatrix}$, find the maximum and minimum of the Rayleigh
quotient $\mathbf{x}^{\mathsf{T}}A\mathbf{x}/\mathbf{x}^{\mathsf{T}}\mathbf{x}$ on $\mathbb{R}^2\setminus\{\mathbf{0}\}$
and the vectors where they are attained.

## Advanced

**23.** Prove the **polarization identity** in a real inner product space:
$\langle\mathbf{u},\mathbf{v}\rangle = \tfrac14\big(\lVert\mathbf{u}+\mathbf{v}\rVert^2 - \lVert\mathbf{u}-\mathbf{v}\rVert^2\big)$.
Deduce that the inner product is determined by the norm it induces.

**24.** (a) Prove the parallelogram law. (b) Show that the norms
$\lVert(x,y)\rVert_1 = \lvert x\rvert+\lvert y\rvert$ and
$\lVert(x,y)\rVert_\infty = \max\{\lvert x\rvert,\lvert y\rvert\}$ on $\mathbb{R}^2$ do **not** satisfy it,
so neither comes from an inner product.

**25.** (a) Prove that if $\mathbf{u}\perp\mathbf{v}$ then $\lVert\mathbf{u}+\mathbf{v}\rVert^2 = \lVert\mathbf{u}\rVert^2+\lVert\mathbf{v}\rVert^2$,
and generalise to pairwise orthogonal vectors. (b) Deduce that for an orthogonal projection $P_W$ and any
$\mathbf{b}$, $\lVert P_W\mathbf{b}\rVert \le \lVert\mathbf{b}\rVert$.

**26.** Prove the Gram–Schmidt theorem: the vectors produced are orthonormal and
$\operatorname{span}\{\mathbf{u}_1,\dots,\mathbf{u}_j\} = \operatorname{span}\{\mathbf{a}_1,\dots,\mathbf{a}_j\}$
for each $j$. (Induction; show $\mathbf{v}_j \neq \mathbf{0}$.)

**27.** Let $P \in M_n(\mathbb{R})$ satisfy $P^2 = P$. (a) Prove that $P$ is the orthogonal projection onto
$\operatorname{col}(P)$ if and only if $P^{\mathsf{T}} = P$. (b) Give an example of an idempotent matrix
that is not symmetric and describe its projection geometrically.

**28.** (a) Prove that $A^{\mathsf{T}}A$ is invertible if and only if the columns of $A$ are linearly
independent. (b) Derive the normal equations by minimising
$F(\mathbf{x}) = \lVert A\mathbf{x}-\mathbf{b}\rVert^2$ with calculus.

**29.** (a) Prove that an orthogonal matrix has $\det Q = \pm1$ and that all its eigenvalues have modulus
$1$. (b) Prove that every $2\times2$ orthogonal matrix is a rotation or a reflection, writing it explicitly
in terms of an angle $\theta$.

**30.** Let $\mathbf{u}_1,\dots,\mathbf{u}_m$ be orthonormal in an inner product space $V$ and
$\mathbf{x} \in V$. (a) Prove Bessel's inequality
$\sum_{i=1}^{m}\lvert\langle\mathbf{x},\mathbf{u}_i\rangle\rvert^2 \le \lVert\mathbf{x}\rVert^2$.
(b) Prove that equality holds if and only if $\mathbf{x} \in \operatorname{span}\{\mathbf{u}_1,\dots,\mathbf{u}_m\}$.

**31.** Prove the spectral theorem for real symmetric $2\times2$ matrices directly: show that
$A = \begin{pmatrix}a&b\\b&d\end{pmatrix}$ has real eigenvalues, orthogonal eigenvectors, and an orthogonal
$Q$ with $Q^{\mathsf{T}}AQ$ diagonal, treating the cases $b = 0$ and $b \neq 0$.

## Challenge

**32.** *(challenge)* Prove that equality holds in the triangle inequality
$\lVert\mathbf{u}+\mathbf{v}\rVert = \lVert\mathbf{u}\rVert+\lVert\mathbf{v}\rVert$ if and only if one of
the vectors is a nonnegative multiple of the other. Deduce the corresponding statement for the equality
case of Cauchy–Schwarz.

**33.** *(challenge)* Orthonormalise $1, x, x^2, x^3$ on $C[-1,1]$ with
$\langle f,g\rangle = \int_{-1}^1fg$, obtaining (up to normalisation) the first four Legendre polynomials.
Verify pairwise orthogonality and compute the four norms.

**34.** *(challenge)* For data $(t_i,y_i)$, $i = 1,\dots,m$, let $S_t = \sum t_i$, $S_{tt} = \sum t_i^2$,
$S_y = \sum y_i$, $S_{ty} = \sum t_iy_i$. Derive the least-squares formulas

$$
b = \frac{mS_{ty}-S_tS_y}{mS_{tt}-S_t^2}, \qquad a = \frac{S_y - bS_t}{m},
$$

prove $mS_{tt} - S_t^2 > 0$ unless all $t_i$ are equal, and show that the sample correlation satisfies
$\lvert r\rvert \le 1$ as a consequence of Cauchy–Schwarz.

**35.** *(challenge)* For the square wave $f(x) = 1$ on $(0,\pi)$ and $f(x) = -1$ on $(-\pi,0)$, compute
the Fourier coefficients, write the series, and use Parseval's identity to prove that
$\sum_{k \text{ odd}}\frac{1}{k^2} = \frac{\pi^2}{8}$.
