# Coordinate Geometry — Solutions

> [Tutorial](README.md) · [Exercises](exercises.md) · 35 worked solutions

Each solution names the strategy, carries out every significant step, and checks the result — by a
second method, by substitution, or by a sketch-level estimate. Where a problem admits a second
approach, it is shown or described.

## Beginner

**1.** $\Delta x=6-2=4$ and $\Delta y=4-1=3$, so
$$d=\sqrt{4^2+3^2}=\sqrt{25}=\boxed{5}.$$
Check: $(4,3)$ is a $3$–$4$–$5$ triangle, and the sketch confirms a short segment in the first quadrant.

**2.** The midpoint is the average of the coordinates:
$$M=\left(\frac{-3+7}{2},\frac{5+(-1)}{2}\right)=\left(\frac42,\frac42\right)=\boxed{(2,2)}.$$
Check: $(-3,5)\to(2,2)$ is $(5,-3)$ and $(2,2)\to(7,-1)$ is $(5,-3)$; the two halves are equal vectors,
so $M$ is indeed the midpoint.

**3.** With $O(0,0)$ and $P(5,-12)$,
$$d=\sqrt{(5-0)^2+(-12-0)^2}=\sqrt{25+144}=\sqrt{169}=\boxed{13}.$$
This is the $5$–$12$–$13$ triangle; the negative sign of the $y$-coordinate does not matter, because both
coordinates are squared.

**4.**

$$m=\frac{7-(-1)}{6-2}=\frac{8}{4}=\boxed{2}.$$
Check: going $2$ right from $(2,-1)$ should go $4$ up, giving $(4,3)$; the line through $(2,-1)$ and
$(6,7)$ does pass through $(4,3)$ since $(4,3)$ is the midpoint of the two given points.

**5.** Point-slope form with $(x_1,y_1)=(1,-2)$ and $m=3$:
$$y-(-2)=3(x-1)\quad\Longrightarrow\quad \boxed{y+2=3(x-1)}.$$
Expanding: $y+2=3x-3$, so
$$\boxed{y=3x-5}.$$
Check: at $x=1$, $y=3-5=-2$, as required; the $y$-intercept is $-5$.

**6.** Substitute $x=3$, $y=5$ into the left-hand side:
$$2(3)-3(5)+9=6-15+9=0.$$
The result is $0$, so the point **does** lie on the line: $\boxed{\text{yes}}$.

**7.** (a) Both lines have slope $2$, and their $y$-intercepts $1$ and $-3$ differ, so they are **parallel**
(and distinct).

(b) The slopes are $2$ and $-\tfrac12$, and $2\cdot\left(-\tfrac12\right)=-1$, so the lines are
**perpendicular**.

(c) The slopes are $3$ and $-3$. They are not equal, so not parallel; their product is $-9\ne-1$, so not
perpendicular. The pair is **neither** (they are mirror images across the $y$-axis).

**8.** The intercepts are $x=5$ and $y=-2$, so intercept form is
$$\frac{x}{5}+\frac{y}{-2}=1.$$
Multiplying by $10$: $2x-5y=10$, so the general form is $\boxed{2x-5y-10=0}$.
From $y=\tfrac25x-2$ the slope is $\boxed{\tfrac25}$, matching $-\frac{A}{B}=-\frac{2}{-5}$.

**9.** Here $A=4$, $B=-3$, $C=5$ and $(x_0,y_0)=(2,-1)$:
$$d=\frac{\lvert 4(2)-3(-1)+5\rvert}{\sqrt{16+9}}=\frac{\lvert 8+3+5\rvert}{5}=\boxed{\frac{16}{5}}=3.2.$$
Check: the line passes through $(1,3)$, since $4(1)-3(3)+5=0$, and $\lvert(2,-1)-(1,3)\rvert=\sqrt{17}\approx4.12$
exceeds $3.2$ — as the distance to any point of the line must. The distance from $(2,-1)$ to the origin is
$\sqrt5\approx2.24$, and the line's distance from the origin is $5/5=1$, so a point-to-line distance of
about $3.2$ is consistent with the sketch.

**10.** Standard form: $\boxed{(x-2)^2+(y+3)^2=25}$.
Expanding: $x^2-4x+4+y^2+6y+9=25$, hence
$$\boxed{x^2+y^2-4x+6y-12=0}.$$
Check with the coefficient test: $D^2+E^2-4F=16+36+48=100$, so $r=\tfrac12\sqrt{100}=5$, correct.

**11.** Complete both squares:
$$\begin{aligned}
x^2-8x+y^2+2y+8&=0\\
(x^2-8x+16)+(y^2+2y+1)&=-8+16+1\\
(x-4)^2+(y+1)^2&=9 .
\end{aligned}$$
So the centre is $\boxed{(4,-1)}$ and the radius is $\boxed{3}$. Check: $D=-8$, $E=2$, $F=8$ give
$D^2+E^2-4F=64+4-32=36$ and $r=\tfrac12\sqrt{36}=3$. The point $(1,-1)$ satisfies the original equation
($1+1-8-2+8=0$) and is $3$ units from $(4,-1)$.

**12.** The vertical line through $(4,-2)$ is $x=4$; its slope is **undefined** (there is no $\Delta x$). The
horizontal line is $y=-2$; its slope is $0$.

## Intermediate

**13.** Use Theorem 7.3 with $m=2$, $n=1$, $P(-3,2)$, $Q(6,-4)$:
$$x=\frac{1(-3)+2(6)}{3}=\frac{9}{3}=3,\qquad y=\frac{1(2)+2(-4)}{3}=\frac{-6}{3}=-2.$$
The point is $\boxed{(3,-2)}$. Check: $R-P=(6,-4)$ and $Q-R=(3,-2)=\tfrac12(6,-4)$, so $PR:RQ=2:1$.

**14.** With $m=2$, $n=3$, $A(-1,2)$, $B(5,10)$:
$$x=\frac{3(-1)+2(5)}{5}=\frac{7}{5},\qquad y=\frac{3(2)+2(10)}{5}=\frac{26}{5}.$$
So $P=\boxed{\left(\tfrac75,\tfrac{26}5\right)}$. Check: $\overrightarrow{AP}=\left(\tfrac{12}{5},\tfrac{16}{5}\right)$
and $\overrightarrow{PB}=\left(\tfrac{18}{5},\tfrac{24}{5}\right)=\tfrac32\left(\tfrac{12}{5},\tfrac{16}{5}\right)$,
so the ratio of lengths is $2:3$.

**15.** Solve for $y$: $5y=-2x+10$, so
$$y=-\frac25x+2,$$
giving slope $\boxed{-\tfrac25}$ and $y$-intercept $\boxed{2}$. Setting $y=0$ gives $2x=10$, so
$x=5$: the $x$-intercept is $\boxed{5}$. Intercept form:
$$\frac{x}{5}+\frac{y}{2}=1.$$
Check: multiplying by $10$ gives $2x+5y=10$, i.e. $2x+5y-10=0$, the original equation.

**16.** From $4x+y=7$, the slope is $-4$. A parallel line has the same slope, so through $(3,-1)$:
$$y+1=-4(x-3)\quad\Longrightarrow\quad y=-4x+12-1=-4x+11,$$
that is $\boxed{4x+y=11}$. Check: $(3,-1)$ gives $12-1=11$, and the coefficient vector $(4,1)$ matches
the original, as parallel lines must.

**17.** The midpoint of the segment is
$$M=\left(\frac{1+7}{2},\frac{2+10}{2}\right)=(4,6).$$
The segment's slope is $\frac{10-2}{7-1}=\frac86=\frac43$, so the perpendicular bisector has slope
$-\frac34$. Through $(4,6)$:
$$y-6=-\frac34(x-4)\quad\Longrightarrow\quad 4y-24=-3x+12\quad\Longrightarrow\quad 3x+4y=36.$$
The answer is $\boxed{3x+4y-36=0}$. Check: the two endpoints are equidistant from the line:
$\frac{\lvert 3+8-36\rvert}{5}=\frac{25}{5}=5$ and $\frac{\lvert 21+40-36\rvert}{5}=\frac{25}{5}=5$.

**18.** Both equations already share the coefficients $(5,-12)$; write them as $5x-12y-6=0$ and
$5x-12y-32=0$. Then
$$d=\frac{\lvert-32-(-6)\rvert}{\sqrt{25+144}}=\frac{26}{13}=\boxed{2}.$$
Check: $(6,2)$ lies on the first line since $30-24=6$, and its distance to the second is
$\frac{\lvert 30-24-32\rvert}{13}=\frac{26}{13}=2$, as required.

**19.** From $2x-4y=7$ we get $y=\tfrac12x-\tfrac74$, so its slope is $\tfrac12$. A perpendicular must have slope
$-2$. Write the first line as $3y=-kx+6$, i.e. $y=-\frac{k}{3}x+2$, whose slope is $-\frac{k}{3}$.
Therefore
$$-\frac{k}{3}=-2\quad\Longrightarrow\quad \boxed{k=6}.$$
Check: $6x+3y=6$ has slope $-2$, and $(-2)\cdot\tfrac12=-1$.

**20.** Use the shoelace formula with $(1,1)$, $(5,2)$, $(3,6)$:
$$\begin{aligned}
2\cdot\text{area}&=\lvert x_1(y_2-y_3)+x_2(y_3-y_1)+x_3(y_1-y_2)\rvert\\
&=\lvert 1(2-6)+5(6-1)+3(1-2)\rvert\\
&=\lvert -4+25-3\rvert=18 .
\end{aligned}$$
So the area is $\boxed{9}$. Check by subtracting right triangles from the bounding rectangle
$1\le x\le5$, $1\le y\le6$ (area $20$): the three corner triangles have areas $2$, $6$ and $3$, and
$20-11=9$.

**21.** The centre is the midpoint of the diameter:
$$C=\left(\frac{1+7}{2},\frac{3+11}{2}\right)=(4,7).$$
The radius is half the diameter:
$$r=\frac12\sqrt{(7-1)^2+(11-3)^2}=\frac12\sqrt{36+64}=\frac{10}{2}=5.$$
Hence $\boxed{(x-4)^2+(y-7)^2=25}$. Check: $(1,3)$ gives $9+16=25$ and $(7,11)$ gives $9+16=25$.

**22.** Substitute $y=x-1$ into $x^2+y^2=25$:
$$\begin{aligned}
x^2+(x-1)^2&=25\\
x^2+x^2-2x+1&=25\\
2x^2-2x-24&=0\\
x^2-x-12&=0\\
(x-4)(x+3)&=0 .
\end{aligned}$$
So $x=4$ or $x=-3$. With $y=x-1$ these give the points $\boxed{(4,3)}$ and $\boxed{(-3,-4)}$.
Check: $16+9=25$ and $9+16=25$, and both satisfy $y=x-1$.

## Advanced

**23.** **Given.** $A(x_1,y_1)$, $B(x_2,y_2)$, $C(x_3,y_3)$; $M$ is the midpoint of $AB$, $N$ the midpoint of
$AC$. **To prove.** $MN\parallel BC$ and $\lvert MN\rvert=\frac12\lvert BC\rvert$.

By Theorem 7.2,

$$
M=\left(\frac{x_1+x_2}{2},\frac{y_1+y_2}{2}\right),\qquad
N=\left(\frac{x_1+x_3}{2},\frac{y_1+y_3}{2}\right).
$$

Subtract coordinatewise:

$$
\overrightarrow{MN}=\left(\frac{x_1+x_3-x_1-x_2}{2},\frac{y_1+y_3-y_1-y_2}{2}\right)
=\left(\frac{x_3-x_2}{2},\frac{y_3-y_2}{2}\right)=\tfrac12\overrightarrow{BC}.
$$

Since $\overrightarrow{MN}$ is a positive scalar multiple of $\overrightarrow{BC}$, the segments are
parallel. Taking lengths, $\lvert MN\rvert=\tfrac12\lvert BC\rvert$. Nothing was assumed about the shape
of the triangle, so the result holds for every triangle; the computation also shows that $MN$ and $BC$
have the same direction, not merely parallel lines. $\blacksquare$

**Remark.** The converse is also true and follows from the same formula: the line through the midpoint
of $AB$ parallel to $BC$ must meet $AC$ at its midpoint, since the parameter $\tfrac12$ is forced.

**24.** **Setting.** Let $A,B,C,D$ be four points, no three collinear, named in order around the quadrilateral,
so that $AC$ and $BD$ are the diagonals.

**($\Rightarrow$) If the diagonals bisect each other, the figure is a parallelogram.**
The common midpoint condition gives $\frac{A+C}{2}=\frac{B+D}{2}$, hence

$$
A+C=B+D\quad\Longrightarrow\quad B-A=C-D\quad\text{and}\quad D-A=C-B .
$$

The first equation says $\overrightarrow{AB}=\overrightarrow{DC}$: the sides $AB$ and $DC$ are parallel
and equal. The second says $\overrightarrow{AD}=\overrightarrow{BC}$: the sides $AD$ and $BC$ are
parallel and equal. Both pairs of opposite sides are parallel, which is the definition of a
parallelogram.

**($\Leftarrow$) If the figure is a parallelogram, the diagonals bisect each other.**
In a parallelogram, diagonal $AC$ splits it into triangles $ABC$ and $CDA$. The alternate angles give
$\angle BAC=\angle DCA$ and $\angle BCA=\angle DAC$, and $AC$ is common, so the triangles are congruent
by ASA. Hence $\lvert AB\rvert=\lvert DC\rvert$. Because $AB\parallel DC$ and the vertices are named in
order, the vectors $\overrightarrow{AB}$ and $\overrightarrow{DC}$ point the same way, so equal lengths
force $\overrightarrow{AB}=\overrightarrow{DC}$, i.e. $B-A=C-D$, i.e. $A+C=B+D$. Therefore the
midpoints $\frac{A+C}{2}$ and $\frac{B+D}{2}$ coincide.

**Where the "in order" hypothesis is used.** It identifies which segments are sides and which are
diagonals, and it fixes the *orientation* in the last step. Without it, $AB$ and $DC$ could be parallel
and equal as segments while pointing in opposite directions ($\overrightarrow{AB}=-\overrightarrow{DC}$),
which describes a crossed or differently labelled figure rather than a parallelogram. With the
orientation fixed, equal parallel sides give equal vectors, and the midpoints coincide.
$\blacksquare$

**25.** Let $A$, $B$, $C$ be the vertices, and let $M_A=\frac{B+C}{2}$ be the midpoint of $BC$. Define

$$
G=\frac{A+B+C}{3}.
$$

**Step 1: $G$ lies on the median from $A$ and divides it $2:1$.** Since $G=\frac{A+2M_A}{3}$, Theorem 7.3
with $m:n=2:1$ says $G$ divides the segment $AM_A$ in the ratio $AG:GM_A=2:1$. Explicitly,

$$
G=A+\frac23(M_A-A)=A+\frac23\left(\frac{B+C}{2}-A\right)
=\frac{3A+B+C-2A}{3}=\frac{A+B+C}{3}. \checkmark
$$

**Step 2: the same point lies on the other medians.** The expression $\frac{A+B+C}{3}$ is unchanged by
permuting $A,B,C$. Relabelling the vertices, the identical argument shows that $G$ lies on the median
from $B$ (dividing it $2:1$) and on the median from $C$ (dividing it $2:1$).

**Conclusion.** All three medians pass through the single point $G$, so they are concurrent, and each
median is divided $2:1$ measured from its vertex. $\blacksquare$

The essential device is writing the candidate point in a *symmetric* form: concurrence then costs
nothing, whereas intersecting the medians pairwise would require two separate computations and a
comparison.

**26.** **Parallelogram part.** Let $A,B,C,D$ be the vertices in order and $P,Q,R,S$ the midpoints of $AB$,
$BC$, $CD$, $DA$. Then

$$
\overrightarrow{PQ}=Q-P=\frac{B+C}{2}-\frac{A+B}{2}=\frac{C-A}{2},
\qquad
\overrightarrow{SR}=R-S=\frac{C+D}{2}-\frac{D+A}{2}=\frac{C-A}{2}.
$$

So $\overrightarrow{PQ}=\overrightarrow{SR}$; by Theorem 7.16, $PQRS$ is a parallelogram. Note also
$\overrightarrow{QR}=R-Q=\frac{D-B}{2}$, so the sides of $PQRS$ are half the diagonals of $ABCD$:

$$
\lvert PQ\rvert=\tfrac12\lvert AC\rvert,\qquad \lvert QR\rvert=\tfrac12\lvert BD\rvert,
$$

and $PQ\parallel AC$, $QR\parallel BD$.

**Area part.** Assume $ABCD$ convex and let its diagonals meet at $O$ at angle $\theta$. The diagonals
split $ABCD$ into four triangles with vertex $O$; each has angle $\theta$ or $\pi-\theta$ at $O$, and
both have the same sine. Hence

$$
[ABCD]=\tfrac12\sin\theta\,(AO\cdot BO+BO\cdot CO+CO\cdot DO+DO\cdot AO)
=\tfrac12\sin\theta\,(AO+CO)(BO+DO)=\tfrac12\,\lvert AC\rvert\,\lvert BD\rvert\sin\theta .
$$

For the parallelogram $PQRS$, the sides are $\tfrac12\lvert AC\rvert$ and $\tfrac12\lvert BD\rvert$ and
the angle between them is the same $\theta$ (corresponding angles between parallel lines). Therefore

$$
[PQRS]=\tfrac12\cdot\tfrac12\lvert AC\rvert\cdot\tfrac12\lvert BD\rvert\sin\theta
=\tfrac14\cdot\tfrac12\lvert AC\rvert\lvert BD\rvert\sin\theta
=\tfrac12[ABCD]. \qquad\blacksquare
$$

**Check.** For the square with vertices $(\pm1,\pm1)$, the quadrilateral has area $4$ and the Varignon
figure is the square with vertices $(0,\pm1),(\pm1,0)$, of area $2$. Agreement.

**27.** **Foot.** The given line $x+2y-7=0$ has slope $-\tfrac12$, so the perpendicular through $(3,4)$
has slope $2$:

$$
y-4=2(x-3)\quad\Longrightarrow\quad y=2x-2 .
$$

Solving with $x+2y=7$ (the given line): $x+2(2x-2)=7$, so $5x=11$, $x=\tfrac{11}{5}$, and
$y=2\cdot\tfrac{11}{5}-2=\tfrac{12}{5}$. The foot is $\boxed{\left(\tfrac{11}{5},\tfrac{12}{5}\right)}$.

**Distance.** By Theorem 7.9,

$$
d=\frac{\lvert 3+2(4)-7\rvert}{\sqrt{1+4}}=\frac{4}{\sqrt5}=\frac{4\sqrt5}{5}\approx1.789 .
$$

**Verification 1 (direct).** $\overrightarrow{PF}=\left(\tfrac{11}{5}-3,\tfrac{12}{5}-4\right)=\left(-\tfrac45,-\tfrac85\right)$,
whose length is
$\sqrt{\tfrac{16}{25}+\tfrac{64}{25}}=\sqrt{\tfrac{80}{25}}=\tfrac{4\sqrt5}{5}$, matching.

**Verification 2 (perpendicularity).** The slope of $PF$ is $\dfrac{-8/5}{-4/5}=2$, the negative
reciprocal of $-\tfrac12$, so $PF\perp l$. Since $F\in l$ and $PF\perp l$, the length $\lvert PF\rvert$
is the distance from $P$ to $l$.

**28.** **Step 1: the perpendicular bisector of the two points.** The midpoint of $(7,2)$ and $(3,4)$ is
$(5,3)$, and the segment's slope is $\frac{4-2}{3-7}=-\tfrac12$. The bisector has slope $2$:

$$
y-3=2(x-5)\quad\Longrightarrow\quad y=2x-7 .
$$

**Step 2: intersect with the constraint.** Setting $2x-7=x-3$ gives $x=4$ and $y=1$. The centre is
$C(4,1)$.

**Step 3: radius.**

$$
r^2=(7-4)^2+(2-1)^2=9+1=10,\qquad r=\sqrt{10} .
$$

The circle is $\boxed{(x-4)^2+(y-1)^2=10}$, or $x^2+y^2-8x-2y+7=0$ in general form.

**Check.** For $(3,4)$: $(3-4)^2+(4-1)^2=1+9=10$. For $(7,2)$: $9+1=10$. The centre satisfies
$1=4-3$, as required. General-form coefficients: $D^2+E^2-4F=64+4-28=40$, so
$r=\tfrac12\sqrt{40}=\sqrt{10}$. $\checkmark$

**29.** Let $(a,b)$ satisfy $a^2+b^2=r^2$, and let $l$ be the line $ax+by=r^2$. We show that $l$ is tangent to
the circle at $(a,b)$.

**The point lies on $l$:** $a\cdot a+b\cdot b=a^2+b^2=r^2$. $\checkmark$

**Case 1: $a\ne0$ and $b\ne0$.** The radius from $(0,0)$ to $(a,b)$ has slope $b/a$. The line $l$ has
slope $-a/b$, by Theorem 7.8 with $A=a$, $B=b$. Since $\frac{b}{a}\cdot\left(-\frac{a}{b}\right)=-1$,
the radius is perpendicular to $l$, so $l$ is the tangent at $(a,b)$.

**Case 2: $a=0$.** Then $b^2=r^2$, so $b=\pm r$ and $l$ is $by=r^2$, i.e. $y=r^2/b=b=\pm r$: the
horizontal line through the top or bottom of the circle, which is plainly tangent there. The radius to
$(0,b)$ is vertical, consistent with "$l$ perpendicular to the radius".

**Case 3: $b=0$.** Symmetrically $a=\pm r$ and $l$ is the vertical line $x=\pm r$.

In every case $l$ passes through the point of the circle and is perpendicular to the radius there, so it
is the tangent. The formula $ax+by=r^2$ therefore covers all positions of the point, with no exceptional
case left over. $\blacksquare$

**30.** **Reflection argument.** Let $A'=(2,-1)$ be the reflection of $A$ in the $x$-axis. For every point
$P=(p,0)$ on the axis, $\lvert AP\rvert=\sqrt{(p-2)^2+1}=\lvert A'P\rvert$. Hence

$$
\lvert AP\rvert+\lvert PB\rvert=\lvert A'P\rvert+\lvert PB\rvert\ge\lvert A'B\rvert
$$

by the triangle inequality, with equality exactly when $A',P,B$ are collinear and $P$ lies on the segment
$A'B$.

**Locating $P$.** The line through $A'(2,-1)$ and $B(6,5)$ has slope $\frac{5-(-1)}{6-2}=\frac32$ and
equation $y+1=\tfrac32(x-2)$, i.e. $y=\tfrac32x-4$. It meets $y=0$ at $x=\tfrac83$. So
$P=\left(\tfrac83,0\right)$, which does lie between $A'$ and $B$ (its $x$-coordinate is between $2$ and
$6$).

**Minimum value.**

$$
\lvert A'B\rvert=\sqrt{(6-2)^2+(5+1)^2}=\sqrt{16+36}=\sqrt{52}=2\sqrt{13}\approx7.211 .
$$

**Direct check.** $\lvert AP\rvert=\sqrt{\tfrac49+1}=\tfrac{\sqrt{13}}{3}$ and
$\lvert PB\rvert=\sqrt{\tfrac{100}{9}+25}=\tfrac{5\sqrt{13}}{3}$, total $\tfrac{6\sqrt{13}}{3}=2\sqrt{13}$.
For $P'=(3,0)$: $\sqrt2+\sqrt{34}\approx1.414+5.831=7.245>7.211$. For $P''=(2,0)$:
$1+\sqrt{16+25}=1+\sqrt{41}\approx7.403>7.211$.

**Calculus check.** With $f(p)=\sqrt{(p-2)^2+1}+\sqrt{(p-6)^2+25}$,

$$
f'(p)=\frac{p-2}{\sqrt{(p-2)^2+1}}+\frac{p-6}{\sqrt{(p-6)^2+25}},
\qquad f'\!\left(\tfrac83\right)=\frac{2/3}{\sqrt{13}/3}+\frac{-10/3}{5\sqrt{13}/3}
=\frac{2}{\sqrt{13}}-\frac{2}{\sqrt{13}}=0,
$$

and $f''>0$ everywhere (each term has positive second derivative), so this critical point is the unique
global minimum. $\blacksquare$

## Challenge

**31.** **Signed trapezoid areas.** For a point $P$ and the next point $Q$, define

$$
S(P,Q)=\tfrac12\,(y_P+y_Q)(x_Q-x_P),
$$

the signed area of the trapezoid bounded by $PQ$, the two perpendiculars to the $x$-axis, and the axis
itself. This is positive when $Q$ is to the right of $P$ and the segment lies above the axis, and it
carries a sign in general.

**Key claim.** For a triangle $ABC$, the signed area equals $S(A,B)+S(B,C)+S(C,A)$. Reason: cut the
plane into thin vertical strips. Inside one strip, each of the three segments contributes the signed area
between the $x$-axis and that segment, the sign being that of $x_Q-x_P$. Where two boundary segments lie
one above the other, one is traversed left-to-right and the other right-to-left, so their contributions
cancel; what survives is the signed area between the lowest and the highest boundary point of the triangle
in that strip, i.e. the area of the part of the triangle inside the strip. Summing over strips gives the
area. (This is the boundary form of $\int y\,dx$.)

**Computation.** Expand the sum:

$$
\begin{aligned}
2\bigl(S(A,B)+S(B,C)+S(C,A)\bigr)
&=(y_1+y_2)(x_2-x_1)+(y_2+y_3)(x_3-x_2)+(y_3+y_1)(x_1-x_3)\\
&=y_1x_2-y_1x_1+y_2x_2-y_2x_1+y_2x_3-y_2x_2+y_3x_3-y_3x_2\\
&\qquad +y_3x_1-y_3x_3+y_1x_1-y_1x_3\\
&=y_1x_2-y_2x_1+y_2x_3-y_3x_2+y_3x_1-y_1x_3\\
&=(x_1y_2-x_2y_1)+(x_2y_3-x_3y_2)+(x_3y_1-x_1y_3)\\
&=x_1(y_2-y_3)+x_2(y_3-y_1)+x_3(y_1-y_2).
\end{aligned}
$$

Every squared term cancelled. Hence the signed area, for vertices taken anticlockwise, is

$$
[ABC]=\tfrac12\bigl(x_1(y_2-y_3)+x_2(y_3-y_1)+x_3(y_1-y_2)\bigr). \qquad\blacksquare
$$

**Clockwise.** Swapping two vertices, say $B$ and $C$, replaces the bracket by its negative (immediate
from the display), and reverses the orientation. So the formula returns the *negative* of the area when
the vertices are listed clockwise; this is why the area statement uses the absolute value.

**Collinear.** If the three points are collinear, the triangle has zero area, so the bracket is $0$. The
converse is the useful direction: the bracket vanishing *characterises* collinearity (for points in the
plane), giving the collinearity test of §8.

**Check.** For $(0,0)$, $(4,0)$, $(0,3)$: the bracket is $0(0-3)+4(3-0)+0(0-0)=12$, half is $6$, which is
$\tfrac12\cdot4\cdot3$. $\checkmark$

**32.** **Derivation.** A point of the line $PQ$ is $P+t(Q-P)$, $t\in\mathbb{R}$: $t=0$ gives $P$, $t=1$ gives
$Q$, and $t$ outside $[0,1]$ gives points beyond the segment. Suppose $R$ is beyond $Q$, so $t>1$. Then

$$
\lvert PR\rvert=t\,\lvert PQ\rvert,\qquad \lvert RQ\rvert=(t-1)\lvert PQ\rvert,
$$

so $PR:RQ=t:(t-1)=m:n$ gives $tn=m(t-1)$, i.e. $t(n-m)=-m$, i.e.

$$
t=\frac{m}{m-n}.
$$

This has $t>1$ exactly when $m>n$, consistent with $R$ beyond $Q$. If $m<n$, the same algebra gives
$t<0$, which is the point beyond $P$, and taking absolute values in the ratio reproduces the same
condition. The formula requires $m\ne n$; when $m=n$ the ratio condition $t:(t-1)=1:1$ is impossible
(there is no external division in equal parts).

Substituting into the parametrisation:

$$
x_R=x_1+\frac{m}{m-n}(x_2-x_1)
=\frac{(m-n)x_1+mx_2-mx_1}{m-n}
=\frac{mx_2-nx_1}{m-n},
$$

and identically for $y$. $\blacksquare$

**Application.** $A(1,2)$, $B(4,8)$, $m:n=2:1$:

$$
R=\left(\frac{2(4)-1(1)}{1},\frac{2(8)-1(2)}{1}\right)=(7,14).
$$

**Check.** $\overrightarrow{AB}=(3,6)$ and $\overrightarrow{AR}=(6,12)=2\overrightarrow{AB}$, so
$\lvert AR\rvert=2\lvert AB\rvert$. Also $\overrightarrow{RB}=B-R=(-3,-6)$, of length $\lvert AB\rvert$.
Hence $AR:RB=2:1$ with $R$ beyond $B$. $\checkmark$

**33.** **Translate the condition.** $\lvert PA\rvert=2\lvert PB\rvert$ means

$$
(x-0)^2+(y-0)^2=4\bigl((x-6)^2+(y-0)^2\bigr).
$$

**Expand.**

$$
\begin{aligned}
x^2+y^2&=4(x^2-12x+36+y^2)\\
x^2+y^2&=4x^2-48x+144+4y^2\\
0&=3x^2+3y^2-48x+144\\
0&=x^2+y^2-16x+48 && \text{divide by }3.
\end{aligned}
$$

**Complete the square.**

$$
(x-8)^2-64+y^2+48=0\quad\Longrightarrow\quad (x-8)^2+y^2=16 .
$$

**Answer.** The locus is the circle with centre $(8,0)$ and radius $4$: $\boxed{(x-8)^2+y^2=16}$.

**Checks.** $P=(12,0)$ is on the circle since $(12-8)^2=16$; then $\lvert PA\rvert=12$ and
$\lvert PB\rvert=6$, a ratio of $2$. $P=(4,0)$ is on the circle since $(4-8)^2=16$; then
$\lvert PA\rvert=4$ and $\lvert PB\rvert=2$, again $2:1$. The circle is exactly the Apollonius circle
of the ratio $2:1$ with respect to $A$ and $B$; its centre lies on the line $AB$ because the
configuration is symmetric about that line.

**34.** **Set-up.** Let $A(x_1,y_1)$, $B(x_2,y_2)$, $C(x_3,y_3)$ be non-collinear. The perpendicular bisector of
$AB$ is the locus of points equidistant from $A$ and $B$:

$$
(x-x_1)^2+(y-y_1)^2=(x-x_2)^2+(y-y_2)^2 .
$$

Expanding and cancelling $x^2+y^2$ from both sides:

$$
-2xx_1-2yy_1+x_1^2+y_1^2=-2xx_2-2yy_2+x_2^2+y_2^2,
$$

i.e.

$$
2(x_2-x_1)x+2(y_2-y_1)y=x_2^2+y_2^2-x_1^2-y_1^2 .
$$

This is a line with normal vector $(x_2-x_1,\,y_2-y_1)$ — the direction vector of $AB$ — as a
perpendicular bisector should have.

**Concurrence.** Apply the same computation to the pair $A,C$, obtaining a second line with normal
$(x_3-x_1,y_3-y_1)$. Since $A,B,C$ are not collinear, the vectors $(x_2-x_1,y_2-y_1)$ and
$(x_3-x_1,y_3-y_1)$ are not parallel, so the two lines are not parallel: they meet in exactly one point
$O$.

**Equidistance.** Because $O$ lies on the bisector of $AB$, $\lvert OA\rvert=\lvert OB\rvert$; because it
lies on the bisector of $AC$, $\lvert OA\rvert=\lvert OC\rvert$. Hence
$\lvert OA\rvert=\lvert OB\rvert=\lvert OC\rvert=:\rho$. Since $O$ is equidistant from $A$ and $C$, it
also lies on the third perpendicular bisector, so all three are concurrent. Finally $\rho>0$ (the
vertices are distinct), so the circle with centre $O$ and radius $\rho$ passes through $A$, $B$ and $C$;
this is the circumcircle, and $O$ is the circumcentre. $\blacksquare$

**Check.** For $A(0,0)$, $B(4,0)$, $C(0,3)$ the bisectors are $x=2$ and $y=\tfrac32$, meeting at
$\left(2,\tfrac32\right)$, whose distance to each vertex is $\sqrt{4+\tfrac94}=\tfrac52$. The circumradius
of this right triangle is half the hypotenuse, $\tfrac12\cdot5=\tfrac52$. $\checkmark$

**35.** **Set-up.** Let the diagonals $AC$ and $BD$ bisect each other at $O$, and let $\lvert AC\rvert=\lvert BD\rvert$.
By Exercise 24 the quadrilateral is a parallelogram, so it suffices to find one right angle.

**Coordinates.** Place $O$ at the origin and write

$$
A=(p,q),\qquad C=(-p,-q),\qquad B=(r,s),\qquad D=(-r,-s),
$$

which expresses exactly that $O$ is the midpoint of both diagonals.

**Equal diagonals.**

$$
\lvert AC\rvert=2\sqrt{p^2+q^2},\qquad \lvert BD\rvert=2\sqrt{r^2+s^2},
$$

so $\lvert AC\rvert=\lvert BD\rvert$ gives $p^2+q^2=r^2+s^2$.

**Compute two adjacent sides.**

$$
\lvert AB\rvert^2=(r-p)^2+(s-q)^2,\qquad \lvert BC\rvert^2=(r+p)^2+(s+q)^2 .
$$

Adding, the cross terms cancel:

$$
\lvert AB\rvert^2+\lvert BC\rvert^2=2(r^2+s^2)+2(p^2+q^2)=4(p^2+q^2)=\lvert AC\rvert^2 .
$$

**Conclusion.** In triangle $ABC$ the side lengths satisfy $AB^2+BC^2=AC^2$, so by the converse of the
Pythagorean theorem the angle at $B$ is a right angle. A parallelogram with a right angle is a
rectangle. $\blacksquare$

**Remark.** The same computation shows more: a parallelogram is a rectangle exactly when its diagonals
are equal, the companion of the familiar fact that a parallelogram is a rhombus exactly when its
diagonals are perpendicular.

