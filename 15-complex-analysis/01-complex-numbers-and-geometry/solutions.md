# Complex Numbers and Geometry — Solutions

> [Tutorial](README.md) · [Exercises](exercises.md) · 36 worked solutions

Each solution states the strategy, carries out every step, and ends with an independent check where one
is available. Alternative approaches are indicated where they are instructive.

## Beginner

**1.** Expand and use $i^2 = -1$:

$$(3+4i)(1-2i) = 3 - 6i + 4i - 8i^2 = 3 - 2i + 8 = 11-2i.$$

**Check.** $\lvert 3+4i\rvert = 5$ and $\lvert 1-2i\rvert = \sqrt5$, so the product must have modulus
$5\sqrt5 = \sqrt{125}$; indeed $\lvert 11-2i\rvert = \sqrt{121+4} = \sqrt{125}$.

**2.** $\lvert z\rvert = \sqrt{(-1)^2+(\sqrt3)^2} = \sqrt{1+3} = 2$. Since $z/2 = (-1/2,\ \sqrt3/2)$,
the point is in the second quadrant with reference angle $\pi/3$, so
$\operatorname{Arg}z = \pi - \pi/3 = 2\pi/3$.

**Check.** $2\cos(2\pi/3) = 2(-1/2) = -1$ and $2\sin(2\pi/3) = 2(\sqrt3/2) = \sqrt3$.

**3.** $\lvert 1-i\rvert = \sqrt2$ and the point is in the fourth quadrant with reference angle $\pi/4$,
so $\operatorname{Arg}(1-i) = -\pi/4$. Therefore

$$1-i = \sqrt2\left(\cos\left(-\frac\pi4\right)+i\sin\left(-\frac\pi4\right)\right) = \sqrt2\,e^{-i\pi/4}.$$

**Check.** $\sqrt2\cos(-\pi/4) = \sqrt2\cdot\sqrt2/2 = 1$ and $\sqrt2\sin(-\pi/4) = -1$.

**4.** The equation is $z^2 = -16 = 16e^{i\pi}$. By Proposition 7.13 with $n = 2$, the roots are
$4e^{i\pi/2} = 4i$ and $4e^{3\pi i/2} = -4i$.

**Check.** $(4i)^2 = 16i^2 = -16$ and $(-4i)^2 = 16i^2 = -16$.

**5.** Divide the exponents by $4$: $2025 = 4\cdot506+1$, so $i^{2025} = (i^4)^{506}i = i$.
Then $i^{2026} = i^{2025}\cdot i = i\cdot i = -1$.

**6.** $\bar z = 2-3i$, $\lvert z\rvert^2 = 4+9 = 13$, and by Proposition 7.3,

$$\frac1z = \frac{\bar z}{\lvert z\rvert^2} = \frac{2-3i}{13}.$$

**Check.** $(2+3i)(2-3i)/13 = (4+9)/13 = 1$.

**7.** $1+i = \sqrt2\,e^{i\pi/4}$, so by De Moivre

$$(1+i)^8 = (\sqrt2)^8 e^{8\pi i/4} = 16\,e^{2\pi i} = 16.$$

**Check.** $(1+i)^2 = 2i$, so $(1+i)^4 = (2i)^2 = -4$ and $(1+i)^8 = 16$.

**8.** Multiply numerator and denominator by $2+i$:

$$\frac{1+i}{2-i} = \frac{(1+i)(2+i)}{(2-i)(2+i)} = \frac{2+i+2i+i^2}{4+1} = \frac{1+3i}{5}.$$

Hence $\operatorname{Re} = 1/5$ and $\operatorname{Im} = 3/5$.

**Check.** $(1+3i)(2-i)/5 = (2-i+6i-3i^2)/5 = (5+5i)/5 = 1+i$.

**9.** $z+\bar z = (5-2i)+(5+2i) = 10 = 2\operatorname{Re}z$ since $\operatorname{Re}z = 5$;
$z-\bar z = (5-2i)-(5+2i) = -4i = 2i\operatorname{Im}z$ since $\operatorname{Im}z = -2$.

**10.** $\lvert z-(2+i)\rvert = 3$ is the circle with centre $2+i$ and radius $3$. The inequality
$\lvert z-(2+i)\rvert\le3$ is the closed disc bounded by that circle, i.e. the set of points at distance
at most $3$ from $2+i$.

**11.** The equation says that $z$ is equidistant from $1$ and $-1$. Writing $z = x+iy$,

$$(x-1)^2+y^2 = (x+1)^2+y^2 \iff x^2-2x+1 = x^2+2x+1 \iff -2x = 2x \iff x = 0.$$

So the set is the imaginary axis, the perpendicular bisector of the segment from $-1$ to $1$.

**12.** $\omega = e^{2\pi i/3} = \cos(2\pi/3)+i\sin(2\pi/3) = -1/2+i\sqrt3/2$, and
$\omega^2 = e^{4\pi i/3} = -1/2-i\sqrt3/2$. The three cube roots of unity are $1,\omega,\omega^2$.
By De Moivre, $\omega^3 = e^{2\pi i} = 1$ and $(\omega^2)^3 = \omega^6 = 1$. The sum is
$1+(-1/2+i\sqrt3/2)+(-1/2-i\sqrt3/2) = 0$, which also follows from Proposition 7.17 with $n = 3$.

## Intermediate

**13.** $z+w = (3+4i)+(5-12i) = 8-8i$, so $\lvert z+w\rvert = \sqrt{64+64} = 8\sqrt2\approx11.31$.
Also $\lvert z\rvert = 5$, $\lvert w\rvert = 13$, hence $\lvert z\rvert+\lvert w\rvert = 18$. Since
$11.31<18$, the triangle inequality holds strictly, as it must: $z$ and $w$ do not point in the same
direction.

**14.** Write $z = a+bi$, $w = c+di$. Then

$$\lvert zw\rvert^2 = (ac-bd)^2+(ad+bc)^2 = a^2c^2-2abcd+b^2d^2+a^2d^2+2abcd+b^2c^2 = (a^2+b^2)(c^2+d^2) = \lvert z\rvert^2\lvert w\rvert^2.$$

Both sides are non-negative, so taking square roots gives $\lvert zw\rvert = \lvert z\rvert\lvert w\rvert$.
For the power, induct on $n$: $\lvert z^1\rvert = \lvert z\rvert$, and
$\lvert z^{n+1}\rvert = \lvert z^n\rvert\lvert z\rvert = \lvert z\rvert^n\lvert z\rvert = \lvert z\rvert^{n+1}$.

**15.** The parallelogram law (Proposition 7.7) gives

$$\lvert z+w\rvert^2+\lvert z-w\rvert^2 = 2\lvert z\rvert^2+2\lvert w\rvert^2 = 2\cdot9+2\cdot25 = 68.$$

Since $\lvert z-w\rvert = 7$, we get $\lvert z+w\rvert^2 = 68-49 = 19$, so $\lvert z+w\rvert = \sqrt{19}$.

**Check.** The parallelogram with sides $3$ and $5$ and one diagonal $7$ has, by the law of cosines,
$\cos\theta = (9+25-49)/(2\cdot3\cdot5) = -15/30 = -1/2$, so $\theta = 120^\circ$ and the other diagonal
satisfies $\lvert z+w\rvert^2 = 9+25+2\cdot15\cos120^\circ = 34-15 = 19$. Agrees.

**16.** Write $-4 = 4e^{i\pi}$. By Proposition 7.13 with $n = 4$ and $\rho^{1/4} = \sqrt2$,

$$z_k = \sqrt2\,\exp\!\left(i\frac{\pi+2\pi k}{4}\right), \qquad k = 0,1,2,3.$$

In Cartesian form: $z_0 = \sqrt2e^{i\pi/4} = 1+i$, $z_1 = \sqrt2e^{3\pi i/4} = -1+i$,
$z_2 = \sqrt2e^{5\pi i/4} = -1-i$, $z_3 = \sqrt2e^{7\pi i/4} = 1-i$.

**Check.** $(1+i)^2 = 2i$ and $(2i)^2 = -4$. The other roots are $-z_0$ and $\pm\bar z_0$, whose fourth
powers are also $-4$. Their sum is zero, matching the vanishing $z^3$ coefficient.

**17.** The quadratic formula gives

$$z = \frac{-2\pm\sqrt{4-20}}{2} = \frac{-2\pm\sqrt{-16}}{2} = \frac{-2\pm4i}{2} = -1\pm2i.$$

**Check.** For $z = -1+2i$: $z^2 = 1-4i+4i^2 = -3-4i$, and $z^2+2z+5 = (-3-4i)+(-2+4i)+5 = 0$.
The other root is the conjugate, and the coefficients are real.

**18.** Let $z = x+iy$. Then $z^2 = (x^2-y^2)+2xyi$, so the equation is equivalent to the system

$$x^2-y^2 = 3, \qquad 2xy = 4.$$

Also $\lvert z\rvert^2 = x^2+y^2 = \lvert z^2\rvert = \lvert 3+4i\rvert = 5$. Adding and subtracting the
first and third equations gives $2x^2 = 8$ and $2y^2 = 2$, so $x = \pm2$ and $y = \pm1$. The condition
$2xy = 4>0$ forces $x$ and $y$ to have the same sign, so $z = 2+i$ or $z = -2-i$.

**Check.** $(2+i)^2 = 4+4i+i^2 = 3+4i$.

**19.** Points of the line are $z = t(1+i)$ with $t\in\mathbb{R}$. Then
$iz = it(1+i) = t(i+i^2) = t(-1+i)$, which is the line $y = -x$. Geometrically, multiplication by $i$
is rotation by $\pi/2$; the line at angle $\pi/4$ is carried to the line at angle $\pi/4+\pi/2 = 3\pi/4$,
which is $y = -x$.

**20.** If $\lvert z\rvert = 1$ then $\lvert 1/z\rvert = 1/\lvert z\rvert = 1$, so the unit circle maps
into itself; since $J(z) = 1/z$ is its own inverse, every point of the circle is an image, so the image is
the whole circle. For the real axis: if $z = x$ is real and non-zero, $1/z = 1/x$ is real; and $0\mapsto\infty$,
$\infty\mapsto0$. Hence $\mathbb{R}_\infty$ maps onto itself.

**21.** Write $T(z) = (az+b)/(cz+d)$. The condition $T(\infty) = 0$ gives $a/c = 0$, so $a = 0$ and
$c\ne0$. The condition $T(0) = 1$ gives $b/d = 1$, so $b = d$. The condition $T(1) = \infty$ means the
denominator vanishes at $1$: $c+d = 0$, so $c = -d$. Choosing $d = 1$ gives

$$T(z) = \frac{1}{1-z}.$$

**Check.** $T(0) = 1$, $T(1) = \infty$, $T(\infty) = 0/(-1) = 0$; and the determinant is $0\cdot1-1\cdot(-1) = 1\ne0$.

**22.** By Definition 5.10,

$$(1,-1;i,-i) = \frac{(1-i)(-1+i)}{(1+i)(-1-i)} = \frac{-(1-i)^2}{-(1+i)^2} = \frac{(1-i)^2}{(1+i)^2}.$$

Now $(1-i)^2 = 1-2i+i^2 = -2i$ and $(1+i)^2 = 2i$, so the cross-ratio equals $-2i/2i = -1$. It is real,
so by Theorem 7.32 the four points lie on a generalized circle; indeed all four satisfy $\lvert z\rvert = 1$.

**23.** With $x = 1$, $y = 1$ and $\lvert z\rvert^2 = 2$, Proposition 7.36 gives

$$\sigma^{-1}(1+i) = \left(\frac{2}{3},\ \frac{2}{3},\ \frac{2-1}{3}\right) = \left(\frac23,\ \frac23,\ \frac13\right).$$

**Check.** $(2/3)^2+(2/3)^2+(1/3)^2 = 4/9+4/9+1/9 = 1$.

**24.** By Proposition 7.39, $d(0,\infty) = 2/\sqrt{1+0} = 2$. Also

$$d(1,-1) = \frac{2\lvert 1-(-1)\rvert}{\sqrt{(1+1)(1+1)}} = \frac{4}{2} = 2.$$

The value $d = 2$ is the maximum possible, so the corresponding points must be antipodal; indeed
$\sigma^{-1}(1) = (1,0,0)$ and $\sigma^{-1}(-1) = (-1,0,0)$ are antipodal.

## Advanced

**25.** Expand both squares, using $\lvert\zeta\rvert^2 = \zeta\bar\zeta$:

$$\lvert 1-z\bar w\rvert^2 = 1-2\operatorname{Re}(z\bar w)+\lvert z\rvert^2\lvert w\rvert^2, \qquad \lvert z-w\rvert^2 = \lvert z\rvert^2-2\operatorname{Re}(z\bar w)+\lvert w\rvert^2.$$

The real parts agree because $\overline{z\bar w} = \bar z w$ and $\operatorname{Re}\zeta = \operatorname{Re}\bar\zeta$.
Subtracting,

$$\lvert 1-z\bar w\rvert^2-\lvert z-w\rvert^2 = 1-\lvert z\rvert^2-\lvert w\rvert^2+\lvert z\rvert^2\lvert w\rvert^2 = (1-\lvert z\rvert^2)(1-\lvert w\rvert^2).$$

If $\lvert z\rvert<1$ and $\lvert w\rvert<1$, the right side is positive, so
$\lvert 1-z\bar w\rvert>\lvert z-w\rvert\ge0$. In particular $1-z\bar w\ne0$ (otherwise $\lvert z\rvert\lvert w\rvert = 1$,
contradicting $\lvert z\rvert\lvert w\rvert<1$), so division is legitimate and gives
$\lvert z-w\rvert/\lvert 1-z\bar w\rvert<1$.

**26.** Let $T(z) = (az+b)/(cz+d)$ with $a,b,c,d\in\mathbb{R}$ and $ad-bc\ne0$. If $x\in\mathbb{R}$ and
$cx+d\ne0$, then $T(x) = (ax+b)/(cx+d)\in\mathbb{R}$. If $c\ne0$, then $T(-d/c) = \infty$ and
$T(\infty) = a/c\in\mathbb{R}$; if $c = 0$, then $T(\infty) = \infty$ and $T$ is a real affine map on
$\mathbb{R}$. Hence $T(\mathbb{R}_\infty)\subseteq\mathbb{R}_\infty$. The inverse of $T$ is represented by
$\begin{pmatrix}d&-b\\ -c&a\end{pmatrix}$, again with real entries, so the same argument gives
$T^{-1}(\mathbb{R}_\infty)\subseteq\mathbb{R}_\infty$, hence equality.

For four distinct real points, each factor $z_j-z_k$ in Definition 5.10 is real and each denominator is
non-zero (or the formula is interpreted by the convention at $\infty$, which also yields a real value).
Hence the cross-ratio is real.

**27.** Put $w = 1/z$, so $z = 1/w$. The equation $\lvert z-c\rvert^2 = r^2$ expands to

$$\lvert z\rvert^2-2\operatorname{Re}(z\bar c)+\lvert c\rvert^2 = r^2.$$

Substituting $z = 1/w$ and multiplying by $\lvert w\rvert^2 = w\bar w$ gives

$$1-2\operatorname{Re}(c w)+(\lvert c\rvert^2-r^2)\lvert w\rvert^2 = 0,$$

because $\lvert w\rvert^2 z\bar c = \bar c\bar w$ and $\lvert w\rvert^2\bar zc = cw$, whose sum is
$2\operatorname{Re}(cw)$. Put $D := \lvert c\rvert^2-r^2\ne0$. Dividing by $D$,

$$\lvert w\rvert^2-\frac{2}{D}\operatorname{Re}(cw)+\frac1D = 0.$$

Completing the square gives

$$\left\lvert w-\frac{\bar c}{D}\right\rvert^2 = \frac{\lvert c\rvert^2}{D^2}-\frac1D = \frac{\lvert c\rvert^2-D}{D^2} = \frac{r^2}{D^2},$$

so the image is the circle with centre $\bar c/D$ and radius $r/\lvert D\rvert$. If $D = 0$ the equation
becomes $-2\operatorname{Re}(cw)+1 = 0$, a line, consistent with Corollary 7.28.

**28.** Compute

$$R_{b,\varphi}\bigl(R_{a,\theta}(z)\bigr) = b+e^{i\varphi}\bigl(a+e^{i\theta}(z-a)-b\bigr) = e^{i(\theta+\varphi)}z+\mu,$$

with $\mu := a e^{i\varphi}(1-e^{i\theta})+b(1-e^{i\varphi})$. If $e^{i(\theta+\varphi)}\ne1$, the map
$z\mapsto e^{i(\theta+\varphi)}z+\mu$ is a rotation by $\theta+\varphi$ about the unique fixed point
$c = \mu/(1-e^{i(\theta+\varphi)})$. If $e^{i(\theta+\varphi)} = 1$, the map is the translation
$z\mapsto z+\mu$; it is the identity exactly when $\mu = 0$.

**Example check.** Take $\theta = \varphi = \pi/2$, $a = 0$, $b = 1$. Then $\mu = 1-i$ and
$e^{i(\theta+\varphi)} = -1$, so $c = (1-i)/2$: the composite is a half-turn about $(1-i)/2$. Indeed
$0\mapsto0\mapsto1-i$, and the half-turn about $(1-i)/2$ sends $0$ to $1-i$.

**29.** Put $g(x) := f(x)-f(0)$; then $\lvert g(x)\rvert = \lambda\lvert x\rvert$ and
$\lvert g(x)-g(y)\rvert = \lambda\lvert x-y\rvert$. Expanding the second identity,

$$\lvert g(x)\rvert^2+\lvert g(y)\rvert^2-2\,g(x)\cdot g(y) = \lambda^2\bigl(\lvert x\rvert^2+\lvert y\rvert^2-2\,x\cdot y\bigr),$$

and using $\lvert g(x)\rvert = \lambda\lvert x\rvert$, $\lvert g(y)\rvert = \lambda\lvert y\rvert$ gives

$$g(x)\cdot g(y) = \lambda^2\,x\cdot y. \tag{$\ast$}$$

Now

$$\lvert g(x+y)-g(x)-g(y)\rvert^2 = \lvert g(x+y)\rvert^2+\lvert g(x)\rvert^2+\lvert g(y)\rvert^2-2g(x+y)\cdot g(x)-2g(x+y)\cdot g(y)+2g(x)\cdot g(y),$$

and substituting $(\ast)$ into each inner product gives

$$\lambda^2\bigl(\lvert x+y\rvert^2+\lvert x\rvert^2+\lvert y\rvert^2-2(x+y)\cdot x-2(x+y)\cdot y+2x\cdot y\bigr) = 0.$$

Hence $g$ is additive. Similarly, for $t\in\mathbb{R}$,

$$\lvert g(tx)-tg(x)\rvert^2 = \lambda^2t^2\lvert x\rvert^2+t^2\lambda^2\lvert x\rvert^2-2t\,g(tx)\cdot g(x) = 2\lambda^2t^2\lvert x\rvert^2-2t\cdot\lambda^2t\lvert x\rvert^2 = 0,$$

so $g(tx) = tg(x)$. Thus $g$ is real-linear: $g(x) = Ax$ for a linear map $A$. By $(\ast)$,
$(Ax)\cdot(Ay) = \lambda^2x\cdot y$, so $A^{\mathsf T}A = \lambda^2I$; in particular $A$ is $\lambda$ times
an orthogonal matrix. Since $f$ preserves orientation, $\det A>0$, hence $\det A = \lambda^2$ and $A$ is
$\lambda$ times a rotation $R_\theta = \begin{pmatrix}\cos\theta&-\sin\theta\\ \sin\theta&\cos\theta\end{pmatrix}$.
Identifying $\mathbb{R}^2$ with $\mathbb{C}$, this matrix is multiplication by $a := \lambda e^{i\theta}$,
so $f(z) = az+b$ with $b = f(0)$ and $a\ne0$.

**30.** Let $T(z) = (az+b)/(cz+d)$ be Möbius, and first look for finite fixed points $z\in\mathbb{C}$ with $cz+d\ne0$. The equation $T(z) = z$ is

$$az+b = cz^2+dz \iff cz^2+(d-a)z-b = 0.$$

If $c\ne0$ this is a genuine quadratic, so it has at most two roots; and $\infty$ is not fixed because $T(\infty) = a/c$ is finite. If $c = 0$, then $T(z) = (a/d)z+b/d$. When $a\ne d$ there is exactly one finite fixed point $z = b/(d-a)$, and $\infty$ is also fixed; when $a = d$ and $b\ne0$ there is no finite fixed point and only $\infty$ is fixed; when $a = d$ and $b = 0$ the map is the identity. Hence a non-identity Möbius map has at most two fixed points.

If a Möbius map has three distinct fixed points, then the case $c\ne0$ is impossible (a quadratic with three roots is the zero polynomial, which would force $c = 0$), and the case $c = 0$ gives the identity unless at most two fixed points exist. Hence the map is the identity.

**31.** If $T$ exists, Proposition 7.31 gives $(w_1,w_2;w_3,w_4) = (z_1,z_2;z_3,z_4)$.

Conversely, suppose the cross-ratios are equal. By Theorem 7.23 there is a Möbius map $T$ with $T(z_j) = w_j$ for $j = 1,2,3$. Applying Proposition 7.31 to the fourth point,

$$(w_1,w_2;w_3,Tz_4) = (Tz_1,Tz_2;Tz_3,Tz_4) = (z_1,z_2;z_3,z_4) = (w_1,w_2;w_3,w_4).$$

For fixed distinct $w_1,w_2,w_3$, the map $u\mapsto(w_1,w_2;w_3,u)$ is a Möbius transformation of $u$ (a quotient of linear factors in $u$ with non-zero determinant), hence injective on $\mathbb{C}_\infty$. Equality of the two values therefore gives $Tz_4 = w_4$. Thus $T$ maps all four points correctly.

## Challenge

**32.** Assume first that all four points are finite. Consider

$$\lambda := (z_1,z_2;z_3,z_4) = \frac{(z_1-z_3)(z_2-z_4)}{(z_1-z_4)(z_2-z_3)}.$$

Since $z_1-z_3 = -(z_3-z_1)$ and $z_1-z_4 = -(z_4-z_1)$, we may write

$$\lambda = \frac{(z_3-z_1)/(z_4-z_1)}{(z_3-z_2)/(z_4-z_2)}.$$

Taking arguments, and writing $\measuredangle z_4z_1z_3$ for the oriented angle at $z_1$ from the ray $z_1z_4$ to the ray $z_1z_3$,

$$\arg\lambda \equiv \measuredangle z_4z_1z_3-\measuredangle z_4z_2z_3 \pmod{2\pi}.$$

Thus $\lambda$ is real exactly when the two oriented angles are equal or differ by $\pi$. By the inscribed-angle theorem, two points $z_1,z_2$ see the chord $z_3z_4$ under equal (or supplementary) angles precisely when $z_1,z_2,z_3,z_4$ lie on a common circle — if $z_1,z_2$ are on the same side of the chord the angles are equal, and if they are on opposite sides they are supplementary — or on the common line $z_3z_4$. This is exactly the condition that the four points lie on a generalized circle.

Conversely, if the four points lie on a common circle or line, the inscribed-angle theorem (or, in the collinear case, the equality of the angles $0$ and $\pi$) gives $\arg\lambda\in\{0,\pi\}\pmod{2\pi}$, so $\lambda\in\mathbb{R}$. This proves the criterion without using the circle-preservation theorem.

**33.** *Step 1: the maps of the stated form work.* Let $\lvert a\rvert<1$ and define
$\varphi_a(z) := (z-a)/(1-\bar az)$, which is Möbius with determinant $1-\lvert a\rvert^2\ne0$. For $\lvert z\rvert<1$, exercise 25 (applied with $w = a$) gives

$$\lvert 1-\bar az\rvert^2-\lvert z-a\rvert^2 = (1-\lvert z\rvert^2)(1-\lvert a\rvert^2)>0,$$

so $\lvert\varphi_a(z)\rvert<1$. Its inverse is $\varphi_{-a}$, so $\varphi_a$ is a bijection of $D$ onto itself. Multiplication by $e^{i\theta}$ is a rotation, hence also a bijection of $D$. Therefore every $T$ of the stated form maps $D$ onto $D$.

*Step 2: every automorphism has that form.* Suppose $T$ is Möbius with $T(D) = D$. Put $a := T^{-1}(0)\in D$, so $T(a) = 0$, and define $S := T\circ\varphi_{-a}$, where $\varphi_{-a}$ is the inverse of $\varphi_a$. Then $S$ maps $D$ onto $D$ and $S(0) = T(\varphi_{-a}(0)) = T(a) = 0$.

Because $T$ and $\varphi_{-a}$ are homeomorphisms of $\mathbb{C}_\infty$, the map $S$ is a homeomorphism with $S(D) = D$; therefore $S(\overline D) = \overline D$ and
$S(\partial D) = S(\overline D\setminus D) = \overline D\setminus D = \partial D$. Write $S(z) = (\alpha z+\beta)/(\gamma z+\delta)$. The condition $S(0) = 0$ gives $\beta = 0$. For $\lvert z\rvert = 1$ we have $\lvert S(z)\rvert = 1$, hence $\lvert\gamma z+\delta\rvert = \lvert\alpha\rvert$ for every $\lvert z\rvert = 1$. Squaring,

$$\lvert\gamma\rvert^2+\lvert\delta\rvert^2+2\operatorname{Re}\bigl(\bar\gamma\delta z\bigr) = \lvert\alpha\rvert^2$$

is constant on the unit circle, which forces $\bar\gamma\delta = 0$. If $\delta = 0$ and $\gamma\ne0$, then $S(z) = \alpha z/(\gamma z) = \alpha/\gamma$ is constant, contradicting bijectivity; hence $\gamma = 0$. Then $S(z) = (\alpha/\delta)z$ and $\lvert S(z)\rvert = 1$ forces $\lvert\alpha/\delta\rvert = 1$, i.e. $\alpha/\delta = e^{i\theta}$. Therefore $S(z) = e^{i\theta}z$ and

$$T = S\circ\varphi_a, \qquad T(z) = e^{i\theta}\frac{z-a}{1-\bar az}.$$

**34.** Suppose first that $T(z) = (az+b)/(cz+d)$ with $a,b,c,d\in\mathbb{R}$ and $ad-bc\ne0$. By exercise 26, $T(\mathbb{R}_\infty) = \mathbb{R}_\infty$. If in addition $ad-bc>0$, then for $z = i$,

$$T(i) = \frac{ai+b}{ci+d} = \frac{(ai+b)(d-ci)}{\lvert ci+d\rvert^2} = \frac{(ac+bd)+i(ad-bc)}{\lvert ci+d\rvert^2},$$

so $\operatorname{Im}T(i) = (ad-bc)/\lvert ci+d\rvert^2>0$. The pole $-d/c$ is real (or absent if $c=0$), so $T$ is continuous on the upper half-plane $\mathbb{H}$; its image is connected and contained in $\mathbb{C}\setminus\mathbb{R} = \mathbb{H}\cup(-\mathbb{H})$, and since $T(i)\in\mathbb{H}$, the image lies in $\mathbb{H}$. The inverse $T^{-1}$ is represented by $\begin{pmatrix}d&-b\\ -c&a\end{pmatrix}$, which again has real entries and determinant $ad-bc>0$, so $T^{-1}(\mathbb{H})\subseteq\mathbb{H}$. Hence $T(\mathbb{H}) = \mathbb{H}$.

Conversely, suppose $T(\mathbb{R}_\infty) = \mathbb{R}_\infty$. Choose three distinct real points $x_1,x_2,x_3$. Their images $y_j := T(x_j)$ lie in $\mathbb{R}_\infty$. Let $g(z) := (z,x_1;x_2,x_3)$ and $R(w) := (w,y_1;y_2;y_3)$, and put $S := R^{-1}\circ g$. Both $g$ and $R$ have real coefficients, because every number appearing in them is real; hence $S$ has real coefficients, since the inverse of a real matrix is real and a composition of real matrices is real. Also $S(x_j) = y_j = T(x_j)$ for $j = 1,2,3$. By uniqueness in Theorem 7.23, $S = T$. Hence $T$ has real coefficients up to a common factor.

If $T(\mathbb{H}) = \mathbb{H}$, then $T$ maps the boundary of $\mathbb{H}$ onto the boundary of its image, so $T(\mathbb{R}_\infty) = \mathbb{R}_\infty$ and $T$ has real coefficients. The computation of $\operatorname{Im}T(i)$ above then shows that $ad-bc$ and $\operatorname{Im}T(i)$ have the same sign; since $T(i)\in\mathbb{H}$, we get $ad-bc>0$. Conversely, real coefficients with $ad-bc>0$ give $T(\mathbb{H}) = \mathbb{H}$ by the first part.

**35.** By the computation in the proof of Theorem 7.38, the stereographic image of the circle $\Pi\cap S^2$ is the set of $z = x+iy$ satisfying

$$(\gamma-\delta)(x^2+y^2)+2\alpha x+2\beta y-(\gamma+\delta) = 0.$$

Since $\gamma\ne\delta$, put $A := \gamma-\delta\ne0$ and divide by $A$:

$$x^2+y^2+\frac{2\alpha}{A}x+\frac{2\beta}{A}y-\frac{\gamma+\delta}{A} = 0.$$

Completing the square,

$$\left(x+\frac{\alpha}{A}\right)^2+\left(y+\frac{\beta}{A}\right)^2 = \frac{\alpha^2+\beta^2}{A^2}+\frac{\gamma+\delta}{A} = \frac{\alpha^2+\beta^2+(\gamma+\delta)(\gamma-\delta)}{A^2} = \frac{\alpha^2+\beta^2+\gamma^2-\delta^2}{A^2}.$$

Therefore the centre is $-\alpha/A-i\beta/A = -(\alpha+i\beta)/(\gamma-\delta)$ and the radius is
$\sqrt{\alpha^2+\beta^2+\gamma^2-\delta^2}/\lvert\gamma-\delta\rvert$. The quantity under the square root is positive because the plane meets the sphere in a genuine circle, which requires its distance from the origin, $\lvert\delta\rvert/\sqrt{\alpha^2+\beta^2+\gamma^2}$, to be less than $1$.

**Check.** For the equator, $\alpha = \beta = \delta = 0$ and $\gamma = 1$: the formula gives centre $0$ and radius $1$, the unit circle. For the plane $Z = 1/2$, $\alpha = \beta = 0$, $\gamma = 1$, $\delta = 1/2$: the centre is $0$ and the radius is $\sqrt{1-1/4}/(1/2) = \sqrt3$, which agrees with solving $(\lvert z\rvert^2-1)/(\lvert z\rvert^2+1) = 1/2$.

**36.** Factor $z^n-1$ over $\mathbb{C}$:

$$z^n-1 = \prod_{k=0}^{n-1}(z-\omega^k), \qquad \omega = e^{2\pi i/n}.$$

Dividing by $z-1$ (the factor with $k=0$) and using the geometric sum,

$$1+z+\cdots+z^{n-1} = \prod_{k=1}^{n-1}(z-\omega^k).$$

Evaluate at $z = 1$: the left side equals $n$, so

$$n = \prod_{k=1}^{n-1}(1-\omega^k).$$

Taking moduli,

$$n = \prod_{k=1}^{n-1}\lvert 1-\omega^k\rvert.$$

Now

$$1-e^{2\pi ik/n} = e^{\pi ik/n}\left(e^{-\pi ik/n}-e^{\pi ik/n}\right) = -2i\,e^{\pi ik/n}\sin\frac{k\pi}{n},$$

so $\lvert 1-\omega^k\rvert = 2\sin(k\pi/n)$, which is positive for $1\le k\le n-1$ because $0<k\pi/n<\pi$. Therefore

$$n = 2^{n-1}\prod_{k=1}^{n-1}\sin\frac{k\pi}{n}, \qquad\text{that is,}\qquad \prod_{k=1}^{n-1}\sin\frac{k\pi}{n} = \frac{n}{2^{n-1}}.$$

**Check.** For $n = 2$: $\sin(\pi/2) = 1 = 2/2$. For $n = 3$: $\sin(\pi/3)\sin(2\pi/3) = (\sqrt3/2)^2 = 3/4 = 3/4$. For $n = 4$: $\sin(\pi/4)\sin(\pi/2)\sin(3\pi/4) = (\sqrt2/2)(1)(\sqrt2/2) = 1/2 = 4/8$.
