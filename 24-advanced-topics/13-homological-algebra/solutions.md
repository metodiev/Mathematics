# Homological Algebra — Solutions

> [Homological Algebra](README.md) · Solutions to [exercises.md](exercises.md) · 36 problems

Each solution states the strategy, then carries out every step. Section references point into
[README.md](README.md). Notation is that of the exercises.

## Beginner

**1.** **Strategy.** Compute kernels and images degree by degree.

In degree $2$, the map $\times 3 : \mathbb{Z} \to \mathbb{Z}$ is injective, so $H_2 = 0$. In degree $1$, $Z_1 = \mathbb{Z}$ because the outgoing map is zero, and $B_1 = 3\mathbb{Z}$. Hence
$$H_1 = \mathbb{Z}/3\mathbb{Z}.$$
In degree $0$, $Z_0 = \mathbb{Z}$ and $B_0 = 0$, so $H_0 = \mathbb{Z}$. The homology is $(\mathbb{Z}, \mathbb{Z}/3, 0)$.

**2.** **Strategy.** Check injectivity of the first map, surjectivity of the last, and equality of kernel and image in the middle.

(a) The map $\times 2 : \mathbb{Z} \to \mathbb{Z}$ is injective; the quotient map $\mathbb{Z} \to \mathbb{Z}/2$ is surjective with kernel $2\mathbb{Z}$, which is the image. Exact.

(b) The map $\mathbb{Z}/2 \to \mathbb{Z}/4$, $1 \mapsto 2$, is injective because $2$ has order $2$ in $\mathbb{Z}/4$. The quotient map $\mathbb{Z}/4 \to \mathbb{Z}/2$ is surjective with kernel $\{0,2\}$, which is the image. Exact.

(c) The quotient map $\mathbb{Z} \to \mathbb{Z}/4$ has kernel $4\mathbb{Z}$, while the image of $\times 2$ is $2\mathbb{Z}$. Since $2\mathbb{Z} \ne 4\mathbb{Z}$, the sequence is not exact at $\mathbb{Z}$. Concretely, $2 = 2\cdot 1$ lies in the image of $\times 2$, but its image in $\mathbb{Z}/4$ is $2 \ne 0$, so it is not killed by the next map.

**3.** **Strategy.** Use the lifting property for free modules; use Hom to disprove projectivity.

*Free is projective.* Let $F$ be free with basis $\{e_i\}$, let $p : B \to C$ be surjective, and let $f : F \to C$. For each $i$, choose $b_i \in B$ with $p(b_i) = f(e_i)$ (possible because $p$ is surjective). Define $\tilde f : F \to B$ on the basis by $\tilde f(e_i) = b_i$ and extend linearly. Then $p\tilde f(e_i) = f(e_i)$ for all $i$, so $p\tilde f = f$.

*$\mathbb{Z}/2$ is not projective.* Suppose it were. Then every surjection $B \to \mathbb{Z}/2$ would split. Take $B = \mathbb{Z}$ and the quotient map $\mathbb{Z} \to \mathbb{Z}/2$. A splitting would be a homomorphism $s : \mathbb{Z}/2 \to \mathbb{Z}$ with $p s = \operatorname{id}$. But every homomorphism $\mathbb{Z}/2 \to \mathbb{Z}$ is zero, because $\mathbb{Z}$ is torsion-free, so $p s = 0 \ne \operatorname{id}$. Contradiction.

**4.** **Strategy.** Use Baer's criterion over $\mathbb{Z}$, where the ideals are $n\mathbb{Z}$.

*$\mathbb{Q}$ is injective.* A $\mathbb{Z}$-module is injective iff it is divisible (Baer's criterion plus the structure of ideals of $\mathbb{Z}$). The group $\mathbb{Q}$ is divisible: for $q \in \mathbb{Q}$ and $n \ne 0$, the element $q/n \in \mathbb{Q}$ satisfies $n(q/n) = q$. Hence $\mathbb{Q}$ is injective.

*$\mathbb{Z}$ is not injective.* Consider the inclusion $2\mathbb{Z} \hookrightarrow \mathbb{Z}$ and the map $f : 2\mathbb{Z} \to \mathbb{Z}$ defined by $f(2k) = k$. If an extension $g : \mathbb{Z} \to \mathbb{Z}$ existed, then $g(2) = f(2) = 1$, but $g(2) = 2g(1)$ is even, contradiction. Hence $\mathbb{Z}$ is not injective.

**5.** **Strategy.** A homomorphism out of $\mathbb{Z}/n$ is determined by the image of $1$, which must be killed by $n$.

A homomorphism $\varphi : \mathbb{Z}/n \to \mathbb{Z}$ is determined by $a = \varphi(1)$, and $na = 0$ in $\mathbb{Z}$, so $a = 0$. Hence $\operatorname{Hom}(\mathbb{Z}/n,\mathbb{Z}) = 0$.

For $\varphi : \mathbb{Z}/n \to \mathbb{Z}/m$, the element $a = \varphi(1)$ must satisfy $na \equiv 0 \pmod m$, that is, $a$ is a multiple of $m/g$ where $g = \gcd(n,m)$. There are exactly $g$ such elements modulo $m$, forming a cyclic group of order $g$. Hence
$$\operatorname{Hom}_{\mathbb{Z}}(\mathbb{Z}/n,\mathbb{Z}/m) \cong \mathbb{Z}/\gcd(n,m).$$

**6.** **Strategy.** Left exactness is formal; failure of exactness is visible at the last map.

For any ring $R$ and modules, $\operatorname{Hom}_R(-,N)$ is left exact: given $0 \to A \to B \to C \to 0$, the sequence $0 \to \operatorname{Hom}(C,N) \to \operatorname{Hom}(B,N) \to \operatorname{Hom}(A,N)$ is exact. This is a direct check: the first map is injective because a map out of $C$ that vanishes on the image of $B$ is zero; the composite is zero because the composite $A \to B \to C$ is zero; and a map $B \to N$ that vanishes on $A$ descends to $C$.

Apply to $0 \to \mathbb{Z} \xrightarrow{2} \mathbb{Z} \to \mathbb{Z}/2 \to 0$ and $N = \mathbb{Z}$:
$$0 \to \operatorname{Hom}(\mathbb{Z}/2,\mathbb{Z}) \to \operatorname{Hom}(\mathbb{Z},\mathbb{Z}) \xrightarrow{\times 2} \operatorname{Hom}(\mathbb{Z},\mathbb{Z}).$$
The first group is $0$, and the map is multiplication by $2$ on $\mathbb{Z}$, whose image is $2\mathbb{Z} \ne \mathbb{Z}$. Hence the sequence is not exact at the last $\mathbb{Z}$. The cokernel is $\mathbb{Z}/2$, which is $\operatorname{Ext}^1(\mathbb{Z}/2,\mathbb{Z})$.

**7.** **Strategy.** Right exactness is formal; failure of exactness is visible at the first map.

Tensor is right exact: for $0 \to A \to B \to C \to 0$, the sequence $A \otimes N \to B \otimes N \to C \otimes N \to 0$ is exact. Apply with $N = \mathbb{Z}/2$:
$$\mathbb{Z}/2 \xrightarrow{\times 2} \mathbb{Z}/2 \to \mathbb{Z}/2 \otimes \mathbb{Z}/2 \to 0.$$
The map $\times 2$ on $\mathbb{Z}/2$ is the zero map, whose kernel is $\mathbb{Z}/2 \ne 0$. Hence the sequence is not exact at the left, and
$$\operatorname{Tor}_1^{\mathbb{Z}}(\mathbb{Z}/2,\mathbb{Z}/2) \cong \mathbb{Z}/2.$$

**8.** **Strategy.** Use the standard two-term resolutions.

For $\mathbb{Z}/6$:
$$0 \to \mathbb{Z} \xrightarrow{\ \times 6\ } \mathbb{Z} \xrightarrow{\ \operatorname{mod} 6\ } \mathbb{Z}/6 \to 0.$$
The map $\times 6$ is injective, the quotient map is surjective, and its kernel is $6\mathbb{Z}$, the image. Exact.

For $\mathbb{Z}/2$:
$$0 \to \mathbb{Z} \xrightarrow{\ \times 2\ } \mathbb{Z} \xrightarrow{\ \operatorname{mod} 2\ } \mathbb{Z}/2 \to 0.$$
Same verification with $2$ in place of $6$. Both are projective resolutions because $\mathbb{Z}$ is free, hence projective.

**9.** **Strategy.** Use divisible groups, which are injective over $\mathbb{Z}$.

For $\mathbb{Z}$:
$$0 \to \mathbb{Z} \hookrightarrow \mathbb{Q} \xrightarrow{\ \operatorname{mod} 1\ } \mathbb{Q}/\mathbb{Z} \to 0.$$
The inclusion is injective, the quotient map is surjective, and its kernel is $\mathbb{Z}$. Both $\mathbb{Q}$ and $\mathbb{Q}/\mathbb{Z}$ are divisible, hence injective.

For $\mathbb{Z}/3$:
$$0 \to \mathbb{Z}/3 \hookrightarrow \mathbb{Q}/\mathbb{Z} \xrightarrow{\ \times 3\ } \mathbb{Q}/\mathbb{Z} \to 0.$$
The kernel of $\times 3$ on $\mathbb{Q}/\mathbb{Z}$ is the subgroup of elements of order dividing $3$, which is $\mathbb{Z}/3$; the map $\times 3$ is surjective because $\mathbb{Q}/\mathbb{Z}$ is divisible. Exact, and $\mathbb{Q}/\mathbb{Z}$ is injective.

**10.** **Strategy.** Use the lifting property of projective modules, and dually the extension property of injective modules.

Suppose $0 \to A \xrightarrow{i} B \xrightarrow{p} C \to 0$ is exact and $C$ is projective. Apply the lifting property to the identity map $\operatorname{id}_C : C \to C$ and the surjection $p : B \to C$: there is $s : C \to B$ with $p s = \operatorname{id}_C$. Then
$$\Phi : A \oplus C \to B, \qquad \Phi(a,c) = i(a) + s(c)$$
is an isomorphism: it is injective because $i(a) + s(c) = 0$ implies $p(i(a)+s(c)) = c = 0$ and then $i(a)=0$, so $a=0$; it is surjective because for $b \in B$, $c = p(b)$ and $b - s(c)$ lies in $\ker p = \operatorname{im} i$. Hence the sequence splits.

Dually, if $A$ is injective, apply the extension property to $\operatorname{id}_A : A \to A$ and the injection $i : A \to B$: there is $r : B \to A$ with $r i = \operatorname{id}_A$. Then $B \cong A \oplus \ker r$ via $b \mapsto (r(b), b - i r(b))$, and the sequence splits.

**11.** **Strategy.** Use the definitions $\operatorname{Ext}^0 = \operatorname{Hom}$ and $\operatorname{Tor}_0 = \otimes$.

$$\operatorname{Ext}^0_{\mathbb{Z}}(\mathbb{Z}/12,\mathbb{Z}/18) = \operatorname{Hom}(\mathbb{Z}/12,\mathbb{Z}/18) \cong \mathbb{Z}/\gcd(12,18) = \mathbb{Z}/6.$$
$$\operatorname{Tor}_0^{\mathbb{Z}}(\mathbb{Z}/12,\mathbb{Z}/18) = \mathbb{Z}/12 \otimes_{\mathbb{Z}} \mathbb{Z}/18 \cong \mathbb{Z}/\gcd(12,18) = \mathbb{Z}/6.$$

**12.** **Strategy.** Use the splitting criterion for projective third terms.

Since free modules are projective, Exercise 10 applies and gives $B \cong A \oplus C$.

If $C$ is only projective, the conclusion still holds: projective modules are exactly the direct summands of free modules, and the lifting property used in Exercise 10 requires only projectivity, not freeness. Hence $B \cong A \oplus C$ in that case as well.

## Intermediate

**13.** **Strategy.** Use the two-term projective resolution and the long exact sequence for Hom.

Resolve $\mathbb{Z}/12$ by $0 \to \mathbb{Z} \xrightarrow{12} \mathbb{Z} \to \mathbb{Z}/12 \to 0$ and apply $\operatorname{Hom}_{\mathbb{Z}}(-,\mathbb{Z}/18)$:
$$0 \to \operatorname{Hom}(\mathbb{Z}/12,\mathbb{Z}/18) \to \mathbb{Z}/18 \xrightarrow{\ \times 12\ } \mathbb{Z}/18 \to \operatorname{Ext}^1 \to 0.$$
The first group is $\mathbb{Z}/6$ by Exercise 5. The image of $\times 12$ on $\mathbb{Z}/18$ is $\{0,6,12\}$, of order $3$, so the cokernel has order $18/3 = 6$ and is cyclic, hence $\mathbb{Z}/6$. Therefore
$$\operatorname{Ext}^n_{\mathbb{Z}}(\mathbb{Z}/12,\mathbb{Z}/18) = \begin{cases}\mathbb{Z}/6, & n = 0,\\ \mathbb{Z}/6, & n = 1,\\ 0, & n \ge 2.\end{cases}$$

**14.** **Strategy.** Tensor the same resolution with $\mathbb{Z}/18$.

$$0 \to \operatorname{Tor}_1 \to \mathbb{Z}/18 \xrightarrow{\ \times 12\ } \mathbb{Z}/18 \to \mathbb{Z}/12 \otimes \mathbb{Z}/18 \to 0.$$
The kernel of $\times 12$ on $\mathbb{Z}/18$ consists of $x$ with $12x \equiv 0 \pmod{18}$, equivalently $2x \equiv 0 \pmod 3$, so $x$ is a multiple of $3$. There are $6$ such elements, forming $\mathbb{Z}/6$. The cokernel is $\mathbb{Z}/6$ as in Exercise 13. Hence
$$\operatorname{Tor}_n^{\mathbb{Z}}(\mathbb{Z}/12,\mathbb{Z}/18) = \begin{cases}\mathbb{Z}/6, & n = 0,\\ \mathbb{Z}/6, & n = 1,\\ 0, & n \ge 2.\end{cases}$$
The agreement with Exercise 13 is the general formula $\operatorname{Ext}^1_{\mathbb{Z}}(\mathbb{Z}/m,\mathbb{Z}/n) \cong \operatorname{Tor}_1^{\mathbb{Z}}(\mathbb{Z}/m,\mathbb{Z}/n) \cong \mathbb{Z}/\gcd(m,n)$; both compute the same $\gcd$, but they measure different things (extensions versus torsion).

**15.** **Strategy.** Use the Koszul-type resolution $0 \to k[x] \xrightarrow{x} k[x] \to k \to 0$.

Apply $\operatorname{Hom}_{k[x]}(-,k)$:
$$0 \to \operatorname{Hom}(k,k) \to \operatorname{Hom}(k[x],k) \xrightarrow{\ x^*\ } \operatorname{Hom}(k[x],k) \to \operatorname{Ext}^1 \to 0.$$
Both Hom groups are $k$, and $x^*$ is multiplication by $x$ on $k$, which is zero because $x$ acts on $k$ by zero. Hence $\operatorname{Ext}^1(k,k) \cong k$ and $\operatorname{Ext}^0(k,k) \cong k$.

Tensor the resolution with $k$:
$$0 \to \operatorname{Tor}_1(k,k) \to k \xrightarrow{\ x\ } k \to k \otimes k \to 0.$$
Again $x = 0$ on $k$, so the kernel is $k$ and the cokernel is $k$. Hence $\operatorname{Tor}_1(k,k) \cong k$ and $\operatorname{Tor}_0(k,k) \cong k$.

**16.** **Strategy.** Resolve $k[x]/(x^2)$ by $0 \to k[x] \xrightarrow{x^2} k[x] \to k[x]/(x^2) \to 0$.

Apply $\operatorname{Hom}_{k[x]}(-,k)$:
$$0 \to \operatorname{Hom}(k[x]/(x^2),k) \to k \xrightarrow{\ (x^2)^*\ } k \to \operatorname{Ext}^1 \to 0.$$
The first group is $k$ (a map is determined by the image of $1$, and $x^2$ acts by zero on $k$). The map $(x^2)^*$ is multiplication by $x^2$ on $k$, which is zero. Hence $\operatorname{Ext}^1(k[x]/(x^2),k) \cong k$ and $\operatorname{Ext}^0 \cong k$.

Tensor with $k$:
$$0 \to \operatorname{Tor}_1 \to k \xrightarrow{\ x^2\ } k \to k[x]/(x^2) \otimes k \to 0.$$
The map $x^2$ is zero on $k$, so $\operatorname{Tor}_1 \cong k$ and $\operatorname{Tor}_0 \cong k$.

**17.** **Strategy.** Apply Hom to the extension and use the connecting map.

Let $\mathcal{E} : 0 \to N \xrightarrow{i} E \xrightarrow{p} M \to 0$ be an extension. Apply $\operatorname{Hom}_R(-,N)$ and look at the connecting map
$$\delta : \operatorname{Hom}_R(N,N) \to \operatorname{Ext}^1_R(M,N).$$
Define $\Phi(\mathcal{E}) = \delta(\operatorname{id}_N)$.

*Well-definedness.* If $\mathcal{E}$ and $\mathcal{E}'$ are equivalent, there is a commutative diagram
$$
\begin{array}{ccccccccc}
0 & \to & N & \to & E & \to & M & \to & 0\\
 & & \downarrow{\scriptstyle \operatorname{id}} & & \downarrow & & \downarrow{\scriptstyle \operatorname{id}} & & \\
0 & \to & N & \to & E' & \to & M & \to & 0.
\end{array}
$$
Naturality of the connecting map gives $\delta_{\mathcal{E}'}(\operatorname{id}_N) = \delta_{\mathcal{E}}(\operatorname{id}_N)$. Hence $\Phi$ is well defined.

*A split extension maps to zero.* If $\mathcal{E}$ splits, then $E \cong N \oplus M$ and the projection $E \to N$ is a retraction. The identity $\operatorname{id}_N$ extends over $E$, so it lies in the image of $\operatorname{Hom}(E,N) \to \operatorname{Hom}(N,N)$; exactness of the Hom sequence shows that its image under $\delta$ is zero.

The converse and additivity are proved by constructing the inverse (the Baer sum); see §7.6 for the full bijection.

**18.** **Strategy.** Use the periodic resolution for a cyclic group.

For $C_3 = \langle t \mid t^3 = 1\rangle$, the norm element is $N = 1 + t + t^2$, and the resolution is
$$\cdots \to \mathbb{Z}C_3 \xrightarrow{\ t-1\ } \mathbb{Z}C_3 \xrightarrow{\ N\ } \mathbb{Z}C_3 \xrightarrow{\ t-1\ } \mathbb{Z}C_3 \xrightarrow{\ \varepsilon\ } \mathbb{Z} \to 0.$$
Applying $\operatorname{Hom}_{\mathbb{Z}C_3}(-,\mathbb{Z})$ gives
$$\cdots \to \mathbb{Z} \xrightarrow{\ 0\ } \mathbb{Z} \xrightarrow{\ 3\ } \mathbb{Z} \xrightarrow{\ 0\ } \mathbb{Z} \to 0.$$
Hence
$$H^0 = \mathbb{Z}, \qquad H^1 = \ker 3/\operatorname{im}0 = 0, \qquad H^2 = \ker 0/\operatorname{im}3 = \mathbb{Z}/3,$$
and the pattern repeats:
$$H^n(C_3,\mathbb{Z}) = \begin{cases}\mathbb{Z}, & n = 0,\\ 0, & n \text{ odd},\\ \mathbb{Z}/3, & n \text{ even and } n \ge 2.\end{cases}$$

**19.** **Strategy.** Use the bar resolution in low degrees.

For $H^1$: a $1$-cochain is a map $\varphi : G \to M$. The cocycle condition is
$$(d\varphi)(g,h) = g\varphi(h) - \varphi(gh) + \varphi(g) = 0,$$
that is, $\varphi(gh) = g\varphi(h) + \varphi(g)$, which is exactly the derivation condition. A coboundary is $\varphi(g) = (d m)(g) = gm - m$, a principal derivation. Hence $H^1(G,M) = \operatorname{Der}(G,M)/\operatorname{Inn}(G,M)$.

For $H_1$: use the bar resolution in degrees $0$ and $1$. Tensoring with $\mathbb{Z}$ over $\mathbb{Z}G$ gives $C_0 \otimes \mathbb{Z} = \mathbb{Z}$ and $C_1 \otimes \mathbb{Z}$ free on symbols $[g]$. The boundary is $\partial_1[g] = g[e] - [e] = 0$ after tensoring because $g$ acts trivially on $\mathbb{Z}$. In degree $2$, $\partial_2[g|h] = [g] - [gh] + [h]$ (again after tensoring), so in $H_1$ the relations $[gh] = [g] + [h]$ hold. Thus $H_1(G,\mathbb{Z})$ is the abelian group generated by the symbols $[g]$ subject to the relations of the abelianization, namely
$$H_1(G,\mathbb{Z}) \cong G^{\mathrm{ab}} = G/[G,G].$$

**20.** **Strategy.** Prove injectivity and surjectivity of the middle map by diagram chases.

Consider the diagram
$$
\begin{array}{ccccccccc}
A & \xrightarrow{f} & B & \xrightarrow{g} & C & \xrightarrow{h} & D & \xrightarrow{k} & E\\
\downarrow{\alpha} & & \downarrow{\beta} & & \downarrow{\gamma} & & \downarrow{\delta} & & \downarrow{\varepsilon}\\
A' & \xrightarrow{f'} & B' & \xrightarrow{g'} & C' & \xrightarrow{h'} & D' & \xrightarrow{k'} & E',
\end{array}
$$
with exact rows and $\alpha,\beta,\delta,\varepsilon$ isomorphisms.

*Injectivity of $\gamma$.* Let $c \in C$ with $\gamma(c) = 0$. Since $h : C \to D$ and $\delta$ is an isomorphism, $\delta(h(c)) = h'(\gamma(c)) = 0$. Since $\delta$ is injective, $h(c) = 0$, so $c = g(b)$ for some $b \in B$ by exactness at $C$. Then $g'(\beta(b)) = \gamma(g(b)) = \gamma(c) = 0$, so $\beta(b) = f'(a')$ for some $a' \in A'$. Since $\alpha$ is surjective, $a' = \alpha(a)$ for some $a \in A$. Then $\beta(b) = f'\alpha(a) = \beta(f(a))$, so $\beta(b - f(a)) = 0$. Since $\beta$ is injective, $b = f(a)$, hence $c = g(b) = g(f(a)) = 0$.

*Surjectivity of $\gamma$.* Let $c' \in C'$. Set $d' = h'(c')$. Since $\delta$ is surjective, choose $d \in D$ with $\delta(d) = d'$. Then
$$k'\delta(d) = k'h'(c') = 0,$$
because the bottom row is exact at $D'$. By commutativity $k'\delta(d) = \varepsilon k(d)$, so $\varepsilon k(d) = 0$. Since $\varepsilon$ is injective, $k(d) = 0$. Exactness of the top row at $D$ gives $d = h(c)$ for some $c \in C$. Then
$$h'(\gamma(c)) = \delta(h(c)) = \delta(d) = h'(c'),$$
so $h'(c' - \gamma(c)) = 0$. Exactness of the bottom row at $C'$ gives $c' - \gamma(c) = g'(b')$ for some $b' \in B'$. Since $\beta$ is surjective, $b' = \beta(b)$ for some $b \in B$. Therefore
$$c' = \gamma(c) + g'\beta(b) = \gamma(c) + \gamma(g(b)) = \gamma(c + g(b)),$$
so $c'$ is in the image of $\gamma$.

**21.** **Strategy.** Build the resolution degreewise as $Q_n = P_n \oplus R_n$ and choose the off-diagonal maps inductively.

Let $P_* \to A$ and $R_* \to C$ be projective resolutions. Set $Q_n = P_n \oplus R_n$. Define
$$\partial^Q_n = \begin{pmatrix} \partial^P_n & \psi_n\\ 0 & \partial^R_n\end{pmatrix} : P_n \oplus R_n \to P_{n-1} \oplus R_{n-1},$$
with $\psi_0 = 0$ and $\psi_n : R_n \to P_{n-1}$ chosen inductively. The inclusion $P_n \to Q_n$ and projection $Q_n \to R_n$ then form a short exact sequence of graded modules; the differentials commute with them by the block form.

At degree $0$, define $\varepsilon_Q : Q_0 \to B$ by $\varepsilon_Q(p,r) = i\varepsilon_P(p) + s(r)$, where $s : R_0 \to B$ is a lift of $\varepsilon_C$ (exists because $R_0$ is projective). It is surjective: given $b \in B$, choose $r$ with $\varepsilon_C(r) = \pi(b)$; then $b - s(r) \in \ker\pi = \operatorname{im} i$, so choose $p$ with $\varepsilon_P(p) = i^{-1}(b-s(r))$.

Inductively, suppose $\psi_{n-1}$ has been chosen so that $\partial^Q_{n-1}\partial^Q_n=0$ on the part already defined. The composite $\psi_{n-1}\partial^R_n : R_n \to P_{n-2}$ lands in $\ker\partial^P_{n-2} = \operatorname{im}\partial^P_{n-1}$. Since $R_n$ is projective, it lifts to a map $\psi_n : R_n \to P_{n-1}$ with $\partial^P_{n-1}\psi_n = -\psi_{n-1}\partial^R_n$. Then the off-diagonal part of $(\partial^Q)^2$ vanishes, and the diagonal parts vanish because $P_*$ and $R_*$ are complexes. For $n=1$, the same argument is run with the augmentation condition: choose $\psi_1$ lifting $-s\partial^R_1$ through $\varepsilon_P$. This is possible because the target lands in $\ker\varepsilon_C = \operatorname{im} i$, and $i\varepsilon_P$ is surjective onto that image.

Thus $Q_*$ is a complex of projectives and $0 \to P_* \to Q_* \to R_* \to 0$ is a short exact sequence of complexes. The associated long exact sequence in homology has $H_n(P_*)=H_n(R_*)=0$ for $n>0$, so $H_n(Q_*)=0$ for $n>0$; and $H_0(Q_*) \cong B$ by the augmentation. Hence $Q_* \to B$ is a projective resolution.

**22.** **Strategy.** Apply the long exact sequence of Ext to $0 \to K \to P \to M \to 0$ and use that $P$ is projective.

The Ext sequence in the first variable is
$$0 \to \operatorname{Hom}(M,N) \to \operatorname{Hom}(P,N) \to \operatorname{Hom}(K,N) \to \operatorname{Ext}^1(M,N) \to \operatorname{Ext}^1(P,N) = 0 \to \operatorname{Ext}^1(K,N) \to \operatorname{Ext}^2(M,N) \to \operatorname{Ext}^2(P,N)=0 \to \cdots.$$
The vanishing of $\operatorname{Ext}^k(P,N)$ for $k>0$ splits the sequence into isomorphisms $\operatorname{Ext}^{n+1}(M,N) \cong \operatorname{Ext}^n(K,N)$ for every $n \ge 0$ (with the convention that $\operatorname{Ext}^0=\operatorname{Hom}$).

**23.** **Strategy.** Use the Koszul resolution and note that all differentials vanish after tensoring with $k$.

The Koszul complex is
$$0 \to R \xrightarrow{\ d_2\ } R^2 \xrightarrow{\ d_1\ } R \to k \to 0, \qquad d_2(1) = (-y,x), \quad d_1(a,b) = xa + yb.$$
It is exact: $d_1d_2(1) = -xy + yx = 0$; $\ker d_1$ consists of pairs $(a,b)$ with $xa + yb = 0$, and since $R$ is a UFD and $x,y$ are coprime, $(a,b) = c(-y,x)$ for some $c$, so $\ker d_1 = \operatorname{im} d_2$; and $d_2$ is injective.

Tensor with $k = R/(x,y)$. Since $x$ and $y$ act by zero on $k$, all differentials become zero, and the chain groups become $k, k^2, k$ in degrees $0,1,2$. Hence
$$\operatorname{Tor}_0^R(k,k) = k, \qquad \operatorname{Tor}_1^R(k,k) = k^2, \qquad \operatorname{Tor}_2^R(k,k) = k, \qquad \operatorname{Tor}_i^R(k,k)=0 \ (i \ge 3).$$

**24.** **Strategy.** Use the long exact sequence for Tor and the vanishing of Tor on flat modules.

Let $N$ be arbitrary. The Tor sequence for $0 \to A \to B \to C \to 0$ is
$$\cdots \to \operatorname{Tor}_1(A,N) \to \operatorname{Tor}_1(B,N) \to \operatorname{Tor}_1(C,N) \to A \otimes N \to B \otimes N \to C \otimes N \to 0.$$
Since $A$ and $C$ are flat, $\operatorname{Tor}_1(A,N) = \operatorname{Tor}_1(C,N) = 0$, so exactness gives $\operatorname{Tor}_1(B,N) = 0$. For $m \ge 1$, the segment
$$\operatorname{Tor}_{m+1}(C,N) \to \operatorname{Tor}_m(A,N) \to \operatorname{Tor}_m(B,N) \to \operatorname{Tor}_m(C,N)$$
has zero outer terms, so $\operatorname{Tor}_m(B,N) = 0$. Hence $\operatorname{Tor}_n(B,N)=0$ for all $n \ge 1$ and all $N$, so $B$ is flat.

## Advanced

**25.** **Strategy.** Compare the two constructions of the connecting map.

Let
$$
\begin{array}{ccccccccc}
0 & \to & A_* & \to & B_* & \to & C_* & \to & 0\\
 & & \downarrow & & \downarrow & & \downarrow & & \\
0 & \to & A'_* & \to & B'_* & \to & C'_* & \to & 0
\end{array}
$$
be a commutative diagram of short exact sequences of complexes. Let $\partial_n : H_n(C_*) \to H_{n-1}(A_*)$ and $\partial'_n : H_n(C'_*) \to H_{n-1}(A'_*)$ be the connecting maps. For $[c] \in H_n(C_*)$, choose a lift $b \in B_n$ with $b \mapsto c$. Its image $b' \in B'_n$ lifts the image cycle $c'$. The element $\partial b \in A_{n-1}$ maps to $\partial' b' \in A'_{n-1}$, and the unique preimage $a$ of $\partial b$ maps to the unique preimage $a'$ of $\partial' b'$. Hence
$$\partial'_n([c']) = [a'] = \text{image of } [a] = \text{image of } \partial_n([c]).$$
So the ladder commutes. The other squares commute because the induced maps on homology are functorial. Exactness of both rows is Theorem 7.8.1.

**26.** **Strategy.** Lift inductively using projectivity; construct the homotopy inductively using the same property.

**Existence.** Let $P_* \to M$ and $Q_* \to N$ be projective resolutions and let $f : M \to N$. At degree $0$, the composite $P_0 \to M \to N$ lifts through the surjection $Q_0 \to N$ because $P_0$ is projective. Suppose $\tilde f_0,\dots,\tilde f_{n-1}$ are constructed and commute with boundaries. The composite $P_n \to P_{n-1} \xrightarrow{\tilde f_{n-1}} Q_{n-1}$ lands in $\ker(Q_{n-1}\to Q_{n-2}) = \operatorname{im}(Q_n\to Q_{n-1})$. Since $P_n$ is projective, it lifts to $\tilde f_n : P_n \to Q_n$.

**Uniqueness.** Let $\tilde f,\tilde g$ be two lifts. Construct $h_n : P_n \to Q_{n+1}$ with $\partial h_n + h_{n-1}\partial = \tilde g_n - \tilde f_n$. For $n=0$, $\tilde g_0 - \tilde f_0$ maps into $\ker(Q_0\to N) = \operatorname{im}(Q_1\to Q_0)$, so it lifts to $h_0$ by projectivity of $P_0$. Inductively,
$$\partial(\tilde g_n - \tilde f_n - h_{n-1}\partial) = (\tilde g_{n-1}-\tilde f_{n-1})\partial - \partial h_{n-1}\partial = \partial h_{n-2}\partial - \partial h_{n-1}\partial = 0,$$
so the expression lands in $\ker\partial = \operatorname{im}(Q_{n+1}\to Q_n)$ and lifts to $h_n$. This completes the induction.

**27.** **Strategy.** Use the trivial resolutions $0 \to M \to M \to 0$ for projective or flat $M$, and $0 \to N \to N \to 0$ for injective $N$.

If $M$ is projective, $0 \to M \xrightarrow{\operatorname{id}} M \to 0$ is a projective resolution (of length $0$). Applying $\operatorname{Hom}(-,N)$ gives $0 \to \operatorname{Hom}(M,N) \to \operatorname{Hom}(M,N) \to 0$, whose cohomology vanishes in positive degrees. Hence $\operatorname{Ext}^n(M,N)=0$ for $n>0$.

If $N$ is injective, $0 \to N \xrightarrow{\operatorname{id}} N \to 0$ is an injective resolution. Applying $\operatorname{Hom}(M,-)$ gives an exact sequence, so $R^n\operatorname{Hom}(M,-)(N)=0$ for $n>0$.

If $M$ is flat, $0 \to M \to M \to 0$ is a flat resolution; tensoring with $N$ gives an exact sequence $0 \to M\otimes N \to M\otimes N \to 0$, so $\operatorname{Tor}_n(M,N)=0$ for $n>0$.

**28.** **Strategy.** Compute the case $n=1$ directly, then shift dimension repeatedly.

For $n=1$, use $0 \to \mathbb{Z} \xrightarrow{m} \mathbb{Z} \to \mathbb{Z}/m \to 0$ and apply $\operatorname{Hom}(- ,N)$:
$$0 \to \operatorname{Hom}(\mathbb{Z}/m,N) \to N \xrightarrow{\ m\ } N \to \operatorname{Ext}^1(\mathbb{Z}/m,N) \to 0.$$
Hence $\operatorname{Ext}^1(\mathbb{Z}/m,N) \cong N/mN$.

For $n \ge 2$, apply dimension shifting (Exercise 22) with $K = \mathbb{Z}$ and $P = \mathbb{Z}$:
$$\operatorname{Ext}^n(\mathbb{Z}/m,N) \cong \operatorname{Ext}^{n-1}(\mathbb{Z},N) = 0,$$
because $\mathbb{Z}$ is projective. Hence all higher Ext groups vanish.

**29.** **Strategy.** Identify $\operatorname{Hom}_{\mathbb{Z}G}(B_n,M)$ with functions on $G^n$ and dualize the bar differential.

A $\mathbb{Z}G$-linear map $\varphi : B_n \to M$ is determined by its values on the basis elements $[g_1|\cdots|g_n]$, and conversely any function $\varphi : G^n \to M$ extends uniquely by $\mathbb{Z}G$-linearity. Hence $\operatorname{Hom}_{\mathbb{Z}G}(B_n,M) \cong \operatorname{Maps}(G^n,M)$.

The coboundary is $d^n\varphi = \varphi \circ \partial_{n+1}$. Using
$$\partial_{n+1}[g_1|\cdots|g_{n+1}] = g_1[g_2|\cdots|g_{n+1}] + \sum_{i=1}^{n}(-1)^i[g_1|\cdots|g_ig_{i+1}|\cdots|g_{n+1}] + (-1)^{n+1}[g_1|\cdots|g_n]$$
and $\varphi(g_1[g_2|\cdots]) = g_1\varphi([g_2|\cdots])$ gives
$$(d\varphi)(g_1,\dots,g_{n+1}) = g_1\varphi(g_2,\dots,g_{n+1}) + \sum_{i=1}^{n}(-1)^i\varphi(g_1,\dots,g_ig_{i+1},\dots,g_{n+1}) + (-1)^{n+1}\varphi(g_1,\dots,g_n).$$

For $n=0$, $C^0(G,M)=M$ and $(d m)(g) = gm - m$, so $H^0 = M^G$. For $n=1$, the cocycle condition is the derivation condition, and coboundaries are principal derivations, so $H^1 = \operatorname{Der}/\operatorname{Inn}$.

**30.** **Strategy.** Use restriction to the trivial subgroup and the corestriction (transfer).

For a subgroup $H \le G$ of finite index, there are maps
$$\operatorname{res} : H^n(G,M) \to H^n(H,M), \qquad \operatorname{cor} : H^n(H,M) \to H^n(G,M)$$
with $\operatorname{cor} \circ \operatorname{res} = [G:H]\cdot\operatorname{id}$. The map $\operatorname{cor}$ is induced on the bar resolution by summing over coset representatives; it is a chain map and satisfies the identity.

Take $H = 1$. Then $H^n(1,M) = 0$ for $n \ge 1$ because the trivial group has cohomological dimension $0$. The composite
$$H^n(G,M) \xrightarrow{\operatorname{res}} H^n(1,M) = 0 \xrightarrow{\operatorname{cor}} H^n(G,M)$$
is therefore zero, but it equals multiplication by $[G:1] = |G|$. Hence $|G| \cdot H^n(G,M) = 0$ for $n \ge 1$.

**31.** **Strategy.** Read off the two lowest degrees from the convergence filtration.

Let $E_r^{p,q}$ be a first-quadrant cohomological spectral sequence with $d_r : E_r^{p,q} \to E_r^{p+r,q-r+1}$ and $E_\infty^{p,q} = F^pH^{p+q}/F^{p+1}H^{p+q}$, where $F^\bullet$ is a decreasing filtration with $F^0H^n=H^n$ and $F^{n+1}H^n=0$.

*Degree $1$.* We have $E_\infty^{1,0} = F^1H^1/F^2H^1 = F^1H^1$ and $E_\infty^{0,1} = F^0H^1/F^1H^1 = H^1/F^1H^1$. Hence there is a short exact sequence
$$0 \to E_\infty^{1,0} \to H^1 \to E_\infty^{0,1} \to 0.$$
Since $d_2 : E_2^{1,0} \to E_2^{3,-1} = 0$, we have $E_\infty^{1,0} = E_2^{1,0}$. Since $d_2 : E_2^{-2,2} = 0 \to E_2^{0,1}$, we have $E_\infty^{0,1} = \ker(d_2 : E_2^{0,1} \to E_2^{2,0})$.

*Degree $2$.* We have $E_\infty^{2,0} = F^2H^2/F^3H^2 = F^2H^2$, and
$$E_\infty^{2,0} = \frac{\ker(d_2 : E_2^{2,0} \to E_2^{4,-1}=0)}{\operatorname{im}(d_2 : E_2^{0,1} \to E_2^{2,0})} = \operatorname{coker}(d_2 : E_2^{0,1} \to E_2^{2,0}).$$
Therefore the sequence
$$0 \to E_2^{1,0} \to H^1 \to E_2^{0,1} \xrightarrow{\ d_2\ } E_2^{2,0} \to H^2$$
is exact: the first map is injective by the degree-$1$ sequence; the middle map has image $\ker d_2$; the map $E_2^{2,0} \to H^2$ has kernel $\operatorname{im} d_2$ and is injective on the cokernel by the description of $E_\infty^{2,0}$.

**32.** **Strategy.** Put the abelian structure on each degree and check the axioms degreewise.

Define a chain map $f : C_* \to D_*$ degreewise. The **kernel** is the complex with $(\ker f)_n = \ker f_n$ and the induced differential; the **cokernel** is $(D_n/\operatorname{im} f_n)$ with the induced differential. These are well defined because $f$ commutes with $\partial$.

A chain map is a **monomorphism** iff each $f_n$ is injective, and an **epimorphism** iff each $f_n$ is surjective. Indeed, a chain map $g$ with $f g = 0$ is zero iff each $g_n = 0$ when $f_n$ is injective, and the dual statement holds for surjections.

Every monomorphism $f : A_* \to B_*$ is the kernel of its cokernel: degreewise, $A_n \to B_n \to B_n/A_n$ is exact, and the kernel of $B_* \to B_*/A_*$ is exactly $A_*$. Every epimorphism is the cokernel of its kernel by the dual argument. Finite direct sums are formed degreewise, and the category is additive. Exactness of a sequence of complexes is equivalent to exactness in each degree, because kernels and images are computed degreewise. Hence $\mathbf{Ch}(R)$ is abelian.

Homology $H_n : \mathbf{Ch}(R) \to R\text{-}\mathbf{Mod}$ is an additive functor, but it is neither left nor right exact in general: a short exact sequence of complexes gives a long exact sequence, not a short one.

## Challenge

**33.** **Strategy.** Reduce the statement to a finite diagram, embed the small abelian subcategory generated by it into modules, and use the five lemma there.

The five lemma is a statement about a single commutative diagram with five columns, two exact rows and five vertical maps. Let $\mathcal{D}$ be the set of objects and morphisms appearing in the diagram. Let $\mathcal{A}_0$ be the smallest full subcategory of the ambient abelian category $\mathcal{A}$ containing $\mathcal{D}$ and closed under finite direct sums, kernels, cokernels and extensions of morphisms. Then $\mathcal{A}_0$ is a small abelian category: it is generated by finitely many objects under finitely many finite operations, so its objects form a set, and the abelian axioms are inherited from $\mathcal{A}$.

By the Freyd–Mitchell theorem, there is a full, faithful and exact functor $F : \mathcal{A}_0 \to R\text{-}\mathbf{Mod}$ for some ring $R$. Exactness means that $F$ preserves kernels and cokernels, hence preserves exact sequences. Full faithfulness means that the commutative diagram and its exact rows are carried to a commutative diagram with exact rows in $R\text{-}\mathbf{Mod}$, and the vertical maps remain isomorphisms (a functor preserves isomorphisms).

The five lemma holds in $R\text{-}\mathbf{Mod}$ by Exercise 20. Applying it to $F(\mathcal{D})$ shows that $F(\gamma)$ is an isomorphism. Since $F$ is full and faithful, $\gamma$ is an isomorphism in $\mathcal{A}_0$, hence in $\mathcal{A}$. Therefore the five lemma holds in every abelian category.

**34.** **Strategy.** Apply the Grothendieck spectral sequence to the composite of invariants.

Let $Q = G/N$. The functor
$$F = (-)^N : \mathbb{Z}G\text{-}\mathbf{Mod} \to \mathbb{Z}Q\text{-}\mathbf{Mod}$$
is left exact, and the functor $G_0 = (-)^Q : \mathbb{Z}Q\text{-}\mathbf{Mod} \to \mathbf{Ab}$ is left exact. Their composite is $(-)^G$. The category $\mathbb{Z}G\text{-}\mathbf{Mod}$ has enough injectives, and injective $\mathbb{Z}G$-modules are coinduced, hence are $G_0$-acyclic (their $Q$-invariants are coinduced and have vanishing higher cohomology). The Grothendieck spectral sequence (Theorem 8.12) therefore gives
$$E_2^{p,q} = H^p\bigl(Q, H^q(N,M)\bigr) \Longrightarrow H^{p+q}(G,M).$$

Apply the five-term exact sequence of Exercise 31:
$$0 \to E_2^{1,0} \to H^1(G,M) \to E_2^{0,1} \to E_2^{2,0} \to H^2(G,M).$$
Here
$$E_2^{1,0} = H^1(Q, H^0(N,M)) = H^1(Q,M^N), \qquad E_2^{0,1} = H^0(Q,H^1(N,M)) = H^1(N,M)^Q,$$
$$E_2^{2,0} = H^2(Q,H^0(N,M)) = H^2(Q,M^N).$$
The resulting sequence is
$$0 \to H^1(Q,M^N) \to H^1(G,M) \to H^1(N,M)^Q \to H^2(Q,M^N) \to H^2(G,M),$$
which is the inflation-restriction sequence.

**35.** **Strategy.** Use the Serre spectral sequence of the path fibration and the fact that the total space is contractible.

The path–loop fibration $\Omega S^n \to P S^n \to S^n$ has contractible total space $P S^n$ (the path space based at a point). The Serre spectral sequence has
$$E^2_{p,q} = H_p(S^n; H_q(\Omega S^n;\mathbb{Q})) \Longrightarrow H_{p+q}(P S^n;\mathbb{Q}).$$
Since $P S^n$ is contractible, the abutment is $\mathbb{Q}$ in degree $0$ and $0$ otherwise. The only nonzero columns of $E^2$ are $p=0$ and $p=n$.

*Case $n=2$.* The differential $d^2 : E^2_{2,q} \to E^2_{0,q+1}$ must be an isomorphism for every $q \ge 0$: the term $E^\infty_{2,q}$ contributes to $H_{q+2}(PS^2)=0$, so $d^2$ is injective; the term $E^\infty_{0,q+1}$ contributes to $H_{q+1}(PS^2)=0$, so $d^2$ is surjective. Hence $H_q(\Omega S^2;\mathbb{Q}) \cong H_{q-1}(\Omega S^2;\mathbb{Q})$ for $q \ge 1$. Since $\Omega S^2$ is path-connected, $H_0 = \mathbb{Q}$, and induction gives $H_q(\Omega S^2;\mathbb{Q}) = \mathbb{Q}$ for every $q \ge 0$.

*Case $n=3$.* Now the differential is $d^3 : E^3_{3,q} \to E^3_{0,q+2}$, and the same argument shows it is an isomorphism for every $q \ge 0$. Hence $H_{q+2}(\Omega S^3;\mathbb{Q}) \cong H_q(\Omega S^3;\mathbb{Q})$. We have $H_0 = \mathbb{Q}$; also $H_1 = 0$ because $\pi_1(\Omega S^3) = \pi_2(S^3) = 0$, so $H_1(\Omega S^3;\mathbb{Q}) = 0$. Therefore
$$H_q(\Omega S^3;\mathbb{Q}) = \begin{cases}\mathbb{Q}, & q \text{ even},\\ 0, & q \text{ odd}.\end{cases}$$

**36.** **Strategy.** Tensor commutes with colimits, and homology of a filtered colimit of complexes is the colimit of the homologies.

Let $N = \operatorname{colim}_{i \in I} N_i$ be a filtered colimit and let $P_* \to M$ be a projective resolution. Tensor products commute with colimits, so
$$P_* \otimes_R N \cong P_* \otimes_R \operatorname{colim}_i N_i \cong \operatorname{colim}_i (P_* \otimes_R N_i).$$
Filtered colimits are exact in $R\text{-}\mathbf{Mod}$, so homology commutes with them:
$$\operatorname{Tor}_n^R(M,N) = H_n(P_* \otimes N) \cong \operatorname{colim}_i H_n(P_* \otimes N_i) = \operatorname{colim}_i \operatorname{Tor}_n^R(M,N_i).$$

*Every module is a filtered colimit of finitely presented modules.* Consider the category whose objects are finitely presented $R$-modules $P$ equipped with a map $P \to M$, and whose morphisms are commutative triangles. This category is filtered: any two such maps are dominated by the finitely presented module generated by their images and the relations among them, and the canonical map $\operatorname{colim} P \to M$ is an isomorphism because every element of $M$ and every relation among finitely many elements is witnessed by a finitely presented module.

*Flatness criterion.* A module $M$ is flat iff for every finitely generated ideal $I \subseteq R$, the map $M \otimes I \to M$ is injective. But $\operatorname{Tor}_1^R(M,R/I)$ is exactly the kernel of this map, so the condition is $\operatorname{Tor}_1^R(M,R/I)=0$ for every finitely generated ideal $I$. Since $\operatorname{Tor}_1$ commutes with filtered colimits and every module is a filtered colimit of finitely presented modules, checking this on finitely generated ideals suffices to conclude $\operatorname{Tor}_1^R(M,N)=0$ for all $N$, which is equivalent to flatness.
