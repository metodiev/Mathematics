# Trees — Exercises

> [Trees](README.md) · 36 problems · Beginner → Challenge · Solutions: [solutions.md](solutions.md)

Attempt every problem in writing before looking at [solutions.md](solutions.md). Each problem names the section of the tutorial that supplies the technique, so a stuck reader knows where to reread.

Notation: $T$ is a finite simple tree unless stated otherwise, $n = \lvert V(T)\rvert$, $m = \lvert E(T)\rvert$, $n_k$ is the number of vertices of degree $k$, and $L = n_1$ is the number of leaves. In a rooted tree, depth means distance from the root. A Prüfer code is written as a word in parentheses.

## Beginner

**1.** *(§7.2, §7.3)* (a) A tree has $17$ vertices. How many edges?
(b) A tree has $30$ edges. How many vertices?
(c) A forest has $20$ vertices and $6$ components. How many edges?

**2.** *(§7.2)* Decide whether each graph is a tree, justifying the answer with an edge count and a connectivity or acyclicity check:
(a) $V=\{1,\dots,6\}$, $E=\{12,23,34,45,56\}$;
(b) $V=\{1,\dots,6\}$, $E=\{12,23,34,45,56,61\}$;
(c) $V=\{1,\dots,6\}$, $E=\{12,13,14,15,16\}$;
(d) $V=\{1,\dots,6\}$, $E=\{12,13,24,35,46\}$;
(e) $V=\{1,\dots,6\}$, $E=\{12,13,14,15\}$.

**3.** *(§7.2)* Draw all pairwise non-isomorphic trees on $5$ vertices. How many are there? Confirm that the total number of labelled trees on $5$ vertices, $5^3 = 125$, is the sum of the numbers of labellings of your shapes.

**4.** *(§7.9)* Verify Cayley's formula for $n = 4$ by classifying the $16$ labelled trees on $\{1,2,3,4\}$ into stars and paths and counting each class directly.

**5.** *(§7.9)* Compute the Prüfer code of the tree with $V = \{1,\dots,8\}$ and
$$E = \{12,\ 13,\ 14,\ 25,\ 26,\ 37,\ 48\}.$$

**6.** *(§7.9)* Decode the Prüfer code $P = (5,3,1,3,5)$ for $n = 7$: list the edges of the tree, compute its degrees, and verify them against Lemma 7.9.2.

**7.** *(§5.2)* For the rooted tree with root $1$, $V=\{1,\dots,8\}$ and $E=\{12,13,24,25,36,47,48\}$, list the parent of every non-root vertex, the children of every vertex, the leaves, the depth of every vertex and the height.

**8.** *(§7.4)* (a) A full binary tree has $8$ internal vertices. How many leaves and how many vertices does it have in total?
(b) A full binary tree has $21$ vertices. How many leaves and how many internal vertices does it have?

**9.** *(§7.4)* (a) What is the maximum number of leaves of a binary tree of height $4$?
(b) What is the maximum number of vertices of a binary tree of height $4$?
(c) What is the minimum possible height of a binary tree with $20$ vertices?

**10.** *(§7.5)* How many spanning trees does each of $P_4$, $K_3$ and $C_5$ have? Explain each count.

**11.** *(§7.7)* Run Kruskal's algorithm on the weighted graph with $V=\{1,\dots,5\}$ and edges
$$12:2,\quad 13:7,\quad 14:4,\quad 23:3,\quad 24:6,\quad 25:1,\quad 34:5,\quad 35:8 .$$
Show the sorted order, the decisions, the final tree and its weight.

**12.** *(§7.8)* Run Prim's algorithm from vertex $3$ on the graph of Problem 11. Compare the result with Kruskal's output and explain why the two must agree here.

## Intermediate

**13.** *(§7.2)* Prove that if $T$ is a tree with $n \ge 2$ vertices and $\ell$ is a leaf, then $T - \ell$ is a tree on $n-1$ vertices.

**14.** *(§7.2)* Prove that a connected graph on $n$ vertices with exactly $n-1$ edges is acyclic, using the fact that a connected graph has at least $n-1$ edges.

**15.** *(§7.3)* Prove that in a tree with $n \ge 2$ vertices,
$$n_1 = 2 + \sum_{k\ge3}(k-2)\,n_k .$$
Then construct a tree with $n_4 = 1$, $n_3 = 1$, $n_2 = 2$ and check the identity.

**16.** *(§7.2)* Prove that $G$ is a tree if and only if there is exactly one simple path between every pair of distinct vertices.

**17.** *(§7.2)* Prove that if $T$ is a tree and $u,v$ are non-adjacent vertices of $T$, then $T + uv$ contains exactly one cycle.

**18.** *(§7.5)* Prove that every connected graph has a spanning tree, and deduce that a connected graph on $n$ vertices has at least $n-1$ edges.

**19.** *(§7.6)* Prove that if $e$ is a lightest edge incident with a vertex $v$, then some minimum spanning tree contains $e$. Then give an example of a weighted graph with two different minimum spanning trees.

**20.** *(§7.6)* Prove that a connected weighted graph whose edge weights are pairwise distinct has a unique minimum spanning tree.

**21.** *(§7.6, §9)* For the weighted graph with $V=\{1,\dots,6\}$ and
$$13:1,\quad 24:2,\quad 35:3,\quad 46:4,\quad 12:5,\quad 26:6,\quad 34:7,\quad 45:8,\quad 56:9,$$
find a minimum spanning tree and verify it using the local optimality criterion of Example 9.8: every tree edge must be a lightest edge across the cut determined by deleting it.

**22.** *(§7.5)* Prove that the cycle $C_n$ has exactly $n$ spanning trees, and use the same idea to count the spanning trees of $K_{2,3}$ (which has $5$ vertices and $6$ edges).

## Advanced

**23.** *(§7.8)* Prove that Prim's algorithm returns a minimum spanning tree. State carefully where the cut property is used.

**24.** *(§7.6)* Prove the cycle property: if $e$ is an edge of a cycle $C$ whose weight is strictly greater than the weight of every other edge of $C$, then no minimum spanning tree contains $e$.

**25.** *(§7.9)* Using Prüfer codes, prove that the number of labelled trees on $\{1,\dots,n\}$ with prescribed degrees $d_1,\dots,d_n$ (all positive, summing to $2n-2$) is
$$\frac{(n-2)!}{\prod_{i=1}^{n}(d_i-1)!}.$$

**26.** *(§7.9)* Deduce Cayley's formula $n^{n-2}$ from Problem 25 by summing over all degree sequences and applying the multinomial theorem.

**27.** *(§7.8, §5.2)* Prove that every tree is bipartite and that its bipartition is unique up to interchanging the two parts.

**28.** *(§7.2)* Prove that a connected graph $G$ is a tree if and only if every edge of $G$ is a bridge.

**29.** *(§7.6)* A **minimum bottleneck spanning tree** is a spanning tree whose largest edge weight is as small as possible, with no condition on the total weight. Prove that every minimum spanning tree is a minimum bottleneck spanning tree, and give an example of a minimum bottleneck spanning tree that is not a minimum spanning tree.

**30.** *(§7.5)* Prove that if $T_1$ and $T_2$ are two spanning trees of the same connected graph, then there is a sequence of spanning trees
$$T_1 = S_0,\ S_1,\ \dots,\ S_r = T_2$$
such that each $S_{i+1}$ is obtained from $S_i$ by deleting one edge and adding one edge.

## Challenge

**31.** *(§7.9)* Prove that the number of labelled trees on $\{1,\dots,n\}$ with maximum degree at most $2$ is $n!/2$ for $n \ge 2$, and check the formula for $n = 4$.

**32.** *(§7.9)* Prove that the expected number of leaves of a uniformly random labelled tree on $n$ vertices is
$$n\left(\frac{n-1}{n}\right)^{n-2},$$
and check the value for $n = 4$ and $n = 5$ against a direct enumeration.

**33.** *(§7.9)* Prove that a sequence $d_1,\dots,d_n$ of positive integers with $\sum_i d_i = 2n-2$ is the degree sequence of some tree. Construct a tree on $6$ vertices with degree sequence $(3,2,2,1,1,1)$ by writing down a Prüfer code and decoding it.

**34.** *(§7.3)* Prove that a tree with $n \ge 2$ vertices has at least $\Delta(T)$ leaves, and determine when equality holds.

**35.** *(§7.9)* Prove that for every word $P$ of length $n-2$ over $\{1,\dots,n\}$, the decoder of Algorithm 7.9.4 produces a tree whose Prüfer code is $P$. (This is Lemma 7.9.5(b); write out the induction in full.)

**36.** *(§7.9)* Prove that, for $n \ge 3$, the number of labelled trees on $\{1,\dots,n\}$ that contain the edge $12$ is $2n^{\,n-3}$.
