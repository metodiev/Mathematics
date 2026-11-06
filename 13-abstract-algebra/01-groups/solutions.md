# Groups — Solutions

> [Groups](README.md) · Solutions to [exercises.md](exercises.md) · 38 problems

Each solution states the strategy, then carries out every step. Section references point into [README.md](README.md).

## Beginner

### 1.

(a) **Group.** Addition is associative on $\mathbb{Z}$, $0$ is the identity, and $-a$ is the inverse of $a$. It is abelian.

(b) **Not a group.** The operation is associative with identity $1$, but $2$ has no inverse: $2b = 1$ has no solution in $\mathbb{Z}$. Axiom (G3) fails.

(c) **Group.** The product of two nonzero rationals is nonzero, $1$ is the identity, and $1/a$ is defined for $a \ne 0$. It is abelian.

(d) **Group.** The set $\{1,-1,i,-i\}$ equals $\{i^0,i^1,i^2,i^3\}$; products of powers of $i$ are powers of $i$, the identity is $1 = i^0$, and the inverse of $i^k$ is $i^{4-k}$. This is the cyclic group of order $4$.

(e) **Not a group.** Subtraction is not associative: $(5-3)-1 = 1$ but $5-(3-1) = 3$. It also has no identity: $a - e = a$ forces $e = 0$, but then $e - a = -a \ne a$ for $a \ne 0$.

(f) **Not a group.** Matrix multiplication is associative and $I$ is an identity, but a singular matrix has no inverse. (G3) fails.

(g) **Group.** A product of positive reals is positive, $1$ is the identity, and $1/a > 0$ for $a > 0$. Associativity is inherited from $\mathbb{R}$. It is abelian.

### 2.

**Closure.** If $a,b \ne -1$ then
$$1 + (a \ast b) = 1 + a + b + ab = (1+a)(1+b) \ne 0,$$
so $a \ast b \ne -1$ and the operation is defined.

**Associativity.** Expanding both bracketings,
$$(a\ast b)\ast c = (a+b+ab) + c + (a+b+ab)c = a+b+c+ab+ac+bc+abc,$$
and the same expression arises from $a \ast (b \ast c)$; the operation is commutative in form, so the two agree.

**Identity.** $a \ast 0 = a + 0 + 0 = a$ and $0 \ast a = a$, so $e = 0$.

**Inverses.** Solve $a \ast b = 0$: $a + b + ab = 0 \iff b(1+a) = -a \iff b = -a/(1+a)$, which is defined because $a \ne -1$. So $a^{-1} = -\dfrac{a}{1+a}$.

**Abelian.** $a \ast b = a+b+ab$ is symmetric in $a$ and $b$.

**Isomorphism.** Put $\psi(a) = 1+a$. Then $\psi$ is a bijection $\mathbb{R}\setminus\{-1\} \to \mathbb{R}\setminus\{0\}$ (inverse $y \mapsto y-1$), and
$$\psi(a \ast b) = 1 + a + b + ab = (1+a)(1+b) = \psi(a)\psi(b).$$
So $(G,\ast) \cong (\mathbb{R}\setminus\{0\},\cdot)$, which also proves the axioms at one stroke.

### 3.

**Two factors.** $(ab)(b^{-1}a^{-1}) = a(bb^{-1})a^{-1} = aea^{-1} = e$ and $(b^{-1}a^{-1})(ab) = b^{-1}(a^{-1}a)b = e$. By uniqueness of inverses (Proposition 7.1.2), $(ab)^{-1} = b^{-1}a^{-1}$.

**Induction.** For $n = 1$ the claim is trivial. Assume it for $n$; then by the two-factor case applied to $a_1\cdots a_n$ and $a_{n+1}$,
$$(a_1\cdots a_n a_{n+1})^{-1} = a_{n+1}^{-1}(a_1\cdots a_n)^{-1} = a_{n+1}^{-1}a_n^{-1}\cdots a_1^{-1}.$$

**Computation.** With $a = (1\,2\,3)$ and $b = (4\,5)$,
$$\big((1\,2\,3)(4\,5)\big)^{-1} = (4\,5)^{-1}(1\,2\,3)^{-1} = (4\,5)(1\,3\,2).$$

### 4.

Let $a,b \in G$. By hypothesis $(ab)^2 = e$, so $ab$ is its own inverse (Proposition 7.1.5). Therefore
$$ab = (ab)^{-1} = b^{-1}a^{-1} = b\,a,$$
where the last equality uses $b^2 = e \Rightarrow b^{-1} = b$ and $a^2 = e \Rightarrow a^{-1} = a$. Hence $G$ is abelian.

### 5.

**Additive group.** In $\mathbb{Z}/12\mathbb{Z}$ the order of $\bar k$ is $12/\gcd(12,k)$ (Proposition 7.2.5):

| $\bar k$ | $\bar 0$ | $\bar 1$ | $\bar 2$ | $\bar 3$ | $\bar 4$ | $\bar 5$ | $\bar 6$ | $\bar 7$ | $\bar 8$ | $\bar 9$ | $\overline{10}$ | $\overline{11}$ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| order | $1$ | $12$ | $6$ | $4$ | $3$ | $12$ | $2$ | $12$ | $3$ | $4$ | $6$ | $12$ |

**Units.** $(\mathbb{Z}/12\mathbb{Z})^\times = \{\bar 1, \bar 5, \bar 7, \overline{11}\}$. Now $\bar 5^2 = \overline{25} = \bar 1$, $\bar 7^2 = \overline{49} = \bar 1$ and $\overline{11}^2 = \overline{121} = \bar 1$, so every non-identity element has order $2$. A group of order $4$ in which every element other than the identity has order $2$ is $V_4$: pick two distinct non-identity elements $x,y$; then $xy$ is the fourth element and $xy = (xy)^{-1} = yx$. Hence $(\mathbb{Z}/12\mathbb{Z})^\times \cong V_4$, not $\mathbb{Z}/4\mathbb{Z}$ (which has elements of order $4$).

### 6.

**First claim.** By Proposition 7.2.2, $(a^{-1})^n = (a^n)^{-1}$, and this is $e$ if and only if $a^n = e$. So $a$ and $a^{-1}$ have the same positive exponents and the same order (finite or infinite).

**Second claim.** For $n \ge 1$, $(ab)^n = a(ba)^{n-1}b$ (induction on $n$). Hence
$$(ab)^n = e \iff a(ba)^{n-1}b = e \iff (ba)^{n-1} = a^{-1}b^{-1} = (ba)^{-1} \iff (ba)^n = e.$$
The positive integers $n$ with $(ab)^n = e$ and with $(ba)^n = e$ coincide, so the orders are equal.

**Counterexample.** In $S_3$ take $a = (1\,2)$ and $b = (1\,2\,3)$. Then $ab = (2\,3)$, so $\operatorname{ord}(a) = 2$, $\operatorname{ord}(b) = 3$, $\operatorname{ord}(ab) = 2 \ne 6 = 2\cdot 3$.

### 7.

Use the subgroup criterion (Theorem 7.3.2); both sets contain $1$, so are nonempty.

**$S^1$.** If $|z| = |w| = 1$ then $|zw^{-1}| = |z|/|w| = 1$, so $zw^{-1} \in S^1$.

**$\mu_n$.** If $z^n = w^n = 1$ then $(zw^{-1})^n = z^n (w^n)^{-1} = 1$, so $zw^{-1} \in \mu_n$.

In both cases Theorem 7.3.2 gives a subgroup of $\mathbb{C}^\times$.

### 8.

By Theorem 7.4.5 the subgroups of $\mathbb{Z}/18\mathbb{Z}$ correspond to the divisors $1,2,3,6,9,18$ of $18$, and each is generated by $\overline{18/d}$ for the divisor $d$:

| Order $d$ | Generator | Elements |
|---|---|---|
| $1$ | $\overline{18} = \bar 0$ | $\{\bar 0\}$ |
| $2$ | $\bar 9$ | $\{\bar 0, \bar 9\}$ |
| $3$ | $\bar 6$ | $\{\bar 0,\bar 6,\overline{12}\}$ |
| $6$ | $\bar 3$ | $\{\bar 0,\bar 3,\bar 6,\bar 9,\overline{12},\overline{15}\}$ |
| $9$ | $\bar 2$ | $\{\bar 0,\bar 2,\bar 4,\dots,\overline{16}\}$ |
| $18$ | $\bar 1$ | all of $\mathbb{Z}/18\mathbb{Z}$ |

Inclusions: $\{\bar 0\} \subset \langle\bar 9\rangle \subset \langle\bar 3\rangle \subset \langle\bar 1\rangle$; also $\{\bar 0\} \subset \langle\bar 6\rangle \subset \langle\bar 3\rangle$ and $\langle\bar 6\rangle \subset \langle\bar 2\rangle \subset \langle\bar 1\rangle$, while $\langle\bar 9\rangle \not\subset \langle\bar 2\rangle$ and $\langle\bar 2\rangle \not\subset \langle\bar 3\rangle$. So the lattice has the shape of a hexagon with one diagonal.

### 9.

Powers of $\bar 3$ in $\mathbb{Z}/7\mathbb{Z}$: $3^1 = 3$, $3^2 = 2$, $3^3 = 6$, $3^4 = 4$, $3^5 = 5$, $3^6 = 1$. All six nonzero classes occur, so $\bar 3$ has order $6 = |(\mathbb{Z}/7\mathbb{Z})^\times|$ and the group is cyclic. The other generator is $3^5 = 5$ (exponents coprime to $6$ are $1$ and $5$).

The generators of $\mathbb{Z}/12\mathbb{Z}$ are the classes $\bar k$ with $\gcd(k,12) = 1$ (Corollary 7.4.6), namely $\bar 1, \bar 5, \bar 7, \overline{11}$: four generators, matching $\varphi(12) = 4$.

### 10.

$H = \langle\bar 4\rangle = \{\bar 0,\bar 4,\bar 8\}$. The cosets are
$$H,\quad \bar 1 + H = \{\bar 1,\bar 5,\bar 9\},\quad \bar 2 + H = \{\bar 2,\bar 6,\overline{10}\},\quad \bar 3 + H = \{\bar 3,\bar 7,\overline{11}\}.$$
Every class of $\mathbb{Z}/12\mathbb{Z}$ appears exactly once, so there are $4$ cosets and $[\mathbb{Z}/12\mathbb{Z} : H] = 4$. Lagrange: $|G| = 12 = 4 \cdot 3 = [G:H]\,|H|$, as claimed.

### 11.

Since $60 = 2^2\cdot 3\cdot 5$, the divisors of $60$ are $1,2,3,4,5,6,10,12,15,20,30,60$.

**Element orders.** By Corollary 7.5.6 the order of an element divides $60$, so it must be one of these twelve numbers. Lagrange gives no further restriction, and all twelve do occur in some group of order $60$ (for example in $\mathbb{Z}/60\mathbb{Z}$, which is cyclic and has elements of every order dividing $60$).

**Subgroup orders.** The same list is the set of *candidates*: $A_4$ shows that a divisor need not be realised, and $A_5$ of order $60$ has no subgroup of order $30$, $20$ or $15$. So Lagrange's theorem is a necessary condition only; it neither guarantees existence nor excludes any specific divisor on general grounds.

### 12.

(a) **Not normal.** Conjugate by $(1\,3)$: $(1\,3)(1\,2)(1\,3)^{-1} = (2\,3) \notin \langle(1\,2)\rangle$.

(b) **Normal.** $\langle(1\,2\,3)\rangle = A_3$ has index $2$ in $S_3$, and subgroups of index $2$ are normal (Example 7.6.3).

(c) **Normal.** $\langle r\rangle$ has index $2$ in $D_4$.

(d) **Not normal.** In $D_4$, $r s r^{-1} = (r(2)\ r(4)) = (1\,3) = r^2s \notin \langle s\rangle$.

(e) **Normal.** $\mathbb{Z}$ is abelian, so every subgroup is normal; indeed $g + 3\mathbb{Z} - g = 3\mathbb{Z}$.

## Intermediate

### 13.

Let $G$ have an associative operation, a right identity $e$ (so $ae = a$ for all $a$) and right inverses (for each $a$ there is $b$ with $ab = e$).

Fix $a$ and a right inverse $b$, so $ab = e$. First we show $ba = e$. Let $c$ be a right inverse of $ba$: $(ba)c = e$. Then, by associativity,
$$(ba)(ba) = b(ab)a = bea = ba,$$
using $ea = a$. Consequently
$$ba = (ba)e = (ba)\big((ba)c\big) = \big((ba)(ba)\big)c = (ba)c = e.$$
So every right inverse is also a left inverse.

Next, $e$ is a left identity:
$$a = ae = a(ba) = (ab)a = ea.$$
So $ea = a = ae$ and $e$ is a two-sided identity; with $ab = ba = e$, $b$ is a two-sided inverse. Hence $G$ is a group.

### 14.

Because $a$ and $b$ commute, $(ab)^k = a^k b^k$ for all $k \ge 0$ (Proposition 7.2.2).

$(ab)^{mn} = a^{mn}b^{mn} = e$, so $\operatorname{ord}(ab)$ divides $mn$.

Conversely suppose $(ab)^k = e$. Then $a^k = b^{-k}$. The left side lies in $\langle a\rangle$ and the right side in $\langle b\rangle$, so both lie in $\langle a\rangle \cap \langle b\rangle$, a subgroup whose order divides $|\langle a\rangle| = m$ and $|\langle b\rangle| = n$ by Lagrange. Since $\gcd(m,n) = 1$, its order is $1$, so $a^k = b^{-k} = e$. Hence $m \mid k$ and $n \mid k$, and coprimality gives $mn \mid k$.

Therefore $mn$ is the least positive exponent killing $ab$: $\operatorname{ord}(ab) = mn$.

### 15.

($\Rightarrow$) Suppose $HK \le G$. Let $h \in H$, $k \in K$. Then $hk \in HK$, and since $HK$ is a subgroup, $(hk)^{-1} = k^{-1}h^{-1} \in HK$. As $k^{-1}$ and $h^{-1}$ range over $K$ and $H$, this shows $KH \subseteq HK$. Applying the same argument with the roles of $H$ and $K$ exchanged gives $HK \subseteq KH$. Hence $HK = KH$.

($\Leftarrow$) Suppose $HK = KH$. Then $e = ee \in HK$, so $HK \ne \varnothing$. Take $h_1k_1, h_2k_2 \in HK$. Then
$$(h_1k_1)(h_2k_2)^{-1} = h_1k_1k_2^{-1}h_2^{-1} = h_1\big(k_1k_2^{-1}\big)h_2^{-1}.$$
Let $k_3 = k_1k_2^{-1} \in K$. Since $KH = HK$, there are $h_3 \in H$, $k_4 \in K$ with $k_3h_2^{-1} = h_3k_4$. Hence
$$(h_1k_1)(h_2k_2)^{-1} = h_1h_3k_4 \in HK.$$
By the subgroup criterion, $HK \le G$.

### 16.

Write $d = \gcd(n,k)$ and $k = dk_1$, $n = dn_1$ with $\gcd(n_1,k_1) = 1$.

$\langle a^k\rangle \subseteq \langle a^d\rangle$: since $d \mid k$, $a^k = (a^d)^{k/d}$.

$\langle a^d\rangle \subseteq \langle a^k\rangle$: by Bézout there are $x,y \in \mathbb{Z}$ with $d = xk + yn$, so
$$a^d = a^{xk+yn} = (a^k)^x (a^n)^y = (a^k)^x \in \langle a^k\rangle.$$

Hence $\langle a^k\rangle = \langle a^d\rangle$. Its order is $\operatorname{ord}(a^k) = n/d$ (Proposition 7.2.5). In particular $a^k$ generates $G$ iff $n/d = n$, i.e. $d = 1$, i.e. $\gcd(n,k) = 1$. There are $\varphi(n)$ such $k$ in $\{0,\dots,n-1\}$, so $G$ has $\varphi(n)$ generators.

For $n = 12$: $\varphi(12) = 4$ and the generators are $\bar 1, \bar 5, \bar 7, \overline{11}$.

### 17.

**Not cyclic.** Suppose $\mathbb{Q} = \langle q\rangle$ for some $q \in \mathbb{Q}$. Since $q \ne 0$, write $q = a/b$ with $a \ne 0$. Then $q/2 \in \mathbb{Q} = \langle q\rangle$, so $q/2 = nq$ for some $n \in \mathbb{Z}$. Dividing by $q$ gives $1/2 = n$, which is impossible for an integer. So no single element generates $\mathbb{Q}$.

**Not finitely generated.** Suppose $\mathbb{Q} = \langle q_1,\dots,q_r\rangle$ with $q_i = a_i/b_i$. Every element of the generated subgroup is an integer combination $\sum n_iq_i$, which has denominator dividing $B = |b_1b_2\cdots b_r|$ after putting over a common denominator. But $1/(2B) \in \mathbb{Q}$ and $1/(2B) = m/B$ would force $m = 1/2 \notin \mathbb{Z}$. Contradiction. So $\mathbb{Q}$ requires infinitely many generators.

### 18.

**Fermat.** Let $p$ be prime and $p \nmid a$. The classes $\bar 1,\dots,\overline{p-1}$ form the group $(\mathbb{Z}/p\mathbb{Z})^\times$ of order $p-1$: the product of two classes not divisible by $p$ is not divisible by $p$, and each $\bar a$ has an inverse by Bézout ($ax + py = 1$). By Corollary 7.5.6, $\bar a^{p-1} = \bar 1$, i.e. $a^{p-1} \equiv 1 \pmod p$.

**Computation.** $101$ is prime and $101 \nmid 3$, so $3^{100} \equiv 1 \pmod{101}$. (A direct check: $3^4 = 81$, $3^8 \equiv 81^2 = 6561 \equiv 6561 - 64\cdot101 = 6561-6464 = 97 \equiv -4$, $3^{16} \equiv 16$, $3^{32} \equiv 256 \equiv 54$, $3^{64} \equiv 54^2 = 2916 \equiv 2916-28\cdot101 = 88 \equiv -13$; then $3^{100} = 3^{64}3^{32}3^4 \equiv (-13)(54)(81)$. Now $(-13)(54) = -702 \equiv -702 + 7\cdot101 = 5$, and $5\cdot81 = 405 \equiv 405 - 4\cdot101 = 1$.)

### 19.

$\varphi(100) = \varphi(2^2\cdot 5^2) = 100(1-\tfrac12)(1-\tfrac15) = 40$, and $\gcd(7,100) = 1$, so Euler's theorem gives $7^{40} \equiv 1 \pmod{100}$.

Divide the exponent: $222 = 5\cdot 40 + 22$. Hence
$$7^{222} = (7^{40})^5\cdot 7^{22} \equiv 7^{22} \pmod{100}.$$
Now $7^2 = 49$ and $7^4 = 2401 \equiv 1 \pmod{100}$, so $7^{20} = (7^4)^5 \equiv 1$ and
$$7^{22} = 7^{20}\cdot 7^2 \equiv 49 \pmod{100}.$$
So $7^{222} \equiv 49 \pmod{100}$.

### 20.

**Index $2$ implies normal.** If $[G:H] = 2$ there are exactly two left cosets, $H$ and its complement $G\setminus H$, and exactly two right cosets, likewise $H$ and $G\setminus H$. For $g \in H$ we get $gH = H = Hg$; for $g \notin H$, both $gH$ and $Hg$ equal $G\setminus H$. So $gH = Hg$ for all $g$ and $H \trianglelefteq G$ by Lemma 7.6.2.

**Squares lie in $H$.** For $g \in G$, the two cosets are $H$ and $gH$. If $g \in H$ then $g^2 \in H$ by closure. If $g \notin H$, then $g^2 \in H \cup gH$; were $g^2 = gh$ with $h \in H$, cancellation would give $g = h \in H$, a contradiction. So $g^2 \in H$ in all cases.

**Is every normal subgroup of index $2$?** No: normality does not constrain the index to be $2$. In $S_4$ the subgroup $V_4$ is normal (Exercise 21) and has index $6$. The implication proved above runs in one direction only.

### 21.

**$V_4 \trianglelefteq S_4$.** Conjugation preserves cycle type (Proposition 7.9.11), so the conjugate of $e$ is $e$ and the conjugate of a double transposition is a double transposition, which lies in $V_4$. Hence $gV_4g^{-1} \subseteq V_4$ for every $g \in S_4$; conjugation is injective, so equality holds. Restricting to $g \in A_4$ gives $V_4 \trianglelefteq A_4$.

**Order.** $|S_4/V_4| = 24/4 = 6$ by Theorem 7.6.4.

**No element of order $6$.** Take a coset $gV_4 \ne V_4$.
* If $g$ is a transposition or a double transposition, $g^2 = e \in V_4$, so $gV_4$ has order $2$.
* If $g$ is a $3$-cycle, $g^3 = e \in V_4$ and $g \notin V_4$, so $gV_4$ has order $3$.
* If $g$ is a $4$-cycle, $g^2$ is a double transposition, hence lies in $V_4$, so $gV_4$ has order $2$.

So the quotient has elements of orders $1,2,3$ only, and no element of order $6$.

**Conclusion.** By §7.11 every group of order $6$ is either $\mathbb{Z}/6\mathbb{Z}$ (which has an element of order $6$) or $S_3$. Hence $S_4/V_4 \cong S_3$. (Example 9.7 gives a direct isomorphism.)

### 22.

**Identity.** $\varphi(e)\varphi(e) = \varphi(ee) = \varphi(e)$; cancelling $\varphi(e)$ in $H$ gives $\varphi(e) = e_H$.

**Inverses.** $\varphi(a)\varphi(a^{-1}) = \varphi(aa^{-1}) = \varphi(e) = e_H$ and similarly $\varphi(a^{-1})\varphi(a) = e_H$; by uniqueness of inverses, $\varphi(a^{-1}) = \varphi(a)^{-1}$.

**Image.** $\operatorname{im}\varphi$ is nonempty, and for $\varphi(a),\varphi(b) \in \operatorname{im}\varphi$,
$$\varphi(a)\varphi(b)^{-1} = \varphi(a)\varphi(b^{-1}) = \varphi(ab^{-1}) \in \operatorname{im}\varphi,$$
so $\operatorname{im}\varphi \le H$ by Theorem 7.3.2.

**Kernel.** $e_G \in \ker\varphi$, and if $a,b \in \ker\varphi$ then $\varphi(ab^{-1}) = \varphi(a)\varphi(b)^{-1} = e_He_H^{-1} = e_H$, so $\ker\varphi \le G$.

**Normality.** For $k \in \ker\varphi$ and $g \in G$,
$$\varphi(gkg^{-1}) = \varphi(g)\varphi(k)\varphi(g^{-1}) = \varphi(g)\,e_H\,\varphi(g)^{-1} = e_H,$$
so $g(\ker\varphi)g^{-1} \subseteq \ker\varphi$ and $\ker\varphi \trianglelefteq G$.

### 23.

**$\mathbb{Z}/6 \to \mathbb{Z}/4$.** A homomorphism is determined by $a = \varphi(\bar 1)$, and $\varphi(\bar k) = k a$. The condition is $6a = 0$ in $\mathbb{Z}/4$, i.e. $4 \mid 6a$, i.e. $2 \mid 3a$, i.e. $a$ even. So $a \in \{\bar 0, \bar 2\}$: exactly **two** homomorphisms, $\varphi \equiv 0$ and $\varphi(\bar k) = \overline{2k \bmod 4}$.

**$\mathbb{Z}/6 \to \mathbb{Z}/6$.** Here $6a = 0$ holds for every $a \in \mathbb{Z}/6$, so every $a$ gives a homomorphism $\varphi(\bar k) = \overline{ka}$: exactly **six**.

**Why they differ.** The order of $\varphi(\bar 1)$ must divide $6 = \operatorname{ord}(\bar 1)$ (Proposition 7.7.2(4)) and must be the order of an element of the target group. In $\mathbb{Z}/6$ every element has order dividing $6$, so all six choices work; in $\mathbb{Z}/4$ only $\bar 0$ and $\bar 2$ have order dividing $6$.

### 24.

The six two-element subsets of $\{1,2,3,4\}$ are the four edges $\{1,2\},\{2,3\},\{3,4\},\{1,4\}$ and the two diagonals $\{1,3\},\{2,4\}$.

**Orbit of an edge.** $r$ sends $\{1,2\} \mapsto \{2,3\} \mapsto \{3,4\} \mapsto \{1,4\}$, so the four edges form one orbit, and no symmetry sends an edge to a diagonal (adjacency is preserved). Orbit size $4$.

**Orbit of a diagonal.** $r$ swaps $\{1,3\}$ and $\{2,4\}$, so the two diagonals form one orbit of size $2$.

**Stabilisers.** For $\{1,2\}$: the elements fixing the set are $e$ and $rs = (1\,2)(3\,4)$, which swaps $1$ and $2$, so $G_{\{1,2\}} = \{e, rs\}$ has order $2$. For $\{1,3\}$: $e$, $r^2$, $s = (2\,4)$ and $r^2s = (1\,3)$ all preserve $\{1,3\}$ (the first two fix it pointwise, the last two swap), giving $G_{\{1,3\}} = \{e, r^2, s, r^2s\}$ of order $4$.

**Check.** $|G\cdot\{1,2\}| = 8/2 = 4$ and $|G\cdot\{1,3\}| = 8/4 = 2$, in agreement with the orbit–stabiliser theorem; the two orbits account for all $6 = 4+2$ subsets.

## Advanced

### 25.

**Definition.** Put $\bar\varphi(aN) = \varphi(a)$.

**Well defined.** Suppose $aN = bN$. Then $a^{-1}b \in N \subseteq \ker\varphi$ (Corollary 7.5.3), so $e_H = \varphi(a^{-1}b) = \varphi(a)^{-1}\varphi(b)$, i.e. $\varphi(a) = \varphi(b)$.

**Homomorphism.** $\bar\varphi(aN \cdot bN) = \bar\varphi(abN) = \varphi(ab) = \varphi(a)\varphi(b) = \bar\varphi(aN)\bar\varphi(bN)$.

**Uniqueness.** The quotient map $\pi : G \to G/N$ is surjective, so a homomorphism with $\bar\varphi\circ\pi = \varphi$ is determined on every coset: $\bar\varphi(aN) = \varphi(a)$.

**Kernel.** $\bar\varphi(aN) = e_H \iff \varphi(a) = e_H \iff a \in \ker\varphi$; hence
$$\ker\bar\varphi = \{aN : a \in \ker\varphi\} = (\ker\varphi)/N,$$
the image of $\ker\varphi$ under $\pi$, which is a subgroup of $G/N$ because $N \subseteq \ker\varphi$.

**Injectivity.** By Proposition 7.7.3, $\bar\varphi$ is injective iff $\ker\bar\varphi = \{N\}$, i.e. iff $(\ker\varphi)/N = \{N\}$, i.e. iff $\ker\varphi = N$.

### 26.

**The regular action.** Define $g\cdot x = gx$ for $g, x \in G$. Then $e\cdot x = x$ and $(gh)\cdot x = (gh)x = g(hx) = g\cdot(h\cdot x)$, so by Theorem 7.8.2 there is a homomorphism
$$\rho : G \to \operatorname{Sym}(G), \qquad \rho(g)(x) = gx.$$

**Injectivity.** If $\rho(g) = \mathrm{id}$ then $g = ge = \rho(g)(e) = e$. So $\ker\rho = \{e\}$ and $\rho$ is injective.

**Conclusion.** $\rho$ is an isomorphism of $G$ onto its image, so $G \cong \operatorname{im}\rho \le \operatorname{Sym}(G)$. If $|G| = n$, any bijection $G \to \{1,\dots,n\}$ conjugates $\operatorname{Sym}(G)$ to $S_n$, so $G$ embeds in $S_n$.

**Examples.** For $G = \mathbb{Z}/3\mathbb{Z}$, label the elements $0,1,2$; left translation by $1$ is the cycle $0\mapsto1\mapsto2\mapsto0$, so the image is $\langle(0\,1\,2)\rangle = A_3 \le S_3$. For $G = V_4$, label $e, a=(1\,2)(3\,4), b=(1\,3)(2\,4), c=(1\,4)(2\,3)$; left translation by $a$ swaps $e \leftrightarrow a$ and $b \leftrightarrow c$, i.e. it is $(e\,a)(b\,c)$ in the labelling, and similarly for $b$ and $c$. Under the identification of the labels with the permutations themselves, the image is exactly $V_4 \le S_4$.

### 27.

Throughout, $\varepsilon(\sigma) = \prod_{i<j}\dfrac{\sigma(j)-\sigma(i)}{j-i}$ as in Definition 7.9.6 and $N(\sigma) = \#\{(i,j) : i<j,\ \sigma(i) > \sigma(j)\}$.

**Step 1: $\varepsilon(\sigma) = (-1)^{N(\sigma)}$.** Induct on $N = N(\sigma)$. If $N = 0$ then $\sigma$ is increasing, hence the identity, and $\varepsilon = 1$. If $N > 0$, choose an inversion $(i,j)$ with $j-i$ minimal. Then $j = i+1$: for $i<k<j$ minimality gives $\sigma(i) < \sigma(k)$ and $\sigma(k) < \sigma(j)$, hence $\sigma(i) < \sigma(j)$, contradicting that $(i,j)$ is an inversion. Let $t = (i\ i+1)$. Swapping the adjacent entries at positions $i$ and $i+1$ changes only the comparison of that pair (for any $k \notin \{i,i+1\}$ the two comparisons $\sigma(k)$ vs $\sigma(i)$ and $\sigma(k)$ vs $\sigma(i+1)$ are merely exchanged), so $N(\sigma t) = N(\sigma) - 1$. By Theorem 7.9.7, $\varepsilon$ is multiplicative and $\varepsilon(t) = -1$, so $\varepsilon(\sigma) = -\varepsilon(\sigma t) = -(-1)^{N(\sigma)-1} = (-1)^{N(\sigma)}$ by the inductive hypothesis.

**Step 2: additivity mod $2$.** By Theorem 7.9.7(2) and Step 1,
$$(-1)^{N(\sigma\tau)} = \varepsilon(\sigma\tau) = \varepsilon(\sigma)\varepsilon(\tau) = (-1)^{N(\sigma)+N(\tau)},$$
so $N(\sigma\tau) \equiv N(\sigma)+N(\tau) \pmod 2$. (In particular the parity of a product depends only on the parities of the factors.)

**Step 3: $\operatorname{sgn}(\sigma) = (-1)^{n-c(\sigma)}$.** By Proposition 7.9.5, $\sigma$ is a product of $n - c(\sigma)$ transpositions; each has $\varepsilon = -1$; multiplicativity gives $\varepsilon(\sigma) = (-1)^{n-c(\sigma)}$.

**Computation.** $\sigma = (1\,4\,2)(3\,5) \in S_5$ has $n = 5$ and $c(\sigma) = 2$, so $\operatorname{sgn}(\sigma) = (-1)^{5-2} = -1$: the permutation is odd.

### 28.

**Generation.** Every $3$-cycle is even, since $(a\,b\,c) = (a\,c)(a\,b)$, so $\langle 3\text{-cycles}\rangle \subseteq A_n$. Conversely, an element of $A_n$ is a product of an even number of transpositions (Proposition 7.9.5 combined with Theorem 7.9.7(4)), and a product of two transpositions is
$$(a\,b)(a\,b) = e, \qquad (a\,b)(a\,c) = (a\,c\,b), \qquad (a\,b)(c\,d) = (a\,c\,b)(a\,c\,d)$$
for distinct $a,b,c,d$ (the last identity is checked by tracking the four letters). So every element of $A_n$ is a product of $3$-cycles.

**The case $n = 4$.** $A_4$ has $12$ elements: $e$, eight $3$-cycles and three double transpositions. The eight $3$-cycles are
$$(1\,2\,3),\ (1\,3\,2),\ (1\,2\,4),\ (1\,4\,2),\ (1\,3\,4),\ (1\,4\,3),\ (2\,3\,4),\ (2\,4\,3).$$
Each subgroup of order $3$ contains $e$ and two of them, and there are four such subgroups:
$$\langle(1\,2\,3)\rangle = \{e,(1\,2\,3),(1\,3\,2)\}, \quad \langle(1\,2\,4)\rangle,\quad \langle(1\,3\,4)\rangle,\quad \langle(2\,3\,4)\rangle,$$
each determined by the fixed point ($4$, $3$, $2$, $1$ respectively). These account for all eight $3$-cycles ($4 \times 2 = 8$) and for the count $1 + 8 + 3 = 12$.

**None is normal.** Conjugate $(1\,2\,3)$ by $(1\,2)(3\,4) \in A_4$ and use Proposition 7.9.11:
$$(1\,2)(3\,4)\,(1\,2\,3)\,(1\,2)(3\,4) = (2\,1\,4) = (1\,4\,2) \notin \langle(1\,2\,3)\rangle.$$
The conjugate lies in a different one of the four subgroups, so $\langle(1\,2\,3)\rangle$ is not normal. The same computation, with the roles of the letters permuted, shows that no subgroup of order $3$ is normal in $A_4$.

### 29.

**The rotation group.** A tetrahedron has $12$ rotations: the identity; $8$ rotations of $\pm120°$ about the four axes through a vertex and the centre of the opposite face ($4$ axes, $2$ each); and $3$ rotations of $180°$ about the three axes through the midpoints of opposite edge pairs. Total $1 + 8 + 3 = 12$.

**Cycle structures on the four faces.** Let $X$ be the $3^4 = 81$ colourings.

* Identity: $4$ fixed faces, cycle type $1^4$, so $3^4 = 81$ fixed colourings.
* $120°$ about a vertex–face axis: the face opposite the vertex is fixed and the other three are cycled, cycle type $1^1 3^1$, so $3^2 = 9$ fixed colourings. There are $8$ such rotations.
* $180°$ about an edge axis: the four faces are paired, cycle type $2^2$, so $3^2 = 9$ fixed colourings. There are $3$ such rotations.

**Burnside.** The number of colourings up to rotation is
$$\frac{1}{12}\Big(81 + 8\cdot 9 + 3\cdot 9\Big) = \frac{81+72+27}{12} = \frac{180}{12} = 15.$$
So there are **15** distinct colourings.

### 30.

**If $\gcd(m,n) = 1$.** Define $\varphi : \mathbb{Z} \to \mathbb{Z}/m\mathbb{Z}\times\mathbb{Z}/n\mathbb{Z}$ by $\varphi(k) = (\bar k, \bar k)$. It is a homomorphism, and
$$\ker\varphi = \{k : m \mid k \text{ and } n \mid k\} = \{k : mn \mid k\} = mn\mathbb{Z},$$
because $\gcd(m,n) = 1$. Both sides have $mn$ elements, so $\varphi$ induces an isomorphism $\mathbb{Z}/mn\mathbb{Z} \to \mathbb{Z}/m\mathbb{Z}\times\mathbb{Z}/n\mathbb{Z}$ (first isomorphism theorem).

**If $\gcd(m,n) = d > 1$.** For any $(a,b)$ in the product, $\operatorname{ord}(a) \mid m$ and $\operatorname{ord}(b) \mid n$, so $\operatorname{ord}(a,b)$ divides $\operatorname{lcm}(m,n) = mn/d < mn$. No element has order $mn$, so the product is not cyclic, whereas $\mathbb{Z}/mn\mathbb{Z}$ is. Hence the groups are not isomorphic.

**The case $m = n = 2$.** $\mathbb{Z}/2\times\mathbb{Z}/2$ has order $4$ but every element satisfies $2x = 0$ (each coordinate does), so no element has order $4$; $\mathbb{Z}/4$ has an element of order $4$. Hence they are not isomorphic.

**$V_4$.** Define $\psi : \mathbb{Z}/2\times\mathbb{Z}/2 \to V_4$ by $\psi(1,0) = (1\,2)(3\,4)$, $\psi(0,1) = (1\,3)(2\,4)$, extended by $\psi(a,b) = \psi(1,0)^a\psi(0,1)^b$. Both generators of the source have order $2$, the source is generated by them and is abelian, so $\psi$ is a well-defined homomorphism; its four values are $e$, $(1\,2)(3\,4)$, $(1\,3)(2\,4)$ and $(1\,2)(3\,4)(1\,3)(2\,4) = (1\,4)(2\,3)$, all distinct. So $\psi$ is a bijection, and $\mathbb{Z}/2\times\mathbb{Z}/2 \cong V_4$.

### 31.

Let $|G| = 10$. By Cauchy's theorem there are elements $a$ of order $5$ and $b$ of order $2$. Put $H = \langle a\rangle$, of order $5$ and index $2$; then $H \trianglelefteq G$ and $G = H \cup bH$, with $b \notin H$. Every element of $G$ is uniquely $a^ib^j$ with $0 \le i \le 4$, $0 \le j \le 1$, because the ten products $a^ib^j$ are distinct (if $a^ib^j = a^{i'}b^{j'}$ with $j \ne j'$ then $b \in H$, contradiction; with $j = j'$ then $a^i = a^{i'}$ and $i = i'$).

Since $H$ is normal, $bab^{-1} = a^j$ for some $j$. Conjugating twice,
$$a = b(ba b^{-1})b^{-1} = (bab^{-1})^j = a^{j^2},$$
so $5 \mid (j^2-1)$, i.e. $j \equiv \pm1 \pmod 5$.

**Case $j \equiv 1$.** Then $ab = ba$, so $\operatorname{ord}(ab) = \operatorname{ord}(a)\operatorname{ord}(b) = 10$ by Exercise 14 (with $m = 5$, $n = 2$ coprime). Hence $G = \langle ab\rangle \cong \mathbb{Z}/10\mathbb{Z}$.

**Case $j \equiv -1$.** Then $ba = a^{-1}b$, and the normal form gives
$$(a^ib^j)(a^{i'}b^{j'}) = a^{i + (-1)^j i'}\,b^{j+j'}.$$
The dihedral group $D_5 = \langle r,s \mid r^5 = s^2 = e,\ srs = r^{-1}\rangle$ has the same normal forms and the same multiplication rule, so $a^ib^j \mapsto r^is^j$ is a well-defined bijection preserving products: an isomorphism $G \cong D_5$.

Therefore the groups of order $10$ are exactly $\mathbb{Z}/10\mathbb{Z}$ and $D_5$. They are not isomorphic because $D_5$ is non-abelian while $\mathbb{Z}/10\mathbb{Z}$ is abelian.

### 32.

**The centre is nontrivial.** The class equation (Corollary 7.8.8) reads
$$|G| = |Z(G)| + \sum_i [G : C_G(a_i)],$$
where $a_i$ represent the conjugacy classes of size $>1$. Each index $[G:C_G(a_i)]$ is $>1$ and divides $|G| = p^2$, so it is $p$ or $p^2$; in either case $p$ divides it. Since $p \mid |G|$, it follows that $p \mid |Z(G)|$, so $Z(G) \ne \{e\}$.

**$G$ is abelian.** $Z(G)$ has order $p$ or $p^2$, so $G/Z(G)$ has order $p$ or $1$. A group of prime order is cyclic (Corollary 7.5.9), so $G/Z(G)$ is cyclic; by Proposition 7.7.11, $G$ is abelian.

**Groups of order $9$.** $G$ is abelian of order $9$. If some element has order $9$, then $G$ is cyclic and $G \cong \mathbb{Z}/9\mathbb{Z}$. Otherwise every non-identity element has order $3$ (orders divide $9$). Choose $a \ne e$ and $b \notin \langle a\rangle$; then $\langle a\rangle \cap \langle b\rangle$ has order dividing $3$ and does not contain $b$, hence is trivial. Since $G$ is abelian, $\langle a\rangle\langle b\rangle = \{a^ib^j\}$ is a subgroup of order $9$, i.e. all of $G$, and the map $(i,j) \mapsto a^ib^j$ is an isomorphism $\mathbb{Z}/3\mathbb{Z}\times\mathbb{Z}/3\mathbb{Z} \to G$.

So there are exactly two groups of order $9$: $\mathbb{Z}/9\mathbb{Z}$ and $\mathbb{Z}/3\mathbb{Z}\times\mathbb{Z}/3\mathbb{Z}$.

## Challenge

### 33.

Let $|G| = 8$. By Lagrange the possible element orders are $1,2,4,8$. We split into cases according to the largest order occurring.

**Case A: some element has order $8$.** Then $G = \langle a\rangle \cong \mathbb{Z}/8\mathbb{Z}$.

**Case B: every non-identity element has order $2$.** Then $G$ is abelian (Exercise 4). Choose $a \ne e$ and $b \notin \langle a\rangle$; then $H = \langle a, b\rangle = \{e, a, b, ab\}$ has four distinct elements (each of $a, b, ab$ has order $2$, and $ab$ equals none of $e,a,b$). Choose $c \notin H$, which is possible since $|H| = 4 < 8$. As $G$ is abelian, every element of $G$ has the form $a^ib^jc^k$ with $i,j,k \in \{0,1\}$. These eight elements are distinct: if $a^ib^jc^k = a^{i'}b^{j'}c^{k'}$ with $k \ne k'$, then $c \in H$, contradiction; with $k = k'$, the equality holds inside $H$, giving $i=i'$, $j=j'$. So
$$\varphi : (\mathbb{Z}/2)^3 \to G, \qquad (i,j,k) \mapsto a^ib^jc^k$$
is a bijective homomorphism (the source is generated by the three standard basis vectors of order $2$ and is abelian, so the assignment extends to a homomorphism). Hence $G \cong (\mathbb{Z}/2)^3$.

**Case C: some element $a$ has order $4$, and no element has order $8$.** Put $H = \langle a\rangle$, of index $2$, hence normal. Choose $b \notin H$; then $G = H \cup bH = \{e,a,a^2,a^3,b,ab,a^2b,a^3b\}$, and $b^2 \in H$ (Exercise 20). Moreover $b^2 \ne a$ and $b^2 \ne a^3$: if $b^2 = a$ then $b^4 = a^2 \ne e$ while $b^8 = a^4 = e$, so $\operatorname{ord}(b) = 8$, which is excluded; similarly for $a^3$. So $b^2 \in \{e, a^2\}$.

Conjugation by $b$ is an automorphism of $H$, so $bab^{-1} = a^j$ with $j \in \{1,3\}$ (Lemma 7.11.1). Four subcases remain.

* **(i) $b^2 = e$, $j = 1$.** Then $ab = ba$, $\langle a\rangle \cap \langle b\rangle = \{e\}$ and $|\langle a\rangle\langle b\rangle| = 8$, so $G = \langle a\rangle\times\langle b\rangle \cong \mathbb{Z}/4\mathbb{Z}\times\mathbb{Z}/2\mathbb{Z}$.
* **(ii) $b^2 = e$, $j = 3$.** Then $bab^{-1} = a^{-1}$. The symmetry group $D_4$ of the square has generators $r$ (order $4$) and $s$ (order $2$) satisfying $srs = r^{-1}$; the map $a^ib^j \mapsto r^is^j$ is a bijection on the eight normal forms and preserves products, so $G \cong D_4$.
* **(iii) $b^2 = a^2$, $j = 1$.** Then $b$ commutes with $a$, and $b' = ab^{-1}$ satisfies $b'^2 = a^2b^{-2} = a^2a^{-2} = e$ and $b' \notin H$ (else $b = a(b')^{-1} \in H$). Applying (i) to $b'$ gives $G \cong \mathbb{Z}/4\mathbb{Z}\times\mathbb{Z}/2\mathbb{Z}$.
* **(iv) $b^2 = a^2$, $j = 3$.** Then $a^4 = e$, $b^2 = a^2 \ne e$ and $bab^{-1} = a^{-1}$. These are exactly the relations of $Q_8$: there, with generators $i,j$, one has $i^4 = e$, $j^2 = i^2 = -1$ and $jij^{-1} = -i = i^{-1}$. The eight normal forms $a^ib^j$ are distinct, matching $1,i,i^2,i^3,j,ij,i^2j,i^3j$, and the multiplication is determined by the relations in both groups; so $a^ib^j \mapsto i^mj^n$ (with the same exponents) is an isomorphism $G \cong Q_8$.

**The five groups are pairwise non-isomorphic.** Count the elements of order $2$ and of order $4$:

| Group | elements of order $2$ | elements of order $4$ |
|---|---|---|
| $\mathbb{Z}/8$ | $1$ | $2$ |
| $\mathbb{Z}/4\times\mathbb{Z}/2$ | $3$ | $4$ |
| $(\mathbb{Z}/2)^3$ | $7$ | $0$ |
| $D_4$ | $5$ | $2$ |
| $Q_8$ | $1$ | $6$ |

The five profiles are distinct, so no two of the groups are isomorphic. (In particular $D_4 \not\cong Q_8$, although both have order $8$ and both are non-abelian.)

### 34.

**Setting up the action.** Place the $p$ beads at the vertices of a regular $p$-gon; a colouring is a function from the vertex set to the $k$ colours, so there are $k^p$ colourings. The group $C_p = \mathbb{Z}/p\mathbb{Z}$ acts by rotation, and two colourings give the same necklace exactly when they lie in the same orbit. Since $p$ is prime, the rotations are the identity and $p-1$ rotations of order $p$; each non-trivial rotation permutes the $p$ beads in a single $p$-cycle.

**Burnside's lemma.** The identity fixes all $k^p$ colourings. A non-trivial rotation fixes a colouring only if the colouring is constant, so it fixes exactly $k$ colourings. Hence
$$N = \frac{1}{p}\Big(k^p + (p-1)k\Big).$$

**Fermat.** $N$ is an integer, so $p \mid k^p + (p-1)k = k^p - k + pk$, hence $p \mid k^p - k$, i.e. $k^p \equiv k \pmod p$. If $p \nmid k$ we may divide by $k$ and recover $k^{p-1} \equiv 1 \pmod p$. (This is a second, independent proof of Fermat's little theorem.)

**Evaluation.** For $p = 5$ and $k = 2$,
$$N = \frac{2^5 + 4\cdot 2}{5} = \frac{32+8}{5} = 8.$$
So there are eight two-coloured necklaces with five beads: two monochromatic ones, and six with a non-constant pattern (two black beads adjacent, or two apart, and their complements).

### 35.

Let $|G| = 2n$ with $n$ odd.

**An involution exists.** Since $2 \mid |G|$, Cauchy's theorem (Theorem 7.8.11) gives an element $g \ne e$ with $\operatorname{ord}(g) = 2$, i.e. $g^2 = e$.

**The left regular action.** By Exercise 26 the map $\rho : G \to \operatorname{Sym}(G) \cong S_{2n}$, $\rho(x)(y) = xy$, is an injective homomorphism. Consider $L = \rho(g)$, the permutation $y \mapsto gy$ of the $2n$-element set $G$.

* $L$ has no fixed point: $gy = y$ implies $g = e$ by cancellation.
* $L^2 = \rho(g^2) = \rho(e) = \mathrm{id}$.

A fixed-point-free involution is a product of disjoint transpositions covering all $2n$ points, hence is a product of exactly $n$ transpositions. Since $n$ is odd, $\operatorname{sgn}(L) = (-1)^n = -1$.

**Conclusion.** The composite $\sigma = \operatorname{sgn}\circ\rho : G \to \{+1,-1\}$ is a homomorphism (a composite of homomorphisms), and $\sigma(g) = -1$, so $\sigma$ is surjective. Its kernel
$$K = \{x \in G : \operatorname{sgn}(\rho(x)) = +1\}$$
is a normal subgroup of index $2$ by Theorem 7.9.10 (or Proposition 7.7.3 together with the first isomorphism theorem). Hence $|K| = |G|/2 = n$ and $K \trianglelefteq G$.

### 36.

**The action.** Let $G/H$ denote the set of left cosets of $H$. Define $g \cdot (aH) = gaH$. This is well defined: if $aH = bH$ then $b = ah$ with $h \in H$, so $gb = gah$ and $gbH = gaH$. The axioms hold: $e\cdot(aH) = aH$ and $(g_1g_2)\cdot(aH) = g_1g_2aH = g_1\cdot(g_2\cdot aH)$. So by Theorem 7.8.2 there is a homomorphism
$$\rho : G \to \operatorname{Sym}(G/H) \cong S_n.$$

**The kernel.** $g \in K := \ker\rho$ iff $gaH = aH$ for every $a \in G$ iff $a^{-1}ga \in H$ for every $a$ iff $g \in aHa^{-1}$ for every $a$. Hence
$$K = \bigcap_{a \in G} aHa^{-1}.$$
It is normal, being a kernel (Proposition 7.7.3), and $K \le H$ (take $a = e$). This intersection is called the **core** of $H$.

**Index $p$.** Now let $p$ be the smallest prime dividing $|G|$ and suppose $[G:H] = p$. By the index tower,
$$[G:K] = [G:H]\,[H:K] = p\,[H:K].$$
Since $G/K$ embeds in $S_p$ (first isomorphism theorem: $G/K \cong \operatorname{im}\rho \le S_p$), $[G:K]$ divides $p! = p(p-1)!$. Hence $[H:K]$ divides $(p-1)!$.

But every prime divisor of $[H:K]$ divides $|H|$, hence divides $|G|$, hence is at least $p$ (as $p$ is the smallest prime divisor of $|G|$). On the other hand every prime divisor of $(p-1)!$ is less than $p$. So $[H:K]$ has no prime divisor, i.e. $[H:K] = 1$, giving $K = H$ and $H \trianglelefteq G$.

**Simple groups.** If $G$ is simple and $H \le G$ with $[G:H] = n \ge 2$, then $K \trianglelefteq G$ and $K \le H < G$, so $K \ne G$; simplicity forces $K = \{e\}$. Then $\rho$ is injective and $G \cong \operatorname{im}\rho \le S_n$, so $|G|$ divides $n!$. (For example a simple group with a subgroup of index $5$ has order dividing $120$.)

### 37.

**Realisation in $GL_2(\mathbb{C})$.** Let
$$I = \begin{pmatrix}1&0\\0&1\end{pmatrix}, \quad A = \begin{pmatrix} i&0\\0&-i\end{pmatrix}, \quad B = \begin{pmatrix}0&1\\-1&0\end{pmatrix}, \quad C = AB = \begin{pmatrix}0&i\\ i&0\end{pmatrix}.$$
Direct computation gives
$$A^2 = B^2 = C^2 = -I, \qquad AB = C, \quad BA = -C,$$
and hence $AB = -BA$. The set $\{\pm I, \pm A, \pm B, \pm C\}$ is closed under multiplication (products of the generators reduce to $\pm$ one of them) and under inversion ($X^{-1} = -X$ for $X \in \{\pm A, \pm B, \pm C\}$, since $X^2 = -I$). By the subgroup criterion (Theorem 7.3.2) it is a subgroup of $GL_2(\mathbb{C})$, and it is $Q_8$ with $i \leftrightarrow A$, $j \leftrightarrow B$, $k \leftrightarrow C$.

**Exactly one element of order $2$.** The identity has order $1$; $-I \ne I$ and $(-I)^2 = I$, so $-I$ has order $2$. For $X \in \{\pm A,\pm B,\pm C\}$ we have $X^2 = -I \ne I$ but $X^4 = I$, so $\operatorname{ord}(X) = 4$. So the only element of order $2$ is $-I$. Equivalently, $Q_8$ has six elements of order $4$ and one of order $2$.

**Every subgroup is normal.** The subgroups are:
* $\{I\}$ and $Q_8$ (trivially normal);
* $\{\pm I\} = Z(Q_8)$, normal because central;
* $\langle A\rangle = \{\pm I, \pm A\}$, $\langle B\rangle$, $\langle C\rangle$, each of order $4$ and index $2$, hence normal.

There are no others: a subgroup of order $4$ is either cyclic, hence generated by one of the six elements of order $4$ (giving the three subgroups above), or isomorphic to $V_4$, which would contain three elements of order $2$ — impossible; and a subgroup of order $2$ is generated by an element of order $2$, of which there is only $-I$. Thus every subgroup of $Q_8$ is normal (such groups are called *Hamiltonian*).

**$Q_8 \not\cong D_4$.** $D_4$ has five elements of order $2$ ($r^2$ and the four reflections) and two of order $4$ ($r, r^3$), whereas $Q_8$ has one element of order $2$ and six of order $4$. Isomorphic groups have the same number of elements of each order, so $Q_8 \not\cong D_4$.

### 38.

**The normaliser is a subgroup.** $e \in N_G(H)$ since $eHe^{-1} = H$. If $g_1, g_2 \in N_G(H)$ then $g_2Hg_2^{-1} = H$, hence also $g_2^{-1}Hg_2 = H$ (multiply the equality by $g_2^{-1}$ on the left and $g_2$ on the right). Therefore
$$(g_1g_2^{-1})H(g_1g_2^{-1})^{-1} = g_1\big(g_2^{-1}Hg_2\big)g_1^{-1} = g_1Hg_1^{-1} = H,$$
so $g_1g_2^{-1} \in N_G(H)$ and $N_G(H) \le G$ by Theorem 7.3.2. (Independently, $N_G(H)$ is the stabiliser of $H$ under the conjugation action on the set of subgroups, so Proposition 7.8.6 also applies.)

**Conjugation action.** $G$ acts on its set of subgroups by $g \cdot H = gHg^{-1}$; the axioms hold because $(g_1g_2)Hg_1g_2^{-1} = g_1(g_2Hg_2^{-1})g_1^{-1}$ and $eHe^{-1} = H$. The orbit of $H$ is the set of its conjugates, and the stabiliser of $H$ is, by definition, $N_G(H)$. The orbit–stabiliser theorem (Theorem 7.8.7) therefore gives
$$\#\{\text{conjugates of } H\} = [G : N_G(H)].$$

**The subgroups of $S_3$.** There are six: $\{e\}$, $A_3 = \langle(1\,2\,3)\rangle$, and the three subgroups of order $2$, namely $\langle(1\,2)\rangle, \langle(1\,3)\rangle, \langle(2\,3)\rangle$.

* $H = \{e\}$: $N_G(H) = G$, so $H$ has $[G:G] = 1$ conjugate.
* $H = A_3$: $A_3 \trianglelefteq S_3$, so $N_G(A_3) = G$ and there is $1$ conjugate.
* $H = \langle(1\,2)\rangle$: if $gHg^{-1} = H$ then $g(1\,2)g^{-1}$ must be the unique element of order $2$ in $H$, namely $(1\,2)$ itself. The centraliser of $(1\,2)$ in $S_3$ is $\{e, (1\,2)\}$ (checking: $(1\,3)(1\,2)(1\,3)^{-1} = (2\,3) \ne (1\,2)$ and $(1\,2\,3)(1\,2)(1\,3\,2) = (2\,3) \ne (1\,2)$), so $N_G(H) = H$ and the number of conjugates is $[S_3 : H] = 3$. Indeed the three subgroups of order $2$ are conjugate to each other.

As a check, the conjugacy classes of subgroups have sizes $1 + 1 + 3 = 5$, and together with $S_3$ itself (one conjugate, since $N_G(G) = G$) they account for all six subgroups.


