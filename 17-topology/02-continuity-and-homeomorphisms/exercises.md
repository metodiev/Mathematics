# Continuity and Homeomorphisms — Exercises

> [Tutorial](README.md) · 36 problems · Levels: Beginner, Intermediate, Advanced, Challenge

Every problem asks for a proof unless it explicitly asks for a computation; for computations you must
justify each step by a theorem or definition. You may use any result proved in the
[tutorial](README.md) and in [Topological Spaces](../01-topological-spaces/README.md), together with the
standard facts of real analysis: the intermediate value theorem, the extreme value theorem, the density
of $\mathbb{Q}$ in $\mathbb{R}$, and the connectedness of intervals. Results about compactness may be
used in the form recorded in §5 and §7.6 of the tutorial.

Full solutions are in [solutions.md](solutions.md). Do not open that file until you have attempted the
problems.

## Beginner

**1.** Prove from the definition that $f : \mathbb{R}\to\mathbb{R}$, $f(x) = 3x-2$, is continuous, by
showing that $f^{-1}\big[(a,b)\big]$ is open for every open interval $(a,b)$.

**2.** Prove that (a) every constant map $X\to Y$ is continuous, (b) $\mathrm{id}_X : X\to X$ is
continuous, and (c) the inclusion $A\hookrightarrow X$ of a subspace is continuous.

**3.** Prove that $f : \mathbb{R}\to\mathbb{R}$, $f(x) = x^2$, is continuous using the closed-set
formulation: show that $f^{-1}[F]$ is closed for every closed $F\subseteq\mathbb{R}$.

**4.** (a) Prove that if $f : X\to Y$ is continuous then $f[\overline A]\subseteq\overline{f[A]}$ for every
$A\subseteq X$.
(b) Give an example of a continuous $f$ and a set $A$ for which the inclusion is strict.

**5.** (a) Prove that if $f : X\to Y$ is continuous then $f^{-1}[B^{\circ}]\subseteq\big(f^{-1}[B]\big)^{\circ}$
for every $B\subseteq Y$.
(b) Give an example in which the inclusion is strict.

**6.** Let $f : \mathbb{R}\to\mathbb{R}$ be $f(x) = 0$ for $x<1$ and $f(x) = 1$ for $x\ge1$. Determine
the set of points at which $f$ is continuous, and prove your answer.

**7.** Prove that (a) every map from a space into an indiscrete space is continuous, and (b) every map
from a discrete space into any space is continuous.

**8.** Let $\tau_1,\tau_2$ be topologies on a set $X$. Prove that $\mathrm{id} : (X,\tau_1)\to(X,\tau_2)$
is continuous if and only if $\tau_2\subseteq\tau_1$.

**9.** Prove directly (using complements, without quoting Theorem 7.1.1) that $f : X\to Y$ is continuous
if and only if $f^{-1}[F]$ is closed in $X$ for every closed $F\subseteq Y$.

**10.** Prove that $f : (0,1)\to(0,3)$, $f(x) = 3x$, is a homeomorphism.

## Intermediate

**11.** (a) Prove directly that $f : X\to Y$ is continuous if and only if $f[\overline A]\subseteq\overline{f[A]}$
for every $A\subseteq X$, using neither of the other formulations.
(b) Show that the condition fails for a suitable discontinuous map and a suitable set $A$.

**12.** Prove that continuity may be tested on a base and on a subbase: if $\mathcal{B}$ is a base for the
topology of $Y$, or $\mathcal{S}$ is a subbase with $\bigcup\mathcal{S} = Y$, then $f$ is continuous iff
$f^{-1}[B]$ is open for every $B\in\mathcal{B}$ (respectively every $S\in\mathcal{S}$).

**13.** Prove that the following are equivalent for $f : X\to Y$ and $x_0\in X$:
(i) for every neighbourhood $V$ of $f(x_0)$ there is a neighbourhood $U$ of $x_0$ with $f[U]\subseteq V$;
(ii) for every open $V$ containing $f(x_0)$ there is an open $U$ containing $x_0$ with $f[U]\subseteq V$;
(iii) for every basic open $V$ containing $f(x_0)$ (with respect to a fixed base of $Y$) there is an open
$U$ containing $x_0$ with $f[U]\subseteq V$. Deduce that $f$ is continuous iff it is continuous at every
point.

**14.** (a) Prove that $f : X\to Y$ is continuous if and only if $\overline{f^{-1}[B]}\subseteq f^{-1}[\overline B]$
for every $B\subseteq Y$.
(b) Give an example in which the inclusion is strict for a continuous $f$.

**15.** Prove the pasting lemma for a finite closed cover: if $X = A\cup B$ with $A,B$ closed and
$f|_A$, $f|_B$ continuous, then $f$ is continuous. Include a proof that a set closed in the closed
subspace $A$ is closed in $X$.

**16.** (a) Prove the pasting lemma for an arbitrary open cover.
(b) Show that the closed version fails for a countable closed cover by constructing a counterexample.

**17.** Let $f : X\to Y$ be a continuous bijection. Prove that the following are equivalent:
(i) $f$ is a homeomorphism; (ii) $f$ is an open map; (iii) $f$ is a closed map.

**18.** (a) Prove that a continuous injection from a compact space into a Hausdorff space is an
embedding.
(b) Show that both hypotheses are needed.

**19.** Using topological invariants, prove that (a) $[0,1)$ is not homeomorphic to $S^1$;
(b) $[0,1)$ is not homeomorphic to $[0,1]$; (c) $\mathbb{R}$ is not homeomorphic to $[0,1]$;
(d) $\mathbb{N}$ (with the subspace topology) is not homeomorphic to $\mathbb{Q}$.

**20.** (a) Prove that the order topology on $\mathbb{R}$ is the usual topology.
(b) Determine the order topology on $\mathbb{Z}$ and on $\mathbb{Q}$, with proof.

**21.** State and prove the characteristic property of the initial topology of a family of maps
$f_i : X\to Y_i$: a map $g : Z\to X$ is continuous if and only if every $f_i\circ g$ is continuous.

## Advanced

**22.** (a) Prove that a continuous bijection from a compact space onto a Hausdorff space is a
homeomorphism, including full proofs of the three lemmas used.
(b) Show by example that neither hypothesis can be dropped.

**23.** Prove that $\mathbb{R}$ and $\mathbb{R}^2$ are not homeomorphic. *(Use cut points: removing one
point from $\mathbb{R}$ disconnects it, while $\mathbb{R}^2$ minus a point is path-connected.)*

**24.** Let $f : X\to Y$ be continuous with $Y$ Hausdorff, and let $\Gamma_f = \{(x,f(x)) : x\in X\}$.
(a) Prove that $\Gamma_f$ is closed in $X\times Y$.
(b) Prove that $\Gamma_f$ is homeomorphic to $X$.
(c) Show that the converse of (a) fails: exhibit a discontinuous $f : \mathbb{R}\to\mathbb{R}$ with closed
graph.

**25.** (a) Prove that the continuous image of a connected space is connected, and that the continuous
image of a path-connected space is path-connected.
(b) Deduce the intermediate value theorem for a continuous $f : [a,b]\to\mathbb{R}$.

**26.** (a) Prove that if $f,g : X\to Y$ are continuous, $Y$ is Hausdorff, and $f = g$ on a dense subset
$D$, then $f = g$.
(b) Show that the Hausdorff hypothesis is needed, using the Sierpiński space.

**27.** Prove that every continuous bijection $f : \mathbb{R}\to\mathbb{R}$ is a homeomorphism.

**28.** (a) Prove that $S^1\setminus\{1\}$ is homeomorphic to $\mathbb{R}$.
(b) Prove that $S^1$ has no cut points, and deduce that $[0,1]$ is not homeomorphic to $S^1$.

**29.** Let $q : S^1\to S^1$ be $q(z) = z^2$. Prove that the quotient $S^1/{\sim}$, where $z\sim -z$, is
homeomorphic to $S^1$; that is, $\mathbb{RP}^1\cong S^1$.

**30.** Prove that a topology satisfying the characteristic property of the initial topology is unique:
if $\tau$ and $\tau'$ are topologies on $X$ such that for every space $Z$ and map $g : Z\to X$, $g$ is
$\tau$-continuous iff every $f_i\circ g$ is continuous, and similarly for $\tau'$, then $\tau = \tau'$.

**31.** Prove the pasting lemma for a locally finite closed cover: if $\{F_i\}_{i\in I}$ is a locally
finite family of closed subsets of $X$ with $X = \bigcup_i F_i$, and every $f|_{F_i}$ is continuous, then
$f$ is continuous.

## Challenge

**32.** A linear order is *dense* if between any two elements there is a third, and *without endpoints* if
it has neither a least nor a greatest element. Prove that any two countable dense linear orders without
endpoints are order-isomorphic. *(Use the back-and-forth construction, alternating between the two
orders.)* Deduce that any two countable dense subsets of $\mathbb{R}$ without endpoints are homeomorphic
in their order topologies.

**33.** Prove the extreme value theorem topologically: if $X$ is compact and $f : X\to\mathbb{R}$ is
continuous, then $f$ is bounded and attains a maximum and a minimum. *(Show that $f[X]$ is compact, that a
compact subset of $\mathbb{R}$ is bounded and closed, and use the completeness of $\mathbb{R}$.)*

**34.** A space $X$ is *homogeneous* if for all $p,q\in X$ there is a homeomorphism $h : X\to X$ with
$h(p) = q$. (a) Prove that $\mathbb{R}$, $S^1$ and $\mathbb{Q}$ are homogeneous.
(b) Prove that $[0,1]$ is not homogeneous.
(c) Prove that a connected $1$-manifold without boundary is homogeneous.

**35.** Prove that there is no continuous injection $S^1\to\mathbb{R}$. *(Use the fact that a continuous
injection from a compact space into a Hausdorff space is an embedding, that a compact connected subset of
$\mathbb{R}$ is a closed interval, and that $S^1$ has no cut points.)*

**36.** Let $C[0,1]$ carry the topology of pointwise convergence, that is, the initial topology with
respect to the evaluation maps $\mathrm{ev}_t$, $t\in[0,1]$. Prove that this topology is not first
countable, and deduce that it is not metrisable.
