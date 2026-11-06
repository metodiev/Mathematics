# Paths and Connectivity — Exercises

> [Paths and Connectivity](README.md) · 36 problems · Beginner → Challenge · Solutions: [solutions.md](solutions.md)

Attempt every problem in writing before looking at [solutions.md](solutions.md). Each problem names the section of the tutorial that supplies the technique, so a stuck reader knows where to reread.

Notation: $G = (V,E)$ is a finite graph, $n = \lvert V\rvert$, $m = \lvert E\rvert$; $uv$ denotes the edge $\{u,v\}$; a graph is simple unless the problem says otherwise. All distances are with respect to the stated edge weights. "$L(G)$" is the line graph of $G$: its vertices are the edges of $G$, two of them adjacent when the corresponding edges share an endpoint.

## Beginner

**1.** *(§7.2, §7.3)* For each graph, compute the degree sequence, count the odd-degree vertices, and decide whether the graph has an Eulerian circuit, an Eulerian trail but no circuit, or neither. Cite the criterion you use.
(a) $C_5$; (b) $K_4$; (c) the house (a square $1$–$2$–$3$–$4$–$1$ with a roof $5$ joined to $2$ and $3$); (d) the bowtie (two triangles sharing exactly one vertex); (e) $K_{3,3}$.

**2.** *(§7.1, §7.3)* The Königsberg multigraph has vertices $A,B,C,D$ with degrees $5,3,3,3$ and seven bridges.
(a) Explain why no Eulerian trail exists.
(b) One bridge is demolished. Which bridges leave an Eulerian trail, and what are its endpoints? Prove that no single demolition can produce an Eulerian circuit.

**3.** *(§7.2, §7.5)* Let $V = \{1,\dots,7\}$ and $E = \{12, 23, 31, 34, 45, 53, 56, 67, 75\}$.
(a) Verify that every degree is even and that the graph is connected.
(b) Run Hierholzer's algorithm starting at $1$ and write down an Eulerian circuit.
(c) How many edges does the circuit have, and how many vertices does it visit?

**4.** *(§7.3)* Let $V = \{1,\dots,6\}$ and $E = \{12, 23, 34, 45, 51, 16, 64\}$.
(a) Compute the degrees and identify the odd vertices.
(b) Write down an Eulerian trail.
(c) Explain why every Eulerian trail must start at $1$ or at $4$.

**5.** *(§7.4)* Decide for each digraph whether it has a directed Eulerian circuit, a directed Eulerian trail but no circuit, or neither. Justify with in-degrees, out-degrees and connectivity.
(a) $V = \{1,2,3\}$ and arcs $1\to2,\ 2\to3,\ 3\to1,\ 1\to3,\ 3\to2,\ 2\to1$.
(b) $V = \{1,2,3,4\}$ and arcs $1\to2,\ 2\to3,\ 3\to1,\ 3\to4$.

**6.** *(§7.7, §7.8)* (a) For $K_{3,3}$: compute $n$ and $\delta$, decide whether Dirac's condition holds, and either exhibit a Hamiltonian cycle or prove that none exists.
(b) Same questions for $K_6$.
(c) Same questions for $C_6$. What does the comparison of (a)–(c) show about the status of Dirac's condition?

**7.** *(§7.6, §7.7)* For each graph decide whether it has a Hamiltonian cycle, only a Hamiltonian path, or neither, and justify the answer with a proof or a named necessary condition.
(a) $K_{2,3}$; (b) $C_6$; (c) the bowtie; (d) $K_4$; (e) $P_5$.

**8.** *(§7.11)* Run Dijkstra's algorithm from vertex $1$ on the graph with $V = \{1,\dots,5\}$ and edges
$$12:4,\quad 13:2,\quad 23:1,\quad 24:5,\quad 34:8,\quad 35:10,\quad 45:2,\quad 25:12 .$$
Produce a table of tentative labels after each extraction, state the final distances, and give a shortest path from $1$ to $5$.

**9.** *(§7.12)* Run Bellman–Ford from $s$ on the graph with $V = \{s,a,b,c,t\}$ and edges
$$sa:6,\quad sb:7,\quad sc:3,\quad cb:2,\quad ba:-2,\quad at:5,\quad bt:4,\quad ct:20 .$$
Give the labels after each pass, the final distances, and the shortest $s$–$t$ path. Is there a negative cycle?

**10.** *(§7.14, §7.16)* Let $V = \{1,\dots,7\}$ and
$$E = \{12,\ 23,\ 31,\ 34,\ 45,\ 56,\ 64,\ 27\}.$$
Find every bridge, every cut vertex and every block, and draw the block-cut tree.

**11.** *(§7.14)* Compute $\kappa(G)$, $\lambda(G)$ and $\delta(G)$ for each graph, and verify Whitney's inequality: (a) $K_4$; (b) $C_6$; (c) $K_{2,3}$; (d) the star $K_{1,4}$; (e) $P_5$.

**12.** *(§7.5, §7.10, §7.14)* Name the most appropriate algorithm or theorem for each task, and state its running time in terms of $n$ and $m$.
(a) single-source shortest paths with non-negative weights on a sparse graph;
(b) single-source shortest paths with arbitrary real weights, where a negative cycle must be reported;
(c) all-pairs shortest paths on a dense graph with $n = 300$;
(d) constructing an Eulerian circuit;
(e) finding all bridges;
(f) computing $\kappa(G)$ for a graph with $100$ vertices and $400$ edges.

## Intermediate

**13.** *(§7.2)* Prove the necessity direction of Euler's criterion: if a graph with $m \ge 1$ has an Eulerian circuit, then all its edges lie in one component and every vertex has even degree. Do not quote the theorem; give the counting argument in full, including the case of the starting vertex.

**14.** *(§7.2)* Prove Lemma 7.2.2 (a maximal trail in a graph with all degrees even is closed) and then Theorem 7.2.3 (sufficiency), including the claim that if unused edges remain, some vertex of the current closed trail is incident with an unused edge.

**15.** *(§7.3)* Prove Theorem 7.3.1: a connected graph with $m \ge 1$ has an Eulerian trail if and only if it has $0$ or $2$ odd-degree vertices. Then deduce that when there are exactly two odd vertices, every Eulerian trail has them as endpoints.

**16.** *(§7.2, §7.14)* (a) Prove that a connected Eulerian graph with at least one edge has no bridge. (b) Show that the converse fails: exhibit a connected graph in which every edge lies on a cycle but which is not Eulerian.

**17.** *(§7.7)* (a) Prove the cut condition: if $G$ is Hamiltonian and $S \subseteq V$, then $c(G - S) \le \lvert S\rvert$. (b) Apply it to $K_{2,3}$ with a suitable $S$ to prove that $K_{2,3}$ is not Hamiltonian. (c) Explain why the condition cannot be a characterisation.

**18.** *(§7.7)* (a) Prove that a bipartite Hamiltonian graph has parts of equal size. (b) The Herschel graph is bipartite with $11$ vertices and parts of sizes $6$ and $5$; deduce that it is not Hamiltonian. (c) Show that $K_{3,3}$ satisfies the balance condition and is Hamiltonian, so balance is not sufficient.

**19.** *(§7.14)* Prove Whitney's inequality $\kappa(G) \le \lambda(G) \le \delta(G)$ for a graph with at least two vertices, including the full construction that turns a minimum edge cut into a vertex cut of no greater size.

**20.** *(§7.14)* Prove: (a) an edge $e$ is a bridge if and only if $e$ lies on no cycle; (b) a vertex $v$ is a cut vertex if and only if there exist vertices $u,w \ne v$ such that every $u$–$w$ path passes through $v$.

**21.** *(§7.12)* Prove the round invariant of Bellman–Ford: after the $k$-th pass, $d[v]$ is the weight of some $s$–$v$ walk and is at most the weight of every $s$–$v$ walk with at most $k$ edges.

**22.** *(§7.13)* Run Floyd–Warshall on the digraph with $V = \{1,2,3,4\}$ and arcs
$$1\to2:2,\quad 2\to3:3,\quad 3\to1:4,\quad 1\to3:9,\quad 3\to4:2,\quad 4\to2:5,\quad 4\to1:8 .$$
Display $D^{(0)}, D^{(1)}, D^{(2)}, D^{(3)}, D^{(4)}$, verify two entries by exhibiting explicit paths, and check that there is no negative cycle.

## Advanced

**23.** *(§7.8)* Prove Ore's theorem: if $n \ge 3$ and $\deg(u) + \deg(v) \ge n$ for every pair of non-adjacent vertices, then $G$ is Hamiltonian. Use the maximal non-Hamiltonian supergraph and the rotation argument.

**24.** *(§7.8)* Deduce Dirac's theorem from Ore's theorem. Then show that $C_n$ with $n \ge 5$ is Hamiltonian but satisfies neither hypothesis, and explain why this means no strengthening of the constants can turn either theorem into a characterisation.

**25.** *(§7.8)* Prove the Bondy–Chvátal lemma: if $u$ and $v$ are non-adjacent and $\deg(u) + \deg(v) \ge n$, then $G$ is Hamiltonian if and only if $G + uv$ is Hamiltonian.

**26.** *(§7.6, §7.9)* Let $G \vee K_1$ be the graph obtained from $G$ by adding one new vertex adjacent to every vertex of $G$. Prove that $G$ has a Hamiltonian path if and only if $G \vee K_1$ has a Hamiltonian cycle. Explain why this is a polynomial-time reduction from Hamiltonian Path to Hamiltonian Cycle.

**27.** *(§7.15)* Prove that a graph with $n \ge 3$ is 2-connected if and only if every two vertices lie on a common cycle. You may use Menger's theorem in the global form (Theorem 7.15.3).

**28.** *(§7.14)* Prove that a connected graph is 2-edge-connected (that is, $\lambda(G) \ge 2$) if and only if every edge lies on a cycle.

**29.** *(§7.16)* Prove that the block-cut graph of a connected graph is a tree.

**30.** *(§7.2)* Prove that a connected graph with at least one edge is Eulerian if and only if its edge set can be partitioned into cycles.

## Challenge

**31.** *(§7.6, §7.9)* Prove that the Petersen graph is not Hamiltonian. Model it with outer vertices $a_0,\dots,a_4$ in a pentagon, inner vertices $b_0,\dots,b_4$ forming a pentagram (edges $b_ib_{i+2}$, indices mod $5$), and spokes $a_ib_i$. Let $k$ be the number of spokes used by a putative Hamiltonian cycle; show that $k$ is even and at most $4$, then rule out $k = 2$ and $k = 4$.

**32.** *(§7.7)* Prove Rédei's theorem: every tournament (an orientation of a complete graph) has a Hamiltonian path. Use induction on the number of vertices, inserting the new vertex into the Hamiltonian path of the smaller tournament.

**33.** *(§7.6)* Prove that if $G$ is connected and Eulerian with $m \ge 3$, then its line graph $L(G)$ has a Hamiltonian cycle. Show by an example that the converse fails: a graph whose line graph is Hamiltonian need not be Eulerian.

**34.** *(§7.3)* Prove that if $G$ is connected with exactly $2k$ vertices of odd degree, $k \ge 1$, then $E(G)$ can be partitioned into $k$ trails, and that no partition into fewer than $k$ trails exists.

**35.** *(§7.7)* Let $G$ be bipartite with parts $X$ and $Y$. (a) Prove that if $G$ is Hamiltonian then $\lvert N(S)\rvert \ge \lvert S\rvert$ for every $S \subseteq X$. (b) Deduce that a bipartite graph failing this condition for some $S$ is not Hamiltonian, and apply it to the Herschel graph, whose parts have sizes $6$ and $5$.

**36.** *(§7.16)* Prove that a connected graph with at least one edge is Eulerian if and only if every one of its blocks is Eulerian.
