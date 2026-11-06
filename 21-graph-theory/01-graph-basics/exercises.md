# Graph Basics — Exercises

> [Graph Basics](README.md) · 36 problems · Beginner → Challenge · Solutions: [solutions.md](solutions.md)

Attempt every problem in writing before looking at [solutions.md](solutions.md). Each problem names the section of the tutorial that supplies the technique, so a stuck reader knows where to reread.

Notation: $G = (V,E)$ is a finite simple graph unless the problem says otherwise, $n = \lvert V\rvert$, $m = \lvert E\rvert$, and $uv$ denotes the edge $\{u,v\}$. Degrees count loops twice. $\binom{n}{k}$ is the binomial coefficient. A "graphical sequence" is the degree sequence of some simple graph.

## Beginner

**1.** *(§7.3)* For the graph $G$ with $V = \{1,2,3,4,5,6,7\}$ and
$$E = \{12,\ 13,\ 14,\ 23,\ 25,\ 36,\ 45,\ 67\},$$
compute all seven degrees, verify the handshake lemma, and state $\delta(G)$, $\Delta(G)$ and the degree sequence in non-increasing order.

**2.** *(§7.4)* For the graph $G$ of Problem 1, write down $E(\overline{G})$ explicitly, compute the degree sequence of $\overline{G}$, and verify both identities of Proposition 7.4.4.

**3.** *(§5.1, §5.2)* Let $M$ be the multigraph with $V = \{a,b,c,d\}$ and edges $e_1 = ab$, $e_2 = ab$, $e_3 = bc$, $e_4 = cc$, $e_5 = ad$.
(a) Compute the degree of every vertex (loops counting twice) and verify the handshake lemma.
(b) Explain why $M$ is neither a simple graph nor a tree.

**4.** *(§7.3, §5.3)* (a) A $3$-regular graph has $18$ edges. How many vertices does it have?
(b) A graph on $5$ vertices is $4$-regular. How many edges does it have, and which named graph is it?
(c) Explain why no $3$-regular graph has exactly $5$ vertices.

**5.** *(§7.8)* Decide whether each of the following is bipartite, justifying each answer with either an explicit bipartition or an explicit odd cycle: $C_4$, $C_7$, $K_{3,3}$, $K_5$, $P_5$, and the Petersen graph.

**6.** *(§7.3, §5.3)* For the complete graph $K_8$: state the number of vertices, the number of edges, the degree of every vertex and the sum of all degrees. Check the handshake lemma against your edge count.

**7.** *(§7.3, §7.8)* For $K_{3,5}$: state the number of vertices, the number of edges, the degree of every vertex and the sum of all degrees. Verify Proposition 7.8.5 and the handshake lemma.

**8.** *(§7.10)* The matrix $A$ below is the adjacency matrix of a simple graph on $\{1,2,3,4\}$, rows and columns in that order.
$$A = \begin{pmatrix}0&1&0&1\\1&0&1&1\\0&1&0&1\\1&1&1&0\end{pmatrix}.$$
List the edges, compute the degree sequence, decide whether the graph is bipartite, and compute $(A^2)_{14}$, interpreting it as a number of walks.

**9.** *(§7.5)* In the graph $G$ of Problem 1, classify each sequence below as a walk, a trail, a path or a cycle; more than one label may apply.
(a) $7,6,3,1,4,5,2$  (b) $6,3,1,2,3,6$  (c) $4,1,4$  (d) $1,2,5,4,1$.

**10.** *(§7.6)* Find all components of the graph with $V = \{1,\dots,8\}$ and $E = \{12,\ 23,\ 13,\ 45,\ 56,\ 78\}$, and state $c(G)$.

**11.** *(§7.7)* (a) Is $C_4$ isomorphic to the graph obtained by attaching one pendant edge to a triangle? (b) Is $P_4$ isomorphic to the graph with $V = \{a,b,c,d\}$ and $E = \{ab, bc, cd\}$? In each case give either an explicit isomorphism or an invariant that differs.

**12.** *(§7.4)* Describe $\overline{K_{2,3}}$, $\overline{K_4}$ and $\overline{C_5}$: for each, state the number of vertices, the number of edges, and name the resulting graph if it has a standard name.

## Intermediate

**13.** *(§7.3, §7.9)* Prove that a simple graph on $n$ vertices has at most $\binom{n}{2}$ edges, and that equality holds if and only if the graph is complete.

**14.** *(§7.3)* Prove that every simple graph with $n \ge 2$ vertices has two vertices of the same degree.

**15.** *(§7.3)* Prove that a $k$-regular graph on $n$ vertices has $m = kn/2$ edges, and deduce that $kn$ is even. Use this to prove that no $3$-regular graph has an odd number of vertices.

**16.** *(§7.3)* (a) Prove that the number of odd-degree vertices of a finite graph is even.
(b) Can a graph have exactly one vertex of odd degree? Exactly two? Exactly three? Give an example or a proof in each case.

**17.** *(§7.11)* Decide by the Havel–Hakimi algorithm whether each sequence is graphical, and exhibit a realisation when it is:
(a) $(4,3,3,1,1)$; (b) $(3,2,2,2,2,1)$; (c) $(3,3,3,3,2)$.

**18.** *(§7.8)* Prove that a graph is bipartite if and only if $V$ can be partitioned into two sets $A$ and $B$ with no edge inside $A$ and no edge inside $B$. Then prove that if $G$ has at least one edge, both parts of a bipartition can be chosen non-empty.

**19.** *(§7.8)* Let $G$ be bipartite with parts of sizes $a$ and $b$. Prove that $m \le ab$ and deduce that a bipartite graph on $n$ vertices has at most $\lfloor n^2/4\rfloor$ edges. Check the bound on $K_{3,3}$ and on $K_{4,4}$.

**20.** *(§7.10)* For the path $P_3$ on vertices $1,2,3$: write down $A$, compute $A^2$ and $A^3$, and interpret $(A^2)_{13}$, $(A^2)_{11}$, $(A^3)_{11}$ and $(A^3)_{13}$ as walk counts. Explain why the last two entries vanish.

**21.** *(§7.6)* Prove that a simple graph on $n \ge 2$ vertices with $m \ge \binom{n-1}{2} + 2$ edges is connected.

**22.** *(§7.4, §7.6)* Prove that the complement of a disconnected simple graph is connected. Then give an example of a connected graph whose complement is disconnected.

## Advanced

**23.** *(§7.5)* Prove that every $u$–$v$ walk contains a $u$–$v$ path.

**24.** *(§7.8)* Prove that every closed walk of odd length contains a cycle of odd length.

**25.** *(§7.3, §7.5)* Prove that if every vertex of a finite graph has even degree, then the edge set can be partitioned into edge-disjoint cycles.

**26.** *(§7.8)* Prove that a graph is bipartite if and only if it has no closed walk of odd length.

**27.** *(§5.1, §7.3)* For a digraph $D = (V,A)$, let $\deg^+(v)$ and $\deg^-(v)$ be the out-degree and in-degree of $v$.
(a) Prove that $\sum_{v \in V} \deg^+(v) = \sum_{v \in V} \deg^-(v) = \lvert A\rvert$.
(b) Show by example that two digraphs with the same underlying graph can have different out-degree sequences.

**28.** *(§7.3, §7.6)* Prove that a simple graph on $n \ge 2$ vertices with $\delta(G) \ge (n-1)/2$ is connected.

**29.** *(§7.10)* Prove that simple graphs $G$ and $H$ on $n$ vertices are isomorphic if and only if there is an $n \times n$ permutation matrix $P$ with $A(H) = P\,A(G)\,P^{\mathsf T}$.

**30.** *(§7.10)* Prove that $\sum_{v \in V} \deg(v)^2$ equals the number of walks of length $2$ in $G$, and deduce from the Cauchy–Schwarz inequality that
$$\sum_{v \in V} \deg(v)^2 \ \ge \ \frac{4m^2}{n}.$$

## Challenge

**31.** *(§7.9)* (Mantel's theorem) Prove that a simple graph on $n$ vertices containing no triangle has at most $\lfloor n^2/4\rfloor$ edges.

**32.** *(§7.7)* Determine the number of pairwise non-isomorphic simple graphs on $4$ vertices. Tabulate them by number of edges, and identify every self-complementary graph on $4$ vertices.

**33.** *(§7.6, §7.8)* Prove that every graph with $m$ edges has a bipartite subgraph with at least $m/2$ edges.

**34.** *(§7.3)* Prove that every graph with $n$ vertices and $m$ edges has a non-empty subgraph whose minimum degree is at least $m/n$.

**35.** *(§7.5)* Prove that a simple graph in which every vertex has degree at least $2$ contains a cycle of length at least $\delta(G) + 1$.

**36.** *(§7.4, §7.7)* A graph is **self-complementary** if $G \cong \overline{G}$. Prove that a self-complementary graph on $n$ vertices exists if and only if $n \equiv 0$ or $1 \pmod 4$.
