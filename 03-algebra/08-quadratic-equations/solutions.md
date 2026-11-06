# Quadratic Equations — Solutions

> [Tutorial](README.md) · [Exercises](exercises.md) · 36 worked solutions

Every solution states the method and why it applies, carries out each algebraic step, checks the roots
by substitution, and — where the problem comes from a context — states the interpretation and the
reason for accepting or rejecting each root.

## Beginner

**1.** *Method: square roots.*

$$
x^2 - 16 = 0 \iff x^2 = 16 \iff x = \pm 4 .
$$

*Check:* $(\pm4)^2 - 16 = 16 - 16 = 0$. ✓ The solution set is $\{-4, 4\}$. Both signs are required:
$u^2 = k$ with $k > 0$ has exactly the two solutions $u = \pm\sqrt{k}$.

**2.** *Method: square roots.* Divide by $5$, then take roots:

$$
5x^2 = 45 \iff x^2 = 9 \iff x = \pm 3 .
$$

*Check:* $5 \cdot 9 = 45$. ✓ The solution set is $\{-3, 3\}$.

**3.** *Method: factoring.* We need $p + q = 6$ and $pq = 8$; since both $b$ and $c$ are positive, both are
positive, and the pair $(2,4)$ has sum $6$ and product $8$. Hence

$$
x^2 + 6x + 8 = (x+2)(x+4) = 0 \iff x = -2 \text{ or } x = -4 .
$$

*Check:* $(-2)^2 + 6(-2) + 8 = 4 - 12 + 8 = 0$ ✓ and $(-4)^2 - 24 + 8 = 0$ ✓. *Corroboration:*
$\Delta = 36 - 32 = 4 = 2^2$, a perfect square, as an integer factorisation requires.

**4.** *Method: factoring.* Here $p + q = -7$ and $pq = 10$, so both are negative; the pair $(-2,-5)$ works:

$$
x^2 - 7x + 10 = (x-2)(x-5) = 0 \iff x = 2 \text{ or } x = 5 .
$$

*Check:* $4 - 14 + 10 = 0$ ✓ and $25 - 35 + 10 = 0$ ✓.

**5.** *Method: common factor.* There is no constant term, so $x$ is a common factor:

$$
3x^2 - 12x = 3x(x - 4) = 0 \iff x = 0 \text{ or } x = 4 .
$$

*Check:* $3(0) - 0 = 0$ ✓ and $3(16) - 48 = 0$ ✓. *Warning:* dividing both sides by $3x$ at the start
would have produced $x = 4$ only, losing the solution $x = 0$; division by a quantity that can vanish
is never legitimate.

**6.** *Method: square roots.* The variable appears only inside a square:

$$
(x-5)^2 = 9 \iff x - 5 = \pm 3 \iff x = 8 \text{ or } x = 2 .
$$

*Check:* $(8-5)^2 = 9$ ✓ and $(2-5)^2 = 9$ ✓. Expanding first gives $x^2 - 10x + 16 = 0 = (x-2)(x-8)$,
the same roots.

**7.** *Method: perfect square.* The left side is a perfect-square trinomial, since $2 \cdot x \cdot 1 = 2x$:

$$
x^2 + 2x + 1 = (x+1)^2 = 0 \iff x = -1 .
$$

*Check:* $1 - 2 + 1 = 0$ ✓. This root has multiplicity $2$: $(x+1)^2$ divides the polynomial twice. The
discriminant confirms it, $\Delta = 4 - 4 = 0$, so there is exactly one real solution — the parabola
touches the axis at its vertex $(-1,0)$.

**8.** *Method: quadratic formula.* Here $a = 1$, $b = -4$, $c = -12$, so

$$
\Delta = (-4)^2 - 4(1)(-12) = 16 + 48 = 64, \qquad x = \frac{4 \pm \sqrt{64}}{2} = \frac{4 \pm 8}{2}.
$$

Hence $x = 6$ or $x = -2$.

*Checks:* $36 - 24 - 12 = 0$ ✓ and $4 + 8 - 12 = 0$ ✓. Since $\Delta = 64 = 8^2$ is a perfect square
the roots are rational, and indeed $x^2-4x-12 = (x-6)(x+2)$.

**9.** *Method: $ac$ method, then factoring.* With $a = 2$, $c = -2$ we have $ac = -4$ and $b = 3$; the pair
$(4,-1)$ has sum $3$ and product $-4$. Splitting the middle term,

$$
2x^2 + 3x - 2 = 2x^2 + 4x - x - 2 = 2x(x+2) - (x+2) = (2x-1)(x+2) = 0,
$$

so $x = \tfrac12$ or $x = -2$.

*Checks:* $2\left(\tfrac14\right) + \tfrac32 - 2 = \tfrac12 + \tfrac32 - 2 = 0$ ✓ and $2(4) - 6 - 2 = 0$ ✓.
The discriminant is $9 + 16 = 25 = 5^2$, and the formula gives $\frac{-3 \pm 5}{4} \in \left\{\tfrac12, -2\right\}$ ✓.

**10.** Here $a = 2$, $b = -3$, $c = 4$, so

$$
\Delta = b^2 - 4ac = (-3)^2 - 4 \cdot 2 \cdot 4 = 9 - 32 = -23 .
$$

Since $\Delta < 0$ there are **no real solutions**: the equation $(x - h)^2 = \Delta/(4a^2)$ would
require a square to equal a negative number. *Corroboration:* completing the square,

$$
2x^2 - 3x + 4 = 2\left(x - \tfrac34\right)^2 + \tfrac{23}{8},
$$

which is at least $\tfrac{23}{8} > 0$ for every real $x$. The vertex is $\left(\tfrac34, \tfrac{23}{8}\right)$
and the parabola lies entirely above the axis. Over $\mathbb{C}$ the solutions are
$x = \dfrac{3 \pm i\sqrt{23}}{4}$.

**11.** *Method: completing the square.*

$$
y = x^2 - 8x + 11 = \left(x^2 - 8x + 16\right) - 16 + 11 = (x-4)^2 - 5 .
$$

The vertex is $(4,-5)$. *Checks:* expanding gives $x^2 - 8x + 16 - 5 = x^2 - 8x + 11$ ✓; the vertex
formula gives $h = -\frac{-8}{2} = 4$ and $k = \frac{4(1)(11) - 64}{4} = \frac{-20}{4} = -5$ ✓. Since
$a = 1 > 0$ the vertex is a minimum.

**12.** From $y = 3(x+2)^2 - 12$ we read off $h = -2$, $k = -12$, and $a = 3 > 0$:

* vertex $(-2,-12)$;
* axis of symmetry $x = -2$;
* the parabola opens **upward**, so $(-2,-12)$ is the minimum.

For the $x$-intercepts set $y = 0$:

$$
3(x+2)^2 - 12 = 0 \iff (x+2)^2 = 4 \iff x + 2 = \pm 2 \iff x = 0 \text{ or } x = -4 .
$$

So the intercepts are $(0,0)$ and $(-4,0)$. *Check:* $y(0) = 3(4) - 12 = 0$ ✓ and $y(-4) = 3(4) - 12 = 0$ ✓.
The $y$-intercept is $y(0) = 0$, the same point, because one $x$-intercept happens to lie on the $y$-axis.

## Intermediate

**13.** *Method: completing the square.* Since $\left(\tfrac{10}{2}\right)^2 = 25$,

$$
x^2 + 10x + 7 = (x+5)^2 - 25 + 7 = (x+5)^2 - 18 .
$$

Setting this to zero gives $(x+5)^2 = 18$, hence $x + 5 = \pm\sqrt{18} = \pm 3\sqrt2$ and

$$
x = -5 \pm 3\sqrt2 .
$$

*Check* for $x = -5 + 3\sqrt2$: $x^2 = 25 - 30\sqrt2 + 18 = 43 - 30\sqrt2$; $10x = -50 + 30\sqrt2$; adding
$7$ gives $43 - 30\sqrt2 - 50 + 30\sqrt2 + 7 = 0$ ✓. Numerically $x \approx -0.757$ or $x \approx -9.243$.
*Corroboration:* $\Delta = 100 - 28 = 72 > 0$, and $\frac{-10 \pm \sqrt{72}}{2} = -5 \pm 3\sqrt2$ ✓.

**14.** *Method: completing the square.* First divide by $2$ so that the leading coefficient is $1$:

$$
2x^2 - 8x + 3 = 0 \iff x^2 - 4x + \tfrac32 = 0 \iff (x-2)^2 - 4 + \tfrac32 = 0 \iff (x-2)^2 = \tfrac52 .
$$

Hence $x = 2 \pm \sqrt{\tfrac52} = 2 \pm \dfrac{\sqrt{10}}{2}$.

*Check* in the original equation for $x = 2 + \frac{\sqrt{10}}{2}$. First,
$x^2 = 4 + 2\sqrt{10} + \frac{10}{4} = \frac{13}{2} + 2\sqrt{10}$, so $2x^2 = 13 + 4\sqrt{10}$. Also
$8x = 16 + 4\sqrt{10}$. Hence $2x^2 - 8x + 3 = \left(13 + 4\sqrt{10}\right) - \left(16 + 4\sqrt{10}\right) + 3 = 0$ ✓.
*Corroboration:* $\Delta = 64 - 24 = 40$, and $\frac{8 \pm \sqrt{40}}{4} = 2 \pm \frac{\sqrt{10}}{2}$ ✓.

**15.** *Method: quadratic formula.* $a = 3$, $b = -7$, $c = 2$:

$$
\Delta = 49 - 24 = 25, \qquad x = \frac{7 \pm 5}{6} \in \left\{2, \tfrac13\right\}.
$$

*Checks:* $3(4) - 14 + 2 = 0$ ✓ and $3\left(\tfrac19\right) - \tfrac73 + 2 = \tfrac13 - \tfrac73 + 2 = 0$ ✓.
Since $\Delta = 25 = 5^2$ is a perfect square, factoring also works:
$3x^2 - 7x + 2 = (3x-1)(x-2)$.

**16.** *Method: standard form, then factoring.* Subtract the right side:

$$
x^2 = 4x + 5 \iff x^2 - 4x - 5 = 0 \iff (x-5)(x+1) = 0,
$$

so $x = 5$ or $x = -1$. *Checks:* $25 = 20 + 5$ ✓ and $1 = -4 + 5$ ✓. Here $p + q = -4$ and
$pq = -5$, giving $p, q = -5, 1$.

**17.** *Method: discriminant.* Exactly one real solution means the discriminant vanishes:

$$
\Delta = k^2 - 4 \cdot 1 \cdot 25 = k^2 - 100 = 0 \iff k = \pm 10 .
$$

*Checks:* for $k = 10$, $x^2 + 10x + 25 = (x+5)^2$ has the single root $-5$ ✓; for $k = -10$,
$x^2 - 10x + 25 = (x-5)^2$ has the single root $5$ ✓. Both are perfect squares, as Proposition 8.2 of
the tutorial requires.

**18.** *Method: discriminant, then vertex form for the complex roots.* Here $a = 1$, $b = -6$, $c = 11$:

$$
\Delta = 36 - 4 \cdot 1 \cdot 11 = 36 - 44 = -8 < 0 .
$$

Since $\Delta < 0$ the equation has no real solutions. Completing the square shows the same thing
directly: $x^2 - 6x + 11 = (x-3)^2 + 2$, which is at least $2 > 0$ for every real $x$, so the parabola
never meets the axis.

Over $\mathbb{C}$ the formula continues to apply, with $\sqrt{-8} = i\sqrt8 = 2i\sqrt2$:

$$
x = \frac{6 \pm 2i\sqrt2}{2} = 3 \pm i\sqrt2 .
$$

*Check* for $x = 3 + i\sqrt2$: $(3+i\sqrt2)^2 = 9 + 6i\sqrt2 - 2 = 7 + 6i\sqrt2$; $-6x = -18 - 6i\sqrt2$;
adding $11$ gives $7 + 6i\sqrt2 - 18 - 6i\sqrt2 + 11 = 0$ ✓.

**19.** *Let $w$ be the width in centimetres.* Then the length is $w + 4$, and the area condition is

$$
w(w+4) = 96 \iff w^2 + 4w - 96 = 0 \iff (w + 12)(w - 8) = 0,
$$

since $12 \cdot (-8) = -96$ and $12 + (-8) = 4$. So $w = 8$ or $w = -12$.

*Filter:* a width must be positive, so $w = -12$ is rejected. The rectangle is $8\ \mathrm{cm}$ by
$12\ \mathrm{cm}$.

*Check:* $8 \cdot 12 = 96\ \mathrm{cm^2}$ ✓ and $12 - 8 = 4\ \mathrm{cm}$ ✓. Note that $w = -12$ is a
perfectly good root of the equation — it is the width of a "rectangle" with a negative side — but it is
not a solution of the problem. Stating the domain before solving is what makes the rejection principled
rather than arbitrary.

**20.** *Method: clear fractions, then the formula.* Multiply every term by $6$:

$$
\frac{x^2}{3} - \frac{x}{2} = 2 \iff 2x^2 - 3x = 12 \iff 2x^2 - 3x - 12 = 0 .
$$

Then $\Delta = (-3)^2 - 4 \cdot 2 \cdot (-12) = 9 + 96 = 105$, so

$$
x = \frac{3 \pm \sqrt{105}}{4} \approx 3.312 \text{ or } -1.812 .
$$

*Check* numerically for the positive root: $\frac{3.312^2}{3} - \frac{3.312}{2} \approx 3.656 - 1.656 = 2.000$ ✓.
Since $105$ is not a perfect square the roots are irrational and no rational factorisation exists.

**21.** *Method: Vieta's formulas.* For $3x^2 - 6x + 2 = 0$ we have $a = 3$, $b = -6$, $c = 2$, so

$$
\alpha + \beta = -\frac{b}{a} = 2, \qquad \alpha\beta = \frac{c}{a} = \frac23 .
$$

Then

$$
\frac{1}{\alpha} + \frac{1}{\beta} = \frac{\alpha + \beta}{\alpha\beta} = \frac{2}{2/3} = 3,
\qquad
\alpha^2 + \beta^2 = (\alpha+\beta)^2 - 2\alpha\beta = 4 - \frac43 = \frac83 .
$$

*Check by solving:* $\Delta = 36 - 24 = 12$, so $\alpha, \beta = \frac{6 \pm 2\sqrt3}{6} = 1 \pm \frac{\sqrt3}{3}$.
Their sum is $2$ ✓ and their product is $1 - \frac13 = \frac23$ ✓. Also
$\alpha^2 + \beta^2 = 2\left(1 + \frac13\right) = \frac83$ ✓.

**22.** *Method: build from the roots.* If the roots are $r_1 = \tfrac23$ and $r_2 = -4$, then
$x^2 - (r_1+r_2)x + r_1r_2 = 0$ with $r_1 + r_2 = \tfrac23 - 4 = -\tfrac{10}{3}$ and
$r_1r_2 = -\tfrac83$. Hence

$$
x^2 + \frac{10}{3}x - \frac83 = 0 .
$$

Multiplying by $3$ clears the denominators:

$$
3x^2 + 10x - 8 = 0 .
$$

*Check:* $3\left(x - \tfrac23\right)(x+4) = (3x-2)(x+4) = 3x^2 + 12x - 2x - 8 = 3x^2 + 10x - 8$ ✓. Both
roots can also be read from the factored form: $x = \tfrac23$ and $x = -4$ ✓.

**23.** *Method: substitution.* The equation is quadratic in $x^2$; put $u = x^2$:

$$
u^2 - 13u + 36 = 0 \iff (u-4)(u-9) = 0 \iff u = 4 \text{ or } u = 9,
$$

since $(-4)(-9) = 36$ and $-4 - 9 = -13$. Substituting back, $x^2 = 4$ gives $x = \pm2$ and $x^2 = 9$
gives $x = \pm3$. The solution set is $\{-3, -2, 2, 3\}$.

*Checks:* $x = 2$: $16 - 52 + 36 = 0$ ✓; $x = 3$: $81 - 117 + 36 = 0$ ✓; the negatives give the same
values because only even powers occur.

**24.** *Method: square roots.* Divide by $2$, then take roots:

$$
2(x-1)^2 = 10 \iff (x-1)^2 = 5 \iff x - 1 = \pm\sqrt5 \iff x = 1 \pm \sqrt5 .
$$

*Check* for $x = 1+\sqrt5$: $(x-1)^2 = 5$, so $2 \cdot 5 = 10$ ✓. Numerically $x \approx 3.236$ or
$x \approx -1.236$. The vertex of $y = 2(x-1)^2 - 10$ is $(1,-10)$, and the roots are at distance
$\sqrt5$ on either side of the axis $x = 1$.

## Advanced

**25.** *Method: quadratic formula over $\mathbb{C}$.* With $a = 1$, $b = 4$, $c = 13$,

$$
\Delta = 16 - 52 = -36 < 0, \qquad x = \frac{-4 \pm \sqrt{-36}}{2} = \frac{-4 \pm 6i}{2} = -2 \pm 3i .
$$

*Checks:* for $x = -2+3i$,
$(-2+3i)^2 = 4 - 12i + 9i^2 = 4 - 12i - 9 = -5 - 12i$; $4x = -8 + 12i$; adding $13$ gives
$-5 - 12i - 8 + 12i + 13 = 0$ ✓. For the conjugate, the imaginary parts cancel with the opposite
signs and the same computation gives $0$ ✓.

The roots are complex conjugates, as they must be for a real quadratic with $\Delta < 0$, and their
real part $-2 = -\frac{b}{2a}$ is the axis of symmetry. In vertex form $x^2+4x+13 = (x+2)^2 + 9 \geq 9$,
so the parabola lies strictly above the axis.

**26.** *Method: isolate the radical and square, then check.* The equation $\sqrt{2x+5} = x+1$ requires
$2x + 5 \geq 0$ for the radical to be real. Squaring both sides:

$$
2x + 5 = (x+1)^2 = x^2 + 2x + 1 \iff 5 = x^2 + 1 \iff x^2 = 4 \iff x = \pm 2 .
$$

*Check in the original equation:*

* $x = 2$: left side $\sqrt{4+5} = 3$; right side $2 + 1 = 3$. ✓
* $x = -2$: left side $\sqrt{-4+5} = 1$; right side $-2 + 1 = -1$. ✗ Since $1 \neq -1$, this is not a
  solution.

The only solution is $x = 2$.

*Why the extraneous root appeared.* Squaring is not reversible: $A = B$ implies $A^2 = B^2$, but
$A^2 = B^2$ implies only $A = B$ **or** $A = -B$. The value $x = -2$ satisfies $\sqrt{2x+5} = -(x+1)$,
the equation with the sign flipped. Substituting into the original equation is therefore not optional
but part of the method: it is the step that restores the lost information.

**27.** *Method: factor and use a sign chart.* Factor the quadratic:

$$
x^2 - 3x - 10 = (x-5)(x+2).
$$

The factors vanish at $x = 5$ and $x = -2$, so the sign of the product can change only there:

| Interval | Sign of $x-5$ | Sign of $x+2$ | Sign of product |
|---|---|---|---|
| $x < -2$ | $-$ | $-$ | $+$ |
| $-2 < x < 5$ | $-$ | $+$ | $-$ |
| $x > 5$ | $+$ | $+$ | $+$ |

The inequality is $\leq 0$, so it holds on the middle interval, including the endpoints where the
product is exactly zero. The solution set is $\boxed{[-2,5]}$.

*Checks:* $x = 0$ (interior) gives $-10 \leq 0$ ✓; $x = -2$ gives $4 + 6 - 10 = 0 \leq 0$ ✓; $x = 5$
gives $25 - 15 - 10 = 0 \leq 0$ ✓; $x = 6$ gives $36 - 18 - 10 = 8 > 0$, so $6$ is correctly excluded.

**28.** *Method: factor and use a sign chart.* The quadratic factors as

$$
3x^2 + 2x - 8 = (3x - 4)(x + 2),
$$

whose zeros are $x = \tfrac43$ and $x = -2$. Because $a = 3 > 0$ the parabola opens upward, so it is
positive outside the interval between the roots:

$$
x < -2 \quad \text{or} \quad x > \tfrac43 .
$$

In interval notation the solution set is $\left(-\infty, -2\right) \cup \left(\tfrac43, \infty\right)$,
with the endpoints excluded because the inequality is strict.

*Checks:* at $x = 0$ (between the roots) the value is $-8$, not positive, so $0$ is correctly excluded;
at $x = -3$ the value is $27 - 6 - 8 = 13 > 0$ ✓; at $x = 2$ it is $12 + 4 - 8 = 8 > 0$ ✓.

**29.** *Vertex form.*

$$
y = -x^2 + 6x - 5 = -\left(x^2 - 6x\right) - 5 = -\left[(x-3)^2 - 9\right] - 5 = -(x-3)^2 + 4 .
$$

*Features.* Vertex $(3,4)$; axis of symmetry $x = 3$; $a = -1 < 0$, so the parabola opens **downward**
and the vertex is the maximum.

*Intercepts.* The $y$-intercept is $y(0) = -5$, i.e. $(0,-5)$. The $x$-intercepts solve

$$
-(x-3)^2 + 4 = 0 \iff (x-3)^2 = 4 \iff x - 3 = \pm 2 \iff x = 1 \text{ or } x = 5,
$$

so $(1,0)$ and $(5,0)$.

*Description of the graph.* A downward parabola with its peak at $(3,4)$, passing through $(0,-5)$,
$(1,0)$ and $(5,0)$. By symmetry the axis $x = 3$ is the midpoint of the intercepts,
$\frac{1+5}{2} = 3$ ✓, and the vertical distance from the vertex to the $x$-axis is $4$, while the
horizontal distance from the axis to each intercept is $\frac{\sqrt\Delta}{2|a|} = \frac{\sqrt{16}}{2} = 2$ ✓,
since $\Delta = 36 - 20 = 16$.

**30.** *Setup.* The height is $h(t) = -4.9t^2 + 24.5t$ metres, with $t \geq 0$ in seconds. Here $a = -4.9$,
$b = 24.5$, $c = 0$.

*Maximum height.* The vertex occurs at

$$
t = -\frac{b}{2a} = -\frac{24.5}{2(-4.9)} = 2.5\ \text{s},
\qquad
h(2.5) = -4.9(6.25) + 24.5(2.5) = -30.625 + 61.25 = 30.625\ \text{m}.
$$

So the ball reaches $30.625\ \mathrm{m}$ after $2.5\ \mathrm{s}$. This is the maximum because $a < 0$.

*Return to the ground.* Solve $h(t) = 0$:

$$
-4.9t^2 + 24.5t = -4.9t(t - 5) = 0 \iff t = 0 \text{ or } t = 5 .
$$

$t = 0$ is the launch instant and $t = 5\ \mathrm{s}$ is the landing time.

*Interpretation.* The upward speed $24.5\ \mathrm{m/s}$ is removed at $9.8\ \mathrm{m/s}$ per second, so
the rise lasts $2.5$ s; the flight is symmetric, so the fall also lasts $2.5$ s and the total is $5$ s.
Both roots are physically meaningful here — the launch instant is a genuine moment when the height is
zero — which is why neither is discarded.

**31.** *Setup.* Units sold $x$ (units per week), price $p = 120 - 2x$ (dollars per unit), so revenue is

$$
R(x) = xp = x(120 - 2x) = -2x^2 + 120x \quad \text{(dollars per week)}.
$$

*Maximum.* This is a downward parabola; the vertex is at

$$
x = -\frac{120}{2(-2)} = 30\ \text{units}, \qquad p = 120 - 60 = 60\ \text{dollars per unit},
$$

and the maximum revenue is $R(30) = 30 \cdot 60 = 1800$ dollars per week.

*Checks.* $R(29) = 29 \cdot 62 = 1798$ and $R(31) = 31 \cdot 58 = 1798$, both below $1800$ ✓. The
roots of $R$ are $x = 0$ and $x = 60$, and the vertex is their midpoint $30$ ✓.

*Interpretation and domain.* The model makes sense for $0 \leq x \leq 60$; beyond $60$ units the price
formula would give a negative price. Units are consistent: units $\times$ dollars per unit = dollars,
so revenue is in dollars per week.

**32.** *Proof.* Let $p(x) = ax^2 + bx + c$ with $a \neq 0$ and roots $r_1, r_2$. By the factor theorem,
$p(x) = a(x - r_1)(x - r_2)$: the two linear factors are exact, and the leading coefficient $a$
restores the degree and the leading term. Expanding the right side,

$$
a(x-r_1)(x-r_2) = a\left(x^2 - (r_1+r_2)x + r_1r_2\right) = ax^2 - a(r_1+r_2)x + a\,r_1r_2 .
$$

Two polynomials are equal exactly when their coefficients agree, so comparing the coefficient of $x$
gives

$$
b = -a(r_1 + r_2) \quad\Longrightarrow\quad r_1 + r_2 = -\frac{b}{a},
$$

and comparing constant terms gives

$$
c = a\,r_1r_2 \quad\Longrightarrow\quad r_1r_2 = \frac{c}{a}.
$$

$\blacksquare$

*Remark.* The argument uses only the factor theorem and coefficient comparison; it does not require the
roots to be real, so the formulas hold for complex roots as well. An alternative proof uses the
quadratic formula: adding and multiplying $\frac{-b+\sqrt\Delta}{2a}$ and $\frac{-b-\sqrt\Delta}{2a}$
gives $-\frac{b}{a}$ and $\frac{b^2-\Delta}{4a^2} = \frac{4ac}{4a^2} = \frac{c}{a}$. Both routes are
complete, but the first is preferable because it generalises to higher degree.

## Challenge

**33.** *Step 1: determine $b$ and $c$.* Since $2+\sqrt5$ is a root of $x^2+bx+c$,

$$
(2+\sqrt5)^2 + b(2+\sqrt5) + c = 0 .
$$

Compute $(2+\sqrt5)^2 = 4 + 4\sqrt5 + 5 = 9 + 4\sqrt5$, and separate the rational and irrational parts:

$$
\left(9 + 2b + c\right) + \left(4 + b\right)\sqrt5 = 0 .
$$

Because $\sqrt5$ is irrational, a number of the form $u + v\sqrt5$ with $u, v \in \mathbb{Q}$ is zero if
and only if $u = 0$ and $v = 0$ (otherwise $\sqrt5 = -u/v$ would be rational). Hence

$$
4 + b = 0 \ \Rightarrow\ b = -4, \qquad 9 + 2(-4) + c = 0 \ \Rightarrow\ c = -1 .
$$

So the equation is $x^2 - 4x - 1 = 0$.

*Step 2: find the other root.* By Vieta, $r_1 + r_2 = 4$, so with $r_1 = 2+\sqrt5$ we get
$r_2 = 4 - (2+\sqrt5) = 2 - \sqrt5$. Hence

$$
\boxed{b = -4,\quad c = -1,\quad \text{other root } 2-\sqrt5 } .
$$

*Step 3: prove the other root must be the conjugate.* The computation of Step 1 shows that any
rational $b, c$ admitting $2+\sqrt5$ as a root must satisfy $b = -4$ and $c = -1$. For those values,

$$
(2-\sqrt5)^2 - 4(2-\sqrt5) - 1 = (9 - 4\sqrt5) - 8 + 4\sqrt5 - 1 = 0 ,
$$

so $2-\sqrt5$ is indeed a root. Therefore the other root is forced to be $2-\sqrt5$; it could not be
anything else. $\blacksquare$

*Check.* $(x - (2+\sqrt5))(x-(2-\sqrt5)) = (x-2)^2 - 5 = x^2 - 4x - 1$ ✓. The phenomenon is general: a
quadratic with rational coefficients and an irrational root $p + \sqrt{q}$ has the conjugate
$p - \sqrt{q}$ as its other root, which is why such roots always come in pairs.

**34.** *Method: discriminant.* For $x^2 - 2kx + k + 6 = 0$ we have $a = 1$, $b = -2k$, $c = k+6$, so

$$
\Delta = (-2k)^2 - 4(1)(k+6) = 4k^2 - 4k - 24 = 4\left(k^2 - k - 6\right) = 4(k-3)(k+2).
$$

Two distinct real roots require $\Delta > 0$, i.e. $(k-3)(k+2) > 0$. The product of two factors is
positive when they have the same sign, so

$$
k < -2 \quad \text{or} \quad k > 3 .
$$

*Checks:* at $k = 4$ the equation is $x^2 - 8x + 10 = 0$ with $\Delta = 64 - 40 = 24 > 0$ ✓; at $k = 0$
it is $x^2 + 6 = 0$ with $\Delta = -24 < 0$, so no real roots ✓; at the boundary $k = 3$ the equation
is $x^2 - 6x + 9 = (x-3)^2$, a double root ✓, and at $k = -2$ it is $x^2 + 4x + 4 = (x+2)^2$ ✓. Both
boundary values are excluded because the inequality is strict.

**35.** *Method: substitution.* The expression is quadratic in the block $x^2 - 2x$; put $u = x^2 - 2x$. Then

$$
u^2 - 11u + 24 = 0 \iff (u-3)(u-8) = 0 \iff u = 3 \text{ or } u = 8,
$$

since $(-3)(-8) = 24$ and $-3 - 8 = -11$.

*Case $u = 3$:* $x^2 - 2x - 3 = 0 \iff (x-3)(x+1) = 0 \iff x = 3$ or $x = -1$.

*Case $u = 8$:* $x^2 - 2x - 8 = 0 \iff (x-4)(x+2) = 0 \iff x = 4$ or $x = -2$.

The solution set is $\{-2,-1,3,4\}$.

*Checks in the original equation* (using $u = x^2-2x$): for $x = 3$, $u = 3$ and $9 - 33 + 24 = 0$ ✓;
$x = -1$, $u = 1 + 2 = 3$ and $9 - 33 + 24 = 0$ ✓; $x = 4$, $u = 16 - 8 = 8$ and $64 - 88 + 24 = 0$ ✓;
$x = -2$, $u = 4 + 4 = 8$ and again $0$ ✓.

**36.** *Proof.* Since $y = S - x$, the product is

$$
xy = x(S - x) = Sx - x^2 .
$$

Complete the square in $x$:

$$
Sx - x^2 = -\left(x^2 - Sx\right) = -\left[\left(x - \tfrac{S}{2}\right)^2 - \tfrac{S^2}{4}\right] = \frac{S^2}{4} - \left(x - \frac{S}{2}\right)^2 .
$$

*Check of the identity:* $\frac{S^2}{4} - \left(x^2 - Sx + \frac{S^2}{4}\right) = Sx - x^2$ ✓.

Because $\left(x - \frac{S}{2}\right)^2 \geq 0$ for every real $x$, it follows that

$$
xy = \frac{S^2}{4} - \left(x - \frac{S}{2}\right)^2 \leq \frac{S^2}{4},
$$

which is the required inequality. Equality holds exactly when the subtracted square is zero, that is
when $x = \frac{S}{2}$; then $y = S - \frac{S}{2} = \frac{S}{2} = x$. So equality holds **if and only
if $x = y$**. $\blacksquare$

*What this says about rectangles.* A rectangle with sides $x$ and $y$ has perimeter $P = 2(x+y)$, so
$x + y = \frac{P}{2} = S$ is fixed. Its area is $xy \leq \frac{S^2}{4} = \left(\frac{P}{4}\right)^2$,
with equality exactly when $x = y = \frac{P}{4}$. Hence **among all rectangles with a given perimeter,
the square has the largest area**, and the maximum area is $P^2/16$.

*Numerical illustration.* With $P = 40\ \mathrm{m}$ we have $S = 20$, so the area is at most
$\frac{400}{4} = 100\ \mathrm{m^2}$, attained by the square $10 \times 10$. A $6 \times 14$ rectangle has
the same perimeter and area $84\ \mathrm{m^2} < 100$ ✓.