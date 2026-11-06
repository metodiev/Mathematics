# Graph Basics — Solutions

> [Graph Basics](README.md) · Solutions to the 36 problems in [exercises.md](exercises.md)

Each solution states the strategy, then carries out every significant step. Proof problems receive complete proofs; numerical claims are checked at small values. Where two arguments are available, the second is described briefly.

## Beginner

**1.** *Strategy: read the edge list vertex by vertex; a vertex is incident with an edge exactly when its label appears in the edge's two-digit name.*

Collecting the edges containing each label:

| Vertex | Incident edges | Degree |
|---|---|---|
| $1$ | $12, 13, 14$ | $3$ |
| $2$ | $12, 23, 25$ | $3$ |
| $3$ | $13, 23, 36$ | $3$ |
| $4$ | $14, 45$ | $2$ |
| $5$ | $25, 45$ | $2$ |
| $6$ | $36, 67$ | $2$ |
| $7$ | $67$ | $1$ |

The sum is $3+3+3+2+2+2+1 = 16$. The edge set has $8$ members, and $2 \cdot 8 = 16$, so Theorem 7.3.1 holds. Thus $\delta(G) = 1$ (attained only at vertex $7$), $\Delta(G) = 3$ (attained at $1$, $2$, $3$), and the degree sequence is $(3,3,3,2,2,2,1)$.

*Check on the parity corollary.* The odd-degree vertices are $1,2,3,7$: four of them, and four is even, as Corollary 7.3.2 requires.

**2.** *Strategy: list the pairs of $K_7$ and delete the edges of $G$; then compare with the complement degree formula.*

$K_7$ has $\binom{7}{2} = 21$ edges. Deleting the eight edges of $G$ leaves
$$E(\overline{G}) = \{15,\ 16,\ 17,\ 24,\ 26,\ 27,\ 34,\ 35,\ 37,\ 46,\ 47,\ 56,\ 57\},$$
thirteen edges, and indeed $8 + 13 = 21$ by Proposition 7.4.4. Reading degrees from this list:

| Vertex | Neighbours in $\overline G$ | Degree |
|---|---|---|
| $1$ | $5,6,7$ | $3$ |
| $2$ | $4,6,7$ | $3$ |
| $3$ | $4,5,7$ | $3$ |
| $4$ | $2,3,6,7$ | $4$ |
| $5$ | $1,3,6,7$ | $4$ |
| $6$ | $1,2,4,5$ | $4$ |
| $7$ | $1,2,3,4,5$ | $5$ |

The formula $6 - \deg_G(v)$ gives $6-3 = 3$, $6-3=3$, $6-3=3$, $6-2=4$, $6-2=4$, $6-2=4$, $6-1=5$, which matches. The degree sum is $3+3+3+4+4+4+5 = 26 = 2 \cdot 13$, so the handshake lemma holds in the complement too.

**3.** (a) *Strategy: count edge-ends; a loop contributes two.*

* $a$: $e_1, e_2, e_5$ give $3$.
* $b$: $e_1, e_2, e_3$ give $3$.
* $c$: $e_3$ contributes $1$ and the loop $e_4$ contributes $2$, so $\deg(c) = 3$.
* $d$: $e_5$ gives $1$.

The sum is $3+3+3+1 = 10$, and there are five edges, so $10 = 2 \cdot 5$; the handshake lemma holds. Note that without the "loop counts twice" convention the sum would be $9$, which is odd and would contradict Theorem 7.3.1.

(b) $M$ is not simple for two independent reasons: $e_1$ and $e_2$ are parallel (two edges with the same endpoints $a, b$), and $e_4 = cc$ is a loop. It is not a tree because it has a cycle: the loop $e_4$ is a cycle of length $1$, and $e_1, e_2$ together form a cycle of length $2$ (alternatively, $M$ is connected but has a cycle, and a tree is a connected graph with none).

**4.** (a) *Strategy: Corollary 7.3.4.* A $3$-regular graph satisfies $3n = 2 \cdot 18 = 36$, so $n = 12$.

(b) $4 \cdot 5 = 2m$ gives $m = 10$. Since $\binom{5}{2} = 10$, a $5$-vertex simple graph with $10$ edges has *every* pair joined, so it is $K_5$.

(c) If a $3$-regular graph on $n$ vertices existed, then $3n = 2m$ would be even; but $3n$ is odd when $n = 5$. So no such graph exists. Equivalently, Corollary 7.3.4 says a $k$-regular graph with $k$ odd must have an even number of vertices.

**5.** *Strategy: use Theorem 7.8.3 — bipartite exactly when there is no odd cycle.*

* $C_4$: bipartite. Bipartition $\{1,3\}$ and $\{2,4\}$; every edge joins the two sets.
* $C_7$: not bipartite. The cycle itself has length $7$, which is odd.
* $K_{3,3}$: bipartite by construction; the two parts of size $3$ form a bipartition and every edge crosses between them.
* $K_5$: not bipartite. It contains the triangle on any three vertices, and a triangle is an odd cycle.
* $P_5$: bipartite. Bipartition $\{1,3,5\}$ and $\{2,4\}$.
* Petersen graph: not bipartite. Label the vertices by two-element subsets of $\{1,2,3,4,5\}$, adjacent when disjoint. The sequence
$$12,\ 34,\ 15,\ 23,\ 45,\ 12$$
is a cycle of length $5$: consecutive sets are disjoint, and the fifth is disjoint from the first. So the graph contains an odd cycle.

**6.** $K_8$ has $8$ vertices; every vertex is joined to the other $7$, so it is $7$-regular. Then $m = \binom{8}{2} = 28$, the sum of degrees is $8 \cdot 7 = 56$, and $2m = 2 \cdot 28 = 56$ agrees.

**7.** $K_{3,5}$ has $3+5 = 8$ vertices. Every vertex in the part of size $3$ is joined to all five vertices of the other part, so it has degree $5$; every vertex in the part of size $5$ has degree $3$. The sum of degrees is $3 \cdot 5 + 5 \cdot 3 = 30 = 2 \cdot 15$, so there are $15$ edges, and indeed $m = ab = 3 \cdot 5 = 15$ by Proposition 7.8.5. The bipartite bound also gives $m = 15 \le \lfloor 8^2/4 \rfloor = 16$, which holds with slack because the parts are unequal.

**8.** *Strategy: read the nonzero entries above the diagonal; then read $(A^2)_{14}$ as a sum over common neighbours.*

The nonzero entries for $i < j$ are $a_{12}, a_{14}, a_{23}, a_{24}, a_{34}$, so
$$E = \{12,\ 14,\ 23,\ 24,\ 34\}, \qquad m = 5 .$$
Row sums give the degrees $\deg(1) = 2$, $\deg(2) = 3$, $\deg(3) = 2$, $\deg(4) = 3$, with sum $10 = 2 \cdot 5$.

The vertices $2,3,4$ form a triangle (edges $23$, $24$, $34$), so the graph is not bipartite by Theorem 7.8.3.

For the walk count,
$$(A^2)_{14} = \sum_{\ell=1}^{4} a_{1\ell}\,a_{\ell 4} = a_{12}a_{24} + a_{13}a_{34} + a_{14}a_{44} = 1\cdot 1 + 0\cdot 1 + 1 \cdot 0 = 1 .$$
There is exactly one walk of length $2$ from $1$ to $4$, namely $1 \to 2 \to 4$; the attempted walk $1 \to 4 \to 4$ is not a walk because there is no loop at $4$.

**9.** *Strategy: check each consecutive pair is an edge, then check the two repetition conditions.*

(a) $7,6,3,1,4,5,2$: the pairs $76, 63, 31, 14, 45, 52$ are all edges of $G$; all seven vertices are distinct. It is a **path** (so also a walk and a trail), of length $6$, and it visits every vertex, so it is a Hamiltonian path.

(b) $6,3,1,2,3,6$: the pairs $63, 31, 12, 23, 36$ are edges. The edge $36$ occurs twice, so it is a **walk but not a trail**; the vertices $3$ and $6$ repeat, and it is closed because it begins and ends at $6$. It is not a cycle.

(c) $4,1,4$: the pair $41$ is an edge, used twice. It is a **walk**, it is closed, but it is **not a trail** (an edge repeats) and **not a cycle** (its vertices are not distinct apart from the endpoints).

(d) $1,2,5,4,1$: the pairs $12, 25, 54, 41$ are edges, all distinct, and $1,2,5,4$ are distinct with the last equal to the first. It is a **cycle**, namely $1$–$2$–$5$–$4$–$1$.

**10.** *Strategy: follow the adjacencies.*

* From $1$ we reach $2$ and $3$; from $2$ we reach $3$; nothing else is reachable. So $\{1,2,3\}$ is a component (it is a triangle).
* $4$ is adjacent only to $5$, and $5$ only to $4$ and $6$, so $\{4,5,6\}$ is a component (a path $4$–$5$–$6$).
* $7$ is adjacent only to $8$, so $\{7,8\}$ is a component (a single edge).

Hence $c(G) = 3$. Note that $m = 6$ and $n - c = 8 - 3 = 5$, consistent with $m \ge n-c$ (Theorem 7.6.4).

**11.** (a) *Strategy: compare the degree sequences first.*

$C_4$ has four vertices, all of degree $2$: degree sequence $(2,2,2,2)$. A triangle with a pendant edge has vertices of degrees $2,2,3,1$: degree sequence $(3,2,2,1)$. Degree sequences are isomorphism invariants (Theorem 7.7.2), so the graphs are not isomorphic. (Both do have $4$ vertices and $4$ edges — the size alone would not detect the difference.)

(b) Both graphs are paths on four vertices: $P_4$ has edges $12, 23, 34$, and the second graph has edges $ab, bc, cd$. The map
$$1 \mapsto a, \quad 2 \mapsto b, \quad 3 \mapsto c, \quad 4 \mapsto d$$
is a bijection and sends the edge set $\{12,23,34\}$ to $\{ab, bc, cd\}$, so it is an isomorphism. Both are $P_4$.

**12.** *Strategy: use $m(\overline G) = \binom{n}{2} - m(G)$ and look at the structure.*

* $\overline{K_{2,3}}$: $K_{2,3}$ has $2+3 = 5$ vertices and $6$ edges, so its complement has $5$ vertices and $10 - 6 = 4$ edges. Inside each part of $K_{2,3}$ there are no edges, so in the complement each part becomes a clique; between the parts there are no complement edges. Hence $\overline{K_{2,3}} = K_2 \cup K_3$: a disjoint triangle and edge.
* $\overline{K_4}$: $K_4$ has $6$ edges out of $6$ possible, so the complement has $4$ vertices and $0$ edges: the empty graph $\overline{K_4}$.
* $\overline{C_5}$: $C_5$ has $5$ edges out of $10$, so the complement has $5$ edges. Its degrees are $4 - 2 = 2$ at every vertex by Proposition 7.4.4, and a $2$-regular graph on $5$ vertices is $C_5$. Hence $C_5$ is self-complementary. (An explicit isomorphism sends $i \mapsto 2i \bmod 5$.)

## Intermediate

**13.** *Strategy: inject the edge set into the set of two-element subsets of $V$.*

A simple graph has no loops and no parallel edges, so each edge is a two-element subset of $V$, and the map $e \mapsto e$ from $E$ to $\binom{V}{2}$ is injective. Therefore
$$m = \lvert E\rvert \le \left\lvert \binom{V}{2} \right\rvert = \binom{n}{2}.$$
Equality holds exactly when the injection is a bijection, that is, when every two-element subset of $V$ is an edge — precisely the definition of $K_n$. $\blacksquare$

**14.** *Strategy: pigeonhole, with a twist at the extremes.*

Each of the $n$ vertices has a degree in $\{0,1,\dots,n-1\}$, a set of $n$ possible values. Suppose all degrees were distinct. Then the $n$ degrees would be exactly $0,1,\dots,n-1$. But a vertex of degree $n-1$ is adjacent to every other vertex, so no vertex can have degree $0$; the two values $0$ and $n-1$ cannot both occur. That contradiction shows two degrees coincide. $\blacksquare$

*Remark.* The statement is false for $n = 1$: a single vertex has degree $0$, and there is no second vertex to compare with.

**15.** *Strategy: the handshake lemma, then parity.*

If $G$ is $k$-regular on $n$ vertices then every one of the $n$ terms in $\sum_v \deg(v)$ equals $k$, so Theorem 7.3.1 gives
$$kn = \sum_{v} \deg(v) = 2m, \qquad\text{hence}\qquad m = \frac{kn}{2}.$$
Since $m$ is an integer, $kn$ is even. If $k = 3$ then $3n$ is even, so $n$ is even. Hence a $3$-regular graph cannot have an odd number of vertices; in particular there is no $3$-regular graph on $5$ vertices. $\blacksquare$

**16.** (a) *Strategy: reduce the handshake lemma modulo $2$.*

By Theorem 7.3.1, $\sum_{v} \deg(v) = 2m$, which is even. Split the sum:
$$\underbrace{\sum_{\deg(v)\text{ even}} \deg(v)}_{\text{even}} + \sum_{\deg(v)\text{ odd}} \deg(v) = 2m .$$
The first summand is a sum of even numbers, hence even. Therefore the second summand is even too. Modulo $2$, each odd degree contributes $1$, so
$$\sum_{\deg(v)\text{ odd}} \deg(v) \equiv \bigl\lvert\{v : \deg(v) \text{ odd}\}\bigr\rvert \pmod 2 .$$
An even number congruent to the count forces the count to be even. $\blacksquare$

(b) *Exactly one:* impossible, by part (a), since $1$ is odd.
*Exactly two:* possible. $P_3$ has degrees $1,2,1$, with exactly two odd-degree vertices; $K_2$ has degrees $1,1$; even $K_1$ has zero odd-degree vertices, so the count can also be $0$.
*Exactly three:* impossible, because $3$ is odd and part (a) forbids an odd count.

**17.** (a) $(4,3,3,1,1)$: the sum is $12$, even, and the largest entry is $4 = n-1$, so no crude obstruction. Havel–Hakimi with $k = 4$ subtracts $1$ from the next four entries:
$$(4,3,3,1,1) \longmapsto (2,2,0,0).$$
Next $k = 2$: subtract $1$ from the next two entries, giving $(1,-1)$, which has a negative entry. Hence the sequence is **not graphical**.

*Direct reason.* A vertex of degree $4$ in a $5$-vertex graph is adjacent to all four others. The two vertices of degree $1$ therefore have their only neighbour equal to that vertex, so they cannot be adjacent to the two vertices of degree $3$. But those two vertices of degree $3$ need two neighbours besides the degree-$4$ vertex, and only each other remains; each would then have degree $2$, not $3$. Contradiction.

(b) $(3,2,2,2,2,1)$: sum $12$, even; $n = 6$, largest entry $3 \le 5$. Steps:
$$(3,2,2,2,2,1) \longmapsto (1,1,1,2,1) \longmapsto (2,1,1,1,1) \longmapsto (0,0,1,1) \longmapsto (1,1,0,0) \longmapsto (0,0,0),$$
where after each step the sequence is re-sorted. The terminal sequence is all zeros, so the sequence is **graphical**.

*Realisation.* Take a triangle on $a,b,c$ and attach the path $b$–$d$–$e$–$f$. The degrees are $\deg(a)=2$, $\deg(b)=3$ (neighbours $a,c,d$), $\deg(c)=2$, $\deg(d)=2$, $\deg(e)=2$, $\deg(f)=1$, which is $(3,2,2,2,2,1)$ after sorting.

(c) $(3,3,3,3,2)$: sum $14$, even; $n = 5$, largest entry $3 \le 4$. Steps:
$$(3,3,3,3,2) \longmapsto (2,2,2,2) \longmapsto (1,1,2) \longmapsto (2,1,1) \longmapsto (0,0).$$
All zeros, so the sequence is **graphical**.

*Realisation.* Start from $K_5$ and delete the three edges $12$, $23$, $45$. The complements of those edges are the only missing ones, so the degree of a vertex is $4$ minus the number of deleted edges at it: $\deg(1) = 3$, $\deg(2) = 2$, $\deg(3) = 3$, $\deg(4) = 3$, $\deg(5) = 3$. Sorted: $(3,3,3,3,2)$.

**18.** *Strategy: unwrap the definitions and then handle non-emptiness.*

A bipartition $V = A \sqcup B$ with every edge having one end in $A$ and one in $B$ says exactly that no edge has both ends in $A$ and no edge has both ends in $B$. That is, $A$ and $B$ are both **independent sets** (no edge inside either), and every vertex lies in exactly one of them. So the two formulations are the same statement. $\blacksquare$

For the second claim, suppose $G$ has an edge $uv$ and $(A,B)$ is a bipartition. Since $uv$ is an edge, one endpoint lies in $A$ and the other in $B$; hence $A \ne \varnothing$ and $B \ne \varnothing$. (If $G$ has no edges, one part may be taken empty.)

**19.** *Strategy: count the possible edges.*

Every edge has one endpoint in $A$ and one in $B$, so $E \subseteq \{uv : u \in A,\ v \in B\}$. That set has $a b$ members (one for each ordered choice of $u \in A$ and $v \in B$), so $m \le ab$. Next,
$$4ab \le (a+b)^2 \quad\Longleftrightarrow\quad 0 \le (a-b)^2 ,$$
so $ab \le n^2/4$ with $n = a+b$. Since $ab$ is an integer, $ab \le \lfloor n^2/4\rfloor$, and hence $m \le \lfloor n^2/4\rfloor$. $\blacksquare$

*Checks.* $K_{3,3}$ has $a = b = 3$, $m = 9 = ab$, and $9 \le \lfloor 36/4\rfloor = 9$ with equality. $K_{4,4}$ has $a = b = 4$, $m = 16 = ab$, and $16 \le \lfloor 64/4 \rfloor = 16$ with equality. Both are the extremal complete bipartite graphs.

**20.** *Strategy: multiply the matrices explicitly and use Theorem 7.10.1.*

With vertices $1,2,3$,
$$A = \begin{pmatrix}0&1&0\\1&0&1\\0&1&0\end{pmatrix}.$$
Then
$$A^2 = \begin{pmatrix}1&0&1\\0&2&0\\1&0&1\end{pmatrix}, \qquad
A^3 = A^2 A = \begin{pmatrix}0&2&0\\2&0&2\\0&2&0\end{pmatrix}.$$

Interpretations:
* $(A^2)_{13} = 1$: one walk of length $2$ from $1$ to $3$, namely $1 \to 2 \to 3$.
* $(A^2)_{11} = 1$: one walk of length $2$ from $1$ to $1$, namely $1 \to 2 \to 1$.
* $(A^3)_{11} = 0$: no closed walk of length $3$ at $1$.
* $(A^3)_{13} = 0$: no walk of length $3$ from $1$ to $3$.

The zeros are not accidental. $P_3$ is bipartite with parts $\{1,3\}$ and $\{2\}$, and a walk of odd length starting in $\{1,3\}$ must end in the other part $\{2\}$. Since $1$ and $3$ lie in the same part, no odd-length walk joins them, and no odd-length walk returns to $1$. Consistent with Corollary 7.10.2, $\operatorname{tr}(A^3) = 0$ and $P_3$ has no triangles.

**21.** *Strategy: bound the number of edges of a disconnected graph.*

Suppose $G$ is disconnected, with components of sizes $n_1, n_2, \dots, n_c$ where $c \ge 2$ and $\sum_i n_i = n$. There are no edges between components, so
$$m = \sum_{i=1}^{c} \binom{n_i}{2}.$$
We claim this is at most $\binom{n-1}{2}$. First take $c = 2$ with parts of sizes $a$ and $n-a$, where $1 \le a \le n-1$:
$$\binom{a}{2} + \binom{n-a}{2} = \frac{a(a-1) + (n-a)(n-a-1)}{2} = a^2 - na + \frac{n(n-1)}{2}.$$
As a function of $a$ this is a convex parabola, so on the interval $1 \le a \le n-1$ its maximum is attained at an endpoint. At $a = 1$ the value is
$$1 - n + \frac{n(n-1)}{2} = \frac{2 - 2n + n^2 - n}{2} = \frac{(n-1)(n-2)}{2} = \binom{n-1}{2},$$
and the same at $a = n-1$. For $c > 2$, repeatedly merging two components never decreases $\sum \binom{n_i}{2}$, because $\binom{a}{2} + \binom{b}{2} \le \binom{a+b}{2}$; after $c-1$ merges we reach $c = 2$, and the sum is at most $\binom{n-1}{2}$. Hence a disconnected graph satisfies $m \le \binom{n-1}{2}$.

Now if $m \ge \binom{n-1}{2} + 2 > \binom{n-1}{2}$, the graph cannot be disconnected, so it is connected. $\blacksquare$

**22.** *Strategy: two vertices either already lie in different components or can be joined through a third component.*

Let $G$ be disconnected, with at least two components, and let $u, v \in V$.

*Case 1: $u$ and $v$ lie in different components of $G$.* Then no edge of $G$ joins them, so $uv \in E(\overline{G})$ and $u, v$ are adjacent in the complement.

*Case 2: $u$ and $v$ lie in the same component $C$.* Choose a vertex $w$ outside $C$ (it exists because there are at least two components). Then $u w \notin E(G)$ and $w v \notin E(G)$, since $G$ has no edges between components; hence $uw, wv \in E(\overline{G})$, and $u$–$w$–$v$ is a path in $\overline{G}$.

Every pair is joined by a path in $\overline{G}$, which is therefore connected. $\blacksquare$

*Example where the converse fails:* $K_4$ is connected, and its complement is the empty graph on four vertices, which is disconnected (indeed has four components). So a connected graph can have a disconnected complement; only the direction proved above is valid in general.

## Advanced

**23.** *Strategy: choose a shortest walk, then show it cannot repeat a vertex.*

Let $W = v_0 e_1 v_1 \cdots e_k v_k$ be a $u$–$v$ walk with $v_0 = u$ and $v_k = v$, and suppose $W$ has the smallest possible length among all $u$–$v$ walks. Suppose a vertex repeats: $v_i = v_j$ with $0 \le i < j \le k$. Delete the segment from position $i$ to position $j$, obtaining
$$v_0 e_1 \cdots v_i\, e_{j+1} v_{j+1} \cdots e_k v_k .$$
This is a valid walk because the vertex before the deletion point ($v_i$) equals the vertex after it ($v_j$). Its length is $k - (j-i) < k$, contradicting minimality. Therefore $v_0, \dots, v_k$ are pairwise distinct and $W$ is a path. $\blacksquare$

**24.** *Strategy: among all odd closed walks, take a shortest one and show it has no repeated vertex.*

Let $W = v_0 e_1 v_1 \cdots e_k v_k$ be a closed walk, so $v_0 = v_k$, with $k$ odd, chosen with $k$ minimal among all odd closed walks. Assume a vertex repeats: $v_i = v_j$ with $0 \le i < j \le k-1$. Then $W$ splits at the two occurrences into
$$W_1 = v_i e_{i+1} v_{i+1} \cdots e_j v_j, \qquad W_2 = v_j e_{j+1} \cdots e_k v_0 e_1 \cdots e_i v_i .$$
Both are closed walks (note $v_k = v_0$ in $W_2$). Their lengths are $\ell_1 = j-i \ge 1$ and $\ell_2 = (k-j) + i \ge 1$ because $j \le k-1$. Moreover $\ell_1 + \ell_2 = k$, which is odd, so exactly one of $\ell_1, \ell_2$ is odd; that one is a closed walk of odd length strictly smaller than $k$, contradicting minimality.

Hence $v_0, \dots, v_{k-1}$ are pairwise distinct. Since $G$ is a simple graph, $k \neq 1$ (no loops) and $k \neq 2$ (no parallel edges), so $k \ge 3$ and $W$ is a cycle of odd length. $\blacksquare$

*Remark.* Without simplicity, the conclusion still holds with "cycle" allowing length $1$ (a loop) or $2$ (parallel edges); the argument above only uses that a closed walk of length $1$ or $2$ with distinct internal vertices *is* itself a cycle in that wider sense.

**25.** *Strategy: extract a closed trail greedily, then split it into cycles, then induct on $m$.*

We prove the statement by induction on $m = \lvert E\rvert$. If $m = 0$ there is nothing to prove. Otherwise some vertex has positive degree, hence degree at least $2$ (all degrees are even).

Start at any vertex $v_0$ incident with an edge and extend a trail as long as possible: from the current endpoint, take any unused edge incident with it. The trail cannot get stuck at a vertex other than $v_0$: at an internal or final vertex $x \ne v_0$ the trail has used an odd number of edge-ends (each visit uses one edge in and one out, and the final arrival uses one more in than out), while $\deg(x)$ is even, so at least one edge at $x$ is unused and the trail can continue. Since there are finitely many edges, the procedure terminates, and it can only terminate at $v_0$, giving a **closed trail** $C$ of positive length.

Now split $C$ into cycles. If $C$ visits a vertex twice, split $C$ at two occurrences of that vertex into two shorter closed trails; repeat. Since lengths strictly decrease, the process stops, and the terminal closed trails have no repeated internal vertices, i.e. they are cycles. Thus $C$'s edges are partitioned into edge-disjoint cycles.

Let $F$ be the set of edges of $C$. Remove $F$ from $G$. At each vertex, the number of removed edge-ends is even (it is $2$ times the number of times the closed trail passes through the vertex), so in $G - F$ every degree is still even. By induction, the edges of $G - F$ are partitioned into cycles, and adding the cycles that partition $F$ gives a partition of all of $E$. $\blacksquare$

*Check.* A figure-eight (two triangles sharing one vertex) has all degrees even ($4$ at the shared vertex, $2$ at the others), and its six edges split into the two triangles.

**26.** *Strategy: one direction is a parity argument on the two parts; the other reduces to Theorem 7.8.3.*

*($\Rightarrow$)* Suppose $G$ is bipartite with parts $A$ and $B$, and let $W = v_0 e_1 v_1 \cdots e_k v_k$ be a closed walk, $v_0 = v_k$. Consecutive vertices are joined by an edge, so they lie in different parts. By induction on $i$, $v_i \in A$ when $i$ is even and $v_i \in B$ when $i$ is odd. Since $v_k = v_0 \in A$, the index $k$ must be even. So every closed walk has even length.

*($\Leftarrow$)* Suppose $G$ has no closed walk of odd length. A cycle is a closed walk (of length at least $3$), so $G$ has no odd cycle; by Theorem 7.8.3, $G$ is bipartite. $\blacksquare$

*Remark.* The two characterisations are therefore equivalent: $G$ is bipartite $\Leftrightarrow$ no odd cycle $\Leftrightarrow$ no odd closed walk. The second equivalence also follows from Lemma 7.8.2 in one direction and from "a cycle is a closed walk" in the other.

**27.** (a) *Strategy: count the arcs by tail and by head.*

Each arc $(u,v) \in A$ has exactly one tail $u$ and exactly one head $v$. Counting the arcs by their tail,
$$\lvert A\rvert = \sum_{v \in V} \bigl\lvert\{a \in A : a \text{ has tail } v\}\bigr\rvert = \sum_{v \in V} \deg^+(v) .$$
Counting the same arcs by their head gives $\lvert A\rvert = \sum_v \deg^-(v)$. Hence both sums equal $\lvert A\rvert$. $\blacksquare$

(b) Take $V = \{1,2,3\}$ and the underlying graph $P_3$ with edges $12$ and $23$.

* $D_1$ with arcs $(1,2)$ and $(3,2)$: out-degrees $(1,0,1)$, in-degrees $(0,2,0)$.
* $D_2$ with arcs $(2,1)$ and $(2,3)$: out-degrees $(0,2,0)$, in-degrees $(1,0,1)$.

Both have underlying graph $P_3$, but the out-degree sequences differ: $(1,0,1)$ versus $(0,2,0)$. So the underlying graph does not determine the in- and out-degrees.

**28.** *Strategy: suppose there are at least two components and look at the smallest one.*

Suppose $G$ is disconnected. Its components have sizes summing to $n$, so at least one component $S$ satisfies $\lvert S\rvert \le n/2$. Pick $v \in S$. All neighbours of $v$ lie in $S$, so
$$\deg(v) \le \lvert S\rvert - 1 \le \frac{n}{2} - 1 = \frac{n-2}{2} < \frac{n-1}{2} \le \delta(G),$$
contradicting $\deg(v) \ge \delta(G)$. Hence $G$ is connected. $\blacksquare$

*Remark.* The bound is sharp in the sense that $\delta \ge (n-1)/2$ cannot be lowered much: two disjoint copies of $K_{n/2}$ have minimum degree $n/2 - 1$ and are disconnected (for even $n$).

**29.** *Strategy: translate the permutation matrix into a bijection and back.*

*($\Rightarrow$)* Let $\varphi : V(G) \to V(H)$ be an isomorphism, and index both vertex sets by $1,\dots,n$ in such a way that $\varphi$ sends the $i$-th vertex of $G$ to the $i$-th vertex of $H$ (relabel $H$ along $\varphi$). With this labelling the two adjacency matrices are *equal*, because $a^G_{ij} = 1$ iff $v_i v_j \in E(G)$ iff $\varphi(v_i)\varphi(v_j) \in E(H)$ iff $a^H_{ij} = 1$. Taking $P = I$ gives $A(H) = I A(G) I^{\mathsf T}$.

For the general statement, let $P$ be the permutation matrix of the permutation $\sigma$ of $\{1,\dots,n\}$, defined by $P_{\sigma(i), i} = 1$ and all other entries $0$. Then $(P A P^{\mathsf T})_{ab} = A_{\sigma^{-1}(a), \sigma^{-1}(b)}$, so the identity $A(H) = P A(G) P^{\mathsf T}$ says
$$a^H_{ab} = a^G_{\sigma^{-1}(a)\,\sigma^{-1}(b)} \qquad\text{for all } a,b,$$
which is exactly the statement that $\sigma^{-1}$ is an isomorphism $H \to G$, equivalently $\sigma$ is an isomorphism $G \to H$.

*($\Leftarrow$)* If $A(H) = P A(G) P^{\mathsf T}$ for a permutation matrix $P$, then the permutation $\sigma$ associated with $P$ satisfies $a^H_{\sigma(i)\sigma(j)} = a^G_{ij}$ for all $i,j$, so $\sigma$ is a bijection preserving adjacency and non-adjacency: an isomorphism. $\blacksquare$

**30.** *Strategy: count walks of length $2$ in two ways, then apply Cauchy–Schwarz.*

A walk of length $2$ has the form $v \to u \to w$ where $u$ is adjacent to both $v$ and $w$. Group the walks by their **middle** vertex $u$: for each $u$ there are $\deg(u)$ choices for $v$ and, independently, $\deg(u)$ choices for $w$, hence $\deg(u)^2$ walks with middle vertex $u$. Summing,
$$\#\{\text{walks of length } 2\} = \sum_{u \in V} \deg(u)^2 .$$
The same count comes from Theorem 7.10.1: the number of walks of length $2$ is the sum of all entries of $A^2$, which equals $\mathbf{1}^{\mathsf T} A^2 \mathbf{1} = (A\mathbf{1})^{\mathsf T}(A\mathbf{1}) = \sum_u \deg(u)^2$, since $A\mathbf{1}$ is the degree vector.

Now apply the Cauchy–Schwarz inequality to the vectors $(1,1,\dots,1)$ and $(\deg(v_1),\dots,\deg(v_n))$:
$$\left(\sum_{v} 1 \cdot \deg(v)\right)^2 \le \left(\sum_v 1^2\right)\left(\sum_v \deg(v)^2\right) = n \sum_v \deg(v)^2 .$$
The left side is $(2m)^2$ by the handshake lemma, so $4m^2 \le n \sum_v \deg(v)^2$, that is
$$\sum_{v \in V} \deg(v)^2 \ \ge \ \frac{4m^2}{n}. \qquad\blacksquare$$

*Check.* For $K_n$ every degree is $n-1$ and every term is $(n-1)^2$, so the sum is $n(n-1)^2$; the right side is $4\binom{n}{2}^2/n = 4 \cdot \frac{n^2(n-1)^2}{4} / n = n(n-1)^2$, with equality, as Cauchy–Schwarz predicts for a constant vector.

## Challenge

**31.** *Strategy: induction on $n$, deleting the two endpoints of an edge and bounding $d(u) + d(v)$.*

**Claim.** A triangle-free simple graph on $n \ge 1$ vertices has at most $\lfloor n^2/4 \rfloor$ edges.

**Proof.** Induct on $n$. For $n = 1$ there are no edges and $\lfloor 1/4 \rfloor = 0$.

For $n \ge 2$: if $G$ has no edge, then $m = 0 \le \lfloor n^2/4\rfloor$ and we are done. Otherwise choose an edge $uv$. Because $G$ is triangle-free, $u$ and $v$ have no common neighbour: if $w$ were adjacent to both, then $u,v,w$ would form a triangle. Hence $N(u) \cap N(v) = \varnothing$. Also $u \in N(v)$ and $v \in N(u)$, so $N(u) \cup N(v) \subseteq V$ and
$$\deg(u) + \deg(v) = \lvert N(u)\rvert + \lvert N(v)\rvert = \lvert N(u) \cup N(v)\rvert \le n .$$

Now delete $u$ and $v$. The graph $G - \{u,v\}$ is triangle-free on $n-2$ vertices, so by induction it has at most $\lfloor (n-2)^2/4 \rfloor$ edges. Counting the edges of $G$:
$$m = e\bigl(G - \{u,v\}\bigr) + \deg(u) + \deg(v) - 1,$$
where the $-1$ corrects the double count of the edge $uv$. Hence
$$m \le \left\lfloor \frac{(n-2)^2}{4} \right\rfloor + n - 1 .$$
It remains to check that the right side equals $\lfloor n^2/4 \rfloor$.

*If $n = 2k$:* $\lfloor (2k-2)^2/4\rfloor + 2k - 1 = (k-1)^2 + 2k - 1 = k^2 - 2k + 1 + 2k - 1 = k^2 = \lfloor n^2/4\rfloor$.

*If $n = 2k+1$:* $\lfloor (2k-1)^2/4 \rfloor = \lfloor k^2 - k + \tfrac14\rfloor = k^2 - k$, so the right side is $k^2 - k + 2k + 1 - 1 = k^2 + k$, while $\lfloor n^2/4 \rfloor = \lfloor (4k^2+4k+1)/4\rfloor = k^2+k$. Equal.

The induction is complete. $\blacksquare$

*Sharpness.* The complete bipartite graph $K_{\lfloor n/2\rfloor,\lceil n/2\rceil}$ is triangle-free and has $\lfloor n^2/4\rfloor$ edges, so the bound cannot be improved. For $n = 5$ this is $K_{2,3}$, with $6 = \lfloor 25/4 \rfloor$ edges.

**32.** *Strategy: sort by the number of edges, and note that the complement pairs up graphs whose edge counts sum to $6$.*

A graph on $4$ vertices has at most $\binom{4}{2} = 6$ edges.

* $0$ edges: the empty graph. **$1$ type.**
* $1$ edge: $K_2 \cup 2K_1$. **$1$ type.**
* $2$ edges: either the two edges share a vertex ($P_3 \cup K_1$) or they are disjoint ($2K_2$). **$2$ types.**
* $3$ edges: using all four vertices, the possibilities are $K_3 \cup K_1$, the path $P_4$, and the star $K_{1,3}$. These are pairwise non-isomorphic (degree sequences $(2,2,2,0)$, $(2,2,1,1)$, $(3,1,1,1)$). **$3$ types.**
* $4$ edges: the complement has $2$ edges, so by the previous line the complement is $P_3 \cup K_1$ or $2K_2$, giving the triangle-with-a-pendant-edge and $C_4$. **$2$ types.**
* $5$ edges: the complement has $1$ edge, so the graph is $K_4$ minus one edge. **$1$ type.**
* $6$ edges: $K_4$. **$1$ type.**

Total: $1+1+2+3+2+1+1 = 11$ pairwise non-isomorphic graphs.

*Self-complementary graphs.* A self-complementary graph on $4$ vertices has $m = 6/2 = 3$ edges. Among the three $3$-edge graphs, $\overline{K_3 \cup K_1} = K_{1,3}$ and $\overline{K_{1,3}} = K_3 \cup K_1$, so those two are complementary to each other rather than to themselves. The complement of $P_4$ is again a path on four vertices: $P_4$ has edges $12, 23, 34$, so its complement has $13, 14, 24$, which is the path $3$–$1$–$4$–$2$. Hence $P_4$ is the unique self-complementary graph on $4$ vertices.

**33.** *Strategy: colour the vertices at random; the expected size of the cut is $m/2$.*

Choose, independently for every vertex, one of two colours with probability $1/2$ each, and let $A$ be the set of vertices of the first colour. Let $X$ be the number of edges with one end in $A$ and one end outside $A$. For a fixed edge $e = uv$, the two endpoints receive different colours with probability $1/2$, so $\mathbb{E}[\text{indicator that } e \text{ is cut}] = 1/2$. By linearity of expectation,
$$\mathbb{E}[X] = \sum_{e \in E} \frac{1}{2} = \frac{m}{2}.$$
An average of $m/2$ over all colourings implies that at least one colouring has $X \ge m/2$; otherwise every colouring would have $X < m/2$ and the average would be less than $m/2$. For that colouring, the subgraph with vertex set $V$ and edge set $\delta(A)$ is bipartite (its parts are $A$ and $V \setminus A$) and has $X \ge m/2$ edges. $\blacksquare$

*Second approach.* Place the vertices one at a time, each on the side where it has more already-placed neighbours. When a vertex is placed, at least half of the edges joining it to earlier vertices are cut; summing over the vertices counts every edge exactly once, at the moment its later endpoint was placed. Hence at least $m/2$ edges are cut. This is the greedy version and needs no probability.

**34.** *Strategy: delete low-degree vertices and count how many edges can disappear.*

Let $n$ and $m$ be the vertex and edge counts of the original graph $G$. If $m = 0$ the statement is vacuous (there is no non-empty subgraph, and the claim is understood for $m \ge 1$). Assume $m \ge 1$.

Run the following procedure. While the current graph has a vertex of degree less than $m/n$, delete that vertex and all its incident edges. Each deletion removes strictly fewer than $m/n$ edges, and the procedure performs at most $n$ deletions, so the total number of edges removed is strictly less than
$$n \cdot \frac{m}{n} = m .$$
Therefore at least one edge survives: the process cannot delete all edges, and in particular it cannot delete all vertices. Let $H$ be the final graph. By construction every vertex of $H$ has degree at least $m/n$ *in* $H$ (the procedure stops only when no vertex violates the condition), and $H$ is non-empty. Hence $\delta(H) \ge m/n$. $\blacksquare$

*Check.* For $G = K_{1,3}$ we have $m/n = 3/4$; the whole graph already has minimum degree $1 \ge 3/4$, so nothing is deleted. For a long path $P_n$ we have $m/n \approx 1$, and the graph itself has minimum degree $1$, so again it qualifies.

**35.** *Strategy: a longest path, and the furthest neighbour of its first vertex.*

Let $P = v_0 v_1 \cdots v_k$ be a longest path in $G$. Every neighbour of $v_0$ lies on $P$ (otherwise $P$ could be extended at $v_0$). So $\deg(v_0) \le k+1$; more precisely, $v_0$ has $\deg(v_0)$ neighbours among $v_1,\dots,v_k$.

Because $\deg(v_0) \ge \delta(G) \ge 2$, the vertex $v_0$ has at least two neighbours on $P$; let $v_i$ be the neighbour with the largest index $i$. The neighbours of $v_0$ are $\deg(v_0)$ distinct vertices among $v_1,\dots,v_k$, so the largest of their indices satisfies $i \ge \deg(v_0) \ge \delta(G)$.

The closed walk
$$v_0 v_1 \cdots v_i v_0$$
has distinct vertices $v_0,\dots,v_i$ (they lie on the path) and length $i + 1$, so it is a cycle of length $i+1 \ge \delta(G)+1$. $\blacksquare$

*Check.* For $G = K_{n}$: $\delta = n-1$, and the graph contains a cycle of length $n = \delta + 1$, namely the Hamiltonian cycle. For $C_5$: $\delta = 2$ and the whole $5$-cycle has length $5 \ge 3$.

**36.** *Strategy: parity gives necessity; an explicit $+4$ construction gives sufficiency.*

**Necessity.** If $G$ is self-complementary on $n$ vertices then $G \cong \overline G$, so $m(G) = m(\overline G)$. By Proposition 7.4.4,
$$2m(G) = m(G) + m(\overline G) = \binom{n}{2} = \frac{n(n-1)}{2},$$
so $\binom{n}{2}$ is even, i.e. $n(n-1)$ is divisible by $4$. Among two consecutive integers exactly one is even; for the product to be divisible by $4$, the even one must be divisible by $4$. If $n$ is even, $n \equiv 0 \pmod 4$; if $n$ is odd, $n-1$ is even and must be divisible by $4$, so $n \equiv 1 \pmod 4$. Hence $n \equiv 0$ or $1 \pmod 4$.

**Sufficiency.** We construct examples for every $n \equiv 0, 1 \pmod 4$.

*Base cases.* $n = 1$: the one-vertex graph is self-complementary. $n = 4$: $P_4$ is self-complementary (Problem 32). $n = 5$: $C_5$ is self-complementary: its complement is $2$-regular on $5$ vertices, hence again a $5$-cycle.

*Induction step $n \to n+4$.* Suppose $G$ is self-complementary on $V$ with $\lvert V\rvert = n$, and let $\psi : V \to V$ be an isomorphism $G \to \overline G$. Add four new vertices $x_1,x_2,x_3,x_4$ and define $G'$ on $V \cup \{x_1,x_2,x_3,x_4\}$ by
* the path edges $x_1x_2$, $x_2x_3$, $x_3x_4$;
* all edges $x_1 v$ and $x_4 v$ for $v \in V$;
* the edges of $G$ inside $V$, and nothing else.

Define $\Phi$ on $V(G')$ by $\Phi(v) = \psi(v)$ for $v \in V$ and
$$\Phi(x_1) = x_3, \quad \Phi(x_2) = x_1, \quad \Phi(x_3) = x_4, \quad \Phi(x_4) = x_2 .$$
This is a bijection. Check that it sends every edge of $G'$ to an edge of $\overline{G'}$:

| Edge of $G'$ | Image | Why the image is an edge of $\overline{G'}$ |
|---|---|---|
| $uv$ with $u,v \in V$ | $\psi(u)\psi(v)$ | $\psi$ is an isomorphism $G \to \overline G$, so this is a non-edge of $G$, hence a complement edge |
| $x_1v$ | $x_3\psi(v)$ | $N_{G'}(x_3) = \{x_2,x_4\}$, so $x_3\psi(v)$ is a non-edge of $G'$ |
| $x_4v$ | $x_2\psi(v)$ | $N_{G'}(x_2) = \{x_1,x_3\}$, so this is a non-edge of $G'$ |
| $x_1x_2$ | $x_3x_1$ | $N_{G'}(x_1) = \{x_2\} \cup V$, so $x_1x_3 \notin E(G')$ |
| $x_2x_3$ | $x_1x_4$ | $N_{G'}(x_1) = \{x_2\}\cup V$ and $x_4 \notin V$, so $x_1x_4 \notin E(G')$ |
| $x_3x_4$ | $x_4x_2$ | $N_{G'}(x_4) = \{x_3\} \cup V$, so $x_4x_2 \notin E(G')$ |

The images are distinct because $\Phi$ is a bijection on vertex pairs. Finally the two graphs have the same number of edges:
$$\lvert E(G')\rvert = m(G) + 3 + 2n, \qquad
\lvert E(\overline{G'})\rvert = \binom{n+4}{2} - \lvert E(G')\rvert = \binom{n}{2} + 4n + 6 - m(G) - 3 - 2n,$$
and $\binom{n}{2} = 2m(G)$ because $G$ is self-complementary, so $\lvert E(\overline{G'})\rvert = 2m(G) + 2n + 3 - m(G) = m(G) + 2n + 3 = \lvert E(G')\rvert$. An injective map between edge sets of equal finite size is a bijection, so $\Phi$ is an isomorphism $G' \to \overline{G'}$ and $G'$ is self-complementary on $n+4$ vertices.

By induction from $n = 4$ and $n = 5$ (and the trivial case $n = 1$), self-complementary graphs exist for every $n \equiv 0$ or $1 \pmod 4$. Together with necessity, this proves the criterion. $\blacksquare$
