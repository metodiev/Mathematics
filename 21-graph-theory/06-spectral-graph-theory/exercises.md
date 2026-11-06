# Spectral Graph Theory — Exercises

> [Spectral Graph Theory](README.md) · 36 problems · Beginner → Challenge · Solutions: [solutions.md](solutions.md)

Attempt every problem in writing before opening [solutions.md](solutions.md). Each problem names the
section of the tutorial that supplies the technique.

Notation: $G$ is a finite simple graph, $n=\lvert V\rvert$, $m=\lvert E\rvert$; $\lambda_1\ge\cdots\ge\lambda_n$
are the eigenvalues of the adjacency matrix $A$ and $0=\mu_1\le\mu_2\le\cdots\le\mu_n$ those of the
Laplacian $L=D-A$. Spectra are written as multisets with multiplicities, e.g. $2,0,0,-2$. Decimal values
are rounded to three places; exact values are given in closed form where they exist.

## Beginner

**1.** *(§7.2)* Compute the adjacency spectrum of (a) $P_3$, (b) $K_{1,3}$, (c) $C_4$, (d) $K_4$. In each
case verify $\sum_i\lambda_i=0$ and $\sum_i\lambda_i^2=2m$.

**2.** *(§7.1)* For $C_5$: (a) compute the spectrum; (b) verify $\sum\lambda_i^2=2m$; (c) compute
$\operatorname{tr}(A^3)$ and explain why the answer is what it is. For $K_4$, compute
$\operatorname{tr}(A^3)$ and deduce the number of triangles.

**3.** *(§7.1)* Let $G$ be the paw: vertices $1,2,3,4$, edges $12,23,31,14$. Compute $(A^2)_{13}$,
$(A^2)_{14}$ and $(A^3)_{14}$, and interpret each number combinatorially.

**4.** *(§7.1)* How many closed walks of length $4$ does $C_4$ have? Compute the answer twice: from
$\operatorname{tr}(A^4)$ and by counting.

**5.** *(§7.5)* For $P_4$: (a) write down $L$; (b) compute its eigenvalues; (c) evaluate $x^{\mathsf T}Lx$
for $x=(1,1,-1,-1)$ from the matrix and from the identity $\sum_{uv}(x_u-x_v)^2$.

**6.** *(§7.5)* How many connected components has a graph whose Laplacian spectrum is
(a) $0,0,2,3,3$; (b) $0,1,1,4$; (c) $0,0,0,1,1,1,2$? Justify each answer.

**7.** *(§7.4)* Decide which of these spectra belong to bipartite graphs:
(a) $2,0,0,-2$; (b) $1.732,0,0,-1.732$; (c) $2.562,0,-1,-1.562$; (d) $3,1,1,1,-1,-1,-1,-3$.

**8.** *(§7.3)* Give the spectral radius of (a) $K_{1,4}$, (b) $C_6$, (c) $K_5$, (d) the Petersen graph.

**9.** *(§7.6)* Use the eigenvalue form of the matrix-tree theorem to compute the number of spanning trees
of $C_5$, and check the answer by a direct argument.

**10.** *(§7.8)* For the simple random walk on $C_4$: write $P$, give the stationary distribution, and
compute the distributions $p_1,p_2$ from a start at vertex $1$. Does the walk converge? Explain.

**11.** *(§7.9)* Let $A$ be a symmetric $4\times4$ matrix with spectrum $3,1,-1,-2$ and let $B$ be a
$3\times3$ principal submatrix. Which of the following can be $\operatorname{spec}(B)$:
(a) $2,0,-2$; (b) $2,1,0$; (c) $3,1,-1$; (d) $1.5,0.5,-1.5$?

**12.** *(§7.10)* Are $P_4$ and $K_{1,3}$ cospectral? Are $C_4$ and $K_{1,3}$ cospectral? Justify with the
spectra.

## Intermediate

**13.** *(§7.1)* Prove that $\operatorname{tr}A=0$ and $\operatorname{tr}(A^2)=2m$, and deduce
$\sum_i\lambda_i=0$ and $\sum_i\lambda_i^2=2m$.

**14.** *(§7.3)* Prove that $\lambda_1\ge 2m/n$, with equality if and only if $G$ is regular.

**15.** *(§7.1)* Prove that if $G=G_1\sqcup G_2$ then $\operatorname{spec}(G)=\operatorname{spec}(G_1)\cup\operatorname{spec}(G_2)$,
and that the same holds for the Laplacian spectra.

**16.** *(§7.4)* Using Corollary 7.3.2, prove that a connected graph is bipartite if and only if
$\lambda_n=-\lambda_1$.

**17.** *(§7.5)* Prove that $x^{\mathsf T}Lx=\sum_{uv\in E}(x_u-x_v)^2$ for every $x$, and deduce that $L$
is positive semidefinite with $L\mathbf{1}=0$.

**18.** *(§7.5)* Prove that the multiplicity of $0$ as an eigenvalue of $L$ equals the number of connected
components of $G$.

**19.** *(§7.6)* Compute the Laplacian spectra of $K_n$ and of $K_{m,n}$, and deduce
$\tau(K_n)=n^{n-2}$ and $\tau(K_{m,n})=m^{n-1}n^{m-1}$.

**20.** *(§7.5)* Prove that a $d$-regular graph satisfies $\mu_i=d-\lambda_i$ for each $i$, and explain
where the argument fails for a non-regular graph.

**21.** *(§7.6)* The house graph (a $C_4$ with a triangle on top) has Laplacian eigenvalues
$0,\ \frac{5-\sqrt5}{2},\ \frac{7-\sqrt5}{2},\ \frac{7+\sqrt5}{2},\ \frac{5+\sqrt5}{2}$.
Compute its number of spanning trees.

**22.** *(§7.8)* For the simple random walk on $K_4$, compute $P$, its eigenvalues, and the total-variation
distance from uniform after two steps starting at a vertex.

**23.** *(§7.5)* Prove that $\mu_2\le\dfrac{n}{n-1}\,\delta(G)$, where $\delta(G)$ is the minimum degree.

**24.** *(§7.9)* Prove that adding an edge to a graph cannot decrease $\mu_2$, using the variational
characterisation of $\mu_2$.

## Advanced

**25.** *(§7.3)* Prove that a $d$-regular graph is connected if and only if the eigenvalue $d$ has
multiplicity $1$; deduce that the multiplicity of $d$ equals the number of connected components.

**26.** *(§7.3)* Prove Hoffman's bound: if $G$ is $d$-regular with smallest adjacency eigenvalue
$\lambda_n<0$, then
$$\alpha(G)\le\frac{n\,(-\lambda_n)}{d-\lambda_n},$$
where $\alpha(G)$ is the largest size of an independent set.

**27.** *(§7.2, §7.8)* Prove that $\lambda_2(C_n)=2-2\cos\dfrac{2\pi}{n}$, and deduce that the simple random
walk on $C_n$ has mixing time $\Theta(n^2)$.

**28.** *(§7.9)* Prove Cauchy's interlacing theorem from the Courant–Fischer characterisation.

**29.** *(§7.1, §7.10)* Prove that cospectral graphs have the same number of **closed** walks of every
length, the same number of edges, and the same number of triangles. Verify these invariants on the pair
$K_{1,4}$ and $C_4\cup K_1$, and on the pair of Example 7.10.2.

**30.** *(§7.5–7.6)* Prove that the Laplacian spectrum determines the number of connected components and
the number of spanning trees, and show that $K_{1,4}$ and $C_4\cup K_1$ — cospectral for $A$ — have
different Laplacian spectra.

**31.** *(§7.6)* Deduce Cayley's formula $\tau(K_n)=n^{n-2}$ from the matrix-tree theorem, and check it for
$n=4$ two ways.

## Challenge

**32.** *(§7.2)* Prove that the Cartesian product $G\,\square\,H$ has adjacency eigenvalues
$\lambda_i(G)+\lambda_j(H)$ with multiplicities, deduce the spectrum of $Q_d=K_2\,\square\cdots\square\,K_2$
and of the grid $P_m\,\square\,P_n$.

**33.** *(§7.7)* Prove the expander mixing lemma: for a $d$-regular graph with
$\lambda=\max(\lvert\lambda_2\rvert,\lvert\lambda_n\rvert)$ and disjoint sets $S,T\subseteq V$,
$$\Bigl\lvert e(S,T)-\frac{d\,\lvert S\rvert\,\lvert T\rvert}{n}\Bigr\rvert\ \le\ \lambda\sqrt{\lvert S\rvert\,\lvert T\rvert},$$
where $e(S,T)$ is the number of edges with one endpoint in $S$ and one in $T$.

**34.** *(§7.6)* Prove the key lemma of the Cauchy–Binet proof of the matrix-tree theorem: for an
$(n-1)\times(n-1)$ submatrix of the incidence matrix, the determinant is $\pm1$ if the chosen columns form
a spanning tree and $0$ otherwise.

**35.** *(§7.8)* Let $G$ be connected and $d$-regular. Prove that the simple random walk converges to the
uniform distribution for every starting point if and only if $G$ is not bipartite, and that the **lazy**
walk with transition matrix $\tfrac12(I+P)$ converges for every connected graph.

**36.** *(§7.3)* Prove that if $G$ is $d$-regular with adjacency eigenvalues $\lambda_i$, then its complement
$\bar G$ has eigenvalues $n-1-d$ and $-1-\lambda_i$ for $i\ge2$. Deduce that $\bar G$ is connected if and
only if no eigenvalue of $G$ equals $d-n$, and check the criterion on $C_4$ (whose complement is $2K_2$)
and on $C_5$ (whose complement is $C_5$).
