# Linear Transformations — Solutions

> [Tutorial](README.md) · [Exercises](exercises.md)

Every exercise is solved in full: the strategy first, then the algebra, then a check. Proofs are written
out with the theorem each step appeals to. Where a problem admits a second method, the alternative is
noted.

## Beginner

**1.** *(a)* $T$ is linear. Both components are linear polynomials without constant term, so
$T\big((x,y)+(x',y')\big) = T(x+x',\ y+y') = \big(3(x+x') - (y+y'),\ 2(y+y')\big) = T(x,y) + T(x',y')$
and $T(cx,cy) = (3cx - cy,\ 2cy) = cT(x,y)$.

*(b)* $S$ is not linear: $S(1,0) + S(1,0) = (1,0) + (1,0) = (2,0)$, while $S(2,0) = (4,0)$. (The
obstruction is the square; note $S(\mathbf{0}) = \mathbf{0}$ here, so the zero test alone would not
have detected it.)

*(c)* $F$ is not linear: $F(0,0) = (-1,0) \neq (0,0)$.

*(d)* $G$ is not linear: $G(1,1) + G(1,1) = (2,1)+(2,1) = (4,2)$, while $G(2,2) = (8,2)$.

**2.** Let $\mathbf{u} = (x,y)$, $\mathbf{v} = (x',y')$ and $c \in \mathbb{R}$. Then

$$
T(\mathbf{u}+\mathbf{v}) = T(x+x',\ y+y') = \big((x+x') + 2(y+y'),\ 3(x+x') - (y+y')\big),
$$

and collecting terms gives $\big((x+2y) + (x'+2y'),\ (3x-y) + (3x'-y')\big) = T(\mathbf{u})+T(\mathbf{v})$.
Also $T(c\mathbf{u}) = T(cx, cy) = (cx + 2cy,\ 3cx - cy) = c(x+2y,\ 3x-y) = cT(\mathbf{u})$. So $T$ is
linear, and since $T(\mathbf{e}_1) = (1,3)$ and $T(\mathbf{e}_2) = (2,-1)$,

$$
[T] = \begin{pmatrix}1&2\\ 3&-1\end{pmatrix},
\qquad
T(x,y) = \begin{pmatrix}1&2\\ 3&-1\end{pmatrix}\begin{pmatrix}x\\ y\end{pmatrix}.
$$

**3.** The matrix is $\begin{pmatrix}1&-1&0\\ 0&1&-1\end{pmatrix}$, which is already in reduced row
echelon form with pivots in columns $1$ and $2$. The kernel: $x - y = 0$ and $y - z = 0$ give
$x = y = z$, so

$$
\ker T = \operatorname{span}\{(1,1,1)^{\mathsf{T}}\}.
$$

The image is spanned by the columns, $\{(1,0)^{\mathsf{T}}, (-1,1)^{\mathsf{T}}, (0,-1)^{\mathsf{T}}\}$;
the first two are independent and already span $\mathbb{R}^2$, so
$\operatorname{im}T = \mathbb{R}^2$. Check: $\operatorname{rank}T + \operatorname{nullity}T = 2 + 1 = 3
= \dim\mathbb{R}^3$, and $T(1,1,1) = (0,0)$.

**4.** The matrix is $\begin{pmatrix}2&1&0\\ 0&1&-1\\ 1&0&1\end{pmatrix}$, so

$$
T(1,-2,3) = \big(2 - 2 + 0,\ -2 - 3,\ 1 + 0 + 3\big) = (0,\ -5,\ 4).
$$

For the kernel solve $2x + y = 0$, $y - z = 0$, $x + z = 0$. The second gives $y = z$, the third
$x = -z$, and substituting into the first gives $-2z + z = -z = 0$, so $z = 0$ and hence $x = y = 0$:

$$
\ker T = \{\mathbf{0}\}.
$$

By Theorem 7.6, $T$ is injective; as a map $\mathbb{R}^3 \to \mathbb{R}^3$ it is therefore an
isomorphism (Corollary 7.13). *Independent check:* row reducing the matrix produces three pivots, so the
rank is $3$ and the nullity is $3 - 3 = 0$.

**5.** With $\theta = 60^\circ$, $\cos\theta = \tfrac12$ and $\sin\theta = \tfrac{\sqrt3}{2}$, so

$$
R_{60^\circ} = \begin{pmatrix}\tfrac12 & -\tfrac{\sqrt3}{2}\\[2pt] \tfrac{\sqrt3}{2} & \tfrac12\end{pmatrix},
\qquad
R_{60^\circ}\mathbf{e}_1 = \Big(\tfrac12,\ \tfrac{\sqrt3}{2}\Big),\
R_{60^\circ}\mathbf{e}_2 = \Big(-\tfrac{\sqrt3}{2},\ \tfrac12\Big).
$$

*Check:* both images have length $\sqrt{\tfrac14 + \tfrac34} = 1$ and are orthogonal, as the columns of a
rotation must be; the angle between $(1,0)$ and $(\tfrac12,\tfrac{\sqrt3}{2})$ is $60^\circ$.

**6.** Reflection in $y = -x$ sends $(x,y)$ to $(-y,-x)$, so

$$
M = \begin{pmatrix}0&-1\\ -1&0\end{pmatrix},
\qquad
M\begin{pmatrix}2\\ 3\end{pmatrix} = \begin{pmatrix}-3\\ -2\end{pmatrix}.
$$

Then $M^2 = \begin{pmatrix}0&-1\\-1&0\end{pmatrix}\begin{pmatrix}0&-1\\-1&0\end{pmatrix} =
\begin{pmatrix}1&0\\0&1\end{pmatrix}$: reflecting twice restores every vector. *Check:* $(-3,-2)$ lies on
$y = -x$? It lies on $y = \tfrac23 x$, not on the mirror line; the midpoint of $(2,3)$ and $(-3,-2)$ is
$(-\tfrac12,\tfrac12)$, which does lie on $y = -x$, and the segment joining them is perpendicular to that
line (direction $(5,5)$ against line direction $(1,-1)$, dot product $0$). Both facts confirm a
reflection.

**7.** Projection onto the $y$-axis sends $(x,y)$ to $(0,y)$, so $P = \begin{pmatrix}0&0\\0&1\end{pmatrix}$.
Its kernel is $\{(x,0)\} = \operatorname{span}\{(1,0)\}$, the $x$-axis; its image is
$\operatorname{span}\{(0,1)\}$, the $y$-axis. Finally
$P^2 = \begin{pmatrix}0&0\\0&1\end{pmatrix}\begin{pmatrix}0&0\\0&1\end{pmatrix} = P$. Rank–nullity reads
$1 + 1 = 2$. Every vector splits as $(x,y) = (x,0) + (0,y)$, kernel part plus image part, which is
Proposition 8.3 in action.

**8.** The matrix is $\begin{pmatrix}1&3\\0&1\end{pmatrix}$. The unit square has vertices
$(0,0), (1,0), (1,1), (0,1)$, and they map to
$(0,0),\ (1,0),\ (1+3,\ 1) = (4,1),\ (3,1)$: a parallelogram of base $1$ and height $1$, hence of area
$1$, the same as the square. The kernel is trivial, since $(x + 3y,\ y) = (0,0)$ forces $y = 0$ and then
$x = 0$; the shear is injective and, being square, an isomorphism.

**9.** The columns of the matrix are the images of the standard basis vectors, so
$[T] = \begin{pmatrix}2&3\\ -1&4\end{pmatrix}$, and
$T(2,5) = 2T(\mathbf{e}_1) + 5T(\mathbf{e}_2) = 2(2,-1) + 5(3,4) = (4+15,\ -2+20) = (19,18)$.
*Check with the matrix:* $\begin{pmatrix}2&3\\-1&4\end{pmatrix}\begin{pmatrix}2\\5\end{pmatrix} =
(4+15,\ -2+20)^{\mathsf{T}} = (19,18)^{\mathsf{T}}$.

**10.** $D(1) = 0$, $D(x) = 1$, $D(x^2) = 2x$, so

$$
[D] = \begin{pmatrix}0&1&0\\ 0&0&2\\ 0&0&0\end{pmatrix}.
$$

For $p = 3 - 2x + x^2$ the coordinate column is $(3,-2,1)^{\mathsf{T}}$, and
$[Dp] = [D]\left(3,-2,1\right)^{\mathsf{T}} = (-2,\ 2,\ 0)^{\mathsf{T}}$, that is $p' = -2 + 2x$. The kernel is
$\operatorname{span}\{1\}$ (the constants) and the image is $\operatorname{span}\{1,x\}$ (all polynomials
of degree $\le 1$). Rank–nullity: $2 + 1 = 3 = \dim\mathcal{P}_2$.

**11.** $T_A(x,y) = (x + 2y,\ 2x + 4y)$, so both components vanish exactly when $x = -2y$:

$$
\ker T_A = \{(-2t,\ t) : t \in \mathbb{R}\} = \operatorname{span}\{(-2,1)\},
$$

the line $y = -x/2$. The image is spanned by the columns $(1,2)$ and $(2,4)$, which are proportional, so
$\operatorname{im}T_A = \operatorname{span}\{(1,2)\}$, the line $y = 2x$. The kernel is nontrivial
($\operatorname{nullity} = 1$, $\operatorname{rank} = 1$, sum $2$), so $T_A$ is not injective; it collapses
each line parallel to $(-2,1)$ onto a single point of the line $y = 2x$.

**12.** The columns of $[T]_C^B$ are the images of the basis vectors of $B$, written in $C$ (the standard
basis). Now $T(1,1) = (2,0)$ and $T(1,-1) = (0,2)$, so

$$
[T]_C^B = \begin{pmatrix}2&0\\ 0&2\end{pmatrix}.
$$

*Check:* $[(x,y)]_B = (s,t)^{\mathsf{T}}$ means $(x,y) = s(1,1) + t(1,-1) = (s+t,\ s-t)$, so
$s = \tfrac{x+y}{2}$ and $t = \tfrac{x-y}{2}$. Then $[T(x,y)]_C = (x+y,\ x-y)^{\mathsf{T}} =
(2s,\ 2t)^{\mathsf{T}} = \begin{pmatrix}2&0\\0&2\end{pmatrix}(s,t)^{\mathsf{T}}$, as Theorem 7.8 asserts.
In the standard basis the same map has matrix $\begin{pmatrix}1&1\\1&-1\end{pmatrix}$, so the basis $B$
diagonalises it: the map stretches by $2$ along both basis directions.

## Intermediate

**13.** The matrix is $A = \begin{pmatrix}1&1&0\\ 0&1&1\\ 1&0&1\end{pmatrix}$. Row reduction:
$R_3 \leftarrow R_3 - R_1$ gives $(0,-1,1)$, and $R_3 \leftarrow R_3 + R_2$ gives $(0,0,2)$. So there are
three pivots and $\operatorname{rank}A = 3$. Hence $\operatorname{nullity} = 0$: if $x + y = 0$,
$y + z = 0$ and $z + x = 0$, then $x = -y = z = -x$, so $x = 0$ and all components vanish. Since $T$ is
injective with $\dim V = \dim W = 3$, it is an isomorphism (Corollary 7.13), with

$$
T^{-1}(u,v,w) = \Big(\tfrac{u - v + w}{2},\ \tfrac{u + v - w}{2},\ \tfrac{-u + v + w}{2}\Big),
$$

as one verifies by applying $T$. *Check:* $T(1,1,1) = (2,2,2)$, and the formula returns $(1,1,1)$.

**14.** Row reduction: $R_2 \leftarrow R_2 - 2R_1$ gives $(0,0,0)$ and $R_3 \leftarrow R_3 - R_1$ gives
$(0,-1,-2)$; swapping and scaling,

$$
A \sim \begin{pmatrix}1&0&-1\\ 0&1&2\\ 0&0&0\end{pmatrix}.
$$

Pivots in columns $1,2$ give $\operatorname{rank} = 2$ and one free variable. The kernel: $x_1 = x_3$ and
$x_2 = -2x_3$, so $\ker T_A = \operatorname{span}\{(1,-2,1)^{\mathsf{T}}\}$. The image is spanned by the
pivot columns of $A$, namely

$$
\operatorname{im}T_A = \operatorname{span}\{(1,2,1)^{\mathsf{T}},\ (2,4,1)^{\mathsf{T}}\}.
$$

*Check:* $A(1,-2,1)^{\mathsf{T}} = (1-4+3,\ 2-8+6,\ 1-2+1)^{\mathsf{T}} = \mathbf{0}$, and
$2 + 1 = 3 = \dim\mathbb{R}^3$.

**15.** Solve $T_a(x,y,z) = \mathbf{0}$, i.e. $x + ay = 0$, $y + az = 0$, $ax + z = 0$. From the first
two, $x = -ay$ and $y = -az$, hence $x = a^2z$; the third then reads $a(a^2z) + z = (a^3 + 1)z = 0$.
So the kernel is trivial exactly when $a^3 + 1 \neq 0$.

Over $\mathbb{R}$, $a^3 = -1$ has the single solution $a = -1$, so $T_a$ is an isomorphism for every
$a \neq -1$. (Over $\mathbb{C}$ there are three exceptional values, the cube roots of $-1$.) At $a = -1$
the vector $(1,1,1)$ lies in the kernel, since $x + ay = 1 - 1 = 0$, $y + az = 0$, $ax + z = -1 + 1 = 0$,
so $T_{-1}$ is not injective. *Check with a determinant-free rank count at* $a = -1$: the matrix
$\begin{pmatrix}1&-1&0\\0&1&-1\\-1&0&1\end{pmatrix}$ has third row equal to minus the sum of the first two,
hence rank $2$ and nullity $1$, consistent with the kernel found.

**16.** With $S = \begin{pmatrix}1&-1\\0&2\end{pmatrix}$ and $T = \begin{pmatrix}3&0\\1&1\end{pmatrix}$,

$$
[T\circ S] = [T][S] = \begin{pmatrix}3&0\\1&1\end{pmatrix}\begin{pmatrix}1&-1\\0&2\end{pmatrix}
= \begin{pmatrix}3&-3\\1&1\end{pmatrix},
\qquad
[S\circ T] = [S][T] = \begin{pmatrix}1&-1\\0&2\end{pmatrix}\begin{pmatrix}3&0\\1&1\end{pmatrix}
= \begin{pmatrix}2&-1\\2&2\end{pmatrix}.
$$

The matrices differ, so $T\circ S \neq S\circ T$ (one checks directly on $(1,0)$: $T(S(1,0)) = T(1,0) =
(3,1)$ while $S(T(1,0)) = S(3,0) = (3,0)$). For injectivity of $T\circ S$ solve $3x - 3y = 0$ and
$x + y = 0$: the first gives $x = y$, the second then $2x = 0$, so the kernel is trivial and $T\circ S$ is
injective. *Check:* $\det\begin{pmatrix}3&-3\\1&1\end{pmatrix} = 3 + 3 = 6 \neq 0$, and
$\det S \cdot \det T = 2\cdot 3 = 6$, as multiplicativity requires.

**17.** Here $T(x,y) = (3x + y,\ -x + 2y)$ has standard matrix $\begin{pmatrix}3&1\\-1&2\end{pmatrix}$.
Compute the images and express them in $B = (\mathbf{b}_1,\mathbf{b}_2)$ with $\mathbf{b}_1 = (1,1)$,
$\mathbf{b}_2 = (2,1)$:

$$
T(\mathbf{b}_1) = (4,1) = -2\mathbf{b}_1 + 3\mathbf{b}_2,
\qquad
T(\mathbf{b}_2) = (7,0) = -7\mathbf{b}_1 + 7\mathbf{b}_2 .
$$

Hence

$$
[T]_B = \begin{pmatrix}-2&-7\\ 3&7\end{pmatrix}.
$$

*Check:* $[\mathbf{b}_1]_B = (1,0)^{\mathsf{T}}$ gives first column $(-2,3)^{\mathsf{T}}$, and
$-2(1,1) + 3(2,1) = (4,1) = T(\mathbf{b}_1)$ ✓. Similarly the second column reproduces $(7,0)$. Also
$\operatorname{tr}[T]_B = 5 = \operatorname{tr}\begin{pmatrix}3&1\\-1&2\end{pmatrix}$, as similarity
requires.

**18.** Since $\det P = -2$ and $P^2 = 2I$, we have $P^{-1} = \tfrac12P$. Then

$$
P^{-1}AP = \tfrac12\begin{pmatrix}1&1\\1&-1\end{pmatrix}\begin{pmatrix}4&2\\1&3\end{pmatrix}
\begin{pmatrix}1&1\\1&-1\end{pmatrix}
= \tfrac12\begin{pmatrix}5&5\\3&-1\end{pmatrix}\begin{pmatrix}1&1\\1&-1\end{pmatrix}
= \begin{pmatrix}5&0\\1&2\end{pmatrix}.
$$

Traces: $4 + 3 = 7$ and $5 + 2 = 7$ ✓. *Check by columns:* the columns of $P$ are $\mathbf{b}_1 = (1,1)$
and $\mathbf{b}_2 = (1,-1)$; $A\mathbf{b}_1 = (6,4) = 5\mathbf{b}_1 + 1\mathbf{b}_2$ and
$A\mathbf{b}_2 = (2,-2) = 0\mathbf{b}_1 + 2\mathbf{b}_2$, which are the columns of the result.

**19.** Compute $D$ on each basis vector and expand in $B$:

$$
D(1+x) = 1 = \tfrac12(1+x) + \tfrac12(1-x),
\qquad
D(1-x) = -1 = -\tfrac12(1+x) - \tfrac12(1-x),
\qquad
D(x^2) = 2x = (1+x) - (1-x).
$$

Hence

$$
[D]_B = \begin{pmatrix}\tfrac12&-\tfrac12&1\\[2pt] \tfrac12&-\tfrac12&-1\\[2pt] 0&0&0\end{pmatrix},
\qquad
[D]_B^2 = \begin{pmatrix}0&0&1\\ 0&0&1\\ 0&0&0\end{pmatrix}.
$$

The square is $[D^2]_B$ by Theorem 7.10, and indeed $D^2(x^2) = 2 = 1\cdot(1+x) + 1\cdot(1-x)$, which is
the third column of $[D]_B^2$, while $D^2(1 \pm x) = 0$. Rank–nullity for $D$:
$\operatorname{rank} = 2$ (the image is $\operatorname{span}\{1,x\}$) and $\operatorname{nullity} = 1$
(the constants), summing to $3$.

**20.** Let $M = \begin{pmatrix}0&1\\1&0\end{pmatrix}$ be reflection in $y = x$ and
$R = \begin{pmatrix}0&-1\\1&0\end{pmatrix}$ rotation by $90^\circ$. The composite "reflection, then
rotation" is $R\circ M$:

$$
RM = \begin{pmatrix}0&-1\\1&0\end{pmatrix}\begin{pmatrix}0&1\\1&0\end{pmatrix}
= \begin{pmatrix}-1&0\\ 0&1\end{pmatrix}.
$$

This is reflection in the $y$-axis, since it sends $(x,y)$ to $(-x,y)$. The kernel is
$\{\mathbf{0}\}$: an isometry with a trivial kernel. *Check geometrically:* the $y$-axis makes angle
$90^\circ$ with the $x$-axis, and one may verify the composite fixes exactly the points with $x = 0$.
(The other order, $MR$, gives $\begin{pmatrix}0&1\\1&0\end{pmatrix}\begin{pmatrix}0&-1\\1&0\end{pmatrix}
= \begin{pmatrix}1&0\\0&-1\end{pmatrix}$, reflection in the $x$-axis: the two composites differ.)

**21.** *Linearity.* For matrices $X, Y$ and scalars $a, b$,
$T(aX + bY) = (aX + bY) - (aX+bY)^{\mathsf{T}} = a(X - X^{\mathsf{T}}) + b(Y - Y^{\mathsf{T}}) = aT(X) +
bT(Y)$, using that transposition is linear.

*Kernel.* $T(X) = 0$ means $X = X^{\mathsf{T}}$, so $\ker T$ is the space of symmetric matrices, with
basis $\Big\{\begin{pmatrix}1&0\\0&0\end{pmatrix}, \begin{pmatrix}0&1\\1&0\end{pmatrix},
\begin{pmatrix}0&0\\0&1\end{pmatrix}\Big\}$ and dimension $3$.

*Image.* $T(X)$ is always skew-symmetric, since $(X - X^{\mathsf{T}})^{\mathsf{T}} = X^{\mathsf{T}} - X =
-T(X)$. Conversely every skew-symmetric matrix $\begin{pmatrix}0&c\\-c&0\end{pmatrix}$ equals $T(X)$ for
$X = \begin{pmatrix}0&c\\0&0\end{pmatrix}$. So $\operatorname{im}T$ is the skew-symmetric subspace, of
dimension $1$. Rank–nullity: $1 + 3 = 4 = \dim M_2(\mathbb{R})$ ✓.

**22.** The unit vector along $(3,4)$ is $\mathbf{u} = \tfrac15(3,4)$, and the projection is
$P = \mathbf{u}\mathbf{u}^{\mathsf{T}}$:

$$
P = \frac{1}{25}\begin{pmatrix}9&12\\ 12&16\end{pmatrix},
\qquad
P^2 = \frac{1}{625}\begin{pmatrix}81+144 & 108+192\\ 108+192 & 144+256\end{pmatrix}
= \frac{1}{625}\begin{pmatrix}225&300\\ 300&400\end{pmatrix} = P .
$$

The kernel is the perpendicular line: solve $9x + 12y = 0$, giving
$\ker P = \operatorname{span}\{(-4,3)\}$. The image is the line
$\operatorname{span}\{(3,4)\}$ (the first column $(9,12)$ is $3(3,4)$). Rank–nullity: $1 + 1 = 2$ ✓.
*Check:* $P(3,4) = \tfrac{1}{25}(27+48,\ 36+64) = \tfrac{1}{25}(75,100) = (3,4)$ ✓, and $P(-4,3) =
\tfrac{1}{25}(-36+36,\ -48+48) = \mathbf{0}$ ✓.

**23.** Strategy: prescribe the map on the basis $\mathbf{b}_1 = (1,1,0)$, $\mathbf{b}_2 = (1,0,0)$,
$\mathbf{b}_3 = (0,0,1)$ by sending $\mathbf{b}_1$ to $\mathbf{0}$ and the other two to spanning vectors of
the required image. Take

$$
T(\mathbf{b}_1) = \mathbf{0},\qquad T(\mathbf{b}_2) = (1,0,1),\qquad T(\mathbf{b}_3) = (0,1,1),
$$

and extend by Theorem 7.3. Since $\mathbf{e}_1 = \mathbf{b}_2$, $\mathbf{e}_2 = \mathbf{b}_1 - \mathbf{b}_2$
and $\mathbf{e}_3 = \mathbf{b}_3$, the standard matrix has columns $T(\mathbf{e}_1) = (1,0,1)$,
$T(\mathbf{e}_2) = -(1,0,1) = (-1,0,-1)$, $T(\mathbf{e}_3) = (0,1,1)$:

$$
A = \begin{pmatrix}1&-1&0\\ 0&0&1\\ 1&-1&1\end{pmatrix}.
$$

*Kernel:* $(x - y,\ z,\ x - y + z) = (0,0,0)$ gives $z = 0$, $x = y$, so
$\ker T = \operatorname{span}\{(1,1,0)\}$ ✓. *Image:* spanned by the columns, and the first and third
columns are $(1,0,1)$ and $(0,1,1)$, which are independent; so
$\operatorname{im}T = \operatorname{span}\{(1,0,1),(0,1,1)\}$ ✓. Rank–nullity: $2 + 1 = 3$ ✓.

## Advanced

**24.** *Strategy:* prove the two inclusions separately.

($\subseteq$) Let $\mathbf{w} \in T(\operatorname{span}S)$. Then $\mathbf{w} = T(\mathbf{v})$ for some
$\mathbf{v} = \sum_{i=1}^{k} c_i\mathbf{s}_i$ with $\mathbf{s}_i \in S$. By (5.1),
$\mathbf{w} = \sum_i c_iT(\mathbf{s}_i)$, a finite linear combination of elements of $T[S]$; hence
$\mathbf{w} \in \operatorname{span}T[S]$.

($\supseteq$) Each $\mathbf{s} \in S$ lies in $\operatorname{span}S$, so each $T(\mathbf{s})$ lies in
$T(\operatorname{span}S)$. By Theorem 7.4, $T(\operatorname{span}S)$ is a subspace of $W$, so it contains
the span of any of its subsets; in particular $\operatorname{span}T[S] \subseteq
T(\operatorname{span}S)$. $\square$

**25.** *Strategy:* subspace criterion, twice. Both sets contain $\mathbf{0}$: $\mathbf{0} \in U$ gives
$T(\mathbf{0}) = \mathbf{0} \in T[U]$, and $T(\mathbf{0}) = \mathbf{0} \in U'$ gives
$\mathbf{0} \in T^{-1}[U']$.

*Image.* Take $\mathbf{w}_1 = T(\mathbf{u}_1)$, $\mathbf{w}_2 = T(\mathbf{u}_2)$ in $T[U]$ with
$\mathbf{u}_i \in U$, and $a, b \in K$. Then $a\mathbf{w}_1 + b\mathbf{w}_2 = T(a\mathbf{u}_1 +
b\mathbf{u}_2)$, and $a\mathbf{u}_1 + b\mathbf{u}_2 \in U$ because $U$ is a subspace; hence
$a\mathbf{w}_1 + b\mathbf{w}_2 \in T[U]$.

*Preimage.* Take $\mathbf{v}_1, \mathbf{v}_2 \in T^{-1}[U']$, so $T(\mathbf{v}_i) \in U'$, and
$a, b \in K$. Then $T(a\mathbf{v}_1 + b\mathbf{v}_2) = aT(\mathbf{v}_1) + bT(\mathbf{v}_2) \in U'$
because $U'$ is a subspace; hence $a\mathbf{v}_1 + b\mathbf{v}_2 \in T^{-1}[U']$. $\square$

**26.** ($\Rightarrow$) Suppose $T$ is injective, $\mathbf{v}_1,\dots,\mathbf{v}_k$ independent, and
$\sum_i c_iT(\mathbf{v}_i) = \mathbf{0}$. By (5.1), $T\big(\sum_i c_i\mathbf{v}_i\big) = \mathbf{0} =
T(\mathbf{0})$, so injectivity gives $\sum_i c_i\mathbf{v}_i = \mathbf{0}$, and independence gives
$c_i = 0$ for all $i$. Hence the images are independent.

($\Leftarrow$) Suppose $T$ sends every independent list to an independent list. If
$\mathbf{v} \neq \mathbf{0}$, the one-term list $(\mathbf{v})$ is independent, so $(T(\mathbf{v}))$ is
independent, which by definition means $T(\mathbf{v}) \neq \mathbf{0}$. Hence
$\ker T = \{\mathbf{0}\}$ and $T$ is injective (Theorem 7.6). $\square$

*Remark.* The injectivity hypothesis cannot be dropped: the zero map sends every independent list to the
dependent list $(\mathbf{0},\dots,\mathbf{0})$.

**27.** Suppose $\sum_i c_i\mathbf{v}_i = \mathbf{0}$. Applying $T$ and using (5.1),
$\sum_i c_iT(\mathbf{v}_i) = T(\mathbf{0}) = \mathbf{0}$; independence of the images forces every
$c_i = 0$. Hence the $\mathbf{v}_i$ are independent.

The converse is false. Take $T : \mathbb{R}^2 \to \mathbb{R}^2$, $T(x,y) = (x,0)$, and the independent
list $(1,0)$, $(1,1)$. Its image is $(1,0)$, $(1,0)$, a dependent list. (Linearity transports dependence
forward automatically, but reflects it backward only when $T$ is injective — Exercise 26.) $\square$

**28.** If $\mathbf{w} = T(\mathbf{v}) \in \operatorname{im}T$ then $T(\mathbf{w}) = T^2(\mathbf{v}) =
\mathbf{0}$, so $\operatorname{im}T \subseteq \ker T$. Taking dimensions,
$\operatorname{rank}T \le \operatorname{nullity}T$, and rank–nullity gives
$\dim V = \operatorname{rank}T + \operatorname{nullity}T \ge 2\operatorname{rank}T$, that is
$\operatorname{rank}T \le \tfrac12\dim V$.

Example on $\mathbb{R}^4$: $T(x_1,x_2,x_3,x_4) = (x_3,\ x_4,\ 0,\ 0)$, with matrix

$$
\begin{pmatrix}0&0&1&0\\ 0&0&0&1\\ 0&0&0&0\\ 0&0&0&0\end{pmatrix}.
$$

Then $T^2 = 0$ and the image is $\operatorname{span}\{\mathbf{e}_1,\mathbf{e}_2\}$, of dimension
$2 = \tfrac12\cdot4$. $\square$

**29.** Apply rank–nullity (Theorem 7.12) to the restriction
$T|_{U} : U \to W$, which is linear with

$$
\ker(T|_U) = \{\mathbf{u} \in U : T(\mathbf{u}) = \mathbf{0}\} = U \cap \ker T,
\qquad
\operatorname{im}(T|_U) = \{T(\mathbf{u}) : \mathbf{u} \in U\} = T[U].
$$

Since $U$ is a subspace of the finite-dimensional $V$, it is finite-dimensional, so

$$
\dim U = \dim(U \cap \ker T) + \dim T[U],
$$

which is the claimed identity. The inequality $\dim T[U] \le \dim U$ follows because
$\dim(U \cap \ker T) \ge 0$. $\square$

*Remark.* Taking $U = V$ recovers rank–nullity itself; taking $U \cap \ker T = \{\mathbf{0}\}$ shows that
an injective map preserves the dimension of every subspace it meets.

**30.** *Existence.* Let $Q = (q_{ij})$ and define $\mathbf{b}'_j = \sum_{i=1}^{n} q_{ij}\mathbf{b}_i$ for
$j = 1,\dots,n$. The coordinate vector of $\mathbf{b}'_j$ in $B$ is exactly the $j$-th column of $Q$. Since
$\Phi_B : V \to K^n$ is a linear bijection (Lemma 7.7) and $Q$ is invertible, the map
$K^n \to K^n$, $\mathbf{x}\mapsto Q\mathbf{x}$ is a linear bijection, so
$\mathbf{x}\mapsto\Phi_B^{-1}(Q\mathbf{x})$ is a linear bijection $K^n \to V$. The image of the standard
basis of $K^n$ under this bijection is $(\mathbf{b}'_1,\dots,\mathbf{b}'_n)$, which is therefore a basis of
$V$; and $[\operatorname{id}_V]_B^{B'} = Q$ by construction.

*Uniqueness.* If $B'$ is any basis with $[\operatorname{id}_V]_B^{B'} = Q$, then by definition the $j$-th
column of that matrix is $[\mathbf{b}'_j]_B$, so $\mathbf{b}'_j = \sum_i q_{ij}\mathbf{b}_i$: the basis is
determined by $Q$.

*Deduction.* Let $C = P^{-1}[T]_BP$ be similar to $[T]_B$. By existence, there is a basis $B'$ with
$[\operatorname{id}_V]_B^{B'} = P$; then Theorem 7.17 gives $[T]_{B'} = P^{-1}[T]_BP = C$. Conversely
Theorem 7.17 shows every $[T]_{B'}$ is similar to $[T]_B$, so similarity classes of matrices are exactly
the matrices of one map in all possible bases. $\square$

**31.** ($\Leftarrow$) If $S\circ T = \operatorname{id}_V$ and $T(\mathbf{v}) = \mathbf{0}$, then
$\mathbf{v} = S(T(\mathbf{v})) = S(\mathbf{0}) = \mathbf{0}$; so $\ker T = \{\mathbf{0}\}$ and $T$ is
injective.

($\Rightarrow$) Suppose $T$ is injective and let $B = (\mathbf{b}_1,\dots,\mathbf{b}_n)$ be a basis of
$V$. The list $T(\mathbf{b}_1),\dots,T(\mathbf{b}_n)$ is independent (Exercise 26) and spans
$\operatorname{im}T$, so it is a basis of $\operatorname{im}T$. Extend it to a basis
$T(\mathbf{b}_1),\dots,T(\mathbf{b}_n),\mathbf{w}_1,\dots,\mathbf{w}_k$ of $W$ (basis extension lemma), and
define $S : W \to V$ on that basis by

$$
S\big(T(\mathbf{b}_i)\big) = \mathbf{b}_i,\qquad S(\mathbf{w}_l) = \mathbf{0},
$$

extended linearly (Theorem 7.3). Then for $\mathbf{v} = \sum_i c_i\mathbf{b}_i$,
$S(T(\mathbf{v})) = \sum_i c_iS(T(\mathbf{b}_i)) = \sum_i c_i\mathbf{b}_i = \mathbf{v}$. $\square$

*Remark.* The finite dimension is used twice: to have a finite basis to extend, and to know that a basis
of $\operatorname{im}T$ exists with $n$ elements.

**32.** ($\Leftarrow$) If $A = [T]_B$ and $C = [T]_{B'}$ for bases $B, B'$ of $V$, then
Theorem 7.17 gives $C = P^{-1}AP$ with $P = [\operatorname{id}_V]_B^{B'}$, which is invertible by
Corollary 7.11. So $A$ and $C$ are similar.

($\Rightarrow$) Suppose $C = P^{-1}AP$ with $P$ invertible, and let $B$ be a basis of $V$ with
$A = [T]_B$. By Exercise 30 there is a basis $B'$ with $[\operatorname{id}_V]_B^{B'} = P$, and then
Theorem 7.17 gives $[T]_{B'} = P^{-1}AP = C$. So $A$ and $C$ represent the same map in different bases.

*Deduction.* If $\begin{pmatrix}1&1\\0&1\end{pmatrix}$ were similar to $I_2$, there would be an invertible
$P$ with $P^{-1}\begin{pmatrix}1&1\\0&1\end{pmatrix}P = I_2$. Multiplying on the left by $P$ and on the
right by $P^{-1}$ gives $\begin{pmatrix}1&1\\0&1\end{pmatrix} = PIP^{-1} = I_2$, which is false. Hence the
two matrices are not similar. Note that the numerical invariants of Proposition 7.19 do not detect this:
both matrices have trace $2$ and rank $2$. The structural reason is that $I_2$ commutes with every
matrix, whereas $\begin{pmatrix}1&1\\0&1\end{pmatrix}$ does not, and commuting with everything is
preserved by conjugation. $\square$

**33.** *Invertibility.* The relation $T^2 = T + 2\operatorname{id}_V$ rearranges to
$T^2 - T = 2\operatorname{id}_V$. Since polynomials in $T$ commute, both one-sided computations agree:

$$
T\circ\Big(\tfrac12(T - \operatorname{id}_V)\Big) = \tfrac12(T^2 - T) = \operatorname{id}_V,
\qquad
\Big(\tfrac12(T - \operatorname{id}_V)\Big)\circ T = \tfrac12(T^2 - T) = \operatorname{id}_V ,
$$

so $T$ is invertible with $T^{-1} = \tfrac12(T - \operatorname{id}_V)$.

*Decomposition.* Note $(T - 2\operatorname{id}_V)\circ(T + \operatorname{id}_V) = T^2 - T -
2\operatorname{id}_V = 0$. For any $\mathbf{v} \in V$,

$$
\mathbf{v} = \tfrac13\big(T + \operatorname{id}_V\big)(\mathbf{v}) - \tfrac13\big(T - 2\operatorname{id}_V\big)(\mathbf{v}),
$$

because the right side is $\tfrac13\big(T\mathbf{v} + \mathbf{v} - T\mathbf{v} + 2\mathbf{v}\big) =
\mathbf{v}$. The first summand lies in $\ker(T - 2\operatorname{id}_V)$, since
$(T - 2\operatorname{id}_V)(T + \operatorname{id}_V)\mathbf{v} = \mathbf{0}$; the second lies in
$\ker(T + \operatorname{id}_V)$, since $(T + \operatorname{id}_V)(T - 2\operatorname{id}_V) = T^2 - T -
2\operatorname{id}_V = 0$ as well (the two factors commute, being polynomials in $T$). If
$\mathbf{w}$ lies in both kernels then $T\mathbf{w} = 2\mathbf{w}$ and $T\mathbf{w} = -\mathbf{w}$, so
$3\mathbf{w} = \mathbf{0}$ and $\mathbf{w} = \mathbf{0}$. Hence the sum is direct. $\square$

## Challenge

**34.** *Strategy.* The map $\mathbf{x} \mapsto \mathbf{x} - \tfrac{1}{4}\big(\sum_i x_i\big)
(1,1,1,1)$ removes the component along $(1,1,1,1)$, so it should kill exactly that direction and land in
the hyperplane of zero coordinate sum. Define

$$
T(\mathbf{x}) = \mathbf{x} - \frac{x_1 + x_2 + x_3 + x_4}{4}(1,1,1,1),
\qquad
[T] = I_4 - \tfrac14 J_4 = \frac14\begin{pmatrix}
3&-1&-1&-1\\ -1&3&-1&-1\\ -1&-1&3&-1\\ -1&-1&-1&3\end{pmatrix},
$$

where $J_4$ is the all-ones matrix. $T$ is linear: it is the sum of the identity and a scalar multiple of
the linear functional $\mathbf{x}\mapsto\sum_i x_i$ times a fixed vector.

*Kernel.* If $T(\mathbf{x}) = \mathbf{0}$ then $\mathbf{x} = c(1,1,1,1)$ with
$c = \tfrac14\sum_i x_i = \tfrac14\cdot 4c = c$, so every $c$ works and
$\ker T = \operatorname{span}\{(1,1,1,1)\}$.

*Image.* For any $\mathbf{x}$, the coordinate sum of $T(\mathbf{x})$ is
$\sum_i x_i - \tfrac{4}{4}\sum_i x_i = 0$, so $\operatorname{im}T \subseteq H := \{\mathbf{x} :
\sum_i x_i = 0\}$, a hyperplane of dimension $3$. By rank–nullity,
$\dim(\operatorname{im}T) = 4 - 1 = 3 = \dim H$; a $3$-dimensional subspace of a $3$-dimensional space is
the whole space, so $\operatorname{im}T = H$ ✓.

*Check on a vector:* $T(1,0,0,0) = (1,0,0,0) - \tfrac14(1,1,1,1) = \tfrac14(3,-1,-1,-1)$, whose entries sum
to $0$ ✓, and $T(1,1,1,1) = (1,1,1,1) - \tfrac44(1,1,1,1) = \mathbf{0}$ ✓. Also $T^2 = T$, as a
projection must satisfy — see Proposition 8.3.

**35.** *$R$ injective.* If $R(\mathbf{x}) = \mathbf{0}$ then $(0,x_1,x_2,\dots) = (0,0,0,\dots)$, so every
$x_i = 0$ and $\mathbf{x} = \mathbf{0}$; a linear map with trivial kernel is injective (Theorem 7.6).

*$R$ not surjective.* The sequence $\mathbf{e} = (1,0,0,\dots)$ is not in $\operatorname{im}R$: every
image has first term $0$.

*$L$ surjective.* Given $\mathbf{y} = (y_1,y_2,\dots)$, the sequence $\mathbf{x} = (0,y_1,y_2,\dots)$
satisfies $L(\mathbf{x}) = \mathbf{y}$.

*$L$ not injective.* $\ker L = \{(c,0,0,\dots) : c \in \mathbb{R}\} \neq \{\mathbf{0}\}$.

*Compositions.* For every $\mathbf{x}$,
$L(R(\mathbf{x})) = L(0,x_1,x_2,\dots) = (x_1,x_2,\dots) = \mathbf{x}$, so
$L\circ R = \operatorname{id}_V$; but $R(L(\mathbf{x})) = (0,x_2,x_3,\dots)$, which differs from
$\mathbf{x}$ whenever $x_1 \neq 0$.

*Why no contradiction.* Corollary 7.13(4) assumes $\dim V = \dim W < \infty$. Here $V$ is
infinite-dimensional, and indeed $L\circ R = \operatorname{id}$ with $R\circ L \neq \operatorname{id}$ is
impossible in finite dimension: if $S\circ T = \operatorname{id}$ and $V$ is finite-dimensional then $T$
is an isomorphism (Exercise 37), so $T\circ S = \operatorname{id}$ as well.

**36.** *$T$ is an isomorphism.* $T\circ(-T) = -T^2 = \operatorname{id}_V$ and
$(-T)\circ T = \operatorname{id}_V$, so $T$ is bijective with $T^{-1} = -T$.

*Independence.* Let $\mathbf{v} \neq \mathbf{0}$ and suppose $T(\mathbf{v}) = c\mathbf{v}$ with
$c \in \mathbb{R}$. Then $\mathbf{0} \neq -\mathbf{v} = T^2(\mathbf{v}) = cT(\mathbf{v}) = c^2\mathbf{v}$,
so $c^2 = -1$, which has no real solution. Hence $T(\mathbf{v})$ is not a multiple of $\mathbf{v}$ and the
pair is independent; in particular $T(\mathbf{v}) \neq \mathbf{0}$ and $U =
\operatorname{span}\{\mathbf{v}, T(\mathbf{v})\}$ is two-dimensional.

*$U$ is $T$-invariant.* $T(\mathbf{v}) \in U$ and $T(T(\mathbf{v})) = -\mathbf{v} \in U$. Since $T$ is
injective, $T|_U : U \to U$ is injective, hence bijective, so $T(U) = U$ and therefore
$T^{-1}(U) = U$.

*Averaging.* Choose any projection $\pi : V \to V$ onto $U$ (extend a basis of $U$ to a basis of $V$ and
define $\pi$ to fix $U$ and kill the extra basis vectors) and set

$$
\pi' = \tfrac12\big(\pi + T^{-1}\pi T\big).
$$

$\pi'$ has image inside $U$: for any $\mathbf{x}$, $\pi(\mathbf{x}) \in U$, and
$\pi(T(\mathbf{x})) \in U$ with $T^{-1}(U) = U$, so $T^{-1}\pi T(\mathbf{x}) \in U$. Also $\pi'$ fixes
$U$ pointwise: for $\mathbf{u} \in U$, $\pi(\mathbf{u}) = \mathbf{u}$ and
$T^{-1}\pi T(\mathbf{u}) = T^{-1}T(\mathbf{u}) = \mathbf{u}$. A linear map with image $U$ that fixes $U$
satisfies $\pi'^2 = \pi'$, so $\pi'$ is a projection onto $U$ and $V = U \oplus \ker\pi'$
(Proposition 8.3).

*$\pi'$ commutes with $T$.* Since $T^{-1} = -T$, we have $T^{-1}\pi T = -T\pi T = T\pi T^{-1}$, hence

$$
T\pi'T^{-1} = \tfrac12\big(T\pi T^{-1} + T T^{-1}\pi T T^{-1}\big) = \tfrac12\big(T\pi T^{-1} + \pi\big)
= \tfrac12\big(T^{-1}\pi T + \pi\big) = \pi'.
$$

*Conclusion.* $\ker\pi'$ is $T$-invariant: if $\pi'(\mathbf{x}) = \mathbf{0}$ then
$\pi'(T(\mathbf{x})) = T(\pi'(\mathbf{x})) = \mathbf{0}$. Its dimension is $\dim V - 2$, and $T$ restricted
to it still satisfies $T^2 = -\operatorname{id}$. Induction on $\dim V$ (base case $\dim V = 0$) shows
$\dim(\ker\pi')$ is even, hence $\dim V = 2 + \dim(\ker\pi')$ is even. $\square$

**37.** *$T$ injective.* If $T(\mathbf{v}) = \mathbf{0}$ then
$\mathbf{v} = (S\circ T)(\mathbf{v}) = S(\mathbf{0}) = \mathbf{0}$.

*$T$ an isomorphism.* Since $V$ is finite-dimensional and $T : V \to V$ is injective, Corollary 7.13
gives that $T$ is bijective, so $T^{-1}$ exists.

*$S = T^{-1}$.* From $S\circ T = \operatorname{id}_V$, compose on the right with $T^{-1}$:
$S = S\circ(T\circ T^{-1}) = (S\circ T)\circ T^{-1} = T^{-1}$. $\square$

*Finite dimension is essential.* On the space of real sequences take $T = R$ (right shift) and $S = L$
(left shift) from Exercise 35: $S\circ T = L\circ R = \operatorname{id}$, yet $T$ is not surjective and
therefore not an isomorphism. The argument above fails at the step "injective implies bijective", which
needs equal finite dimension.

**38.** *Answer.* Exactly the following: $A = I_2$; $A = -I_2$; and
$A = \begin{pmatrix}a&b\\ c&-a\end{pmatrix}$ with $a^2 + bc = 1$.

*Proof.* If $A^2 = I$ then $(A - I)(A + I) = A^2 - I = 0$. Put
$U_+ = \ker(A - I)$ and $U_- = \ker(A + I)$. For any $\mathbf{x} \in \mathbb{R}^2$,

$$
\mathbf{x} = \tfrac12\big((A + I)\mathbf{x}\big) - \tfrac12\big((A - I)\mathbf{x}\big),
$$

and $(A - I)\big((A+I)\mathbf{x}\big) = (A^2 - I)\mathbf{x} = \mathbf{0}$, so the first summand lies in
$U_+$; similarly the second lies in $U_-$. If $\mathbf{y} \in U_+ \cap U_-$ then
$A\mathbf{y} = \mathbf{y}$ and $A\mathbf{y} = -\mathbf{y}$, so $\mathbf{y} = \mathbf{0}$. Hence
$\mathbb{R}^2 = U_+ \oplus U_-$.

The dimensions add to $2$, so the possibilities are $(\dim U_+, \dim U_-) = (2,0)$, $(0,2)$ or $(1,1)$.
In the first case $A\mathbf{x} = \mathbf{x}$ for all $\mathbf{x}$, so $A = I$; in the second
$A = -I$. In the third case $A$ has eigenvalue $1$ with a one-dimensional eigenspace and eigenvalue $-1$
with a one-dimensional eigenspace, so $\operatorname{tr}A = 1 + (-1) = 0$; a $2\times2$ matrix with trace
$0$ has the form $\begin{pmatrix}a&b\\c&-a\end{pmatrix}$, and its determinant is $-a^2 - bc$. But the
determinant is also the product of the eigenvalues, $-1$, so $a^2 + bc = 1$.

*Converse.* If $A = \begin{pmatrix}a&b\\c&-a\end{pmatrix}$ with $a^2 + bc = 1$, then
$A^2 = (a^2 + bc)I = I$, and $A \neq \pm I$ in this family. $\square$

*Geometric interpretation.* In the third case $A$ fixes the line $U_+$ pointwise and negates the
directions in $U_-$; it is a **reflection in the line** $U_+$ **along the direction** $U_-$. When $U_+$
and $U_-$ are perpendicular the reflection is the usual orthogonal one (for instance
$\begin{pmatrix}1&0\\0&-1\end{pmatrix}$, or $\begin{pmatrix}0&1\\1&0\end{pmatrix}$ for the line $y = x$);
when they are not, the reflection is **oblique**, as in $\begin{pmatrix}1&2\\0&-1\end{pmatrix}$, which
fixes the $x$-axis pointwise and moves $(0,1)$ to $(2,-1)$. Real eigenvalues $1$ and $-1$ with independent
eigenvectors are exactly what makes this a reflection rather than a rotation.
