# Compactness — Solutions

> [Tutorial](README.md) · [Exercises](exercises.md) · 36 worked solutions

Each solution states the strategy, checks the hypotheses, and verifies the conclusion. References such as
"Theorem 7.1" point to the tutorial.

## Beginner

### Solution 1

An **open cover** of $X$ is a family $\{U_i\}_{i\in I}$ of open sets with $X=\bigcup_iU_i$. A **subcover** is a
subfamily that still covers $X$; it is finite if it has finitely many members. $X$ is **compact** if every open
cover has a finite subcover.

If $X=\{x_1,\dots,x_n\}$ is finite and $\{U_i\}$ is an open cover, choose for each $j$ an index $i_j$ with
$x_j\in U_{i_j}$. Then $U_{i_1},\dots,U_{i_n}$ is a finite subcover. Hence $X$ is compact. ∎

### Solution 2

In the discrete topology every singleton $\{x\}$ is open. If $X$ is compact, the cover
$\{\{x\}:x\in X\}$ has a finite subcover; but every subcover of the singleton cover is the whole cover, so
$X$ is finite. Conversely, a finite discrete space is compact by Solution 1. ∎

### Solution 3

In the indiscrete topology the only open sets are $\varnothing$ and $X$. If $X\ne\varnothing$, every open cover
contains $X$, so $\{X\}$ is a finite subcover. If $X=\varnothing$, the empty family is a finite open cover.
Hence $X$ is compact. ∎

### Solution 4

Let $X$ be cofinite and $\{U_i\}_{i\in I}$ an open cover. If $X=\varnothing$, the result is trivial. Otherwise
choose a nonempty $U_{i_0}$. Its complement $X\setminus U_{i_0}$ is finite, say $\{x_1,\dots,x_m\}$. For each
$j$, choose $U_{i_j}$ containing $x_j$. Then $U_{i_0},U_{i_1},\dots,U_{i_m}$ cover $X$, a finite subcover. ∎

### Solution 5

Let $\mathcal{U}=\{(1/n,1):n\ge2\}$. For $x\in(0,1)$, choose $n>1/x$; then $x\in(1/n,1)$, so $\mathcal{U}$
covers $(0,1)$. If $n_1,\dots,n_k$ are finitely many indices and $N=\max n_j$, then
$$\bigcup_{j=1}^k\left(\frac1{n_j},1\right)=\left(\frac1N,1\right),$$
which does not contain $1/(N+1)\in(0,1)$. Hence no finite subcover exists. ∎

### Solution 6

Let $\mathcal{U}=\{[0,1-1/n):n\ge2\}$. Each set is open in the subspace $[0,1)$, because
$[0,1-1/n)=[0,1)\cap(-1,1-1/n)$. Every $x\in[0,1)$ satisfies $x<1$, so choosing $n$ with $1/n<1-x$ gives
$x<1-1/n$. Thus $\mathcal{U}$ covers $[0,1)$. A finite subcover has a largest $N$ and union $[0,1-1/N)$,
which misses $1-1/(2N)\in[0,1)$. ∎

### Solution 7

The cover $\{(-n,n):n\in\mathbb{N}\}$ is open. A finite subcover has a largest $N$ and union $(-N,N)$, which
misses $N\in\mathbb{R}$. Hence $\mathbb{R}$ is not compact. ∎

### Solution 8

With the discrete topology, $\{\{n\}:n\in\mathbb{Z}\}$ is an open cover. Any subcover that covers all of
$\mathbb{Z}$ must contain every singleton, so there is no finite subcover. ∎

### Solution 9

Take
$$\mathcal{U}=\left\{\left(-1,1-\frac1n\right):n\ge2\right\}\cup\{(0,2)\}.$$
It covers $[0,1]$: points $x<1$ lie in $(-1,1-1/n)$ for large $n$, and $x=1$ lies in $(0,2)$. A finite
subcover is $\{(-1,1/2),(0,2)\}$: every $x\in[0,1/2)$ is in the first set, and every $x\in(0,1]$ is in the
second (and $1/2$ is in $(0,2)$). ✓

### Solution 10

Let $X$ be compact, $F\subseteq X$ closed, and $\{U_i\}$ an open cover of $F$. Then
$\{U_i\}\cup\{X\setminus F\}$ is an open cover of $X$: points of $F$ lie in some $U_i$, and points outside $F$
lie in $X\setminus F$. By compactness, finitely many sets cover $X$. Discarding $X\setminus F$ if necessary
leaves finitely many $U_i$'s covering $F$. ∎

### Solution 11

Let $f:X\to Y$ be continuous, $X$ compact, and $\{V_i\}$ an open cover of $f[X]$. Then
$\{f^{-1}[V_i]\}$ is an open cover of $X$. Choose a finite subcover
$f^{-1}[V_{i_1}],\dots,f^{-1}[V_{i_n}]$. For $y\in f[X]$, write $y=f(x)$; then $x\in f^{-1}[V_{i_j}]$ for some
$j$, so $y\in V_{i_j}$. Hence $V_{i_1},\dots,V_{i_n}$ cover $f[X]$.

For $f(x)=x^2$ on $[-1,1]$, the image is $[0,1]$, which is compact (closed and bounded in $\mathbb{R}$). ✓

### Solution 12

Let $K\subseteq X$ be compact and $X$ Hausdorff. For $x\notin K$, separate $x$ from each $k\in K$ by disjoint
open sets $U_k\ni x$, $V_k\ni k$. The $V_k$ cover $K$; choose finitely many $V_{k_1},\dots,V_{k_n}$ covering
$K$. Then $U=U_{k_1}\cap\cdots\cap U_{k_n}$ is an open neighbourhood of $x$ disjoint from $K$. Hence
$X\setminus K$ is open, so $K$ is closed.

For $[0,1]\subseteq\mathbb{R}$: $\mathbb{R}$ is Hausdorff, and $[0,1]$ is compact by Heine–Borel; the theorem
then says $[0,1]$ is closed, which it is. ✓

## Intermediate

### Solution 13

Let $K_1,\dots,K_n$ be compact and let $\{U_i\}$ be an open cover of $K=K_1\cup\cdots\cup K_n$. For each $j$,
the sets $U_i$ cover $K_j$; choose a finite subcover $\mathcal{V}_j$. Then
$\mathcal{V}_1\cup\cdots\cup\mathcal{V}_n$ is a finite subcover of $K$. ∎

### Solution 14

Each $[-n,n]$ is compact by Heine–Borel. Their union is $\mathbb{R}$, since every real $x$ lies in $[-n,n]$ for
$n>|x|$. But $\mathbb{R}$ is not compact (cover $(-n,n)$). Hence an arbitrary union of compact sets need not
be compact. ∎

### Solution 15

Let $K_1,K_2$ be compact subsets of a Hausdorff space. By Theorem 7.2, both are closed; hence $K_1\cap K_2$ is
closed. Since $K_1\cap K_2\subseteq K_1$ and $K_1$ is compact, the closed subset $K_1\cap K_2$ is compact by
Theorem 7.1. ∎

### Solution 16

Let $X$ be compact metric and $(x_n)$ Cauchy. By Theorem 7.14, $X$ is sequentially compact, so a subsequence
$x_{n_k}$ converges to some $x$. Given $\varepsilon>0$, choose $K$ with $d(x_{n_k},x)<\varepsilon/2$ for
$k\ge K$, and $N$ with $d(x_n,x_m)<\varepsilon/2$ for $n,m\ge N$. Pick $k\ge K$ with $n_k\ge N$. For $n\ge N$,
$$d(x_n,x)\le d(x_n,x_{n_k})+d(x_{n_k},x)<\frac\varepsilon2+\frac\varepsilon2=\varepsilon.$$
Hence $x_n\to x$, so $X$ is complete. ∎

### Solution 17

Suppose $X$ is compact metric but not totally bounded. Then there is $\varepsilon>0$ such that no finite
$\varepsilon$-net exists. Choose $x_1\in X$; having chosen $x_1,\dots,x_n$, choose
$x_{n+1}\notin\bigcup_{i=1}^nB_\varepsilon(x_i)$. Then $d(x_i,x_j)\ge\varepsilon$ for $i\ne j$, so the sequence
has no Cauchy subsequence and hence no convergent subsequence. This contradicts the sequential compactness of
$X$ (Theorem 7.14). ∎

### Solution 18

For each $n$, total boundedness (Solution 17) gives finitely many points $x_{n,1},\dots,x_{n,m_n}$ such that the
balls $B_{1/n}(x_{n,j})$ cover $X$. Let $D=\{x_{n,j}:n\in\mathbb{N},\ 1\le j\le m_n\}$, a countable union of
finite sets, hence countable. For $x\in X$ and $\varepsilon>0$, choose $n>1/\varepsilon$; then $x$ lies in
some $B_{1/n}(x_{n,j})$, so $d(x,x_{n,j})<1/n<\varepsilon$. Hence $D$ is dense and $X$ is separable. ∎

### Solution 19

Suppose an open cover $\mathcal{U}$ of $[0,1]$ has no finite subcover. Set $I_0=[0,1]$. Bisect $I_n=[a_n,b_n]$
at its midpoint. The two halves cover $I_n$; if both had finite subcovers, their union would be a finite
subcover of $I_n$. So one half has no finite subcover; call it $I_{n+1}$. Thus $I_0\supseteq I_1\supseteq\cdots$,
$b_n-a_n=2^{-n}$, and no $I_n$ has a finite subcover. By the nested interval theorem,
$\bigcap_nI_n=\{x\}$ for some $x\in[0,1]$. Choose $U\in\mathcal{U}$ containing $x$. Since $U$ is open, there is
$\varepsilon>0$ with $(x-\varepsilon,x+\varepsilon)\subseteq U$. For $n$ large, $b_n-a_n<\varepsilon$ and
$x\in I_n$, so $I_n\subseteq(x-\varepsilon,x+\varepsilon)\subseteq U$. Thus one set $U$ covers $I_n$,
contradicting the construction. ∎

### Solution 20

$S^1=\{(x,y):x^2+y^2=1\}$ is closed (preimage of $\{1\}$ under the continuous map $(x,y)\mapsto x^2+y^2$) and
bounded (every point has norm $1$). By Heine–Borel it is compact. The closed disk
$\overline{B_1(0)}=\{(x,y):x^2+y^2\le1\}$ is also closed and bounded, hence compact. ∎

### Solution 21

$f(x)=x^3-3x$ is continuous and $[0,2]$ is compact, so the extreme value theorem applies. The critical points
satisfy $f'(x)=3x^2-3=0$, so $x=\pm1$; in $[0,2]$ only $x=1$. Values:
$$f(0)=0,\qquad f(1)=1-3=-2,\qquad f(2)=8-6=2.$$
Hence the maximum is $2$ at $x=2$, and the minimum is $-2$ at $x=1$. ✓

### Solution 22

$f(x)=1/x$ is continuous on $(0,1)$. Take $x_n=1/n$ and $y_n=1/(n+1)$. Then
$|x_n-y_n|=1/(n(n+1))\to0$, but
$$|f(x_n)-f(y_n)|=|n-(n+1)|=1,$$
so for $\varepsilon=1/2$ no single $\delta$ works. Hence $f$ is not uniformly continuous. Theorem 7.26 requires
the domain to be compact; $(0,1)$ is not compact (Solution 5). ∎

### Solution 23

Let $r_n$ be rationals increasing to $\sqrt2$ (for example, the decimal truncations of $\sqrt2$). Put
$U_n=(-\infty,r_n)\cap(\mathbb{Q}\cap[0,1])$. Each $U_n$ is open in the subspace $\mathbb{Q}\cap[0,1]$, and the
$U_n$ cover it because every rational $q\in[0,1]$ satisfies $q<\sqrt2$ and hence $q<r_n$ for large $n$. A finite
subcover has a largest $r_N<\sqrt2$; choose a rational $q$ with $r_N<q<\sqrt2$ (density of $\mathbb{Q}$). Then
$q\in[0,1]$ is not covered. Hence no finite subcover exists. ∎

## Advanced

### Solution 24

Let $X$ be compact metric and $(x_n)$ a sequence. Suppose no subsequence converges. Then for each $x\in X$
there is $\varepsilon_x>0$ such that $B_{\varepsilon_x}(x)$ contains only finitely many terms of the sequence:
otherwise, if every ball $B_{1/k}(x)$ contained infinitely many terms, choose $n_1<n_2<\cdots$ with
$x_{n_k}\in B_{1/k}(x)$, and $x_{n_k}\to x$, a convergent subsequence. The balls $B_{\varepsilon_x}(x)$ cover
$X$; choose finitely many covering $X$. Each contains finitely many terms, so their union contains finitely
many terms, contradicting that the sequence has infinitely many indices. Hence a convergent subsequence
exists. ∎

### Solution 25

Let $X$ be sequentially compact metric.

*Total boundedness.* If some $\varepsilon>0$ had no finite $\varepsilon$-net, choose
$x_{n+1}\notin\bigcup_{i\le n}B_\varepsilon(x_i)$ recursively. Then $d(x_i,x_j)\ge\varepsilon$ for $i\ne j$, so
no subsequence is Cauchy, contradicting sequential compactness (a convergent subsequence is Cauchy).

*Lebesgue number.* Let $\mathcal{U}$ be an open cover. Suppose no $\lambda>0$ works. Then for each $n$ there is
$A_n$ with $\operatorname{diam}A_n<1/n$ contained in no member of $\mathcal{U}$. Choose $x_n\in A_n$;
sequential compactness gives $x_{n_k}\to x$. Choose $U\in\mathcal{U}$ containing $x$ and $r>0$ with
$B_r(x)\subseteq U$. For large $k$, $d(x_{n_k},x)<r/2$ and $1/n_k<r/2$, so for $y\in A_{n_k}$,
$$d(y,x)\le d(y,x_{n_k})+d(x_{n_k},x)<1/n_k+r/2<r.$$
Thus $A_{n_k}\subseteq U$, a contradiction.

*Finite subcover.* By total boundedness choose a finite $\lambda/3$-net $x_1,\dots,x_m$. Each
$B_{\lambda/3}(x_i)$ has diameter at most $2\lambda/3<\lambda$, so it lies in some $U_i\in\mathcal{U}$. The
balls cover $X$, so $U_1,\dots,U_m$ is a finite subcover. ∎

### Solution 26

**Lemma.** $[a,b]$ is compact. Suppose $\mathcal{U}$ is an open cover with no finite subcover. Bisect $[a,b]$;
one half has no finite subcover. Iterate to get nested closed intervals $I_n$ with
$\operatorname{length}(I_n)=(b-a)/2^n$, none finitely covered. By the nested interval theorem,
$\bigcap I_n=\{x\}$. Choose $U\in\mathcal{U}$ containing $x$ and $\varepsilon>0$ with
$(x-\varepsilon,x+\varepsilon)\subseteq U$. For $n$ large, $I_n\subseteq(x-\varepsilon,x+\varepsilon)\subseteq U$,
contradicting that $I_n$ has no finite subcover.

**Tube lemma.** If $X,Y$ are spaces, $Y$ compact, $N\subseteq X\times Y$ open and
$\{x_0\}\times Y\subseteq N$, then there is an open neighbourhood $W$ of $x_0$ with $W\times Y\subseteq N$.
For each $y$ choose a basic open $U_y\times V_y\subseteq N$ containing $(x_0,y)$. Finitely many $V_{y_1},\dots,V_{y_m}$
cover $Y$. Let $W=U_{y_1}\cap\cdots\cap U_{y_m}$; then $W\times Y\subseteq N$.

**Products.** If $X,Y$ are compact, then $X\times Y$ is compact. Cover $X\times Y$ by open sets. For each
$x$, finitely many cover the slice $\{x\}\times Y$; the tube lemma gives a neighbourhood $W_x$ of $x$ whose
product with $Y$ is covered by those finitely many sets. Finitely many $W_x$ cover $X$; the corresponding
finite collections cover $X\times Y$.

**Closed boxes.** By induction, $[a_1,b_1]\times\cdots\times[a_n,b_n]$ is compact: it is
$([a_1,b_1]\times\cdots\times[a_{n-1},b_{n-1}])\times[a_n,b_n]$, a product of two compact spaces.

**Heine–Borel.** If $K$ is compact, it is closed (compact in the Hausdorff space $\mathbb{R}^n$) and bounded
(cover by balls $B_m(0)$). Conversely, if $K$ is closed and bounded, then $K\subseteq[-M,M]^n$ for some $M$.
The box is compact, and $K$ is a closed subset of it; hence $K$ is compact. ∎

### Solution 27

Let $X$ be compact metric, $Y$ metric, $f:X\to Y$ continuous, and $\varepsilon>0$. The balls
$B_{\varepsilon/2}(y)$, $y\in Y$, cover $Y$; their preimages form an open cover of $X$. Let $\lambda$ be a
Lebesgue number (Theorem 7.25). If $d(x,x')<\lambda$, the set $\{x,x'\}$ has diameter less than $\lambda$, so it
lies in some $f^{-1}[B_{\varepsilon/2}(y)]$. Then $f(x),f(x')\in B_{\varepsilon/2}(y)$, so
$d(f(x),f(x'))<\varepsilon$. Hence $f$ is uniformly continuous. ∎

### Solution 28

Let $X$ be compact metric and $\mathcal{U}$ an open cover. By Theorem 7.14, $X$ is sequentially compact. Suppose
no $\lambda>0$ works. For each $n$, choose $A_n$ with $\operatorname{diam}A_n<1/n$ and $A_n$ not contained in
any member of $\mathcal{U}$; choose $x_n\in A_n$. A subsequence $x_{n_k}\to x$. Choose $U\in\mathcal{U}$
containing $x$ and $r>0$ with $B_r(x)\subseteq U$. For large $k$, $d(x_{n_k},x)<r/2$ and $1/n_k<r/2$, so for
$y\in A_{n_k}$,
$$d(y,x)\le d(y,x_{n_k})+d(x_{n_k},x)<1/n_k+r/2<r.$$
Thus $A_{n_k}\subseteq U$, contradiction. Hence a Lebesgue number exists. ∎

### Solution 29

Let $X$ be locally compact Hausdorff and $X^*=X\cup\{\infty\}$ with the topology of Construction 7.21. If
$\{U_i\}$ is an open cover of $X^*$, choose $U_{i_0}$ containing $\infty$. Then $K=X^*\setminus U_{i_0}$ is
compact in $X$. The remaining sets cover $K$; choose finitely many covering $K$. Together with $U_{i_0}$ they
cover $X^*$, so $X^*$ is compact.

For Hausdorff: distinct points of $X$ are separated by $X$'s Hausdorff property. For $x\in X$ and $\infty$,
local compactness gives an open $V$ with $x\in V\subseteq K$ and $K$ compact. Then $V$ and $X^*\setminus K$ are
disjoint open neighbourhoods of $x$ and $\infty$. Hence $X^*$ is Hausdorff. ∎

### Solution 30

Suppose $\mathbb{Q}$ is locally compact. Then some $x\in\mathbb{Q}$ has a compact neighbourhood $K$; by
definition $K$ contains an open $U\ni x$, and $U$ contains $(x-\varepsilon,x+\varepsilon)\cap\mathbb{Q}$ for
some $\varepsilon>0$. Choose an irrational $\alpha\in(x-\varepsilon,x+\varepsilon)$ and rationals
$q_n\to\alpha$ in that interval. Then $(q_n)$ is Cauchy in $K$. Since $K$ is a compact metric space, it is
sequentially compact (Theorem 7.14), so some subsequence $q_{n_k}$ converges to $y\in K\subseteq\mathbb{Q}$.
But in $\mathbb{R}$ the subsequence also converges to $\alpha$, so $y=\alpha\notin\mathbb{Q}$, a contradiction.
Hence $\mathbb{Q}$ is not locally compact. ∎

### Solution 31

Replacing $f_n$ by $-f_n$ if necessary, assume $f_n\ge f_{n+1}\ge f$ and $f_n\to f$ pointwise. Put
$g_n=f_n-f$, so $g_n\ge0$ is continuous, $g_n\ge g_{n+1}$, and $g_n\to0$ pointwise. For $\varepsilon>0$, the
sets $U_n=\{x:g_n(x)<\varepsilon\}$ are open, increase with $n$, and cover $X$ because $g_n(x)\to0$ for each
$x$. By compactness, finitely many $U_{n_1},\dots,U_{n_k}$ cover $X$; let $N=\max n_j$. Since the $U_n$ increase,
$U_N=X$. Hence for all $x\in X$ and all $n\ge N$, $0\le g_n(x)\le g_N(x)<\varepsilon$. Thus $f_n\to f$
uniformly. ∎

## Challenge

### Solution 32

(⇒) If $X$ is compact and $f:X\to\mathbb{R}$ continuous, then $f[X]$ is compact (Theorem 7.4), hence closed and
bounded (Corollary 7.3). So $f$ is bounded.

(⇐) Contrapositive. Suppose $X$ is a metric space that is not compact. By Corollary 7.19, $X$ is not
sequentially compact, so there is a sequence $(x_n)$ with no convergent subsequence. Passing to a subsequence
if necessary, assume the $x_n$ are distinct. Then no point of $X$ is a cluster point of the set $S=\{x_n\}$,
and each $x_n$ is isolated in $S$. For each $n$, choose $r_n>0$ with $r_n<1/n$ and
$B(x_n,2r_n)\cap S=\{x_n\}$ (otherwise a sequence of other points of $S$ would converge to $x_n$). The open
balls $B(x_n,r_n)$ are pairwise disjoint and their radii tend to $0$. Define
$$\varphi_n(x)=\max\left(0,1-\frac{d(x,x_n)}{r_n}\right),$$
a continuous function supported in $B(x_n,r_n)$ with $\varphi_n(x_n)=1$. Let
$$f(x)=\sum_{n=1}^{\infty}n\,\varphi_n(x).$$
At most one term is nonzero at any $x$ (the supports are disjoint). The family of supports is locally finite:
if a sequence $y_k$ with $y_k\in B(x_{n_k},r_{n_k})$ converged to $y$ and the indices $n_k$ were unbounded, then
$d(y,x_{n_k})\le d(y,y_k)+r_{n_k}\to0$, producing a convergent subsequence of $(x_n)$, impossible. Hence
near each point only finitely many (in fact at most one) term is nonzero, so $f$ is well defined and
continuous. But $f(x_n)=n$, so $f$ is unbounded. Thus if every continuous real-valued function on $X$ is
bounded, $X$ must be compact. ∎

### Solution 33

Let $Y$ be a compact Hausdorff space with $X\subseteq Y$ open and dense, $Y\setminus X=\{p\}$. Define
$\varphi:X^*\to Y$ by $\varphi(x)=x$ for $x\in X$ and $\varphi(\infty)=p$. It is a bijection. It is continuous:
if $V\subseteq Y$ is open and $p\notin V$, then $\varphi^{-1}(V)=V\cap X$ is open in $X$, hence in $X^*$. If
$p\in V$, then $Y\setminus V$ is closed in the compact space $Y$, hence compact, and lies in $X$ (as
$p\notin Y\setminus V$); so $X\setminus V=Y\setminus V$ is compact in $X$, and
$\varphi^{-1}(V)=V\cup\{\infty\}=X^*\setminus(X\setminus V)$ is open in $X^*$. Thus $\varphi$ is continuous.
Since $X^*$ is compact (Theorem 7.22) and $Y$ is Hausdorff, Corollary 7.6 implies $\varphi$ is a homeomorphism.
It fixes $X$ pointwise by construction. ∎

### Solution 34

Let $e_n=(0,\dots,0,1,0,\dots)$ be the $n$-th standard basis vector in
$\ell^2=\{x=(x_k):\sum_k|x_k|^2<\infty\}$. Then $\lVert e_n\rVert=1$, so all $e_n$ lie in the closed unit
ball, and $\lVert e_n-e_m\rVert=\sqrt2$ for $n\ne m$. Hence the sequence $(e_n)$ has no Cauchy subsequence, so
no convergent subsequence. A metric space that is compact is sequentially compact, so the closed unit ball is
not compact. It is closed (the norm is continuous) and bounded (norm $1$), which shows that Heine–Borel fails
in infinite-dimensional normed spaces. ∎

### Solution 35

Let $\mathcal{U}=\{(1/n,1):n\ge2\}$ be the standard cover of $(0,1)$. Suppose $\lambda>0$ were a Lebesgue
number. Choose $n>2/\lambda$ and let $A=(0,1/n]$. Then $\operatorname{diam}A=1/n<\lambda/2<\lambda$. But no
member of $\mathcal{U}$ contains $A$: for any $m$, the set $(1/m,1)$ excludes points of $A$ that are at most
$1/m$ (and $A$ contains such points, since it contains all sufficiently small positive numbers). Hence no
$\lambda$ works; the cover has no Lebesgue number.

The Lebesgue number lemma requires compactness. For the compact interval $[0,1]$, every open cover does have a
Lebesgue number; for the noncompact $(0,1)$, the cover above fails. This is exactly the point of Theorem 7.25.
∎

### Solution 36

**Theorem.** Let $(F_n)$ be a nested sequence of nonempty closed subsets of a complete metric space $X$ with
$\operatorname{diam}F_n\to0$. Then $\bigcap_nF_n$ is a single point.

*Proof.* Choose $x_n\in F_n$. Given $\varepsilon>0$, choose $N$ with $\operatorname{diam}F_N<\varepsilon$. For
$n,m\ge N$, both $x_n,x_m\in F_N$, so $d(x_n,x_m)<\varepsilon$. Hence $(x_n)$ is Cauchy; by completeness it
converges to some $x$. For each $k$, all $x_n$ with $n\ge k$ lie in $F_k$, and $F_k$ is closed, so $x\in F_k$.
Thus $x\in\bigcap_nF_n$. If $x,y\in\bigcap_nF_n$, then $d(x,y)\le\operatorname{diam}F_n$ for every $n$, so
$d(x,y)=0$ and $x=y$. ∎

**Completeness is necessary.** In $\mathbb{Q}$ with the usual metric, let
$$F_n=\left[\sqrt2-\frac1n,\sqrt2+\frac1n\right]\cap\mathbb{Q}.$$
Each $F_n$ is closed in $\mathbb{Q}$, nonempty (by density of $\mathbb{Q}$), and the sequence is nested with
$\operatorname{diam}F_n=2/n\to0$. But $\bigcap_nF_n=\varnothing$, because the only real point in the
intersection is $\sqrt2\notin\mathbb{Q}$. Thus the theorem fails without completeness. ∎
