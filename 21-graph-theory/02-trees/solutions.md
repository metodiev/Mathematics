# Trees — Solutions

> [Trees](README.md) · Solutions to the 36 problems in [exercises.md](exercises.md)

Each solution states the strategy, then carries out every step. Proofs cite the exact characterisation of Theorem 7.2.1 that is being used, because most errors in this subject come from silently assuming the wrong one.

## Beginner

**1.** *Strategy: use $m = n-1$ for a tree and $m = n-c$ for a forest (Theorem 7.2.1 and Lemma 7.2.4).*

(a) $17 - 1 = 16$ edges.
(b) $30 + 1 = 31$ vertices.
(c) $20 - 6 = 14$ edges.

**2.** *Strategy: count edges first, then check exactly one of connectivity and acyclicity.*

(a) $5$ edges $= 6-1$, and the graph is the path $1$–$2$–$3$–$4$–$5$–$6$, which is connected. By (T2), a tree. **Tree.**

(b) $6$ edges $= n$, not $n-1$, so it is not a tree; indeed $1$–$2$–$3$–$4$–$5$–$6$–$1$ is a cycle. **Not a tree.**

(c) $5$ edges $= 6-1$, and the graph is the star $K_{1,5}$ with centre $1$; every edge uses vertex $1$, so there is no cycle. **Tree.**

(d) $5$ edges $= 6-1$. Connectivity: $1$–$2$–$4$–$6$ and $1$–$3$–$5$ reaches all six vertices. A connected graph with $n-1$ edges is a tree by (T2)$\Rightarrow$(T1). **Tree.**

(e) $4$ edges $< 5 = n-1$, so the graph cannot be connected; indeed vertex $6$ is isolated and $2,3,4,5$ are leaves at $1$. **Not a tree.**

**3.** *Strategy: classify by the largest degree, which is at most $4$.*

The three shapes are:

* the path $P_5$: degrees $(2,2,2,1,1)$;
* the star $K_{1,4}$: degrees $(4,1,1,1,1)$;
* the "T" shape, one vertex of degree $3$ with one of its neighbours of degree $2$: degrees $(3,2,1,1,1)$.

No other shape exists: if $\Delta = 4$ the graph is the star; if $\Delta = 3$ the tree is a spider with three legs whose lengths sum to $4$, giving legs $(1,1,2)$ up to order — that is the T shape; if $\Delta \le 2$ the tree is a path. So there are exactly three unlabelled trees on five vertices.

Labelling counts, from Corollary 7.9.6:

* $P_5$: $5!/2 = 60$ (a path is determined by the order of its vertices up to reversal);
* $K_{1,4}$: $5$ (the choice of centre);
* T shape: $\binom{5}{1}\binom{4}{1}\cdot\frac{3!}{2!\,1!} = 20\cdot 3 = 60$.

Total $60+5+60 = 125 = 5^3$, in agreement with Cayley's formula by Theorem 7.9.1.

**4.** *Strategy: split the $16$ trees by degree sequence.*

A tree on four vertices has $3$ edges and degree sum $6$, so the possible degree multisets are $(3,1,1,1)$ and $(2,2,1,1)$.

* $(3,1,1,1)$: the star $K_{1,3}$. Choose the centre in $4$ ways, and the tree is determined. By Corollary 7.9.6 a fixed labelled sequence has $2!/2! = 1$ tree, so there are $4$ stars.
* $(2,2,1,1)$: the path $P_4$. Choose the two vertices of degree $2$: $\binom{4}{2} = 6$ ways; for each, the number of trees is $2!/(1!\,1!) = 2$ (the two degree-$2$ vertices can be joined to the leaves in two ways, giving the two orders along the path). Total $6 \cdot 2 = 12$ paths.

Total $4 + 12 = 16 = 4^2$ ✓.

**5.** *Strategy: repeatedly delete the smallest leaf, recording its neighbour.*

The degrees are $\deg(1) = 3$ (neighbours $2,3,4$), $\deg(2) = 3$ ($1,5,6$), $\deg(3) = 2$ ($1,7$), $\deg(4) = 2$ ($1,8$), and $5,6,7,8$ are leaves.

| Step | Current leaves | Smallest leaf | Recorded neighbour | Remaining edges |
|---|---|---|---|---|
| 1 | $5,6,7,8$ | $5$ | $2$ | $12,13,14,26,37,48$ |
| 2 | $6,7,8$ | $6$ | $2$ | $12,13,14,37,48$ |
| 3 | $2,7,8$ | $2$ | $1$ | $13,14,37,48$ |
| 4 | $7,8$ | $7$ | $3$ | $13,14,48$ |
| 5 | $3,8$ | $3$ | $1$ | $14,48$ |
| 6 | $1,8$ | $1$ | $4$ | $48$ (two vertices left, stop) |

Note the third step: after deleting $5$ and $6$, the vertex $2$ has become a leaf and is smaller than $7$ and $8$, so it is deleted next. So $P(T) = (2,\,2,\,1,\,3,\,1,\,4)$. Check with Lemma 7.9.2: $1$ occurs twice and $\deg(1) = 3$ ✓; $2$ occurs twice and $\deg(2) = 3$ ✓; $3$ and $4$ occur once each and have degree $2$ ✓; $5,6,7,8$ occur zero times and have degree $1$ ✓. Also the length is $6 = 8-2$ ✓.

**6.** *Strategy: apply Algorithm 7.9.4 literally; at every step the smallest label absent from the remaining word.*

$U = \{1,\dots,7\}$ and $P = (5,3,1,3,5)$.

| Step | Remaining word | Labels of $U$ absent from it | Smallest | Edge |
|---|---|---|---|---|
| 1 | $(5,3,1,3,5)$ | $2,4,6,7$ | $2$ | $25$ |
| 2 | $(3,1,3,5)$ | $4,6,7$ | $4$ | $43$ |
| 3 | $(1,3,5)$ | $6,7$ | $6$ | $61$ |
| 4 | $(3,5)$ | $1,7$ | $1$ | $13$ |
| 5 | $(5)$ | $3,7$ | $3$ | $35$ |
| final | — | $\{5,7\}$ remain | — | $57$ |

The edges are $25, 34, 16, 13, 35, 57$: six edges on seven vertices ✓. Degrees:
$$\deg(1)=2\ (6,3),\ \deg(2)=1,\ \deg(3)=3\ (4,1,5),\ \deg(4)=1,\ \deg(5)=3\ (2,3,7),\ \deg(6)=1,\ \deg(7)=1 .$$
Check against Lemma 7.9.2: $5$ occurs twice, degree $3$ ✓; $3$ occurs twice, degree $3$ ✓; $1$ occurs once, degree $2$ ✓; $2,4,6,7$ occur zero times, degree $1$ ✓. The graph is connected (each vertex is joined to a vertex that survives longer, ending with the edge $57$) and has $n-1$ edges, so it is a tree ✓.

**7.** *Strategy: compute depths by breadth-first from the root; a vertex's parent is its neighbour at depth one less.*

Edges: $12, 13, 24, 25, 36, 47, 48$, root $1$.

| Vertex | Parent | Children | Depth |
|---|---|---|---|
| $1$ | — | $2,3$ | $0$ |
| $2$ | $1$ | $4,5$ | $1$ |
| $3$ | $1$ | $6$ | $1$ |
| $4$ | $2$ | $7,8$ | $2$ |
| $5$ | $2$ | — | $2$ |
| $6$ | $3$ | — | $2$ |
| $7$ | $4$ | — | $3$ |
| $8$ | $4$ | — | $3$ |

The leaves are $5,6,7,8$; the internal vertices are $1,2,3,4$; the height is $\max_v\operatorname{depth}(v) = 3$. The subtree rooted at $4$ is the tree on $\{4,7,8\}$ with edges $47, 48$.

**8.** *Strategy: Proposition 7.4.4, $L = i+1$ and $n = 2i+1$.*

(a) With $i = 8$ internal vertices, $L = 9$ leaves and $n = 17$ vertices.

(b) $2i + 1 = 21$ gives $i = 10$, hence $L = 11$.

**9.** *Strategy: Proposition 7.4.3.*

(a) At most $2^4 = 16$ leaves (attained by the perfect binary tree of height $4$, all of whose $16$ leaves are at depth $4$).

(b) At most $2^{5} - 1 = 31$ vertices (the perfect tree of height $4$).

(c) The bound $n \le 2^{h+1}-1$ with $n = 20$ gives $2^{h+1} \ge 21$. Since $2^4 = 16 < 21 \le 32 = 2^5$, we need $h+1 \ge 5$, that is $h \ge 4$. The bound is attained, for instance, by putting $16$ vertices on levels $0$–$3$ and $4$ more on level $4$.

**10.** *Strategy: a spanning tree has $n-1$ edges.*

* $P_4$: the graph itself is a tree, so its only spanning tree is $P_4$. Count $1$.
* $K_3$: $3$ edges and $3$ vertices; a spanning tree is any $2$ edges, and all three pairs are connected and acyclic. Count $3$.
* $C_5$: $5$ edges; a spanning tree needs $4$, so exactly one edge is deleted, giving $5$ possibilities. Count $5$.

**11.** *Strategy: sort, then add every edge whose endpoints are in different current components.*

Sorted order: $25\,(1)$, $12\,(2)$, $23\,(3)$, $14\,(4)$, $34\,(5)$, $24\,(6)$, $13\,(7)$, $35\,(8)$.

| Step | Edge | Weight | Components before | Cycle? | Action |
|---|---|---|---|---|---|
| 1 | $25$ | $1$ | $\{1\},\{2\},\{3\},\{4\},\{5\}$ | no | add |
| 2 | $12$ | $2$ | $\{2,5\},\{1\},\{3\},\{4\}$ | no | add |
| 3 | $23$ | $3$ | $\{1,2,5\},\{3\},\{4\}$ | no | add |
| 4 | $14$ | $4$ | $\{1,2,3,5\},\{4\}$ | no | add |

After four edges the five vertices are connected, so the algorithm stops. The output is
$$F = \{25, 12, 23, 14\}, \qquad w(F) = 1+2+3+4 = 10 .$$

*Why optimal.* Each chosen edge is a lightest edge across the cut defined by the component it joined: $25$ is lightest at $\{5\}$ (weights $1$ versus $35$'s $8$); $12$ is lightest at $\{1\}$ (weights $2,7,4$); $23$ is lightest at $\{3\}$ (weights $3, 7, 5, 8$); $14$ is lightest at $\{4\}$ (weights $4, 6$). By Lemma 7.6.2 each is safe, so the result is an MST.

**12.** *Strategy: grow a set $S$ from $3$, always taking the lightest edge leaving $S$.*

| Step | $S$ | Edges leaving $S$ (weight) | Chosen |
|---|---|---|---|
| 1 | $\{3\}$ | $23(3), 13(7), 34(5), 35(8)$ | $23$ |
| 2 | $\{2,3\}$ | $12(2), 25(1), 24(6), 13(7), 34(5), 35(8)$ | $25$ |
| 3 | $\{2,3,5\}$ | $12(2), 24(6), 13(7), 34(5), 35(8)$ | $12$ |
| 4 | $\{1,2,3,5\}$ | $14(4), 24(6), 34(5)$ | $14$ |

Output $\{23, 25, 12, 14\}$ with weight $3+1+2+4 = 10$: the same tree as Kruskal's. The two algorithms *must* agree here because all nine edge weights are distinct, so the minimum spanning tree is unique (Corollary 7.6.4); any algorithm that returns an MST returns this one.

## Intermediate

**13.** *Strategy: check both halves of the definition separately.*

Let $T$ be a tree with $n \ge 2$ and let $\ell$ be a leaf, so $\deg(\ell) = 1$ with unique neighbour $w$.

*Acyclic.* $T - \ell$ is a subgraph of $T$, and every cycle of a subgraph would be a cycle of $T$. Since $T$ has none, neither does $T - \ell$.

*Connected.* Let $x, y$ be vertices of $T - \ell$. Since $T$ is connected there is a simple $x$–$y$ path $P$. If $\ell$ appeared on $P$ as an internal vertex, $P$ would use two distinct edges incident with $\ell$ (one to enter and one to leave), contradicting $\deg(\ell) = 1$. Since $\ell \ne x, y$, the path $P$ avoids $\ell$ entirely and is a path in $T - \ell$.

Hence $T - \ell$ is connected and acyclic on $n-1$ vertices: a tree. $\blacksquare$

**14.** *Strategy: delete a cycle edge and contradict the edge bound.*

Let $G$ be connected with $n$ vertices and $n-1$ edges, and suppose $G$ contains a cycle $C$. Choose an edge $e$ of $C$. The endpoints of $e$ remain joined along the rest of $C$, so $G - e$ is still connected; it has $n$ vertices and $n-2$ edges. But every connected graph on $n$ vertices has at least $n-1$ edges (Theorem 7.6.4 of [Graph Basics](../01-graph-basics/README.md) with $c = 1$, or Corollary 7.5.2 above). Contradiction. Hence $G$ is acyclic. $\blacksquare$

**15.** *Strategy: combine the handshake lemma with $\sum_k n_k = n$.*

**Proof of the identity.** From Theorem 7.2.1 and the handshake lemma,
$$2(n-1) = 2m = \sum_v \deg(v) = n_1 + 2n_2 + \sum_{k\ge3} k\,n_k .$$
Also $n = n_1 + n_2 + \sum_{k\ge3} n_k$, so $2(n-1) = 2n_1 + 2n_2 + 2\sum_{k\ge3}n_k - 2$. Equating:
$$n_1 + 2n_2 + \sum_{k\ge3} k\,n_k = 2n_1 + 2n_2 + 2\sum_{k\ge3} n_k - 2 .$$
Cancelling $2n_2$ and moving terms,
$$n_1 = 2 + \sum_{k\ge3}(k-2)\,n_k . \qquad\blacksquare$$

**Construction.** Take $V = \{a,b,c,d,e,f,g,h,j\}$ and
$$E = \{ab,\ ac,\ ad,\ ae,\ bf,\ bg,\ fh,\ cj\}.$$
The graph is connected with $9$ vertices and $8$ edges, hence a tree. Its degrees are $\deg(a) = 4$, $\deg(b) = 3$, $\deg(c) = 2$, $\deg(f) = 2$, and $\deg(d) = \deg(e) = \deg(g) = \deg(h) = \deg(j) = 1$. So $n_4 = 1$, $n_3 = 1$, $n_2 = 2$, $n_1 = 5$, and
$$2 + (4-2)\cdot 1 + (3-2)\cdot 1 = 2+2+1 = 5 = n_1 \checkmark .$$

**16.** *Strategy: one direction is (T4) of Theorem 7.2.1; for the other, a cycle would give two paths.*

*($\Rightarrow$)* A tree is connected and acyclic, so it satisfies (T1), and Theorem 7.2.1 gives (T4): exactly one simple path between every pair.

*($\Leftarrow$)* If there is exactly one path between every pair, the graph is connected (a path exists) and cannot contain a cycle: if $C$ were a cycle and $x \ne y$ two of its vertices, the two arcs of $C$ from $x$ to $y$ would be two distinct simple paths. So the graph is connected and acyclic, i.e. a tree. $\blacksquare$

**17.** *Strategy: every cycle must use the new edge, and deleting it leaves a path in $T$.*

Let $T$ be a tree and $u, v$ non-adjacent. By (T4) there is a unique simple $u$–$v$ path $P$ in $T$; then $P$ together with the edge $uv$ is a cycle of $T + uv$, so at least one cycle exists.

Conversely, let $C$ be any cycle of $T + uv$. Since $T$ itself is acyclic, $C$ uses the edge $uv$. Deleting $uv$ from $C$ leaves a $u$–$v$ path in $T$, which by uniqueness must be $P$. Hence $C = P + uv$, and there is exactly one cycle. $\blacksquare$

**18.** *Strategy: delete cycle edges one at a time.*

**Existence.** Let $G$ be connected. If $G$ has a cycle, choose one of its edges $e$; the endpoints of $e$ remain joined along the rest of the cycle, so $G - e$ is connected and has the same vertex set. Replace $G$ by $G - e$ and repeat. Each step decreases the number of edges by one, so after finitely many steps no cycle remains; the result is a connected spanning subgraph with no cycle, that is, a spanning tree. $\blacksquare$

**Edge bound.** The spanning tree has $n-1$ edges, and it is a subgraph of $G$, so $m(G) \ge n-1$. $\blacksquare$

**19.** *Strategy: the cut property applied to the cut $\{v\}$.*

The edges crossing the cut $\delta(\{v\})$ are exactly the edges incident with $v$. Let $e$ be a lightest of them. By Theorem 7.6.1 (cut property) applied to $S = \{v\}$, some MST contains $e$. $\blacksquare$

*Example with two MSTs.* Take $K_3$ with all three edges of weight $1$. Any two edges form a spanning tree of total weight $2$, and every spanning tree has two edges of weight $1$, so all three choices are minimum spanning trees. Ties are exactly what makes non-uniqueness possible (compare Corollary 7.6.4).

**20.** *Strategy: exchange along the cycle created by adding an edge of one tree to the other.*

Suppose $T_1 \ne T_2$ are both MSTs and all weights are distinct. The symmetric difference $T_1 \triangle T_2 = (T_1 \setminus T_2) \cup (T_2 \setminus T_1)$ is non-empty and finite, and because all weights are distinct it has a unique lightest edge $e$. Relabel so that $e \in E(T_1) \setminus E(T_2)$.

Add $e$ to $T_2$. By Proposition 7.5.4 there is a unique cycle $C$ in $T_2 + e$. The cycle cannot consist only of $T_1$-edges, because $T_1$ is acyclic; so $C$ contains some $f \in E(T_2) \setminus E(T_1)$. Now $f \in T_1 \triangle T_2$ and $f \ne e$, so by the choice of $e$ we have $w(f) > w(e)$.

Then $T_2 - f + e$ is a spanning tree with
$$w(T_2 - f + e) = w(T_2) - w(f) + w(e) < w(T_2),$$
contradicting the minimality of $T_2$. Hence $T_1 = T_2$. $\blacksquare$

**21.** *Strategy: run Kruskal, then verify the criterion of Example 9.8 edge by edge.*

Sorted edges: $13(1)$, $24(2)$, $35(3)$, $46(4)$, $12(5)$, $26(6)$, $34(7)$, $45(8)$, $56(9)$.

Kruskal accepts $13$, $24$, $35$, $46$, then $12$ (which merges the two three-vertex components), and stops after five edges:
$$T = \{13,\ 24,\ 35,\ 46,\ 12\}, \qquad w(T) = 1+2+3+4+5 = 15 .$$

*Verification by the local criterion.* Remove each tree edge and check that it is lightest across the resulting cut.

| Removed edge | Components of $T - e$ | Edges crossing the cut (weight) | Lightest |
|---|---|---|---|
| $13$ | $\{3,5\}$ and $\{1,2,4,6\}$ | $13(1)$, $34(7)$, $45(8)$, $56(9)$ | $13$ ✓ |
| $24$ | $\{2\}$ and the rest | $24(2)$, $12(5)$, $26(6)$ | $24$ ✓ |
| $35$ | $\{5\}$ and the rest | $35(3)$, $45(8)$, $56(9)$ | $35$ ✓ |
| $46$ | $\{6\}$ and the rest | $46(4)$, $26(6)$, $56(9)$ | $46$ ✓ |
| $12$ | $\{1,3,5\}$ and $\{2,4,6\}$ | $12(5)$, $34(7)$, $45(8)$, $56(9)$ | $12$ ✓ |

Every tree edge is lightest across its fundamental cut, so by the criterion of Example 9.8 the tree is an MST, with weight $15$.

**22.** *Strategy: count by the number of edges deleted, and control connectivity.*

**$C_n$.** A spanning tree has $n-1$ edges, so exactly one of the $n$ cycle edges is deleted. Deleting any one edge leaves the path $P_n$, which is connected and acyclic, so each of the $n$ deletions gives a spanning tree. Deleting two or more edges leaves at most $n-2$ edges and hence cannot span. Count: $n$.

**$K_{2,3}$.** Let the parts be $A = \{x,y\}$ and $B = \{a,b,c\}$; there are $3 \times 2 = 6$ edges and $5$ vertices, and every edge joins $A$ to $B$. A spanning tree has $4$ edges, so
$$\deg_T(x) + \deg_T(y) = 4,$$
and every vertex of $B$ must have degree at least $1$ (otherwise it would be isolated). Similarly $x$ and $y$ are not isolated, so $1 \le \deg_T(x), \deg_T(y) \le 3$, leaving only the three cases below.

*Case $\deg_T(x) = 1$, $\deg_T(y) = 3$:* choose the single neighbour of $x$ in $3$ ways; then $y$ must be joined to all three vertices of $B$. This gives $3$ trees, and each is connected with $4$ edges, hence a tree.
*Case $\deg_T(x) = 3$, $\deg_T(y) = 1$:* symmetrically $3$ trees.
*Case $\deg_T(x) = 2$, $\deg_T(y) = 2$:* choose the two neighbours of $x$ in $\binom{3}{2} = 3$ ways; the third vertex of $B$ must be a neighbour of $y$ (it would otherwise be isolated), and $y$ needs one more neighbour among the two already adjacent to $x$, giving $2$ choices. Total $3 \cdot 2 = 6$ trees.

Total $3 + 3 + 6 = 12$. As a check, the general formula for the number of spanning trees of $K_{m,n}$ gives $m^{n-1}n^{m-1} = 2^{2}\cdot 3^{1} = 12$ ✓.

## Advanced

**23.** *Strategy: run the cut property at every step, keeping the invariant "the current forest lies in some MST".*

**Claim.** Prim's algorithm returns a minimum spanning tree.

**Proof.**

*The output is a spanning tree.* After $k$ iterations, $\lvert S\rvert = k+1$ and $F$ has $k$ edges, each added edge having joined a new vertex to the tree on $S$. So $F$ is always a tree on $S$. The loop ends exactly when $S = V$ (the graph is connected, so as long as $S \ne V$ some edge leaves $S$, and the algorithm can proceed). Hence $F$ is a tree on all $n$ vertices with $n-1$ edges.

*The output is minimum.* We prove by induction on the number of iterations that $F$ is contained in some MST.

Initially $F = \varnothing$, and an MST exists because $G$ is connected and has finitely many spanning trees.

For the step, let $S$ be the current set and $F$ the current forest. Every edge of $F$ has both endpoints in $S$, so **no edge of $F$ crosses $\delta(S)$** — this is exactly the hypothesis of Lemma 7.6.2. The algorithm chooses an edge $e$ of minimum weight in $\delta(S)$. Lemma 7.6.2 then says that $F \cup \{e\}$ is contained in some MST.

At the end $F$ is a spanning tree contained in an MST $T$; since both have $n-1$ edges, $F = T$ and $F$ is minimum. $\blacksquare$

The cut property enters only through Lemma 7.6.2, which is the cut property with the extra bookkeeping that the already-chosen edges may be kept fixed.

**24.** *Strategy: exchange the heavy edge for a lighter one crossing the same cut.*

Let $C$ be a cycle and $e \in E(C)$ strictly heavier than every other edge of $C$. Suppose, for contradiction, that some minimum spanning tree $T$ contains $e$.

Delete $e$ from $T$. By Theorem 7.2.1, $(T1)\Rightarrow(T5)$, the edge $e$ is a bridge of $T$, so $T - e$ has exactly two components with vertex sets $S$ and $V \setminus S$; the edge $e$ crosses this cut.

Now $C - e$ is a path joining the two endpoints of $e$, hence a path from $S$ to $V\setminus S$. It must therefore use an edge $f$ with one endpoint in $S$ and one outside, and $f \ne e$. Because $f \in E(C)$ and $e$ is strictly heavier than every other edge of $C$, $w(f) < w(e)$.

Then $T - e + f$ is a spanning tree (removing an edge and adding one across the resulting cut reconnects the two components without creating a cycle) with
$$w(T - e + f) = w(T) - w(e) + w(f) < w(T),$$
contradicting the minimality of $T$. Hence no MST contains $e$. $\blacksquare$

**25.** *Strategy: transport the problem to Prüfer codes, where degrees become multiplicities.*

Let $d_1,\dots,d_n$ be positive integers with $\sum_i d_i = 2n-2$, and put $e_i = d_i - 1 \ge 0$. Then $\sum_i e_i = n-2$.

By Lemma 7.9.2, a labelled tree $T$ satisfies $\deg_T(i) = d_i$ for all $i$ exactly when its Prüfer code contains the symbol $i$ exactly $e_i$ times. By Theorem 7.9.1 the Prüfer map is a bijection between labelled trees and words of length $n-2$ over $\{1,\dots,n\}$, so the trees with the prescribed degrees correspond bijectively to the words with prescribed multiplicities.

The number of words of length $n-2$ in which symbol $i$ occurs $e_i$ times is the multinomial coefficient
$$\binom{n-2}{e_1, e_2, \dots, e_n} = \frac{(n-2)!}{e_1!\,e_2!\cdots e_n!} = \frac{(n-2)!}{\prod_{i=1}^{n}(d_i-1)!}. \qquad\blacksquare$$

*Check.* For $n = 5$ and $(d_1,\dots,d_5) = (4,1,1,1,1)$ the count is $3!/3! = 1$; for $(3,2,1,1,1)$ it is $3!/(2!\,1!) = 3$, matching Example 9.5.

**26.** *Strategy: sum the formula of Problem 25 over all admissible degree sequences and recognise the multinomial theorem.*

Every labelled tree has some degree sequence, and the classes for different sequences are disjoint, so
$$n^{n-2} = \sum_{\substack{d_i \ge 1\\ \sum_i d_i = 2n-2}} \frac{(n-2)!}{\prod_{i=1}^{n}(d_i-1)!}.$$
Substituting $e_i = d_i - 1$ turns the condition into $e_i \ge 0$ and $\sum_i e_i = n-2$, so
$$n^{n-2} = \sum_{\substack{e_i \ge 0\\ \sum_i e_i = n-2}} \frac{(n-2)!}{e_1!\,e_2!\cdots e_n!}.$$
The right-hand side is the multinomial expansion of
$$(1+1+\cdots+1)^{n-2}$$
with $n$ terms in the base: each monomial $\frac{(n-2)!}{\prod e_i!}x_1^{e_1}\cdots x_n^{e_n}$ evaluated at $x_1 = \cdots = x_n = 1$ contributes exactly the summand. The base sums to $n$, so the value is $n^{n-2}$, as required. $\blacksquare$

**27.** *Strategy: acyclic implies no odd cycle, and connectivity forces the colouring.*

**Bipartiteness.** A tree is acyclic, so it has no cycle at all, in particular no cycle of odd length. By the characterisation of bipartite graphs (Theorem 7.8.3 of [Graph Basics](../01-graph-basics/README.md)), a graph with no odd cycle is bipartite. Alternatively, colour by distance parity from any fixed vertex: adjacent vertices have distances of opposite parity, because a tree has unique paths (Theorem 7.2.1, (T4)).

**Uniqueness.** Let $(A,B)$ and $(A',B')$ be two bipartitions. Fix a vertex $r$. Either $r \in A \cap A'$ or $r \in A \cap B'$; in the second case interchange the names of $A'$ and $B'$, so we may assume $r \in A \cap A'$. Now let $v$ be any vertex. The unique $r$–$v$ path has length $d$; along it, colours alternate in any proper 2-colouring. Hence $v$ lies in the same part as $r$ in both bipartitions if $d$ is even, and in the opposite part in both if $d$ is odd. So $v \in A \Leftrightarrow v \in A'$, giving $A = A'$ and $B = B'$. $\blacksquare$

**28.** *Strategy: this is the equivalence $(T1)\Leftrightarrow(T5)$, but write both directions out.*

*($\Rightarrow$)* Let $G$ be a tree and $e \in E(G)$. Since $G$ is acyclic, $e$ lies on no cycle. If $G - e$ were connected, there would be a path in $G - e$ between the endpoints of $e$, and that path together with $e$ would be a cycle of $G$ — contradiction. Hence $G - e$ is disconnected and $e$ is a bridge.

*($\Leftarrow$)* Let $G$ be connected and suppose every edge is a bridge. If $G$ had a cycle, take an edge $e$ of that cycle: its endpoints remain joined along the rest of the cycle, so $G - e$ is connected and $e$ is not a bridge — contradiction. Hence $G$ is acyclic, and being connected it is a tree. $\blacksquare$

**29.** *Strategy: compare the two optimality conditions through the cut of the heaviest MST edge.*

**Every MST is a minimum bottleneck tree.** Let $T$ be an MST and let $B = \max_{e \in E(T)} w(e)$ be its bottleneck. Suppose some spanning tree $T'$ had bottleneck strictly smaller than $B$. Choose an edge $e \in E(T)$ with $w(e) = B$, and let $S$, $V\setminus S$ be the vertex sets of the two components of $T - e$. Since $T'$ is connected and spans, it has an edge $f$ crossing this cut; indeed the unique path in $T'$ between the endpoints of $e$ must cross the cut. Every edge of $T'$ has weight $< B = w(e)$, in particular $w(f) < w(e)$. Then $T - e + f$ is a spanning tree with
$$w(T-e+f) = w(T) - w(e) + w(f) < w(T),$$
contradicting the minimality of $T$. So no spanning tree has a smaller bottleneck, and $T$ is a minimum bottleneck spanning tree. $\blacksquare$

**The converse fails.** Take $V = \{1,2,3,4\}$ with edges
$$12:1,\quad 13:1,\quad 23:2,\quad 34:2,\quad 41:2 .$$
The minimum possible bottleneck is $2$, because the two edges of weight $1$ do not span all four vertices, so every spanning tree uses an edge of weight at least $2$. The tree
$$T' = \{12, 23, 34\}$$
is a path $1$–$2$–$3$–$4$ with weight $1+2+2 = 5$ and bottleneck $2$: it is a minimum bottleneck spanning tree. But the MST is $\{12, 13, 34\}$, of weight $1+1+2 = 4 < 5$. So a minimum bottleneck spanning tree need not be an MST.

**30.** *Strategy: induction on the number of edges that differ, using the fundamental cycle.*

Let $T_1 \ne T_2$ be spanning trees. Pick an edge $e \in E(T_1) \setminus E(T_2)$. Adding $e$ to $T_2$ creates a unique cycle $C$ (Proposition 7.5.4). The cycle contains some edge $f \in E(T_2) \setminus E(T_1)$: if every other edge of $C$ lay in $T_1$, then $C$ would be a subgraph of the acyclic graph $T_1$, which is impossible.

Define $S_1 = T_2 - f + e$. This is a spanning tree: it has $n$ vertices and $n-1$ edges, and it is connected. Indeed $f$ is a bridge of $T_2$, so $T_2 - f$ has exactly two components; since $f$ lies on the $x$–$y$ path $C - e$ in $T_2$, its removal puts $x$ and $y$ in different components, and adding the edge $e = xy$ reconnects exactly those two components. Hence $S_1$ is a spanning tree obtained from $T_2$ by one exchange.

Moreover
$$\lvert E(S_1) \cap E(T_1)\rvert = \lvert E(T_2) \cap E(T_1)\rvert + 1,$$
because $e \in E(T_1)$ is gained and $f \notin E(T_1)$ is lost. Repeating the argument with $S_1$ in place of $T_2$, the intersection with $T_1$ strictly increases at every step and is bounded by $n-1$, so after finitely many steps we reach a spanning tree equal to $T_1$. $\blacksquare$

## Challenge

**31.** *Strategy: maximum degree at most $2$ means Prüfer entries are distinct.*

By Lemma 7.9.2, $\deg(v) \le 2$ for every $v$ exactly when each symbol occurs at most once in the Prüfer code. So we must count words of length $n-2$ with pairwise distinct entries from an alphabet of size $n$. Choosing such a word amounts to choosing an ordered list of $n-2$ distinct symbols:
$$n(n-1)(n-2)\cdots\bigl(n-(n-2)+1\bigr) = \frac{n!}{(n-(n-2))!} = \frac{n!}{2} .$$
(For $n = 2$ the empty word is the only one, and $2!/2 = 1$ ✓.) $\blacksquare$

*Check for $n = 4$:* $4!/2 = 12$, and Example 9.5 found $12$ labelled paths on four vertices ✓.

*Remark.* A tree with maximum degree at most $2$ is a path, so this also says that there are $n!/2$ labelled paths on $n$ vertices: choose an ordering of the $n$ labels and identify each ordering with its reverse.

**32.** *Strategy: a vertex is a leaf exactly when it is absent from the Prüfer code; use linearity of expectation.*

By Lemma 7.9.2, $\deg(v) = 1 + \operatorname{occ}_P(v)$, so $v$ is a leaf exactly when it does not occur in $P$. Under the uniform distribution on trees, the Prüfer code is a uniformly random word of length $n-2$ over $n$ symbols (Theorem 7.9.1 is a bijection, so it preserves uniformity). Hence for a fixed $v$,
$$\Pr(v \text{ not in } P) = \left(\frac{n-1}{n}\right)^{n-2},$$
since each of the $n-2$ positions independently avoids $v$ with probability $(n-1)/n$. Writing $L = \sum_{v} \mathbf{1}_v$ for the indicator that $v$ is a leaf,
$$\mathbb{E}[L] = \sum_{v=1}^{n}\Pr(v \text{ is a leaf}) = n\left(\frac{n-1}{n}\right)^{n-2}. \qquad\blacksquare$$

*Check for $n = 4$:* $4\cdot(3/4)^{2} = 9/4 = 2.25$. Direct count: the $16$ trees are $4$ stars with $3$ leaves each ($12$ leaves) and $12$ paths with $2$ leaves each ($24$ leaves), so the average is $(12+24)/16 = 36/16 = 2.25$ ✓.

*Check for $n = 5$:* $5\cdot(4/5)^{3} = 320/125 = 2.56$. Direct count from Example 9.5: $5$ stars with $4$ leaves ($20$), $60$ trees of type $(3,2,1,1,1)$ with $3$ leaves ($180$) and $60$ trees of type $(2,2,2,1,1)$ with $2$ leaves ($120$); total $320$ over $125$ trees, average $2.56$ ✓.

**33.** *Strategy: build a Prüfer code with the right multiplicities.*

**Existence.** Let $d_1,\dots,d_n$ be positive integers with $\sum_i d_i = 2n-2$, and put $e_i = d_i - 1 \ge 0$. Then $\sum_i e_i = n-2$. Form any word $P$ of length $n-2$ containing the symbol $i$ exactly $e_i$ times (for example, write the symbols in increasing order, repeated according to their multiplicities). By Lemma 7.9.5 the decoder produces a tree $T$ with $P(T) = P$, and by Lemma 7.9.2, $\deg_T(i) = 1 + e_i = d_i$. So $T$ is the required tree. $\blacksquare$

**Construction for $(3,2,2,1,1,1)$ on $6$ vertices.** Here $e = (2,1,1,0,0,0)$, summing to $4 = 6-2$. Take
$$P = (1,1,2,3).$$
Decoding with $U = \{1,\dots,6\}$:

| Step | Remaining word | Smallest absent | Edge |
|---|---|---|---|
| 1 | $(1,1,2,3)$ | $4$ | $41$ |
| 2 | $(1,2,3)$ | $5$ | $51$ |
| 3 | $(2,3)$ | $1$ | $12$ |
| 4 | $(3)$ | $2$ | $23$ |
| final | — | $\{3,6\}$ | $36$ |

The tree has edges $\{14, 15, 12, 23, 36\}$ and degrees $\deg(1) = 3$, $\deg(2) = 2$, $\deg(3) = 2$, $\deg(4) = \deg(5) = \deg(6) = 1$, as required ✓.

**34.** *Strategy: read the bound off the leaf identity, then characterise equality.*

Let $T$ have $n \ge 2$ vertices and let $\Delta = \Delta(T)$.

*If $\Delta \ge 3$:* by Corollary 7.3.2,
$$n_1 = 2 + \sum_{k\ge3}(k-2)n_k .$$
The vertex of maximum degree contributes $\Delta - 2$ to the sum, and all summands are non-negative, so
$$n_1 \ge 2 + (\Delta-2) = \Delta .$$

*If $\Delta \le 2$:* every vertex has degree $1$ or $2$, and a connected graph with maximum degree at most $2$ is a path or a cycle; a tree cannot be a cycle, so $T$ is a path and $n_1 = 2 = \Delta$. $\blacksquare$

*Equality case.* For $\Delta \ge 3$, equality holds exactly when $\sum_{k\ge3}(k-2)n_k = \Delta - 2$, i.e. when the only vertex of degree $\ge 3$ is the one of degree $\Delta$; such trees are precisely the **spiders**: a central vertex of degree $\Delta$ with $\Delta$ internally disjoint paths (legs) radiating from it. A star $K_{1,\Delta}$ is the special case in which every leg has length $1$. For $\Delta \le 2$ every tree (a path) has $n_1 = 2 = \Delta$, so equality always holds.

**35.** *Strategy: track the decoder's state, prove the degree formula, then induct on the steps.*

Let $P = (p_1,\dots,p_{n-2})$ be a word over $\{1,\dots,n\}$ and $T = \mathrm{Dec}(P)$. Write $P_i = (p_i,\dots,p_{n-2})$ for the suffix starting at $i$, and $U_i$ for the set of unused labels just before step $i$; thus $U_1 = \{1,\dots,n\}$ and $U_i = \{1,\dots,n\} \setminus \{\ell_1,\dots,\ell_{i-1}\}$.

**(i) The suffix decodes the remaining tree.** The edges added at steps $i, i+1, \dots, n-2$, together with the final edge, form exactly the tree that the decoder would construct from $P_i$ starting with the label set $U_i$. This is immediate from the algorithm: the operations at steps $i,\dots,n-2$ depend only on the suffix and on $U_i$.

**(ii) A degree formula.** In the tree $T_i$ on $U_i$ built from $P_i$, every occurrence of $v$ in $P_i$ produces one edge at $v$ (the edge added at the step where $v$ is the current symbol). If $v$ is later removed as some $\ell_j$, it gains exactly one more edge at that step; if $v$ is one of the two final vertices, it gains one edge from the final edge. Hence
$$\deg_{T_i}(v) = 1 + \operatorname{occ}_{P_i}(v).$$

**(iii) The leaves of $T_i$.** By (ii), $v \in U_i$ is a leaf of $T_i$ exactly when $\operatorname{occ}_{P_i}(v) = 0$, i.e. when $v$ does not occur in the suffix $P_i$. Therefore
$$\ell_i = \min\{v \in U_i : v \text{ does not occur in } P_i\} = \text{the smallest leaf of } T_i .$$

**(iv) Induction on $i$.** Run the encoder on $T$. At the first step $T_1 = T$, so by (iii) the encoder deletes the smallest leaf $\ell_1$, and it records its unique neighbour in $T_1$. That neighbour is $p_1$, because the edge $\ell_1 p_1$ was added by the decoder at step $1$. After deleting $\ell_1$ the remaining tree is exactly $T_2$ (by (i)), so the same argument shows that the encoder next deletes $\ell_2$ and records $p_2$. Continuing, the encoder records $p_1, p_2, \dots, p_{n-2}$ and stops with the same final two vertices. Hence $P(T) = P$. $\blacksquare$

**36.** *Strategy: double counting over all trees and all their edges, then symmetry.*

Let $\mathcal{T}_n$ be the set of labelled trees on $\{1,\dots,n\}$. Count the pairs $(T, e)$ consisting of a tree $T \in \mathcal{T}_n$ and one of its edges $e$:

* each tree has $n-1$ edges, and there are $\lvert\mathcal{T}_n\rvert = n^{n-2}$ trees, so the number of pairs is $(n-1)\,n^{n-2}$;
* on the other hand, group the pairs by the edge $e$. The symmetric group $S_n$ acts on labelled trees by relabelling and maps $\{T : e \in E(T)\}$ bijectively onto $\{T : \sigma(e) \in E(T)\}$ for every permutation $\sigma$. Since $S_n$ is transitive on the $\binom{n}{2}$ two-element subsets of $\{1,\dots,n\}$, every possible edge occurs in the same number $N$ of trees.

Therefore
$$\binom{n}{2}\,N = (n-1)\,n^{n-2}, \qquad\text{so}\qquad N = \frac{2(n-1)\,n^{n-2}}{n(n-1)} = 2n^{\,n-3}. \qquad\blacksquare$$

*Check for $n = 3$:* $2\cdot 3^{0} = 2$. The three labelled trees are the paths with centres $1$, $2$, $3$; the edge $\{1,2\}$ appears in the paths centred at $1$ (edges $12, 13$) and at $2$ (edges $12, 23$), so twice ✓.

*Check for $n = 4$:* $2\cdot 4 = 8$. There are $16$ trees with $3$ edges each, hence $48$ edge slots over $\binom{4}{2} = 6$ possible edges, giving $48/6 = 8$ per edge ✓.
