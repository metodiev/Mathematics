# Paths and Connectivity — Solutions

> [Paths and Connectivity](README.md) · Solutions to the 36 problems in [exercises.md](exercises.md)

Each solution states the strategy, then carries out every significant step. Proof problems receive complete proofs; numerical claims are checked against the criterion or invariant they illustrate. Where a second argument exists, it is described at the end of the solution.

## Beginner

**1.** *Strategy: compute degrees, count odd vertices, then apply Theorem 7.2.1/7.2.3 (circuit: connected and all even) and Theorem 7.3.1 (trail: connected and exactly $0$ or $2$ odd).*

(a) $C_5$: all five degrees are $2$. Connected, $0$ odd vertices. **Eulerian circuit.**

(b) $K_4$: all four degrees are $3$. Connected, but $4$ odd vertices, so the trail condition already fails. **Neither.**

(c) House: vertices $1,2,3,4$ form the square and $5$ is the roof joined to $2,3$. Then $\deg(1) = 2$, $\deg(2) = 3$, $\deg(3) = 3$, $\deg(4) = 2$, $\deg(5) = 2$. Connected, exactly $2$ odd vertices. **Eulerian trail, no circuit.**

(d) Bowtie: the shared vertex has degree $4$, the other four have degree $2$. Connected, $0$ odd vertices. **Eulerian circuit.**

(e) $K_{3,3}$: all six degrees are $3$. Connected, $6$ odd vertices. **Neither.**

*Check.* Each degree sequence sums to $2m$: (a) $10 = 2\cdot5$; (b) $12 = 2\cdot6$; (c) $12 = 2\cdot6$; (d) $12 = 2\cdot6$; (e) $18 = 2\cdot9$ ✓.

**2.** *Strategy: one edge removal toggles the parity of exactly its two endpoints.*

(a) A graph with an Eulerian trail has at most two odd vertices (Theorem 7.3.1). Königsberg has four ($A$ of degree $5$, and $B,C,D$ of degree $3$), and it is connected, so no Eulerian trail exists — in particular no closed one.

(b) Removing a bridge $xy$ decreases $\deg(x)$ and $\deg(y)$ by $1$ and leaves all other degrees unchanged, so exactly the parities of $x$ and $y$ flip. Since all four vertices are odd, removing any bridge leaves exactly the two *other* vertices odd. Hence **every** bridge may be demolished, and the resulting multigraph has an Eulerian trail between the two odd vertices that were not touched. For example, demolishing the bridge $BC$ leaves $A$ and $D$ odd, so the trail runs from $A$ to $D$ or from $D$ to $A$.

To obtain an Eulerian circuit one would need $0$ odd vertices. A single removal changes the number of odd vertices by $\pm 2$ or $0$ (it flips two parities), so from $4$ one can reach $2$, $4$ or $6$, never $0$. Hence no single demolition gives an Eulerian circuit. In general, if $2r$ is the number of odd vertices, at least $r$ edges must be added or removed (in pairs of odd vertices) to reach the Eulerian case.

**3.** *Strategy: check the two hypotheses of Theorem 7.2.3, then run the splicing algorithm.*

(a) Degrees: $1$: $12, 31 \Rightarrow 2$; $2$: $12, 23 \Rightarrow 2$; $3$: $23, 31, 34, 53 \Rightarrow 4$; $4$: $34, 45 \Rightarrow 2$; $5$: $45, 53, 56, 75 \Rightarrow 4$; $6$: $56, 67 \Rightarrow 2$; $7$: $67, 75 \Rightarrow 2$. All even, sum $18 = 2\cdot9$ ✓. Connectivity: $1$–$2$–$3$ reaches the first triangle; $3$–$4$–$5$ the second; $5$–$6$–$7$ the third. So the graph is connected with all degrees even and has an Eulerian circuit.

(b) Start at $1$ and take edges greedily. First circuit: $1 \to 2 \to 3 \to 1$, using $12, 23, 31$; it closes at $1$ and no edge at $1$ remains. The unused edges are $34, 45, 53, 56, 67, 75$, which form the two triangles $\{3,4,5\}$ and $\{5,6,7\}$ joined at $5$, and vertex $3$ of the first circuit is incident with the unused edge $34$. Grow from $3$: $3 \to 4 \to 5 \to 3$ (edges $34, 45, 53$), which closes. Splice into the first circuit at $3$:
$$1 \to 2 \to 3 \to 4 \to 5 \to 3 \to 1 .$$
Unused edges now: $56, 67, 75$, all at $5$, which lies on the current circuit. Grow $5 \to 6 \to 7 \to 5$ and splice at $5$:
$$1 \to 2 \to 3 \to 4 \to 5 \to 6 \to 7 \to 5 \to 3 \to 1 .$$
(c) The circuit uses the nine edges $12, 23, 34, 45, 56, 67, 75, 53, 31$ exactly once ✓. It has length $9 = m$ and visits $10$ positions, with vertices $3$ and $5$ each appearing twice.

*Check.* The edge list of the proposed circuit, read in order, is $12, 23, 34, 45, 56, 67, 75, 53, 31$, which is exactly $E$ ✓, and consecutive edges share a vertex, so it is a trail ✓.

**4.** *Strategy: find the odd vertices, then build a trail from one to the other.*

(a) $\deg(1) = 3$ ($12, 51, 16$); $\deg(2) = 2$ ($12, 23$); $\deg(3) = 2$ ($23, 34$); $\deg(4) = 3$ ($34, 45, 64$); $\deg(5) = 2$ ($45, 51$); $\deg(6) = 2$ ($16, 64$). Odd vertices: $1$ and $4$. Sum $= 14 = 2\cdot7$ ✓.

(b) The graph is a pentagon $1$–$2$–$3$–$4$–$5$–$1$ with a pendant path $1$–$6$–$4$ attached at $1$ and $4$. The trail
$$1 \to 2 \to 3 \to 4 \to 5 \to 1 \to 6 \to 4$$
uses $12, 23, 34, 45, 51, 16, 64$: all seven edges once ✓, starts at $1$, ends at $4$ ✓.

(c) By Corollary 7.3.2 the endpoints of an Eulerian trail are exactly the odd-degree vertices, here $1$ and $4$. So every Eulerian trail runs from $1$ to $4$ or from $4$ to $1$; in particular it cannot start anywhere else.

**5.** *Strategy: apply Theorem 7.4.2 — weak connectivity plus $\deg^{\mathrm{in}}(v) = \deg^{\mathrm{out}}(v)$ at every vertex for a circuit; for a trail, look for one vertex with out $-$ in $= +1$ and one with out $-$ in $= -1$.*

(a) Each of $1,2,3$ has out-degree $2$ and in-degree $2$; the digraph is weakly connected (indeed strongly connected: $1\to2\to3\to1$). By Theorem 7.4.2 there is a directed Eulerian circuit, for example
$$1 \to 2 \to 3 \to 1 \to 3 \to 2 \to 1 .$$
The arcs used are $12, 23, 31, 13, 32, 21$: all six, each once ✓.

(b) Degrees: vertex $1$: out $1$, in $1$; vertex $2$: out $1$, in $1$; vertex $3$: out $2$ (to $1$ and $4$), in $1$ (from $2$); vertex $4$: out $0$, in $1$ (from $3$). So balance fails at $3$ (excess $+1$) and $4$ (excess $-1$), and the digraph is weakly connected. There is no Eulerian circuit, but there is a directed Eulerian trail from $3$ to $4$:
$$3 \to 1 \to 2 \to 3 \to 4 .$$
It uses the four arcs $31, 12, 23, 34$ ✓.

*Check.* The in/out balance is exactly the statement that every cut has equally many arcs in each direction; in (b) the cut $\delta^{+}(\{1,2\}) = \{23, 13\}$? Careful: the arcs leaving $\{1,2\}$ are $23$; the arcs entering are $12$ and $31$ — the imbalance is accounted for by the endpoints of the trail.

**6.** *Strategy: Dirac needs $\delta \ge n/2$ and $n \ge 3$; when it applies, a Hamiltonian cycle is guaranteed, and one then exhibits a cycle to confirm.*

(a) $K_{3,3}$ has $n = 6$ and every degree $3$, so $\delta = 3 = n/2$ and Dirac's condition holds. A Hamiltonian cycle exists: with parts $\{x_1,x_2,x_3\}$ and $\{y_1,y_2,y_3\}$,
$$x_1 y_1 x_2 y_2 x_3 y_3 x_1$$
is a cycle through all six vertices ✓.

(b) $K_6$ has $n = 6$, $\delta = 5 \ge 3$, so Dirac applies. The cycle $1\,2\,3\,4\,5\,6\,1$ is Hamiltonian ✓.

(c) $C_6$ has $n = 6$, $\delta = 2 < 3$, so Dirac's condition fails and the theorem is silent. Nevertheless $C_6$ itself is a Hamiltonian cycle ✓.

The comparison shows that Dirac's condition is **sufficient but not necessary**: (c) is Hamiltonian without satisfying it, while (a) and (b) are Hamiltonian and do satisfy it. No choice of the constant $\tfrac12$ repairs this, because $C_n$ has minimum degree $2$ for every $n$, so the ratio $\delta/n$ tends to $0$ along Hamiltonian graphs.

**7.** *Strategy: look first for a cheap obstruction (cut vertex, bipartite imbalance, wrong edge count), then exhibit a cycle or path.*

(a) $K_{2,3}$ is bipartite with parts of sizes $2$ and $3$. By Proposition 7.7.3 a Hamiltonian cycle would force equal sizes, so **no Hamiltonian cycle**. A Hamiltonian path exists: $y_1 x_1 y_2 x_2 y_3$ visits all five vertices ✓. So $K_{2,3}$ is traceable but not Hamiltonian.

(b) $C_6$ **has a Hamiltonian cycle** (itself). 

(c) The bowtie has a cut vertex (the shared vertex). By Proposition 7.7.1 a Hamiltonian graph with $n \ge 3$ has no cut vertex, so **no Hamiltonian cycle**. It does have a Hamiltonian path: if the triangles are $1$–$2$–$3$ and $3$–$4$–$5$, the path $2 \to 1 \to 3 \to 4 \to 5$ visits all five ✓.

(d) $K_4$ **has a Hamiltonian cycle** $1\,2\,3\,4\,1$ ✓.

(e) $P_5$ is a tree with $4$ edges and $5$ vertices, so it contains no cycle at all and in particular **no Hamiltonian cycle**. Its Hamiltonian path is the path itself ✓.

**8.** *Strategy: settle vertices in increasing order of tentative distance; relax every edge out of the settled vertex.*

| Step | Extract | $d[1]$ | $d[2]$ | $d[3]$ | $d[4]$ | $d[5]$ | Relaxations |
|---|---|---|---|---|---|---|---|
| 0 | — | $0$ | $\infty$ | $\infty$ | $\infty$ | $\infty$ | initialise |
| 1 | $1$ | $0$ | $4$ | $2$ | $\infty$ | $\infty$ | $12 = 4$, $13 = 2$ |
| 2 | $3$ | $0$ | $3$ | $2$ | $10$ | $12$ | $3\to2$: $2+1 = 3 < 4$; $3\to4$: $10$; $3\to5$: $12$ |
| 3 | $2$ | $0$ | $3$ | $2$ | $8$ | $12$ | $2\to4$: $3+5 = 8 < 10$; $2\to5$: $15 > 12$ |
| 4 | $4$ | $0$ | $3$ | $2$ | $8$ | $10$ | $4\to5$: $8+2 = 10 < 12$ |
| 5 | $5$ | $0$ | $3$ | $2$ | $8$ | $10$ | none |

Final distances $(d_1,\dots,d_5) = (0,3,2,8,10)$. The extraction order is $1,3,2,4,5$; note that vertex $2$ was first labelled $4$ and improved to $3$ before extraction, which is exactly what the priority queue is for.

A shortest path to $5$ is $1 \to 3 \to 2 \to 4 \to 5$, of weight $2 + 1 + 5 + 2 = 10$ ✓, matching $d[5]$. Its predecessors are $\pi[3] = 1$, $\pi[2] = 3$, $\pi[4] = 2$, $\pi[5] = 4$.

*Check.* No shorter route to $5$ exists: any route enters $5$ from $3$ (cost $d_3 + 10 \ge 12$) or from $4$ (cost $d_4 + 2 = 10$), and $d_4 = 8$ is the minimum over $1\to2\to4$ $(4+5 = 9)$ and $1\to3\to2\to4$ $(2+1+5 = 8)$ ✓.

**9.** *Strategy: relax every edge in the stated order, one pass at a time, for at most $n-1 = 4$ passes; stop early if a pass changes nothing.*

Order of relaxation: $sa, sb, sc, cb, ba, at, bt, ct$.

| Pass | $d[s]$ | $d[a]$ | $d[b]$ | $d[c]$ | $d[t]$ | What changed |
|---|---|---|---|---|---|---|
| 0 | $0$ | $\infty$ | $\infty$ | $\infty$ | $\infty$ | initialise |
| 1 | $0$ | $6 \to 3$ | $7 \to 5$ | $3$ | $8$ | $sb$ sets $7$, then $sc$ sets $c=3$, $cb$ lowers $b$ to $5$, $ba$ lowers $a$ to $3$, $at$ sets $t = 8$ |
| 2 | $0$ | $3$ | $5$ | $3$ | $8$ | nothing changes; stop |

The final distances are $d(s) = 0$, $d(a) = 3$, $d(b) = 5$, $d(c) = 3$, $d(t) = 8$. The shortest $s$–$t$ path is $s \to c \to b \to a \to t$, of weight $3 + 2 - 2 + 5 = 8$ ✓.

There is no negative cycle: the only cycles are $s$–$c$–$b$–$s$ of weight $3+2+7 = 12$ and $s$–$c$–$b$–$a$–$?$ — there is no arc back from $a$ to $s$, and no other cycle exists. All are positive, so the detection pass finds no relaxable edge and the algorithm terminates normally.

*Remark.* Pass $2$ changed nothing, which is the early-termination test of Corollary 7.12.4. Had the edge $ba$ been processed before $sb$, pass $1$ would already have produced the final labels — the order only affects speed, not correctness.

**10.** *Strategy: find bridges first (an edge is a bridge iff it lies on no cycle), then cut vertices (a vertex is a cut vertex iff its removal increases the number of components), then read off the blocks.*

The triangles are $1$–$2$–$3$ and $4$–$5$–$6$; the remaining edges are $34$ and $27$.

*Bridges.* $34$ lies on no cycle (every cycle is inside one of the triangles, and $34$ joins them), so it is a bridge. $27$ is a pendant edge, hence a bridge. Every edge of either triangle lies on that triangle, so it is not a bridge. **Bridges: $\{34, 27\}$.**

*Cut vertices.* 
* $2$: $G - 2$ leaves $7$ isolated, so $c(G-2) = 2 > 1$; $2$ is a cut vertex.
* $3$: $G - 3$ separates $\{1,2,7\}$ from $\{4,5,6\}$; cut vertex.
* $4$: $G - 4$ separates $\{1,2,3,7\}$ from $\{5,6\}$; cut vertex.
* $1,5,6,7$: removing any of them leaves a connected graph (for $7$ the graph loses only a leaf; for $5$ or $6$ the other triangle vertex remains attached through $4$; for $1$ the triangle edge $23$ survives), so none is a cut vertex.
**Cut vertices: $\{2,3,4\}$.**

*Blocks.* The maximal subgraphs without a cut vertex are the two triangles $\{1,2,3\}$ and $\{4,5,6\}$, and the two bridges as subgraphs on two vertices: $\{34\}$ and $\{27\}$. That is $4$ blocks, and every edge lies in exactly one of them ✓.

*Block-cut tree.* Block nodes $B_1 = \{1,2,3\}$, $B_2 = \{4,5,6\}$, $B_3 = \{34\}$, $B_4 = \{27\}$; cut-vertex nodes $2,3,4$. Incidence: $B_1$ with $2$ and $3$; $B_2$ with $4$; $B_3$ with $3$ and $4$; $B_4$ with $2$. As a tree:
$$B_4 \;-\; 2 \;-\; B_1 \;-\; 3 \;-\; B_3 \;-\; 4 \;-\; B_2 .$$
It has $7$ nodes and $6$ edges, is connected and acyclic ✓, as Theorem 7.16.3 requires.

**11.** *Strategy: $\delta$ from the degree sequence; $\lambda$ from the smallest edge cut (often the edges at a minimum-degree vertex); $\kappa$ from the smallest vertex cut (cut vertices, or a small separator).*

| Graph | $\delta$ | $\lambda$ | $\kappa$ | Reason |
|---|---|---|---|---|
| $K_4$ | $3$ | $3$ | $3$ | complete: $\kappa = \lambda = n-1$ |
| $C_6$ | $2$ | $2$ | $2$ | every vertex has degree $2$; deleting two non-adjacent vertices disconnects |
| $K_{2,3}$ | $2$ | $2$ | $2$ | $\delta = 2$; the two vertices of the part of size $2$ form a separator; no single vertex or edge disconnects |
| $K_{1,4}$ | $1$ | $1$ | $1$ | the centre is a cut vertex and every edge is a bridge |
| $P_5$ | $1$ | $1$ | $1$ | internal vertices are cut vertices, every edge is a bridge |

Whitney's inequality $\kappa \le \lambda \le \delta$ holds with equality in all five cases; strictness requires larger examples (Examples 7.14.4 and 7.14.5).

*Note on $K_{2,3}$.* Removing one vertex of the size-$3$ part leaves $K_{2,2}$, which is connected; removing one vertex of the size-$2$ part leaves a star $K_{1,3}$, connected. So $\kappa \ge 2$, and the two vertices of the size-$2$ part form a separator, so $\kappa = 2$. For edges: every edge lies on a $4$-cycle, so there is no bridge, and the two edges at a vertex of the size-$3$ part do not disconnect (the other vertex of the size-$2$ part still connects everything). Deleting the two edges at a vertex $y$ of the size-$3$ part isolates $y$, so $\lambda = 2$.

**12.** *Strategy: match the problem's requirements (single source or all pairs, negative weights, connectivity versus routing) to the algorithms of Sections 7.5, 7.10–7.14.*

(a) **Dijkstra with a binary heap**, $O((n+m)\log n)$; with a Fibonacci heap, $O(m + n\log n)$. A sparse graph is exactly where the heap version pays off.

(b) **Bellman–Ford**, $O(nm)$. It tolerates negative weights and its $n$-th pass detects a negative cycle reachable from the source. If the graph is sparse and all pairs are wanted, Johnson's algorithm ($O(nm + n^2\log n)$) reweights with one Bellman–Ford run and then runs Dijkstra $n$ times.

(c) **Floyd–Warshall**, $\Theta(n^3) = 2.7\times 10^7$ elementary operations for $n = 300$, which is fast; its $O(n^2)$ memory is modest. Johnson's algorithm would be better only if the graph were very sparse.

(d) **Hierholzer's algorithm**, $O(n+m)$, after checking the degree condition. Fleury's algorithm is correct but $O(m^2)$ with a naive bridge test.

(e) **Tarjan's lowlink algorithm** (a single depth-first search), $O(n+m)$.

(f) **Max-flow with vertex splitting**: compute $\lambda(s,v)$ for a fixed vertex $s$ and every other $v$, and take the minimum; equivalently split each vertex $x \notin \{s,v\}$ into $x^{-} \to x^{+}$ with capacity $1$. With at most $n-1$ flow computations, each of value at most $n$ and costing $O(nm)$ by augmenting paths, the total is polynomial — about $O(n^2m)$, entirely practical for $n = 100$, $m = 400$. (The exact value of $\kappa$ is always at most $n-1$, so the number of augmentations per flow is small.)

## Intermediate

**13.** *Strategy: count the edges of the circuit at each vertex. This is the argument of Section 7.1 in general form.*

Let $C = v_0e_1v_1e_2\cdots e_mv_0$ be an Eulerian circuit, so $e_1,\dots,e_m$ are exactly the edges of $G$, each once.

*Connectivity.* Every edge of $G$ is one of the $e_i$. The subgraph formed by the edges of $C$ is connected, because the walk visits every one of its vertices consecutively: $v_{i-1}$ and $v_i$ are joined by $e_i$ for each $i$, so the whole sequence lies in a single component. Since that subgraph is $G$ itself (all edges are present), $G$ has one component containing all edges.

*Parity.* Fix a vertex $x$ and let $r$ be the number of indices $i \in \{0,\dots,m-1\}$ with $v_i = x$. Consider the $2r$ edges
$$e_1, e_2, \dots \text{ at each occurrence of } x,$$
more precisely: for each occurrence $v_i = x$ with $0 \le i \le m-1$, take the edge $e_i$ (entering $x$ from $v_{i-1}$) and the edge $e_{i+1}$ (leaving $x$ towards $v_{i+1}$), where indices are read modulo $m$ so that $e_{m+1} := e_1$. These $2r$ positions are distinct: the entering edge at occurrence $i$ is $e_i$ and the leaving edge is $e_{i+1}$, and different occurrences $i \ne j$ give different edge indices $e_i \ne e_j$. Each edge of $C$ incident with $x$ is of one of these two kinds, because an edge $e_k$ incident with $x$ has $x$ as one of its endpoints $v_{k-1}, v_k$, so it is the entering edge at occurrence $k$ or the leaving edge at occurrence $k-1$. Hence the number of edges at $x$ is exactly $2r$, which is even.

This covers the starting vertex too: with indices read modulo $m$, the occurrence $i = 0$ contributes the entering edge $e_m$ and the leaving edge $e_1$, and these are distinct because $m \ge 1$. $\blacksquare$

**14.** *Strategy: first prove the closure lemma by counting used edges at each vertex, then run the splicing induction.*

**Lemma.** Let every vertex of $G$ have even degree, $m \ge 1$, and let $W = v_0e_1v_1\cdots e_kv_k$ be a trail that cannot be extended at $v_k$. Then $v_k = v_0$.

*Proof.* For a vertex $x$, let $u(x)$ be the number of edges of $W$ incident with $x$, and write $[P]$ for $1$ when the statement $P$ is true and $0$ otherwise. We claim
$$u(x) \equiv \begin{cases} 0 \pmod 2, & x \notin \{v_0,v_k\}, \\ 1 \pmod 2, & x \in \{v_0,v_k\},\ v_0 \ne v_k, \\ 0 \pmod 2, & x = v_0 = v_k. \end{cases}$$
Indeed, each internal occurrence of $x$ in $v_1,\dots,v_{k-1}$ contributes exactly two edges ($e_i$ and $e_{i+1}$); the first edge $e_1$ contributes one at $v_0$, the last edge $e_k$ contributes one at $v_k$, and every edge of $W$ is accounted for exactly once by this classification (an edge $e_i$ contributes to $v_{i-1}$ as an outgoing and to $v_i$ as an incoming, except the first and last which contribute once). Summing: $u(x) = 2\cdot(\text{internal occurrences}) + [x = v_0] + [x = v_k]$, and the two indicator terms are $2$ when $v_0 = v_k = x$, $1$ when exactly one of them is $x$, and $0$ otherwise.

Now suppose $v_k \ne v_0$. Then $u(v_k)$ is odd, while $\deg(v_k)$ is even, so $u(v_k) \le \deg(v_k) - 1 < \deg(v_k)$: there is an unused edge at $v_k$, and $W$ could be extended, contradicting maximality. Therefore $v_k = v_0$. $\;\square$

**Theorem (sufficiency).** Let $G$ be connected with $m \ge 1$ and all degrees even. Then $G$ has an Eulerian circuit.

*Proof.* We describe a procedure and prove it terminates with the required circuit.

*Step 1.* Start at any vertex $v_0$ of positive degree and extend a trail by unused edges until no unused edge remains at the current vertex. By the lemma, the trail $C$ is closed.

*Step 2 (the splicing claim).* If some edge is unused, then some vertex of $C$ is incident with an unused edge. Proof: pick an unused edge $ab$. Since $G$ is connected, there is a path $v_0 = p_0, p_1, \dots, p_r = a$. Let $j$ be the largest index with $p_j$ lying on $C$ (such an index exists because $p_0 = v_0$ is on $C$), and set $w = p_j$, $w' = p_{j+1}$. The edge $ww'$ is not an edge of $C$: if it were, then $w'$ would be a vertex of $C$, contradicting the maximality of $j$ (note $j < r$ since $a$ may or may not be on $C$, but if $p_{j+1}$ were on $C$ then $j+1$ would be a larger index). Hence $w$ lies on $C$ and is incident with the unused edge $ww'$.

*Step 3 (splice).* Delete from $G$ all edges of $C$, obtaining $G'$. Every vertex of $G'$ has even degree: a vertex $x$ loses $u(x)$ edges, which is even by the lemma, and degrees of vertices not on $C$ are unchanged. Let $H$ be the component of $G'$ containing the vertex $w$ found in Step 2; every degree in $H$ is even and $H$ has at least one edge ($ww'$), so by Step 1 applied inside $H$ there is a closed trail $C'$ from $w$ using only edges of $H$. Form the closed trail $C \cdot C'$: walk $C$ from $v_0$ to $w$, then $C'$, then the remainder of $C$ from $w$ back to $v_0$. It is a trail because $C$ and $C'$ have no edge in common and each is a trail.

*Step 4 (termination).* Each splice strictly increases the number of edges used, so after at most $m$ splices no unused edge remains. The resulting closed trail uses every edge exactly once: an Eulerian circuit. $\blacksquare$

*Remark.* The procedure is exactly Hierholzer's algorithm; Step 2 is the only place where connectivity is used, and Step 1 is the only place where evenness is used.

**15.** *Strategy: necessity by the endpoint count; sufficiency by adding a dummy edge and applying Theorem 7.2.3.*

*Necessity.* Let $W$ be an Eulerian trail from $u$ to $v$. If $u = v$, $W$ is an Eulerian circuit and Theorem 7.2.1 gives all degrees even. If $u \ne v$, apply the counting of the lemma in Solution 14 to $W$ (which uses every edge): for every vertex $x \notin \{u,v\}$ the number of incident edges is $2\cdot(\text{internal occurrences})$, hence even; for $u$ and $v$ it is $2\cdot(\text{internal occurrences}) + 1$, hence odd. So the number of odd vertices is exactly $2$.

*Sufficiency.* If every degree is even, Theorem 7.2.3 gives a circuit, which is a trail with $0$ odd vertices. If exactly $u \ne v$ are odd, form $G^{+}$ by adding a new edge $e_0$ between $u$ and $v$ (a parallel edge if $uv$ already exists). Every degree of $G^{+}$ is even, and $G^{+}$ is connected, so $G^{+}$ has an Eulerian circuit $C^{+}$. Deleting $e_0$ from $C^{+}$ leaves a trail in $G$ that uses every edge of $G$ exactly once: an Eulerian trail. Its endpoints are the endpoints of $e_0$, that is $u$ and $v$.

*Deduction.* If $G$ has exactly two odd vertices $u,v$, the necessity argument applied to any Eulerian trail shows that the trail's start and end are precisely the odd vertices. So every Eulerian trail runs between $u$ and $v$; none can be closed, and none can start at a vertex of even degree. $\blacksquare$

**16.** *Strategy: (a) an Eulerian circuit minus a bridge would give a path across the cut; (b) find a graph with no bridges and odd degrees.*

(a) Suppose $e = uv$ is a bridge of a connected Eulerian graph $G$ with $m \ge 1$. Let $C$ be an Eulerian circuit and delete the single occurrence of $e$ from it: the remaining edges of $C$ form a $u$–$v$ trail $W$ in $G - e$ (walk $C$ from one endpoint of $e$ to the other). A trail is a walk, and a walk between $u$ and $v$ lies entirely in one component of $G - e$ and connects them; so $G - e$ is connected, contradicting that $e$ is a bridge.

*Alternative.* $G - e$ has two components. Each component contains exactly one of $u,v$ (since $e$ crosses the cut). Within a component, all degrees are even except possibly at the endpoint of $e$, so the component has exactly one odd-degree vertex, contradicting the handshake lemma. $\blacksquare$

(b) $K_4$: every edge lies on a triangle ($12$ on $1$–$2$–$3$–$1$, and similarly by symmetry), so $K_4$ has no bridge; but every degree is $3$, which is odd, so $K_4$ has no Eulerian circuit. Hence "every edge on a cycle" (equivalently, no bridge, by Solution 20) is strictly weaker than "Eulerian".

**17.** *Strategy: (a) restrict the Hamiltonian cycle to $V \setminus S$ and count its pieces; (b) choose $S$ to be a small part; (c) a necessary condition derived from cycles cannot see all obstructions.*

(a) Let $C$ be a Hamiltonian cycle and $S \subseteq V$ with $k = \lvert S\rvert$. Removing the $k$ vertices of $S$ from the cycle $C$ removes $k$ vertices and the $2k$ edges incident with them (some edges counted twice if two vertices of $S$ are adjacent, in which case fewer than $2k$ distinct edges are removed). What remains of $C$ is a disjoint union of paths: between consecutive deleted vertices along the cycle there is a maximal segment of undeleted vertices, and there are at most $k$ such segments (one per gap). Hence
$$c(C - S) \le k .$$
Each component of $C - S$ is a connected subgraph of $G - S$, hence lies in a single component of $G - S$; distinct components of $C - S$ may lie in the same component of $G - S$, but not conversely, so $c(G - S) \le c(C - S)$. Therefore
$$c(G - S) \le c(C - S) \le \lvert S\rvert . \qquad \blacksquare$$

(b) Let $K_{2,3}$ have parts $X = \{x_1,x_2\}$ and $Y = \{y_1,y_2,y_3\}$, and take $S = X$. Then $G - S$ has vertex set $Y$ and no edges (all edges of $K_{2,3}$ join $X$ to $Y$), so $c(G - S) = 3 > 2 = \lvert S\rvert$. The cut condition fails, so $K_{2,3}$ is not Hamiltonian ✓ — consistent with Proposition 7.7.3.

(c) The condition is *necessary* but cannot be *sufficient*. A direct witness is the Petersen graph: it satisfies $c(G - S) \le \lvert S\rvert$ for every $S \subseteq V$ (it is 1-tough — a standard fact, see Diestel, *Graph Theory*, §1.3, or Holton and Sheehan, *The Petersen Graph*) and it has no Hamiltonian cycle (Solution 31). So no condition of this form can characterise Hamiltonicity; it records only how a cycle must cross each cut, which is a small part of the global structure.

**18.** *Strategy: (a) a cycle alternates between the parts; (b) apply (a); (c) verify both sides.*

(a) Let $G$ be bipartite with parts $X,Y$ and let $C = v_0v_1\cdots v_{n-1}v_0$ be a Hamiltonian cycle. Since consecutive vertices of a cycle are adjacent and every edge joins $X$ to $Y$, the parts alternate: $v_0 \in X$ implies $v_1 \in Y$, $v_2 \in X$, and so on. The cycle has $n$ vertices, so it contains $\lceil n/2\rceil$ vertices of one part and $\lfloor n/2\rfloor$ of the other; since it contains all vertices, $\lvert X\rvert = \lvert Y\rvert = n/2$. In particular $n$ is even. $\blacksquare$

(b) The Herschel graph has parts of sizes $6$ and $5$, which are unequal, so by (a) it is not Hamiltonian. (It is the smallest non-Hamiltonian 3-connected planar graph, which is why it is the standard example that 3-connected planarity does not force a Hamiltonian cycle.)

(c) $K_{3,3}$ has parts of size $3$ each, so the balance condition holds; and $x_1y_1x_2y_2x_3y_3x_1$ is a Hamiltonian cycle ✓. So balance is satisfied by a Hamiltonian graph and violated by a non-Hamiltonian one — it is necessary, not sufficient.

**19.** *Strategy: $\lambda \le \delta$ from the edges at a minimum-degree vertex; $\kappa \le \lambda$ by choosing one endpoint of each cut edge, avoiding two chosen vertices.*

**$\lambda \le \delta$.** Let $v$ be a vertex of minimum degree $\delta(G)$. The set $F = \delta(\{v\})$ of edges at $v$ has $\lvert F\rvert = \deg(v) = \delta(G)$, and $G - F$ has $v$ isolated. If $n \ge 2$ then $G - F$ is disconnected (or has an isolated vertex plus at least one other), so $F$ is an edge cut and $\lambda(G) \le \lvert F\rvert = \delta(G)$. (If $G = K_1$ both are $0$.)

**$\kappa \le \lambda$.** If $G$ is complete, $\kappa(G) = \lambda(G) = n-1$. Otherwise let $F$ be a minimum edge cut, $\lvert F\rvert = \lambda(G)$, and let $X$ be the vertex set of one component of $G - F$; put $Y = V \setminus X$. Both $X$ and $Y$ are non-empty, and every edge with one endpoint in $X$ and one in $Y$ belongs to $F$ (and, since $F$ is a cut, $F$ consists exactly of such edges).

Choose $x_0 \in X$ and $y_0 \in Y$. For each edge $f = xy \in F$ with $x \in X$, $y \in Y$, choose the endpoint of $f$ that is not $x_0$ and not $y_0$: at most one of $x,y$ can lie in $\{x_0,y_0\}$, so such an endpoint exists. Let $S$ be the set of chosen endpoints; then $\lvert S\rvert \le \lvert F\rvert = \lambda(G)$.

Now $x_0 \notin S$ and $y_0 \notin S$ by construction. In $G - S$ there is no $X$–$Y$ edge: every such edge lies in $F$ and has its chosen endpoint removed. Since $X$ and $Y$ partition $V$ and neither $x_0$ nor $y_0$ is removed, $G - S$ is disconnected (no path can cross from $X \setminus S$ to $Y \setminus S$). Hence $S$ is a vertex cut and $\kappa(G) \le \lvert S\rvert \le \lambda(G)$. $\blacksquare$

*Remark.* The construction needs both parts to keep a surviving vertex, which is why $x_0$ and $y_0$ are excluded from the choice; this is the step that many sketch proofs get wrong.

**20.** *Strategy: (a) a cycle through $e$ gives an alternative route; (b) a component split gives the two vertices.*

(a) Let $e = uv$.
*If $e$ lies on a cycle $C$*, then $C - e$ is a $u$–$v$ path, so $G - e$ is connected: every vertex of $C$ is reachable along the path, and every other vertex of $G$ was already reachable from $C$ in $G$ by a path that does not use $e$ (a path can be chosen to avoid $e$ unless it is the edge itself, since $e$'s removal only splits $u$ from $v$ along the direct edge). More carefully: $G$ connected and $G - e$ containing a $u$–$v$ path implies $G - e$ connected, because any $G$-path that uses $e$ can be rerouted along that path. Hence $e$ is not a bridge.
*Conversely, if $e$ is not a bridge*, then $G - e$ is connected, so there is a $u$–$v$ path $P$ in $G - e$; then $P + e$ is a cycle through $e$. $\blacksquare$

(b) *If every $u$–$w$ path passes through $v$*, then in $G - v$ there is no $u$–$w$ path, so $u$ and $w$ lie in different components of $G - v$, which is therefore disconnected: $v$ is a cut vertex.
*Conversely, if $v$ is a cut vertex*, $G - v$ has at least two components; choose $u$ in one and $w$ in another. Any $u$–$w$ path in $G$ that avoided $v$ would be a path in $G - v$, contradicting that $u,w$ are in different components. So every $u$–$w$ path passes through $v$. $\blacksquare$

**21.** *Strategy: induction on the pass number, splitting the optimal walk according to its last edge.*

**Claim.** After the $k$-th pass: (i) $d[v]$ is the weight of some $s$–$v$ walk (or $\infty$); (ii) $d[v] \le w(W)$ for every $s$–$v$ walk $W$ with at most $k$ edges.

*Base $k = 0$.* Before any pass, $d[s] = 0$ (the empty walk) and $d[v] = \infty$ for $v \ne s$ (no walk). There are no walks of length $0$ from $s$ to $v \ne s$, so (ii) is vacuous there.

*Step.* Assume the claim after pass $k-1$; consider pass $k$ and a vertex $v$. Property (i) is clear: a label is only ever set to $d[u] + w(uv)$ where, by the induction hypothesis, $d[u]$ is a walk weight, so the new label is the weight of a walk ending with the edge $uv$.

For (ii), let $W$ be an $s$–$v$ walk of minimum weight among those with at most $k$ edges. If $W$ has at most $k-1$ edges, the induction hypothesis gives $d[v] \le w(W)$ already after pass $k-1$, and labels never increase during a pass (only strict improvements are assigned). Otherwise $W$ has exactly $k$ edges and ends with an edge $uv$: $W = W' + uv$, where $W'$ is an $s$–$u$ walk with $k-1$ edges. By induction $d[u] \le w(W')$ at the end of pass $k-1$, and during pass $k$ the edge $uv$ is relaxed at some moment. At that moment the label of $u$ is at most its value at the end of pass $k-1$ (labels never increase), so after relaxing,
$$d[v] \le d[u] + w(uv) \le w(W') + w(uv) = w(W). \qquad \blacksquare$$

**22.** *Strategy: run the recurrence with $k$ outermost, updating only entries that improve.*

$$D^{(0)} = \begin{pmatrix} 0 & 2 & 9 & \infty \\ \infty & 0 & 3 & \infty \\ 4 & \infty & 0 & 2 \\ 8 & 5 & \infty & 0 \end{pmatrix}$$

*Round $k=1$* (intermediate vertex $1$). Entries improve when $D[i][1] + D[1][j] < D[i][j]$: row $3$ gives $D[3][2] = \min(\infty, 4+2) = 6$, and row $4$ gives $D[4][3] = \min(\infty, 8+9) = 17$. No other entry improves.

$$D^{(1)} = \begin{pmatrix} 0 & 2 & 9 & \infty \\ \infty & 0 & 3 & \infty \\ 4 & 6 & 0 & 2 \\ 8 & 5 & 17 & 0 \end{pmatrix}$$

*Round $k=2$.* Row $1$: $D[1][3] = \min(9, 2+3) = 5$. Row $4$: $D[4][3] = \min(17, 5+3) = 8$.

$$D^{(2)} = \begin{pmatrix} 0 & 2 & 5 & \infty \\ \infty & 0 & 3 & \infty \\ 4 & 6 & 0 & 2 \\ 8 & 5 & 8 & 0 \end{pmatrix}$$

*Round $k=3$.* Row $1$: $D[1][4] = \min(\infty, 5+2) = 7$. Row $2$: $D[2][1] = \min(\infty, 3+4) = 7$, $D[2][4] = \min(\infty, 3+2) = 5$.

$$D^{(3)} = \begin{pmatrix} 0 & 2 & 5 & 7 \\ 7 & 0 & 3 & 5 \\ 4 & 6 & 0 & 2 \\ 8 & 5 & 8 & 0 \end{pmatrix}$$

*Round $k=4$.* Row $1$: $D[1][3] = \min(5, 7+8) = 5$ (no change), $D[1][2] = \min(2, 7+5) = 2$. Row $2$: $D[2][3] = \min(3, 5+8) = 3$. Row $3$: $D[3][1] = \min(4, 2+8) = 4$, $D[3][2] = \min(6, 2+5) = 6$. So

$$D^{(4)} = \begin{pmatrix} 0 & 2 & 5 & 7 \\ 7 & 0 & 3 & 5 \\ 4 & 6 & 0 & 2 \\ 8 & 5 & 8 & 0 \end{pmatrix} = D^{(3)} .$$

*Verification of two entries.* $D[1][4] = 7$ is realised by $1 \to 2 \to 3 \to 4$ of weight $2+3+2 = 7$ ✓; any route must leave $1$ through $2$ or $3$, and $2 \to 3 \to 4 = 5$ is cheaper than $1 \to 3$ followed by $3 \to 4 = 11$, so $7$ is minimal ✓. $D[2][1] = 7$ is realised by $2 \to 3 \to 1$ of weight $3+4 = 7$ ✓, and $2 \to 3 \to 4 \to 1$ costs $3+2+8 = 13$, so $7$ is minimal ✓.

*No negative cycle.* The diagonal of $D^{(4)}$ is $0$ everywhere, so by Corollary 7.13.2 no vertex lies on a negative cycle. One also checks directly: the cycles are $1\to2\to3\to1$ of weight $9$, $1\to3\to1$ of weight $13$, $2\to3\to4\to2$ of weight $10$, and $1\to2\to3\to4\to1$ of weight $15$, all positive ✓.

## Advanced

**23.** *Strategy: pass to a maximal non-Hamiltonian supergraph, then use the rotation argument on a Hamiltonian path of that supergraph.*

Suppose the theorem false. Among all non-Hamiltonian graphs on the vertex set $V$ that contain $G$, choose $G'$ with as many edges as possible. Adding edges cannot decrease a degree and cannot create new non-adjacent pairs, so $G'$ satisfies the same hypothesis: $\deg_{G'}(u) + \deg_{G'}(v) \ge n$ for every pair of non-adjacent vertices.

Since $G'$ is non-Hamiltonian and maximal, for every non-adjacent pair $u,v$ the graph $G' + uv$ has a Hamiltonian cycle. That cycle must use the new edge $uv$ (otherwise it would already be a cycle of $G'$), so deleting $uv$ from it gives a Hamiltonian path
$$v_1v_2\cdots v_n \qquad \text{with } v_1 = u,\ v_n = v .$$

**Claim.** There is no index $i$ with $1 \le i \le n-2$ such that $uv_{i+1} \in E(G')$ and $v_iv \in E(G')$.

Suppose such an $i$ exists. Then the cyclic sequence
$$v_1,\ v_{i+1},\ v_{i+2},\ \dots,\ v_n,\ v_i,\ v_{i-1},\ \dots,\ v_2,\ v_1$$
is a Hamiltonian cycle: the consecutive pairs are $v_1v_{i+1}$ (present by hypothesis), the path edges $v_{i+1}v_{i+2}, \dots, v_{n-1}v_n$ (present), the edge $v_nv_i$ (present by hypothesis), and the path edges $v_iv_{i-1}, \dots, v_2v_1$ (present). It visits $v_1$, then $v_{i+1},\dots,v_n$, then $v_i,\dots,v_2$: all $n$ vertices exactly once ✓. This contradicts the non-Hamiltonicity of $G'$. $\;\diamond$

Now put
$$A = \{i : 1 \le i \le n-2,\ uv_{i+1} \in E(G')\}, \qquad B = \{i : 1 \le i \le n-2,\ v_iv \in E(G')\}.$$
Both are subsets of the $(n-2)$-element set $\{1,\dots,n-2\}$, and the claim says $A \cap B = \varnothing$.

*Size of $A$.* The neighbours of $u = v_1$ in $G'$ are some of $v_2,\dots,v_{n-1}$; the vertex $v_n = v$ is not a neighbour, by assumption. Each neighbour $v_{i+1}$ corresponds to exactly one $i \in \{1,\dots,n-2\}$, so $\lvert A\rvert = \deg_{G'}(u)$.

*Size of $B$.* The neighbours of $v = v_n$ are some of $v_1,\dots,v_{n-1}$; the vertex $v_{n-1}$ is a neighbour (path edge) but its index $n-1$ is outside the range, so the indices in $B$ count the remaining neighbours: $\lvert B\rvert = \deg_{G'}(v) - 1$.

Therefore
$$\deg_{G'}(u) + \deg_{G'}(v) - 1 = \lvert A\rvert + \lvert B\rvert \le n-2,$$
since $A$ and $B$ are disjoint subsets of an $(n-2)$-element set. Hence $\deg_{G'}(u) + \deg_{G'}(v) \le n-1 < n$, contradicting the hypothesis. So no counterexample exists and $G$ is Hamiltonian. $\blacksquare$

**24.** *Strategy: Dirac is the special case of Ore in which every degree is at least $n/2$; then compare with a cycle.*

**Dirac from Ore.** Assume $n \ge 3$ and $\delta(G) \ge n/2$. For any two non-adjacent vertices $u,v$,
$$\deg(u) + \deg(v) \ge 2\delta(G) \ge n,$$
so Ore's hypothesis holds and Theorem 7.8.1 (Solution 23) gives a Hamiltonian cycle. $\blacksquare$

**The cycle $C_n$, $n \ge 5$.** $C_n$ is Hamiltonian, but $\delta(C_n) = 2 < n/2$, so Dirac's hypothesis fails. For non-adjacent $u,v$ on $C_n$ we have $\deg(u) + \deg(v) = 4 < n$ (since $n \ge 5$), so Ore's hypothesis fails too. Both theorems are therefore *not necessary*, and the gap is not a matter of a lucky constant.

**Why no constant repairs this.** Consider a hypothesis of the form $\delta(G) \ge f(n)$, and suppose it were necessary for Hamiltonicity. Then every Hamiltonian graph, in particular $C_n$, would satisfy it, forcing $f(n) \le 2$ for all $n \ge 5$. But with $f(n) \le 2$ the hypothesis is satisfied by the bowtie (two triangles sharing a vertex), which has $\delta = 2$ and is not Hamiltonian because it has a cut vertex. So no degree threshold can be both necessary and sufficient.

The same argument works for Ore-type thresholds $g(n)$: necessity would force $g(5) \le 4$ (all non-adjacent pairs of $C_5$ have degree sum $4$), but the bowtie has $n = 5$ and every non-adjacent pair has degree sum $4$, so it would satisfy the hypothesis while being non-Hamiltonian. Hence no condition of the form "$\deg u + \deg v \ge g(n)$ for all non-adjacent $u,v$" can characterise Hamiltonicity either. $\blacksquare$

**25.** *Strategy: the non-trivial direction is that a Hamiltonian cycle using the new edge can be rotated into one avoiding it.*

Let $u,v$ be non-adjacent with $\deg(u) + \deg(v) \ge n$.

*If $G$ is Hamiltonian, then $G + uv$ is*: the same cycle works. That direction is immediate.

*Conversely, suppose $G + uv$ has a Hamiltonian cycle.* If the cycle does not use $uv$, it is a Hamiltonian cycle of $G$ and there is nothing to prove. Otherwise delete $uv$ from the cycle: the result is a Hamiltonian path
$$v_1v_2\cdots v_n \quad\text{with } v_1 = u,\ v_n = v .$$
Define $A$ and $B$ as in Solution 23. Since $uv \notin E(G)$, the vertex $v_n$ is not a neighbour of $v_1$, so $\lvert A\rvert = \deg_G(u)$; and $v_{n-1}$ is a neighbour of $v_n$ but excluded from the index range, so $\lvert B\rvert = \deg_G(v) - 1$. If $A \cap B \ne \varnothing$, say $i \in A \cap B$, then the rotation of Solution 23 produces a Hamiltonian cycle of $G$ (all its edges are edges of $G$, since $uv$ is not used) ✓. If $A \cap B = \varnothing$, then
$$\deg_G(u) + \deg_G(v) - 1 = \lvert A\rvert + \lvert B\rvert \le n-2,$$
so $\deg_G(u) + \deg_G(v) \le n-1$, contradicting the hypothesis. Hence $A \cap B \ne \varnothing$ and $G$ is Hamiltonian. $\blacksquare$

*Remark.* Iterating the lemma adds edges for as long as some non-adjacent pair has degree sum at least $n$; the resulting graph is the **closure** $\operatorname{cl}(G)$, and the lemma shows that $G$ is Hamiltonian if and only if $\operatorname{cl}(G)$ is. Ore's theorem is the case where the closure is complete.

**26.** *Strategy: a Hamiltonian cycle through the new universal vertex is a Hamiltonian path in $G$ once the vertex is deleted, and conversely.*

Let $w$ be the new vertex of $G \vee K_1$, adjacent to every vertex of $G$.

*If $G$ has a Hamiltonian path* $v_1v_2\cdots v_n$, then
$$v_1v_2\cdots v_n\,w\,v_1$$
is a Hamiltonian cycle of $G \vee K_1$: all edges $v_iv_{i+1}$ lie in $G$, and $v_nw$, $wv_1$ are edges of the join ✓.

*If $G \vee K_1$ has a Hamiltonian cycle* $C$, then $C$ passes through $w$ (it contains all vertices), and its two neighbours on $C$ are two vertices of $G$. Deleting $w$ and its two incident cycle edges leaves a path through all $n$ vertices of $G$: a Hamiltonian path ✓.

*Reduction.* The map $G \mapsto G \vee K_1$ is computable in time $O(n)$ from an adjacency list (add one vertex and $n$ edges), and it preserves the answer in both directions, so it is a polynomial-time reduction from Hamiltonian Path to Hamiltonian Cycle. A Hamiltonian path is an NP-certificate checkable in $O(n)$ time, so Hamiltonian Path lies in NP; since Hamiltonian Cycle is NP-complete (Section 7.9), Hamiltonian Path is NP-complete as well. $\blacksquare$

**27.** *Strategy: (⇒) two internally disjoint paths give a cycle; (⇐) a cycle survives the deletion of any one vertex.*

*Assume $G$ is 2-connected*, so $n \ge 3$ and $\kappa(G) \ge 2$. Let $u \ne v$ be vertices. By the global form of Menger's theorem (Theorem 7.15.3(b)) with $k = 2$, there are two internally vertex-disjoint $u$–$v$ paths $P_1, P_2$ (if $uv$ is an edge, one of them is that edge). Their union is a connected subgraph in which every vertex other than $u$ and $v$ has degree $2$ and $u,v$ have degree $2$; hence it is a cycle containing $u$ and $v$ ✓.

*Assume every two vertices lie on a common cycle.* First, $G$ is connected: any two vertices lie on a cycle, hence are joined by a path. Now let $x$ be any vertex and $u,v$ any two vertices different from $x$. By hypothesis $u$ and $v$ lie on a common cycle $C$. If $x \notin V(C)$, then $C \subseteq G - x$ joins $u$ and $v$. If $x \in V(C)$, then $C - x$ is a path (a cycle minus one vertex) joining $u$ and $v$ inside $G - x$. So any two vertices of $G - x$ are joined in $G - x$, which is therefore connected. Hence $G$ has no cut vertex and $\kappa(G) \ge 2$: $G$ is 2-connected ✓. $\blacksquare$

*Remark.* The proof of the forward direction uses Menger's theorem; a direct proof is possible by induction on the distance between $u$ and $v$, but it is longer.

**28.** *Strategy: use the equivalence "bridge iff on no cycle" (Solution 20) and the characterisation $\lambda = 1$ iff a bridge exists.*

*If $G$ is 2-edge-connected*, then $\lambda(G) \ge 2$, so $G$ has no cut consisting of a single edge, that is, no bridge. By Solution 20(a), every edge lies on a cycle.

*Conversely, if every edge lies on a cycle*, then no edge is a bridge (Solution 20(a) again), so $\lambda(G) \ne 1$. Since $G$ is connected with at least two vertices, $\lambda(G) \ge 1$, hence $\lambda(G) \ge 2$ ✓. $\blacksquare$

*Remark.* For a connected graph with at least two vertices, the three statements "$\lambda \ge 2$", "no bridge", "every edge lies on a cycle" are therefore equivalent.

**29.** *Strategy: connectedness from chains of blocks along paths in $G$; acyclicity from the fact that a cycle of blocks would merge into a larger block.*

Let $\operatorname{BC}(G)$ have as vertices the blocks of $G$ and the cut vertices of $G$, with an incidence edge $B \sim v$ when $v \in V(B)$.

*Connected.* Let $B_1, B_2$ be blocks. Pick $u \in V(B_1)$ and $w \in V(B_2)$ and a path $P$ from $u$ to $w$ in $G$ (possible since $G$ is connected). Each edge of $P$ lies in a unique block (Proposition 7.16.2), so $P$ determines a sequence of blocks $B_1 = C_0, C_1, \dots, C_r = B_2$ in which consecutive blocks share the vertex between consecutive edges of $P$; that shared vertex is a cut vertex whenever $C_{i-1} \ne C_i$ (Proposition 7.16.2). So the corresponding vertices of $\operatorname{BC}(G)$ form a walk from $B_1$ to $B_2$, and $\operatorname{BC}(G)$ is connected.

*Acyclic.* Suppose, for contradiction, that $\operatorname{BC}(G)$ contains a cycle. Its vertices alternate between blocks and cut vertices (the graph is bipartite by construction), so it has the form
$$B_1,\ c_1,\ B_2,\ c_2,\ \dots,\ B_r,\ c_r,\ B_1$$
with $r \ge 2$, the $B_i$ distinct blocks and the $c_i$ distinct cut vertices, and $c_i \in V(B_i) \cap V(B_{i+1})$ (indices modulo $r$). Let $U = B_1 \cup B_2 \cup \cdots \cup B_r$.

$U$ is connected, since consecutive blocks share $c_i$. We show that $U$ has no cut vertex. Let $x \in V(U)$. The blocks containing $x$ are some of the $B_i$; the others are untouched by the deletion. Each $B_i$ with $x \in V(B_i)$ satisfies: $B_i - x$ is connected (a block has no cut vertex; and $B_i - x$ is non-empty because $B_i$ has at least two vertices and is 2-connected or a single edge). Moreover $B_i - x$ still contains $c_{i-1}$ and $c_i$, because $c_{i-1} \ne c_i$ (they are distinct vertices of the cycle in $\operatorname{BC}(G)$) and at most one of them equals $x$. So $B_i - x$ meets $B_{i-1} - x$ at $c_{i-1}$ and $B_{i+1} - x$ at $c_i$, and the pieces join up around the cycle into a connected graph. Any block of $U$ outside the cycle is attached through a cut vertex; but since $U$ is exactly the union of the $B_i$, there are no others. Hence $U - x$ is connected for every $x$, so $U$ has no cut vertex.

But $U$ properly contains $B_1$ (it contains $B_2$ and $c_1$, and $B_2 \not\subseteq B_1$ because distinct blocks share at most one vertex while $B_2$ has at least two vertices). This contradicts the maximality of the block $B_1$. Therefore $\operatorname{BC}(G)$ has no cycle, and being connected and acyclic it is a tree ✓. $\blacksquare$

**30.** *Strategy: (⇒) cut an Eulerian circuit at repeated vertices; (⇐) evenness plus Theorem 7.2.3.*

*If $G$ is Eulerian*, let $C$ be an Eulerian circuit. Proof by induction on $m = \lvert E\rvert$. For $m = 0$ there is nothing to prove. For $m \ge 1$, walk along $C$ and let $j$ be the smallest index $\ge 1$ such that $v_j = v_i$ for some $i < j$; such a $j$ exists because $C$ is closed ($v_m = v_0$). Then $v_i e_{i+1} v_{i+1} \cdots e_j v_j$ is a cycle: the vertices $v_i,\dots,v_{j-1}$ are distinct by minimality of $j$, and $v_j = v_i$ ✓. Remove the edges of this cycle; the remaining graph $G'$ has all degrees even (each vertex of the cycle loses exactly $2$, others lose $0$), and each component of $G'$ is Eulerian by Theorem 7.2.3 (or empty). By induction, the edges of each component partition into cycles, and adding the cycle we removed gives a partition of $E(G)$ into cycles ✓.

*If $E(G)$ partitions into cycles*, then every vertex has even degree: the cycles through a vertex $x$ each contribute exactly $2$ to $\deg(x)$ (a cycle passes through $x$ once, using two of its edges), and the cycles not through $x$ contribute nothing. Since $G$ is connected with $m \ge 1$ and all degrees are even, Theorem 7.2.3 gives an Eulerian circuit ✓. $\blacksquare$

## Challenge

**31.** *Strategy: count how many spokes a Hamiltonian cycle can use, then analyse the two remaining cases geometrically.*

Label the outer pentagon $a_0a_1a_2a_3a_4a_0$, the inner pentagram $b_0b_2b_4b_1b_3b_0$ (that is, $b_i$ is adjacent to $b_{i+2}$ and $b_{i-2}$), and the spokes $a_ib_i$; all indices are modulo $5$. Suppose $C$ is a Hamiltonian cycle, and let $k$ be the number of spokes in $C$.

**Step 1: $k$ is even and $k \le 4$.** Write $x_i = 1$ if the spoke $a_ib_i$ lies in $C$ and $x_i = 0$ otherwise, so $k = \sum_i x_i$. At the outer vertex $a_i$, exactly $2 - x_i$ of the two pentagon edges at $a_i$ belong to $C$ (each vertex has degree $3$, and exactly one incident edge is missing from $C$). Summing over the outer pentagon,
$$2e_O = \sum_{i=0}^{4} (2 - x_i) = 10 - k,$$
where $e_O$ is the number of pentagon edges of $C$, so $k$ is even. The same count in the inner pentagram gives $2e_I = 10 - k$. Since $0 \le k \le 5$ and $k$ is even, $k \in \{0,2,4\}$.

**Step 2: $k \ne 0$.** If $k = 0$, then $C$ uses only edges of the outer pentagon and the inner pentagram, which are two disjoint $5$-cycles; a single cycle cannot cover vertices of both. Contradiction.

**Step 3: $k \ne 2$.** Suppose the two spokes used are $a_ib_i$ and $a_jb_j$ with $i \ne j$. Deleting those two edges from the $10$-cycle $C$ leaves exactly two paths. Their endpoints are the four vertices $a_i, a_j, b_i, b_j$. A path that lies entirely in the outer pentagon has both endpoints among $\{a_i,a_j\}$ (its endpoints are endpoints of deleted edges, and deleted edges are the spokes); since the paths are disjoint and cover all ten vertices, one path contains all five outer vertices and the other all five inner vertices. So the outer path is a spanning path of the $5$-cycle $O$, which must be $O$ minus one edge; its endpoints $a_i, a_j$ are the endpoints of that omitted edge and are therefore adjacent in $O$, so $j \equiv i \pm 1 \pmod 5$. Similarly the inner path is $I$ minus one edge with endpoints $b_i, b_j$, so $j \equiv i \pm 2 \pmod 5$. Both cannot hold ✓. Contradiction.

**Step 4: $k \ne 4$.** Now exactly one spoke is missing from $C$; suppose it is $a_jb_j$ (we may relabel so that this is the missing spoke). Then $x_j = 0$, so $a_j$ has both pentagon edges in $C$, and every other outer vertex has exactly one pentagon edge in $C$; the number of outer pentagon edges in $C$ is $e_O = (10-4)/2 = 3$.

The two outer pentagon edges *not* in $C$ must be edges of the path $O - a_j$, whose vertices are $a_{j+1}, a_{j+2}, a_{j+3}, a_{j+4}$ and whose edges are
$$f_1 = a_{j+1}a_{j+2},\quad f_2 = a_{j+2}a_{j+3},\quad f_3 = a_{j+3}a_{j+4}.$$
Each of the four vertices $a_{j+1},\dots,a_{j+4}$ has exactly one pentagon edge in $C$, so each must be an endpoint of at least one of the two omitted edges. Among the three pairs of edges of this path, only $\{f_1, f_3\}$ covers all four vertices (the pairs $\{f_1,f_2\}$ and $\{f_2,f_3\}$ leave $a_{j+4}$ resp. $a_{j+1}$ uncovered). Hence
$$E(C) \cap E(O) = \{a_ja_{j+1},\ a_ja_{j+4},\ a_{j+2}a_{j+3}\}.$$

The same reasoning in the inner pentagram: $I - b_j$ is the path
$$b_{j+3} \;-\; b_{j+1} \;-\; b_{j+4} \;-\; b_{j+2}$$
(edges $b_{j+1}b_{j+3}$, $b_{j+1}b_{j+4}$, $b_{j+2}b_{j+4}$), and the two omitted inner edges must cover the four inner vertices, so they are $b_{j+1}b_{j+3}$ and $b_{j+2}b_{j+4}$, leaving
$$E(C) \cap E(I) = \{b_jb_{j+2},\ b_jb_{j+3},\ b_{j+1}b_{j+4}\}.$$

Now trace $C$ from $a_j$. Its two incident edges in $C$ are $a_ja_{j+1}$ and $a_ja_{j+4}$ (the spoke is missing), so locally $C$ is $a_{j+1} - a_j - a_{j+4}$. At $a_{j+1}$ the only pentagon edge in $C$ is $a_{j+1}a_j$, so the other incident edge of $C$ must be the spoke $a_{j+1}b_{j+1}$. At $b_{j+1}$ the inner edge $b_{j+1}b_{j+3}$ is omitted, so the only inner edge of $C$ at $b_{j+1}$ is $b_{j+1}b_{j+4}$, and $C$ continues to $b_{j+4}$. At $b_{j+4}$ the inner edge $b_{j+2}b_{j+4}$ is omitted, so $C$ leaves along the spoke $a_{j+4}b_{j+4}$ to $a_{j+4}$. At $a_{j+4}$ the pentagon edge $a_{j+3}a_{j+4}$ is omitted, so the only pentagon edge of $C$ at $a_{j+4}$ is $a_{j+4}a_j$, and $C$ returns to $a_j$.

So $C$ contains the closed cycle
$$a_j - a_{j+1} - b_{j+1} - b_{j+4} - a_{j+4} - a_j,$$
which has only five vertices. Since $C$ is a single cycle, $C$ equals this $5$-cycle, contradicting $\lvert V(C)\rvert = 10$ ✓.

**Conclusion.** Every possible even value of $k$ leads to a contradiction, so no Hamiltonian cycle exists. $\blacksquare$

*Remark.* The remaining five vertices $a_{j+2}, a_{j+3}, b_j, b_{j+2}, b_{j+3}$ form the other $5$-cycle $a_{j+2}-a_{j+3}-b_{j+3}-b_j-b_{j+2}-a_{j+2}$, so the $2$-factor found in Step 4 is two pentagons; the Petersen graph has no $2$-factor that is a single $10$-cycle.

**32.** *Strategy: induction on $n$; insert the new vertex into the Hamiltonian path of the smaller tournament.*

Let $T$ be a tournament on $n$ vertices. We prove by induction on $n$ that $T$ has a directed Hamiltonian path.

*Base.* $n = 1$: a single vertex is a Hamiltonian path.

*Step.* Let $v$ be any vertex and let $T' = T - v$, a tournament on $n-1$ vertices. By induction $T'$ has a Hamiltonian path
$$v_1 \to v_2 \to \cdots \to v_{n-1} .$$
Because $T$ is a tournament, for each $i$ exactly one of $v_i \to v$ and $v \to v_i$ holds.

* If $v \to v_1$, then $v \to v_1 \to v_2 \to \cdots \to v_{n-1}$ is a Hamiltonian path.
* If $v_{n-1} \to v$, then $v_1 \to \cdots \to v_{n-1} \to v$ is a Hamiltonian path.
* Otherwise $v_1 \to v$ and $v \to v_{n-1}$. Let $i$ be the largest index with $v_i \to v$; then $1 \le i \le n-2$ and, by maximality, $v \to v_{i+1}$. Hence
$$v_1 \to \cdots \to v_i \to v \to v_{i+1} \to \cdots \to v_{n-1}$$
is a Hamiltonian path: the new edges are $v_i \to v$ and $v \to v_{i+1}$ ✓.

In every case $T$ has a Hamiltonian path ✓. $\blacksquare$

*Remark.* The tournament need not be strongly connected and need not have a Hamiltonian cycle; the path conclusion is the best possible in general. A tournament has a Hamiltonian cycle exactly when it is strongly connected (Camion's theorem), a result not needed here.

**33.** *Strategy: an Eulerian circuit gives a cyclic ordering of the edges in which consecutive edges are adjacent; the star shows that not every Hamiltonian cycle of $L(G)$ arises this way.*

*Forward direction.* Let $G$ be connected and Eulerian with $m \ge 3$, and let
$$C = v_0e_1v_1e_2\cdots e_mv_0$$
be an Eulerian circuit. The vertices of $L(G)$ are the edges of $G$. The edges $e_1,\dots,e_m$ are pairwise distinct (an Eulerian circuit uses each edge once) and they are all the edges, so they are all the vertices of $L(G)$. Consecutive edges $e_i, e_{i+1}$ share the vertex $v_i$ (indices modulo $m$), so $e_ie_{i+1}$ is an edge of $L(G)$; therefore
$$e_1e_2\cdots e_m e_1$$
is a cycle in $L(G)$ through all $m \ge 3$ vertices: a Hamiltonian cycle ✓.

*Failure of the converse.* Let $G = K_{1,3}$ be the star with centre $c$ and leaves $x_1,x_2,x_3$. Its three edges $e_i = cx_i$ are pairwise adjacent (they all share $c$), so $L(G)$ is the triangle $e_1e_2e_3e_1$, which is Hamiltonian. But $G$ has degree sequence $(3,1,1,1)$, so it is not Eulerian ✓. Hence the converse fails.

*Why.* A Hamiltonian cycle of $L(G)$ is only a cyclic ordering of the edges in which consecutive edges share *some* vertex; an Eulerian circuit requires the shared vertices to match up consistently, so that the edges can actually be traversed one after another. In $K_{1,3}$ the ordering $e_1,e_2,e_3$ shares the centre each time, but walking $e_1$ and then $e_2$ would require returning to $c$ without an edge. $\blacksquare$

**34.** *Strategy: pair up the odd vertices with dummy edges, apply the Eulerian circuit theorem, then delete the dummy edges; the lower bound is a parity count over trails.*

**Upper bound: a partition into $k$ trails.** Let $O = \{o_1,\dots,o_{2k}\}$ be the set of odd-degree vertices. Add $k$ new edges $o_{2i-1}o_{2i}$ (as parallel edges if necessary, working in a multigraph) and call the result $G^{+}$. Every vertex of $G^{+}$ has even degree, and $G^{+}$ is connected because $G$ is; by Theorem 7.2.3, $G^{+}$ has an Eulerian circuit $C^{+}$.

Delete the $k$ new edges from the cyclic sequence $C^{+}$. This cuts the circuit into exactly $k$ linear trails (fewer only if two deleted edges are consecutive, in which case one of the pieces is empty and can be discarded), whose edge sets are disjoint and together form $E(G)$. Each piece is a trail of $G$, since it uses no new edge. So $E(G)$ is partitioned into at most $k$ trails.

**Lower bound: at least $k$ trails.** Let $E(G) = E_1 \sqcup \cdots \sqcup E_r$ be a partition into trails $T_1,\dots,T_r$. Fix a vertex $x$. For each trail $T_i$, the number of edges of $T_i$ at $x$ has the parity computed in the lemma of Solution 14: it is even unless $x$ is an endpoint of $T_i$, in which case it is odd. Since the $E_i$ partition the edges,
$$\deg_G(x) = \sum_{i=1}^{r} \deg_{T_i}(x),$$
so $\deg_G(x)$ is odd exactly when $x$ is an endpoint of an odd number of the trails, in particular of at least one. Each trail has at most two endpoints, so the total number of odd vertices, $2k$, is at most $2r$, giving $r \ge k$.

Combining the two bounds, the minimum number of trails in such a partition is exactly $k$ ✓. $\blacksquare$

**35.** *Strategy: a Hamiltonian cycle in a bipartite graph contains a perfect matching obtained by taking alternate edges.*

(a) Let $G$ be bipartite with parts $X,Y$ and let $C$ be a Hamiltonian cycle. Since $G$ is bipartite, $C$ alternates between $X$ and $Y$; since $C$ contains every vertex, $\lvert X\rvert = \lvert Y\rvert = n/2$. Choose one of the two perfect matchings of the cycle,
$$M = \{v_{2i}v_{2i+1} : i = 0,\dots,n/2-1\}$$
(reading $C$ cyclically with $v_0 \in X$). Then $M$ matches every vertex of $X$ with a distinct vertex of $Y$, and vice versa.

Now let $S \subseteq X$. Every $x \in S$ is matched by $M$ to a neighbour $m(x) \in Y$, and $m$ is injective on $X$, so $m(S) \subseteq N(S)$ has $\lvert S\rvert$ elements. Hence
$$\lvert N(S)\rvert \ge \lvert m(S)\rvert = \lvert S\rvert . \qquad \blacksquare$$

(b) If some $S \subseteq X$ has $\lvert N(S)\rvert < \lvert S\rvert$, then by (a) no Hamiltonian cycle exists. For the Herschel graph, take $S = X$, the part of size $6$. The graph is connected and bipartite, so every vertex of $Y$ has a neighbour in $X$ (otherwise it would be isolated from the rest), that is, $N(X) = Y$, and
$$\lvert N(X)\rvert = 5 < 6 = \lvert X\rvert .$$
So the Herschel graph is not Hamiltonian ✓ — the same conclusion as in Solution 18(b), now from Hall's condition rather than from the part sizes.

*Remark.* The condition $\lvert N(S)\rvert \ge \lvert S\rvert$ for all $S \subseteq X$ is exactly Hall's condition for the existence of a matching saturating $X$; a Hamiltonian cycle is a much stronger object than a perfect matching, so the condition is necessary and far from sufficient.

**36.** *Strategy: degrees add over blocks; the (⇒) direction needs a leaf block of the block-cut tree and an induction.*

Recall that the blocks of a connected graph partition its edges (Proposition 7.16.2), so for every vertex $v$,
$$\deg_G(v) = \sum_{B \ni v} \deg_B(v),$$
the sum being over the blocks containing $v$.

*If every block is Eulerian*, each $\deg_B(v)$ is even, so $\deg_G(v)$ is even for every $v$; since $G$ is connected and has at least one edge, Theorem 7.2.3 makes $G$ Eulerian ✓.

*Conversely, suppose $G$ is Eulerian*, and induct on the number of blocks. If $G$ has one block, then $G$ itself is that block and it is Eulerian. Otherwise, the block-cut tree of $G$ has at least two block-nodes, so it has a leaf block $B$ (a leaf of a tree is a block-node, because leaves of $\operatorname{BC}(G)$ are never cut vertices — a cut vertex has degree at least $2$ in the block-cut tree). Let $v$ be the unique cut vertex of $G$ lying in $B$.

Every vertex $u \in V(B)$ with $u \ne v$ lies in no other block, so $\deg_B(u) = \deg_G(u)$, which is even. Summing degrees inside $B$,
$$2\lvert E(B)\rvert = \sum_{u \in V(B)} \deg_B(u) \equiv \deg_B(v) \pmod 2,$$
so $\deg_B(v)$ is even as well. Hence every degree of $B$ is even, and $B$ (connected by definition) is Eulerian.

Now remove the edges of $B$ and the vertices of $B \setminus \{v\}$ from $G$, obtaining $G'$. The graph $G'$ is connected (or empty): $B$ was a leaf of the block-cut tree, so every path from a vertex of $B \setminus \{v\}$ to the rest of $G$ passed through $v$; and every remaining vertex is still joined to $v$ through the other blocks. Its degrees are even: the only vertex whose incident edges changed is $v$, which lost the even number $\deg_B(v)$. The blocks of $G'$ are exactly the blocks of $G$ other than $B$. By induction every block of $G'$ is Eulerian, and $B$ is Eulerian, so every block of $G$ is Eulerian ✓. $\blacksquare$

*Corollary.* A connected graph with an Eulerian block decomposition has no bridge block: $K_2$ is a block with odd degrees, so an Eulerian graph cannot contain one, which recovers Proposition 7.3.3.

