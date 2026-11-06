# Functional Analysis — Exercises

> [Functional Analysis](README.md) · 38 problems · Beginner → Challenge · Solutions: [solutions.md](solutions.md)

Every problem asks for a proof unless it explicitly asks for a computation. A computation is complete only when the norm, the space, the operator and the theorem being applied are named, and when every hypothesis of that theorem has been checked. You may use anything proved in the [tutorial](README.md); results that the tutorial only quotes (Riesz–Fischer, Riesz–Markov–Kakutani, Banach–Alaoglu, Arzelà–Ascoli, the spectral radius formula) may be quoted but not reproved.

**Notation.** $X,Y$ are normed spaces over $\mathbb{F}\in\{\mathbb{R},\mathbb{C}\}$; $X^*$ is the dual; $\mathcal{B}(X,Y)$ is the space of bounded linear maps; $\mathcal{K}(X,Y)$ is the space of compact maps; $H$ is a Hilbert space with inner product linear in the first argument; $\ell^p$, $c_0$, $C[0,1]$, $L^p$ are as in §7.1; $e_n$ is the $n$-th standard basis vector; $E_n$ denotes an $n$-dimensional subspace when it appears; $D_n$ is the Dirichlet kernel; and $x_n\rightharpoonup x$ denotes weak convergence.

Do not open [solutions.md](solutions.md) before writing an attempt.

## Beginner

**1.** Let $X$ be a normed space.

(a) Prove the **reverse triangle inequality**: $\bigl\lvert\lVert x\rVert-\lVert y\rVert\bigr\rvert\le\lVert x-y\rVert$ for all $x,y\in X$.

(b) Deduce that $x\mapsto\lVert x\rVert$ is uniformly continuous.

(c) Verify in full that $d(x,y):=\lVert x-y\rVert$ is a metric on $X$, quoting the norm axioms used at each step.

**2.** On $\mathbb{R}^n$, prove the chain of inequalities
$$\lVert x\rVert_\infty\le\lVert x\rVert_2\le\lVert x\rVert_1\le\sqrt n\,\lVert x\rVert_2\le n\,\lVert x\rVert_\infty,$$
and show that each of the five constants $1,1,\sqrt n,\sqrt n,n$ is sharp, giving for each one a vector (or a sequence of vectors) for which equality holds.

**3.** Prove directly from the Cauchy–Schwarz inequality that $\lVert x\rVert_2$ satisfies the triangle inequality on $\mathbb{R}^2$, and determine exactly when equality holds.

**4.** For $0<p<1$ define $N_p(x):=\left(\sum_{k=1}^2\lvert x_k\rvert^p\right)^{1/p}$ on $\mathbb{R}^2$. Show by explicit example that $N_p$ fails the triangle inequality, and explain why this is consistent with the hypothesis $p\ge1$ in Minkowski's inequality.

**5.** Prove that $\ell^1\subseteq\ell^2$ and that $\lVert x\rVert_2\le\lVert x\rVert_1$ for $x\in\ell^1$. Show that the inclusion is proper. Is $\ell^2\subseteq\ell^1$? Justify your answer with a proof or a counterexample.

**6.** Compute the following operator norms, with proof of both the upper bound and its attainment (or non-attainment, as the case may be).

(a) $T:\mathbb{R}^2\to\mathbb{R}^2$, $T(x,y)=(2x-y,x+2y)$, with the Euclidean norm on both sides.

(b) The matrix $A=\begin{pmatrix}1&2\\3&4\end{pmatrix}$ acting on $\mathbb{R}^2$, with respect to $\lVert\cdot\rVert_\infty$ and with respect to $\lVert\cdot\rVert_1$.

(c) The evaluation functional $f\mapsto f(1/2)$ on $C[0,1]$ with the supremum norm.

(d) The right shift $S(x_1,x_2,\dots)=(0,x_1,x_2,\dots)$ on $\ell^p$ for $1\le p\le\infty$.

**7.** Let $D:C^1[0,1]\to C[0,1]$ be $Df:=f'$, with both spaces carrying the supremum norm.

(a) Prove that $D$ is unbounded, using the functions $f_n(t)=\sin(nt)$ or any other explicit family.

(b) Prove that for each fixed $n$, the restriction of $D$ to the space $P_n$ of polynomials of degree at most $n$ is bounded. You may use the finite-dimensional theorem, but state exactly which theorem and why its hypotheses hold.

**8.** Prove that $c_0$ is a closed subspace of $\ell^\infty$. Deduce that $c_0$ is a Banach space.

**9.** In $\ell^2$, let $e_n$ be the standard basis.

(a) Prove that $\lVert e_n-e_m\rVert_2=\sqrt2$ for $n\ne m$, and deduce that the closed unit ball of $\ell^2$ contains a sequence with no convergent subsequence.

(b) Deduce that neither the closed unit ball nor the unit sphere of $\ell^2$ is compact. Which theorem from the tutorial does this illustrate?

**10.** (a) Prove that every Cauchy sequence in a normed space is bounded.

(b) Prove that if $x_n\to x$ in a normed space, then $\lVert x_n\rVert\to\lVert x\rVert$.

(c) Give an example of a bounded sequence in a normed space that has no convergent subsequence, and explain why this does not contradict (a).

**11.** (a) Prove that in a Banach space, every absolutely convergent series converges: if $\sum_{n\ge1}\lVert x_n\rVert<\infty$, then $\sum_{n\ge1}x_n$ converges.

(b) Show that the space of real polynomials on $[0,1]$ with the supremum norm is not complete by exhibiting an absolutely convergent series of polynomials whose sum is not a polynomial.

**12.** For $a=(1,2,-2)$ let $f(x)=a_1x_1+a_2x_2+a_3x_3$ on $\mathbb{R}^3$. Compute $\lVert f\rVert$ when $\mathbb{R}^3$ carries $\lVert\cdot\rVert_1$, $\lVert\cdot\rVert_2$ and $\lVert\cdot\rVert_\infty$, and in each case exhibit a vector at which the norm is attained.

## Intermediate

**13.** Prove from the definitions that $\ell^p$ is complete for $1\le p<\infty$. Your proof should explicitly handle the three steps: coordinatewise convergence, membership of the limit in $\ell^p$, and norm convergence. Then indicate the changes needed for $p=\infty$.

**14.** Prove that $C[0,1]$ is not complete in the norm $\lVert f\rVert_1=\int_0^1\lvert f(t)\rvert\,dt$ by constructing a Cauchy sequence of continuous functions with no continuous limit. Show explicitly where the argument uses continuity of a putative limit.

**15.** (a) Prove that every finite-dimensional linear subspace of a normed space is closed.

(b) Show that $c_{00}:=\{x\in\ell^2 : x_k=0 \text{ for all sufficiently large }k\}$ is a linear subspace of $\ell^2$ that is not closed. Deduce that completeness is essential in (a).

**16.** On $C[0,1]$, compare the norms $\lVert f\rVert_\infty$ and $\lVert f\rVert_\star:=\lVert f\rVert_\infty+\lVert f\rVert_1$.

(a) Prove that they are equivalent, with explicit constants.

(b) Show that the constants you found are sharp.

(c) Prove that $\lVert\cdot\rVert_\infty$ and $\lVert\cdot\rVert_1$ are not equivalent.

**17.** Let $X$ be a normed space and $Y$ a Banach space. Prove that $\mathcal{B}(X,Y)$ with the operator norm is complete. Your proof must show that the pointwise limit of a Cauchy sequence of operators is linear, bounded, and the norm limit of the sequence.

**18.** Let $T:X\to Y$ be linear. Prove that the following are equivalent:

(a) $T$ is continuous on $X$;
(b) $T$ is continuous at $0$;
(c) $T$ is bounded;
(d) $T$ is Lipschitz;
(e) there is a ball $B(x_0,r)$ on which $T$ is bounded.

Show that the implication (c)⇒(a) uses linearity: the nonlinear map $h(t)=1$ for rational $t$ and $h(t)=0$ for irrational $t$ maps bounded sets to bounded sets but is discontinuous. Also show, with a nonlinear example, that continuity at a single point does not imply continuity everywhere.

**19.** Let $X$ be a Banach space and $T\in\mathcal{B}(X)$ with $\lVert T\rVert<1$.

(a) Prove that the Neumann series $\sum_{k=0}^\infty T^k$ converges in $\mathcal{B}(X)$.

(b) Prove that $I-T$ is invertible and that $(I-T)^{-1}=\sum_{k=0}^\infty T^k$ with $\lVert(I-T)^{-1}\rVert\le(1-\lVert T\rVert)^{-1}$.

(c) Show that the hypothesis $\lVert T\rVert<1$ is sufficient but not necessary: give an example with $\lVert T\rVert\ge1$ for which $I-T$ is invertible. Then prove that the weaker hypothesis "$\lVert T^n\rVert<1$ for some $n\ge1$" still implies that $I-T$ is invertible, and explain why the bound on the inverse in (b) must be replaced by a different one in that case.

**20.** (a) Prove that for every $x\ne0$ in a normed space $X$ there is $f\in X^*$ with $\lVert f\rVert=1$ and $f(x)=\lVert x\rVert$.

(b) Deduce that $\lVert x\rVert=\max_{\lVert f\rVert\le1}\lvert f(x)\rvert$ for every $x$, and that $X^*$ separates points.

(c) Prove that the canonical map $J:X\to X^{**}$, $(Jx)(f):=f(x)$, is a linear isometry.

**21.** Let $M$ be a closed subspace of a normed space $X$ and let $x\in X\setminus M$. Prove that
$$d(x,M)=\max\{\lvert f(x)\rvert : f\in X^*,\ \lVert f\rVert\le1,\ f|_M=0\},$$
including the assertion that the maximum is attained. Give an example in $C[0,1]$ where the maximum is attained by a functional that is not of the form $f\mapsto\int g f$.

**22.** This problem constructs a **Banach limit**.

(a) Let $p(x):=\limsup_{n\to\infty}\frac1n\sum_{k=1}^nx_k$ on $\ell^\infty(\mathbb{R})$. Prove that $p$ is sublinear.

(b) Let $M$ be the subspace of sequences for which $\frac1n\sum_{k=1}^nx_k$ converges, and let $f(x)$ be that limit. Prove that $f\le p$ on $M$, and extend $f$ to $L\in(\ell^\infty)^*$ with $L\le p$.

(c) Prove that $\lVert L\rVert\le1$, $L(\mathbf{1})=1$, $L(x)\ge0$ for $x\ge0$, and $L(Sx)=L(x)$ for the shift $S$.

(d) Prove that $L$ is not represented by any $y\in\ell^1$, i.e. there is no $y\in\ell^1$ with $L(x)=\sum x_ky_k$ for all $x\in\ell^\infty$.

**23.** Prove that $(\ell^1)^*$ is isometrically isomorphic to $\ell^\infty$. That is, show that every $y\in\ell^\infty$ defines a bounded functional $f_y(x)=\sum_kx_ky_k$ with $\lVert f_y\rVert=\lVert y\rVert_\infty$, and that every $f\in(\ell^1)^*$ arises in this way from a unique $y\in\ell^\infty$.

**24.** On $H=L^2[0,1]$ define
$$f(x):=\int_0^{1/2}x(t)\,dt-\int_{1/2}^1x(t)\,dt.$$
(a) Find $y\in H$ with $f(x)=\langle x,y\rangle$ for all $x\in H$, and compute $\lVert f\rVert$.

(b) Verify that Cauchy–Schwarz is an equality for $x=y$ and explain why this shows that the norm of $f$ is attained on the unit sphere.

(c) Prove that the representing vector is unique.

(d) Show that $y$ may be chosen discontinuous, and explain why this does not contradict the fact that $f$ is continuous on $L^2$.

## Advanced

**25.** Prove the projection theorem: if $M$ is a closed subspace of a Hilbert space $H$ and $x\in H$, then there is a unique $m_0\in M$ with $\lVert x-m_0\rVert=d(x,M)$; moreover $x-m_0\perp M$. Deduce that $H=M\oplus M^\perp$ and that the orthogonal projection $P_M$ is linear, bounded with norm $1$ (when $M\ne\{0\}$), idempotent and self-adjoint.

**26.** Let $\{e_\alpha\}_{\alpha\in A}$ be an orthonormal system in a Hilbert space $H$.

(a) Prove Bessel's inequality: $\sum_\alpha\lvert\langle x,e_\alpha\rangle\rvert^2\le\lVert x\rVert^2$ for every $x\in H$, where the sum is the supremum over finite subsets.

(b) Prove that equality holds if and only if $x\in\overline{\operatorname{span}}\{e_\alpha\}$.

(c) Deduce that at most countably many coefficients $\langle x,e_\alpha\rangle$ are nonzero.

**27.** Let $\{e_\alpha\}_{\alpha\in A}$ be an orthonormal system in a Hilbert space $H$. Prove that the following are equivalent:

(a) the system is maximal;
(b) its closed span is $H$;
(c) Parseval's identity $\lVert x\rVert^2=\sum_\alpha\lvert\langle x,e_\alpha\rangle\rvert^2$ holds for every $x$;
(d) $x=\sum_\alpha\langle x,e_\alpha\rangle e_\alpha$ for every $x$, in norm.

Deduce that every separable infinite-dimensional Hilbert space is isometrically isomorphic to $\ell^2$.

**28.** Let $X$ be a Banach space.

(a) Prove that $\mathcal{K}(X)$ is a linear subspace of $\mathcal{B}(X)$.

(b) Prove that it is a two-sided ideal: if $T\in\mathcal{K}(X)$ and $S\in\mathcal{B}(X)$, then $ST,TS\in\mathcal{K}(X)$.

(c) Prove that $\mathcal{K}(X)$ is closed in $\mathcal{B}(X)$.

(d) Deduce that a compact operator on an infinite-dimensional Banach space cannot be invertible.

(e) Give an example of a compact operator that is not of finite rank.

**29.** Let $k\in C([0,1]^2)$ and let $Tf(x)=\int_0^1k(x,t)f(t)\,dt$ on $C[0,1]$.

(a) Prove that $T$ is bounded with $\lVert T\rVert\le\sup_x\int_0^1\lvert k(x,t)\rvert\,dt$.

(b) Prove that $T$ is compact, using the Arzelà–Ascoli theorem. State precisely the hypotheses of the version you use, and verify each of them for the image of the unit ball.

(c) For $k(x,t)=\min(x,t)$, prove that $T$ is not of finite rank.

**30.** Let $(e_n)$ be an orthonormal basis of a Hilbert space $H$, let $(\lambda_n)$ be a bounded real sequence, and let $T$ be defined by $Tx=\sum_n\lambda_n\langle x,e_n\rangle e_n$.

(a) Prove that $T$ is bounded, self-adjoint, and that $\lVert T\rVert=\sup_n\lvert\lambda_n\rvert$.

(b) Prove that $T$ is compact if and only if $\lambda_n\to0$.

(c) Assuming $\lambda_n\to0$, determine $\sigma(T)$ and verify the conclusions of the spectral theorem: $T=\sum_n\lambda_nP_n$ in operator norm, $H=\ker T\oplus\overline{\operatorname{span}}\{e_n:\lambda_n\ne0\}$, and every nonzero eigenspace is finite-dimensional.

**31.** State and prove the Fredholm alternative for a compact self-adjoint operator $T$ on a Hilbert space $H$: for the equation $u-Tu=f$, either $I-T$ is bijective with bounded inverse, or $\ker(I-T)$ is a nonzero finite-dimensional space and the equation is solvable exactly when $f\perp\ker(I-T)$.

**32.** Prove the following facts about weak convergence in a normed space $X$.

(a) Weak limits are unique.

(b) Every weakly convergent sequence is bounded. (Use the uniform boundedness principle, and explain why it applies.)

(c) If $x_n\rightharpoonup x$, then $\lVert x\rVert\le\liminf_n\lVert x_n\rVert$.

(d) If $\dim X<\infty$, then weak convergence is equivalent to norm convergence.

(e) If $T\in\mathcal{K}(X,Y)$ and $x_n\rightharpoonup x$, then $Tx_n\to Tx$ in norm.

## Challenge

**33.** Assume the uniform boundedness principle. Let $C(\mathbb{T})$ be the space of continuous $2\pi$-periodic functions with the supremum norm, let
$$D_n(t)=\sum_{k=-n}^{n}e^{ikt}=\frac{\sin\bigl((n+\tfrac12)t\bigr)}{\sin(t/2)}$$
be the Dirichlet kernel, and let $S_nf(0)=\sum_{k=-n}^{n}\hat f(k)$ be the $n$-th symmetric partial sum of the Fourier series of $f$ at $0$.

(a) Prove that the functional $f\mapsto S_nf(0)$ is bounded and that its norm is $\lVert S_n\rVert=\frac{1}{2\pi}\int_{-\pi}^{\pi}\lvert D_n(t)\rvert\,dt$. (You may quote the Riesz–Markov–Kakutani theorem for the norm of a functional given by a measure.)

(b) Prove that $\lVert D_n\rVert_1\ge\frac{4}{\pi^2}\sum_{k=1}^{n}\frac{1}{k+1}\to\infty$.

(c) Deduce that there is a continuous $2\pi$-periodic $f$ whose Fourier series diverges at $0$. Explain precisely where the uniform boundedness principle is used.

**34.** Prove Schauder's theorem in the Hilbert case: if $T\in\mathcal{B}(H)$, then $T$ is compact if and only if $T^*$ is compact.

*Hint.* Show first that $T^*T$ is compact and self-adjoint when $T$ is compact, apply the spectral theorem to $T^*T$, and show that $T$ is the norm limit of finite-rank operators. For the converse apply the same argument to $T^*$ and use $T^{**}=T$.

**35.** Let $X$ be a Banach space. Prove that if $X^*$ is separable, then $X$ is separable.

*Hint.* Choose a countable dense sequence $(f_n)$ in $X^*$, choose $x_n$ with $\lVert x_n\rVert=1$ and $\lvert f_n(x_n)\rvert\ge\frac12\lVert f_n\rVert$, and show that the closed span of $(x_n)$ is $X$ by using Hahn–Banach.

**36.** Prove the Lax–Milgram theorem: let $H$ be a Hilbert space and $B:H\times H\to\mathbb{F}$ a sesquilinear form that is bounded, $\lvert B(u,v)\rvert\le M\lVert u\rVert\lVert v\rVert$, and coercive, $\lvert B(u,u)\rvert\ge c\lVert u\rVert^2$ with $c>0$. Then for every $f\in H^*$ there is a unique $u\in H$ with $B(u,v)=f(v)$ for all $v\in H$, and $\lVert u\rVert\le c^{-1}\lVert f\rVert$.

*Hint.* Represent $v\mapsto\overline{B(u,v)}$ by a vector $Au$, prove $A$ is bounded below, and show the range of $A$ is dense.

**37.** (a) Prove that the closed unit ball of $\ell^2$ is **weakly sequentially compact**: every sequence $(x^{(n)})$ with $\lVert x^{(n)}\rVert\le1$ has a subsequence converging weakly to some $x$ with $\lVert x\rVert\le1$. (Use a diagonal argument: choose a subsequence whose coordinates converge, then prove weak convergence using boundedness and truncation.)

(b) Prove that the closed unit ball of $\ell^2$ is not norm compact, by exhibiting a sequence of unit vectors with no norm-convergent subsequence.

(c) Explain why (a) and (b) are consistent, and why (a) does not follow from the compactness of the unit ball.

**38.** Let $k(x,t)=xt$ on $[0,1]^2$ and consider the integral equation
$$u(x)-\lambda\int_0^1xt\,u(t)\,dt=f(x),\qquad x\in[0,1],$$
with $f\in C[0,1]$ and $\lambda\in\mathbb{R}$.

(a) Show that the integral operator $Kf(x)=\int_0^1xt\,f(t)\,dt$ is compact, self-adjoint and of rank one, and find its nonzero eigenvalue and eigenfunction.

(b) Solve the equation explicitly for every real $\lambda$, identifying the exceptional value and the solvability condition.

(c) Reconcile the answer with the Fredholm alternative: describe $\ker(I-\lambda K)$ and $\operatorname{im}(I-\lambda K)$ at the exceptional value.
