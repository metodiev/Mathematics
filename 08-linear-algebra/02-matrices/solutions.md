# Matrices — Solutions

> [Tutorial](README.md) · [Exercises](exercises.md) · 36 worked solutions

Each solution names the strategy, carries out every significant step, and verifies every matrix product
explicitly — by computing both sides or by checking entries. Where a problem admits a second approach, it
is shown or described.

## Beginner

### Solution 1

Add entrywise:
$$A+B=\begin{pmatrix}1+0&2+(-1)\\3+2&4+5\end{pmatrix}=\begin{pmatrix}1&1\\5&9\end{pmatrix}.$$
Scale first, then subtract:
$$3A=\begin{pmatrix}3&6\\9&12\end{pmatrix},\qquad 2B=\begin{pmatrix}0&-2\\4&10\end{pmatrix},\qquad
3A-2B=\begin{pmatrix}3&8\\5&2\end{pmatrix}.$$
Check one entry: $(3A-2B)_{22}=12-10=2$. $\checkmark$

### Solution 2

Row by column:
$$AB=\begin{pmatrix}2\cdot1+1\cdot4 & 2\cdot0+1\cdot2\\ (-1)\cdot1+3\cdot4 & (-1)\cdot0+3\cdot2\end{pmatrix}
=\begin{pmatrix}6&2\\11&6\end{pmatrix},$$
$$BA=\begin{pmatrix}1\cdot2+0\cdot(-1) & 1\cdot1+0\cdot3\\ 4\cdot2+2\cdot(-1) & 4\cdot1+2\cdot3\end{pmatrix}
=\begin{pmatrix}2&1\\6&10\end{pmatrix}.$$
Check: $(AB)_{11}=2+4=6$ and $(BA)_{22}=4+6=10$. The products are not equal, so the matrices do not
commute. Both are $2\times2$, as they must be for square matrices of the same size.

### Solution 3

A product is defined when the inner dimensions agree.

| Product | Inner dimensions | Defined? | Size |
|---|---|---|---|
| $AB$ | $3$ and $3$ | yes | $2\times4$ |
| $BC$ | $4$ and $4$ | yes | $3\times2$ |
| $CD$ | $2$ and $2$ | yes | $4\times2$ |
| $CA$ | $2$ and $2$ | yes | $4\times3$ |
| $DA$ | $2$ and $2$ | yes | $2\times3$ |
| $D^2$ | $2$ and $2$ | yes | $2\times2$ |

The remaining products fail: $BA$ needs $4=2$; $AC$ needs $3=4$; $AD$ needs $3=2$; $CB$ needs $2=3$;
$DB$ needs $2=3$; $DC$ needs $2=4$. In each case the number of columns of the left factor differs from the
number of rows of the right factor, so the sum $\sum_k a_{ik}b_{kj}$ has no common index range.

### Solution 4

First $AB$, row by column:
$$AB=\begin{pmatrix}
1\cdot1+2\cdot0+0\cdot3 & 1\cdot0+2\cdot1+0\cdot0 & 1\cdot2+2\cdot0+0\cdot1\\
0\cdot1+1\cdot0+3\cdot3 & 0\cdot0+1\cdot1+3\cdot0 & 0\cdot2+1\cdot0+3\cdot1\\
2\cdot1+0\cdot0+1\cdot3 & 2\cdot0+0\cdot1+1\cdot0 & 2\cdot2+0\cdot0+1\cdot1
\end{pmatrix}
=\begin{pmatrix}1&2&2\\9&1&3\\5&0&5\end{pmatrix}.$$

In the other order, $BA$ has entries:
$$BA=\begin{pmatrix}
1\cdot1+0\cdot0+2\cdot2 & 1\cdot2+0\cdot1+2\cdot0 & 1\cdot0+0\cdot3+2\cdot1\\
0\cdot1+1\cdot0+0\cdot2 & 0\cdot2+1\cdot1+0\cdot0 & 0\cdot0+1\cdot3+0\cdot1\\
3\cdot1+0\cdot0+1\cdot2 & 3\cdot2+0\cdot1+1\cdot0 & 3\cdot0+0\cdot3+1\cdot1
\end{pmatrix}
=\begin{pmatrix}5&2&2\\0&1&3\\5&6&1\end{pmatrix}.$$

Check one entry of each: $(AB)_{31}=2+0+3=5$; $(BA)_{23}=0+3+0=3$. The products differ, so $A$ and $B$ do
not commute, even though both are $3\times3$.

### Solution 5

For the $2\times2$ identity $I=\begin{pmatrix}1&0\\0&1\end{pmatrix}$,
$$AI=\begin{pmatrix}2\cdot1+(-3)\cdot0 & 2\cdot0+(-3)\cdot1\\5\cdot1+1\cdot0 & 5\cdot0+1\cdot1\end{pmatrix}
=\begin{pmatrix}2&-3\\5&1\end{pmatrix}=A,$$
$$IA=\begin{pmatrix}1\cdot2+0\cdot5 & 1\cdot(-3)+0\cdot1\\0\cdot2+1\cdot5 & 0\cdot(-3)+1\cdot1\end{pmatrix}
=\begin{pmatrix}2&-3\\5&1\end{pmatrix}=A.$$
In general $(AI)_{ij}=\sum_k a_{ik}\delta_{kj}=a_{ij}$, since only the $k=j$ term survives; the other order
is the same argument.

### Solution 6

Compute $AB$ (a $2\times2$ matrix):
$$AB=\begin{pmatrix}1\cdot1+2\cdot2+3\cdot3 & 1\cdot0+2\cdot(-1)+3\cdot1\\
4\cdot1+5\cdot2+6\cdot3 & 4\cdot0+5\cdot(-1)+6\cdot1\end{pmatrix}
=\begin{pmatrix}14&1\\32&1\end{pmatrix}.$$

Hence $(AB)^{\mathsf{T}}=\begin{pmatrix}14&32\\1&1\end{pmatrix}$. Now
$B^{\mathsf{T}}=\begin{pmatrix}1&2&3\\0&-1&1\end{pmatrix}$ and
$A^{\mathsf{T}}=\begin{pmatrix}1&4\\2&5\\3&6\end{pmatrix}$, so
$$B^{\mathsf{T}}A^{\mathsf{T}}=\begin{pmatrix}
1\cdot1+2\cdot2+3\cdot3 & 1\cdot4+2\cdot5+3\cdot6\\
0\cdot1+(-1)\cdot2+1\cdot3 & 0\cdot4+(-1)\cdot5+1\cdot6
\end{pmatrix}
=\begin{pmatrix}14&32\\1&1\end{pmatrix},$$
which agrees with $(AB)^{\mathsf{T}}$. Note the shapes: $A$ is $2\times3$, $B$ is $3\times2$, so $AB$ is
$2\times2$ while $B^{\mathsf{T}}A^{\mathsf{T}}$ is also $2\times2$, as it must be.

### Solution 7

$$AB=\begin{pmatrix}1\cdot5+2\cdot7 & 1\cdot6+2\cdot8\\3\cdot5+4\cdot7 & 3\cdot6+4\cdot8\end{pmatrix}
=\begin{pmatrix}19&22\\43&50\end{pmatrix},\qquad \operatorname{tr}(AB)=19+50=69.$$
$$BA=\begin{pmatrix}5\cdot1+6\cdot3 & 5\cdot2+6\cdot4\\7\cdot1+8\cdot3 & 7\cdot2+8\cdot4\end{pmatrix}
=\begin{pmatrix}23&34\\31&46\end{pmatrix},\qquad \operatorname{tr}(BA)=23+46=69.$$
Both traces equal $69$, although $AB\ne BA$ (compare entries). The identity
$\operatorname{tr}(AB)=\operatorname{tr}(BA)$ holds in general, and this example shows it is not a
coincidence of equal products.

### Solution 8

$$R\begin{pmatrix}3\\1\end{pmatrix}=\begin{pmatrix}0\cdot3+(-1)\cdot1\\1\cdot3+0\cdot1\end{pmatrix}
=\begin{pmatrix}-1\\3\end{pmatrix},\qquad
R\begin{pmatrix}-2\\5\end{pmatrix}=\begin{pmatrix}0\cdot(-2)+(-1)\cdot5\\1\cdot(-2)+0\cdot5\end{pmatrix}
=\begin{pmatrix}-5\\-2\end{pmatrix}.$$
Lengths: $\lVert(3,1)\rVert=\sqrt{10}=\lVert(-1,3)\rVert$ and
$\lVert(-2,5)\rVert=\sqrt{29}=\lVert(-5,-2)\rVert$. Dot products are preserved too:
$(3,1)\cdot(-2,5)=-6+5=-1$ and $(-1,3)\cdot(-5,-2)=5-6=-1$. This is expected: a rotation is an orthogonal
transformation, so it preserves lengths and angles.

### Solution 9

The coefficient matrix is $A=\begin{pmatrix}2&1\\1&3\end{pmatrix}$ with $ad-bc=6-1=5\ne0$, so
$$A^{-1}=\frac15\begin{pmatrix}3&-1\\-1&2\end{pmatrix}.$$
Then
$$\mathbf{x}=A^{-1}\begin{pmatrix}5\\10\end{pmatrix}
=\frac15\begin{pmatrix}3\cdot5-1\cdot10\\-1\cdot5+2\cdot10\end{pmatrix}
=\frac15\begin{pmatrix}5\\15\end{pmatrix}=\begin{pmatrix}1\\3\end{pmatrix}.$$
Verification: $2(1)+1(3)=5$ and $1(1)+3(3)=10$. $\checkmark$ The inverse computation can be checked by
multiplying $AA^{-1}=\frac15\begin{pmatrix}6-1&-2+2\\3-3&-1+6\end{pmatrix}=I$.

### Solution 10

$$EA=\begin{pmatrix}0&1\\1&0\end{pmatrix}\begin{pmatrix}1&2\\3&4\end{pmatrix}
=\begin{pmatrix}3&4\\1&2\end{pmatrix},\qquad
AE=\begin{pmatrix}1&2\\3&4\end{pmatrix}\begin{pmatrix}0&1\\1&0\end{pmatrix}
=\begin{pmatrix}2&1\\4&3\end{pmatrix}.$$
Left multiplication by $E$ swapped the two *rows* of $A$; right multiplication swapped the two *columns*.
The two operations are different, which is another instance of non-commutativity: $E$ acting on one side
is not the same as $E$ acting on the other.

### Solution 11

For a diagonal matrix, powers act entrywise:
$$D^3=\begin{pmatrix}2^3&0\\0&3^3\end{pmatrix}=\begin{pmatrix}8&0\\0&27\end{pmatrix},\qquad
D^0=I_2=\begin{pmatrix}1&0\\0&1\end{pmatrix},\qquad
D^{-1}=\begin{pmatrix}1/2&0\\0&1/3\end{pmatrix}.$$
Verification: $DD^{-1}=\begin{pmatrix}2\cdot\frac12&0\\0&3\cdot\frac13\end{pmatrix}=I$. $\checkmark$
A diagonal matrix is invertible exactly when no diagonal entry is zero; here both are non-zero.

### Solution 12

$$A^2=\begin{pmatrix}1&2\\0&1\end{pmatrix}\begin{pmatrix}1&2\\0&1\end{pmatrix}
=\begin{pmatrix}1&4\\0&1\end{pmatrix},\qquad
A^3=A^2A=\begin{pmatrix}1&4\\0&1\end{pmatrix}\begin{pmatrix}1&2\\0&1\end{pmatrix}
=\begin{pmatrix}1&6\\0&1\end{pmatrix}.$$
The pattern is $A^n=\begin{pmatrix}1&2n\\0&1\end{pmatrix}$. It holds for $n=1$. If it holds for $n$, then
$$A^{n+1}=A^nA=\begin{pmatrix}1&2n\\0&1\end{pmatrix}\begin{pmatrix}1&2\\0&1\end{pmatrix}
=\begin{pmatrix}1&2n+2\\0&1\end{pmatrix}=\begin{pmatrix}1&2(n+1)\\0&1\end{pmatrix},$$
so it holds for $n+1$ and hence for all $n\ge1$ by induction.

## Intermediate

### Solution 13

Here $a=3$, $b=5$, $c=1$, $d=2$, so $\Delta=6-5=1$ and
$$A^{-1}=\frac11\begin{pmatrix}2&-5\\-1&3\end{pmatrix}=\begin{pmatrix}2&-5\\-1&3\end{pmatrix}.$$
Verify both orders:
$$AA^{-1}=\begin{pmatrix}3\cdot2+5\cdot(-1) & 3\cdot(-5)+5\cdot3\\1\cdot2+2\cdot(-1) & 1\cdot(-5)+2\cdot3\end{pmatrix}
=\begin{pmatrix}1&0\\0&1\end{pmatrix},$$
$$A^{-1}A=\begin{pmatrix}2\cdot3+(-5)\cdot1 & 2\cdot5+(-5)\cdot2\\(-1)\cdot3+3\cdot1 & (-1)\cdot5+3\cdot2\end{pmatrix}
=\begin{pmatrix}1&0\\0&1\end{pmatrix}.$$
Both products are $I$, as required.

### Solution 14

Row-reduce $(A\mid I)$:

$$\left(\begin{array}{ccc|ccc}
1&2&3&1&0&0\\0&1&4&0&1&0\\5&6&0&0&0&1
\end{array}\right)
\xrightarrow{R_3-5R_1}
\left(\begin{array}{ccc|ccc}
1&2&3&1&0&0\\0&1&4&0&1&0\\0&-4&-15&-5&0&1
\end{array}\right)$$
$$\xrightarrow{R_3+4R_2}
\left(\begin{array}{ccc|ccc}
1&2&3&1&0&0\\0&1&4&0&1&0\\0&0&1&-5&4&1
\end{array}\right)
\xrightarrow[R_2-4R_3]{R_1-3R_3}
\left(\begin{array}{ccc|ccc}
1&2&0&16&-12&-3\\0&1&0&20&-15&-4\\0&0&1&-5&4&1
\end{array}\right)$$
$$\xrightarrow{R_1-2R_2}
\left(\begin{array}{ccc|ccc}
1&0&0&-24&18&5\\0&1&0&20&-15&-4\\0&0&1&-5&4&1
\end{array}\right).$$

So $A^{-1}=\begin{pmatrix}-24&18&5\\20&-15&-4\\-5&4&1\end{pmatrix}$. Verify $AA^{-1}$ entry by entry:

$$\begin{aligned}
\text{row 1}&:\ (-24+40-15,\ 18-30+12,\ 5-8+3)=(1,0,0),\\
\text{row 2}&:\ (0+20-20,\ 0-15+16,\ 0-4+4)=(0,1,0),\\
\text{row 3}&:\ (-120+120+0,\ 90-90+0,\ 25-24+0)=(0,0,1).
\end{aligned}$$

Hence $AA^{-1}=I$. $\checkmark$

### Solution 15

Using the inverse from Exercise 14, with $\mathbf{b}=(1,2,3)$,
$$\mathbf{x}=A^{-1}\mathbf{b}=
\begin{pmatrix}-24\cdot1+18\cdot2+5\cdot3\\20\cdot1-15\cdot2-4\cdot3\\-5\cdot1+4\cdot2+1\cdot3\end{pmatrix}
=\begin{pmatrix}-24+36+15\\20-30-12\\-5+8+3\end{pmatrix}
=\begin{pmatrix}27\\-22\\6\end{pmatrix}.$$
Verification in all three equations:
$$27+2(-22)+3(6)=27-44+18=1,$$
$$(-22)+4(6)=-22+24=2,$$
$$5(27)+6(-22)=135-132=3.$$
All three hold, so $(x,y,z)=(27,-22,6)$. $\checkmark$

### Solution 16

$A$ is $3\times2$, so $A^{\mathsf{T}}$ is $2\times3$ and $A^{\mathsf{T}}A$ is $2\times2$:
$$A^{\mathsf{T}}A=\begin{pmatrix}1&3&5\\2&4&6\end{pmatrix}\begin{pmatrix}1&2\\3&4\\5&6\end{pmatrix}
=\begin{pmatrix}1+9+25 & 2+12+30\\2+12+30 & 4+16+36\end{pmatrix}
=\begin{pmatrix}35&44\\44&56\end{pmatrix}.$$
Also $AA^{\mathsf{T}}$ is $3\times3$:
$$AA^{\mathsf{T}}=\begin{pmatrix}1&2\\3&4\\5&6\end{pmatrix}\begin{pmatrix}1&3&5\\2&4&6\end{pmatrix}
=\begin{pmatrix}1+4&3+8&5+12\\3+8&9+16&15+24\\5+12&15+24&25+36\end{pmatrix}
=\begin{pmatrix}5&11&17\\11&25&39\\17&39&61\end{pmatrix}.$$
Both are symmetric: the $(1,2)$ and $(2,1)$ entries agree, and likewise for the other pairs. This is the
remark after Proposition 7.8: $A^{\mathsf{T}}A$ and $AA^{\mathsf{T}}$ are always symmetric, whatever the
shape of $A$.

### Solution 17

Write $A=\begin{pmatrix}P&Q\\0&R\end{pmatrix}$ and $B=\begin{pmatrix}S&0\\T&I\end{pmatrix}$ with
$$P=I_2,\quad Q=\begin{pmatrix}2&1\\1&0\end{pmatrix},\quad R=\begin{pmatrix}1&2\\0&1\end{pmatrix},\quad
S=\begin{pmatrix}1&1\\0&1\end{pmatrix},\quad T=I_2.$$
Then
$$AB=\begin{pmatrix}PS+QT & Q\\RT & R\end{pmatrix}.$$
Compute
$$PS+QT=S+Q=\begin{pmatrix}1&1\\0&1\end{pmatrix}+\begin{pmatrix}2&1\\1&0\end{pmatrix}
=\begin{pmatrix}3&2\\1&1\end{pmatrix},$$
and $RT=R=\begin{pmatrix}1&2\\0&1\end{pmatrix}$. Hence
$$AB=\begin{pmatrix}3&2&2&1\\1&1&1&0\\1&2&1&2\\0&1&0&1\end{pmatrix}.$$
Check row 1 of $A$, which is $(1,0,2,1)$, against the columns of $B$: column 1 is $(1,0,1,0)$, giving
$1+0+2+0=3$; column 2 is $(1,1,0,1)$, giving $1+0+0+1=2$; column 3 is $(0,0,1,0)$, giving $2$; column 4 is
$(0,0,0,1)$, giving $1$. So the first row is $(3,2,2,1)$, as computed. $\checkmark$

### Solution 18

$$A+B=\begin{pmatrix}1&3\\4&4\end{pmatrix},\qquad \operatorname{tr}(A+B)=1+4=5.$$
$$\operatorname{tr}A+\operatorname{tr}B=(1+4)+(0+0)=5,$$
so the trace is additive. Next
$$AB=\begin{pmatrix}1\cdot0+2\cdot1 & 1\cdot1+2\cdot0\\3\cdot0+4\cdot1 & 3\cdot1+4\cdot0\end{pmatrix}
=\begin{pmatrix}2&1\\4&3\end{pmatrix},\qquad \operatorname{tr}(AB)=2+3=5,$$
$$BA=\begin{pmatrix}0\cdot1+1\cdot3 & 0\cdot2+1\cdot4\\1\cdot1+0\cdot3 & 1\cdot2+0\cdot4\end{pmatrix}
=\begin{pmatrix}3&4\\1&2\end{pmatrix},\qquad \operatorname{tr}(BA)=3+2=5.$$
But $\operatorname{tr}A\cdot\operatorname{tr}B=5\cdot0=0\ne5$. So the trace is additive and cyclic, but not
multiplicative: $\operatorname{tr}(AB)\ne\operatorname{tr}A\cdot\operatorname{tr}B$ in general.

### Solution 19

For $n=1$ the formula reads $A^1=\begin{pmatrix}2&1\\0&2\end{pmatrix}$, which is true. Suppose
$A^n=\begin{pmatrix}2^n&n2^{n-1}\\0&2^n\end{pmatrix}$. Then
$$A^{n+1}=A^nA=\begin{pmatrix}2^n&n2^{n-1}\\0&2^n\end{pmatrix}\begin{pmatrix}2&1\\0&2\end{pmatrix}
=\begin{pmatrix}2^{n+1} & 2^n+2n2^{n-1}\\0&2^{n+1}\end{pmatrix}
=\begin{pmatrix}2^{n+1}&(n+1)2^n\\0&2^{n+1}\end{pmatrix},$$
since $2^n+2n2^{n-1}=2^n(1+n)=2^n(n+1)$. This is the formula for $n+1$, so by induction it holds for all
$n\ge1$. At $n=4$: $A^4=\begin{pmatrix}16&4\cdot8\\0&16\end{pmatrix}=\begin{pmatrix}16&32\\0&16\end{pmatrix}$,
and indeed $A^2=\begin{pmatrix}4&4\\0&4\end{pmatrix}$, so $A^4=A^2A^2=\begin{pmatrix}16&32\\0&16\end{pmatrix}$.

### Solution 20

First $A^2=\begin{pmatrix}1&2\\0&1\end{pmatrix}$, $B^2=\begin{pmatrix}1&0\\2&1\end{pmatrix}$,
$AB=\begin{pmatrix}2&1\\1&1\end{pmatrix}$, $BA=\begin{pmatrix}1&1\\1&2\end{pmatrix}$ and
$A+B=\begin{pmatrix}2&1\\1&2\end{pmatrix}$, so
$$(A+B)^2=\begin{pmatrix}2&1\\1&2\end{pmatrix}^2
=\begin{pmatrix}4+1&2+2\\2+2&1+4\end{pmatrix}=\begin{pmatrix}5&4\\4&5\end{pmatrix}.$$
Next
$$A^2+2AB+B^2=\begin{pmatrix}1&2\\0&1\end{pmatrix}+\begin{pmatrix}4&2\\2&2\end{pmatrix}+\begin{pmatrix}1&0\\2&1\end{pmatrix}
=\begin{pmatrix}6&4\\4&4\end{pmatrix}\ne\begin{pmatrix}5&4\\4&5\end{pmatrix}.$$
The correct expansion is
$$A^2+AB+BA+B^2=\begin{pmatrix}1&2\\0&1\end{pmatrix}+\begin{pmatrix}2&1\\1&1\end{pmatrix}+\begin{pmatrix}1&1\\1&2\end{pmatrix}+\begin{pmatrix}1&0\\2&1\end{pmatrix}
=\begin{pmatrix}5&4\\4&5\end{pmatrix},$$
which agrees with $(A+B)^2$. The shortcut $2AB$ is legitimate only when $AB=BA$; here $AB\ne BA$.

### Solution 21

Let $X=\begin{pmatrix}a&b\\c&d\end{pmatrix}$. Compute
$$XA=\begin{pmatrix}a&b\\c&d\end{pmatrix}\begin{pmatrix}1&1\\0&1\end{pmatrix}
=\begin{pmatrix}a&a+b\\c&c+d\end{pmatrix},\qquad
AX=\begin{pmatrix}1&1\\0&1\end{pmatrix}\begin{pmatrix}a&b\\c&d\end{pmatrix}
=\begin{pmatrix}a+c&b+d\\c&d\end{pmatrix}.$$
Equating entries: $a=a+c$ gives $c=0$; $a+b=b+d$ gives $a=d$; the remaining equations $c=c$ and $c+d=d$
give $c=0$ again. So $X=\begin{pmatrix}a&b\\0&a\end{pmatrix}$ with arbitrary $a,b$.

Check that every such matrix commutes:
$$\begin{pmatrix}a&b\\0&a\end{pmatrix}\begin{pmatrix}1&1\\0&1\end{pmatrix}
=\begin{pmatrix}a&a+b\\0&a\end{pmatrix}
=\begin{pmatrix}1&1\\0&1\end{pmatrix}\begin{pmatrix}a&b\\0&a\end{pmatrix}. \checkmark$$
These are exactly the matrices of the form $aI+b(A-I)$; the family is two-dimensional, not just the
multiples of $I$.

### Solution 22

Row by column:
$$A^2=\begin{pmatrix}0&1&1\\1&0&1\\1&1&0\end{pmatrix}^2
=\begin{pmatrix}0+1+1 & 0+0+1 & 0+1+0\\0+0+1 & 1+0+1 & 1+0+0\\0+1+0 & 0+0+1 & 1+1+0\end{pmatrix}
=\begin{pmatrix}2&1&1\\1&2&1\\1&1&2\end{pmatrix}.$$
The $(i,i)$ entry is $2$ for every vertex, because from each vertex there are exactly two two-step walks
returning to it (go to one of the other two vertices and back). The off-diagonal entries are $1$: there is
exactly one two-step walk between distinct vertices, through the third vertex. Interpreted generally,
$(A^2)_{ii}$ equals the degree of vertex $i$ (here $2$ for all).

## Advanced

### Solution 23

Let $A$ be $m\times n$ and $B$ be $n\times p$. For any indices $i\in\{1,\dots,p\}$ and
$j\in\{1,\dots,m\}$,

$$((AB)^{\mathsf{T}})_{ij}=(AB)_{ji}=\sum_{k=1}^{n}a_{jk}b_{ki}.$$

On the other hand, $(B^{\mathsf{T}})_{ik}=b_{ki}$ and $(A^{\mathsf{T}})_{kj}=a_{jk}$, so

$$(B^{\mathsf{T}}A^{\mathsf{T}})_{ij}=\sum_{k=1}^{n}(B^{\mathsf{T}})_{ik}(A^{\mathsf{T}})_{kj}
=\sum_{k=1}^{n}b_{ki}a_{jk}.$$

The two sums are equal term by term, since multiplication of real numbers is commutative. Hence the
matrices have equal entries in every position, so they are equal. Note the shapes: $(AB)^{\mathsf{T}}$ is
$p\times m$ and $B^{\mathsf{T}}A^{\mathsf{T}}$ is $(p\times n)(n\times m)=p\times m$, as required.

### Solution 24

For square $n\times n$ matrices,
$$\operatorname{tr}(AB)=\sum_{i=1}^{n}(AB)_{ii}=\sum_{i=1}^{n}\sum_{k=1}^{n}a_{ik}b_{ki}
=\sum_{k=1}^{n}\sum_{i=1}^{n}b_{ki}a_{ik}=\sum_{k=1}^{n}(BA)_{kk}=\operatorname{tr}(BA),$$
where the third equality interchanges the order of the finite sums (valid because the index set is finite).
For the cyclic version, apply the identity to the pair $A$ and $BC$:
$\operatorname{tr}(A(BC))=\operatorname{tr}((BC)A)=\operatorname{tr}(BCA)$.

For the counterexample, take $A=\begin{pmatrix}1&2\\3&4\end{pmatrix}$ and
$B=\begin{pmatrix}0&1\\1&0\end{pmatrix}$. Then
$AB=\begin{pmatrix}2&1\\4&3\end{pmatrix}$, so $\operatorname{tr}(AB)=5$, while
$\operatorname{tr}A\cdot\operatorname{tr}B=5\cdot0=0$. The trace is additive and cyclic, not
multiplicative.

### Solution 25

Let $A$ be $m\times n$, $B$ be $n\times p$, $C$ be $p\times q$. For each $i,j$,

$$\begin{aligned}
\bigl((AB)C\bigr)_{ij}
&=\sum_{l=1}^{p}(AB)_{il}c_{lj}
=\sum_{l=1}^{p}\Bigl(\sum_{k=1}^{n}a_{ik}b_{kl}\Bigr)c_{lj}\\
&=\sum_{k=1}^{n}a_{ik}\Bigl(\sum_{l=1}^{p}b_{kl}c_{lj}\Bigr)
=\sum_{k=1}^{n}a_{ik}(BC)_{kj}=\bigl(A(BC)\bigr)_{ij}.
\end{aligned}$$

The properties used are: distributivity of multiplication over addition in $\mathbb{R}$ (to move $c_{lj}$
inside the inner sum), associativity of multiplication in $\mathbb{R}$ (to write $a_{ik}b_{kl}c_{lj}$),
and the fact that a finite double sum may be summed in either order. Since all entries agree,
$(AB)C=A(BC)$.

### Solution 26

**Uniqueness.** Suppose $B$ and $C$ both satisfy $AB=BA=I$ and $AC=CA=I$. Then
$$B=BI=B(AC)=(BA)C=IC=C,$$
using associativity and the two inverse properties. So there is at most one inverse.

**Product.** Let $A,B$ be invertible. Then
$$(AB)(B^{-1}A^{-1})=A(BB^{-1})A^{-1}=AA^{-1}=I,\qquad
(B^{-1}A^{-1})(AB)=B^{-1}(A^{-1}A)B=B^{-1}B=I,$$
so $B^{-1}A^{-1}$ is an inverse of $AB$; by uniqueness it is *the* inverse.

**Double inverse.** $A^{-1}A=I$ and $AA^{-1}=I$ say precisely that $A$ is an inverse of $A^{-1}$; by
uniqueness, $(A^{-1})^{-1}=A$.

### Solution 27

**Zero row.** Suppose row $i$ of $A$ is entirely zero. For any matrix $B$, the $i$-th row of $AB$ is
$\sum_k a_{ik}(\text{row }k\text{ of }B)=\mathbf{0}$, because every $a_{ik}=0$. But row $i$ of $I$ is
$\mathbf{e}_i^{\mathsf{T}}\ne\mathbf{0}$. So $AB$ cannot equal $I$ for any $B$, and $A$ is not invertible.

**Equal rows.** Suppose rows $i$ and $j$ of $A$ are equal, with $i\ne j$. Then rows $i$ and $j$ of $AB$ are
equal for every $B$, since row $i$ of $AB$ is (row $i$ of $A$) times $B$. But rows $i$ and $j$ of $I$ are
$\mathbf{e}_i^{\mathsf{T}}$ and $\mathbf{e}_j^{\mathsf{T}}$, which are different. Hence $AB\ne I$ for every
$B$, so $A$ is not invertible. This is the algebraic form of "information has been duplicated, so it cannot
be recovered".

### Solution 28

**The inverse.** Let $\Delta=ad-bc\ne0$ and $B=\frac{1}{\Delta}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}$. Then
$$AB=\frac{1}{\Delta}\begin{pmatrix}a&b\\c&d\end{pmatrix}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}
=\frac{1}{\Delta}\begin{pmatrix}ad-bc&-ab+ab\\cd-dc&-bc+ad\end{pmatrix}
=\frac{1}{\Delta}\begin{pmatrix}\Delta&0\\0&\Delta\end{pmatrix}=I,$$
$$BA=\frac{1}{\Delta}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}\begin{pmatrix}a&b\\c&d\end{pmatrix}
=\frac{1}{\Delta}\begin{pmatrix}da-bc&db-bd\\-ca+ac&-cb+ad\end{pmatrix}=I.$$
So $B$ is the inverse.

**No inverse when $\Delta=0$.** Suppose $\Delta=0$ and an inverse existed. If $(c,d)\ne(0,0)$, put
$\mathbf{v}=(d,-c)\ne\mathbf{0}$; then
$$A\mathbf{v}=\begin{pmatrix}ad-bc\\cd-dc\end{pmatrix}=\begin{pmatrix}0\\0\end{pmatrix}.$$
Applying the inverse would give $\mathbf{v}=A^{-1}\mathbf{0}=\mathbf{0}$, a contradiction. If
$(c,d)=(0,0)$ and $(a,b)\ne(0,0)$, the same argument with $\mathbf{v}=(b,-a)$ applies, since
$A\mathbf{v}=(ab-ba,0)=\mathbf{0}$. If all entries are zero, $AB=0\ne I$ for every $B$. Hence no inverse
exists in any of the cases.

### Solution 29

**Swap.** Let $E_{ij}$ swap rows $i$ and $j$ of $I$. Applying the swap twice restores the original matrix,
and matrix multiplication represents composition, so $E_{ij}E_{ij}=I$; hence $E_{ij}^{-1}=E_{ij}$.

**Scaling.** Let $D_i(c)$ have $c\ne0$ in position $(i,i)$ and $1$ elsewhere on the diagonal. Then
$D_i(c)D_i(1/c)=D_i(1)$: multiplying the $i$-th row by $c$ and then by $1/c$ restores it, and the other
rows are untouched. So $D_i(c)^{-1}=D_i(1/c)$.

**Row addition.** Let $T=T_{ij}(c)=I+c\mathbf{e}_i\mathbf{e}_j^{\mathsf{T}}$ with $i\ne j$. Since
$\mathbf{e}_j^{\mathsf{T}}\mathbf{e}_i=0$,
$$(c\mathbf{e}_i\mathbf{e}_j^{\mathsf{T}})^2=c^2\mathbf{e}_i(\mathbf{e}_j^{\mathsf{T}}\mathbf{e}_i)\mathbf{e}_j^{\mathsf{T}}=\mathbf{0}.$$
Hence
$$(I+c\mathbf{e}_i\mathbf{e}_j^{\mathsf{T}})(I-c\mathbf{e}_i\mathbf{e}_j^{\mathsf{T}})
=I-c^2\mathbf{e}_i\mathbf{e}_j^{\mathsf{T}}\mathbf{e}_i\mathbf{e}_j^{\mathsf{T}}=I,$$
and the same computation in the other order gives $I$ as well. Therefore
$T_{ij}(c)^{-1}=T_{ij}(-c)$.

### Solution 30

For $n=1$, $\begin{pmatrix}F_2&F_1\\F_1&F_0\end{pmatrix}=\begin{pmatrix}1&1\\1&0\end{pmatrix}=M$. Suppose
$M^n=\begin{pmatrix}F_{n+1}&F_n\\F_n&F_{n-1}\end{pmatrix}$. Then
$$M^{n+1}=M^nM=\begin{pmatrix}F_{n+1}&F_n\\F_n&F_{n-1}\end{pmatrix}\begin{pmatrix}1&1\\1&0\end{pmatrix}
=\begin{pmatrix}F_{n+1}+F_n & F_{n+1}\\F_n+F_{n-1} & F_n\end{pmatrix}
=\begin{pmatrix}F_{n+2}&F_{n+1}\\F_{n+1}&F_n\end{pmatrix},$$
using $F_{n+2}=F_{n+1}+F_n$ and $F_{n+1}=F_n+F_{n-1}$. This is the formula for $n+1$, so by induction it
holds for all $n\ge1$.

At $n=9$: $M^9=\begin{pmatrix}F_{10}&F_9\\F_9&F_8\end{pmatrix}=\begin{pmatrix}55&34\\34&21\end{pmatrix}$.
Check by one more multiplication: $M^5=\begin{pmatrix}8&5\\5&3\end{pmatrix}$ and
$M^6=\begin{pmatrix}13&8\\8&5\end{pmatrix}$, continuing to
$M^7=\begin{pmatrix}21&13\\13&8\end{pmatrix}$, $M^8=\begin{pmatrix}34&21\\21&13\end{pmatrix}$,
$M^9=\begin{pmatrix}55&34\\34&21\end{pmatrix}$. $\checkmark$

## Challenge

### Solution 31

$$A^2=\begin{pmatrix}0&1&0\\0&0&1\\0&0&0\end{pmatrix}^2
=\begin{pmatrix}0&0&1\\0&0&0\\0&0&0\end{pmatrix},\qquad
A^3=A^2A=\mathbf{0}.$$

Then
$$(I-A)(I+A+A^2)=I+A+A^2-A-A^2-A^3=I-A^3=I,$$
and the same expansion in the other order gives $I$ as well (the factors $A^k$ commute with each other and
with $I$). Hence $(I-A)^{-1}=I+A+A^2$.

Explicitly,
$$I-A=\begin{pmatrix}1&-1&0\\0&1&-1\\0&0&1\end{pmatrix},\qquad
I+A+A^2=\begin{pmatrix}1&1&1\\0&1&1\\0&0&1\end{pmatrix},$$
and their product is
$$\begin{pmatrix}
1\cdot1+(-1)\cdot0+0\cdot0 & 1\cdot1+(-1)\cdot1+0\cdot0 & 1\cdot1+(-1)\cdot1+0\cdot1\\
0+1\cdot0+(-1)\cdot0 & 0+1\cdot1+(-1)\cdot0 & 0+1\cdot1+(-1)\cdot1\\
0&0&1
\end{pmatrix}
=\begin{pmatrix}1&0&0\\0&1&0\\0&0&1\end{pmatrix}.$$
So the inverse is verified. $\checkmark$

### Solution 32

Write $A=\begin{pmatrix}a&b\\c&d\end{pmatrix}$ and $B=\begin{pmatrix}p&q\\r&s\end{pmatrix}$. The condition
$AB=I$ is the four equations
$$ap+br=1,\qquad aq+bs=0,\qquad cp+dr=0,\qquad cq+ds=1.$$

First show $\Delta=ad-bc\ne0$. Multiply the first equation by $d$ and the third by $b$, then subtract:
$$(ad-bc)p=d.$$
If $\Delta=0$ then $d=0$. Multiplying the second by $d$ and the fourth by $b$ and subtracting gives
$(ad-bc)q=-b$, so $b=0$. Similarly, multiplying the first by $c$ and the third by $a$ gives
$(ad-bc)r=-c$, so $c=0$, and the second/fourth combination gives $(ad-bc)s=a$, so $a=0$. Then $A=0$, and
$AB=0\ne I$, a contradiction. Hence $\Delta\ne0$.

Dividing the four derived equations by $\Delta$ gives
$$p=\frac{d}{\Delta},\qquad q=-\frac{b}{\Delta},\qquad r=-\frac{c}{\Delta},\qquad s=\frac{a}{\Delta},$$
so $B=\frac{1}{\Delta}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}$, which is the $2\times2$ inverse of $A$. Then
$$BA=\frac{1}{\Delta}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}\begin{pmatrix}a&b\\c&d\end{pmatrix}
=\frac{1}{\Delta}\begin{pmatrix}da-bc&db-bd\\-ca+ac&-cb+ad\end{pmatrix}=I,$$
as claimed. So a one-sided inverse of a $2\times2$ matrix is two-sided.

### Solution 33

Multiply the two block matrices:
$$\begin{pmatrix}A&B\\0&D\end{pmatrix}\begin{pmatrix}A^{-1}&-A^{-1}BD^{-1}\\0&D^{-1}\end{pmatrix}
=\begin{pmatrix}AA^{-1}+B\cdot0 & A(-A^{-1}BD^{-1})+BD^{-1}\\0\cdot A^{-1}+D\cdot0 & 0\cdot(-A^{-1}BD^{-1})+DD^{-1}\end{pmatrix}.$$
Each block simplifies: $AA^{-1}=I$, the upper-right block is $-BD^{-1}+BD^{-1}=0$, the lower-left is $0$,
and the lower-right is $DD^{-1}=I$. Hence the product is $\begin{pmatrix}I&0\\0&I\end{pmatrix}=I$. The same
computation in the other order gives $I$ as well, since
$\begin{pmatrix}A^{-1}&-A^{-1}BD^{-1}\\0&D^{-1}\end{pmatrix}\begin{pmatrix}A&B\\0&D\end{pmatrix}$
has upper-right block $A^{-1}B-A^{-1}BD^{-1}D=0$.

**Application.** For $M=\begin{pmatrix}A&B\\0&D\end{pmatrix}$ with $A=\begin{pmatrix}1&2\\0&1\end{pmatrix}$,
$D=\begin{pmatrix}2&1\\0&1\end{pmatrix}$ and $B=I_2$,
$$A^{-1}=\begin{pmatrix}1&-2\\0&1\end{pmatrix},\qquad D^{-1}=\begin{pmatrix}1/2&-1/2\\0&1\end{pmatrix},$$
$$-A^{-1}BD^{-1}=-A^{-1}D^{-1}=-\begin{pmatrix}1/2&-5/2\\0&1\end{pmatrix}
=\begin{pmatrix}-1/2&5/2\\0&-1\end{pmatrix},$$
where
$$A^{-1}D^{-1}=\begin{pmatrix}1&-2\\0&1\end{pmatrix}\begin{pmatrix}1/2&-1/2\\0&1\end{pmatrix}
=\begin{pmatrix}1/2&-1/2-2\\0&1\end{pmatrix}
=\begin{pmatrix}1/2&-5/2\\0&1\end{pmatrix}.$$
Hence
$$M^{-1}=\begin{pmatrix}1&-2&-1/2&5/2\\0&1&0&-1\\0&0&1/2&-1/2\\0&0&0&1\end{pmatrix}.$$
Verify row 1 of $M$, which is $(1,2,1,0)$, against the columns of $M^{-1}$: column 1 gives $1$, column 2
gives $-2+2=0$, column 3 gives $-1/2+0+1/2+0=0$, column 4 gives $5/2-2-1/2+0=0$. So the first row of
$MM^{-1}$ is $(1,0,0,0)$, as required. $\checkmark$

### Solution 34

**Induction.** For $k=1$, $(A^1)_{ij}=a_{ij}$ is $1$ exactly when there is an edge $i\to j$, which is a walk
of length $1$. Suppose the statement holds for $k$. A walk of length $k+1$ from $i$ to $j$ consists of a
walk of length $k$ from $i$ to some vertex $m$, followed by an edge $m\to j$. Therefore the number of such
walks is
$$\sum_{m}(A^k)_{im}a_{mj}=(A^kA)_{ij}=(A^{k+1})_{ij}.$$
So the statement holds for $k+1$, hence for all $k\ge1$ by induction.

**Application.** For the triangle graph, multiply $A$ by $A^2$:
$$A^3=A\cdot A^2=\begin{pmatrix}0&1&1\\1&0&1\\1&1&0\end{pmatrix}
\begin{pmatrix}2&1&1\\1&2&1\\1&1&2\end{pmatrix}.$$
Row 1, $(0,1,1)$: against $(2,1,1)$ gives $0+1+1=2$; against $(1,2,1)$ gives $0+2+1=3$; against $(1,1,2)$
gives $0+1+2=3$. Row 2, $(1,0,1)$: $2+0+1=3$, $1+0+1=2$, $1+0+2=3$. Row 3, $(1,1,0)$: $2+1+0=3$,
$1+2+0=3$, $1+1+0=2$. Hence
$$A^3=\begin{pmatrix}2&3&3\\3&2&3\\3&3&2\end{pmatrix}.$$

The total number of three-step walks from vertex $1$ is the sum of the first row, $2+3+3=8$. Direct count:
the first step goes to either $2$ or $3$ (2 choices), and at each of the remaining two steps there are 2
choices because the graph is complete, giving $2\cdot2\cdot2=8$. $\checkmark$

### Solution 35

Write $A=\begin{pmatrix}a&b\\c&d\end{pmatrix}$. Then
$$A^2=\begin{pmatrix}a^2+bc&ab+bd\\ac+cd&bc+d^2\end{pmatrix},\qquad
(\operatorname{tr}A)A=(a+d)\begin{pmatrix}a&b\\c&d\end{pmatrix}
=\begin{pmatrix}a^2+ad&ab+bd\\ac+cd&ad+d^2\end{pmatrix}.$$
Subtracting,
$$A^2-(\operatorname{tr}A)A=\begin{pmatrix}bc-ad&0\\0&bc-ad\end{pmatrix}=-(\det A)I.$$
Hence $A^2-(\operatorname{tr}A)A+(\det A)I=0$, the Cayley–Hamilton identity for $2\times2$ matrices.

**Inverse formula.** If $\det A\ne0$, rearrange:
$A^2-(\operatorname{tr}A)A=-(\det A)I$, so
$$A\bigl((\operatorname{tr}A)I-A\bigr)=(\det A)I,\qquad
A\cdot\frac{(\operatorname{tr}A)I-A}{\det A}=I,$$
and the same product in the other order is also $I$ because the expression is a polynomial in $A$. Hence
$A^{-1}=\frac{1}{\det A}((\operatorname{tr}A)I-A)$.

**Application.** For $A=\begin{pmatrix}3&1\\2&4\end{pmatrix}$: $\operatorname{tr}A=7$,
$\det A=12-2=10$,
$$A^2=\begin{pmatrix}3&1\\2&4\end{pmatrix}^2=\begin{pmatrix}9+2&3+4\\6+8&2+16\end{pmatrix}
=\begin{pmatrix}11&7\\14&18\end{pmatrix},$$
and
$$A^2-7A+10I=\begin{pmatrix}11&7\\14&18\end{pmatrix}-\begin{pmatrix}21&7\\14&28\end{pmatrix}
+\begin{pmatrix}10&0\\0&10\end{pmatrix}=\begin{pmatrix}0&0\\0&0\end{pmatrix}.$$
Finally
$$A^{-1}=\frac{1}{10}\left(7I-A\right)=\frac{1}{10}\begin{pmatrix}4&-1\\-2&3\end{pmatrix},$$
and indeed
$$AA^{-1}=\frac{1}{10}\begin{pmatrix}12-2&-3+3\\8-8&-2+12\end{pmatrix}
=\frac{1}{10}\begin{pmatrix}10&0\\0&10\end{pmatrix}=I.$$
This agrees with the $2\times2$ formula $\frac{1}{ad-bc}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}$.

### Solution 36

Use homogeneous coordinates $(x,y,1)$. Rotation about $(-1,2)$ is
$M=T\,R\,T^{-1}$ with
$$T=\begin{pmatrix}1&0&-1\\0&1&2\\0&0&1\end{pmatrix},\quad
R=\begin{pmatrix}0&-1&0\\1&0&0\\0&0&1\end{pmatrix},\quad
T^{-1}=\begin{pmatrix}1&0&1\\0&1&-2\\0&0&1\end{pmatrix}.$$
First
$$RT^{-1}=\begin{pmatrix}0&-1&0\\1&0&0\\0&0&1\end{pmatrix}\begin{pmatrix}1&0&1\\0&1&-2\\0&0&1\end{pmatrix}
=\begin{pmatrix}0&-1&2\\1&0&1\\0&0&1\end{pmatrix},$$
then
$$M=T(RT^{-1})=\begin{pmatrix}1&0&-1\\0&1&2\\0&0&1\end{pmatrix}
\begin{pmatrix}0&-1&2\\1&0&1\\0&0&1\end{pmatrix}
=\begin{pmatrix}0&-1&1\\1&0&3\\0&0&1\end{pmatrix}.$$
Apply it:
$$M\begin{pmatrix}0\\2\\1\end{pmatrix}=\begin{pmatrix}0-2+1\\0+0+3\\1\end{pmatrix}=\begin{pmatrix}-1\\3\\1\end{pmatrix},
\qquad
M\begin{pmatrix}-1\\3\\1\end{pmatrix}=\begin{pmatrix}0-3+1\\-1+0+3\\1\end{pmatrix}=\begin{pmatrix}-2\\2\\1\end{pmatrix}.$$
Check geometrically: $(0,2)$ is $1$ unit to the right of the centre $(-1,2)$; a quarter turn sends that
displacement $(1,0)$ to $(0,1)$, giving $(-1,3)$. Then $(-1,3)$ is $1$ unit above the centre; the turn
sends $(0,1)$ to $(-1,0)$, giving $(-2,2)$. The centre is fixed:
$$M\begin{pmatrix}-1\\2\\1\end{pmatrix}=\begin{pmatrix}0-2+1\\-1+0+3\\1\end{pmatrix}
=\begin{pmatrix}-1\\2\\1\end{pmatrix}. \checkmark$$
