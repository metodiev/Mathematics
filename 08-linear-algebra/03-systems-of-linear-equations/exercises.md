# Systems of Linear Equations — Exercises

> [Tutorial](README.md) · [Solutions](solutions.md) · Level: Intermediate

Thirty-five problems, numbered continuously. The levels are cumulative, not independent: a Beginner
problem may be needed inside an Advanced one.

**How to use this set.**

* Attempt each problem on paper before opening [solutions.md](solutions.md). Reading a solution feels
  like learning and is not.
* For every system you solve, **check the answer in the original equations**. Checking is part of the
  problem, not an optional extra.
* An infinite solution set is only described completely when it is written as a parametrised family,
  e.g. $\{(2 - t,\ 1,\ t) : t \in \mathbb{R}\}$, together with the statement that *every* solution has
  that form.
* Problems that ask for a proof need complete sentences, every theorem named, and both inclusions
  whenever a set equality is claimed.
* Unless stated otherwise, all variables range over $\mathbb{R}$ and all matrices are real.

## Beginner

**1.** Write the coefficient matrix and the augmented matrix of

$$
\begin{cases}
2x - y + 3z = 4\\
x + 5y = -2\\
-3x + 2y - z = 0 .
\end{cases}
$$

**2.** The augmented matrix

$$
\left(\begin{array}{ccc|c}
1 & 0 & 2 & 4\\
0 & 1 & -1 & 1
\end{array}\right)
$$

is in reduced row echelon form. Write out the system it represents and its full solution set.

**3.** Solve by Gauss–Jordan elimination:

$$
\begin{cases}
3x + y = 7\\
x - y = 1 .
\end{cases}
$$

**4.** Solve, clearing denominators first:

$$
\begin{cases}
\tfrac12 x + \tfrac13 y = 2\\[2pt]
\tfrac14 x - \tfrac12 y = -1 .
\end{cases}
$$

**5.** Decide whether the system is consistent, and justify the answer with ranks:

$$
\begin{cases}
x + 2y = 3\\
2x + 4y = 7 .
\end{cases}
$$

**6.** Solve by elimination and back substitution:

$$
\begin{cases}
x + y + z = 2\\
2x - y + z = 7\\
x + 2y - z = -6 .
\end{cases}
$$

**7.** Solve, and give the solution set in parametric form:

$$
\begin{cases}
x + y + z = 5\\
x - y + 2z = 4 .
\end{cases}
$$

**8.** For each matrix decide whether it is in row echelon form, and whether it is in reduced row
echelon form:

$$
\text{(i)}\ \begin{pmatrix}1 & 2 & 0\\ 0 & 0 & 1\\ 0 & 0 & 0\end{pmatrix},
\quad
\text{(ii)}\ \begin{pmatrix}1 & 0 & 3\\ 0 & 1 & 2\\ 0 & 0 & 4\end{pmatrix},
\quad
\text{(iii)}\ \begin{pmatrix}0 & 1 & 2\\ 1 & 0 & 3\end{pmatrix},
\quad
\text{(iv)}\ \begin{pmatrix}1 & 2 & 3\\ 0 & 0 & 0\\ 0 & 1 & 0\end{pmatrix}.
$$

**9.** Compute the rank of

$$
A = \begin{pmatrix}
1 & 2 & 3 & 4\\
2 & 4 & 6 & 8\\
0 & 1 & 1 & 1\\
1 & 3 & 4 & 5
\end{pmatrix}.
$$

**10.** Solve the homogeneous system and describe the solution set:

$$
\begin{cases}
x + 2y - z = 0\\
2x + y + z = 0 .
\end{cases}
$$

**11.** With $A = \begin{pmatrix}1 & 2 & -1\\ 0 & 1 & 1\end{pmatrix}$ and
$\mathbf{b} = (2, 5)^{\mathsf{T}}$, decide whether $(1, 2, 3)$ is a solution of $A\mathbf{x} = \mathbf{b}$.

**12.** Give an example of a system of **three** equations in **two** unknowns whose solution set is
(a) infinite, and (b) empty. In each case say what the three lines look like.

**13.** Two numbers have sum $30$, and twice the first minus the second equals $6$. Find them by setting
up and solving a linear system.

## Intermediate

**14.** Solve the $4 \times 4$ system

$$
\begin{cases}
x_1 + x_2 + x_3 + x_4 = 10\\
x_1 - x_2 + x_3 - x_4 = 0\\
x_1 + x_2 - x_3 - x_4 = 4\\
x_1 - x_2 - x_3 + x_4 = 2 .
\end{cases}
$$

**15.** Find the general solution of

$$
\begin{cases}
x_1 + x_2 + x_3 + x_4 = 6\\
x_1 + 2x_2 + 3x_3 + 4x_4 = 10\\
2x_1 + 3x_2 + 4x_3 + 5x_4 = 16 .
\end{cases}
$$

**16.** For which values of $k$ does

$$
\begin{cases}
x + ky = 1\\
kx + y = 1
\end{cases}
$$

have no solution? exactly one solution? infinitely many? Give the solution in each consistent case.

**17.** Using only rank computations, decide whether

$$
\begin{pmatrix}1 & 2\\ 2 & 4\\ 3 & 6\end{pmatrix}\mathbf{x} = \begin{pmatrix}1\\ 2\\ 4\end{pmatrix}
$$

is consistent.

**18.** Solve the homogeneous system

$$
\begin{cases}
x - y + 2z = 0\\
2x + y - z = 0
\end{cases}
$$

and write the solution set as $\{t\mathbf{v} : t \in \mathbb{R}\}$ for an explicit vector $\mathbf{v}$.

**19.** Prove that if $\mathbf{x}$ and $\mathbf{y}$ both satisfy $A\mathbf{x} = \mathbf{0}$, then
$a\mathbf{x} + b\mathbf{y}$ satisfies $A\mathbf{x} = \mathbf{0}$ for all $a, b \in \mathbb{R}$.

**20.** Find an LU factorisation of

$$
A = \begin{pmatrix}1 & 2 & 3\\ 2 & 5 & 8\\ 3 & 7 & 14\end{pmatrix},
$$

verify it by multiplying $LU$, and use it to solve $A\mathbf{x} = (6, 15, 24)^{\mathsf{T}}$ and
$A\mathbf{x} = (3, 8, 14)^{\mathsf{T}}$.

**21.** Compute $A^{-1}$ by row-reducing $[A \mid I]$ for

$$
A = \begin{pmatrix}2 & 1 & 1\\ 1 & 3 & 2\\ 1 & 0 & 0\end{pmatrix},
$$

and use the result to solve $A\mathbf{x} = (1, 1, 1)^{\mathsf{T}}$.

**22.** Balance the reaction $\mathrm{Fe_2O_3} + \mathrm{CO} \to \mathrm{Fe} + \mathrm{CO_2}$ by solving a
homogeneous linear system, and explain why the solution is unique up to scale.

**23.** Water flows through three pipes of a network: $x_1$ from $A$ to $B$, $x_2$ from $B$ to $C$, and
$x_3$ from $A$ to $C$. Node $A$ has an inflow of $30$, node $B$ discharges $10$, and node $C$
discharges $20$. Write the conservation equations, find the general solution, and state the range of the
free parameter for which all flows are non-negative.

**24.** Find the quadratic $p(x) = a + bx + cx^2$ with $p(-1) = 0$, $p(1) = 4$ and $p(2) = 3$. Set up
the linear system, solve it, and verify all three conditions.

## Advanced

**25.** Prove Theorem 7.1 in full: each of the three elementary row operations preserves the solution
set of a linear system, with both inclusions written out.

**26.** Prove that a linear system with at least two distinct solutions has infinitely many. Your proof
must not use the rank criterion.

**27.** Let $S = \{\mathbf{x} : A\mathbf{x} = \mathbf{b}\}$ be non-empty with $\mathbf{x}_p \in S$. Prove
$S = \mathbf{x}_p + \operatorname{null}A$ (both inclusions) and deduce that if $S$ is finite then
$S = \{\mathbf{x}_p\}$.

**28.** Let $A$ be $n \times n$ and suppose row reduction of $A$ produces $I_n$. Prove carefully that $A$
is invertible and that the same sequence of row operations, applied to $[A \mid I]$, produces
$[I \mid A^{-1}]$.

**29.** Prove that $\operatorname{rank}A = \operatorname{rank}A^{\mathsf{T}}$ for every $m \times n$
matrix $A$. (This is the statement that row rank equals column rank.)

**30.** Prove that if the system $A\mathbf{x} = \mathbf{b}$ is inconsistent, then
$\operatorname{rank}[A \mid \mathbf{b}] = \operatorname{rank}A + 1$.

**31.** Let $A$ be invertible and suppose $A = L_1U_1 = L_2U_2$ with each $L_i$ unit lower triangular and
each $U_i$ upper triangular. Prove $L_1 = L_2$ and $U_1 = U_2$.

## Challenge

**32.** Find **all** $3 \times 3$ matrices whose null space is exactly
$\operatorname{span}\{(1,1,0),\, (0,1,1)\}$, and prove that your list is complete.

**33.** Let $A$ be $n \times n$. Prove that the following are equivalent:

* (i) $A\mathbf{x} = \mathbf{b}$ has a unique solution for at least one $\mathbf{b}$;
* (ii) $A\mathbf{x} = \mathbf{0}$ has only the solution $\mathbf{x} = \mathbf{0}$;
* (iii) $A\mathbf{x} = \mathbf{b}$ has a solution for every $\mathbf{b}$.

**34.** Gaussian elimination with **partial pivoting** swaps into the current position a row whose entry
in the current column has the largest absolute value among the candidate rows. Prove that if $A$ is
invertible, then at every stage the chosen pivot is nonzero, so the algorithm never divides by zero.

**35.** Prove that the solution set of a linear system over $\mathbb{R}$ is either empty, a single
point, or uncountable. Deduce that a linear system can never have *exactly* countably many solutions.
