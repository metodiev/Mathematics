# Algebraic Topology — Solutions

> [Algebraic Topology](README.md) · Solutions to [exercises.md](exercises.md) · 36 problems

Each solution states the strategy, then carries out every step. Section references point into
[README.md](README.md). Notation is that of the exercises: $H_n(X) = H_n(X;\mathbb{Z})$ unless
coefficients are displayed, and $\tilde H_n$ is reduced homology.

## Beginner

**1.** **Strategy.** Write down the conjugation map, check that it is a homomorphism, exhibit an
inverse, and compare two paths that are homotopic rel endpoints.

**Homomorphism.** Let $\gamma, \delta$ be loops at $x_1$. Then
$$\varphi_\alpha([\gamma][\delta]) = [\alpha * (\gamma * \delta) * \bar\alpha], \qquad
\varphi_\alpha([\gamma])\varphi_\alpha([\delta]) = [(\alpha * \gamma * \bar\alpha) * (\alpha * \delta * \bar\alpha)].$$
The two loops differ only by inserting the backtracking path $\bar\alpha * \alpha$ at the junction.
The loop $\bar\alpha * \alpha$ is null-homotopic rel endpoints, so the two classes are equal.

**Inverse.** Let $\bar\alpha$ be the reverse path from $x_1$ to $x_0$. Then $\varphi_{\bar\alpha} \circ \varphi_\alpha$ sends $[\gamma]$ to $[\bar\alpha * \alpha * \gamma * \bar\alpha * \alpha]$, which is $[\gamma]$ because the inserted backtracking loops are null-homotopic. Similarly in the other order. Hence $\varphi_\alpha$ is bijective and is an isomorphism.

**Well-definedness.** If $\alpha \simeq \alpha'$ rel endpoints, then $\alpha * \gamma * \bar\alpha$ and $\alpha' * \gamma * \bar\alpha'$ are homotopic rel endpoints by composing the homotopy of $\alpha$ with $\gamma$ and the reverse homotopy. Hence $\varphi_\alpha = \varphi_{\alpha'}$.

**2.** **Strategy.** Use the identification $\pi_1(S^1,1) \cong \mathbb{Z}$ and the Hurewicz theorem.

For $k \ge 0$, the map $f_k$ sends the loop $\gamma(t) = e^{2\pi i t}$ to $t \mapsto e^{2\pi i k t}$, which represents $k$ times the generator of $\pi_1(S^1,1)$. Hence $(f_k)_*$ is multiplication by $k$ on $\pi_1$, and therefore multiplication by $k$ on $H_1$ by Theorem 7.1.1. Thus $\deg(f_k) = k$ for $k \ge 0$.

For $k = -m < 0$, write $f_k = f_{-1} \circ f_m$, where $f_{-1}(z) = \bar z$ is the reflection of the circle, a homeomorphism reversing orientation. Its degree is $-1$: it sends the counterclockwise generator to the clockwise generator. By multiplicativity of degree,
$$\deg(f_k) = \deg(f_{-1})\deg(f_m) = (-1) \cdot m = -m = k.$$
The case $k = 0$ is the constant map, of degree $0$. In every case $(f_k)_* : H_1 \to H_1$ is multiplication by $k$.

**Common pitfall.** It is tempting to say that $z \mapsto z^{-1}$ has degree $1$ because it is a bijection. Degree counts orientation, and the conjugation reverses it.

**3.** **Strategy.** Compute the simplicial boundary maps and solve the cycle equations.

The chain groups are $C_0 = \mathbb{Z}^4$ with basis $v_0,v_1,v_2,v_3$, $C_1 = \mathbb{Z}^4$ with basis $e_{01},e_{12},e_{23},e_{30}$, and $C_n = 0$ for $n \ge 2$. The boundaries are
$$\partial e_{01} = v_1 - v_0, \quad \partial e_{12} = v_2 - v_1, \quad \partial e_{23} = v_3 - v_2, \quad \partial e_{30} = v_0 - v_3.$$

*Degree $1$.* For $c = a e_{01} + b e_{12} + c e_{23} + d e_{30}$,
$$\partial c = (d-a)v_0 + (a-b)v_1 + (b-c)v_2 + (c-d)v_3.$$
This vanishes iff $a = b = c = d$. Hence $Z_1 = \mathbb{Z}(e_{01} + e_{12} + e_{23} + e_{30}) \cong \mathbb{Z}$. Since $C_2 = 0$, $B_1 = 0$, so $H_1 = Z_1 \cong \mathbb{Z}$.

*Degree $0$.* The space is path-connected, so $H_0 \cong \mathbb{Z}$ by Theorem 7.4.1.

*Degree $2$.* $C_2 = 0$, so $H_2 = 0$. Therefore $H_0 \cong \mathbb{Z}$, $H_1 \cong \mathbb{Z}$, and all other groups vanish. The Euler characteristic is $4 - 4 = 0$, consistent with $b_0 - b_1 = 1 - 1 = 0$.

**4.** **Strategy.** Use additivity of singular chains over disjoint unions and Theorem 7.4.1.

Chains split: $C_n(X) \cong C_n(S^1) \oplus C_n(S^1) \oplus C_n(\mathrm{pt})$, so homology splits. Therefore
$$H_0(X) \cong \mathbb{Z} \oplus \mathbb{Z} \oplus \mathbb{Z} = \mathbb{Z}^3, \qquad H_1(X) \cong \mathbb{Z} \oplus \mathbb{Z} \oplus 0 = \mathbb{Z}^2,$$
and $H_n(X) = 0$ for $n \ge 2$. The three path components give $H_0 \cong \mathbb{Z}^3$, in agreement with Theorem 7.4.1. The Euler characteristic is
$$\chi(X) = 3 - 2 = 1,$$
which also equals $\chi(S^1) + \chi(S^1) + \chi(\mathrm{pt}) = 0 + 0 + 1$.

**5.** **Strategy.** Compare the identity with a constant map using homotopy invariance.

Let $c : X \to X$ be a constant map with value $x_0$. Since $X$ is contractible, $\operatorname{id}_X \simeq c$. By Theorem 7.5.2, the induced maps on reduced homology are equal:
$$\operatorname{id}_{\tilde H_n(X)} = (\operatorname{id}_X)_* = c_*.$$
But $c$ factors as $X \to \{x_0\} \hookrightarrow X$, so $c_*$ factors through $\tilde H_n(\{x_0\}) = 0$ (Theorem 8.1). Hence $c_* = 0$, and therefore $\operatorname{id}_{\tilde H_n(X)} = 0$. The only abelian group whose identity endomorphism is zero is the zero group, so $\tilde H_n(X) = 0$ for every $n$.

**6.** **Strategy.** Compute kernels and images degree by degree.

*Degree $2$.* $\partial_2$ is injective, so $H_2 = \ker \partial_2 = 0$.

*Degree $1$.* $Z_1 = \ker \partial_1 = \mathbb{Z}$ because $\partial_1 = 0$. $B_1 = \operatorname{im}\partial_2 = 2\mathbb{Z}$. Hence
$$H_1 = \mathbb{Z}/2\mathbb{Z}.$$

*Degree $0$.* $Z_0 = \mathbb{Z}$ and $B_0 = \operatorname{im}\partial_1 = 0$, so $H_0 = \mathbb{Z}$.

The complex has the homology of $\mathbb{R}P^2$, namely $(\mathbb{Z}, \mathbb{Z}/2, 0)$.

**7.** **Strategy.** Show that a chain map sends cycles to cycles and boundaries to boundaries.

Let $z \in Z_n(C_*)$, so $\partial z = 0$. Then $\partial' f_n(z) = f_{n-1}(\partial z) = 0$, so $f_n(z) \in Z_n(D_*)$. If $z = \partial w$ with $w \in C_{n+1}$, then $f_n(z) = f_n(\partial w) = \partial' f_{n+1}(w) \in B_n(D_*)$. Hence the formula $f_*[z] = [f_n(z)]$ is well defined on $Z_n/B_n$.

It is a homomorphism because $f_n$ is. Functoriality is immediate: $(g \circ f)_n = g_n \circ f_n$, which induces $(g \circ f)_* = g_* \circ f_*$ on homology, and $(\operatorname{id}_{C_*})_n = \operatorname{id}_{C_n}$ induces the identity.

**8.** **Strategy.** Use the augmentation $\varepsilon : C_0(X) \to \mathbb{Z}$ and show that its kernel is exactly $B_0(X)$ when $X$ is path-connected.

For a $1$-simplex $\sigma$, $\partial\sigma = \sigma(e_1) - \sigma(e_0)$, so $\varepsilon(\partial\sigma) = 0$. Hence $B_0(X) \subseteq \ker\varepsilon$, and $\varepsilon$ descends to a homomorphism $\varepsilon_* : H_0(X) \to \mathbb{Z}$.

It is surjective: the class of any point $x \in X$ maps to $1$.

It is injective. Let $c = \sum_i n_i x_i$ be a $0$-cycle with $\varepsilon(c) = \sum_i n_i = 0$. Fix a basepoint $b \in X$. For each $x_i$ choose a path $\gamma_i$ from $x_i$ to $b$. Then $\partial\gamma_i = b - x_i$, so $x_i - b = -\partial\gamma_i$ is a boundary. Hence
$$c = \sum_i n_i x_i = \Bigl(\sum_i n_i\Bigr)b - \partial\Bigl(\sum_i n_i \gamma_i\Bigr) = -\partial\Bigl(\sum_i n_i \gamma_i\Bigr)$$
because $\sum n_i = 0$. Thus $c \in B_0(X)$, so $[c] = 0$. Therefore $\varepsilon_*$ is an isomorphism and $H_0(X) \cong \mathbb{Z}$.

**9.** **Strategy.** Use $\chi = \sum(-1)^i c_i$ and $\chi = \sum(-1)^i b_i$.

*Cell counts.*
- $S^2$: one $0$-cell and one $2$-cell, so $\chi = 1 + 1 = 2$.
- $T^2$: one $0$-cell, two $1$-cells and one $2$-cell, so $\chi = 1 - 2 + 1 = 0$.
- $\mathbb{R}P^2$: one cell in each of dimensions $0,1,2$, so $\chi = 1 - 1 + 1 = 1$.
- $K$: one $0$-cell, two $1$-cells and one $2$-cell, so $\chi = 1 - 2 + 1 = 0$.

*Betti numbers.*
- $S^2$: $(b_0,b_1,b_2) = (1,0,1)$, so $\chi = 1 - 0 + 1 = 2$.
- $T^2$: $(1,2,1)$, so $\chi = 1 - 2 + 1 = 0$.
- $\mathbb{R}P^2$: $H_1$ is $\mathbb{Z}/2$, which has rank $0$ over $\mathbb{Q}$, so $(1,0,0)$ and $\chi = 1$.
- $K$: $H_1 \cong \mathbb{Z} \oplus \mathbb{Z}/2$ has rank $1$, so $(1,1,0)$ and $\chi = 1 - 1 = 0$.

**10.** **Strategy.** Use Theorem 5.2.6 and the classification of subgroups of $\mathbb{Z}$.

The subgroups of $\pi_1(S^1,1) \cong \mathbb{Z}$ are exactly $n\mathbb{Z}$ for $n \ge 0$.

- $n = 0$: the universal cover $\exp : \mathbb{R} \to S^1$. The total space is connected and simply connected, and the deck group is $\mathbb{Z}$.
- $n \ge 1$: the $n$-fold cover $p_n : S^1 \to S^1$, $p_n(z) = z^n$. The total space is connected, the subgroup is $n\mathbb{Z}$, and the deck group is $\mathbb{Z}/n\mathbb{Z}$, generated by rotation by $2\pi/n$.

These are all the connected coverings up to isomorphism over $S^1$. A covering with disconnected total space is a disjoint union of connected coverings, so the connected classification determines all coverings.

**11.** **Strategy.** Use the definitions and an explicit winding computation.

The constant map $c : S^n \to S^n$ factors through a point, and $H_n(\mathrm{pt}) = 0$, so $c_* = 0$ and $\deg(c) = 0$. The identity induces the identity on $H_n$, so $\deg(\operatorname{id}) = 1$.

For the nonconstant example, define $f : S^1 \to S^1$ by
$$
f(e^{i\theta}) =
\begin{cases}
e^{i\theta}, & 0 \le \theta \le \pi,\\
e^{-i\theta}, & \pi \le \theta \le 2\pi.
\end{cases}
$$
The formula is well defined at $\theta = 0, \pi, 2\pi$ because $e^{i\pi} = e^{-i\pi} = -1$ and $e^{0} = e^{-2\pi i} = 1$, so $f$ is continuous (the two branches agree at the endpoints). On the upper semicircle, $f$ traverses the upper semicircle counterclockwise; on the lower semicircle, $f$ traverses the *same* upper semicircle clockwise. The total signed winding is $+1 + (-1) = 0$, so $\deg(f) = 0$. The map is not constant.

**12.** **Strategy.** Write the singular chain complex explicitly; it is larger than one might expect, because every constant simplex is a singular simplex.

$S^0 = \{1,-1\}$ is a discrete space with two points. Since $\Delta^n$ is path-connected and $S^0$ is discrete, every continuous map $\sigma : \Delta^n \to S^0$ is constant. Hence for every $n \ge 0$ the group $C_n(S^0)$ is free abelian on two generators, the constant simplices $c_1$ and $c_{-1}$ at the two points.

For $n \ge 1$,
$$\partial_n c_p = \sum_{i=0}^{n} (-1)^i c_p = \Bigl(\sum_{i=0}^{n} (-1)^i\Bigr) c_p = \begin{cases} c_p, & n \text{ even},\\ 0, & n \text{ odd}.\end{cases}$$
Thus $\partial_n$ is the identity map $\mathbb{Z}^2 \to \mathbb{Z}^2$ when $n$ is even and the zero map when $n$ is odd. (For $n=0$, $\partial_0=0$.)

Now compute degree by degree. $H_0 = C_0/\operatorname{im}\partial_1 = \mathbb{Z}^2$ because $\partial_1 = 0$.

If $n \ge 1$ is odd, then $\partial_n = 0$, so $Z_n = \mathbb{Z}^2$; but $n+1$ is even, so $\partial_{n+1}$ is the identity and $B_n = \mathbb{Z}^2$. Hence $H_n = 0$.

If $n \ge 2$ is even, then $\partial_n$ is the identity, so $Z_n = 0$, and hence $H_n = 0$.

Therefore
$$H_0(S^0) = \mathbb{Z}^2, \qquad H_n(S^0) = 0 \quad (n \ge 1),$$
and the reduced groups are $\tilde H_0(S^0) = \mathbb{Z}$ and $\tilde H_n(S^0) = 0$ for $n \ge 1$. This agrees with Theorem 7.4.1, since $S^0$ has two path components.

## Intermediate

**13.** **Strategy.** Write the Möbius band as a quotient and exhibit the deformation retraction.

Model the Möbius band as $M = [0,1] \times [-1,1] / \sim$ with $(0,t) \sim (1,-t)$. Define
$$H : M \times [0,1] \to M, \qquad H([(s,t)],u) = [(s,(1-u)t)].$$
This is well defined: if $s = 0$ and $t$ is replaced by the equivalent point $(1,-t)$, then the images are $[(0,(1-u)t)]$ and $[(1,-(1-u)t)]$, which are equivalent. It is continuous because the quotient map is a quotient map and the formula respects the relation. At $u=0$ it is the identity; at $u=1$ it lands in the image of $[0,1] \times \{0\}$, which is a circle (the core). On the core it is the identity. Hence $M$ deformation retracts onto $S^1$.

By homotopy invariance, $H_0(M) \cong \mathbb{Z}$, $H_1(M) \cong \mathbb{Z}$, and $H_n(M) = 0$ for $n \ge 2$. The Euler characteristic is $1 - 1 = 0$. The standard square model has two $0$-cells (the two equivalence classes of corners), three $1$-cells (the top edge, the bottom edge, and the identified pair of vertical edges) and one $2$-cell, so the cell count is $2 - 3 + 1 = 0$, in agreement.

**14.** **Strategy.** Use the wedge axiom and the known homology of the summands.

For a finite wedge of path-connected CW complexes,
$$\tilde H_n(S^2 \vee S^2 \vee S^1) \cong \tilde H_n(S^2) \oplus \tilde H_n(S^2) \oplus \tilde H_n(S^1).$$
Therefore $\tilde H_0 = 0$ (the wedge is path-connected), $\tilde H_1 \cong \mathbb{Z}$ and $\tilde H_2 \cong \mathbb{Z}^2$, and all other reduced groups vanish. Thus
$$H_0 \cong \mathbb{Z}, \qquad H_1 \cong \mathbb{Z}, \qquad H_2 \cong \mathbb{Z}^2, \qquad H_n = 0 \ (n \ge 3).$$
The Euler characteristic is $1 - 1 + 2 = 2$.

**15.** **Strategy.** Collapse the arc, which is a contractible subcomplex.

Let $X$ be the union of two spheres and an arc joining them. The arc is contractible, and the quotient $X \to X/A$ that collapses the arc to a point is a homotopy equivalence (the pair $(X,A)$ has $A$ contractible and is a CW pair). The quotient is $S^2 \vee S^2$. Hence
$$H_0(X) \cong \mathbb{Z}, \qquad H_2(X) \cong \mathbb{Z}^2, \qquad H_1(X) = 0, \qquad H_n(X) = 0 \ (n \ge 3).$$
The Euler characteristic is $1 + 2 = 3$. Inclusion–exclusion for the union of the two spheres and the arc gives
$$\chi(X) = \chi(S^2) + \chi(S^2) + \chi(\text{arc}) - \chi(\mathrm{pt}) - \chi(\mathrm{pt}) = 2 + 2 + 1 - 1 - 1 = 3,$$
since the arc meets each sphere in one point and the two spheres are disjoint.

**16.** **Strategy.** Use the cellular chain complex with one cell in each dimension.

$\mathbb{R}P^4$ has one cell in dimensions $0,1,2,3,4$. The cellular boundary is $d_k = 1 + (-1)^k$, so $d_1 = 0$, $d_2 = 2$, $d_3 = 0$, $d_4 = 2$. The chain complex is
$$0 \to \mathbb{Z} \xrightarrow{\ 2\ } \mathbb{Z} \xrightarrow{\ 0\ } \mathbb{Z} \xrightarrow{\ 2\ } \mathbb{Z} \xrightarrow{\ 0\ } \mathbb{Z} \to 0.$$
Then
$$H_0 = \mathbb{Z}, \quad H_1 = \frac{\ker d_1}{\operatorname{im} d_2} = \frac{\mathbb{Z}}{2\mathbb{Z}} = \mathbb{Z}/2, \quad H_2 = \frac{\ker d_2}{\operatorname{im} d_3} = 0,$$
$$H_3 = \frac{\ker d_3}{\operatorname{im} d_4} = \frac{\mathbb{Z}}{2\mathbb{Z}} = \mathbb{Z}/2, \quad H_4 = \ker d_4 = 0.$$
In general, $H_k(\mathbb{R}P^n) \cong \mathbb{Z}/2$ for $k$ odd with $1 \le k \le n-1$, $H_k \cong \mathbb{Z}$ for $k = 0$ and for $k = n$ when $n$ is odd, and $H_k = 0$ otherwise.

**17.** **Strategy.** Apply Künneth, then verify with Mayer–Vietoris.

*Künneth.* Since $H_*(S^1) = (\mathbb{Z}, \mathbb{Z})$ and $H_*(S^2) = (\mathbb{Z}, 0, \mathbb{Z})$ are free, all Tor terms vanish, and
$$H_n(S^1 \times S^2) \cong \bigoplus_{p+q=n} H_p(S^1) \otimes H_q(S^2).$$
This gives $H_0 = \mathbb{Z}$, $H_1 = \mathbb{Z}$, $H_2 = \mathbb{Z}$, $H_3 = \mathbb{Z}$, and zero otherwise.

*Mayer–Vietoris.* Write $S^2 = D^2_+ \cup D^2_-$ as the union of open upper and lower hemispheres, and put $A = S^1 \times D^2_+$, $B = S^1 \times D^2_-$. Then $A \simeq S^1$, $B \simeq S^1$, and $A \cap B = S^1 \times (\text{equatorial annulus}) \simeq S^1 \times S^1 = T^2$. The reduced sequence begins
$$\tilde H_2(A) \oplus \tilde H_2(B) \to \tilde H_2(X) \xrightarrow{\ \alpha\ } \tilde H_1(T^2) \xrightarrow{\ \beta\ } \tilde H_1(A) \oplus \tilde H_1(B) \to \tilde H_1(X) \to \tilde H_0(T^2) = 0.$$
The first term is zero. The map $\beta$ sends the two torus directions to the two circle directions, one in each summand:
$$\beta(m,n) = (m,m).$$
Hence $\ker\beta = \mathbb{Z}\cdot(1,-1) \cong \mathbb{Z}$, so $\alpha$ is an isomorphism onto $\ker\beta$ and $\tilde H_2(X) \cong \mathbb{Z}$. Next,
$$\tilde H_1(X) \cong \operatorname{coker}\beta = \frac{\mathbb{Z} \oplus \mathbb{Z}}{\langle(1,1)\rangle} \cong \mathbb{Z}.$$
In degree $3$ the sequence reads
$$0 = \tilde H_3(A) \oplus \tilde H_3(B) \to \tilde H_3(X) \to \tilde H_2(T^2) \to \tilde H_2(A) \oplus \tilde H_2(B) = 0,$$
so $\tilde H_3(X) \cong \mathbb{Z}$. Thus $H_0 = \mathbb{Z}$, $H_1 = \mathbb{Z}$, $H_2 = \mathbb{Z}$, $H_3 = \mathbb{Z}$, in agreement with Künneth. The computation shows that knowing the groups of the pieces is not enough; the maps matter.

**18.** **Strategy.** Remove a disk from $\Sigma_2$ and apply Mayer–Vietoris as for the torus.

Let $A = \Sigma_2 \setminus \{\text{point}\}$ and let $B$ be a small disk around that point. Then $A \cup B = \Sigma_2$, $A \simeq S^1 \vee S^1 \vee S^1 \vee S^1$ (a genus-$2$ surface with a point removed deformation retracts onto a wedge of $2g = 4$ circles), and $A \cap B$ is an annulus, homotopy equivalent to $S^1$. Hence
$$\tilde H_1(A) = \mathbb{Z}^4, \qquad \tilde H_2(A) = 0, \qquad \tilde H_1(A \cap B) = \mathbb{Z}.$$
The reduced Mayer–Vietoris sequence is
$$0 \to \tilde H_2(\Sigma_2) \to \tilde H_1(A \cap B) \xrightarrow{\ \partial\ } \tilde H_1(A) \to \tilde H_1(\Sigma_2) \to \tilde H_0(A \cap B) = 0.$$
The boundary circle of the disk, viewed in $A$, is the product of the four commutators corresponding to the standard presentation of $\pi_1(\Sigma_2)$. Since $H_1(A) = \mathbb{Z}^4$ is abelian, this class is zero, so $\partial = 0$. Therefore
$$\tilde H_2(\Sigma_2) \cong \mathbb{Z}, \qquad \tilde H_1(\Sigma_2) \cong \mathbb{Z}^4, \qquad \tilde H_0(\Sigma_2) = 0.$$
Thus $H_0 = \mathbb{Z}$, $H_1 = \mathbb{Z}^4$, $H_2 = \mathbb{Z}$, and $\chi(\Sigma_2) = 1 - 4 + 1 = -2$. The classification of surfaces (Theorem 7.13.1) says that the closed orientable surface of genus $2$ is the unique orientable closed surface with $\chi = -2$, since $2 - 2g = -2$ gives $g = 2$.

**19.** **Strategy.** Use the Kronecker pairing and naturality, or the universal coefficient theorem.

Let $[S^n] \in H_n(S^n;\mathbb{Z})$ be the chosen generator and let $\alpha \in H^n(S^n;\mathbb{Z})$ be the dual generator, so that $\langle\alpha,[S^n]\rangle = 1$. Naturality of the evaluation pairing gives
$$\langle f^*\alpha, [S^n]\rangle = \langle \alpha, f_*[S^n]\rangle = \langle \alpha, d[S^n]\rangle = d.$$
Since $H^n(S^n;\mathbb{Z}) \cong \mathbb{Z}$ is generated by $\alpha$, it follows that $f^*\alpha = d\alpha$. Hence $f^*$ is multiplication by $d$.

**20.** **Strategy.** Use parts (2) and (4) of Theorem 7.9.2.

If $f$ is not surjective, Theorem 7.9.2(4) gives $\deg(f) = 0$. Taking the contrapositive, $\deg(f) = 1 \ne 0$ implies that $f$ is surjective.

If $f$ were null-homotopic, it would be homotopic to a constant map, and by homotopy invariance $\deg(f) = \deg(\text{constant}) = 0$, contradiction. Hence $f$ is not null-homotopic.

The same argument works for degree $-1$: a nonzero degree implies surjectivity and non-null-homotopy. In fact every map of nonzero degree is surjective and not null-homotopic.

**21.** **Strategy.** Use the top homology of a closed connected manifold and the cellular computation for $\mathbb{R}P^n$.

A closed connected $n$-manifold $M$ is orientable iff $H_n(M;\mathbb{Z}) \cong \mathbb{Z}$; if $M$ is non-orientable, then $H_n(M;\mathbb{Z}) = 0$. (This is the orientation character of the top homology; it follows from the orientation double cover and the fact that a connected non-orientable manifold has no fundamental class over $\mathbb{Z}$.)

From Example 7.10.4,
$$
H_n(\mathbb{R}P^n;\mathbb{Z}) \cong
\begin{cases}
\mathbb{Z}, & n \text{ odd},\\
0, & n \text{ even}.
\end{cases}
$$
Therefore $\mathbb{R}P^n$ is orientable iff $n$ is odd. For $n = 1$, $\mathbb{R}P^1 \cong S^1$ is orientable; for $n = 2$, $\mathbb{R}P^2$ is non-orientable.

**22.** **Strategy.** Translate coverings into index-$2$ subgroups, then count surjections.

By Theorem 5.2.6, connected $2$-sheeted coverings of $S^1 \vee S^1$ correspond to subgroups of index $2$ in $\pi_1(S^1 \vee S^1) \cong F_2 = \langle a,b\rangle$. Such a subgroup is the kernel of a surjective homomorphism $F_2 \to \mathbb{Z}/2$. A homomorphism is determined by the images of $a$ and $b$, each of which can be $0$ or $1$. There are $2^2 = 4$ homomorphisms, and the trivial one is not surjective, so there are $3$ surjections and hence $3$ connected $2$-sheeted coverings.

The total space of such a covering is a connected graph with $V' = 2$ vertices and $E' = 4$ edges, so its Euler characteristic is $2 - 4 = -2$ and its first Betti number is $1 - \chi = 3$. Hence each total space is homotopy equivalent to $S^1 \vee S^1 \vee S^1$. The three coverings are non-isomorphic as coverings; they correspond to the three nontrivial ways of assigning the two generators to the two sheets.

**23.** **Strategy.** Use the cellular chain complex of a graph.

Give $X$ its structure as a CW complex with $V$ vertices and $E$ edges. Then $C_0 = \mathbb{Z}^V$, $C_1 = \mathbb{Z}^E$, and $C_n = 0$ for $n \ge 2$. The boundary $d_1 : \mathbb{Z}^E \to \mathbb{Z}^V$ sends an edge $e$ from $u$ to $v$ to $v - u$. Since $X$ is connected, the image of $d_1$ is exactly the subgroup of $\mathbb{Z}^V$ consisting of vectors whose coordinates sum to $0$; this subgroup has rank $V-1$. Hence
$$H_0(X) = \mathbb{Z}^V / \operatorname{im} d_1 \cong \mathbb{Z}, \qquad H_1(X) = \ker d_1 \cong \mathbb{Z}^{E - (V-1)} = \mathbb{Z}^{E-V+1},$$
and $H_n(X) = 0$ for $n \ge 2$ because the cellular chain complex vanishes there. This also gives $\chi(X) = V - E = 1 - (E - V + 1)$.

**24.** **Strategy.** Apply Künneth over $\mathbb{Q}$ and factor the alternating sum.

By Theorem 8.8 with field coefficients,
$$H_n(X \times Y;\mathbb{Q}) \cong \bigoplus_{p+q=n} H_p(X;\mathbb{Q}) \otimes_{\mathbb{Q}} H_q(Y;\mathbb{Q}).$$
Taking dimensions,
$$b_n(X \times Y) = \sum_{p+q=n} b_p(X)b_q(Y).$$
Therefore
$$\chi(X \times Y) = \sum_n (-1)^n b_n(X \times Y) = \sum_{p,q} (-1)^{p+q} b_p(X)b_q(Y) = \Bigl(\sum_p (-1)^p b_p(X)\Bigr)\Bigl(\sum_q (-1)^q b_q(Y)\Bigr) = \chi(X)\chi(Y).$$

## Advanced

**25.** **Strategy.** Induct on $n$ using the cover of $S^n$ by two hemispheres and the reduced Mayer–Vietoris sequence.

*Base case $n = 0$.* $S^0$ is two points, so $H_0(S^0) = \mathbb{Z}^2$ and $\tilde H_0(S^0) = \mathbb{Z}$; all higher groups vanish. This is the statement for $n = 0$.

*Inductive step.* Assume the result for $S^{n-1}$ with $n \ge 1$. Let $N,S$ be antipodal points and put
$$A = S^n \setminus \{N\}, \qquad B = S^n \setminus \{S\}.$$
Stereographic projection gives homeomorphisms $A \cong \mathbb{R}^n$ and $B \cong \mathbb{R}^n$, so $A$ and $B$ are contractible and their reduced homology vanishes in every degree. The intersection $A \cap B = S^n \setminus \{N,S\}$ is homeomorphic to $S^{n-1} \times \mathbb{R}$, which deformation retracts onto $S^{n-1}$; hence $\tilde H_k(A \cap B) \cong \tilde H_k(S^{n-1})$ for all $k$.

The reduced Mayer–Vietoris sequence (Theorem 8.4) gives, for every $k \ge 1$,
$$\tilde H_k(A) \oplus \tilde H_k(B) \to \tilde H_k(S^n) \to \tilde H_{k-1}(A \cap B) \to \tilde H_{k-1}(A) \oplus \tilde H_{k-1}(B).$$
The outer groups vanish, so
$$\tilde H_k(S^n) \cong \tilde H_{k-1}(A \cap B) \cong \tilde H_{k-1}(S^{n-1}).$$
By the induction hypothesis, $\tilde H_{k-1}(S^{n-1}) \cong \mathbb{Z}$ when $k-1 = n-1$, that is $k = n$, and vanishes otherwise. Hence $\tilde H_n(S^n) \cong \mathbb{Z}$ and $\tilde H_k(S^n) = 0$ for $k \ne n$, $k \ge 1$. Finally $S^n$ is path-connected for $n \ge 1$, so $\tilde H_0(S^n) = 0$. This completes the induction. The hypotheses used are that $A$ and $B$ are open, that $S^n = A \cup B$, and that $A \cap B$ is nonempty; all hold.

**26.** **Strategy.** Prove each implication separately.

*(ii) $\Rightarrow$ (i).* Suppose there is a fixed-point-free continuous $f : D^n \to D^n$. For $x \in D^n$, the points $f(x)$ and $x$ are distinct, so the ray from $f(x)$ through $x$ meets $S^{n-1}$ in a unique point $r(x)$ beyond $x$. The formula
$$r(x) = x + t(x)(x - f(x)), \qquad t(x) = \frac{-b + \sqrt{b^2 - 4ac}}{2a},$$
with $a = |x-f(x)|^2 > 0$, $b = 2\langle x, x-f(x)\rangle$, $c = |x|^2-1 \le 0$, defines a continuous map $D^n \to S^{n-1}$. If $|x| = 1$, then $c = 0$ and $b \ge 0$, so $t(x) = 0$ and $r(x) = x$. Hence $r$ is a retraction, contradicting (ii). Therefore (i) holds.

*(i) $\Rightarrow$ (ii).* Suppose there is a retraction $r : D^n \to S^{n-1}$. Define $f : D^n \to D^n$ by $f(x) = -r(x)$. This is continuous and maps into $S^{n-1} \subset D^n$. If $x$ were a fixed point, then $x = -r(x)$, so $x \in S^{n-1}$ and $r(x) = x$ (because $r$ is a retraction). Hence $x = -x$, so $x = 0$, contradicting $x \in S^{n-1}$. Thus $f$ is fixed-point-free, contradicting (i). Therefore (ii) holds.

Both implications are proved, so the statements are equivalent.

**27.** **Strategy.** Compute the traces on $H_0,H_1,H_2$ and interpret fixed points as the kernel of $A-I$ on the torus.

*Lefschetz number.* The homology of $T^2$ is $H_0 = \mathbb{Z}$, $H_1 = \mathbb{Z}^2$, $H_2 = \mathbb{Z}$. The map $f_A$ acts as the identity on $H_0$, as $A$ on $H_1$, and as multiplication by $\det A$ on $H_2$ (because it multiplies the fundamental class by the determinant). Hence
$$L(f_A) = 1 - \operatorname{tr} A + \det A = \det(I-A),$$
using $\det(I-A) = 1 - \operatorname{tr} A + \det A$ for a $2 \times 2$ matrix.

*Fixed points.* A point $x \in T^2 = \mathbb{R}^2/\mathbb{Z}^2$ is fixed iff $(A-I)x \in \mathbb{Z}^2$. If $B = A-I$ is invertible, the induced map $B : T^2 \to T^2$ has kernel $B^{-1}\mathbb{Z}^2/\mathbb{Z}^2 \cong \mathbb{Z}^2/B\mathbb{Z}^2$, whose order is $|\det B| = |\det(I-A)|$. Hence $f_A$ has exactly $|\det(I-A)|$ fixed points.

**28.** **Strategy.** Use rank–nullity and telescoping, as in Theorem 7.12.2.

Let $Z_i = \ker\partial_i$ and $B_i = \operatorname{im}\partial_{i+1}$. The map $\partial_i : C_i \to C_{i-1}$ has image $B_{i-1}$ and kernel $Z_i$, so
$$\dim C_i = \dim Z_i + \dim B_{i-1}.$$
Also $H_i = Z_i/B_i$, so
$$\dim Z_i = \dim H_i + \dim B_i.$$
Substituting,
$$\dim C_i = \dim H_i + \dim B_i + \dim B_{i-1}.$$
Multiply by $(-1)^i$ and sum over $i$. The terms involving $B$ cancel in pairs:
$$\sum_i (-1)^i \dim C_i = \sum_i (-1)^i \dim H_i + \sum_i (-1)^i \dim B_i + \sum_i (-1)^i \dim B_{i-1} = \sum_i (-1)^i \dim H_i,$$
because $\sum_i (-1)^i \dim B_{i-1} = -\sum_j (-1)^j \dim B_j$. The sums are finite because the complex is finite.

**29.** **Strategy.** Use the homotopy invariance of the Lefschetz number and the Lefschetz theorem.

If $f \simeq \operatorname{id}_X$, then $L(f) = L(\operatorname{id}_X)$ by homotopy invariance. On $H_i(X;\mathbb{Q})$ the identity map has trace $b_i$, so
$$L(\operatorname{id}_X) = \sum_i (-1)^i b_i = \chi(X) \ne 0.$$
By the Lefschetz fixed point theorem (Theorem 7.13.3), $f$ has a fixed point.

**30.** **Strategy.** Apply the Lefschetz theorem to a fixed-point-free map, then give counterexamples to the converse.

If $f$ has no fixed point, then the Lefschetz number must vanish: otherwise Theorem 7.13.3 would produce a fixed point. For $S^n$, $H_0 = \mathbb{Z}$ and $H_n = \mathbb{Z}$ are the only nonzero groups, and $f_*$ is the identity on $H_0$ and multiplication by $\deg(f)$ on $H_n$. Hence
$$0 = L(f) = 1 + (-1)^n \deg(f),$$
so $\deg(f) = -(-1)^n = (-1)^{n+1}$.

The converse fails. For odd $n$, the identity has degree $1 = (-1)^{n+1}$ and has every point fixed. For even $n$, a reflection has degree $-1 = (-1)^{n+1}$ and fixes the equator. Thus the degree condition is necessary but not sufficient for being fixed-point-free.

**31.** **Strategy.** Use the universal coefficient theorem over the field $\mathbb{Q}$, then Künneth.

Over a field $k$, $\operatorname{Ext}^1_k$ vanishes, so Theorem 8.7 gives
$$H^n(X;k) \cong \operatorname{Hom}_k(H_n(X;k),k).$$
Taking $k = \mathbb{Q}$ gives the first claim.

For $T^2 \times S^2$, the Künneth formula over $\mathbb{Q}$ gives
$$H_n(T^2 \times S^2;\mathbb{Q}) \cong \bigoplus_{p+q=n} H_p(T^2;\mathbb{Q}) \otimes H_q(S^2;\mathbb{Q}).$$
With $b_*(T^2) = (1,2,1)$ and $b_*(S^2) = (1,0,1)$, the dimensions are
$$b_0 = 1, \quad b_1 = 2, \quad b_2 = 1\cdot1 + 2\cdot0 + 1\cdot1 = 2, \quad b_3 = 2, \quad b_4 = 1.$$
Thus $(b_0,b_1,b_2,b_3,b_4) = (1,2,2,2,1)$ and $\chi = 1 - 2 + 2 - 2 + 1 = 0 = \chi(T^2)\chi(S^2)$.

**32.** **Strategy.** Show that the deck group acts simply transitively on the fibre.

Let $p : E \to B$ be a covering, $B$ path-connected, $E$ simply connected, and fix $e_0 \in E$ with $b_0 = p(e_0)$. Let $F = p^{-1}(b_0)$.

*Transitivity.* Let $e \in F$. For each $y \in E$, choose a path $\alpha$ in $E$ from $e_0$ to $y$ and let $\beta$ be the unique lift of $p \circ \alpha$ starting at $e$ (Theorem 5.2.2). Define $\tau(y) = \beta(1)$. If $\alpha'$ is another path from $e_0$ to $y$, then $\alpha * \bar\alpha'$ is a loop in $E$ based at $e_0$, hence null-homotopic because $E$ is simply connected. Lifting the null-homotopy shows that the lifts of $p \circ \alpha$ and $p \circ \alpha'$ starting at $e$ have the same endpoint. Thus $\tau$ is well defined. Local triviality and path lifting show that $\tau$ is continuous; the same construction with $e$ and $e_0$ interchanged gives a continuous inverse. Hence $\tau$ is a deck transformation with $\tau(e_0) = e$.

*Faithfulness.* If $\tau(e_0) = e_0$, then $\tau$ and the identity are two lifts of $p$ that agree at $e_0$; by uniqueness of lifts on a connected space, $\tau = \operatorname{id}_E$.

Therefore the action is simply transitive, so $\operatorname{Deck}(E/B) \cong F$ as sets. The fibre is in bijection with $\pi_1(B,b_0)/p_*\pi_1(E,e_0)$ (each coset corresponds to the endpoint of the lift of a loop), and $p_*\pi_1(E,e_0) = 1$ because $E$ is simply connected. Hence $\operatorname{Deck}(E/B) \cong \pi_1(B,b_0)$. The subgroup is trivial, hence normal, so the covering is normal.

## Challenge

**33.** **Strategy.** Prove the Hopf trace formula for a chain map, then apply it to a simplicial map with no fixed simplex.

*Hopf trace formula.* Let $C_*$ be a finite chain complex of finite-dimensional $\mathbb{Q}$-vector spaces and let $f : C_* \to C_*$ be a chain map. Put $Z_i = \ker\partial_i$, $B_i = \operatorname{im}\partial_{i+1}$. Since $f$ is a chain map, $f(Z_i) \subseteq Z_i$ and $f(B_i) \subseteq B_i$. The sequences
$$0 \to Z_i \to C_i \to B_{i-1} \to 0, \qquad 0 \to B_i \to Z_i \to H_i \to 0$$
are exact and $f$-equivariant. For an endomorphism of a finite-dimensional vector space preserving a subspace, the trace is the sum of the traces on the subspace and the quotient: choose a basis adapted to the subspace, so the matrix is block upper triangular. Hence
$$\operatorname{tr}(f \mid C_i) = \operatorname{tr}(f \mid Z_i) + \operatorname{tr}(f \mid B_{i-1}), \qquad \operatorname{tr}(f \mid Z_i) = \operatorname{tr}(f \mid H_i) + \operatorname{tr}(f \mid B_i).$$
Substituting and taking the alternating sum, the $B$-terms cancel, giving
$$\sum_i (-1)^i \operatorname{tr}(f \mid C_i) = \sum_i (-1)^i \operatorname{tr}(f \mid H_i) = L(f).$$

*Simplicial maps.* Let $K$ be a finite simplicial complex and let $f : K \to K$ be simplicial. Then $f$ induces a chain map $f_\#$ on the simplicial chain complex with basis the oriented $i$-simplices. If $f$ has no fixed simplex, then for every $i$-simplex $\sigma$, the simplex $f(\sigma)$ is different from $\sigma$. Hence the coefficient of $\sigma$ in $f_\#(\sigma)$ is $0$ (the only way it could be nonzero is $f(\sigma) = \sigma$ with the same orientation or the opposite orientation, and the latter is still a fixed simplex). Thus the matrix of $f_\#$ in the simplex basis has zero diagonal, so $\operatorname{tr}(f_\# \mid C_i) = 0$ for every $i$. The Hopf trace formula gives $L(f) = 0$.

*Continuous maps.* Let $X$ be compact triangulable and let $f : X \to X$ be continuous with no fixed point. A standard consequence of the simplicial approximation theorem is that, after subdividing sufficiently finely, there is a simplicial map $g : K \to K$ homotopic to $f$ with no fixed simplex. (Choose a subdivision whose mesh is smaller than the minimum of the positive continuous function $x \mapsto d(x,f(x))$ on the compact set $X$, and then choose a simplicial approximation.) Hence $L(g) = 0$ by the previous paragraph. Since $g \simeq f$, $L(g) = L(f)$, so $L(f) = 0$. Taking the contrapositive, $L(f) \ne 0$ implies that $f$ has a fixed point.

**34.** **Strategy.** Write down the cellular chain complex and compute its homology.

The action of $\mathbb{Z}/p$ on $S^3$ is free: if $\zeta^k z_1 = z_1$ and $\zeta^k z_2 = z_2$ with $\zeta^k \ne 1$, then $z_1 = z_2 = 0$, which is not on the sphere. The quotient $L(p,1)$ inherits a CW structure with one cell in each dimension $0,1,2,3$: the sphere $S^3$ is the join $S^1 * S^1$, and the cells of the join are the joins of the cells of the two circles, giving one cell in each dimension. The action preserves this cell structure and acts freely, so the quotient has one cell in each dimension.

Let $C_k = \mathbb{Z}$ for $k = 0,1,2,3$. The $1$-skeleton is a circle, so $d_1 = 0$. The $2$-cell attaches to the $1$-skeleton by a map of degree $p$: the boundary of the $2$-cell is the orbit of the attaching circle under the $\mathbb{Z}/p$ action, which wraps $p$ times around the $1$-skeleton. Hence $d_2 = p$. The $3$-cell attaches along the $2$-skeleton by a map whose degree is $0$; equivalently, $L(p,1)$ is a closed orientable $3$-manifold (the action preserves the orientation of $S^3$), so $H_3(L) = \mathbb{Z}$, and since $C_4 = 0$ this forces $d_3 = 0$. The chain complex is
$$0 \to \mathbb{Z} \xrightarrow{\ 0\ } \mathbb{Z} \xrightarrow{\ p\ } \mathbb{Z} \xrightarrow{\ 0\ } \mathbb{Z} \to 0.$$
Therefore
$$H_0 = \mathbb{Z}, \qquad H_1 = \ker d_1/\operatorname{im} d_2 = \mathbb{Z}/p\mathbb{Z}, \qquad H_2 = \ker d_2/\operatorname{im} d_3 = 0, \qquad H_3 = \ker d_3 = \mathbb{Z}.$$
Replacing $\zeta$ by another primitive $p$-th root $\zeta^a$ with $\gcd(a,p)=1$ gives the same cyclic subgroup of $U(2)$ (because $\langle \zeta^a\rangle = \langle \zeta\rangle$), hence the same quotient. Thus the homology is independent of the choice of generator.

**35.** **Strategy.** Use the Künneth theorem for cohomology and induction on the number of circle factors.

Since $H^*(S^1;\mathbb{Z}) = \mathbb{Z} \oplus \mathbb{Z}\alpha$ with $\alpha^2 = 0$ is torsion-free, the cohomology Künneth theorem gives a ring isomorphism
$$H^*(T^3;\mathbb{Z}) \cong H^*(S^1;\mathbb{Z})^{\otimes 3} \cong \Lambda_{\mathbb{Z}}(\alpha,\beta,\gamma),$$
where $\alpha,\beta,\gamma$ are the pullbacks of the generator of $H^1(S^1)$ under the three projections. The exterior algebra has basis the products of distinct generators:
$$1, \quad \alpha, \beta, \gamma, \quad \alpha\beta, \alpha\gamma, \beta\gamma, \quad \alpha\beta\gamma,$$
in degrees $0,1,2,3$. Hence $H^0 = \mathbb{Z}$, $H^1 = \mathbb{Z}^3$, $H^2 = \mathbb{Z}^3$, $H^3 = \mathbb{Z}$.

The product is associative and satisfies $\alpha^2 = \beta^2 = \gamma^2 = 0$ and
$$\alpha\beta = -\beta\alpha, \qquad \alpha\gamma = -\gamma\alpha, \qquad \beta\gamma = -\gamma\beta.$$
For example, $\alpha\beta$ and $\beta\alpha$ are opposite generators of $H^2$. The ring is not commutative in the ordinary sense: $\alpha\beta \ne \beta\alpha$, since $\alpha\beta = -\beta\alpha$ and $2\alpha\beta \ne 0$ (it is a generator of a free abelian group). It is graded-commutative, as Theorem 7.11.3 predicts.

**36.** **Strategy.** Derive the Wang sequence from Mayer–Vietoris, split the resulting long exact sequence over $\mathbb{Q}$, and compute.

*(a) Wang sequence.* Write $T_f$ as the union of the images of $X \times [0,1/2]$ and $X \times [1/2,1]$; both are homotopy equivalent to $X$, and their intersection is a copy of $X$. The Mayer–Vietoris sequence, with the identifications at the two ends given by $f$, yields
$$\cdots \to H_n(X;\mathbb{Q}) \xrightarrow{\ f_* - \operatorname{id}\ } H_n(X;\mathbb{Q}) \to H_n(T_f;\mathbb{Q}) \to H_{n-1}(X;\mathbb{Q}) \xrightarrow{\ f_* - \operatorname{id}\ } H_{n-1}(X;\mathbb{Q}) \to \cdots.$$

*(b) Splitting.* Over $\mathbb{Q}$ every vector space is injective and every short exact sequence splits. The long exact sequence therefore decomposes into short exact sequences
$$0 \to \operatorname{coker}(f_* - \operatorname{id} \mid H_n) \to H_n(T_f) \to \ker(f_* - \operatorname{id} \mid H_{n-1}) \to 0,$$
and these split, giving
$$H_n(T_f;\mathbb{Q}) \cong \operatorname{coker}(f_* - \operatorname{id} \mid H_n(X;\mathbb{Q})) \oplus \ker(f_* - \operatorname{id} \mid H_{n-1}(X;\mathbb{Q})).$$

*(c) Antipodal map on $S^2$.* The map $f$ acts as the identity on $H_0(S^2;\mathbb{Q}) = \mathbb{Q}$ and as multiplication by $-1$ on $H_2(S^2;\mathbb{Q}) = \mathbb{Q}$, and $H_1 = 0$. Hence
$$H_0(T_f) \cong \operatorname{coker}(0) \oplus 0 = \mathbb{Q}, \qquad H_1(T_f) \cong 0 \oplus \ker(0 \text{ on } H_0) = \mathbb{Q},$$
$$H_2(T_f) \cong \operatorname{coker}(-2) \oplus \ker(0 \text{ on } H_1) = 0, \qquad H_3(T_f) \cong 0 \oplus \ker(-2) = 0.$$
Thus $H_*(T_f;\mathbb{Q}) = (\mathbb{Q},\mathbb{Q},0,0)$, and $\chi(T_f) = 1 - 1 = 0$, as required for a closed $3$-manifold.
