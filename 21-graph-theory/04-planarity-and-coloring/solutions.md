# Planarity and Colouring — Solutions

> [Planarity and Colouring](README.md) · Solutions to the 36 problems in [exercises.md](exercises.md)

Each solution states the strategy, then carries out every significant step. Proof problems receive complete proofs; numerical claims are checked against Euler's formula, the face handshake, or the recurrence they illustrate. Where a second argument exists it is described at the end.

## Beginner

**1.** *Strategy: count vertices and edges from the graph, faces from the drawing, and check both identities.*

(a) Cube: $n = 8$, $m = 12$, $f = 6$. Then $8 - 12 + 6 = 2$ ✓. Each face is a square, so the face lengths sum to $6\cdot4 = 24 = 2m$ ✓.

(b) Octahedron: $n = 6$ and each vertex has degree $4$, so $m = 6\cdot4/2 = 12$; drawn with triangular faces, $f = 8$. Then $6 - 12 + 8 = 2$ ✓, and $8\cdot3 = 24 = 2m$ ✓.

(c) $K_4$: $n = 4$, $m = 6$; drawn as a tetrahedron it has $4$ triangular faces. Then $4 - 6 + 4 = 2$ ✓ and $4\cdot3 = 12 = 2m$ ✓.

*Common pitfall.* In each case the outer face must be counted. The cube has five visible squares plus the "back" one; the tetrahedron has three visible triangles plus the base. Forgetting the outer face gives $f = 5$, $7$, $3$ respectively and Euler's formula fails by one.

**2.** *Strategy: exhibit a drawing where possible; when impossible, use $m \le 3n-6$ or the bipartite bound $m \le 2n-4$.*

(a) $K_4$: **planar** — draw a triangle and put the fourth vertex inside it, joined to the three corners ✓.

(b) $K_{2,4}$: **planar** — draw the two vertices of the small part as two points $x,y$, and the four vertices of the large part as four disjoint arcs, two going above $x$–$y$ and two below, each joining $x$ to $y$ through an intermediate vertex. All edges meet only at $x$ and $y$ ✓.

(c) $K_{3,3}$: **not planar**. It is bipartite with $n = 6$, $m = 9$, but the bipartite bound requires $m \le 2\cdot6 - 4 = 8$ (Solution 15) ✓.

(d) $Q_3$: **planar** — draw it as a cube ✓.

(e) $K_5$: **not planar** — $n = 5$, $m = 10$, and $3n - 6 = 9 < 10$ ✓.

(f) $W_5$: **planar** — draw a pentagon and put the hub inside it, joined to all five corners ✓. Here $n = 6$, $m = 10 \le 12 = 3n - 6$, consistent with planarity; the counting bound does not prove it, the drawing does.

**3.** *Strategy: a $4$-regular graph has $m = 2n$; impose the planar bound.*

(a) A $4$-regular graph satisfies $2m = 4n$, so $m = 2n$. If it is simple and planar with $n \ge 3$ then $m \le 3n - 6$, hence
$$2n \le 3n - 6, \qquad \text{so } n \ge 6 .$$
(b) The octahedron is $4$-regular with $n = 6$ and $m = 12$, and $12 = 3\cdot6-6$: the bound is attained, so it is maximal planar ✓.

(c) $K_5$ is $4$-regular with $n = 5$, and (a) forbids a $4$-regular planar graph on five vertices. The edge bound gives the same verdict by a different route: $m = 10 > 9 = 3n-6$ ✓. Both arguments use the same inequality, but (a) organises it as a constraint on $n$ and (c) as a constraint on $m$; when the degree is fixed, the first form is often the more useful.

**4.** *Strategy: apply the triangle-free bound and check whether it is decisive.*

(a) If $G$ is simple, planar, triangle-free and $n \ge 3$, then $m \le 2n - 4$ (Theorem 7.4.1). For $K_{3,3}$: $n = 6$, $m = 9$, and $2n - 4 = 8 < 9$, so $K_{3,3}$ is **not planar**.

(b) $K_{2,4}$ has $n = 6$ and $m = 8$, and $2\cdot6-4 = 8$: equality holds ✓. This is consistent with the drawing of Solution 2(b), in which every face is a quadrilateral: then $2m = 4f$ and Euler give $f = 4$, $m = 8$ ✓.

(c) $K_{3,3}$ minus an edge has $n = 6$, $m = 8 = 2n-4$, so the bound is satisfied and says nothing. The graph is in fact **planar**: label the parts $a_1,a_2,a_3$ and $b_1,b_2,b_3$ and delete $a_3b_3$; draw the $4$-cycle $a_1b_1a_2b_2a_1$, place $a_3$ inside it joined to $b_1$ and $b_2$, and place $b_3$ outside joined to $a_1$ and $a_2$. All eight edges are drawn with no crossings ✓. So the bound is necessary but not sufficient: equality in it permits both planar and non-planar graphs (compare $K_{3,3}$, which violates it).

**5.** *Strategy: $\omega$ from the largest clique, $\alpha$ from the largest independent set, $\chi$ from a colouring plus a lower bound.*

| Graph | $\chi$ | $\omega$ | $\alpha$ | Reason |
|---|---|---|---|---|
| $K_4$ | $4$ | $4$ | $1$ | all vertices mutually adjacent |
| $C_5$ | $3$ | $2$ | $2$ | odd cycle: $\chi = 3$ (Proposition 7.8.2(c)); largest independent set is two non-adjacent vertices |
| $K_{2,3}$ | $2$ | $2$ | $3$ | bipartite with edges; the part of size $3$ is independent and maximal |
| Petersen | $3$ | $2$ | $4$ | triangle-free so $\omega = 2$; not bipartite so $\chi \ge 3$; a $3$-colouring is exhibited in Example 9.3(c) |
| $P_4$ | $2$ | $2$ | $2$ | bipartite with an edge; the two ends form a maximum independent set |

*Checks.* Each clique sits inside an independent set's complement; for $C_5$, $n = 5 = \alpha + \omega$ ✓; for the Petersen graph, $n = 10 = 4 + 6$ and $\chi \ge \lceil 10/4\rceil = 3$ ✓, consistent with $\chi = 3$.

**6.** *Strategy: run the algorithm literally, recording the forbidden colours at each step.*

*Order $4,5,6,1,2,3$:*

| Step | Vertex | Coloured neighbours | Forbidden | Colour |
|---|---|---|---|---|
| 1 | $4$ | none | none | $1$ |
| 2 | $5$ | none | none | $1$ |
| 3 | $6$ | none | none | $1$ |
| 4 | $1$ | $4$ ($1$) | $\{1\}$ | $2$ |
| 5 | $2$ | $1$ ($2$), $5$ ($1$) | $\{1,2\}$ | $3$ |
| 6 | $3$ | $1$ ($2$), $2$ ($3$), $6$ ($1$) | $\{1,2,3\}$ | $4$ |

Four colours.

*Order $1,2,3,4,5,6$:* $1\mapsto1$; $2\mapsto2$ (adjacent to $1$); $3\mapsto3$ (adjacent to $1,2$); $4\mapsto2$ (only neighbour $1$ has colour $1$); $5\mapsto1$ (only neighbour $2$ has colour $2$); $6\mapsto1$ (only neighbour $3$ has colour $3$). Three colours.

*The chromatic number.* The triangle $1$–$2$–$3$ forces $\chi \ge 3$, and the second order produces a proper $3$-colouring, so $\chi = 3$ ✓. The first order uses four colours because vertices $1,2,3$ are coloured last, each seeing two or three of the colours already used on its neighbours — the greedy algorithm cannot recover.

**7.** *Strategy: colour sequentially, choosing an order that makes the count a product, and check small values.*

(a) $K_3$: three mutually adjacent vertices, so the first has $k$ choices, the second $k-1$, the third $k-2$:
$$P_{K_3}(k) = k(k-1)(k-2).$$
(b) $P_3$ with vertices $1$–$2$–$3$: $1$ has $k$ choices, $2$ has $k-1$, $3$ has $k-1$ (only $2$ is adjacent):
$$P_{P_3}(k) = k(k-1)^2 .$$
(c) $C_4$ with vertices $1$–$2$–$3$–$4$–$1$: colour $1$ ($k$ ways), $2$ ($k-1$), $3$ ($k-1$). For $4$ there are two cases: if $3$ has the same colour as $1$ (exactly $1$ way) then $4$ may use any of the remaining $k-1$ colours; otherwise ($k-2$ ways) $4$ must avoid both colours and has $k-2$ choices. Hence
$$P_{C_4}(k) = k(k-1)\bigl[1\cdot(k-1) + (k-2)(k-2)\bigr] = k(k-1)(k^2 - 3k + 3).$$
(d) $K_{1,3}$: the centre has $k$ choices and each of the three leaves independently has $k-1$, so $P = k(k-1)^3$ ✓.

*Checks.* (a) at $k=2$: $0$ ✓. (b) at $k=2$: $2$ ✓ (two colourings of a path). (c) at $k=2$: $2\cdot1\cdot(4-6+3) = 2$ ✓. (d) at $k=1$: $0$ ✓.

**8.** *Strategy: substitute into $(k-1)^5 + (-1)^5(k-1) = (k-1)^5 - (k-1)$.*

$$P_{C_5}(2) = 1^5 - 1 = 0, \qquad P_{C_5}(3) = 2^5 - 2 = 30, \qquad P_{C_5}(4) = 3^5 - 3 = 240 .$$

$P(2) = 0$ says no proper $2$-colouring exists, so $\chi(C_5) > 2$. $P(3) = 30 > 0$ says $3$-colourings exist. Hence $\chi(C_5) = 3$ ✓. The value $30$ is consistent with a direct count: fix the colour of the first vertex ($3$ ways) and count the extensions of the $5$-cycle, which gives $10$ per choice of the first colour ✓. $P(4) = 240 = 4\cdot 60$ counts the $4$-colourings.

**9.** *Strategy: exhibit the colouring; for the lower bound find a forbidden subgraph or use a degree/edge-count argument.*

(a) Label the cube's vertices by binary strings of length $3$. Colour a vertex by the parity of the number of $1$s. Adjacent vertices differ in exactly one coordinate, hence have opposite parity, so this is a proper $2$-colouring ✓. One colour is impossible because the cube has edges (and $8 \ge 2$ vertices) ✓. Hence $\chi(Q_3) = 2$.

(b) $W_6$: give the hub colour $1$ and colour the rim $v_1,\dots,v_6$ alternately $2,3,2,3,2,3$; this is proper on the rim (consecutive vertices differ) and every rim vertex differs from the hub ✓. Two colours are impossible because the hub together with any rim edge forms a triangle, and a triangle needs three colours ✓. Hence $\chi(W_6) = 3$.

**10.** *Strategy: identify each face and walk round its boundary.*

Vertices $1,\dots,5$; edges $12, 23, 31$ (triangle on $1,2,3$) and $34, 45, 51$ (giving the quadrilateral $1$–$3$–$4$–$5$).

* Faces: the triangle $1$–$2$–$3$, of length $3$; the quadrilateral $1$–$3$–$4$–$5$, of length $4$; the outer face, whose boundary walk is $1$–$2$–$3$–$4$–$5$–$1$, of length $5$.
* Face handshake: $3 + 4 + 5 = 12 = 2\cdot6 = 2m$ ✓.
* Euler: $n - m + f = 5 - 6 + 3 = 2$ ✓.

The chord $13$ borders the triangle and the quadrilateral; the edges $12, 23$ border the triangle and the outer face; the edges $34, 45, 51$ border the quadrilateral and the outer face. This information is exactly what the dual records (compare Example 7.7.6).

**11.** *Strategy: dual vertices are faces of the cube; the degree of a dual vertex equals the length of the corresponding face.*

The cube has $f = 6$ faces, so $n^{*} = 6$; it has $m = 12$ edges, so $m^{*} = 12$; and $f^{*} = n = 8$.

Every face of the cube is a square, so every vertex of $Q_3^{*}$ has degree $4$: the dual is $4$-regular. A $4$-regular simple graph on $6$ vertices with $12$ edges is the octahedron (the only $4$-regular graph on six vertices up to isomorphism: the complement of a perfect matching). Hence
$$Q_3^{*} \cong \text{octahedron}, \qquad \text{and dually the octahedron}^{*} \cong Q_3 .$$
Check Euler for the dual: $6 - 12 + 8 = 2$ ✓.

*Sanity check.* The octahedron has $8$ faces and the cube has $8$ vertices, matching $f^{*} = n$ ✓; the cube has $6$ faces and the octahedron $6$ vertices, matching $n^{*} = f$ ✓. The cube and the octahedron are dual polyhedra, which is the geometric content of the computation.

**12.** *Strategy: find a clique for the lower bound and a colouring for the upper bound.*

The vertices $1,2,3$ form a triangle (edges $12, 23, 13$), so $\chi \ge 3$.

A proper $3$-colouring: $c(1) = 1$, $c(2) = 2$, $c(3) = 3$, $c(4) = 1$, $c(5) = 2$, $c(6) = 3$. Check every edge:

| Edge | Colours | Proper? |
|---|---|---|
| $12$ | $1,2$ | ✓ |
| $23$ | $2,3$ | ✓ |
| $34$ | $3,1$ | ✓ |
| $45$ | $1,2$ | ✓ |
| $56$ | $2,3$ | ✓ |
| $61$ | $3,1$ | ✓ |
| $13$ | $1,3$ | ✓ |
| $46$ | $1,3$ | ✓ |

So $\chi = 3$ ✓. Note that $G$ is planar: its edges form the triangle $1$–$2$–$3$, the triangle $4$–$5$–$6$, and the two edges $34$ and $61$ joining them; drawing the triangles side by side and the two joining edges without crossing gives a plane embedding ✓.

## Intermediate

**13.** *Strategy: induction on the number of edges, using the two ways an edge can sit in a drawing.*

The proof uses two facts.

*Fact A (bridges).* If $e$ is a bridge of a connected plane graph, then deleting $e$ does not change the number of faces. The bridge lies inside one face, and its two sides are part of the boundary of that same face; deleting it neither merges two faces nor splits one.

*Fact B (cycle edges).* If $e$ lies on a cycle, then deleting $e$ merges exactly two faces into one, so $f(G - e) = f(G) - 1$. The cycle containing $e$ is a simple closed curve; its interior and exterior are distinct faces of $G - e$, and $e$ is the only connection across the curve at that place.

*Base.* If $m = 0$, then $G$ is a single vertex (connectivity), $f = 1$, and $n - m + f = 1 - 0 + 1 = 2$ ✓.

*Step.* Let $m \ge 1$.

*Case 1: $G$ is a tree.* Every edge is a bridge, so by Fact A deleting edges one at a time never changes $f$; starting from one vertex with one face, $f = 1$. Also $m = n - 1$. Hence $n - m + f = n - (n-1) + 1 = 2$ ✓.

*Case 2: $G$ is not a tree.* Then $G$ has a cycle; choose $e$ on a cycle. Since $e$ is not a bridge, $G - e$ is connected; it has $n$ vertices, $m - 1$ edges and, by Fact B, $f - 1$ faces. By induction,
$$n - (m-1) + (f-1) = 2, \qquad \text{i.e.} \qquad n - m + f = 2 . \qquad \blacksquare$$

*Where connectivity enters.* It is used twice: to conclude that $G - e$ is connected when $e$ is not a bridge (so that the induction hypothesis applies to a connected graph), and in the base case (a graph with no edges and several vertices has several faces and does not satisfy the formula). Without connectivity the correct statement is $n - m + f = 1 + c$ (Corollary 7.2.2).

**14.** *Strategy: bound each face length below by $3$, sum over faces, and substitute Euler.*

*Face length at least $3$.* A face of length $1$ would be bounded by a loop, and a face of length $2$ by two parallel edges; a simple graph has neither. A face of length $0$ does not occur. So every face has length $\ge 3$. Simplicity is used exactly here: with loops or parallel edges, faces of length $1$ or $2$ exist and the bound fails. The hypothesis $n \ge 3$ excludes $K_2$, whose single face has length $2$ (the two sides of the edge belong to the same face).

*The inequality.* Each edge has two sides, so summing face lengths counts each edge twice:
$$2m = \sum_{\varphi} \operatorname{len}(\varphi) \ge 3f .$$
*The edge bound.* Euler gives $f = 2 - n + m$. Substituting,
$$2m \ge 3(2 - n + m) = 6 - 3n + 3m,$$
so $m \le 3n - 6$ ✓.

*Counterexample at $n = 2$.* $K_2$ is planar with $n = 2$ and $m = 1$, while $3n - 6 = 0$. The bound fails because the single face has length $2$; the computation $2m \ge 3f$ reads $2 \ge 3$, which is false. This is why the hypothesis $n \ge 3$ cannot be dropped.

**15.** *Strategy: in a triangle-free graph, pay $4$ per face instead of $3$.*

Let $G$ be simple, planar, triangle-free and $n \ge 3$. Every face has length at least $4$: a face boundary is a closed walk, and a closed walk in a triangle-free graph cannot have length $3$; lengths $1$ and $2$ are excluded by simplicity as in Solution 14. Hence
$$2m = \sum_\varphi \operatorname{len}(\varphi) \ge 4f .$$
With $f = 2 - n + m$,
$$2m \ge 4(2 - n + m) = 8 - 4n + 4m \quad\Longrightarrow\quad 2m \le 4n - 8 \quad\Longrightarrow\quad m \le 2n - 4 . \qquad \blacksquare$$

*$K_{3,3}$.* It is bipartite, hence triangle-free, with $n = 6$ and $m = 9 > 8 = 2\cdot 6 - 4$. So $K_{3,3}$ is not planar ✓.

*Sharpness.* $K_{2,n}$ has $n + 2$ vertices and $2n$ edges, and $2(n+2) - 4 = 2n$ ✓. It is planar by the drawing of Solution 2(b), in which all $n$ bounded faces are quadrilaterals; equality in $4f \le 2m$ holds because every face is a quadrilateral ✓.

**16.** *Strategy: average degree arguments, using the two edge bounds.*

*Planar case.* Let $G$ be simple and planar with $n \ge 3$. By the handshake lemma and Theorem 7.3.2,
$$2m \le 6n - 12 \quad\Longrightarrow\quad \frac{2m}{n} \le 6 - \frac{12}{n} < 6 .$$
If every vertex had degree at least $6$, the average would be at least $6$; so some vertex has degree at most $5$ ✓.

*Bipartite planar case.* If in addition $G$ is bipartite, Theorem 7.4.1 gives $2m \le 4n - 8$, so the average degree is at most $4 - 8/n < 4$, and some vertex has degree at most $3$ ✓.

*Why the second does not follow from the first.* The first argument gives $\delta \le 5$ for all planar graphs; it says nothing about bipartite ones beyond that. The sharper conclusion needs the sharper edge bound, which in turn needs the absence of triangles. Indeed the icosahedron is planar, $5$-regular, and has minimum degree $5$; it is not bipartite. So a bound of $3$ genuinely requires the bipartite hypothesis.

**17.** *Strategy: cycle of implications (a) $\Rightarrow$ (b) $\Rightarrow$ (c) $\Rightarrow$ (a).*

(a) $\Rightarrow$ (b): Suppose $G$ is maximal planar and embed it in the plane. By Proposition 7.3.1 every face has length at least $3$. If some face $\varphi$ had length at least $4$, two non-adjacent vertices $x,y$ on its boundary could be joined by an arc drawn inside $\varphi$ (a diagonal of the face), producing a planar supergraph: this contradicts maximality. So every face has length exactly $3$.

(b) $\Rightarrow$ (c): If every face is a triangle then $2m = 3f$. Euler gives $f = 2 - n + m$, so
$$2m = 3(2 - n + m) = 6 - 3n + 3m, \qquad \text{hence } m = 3n - 6 .$$
(c) $\Rightarrow$ (a): Suppose $m = 3n - 6$. Then $f = 2 - n + m = 2n - 4$ and $3f = 6n - 12 = 2m$. Since every face has length at least $3$,
$$2m = \sum_\varphi \operatorname{len}(\varphi) \ge 3f = 2m,$$
so equality holds throughout and every face has length exactly $3$. No edge can be added: a new edge between two existing vertices would have to be drawn inside a face, and every face is a triangle, whose boundary already uses all three pairs of vertices; drawing it outside a face is impossible because the plane minus the drawing is exactly the union of the faces. So $G$ is maximal planar ✓. $\blacksquare$

*Note.* The equivalence uses "some embedding" in (b) and "every embedding" is then automatic: if one embedding has all faces triangular, then (c) holds, and the argument for (c) $\Rightarrow$ (a) shows that *every* embedding of a graph with $m = 3n-6$ has triangular faces, since the face-length sum is embedding-independent in its total but the equality forces each face to be a triangle in whatever embedding is chosen.

**18.** *Strategy: read the definitions and apply Euler twice.*

Let $G$ be connected and plane, with face set $\Phi$.

*Vertices.* $G^{*}$ has one vertex per face of $G$, so $n^{*} = \lvert\Phi\rvert = f$ ✓.

*Edges.* Each edge $e$ of $G$ gives exactly one edge $e^{*}$ of $G^{*}$, and distinct edges give distinct dual edges (they cross different edges), so $m^{*} = m$ ✓. (If $e$ is a bridge, $e^{*}$ is a loop, still one edge.)

*Faces.* Each face of $G^{*}$ contains exactly one vertex of $G$: the arcs of $G^{*}$ cross edges of $G$ and hence never pass through a vertex of $G$, and the vertices of $G$ lie in distinct faces of $G^{*}$ because the closed curves formed by $G^{*}$ around each vertex separate them. The correspondence is bijective, so $f^{*} = n$ ✓.

*Connectivity.* Given two vertices $x,y$ of $G^{*}$ (faces of $G$), choose points in those faces and a curve in the plane joining them that avoids the vertices of $G$ and crosses edges transversally. Each crossing of an edge $e$ corresponds to moving along $e^{*}$ in $G^{*}$, so the curve gives a walk in $G^{*}$ from $x$ to $y$ ✓.

*Double dual.* A face of $G^{*}$ contains exactly one vertex $v$ of $G$, so the vertices of $G^{**}$ are in bijection with $V(G)$; the edge $e^{**}$ crosses $e^{*}$, which crosses $e$, so edges correspond. Incidence and embedding are preserved, so $G^{**} \cong G$ as plane graphs ✓. (For disconnected $G$ the statement fails; see Common Mistake 9.)

*Consistency check.* Euler for $G$: $n - m + f = 2$. Euler for $G^{*}$: $n^{*} - m^{*} + f^{*} = f - m + n = 2$ ✓, the same identity.

**19.** *Strategy: translate "both sides in the same face" into "loop".*

*If $e$ is a bridge*, then deleting $e$ disconnects $G$, so $e$ separates no two regions: its two sides lie in the same face. The dual edge $e^{*}$ joins the vertex of that face to itself, so $e^{*}$ is a loop.

*Conversely, if $e^{*}$ is a loop*, its two sides lie in the same face of $G$; then $e$ separates no two faces, so deleting $e$ does not disconnect $G$, that is, $e$ is a bridge ✓.

*Tree criterion.* If $G$ is a tree with $n \ge 2$, every edge is a bridge, so every dual edge is a loop, and there is exactly one face ($f = 1$): the dual has one vertex and $n-1$ loops. Conversely, if $G^{*}$ has exactly one vertex, then $f = 1$, so Euler gives $m = n - 1$; since $G$ is connected, $G$ is a tree ✓.

*Dual statement.* Dually, $G$ has no bridge if and only if $G^{*}$ has no loop, which is the same statement read backwards: $e$ is a bridge exactly when $e^{*}$ is a loop ✓.

**20.** *Strategy: split the colourings of $G - e$ according to whether the endpoints of $e$ agree.*

Let $e = uv$. Every proper $k$-colouring of $G - e$ either has $c(u) \ne c(v)$ or $c(u) = c(v)$.

*Different colours.* If $c(u) \ne c(v)$, then $c$ is also a proper colouring of $G$, since the only constraint missing in $G - e$ is the one on $e$, and $c$ satisfies it. Conversely every colouring of $G$ is a colouring of $G - e$ with $c(u)\ne c(v)$ ✓.

*Same colour.* If $c(u) = c(v)$, identify $u$ and $v$ in $G - e$ to form $G/e$; the colouring descends to a proper colouring of $G/e$, because every edge of $G/e$ corresponds to an edge of $G - e$ incident with $u$ or $v$, and its endpoints keep distinct colours. Conversely, every proper colouring of $G/e$ pulls back to a colouring of $G - e$ with $u,v$ of the same colour ✓.

*Count.* Hence
$$P_{G-e}(k) = P_G(k) + P_{G/e}(k), \qquad \text{that is,} \qquad P_G(k) = P_{G-e}(k) - P_{G/e}(k). \qquad \blacksquare$$

*Parallel edges.* Contracting $e$ may identify two neighbours of $u$ or $v$ and create parallel edges. Parallel edges impose the same constraint as a single edge (a proper colouring only requires the two endpoints to differ, and a second edge between the same pair adds nothing), so the number of colourings is unaffected; one may suppress them, but the recurrence remains valid even if they are kept. Loops created by contraction are discarded, since a loop would make the colouring impossible — this happens only when $e$ is a loop, which we exclude.

*Check.* For a triangle with edge $e$: $P_{K_3} = P_{P_3} - P_{K_2} = k(k-1)^2 - k(k-1) = k(k-1)(k-2)$ ✓.

**21.** *Strategy: colour a tree from a root; for the cycle, use the recurrence and induction.*

*Trees.* Root the tree at any vertex $r$ and colour the vertices in order of increasing distance from $r$. The root has $k$ choices. Every other vertex has exactly one neighbour closer to the root (its parent) and all its other neighbours are farther away and still uncoloured, so it has exactly $k - 1$ choices. The choices are independent, so
$$P_T(k) = k(k-1)^{n-1} . \qquad \blacksquare$$

*Cycles.* Induction on $n \ge 3$. For $n = 3$: $C_3 = K_3$, and the formula gives $(k-1)^3 - (k-1) = (k-1)\bigl[(k-1)^2-1\bigr] = (k-1)(k^2-2k) = k(k-1)(k-2)$ ✓, which is $P_{K_3}$.

For $n \ge 4$, delete an edge $e$ of $C_n$. Then $C_n - e = P_n$, a tree, so $P_{C_n-e} = k(k-1)^{n-1}$; and $C_n/e \cong C_{n-1}$ (contracting an edge of a cycle gives a shorter cycle). The recurrence gives
$$P_{C_n} = k(k-1)^{n-1} - P_{C_{n-1}} .$$
Assume the formula for $n-1$: $P_{C_{n-1}} = (k-1)^{n-1} + (-1)^{n-1}(k-1)$. Then
$$P_{C_n} = k(k-1)^{n-1} - (k-1)^{n-1} - (-1)^{n-1}(k-1) = (k-1)^n + (-1)^n(k-1),$$
since $-(-1)^{n-1} = (-1)^n$ ✓. $\blacksquare$

*Checks.* $n = 3$: $k(k-1)(k-2)$ ✓ (computed above). $n = 4$: $(k-1)^4 + (k-1)$, and at $k = 2$ this is $1 + 1 = 2$ ✓ (the two alternating colourings), at $k = 3$ it is $16 + 2 = 18$ ✓. $n = 5$ at $k = 3$: $2^5 - 2 = 30$ ✓ (Solution 8).

**22.** *Strategy: count forbidden colours at the moment of colouring; count independent sets for the lower bound.*

*Greedy bound.* Order the vertices arbitrarily and colour them in that order, giving each vertex the smallest colour not already used by a coloured neighbour. When $v$ is coloured, at most $\deg(v) \le \Delta(G)$ neighbours are coloured, so at most $\Delta(G)$ colours are forbidden and one of the colours $1,\dots,\Delta(G)+1$ is available. Hence a proper $(\Delta+1)$-colouring exists and $\chi(G) \le \Delta(G)+1$ ✓.

*Independence bound.* In a proper colouring with $k$ colours, each colour class is an independent set, hence has at most $\alpha(G)$ vertices. The $k$ classes cover all $n$ vertices, so $n \le k\,\alpha(G)$ and $k \ge n/\alpha(G)$. Since $k$ is an integer, $k \ge \lceil n/\alpha(G)\rceil$ ✓.

*Application to $C_5$.* $\alpha(C_5) = 2$ (any three vertices of a $5$-cycle contain two that are adjacent), so $\chi(C_5) \ge \lceil 5/2\rceil = 3$ ✓, matching the explicit value.

*Comparison of the two bounds.* The greedy bound is additive and depends on the maximum degree; the independence bound is multiplicative and depends on global structure. Neither dominates the other: for $K_n$ both give $n$; for $C_5$ the greedy bound gives $3$ and the independence bound $3$; for the Petersen graph the greedy bound gives $4$ and the independence bound $3$.

## Advanced

**23.** *Strategy: induction on $n$, a vertex of degree at most $5$, and Kempe swaps.*

**Claim.** Every planar graph is $5$-colourable.

*Proof.* Induct on $n$. For $n \le 5$ give every vertex a different colour. For $n \ge 6$, by Corollary 7.3.4 there is a vertex $v$ with $\deg(v) \le 5$. By induction, $G - v$ has a proper colouring $c$ with colours $\{1,\dots,5\}$.

If $\deg(v) \le 4$, or if $\deg(v) = 5$ but some colour is missing from $N(v)$, then a free colour exists and $c$ extends to $v$. So assume $\deg(v) = 5$ and the five neighbours $v_1,\dots,v_5$ of $v$ receive the colours $1,2,3,4,5$ respectively. Label them in the cyclic order in which the edges $vv_i$ appear around $v$ in the embedding.

*The $1$–$3$ subgraph.* Let $H_{13}$ be the subgraph of $G - v$ induced by the vertices of colours $1$ and $3$.

*Case 1.* If $v_1$ and $v_3$ lie in different components of $H_{13}$, swap the colours $1$ and $3$ on the component containing $v_1$. This preserves properness: every edge with one endpoint in that component and the other outside joins a vertex of colour $1$ or $3$ to a vertex of colour $2,4$ or $5$, and the latter colours are untouched. After the swap, colour $1$ is not used on $N(v)$ — it is gone from $v_1$ and was not on $v_2,\dots,v_5$ — so $v$ takes colour $1$.

*Case 2.* If $v_1$ and $v_3$ lie in the same component of $H_{13}$, there is a path $P$ in $G - v$ from $v_1$ to $v_3$ whose vertices alternate in colours $1$ and $3$. The path $P$ together with the edges $vv_1$ and $vv_3$ is a cycle $C$ through $v$.

Because $G$ is drawn in the plane, $C$ is a simple closed curve, and by the Jordan curve theorem it separates the plane into an inside and an outside. The neighbours $v_2$ and $v_4$ lie on opposite sides of $C$: going around $v$, the edges $vv_1, vv_2, vv_3, vv_4, vv_5$ occur in that cyclic order, so $v_2$ lies in the sector between $v_1$ and $v_3$ and $v_4$ in the sector between $v_3$ and $v_5$; these sectors are on opposite sides of the closed curve formed by $P$ and the two edges through $v$ ✓.

Now let $H_{24}$ be the subgraph induced by the vertices of colours $2$ and $4$. If $v_2$ and $v_4$ lay in the same component of $H_{24}$, a path between them inside $G - v$ would have to cross the curve $C$; but it cannot pass through a vertex of $C$ (those have colours $1$ or $3$, while the path uses only colours $2$ and $4$) and it cannot cross an edge of $C$ (the drawing is plane). So $v_2$ and $v_4$ are in different components of $H_{24}$.

Swap the colours $2$ and $4$ on the component of $H_{24}$ containing $v_2$. As in Case 1 this preserves properness, and afterwards colour $2$ is not used on $N(v)$: it is gone from $v_2$ and was not on the other neighbours. So $v$ takes colour $2$.

Every case produces a proper $5$-colouring of $G$, completing the induction. $\blacksquare$

*Why not four colours.* With four colours and a vertex of degree $5$, the neighbourhood of $v$ is *larger* than the palette, so even if a colour could be freed on one chain, some other neighbour may use it. In the argument above the crucial step is that after the swap colour $1$ is missing from the whole neighbourhood; with five colours and five neighbours that works because each neighbour has a distinct colour and a swap removes exactly one colour from exactly one neighbour. With four colours this counting fails, and there are configurations of a degree-$5$ vertex in a planar graph in which every Kempe swap is blocked — precisely the configurations that the four-colour proof must analyse by computer.

**24.** *Strategy: the greedy induction with six colours, then locate the exact failure with five.*

*Six colours.* Induct on $n$. For $n \le 6$ use six distinct colours. For $n \ge 7$, Corollary 7.3.4 gives a vertex $v$ of degree at most $5$; by induction, $G - v$ has a proper $6$-colouring; at most five colours appear on $N(v)$, so one of the six colours is free and extends the colouring to $v$ ✓. $\blacksquare$

*Why five fails.* The same induction with a palette of five needs a free colour on $N(v)$. If $\deg(v) \le 4$ there is one. But if $\deg(v) = 5$ and the five neighbours carry five distinct colours, then all five colours are forbidden and the induction cannot proceed. The planar bound $\delta \le 5$ gives no control over the neighbours' colours.

*What the five-colour theorem adds.* Instead of asking for a free colour, it *manufactures* one by recolouring a Kempe chain: swap two colours on a connected component of the subgraph induced by those two colours. This removes a colour from the neighbourhood without disturbing the rest of the colouring. The six-colour argument needs no such device because it has one colour to spare; the five-colour argument needs it exactly once.

*Remark.* The four-colour theorem cannot be obtained by this induction at all: with four colours and a vertex of degree $5$, the neighbourhood exceeds the palette, and the analysis of the blocked Kempe configurations is the content of the computer-assisted proof.

**25.** *Strategy: (a) a clique forces distinct colours; (b) verify the Mycielski step.*

(a) Let $K$ be a clique of size $\omega = \omega(G)$. Any two vertices of $K$ are adjacent, so a proper colouring must assign them pairwise different colours; hence at least $\omega$ colours are needed and $\chi(G) \ge \omega(G)$ ✓. The inequality can be strict: $C_5$ has $\omega = 2$ (it has no triangle) but $\chi = 3$ (it is not bipartite), so $\chi - \omega = 1$.

(b) **Mycielski's construction.** Given $G$ with $V = \{v_1,\dots,v_n\}$, let $M(G)$ have vertex set $V \cup U \cup \{w\}$ with $U = \{u_1,\dots,u_n\}$, edges of $G$, edges $u_ix$ for every $x \in N_G(v_i)$, and edges $wu_i$ for every $i$. Then:

* $\chi(M(G)) \le \chi(G) + 1$: from a proper $k$-colouring $c$ of $G$, set $c(u_i) = c(v_i)$ and $c(w) = k+1$. For an edge $u_ix$ with $x \in N(v_i)$, $c(x) \ne c(v_i) = c(u_i)$ ✓; all other edges are edges of $G$ or meet $w$ ✓.
* $\chi(M(G)) \ge \chi(G) + 1$: let $c$ be a proper $t$-colouring of $M(G)$ with $c(w) = t$ (relabel so that $w$ has colour $t$). No $u_i$ has colour $t$ (each is adjacent to $w$). Define $c'(v_i) = c(v_i)$ if $c(v_i) \ne t$, and $c'(v_i) = c(u_i)$ otherwise. For an edge $v_iv_j$: at most one of the two has colour $t$ (they are adjacent); if $c(v_i) = t$ then $c'(v_i) = c(u_i)$, and $u_i$ is adjacent to $v_j$, so $c(u_i) \ne c(v_j) = c'(v_j)$ ✓. Hence $G$ is $(t-1)$-colourable, i.e. $\chi(G) \le \chi(M(G)) - 1$.
* Triangle-freeness: $U$ is independent; $w$'s neighbourhood is $U$, independent; so no triangle contains $w$ or two vertices of $U$. A triangle is therefore either three vertices of $V$ (a triangle of $G$) or $u_i$ with two adjacent neighbours $x,y$ of $v_i$ (giving the triangle $v_ixy$ of $G$). So $G$ triangle-free implies $M(G)$ triangle-free ✓.

Now start from $G_2 = K_2$, which has $\omega = \chi = 2$ and no triangle. Define $G_{k+1} = M(G_k)$; by induction each $G_k$ is triangle-free (so $\omega = 2$, since it has an edge) and $\chi(G_k) = k$ ✓. This proves the claim for every $k \ge 2$. The first interesting case is
$$M(C_5) = \text{the Grötzsch graph},$$
with $1 + 5 + 5 = 11$ vertices, $5 + 10 + 5 = 20$ edges, chromatic number $4$ and clique number $2$ ✓.

**26.** *Strategy: induction on $m$ with the recurrence, and the count at $k = 0$.*

Let $G$ have $n \ge 1$ and $m \ge 0$.

*Degree and leading coefficient.* Induct on $m$. For $m = 0$, $P_G(k) = k^n$ ✓. For $m \ge 1$, choose $e \in E$ and apply the recurrence:
$$P_G = P_{G-e} - P_{G/e}.$$
$G - e$ has $n$ vertices and $m-1$ edges, so by induction $P_{G-e}$ has degree $n$ and leading coefficient $1$. $G/e$ has $n-1$ vertices, so $P_{G/e}$ has degree $n-1$. The difference therefore has degree $n$ with leading coefficient $1$ ✓.

*Constant term.* $P_G(0)$ is the number of proper colourings with an empty palette, which is $0$ when $n \ge 1$ (there is no function from a non-empty set to an empty set). As the polynomial agrees with the count at every $k \ge 0$, its constant term is $P_G(0) = 0$ ✓.

*Coefficient of $k^{n-1}$.* Induct on $m$. For $m = 0$ the coefficient is $0 = -m$ ✓. For $m \ge 1$: $P_{G-e}$ has $n$ vertices and $m-1$ edges, so by induction the coefficient of $k^{n-1}$ in $P_{G-e}$ is $-(m-1)$. And $P_{G/e}$ has degree $n-1$ with leading coefficient $1$, so its contribution to the coefficient of $k^{n-1}$ in $P_G = P_{G-e} - P_{G/e}$ is $-1$. Total:
$$-(m-1) - 1 = -m . \qquad \blacksquare$$

*Consequence.* From the coefficient list of $P_G$ one reads off $n$ (the degree) and $m$ (minus the coefficient of $k^{n-1}$). Two graphs with different numbers of vertices or edges have different chromatic polynomials. (The converse fails: there are pairs of graphs with the same chromatic polynomial and different structure, so the polynomial is a strong but incomplete invariant.)

**27.** *Strategy: equality in $3f \le 2m$ forces every face to be a triangle.*

Let $G$ be simple, planar, $n \ge 3$, with $m = 3n - 6$. Then $f = 2 - n + m = 2n - 4$ and
$$3f = 6n - 12 = 2m .$$
On the other hand, every face has length at least $3$ (Proposition 7.3.1), so
$$2m = \sum_{\varphi}\operatorname{len}(\varphi) \ge 3f = 2m .$$
Hence equality holds in the sum: every face has length exactly $3$ ✓. This conclusion does not depend on which embedding is chosen — the face lengths in any embedding satisfy the same inequality, and the same forcing applies.

Now suppose an edge $g$ could be added to $G$ while keeping planarity. In a plane embedding of $G + g$, the edge $g$ is drawn as an arc joining two vertices and lying, except at its endpoints, inside a single face $\varphi$ of $G$. The endpoints of $g$ are two vertices on the boundary of $\varphi$, and $\varphi$ is a triangle, so its boundary is a cycle on three vertices: any two of its vertices are already joined by an edge of $G$. Adding $g$ would therefore create a parallel edge, contradicting simplicity, or coincide with an existing edge. So no edge can be added and $G$ is maximal planar ✓.

**28.** *Strategy: one direction is a parity count along a closed walk; the other is a greedy colouring by distance parity.*

*If $G$ is bipartite*, its vertices split into $X \cup Y$ with every edge joining $X$ to $Y$. Walking along a cycle the parts alternate, so the cycle has even length ✓.

*If $G$ has no odd cycle*, then in each connected component every closed walk has even length: a closed walk of odd length contains an odd cycle (delete repeated vertices; a closed walk decomposes into cycles, and an odd total length forces an odd summand — more directly, a shortest odd closed walk is a cycle, since any repetition inside it would split off a shorter odd closed walk). Hence no odd closed walk exists. Fix a vertex $r$ in a component and define $c(v) \in \{0,1\}$ to be the parity of the length of any path from $r$ to $v$. This is well defined: two paths of different parity would form an odd closed walk. For an edge $uv$, the path to $u$ followed by the edge $uv$ is a path to $v$, so $c(u) \ne c(v)$. Thus $c$ is a proper $2$-colouring and $G$ is bipartite ✓. $\blacksquare$

*Consequences.* $C_n$ is bipartite when $n$ is even (so $\chi = 2$) and not when $n$ is odd (so $\chi \ge 3$, and $3$ suffices by alternating two colours and giving one vertex the third, hence $\chi(C_n) = 3$) ✓. And $\chi(G) \le 2$ if and only if $G$ is bipartite: if $\chi \le 1$, there are no edges and the graph is bipartite; if $\chi = 2$, the two colour classes form a bipartition ✓.

**29.** *Strategy: (a) translate between colourings and evaluations; (b) find the smallest obstruction; (c) distinguish a restatement from a proof.*

(a) A proper $4$-colouring is by definition a colouring with colours from a set of size $4$, and $P_G(4)$ counts exactly those. So
$$P_G(4) > 0 \iff G \text{ is } 4\text{-colourable}.$$
The four-colour theorem is the assertion that this holds for every planar $G$, so the two statements are the same statement ✓.

(b) $K_4$ is planar and $P_{K_4}(k) = k(k-1)(k-2)(k-3)$, so $P_{K_4}(3) = 3\cdot2\cdot1\cdot0 = 0$ ✓. No planar graph with at most $3$ vertices has chromatic number $4$, since such a graph is a subgraph of $K_3$; so $K_4$ is the smallest planar graph with $\chi = 4$ ✓. Hence three colours do not suffice for planar graphs in general, and four cannot be improved to three.

(c) Part (a) is a *reformulation*, not a proof: it says that proving the four-colour theorem is the same as proving that $P_G(4) > 0$ for every planar $G$. The hard content — that no planar graph has $P_G(4) = 0$ — is untouched. A proof must show something about planar graphs, and the known proof does so by discharging and reducibility.

**30.** *Strategy: characterise spanning trees by "acyclic plus complement contains no cut", then dualise both conditions.*

**Lemma.** Let $G$ be connected. A set $T \subseteq E(G)$ is the edge set of a spanning tree if and only if (i) $T$ contains no cycle and (ii) $E \setminus T$ contains no cut of $G$.

*Proof.* If $T$ is a spanning tree, (i) is clear, and (ii) holds because every cut $\delta(S)$ with $\varnothing \ne S \subsetneq V$ must contain an edge of $T$ (the tree connects $S$ to $V\setminus S$), so no cut is contained in $E \setminus T$. Conversely, suppose (i) and (ii). If $T$ did not connect all vertices, take a component $S$ of $(V,T)$ with $\varnothing \ne S \subsetneq V$; then no edge of $T$ crosses $\delta(S)$, so $\delta(S) \subseteq E\setminus T$, contradicting (ii). So $T$ is connected and, by (i), acyclic: a spanning tree ✓. $\square$

Now apply the lemma to $G$ and to $G^{*}$. By Proposition 7.7.5, a set of edges is a cycle of $G$ if and only if its duals form a minimal cut of $G^{*}$, and a set of edges is a cut of $G$ if and only if its duals contain a cycle of $G^{*}$. Set
$$T' = \{e^{*} : e \in E(G) \setminus T\}, \qquad \text{so that } T^{*} = E(G^{*}) \setminus T' .$$

*Condition (i) for $T$ in $G$.* $T$ contains no cycle of $G$ $\iff$ $T^{*}$ contains no minimal cut of $G^{*}$ $\iff$ $E(G^{*}) \setminus T'$ contains no cut of $G^{*}$, which is condition (ii) for the set $T'$ in $G^{*}$.

*Condition (ii) for $T$ in $G$.* $E\setminus T$ contains no cut of $G$ $\iff$ $T'$ contains no cycle of $G^{*}$, which is condition (i) for $T'$ in $G^{*}$.

So $T$ is a spanning tree of $G$ exactly when $T'$ is a spanning tree of $G^{*}$ ✓.

*Counting check.* $\lvert T'\rvert = m - (n-1) = m - n + 1 = f - 1 = n^{*} - 1$, the correct number of edges for a spanning tree of $G^{*}$ ✓. $\blacksquare$

*Example.* For a plane tree $G$, $G^{*}$ has one vertex, $T' = \varnothing$ is its spanning tree, and $T = E(G)$ ✓.

## Challenge

**31.** *Strategy: construct the graph, prove the chromatic number increases by exactly one, prove triangle-freeness is preserved, and iterate.*

**Definition.** Let $G$ have vertex set $V = \{v_1,\dots,v_n\}$. The **Mycielskian** $M(G)$ has vertex set
$$V \cup U \cup \{w\}, \qquad U = \{u_1,\dots,u_n\},$$
and edge set consisting of all edges of $G$, all edges $u_ix$ with $x \in N_G(v_i)$, and all edges $wu_i$. There are no other edges: $U$ is independent and $w$ is adjacent only to the vertices of $U$.

**(1) $\chi(M(G)) = \chi(G) + 1$.**

*Upper bound.* Let $c$ be a proper $k$-colouring of $G$. Define a colouring of $M(G)$ by $c'(v_i) = c(v_i)$, $c'(u_i) = c(v_i)$, $c'(w) = k+1$. For an edge $u_ix$ with $x \in N(v_i)$ we have $c'(x) = c(x) \ne c(v_i) = c'(u_i)$ ✓; the edges of $G$ are proper ✓; the edges at $w$ are proper because no $u_i$ has colour $k+1$ ✓. So $\chi(M(G)) \le k+1$.

*Lower bound.* Let $t = \chi(M(G))$ and let $c$ be a proper $t$-colouring. Relabel the colours so that $c(w) = t$. Since every $u_i$ is adjacent to $w$, no $u_i$ has colour $t$. Define
$$c'(v_i) = \begin{cases} c(v_i), & c(v_i) \ne t, \\ c(u_i), & c(v_i) = t. \end{cases}$$
This is well defined (the second case uses $c(u_i) \ne t$). It is proper: for an edge $v_iv_j$ of $G$, at most one of $v_i,v_j$ has colour $t$, since they are adjacent. If neither does, properness is inherited from $c$. If $c(v_i) = t$, then $c'(v_i) = c(u_i)$, and $u_i$ is adjacent to $v_j$, so
$$c'(v_i) = c(u_i) \ne c(v_j) = c'(v_j) \ ✓ .$$
Hence $G$ is $(t-1)$-colourable, that is $\chi(G) \le \chi(M(G)) - 1$. Together with the upper bound, $\chi(M(G)) = \chi(G)+1$ ✓.

**(2) $M(G)$ is triangle-free whenever $G$ is.**

The set $U$ is independent, and $w$ is adjacent only to $U$, so a triangle cannot contain $w$ (its two other vertices would have to be adjacent members of $U$) and cannot contain two vertices of $U$. A triangle is therefore either three vertices of $V$ — a triangle of $G$ — or a vertex $u_i$ together with two vertices $x,y \in V$. In the second case $x,y \in N_G(v_i)$ and $x \sim y$, so $v_i, x, y$ form a triangle of $G$. Since $G$ has none, $M(G)$ has none ✓.

**(3) Iteration.** Start from $G_2 = K_2$: it has $\omega = \chi = 2$ and is triangle-free. Define $G_{k+1} = M(G_k)$. By (2), every $G_k$ is triangle-free, so $\omega(G_k) = 2$ for $k \ge 2$ (each $G_k$ has an edge). By (1), $\chi(G_k) = k$. Hence for every $k \ge 2$ there is a triangle-free graph with chromatic number $k$ ✓.

**(4) The first case.** $M(C_5)$ has
$$\lvert V\rvert = 1 + 5 + 5 = 11, \qquad \lvert E\rvert = 5 + 2\cdot 5 + 5 = 20$$
(the five edges of $C_5$, the $10 = \sum_v \deg v$ edges between $U$ and $V$, and the five edges at $w$). It is triangle-free by (2) and has $\chi = 3 + 1 = 4$ by (1): the **Grötzsch graph**, the smallest triangle-free $4$-chromatic graph ✓. By Grötzsch's theorem a triangle-free planar graph is $3$-colourable, so the Grötzsch graph is not planar ✓. $\blacksquare$

**32.** *Strategy: extend to a triangulation, then use the degree-sum identity $\sum(6 - \deg) = 12$.*

Let $G$ be planar with $n \ge 4$. Embed it and add edges one at a time, drawn inside faces, for as long as planarity is preserved; the process stops at a maximal planar graph $H$ on the same vertex set with $E(G) \subseteq E(H)$.

Because $n \ge 4$ and $H$ is maximal planar, every face of $H$ is a triangle (Theorem 7.5.1) and every vertex has degree at least $3$: the neighbours of a vertex $v$ occur in a cyclic order around $v$, and consecutive neighbours are joined by edges of the triangular faces, forming a cycle of length $\deg(v) \ge 3$.

Also $m_H = 3n - 6$ (Theorem 7.5.1). Compute
$$\sum_{v \in V}(6 - \deg_H(v)) = 6n - 2m_H = 6n - 2(3n - 6) = 12 .$$

Every vertex of degree at least $6$ contributes at most $0$ to this sum. Every vertex of degree at most $5$ contributes $6 - \deg_H(v) \le 6 - 3 = 3$. Hence
$$12 = \sum_v (6 - \deg_H(v)) \le 3\cdot \#\{v : \deg_H(v) \le 5\},$$
so there are at least $4$ vertices of degree at most $5$ in $H$.

Finally, $E(G)\subseteq E(H)$ gives $\deg_G(v) \le \deg_H(v)$ for every $v$, so each vertex of degree at most $5$ in $H$ also has degree at most $5$ in $G$. Hence $G$ has at least four vertices of degree at most $5$ ✓. $\blacksquare$

*Sharpness.* $K_4$ has four vertices, all of degree $3 \le 5$, and no fifth vertex; so the number four cannot be increased. The octahedron has six vertices, all of degree $4$, so it has six.

**33.** *Strategy: augment to a triangulation; a colouring of the supergraph restricts.*

*Augmentation.* Let $G$ be simple and planar with $n \ge 3$. Embed it. If some face has length at least $4$, two non-adjacent vertices on its boundary can be joined by an arc drawn inside the face, increasing the edge count by one and keeping the graph simple and planar. Repeat. Each step increases $m$, and $m \le \binom{n}{2}$ always, so the process terminates at a simple planar graph $H$ that contains $G$ as a spanning subgraph and to which no edge can be added: $H$ is maximal planar ✓.

*Reduction of the four-colour theorem.* A triangulation is planar, so "every planar graph is $4$-colourable" implies "every triangulation is $4$-colourable". Conversely, suppose every triangulation is $4$-colourable, and let $G$ be planar with $n \ge 3$. Take a maximal planar supergraph $H \supseteq G$ on the same vertex set. A proper $4$-colouring $c$ of $H$ restricts to a proper $4$-colouring of $G$: every edge of $G$ is an edge of $H$, so its endpoints have different colours ✓. For $n \le 2$ the graph is trivially $4$-colourable. Hence the theorem for all planar graphs follows from the theorem for triangulations ✓. $\blacksquare$

*Why this matters.* The proof of the four-colour theorem is a proof for triangulations (equivalently, for maximal planar graphs); the reduction shows that nothing is lost by restricting attention to them, and every discharging argument in the literature does exactly that.

**34.** *Strategy: (a) a face boundary is a closed walk, and an odd cycle would enclose an odd number of odd faces; (b) the degree of a dual vertex is a face length.*

(a) *If $G$ is bipartite*, every closed walk has even length (the parts alternate), and the boundary of every face is a closed walk; so every face length is even ✓.

*Conversely, suppose every face has even length.* Let $C$ be a cycle of $G$. As a simple closed curve, $C$ bounds a region $R$ of the plane. The faces of $G$ contained in $R$ have lengths summing to
$$\sum_{\varphi \subseteq R} \operatorname{len}(\varphi) = \lvert C\rvert + 2k,$$
where $k$ is the number of edges of $G$ that lie strictly inside $R$: each such edge is counted twice (once on each side), while each edge of $C$ is counted once. Since every face length is even, the sum is even, hence $\lvert C\rvert$ is even. So every cycle of $G$ is even, and by Solution 28 the graph is bipartite ✓.

(b) The vertices of $G^{*}$ correspond to the faces of $G$, and
$$\deg_{G^{*}}(\varphi) = \operatorname{len}(\varphi)$$
for each face $\varphi$: each edge on the boundary of $\varphi$ gives one dual edge at the dual vertex, and a bridge on the boundary is counted twice, exactly as the face length counts it twice. Hence
$$G^{*} \text{ is Eulerian} \iff \text{every degree of } G^{*} \text{ is even} \iff \text{every face of } G \text{ has even length} \iff G \text{ is bipartite},$$
the last equivalence by (a) ✓. $\blacksquare$

*Check.* If $G$ is a tree, $G$ is bipartite and $G^{*}$ has one vertex with $n-1$ loops; a loop contributes $2$ to the degree, so the degree is $2(n-1)$, even ✓ — agreeably with the criterion.

**35.** *Strategy: induction on $\lvert E\rvert$; split the sum according to whether the subset contains a fixed edge; identify the two halves with $G-e$ and $G/e$.*

**Claim (Whitney).** For every graph $G$ and every $k \ge 0$,
$$P_G(k) = \sum_{A \subseteq E(G)} (-1)^{\lvert A\rvert}\, k^{c(A)},$$
where $c(A)$ is the number of components of the spanning subgraph $(V,A)$.

*Proof.* Induct on $m = \lvert E(G)\rvert$.

*Base.* If $E = \varnothing$, the only subset is $A = \varnothing$, with $c(\varnothing) = n$; the sum is $k^n$, and indeed every colouring of the empty graph is proper, so $P_G(k) = k^n$ ✓.

*Step.* Let $e \in E(G)$ and split the subsets $A \subseteq E$ into those with $e \notin A$ and those with $e \in A$:
$$\sum_{A\subseteq E}(-1)^{\lvert A\rvert}k^{c_G(A)} = \underbrace{\sum_{A\subseteq E\setminus\{e\}}(-1)^{\lvert A\rvert}k^{c_G(A)}}_{S_1} \;+\; \underbrace{\sum_{B\subseteq E\setminus\{e\}}(-1)^{\lvert B\rvert+1}k^{c_G(B\cup\{e\})}}_{S_2}.$$

For $A \subseteq E\setminus\{e\}$ the component count $c_G(A)$ equals $c_{G-e}(A)$, because no edge other than $e$ was deleted. Hence $S_1 = \sum_{A\subseteq E(G-e)}(-1)^{\lvert A\rvert}k^{c_{G-e}(A)} = P_{G-e}(k)$ by induction ✓.

For $B \subseteq E\setminus\{e\}$, adding the edge $e$ to $B$ joins the two components of $(V,B)$ that contain the endpoints of $e$ (or creates a cycle inside one component if they already lie together). Contracting $e$ in $G$ identifies those two endpoints, so the component structure of $(V, B\cup\{e\})$ is exactly the component structure of the contraction graph $(V/e, B/e)$, where $B/e$ is the image of $B$ under the contraction. The correspondence $B \leftrightarrow B/e$ is a bijection between subsets of $E\setminus\{e\}$ and subsets of $E(G/e)$, and $\lvert B/e\rvert = \lvert B\rvert$. Hence
$$S_2 = -\sum_{B/e \subseteq E(G/e)} (-1)^{\lvert B/e\rvert}k^{c_{G/e}(B/e)} = -P_{G/e}(k)$$
by induction ✓.

Therefore the sum equals $P_{G-e}(k) - P_{G/e}(k)$, which is $P_G(k)$ by the deletion–contraction recurrence (Theorem 7.12.3) ✓. $\blacksquare$

*Integrality.* The right-hand side is a finite sum of terms $(-1)^{\lvert A\rvert}k^{c(A)}$ with integer coefficients, so $P_G$ is a polynomial with integer coefficients ✓. (This also shows that the a priori counting function agrees with a polynomial for all $k \ge 0$, since both sides are polynomials that agree at every non-negative integer.)

*Example.* For $K_3$ with edges $\{12,23,31\}$ the eight subsets give
$$k^3 - 3k^2 + (3k - k) = k^3 - 3k^2 + 2k = k(k-1)(k-2) \ ✓,$$
where the three one-edge subsets contribute $-k^2$ each, the three two-edge subsets contribute $+k$ each, and the full set contributes $-k$.

**36.** *Strategy: draw the wheel; colour rim and hub separately; for criticality delete one vertex at a time.*

(a) *Planarity.* Draw the rim $v_1v_2\cdots v_nv_1$ as a convex $n$-gon in the plane, and place the hub $h$ at its centre. The $n$ spokes $hv_i$ can be drawn as straight segments inside the polygon; they meet only at $h$ and meet the rim only at the rim vertices ✓. So $W_n$ is planar. It has $n+1$ vertices and $2n$ edges ($n$ rim edges plus $n$ spokes), and
$$2n \le 3(n+1) - 6 = 3n - 3 \iff n \ge 3 \ ✓,$$
consistent with the bound.

(b) *Chromatic number.* $W_n$ contains the triangle $h\,v_i\,v_{i+1}$ for every $i$, so $\chi(W_n) \ge 3$.

*If $n$ is even*, colour the rim alternately with colours $2$ and $3$ (possible since $C_n$ is bipartite) and give the hub colour $1$. Every rim vertex differs from its two rim neighbours and from the hub ✓, so $\chi(W_n) \le 3$ and hence $\chi(W_n) = 3$.

*If $n$ is odd*, the rim needs three colours, so suppose the rim is coloured with $\{1,2,3\}$. The hub is adjacent to every rim vertex, so it must avoid all colours used on the rim. If the rim uses all three colours, the hub needs a fourth, so $\chi(W_n) \ge 4$. Four suffice: colour the rim with three colours (alternating $1,2$ around the odd cycle and giving one vertex the colour $3$) and the hub the colour $4$ ✓. Hence $\chi(W_n) = 4$.

(c) *Criticality for odd $n$.* Let $n$ be odd. We show $\chi(W_n - x) = 3$ for every vertex $x$.
* If $x = h$: $W_n - h = C_n$, which has chromatic number $3$ (odd cycle) ✓.
* If $x = v_i$: the remaining graph consists of $h$ together with the path $v_{i+1}v_{i+2}\cdots v_{i-1}$ (the rim with $v_i$ removed), and $h$ is adjacent to every vertex of the path. Colour the path alternately with colours $1,2$ (a path is bipartite) and give $h$ colour $3$ ✓. So $\chi(W_n - v_i) \le 3$, and it is at least $3$ because the remaining graph contains a triangle whenever $n \ge 4$ (for $n = 3$, $W_3 = K_4$ and deleting any vertex leaves $K_3$) ✓.

Hence $\chi(W_n - x) = 3 < 4 = \chi(W_n)$ for every vertex $x$, so $W_n$ is $4$-critical ✓. $\blacksquare$

*Remark.* The odd wheels are the standard examples of 4-critical planar graphs, and they are the reason the four-colour theorem cannot be proved by a local exchange argument of the kind used for five colours: at the hub of an odd wheel, all four colours appear on the neighbours, and every Kempe swap is blocked in one of the two ways analysed in Solution 23.

