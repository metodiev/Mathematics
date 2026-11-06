# Metric Spaces — Exercises

> [Metric Spaces](README.md) · 36 problems · Beginner → Challenge · Solutions: [solutions.md](solutions.md)

Every problem is a proof unless it asks for a computation or a description. "Describe the balls" means:
give the set $B_r(x)$ explicitly for each range of $r$. You may use anything proved in the
[tutorial](README.md), but not results from later topics. Do not open [solutions.md](solutions.md) before
writing an attempt.

Notation: $(X,d)$ is a metric space, $B_r(x)$ is the open ball, $\overline A$, $A^{\circ}$ and $\partial A$
are the closure, interior and boundary, $A'$ is the derived set, and $\mathcal{T}$ is the family of open
sets. $C[a,b]$ is the space of continuous real functions on $[a,b]$.

## Beginner

**1.** *(§7.2)* Let $X = \mathbb{R}$ and $d(x,y) = 3\lvert x - y\rvert$. Verify that $d$ is a metric.
Describe $B_r(x)$ for $r>0$, and decide whether $d$ and the usual metric $\lvert x-y\rvert$ are Lipschitz
equivalent.

**2.** *(§7.2)* On $\mathbb{R}^2$ let $d_1(x,y) = \lvert x_1-y_1\rvert + \lvert x_2-y_2\rvert$. Prove the
triangle inequality directly (do not cite Minkowski), and sketch or describe $B_1((0,0))$.

**3.** *(§7.2)* On $\mathbb{R}^2$ let $d_\infty(x,y) = \max\{\lvert x_1-y_1\rvert,\lvert x_2-y_2\rvert\}$.
Prove that $d_\infty$ is a metric, prove $d_\infty \le d_2 \le \sqrt2\,d_\infty$, and describe
$B_1((0,0))$.

**4.** *(§7.2, §7.3)* Let $X = \{a,b,c\}$ with the discrete metric. List every open ball, every open set and
every closed set. Which subsets are clopen?

**5.** *(§7.3, §7.4)* In $\mathbb{R}$ with the usual metric, decide for each of the following whether it is
open, closed, both or neither, and justify with balls: $(0,1)$; $[0,1]$; $[0,1)$; $\{1/n : n\in\mathbb{N}\}$;
$\mathbb{Z}$; $\mathbb{Q}$; $\mathbb{R}\setminus\mathbb{Q}$.

**6.** *(§7.2, §7.3)* Let $X = [0,1]\cup\{2\}$ with the metric induced from $\mathbb{R}$. Prove that $[0,1]$
is open in $X$ and that $\{2\}$ is open in $X$. Are they open in $\mathbb{R}$?

**7.** *(§7.3, §7.4)* Let $X = [0,1]\cup\{2\}$ with the metric induced from $\mathbb{R}$. Compute
$B_1(1)$, its closure in $X$, and the closed ball $\overline{B}_1(1)$. Deduce that the closure of an open
ball need not equal the closed ball of the same radius.

**8.** *(§7.6)* Prove that in a metric space limits are unique: if $x_n\to x$ and $x_n\to y$, then $x=y$.
Also prove that every subsequence of a convergent sequence converges to the same limit.

**9.** *(§7.5)* Prove that $A\subseteq B$ implies $\overline A\subseteq\overline B$ and
$A^{\circ}\subseteq B^{\circ}$.

**10.** *(§7.5)* Compute $\partial(a,b)$, $\partial[a,b]$, $\partial\mathbb{Q}$ and
$\partial\{1/n : n\in\mathbb{N}\}$ in $\mathbb{R}$.

**11.** *(§7.5)* Let $A = \{1/n : n\in\mathbb{N}\}\cup\{0\}\subseteq\mathbb{R}$. Compute $A^{\circ}$,
$\overline A$, $A'$ and $\partial A$.

**12.** *(§7.8, §7.10)* Prove that a finite union of bounded subsets of a metric space is bounded. Give an
example of a bounded metric space that is not totally bounded, and prove that it is not.

## Intermediate

**13.** *(§7.3, §7.4)* Prove that an arbitrary union of open sets is open and that an arbitrary
intersection of closed sets is closed. Give an explicit example in $\mathbb{R}$ of a countable intersection
of open sets that is not open, and of a countable union of closed sets that is not closed.

**14.** *(§7.5)* Prove $\overline{A\cup B} = \overline A\cup\overline B$ and
$(A\cup B)^{\circ}\supseteq A^{\circ}\cup B^{\circ}$. Give an example in $\mathbb{R}$ where the inclusion
is strict.

**15.** *(§7.5)* Prove $\overline{A\cap B}\subseteq \overline A\cap\overline B$ and
$(A\cap B)^{\circ} = A^{\circ}\cap B^{\circ}$. Give an example in $\mathbb{R}$ where the first inclusion is
strict.

**16.** *(§7.5)* Prove that $\partial A = \overline A\cap\overline{X\setminus A}$ is closed and that
$\partial A = \partial(X\setminus A)$. Decide, with proof or counterexample, whether $A\subseteq B$ with $B$
open implies $\partial A\subseteq\partial B$.

**17.** *(§7.4, §7.6)* Prove that $A$ is closed if and only if $A$ contains all its limit points, and that
$A$ is open if and only if $X\setminus A$ is closed.

**18.** *(§7.6)* Prove that $x$ is a limit point of $A$ if and only if every ball $B_r(x)$ contains
infinitely many points of $A$.

**19.** *(§7.7)* Define $f:\mathbb{R}\to\mathbb{R}$ by $f(x) = 0$ if $x\in\mathbb{Q}$ and $f(x) = x$ if
$x\notin\mathbb{Q}$. Prove that $f$ is continuous at $0$ and at no other point, using the sequential
characterisation of continuity.

**20.** *(§7.2, §7.7)* Let $A\subseteq X$ carry the subspace metric and let $i:A\to X$ be the inclusion.
Prove that $i$ is continuous, and prove that a set $U\subseteq A$ that is open in $A$ need not be open in
$X$. State and prove the precise relationship between the two notions of openness.

**21.** *(§7.7)* Let $f,g:X\to\mathbb{R}$ be continuous. Prove that $f+g$ and $fg$ are continuous, using the
sequential characterisation, and deduce that the zero set $\{x : f(x)=0\}$ is closed.

**22.** *(§7.7)* Prove that an isometry is injective and that its inverse (on its image) is an isometry.
Give an example of a continuous bijection between metric spaces whose inverse is not continuous.

**23.** *(§7.8)* Let $(x_n)$ and $(y_n)$ be Cauchy sequences in a metric space. Prove that the real sequence
$d(x_n,y_n)$ converges.

**24.** *(§7.8)* Let $(X,d)$ be complete and $A\subseteq X$. Prove that $(A,d)$ is complete if and only if
$A$ is closed in $X$.

## Advanced

**25.** *(§7.9)* Prove the Baire category theorem: in a complete nonempty metric space, the intersection of
countably many open dense sets is dense. Give all details of the nested-balls construction and of the
passage to the limit.

**26.** *(§7.9)* Using the Baire category theorem, prove that $\mathbb{Q}$ is not a countable intersection
of open subsets of $\mathbb{R}$. Deduce that $\mathbb{R}\setminus\mathbb{Q}$ is not a countable union of
closed subsets of $\mathbb{R}$.

**27.** *(§7.10)* Prove in detail that a compact metric space is sequentially compact. Then exhibit a
bounded, closed subset of a metric space that is not compact, and prove that it is not compact.

**28.** *(§7.10)* State and prove the Lebesgue number lemma for a sequentially compact metric space, and use
it to prove that a sequentially compact metric space is compact.

**29.** *(§7.10)* Prove that a complete, totally bounded metric space is sequentially compact, by the
diagonal subsequence argument.

**30.** *(§7.11)* Prove the contraction mapping principle, including both error estimates. Then apply it to
$T(x) = 1 + \tfrac12\sin x$ on $\mathbb{R}$: prove that $T$ has a unique fixed point, compute three Picard
iterates from $x_0 = 1$, and bound the error of the third iterate.

**31.** *(§7.12)* Prove that $\mathbb{R}$ is connected, and deduce the intermediate value theorem. Prove
that $\mathbb{Q}$ is totally disconnected: its only connected subsets are single points.

## Challenge

**32.** *(§7.12)* Let $S = \{(x,\sin(1/x)) : 0<x\le1\}\cup(\{0\}\times[-1,1])\subseteq\mathbb{R}^2$. Prove
that $S$ is connected and that $S$ is not path-connected.

**33.** *(§7.8)* Prove that $C[0,1]$ with the metric $d_1(f,g) = \int_0^1\lvert f-g\rvert$ is not complete,
by constructing a Cauchy sequence of continuous functions with no continuous limit.

**34.** *(§7.10)* Prove that a metric space $X$ is compact if and only if every family of closed subsets of
$X$ with the finite intersection property has nonempty intersection. (A family $\mathcal{F}$ has the
*finite intersection property* if every finite subfamily has nonempty intersection.)

**35.** *(§7.8)* Prove that every metric space $(X,d)$ embeds isometrically into a complete metric space.
(Construct the completion from equivalence classes of Cauchy sequences; you may use without proof that the
relation "$\lim_n d(x_n,y_n) = 0$" is an equivalence relation on Cauchy sequences, but you must prove that
the distance is well defined.)

**36.** *(§7.11)* Let $(X,d)$ be complete and nonempty and let $T:X\to X$ be continuous. Suppose that some
iterate $T^n = T\circ\cdots\circ T$ ($n$ times) is a contraction. Prove that $T$ has exactly one fixed
point, and that it is the limit of the iterates $T^k(x_0)$ for every $x_0\in X$. Show by example that $T$
itself need not be a contraction.
