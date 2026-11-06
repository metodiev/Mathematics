# Matrices — Exercises

> Companion to the [tutorial](README.md). Solutions are in [solutions.md](solutions.md).

Work on paper. Before each computation write down the sizes of the matrices involved and the size of the
expected answer; after each computation check one entry by a second route. If you are stuck for more than
twenty minutes, read only the first line of the corresponding solution and continue on your own.

Problems are numbered continuously so that the solutions file mirrors them exactly. Level labels indicate
the amount of synthesis required, not the length of the answer.

## Beginner

**1.** For $A=\begin{pmatrix}1&2\\3&4\end{pmatrix}$ and $B=\begin{pmatrix}0&-1\\2&5\end{pmatrix}$, compute
$A+B$ and $3A-2B$.

**2.** For $A=\begin{pmatrix}2&1\\-1&3\end{pmatrix}$ and $B=\begin{pmatrix}1&0\\4&2\end{pmatrix}$, compute
$AB$ and $BA$. Are they equal?

**3.** Let $A$ be $2\times3$, $B$ be $3\times4$, $C$ be $4\times2$ and $D$ be $2\times2$. Which of the
products $AB$, $BA$, $AC$, $AD$, $BC$, $CB$, $CD$, $DC$, $CA$, $DA$, $D^2$ are defined? Give the size of
each that is.

**4.** For $A=\begin{pmatrix}1&2&0\\0&1&3\\2&0&1\end{pmatrix}$ and
$B=\begin{pmatrix}1&0&2\\0&1&0\\3&0&1\end{pmatrix}$, compute $AB$ and $BA$.

**5.** For $A=\begin{pmatrix}2&-3\\5&1\end{pmatrix}$, verify that $AI=IA=A$ for the $2\times2$ identity.

**6.** For $A=\begin{pmatrix}1&2&3\\4&5&6\end{pmatrix}$ and $B=\begin{pmatrix}1&0\\2&-1\\3&1\end{pmatrix}$,
compute $AB$, $(AB)^{\mathsf{T}}$ and $B^{\mathsf{T}}A^{\mathsf{T}}$, and check that the last two agree.

**7.** For $A=\begin{pmatrix}1&2\\3&4\end{pmatrix}$ and $B=\begin{pmatrix}5&6\\7&8\end{pmatrix}$, compute
$AB$, $BA$, and verify $\operatorname{tr}(AB)=\operatorname{tr}(BA)$.

**8.** The matrix $R=\begin{pmatrix}0&-1\\1&0\end{pmatrix}$ rotates the plane by $90^\circ$ anticlockwise.
Apply it to $(3,1)$ and to $(-2,5)$, and check that lengths are preserved.

**9.** Solve $\begin{pmatrix}2&1\\1&3\end{pmatrix}\begin{pmatrix}x\\y\end{pmatrix}=\begin{pmatrix}5\\10\end{pmatrix}$
using the inverse of the coefficient matrix, and verify the solution.

**10.** Let $E=\begin{pmatrix}0&1\\1&0\end{pmatrix}$ and $A=\begin{pmatrix}1&2\\3&4\end{pmatrix}$. Compute
$EA$ and $AE$, and describe what each product does to $A$.

**11.** For $D=\begin{pmatrix}2&0\\0&3\end{pmatrix}$, compute $D^3$, $D^0$ and $D^{-1}$.

**12.** For $A=\begin{pmatrix}1&2\\0&1\end{pmatrix}$, compute $A^2$ and $A^3$, guess $A^n$, and prove the
guess by induction.

## Intermediate

**13.** Find the inverse of $\begin{pmatrix}3&5\\1&2\end{pmatrix}$ and verify both $AA^{-1}=I$ and
$A^{-1}A=I$.

**14.** Find the inverse of $A=\begin{pmatrix}1&2&3\\0&1&4\\5&6&0\end{pmatrix}$ by row reduction, and verify
$AA^{-1}=I$ explicitly.

**15.** Solve the system $x+2y+3z=1$, $y+4z=2$, $5x+6y=3$ using the inverse from Exercise 14, and verify
the solution in all three equations.

**16.** For $A=\begin{pmatrix}1&2\\3&4\\5&6\end{pmatrix}$, compute $A^{\mathsf{T}}A$ and $AA^{\mathsf{T}}$.
State the size of each and check that both are symmetric.

**17.** Partition $A=\begin{pmatrix}1&0&2&1\\0&1&1&0\\0&0&1&2\\0&0&0&1\end{pmatrix}$ and
$B=\begin{pmatrix}1&1&0&0\\0&1&0&0\\1&0&1&0\\0&1&0&1\end{pmatrix}$ into $2\times2$ blocks, compute $AB$ by
block multiplication, and check one entry directly.

**18.** For $A=\begin{pmatrix}1&2\\3&4\end{pmatrix}$ and $B=\begin{pmatrix}0&1\\1&0\end{pmatrix}$, compute
$\operatorname{tr}(A+B)$, $\operatorname{tr}(AB)$, $\operatorname{tr}A\cdot\operatorname{tr}B$ and
$\operatorname{tr}(BA)$. What do the results show?

**19.** For $A=\begin{pmatrix}2&1\\0&2\end{pmatrix}$, prove by induction that
$A^n=\begin{pmatrix}2^n&n2^{n-1}\\0&2^n\end{pmatrix}$ for $n\ge1$, and compute $A^4$.

**20.** For $A=\begin{pmatrix}1&1\\0&1\end{pmatrix}$ and $B=\begin{pmatrix}1&0\\1&1\end{pmatrix}$, compute
$(A+B)^2$, $A^2+2AB+B^2$ and $A^2+AB+BA+B^2$. Which expansion is correct, and why?

**21.** Find every $2\times2$ matrix that commutes with $A=\begin{pmatrix}1&1\\0&1\end{pmatrix}$.

**22.** The triangle graph on vertices $1,2,3$ has adjacency matrix
$A=\begin{pmatrix}0&1&1\\1&0&1\\1&1&0\end{pmatrix}$. Compute $A^2$ and interpret its diagonal entries.

## Advanced

**23.** Prove that $(AB)^{\mathsf{T}}=B^{\mathsf{T}}A^{\mathsf{T}}$ for $A\in M_{m\times n}$ and
$B\in M_{n\times p}$, by comparing the $(i,j)$ entries.

**24.** Prove that $\operatorname{tr}(AB)=\operatorname{tr}(BA)$ for square matrices of the same size, deduce
$\operatorname{tr}(ABC)=\operatorname{tr}(BCA)$, and give an explicit pair with
$\operatorname{tr}(AB)\ne\operatorname{tr}A\cdot\operatorname{tr}B$.

**25.** Prove $(AB)C=A(BC)$ by comparing entries, stating which properties of real numbers are used.

**26.** Prove that an inverse, when it exists, is unique; then prove $(AB)^{-1}=B^{-1}A^{-1}$ and
$(A^{-1})^{-1}=A$ for invertible square matrices.

**27.** Prove that a square matrix with a row of zeros cannot be invertible. Then prove that a square matrix
with two equal rows cannot be invertible either.

**28.** For $A=\begin{pmatrix}a&b\\c&d\end{pmatrix}$ with $\Delta=ad-bc$, prove that
$\frac{1}{\Delta}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}$ is the inverse when $\Delta\ne0$, and prove that no
inverse exists when $\Delta=0$.

**29.** Prove that each of the three types of elementary matrix is invertible, giving the inverse explicitly,
and show that $T_{ij}(c)^{-1}=T_{ij}(-c)$ for $i\ne j$.

**30.** Prove by induction that $M^n=\begin{pmatrix}F_{n+1}&F_n\\F_n&F_{n-1}\end{pmatrix}$ for
$M=\begin{pmatrix}1&1\\1&0\end{pmatrix}$ and the Fibonacci numbers $F_0=0$, $F_1=F_2=1$. Use it to compute
$M^9$.

## Challenge

**31.** Let $A=\begin{pmatrix}0&1&0\\0&0&1\\0&0&0\end{pmatrix}$. Compute $A^2$ and $A^3$, show that
$(I-A)^{-1}=I+A+A^2$, and verify the product explicitly.

**32.** Let $A,B$ be $2\times2$ matrices with $AB=I$. Prove, by writing out the four entries of the product,
that then $BA=I$ as well. (In particular, a one-sided inverse of a $2\times2$ matrix is two-sided.)

**33.** Prove that if $A$ and $D$ are invertible then
$\begin{pmatrix}A&B\\0&D\end{pmatrix}^{-1}=\begin{pmatrix}A^{-1}&-A^{-1}BD^{-1}\\0&D^{-1}\end{pmatrix}$
by multiplying the two block matrices. Apply the formula to
$M=\begin{pmatrix}1&2&1&0\\0&1&0&1\\0&0&2&1\\0&0&0&1\end{pmatrix}$ and verify one row of $MM^{-1}$.

**34.** Prove by induction that for an adjacency matrix $A$, the entry $(A^k)_{ij}$ counts the walks of
length $k$ from vertex $i$ to vertex $j$. Then compute $A^3$ for the triangle graph of Exercise 22 and
check the total number of three-step walks from vertex $1$ against a direct count.

**35.** Prove the $2\times2$ Cayley–Hamilton identity $A^2-(\operatorname{tr}A)A+(\det A)I=0$ by direct
computation, and deduce that $A^{-1}=\frac{1}{\det A}\bigl((\operatorname{tr}A)I-A\bigr)$ when
$\det A\ne0$. Apply both statements to $A=\begin{pmatrix}3&1\\2&4\end{pmatrix}$.

**36.** Find the $3\times3$ homogeneous matrix that rotates the plane by $90^\circ$ anticlockwise about
$(-1,2)$, and apply it to $(0,2)$ and $(-1,3)$. Verify that the centre is fixed.
