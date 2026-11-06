# Algorithms and Complexity — Exercises

> [Algorithms and Complexity](README.md) · 36 problems · Beginner → Challenge · Solutions: [solutions.md](solutions.md)

Attempt every problem in writing before consulting [solutions.md](solutions.md). Each problem names the tutorial section that supplies the method. Unless stated otherwise, $\lg$ means $\log_2$, $n$ is the input size, $T(n)$ is a worst-case running time, and graph problems refer to the RAM model of Section 5.1 with adjacency lists.

Useful conventions: $H_n = \sum_{k=1}^{n} 1/k$; a *clique* is a set of pairwise adjacent vertices; an *independent set* is a set of pairwise non-adjacent vertices; a *vertex cover* is a set of vertices meeting every edge; $\mathrm{SAT}$ is satisfiability of CNF formulas and $\mathrm{3SAT}$ its restriction to three literals per clause.

## Beginner

**1.** *(§7.3, §8.1)* Prove from Definition 5.3 that $f(n) = 4n^2 + 7n + 3$ is $O(n^2)$, giving explicit values of $c$ and $n_0$. Then find the smallest $n_0$ that works with $c = 7$.

**2.** *(§7.3, §8.1)* Prove from the definition that $g(n) = 2n^3 - 5n + 1$ is $\Omega(n^3)$. State the witnesses and check the inequality at $n = 1, 2, 3$.

**3.** *(§7.3, §8.1)* Prove that $h(n) = 7n + 4$ is $\Theta(n)$ by exhibiting both constants, and explain why $7n + 4$ is not $\Theta(n^2)$.

**4.** *(§7.3, §9.2)* Decide whether each statement is true or false, justifying each answer in one line.
(a) $n^2 + 3n = O(n^2)$;
(b) $5n^3 = O(n^2)$;
(c) $n\lg n = \Omega(n)$;
(d) $2^n = O(3^n)$;
(e) $n! = O(2^n)$;
(f) $\lg(n^2) = \Theta(\lg n)$.

**5.** *(§7.4)* Give the exact number of executions of the innermost statement and its $\Theta$ class.

```
s = 0
for i = 1 to n:
    for j = 1 to i:
        s = s + 1
```

**6.** *(§7.6, §9.3)* Sort $A = [3,1,4,6,5,9,2]$ by insertion sort. Record the array after each outer iteration, count the comparisons, and compare the count with the worst-case bound $n(n-1)/2$.

**7.** *(§7.7, §9.4)* On the sorted array $A = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29]$ (fifteen elements), trace binary search for $1$, for $29$, and for $8$. Count the comparisons in each case and compare with $\lfloor\lg n\rfloor + 1$.

**8.** *(§7.6, §9.5)* Sort $A = [8,3,7,1]$ by merge sort. Show the recursion tree, count comparisons exactly, and verify the count against $n\lg n - n + 1$.

**9.** *(§7.6)* Complete the table for insertion sort, merge sort and quicksort with the best, average and worst-case comparison counts and the extra space used. One entry per cell, using $\Theta$ notation except where an exact count is requested.

| Algorithm | Best | Average | Worst | Extra space | Stable |
|---|---|---|---|---|---|
| Insertion sort | | | | | |
| Merge sort | | | | | |
| Quicksort | | | | | |

**10.** *(§7.2)* The following loop is meant to compute the maximum of $A[1..n]$.

```
m = A[1]
for i = 2 to n:
    if A[i] > m:
        m = A[i]
```

State a loop invariant, prove initialisation, maintenance and termination, and conclude that $m = \max(A[1..n])$ at the end.

**11.** *(§8.4)* Prove that $\lg(n!) \le n\lg n$ for every $n \ge 1$ and that $\lg(n!) \ge \frac{n}{2}\lg\frac{n}{2}$ for every $n \ge 2$. Deduce $\lg(n!) = \Theta(n\lg n)$.

**12.** *(§7.10, §5.5–5.9)* Define $\mathrm{P}$, $\mathrm{NP}$, $\mathrm{NP}$-hard and $\mathrm{NP}$-complete in one sentence each, and place each of the following in the appropriate class or classes: sorting, $\mathrm{CLIQUE}$, the halting problem, integer factorisation.

## Intermediate

**13.** *(§7.3, §8.1)* Show that $3n^2 + 2n = \Theta(n^2)$ twice: once with the limit test and once by constructing witnesses by hand. Explain why the limit test does not by itself establish the lower bound for a *negated* statement.

**14.** *(§8.4)* Prove that $2^{2n+1} = O(4^n)$ but $2^{2n} \ne O(2^n)$.

**15.** *(§8.1)* Prove that $\log_{10} n = \Theta(\ln n)$. What does this imply about the base of logarithms in complexity statements?

**16.** *(§7.4)* Determine the exact number of additions performed by

```
for i = 1 to n:
    for j = 1 to i:
        for k = 1 to j:
            x = x + 1
```

and give the $\Theta$ class.

**17.** *(§7.6)* Let $A$ be a uniformly random permutation of $n$ distinct keys. Show that the expected number of inversions is $n(n-1)/4$, and explain why this makes insertion sort $\Theta(n^2)$ on average.

**18.** *(§7.6, §8.7)* Apply quicksort with the last element as pivot to the reverse-sorted array $[6,5,4,3,2,1]$. Show the partition at each step and count the comparisons. Verify the total against $n(n-1)/2$.

**19.** *(§7.5, §8.6)* Solve the recurrence $T(n) = 2T(n/2) + n - 1$ with $T(1) = 0$ for $n = 2^k$ by the substitution method (divide by $n$ and telescope). Check the answer at $n = 4$ and $n = 8$.

**20.** *(§7.9)* A graph has $V = 5000$ vertices and $E = 20000$ edges. Compare the operation counts of Dijkstra's algorithm with an array implementation, $V^2$, and with a binary heap, $(V+E)\lg V$. Which is faster and by what factor? At what edge density $E = \Theta(V^2)$ does the comparison reverse?

**21.** *(§7.9)* Consider the directed graph with vertices $s,a,b$ and edges $s \to a$ (weight $2$), $s \to b$ (weight $5$), $b \to a$ (weight $-4$). Run Dijkstra's algorithm from $s$ and show that it reports the wrong distance for $a$. Then compute the correct distances by Bellman–Ford and list the relaxation order.

**22.** *(§7.9)* For the undirected graph with vertices $\{1,2,3,4,5,6\}$ and edges $\{1\text{–}2,\ 1\text{–}3,\ 2\text{–}4,\ 3\text{–}4,\ 4\text{–}5,\ 5\text{–}6\}$, run BFS from vertex $1$ and give the distance of every vertex. State the time complexity for this graph and how many edge examinations it performs.

**23.** *(§7.2)* Prove the binary-search invariant stated in Section 7.2: if $v$ occurs in $A[1..n]$ then it occurs in $A[lo..hi]$, where the range is empty when $lo = hi+1$. Show that the invariant is maintained when the middle element is smaller than $v$, and that the loop terminates.

**24.** *(§5.8, §8.2)* Prove: if $L_1 \le_{\mathrm{p}} L_2$ and $L_2 \in \mathrm{P}$, then $L_1 \in \mathrm{P}$. Explain why this is the formal content of "a reduction transfers tractability backwards".

## Advanced

**25.** *(§7.8, §8.4)* Give a complete proof that every comparison-based sorting algorithm uses at least $\lceil\lg(n!)\rceil$ comparisons in the worst case. Evaluate the bound for $n = 6$ and compare it with the following procedure: sort each of two triples with three comparisons, then merge the two sorted triples. Explain why the counting argument does not by itself produce an algorithm that attains the bound.

**26.** *(§7.8)* Prove that any comparison-based algorithm that searches for a key in a sorted array of $n$ elements, and must also report correctly when the key is absent, uses at least $\lceil\lg(n+1)\rceil$ comparisons in the worst case. Then prove the $\Omega(n)$ lower bound for searching an unordered array.

**27.** *(§7.6)* Prove that building a binary max-heap from an array of $n$ elements by successive sift-down operations takes $O(n)$ time, not $O(n\lg n)$. Use the bound $\sum_{h\ge0} h/2^{h} = 2$ for the sum of heights.

**28.** *(§8.6)* Prove by induction on $k$ that merge sort performs exactly $n\lg n - n + 1$ comparisons in the worst case when $n = 2^k$, starting from the recurrence $T(n) = 2T(n/2) + n - 1$, $T(1) = 0$.

**29.** *(§7.11)* Prove that $\mathrm{CLIQUE} \le_{\mathrm{p}} \mathrm{VERTEX}$-$\mathrm{COVER}$ by showing that $G$ has a clique of size $k$ if and only if its complement $\overline{G}$ has a vertex cover of size $n - k$. Deduce that $\mathrm{VERTEX}$-$\mathrm{COVER}$ is $\mathrm{NP}$-complete, given that it is in $\mathrm{NP}$.

**30.** *(§5.7, §7.11)* Show that $\mathrm{SUBSET}$-$\mathrm{SUM}$ is in $\mathrm{NP}$ and that $\mathrm{PARTITION} \le_{\mathrm{p}} \mathrm{SUBSET}$-$\mathrm{SUM}$, where $\mathrm{PARTITION}$ asks whether a multiset of positive integers can be split into two parts of equal sum. Handle the case of odd total sum explicitly.

**31.** *(§5.8, §7.10)* Prove that $\mathrm{NP}$ is closed under polynomial-time reductions: if $L' \le_{\mathrm{p}} L$ and $L \in \mathrm{NP}$, then $L' \in \mathrm{NP}$. Then prove that $\mathrm{P}$ is closed under reductions as well.

**32.** *(§7.13)* Prove that the halting problem is not decidable. Then prove that its complement $\overline{H}$ is not recognisable, although $H$ itself is recognisable.

## Challenge

**33.** *(§7.10, §7.11)* Prove that if some $\mathrm{NP}$-complete language belongs to $\mathrm{coNP}$, then $\mathrm{NP} = \mathrm{coNP}$. Explain why this is regarded as evidence that no $\mathrm{NP}$-complete problem lies in $\mathrm{coNP}$.

**34.** *(§7.10, §7.11)* Suppose a polynomial-time decision algorithm $D$ for $\mathrm{SAT}$ is given. Show how to compute, in polynomial time, a satisfying assignment of any satisfiable CNF formula $\varphi$, using only calls to $D$ on formulas derived from $\varphi$. Count the number of calls in terms of the number of variables.

**35.** *(§7.13)* (a) Using Cantor's theorem, prove that some language over $\{0,1\}$ is undecidable. (b) Construct one explicitly by diagonalisation over an enumeration of all programs, and prove that it differs from every decidable language.

**36.** *(§7.11, §7.13)* Prove that the halting problem is $\mathrm{NP}$-hard: for every $L \in \mathrm{NP}$ there is a polynomial-time reduction $L \le_{\mathrm{p}} H$, where $H$ is the halting set. Explain why this does not make $H$ $\mathrm{NP}$-complete.
