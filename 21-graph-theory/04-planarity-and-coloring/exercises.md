# Planarity and Colouring — Exercises

> [Planarity and Colouring](README.md) · 36 problems · Beginner → Challenge · Solutions: [solutions.md](solutions.md)

Attempt every problem in writing before looking at [solutions.md](solutions.md). Each problem names the section of the tutorial that supplies the technique, so a stuck reader knows where to reread.

Notation: $G$ is a finite simple graph with $n = \lvert V\rvert$ and $m = \lvert E\rvert$ unless the problem says otherwise; $f$ is the number of faces of a stated plane embedding; $G^{*}$ is the dual with respect to that embedding; $\chi$, $\omega$, $\alpha$ are the chromatic number, clique number and independence number. $W_n$ is the wheel with $n$ rim vertices (so $n+1$ vertices in total). $P_G(k)$ is the chromatic polynomial.

## Beginner

**1.** *(§7.2)* For each plane graph, count $V$, $E$ and $F$, verify Euler's formula, and check the face handshake:
(a) the cube $Q_3$ drawn as a cube;
(b) the octahedron;
(c) $K_4$ drawn as a tetrahedron.

**2.** *(§7.3, §7.4, §7.6)* Decide whether each graph is planar, justifying each answer with a drawing or with a counting bound: (a) $K_4$; (b) $K_{2,4}$; (c) $K_{3,3}$; (d) the cube $Q_3$; (e) $K_5$; (f) the wheel $W_5$.

**3.** *(§7.3)* (a) Show that a $4$-regular simple planar graph must have at least $6$ vertices. (b) Verify the bound is attained by the octahedron. (c) Explain why $K_5$ is ruled out by (a) as well as by the edge bound.

**4.** *(§7.4)* (a) State the bound $m \le 2n - 4$ for triangle-free planar graphs and apply it to $K_{3,3}$. (b) Apply it to $K_{2,4}$ and check that equality holds. (c) Apply it to $K_{3,3}$ with one edge deleted ($n = 6$, $m = 8$) and explain why the bound cannot decide whether that graph is planar. (It is planar.)

**5.** *(§7.8)* For each graph compute $\chi$, $\omega$ and $\alpha$: (a) $K_4$; (b) $C_5$; (c) $K_{2,3}$; (d) the Petersen graph; (e) $P_4$.

**6.** *(§7.9)* Let $G$ be the triangle $1$–$2$–$3$ with a pendant vertex attached to each of $1$, $2$, $3$ (so $V = \{1,\dots,6\}$ and $E = \{12, 23, 31, 14, 25, 36\}$). Run greedy colouring in the order $4,5,6,1,2,3$ and again in the order $1,2,3,4,5,6$. How many colours does each order use? What is $\chi(G)$?

**7.** *(§7.12)* Compute $P_G(k)$ by direct counting (not by the recurrence) for (a) $K_3$; (b) $P_3$; (c) $C_4$; (d) $K_{1,3}$.

**8.** *(§7.12)* For $C_5$, compute $P_{C_5}(2)$, $P_{C_5}(3)$ and $P_{C_5}(4)$ from the formula $(k-1)^5 - (k-1)$. What do the three values tell you about $\chi(C_5)$?

**9.** *(§7.8)* (a) Exhibit a proper 2-colouring of the cube $Q_3$ and explain why one colour is impossible. (b) Exhibit a proper 3-colouring of the wheel $W_6$ and explain why two colours are impossible.

**10.** *(§7.1)* Let $G$ have $V = \{1,\dots,5\}$ and $E = \{12, 23, 31, 34, 45, 51\}$, drawn so that the triangle $1$–$2$–$3$ and the quadrilateral $1$–$3$–$4$–$5$ are bounded faces. List the faces, give their lengths, and check the face handshake.

**11.** *(§7.7)* Compute the dual of the cube $Q_3$: state $n^{*}$, $m^{*}$, $f^{*}$, and identify the resulting graph by name.

**12.** *(§7.8)* Find $\chi$ for the graph with $V = \{1,\dots,6\}$ and $E = \{12, 23, 34, 45, 56, 61, 13, 46\}$, and prove your answer.

## Intermediate

**13.** *(§7.2)* Prove Euler's formula $n - m + f = 2$ for connected plane graphs by induction on $m$. State clearly the two facts about deleting an edge that the proof uses, and explain where the hypothesis of connectivity enters.

**14.** *(§7.3)* Prove that for a simple planar graph with $n \ge 3$ every face has length at least $3$, that $3f \le 2m$, and that $m \le 3n - 6$. Identify exactly where simplicity and the hypothesis $n \ge 3$ are used, and give a counterexample to the bound when $n = 2$.

**15.** *(§7.4)* Prove that a simple planar graph with $n \ge 3$ and no triangle satisfies $m \le 2n - 4$. Deduce that $K_{3,3}$ is not planar, and show that $K_{2,n}$ attains the bound for every $n \ge 2$.

**16.** *(§7.3, §7.4)* Prove that every simple planar graph with $n \ge 3$ has a vertex of degree at most $5$, and that every simple bipartite planar graph with $n \ge 3$ has a vertex of degree at most $3$. Explain why the second statement does not follow from the first.

**17.** *(§7.5)* Prove that for a simple planar graph with $n \ge 3$ the following are equivalent: (a) $G$ is maximal planar; (b) in some embedding every face is a triangle; (c) $m = 3n - 6$.

**18.** *(§7.7)* Let $G$ be a connected plane graph. Prove that $n^{*} = f$, $m^{*} = m$, $f^{*} = n$, that $G^{*}$ is connected, and that $G^{**} \cong G$.

**19.** *(§7.7)* Prove that an edge $e$ of a connected plane graph is a bridge if and only if $e^{*}$ is a loop of the dual. Deduce that a connected plane graph with at least two vertices is a tree if and only if its dual has exactly one vertex (all edges loops).

**20.** *(§7.12)* Prove the deletion–contraction recurrence $P_G(k) = P_{G-e}(k) - P_{G/e}(k)$ for a graph $G$ and an edge $e$. Explain why the contraction may produce parallel edges and why they do not affect the count.

**21.** *(§7.12)* Prove that $P_T(k) = k(k-1)^{n-1}$ for a tree with $n$ vertices, and that $P_{C_n}(k) = (k-1)^n + (-1)^n(k-1)$ for $n \ge 3$. Check both formulas at $n = 3$ and at $n = 4$.

**22.** *(§7.8, §7.9)* Prove that $\chi(G) \le \Delta(G) + 1$ for every graph, and that $\chi(G) \ge \lceil n/\alpha(G)\rceil$. Use the second inequality to show that $\chi(C_5) \ge 3$.

## Advanced

**23.** *(§7.14)* Prove the five-colour theorem in full: every planar graph has a proper colouring with five colours. Include the Kempe-chain argument and the use of the Jordan curve theorem, and explain why the argument does not give four colours.

**24.** *(§7.9)* Prove that every planar graph is $6$-colourable by induction using a vertex of degree at most $5$. Explain why the same induction, with five colours, fails, and what additional idea the five-colour theorem supplies.

**25.** *(§7.8, §7.11)* (a) Prove that $\chi(G) \ge \omega(G)$ for every graph, and exhibit a graph where the inequality is strict. (b) Prove that for every $k \ge 2$ there is a graph with $\omega = 2$ and $\chi = k$; you may quote the Mycielski construction but must verify that it has the stated effect.

**26.** *(§7.12)* Let $G$ have $n \ge 1$ vertices and $m$ edges. Prove that $P_G(k)$ is a polynomial of degree $n$ with leading coefficient $1$, constant term $0$, and coefficient of $k^{n-1}$ equal to $-m$. Deduce that $P_G$ determines $n$ and $m$.

**27.** *(§7.5)* Let $G$ be a simple planar graph with $n \ge 3$ and $m = 3n - 6$. Prove that every face of every plane embedding of $G$ is a triangle, and deduce that no edge can be added to $G$ without destroying planarity.

**28.** *(§7.8)* Prove that a graph is bipartite if and only if it has no cycle of odd length. Deduce the values of $\chi(C_n)$ for even and odd $n$, and prove that $\chi(G) \le 2$ if and only if $G$ is bipartite.

**29.** *(§7.15)* (a) Prove that the four-colour theorem is equivalent to the statement $P_G(4) > 0$ for every planar graph $G$. (b) Show that $P_G(3) > 0$ fails for some planar $G$, and identify the smallest such $G$. (c) Explain why (a) is not a proof of the theorem.

**30.** *(§7.7)* Let $G$ be a connected plane graph and $T \subseteq E(G)$. Prove that $T$ is the edge set of a spanning tree of $G$ if and only if $\{e^{*} : e \in E(G)\setminus T\}$ is the edge set of a spanning tree of $G^{*}$.

## Challenge

**31.** *(§7.11)* Define the Mycielski construction $M(G)$ and prove that $\chi(M(G)) = \chi(G) + 1$ and that $M(G)$ is triangle-free whenever $G$ is. Deduce that there are triangle-free graphs of every chromatic number $k \ge 2$, and describe the graph $M(C_5)$ (the Grötzsch graph) and its chromatic number.

**32.** *(§7.3, §7.5)* Prove that every planar graph with $n \ge 4$ has at least four vertices of degree at most $5$. Use a maximal planar supergraph and the identity $\sum_v (6 - \deg v) = 12$.

**33.** *(§7.5, §7.15)* Prove that every simple planar graph with $n \ge 3$ is a spanning subgraph of a maximal planar graph on the same vertex set, and deduce that the four-colour theorem holds for all planar graphs if and only if it holds for triangulations.

**34.** *(§7.7, §7.8)* Let $G$ be a connected plane graph with $n \ge 2$. (a) Prove that $G$ is bipartite if and only if every face of the embedding has even length. (b) Deduce that the dual $G^{*}$ is Eulerian if and only if $G$ is bipartite.

**35.** *(§7.12)* Prove Whitney's expansion
$$P_G(k) = \sum_{A \subseteq E(G)} (-1)^{\lvert A\rvert} k^{c(A)},$$
where $c(A)$ is the number of components of the spanning subgraph $(V, A)$, by induction on $\lvert E\rvert$ using deletion–contraction. Deduce that $P_G$ is a polynomial with integer coefficients.

**36.** *(§7.8)* Let $W_n$ be the wheel with hub $h$ and rim $v_1v_2\cdots v_nv_1$. (a) Show that $W_n$ is planar. (b) Prove that $\chi(W_n) = 4$ when $n$ is odd and $\chi(W_n) = 3$ when $n$ is even. (c) Prove that for odd $n$, $W_n$ is $4$-critical.
