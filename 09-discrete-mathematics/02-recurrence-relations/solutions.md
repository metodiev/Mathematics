# Recurrence Relations — Solutions

> [Recurrence Relations](README.md) · Solutions to the 36 problems in [exercises.md](exercises.md)

Each solution names the method, carries out every algebraic step, and — as the tutorial insists — checks the closed form against the recurrence at small values of $n$ before or after the derivation. Bounds obtained from the master theorem are accompanied by the case that produced them.

## Beginner

**1.** *Strategy: iterate until the pattern is visible, then verify by induction.*

Iterating,

$$a_n = a_{n-1} + 3 = a_{n-2} + 6 = a_{n-3}+9 = \cdots = a_0 + 3n.$$

**Closed form.** $a_n = 3n + 2$.

*Values.* $a_0 = 2$, $a_1 = 5$, $a_2 = 8$, $a_3 = 11$, $a_4 = 14$ ✓.

*Induction.* Base $n = 0$: $3\cdot 0 + 2 = 2$ ✓. Step: if $a_k = 3k+2$ then
$a_{k+1} = (3k+2)+3 = 3(k+1)+2$ ✓. $\square$

**2.** *Strategy: a first-order homogeneous recurrence is a geometric progression.*

$a_1 = 5$, $a_2 = 10$, $a_3 = 20$, $a_4 = 40$, and in general $a_n = 5\cdot 2^{n-1}$.

*Check.* $a_1 = 5\cdot 2^0 = 5$ ✓; $a_2 = 5\cdot 2 = 10$ ✓; $a_3 = 5\cdot 4 = 20$ ✓.

*Why one initial condition is enough.* The recurrence has order $1$: to compute $a_{n+1}$ you need only $a_n$. Theorem 5.6 with $k = 1$ says that one prescribed value determines the whole sequence, and the iteration $a_n = 2^{n-1}a_1$ exhibits it. $\square$

**3.** *Strategy: multiply the initial value by $3$ once per step, starting from $a_0$.*

Iterating, $a_n = 3^na_0 = 2\cdot 3^n$.

*Values.* $2, 6, 18, 54, 162$; the recurrence gives $3\cdot 2 = 6$, $3\cdot 6 = 18$, and so on ✓.

*Why not $3^{n+1}$?* That would give $a_0 = 3$, contradicting $a_0 = 2$. The exponent counts the number of multiplications applied, which is $n$ when the starting index is $0$. Writing $3^{n+1}$ would describe the sequence with $a_0 = 3$. $\square$

**4.** *Strategy: the recurrence is additive, so the solution is $a_1$ plus a sum of consecutive integers.*

$$a_n = a_1 + \sum_{j=2}^{n} j = 1 + \bigl(2 + 3 + \cdots + n\bigr) = 1 + \left(\frac{n(n+1)}{2} - 1\right) = \frac{n(n+1)}{2}.$$

*Values.* $a_1 = 1$; $a_2 = 1+2 = 3$ and $\frac{2\cdot3}{2} = 3$ ✓; $a_3 = 3+3 = 6$ and $\frac{3\cdot4}{2} = 6$ ✓; $a_4 = 6+4 = 10$ and $\frac{4\cdot5}{2} = 10$ ✓.

*Remark.* The same answer is often written $a_n = 1 + 2 + \cdots + n$, since $a_1 = 1$ already equals the first term. $\square$

**5.** *Strategy: additive recurrence with a geometric summand.*

$$a_n = a_0 + \sum_{j=1}^{n}2^j = 0 + (2 + 4 + \cdots + 2^n) = 2\,\frac{2^n-1}{2-1} = 2^{n+1}-2.$$

*Values.* $a_0 = 0$; $a_1 = 2$ and $2^2-2 = 2$ ✓; $a_2 = 2+4 = 6$ and $2^3-2 = 6$ ✓; $a_3 = 6+8 = 14$ and $2^4-2 = 14$ ✓.

*Induction.* Base $n=0$: $2^1-2 = 0$ ✓. Step: $a_{k+1} = (2^{k+1}-2) + 2^{k+1} = 2^{k+2}-2$ ✓. $\square$

**6.** *Strategy: characteristic equation. The simplicity of the answer reflects the choice of initial conditions, not a general rule.*

*Characteristic equation.* $r^2-5r+6 = (r-2)(r-3) = 0$, roots $2$ and $3$.

*General solution.* $a_n = A2^n + B3^n$.

*Initial conditions.* $A+B = 1$ and $2A+3B = 2$. Subtracting twice the first from the second gives $B = 0$, hence $A = 1$.

**Closed form.** $a_n = 2^n$.

*Check.* $a_2 = 5\cdot 2 - 6\cdot 1 = 4 = 2^2$ ✓; $a_3 = 5\cdot 4 - 6\cdot 2 = 8 = 2^3$ ✓.

*Why it is simple.* The initial values satisfy $a_1 = 2a_0$, so the sequence lies in the one-dimensional subspace of solutions proportional to $2^n$. Choosing $a_1 = 3$ instead would give $A = 0$, $B = 1$ and the answer $3^n$. In general the coefficient of a root vanishes exactly when the initial data match that root's mode. $\square$

**7.** *Strategy: same characteristic equation as Fibonacci, different initial conditions.*

*Values.* $L_0 = 2$, $L_1 = 1$, $L_2 = 3$, $L_3 = 4$, $L_4 = 7$, $L_5 = 11$.

*Characteristic equation.* $r^2 - r - 1 = 0$, roots $\varphi$ and $\psi$.

*General solution.* $L_n = A\varphi^n + B\psi^n$. The initial conditions give $A + B = 2$ and $A\varphi + B\psi = 1$. From $B = 2-A$:

$$A\varphi + (2-A)\psi = 1 \;\Longrightarrow\; A(\varphi-\psi) = 1 - 2\psi \;\Longrightarrow\; A = \frac{1-2\psi}{\sqrt5}.$$

Using $1 - 2\psi = 1 - (1-\sqrt5) = \sqrt5$, we get $A = 1$, and then $B = 1$.

**Closed form.** $L_n = \varphi^n + \psi^n$.

*Check.* $n=0$: $1+1 = 2$ ✓. $n=1$: $\varphi+\psi = 1$ ✓. $n=2$: $\varphi^2+\psi^2 = (\varphi+\psi)^2 - 2\varphi\psi = 1 + 2 = 3$ ✓. $n=3$: $\varphi^3+\psi^3 = (\varphi+\psi)^3 - 3\varphi\psi(\varphi+\psi) = 1 + 3 = 4$ ✓. $n=4, 5$ follow from the recurrence: $3+4 = 7$ ✓, $4+7 = 11$ ✓.

*Remark.* $L_n = F_{n-1}+F_{n+1}$ for $n \ge 1$; check $n=4$: $F_3+F_5 = 2+5 = 7$ ✓. $\square$

**8.** *Strategy: discriminant zero, so the repeated-root form $(A+Bn)r^n$ applies.*

*Characteristic equation.* $r^2-4r+4 = (r-2)^2 = 0$: root $r = 2$, multiplicity $2$.

*General solution.* $a_n = (A+Bn)2^n$.

*Initial conditions.* $a_0 = A = 1$; $a_1 = (1+B)\cdot 2 = 4$ gives $B = 1$.

**Closed form.** $a_n = (1+n)2^n$.

*Check.* $a_2 = 4\cdot 4 - 4\cdot 1 = 12$ and $(1+2)\cdot4 = 12$ ✓. $a_3 = 4\cdot 12 - 4\cdot 4 = 32$ and $4\cdot 8 = 32$ ✓. $a_4 = 4\cdot32 - 4\cdot12 = 80$ and $5\cdot16 = 80$ ✓. $\square$

**9.** *Strategy: telescoping after the partial-fraction identity $\frac{1}{j(j+1)} = \frac1j-\frac1{j+1}$.*

$$a_n = a_0 + \sum_{j=1}^{n}\left(\frac1j - \frac1{j+1}\right) = 0 + \left(1 - \frac{1}{n+1}\right) = \frac{n}{n+1}.$$

*Check.* $a_1 = 1/2$ ✓; $a_2 = 1/2 + 1/6 = 2/3$ ✓; $a_3 = 2/3 + 1/12 = 3/4$ ✓. $\square$

**10.** *Strategy: multiplicative recurrence, so the solution is a product.*

$$a_n = a_0\prod_{j=1}^{n} j = 1\cdot n! = n!.$$

*Values.* $1, 1, 2, 6, 24, 120$ ✓.

*Why "linear".* An equation is linear in the unknown sequence when it is a linear combination of the unknown terms (with coefficients that may depend on $n$) plus a term independent of the unknown. Here $a_n - n\,a_{n-1} = 0$ is exactly of that form with coefficient $c_1(n) = n$. The coefficient varies with $n$, which is why the characteristic-equation method does not apply, but it is still a coefficient, not an unknown. By contrast $a_n = a_{n-1}^2$ is non-linear because the unknown is squared. $\square$

**11.** *Strategy: check each of the four adjectives separately: order (how far back), linearity (no products or powers of unknowns), homogeneity (no added function of $n$), constancy of coefficients.*

| Recurrence | Order | Linear | Homogeneous | Constant coefficients |
|---|---|---|---|---|
| (a) $a_n = 7a_{n-1}-12a_{n-2}$ | 2 | yes | yes | yes |
| (b) $a_n = a_{n-1}+n^2$ | 1 | yes | no ($f(n) = n^2$) | yes |
| (c) $a_n = n^2a_{n-1}$ | 1 | yes ($c_1(n) = n^2$) | yes | no |
| (d) $a_n = a_{n-1}+a_{n-2}+a_{n-3}$ | 3 | yes | yes | yes |
| (e) $a_n = a_{n-1}^2$ | 1 | no | yes (no forcing term) | yes (coefficient $1$) |
| (f) $T(n) = 3T(n/2)+n$ | not defined | yes | no ($f(n) = n$) | yes |

*Remarks.* (e) is homogeneous but non-linear: homogeneity is about the absence of an added term, not about linearity. (f) is a divide-and-conquer recurrence; "order" counts how many earlier values appear, which is meaningless when the index is divided, so it is handled by the master theorem instead. $\square$

**12.** *Strategy: compute the recurrence forward, compute the formula forward, and compare.*

*From the recurrence.* $a_0 = 1$, $a_1 = 1$, then
$a_2 = a_1 + 2a_0 = 1+2 = 3$, $a_3 = a_2+2a_1 = 3+2 = 5$, $a_4 = a_3+2a_2 = 5+6 = 11$, $a_5 = a_4+2a_3 = 11+10 = 21$.

*From the formula.* With $a_n = \frac{2^{n+1}+(-1)^n}{3}$:

| $n$ | $2^{n+1}$ | $(-1)^n$ | numerator | $a_n$ |
|---|---|---|---|---|
| 0 | 2 | 1 | 3 | 1 |
| 1 | 4 | $-1$ | 3 | 1 |
| 2 | 8 | 1 | 9 | 3 |
| 3 | 16 | $-1$ | 15 | 5 |
| 4 | 32 | 1 | 33 | 11 |
| 5 | 64 | $-1$ | 63 | 21 |

The two lists agree: $1, 1, 3, 5, 11, 21$. ✓

*Remark.* Agreement of six values is evidence, not proof; the proof is in Exercise 26, where the same formula is *derived* by generating functions, and in the induction of Section 9.5 of [Mathematical Induction](../01-mathematical-induction/README.md), which uses the same recurrence. $\square$

## Intermediate

**13.** *Strategy: unroll the recurrence, noting that the argument halves at each step until it reaches $1$.*

For $n = 2^k$, unrolling $k$ times gives

$$T(2^k) = 2T(2^{k-1}) + 2^k = 2^2T(2^{k-2}) + 2\cdot 2^{k-1} + 2^k = \cdots = 2^kT(1) + k\cdot 2^k .$$

The middle terms are $k$ copies of $2^k$: at step $j$ the cost is $2^j \cdot (n/2^j) = n$. Hence, with $T(1) = 1$ and $k = \log_2 n$,

$$T(n) = 2^k + k\,2^k = n + n\log_2 n = n\log_2 n + n.$$

*Check by direct computation.*

* $T(2) = 2T(1)+2 = 4$; formula $2\cdot 1 + 2 = 4$ ✓.
* $T(4) = 2T(2)+4 = 8+4 = 12$; formula $4\cdot 2+4 = 12$ ✓.
* $T(8) = 2T(4)+8 = 24+8 = 32$; formula $8\cdot 3+8 = 32$ ✓.

*Induction.* Base $n=1$: $1\cdot 0+1 = 1$ ✓. Step for $n$ even: if $T(m) = m\log_2 m + m$ for all $m < n$, then
$T(n) = 2\bigl(\frac n2\log_2\frac n2 + \frac n2\bigr) + n = n(\log_2 n - 1) + n + n = n\log_2 n + n$ ✓. $\square$

**14.** *Strategy: particular solution of the same polynomial shape as the forcing term, then add $A2^n$ and fit $a_0$.*

*Homogeneous part.* $a_n = 2a_{n-1}$ has solution $A2^n$.

*Particular solution.* Try $a_n = \alpha n + \beta$. Substituting,

$$\alpha n + \beta = 2\bigl(\alpha(n-1)+\beta\bigr) + n = 2\alpha n - 2\alpha + 2\beta + n.$$

Comparing coefficients of $n$: $\alpha = 2\alpha + 1$, so $\alpha = -1$. Comparing constants: $\beta = -2\alpha + 2\beta$, so $\beta = 2\alpha = -2$.

*General solution.* $a_n = A2^n - n - 2$.

*Initial condition.* $a_0 = A - 2 = 0$ gives $A = 2$.

**Closed form.** $a_n = 2^{n+1} - n - 2$.

*Check.* $a_0 = 2-0-2 = 0$ ✓; $a_1 = 4-3 = 1$ and the recurrence gives $2\cdot 0+1 = 1$ ✓; $a_2 = 8-4 = 4$ and the recurrence gives $2\cdot1+2 = 4$ ✓; $a_3 = 16-5 = 11$ and the recurrence gives $2\cdot4+3 = 11$ ✓. $\square$

**15.** *Strategy: resonance. Since $3$ is a root of the homogeneous recurrence, the trial $C3^n$ is annihilated; use $Cn3^n$.*

*Homogeneous part.* $a_n = 3a_{n-1}$ has solution $A3^n$.

*Particular solution.* Try $a_n = Cn3^n$. Then

$$Cn3^n = 3C(n-1)3^{n-1} + 2\cdot 3^n .$$

Divide by $3^{n-1}$:

$$3Cn = 3C(n-1) + 6 = 3Cn - 3C + 6,$$

so $3C = 6$ and $C = 2$. The particular solution is $2n3^n$.

*General solution.* $a_n = A3^n + 2n3^n$.

*Initial condition.* $a_0 = A = 1$.

**Closed form.** $a_n = (1+2n)3^n$.

*Check.* $a_1 = 3\cdot 1 + 2\cdot3 = 9$ and $(1+2)\cdot 3 = 9$ ✓; $a_2 = 3\cdot 9 + 2\cdot 9 = 45$ and $5\cdot 9 = 45$ ✓; $a_3 = 3\cdot45+2\cdot27 = 189$ and $7\cdot27 = 189$ ✓. $\square$

**16.** *Strategy: resonance with base $2$. Show the failure of $C2^n$ explicitly, then use $Cn2^n$.*

*Why $C2^n$ fails.* Substituting $a_n = C2^n$ into $a_n = 2a_{n-1}+2^n$ gives $C2^n = C2^n + 2^n$, i.e. $0 = 2^n$, which is impossible. The trial is a homogeneous solution, so it is mapped to $0$ by the operator and cannot equal the forcing term.

*Particular solution.* Try $a_n = Cn2^n$:

$$Cn2^n = 2C(n-1)2^{n-1} + 2^n .$$

Divide by $2^{n-1}$: $2Cn = 2C(n-1) + 2 = 2Cn - 2C + 2$, so $C = 1$. The particular solution is $n2^n$.

*General solution.* $a_n = A2^n + n2^n$.

*Initial condition.* $a_1 = 2A + 2 = 3$ gives $A = 1/2$.

**Closed form.** $a_n = 2^n\bigl(n+\tfrac12\bigr) = 2^{n-1}(2n+1)$.

*Check.* $a_1 = 1\cdot 3 = 3$ ✓; $a_2 = 2\cdot 3+4 = 10$ and $2\cdot 5 = 10$ ✓; $a_3 = 2\cdot 10 + 8 = 28$ and $4\cdot 7 = 28$ ✓. $\square$

**17.** *Strategy: iteration, or the master theorem with $a=1$, $b=2$, $f(n)=\Theta(n^0)$.*

For $n = 2^k$,

$$T(2^k) = T(2^{k-1}) + 1 = T(2^{k-2})+2 = \cdots = T(1) + k = k.$$

Since $k = \log_2 n$ and $T(1) = 0$, **$T(n) = \log_2 n$**.

*Check.* $T(2) = T(1)+1 = 1$ ✓; $T(4) = 2$ ✓; $T(8) = 3$ ✓; $T(16) = 4$ ✓.

*Master theorem.* $a = 1$, $b = 2$, $c = \log_2 1 = 0$, and $f(n) = 1 = \Theta(n^0)$: Case 2 gives $\Theta(n^0\log n) = \Theta(\log n)$ ✓. $\square$

**18.** *Strategy: read off $a$, $b$, $f$, compute $c = \log_ba$, and compare $f$ with $n^c$.*

Here $a = 4$, $b = 2$, so $c = \log_2 4 = 2$. The forcing term is $f(n) = n$, and $n = O(n^{2-\varepsilon})$ with $\varepsilon = 1 > 0$. This is **Case 1**, so

$$T(n) = \Theta(n^{2}).$$

*Check by unrolling.* Level $j$ costs $4^j\cdot\frac{n}{2^j} = 2^jn$; the levels $j = 0, \ldots, \log_2 n - 1$ sum to $n(2^{\log_2 n}-1) = n(n-1)$, and the $4^{\log_2 n} = n^2$ leaves each cost $T(1) = 1$. Hence $T(n) = n(n-1)+n^2 = 2n^2-n$, which is indeed $\Theta(n^2)$.

*Values.* $T(2) = 4+2 = 6$ and $2\cdot4-2 = 6$ ✓; $T(4) = 4\cdot6+4 = 28$ and $2\cdot16-4 = 28$ ✓. $\square$

**19.** *Strategy: Case 3, after checking the regularity condition.*

Here $a = 2$, $b = 2$, $c = \log_2 2 = 1$, and $f(n) = n^2 = \Omega(n^{1+\varepsilon})$ with $\varepsilon = 1$. *Regularity:*

$$a\,f\!\left(\frac nb\right) = 2\left(\frac n2\right)^2 = \frac{n^2}{2} = \frac12 f(n),$$

so the condition holds with $\delta = 1/2 < 1$. **Case 3** gives

$$T(n) = \Theta(n^2).$$

*Recursion-tree check.* Level $j$ costs $2^j(n/2^j)^2 = n^2/2^j$; summing over $j \ge 0$ gives at most $2n^2$, and the root alone costs $n^2$, so the total is between $n^2$ and $2n^2$ plus the leaves: $\Theta(n^2)$ ✓.

*Values.* With $T(1)=1$: $T(2) = 2+4 = 6$; $T(4) = 12+16 = 28$. Both match $2n^2-n$ from the exact unrolling. $\square$

**20.** *Strategy: compare $f(n) = n^2$ with $n^{\log_2 7}$.*

Here $a = 7$, $b = 2$, so $c = \log_2 7 \approx 2.8073549$. Since $n^2 = O(n^{2.807-0.807})$, **Case 1** applies and

$$T(n) = \Theta(n^{\log_2 7}) \approx \Theta(n^{2.807}).$$

*Comparison.* The naive algorithm satisfies $T(n) = 8T(n/2)+\Theta(n^2)$, whose exponent is $\log_2 8 = 3$; Strassen saves one recursive multiplication and lowers the exponent from $3$ to about $2.807$. The saving is real but sub-quadratic in the exponent, which is why Strassen's method only wins for large matrices.

*Sanity check by levels.* Level $j$ costs $7^j(n/2^j)^2 = n^2(7/4)^j$, which grows geometrically; the deepest level costs $7^{\log_2 n} = n^{\log_2 7}$, and it dominates the geometric sum ✓. $\square$

**21.** *Strategy: particular solution $Cn3^n$ because $3$ is a simple characteristic root, then fit the two initial conditions.*

*Homogeneous part.* $r^2-5r+6 = (r-2)(r-3)$, so $A2^n + B3^n$.

*Particular solution.* Try $Cn3^n$:

$$Cn3^n = 5C(n-1)3^{n-1} - 6C(n-2)3^{n-2} + 3^n .$$

Divide by $3^{n-2}$:

$$9Cn = 15C(n-1) - 6C(n-2) + 9 = 15Cn - 15C - 6Cn + 12C + 9 = 9Cn - 3C + 9,$$

so $3C = 9$ and $C = 3$. The particular solution is $3n3^n = n\,3^{n+1}$.

*General solution.* $a_n = A2^n + B3^n + n3^{n+1}$.

*Initial conditions.* $A + B = 1$; and $2A + 3B + 9 = 6$, i.e. $2A + 3B = -3$. Substituting $A = 1-B$: $2 - 2B + 3B = -3$, so $B = -5$ and $A = 6$.

**Closed form.** $a_n = 6\cdot2^n - 5\cdot3^n + n\,3^{n+1}$.

*Check.* $a_0 = 6-5+0 = 1$ ✓. $a_1 = 12-15+9 = 6$ ✓. $a_2 = 24-45+54 = 33$, and the recurrence gives $5\cdot6 - 6\cdot1 + 9 = 33$ ✓. $a_3 = 48-135+243 = 156$, and the recurrence gives $5\cdot33-6\cdot6+27 = 165-36+27 = 156$ ✓. $\square$

**22.** *Strategy: multiply by $x^n$, sum over $n$, and express everything in terms of $G$.*

Let $G(x) = \sum_{n\ge0}a_nx^n$. For $n \ge 1$ the recurrence gives $a_n - 2a_{n-1} = 1$; multiplying by $x^n$ and summing over $n \ge 1$,

$$(G - a_0) - 2xG = \frac{x}{1-x}.$$

With $a_0 = 1$: $G(1-2x) = 1 + \frac{x}{1-x} = \frac{1}{1-x}$, so

$$G(x) = \frac{1}{(1-x)(1-2x)}.$$

*Partial fractions.* $\frac{1}{(1-x)(1-2x)} = \frac{A}{1-x} + \frac{B}{1-2x}$ with $A(1-2x) + B(1-x) = 1$. Comparing: $A + B = 1$ and $-2A - B = 0$, so $B = -2A$ and $-A = 1$, i.e. $A = -1$, $B = 2$.

*Read off coefficients.*

$$G(x) = \frac{2}{1-2x} - \frac{1}{1-x} = \sum_{n\ge0}\bigl(2\cdot2^n - 1\bigr)x^n,$$

so $a_n = 2^{n+1}-1$.

*Check.* $a_0 = 1$ ✓; $a_1 = 3$ and $2\cdot 1+1 = 3$ ✓; $a_2 = 7$ and $2\cdot3+1 = 7$ ✓; $a_3 = 15$ ✓. $\square$

## Advanced

**23.** *Strategy: repeated characteristic root $1$, so the general solution is $(A+Bn)\cdot1^n = A+Bn$.*

*Characteristic equation.* $r^2-2r+1 = (r-1)^2 = 0$: root $1$, multiplicity $2$.

*General solution.* $a_n = A + Bn$.

*Initial conditions.* $a_0 = A = 1$; $a_1 = 1+B = 3$ gives $B = 2$.

**Closed form.** $a_n = 2n+1$.

*Check.* $a_2 = 2\cdot 3 - 1 = 5$ and $2\cdot2+1 = 5$ ✓; $a_3 = 2\cdot5-3 = 7$ and $7$ ✓; $a_4 = 2\cdot7-5 = 9$ ✓.

*Why linear?* A double root means the exponential $1^n$ is a "critical" solution: the operator $L$ annihilates both $1$ and $n$. (Indeed $n - 2(n-1) + (n-2) = 0$.) With a single root there would be one free constant, but two initial conditions need two; the second solution $n$ supplies the missing degree of freedom, and it is linear in $n$ because the multiplicity is $2$. $\square$

**24.** *Strategy: complex characteristic roots, written in polar form.*

The characteristic equation is $r^2-2r+2 = 0$, so

$$r = \frac{2 \pm \sqrt{4-8}}{2} = 1 \pm i = \sqrt2\,e^{\pm i\pi/4}.$$

Thus $\rho = \sqrt2$ and $\theta = \pi/4$, and the general real solution is

$$a_n = (\sqrt2)^n\left(C\cos\frac{n\pi}{4} + D\sin\frac{n\pi}{4}\right).$$

*Initial conditions.* $a_0 = C = 0$. Then $a_1 = \sqrt2\cdot D\sin\frac{\pi}{4} = \sqrt2\cdot D\cdot\frac{1}{\sqrt2} = D = 2$.

**Closed form.** $a_n = 2(\sqrt2)^n\sin\dfrac{n\pi}{4}$.

*Check.* $a_0 = 0$ ✓; $a_1 = 2\cdot\sqrt2\cdot\frac{1}{\sqrt2} = 2$ ✓; $a_2 = 2\cdot2\cdot1 = 4$, and the recurrence gives $2\cdot2-2\cdot0 = 4$ ✓; $a_3 = 2\cdot2\sqrt2\cdot\frac{1}{\sqrt2} = 4$, and the recurrence gives $2\cdot4-2\cdot2 = 4$ ✓; $a_4 = 2\cdot4\cdot0 = 0$, and the recurrence gives $2\cdot4-2\cdot4 = 0$ ✓.

*Interpretation.* The sequence oscillates with period $8$ in $n$ (since $\theta = \pi/4$) while its amplitude grows like $(\sqrt2)^n$. $\square$

**25.** *Strategy: repeated root $3$, with $a_1 = 0$ forcing the coefficients to cancel at $n = 1$.*

*Characteristic equation.* $r^2-6r+9 = (r-3)^2 = 0$: root $3$, multiplicity $2$.

*General solution.* $a_n = (A+Bn)3^n$.

*Initial conditions.* $a_0 = A = 1$; $a_1 = (1+B)\cdot3 = 0$ gives $B = -1$.

**Closed form.** $a_n = (1-n)3^n$.

*Check.* $a_2 = 6\cdot0 - 9\cdot1 = -9$ and $(1-2)\cdot9 = -9$ ✓; $a_3 = 6(-9) - 9\cdot0 = -54$ and $(1-3)\cdot27 = -54$ ✓; $a_4 = 6(-54) - 9(-9) = -324+81 = -243$ and $(1-4)\cdot81 = -243$ ✓. $\square$

**26.** *Strategy: one generating function, one algebraic equation, one partial-fraction decomposition.*

Let $G(x) = \sum_{n\ge0}a_nx^n$. Multiplying $a_n = a_{n-1}+2a_{n-2}$ by $x^n$ and summing over $n \ge 2$:

$$\sum_{n\ge2}a_nx^n = x\sum_{n\ge2}a_{n-1}x^{n-1} + 2x^2\sum_{n\ge2}a_{n-2}x^{n-2},$$

that is $G - a_0 - a_1x = x(G-a_0) + 2x^2G$. With $a_0 = a_1 = 1$:

$$G(1 - x - 2x^2) = 1 - x + x = 1, \qquad G(x) = \frac{1}{(1-2x)(1+x)},$$

using $1 - x - 2x^2 = (1-2x)(1+x)$.

*Partial fractions.* Write $\frac{1}{(1-2x)(1+x)} = \frac{A}{1-2x} + \frac{B}{1+x}$; then $A(1+x) + B(1-2x) = 1$, giving $A+B = 1$ and $A - 2B = 0$. Hence $A = 2B$, $3B = 1$, $B = 1/3$ and $A = 2/3$.

*Read off coefficients.*

$$G(x) = \frac{2/3}{1-2x} + \frac{1/3}{1+x} = \sum_{n\ge0}\left(\frac23\,2^n + \frac13(-1)^n\right)x^n,$$

so $a_n = \dfrac{2^{n+1}+(-1)^n}{3}$.

*Check.* $1, 1, 3, 5, 11, 21$ for $n = 0,\ldots,5$ ✓, matching the recurrence computed in Exercise 12. $\square$

**27.** *Strategy: the convolution becomes a product; the resulting quadratic is solved and the correct branch chosen by the value at $x = 0$.*

*Set up.* With $C(x) = \sum_{n\ge0}C_nx^n$, the recurrence $C_n = \sum_{k=0}^{n-1}C_kC_{n-1-k}$ says that for $n \ge 1$ the coefficient of $x^{n-1}$ in $C(x)^2$ is $C_n$. Hence

$$C(x) - C_0 = x\,C(x)^2, \qquad\text{i.e.}\qquad C(x) = 1 + xC(x)^2 .$$

*Solve the quadratic.* $xC^2 - C + 1 = 0$ gives

$$C(x) = \frac{1 \pm \sqrt{1-4x}}{2x}.$$

As $x \to 0$, the branch with the plus sign behaves like $2/(2x) = 1/x$, which is not a power series; the branch with the minus sign behaves like $\frac{1-(1-2x)}{2x} = 1$. So

$$C(x) = \frac{1-\sqrt{1-4x}}{2x}.$$

*Expand.* By the binomial theorem, $\sqrt{1-4x} = \sum_{n\ge0}\binom{1/2}{n}(-4x)^n$, so for $n \ge 0$,

$$C_n = -\frac12\binom{1/2}{n+1}(-4)^{n+1}.$$

Using $\binom{1/2}{n+1} = \dfrac{(-1)^n}{2^{2n+1}(n+1)}\dbinom{2n}{n}$ (check: $n=0$ gives $\frac12$ ✓, $n=1$ gives $-\frac18$ ✓),

$$C_n = -\frac12\cdot\frac{(-1)^n}{2^{2n+1}(n+1)}\binom{2n}{n}\cdot(-1)^{n+1}2^{2n+2} = \frac{1}{n+1}\binom{2n}{n}.$$

*Verify.* $C_0 = 1$, $C_1 = \frac12\binom21 = 1$, $C_2 = \frac13\binom42 = 2$, $C_3 = \frac14\binom63 = 5$, $C_4 = \frac15\binom84 = 14$ ✓. These are the counts of triangulations of a triangle, quadrilateral, pentagon, hexagon and heptagon. $\square$

**28.** *Strategy: sum the level costs of the recursion tree exactly, then identify the resulting sum as $\Theta(n\log^2n)$.*

For $n = 2^L$, level $j$ (with $0 \le j \le L$) has $2^j$ nodes, each of size $n/2^j$, and each costs $\frac{n}{2^j}\log_2\frac{n}{2^j}$. So

$$W_j = 2^j\cdot\frac{n}{2^j}\log_2\frac{n}{2^j} = n\,(L - j).$$

Summing,

$$T(n) = \sum_{j=0}^{L} n(L-j) = n\sum_{i=0}^{L} i = n\cdot\frac{L(L+1)}{2} = \Theta\bigl(nL^2\bigr) = \Theta\bigl(n\log^2 n\bigr).$$

*Which case?* Here $c = \log_2 2 = 1$ and $f(n) = n\log n = \Theta(n^{1}\log^{1}n)$, so this is the **extended second case** with $k = 1$, which predicts $\Theta(n^{\log_ba}\log^{k+1}n) = \Theta(n\log^2n)$ ✓.

*Check at small values.* With $T(1) = 1$: $T(2) = 2\cdot1 + 2\cdot1 = 4$ and $T(4) = 2\cdot4+4\cdot2 = 16$. The exact level sum is $n\frac{L(L+1)}{2}$ plus the leaf term $T(1)\,n$: at $n = 4$ (so $L = 2$) this is $4\cdot\frac{2\cdot3}{2}+4 = 12+4 = 16$ ✓, and at $n = 2$ (so $L = 1$) it is $2\cdot\frac{1\cdot2}{2}+2 = 4$ ✓. $\square$

**29.** *Strategy: resonance with base $2$ for a recurrence whose homogeneous roots are $1$ and $2$.*

*Homogeneous part.* $r^2-3r+2 = (r-1)(r-2)$, so $A + B2^n$.

*Particular solution.* Since $2$ is a simple root, try $Cn2^n$:

$$Cn2^n = 3C(n-1)2^{n-1} - 2C(n-2)2^{n-2} + 2^n .$$

Divide by $2^{n-2}$:

$$4Cn = 6C(n-1) - 2C(n-2) + 4 = 6Cn - 6C - 2Cn + 4C + 4 = 4Cn - 2C + 4,$$

so $C = 2$ and the particular solution is $2n2^n$.

*General solution.* $a_n = A + B2^n + 2n2^n$.

*Initial conditions.* $A + B = 0$; $A + 2B + 4 = 1$, i.e. $A+2B = -3$. Subtracting gives $B = -3$, so $A = 3$.

**Closed form.** $a_n = 3 - 3\cdot2^n + 2n\,2^n$.

*Check.* $a_2 = 3\cdot1 - 2\cdot0 + 4 = 7$ and $3-12+16 = 7$ ✓; $a_3 = 3\cdot7 - 2\cdot1 + 8 = 27$ and $3-24+48 = 27$ ✓. $\square$

**30.** *Strategy: prove existence and uniqueness in the same induction; the key point is that at each index the value is forced by earlier ones.*

**Claim.** Let $k \ge 1$, let $c_1,\ldots,c_k$ and $f$ be fixed, and let $u_0,\ldots,u_{k-1}$ be prescribed. Then there is exactly one sequence $(a_n)_{n\ge0}$ with

$$a_n = c_1a_{n-1}+\cdots+c_ka_{n-k}+f(n) \ \ (n \ge k), \qquad a_i = u_i \ \ (0 \le i \le k-1).$$

*Proof.* **Uniqueness.** Suppose $(a_n)$ and $(b_n)$ both satisfy the conditions. We show $a_n = b_n$ by strong induction on $n$. For $n < k$ this is the hypothesis $a_n = u_n = b_n$. For $n \ge k$, assume $a_m = b_m$ for all $m < n$; then

$$a_n = \sum_{i=1}^{k}c_ia_{n-i} + f(n) = \sum_{i=1}^{k}c_ib_{n-i} + f(n) = b_n,$$

because the recurrence expresses $a_n$ (and $b_n$) entirely in terms of earlier values. So $a_n = b_n$ for every $n$.

**Existence.** Define $a_n$ recursively: for $n < k$ set $a_n = u_n$, and for $n \ge k$ set $a_n$ equal to the right-hand side, which involves only $a_0,\ldots,a_{n-1}$ and is therefore already defined. This is a legitimate definition by recursion on $n$ (the recursion theorem, Theorem 7.8.1 of [Mathematical Induction](../01-mathematical-induction/README.md)), and by construction the resulting sequence satisfies both the initial conditions and the recurrence.

Existence and uniqueness together give exactly one sequence. $\square$

*Remark.* The proof also shows *why* $k$ initial conditions are needed: at $n = k$ the recurrence refers to $a_0, \ldots, a_{k-1}$, so all of them must be given; with fewer, the value $a_k$ is not determined, which is precisely the failure of existence with a prescribed prefix.

## Challenge

**31.** *Strategy: characteristic roots $2 \pm \sqrt3$, then a separate parity induction using the recurrence rather than the binomial expansion.*

*Solve.* $r^2-4r+1 = 0$ gives $r = 2 \pm \sqrt3$, so the general solution is $a_n = A(2+\sqrt3)^n + B(2-\sqrt3)^n$. The initial conditions give

$$A + B = 2, \qquad A(2+\sqrt3) + B(2-\sqrt3) = 4.$$

The second equation is $2(A+B) + \sqrt3(A-B) = 4$, so $4 + \sqrt3(A-B) = 4$ and $A = B$; with $A+B = 2$ we get $A = B = 1$. Hence

$$a_n = (2+\sqrt3)^n + (2-\sqrt3)^n .$$

*Values.* $a_0 = 2$, $a_1 = 4$, $a_2 = 4\cdot4-2 = 14$, $a_3 = 4\cdot14-4 = 52$, $a_4 = 4\cdot52-14 = 194$ ✓.

*Parity.* The sequence satisfies $a_0 = 2$ and $a_1 = 4$, both even, and $a_n = 4a_{n-1}-a_{n-2}$. If $a_{n-1}$ and $a_{n-2}$ are even then $4a_{n-1}$ is even and $a_n$ is a difference of even numbers, hence even. By strong induction $a_n$ is even for every $n \ge 0$. $\square$

*Remark.* The parity is obvious from the recurrence but not from the closed form, since the two irrational summands are not integers individually. This is a good illustration of the general principle that a recurrence often reveals arithmetic structure that a closed form hides.

**32.** *Strategy: bound each level of the recursion tree by a geometric series and use $b^{\varepsilon k} = n^{\varepsilon}$; the leaves give the matching lower bound.*

**Claim (Case 1).** Let $a \ge 1$, $b > 1$, $c = \log_ba$, and suppose $T(n) = aT(n/b)+f(n)$ with $f(n) \le C n^{c-\varepsilon}$ for some $\varepsilon > 0$ and all $n = b^k$. Then $T(n) = \Theta(n^{c})$.

*Upper bound.* Level $j$ costs

$$W_j = a^j f\!\left(\frac{n}{b^j}\right) \le a^j\cdot C\left(\frac{n}{b^j}\right)^{c-\varepsilon} = C\,n^{c-\varepsilon}\cdot \frac{a^j}{b^{j(c-\varepsilon)}} = C\,n^{c-\varepsilon}\,b^{j\varepsilon},$$

where the last equality uses $a = b^{c}$, so that $a^j/b^{jc} = 1$ and $b^{j\varepsilon}$ remains. Summing the geometric series over $j = 0,\ldots,k$ with ratio $b^{\varepsilon} > 1$,

$$T(n) \le C\,n^{c-\varepsilon}\cdot\frac{b^{\varepsilon(k+1)}-1}{b^{\varepsilon}-1} = O\bigl(n^{c-\varepsilon}\cdot b^{\varepsilon k}\bigr) = O\bigl(n^{c-\varepsilon}\cdot n^{\varepsilon}\bigr) = O(n^{c}),$$

because $b^{\varepsilon k} = (b^{k})^{\varepsilon} = n^{\varepsilon}$.

*Lower bound.* The recursion tree has $a^{k}$ leaves, and $a^{k} = (b^{c})^{k} = (b^{k})^{c} = n^{c}$. Each leaf costs $T(1) = \Theta(1)$, so $T(n) \ge a^{k}\cdot T(1) = \Theta(n^{c})$.

The two bounds agree, so $T(n) = \Theta(n^{c})$. $\square$

**33.** *Strategy: substitute $n = 2^m$ to turn the radical recurrence into a standard halving recurrence.*

Let $n = 2^m$ with $m = 2^k$ (so that the repeated square roots stay integral) and define $S(m) = T(2^m)$. Since $\sqrt n = 2^{m/2}$,

$$S(m) = T(2^m) = 2T(2^{m/2}) + \log_2(2^m) = 2S(m/2) + m .$$

This is the recurrence of Exercise 13 with $m$ in place of $n$ and $f(m) = m$: by the master theorem, $a = 2$, $b = 2$, $c = \log_2 2 = 1$, $f(m) = \Theta(m^{1})$ is Case 2, so

$$S(m) = \Theta(m\log m).$$

Substituting back $m = \log_2 n$,

$$T(n) = \Theta\bigl(\log n\cdot\log\log n\bigr).$$

*Domain.* The substitution is valid for $n = 2^{2^k}$, since then $\sqrt n = 2^{2^{k-1}}$ is again of the same form. The $\Theta$ statement extends to all $n$ by monotonicity of $T$: for $2^{2^{k}} \le n \le 2^{2^{k+1}}$, the value $T(n)$ is sandwiched between $T(2^{2^k})$ and $T(2^{2^{k+1}})$, and the two sandwiching expressions differ by a constant factor in the $\Theta$ sense. $\square$

**34.** *Strategy: write both sides in terms of $\varphi$ and $\psi$, and use $|\psi| < 1$ for the rounding formula.*

Let $L_n = \varphi^n+\psi^n$. Then, using $(\varphi^n-\psi^n)(\varphi^n+\psi^n) = \varphi^{2n}-\psi^{2n}$ and $\sqrt5\cdot\sqrt5 = 5$,

$$F_nL_n = \frac{\varphi^n-\psi^n}{\sqrt5}\bigl(\varphi^n+\psi^n\bigr) = \frac{\varphi^{2n}-\psi^{2n}}{\sqrt5} = F_{2n},$$

which is exactly Binet's formula at index $2n$.

*Rounding.* By Binet, $F_n = \varphi^n/\sqrt5 - \psi^n/\sqrt5$. Since $|\psi| = (\sqrt5-1)/2 \approx 0.618 < 1$,

$$\left|\frac{\psi^n}{\sqrt5}\right| \le \frac{1}{\sqrt5} \approx 0.447 < \frac12 .$$

So $\varphi^n/\sqrt5$ differs from the integer $F_n$ by less than $\frac12$, which means $F_n$ is the integer nearest to $\varphi^n/\sqrt5$; adding $\frac12$ and taking the floor selects that integer. Hence $F_n = \left\lfloor \varphi^n/\sqrt5+\frac12\right\rfloor$.

*Check at $n=4$.* $F_8 = 21$ and $F_4L_4 = 3\cdot7 = 21$ ✓. Also $\varphi^4/\sqrt5 = 6.8541/2.2361 = 3.0652$, and $\lfloor 3.0652+0.5\rfloor = \lfloor 3.5652\rfloor = 3 = F_4$ ✓. $\square$

**35.** *Strategy: expand $G$ by partial fractions and use the geometric series, factor by factor. No recurrence theory is used beyond the derivation of $G$ itself.*

From Section 7.11, $G(x) = \dfrac{x}{1-x-x^2}$ with $1-x-x^2 = (1-\varphi x)(1-\psi x)$, because $\varphi+\psi = 1$ and $\varphi\psi = -1$.

*Partial fractions.* Write

$$\frac{x}{(1-\varphi x)(1-\psi x)} = \frac{A}{1-\varphi x} + \frac{B}{1-\psi x}.$$

Multiplying out, $A(1-\psi x) + B(1-\varphi x) = x$. Comparing constant terms: $A + B = 0$. Comparing coefficients of $x$: $-A\psi - B\varphi = 1$. With $B = -A$ the second equation is $A(\varphi-\psi) = 1$, and since $\varphi-\psi = \sqrt5$,

$$A = \frac{1}{\sqrt5}, \qquad B = -\frac{1}{\sqrt5}.$$

*Expand each factor.* Since $\frac{1}{1-cx} = \sum_{n\ge0}c^nx^n$ for $|cx| < 1$,

$$G(x) = \frac{1}{\sqrt5}\left(\sum_{n\ge0}\varphi^nx^n - \sum_{n\ge0}\psi^nx^n\right) = \sum_{n\ge0}\frac{\varphi^n-\psi^n}{\sqrt5}\,x^n .$$

*Read off.* The coefficient of $x^n$ is $F_n$, so

$$F_n = \frac{\varphi^n-\psi^n}{\sqrt5}. \qquad \square$$

*Check.* $n = 0$: $0$ ✓. $n = 1$: $(\varphi-\psi)/\sqrt5 = 1$ ✓. $n = 2$: $(\varphi^2-\psi^2)/\sqrt5 = (\varphi-\psi)(\varphi+\psi)/\sqrt5 = 1$ ✓. $n = 3$: $(\varphi^3-\psi^3)/\sqrt5 = (\varphi-\psi)((\varphi+\psi)^2-\varphi\psi)/\sqrt5 = (1+1) = 2$ ✓.

*Remark.* The two ingredients are the geometric series and the factorisation $1-x-x^2 = (1-\varphi x)(1-\psi x)$ — that is, nothing beyond the definition of $\varphi$ and $\psi$. This is why generating functions are described as "automatic": the recurrence is used once, at the start, to produce the equation for $G$.

**36.** *Strategy: locate the real root by sign changes, show it is the only real root by examining the local maximum, and control the other two roots by the product of the roots.*

Let $P(r) = r^3-r^2-r-1$, the characteristic polynomial of $a_n = a_{n-1}+a_{n-2}+a_{n-3}$.

*Existence.* $P(1) = 1-1-1-1 = -2 < 0$ and $P(2) = 8-4-2-1 = 1 > 0$, so by the intermediate value theorem $P$ has a root $\alpha \in (1,2)$. Numerically $\alpha \approx 1.8392867$, and indeed $P(1.8392867) \approx 0$.

*Uniqueness of the real root.* $P'(r) = 3r^2-2r-1 = (3r+1)(r-1)$, so $P$ has a local maximum at $r = -1/3$ and a local minimum at $r = 1$. Now

$$P\!\left(-\tfrac13\right) = -\tfrac1{27}-\tfrac19+\tfrac13-1 = \frac{-1-3+9-27}{27} = -\frac{22}{27} < 0, \qquad P(1) = -2 < 0 .$$

The local maximum is negative, so the graph crosses the axis exactly once, to the right of the local minimum: $\alpha$ is the only real root.

*The other two roots.* Let them be $\beta$ and $\gamma$. Since the polynomial is real, $\gamma = \bar\beta$. For a monic cubic $r^3+a_2r^2+a_1r+a_0$ the product of the roots is $-a_0$; here $a_0 = -1$, so

$$\alpha\beta\gamma = 1, \qquad |\beta|^2 = \beta\gamma = \frac{1}{\alpha}, \qquad |\beta| = \frac{1}{\sqrt\alpha} \approx \frac{1}{1.3562} \approx 0.7373 < 1 .$$

*Conclusion.* By Theorem 7.6.1 the general solution is

$$a_n = c_1\alpha^n + c_2\beta^n + \overline{c_2}\,\bar\beta^{\,n},$$

and the last two terms are $O(0.738^n) \to 0$. The coefficient $c_1$ cannot vanish: if it did, $a_n \to 0$, whereas the sequence begins $a_2 = 1$, $a_3 = 1$, $a_4 = 2$, $a_5 = 4$, $a_6 = 7$ and is non-decreasing (each term is a sum of non-negative earlier terms), so $a_n \ge 1$ for all $n \ge 2$. Hence $c_1 > 0$ and

$$a_n = \Theta(\alpha^n), \qquad \alpha \approx 1.8392867 . \qquad \square$$

*Check of the growth rate.* The first terms are $0, 0, 1, 1, 2, 4, 7, 13, 24, 44, 81$, and $\alpha^{10} \approx 443.09$; the ratio $a_{10}/\alpha^{10} = 81/443.09 \approx 0.1828$ already approximates the limiting constant $c_1$. This is the same dominant-root phenomenon as $F_n = \Theta(\varphi^n)$, with $\varphi = 1.618\ldots$ replaced by the **Tribonacci constant** $\alpha = 1.839\ldots$
