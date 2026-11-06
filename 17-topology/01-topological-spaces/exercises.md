# Topological Spaces — Exercises

> [Tutorial](README.md) · 36 problems · Levels: Beginner, Intermediate, Advanced, Challenge

Every problem asks for a proof unless it explicitly asks for a computation; for computations you must
also justify the answer, quoting the theorem or definition used at each step. You may use any result
proved in the [tutorial](README.md), including the worked examples, and the standard facts about
$\mathbb{R}$: the density of $\mathbb{Q}$, the uncountability of any nonempty open interval, and the
fact that a nonzero polynomial in one variable has finitely many roots.

The phrase *"prove from the definition"* means: do not cite the general theorem, but reproduce its
argument in the special case.

Full solutions are in [solutions.md](solutions.md). Do not open that file until you have attempted the
problems.

## Beginner

**1.** Let $X = \{a,b,c\}$ and $\tau = \big\{\varnothing,\{a\},\{b\},\{a,b\},X\big\}$.
(a) Verify that $\tau$ is a topology on $X$.
(b) List all closed subsets of $X$.
(c) Compute $\overline{\{c\}}$, $\{c\}^{\circ}$ and $\partial\{c\}$.
(d) Compute $\overline{\{a\}}$ and $\{a,b\}^{\circ}$.
(e) Decide whether $(X,\tau)$ satisfies $T_0$, and whether it satisfies $T_1$.

**2.** Let $X$ be a set, $p\in X$, and
$$
\tau_p = \{\varnothing\}\cup\{U\subseteq X : p\in U\}.
$$
(a) Prove that $\tau_p$ is a topology (the *particular point topology*).
(b) Describe the closed sets and compute $\overline{\{p\}}$ and $\overline{\{x\}}$ for $x\ne p$.
(c) Prove that if $\lvert X\rvert\ge2$ then $(X,\tau_p)$ is $T_0$ but not $T_1$, and identify the point that fails to be closed.

**3.** (a) Prove that in any topological space $\varnothing$ and $X$ are closed.
(b) Prove that the intersection of an arbitrary family of closed sets is closed and that the union of
finitely many closed sets is closed.
(c) Give an example in $\mathbb{R}$ (usual topology) of a countable union of closed sets that is not
closed, and an example of a countable intersection of open sets that is not open.

**4.** Let $X$ be a set and
$$
\tau_{\mathrm{cof}} = \{\varnothing\}\cup\{U\subseteq X : X\setminus U \text{ is finite}\}.
$$
(a) Prove that $\tau_{\mathrm{cof}}$ is a topology.
(b) Describe the closed sets and prove that the space is $T_1$.
(c) Prove that if $X$ is infinite then every nonempty open set is infinite.

**5.** (a) Prove that the discrete topology is the finest topology on a set $X$ and the indiscrete
topology the coarsest.
(b) Prove that a topological space is discrete if and only if every singleton subset is open.

**6.** Let $\tau_1$ and $\tau_2$ be topologies on the same set $X$.
(a) Prove that $\tau_1\cap\tau_2$ is a topology on $X$.
(b) Show by example that $\tau_1\cup\tau_2$ need not be a topology.

**7.** In $\mathbb{R}$ with the usual topology compute $\overline A$, $A^{\circ}$, $\partial A$ and
$A'$ for
(a) $A = (0,1)$; (b) $A = \mathbb{Q}$; (c) $A = \{1/n : n\in\mathbb{N}\}$; (d) $A = [0,1]\cup\{2\}$.
Justify each answer from Definition 5.8 and Definition 5.9.

**8.** Let $A\subseteq X$ and $x\in X$. Prove that $x\in\overline A$ if and only if every neighbourhood
of $x$ meets $A$. Deduce that if $\mathcal{B}_x$ is a neighbourhood base at $x$, then $x\in\overline A$
if and only if $B\cap A\ne\varnothing$ for every $B\in\mathcal{B}_x$.

**9.** Prove that $F\subseteq X$ is closed if and only if $F'\subseteq F$, where $F'$ is the derived set
of $F$.

**10.** (a) Prove that in a $T_1$ space every finite set is closed.
(b) Deduce that a finite $T_1$ space is discrete.

## Intermediate

**11.** Prove the base criterion in both directions: a family $\mathcal{B}\subseteq\mathcal{P}(X)$ is a
base for some topology on $X$ if and only if (B1) $\bigcup\mathcal{B} = X$ and (B2) for all
$B_1,B_2\in\mathcal{B}$ and all $x\in B_1\cap B_2$ there is $B_3\in\mathcal{B}$ with
$x\in B_3\subseteq B_1\cap B_2$. Show also that the topology is then unique.

**12.** Let $\mathcal{S}\subseteq\mathcal{P}(X)$ with $\bigcup\mathcal{S} = X$. Prove that the family of
all finite intersections of members of $\mathcal{S}$ is a base for a topology, and that this topology is
the coarsest topology containing $\mathcal{S}$. Give an example showing that the hypothesis
$\bigcup\mathcal{S} = X$ cannot be dropped.

**13.** On $\mathbb{R}$ let $\mathcal{B} = \{[a,b) : a<b\}$.
(a) Prove that $\mathcal{B}$ is a base for a topology $\tau_\ell$, the Sorgenfrey topology.
(b) Prove that every usual-open set is $\tau_\ell$-open, and that the inclusion is strict.
(c) Prove that $[a,b)$ is closed in $\tau_\ell$.
(d) Prove that $\mathbb{R}_\ell$ is not discrete.

**14.** Let $A\subseteq X$ with inclusion $i : A\to X$, and let $\tau_A = \{U\cap A : U\in\tau\}$.
(a) Prove that $\tau_A$ is a topology on $A$.
(b) Prove that $i$ is continuous and that $\tau_A$ is the coarsest topology on $A$ with this property.
(c) Prove that for every space $Z$ and every $f : Z\to A$, $f$ is continuous if and only if
$i\circ f$ is continuous.

**15.** Let $A$ be a subspace of $X$.
(a) Prove that if $\mathcal{B}$ is a base for $X$ then $\{B\cap A : B\in\mathcal{B}\}$ is a base for $A$.
(b) Deduce that every subspace of a second-countable space is second countable.
(c) Prove that the closed subsets of $A$ are exactly the sets $F\cap A$ with $F$ closed in $X$.

**16.** Let $\{(X_i,\tau_i)\}_{i\in I}$ be spaces and $P = \prod_{i\in I}X_i$.
(a) Prove that the family of all products $\prod_i U_i$ with $U_i\in\tau_i$ and $U_i = X_i$ for all but
finitely many $i$ is a base for a topology on $P$.
(b) Prove that this topology is the coarsest making every projection $\pi_j$ continuous.
(c) Prove the characteristic property in the case of a finite index set: $f : Z\to P$ is continuous if
and only if every $\pi_j\circ f$ is continuous.

**17.** (a) Prove that every projection $\pi_j : \prod_{i\in I}X_i\to X_j$ is an open map.
(b) Give an example of a projection that is not a closed map.

**18.** Prove that (a) every subspace of a Hausdorff space is Hausdorff, (b) every product of Hausdorff
spaces is Hausdorff, and (c) every subspace of a $T_1$ space is $T_1$.

**19.** Let $c : \mathcal{P}(X)\to\mathcal{P}(X)$ satisfy (K1) $c(\varnothing) = \varnothing$,
(K2) $A\subseteq c(A)$, (K3) $c(c(A)) = c(A)$ and (K4) $c(A\cup B) = c(A)\cup c(B)$ for all
$A,B\subseteq X$. Prove that $\mathcal{F} = \{A : c(A) = A\}$ satisfies (C1)–(C3), and that in the
resulting topology the closure of $A$ is exactly $c(A)$.

**20.** Let $A\subseteq X$. Prove that
$$
\overline A = A\cup\partial A, \qquad A^{\circ} = A\setminus\partial A, \qquad
X = A^{\circ}\ \sqcup\ \partial A\ \sqcup\ (X\setminus\overline A),
$$
and deduce that $A$ is clopen if and only if $\partial A = \varnothing$.

**21.** (a) Prove that $\mathbb{Q}$ is dense in $\mathbb{R}$ and that $\mathbb{Q}^2$ is dense in
$\mathbb{R}^2$.
(b) Prove that if $D$ is dense in $X$ and $A\subseteq X$, then $D\cap A$ is dense in the subspace $A$;
give an example showing that $D\cap A$ need not be dense in $X$.
(c) Deduce that every subspace of a separable space is separable.

**22.** Let $\mathcal{N}(x)$ be the neighbourhood system of a point $x$ in a topological space.
(a) Prove (N1)–(N4) of Theorem 7.3.1 for $\mathcal{N}(x)$.
(b) Prove that $U\subseteq X$ is open if and only if $U\in\mathcal{N}(x)$ for every $x\in U$.
(c) Show by example that the intersection of infinitely many neighbourhoods of $x$ need not be a
neighbourhood of $x$.

## Advanced

**23.** Let $q : X\to Y$ be a quotient map.
(a) Prove the characteristic property: for every space $Z$ and every $f : Y\to Z$, $f$ is continuous if
and only if $f\circ q$ is continuous.
(b) Prove that $q$ is an open map if and only if $q^{-1}[q[U]]$ is open for every open $U\subseteq X$
(that is, if and only if it maps saturated open sets to open sets).
(c) Show that a quotient map need not be open, and need not be closed.

**24.** (a) Prove that $\mathbb{R}_\ell$ is separable.
(b) Prove that $\mathbb{R}_\ell$ has no countable base.
(c) Prove that a separable metric space is second countable.
(d) Deduce that the Sorgenfrey line is not metrisable.

**25.** Let $K = \{1/n : n\in\mathbb{N}\}$ and let $\mathbb{R}_K$ be $\mathbb{R}$ with the topology
generated by the base $\{(a,b)\}\cup\{(a,b)\setminus K\}$.
(a) Prove that $\mathbb{R}_K$ is finer than the usual topology and hence Hausdorff.
(b) Prove that $K$ is closed in $\mathbb{R}_K$ and that $0\notin K$.
(c) Prove that no open set containing $0$ is disjoint from any open set containing $K$. Conclude that
$\mathbb{R}_K$ is not regular.

**26.** Let $(X,d)$ be a metric space and $A\ne\varnothing$ a subset. Put
$d(x,A) = \inf\{d(x,a) : a\in A\}$.
(a) Prove that $\lvert d(x,A) - d(y,A)\rvert\le d(x,y)$.
(b) Prove that $d(x,A) = 0$ if and only if $x\in\overline A$.
(c) Prove that $X$ is normal: given disjoint closed $F,G$, show that
$U = \{x : d(x,F) < d(x,G)\}$ and $V = \{x : d(x,G) < d(x,F)\}$ are disjoint open sets with
$F\subseteq U$ and $G\subseteq V$. (Handle the case $F = \varnothing$ separately.)
(d) Deduce that every metrisable space is $T_1$ and $T_4$.

**27.** (a) Prove that in a Hausdorff space a sequence has at most one limit.
(b) Prove that in the cofinite topology on $\mathbb{N}$ the sequence $x_n = n$ converges to every point.
(c) Give an example of a space in which some sequence converges to exactly two distinct points.

**28.** (a) Prove that a space is $T_1$ if and only if every singleton is closed.
(b) Prove that $T_2\Rightarrow T_1\Rightarrow T_0$.
(c) Prove that $T_3\Rightarrow T_2$ and $T_4\Rightarrow T_3$, carefully using the convention of
Definition 7.11.1 in which regularity and normality include $T_1$.

**29.** Let $\tau_Z$ be the Zariski topology on $\mathbb{R}^2$, whose closed sets are the sets
$V(S) = \{p : f(p) = 0 \text{ for all } f\in S\}$.
(a) Prove that the family $\{V(S)\}$ satisfies (C1)–(C3), hence defines a topology.
(b) Prove that $(\mathbb{R}^2,\tau_Z)$ is $T_1$.
(c) Prove that any two nonempty $\tau_Z$-open sets intersect, and deduce that the space is not
Hausdorff.

**30.** Let $D : \mathbb{R}\to\mathbb{R}^{\mathbb{N}}$ be the diagonal map $D(t) = (t,t,t,\dots)$, where
$\mathbb{R}^{\mathbb{N}}$ carries either the product topology or the box topology.
(a) Prove that $D$ is continuous for the product topology.
(b) Prove that $D$ is not continuous for the box topology.
(c) Deduce that the box topology is strictly finer than the product topology when the index set is
infinite.

**31.** Let $X = \mathbb{R}\times\{0,1\}$ (with $\{0,1\}$ discrete) and let $Y = X/{\sim}$ where
$(x,0)\sim(x,1)$ for $x\ne0$. Prove that $Y$ is $T_1$, is not Hausdorff, and is not metrisable.

## Challenge

**32.** (a) Prove that if $X$ is second countable and $\mathcal{C}$ is *any* base for $X$, then
$\mathcal{C}$ contains a countable subfamily that is still a base. *(Hint: enumerate a countable base
$\{B_n\}$ and, for each pair $(n,m)$ with $B_n\subseteq B_m$, choose one member of $\mathcal{C}$ between
them.)*
(b) Deduce that a second-countable space has at most $2^{\aleph_0}$ open sets.

**33.** Prove that for a topological space $X$ the following are equivalent:
(i) $X$ is Hausdorff;
(ii) the diagonal $\Delta_X = \{(x,x) : x\in X\}$ is closed in $X\times X$;
(iii) for every space $Y$ and every pair of continuous maps $f,g : Y\to X$, the *equaliser*
$E = \{y\in Y : f(y) = g(y)\}$ is closed in $Y$.

**34.** (Finite spaces and preorders.) Let $X$ be a finite set and $\tau$ a topology on it. Define
$x\preceq y$ if and only if $x\in\overline{\{y\}}$.
(a) Prove that $\preceq$ is a preorder (reflexive and transitive).
(b) Prove that $\tau$ is $T_0$ if and only if $\preceq$ is antisymmetric, i.e. a partial order.
(c) Prove that in a finite space every intersection of open sets is open (such spaces are called
*Alexandrov*), that every open set $U$ is an *up-set* for $\preceq$ (if $x\in U$ and $x\preceq y$ then
$y\in U$), and that $\{x : y\preceq x\}$ is the smallest open set containing $y$.
(d) Prove that $\tau$ is determined by $\preceq$. Conversely, prove that for every preorder on a finite
set the up-sets form a topology whose specialisation order is the given preorder. Deduce that
topologies on a finite set are in bijection with preorders on it.

**35.** (a) Prove that a countable product of metrisable spaces is metrisable. *(Hint: on
$\prod_n X_n$ with bounded metrics $d_n\le1$, consider $d(x,y) = \sum_n 2^{-n}d_n(x_n,y_n)$ and show
that it induces the product topology.)*
(b) Prove that $\mathbb{R}^I$ with the product topology is not first countable when $I$ is uncountable,
and deduce that it is not metrisable.

**36.** Let $X$ be uncountable with the co-countable topology: $U$ is open if $U = \varnothing$ or
$X\setminus U$ is countable.
(a) Prove that $X$ is not first countable.
(b) Determine exactly which sequences in $X$ converge, and to which points. *(Show: if the range of the
sequence is infinite then it converges to every point of $X$, and if the range is finite then it
converges to $x$ if and only if it is eventually equal to $x$.)*
(c) Deduce that a countably infinite $A\subseteq X$ is closed, yet there is a sequence in $A$ converging to
every point of $X$. Conclude that a limit of a sequence from $A$ need not lie in $\overline A$, so the
sequential description of the closure fails in this direction as well (compare Remark 7.9.6, where it
fails in the other direction).
