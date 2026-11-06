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

**19.** Replace row $1$ by row $1$ minus row $2$, then row $2$ by row $2$ minus row $3$ (operations of
the third kind, so the determinant is unchanged):

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

## Advanced

**21.** First note the **first-column expansion**: grouping the Leibniz terms by the row $j$ in which the
column $1$ is used, that is by $\sigma(j) = 1$, and repeating the argument of Theorem 7.5 with rows and
columns exchanged, gives

$$
\det A = \sum_{j=1}^{n}(-1)^{1+j}a_{j1}\det M_{j1}.
\tag{$\ast$}
$$

Now induct on $n$. For $n = 1$ there is nothing to prove. For $n \ge 2$, expand $\det A^{\mathsf{T}}$
along its first row. The entry in position $(1,j)$ of $A^{\mathsf{T}}$ is $a_{j1}$, and the minor of
$A^{\mathsf{T}}$ obtained by deleting row $1$ and column $j$ is $(M_{j1})^{\mathsf{T}}$: deleting row $1$
and column $j$ from $A^{\mathsf{T}}$ is the same as deleting column $1$ and row $j$ from $A$ and then
transposing. Hence, by the induction hypothesis applied to the $(n-1)\times(n-1)$ matrix $M_{j1}$,

$$
\det A^{\mathsf{T}} = \sum_{j=1}^{n}(-1)^{1+j}a_{j1}\det\big((M_{j1})^{\mathsf{T}}\big)
= \sum_{j=1}^{n}(-1)^{1+j}a_{j1}\det M_{j1} = \det A
$$

by $(\ast)$. $\square$

**22.** Let $A'$ be $A$ with rows $p$ and $q$ exchanged, and let $\pi = (p\,q)$ be the transposition of the
row indices, so $a'_{ij} = a_{\pi(i),j}$. In the Leibniz formula for $A'$, put $\sigma = \tau\circ\pi$
(equivalently $\tau = \sigma\circ\pi^{-1} = \sigma\circ\pi$). Then

$$
\prod_{i=1}^{n}a'_{i,\sigma(i)} = \prod_{i=1}^{n}a_{\pi(i),\sigma(i)}
= \prod_{i=1}^{n}a_{\pi(i),\tau(\pi(i))} = \prod_{k=1}^{n}a_{k,\tau(k)},
$$

the last step by relabelling $k = \pi(i)$, and
$\operatorname{sgn}(\sigma) = \operatorname{sgn}(\tau)\operatorname{sgn}(\pi) = -\operatorname{sgn}(\tau)$.
Therefore

$$
\det A' = \sum_{\tau}(-\operatorname{sgn}\tau)\prod_{k}a_{k,\tau(k)} = -\det A . \qquad\square
$$

For two equal rows, exchanging them leaves the matrix unchanged, so $\det A = \det A' = -\det A$, whence
$\det A = 0$ (and $2 \neq 0$ in $K$).

**23.** Suppose $\mathbf{r}_i = \sum_{k \ne i}c_k\mathbf{r}_k$ is the $i$-th row. By multilinearity in
row $i$,

$$
\det A = \sum_{k\ne i}c_k\det A^{(k)},
$$

where $A^{(k)}$ is $A$ with row $i$ replaced by row $k$. Each $A^{(k)}$ has rows $i$ and $k$ equal, so
$\det A^{(k)} = 0$ and $\det A = 0$.

For the deduction: if the rows are linearly dependent there are scalars $c_i$, not all zero, with
$\sum_i c_i\mathbf{r}_i = \mathbf{0}$. Choosing $k$ with $c_k \ne 0$ and solving,
$\mathbf{r}_k = \sum_{i \ne k}(-c_i/c_k)\mathbf{r}_i$; by the first part, $\det A = 0$, so by Theorem 7.9
the matrix is singular. $\square$

*Remark.* The same argument with columns is Exercise 24; both are instances of "a repeated direction
flattens the parallelepiped".

**24.** Repeated columns: if $\mathbf{a}_i = \mathbf{a}_j$ with $i \ne j$, alternation gives
$\det A = 0$ directly.

Rank: if $\operatorname{rank}A < n$ then the $n$ columns are linearly dependent, so there are scalars
$c_1,\dots,c_n$ not all zero with $\sum_j c_j\mathbf{a}_j = \mathbf{0}$. Pick $k$ with $c_k \ne 0$ and
solve for $\mathbf{a}_k$:

$$
\mathbf{a}_k = \sum_{j \ne k}\Big(-\frac{c_j}{c_k}\Big)\mathbf{a}_j .
$$

By multilinearity in column $k$, $\det A$ is the corresponding linear combination of determinants of
matrices in which column $k$ has been replaced by column $j$ for some $j \ne k$; each such matrix has a
repeated column, so each determinant is $0$, and hence $\det A = 0$. $\square$

**25.** *Step 1: elementary matrices.* Let $E$ be elementary and $A$ arbitrary.

* If $E$ is a row swap, then $EA$ is $A$ with two rows exchanged, so $\det(EA) = -\det A = \det E\det A$
  by Exercise 22, since $\det E = -1$.
* If $E$ scales row $i$ by $c$, then $EA$ scales that row, so $\det(EA) = c\det A = \det E\det A$.
* If $E$ adds $c$ times row $i$ to row $j$ ($i \ne j$), then $\det(EA) = \det A = \det E\det A$, since
  $\det E = 1$.

*Step 2: reduction.* Reduce $A$ to a row echelon form: there are elementary matrices with
$E_k\cdots E_1A = R$. Iterating Step 1, $\det R = \big(\prod_i\det E_i\big)\det A$.

*Case $A$ invertible:* then $R = I_n$, so $\big(\prod_i \det E_i\big)\det A = 1$ and
$\det A = \prod_i \det(E_i^{-1})$, because $\det(E_i^{-1}) = 1/\det E_i$. Also
$A = (E_k\cdots E_1)^{-1} = E_1^{-1}\cdots E_k^{-1}$. For arbitrary $B$,

$$
\det(AB) = \det(E_1^{-1}\cdots E_k^{-1}B) = \Big(\prod_i\det E_i^{-1}\Big)\det B = \det A\,\det B,
$$

again by iterating Step 1 (each $E_i^{-1}$ is elementary).

*Case $A$ singular:* then $\det A = 0$ by Theorem 7.9. Also $\operatorname{im}(AB) \subseteq
\operatorname{im}A$, so $\operatorname{rank}(AB) \le \operatorname{rank}A < n$ and $AB$ is singular, giving
$\det(AB) = 0 = \det A\det B$. $\square$

**26.** By Theorem 7.17 of [Linear Transformations](../05-linear-transformations/README.md), matrices of
the same operator in two bases satisfy $[T]_{B'} = P^{-1}[T]_BP$ with $P = [\operatorname{id}]_B^{B'}$
invertible. Then, using multiplicativity twice,

$$
\det[T]_{B'} = \det(P^{-1})\det[T]_B\det P = \frac{1}{\det P}\det[T]_B\det P = \det[T]_B .
$$

So all matrices of $T$ have the same determinant, and $\det T := \det[T]_B$ is well defined: it does not
depend on the chosen basis. $\square$

**27.** *The naive formula fails.* Take $2\times2$ blocks $A = D = 0$ and $B = C = I_2$. Then
$\begin{pmatrix}0&I\\I&0\end{pmatrix}$ has determinant $(-1)^{2\cdot2}\det I\det I = 1$ (Proposition 7.17),
whereas $\det A\det D - \det B\det C = 0 - 1 = -1$. So there is no "$2\times2$ Sarrus rule" for blocks.

*Schur complement.* Factor

$$
\begin{pmatrix}A&B\\ C&D\end{pmatrix}
= \begin{pmatrix}I_p&0\\ CA^{-1}&I_q\end{pmatrix}
\begin{pmatrix}A&B\\ 0&D - CA^{-1}B\end{pmatrix}.
$$

The first factor is block lower triangular with identity diagonal blocks, so its determinant is $1$; the
second is block upper triangular, so by Theorem 7.16 its determinant is
$\det A\cdot\det(D - CA^{-1}B)$. Multiplying out confirms the factorisation: the bottom-left block of the
product is $CA^{-1}A + 0 = C$ and the bottom-right is $CA^{-1}B + (D - CA^{-1}B) = D$. Hence

$$
\det\begin{pmatrix}A&B\\ C&D\end{pmatrix} = \det A\,\det(D - CA^{-1}B). \qquad\square
$$

**28.** From $A\operatorname{adj}A = (\det A)I$ (Theorem 7.14), multiply on the left by $A^{-1}$:
$\operatorname{adj}A = \det(A)A^{-1}$.

Then, for invertible $A, B$,

$$
\operatorname{adj}(AB) = \det(AB)(AB)^{-1} = \det A\det B\,B^{-1}A^{-1}
= \big(\det B\,B^{-1}\big)\big(\det A\,A^{-1}\big) = \operatorname{adj}B\,\operatorname{adj}A . \qquad\square
$$

The order reverses, exactly as for inverses; the identity extends to all matrices by the argument of
Exercise 36.

**29.** Expanding the $2\times2$ determinant,

$$
\det(\lambda I - A) = \begin{vmatrix}\lambda - a&-b\\ -c&\lambda - d\end{vmatrix}
= (\lambda - a)(\lambda - d) - bc = \lambda^2 - (a+d)\lambda + (ad - bc),
$$

which is $\lambda^2 - (\operatorname{tr}A)\lambda + \det A$ ✓. For
$A = \begin{pmatrix}3&1\\2&4\end{pmatrix}$: $\operatorname{tr}A = 7$, $\det A = 12 - 2 = 10$, so
$p_A(\lambda) = \lambda^2 - 7\lambda + 10 = (\lambda - 5)(\lambda - 2)$. *Check:* $p_A(0) = 10 = \det A$ ✓
and the coefficient of $\lambda$ is $-7 = -\operatorname{tr}A$ ✓; the roots $5, 2$ sum to $7$ and multiply
to $10$, as Proposition 7.18 predicts.

**30.** Moving the last $q$ rows above the first $p$ rows costs $p q$ row transpositions (each of the $q$
rows must pass $p$ others), and each transposition multiplies the determinant by $-1$. The result is
$\begin{pmatrix}C&0\\0&B\end{pmatrix}$, whose determinant is $\det C\det B$ by Theorem 7.16. Hence

$$
\det\begin{pmatrix}0&B\\ C&0\end{pmatrix} = (-1)^{pq}\det C\det B = (-1)^{pq}\det B\det C . \qquad\square
$$

*Check with Exercise 18:* $p = q = 2$, $\det B = \det C = -2$, sign $(-1)^4 = 1$, determinant $4$ ✓,
matching the direct computation.

## Challenge

**31.** ($\Rightarrow$) If $A^{-1}$ has integer entries then $\det A$ and $\det A^{-1}$ are both integers,
and their product is $\det(AA^{-1}) = 1$. The only integers whose product is $1$ are $1$ and $1$, or $-1$
and $-1$; in either case $\det A = \pm1$.

($\Leftarrow$) Suppose $\det A = \pm1$. The entries of $\operatorname{adj}A$ are cofactors, that is
$\pm$ determinants of $(n-1)\times(n-1)$ matrices with integer entries, hence integers. By
Corollary 7.15, $A^{-1} = \operatorname{adj}A/\det A = \pm\operatorname{adj}A$, which has integer
entries. $\square$

*Example.* $A = \begin{pmatrix}2&1\\5&3\end{pmatrix}$ has $\det A = 1$, and indeed
$A^{-1} = \begin{pmatrix}3&-1\\-5&2\end{pmatrix}$ is integral (Exercise 15). The matrix
$\begin{pmatrix}2&0\\0&2\end{pmatrix}$ has determinant $4$ and inverse with entries $\tfrac12$, not
integral.

**32.** By multiplicativity and transpose invariance,
$\det(A^{\mathsf{T}}A) = \det(A^{\mathsf{T}})\det A = (\det A)^2 \ge 0$, since a square of a real number
is non-negative. (This also shows $A^{\mathsf{T}}A$ is invertible exactly when $A$ is.)

Now let $S$ be real skew-symmetric of odd size $n$, so $S^{\mathsf{T}} = -S$. Then

$$
\det S = \det(S^{\mathsf{T}}) = \det(-S) = (-1)^n\det S = -\det S,
$$

using $\det(cS) = c^n\det S$ with $c = -1$ and $n$ odd. Hence $2\det S = 0$, so $\det S = 0$: every
real skew-symmetric matrix of odd size is singular. $\square$

*Example.* $S = \begin{pmatrix}0&a&b\\ -a&0&c\\ -b&-c&0\end{pmatrix}$ has determinant
$a b c - a b c = 0$; for skew-symmetric matrices of size $2$ the determinant is $a^2 \ge 0$ in general
non-negative, and the eigenvalues come in pairs $\pm i\lambda$.

**33.** Write $M = (1-t)I_n + tJ_n$, where $J_n$ is the all-ones matrix, but argue with row operations so
that no unproved identity is used. Subtract row $n$ from each of rows $1,\dots,n-1$ (operations of the
third kind, so the determinant is unchanged). Row $i$, for $i < n$, becomes

$$
\big(0,\dots,0,\ 1 - t,\ 0,\dots,0,\ t - 1\big),
$$

with $1-t$ in position $i$ and $t-1$ in position $n$. Factor $1-t$ out of each of the first $n-1$ rows:

$$
\det M = (1-t)^{n-1}\det N,\qquad
N = \begin{pmatrix}
1&0&\cdots&0&-1\\
0&1&\cdots&0&-1\\
\vdots&&\ddots&&\vdots\\
0&0&\cdots&1&-1\\
t&t&\cdots&t&1
\end{pmatrix}.
$$

Add rows $1,\dots,n-1$ of $N$ to its last row: that row becomes $(t+1,\dots,t+1,\ 2-n)$. Then subtract
$(t+1)$ times each of rows $1,\dots,n-1$ from the last row; this clears its first $n-1$ entries and
leaves in the last position $(2-n) + (n-1)(t+1) = 1 + (n-1)t$. The matrix is now upper triangular with
diagonal $1,\dots,1,1+(n-1)t$, so $\det N = 1 + (n-1)t$ and

$$
\det M = (1-t)^{n-1}\big(1 + (n-1)t\big). \qquad\square
$$

*Check for $n = 4$, $t = 1$:* the formula gives $0$, and indeed all entries are $1$, so the rank is $1$;
for $n = 3$ and $t = -1$ the formula gives $(2)^2(1-2) = -4$, and direct expansion of
$\begin{pmatrix}1&-1&-1\\-1&1&-1\\-1&-1&1\end{pmatrix}$ gives $-4$ ✓.

**34.** Consider the $(m+n)\times(m+n)$ matrix
$M = \begin{pmatrix}I_m&-B\\ A&I_n\end{pmatrix}$ and factor it in two ways:

$$
M = \begin{pmatrix}I_m&0\\ A&I_n\end{pmatrix}\begin{pmatrix}I_m&-B\\ 0&I_n + AB\end{pmatrix},
\qquad
M = \begin{pmatrix}I_m&-B\\ 0&I_n\end{pmatrix}\begin{pmatrix}I_m + BA&0\\ A&I_n\end{pmatrix}.
$$

Both factorisations are checked by multiplying out: in the first, the bottom-right block is
$A(-B) + I_n\cdot(I_n + AB) = -AB + I_n + AB = I_n$; in the second, the top-left block is
$I_m(I_m + BA) + (-B)A = I_m + BA - BA = I_m$, and the top-right block is $I_m\cdot 0 + (-B)I_n = -B$.

Each factor is block triangular with identity diagonal blocks, so has determinant $1$, and the other
factor has determinant $\det(I_n + AB)$ respectively $\det(I_m + BA)$ by Theorem 7.16. Hence

$$
\det(I_n + AB) = \det M = \det(I_m + BA). \qquad\square
$$

*Check.* Take $m = 1$, $n = 2$, $A = (1\ \ 2)$, $B = \binom{3}{4}$; then $AB = 11$ (a $1\times1$
matrix), so $\det(I_1 + AB) = 12$, while $BA = \begin{pmatrix}3&6\\4&8\end{pmatrix}$ and
$\det(I_2 + BA) = \det\begin{pmatrix}4&6\\4&9\end{pmatrix} = 36 - 24 = 12$ ✓.

**35.** Let $V_n$ denote the $n\times n$ Vandermonde determinant, and argue by induction on $n$. For $n=1$
it is $1$, the empty product. For $n \ge 2$, perform the column operations
$C_j \leftarrow C_j - x_1C_{j-1}$ for $j = n, n-1, \dots, 2$, in that order. These are additions of
multiples of one column to another, so they leave the determinant unchanged, and they clear the first row:

$$
\begin{pmatrix}
1&x_1&x_1^2&\cdots&x_1^{n-1}\\
1&x_2&x_2^2&\cdots&x_2^{n-1}\\
\vdots&\vdots&&&\vdots\\
1&x_n&x_n^2&\cdots&x_n^{n-1}
\end{pmatrix}
\longrightarrow
\begin{pmatrix}
1&0&0&\cdots&0\\
1&x_2 - x_1&x_2(x_2-x_1)&\cdots&x_2^{n-2}(x_2-x_1)\\
\vdots&\vdots&&&\vdots\\
1&x_n - x_1&x_n(x_n-x_1)&\cdots&x_n^{n-2}(x_n-x_1)
\end{pmatrix},
$$

because the entry in row $i \ge 2$ and column $j \ge 2$ becomes
$x_i^j - x_1x_i^{j-1} = x_i^{j-1}(x_i - x_1)$. Expanding along the first row (whose only nonzero entry is
the leading $1$, with cofactor $+1$) leaves the $(n-1)\times(n-1)$ matrix with rows indexed by
$i = 2,\dots,n$ and columns $j = 1,\dots,n-1$; factor $(x_i - x_1)$ out of row $i$:

$$
V_n = \Big(\prod_{i=2}^{n}(x_i - x_1)\Big)\, V_{n-1}(x_2,\dots,x_n).
$$

By the induction hypothesis $V_{n-1}(x_2,\dots,x_n) = \prod_{2 \le i < j \le n}(x_j - x_i)$, so

$$
V_n = \prod_{i=2}^{n}(x_i - x_1)\prod_{2 \le i < j \le n}(x_j - x_i) = \prod_{1 \le i < j \le n}(x_j - x_i),
$$

which is exactly the claimed formula (the first product supplies the pairs $(1,j)$). $\square$

*Consequence:* the Vandermonde determinant is nonzero exactly when the $x_i$ are pairwise distinct, which
is the linear-algebra proof that $n$ distinct points determine a unique interpolating polynomial of degree
$< n$.

**36.** *Non-singular case.* If $\det A \ne 0$, take determinants in $A\operatorname{adj}A = (\det A)I_n$
(Theorem 7.14):

$$
\det A\cdot\det(\operatorname{adj}A) = \det\big((\det A)I_n\big) = (\det A)^n,
$$

so $\det(\operatorname{adj}A) = (\det A)^{n-1}$ after dividing by $\det A \ne 0$.

*Singular case.* Let $A$ be arbitrary and consider $A + tI_n$ for $t \in \mathbb{R}$. The function
$t \mapsto \det(A + tI_n)$ is a polynomial of degree $n$, so it has at most $n$ roots; for every other $t$
the matrix $A + tI$ is invertible and the previous case gives

$$
\det\big(\operatorname{adj}(A + tI)\big) = \det(A + tI)^{n-1}.
$$

Both sides are polynomials in $t$ — the entries of the adjugate are polynomials in the entries of the
matrix, hence in $t$ — and they agree at infinitely many $t$. A nonzero polynomial has only finitely many
roots, so the two polynomials are identical, and evaluating at $t = 0$ gives
$\det(\operatorname{adj}A) = (\det A)^{n-1}$, which is $0$ when $A$ is singular. $\square$

*Iteration.* Apply the formula to the $n\times n$ matrix $\operatorname{adj}A$:

$$
\det\big(\operatorname{adj}(\operatorname{adj}A)\big) = \big(\det(\operatorname{adj}A)\big)^{n-1}
= \big((\det A)^{n-1}\big)^{n-1} = (\det A)^{(n-1)^2}. \qquad\square
$$

*Check for $n = 2$:* $\operatorname{adj}\begin{pmatrix}a&b\\c&d\end{pmatrix} =
\begin{pmatrix}d&-b\\-c&a\end{pmatrix}$ has determinant $ad - bc = \det A$, matching $(n-1)^2 = 1$; and
$\operatorname{adj}(\operatorname{adj}A) = A$ for $2\times2$ matrices, so
$\det(\operatorname{adj}(\operatorname{adj}A)) = \det A = (\det A)^{1}$ ✓.
