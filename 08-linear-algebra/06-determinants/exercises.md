# Determinants — Exercises

> [Tutorial](README.md) · [Solutions](solutions.md) · Level: Advanced

Thirty-six problems, numbered continuously. Levels are cumulative: proofs in Advanced use the properties
established in Beginner computations.

**How to use this set.**

* Attempt each problem on paper before opening [solutions.md](solutions.md).
* Compute every determinant **twice**, by two different methods (expansion against elimination, or against
  a known factorisation). A single arithmetic slip is invisible in a single computation.
* When a determinant is claimed zero, say *why* — a zero row, two proportional rows, a repeated column, or
  rank less than $n$.
* Proof problems require every hypothesis and every theorem named. "It is obvious" is not a proof.
* Unless stated otherwise, matrices are real, "$M_{ij}$" is the $(i,j)$-minor and $C_{ij} = (-1)^{i+j}M_{ij}$
  the cofactor.

## Beginner

**1.** Compute: (a) $\begin{vmatrix}3&4\\1&2\end{vmatrix}$; (b) $\begin{vmatrix}-2&5\\3&-1\end{vmatrix}$;
(c) $\begin{vmatrix}a&b\\b&a\end{vmatrix}$; (d) $\begin{vmatrix}0&1\\1&0\end{vmatrix}$.

**2.** Compute $\det\begin{pmatrix}2&-1&3\\ 0&4&1\\ 5&2&-2\end{pmatrix}$ by cofactor expansion along the
first row.

**3.** Compute the determinant of $\begin{pmatrix}1&2&3\\ 0&0&0\\ 4&5&6\end{pmatrix}$ and justify the answer
from the defining properties rather than from arithmetic.

**4.** Compute $\det\begin{pmatrix}2&5&1&3\\ 0&-1&4&2\\ 0&0&3&7\\ 0&0&0&5\end{pmatrix}$.

**5.** Let $A$ be $3\times3$ with $\det A = 2$. Compute $\det(3A)$, $\det(-A)$ and $\det(A^{\mathsf{T}})$.

**6.** Compute the determinant of $\begin{pmatrix}1&2&3\\ 2&4&6\\ 7&1&5\end{pmatrix}$ and identify the
property of the determinant that makes the answer immediate.

**7.** For $A = \begin{pmatrix}1&2&3\\ 4&5&6\\ 7&8&10\end{pmatrix}$, compute $\det A$ and $\det A^{\mathsf{T}}$
independently.

**8.** Write down the three $3\times3$ elementary matrices: a row swap, a row scaled by $5$, and the
addition of $-2$ times row 1 to row 3. Give each determinant.

**9.** Solve $\begin{vmatrix}x&2\\ 8&x\end{vmatrix} = 0$ for $x \in \mathbb{R}$.

**10.** Decide by determinant which of these matrices are invertible:
$A = \begin{pmatrix}1&2&3\\0&1&4\\5&6&0\end{pmatrix}$,
$B = \begin{pmatrix}2&4\\1&2\end{pmatrix}$,
$C = \begin{pmatrix}1&0&2\\0&1&0\\3&0&1\end{pmatrix}$.

## Intermediate

**11.** Using only the Leibniz formula, prove that $\det$ is linear in its first column: for fixed
$\mathbf{a}_2,\dots,\mathbf{a}_n$ and scalars $s, t$,
$\det(s\mathbf{u} + t\mathbf{v},\mathbf{a}_2,\dots,\mathbf{a}_n) = s\det(\mathbf{u},\mathbf{a}_2,\dots)
+ t\det(\mathbf{v},\mathbf{a}_2,\dots)$.

**12.** Prove from the defining properties that a matrix with a row of zeros has determinant $0$.

**13.** Prove that $\det(cA) = c^n\det A$ for $A \in M_n(K)$ and $c \in K$.

**14.** Prove that if $A$ is invertible then $\det(A^{-1}) = 1/\det A$, and that
$\det(A^k) = (\det A)^k$ for every $k \ge 1$.

**15.** For $A = \begin{pmatrix}2&1\\5&3\end{pmatrix}$ and $B = \begin{pmatrix}1&4\\2&1\end{pmatrix}$,
compute $\det A$, $\det B$, $AB$ and $\det(AB)$, and verify multiplicativity.

**16.** For $M = \begin{pmatrix}1&2&0\\ 0&3&1\\ 2&1&1\end{pmatrix}$, compute the cofactors, the adjugate,
$\det M$, and $M^{-1}$. Verify $M\operatorname{adj}M = (\det M)I_3$.

**17.** Solve by Cramer's rule:
$x + 2y + z = 4$, $2x + y - z = 5$, $x - y + 2z = -3$.

**18.** Compute the determinants of
$\begin{pmatrix}1&2&3&4\\ 0&1&2&3\\ 0&0&2&5\\ 0&0&4&1\end{pmatrix}$ and of
$\begin{pmatrix}0&0&1&2\\ 0&0&3&4\\ 5&6&0&0\\ 7&8&0&0\end{pmatrix}$ using block formulas.

**19.** For which real $t$ is $\begin{pmatrix}1&t&t\\ t&1&t\\ t&t&1\end{pmatrix}$ singular?

**20.** Compute $\det\begin{pmatrix}1&1&1\\ 1&2&4\\ 1&4&16\end{pmatrix}$ and state the general
Vandermonde formula for $3\times3$.

## Advanced

**21.** Prove $\det A = \det A^{\mathsf{T}}$ by induction on $n$, using cofactor expansion along the
first row of $A$ and along the first column of $A^{\mathsf{T}}$.

**22.** Prove from the Leibniz formula that swapping two rows of a matrix multiplies its determinant by
$-1$, and deduce that a matrix with two equal rows has determinant $0$.

**23.** Prove that if one row of $A$ is a linear combination of the other rows, then $\det A = 0$.
Deduce that a square matrix whose rows are linearly dependent is singular.

**24.** Prove that if two columns of $A$ are equal then $\det A = 0$, and deduce that
$\operatorname{rank}A < n$ implies $\det A = 0$.

**25.** Prove that $\det(EA) = \det E\det A$ for every elementary matrix $E$ and every $A \in M_n(K)$, and
deduce $\det(AB) = \det A\det B$ for all $A, B \in M_n(K)$ by reducing $A$ to echelon form.

**26.** Prove that similar matrices have equal determinant. Deduce that if $T : V \to V$ is a linear
operator and $B, B'$ are bases of $V$, then $\det[T]_B = \det[T]_{B'}$, so that $\det T$ is well defined.

**27.** Show by counterexample that
$\det\begin{pmatrix}A&B\\C&D\end{pmatrix} \ne \det A\det D - \det B\det C$ for $2\times2$ blocks, and prove
the **Schur complement** formula: if $A$ is invertible, then

$$
\det\begin{pmatrix}A&B\\ C&D\end{pmatrix} = \det A\cdot\det\big(D - CA^{-1}B\big).
$$

**28.** Prove that if $A$ is invertible then $\operatorname{adj}A = \det(A)A^{-1}$, and deduce
$\operatorname{adj}(AB) = \operatorname{adj}(B)\operatorname{adj}(A)$ for invertible $A$ and $B$.

**29.** Prove that for $A \in M_2(K)$, $p_A(\lambda) = \det(\lambda I - A) = \lambda^2 -
(\operatorname{tr}A)\lambda + \det A$. Compute $p_A$ for $A = \begin{pmatrix}3&1\\2&4\end{pmatrix}$ and
verify both coefficients.

**30.** Prove that for blocks of sizes $p\times q$ and $q\times p$,
$\det\begin{pmatrix}0&B\\C&0\end{pmatrix} = (-1)^{pq}\det B\det C$.

## Challenge

**31.** Let $A \in M_n(\mathbb{Z})$ have integer entries. Prove that $A^{-1}$ has integer entries if and
only if $\det A = \pm 1$.

**32.** Prove that for real $A \in M_n(\mathbb{R})$, $\det(A^{\mathsf{T}}A) = (\det A)^2$, and deduce
$\det(A^{\mathsf{T}}A) \ge 0$. Then prove that every real skew-symmetric matrix of odd size is singular.

**33.** Prove that the $n\times n$ matrix with $1$ on the diagonal and $t$ in every off-diagonal position
has determinant $(1-t)^{n-1}\big(1 + (n-1)t\big)$.

**34.** Let $A \in M_{m\times n}(K)$ and $B \in M_{n\times m}(K)$. Prove **Sylvester's identity**
$\det(I_m + AB) = \det(I_n + BA)$.

**35.** Prove the general Vandermonde formula

$$
\det\begin{pmatrix}
1&x_1&x_1^2&\cdots&x_1^{n-1}\\
1&x_2&x_2^2&\cdots&x_2^{n-1}\\
\vdots&\vdots&\vdots&&\vdots\\
1&x_n&x_n^2&\cdots&x_n^{n-1}
\end{pmatrix}
= \prod_{1 \le i < j \le n}(x_j - x_i),
$$

by induction on $n$, using column operations.

**36.** Prove that $\det(\operatorname{adj}A) = (\det A)^{n-1}$ for **every** $A \in M_n(K)$ with $n \ge 2$,
including singular $A$, and deduce $\det(\operatorname{adj}(\operatorname{adj}A)) =
(\det A)^{(n-1)^2}$ when $n \ge 2$.
