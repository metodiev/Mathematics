# Determinants — Solutions

> [Tutorial](README.md) · [Exercises](exercises.md)

Every determinant below is checked by a second method, and every proof names the property or theorem it
uses. Strategy first, then algebra, then verification.

## Beginner

**1.** *(a)* $3\cdot2 - 4\cdot1 = 6 - 4 = 2$.

*(b)* $(-2)(-1) - 5\cdot3 = 2 - 15 = -13$.

*(c)* $a\cdot a - b\cdot b = a^2 - b^2$; the matrix is singular exactly when $a = \pm b$.

*(d)* $0\cdot0 - 1\cdot1 = -1$: this is the transposition matrix, a reflection in $y = x$, with the
expected sign $-1$.

**2.** Expanding along the first row, with cofactor signs $+,-,+$:

$$
\det A = 2\begin{vmatrix}4&1\\2&-2\end{vmatrix}
- (-1)\begin{vmatrix}0&1\\5&-2\end{vmatrix}
+ 3\begin{vmatrix}0&4\\5&2\end{vmatrix}
= 2(-8-2) + 1(0-5) + 3(0-20).
$$

So $\det A = -20 - 5 - 60 = -85$. *Check by Sarrus:*
$2\cdot4\cdot(-2) + (-1)\cdot1\cdot5 + 3\cdot0\cdot2 - 3\cdot4\cdot5 - 2\cdot1\cdot2 - (-1)\cdot0\cdot(-2)
= -16 - 5 + 0 - 60 - 4 = -85$ ✓.

**3.** The determinant is $0$. The matrix has a zero row, and this alone forces the value: if the second
row is $\mathbf{0}$, multiplying that row by any scalar $c$ leaves the matrix unchanged, so by
multilinearity $\det A = c\det A$ for every $c$; taking $c = 0$ gives $\det A = 0$. No arithmetic on the
other entries is needed, and the same argument applies to a zero column.

**4.** The matrix is upper triangular, so only the identity permutation contributes to the Leibniz sum
(Proposition 7.7(5)). Hence

$$
\det = 2\cdot(-1)\cdot3\cdot5 = -30 .
$$

*Check:* expanding along the first column gives the same value after three reductions, each to a smaller
triangular determinant: $2\big[(-1)(3\cdot5 - 0)\big] = -30$ ✓.

**5.** $\det(3A) = 3^3\det A = 27\cdot2 = 54$; $\det(-A) = (-1)^3\det A = -2$;
$\det(A^{\mathsf{T}}) = \det A = 2$ by Theorem 7.8. The first two use $\det(cA) = c^n\det A$ with $n = 3$
— a common trap is to write $\det(3A) = 3\det A$, which would be right only for a single row being
scaled.

**6.** The second row is $2$ times the first. By linearity in the second row,
$\det A = 2\det A'$ where $A'$ is $A$ with its second row replaced by the first; $A'$ has two equal rows,
so $\det A' = 0$ by alternation. Hence $\det A = 0$. The property at work is multilinearity plus
alternation — proportional rows always give determinant zero, whatever the other rows are.

**7.** Expanding along the first row of $A$:

$$
\det A = 1(50 - 48) - 2(40 - 42) + 3(32 - 35) = 2 + 4 - 9 = -3 .
$$

For $A^{\mathsf{T}} = \begin{pmatrix}1&4&7\\ 2&5&8\\ 3&6&10\end{pmatrix}$, expanding again along the first
row: $\det A^{\mathsf{T}} = 1(50-48) - 4(20-24) + 7(12-15) = 2 + 16 - 21 = -3$ ✓. The two determinants
agree, as Theorem 7.8 predicts; note that the intermediate cofactors are quite different, so this is a
genuine check rather than a repetition.

**8.** *(a)* The swap $\begin{pmatrix}0&1&0\\1&0&0\\0&0&1\end{pmatrix}$ has determinant $-1$.

*(b)* Scaling the first row by $5$ gives $\operatorname{diag}(5,1,1)$, determinant $5$.

*(c)* Adding $-2$ times row $1$ to row $3$ gives $\begin{pmatrix}1&0&0\\0&1&0\\-2&0&1\end{pmatrix}$, which is
lower triangular with diagonal entries $1$, determinant $1$.

These three numbers are exactly the factors by which the corresponding row operations multiply a
determinant (Proposition 7.7), which is why Gaussian elimination can compute determinants.

**9.** $\begin{vmatrix}x&2\\8&x\end{vmatrix} = x^2 - 16 = (x-4)(x+4)$, so the equation holds exactly for
$x = 4$ and $x = -4$. *Check:* at $x = 4$ the rows are proportional, $(8, 4) = 2(4,2)$; at $x = -4$,
$(8,-4) = -2(-4,2)$ ✓.

**10.** $A$: $\det A = 1(0 - 24) - 2(0 - 20) + 3(0 - 5) = -24 + 40 - 15 = 1 \ne 0$, invertible. $B$:
$\det B = 4 - 4 = 0$, singular (the second row is twice the first). $C$:
$\det C = 1(1 - 0) - 0 + 2(0 - 3) = 1 - 6 = -5 \ne 0$, invertible. The criterion is Theorem 7.9.

## Intermediate

**11.** Fix $\mathbf{a}_2,\dots,\mathbf{a}_n$ and let the first argument be
$\mathbf{c} = s\mathbf{u} + t\mathbf{v}$, so $c_{i1} = su_i + tv_i$. Each term of the Leibniz sum contains
exactly one entry from the first column, so

$$
\det(\mathbf{c},\mathbf{a}_2,\dots,\mathbf{a}_n)
= \sum_{\sigma}\operatorname{sgn}(\sigma)\,(su_{\sigma(1)} + tv_{\sigma(1)})
\prod_{i=2}^{n}a_{i,\sigma(i)} .
$$

Splitting the sum into the $s$-part and the $t$-part gives

$$
= s\sum_{\sigma}\operatorname{sgn}(\sigma)u_{\sigma(1)}\prod_{i\ge2}a_{i,\sigma(i)}
+ t\sum_{\sigma}\operatorname{sgn}(\sigma)v_{\sigma(1)}\prod_{i\ge2}a_{i,\sigma(i)}
= s\det(\mathbf{u},\mathbf{a}_2,\dots) + t\det(\mathbf{v},\mathbf{a}_2,\dots). \ \square
$$

The same argument with the first column replaced by column $j$ proves linearity in every column, which is
multilinearity.

**12.** Let the $i$-th row of $A$ be $\mathbf{0}$, and let $A(c)$ be $A$ with that row multiplied by $c$.
Since $c\cdot\mathbf{0} = \mathbf{0}$, the matrix $A(c)$ equals $A$ for every $c$. By multilinearity in
row $i$, $\det A(c) = c\det A$. So $\det A = c\det A$ for all $c \in K$, in particular for $c = 0$, giving
$\det A = 0$. $\square$ (Alternatively, expand along a different row: every term contains the zero row's
entry, hence vanishes. The multilinearity argument is cleaner because it uses only the axioms.)

**13.** Write the rows of $A$ as $\mathbf{r}_1,\dots,\mathbf{r}_n$; the rows of $cA$ are
$c\mathbf{r}_1,\dots,c\mathbf{r}_n$. Applying multilinearity in each row in turn,

$$
\det(cA) = \det(c\mathbf{r}_1,\dots,c\mathbf{r}_n)
= c\det(\mathbf{r}_1, c\mathbf{r}_2,\dots,c\mathbf{r}_n) = \cdots = c^n\det(\mathbf{r}_1,\dots,\mathbf{r}_n).
$$

So $\det(cA) = c^n \det A$. The exponent is the size of the matrix, not to be confused with the factor for
scaling a single row. $\square$

**14.** Since $AA^{-1} = I$, multiplicativity (Theorem 7.11) gives
$1 = \det I = \det(A)\det(A^{-1})$, so $\det(A^{-1}) = 1/\det A$. For the powers, induct on $k$: the case
$k = 1$ is trivial, and if $\det(A^k) = (\det A)^k$ then
$\det(A^{k+1}) = \det(A^kA) = \det(A^k)\det A = (\det A)^{k+1}$. $\square$

**15.** $\det A = 2\cdot3 - 1\cdot5 = 1$ and $\det B = 1\cdot1 - 4\cdot2 = -7$. The product is

$$
AB = \begin{pmatrix}2&1\\5&3\end{pmatrix}\begin{pmatrix}1&4\\2&1\end{pmatrix}
= \begin{pmatrix}2+2 & 8+1\\ 5+6 & 20+3\end{pmatrix} = \begin{pmatrix}4&9\\11&23\end{pmatrix},
\qquad \det(AB) = 92 - 99 = -7 .
$$

And $\det A\det B = 1\cdot(-7) = -7$ ✓. Note $\det A = 1$ here, so $A$ is unimodular and
$A^{-1} = \begin{pmatrix}3&-1\\-5&2\end{pmatrix}$ has integer entries, consistent with Exercise 31.

**16.** The cofactors, using $C_{ij} = (-1)^{i+j}M_{ij}$:

$$
C_{11} = 3-1 = 2,\quad C_{12} = -(0-2) = 2,\quad C_{13} = 0-6 = -6,
$$
$$
C_{21} = -(2-0) = -2,\quad C_{22} = 1-0 = 1,\quad C_{23} = -(1-4) = 3,
$$
$$
C_{31} = 2-0 = 2,\quad C_{32} = -(1-0) = -1,\quad C_{33} = 3-0 = 3 .
$$

The adjugate is the transpose of the cofactor matrix:

$$
\operatorname{adj}M = \begin{pmatrix}2&-2&2\\ 2&1&-1\\ -6&3&3\end{pmatrix},
\qquad
\det M = 1(3-1) - 2(0-2) + 0 = 2 + 4 = 6 .
$$

*Check* $M\operatorname{adj}M = 6I_3$, row by row against the columns $(2,2,-6)$, $(-2,1,3)$, $(2,-1,3)$
of the adjugate:

$$
(1,2,0)\cdot(2,2,-6) = 6,\quad (1,2,0)\cdot(-2,1,3) = 0,\quad (1,2,0)\cdot(2,-1,3) = 0;
$$
$$
(0,3,1)\cdot(2,2,-6) = 0,\quad (0,3,1)\cdot(-2,1,3) = 6,\quad (0,3,1)\cdot(2,-1,3) = 0;
$$
$$
(2,1,1)\cdot(2,2,-6) = 0,\quad (2,1,1)\cdot(-2,1,3) = 0,\quad (2,1,1)\cdot(2,-1,3) = 6,
$$

so the product is $6I_3$ ✓. Hence
$M^{-1} = \tfrac16\operatorname{adj}M =
\begin{pmatrix}1/3&-1/3&1/3\\ 1/3&1/6&-1/6\\ -1&1/2&1/2\end{pmatrix}$, and $MM^{-1} = I$ by construction
(Theorem 7.14).

**17.** The coefficient matrix is $S = \begin{pmatrix}1&2&1\\ 2&1&-1\\ 1&-1&2\end{pmatrix}$ with

$$
\det S = 1(2-1) - 2(4+1) + 1(-2-1) = 1 - 10 - 3 = -12 .
$$

Replacing the columns by $\mathbf{b} = (4,5,-3)^{\mathsf{T}}$:

$$
\det S_1 = \begin{vmatrix}4&2&1\\ 5&1&-1\\ -3&-1&2\end{vmatrix} = -12,\qquad
\det S_2 = \begin{vmatrix}1&4&1\\ 2&5&-1\\ 1&-3&2\end{vmatrix} = -24,\qquad
\det S_3 = \begin{vmatrix}1&2&4\\ 2&1&5\\ 1&-1&-3\end{vmatrix} = 12 .
$$

So $x = \tfrac{-12}{-12} = 1$, $y = \tfrac{-24}{-12} = 2$, $z = \tfrac{12}{-12} = -1$. *Check:*
$1 + 4 - 1 = 4$ ✓; $2 + 2 + 1 = 5$ ✓; $1 - 2 - 2 = -3$ ✓. Note also that each numerator is
$\det S$ times the corresponding unknown, so a single wrong numerator shows up immediately in the
substitution check.

**18.** The first matrix is block upper triangular with $A = \begin{pmatrix}1&2\\0&1\end{pmatrix}$ (upper
triangular, $\det A = 1$) and $D = \begin{pmatrix}2&5\\4&1\end{pmatrix}$ ($\det D = 2 - 20 = -18$). By
Theorem 7.16, $\det = 1\cdot(-18) = -18$. *Check by expansion along the first column:* two nonzero entries,
and the recursion reproduces $-18$ ✓.

The second matrix has the anti-block form with $B = \begin{pmatrix}1&2\\3&4\end{pmatrix}$,
$C = \begin{pmatrix}5&6\\7&8\end{pmatrix}$, $p = q = 2$. Now $\det B = 4 - 6 = -2$ and
$\det C = 40 - 42 = -2$, so by Proposition 7.17,

$$
\det = (-1)^{2\cdot2}(-2)(-2) = 1\cdot4 = 4 .
$$

*Check:* moving the two bottom rows above the top two costs $4$ row swaps, so the sign is
$(-1)^4 = +1$, and the resulting block diagonal matrix has determinant $(-2)(-2) = 4$ ✓; direct expansion
confirms $4$.

**19.** Subtract row $3$ from rows $1$ and $2$ (operations of the third kind, so the determinant is
unchanged):

$$
\begin{pmatrix}1&t&t\\ t&1&t\\ t&t&1\end{pmatrix} \longrightarrow
\begin{pmatrix}1-t&t-1&0\\ 0&1-t&t-1\\ t&t&1\end{pmatrix}.
$$

Factor $1-t$ out of the first two rows:

$$
\det = (1-t)^2\begin{vmatrix}1&-1&0\\ 0&1&-1\\ t&t&1\end{vmatrix}.
$$

Expanding the remaining determinant along its first row gives
$1(1 + t) - (-1)(0 + t) = 1 + 2t$. Hence

$$
\det = (1-t)^2(1+2t),
$$

which vanishes exactly for $t = 1$ and $t = -\tfrac12$. *Check at* $t = 1$: all entries are $1$, the rank
is $1$, and indeed the determinant is $0$; at $t = 0$ the formula gives $1$, and the matrix is $I_3$ ✓.

**20.** Expanding along the first column (or first row),

$$
\begin{vmatrix}1&1&1\\ 1&2&4\\ 1&4&16\end{vmatrix}
= 1(32 - 16) - 1(16 - 4) + 1(4 - 2) = 16 - 12 + 2 = 6 .
$$

The general formula is

$$
\det\begin{pmatrix}1&x_1&x_1^2\\ 1&x_2&x_2^2\\ 1&x_3&x_3^2\end{pmatrix} = (x_2 - x_1)(x_3 - x_1)(x_3 - x_2),
$$

which for $(x_1,x_2,x_3) = (1,2,4)$ gives $(1)(3)(2) = 6$ ✓. The determinant is the product of all
pairwise differences, so it vanishes exactly when two of the $x_i$ coincide — the algebraic reason a
polynomial is determined by its values at distinct points (Exercise 35 proves the general $n$ case).
