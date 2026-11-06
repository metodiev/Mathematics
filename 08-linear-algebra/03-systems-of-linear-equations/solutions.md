# Systems of Linear Equations — Solutions

> [Tutorial](README.md) · [Exercises](exercises.md)

Every exercise is solved in full: the strategy is stated first, then the algebra, then a check. Proofs
are written out completely, with both inclusions where a set equality is claimed.

## Beginner

**1.** *Answer:*

$$
A = \begin{pmatrix}2 & -1 & 3\\ 1 & 5 & 0\\ -3 & 2 & -1\end{pmatrix},
\qquad
[A \mid \mathbf{b}] = \left(\begin{array}{ccc|c}
2 & -1 & 3 & 4\\
1 & 5 & 0 & -2\\
-3 & 2 & -1 & 0
\end{array}\right).
$$

The coefficient matrix collects only the three unknowns' coefficients; the augmented matrix appends the
right-hand sides as a fourth column. The second equation is $x + 5y + 0z = -2$: the missing $z$ becomes
a $0$, not a blank. Missing entries are the most common source of error at this stage.

**2.** *Answer: $S = \{(4 - 2t,\ 1 + t,\ t) : t \in \mathbb{R}\}$.*

The matrix has two rows, three coefficient columns and no bar entry, so it encodes two equations in
three unknowns:

$$
\begin{cases}
x + 2z = 4\\
y - z = 1 .
\end{cases}
$$

Column $3$ has no pivot, so $z$ is free. Set $z = t$; the equations give $x = 4 - 2t$ and $y = 1 + t$
directly, because the matrix is in RREF (no back substitution needed). *Check* with $t = 1$:
$(2, 2, 1)$ gives $2 + 2 = 4$ and $2 - 1 = 1$. ✓ Here $r = 2$ and $n = 3$, so exactly one free
parameter, as Theorem 7.3 predicts.

**3.** *Answer: $(2, 1)$.*

Strategy: put the pivot first to avoid fractions.

$$
\left(\begin{array}{cc|c}3 & 1 & 7\\ 1 & -1 & 1\end{array}\right)
\xrightarrow{R_1 \leftrightarrow R_2}
\left(\begin{array}{cc|c}1 & -1 & 1\\ 3 & 1 & 7\end{array}\right)
\xrightarrow{R_2 \leftarrow R_2 - 3R_1}
\left(\begin{array}{cc|c}1 & -1 & 1\\ 0 & 4 & 4\end{array}\right)
$$

$$
\xrightarrow{R_2 \leftarrow \frac14R_2}
\left(\begin{array}{cc|c}1 & -1 & 1\\ 0 & 1 & 1\end{array}\right)
\xrightarrow{R_1 \leftarrow R_1 + R_2}
\left(\begin{array}{cc|c}1 & 0 & 2\\ 0 & 1 & 1\end{array}\right).
$$

*Check:* $3(2) + 1 = 7$ and $2 - 1 = 1$. ✓ Both pivots are $1$ and each is alone in its column, so the
final matrix is the RREF and the solution is read off.

**4.** *Answer: $(2, 3)$.*

Clear denominators: multiply the first equation by $6$ and the second by $4$.

$$
\begin{cases}
3x + 2y = 12\\
x - 2y = -4 .
\end{cases}
$$

Adding eliminates $y$: $4x = 8$, so $x = 2$. Substituting into $3x + 2y = 12$ gives $6 + 2y = 12$, so
$y = 3$. *Check in the original fractional form:* $\tfrac12(2) + \tfrac13(3) = 1 + 1 = 2$ and
$\tfrac14(2) - \tfrac12(3) = \tfrac12 - \tfrac32 = -1$. ✓ Multiplying an equation by a nonzero constant is
operation (R2), so by Theorem 7.1 the cleared system has the same solution set.

**5.** *Answer: inconsistent.*

The augmented matrix is $\left(\begin{array}{cc|c}1 & 2 & 3\\ 2 & 4 & 7\end{array}\right)$.
$R_2 \leftarrow R_2 - 2R_1$ gives $\left(\begin{array}{cc|c}1 & 2 & 3\\ 0 & 0 & 1\end{array}\right)$.

The pivots are in column $1$ and in the right-hand column, so $\operatorname{rank}A = 1$ while
$\operatorname{rank}[A \mid \mathbf{b}] = 2$. Since $2 \neq 1$, Theorem 7.3 says the system has no
solution: the last row reads $0 = 1$. Geometrically the two lines have the same slope
($y = -\tfrac12x + \tfrac32$ and $y = -\tfrac12x + \tfrac74$) and are parallel and distinct.

**6.** *Answer: $(1, -2, 3)$.*

$$
\left(\begin{array}{ccc|c}1 & 1 & 1 & 2\\ 2 & -1 & 1 & 7\\ 1 & 2 & -1 & -6\end{array}\right)
\xrightarrow{\substack{R_2 \leftarrow R_2 - 2R_1\\ R_3 \leftarrow R_3 - R_1}}
\left(\begin{array}{ccc|c}1 & 1 & 1 & 2\\ 0 & -3 & -1 & 3\\ 0 & 1 & -2 & -8\end{array}\right)
$$

Swapping rows $2$ and $3$ puts the pivot $1$ in place; then $R_3 \leftarrow R_3 + 3R_2$ gives
$(0, 0, -7 \mid -21)$, so $z = 3$. Back substitution: $y - 2z = -8$ gives $y = -2$; $x + y + z = 2$ gives
$x = 1$. *Check:* $1 - 2 + 3 = 2$, $2 + 2 + 3 = 7$, $1 - 4 - 3 = -6$. ✓ Three pivots, three unknowns:
unique.

**7.** *Answer: $S = \{(6 - 3t,\ t,\ 2t - 1) : t \in \mathbb{R}\}$.*

Two equations in three unknowns, so at most two pivots and at least one free unknown. Eliminating $x$:
$R_2 \leftarrow R_2 - R_1$ gives $(0, -2, 1 \mid -1)$, that is $2y - z = 1$, so $z = 2y - 1$. Then the
first equation gives $x = 5 - y - z = 5 - y - (2y - 1) = 6 - 3y$. Writing $y = t$:

$$
(x, y, z) = (6, 0, -1) + t(-3, 1, 2).
$$

*Check* in the second equation: $(6 - 3t) - t + 2(2t - 1) = 6 - 4t + 4t - 2 = 4$. ✓ The parameter $t$ is
free, so the solution set is a line in $\mathbb{R}^3$.

**8.** *Answer:* (i) both REF and RREF; (ii) REF but not RREF; (iii) neither; (iv) neither.

* (i) Zero row at the bottom; leading entries are in column $1$ (row 1) and column $3$ (row 2), strictly
  rightward; all pivots equal $1$; column $1$ has a $0$ below its pivot and column $3$ has a $0$ above
  and below its pivot. So the matrix is in RREF, hence also in REF.
* (ii) The staircase condition holds, so it is in REF. It is not in RREF: the pivot $4$ in row $3$ is not
  $1$, and its column contains the nonzero entries $3$ and $2$ above it.
* (iii) Row $1$'s leading entry is in column $2$, which is to the *right* of row $2$'s leading entry in
  column $1$. The staircase fails, so it is not in REF (and therefore not in RREF).
* (iv) The zero row lies above a nonzero row, violating the first requirement. It is not in REF.

**9.** *Answer: $\operatorname{rank}A = 2$.*

$R_2 \leftarrow R_2 - 2R_1$ gives a zero row, since $(2,4,6,8) = 2(1,2,3,4)$. Also
$R_4 \leftarrow R_4 - R_1$ gives $(0,1,1,1)$, which equals row $3$; hence $R_4 \leftarrow R_4 - R_3$ gives
another zero row. The remaining rows are $(1,2,3,4)$ and $(0,1,1,1)$, whose leading entries are in
columns $1$ and $2$, so there are two pivots and the rank is $2$. The four rows span only a
two-dimensional space: two of the four equations were redundant.

**10.** *Answer: $S = \{t(-1, 1, 1) : t \in \mathbb{R}\}$.*

$R_2 \leftarrow R_2 - 2R_1$ gives $(0, -3, 3)$, and scaling by $-\tfrac13$ gives $(0, 1, -1)$; then
$R_1 \leftarrow R_1 - 2R_2$ gives $(1, 0, 1)$. So $x = -z$ and $y = z$, and with $z = t$ the solution
set is $\{(-t, t, t)\}$. *Check:* $-t + 2t - t = 0$ and $-2t + t + t = 0$. ✓ A homogeneous system with
$r = 2 < n = 3$ has a non-trivial solution, and the solution set is a line through the origin.

**11.** *Answer: yes, $(1,2,3)$ is a solution.*

$$
A\mathbf{x} = \begin{pmatrix}1 & 2 & -1\\ 0 & 1 & 1\end{pmatrix}\begin{pmatrix}1\\ 2\\ 3\end{pmatrix}
= \begin{pmatrix}1\cdot1 + 2\cdot2 + (-1)\cdot3\\ 0\cdot1 + 1\cdot2 + 1\cdot3\end{pmatrix}
= \begin{pmatrix}2\\ 5\end{pmatrix} = \mathbf{b}. \ \checkmark
$$

Note that a solution of a $2 \times 3$ system has three coordinates; the size of $\mathbf{x}$ is the
number of *columns* of $A$, not the number of rows.

**12.** *Answer:*

(a) *Infinite:* take three copies of the same line,

$$
x + y = 2, \qquad 2x + 2y = 4, \qquad -x - y = -2 .
$$

All three equations are equivalent to $x + y = 2$, so all three lines coincide and
$S = \{(2 - t, t) : t \in \mathbb{R}\}$. The rank is $1$ and $n = 2$.

(b) *Empty:*

$$
x + y = 2, \qquad 2x + 2y = 4, \qquad x + y = 3 .
$$

The first two lines coincide; the third is parallel and distinct. Row-reducing gives the row
$(0,0 \mid 1)$, so $\operatorname{rank}A = 1$ and $\operatorname{rank}[A \mid \mathbf{b}] = 2$.

In both cases more equations than unknowns does *not* force uniqueness or inconsistency; what matters is
how many independent conditions there are.

**13.** *Answer: $12$ and $18$.*

Let the numbers be $x$ and $y$. The data give

$$
\begin{cases}
x + y = 30\\
2x - y = 6 .
\end{cases}
$$

Adding: $3x = 36$, so $x = 12$, and then $y = 30 - 12 = 18$. *Check:* $12 + 18 = 30$ and
$2(12) - 18 = 6$. ✓ Both equations are independent ($\operatorname{rank} = 2 = n$), so the answer is
unique.

## Intermediate

**14.** *Answer: $(4, 3, 1, 2)$.*

$$
\left(\begin{array}{cccc|c}
1 & 1 & 1 & 1 & 10\\
1 & -1 & 1 & -1 & 0\\
1 & 1 & -1 & -1 & 4\\
1 & -1 & -1 & 1 & 2
\end{array}\right)
\xrightarrow{R_i \leftarrow R_i - R_1\ (i = 2,3,4)}
\left(\begin{array}{cccc|c}
1 & 1 & 1 & 1 & 10\\
0 & -2 & 0 & -2 & -10\\
0 & 0 & -2 & -2 & -6\\
0 & -2 & -2 & 0 & -8
\end{array}\right)
$$

Now $R_4 \leftarrow R_4 - R_2$ gives $(0, 0, -2, 2 \mid 2)$, and $R_4 \leftarrow R_4 - R_3$ gives
$(0, 0, 0, 4 \mid 8)$, so $x_4 = 2$. Back substitution: $-2x_3 - 4 = -6$ gives $x_3 = 1$;
$-2x_2 - 4 = -10$ gives $x_2 = 3$; $x_1 + 3 + 1 + 2 = 10$ gives $x_1 = 4$.

*Check:* $4+3+1+2 = 10$; $4-3+1-2 = 0$; $4+3-1-2 = 4$; $4-3-1+2 = 2$. ✓

*Second approach.* Adding and subtracting the equations in symmetric pairs gives $x_1 + x_2 = 7$,
$x_3 + x_4 = 3$, $x_1 - x_2 = 1$, $x_3 - x_4 = -1$, whence the same answer with no elimination. The
symmetry of the coefficient matrix is what makes this work.

**15.** *Answer: $S = \{(2 + s + 2t,\ 4 - 2s - 3t,\ s,\ t) : s, t \in \mathbb{R}\}$.*

Rows: $(1,1,1,1 \mid 6)$, $(1,2,3,4 \mid 10)$, $(2,3,4,5 \mid 16)$. Note that row $3$ = row $1$ + row $2$
in the coefficient part, and $16 = 6 + 10$, so the third equation is exactly the sum of the first two and
adds nothing. Eliminate: $R_2 \leftarrow R_2 - R_1$ gives $(0,1,2,3 \mid 4)$;
$R_3 \leftarrow R_3 - 2R_1$ gives the same row, hence a zero row after $R_3 \leftarrow R_3 - R_2$. Then
$R_1 \leftarrow R_1 - R_2$ gives $(1, 0, -1, -2 \mid 2)$.

The RREF has pivots in columns $1$ and $2$, so $r = 2$ and there are $4 - 2 = 2$ free unknowns, $x_3 = s$
and $x_4 = t$. Then $x_1 = 2 + s + 2t$ and $x_2 = 4 - 2s - 3t$.

*Check* with $s = 1$, $t = 0$: $(3, 2, 1, 0)$ gives $3 + 2 + 1 = 6$; $3 + 4 + 3 = 10$;
$6 + 6 + 4 = 16$. ✓ The redundancy of the third equation was visible in advance as row $3$ = row $1$ +
row $2$; recognising it saves work but is not necessary.

**16.** *Answer:* unique for $k \notin \{-1, 1\}$, none for $k = -1$, infinitely many for $k = 1$.

Eliminate $x$: $R_2 \leftarrow R_2 - kR_1$ gives

$$
(1 - k^2)y = 1 - k, \qquad \text{that is} \qquad (1 - k)(1 + k)y = 1 - k .
$$

* If $k \neq 1$ we may divide by $1 - k$, leaving $(1 + k)y = 1$.
  * If also $k \neq -1$, then $y = \dfrac{1}{1+k}$ and $x = 1 - ky = 1 - \dfrac{k}{1+k} = \dfrac{1}{1+k}$.
    The unique solution is $\big(\tfrac{1}{1+k}, \tfrac{1}{1+k}\big)$.
  * If $k = -1$, the equation reads $0 \cdot y = 2$, which has no solution.
* If $k = 1$, both equations are $x + y = 1$ and $S = \{(1 - t,\ t)\}$.

*Check the three regimes:* $k = 0$ gives $(1,1)$, and indeed $x = 1$, $y = 1$. For $k = 1$,
$(1 - t) + t = 1$ in both equations. For $k = -1$ the equations $x - y = 1$ and $-x + y = 1$ are
incompatible. The critical values are exactly those making the determinant $1 - k^2$ vanish.

**17.** *Answer: inconsistent.*

The coefficient matrix has rows $(1,2)$, $(2,4)$, $(3,6)$, all multiples of $(1,2)$; after
$R_2 \leftarrow R_2 - 2R_1$ and $R_3 \leftarrow R_3 - 3R_1$ two zero rows remain, so
$\operatorname{rank}A = 1$.

For the augmented matrix, the same operations give rows $(1, 2 \mid 1)$, $(0,0 \mid 0)$ and
$(0,0 \mid 1)$. The last row is a pivot in the right-hand column, so
$\operatorname{rank}[A \mid \mathbf{b}] = 2$. Since $2 \neq 1 = \operatorname{rank}A$, Theorem 7.3 gives
$S = \varnothing$.

*Sanity check without matrices:* the equations demand $x + 2y = 1$, $x + 2y = 1$ and $x + 2y = \tfrac43$,
which cannot all hold.

**18.** *Answer: $S = \{t(-1, 5, 3) : t \in \mathbb{R}\}$.*

$R_2 \leftarrow R_2 - 2R_1$ gives $(0, 3, -5)$; scale by $\tfrac13$ to get $(0, 1, -\tfrac53)$; then
$R_1 \leftarrow R_1 + R_2$ gives $(1, 0, \tfrac13)$. Hence $x = -\tfrac13z$ and $y = \tfrac53z$. Setting
$z = 3t$ clears the fractions: $(x,y,z) = (-t, 5t, 3t) = t(-1,5,3)$.

*Check:* $(-t) - (5t) + 2(3t) = 0$ and $2(-t) + 5t - 3t = 0$. ✓ Note $r = 2$, $n = 3$, one free
parameter; the solution set is a line through the origin, and $(-1,5,3)$ is one vector spanning it.

**19.** *Proof.* Let $\mathbf{x}, \mathbf{y}$ satisfy $A\mathbf{x} = A\mathbf{y} = \mathbf{0}$ and let
$a, b \in \mathbb{R}$. Matrix–vector multiplication is linear in the vector variable, that is
$A(a\mathbf{x} + b\mathbf{y}) = aA\mathbf{x} + bA\mathbf{y}$ (this is distributivity of the matrix
product over sums, and the fact that scalars commute with matrices). Therefore

$$
A(a\mathbf{x} + b\mathbf{y}) = a\cdot\mathbf{0} + b\cdot\mathbf{0} = \mathbf{0}. \qquad \blacksquare
$$

The same computation shows that the solution set of a homogeneous system is closed under all linear
combinations, which is the concrete prototype of "subspace" in
[Vector Spaces](../04-vector-spaces/README.md).

**20.** *Answer:*

$$
L = \begin{pmatrix}1 & 0 & 0\\ 2 & 1 & 0\\ 3 & 1 & 1\end{pmatrix},
\qquad
U = \begin{pmatrix}1 & 2 & 3\\ 0 & 1 & 2\\ 0 & 0 & 3\end{pmatrix}.
$$

*Construction.* $R_2 \leftarrow R_2 - 2R_1$ (multiplier $2$) gives $(0,1,2)$;
$R_3 \leftarrow R_3 - 3R_1$ (multiplier $3$) gives $(0,1,5)$; then $R_3 \leftarrow R_3 - R_2$
(multiplier $1$) gives $(0,0,3)$. The multipliers, in their positions, form $L$; the echelon matrix is
$U$.

*Verify:* row $2$ of $LU$ is $2(1,2,3) + (0,1,2) = (2,5,8)$ ✓; row $3$ is
$3(1,2,3) + (0,1,2) + (0,0,3) = (3,7,14)$ ✓; row $1$ is $(1,2,3)$ ✓.

*First right-hand side $\mathbf{b}_1 = (6,15,24)$.* Solve $L\mathbf{y} = \mathbf{b}_1$: $y_1 = 6$;
$2(6) + y_2 = 15$ gives $y_2 = 3$; $3(6) + 3 + y_3 = 24$ gives $y_3 = 3$. Solve $U\mathbf{x} = \mathbf{y}$:
$3x_3 = 3$ gives $x_3 = 1$; $x_2 + 2 = 3$ gives $x_2 = 1$; $x_1 + 2 + 3 = 6$ gives $x_1 = 1$. So
$\mathbf{x} = (1,1,1)$; indeed $A(1,1,1) = (6,15,24)$. ✓

*Second right-hand side $\mathbf{b}_2 = (3,8,14)$.* $y_1 = 3$; $6 + y_2 = 8$ gives $y_2 = 2$;
$9 + 2 + y_3 = 14$ gives $y_3 = 3$. Then $3x_3 = 3$ gives $x_3 = 1$; $x_2 + 2 = 2$ gives $x_2 = 0$;
$x_1 + 0 + 3 = 3$ gives $x_1 = 0$. So $\mathbf{x} = (0,0,1)$, which is the third column of $A$ — as it
must be, since $A(0,0,1)$ is that column.

**21.** *Answer:*

$$
A^{-1} = \begin{pmatrix}0 & 0 & 1\\ -2 & 1 & 3\\ 3 & -1 & -5\end{pmatrix},
\qquad
\mathbf{x} = A^{-1}(1,1,1)^{\mathsf{T}} = (1, 2, -3)^{\mathsf{T}}.
$$

*Row reduction of $[A \mid I]$.*

$$
\left(\begin{array}{ccc|ccc}
2 & 1 & 1 & 1 & 0 & 0\\
1 & 3 & 2 & 0 & 1 & 0\\
1 & 0 & 0 & 0 & 0 & 1
\end{array}\right)
\xrightarrow{R_1 \leftrightarrow R_3}
\left(\begin{array}{ccc|ccc}
1 & 0 & 0 & 0 & 0 & 1\\
1 & 3 & 2 & 0 & 1 & 0\\
2 & 1 & 1 & 1 & 0 & 0
\end{array}\right)
$$

$$
\xrightarrow{\substack{R_2 \leftarrow R_2 - R_1\\ R_3 \leftarrow R_3 - 2R_1}}
\left(\begin{array}{ccc|ccc}
1 & 0 & 0 & 0 & 0 & 1\\
0 & 3 & 2 & 0 & 1 & -1\\
0 & 1 & 1 & 1 & 0 & -2
\end{array}\right)
\xrightarrow{R_2 \leftrightarrow R_3}
\left(\begin{array}{ccc|ccc}
1 & 0 & 0 & 0 & 0 & 1\\
0 & 1 & 1 & 1 & 0 & -2\\
0 & 3 & 2 & 0 & 1 & -1
\end{array}\right)
$$

$$
\xrightarrow{R_3 \leftarrow R_3 - 3R_2}
\left(\begin{array}{ccc|ccc}
1 & 0 & 0 & 0 & 0 & 1\\
0 & 1 & 1 & 1 & 0 & -2\\
0 & 0 & -1 & -3 & 1 & 5
\end{array}\right)
\xrightarrow{R_3 \leftarrow -R_3}
\left(\begin{array}{ccc|ccc}
1 & 0 & 0 & 0 & 0 & 1\\
0 & 1 & 1 & 1 & 0 & -2\\
0 & 0 & 1 & 3 & -1 & -5
\end{array}\right)
$$

and finally $R_2 \leftarrow R_2 - R_3$ gives $(0,1,0 \mid -2, 1, 3)$. Reading the right block:
$A^{-1}$ as displayed.

*Verify:* $AA^{-1}$ has $(1,1)$-entry $2\cdot0 + 1\cdot(-2) + 1\cdot3 = 1$;
$(2,2)$-entry $1\cdot0 + 3\cdot1 + 2\cdot(-1) = 1$; $(3,1)$-entry $1\cdot0 + 0 + 0 = 0$;
$(1,3)$-entry $2\cdot1 + 1\cdot3 + 1\cdot(-5) = 0$. ✓

*Solve.* $\mathbf{x} = A^{-1}(1,1,1)^{\mathsf{T}} = (0 + 0 + 1,\ -2 + 1 + 3,\ 3 - 1 - 5) = (1,2,-3)$.
*Check:* $A(1,2,-3) = (2 + 2 - 3,\ 1 + 6 - 6,\ 1 + 0 + 0) = (1,1,1)$. ✓

**22.** *Answer:* $\mathrm{Fe_2O_3} + 3\,\mathrm{CO} \to 2\,\mathrm{Fe} + 3\,\mathrm{CO_2}$, that is
$(a,b,c,d) = (1,3,2,3)$.

Let the coefficients be $a, b, c, d$ in the order written. Conservation of each element gives one
equation:

$$
\text{Fe}: \ 2a = c, \qquad \text{O}: \ 3a + b = 2d, \qquad \text{C}: \ b = d .
$$

This is a homogeneous system in four unknowns. Solving: $c = 2a$ and $b = d$; substituting into the
oxygen equation gives $3a + d = 2d$, so $d = 3a$ and therefore $b = 3a$. With $a = 1$:
$(a,b,c,d) = (1,3,2,3)$, and indeed $\mathrm{Fe_2O_3} + 3\mathrm{CO} \to 2\mathrm{Fe} + 3\mathrm{CO_2}$
balances ($2$ Fe, $6$ O, $3$ C on both sides).

*Why unique up to scale.* The coefficient matrix of the system has rank $3$ (three independent element
conditions) and $4$ unknowns, so $n - r = 1$: the solution set is a line through the origin,
$\{t(1,3,2,3) : t \in \mathbb{R}\}$. Every positive solution is a positive multiple of $(1,3,2,3)$, so
there is exactly one with smallest positive integers.

**23.** *Answer:* $x_1 = 30 - t$, $x_2 = 20 - t$, $x_3 = t$ with $0 \le t \le 20$.

Conservation at each node (inflow $=$ outflow):

$$
\begin{cases}
x_1 + x_3 = 30 & \text{(node } A\text{)}\\
x_1 = x_2 + 10 & \text{(node } B\text{)}\\
x_2 + x_3 = 20 & \text{(node } C\text{).}
\end{cases}
$$

Row-reducing $\left(\begin{array}{ccc|c}1&0&1&30\\ 1&-1&0&10\\ 0&1&1&20\end{array}\right)$:
$R_2 \leftarrow R_2 - R_1$ gives $(0,-1,-1 \mid -20)$, i.e. $(0,1,1 \mid 20)$ after scaling by $-1$. Then
$R_3 \leftarrow R_3 - R_2$ gives a zero row. The pivots are in columns $1$ and $2$, so $r = 2$ and there
is $3 - 2 = 1$ free parameter. Taking $x_3 = t$: $x_2 = 20 - t$ and $x_1 = 30 - t$.

*Check at node $B$:* $x_1 - x_2 = (30 - t) - (20 - t) = 10$. ✓ The third equation is redundant because
the three conservation equations sum to $0 = 0$: each pipe contributes once as an inflow and once as an
outflow.

*Non-negativity.* Require $t \ge 0$, $20 - t \ge 0$ and $30 - t \ge 0$; the tightest is $t \le 20$. So
the physically admissible flows are exactly $0 \le t \le 20$, with $t = 0$ sending everything through
$A \to B \to C$ and $t = 20$ sending $20$ directly on $A \to C$.

**24.** *Answer: $p(x) = 3 + 2x - x^2$.*

Substituting the three points into $p(x) = a + bx + cx^2$:

$$
p(-1) = a - b + c = 0, \qquad p(1) = a + b + c = 4, \qquad p(2) = a + 2b + 4c = 3 .
$$

Adding the first two gives $2a + 2c = 4$, i.e. $a + c = 2$. Subtracting the first from the second gives
$2b = 4$, so $b = 2$. Subtracting the first from the third gives $3b + 3c = 3$, so $b + c = 1$ and
$c = -1$; then $a = 2 - c = 3$.

*Check:* $p(-1) = 3 - 2 - 1 = 0$ ✓; $p(1) = 3 + 2 - 1 = 4$ ✓; $p(2) = 3 + 4 - 4 = 3$ ✓.

The coefficient matrix $\begin{pmatrix}1&-1&1\\ 1&1&1\\ 1&2&4\end{pmatrix}$ is a Vandermonde matrix; the
three nodes $-1, 1, 2$ are distinct, which is exactly the condition making the interpolating polynomial
unique.

## Advanced

**25.** *Proof.* Write $\mathbf{a}_i$ for row $i$ of $A$, so that the system is
$\mathbf{a}_i \cdot \mathbf{x} = b_i$ for all $i$. Let $S$ and $S'$ be the solution sets before and after
one operation; we prove $S \subseteq S'$ and $S' \subseteq S$ in each of the three cases.

*(R1) Exchange of rows $i$ and $j$.* The new system contains exactly the same equations, listed in a
different order. A tuple satisfies a list of equations precisely when it satisfies every member of the
list, and membership of a list does not depend on the order. Hence $S = S'$ directly.

*(R2) $R_i \leftarrow cR_i$ with $c \neq 0$.* The new system is the old system with equation $i$
replaced by $c\,\mathbf{a}_i \cdot \mathbf{x} = cb_i$.

*$S \subseteq S'$:* let $\mathbf{x} \in S$. Then $\mathbf{a}_i\cdot\mathbf{x} = b_i$; multiplying this
equality of real numbers by $c$ gives $c(\mathbf{a}_i \cdot \mathbf{x}) = cb_i$, and by linearity of the
dot product $c(\mathbf{a}_i\cdot\mathbf{x}) = (c\mathbf{a}_i)\cdot\mathbf{x}$. All other equations are
untouched, so $\mathbf{x} \in S'$.

*$S' \subseteq S$:* let $\mathbf{x} \in S'$. Then $(c\mathbf{a}_i)\cdot\mathbf{x} = cb_i$, that is
$c(\mathbf{a}_i\cdot\mathbf{x} - b_i) = 0$. Since $c \neq 0$ and $\mathbb{R}$ has no zero divisors,
$\mathbf{a}_i\cdot\mathbf{x} = b_i$. All other equations hold because they are unchanged, so
$\mathbf{x} \in S$. This is the only place where $c \neq 0$ is used.

*(R3) $R_i \leftarrow R_i + cR_j$ with $i \neq j$.* Only equation $i$ changes, to
$(\mathbf{a}_i + c\mathbf{a}_j)\cdot\mathbf{x} = b_i + cb_j$.

*$S \subseteq S'$:* for $\mathbf{x} \in S$,
$(\mathbf{a}_i + c\mathbf{a}_j)\cdot\mathbf{x} = \mathbf{a}_i\cdot\mathbf{x} + c\,\mathbf{a}_j\cdot\mathbf{x} = b_i + cb_j$.

*$S' \subseteq S$:* for $\mathbf{x} \in S'$, equation $j$ is unchanged, so $\mathbf{a}_j\cdot\mathbf{x} = b_j$;
and equation $i$ of the new system holds. Hence

$$
\mathbf{a}_i \cdot \mathbf{x} = \big[(\mathbf{a}_i + c\mathbf{a}_j)\cdot\mathbf{x}\big] - c\,(\mathbf{a}_j\cdot\mathbf{x})
= (b_i + cb_j) - cb_j = b_i .
$$

So $\mathbf{x}$ satisfies every old equation.

A finite sequence of operations is handled by induction: each single step preserves the solution set, so
the composition does too. $\blacksquare$

**26.** *Proof.* Suppose $\mathbf{u} \neq \mathbf{v}$ both solve $A\mathbf{x} = \mathbf{b}$. For $t \in \mathbb{R}$
define $\mathbf{x}(t) = \mathbf{u} + t(\mathbf{v} - \mathbf{u})$. By linearity,

$$
A\mathbf{x}(t) = A\mathbf{u} + t(A\mathbf{v} - A\mathbf{u}) = \mathbf{b} + t(\mathbf{b} - \mathbf{b}) = \mathbf{b},
$$

so $\mathbf{x}(t) \in S$ for every $t$.

The map $t \mapsto \mathbf{x}(t)$ is injective. Indeed if $\mathbf{x}(t) = \mathbf{x}(s)$ with $t \neq s$,
then $t(\mathbf{v} - \mathbf{u}) = s(\mathbf{v} - \mathbf{u})$, so $(t - s)(\mathbf{v} - \mathbf{u}) = \mathbf{0}$. Since
$t - s \neq 0$ and $\mathbf{v} - \mathbf{u} \neq \mathbf{0}$, this contradicts the fact that a nonzero real
scalar times a nonzero vector is nonzero.

An injective map from $\mathbb{R}$ into $S$ exists, so $S$ is infinite (indeed uncountable). The proof
never mentions rank, pivots, or consistency: it uses only linearity and the absence of zero divisors in
$\mathbb{R}$. $\blacksquare$

**27.** *Proof.* Let $N = \operatorname{null}A$.

*First inclusion.* Let $\mathbf{x} \in S$. Then
$A(\mathbf{x} - \mathbf{x}_p) = A\mathbf{x} - A\mathbf{x}_p = \mathbf{b} - \mathbf{b} = \mathbf{0}$, so
$\mathbf{h} := \mathbf{x} - \mathbf{x}_p \in N$ and $\mathbf{x} = \mathbf{x}_p + \mathbf{h}$.

*Second inclusion.* Let $\mathbf{h} \in N$. Then
$A(\mathbf{x}_p + \mathbf{h}) = A\mathbf{x}_p + A\mathbf{h} = \mathbf{b} + \mathbf{0} = \mathbf{b}$, so
$\mathbf{x}_p + \mathbf{h} \in S$.

Hence $S = \mathbf{x}_p + N$.

*The corollary.* The map $\varphi : N \to S$, $\varphi(\mathbf{h}) = \mathbf{x}_p + \mathbf{h}$, is a
bijection: it is surjective by the equality just proved, and injective because
$\mathbf{x}_p + \mathbf{h}_1 = \mathbf{x}_p + \mathbf{h}_2$ implies $\mathbf{h}_1 = \mathbf{h}_2$ after
subtracting $\mathbf{x}_p$. Therefore $|S| = |N|$.

Now suppose $S$ is finite. Then $N$ is finite. If $\mathbf{h} \in N$ with $\mathbf{h} \neq \mathbf{0}$, the
vectors $t\mathbf{h}$ for $t \in \mathbb{R}$ are pairwise distinct (if $t\mathbf{h} = s\mathbf{h}$ then
$(t - s)\mathbf{h} = \mathbf{0}$, forcing $t = s$) and all lie in $N$, so $N$ would be infinite. Hence
$N = \{\mathbf{0}\}$ and $S = \{\mathbf{x}_p\}$: a finite solution set is necessarily a singleton, which
is the trichotomy of Theorem 7.4 again. $\blacksquare$

**28.** *Proof.* Let $E_1, \dots, E_k$ be the elementary matrices of the row operations, so that
$E_k\cdots E_1A = I_n$; put $E = E_k\cdots E_1$. Each $E_i$ is invertible — its inverse is the elementary
matrix of the inverse operation ($R_i \leftrightarrow R_j$ again, $R_i \leftarrow \tfrac1cR_i$, or
$R_i \leftarrow R_i - cR_j$) — hence $E$ is invertible.

From $EA = I_n$ we get $A = E^{-1}$. Then $AE = E^{-1}E = I_n$ as well, so $E$ is a two-sided inverse of
$A$ and $A$ is invertible with $A^{-1} = E$.

For the algorithm, applying the same operations to the augmented matrix $[A \mid I_n]$ means computing
$E[A \mid I_n] = [EA \mid E]$. By the first part, $EA = I_n$ and $E = A^{-1}$, so the result is
$[I_n \mid A^{-1}]$.

If instead the reduction of $A$ stops with a zero row, then $A$ is not invertible: reduction gives
$EA = R$ with $E$ invertible and $R$ having a zero row, say row $k$. Then $(R\mathbf{x})_k = 0$ for every
$\mathbf{x}$, so $R\mathbf{x} = \mathbf{e}_k$ has no solution, and $R$ is not surjective, hence not
invertible. Since $A = E^{-1}R$ and $E^{-1}$ is invertible, $A$ is not invertible either. $\blacksquare$

**29.** *Proof.* Let $R = EA$ be the RREF of $A$, with $E$ invertible, and let $r$ be the number of
pivots.

*Row rank.* Every row of $R$ is a linear combination of rows of $A$ (row operations replace rows by
combinations of rows), so $\operatorname{Row}(R) \subseteq \operatorname{Row}(A)$. Since $A = E^{-1}R$,
the same argument gives $\operatorname{Row}(A) \subseteq \operatorname{Row}(R)$. Hence
$\operatorname{Row}(A) = \operatorname{Row}(R)$. The nonzero rows of $R$ are linearly independent: each
has its pivot $1$ in a column where every other nonzero row has a $0$, so a combination equal to
$\mathbf{0}$ forces every coefficient to vanish, reading the pivot columns in turn. Therefore
$\dim\operatorname{Row}(A) = $ (number of nonzero rows of $R$) $= r$.

*Column rank.* A linear relation among the columns of a matrix $M$ is exactly a vector
$\mathbf{c}$ with $M\mathbf{c} = \mathbf{0}$, that is, an element of $\operatorname{null}M$. By Lemma
7.2.1, $\operatorname{null}A = \operatorname{null}R$: row operations do not change which column
combinations vanish. Consequently a set of columns of $A$ is linearly independent exactly when the
corresponding set of columns of $R$ is.

In $R$, the pivot columns are linearly independent: the submatrix formed by the pivot rows and pivot
columns is the $r \times r$ identity (a pivot is $1$ and is the only nonzero entry of its column), so a
combination of pivot columns equal to $\mathbf{0}$ forces all coefficients to be $0$ when read off in
the pivot rows. Every other column of $R$ is a combination of the pivot columns, as shown in the proof
of Theorem 7.2. Hence $\dim\operatorname{Col}(R) = r$, and by the previous paragraph
$\dim\operatorname{Col}(A) = r$.

Since $\operatorname{rank}A = \dim\operatorname{Col}(A)$ and
$\operatorname{rank}A^{\mathsf{T}} = \dim\operatorname{Col}(A^{\mathsf{T}}) = \dim\operatorname{Row}(A)$,
both equal $r$. $\blacksquare$

**30.** *Proof.* Let $A$ be $m \times n$. By Theorem 7.3, $A\mathbf{x} = \mathbf{b}$ is inconsistent exactly
when $\operatorname{rank}[A \mid \mathbf{b}] \neq \operatorname{rank}A$. Appending one column can raise the
rank by at most one: the column space of $[A \mid \mathbf{b}]$ is
$\operatorname{Col}(A) + \operatorname{span}\{\mathbf{b}\}$, which is spanned by a spanning set of
$\operatorname{Col}(A)$ together with one extra vector, so its dimension is at most
$\dim\operatorname{Col}(A) + 1$. Hence
$\operatorname{rank}[A \mid \mathbf{b}] \le \operatorname{rank}A + 1$.

Since the rank cannot decrease when a column is added (a spanning set of a subspace spans only that
subspace), $\operatorname{rank}[A \mid \mathbf{b}] \ge \operatorname{rank}A$. If the system is inconsistent
the two ranks differ, so the only possibility is
$\operatorname{rank}[A \mid \mathbf{b}] = \operatorname{rank}A + 1$. $\blacksquare$

**31.** *Proof.* Since $L_1$ and $L_2$ are unit lower triangular, they are invertible: each can be
reduced to $I$ by adding multiples of earlier rows to later ones, so their columns are independent.
Since $A$ is invertible, $U_1$ and $U_2$ must be invertible too: if $U_1\mathbf{x} = \mathbf{0}$ for some
$\mathbf{x} \neq \mathbf{0}$, then $A\mathbf{x} = L_1U_1\mathbf{x} = \mathbf{0}$, contradicting the
invertibility of $A$.

From $L_1U_1 = L_2U_2$ we get $L_2^{-1}L_1 = U_2U_1^{-1}$.

* The left side is a product of unit lower triangular matrices, hence unit lower triangular: the product
  of lower triangular matrices is lower triangular, and the diagonal of a product of unit triangular
  matrices is the product of the diagonals, all $1$.
* The right side is a product of upper triangular matrices, hence upper triangular.

A matrix that is both upper and lower triangular is diagonal. A diagonal matrix that is unit lower
triangular has all diagonal entries $1$, so it is $I$. Therefore $L_2^{-1}L_1 = I$, giving $L_1 = L_2$,
and then $U_1 = U_2$ by multiplying $L_1U_1 = L_1U_2$ on the left by $L_1^{-1}$. $\blacksquare$

## Challenge

**32.** *Answer: exactly the matrices*

$$
A = \begin{pmatrix}\alpha & -\alpha & \alpha\\ \beta & -\beta & \beta\\ \gamma & -\gamma & \gamma\end{pmatrix},
\qquad (\alpha, \beta, \gamma) \neq (0,0,0),
$$

that is, the nonzero $3 \times 3$ matrices all of whose rows are multiples of $(1, -1, 1)$.

*Verification.* Let $\mathbf{x} = (x_1, x_2, x_3)$. For such a matrix,
$A\mathbf{x} = 0$ holds exactly when $\alpha(x_1 - x_2 + x_3) = \beta(x_1 - x_2 + x_3) = \gamma(x_1 - x_2 + x_3) = 0$,
which (some coefficient being nonzero) is equivalent to $x_1 - x_2 + x_3 = 0$. Solving,
$x_2 = x_1 + x_3$, so

$$
\mathbf{x} = (x_1,\ x_1 + x_3,\ x_3) = x_1(1,1,0) + x_3(0,1,1),
$$

and conversely every element of $\operatorname{span}\{(1,1,0), (0,1,1)\}$ has $x_1 - x_2 + x_3 = 0$. Hence
the null space is exactly that span, provided $A \neq 0$.

*Completeness.* Suppose $\operatorname{null}A = \operatorname{span}\{(1,1,0), (0,1,1)\}$, a space of
dimension $2$. Then $\operatorname{rank}A = 3 - 2 = 1$ by Theorem 7.3, so the rows of $A$ span a
one-dimensional space and $A \neq 0$. Every row $\mathbf{r} = (r_1, r_2, r_3)$ of $A$ satisfies
$\mathbf{r}\cdot(1,1,0) = 0$ and $\mathbf{r}\cdot(0,1,1) = 0$, because those two vectors lie in the null
space. These two equations read $r_1 + r_2 = 0$ and $r_2 + r_3 = 0$, so $r_1 = r_3 = -r_2$ and the row is
$r_2(1,-1,1)$. Hence all rows are multiples of $(1,-1,1)$, as claimed, and at least one is nonzero.
$\blacksquare$

**33.** *Proof.* We prove (i) $\Rightarrow$ (ii) $\Rightarrow$ (iii) $\Rightarrow$ (i).

*(i) $\Rightarrow$ (ii).* Suppose $A\mathbf{x} = \mathbf{b}$ has exactly one solution $\mathbf{x}_0$, and
suppose $A\mathbf{h} = \mathbf{0}$. Then $A(\mathbf{x}_0 + \mathbf{h}) = \mathbf{b} + \mathbf{0} = \mathbf{b}$,
so $\mathbf{x}_0 + \mathbf{h}$ is also a solution; uniqueness forces $\mathbf{x}_0 + \mathbf{h} = \mathbf{x}_0$,
hence $\mathbf{h} = \mathbf{0}$. So $A\mathbf{x} = \mathbf{0}$ has only the trivial solution.

*(ii) $\Rightarrow$ (iii).* Let $R = EA$ be the RREF of $A$, with $E$ invertible. If $A\mathbf{x} = \mathbf{0}$
has only $\mathbf{x} = \mathbf{0}$, then $R$ has no free columns: a free column would let us set that
unknown to $1$ and solve for the pivots, producing $\mathbf{x} \neq \mathbf{0}$ with $R\mathbf{x} = \mathbf{0}$
and hence $A\mathbf{x} = E^{-1}R\mathbf{x} = \mathbf{0}$. With $n$ columns and no free column, $R$ has $n$
pivots, one per column, so $R = I_n$ and $\operatorname{rank}A = n$. Then for any $\mathbf{b}$,
$\operatorname{rank}[A \mid \mathbf{b}] \le n = \operatorname{rank}A$, so by Theorem 7.3 the system
$A\mathbf{x} = \mathbf{b}$ is consistent.

*(iii) $\Rightarrow$ (i).* Suppose $A\mathbf{x} = \mathbf{b}$ has a solution for every $\mathbf{b}$, and
suppose for contradiction that $r = \operatorname{rank}A < n$. Then $R = EA$ has a zero row, say row $k$.
Choose $\mathbf{b}$ with $E\mathbf{b} = \mathbf{e}_k$; this is possible because $E$ is invertible. Then
$[R \mid E\mathbf{b}]$ has the row $(0 \;\cdots\; 0 \mid 1)$, so $R\mathbf{x} = E\mathbf{b}$ is inconsistent,
and multiplying by $E^{-1}$ shows $A\mathbf{x} = \mathbf{b}$ is inconsistent — contradicting (iii). Hence
$r = n$, and by Theorem 7.3 the solution is unique for any $\mathbf{b}$, in particular for one.

All three conditions are therefore equivalent to invertibility of $A$. $\blacksquare$

**34.** *Proof.* We show that after $k$ steps of the algorithm (for $0 \le k \le n-1$) the current matrix
$M$ is row-equivalent to $A$, has its first $k$ columns in echelon form with pivots in rows $1, \dots, k$,
and satisfies: *column $k+1$ is not entirely zero in rows $k+1, \dots, n$.*

Row equivalence is clear: every step is an elementary row operation (a swap or a replacement), and both
preserve row equivalence. By induction, the first $k$ columns have pivots in rows $1, \dots, k$ and zeros
below them, so every one of the remaining rows $k+1, \dots, n$ is zero in columns $1, \dots, k$.

Suppose the claim fails: column $k+1$ is zero in all rows $k+1, \dots, n$. Then the submatrix consisting
of rows $k+1, \dots, n$ and columns $k+1, \dots, n$ has a zero first column. Any pivot found later must
therefore lie in a column $\ge k+2$. So $M$ admits at most $k$ pivots in total, and hence
$\operatorname{rank}M \le k$. But rank is invariant under row operations (Theorem 7.2 and §7.5), so
$\operatorname{rank}A = \operatorname{rank}M \le k < n$, contradicting $\operatorname{rank}A = n$, which holds
because $A$ is invertible (Theorem 7.8).

Therefore column $k+1$ has at least one nonzero entry among rows $k+1, \dots, n$, and partial pivoting —
which selects the largest absolute value in that column — selects a nonzero entry. Dividing by it is
therefore legitimate. $\blacksquare$

**35.** *Proof.* Let $S$ be the solution set of a linear system over $\mathbb{R}$.

If $S = \varnothing$ we are done. If $S = \{\mathbf{x}_0\}$ we are done. Otherwise $S$ contains two
distinct points $\mathbf{u} \neq \mathbf{v}$. Define $\varphi : \mathbb{R} \to S$ by
$\varphi(t) = \mathbf{u} + t(\mathbf{v} - \mathbf{u})$. As in Exercise 26, $\varphi(t) \in S$ for every
$t$, and $\varphi$ is injective: if $\varphi(t) = \varphi(s)$ then $(t - s)(\mathbf{v} - \mathbf{u}) = \mathbf{0}$,
so $t = s$ because $\mathbf{v} - \mathbf{u} \neq \mathbf{0}$.

Thus $S$ contains a subset in bijection with $\mathbb{R}$. Since $\mathbb{R}$ is uncountable (Cantor's
diagonal argument), $S$ is uncountable.

Consequently $|S| \in \{0, 1, 2^{\aleph_0}\}$ up to cardinality, and a linear system can never have
exactly countably many solutions: a countably infinite set would be neither a singleton nor
uncountable. $\blacksquare$
