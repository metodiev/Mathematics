# Fields — Exercises

> [Fields](README.md) · 36 problems · Beginner → Challenge · Solutions: [solutions.md](solutions.md)

Attempt every problem in writing before looking at [solutions.md](solutions.md). Each problem names the section of the tutorial that supplies the technique. Problems marked *(proof)* require a complete argument, with the hypotheses stated and every step justified.

Notation: $F^\times = F\setminus\{0\}$; $\mathbb{F}_q$ is the field with $q$ elements; $[E:F]$ is the degree; $m_\alpha$ is the minimal polynomial of $\alpha$ over the base field; $\zeta_n = e^{2\pi i/n}$; $\mathbb{Q}(x)$ is the field of rational functions and $\mathbb{Q}[[x]]$ the ring of formal power series. All fields have $1 \ne 0$.

## Beginner

**1.** *(§5.1)* Decide which of the following are fields. For those that are not, name the axiom that fails and give a nonzero element with no inverse.
(a) $\mathbb{Q}$; (b) $\mathbb{Z}$; (c) $\mathbb{Z}/7\mathbb{Z}$; (d) $\mathbb{Z}/8\mathbb{Z}$; (e) $\mathbb{Q}[x]$; (f) $\mathbb{Q}(\sqrt2)$; (g) $\mathbb{H}$; (h) $\mathbb{Q}[[x]]$, the ring of formal power series $\sum_{n\ge0}a_nx^n$ with coefficientwise addition and the Cauchy product; (i) $\mathbb{F}_4$; (j) $\mathbb{Z}[i]$.

**2.** *(§5.3)* Determine the prime subfield of each field: $\mathbb{F}_{49}$; $\mathbb{Q}(\sqrt[3]{2})$; $\mathbb{F}_2(x)$; $\mathbb{Q}(\pi)$; $\mathbb{C}$.

**3.** *(§7.3)* Compute the minimal polynomial over $\mathbb{Q}$ and the degree of: (a) $\sqrt5$; (b) $\sqrt[3]{3}$; (c) $\zeta_6$; (d) $i$ over $\mathbb{Q}(\sqrt2)$.

**4.** *(§7.2)* Compute the following degrees, justifying each step: $[\mathbb{Q}(\sqrt2,\sqrt5):\mathbb{Q}]$; $[\mathbb{F}_{27}:\mathbb{F}_3]$; $[\mathbb{C}:\mathbb{Q}]$; $[\mathbb{Q}(\sqrt2,\sqrt[3]{2}):\mathbb{Q}]$.

**5.** *(§7.5)* Write out the elements of $\mathbb{F}_4 = \mathbb{F}_2[x]/(x^2+x+1)$ and of $\mathbb{F}_9 = \mathbb{F}_3[x]/(x^2+1)$, and compute $(1+\alpha)(1+\alpha^2)$ in $\mathbb{F}_4$ and $(1+\alpha)(2+\alpha)$ in $\mathbb{F}_9$, where $\alpha$ denotes the class of $x$ in each case.

**6.** *(§7.5)* Prove that $x^2+1$ is irreducible over $\mathbb{F}_3$, so that $\mathbb{F}_9 = \mathbb{F}_3[x]/(x^2+1)$ is a field. Show that the class of $x$ has order $4$ in $\mathbb{F}_9^\times$ and find a generator of $\mathbb{F}_9^\times$, listing its eight powers.

**7.** *(§7.2)* *(proof)* Prove that $\sqrt2 \notin \mathbb{Q}$ and $\sqrt[3]{2} \notin \mathbb{Q}$.

**8.** *(§7.4)* Compute the inverses in $\mathbb{Q}(\sqrt2)$ of $3+2\sqrt2$, of $1-\sqrt2$ and of $2+3\sqrt2$.

**9.** *(§7.5)* List all subfields of $\mathbb{F}_{64}$ and of $\mathbb{F}_{81}$, giving the inclusion relations.

**10.** *(§7.5)* In $\mathbb{F}_5$, verify that $a^4 = 1$ for every nonzero $a$ and that $x^5-x = \prod_{a\in\mathbb{F}_5}(x-a)$.

**11.** *(§7.7)* Show that $\sqrt5$ and $\sqrt[4]{2}$ are constructible, and state the degree of each over $\mathbb{Q}$.

**12.** *(§7.3)* *(proof)* Using the fact that $\pi$ is transcendental over $\mathbb{Q}$, prove that $\mathbb{Q}(\pi) \cong \mathbb{Q}(x)$ and that $\pi^2$ is transcendental over $\mathbb{Q}$.

## Intermediate

**13.** *(§7.1)* *(proof)* Prove that $\operatorname{Frac}(\mathbb{Z}[i]) = \mathbb{Q}(i)$, that $\operatorname{Frac}(\mathbb{Z}[\sqrt2]) = \mathbb{Q}(\sqrt2)$, and that $\operatorname{Frac}(F[x]) = F(x)$.

**14.** *(§7.1)* *(proof)* Use the universal property (Theorem 7.1.2) to prove that if $D$ is an integral domain contained in a field $K$, then there is an injective homomorphism $\operatorname{Frac}(D) \to K$ fixing $D$. Deduce that $\operatorname{Frac}(D)$ is the smallest field containing $D$, up to isomorphism, and that $\operatorname{Frac}(\operatorname{Frac}(D)) = \operatorname{Frac}(D)$.

**15.** *(§7.2, §7.8)* *(proof)* Prove that $[\mathbb{Q}(\sqrt2,\sqrt3):\mathbb{Q}] = 4$ and that its intermediate fields are exactly $\mathbb{Q}$, $\mathbb{Q}(\sqrt2)$, $\mathbb{Q}(\sqrt3)$, $\mathbb{Q}(\sqrt6)$ and $\mathbb{Q}(\sqrt2,\sqrt3)$.

**16.** *(§7.2)* *(proof)* Let $E/F$ be a field extension with $[E:F] = p$ prime. Prove that for every $\alpha \in E\setminus F$ one has $E = F(\alpha)$, and deduce that $E/F$ has no intermediate fields.

**17.** *(§7.3)* *(proof)* Prove that $\alpha$ is algebraic over $F$ if and only if $F[\alpha] = F(\alpha)$, and that in that case $[F(\alpha):F] = \deg m_\alpha$.

**18.** *(§7.3)* *(proof)* Let $\alpha, \beta$ be algebraic over $F$. Prove that $[F(\alpha,\beta):F] \le [F(\alpha):F]\cdot[F(\beta):F]$ and that $F(\alpha,\beta)/F$ is algebraic.

**19.** *(§7.4)* Compute $(\alpha^2+\alpha)^{-1}$ in $\mathbb{F}_8 = \mathbb{F}_2[x]/(x^3+x+1)$ and $(1+\alpha)^{-1}$ in $\mathbb{F}_9 = \mathbb{F}_3[x]/(x^2+1)$, expressing both in the standard basis.

**20.** *(§7.5)* *(proof)* Let $F$ be a finite field with $q$ elements. Prove that $a^q = a$ for all $a \in F$, and deduce that $x^q-x = \prod_{a\in F}(x-a)$ in $F[x]$.

**21.** *(§7.5)* *(proof)* Prove that the fixed field of the Frobenius automorphism of $\mathbb{F}_{p^n}$ is $\mathbb{F}_p$, and deduce that if $\alpha$ is a root of an irreducible polynomial of degree $d$ over $\mathbb{F}_p$, then $\alpha^{p^d} = \alpha$.

**22.** *(§7.7)* *(proof)* Prove that if $x > 0$ is constructible then so is $\sqrt x$, by giving the construction and proving that it works. Deduce that every element of a tower $\mathbb{Q} = K_0 \subseteq K_1 \subseteq \cdots \subseteq K_n$ with $[K_{i+1}:K_i] \le 2$ that is real is constructible.

## Advanced

**23.** *(§7.5)* *(proof)* Let $F$ be a finite field with $q$ elements. For each divisor $d$ of $q-1$, prove that $F^\times$ has exactly $\varphi(d)$ elements of order $d$, and deduce $\sum_{d \mid q-1}\varphi(d) = q-1$.

**24.** *(§7.5)* Use the factorisation of $x^{p^n}-x$ (Theorem 7.5.6) to compute the number of monic irreducible polynomials of degree $5$ over $\mathbb{F}_2$ and of degree $2$ over $\mathbb{F}_3$. Verify the second answer by listing the polynomials.

**25.** *(§7.5)* *(proof)* Exhibit an explicit isomorphism
$$\mathbb{F}_3[x]/(x^2+1) \longrightarrow \mathbb{F}_3[y]/(y^2+2y+2),$$
by finding a root of $X^2+1$ in the second field, and prove that your map is well defined and bijective.

**26.** *(§7.2, §7.3)* *(proof)* Let $F \subseteq F(\beta) \subseteq E$ with $\beta$ algebraic over $F$ and $\alpha \in E$ algebraic over $F(\beta)$. Prove that $\alpha$ is algebraic over $F$ and that
$$[F(\alpha,\beta):F] \le [F(\alpha):F]\,[F(\beta):F].$$

**27.** *(§7.7)* *(proof)* Prove that if $x \in \mathbb{R}$ has $[\mathbb{Q}(x):\mathbb{Q}] = 2$ then $x$ is constructible. Combine this with Theorem 7.7.3 to state precisely which numbers of degree $2$ are constructible.

**28.** *(§7.8)* *(proof)* Let $E/F$ be a Galois extension of degree $4$. Prove that $\operatorname{Gal}(E/F)$ is isomorphic to either $\mathbb{Z}/4\mathbb{Z}$ or $\mathbb{Z}/2\mathbb{Z}\times\mathbb{Z}/2\mathbb{Z}$, and give an example of each.

**29.** *(§7.5)* *(proof)* Let $\sigma$ be the Frobenius automorphism of $\mathbb{F}_{p^n}$. Prove that $\sigma$ has order exactly $n$ in $\operatorname{Aut}(\mathbb{F}_{p^n})$, and that the fixed field of $\sigma^k$ is $\mathbb{F}_{p^{\gcd(k,n)}}$.

**30.** *(§7.3, §7.2)* *(proof)* Let $\alpha = \sqrt[3]{2}$ and $\omega = \zeta_3$. Prove that the minimal polynomial of $\omega$ over $\mathbb{Q}(\alpha)$ is $x^2+x+1$ and deduce $[\mathbb{Q}(\alpha,\omega):\mathbb{Q}] = 6$.

**31.** *(§5.1, §7.3)* *(proof)* Prove that every field isomorphism fixes the prime subfield pointwise, and deduce that $\mathbb{Q}(\sqrt2)$ and $\mathbb{Q}(\sqrt3)$ are not isomorphic as fields.

## Challenge

**32.** *(§7.5)* *(proof)* Let $f \in \mathbb{F}_p[x]$ be irreducible of degree $n$. Prove that $f$ has $n$ distinct roots in $\mathbb{F}_{p^n}$ and that $\mathbb{F}_{p^n}$ is a splitting field of $f$ over $\mathbb{F}_p$. Deduce that every finite extension of finite fields is normal.

**33.** *(§7.7)* *(proof)* Prove that the set of constructible real numbers is a subfield of $\mathbb{R}$ closed under the operation $x \mapsto \sqrt x$ for $x > 0$. You may use the classical constructions of sums, products, quotients and square roots by similar triangles and by the semicircle, but you must say precisely which construction you use and why it produces the required length.

**34.** *(§7.8)* *(proof)* Prove that $\mathbb{Q}(\zeta_5)/\mathbb{Q}$ is Galois with cyclic Galois group of order $4$, determine its subgroup lattice, and use the fundamental theorem to prove that $\mathbb{Q}(\sqrt5)$ is the unique intermediate field of degree $2$ over $\mathbb{Q}$.

**35.** *(§7.2, §7.3)* *(proof)* Prove that $\mathbb{Q}(2^{1/6}) = \mathbb{Q}(\sqrt2,\sqrt[3]{2})$ and compute $[\mathbb{Q}(2^{1/6}):\mathbb{Q}]$. What is the minimal polynomial of $2^{1/6}$ over $\mathbb{Q}$?

**36.** *(§7.8)* *(proof)* Let $E$ be the splitting field of $x^4-2$ over $\mathbb{Q}$. Prove that $[E:\mathbb{Q}] = 8$ and that $\operatorname{Gal}(E/\mathbb{Q}) \cong D_4$, the dihedral group of order $8$.
