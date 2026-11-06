# Eigenvalues and Eigenvectors — Solutions

> [Tutorial](README.md) · [Exercises](exercises.md)

Every exercise is solved in full: the strategy first, then the algebra, then a check. Proofs are written
out completely, with the hypotheses named where they are used.

## Beginner

**1.** *Answer:* $\mathbf{v}_1$ and $\mathbf{v}_3$ are eigenvectors with eigenvalue $4$; $\mathbf{v}_4$ is
an eigenvector with eigenvalue $1$; $\mathbf{v}_2$ is not an eigenvector.

*Strategy:* an eigenvector must satisfy $A\mathbf{v} = \lambda\mathbf{v}$ for a single scalar $\lambda$;
compute the product and compare coordinates.

$$
A\begin{pmatrix}1\\1\end{pmatrix} = \begin{pmatrix}2+2\\1+3\end{pmatrix} = \begin{pmatrix}4\\4\end{pmatrix} = 4\begin{pmatrix}1\\1\end{pmatrix} ✓,
\qquad
A\begin{pmatrix}1\\0\end{pmatrix} = \begin{pmatrix}2\\1\end{pmatrix},
$$

and $(2,1)$ is not a multiple of $(1,0)$ (the second coordinate would have to be $0$). Next,

$$
A\begin{pmatrix}2\\2\end{pmatrix} = \begin{pmatrix}4+4\\2+6\end{pmatrix} = \begin{pmatrix}8\\8\end{pmatrix} = 4\begin{pmatrix}2\\2\end{pmatrix} ✓,
\qquad
A\begin{pmatrix}-2\\1\end{pmatrix} = \begin{pmatrix}-4+2\\-2+3\end{pmatrix} = \begin{pmatrix}-2\\1\end{pmatrix} = 1\cdot\begin{pmatrix}-2\\1\end{pmatrix} ✓ .
$$

Note that $\mathbf{v}_3 = 2\mathbf{v}_1$ is automatically an eigenvector whenever $\mathbf{v}_1$ is, with
the same eigenvalue — scalar multiples of an eigenvector are eigenvectors (Exercise 8(a)). *Check by
invariants:* $\operatorname{tr}A = 5 = 4 + 1$ ✓ and $\det A = 6 - 2 = 4 = 4\cdot1$ ✓.

**2.** *Answer:*
$p_A(\lambda) = \lambda^2 - 6\lambda + 5 = (\lambda-5)(\lambda-1)$; eigenvalues $5$ and $1$;
$E_5 = \operatorname{span}\{(1,1)\}$ and $E_1 = \operatorname{span}\{(-3,1)\}$.

*Strategy:* use $p_A(\lambda) = \lambda^2 - (\operatorname{tr}A)\lambda + \det A$. Here
$\operatorname{tr}A = 2+4 = 6$ and $\det A = 2\cdot4 - 3\cdot1 = 5$, so
$p_A(\lambda) = \lambda^2 - 6\lambda + 5 = (\lambda-5)(\lambda-1)$.

For $\lambda = 5$:

$$
A - 5I = \begin{pmatrix}-3 & 3\\ 1 & -1\end{pmatrix}
\longrightarrow \begin{pmatrix}1 & -1\\ 0 & 0\end{pmatrix}
\;\Rightarrow\; x = y,
\qquad \mathbf{v} = \begin{pmatrix}1\\1\end{pmatrix}.
$$

For $\lambda = 1$:

$$
A - I = \begin{pmatrix}1 & 3\\ 1 & 3\end{pmatrix}
\;\Rightarrow\; x = -3y,
\qquad \mathbf{v} = \begin{pmatrix}-3\\1\end{pmatrix}.
$$

*Check:* $A(1,1) = (5,5) = 5(1,1)$ ✓ and $A(-3,1) = (-6+3,\ -3+4) = (-3,1)$ ✓. The two eigenvectors are
independent (they belong to distinct eigenvalues, Theorem 7.8), so this matrix is diagonalisable.

**3.** *Answer:* (a) $2$, $-3$, $4$; (b) $1$ with algebraic multiplicity $2$, $2$, $-5$; (c) $3$, $-1$,
$2$.

The determinant of a triangular matrix is the product of its diagonal entries. Applying this to
$\lambda I - A$ (which is triangular whenever $A$ is, with diagonal entries $\lambda - a_{ii}$),

$$
p_A(\lambda) = \det(\lambda I - A) = \prod_{i=1}^{n}(\lambda - a_{ii}),
$$

so the eigenvalues are exactly the diagonal entries, each appearing as often as it appears on the
diagonal. For (b) the diagonal is $1,1,2,-5$, so $a_1 = 2$ and $a_2 = a_{-5} = 1$. Note that (c) is lower
triangular, which changes nothing: the same product formula holds.

**4.** *Answer:* $p_A(\lambda) = \lambda^2 - 1$; eigenvalues $1$ and $-1$;
$E_1 = \operatorname{span}\{(1,1)\}$, $E_{-1} = \operatorname{span}\{(1,-1)\}$. The map is the reflection
in the line $y = x$.

For $\lambda = 1$: $A - I = \begin{pmatrix}-1&1\\1&-1\end{pmatrix}$ gives $-x + y = 0$, so $x = y$ and
$\mathbf{v} = (1,1)$. For $\lambda = -1$: $A + I = \begin{pmatrix}1&1\\1&1\end{pmatrix}$ gives $x + y = 0$,
so $\mathbf{v} = (1,-1)$. *Check:* $A(1,1) = (1,1)$ ✓ and $A(1,-1) = (-1,1) = -(1,-1)$ ✓.

Geometrically, the line $y = x$ is fixed pointwise and the perpendicular line $y = -x$ is flipped; that
is exactly a reflection, whose eigenvalues are therefore $1$ (the fixed direction) and $-1$ (the flipped
one). Any reflection in a line through the origin has this spectrum.

**5.** *Answer:* no real eigenvalue; over $\mathbb{C}$ the eigenvalues are $i$ and $-i$, with
eigenvectors $(1,-i)$ and $(1,i)$.

*Strategy:* compute $p_R$ and look at its discriminant. Since $\operatorname{tr}R = 0$ and
$\det R = 0\cdot0 - (-1)\cdot1 = 1$,

$$
p_R(\lambda) = \lambda^2 + 1,
$$

whose discriminant is $0 - 4 = -4 < 0$. Hence there is no real root, and no real $\lambda$ with
$R\mathbf{v} = \lambda\mathbf{v}$: the rotation turns every line.

Over $\mathbb{C}$, $\lambda = \pm i$. For $\lambda = i$, the system $(R - iI)\mathbf{v} = \mathbf{0}$ is

$$
\begin{pmatrix}-i & -1\\ 1 & -i\end{pmatrix}\begin{pmatrix}x\\y\end{pmatrix} = \begin{pmatrix}0\\0\end{pmatrix}
\;\Rightarrow\; -ix - y = 0 \;\Rightarrow\; y = -ix,
$$

so $\mathbf{v} = (1,-i)$. *Verify by direct multiplication:*
$R(1,-i) = (0\cdot1 + (-1)(-i),\ 1\cdot1 + 0\cdot(-i)) = (i,1)$, and
$i(1,-i) = (i, -i^2) = (i,1)$ ✓. Conjugating every entry gives the other pair: $R(1,i) = (-i,1) = -i(1,i)$ ✓.

The complex eigenvalues are not a defect: their modulus is $|i| = 1$, which encodes that $R$ preserves
lengths, and their conjugate pair encodes the rotation angle.

**6.** *Answer:* $\operatorname{tr}A = 2 + (-1) + 4 = 5$, $\det A = 2\cdot(-1)\cdot4 = -8$, and

$$
p_A(\lambda) = (\lambda-2)(\lambda+1)(\lambda-4) = \lambda^3 - 5\lambda^2 + 2\lambda + 8 .
$$

*Check of the middle coefficient:* the pairwise products of the eigenvalues sum to
$2(-1) + 2\cdot4 + (-1)4 = -2 + 8 - 4 = 2$, which is the coefficient of $\lambda$. The constant term is
$(-1)^3\det A = -(-8) = 8$ ✓.

All three quantities are **similarity invariants**, so none of them changes when $A$ is replaced by
$P^{-1}AP$: the characteristic polynomial is unchanged by Theorem 7.13, and trace and determinant are
read off from it (Corollary 7.5). What *would* change is the matrix itself, its eigenvectors (they
become $P^{-1}\mathbf{v}$) and its entries.

**7.** *Proof.* By definition, $0$ is an eigenvalue of $A$ if and only if there is a vector
$\mathbf{v} \neq \mathbf{0}$ with

$$
A\mathbf{v} = 0\cdot\mathbf{v} = \mathbf{0},
$$

that is, if and only if $\ker A \neq \{\mathbf{0}\}$. By the criterion of Lemma 7.2, a square matrix has
nontrivial kernel exactly when it is singular, that is, exactly when $\det A = 0$. Chaining the
equivalences proves the claim. $\blacksquare$

*Remark:* the same argument shows that the eigenspace $E_0$ is precisely $\ker A$, the null space.

**8.** *(a)* Compute

$$
A(c\mathbf{v}) = c\,A\mathbf{v} = c\,\lambda\mathbf{v} = \lambda(c\mathbf{v}),
$$

and $c\mathbf{v} \neq \mathbf{0}$ because $c \neq 0$ and $\mathbf{v} \neq \mathbf{0}$. So $c\mathbf{v}$ is
an eigenvector for $\lambda$.

*(b)* By linearity,

$$
A(\mathbf{v} + \mathbf{w}) = A\mathbf{v} + A\mathbf{w} = \lambda\mathbf{v} + \lambda\mathbf{w} = \lambda(\mathbf{v} + \mathbf{w}).
$$

If $\mathbf{v} + \mathbf{w} \neq \mathbf{0}$ this is exactly the definition of an eigenvector for
$\lambda$; if it is $\mathbf{0}$, the zero vector is not an eigenvector, which is why the case must be
excluded.

*(c)* By definition $E_\lambda = \{\mathbf{v} : A\mathbf{v} = \lambda\mathbf{v}\}$. Every element of
$E_\lambda \setminus \{\mathbf{0}\}$ is an eigenvector by Definition 5.1, and conversely every eigenvector
for $\lambda$ lies in $E_\lambda$ and is nonzero. Parts (a) and (b) are the closure properties that make
$E_\lambda$ a subspace (Proposition 7.6).

**9.** *Answer:* (a) $\operatorname{diag}(1, 1024)$; (b) $\operatorname{diag}(59049, 1/59049)$.

For a diagonal matrix $D = \operatorname{diag}(d_1,\dots,d_n)$ we have
$D^k = \operatorname{diag}(d_1^k,\dots,d_n^k)$, because multiplying diagonal matrices multiplies
corresponding entries. Hence

$$
\begin{pmatrix}1&0\\0&-2\end{pmatrix}^{10} = \begin{pmatrix}1^{10}&0\\0&(-2)^{10}\end{pmatrix}
= \begin{pmatrix}1&0\\0&1024\end{pmatrix},
\qquad
\begin{pmatrix}3&0\\0&\tfrac13\end{pmatrix}^{10}
= \begin{pmatrix}3^{10}&0\\0&3^{-10}\end{pmatrix}
= \begin{pmatrix}59049&0\\0&\tfrac{1}{59049}\end{pmatrix}.
$$

The eigenvalues here are $1$ and $-2$ (respectively $3$ and $\tfrac13$), and the eigenvalues of $A^{10}$
are their tenth powers: $1$ and $1024$ (respectively $3^{10}$ and $3^{-10}$), in agreement with
Exercise 23. Note that the second matrix is the first with every eigenvalue replaced by its reciprocal
times $3^2$; it is harmless but a reminder that eigenvalues of $A^k$ are $\lambda^k$, not $k\lambda$.

**10.** *Answer:* $p_A(\lambda) = \lambda^2 - 5\lambda + 5$, and
$A^{-1} = \tfrac15(5I - A) = \tfrac15\begin{pmatrix}3&-1\\-1&2\end{pmatrix} = \begin{pmatrix}0.6&-0.2\\-0.2&0.4\end{pmatrix}$.

*Verification of Cayley–Hamilton.* With $\operatorname{tr}A = 5$ and $\det A = 6 - 1 = 5$,

$$
p_A(\lambda) = \lambda^2 - 5\lambda + 5, \qquad
A^2 = \begin{pmatrix}2&1\\1&3\end{pmatrix}^2 = \begin{pmatrix}5&5\\5&10\end{pmatrix}.
$$

Then

$$
A^2 - 5A + 5I = \begin{pmatrix}5&5\\5&10\end{pmatrix}
- \begin{pmatrix}10&5\\5&15\end{pmatrix} + \begin{pmatrix}5&0\\0&5\end{pmatrix}
= \begin{pmatrix}0&0\\0&0\end{pmatrix} ✓ .
$$

*Deriving the inverse.* From $A^2 - 5A + 5I = 0$ we get $A^2 - 5A = -5I$, that is
$A(5I - A) = 5I$ (multiply $A^2 - 5A = -5I$ by $-1$: $5A - A^2 = 5I$, i.e. $A(5I - A) = 5I$). Hence

$$
A^{-1} = \tfrac15(5I - A) = \tfrac15\begin{pmatrix}3&-1\\-1&2\end{pmatrix}.
$$

*Check:* $\det A = 5$, so the cofactor formula gives
$A^{-1} = \tfrac15\begin{pmatrix}3&-1\\-1&2\end{pmatrix}$ ✓. Also
$A\cdot\tfrac15(5I - A) = \tfrac15(5A - A^2) = \tfrac15(5A - (5A - 5I)) = I$ ✓.

**11.** *Answer:* eigenvalues $3$ and $1$; unit eigenvectors $(1,1)/\sqrt2$ and $(1,-1)/\sqrt2$, which are
orthogonal.

$p_A(\lambda) = \lambda^2 - 4\lambda + 3 = (\lambda-3)(\lambda-1)$. For $\lambda = 3$:
$A - 3I = \begin{pmatrix}-1&1\\1&-1\end{pmatrix}$ gives $x = y$, so $\mathbf{u}_1 = (1,1)/\sqrt2$. For
$\lambda = 1$: $A - I = \begin{pmatrix}1&1\\1&1\end{pmatrix}$ gives $x = -y$, so
$\mathbf{u}_2 = (1,-1)/\sqrt2$. Orthogonality:

$$
\mathbf{u}_1\cdot\mathbf{u}_2 = \frac{1\cdot1 + 1\cdot(-1)}{2} = 0 ✓,
$$

and both have norm $1$ because $\sqrt{1^2+1^2} = \sqrt2$. This is not an accident: $A$ is symmetric, so
Lemma 7.20 guarantees orthogonality of eigenvectors for distinct eigenvalues. Consequently
$A = Q\operatorname{diag}(3,1)Q^{\mathsf{T}}$ with $Q = \tfrac{1}{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}$.

**12.** *Answer:* the only eigenvalue is $1$ (algebraic multiplicity $2$) and
$E_1 = \operatorname{span}\{(1,0)\}$; the matrix is not diagonalisable.

Since $S_k$ is triangular, $p_{S_k}(\lambda) = (\lambda-1)^2$, so $a_1 = 2$. Now

$$
S_k - I = \begin{pmatrix}0&k\\0&0\end{pmatrix}
$$

has rank $1$ because $k \neq 0$, so $g_1 = 2 - 1 = 1 < 2 = a_1$. Solving directly:
$(S_k - I)(x,y)^{\mathsf{T}} = (ky, 0)^{\mathsf{T}} = \mathbf{0}$ forces $y = 0$, so
$E_1 = \{(x,0)\} = \operatorname{span}\{\mathbf{e}_1\}$.

*Geometrically:* the shear fixes every point of the $x$-axis and slides every horizontal line sideways.
There is exactly one invariant line, so there cannot be a basis of eigenvectors: a basis of
$\mathbb{R}^2$ would need two independent invariant directions. By Theorem 7.9, $g_1 \neq a_1$ is
precisely the failure of diagonalisability.

## Intermediate

**13.** *Answer:*

$$
P = \begin{pmatrix}1&1\\1&-2\end{pmatrix}, \qquad D = \begin{pmatrix}5&0\\0&2\end{pmatrix}, \qquad A = PDP^{-1}.
$$

*Strategy:* find the eigenvalues, then one eigenvector each, then check $AP = PD$.

Since $\operatorname{tr}A = 7$ and $\det A = 12 - 2 = 10$,
$p_A(\lambda) = \lambda^2 - 7\lambda + 10 = (\lambda-5)(\lambda-2)$.

For $\lambda = 5$: $A - 5I = \begin{pmatrix}-1&1\\2&-2\end{pmatrix}$ gives $x = y$, so
$\mathbf{v}_1 = (1,1)^{\mathsf{T}}$. For $\lambda = 2$: $A - 2I = \begin{pmatrix}2&1\\2&1\end{pmatrix}$
gives $2x + y = 0$, so $\mathbf{v}_2 = (1,-2)^{\mathsf{T}}$.

*Verification of $AP = PD$:*

$$
AP = \begin{pmatrix}4&1\\2&3\end{pmatrix}\begin{pmatrix}1&1\\1&-2\end{pmatrix}
= \begin{pmatrix}5&4-2\\5&2-6\end{pmatrix} = \begin{pmatrix}5&2\\5&-4\end{pmatrix},
$$

$$
PD = \begin{pmatrix}1&1\\1&-2\end{pmatrix}\begin{pmatrix}5&0\\0&2\end{pmatrix}
= \begin{pmatrix}5&2\\5&-4\end{pmatrix} ✓ .
$$

Since $\det P = -2 - 1 = -3 \neq 0$, $P$ is invertible and $A = PDP^{-1}$ with
$D = \operatorname{diag}(5,2)$. The eigenvalues of $A$ are $5$ and $2$, distinct, so diagonalisability
was guaranteed in advance (Corollary 7.10).

**14.** *Answer:* yes, $A$ is diagonalisable; one choice is

$$
P = \begin{pmatrix}1&0&1\\0&1&0\\0&0&1\end{pmatrix}, \qquad D = \operatorname{diag}(2,2,3).
$$

*Eigenvalues.* $A$ is block triangular with a $2\times2$ block $2I_2$ and the entry $3$, so
$p_A(\lambda) = (\lambda-2)^2(\lambda-3)$: $a_2 = 2$ and $a_3 = 1$.

*Geometric multiplicities.* For $\lambda = 2$,

$$
A - 2I = \begin{pmatrix}0&0&1\\0&0&0\\0&0&1\end{pmatrix}, \qquad \operatorname{rank} = 1,
\qquad g_2 = 3 - 1 = 2 = a_2 ✓ .
$$

The eigenspace is $\{(x,y,0)\} = \operatorname{span}\{\mathbf{e}_1,\mathbf{e}_2\}$. For $\lambda = 3$,

$$
A - 3I = \begin{pmatrix}-1&0&1\\0&-1&0\\0&0&0\end{pmatrix}, \qquad \operatorname{rank} = 2,
\qquad g_3 = 3 - 2 = 1 = a_3 ✓,
$$

with eigenspace $\{(z,0,z)\} = \operatorname{span}\{(1,0,1)\}$. Both multiplicities agree, so by
Theorem 7.9 the matrix is diagonalisable. *Check:* $A(1,0,1)^{\mathsf{T}} = (3,0,3)^{\mathsf{T}} = 3(1,0,1)^{\mathsf{T}}$ ✓,
while $\mathbf{e}_1,\mathbf{e}_2$ are fixed up to the factor $2$ ✓.

**15.** *Answer:* $B = 2I$ has $g_2 = 2 = a_2$ and is diagonalisable (it is already diagonal); $A$ has
$g_2 = 1 < 2 = a_2$ and is not.

Both matrices satisfy $p(\lambda) = (\lambda-2)^2$, so both have the single eigenvalue $2$ with algebraic
multiplicity $2$. The difference is the *geometric* multiplicity:

$$
A - 2I = \begin{pmatrix}0&1\\0&0\end{pmatrix}, \quad \operatorname{rank} = 1, \quad g_2 = 2-1 = 1;
\qquad
B - 2I = \begin{pmatrix}0&0\\0&0\end{pmatrix}, \quad \operatorname{rank} = 0, \quad g_2 = 2-0 = 2 .
$$

For $A$, the eigenspace is $\{(x,0)\} = \operatorname{span}\{\mathbf{e}_1\}$, a line; two independent
eigenvectors do not exist, so no basis of eigenvectors exists (Theorem 7.9). For $B$, the eigenspace is
all of $\mathbb{R}^2$: every vector is an eigenvector. The distinguishing quantity is $g_\lambda$, not
$a_\lambda$; the pair $(a_\lambda, g_\lambda)$ is the complete local invariant for $2\times2$ matrices.

**16.** *Answer:* eigenvalues $1+i$ and $1-i$; eigenvectors $(1,-i)$ and $(1,i)$; $A^4 = -4I$.

$p_A(\lambda) = \lambda^2 - (\operatorname{tr}A)\lambda + \det A = \lambda^2 - 2\lambda + 2$, with roots

$$
\lambda = \frac{2 \pm \sqrt{4 - 8}}{2} = 1 \pm i .
$$

For $\lambda = 1+i$:

$$
A - (1+i)I = \begin{pmatrix}-i&-1\\1&-i\end{pmatrix}
\;\Rightarrow\; -ix - y = 0 \;\Rightarrow\; y = -ix,
\qquad \mathbf{v} = \begin{pmatrix}1\\-i\end{pmatrix}.
$$

*Check:* $A(1,-i) = (1 + i,\ 1 - i)$ and $(1+i)(1,-i) = (1+i,\ -i + 1) = (1+i,\ 1-i)$ ✓.

*The fourth power.* First $A^2$:

$$
A^2 = \begin{pmatrix}1&-1\\1&1\end{pmatrix}\begin{pmatrix}1&-1\\1&1\end{pmatrix}
= \begin{pmatrix}1-1 & -1-1\\ 1-1 & -1+1\end{pmatrix} = \begin{pmatrix}0&-2\\2&0\end{pmatrix},
$$

so $A^4 = \begin{pmatrix}0&-2\\2&0\end{pmatrix}^2 = \begin{pmatrix}-4&0\\0&-4\end{pmatrix} = -4I$.

*Interpretation.* $A$ is the composition of a rotation by $45^\circ$ with a scaling by $\sqrt2$; indeed
$A = \sqrt2\,R_{45^\circ}$, and the eigenvalues have modulus $\sqrt2$ and argument $\pm 45^\circ$. Four
applications rotate by $180^\circ$ and scale by $(\sqrt2)^4 = 4$: $A^4 = 4R_{180^\circ} = -4I$, as
computed. Consistent with Exercise 23, the eigenvalues of $A^4$ are $(1\pm i)^4 = -4$.

**17.** *Answer:* $u_n = 2\cdot3^n - 2^n$.

*Reduction to a matrix problem.* Put $\mathbf{x}_n = (u_{n+1}, u_n)^{\mathsf{T}}$. Then
$u_{n+2} = 5u_{n+1} - 6u_n$ becomes

$$
\mathbf{x}_n = \begin{pmatrix}u_{n+1}\\u_n\end{pmatrix}
= \begin{pmatrix}5u_n - 6u_{n-1}\\ u_n\end{pmatrix}
= \begin{pmatrix}5 & -6\\ 1 & 0\end{pmatrix}\mathbf{x}_{n-1},
\qquad \mathbf{x}_0 = \begin{pmatrix}u_1\\u_0\end{pmatrix} = \begin{pmatrix}4\\1\end{pmatrix}.
$$

*Eigenvalues.* $p_A(\lambda) = \lambda^2 - 5\lambda + 6 = (\lambda-3)(\lambda-2)$: they are $3$ and $2$,
the roots of the characteristic equation $t^2 = 5t - 6$ of the recurrence.

*Eigenvectors.* For $\lambda = 3$: $A - 3I = \begin{pmatrix}2&-6\\1&-3\end{pmatrix}$ gives $x = 3y$, so
$\mathbf{v}_1 = (3,1)^{\mathsf{T}}$. For $\lambda = 2$: $A - 2I = \begin{pmatrix}3&-6\\1&-2\end{pmatrix}$
gives $x = 2y$, so $\mathbf{v}_2 = (2,1)^{\mathsf{T}}$.

*Initial condition.* Solve $(4,1) = c_1(3,1) + c_2(2,1)$: from the second coordinate $c_1 + c_2 = 1$, and
from the first $3c_1 + 2c_2 = 4$. Subtracting twice the first from the second gives $c_1 = 2$, hence
$c_2 = -1$. Therefore

$$
\mathbf{x}_n = 2\cdot3^n\begin{pmatrix}3\\1\end{pmatrix} - 2^n\begin{pmatrix}2\\1\end{pmatrix},
\qquad
u_n = 2\cdot3^n - 2^n .
$$

*Checks:* $u_0 = 2-1 = 1$ ✓; $u_1 = 6-2 = 4$ ✓; $u_2 = 18-4 = 14$ and $5u_1 - 6u_0 = 20-6 = 14$ ✓;
$u_3 = 54-8 = 46$ and $5\cdot14 - 6\cdot4 = 70-24 = 46$ ✓.

**18.** *Answer:* eigenvalues $1$ and $\tfrac12$; $\boldsymbol{\pi} = (\tfrac25,\tfrac35)$;
$\mathbf{x}_n = \big(\tfrac25 + \tfrac35(\tfrac12)^n,\ \tfrac35 - \tfrac35(\tfrac12)^n\big)$; the limit is
$\boldsymbol{\pi}$.

(a) Both columns sum to $1$, so $1$ is an eigenvalue. Concretely
$\operatorname{tr}P = 1.5$ and $\det P = 0.56 - 0.06 = 0.5$, so

$$
p_P(\lambda) = \lambda^2 - 1.5\lambda + 0.5 = (\lambda-1)(\lambda-\tfrac12),
$$

and the second eigenvalue is $\tfrac12$. The stationary vector satisfies $P\boldsymbol{\pi} = \boldsymbol{\pi}$:

$$
0.7x + 0.2y = x \;\Rightarrow\; 0.2y = 0.3x \;\Rightarrow\; x = \tfrac23 y,
\qquad \boldsymbol{\pi} = \frac{(2,3)}{5} = \left(\tfrac25,\tfrac35\right).
$$

*Check:* $P(0.4,0.6) = (0.28 + 0.12,\ 0.12 + 0.48) = (0.4, 0.6)$ ✓.

(b) An eigenvector for $\lambda = \tfrac12$ is $(1,-1)$, since
$P(1,-1) = (0.7-0.2,\ 0.3-0.8) = (0.5,-0.5)$ ✓. Write $(1,0) = c_1(2,3) + c_2(1,-1)$: the equations are
$2c_1 + c_2 = 1$ and $3c_1 - c_2 = 0$, so $c_1 = \tfrac15$ and $c_2 = \tfrac35$. Hence

$$
\mathbf{x}_n = \tfrac15\begin{pmatrix}2\\3\end{pmatrix} + \tfrac35\left(\tfrac12\right)^n\begin{pmatrix}1\\-1\end{pmatrix}
= \begin{pmatrix}\tfrac25 + \tfrac35(\tfrac12)^n\\[2pt] \tfrac35 - \tfrac35(\tfrac12)^n\end{pmatrix}.
$$

*Check* $n = 1$: $(0.4+0.3,\ 0.6-0.3) = (0.7,0.3) = P(1,0)$ ✓.

(c) Since $\lvert\tfrac12\rvert < 1$, the second term tends to $\mathbf{0}$ and
$\mathbf{x}_n \to (\tfrac25,\tfrac35) = \boldsymbol{\pi}$. The convergence is geometric with rate
$\tfrac12$: the deviation is halved at every step.

**19.** *Answer:* (a) stable; (b) unstable; (c) asymptotically stable.

The principle is that a mode $\mathbf{v}\lambda^k$ (discrete) or $\mathbf{v}e^{\lambda t}$ (continuous)
decays exactly when $\lvert\lambda\rvert < 1$ (discrete) or $\operatorname{Re}\lambda < 0$ (continuous).

(a) $A$ is triangular, so its eigenvalues are the diagonal entries $0.5$ and $0.9$. Both have modulus
$< 1$ (the larger is $0.9$), so every solution satisfies $\mathbf{x}_k \to \mathbf{0}$: stable. The rate
is governed by the slower mode $0.9^k$.

(b) The eigenvalues are $1.2$ and $0.8$. Since $\lvert 1.2\rvert > 1$, the mode along $\mathbf{e}_1$
grows like $1.2^k$: unstable.

(c) $C$ is triangular with eigenvalues $-1$ and $-3$. Both are real and negative, so
$\operatorname{Re}\lambda < 0$ and the equilibrium is asymptotically stable; solutions oscillate (because
of the negative sign) while decaying like $e^{-t}$ and $e^{-3t}$. Equivalently, for the continuous
$2\times2$ criterion: $\operatorname{tr}C = -4 < 0$ and $\det C = 3 > 0$ ✓.

**20.** *Answer:* $p_A(\lambda) = \lambda^2 - 5\lambda + 5$ and $A^3 = 20A - 25I = \begin{pmatrix}15&20\\20&35\end{pmatrix}$.

*Cayley–Hamilton.* With $\operatorname{tr}A = 5$ and $\det A = 6-1 = 5$, the theorem gives
$A^2 - 5A + 5I = 0$, that is $A^2 = 5A - 5I$.

*Reduction of the cube.*

$$
A^3 = A\cdot A^2 = A(5A - 5I) = 5A^2 - 5A = 5(5A - 5I) - 5A = 20A - 25I .
$$

*Numerical check.*
$A^2 = \begin{pmatrix}5&5\\5&10\end{pmatrix}$ and
$A^3 = A\cdot A^2 = \begin{pmatrix}2&1\\1&3\end{pmatrix}\begin{pmatrix}5&5\\5&10\end{pmatrix}
= \begin{pmatrix}10+5 & 10+10\\ 5+15 & 5+30\end{pmatrix} = \begin{pmatrix}15&20\\20&35\end{pmatrix}$;
and $20A - 25I = \begin{pmatrix}40-25 & 20\\ 20 & 60-25\end{pmatrix} = \begin{pmatrix}15&20\\20&35\end{pmatrix}$ ✓.
The eigenvalues of $A$ are $\tfrac{5\pm\sqrt5}{2}$, and indeed $(20\lambda - 25)$ evaluated at them gives
$\lambda^3$, since $\lambda^2 = 5\lambda - 5$.

**21.** *Answer:* $P^{-1}AP = \begin{pmatrix}3&3\\0&2\end{pmatrix}$, with eigenvalues $3,2$, trace $5$ and
determinant $6$ — the same as $A$.

$P = \begin{pmatrix}1&1\\0&2\end{pmatrix}$ has $\det P = 2$, so
$P^{-1} = \tfrac12\begin{pmatrix}2&-1\\0&1\end{pmatrix} = \begin{pmatrix}1&-\tfrac12\\0&\tfrac12\end{pmatrix}$.
Then

$$
AP = \begin{pmatrix}3&1\\0&2\end{pmatrix}\begin{pmatrix}1&1\\0&2\end{pmatrix}
= \begin{pmatrix}3&5\\0&4\end{pmatrix},
\qquad
P^{-1}AP = \begin{pmatrix}1&-\tfrac12\\0&\tfrac12\end{pmatrix}\begin{pmatrix}3&5\\0&4\end{pmatrix}
= \begin{pmatrix}3&5-2\\0&2\end{pmatrix} = \begin{pmatrix}3&3\\0&2\end{pmatrix}.
$$

The result is triangular with diagonal $3,2$, so its eigenvalues are $3$ and $2$; its trace is $5$ and its
determinant $6$. For $A$ the same values hold ($\operatorname{tr}A = 5$, $\det A = 6$, triangular with
diagonal $3,2$). This is Theorem 7.13 in action: similarity preserves the characteristic polynomial, hence
trace and determinant. Note that the *eigenvectors* changed: for $A$ an eigenvector for $2$ is
$(1,-1)$, while for $P^{-1}AP$ it is $P^{-1}(1,-1) = (1.5,-0.5)$.

**22.** *Answer:*

$$
A^n = \frac{1}{2}\begin{pmatrix}3^n + 1 & 3^n - 1\\ 3^n - 1 & 3^n + 1\end{pmatrix}.
$$

*Orthogonal diagonalisation.* $A$ is symmetric, with
$p_A(\lambda) = \lambda^2 - 4\lambda + 3 = (\lambda-3)(\lambda-1)$. Unit eigenvectors:
$\mathbf{u}_1 = (1,1)/\sqrt2$ for $\lambda = 3$ and $\mathbf{u}_2 = (1,-1)/\sqrt2$ for $\lambda = 1$ (they
are orthogonal, as Lemma 7.20 promises). So with
$Q = \tfrac{1}{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}$, which satisfies $Q^{\mathsf{T}}Q = I$,

$$
A = Q\begin{pmatrix}3&0\\0&1\end{pmatrix}Q^{\mathsf{T}} .
$$

*Powers.* By Corollary 7.12, $A^n = Q\operatorname{diag}(3^n,1)Q^{\mathsf{T}}$, and multiplying out,

$$
A^n = \frac12\left[3^n\begin{pmatrix}1&1\\1&1\end{pmatrix} + 1\cdot\begin{pmatrix}1&-1\\-1&1\end{pmatrix}\right]
= \frac12\begin{pmatrix}3^n+1 & 3^n-1\\ 3^n-1 & 3^n+1\end{pmatrix}.
$$

*Check* $n = 3$: $\tfrac12\begin{pmatrix}28&26\\26&28\end{pmatrix} = \begin{pmatrix}14&13\\13&14\end{pmatrix}$,
and indeed $A^3 = A\cdot A^2 = \begin{pmatrix}2&1\\1&2\end{pmatrix}\begin{pmatrix}5&4\\4&5\end{pmatrix}
= \begin{pmatrix}14&13\\13&14\end{pmatrix}$ ✓. Also $n = 1$ returns $A$ ✓.

## Advanced

**23.** *(a)* We prove $A^k\mathbf{v} = \lambda^k\mathbf{v}$ by induction on $k \ge 0$. For $k = 0$ both
sides equal $\mathbf{v}$. If $A^k\mathbf{v} = \lambda^k\mathbf{v}$, then

$$
A^{k+1}\mathbf{v} = A(A^k\mathbf{v}) = A(\lambda^k\mathbf{v}) = \lambda^k A\mathbf{v} = \lambda^k\lambda\mathbf{v} = \lambda^{k+1}\mathbf{v} .
$$

*(b)* If $A$ is invertible, then $\det A \neq 0$. Over $\mathbb{C}$, $\det A$ is the product of the $n$
eigenvalues counted with algebraic multiplicity (Corollary 7.5), so no factor can be zero: $\lambda \neq 0$.
From $A\mathbf{v} = \lambda\mathbf{v}$, apply $A^{-1}$ to both sides:

$$
\mathbf{v} = A^{-1}(\lambda\mathbf{v}) = \lambda A^{-1}\mathbf{v}
\quad\Rightarrow\quad
A^{-1}\mathbf{v} = \lambda^{-1}\mathbf{v},
$$

using $\lambda \neq 0$. Since $\mathbf{v} \neq \mathbf{0}$, this says $\lambda^{-1}$ is an eigenvalue of
$A^{-1}$ with eigenvector $\mathbf{v}$.

*(c)* Part (b) applies to every eigenvalue of $A$, so every $\lambda^{-1}$ is an eigenvalue of $A^{-1}$.
Conversely, applying (b) to $A^{-1}$ (whose inverse is $A$) shows that every eigenvalue $\mu$ of $A^{-1}$
equals $\lambda^{-1}$ for some eigenvalue $\lambda$ of $A$. Hence
$\sigma(A^{-1}) = \{1/\lambda : \lambda \in \sigma(A)\}$. $\blacksquare$

**24.** *(a)* For any square matrix $M$, $\det M = \det M^{\mathsf{T}}$, because the Leibniz formula sums
the same products over inverse permutations. Since $(\lambda I - A)^{\mathsf{T}} = \lambda I - A^{\mathsf{T}}$
(the identity is symmetric and transposition is linear),

$$
p_{A^{\mathsf{T}}}(\lambda) = \det(\lambda I - A^{\mathsf{T}}) = \det\big((\lambda I - A)^{\mathsf{T}}\big) = \det(\lambda I - A) = p_A(\lambda).
$$

Equal characteristic polynomials have equal roots, so $A$ and $A^{\mathsf{T}}$ have the same eigenvalues
with the same algebraic multiplicities.

*(b)* For $A = \begin{pmatrix}2&1\\0&3\end{pmatrix}$ the eigenvalue $2$ has eigenvector $(1,0)$:
$A - 2I = \begin{pmatrix}0&1\\0&1\end{pmatrix}$ forces $y = 0$. For
$A^{\mathsf{T}} = \begin{pmatrix}2&0\\1&3\end{pmatrix}$ the same eigenvalue has eigenvectors given by
$A^{\mathsf{T}} - 2I = \begin{pmatrix}0&0\\1&1\end{pmatrix}$, i.e. $x + y = 0$, so $(1,-1)$ is an
eigenvector. The vectors $(1,0)$ and $(1,-1)$ are different, so the eigenvectors are genuinely not
shared — only the spectrum is. $\blacksquare$

**25.** Suppose $N$ is diagonalisable, so $N = PDP^{-1}$ with $D$ diagonal, and $N^k = 0$ for some $k$.
Then

$$
0 = N^k = (PDP^{-1})^k = PD^kP^{-1},
$$

and multiplying by $P^{-1}$ on the left and $P$ on the right gives $D^k = 0$. For a diagonal matrix
$D = \operatorname{diag}(d_1,\dots,d_n)$ we have $D^k = \operatorname{diag}(d_1^k,\dots,d_n^k)$, so
$d_i^k = 0$ and hence $d_i = 0$ for every $i$. Thus $D = 0$ and $N = P\,0\,P^{-1} = 0$.

For $N = \begin{pmatrix}0&1\\0&0\end{pmatrix}$ we have $N \neq 0$ but
$N^2 = \begin{pmatrix}0&0\\0&0\end{pmatrix} = 0$. If $N$ were diagonalisable it would have to be zero,
which it is not; so $N$ is not diagonalisable. (Consistently, $p_N(\lambda) = \lambda^2$ gives
$a_0 = 2$, while $\operatorname{rank}N = 1$ gives $g_0 = 1$.) $\blacksquare$

**26.** We prove (b) first, since (a) uses it.

*(b)* Write $\lambda = a + bi$ and $A\mathbf{v} = \lambda\mathbf{v}$ with
$\mathbf{v} = \mathbf{u} + i\mathbf{w}$ and $\mathbf{u},\mathbf{w} \in \mathbb{R}^2$. Because $A$ is real,

$$
A\mathbf{u} + iA\mathbf{w} = A(\mathbf{u} + i\mathbf{w}) = (a+bi)(\mathbf{u} + i\mathbf{w})
= (a\mathbf{u} - b\mathbf{w}) + i(b\mathbf{u} + a\mathbf{w}),
$$

where the last step uses $i^2 = -1$. Two complex vectors are equal exactly when their real and imaginary
parts are equal, so

$$
A\mathbf{u} = a\mathbf{u} - b\mathbf{w}, \qquad A\mathbf{w} = b\mathbf{u} + a\mathbf{w} .
$$

*(a)* Suppose $\mathbf{u},\mathbf{w}$ are linearly dependent. They cannot both be zero, since then
$\mathbf{v} = \mathbf{0}$, which is not an eigenvector. If $\mathbf{u} \neq \mathbf{0}$ and
$\mathbf{w} = c\mathbf{u}$, then by (b)

$$
A\mathbf{u} = a\mathbf{u} - bc\,\mathbf{u} = (a - bc)\mathbf{u},
$$

so $\mathbf{u}$ is a real eigenvector with the real eigenvalue $a - bc$, contradicting the hypothesis that
the eigenvalues $a \pm bi$ are not real. If $\mathbf{u} = \mathbf{0}$ then $\mathbf{w} \neq \mathbf{0}$ and
(b) gives $A\mathbf{w} = a\mathbf{w}$, again a real eigenvalue. Hence $\mathbf{u},\mathbf{w}$ are
independent.

*(c)* In the basis $(\mathbf{u},\mathbf{w})$ the matrix of $A$ has columns equal to the coordinates of
$A\mathbf{u}$ and $A\mathbf{w}$. From (b), $A\mathbf{u} = a\mathbf{u} - b\mathbf{w}$ gives the first column
$(a,-b)^{\mathsf{T}}$ and $A\mathbf{w} = b\mathbf{u} + a\mathbf{w}$ gives the second column
$(b,a)^{\mathsf{T}}$. Hence the matrix is $\begin{pmatrix}a&b\\-b&a\end{pmatrix}$, which is
$r\begin{pmatrix}\cos\theta & \sin\theta\\ -\sin\theta & \cos\theta\end{pmatrix}$ with
$r = \sqrt{a^2+b^2}$ and $\cos\theta = a/r$, $\sin\theta = b/r$: a rotation by $-\theta$ composed with a
scaling by $r$. $\blacksquare$

*Example.* For $A = \begin{pmatrix}1&-1\\1&1\end{pmatrix}$ and $\lambda = 1+i$ the eigenvector is
$(1,-i)$, so $\mathbf{u} = (1,0)$ and $\mathbf{w} = (0,-1)$. In the basis $(\mathbf{u},\mathbf{w})$ the
matrix is $\begin{pmatrix}1&1\\-1&1\end{pmatrix}$, as predicted with $a = b = 1$ ✓.

**27.** Let $p(\lambda) = \det(\lambda I - A^2)$. By hypothesis $p(\mu) = 0$.

*Case $\mu = 0$.* Then $\det(A^2) = 0$, so $\det A = 0$ and $A$ is singular; by Exercise 7, $0$ is an
eigenvalue of $A$, and $\mu = 0 = 0^2$.

*Case $\mu \neq 0$.* Choose $\alpha \in \mathbb{C}$ with $\alpha^2 = \mu$ (every complex number has a
square root). Then the difference of two squares factors:

$$
A^2 - \mu I = (A - \alpha I)(A + \alpha I),
$$

because $\alpha I$ commutes with $A$. Taking determinants and using multiplicativity,

$$
0 = \det(A^2 - \mu I) = \det(A - \alpha I)\det(A + \alpha I).
$$

A product of complex numbers is zero only if a factor is zero, so $\det(A - \alpha I) = 0$ or
$\det(A + \alpha I) = 0$. In the first case $\lambda = \alpha$ is an eigenvalue of $A$; in the second
$\lambda = -\alpha$ is. Either way $\lambda^2 = \alpha^2 = \mu$. $\blacksquare$

**28.** Since $A$ is diagonalisable, $A = PDP^{-1}$ with $D = \operatorname{diag}(d_1,\dots,d_n)$ and $P$
invertible. Since $A$ is invertible, $\det A = \prod_i d_i \neq 0$, so every $d_i \neq 0$ and

$$
A^{-1} = (PDP^{-1})^{-1} = P D^{-1} P^{-1},
\qquad
D^{-1} = \operatorname{diag}(d_1^{-1},\dots,d_n^{-1}).
$$

Thus $A^{-1}$ is similar to a diagonal matrix, hence diagonalisable, and its eigenvalues are
$d_i^{-1} = 1/\lambda_i$. (This agrees with Exercise 23(c), which gives the same conclusion from the
eigenvector definition, without any diagonalisation.) $\blacksquare$

**29.** *(a)* $E_\lambda = \ker(A - \lambda I)$ by definition, and by the rank–nullity theorem applied to
the $n\times n$ matrix $A - \lambda I$,

$$
\dim\ker(A - \lambda I) + \operatorname{rank}(A - \lambda I) = n,
$$

so $g_\lambda = n - \operatorname{rank}(A - \lambda I)$.

*(b)* Assume $p_A$ splits. By Theorem 7.9, $A$ is diagonalisable if and only if $g_\lambda = a_\lambda$
for every eigenvalue. Substituting (a), this is

$$
n - \operatorname{rank}(A - \lambda I) = a_\lambda
\quad\Longleftrightarrow\quad
\operatorname{rank}(A - \lambda I) = n - a_\lambda .
$$

Since $g_\lambda \ge 1$ always, the rank is at most $n-1$; the formula makes this explicit. $\blacksquare$

**30.** *(a)* Let $B = P^{-1}AP$ with $P$ invertible. Multiplying by an invertible matrix does not change
rank, so

$$
\operatorname{rank}B = \operatorname{rank}(P^{-1}AP) = \operatorname{rank}(A).
$$

If $A$ is diagonalisable, $A = QDQ^{-1}$, so $B = (P^{-1}Q)D(P^{-1}Q)^{-1}$ and $P^{-1}Q$ is invertible;
hence $B$ is diagonalisable, with the same diagonal $D$ and therefore the same eigenvalues.

*(b)* Take

$$
A = \begin{pmatrix}0&1\\0&0\end{pmatrix}, \qquad Z = \begin{pmatrix}0&0\\0&0\end{pmatrix}.
$$

Both have the single eigenvalue $0$ with algebraic multiplicity $2$ (both have $p(\lambda) = \lambda^2$).
But $E_0(A) = \operatorname{span}\{(1,0)\}$ while $E_0(Z) = \mathbb{R}^2$, so their eigenvectors differ.
There is no contradiction with (a): the hypothesis of (a) is *similarity*, which is much stronger than
equality of spectra. Here $\operatorname{rank}A = 1 \neq 0 = \operatorname{rank}Z$, so $A$ and $Z$ are not
similar, and (a) says nothing about them. The example also shows that the spectrum does not determine the
eigenvectors, only (for diagonalisable matrices) the matrix up to similarity. $\blacksquare$

**31.** *Claim:* for every $n \ge 1$ and every real symmetric $n\times n$ matrix $A$ there is an
orthonormal basis of $\mathbb{R}^n$ consisting of eigenvectors of $A$, all eigenvalues being real.

*Base case $n = 1$:* a $1\times1$ matrix $[a]$ is symmetric, has the real eigenvalue $a$, and
$\mathbf{e}_1$ is a unit eigenvector.

*Inductive step.* Assume the claim for $n-1$ and let $A$ be real symmetric of size $n$. By Lemma 7.19
(applied with $n \ge 1$) $A$ has a real eigenvalue $\lambda_1$; choose a corresponding eigenvector and
normalise it to $\mathbf{u}_1$. Define

$$
W = \mathbf{u}_1^{\perp} = \{\mathbf{x} \in \mathbb{R}^n : \langle \mathbf{x},\mathbf{u}_1\rangle = 0\},
$$

a subspace of dimension $n-1$.

*$W$ is $A$-invariant.* For $\mathbf{x} \in W$,

$$
\langle A\mathbf{x},\mathbf{u}_1\rangle = \langle \mathbf{x}, A\mathbf{u}_1\rangle
= \langle \mathbf{x}, \lambda_1\mathbf{u}_1\rangle = \lambda_1\langle \mathbf{x},\mathbf{u}_1\rangle = 0,
$$

where symmetry gives the first equality and $\lambda_1$ real is needed so that
$\langle \mathbf{x},\lambda_1\mathbf{u}_1\rangle = \lambda_1\langle\mathbf{x},\mathbf{u}_1\rangle$ with no
conjugation. Hence $A\mathbf{x} \in W$.

*Induction on $W$.* The restriction $A|_W : W \to W$ is symmetric with respect to the same inner product:
for $\mathbf{x},\mathbf{y} \in W$, $\langle A\mathbf{x},\mathbf{y}\rangle = \langle \mathbf{x},A\mathbf{y}\rangle$.
Choosing an orthonormal basis of $W$, this restriction is represented by a real symmetric
$(n-1)\times(n-1)$ matrix, so by the induction hypothesis $W$ has an orthonormal basis
$\mathbf{u}_2,\dots,\mathbf{u}_n$ of eigenvectors of $A|_W$ — hence of $A$.

*Conclusion.* $(\mathbf{u}_1,\mathbf{u}_2,\dots,\mathbf{u}_n)$ is orthonormal (each $\mathbf{u}_j$ with
$j \ge 2$ lies in $W = \mathbf{u}_1^\perp$) and consists of eigenvectors, so it is an orthonormal basis of
$\mathbb{R}^n$. Assembling it as the columns of $Q$ gives $Q^{\mathsf{T}}AQ = D$ diagonal, i.e.
$A = QDQ^{\mathsf{T}}$. $\blacksquare$

*Where symmetry was used:* in the invariance of $W$ (transpose property) and in the symmetry of the
restriction. Without symmetry both steps fail, and indeed non-symmetric matrices need not be
diagonalisable at all.

## Challenge

**32.** Let $M = \begin{pmatrix}I_m & -A\\ B & I_n\end{pmatrix}$ with $A \in M_{m\times n}$ and
$B \in M_{n\times m}$. We compute $\det M$ in two ways using block triangular factorisations (valid
because $I_m$ and $I_n$ are invertible).

*First factorisation.*

$$
\begin{pmatrix}I_m & 0\\ B & I_n\end{pmatrix}\begin{pmatrix}I_m & -A\\ 0 & I_n + BA\end{pmatrix}
= \begin{pmatrix}I_m & -A\\ B & -BA + I_n + BA\end{pmatrix}
= \begin{pmatrix}I_m & -A\\ B & I_n\end{pmatrix} = M .
$$

The first factor is block lower triangular with diagonal blocks $I_m, I_n$, so its determinant is $1$; the
second is block upper triangular with diagonal blocks $I_m$ and $I_n + BA$, so its determinant is
$\det(I_n + BA)$. Hence $\det M = \det(I_n + BA)$.

*Second factorisation.*

$$
\begin{pmatrix}I_m & -A\\ 0 & I_n\end{pmatrix}\begin{pmatrix}I_m + AB & 0\\ B & I_n\end{pmatrix}
= \begin{pmatrix}I_m + AB - AB & -A\\ B & I_n\end{pmatrix} = M .
$$

Now the first factor is block upper triangular with determinant $\det I_m\det I_n = 1$ and the second is
block lower triangular with determinant $\det(I_m + AB)\det I_n = \det(I_m + AB)$. Hence
$\det M = \det(I_m + AB)$.

Comparing the two computations, $\det(I_m + AB) = \det(I_n + BA)$. $\blacksquare$

*Application to characteristic polynomials.* Let $A, B \in M_n(\mathbb{C})$ and $\lambda \neq 0$. Applying
the identity to $\frac{1}{\lambda}A$ and $B$ gives
$\det\big(I_n + \frac{1}{\lambda}AB\big) = \det\big(I_n + \frac{1}{\lambda}BA\big)$, and multiplying by
$\lambda^n$,

$$
\det(\lambda I - AB) = \lambda^n\det\!\left(I_n - \tfrac{1}{\lambda}AB\right)
= \lambda^n\det\!\left(I_n - \tfrac{1}{\lambda}BA\right) = \det(\lambda I - BA).
$$

The two sides are polynomials in $\lambda$ that agree for infinitely many $\lambda$ (all nonzero ones),
so they are equal as polynomials:
$p_{AB} = p_{BA}$. In particular $AB$ and $BA$ have the same eigenvalues with the same algebraic
multiplicities, the same trace and the same determinant.

**33.** *(a)* Write $P = \begin{pmatrix}1-a & b\\ a & 1-b\end{pmatrix}$. Then

$$
\operatorname{tr}P = 2 - a - b, \qquad \det P = (1-a)(1-b) - ab = 1 - a - b + ab - ab = 1 - a - b,
$$

so

$$
p_P(\lambda) = \lambda^2 - (2-a-b)\lambda + (1-a-b) = \big(\lambda - 1\big)\big(\lambda - (1-a-b)\big),
$$

which shows that $1$ is an eigenvalue and the other eigenvalue is $1 - a - b$. Since $0 < a < 1$ and
$0 < b < 1$, we have $0 < a + b < 2$, hence

$$
-1 < 1 - a - b < 1, \qquad\text{i.e.}\qquad \lvert 1 - a - b\rvert < 1 .
$$

*(b)* A stationary vector satisfies $P\boldsymbol{\pi} = \boldsymbol{\pi}$. From the first row,

$$
(1-a)x + by = x \;\Longrightarrow\; by = ax \;\Longrightarrow\; x = \frac{b}{a}y .
$$

(Here $a \neq 0$.) Normalising $x + y = 1$ gives $y\left(\frac{b}{a} + 1\right) = 1$, so

$$
\boldsymbol{\pi} = \begin{pmatrix}\dfrac{b}{a+b}\\[4pt] \dfrac{a}{a+b}\end{pmatrix},
$$

and both entries are strictly positive because $a, b > 0$.

*(c)* An eigenvector for $\lambda_2 = 1-a-b$ is $(1,-1)^{\mathsf{T}}$, since
$P(1,-1) = (1-a-b,\ a - (1-b)) = (1-a-b)(1,-1)$ ✓. If $\mathbf{x}_0 = (x_0,y_0)$ has entries summing to
$1$, write $\mathbf{x}_0 = \boldsymbol{\pi} + c(1,-1)$; the second coordinate gives
$y_0 = \frac{a}{a+b} - c$, so $c$ is determined. Then

$$
P^n\mathbf{x}_0 = \boldsymbol{\pi} + c(1-a-b)^n\begin{pmatrix}1\\-1\end{pmatrix}
\longrightarrow \boldsymbol{\pi},
$$

because $\lvert 1-a-b\rvert < 1$ by (a). The convergence is geometric with rate
$\lvert 1-a-b\rvert$, which is smaller the larger $a+b$ is. Both entries of the limit are positive, so the
limit does not depend on the starting vector: the chain is ergodic. $\blacksquare$

**34.** *Step 1: $B$ preserves every eigenspace of $A$.* Let $A\mathbf{v} = \lambda\mathbf{v}$ with
$\mathbf{v} \neq \mathbf{0}$. Using $AB = BA$,

$$
A(B\mathbf{v}) = (AB)\mathbf{v} = (BA)\mathbf{v} = B(A\mathbf{v}) = B(\lambda\mathbf{v}) = \lambda(B\mathbf{v}).
$$

So $B\mathbf{v} \in E_\lambda(A)$. Since $A$ has $n$ distinct eigenvalues, each eigenspace is
one-dimensional (Theorem 7.7 gives $1 \le g_\lambda \le a_\lambda = 1$). Therefore $B\mathbf{v}$ is a
multiple of $\mathbf{v}$: there is a scalar $\mu$ with $B\mathbf{v} = \mu\mathbf{v}$.

*Step 2: a polynomial that matches $B$ on a basis.* Choose eigenvectors
$\mathbf{v}_1,\dots,\mathbf{v}_n$ with $A\mathbf{v}_i = \lambda_i\mathbf{v}_i$; they form a basis because
the $\lambda_i$ are distinct (Theorem 7.8). By Step 1, $B\mathbf{v}_i = \mu_i\mathbf{v}_i$ for scalars
$\mu_i$.

The $\lambda_i$ are distinct, so the Lagrange interpolation polynomial

$$
f(t) = \sum_{i=1}^{n} \mu_i\prod_{j \neq i}\frac{t - \lambda_j}{\lambda_i - \lambda_j}
$$

is well defined (no denominator vanishes), has degree at most $n-1$, and satisfies
$f(\lambda_i) = \mu_i$: every term except the $i$-th contains the factor $t - \lambda_i$ and vanishes at
$t = \lambda_i$, while the $i$-th term equals $\mu_i$.

*Step 3: conclude.* For each basis vector,

$$
f(A)\mathbf{v}_i = f(\lambda_i)\mathbf{v}_i = \mu_i\mathbf{v}_i = B\mathbf{v}_i,
$$

using that polynomials in $A$ act on eigenvectors by $A^k\mathbf{v} = \lambda^k\mathbf{v}$
(Exercise 23). Two linear maps that agree on a basis are equal, so $B = f(A)$. $\blacksquare$

**35.** Recall $\varphi = (1+\sqrt5)/2 \approx 1.6180$ and $\psi = (1-\sqrt5)/2 \approx -0.6180$; they are
the two roots of $t^2 = t + 1$, and $\varphi - \psi = \sqrt5$.

*(a)* Since $\sqrt5 < 3$, we have $\lvert\psi\rvert = (\sqrt5 - 1)/2 < (3-1)/2 = 1$. Hence
$\lvert\psi\rvert^n \le \lvert\psi\rvert < 1$ for $n \ge 1$, and dividing by $\sqrt5 > 1$,

$$
\frac{\lvert\psi\rvert^n}{\sqrt5} < \frac{1}{\sqrt5} < \frac12 .
$$

*(b)* By Binet's formula (Example 9.5), $F_n = \dfrac{\varphi^n - \psi^n}{\sqrt5}$, so

$$
\left\lvert F_n - \frac{\varphi^n}{\sqrt5}\right\rvert = \frac{\lvert\psi\rvert^n}{\sqrt5} < \frac12 .
$$

If an integer $F_n$ lies within distance $< \tfrac12$ of a real number $x = \varphi^n/\sqrt5$, then $F_n$
is the unique integer nearest to $x$: any other integer $m \neq F_n$ satisfies
$\lvert m - x\rvert \ge \lvert m - F_n\rvert - \lvert F_n - x\rvert > 1 - \tfrac12 = \tfrac12$.

*(c)* With $\varphi^{20}/\sqrt5 \approx 6765.0000296$, the nearest integer is $6765$, and indeed
$F_{20} = 6765$ ✓. The correction $\lvert\psi\rvert^{20}/\sqrt5 \approx 0.0000296$ is exactly the gap,
which confirms (b) quantitatively. $\blacksquare$
