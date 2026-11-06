# Complex Numbers — Solutions

> [Tutorial](README.md) · [Exercises](exercises.md) · 40 worked solutions

Each solution states the strategy, carries out every step, and ends with a check that is
independent of the method used. Where a problem has a second natural approach, it is mentioned.

## Beginner

**1.** Add real parts and imaginary parts separately:
$$(3+2i)+(1-5i) = (3+1)+(2-5)i = 4-3i.$$
**Check.** Subtract the answer from the first term: $(3+2i)-(4-3i) = -1+5i$, which is the negative
of $1-5i$. Correct.

**2.** Expand and use $i^2=-1$:
$$(2+i)(3-4i) = 6-8i+3i-4i^2 = 6-5i+4 = 10-5i.$$
**Check.** $\lvert 2+i\rvert = \sqrt5$, $\lvert 3-4i\rvert = 5$, so the product must have modulus
$5\sqrt5$; and $\lvert 10-5i\rvert = \sqrt{100+25} = \sqrt{125} = 5\sqrt5$. Agrees.

**3.** Reduce the exponents modulo $4$: $17 = 4\cdot4+1$, so $i^{17} = i$; and $23 = 4\cdot5+3$, so
$i^{23} = i^3 = -i$. Therefore
$$i^{17}+i^{23} = i + (-i) = 0.$$
**Check.** $i^{17}i^{23} = i^{40} = (i^4)^{10} = 1$, consistent with the two numbers being $i$ and
$-i$.

**4.** Cube the coefficient and use $i^3 = -i$:
$$(2i)^3 = 2^3i^3 = 8(-i) = -8i.$$
**Check.** $(2i)^2 = 4i^2 = -4$, and $(-4)(2i) = -8i$. Agrees.

**5.** The conjugate changes the sign of the imaginary part, and the modulus is the square root of
$a^2+b^2$:
$$\bar z = 5+12i, \qquad \lvert z\rvert = \sqrt{25+144} = \sqrt{169} = 13, \qquad z\bar z = 13^2 = 169.$$
**Check.** $z\bar z = (5-12i)(5+12i) = 25+144 = 169$, and also $\lvert z\rvert^2 = 169$. The identity
$z\bar z = \lvert z\rvert^2$ holds.

**6.** Multiply numerator and denominator by the conjugate $1+i$ of the denominator:
$$\frac{3+i}{1-i} = \frac{(3+i)(1+i)}{(1-i)(1+i)} = \frac{3+3i+i+i^2}{1+1} = \frac{2+4i}{2} = 1+2i.$$
**Check.** $(1+2i)(1-i) = 1-i+2i-2i^2 = 3+i$, which is the original numerator. Correct.

**7.** The equation is $x^2 = -9$. Since $(\pm3i)^2 = 9i^2 = -9$, the solutions are
$$x = 3i \quad\text{or}\quad x = -3i.$$
**Check.** Both have square $-9$; a quadratic has at most two roots (Exercise 36), so this is the
complete list.

**8.** Use the quadratic formula with $a=1$, $b=-4$, $c=13$:
$$\Delta = b^2-4ac = 16-52 = -36, \qquad \sqrt{\Delta} = 6i, \qquad x = \frac{4 \pm 6i}{2} = 2 \pm 3i.$$
**Check by Vieta.** The sum is $(2+3i)+(2-3i) = 4 = -b/a$; the product is
$(2+3i)(2-3i) = 4+9 = 13 = c/a$. Both hold.

**9.** For $z = 1+i$: $\lvert z\rvert = \sqrt{1+1} = \sqrt2$, and since $a>0$ the argument is
$\arctan(1) = \pi/4$. Hence
$$1+i = \sqrt2\left(\cos\frac{\pi}{4}+i\sin\frac{\pi}{4}\right).$$
**Check.** $\sqrt2\cdot\frac{\sqrt2}{2} = 1$ for both the real and the imaginary part. Correct.

**10.** The point $-2$ lies on the negative real axis, so its distance is $2$ and its principal argument is
$\pi$ (not $-\pi$; the principal branch includes $+\pi$):
$$-2 = 2(\cos\pi+i\sin\pi).$$
**Check.** $\cos\pi = -1$ and $\sin\pi = 0$, giving $-2$. Correct.

**11.** The modulus is multiplicative, so no multiplication is needed:
$$\lvert(3+4i)(5-12i)\rvert = \lvert 3+4i\rvert\cdot\lvert 5-12i\rvert = 5\cdot 13 = 65.$$
**Check.** The direct product is $15-36i+20i-48i^2 = 63-16i$, whose modulus is
$\sqrt{3969+256} = \sqrt{4225} = 65$. Agrees.

**12.** Multiply the moduli and add the arguments:
$$2\cdot3 = 6, \qquad \frac{\pi}{6}+\frac{\pi}{3} = \frac{\pi}{2}, \qquad
2\left(\cos\frac{\pi}{6}+i\sin\frac{\pi}{6}\right)\cdot3\left(\cos\frac{\pi}{3}+i\sin\frac{\pi}{3}\right)
= 6\left(\cos\frac{\pi}{2}+i\sin\frac{\pi}{2}\right) = 6i.$$
**Check.** $2\left(\cos\frac{\pi}{6}+i\sin\frac{\pi}{6}\right) = 2\left(\frac{\sqrt3}{2}+\frac12 i\right) = \sqrt3+i$ and
$3\left(\cos\frac{\pi}{3}+i\sin\frac{\pi}{3}\right) = 3\left(\frac12+\frac{\sqrt3}{2}i\right) = \frac32+\frac{3\sqrt3}{2}i$.
Multiplying in Cartesian form gives real part $\sqrt3\cdot\frac32-1\cdot\frac{3\sqrt3}{2} = 0$ and
imaginary part $\sqrt3\cdot\frac{3\sqrt3}{2}+1\cdot\frac32 = \frac92+\frac32 = 6$, so the product is
$6i$. Agrees.

## Intermediate

**13.** Multiply numerator and denominator by the conjugate $1+i\sqrt3$:
$$\frac{1+i\sqrt3}{1-i\sqrt3} = \frac{(1+i\sqrt3)^2}{1^2+3} = \frac{1+2i\sqrt3+3i^2}{4} = \frac{-2+2i\sqrt3}{4} = -\frac12+\frac{\sqrt3}{2}i.$$
**Check.** The numerator has modulus $2$ and argument $\pi/3$; the denominator has modulus $2$ and
argument $-\pi/3$. The quotient therefore has modulus $1$ and argument $2\pi/3$, which is exactly
$-\frac12+\frac{\sqrt3}{2}i = \omega_3$. Correct.

**14.** Compute each fourth power by squaring twice:
$$(1+i)^2 = 2i \implies (1+i)^4 = (2i)^2 = -4, \qquad
(1-i)^2 = -2i \implies (1-i)^4 = (-2i)^2 = -4.$$
Hence $(1+i)^4+(1-i)^4 = -8$.
**Check.** $(1+i)^4 = (1+i)^2(1+i)^2 = (2i)(2i) = -4$; and $(1-i)^4$ is the complex conjugate of
$(1+i)^4$, hence also $-4$ because $-4$ is real. Agrees.

**15.** $\Delta = (-6)^2-4\cdot25 = 36-100 = -64$, so $\sqrt\Delta = 8i$ and
$$z = \frac{6\pm8i}{2} = 3\pm4i.$$
**Check by Vieta.** Sum $= 6 = -b/a$; product $= 9+16 = 25 = c/a$. Both correct.

**16.** Write $(a+bi)^2 = (a^2-b^2)+2abi = 5+12i$. Comparing parts,
$$a^2-b^2 = 5, \qquad 2ab = 12.$$
Since $\lvert (a+bi)^2\rvert = a^2+b^2$ and $\lvert 5+12i\rvert = 13$, we also get $a^2+b^2 = 13$.
Adding and subtracting:
$$2a^2 = 18 \implies a^2 = 9, \qquad 2b^2 = 8 \implies b^2 = 4.$$
So $a = \pm3$, $b = \pm2$, and $2ab = 12>0$ forces the same sign. The roots are
$$z = 3+2i \quad\text{and}\quad z = -3-2i.$$
**Check.** $(3+2i)^2 = 9+12i-4 = 5+12i$. Correct, and the other root is its negative.

**17.** For $z = 1-i$: $r = \sqrt2$ and $\theta = -\pi/4$. By De Moivre,
$$(1-i)^{10} = (\sqrt2)^{10}\left(\cos\left(-\frac{10\pi}{4}\right)+i\sin\left(-\frac{10\pi}{4}\right)\right)
= 32\left(\cos\left(-\frac{5\pi}{2}\right)+i\sin\left(-\frac{5\pi}{2}\right)\right).$$
Since $-\frac{5\pi}{2}+2\pi = -\frac{\pi}{2}$, this is $32\left(\cos\left(-\frac{\pi}{2}\right)+i\sin\left(-\frac{\pi}{2}\right)\right) = -32i$.
**Check by squaring.** $(1-i)^2 = -2i$, so $(1-i)^4 = -4$, $(1-i)^8 = 16$, and
$(1-i)^{10} = 16\cdot(-2i) = -32i$. Agrees.

**18.** Write $27 = 27(\cos0+i\sin0)$, so $\rho = 27$ and $\varphi = 0$. By Theorem 7.4,
$$z_k = 3\left(\cos\frac{2\pi k}{3}+i\sin\frac{2\pi k}{3}\right), \qquad k = 0,1,2,$$
that is
$$z_0 = 3, \qquad z_1 = 3\left(-\frac12+\frac{\sqrt3}{2}i\right) = -\frac32+\frac{3\sqrt3}{2}i, \qquad
z_2 = 3\left(-\frac12-\frac{\sqrt3}{2}i\right) = -\frac32-\frac{3\sqrt3}{2}i.$$
They are the vertices of an equilateral triangle inscribed in the circle of radius $3$, with one
vertex at $3$ on the positive real axis.
**Check.** $z_1^3 = 27\omega_3^3 = 27$ because $\omega_3^3 = 1$; the same for $z_2$. Also
$\lvert z_1\rvert = 3\sqrt{\frac14+\frac34} = 3$. Correct.

**19.** Write $-4 = 4(\cos\pi+i\sin\pi)$, so $\rho = 4$, $\varphi = \pi$ and $\rho^{1/4} = \sqrt2$. The
fourth roots are
$$z_k = \sqrt2\left(\cos\frac{\pi+2\pi k}{4}+i\sin\frac{\pi+2\pi k}{4}\right), \qquad k=0,1,2,3,$$
with angles $\pi/4,\ 3\pi/4,\ 5\pi/4,\ 7\pi/4$. In Cartesian form:
$$1+i, \qquad -1+i, \qquad -1-i, \qquad 1-i.$$
**Check.** $(1+i)^4 = ((1+i)^2)^2 = (2i)^2 = -4$, and each of the four numbers has the same fourth
power because they differ by factors of $i$ with $i^4 = 1$. Correct.

**20.** Write $1 = \cos0+i\sin0$; the cube roots are
$$z_k = \cos\frac{2\pi k}{3}+i\sin\frac{2\pi k}{3}, \qquad k = 0,1,2,$$
so the roots are
$$1, \qquad -\frac12+\frac{\sqrt3}{2}i, \qquad -\frac12-\frac{\sqrt3}{2}i.$$
The last two are conjugates, so their product is $1$ and their sum is $-1$; hence
$$z^3-1 = (z-1)\left(z^2+z+1\right).$$
**Check.** Expanding, $(z-1)(z^2+z+1) = z^3+z^2+z-z^2-z-1 = z^3-1$. Correct. (Equivalently,
$(z-\omega_3)(z-\omega_3^2) = z^2-(\omega_3+\omega_3^2)z+\omega_3^3 = z^2+z+1$.)

**21.** (a) $\lvert z-2i\rvert = 3$ says: the distance from $z$ to the point $2i$ equals $3$. That is the
circle with centre $2i = (0,2)$ and radius $3$.

(b) $\lvert z-1\rvert = \lvert z+1\rvert = \lvert z-(-1)\rvert$ says: the distance from $z$ to $1$
equals the distance from $z$ to $-1$. That is the perpendicular bisector of the segment joining $-1$
and $1$, which is the imaginary axis $\{z : \operatorname{Re}z = 0\}$.
**Check for (b).** If $z = yi$ then $\lvert yi-1\rvert = \sqrt{1+y^2} = \lvert yi+1\rvert$; if
$z = x+yi$ then the two squared distances differ by $(x-1)^2-(x+1)^2 = -4x$, which is non-zero
when $x\neq0$. Correct.

**22.** For $z = -\sqrt3+i$: $\lvert z\rvert = \sqrt{3+1} = 2$. The point is in the second quadrant with
reference angle $\arctan(1/\sqrt3) = \pi/6$, so
$$\theta = \pi-\frac{\pi}{6} = \frac{5\pi}{6}, \qquad z = 2\left(\cos\frac{5\pi}{6}+i\sin\frac{5\pi}{6}\right).$$
By De Moivre,
$$z^6 = 2^6\left(\cos5\pi+i\sin5\pi\right) = 64(-1+0i) = -64.$$
**Check.** $z^2 = 3-2i\sqrt3+i^2 = 2-2i\sqrt3$, and
$z^3 = (2-2i\sqrt3)(-\sqrt3+i) = -2\sqrt3+2i+6i+2\sqrt3 = 8i$. Then $z^6 = (8i)^2 = -64$. Agrees.

**23.** Compute the product directly:
$$(1+i)(\sqrt3-i) = \sqrt3-i+i\sqrt3-i^2 = (\sqrt3+1)+(\sqrt3-1)i.$$
Its modulus is
$$\sqrt{(\sqrt3+1)^2+(\sqrt3-1)^2} = \sqrt{(4+2\sqrt3)+(4-2\sqrt3)} = \sqrt8 = 2\sqrt2.$$
The argument is the sum of the arguments: $\frac{\pi}{4}+\left(-\frac{\pi}{6}\right) = \frac{\pi}{12}$,
and since both components are positive this is the principal argument.
**Check.** $\tan\frac{\pi}{12} = \frac{\sqrt3-1}{\sqrt3+1} = \frac{(\sqrt3-1)^2}{3-1} = \frac{4-2\sqrt3}{2} = 2-\sqrt3$,
which is the ratio of the imaginary to the real part above. Also $\lvert 1+i\rvert\lvert\sqrt3-i\rvert = \sqrt2\cdot2 = 2\sqrt2$. Both agree.

**24.** Use the quadratic formula with $a=1$, $b = -(3+2i)$, $c = 1+3i$:
$$\Delta = (3+2i)^2-4(1+3i) = (9+12i+4i^2)-4-12i = (5+12i)-4-12i = 1.$$
So $w = 1$ and
$$z = \frac{(3+2i)\pm1}{2} = \frac{4+2i}{2}\ \text{or}\ \frac{2+2i}{2} = 2+i\ \text{or}\ 1+i.$$
**Check by Vieta.** Sum $= 3+2i = -b/a$; product $= (2+i)(1+i) = 2+2i+i+i^2 = 1+3i = c/a$. Both
hold, so the roots are $z = 2+i$ and $z = 1+i$.

## Advanced

**25.** Let $u = z^2$. Then $u^2+u+1 = 0$, whose roots are the primitive cube roots of unity
$$u = \frac{-1\pm i\sqrt3}{2} = \omega_3, \ \omega_3^2.$$
Now solve $z^2 = \omega_3 = e^{2\pi i/3}$ and $z^2 = \omega_3^2 = e^{-2\pi i/3}$ with Theorem 7.4
($\rho = 1$, two roots each):
$$z = e^{i\pi/3},\ e^{i4\pi/3} \quad\text{and}\quad z = e^{-i\pi/3},\ e^{i2\pi/3}.$$
In Cartesian form,
$$\frac12+\frac{\sqrt3}{2}i, \qquad -\frac12+\frac{\sqrt3}{2}i, \qquad -\frac12-\frac{\sqrt3}{2}i, \qquad \frac12-\frac{\sqrt3}{2}i.$$
**Identification.** These are exactly the sixth roots of unity other than $\pm1$: they satisfy
$z^6 = 1$ but $z^3 = \pm1$ fails ($z^3 = -1$ indeed: $e^{i\pi} = -1$).
**Check by factorisation.** $z^4+z^2+1 = (z^2+z+1)(z^2-z+1)$, whose roots are the primitive cube
roots of unity and the roots of $z^2-z+1 = 0$, namely $e^{\pm i\pi/3}$. The four values agree.

**26.** By De Moivre, with $1+i = \sqrt2\,e^{i\pi/4}$,
$$(1+i)^n = 2^{n/2}\left(\cos\frac{n\pi}{4}+i\sin\frac{n\pi}{4}\right).$$
This is real exactly when $\sin\frac{n\pi}{4} = 0$, i.e. $\frac{n\pi}{4} \in \pi\mathbb{Z}$, i.e.
$n = 4k$ for an integer $k \ge 1$. Then
$$(1+i)^{4k} = 2^{2k}\cos(k\pi) = (-1)^k4^k.$$
**Check.** $k=1$: $(1+i)^4 = -4 = (-1)^14$; $k=2$: $(1+i)^8 = 16 = (-1)^24^2$. Correct. Note that
$n = 4k+2$ gives $(1+i)^n = \pm i\,2^{n/2}$, purely imaginary but not real.

**27.** Expand both squared moduli using $\lvert\zeta\rvert^2 = \zeta\bar\zeta$:
$$\lvert z+w\rvert^2 = (z+w)(\bar z+\bar w) = \lvert z\rvert^2+z\bar w+\bar zw+\lvert w\rvert^2
= \lvert z\rvert^2+2\operatorname{Re}(z\bar w)+\lvert w\rvert^2,$$
$$\lvert z-w\rvert^2 = (z-w)(\bar z-\bar w) = \lvert z\rvert^2-z\bar w-\bar zw+\lvert w\rvert^2
= \lvert z\rvert^2-2\operatorname{Re}(z\bar w)+\lvert w\rvert^2.$$
Adding, the mixed terms cancel:
$$\lvert z+w\rvert^2+\lvert z-w\rvert^2 = 2\lvert z\rvert^2+2\lvert w\rvert^2.$$
**Interpretation.** In the parallelogram with vertices $0,z,z+w,w$, the sides are $z$ and $w$ and
the diagonals are $z+w$ and $z-w$. The identity says that the sum of the squares of the diagonals
equals the sum of the squares of the four sides (each side appears twice, once as $z$ and once as
$w$). It is the parallelogram law of Euclidean geometry, proved here in one line of algebra.

**28.** Let $u = \dfrac{z+w}{1+zw}$; the denominator is non-zero by hypothesis. Since $\lvert z\rvert = \lvert w\rvert = 1$,
we have $z\bar z = w\bar w = 1$, so $\bar z = 1/z$ and $\bar w = 1/w$. Conjugate:
$$\bar u = \frac{\bar z+\bar w}{1+\bar z\bar w}
= \frac{\frac1z+\frac1w}{1+\frac{1}{zw}}
= \frac{\frac{z+w}{zw}}{\frac{zw+1}{zw}} = \frac{z+w}{1+zw} = u.$$
A complex number equal to its conjugate is real, so $u \in \mathbb{R}$.
**Check with an example.** $z = 1$, $w = i$: $u = \dfrac{1+i}{1+i} = 1$, real. And $z = i$, $w = -1$:
$u = \dfrac{i-1}{1-i} = \dfrac{-(1-i)}{1-i} = -1$, real. Correct.

**29.** Let $z = a+bi$ with $a,b\in\mathbb{R}$, so $\lvert\operatorname{Re}z\rvert = \lvert a\rvert$,
$\lvert\operatorname{Im}z\rvert = \lvert b\rvert$ and $\lvert z\rvert = \sqrt{a^2+b^2}$. Since both
sides are non-negative, it suffices to compare squares:
$$\left(\lvert a\rvert+\lvert b\rvert\right)^2 = a^2+2\lvert ab\rvert+b^2, \qquad
2\lvert z\rvert^2 = 2a^2+2b^2.$$
The inequality $a^2+2\lvert ab\rvert+b^2 \le 2a^2+2b^2$ is equivalent to
$$0 \le a^2-2\lvert ab\rvert+b^2 = \left(\lvert a\rvert-\lvert b\rvert\right)^2,$$
which is true. Equality holds exactly when $\lvert a\rvert = \lvert b\rvert$, that is, when
$\lvert\operatorname{Re}z\rvert = \lvert\operatorname{Im}z\rvert$.
**Check.** For $z = 3+4i$: $\lvert a\rvert+\lvert b\rvert = 7 \le \sqrt2\cdot5 \approx 7.07$, and the
inequality is strict because $3\neq4$. For $z = 1+i$: $1+1 = \sqrt2\cdot\sqrt2$. Correct.

**30.** Let $P(z) = \sum_{j=0}^n c_jz^j$ with every $c_j$ real, and suppose $P(\alpha) = 0$. Conjugating the
equation and using $\overline{c_j} = c_j$ and $\overline{\alpha^j} = \bar\alpha^j$,
$$0 = \overline{P(\alpha)} = \sum_{j=0}^n c_j\bar\alpha^j = P(\bar\alpha).$$
So $\bar\alpha$ is also a root. If $\alpha$ is not real then $\bar\alpha \neq \alpha$, so nonreal
roots occur in pairs.

Now let $n$ be odd. By the fundamental theorem of algebra, $P$ has exactly $n$ roots counted with
multiplicity. If none were real, the roots would split into pairs $\{\alpha,\bar\alpha\}$, giving an
even total — contradiction. Hence at least one root is real.
**Check.** $P(x) = x^3+x+1$ has real coefficients and odd degree; indeed it has one real root
($\approx -0.682$) and a conjugate pair. Correct.

**31.** Factor $z^n-1$ using its $n$ roots $1,\omega,\dots,\omega^{n-1}$: since the polynomial is monic of
degree $n$ with exactly these roots,
$$z^n-1 = \prod_{k=0}^{n-1}\left(z-\omega^k\right) = (z-1)\prod_{k=1}^{n-1}\left(z-\omega^k\right).$$
On the other hand $z^n-1 = (z-1)\left(1+z+\cdots+z^{n-1}\right)$. Cancelling the common factor
$z-1$ (a non-zero polynomial),
$$\prod_{k=1}^{n-1}\left(z-\omega^k\right) = 1+z+\cdots+z^{n-1}.$$
Setting $z = 1$ gives
$$\prod_{k=1}^{n-1}\left(1-\omega^k\right) = 1+1+\cdots+1 = n.$$
**Check for $n=3$.** $(1-\omega)(1-\omega^2) = 1-(\omega+\omega^2)+\omega^3 = 1-(-1)+1 = 3$. For
$n=4$: $(1-i)(1-(-1))(1+i) = (1-i)(2)(1+i) = 2\cdot2 = 4$. Both agree.

**32.** Taking moduli in $z^2 = \bar z$ gives $\lvert z\rvert^2 = \lvert\bar z\rvert = \lvert z\rvert$, so
$\lvert z\rvert\left(\lvert z\rvert-1\right) = 0$, i.e. $\lvert z\rvert = 0$ or $\lvert z\rvert = 1$.

* If $\lvert z\rvert = 0$ then $z = 0$, which indeed satisfies $0^2 = \bar 0$.
* If $\lvert z\rvert = 1$ then $\bar z = 1/z$, so the equation becomes $z^2 = 1/z$, i.e. $z^3 = 1$.
  Hence $z \in \{1, \omega_3, \omega_3^2\}$.

The solutions are
$$z = 0, \qquad z = 1, \qquad z = -\frac12+\frac{\sqrt3}{2}i, \qquad z = -\frac12-\frac{\sqrt3}{2}i.$$
**Check.** For $z = \omega_3$: $\omega_3^2 = -\frac12-\frac{\sqrt3}{2}i$ and $\bar\omega_3 = -\frac12-\frac{\sqrt3}{2}i$
(noting $\lvert\omega_3\rvert = 1$), so they agree. The same check works for $\omega_3^2$. Correct.
**Remark.** Squaring is not reversible in general, which is why the modulus argument — not
squaring — drives this solution.

**33.** Write $z = x+yi$. The condition $z+\bar z = 1$ gives $2x = 1$, so $x = \frac12$. The condition
$\lvert z\rvert = 1$ gives $x^2+y^2 = 1$, hence
$$y^2 = 1-\frac14 = \frac34 \implies y = \pm\frac{\sqrt3}{2}.$$
So
$$z = \frac12\pm\frac{\sqrt3}{2}i = e^{\pm i\pi/3}.$$
**Check.** $\lvert z\rvert^2 = \frac14+\frac34 = 1$, and $z+\bar z = 2\cdot\frac12 = 1$. Correct.
These are the two intersections of the unit circle with the vertical line $x = \frac12$.

**34.** The modulus is $\lvert Z\rvert = \sqrt{4^2+3^2} = 5\,\Omega$ and the phase is
$\arg Z = \arctan(3/4) \approx 0.6435$ rad $\approx 36.87^\circ$, so the impedance is inductive and
the voltage leads the current by that angle.

The current is
$$I = \frac{V}{Z} = \frac{10}{4+3i} = \frac{10(4-3i)}{25} = 1.6-1.2i \ \text{A}.$$
Its magnitude is $\lvert I\rvert = \sqrt{1.6^2+1.2^2} = \sqrt{2.56+1.44} = 2$ A, and its argument is
$\arctan(-1.2/1.6) = -\arctan(0.75) \approx -0.6435$ rad.
**Check.** $\lvert I\rvert = \lvert V\rvert/\lvert Z\rvert = 10/5 = 2$ A, agreeing. The phase
difference between voltage and current is $\arg V-\arg I = 0-(-0.6435) = +0.6435$ rad, i.e. the
current lags the voltage by $36.87^\circ$, as expected for an inductive load.

**35.** The multiplier is $m = 3\left(\cos\left(-\frac{2\pi}{3}\right)+i\sin\left(-\frac{2\pi}{3}\right)\right)$,
since a clockwise rotation by $120^\circ$ is an angle of $-\frac{2\pi}{3}$, and the length is
tripled. Hence
$$m = 3\left(-\frac12-\frac{\sqrt3}{2}i\right) = -\frac32-\frac{3\sqrt3}{2}i.$$
Now $1+i\sqrt3 = 2\left(\cos\frac{\pi}{3}+i\sin\frac{\pi}{3}\right)$, so
$$(1+i\sqrt3)\,m = 6\left(\cos\left(\frac{\pi}{3}-\frac{2\pi}{3}\right)+i\sin\left(\frac{\pi}{3}-\frac{2\pi}{3}\right)\right)
= 6\left(\cos\left(-\frac{\pi}{3}\right)+i\sin\left(-\frac{\pi}{3}\right)\right) = 3-3\sqrt3\,i.$$
**Check by direct expansion.**
$$(1+i\sqrt3)\left(-\frac32-\frac{3\sqrt3}{2}i\right) = -\frac32-\frac{3\sqrt3}{2}i-\frac{3\sqrt3}{2}i+\frac{9}{2} = 3-3\sqrt3\,i.$$
Agrees.
**Interpretation.** The point $1+i\sqrt3$ has modulus $2$ and argument $60^\circ$; the image has
modulus $6$ and argument $-60^\circ$, exactly a tripling combined with a clockwise turn through
$120^\circ$.

**36.** If $z_1z_2 = 0$, take moduli and use multiplicativity:
$$0 = \lvert 0\rvert = \lvert z_1z_2\rvert = \lvert z_1\rvert\lvert z_2\rvert.$$
A product of two non-negative reals is zero only when one factor is zero, so $\lvert z_1\rvert = 0$ or
$\lvert z_2\rvert = 0$; and $\lvert z\rvert = 0$ is equivalent to $z = 0$ (Definition 5.8).

For the deduction, let $P(z) = az^2+bz+c$ with $a\neq0$ and let $\alpha$ be a root. The factor
theorem gives $P(z) = (z-\alpha)Q(z)$ with $\deg Q = 1$, say $Q(z) = a(z-\beta)$; hence
$P(z) = a(z-\alpha)(z-\beta)$. If $\gamma$ is any root, then
$$0 = P(\gamma) = a(\gamma-\alpha)(\gamma-\beta),$$
and by absence of zero divisors one of the factors is zero, so $\gamma = \alpha$ or $\gamma = \beta$.
Thus there are at most two roots.
**Check.** The argument uses only F9-type algebra and the modulus, so it does not rely on the
quadratic formula.

## Challenge

**37.** Let $\omega = e^{2\pi i/7}$, so $\omega^7 = 1$ and $\omega \neq 1$. By Proposition 7.7 (or the
geometric sum formula applied to the seven roots of unity),
$$1+\omega+\omega^2+\omega^3+\omega^4+\omega^5+\omega^6 = 0.$$
Because $\omega^7 = 1$ and $\lvert\omega\rvert = 1$, conjugation acts as $\bar\omega = \omega^{-1} = \omega^6$.
Hence $\omega^6 = \bar\omega$, $\omega^5 = \bar\omega^2$ and $\omega^4 = \bar\omega^3$, so grouping
conjugate pairs,
$$0 = 1 + \left(\omega+\bar\omega\right) + \left(\omega^2+\bar\omega^2\right) + \left(\omega^3+\bar\omega^3\right)
= 1 + 2\cos\frac{2\pi}{7} + 2\cos\frac{4\pi}{7} + 2\cos\frac{6\pi}{7}.$$
Therefore
$$\cos\frac{2\pi}{7}+\cos\frac{4\pi}{7}+\cos\frac{6\pi}{7} = -\frac12.$$
**Check numerically.** The three cosines are approximately $0.6235$, $-0.2225$ and $-0.9010$, whose
sum is $-0.5000$. Correct.

**38.** Let $\zeta = e^{2\pi i/5}$. Since $\zeta^5 = 1$ and $\zeta \neq 1$,
$$1+\zeta+\zeta^2+\zeta^3+\zeta^4 = 0.$$
Now $\zeta^5 = 1$ gives $\bar\zeta = \zeta^4$ and $\bar\zeta^2 = \zeta^3$, so grouping,
$$0 = 1 + 2\cos\frac{2\pi}{5} + 2\cos\frac{4\pi}{5}.$$
Put $u = 2\cos\frac{2\pi}{5}$ and $v = 2\cos\frac{4\pi}{5}$. Then $u+v = -1$, and
$$uv = \left(\zeta+\zeta^4\right)\left(\zeta^2+\zeta^3\right) = \zeta^3+\zeta^4+\zeta^6+\zeta^7
= \zeta^3+\zeta^4+\zeta+\zeta^2 = -1,$$
using $\zeta^5 = 1$ and $1+\zeta+\zeta^2+\zeta^3+\zeta^4 = 0$. So $u$ and $v$ are the roots of
$$t^2-(u+v)t+uv = t^2+t-1 = 0, \qquad t = \frac{-1\pm\sqrt5}{2}.$$
Since $\frac{2\pi}{5} = 72^\circ$ lies in the first quadrant, $u = 2\cos72^\circ > 0$, so
$u = \frac{-1+\sqrt5}{2}$ and therefore
$$\cos72^\circ = \frac{\sqrt5-1}{4}.$$
The other root gives $2\cos144^\circ = \frac{-1-\sqrt5}{2}$, i.e.
$\cos144^\circ = -\frac{\sqrt5+1}{4}$.
**Check.** $\cos72^\circ \approx 0.3090$ and $\frac{\sqrt5-1}{4} \approx 0.3090$;
$\cos144^\circ \approx -0.8090$ and $-\frac{\sqrt5+1}{4} \approx -0.8090$. Also
$u+v = -1$: $0.6180 + (-1.6180) = -1$. Correct.

**39.** Let $\omega = e^{2\pi i/3}$, so $1+\omega+\omega^2 = 0$, $1+\omega = -\omega^2$ and $1+\omega^2 = -\omega$.

**(a)** Suppose $F_1 := z_1+\omega z_2+\omega^2z_3 = 0$, so $z_1 = -\omega z_2-\omega^2z_3$. Then
$$z_1-z_2 = -\omega z_2-\omega^2z_3-z_2 = -(1+\omega)z_2-\omega^2z_3 = \omega^2z_2-\omega^2z_3 = \omega^2\left(z_2-z_3\right),$$
and
$$z_3-z_1 = z_3+\omega z_2+\omega^2z_3 = \omega z_2+\left(1+\omega^2\right)z_3 = \omega z_2-\omega z_3 = \omega\left(z_2-z_3\right).$$
Taking moduli and using $\lvert\omega\rvert = 1$,
$$\lvert z_1-z_2\rvert = \lvert z_2-z_3\rvert = \lvert z_3-z_1\rvert.$$
All three sides are equal, and the points are distinct, so the triangle is equilateral.

**(b)** Multiply the two factors $F_1 = z_1+\omega z_2+\omega^2z_3$ and
$F_2 = z_1+\omega^2z_2+\omega z_3$. The diagonal terms give $z_1^2+z_2^2+z_3^2$;
the mixed terms collect as
$$\left(\omega^2+\omega\right)z_1z_2+\left(\omega+\omega^2\right)z_2z_3+\left(\omega+\omega^2\right)z_3z_1
= -\left(z_1z_2+z_2z_3+z_3z_1\right),$$
because $\omega+\omega^2 = -1$ and each pair of distinct indices appears twice with exponents
summing to $\omega+\omega^2$. Hence
$$F_1F_2 = z_1^2+z_2^2+z_3^2-\left(z_1z_2+z_2z_3+z_3z_1\right).$$
Therefore the identity $z_1^2+z_2^2+z_3^2 = z_1z_2+z_2z_3+z_3z_1$ holds exactly when $F_1F_2 = 0$,
which by Exercise 36 means $F_1 = 0$ or $F_2 = 0$.

If $F_1 = 0$, part (a) shows the triangle is equilateral. If $F_2 = 0$, conjugating the whole
configuration (which swaps $\omega$ and $\omega^2$) reduces to the same computation, so again the
triangle is equilateral.

Conversely, suppose the triangle is equilateral with vertices labelled counterclockwise, so that
rotation about $z_1$ through $60^\circ$ sends $z_2$ to $z_3$. Writing $\eta = e^{i\pi/3}$ and using
$\eta = -\omega^2$ and $1-\eta = -\omega$,
$$z_3 = \eta z_2+(1-\eta)z_1,$$
and substituting into $F_1$:
$$F_1 = z_1+\omega z_2+\omega^2\left(\eta z_2+(1-\eta)z_1\right)
= z_1\left(1+\omega^2(1-\eta)\right)+z_2\left(\omega+\omega^2\eta\right)
= z_1\left(1-\omega^3\right)+z_2\left(\omega-\omega\right) = 0,$$
since $\omega^2(1-\eta) = \omega^2(-\omega) = -\omega^3 = -1$ and $\omega^2\eta = \omega^2(-\omega^2) = -\omega^4 = -\omega$.
For the opposite orientation the same computation gives $F_2 = 0$.

Hence the identity holds exactly for equilateral triangles.
**Check on an example.** For the equilateral triangle $1,\omega,\omega^2$:
$1^2+\omega^2+\omega^4 = 1+\omega^2+\omega$ and $\omega+\omega^2+\omega^3 = \omega+\omega^2+1$; both
equal $1+\omega+\omega^2$, so the identity holds. And indeed
$F_1 = 1+\omega\cdot\omega+\omega^2\cdot\omega^2 = 1+\omega^2+\omega^4 = 0$.

**40.** The polygon's vertices are $P_k = \omega_n^k = e^{2\pi i k/n}$, $k = 0,\dots,n-1$, all on the unit
circle. Join the centre $0$ to consecutive vertices. This divides the polygon into $n$ congruent
isosceles triangles, each with two sides of length $1$ and included angle
$\angle P_k0P_{k+1} = \frac{2\pi}{n}$.

The area of a triangle with sides $r, s$ enclosing angle $\theta$ is $\frac12rs\sin\theta$, so each
triangle has area $\frac12\sin\frac{2\pi}{n}$, and the polygon has area
$$A_n = n\cdot\frac12\sin\frac{2\pi}{n} = \frac{n}{2}\sin\frac{2\pi}{n}.$$
**Check for $n=4$.** $A_4 = 2\sin\frac{\pi}{2} = 2$, which is the area of the square with vertices
$\pm1,\pm i$ (side $\sqrt2$, so area $2$). Correct.
**Check for $n=6$.** $A_6 = 3\sin\frac{\pi}{3} = \frac{3\sqrt3}{2}$, which is the standard area of a
regular hexagon of side $1$. Correct.
**Alternative derivation.** The shoelace formula for a polygon with vertices $(x_k,y_k)$ gives
$A = \frac12\sum_k\left(x_ky_{k+1}-x_{k+1}y_k\right)$; here that summand equals
$\sin\frac{2\pi}{n}$ for every $k$, recovering $A = \frac n2\sin\frac{2\pi}{n}$.
