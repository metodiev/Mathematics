# Algorithms and Complexity — Solutions

> [Algorithms and Complexity](README.md) · Solutions to the 36 problems in [exercises.md](exercises.md)

Each solution names the strategy, carries out the steps and checks the answer — numerically for counting problems, against the definition for asymptotic ones, and against the hypotheses for reductions. Theorem numbers refer to the tutorial.

## Beginner

**1.** *Strategy: bound every term by a multiple of the dominant one, then solve a quadratic for the sharp constant.*

*Upper bound with witnesses.* For $n \ge 1$ we have $7n \le 7n^2$ and $3 \le 3n^2$, so

$$f(n) = 4n^2 + 7n + 3 \le 4n^2 + 7n^2 + 3n^2 = 14n^2.$$

Thus $f = O(n^2)$ with $c = 14$, $n_0 = 1$.

*Sharp constant.* With $c = 7$ the requirement is $4n^2 + 7n + 3 \le 7n^2$, i.e. $3n^2 - 7n - 3 \ge 0$. The positive root of $3x^2 - 7x - 3$ is $\frac{7+\sqrt{49+36}}{6} = \frac{7+\sqrt{85}}{6} \approx 2.703$. Check the two integers around it: at $n = 2$, $f(2) = 16 + 14 + 3 = 33$ and $7n^2 = 28$, so the inequality fails; at $n = 3$, $f(3) = 36 + 21 + 3 = 60$ and $7n^2 = 63$, so it holds. Hence $n_0 = 3$ is the smallest valid choice.

**2.** *Strategy: show the negative term is dominated by the cubic term once $n$ is large enough.*

We want $2n^3 - 5n + 1 \ge c\,n^3$ for all $n \ge n_0$. Take $c = 1$; the inequality becomes $n^3 - 5n + 1 \ge 0$.

| $n$ | $2n^3 - 5n + 1$ | $n^3$ | inequality |
|---|---|---|---|
| 1 | $-2$ | 1 | fails |
| 2 | $16 - 10 + 1 = 7$ | 8 | fails |
| 3 | $54 - 15 + 1 = 40$ | 27 | holds |

For $n \ge 2$ the function $n^3 - 5n + 1$ has derivative $3n^2 - 5 > 0$, so it is increasing from $n = 2$ onwards; since it is already $13 > 0$ at $n = 3$, it stays positive. Hence $2n^3 - 5n + 1 \ge n^3$ for all $n \ge 3$: witnesses $c = 1$, $n_0 = 3$.

*Remark.* The value at $n = 1$ is negative, which is allowed: the definition of $\Omega$ only constrains $n \ge n_0$.

**3.** *Strategy: two inequalities, one for the upper and one for the lower bound.*

For $n \ge 1$: $7n + 4 \le 7n + 4n = 11n$, so $h = O(n)$ with $c = 11$. Also $7n + 4 \ge 7n$, so $h = \Omega(n)$ with $c = 7$. Therefore $h = \Theta(n)$.

*Why not $\Theta(n^2)$?* $\dfrac{7n+4}{n^2} = \dfrac{7}{n} + \dfrac{4}{n^2} \to 0$, so for every $c > 0$ and every $n_0$ there is an $n \ge n_0$ with $7n + 4 < c\,n^2$; that is, $h = o(n^2)$ and in particular not $\Omega(n^2)$.

**4.** *(a)* True: $n^2 + 3n \le 4n^2$ for $n \ge 1$, so $c = 4$, $n_0 = 1$.

*(b)* False: $\dfrac{5n^3}{n^2} = 5n \to \infty$, so $5n^3 = \omega(n^2)$.

*(c)* True: for $n \ge 2$, $n\lg n \ge n$ since $\lg n \ge 1$; so $c = 1$, $n_0 = 2$.

*(d)* True: $2^n \le 3^n$ for all $n \ge 0$; $c = 1$, $n_0 = 1$.

*(e)* False: $\dfrac{n!}{2^n} = \prod_{k=1}^{n}\dfrac{k}{2} \ge \dfrac34\cdot 2^{n-3} \to \infty$ (Theorem 8.4), so $2^n = o(n!)$.

*(f)* True: $\lg(n^2) = 2\lg n$, so $c_1 = 2$ and $c_2 = 2$ give the two inequalities; alternatively $\lg(n^2)/\lg n = 2$.

**5.** *Strategy: the inner loop runs $i$ times, so sum $i$ over $i = 1,\dots,n$.*

The innermost statement executes

$$\sum_{i=1}^{n} i = \frac{n(n+1)}{2}$$

times. Check: $n = 1$ gives $1$; $n = 2$ gives $1 + 2 = 3 = 2\cdot3/2$; $n = 3$ gives $1+2+3 = 6 = 3\cdot4/2$. Since $\frac{n(n+1)}{2} = \Theta(n^2)$, the loop is quadratic.

*Remark.* The total is $\binom{n+1}{2}$, the number of unordered pairs from a set of $n+1$ objects, which is a useful sanity check.

**6.** *Strategy: run the inner loop literally, counting one comparison per array element examined until the scan stops.*

The worst-case bound is $n(n-1)/2 = 7\cdot6/2 = 21$.

| $i$ | key | comparisons | array afterwards |
|---|---|---|---|
| 2 | 1 | 1 (3 > 1, then $j = 0$) | $[1,3,4,6,5,9,2]$ |
| 3 | 4 | 1 (3 ≤ 4 stops) | $[1,3,4,6,5,9,2]$ |
| 4 | 6 | 1 (4 ≤ 6 stops) | $[1,3,4,6,5,9,2]$ |
| 5 | 5 | 2 (6 > 5; 4 ≤ 5 stops) | $[1,3,4,5,6,9,2]$ |
| 6 | 9 | 1 (6 ≤ 9 stops) | $[1,3,4,5,6,9,2]$ |
| 7 | 2 | 6 (9, 6, 5, 4, 3 all exceed 2; 1 ≤ 2 stops) | $[1,2,3,4,5,6,9]$ |

Total: $1 + 1 + 1 + 2 + 1 + 6 = 12$ comparisons, well below $21$.

*Consistency check.* The input has $7$ inversions — $(3,1)$, $(3,2)$, $(4,2)$, $(6,5)$, $(6,2)$, $(5,2)$, $(9,2)$ — and every successful comparison corresponds to one inversion, so there are $7$ successful comparisons. The remaining $12 - 7 = 5$ comparisons are the failing ones that stop the scan, at iterations $i = 3,4,5,6,7$. Iteration $i = 2$ hit $j = 0$ and made no failing comparison, which is why the count is $7 + 5 = 12$.

**7.** *Strategy: maintain the half-open range that can still contain the key.*

Here $n = 15$, so $\lfloor\lg 15\rfloor + 1 = 3 + 1 = 4$ comparisons is the bound.

*Searching for $1$:* mid $= 8$ ($A[8] = 15 > 1$, so $hi = 7$); mid $= 4$ ($A[4] = 7 > 1$, so $hi = 3$); mid $= 2$ ($A[2] = 3 > 1$, so $hi = 1$); mid $= 1$ ($A[1] = 1$, found). Four comparisons.

*Searching for $29$:* mid $= 8$ ($15 < 29$, so $lo = 9$); mid $= 12$ ($A[12] = 23 < 29$, so $lo = 13$); mid $= 14$ ($A[14] = 27 < 29$, so $lo = 15$); mid $= 15$ ($A[15] = 29$, found). Four comparisons.

*Searching for $8$:* mid $= 8$ ($15 > 8$, so $hi = 7$); mid $= 4$ ($7 < 8$, so $lo = 5$); mid $= 6$ ($11 > 8$, so $hi = 5$); mid $= 5$ ($9 > 8$, so $hi = 4$); now $lo = 5 > hi = 4$ and the algorithm reports absence. Four comparisons.

Every query uses at most four comparisons, matching $\lfloor\lg 15\rfloor + 1 = 4$.

**8.** *Strategy: count the comparisons of each merge separately and add.*

*Recursion tree.* Level 0: $[8,3,7,1]$. Level 1: $[8,3]$ and $[7,1]$. Level 2: singletons.

*Base sorts.* $[8,3]$ costs one comparison ($8 > 3$) and gives $[3,8]$; $[7,1]$ costs one comparison ($7 > 1$) and gives $[1,7]$.

*Top merge.* Compare $3$ with $1$ (emit $1$); compare $3$ with $7$ (emit $3$); compare $8$ with $7$ (emit $7$); copy the remaining $8$. Three comparisons.

Total $1 + 1 + 3 = 5$, and $n\lg n - n + 1 = 4\cdot2 - 4 + 1 = 5$.

*Check the bound.* The level argument gives $n\lceil\lg n\rceil = 4\cdot2 = 8$, which is looser; the exact count for a power of two is the sharper $n\lg n - n + 1$.

**9.** Completed table:

| Algorithm | Best | Average | Worst | Extra space | Stable |
|---|---|---|---|---|---|
| Insertion sort | $\Theta(n)$ | $\Theta(n^2)$ | $\Theta(n^2)$ | $\Theta(1)$ | yes |
| Merge sort | $\Theta(n\log n)$ | $\Theta(n\log n)$ | $\Theta(n\log n)$ | $\Theta(n)$ | yes |
| Quicksort | $\Theta(n\log n)$ | $\Theta(n\log n)$ expected | $\Theta(n^2)$ | $\Theta(\log n)$ | no |

*Justifications.* Insertion sort is linear on an already sorted array and quadratic on a reversed one; merge sort's recurrence is the same in all cases; quicksort's worst case is a maximally unbalanced partition and its balanced case is optimal up to the leading constant. Quicksort's stack depth is $\Theta(\log n)$ when partitions are balanced and $\Theta(n)$ in the worst case.

**10.** *Strategy: the invariant must record that every element up to $i-1$ has been examined.*

*Invariant.* At the start of iteration $i$ (for $2 \le i \le n+1$),
$$I:\quad m = \max(A[1..i-1]).$$

*Initialisation.* Before the first iteration $i = 2$, and $m = A[1] = \max(A[1..1])$.

*Maintenance.* Suppose $I$ holds before iteration $i \le n$. If $A[i] > m$, the assignment sets $m = A[i] = \max(\max(A[1..i-1]), A[i]) = \max(A[1..i])$. If $A[i] \le m$, then $m \ge A[i]$ and $m = \max(A[1..i-1]) \ge A[i]$, so $m = \max(A[1..i])$. Either way $I$ holds for $i+1$.

*Termination.* The loop ends with $i = n+1$, and $I$ gives $m = \max(A[1..n])$, which is the postcondition. The loop terminates because $i$ increases by one per iteration and is bounded above by $n+1$.

**11.** *Strategy: bound the product term by term.*

*Upper bound.* For $n \ge 1$, every factor satisfies $k \le n$, so
$$\lg(n!) = \sum_{k=1}^{n}\lg k \le \sum_{k=1}^{n}\lg n = n\lg n.$$

*Lower bound.* For $n \ge 2$, all factors with $k \ge \lceil n/2\rceil$ satisfy $k \ge n/2$, and there are $n - \lceil n/2\rceil + 1 \ge n/2$ of them, so
$$\lg(n!) \ge \sum_{k=\lceil n/2\rceil}^{n}\lg\frac{n}{2} \ge \frac{n}{2}\lg\frac{n}{2}.$$

*Conclusion.* The upper bound shows $\lg(n!) = O(n\lg n)$. For $n \ge 4$, $\lg\frac{n}{2} = \lg n - 1 \ge \frac12\lg n$ (because $\lg n \ge 2$), hence $\lg(n!) \ge \frac{n}{4}\lg n = \Omega(n\lg n)$. Therefore $\lg(n!) = \Theta(n\lg n)$.

Check at $n = 4$: $\lg 24 \approx 4.585$, while $n\lg n = 8$ and $\frac n2\lg\frac n2 = 2$ ✓.

**12.** *Definitions.*

* $\mathrm{P}$: languages decidable by a deterministic algorithm in time polynomial in the input length.
* $\mathrm{NP}$: languages $L$ for which some polynomial-time verifier $V$ satisfies $x \in L \iff \exists w\,(|w| \le \mathrm{poly}(|x|),\ V(x,w)=1)$.
* $\mathrm{NP}$-hard: every language in $\mathrm{NP}$ reduces to $L$ in polynomial time.
* $\mathrm{NP}$-complete: $L \in \mathrm{NP}$ and $L$ is $\mathrm{NP}$-hard.

*Placement.*

| Problem | Where it lies |
|---|---|
| sorting | $\mathrm{P}$ (merge sort, $O(n\log n)$) |
| $\mathrm{CLIQUE}$ | $\mathrm{NP}$ and $\mathrm{NP}$-complete (Theorem 7.5), hence also $\mathrm{NP}$-hard |
| halting problem | undecidable, hence outside $\mathrm{NP}$; it is $\mathrm{NP}$-hard (Exercise 36) but not $\mathrm{NP}$-complete |
| integer factorisation | in $\mathrm{NP} \cap \mathrm{coNP}$; not known to lie in $\mathrm{P}$, and believed not $\mathrm{NP}$-complete |

## Intermediate

**13.** *Strategy: compute one limit, then reproduce the same conclusion with explicit inequalities.*

*Limit test.*
$$\lim_{n\to\infty}\frac{3n^2+2n}{n^2} = \lim_{n\to\infty}\left(3 + \frac2n\right) = 3.$$
Since $0 < 3 < \infty$, Theorem 8.1 gives $3n^2 + 2n = \Theta(n^2)$.

*Witnesses.* For $n \ge 1$, $2n \le 2n^2$, so $3n^2 + 2n \le 5n^2$: $c = 5$, $n_0 = 1$. And $3n^2 + 2n \ge 3n^2$: $c = 3$, $n_0 = 1$.

*Why the limit test cannot replace the definition.* Each clause of Theorem 8.1 is an implication from a *limit that exists* to a bound. If $f/g$ oscillates and has no limit, the test says nothing (take $f(n) = 2 + \sin n$, $g \equiv 1$). More importantly, the test is not an equivalence: $f = O(g)$ does not imply that $f/g$ converges. To *disprove* a bound one therefore has to negate the quantified definition and produce, for every proposed $c$ and $n_0$, a witness $n$ — a limit computation is a proof only in the direction in which it applies.

**14.** *Strategy: rewrite both sides with a common base.*

*First claim.* $2^{2n+1} = 2\cdot 2^{2n} = 2\cdot 4^n$, so $2^{2n+1} \le 2\cdot4^n$ for all $n$: witnesses $c = 2$, $n_0 = 1$.

*Second claim.* Suppose $2^{2n} \le c\,2^n$ for all $n \ge n_0$. Dividing by $2^n > 0$ gives $2^n \le c$ for all $n \ge n_0$, which is false because $2^n$ is unbounded. Equivalently $\dfrac{2^{2n}}{2^n} = 2^n \to \infty$, so $2^{2n} = \omega(2^n)$, in particular not $O(2^n)$.

*Moral.* The constants matter inside the exponent: multiplying $n$ by $2$ squares the function, which no constant can compensate.

**15.** *Strategy: change of base is multiplication by a constant.*

$$\log_{10} n = \frac{\ln n}{\ln 10} = \frac{1}{\ln 10}\ln n, \qquad \ln 10 \approx 2.302585.$$

Since $\frac{1}{\ln 10} \approx 0.4343$ is a positive constant, both inequalities $\log_{10} n \le c_2 \ln n$ and $\log_{10} n \ge c_1 \ln n$ hold with $c_1 = c_2 = \frac{1}{\ln 10}$ (for $n \ge 1$). Hence $\log_{10} n = \Theta(\ln n)$.

*Implication.* Changing the base of logarithms multiplies every running time by a constant, and constants are absorbed by $\Theta$. This is why complexity statements can write $\log$ without specifying the base, and why $\lg$ is used only for exact counts (such as $\lfloor \lg n\rfloor + 1$ comparisons in binary search).

**16.** *Strategy: sum over the three nested indices, innermost first.*

For fixed $i$ and $j$ the innermost loop runs $j$ times, so the total is

$$N(n) = \sum_{i=1}^{n}\sum_{j=1}^{i} j = \sum_{i=1}^{n}\frac{i(i+1)}{2}.$$

Using $\sum i^2 = \frac{n(n+1)(2n+1)}{6}$ and $\sum i = \frac{n(n+1)}{2}$,

$$N(n) = \frac12\left(\frac{n(n+1)(2n+1)}{6} + \frac{n(n+1)}{2}\right) = \frac{n(n+1)(2n+1) + 3n(n+1)}{12} = \frac{n(n+1)(2n+4)}{12} = \frac{n(n+1)(n+2)}{6}.$$

Check: $n = 1$ gives $1\cdot2\cdot3/6 = 1$ ✓; $n = 2$ gives $2\cdot3\cdot4/6 = 4$, and directly $1 + (1+2) = 4$ ✓; $n = 3$ gives $3\cdot4\cdot5/6 = 10$, directly $1 + 3 + 6 = 10$ ✓.

The answer is $\binom{n+2}{3} = \Theta(n^3)$.

**17.** *Strategy: linearity of expectation over pairs, with a symmetry argument for each pair.*

Label the keys so that their sorted order is $z_1 < \dots < z_n$, and for $i < j$ let $X_{ij}$ be the indicator that $z_j$ appears before $z_i$ in the random permutation $A$ (an inversion). In a uniformly random permutation the two relative orders of $z_i$ and $z_j$ are equally likely, so $\mathbb{E}[X_{ij}] = \frac12$. Therefore

$$\mathbb{E}[\text{inversions}] = \sum_{1 \le i < j \le n}\mathbb{E}[X_{ij}] = \binom{n}{2}\cdot\frac12 = \frac{n(n-1)}{4}.$$

*Why this gives $\Theta(n^2)$ for insertion sort.* By Theorem 8.5, the number of comparisons is the number of inversions plus the number of iterations in which the inner scan stops on a failed comparison, which is at most $n-1$. Hence

$$\frac{n(n-1)}{4} \le \mathbb{E}[\text{comparisons}] \le \frac{n(n-1)}{4} + (n-1),$$

so the expectation is $\Theta(n^2)$.

**18.** *Strategy: each partition of a reverse-sorted array with a last-element pivot removes exactly one element.*

*Step 1.* $[6,5,4,3,2,1]$, pivot $1$: each of the five other elements is compared with $1$ and is larger, so five comparisons; the pivot moves to the front: $[1,6,5,4,3,2]$.

*Step 2.* On $[6,5,4,3,2]$, pivot $2$: four comparisons, result $[2,6,5,4,3]$.

*Step 3.* On $[6,5,4,3]$, pivot $3$: three comparisons, result $[3,6,5,4]$.

*Step 4.* On $[6,5,4]$, pivot $4$: two comparisons, result $[4,6,5]$.

*Step 5.* On $[6,5]$, pivot $5$: one comparison, result $[5,6]$.

Total: $5 + 4 + 3 + 2 + 1 = 15 = 6\cdot5/2$, exactly the worst-case bound of Theorem 8.7. The subproblem sizes are $6, 5, 4, 3, 2$, so the recurrence $T(m) = T(m-1) + (m-1)$ is realised at every step.

**19.** *Strategy: divide the recurrence by $n$ to make the right-hand side telescope.*

Let $S(k) = T(2^k)/2^k$. Dividing $T(n) = 2T(n/2) + n - 1$ by $n$ gives

$$\frac{T(n)}{n} = \frac{T(n/2)}{n/2} + 1 - \frac1n, \qquad\text{i.e.}\qquad S(k) = S(k-1) + 1 - 2^{-k}.$$

With $S(0) = T(1)/1 = 0$, summing from $j = 1$ to $k$:

$$S(k) = \sum_{j=1}^{k}\left(1 - 2^{-j}\right) = k - \sum_{j=1}^{k}2^{-j} = k - \left(1 - 2^{-k}\right) = k - 1 + 2^{-k}.$$

Therefore

$$T(2^k) = 2^k\left(k - 1 + 2^{-k}\right) = k2^k - 2^k + 1 = n\lg n - n + 1.$$

*Checks.* $T(2) = 1$ and $2\cdot1 - 2 + 1 = 1$ ✓. $T(4) = 2T(2) + 3 = 2 + 3 = 5$ and $4\cdot2 - 4 + 1 = 5$ ✓. $T(8) = 2\cdot5 + 7 = 17$ and $8\cdot3 - 8 + 1 = 17$ ✓.

**20.** *Strategy: evaluate both operation counts numerically and compare.*

$$V^2 = 5000^2 = 2.5\times10^{7}.$$

$$\lg 5000 = \frac{\ln 5000}{\ln 2} \approx \frac{8.5172}{0.6931} \approx 12.29, \qquad (V+E)\lg V = 25\,000\cdot12.29 \approx 3.07\times10^{5}.$$

The heap implementation is faster by a factor $\dfrac{2.5\times10^{7}}{3.07\times10^{5}} \approx 81$.

*When does the comparison reverse?* Set $(V+E)\lg V = V^2$:

$$E \approx \frac{V^2}{\lg V} - V = \frac{2.5\times10^{7}}{12.29} - 5000 \approx 2.03\times10^{6} - 5000 \approx 2.03\times10^{6}.$$

So for graphs denser than about two million edges at $V = 5000$ (density $2E/V^2 \approx 0.16$), the array implementation wins. Asymptotically, if $E = \Theta(V^2)$ then the heap runs in $\Theta(V^2\lg V)$ while the array runs in $\Theta(V^2)$: on dense graphs the array wins, on sparse graphs the heap wins.

**21.** *Strategy: run Dijkstra exactly and watch the settled vertex whose distance should later improve.*

*Dijkstra.* Initialise $d(s) = 0$, $d(a) = 2$, $d(b) = 5$, all other distances infinite.

1. Extract $a$ with $d(a) = 2$. It has no outgoing edge in the example, so nothing is relaxed. $a$ is now finalised.
2. Extract $b$ with $d(b) = 5$. Relaxing $b \to a$ would give $5 - 4 = 1 < 2$, but $a$ is already finalised and is never revisited.

The algorithm reports $d(a) = 2$. The true distance is $1$, via $s \to b \to a$ with cost $5 - 4 = 1$.

*Bellman–Ford.* Initialise $d(s) = 0$, others $\infty$, and relax all edges $V - 1 = 2$ times.

*Pass 1:* $s\to a$ gives $d(a) = 2$; $s\to b$ gives $d(b) = 5$; $b\to a$ gives $\min(2, 5-4) = 1$. So after pass 1, $d = (0, 1, 5)$ if the edges are processed in the order $s\to a, s\to b, b\to a$. If $b\to a$ is processed before $s\to b$, then pass 1 leaves $d(a) = 2$ and pass 2 lowers it to $1$.

*Pass 2:* no change, so the distances are final: $d(s) = 0$, $d(a) = 1$, $d(b) = 5$.

*Moral.* The correctness proof of Dijkstra uses non-negativity to argue that a settled vertex cannot later be improved; a negative edge invalidates exactly that step.

**22.** *Strategy: expand the BFS frontier layer by layer.*

Start with $d(1) = 0$ and the queue $[1]$.

* Layer 0: vertex $1$. Its neighbours $2$ and $3$ get distance $1$; queue $[2,3]$.
* Layer 1: vertices $2$ and $3$. Neighbour $4$ is discovered from $2$ (and would also be reachable from $3$) with distance $2$; queue $[4]$.
* Layer 2: vertex $4$. Neighbour $5$ gets distance $3$; queue $[5]$.
* Layer 3: vertex $5$. Neighbour $6$ gets distance $4$; queue $[6]$.
* Layer 4: vertex $6$ has no unvisited neighbours.

Distances: $d(1) = 0$, $d(2) = 1$, $d(3) = 1$, $d(4) = 2$, $d(5) = 3$, $d(6) = 4$.

*Complexity.* With adjacency lists the run time is $O(V+E) = O(6+6) = O(12)$. Each vertex is enqueued once, and each of the $E = 6$ undirected edges is examined twice (once from each endpoint), for $2E = 12$ edge examinations.

**23.** *Strategy: show that discarding a half provably discards no occurrence of $v$.*

Recall the invariant

$$I:\quad 1 \le lo \le hi+1 \le n+1 \quad\text{and}\quad \bigl(v \in A[1..n] \Rightarrow v \in A[lo..hi]\bigr),$$

where $A[lo..hi]$ is empty when $lo = hi+1$.

*Initialisation.* $lo = 1$, $hi = n$ satisfy $1 \le 1 \le n+1 \le n+1$, and the second clause is trivial.

*Maintenance.* Suppose $lo \le hi$ and let $mid = \lfloor (lo+hi)/2\rfloor$, so $lo \le mid \le hi$.

* If $A[mid] = v$, the loop exits with the correct index and there is nothing to maintain.
* If $A[mid] < v$: for every $j \le mid$ we have $A[j] \le A[mid] < v$ because $A$ is sorted. Hence $v \notin A[lo..mid]$. If $v \in A[lo..hi]$ before the update, then $v \in A[mid+1..hi]$, so setting $lo := mid+1$ preserves the second clause. Also $lo = mid+1 \le hi+1$, and the upper bound $hi+1 \le n+1$ is unchanged.
* If $A[mid] > v$: for every $j \ge mid$, $A[j] \ge A[mid] > v$, so $v \notin A[mid..hi]$. Setting $hi := mid-1$ preserves the clause, and $lo \le mid = (mid-1)+1 = hi+1$.

*Termination.* Each iteration either exits or changes $lo$ or $hi$ so that $hi - lo$ strictly decreases. Since $hi - lo$ is a non-negative integer, only finitely many iterations are possible.

*Postcondition.* If the loop exits with $lo = hi+1$ and $v$ occurred in $A[1..n]$, the invariant would give $v \in A[lo..hi] = \varnothing$, a contradiction. Hence the algorithm reports absence correctly, and if it exits by finding $v$ it returns the correct index.

**24.** *Strategy: compose the reduction with the decider and count the time.*

Let $f$ compute the reduction $L_1 \le_{\mathrm{p}} L_2$ in time $O(n^a)$ and let $D$ decide $L_2$ in time $O(m^b)$ on inputs of length $m$. On input $x$ with $|x| = n$:

1. compute $y = f(x)$; this takes $O(n^a)$ time and produces a string of length $|y| \le c\,n^a$ for some constant $c$ (a machine running in time $t$ writes at most $t$ symbols);
2. run $D$ on $y$, which takes $O(|y|^b) = O(n^{ab})$ time;
3. output the answer of $D$.

Since $x \in L_1 \iff f(x) \in L_2$, the output is correct, and the total time is $O(n^a + n^{ab}) = O(n^{ab})$, a polynomial. Hence $L_1 \in \mathrm{P}$.

*Interpretation.* The reduction maps $x$ to an equivalent instance of $L_2$. A fast algorithm for $L_2$, composed with the (fast) map, is a fast algorithm for $L_1$. This is why reductions transfer tractability *backwards*, and hardness *forwards*: if $L_1$ is hard, then $L_2$ must be at least as hard, because a fast $L_2$ algorithm would solve $L_1$ fast.

## Advanced

**25.** *Strategy: count leaves, bound the height, then compare the bound with a concrete algorithm.*

*Proof.* Fix any comparison-based sorting algorithm $A$ and a size $n$. Consider its decision tree: each internal node asks one comparison of two elements, each leaf is an output permutation. On an input permutation $\pi$, the execution follows a root-to-leaf path and the leaf must be the permutation that sorts $\pi$, i.e. $\pi$ itself (relabelled by the output). Two different input permutations cannot reach the same leaf: if $\pi \ne \sigma$ both reached a leaf labelled $\rho$, then on input $\pi$ the algorithm would output $\rho$, which does not sort $\pi$ unless $\rho = \pi$; the same leaf would have to be labelled $\sigma$ as well, contradiction. Hence the tree has at least $n!$ leaves. A binary tree of height $h$ has at most $2^h$ leaves, so $2^h \ge n!$ and $h \ge \log_2(n!)$; since $h$ is an integer, $h \ge \lceil \lg(n!)\rceil$.

*Evaluation for $n = 6$.* $6! = 720$ and $2^9 = 512 < 720 \le 1024 = 2^{10}$, so the bound is $10$.

*The two-triples procedure.* Sorting a triple takes at most three comparisons (insertion sort: 1 for the second element, at most 2 for the third). Two triples therefore cost $3 + 3 = 6$ comparisons, and merging two sorted lists of total length $6$ costs at most $6 - 1 = 5$ comparisons. Total: $11$.

So this natural algorithm is one comparison above the bound. The counting argument is *non-constructive*: it constrains the shape of any decision tree but does not exhibit one. Whether a tree with exactly $\lceil \lg(n!)\rceil$ leaves-at-depth leaves exists is a separate combinatorial question. For $n = 6$ a 10-comparison algorithm does exist — the merge–insertion (Ford–Johnson) algorithm attains $10$, and its counts for $n = 1,\dots,6$ are $0,1,3,5,7,10$ — but the bound is not always attainable: for $n = 12$ the bound is $\lceil\lg 12!\rceil = 29$ while $30$ comparisons are necessary (Wells, 1971). The general statement is only $\Theta(n\log n)$, and merge sort attains that up to the constant factor $1$.

**26.** *Strategy: count the outcomes that must be distinguished, then use an adversary for the unordered case.*

*(a) Ordered search with absence.* The algorithm must behave correctly on $n+1$ possible situations: the key is at position $i$ for $i = 1,\dots,n$, or the key is absent. Its decision tree therefore has at least $n+1$ leaves, one per situation (two different situations cannot share a leaf, because the outputs — an index or "absent" — differ). A binary tree of height $h$ has at most $2^h$ leaves, so $h \ge \lg(n+1)$, and since $h$ is an integer, $h \ge \lceil\lg(n+1)\rceil$. This is $\Omega(\log n)$.

*(b) Unordered search.* Claim: every algorithm makes at least $n$ comparisons in the worst case. Suppose an algorithm uses at most $n-1$ comparisons on every input of size $n$. Run it on the input in which the target is absent; every comparison answers "not equal", and at most $n-1$ elements are examined, so some element $A[k]$ is never compared with the target. Now run the algorithm on the input in which $A[k]$ *is* the target and all other entries are unchanged. Every comparison made on the first input has the same outcome on the second (the comparisons never involve $A[k]$ against the target), so the algorithm follows the same path and gives the same answer — "absent" — on the second input, which is wrong. Contradiction. Hence $\Omega(n)$ comparisons are necessary, and linear search attains the bound.

**27.** *Strategy: sum the per-node sift-down costs by height, using how few nodes have large height.*

In a heap stored in an array of $n$ elements, a node at index $i$ has height equal to the length of the longest downward path from it. The number of nodes of height $h$ is at most $\left\lceil n/2^{h+1}\right\rceil \le n/2^{h+1}$: nodes of height $h$ sit at levels near the bottom, and there are at most $n/2^{h+1}$ of them.

Sifting down a node of height $h$ costs at most $h$ comparisons and swaps (one per level). Therefore the total work of building the heap bottom-up is at most

$$\sum_{h \ge 0} \frac{n}{2^{h+1}}\,h = \frac{n}{2}\sum_{h \ge 0}\frac{h}{2^{h}}.$$

The series is evaluated by the standard identity $\sum_{h\ge0} hx^{h} = \dfrac{x}{(1-x)^2}$ at $x = \frac12$:

$$\sum_{h\ge0}\frac{h}{2^h} = \frac{1/2}{(1/2)^2} = 2.$$

Hence the total is at most $\frac{n}{2}\cdot 2 = n = O(n)$, not $O(n\log n)$.

*Why the naive bound is loose.* Almost all nodes are near the bottom and have height $0$ or $1$; only the single root has height $\lfloor\lg n\rfloor$. Summing "height $\le \lg n$" for all $n$ nodes overcounts massively.

**28.** *Strategy: substitute the induction hypothesis into the recurrence and simplify.*

*Claim.* For $n = 2^k$, $T(n) = n\lg n - n + 1$.

*Base.* $k = 0$, $n = 1$: $T(1) = 0$ and $1\cdot 0 - 1 + 1 = 0$ ✓.

*Step.* Assume the claim for $k-1$, i.e. $T(2^{k-1}) = (k-1)2^{k-1} - 2^{k-1} + 1$. Then

$$\begin{aligned}
T(2^k) &= 2T(2^{k-1}) + 2^k - 1 \\
&= 2\left((k-1)2^{k-1} - 2^{k-1} + 1\right) + 2^k - 1 \\
&= (k-1)2^k - 2^k + 2 + 2^k - 1 \\
&= (k-1)2^k + 1 \\
&= k2^k - 2^k + 1.
\end{aligned}$$

Since $n = 2^k$ and $k = \lg n$, this is $n\lg n - n + 1$ ✓.

*Check.* $k = 2$: $T(4) = 2\cdot1 + 3 = 5 = 8 - 4 + 1$ ✓. $k = 3$: $T(8) = 2\cdot5 + 7 = 17 = 24 - 8 + 1$ ✓.

**29.** *Strategy: translate "clique in $G$" into "vertex cover in the complement" and verify both directions.*

Let $G = (V,E)$ have $n$ vertices and let $\overline{G} = (V, \overline{E})$ be its complement, where $\{u,v\} \in \overline{E}$ exactly when $\{u,v\} \notin E$ (for $u \ne v$).

*Claim.* For every $S \subseteq V$: $S$ is a clique in $G$ if and only if $V \setminus S$ is a vertex cover of $\overline{G}$.

*Proof.* ($\Rightarrow$) If $S$ is a clique in $G$, then no pair of vertices of $S$ is joined in $\overline{G}$; equivalently, every edge of $\overline{G}$ has at least one endpoint outside $S$, i.e. in $V\setminus S$. Hence $V\setminus S$ covers every edge of $\overline{G}$.

($\Leftarrow$) If $V\setminus S$ is a vertex cover of $\overline{G}$, then no edge of $\overline{G}$ has both endpoints in $S$, so every pair of distinct vertices of $S$ is joined in $G$: $S$ is a clique. $\square$

*The reduction.* Map $(G,k)$ to $(\overline{G}, n-k)$, where $\overline{G}$ is built in $O(V^2)$ time from the adjacency matrix. By the claim, $G$ has a clique of size $k$ iff $\overline{G}$ has a vertex cover of size $n-k$ (the map $S \mapsto V\setminus S$ is a bijection on subsets, reversing inclusions). If $k > n$ there is no clique and $n-k < 0$, which we interpret as "no vertex cover of that size"; both answers are "no". The reduction is polynomial.

*Membership in $\mathrm{NP}$.* A certificate is a set $C$ of at most $k$ vertices; verifying that every edge has an endpoint in $C$ takes $O(V+E)$ time by scanning the adjacency list. So $\mathrm{VERTEX}$-$\mathrm{COVER} \in \mathrm{NP}$.

*Conclusion.* $\mathrm{CLIQUE} \le_{\mathrm{p}} \mathrm{VERTEX}$-$\mathrm{COVER}$ and $\mathrm{CLIQUE}$ is $\mathrm{NP}$-hard (Theorem 7.5), so $\mathrm{VERTEX}$-$\mathrm{COVER}$ is $\mathrm{NP}$-hard; with membership, it is $\mathrm{NP}$-complete.

**30.** *Strategy: use the total sum as the target, and handle parity by mapping odd instances to a fixed no-instance.*

*$\mathrm{SUBSET}$-$\mathrm{SUM} \in \mathrm{NP}$.* An instance is a list $A = (a_1,\dots,a_m)$ of positive integers and a target $T$, encoded in binary. A certificate is a subset $S \subseteq \{1,\dots,m\}$, encoded by its indicator vector of length $m$. The verifier computes $\sum_{i \in S} a_i$ and checks it equals $T$. The sum has $O(m + \log T)$ bits and the additions take polynomial time in the input length. So the instance is a yes-instance exactly when a short certificate exists.

*The reduction.* Given a $\mathrm{PARTITION}$ instance $A$ with total sum $\Sigma = \sum_i a_i$:

* if $\Sigma$ is even, output the $\mathrm{SUBSET}$-$\mathrm{SUM}$ instance $(A, \Sigma/2)$;
* if $\Sigma$ is odd, output the fixed instance $((1), 2)$, which has no solution.

*Correctness.* If $\Sigma$ is even, a partition into two parts of equal sum exists iff some subset sums to $\Sigma/2$: one part of the partition is such a subset, and conversely a subset of sum $\Sigma/2$ has complement of the same sum. If $\Sigma$ is odd, no partition into two equal integer sums exists, and the fixed instance is also a no-instance. The map is computable in polynomial time (compute $\Sigma$, compare to an integer, output either a copy of $A$ with a target or a constant).

*Conclusion.* $\mathrm{PARTITION} \le_{\mathrm{p}} \mathrm{SUBSET}$-$\mathrm{SUM}$; since $\mathrm{PARTITION}$ is $\mathrm{NP}$-complete (a standard result, reducible from $\mathrm{3SAT}$ via a number gadget), $\mathrm{SUBSET}$-$\mathrm{SUM}$ is $\mathrm{NP}$-hard, and with the membership above it is $\mathrm{NP}$-complete.

**31.** *Strategy: prepend the reduction to the verifier or decider.*

*(a) $\mathrm{NP}$ is closed under $\le_{\mathrm{p}}$.* Let $L' \le_{\mathrm{p}} L$ via a polynomial-time computable $f$, and let $L \in \mathrm{NP}$ with verifier $V$ running in time $O(m^c)$ on inputs of length $m$ and certificates of length at most $p(m)$. Define

$$V'(x, w) = V(f(x), w).$$

Then $x \in L' \iff f(x) \in L \iff \exists w\,(|w| \le p(|f(x)|),\ V(f(x),w)=1) \iff \exists w\, V'(x,w) = 1$. The length bound is polynomial in $|x|$ because $|f(x)| \le \mathrm{poly}(|x|)$, and $V'$ runs in time $O(|f(x)|^c + \text{time}(f)) = \mathrm{poly}(|x|)$. So $L' \in \mathrm{NP}$.

*(b) $\mathrm{P}$ is closed under $\le_{\mathrm{p}}$.* This is Exercise 24: compose $f$ with a polynomial-time decider for $L$.

*Remark.* Neither argument needs the reduction to be injective or surjective; only computability in polynomial time and the equivalence $x \in L' \iff f(x) \in L$.

**32.** *Strategy: suppose a decider exists, build the opposite program, and derive a contradiction; then use the duality between recognisability and decidability.*

*(a) Undecidability.* Suppose a program `Halts(P, x)` decides membership in $H$ and always terminates. Define

```
D(P):
    if Halts(P, P) = "halts":
        loop forever
    else:
        halt
```

Then `D` is a program. Consider the question "does `D` halt on input `D`?".

* If `D` halts on `D`, then by definition of $H$, `Halts(D, D)` returns "halts"; the code of `D` then loops forever. Contradiction.
* If `D` loops on `D`, then `Halts(D, D)` returns "loops"; the code of `D` then halts. Contradiction.

Both cases are impossible, so `Halts` cannot exist: $H$ is undecidable. $\blacksquare$

*(b) $H$ is recognisable.* The following semi-decider accepts exactly $H$: on input $\langle P,x\rangle$, simulate $P$ on $x$; if the simulation halts, accept. If $\langle P,x\rangle \in H$ it halts and accepts; if not, it runs forever. Recognisability does not require termination on the complement.

*(c) $\overline{H}$ is not recognisable.* Suppose both $H$ and $\overline{H}$ were recognisable, with semi-deciders $M_1$ and $M_2$. Decide $H$ as follows: on input $y$, run $M_1$ and $M_2$ in parallel, one step at a time (dovetail). Every $y$ lies in exactly one of $H$ and $\overline{H}$, so exactly one of the two machines eventually halts; when it does, output its answer. This decides $H$, contradicting (a). Hence $\overline{H}$ is not recognisable. $\blacksquare$

## Challenge

**33.** *Strategy: use NP-hardness to pull every NP language into coNP, then complement.*

Assume $L$ is $\mathrm{NP}$-complete and $L \in \mathrm{coNP}$.

*Step 1: $\mathrm{coNP}$ is closed under polynomial-time reductions.* Suppose $B \le_{\mathrm{p}} C$ via $f$ and $C \in \mathrm{coNP}$. Then for every $x$,
$$x \in B \iff f(x) \in C, \qquad\text{so}\qquad x \in \overline{B} \iff f(x) \in \overline{C}.$$
Since $C \in \mathrm{coNP}$, $\overline{C} \in \mathrm{NP}$, and $f$ is a polynomial-time reduction $\overline{B} \le_{\mathrm{p}} \overline{C}$; because $\mathrm{NP}$ is closed under reductions (Exercise 31), $\overline{B} \in \mathrm{NP}$, i.e. $B \in \mathrm{coNP}$.

*Step 2: $\mathrm{NP} \subseteq \mathrm{coNP}$.* Let $A \in \mathrm{NP}$. Since $L$ is $\mathrm{NP}$-hard, $A \le_{\mathrm{p}} L$. By Step 1 and $L \in \mathrm{coNP}$, $A \in \mathrm{coNP}$.

*Step 3: $\mathrm{coNP} \subseteq \mathrm{NP}$.* Let $B \in \mathrm{coNP}$; then $\overline{B} \in \mathrm{NP} \subseteq \mathrm{coNP}$ by Step 2. So $\overline{B} \in \mathrm{coNP}$, which means $B \in \mathrm{NP}$.

Therefore $\mathrm{NP} \subseteq \mathrm{coNP}$ and $\mathrm{coNP} \subseteq \mathrm{NP}$, hence $\mathrm{NP} = \mathrm{coNP}$. $\blacksquare$

*Why this is evidence that no $\mathrm{NP}$-complete problem lies in $\mathrm{coNP}$.* $\mathrm{NP} = \mathrm{coNP}$ is widely believed false. It would mean that every problem whose *yes*-instances have short certificates also has short certificates for *no*-instances, an implausible symmetry; and it would collapse the polynomial hierarchy to its first level, since $\mathrm{NP} = \mathrm{coNP}$ implies $\Sigma_2 = \mathrm{NP}$. If one could exhibit a single $\mathrm{NP}$-complete problem in $\mathrm{coNP}$, all of this would follow, so such an exhibition is not expected — and this is exactly why problems in $\mathrm{NP} \cap \mathrm{coNP}$ such as factoring are believed *not* to be $\mathrm{NP}$-complete.

**34.** *Strategy: fix the variables one at a time, using the decider to test whether the current partial assignment can still be extended.*

Let $\varphi$ be a CNF formula over variables $x_1,\dots,x_n$, and let $D$ be a polynomial-time decider for $\mathrm{SAT}$.

*Algorithm.*

1. If $D(\varphi) = 0$, output "unsatisfiable" and stop.
2. For $i = 1$ to $n$:
   * form $\varphi_i$ by substituting the already chosen values for $x_1,\dots,x_{i-1}$ and setting $x_i = 1$;
   * if $D(\varphi_i) = 1$, set $x_i := 1$ and keep $\varphi_i$ as the current formula;
   * otherwise set $x_i := 0$ and keep the formula with $x_i = 0$ substituted.
3. Output the assignment $(x_1,\dots,x_n)$.

*Correctness.* Maintain the invariant: after the $i$-th step, the partial assignment to $x_1,\dots,x_i$ extends to a satisfying assignment of $\varphi$. It holds initially because $D(\varphi) = 1$. Suppose it holds before step $i+1$. Among the satisfying extensions there is at least one; such an extension sets $x_{i+1}$ either to $1$ or to $0$. If $D(\varphi_{i+1}) = 1$, setting $x_{i+1} = 1$ preserves the invariant. If $D(\varphi_{i+1}) = 0$, no satisfying extension sets $x_{i+1} = 1$, so every satisfying extension sets $x_{i+1} = 0$, and the invariant is preserved. At the end all variables are assigned and the invariant says the assignment satisfies $\varphi$.

*Polynomial time.* The algorithm makes $1 + n$ calls to $D$. Each formula $\varphi_i$ is obtained by substitution, has length at most $|\varphi|$, and is built in $O(|\varphi|)$ time. If $D$ runs in time $O(m^c)$, the total is $O(n\cdot|\varphi|^c)$, polynomial in the input length. $\blacksquare$

*Remark.* This is the prototype of a **search-to-decision reduction**: a decider for the decision version yields a polynomial-time finder for the witness version. The same argument works for any language in $\mathrm{NP}$ whose certificates have a bit-by-bit structure, such as $\mathrm{CLIQUE}$ (add vertices one at a time) and $\mathrm{3COLORING}$ (fix colours one vertex at a time).

**35.** *Strategy: compare the cardinalities, then diagonalise explicitly.*

*(a) A counting argument.* Every program is a finite string over a finite alphabet, so the set of all programs is countably infinite. The set of all languages over $\{0,1\}$ is the power set $\mathcal{P}(\{0,1\}^*)$, which is uncountable by Cantor's theorem: if $L_1, L_2, \dots$ were a listing of all languages, the diagonal language $K = \{x_i : x_i \notin L_i\}$ (where $x_i$ is the $i$-th binary string) would be a language not in the list, because it differs from $L_i$ on $x_i$. Since each decidable language is decided by at least one program, there are countably many decidable languages but uncountably many languages, so some language is undecidable.

*(b) An explicit diagonal language.* Fix an encoding of programs by natural numbers and let $P_1, P_2, P_3, \dots$ list all programs (for instance, all syntactically valid strings in lexicographic order). Define

$$L = \{\, i \in \mathbb{N} : P_i \text{ does not halt on input } i \text{ with output } 1 \,\}.$$

*$L$ is undecidable.* Suppose some program $P_j$ decides $L$: it halts on every input and outputs $1$ exactly on the members of $L$. Consider the input $j$. Two equivalences hold:

$$j \in L \iff P_j \text{ does not halt with output } 1 \text{ on } j \qquad\text{(definition of } L\text{)},$$
$$P_j \text{ halts with output } 1 \text{ on } j \iff j \in L \qquad\text{(}P_j \text{ decides } L\text{).}$$

Chaining them gives $j \in L \iff j \notin L$, which is impossible. Hence no program decides $L$. $\blacksquare$

*Remark.* The construction differs from Theorem 7.6 only in the diagonal clause: there, the contradictory program was built to loop exactly when the decider said "halts"; here, the contradiction is read directly off the definition of $L$. Both are instances of the same diagonalisation.

**36.** *Strategy: encode "there exists a certificate" as "this program halts".*

Let $L \in \mathrm{NP}$, witnessed by a verifier $V$ and a polynomial $p$ such that

$$x \in L \iff \exists w\ \bigl(|w| \le p(|x|) \text{ and } V(x,w) = 1\bigr).$$

Given $x$, construct the program $Q_x$:

```
Q_x:
    for each binary string w with |w| <= p(|x|), in lexicographic order:
        if V(x, w) = 1:
            halt
    loop forever
```

Then $Q_x$ halts on the empty input if and only if a certificate exists, i.e. if and only if $x \in L$. The map $x \mapsto \langle Q_x, \varepsilon\rangle$ is computable in polynomial time: $V$ and $p$ are fixed, the only variable part of the program text is the constant $x$, and the loop bound is written in binary. Hence $L \le_{\mathrm{p}} H$ for every $L \in \mathrm{NP}$, so $H$ is $\mathrm{NP}$-hard.

*Why $H$ is not $\mathrm{NP}$-complete.* $\mathrm{NP}$-completeness requires membership in $\mathrm{NP}$, and every language in $\mathrm{NP}$ is decidable: given $x$, enumerate all certificates $w$ with $|w| \le p(|x|)$ and run $V$; this terminates in time $O(2^{p(|x|)}\cdot p(|x|))$. The halting set is undecidable (Theorem 7.6), hence not decidable, hence not in $\mathrm{NP}$. So $H$ is $\mathrm{NP}$-hard but lies outside $\mathrm{NP}$, which is exactly the distinction between $\mathrm{NP}$-hard and $\mathrm{NP}$-complete. $\blacksquare$

