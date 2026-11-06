# Matching and Flows — Exercises

> [Matching and Flows](README.md) · 36 problems · Beginner → Challenge · Solutions: [solutions.md](solutions.md)

Attempt every problem in writing before opening [solutions.md](solutions.md). Each problem names the
section of the tutorial that supplies the technique.

Notation: $G$ is a finite simple graph; $n=\lvert V\rvert$, $m=\lvert E\rvert$; $\alpha'(G)$ is the
matching number, $\tau(G)$ the vertex-cover number; in a bipartite graph the sides are $A$ and $B$ and
$N(S)$ is the neighbourhood of $S\subseteq A$. A matching is written as a set of edges, e.g.
$\{a_1b_1,\ a_3b_2\}$; "$uv$" means the edge $\{u,v\}$.

## Beginner

**1.** *(§7.1)* For each graph give $\alpha'(G)$ and state whether it has a perfect matching:
(a) $P_7$; (b) $C_6$; (c) $K_{1,5}$; (d) $K_{3,4}$; (e) $K_4$.

**2.** *(§7.1)* How many perfect matchings does each graph have: $K_6$, $K_{4,4}$, $C_8$, $P_8$, $K_{2,3}$?

**3.** *(§7.1)* Write the edges of $K_{3,3}$ (sides $A=\{a_1,a_2,a_3\}$, $B=\{b_1,b_2,b_3\}$) as a union
of three perfect matchings.

**4.** *(§7.2)* Let $V=\{1,\dots,6\}$ and $E=\{12,23,34,45,56,26\}$. Give a maximal matching of size $2$,
a maximum matching of size $3$, and an augmenting path for the maximal one.

**5.** *(§7.2)* In the cycle $C_6=1234561$ with the matching $M=\{12,45\}$, find an $M$-augmenting path
and compute $M\triangle P$.

**6.** *(§7.4)* Let $A=\{a_1,\dots,a_4\}$, $B=\{b_1,\dots,b_4\}$ and
$$E=\{a_1b_1,a_1b_2,\ a_2b_1,a_2b_2,\ a_3b_1,a_3b_2,\ a_4b_2,a_4b_3,a_4b_4\}.$$
Find a deficient set, decide whether a perfect matching exists, and compute $\alpha'(G)$.

**7.** *(§7.3)* Let $A=\{a_1,a_2,a_3\}$, $B=\{b_1,b_2,b_3\}$ with
$E=\{a_1b_1,a_1b_2,\ a_2b_1,\ a_3b_2,a_3b_3\}$ and $M=\{a_1b_1\}$. Run one round of the alternating BFS:
exhibit the augmenting path, augment, and state the new matching.

**8.** *(§7.4)* Five students must each be given a distinct project. Allowed projects:
$s_1:\{p_1,p_2\}$, $s_2:\{p_1,p_2\}$, $s_3:\{p_2,p_3\}$, $s_4:\{p_3,p_4\}$, $s_5:\{p_1\}$.
Does a system of distinct representatives exist? Find the maximum number of students that can be served.

**9.** *(§7.6)* For the graph of Problem 6, find a minimum vertex cover and verify that its size equals
the matching number.

**10.** *(§7.8)* A network on $s,a,b,t$ has arcs $sa:4$, $sb:2$, $ab:1$, $at:3$, $bt:3$. The flow
$f(sa)=3$, $f(sb)=2$, $f(ab)=0$, $f(at)=3$, $f(bt)=2$ is proposed. Verify feasibility, compute $\lvert f\rvert$,
augment it to a maximum flow, and exhibit a cut certifying optimality.

**11.** *(§7.9)* For the network with arcs $sa:3$, $sb:1$, $ab:2$, $at:1$, $bt:3$, list the capacity of
every $s$–$t$ cut, then find the maximum flow and check that it equals the minimum cut.

**12.** *(§7.1–7.6)* Decide true or false, with a one-line justification:
(a) every maximal matching is maximum; (b) every perfect matching is maximum; (c) a graph with a perfect
matching has an even number of vertices; (d) $\alpha'(G)=n/2$ implies $G$ is connected; (e) Hall's
condition with respect to $A$ implies Hall's condition with respect to $B$.

## Intermediate

**13.** *(§7.1)* Prove that if $G$ has a perfect matching then every connected component of $G$ has even
order. Show that the converse fails, even for trees.

**14.** *(§7.4)* Let $G$ be bipartite with $\lvert A\rvert=\lvert B\rvert=n$ and minimum degree
$\delta(G)\ge n/2$. Prove that $G$ has a perfect matching.

**15.** *(§7.5)* Prove that
$$\alpha'(G)=\min_{S\subseteq A}\bigl(\lvert A\rvert-\lvert S\rvert+\lvert N(S)\rvert\bigr)$$
for every bipartite graph, and check the formula on the graph of Problem 6.

**16.** *(§7.5)* Prove that a $k$-regular bipartite graph with $k\ge1$ has at least $k$ perfect matchings,
and that every edge of it lies in some perfect matching.

**17.** *(§7.9)* Deduce König's theorem from the max-flow min-cut theorem by building the unit-capacity
network of Remark 7.9.3 and interpreting a minimum cut.

**18.** *(§7.7)* Solve the assignment problem with cost matrix
$$\begin{pmatrix}5&9&1\\10&3&2\\8&7&4\end{pmatrix}$$
by the Hungarian algorithm, and exhibit optimal dual potentials $u,v$ with $\sum u_i+\sum v_j$ equal to
the optimal cost.

**19.** *(§7.7)* Prove that adding a constant $c$ to every entry of one row (or one column) of a cost
matrix does not change the set of optimal assignments.

**20.** *(§7.10)* Prove that every integral feasible flow in a network can be written as a sum of flows
along $s$–$t$ paths plus flows around directed cycles, all with non-negative integer values.

**21.** *(§7.9)* For the network with arcs $sa:3$, $sb:2$, $ab:1$, $at:2$, $bt:3$, find a maximum flow and
a minimum cut, and verify the two numbers agree.

**22.** *(§7.10)* Prove that the bound "at most $\lvert f^*\rvert$ augmentations" of Theorem 7.10.2 is
attained: for every $k\ge1$ construct a network with integer capacities on which Ford–Fulkerson performs
exactly $k$ augmentations, with $k$ equal to the maximum flow value.

**23.** *(§7.9)* In the network with arcs $sa:3$, $sb:2$, $at:3$, $bt:1$, $ab:2$, compute the maximum flow,
then determine the minimum cut by residual reachability, and confirm that both have value $4$.

**24.** *(§7.4)* Four jobs must be assigned to machines, at most one job per machine. Job $J_1$ can run
only on $M_1$; $J_2$ on $M_1$ or $M_2$; $J_3$ only on $M_2$; $J_4$ on $M_2$ or $M_3$. Find the maximum
number of jobs that can run, and identify a deficient set of jobs.

## Advanced

**25.** *(§7.5)* Prove that a bipartite graph has a matching with at least $k$ edges if and only if
$$\lvert N(S)\rvert\ge\lvert S\rvert-(\lvert A\rvert-k)\qquad\text{for every } S\subseteq A.$$

**26.** *(§7.6)* Prove that $\tau(G)\le2\alpha'(G)$ for every graph, and show that the ratio $2$ is
attained by a disjoint union of triangles. Explain why the bound cannot be improved by a constant
independent of the graph.

**27.** *(§7.9, §7.10)* Prove the edge version of Menger's theorem: the maximum number of pairwise
arc-disjoint $s$–$t$ paths in a directed graph equals the minimum number of arcs whose deletion destroys
all $s$–$t$ paths.

**28.** *(§7.11)* Show that Edmonds–Karp, applied to the bipartite-matching network of Remark 7.9.3 on a
bipartite graph with sides of size $n$ and $m$ edges, performs at most $n$ augmentations and therefore
runs in $O\bigl(n(m+n)\bigr)$ time. Explain how its augmenting paths correspond to those of Algorithm
7.3.1, and why the general bound $O(VE^2)$ is much weaker here.

**29.** *(§5.4, §12.2)* For the transportation problem with supplies $a_1,\dots,a_p$, demands $b_1,\dots,b_q$ and
$\sum a_i=\sum b_j$, (a) construct a feasible solution; (b) prove that a feasible solution with more than
$p+q-1$ positive entries cannot be a vertex of the feasible polytope.

**30.** *(§7.1)* Let $G$ be bipartite with a $0/1$ adjacency matrix $M$ (rows $A$, columns $B$). Prove
that the number of perfect matchings of $G$ equals the permanent $\operatorname{per}(M)=\sum_\sigma\prod_i m_{i,\sigma(i)}$.
Explain why this does not give a polynomial algorithm for counting, while Hall's theorem gives one for
deciding existence.

**31.** *(§7.7)* State and prove the complementary-slackness criterion for the assignment problem: a
permutation $\sigma$ and dual-feasible potentials $(u,v)$ are jointly optimal if and only if every edge
$i\sigma(i)$ is tight.

## Challenge

**32.** *(§7.9)* Derive Hall's theorem from the max-flow min-cut theorem: build the unit-capacity
network, assume the maximum flow is less than $\lvert A\rvert$, and show that a minimum cut yields a
deficient set $S\subseteq A$.

**33.** *(§7.1)* Prove that the number of perfect matchings of $K_{n,n}$ that avoid a fixed perfect
matching is the number of derangements $D_n=n!\sum_{k=0}^{n}(-1)^k/k!$, and evaluate it for $n=3,4$.

**34.** *(§7.2)* Prove that if a bipartite graph has a unique perfect matching, then that matching
contains a bridge of the graph.

**35.** *(§7.9)* Prove the vertex version of Menger's theorem for non-adjacent $s,t$: the maximum number
of pairwise internally vertex-disjoint $s$–$t$ paths equals the minimum size of a set $X\subseteq V\setminus\{s,t\}$
whose deletion separates $s$ from $t$. (Hint: split every vertex $v\notin\{s,t\}$ into $v^-\to v^+$ of
capacity $1$.)

**36.** *(§7.5)* Prove the $0/1$ case of the Birkhoff–von Neumann theorem: if an $n\times n$ matrix $M$
has entries in $\{0,1\}$ and every row and column sum equals $k$, then $M$ is a sum of $k$ permutation
matrices.
