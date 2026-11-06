# Geometric Transformations — Solutions

> [Tutorial](README.md) · [Exercises](exercises.md) · 35 worked solutions

Each solution gives the formula used, the computation, and a check on distances or a sketch-level
property. Composition problems state the order explicitly, since that is where most errors occur.

## Beginner

**1.** $T_{(6,-3)}(-4,5)=(-4+6,\ 5-3)=\boxed{(2,2)}$.
Check: the displacement is $(6,-3)$, whose length is $\sqrt{36+9}=\sqrt{45}=3\sqrt5$, and indeed the
image is that far from the original: $(2+4)^2+(2-5)^2=36+9=45$. $\checkmark$

**2.** The quarter-turn is $(x,y)\mapsto(-y,x)$, so $(-2,5)\mapsto(-5,-2)$. Check: both points are
$\sqrt{29}$ units from the origin and the radii are perpendicular,
$(-2,5)\cdot(-5,-2)=10-10=0$. $\checkmark$

**3.** The half-turn is $(x,y)\mapsto(-x,-y)$, so $(-3,4)\mapsto(3,-4)$. This is also the dilation by factor
$-1$ about the origin; both descriptions agree.

**4.** (a) Reflection in the $x$-axis: $(x,y)\mapsto(x,-y)$, so $(5,-3)\mapsto(5,3)$.
(b) Reflection in the $y$-axis: $(x,y)\mapsto(-x,y)$, so $(5,-3)\mapsto(-5,-3)$.
Check: all three points have distance $\sqrt{34}$ from the origin, and the three lie on a circle centred
there, as reflections must preserve distance from the fixed point of the axis intersection.

**5.** Reflection in $y=x$ is $(x,y)\mapsto(y,x)$, so $(2,7)\mapsto(7,2)$. Check: the midpoint of $(2,7)$ and
$(7,2)$ is $(4.5,4.5)$, which lies on $y=x$, and the segment joining them has slope $-1$, perpendicular
to the mirror. $\checkmark$

**6.** $D_{3}\left(6,-9\right)=\left(\tfrac13\cdot6,\ \tfrac13\cdot(-9)\right)=(2,-3)$.
Check: the image is one third as far from the origin, $\sqrt{13}=\tfrac13\sqrt{117}$. $\checkmark$

**7.**

$$
R_{90^\circ}=\begin{pmatrix}\cos90^\circ&-\sin90^\circ\\ \sin90^\circ&\cos90^\circ\end{pmatrix}
=\begin{pmatrix}0&-1\\ 1&0\end{pmatrix},
\qquad
R_{90^\circ}\begin{pmatrix}1\\0\end{pmatrix}=\begin{pmatrix}0\\1\end{pmatrix}.
$$

So $(1,0)\mapsto(0,1)$, the quarter-turn in agreement with $(x,y)\mapsto(-y,x)$.

**8.** The rule adds a constant vector: $(x,y)\mapsto(x+4,y-1)$ is the **translation** by $(4,-1)$. It has no
fixed point, preserves distances, and its inverse is the translation by $(-4,1)$.

**9.** $(x,y)\mapsto(-x,y)$ changes the sign of the $x$-coordinate and keeps $y$: the **reflection in the
$y$-axis**. Its fixed points are those with $x=0$, i.e. the whole axis, and it is its own inverse.

**10.** $(x,y)\mapsto(2x,2y)$ multiplies both coordinates by $2$: the **dilation** with centre the origin and
factor $2$. Lengths double, areas quadruple, and the only fixed point is the origin.

**11.** $(x,y)\mapsto(y,x)$ swaps the coordinates: the **reflection in the line $y=x$**. Check: the fixed points
satisfy $y=x$, exactly the mirror line; and applying the rule twice returns the original point.

**12.**

| Figure | Lines of symmetry | Order of rotation |
|---|---|---|
| Regular decagon | $10$ | $10$ |
| Non-square rhombus | $2$ | $2$ |
| Isosceles (non-equilateral) triangle | $1$ | $1$ |
| Scalene triangle | $0$ | $1$ |

For a regular $n$-gon the group always has order $2n$; the decagon is regular with $n=10$. Neither the
rhombus nor the triangles are regular: the rhombus has two axes (its diagonals) and half-turn symmetry,
the isosceles triangle has one axis and no non-trivial rotation, and the scalene triangle has only the
identity.

## Intermediate

**13.** With $\cos60^\circ=\tfrac12$ and $\sin60^\circ=\tfrac{\sqrt3}{2}$,

$$
x'=3\cdot\tfrac12-4\cdot\tfrac{\sqrt3}{2}=\frac{3-4\sqrt3}{2},\qquad
y'=3\cdot\tfrac{\sqrt3}{2}+4\cdot\tfrac12=\frac{3\sqrt3+4}{2}.
$$

The image is $\boxed{\left(\frac{3-4\sqrt3}{2},\ \frac{3\sqrt3+4}{2}\right)}\approx(-1.964,\ 4.598)$.
Check: the original point has distance $5$ from the origin, and so does the image, since
$\left(3-4\sqrt3\right)^2+\left(3\sqrt3+4\right)^2=9-24\sqrt3+48+27+24\sqrt3+16=100$ and
$\tfrac12\sqrt{100}=5$. The angle increases by $60^\circ$: the original is at
$\arctan(4/3)\approx53.13^\circ$ and the image at $\approx113.13^\circ$. $\checkmark$

**14.**

$$
(R\circ T)(1,1)=R(3,2)=(-2,3),\qquad (T\circ R)(1,1)=T(-1,1)=(1,2).
$$

The results differ, so $R\circ T\ne T\circ R$: **composition is not commutative**. The first is a
$90^\circ$ rotation about $\left(-\tfrac32,\tfrac12\right)$, the second a $90^\circ$ rotation about
$\left(\tfrac12,\tfrac32\right)$ — both rotations, but about different centres. Indeed
$R\circ T$ fixes $\left(-\tfrac32,\tfrac12\right)$: $T$ sends it to $\left(\tfrac12,\tfrac32\right)$ and
$R$ returns it.

**15.** A point of the line is $(x,\,-3x+2)$; reflecting in the $y$-axis sends it to $(-x,\,-3x+2)$. Put
$X=-x$, so $x=-X$; then the image satisfies $Y=-3(-X)+2=3X+2$. The image is
$$\boxed{y=3x+2}.$$
Check: the original passes through $(0,2)$, which is fixed by the reflection, and through $(1,-1)$, whose
image is $(-1,-1)$; both $(0,2)$ and $(-1,-1)$ satisfy $y=3x+2$. $\checkmark$

**16.** A point of $y=2x+3$ is $(x,\,2x+3)$, whose image under the quarter-turn is
$(-(2x+3),\,x)=(-2x-3,\,x)$. Put $Y=x$; then $X=-2Y-3$, i.e. $Y=-\frac{X+3}{2}$. The image is
$$\boxed{y=-\frac{x+3}{2}}\quad\text{or}\quad x+2y+3=0.$$
Check: $(0,3)$ lies on the original and maps to $(-3,0)$, which satisfies $x+2y+3=0$; the original slope
$2$ becomes $-\tfrac12$, the negative reciprocal, as a quarter-turn requires. $\checkmark$

**17.** **Fixed points.** $g(x,y)=(x,y)$ requires $x-4=x$ and $-y=y$. The first is impossible, so $g$ has
$\boxed{\text{no fixed points}}$.

**Square.** $g(g(x,y))=g(x-4,-y)=(x-4-4,\ -(-y))=(x-8,\ y)$, so
$$g\circ g=T_{(-8,0)}.$$

**Inverse.** From $g^2=T_{(-8,0)}$ we get $g^{-1}=T_{(8,0)}\circ g$, and directly
$g^{-1}(x,y)=(x+4,-y)$. Check: $g(x+4,-y)=(x+4-4,\ y)=(x,y)$. $\checkmark$

Geometrically $g$ is the glide reflection with axis the $x$-axis and glide vector $(-4,0)$.

**18.** Rotate the displacement from the centre, then add the centre back. Here $C=(2,1)$ and
$P-C=(3,1)$; the quarter-turn gives $(-1,3)$, so
$$P'=C+(-1,3)=(2-1,\ 1+3)=\boxed{(1,4)}.$$
Check: $\lvert CP\rvert=\sqrt{9+1}=\sqrt{10}=\lvert CP'\rvert$, and $(3,1)\cdot(-1,3)=-3+3=0$, so the
angle at $C$ is $90^\circ$. $\checkmark$

**19.** $D_{C,2}(P)=C+2(P-C)=(2,3)+2(3,-2)=(2+6,\ 3-4)=\boxed{(8,-1)}$.
Check: $P-C=(3,-2)$ and $P'-C=(6,-4)=2(3,-2)$, so $P'$ is twice as far from $C$ along the same ray.
$\checkmark$

**20.** A regular pentagon has $5$ rotational symmetries (rotations through $0^\circ,72^\circ,144^\circ,216^\circ,
288^\circ$ about the centre) and $5$ lines of symmetry, each through a vertex and the midpoint of the
opposite side. The symmetry group therefore has
$$\boxed{2\cdot5=10\ \text{elements}},$$
with $5$ rotations and $5$ reflections. No symmetry can be a translation or a glide reflection, because
the pentagon is bounded.

**21.** Reflection in $x=1$: $x\mapsto 2-x$. Reflection in $x=4$: $x\mapsto8-x$.

*Reflect in $x=1$, then in $x=4$:* $x\mapsto 2-x\mapsto 8-(2-x)=x+6$, a translation by $6$ to the right.
*Reflect in $x=4$, then in $x=1$:* $x\mapsto 8-x\mapsto 2-(8-x)=x-6$, a translation by $6$ to the left.

Both are translations by twice the separation $2(4-1)=6$, in opposite directions — the parallel-line case
of Theorem 7.7, and another illustration of non-commutativity.

**22.** Compare the displacements from $A$:

$$
B-A=(2,0)\mapsto(7-3,\ 3-3)=(4,0)=2(2,0),\qquad
C-A=(0,1)\mapsto(3-3,\ 5-3)=(0,2)=2(0,1).
$$

The linear part is multiplication by $2$, so the factor is $2$. A dilation fixes its centre, so the
centre $c$ satisfies $c\mapsto A'=(3,3)$ and also $c\mapsto c$; from $A'=c+2(A-c)$,

$$
(3,3)=c+2\bigl((1,1)-c\bigr)=(2,2)-c\quad\Longrightarrow\quad c=(-1,-1).
$$

The transformation is $\boxed{D_{(-1,-1),2}}$. Check with $B$: $(-1,-1)+2(4,2)=(7,3)$;
with $C$: $(-1,-1)+2(2,3)=(3,5)$. $\checkmark$

**23.** Rotations about the same centre add angles, so $R_{60^\circ}\circ R_{30^\circ}=R_{90^\circ}$ (the order
does not matter here). Verify on $(2,0)$:

$$
(2,0)\xrightarrow{R_{30^\circ}}\left(2\cos30^\circ,\,2\sin30^\circ\right)=(\sqrt3,\,1),
$$

$$
(\sqrt3,1)\xrightarrow{R_{60^\circ}}
\left(\sqrt3\cdot\tfrac12-1\cdot\tfrac{\sqrt3}{2},\ \sqrt3\cdot\tfrac{\sqrt3}{2}+1\cdot\tfrac12\right)
=\left(0,\ \tfrac32+\tfrac12\right)=(0,2),
$$

which is exactly $R_{90^\circ}(2,0)$. $\checkmark$

**24.** Let $A=\begin{pmatrix}0&1\\1&0\end{pmatrix}$. Then
$A^{\mathsf T}A=\begin{pmatrix}0&1\\1&0\end{pmatrix}\begin{pmatrix}0&1\\1&0\end{pmatrix}=\begin{pmatrix}1&0\\0&1\end{pmatrix}$,
so $A$ is orthogonal, and $\det A=0\cdot0-1\cdot1=-1$. Orthogonality says lengths and angles are
preserved; the determinant $-1$ says orientation is reversed. The map is $(x,y)\mapsto(y,x)$, the
reflection in $y=x$ — matching the general reflection matrix with $2\alpha=90^\circ$.

## Advanced

**25.** Write $P=(x_1,y_1)$, $Q=(x_2,y_2)$, $\Delta x=x_2-x_1$, $\Delta y=y_2-y_1$. Then

$$
R_\theta(P)=\bigl(x_1\cos\theta-y_1\sin\theta,\ x_1\sin\theta+y_1\cos\theta\bigr),
$$

and the difference $R_\theta(Q)-R_\theta(P)$ equals $R_\theta$ applied to $(\Delta x,\Delta y)$ by
linearity:

$$
\bigl(\Delta x\cos\theta-\Delta y\sin\theta,\ \Delta x\sin\theta+\Delta y\cos\theta\bigr).
$$

Its squared length is

$$
\begin{aligned}
&\Delta x^2\cos^2\theta-2\Delta x\Delta y\sin\theta\cos\theta+\Delta y^2\sin^2\theta\\
&\qquad+\Delta x^2\sin^2\theta+2\Delta x\Delta y\sin\theta\cos\theta+\Delta y^2\cos^2\theta\\
&=\Delta x^2(\cos^2\theta+\sin^2\theta)+\Delta y^2(\sin^2\theta+\cos^2\theta)=\Delta x^2+\Delta y^2 .
\end{aligned}
$$

Hence $\lvert R_\theta(P)-R_\theta(Q)\rvert=\lvert P-Q\rvert$, so the rotation preserves distance.
$\blacksquare$

**26.** By §7.4, reflection in the line at angle $\alpha$ has matrix

$$
S_\alpha=\begin{pmatrix}\cos2\alpha&\sin2\alpha\\ \sin2\alpha&-\cos2\alpha\end{pmatrix}.
$$

Compose (first $\alpha$, then $\beta$): the composite has matrix $S_\beta S_\alpha$. Its entries are

$$
\begin{aligned}
(1,1)&:\ \cos2\beta\cos2\alpha+\sin2\beta\sin2\alpha=\cos(2\beta-2\alpha),\\
(1,2)&:\ \cos2\beta\sin2\alpha-\sin2\beta\cos2\alpha=-\sin(2\beta-2\alpha),\\
(2,1)&:\ \sin2\beta\cos2\alpha-\cos2\beta\sin2\alpha=\sin(2\beta-2\alpha),\\
(2,2)&:\ \sin2\beta\sin2\alpha+\cos2\beta\cos2\alpha=\cos(2\beta-2\alpha),
\end{aligned}
$$

using the addition formulas for cosine and sine. Therefore

$$
S_\beta S_\alpha=\begin{pmatrix}\cos2(\beta-\alpha)&-\sin2(\beta-\alpha)\\ \sin2(\beta-\alpha)&\cos2(\beta-\alpha)\end{pmatrix}
=R_{2(\beta-\alpha)},
$$

a rotation about the origin through twice the angle between the lines. $\blacksquare$

**Check.** For $\alpha=0^\circ$, $\beta=30^\circ$ the composite must be $R_{60^\circ}$: the point $(1,0)$
is fixed by the first reflection and goes to $\left(\tfrac12,\tfrac{\sqrt3}{2}\right)$ under the second,
which is indeed its image under $R_{60^\circ}$.

**27.** **Step 1: $T$ preserves lengths from the origin.** Since $T(0)=0$,
$\lvert T(P)\rvert=d(T(P),T(0))=d(P,0)=\lvert P\rvert$.

**Step 2: $T$ preserves dot products.** Expanding the distance condition
$\lvert T(P)-T(Q)\rvert^2=\lvert P-Q\rvert^2$ and using Step 1 to cancel $\lvert T(P)\rvert^2=\lvert P\rvert^2$
and $\lvert T(Q)\rvert^2=\lvert Q\rvert^2$ leaves $T(P)\cdot T(Q)=P\cdot Q$. Applying this to the
standard basis, the vectors $T(e_1)$, $T(e_2)$ are unit and orthogonal.

**Step 3: $T$ is linear.** Write $P=xe_1+ye_2$ and let $W=xT(e_1)+yT(e_2)$. Then

$$
\begin{aligned}
\lvert T(P)-W\rvert^2
&=\lvert T(P)\rvert^2+\lvert W\rvert^2-2T(P)\cdot W\\
&=(x^2+y^2)+(x^2+y^2)-2\bigl(x\,T(P)\cdot T(e_1)+y\,T(P)\cdot T(e_2)\bigr)\\
&=2(x^2+y^2)-2(x\cdot x+y\cdot y)=0,
\end{aligned}
$$

where $T(P)\cdot T(e_1)=P\cdot e_1=x$ and $T(P)\cdot T(e_2)=P\cdot e_2=y$ by Step 2. A zero squared
length means $T(P)=W$. Hence $T(x,y)=xT(e_1)+yT(e_2)$ is linear, and its matrix
$A=\bigl(T(e_1)\ \ T(e_2)\bigr)$ has orthonormal columns, i.e. $A^{\mathsf T}A=I$. Additivity and scalar
multiplication now follow from linearity. $\blacksquare$

**28.** Let $A=\begin{pmatrix}a&b\\ c&d\end{pmatrix}$ with $A^{\mathsf T}A=I$.

**Determinant $+1$.** Orthogonality gives $a^2+c^2=1$ and $b^2+d^2=1$ with $(a,c)\cdot(b,d)=0$. Write
$a=\cos\theta$, $c=\sin\theta$; the unit vector orthogonal to $(a,c)$ is $\pm(-\sin\theta,\cos\theta)$.
The condition $\det A=ad-bc=1$ selects the $+$ sign, so $b=-\sin\theta$ and $d=\cos\theta$:

$$
A=\begin{pmatrix}\cos\theta&-\sin\theta\\ \sin\theta&\cos\theta\end{pmatrix}=R_\theta,
$$

a rotation (with $A=I$ when $\theta=0$).

**Determinant $-1$.** Since $A^{-1}=A^{\mathsf T}$ and also
$A^{-1}=\frac{1}{\det A}\begin{pmatrix}d&-b\\ -c&a\end{pmatrix}=-\begin{pmatrix}d&-b\\ -c&a\end{pmatrix}$,
comparing entries gives $a=-d$ and $b=c$, so

$$
A=\begin{pmatrix}a&b\\ b&-a\end{pmatrix},\qquad a^2+b^2=1 .
$$

Write $a=\cos\varphi$, $b=\sin\varphi$; then $A=S_{\varphi/2}$, the reflection in the line at angle
$\varphi/2$. Every orthogonal $2\times2$ matrix is therefore a rotation or a reflection, according to the
sign of its determinant. $\blacksquare$

**29.** Let the regular polygon have $n\ge3$ sides. Its interior angle is

$$
\alpha=\frac{(n-2)180^\circ}{n}.
$$

At each vertex of a tiling by congruent copies, $k\ge3$ tiles meet and their angles fill a full turn:

$$
k\alpha=360^\circ\quad\Longrightarrow\quad k=\frac{360}{\alpha}=\frac{2n}{n-2}=2+\frac{4}{n-2}.
$$

Because $k$ is an integer, $n-2$ divides $4$. With $n\ge3$, $n-2\ge1$, so
$n-2\in\{1,2,4\}$ and $n\in\{3,4,6\}$, giving $k=6,4,3$ respectively. Each case occurs: six equilateral
triangles, four squares, or three regular hexagons meet at every vertex, and these tilings exist. Hence
exactly three regular polygons tile. $\blacksquare$

**30.** For $n=5$, $\alpha=\frac{3\cdot180^\circ}{5}=108^\circ$, and

$$
k=\frac{360^\circ}{108^\circ}=\frac{10}{3}=3+\frac13,
$$

not an integer. Three pentagons meeting at a vertex occupy $324^\circ$, leaving a $36^\circ$ gap; four
occupy $432^\circ$ and overlap by $72^\circ$. At every vertex of any tiling by congruent regular
pentagons, some whole number $k$ of the $108^\circ$ angles must meet and fill exactly $360^\circ$, and
$108k=360$ has no integer solution. No vertex can therefore be covered correctly, so no tiling exists.
$\blacksquare$

**Remark.** Irregular pentagons *can* tile: fifteen families of convex pentagon tilings are known, the
first found by K. Reinhardt in 1918 and the complete classification finished in 2017. The obstruction
above is specifically the regular pentagon's angle, not the number five.

**31.** **Set-up.** Let $g=T_v\circ r_\ell$ with $v\parallel\ell$, $v\ne(0,0)$.

**Inverse.** Since $g^{-1}=r_\ell^{-1}\circ T_v^{-1}=r_\ell\circ T_{-v}$, and since a reflection commutes
with every translation parallel to its mirror line ($r_\ell T_w=T_w r_\ell$ whenever $w\parallel\ell$ —
both sides give "shift by $w$ inside the mirror"), we may rewrite

$$
g^{-1}=T_{-v}\circ r_\ell .
$$

**Identification.** This is the composition of the reflection in $\ell$ with a translation by $-v$, and
$-v$ is parallel to $\ell$ and non-zero. Therefore $g^{-1}$ is a glide reflection with the *same* axis
$\ell$ and glide vector $-v$.

**Check.** $(T_{-v}r_\ell)\circ(T_vr_\ell)=T_{-v}(r_\ell T_v)r_\ell=T_{-v}T_vr_\ell r_\ell=\operatorname{id}$.
Concretely, for $g(x,y)=(x+3,-y)$, the inverse is $g^{-1}(x,y)=(x-3,-y)$, which is the glide with the
same axis and glide vector $(-3,0)$. $\blacksquare$

## Challenge

**32.** **Set-up.** Let $\Lambda$ be a lattice with a basis of two non-parallel vectors $u,w$; every lattice
point is $mu+nw$ with $m,n\in\mathbb{Z}$. Suppose a rotation $R$ about a lattice point (taken as the
origin) maps $\Lambda$ onto itself.

**Integer matrix.** Because $R$ maps lattice vectors to lattice vectors, there are integers $a,b,c,d$ with

$$
R(u)=au+bw,\qquad R(w)=cu+dw .
$$

In the basis $\{u,w\}$ the linear map $R$ therefore has the integer matrix
$M=\begin{pmatrix}a&c\\ b&d\end{pmatrix}$.

**Trace.** The trace is basis-independent and equals $a+d$. But the trace of a rotation through
$\theta$ is also $2\cos\theta$. Hence $2\cos\theta=a+d\in\mathbb{Z}$.

**Conclusion.** Since $\lvert\cos\theta\rvert\le1$, we have $2\cos\theta\in\{-2,-1,0,1,2\}$, so
$\cos\theta\in\{-1,-\tfrac12,0,\tfrac12,1\}$ and

$$
\theta\in\{180^\circ,\ 120^\circ,\ 90^\circ,\ 60^\circ,\ 0^\circ\},
$$

whose orders are $2,3,4,6,1$ respectively. No other rotational order is compatible with a periodic
lattice: in particular five-fold and eight-fold rotations are impossible. $\blacksquare$

The argument is the standard "crystallographic restriction"; the same computation in three dimensions
gives the same list.

**33.** **Exactly four elements.** Let $R$ be a non-square rectangle with centre $O$, and let $T$ be a symmetry.
Vertices must map to vertices, so $T$ permutes the four vertices; also $T$ fixes $O$, since $O$ is the
unique point equidistant from all four vertices.

*Rotations.* A rotation about $O$ mapping the rectangle to itself must map the pair of long sides to
itself. The rotation through $90^\circ$ would map a long side to a short side, impossible since the
rectangle is not a square. Only the identity and the half-turn qualify.

*Reflections.* A reflection symmetry must fix the vertex set. The two axes through $O$ parallel to the
sides do qualify. A reflection in a diagonal does not: it swaps the two long sides with the two short
sides, so it maps the rectangle to a different quadrilateral unless the rectangle is a square. Hence
there are exactly two reflections.

So $\operatorname{Sym}(R)=\{\operatorname{id},\ h,\ s_1,\ s_2\}$ with $h$ the half-turn and $s_1,s_2$ the
two reflections: **four elements**.

**Commutativity.** Each element is its own inverse ($h^2=s_1^2=s_2^2=\operatorname{id}$), and
$h=s_2\circ s_1=s_1\circ s_2$ (composition of two perpendicular reflections is the half-turn about their
intersection, and perpendicular reflections commute in the sense that either order gives the same
half-turn). Checking the six pairs: $\operatorname{id}$ commutes with everything; $h$ commutes with
$s_1,s_2$ by the relation above; $s_1$ commutes with $s_2$ likewise. Hence the group is abelian, and it
is the Klein four-group $\mathbb{Z}/2\times\mathbb{Z}/2$. $\blacksquare$

**34.** **Set-up.** Let $s_1=r_{\ell_1}$ and $s_2=r_{\ell_2}$ be the two reflections, and let $O=\ell_1\cap\ell_2$.

**The composite is a symmetry.** Since $s_1(F)=F$ and $s_2(F)=F$,
$$(s_2\circ s_1)(F)=s_2\bigl(s_1(F)\bigr)=s_2(F)=F,$$
so the composite is again a symmetry of $F$.

**The composite is a rotation by $2\theta$.** By Theorem 7.7 (or Exercise 26), the composition of the
reflections in two lines meeting at angle $\theta$ is the rotation about $O$ through $2\theta$. Briefly: a
ray from $O$ at angle $\phi$ to $\ell_1$ goes, under $s_1$, to angle $2\alpha-\phi$ (where $\alpha$ is
the direction of $\ell_1$), and under $s_2$ to $2\beta-(2\alpha-\phi)=\phi+2(\beta-\alpha)$ with
$\beta-\alpha=\theta$. Every ray is turned by the same amount and $O$ is fixed, so the map is
$R_{O,2\theta}$.

**Conclusion.** $F$ is invariant under $R_{O,2\theta}$: a rotational symmetry of order dividing
$360^\circ/(2\theta)$.

**Perpendicular axes.** If $\theta=90^\circ$ then $2\theta=180^\circ$, so $F$ is invariant under the
half-turn about $O$. $\blacksquare$

**35.** **A glide has no fixed points.** Let $g=T_v\circ r_\ell$ with $v\parallel\ell$, $v\ne0$. Suppose
$g(P)=P$. Apply $r_\ell$ to both sides: $r_\ell g(P)=r_\ell(P)$. But
$r_\ell g=r_\ell T_v r_\ell = T_v$ (the reflection commutes with translations parallel to $\ell$), so
$T_v(P)=r_\ell(P)$. Applying $g$ again, or comparing distances, is unnecessary: it is cleaner to note
that $g^2=T_{2v}\ne\operatorname{id}$, and if $g$ had a fixed point then $g^2$ would fix it too, whereas
$T_{2v}$ has no fixed point. Hence $g$ has none. $\blacksquare$

**Conversely.** Let $T$ be an orientation-reversing isometry with no fixed point. By the classification
form, $T(X)=AX+b$ with $A$ orthogonal and $\det A=-1$. By Exercise 28, $A$ is a reflection matrix; after
rotating coordinates (an isometry that does not change the type of $T$), we may take
$A=\begin{pmatrix}1&0\\0&-1\end{pmatrix}$. Write $b=(b_1,b_2)$. Then

$$
T(x,y)=(x+b_1,\ -y+b_2).
$$

**Fixed points.** Solving $T(x,y)=(x,y)$ gives $b_1=0$ from the first coordinate and $y=b_2/2$ from the
second. So if $b_1=0$, the fixed set is the horizontal line $y=b_2/2$, and $T$ is the reflection in that
line. Since $T$ is assumed to have *no* fixed point, $b_1\ne0$.

**Identification.** Write $r(x,y)=(x,\ b_2-y)$, the reflection in the line $y=b_2/2$. Then

$$
T(x,y)=(x+b_1,\ b_2-y)=T_{(b_1,0)}\bigl(r(x,y)\bigr),
$$

and $(b_1,0)$ is parallel to the axis $y=b_2/2$. Therefore $T$ is the composition of a reflection and a
non-zero translation parallel to the mirror: a glide reflection. $\blacksquare$
