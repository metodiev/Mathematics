# Rings — Solutions

> [Rings](README.md) · Solutions to [exercises.md](exercises.md) · 36 problems

Each solution states the strategy, then carries out every step. Section references point into [README.md](README.md).

## Beginner

**1.** (a) **Ring**, commutative, a domain, not a field ($2$ has no inverse in $\mathbb{Z}$).

(b) **Not a ring.** $(2\mathbb{Z},+)$ is an abelian group, multiplication is associative and distributive. But there is no identity: if $e \in 2\mathbb{Z}$ were an identity then $2e = 2$, so $e = 1 \notin 2\mathbb{Z}$. Axiom (R3) fails. This is the standard example of a rng.

(c) **Not a ring in our convention.** All of (R1)–(R4) hold, but $1 = 0$, so (R5) fails: it is the zero ring.

(d) **Not a ring.** The odd integers are not closed under addition ($1 + 1 = 2$ is even), so there is not even a binary operation of addition. (R1) fails.

(e) **Ring**, not commutative, not a domain: $E_{11}E_{22} = 0$ with both factors nonzero. Not a field.

(f) **Ring**, commutative, not a domain: $f = (1,0)$ and $g = (0,1)$ satisfy $fg = 0$ with $f, g \ne 0$. It is isomorphic to $\mathbb{Z} \times \mathbb{Z}$ via $h \mapsto (h(1), h(2))$.

(g) **Ring**, and in fact a field. Check each axiom. (R1) is the usual addition. (R2): $(a \star b)\star c = \frac{ab/2 \cdot c}{2} = \frac{abc}{4} = \frac{a(bc/2)}{2} = a \star (b \star c)$. (R3): $a \star 2 = \frac{2a}{2} = a = 2 \star a$, so the identity is $2 \ne 0$. (R4): $a \star (b+c) = \frac{a(b+c)}{2} = \frac{ab}{2} + \frac{ac}{2} = a\star b + a \star c$, and symmetrically. (R5): $2 \ne 0$. It is commutative, and if $a \star b = 0$ then $ab = 0$, so $a = 0$ or $b = 0$: a domain. Finally $a \star (4/a) = \frac{a \cdot 4/a}{2} = 2$ for $a \ne 0$, so every nonzero element is a unit. The map $a \mapsto a/2$ is an isomorphism $(\mathbb{R},+,\star) \to (\mathbb{R},+,\cdot)$.

**2.** *If $R$ is commutative*, then for all $a,b$,
$$(a+b)(a-b) = a^2 - ab + ba - b^2 = a^2 - b^2,$$
because $ba = ab$ and $ab - ba = 0$; distributivity and Proposition 5.2.1 give the expansion.

*Conversely*, suppose the identity holds for all $a,b$. Expanding both sides with distributivity,
$$a^2 - ab + ba - b^2 = a^2 - b^2.$$
Adding $-a^2 + b^2$ to both sides (in the abelian group $(R,+)$) gives $-ab + ba = 0$, i.e. $ba = ab$. Hence $R$ is commutative. The identity is therefore exactly a restatement of commutativity.

**3.** Using distributivity and $ab = ba$,
$$(a+b)^3 = (a+b)^2(a+b) = (a^2+2ab+b^2)(a+b) = a^3 + a^2b + 2a^2b + 2ab^2 + ab^2 + b^3 = a^3 + 3a^2b + 3ab^2 + b^3.$$
The step $(a+b)^2 = a^2 + 2ab + b^2$ uses $ab = ba$ (Proposition 5.2.2). In a non-commutative ring the expansion is $a^3 + a^2b + aba + ab^2 + ba^2 + bab + b^2a + b^3$, and the two expressions agree only under commutativity.

In $\mathbb{H}$, using $ij = k$ and $ji = -k$ (Exercise 31),
$$(i+j)(i-j) = i^2 - ij + ji - j^2 = (-1) - k + (-k) - (-1) = -2k \ne 0.$$
So the identity of Exercise 2 fails in $\mathbb{H}$, exactly as it must: $\mathbb{H}$ is not commutative.

**4.** *Units* are the classes $\bar a$ with $\gcd(a,n) = 1$ (Example 7.1.4).

* $\mathbb{Z}/8\mathbb{Z}$: units $\{1,3,5,7\}$, zero divisors $\{2,4,6\}$. Not a domain ($8$ not prime, and indeed $2\cdot 4 = 0$), not a field. Each unit squares to $1$ ($3^2 = 9 \equiv 1$, $5^2 = 25 \equiv 1$, $7^2 = 49 \equiv 1$), so $R^\times \cong \mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/2\mathbb{Z}$: no element has order $4$.
* $\mathbb{Z}/9\mathbb{Z}$: units $\{1,2,4,5,7,8\}$, zero divisors $\{3,6\}$ (since $3\cdot 3 = 9 \equiv 0$ and $6\cdot 6 = 36 \equiv 0$). Not a domain, not a field. The powers of $2$ are $2, 4, 8, 7, 5, 1$, so $R^\times = \langle 2\rangle \cong \mathbb{Z}/6\mathbb{Z}$.
* $\mathbb{Z}/10\mathbb{Z}$: units $\{1,3,7,9\}$, zero divisors $\{2,4,5,6,8\}$ (for instance $2\cdot 5 = 10 \equiv 0$, $4 \cdot 5 \equiv 0$, $6\cdot 5 \equiv 0$, $8\cdot 5 \equiv 0$). Not a domain, not a field. The powers of $3$ are $3, 9, 7, 1$, so $R^\times = \langle 3 \rangle \cong \mathbb{Z}/4\mathbb{Z}$.

In each case a nonzero nonunit is a zero divisor, which is no accident: in $\mathbb{Z}/n\mathbb{Z}$, $\bar a \ne 0$ is a zero divisor exactly when $\gcd(a,n) > 1$, and then $\bar a \cdot \overline{n/\gcd(a,n)} = \bar 0$.

**5.** (a) Since $a$ is a zero divisor there is $b \ne 0$ with $ab = 0$ or $ba = 0$; treat the first case, the other is symmetric. Then $(ua)b = u(ab) = 0$, and $ua \ne 0$ because $u^{-1}(ua) = a \ne 0$. So $ua$ is a zero divisor.

For the deduction, suppose $u$ were a zero divisor. Applying the first part with $u^{-1}$ in place of $u$ shows that $u^{-1}u = 1$ is a zero divisor. But $1 \cdot b = b \ne 0$ for every $b \ne 0$, so $1$ is not a zero divisor. Contradiction.

(b) In $\mathbb{Z}$, the element $2$ is neither a unit ($1/2 \notin \mathbb{Z}$) nor a zero divisor ($2b = 0$ forces $b = 0$). Such an example is **impossible** in $\mathbb{Z}/n\mathbb{Z}$: if $\gcd(a,n) = 1$ then $\bar a$ is a unit, and if $\gcd(a,n) = d > 1$ then $\overline{n/d} \ne \bar 0$ and $\bar a \cdot \overline{n/d} = \overline{a/d \cdot n} = \bar 0$, so $\bar a$ is a zero divisor. Thus for $n \ge 1$ every nonzero class is a unit or a zero divisor (or both, when the class is $0$; the nonzero case is exclusive).

**6.** Compute the least $n \ge 1$ with $n \cdot 1_R = 0$.

* $\mathbb{Z}/4\mathbb{Z} \times \mathbb{Z}/6\mathbb{Z}$: $\operatorname{lcm}(4,6) = 12$. Indeed $n\cdot(1,1) = (n \bmod 4, n\bmod 6) = 0$ iff $4\mid n$ and $6 \mid n$.
* $\mathbb{Z}/7\mathbb{Z}[x]$: $7$; the constants embed $\mathbb{Z}/7\mathbb{Z}$ and $x$ adds nothing.
* $M_3(\mathbb{Z}/5\mathbb{Z})$: $5$, since $n\cdot I_3 = nI_3$ vanishes iff $5 \mid n$.
* $\mathbb{Q}(\sqrt3)$: $0$, because it contains $\mathbb{Q}$ and $n \cdot 1 = n \ne 0$ for $n \ne 0$.
* $\mathbb{Z}/2\mathbb{Z} \times \mathbb{Q}$: $0$. If $n\cdot(1,1) = (n \bmod 2, n) = (0,0)$, the second coordinate gives $n = 0$. A ring of characteristic $0$ can therefore have a quotient of characteristic $2$.
* $\mathbb{Z}[i]/(3)$: $3$. We have $3 \cdot \bar 1 = \overline{3} = \bar 0$, and $1 \notin (3)$ because $1/3 \notin \mathbb{Z}[i]$, so $\bar 1 \ne \bar 0$.

**7.** (a) **Ideal.** $6\mathbb{Z}$ is an additive subgroup and $r(6k) = 6(rk) \in 6\mathbb{Z}$.

(b) **Ideal.** It is the kernel of the composite $\mathbb{Z}[x] \to \mathbb{Z} \to \mathbb{Z}/2\mathbb{Z}$, $f \mapsto f(0) \bmod 2$, hence an ideal by Theorem 7.5.4. Explicitly it is the ideal $(2,x)$: a polynomial with even constant term is $2g + xh$.

(c) **Ideal.** It is the kernel of the evaluation $f \mapsto f(1)$, so an ideal; explicitly it is $(x-1)$ by the factor theorem applied in $\mathbb{Z}[x]$ (division by the monic polynomial $x-1$).

(d) **Not an ideal**, though it is a subring (it contains $I_2$ and is closed under subtraction and multiplication). It is not closed under left multiplication by arbitrary matrices: with $E_{21} = \begin{pmatrix}0&0\\1&0\end{pmatrix}$ and $E_{11} = \begin{pmatrix}1&0\\0&0\end{pmatrix}$ upper triangular, the product $E_{21}E_{11} = E_{21}$ is not upper triangular.

(e) **Not an ideal.** $\mathbb{Z}[\frac12]$ is a subring of $\mathbb{Q}$, but $\mathbb{Q}$ is a field, so its only ideals are $(0)$ and $\mathbb{Q}$ (Proposition 7.8.7), and $\mathbb{Z}[\frac12]$ is neither. Concretely, $\frac13 \cdot \frac12 = \frac16 \notin \mathbb{Z}[\frac12]$.

(f) **Ideal.** $\{0,6,12\} = (6) = \{6\bar k : \bar k \in \mathbb{Z}/18\mathbb{Z}\}$, and $6 \cdot 18/6 = 18 \equiv 0$.

**8.** *Sum.* By Proposition 7.8.6-style reasoning in $\mathbb{Z}$, $(6) + (8) = (d)$ where $d = \gcd(6,8) = 2$. Directly, $2 = 8 - 6 \in (6)+(8)$, and $6, 8 \in (2)$, so $(6)+(8) = (2)$.

*Intersection.* $(6) \cap (8) = (24)$, because $24$ is the least positive common multiple. Indeed an element of the intersection is divisible by both $6$ and $8$, hence by $\operatorname{lcm}(6,8) = 24$.

*Product.* $(6)(8) = (48)$: finite sums of products $6a \cdot 8b = 48ab$ generate exactly the multiples of $48$.

*Strict inclusion.* $24 \in (6) \cap (8)$ but $24 \notin (48)$. This illustrates $IJ \subseteq I \cap J$, which is strict here because $(6) + (8) = (2) \ne \mathbb{Z}$. By Theorem 7.7.3, equality $IJ = I \cap J$ holds whenever $I + J = R$.

**9.** Take $I = 12\mathbb{Z} \subseteq J = 4\mathbb{Z}$ in $\mathbb{Z}$. The third isomorphism theorem (Corollary 7.6.4) with $R = \mathbb{Z}$ gives
$$(\mathbb{Z}/12\mathbb{Z})\big/(4\mathbb{Z}/12\mathbb{Z}) \cong \mathbb{Z}/4\mathbb{Z}.$$
*Counting check.* The elements of $4\mathbb{Z}/12\mathbb{Z}$ are $\{\bar 0, \bar 4, \bar 8\}$, an additive subgroup of order $3$ inside the group of order $12$. Its cosets are
$$\{\bar 0,\bar 4,\bar 8\}, \qquad \{\bar 1, \bar 5, \bar 9\}, \qquad \{\bar 2, \bar 6, \overline{10}\}, \qquad \{\bar 3, \bar 7, \overline{11}\},$$
four of them, and the quotient has order $12/3 = 4$. Since $4$ is prime, any ring of order $4$ that is a quotient of $\mathbb{Z}$ is $\mathbb{Z}/4\mathbb{Z}$. The quotient map sends $\bar k$ to $k \bmod 4$, which is exactly the identification.

**10.** Long division in $\mathbb{Q}[x]$:
$$2x^4 - 3x^3 + 4x - 5 = 2x^2(x^2-2) + \big(-3x^3 + 4x^2 + 4x - 5\big),$$
$$-3x^3 + 4x^2 + 4x - 5 = -3x(x^2-2) + \big(4x^2 - 2x - 5\big),$$
$$4x^2 - 2x - 5 = 4(x^2-2) + (-2x+3).$$
So $q = 2x^2 - 3x + 4$ and $r = -2x + 3$, with $\deg r = 1 < 2 = \deg g$. Verification:
$$(2x^2-3x+4)(x^2-2) = 2x^4 - 3x^3 + 4x^2 - 4x^2 + 6x - 8 = 2x^4 - 3x^3 + 6x - 8,$$
and adding $r$ gives $2x^4 - 3x^3 + 4x - 5$. By Theorem 7.11.3 the pair $(q,r)$ is unique.

**11.** Write $f = 2x^3+3x^2-8x+3$, so $a_0 = 3$, $a_3 = 2$. By Theorem 7.12.5 a rational root $p/q$ in lowest terms has $p \mid 3$ and $q \mid 2$, so the candidates are
$$\pm 1,\quad \pm 3,\quad \pm \tfrac12,\quad \pm \tfrac32.$$
Testing: $f(1) = 2+3-8+3 = 0$, so $x = 1$ is a root. Dividing by $x-1$,
$$2x^3+3x^2-8x+3 = (x-1)(2x^2+5x-3).$$
The quadratic factors as $(2x-1)(x+3)$ because $2x^2+5x-3 = 2x^2+6x-x-3 = 2x(x+3)-(x+3)$. Hence
$$f = (x-1)(2x-1)(x+3),$$
with roots $1$, $\tfrac12$, $-3$. Checks: $f(\tfrac12) = \tfrac14 + \tfrac34 - 4 + 3 = 0$ and $f(-3) = -54+27+24+3 = 0$. The rational root test produced exactly the three roots, as it must, since a cubic has at most three.

**12.** (a) $x^3+x+1$: the only candidates are $\pm1$; $f(1) = 3$ and $f(-1) = -1-1+1 = -1$, so there is no rational root. A degree $3$ polynomial with no root is irreducible over $\mathbb{Q}$ (Proposition 7.11.5).

(b) $x^2-3x+5$: the discriminant is $9 - 20 = -11 < 0$, so there is no real root, hence no rational root. A quadratic with no root is irreducible.

(c) $3x^2+6x+9$: **reducible**, because $3x^2+6x+9 = 3\,(x^2+2x+3)$ and both factors are nonunits in $\mathbb{Q}[x]$ (the content $3$ shows up as a nonunit constant factor). The quadratic $x^2+2x+3$ is itself irreducible (discriminant $-8 < 0$). This is the content trap: Eisenstein and the root test apply to primitive polynomials, and $f$ is not primitive.

(d) $x^4+x^2+1$: **reducible**, with the factorisation
$$x^4+x^2+1 = (x^2+x+1)(x^2-x+1),$$
which one finds by writing $x^4+x^2+1 = (x^2+1)^2 - x^2$ and using $A^2 - B^2 = (A-B)(A+B)$. Verification: $x^4 - x^3 + x^2 + x^3 - x^2 + x + x^2 - x + 1 = x^4+x^2+1$. Note that the polynomial has no rational root; the factorisation is into quadratics, which is why the root test alone would have been inconclusive.

## Intermediate

**13.** *Group.* By Proposition 7.1.2 the inverse of a unit is unique, $1 \in R^\times$, and the product of units is a unit because $(uu')(v'v) = 1 = (v'v)(uu')$ where $v, v'$ are the inverses of $u, u'$. Multiplication is associative in $R$, hence in $R^\times$, and $u^{-1}$ is the inverse of $u$ in $R^\times$. So $R^\times$ is a group.

*Product.* Let $R, S$ be rings. An element $(r,s) \in R \times S$ is a unit iff there is $(r', s')$ with $rr' = r'r = 1_R$ and $ss' = s's = 1_S$, that is, iff $r \in R^\times$ and $s \in S^\times$. Hence $(R\times S)^\times = R^\times \times S^\times$ as sets, and the multiplication is componentwise on both sides, so the two groups are equal (not merely isomorphic) under the identification. In particular $\lvert (R\times S)^\times\rvert = \lvert R^\times\rvert \cdot \lvert S^\times\rvert$, which for $R = \mathbb{Z}/m$, $S = \mathbb{Z}/n$ recovers $\varphi(mn) = \varphi(m)\varphi(n)$ when $\gcd(m,n) = 1$.

**14.** (a) $0 \in I_j$ for every $j$, so $0 \in \bigcap_j I_j$. If $a, b \in \bigcap_j I_j$ then for each $j$, $a - b \in I_j$ since $I_j$ is an additive subgroup; hence $a - b \in \bigcap_j I_j$. If $a \in \bigcap_j I_j$ and $r \in R$, then $ra, ar \in I_j$ for each $j$, so both lie in the intersection. Hence the intersection is an ideal.

(b) $0 = 0+0 \in I+J$. If $i_1+j_1$ and $i_2+j_2$ are in $I+J$ then their difference $(i_1-i_2) + (j_1-j_2) \in I+J$, and $r(i+j) = ri + rj \in I + J$, $(i+j)r = ir + jr \in I+J$. So $I+J$ is an ideal. (In a commutative ring only one of the last two displays is needed.)

(c) In $\mathbb{Z}$, $2 \in (2) \subseteq (2)\cup(3)$ and $3 \in (3) \subseteq (2)\cup(3)$, but $2+3 = 5 \notin (2)\cup(3)$: $5$ is divisible by neither $2$ nor $3$. So the union is not closed under addition and is not an ideal. The correct union-like operation is the sum: here $(2)+(3) = \mathbb{Z}$, since $3-2 = 1$.

**15.** (a) If $\varphi$ is injective then $\varphi(a) = 0 = \varphi(0)$ forces $a = 0$, so $\ker\varphi = (0)$. Conversely if the kernel is trivial and $\varphi(a) = \varphi(b)$, then $\varphi(a-b) = 0$, so $a - b = 0$ and $a = b$ (Theorem 7.5.4).

(b) Let $\varphi : F \to S$ be unital with $S \ne \{0\}$, so $1_S \ne 0_S$. The kernel is an ideal of the field $F$, hence $(0)$ or $F$ (Proposition 7.8.7). It is not $F$, because $\varphi(1_F) = 1_S \ne 0_S$. So it is $(0)$ and $\varphi$ is injective by (a).

(c) The map $\iota : \mathbb{Z} \to R$ is unital. By (a) it is injective iff its kernel is $(0)$, and by Definition 7.4.1 its kernel is $\operatorname{char}(R)\cdot\mathbb{Z}$. This is $(0)$ iff $\operatorname{char} R = 0$. (For $R$ a domain, (b) applied with $F = \mathbb{Q}$ shows that a ring of characteristic $0$ contains a copy of $\mathbb{Q}$ only if it is a field; $\mathbb{Z}$ itself is the typical characteristic-$0$ ring that is not a field.)

**16.** ($\Rightarrow$) If $I$ is a two-sided ideal, the quotient ring $R/I$ exists (Theorem 7.6.1) and the quotient map $\pi : R \to R/I$ is a ring homomorphism with $\ker\pi = I$.

($\Leftarrow$) If $I = \ker\varphi$ for a ring homomorphism $\varphi : R \to S$, then $I$ is an additive subgroup, and for $r \in R$, $x \in I$,
$$\varphi(rx) = \varphi(r)\varphi(x) = \varphi(r)\cdot 0 = 0, \qquad \varphi(xr) = 0,$$
so $rx, xr \in I$ (Theorem 7.5.4). This uses both operations in an essential way: an additive subgroup that is only a left ideal is the kernel of no ring homomorphism, as Example 7.6.2 illustrates.

**17.** (a) Define $\varphi : \mathbb{Z}[x] \to \mathbb{Z}[i]$ by $\varphi(f) = f(i)$. It respects addition, multiplication and $1$; it is surjective because $\varphi(a+bx) = a+bi$. Its kernel is $(x^2+1)$: certainly $x^2+1 \in \ker\varphi$. Conversely, if $f(i) = 0$, divide $f$ by the monic polynomial $x^2+1$ in $\mathbb{Z}[x]$: $f = q(x^2+1) + r$ with $q, r \in \mathbb{Z}[x]$ and $\deg r \le 1$ (division by a monic polynomial keeps integer coefficients). Then $0 = f(i) = r(i)$; writing $r = ax+b$ with $a,b \in \mathbb{Z}$ gives $b + ai = 0$, so $a = b = 0$ and $r = 0$. Hence $\ker\varphi = (x^2+1)$ and Theorem 7.7.1 gives $\mathbb{Z}[x]/(x^2+1) \cong \mathbb{Z}[i]$.

(b) Define $\varphi : \mathbb{Z} \to \mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/3\mathbb{Z}$ by $\varphi(n) = (n \bmod 2, n \bmod 3)$. It is a unital ring homomorphism and $\ker\varphi = 6\mathbb{Z}$. It is surjective: $\varphi(3) = (1,0)$ and $\varphi(4) = (0,1)$, so $\varphi(3a + 4b) = (a \bmod 2, b \bmod 3)$. Hence $\mathbb{Z}/6\mathbb{Z} \cong \mathbb{Z}/2\mathbb{Z}\times\mathbb{Z}/3\mathbb{Z}$ by Theorem 7.7.1. This is the Chinese remainder theorem in the smallest case.

(c) Define $\varphi : \mathbb{Z}[x] \to \mathbb{Z}$ by $\varphi(f) = f(3)$. It is a surjective unital homomorphism (constant polynomials hit everything). Its kernel is $(x-3)$ by the factor theorem: $f(3) = 0$ iff $x-3$ divides $f$, and division by the monic polynomial $x-3$ keeps integer coefficients. So $\mathbb{Z}[x]/(x-3) \cong \mathbb{Z}$.

**18.** *Statement.* If $\gcd(m,n) = 1$ then $\mathbb{Z}/mn\mathbb{Z} \cong \mathbb{Z}/m\mathbb{Z} \times \mathbb{Z}/n\mathbb{Z}$, or equivalently: for any residues $a, b$ the system $x \equiv a \pmod m$, $x \equiv b \pmod n$ has a solution, unique modulo $mn$. This is Theorem 7.7.3 with $(m) + (n) = \mathbb{Z}$.

*Solution.* Put $x = 2 + 7k$. The second congruence gives
$$2 + 7k \equiv 5 \pmod{12} \iff 7k \equiv 3 \pmod{12}.$$
Since $7 \cdot 7 = 49 \equiv 1 \pmod{12}$, the inverse of $7$ modulo $12$ is $7$, so
$$k \equiv 7 \cdot 3 = 21 \equiv 9 \pmod{12}.$$
Thus $x = 2 + 7\cdot 9 = 65$, and the general solution is $x \equiv 65 \pmod{84}$ because $\operatorname{lcm}(7,12) = 84$.

*Verification.* $65 = 9\cdot 7 + 2$, so $65 \equiv 2 \pmod 7$; $65 = 5\cdot 12 + 5$, so $65 \equiv 5 \pmod{12}$. Both hold, and $84 - 19 = 65$ confirms that the solution lies in $\{0,\dots,83\}$.

**19.** The ideals of $\mathbb{Z}/18\mathbb{Z}$ correspond to the divisors $d$ of $18$, that is, to $(d)$ for $d \in \{1,2,3,6,9,18\}$ (Theorem 7.6.3 applied to the ideals $d\mathbb{Z} \supseteq 18\mathbb{Z}$). Their containments are
$$(1) \supsetneq (2) \supsetneq (6) \supsetneq (0), \qquad (1) \supsetneq (3) \supsetneq (6) \supsetneq (0), \qquad (3) \supsetneq (9) \supsetneq (0).$$
*Prime and maximal.* $\mathbb{Z}/18\mathbb{Z}\big/(d) \cong \mathbb{Z}/d\mathbb{Z}$ (Corollary 7.6.4), which is a domain, equivalently a field, exactly when $d$ is prime. Among the divisors of $18$ only $2$ and $3$ are prime, so
$$\text{prime ideals} = \text{maximal ideals} = \{(2), (3)\}.$$
For instance $(6)$ is not prime: $\bar 2\bar 3 = \bar 6 = \bar 0$ with $\bar 2, \bar 3 \notin (6)$. And $(9)$ is not prime: $\bar 3 \cdot \bar 3 = \bar 9 = \bar 0$ with $\bar 3 \notin (9)$. The lattice is not a chain: $(2)$ and $(3)$ are incomparable.

**20.** *Prime.* By Exercise 17(a), $\mathbb{Z}[x]/(x^2+1) \cong \mathbb{Z}[i]$, which is a subring of $\mathbb{C}$ and hence an integral domain. By Theorem 7.8.3(1), $(x^2+1)$ is prime.

*Not maximal.* $\mathbb{Z}[i]$ is not a field: $2$ is a nonzero element with no inverse in $\mathbb{Z}[i]$ (if $2(a+bi) = 1$ then $2a = 1$ in $\mathbb{Z}$, impossible). So $R/(x^2+1) \cong \mathbb{Z}[i]$ is a domain that is not a field, and Theorem 7.8.3(2) says $(x^2+1)$ is not maximal.

*A maximal ideal containing it.* Take $M = (x^2+1, x-1)$. In the quotient, $x \equiv 1$ and $x^2 \equiv -1$, so $1 \equiv x^2 \equiv -1$, i.e. $2 \equiv 0$. Hence
$$\mathbb{Z}[x]/M \cong \mathbb{Z}[i]/(1-i) \cong \mathbb{F}_2,$$
which is a field, so $M$ is maximal. Explicitly the map $\mathbb{Z}[x] \to \mathbb{F}_2$, $f \mapsto f(1) \bmod 2$, is a surjective homomorphism with kernel exactly $(x^2+1, x-1)$: modulo $x^2+1$ and $x-1$ every polynomial reduces to a constant, and the surviving constants are those even modulo $2$. Since $2 \in M$ and $x - 1 \in M$, we have $(x^2+1) \subsetneq M \subsetneq \mathbb{Z}[x]$, confirming that the prime ideal is not maximal.

**21.** Write $R = \mathbb{Z}[\sqrt{-2}]$ and $N(a+b\sqrt{-2}) = a^2+2b^2 = z\bar z$. Then $N(zw) = z w \overline{zw} = z\bar z\, w \bar w = N(z)N(w)$, so $N$ is multiplicative, and $N(z) = 0$ iff $z = 0$.

Let $a, b \in R$ with $b \ne 0$. In the field $\mathbb{Q}(\sqrt{-2})$ compute
$$\frac{a}{b} = s + t\sqrt{-2}, \qquad s, t \in \mathbb{Q}.$$
Choose $m, n \in \mathbb{Z}$ with $\lvert s - m\rvert \le \tfrac12$ and $\lvert t - n\rvert \le \tfrac12$, and set $q = m+n\sqrt{-2} \in R$, $r = a - qb$. If $r = 0$ we are done. Otherwise
$$\frac{r}{b} = (s-m) + (t-n)\sqrt{-2}, \qquad N\!\left(\frac rb\right) = (s-m)^2 + 2(t-n)^2 \le \tfrac14 + \tfrac12 = \tfrac34 < 1,$$
so $N(r) = N(r/b)N(b) < N(b)$. Thus $N$ is a Euclidean function and $R$ is Euclidean. Note where the constant $2$ matters: the bound is $\tfrac14 + \tfrac{2}{4} = \tfrac34 < 1$. For $\mathbb{Z}[\sqrt{-5}]$ the same computation gives $\tfrac14 + \tfrac54 = \tfrac32 > 1$, so the argument fails, and indeed that ring is not Euclidean (Example 9.8).

**22.** Induct on $n = \deg f$. For $n = 0$, $f$ is a nonzero constant and has no roots.

For $n \ge 1$, if $f$ has no root there is nothing to prove. Otherwise let $a \in F$ be a root; by the factor theorem (Corollary 7.11.4), $f = (x-a)g$ with $\deg g = n-1$. If $b \in F$ is a root of $f$, then
$$0 = f(b) = (b-a)g(b),$$
and since $F$ is a field (so a domain) either $b = a$ or $g(b) = 0$. By induction $g$ has at most $n-1$ roots, so $f$ has at most $1 + (n-1) = n$ roots.

*Failure over $\mathbb{Z}/6\mathbb{Z}$.* Take $f = 3x \in (\mathbb{Z}/6\mathbb{Z})[x]$. It has degree $1$, but $\bar 0$, $\bar 2$ and $\bar 4$ are all roots, since $3\cdot 0 = 0$, $3\cdot 2 = 6 \equiv 0$ and $3 \cdot 4 = 12 \equiv 0$. That is three roots for a degree $1$ polynomial. The induction fails because a product of nonzero elements can be zero: $3 \cdot 2 = 0$ in $\mathbb{Z}/6\mathbb{Z}$.

## Advanced

**23.** (a) $N(zw) = zw\overline{zw} = z w \bar z\bar w = (z\bar z)(w\bar w) = N(z)N(w)$, using that conjugation is multiplicative. If $N(z) = 1$ then $z\bar z = 1$, so $\bar z$ is an inverse of $z$ and lies in $\mathbb{Z}[i]$; hence $z$ is a unit. Conversely, if $z$ is a unit with inverse $w$, then $1 = N(1) = N(zw) = N(z)N(w)$ with $N(z), N(w) \in \mathbb{N}_0$, so $N(z) = 1$.

(b) $N(a+bi) = a^2+b^2 = 1$ forces $a^2, b^2 \in \{0,1\}$ with exactly one of them $1$. Hence $z \in \{\pm1, \pm i\}$, and all four of these are units ($i \cdot (-i) = 1$). So $\mathbb{Z}[i]^\times = \{\pm1, \pm i\}$, a cyclic group of order $4$.

(c) If $z \mid w$ then $w = zk$ for some $k \in \mathbb{Z}[i]$, so $N(w) = N(z)N(k)$. If $w \ne 0$ then $N(k) \ne 0$, hence $N(k) \ge 1$ and $N(z) \le N(w)$. In the Euclidean algorithm, each remainder $r$ satisfies $N(r) < N(b)$ (Proposition 7.9.4), so the norms form a strictly decreasing sequence in $\mathbb{N}_0$; such a sequence cannot be infinite, so the algorithm reaches a zero remainder after finitely many steps. Part (c) is exactly the statement that "divisibility forces the norm to grow", which is what rules out infinite descent.

**24.** Let $R$ be a UFD and let $p \in R$ be irreducible. Suppose $p \mid ab$, so $ab = pc$ for some $c$. Write
$$a = u\,a_1\cdots a_r, \qquad b = v\,b_1\cdots b_s, \qquad c = w\,c_1\cdots c_t$$
with $u, v, w$ units and all $a_i, b_j, c_k$ irreducible; this is possible because $R$ is a UFD (for a unit the product is empty). Then
$$uv\,a_1\cdots a_r b_1\cdots b_s = pw\,c_1\cdots c_t.$$
Both sides are factorisations into irreducibles (the units do not count as factors). By uniqueness, the multiset of irreducible factors on the left equals that on the right up to associates. The left side contains the irreducible factors $a_i$ and $b_j$; the right side contains $p$ and the $c_k$. Hence $p$ is associate to some $a_i$ or to some $b_j$. In the first case $p \mid a$, in the second $p \mid b$. Therefore $p$ is prime.

**25.** Since $R$ is a PID, the ideal $(a) + (b)$ is principal, say $(a) + (b) = (d)$.

*d is a gcd.* Because $a \in (d)$ and $b \in (d)$, $d \mid a$ and $d \mid b$. If $e \mid a$ and $e \mid b$, then $(a) \subseteq (e)$ and $(b) \subseteq (e)$, so $(d) = (a)+(b) \subseteq (e)$, i.e. $e \mid d$. Hence $d$ is a greatest common divisor of $a$ and $b$.

*Bézout.* Since $d \in (a)+(b) = \{ax + by : x,y \in R\}$, there exist $x, y$ with $d = ax+by$.

*Uniqueness up to associates.* If $d'$ is another gcd then $d \mid d'$ and $d' \mid d$, so $d' = du$ with $u$ a unit; thus $(d') = (d)$.

*lcm.* Let $(a) \cap (b) = (l)$. Then $l \in (a)$ and $l \in (b)$, so $a \mid l$ and $b \mid l$: $l$ is a common multiple. If $a \mid m$ and $b \mid m$ then $m \in (a)\cap(b) = (l)$, so $l \mid m$. Hence $l$ is a least common multiple. In $\mathbb{Z}$ this reduces to $(a)+(b) = (\gcd(a,b))$ and $(a)\cap(b) = (\operatorname{lcm}(a,b))$, which sharpens Exercise 8.

**26.** $k[x,y]$ is a domain by Proposition 7.11.1 applied twice.

*$(x,y)$ is maximal.* It is the kernel of the evaluation $\varphi : k[x,y] \to k$, $\varphi(f) = f(0,0)$, which is a surjective unital ring homomorphism. Hence $k[x,y]/(x,y) \cong k$ is a field, and $(x,y)$ is maximal by Theorem 7.8.3(2).

*$(x,y)$ is not principal.* Suppose $(x,y) = (h)$. Since $x \in (h)$, $x = hg$ for some $g$, and comparing total degrees gives $\deg h + \deg g = 1$. If $\deg h = 0$ then $h \in k\setminus\{0\}$ is a unit, so $(h) = k[x,y]$, contradicting the properness of $(x,y)$. Hence $\deg h = 1$ and $\deg g = 0$, i.e. $g \in k^\times$; then $h = x/g$ is a nonzero scalar multiple of $x$, so $(h) = (x)$. But $y \notin (x)$: every element $xf$ has zero coefficient of $y^1$ when expanded in powers of $y$. Contradiction.

*$k[x,y]$ is not a PID*, since $(x,y)$ is an ideal that is not principal.

*$(x)$ is prime but not maximal.* $k[x,y]/(x) \cong k[y]$, a domain but not a field (the class of $y$ is a nonzero nonunit). So $(x)$ is prime and not maximal, exactly as with $(x) \subseteq \mathbb{Z}[x]$ (Example 7.8.5). Note $(x) \subsetneq (x,y)$, which is another way to see that $(x)$ is not maximal.

**27.** Let $R$ be a domain and suppose $R[x]$ is a UFD. $R$ is a domain by hypothesis.

*Existence.* Let $a \in R$ be a nonzero nonunit. In $R[x]$, factor $a = f_1\cdots f_m$ with each $f_i$ irreducible. Since $\deg a = 0$ and $\deg(fg) = \deg f + \deg g$ in a polynomial ring over a domain (Proposition 7.11.1), each $\deg f_i = 0$, so $f_i \in R$. If $f_i = bc$ with $b, c \in R$ nonunits, then $b, c$ are also nonunits in $R[x]$ (because $R[x]^\times = R^\times$ by Proposition 7.11.2), contradicting irreducibility of $f_i$ in $R[x]$. Hence each $f_i$ is irreducible in $R$, and $a$ is a product of irreducibles.

*Uniqueness.* Suppose $p_1\cdots p_m = q_1\cdots q_s$ in $R$ with all factors irreducible in $R$. These are irreducible in $R[x]$ by the argument above (a nonunit of $R$ is a nonunit of $R[x]$). Since $R[x]$ is a UFD, $m = s$ and, after reordering, $p_i = u_i q_i$ with $u_i \in R[x]^\times = R^\times$. So $p_i \sim q_i$ in $R$. Hence $R$ is a UFD.

**28.** Start from the identity
$$\Phi_p(x) = \frac{x^p-1}{x-1} = x^{p-1}+x^{p-2}+\cdots+x+1,$$
valid in $\mathbb{Z}[x]$ because $(x-1)\Phi_p(x) = x^p-1$. Substitute $x+1$:
$$\Phi_p(x+1) = \frac{(x+1)^p - 1}{x} = \sum_{k=1}^{p}\binom{p}{k}x^{k-1} = x^{p-1} + \binom{p}{p-1}x^{p-2} + \cdots + \binom{p}{2}x + \binom{p}{1}.$$
The division by $x$ is exact because $(x+1)^p - 1$ has zero constant term. The coefficients are:

* the leading coefficient is $1$, not divisible by $p$;
* for $1 \le j \le p-1$ the coefficient of $x^{p-1-j}$ is $\binom{p}{j}$, divisible by $p$ because $p$ is prime and $1 \le j \le p-1$;
* the constant term is $\binom{p}{1} = p$, and $p^2 \nmid p$.

Eisenstein's criterion (Theorem 7.12.6) therefore gives irreducibility of $\Phi_p(x+1)$ over $\mathbb{Q}$, and by Corollary 7.12.7 ($x \mapsto x-1$ is an automorphism of $\mathbb{Q}[x]$) $\Phi_p(x)$ is irreducible over $\mathbb{Q}$. For example $\Phi_3 = x^2+x+1$ and $\Phi_3(x+1) = x^2+3x+3$, Eisenstein at $3$; $\Phi_5 = x^4+x^3+x^2+x+1$ and $\Phi_5(x+1) = x^4+5x^3+10x^2+10x+5$.

**29.** *$(2+i)$ is maximal.* By Proposition 7.9.4, $\mathbb{Z}[i]$ is Euclidean, hence a PID (Theorem 7.9.2). The element $2+i$ is irreducible: $N(2+i) = 4+1 = 5$, and if $2+i = zw$ with both factors nonunits, then $5 = N(z)N(w)$ with $N(z), N(w) \ge 2$, which is impossible. In a PID irreducible elements are prime (Lemma 7.10.5), so $(2+i)$ is a prime ideal, and in a PID every nonzero prime ideal is maximal (Proposition 7.8.6). Hence $\mathbb{Z}[i]/(2+i)$ is a field.

*Size.* In the quotient, $2 + i = 0$, so $i = -2$. Hence every class is the class of an integer: $a + bi \equiv a - 2b \pmod{2+i}$, an integer. Also $5 = (2+i)(2-i) \equiv 0$, so the class of $a-2b$ depends only on $a - 2b \bmod 5$. Therefore the quotient has at most $5$ elements, and it has exactly $5$ because the classes of $0,1,2,3,4$ are distinct: if $a \in \{0,\dots,4\}$ were divisible by $2+i$ in $\mathbb{Z}[i]$, then $a = (2+i)(u+vi) = (2u - v) + (u + 2v)i$, so $u + 2v = 0$, $u = -2v$, $a = 2(-2v) - v = -5v$, which forces $v = 0$ and $a = 0$. A field with $5$ elements is $\mathbb{F}_5$, so $\mathbb{Z}[i]/(2+i) \cong \mathbb{F}_5$.

*Explicit isomorphism.* The map
$$\varphi : \mathbb{Z}[i] \to \mathbb{F}_5, \qquad \varphi(a+bi) = a - 2b \bmod 5,$$
is a unital ring homomorphism (it is evaluation at $i \mapsto -2$, i.e. reduction modulo the ideal $(x+2)$ composed with $\mathbb{Z}[x] \to \mathbb{Z}[i]$). It is surjective, and $\varphi(a+bi) = 0$ iff $a \equiv 2b \pmod 5$ iff $a + bi = (a-2b) + b(2+i) \in (2+i)$. So the kernel is $(2+i)$ and Theorem 7.7.1 identifies the quotient with $\mathbb{F}_5$.

**30.** (a) Let $R$ be a PID, $I$ an ideal, and $\pi : R \to R/I$ the quotient map. By Theorem 7.6.3 every ideal of $R/I$ has the form $J/I$ with $J$ an ideal of $R$ containing $I$. Since $R$ is a PID, $J = (a)$ for some $a$, so
$$J/I = \pi(J) = \pi((a)) = (a + I)$$
is principal, generated by the class of $a$. Hence every ideal of $R/I$ is principal.

(b) For $R = \mathbb{Z}$, $I = 4\mathbb{Z}$: the ideals of $\mathbb{Z}/4\mathbb{Z}$ correspond to the divisors $d$ of $4$, namely $d \in \{1,2,4\}$, giving
$$(\bar 1) = \mathbb{Z}/4\mathbb{Z}, \qquad (\bar 2) = \{\bar 0, \bar 2\}, \qquad (\bar 4) = (\bar 0) = \{\bar 0\}.$$
All are principal, as (a) predicts. The ring is not a domain because $\bar 2 \cdot \bar 2 = \bar 4 = \bar 0$ with $\bar 2 \ne \bar 0$; and it is not a field because $\bar 2$ is not a unit ($\bar 2 \cdot \bar k \in \{\bar 0, \bar 2\}$ for every $k$). This shows that "every ideal is principal" does not imply "domain", so a principal ideal *ring* need not be a principal ideal *domain*.

**31.** *The multiplication table.* From $i^2 = j^2 = k^2 = -1$ and $ijk = -1$: multiply $ijk = -1$ on the left by $i^{-1} = -i$ to get $jk = i$; multiply on the left by $j^{-1} = -j$ to get $ki = j$. Then $k = ij$ because $i \cdot jk = i \cdot i = -1$ and also $i(jk) = (ij)k$, so $(ij)k = -1 = k^2$, giving $ij = k$ after multiplying by $k^{-1}$ on the right. Now $ji = -k$ since $(ij)^{-1} = j^{-1}i^{-1} = (-j)(-i) = ji$ while $(ij)^{-1} = k^{-1} = -k$. Similarly $kj = -i$ and $ik = -j$. Summarising,
$$ij = k,\quad ji = -k,\quad jk = i,\quad kj = -i,\quad ki = j,\quad ik = -j,$$
and $ijk = (ij)k = k^2 = -1$, consistent with the defining relation.

*Associativity.* Rather than checking $4^3 = 64$ triples by hand, represent
$$1 \mapsto I_2, \quad i \mapsto \begin{pmatrix} i & 0\\ 0 & -i\end{pmatrix}, \quad j \mapsto \begin{pmatrix}0&1\\-1&0\end{pmatrix}, \quad k \mapsto \begin{pmatrix}0&i\\ i&0\end{pmatrix}.$$
These four complex matrices are linearly independent over $\mathbb{R}$ and satisfy $i^2 = j^2 = k^2 = ijk = -I_2$, as a direct computation shows. Hence the eight axioms hold for $\mathbb{H}$ by transport: $\mathbb{H}$ is isomorphic to the $\mathbb{R}$-span of these matrices, a subring of $M_2(\mathbb{C})$, so associativity and distributivity are inherited.

*Inverses.* For $z = a+bi+cj+dk$ put $\bar z = a - bi - cj - dk$. Multiplying out and using the table, every cross term cancels in pairs: for example $bi \cdot (-cj) = -bc\,ij = -bc k$ and $cj \cdot (-bi) = -bc\,ji = +bc k$. Hence
$$z\bar z = a^2+b^2+c^2+d^2 \in \mathbb{R}_{\ge 0},$$
which is nonzero when $z \ne 0$. Therefore
$$z^{-1} = \frac{\bar z}{z\bar z}$$
is defined and satisfies $zz^{-1} = 1$. Every nonzero element is a unit, so $\mathbb{H}$ is a division ring; it is not a field because $ij = k \ne -k = ji$.

## Challenge

**32.** Let $R = \mathbb{Z}[\sqrt{-3}] = \{a+b\sqrt{-3} : a,b \in \mathbb{Z}\}$, a subring of $\mathbb{C}$ and hence a domain, with $N(a+b\sqrt{-3}) = a^2+3b^2 = z\bar z$, multiplicative because conjugation is.

*Units.* $N(u) = 1$ gives $a^2+3b^2 = 1$, so $b = 0$ and $a = \pm1$: the units are $\pm 1$.

*Two factorisations.*
$$4 = 2\cdot 2 = (1+\sqrt{-3})(1-\sqrt{-3}),$$
since $(1+\sqrt{-3})(1-\sqrt{-3}) = 1 - (-3) = 4$.

*$2$ is irreducible.* $N(2) = 4$. If $2 = zw$ with $z, w$ nonunits then $4 = N(z)N(w)$ with $N(z), N(w) \ge 2$, so $N(z) = N(w) = 2$. But $a^2+3b^2 = 2$ has no integer solution: $a^2 \le 2$ gives $a^2 \in \{0,1\}$, leaving $3b^2 \in \{2,1\}$, impossible.

*$1+\sqrt{-3}$ is irreducible.* $N(1+\sqrt{-3}) = 1+3 = 4$. A factorisation into two nonunits would again force a factor of norm $2$, which does not exist. The same argument applies to $1-\sqrt{-3}$.

*The factorisations are genuinely different.* All four factors have norm $4$, so the norm does **not** distinguish them; this is the difference from Example 9.8, where the norms $4, 9, 6, 6$ separated the factors. Instead compare directly. The only units are $\pm 1$, and
$$1+\sqrt{-3} \ne \pm 2, \qquad 1-\sqrt{-3} \ne \pm 2, \qquad 1+\sqrt{-3} \ne \pm(1-\sqrt{-3}).$$
So no factor $2$ is associate to either $1\pm\sqrt{-3}$, and the multisets $\{2,2\}$ and $\{1+\sqrt{-3}, 1-\sqrt{-3}\}$ are different up to order and associates. Therefore $4$ has two essentially different factorisations into irreducibles and $R$ is not a UFD.

*Remark.* Since $\mathbb{Z}[\sqrt{-3}]$ is not integrally closed (the element $\frac{1+\sqrt{-3}}{2}$ is integral over $\mathbb{Z}[\sqrt{-3}]$ but not in it), it is not a ring of integers of a number field; the ring of integers of $\mathbb{Q}(\sqrt{-3})$ is $\mathbb{Z}[\frac{1+\sqrt{-3}}{2}]$, and that larger ring is a PID.

**33.** $M$ is well defined because $\{N(ax) : x \ne 0\}$ is a nonempty subset of $\mathbb{N}_0$ and $\mathbb{N}_0$ is well ordered.

*$M$ is a Euclidean function.* Let $a, b \in R$ with $b \ne 0$. Choose $x_0 \ne 0$ with $M(b) = N(bx_0)$, which exists by definition of a minimum. Apply the Euclidean property of $N$ to the pair $(ax_0, bx_0)$: there are $q, r_0 \in R$ with
$$ax_0 = q\,bx_0 + r_0, \qquad r_0 = 0 \ \text{or}\ N(r_0) < N(bx_0) = M(b).$$
If $r_0 = 0$ then $(a - qb)x_0 = 0$, and since $R$ is a domain and $x_0 \ne 0$ we get $a = qb$, so the division of $a$ by $b$ has remainder $0$.

If $r_0 \ne 0$, put $r = a - qb$, so that $r_0 = rx_0$. Then $r \ne 0$, and by definition of $M$,
$$M(r) = \min_{x \ne 0} N(rx) \le N(rx_0) = N(r_0) < M(b).$$
So $a = qb + r$ with $r = 0$ or $M(r) < M(b)$: $M$ is a Euclidean function.

*Submultiplicativity.* For nonzero $a, b$,
$$M(ab) = \min_{x \ne 0} N(abx), \qquad M(a) = \min_{y \ne 0} N(ay) \le N(abx) \ \text{ for every } x \ne 0,$$
where the inequality uses $y = bx \ne 0$ (valid since $R$ is a domain and $b, x \ne 0$). Taking the minimum over $x \ne 0$ gives $M(a) \le M(ab)$.

**34.** Write $f = x^4+1$.

*$p = 2$.* In $\mathbb{F}_2[x]$, $f = x^4 + 1 = x^4 + 2x^2 + 1 = (x^2+1)^2$, since $2 = 0$. So $f$ is reducible.

*$p$ odd.* The multiplicative group $\mathbb{F}_p^\times$ has order $p-1$, and the map $x \mapsto x^2$ has kernel $\{\pm1\}$ of size $2$, so exactly $(p-1)/2$ nonzero squares and $(p-1)/2$ non-squares; the product of two non-squares is a square because the Legendre symbol is multiplicative. Hence at least one of $-1$, $2$, $-2$ is a square modulo $p$: if $-1$ is a square we are done, otherwise if $2$ is a square we are done, and if both are non-squares then $(-1)\cdot 2 = -2$ is a square.

Let $a \in \mathbb{F}_p$ be a square root of the relevant element.

* If $a^2 = -1$: $x^4+1 = x^4 - a^2 = (x^2-a)(x^2+a)$.
* If $a^2 = 2$: $x^4+1 = (x^2+1)^2 - 2x^2 = (x^2+1)^2 - (ax)^2 = (x^2+1-ax)(x^2+1+ax)$.
* If $a^2 = -2$: $x^4+1 = (x^2-1)^2 + 2x^2 = (x^2-1)^2 - (ax)^2 = (x^2-1-ax)(x^2-1+ax)$.

Each display is a factorisation into two polynomials of degree $2$ with coefficients in $\mathbb{F}_p$, so $f$ is reducible over $\mathbb{F}_p$ for every prime $p$. Irreducibility over $\mathbb{Q}$ (Example 9.6) is therefore not detected by reduction: by Proposition 7.12.8, a *sufficient* condition is that some reduction be irreducible, and here no reduction is.

**35.** Let $I \subsetneq R$ be a proper ideal and let
$$\mathcal{S} = \{J : J \text{ ideal of } R,\ I \subseteq J \subsetneq R\},$$
partially ordered by inclusion. Then $\mathcal{S} \ne \varnothing$ because $I \in \mathcal{S}$.

*Chains have upper bounds.* Let $\mathcal{C} \subseteq \mathcal{S}$ be a nonempty chain and put $U = \bigcup_{J \in \mathcal{C}} J$. Then $U$ is an ideal: given $a, b \in U$ there are $J_1, J_2 \in \mathcal{C}$ with $a \in J_1$, $b \in J_2$; since $\mathcal{C}$ is a chain, one of $J_1, J_2$ contains the other, say $J_1 \subseteq J_2$; then $a, b \in J_2$, so $a - b \in J_2 \subseteq U$, and for $r \in R$, $ra \in J_1 \subseteq U$. Finally $U$ is proper: if $1 \in U$ then $1 \in J$ for some $J \in \mathcal{C}$, which would give $J = R$, contradicting $J \subsetneq R$. So $U \in \mathcal{S}$ and $U$ is an upper bound for $\mathcal{C}$.

*Zorn.* By Zorn's lemma $\mathcal{S}$ has a maximal element $M$. If $M \subsetneq J \subsetneq R$ for some ideal $J$, then $J \in \mathcal{S}$ and $J$ strictly contains $M$, contradicting maximality. Hence $M$ is a maximal ideal, and $I \subseteq M$.

The argument uses Zorn's lemma, which is equivalent to the axiom of choice; without it the statement can fail in ZF. Note also where $1 \ne 0$ is used: it is what makes $I$ itself proper and what makes a union of proper ideals proper, via the element $1$.

**36.** (i) $\Rightarrow$ (ii): let $R = F$ be a field and $\varphi : F \to S$ a nonzero ring homomorphism. The kernel is an ideal of $F$, so it is $(0)$ or $F$ (Proposition 7.8.7). If $\ker\varphi = F$ then $\varphi(1) = 0$, so $\varphi(r) = \varphi(r\cdot1) = 0$ for all $r$ and $\varphi$ is the zero homomorphism, contrary to hypothesis. Hence $\ker\varphi = (0)$ and $\varphi$ is injective by Theorem 7.5.4.

(ii) $\Rightarrow$ (i): suppose $R$ is not a field. Then $R$ has a nonzero nonunit $a$: if every nonzero element were a unit, $R$ would be a field. The quotient map $\pi : R \to R/(a)$ is a nonzero homomorphism, because $\pi(1) = 1 + (a) \ne 0 + (a)$ (as $(a) \ne R$), and it is not injective, because $a \ne 0$ lies in its kernel. This contradicts (ii). Hence $R$ is a field.

(i) $\Rightarrow$ (iii): if $R = F$ is a field, $F[x]$ is Euclidean with Euclidean function $\deg$ by the division algorithm (Theorem 7.11.3), so (iii) holds.

(iii) $\Rightarrow$ (i): if $R[x]$ is a Euclidean domain then it is a PID (Theorem 7.9.2), and $R$ is a field by Proposition 7.11.7.

The three conditions are therefore equivalent. The equivalence (i) $\Leftrightarrow$ (iii) is a good illustration of the general principle that a property of $R$ can be read off from $R[x]$: the polynomial ring adds a variable but remembers the coefficient ring.
