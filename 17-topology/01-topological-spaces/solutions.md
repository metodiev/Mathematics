# Topological Spaces — Solutions

> [Tutorial](README.md) · [Exercises](exercises.md) · 36 complete solutions

Every solution below is complete: the construction is motivated before it is used, every theorem is
named when it is applied, and all quantifiers are displayed where they matter. Where a problem admits a
second natural approach, the alternative is indicated at the end.

## Beginner

### Solution 1

**(a)** With $\tau = \{\varnothing,\{a\},\{b\},\{a,b\},X\}$: (O1) holds because $\varnothing$ and $X$ are
listed. For (O2), let $\{U_i\}_{i\in I}\subseteq\tau$. If $X$ is among the $U_i$ the union is $X\in\tau$.
Otherwise every $U_i$ is a subset of $\{a,b\}$, so the union is also a subset of $\{a,b\}$; it is
determined by which of $a,b$ belong to it, hence it is one of $\varnothing,\{a\},\{b\},\{a,b\}$, all of
which lie in $\tau$. For (O3) check the pairs: intersections involving $\varnothing$ or $X$ are trivial,
$\{a\}\cap\{b\} = \varnothing$, $\{a\}\cap\{a,b\} = \{a\}$ and $\{b\}\cap\{a,b\} = \{b\}$, all in $\tau$.

**(b)** Taking complements: $X\setminus X = \varnothing$, $X\setminus\varnothing = X$,
$X\setminus\{a\} = \{b,c\}$, $X\setminus\{b\} = \{a,c\}$, $X\setminus\{a,b\} = \{c\}$. So the closed sets
are $\varnothing,\{c\},\{b,c\},\{a,c\},X$.

**(c)** The closed supersets of $\{c\}$ are $\{c\},\{b,c\},\{a,c\},X$, the smallest of which is $\{c\}$;
so $\overline{\{c\}} = \{c\}$, consistent with $\{c\}$ being closed. The open subsets of $\{c\}$ are only
$\varnothing$ (none of $\{a\},\{b\},\{a,b\}$ is contained in $\{c\}$), so $\{c\}^{\circ} = \varnothing$
and $\partial\{c\} = \overline{\{c\}}\setminus\{c\}^{\circ} = \{c\}$.

**(d)** The closed supersets of $\{a\}$ are $\{a,c\}$ and $X$, so $\overline{\{a\}} = \{a,c\}$; in
particular $\{a\}$ is not closed. Since $\{a,b\}$ is itself open, $\{a,b\}^{\circ} = \{a,b\}$.

**(e)** The space is $T_0$: for $a,b$ the open set $\{a\}$ contains exactly one of them; for $a,c$ the
same set works; for $b,c$ the open set $\{b\}$ works. It is not $T_1$: every neighbourhood of $c$ is
$X$, so there is no open set containing $c$ and omitting $a$. Equivalently, by Theorem 7.11.2, $\{c\}$
is not closed (its only closed superset is $X$).

### Solution 2

**(a)** (O1): $\varnothing\in\tau_p$ by definition and $X\in\tau_p$ because $p\in X$. (O2): a union of
members of $\tau_p$ is empty (if all are empty) or contains $p$ (if one does), hence lies in $\tau_p$.
(O3): if $U,V\in\tau_p$ are nonempty then $p\in U\cap V$, so $U\cap V\in\tau_p$; if either is empty, so
is the intersection.

**(b)** $F$ is closed iff $X\setminus F\in\tau_p$ iff $X\setminus F = \varnothing$ or $p\in X\setminus F$,
that is, iff $F = X$ or $p\notin F$. So the closed sets are $X$ together with all subsets avoiding $p$.
Then $\overline{\{p\}} = X$ (the only closed superset of $\{p\}$), while for $x\ne p$ the set $\{x\}$ is
closed and $\overline{\{x\}} = \{x\}$.

**(c)** Let $x\ne y$. If $x = p$, the open set $\{p\}$ contains $x$ and not $y$. If $y = p$, the same open
set $\{p\}$ contains exactly one of the two points, namely $y$. If neither point is $p$, then $\{p,x\}$ is
open (it contains $p$), it contains $x$, and it does not contain $y$ because $y\ne x$ and $y\ne p$. In
every case some open set contains exactly one of $x,y$.

*Not $T_1$.* Let $x\ne p$. Every open set containing $x$ is nonempty, hence contains $p$. So there is no
open set containing $x$ and omitting $p$, and the singleton $\{p\}$ is not closed ($X\setminus\{p\}$ is
nonempty and does not contain $p$, so it is not open). The point that fails to be closed is $p$; all
other points are isolated in the strong sense that $\{x\}$ is both open and closed.

### Solution 3

**(a)** $\varnothing$ is closed because $X\setminus\varnothing = X$ is open by (O1); $X$ is closed because
$X\setminus X = \varnothing$ is open.

**(b)** Let $\{F_i\}_{i\in I}$ be closed. Then
$X\setminus\bigcap_{i\in I}F_i = \bigcup_{i\in I}(X\setminus F_i)$ is a union of open sets, hence open by
(O2), so $\bigcap_i F_i$ is closed. For finitely many, $X\setminus\bigcup_{k=1}^{n}F_k = \bigcap_{k=1}^{n}(X\setminus F_k)$
is a finite intersection of open sets, open by (O3) and induction.

**(c)** $\bigcup_{n\in\mathbb{N}}[1/n,\,1] = (0,1]$, which is not closed: the point $0$ lies in the
closure, since every interval $(-\varepsilon,\varepsilon)$ meets $(0,1]$, but $0\notin(0,1]$. Dually
$\bigcap_{n\in\mathbb{N}}(-1/n,\,1/n) = \{0\}$, which is not open: every interval around $0$ contains a
point different from $0$, so no interval is contained in $\{0\}$.

### Solution 4

**(a)** (O1): $\varnothing$ is listed and $X\setminus X = \varnothing$ is finite. (O2): let
$\{U_i\}\subseteq\tau_{\mathrm{cof}}$. If all $U_i = \varnothing$ the union is $\varnothing$. Otherwise
pick $j$ with $U_j\ne\varnothing$; then $X\setminus U_j$ is finite, and
$X\setminus\bigcup_i U_i = \bigcap_i(X\setminus U_i)\subseteq X\setminus U_j$ is finite, so the union is
cofinite. (O3): if $U = \varnothing$ or $V = \varnothing$ the intersection is empty; otherwise
$X\setminus(U\cap V) = (X\setminus U)\cup(X\setminus V)$ is a union of two finite sets.

**(b)** $F$ is closed iff $X\setminus F$ is open iff $X\setminus F = \varnothing$ or $X\setminus(X\setminus F) = F$ is
finite, i.e. iff $F = X$ or $F$ is finite. In particular every singleton is closed, so the space is $T_1$
by Theorem 7.11.2.

**(c)** Let $U\ne\varnothing$ be open. Then $X\setminus U$ is finite and $U = X\setminus(X\setminus U)$.
If $X$ were finite then $U$ could be finite; but $X$ is infinite, so removing finitely many points from
an infinite set leaves an infinite set. Explicitly, $U$ is in bijection with $X$ minus a finite set, so
$U$ is infinite.

### Solution 5

**(a)** The discrete topology $\mathcal{P}(X)$ is a topology: an arbitrary union or a finite intersection
of subsets of $X$ is a subset of $X$. Every topology $\tau$ on $X$ satisfies $\tau\subseteq\mathcal{P}(X)$
by definition, so $\mathcal{P}(X)$ is the finest. The indiscrete family $\{\varnothing,X\}$ is a topology:
its only unions are $\varnothing$ and $X$, and its only intersections are $\varnothing$ and $X$. Every
topology contains $\varnothing$ and $X$ by (O1), so $\{\varnothing,X\}\subseteq\tau$ for every $\tau$, and
the indiscrete topology is the coarsest.

**(b)** If the space is discrete, every subset — in particular every singleton — is open. Conversely,
suppose every singleton is open. Any $A\subseteq X$ satisfies $A = \bigcup_{x\in A}\{x\}$, a union of open
sets, hence open by (O2). So every subset is open and the topology is discrete.

### Solution 6

**(a)** $\varnothing$ and $X$ belong to both $\tau_1$ and $\tau_2$, hence to the intersection. If
$\{U_i\}\subseteq\tau_1\cap\tau_2$, then $\bigcup_i U_i\in\tau_1$ and $\in\tau_2$, so it lies in the
intersection. If $U,V\in\tau_1\cap\tau_2$ then $U\cap V\in\tau_1\cap\tau_2$. So (O1)–(O3) hold.

**(b)** On $X = \{1,2,3\}$ take $\tau_1 = \{\varnothing,\{1\},X\}$ and $\tau_2 = \{\varnothing,\{2\},X\}$;
both are topologies. Their union is $\{\varnothing,\{1\},\{2\},X\}$, which is not closed under unions,
since $\{1\}\cup\{2\} = \{1,2\}$ is not in it.

### Solution 7

Throughout, a point $x$ is in $\overline A$ exactly when every interval $(x-\varepsilon,x+\varepsilon)$
meets $A$, and $x\in A'$ exactly when every such interval meets $A\setminus\{x\}$.

**(a) $A = (0,1)$.** If $0<x<1$ then $x\in A\subseteq\overline A$. For $x = 0$ every interval
$(-\varepsilon,\varepsilon)$ contains points of $(0,1)$, and similarly for $x = 1$; so $[0,1]\subseteq\overline A$.
If $x<0$ take $\varepsilon = -x/2$, then $(x-\varepsilon,x+\varepsilon)\subseteq(-\infty,0)$ misses $A$; if
$x>1$ take $\varepsilon = (x-1)/2$. Hence $\overline A = [0,1]$. Since $A$ is open,
$A^{\circ} = A = (0,1)$. Then $\partial A = \overline A\setminus A^{\circ} = \{0,1\}$. Finally
$A' = [0,1]$: points of $(0,1)$ are limits (every interval around them contains other points of $A$),
and $0,1$ are limits as shown; points outside $[0,1]$ are not.

**(b) $A = \mathbb{Q}$.** Every nonempty open interval contains a rational (density of $\mathbb{Q}$) and
an irrational, so $\overline{\mathbb{Q}} = \mathbb{R}$ and no nonempty open interval is contained in
$\mathbb{Q}$, whence $\mathbb{Q}^{\circ} = \varnothing$. Therefore $\partial\mathbb{Q} = \mathbb{R}$,
and $\mathbb{Q}' = \mathbb{R}$ because every interval meets $\mathbb{Q}\setminus\{x\}$.

**(c) $A = \{1/n : n\in\mathbb{N}\}$.** The point $0$ lies in the closure, because for every
$\varepsilon>0$ some $1/n<\varepsilon$ lies in $(-\varepsilon,\varepsilon)$. A point $x\notin A$ with
$x\ne0$ has positive distance to $A$: if $x<0$ or $x>1$ this is clear; if $0<x<1$ and $x\notin A$ then
$x\in(1/(n+1),1/n)$ for a unique $n$, and $\varepsilon = \min(x-1/(n+1),\,1/n-x)>0$ isolates $x$ from
$A$. Hence $\overline A = A\cup\{0\}$. Since $A$ is countable while every interval is uncountable, no
interval is contained in $A$ and $A^{\circ} = \varnothing$. Thus $\partial A = A\cup\{0\}$. The derived
set is $A' = \{0\}$, because each $1/n$ is isolated in $A$ (the interval
$(1/(n+1),1/(n-1))$ meets $A$ only in $1/n$) and $0$ is a limit point.

**(d) $A = [0,1]\cup\{2\}$.** This set is closed, since its complement
$(-\infty,0)\cup(1,2)\cup(2,\infty)$ is open; so $\overline A = A$. The interior is $(0,1)$: points of
that interval have a small interval inside $A$, while $0,1,2$ do not ($0$ and $1$ are endpoints, and every
interval around $2$ contains points outside $A$). Hence $\partial A = A\setminus(0,1) = \{0,1,2\}$. Since
$2$ is isolated in $A$, $A' = [0,1]$.

### Solution 8

Suppose $x\in\overline A$ and let $N$ be a neighbourhood of $x$. By definition there is an open $U$ with
$x\in U\subseteq N$. If $N\cap A = \varnothing$ then $U\cap A = \varnothing$, so $X\setminus U$ is a closed
set containing $A$; by Theorem 7.9.1(1), $\overline A\subseteq X\setminus U$, and since $x\in U$ this
contradicts $x\in\overline A$. Hence $N\cap A\ne\varnothing$.

Conversely, suppose every neighbourhood of $x$ meets $A$. If $x\notin\overline A$, then
$X\setminus\overline A$ is an open neighbourhood of $x$ disjoint from $A$ (because
$A\subseteq\overline A$), a contradiction.

For the neighbourhood base: if every neighbourhood of $x$ meets $A$, then in particular every
$B\in\mathcal{B}_x$ does. Conversely, if every $B\in\mathcal{B}_x$ meets $A$ and $N$ is a neighbourhood of
$x$, choose $B\in\mathcal{B}_x$ with $B\subseteq N$; then $B\cap A\subseteq N\cap A$ is nonempty.

### Solution 9

*If $F$ is closed, then $F'\subseteq F$.* Let $x\notin F$. Since $F$ is closed, $X\setminus F$ is an open
neighbourhood of $x$ disjoint from $F$, hence disjoint from $F\setminus\{x\}$. So $x\notin F'$.

*If $F'\subseteq F$, then $F$ is closed.* Let $x\in X\setminus F$. Since $x\notin F'$ there is a
neighbourhood $N$ of $x$ with $N\cap(F\setminus\{x\}) = \varnothing$; as $x\notin F$ this gives
$N\cap F = \varnothing$. Choose an open $U_x$ with $x\in U_x\subseteq N$; then $U_x\cap F = \varnothing$
and $U_x\subseteq X\setminus F$. Therefore $X\setminus F = \bigcup_{x\in X\setminus F}U_x$ is open, so
$F$ is closed.

### Solution 10

**(a)** By Theorem 7.11.2 (or directly: $T_1$ gives, for each $y\ne x$, an open $U_y\ni y$ with $x\notin U_y$,
so $X\setminus\{x\} = \bigcup_{y\ne x}U_y$ is open), every singleton is closed. A finite set
$\{x_1,\dots,x_n\} = \{x_1\}\cup\cdots\cup\{x_n\}$ is a finite union of closed sets, hence closed by
Theorem 7.2.1(C3).

**(b)** If $X$ is finite and $T_1$, every subset $A\subseteq X$ is finite, hence closed by (a). So every
subset is closed, and taking complements every subset is open: the topology is $\mathcal{P}(X)$.

## Intermediate

### Solution 11

**Necessity.** Let $\mathcal{B}$ be a base for $\tau$. Since $X\in\tau$ is a union of members of
$\mathcal{B}$, (B1) holds. For (B2), let $B_1,B_2\in\mathcal{B}$ and $x\in B_1\cap B_2$. The set
$B_1\cap B_2$ is open (it is in $\tau$), so by the second form of Definition 5.4 there is
$B_3\in\mathcal{B}$ with $x\in B_3\subseteq B_1\cap B_2$.

**Sufficiency.** Assume (B1) and (B2) and let
$\tau = \{\bigcup\mathcal{C} : \mathcal{C}\subseteq\mathcal{B}\}$, with the empty union equal to
$\varnothing$. Then $\varnothing\in\tau$, and $X = \bigcup\mathcal{B}\in\tau$ by (B1). A union of members
of $\tau$ is a union of unions of members of $\mathcal{B}$, hence a union of members of $\mathcal{B}$, so
it lies in $\tau$. For a binary intersection write $U = \bigcup_i B_i$ and $V = \bigcup_j C_j$; then

$$
U\cap V = \bigcup_{i,j}(B_i\cap C_j).
$$

Each $B_i\cap C_j$ is a union of members of $\mathcal{B}$: given $x\in B_i\cap C_j$, axiom (B2) provides
$B\in\mathcal{B}$ with $x\in B\subseteq B_i\cap C_j$, and therefore
$B_i\cap C_j = \bigcup\{B\in\mathcal{B} : B\subseteq B_i\cap C_j\}$. So $U\cap V$ is a union of unions of
members of $\mathcal{B}$ and lies in $\tau$. Hence $\tau$ is a topology, and by construction every
member of $\mathcal{B}$ is open in it and every open set is a union of members of $\mathcal{B}$: so
$\mathcal{B}$ is a base for $\tau$.

**Uniqueness.** If $\tau$ and $\tau'$ are topologies for which $\mathcal{B}$ is a base, then every
$U\in\tau$ is a union of members of $\mathcal{B}\subseteq\tau'$, hence $U\in\tau'$; symmetrically
$\tau'\subseteq\tau$.

### Solution 12

Let $\mathcal{B}$ be the family of finite intersections $S_1\cap\cdots\cap S_k$ of members of $\mathcal{S}$
(with $k = 0$ giving $X$). We verify the base criterion of Theorem 7.5.2. (B1): $X\in\mathcal{B}$ by the
empty intersection, so $\bigcup\mathcal{B}\supseteq X$. (B2): if $B_1 = S_1\cap\cdots\cap S_m$ and
$B_2 = T_1\cap\cdots\cap T_n$ then $B_1\cap B_2 = S_1\cap\cdots\cap S_m\cap T_1\cap\cdots\cap T_n$ is
again a finite intersection of members of $\mathcal{S}$, so $B_3 = B_1\cap B_2$ works. Hence
$\mathcal{B}$ is a base for a topology $\tau$, and $\mathcal{S}\subseteq\mathcal{B}\subseteq\tau$.

For minimality, let $\sigma$ be any topology containing $\mathcal{S}$. It contains every finite
intersection of members of $\mathcal{S}$, i.e. $\mathcal{B}\subseteq\sigma$, hence contains all unions of
members of $\mathcal{B}$, i.e. $\tau\subseteq\sigma$. So $\tau$ is the coarsest topology containing
$\mathcal{S}$.

**The covering hypothesis.** Let $X = \{1,2,3\}$ and $\mathcal{S} = \{\{1\}\}$. The finite intersections
are $X$ and $\{1\}$, and $\bigcup\mathcal{B} = \{1\}\ne X$: condition (B1) fails, so these sets are not a
base for any topology on $X$. The topology generated by $\mathcal{S}$ in the sense of Definition 7.1.2 is
$\{\varnothing,\{1\},X\}$ — it contains $\varnothing,X,\{1\}$ and is closed under unions and intersections,
and it is contained in every topology containing $\{1\}$. But the open set $X$ of that topology is not a
union of members of $\mathcal{B} = \{\varnothing,\{1\}\}$, so $\mathcal{B}$ is not a base for it.

### Solution 13

**(a)** (B1): for every $x$, $x\in[x,x+1)\in\mathcal{B}$. (B2): let $x\in[a,b)\cap[c,d)$. Put
$e = \max(a,c)$ and $f = \min(b,d)$. Then $e\le x<f$ because $x\ge a$, $x\ge c$ and $x<b$, $x<d$. Hence
$[e,f)\in\mathcal{B}$ and $[e,f)\subseteq[a,b)\cap[c,d)$: if $e\le t<f$ then $a\le e\le t<f\le b$ and
likewise for $c,d$. By Theorem 7.5.2, $\mathcal{B}$ is a base for a topology $\tau_\ell$.

**(b)** For $a<b$,

$$
(a,b) = \bigcup_{n\in\mathbb{N}}\Big[a+\frac1n,\;b\Big).
$$

The inclusion $\supseteq$ is clear since $[a+1/n,b)\subseteq(a,b)$. For $\subseteq$, let $a<x<b$; choose
$n$ with $1/n\le x-a$, which is possible because $1/n\to0$; then $x\in[a+1/n,b)$. So every open interval
is $\tau_\ell$-open, and since every usual-open set is a union of open intervals, every usual-open set is
$\tau_\ell$-open. The inclusion is strict: $[0,1)$ is $\tau_\ell$-open, but it is not a usual
neighbourhood of $0$, since every interval $(-\varepsilon,\varepsilon)$ contains negative numbers.

**(c)** $[a,b)$ is open by definition. Its complement is $(-\infty,a)\cup[b,\infty)$, and

$$
(-\infty,a) = \bigcup_{n\in\mathbb{N}}[a-n,\,a), \qquad [b,\infty) = \bigcup_{n\in\mathbb{N}}[b,\,b+n),
$$

so the complement is a union of basic open sets, hence open. Therefore $[a,b)$ is closed.

**(d)** Suppose $\{x\}$ were open. Since it is nonempty and open, it is a union of basic sets, so it
contains a basic set $[a,b)$ with $x\in[a,b)\subseteq\{x\}$. As $a<b$ the interval $[a,b)$ contains
infinitely many points, in particular a point different from $x$, contradicting
$[a,b)\subseteq\{x\}$. Hence no singleton is open and $\mathbb{R}_\ell$ is not discrete.

### Solution 14

**(a)** $\varnothing = \varnothing\cap A$ and $A = X\cap A$ are in $\tau_A$. If $V_i = U_i\cap A$ then
$\bigcup_i V_i = \bigl(\bigcup_i U_i\bigr)\cap A\in\tau_A$ and
$V_1\cap V_2 = (U_1\cap U_2)\cap A\in\tau_A$.

**(b)** For open $U\subseteq X$, $i^{-1}[U] = \{a\in A : a\in U\} = U\cap A\in\tau_A$, so $i$ is continuous.
If $\sigma$ is a topology on $A$ for which $i$ is continuous, then $U\cap A = i^{-1}[U]\in\sigma$ for every
open $U$, so $\tau_A\subseteq\sigma$. Hence $\tau_A$ is the coarsest such topology.

**(c)** If $f$ is continuous then $i\circ f$ is a composite of continuous maps. Conversely, suppose
$i\circ f$ is continuous and let $V\subseteq A$ be open. By the definition of $\tau_A$ there is an open
$U\subseteq X$ with $V = U\cap A$. Then

$$
f^{-1}[V] = f^{-1}\big[i^{-1}[U]\big] = (i\circ f)^{-1}[U]
$$

is open in $Z$, because $i\circ f$ is continuous and $U$ is open in $X$.

### Solution 15

**(a)** Let $\mathcal{B}$ be a base for $X$ and $\mathcal{B}_A = \{B\cap A : B\in\mathcal{B}\}$. (B1):
$A = X\cap A$ and $X$ is a union of members of $\mathcal{B}$, so $A$ is a union of members of
$\mathcal{B}_A$. (B2): if $x\in(B_1\cap A)\cap(B_2\cap A) = (B_1\cap B_2)\cap A$, choose $B_3\in\mathcal{B}$
with $x\in B_3\subseteq B_1\cap B_2$; then $x\in B_3\cap A\subseteq(B_1\cap B_2)\cap A$. So
$\mathcal{B}_A$ is a base for a topology on $A$; and every set $U\cap A$ with $U$ open is a union of sets
$B\cap A$, so $\mathcal{B}_A$ is a base for $\tau_A$.

**(b)** If $\mathcal{B}$ is a countable base for $X$, then $\mathcal{B}_A$ is a countable base for $A$.

**(c)** $A\setminus(U\cap A) = (X\setminus U)\cap A$, so the complement in $A$ of an open set of $A$ is the
trace of a closed set of $X$. Conversely, if $F\subseteq X$ is closed then $F\cap A = A\setminus(U\cap A)$
with $U = X\setminus F$ open, so $F\cap A$ is closed in $A$.

### Solution 16

**(a)** Let $\mathcal{B}_p$ be the family described. (B1): the product $\prod_i X_i$ belongs to
$\mathcal{B}_p$ (all factors $X_i$). (B2): if $B = \prod_i U_i$ and $C = \prod_i V_i$ are in
$\mathcal{B}_p$, then $B\cap C = \prod_i(U_i\cap V_i)$, and $U_i\cap V_i = X_i$ for all but finitely many
$i$; so $B\cap C\in\mathcal{B}_p$ and $B_3 = B\cap C$ satisfies (B2). By Theorem 7.5.2 there is a topology
$\tau_p$ with base $\mathcal{B}_p$.

**(b)** Each subbasic set $\pi_j^{-1}[U] = U\times\prod_{i\ne j}X_i$ lies in $\mathcal{B}_p$, so $\pi_j$ is
continuous for $\tau_p$. If $\sigma$ is any topology making all $\pi_j$ continuous, then
$\pi_j^{-1}[U]\in\sigma$ for all $j,U$, so $\sigma$ contains all finite intersections of such sets,
i.e. $\mathcal{B}_p\subseteq\sigma$, and hence contains all unions, i.e. $\tau_p\subseteq\sigma$. So
$\tau_p$ is the coarsest.

**(c)** If $f$ is continuous then each $\pi_j\circ f$ is continuous as a composition. Conversely assume
every $\pi_j\circ f$ is continuous. For a basic open $B = \prod_j U_j$ with $U_j = X_j$ for $j\notin F$,
$F$ finite,

$$
f^{-1}[B] = \bigcap_{j\in F}(\pi_j\circ f)^{-1}[U_j],
$$

a finite intersection of open sets, hence open. Since every open set of $P$ is a union of basic ones,
$f^{-1}$ of an open set is a union of open sets, hence open. So $f$ is continuous.

### Solution 17

**(a)** Let $V\subseteq P$ be open; write $V = \bigcup_{i}B_i$ with $B_i = \prod_j U_{ij}$ basic. Then
$\pi_j[V] = \bigcup_i \pi_j[B_i]$. For a basic $B = \prod_i U_i$ we have
$\pi_j[B] = U_j$ if all $U_i\ne\varnothing$, and $\pi_j[B] = \varnothing$ otherwise (if some factor is
empty then $B = \varnothing$). In both cases $\pi_j[B]$ is open, so $\pi_j[V]$ is a union of open sets.
Hence $\pi_j$ is open.

**(b)** Let $\pi_1 : \mathbb{R}^2\to\mathbb{R}$ be the first projection and let
$F = \{(x,y)\in\mathbb{R}^2 : xy = 1\}$. The map $(x,y)\mapsto xy$ is continuous, so $F$ is the preimage of
the closed set $\{1\}$ and is closed. But $\pi_1[F] = \mathbb{R}\setminus\{0\}$, which is not closed in
$\mathbb{R}$. (Equivalently, $\{(x,y) : xy = 1\}$ is closed because it is the zero set of the continuous
function $xy-1$.) So projections need not be closed.

### Solution 18

**(a)** Let $A\subseteq X$ be a subspace of a Hausdorff $X$, and let $x\ne y$ in $A$. Choose disjoint open
$U,V\subseteq X$ with $x\in U$, $y\in V$. Then $U\cap A$ and $V\cap A$ are open in $A$, disjoint, and
contain $x$ and $y$.

**(b)** Let $x\ne y$ in $P = \prod_i X_i$. Then $x_j\ne y_j$ for some $j$. Choose disjoint open
$U_j,V_j\subseteq X_j$ with $x_j\in U_j$, $y_j\in V_j$. Then $\pi_j^{-1}[U_j]$ and $\pi_j^{-1}[V_j]$ are
open in $P$, disjoint (because $U_j\cap V_j = \varnothing$), and contain $x$ and $y$.

**(c)** If $A\subseteq X$ and $X$ is $T_1$, then for $x\in A$ the set $\{x\} = A\cap\{x\}$ is the trace of
a closed set of $X$ (Theorem 7.11.2), hence closed in $A$ by Solution 15(c). So all singletons in $A$ are
closed and $A$ is $T_1$.

### Solution 19

By (K2), $A\subseteq c(A)$ always, so (C1) follows from (K1): $c(\varnothing) = \varnothing$, and
$c(X) = X$ because $X\subseteq c(X)\subseteq X$.

*Monotonicity.* If $A\subseteq B$ then $A\cup B = B$, so by (K4)
$c(A)\cup c(B) = c(B)$, whence $c(A)\subseteq c(B)$.

(C2): let $\{A_i\}\subseteq\mathcal{F}$, so $c(A_i) = A_i$, and put $A = \bigcap_i A_i$. Since
$A\subseteq A_i$, monotonicity gives $c(A)\subseteq c(A_i) = A_i$ for every $i$, hence
$c(A)\subseteq\bigcap_i A_i = A$. With (K2), $c(A) = A$.

(C3): if $c(A) = A$ and $c(B) = B$ then by (K4) $c(A\cup B) = c(A)\cup c(B) = A\cup B$.

Let $\overline{\cdot}$ denote closure in the topology whose closed sets are $\mathcal{F}$ (legitimate by
Theorem 7.2.1). Since $c(A)\in\mathcal{F}$ and $A\subseteq c(A)$, minimality of the closure gives
$\overline A\subseteq c(A)$. Conversely $\overline A$ is closed, so $c(\overline A) = \overline A$, and
$A\subseteq\overline A$ with monotonicity gives $c(A)\subseteq c(\overline A) = \overline A$. Hence
$c(A) = \overline A$.

### Solution 20

Write $\overline A = \bigcap\{F : F \text{ closed}, A\subseteq F\}$ and
$\partial A = \overline A\cap\overline{X\setminus A}$.

*First identity.* If $x\in\overline A$ and $x\notin A$, then every neighbourhood of $x$ meets $A$
(Theorem 7.9.1(2)) and contains $x\notin A$, so it meets $X\setminus A$; hence $x\in\partial A$. Together
with $A\subseteq\overline A$ and $\partial A\subseteq\overline A$ this gives
$\overline A = A\cup\partial A$.

*Second identity.* If $x\in A^{\circ}$ then $A^{\circ}$ is an open neighbourhood of $x$ contained in $A$,
so it is disjoint from $X\setminus A$ and $x\notin\overline{X\setminus A}$; hence $x\in A\setminus\partial A$.
Conversely, if $x\in A\setminus\partial A$ then $x\in A\subseteq\overline A$ and
$x\notin\overline{X\setminus A}$, so there is an open $U\ni x$ with $U\cap(X\setminus A) = \varnothing$;
then $x\in U\subseteq A$ and $x\in A^{\circ}$.

*Third identity.* The three sets are pairwise disjoint: $A^{\circ}\cap\partial A = \varnothing$ by the
second identity, $A^{\circ}\cap(X\setminus\overline A) = \varnothing$ since $A^{\circ}\subseteq\overline A$,
and $\overline A\cap(X\setminus\overline A) = \varnothing$. They cover $X$: if $x\notin A^{\circ}$ and
$x\notin X\setminus\overline A$ then $x\in\overline A$ and $x\notin A^{\circ}$, so $x\in\partial A$.

*Clopen criterion.* If $A$ is clopen then $\overline A = A$ and $\overline{X\setminus A} = X\setminus A$,
so $\partial A = A\cap(X\setminus A) = \varnothing$. Conversely if $\partial A = \varnothing$ then the
first identity gives $\overline A = A$, so $A$ is closed; applying the same argument to $X\setminus A$
(using $\partial(X\setminus A) = \partial A$, which is immediate from the definition) gives that
$X\setminus A$ is closed, so $A$ is open.

### Solution 21

**(a)** Let $a<b$ in $\mathbb{R}$ and choose $n$ with $1/n < b-a$. Then some integer multiple $k/n$
satisfies $a<k/n<b$ (take $k = \lfloor na\rfloor+1$; then $k/n>a$ and $k/n\le a+1/n<b$). So every
nonempty open interval meets $\mathbb{Q}$, and $\mathbb{Q}$ is dense. For $\mathbb{Q}^2$: a nonempty basic
open set of $\mathbb{R}^2$ contains a rectangle $(a,b)\times(c,d)$, which contains
$(q_1,q_2)\in\mathbb{Q}^2$ by the first part.

**(b)** Let $V\subseteq A$ be nonempty and open. Then $V = U\cap A$ for some open $U\subseteq X$, and
$U\ne\varnothing$ because $V\ne\varnothing$. Since $D$ is dense, $U\cap D\ne\varnothing$
(Corollary 7.9.5), so $V\cap(D\cap A) = (U\cap A)\cap D = U\cap D\cap A\ne\varnothing$. Hence $D\cap A$
meets every nonempty open subset of $A$, i.e. it is dense in $A$.

*Example where $D\cap A$ is not dense in $X$*: take $D = \mathbb{Q}\subseteq\mathbb{R}$ and
$A = \{\sqrt2\}$. Then $D\cap A = \varnothing$, which is not dense in $\mathbb{R}$. (It *is* dense in the
subspace $A$ only when $A$ is empty; here $A\ne\varnothing$, and indeed $\varnothing$ is not dense in
$A$.) The point is that density is relative to an ambient space.

**(c)** If $X$ is separable with countable dense $D$ and $A\subseteq X$, then $D\cap A$ is countable and,
by (b), dense in $A$. So $A$ is separable.

### Solution 22

**(a)** (N1): if $N\in\mathcal{N}(x)$ there is an open $U$ with $x\in U\subseteq N$, so $x\in N$; and
$\mathcal{N}(x)\ne\varnothing$ because $X$ is a neighbourhood of $x$. (N2): the same $U$ gives
$x\in U\subseteq M$. (N3): if $x\in U\subseteq N_1$ and $x\in V\subseteq N_2$ with $U,V$ open, then
$x\in U\cap V\subseteq N_1\cap N_2$ and $U\cap V$ is open. (N4): for $N\in\mathcal{N}(x)$ choose open $U$
with $x\in U\subseteq N$; then $U\in\mathcal{N}(x)$ and, for every $y\in U$, the same $U$ witnesses
$U\in\mathcal{N}(y)$.

**(b)** If $U$ is open then $U$ is a neighbourhood of each of its points (take $V = U$ in
Definition 5.3). Conversely, if $U\in\mathcal{N}(x)$ for all $x\in U$, choose for each $x$ an open $V_x$
with $x\in V_x\subseteq U$; then $U = \bigcup_{x\in U}V_x$ is open by (O2).

**(c)** In $\mathbb{R}$ the sets $N_n = (-1/n,1/n)$ are neighbourhoods of $0$, but
$\bigcap_n N_n = \{0\}$ is not a neighbourhood of $0$: a neighbourhood must contain an interval
$(-\varepsilon,\varepsilon)$, and no such interval is contained in $\{0\}$.

## Advanced

### Solution 23

**(a)** If $f$ is continuous then $f\circ q$ is a composite of continuous maps. Conversely assume
$f\circ q$ continuous and let $W\subseteq Z$ be open. Then
$q^{-1}\big[f^{-1}[W]\big] = (f\circ q)^{-1}[W]$ is open in $X$, so $f^{-1}[W]$ is open in $Y$ by the
definition of the quotient topology. Hence $f$ is continuous.

**(b)** Recall that $q$ is surjective, so $q\big[q^{-1}[B]\big] = B$ for every $B\subseteq Y$, and that
$A\subseteq X$ is saturated iff $A = q^{-1}[q[A]]$.

Assume $q$ open. If $U\subseteq X$ is open, then $q[U]$ is open, so $q^{-1}[q[U]]$ is open because $q$ is
continuous.

Conversely, assume $q^{-1}[q[U]]$ is open for every open $U$. Let $U$ be open. Then
$q[U] = q\big[q^{-1}[q[U]]\big]$, and since $q^{-1}[q[U]]$ is open, $q[U]$ is open by the definition of
the quotient topology. So $q$ is open. (The displayed identity uses only surjectivity of $q$.)

**(c)** *A quotient map that is not open.* Let $X = [0,1]\cup[2,3]\subseteq\mathbb{R}$ with the subspace
topology, $Y = [0,2]$, and $q(x) = x$ for $x\in[0,1]$, $q(x) = x-1$ for $x\in[2,3]$. Then $q$ is a
continuous surjection. It is closed: if $F\subseteq X$ is closed then $F = F_1\cup F_2$ with
$F_1 = F\cap[0,1]$ and $F_2 = F\cap[2,3]$ closed in $\mathbb{R}$, so $q[F] = F_1\cup(F_2-1)$ is a finite
union of closed subsets of $\mathbb{R}$, hence closed. A continuous surjection that is closed is a
quotient map: if $q^{-1}[V]$ is open then $X\setminus q^{-1}[V] = q^{-1}[Y\setminus V]$ is closed, so
$Y\setminus V = q[q^{-1}[Y\setminus V]]$ is closed, so $V$ is open. Finally $q$ is not open:
$U = [0,1] = X\cap(-1,1.5)$ is open in $X$, but $q[U] = [0,1]$ is not open in $Y = [0,2]$, since every
$Y$-neighbourhood of $1$ contains points $>1$.

*A quotient map that is not closed.* Let $q : \mathbb{R}\to S^1$, $q(t) = e^{2\pi it}$. It is a
continuous surjection. It is open: an open interval $(a,b)$ is a union of intervals of length $<1$, each
of which maps onto an open arc of $S^1$; so the image of any open set is open. A continuous surjection
that is open is a quotient map (dual argument to the one above: if $q^{-1}[V]$ is open then
$V = q[q^{-1}[V]]$ is open). It is not closed: $A = \{n+1/n : n\ge2\}$ is closed in $\mathbb{R}$ (a
discrete set with no finite accumulation point), but $q[A] = \{e^{2\pi i/n} : n\ge2\}$ has the limit
$1 = q(0)$, which is not in $q[A]$.

### Solution 24

**(a)** Let $[a,b)$ be a nonempty basic open set. Then $[a,b)\supseteq(a,b)\ne\varnothing$, and $(a,b)$
contains a rational. So every nonempty basic open set meets $\mathbb{Q}$, hence by Corollary 7.9.5
$\mathbb{Q}$ is dense and $\mathbb{R}_\ell$ is separable.

**(b)** Suppose $\mathcal{C}$ is a base. For each $x\in\mathbb{R}$ the set $[x,x+1)$ is an open
neighbourhood of $x$, so there is $C_x\in\mathcal{C}$ with $x\in C_x\subseteq[x,x+1)$. We show that
$\inf C_x = x$. First, $\inf C_x\ge x$ because $C_x\subseteq[x,x+1)$. Second, $C_x$ is open and contains
$x$, so it contains a basic set $[a,b)\ni x$; then $a\le x$ and $a\ge\inf C_x$, so $\inf C_x\le x$. Hence
$\inf C_x = x$. If $x\ne y$ then $\inf C_x = x\ne y = \inf C_y$, so $C_x\ne C_y$: the map
$x\mapsto C_x$ is injective from $\mathbb{R}$ into $\mathcal{C}$. Therefore $\mathcal{C}$ is uncountable
and no countable base exists.

**(c)** Let $(X,d)$ be metric, $D$ countable and dense. Claim:
$\mathcal{B} = \{B_{1/n}(q) : q\in D,\ n\in\mathbb{N}\}$ is a countable base. It is countable as a product
of two countable sets. Let $x\in U$ with $U$ open; choose $r>0$ with $B_r(x)\subseteq U$ and then $n$ with
$2/n<r$. Since $D$ is dense there is $q\in D$ with $d(x,q)<1/n$. Then $x\in B_{1/n}(q)$, and for
$y\in B_{1/n}(q)$,

$$
d(x,y)\le d(x,q)+d(q,y) < \frac1n+\frac1n = \frac2n < r,
$$

so $y\in B_r(x)\subseteq U$. Hence $x\in B_{1/n}(q)\subseteq U$, and $\mathcal{B}$ is a base.

**(d)** $\mathbb{R}_\ell$ is separable by (a). If it were metrisable, (c) would give it a countable base,
contradicting (b). So it carries no metric inducing its topology.

### Solution 25

**(a)** Every open interval $(a,b)$ belongs to the base $\mathcal{B}_K$, so the usual topology is contained
in $\tau_K$; hence $\tau_K$ is finer. Two distinct points $x,y$ are separated by disjoint usual-open
neighbourhoods, and these are also $\tau_K$-open; so $\mathbb{R}_K$ is Hausdorff. (The inclusion is strict:
$(-1,1)\setminus K$ is $\tau_K$-open but not usual-open, since $0$ is in it while every interval around
$0$ contains some $1/n\in K$.)

**(b)** As computed in Example 9.7,

$$
\mathbb{R}\setminus K = (-\infty,0)\cup\bigcup_{n\in\mathbb{N}}\Big(\frac{1}{n+1},\frac{1}{n}\Big)\cup(1,\infty)
$$

is a union of usual-open, hence $\tau_K$-open, sets. So $K$ is closed. Clearly $0\notin K$, since
$1/n>0$ for all $n$.

**(c)** Suppose $U\ni0$ and $V\supseteq K$ are disjoint $\tau_K$-open sets. Since $U$ is a neighbourhood
of $0$, it contains a basic $B\ni0$, necessarily $B = (a,b)$ or $(a,b)\setminus K$ with $a<0<b$; in either
case $(a,b)\setminus K\subseteq U$. Choose $n$ with $0<1/n<b$ (and $1/n>a$, which holds for large $n$
since $a<0$). Since $1/n\in K\subseteq V$ and $V$ is open, $V$ contains a basic $B_n\ni1/n$. Because
$1/n\in K$, the set $B_n$ is not of the form $(c,d)\setminus K$ (those avoid $K$), so $B_n = (c,d)$ with
$1/n\in(c,d)$.

Now $(a,b)\cap(c,d)$ is a nonempty open interval, hence uncountable, so it contains some $t\notin K$.
Then $t\in(a,b)\setminus K\subseteq U$ and $t\in(c,d)\subseteq V$, contradicting
$U\cap V = \varnothing$. So $0$ and the closed set $K$ cannot be separated by disjoint open sets, and
$\mathbb{R}_K$ is not regular. It is $T_1$ because it is finer than $\mathbb{R}$, so it is $T_2$ but not
$T_3$.

### Solution 26

**(a)** For $a\in A$, the triangle inequality gives $d(x,a)\le d(x,y)+d(y,a)$. Taking the infimum over
$a\in A$ gives $d(x,A)\le d(x,y)+d(y,A)$, i.e. $d(x,A)-d(y,A)\le d(x,y)$. Interchanging $x$ and $y$ gives
the reverse inequality, so $\lvert d(x,A)-d(y,A)\rvert\le d(x,y)$.

**(b)** If $d(x,A) = 0$ then for every $\varepsilon>0$ there is $a\in A$ with $d(x,a)<\varepsilon$, so
$B_\varepsilon(x)\cap A\ne\varnothing$; by Theorem 7.9.1(2), $x\in\overline A$. Conversely if
$x\in\overline A$ then every ball around $x$ meets $A$, so for every $\varepsilon>0$ there is $a\in A$ with
$d(x,a)<\varepsilon$, and the infimum is $0$.

**(c)** If $F = \varnothing$ take $U = \varnothing$ and $V = X$; if $G = \varnothing$ take $U = X$ and
$V = \varnothing$. Otherwise both are nonempty. By (a), $h(x) = d(x,F)-d(x,G)$ satisfies
$\lvert h(x)-h(y)\rvert\le 2d(x,y)$, so $h$ is continuous. Hence
$U = h^{-1}\big((-\infty,0)\big)$ and $V = h^{-1}\big((0,\infty)\big)$ are open, and they are disjoint
since no real number is both negative and positive. If $x\in F$ then $d(x,F) = 0$ by (b) and
$d(x,G)>0$ because $x\notin G$ and $G$ is closed, so $h(x)<0$ and $x\in U$. Symmetrically $G\subseteq V$.

**(d)** $T_1$: for $x\ne y$ the balls $B_r(x)$ and $B_r(y)$ with $r = d(x,y)/2>0$ are disjoint open sets
separating them (and $\{y\}$ is closed because $d(x,\{y\}) = d(x,y)>0$ for $x\ne y$). $T_4$: (c) shows that
disjoint closed sets can be separated by disjoint open sets, and $T_1$ was just proved.

### Solution 27

**(a)** Suppose $x_n\to x$ and $x_n\to y$ with $x\ne y$. Choose disjoint open $U\ni x$, $V\ni y$. There are
$n_1,n_2$ with $x_n\in U$ for $n\ge n_1$ and $x_n\in V$ for $n\ge n_2$. For $n\ge\max(n_1,n_2)$ we get
$x_n\in U\cap V = \varnothing$, a contradiction.

**(b)** Let $k\in\mathbb{N}$ and let $N$ be a neighbourhood of $k$. Then $N$ contains a cofinite open
$U\ni k$, so $\mathbb{N}\setminus U$ is a finite set of integers; let $m = \max(\mathbb{N}\setminus U)$
(with $m = 0$ if the set is empty). For $n>m$ we have $n\in U\subseteq N$, so $x_n = n\to k$. As $k$ was
arbitrary, the sequence converges to every point.

**(c)** In the Sierpiński space $\mathbb{S} = \{0,1\}$ with open sets $\varnothing,\{1\},\{0,1\}$, the
constant sequence $x_n = 1$ converges to $1$ (every neighbourhood of $1$ contains $1$) and also to $0$
(the only neighbourhood of $0$ is $\{0,1\}$, which contains every term). These are all the points of the
space, so the sequence converges to exactly two distinct points. The space is not Hausdorff, as
Theorem 7.10.2 requires.

### Solution 28

**(a)** Suppose $X$ is $T_1$ and $x\in X$. For each $y\ne x$ choose open $U_y$ with $y\in U_y$ and
$x\notin U_y$. Then $X\setminus\{x\} = \bigcup_{y\ne x}U_y$ is open, so $\{x\}$ is closed. Conversely, if
every singleton is closed and $x\ne y$, then $X\setminus\{y\}$ is open, contains $x$ and not $y$, and
$X\setminus\{x\}$ is open, contains $y$ and not $x$; this is $T_1$.

**(b)** $T_2\Rightarrow T_1$: disjoint open $U\ni x$, $V\ni y$ give an open set containing $x$ and not $y$,
and one containing $y$ and not $x$. $T_1\Rightarrow T_0$: the open set witnessing $T_1$ for the ordered pair
$(x,y)$ contains exactly one of $x,y$.

**(c)** $T_3\Rightarrow T_2$: let $x\ne y$. By $T_1$ and (a), $\{y\}$ is closed, and $x\notin\{y\}$.
Regularity gives disjoint open $U\ni x$ and $V\supseteq\{y\}$, so $U,V$ are disjoint open neighbourhoods of
$x$ and $y$. $T_4\Rightarrow T_3$: let $F$ be closed and $x\notin F$. By $T_1$, $\{x\}$ is closed and
disjoint from $F$; normality gives disjoint open $U\supseteq\{x\}$ and $V\supseteq F$.

### Solution 29

**(a)** (C1): $V(\{1\}) = \varnothing$ because $1$ never vanishes, and $V(\varnothing) = \mathbb{R}^2$
because the condition is vacuous. (C2): a point satisfies every $f\in\bigcup_i S_i$ iff it satisfies every
$f\in S_i$ for every $i$, so $\bigcap_i V(S_i) = V\big(\bigcup_i S_i\big)$. (C3): with
$ST = \{fg : f\in S,\ g\in T\}$ we have $V(S)\cup V(T) = V(ST)$: if $p\in V(S)$ then all $f\in S$ vanish
at $p$, hence all products $fg$ vanish; symmetrically for $T$; conversely if $p\notin V(S)\cup V(T)$ there
are $f\in S$, $g\in T$ with $f(p)\ne0\ne g(p)$, so $(fg)(p)\ne0$ and $p\notin V(ST)$. By Theorem 7.2.1
these sets are the closed sets of a topology.

**(b)** For $p = (u,v)$, $\{p\} = V(\{x-u,\,y-v\})$ is closed. So singletons are closed and the space is
$T_1$ (Theorem 7.11.2).

**(c)** Let $U = \mathbb{R}^2\setminus V(S)$ and $W = \mathbb{R}^2\setminus V(T)$ be nonempty. Choose
$p\in U$; then $p\notin V(S)$, so some $f\in S$ satisfies $f(p)\ne0$, and in particular $f$ is not the
zero polynomial. Similarly choose a nonzero $g\in T$. Now
$V(S)\cup V(T)\subseteq V(f)\cup V(g) = V(fg)$, and $fg$ is not the zero polynomial, so $V(fg)\ne\mathbb{R}^2$.
To see the last point: write $f = \sum_{i=0}^{d}a_i(x)y^i$ with some coefficient $a_i\ne0$; since a
nonzero one-variable polynomial has finitely many roots, choose $x_0$ with $a_i(x_0)\ne0$; then
$y\mapsto f(x_0,y)$ is a nonzero polynomial, so there is $y_0$ with $f(x_0,y_0)\ne0$. Hence

$$
U\cap W = \mathbb{R}^2\setminus\big(V(S)\cup V(T)\big)\supseteq\mathbb{R}^2\setminus V(fg)\ne\varnothing,
$$

so any two nonempty open sets meet and the space is not Hausdorff.

### Solution 30

**(a)** The $n$-th component of $D$ is $\pi_n\circ D = \mathrm{id}_{\mathbb{R}}$, which is continuous. By
the characteristic property of the product topology (Theorem 7.7.2), $D$ is continuous.

**(b)** Let $B = \prod_{n\in\mathbb{N}}\big(-1/n,\,1/n\big)$, which is open in the box topology. Then

$$
D^{-1}[B] = \{t\in\mathbb{R} : \lvert t\rvert<1/n \text{ for every } n\} = \{0\},
$$

because for $t\ne0$ some $1/n\le\lvert t\rvert$. But $\{0\}$ is not open in $\mathbb{R}$, so $D$ is not
continuous for the box topology.

**(c)** The set $B$ of (b) is box-open. It contains no product-basic set around $(0,0,\dots)$: a
product-basic set fixes only finitely many coordinates, so it contains a point $(0,\dots,0,N,0,\dots)$
with $N>1$ in a free coordinate, and that point is not in $B$. Hence $B$ is not open in the product
topology, and the box topology is strictly finer.

### Solution 31

Write $q : X\to Y$ for the quotient map, $0_0 = q(0,0)$, $0_1 = q(0,1)$.

*$T_1$.* For $x\ne0$ the class $[x]$ has preimage $(\mathbb{R}\setminus\{x\})\times\{0,1\}$, which is open
in $X$; and $q^{-1}(Y\setminus\{0_0\}) = (\mathbb{R}\setminus\{0\})\times\{0,1\}$ is open. So every class
is closed, and the quotient is $T_1$.

*Not Hausdorff.* Let $V\ni0_0$ and $W\ni0_1$ be open in $Y$. Then $q^{-1}[V]$ is an open neighbourhood of
$(0,0)$, so it contains $(-\varepsilon,\varepsilon)\times\{0\}$ for some $\varepsilon>0$; similarly
$q^{-1}[W]\supseteq(-\delta,\delta)\times\{1\}$. For $0<\lvert x\rvert<\min(\varepsilon,\delta)$ we have
$q(x,0) = [x] = q(x,1)\in V\cap W$. So $V\cap W\ne\varnothing$.

*Not metrisable.* Every metrisable space is Hausdorff (Theorem 7.11.4), and $Y$ is not. Note also that
$X$ is metrisable (it is a subspace of $\mathbb{R}^2$), so this is a quotient of a metrisable space that
is not metrisable.

## Challenge

### Solution 32

**(a)** Let $\mathcal{B} = \{B_n : n\in\mathbb{N}\}$ be a countable base and $\mathcal{C}$ any base. For
each pair $(n,m)$ such that $B_n\subseteq B_m$ and such that some member $C\in\mathcal{C}$ satisfies
$B_n\subseteq C\subseteq B_m$, choose one such $C$ and call it $C_{n,m}$. The resulting family
$\mathcal{C}'$ is countable (it is indexed by a subset of $\mathbb{N}^2$).

*$\mathcal{C}'$ is a base.* Let $x\in U$ with $U$ open. Choose $m$ with $x\in B_m\subseteq U$ (using that
$\mathcal{B}$ is a base), then $C\in\mathcal{C}$ with $x\in C\subseteq B_m$ (using that $\mathcal{C}$ is a
base), then $n$ with $x\in B_n\subseteq C$ (using $\mathcal{B}$ again). Then $B_n\subseteq C\subseteq B_m$,
so $C_{n,m}$ is defined and $x\in B_n\subseteq C_{n,m}\subseteq B_m\subseteq U$. So every point of every
open set has a member of $\mathcal{C}'$ between it and the open set.

**(b)** Every open set is a union of members of the countable base $\mathcal{B}$, hence is determined by
the subset of $\mathcal{B}$ consisting of its members. The map $U\mapsto\{B\in\mathcal{B} : B\subseteq U\}$
is injective from $\tau$ into $\mathcal{P}(\mathcal{B})$, so
$\lvert\tau\rvert\le 2^{\lvert\mathcal{B}\rvert} = 2^{\aleph_0}$.

### Solution 33

**(i) $\Rightarrow$ (ii).** Suppose $X$ is Hausdorff and $(x,y)\notin\Delta$, so $x\ne y$. Choose disjoint
open $U\ni x$, $V\ni y$. Then $U\times V$ is an open neighbourhood of $(x,y)$ in $X\times X$ and it is
disjoint from $\Delta$: if $(z,z)\in U\times V$ then $z\in U\cap V = \varnothing$. So
$X\times X\setminus\Delta$ is open and $\Delta$ is closed.

**(ii) $\Rightarrow$ (iii).** The map $h : Y\to X\times X$, $h(y) = (f(y),g(y))$, has continuous components,
so by Theorem 7.7.2 it is continuous. Then $E = h^{-1}[\Delta]$ is the preimage of a closed set under a
continuous map, hence closed.

**(iii) $\Rightarrow$ (i).** Take $Y = X\times X$ and $f = \pi_1$, $g = \pi_2$, both continuous. Their
equaliser is $E = \{(x,y) : x = y\} = \Delta$, which is closed by (iii). By Proposition 7.10.5 a space with
closed diagonal is Hausdorff.

### Solution 34

**(a)** $x\preceq x$ because $x\in\{x\}\subseteq\overline{\{x\}}$. For transitivity, suppose $x\preceq y$ and
$y\preceq z$, i.e. $x\in\overline{\{y\}}$ and $y\in\overline{\{z\}}$. Since $\overline{\{z\}}$ is a closed
set containing $y$, and $\overline{\{y\}}$ is the smallest closed set containing $y$, we get
$\overline{\{y\}}\subseteq\overline{\{z\}}$, hence $x\in\overline{\{z\}}$, i.e. $x\preceq z$.

**(b)** *$T_0$ implies antisymmetry.* Suppose $x\preceq y$ and $y\preceq x$ with $x\ne y$. By $T_0$ there is
an open $U$ containing exactly one of them; say $x\in U$, $y\notin U$. Since $x\in\overline{\{y\}}$ and $U$
is an open neighbourhood of $x$, we get $U\cap\{y\}\ne\varnothing$, i.e. $y\in U$, a contradiction. The
case $y\in U$, $x\notin U$ is symmetric.

*Antisymmetry implies $T_0$.* Suppose $x\ne y$ cannot be separated: every open set contains $x$ iff it
contains $y$. Then every open neighbourhood of $x$ contains $y$, so $x\in\overline{\{y\}}$; and every
open neighbourhood of $y$ contains $x$, so $y\in\overline{\{x\}}$. Antisymmetry forces $x = y$, contrary
to hypothesis.

**(c)** *Alexandrov.* A finite set has only finitely many subsets, so an arbitrary family of open sets has
only finitely many distinct members $U_1,\dots,U_r$; its intersection equals $U_1\cap\cdots\cap U_r$,
which is open by (O3) and induction.

*Up-sets.* Let $U$ be open, $x\in U$ and $x\preceq y$. If $y\notin U$ then $X\setminus U$ is closed and
contains $y$, so $\overline{\{y\}}\subseteq X\setminus U$ and $x\notin\overline{\{y\}}$, contradicting
$x\preceq y$. Hence $y\in U$: every open set is an up-set.

*Smallest neighbourhood.* Let $S_y = \{x : y\preceq x\}$. It is open: it is the intersection of all open
sets containing $y$ — indeed each such open set is an up-set containing $y$, hence contains $S_y$; and
$S_y$ itself is open because it is the intersection of the finite family of open sets containing $y$
(Alexandrov property). Hence $S_y$ is the smallest open set containing $y$ (note $y\in S_y$ by
reflexivity).

**(d)** *$\tau$ determines $\preceq$* by definition. *$\preceq$ determines $\tau$:* every
$\overline{\{y\}} = \{x : x\preceq y\}$ is determined by $\preceq$, and since $X$ is finite, for any
$A\subseteq X$ the set $A$ is finite and by (K4)
$\overline A = \bigcup_{y\in A}\overline{\{y\}}$. Hence the closure of every set, and therefore the
family of closed sets (the fixed points of the closure), is determined by $\preceq$.

*Every preorder arises.* Let $\preceq$ be a preorder on the finite set $X$ and let $\tau$ be the family of
up-sets: $U\in\tau$ iff $x\in U$ and $x\preceq y$ imply $y\in U$. Then $\varnothing$ and $X$ are up-sets;
unions and intersections of up-sets are up-sets (for an intersection, if $x$ is in all of them and
$x\preceq y$, then $y$ is in all of them), so $\tau$ is a topology. Its specialisation order
$\preceq'$ satisfies $x\preceq'y$ iff $x\in\overline{\{y\}}$ iff every up-set containing $x$ contains $y$.
This holds when $x\preceq y$, because up-sets are upward closed. Conversely, if $x\not\preceq y$, the
up-set $S = \{z : x\preceq z\}$ contains $x$ (reflexivity) and does not contain $y$; so
$x\notin\overline{\{y\}}$. Hence $\preceq' = \preceq$, and the two constructions are mutually inverse.
So topologies on a finite set correspond bijectively to preorders on it.

### Solution 35

**(a)** Let $(X_n,d_n)$ be metrisable for each $n$; replacing $d_n$ by $\min(d_n,1)$ does not change the
topology, so assume $d_n\le1$ and put

$$
d(x,y) = \sum_{n=1}^{\infty}2^{-n}d_n(x_n,y_n).
$$

The series converges since each term is at most $2^{-n}$, and $d$ is a metric: definiteness because
$d(x,y) = 0$ forces every $d_n(x_n,y_n) = 0$, symmetry is clear, and the triangle inequality follows from
the triangle inequality in each summand after summing.

*Product $\subseteq$ $d$-topology.* Let $x\in\prod_n U_n$ with $U_n = X_n$ for $n>N$ and $U_n$ open in
$X_n$ for $n\le N$. Choose $\varepsilon_n>0$ with $B^{d_n}_{\varepsilon_n}(x_n)\subseteq U_n$ for $n\le N$
and put $\delta = \min_{n\le N}2^{-n}\varepsilon_n>0$. If $d(x,y)<\delta$ then for $n\le N$,
$2^{-n}d_n(x_n,y_n)\le d(x,y)<\delta\le2^{-n}\varepsilon_n$, so $d_n(x_n,y_n)<\varepsilon_n$ and
$y_n\in U_n$. Hence $B^d_\delta(x)\subseteq\prod_n U_n$.

*$d$-topology $\subseteq$ product.* Let $\varepsilon>0$ and choose $N$ with
$\sum_{n>N}2^{-n}<\varepsilon/2$. Put $\delta_n = \varepsilon/(2(N+1))$ for $n\le N$ and let
$V = \prod_n V_n$ with $V_n = B^{d_n}_{\delta_n}(x_n)$ for $n\le N$ and $V_n = X_n$ otherwise; this is a
product-basic neighbourhood of $x$. If $y\in V$ then

$$
d(x,y)\le\sum_{n\le N}2^{-n}\delta_n + \sum_{n>N}2^{-n} \le \frac{\varepsilon}{2(N+1)}\sum_{n\le N}2^{-n} + \frac{\varepsilon}{2} \le \frac{\varepsilon}{2}+\frac{\varepsilon}{2} = \varepsilon .
$$

So $V\subseteq B^d_\varepsilon(x)$ and the two topologies coincide.

**(b)** Let $I$ be uncountable and consider $\mathbb{R}^I$ with the product topology at the point $0$.
Suppose $\{U_k\}_{k\in\mathbb{N}}$ is a countable neighbourhood base at $0$. Each $U_k$ contains a basic
open set $B_k = \prod_i V^k_i$, where $V^k_i = \mathbb{R}$ for all $i$ outside a finite set $F_k$. Then
$F = \bigcup_k F_k$ is countable, and since $I$ is uncountable there is $j\in I\setminus F$. The set
$W = \pi_j^{-1}\big((-1,1)\big)$ is an open neighbourhood of $0$. If $U_k\subseteq W$ for some $k$, then
$B_k\subseteq W$; but $B_k$ imposes no condition on the $j$-th coordinate, so it contains the point $y$
with $y_j = 2$ and $y_i = 0$ for $i\ne j$, and $y\notin W$ — contradiction. Hence no $U_k$ is contained
in $W$, the family is not a base at $0$, and $\mathbb{R}^I$ is not first countable. Since every metrisable
space is first countable, $\mathbb{R}^I$ is not metrisable.

### Solution 36

**(a)** Suppose $\{U_n\}_{n\in\mathbb{N}}$ is a countable neighbourhood base at $x$. Each $U_n$ is
nonempty (it contains $x$), so $X\setminus U_n$ is countable. Then
$C = \bigcup_n(X\setminus U_n)$ is countable, and so is $C\cup\{x\}$; since $X$ is uncountable, choose
$y\in X\setminus(C\cup\{x\})$. Then $V = X\setminus\{y\}$ is open (its complement is a singleton) and
contains $x$. If $U_n\subseteq V$ for some $n$, then $y\notin U_n$, so $y\in X\setminus U_n\subseteq C$,
contrary to the choice of $y$. So no $U_n$ is contained in $V$, and the family is not a base at $x$.

**(b)** Let $(a_n)$ be a sequence in $X$.

*Infinite range.* Suppose the set $R = \{a_n : n\in\mathbb{N}\}$ is infinite, and let $x\in X$. For an open
$U\ni x$, the set $X\setminus U$ is countable, so only countably many values of the sequence lie outside
$U$; since the values in $R\cap(X\setminus U)$ are distinct, only finitely many indices $n$ satisfy
$a_n\notin U$. Hence $a_n\in U$ for all sufficiently large $n$, and $a_n\to x$. As $x$ was arbitrary, the
sequence converges to every point.

*Finite range.* Suppose $R$ is finite and $a_n\to x$. The set $U = X\setminus(R\setminus\{x\})$ is
co-countable (its complement is finite), hence open, and contains $x$. So $a_n\in U$ eventually, and since
every $a_n\in R$, this says $a_n = x$ eventually. Conversely an eventually constant sequence with value
$x$ converges to $x$. So a finite-range sequence converges exactly to those points at which it is
eventually constant.

**(c)** Let $A$ be countably infinite. Then $X\setminus A$ is co-countable, hence open, so $A$ is closed
and $\overline A = A$. Enumerate $A = \{a_1,a_2,\dots\}$ with distinct terms; by (b) the sequence
$(a_n)$ has infinite range and therefore converges to every point of $X$, in particular to every point of
$X\setminus A$. Those points do not lie in $\overline A = A$. So "there is a sequence in $A$ converging to
$x$" does not imply "$x\in\overline A$".

Both implications of the sequential description of the closure therefore fail in general: here a sequence
can escape the closure of its index set, while in the ordinal space of Remark 7.9.6 a point of the closure
can be unreachable by sequences. First countability is exactly the hypothesis that makes sequences
adequate, and the present space fails it by (a) even though it is $T_1$.
