# Extremal Combinatorics — Exercises

> [Extremal Combinatorics](README.md) · 36 problems · Beginner → Challenge · Solutions: [solutions.md](solutions.md)

Attempt every problem in writing before looking at [solutions.md](solutions.md). Each problem names the section of the tutorial that supplies the technique.

Notation: $\operatorname{ex}(n,H)$ is the maximum number of edges in an $n$-vertex graph containing no subgraph isomorphic to $H$; $T_r(n)$ is the Turán graph and $t_r(n) = e(T_r(n))$; $R(r,s)$ is the Ramsey number; $[n] = \{1,\dots,n\}$ and $2^{[n]}$ is the power set; a family is **intersecting** if any two members meet. Graphs are simple and undirected.

Unless a problem says otherwise, an extremal statement must be justified in both directions: an upper bound for all graphs, and an example attaining (or nearly attaining) it.

## Beginner

**1.** *(§7.2)* Use Mantel's theorem to compute $\operatorname{ex}(4,K_3)$, and exhibit a $4$-vertex triangle-free graph attaining it.

**2.** *(§7.2)* Compute $t_2(6)$ and $t_3(6)$ from the part sizes, and verify each by subtracting $\sum_i\binom{n_i}{2}$ from $\binom62$.

**3.** *(§7.2)* Compute $t_3(7)$ from the closed formula $t_r(n) = \left(1-\frac1r\right)\frac{n^2}{2} - \frac{s(r-s)}{2r}$ and directly from the parts of $T_3(7)$.

**4.** *(§7.2)* State Mantel's theorem precisely and use it to bound the number of edges of a triangle-free graph on $12$ vertices.

**5.** *(§7.3)* Compute $R(2,5)$ and justify both the upper and the lower bound.

**6.** *(§7.3)* Exhibit a two-colouring of $K_5$ with no monochromatic triangle, and verify that both colour classes are $5$-cycles.

**7.** *(§5.1)* Explain why $\operatorname{ex}(n,K_2) = 0$, and why $\operatorname{ex}(n,H) = \binom n2$ whenever $H$ has more than $n$ vertices.

**8.** *(§7.2)* Show that $K_{3,3}$ is triangle-free with $9$ edges, and deduce $\operatorname{ex}(6,K_3) = 9$.

**9.** *(§7.2)* Prove that the Turán graph $T_r(n)$ contains no $K_{r+1}$.

**10.** *(§7.2)* Use the degree form of Turán's theorem to show that every $K_4$-free graph on $9$ vertices has a vertex of degree at most $6$, and check that $T_3(9)$ attains this.

**11.** *(§7.5)* State Sperner's theorem for $n = 3$ and list an extremal antichain. What is the largest antichain containing $\{1\}$?

**12.** *(§7.6)* State the Erdős–Ko–Rado bound for $n = 5$, $k = 2$, exhibit a star attaining it, and check that the hypothesis $n \ge 2k$ holds.

## Intermediate

**13.** *(§7.3)* Describe the colouring of $K_8$ that proves $R(3,4) > 8$, verify that the red graph has $12$ edges and no triangle, and verify that the blue graph has no $K_4$.

**14.** *(§7.3)* Prove $R(3,4) \le 9$, stating clearly where the handshake lemma and the value $R(3,3) = 6$ are used.

**15.** *(§7.3)* Use the Erdős–Szekeres bound to bound $R(3,5)$ and $R(4,4)$ from above, and compare with the exact values $14$ and $18$.

**16.** *(§7.3)* Prove the recursion $R(r,s) \le R(r-1,s) + R(r,s-1)$ for $r,s \ge 2$.

**17.** *(§7.5)* Compute the LYM sum for (a) the family of all $3$-subsets of $[6]$ and (b) the star at $1$ inside $\binom{[6]}{3}$. What does LYM conclude in each case?

**18.** *(§7.6)* Prove directly that an intersecting family of $2$-subsets of $[n]$ has at most $n-1$ members for $n \ge 4$.

**19.** *(§7.7)* Give a bipartite graph with $\lvert A\rvert = 3$, $\lvert B\rvert = 2$ for which Hall's condition fails, compute the defect $\max_S(\lvert S\rvert - \lvert N(S)\rvert)$, and check the defect formula.

**20.** *(§7.7)* Prove that a $k$-regular bipartite graph with $k \ge 1$ has parts of equal size and a perfect matching.

**21.** *(§7.4)* Show that there is a two-colouring of $K_{15}$ with no monochromatic $K_6$, by evaluating the union bound.

**22.** *(§7.4)* Use the alteration method of Theorem 7.15 to guarantee a triangle-free graph on $64$ vertices with at least a stated number of edges, and compare with Mantel's exact value.

**23.** *(§7.2)* Compute $\operatorname{ex}(9,K_3)$ and $\operatorname{ex}(9,K_4)$, and describe the extremal graphs.

**24.** *(§7.2)* Prove that $T_r(n)$ is the unique complete $r$-partite graph on $n$ vertices with $t_r(n)$ edges.

## Advanced

**25.** *(§7.2)* Prove Mantel's theorem by the degree-sum argument, including the use of Cauchy–Schwarz and the passage from $m \le n^2/4$ to $m \le \lfloor n^2/4\rfloor$.

**26.** *(§7.2)* Deduce from Turán's theorem that $\operatorname{ex}(n,K_4) = t_3(n)$, and compute $\operatorname{ex}(7,K_4)$ and $\operatorname{ex}(10,K_4)$.

**27.** *(§7.3)* Prove the Erdős–Szekeres bound $R(r,s) \le \binom{r+s-2}{r-1}$ by induction, including the base cases.

**28.** *(§7.4)* Prove carefully that $R(k,k) > 2^{k/2}$ for $k \ge 3$, justifying every inequality, including $\binom nk \le n^k/k!$ and $2^{1+k/2} < k!$.

**29.** *(§7.6)* Prove Katona's lemma: in a cyclic order of $n \ge 2k$ elements, a family of pairwise intersecting intervals of length $k$ has at most $k$ members.

**30.** *(§7.5)* Prove the LYM inequality and deduce Sperner's theorem from it, explaining why the deduction is not an equivalence.

**31.** *(§7.7)* Prove the defect form of Hall's theorem from Hall's theorem itself.

**32.** *(§7.7)* Prove that a $k$-regular bipartite graph decomposes into $k$ perfect matchings.

## Challenge

**33.** *(§7.3)* Prove $R(4,4) \le 18$ using the recursion and the exact value $R(3,4) = 9$. (The true value is $18$; the lower bound is not asked for.)

**34.** *(§7.4)* Prove in full that for $n \ge 3$ there is a triangle-free graph on $n$ vertices with at least $\frac13 n^{3/2} - \frac12\sqrt n$ edges, and evaluate the bound at $n = 10^4$.

**35.** *(§7.6)* Prove the Erdős–Ko–Rado theorem for $n \ge 2k$ by Katona's circle method, including the expectation computation and the use of the interval lemma.

**36.** *(§7.2, §5.1)* Prove that $\operatorname{ex}(n,C_4) \le \frac n4\left(1+\sqrt{4n-3}\right)$, by counting pairs of vertices with a common neighbour and applying convexity. Deduce $\operatorname{ex}(n,C_4) = O(n^{3/2})$.
