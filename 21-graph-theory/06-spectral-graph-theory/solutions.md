# Spectral Graph Theory — Solutions

> [Spectral Graph Theory](README.md) · Solutions to the 36 problems in [exercises.md](exercises.md)

Each solution states its strategy, then carries out every step. Numerical answers are given exactly where
possible and to three decimals otherwise.

## Beginner

**1.** *Strategy: use the standard families from Section 7.2 and check the two trace identities.*

(a) $P_3$: $A=\begin{pmatrix}0&1&0\\1&0&1\\0&1&0\end{pmatrix}$, so
$\det(\lambda I-A)=\lambda^3-2\lambda=\lambda(\lambda^2-2)$ and the spectrum is
$\sqrt2,\,0,\,-\sqrt2$. Sum $=0$ ✓; squares $=2+0+2=4=2m$ ✓.
(b) $K_{1,3}$: star formula, $\sqrt3,\,0,\,0,\,-\sqrt3$. Sum $0$ ✓; squares $6=2m$ ✓.
(c) $C_4$: $2,\,0,\,0,\,-2$. Sum $0$ ✓; squares $8=2m$ ✓.
(d) $K_4$: $3,\,-1,\,-1,\,-1$. Sum $0$ ✓; squares $9+3=12=2m$ ✓.

**2.** *Strategy: the cycle formula plus the walk interpretation of $\operatorname{tr}(A^k)$.*

(a) $2\cos(2\pi k/5)$ for $k=0,\dots,4$: $2,\ 0.618,\ 0.618,\ -1.618,\ -1.618$.
(b) Squares: $4+2(0.382)+2(2.618)=4+0.764+5.236=10=2\cdot5$ ✓.
(c) $\operatorname{tr}(A^3)=\sum_i\lambda_i^3=8+2(0.236)+2(-4.236)=8+0.472-8.472=0$. This is Lemma 7.1.1(4):
  $\operatorname{tr}(A^3)=6\cdot(\text{triangles})$, and $C_5$ has no triangle, so the sum must vanish.
  For $K_4$: $\operatorname{tr}(A^3)=27+3(-1)=24$, hence $24/6=4$ triangles — and indeed every one of the
  $\binom43=4$ triples of vertices spans a triangle.

**3.** *Strategy: $(A^k)_{uv}$ counts walks of length $k$; compute by summing over intermediate vertices.*

$(A^2)_{13}=\sum_wA_{1w}A_{w3}=\lvert N(1)\cap N(3)\rvert=\lvert\{2\}\rvert=1$: exactly one walk of length
$2$, namely $1$–$2$–$3$. $(A^2)_{14}=\lvert N(1)\cap N(4)\rvert$, and $N(4)=\{1\}$, $N(1)=\{2,3,4\}$, so
the intersection is empty and $(A^2)_{14}=0$: no walk of length $2$ from $1$ to $4$ (the shortest is $14$,
of length $1$). $(A^3)_{14}=\sum_w(A^2)_{1w}A_{w4}$; only $w=1$ contributes because $A_{14}=1$ and
$A_{w4}=0$ otherwise, giving $(A^2)_{11}=\deg(1)=3$. The three walks are $1$–$2$–$1$–$4$,
$1$–$3$–$1$–$4$ and $1$–$4$–$1$–$4$.

**4.** *Strategy: compute $\operatorname{tr}(A^4)=\sum\lambda_i^4$ and compare with a direct count.*

$\operatorname{tr}(A^4)=2^4+0+0+(-2)^4=32$. By Lemma 7.1.1(3), this counts closed walks of length $4$. From
a fixed vertex of $C_4$, a closed walk of length $4$ is a sequence of four steps $\pm1$ whose sum is
$0\bmod 4$: the six sequences with two $+$ and two $-$ and the two constant sequences $++++$ and $----$,
so $8$ walks per vertex and $4\cdot8=32$ in total ✓.

**5.** *Strategy: write $L=D-A$ and verify the quadratic form twice.*

(a) $D=\operatorname{diag}(1,2,2,1)$ and $A$ is the path adjacency, so
$$L=\begin{pmatrix}1&-1&0&0\\-1&2&-1&0\\0&-1&2&-1\\0&0&-1&1\end{pmatrix}.$$
(b) By Section 7.5 the eigenvalues are $2-2\cos(k\pi/4)$, $k=0,1,2,3$:
$0,\ 2-\sqrt2\approx0.586,\ 2,\ 2+\sqrt2\approx3.414$.
(c) $Lx=(0,2,-2,0)$ for $x=(1,1,-1,-1)$, so $x^{\mathsf T}Lx=0+2+2+0=4$. Directly from the identity: the
edge differences are $x_1-x_2=0$, $x_2-x_3=2$, $x_3-x_4=0$, so the sum of squares is $4$ ✓.

**6.** *Strategy: Theorem 7.5.3 — the multiplicity of $0$ is the number of components.*

(a) Two zeros: $2$ components. (b) One zero: $1$ component. (c) Three zeros: $3$ components. In each case
the remaining eigenvalues are positive, as they must be for a Laplacian.

**7.** *Strategy: Theorem 7.4.1 — check whether the multiset is symmetric under $\lambda\mapsto-\lambda$.*

(a) $2,0,0,-2$: symmetric ✓ bipartite (e.g. $C_4$). (b) $1.732,0,0,-1.732$: symmetric ✓ bipartite
(this is $K_{1,3}$). (c) $2.562,0,-1,-1.562$: not symmetric — $2.562$ has no partner $-2.562$, so **not**
bipartite; the graph is $K_4$ minus an edge, which contains a triangle. (d) $3,1,1,1,-1,-1,-1,-3$:
symmetric ✓ bipartite (this is the cube $Q_3$, which is bipartite).

**8.** *Strategy: $\rho=\max_i\lvert\lambda_i\rvert$; for these families the spectrum is known.*

(a) $K_{1,4}$: $\pm2$ and $0^{(3)}$, so $\rho=2$. (b) $C_6$: $\pm2$, $\pm1$, $\pm1$, so $\rho=2$.
(c) $K_5$: $4$ and $-1^{(4)}$, so $\rho=4=\Delta$. (d) The Petersen graph has spectrum
$3,1^{(5)},-2^{(4)}$, so $\rho=3$.

**9.** *Strategy: $\tau=\frac1n\prod_{i\ge2}\mu_i$ and the cycle Laplacian formula.*

The Laplacian eigenvalues of $C_5$ are $2-2\cos(2\pi k/5)$, i.e. $0,\ 1.382,\ 1.382,\ 3.618,\ 3.618$.
These are $\frac{5-\sqrt5}{2}$ and $\frac{5+\sqrt5}{2}$, whose product is $\frac{25-5}{4}=5$, so the
product of the non-zero eigenvalues is $5^2=25$ and
$$\tau(C_5)=\tfrac15\cdot25=5 .$$
Direct check: a spanning tree of $C_5$ omits exactly one of the five edges (omitting none leaves the
cycle, omitting two disconnects), so there are $5$ ✓.

**10.** *Strategy: $P=D^{-1}A=\frac12A$ for a $2$-regular graph.*

With vertices $1,2,3,4$ cyclically, $P$ has rows $(0,\frac12,0,\frac12)$, $(\frac12,0,\frac12,0)$ and so on;
$P=\frac12A$. The uniform distribution is stationary by Lemma 7.8.1. Starting at $1$:
$p_1=(0,0.5,0,0.5)$ and $p_2=(0.5,0,0.5,0)$. The walk does **not** converge: $C_4$ is bipartite, so the
eigenvalue $-1$ of $P$ (from $\lambda_n=-2$) makes the distribution oscillate with period $2$ — after an
even number of steps only the vertices at even distance from $1$ carry mass. This is exactly the failure
of aperiodicity discussed in Section 7.8 and item 11.7.

**11.** *Strategy: Cauchy interlacing, $\lambda_i(A)\ge\lambda_i(B)\ge\lambda_{i+1}(A)$ for a $3\times3$
principal submatrix of a $4\times4$ matrix.*

The windows are $\lambda_1(B)\in[1,3]$, $\lambda_2(B)\in[-1,1]$, $\lambda_3(B)\in[-2,-1]$.

(a) $2,0,-2$: $2\in[1,3]$, $0\in[-1,1]$, $-2\in[-2,-1]$ — **possible**.
(b) $2,1,0$: $0\notin[-2,-1]$ — **impossible**.
(c) $3,1,-1$: $3\in[1,3]$, $1\in[-1,1]$, $-1\in[-2,-1]$ — **possible**.
(d) $1.5,0.5,-1.5$: all three in their windows — **possible**.

**12.** *Strategy: compare multisets.*

$\operatorname{spec}(P_4)=\{1.618,0.618,-0.618,-1.618\}$ and $\operatorname{spec}(K_{1,3})=\{1.732,0,0,-1.732\}$:
not cospectral. $\operatorname{spec}(C_4)=\{2,0,0,-2\}\ne\{1.732,0,0,-1.732\}=\operatorname{spec}(K_{1,3})$:
also not cospectral. (Both pairs are, however, *bipartite*, which is why all four spectra are symmetric.)

## Intermediate

**13.** *Strategy: read the traces off the matrix and use $\operatorname{tr}M=\sum_i\lambda_i$.*

The diagonal of $A$ is zero, so $\operatorname{tr}A=0$; since the eigenvalues of $A$ are its diagonal
entries after orthogonal diagonalisation, $\operatorname{tr}A=\sum_i\lambda_i$ and the first identity
follows. For the second, $\operatorname{tr}(A^2)=\sum_{u,v}A_{uv}A_{vu}=\sum_{u,v}A_{uv}^2$ (symmetry), and
$A_{uv}^2=1$ exactly for the $2m$ ordered pairs $(u,v)$ with $uv\in E$. Thus $\operatorname{tr}(A^2)=2m$;
and $\operatorname{tr}(A^2)=\sum_i\lambda_i^2$ because the eigenvalues of $A^2$ are $\lambda_i^2$.

**14.** *Strategy: Rayleigh quotient at the all-ones vector.*

$\lambda_1=\max_{x\ne0}R_A(x)\ge R_A(\mathbf{1})=\dfrac{\mathbf{1}^{\mathsf T}A\mathbf{1}}{\mathbf{1}^{\mathsf T}\mathbf{1}}
=\dfrac{\sum_{u,v}A_{uv}}{n}=\dfrac{2m}{n}$.

If $G$ is $d$-regular then $2m/n=d$ and $\lambda_1\ge d$; but $\mathbf{1}$ is an eigenvector with
eigenvalue $d$, so $\lambda_1=d$ and equality holds. Conversely, if $\lambda_1=2m/n$ then $\mathbf{1}$
realises the maximum of the Rayleigh quotient, so $\mathbf{1}$ is an eigenvector of $A$: $A\mathbf{1}$ has
all entries equal to $\lambda_1$, i.e. $\deg(u)=\lambda_1$ for every $u$, and $G$ is regular.

**15.** *Strategy: block-diagonal matrices.*

Order the vertices component by component; then $A=\begin{pmatrix}A_1&0\\0&A_2\end{pmatrix}$ and
$\det(\lambda I-A)=\det(\lambda I-A_1)\det(\lambda I-A_2)$, so the characteristic polynomial is the product
and the spectra multiply as multisets: $\operatorname{spec}(G)=\operatorname{spec}(G_1)\cup\operatorname{spec}(G_2)$.
The same argument applies to $L=\begin{pmatrix}L_1&0\\0&L_2\end{pmatrix}$. Induction extends both statements
to any finite number of components.

**16.** *Strategy: combine Theorem 7.4.1 with Corollaries 7.3.2 and 7.4.2.*

($\Rightarrow$) If $G$ is bipartite, Theorem 7.4.1 makes $-\lambda_1$ an eigenvalue; by Corollary 7.3.2,
$\lambda_1$ is the spectral radius, so $-\lambda_1$ is the smallest eigenvalue and $\lambda_n=-\lambda_1$.
($\Leftarrow$) If $\lambda_n=-\lambda_1$ then $\lvert\lambda_n\rvert=\lambda_1$, so $A$ cannot be primitive;
by Corollary 7.3.2 a connected non-bipartite graph has $\lvert\lambda_i\rvert<\lambda_1$ for $i\ge2$, hence
$G$ is bipartite.

**17.** *Strategy: expand the sum of squares.*

$$\sum_{uv\in E}(x_u-x_v)^2=\sum_{uv\in E}(x_u^2+x_v^2)-2\sum_{uv\in E}x_ux_v
=\sum_{u}\deg(u)x_u^2-2\,x^{\mathsf T}Ax=x^{\mathsf T}Dx-x^{\mathsf T}Ax=x^{\mathsf T}Lx,$$
using that each $x_u^2$ appears once for every edge at $u$ and that $\sum_{uv\in E}x_ux_v=\frac12x^{\mathsf T}Ax\cdot2$
counts each edge twice in $x^{\mathsf T}Ax$ (once as $x_ux_v$ and once as $x_vx_u$). Since the left side is a
sum of squares, $x^{\mathsf T}Lx\ge0$: $L$ is positive semidefinite. Taking $x=\mathbf{1}$ gives
$\mathbf{1}^{\mathsf T}L\mathbf{1}=\sum_{uv}0=0$, and since $L$ is symmetric and positive semidefinite this
forces $L\mathbf{1}=0$.

**18.** *Strategy: the two inclusions of Theorem 7.5.3.*

$(\supseteq)$ If $x=\mathbf{1}_{C}$ for a component $C$, then $x_u-x_v=0$ for every edge (an edge never joins
two components), so $x^{\mathsf T}Lx=0$ and, $L$ being positive semidefinite, $Lx=0$. Distinct components
give linearly independent indicators, so the nullity is at least the number $c$ of components.
$(\subseteq)$ If $Lx=0$ then $x^{\mathsf T}Lx=\sum_{uv}(x_u-x_v)^2=0$, so every edge has $x_u=x_v$: $x$ is
constant on each component, hence a linear combination of the $c$ indicator vectors. So the nullity is
exactly $c$.

**19.** *Strategy: $L=dB-A$ for regular graphs, and the direct eigenvector analysis for $K_{m,n}$.*

$K_n$: $L=nI-J$, so on $\mathbf{1}$ the eigenvalue is $0$ and on the $(n-1)$-dimensional
$\mathbf{1}^{\perp}$ we have $J=0$ and $L=nI$: spectrum $0,n^{(n-1)}$. Hence
$\tau(K_n)=\frac1n n^{n-1}=n^{n-2}$, Cayley's formula.

$K_{m,n}$: eigenvectors constant on each side give eigenvalue $m$ on the $A$-side functions of sum $0$
(dimension $n-1$) and $n$ on the $B$-side functions of sum $0$ (dimension $m-1$); the bipartition vector
$(+1$ on $A$, $-1$ on $B$) gives eigenvalue $m+n$; the constant vector gives $0$. So the spectrum is
$0,\ m^{(n-1)},\ n^{(m-1)},\ m+n$ and
$$\tau(K_{m,n})=\frac{1}{m+n}\,m^{n-1}n^{m-1}(m+n)=m^{n-1}n^{m-1}.$$

**20.** *Strategy: compare $L$ with $dI-A$.*

If $G$ is $d$-regular then $D=dI$, so $L=D-A=dI-A$: the two matrices have the same eigenvectors, and each
eigenvalue of $L$ is $d$ minus an eigenvalue of $A$. As multisets, $\operatorname{spec}(L)=d-\operatorname{spec}(A)$;
with the standard orderings $\lambda_1\ge\cdots\ge\lambda_n$ and $0=\mu_1\le\cdots\le\mu_n$ this reads
$\mu_i=d-\lambda_i$, consistent with $\lambda_1=d$ and $\mu_1=0$. The argument fails for a non-regular graph
because $D\ne dI$: for $P_4$ the number $d$ is not even defined, and indeed $2-\lambda_1=0.382$ while
$\mu_2=0.586$.

**21.** *Strategy: $\tau=\frac1n\prod_{i\ge2}\mu_i$ with $n=5$.*

Pair the conjugate eigenvalues:
$$\frac{5-\sqrt5}{2}\cdot\frac{5+\sqrt5}{2}=\frac{25-5}{4}=5,\qquad
\frac{7-\sqrt5}{2}\cdot\frac{7+\sqrt5}{2}=\frac{49-5}{4}=11 .$$
So $\prod_{i\ge2}\mu_i=5\cdot11=55$ and $\tau=\frac{55}{5}=11$. As a check, the house graph has $6$ edges
and is connected, so a spanning tree is obtained by deleting $2$ edges; of the $\binom62=15$ pairs, exactly
$11$ leave a connected graph. The four failures isolate a vertex (deleting the two edges at one of the
degree-$2$ vertices $0,3,4$) or split the square from the apex (deleting $01$ and $23$).

**22.** *Strategy: $P=(\mathbf{1}\mathbf{1}^{\mathsf T}-I)/(n-1)$ for $K_n$.*

For $K_4$, $P=\frac13(J-I)$. On $\mathbf{1}$: eigenvalue $1$. On $\mathbf{1}^{\perp}$: $J=0$, so
$P=-\frac13I$ and the eigenvalue is $-1/3$ with multiplicity $3$. Hence $\theta_*=\frac13$. Also
$P^2=\frac19(J-I)^2=\frac19(4J-2J+I)=\frac19(2J+I)$, so after two steps from a vertex $v$,
$(P^2)_{vv}=\frac13$ and $(P^2)_{vw}=\frac29$ for $w\ne v$. With $\pi=\frac14$,
$$\tfrac12\lVert p_2-\pi\rVert_1=\tfrac12\Bigl(\bigl\lvert\tfrac13-\tfrac14\bigr\rvert+3\bigl\lvert\tfrac29-\tfrac14\bigr\rvert\Bigr)
=\tfrac12\Bigl(\tfrac1{12}+\tfrac3{36}\Bigr)=\tfrac1{12},$$
so two steps already give total variation $1/12$ — mixing in a constant number of steps.

**23.** *Strategy: test vector equal to $n-1$ at a minimum-degree vertex and $-1$ elsewhere.*

Let $v$ have degree $\delta=\delta(G)$ and set $x_v=n-1$, $x_u=-1$ for $u\ne v$. Then
$\sum_ux_u=(n-1)-(n-1)=0$, so $x\perp\mathbf{1}$ and $R_L(x)\ge\mu_2$. Moreover
$x^{\mathsf T}x=(n-1)^2+(n-1)=n(n-1)$, and in $\sum_{uv}(x_u-x_v)^2$ only the $\delta$ edges at $v$
contribute, each contributing $n^2$. Hence
$$\mu_2\le R_L(x)=\frac{\delta n^2}{n(n-1)}=\frac{n}{n-1}\,\delta .$$

**24.** *Strategy: compare the two quadratic forms on the same subspace.*

Let $e_u,e_v$ be the endpoints of the added edge and $L'=L+(e_u-e_v)(e_u-e_v)^{\mathsf T}$. For every $x$,
$$x^{\mathsf T}L'x=x^{\mathsf T}Lx+(x_u-x_v)^2\ \ge\ x^{\mathsf T}Lx .$$
Both $L$ and $L'$ have $\mathbf{1}$ in their kernel, so by Lemma 7.5.5
$$\mu_2(L')=\min_{x\perp\mathbf{1}}R_{L'}(x)\ \ge\ \min_{x\perp\mathbf{1}}R_L(x)=\mu_2(L).$$
(Adding an edge corresponds to writing $L'=B'B'^{\mathsf T}$ with one more column; the same conclusion
follows from the variational formula.)

## Advanced

**25.** *Strategy: the maximum principle, applied to an eigenvector for $d$.*

($\Leftarrow$) If $G$ has $c$ components, each is $d$-regular and its indicator vector $\mathbf{1}_{C}$ satisfies
$A\mathbf{1}_{C}=d\,\mathbf{1}_{C}$; the $c$ indicators are independent, so $d$ has multiplicity at least $c$.

($\Rightarrow$) Suppose $Ax=dx$ with $x\ne0$ and choose $v$ with $\lvert x_v\rvert$ maximal. Then
$$d\lvert x_v\rvert=\Bigl\lvert\sum_{u\sim v}x_u\Bigr\rvert\le\sum_{u\sim v}\lvert x_u\rvert\le d\lvert x_v\rvert,$$
so equality holds throughout: every neighbour $u$ of $v$ has $\lvert x_u\rvert=\lvert x_v\rvert$ and $x_u$ has
the same sign as $x_v$. Hence $x_u=x_v$ for all neighbours, and by connectedness $x$ is constant, so $x$ is
a multiple of $\mathbf{1}$ and the eigenspace is one-dimensional.

Combining the two directions: the multiplicity of $d$ equals the number of connected components. In
particular $G$ is connected $\iff$ $d$ is a simple eigenvalue.

**26.** *Strategy: the matrix $B-\frac{d-\lambda_n}{n}J$ is positive semidefinite and vanishes on the
indicator of an independent set.*

Let $S$ be independent with $\lvert S\rvert=\alpha$ and let $B=A-\lambda_nI$. Since
$\lambda_n<0$ and the eigenvalues of $B$ are $\lambda_i-\lambda_n\ge0$, $B$ is positive semidefinite; also
$B\mathbf{1}=(d-\lambda_n)\mathbf{1}$. Define
$$M=B-\frac{d-\lambda_n}{n}J .$$
On $\mathbf{1}$ the eigenvalue is $(d-\lambda_n)-(d-\lambda_n)=0$; on $\mathbf{1}^{\perp}$ we have $J=0$, so
the eigenvalues are $\lambda_i-\lambda_n\ge0$. Hence $M$ is positive semidefinite. Now
$\mathbf{1}_S^{\mathsf T}B\mathbf{1}_S=\sum_{u,v\in S}A_{uv}-\lambda_n\lvert S\rvert=0-\lambda_n\alpha$ because $S$
is independent, and $\mathbf{1}_S^{\mathsf T}J\mathbf{1}_S=\alpha^2$. Therefore
$$0\le\mathbf{1}_S^{\mathsf T}M\mathbf{1}_S=-\lambda_n\alpha-\frac{d-\lambda_n}{n}\alpha^2,$$
and dividing by $\alpha>0$ and by $d-\lambda_n>0$ gives $\alpha\le\dfrac{n(-\lambda_n)}{d-\lambda_n}$.
(For $K_{3,3}$: $d=3$, $\lambda_n=-3$, bound $=6\cdot3/6=3=\alpha$ ✓; for $C_5$: $d=2$, $\lambda_n=-1.618$,
bound $=5\cdot1.618/3.618=2.24\ge2=\alpha$ ✓.)

**27.** *Strategy: the cycle formula gives $\lambda_2$; then Theorem 7.8.2 gives the upper bound, and a
diffusion argument gives the lower bound.*

By Section 7.2 the Laplacian eigenvalues of $C_n$ are $2-2\cos(2\pi k/n)$, so the smallest non-zero one is
$$\mu_2=2-2\cos\frac{2\pi}{n}=4\sin^2\frac{\pi}{n}\ \sim\ \frac{4\pi^2}{n^2}.$$
For the walk, $P=A/2$ has $\theta_2=1-\mu_2/2=\cos(2\pi/n)\sim1-2\pi^2/n^2$, so
$1-\theta_*\sim2\pi^2/n^2$ and Corollary 7.8.4 gives
$$t_{\mathrm{mix}}(\varepsilon)\le\frac{\ln(\sqrt n/\varepsilon)}{1-\theta_*}=O(n^2\ln n).$$
*Lower bound.* The walk started at a vertex behaves like a simple random walk on $\mathbb{Z}$ for
$t\ll n^2$: its position has variance $\Theta(t)$, so unless $t=\Omega(n^2)$ the mass stays concentrated
in an arc of length $o(n)$ and the distribution cannot be within $1/4$ in total variation of uniform.
Hence $t_{\mathrm{mix}}=\Theta(n^2)$, the square of the diameter. The same conclusion follows from the
inverse direction of the Cheeger inequality, since $h(C_n)\asymp 4/n$ (a path of about $n/2$ consecutive
vertices has only two boundary edges, giving the ratio $2/(n/2)=4/n$) and $h^2/2\asymp 8/n^2\lesssim\mu_2$.

**28.** *Strategy: Courant–Fischer in both directions, using the coordinate subspace
$W_J=\{x:x_i=0\ \text{for}\ i\notin J\}$.*

Let $B$ be the principal submatrix on the index set $J$, $\lvert J\rvert=m$. Every $x\in W_J$ satisfies
$R_A(x)=R_B(x_J)$, and subspaces of $W_J$ are subspaces of $\mathbb{R}^n$.

*Upper inequality* $\lambda_i(B)\le\lambda_i(A)$. Courant–Fischer in the max-min form gives
$$\lambda_i(A)=\max_{\dim U=i}\ \min_{0\ne x\in U}R_A(x),\qquad
\lambda_i(B)=\max_{\dim V=i}\ \min_{0\ne y\in V}R_B(y).$$
For every $i$-dimensional $V\le W_J$ the inner minimum equals $\min_{0\ne x\in V}R_A(x)\le\lambda_i(A)$,
because $\lambda_i(A)$ is the maximum of that minimum. Taking the maximum over all such $V$ gives
$\lambda_i(B)\le\lambda_i(A)$.

*Lower inequality* $\lambda_i(B)\ge\lambda_{i+n-m}(A)$. Using the min-max form,
$$\lambda_{i+n-m}(A)=\min_{\dim U=m-i+1}\ \max_{0\ne x\in U}R_A(x),$$
while $\lambda_i(B)=\min_{\dim V=m-i+1}\max_{0\ne y\in V}R_B(y)$. Each $(m-i+1)$-dimensional $V\le W_J$ is
an admissible $U$ in the first minimum, and for it the two inner maxima coincide; the minimum over all
$U$ is therefore no larger than the minimum over those inside $W_J$, that is
$\lambda_{i+n-m}(A)\le\lambda_i(B)$. Combining proves interlacing. $\blacksquare$

**29.** *Strategy: express every invariant as $\sum_i\lambda_i^k$ or a symmetric function of the spectrum.*

Closed walks of length $k$: $\sum_{u}(A^k)_{uu}=\operatorname{tr}(A^k)=\sum_i\lambda_i^k$, a symmetric function
of the spectrum; so cospectral graphs agree for every $k$. Edges: $m=\tfrac12\operatorname{tr}(A^2)$.
Triangles: $t=\tfrac16\operatorname{tr}(A^3)$.

*$K_{1,4}$ versus $C_4\cup K_1$.* Spectra both $2,0,0,0,-2$, hence $\sum\lambda^2=8$, $m=4$ ✓ (star: $4$
edges; $C_4\cup K_1$: $4$ edges) and $\sum\lambda^3=8-8=0$, $t=0$ ✓ (neither has a triangle).

*Example 7.10.2.* Both spectra give $\sum\lambda^2=2\cdot7=14$, so $m=7$ ✓, and both graphs have exactly
two triangles ($\{0,1,4\},\{0,2,3\}$ in $G_1$ and $\{0,2,3\},\{1,2,3\}$ in $G_2$), consistent with
$\sum\lambda^3=12$ and $t=2$.

**30.** *Strategy: the multiplicity of $0$ is the component count; $\tau$ is the product formula.*

Components: Theorem 7.5.3 identifies the multiplicity of $0$ in $\operatorname{spec}(L)$ with the number of
components, so Laplacian-cospectral graphs have the same number of components. Spanning trees: for a
connected graph Corollary 7.6.2 gives $\tau=\frac1n\prod_{i\ge2}\mu_i$, a symmetric function of the
Laplacian spectrum; for a disconnected graph $\tau=0$, detected by the repeated zero. Hence the Laplacian
spectrum determines $\tau$ as well.

*The pair.* $\operatorname{spec}(L(K_{1,4}))=0,1,1,1,5$ and $\operatorname{spec}(L(C_4\cup K_1))=0,0,2,2,4$.
These differ (two zeros versus one), so the pair is not Laplacian-cospectral, and indeed
$\tau(K_{1,4})=1$ while $C_4\cup K_1$ has no spanning tree.

**31.** *Strategy: $L(K_n)=nI-J$ and the product formula.*

The Laplacian of $K_n$ is $nI-J$: diagonal $n-1$, off-diagonal $-1$, which is $nI-J$ because $n-1=n-1$ and
$-1=0-1$. On $\mathbf{1}$ the eigenvalue is $0$; on $\mathbf{1}^{\perp}$, $J=0$ and the eigenvalue is $n$,
with multiplicity $n-1$. Hence
$$\tau(K_n)=\frac1n\,n^{n-1}=n^{n-2},$$
which is Cayley's formula. For $n=4$: $4^2=16$. Two checks: (i) the cofactor of $L(K_4)$ is the $3\times3$
matrix with $3$ on the diagonal and $-1$ elsewhere, whose eigenvalues are $4,4,1$, so its determinant is
$16$; (ii) Cayley's formula counts labelled trees on $4$ vertices, which are $4^{2}=16$ (four stars and
twelve paths, as counted in the [Trees](../02-trees/solutions.md) exercises).

## Challenge

**32.** *Strategy: Kronecker products and the identity $(A\otimes I+I\otimes B)(u\otimes v)=Au\otimes v+u\otimes Bv$.*

Order the vertices of $G\,\square\,H$ as pairs $(g,h)$. Its adjacency matrix is
$A_{G\square H}=A_G\otimes I_H+I_G\otimes A_H$: the first term joins $(g,h)$ to $(g',h)$ for $gg'\in E(G)$,
the second joins it to $(g,h')$ for $hh'\in E(H)$. If $A_Gu=\lambda u$ and $A_Hv=\mu v$, then
$$(A_G\otimes I+I\otimes A_H)(u\otimes v)=(\lambda u)\otimes v+u\otimes(\mu v)=(\lambda+\mu)(u\otimes v).$$
The products $u\otimes v$ over eigenbases of $G$ and $H$ form a basis of $\mathbb{R}^{V(G)\times V(H)}$, so the
spectrum of $G\,\square\,H$ is $\{\lambda_i(G)+\lambda_j(H)\}$ with multiplicities.

*The cube.* $Q_d=K_2\,\square\cdots\square\,K_2$ ($d$ factors) and $\operatorname{spec}(K_2)=\{1,-1\}$, so the
eigenvalues are $d-2k$ with multiplicity $\binom dk$, $k=0,\dots,d$: for $Q_3$ that is
$3,1,1,1,-1,-1,-1,-3$ ✓.

*The grid.* $P_m\,\square\,P_n$ has eigenvalues $2\cos\frac{i\pi}{m+1}+2\cos\frac{j\pi}{n+1}$ for
$1\le i\le m$, $1\le j\le n$. For $P_2\,\square\,P_3$ the path spectra are $\{1,-1\}$ and
$\{1.414,0,-1.414\}$, so the six sums are
$$1+1.414=2.414,\quad 1+0=1,\quad 1-1.414=-0.414,\quad -1+1.414=0.414,\quad -1+0=-1,\quad -1-1.414=-2.414 .$$

**33.** *Strategy: decompose the indicator vectors into their constant part and an orthogonal part.*

Let $x=\mathbf{1}_S-\frac{\lvert S\rvert}{n}\mathbf{1}$ and $y=\mathbf{1}_T-\frac{\lvert T\rvert}{n}\mathbf{1}$. Then
$x,y\perp\mathbf{1}$ and
$$\lVert x\rVert^2=\lvert S\rvert-\frac{\lvert S\rvert^2}{n},\qquad \lVert y\rVert^2=\lvert T\rvert-\frac{\lvert T\rvert^2}{n}.$$
Since $e(S,T)=\mathbf{1}_S^{\mathsf T}A\mathbf{1}_T$ and $A\mathbf{1}=d\mathbf{1}$,
$$e(S,T)=\frac{\lvert S\rvert\lvert T\rvert}{n^2}\,\mathbf{1}^{\mathsf T}A\mathbf{1}+x^{\mathsf T}Ay
=\frac{d\lvert S\rvert\lvert T\rvert}{n}+x^{\mathsf T}Ay .$$
On $\mathbf{1}^{\perp}$ the operator $A$ has eigenvalues $\lambda_2,\dots,\lambda_n$, all of modulus at most
$\lambda$, so $\lvert x^{\mathsf T}Ay\rvert\le\lambda\lVert x\rVert\lVert y\rVert$ (diagonalise $A$ on
$\mathbf{1}^{\perp}$ and apply Cauchy–Schwarz). Finally
$\lVert x\rVert\lVert y\rVert\le\sqrt{\lvert S\rvert\lvert T\rvert}$ because $\lVert x\rVert^2\le\lvert S\rvert$
and $\lVert y\rVert^2\le\lvert T\rvert$. Combining gives the claim. $\blacksquare$

*Interpretation.* If $\lambda$ is much smaller than $d$, the number of edges between $S$ and $T$ is
within an additive $O(\lambda\sqrt{\lvert S\rvert\lvert T\rvert})$ of what a random $d$-regular graph would
have — a "pseudo-randomness" statement that is the combinatorial form of expansion.

**34.** *Strategy: dependency for a cycle, triangularity for a tree.*

Let $B_i$ be the incidence matrix with row $i$ deleted, and let $S$ be a set of $n-1$ edges.

*If $S$ contains a cycle* $C$: the signed incidence vectors of the edges of $C$ sum to the zero vector
(each vertex of $C$ has one $+1$ and one $-1$ among them, and vertices off $C$ have $0$), so the columns
of $B_i[S]$ are linearly dependent and $\det B_i[S]=0$.

*If $S$ is a spanning tree*: choose a leaf $\ell\ne i$ of the tree (such a leaf exists because a tree has
at least two leaves and at most one of them is $i$). Its unique incident edge in $S$ gives a column with
a single non-zero entry $\pm1$ in row $\ell$. Expand the determinant along that row: the cofactor is the
determinant of the incidence matrix of the smaller tree $S-\ell$ with row $\ell$ removed and row $i$ still
deleted. Induct on $n$: the determinant is $\pm1$. (Equivalently, order the edges by repeatedly removing
leaves other than $i$; the matrix becomes triangular with $\pm1$ on the diagonal.)

So $\det(B_i[S])^2$ is $1$ exactly for spanning trees and $0$ otherwise, which is precisely what
Cauchy–Binet needs. $\blacksquare$

**35.** *Strategy: convergence is governed by the eigenvalues of $P$; the obstruction is the eigenvalue $-1$.*

Let $G$ be connected and $d$-regular, so $P=A/d$ is symmetric with eigenvalues $\theta_i=\lambda_i/d$.
Then $\theta_1=1$ with eigenvector $\mathbf{1}$, and convergence to the uniform distribution from every start
is equivalent to $\lvert\theta_i\rvert<1$ for all $i\ge2$: if some $\lvert\theta_i\rvert=1$ then the
component of $p_0-\pi$ along $v_i$ persists forever, while if all are $<1$ then Theorem 7.8.2 gives
exponential decay.

By Corollary 7.3.2, $\lvert\lambda_i\rvert<\lambda_1=d$ for $i\ge2$ exactly when $G$ is not bipartite. If
$G$ is bipartite then $\theta_n=-1$: starting at a vertex, $p_t$ is supported on the parity class of
distance $t$ from the start, so $p_t$ never approaches the uniform distribution.

*The lazy walk.* Let $P'=\frac12(I+P)$, with eigenvalues $(1+\theta_i)/2\in[0,1]$. Then $\theta'_1=1$ and
$\theta'_i=(1+\theta_i)/2<1$ for $i\ge2$, since $\theta_i<1$; also $\theta'_i\ge0$, so no eigenvalue is
$-1$. Theorem 7.8.2 therefore applies to $P'$ and the lazy walk converges for every connected graph,
bipartite or not. (Its mixing time is at most a constant factor larger than that of the walk when the
walk converges, because $(1+\theta_2)/2\ge\theta_2$.)

**36.** *Strategy: $\bar A=J-I-A$, and $J$ acts as $0$ on $\mathbf{1}^{\perp}$.*

Since $G$ is $d$-regular, $\bar G$ is $(n-1-d)$-regular and $\bar A=J-I-A$. On $\mathbf{1}$:
$$\bar A\mathbf{1}=(n-1)\mathbf{1}-\mathbf{1}-d\mathbf{1}=(n-1-d)\mathbf{1}.$$
On $\mathbf{1}^{\perp}$ we have $J=0$, so $\bar A=-I-A$ and each eigenvector $v_i$ of $A$ with eigenvalue
$\lambda_i$ ($i\ge2$) is an eigenvector of $\bar A$ with eigenvalue $-1-\lambda_i$. Hence
$$\operatorname{spec}(\bar G)=\{n-1-d\}\cup\{-1-\lambda_i:\ i\ge2\}.$$

*Connectivity.* By Exercise 25 applied to the $(n-1-d)$-regular graph $\bar G$, $\bar G$ is connected
exactly when the eigenvalue $n-1-d$ of $\bar A$ is simple, i.e. exactly when no $i\ge2$ satisfies
$-1-\lambda_i=n-1-d$, that is, exactly when no eigenvalue of $G$ equals $d-n$.

*Checks.* $C_4$: $d=2$, $n=4$, $d-n=-2$, and $-2$ is an eigenvalue of $C_4$; the criterion says
$\overline{C_4}$ is disconnected, and indeed $\overline{C_4}=2K_2$ ✓. $C_5$: $d=2$, $n=5$, $d-n=-3$, and the
spectrum $2,0.618,0.618,-1.618,-1.618$ contains no $-3$; the criterion says $\overline{C_5}$ is connected,
and indeed $\overline{C_5}\cong C_5$ ✓.
