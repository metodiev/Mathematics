# Eigenvalues and Eigenvectors — Exercises

> [Tutorial](README.md) · [Solutions](solutions.md) · Level: Advanced

Thirty-five problems, numbered continuously. The levels are cumulative: an Advanced problem often
uses a technique first practised in a Beginner one.

**How to use this set.**

* Attempt each problem on paper before opening [solutions.md](solutions.md).
* Every eigenvalue computation must be **checked** with $\operatorname{tr}A = \sum\lambda_i$ and
  $\det A = \prod\lambda_i$; every claimed eigenvector must be checked by multiplying it by $A$.
* Unless stated otherwise $A$ is a real matrix, and "eigenvalue" means "eigenvalue over $\mathbb{R}$";
  problems that ask for complex eigenvalues say so.
* A proof needs complete sentences, every hypothesis used, and both directions whenever an
  "if and only if" is claimed.
* Problems marked *(challenge)* are competition-flavoured or open-ended; they may use ideas from
  outside the tutorial, but everything needed is stated in the problem.

## Beginner

**1.** Let $A = \begin{pmatrix}2 & 2\\ 1 & 3\end{pmatrix}$. Decide which of the following vectors are
eigenvectors of $A$, and give the eigenvalue in each case:
$\mathbf{v}_1 = (1,1)$, $\mathbf{v}_2 = (1,0)$, $\mathbf{v}_3 = (2,2)$, $\mathbf{v}_4 = (-2,1)$.

**2.** Find the characteristic polynomial, the eigenvalues and a basis of each eigenspace for
$A = \begin{pmatrix}2 & 3\\ 1 & 4\end{pmatrix}$.

**3.** Read off the eigenvalues (with algebraic multiplicities) of the following triangular matrices.

(a) $\begin{pmatrix}2 & 7 & -1\\ 0 & -3 & 5\\ 0 & 0 & 4\end{pmatrix}$;
(b) $\begin{pmatrix}1 & 2 & 0 & 0\\ 0 & 1 & 3 & 0\\ 0 & 0 & 2 & 7\\ 0 & 0 & 0 & -5\end{pmatrix}$;
(c) $\begin{pmatrix}3 & 0 & 0\\ 2 & -1 & 0\\ 5 & 7 & 2\end{pmatrix}$.

**4.** For $A = \begin{pmatrix}0 & 1\\ 1 & 0\end{pmatrix}$, find $p_A$, both eigenvalues, and a basis of
each eigenspace. Describe the map geometrically.

**5.** Show that $R = \begin{pmatrix}0 & -1\\ 1 & 0\end{pmatrix}$ has no real eigenvalue. Then find its
complex eigenvalues and a complex eigenvector for each, and verify $R\mathbf{v} = \lambda\mathbf{v}$ by
direct multiplication.

**6.** A $3\times 3$ matrix $A$ has eigenvalues $2$, $-1$ and $4$. Write down
$\operatorname{tr}A$, $\det A$ and $p_A(\lambda)$, and explain which of these three quantities would
change if $A$ were replaced by a similar matrix.

**7.** Prove that $0$ is an eigenvalue of $A \in M_n(\mathbb{R})$ if and only if $A$ is singular.

**8.** Let $\lambda$ be an eigenvalue of $A$.

(a) Prove that if $\mathbf{v}$ is an eigenvector for $\lambda$ and $c \neq 0$, then $c\mathbf{v}$ is also
an eigenvector for $\lambda$.
(b) Prove that if $\mathbf{v}$ and $\mathbf{w}$ are eigenvectors for $\lambda$, then $\mathbf{v} + \mathbf{w}$
is either $\mathbf{0}$ or an eigenvector for $\lambda$.
(c) Deduce that $E_\lambda \setminus \{\mathbf{0}\}$ is exactly the set of eigenvectors for $\lambda$.

**9.** Compute $A^{10}$ for

(a) $A = \begin{pmatrix}1 & 0\\ 0 & -2\end{pmatrix}$;
(b) $A = \begin{pmatrix}3 & 0\\ 0 & \tfrac13\end{pmatrix}$.

**10.** For $A = \begin{pmatrix}2 & 1\\ 1 & 3\end{pmatrix}$, verify the Cayley–Hamilton theorem by direct
computation, and use it to write $A^{-1}$ as a polynomial in $A$.

**11.** For $A = \begin{pmatrix}2 & 1\\ 1 & 2\end{pmatrix}$, find the eigenvalues and a unit eigenvector
for each, and verify that the two eigenvectors are orthogonal.

**12.** Let $S_k = \begin{pmatrix}1 & k\\ 0 & 1\end{pmatrix}$ with $k \neq 0$. Find all eigenvalues and
all eigenvectors of $S_k$, and explain geometrically why no basis of eigenvectors can exist.

## Intermediate

**13.** Diagonalise $A = \begin{pmatrix}4 & 1\\ 2 & 3\end{pmatrix}$: find $P$ and $D$ with
$A = PDP^{-1}$, and verify $AP = PD$ by direct multiplication.

**14.** Decide whether $A = \begin{pmatrix}2 & 0 & 1\\ 0 & 2 & 0\\ 0 & 0 & 3\end{pmatrix}$ is
diagonalisable. If it is, exhibit $P$ and $D$; if not, prove it is not.

**15.** Compare $A = \begin{pmatrix}2 & 1\\ 0 & 2\end{pmatrix}$ and $B = \begin{pmatrix}2 & 0\\ 0 & 2\end{pmatrix}$.
Both have the single eigenvalue $2$ with algebraic multiplicity $2$. Show that $B$ is diagonalisable and
$A$ is not, and explain which multiplicity distinguishes them.

**16.** For $A = \begin{pmatrix}1 & -1\\ 1 & 1\end{pmatrix}$ find the complex eigenvalues, an eigenvector
for each, and compute $A^4$. Interpret the answer geometrically.

**17.** Solve the recurrence $u_{n+2} = 5u_{n+1} - 6u_n$ with $u_0 = 1$ and $u_1 = 4$, by converting it
to a matrix difference equation and diagonalising. Verify your formula for $n = 0,1,2,3$.

**18.** A two-state Markov chain has transition matrix
$P = \begin{pmatrix}0.7 & 0.2\\ 0.3 & 0.8\end{pmatrix}$ (columns sum to $1$).

(a) Find both eigenvalues of $P$ and a stationary distribution $\boldsymbol{\pi}$.
(b) Starting from $\mathbf{x}_0 = (1,0)$, find a closed formula for $\mathbf{x}_n = P^n\mathbf{x}_0$.
(c) What happens as $n \to \infty$?

**19.** Classify the equilibrium $\mathbf{0}$ of $\mathbf{x}_{k+1} = A\mathbf{x}_k$ as stable or unstable
for (a) $A = \begin{pmatrix}0.5 & 1\\ 0 & 0.9\end{pmatrix}$ and (b) $A = \begin{pmatrix}1.2 & 0\\ 0 & 0.8\end{pmatrix}$.
Then classify the equilibrium of $\mathbf{x}' = C\mathbf{x}$ for (c) $C = \begin{pmatrix}-1 & 2\\ 0 & -3\end{pmatrix}$.

**20.** For $A = \begin{pmatrix}2 & 1\\ 1 & 3\end{pmatrix}$, compute $p_A$, use Cayley–Hamilton to express
$A^3$ as a linear combination of $A$ and $I$, and verify the result numerically.

**21.** Let $A = \begin{pmatrix}3 & 1\\ 0 & 2\end{pmatrix}$ and $P = \begin{pmatrix}1 & 1\\ 0 & 2\end{pmatrix}$.
Compute $P^{-1}AP$ and confirm that it has the same eigenvalues, trace and determinant as $A$.

**22.** For $A = \begin{pmatrix}2 & 1\\ 1 & 2\end{pmatrix}$, find a closed formula for $A^n$, valid for
every $n \ge 1$, and check it for $n = 3$.

## Advanced

**23.** Let $A \in M_n(\mathbb{F})$, $k \in \mathbb{N}$, and let $\mathbf{v}$ be an eigenvector of $A$ with
eigenvalue $\lambda$.

(a) Prove $A^k\mathbf{v} = \lambda^k\mathbf{v}$.
(b) If $A$ is invertible, prove that $\lambda \neq 0$ and $A^{-1}\mathbf{v} = \lambda^{-1}\mathbf{v}$.
(c) Deduce that if $A$ is invertible, the eigenvalues of $A^{-1}$ are the reciprocals of those of $A$.

**24.** (a) Prove that $A$ and $A^{\mathsf{T}}$ have the same characteristic polynomial, hence the same
eigenvalues. (b) Illustrate with $A = \begin{pmatrix}2 & 1\\ 0 & 3\end{pmatrix}$: find an eigenvector of
$A$ and an eigenvector of $A^{\mathsf{T}}$ for the same eigenvalue, and check that they are different.

**25.** A matrix $N$ is **nilpotent** if $N^k = 0$ for some $k \ge 1$. Prove that a nilpotent matrix that
is diagonalisable must be the zero matrix. Deduce that $N = \begin{pmatrix}0 & 1\\ 0 & 0\end{pmatrix}$ is
not diagonalisable.

**26.** Let $A \in M_2(\mathbb{R})$ have the non-real eigenvalues $a \pm bi$ with $b \neq 0$, and let
$\mathbf{v} = \mathbf{u} + i\mathbf{w}$ be an eigenvector for $a + bi$ with $\mathbf{u},\mathbf{w} \in \mathbb{R}^2$.

(a) Prove that $\mathbf{u}$ and $\mathbf{w}$ are linearly independent.
(b) Prove that $A\mathbf{u} = a\mathbf{u} - b\mathbf{w}$ and $A\mathbf{w} = b\mathbf{u} + a\mathbf{w}$.
(c) Deduce that in the basis $(\mathbf{u},\mathbf{w})$ the matrix of $A$ is
$\begin{pmatrix}a & b\\ -b & a\end{pmatrix}$, a rotation–scaling (rotation by $-\theta$ composed with
scaling by $r = \sqrt{a^2+b^2}$).

**27.** Let $A \in M_n(\mathbb{C})$ and suppose $\mu \in \mathbb{C}$ is an eigenvalue of $A^2$. Prove that
$\mu = \lambda^2$ for some eigenvalue $\lambda$ of $A$. (Hint: factor $A^2 - \mu I$ over $\mathbb{C}$ and
use $\det(XY) = \det X\det Y$.)

**28.** Prove that if $A$ is invertible and diagonalisable, then $A^{-1}$ is diagonalisable with
eigenvalues $1/\lambda$ for $\lambda \in \sigma(A)$.

**29.** (a) Prove $g_\lambda = n - \operatorname{rank}(A - \lambda I)$.
(b) Prove that $A$ is diagonalisable if and only if $\operatorname{rank}(A - \lambda I) = n - a_\lambda$
for every eigenvalue $\lambda$ (assume $p_A$ splits).

**30.** (a) Prove that similar matrices have the same rank and are diagonalisable simultaneously.
(b) Give two matrices with the same eigenvalues but different eigenvectors, and explain why this does not
contradict (a).

**31.** Prove by induction on $n$ that every real symmetric $n \times n$ matrix is orthogonally
diagonalisable: it has a real eigenvalue $\lambda_1$ with unit eigenvector $\mathbf{u}_1$; the orthogonal
complement $\mathbf{u}_1^{\perp}$ is invariant under $A$; apply induction there. State clearly where the
symmetry is used.

## Challenge

**32.** *(challenge)* Prove **Sylvester's determinant identity**
$\det(I_m + AB) = \det(I_n + BA)$ for $A \in M_{m\times n}$, $B \in M_{n\times m}$, by considering the
block matrices $\begin{pmatrix}I_m & -A\\ B & I_n\end{pmatrix}$ and computing its determinant in two
ways. Deduce that $p_{AB} = p_{BA}$ for square matrices $A,B$ of the same size.

**33.** *(challenge)* Let $P = \begin{pmatrix}1-a & b\\ a & 1-b\end{pmatrix}$ with $0 < a,b < 1$ be a
column-stochastic matrix.

(a) Prove that $1$ is an eigenvalue and that the other eigenvalue is $1 - a - b$, with
$|1-a-b| < 1$.
(b) Find the stationary distribution and prove that both its entries are positive.
(c) Prove that $P^n\mathbf{x}_0 \to \boldsymbol{\pi}$ for every starting vector $\mathbf{x}_0$ with
entries summing to $1$.

**34.** *(challenge)* Let $A \in M_n(\mathbb{C})$ have $n$ distinct eigenvalues and let $B$ be a matrix
with $AB = BA$. Prove that $B = f(A)$ for some polynomial $f$ of degree at most $n-1$. (Hint: on each
eigenspace of $A$, $B$ acts as a scalar; use the Lagrange interpolation polynomial.)

**35.** *(challenge)* Let $\varphi = (1+\sqrt5)/2$ and $\psi = (1-\sqrt5)/2$, so that
$F_n = (\varphi^n - \psi^n)/\sqrt5$ is the $n$-th Fibonacci number.

(a) Prove $\lvert\psi\rvert < 1$ and $\lvert\psi\rvert^n/\sqrt5 < \tfrac12$ for every $n \ge 1$.
(b) Deduce that $F_n$ is the integer nearest to $\varphi^n/\sqrt5$.
(c) Compute the nearest integer to $\varphi^{20}/\sqrt5$ and check that it is $F_{20} = 6765$.
