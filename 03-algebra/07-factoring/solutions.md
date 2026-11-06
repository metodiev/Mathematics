# Factoring — Solutions

> [Tutorial](README.md) · [Exercises](exercises.md) · 36 worked solutions

Each solution names the method, explains why it applies, carries out every significant step, and
checks the result by expanding. Where a factorisation is claimed to be complete, the irreducibility of
the remaining factors is justified by a discriminant argument.

## Beginner

**1.** *Method: greatest common factor.* The coefficients $15$ and $25$ have $\gcd 5$, and $x$ occurs in both
terms with smallest exponent $2$. Hence

$$
15x^3 - 25x^2 = 5x^2(3x - 5).
$$

*Check:* $5x^2 \cdot 3x = 15x^3$ and $5x^2 \cdot (-5) = -25x^2$. ✓ The cofactor $3x - 5$ is primitive,
so nothing more can be extracted.

**2.** *Method: greatest common factor.* $\gcd(6,9,3) = 3$; the variable $a$ occurs in all three terms with
smallest exponent $1$, and $b$ likewise. So the GCF is $3ab$, and dividing each term by it gives

$$
6a^2b - 9ab^2 + 3ab = 3ab(2a - 3b + 1).
$$

*Check:* $3ab \cdot 2a = 6a^2b$, $3ab \cdot (-3b) = -9ab^2$, $3ab \cdot 1 = 3ab$. ✓ The final "$+1$" is
essential: $3ab \cdot (2a - 3b)$ would omit the term $3ab$.

**3.** *Method: inspection.* We need integers $p, q$ with $p + q = 7$ and $pq = 12$. Since $12 > 0$ and
$7 > 0$, both are positive; the divisor pairs are $(1,12)$, $(2,6)$, $(3,4)$ with sums $13, 8, 7$. The
third works:

$$
x^2 + 7x + 12 = (x + 3)(x + 4).
$$

*Check:* $x^2 + 4x + 3x + 12 = x^2 + 7x + 12$. ✓

**4.** *Method: inspection.* Here $p + q = -9$ and $pq = 20$. Since $20 > 0$ and $-9 < 0$, both are negative;
the negative pairs of $20$ are $(-1,-20)$, $(-2,-10)$, $(-4,-5)$ with sums $-21, -12, -9$. The third
works:

$$
x^2 - 9x + 20 = (x - 4)(x - 5).
$$

*Check:* $x^2 - 5x - 4x + 20 = x^2 - 9x + 20$. ✓

**5.** *Method: inspection.* Here $pq = -12 < 0$, so the two constants have opposite signs, and $p + q = -1$
means the negative one has the larger magnitude. The pairs $( -4, 3)$ and $(4, -3)$ have sums $-1$ and
$1$; the first works:

$$
x^2 - x - 12 = (x - 4)(x + 3).
$$

*Check:* $x^2 + 3x - 4x - 12 = x^2 - x - 12$. ✓

**6.** *Method: difference of squares.* $x^2 - 49 = x^2 - 7^2$, so

$$
x^2 - 49 = (x - 7)(x + 7).
$$

*Check:* $x^2 + 7x - 7x - 49 = x^2 - 49$. ✓ Both factors are linear, so the factorisation is complete.

**7.** *Method: difference of squares.* Both terms are squares: $4x^2 = (2x)^2$ and $25 = 5^2$. Hence

$$
4x^2 - 25 = (2x - 5)(2x + 5).
$$

*Check:* $4x^2 + 10x - 10x - 25 = 4x^2 - 25$. ✓

**8.** *Method: perfect-square trinomial.* The first and last terms are squares, $\sqrt{x^2} = x$ and
$\sqrt{25} = 5$, and twice their product is $2 \cdot x \cdot 5 = 10x$, matching the middle term. With a
positive middle sign,

$$
x^2 + 10x + 25 = (x + 5)^2 .
$$

*Confirmation:* the discriminant is $10^2 - 4 \cdot 1 \cdot 25 = 100 - 100 = 0$, the perfect-square
condition. *Check:* $(x+5)^2 = x^2 + 10x + 25$. ✓

**9.** *Method: perfect-square trinomial.* $\sqrt{x^2} = x$, $\sqrt{36} = 6$, and $2 \cdot x \cdot 6 = 12x$
matches the middle term in magnitude; the sign is negative, so

$$
x^2 - 12x + 36 = (x - 6)^2 .
$$

*Confirmation:* discriminant $144 - 144 = 0$. *Check:* $(x-6)^2 = x^2 - 12x + 36$. ✓

**10.** *Method: difference of cubes.* $x^3 - 8 = x^3 - 2^3$, so with $a = x$, $b = 2$,

$$
x^3 - 8 = (x - 2)\left(x^2 + 2x + 4\right).
$$

*Check:* $x^3 + 2x^2 + 4x - 2x^2 - 4x - 8 = x^3 - 8$. ✓ The quadratic factor has discriminant
$4 - 16 = -12 < 0$, so it has no real root and is irreducible over $\mathbb{R}$: the factorisation is
complete.

**11.** *Method: sum of cubes.* $x^3 + 27 = x^3 + 3^3$, so

$$
x^3 + 27 = (x + 3)\left(x^2 - 3x + 9\right).
$$

*Check:* $x^3 - 3x^2 + 9x + 3x^2 - 9x + 27 = x^3 + 27$. ✓ The quadratic factor has discriminant
$9 - 36 = -27 < 0$, hence is irreducible over $\mathbb{R}$.

**12.** *Method: grouping (four terms).* Group as $(xy + 3x) + (2y + 6)$ and factor each pair:

$$
x(y + 3) + 2(y + 3) = (x + 2)(y + 3).
$$

The common binomial $y + 3$ appears because both groups produce it. *Check:*
$(x+2)(y+3) = xy + 3x + 2y + 6$. ✓

## Intermediate

**13.** *Method: $ac$ method.* Here $a = 2$, $b = 11$, $c = 12$, so $ac = 24$. We need $u + v = 11$ and
$uv = 24$; the pair $(3, 8)$ works. Split the middle term and group:

$$
2x^2 + 11x + 12 = 2x^2 + 3x + 8x + 12 = x(2x + 3) + 4(2x + 3) = (x + 4)(2x + 3).
$$

*Check:* $2x^2 + 3x + 8x + 12 = 2x^2 + 11x + 12$, and $(x+4)(2x+3) = 2x^2 + 3x + 8x + 12$. ✓ As a
further check, $b^2 - 4ac = 121 - 96 = 25 = 5^2$, a perfect square, so an integer factorisation had to
exist.

**14.** *Method: $ac$ method.* $a = 6$, $b = -7$, $c = -5$, so $ac = -30$. We need $u + v = -7$ and
$uv = -30$; the pair $(-10, 3)$ works since $-10 + 3 = -7$ and $(-10)(3) = -30$. Then

$$
6x^2 - 7x - 5 = 6x^2 - 10x + 3x - 5 = 2x(3x - 5) + (3x - 5) = (2x + 1)(3x - 5).
$$

*Check:* $6x^2 - 10x + 3x - 5 = 6x^2 - 7x - 5$, and $(2x+1)(3x-5) = 6x^2 - 10x + 3x - 5$. ✓ The
discriminant is $49 + 120 = 169 = 13^2$, a perfect square, as required.

**15.** *Method: difference of cubes.* Since $8x^3 = (2x)^3$ and $27y^3 = (3y)^3$, apply
$a^3 - b^3 = (a-b)(a^2 + ab + b^2)$ with $a = 2x$, $b = 3y$:

$$
8x^3 - 27y^3 = (2x - 3y)\left(4x^2 + 6xy + 9y^2\right).
$$

*Check:* $8x^3 + 12x^2y + 18xy^2 - 12x^2y - 18xy^2 - 27y^3 = 8x^3 - 27y^3$. ✓ The quadratic factor,
viewed as a quadratic in $x$, has discriminant $(6y)^2 - 4 \cdot 4 \cdot 9y^2 = -108y^2$, which is
negative for $y \neq 0$; so it is irreducible over $\mathbb{R}$ and the factorisation is complete.

**16.** *Method: GCF, then difference of squares.* Both terms share $3x^2$:

$$
3x^4 - 3x^2 = 3x^2\left(x^2 - 1\right) = 3x^2(x - 1)(x + 1).
$$

*Check:* $3x^2(x^2-1) = 3x^4 - 3x^2$. ✓ Every factor is now a monomial or linear, so this is complete.
Note that extracting only $3$ would give $3x^2(x^2-1)$ with the difference of squares still hidden.

**17.** *Method: repeated difference of squares.* The first application gives

$$
x^4 - 16 = \left(x^2\right)^2 - 4^2 = (x^2 - 4)(x^2 + 4),
$$

and $x^2 - 4$ is again a difference of squares:

$$
x^4 - 16 = (x - 2)(x + 2)\left(x^2 + 4\right).
$$

*Check:* $(x^2-4)(x^2+4) = x^4 - 4x^2 + 4x^2 - 16 = x^4 - 16$. ✓ The factor $x^2 + 4$ has discriminant
$-16 < 0$, so it is irreducible over $\mathbb{R}$ and the factorisation is complete.

**18.** *Method: substitution.* With $u = x^2$ the expression becomes $u^2 - 5u + 4$, and $p + q = -5$,
$pq = 4$ gives $p, q = -1, -4$. So

$$
x^4 - 5x^2 + 4 = (x^2 - 1)(x^2 - 4) = (x - 1)(x + 1)(x - 2)(x + 2).
$$

*Check:* $(x^2-1)(x^2-4) = x^4 - 4x^2 - x^2 + 4 = x^4 - 5x^2 + 4$. ✓ All four factors are linear, so
this is complete over $\mathbb{R}$.

**19.** *Method: GCF, then inspection.* Every term contains $2x$:

$$
2x^3 - 8x^2 - 42x = 2x\left(x^2 - 4x - 21\right).
$$

For $x^2 - 4x - 21$ we need $p + q = -4$ and $pq = -21$; the pair $(-7, 3)$ works, so

$$
2x^3 - 8x^2 - 42x = 2x(x - 7)(x + 3).
$$

*Check:* $(x-7)(x+3) = x^2 - 4x - 21$, and multiplying by $2x$ returns $2x^3 - 8x^2 - 42x$. ✓

**20.** *Method: GCF, then perfect square.* The GCF is $5$:

$$
5x^2 + 20x + 20 = 5\left(x^2 + 4x + 4\right) = 5(x + 2)^2 .
$$

*Check:* $5(x+2)^2 = 5(x^2 + 4x + 4) = 5x^2 + 20x + 20$. ✓ This is complete: a constant times an
irreducible factor. Had the $5$ been left inside, the perfect-square pattern would have been harder to
see, although the discriminant test $400 - 400 = 0$ would still have revealed it.

**21.** *Method: perfect-square trinomial.* The expression is a quadratic in the single quantity $xy$:

$$
x^2y^2 - 14xy + 49 = (xy)^2 - 2 \cdot xy \cdot 7 + 7^2 = (xy - 7)^2 .
$$

*Check:* $(xy-7)^2 = x^2y^2 - 14xy + 49$. ✓ The sign is negative because the middle term is negative.
Equivalently, the discriminant in the variable $xy$ is $196 - 196 = 0$.

**22.** *Method: GCF, then difference of squares.* The GCF is $3$, and $4x^2 - 9 = (2x)^2 - 3^2$:

$$
12x^2 - 27 = 3\left(4x^2 - 9\right) = 3(2x - 3)(2x + 3).
$$

*Check:* $3(4x^2 - 9) = 12x^2 - 27$. ✓

**23.** *Method: difference of squares, then sum and difference of cubes.* Treat $x^6$ as $(x^3)^2$:

$$
x^6 - 1 = \left(x^3 - 1\right)\left(x^3 + 1\right).
$$

Each cubic is a sum or difference of cubes:

$$
x^3 - 1 = (x-1)\left(x^2 + x + 1\right), \qquad x^3 + 1 = (x+1)\left(x^2 - x + 1\right).
$$

Therefore

$$
x^6 - 1 = (x-1)(x+1)\left(x^2 + x + 1\right)\left(x^2 - x + 1\right).
$$

*Check by an independent route:* $x^6 - 1 = (x^2)^3 - 1 = (x^2-1)(x^4 + x^2 + 1)$, and
$x^4 + x^2 + 1 = (x^2+x+1)(x^2-x+1)$ by the completing-the-square trick; since $x^2 - 1 = (x-1)(x+1)$,
the two results agree. ✓ Both quadratics have discriminant $1 - 4 = -3 < 0$, so they are irreducible
over $\mathbb{R}$ and the factorisation is complete.

**24.** *Method: perfect-square trinomial.* $\sqrt{9x^2} = 3x$, $\sqrt{16} = 4$, and $2 \cdot 3x \cdot 4 = 24x$
matches the middle term. Hence

$$
9x^2 + 24x + 16 = (3x + 4)^2 .
$$

*Confirmation:* discriminant $576 - 4 \cdot 9 \cdot 16 = 576 - 576 = 0$. *Check:*
$(3x+4)^2 = 9x^2 + 24x + 16$. ✓

## Advanced

**25.** *Method: grouping by pairs, then difference of squares.* Group the first two and last two terms:

$$
x^3 + 2x^2 - 9x - 18 = x^2(x + 2) - 9(x + 2) = \left(x^2 - 9\right)(x + 2).
$$

Now $x^2 - 9 = (x-3)(x+3)$ is a difference of squares, so

$$
x^3 + 2x^2 - 9x - 18 = (x - 3)(x + 3)(x + 2).
$$

*Check:* $(x^2-9)(x+2) = x^3 + 2x^2 - 9x - 18$. ✓ All factors are linear, so this is complete.

**26.** *Method: hidden difference of squares.* Both $x^4 = (x^2)^2$ and $64 = 8^2$ are squares, but the sign
is plus, so the plain difference-of-squares identity does not apply. Complete the square in $x^2$:

$$
\left(x^2 + 8\right)^2 = x^4 + 16x^2 + 64,
$$

hence $x^4 + 64 = \left(x^2+8\right)^2 - 16x^2 = \left(x^2+8\right)^2 - (4x)^2$. This is a difference
of squares with $a = x^2 + 8$ and $b = 4x$:

$$
x^4 + 64 = \left(x^2 + 8 - 4x\right)\left(x^2 + 8 + 4x\right) = (x^2 - 4x + 8)(x^2 + 4x + 8).
$$

*Check:*

$$
(x^2 - 4x + 8)(x^2 + 4x + 8) = x^4 + 4x^3 + 8x^2 - 4x^3 - 16x^2 - 32x + 8x^2 + 32x + 64 = x^4 + 64. \checkmark
$$

Both quadratics have discriminant $16 - 32 = -16 < 0$, so neither splits over $\mathbb{R}$: the
factorisation is complete.

**27.** *Method: substitution.* The expression is quadratic in $x + 2$. With $u = x + 2$,

$$
u^2 - 9u + 20 = (u - 4)(u - 5),
$$

since $-4 + (-5) = -9$ and $(-4)(-5) = 20$. Substituting back,

$$
(x + 2)^2 - 9(x + 2) + 20 = (x + 2 - 4)(x + 2 - 5) = (x - 2)(x - 3).
$$

*Check directly:* $(x+2)^2 - 9(x+2) + 20 = x^2 + 4x + 4 - 9x - 18 + 20 = x^2 - 5x + 6 = (x-2)(x-3)$. ✓

**28.** *Method: $ac$ method with two variables.* Treat the expression as a quadratic in $x$, with "$c$" equal
to $-6y^2$. Then $ac = 6 \cdot (-6y^2) = -36y^2$ and $b = -5y$; we need $u + v = -5y$ and
$uv = -36y^2$. The pair $(-9y, 4y)$ works: $-9y + 4y = -5y$ and $(-9y)(4y) = -36y^2$. Splitting and
grouping,

$$
6x^2 - 5xy - 6y^2 = 6x^2 - 9xy + 4xy - 6y^2 = 3x(2x - 3y) + 2y(2x - 3y) = (3x + 2y)(2x - 3y).
$$

*Check:* $(3x+2y)(2x-3y) = 6x^2 - 9xy + 4xy - 6y^2 = 6x^2 - 5xy - 6y^2$. ✓ Both factors are linear in
$x$ and $y$, so this is complete.

**29.** *Proof.* Suppose $ax^2 + bx + c = (px + q)(rx + s)$ with integers $p, q, r, s$. Expanding the right
side,

$$
(px+q)(rx+s) = pr\,x^2 + (ps + qr)x + qs,
$$

and comparing coefficients with $ax^2 + bx + c$ gives

$$
pr = a, \qquad ps + qr = b, \qquad qs = c .
$$

Define $u := ps$ and $v := qr$. These are integers, and

$$
u + v = ps + qr = b, \qquad uv = ps \cdot qr = (pr)(qs) = a \cdot c = ac ,
$$

which is exactly what was required. $\blacksquare$

*Application to $4x^2 + 6x + 5$.* Here $a = 4$, $b = 6$, $c = 5$, so $ac = 20$. By the result just
proved, an integer factorisation would produce integers $u, v$ with $u + v = 6$ and $uv = 20$. Since
$uv > 0$ and $u + v > 0$, both are positive, so $\{u,v\}$ must be one of the divisor pairs
$\{1, 20\}$, $\{2, 10\}$, $\{4, 5\}$, whose sums are $21$, $12$, $9$. None equals $6$. Hence no such
integers exist and $4x^2 + 6x + 5$ has no factorisation with integer coefficients.

*Remark.* The polynomial is in fact irreducible over $\mathbb{R}$ as well: its discriminant is
$36 - 80 = -80 < 0$. So there is not even a real factorisation, and the negative discriminant is the
quickest way to see that no search is worthwhile.

**30.** *Method: GCF, then repeated difference of squares.* First extract $2x$:

$$
2x^5 - 32x = 2x\left(x^4 - 16\right).
$$

Now $x^4 - 16 = (x^2-4)(x^2+4)$ by a difference of squares, and $x^2 - 4 = (x-2)(x+2)$. Hence

$$
2x^5 - 32x = 2x(x - 2)(x + 2)\left(x^2 + 4\right).
$$

*Check:* $(x^2-4)(x^2+4) = x^4 - 16$, and multiplying by $2x$ returns $2x^5 - 32x$. ✓ The factor
$x^2 + 4$ is irreducible over $\mathbb{R}$ (discriminant $-16$), so the factorisation is complete.

**31.** *Method: substitution.* With $u = x^2$ the expression is $u^2 - 7u + 12$, and $p + q = -7$, $pq = 12$
gives $p, q = -3, -4$. Hence

$$
x^4 - 7x^2 + 12 = (x^2 - 3)(x^2 - 4).
$$

Over $\mathbb{R}$ both factors split, because $3$ is a square of a real number:

$$
x^4 - 7x^2 + 12 = (x - \sqrt3)(x + \sqrt3)(x - 2)(x + 2).
$$

*Check:* $(x^2-3)(x^2-4) = x^4 - 4x^2 - 3x^2 + 12 = x^4 - 7x^2 + 12$. ✓ All four factors are linear, so
this is the complete real factorisation. Note that $x^2 - 3$ is irreducible over $\mathbb{Q}$ and over
$\mathbb{Z}$; only over $\mathbb{R}$ does it split. This is a concrete illustration of the coefficient
set mattering.

**32.** *Method: factor theorem, then inspection.* First verify the given root:
$p(1) = 1 - 6 + 11 - 6 = 0$. ✓ By the factor theorem $x - 1$ is a factor. Write

$$
x^3 - 6x^2 + 11x - 6 = (x - 1)\left(x^2 + \beta x + \gamma\right).
$$

Comparing constant terms: $-\gamma = -6$, so $\gamma = 6$. Comparing $x^2$ coefficients: $\beta - 1 = -6$,
so $\beta = -5$. Therefore

$$
p(x) = (x-1)\left(x^2 - 5x + 6\right) = (x-1)(x-2)(x-3),
$$

since $x^2 - 5x + 6$ has $p + q = -5$, $pq = 6$, giving $p, q = -2, -3$.

*Check:* $(x-1)(x-2) = x^2 - 3x + 2$ and $(x^2-3x+2)(x-3) = x^3 - 3x^2 - 3x^2 + 9x + 2x - 6 = x^3 - 6x^2 + 11x - 6$. ✓ The roots are $1$, $2$, $3$, each of multiplicity one.

## Challenge

**33.** *No linear factor.* For every real $x$, $x^4 \geq 0$, so $x^4 + 1 \geq 1 > 0$. Hence $x^4 + 1$ has no real
root, and therefore no factor of the form $x - a$ with $a \in \mathbb{Q} \subseteq \mathbb{R}$.

*No quadratic-times-quadratic factorisation over $\mathbb{Q}$.* Suppose, for contradiction, that

$$
x^4 + 1 = \left(x^2 + ax + b\right)\left(x^2 + cx + d\right)
$$

with $a, b, c, d \in \mathbb{Q}$. (Any factorisation into two quadratics over $\mathbb{Q}$ can be
normalised so that both factors are monic, since the polynomial is monic.) Expanding and comparing
coefficients:

$$
a + c = 0, \qquad b + d + ac = 0, \qquad ad + bc = 0, \qquad bd = 1 .
$$

The first equation gives $c = -a$. Substituting into the third, $ad - ab = a(d - b) = 0$.

*Case $a = 0$.* Then $c = 0$, so $b + d = 0$, i.e. $d = -b$. With $bd = 1$ this gives $-b^2 = 1$, which
has no rational solution.

*Case $a \neq 0$.* Then $d = b$, so $bd = b^2 = 1$ and $b = \pm 1$. The second equation gives
$2b = a^2$, so $a^2 = \pm 2$. If $a^2 = -2$ there is no rational solution; if $a^2 = 2$ then
$a = \pm\sqrt2 \notin \mathbb{Q}$, contradicting $a \in \mathbb{Q}$.

Both cases are impossible, so $x^4 + 1$ is irreducible over $\mathbb{Q}$ (and, by Gauss's lemma,
over $\mathbb{Z}$ as well).

*Factorisation over $\mathbb{R}$.* Complete the square in $x^2$:

$$
x^4 + 1 = \left(x^2 + 1\right)^2 - 2x^2 = \left(x^2 + 1 - \sqrt2\,x\right)\left(x^2 + 1 + \sqrt2\,x\right).
$$

*Check:* $\left(x^2+1\right)^2 - 2x^2 = x^4 + 2x^2 + 1 - 2x^2 = x^4 + 1$. ✓ Each quadratic has
discriminant $2 - 4 = -2 < 0$, so neither splits over $\mathbb{R}$ and this is the complete real
factorisation. The irrational coefficient $\sqrt2$ is exactly what prevents the factorisation from
being valid over $\mathbb{Q}$.

**34.** *Method: repeated difference of squares, then sum of cubes.* Start with $x^8 - 1 = (x^4)^2 - 1^2$:

$$
x^8 - 1 = \left(x^4 - 1\right)\left(x^4 + 1\right).
$$

Now $x^4 - 1 = (x^2-1)(x^2+1)$ and $x^2 - 1 = (x-1)(x+1)$. For $x^4 + 1$ use the completing-the-square
trick from Solution 33:

$$
x^4 + 1 = \left(x^2 - \sqrt2\,x + 1\right)\left(x^2 + \sqrt2\,x + 1\right).
$$

Combining,

$$
x^8 - 1 = (x-1)(x+1)\left(x^2 + 1\right)\left(x^2 - \sqrt2\,x + 1\right)\left(x^2 + \sqrt2\,x + 1\right).
$$

*Checks.* The discriminants of the three quadratics are $-4$, $-2$, $-2$, all negative, so none splits
over $\mathbb{R}$; every factor is therefore irreducible over $\mathbb{R}$ and the factorisation is
complete. Expanding the rational part first,
$(x^2-1)(x^2+1)(x^4+1) = (x^4-1)(x^4+1) = x^8 - 1$. ✓

*Real roots.* Only the linear factors contribute, so the real roots are $x = 1$ and $x = -1$, both
simple. In particular $x^8 - 1$ has exactly two real roots although it has degree $8$; the other six
roots are complex.

**35.** *Reduction to a divisor problem.* If $x^2 + kx + 12 = (x + p)(x + q)$ with $p, q \in \mathbb{Z}$, then
expanding and comparing coefficients gives

$$
p + q = k, \qquad pq = 12 .
$$

So the question is exactly: which sums arise from integer pairs with product $12$? Since $12 > 0$, $p$
and $q$ have the same sign, and the divisors of $12$ are $\pm 1, \pm 2, \pm 3, \pm 4, \pm 6, \pm 12$.
The unordered pairs with product $12$ are

| Pair $\{p,q\}$ | Sum $p+q$ |
|---|---|
| $\{1, 12\}$ | $13$ |
| $\{2, 6\}$ | $8$ |
| $\{3, 4\}$ | $7$ |
| $\{-1, -12\}$ | $-13$ |
| $\{-2, -6\}$ | $-8$ |
| $\{-3, -4\}$ | $-7$ |

Therefore $k \in \{13, 8, 7, -7, -8, -13\}$, and the list is complete because every integer pair with
product $12$ appears in the table. For example, with $k = 13$,
$x^2 + 13x + 12 = (x+1)(x+12)$, and with $k = -7$, $x^2 - 7x + 12 = (x-3)(x-4)$.

*Remark.* Seven other integers $k$ give a polynomial with no integer factorisation; for instance $k = 0$
gives $x^2 + 12$, which has negative discriminant $-48$ and so is irreducible over $\mathbb{R}$.

**36.** *The factorisation.* Complete the square in $n^2$:

$$
n^4 + 4 = \left(n^2 + 2\right)^2 - 4n^2 = \left(n^2 + 2 - 2n\right)\left(n^2 + 2 + 2n\right),
$$

that is,

$$
n^4 + 4 = \left(n^2 - 2n + 2\right)\left(n^2 + 2n + 2\right).
$$

*Check of the identity:* expanding gives
$n^4 + 2n^3 + 2n^2 - 2n^3 - 4n^2 - 4n + 2n^2 + 4n + 4 = n^4 + 4$. ✓ (The identity holds for every
integer $n$, not only $n \geq 2$.)

*Both factors exceed $1$ when $n \geq 2$.* Write $n^2 - 2n + 2 = (n-1)^2 + 1$, which is at least $2$ for
$n \geq 2$, and $n^2 + 2n + 2 \geq 4 + 4 + 2 = 10 > 1$. Both factors are integers strictly between $1$
and $n^4 + 4$: for $n \geq 2$, $n^4 + 4 - \left(n^2 + 2n + 2\right) = n^4 - n^2 - 2n + 2 > 0$. Hence
$n^4 + 4$ has a non-trivial factorisation into two integers greater than $1$, so it is composite.
$\blacksquare$

*Why $n = 1$ is exceptional.* At $n = 1$ the first factor is $1 - 2 + 2 = 1$, a unit, and the second is
$1 + 2 + 2 = 5$. The factorisation degenerates to $5 = 1 \cdot 5$, which is a trivial factorisation and
says nothing about primality. Indeed $1^4 + 4 = 5$ is prime. The argument requires both factors to be
greater than $1$, which is exactly what fails at $n = 1$. (For completeness: at $n = 0$ the value is
$4$, also composite.)