# Fields — Solutions

> [Fields](README.md) · Solutions to [exercises.md](exercises.md) · 36 problems

Each solution states the strategy, then carries out every step. Section references point into [README.md](README.md).

## Beginner

**1.** (a) **Field.** All axioms hold in $\mathbb{Q}$; every nonzero rational has a rational inverse.

(b) **Not a field.** $2$ has no inverse in $\mathbb{Z}$: $2b = 1$ has no integer solution.

(c) **Field.** $7$ is prime, so every nonzero class $\bar a$ has $\gcd(a,7) = 1$ and Bézout gives $\bar a^{-1}$ (Corollary 7.2.4 of [Rings](../02-rings/README.md)).

(d) **Not a field.** $\bar 2 \ne \bar 0$ but $\bar 2\cdot\bar 4 = \bar 0$, so the ring has zero divisors; equivalently $\bar 2$ has no inverse, since $2b \equiv 1 \pmod 8$ would force an odd number to be even.

(e) **Not a field.** The only units are the nonzero constants, $\mathbb{Q}^\times$; $x$ has no inverse, because $\deg(xf) = 1 + \deg f \ne 0 = \deg 1$.

(f) **Field.** For $a+b\sqrt2 \ne 0$,
$$(a+b\sqrt2)^{-1} = \frac{a-b\sqrt2}{a^2-2b^2},$$
and $a^2 - 2b^2 \ne 0$ because $\sqrt2 \notin \mathbb{Q}$.

(g) **Not a field**, though it is a division ring: every nonzero element is invertible (Exercise 31 of the rings tutorial), but $ij = k \ne -k = ji$, so multiplication is not commutative.

(h) **Not a field.** $\mathbb{Q}[[x]]$ is an integral domain, but $x$ has no inverse: if $x\sum b_nx^n = 1$ then the coefficient of $x^0$ on the left is $0$, on the right it is $1$.

(i) **Field.** $x^2+x+1$ is irreducible over $\mathbb{F}_2$ (no root), so the quotient by its principal ideal is a field (Theorem 7.3.4).

(j) **Not a field.** $2$ is not invertible: $2(a+bi) = 1$ forces $2a = 1$ in $\mathbb{Z}$.

**2.** By Theorem 5.3.3 the prime subfield is $\mathbb{F}_p$ when the characteristic is $p$ and $\mathbb{Q}$ when it is $0$.

* $\mathbb{F}_{49}$: characteristic $7$, so the prime subfield is $\mathbb{F}_7$.
* $\mathbb{Q}(\sqrt[3]2)$: characteristic $0$, so $\mathbb{Q}$.
* $\mathbb{F}_2(x)$: characteristic $2$, so $\mathbb{F}_2$.
* $\mathbb{Q}(\pi)$: characteristic $0$, so $\mathbb{Q}$ (even though $\pi$ is transcendental, the prime field only sees $1$).
* $\mathbb{C}$: characteristic $0$, so $\mathbb{Q}$.

**3.** (a) $\sqrt5$: $x^2-5$ vanishes there, and it is irreducible over $\mathbb{Q}$ because $5$ is not the square of a rational. So $m = x^2-5$ and $[\mathbb{Q}(\sqrt5):\mathbb{Q}] = 2$.

(b) $\sqrt[3]3$: $x^3-3$ is Eisenstein at $p = 3$, hence irreducible, so $m = x^3-3$ and the degree is $3$.

(c) $\zeta_6 = e^{2\pi i/6} = \tfrac12 + \tfrac{\sqrt3}{2}i$. It satisfies
$$\zeta_6^2 - \zeta_6 + 1 = 0,$$
the sixth cyclotomic polynomial. The quadratic $x^2-x+1$ has discriminant $1-4 = -3 < 0$, so it is irreducible over $\mathbb{Q}$; hence $m = x^2-x+1$ and the degree is $2$. (Note $\zeta_6 = -\zeta_3$, so $\mathbb{Q}(\zeta_6) = \mathbb{Q}(\sqrt{-3})$.)

(d) $i$ over $\mathbb{Q}(\sqrt2)$: $x^2+1$ vanishes at $i$. It is irreducible over $\mathbb{Q}(\sqrt2)$ because $\mathbb{Q}(\sqrt2) \subseteq \mathbb{R}$ contains no square root of $-1$. Hence $[\mathbb{Q}(\sqrt2,i):\mathbb{Q}(\sqrt2)] = 2$.

**4.** *$[\mathbb{Q}(\sqrt2,\sqrt5):\mathbb{Q}] = 4$.* We show $\sqrt5 \notin \mathbb{Q}(\sqrt2)$. If $\sqrt5 = a+b\sqrt2$ with $a,b \in \mathbb{Q}$, then $5 = a^2+2b^2+2ab\sqrt2$; since $\sqrt2 \notin \mathbb{Q}$, $ab = 0$. If $b = 0$ then $\sqrt5 \in \mathbb{Q}$, false; if $a = 0$ then $5 = 2b^2$, which has no rational solution ($2p^2 = 5q^2$ forces $2 \mid q$ and then $4 \mid 2p^2$, so $2\mid p$). Hence $x^2-5$ is irreducible over $\mathbb{Q}(\sqrt2)$, and the tower law gives $2\cdot2 = 4$.

*$[\mathbb{F}_{27}:\mathbb{F}_3] = 3$*, because $\lvert\mathbb{F}_{27}\rvert = 27 = 3^3$ and the dimension over $\mathbb{F}_3$ is the exponent (Theorem 7.5.1).

*$[\mathbb{C}:\mathbb{Q}] = \infty$*, since a finite-dimensional vector space over the countable field $\mathbb{Q}$ is countable, while $\mathbb{C}$ is not.

*$[\mathbb{Q}(\sqrt2,\sqrt[3]2):\mathbb{Q}] = 6$.* First $[\mathbb{Q}(\sqrt[3]2):\mathbb{Q}] = 3$. If $\sqrt2 \in \mathbb{Q}(\sqrt[3]2)$ then, by the tower law, $2 = [\mathbb{Q}(\sqrt2):\mathbb{Q}]$ would divide $3$, which is false. So $x^2-2$ is irreducible over $\mathbb{Q}(\sqrt[3]2)$ and the degree over that field is $2$. Total: $3\cdot2 = 6$.

**5.** *$\mathbb{F}_4$.* The elements are $0, 1, \alpha, \alpha+1$ with $\alpha^2 = \alpha+1$. Since $\alpha^2 = \alpha+1$, we get $\alpha^3 = \alpha(\alpha+1) = \alpha^2+\alpha = 1$. Also $1+\alpha^2 = 1+\alpha+1 = \alpha$. Hence
$$(1+\alpha)(1+\alpha^2) = (1+\alpha)\alpha = \alpha+\alpha^2 = \alpha+\alpha+1 = 1.$$

*$\mathbb{F}_9$.* The elements are $a+b\alpha$ with $a,b \in \mathbb{F}_3$ and $\alpha^2 = -1 = 2$: that is $0,1,2,\alpha,2\alpha,1+\alpha,1+2\alpha,2+\alpha,2+2\alpha$. Then
$$(1+\alpha)(2+\alpha) = 2 + \alpha + 2\alpha + \alpha^2 = 2 + 3\alpha + 2 = 4 = 1,$$
using $3 = 0$ and $\alpha^2 = 2$ in $\mathbb{F}_3$. So $2+\alpha$ is the inverse of $1+\alpha$.

**6.** Evaluate $f = x^2+1$ at the three elements: $f(0) = 1$, $f(1) = 2$, $f(2) = 4+1 = 5 \equiv 2$. No value is $0$, so $f$ has no root in $\mathbb{F}_3$ and, being of degree $2$, it is irreducible (Proposition 7.11.5 of [Rings](../02-rings/README.md)). Hence $\mathbb{F}_9 = \mathbb{F}_3[x]/(f)$ is a field with $9$ elements.

Let $\alpha$ be the class of $x$, so $\alpha^2 = -1 = 2$. Then
$$\alpha^2 = 2, \qquad \alpha^3 = 2\alpha, \qquad \alpha^4 = 2\alpha^2 = 4 = 1,$$
so $\alpha$ has order $4$, not $8$; it does not generate $\mathbb{F}_9^\times$.

Try $\beta = 1+\alpha$. Then
$$\beta^2 = 1+2\alpha+\alpha^2 = 1+2\alpha+2 = 3+2\alpha = 2\alpha, \qquad \beta^4 = (2\alpha)^2 = 4\alpha^2 = \alpha^2 = 2,$$
so $\beta^4 = 2 \ne 1$ while $\beta^8 = 2^2 = 4 = 1$. Hence $\beta$ has order $8$ and generates $\mathbb{F}_9^\times$. Its powers are
$$\beta^0 = 1, \quad \beta^1 = 1+\alpha, \quad \beta^2 = 2\alpha, \quad \beta^3 = 1+2\alpha, \quad \beta^4 = 2, \quad \beta^5 = 2+2\alpha, \quad \beta^6 = \alpha, \quad \beta^7 = 2+\alpha,$$
and $\beta^8 = 1$. (Sample check: $\beta^3 = \beta\cdot\beta^2 = (1+\alpha)2\alpha = 2\alpha+2\alpha^2 = 2\alpha+1$.)

**7.** *$\sqrt2 \notin \mathbb{Q}$.* Suppose $\sqrt2 = p/q$ with $\gcd(p,q) = 1$. Then $p^2 = 2q^2$, so $p$ is even, say $p = 2r$; then $4r^2 = 2q^2$, i.e. $q^2 = 2r^2$, so $q$ is even. This contradicts $\gcd(p,q) = 1$.

*$\sqrt[3]2 \notin \mathbb{Q}$.* Suppose $\sqrt[3]2 = p/q$ in lowest terms. Then $p^3 = 2q^3$, so $2 \mid p^3$, hence $2 \mid p$; write $p = 2r$. Then $8r^3 = 2q^3$, i.e. $q^3 = 4r^3$, so $2 \mid q^3$ and $2 \mid q$, again contradicting coprimality.

**8.** Rationalise by the conjugate:
$$(3+2\sqrt2)^{-1} = \frac{3-2\sqrt2}{9-8} = 3-2\sqrt2,$$
$$(1-\sqrt2)^{-1} = \frac{1+\sqrt2}{1-2} = -(1+\sqrt2) = -1-\sqrt2,$$
$$(2+3\sqrt2)^{-1} = \frac{2-3\sqrt2}{4-18} = \frac{2-3\sqrt2}{-14} = \frac{3\sqrt2-2}{14}.$$
Each check: $(3+2\sqrt2)(3-2\sqrt2) = 9-8 = 1$; $(1-\sqrt2)(-1-\sqrt2) = -1+2 = 1$; $(2+3\sqrt2)(3\sqrt2-2)/14 = (18-4)/14 = 1$.

**9.** By Theorem 7.5.11 the subfields of $\mathbb{F}_{p^n}$ are the $\mathbb{F}_{p^m}$ with $m \mid n$.

*$\mathbb{F}_{64} = \mathbb{F}_{2^6}$*: $m \in \{1,2,3,6\}$, giving
$$\mathbb{F}_2 \subset \mathbb{F}_4 \subset \mathbb{F}_{64}, \qquad \mathbb{F}_2 \subset \mathbb{F}_8 \subset \mathbb{F}_{64},$$
with $\mathbb{F}_4 \cap \mathbb{F}_8 = \mathbb{F}_2$ (since $\gcd(2,3) = 1$), so $\mathbb{F}_4$ and $\mathbb{F}_8$ are incomparable. There are four subfields in total.

*$\mathbb{F}_{81} = \mathbb{F}_{3^4}$*: $m \in \{1,2,4\}$, giving the chain
$$\mathbb{F}_3 \subset \mathbb{F}_9 \subset \mathbb{F}_{81}.$$
There are three subfields.

**10.** The nonzero elements are $1,2,3,4$. By Lagrange's theorem in the group $\mathbb{F}_5^\times$ of order $4$, each satisfies $a^4 = 1$; explicitly $1^4 = 1$, $2^4 = 16 \equiv 1$, $3^4 = 81 \equiv 1$, $4^4 = 256 \equiv 1$. Hence $a^5 = a$ for every $a \in \mathbb{F}_5$, including $a = 0$.

So all five elements of $\mathbb{F}_5$ are roots of $x^5-x$, a monic polynomial of degree $5$. A polynomial of degree $5$ has at most five roots, so these are all of them, and
$$x^5-x = \prod_{a \in \mathbb{F}_5}(x-a) = x(x-1)(x-2)(x-3)(x-4)$$
in $\mathbb{F}_5[x]$. Expanding is not necessary; equality of monic polynomials with the same five distinct roots is enough.

**11.** *$\sqrt5$.* It is the hypotenuse of a right triangle with legs $1$ and $2$, since $1^2+2^2 = 5$; both legs are constructible, so $\sqrt5$ is. Its minimal polynomial is $x^2-5$, so $[\mathbb{Q}(\sqrt5):\mathbb{Q}] = 2 = 2^1$.

*$\sqrt[4]{2}$.* It is $\sqrt{\sqrt2}$: construct $\sqrt2$ as the diagonal of the unit square, then apply the square-root construction of Exercise 22 to the segment of length $\sqrt2$. Its minimal polynomial is $x^4-2$ (Eisenstein at $2$), so the degree is $4 = 2^2$, consistent with Theorem 7.7.3. The actual construction shows constructibility directly; the degree only confirms that no obstruction exists.

**12.** Since $\pi$ is transcendental, the evaluation map $\mathrm{ev}_\pi : \mathbb{Q}[x] \to \mathbb{R}$, $f \mapsto f(\pi)$, has trivial kernel, so $\mathbb{Q}[\pi] \cong \mathbb{Q}[x]$. By Corollary 7.3.6, passing to fraction fields gives $\mathbb{Q}(\pi) \cong \mathbb{Q}(x)$.

For $\pi^2$: suppose $\pi^2$ were algebraic, so $f(\pi^2) = 0$ for some nonzero $f \in \mathbb{Q}[x]$. Then $g(x) := f(x^2)$ is a nonzero polynomial in $\mathbb{Q}[x]$ (its leading term is that of $f$ composed with $x^2$) and $g(\pi) = f(\pi^2) = 0$, contradicting the transcendence of $\pi$. Hence $\pi^2$ is transcendental.

## Intermediate

**13.** *$\operatorname{Frac}(\mathbb{Z}[i]) = \mathbb{Q}(i)$.* Every element of $\mathbb{Q}(i)$ is a quotient of Gaussian integers, so $\mathbb{Q}(i) \subseteq \operatorname{Frac}(\mathbb{Z}[i])$; conversely a quotient $(a+bi)/(c+di)$ with $c+di \ne 0$ equals
$$\frac{(a+bi)(c-di)}{c^2+d^2} \in \mathbb{Q}(i),$$
so $\operatorname{Frac}(\mathbb{Z}[i]) \subseteq \mathbb{Q}(i)$.

*$\operatorname{Frac}(\mathbb{Z}[\sqrt2]) = \mathbb{Q}(\sqrt2)$.* The same computation:
$$\frac{a+b\sqrt2}{c+d\sqrt2} = \frac{(a+b\sqrt2)(c-d\sqrt2)}{c^2-2d^2} \in \mathbb{Q}(\sqrt2),$$
with $c^2-2d^2 \ne 0$ because $\sqrt2 \notin \mathbb{Q}$.

*$\operatorname{Frac}(F[x]) = F(x)$.* By definition $F(x)$ is the field of fractions of $F[x]$, and by Theorem 7.1.2 applied to the inclusion $F[x] \hookrightarrow F(x)$ there is an injective map $\operatorname{Frac}(F[x]) \to F(x)$ fixing $F[x]$; it is surjective because every element of $F(x)$ is by definition a quotient of polynomials.

**14.** Let $\iota : D \hookrightarrow K$ be the inclusion. It is an injective ring homomorphism into a field, so Theorem 7.1.2 produces the unique homomorphism $\tilde\iota : \operatorname{Frac}(D) \to K$ with $\tilde\iota(a/1) = a$. Being a field homomorphism, $\tilde\iota$ is injective (Proposition 5.1.3).

*Smallest field.* If $K$ is any field containing $D$, the injection above identifies $\operatorname{Frac}(D)$ with a subfield of $K$ containing $D$. So $\operatorname{Frac}(D)$ embeds in every field containing $D$, which is exactly the statement that it is the smallest one up to isomorphism.

*Idempotence.* $\operatorname{Frac}(D)$ is a field, and the field of fractions of a field $K$ is $K$ itself: every fraction $a/b$ with $a, b \in K$, $b \ne 0$ already lies in $K$, and the construction adds nothing new.

**15.** The degree is $4$ by Example 9.2. By the tower law any intermediate field $K$ has $[K:\mathbb{Q}] \in \{1,2,4\}$.

*The list.* Example 7.8.5 shows that $E = \mathbb{Q}(\sqrt2,\sqrt3)$ is Galois over $\mathbb{Q}$ with group $G = \{\mathrm{id},\sigma,\tau,\sigma\tau\} \cong V_4$. The subgroups of $V_4$ are $\{\mathrm{id}\}$, the whole group, and the three subgroups of order $2$; by the fundamental theorem (Theorem 7.8.6) the intermediate fields are the corresponding fixed fields:
$$E^{\{\mathrm{id}\}} = E, \quad E^{\langle\sigma\rangle} = \mathbb{Q}(\sqrt3), \quad E^{\langle\tau\rangle} = \mathbb{Q}(\sqrt2), \quad E^{\langle\sigma\tau\rangle} = \mathbb{Q}(\sqrt6), \quad E^{G} = \mathbb{Q}.$$
There are five intermediate fields in total, so the list is complete.

*Direct check that $\mathbb{Q}(\sqrt6) \subseteq E$.* $\sqrt6 = \sqrt2\sqrt3 \in E$, and $\sqrt6 \notin \mathbb{Q}(\sqrt2) \cup \mathbb{Q}(\sqrt3)$, so $\mathbb{Q}(\sqrt6)$ is a third quadratic subfield distinct from the other two. Since $V_4$ has exactly three subgroups of order $2$, there cannot be a fourth quadratic subfield.

**16.** Since $\alpha \notin F$, $[F(\alpha):F] > 1$. By the tower law $[F(\alpha):F]$ divides $[E:F] = p$, so $[F(\alpha):F] = p$ and therefore $[E:F(\alpha)] = 1$, i.e. $E = F(\alpha)$.

If $F \subseteq K \subseteq E$, then $[K:F]$ divides $p$, so $[K:F] \in \{1,p\}$; in the first case $K = F$, in the second $[E:K] = 1$ and $K = E$. Hence there are no intermediate fields.

**17.** ($\Rightarrow$) If $\alpha$ is algebraic with minimal polynomial $m$ of degree $n$, then Theorem 7.3.4 gives $F[\alpha] \cong F[x]/(m)$, which is a field because $(m)$ is maximal; hence $F[\alpha] = F(\alpha)$, and $[F(\alpha):F] = n = \deg m$.

($\Leftarrow$) Suppose $F[\alpha] = F(\alpha)$. If $\alpha = 0$ there is nothing to prove. Otherwise $\alpha^{-1} \in F(\alpha) = F[\alpha]$, so $\alpha^{-1} = g(\alpha)$ for some $g \in F[x]$. Then
$$\alpha\,g(\alpha) - 1 = 0,$$
so $\alpha$ is a root of the nonzero polynomial $xg(x)-1 \in F[x]$: $\alpha$ is algebraic. (The polynomial is nonzero because its leading term is that of $g$ times $x$, unless $g = 0$, which is impossible since $\alpha^{-1} \ne 0$.)

**18.** Let $m \in F[x]$ be the minimal polynomial of $\beta$ over $F$. Then $m \in F(\alpha)[x]$, so $\beta$ is algebraic over the larger field $F(\alpha)$, and its minimal polynomial over $F(\alpha)$ divides $m$ (Theorem 7.3.3(3) applied over $F(\alpha)$). Hence
$$[F(\alpha,\beta):F(\alpha)] = \deg m_{\beta,F(\alpha)} \le \deg m = [F(\beta):F].$$
By the tower law,
$$[F(\alpha,\beta):F] = [F(\alpha,\beta):F(\alpha)]\,[F(\alpha):F] \le [F(\beta):F]\,[F(\alpha):F].$$
A finite extension is algebraic (Proposition 7.2.5), so $F(\alpha,\beta)/F$ is algebraic; in particular $\alpha$ and $\beta$ are algebraic over $F$, which is what we assumed, and every element of $F(\alpha,\beta)$ is algebraic over $F$.

**19.** *In $\mathbb{F}_8$.* Here $\alpha^3 = \alpha+1$ and $\alpha^7 = 1$. Note
$$\alpha^2+\alpha = \alpha(\alpha+1) = \alpha\cdot\alpha^3 = \alpha^4.$$
Hence $(\alpha^2+\alpha)^{-1} = \alpha^{-4} = \alpha^{7-4} = \alpha^3 = \alpha+1$. Check: $\alpha^4(\alpha+1) = \alpha^5+\alpha^4 = (\alpha^2+\alpha+1)+(\alpha^2+\alpha) = 1$.

*In $\mathbb{F}_9$.* Here $\alpha^2 = 2$ and $1+\alpha = \beta$ has order $8$ (Exercise 6). Since $\beta^8 = 1$ and $\beta^7 = 2+\alpha$,
$$(1+\alpha)^{-1} = \beta^7 = 2+\alpha.$$
Check against Exercise 5: $(1+\alpha)(2+\alpha) = 1$.

**20.** For $a \ne 0$, $a$ lies in the multiplicative group $F^\times$ of order $q-1$, so Lagrange's theorem gives $a^{q-1} = 1$, i.e. $a^q = a$. For $a = 0$, $0^q = 0$. Thus every element of $F$ is a root of $x^q-x$.

That polynomial has degree $q$, so by Lemma 7.5.2 it has at most $q$ roots; since $F$ has exactly $q$ elements, its roots are precisely the elements of $F$ and
$$x^q - x = \prod_{a \in F}(x-a).$$
Both sides are monic of degree $q$ with the same $q$ distinct roots, so they are equal.

**21.** The fixed points of $\sigma(y) = y^p$ are the roots in $\mathbb{F}_{p^n}$ of $x^p-x$. That polynomial has degree $p$, hence at most $p$ roots (Lemma 7.5.2), and every element of $\mathbb{F}_p$ is a root (Fermat's little theorem inside the prime field). Therefore the fixed field is exactly $\mathbb{F}_p$, as stated in Corollary 7.5.5.

Now let $\alpha$ be a root of an irreducible $f \in \mathbb{F}_p[x]$ of degree $d$. Then $K = \mathbb{F}_p(\alpha) \cong \mathbb{F}_p[x]/(f)$ has $p^d$ elements (Theorem 7.3.4 and Theorem 7.5.1), so by Exercise 20 applied to $K$,
$$\alpha^{p^d} = \alpha.$$
Equivalently, $f \mid x^{p^d}-x$, which is one direction of Lemma 7.5.7.

**22.** *Construction of $\sqrt x$.* On a line mark $A = (0,0)$, $C = (1,0)$ and $B = (x+1,0)$, all constructible since $x$ is. Draw the circle with diameter $AB$; its centre $((x+1)/2,0)$ and radius $(x+1)/2$ are constructible. Erect the perpendicular to the line at $C$ and let $D$ be its intersection with the circle. Then $\angle ADB = 90^\circ$ (angle in a semicircle), so in the right triangle $ADB$ the segment $CD$ is the altitude to the hypotenuse, and the altitude theorem gives
$$CD^2 = AC\cdot CB = 1\cdot x = x, \qquad\text{so } CD = \sqrt x.$$
All steps use only straightedge and compass, so $\sqrt x$ is constructible. (Equivalently, by the intersecting chords theorem applied to the chord through $C$ perpendicular to $AB$.)

*Towers.* Suppose the real elements of $K_i$ are constructible and $K_{i+1} = K_i(\sqrt d)$ with $d \in K_i$, $d > 0$. Every element of $K_{i+1}$ is $a+b\sqrt d$ with $a, b, d \in K_i$ constructible; sums, differences, products and quotients of constructible lengths are constructible by the classical similar-triangle constructions (intercept theorem), and $\sqrt d$ is constructible by the construction above. Hence the real elements of $K_{i+1}$ are constructible, and induction gives the claim for $K_n$.

## Advanced

**23.** By Theorem 7.5.3, $F^\times = \langle g\rangle$ is cyclic of order $q-1$. Every element is $g^k$ for a unique $k \in \{0,1,\dots,q-2\}$, and
$$\operatorname{ord}(g^k) = \frac{q-1}{\gcd(k,\,q-1)}.$$
So $\operatorname{ord}(g^k) = d$ iff $\gcd(k,q-1) = (q-1)/d$. Writing $k = \frac{q-1}{d}j$ with $0 \le j < d$, this condition becomes $\gcd(j,d) = 1$. Hence the number of elements of order $d$ is the number of $j \in \{0,\dots,d-1\}$ coprime to $d$, namely $\varphi(d)$.

Every element of $F^\times$ has some order dividing $q-1$ (Lagrange), so the sets "elements of order $d$" for $d \mid q-1$ partition $F^\times$. Counting gives
$$\sum_{d \mid q-1}\varphi(d) = q-1.$$
For example, in $\mathbb{F}_9^\times$ (cyclic of order $8$) the counts are $\varphi(1)=1$, $\varphi(2)=1$, $\varphi(4)=2$, $\varphi(8)=4$, and $1+1+2+4 = 8$.

**24.** By Theorem 7.5.6, $p^n = \sum_{d \mid n} d\,N_d$ where $N_d$ is the number of monic irreducibles of degree $d$ over $\mathbb{F}_p$.

*Degree $5$ over $\mathbb{F}_2$.* The divisors of $5$ are $1$ and $5$, and $N_1 = 2$ ($x$ and $x+1$). So
$$32 = 1\cdot N_1 + 5\cdot N_5 = 2 + 5N_5, \qquad N_5 = 6.$$

*Degree $2$ over $\mathbb{F}_3$.* The divisors of $2$ are $1$ and $2$, and $N_1 = 3$ ($x, x-1, x-2$). So
$$9 = N_1 + 2N_2 = 3 + 2N_2, \qquad N_2 = 3.$$

*Listing.* The monic quadratics over $\mathbb{F}_3$ without roots are
$$x^2+1 \ (\text{values } 1,2,2), \qquad x^2+x+2 \ (\text{values } 2,1,2), \qquad x^2+2x+2 \ (\text{values } 2,2,1),$$
where the values are at $x = 0,1,2$. There are exactly three, matching the count.

**25.** Write $L = \mathbb{F}_3[y]/(y^2+2y+2)$, where $y^2 = -2y-2 = y+1$ (using $-2 \equiv 1$). The polynomial $X^2+2X+2$ is irreducible over $\mathbb{F}_3$ because its discriminant is $4-8 = -4 \equiv 2$, and $2$ is not a square modulo $3$; so $L$ is a field with $9$ elements.

*A root of $X^2+1$ in $L$.* Compute
$$(1+y)^2 = 1+2y+y^2 = 1+2y+(y+1) = 2+3y = 2 = -1.$$
So $1+y$ is a root of $X^2+1$.

*The map.* Define $\varphi : \mathbb{F}_3[x] \to L$ by $\varphi(x) = 1+y$ (and $\varphi(a) = a$ for constants). It is a unital ring homomorphism (substitution), and $\varphi(x^2+1) = (1+y)^2+1 = 2+1 = 0$, so $(x^2+1) \subseteq \ker\varphi$. Since $x^2+1$ is irreducible, $(x^2+1)$ is maximal and, because $\varphi \ne 0$, the kernel equals $(x^2+1)$. Hence $\varphi$ induces a well-defined injective homomorphism
$$\bar\varphi : \mathbb{F}_3[x]/(x^2+1) \longrightarrow L, \qquad \bar\varphi(x+(x^2+1)) = 1+y.$$
Both fields have $9$ elements, so $\bar\varphi$ is bijective: an explicit isomorphism.

**26.** Since $\beta$ is algebraic over $F$, $m = [F(\beta):F] < \infty$ (Corollary 7.3.5). Over the larger field $F(\beta)$, $\alpha$ has a minimal polynomial of degree $n = [F(\beta)(\alpha):F(\beta)] < \infty$. Then
$$[F(\alpha,\beta):F] = [F(\beta)(\alpha):F] = n\,m < \infty.$$
A finite extension is algebraic (Proposition 7.2.5), so every element of $F(\alpha,\beta)$, in particular $\alpha$, is algebraic over $F$.

For the bound: the minimal polynomial of $\beta$ over $F$ lies in $F(\alpha)[x]$, so $\beta$ is algebraic over $F(\alpha)$ with minimal polynomial dividing $m$, whence $[F(\alpha,\beta):F(\alpha)] \le m$. Therefore
$$[F(\alpha,\beta):F] = [F(\alpha,\beta):F(\alpha)]\,[F(\alpha):F] \le m\,n' = [F(\beta):F]\,[F(\alpha):F],$$
where $n' = [F(\alpha):F]$.

**27.** Let $x \in \mathbb{R}$ with $[\mathbb{Q}(x):\mathbb{Q}] = 2$. Then $x$ satisfies an irreducible quadratic $ax^2+bx+c$ with $a \ne 0$, $a,b,c \in \mathbb{Q}$ (a multiple of its minimal polynomial). By the quadratic formula,
$$x = \frac{-b \pm \sqrt{b^2-4ac}}{2a}.$$
Since $x$ is real, $D := b^2-4ac \ge 0$; and $D \ne 0$ because an irreducible quadratic has no rational root. So $D > 0$ and $x \in \mathbb{Q}(\sqrt D)$.

Now $D = p/q$ with $p, q > 0$. Construct a segment of length $p/q$ (integers by stepping, quotients by the similar-triangle construction), then construct its square root by the semicircle construction of Exercise 22. Hence $\sqrt D$ is constructible, and so is $x$, being a rational expression in constructible numbers (Exercise 33).

*Conclusion.* Every real number of degree $2$ over $\mathbb{Q}$ is constructible; combined with Theorem 7.7.3, over the reals the necessary condition "degree a power of $2$" is also sufficient in degree $\le 2$. It fails in general in degree $4$: a root of an irreducible quartic with Galois group $S_4$ has degree $4$ but is not constructible.

**28.** By Definition 7.8.4 and Theorem 7.8.3, $\lvert G\rvert = \lvert\operatorname{Gal}(E/F)\rvert = [E:F] = 4$. A group of order $4$ is either cyclic or a product of two groups of order $2$: if some element has order $4$ the group is $\mathbb{Z}/4\mathbb{Z}$; otherwise every nonidentity element has order $2$, and then $G$ is abelian because for all $a, b$
$$ab = (ab)^{-1} = b^{-1}a^{-1} = ba,$$
so $G \cong \mathbb{Z}/2\mathbb{Z}\times\mathbb{Z}/2\mathbb{Z}$.

*Cyclic example.* $E = \mathbb{Q}(\zeta_5)$, $F = \mathbb{Q}$. $\Phi_5 = x^4+x^3+x^2+x+1$ is irreducible over $\mathbb{Q}$ (Rings Exercise 28), so $[E:\mathbb{Q}] = 4$; $E$ is the splitting field of $x^5-1$, hence Galois. For each $k \in (\mathbb{Z}/5\mathbb{Z})^\times$ there is an automorphism $\sigma_k(\zeta_5) = \zeta_5^k$, and $k \mapsto \sigma_k$ is an isomorphism $\operatorname{Gal}(E/\mathbb{Q}) \cong (\mathbb{Z}/5\mathbb{Z})^\times \cong \mathbb{Z}/4\mathbb{Z}$.

*Non-cyclic example.* $E = \mathbb{Q}(\sqrt2,\sqrt3)$, $F = \mathbb{Q}$: Example 7.8.5 gives $[E:\mathbb{Q}] = 4$ and $\operatorname{Gal}(E/\mathbb{Q}) \cong V_4$.

**29.** *Order.* Every $y \in \mathbb{F}_{p^n}$ satisfies $y^{p^n} = y$ (Exercise 20), so $\sigma^n = \mathrm{id}$. If $\sigma^k = \mathrm{id}$ for some $k \ge 1$, then every $y \in \mathbb{F}_{p^n}$ is a root of $x^{p^k}-x$; that polynomial has degree $p^k$, so $p^n \le p^k$ and $n \le k$. Hence $n$ is the least positive exponent giving the identity, i.e. $\sigma$ has order $n$.

*Fixed field of $\sigma^k$.* The fixed points are
$$\{y \in \mathbb{F}_{p^n} : y^{p^k} = y\} = \mathbb{F}_{p^n}\cap \mathbb{F}_{p^k},$$
the intersection computed inside a field containing both, say $\mathbb{F}_{p^{nk}}$. By Theorem 7.5.11 the subfields of $\mathbb{F}_{p^{nk}}$ form the set $\{\mathbb{F}_{p^d} : d \mid nk\}$ ordered by divisibility, so the intersection is $\mathbb{F}_{p^{\gcd(n,k)}}$. Hence the fixed field of $\sigma^k$ is $\mathbb{F}_{p^{\gcd(k,n)}}$, a field of size $p^{\gcd(k,n)}$.

**30.** $\omega = \zeta_3$ satisfies $\omega^2+\omega+1 = 0$ (it is a primitive cube root of unity), and the roots of $x^2+x+1$ are $\omega$ and $\omega^2$, both non-real.

*Irreducibility over $\mathbb{Q}(\alpha)$.* We have $\mathbb{Q}(\alpha) \subseteq \mathbb{R}$ since $\alpha = \sqrt[3]2$ is real. If $x^2+x+1$ were reducible over $\mathbb{Q}(\alpha)$ it would have a root there, i.e. $\omega \in \mathbb{Q}(\alpha) \subseteq \mathbb{R}$, which is false. Hence it is irreducible over $\mathbb{Q}(\alpha)$ and is the minimal polynomial of $\omega$ over that field.

*Degree.* $[\mathbb{Q}(\alpha):\mathbb{Q}] = 3$ (Example 9.2) and $[\mathbb{Q}(\alpha,\omega):\mathbb{Q}(\alpha)] = 2$, so the tower law gives
$$[\mathbb{Q}(\alpha,\omega):\mathbb{Q}] = 3\cdot2 = 6.$$
An independent check: $\mathbb{Q}(\alpha,\omega)$ is the splitting field of $x^3-2$, whose six automorphisms were computed in Example 9.7.

**31.** Let $\sigma : F \to K$ be a field isomorphism. Then $\sigma(1_F) = 1_K$, so $\sigma(n\cdot 1_F) = n\cdot 1_K$ for every $n \in \mathbb{Z}$, and for $n \ne 0$,
$$\sigma\left(\frac{m}{n}\right) = \sigma(m\cdot 1)\cdot\sigma(n\cdot1)^{-1} = \frac{m}{n}.$$
Hence $\sigma$ fixes the prime subfield pointwise (identified with $\mathbb{Q}$ or $\mathbb{F}_p$ inside each field).

Now suppose $\sigma : \mathbb{Q}(\sqrt2) \to \mathbb{Q}(\sqrt3)$ were a field isomorphism. Then $\sigma$ fixes $\mathbb{Q}$, so
$$\sigma(\sqrt2)^2 = \sigma(2) = 2,$$
hence $\sigma(\sqrt2) = \pm\sqrt2$. But $\sigma(\sqrt2) \in \mathbb{Q}(\sqrt3)$, so $\pm\sqrt2 \in \mathbb{Q}(\sqrt3)$. Write $\sqrt2 = a+b\sqrt3$ with $a, b \in \mathbb{Q}$; squaring,
$$2 = a^2+3b^2+2ab\sqrt3,$$
and since $\sqrt3 \notin \mathbb{Q}$ we get $ab = 0$. If $b = 0$ then $\sqrt2 \in \mathbb{Q}$, false; if $a = 0$ then $2 = 3b^2$, which has no rational solution. Contradiction. Hence no such isomorphism exists: $\mathbb{Q}(\sqrt2) \not\cong \mathbb{Q}(\sqrt3)$.

## Challenge

**32.** Let $\alpha$ be a root of $f$ in $K = \mathbb{F}_p[x]/(f)$, a field with $p^n$ elements, and identify $K = \mathbb{F}_{p^n}$ (Theorem 7.5.9). Then $K = \mathbb{F}_p(\alpha)$.

*The conjugates are roots.* Since $f$ has coefficients in $\mathbb{F}_p$, applying the Frobenius automorphism gives
$$f(\alpha^p) = f(\alpha)^p = 0,$$
and iterating, $f(\alpha^{p^i}) = 0$ for all $i \ge 0$. Each $\alpha^{p^i}$ lies in $K$, because Frobenius is an automorphism of $K$ (Theorem 7.5.4). Hence $\alpha, \alpha^p, \dots, \alpha^{p^{n-1}} \in K$ are roots of $f$.

*They are distinct.* If $\alpha^{p^i} = \alpha^{p^j}$ with $0 \le i < j \le n-1$, then $\alpha$ is a root of $x^{p^{j-i}}-x$, so $f \mid x^{p^{j-i}}-x$ (Theorem 7.3.3(3)), and Lemma 7.5.7 gives $n = \deg f \mid (j-i)$. But $0 < j-i < n$, contradiction.

So $f$ has at least $n = \deg f$ distinct roots in $K$, hence exactly $n$ and no others: $f$ splits in $K$ as $f = \prod_i (x-\alpha^{p^i})$. Since $K = \mathbb{F}_p(\alpha)$ is generated over $\mathbb{F}_p$ by a root of $f$, $K$ is a splitting field of $f$ over $\mathbb{F}_p$.

*Normality.* Let $L/F$ be a finite extension of finite fields, say $F = \mathbb{F}_q$ with $q = p^m$, and let $g \in F[x]$ be irreducible with a root $\beta \in L$. Then $F(\beta) \cong F[x]/(g)$ is a field with $q^d$ elements, $d = \deg g$, and $\beta \in L$ gives $F(\beta) \subseteq L$. The same argument as above, with $p$ replaced by $q$, shows that the elements $\beta, \beta^q, \dots, \beta^{q^{d-1}}$ are $d$ distinct roots of $g$ and all lie in $F(\beta) \subseteq L$. Hence $g$ splits in $L$: every irreducible over $F$ with a root in $L$ splits in $L$, i.e. $L/F$ is normal.

**33.** *The field structure.* Write $\mathcal{C}$ for the set of constructible real numbers. It contains $0$ and $1$, hence all integers (add $1$ repeatedly) and all rationals: $1/n$ is constructed by dividing a segment into $n$ equal parts with the intercept theorem, and $m/n$ is then a product.

*Sums and differences.* Given segments of lengths $a$ and $b$ on a line, copy the segment of length $b$ onto the ray from the endpoint of the segment of length $a$ (transferring a length with the compass); this produces $a+b$, and transferring in the other direction produces $|a-b|$ (reflection gives negatives).

*Products and quotients.* Use the intercept theorem. Draw an angle with vertex $O$, mark $A$ on one arm with $OA = a$ and $C$ on the same arm with $OC = 1$, and mark $B$ on the other arm with $OB = b$. Draw the line $CB$, and through $A$ draw the parallel to $CB$, meeting the second arm at $D$. Then the triangles $OCB$ and $OAD$ are similar, so
$$\frac{OD}{OB} = \frac{OA}{OC} = \frac{a}{1}, \qquad OD = ab.$$
Swapping the roles of $A$ and $C$ gives $OD = a/b$ (for $b \ne 0$). All auxiliary lines and parallels are constructible, so $ab$ and $a/b$ are constructible.

*Square roots.* For $x > 0$, the semicircle construction of Exercise 22 produces a segment of length $\sqrt x$.

Hence $\mathcal{C}$ is a subfield of $\mathbb{R}$ containing $\mathbb{Q}$ and closed under $x \mapsto \sqrt x$ for $x > 0$. Consequently every element of a tower $\mathbb{Q} = K_0 \subseteq K_1 \subseteq \cdots \subseteq K_n$ of quadratic extensions lies in $\mathcal{C}$, and Theorem 7.7.3 says that, conversely, every constructible number lies in such a tower. So the constructible numbers are exactly $\bigcup K_n$ over all finite towers of quadratic extensions of $\mathbb{Q}$ inside $\mathbb{R}$.

**34.** *Galois and group.* $\Phi_5 = x^4+x^3+x^2+x+1$ is irreducible over $\mathbb{Q}$ (Eisenstein applied to $\Phi_5(x+1)$ at $p = 5$), so $[\mathbb{Q}(\zeta_5):\mathbb{Q}] = 4$. The field $\mathbb{Q}(\zeta_5)$ is the splitting field of $x^5-1$ over $\mathbb{Q}$, since every root is a power of $\zeta_5$; hence it is Galois, and $\lvert G\rvert = 4$ with $G = \operatorname{Gal}(\mathbb{Q}(\zeta_5)/\mathbb{Q})$.

Every $\mathbb{Q}$-automorphism sends $\zeta_5$ to another root of $\Phi_5$, i.e. to $\zeta_5^k$ with $k \in \{1,2,3,4\}$, and conversely each such assignment defines an automorphism (Theorem 7.4.2). Composition corresponds to multiplication of exponents, so
$$G \cong (\mathbb{Z}/5\mathbb{Z})^\times \cong \mathbb{Z}/4\mathbb{Z},$$
the last isomorphism because $2$ has order $4$ modulo $5$ ($2, 4, 3, 1$). So $G = \langle\sigma\rangle$ with $\sigma(\zeta_5) = \zeta_5^2$.

*Subgroups.* $\mathbb{Z}/4\mathbb{Z}$ has exactly three subgroups: $\{0\}$, $\langle 2\rangle \cong \mathbb{Z}/2\mathbb{Z}$ (the unique subgroup of order $2$) and the whole group. By the fundamental theorem (Theorem 7.8.6) there are exactly three intermediate fields: $E$, the fixed field $K = E^{\langle\sigma^2\rangle}$ of index-2 subgroup, and $\mathbb{Q}$.

*The intermediate field is $\mathbb{Q}(\sqrt5)$.* Let $c = \zeta_5+\zeta_5^{-1} = 2\cos72^\circ$. From Example 9.8, $c = (\sqrt5-1)/2$, so
$$\sqrt5 = 2c+1 = 2(\zeta_5+\zeta_5^{-1})+1 \in \mathbb{Q}(\zeta_5).$$
Thus $\mathbb{Q}(\sqrt5) \subseteq \mathbb{Q}(\zeta_5)$, and $[\mathbb{Q}(\sqrt5):\mathbb{Q}] = 2$ because $x^2-5$ is irreducible. Since $K$ is the only intermediate field of degree $2$, necessarily $K = \mathbb{Q}(\sqrt5)$: it is the unique quadratic subfield of $\mathbb{Q}(\zeta_5)$. (Consistently, $\langle\sigma^2\rangle$ is normal in $G$ because $G$ is abelian, so $K/\mathbb{Q}$ is Galois, as a quadratic extension must be.)

**35.** *Equality of the fields.* Since
$$\frac{\sqrt2}{\sqrt[3]2} = 2^{1/2-1/3} = 2^{1/6},$$
we have $2^{1/6} \in \mathbb{Q}(\sqrt2,\sqrt[3]2)$. Conversely
$$(2^{1/6})^2 = 2^{1/3} = \sqrt[3]2, \qquad (2^{1/6})^3 = 2^{1/2} = \sqrt2,$$
so $\mathbb{Q}(\sqrt2,\sqrt[3]2) \subseteq \mathbb{Q}(2^{1/6})$. Hence the two fields are equal.

*Degree.* By Exercise 4, $[\mathbb{Q}(\sqrt2,\sqrt[3]2):\mathbb{Q}] = 6$, so $[\mathbb{Q}(2^{1/6}):\mathbb{Q}] = 6$.

*Minimal polynomial.* The polynomial $x^6-2$ is Eisenstein at $2$, hence irreducible over $\mathbb{Q}$, and it vanishes at $2^{1/6}$. So
$$m_{2^{1/6}} = x^6-2,$$
of degree $6$, matching the degree computed above. (Note $x^6-2 = (x^3-\sqrt2)(x^3+\sqrt2)$ over $\mathbb{Q}(\sqrt2)$: the polynomial factors over the subfield, as it must, since the degree over $\mathbb{Q}(\sqrt2)$ is $3$.)

**36.** Let $\alpha = 2^{1/4}$ and $E = \mathbb{Q}(\alpha, i)$, the field generated by all roots $\pm\alpha, \pm i\alpha$ of $x^4-2$.

*Degree.* $x^4-2$ is Eisenstein at $2$, hence irreducible, so $[\mathbb{Q}(\alpha):\mathbb{Q}] = 4$. Since $\mathbb{Q}(\alpha) \subseteq \mathbb{R}$ and $i \notin \mathbb{R}$, $x^2+1$ is irreducible over $\mathbb{Q}(\alpha)$, so
$$[E:\mathbb{Q}] = [E:\mathbb{Q}(\alpha)]\,[\mathbb{Q}(\alpha):\mathbb{Q}] = 2\cdot4 = 8.$$
$E$ is the splitting field of $x^4-2$, whose roots are distinct in characteristic $0$, so $E/\mathbb{Q}$ is Galois and $\lvert\operatorname{Gal}(E/\mathbb{Q})\rvert = 8$.

*Two automorphisms.* Define $\sigma$ by $\sigma(\alpha) = i\alpha$ and $\sigma(i) = i$, and $\tau$ by $\tau(\alpha) = \alpha$ and $\tau(i) = -i$. Both are well defined because the images are roots of the respective minimal polynomials ($(i\alpha)^4 = i^4\alpha^4 = 2$, and $\pm i$ are the roots of $x^2+1$), and they extend to automorphisms of $E$ since $E = \mathbb{Q}(\alpha,i)$.

*Orders.* $\sigma(\alpha) = i\alpha$, $\sigma^2(\alpha) = i^2\alpha = -\alpha \ne \alpha$, so $\sigma$ has order $4$ (and $\sigma^4 = \mathrm{id}$ since $\sigma^4(\alpha) = i^4\alpha = \alpha$ and $\sigma^4(i) = i$). Also $\tau \ne \mathrm{id}$ and $\tau^2 = \mathrm{id}$, so $\tau$ has order $2$.

*The dihedral relation.* Compute on the generator $\alpha$:
$$\tau\sigma\tau^{-1}(\alpha) = \tau\sigma(\alpha) = \tau(i\alpha) = \tau(i)\tau(\alpha) = -i\alpha = \sigma^{-1}(\alpha),$$
and on $i$ both sides equal $i$. Since $E$ is generated by $\alpha$ and $i$, $\tau\sigma\tau^{-1} = \sigma^{-1}$.

Therefore $\langle\sigma,\tau\rangle$ is a dihedral group of order $2\cdot4 = 8$; it is a subgroup of $\operatorname{Gal}(E/\mathbb{Q})$ of order $8$, hence by $\lvert\operatorname{Gal}(E/\mathbb{Q})\rvert = 8$ the whole group:
$$\operatorname{Gal}(E/\mathbb{Q}) = \langle\sigma,\tau \mid \sigma^4 = \tau^2 = \mathrm{id},\ \tau\sigma\tau^{-1} = \sigma^{-1}\rangle \cong D_4.$$
