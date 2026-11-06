# Conic Sections — Solutions

> [Tutorial](README.md) · [Exercises](exercises.md) · 34 worked solutions

Each solution states the strategy, carries out every step, and ends with an answer and a check.
Proofs state their hypotheses explicitly. Numerical answers are given exactly where possible and to
three decimal places otherwise.

## Beginner

**1.**

**Strategy.** Use the standard form $(x-h)^2+(y-k)^2 = r^2$ with $(h,k)$ the centre and $r$ the radius.

$$(x-3)^2 + \big(y-(-2)\big)^2 = 5^2 \quad\Longrightarrow\quad (x-3)^2+(y+2)^2 = 25.$$

**Answer.** $(x-3)^2+(y+2)^2 = 25$, equivalently $x^2+y^2-6x+4y-12 = 0$.

**Check.** The point $(8,-2)$ should lie on the circle: $(8-3)^2+(-2+2)^2 = 25$. $\checkmark$

**2.**

**Strategy.** Complete the square in $x$ and in $y$; the coefficients of $x^2$ and $y^2$ are both $1$, so
the circle is genuine if the right-hand side is positive.

$$(x^2-8x) + (y^2+6y) = 11.$$

Half of $-8$ is $-4$ with square $16$; half of $6$ is $3$ with square $9$. Hence

$$(x-4)^2 - 16 + (y+3)^2 - 9 = 11 \quad\Longrightarrow\quad (x-4)^2+(y+3)^2 = 36.$$

**Answer.** Centre $(4,-3)$, radius $r = 6$.

**Check.** The right-hand side is $36>0$, so the circle is genuine. The point $(10,-3)$ lies on it:
$100+9-80-18-11 = 0$. $\checkmark$

**3.**

**Strategy.** Compare with $y^2 = 4px$: the coefficient of $x$ is $4p$, and the vertex is the origin
because the equation is in standard position.

$4p = 16$, so $p = 4 > 0$ and the parabola opens to the right.

**Answer.** Vertex $(0,0)$; focus $(4,0)$; directrix $x = -4$; latus rectum $4|p| = 16$, the chord from
$(4,-8)$ to $(4,8)$.

**Check.** The latus-rectum endpoint $(4,8)$ is at distance $8$ from the focus $(4,0)$ and at distance
$4-(-4) = 8$ from the directrix. $\checkmark$

**4.**

**Strategy.** Compare with $x^2 = 4py$, which is the vertical form; here $4p = -8$.

$p = -2 < 0$, so the parabola opens downward.

**Answer.** Focus $(0,-2)$; directrix $y = 2$.

**Check.** The vertex $(0,0)$ is at distance $2$ from the focus and at distance $2$ from the line
$y = 2$. The point $(4,-2)$ lies on the curve because $16 = -8(-2)$; its distance to the focus
$(0,-2)$ is $4$, and its distance to the directrix $y = 2$ is $4$. $\checkmark$

**5.**

**Strategy.** Vertex at the origin with a vertical axis means $x^2 = 4py$; the focus is $(0,p)$, so
$p = 3$.

$$x^2 = 4\cdot 3\cdot y = 12y.$$

**Answer.** $x^2 = 12y$.

**Check.** The focus of $x^2 = 12y$ is $(0,3)$ and the directrix is $y = -3$. The latus-rectum endpoint
has $y = p = 3$, hence $x^2 = 12\cdot3 = 36$ and $x = 6$; the point $(6,3)$ is at distance $6$ from the
focus $(0,3)$ and at distance $3-(-3) = 6$ from the directrix. $\checkmark$

**6.**

**Strategy.** Read the denominators: the larger is $a^2$, and the major axis lies along that variable.

$$a^2 = 36,\quad b^2 = 16 \quad\Longrightarrow\quad a = 6,\ b = 4,\ c = \sqrt{36-16} = \sqrt{20} = 2\sqrt5 \approx 4.472.$$

**Answer.** $a = 6$, $b = 4$, $c = 2\sqrt5$; foci $(\pm2\sqrt5, 0)$; eccentricity
$e = \dfrac{2\sqrt5}{6} = \dfrac{\sqrt5}{3} \approx 0.745$.

**Check.** The vertex $(6,0)$ is at distance $6-2\sqrt5 \approx 1.528$ from the near focus and
$6+2\sqrt5 \approx 10.472$ from the far focus; the sum is $12 = 2a$. $\checkmark$

**7.**

**Strategy.** For $\dfrac{x^2}{a^2}-\dfrac{y^2}{b^2} = 1$ the relations are $c^2 = a^2+b^2$ and the
asymptotes are $y = \pm\frac{b}{a}x$.

$$a = 3,\quad b = 4,\quad c = \sqrt{9+16} = 5.$$

**Answer.** $a = 3$, $b = 4$, $c = 5$; foci $(\pm5,0)$; asymptotes $y = \pm\dfrac43 x$;
eccentricity $e = \dfrac53$.

**Check.** The vertex $(3,0)$ is at distance $5-3 = 2$ from the near focus and $3+5 = 8$ from the far
one; the difference is $6 = 2a$. $\checkmark$

**8.**

**Strategy.** The coefficients of $x^2$ and $y^2$ are equal and there is no $xy$ term, so the curve is a
circle (or degenerate). Divide by $4$ first, then complete the squares.

$$x^2+y^2-3x+2y+\tfrac14 = 0,$$

$$(x^2-3x) + (y^2+2y) = -\tfrac14,$$

$$\left(x-\tfrac32\right)^2 - \tfrac94 + (y+1)^2 - 1 = -\tfrac14,$$

$$\left(x-\tfrac32\right)^2 + (y+1)^2 = \tfrac94 + 1 - \tfrac14 = 3.$$

**Answer.** A circle with centre $\left(\tfrac32,-1\right)$ and radius $\sqrt3 \approx 1.732$.

**Check.** The right-hand side $3>0$ confirms a genuine circle. The point $\left(\tfrac32+\sqrt3,-1\right)$
is on it by construction, and substituting into the expanded form
$4x^2+4y^2-12x+8y+1 = 0$: with $x = \tfrac32+\sqrt3$ and $y=-1$,
$4\left(3+3\sqrt3+\tfrac94\right)+4-12\left(\tfrac32+\sqrt3\right)-8+1 = 12+12\sqrt3+9+4-18-12\sqrt3-8+1 = 0$.
$\checkmark$

**9.**

**Strategy.** Only $y$ is squared, so the curve is a parabola with a horizontal axis. Complete the
square in $y$.

$$y^2-4y = 8x-4 \quad\Longrightarrow\quad (y-2)^2 - 4 = 8x-4 \quad\Longrightarrow\quad (y-2)^2 = 8x.$$

This is $(y-k)^2 = 4p(x-h)$ with $h = 0$, $k = 2$ and $4p = 8$, so $p = 2$.

**Answer.** A parabola with vertex $(0,2)$, opening to the right; focus $(2,2)$; directrix $x = -2$;
latus rectum $8$.

**Check.** The point $(2,6)$ lies on it: $(6-2)^2 = 16 = 8\cdot2$. Its distance to the focus $(2,2)$
is $4$, and its distance to $x = -2$ is $4$. $\checkmark$

**10.**

**Strategy.** Foci on the $x$-axis mean a horizontal major axis. The vertices give $a$; the foci give
$c$; then $b^2 = a^2-c^2$.

Vertices $(\pm5,0)$ give $a = 5$; foci $(\pm3,0)$ give $c = 3$; hence $b^2 = 25-9 = 16$.

**Answer.** $\dfrac{x^2}{25}+\dfrac{y^2}{16} = 1$.

**Check.** The co-vertex $(0,4)$ is at distance $\sqrt{9+16} = 5 = a$ from each focus. $\checkmark$

**11.**

**Strategy.** Vertices on the $y$-axis mean a vertical transverse axis, so the positive term is
$y^2$: $\dfrac{y^2}{a^2}-\dfrac{x^2}{b^2} = 1$ with $b^2 = c^2-a^2$.

Vertices $(0,\pm2)$ give $a = 2$; foci $(0,\pm3)$ give $c = 3$; hence $b^2 = 9-4 = 5$.

**Answer.** $\dfrac{y^2}{4}-\dfrac{x^2}{5} = 1$.

**Check.** $c^2 = a^2+b^2 = 4+5 = 9$, so $c = 3$, as required. $\checkmark$

**12.**

**Strategy.** Divide by $400$ to put the right-hand side equal to $1$.

$$\frac{x^2}{25}+\frac{y^2}{16} = 1 \quad\Longrightarrow\quad a = 5,\ b = 4,\ c = \sqrt{25-16} = 3.$$

**Answer.** $e = \dfrac{c}{a} = \dfrac35 = 0.6$.

**Check.** $b = a\sqrt{1-e^2} = 5\sqrt{1-0.36} = 5(0.8) = 4$. $\checkmark$

## Intermediate

**13.**

**Strategy.** Same-sign squares, no $xy$ term: an ellipse. Complete both squares.

$$9\left(x^2+4x\right) + 4\left(y^2-2y\right) = -4,$$

$$9\left[(x+2)^2-4\right] + 4\left[(y-1)^2-1\right] = -4,$$

$$9(x+2)^2 + 4(y-1)^2 = -4+36+4 = 36,$$

$$\frac{(x+2)^2}{4}+\frac{(y-1)^2}{9} = 1.$$

The larger denominator is $9$, under $y$, so the major axis is **vertical**: $a = 3$, $b = 2$,
$c = \sqrt{9-4} = \sqrt5 \approx 2.236$, $e = \sqrt5/3 \approx 0.745$.

**Answer.** An ellipse with centre $(-2,1)$; major axis vertical of length $6$, minor axis horizontal of
length $4$; vertices $(-2,4)$ and $(-2,-2)$; co-vertices $(0,1)$ and $(-4,1)$; foci
$(-2,1\pm\sqrt5) \approx (-2,3.236)$ and $(-2,-1.236)$; eccentricity $\sqrt5/3$.

**Check.** The vertex $(-2,4)$: $9(4)+4(16)+36(-2)-8(4)+4 = 36+64-72-32+4 = 0$. $\checkmark$ The
co-vertex $(0,1)$: $0+4+0-8+4 = 0$. $\checkmark$

**14.**

**Strategy.** Opposite signs: a hyperbola. Complete both squares and divide so that the right-hand
side is $1$.

$$9\left(x^2-2x\right) - 16\left(y^2-2y\right) = 151,$$

$$9\left[(x-1)^2-1\right] - 16\left[(y-1)^2-1\right] = 151,$$

$$9(x-1)^2 - 16(y-1)^2 = 151+9-16 = 144,$$

$$\frac{(x-1)^2}{16}-\frac{(y-1)^2}{9} = 1.$$

So $a = 4$, $b = 3$, $c = \sqrt{16+9} = 5$, $e = 5/4$. The transverse axis is horizontal.

**Answer.** A hyperbola with centre $(1,1)$; vertices $(5,1)$ and $(-3,1)$; foci $(6,1)$ and $(-4,1)$;
asymptotes $y-1 = \pm\frac34(x-1)$; eccentricity $\frac54$.

**Check.** The vertex $(5,1)$: $9(25)-16(1)-18(5)+32(1)-151 = 225-16-90+32-151 = 0$. $\checkmark$ Its
distance to $(6,1)$ is $1$ and to $(-4,1)$ is $9$; the difference is $8 = 2a$. $\checkmark$

**15.**

**Strategy.** A horizontal directrix means a vertical axis. The vertex is the point of the axis midway
between focus and directrix, and $p$ is the distance from vertex to focus.

The focus $(2,3)$ and the directrix $y = -1$ are at distance $4$ apart, so the vertex lies at
$y = \frac{3+(-1)}{2} = 1$ on the line $x = 2$, and $p = \frac{4}{2} = 2$. The focus is above the
vertex, so the parabola opens upward:

$$(x-2)^2 = 4\cdot2\cdot(y-1) = 8(y-1).$$

**Answer.** Vertex $(2,1)$; equation $(x-2)^2 = 8(y-1)$; latus rectum $4|p| = 8$.

**Check.** The point $(2+4,\,1+2) = (6,3)$ satisfies $16 = 8\cdot2$. Its distance to the focus $(2,3)$
is $4$, and its distance to $y=-1$ is $4$. $\checkmark$

**16.**

**Strategy.** The foci have equal $y$, so the major axis is horizontal. The centre is the midpoint of
the foci; $c$ is half their separation; $a$ is half the major axis.

Centre $= \left(\frac{1+7}{2}, 2\right) = (4,2)$; $c = \frac{7-1}{2} = 3$; $2a = 10$ so $a = 5$; hence
$b^2 = 25-9 = 16$.

**Answer.** $\dfrac{(x-4)^2}{25}+\dfrac{(y-2)^2}{16} = 1$.

**Check.** The co-vertex $(4,6)$ is at distance $\sqrt{9+16} = 5 = a$ from the focus $(1,2)$:
$\sqrt{(4-1)^2+(6-2)^2} = \sqrt{9+16} = 5$. $\checkmark$

**17.**

**Strategy.** Foci and vertices on the $y$-axis give a vertical transverse axis:
$\dfrac{y^2}{a^2}-\dfrac{x^2}{b^2} = 1$, $b^2 = c^2-a^2$, asymptotes $y = \pm\frac{a}{b}x$.

$a = 3$, $c = 5$, so $b^2 = 25-9 = 16$ and $b = 4$.

**Answer.** $\dfrac{y^2}{9}-\dfrac{x^2}{16} = 1$; asymptotes $y = \pm\dfrac34 x$; eccentricity
$e = \dfrac53$.

**Check.** At $y = 5$ the equation gives $\dfrac{25}{9}-\dfrac{x^2}{16} = 1$, so
$x^2 = 16\cdot\dfrac{16}{9} = \dfrac{256}{9}$ and $x = \dfrac{16}{3}$. The point
$\left(\tfrac{16}{3},5\right)$ is at distance $\tfrac{16}{3}$ from the focus $(0,5)$ and at distance
$\sqrt{\tfrac{256}{9}+100} = \sqrt{\tfrac{1156}{9}} = \tfrac{34}{3}$ from $(0,-5)$; the difference is
$\tfrac{18}{3} = 6 = 2a$. $\checkmark$

**18.**

**Strategy.** Compute $\Delta = B^2-4AC$ from the coefficients of $x^2$, $xy$, $y^2$ only.

(a) $A = 5$, $B = 4$, $C = 2$: $\Delta = 16-40 = -24 < 0$ — **ellipse**.
(b) $A = 4$, $B = 12$, $C = 9$: $\Delta = 144-144 = 0$ — **parabola**.
(c) $A = 1$, $B = -6$, $C = 2$: $\Delta = 36-8 = 28 > 0$ — **hyperbola**.
(d) $A = 2$, $B = 0$, $C = 2$: $\Delta = 0-16 = -16 < 0$ — **ellipse**, and since $A = C$ with $B = 0$
it is a **circle**.

**Answer.** (a) ellipse, (b) parabola, (c) hyperbola, (d) circle.

**Check.** For (b) note $4x^2+12xy+9y^2 = (2x+3y)^2$, a perfect square — the signature of a parabola-type
equation. For (d), completing the square gives
$(x-1)^2+\left(y+\tfrac32\right)^2 = \tfrac{13}{4}$, so the radius is $\frac{\sqrt{13}}{2} \approx 1.803$,
confirming a genuine circle. $\checkmark$

**19.**

**Strategy.** Find $c$ from $c^2 = a^2-b^2$; the distance between the foci is $2c$; the latus rectum is
$2b^2/a$.

$$a^2 = 49,\quad b^2 = 24,\quad c^2 = 49-24 = 25,\quad c = 5.$$

**Answer.** Distance between foci $= 2c = 10$; latus rectum $= \dfrac{2\cdot24}{7} = \dfrac{48}{7} \approx 6.857$.

**Check.** The latus-rectum half-length is $b^2/a = 24/7 \approx 3.429$, and at $x = c = 5$ the ellipse
gives $y^2 = 24\left(1-\frac{25}{49}\right) = 24\cdot\frac{24}{49}$, so $y = \frac{24}{7}$. $\checkmark$

**20.**

**Strategy.** Write the general circle $x^2+y^2+Dx+Ey+F = 0$ and impose the three points, which gives
three linear equations in $D$, $E$, $F$.

At $(0,0)$: $F = 0$. At $(4,0)$: $16+4D = 0$, so $D = -4$. At $(0,6)$: $36+6E = 0$, so $E = -6$.

$$x^2+y^2-4x-6y = 0 \quad\Longrightarrow\quad (x-2)^2+(y-3)^2 = 13.$$

**Answer.** $x^2+y^2-4x-6y = 0$; centre $(2,3)$; radius $\sqrt{13} \approx 3.606$.

**Check.** All three points: $(0,0)$ gives $0$; $(4,0)$ gives $16-16 = 0$; $(0,6)$ gives $36-36 = 0$.
And the centre-radius form gives $(0-2)^2+(0-3)^2 = 13$. $\checkmark$

**21.**

**Strategy.** Three conditions determine $a$, $b$, $c$; then complete the square to find the vertex, and
read $p$ from the coefficient.

From $(0,1)$: $c = 1$. From $(1,0)$: $a+b+1 = 0$. From $(2,3)$: $4a+2b+1 = 3$, i.e. $4a+2b = 2$, i.e.
$2a+b = 1$. Subtracting $a+b = -1$ from $2a+b = 1$ gives $a = 2$, and then $b = -3$. So

$$y = 2x^2-3x+1 = 2\left(x^2-\tfrac32 x\right)+1 = 2\left[\left(x-\tfrac34\right)^2-\tfrac{9}{16}\right]+1 = 2\left(x-\tfrac34\right)^2 - \tfrac98+\tfrac88 = 2\left(x-\tfrac34\right)^2 - \tfrac18.$$

Hence $\left(x-\tfrac34\right)^2 = \tfrac12\left(y+\tfrac18\right)$, so $4p = \tfrac12$, $p = \tfrac18$.

**Answer.** $a = 2$, $b = -3$, $c = 1$; vertex $\left(\tfrac34,-\tfrac18\right)$; focus
$\left(\tfrac34, 0\right)$; directrix $y = -\tfrac14$.

**Check.** At the point $(0,1)$ of the parabola, the distance to the focus is
$\sqrt{\left(\tfrac34\right)^2+1} = \sqrt{\tfrac{9}{16}+1} = \sqrt{\tfrac{25}{16}} = \tfrac54$, and the
distance to the line $y = -\tfrac14$ is $1+\tfrac14 = \tfrac54$. $\checkmark$

**22.**

**Strategy.** The asymptotes $y = \pm x$ have slope $b/a = 1$, so $a = b$; a hyperbola with equal
semi-axes is rectangular. A vertical or horizontal axis gives the same relation $c^2 = a^2+b^2$.

$$c = 6,\qquad a^2+b^2 = 36,\qquad a = b \ \Longrightarrow\ 2a^2 = 36,\ a^2 = 18.$$

**Answer.** $\dfrac{x^2}{18}-\dfrac{y^2}{18} = 1$; eccentricity $e = \dfrac{6}{\sqrt{18}} = \sqrt2 \approx 1.414$.

**Check.** $\sqrt{18} \approx 4.243$, and $c = \sqrt{18+18} = 6$. $\checkmark$ For a rectangular hyperbola
$e = \sqrt2$ always, since $e^2 = (a^2+a^2)/a^2 = 2$. $\checkmark$

## Advanced

**23.**

**Strategy.** Compute $|PF_+|^2$ directly, substituting $y^2$ from the ellipse equation, and recognise a
perfect square. Then decide the sign using $|x|\le a$ and $e<1$.

Let $P = (x,y)$ satisfy $\dfrac{x^2}{a^2}+\dfrac{y^2}{b^2} = 1$, so $y^2 = b^2\left(1-\dfrac{x^2}{a^2}\right)$,
and let $c^2 = a^2-b^2$, $e = c/a$.

$$\begin{aligned}
|PF_+|^2 &= (x-c)^2+y^2 \\
&= x^2-2cx+c^2+b^2-\frac{b^2}{a^2}x^2 \\
&= x^2\left(1-\frac{b^2}{a^2}\right)-2cx+(b^2+c^2).
\end{aligned}$$

Now $1-\dfrac{b^2}{a^2} = \dfrac{a^2-b^2}{a^2} = \dfrac{c^2}{a^2} = e^2$ and $b^2+c^2 = a^2$, so

$$|PF_+|^2 = e^2x^2-2cx+a^2 = (ex-a)^2.$$

Because $P$ is on the ellipse, $-a\le x\le a$, so $ex \le ea = c < a$ and therefore $ex-a<0$. Taking
the non-negative square root,

$$|PF_+| = a-ex.$$

Replacing $c$ by $-c$ (that is, $x$ by $-x$ in the same computation) gives
$|PF_-|^2 = (ex+a)^2$, and since $ex+a>0$, $|PF_-| = a+ex$.

Adding: $|PF_+|+|PF_-| = (a-ex)+(a+ex) = 2a$. $\blacksquare$

**Answer.** $|PF_+| = a-ex$, $|PF_-| = a+ex$, and their sum is $2a$ — so every point of the standard
ellipse satisfies the two-focus definition with constant $2a$.

**Check.** At the vertex $(a,0)$: $|PF_+| = a-ea = a-c$, which is exactly the distance from $(a,0)$ to
$(c,0)$; and $|PF_-| = a+c$, the distance to $(-c,0)$. Their sum is $2a$. $\checkmark$

**24.**

**Strategy.** The same computation as Problem 23, with $b^2 = c^2-a^2$ instead of $a^2-c^2$, and the sign
decided by $x\ge a$ on the right branch.

On the hyperbola, $y^2 = b^2\left(\dfrac{x^2}{a^2}-1\right)$ and $c^2 = a^2+b^2$.

$$\begin{aligned}
|PF_+|^2 &= (x-c)^2+y^2 = x^2-2cx+c^2+\frac{b^2}{a^2}x^2-b^2 \\
&= x^2\left(1+\frac{b^2}{a^2}\right)-2cx+(c^2-b^2) = e^2x^2-2cx+a^2 = (ex-a)^2.
\end{aligned}$$

On the right branch $x\ge a$, so $ex \ge ea = c > a$ and $ex-a>0$; hence $|PF_+| = ex-a$. Replacing
$c$ by $-c$ gives $|PF_-|^2 = (ex+a)^2$ with $ex+a>0$, so $|PF_-| = ex+a$.

Subtracting: $|PF_-|-|PF_+| = (ex+a)-(ex-a) = 2a$. $\blacksquare$

**Answer.** $|PF_+| = ex-a$, $|PF_-| = ex+a$, and $|PF_-|-|PF_+| = 2a$ on the right branch. On the left
branch the roles reverse and $|PF_+|-|PF_-| = 2a$; together they give
$\big||PF_+|-|PF_-\big| = 2a$.

**Check.** At the vertex $(a,0)$: $|PF_+| = c-a$ and $|PF_-| = c+a$; their difference is $2a$. $\checkmark$

**25.**

**Strategy.** Write the quadratic part as a matrix product, observe that the change of coordinates is
the linear map $[x,y]^{\mathsf T} = R[X,Y]^{\mathsf T}$ with $R$ a rotation, and use multiplicativity
of the determinant.

Let $\mathbf{x} = (x,y)^{\mathsf T}$ and $\mathbf{X} = (X,Y)^{\mathsf T}$. A counter-clockwise rotation
of the axes through $\theta$ expresses the old coordinates in terms of the new ones by
$\mathbf{x} = R\mathbf{X}$ with

$$R = \begin{pmatrix}\cos\theta & -\sin\theta\\ \sin\theta & \cos\theta\end{pmatrix}, \qquad \det R = \cos^2\theta+\sin^2\theta = 1.$$

The quadratic part is

$$Ax^2+Bxy+Cy^2 = \mathbf{x}^{\mathsf T}M\mathbf{x} = \mathbf{X}^{\mathsf T}\left(R^{\mathsf T}MR\right)\mathbf{X},$$

so the new matrix is $M' = R^{\mathsf T}MR$, whose entries are $A'$, $B'/2$, $C'$ as in Section 7.9.
Now

$$\det M' = \det\left(R^{\mathsf T}\right)\det M\det R = 1\cdot\det M\cdot1 = \det M.$$

Finally, $\det M = AC - \dfrac{B^2}{4}$, so

$$B'^2-4A'C' = -4\det M' = -4\det M = B^2-4AC.\qquad\blacksquare$$

**Answer.** The discriminant is $-4\det M$, and $\det M$ is invariant under the substitution
$M\mapsto R^{\mathsf T}MR$ with $\det R = 1$.

**Check.** The trace is also invariant: the coefficient of $\lambda$ in the characteristic polynomial
$\det(M-\lambda I)$ is $-\operatorname{tr}M = -(A+C)$, so $A'+C' = A+C$. For the rotation of Problem 27
we get $A'+C' = 11+3 = 14 = 5+9$. $\checkmark$

**26.**

**Strategy.** Compute the vertical gap between the asymptote and the curve at the same $x$, then
rationalise the numerator to show it tends to $0$; the perpendicular distance is a constant multiple.

On the upper half of the right branch, $y = b\sqrt{\dfrac{x^2}{a^2}-1} = \dfrac{b}{a}\sqrt{x^2-a^2}$ for
$x>a$. The vertical distance from $P$ to the asymptote $y = \dfrac{b}{a}x$ is

$$\frac{b}{a}x - \frac{b}{a}\sqrt{x^2-a^2} = \frac{b}{a}\cdot\frac{x^2-(x^2-a^2)}{x+\sqrt{x^2-a^2}} = \frac{b}{a}\cdot\frac{a^2}{x+\sqrt{x^2-a^2}},$$

where the first equality multiplies and divides by the conjugate $x+\sqrt{x^2-a^2}$. As
$x\to\infty$, the denominator $x+\sqrt{x^2-a^2}\to\infty$, so the vertical distance tends to $0$.

The perpendicular distance is the vertical distance multiplied by $\cos\varphi$, where $\varphi$ is the
angle between the asymptote and the horizontal, because the component of a vertical segment normal to
a line of inclination $\varphi$ is its length times $\cos\varphi$. Since $\cos\varphi$ is a fixed
positive constant ($\cos\varphi = \dfrac{a}{\sqrt{a^2+b^2}}$), the perpendicular distance also tends
to $0$. $\blacksquare$

**Answer.** The distance from the curve to the asymptote tends to $0$, which is what "asymptote"
means; the curve is not a straight line and never meets it.

**Check.** With $a = 3$, $b = 4$, $x = 10$: $y = \frac43\sqrt{91} \approx 12.718$, while
$\frac43(10) = 13.333$; the gap is $0.615$ and is shrinking. At $x = 100$ the gap is
$\frac43\cdot\frac{9}{100+\sqrt{9991}} \approx 0.060$. $\checkmark$

**27.**

**Strategy.** Use $\Delta$ to identify the type, then the angle formula $\cot2\theta = (A-C)/B$ (or
$\tan2\theta = B/(A-C)$), then the coefficient formulas. Check with the invariants $A+C$ and $\Delta$.

Here $A = 5$, $B = 4\sqrt3$, $C = 9$, so $\Delta = 48-180 = -132<0$: an ellipse. Since
$A-C = -4$,

$$\tan2\theta = \frac{4\sqrt3}{-4} = -\sqrt3.$$

Choosing $2\theta = 120^\circ$ (the other solution differs by $180^\circ$) gives $\theta = 60^\circ$,
with $\cos\theta = \tfrac12$, $\sin\theta = \tfrac{\sqrt3}{2}$, $\cos2\theta = -\tfrac12$,
$\sin2\theta = \tfrac{\sqrt3}{2}$.

$$A' = 5\cdot\tfrac14 + 4\sqrt3\cdot\tfrac{\sqrt3}{4} + 9\cdot\tfrac34 = \tfrac54+3+\tfrac{27}{4} = 11,$$

$$C' = 5\cdot\tfrac34 - 4\sqrt3\cdot\tfrac{\sqrt3}{4} + 9\cdot\tfrac14 = \tfrac{15}{4}-3+\tfrac94 = 3,$$

$$B' = 4\sqrt3\left(-\tfrac12\right) + (9-5)\cdot\tfrac{\sqrt3}{2} = -2\sqrt3+2\sqrt3 = 0.$$

So the equation becomes $11X^2+3Y^2 = 14$, that is

$$\frac{X^2}{14/11}+\frac{Y^2}{14/3} = 1.$$

The major axis is along $Y$ (the larger denominator), so $a^2 = \tfrac{14}{3} \approx 4.667$ and
$b^2 = \tfrac{14}{11} \approx 1.273$, giving $a \approx 2.160$, $b \approx 1.128$, and
$e = \sqrt{1-b^2/a^2} = \sqrt{1-\tfrac{3}{11}} = \sqrt{\tfrac{8}{11}} \approx 0.853$.

**Answer.** An ellipse, $\dfrac{X^2}{14/11}+\dfrac{Y^2}{14/3} = 1$, with semi-axes $\sqrt{14/3}\approx2.160$
and $\sqrt{14/11}\approx1.128$, obtained by rotating the axes through $60^\circ$; eccentricity
$\sqrt{8/11}$.

**Check.** Invariants: $A'+C' = 14 = A+C$; $-4A'C' = -132 = \Delta$; and $B' = 0$ as designed. $\checkmark$

**28.**

**Strategy.** Put $x = c$ in each standard equation; the two $y$-values differ only in sign, so the chord
length is twice $|y|$.

**Ellipse.** At $x = c$, with $c^2 = a^2-b^2$,

$$y^2 = b^2\left(1-\frac{c^2}{a^2}\right) = b^2\cdot\frac{a^2-c^2}{a^2} = b^2\cdot\frac{b^2}{a^2} = \frac{b^4}{a^2},$$

so $y = \pm\dfrac{b^2}{a}$ and the chord has length $\dfrac{2b^2}{a}$.

**Hyperbola.** At $x = c$, with $c^2 = a^2+b^2$,

$$y^2 = b^2\left(\frac{c^2}{a^2}-1\right) = b^2\cdot\frac{c^2-a^2}{a^2} = b^2\cdot\frac{b^2}{a^2} = \frac{b^4}{a^2},$$

and the chord again has length $\dfrac{2b^2}{a}$. $\blacksquare$

**Answer.** Both latus recta have length $2b^2/a$; the chord runs from $(c,-b^2/a)$ to $(c,b^2/a)$.

**Check.** Ellipse $\frac{x^2}{25}+\frac{y^2}{9} = 1$: $c = 4$, chord length $2\cdot9/5 = 3.6$; the points
are $(4,\pm1.8)$, and $16/25+3.24/9 = 0.64+0.36 = 1$. $\checkmark$

**29.**

**Strategy.** Translate the geometric law into coordinates: distance to the focus is $r$, and the
distance to the vertical line $x = d_0$ is $d_0 - x$ when the point is to the left of the line.

Put the focus at the origin and the directrix at $x = d_0 > 0$. A point with polar coordinates
$(r,\theta)$ has $x = r\cos\theta$. Its distance to the directrix is $d_0 - r\cos\theta$, provided the
point lies between the focus and the directrix, which holds for the conic we are describing. The law
$|PF| = e\,d(P,\ell)$ becomes

$$r = e\left(d_0-r\cos\theta\right) \quad\Longrightarrow\quad r\left(1+e\cos\theta\right) = e\,d_0 \quad\Longrightarrow\quad r = \frac{e\,d_0}{1+e\cos\theta}.$$

**Conversion to Cartesian.** From $r\left(1+e\cos\theta\right) = e\,d_0$ and $r\cos\theta = x$,

$$r = e\,d_0 - ex \quad\Longrightarrow\quad \sqrt{x^2+y^2} = e\left(d_0-x\right).$$

Squaring (both sides are non-negative):

$$x^2+y^2 = e^2\left(d_0^2-2d_0x+x^2\right) = e^2d_0^2-2e^2d_0x+e^2x^2.$$

Collect:

$$\left(1-e^2\right)x^2 + 2e^2d_0x + y^2 = e^2d_0^2.$$

Divide by $1-e^2>0$ and complete the square in $x$:

$$x^2 + \frac{2e^2d_0}{1-e^2}x + \frac{y^2}{1-e^2} = \frac{e^2d_0^2}{1-e^2},$$

$$\left(x+\frac{e^2d_0}{1-e^2}\right)^2 + \frac{y^2}{1-e^2} = \frac{e^2d_0^2}{1-e^2} + \frac{e^4d_0^2}{\left(1-e^2\right)^2} = \frac{e^2d_0^2}{\left(1-e^2\right)^2}.$$

Divide by the right-hand side:

$$\frac{\left(x+\frac{e^2d_0}{1-e^2}\right)^2}{\frac{e^2d_0^2}{\left(1-e^2\right)^2}} + \frac{y^2}{\frac{e^2d_0^2}{1-e^2}} = 1.$$

This is an ellipse with

$$a = \frac{e\,d_0}{1-e^2}, \qquad b = \frac{e\,d_0}{\sqrt{1-e^2}}, \qquad c = \sqrt{a^2-b^2} = \frac{e^2d_0}{1-e^2} = ea,$$

centred at $\left(-\dfrac{e^2d_0}{1-e^2},0\right)$ — that is, at distance $c$ to the left of the focus,
exactly as it must be, since the focus is at the origin. $\blacksquare$

**Answer.** $r = \dfrac{e\,d_0}{1+e\cos\theta}$; for $0<e<1$ it is an ellipse with
$a = \dfrac{e\,d_0}{1-e^2}$ and $c = ea$.

**Check.** Take $e = \tfrac12$, $d_0 = 6$: then $a = 3/(3/4) = 4$, $c = 2$, $b^2 = 12$. The equation is
$\frac{(x+2)^2}{16}+\frac{y^2}{12} = 1$, whose focus nearer the directrix is at $x = -2+2 = 0$, the
origin. $\checkmark$

**30.**

**Strategy.** A constant time difference is a constant distance difference; that is the definition of a
hyperbola with the stations as foci.

The extra distance is

$$2a = \left(3\times10^{5}\ \mathrm{km/s}\right)\left(0.0008\ \mathrm{s}\right) = 240\ \mathrm{km},$$

so $a = 120$. The foci are at $(\pm c, 0)$ with $c = 200$, hence

$$b^2 = c^2-a^2 = 40000-14400 = 25600.$$

The locus is

$$\frac{x^2}{14400}-\frac{y^2}{25600} = 1.$$

The signal from $B$ arrives first, so the receiver is nearer $B = (200,0)$ and lies on the branch $x\ge120$.
With $y = 100$:

$$\frac{x^2}{14400} = 1+\frac{10000}{25600} = 1+\frac{25}{64} = \frac{89}{64},$$

$$x^2 = 14400\cdot\frac{89}{64} = 225\cdot89 = 20025, \qquad x = \sqrt{20025} \approx 141.51.$$

**Answer.** The receiver is at approximately $(141.5,\,100)$ km.

**Check.** Distance to $B$: $\sqrt{(200-141.51)^2+100^2} = \sqrt{58.49^2+10000} \approx \sqrt{3421+10000} = 115.85$.
Distance to $A$: $\sqrt{(200+141.51)^2+100^2} \approx \sqrt{116628+10000} = 355.85$. The difference is
$240.00$ km, which at $3\times10^5$ km/s corresponds to $0.0008$ s. $\checkmark$

## Challenge

**31.**

**Strategy.** Translate the verbal condition into an equation, square once, and complete the square.
Then compare with the standard hyperbola to read off $e$.

Let $P = (x,y)$. The distance to the origin is $\sqrt{x^2+y^2}$ and the distance to $x = 3$ is
$|x-3|$. The condition is

$$\sqrt{x^2+y^2} = 2\,|x-3|.$$

Both sides are non-negative, so squaring is reversible:

$$x^2+y^2 = 4\left(x^2-6x+9\right) = 4x^2-24x+36.$$

Collect:

$$0 = 3x^2-24x+36-y^2 \quad\Longrightarrow\quad y^2 = 3x^2-24x+36 = 3\left(x^2-8x\right)+36.$$

Complete the square: $x^2-8x = (x-4)^2-16$, so

$$y^2 = 3(x-4)^2-48+36 = 3(x-4)^2-12,$$

$$3(x-4)^2-y^2 = 12, \qquad \frac{(x-4)^2}{4}-\frac{y^2}{12} = 1.$$

This is a hyperbola with centre $(4,0)$, $a = 2$, $b^2 = 12$, hence $c = \sqrt{4+12} = 4$ and
$e = c/a = 2$. The foci are at $(4\pm4,0)$, that is $(8,0)$ and $(0,0)$ — and $(0,0)$ is the focus $F$
we started with. The directrix belonging to that focus is $x = 4-\dfrac{a^2}{c} = 4-1 = 3$, exactly the
given line.

**Answer.** $\dfrac{(x-4)^2}{4}-\dfrac{y^2}{12} = 1$, a hyperbola with eccentricity $2$.

**Check.** The point $(6,0)$ is on the curve: $\frac{(6-4)^2}{4}-0 = 1$. Its distance to the focus
$(0,0)$ is $6$ and its distance to the line $x=3$ is $3$; the ratio is $2$. $\checkmark$ A second point:
putting $y = 6$ gives $(x-4)^2 = 4\left(1+\frac{36}{12}\right) = 16$, so $x = 8$ or $x = 0$. At $(8,6)$ the
distance to the origin is $\sqrt{64+36} = 10$ and the distance to $x=3$ is $5$; the ratio is again $2$.
$\checkmark$ (The root $x = 0$ gives the point $(0,6)$, on the other branch, whose distances are $6$ and
$3$ — also in the ratio $2$.)

**32.**

**Strategy.** Substitute the line into the ellipse. If the resulting quadratic in one variable has a
double root at the point of tangency, the line meets the curve there and nowhere else.

Let $(x_0,y_0)$ satisfy $\dfrac{x_0^2}{a^2}+\dfrac{y_0^2}{b^2} = 1$ and let $L$ be the line
$\dfrac{xx_0}{a^2}+\dfrac{yy_0}{b^2} = 1$.

*Case $y_0 \ne 0$.* Solve $L$ for $y$:

$$y = \frac{b^2}{y_0}\left(1-\frac{xx_0}{a^2}\right).$$

Write $u = x/a$ and $u_0 = x_0/a$, $v_0 = y_0/b$, so that $u_0^2+v_0^2 = 1$ and, from
$y_0 = bv_0$, $\dfrac{b^2}{y_0^2} = \dfrac{1}{v_0^2}$. Substituting into the ellipse:

$$u^2 + \frac{1}{v_0^2}\left(1-uu_0\right)^2 = 1.$$

Multiply by $v_0^2 = 1-u_0^2$:

$$u^2\left(1-u_0^2\right) + \left(1-uu_0\right)^2 = 1-u_0^2.$$

Expand the square and collect:

$$u^2-u^2u_0^2+1-2uu_0+u^2u_0^2 = 1-u_0^2 \quad\Longrightarrow\quad u^2-2uu_0+u_0^2 = 0 \quad\Longrightarrow\quad (u-u_0)^2 = 0.$$

So $u = u_0$ is the only solution, with multiplicity two, and then $x = x_0$ and
$y = \frac{b^2}{y_0}\left(1-\frac{x_0^2}{a^2}\right) = \frac{b^2}{y_0}\cdot\frac{y_0^2}{b^2} = y_0$.

*Case $y_0 = 0$.* Then $x_0 = \pm a$ and $L$ is $\dfrac{x x_0}{a^2} = 1$, that is $x = x_0$ — a vertical
line touching the ellipse at its vertex only.

Since $L$ meets $E$ at exactly one point, and a line meeting a strictly convex closed curve in exactly
one point is its tangent there, $L$ is the tangent at $(x_0,y_0)$. $\blacksquare$

**Answer.** The line $\dfrac{xx_0}{a^2}+\dfrac{yy_0}{b^2} = 1$ touches the ellipse at $(x_0,y_0)$ and
nowhere else; it is the tangent.

**Check.** For $\frac{x^2}{25}+\frac{y^2}{9} = 1$ at $\left(3,\tfrac{12}{5}\right)$ — which is on the
ellipse, since $\frac{9}{25}+\frac{144/25}{9} = \frac{9}{25}+\frac{16}{25} = 1$ — the tangent is
$\frac{3x}{25}+\frac{4y}{15} = 1$, i.e. $9x+20y = 75$, of slope $-\frac{9}{20}$. The tangent-slope formula
$-\frac{x_0b^2}{y_0a^2} = -\frac{3\cdot9}{(12/5)\cdot25} = -\frac{27}{60} = -\frac{9}{20}$ agrees. $\checkmark$

**33.**

**(a) All parabolas are similar.**

**Strategy.** A single scaling by $|p|$ turns $y^2 = 4px$ into $y^2 = 4x$.

Let $p \ne 0$ and let $(x,y)$ satisfy $y^2 = 4px$. Define

$$X = \frac{x}{p}, \qquad Y = \frac{y}{p}.$$

Then $x = pX$ and $y = pY$, so

$$p^2Y^2 = 4p\cdot pX \quad\Longrightarrow\quad Y^2 = 4X,$$

because $p^2 \ne 0$. The map $(x,y)\mapsto\left(\frac{x}{p},\frac{y}{p}\right)$ is a similarity (a
scaling by $1/|p|$, with a reflection when $p<0$), and it carries the parabola with parameter $p$ onto
the fixed parabola $Y^2 = 4X$. Since any two parabolas are each similar to this one, they are similar
to each other. $\blacksquare$

**(b) The law with $e = 1$ gives a parabola.**

**Strategy.** Put the focus at the origin and the directrix at $x = d_0$, then eliminate the radicals.

The law is

$$\sqrt{x^2+y^2} = \left|d_0-x\right|.$$

Both sides are non-negative, so squaring is reversible:

$$x^2+y^2 = d_0^2-2d_0x+x^2.$$

The $x^2$ terms cancel:

$$y^2 = d_0^2-2d_0x = -2d_0\left(x-\frac{d_0}{2}\right).$$

With $X = x-\frac{d_0}{2}$ and $Y = y$ this is $Y^2 = -2d_0X$, which is a parabola in the standard form
$Y^2 = 4pX$ with $p = -\frac{d_0}{2}$: vertex at the midpoint between focus and directrix, opening away
from the directrix. $\blacksquare$

**Answer.** (a) The scaling $(x,y)\mapsto (x/p,\,y/p)$ maps $y^2 = 4px$ onto $y^2 = 4x$. (b) The law with
$e=1$ yields $y^2 = -2d_0\left(x-\frac{d_0}{2}\right)$, a parabola.

**Check.** For (b) with $d_0 = 4$ the equation is $y^2 = -8(x-2)$. In the shifted frame
$X = x-2$, $Y = y$ this is $Y^2 = -8X$, so $4p = -8$ and $p = -2$: the focus is at $X = -2$, that is
$x = 0$, the origin — as required — and the directrix is $X = 2$, that is $x = 4 = d_0$. $\checkmark$

**34.**

**Strategy.** Put the origin at the waist (the narrowest circle) and the $y$-axis along the axis of the
tower. Then the cross-section is $\dfrac{x^2}{a^2}-\dfrac{y^2}{b^2} = 1$ with $a = 25$, and the second
data point determines $b$.

The waist radius is $a = 25$. At a height of $30$ m above the waist the radius is $30$ m, so

$$\frac{900}{625}-\frac{900}{b^2} = 1 \quad\Longrightarrow\quad 1.44-1 = \frac{900}{b^2} \quad\Longrightarrow\quad b^2 = \frac{900}{0.44} = \frac{22500}{11} \approx 2045.45.$$

Thus $b \approx 45.23$ m and the model is

$$\frac{x^2}{625}-\frac{11y^2}{22500} = 1.$$

At a height of $100$ m the height above the waist is $y = 60$:

$$\frac{x^2}{625} = 1+\frac{11\cdot3600}{22500} = 1+\frac{39600}{22500} = 1+1.76 = 2.76,$$

$$x^2 = 625\cdot2.76 = 1725, \qquad x = \sqrt{1725} \approx 41.53.$$

**Answer.** $a = 25$ m, $b \approx 45.23$ m; the radius at a height of $100$ m is about $41.5$ m.

**Check.** The point $(30,30)$ must satisfy the model: $\frac{900}{625}-\frac{11\cdot900}{22500} = 1.44-0.44 = 1$.
$\checkmark$ The waist point $(25,0)$: $\frac{625}{625}-0 = 1$. $\checkmark$ The radius increases with
height, as a cooling tower's does near the base.

**Why the model must fail eventually.** A hyperbola's radius grows without bound: its asymptotes are
$x = \pm\dfrac{a}{b}y \approx \pm 0.553\,y$, so the model predicts radii far beyond the throat as the
height increases. A real tower has a finite height and a top rim of perhaps $20$–$25$ m radius, so the
model is only valid over the middle band of the tower. The model also ignores the thickening of the
shell and the flare at the base, and treats the tower as an exact surface of revolution, which real
towers approximate but do not equal.
