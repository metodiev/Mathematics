# Vectors — Solutions

> [Tutorial](README.md) · [Exercises](exercises.md) · 36 worked solutions

Each solution names the strategy, carries out every significant step, and checks the result — by a
second method, by substitution, or by an estimate. Where a problem admits a second approach, it is shown
or described.

## Beginner

### Solution 1

Add and subtract corresponding components:

$$\mathbf{a}+\mathbf{b}=(3-2,\;-1+4,\;2+1)=(1,3,3),$$
$$\mathbf{a}-\mathbf{b}=(3+2,\;-1-4,\;2-1)=(5,-5,1).$$

For the combination, scale first and then add:
$2\mathbf{a}=(6,-2,4)$ and $3\mathbf{b}=(-6,12,3)$, so
$$2\mathbf{a}+3\mathbf{b}=(6-6,\;-2+12,\;4+3)=(0,10,7).$$

Finally $\lVert\mathbf{a}\rVert=\sqrt{9+1+4}=\sqrt{14}$. Check: $\mathbf{a}+\mathbf{b}$ and
$\mathbf{a}-\mathbf{b}$ have the same first component as predicted by the parallelogram picture
($(1,3,3)+(5,-5,1)=(6,-2,4)=2\mathbf{a}$).

### Solution 2

$$\lVert\mathbf{v}\rVert=\sqrt{36+4+9}=\sqrt{49}=7,$$
so the unit vector is
$$\hat{\mathbf{v}}=\left(\frac67,-\frac27,\frac37\right),$$
and the opposite one is $\left(-\frac67,\frac27,-\frac37\right)$. Verification: the squared length is
$(36+4+9)/49=49/49=1$ in both cases. A unit vector is never obtained by dividing by $\lVert\mathbf{v}\rVert^2$;
the division must be by the length itself.

### Solution 3

(a) $(2,-1,3)\cdot(4,2,-2)=8-2-6=0$, so the vectors are perpendicular.

(b) $(1,2)\cdot(3,4)=3+8=11$. Not perpendicular; the dot product is positive, so the angle is acute.
Indeed
$$\cos\theta=\frac{11}{\sqrt{5}\cdot5}=\frac{11}{5\sqrt5}\approx0.984>0,$$
so $\theta\approx10.3^\circ$: the vectors point almost the same way. This is the consistency check the
question asks for — a positive dot product and an acute angle are the same statement.

### Solution 4

(a) $(1,1,0)\cdot(1,0,1)=1$, and the norms are $\sqrt2$ and $\sqrt2$. Hence
$\cos\theta=1/2$ and $\theta=60^\circ$.

(b) $(1,2,2)\cdot(2,1,-2)=2+2-4=0$. Both vectors are non-zero, so $\theta=90^\circ$: they are
perpendicular. Check with Pythagoras:
$\lVert(1,2,2)+(2,1,-2)\rVert^2=\lVert(3,3,0)\rVert^2=18=9+9$. $\checkmark$

### Solution 5

A zero cross product is the test for parallel vectors (Theorem 7.12(6)).

(a) $(1,-2,3)\times(-2,4,-6)=(12-12,\;-6+6,\;4-4)=(0,0,0)$: parallel. Indeed
$(-2,4,-6)=-2(1,-2,3)$.

(b) $(1,2,3)\times(2,3,4)=(8-9,\;6-4,\;3-4)=(-1,2,-1)\ne\mathbf{0}$: not parallel.

(c) $(0,0,1)\times(0,0,-5)=(0,-0,0)=\mathbf{0}$: parallel; $(0,0,-5)=-5(0,0,1)$.

### Solution 6

(a) Expand componentwise:
$$(1,2,3)\times(4,5,6)=\bigl(2\cdot6-3\cdot5,\;\;3\cdot4-1\cdot6,\;\;1\cdot5-2\cdot4\bigr)=(-3,6,-3).$$
Check perpendicularity:
$$(-3,6,-3)\cdot(1,2,3)=-3+12-9=0,\qquad (-3,6,-3)\cdot(4,5,6)=-12+30-18=0.$$

(b) $(2,-1,0)\times(1,0,3)=\bigl((-1)\cdot3-0\cdot0,\;\;0\cdot1-2\cdot3,\;\;2\cdot0-(-1)\cdot1\bigr)=(-3,-6,1)$.
Check: $(-3,-6,1)\cdot(2,-1,0)=-6+6=0$ and $(-3,-6,1)\cdot(1,0,3)=-3+3=0$.

### Solution 7

For consecutive vertices $A,B,C$, the fourth vertex satisfies $D=A+C-B$:
$$D=(1+5-4,\;1+5-2)=(2,4).$$
Check: $\overrightarrow{AB}=(3,1)$ and $\overrightarrow{DC}=C-D=(3,1)$, so $AB$ and $DC$ are equal and
parallel, which is exactly the parallelogram condition. Also $\overrightarrow{BC}=(1,3)=\overrightarrow{AD}$.

### Solution 8

(a) Midpoint: average the coordinates,
$$\left(\frac{1+7}{2},\;\frac{-2+4}{2},\;\frac{3-3}{2}\right)=(4,1,0).$$

(b) The displacement is $Q-P=(6,6,-6)$, so one third of the way from $P$ is
$$P+\tfrac13(6,6,-6)=(1+2,\;-2+2,\;3-2)=(3,0,1).$$
Check: this point is $(2,2,-2)$ from $P$ and $(4,4,-4)=2(2,2,-2)$ from $Q$, so the ratio is $1:2$ as
required.

### Solution 9

The normal form is $2(x-1)-(y-2)+4(z-3)=0$. Expanding,
$$2x-2-y+2+4z-12=0 \quad\Longrightarrow\quad 2x-y+4z=12.$$
Check the given point: $2-2+12=12$. $\checkmark$ On the $z$-axis $x=y=0$, so $4z=12$, $z=3$: the plane
meets the $z$-axis at $(0,0,3)$.

### Solution 10

(a) Parametric equations:
$$x=2+t,\qquad y=-1+3t,\qquad z=4-2t.$$

(b) At $t=2$: $(4,5,0)$.

(c) From the first equation $2+t=5$ gives $t=3$; then $y=-1+9=8$ and $z=4-6=-2$, both matching the
candidate point. So $(5,8,-2)$ lies on the line. (If one coordinate had failed, the point would not be on
the line: all three must agree on the same $t$.)

### Solution 11

$$W=\mathbf{F}\cdot\mathbf{d}=2\cdot4+(-3)\cdot1+1\cdot(-2)=8-3-2=3.$$
The work is positive because the angle between $\mathbf{F}$ and $\mathbf{d}$ is acute:
$$\cos\theta=\frac{3}{\sqrt{14}\sqrt{21}}\approx0.175>0.$$
A positive value means the force has a component along the displacement, so it adds energy.

### Solution 12

$$\mathbf{u}+\mathbf{v}=(4,3,-1), \qquad \lVert\mathbf{u}+\mathbf{v}\rVert^2=16+9+1=26,$$
$$\mathbf{u}-\mathbf{v}=(2,-1,1), \qquad \lVert\mathbf{u}-\mathbf{v}\rVert^2=4+1+1=6.$$
Hence $\lVert\mathbf{u}+\mathbf{v}\rVert=\sqrt{26}$ and $\lVert\mathbf{u}-\mathbf{v}\rVert=\sqrt6$. The
parallelogram law reads
$$26+6=32 \quad\text{and}\quad 2\lVert\mathbf{u}\rVert^2+2\lVert\mathbf{v}\rVert^2=2(9+1)+2(1+4+1)=20+12=32,$$
so both sides agree. $\checkmark$

## Intermediate

### Solution 13

(a) $\mathbf{u}\cdot\mathbf{v}=\lVert\mathbf{u}\rVert\lVert\mathbf{v}\rVert\cos60^\circ=2\cdot3\cdot\tfrac12=3$.

(b) $\lVert\mathbf{u}+\mathbf{v}\rVert^2=\lVert\mathbf{u}\rVert^2+2\mathbf{u}\cdot\mathbf{v}+\lVert\mathbf{v}\rVert^2=4+6+9=19$,
so $\lVert\mathbf{u}+\mathbf{v}\rVert=\sqrt{19}$.

(c) $\lVert\mathbf{u}-\mathbf{v}\rVert^2=4-6+9=7$, so $\lVert\mathbf{u}-\mathbf{v}\rVert=\sqrt7$.

(d) Expand the dot product of the two diagonals:
$$(\mathbf{u}+\mathbf{v})\cdot(\mathbf{u}-\mathbf{v})=\lVert\mathbf{u}\rVert^2-\lVert\mathbf{v}\rVert^2=4-9=-5.$$
Hence
$$\cos\varphi=\frac{-5}{\sqrt{19}\sqrt7}=\frac{-5}{\sqrt{133}}\approx-0.434,$$
so $\varphi\approx115.7^\circ$. Because $\lVert\mathbf{u}\rVert\ne\lVert\mathbf{v}\rVert$, the two
diagonals are not perpendicular — the parallelogram is not a rhombus (compare Exercise 28).

### Solution 14

Compute $\mathbf{u}\cdot\mathbf{v}=3+2-4=1$ and $\mathbf{v}\cdot\mathbf{v}=1+4+4=9$. Then
$$\operatorname{proj}_{\mathbf{v}}\mathbf{u}=\frac{1}{9}(1,2,2)=\left(\frac19,\frac29,\frac29\right),$$
and the remainder is
$$\mathbf{w}=\mathbf{u}-\operatorname{proj}_{\mathbf{v}}\mathbf{u}
=\left(\frac{27-1}{9},\frac{9-2}{9},\frac{-18-2}{9}\right)
=\left(\frac{26}{9},\frac79,-\frac{20}{9}\right).$$
Check orthogonality:
$$\mathbf{w}\cdot\mathbf{v}=\frac{26}{9}+\frac{14}{9}-\frac{40}{9}=0.$$
Check the sum:
$\operatorname{proj}_{\mathbf{v}}\mathbf{u}+\mathbf{w}=(27/9,\,9/9,\,-18/9)=(3,1,-2)=\mathbf{u}$. The
scalar component is $1/3>0$, so the projection points along $\mathbf{v}$.

### Solution 15

Perpendicularity means the dot product vanishes:
$$(2,\lambda,3)\cdot(1,-2,4)=2-2\lambda+12=14-2\lambda=0 \quad\Longrightarrow\quad \lambda=7.$$
Check: $(2,7,3)\cdot(1,-2,4)=2-14+12=0$. $\checkmark$

### Solution 16

Place the cube at $[0,1]^3$. Two space diagonals are represented by $\mathbf{d}_1=(1,1,1)$ and
$\mathbf{d}_2=(1,1,-1)$ (the second runs from $(0,0,1)$ to $(1,1,0)$). Then
$$\mathbf{d}_1\cdot\mathbf{d}_2=1+1-1=1,\qquad \lVert\mathbf{d}_1\rVert=\lVert\mathbf{d}_2\rVert=\sqrt3,$$
so
$$\cos\theta=\frac{1}{3},\qquad \theta=\arccos\tfrac13\approx70.53^\circ.$$
The other pair of space diagonals, $(1,1,1)$ and $(-1,-1,1)$, gives $\cos\theta=-1/3$; the *angle between
the lines* is the acute one, obtained by taking the absolute value, again $\arccos(1/3)$. The choice of
directions along the diagonals does not change the angle between the lines.

### Solution 17

Use two edge vectors from $A$:
$$\overrightarrow{AB}=(-1,1,0),\qquad \overrightarrow{AC}=(-1,0,1).$$
Their cross product is
$$\overrightarrow{AB}\times\overrightarrow{AC}
=\bigl(1\cdot1-0\cdot0,\;\;0\cdot(-1)-(-1)\cdot1,\;\;(-1)\cdot0-1\cdot(-1)\bigr)=(1,1,1),$$
with norm $\sqrt3$. Hence
$$\text{area}=\tfrac12\sqrt3\approx0.866.$$
Check by Heron: the three sides are $\sqrt2,\sqrt2,\sqrt2$, an equilateral triangle of side $\sqrt2$,
whose area is $\frac{\sqrt3}{4}(\sqrt2)^2=\frac{\sqrt3}{2}$. $\checkmark$

### Solution 18

Take $\overrightarrow{PQ}=(-1,2,0)$ and $\overrightarrow{PR}=(-1,0,3)$, then
$$\mathbf{n}=\overrightarrow{PQ}\times\overrightarrow{PR}
=\bigl(2\cdot3-0\cdot0,\;\;0\cdot(-1)-(-1)\cdot3,\;\;(-1)\cdot0-2\cdot(-1)\bigr)=(6,3,2).$$
The plane through $P$ is
$$6(x-1)+3(y-0)+2(z-0)=0 \quad\Longrightarrow\quad 6x+3y+2z=6.$$
Check the other two points: $Q$ gives $0+6+0=6$ and $R$ gives $0+0+6=6$. $\checkmark$

### Solution 19

With $\mathbf{n}=(2,-1,2)$, $d=4$ and $(x_0,y_0,z_0)=(2,-1,3)$,
$$d=\frac{\lvert2\cdot2+(-1)(-1)+2\cdot3-4\rvert}{\sqrt{4+1+4}}
=\frac{\lvert4+1+6-4\rvert}{3}=\frac{7}{3}\approx2.33.$$
The numerator is not zero, so the point does not lie on the plane; the distance is positive as expected.

### Solution 20

A point of the line is $(1+2t,\,2-t,\,t)$. Substituting into $x+y+z=5$:
$$(1+2t)+(2-t)+t=3+2t=5 \quad\Longrightarrow\quad t=1.$$
The intersection is $(3,1,1)$. Check: $3+1+1=5$, and the point lies on the line at $t=1$. $\checkmark$

### Solution 21

(a) The normals are $\mathbf{n}_1=(1,2,2)$ and $\mathbf{n}_2=(1,0,0)$. Then
$$\cos\theta=\frac{1}{3\cdot1}=\frac13,\qquad \theta=\arccos\tfrac13\approx70.53^\circ.$$

(b) For a line and a plane we use the sine of the angle with the normal:
$$\sin\theta=\frac{\lvert(2,1,2)\cdot(1,1,0)\rvert}{3\sqrt2}=\frac{3}{3\sqrt2}=\frac{1}{\sqrt2},$$
so $\theta=45^\circ$. Note that the angle with the normal is also $45^\circ$ here, which is not a
coincidence: when the angle is $45^\circ$ it equals its own complement.

### Solution 22

With $\mathbf{r}=(2,0,-1)$ and $\mathbf{F}=(1,2,3)$,
$$\boldsymbol{\tau}=\mathbf{r}\times\mathbf{F}
=\bigl(0\cdot3-(-1)\cdot2,\;\;(-1)\cdot1-2\cdot3,\;\;2\cdot2-0\cdot1\bigr)=(2,-7,4).$$
Checks: $\boldsymbol{\tau}\cdot\mathbf{r}=4+0-4=0$ and $\boldsymbol{\tau}\cdot\mathbf{F}=2-14+12=0$, so
the torque is perpendicular to both factors. Its magnitude is
$\sqrt{4+49+16}=\sqrt{69}\approx8.31$.

### Solution 23

A vector orthogonal to both given vectors is their cross product:
$$\mathbf{a}\times\mathbf{b}=(1,0,1)\times(0,1,1)
=\bigl(0\cdot1-1\cdot1,\;\;1\cdot0-1\cdot1,\;\;1\cdot1-0\cdot0\bigr)=(-1,-1,1).$$
Its length is $\sqrt3$, so the unit vectors in that direction are $\pm\frac{1}{\sqrt3}(-1,-1,1)$, and the
vectors of length $5$ are
$$\pm\frac{5}{\sqrt3}(-1,-1,1).$$
Check orthogonality: $(-1,-1,1)\cdot(1,0,1)=0$ and $(-1,-1,1)\cdot(0,1,1)=0$. These are the only ones
because the orthogonal complement of two independent vectors is one-dimensional.

## Advanced

### Solution 24

Expand both squares:

$$\lVert\mathbf{u}+\mathbf{v}\rVert^2=\lVert\mathbf{u}\rVert^2+2\,\mathbf{u}\cdot\mathbf{v}+\lVert\mathbf{v}\rVert^2,$$
$$\lVert\mathbf{u}-\mathbf{v}\rVert^2=\lVert\mathbf{u}\rVert^2-2\,\mathbf{u}\cdot\mathbf{v}+\lVert\mathbf{v}\rVert^2.$$

Adding, the mixed terms cancel:
$$\lVert\mathbf{u}+\mathbf{v}\rVert^2+\lVert\mathbf{u}-\mathbf{v}\rVert^2=2\lVert\mathbf{u}\rVert^2+2\lVert\mathbf{v}\rVert^2,$$
which is the parallelogram law. Subtracting instead gives
$$\lVert\mathbf{u}+\mathbf{v}\rVert^2-\lVert\mathbf{u}-\mathbf{v}\rVert^2=4\,\mathbf{u}\cdot\mathbf{v},$$
which is the polarization identity
$\mathbf{u}\cdot\mathbf{v}=\tfrac14(\lVert\mathbf{u}+\mathbf{v}\rVert^2-\lVert\mathbf{u}-\mathbf{v}\rVert^2)$.
It says that the dot product is determined by the norm: if you know the length of every sum and
difference, you know every dot product.

Geometrically, the parallelogram law states that the squares of the two diagonals of a parallelogram add
to the squares of the four sides (each side used twice).

### Solution 25

**Cauchy–Schwarz.** If $\mathbf{v}=\mathbf{0}$, both sides of
$\lvert\mathbf{u}\cdot\mathbf{v}\rvert\le\lVert\mathbf{u}\rVert\lVert\mathbf{v}\rVert$ vanish. Otherwise,
for every real $t$,
$$0\le\lVert\mathbf{u}+t\mathbf{v}\rVert^2=\lVert\mathbf{u}\rVert^2+2t(\mathbf{u}\cdot\mathbf{v})+t^2\lVert\mathbf{v}\rVert^2.$$
The right side is a quadratic in $t$ with leading coefficient $\lVert\mathbf{v}\rVert^2>0$ that never takes
negative values, so its discriminant satisfies
$$4(\mathbf{u}\cdot\mathbf{v})^2-4\lVert\mathbf{u}\rVert^2\lVert\mathbf{v}\rVert^2\le0,$$
which is exactly the inequality.

**Equality.** Equality in Cauchy–Schwarz means the discriminant is zero, so the quadratic has a double root
$t_0$ and $\lVert\mathbf{u}+t_0\mathbf{v}\rVert=0$, hence $\mathbf{u}=-t_0\mathbf{v}$; conversely scalar
multiples give equality.

**Triangle inequality.** Expanding,
$$\lVert\mathbf{u}+\mathbf{v}\rVert^2=\lVert\mathbf{u}\rVert^2+2\mathbf{u}\cdot\mathbf{v}+\lVert\mathbf{v}\rVert^2
\le\lVert\mathbf{u}\rVert^2+2\lVert\mathbf{u}\rVert\lVert\mathbf{v}\rVert+\lVert\mathbf{v}\rVert^2
=(\lVert\mathbf{u}\rVert+\lVert\mathbf{v}\rVert)^2,$$
and taking square roots gives $\lVert\mathbf{u}+\mathbf{v}\rVert\le\lVert\mathbf{u}\rVert+\lVert\mathbf{v}\rVert$.
Equality requires both equality in Cauchy–Schwarz and $\mathbf{u}\cdot\mathbf{v}\ge0$, which together say
that one vector is a *non-negative* multiple of the other.

**Why the angle formula needs it.** The formula
$\cos\theta=(\mathbf{u}\cdot\mathbf{v})/(\lVert\mathbf{u}\rVert\lVert\mathbf{v}\rVert)$ presupposes that the
quotient lies in $[-1,1]$, since $\arccos$ is defined only there. Cauchy–Schwarz is precisely that
statement, so without it the definition of angle would be circular.

### Solution 26

Write $\mathbf{u}\times\mathbf{v}=(u_2v_3-u_3v_2,\;u_3v_1-u_1v_3,\;u_1v_2-u_2v_1)$ and expand:

$$\begin{aligned}
\lVert\mathbf{u}\times\mathbf{v}\rVert^2
&=(u_2v_3-u_3v_2)^2+(u_3v_1-u_1v_3)^2+(u_1v_2-u_2v_1)^2\\
&=u_2^2v_3^2+u_3^2v_2^2+u_3^2v_1^2+u_1^2v_3^2+u_1^2v_2^2+u_2^2v_1^2\\
&\qquad-2\bigl(u_2u_3v_2v_3+u_1u_3v_1v_3+u_1u_2v_1v_2\bigr).
\end{aligned}$$

On the other hand,

$$\begin{aligned}
\lVert\mathbf{u}\rVert^2\lVert\mathbf{v}\rVert^2-(\mathbf{u}\cdot\mathbf{v})^2
&=(u_1^2+u_2^2+u_3^2)(v_1^2+v_2^2+v_3^2)-(u_1v_1+u_2v_2+u_3v_3)^2\\
&=u_2^2v_3^2+u_3^2v_2^2+u_3^2v_1^2+u_1^2v_3^2+u_1^2v_2^2+u_2^2v_1^2\\
&\qquad-2\bigl(u_2u_3v_2v_3+u_1u_3v_1v_3+u_1u_2v_1v_2\bigr),
\end{aligned}$$

because the three pure terms $u_1^2v_1^2,u_2^2v_2^2,u_3^2v_3^2$ cancel against the corresponding terms of
the square. The two expressions are identical, proving Lagrange's identity.

Now use the cosine formula $\mathbf{u}\cdot\mathbf{v}=\lVert\mathbf{u}\rVert\lVert\mathbf{v}\rVert\cos\theta$:

$$\lVert\mathbf{u}\times\mathbf{v}\rVert^2=\lVert\mathbf{u}\rVert^2\lVert\mathbf{v}\rVert^2(1-\cos^2\theta)
=\lVert\mathbf{u}\rVert^2\lVert\mathbf{v}\rVert^2\sin^2\theta.$$

Since $0\le\theta\le\pi$, we have $\sin\theta\ge0$, so taking square roots gives
$\lVert\mathbf{u}\times\mathbf{v}\rVert=\lVert\mathbf{u}\rVert\lVert\mathbf{v}\rVert\sin\theta$. This also
proves the area interpretation: base times height of the spanned parallelogram.

### Solution 27

First a lemma, verified by expanding both sides into the same six terms:
$$(\mathbf{a}\times\mathbf{b})\cdot\mathbf{c}=\mathbf{a}\cdot(\mathbf{b}\times\mathbf{c}).$$
Indeed both equal $a_1b_2c_3-a_1b_3c_2+a_2b_3c_1-a_2b_1c_3+a_3b_1c_2-a_3b_2c_1$.

**Sign change under a swap.** Using the lemma and antisymmetry of the cross product,
$$[\mathbf{v},\mathbf{u},\mathbf{w}]=\mathbf{v}\cdot(\mathbf{u}\times\mathbf{w})
=(\mathbf{v}\times\mathbf{u})\cdot\mathbf{w}=-(\mathbf{u}\times\mathbf{v})\cdot\mathbf{w}
=-\mathbf{u}\cdot(\mathbf{v}\times\mathbf{w})=-[\mathbf{u},\mathbf{v},\mathbf{w}].$$
The same argument handles any transposition.

**Cyclic invariance.** A cyclic shift is two swaps, hence two sign changes:
$$[\mathbf{u},\mathbf{v},\mathbf{w}]=-[\mathbf{v},\mathbf{u},\mathbf{w}]=[\mathbf{v},\mathbf{w},\mathbf{u}],$$
and likewise $[\mathbf{v},\mathbf{w},\mathbf{u}]=[\mathbf{w},\mathbf{u},\mathbf{v}]$.

**Geometry.** The three vectors span the same parallelepiped whichever face is called the base, so the
absolute volume cannot change; cyclic relabelling preserves orientation and hence the sign. A transposition
reverses orientation — it is a mirror image — so the signed volume changes sign while the absolute volume
does not.

### Solution 28

Let the parallelogram have vertices $A,B,C,D$ in order, and put
$\mathbf{a}=\overrightarrow{AB}$, $\mathbf{b}=\overrightarrow{AD}$. Then
$\overrightarrow{AC}=\mathbf{a}+\mathbf{b}$ and $\overrightarrow{BD}=\mathbf{b}-\mathbf{a}$.

Compute
$$(\mathbf{a}+\mathbf{b})\cdot(\mathbf{b}-\mathbf{a})
=\mathbf{a}\cdot\mathbf{b}-\lVert\mathbf{a}\rVert^2+\lVert\mathbf{b}\rVert^2-\mathbf{b}\cdot\mathbf{a}
=\lVert\mathbf{b}\rVert^2-\lVert\mathbf{a}\rVert^2.$$

Therefore the diagonals are perpendicular if and only if $\lVert\mathbf{a}\rVert=\lVert\mathbf{b}\rVert$,
that is, if and only if two adjacent sides are equal. A parallelogram with two equal adjacent sides has
all four sides equal (opposite sides are equal in any parallelogram), so it is a rhombus. Conversely, in a
rhombus $\lVert\mathbf{a}\rVert=\lVert\mathbf{b}\rVert$ and the diagonals are perpendicular.

Note that a square is a special case, but so is a diamond-shaped rhombus: perpendicular diagonals, not
right angles, are what characterise a rhombus among parallelograms.

### Solution 29

Let $\Pi=\{\mathbf{x}:\mathbf{n}\cdot\mathbf{x}=d\}$ and let $\mathbf{q}$ be any point. Choose
$\mathbf{p}\in\Pi$; such a point exists because $\mathbf{n}\ne\mathbf{0}$ (if $n_1\ne0$, take
$\mathbf{p}=(d/n_1,0,0)$). Decompose
$$\mathbf{q}-\mathbf{p}=\operatorname{proj}_{\mathbf{n}}(\mathbf{q}-\mathbf{p})+\mathbf{w},
\qquad \mathbf{w}\cdot\mathbf{n}=0.$$
The vector $\mathbf{w}$ is parallel to the plane, so changing $\mathbf{p}$ along the plane does not change
the first term; the normal component is the same for every choice of $\mathbf{p}$. Moving from $\mathbf{q}$
to any point of the plane changes the parallel part but not the normal part, so by Pythagoras the
distance is minimised when the parallel part is zero. Hence

$$d(\mathbf{q},\Pi)=\bigl\lVert\operatorname{proj}_{\mathbf{n}}(\mathbf{q}-\mathbf{p})\bigr\rVert
=\frac{\lvert\mathbf{n}\cdot(\mathbf{q}-\mathbf{p})\rvert}{\lVert\mathbf{n}\rVert}
=\frac{\lvert\mathbf{n}\cdot\mathbf{q}-d\rvert}{\lVert\mathbf{n}\rVert}.$$

**Where $\mathbf{n}\ne\mathbf{0}$ is used.** Three times: to know the plane is non-empty (a point
$\mathbf{p}$ exists), to divide by $\lVert\mathbf{n}\rVert$, and to have a direction in which to project.
If $\mathbf{n}=\mathbf{0}$, the equation reads $0=d$: the set is empty when $d\ne0$ and all of
$\mathbb{R}^3$ when $d=0$, and no distance formula applies.

### Solution 30

Let $M_a=(\mathbf{b}+\mathbf{c})/2$ be the midpoint of $BC$. The median from $A$ consists of the points
$$\mathbf{a}+t(M_a-\mathbf{a}),\qquad t\in\mathbb{R}.$$
At $t=\tfrac23$:
$$\mathbf{a}+\tfrac23\left(\frac{\mathbf{b}+\mathbf{c}}{2}-\mathbf{a}\right)
=\mathbf{a}+\frac{\mathbf{b}+\mathbf{c}}{3}-\frac{2\mathbf{a}}{3}
=\frac{\mathbf{a}+\mathbf{b}+\mathbf{c}}{3}=\mathbf{g}.$$
The same computation with the labels permuted shows that $\mathbf{g}$ lies on the median from $B$ and on
the median from $C$. Hence all three medians pass through $\mathbf{g}$, which is therefore their common
point — the *centroid*.

Because $t=\tfrac23$, the centroid is two thirds of the way from each vertex to the opposite midpoint; the
remaining third is from the midpoint to the centroid, so the median is divided in the ratio $2:1$ from the
vertex.

### Solution 31

**(a)** Suppose $\mathbf{u}\cdot\mathbf{x}=0$ for every $\mathbf{x}$. Take $\mathbf{x}=\mathbf{u}$:
$\lVert\mathbf{u}\rVert^2=\mathbf{u}\cdot\mathbf{u}=0$, and a sum of squares is zero only when every term
is zero, so $\mathbf{u}=\mathbf{0}$.

**(b)** Let $\Pi$ be a plane, and suppose $\mathbf{n}$ and $\mathbf{n}'$ are both normals: every direction
vector of $\Pi$ is orthogonal to both. A plane contains two independent direction vectors
$\mathbf{d}_1,\mathbf{d}_2$; otherwise it would be a line or a point. Put $\mathbf{m}=\mathbf{d}_1\times\mathbf{d}_2\ne\mathbf{0}$,
since the directions are not parallel.

Apply the vector triple product identity of Section 7.9 to $\mathbf{n}$:
$$\mathbf{n}\times\mathbf{m}=\mathbf{n}\times(\mathbf{d}_1\times\mathbf{d}_2)
=(\mathbf{n}\cdot\mathbf{d}_2)\mathbf{d}_1-(\mathbf{n}\cdot\mathbf{d}_1)\mathbf{d}_2=\mathbf{0}.$$
A vanishing cross product with $\mathbf{m}\ne\mathbf{0}$ means $\mathbf{n}$ is parallel to $\mathbf{m}$
(Theorem 7.12(6)), so $\mathbf{n}=\lambda\mathbf{m}$ for some $\lambda\ne0$. The same argument gives
$\mathbf{n}'=\lambda'\mathbf{m}$, hence $\mathbf{n}'=(\lambda'/\lambda)\mathbf{n}$. So the normal direction
is unique up to a non-zero scalar factor, and the equation $\mathbf{n}\cdot\mathbf{x}=d$ is unique up to
multiplying $\mathbf{n}$ and $d$ by the same non-zero number.

## Challenge

### Solution 32

**The identity.** Write $\mathbf{v}\times\mathbf{w}=(v_2w_3-v_3w_2,\;v_3w_1-v_1w_3,\;v_1w_2-v_2w_1)$.
The first component of $\mathbf{u}\times(\mathbf{v}\times\mathbf{w})$ is

$$\begin{aligned}
u_2(v_1w_2-v_2w_1)-u_3(v_3w_1-v_1w_3)
&=u_2v_1w_2-u_2v_2w_1-u_3v_3w_1+u_3v_1w_3.
\end{aligned}$$

The first component of $(\mathbf{u}\cdot\mathbf{w})\mathbf{v}-(\mathbf{u}\cdot\mathbf{v})\mathbf{w}$ is

$$\begin{aligned}
&(u_1w_1+u_2w_2+u_3w_3)v_1-(u_1v_1+u_2v_2+u_3v_3)w_1\\
&\quad=u_1v_1w_1+u_2v_1w_2+u_3v_1w_3-u_1v_1w_1-u_2v_2w_1-u_3v_3w_1\\
&\quad=u_2v_1w_2+u_3v_1w_3-u_2v_2w_1-u_3v_3w_1,
\end{aligned}$$

which is identical. The second and third components follow by cyclic relabelling of the indices
$(1,2,3)\to(2,3,1)\to(3,1,2)$; the computation is the same in each case. Hence
$$\mathbf{u}\times(\mathbf{v}\times\mathbf{w})=(\mathbf{u}\cdot\mathbf{w})\mathbf{v}-(\mathbf{u}\cdot\mathbf{v})\mathbf{w}.$$

**Jacobi identity.** Apply the identity to each term:

$$\mathbf{u}\times(\mathbf{v}\times\mathbf{w})=(\mathbf{u}\cdot\mathbf{w})\mathbf{v}-(\mathbf{u}\cdot\mathbf{v})\mathbf{w},$$
$$\mathbf{v}\times(\mathbf{w}\times\mathbf{u})=(\mathbf{v}\cdot\mathbf{u})\mathbf{w}-(\mathbf{v}\cdot\mathbf{w})\mathbf{u},$$
$$\mathbf{w}\times(\mathbf{u}\times\mathbf{v})=(\mathbf{w}\cdot\mathbf{v})\mathbf{u}-(\mathbf{w}\cdot\mathbf{u})\mathbf{v}.$$

The coefficients of $\mathbf{u}$ are $-(\mathbf{v}\cdot\mathbf{w})+(\mathbf{w}\cdot\mathbf{v})=0$, those of
$\mathbf{v}$ are $(\mathbf{u}\cdot\mathbf{w})-(\mathbf{w}\cdot\mathbf{u})=0$, and those of $\mathbf{w}$ are
$-(\mathbf{u}\cdot\mathbf{v})+(\mathbf{v}\cdot\mathbf{u})=0$. Summing gives $\mathbf{0}$.

### Solution 33

**Derivation.** Let $L_1=\{\mathbf{p}_1+t\mathbf{d}_1\}$ and $L_2=\{\mathbf{p}_2+s\mathbf{d}_2\}$ be skew,
and put $\mathbf{n}=\mathbf{d}_1\times\mathbf{d}_2\ne\mathbf{0}$. For any $t,s$ the vector joining the two
lines is
$$\mathbf{w}=(\mathbf{p}_2+s\mathbf{d}_2)-(\mathbf{p}_1+t\mathbf{d}_1).$$
Since $\mathbf{d}_1\cdot\mathbf{n}=\mathbf{d}_2\cdot\mathbf{n}=0$, we have
$\mathbf{w}\cdot\mathbf{n}=(\mathbf{p}_2-\mathbf{p}_1)\cdot\mathbf{n}$, a constant independent of $t,s$.
By Cauchy–Schwarz,
$$\lVert\mathbf{w}\rVert\ge\frac{\lvert\mathbf{w}\cdot\mathbf{n}\rvert}{\lVert\mathbf{n}\rVert}
=\frac{\lvert(\mathbf{p}_2-\mathbf{p}_1)\cdot\mathbf{n}\rvert}{\lVert\mathbf{n}\rVert}.$$

It remains to see that equality is attained. Choose $t,s$ so that $\mathbf{w}\perp\mathbf{d}_1$ and
$\mathbf{w}\perp\mathbf{d}_2$; this is two linear equations in $t,s$ whose coefficient matrix has
determinant $-\lVert\mathbf{d}_1\rVert^2\lVert\mathbf{d}_2\rVert^2+(\mathbf{d}_1\cdot\mathbf{d}_2)^2=-\lVert\mathbf{n}\rVert^2\ne0$,
so a solution exists and is unique. For that pair, $\mathbf{w}$ is orthogonal to both $\mathbf{d}_1$ and
$\mathbf{d}_2$, hence parallel to $\mathbf{n}$, and the bound is attained. Therefore

$$d(L_1,L_2)=\frac{\lvert(\mathbf{p}_2-\mathbf{p}_1)\cdot(\mathbf{d}_1\times\mathbf{d}_2)\rvert}{\lVert\mathbf{d}_1\times\mathbf{d}_2\rVert}.$$

**Application.** For $L_1$: $\mathbf{p}_1=(1,2,3)$, $\mathbf{d}_1=(1,0,1)$. For $L_2$:
$\mathbf{p}_2=(0,1,2)$, $\mathbf{d}_2=(0,1,1)$. If the lines met, then
$(1+t,\,2,\,3+t)=(0,\,1+s,\,2+s)$ for some $t,s$. The first coordinate gives $t=-1$, the second $s=1$, and
then the third reads $2=3$, which is false. The directions are not parallel because
$$\mathbf{d}_1\times\mathbf{d}_2=(1,0,1)\times(0,1,1)=\bigl(0-1,\;0-1,\;1-0\bigr)=(-1,-1,1)\ne\mathbf{0}.$$
So the lines are skew. Finally $\mathbf{p}_2-\mathbf{p}_1=(-1,-1,-1)$ and
$$d=\frac{\lvert(-1,-1,-1)\cdot(-1,-1,1)\rvert}{\sqrt3}
=\frac{\lvert1+1-1\rvert}{\sqrt3}=\frac{1}{\sqrt3}=\frac{\sqrt3}{3}\approx0.577.$$

### Solution 34

Since $\mathbf{w}=-\mathbf{u}-\mathbf{v}$,

$$\mathbf{v}\times\mathbf{w}=\mathbf{v}\times(-\mathbf{u}-\mathbf{v})=-\mathbf{v}\times\mathbf{u}-\mathbf{v}\times\mathbf{v}
=\mathbf{u}\times\mathbf{v},$$
using $\mathbf{v}\times\mathbf{v}=\mathbf{0}$ and antisymmetry. Similarly
$$\mathbf{w}\times\mathbf{u}=(-\mathbf{u}-\mathbf{v})\times\mathbf{u}=-\mathbf{v}\times\mathbf{u}=\mathbf{u}\times\mathbf{v}.$$
Hence all three cross products are equal.

**Interpretation.** The equation $\mathbf{u}+\mathbf{v}+\mathbf{w}=\mathbf{0}$ says that the three vectors,
placed head to tail, close up into a triangle. Twice the area of that triangle is
$\lVert\mathbf{u}\times\mathbf{v}\rVert$, and the identity says the same number is obtained from
$\mathbf{v}\times\mathbf{w}$ and from $\mathbf{w}\times\mathbf{u}$ — as it must be, since the three choices
are just relabellings of the same pair of sides. In particular
$$\lVert\mathbf{u}\times\mathbf{v}\rVert=\lVert\mathbf{v}\times\mathbf{w}\rVert=\lVert\mathbf{w}\times\mathbf{u}\rVert,$$
and all three point the same way (not merely have the same length), as the computation shows.

### Solution 35

Take the regular tetrahedron with vertices
$$A(1,1,1),\quad B(1,-1,-1),\quad C(-1,1,-1),\quad D(-1,-1,1),$$
whose pairwise squared distances are all $8$, so all edges have length $2\sqrt2$.

Consider the dihedral angle along the edge $AB$. Its midpoint is $M=(A+B)/2=(1,0,0)$. In the face $ABC$,
the vector from $M$ perpendicular to $AB$ is
$$\mathbf{p}=C-M=(-2,1,-1);$$
in the face $ABD$, the corresponding vector is
$$\mathbf{q}=D-M=(-2,-1,1).$$
Both are perpendicular to $AB=(0,2,2)$: indeed $\mathbf{p}\cdot(0,2,2)=2-2=0$ and
$\mathbf{q}\cdot(0,2,2)=-2+2=0$. The dihedral angle $\theta$ is the angle between these two vectors in the
plane perpendicular to the edge, so

$$\cos\theta=\frac{\mathbf{p}\cdot\mathbf{q}}{\lVert\mathbf{p}\rVert\lVert\mathbf{q}\rVert}
=\frac{4-1-1}{\sqrt6\sqrt6}=\frac{2}{6}=\frac{1}{3}.$$

Hence $\theta=\arccos(1/3)\approx70.53^\circ$. Equivalently, the outward normals to the two faces make the
supplementary angle $\arccos(-1/3)\approx109.47^\circ$.

### Solution 36

**(a)** Take the base to be the triangle $OBC$, whose area is $\tfrac12\lVert\mathbf{b}\times\mathbf{c}\rVert$.
The height from $\mathbf{a}$ to the plane of $OBC$ is the length of the component of $\mathbf{a}$ along the
normal $\mathbf{b}\times\mathbf{c}$:
$$h=\frac{\lvert\mathbf{a}\cdot(\mathbf{b}\times\mathbf{c})\rvert}{\lVert\mathbf{b}\times\mathbf{c}\rVert}.$$
The volume of a tetrahedron is one third of base area times height:
$$V=\frac13\cdot\frac12\lVert\mathbf{b}\times\mathbf{c}\rVert\cdot
\frac{\lvert\mathbf{a}\cdot(\mathbf{b}\times\mathbf{c})\rvert}{\lVert\mathbf{b}\times\mathbf{c}\rVert}
=\frac{\lvert[\mathbf{a},\mathbf{b},\mathbf{c}]\rvert}{6}.$$
This also shows that the volume is one sixth of the parallelepiped on the same three edges, a fact
consistent with a cube being decomposed into six congruent tetrahedra by its three space diagonals.

**(b)** With $A(1,0,0)$, $B(0,1,0)$, $C(0,0,1)$, $D(1,1,1)$ and origin $O$,
$$\overrightarrow{OA}=(1,0,0),\quad \overrightarrow{OB}=(0,1,0),\quad \overrightarrow{OC}=(0,0,1),$$
so $[\overrightarrow{OA},\overrightarrow{OB},\overrightarrow{OC}]=1$ and the tetrahedron $OABC$ has
volume $\tfrac16$. (This is the corner tetrahedron of the unit cube.) For $ABCD$ use the same origin and
the three edges from $A$:
$$\overrightarrow{AB}=(-1,1,0),\quad \overrightarrow{AC}=(-1,0,1),\quad \overrightarrow{AD}=(0,1,1).$$
Compute
$$\overrightarrow{AC}\times\overrightarrow{AD}
=\bigl(0\cdot1-1\cdot1,\;\;1\cdot0-(-1)\cdot1,\;\;(-1)\cdot1-0\cdot0\bigr)=(-1,1,-1),$$
so
$$[\overrightarrow{AB},\overrightarrow{AC},\overrightarrow{AD}]
=(-1)(-1)+1\cdot1+0\cdot(-1)=2,$$
and $V=2/6=1/3$.

**(c)** Let $D=(1,1,k)$, so $\overrightarrow{AD}=(0,1,k)$ and
$$\overrightarrow{AC}\times\overrightarrow{AD}
=\bigl(0\cdot k-1\cdot1,\;\;1\cdot0-(-1)k,\;\;(-1)\cdot1-0\cdot0\bigr)=(-1,k,-1).$$
Then
$$[\overrightarrow{AB},\overrightarrow{AC},\overrightarrow{AD}]
=(-1)(-1)+1\cdot k+0\cdot(-1)=1+k,$$
which vanishes exactly when $k=-1$. So $D=(1,1,-1)$ makes the four points coplanar, and for every other
$k$ they form a genuine tetrahedron of volume $\lvert1+k\rvert/6$. In particular $k=1$ gives $1/3$, agreeing
with part (b).
