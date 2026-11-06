# Polynomials — Solutions

> [Tutorial](README.md) · [Exercises](exercises.md)

Every exercise is solved in full, with the strategy, the algebra, and a verification. Expansions were
checked by re-expanding; where a factorisation is produced, the solution shows the expansion that
confirms it.

## Beginner

**1.** *Answer: $p(x) = x^5 - 2x^3 - 4x^2 + 7$; degree $5$, leading coefficient $1$, constant term $7$.*

Reordering the terms by decreasing exponent only uses commutativity of addition. In standard form the
leading term is $x^5$, so the degree is $5$; its coefficient is $1$ (written $x^5$, not $1x^5$, but the
coefficient is $1$). The constant term is the term without $x$, namely $7$. The coefficients are
$1, 0, -2, -4, 0, 7$ for $x^5, x^4, x^3, x^2, x^1, x^0$ respectively — note the two zeros for the
missing powers.

**2.** *Answer: $q(x) = 4x^4 - x + 8$; degree $4$, leading coefficient $4$, constant term $8$.*

Collect the quartic terms: $3x^4 - x^4 + 2x^4 = (3 - 1 + 2)x^4 = 4x^4$. So

$$
q(x) = 4x^4 - x + 8 .
$$

The degree is $4$ and the leading coefficient is $4$ — not $3$, which is the coefficient of the *first
written* term before collection. This is exactly the warning of §5: the degree is a property of the
collected expression. The constant term is $8$.

**3.** *Answer: $3x^2 + 5x - 5$.*

Add coefficients of equal powers:

$$
(5x^2 - 3x + 1) + (-2x^2 + 8x - 6) = (5 - 2)x^2 + (-3 + 8)x + (1 - 6) = 3x^2 + 5x - 5 .
$$

Sanity check at $x = 1$: left side $(5 - 3 + 1) + (-2 + 8 - 6) = 3 + 0 = 3$; right side $3 + 5 - 5 = 3$ ✓.

**4.** *Answer: $-2x^3 - 2x^2 - 4x + 7$.*

Distribute the minus sign over *both* terms of the second polynomial, including the constant:

$$
(x^3 - 4x + 2) - (3x^3 + 2x^2 - 5) = x^3 - 4x + 2 - 3x^3 - 2x^2 + 5 .
$$

Collecting: $(1 - 3)x^3 - 2x^2 - 4x + (2 + 5) = -2x^3 - 2x^2 - 4x + 7$. Check at $x = 1$:
$(1 - 4 + 2) - (3 + 2 - 5) = -1 - 0 = -1$; and $-2 - 2 - 4 + 7 = -1$ ✓.

**5.** *Answer: $x^2 + 3x - 40$.*

$$
(x - 5)(x + 8) = x^2 + 8x - 5x - 40 = x^2 + 3x - 40 .
$$

Check at $x = 0$: $(-5)(8) = -40$ = constant term ✓. At $x = 1$: $(-4)(9) = -36$ and $1 + 3 - 40 = -36$ ✓.

**6.** *Answer: $8x^2 - 10x - 3$.*

$$
(4x + 1)(2x - 3) = 8x^2 - 12x + 2x - 3 = 8x^2 - 10x - 3 .
$$

Check at $x = 1$: $(5)(-1) = -5$; $8 - 10 - 3 = -5$ ✓.

**7.** *Answer: $x^2 - 14x + 49$.*

Using $(a - b)^2 = a^2 - 2ab + b^2$ with $a = x$, $b = 7$:
$x^2 - 2 \cdot x \cdot 7 + 7^2 = x^2 - 14x + 49$. *Pitfall:* the answer $x^2 + 49$ omits the cross term
and is wrong (at $x = 1$: $(1-7)^2 = 36$, while $1 + 49 = 50$).

**8.** *Answer: $25x^2 + 20x + 4$.*

With $a = 5x$, $b = 2$: $(5x)^2 + 2(5x)(2) + 2^2 = 25x^2 + 20x + 4$. Check at $x = 1$:
$(5 + 2)^2 = 49$; $25 + 20 + 4 = 49$ ✓.

**9.** *Answer: $9x^2 - 16$.*

This is $(a - b)(a + b)$ with $a = 3x$, $b = 4$: $a^2 - b^2 = 9x^2 - 16$. Expanding directly:
$9x^2 + 12x - 12x - 16 = 9x^2 - 16$; the cross terms cancel, as the identity guarantees.

**10.** *Answer: $(4x - 5y)(4x + 5y)$.*

Both terms are squares: $16x^2 = (4x)^2$ and $25y^2 = (5y)^2$. By the difference of squares,

$$
16x^2 - 25y^2 = (4x)^2 - (5y)^2 = (4x - 5y)(4x + 5y).
$$

Verify: $16x^2 + 20xy - 20xy - 25y^2 = 16x^2 - 25y^2$ ✓.

**11.** *Answer: $p(x) \to -\infty$ as $x \to -\infty$, and $p(x) \to +\infty$ as $x \to +\infty$.*

The degree is $5$ (odd) and the leading coefficient is $3$ (positive). By the table of §7.2, odd degree
means the ends disagree and a positive leading coefficient means the right end rises. Concretely, for
large $|x|$ the term $3x^5$ dominates: when $x$ is large negative, $x^5$ is large negative, so $p(x)$ is
large negative; when $x$ is large positive, $p(x)$ is large positive.

**12.** *Answer: $p(-1) = -11$.*

$$
p(-1) = 2(-1)^3 - 5(-1)^2 + (-1) - 3 = -2 - 5 - 1 - 3 = -11 .
$$

*Pitfall:* $(-1)^2 = +1$ but $(-1)^3 = -1$; mixing them up gives $-2 + 5 - 1 - 3 = -1$, a wrong answer.

## Intermediate

**13.** *Answer: $2x^4 + 5x^3 - 4x^2 + 11x - 6$.*

Distribute each term of the first factor over the second:

$$
\begin{aligned}
(2x^2 - x + 3)(x^2 + 3x - 2)
&= 2x^2(x^2 + 3x - 2) - x(x^2 + 3x - 2) + 3(x^2 + 3x - 2)\\
&= 2x^4 + 6x^3 - 4x^2 - x^3 - 3x^2 + 2x + 3x^2 + 9x - 6\\
&= 2x^4 + 5x^3 - 4x^2 + 11x - 6 .
\end{aligned}
$$

Check the $x^2$ coefficient: $-4 - 3 + 3 = -4$ ✓. Check at $x = 1$: left
$(2 - 1 + 3)(1 + 3 - 2) = 4 \cdot 2 = 8$; right $2 + 5 - 4 + 11 - 6 = 8$ ✓.

**14.** *Answer: $x^3 - 9x^2 + 27x - 27$.*

With $a = x$, $b = 3$ in $(a - b)^3 = a^3 - 3a^2b + 3ab^2 - b^3$:

$$
x^3 - 3x^2(3) + 3x(3^2) - 3^3 = x^3 - 9x^2 + 27x - 27 .
$$

Check at $x = 1$: $(1 - 3)^3 = -8$; $1 - 9 + 27 - 27 = -8$ ✓.

**15.** *Answer: $8x^3 + 12x^2 + 6x + 1$.*

With $a = 2x$, $b = 1$ in $(a + b)^3 = a^3 + 3a^2b + 3ab^2 + b^3$:

$$
(2x)^3 + 3(2x)^2(1) + 3(2x)(1)^2 + 1 = 8x^3 + 12x^2 + 6x + 1 .
$$

Check at $x = 1$: $(2 + 1)^3 = 27$; $8 + 12 + 6 + 1 = 27$ ✓.

**16.** *Answer: $x^3 + 64 = (x + 4)(x^2 - 4x + 16)$ and $27x^3 - 8 = (3x - 2)(9x^2 + 6x + 4)$.*

For the first, $x^3 + 64 = x^3 + 4^3 = (x + 4)(x^2 - 4x + 16)$ by the sum of cubes. Verify:
$x^3 - 4x^2 + 16x + 4x^2 - 16x + 64 = x^3 + 64$ ✓.

For the second, $27x^3 - 8 = (3x)^3 - 2^3 = (3x - 2)(9x^2 + 6x + 4)$. Verify:
$27x^3 + 18x^2 + 12x - 18x^2 - 12x - 8 = 27x^3 - 8$ ✓.

*Note.* The quadratic factors are irreducible over $\mathbb{R}$: $x^2 - 4x + 16$ has discriminant
$16 - 64 < 0$, and $9x^2 + 6x + 4$ has discriminant $36 - 144 < 0$.

**17.** *Answer: quotient $4x^2 - 5x + 2$, remainder $0$.*

*Step 1.* $8x^3 \div 2x = 4x^2$, and $4x^2(2x + 1) = 8x^3 + 4x^2$. Subtracting,

$$
(8x^3 - 6x^2 - x + 2) - (8x^3 + 4x^2) = -10x^2 - x + 2 .
$$

*Step 2.* $-10x^2 \div 2x = -5x$, and $-5x(2x + 1) = -10x^2 - 5x$. Subtracting,

$$
(-10x^2 - x + 2) - (-10x^2 - 5x) = 4x + 2 .
$$

*Step 3.* $4x \div 2x = 2$, and $2(2x + 1) = 4x + 2$. Subtracting gives $0$.

Hence $8x^3 - 6x^2 - x + 2 = (2x + 1)(4x^2 - 5x + 2)$ with remainder $0$. Check by expanding:
$8x^3 - 10x^2 + 4x + 4x^2 - 5x + 2 = 8x^3 - 6x^2 - x + 2$ ✓.

**18.** *Answer: quotient $3x + 5$, remainder $-5x - 9$.*

*Step 1.* $3x^3 \div x^2 = 3x$, and $3x(x^2 - x + 2) = 3x^3 - 3x^2 + 6x$. Subtracting,

$$
(3x^3 + 2x^2 - 4x + 1) - (3x^3 - 3x^2 + 6x) = 5x^2 - 10x + 1 .
$$

*Step 2.* $5x^2 \div x^2 = 5$, and $5(x^2 - x + 2) = 5x^2 - 5x + 10$. Subtracting,

$$
(5x^2 - 10x + 1) - (5x^2 - 5x + 10) = -5x - 9 .
$$

The remainder has degree $1 < 2 = \deg(x^2 - x + 2)$, so the division stops:

$$
3x^3 + 2x^2 - 4x + 1 = (x^2 - x + 2)(3x + 5) + (-5x - 9).
$$

Check: $(x^2 - x + 2)(3x + 5) = 3x^3 + 5x^2 - 3x^2 - 5x + 6x + 10 = 3x^3 + 2x^2 + x + 10$, and adding
$-5x - 9$ gives $3x^3 + 2x^2 - 4x + 1$ ✓.

**19.** *Answer: $-11$.*

By the remainder theorem, the remainder of division by $x - 2$ is $p(2)$:

$$
p(2) = 2^4 - 3(2^3) + 2(2) - 7 = 16 - 24 + 4 - 7 = -11 .
$$

No long division is needed. (As a cross-check, the quotient is $x^3 - x^2 - 2x - 2$; expanding
$(x-2)(x^3 - x^2 - 2x - 2) - 11$ returns $x^4 - 3x^3 + 2x - 7$.)

**20.** *Answer: $x^3 - 2x^2 - 11x + 12 = (x - 4)(x + 3)(x - 1)$.*

Evaluate at $x = 4$:

$$
p(4) = 64 - 2(16) - 11(4) + 12 = 64 - 32 - 44 + 12 = 0 .
$$

By the factor theorem, $x - 4$ is a factor. Synthetic division with $c = 4$ on the coefficients
$1, -2, -11, 12$:

$$
\begin{array}{c|rrrr}
4 & 1 & -2 & -11 & 12\\
 & & 4 & 8 & -12\\
\hline
 & 1 & 2 & -3 & 0
\end{array}
$$

So $p(x) = (x - 4)(x^2 + 2x - 3)$. Factor the quadratic: $x^2 + 2x - 3 = (x + 3)(x - 1)$, since
$3 \cdot (-1) = -3$ and $3 + (-1) = 2$. Therefore $p(x) = (x - 4)(x + 3)(x - 1)$.

Check by expansion: $(x - 4)(x^2 + 2x - 3) = x^3 + 2x^2 - 3x - 4x^2 - 8x + 12 = x^3 - 2x^2 - 11x + 12$ ✓.
Vieta check: sum $4 - 3 + 1 = 2 = -b/a$ ✓; product $4 \cdot (-3) \cdot 1 = -12 = -d/a = -12$ ✓.

**21.** *Answer: sum $= \tfrac72$, product $= \tfrac32$; roots $\tfrac12$ and $3$.*

For $ax^2 + bx + c$ with $a = 2$, $b = -7$, $c = 3$, Vieta gives

$$
r_1 + r_2 = -\frac{b}{a} = \frac{7}{2}, \qquad r_1r_2 = \frac{c}{a} = \frac{3}{2}.
$$

Factor: $2x^2 - 7x + 3 = 2x^2 - 6x - x + 3 = 2x(x - 3) - (x - 3) = (2x - 1)(x - 3)$. So the roots are
$\tfrac12$ and $3$. Verify the formulas: $\tfrac12 + 3 = \tfrac72$ ✓ and $\tfrac12 \cdot 3 = \tfrac32$ ✓.

*Remark.* Vieta gives the sum and product without the quadratic formula, which is often all a problem
needs. Conversely, knowing the roots makes the factorisation immediate: $2\left(x - \tfrac12\right)(x - 3)$.

**22.** *Answer: $p(x) = x^3 - 6x^2 + 3x + 10$.*

A monic cubic with roots $-1, 2, 5$ is

$$
p(x) = (x + 1)(x - 2)(x - 5).
$$

Multiply in stages:

$$
(x + 1)(x - 2) = x^2 - x - 2, \qquad
(x^2 - x - 2)(x - 5) = x^3 - 5x^2 - x^2 + 5x - 2x + 10 = x^3 - 6x^2 + 3x + 10 .
$$

Vieta with $a = 1$, $b = -6$, $c = 3$, $d = 10$:

$$
r_1 + r_2 + r_3 = -1 + 2 + 5 = 6 = -\frac{b}{a} = 6 \ \checkmark,
$$

$$
r_1r_2 + r_1r_3 + r_2r_3 = (-1)(2) + (-1)(5) + (2)(5) = -2 - 5 + 10 = 3 = \frac{c}{a} \ \checkmark,
$$

$$
r_1r_2r_3 = (-1)(2)(5) = -10 = -\frac{d}{a} = -10 \ \checkmark .
$$

## Advanced

**23.** *Proof.*

Write $m = \deg p$, $n = \deg q$, and let $a = \operatorname{lc}(p) \neq 0$,
$b = \operatorname{lc}(q) \neq 0$. Every term of the product $pq$ has the form
$a_ix^i \cdot b_jx^j = a_ib_jx^{i+j}$ with $i \leq m$, $j \leq n$, so every exponent occurring in $pq$
is at most $m + n$; hence $\deg(pq) \leq m + n$.

For the reverse inequality, examine the coefficient of $x^{m+n}$. To obtain the exponent $m+n$ one must
pair an exponent $i$ from $p$ with an exponent $j$ from $q$ satisfying $i + j = m + n$. Since $i \leq m$
and $j \leq n$, the only possibility is $i = m$ and $j = n$. Hence the coefficient of $x^{m+n}$ in $pq$
is exactly $a_mb_n = ab$.

Now use the hypothesis on $\mathbb{R}$: it has no zero divisors, so $a \neq 0$ and $b \neq 0$ imply
$ab \neq 0$. Therefore $x^{m+n}$ really occurs, and $\deg(pq) \geq m + n$. Combining the two
inequalities, $\deg(pq) = m + n$. $\blacksquare$

*Where the hypothesis is used:* in the last step. Over a ring with zero divisors (for example the
integers modulo $6$), $a = 2$ and $b = 3$ are nonzero but $ab = 6 \equiv 0$, and the degree of a product
can drop.

**24.** *(a) Proof. (b) The four roots modulo $8$ exist because $\mathbb{Z}/8\mathbb{Z}$ has zero
divisors.*

*(a)* Induct on $n$. For $n = 0$, $p$ is a nonzero constant and has no roots.

Suppose the claim holds for degree $n - 1$ and let $\deg p = n$. If $p$ has no real root there is nothing
to prove. Otherwise let $c$ be a root. By the factor theorem, $p(x) = (x - c)q(x)$, and by Theorem 7.2
(degree of a product) $\deg q = n - 1$ because $\deg(x - c) = 1$. If $s \neq c$ is another root of $p$,
then $(s - c)q(s) = 0$. Since $s - c \neq 0$ and $\mathbb{R}$ has no zero divisors, $q(s) = 0$. By the
induction hypothesis $q$ has at most $n - 1$ distinct roots, so $p$ has at most $1 + (n-1) = n$ distinct
roots. $\blacksquare$

*(b)* Modulo $8$, the residues $1, 3, 5, 7$ are the odd classes, and each has square $1$:

$$
1^2 = 1, \quad 3^2 = 9 \equiv 1, \quad 5^2 = 25 \equiv 1, \quad 7^2 = 49 \equiv 1 \pmod 8 .
$$

So $x^2 - 1 \equiv 0 \pmod 8$ has the four roots $1, 3, 5, 7$, more than its degree $2$.

No contradiction arises because part (a) uses the absence of zero divisors, which fails modulo $8$: for
instance $2 \cdot 4 = 8 \equiv 0$ although neither factor is $0$. In the induction step, from
$(s - c)q(s) = 0$ we concluded $q(s) = 0$; modulo $8$ that inference is invalid, so the factor $x - c$
can be "used up" by a nonzero product equal to zero.

**25.** *Answer: $k = 3$, and $x^3 - 3x^2 + 2x - 6 = (x - 3)(x^2 + 2)$.*

By the factor theorem, $x - 3$ is a factor exactly when $p(3) = 0$:

$$
p(3) = 27 - 9k + 6 - 6 = 27 - 9k = 0 \;\Longrightarrow\; k = 3 .
$$

With $k = 3$, factor by grouping:

$$
x^3 - 3x^2 + 2x - 6 = x^2(x - 3) + 2(x - 3) = (x - 3)(x^2 + 2).
$$

Check by expansion: $x^3 - 3x^2 + 2x - 6$ ✓. Over $\mathbb{R}$, $x^2 + 2$ is irreducible (it is always
at least $2$), so this is the complete factorisation.

**26.** *Answer: $a = 2$.*

Division by $x + 1 = x - (-1)$ has remainder $p(-1)$:

$$
p(-1) = (-1)^3 + a(-1)^2 - 3(-1) + 5 = -1 + a + 3 + 5 = a + 7 .
$$

Setting $a + 7 = 9$ gives $a = 2$. Check with $a = 2$: $p(x) = x^3 + 2x^2 - 3x + 5$ and
$p(-1) = -1 + 2 + 3 + 5 = 9$ ✓.

**27.** *Answer: $x \in \left\{2,\ -\tfrac12,\ -3\right\}$.*

*Candidates.* The polynomial has integer coefficients with $a_0 = -6$ and $a_3 = 2$. By the rational
root theorem, a rational root $s/t$ in lowest terms satisfies $s \mid 6$ and $t \mid 2$, so the
candidates are

$$
\pm1,\ \pm2,\ \pm3,\ \pm6,\ \pm\tfrac12,\ \pm\tfrac32 .
$$

*Testing.* Compute $p(1) = 2 + 3 - 11 - 6 = -12$; $p(-1) = -2 + 3 + 11 - 6 = 6$; $p(2) = 16 + 12 - 22 - 6 = 0$.
So $x = 2$ is a root.

*Division.* Synthetic division by $c = 2$ on coefficients $2, 3, -11, -6$:

$$
\begin{array}{c|rrrr}
2 & 2 & 3 & -11 & -6\\
 & & 4 & 14 & 6\\
\hline
 & 2 & 7 & 3 & 0
\end{array}
$$

so $p(x) = (x - 2)(2x^2 + 7x + 3)$. Factor the quadratic:
$2x^2 + 7x + 3 = 2x^2 + 6x + x + 3 = 2x(x + 3) + (x + 3) = (2x + 1)(x + 3)$.

Hence $p(x) = (x - 2)(2x + 1)(x + 3)$ and the roots are $2, -\tfrac12, -3$.

*Verification by Vieta* with $a = 2$, $b = 3$, $c = -11$, $d = -6$:

$$
2 - \tfrac12 - 3 = -\tfrac32 = -\frac{b}{a} \ \checkmark,
$$

$$
2\left(-\tfrac12\right) + 2(-3) + \left(-\tfrac12\right)(-3) = -1 - 6 + \tfrac32 = -\tfrac{11}{2} = \frac{c}{a} \ \checkmark,
$$

$$
2 \cdot \left(-\tfrac12\right) \cdot (-3) = 3 = -\frac{d}{a} = \frac{6}{2} \ \checkmark .
$$

**28.** *(a) $x^4 - 16 = (x - 2)(x + 2)(x^2 + 4)$. (b) $x^4 + 2x^3 - x - 2 = (x + 2)(x - 1)(x^2 + x + 1)$.*

*(a)* Treat as a difference of squares:

$$
x^4 - 16 = (x^2)^2 - 4^2 = (x^2 - 4)(x^2 + 4) = (x - 2)(x + 2)(x^2 + 4).
$$

The factor $x^2 + 4$ is irreducible over $\mathbb{R}$ (discriminant $-16 < 0$). Check:
$(x^2 - 4)(x^2 + 4) = x^4 - 16$ ✓.

*(b)* Factor by grouping:

$$
x^4 + 2x^3 - x - 2 = x^3(x + 2) - (x + 2) = (x + 2)(x^3 - 1).
$$

Then $x^3 - 1 = (x - 1)(x^2 + x + 1)$, and $x^2 + x + 1$ has discriminant $1 - 4 < 0$, so it is
irreducible over $\mathbb{R}$. Therefore

$$
x^4 + 2x^3 - x - 2 = (x + 2)(x - 1)(x^2 + x + 1).
$$

Check: $(x - 1)(x^2 + x + 1) = x^3 - 1$, and $(x + 2)(x^3 - 1) = x^4 + 2x^3 - x - 2$ ✓.

**29.** *Answer: $x^6 - 1 = (x - 1)(x + 1)(x^2 + x + 1)(x^2 - x + 1)$.*

Factor as a difference of squares first, or as a difference of cubes times a sum of cubes:

$$
x^6 - 1 = (x^3)^2 - 1^2 = (x^3 - 1)(x^3 + 1).
$$

Then

$$
x^3 - 1 = (x - 1)(x^2 + x + 1), \qquad x^3 + 1 = (x + 1)(x^2 - x + 1).
$$

Both quadratics are irreducible over $\mathbb{R}$: $x^2 + x + 1$ has discriminant $1 - 4 = -3 < 0$ and
$x^2 - x + 1$ has discriminant $1 - 4 = -3 < 0$. Hence

$$
x^6 - 1 = (x - 1)(x + 1)(x^2 + x + 1)(x^2 - x + 1).
$$

Check by expanding the two quadratics first:
$(x^2 + x + 1)(x^2 - x + 1) = x^4 + x^2 + 1$ (the cross terms cancel). Then
$(x^2 - 1)(x^4 + x^2 + 1) = x^6 + x^4 + x^2 - x^4 - x^2 - 1 = x^6 - 1$ ✓.

*Remark.* Over $\mathbb{C}$ the polynomial splits completely into six linear factors, the roots being
the sixth roots of unity.

**30.** *(Answer: $p(x) = (x - 1)^2(x - 2)(x + 2)$; roots: $1$ double, $2$ simple, $-2$ simple; sign
$+$ on $(-\infty,-2)$, $-$ on $(-2,1)$, $-$ on $(1,2)$, $+$ on $(2,\infty)$.)*

*Finding the roots.* Test small integers. $p(1) = 1 - 2 - 3 + 8 - 4 = 0$ ✓. Divide by $x - 1$
(synthetic, $c = 1$, coefficients $1, -2, -3, 8, -4$):

$$
\begin{array}{c|rrrrr}
1 & 1 & -2 & -3 & 8 & -4\\
 & & 1 & -1 & -4 & 4\\
\hline
 & 1 & -1 & -4 & 4 & 0
\end{array}
$$

so $p(x) = (x - 1)(x^3 - x^2 - 4x + 4)$. Group the cubic:
$x^3 - x^2 - 4x + 4 = x^2(x - 1) - 4(x - 1) = (x - 1)(x^2 - 4) = (x - 1)(x - 2)(x + 2)$.

Therefore

$$
p(x) = (x - 1)^2(x - 2)(x + 2),
$$

with root $1$ of multiplicity $2$ and roots $2, -2$ of multiplicity $1$.

*Multiplicities.* At $x = 1$ the factor $(x-1)^2$ is even, so the graph touches the axis and turns back.
At $x = 2$ and $x = -2$ the multiplicity is odd, so the graph crosses.

*Sign chart.* Since $(x - 1)^2 \geq 0$, the sign of $p$ equals the sign of $(x - 2)(x + 2)$, except at
$x = 1$ where $p = 0$.

| Interval | Test point | Sign of $(x-2)(x+2)$ | Sign of $p$ |
|---|---|---|---|
| $(-\infty, -2)$ | $x = -3$ | $(-)(-) = +$ | $+$ |
| $(-2, 1)$ | $x = 0$ | $(-)(+) = -$ | $-$ |
| $(1, 2)$ | $x = 1.5$ | $(-)(+) = -$ | $-$ |
| $(2, \infty)$ | $x = 3$ | $(+)(+) = +$ | $+$ |

*Graph.* Degree $4$ with leading coefficient $1$: both ends rise. The $y$-intercept is $p(0) = -4$. The
graph comes down from $+\infty$, crosses at $x = -2$, stays below the axis through $x = 1$ where it
merely touches, stays below until it crosses at $x = 2$, then rises to $+\infty$.

## Challenge

**31.** *Proof, and the two deductions.*

Complex conjugation is defined by $\overline{u + vi} = u - vi$ for real $u, v$. It fixes every real
number and satisfies

$$
\overline{z + w} = \overline{z} + \overline{w}, \qquad \overline{zw} = \overline{z}\,\overline{w}
$$

for all $z, w \in \mathbb{C}$. (Verify by writing $z = u + vi$, $w = s + ti$ and expanding both sides;
the imaginary parts cancel in each case.)

Let $p(x) = a_nx^n + \cdots + a_0$ with $a_k \in \mathbb{R}$, so $\overline{a_k} = a_k$. Then

$$
\overline{p(z)} = \overline{a_nz^n + \cdots + a_0}
= \overline{a_n}\,\overline{z^n} + \cdots + \overline{a_0}
= a_n\overline{z}^n + \cdots + a_0 = p(\overline{z}),
$$

where the second step uses the two properties above repeatedly. If $p(z) = 0$, then

$$
0 = \overline{0} = \overline{p(z)} = p(\overline{z}),
$$

so $\overline{z}$ is also a root. $\blacksquare$

*Deduction 1: odd degree forces a real root.* Let $\deg p = n$ be odd. By the fundamental theorem of
algebra, $p$ has $n$ complex roots counted with multiplicity. By the result above, non-real roots occur
in conjugate pairs $(z, \overline{z})$ with $z \neq \overline{z}$, and each pair contributes an even
number (twice the multiplicity) of roots. Since $n$ is odd, the number of roots that are real must be
odd, in particular at least $1$.

*Deduction 2: the number of non-real roots is even.* The same pairing argument, counted with
multiplicity, gives this for every real polynomial.

**32.** *(a) Proof of the identity. (b) $x^4 + 4 = (x^2 + 2x + 2)(x^2 - 2x + 2)$ and
$x^4 + 64 = (x^2 + 4x + 8)(x^2 - 4x + 8)$.*

*(a)* Expand the right-hand side as a difference of squares:

$$
\left(a^2 + 2b^2 + 2ab\right)\left(a^2 + 2b^2 - 2ab\right) = \left(a^2 + 2b^2\right)^2 - (2ab)^2 .
$$

Now

$$
\left(a^2 + 2b^2\right)^2 = a^4 + 4a^2b^2 + 4b^4, \qquad (2ab)^2 = 4a^2b^2,
$$

so the difference is $a^4 + 4b^4$. $\blacksquare$

*(b)* For $x^4 + 4$, take $a = x$, $b = 1$:

$$
x^4 + 4 = (x^2 + 2x + 2)(x^2 - 2x + 2).
$$

Both quadratics have discriminant $4 - 8 = -4 < 0$, so they are irreducible over $\mathbb{R}$ and this
is the complete real factorisation. Check: $(x^2 + 2)^2 - (2x)^2 = x^4 + 4x^2 + 4 - 4x^2 = x^4 + 4$ ✓.

For $x^4 + 64$, write $64 = 4 \cdot 16 = 4 \cdot 2^4$, so take $a = x$, $b = 2$:

$$
x^4 + 64 = (x^2 + 4x + 8)(x^2 - 4x + 8).
$$

Both quadratics have discriminant $16 - 32 = -16 < 0$. Check:
$(x^2 + 8)^2 - (4x)^2 = x^4 + 16x^2 + 64 - 16x^2 = x^4 + 64$ ✓.

*Remark.* The identity shows that $a^4 + 4b^4$ is never irreducible over $\mathbb{R}$ for $b \neq 0$,
although it has no real root. This is why "no real root" does not imply "irreducible" once the degree
exceeds $2$.

**33.** *(a) Proof. (b) The remainder is $5x - 5$.*

*(a)* By the division algorithm, dividing $p$ by $(x - a)(x - b)$ gives

$$
p(x) = (x - a)(x - b)Q(x) + R(x),
$$

where $R = 0$ or $\deg R < 2$; in either case $R$ is a polynomial of degree at most $1$, so
$R(x) = cx + d$.

Evaluate at $x = a$: the product term vanishes because of the factor $(x - a)$, so $p(a) = R(a)$.
Similarly $p(b) = R(b)$. Hence $R$ is a polynomial of degree at most $1$ satisfying the two prescribed
conditions.

*Existence explicitly:* the polynomial

$$
L(x) = p(a) + \frac{p(b) - p(a)}{b - a}(x - a)
$$

is linear (or constant when $p(a) = p(b)$), and $L(a) = p(a)$ while
$L(b) = p(a) + (p(b) - p(a)) = p(b)$. The denominator is nonzero because $a \neq b$.

*Uniqueness:* if $L_1, L_2$ both have degree at most $1$ and agree at $a \neq b$, then $L_1 - L_2$ has
degree at most $1$ and two distinct roots, so by Corollary 7.8 it is the zero polynomial. $\blacksquare$

*(b)* Here $p(x) = x^3 - 2x + 1$, $a = 1$, $b = 2$:

$$
p(1) = 1 - 2 + 1 = 0, \qquad p(2) = 8 - 4 + 1 = 5 .
$$

So $L(1) = 0$, $L(2) = 5$, and the line through these points has slope
$\dfrac{5 - 0}{2 - 1} = 5$, giving

$$
L(x) = 5(x - 1) = 5x - 5 .
$$

*Verification by division.* Since $(x - 1)(x - 2) = x^2 - 3x + 2$:

*Step 1.* $x^3 \div x^2 = x$; $x(x^2 - 3x + 2) = x^3 - 3x^2 + 2x$; subtracting from $x^3 - 2x + 1$ gives
$3x^2 - 4x + 1$.

*Step 2.* $3x^2 \div x^2 = 3$; $3(x^2 - 3x + 2) = 3x^2 - 9x + 6$; subtracting gives $5x - 5$.

So $x^3 - 2x + 1 = (x^2 - 3x + 2)(x + 3) + (5x - 5)$, confirming the remainder $5x - 5$. Check:
$(x^2 - 3x + 2)(x + 3) = x^3 - 7x + 6$, and $x^3 - 7x + 6 + 5x - 5 = x^3 - 2x + 1$ ✓.

**34.** *(a) Proof. (b) $k = 1$.*

*(a)* Expand the square of the sum and collect:

$$
(a + b + c)^2 = a^2 + b^2 + c^2 + 2ab + 2ac + 2bc .
$$

Subtracting $2(ab + ac + bc)$ from both sides gives

$$
a^2 + b^2 + c^2 = (a + b + c)^2 - 2(ab + bc + ca).
$$

$\blacksquare$

*(b)* By Vieta's formulas for the cubic $x^3 - 3x^2 + kx - 1$ with leading coefficient $1$:

$$
a + b + c = 3, \qquad ab + bc + ca = k, \qquad abc = 1 .
$$

Substituting into the identity from part (a):

$$
7 = a^2 + b^2 + c^2 = (a + b + c)^2 - 2(ab + bc + ca) = 9 - 2k .
$$

Hence $2k = 2$ and $k = 1$.

*Remark.* The value $k = 1$ comes from Vieta alone; the roots themselves are not needed and are in fact
not expressible in a simple real form (the cubic $x^3 - 3x^2 + x - 1$ has one real and two non-real
roots, by §7.10).

**35.** *Proof.*

Suppose, for contradiction, that $p$ has an integer root $n$. By the factor theorem,
$p(x) = (x - n)q(x)$ for some polynomial $q$.

*Claim: $q$ has integer coefficients.* Since $x - n$ is monic with integer coefficients, polynomial
division of the integer-coefficient polynomial $p$ by $x - n$ produces an integer-coefficient quotient
and remainder: at each step of the division algorithm, the leading coefficient of the current remainder
is an integer and is divided by the leading coefficient $1$ of $x - n$ (see the recursion in the proof of
Theorem 7.5), so every coefficient produced is an integer. Alternatively, synthetic division with
$c = n$ uses only additions and multiplications of integers.

Now evaluate at $x = 0$ and at $x = 1$:

$$
p(0) = (0 - n)\,q(0) = -n\,q(0), \qquad p(1) = (1 - n)\,q(1).
$$

Since $p(0)$ is odd and $p(0) = -n\,q(0)$ is a product of integers, both $-n$ and $q(0)$ must be odd, so
$n$ is odd. Similarly, since $p(1)$ is odd, both $1 - n$ and $q(1)$ must be odd, so $1 - n$ is odd.

But $n$ and $1 - n$ are consecutive integers, so exactly one of them is even. Contradiction. Therefore
$p$ has no integer root. $\blacksquare$

*Example.* $p(x) = x^2 + x + 1$ has $p(0) = 1$ and $p(1) = 3$, both odd, and indeed it has no integer
root. By contrast $q(x) = x^2 - 1$ has $q(0) = -1$ (odd) but $q(1) = 0$ (even), and it does have integer
roots — the parity hypothesis excludes exactly this possibility.

