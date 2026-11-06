# Functional Analysis — Solutions

> [Functional Analysis](README.md) · Solutions to the 38 problems in [exercises.md](exercises.md)

Each solution states the strategy first—which definition or theorem is applied and why its hypotheses hold—and then carries out every step. Numbers in parentheses refer to the section of the [tutorial](README.md) where the relevant result is proved. Where a second route exists it is mentioned, and likely pitfalls are flagged in place.

## Beginner

**1.** *Strategy: the reverse triangle inequality is the ordinary triangle inequality applied twice; the metric axioms are the three norm axioms rewritten.*

**(a)** From $x=(x-y)+y$ and the triangle inequality,
$$\lVert x\rVert\le\lVert x-y\rVert+\lVert y\rVert,\qquad\text{so}\qquad \lVert x\rVert-\lVert y\rVert\le\lVert x-y\rVert.$$
Interchanging $x$ and $y$ gives $\lVert y\rVert-\lVert x\rVert\le\lVert y-x\rVert=\lVert x-y\rVert$ (using $\lVert y-x\rVert=\lVert(-1)(x-y)\rVert=\lVert x-y\rVert$). Hence the absolute value of the difference is at most $\lVert x-y\rVert$.

**(b)** Given $\varepsilon>0$, take $\delta=\varepsilon$. If $\lVert x-y\rVert<\delta$, then by (a) $\lvert\lVert x\rVert-\lVert y\rVert\rvert<\varepsilon$. The same $\delta$ works for every pair, so the norm is uniformly continuous (not merely continuous).

**(c)** *Positivity.* $d(x,y)=\lVert x-y\rVert\ge0$ by Definition 5.1. *Definiteness.* $d(x,y)=0$ iff $\lVert x-y\rVert=0$ iff $x-y=0$ iff $x=y$, by axiom (N1); conversely $\lVert0\rVert=\lVert0\cdot0\rVert=0$ by (N2) with $\alpha=0$. *Symmetry.* $d(y,x)=\lVert y-x\rVert=\lVert(-1)(x-y)\rVert=\lvert-1\rvert\lVert x-y\rVert=d(x,y)$ by (N2). *Triangle.* $d(x,z)=\lVert x-z\rVert=\lVert(x-y)+(y-z)\rVert\le\lVert x-y\rVert+\lVert y-z\rVert=d(x,y)+d(y,z)$ by (N3).

**2.** *Strategy: each inequality is a one-line estimate; sharpness requires a vector that forces equality.*

*Upper bounds.*
* $\lVert x\rVert_\infty=\max_k\lvert x_k\rvert\le\left(\sum_k\lvert x_k\rvert^2\right)^{1/2}=\lVert x\rVert_2$, because the square of the maximum is one of the summands.
* $\lVert x\rVert_2^2=\sum_k\lvert x_k\rvert^2\le\sum_{j,k}\lvert x_j\rvert\lvert x_k\rvert=\lVert x\rVert_1^2$, because all cross terms are non-negative. Hence $\lVert x\rVert_2\le\lVert x\rVert_1$.
* By Cauchy–Schwarz with the vector $\mathbf1=(1,\dots,1)$, $\lVert x\rVert_1=\sum_k1\cdot\lvert x_k\rvert\le\sqrt n\,\lVert x\rVert_2$.
* $\lVert x\rVert_2^2=\sum_k\lvert x_k\rvert^2\le n\max_k\lvert x_k\rvert^2=n\lVert x\rVert_\infty^2$.
* $\lVert x\rVert_1=\sum_k\lvert x_k\rvert\le n\max_k\lvert x_k\rvert=n\lVert x\rVert_\infty$.

*Sharpness.* The vector $e_1$ gives equality in the first two inequalities. The vector $\mathbf1=(1,\dots,1)$ gives $\lVert\mathbf1\rVert_1=n$, $\lVert\mathbf1\rVert_2=\sqrt n$, $\lVert\mathbf1\rVert_\infty=1$, so it gives equality in the last three. Therefore no smaller constant can replace $1,1,\sqrt n,\sqrt n,n$ respectively.

**3.** *Strategy: expand the square and apply Cauchy–Schwarz to the cross term.* For $x,y\in\mathbb{R}^2$,
$$\lVert x+y\rVert_2^2=\lVert x\rVert_2^2+2\langle x,y\rangle+\lVert y\rVert_2^2\le\lVert x\rVert_2^2+2\lVert x\rVert_2\lVert y\rVert_2+\lVert y\rVert_2^2=(\lVert x\rVert_2+\lVert y\rVert_2)^2.$$
Taking square roots gives the triangle inequality. Equality in the first step requires $\langle x,y\rangle=\lVert x\rVert\lVert y\rVert$, which is exactly the equality case of Cauchy–Schwarz with a non-negative proportionality factor: $x=0$, or $y=cx$ with $c\ge0$. If $y=-cx$ with $c>0$, the cross term is negative and the triangle inequality is strict (unless one vector is zero).

**4.** *Strategy: one explicit counterexample suffices.* Take $p=1/2$ and $x=(1,0)$, $y=(0,1)$. Then
$$N_p(x)=\left(\lvert1\rvert^{1/2}+\lvert0\rvert^{1/2}\right)^2=1,\qquad N_p(y)=1,$$
while
$$N_p(x+y)=\left(1^{1/2}+1^{1/2}\right)^2=4>2=N_p(x)+N_p(y).$$
So the triangle inequality fails. The hypothesis $p\ge1$ in Minkowski's inequality is therefore essential. The mechanism is that $t\mapsto t^p$ is concave for $0<p<1$, so the "norm" rewards spreading mass across coordinates rather than concentrating it; on the unit "ball" of $N_p$ the point $(1,1)$ is far outside, and the ball is not convex. A norm must have a convex unit ball, because $\lVert\lambda x+(1-\lambda)y\rVert\le\lambda\lVert x\rVert+(1-\lambda)\lVert y\rVert\le1$ for $\lambda\in[0,1]$ is exactly convexity.

**5.** *Strategy: compare the two series term by term; then test the borderline sequence $x_n=1/n$.*

*Inclusion and inequality.* For any scalar sequence, $\sum_k\lvert x_k\rvert^2\le\left(\sum_k\lvert x_k\rvert\right)^2$, because the right side is the sum of all terms $\lvert x_j\rvert\lvert x_k\rvert$, which includes the diagonal terms and additional non-negative cross terms. Hence if $\sum\lvert x_k\rvert<\infty$, then $\sum\lvert x_k\rvert^2<\infty$, and $\lVert x\rVert_2\le\lVert x\rVert_1$.

*Properness.* The sequence $x_n=1/n$ satisfies $\sum1/n^2=\pi^2/6<\infty$ but $\sum1/n=\infty$. So $x\in\ell^2\setminus\ell^1$. In particular the inclusion $\ell^1\subseteq\ell^2$ is proper.

*The reverse inclusion.* $\ell^2\not\subseteq\ell^1$, again by $x_n=1/n$: it belongs to $\ell^2$ and not to $\ell^1$. The correct general statement is $\ell^p\subseteq\ell^q$ for $p<q$ (Proposition 7.7), with the inclusion proper.

**6.** *Strategy: use the duality formula for functionals, the row/column-sum formulas for matrices in $\ell^\infty$/$\ell^1$, and the definition of the operator norm for the shift.*

**(a)** The matrix is $A=\begin{pmatrix}2&-1\\1&2\end{pmatrix}$. Then
$$A^{\mathsf T}A=\begin{pmatrix}2&1\\-1&2\end{pmatrix}\begin{pmatrix}2&-1\\1&2\end{pmatrix}=\begin{pmatrix}5&0\\0&5\end{pmatrix}=5I.$$
Hence $\lVert Ax\rVert_2^2=5\lVert x\rVert_2^2$ for every $x$: the map is $\sqrt5$ times an orthogonal map. Therefore $\lVert T\rVert=\sqrt5$, and the norm is attained at every unit vector (in particular at $e_1$).

**(b)** For $\lVert\cdot\rVert_\infty$, the norm is the maximum absolute row sum:
$$\lVert A\rVert_\infty=\max\{\lvert1\rvert+\lvert2\rvert,\ \lvert3\rvert+\lvert4\rvert\}=\max\{3,7\}=7.$$
Indeed $\lVert Ax\rVert_\infty\le7\lVert x\rVert_\infty$ for $\lVert x\rVert_\infty\le1$, and $x=(1,1)$ gives $Ax=(3,7)$ with $\lVert Ax\rVert_\infty=7$.
For $\lVert\cdot\rVert_1$, the norm is the maximum absolute column sum:
$$\lVert A\rVert_1=\max\{\lvert1\rvert+\lvert3\rvert,\ \lvert2\rvert+\lvert4\rvert\}=\max\{4,6\}=6,$$
attained at $x=(0,1)$: $Ax=(2,4)$, whose $1$-norm is $6$.

**(c)** For $\lVert f\rVert_\infty\le1$, $\lvert f(1/2)\rvert\le1$, so the norm is at most $1$; the constant function $f\equiv1$ has norm $1$ and value $1$ at $1/2$. Hence the norm is $1$, attained.

**(d)** For every $x$ and $1\le p\le\infty$, $\lVert Sx\rVert_p=\lVert x\rVert_p$ because the nonzero coordinates are the same, merely shifted. So $S$ is an isometry and $\lVert S\rVert=1$; the norm is attained at every $x\ne0$ (and at $e_1$ in particular). Note that $S$ is not surjective; an isometry need not be invertible.

**7.** *Strategy: for unboundedness exhibit a bounded family with unbounded derivatives; for boundedness on $P_n$ use finite-dimensionality.*

**(a)** Let $f_n(t)=\sin(nt)$. Then $\lVert f_n\rVert_\infty=1$ and $f_n'(t)=n\cos(nt)$, so $\lVert Df_n\rVert_\infty=n\lVert f_n\rVert_\infty$. Hence
$$\frac{\lVert Df_n\rVert_\infty}{\lVert f_n\rVert_\infty}=n\longrightarrow\infty,$$
so no constant $C$ satisfies $\lVert Df\rVert_\infty\le C\lVert f\rVert_\infty$ for all $f\in C^1[0,1]$. Therefore $D$ is unbounded.

**(b)** The space $P_n$ of polynomials of degree at most $n$ is finite-dimensional, and $D:P_n\to C[0,1]$ is linear. By Theorem 7.10(3), every linear map from a finite-dimensional normed space into a normed space is bounded. Hence $D|_{P_n}$ is bounded. The point is that the bound depends on $n$ and tends to infinity; there is no single bound valid for all polynomials. (One can also give an explicit bound: on $[0,1]$, Markov's inequality gives $\lVert p'\rVert_\infty\le2n^2\lVert p\rVert_\infty$ for $\deg p\le n$.)

**8.** *Strategy: prove sequential closedness in the metric of $\ell^\infty$.* Let $x^{(n)}\in c_0$ and $x^{(n)}\to x$ in $\ell^\infty$; given $\varepsilon>0$, choose $n$ with $\lVert x^{(n)}-x\rVert_\infty<\varepsilon/2$. Since $x^{(n)}\in c_0$, choose $K$ with $\lvert x^{(n)}_k\rvert<\varepsilon/2$ for $k>K$. Then for $k>K$,
$$\lvert x_k\rvert\le\lvert x_k-x^{(n)}_k\rvert+\lvert x^{(n)}_k\rvert<\frac{\varepsilon}{2}+\frac{\varepsilon}{2}=\varepsilon.$$
So $x\in c_0$. Thus $c_0$ is closed in the complete space $\ell^\infty$; a closed subset of a complete metric space is complete (Proposition 7.7(3)), so $c_0$ is a Banach space.

**9.** *Strategy: pairwise distances give a sequence with no Cauchy subsequence; compact metric spaces are sequentially compact.*

**(a)** For $n\ne m$, $\lVert e_n-e_m\rVert_2^2=1+1=2$, so $\lVert e_n-e_m\rVert_2=\sqrt2$. A convergent subsequence would be Cauchy, hence would have terms within $1$ of each other eventually, contradicting the constant distance $\sqrt2$. So $(e_n)$ has no convergent subsequence. All $e_n$ lie in the closed unit ball.

**(b)** In a metric space, compactness is equivalent to sequential compactness. The ball contains a sequence with no convergent subsequence; hence the ball is not compact. The same sequence lies in the unit sphere, so the sphere is not compact either. This illustrates Theorem 7.11 (Riesz's lemma): in infinite dimensions the closed unit ball is not compact, in sharp contrast with finite dimensions (Theorem 7.10(4)).

**10.** **(a)** Let $(x_n)$ be Cauchy. Choose $N$ with $\lVert x_n-x_N\rVert\le1$ for $n\ge N$. Then
$$\lVert x_n\rVert\le\max\bigl\{\lVert x_1\rVert,\dots,\lVert x_{N-1}\rVert,\lVert x_N\rVert+1\bigr\}$$
for every $n$: for $n<N$ this is clear, and for $n\ge N$ the triangle inequality gives $\lVert x_n\rVert\le\lVert x_n-x_N\rVert+\lVert x_N\rVert$.

**(b)** By the reverse triangle inequality, $\lvert\lVert x_n\rVert-\lVert x\rVert\rvert\le\lVert x_n-x\rVert\to0$.

**(c)** In $\ell^2$, the sequence $e_n$ is bounded ($\lVert e_n\rVert_2=1$) but has no convergent subsequence because $\lVert e_n-e_m\rVert_2=\sqrt2$. This does not contradict (a): (a) says that a Cauchy sequence is bounded, not that a bounded sequence is Cauchy. Boundedness is necessary for convergence, not sufficient.

**11.** **(a)** Suppose $\sum_n\lVert x_n\rVert<\infty$ and let $s_n=\sum_{k=1}^nx_k$. For $m>n$,
$$\lVert s_m-s_n\rVert=\left\lVert\sum_{k=n+1}^{m}x_k\right\rVert\le\sum_{k=n+1}^{m}\lVert x_k\rVert\longrightarrow0$$
as $n,m\to\infty$, because the tail of a convergent series tends to zero. So $(s_n)$ is Cauchy; completeness gives a limit $s$, and $\sum x_n=s$.

**(b)** Let $X$ be the space of real polynomials on $[0,1]$ with the supremum norm, and let $p_n(t)=\sum_{k=0}^n t^k/k!$. The series $\sum_{k\ge0}t^k/k!$ is absolutely convergent in $X$:
$$\sum_{k\ge0}\lVert t^k/k!\rVert_\infty=\sum_{k\ge0}\frac1{k!}=e<\infty.$$
Its partial sums $p_n$ converge uniformly on $[0,1]$ to $e^t$ by the Weierstrass $M$-test. If the series converged in $X$, its sum would be a polynomial $p$ with $p(t)=e^t$ for all $t\in[0,1]$. But no polynomial equals $e^t$ on an interval: differentiating $p(t)=e^t$ gives $p'(t)=e^t=p(t)$ on $(0,1)$; a polynomial satisfying $p'=p$ must be constant (if $\deg p=d\ge1$, then $\deg p'=d-1<d$, impossible), and the only constant solution of $p'=p$ is $p=0$, which is not $e^t$. Hence the absolutely convergent series has no limit in $X$, so $X$ is not complete. This is exactly the criterion of Proposition 7.8 read backwards.

**12.** *Strategy: for a functional on $\mathbb{F}^n$ with the $p$-norm, the dual norm is the $q$-norm of the coefficient vector, and the bound is attained by aligning $x$ with the coefficient vector.*

Write $f(x)=\sum a_kx_k$ with $a=(1,2,-2)$.

*$p=1$, $q=\infty$.* $\lvert f(x)\rvert\le\max_k\lvert a_k\rvert\sum_k\lvert x_k\rvert=\lVert a\rVert_\infty\lVert x\rVert_1=2\lVert x\rVert_1$. The largest coefficient is $a_2=2$, so equality is attained at $x=e_2$: $f(e_2)=2$ and $\lVert e_2\rVert_1=1$. Hence $\lVert f\rVert=2$.

*$p=2$, $q=2$.* $\lVert a\rVert_2=\sqrt{1+4+4}=3$; equality at $x=a/3=(1/3,2/3,-2/3)$, where $f(x)=9/3=3$ and $\lVert x\rVert_2=1$. So $\lVert f\rVert=3$.

*$p=\infty$, $q=1$.* $\lVert a\rVert_1=1+2+2=5$; equality at $x=(1,1,-1)$: $f(x)=1+2+2=5$ and $\lVert x\rVert_\infty=1$. So $\lVert f\rVert=5$.

## Intermediate

**13.** *Strategy: the three-step pattern of Theorem 7.4—coordinates, membership, norm convergence.*

Let $(x^{(n)})$ be Cauchy in $\ell^p$, $1\le p<\infty$.

*Step 1: coordinate limits.* For each fixed $k$, $\lvert x^{(n)}_k-x^{(m)}_k\rvert\le\lVert x^{(n)}-x^{(m)}\rVert_p$, so $(x^{(n)}_k)_n$ is Cauchy in $\mathbb{F}$ and converges to some $x_k$. Put $x=(x_1,x_2,\dots)$.

*Step 2: boundedness and membership.* A Cauchy sequence is bounded (Exercise 10(a)): there is $M$ with $\lVert x^{(n)}\rVert_p\le M$ for all $n$. For every finite $K$,
$$\sum_{k=1}^{K}\lvert x_k\rvert^p=\lim_{n\to\infty}\sum_{k=1}^{K}\lvert x^{(n)}_k\rvert^p\le M^p,$$
since a finite sum of limits is the limit of the sums. Letting $K\to\infty$ gives $\lVert x\rVert_p\le M$, so $x\in\ell^p$.

*Step 3: norm convergence.* Let $\varepsilon>0$ and choose $N$ with $\lVert x^{(n)}-x^{(m)}\rVert_p<\varepsilon$ for $n,m\ge N$. For every finite $K$ and $n,m\ge N$,
$$\sum_{k=1}^{K}\lvert x^{(n)}_k-x^{(m)}_k\rvert^p<\varepsilon^p.$$
Letting $m\to\infty$ gives $\sum_{k\le K}\lvert x^{(n)}_k-x_k\rvert^p\le\varepsilon^p$, and then letting $K\to\infty$ gives $\lVert x^{(n)}-x\rVert_p\le\varepsilon$ for all $n\ge N$. Hence $x^{(n)}\to x$ in $\ell^p$.

*The case $p=\infty$.* Replace sums by suprema. Coordinate convergence is uniform in $k$: given $\varepsilon$, choose $N$ with $\sup_k\lvert x^{(n)}_k-x^{(m)}_k\rvert<\varepsilon$ for $n,m\ge N$; then for each $k$, $\lvert x^{(n)}_k-x_k\rvert\le\varepsilon$ for $n\ge N$, and the bound is uniform in $k$. The limit is bounded because $\lvert x_k\rvert\le\lvert x^{(N)}_k\rvert+\varepsilon\le\lVert x^{(N)}\rVert_\infty+\varepsilon$, and $\lVert x^{(n)}-x\rVert_\infty\le\varepsilon$ eventually. The same argument proves the completeness of $c_0$ and of $C(K)$ with the sup norm.

**14.** *Strategy: build a Cauchy sequence whose only possible limit is a step function, then show no continuous function can be that limit.*

For $n\ge2$ define
$$f_n(t)=\begin{cases}0,&0\le t\le\frac12-\frac1n,\\[2pt] \frac n2\left(t-\frac12+\frac1n\right),&\frac12-\frac1n<t<\frac12+\frac1n,\\[4pt] 1,&\frac12+\frac1n\le t\le1.\end{cases}$$
Each $f_n$ is continuous and $0\le f_n\le1$. For $m>n$, the functions differ only on $(\frac12-\frac1m,\frac12+\frac1m)$, a set of length $2/m$, and their difference is at most $1$ there; hence
$$\lVert f_n-f_m\rVert_1=\int_0^1\lvert f_n-f_m\rvert\le\frac2m.$$
So $(f_n)$ is Cauchy in $\lVert\cdot\rVert_1$.

Suppose for contradiction that $g\in C[0,1]$ satisfies $\lVert f_n-g\rVert_1\to0$. For $n\ge2$, $f_n=0$ on $[0,\frac12-\frac1n]$, so
$$\int_0^{\frac12-\frac1n}\lvert g(t)\rvert\,dt\le\lVert f_n-g\rVert_1\longrightarrow0.$$
The sets $[0,\frac12-\frac1n]$ increase to $[0,\frac12)$, so $\int_0^{1/2}\lvert g\rvert=0$. If $g(t_0)\ne0$ for some $t_0\in[0,\frac12)$, continuity would give $\lvert g\rvert\ge\lvert g(t_0)\rvert/2$ on a small interval around $t_0$ contained in $[0,\frac12)$, making the integral positive. Hence $g=0$ on $[0,\frac12)$.

Similarly, $f_n=1$ on $[\frac12+\frac1n,1]$, so $\int_{1/2+1/n}^1\lvert1-g\rvert\le\lVert f_n-g\rVert_1\to0$; hence $\int_{1/2}^1\lvert1-g\rvert=0$ and, by continuity, $g=1$ on $(\frac12,1]$. Continuity at $\frac12$ then forces $g(\frac12)=\lim_{t\to1/2^-}g(t)=0$ and $g(\frac12)=\lim_{t\to1/2^+}g(t)=1$, a contradiction. Therefore no continuous limit exists and the norm is not complete.

**15.** **(a)** Let $M$ be a finite-dimensional subspace of a normed space $X$. By Theorem 7.10(1), $M$ with the restricted norm is complete. A complete subset of a metric space is closed: if $x\in\overline M$, choose $m_n\in M$ with $m_n\to x$; then $(m_n)$ is Cauchy, so it converges in $M$ to some $m$, and uniqueness of limits in $X$ gives $x=m\in M$. Hence $M$ is closed.

**(b)** $c_{00}$ is a linear subspace: sums and scalar multiples of finitely supported sequences are finitely supported. It is dense in $\ell^2$: given $x\in\ell^2$ and $\varepsilon>0$, choose $N$ with $\sum_{k>N}\lvert x_k\rvert^2<\varepsilon^2$ (possible because the series converges), and put $y=(x_1,\dots,x_N,0,0,\dots)\in c_{00}$; then $\lVert x-y\rVert_2<\varepsilon$. So $\overline{c_{00}}=\ell^2$. But $c_{00}\ne\ell^2$: the vector $x=(1,1/2,1/3,\dots)$ belongs to $\ell^2$ and is not finitely supported. Hence $c_{00}$ is not closed, which shows that finite-dimensionality cannot be dropped in (a).

**16.** **(a)** Since the interval has length one, $\lVert f\rVert_1=\int_0^1\lvert f\rvert\le\int_0^1\lVert f\rVert_\infty=\lVert f\rVert_\infty$. Therefore
$$\lVert f\rVert_\infty\le\lVert f\rVert_\infty+\lVert f\rVert_1=\lVert f\rVert_\star\le2\lVert f\rVert_\infty.$$
So the norms are equivalent with $c=1$ and $C=2$.

**(b)** The constant $C=2$ is attained by every nonzero constant function: $\lVert1\rVert_\star=1+1=2=2\lVert1\rVert_\infty$. The constant $c=1$ is optimal but not attained for nonzero $f$: for $f\ne0$,
$$\frac{\lVert f\rVert_\star}{\lVert f\rVert_\infty}=1+\frac{\lVert f\rVert_1}{\lVert f\rVert_\infty}>1.$$
However, for the continuous "spike" functions $f_n$ with $0\le f_n\le1$, $f_n(1/2)=1$ and $f_n=0$ outside $[1/2-1/(2n),1/2+1/(2n)]$, we have $\lVert f_n\rVert_\infty=1$ and $\lVert f_n\rVert_1\le1/n$, so the ratio is at most $1+1/n\to1$. Hence no constant larger than $1$ can work in the inequality $\lVert f\rVert_\infty\le c\lVert f\rVert_\star$.

**(c)** The tent functions $f_n$ of Example 7.3 have $\lVert f_n\rVert_\infty=1$ and $\lVert f_n\rVert_1=1/(2n)\to0$. If $\lVert f\rVert_\infty\le C\lVert f\rVert_1$ held for all $f$, then $1\le C/(2n)$ for every $n$, which is impossible. Hence the two norms are not equivalent. This does not contradict (a): adding $\lVert\cdot\rVert_\infty$ to $\lVert\cdot\rVert_1$ repairs the missing control.

**17.** *Strategy: take the pointwise limit, prove it is linear and bounded using the boundedness of Cauchy sequences, then prove norm convergence by letting the second index tend to infinity.*

Let $(T_n)$ be Cauchy in $\mathcal{B}(X,Y)$. For each $x\in X$, $\lVert T_nx-T_mx\rVert\le\lVert T_n-T_m\rVert\lVert x\rVert$, so $(T_nx)$ is Cauchy in the Banach space $Y$; define $Tx:=\lim_nT_nx$.

*Linearity.* For scalars $\alpha,\beta$ and $x,y\in X$,
$$T(\alpha x+\beta y)=\lim_nT_n(\alpha x+\beta y)=\lim_n(\alpha T_nx+\beta T_ny)=\alpha Tx+\beta Ty,$$
using continuity of addition and scalar multiplication in $Y$.

*Boundedness.* A Cauchy sequence is bounded in $\mathcal{B}(X,Y)$ (Exercise 10(a)), so $M:=\sup_n\lVert T_n\rVert<\infty$. For every $x$,
$$\lVert Tx\rVert=\lim_n\lVert T_nx\rVert\le M\lVert x\rVert.$$
Hence $T\in\mathcal{B}(X,Y)$.

*Norm convergence.* Let $\varepsilon>0$ and choose $N$ with $\lVert T_n-T_m\rVert\le\varepsilon$ for $n,m\ge N$. For $\lVert x\rVert\le1$ and $n\ge N$,
$$\lVert T_nx-Tx\rVert=\lim_{m\to\infty}\lVert T_nx-T_mx\rVert\le\varepsilon,$$
so $\lVert T_n-T\rVert\le\varepsilon$. Thus $T_n\to T$ in operator norm and $\mathcal{B}(X,Y)$ is complete.

**18.** *Strategy: (c)⇒(d)⇒(a)⇒(b)⇒(c), with (e) inserted by scaling.*

(c)⇒(d): $\lVert Tx-Ty\rVert=\lVert T(x-y)\rVert\le C\lVert x-y\rVert$; so $T$ is Lipschitz. (d)⇒(a): Lipschitz maps are continuous. (a)⇒(b): immediate.

(b)⇒(c): continuity at $0$ gives $\delta>0$ such that $\lVert Tz\rVert\le1$ whenever $\lVert z\rVert\le\delta$. For $x\ne0$, put $z=\delta x/(2\lVert x\rVert)$; then $\lVert z\rVert=\delta/2<\delta$, so
$$\lVert Tx\rVert=\frac{2\lVert x\rVert}{\delta}\left\lVert T\left(\frac{\delta x}{2\lVert x\rVert}\right)\right\rVert\le\frac{2}{\delta}\lVert x\rVert.$$
So $T$ is bounded with $C=2/\delta$.

(c)⇒(e): if $\lVert Tx\rVert\le C\lVert x\rVert$, then $T$ is bounded by $C(\lVert x_0\rVert+r)$ on the ball $B(x_0,r)$.

(e)⇒(c): suppose $\lVert Tx\rVert\le M$ on $B(x_0,r)$. For $\lVert z\rVert\le r$, the point $x_0+z$ lies in the ball, so
$$\lVert Tz\rVert\le\lVert T(x_0+z)\rVert+\lVert Tx_0\rVert\le2M.$$
For $x\ne0$, apply this to $z=rx/\lVert x\rVert$: $\lVert Tx\rVert\le2M\lVert x\rVert/r$. Hence $T$ is bounded.

*Why linearity matters.* For a nonlinear map, "bounded" has to be interpreted as "maps bounded sets to bounded sets". The map $h(t)=1$ for rational $t$ and $h(t)=0$ for irrational $t$ maps every bounded set into $\{0,1\}$, so it is bounded in that sense, but it is discontinuous at every point; thus (c)⇒(a) fails without linearity. For the second point, the map $g(t)=t$ for rational $t$ and $g(t)=0$ for irrational $t$ satisfies $\lvert g(t)\rvert\le\lvert t\rvert$, so it is continuous at $0$, but it is discontinuous at every other point. For linear maps, continuity at $0$ propagates by translation: $Tx-Tx_0=T(x-x_0)$.

**19.** **(a)** Since $\lVert T^k\rVert\le\lVert T\rVert^k$ and $\sum_k\lVert T\rVert^k=1/(1-\lVert T\rVert)<\infty$, the series is absolutely convergent in $\mathcal{B}(X)$, which is complete because $X$ is a Banach space (Theorem 7.14). By Proposition 7.8, it converges.

**(b)** Let $S_n=\sum_{k=0}^nT^k$. The telescoping identity
$$(I-T)S_n=S_n(I-T)=I-T^{n+1}$$
holds for every $n$. Since $\lVert T^{n+1}\rVert\le\lVert T\rVert^{n+1}\to0$, the right side tends to $I$ in operator norm, and $S_n\to S:=\sum_{k=0}^\infty T^k$. Passing to the limit in the identity gives $(I-T)S=S(I-T)=I$. Hence $I-T$ is invertible with inverse $S$, and
$$\lVert S\rVert\le\sum_{k=0}^\infty\lVert T\rVert^k=\frac{1}{1-\lVert T\rVert}.$$

**(c)** The condition $\lVert T\rVert<1$ is not necessary. For example, on $\mathbb{R}$, $T=-2I$ has $\lVert T\rVert=2\ge1$, while $I-T=3I$ is invertible. If $\lVert T^n\rVert<1$ for some $n$, then $I-T^n$ is invertible by (b) applied to $T^n$, and
$$I-T^n=(I-T)(I+T+\cdots+T^{n-1})=(I+T+\cdots+T^{n-1})(I-T).$$
Hence $I-T$ has both a left and a right inverse, so it is invertible, with
$$(I-T)^{-1}=(I+T+\cdots+T^{n-1})(I-T^n)^{-1}.$$
The bound in (b) must be replaced, because $\lVert T\rVert$ may be large; a valid bound is
$$\lVert(I-T)^{-1}\rVert\le\frac{\lVert I+T+\cdots+T^{n-1}\rVert}{1-\lVert T^n\rVert}.$$
For instance, $T=\begin{pmatrix}0&2\\0&0\end{pmatrix}$ on $\mathbb{R}^2$ with the supremum norm has $\lVert T\rVert=2$ and $T^2=0$, so $\lVert T^2\rVert=0<1$, while $(I-T)^{-1}=I+T$.

**20.** **(a)** Let $x\ne0$. On $M:=\mathbb{F}x$ define $f_0(\alpha x):=\alpha\lVert x\rVert$. Then $\lvert f_0(\alpha x)\rvert=\lvert\alpha\rvert\lVert x\rVert=\lVert\alpha x\rVert$, so $\lVert f_0\rVert_{M^*}=1$, and $f_0(x)=\lVert x\rVert$. By Theorem 7.23 there is $f\in X^*$ with $f|_M=f_0$ and $\lVert f\rVert=\lVert f_0\rVert=1$.

**(b)** For $\lVert f\rVert\le1$, $\lvert f(x)\rvert\le\lVert x\rVert$; the functional of (a) attains $\lVert x\rVert$. Therefore the supremum is a maximum and equals $\lVert x\rVert$. If $f(x)=0$ for every $f\in X^*$, then $\lVert x\rVert=\max_{\lVert f\rVert\le1}\lvert f(x)\rvert=0$, so $x=0$; this is separation of points.

**(c)** $J$ is linear because evaluation is linear in $x$. For $x\in X$,
$$\lVert Jx\rVert_{X^{**}}=\sup_{\lVert f\rVert\le1}\lvert(Jx)(f)\rvert=\sup_{\lVert f\rVert\le1}\lvert f(x)\rvert=\lVert x\rVert$$
by (b). So $J$ is an isometry; in particular it is injective.

**21.** *Strategy: the lower bound is Cauchy–Schwarz in the dual; the upper bound is Hahn–Banach applied to a carefully normalized functional on $M+\mathbb{F}x$.*

*Lower bound.* Let $f\in X^*$ with $\lVert f\rVert\le1$ and $f|_M=0$. For every $m\in M$,
$$\lvert f(x)\rvert=\lvert f(x-m)\rvert\le\lVert f\rVert\lVert x-m\rVert\le\lVert x-m\rVert.$$
Taking the infimum over $m\in M$ gives $\lvert f(x)\rvert\le d(x,M)$.

*Upper bound.* Let $N:=M+\mathbb{F}x$ and define $g:N\to\mathbb{F}$ by $g(m+\alpha x):=\alpha d(x,M)$. This is well defined: if $m+\alpha x=0$ with $\alpha\ne0$, then $x=-m/\alpha\in M$, contradiction; so $\alpha=0$, and then $m=0$. It is linear and vanishes on $M$. For $\alpha\ne0$,
$$\lvert g(m+\alpha x)\rvert=\lvert\alpha\rvert d(x,M)\le\lvert\alpha\rvert\left\lVert x+\frac{m}{\alpha}\right\rVert=\lVert m+\alpha x\rVert,$$
because $m/\alpha\in M$ and $d(x,M)$ is the infimum of $\lVert x-y\rVert$ over $y\in M$. For $\alpha=0$ the inequality is trivial. Hence $\lVert g\rVert_{N^*}\le1$, and $g(x)=d(x,M)$. By Theorem 7.23 extend $g$ to $f\in X^*$ with $\lVert f\rVert=\lVert g\rVert\le1$ and $f|_M=0$. Then $f(x)=d(x,M)$, so the maximum is attained.

*Example.* In $C[0,1]$, let $M$ be the constants and $x(t)=t$. Then $d(x,M)=\inf_c\sup_t\lvert t-c\rvert=1/2$ (the best constant is $c=1/2$). The functional $f=(\delta_0-\delta_1)/2$ has $\lVert f\rVert=1$, vanishes on constants, and $\lvert f(x)\rvert=\lvert(0-1)/2\rvert=1/2$; so it attains the distance. It is not of the form $f\mapsto\int_0^1g(t)f(t)\,dt$ with $g\in L^1$: if it were, then for continuous $f_n$ with $f_n(0)=1$, $0\le f_n\le1$, supported in $[0,1/n]$, we would have
$$\frac12=f_n(0)\cdot\frac12-\frac{f_n(1)}2=\int_0^1g(t)f_n(t)\,dt\longrightarrow0$$
by dominated convergence, a contradiction. So the norming functional genuinely requires a measure.

**22.** **(a)** For real sequences, $\limsup_n(a_n+b_n)\le\limsup_na_n+\limsup_nb_n$, because for every $\varepsilon>0$ the terms $a_n+b_n$ are eventually at most $(\limsup a)+\varepsilon+(\limsup b)+\varepsilon$. Also $\limsup_n(ta_n)=t\limsup_na_n$ for $t\ge0$. Hence $p(x+y)\le p(x)+p(y)$ and $p(tx)=tp(x)$: $p$ is sublinear.

**(b)** If $x\in M$, then the Cesàro averages converge, so $\limsup$ equals the limit: $p(x)=f(x)$. Theorem 7.22 (applied to the real vector space $\ell^\infty$) gives a linear $L:\ell^\infty\to\mathbb{R}$ with $L(x)\le p(x)$ for all $x$ and $L|_M=f$.

**(c)** For every $x$, $p(x)\le\lVert x\rVert_\infty$ and $p(-x)\le\lVert x\rVert_\infty$, so
$$\lvert L(x)\rvert=\max\{L(x),-L(x)\}\le\max\{p(x),p(-x)\}\le\lVert x\rVert_\infty.$$
Thus $\lVert L\rVert\le1$. Since $\mathbf1\in M$ and $f(\mathbf1)=1$, $L(\mathbf1)=1$. If $x\ge0$, then $-x\le0$, so
$$L(-x)\le p(-x)=\limsup_n\left(-\frac1n\sum_{k=1}^nx_k\right)\le0,$$
hence $L(x)\ge0$. For the shift $S$, put $w=x-Sx$. Its Cesàro averages telescope:
$$\frac1n\sum_{k=1}^n(x_k-x_{k+1})=\frac{x_1-x_{n+1}}{n}\longrightarrow0.$$
Hence $p(w)\le0$ and $p(-w)\le0$. Therefore $L(w)\le p(w)\le0$ and $L(-w)\le p(-w)\le0$; the second gives $L(w)\ge0$. So $L(w)=0$, i.e. $L(Sx)=L(x)$.

**(d)** Suppose $L(x)=\sum_kx_ky_k$ for some $y\in\ell^1$ and all $x\in\ell^\infty$. Then $y_k=L(e_k)$. By shift invariance, $L(e_k)=L(S^{k-1}e_1)=L(e_1)$ for every $k$, so $y$ is the constant sequence $y_k=L(e_1)$. A constant sequence in $\ell^1$ must be zero, so $y=0$ and $L=0$, contradicting $L(\mathbf1)=1$. Hence no such $y$ exists; in particular $(\ell^\infty)^*$ is strictly larger than $\ell^1$.

**23.** *Strategy: identify the candidate representing sequence by its values on the standard basis, then use density of finitely supported sequences.*

Let $y\in\ell^\infty$ and define $f_y(x)=\sum_kx_ky_k$ for $x\in\ell^1$. The series converges absolutely and
$$\lvert f_y(x)\rvert\le\sum_k\lvert x_k\rvert\lvert y_k\rvert\le\lVert y\rVert_\infty\lVert x\rVert_1,$$
so $f_y\in(\ell^1)^*$ with $\lVert f_y\rVert\le\lVert y\rVert_\infty$; linearity is clear.

Conversely, let $f\in(\ell^1)^*$ and put $y_k=f(e_k)$. Then $\lvert y_k\rvert\le\lVert f\rVert\lVert e_k\rVert_1=\lVert f\rVert$, so $y\in\ell^\infty$ and $\lVert y\rVert_\infty\le\lVert f\rVert$. For $x\in\ell^1$, the partial sums $x^{(N)}=\sum_{k\le N}x_ke_k$ converge to $x$ in $\ell^1$ because $\lVert x-x^{(N)}\rVert_1=\sum_{k>N}\lvert x_k\rvert\to0$. Continuity of $f$ gives
$$f(x)=\lim_Nf(x^{(N)})=\lim_N\sum_{k\le N}x_ky_k=\sum_{k\ge1}x_ky_k=f_y(x).$$
So $f=f_y$.

It remains to show $\lVert f_y\rVert\ge\lVert y\rVert_\infty$. Given $\varepsilon>0$, choose $k$ with $\lvert y_k\rvert>\lVert y\rVert_\infty-\varepsilon$, and set $x:=\overline{y_k}/\lvert y_k\rvert\,e_k$ (or $\operatorname{sgn}(y_k)e_k$ in the real case). Then $\lVert x\rVert_1=1$ and $\lvert f_y(x)\rvert=\lvert y_k\rvert>\lVert y\rVert_\infty-\varepsilon$. Hence $\lVert f_y\rVert=\lVert y\rVert_\infty$. The map $y\mapsto f_y$ is linear, injective and surjective, and isometric.

**24.** **(a)** Take $y(t)=1$ for $0\le t<1/2$ and $y(t)=-1$ for $1/2\le t\le1$. Then $\lVert y\rVert_2=1$ and
$$\langle x,y\rangle=\int_0^{1/2}x(t)\,dt-\int_{1/2}^1x(t)\,dt=f(x).$$
By Theorem 7.41, $\lVert f\rVert=\lVert y\rVert_2=1$. The same bound follows directly from Cauchy–Schwarz: $\lvert f(x)\rvert=\lvert\langle x,y\rangle\rvert\le\lVert x\rVert_2\lVert y\rVert_2=\lVert x\rVert_2$.

**(b)** With $x=y$, $f(y)=\int_0^{1/2}1\,dt-\int_{1/2}^1(-1)\,dt=\frac12+\frac12=1$, while $\lVert y\rVert_2=1$ and $\lVert f\rVert=1$. Thus $\lvert f(y)\rvert=\lVert f\rVert\lVert y\rVert$, which is equality in Cauchy–Schwarz. Since $y$ is a unit vector, the supremum defining $\lVert f\rVert$ is attained at $y$ (and at $-y$).

**(c)** If $y,y'\in L^2[0,1]$ both represent $f$, then $\langle x,y-y'\rangle=0$ for every $x$. Taking $x=y-y'$ gives $\lVert y-y'\rVert_2^2=0$, so $y=y'$ in $L^2$ (that is, equal almost everywhere).

**(d)** The function $y$ above is discontinuous at $1/2$, but it belongs to $L^2[0,1]$, whose elements are equivalence classes modulo equality almost everywhere; changing $y$ at the single point $1/2$ does not change the class. The functional $f$ is continuous on $L^2$ because it is bounded: $\lvert f(x)\rvert\le\lVert x\rVert_2$ for all $x$. Continuity of a linear functional does not require its representing vector to have a continuous representative. This is a useful reminder that in $L^p$ spaces the pointwise behaviour of a representative is irrelevant.

## Advanced

**25.** *Strategy: minimise by a minimising sequence and use the parallelogram law to force Cauchyness; perpendicularity follows by perturbing the minimiser along $M$.*

*Existence.* Let $d:=d(x,M)$ and choose $m_n\in M$ with $\lVert x-m_n\rVert\to d$. Apply the parallelogram law to the vectors $x-m_n$ and $x-m_k$:
$$\lVert m_n-m_k\rVert^2=2\lVert x-m_n\rVert^2+2\lVert x-m_k\rVert^2-4\left\lVert x-\frac{m_n+m_k}{2}\right\rVert^2.$$
Since $(m_n+m_k)/2\in M$, the last term is at most $4d^2$. Hence
$$\lVert m_n-m_k\rVert^2\le2\lVert x-m_n\rVert^2+2\lVert x-m_k\rVert^2-4d^2\longrightarrow0.$$
So $(m_n)$ is Cauchy. Since $M$ is closed in the complete space $H$, $m_n\to m_0\in M$ and $\lVert x-m_0\rVert=d$.

*Uniqueness.* If $m_0,m_1$ both realise the distance, the same computation with $m_0,m_1$ gives $\lVert m_0-m_1\rVert^2\le2d^2+2d^2-4d^2=0$.

*Perpendicularity.* For $m\in M$ and $t\in\mathbb{R}$, the point $m_0+tm$ lies in $M$, so
$$d^2\le\lVert x-m_0-tm\rVert^2=d^2-2t\operatorname{Re}\langle x-m_0,m\rangle+t^2\lVert m\rVert^2.$$
For small $t>0$ this gives $\operatorname{Re}\langle x-m_0,m\rangle\le0$, and for small $t<0$ it gives $\operatorname{Re}\langle x-m_0,m\rangle\ge0$; hence the real part is zero. Replacing $m$ by $im$ in the complex case makes the imaginary part zero. Thus $x-m_0\perp M$.

*Decomposition.* Every $x$ is $m_0+(x-m_0)\in M+M^\perp$. If $z\in M\cap M^\perp$, then $\langle z,z\rangle=0$, so $z=0$; the sum is direct. Hence $H=M\oplus M^\perp$.

*Properties of $P_M$.* Write $x=P_Mx+x^\perp$ with $x^\perp\perp M$. Linearity: if $x=m+n$, $y=m'+n'$ are the decompositions, then $x+y=(m+m')+(n+n')$ is a decomposition with $m+m'\in M$ and $n+n'\in M^\perp$; uniqueness gives $P_M(x+y)=m+m'=P_Mx+P_My$. Scalars are similar. Boundedness and norm: Pythagoras gives
$$\lVert x\rVert^2=\lVert P_Mx\rVert^2+\lVert x-P_Mx\rVert^2\ge\lVert P_Mx\rVert^2,$$
so $\lVert P_M\rVert\le1$; if $M\ne\{0\}$, any $m\in M$ with $\lVert m\rVert=1$ has $P_Mm=m$, so $\lVert P_M\rVert=1$. Idempotence: $P_Mx\in M$, so $P_M(P_Mx)=P_Mx$. Self-adjointness: with $x=m+n$, $y=m'+n'$,
$$\langle P_Mx,y\rangle=\langle m,m'+n'\rangle=\langle m,m'\rangle=\langle m+n,m'\rangle=\langle x,P_My\rangle,$$
since $n\perp m'$ and $m\perp n'$.

**26.** **(a)** For a finite $F\subseteq A$, put $s_F:=\sum_{\alpha\in F}\langle x,e_\alpha\rangle e_\alpha$. Orthonormality gives $\lVert s_F\rVert^2=\sum_{\alpha\in F}\lvert\langle x,e_\alpha\rangle\rvert^2$ (all cross terms vanish), and
$$\lVert x-s_F\rVert^2=\lVert x\rVert^2-2\operatorname{Re}\langle x,s_F\rangle+\lVert s_F\rVert^2=\lVert x\rVert^2-2\sum_{\alpha\in F}\lvert\langle x,e_\alpha\rangle\rvert^2+\sum_{\alpha\in F}\lvert\langle x,e_\alpha\rangle\rvert^2=\lVert x\rVert^2-\sum_{\alpha\in F}\lvert\langle x,e_\alpha\rangle\rvert^2.$$
The left side is non-negative, so every finite partial sum is at most $\lVert x\rVert^2$. Taking the supremum over finite $F$ gives Bessel's inequality.

**(b)** If equality holds, then for every $\varepsilon>0$ there is a finite $F$ with $\sum_{\alpha\in F}\lvert\langle x,e_\alpha\rangle\rvert^2>\lVert x\rVert^2-\varepsilon^2$; hence $\lVert x-s_F\rVert<\varepsilon$, and $x$ lies within $\varepsilon$ of $\operatorname{span}\{e_\alpha\}$. Since $\varepsilon$ is arbitrary, $x\in\overline{\operatorname{span}}\{e_\alpha\}$.

Conversely, if $x\in\overline{\operatorname{span}}\{e_\alpha\}$ and $\varepsilon>0$, choose $u=\sum_{\alpha\in F}c_\alpha e_\alpha$ with $\lVert x-u\rVert<\varepsilon$. For every finite $F'\supseteq F$, the vector $s_{F'}$ is the orthogonal projection of $x$ onto $\operatorname{span}\{e_\alpha:\alpha\in F'\}$ (Theorem 7.36 applied in that finite-dimensional space), and $u$ belongs to that span; hence $\lVert x-s_{F'}\rVert\le\lVert x-u\rVert<\varepsilon$. Therefore $\lVert x\rVert^2-\sum_{\alpha\in F'}\lvert\langle x,e_\alpha\rangle\rvert^2<\varepsilon^2$, so the supremum of the partial sums is at least $\lVert x\rVert^2-\varepsilon^2$. Letting $\varepsilon\to0$ and using (a) gives equality.

**(c)** For each $n\ge1$, the set $A_n:=\{\alpha:\lvert\langle x,e_\alpha\rangle\rvert>1/n\}$ is finite: otherwise a finite subset of $A_n$ would contain $N$ elements and give a partial sum larger than $N/n^2$, which exceeds $\lVert x\rVert^2$ for large $N$. The set of $\alpha$ with $\langle x,e_\alpha\rangle\ne0$ is $\bigcup_nA_n$, a countable union of finite sets, hence countable.

**27.** **(a)⇒(b)** Suppose the closed span $M:=\overline{\operatorname{span}}\{e_\alpha\}$ is a proper subspace. By Theorem 7.36, $M^\perp\ne\{0\}$; choose a unit vector $y\in M^\perp$. Then $y\perp e_\alpha$ for every $\alpha$, contradicting maximality. **(b)⇒(a)** If some unit $y$ is orthogonal to every $e_\alpha$, then $y\perp M$, so $M\ne H$; contrapositive.

**(b)⇒(d)** Let $x\in H$ and $\varepsilon>0$. Density gives $u=\sum_{\alpha\in F}c_\alpha e_\alpha$ with $\lVert x-u\rVert<\varepsilon$. For every finite $F'\supseteq F$, the partial sum $s_{F'}$ is the orthogonal projection of $x$ onto $\operatorname{span}\{e_\alpha:\alpha\in F'\}$ and $u$ lies in that span, so $\lVert x-s_{F'}\rVert\le\lVert x-u\rVert<\varepsilon$. Hence the net $(s_F)$ converges to $x$, which is (d).

**(d)⇒(c)** Since $\lVert s_F\rVert^2=\sum_{\alpha\in F}\lvert\langle x,e_\alpha\rangle\rvert^2$ and $s_F\to x$, continuity of the norm gives
$$\lVert x\rVert^2=\lim_F\lVert s_F\rVert^2=\sum_\alpha\lvert\langle x,e_\alpha\rangle\rvert^2.$$

**(c)⇒(a)** If $y\perp e_\alpha$ for all $\alpha$ and $\lVert y\rVert=1$, then (c) gives $1=\sum_\alpha0=0$, contradiction. So no unit vector is orthogonal to all $e_\alpha$.

*Separable Hilbert spaces.* Let $H$ be separable and infinite-dimensional, and let $D=\{y_1,y_2,\dots\}$ be a countable dense subset. Apply the Gram–Schmidt process: having constructed orthonormal $e_1,\dots,e_{n-1}$, let $v_n$ be the component of $y_n$ orthogonal to their span; if $v_n=0$ discard $y_n$, otherwise set $e_n=v_n/\lVert v_n\rVert$. The resulting countable orthonormal set has the same closed span as $D$ (each discarded vector was in the span of the previous ones, and each $e_n$ lies in the span of $y_1,\dots,y_n$), hence its closed span is $H$. By (b) it is an orthonormal basis.

Define $U:H\to\ell^2$ by $Ux:=(\langle x,e_n\rangle)_{n\ge1}$. Parseval says $\lVert Ux\rVert_{\ell^2}=\lVert x\rVert$, so $U$ is an isometry. It is surjective: given $c\in\ell^2$, the series $\sum_nc_ne_n$ converges in $H$ because its partial sums are Cauchy ($\lVert\sum_{n=p}^qc_ne_n\rVert^2=\sum_{n=p}^q\lvert c_n\rvert^2$), and its inner product with $e_m$ is $c_m$ by continuity. Hence $U$ is an isometric isomorphism. A finite-dimensional Hilbert space is isometric to $\mathbb{C}^d$ in the same way.

**28.** **(a)** Let $S,T\in\mathcal{K}(X)$ and $\alpha\in\mathbb{F}$. If $(x_n)$ is bounded, compactness of $T$ gives a subsequence $x_{n_k}$ with $Tx_{n_k}$ convergent, and compactness of $S$ applied to the bounded subsequence $x_{n_k}$ gives a further subsequence $x_{n_{k_j}}$ with $Sx_{n_{k_j}}$ convergent. Then $(S+T)x_{n_{k_j}}$ converges. Hence $S+T$ is compact. The case $\alpha T$ is immediate from the definition, and $0$ is compact. So $\mathcal{K}(X)$ is a linear subspace of $\mathcal{B}(X)$.

**(b)** If $(x_n)$ is bounded and $T$ compact, choose a subsequence with $Tx_{n_k}$ convergent; continuity of $S$ makes $STx_{n_k}$ convergent. So $ST$ is compact. For $TS$, note that $(Sx_n)$ is bounded because $S$ is bounded, and compactness of $T$ gives a subsequence with $T(Sx_{n_k})$ convergent. So $TS$ is compact.

**(c)** Let $T_n\in\mathcal{K}(X)$ and $\lVert T_n-T\rVert\to0$. Given $\varepsilon>0$, choose $n$ with $\lVert T-T_n\rVert<\varepsilon/3$. The set $T_n(B_X)$ is relatively compact, so it has a finite $\varepsilon/3$-net $y_1,\dots,y_m$. For $x\in B_X$, choose $j$ with $\lVert T_nx-y_j\rVert<\varepsilon/3$; then
$$\lVert Tx-y_j\rVert\le\lVert T-T_n\rVert+\lVert T_nx-y_j\rVert<\frac{2\varepsilon}{3}<\varepsilon.$$
So $T(B_X)$ is totally bounded, and since $X$ is complete, its closure is compact. Thus $T$ is compact.

**(d)** If $T\in\mathcal{K}(X)$ were invertible with bounded inverse, then $I=T\,T^{-1}$ would be compact by (b), contradicting Proposition 7.47(5) when $\dim X=\infty$.

**(e)** On $\ell^2$, $Tx=\sum_n\frac1n\langle x,e_n\rangle e_n$ is compact by Example 7.48(2) because $1/n\to0$. Its range contains the infinite orthonormal set $\{e_n\}$, so it is infinite-dimensional and $T$ is not of finite rank: a finite-rank operator has finite-dimensional range.

**29.** **(a)** For $f\in C[0,1]$,
$$\lvert Tf(x)\rvert\le\int_0^1\lvert k(x,t)\rvert\,\lvert f(t)\rvert\,dt\le\lVert f\rVert_\infty\sup_x\int_0^1\lvert k(x,t)\rvert\,dt,$$
so $\lVert T\rVert\le\sup_x\int_0^1\lvert k(x,t)\rvert\,dt$.

**(b)** We use the relative-compactness form of Arzelà–Ascoli: a family $\mathcal{F}\subseteq C[0,1]$ is relatively compact in the supremum norm if it is uniformly bounded and equicontinuous. Let $\mathcal{F}:=T(B_{C[0,1]})$.

*Uniform boundedness.* By (a), $\lVert Tf\rVert_\infty\le\lVert k\rVert_\infty\lVert f\rVert_\infty\le\lVert k\rVert_\infty$ for $\lVert f\rVert_\infty\le1$.

*Equicontinuity.* For $x,x'\in[0,1]$ and $\lVert f\rVert_\infty\le1$,
$$\lvert Tf(x)-Tf(x')\rvert\le\int_0^1\lvert k(x,t)-k(x',t)\rvert\,\lvert f(t)\rvert\,dt\le\int_0^1\lvert k(x,t)-k(x',t)\rvert\,dt.$$
The function $k$ is uniformly continuous on the compact square $[0,1]^2$: given $\varepsilon>0$ there is $\delta>0$ such that $\lvert k(x,t)-k(x',t)\rvert<\varepsilon$ whenever $\lvert x-x'\rvert<\delta$, uniformly in $t$. Then $\lvert Tf(x)-Tf(x')\rvert<\varepsilon$ for all $f$ with $\lVert f\rVert_\infty\le1$. So $\mathcal{F}$ is equicontinuous. Arzelà–Ascoli now gives that $\mathcal{F}$ is relatively compact, i.e. $T$ is compact.

**(c)** For $k(x,t)=\min(x,t)$ and $u_n(x)=\sin(k_nx)$ with $k_n=(n-\frac12)\pi$, we have $u_n(0)=0$, $u_n'(1)=0$ and $-u_n''=k_n^2u_n$. Therefore
$$T(k_n^2u_n)(x)=\int_0^1\min(x,t)k_n^2\sin(k_nt)\,dt=\sin(k_nx)=u_n(x),$$
where the identity follows by direct computation: $\int_0^x t k_n^2\sin(k_nt)\,dt+x\int_x^1k_n^2\sin(k_nt)\,dt=\sin(k_nx)$ (differentiate both sides twice, or integrate by parts twice using the boundary conditions). Thus $u_n\in\operatorname{im}T$ for every $n$. The functions $u_n$ are orthogonal in $L^2[0,1]$ (they are eigenfunctions of a self-adjoint operator), hence linearly independent; so $\operatorname{im}T$ is infinite-dimensional and $T$ is not of finite rank.

**30.** **(a)** For $x\in H$, the coefficients $c_n=\langle x,e_n\rangle$ satisfy $\sum_n\lvert c_n\rvert^2=\lVert x\rVert^2$ (Parseval), so the series defining $Tx$ converges absolutely in the coefficient space: $\sum_n\lvert\lambda_nc_n\rvert^2\le(\sup_n\lvert\lambda_n\rvert)^2\lVert x\rVert^2<\infty$. Hence
$$\lVert Tx\rVert^2=\sum_n\lvert\lambda_n\rvert^2\lvert c_n\rvert^2\le\left(\sup_n\lvert\lambda_n\rvert\right)^2\lVert x\rVert^2,$$
so $T$ is bounded with $\lVert T\rVert\le\sup_n\lvert\lambda_n\rvert$. For $x=e_n$, $\lVert Te_n\rVert=\lvert\lambda_n\rvert$, so $\lVert T\rVert\ge\sup_n\lvert\lambda_n\rvert$; equality follows. Self-adjointness: since $\lambda_n\in\mathbb{R}$,
$$\langle Tx,y\rangle=\sum_n\lambda_n\langle x,e_n\rangle\overline{\langle y,e_n\rangle}=\langle x,Ty\rangle.$$

**(b)** If $\lambda_n\to0$, let $T_Nx=\sum_{n\le N}\lambda_n\langle x,e_n\rangle e_n$. Each $T_N$ has finite rank, hence is compact, and
$$\lVert T-T_N\rVert=\sup_{n>N}\lvert\lambda_n\rvert\longrightarrow0.$$
By Proposition 7.47(3), $T$ is compact. Conversely, if $T$ is compact and $\lambda_n\not\to0$, there are $\varepsilon>0$ and indices $n_k$ with $\lvert\lambda_{n_k}\rvert\ge\varepsilon$. Then for $k\ne j$,
$$\lVert Te_{n_k}-Te_{n_j}\rVert^2=\lvert\lambda_{n_k}\rvert^2+\lvert\lambda_{n_j}\rvert^2\ge2\varepsilon^2,$$
so $(Te_n)$ has no Cauchy subsequence, contradicting compactness applied to the bounded sequence $(e_n)$. Hence $\lambda_n\to0$.

**(c)** Assume $\lambda_n\to0$ and group equal nonzero eigenvalues: let $\mu_1,\mu_2,\dots$ be the distinct nonzero values of $\lambda_n$, and let $P_k$ be the orthogonal projection onto the eigenspace $E_k=\{x:Tx=\mu_kx\}$. Then $T=\sum_k\mu_kP_k$ in operator norm, because the partial sums agree with $T$ on the span of the first $N$ eigenspaces and have norm $\sup_{k>N}\lvert\mu_k\rvert\to0$ on the orthogonal complement; the same estimate as in (b) applies. Also $H=\ker T\oplus\overline{\bigoplus_kE_k}$: every $x$ has the expansion $x=\sum_kP_kx+P_0x$, where $P_0$ is the projection onto $\ker T$, and the sum converges because $\sum_k\lVert P_kx\rVert^2\le\lVert x\rVert^2$ and $\lVert P_kx\rVert^2=\lvert\langle x,e\rangle\rvert^2$ over an orthonormal basis of $E_k$. To see that nothing is missed, let $M:=\ker T\oplus\overline{\bigoplus_kE_k}$; its orthogonal complement is invariant under $T$ and contains no nonzero eigenvector of $T$. If the restriction of $T$ to $M^\perp$ were nonzero, Lemma 7.50 would produce a nonzero eigenvector in $M^\perp$, a contradiction; hence $T=0$ on $M^\perp$, so $M^\perp\subseteq\ker T$. But $M^\perp\perp\ker T$, so $M^\perp=\{0\}$ and $M=H$.

If $E_k$ were infinite-dimensional, it would contain an orthonormal sequence $(f_j)$ with $Tf_j=\mu_kf_j$, and then $\lVert Tf_j-Tf_i\rVert^2=2\lvert\mu_k\rvert^2>0$ for $j\ne i$, contradicting compactness. So each $E_k$ is finite-dimensional.

For the spectrum: each $\mu_k$ is an eigenvalue; $0\in\sigma(T)$ because $T$ is not boundedly invertible when infinitely many nonzero eigenvalues tend to $0$ (if it were, $I=TT^{-1}$ would be compact). Conversely, if $\lambda\ne0$ is not equal to any $\mu_k$, then $\delta:=\inf_n\lvert\lambda_n-\lambda\rvert>0$ (only finitely many $\lambda_n$ have $\lvert\lambda_n\rvert\ge\lvert\lambda\rvert/2$, and none equals $\lambda$), and
$$(T-\lambda I)^{-1}y=\sum_n\frac{1}{\lambda_n-\lambda}\langle y,e_n\rangle e_n-\frac1\lambda P_0y$$
is bounded. Hence $\sigma(T)=\{0\}\cup\{\lambda_n:\lambda_n\ne0\}$.

**31.** *Statement.* Let $T\in\mathcal{K}(H)$ be self-adjoint and consider $u-Tu=f$. Then exactly one of the following holds: (i) $\ker(I-T)=\{0\}$ and $I-T$ is bijective with bounded inverse; (ii) $\ker(I-T)$ is a nonzero finite-dimensional space, $\operatorname{im}(I-T)=\ker(I-T)^\perp$ is a proper closed subspace, and the equation is solvable exactly for $f\perp\ker(I-T)$.

*Proof.* By Theorem 7.51, $T=\sum_n\lambda_nP_n$ with $\lambda_n\in\mathbb{R}$, $\lambda_n\to0$, the $P_n$ mutually orthogonal finite-rank projections, and $H=\ker T\oplus\overline{\operatorname{span}}\{e_n\}$.

If $1$ is not an eigenvalue, then $c:=\inf_n\lvert1-\lambda_n\rvert>0$: since $\lambda_n\to0$, only finitely many satisfy $\lvert\lambda_n\rvert>\frac12$, and none of those equals $1$. Hence
$$(I-T)^{-1}f=\sum_n\frac{1}{1-\lambda_n}\langle f,e_n\rangle e_n+P_0f$$
is bounded with norm at most $\max\{1,1/c\}$. This is case (i).

If $1=\lambda_N$ for some $N$, then $E_1:=\ker(I-T)$ is the eigenspace of $T$ for the eigenvalue $1$, which is finite-dimensional by Theorem 7.51 and nonzero by assumption. On $E_1^\perp$, all eigenvalues of $T$ are different from $1$, and $\inf_{\lambda_n\ne1}\lvert1-\lambda_n\rvert>0$ by the same argument. Hence $I-T$ maps $E_1^\perp$ bijectively onto $E_1^\perp$ with bounded inverse. Since $E_1$ is finite-dimensional and $I-T$ vanishes on it, $\operatorname{im}(I-T)=E_1^\perp$; it is closed and proper, and $f\in\operatorname{im}(I-T)$ iff $f\perp E_1$. This is case (ii). The two cases are exhaustive because $1$ is either an eigenvalue or not.

**32.** **(a)** If $x_n\rightharpoonup x$ and $x_n\rightharpoonup y$, then $f(x)=f(y)$ for every $f\in X^*$. Since $X^*$ separates points (Theorem 7.24(2)), $x=y$.

**(b)** For each $n$, let $\varphi_n\in X^{**}$ be $\varphi_n(f):=f(x_n)$. For fixed $f$, $(\varphi_n(f))$ is a convergent scalar sequence, hence bounded. The space $X^*$ is a Banach space (Proposition 7.20). The uniform boundedness principle applied to the family $\{\varphi_n\}$ in $\mathcal{B}(X^*,\mathbb{F})$ gives $\sup_n\lVert\varphi_n\rVert<\infty$. By Theorem 7.24(3), $\lVert\varphi_n\rVert=\lVert x_n\rVert$. Hence $(x_n)$ is bounded.

**(c)** By Theorem 7.24(1), choose $f\in X^*$ with $\lVert f\rVert=1$ and $f(x)=\lVert x\rVert$. Then
$$\lVert x\rVert=f(x)=\lim_nf(x_n)\le\liminf_n\lVert f\rVert\lVert x_n\rVert=\liminf_n\lVert x_n\rVert.$$

**(d)** If $\dim X<\infty$, choose a basis and let $f_1,\dots,f_d$ be the coordinate functionals. If $x_n\rightharpoonup x$, then each coordinate $f_j(x_n)\to f_j(x)$, so $x_n\to x$ in the coordinate norm, hence in the given norm by Theorem 7.10. The converse—norm convergence implies weak convergence—holds in every normed space, since $\lvert f(x_n)-f(x)\rvert\le\lVert f\rVert\lVert x_n-x\rVert$.

**(e)** Let $T\in\mathcal{K}(X,Y)$ and $x_n\rightharpoonup x$. Suppose $Tx_n\not\to Tx$. Then there are $\varepsilon>0$ and a subsequence with $\lVert Tx_{n_k}-Tx\rVert\ge\varepsilon$. The sequence $(x_{n_k}-x)$ is weakly convergent to $0$, hence bounded by (b). Compactness of $T$ gives a further subsequence, relabeled, with $T(x_{n_k}-x)\to z$. For every $g\in Y^*$, the functional $g\circ T$ belongs to $X^*$, so
$$g(z)=\lim_kg\bigl(T(x_{n_k}-x)\bigr)=\lim_k(g\circ T)(x_{n_k}-x)=0.$$
By Theorem 7.24(2), $z=0$, contradicting $\lVert T(x_{n_k}-x)\rVert\ge\varepsilon$.

## Challenge

**33.** **(a)** With $\hat f(k)=\frac1{2\pi}\int_{-\pi}^{\pi}f(t)e^{-ikt}\,dt$,
$$S_nf(0)=\sum_{k=-n}^{n}\hat f(k)=\frac1{2\pi}\int_{-\pi}^{\pi}f(t)\sum_{k=-n}^{n}e^{-ikt}\,dt=\frac1{2\pi}\int_{-\pi}^{\pi}f(t)D_n(t)\,dt,$$
because $\sum_{k=-n}^ne^{-ikt}=D_n(-t)=D_n(t)$ (the Dirichlet kernel is even). Hence
$$\lvert S_nf(0)\rvert\le\frac1{2\pi}\int_{-\pi}^{\pi}\lvert f(t)\rvert\lvert D_n(t)\rvert\,dt\le\lVert f\rVert_\infty\,\lVert D_n\rVert_1.$$
So the norm is at most $\lVert D_n\rVert_1$. For the reverse inequality, approximate the sign of $D_n$ uniformly by continuous functions $f_j$ with $\lVert f_j\rVert_\infty\le1$; then $S_nf_j(0)\to\frac1{2\pi}\int\lvert D_n\rvert=\lVert D_n\rVert_1$, so the norm is at least $\lVert D_n\rVert_1$. (Equivalently, Riesz–Markov–Kakutani identifies the norm of the measure $D_n(t)\,dt/(2\pi)$ with its total variation.)

**(b)** Since $D_n$ is even,
$$\lVert D_n\rVert_1=\frac1{2\pi}\int_{-\pi}^{\pi}\lvert D_n(t)\rvert\,dt=\frac1{\pi}\int_0^{\pi}\lvert D_n(t)\rvert\,dt.$$
On $(0,\pi]$, $\lvert\sin(t/2)\rvert\le t/2$, hence
$$\lvert D_n(t)\rvert=\frac{\lvert\sin((n+\tfrac12)t)\rvert}{\lvert\sin(t/2)\rvert}\ge\frac{2\lvert\sin((n+\tfrac12)t)\rvert}{t}.$$
Therefore
$$\lVert D_n\rVert_1\ge\frac2{\pi}\int_0^{\pi}\frac{\lvert\sin((n+\tfrac12)t)\rvert}{t}\,dt=\frac2{\pi}\int_0^{(n+\frac12)\pi}\frac{\lvert\sin u\rvert}{u}\,du.$$
Split the interval into the half-periods $[(k-\frac12)\pi,(k+\frac12)\pi]$ for $k=1,\dots,n$. On each, $\int\lvert\sin u\rvert\,du=2$ and $1/u\ge1/((k+\frac12)\pi)$. Hence
$$\lVert D_n\rVert_1\ge\frac2{\pi}\sum_{k=1}^{n}\frac{2}{(k+\frac12)\pi}=\frac4{\pi^2}\sum_{k=1}^{n}\frac{1}{k+\frac12}\ge\frac4{\pi^2}\sum_{k=1}^{n}\frac{1}{k+1}\longrightarrow\infty.$$

**(c)** Suppose, for contradiction, that the Fourier series of every $f\in C(\mathbb{T})$ converges at $0$. Then for each fixed $f$, the sequence $(S_nf(0))_n$ converges, hence is bounded. The functionals $S_n$ are bounded by (a), and $C(\mathbb{T})$ is a Banach space with the supremum norm. The uniform boundedness principle (Theorem 7.28) applied to the family $\{S_n\}$ gives
$$\sup_n\lVert S_n\rVert<\infty.$$
But $\lVert S_n\rVert=\lVert D_n\rVert_1\to\infty$ by (b), a contradiction. Therefore some continuous $f$ has a Fourier series that diverges at $0$.

The UBP is used exactly at the step "pointwise boundedness of the family $\{S_n\}$ implies uniform boundedness of the norms"; without completeness of $C(\mathbb{T})$ this implication would not be available, and the divergence conclusion is the standard du Bois-Reymond theorem.

**34.** *Strategy: diagonalise $T^*T$, approximate $T$ by finite-rank operators, and use that adjoints of finite-rank operators are finite rank and that norm limits of compact operators are compact.*

The case $T=0$ is trivial, so assume $T\ne0$. Suppose first that $T$ is compact. Then $T^*T$ is compact (composition of the compact $T$ with the bounded $T^*$) and self-adjoint: $(T^*T)^*=T^*T^{**}=T^*T$. It is positive, since $\langle T^*Tx,x\rangle=\lVert Tx\rVert^2\ge0$. By Theorem 7.51, there are orthonormal eigenvectors $e_n$ of $T^*T$ with eigenvalues $\mu_n\ge0$, $\mu_n\to0$, and
$$T^*T=\sum_n\mu_nP_n,$$
where $P_n$ is the orthogonal projection onto the eigenspace of $\mu_n$, and the series converges in operator norm. Let $P^{(N)}=\sum_{n\le N}P_n$ and define $F_N:=TP^{(N)}$. Then $F_N$ has finite rank, because its range is contained in the span of $Te_1,\dots,Te_N$.

We compute
$$\lVert T-F_N\rVert^2=\lVert(T-TP^{(N)})^*(T-TP^{(N)})\rVert=\lVert(I-P^{(N)})T^*T(I-P^{(N)})\rVert=\sup_{n>N}\mu_n,$$
using the $C^*$-identity $\lVert S^*S\rVert=\lVert S\rVert^2$ (Theorem 7.43(5)), the fact that $P^{(N)}$ commutes with $T^*T$, and the spectral decomposition. The last supremum tends to $0$. Hence $T$ is the norm limit of the finite-rank operators $F_N$.

Now $F_N^*$ is finite rank, hence compact; and $\lVert T^*-F_N^*\rVert=\lVert T-F_N\rVert\to0$. By Proposition 7.47(3), the norm limit $T^*$ is compact. This proves that compactness of $T$ implies compactness of $T^*$. Conversely, if $T^*$ is compact, applying the result just proved to $T^*$ gives that $(T^*)^*=T^{**}=T$ is compact. Hence $T$ is compact if and only if $T^*$ is compact.

**35.** *Strategy: build a countable set whose closed span is everything; if it were not, Hahn–Banach would produce a norm-one functional vanishing on it, contradicting density of the chosen functionals.*

If $X=\{0\}$ there is nothing to prove, so assume $X\ne\{0\}$. Let $(f_n)$ be a countable dense sequence in $X^*$. For each $n$ with $f_n\ne0$, choose $x_n\in X$ with $\lVert x_n\rVert=1$ and
$$\lvert f_n(x_n)\rvert\ge\tfrac12\lVert f_n\rVert;$$
such an $x_n$ exists by the definition of the norm of $f_n$ as a supremum over the unit sphere. (If $f_n=0$, take any unit vector, or skip the index.) Let $M:=\overline{\operatorname{span}}\{x_n:n\ge1\}$, a closed subspace.

Suppose $M\ne X$. Choose $x_0\in X\setminus M$. By the distance formula (Theorem 7.24(4)) there is $f\in X^*$ with $\lVert f\rVert=1$, $f|_M=0$, and $f(x_0)=d(x_0,M)>0$. In particular $f\ne0$. Choose $n$ with $\lVert f-f_n\rVert<\frac14$. Then, since $f(x_n)=0$ and $\lVert x_n\rVert=1$,
$$\lvert f_n(x_n)\rvert=\lvert f_n(x_n)-f(x_n)\rvert\le\lVert f_n-f\rVert\lVert x_n\rVert<\frac14.$$
On the other hand $\lvert f_n(x_n)\rvert\ge\frac12\lVert f_n\rVert$, so $\lVert f_n\rVert<\frac12$. Therefore
$$\lVert f\rVert\le\lVert f-f_n\rVert+\lVert f_n\rVert<\frac14+\frac12=\frac34,$$
contradicting $\lVert f\rVert=1$. Hence $M=X$.

The set of all finite linear combinations of the $x_n$ with coefficients in $\mathbb{Q}$ (or $\mathbb{Q}+i\mathbb{Q}$ in the complex case) is countable. It is dense: it contains all finite linear combinations with scalar coefficients by approximation of scalars, and those are dense in $\operatorname{span}\{x_n\}$, whose closure is $X$. Hence $X$ is separable.

**36.** *Strategy: turn the sesquilinear form into an operator via Riesz, prove the operator is bounded below with dense range, then invert.*

Let $B$ be sesquilinear, linear in the first argument and conjugate-linear in the second. For fixed $u\in H$, the map $v\mapsto\overline{B(u,v)}$ is linear and bounded, since $\lvert\overline{B(u,v)}\rvert\le M\lVert u\rVert\lVert v\rVert$. By the Riesz representation theorem, there is a unique $Au\in H$ with
$$\overline{B(u,v)}=\langle v,Au\rangle,\qquad\text{i.e.}\qquad B(u,v)=\langle Au,v\rangle.$$

*$A$ is linear and bounded.* For $u,w\in H$ and scalars $\alpha,\beta$,
$$\langle A(\alpha u+\beta w),v\rangle=B(\alpha u+\beta w,v)=\alpha B(u,v)+\beta B(w,v)=\langle \alpha Au+\beta Aw,v\rangle$$
for all $v$, so $A(\alpha u+\beta w)=\alpha Au+\beta Aw$. Also $\lVert Au\rVert=\sup_{\lVert v\rVert\le1}\lvert\langle Au,v\rangle\rvert=\sup_{\lVert v\rVert\le1}\lvert B(u,v)\rvert\le M\lVert u\rVert$, so $\lVert A\rVert\le M$.

*$A$ is bounded below.* Coercivity gives, for every $u$,
$$c\lVert u\rVert^2\le\lvert B(u,u)\rvert=\lvert\langle Au,u\rangle\rvert\le\lVert Au\rVert\lVert u\rVert,$$
so $\lVert Au\rVert\ge c\lVert u\rVert$. Hence $A$ is injective, and its range is closed: if $Au_n\to y$, then $(u_n)$ is Cauchy because $\lVert u_n-u_m\rVert\le c^{-1}\lVert Au_n-Au_m\rVert$, so $u_n\to u$; continuity gives $Au=y\in\operatorname{im}A$.

*The range is dense.* Suppose $w\perp\operatorname{im}A$. Then $\langle Aw,w\rangle=0$, so
$$c\lVert w\rVert^2\le\lvert B(w,w)\rvert=\lvert\langle Aw,w\rangle\rvert=0,$$
hence $w=0$. A closed dense subspace is all of $H$, so $A$ is bijective, and $A^{-1}$ is bounded with $\lVert A^{-1}\rVert\le c^{-1}$.

*Solving the equation.* Let $f\in H^*$. By Riesz there is $z\in H$ with $f(v)=\langle z,v\rangle$ for all $v$ and $\lVert z\rVert=\lVert f\rVert$. Put $u:=A^{-1}z$. Then for every $v$,
$$B(u,v)=\langle Au,v\rangle=\langle z,v\rangle=f(v).$$
Moreover $\lVert u\rVert\le c^{-1}\lVert z\rVert=c^{-1}\lVert f\rVert$.

*Uniqueness.* If $B(u,v)=0$ for all $v$, then coercivity with $v=u$ gives $c\lVert u\rVert^2\le\lvert B(u,u)\rvert=0$, so $u=0$.

**37.** **(a)** Let $(x^{(n)})$ satisfy $\lVert x^{(n)}\rVert_2\le1$. The first coordinates $x^{(n)}_1$ form a bounded sequence in $\mathbb{F}$, so choose a subsequence on which they converge. From that subsequence choose a further subsequence on which the second coordinates converge, and continue. Taking the diagonal subsequence $n_j$ (the $j$-th term of the $j$-th subsequence) gives a sequence such that $x^{(n_j)}_k$ converges for every fixed $k$. Let $x_k:=\lim_jx^{(n_j)}_k$.

For each finite $K$, $\sum_{k\le K}\lvert x_k\rvert^2=\lim_j\sum_{k\le K}\lvert x^{(n_j)}_k\rvert^2\le1$; letting $K\to\infty$ gives $x\in\ell^2$ and $\lVert x\rVert_2\le1$.

Let $y\in\ell^2$ and $\varepsilon>0$. Choose $K$ with $\sum_{k>K}\lvert y_k\rvert^2<\varepsilon^2/16$. For every $j$,
$$\lvert\langle x^{(n_j)}-x,y\rangle\rvert\le\sum_{k\le K}\lvert x^{(n_j)}_k-x_k\rvert\,\lvert y_k\rvert+\sum_{k>K}\bigl(\lvert x^{(n_j)}_k\rvert+\lvert x_k\rvert\bigr)\lvert y_k\rvert.$$
The first sum tends to $0$ as $j\to\infty$ (finitely many convergent coordinates). The second is at most
$$\bigl(\sup_j\lVert x^{(n_j)}\rVert_2+\lVert x\rVert_2\bigr)\left(\sum_{k>K}\lvert y_k\rvert^2\right)^{1/2}\le2\cdot\frac{\varepsilon}{4}=\frac{\varepsilon}{2}.$$
So for large $j$ the whole expression is less than $\varepsilon$. Hence $x^{(n_j)}\rightharpoonup x$.

**(b)** The vectors $e_n$ have norm $1$ and $\lVert e_n-e_m\rVert_2=\sqrt2$ for $n\ne m$; a norm-convergent subsequence would be Cauchy, which is impossible. So the closed unit ball is not norm compact.

**(c)** There is no contradiction: weak convergence is convergence in a *coarser* topology than norm convergence. A set can fail to be compact in a fine topology while being compact in a coarser one. Indeed, $\ell^2$ is reflexive, so the closed unit ball is weakly compact (Kakutani's theorem, via Banach–Alaoglu); part (a) proves the sequential version directly. Norm compactness of the unit ball would force finite dimension (Theorem 7.11), whereas weak compactness is compatible with infinite dimension in every reflexive space.

**38.** **(a)** $K$ has rank one: $(Kf)(x)=x\int_0^1t f(t)\,dt$, so its range is contained in $\operatorname{span}\{x\}$. It is nonzero, since $Kx=x\int_0^1t^2dt=x/3$. Hence $K$ is compact (finite rank). It is self-adjoint because
$$\langle Kf,g\rangle=\int_0^1\int_0^1xt\,f(t)\overline{g(x)}\,dt\,dx=\int_0^1f(t)\,\overline{t\int_0^1xg(x)\,dx}\,dt=\langle f,Kg\rangle,$$
using that $xt$ is real and symmetric. The eigenvalue is $\lambda_1=1/3$ with eigenfunction $x$.

**(b)** The equation is
$$u(x)=f(x)+\lambda x\,c,\qquad c:=\int_0^1t\,u(t)\,dt.$$
Multiplying by $t$ and integrating,
$$c=\int_0^1tf(t)\,dt+\lambda c\int_0^1t^2\,dt=f_1+\frac{\lambda c}{3},\qquad f_1:=\int_0^1tf(t)\,dt.$$
Hence
$$c\left(1-\frac{\lambda}{3}\right)=f_1.$$
If $\lambda\ne3$, there is a unique solution
$$u(x)=f(x)+\frac{\lambda f_1}{1-\lambda/3}\,x.$$
If $\lambda=3$, the equation for $c$ reads $0=f_1$. So a solution exists exactly when $f_1=\int_0^1tf(t)\,dt=0$, and then $c$ is arbitrary and
$$u(x)=f(x)+3cx,\qquad c\in\mathbb{R}.$$

**(c)** At $\lambda=3$, $\ker(I-3K)=\{u:u=3Ku\}$. From (b), $u=3Ku$ means $u=3cx$ with $c$ arbitrary, so $\ker(I-3K)=\operatorname{span}\{x\}$, one-dimensional. The range is
$$\operatorname{im}(I-3K)=\{f:f_1=0\}=\left\{f:\int_0^1t f(t)\,dt=0\right\}=\{x\}^\perp,$$
which is closed and has codimension one. Solvability is exactly the condition $f\perp\ker(I-3K)$, as the Fredholm alternative predicts. The exceptional value $\lambda=3$ is the reciprocal of the nonzero eigenvalue $1/3$ of $K$; this is the general pattern: $I-\lambda K$ fails to be invertible exactly when $1/\lambda$ is an eigenvalue of $K$.



