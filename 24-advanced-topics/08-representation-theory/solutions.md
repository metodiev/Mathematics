# Representation Theory — Solutions

> [Representation Theory](README.md) · Solutions to the 36 problems in [exercises.md](exercises.md)

Each solution begins with the strategy, carries out every significant step, and closes with a check.
Orthogonality computations quote Theorem 7.21 for rows and Theorem 7.23 for columns; "norm" always means
$\langle\chi,\chi\rangle_G$.

## Beginner

**1.** *Strategy: write the rotation matrix for $120^\circ$, check the defining relation
$\rho(r)^3 = I$, and read the character off the diagonal.*

With $c = \cos 120^\circ = -\tfrac12$ and $s = \sin 120^\circ = \tfrac{\sqrt3}{2}$,

$$\rho(r) = \begin{pmatrix} c & -s\\ s & c\end{pmatrix}
= \begin{pmatrix} -\tfrac12 & -\tfrac{\sqrt3}{2}\\ \tfrac{\sqrt3}{2} & -\tfrac12\end{pmatrix}.$$

Rotation by $120^\circ$ composes additively, and $\rho(r)^3 = R_{360^\circ} = I$, so $r\mapsto\rho(r)$
respects the only relation of $C_3$ and is a homomorphism. The trace is
$\chi(e) = 2$, $\chi(r) = \operatorname{tr}\rho(r) = 2c = -1$, and
$\chi(r^2) = 2\cos 240^\circ = -1$. Then

$$\langle\chi,\chi\rangle = \tfrac13\bigl(2^2 + (-1)^2 + (-1)^2\bigr) = \tfrac{6}{3} = 2 \ne 1,$$

so the complexification is reducible. The eigenvalues of $\rho(r)$ are
$e^{\pm 2\pi i/3} = \omega_3^{\pm1}$, so over $\mathbb{C}$ the two eigenlines are invariant and
$\rho\cong\chi_1\oplus\chi_2$ with $\chi_k(r) = \omega_3^{k}$; indeed
$(\chi_1+\chi_2)(r) = \omega_3+\omega_3^2 = -1$. Over $\mathbb{R}$, by contrast, there is no real
eigenline and the representation is irreducible (Example 7.5).

**2.** *Strategy: act on the basis by left multiplication and write down the permutation matrices.*

In the basis $(e, r, r^2)$, left multiplication by $r$ sends $e\mapsto r$, $r\mapsto r^2$, $r^2\mapsto e$;
so the matrix has a $1$ in position (row, column) $(r,e)$, $(r^2,r)$, $(e,r^2)$:

$$\rho_{\mathrm{reg}}(e) = I,\qquad
\rho_{\mathrm{reg}}(r) = \begin{pmatrix}0&0&1\\1&0&0\\0&1&0\end{pmatrix},\qquad
\rho_{\mathrm{reg}}(r^2) = \begin{pmatrix}0&1&0\\0&0&1\\1&0&0\end{pmatrix}.$$

The traces are $3, 0, 0$, i.e. $\chi_{\mathrm{reg}} = (3,0,0)$. This is forced by Theorem 7.30: the
permutation matrix of left multiplication by $g$ has a $1$ on the diagonal exactly when $gh = h$ for some
$h$, i.e. $g = e$. Hence the answer depends only on $\lvert G\rvert$, not on the group. Check:
$\langle\chi_{\mathrm{reg}},\chi_{\mathrm{reg}}\rangle = \frac13\cdot 9 = 3 = 1^2+1^2+1^2$, the sum of
squared multiplicities of the three characters of $C_3$ in $\mathbb{C}[C_3]$.

**3.** *Strategy: count fixed vertices for one representative of each class, then apply the multiplicity
formula with the $D_4$ table of Example 9.4.*

Number the vertices $1,2,3,4$ cyclically, so $r = (1234)$. Then $r$ and $r^3$ fix nothing; $r^2 = (13)(24)$
fixes nothing; $s$ (reflection in a diagonal) fixes two vertices, as does $r^2s$; $rs$ and $r^3s$
(reflections in axes through edge midpoints) fix none. Hence

$$\chi_{\mathrm{perm}} = (4,\ 0,\ 0,\ 2,\ 0)$$

on the classes $(e,\ r^2,\ \{r,r^3\},\ \{s,r^2s\},\ \{rs,r^3s\})$. With sizes $1,1,2,2,2$:

$$m_{A_1} = \tfrac18(4+0+0+4+0) = 1,\quad m_{A_2} = \tfrac18(4+0+0-4+0) = 0,$$
$$m_{B_1} = \tfrac18(4+0+0+4+0) = 1,\quad m_{B_2} = \tfrac18(4+0+0-4+0) = 0,\quad
m_E = \tfrac18(4\cdot2 + 0) = 1.$$

So the permutation representation is $A_1\oplus B_1\oplus E$, of dimension $1+1+2 = 4$. Check pointwise:
$A_1+B_1+E = (1+1+2,\ 1+1-2,\ 1-1+0,\ 1+1+0,\ 1-1+0) = (4,0,0,2,0)$. The $B_1$ summand is spanned by the
"checkerboard" vector $e_1-e_2+e_3-e_4$, which is invariant under $r^2$ and $s$ and changes sign under
$r$.

**4.** *Strategy: a one-dimensional representation is a homomorphism into $\mathbb{C}^{\times}$, so
invertibility and modulus are immediate.*

Since $\chi : G\to\mathbb{C}^{\times}$ is a homomorphism, $\chi(g)\chi(g^{-1}) = \chi(e) = 1$, hence
$\chi(g^{-1}) = \chi(g)^{-1}$. Also $\chi(g)$ has finite order dividing $\operatorname{ord}(g)$, so it is
a root of unity and $\chi(g)^{-1} = \overline{\chi(g)}$. For $C_4$ with $\chi_1(r) = i$:
$\chi_1(r^{-1}) = \chi_1(r^3) = i^3 = -i = \overline{i}$ ✓. More generally the identity holds for every
representation because the eigenvalues of $\rho(g)$ are roots of unity (Proposition 7.16(3)).

**5.** *Strategy: apply the definition of the inner product, weighting by class sizes.*

$$\langle\chi,\chi\rangle = \frac{1}{6}\Bigl(3^2\cdot1 + 1^2\cdot3 + 0^2\cdot2\Bigr)
= \frac{9+3}{6} = 2.$$

A character has norm $\sum_i m_i^2$ (Corollary 7.22). The value $2 = 1^2+1^2$ is consistent with two
distinct irreducibles occurring once each, which is exactly $\mathbb{1}\oplus\chi_3$ (dimensions
$1+2 = 3$). It is *not* consistent with $\chi$ being irreducible (norm $1$) or with a single irreducible
of multiplicity $\sqrt2$.

**6.** *Strategy: expand the sums, using the class sizes $1,3,2$ and the table.*

$$\langle\chi_3,\chi_3\rangle = \frac16\Bigl(2\cdot\overline2 + 3\cdot0\cdot\overline0
+ 2\cdot(-1)\overline{(-1)}\Bigr) = \frac{4+0+2}{6} = 1,$$

$$\langle\chi_1,\chi_3\rangle = \frac16\Bigl(1\cdot\overline2 + 3\cdot1\cdot\overline0
+ 2\cdot1\cdot\overline{(-1)}\Bigr) = \frac{2+0-2}{6} = 0.$$

Both agree with Theorem 7.21. As a further check,
$\langle\chi_2,\chi_3\rangle = \frac16(1\cdot2 + 3\cdot(-1)\cdot0 + 2\cdot1\cdot(-1)) = 0$.

**7.** *Strategy: verify invariance directly and solve the fixed-point equations.*

If $v\in V^G$ and $h\in G$ then $\rho(h)v = v$, so $\rho(g)(\rho(h)v) = \rho(gh)v = v$; hence
$\rho(g)v\in V^G$ for every $g$. For the permutation representation of $S_3$ on $\mathbb{C}^3$, a vector
$x$ is fixed by all permutations iff $x_1 = x_2 = x_3$, so $V^{G} = \mathbb{C}\cdot(1,1,1)$. Its dimension
is the multiplicity of the trivial representation, which is $\langle\chi_{\mathrm{perm}},\mathbb{1}\rangle
= \frac16(3+3+0) = 1$, as it must be for a transitive action.

**8.** *Strategy: dualise twice and compute the eigenvalues of the contragredient.*

The dual of the dual is canonically isomorphic to $V$, $V^{**}\cong V$, and the isomorphism is natural,
hence $G$-equivariant; so $V\mapsto V^{*}$ is an involution on isomorphism classes. For the rotation
representation of $C_4$, $\rho(r)$ has eigenvalues $i,-i$, hence $\rho^{*}(r) = \rho(r^{-1})$ has the same
eigenvalues $i^{-1} = -i$ and $(-i)^{-1} = i$; the trace is $0$ either way. Explicitly
$\chi_{V^{*}} = \overline{(2,0,-2,0)} = (2,0,-2,0) = \chi_V$, consistent with $V\cong V^{*}$ (the
rotation matrices are real orthogonal, hence self-dual).

**9.** *Strategy: use $\chi_{\mathrm{reg}} = \lvert G\rvert\delta_e$ and the multiplicity formula.*

$\chi_{\mathrm{reg}}(e) = 5$ and $\chi_{\mathrm{reg}}(r^j) = 0$ for $j = 1,2,3,4$. The multiplicity of
$\chi_k$ is $m_k = \frac15\sum_j\chi_{\mathrm{reg}}(r^j)\overline{\chi_k(r^j)} = \frac15\cdot5\cdot1 = 1$
for each $k = 0,\dots,4$. Hence $\mathbb{C}[C_5]\cong\chi_0\oplus\chi_1\oplus\chi_2\oplus\chi_3\oplus
\chi_4$ and $\sum_k m_k^2 = 5 = \lvert C_5\rvert$ ✓, in agreement with Theorem 7.31 since all $d_k = 1$.

**10.** *Strategy: compute the norm; a character has integer norm equal to a sum of squares.*

For $\chi = (2,0,-1)$: $\langle\chi,\chi\rangle = \frac16(4 + 3\cdot0 + 2\cdot1) = 1$, so $\chi$ is
irreducible (and indeed it is $\chi_3$ of the $S_3$ table).

For $\psi = (2,1,-2)$: $\langle\psi,\psi\rangle = \frac16(4 + 3\cdot1 + 2\cdot4)
= \frac{15}{6} = \frac52$. This is not an integer, while every genuine character has
$\langle\chi,\chi\rangle = \sum_i m_i^2\in\mathbb{Z}$. So $\psi$ is not the character of any
representation. (Equivalently, no decomposition into irreducible characters can reproduce it, since any
such decomposition forces a half-integral coefficient.)

**11.** *Strategy: a diagonal matrix preserves the coordinate axes.*

$\rho(s)e_1 = e_1$ and $\rho(s)e_2 = -e_2$, so $L_1 = \mathbb{C}e_1$ and $L_2 = \mathbb{C}e_2$ are
invariant lines and $\mathbb{C}^2 = L_1\oplus L_2$. The representation is $\chi_+\oplus\chi_-$ where
$\chi_\pm(s) = \pm1$; its character is $(2, 0)$ on $(e,s)$ and
$\langle\chi,\chi\rangle = \frac12(4+0) = 2 = 1^2+1^2$ ✓. Hence it is reducible, and because a complement
exists it is also decomposable — as Maschke's theorem guarantees over $\mathbb{C}$.

**12.** *Strategy: use the character-level multiplication in $R(S_3)$, i.e. pointwise products of the
table entries.*

$[\varepsilon]\cdot[\chi_3]$ has character $\varepsilon\chi_3 = (1\cdot2,\ (-1)\cdot0,\ 1\cdot(-1)) =
(2,0,-1) = \chi_3$. So tensoring with a one-dimensional representation does not change $\chi_3$ up to
isomorphism.

$[\chi_3]^2$ has character $(4, 0, 1) = \chi_1+\chi_2+\chi_3$ (Example 7.27).

Associativity: $([\mathbb{1}]+[\varepsilon])\cdot[\chi_3] = [\chi_3]+[\varepsilon\chi_3] = 2[\chi_3]$;
multiplying by $[\chi_3]$ again gives $2[\chi_3]^2 = 2([\mathbb{1}]+[\varepsilon]+[\chi_3])$. In the other
order, $[\chi_3]\cdot[\chi_3] = [\mathbb{1}]+[\varepsilon]+[\chi_3]$, and multiplying by
$[\mathbb{1}]+[\varepsilon]$ gives
$([\mathbb{1}]+[\varepsilon]) + ([\varepsilon]+[\mathbb{1}]) + ([\chi_3]+[\varepsilon\chi_3])
= 2[\mathbb{1}]+2[\varepsilon]+2[\chi_3]$ ✓.

## Intermediate

**13.** *Strategy: write $G = \langle a\rangle\times\langle b\rangle$ with $a^3 = b^3 = e$ and use the
product rule $\chi_{jk}(a^ib^l) = \omega_3^{ji}\omega_3^{kl}$.*

The nine elements and nine characters:

| $C_3\times C_3$ | $e$ | $a$ | $a^2$ | $b$ | $ab$ | $a^2b$ | $b^2$ | $ab^2$ | $a^2b^2$ |
|---|---|---|---|---|---|---|---|---|---|
| $\chi_{00}$ | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| $\chi_{10}$ | 1 | $\omega$ | $\omega^2$ | 1 | $\omega$ | $\omega^2$ | 1 | $\omega$ | $\omega^2$ |
| $\chi_{20}$ | 1 | $\omega^2$ | $\omega$ | 1 | $\omega^2$ | $\omega$ | 1 | $\omega^2$ | $\omega$ |
| $\chi_{01}$ | 1 | 1 | 1 | $\omega$ | $\omega$ | $\omega$ | $\omega^2$ | $\omega^2$ | $\omega^2$ |
| $\chi_{11}$ | 1 | $\omega$ | $\omega^2$ | $\omega$ | $\omega^2$ | 1 | $\omega^2$ | 1 | $\omega$ |
| $\chi_{21}$ | 1 | $\omega^2$ | $\omega$ | $\omega$ | 1 | $\omega^2$ | $\omega^2$ | $\omega$ | 1 |
| $\chi_{02}$ | 1 | 1 | 1 | $\omega^2$ | $\omega^2$ | $\omega^2$ | $\omega$ | $\omega$ | $\omega$ |
| $\chi_{12}$ | 1 | $\omega$ | $\omega^2$ | $\omega^2$ | 1 | $\omega$ | $\omega$ | $\omega^2$ | 1 |
| $\chi_{22}$ | 1 | $\omega^2$ | $\omega$ | $\omega^2$ | $\omega$ | 1 | $\omega$ | 1 | $\omega^2$ |

with $\omega = \omega_3$. Row orthogonality: for $\chi_{10}$ and $\chi_{11}$ the pointwise product with
the conjugate is $\chi_{10}\overline{\chi_{11}} = \chi_{10}\chi_{22} = \chi_{02}$ (using
$\overline{\chi_{jk}} = \chi_{-j,-k} = \chi_{3-j,3-k}$), which is a nontrivial character; hence
$\sum_g\chi_{02}(g) = 0$ and $\langle\chi_{10},\chi_{11}\rangle = 0$ ✓. Each row has norm
$\frac19\cdot 9 = 1$ because all entries are roots of unity.

Column orthogonality at $e$ and $a$: $\sum_{j,k}\chi_{jk}(e)\overline{\chi_{jk}(a)}
= \sum_{j,k}\omega^{-j} = \bigl(\sum_j\omega^{-j}\bigr)\bigl(\sum_k1\bigr) = 0\cdot3 = 0$ ✓, and the
column at $e$ has sum of squares $9 = \lvert G\rvert$ ✓.

**14.** *Strategy: compute the two inner products and use the additivity and norm formula.*

$$\langle\chi,\chi\rangle = \frac{1}{24}\Bigl(4^2 + 6\cdot2^2 + 3\cdot0^2 + 8\cdot1^2 + 6\cdot0^2\Bigr)
= \frac{16+24+8}{24} = 2,$$

$$\langle\chi,\mathbb{1}\rangle = \frac{1}{24}\bigl(4 + 6\cdot2 + 0 + 8\cdot1 + 0\bigr)
= \frac{24}{24} = 1.$$

The permutation representation contains the trivial representation once (transitivity), so by Maschke
$\chi = \mathbb{1} + \chi_V$ with $V = \{x : \sum x_i = 0\}$ and $\dim V = 3$. Then
$\langle\chi_V,\chi_V\rangle = \langle\chi,\chi\rangle - 2\langle\chi,\mathbb{1}\rangle
+ \langle\mathbb{1},\mathbb{1}\rangle = 2-2+1 = 1$, so $V$ is irreducible. This avoids computing the
whole table: the norm of the permutation character already determines the norm of the complement. The
same argument shows that for any $n$, the standard representation of $S_n$ satisfies
$\langle\chi_{\mathrm{std}},\chi_{\mathrm{std}}\rangle = \langle\chi_{\mathrm{perm}},\chi_{\mathrm{perm}}
\rangle - 1$, which equals $1$ iff the action on ordered pairs has two orbits.

**15.** *Strategy: use Theorem 7.40 with $H = \{e,(12)\}$ and the trivial character.*

The index is $[S_3:H] = 3$. For $g = e$ every $x$ contributes $1$, so $\chi(e) = \frac12\cdot6 = 3$. For
$g = (12)$, $x^{-1}gx\in H$ iff $x$ centralises $(12)$, i.e. $x\in H$, giving
$\chi = \frac12(1+1) = 1$. For $g$ a $3$-cycle no conjugate lies in $H$, so $\chi = 0$. Hence
$\chi = (3,1,0) = \chi_1+\chi_3$: the induced representation is the permutation representation on
$S_3/C_2$, that is, the trivial plus the standard representation. Frobenius reciprocity confirms:
$\langle\chi_{\mathrm{Ind}},\chi_3\rangle = \langle\mathbb{1}_H,\chi_3|_H\rangle = 1$, since
$\chi_3|_H = (2,0)$ and $\langle\mathbb{1},(2,0)\rangle_H = \frac12(2+0) = 1$ ✓.

**16.** *Strategy: characters of a direct product are products of characters of the factors, and
$C_2\times C_4$ has eight of them.*

Write elements as $a^ib^l$ with $a^2 = b^4 = e$; characters are $\chi_{jk}(a^ib^l) = (-1)^{ji}i^{kl}$ for
$j\in\{0,1\}$, $k\in\{0,1,2,3\}$. For example $\chi_{11}(a^ib^l) = (-1)^{i}i^{l}$. Orthogonality of
$\chi_{11}$ and $\chi_{01}$:
$\chi_{11}\overline{\chi_{01}}(a^ib^l) = (-1)^i i^l \overline{i^{0}} = (-1)^i i^{l}$, and summing over
$i\in\{0,1\}$ kills all terms, so the inner product is $\frac18\cdot0 = 0$ ✓. Orthogonality of
$\chi_{11}$ with itself: $\lvert\chi_{11}\rvert = 1$ everywhere, so the inner product is
$\frac18\cdot8 = 1$ ✓. Column check: at $a$ and $b$,
$\sum_{j,k}(-1)^{j}i^{-k\cdot0} = \bigl(\sum_j(-1)^j\bigr)\bigl(\sum_k1\bigr) = 0$ ✓.

**17.** *Strategy: irreducibles of a direct product are external tensor products $V_i\boxtimes W_j$, with
characters $\chi_i(g)\psi_j(h)$; classes are products of classes.*

$S_3$ has classes $e,\mathrm{tr},3\mathrm{c}$ (sizes $1,3,2$) and $C_2$ has classes $e,z$ (sizes $1,1$);
so $S_3\times C_2$ has $3\cdot2 = 6$ classes, each of size the product of the two sizes. The six
irreducible characters and degrees:

| $S_3\times C_2$ | $(e,e)$ | $(e,z)$ | $(\mathrm{tr},e)$ | $(\mathrm{tr},z)$ | $(3\mathrm{c},e)$ | $(3\mathrm{c},z)$ |
|---|---|---|---|---|---|---|
| class size | 1 | 1 | 3 | 3 | 2 | 2 |
| $\chi_1\boxtimes1$ | 1 | 1 | 1 | 1 | 1 | 1 |
| $\chi_1\boxtimes\varepsilon$ | 1 | $-1$ | 1 | $-1$ | 1 | $-1$ |
| $\chi_2\boxtimes1$ | 1 | 1 | $-1$ | $-1$ | 1 | 1 |
| $\chi_2\boxtimes\varepsilon$ | 1 | $-1$ | $-1$ | 1 | 1 | $-1$ |
| $\chi_3\boxtimes1$ | 2 | 2 | 0 | 0 | $-1$ | $-1$ |
| $\chi_3\boxtimes\varepsilon$ | 2 | $-2$ | 0 | 0 | $-1$ | 1 |

Degrees $1,1,1,1,2,2$ give $\sum d_i^2 = 1+1+1+1+4+4 = 12 = \lvert S_3\times C_2\rvert$ ✓, and there are
six rows for six classes ✓. (Row orthogonality is inherited from the factor tables, since
$\langle\chi\boxtimes\psi,\chi'\boxtimes\psi'\rangle = \langle\chi,\chi'\rangle\langle\psi,\psi'\rangle$.)

**18.** *Strategy: apply Theorem 7.40 with $H = A_3$, using that $A_3$ is normal.*

Here $[S_3:A_3] = 2$, so the induced representation is $2$-dimensional. For $g = e$, every $x$
contributes $\psi(e) = 1$ and $\chi(e) = \frac13\cdot6 = 2$. For a transposition, no conjugate lies in
$A_3$, so $\chi(\mathrm{tr}) = 0$. For $g = (123)$ all conjugates lie in $A_3$ (normality), and the
conjugates are $(123)$ for three choices of $x$ and $(132)$ for three; hence

$$\chi\bigl((123)\bigr) = \frac13\bigl(3\psi((123)) + 3\psi((132))\bigr) = \omega_3+\omega_3^2 = -1.$$

So $\chi = (2,0,-1) = \chi_3$: inducing the nontrivial character of $A_3$ gives the standard
representation. Check by reciprocity: $\langle\chi_3|_H,\psi\rangle_H = \frac13\bigl(2\cdot1 + (-1)\omega
+ (-1)\omega^2\bigr) = \frac13(2+1) = 1$ ✓.

**19.** *Strategy: one-dimensional representations have no proper subspaces, and finite order forces roots
of unity.*

A one-dimensional $V$ has exactly two subspaces, $\{0\}$ and $V$, so it is irreducible by Definition 5.5.
The map $\chi = \rho : G\to GL_1(\mathbb{C}) = \mathbb{C}^{\times}$ is a homomorphism by definition.
Finally $\chi(g)^{n} = \chi(g^{n}) = \chi(e) = 1$ for $n = \operatorname{ord}(g)$, so $\chi(g)$ is a root
of unity and its order divides $n$. Note the converse direction used above: for one-dimensional
representations the character *is* the representation, which is why the notation overloads the word.

**20.** *Strategy: apply Theorem 8.6, which needs $\chi(g)$ and $\chi(g^2)$.*

With classes $(e, r^2, \{r,r^3\}, \{s,r^2s\}, \{rs,r^3s\})$, the character of $E$ is
$(2,-2,0,0,0)$. Squaring: $r^2\mapsto e$ and $r\mapsto r^2$; every reflection squares to $e$. Hence
$\chi(g^2) = (2,2,-2,2,2)$. Therefore

$$\chi_{\operatorname{Sym}^2} = \tfrac12\bigl((4,4,0,0,0)+(2,2,-2,2,2)\bigr) = (3,3,-1,1,1),$$
$$\chi_{\Lambda^2} = \tfrac12\bigl((4,4,0,0,0)-(2,2,-2,2,2)\bigr) = (1,1,1,-1,-1) = \chi_{A_2}.$$

Decomposing $(3,3,-1,1,1)$: $m_{A_1} = \frac18(3+3-2+2+2) = 1$,
$m_{A_2} = \frac18(3+3-2-2-2) = 0$,
$m_{B_1} = \frac18(3+3+2+2-2) = 1$,
$m_{B_2} = \frac18(3+3+2-2+2) = 1$,
$m_E = \frac18(3\cdot2 + 3\cdot(-2)) = 0$. So $\operatorname{Sym}^2E\cong A_1\oplus B_1\oplus B_2$ and
$\Lambda^2E\cong A_2$. Check: dimensions $1+1+1 = 3 = \binom{2+1}{2}$ and $1 = \binom22$; adding,
$E^{\otimes2}\cong A_1\oplus A_2\oplus B_1\oplus B_2$, of dimension $4 = 2^2$ ✓.

**21.** *Strategy: use that $R(G)\cong\mathbb{Z}^k$ with pointwise multiplication, and test invertibility
pointwise.*

The augmentation is additive by definition and
$\varepsilon([V][W]) = \dim(V\otimes W) = \dim V\cdot\dim W = \varepsilon([V])\varepsilon([W])$, and
$\varepsilon([\mathbb{1}]) = 1$; so it is a unital ring homomorphism. In $R(S_3)$,
$\varepsilon([\chi_3]-[\mathbb{1}]) = 2-1 = 1$.

For invertibility: under $\operatorname{ch} : R(G)\to\mathbb{Z}^k$ (values on the $k$ classes), a product
becomes pointwise multiplication, so an invertible element must have every character value equal to
$\pm1$ (as an integer). But $[\chi_3]-[\mathbb{1}]$ has values $(2-1,\ 0-1,\ -1-1) = (1,-1,-2)$ on
$(e,\mathrm{tr},3\mathrm{c})$, and $-2\notin\{\pm1\}$. Hence it is not a unit, even though its
augmentation is $1$: the augmentation is not a complete invariant of invertibility.

**22.** *Strategy: one-dimensional characters are unimodular, and an average of roots of unity is $1$ only
in the trivial case.*

For every $g$, $\chi(g)\overline{\chi(g)} = \lvert\chi(g)\rvert^2 = 1$ because $\chi(g)$ is a root of
unity (Problem 19), so $\chi\overline{\chi} = \mathbb{1}$.

Next, $\langle\chi,\mathbb{1}\rangle = \frac{1}{\lvert G\rvert}\sum_g\chi(g)$ is an average of roots of
unity, so its modulus is at most $1$, with equality iff all summands are equal (triangle inequality
equality case). If the average equals $1$ then $\chi(g) = 1$ for every $g$, i.e. $\chi = \mathbb{1}$;
conversely $\langle\mathbb{1},\mathbb{1}\rangle = 1$. Hence $\langle\chi,\mathbb{1}\rangle = 1$ iff
$\chi = \mathbb{1}$; more generally $\langle\chi,\mathbb{1}\rangle = 0$ for every nontrivial
one-dimensional character.

**23.** *Strategy: write $C_6 = \langle r\rangle$ and use $\chi_k(r^j) = \omega_6^{jk}$.*

The table is the $6\times6$ matrix $U_{jk} = \omega_6^{jk}$ with rows indexed by $k$ and columns by $j$:

| $C_6$ | $e$ | $r$ | $r^2$ | $r^3$ | $r^4$ | $r^5$ |
|---|---|---|---|---|---|---|
| $\chi_0$ | 1 | 1 | 1 | 1 | 1 | 1 |
| $\chi_1$ | 1 | $\zeta$ | $\zeta^2$ | $-1$ | $\zeta^4$ | $\zeta^5$ |
| $\chi_2$ | 1 | $\zeta^2$ | $\zeta^4$ | 1 | $\zeta^2$ | $\zeta^4$ |
| $\chi_3$ | 1 | $-1$ | 1 | $-1$ | 1 | $-1$ |
| $\chi_4$ | 1 | $\zeta^4$ | $\zeta^2$ | 1 | $\zeta^4$ | $\zeta^2$ |
| $\chi_5$ | 1 | $\zeta^5$ | $\zeta^4$ | $-1$ | $\zeta^2$ | $\zeta$ |

with $\zeta = e^{2\pi i/6}$. The Fourier transform of $\delta_e$ is
$\widehat{\delta_e}(\chi_k) = \sum_j\delta_e(r^j)\overline{\chi_k(r^j)} = 1$ for every $k$: the delta
function at the identity has a flat transform. Fourier inversion asserts
$\delta_e(r^j) = \frac16\sum_k\widehat{\delta_e}(\chi_k)\chi_k(r^j) = \frac16\sum_k\zeta^{jk}$, which is
$1$ for $j = 0$ and $0$ for $j = 1,\dots,5$ by the geometric sum formula. This is exactly Parseval's
identity in the form "the columns of $U$ are orthogonal", and it confirms Fourier inversion for this
function.

## Advanced

**24.** *Strategy: Schur's lemma gives the scalar action; counting matrix coefficients on cosets of the
centre gives the bound.*

Let $\rho$ be irreducible of degree $d$ and $z\in Z(G)$. For every $g$,
$\rho(z)\rho(g) = \rho(zg) = \rho(gz) = \rho(g)\rho(z)$, so $\rho(z)\in\operatorname{End}_G(V) =
\mathbb{C}\cdot\mathrm{id}$ by Schur's lemma. Write $\rho(z) = \lambda(z)\mathrm{id}$; then
$\lambda : Z(G)\to\mathbb{C}^{\times}$ is a homomorphism, the *central character*.

First note that the $d^{2}$ matrix coefficients $\rho_{ij}(g)$ are linearly independent functions on $G$.
Indeed, the averaging operator $P(T) = \frac{1}{\lvert G\rvert}\sum_g\rho(g)T\rho(g)^{-1}$ is the
projection of $\operatorname{End}(V)$ onto $\operatorname{End}_G(V) = \mathbb{C}\mathrm{id}$
(Lemma 7.19 with $V = W$), whose image has dimension $1$; computing $P$ on the matrix unit $E_{kl}$ gives
$\sum_g\rho_{ik}(g)\rho_{lj}(g^{-1}) = \frac{\lvert G\rvert}{d}\delta_{ij}\delta_{kl}$, which is exactly
the orthogonality of the $d^{2}$ coefficients, hence their independence.

Now let $R\subseteq G$ be a set of coset representatives for $Z(G)$. For $z\in Z(G)$,
$\rho_{ij}(zg) = \lambda(z)\rho_{ij}(g)$, so every $\rho_{ij}$ is determined by its values on $R$: if
$g = zr$ then $\rho_{ij}(g) = \lambda(z)\rho_{ij}(r)$. Hence the evaluation map
$\operatorname{span}\{\rho_{ij}\}\to\mathbb{C}^{\lvert R\rvert}$ is injective, and

$$d^{2} = \dim\operatorname{span}\{\rho_{ij}\}\le \lvert R\rvert = [G:Z(G)].$$

For $S_3$: $d = 2$ and $[S_3:Z] = 6$, so $4\le6$ ✓. For a nonabelian group of order $p^{3}$ with centre
of order $p$, the bound reads $d^{2}\le p^{2}$ and is attained by the unique irreducible of degree $p$.

**25.** *Strategy: compare $\sum d_i^{2}$ with the number of classes.*

If $G$ is abelian then every irreducible is one-dimensional by Corollary 7.13, so all $d_i = 1$.

Conversely suppose all $d_i = 1$. By Theorem 7.31, $\lvert G\rvert = \sum_i d_i^{2} = r$, the number of
irreducibles, and by Corollary 7.24 that number equals the number $k$ of conjugacy classes. Hence
$k = \lvert G\rvert$. Since the classes partition $G$ and each is nonempty, this forces every class to be
a singleton, i.e. $ghg^{-1} = h$ for all $g,h$: the group is abelian. $\square$

**26.** *Strategy: associativity of the tensor product over nested rings.*

By Definition 7.39, $\operatorname{Ind}_H^K W = \mathbb{C}[K]\otimes_{\mathbb{C}[H]}W$, so

$$\operatorname{Ind}_K^G\bigl(\operatorname{Ind}_H^K W\bigr)
= \mathbb{C}[G]\otimes_{\mathbb{C}[K]}\bigl(\mathbb{C}[K]\otimes_{\mathbb{C}[H]}W\bigr)
\cong \mathbb{C}[G]\otimes_{\mathbb{C}[H]}W = \operatorname{Ind}_H^G W,$$

the middle isomorphism being $g\otimes(k\otimes w)\mapsto (gk)\otimes w$, which is well defined and
bijective (both sides satisfy the same universal property for balanced $\mathbb{C}[H]$-maps out of
$\mathbb{C}[G]\times W$). $\square$

Dimension check: $[G:K][K:H]\dim W = [G:H]\dim W$ ✓.

**27.** *Strategy: identify the induced module with functions on the coset space.*

Take $W = \mathbb{C}$ with trivial $H$-action. Then
$\operatorname{Ind}_H^G\mathbb{1}_H = \mathbb{C}[G]\otimes_{\mathbb{C}[H]}\mathbb{C}\cong
\mathbb{C}[G/H]$, the space with basis the cosets $gH$, on which $g$ acts by
$g\cdot(g'H) = gg'H$ — exactly the permutation representation of $G$ on $G/H$. By Proposition 7.17 its
character at $g$ is the number of cosets fixed by $g$. The explicit formula of Theorem 7.40 gives
$\chi(g) = \#\{j : g_j^{-1}gg_j\in H\} = \#\{j : g\,g_jH = g_jH\}$, the same number. $\square$

**28.** *Strategy: one-dimensional representations are homomorphisms into an abelian group, so they factor
through the abelianisation.*

A one-dimensional representation is a homomorphism $\chi : G\to\mathbb{C}^{\times}$. Since
$\mathbb{C}^{\times}$ is abelian,
$\chi(ghg^{-1}h^{-1}) = \chi(g)\chi(h)\chi(g)^{-1}\chi(h)^{-1} = 1$, so $[G,G]\subseteq\ker\chi$ and
$\chi$ factors through $G/[G,G]$. Conversely every homomorphism out of $G/[G,G]$ composed with the
quotient map is a one-dimensional representation. Hence the dual groups of $G$ and $G/[G,G]$ coincide,
and by Theorem 7.43 the latter has order $\lvert G/[G,G]\rvert$. $\square$

**29.** *Strategy: equality in the triangle inequality forces a scalar matrix; faithfulness converts
commuting into centrality.*

By Proposition 7.16(6), $\lvert\chi(g)\rvert = \chi(e) = d$ forces all eigenvalues of $\rho(g)$ to equal a
common root of unity $\lambda$, i.e. $\rho(g) = \lambda\,\mathrm{id}$. Then for every $h$,

$$\rho(ghg^{-1}h^{-1}) = \rho(g)\rho(h)\rho(g)^{-1}\rho(h)^{-1}
= \lambda\rho(h)\lambda^{-1}\rho(h)^{-1} = \mathrm{id},$$

so $ghg^{-1}h^{-1}\in\ker\rho = \{e\}$ because $\rho$ is faithful. Hence $gh = hg$ for all $h$, i.e.
$g\in Z(G)$. $\square$

**30.** *Strategy: expand the characters in cosines, use the product identity
$\chi_l\chi_m = \sum_{k=\lvert l-m\rvert}^{l+m}\chi_k$, and integrate term by term.*

First, $\chi_l(\theta) = \frac{\sin((2l+1)\theta/2)}{\sin(\theta/2)} = 1+2\sum_{k=1}^{l}\cos k\theta$ by
telescoping. Then $\sin^{2}(\theta/2) = \frac{1-\cos\theta}{2}$, so

$$\frac{2}{\pi}\int_0^{\pi}\chi_l\chi_m\sin^{2}\tfrac{\theta}{2}\,d\theta
= \frac{1}{\pi}\sum_{k=\lvert l-m\rvert}^{l+m}\int_0^{\pi}\chi_k(\theta)\bigl(1-\cos\theta\bigr)\,d\theta .$$

Now $\int_0^\pi\chi_k\,d\theta = \pi$ for all $k$, since the cosine terms integrate to zero; and
$\int_0^\pi\chi_k\cos\theta\,d\theta = \pi$ for $k\ge1$ (the $2\cos\theta$ term contributes
$2\cdot\frac{\pi}{2}$) while it is $0$ for $k = 0$. Each summand is therefore $0$, except the summand
$k = 0$, which equals $\pi$ and occurs in the range exactly when $\lvert l-m\rvert = 0$, i.e. $l = m$.
Hence the integral is $\frac{\pi}{\pi} = 1$ for $l = m$ and $0$ otherwise ✓.

The identity $\chi_2^{2} = \chi_0+\chi_1+\chi_2+\chi_3+\chi_4$ at $\theta = 0.5$ was checked numerically:
$\chi_2(0.5)^{2} = 14.713129464$ and $\sum_{l=0}^{4}\chi_l(0.5) = 14.713129464$, agreeing to nine
decimals. This is the character form of
$V_2\otimes V_2\cong V_0\oplus V_1\oplus V_2\oplus V_3\oplus V_4$; dimension check
$25 = 1+3+5+7+9$ ✓.

**31.** *Strategy: unitarity of the scaled character table is exactly row orthogonality.*

Let $U_{jk} = n^{-1/2}\omega_n^{jk}$ for $j,k = 0,\dots,n-1$. Then

$$(U^{*}U)_{j\ell} = \frac1n\sum_{k=0}^{n-1}\overline{\omega_n^{jk}}\,\omega_n^{\ell k}
= \frac1n\sum_{k=0}^{n-1}\omega_n^{(\ell-j)k} = \delta_{j\ell},$$

by the geometric sum formula, so $U$ is unitary.

Fourier inversion: for $f : C_n\to\mathbb{C}$ put $f_j = f(r^j)$ and
$\widehat f_k = \sum_j f_j\omega_n^{-jk}$. Writing $f = (f_j)$, we have
$\widehat f = \sqrt n\,\overline{U}f$, hence

$$\frac1n\sum_k\widehat f_k\,\omega_n^{jk} = \frac{1}{\sqrt n}\bigl(U\widehat f\bigr)_j
= \bigl(U\overline U f\bigr)_j = \bigl(UU^{*}f\bigr)_j = f_j,$$

using $U\overline U = UU^{*} = I$. This is Fourier inversion, so the theorem says precisely that the
character table is a unitary change of basis. $\square$

## Challenge

**32.** *Strategy: five classes give five rows; the degrees are forced by $\sum d_i^{2} = 24$; the
characters come from the permutation representation, twisting by sign, and column orthogonality.*

Classes of $S_4$ with sizes: $e$ (1); transpositions $(ab)$ (6); double transpositions $(ab)(cd)$ (3);
$3$-cycles $(abc)$ (8); $4$-cycles $(abcd)$ (6). The sizes sum to $1+6+3+8+6 = 24$ ✓.

Degrees: the trivial and sign characters are one-dimensional; the permutation character is
$\chi_{\mathrm{perm}} = (4,2,0,1,0)$ and $\chi_{\mathrm{perm}} = \mathbb{1}+\chi_{\mathrm{std}}$, so
$\chi_{\mathrm{std}} = (3,1,-1,0,-1)$; twisting by sign gives $\chi_4 = (3,-1,-1,0,1)$. Four rows give
$\sum d^{2} = 1+1+9+9 = 20$, so $d_5^{2} = 4$ and $d_5 = 2$. Column orthogonality with the column at $e$
gives $\chi_5$:

* at $(ab)$: $1-1+3-3+2\chi_5 = 0\Rightarrow\chi_5 = 0$;
* at $(ab)(cd)$: $1+1-3-3+2\chi_5 = 0\Rightarrow\chi_5 = 2$;
* at $(abc)$: $1+1+0+0+2\chi_5 = 0\Rightarrow\chi_5 = -1$;
* at $(abcd)$: $1-1-3+3+2\chi_5 = 0\Rightarrow\chi_5 = 0$.

| $S_4$ | $e$ | $(ab)$ | $(ab)(cd)$ | $(abc)$ | $(abcd)$ |
|---|---|---|---|---|---|
| class size | 1 | 6 | 3 | 8 | 6 |
| $\chi_1$ | 1 | 1 | 1 | 1 | 1 |
| $\chi_2$ (sign) | 1 | $-1$ | 1 | 1 | $-1$ |
| $\chi_3$ (standard) | 3 | 1 | $-1$ | 0 | $-1$ |
| $\chi_4$ (standard $\otimes$ sign) | 3 | $-1$ | $-1$ | 0 | 1 |
| $\chi_5$ | 2 | 0 | 2 | $-1$ | 0 |

Checks: $\langle\chi_5,\chi_5\rangle = \frac{1}{24}(4+0+3\cdot4+8\cdot1+0) = 1$;
$\langle\chi_3,\chi_3\rangle = \frac{1}{24}(9+6+3+0+6) = 1$;
$\langle\chi_3,\chi_4\rangle = \frac{1}{24}(9-6+3+0-6) = 0$; the column at $e$ gives
$1+1+9+9+4 = 24$ and the column at $(abc)$ gives $1+1+0+0-2 = 0$ against the identity column ✓.

**33.** *Strategy: one direction uses $\chi(g^{-1}) = \overline{\chi(g)}$; the other uses column
orthogonality.*

If every $g$ is conjugate to $g^{-1}$, then every class function, in particular every character, satisfies
$\chi(g) = \chi(g^{-1}) = \overline{\chi(g)}$: all characters are real.

Conversely suppose all characters are real-valued. Then $\chi(g) = \chi(g^{-1}) =
\overline{\chi(g)}$ for all $g$ and $\chi$, so by column orthogonality (Theorem 7.23),

$$\sum_i\chi_i(g)\overline{\chi_i(g^{-1})} = \sum_i\chi_i(g)\overline{\chi_i(g)}
= \sum_i\lvert\chi_i(g)\rvert^{2} \ge \lvert\chi_1(g)\rvert^{2} = 1 > 0 .$$

Theorem 7.23 says the same sum equals $\lvert C_G(g)\rvert$ if $g$ is conjugate to $g^{-1}$ and $0$
otherwise. Being positive, it forces $g\sim g^{-1}$. $\square$

**34.** *Strategy: Burnside's lemma, with the permutation character supplying the fixed-face counts.*

The rotation group of the cube has $24$ elements acting on its $6$ faces:

| type | number | cycle type | fixed faces | fixed colourings ($n$ colours) |
|---|---|---|---|---|
| identity | 1 | $1^{6}$ | 6 | $n^{6}$ |
| $90^\circ$ about a face axis | 6 | $1^{2}4^{1}$ | 2 | $n^{3}$ |
| $180^\circ$ about a face axis | 3 | $1^{2}2^{2}$ | 2 | $n^{4}$ |
| $120^\circ$ about a body diagonal | 8 | $3^{2}$ | 0 | $n^{2}$ |
| $180^\circ$ about an edge axis | 6 | $2^{3}$ | 0 | $n^{3}$ |

A colouring is fixed by a permutation of the faces exactly when it is constant on each cycle, giving
$n^{\#\text{cycles}}$ fixed colourings. Burnside's lemma yields

$$N(n) = \frac{1}{24}\Bigl(n^{6} + 6n^{3} + 3n^{4} + 8n^{2} + 6n^{3}\Bigr)
= \frac{n^{6}+3n^{4}+12n^{3}+8n^{2}}{24}.$$

For $n = 2$: $(64+48+96+32)/24 = 240/24 = 10$ ✓. For $n = 3$:
$(729+243+324+72)/24 = 1368/24 = 57$ ✓.

The character-theoretic content: the fixed-face counts are the values of the permutation character
$\chi$ of the rotation group on the faces, and Burnside's lemma is
$\frac{1}{\lvert G\rvert}\sum_g\chi(g) = \langle\chi,\mathbb{1}\rangle$, the multiplicity of the trivial
representation, which counts the orbits.

**35.** *Strategy: a normal subgroup is a union of conjugacy classes containing $e$, and its order divides
$60$.*

Let $N\trianglelefteq A_5$ be nontrivial. A normal subgroup is a union of conjugacy classes and contains
$e$, so $\lvert N\rvert = 1 + \sum_{j\in J}\lvert C_j\rvert$ for a subset of the class sizes $15,20,12,12$.
The possible values are

$$1,\ 16,\ 21,\ 13,\ 36,\ 28,\ 33,\ 48,\ 40,\ 45,\ 25,\ 60 .$$

(For instance $1+15+20 = 36$, $1+15+12+12 = 40$, $1+20+12+12 = 45$, $1+12+12 = 25$.) By Lagrange,
$\lvert N\rvert$ divides $60$, and among the listed numbers only $1$ and $60$ do. Since $N$ is
nontrivial, $\lvert N\rvert = 60$ and $N = A_5$: the group has no proper nontrivial normal subgroup and is
simple. $\square$

**36.** *Strategy: identify the eigenfunctions of translation and use orthonormality of the
characters.*

Let $L_w$ be left translation by $w\in S^{1}$, $(L_wf)(z) = f(w^{-1}z)$. For $f_n(z) = z^{n}$,
$(L_wf_n)(z) = (w^{-1}z)^{n} = w^{-n}z^{n}$, so $\mathbb{C}f_n$ is a one-dimensional invariant subspace on
which $L_w$ acts by the character $w\mapsto w^{-n}$; these characters are distinct for distinct $n$.
Orthogonality:

$$\langle f_n,f_m\rangle = \frac{1}{2\pi}\int_0^{2\pi}e^{in\theta}\overline{e^{im\theta}}\,d\theta
= \frac{1}{2\pi}\int_0^{2\pi}e^{i(n-m)\theta}d\theta = \delta_{nm}.$$

Every character $z\mapsto z^{n}$ occurs with multiplicity $d_n = 1$, exactly as in Theorem 7.31 for a
finite group; Peter–Weyl (Theorem 7.47) upgrades the orthonormal family to an orthonormal *basis*, which
is the statement that every $L^{2}$ function has a Fourier series converging in $L^{2}$.

For $f(z) = z+\bar z = e^{i\theta}+e^{-i\theta}$ the Fourier coefficients are
$\widehat f(1) = \widehat f(-1) = 1$ and $\widehat f(n) = 0$ otherwise. Parseval:

$$\frac{1}{2\pi}\int_0^{2\pi}\lvert2\cos\theta\rvert^{2}d\theta
= \frac{1}{2\pi}\int_0^{2\pi}\bigl(2+2\cos2\theta\bigr)d\theta = 2,\qquad
\sum_n\lvert\widehat f(n)\rvert^{2} = 1+1 = 2 \ ✓.$$

