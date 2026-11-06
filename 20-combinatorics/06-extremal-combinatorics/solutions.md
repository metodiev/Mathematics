# Extremal Combinatorics — Solutions

> [Extremal Combinatorics](README.md) · Solutions to the 36 problems in [exercises.md](exercises.md)

Every solution gives the idea first, then the details, and checks the numbers. Extremal statements are justified in both directions wherever the problem asks for it.

## Beginner

**1.** *Method: Mantel's theorem plus an explicit graph.*

By Mantel, a triangle-free graph on $4$ vertices has at most $\lfloor 4^2/4\rfloor = 4$ edges. The graph $K_{2,2}$ — a $4$-cycle — has $4$ edges and is bipartite, hence triangle-free. So $\operatorname{ex}(4,K_3) = 4$ ✓.

For completeness, $K_4$ has $6$ edges but contains triangles, and the graph $K_4$ minus one edge has $5$ edges and still contains a triangle, so no $5$-edge graph on $4$ vertices is triangle-free.

**2.** *Method: read the parts from $n = qr + s$ and subtract the missing edges.*

$n = 6$, $r = 2$: $6 = 3\cdot 2 + 0$, so both parts have size $3$ and

$$t_2(6) = \binom62 - \binom32 - \binom32 = 15 - 3 - 3 = 9 .$$

$n = 6$, $r = 3$: $6 = 2\cdot 3 + 0$, so the parts are $2,2,2$ and

$$t_3(6) = \binom62 - 3\binom22 = 15 - 3 = 12 .$$

Both agree with $\left(1-\frac1r\right)\frac{n^2}{2}$: $\frac12\cdot 18 = 9$ and $\frac23\cdot 18 = 12$ ✓.

**3.** *Method: closed formula and direct count.*

$n = 7$, $r = 3$ gives $7 = 2\cdot 3 + 1$, so $q = 2$, $s = 1$. Closed formula:

$$t_3(7) = \left(1-\frac13\right)\frac{49}{2} - \frac{1\cdot(3-1)}{2\cdot 3} = \frac{2}{3}\cdot\frac{49}{2} - \frac{2}{6} = \frac{49}{3} - \frac13 = \frac{48}{3} = 16 .$$

Direct count with parts $3,2,2$:

$$t_3(7) = \binom72 - \binom32 - \binom22 - \binom22 = 21 - 3 - 1 - 1 = 16 ✓.$$

**4.** *Method: state the theorem, then substitute.*

**Mantel's theorem.** If $G$ is a triangle-free graph on $n$ vertices with $m$ edges, then $m \le \left\lfloor \dfrac{n^2}{4}\right\rfloor$; equality holds for $K_{\lfloor n/2\rfloor,\lceil n/2\rceil}$.

For $n = 12$: $m \le \lfloor 144/4\rfloor = 36$, and $K_{6,6}$ attains it with $6\cdot 6 = 36$ edges ✓.

**5.** *Method: $R(2,s) = s$.*

*Upper bound.* In any two-colouring of $K_5$, either some edge is red — that is a red $K_2$ — or all edges are blue, and then $K_5$ is a blue $K_5$. So $R(2,5) \le 5$.

*Lower bound.* Colour every edge of $K_4$ blue. There is no red edge, hence no red $K_2$, and there is no blue $K_5$ because $K_4$ has only $4$ vertices. So $R(2,5) > 4$.

Hence $R(2,5) = 5$ ✓.

**6.** *Method: explicit cyclic colouring.*

On vertices $\{0,1,2,3,4\}$ colour $\{i,j\}$ red when $j - i \equiv \pm 1 \pmod 5$, blue when $j-i \equiv \pm 2 \pmod 5$.

Red edges: $01, 12, 23, 34, 40$ — the cycle $0\to1\to2\to3\to4\to0$, five edges, no triangle.
Blue edges: $02, 24, 41, 13, 30$ — the cycle $0\to2\to4\to1\to3\to0$, five edges, no triangle.

Indeed $5 + 5 = 10 = \binom52$, so every edge is accounted for, and neither colour class has a triangle ✓. So $R(3,3) > 5$.

**7.** *Method: read the definition.*

If $G$ has any edge, that edge is a copy of $K_2$, so a $K_2$-free graph has no edges: $\operatorname{ex}(n,K_2) = 0$ ✓.

If $H$ has more than $n$ vertices, then no $n$-vertex graph can contain a copy of $H$, because a copy of $H$ would need $v(H) > n$ vertices. So every $n$-vertex graph is $H$-free, and $\operatorname{ex}(n,H) = \binom n2$, attained by $K_n$ ✓.

**8.** *Method: count and apply Mantel.*

$K_{3,3}$ has parts of sizes $3$ and $3$, so it has $3\cdot3 = 9$ edges, and it is bipartite, so it has no odd cycle and in particular no triangle ✓. Hence $\operatorname{ex}(6,K_3) \ge 9$.

Mantel gives $\operatorname{ex}(6,K_3) \le \lfloor 36/4\rfloor = 9$. So $\operatorname{ex}(6,K_3) = 9$ ✓.

**9.** *Method: a clique meets each part at most once.*

In $T_r(n)$ the vertex set is split into $r$ parts, each of which is independent (no edges inside a part), and all edges between different parts are present. Let $S$ be a clique. Two vertices of $S$ cannot lie in the same part, so $\lvert S\rvert$ is at most the number of parts, namely $r$. Hence $T_r(n)$ has no $K_{r+1}$ ✓.

**10.** *Method: Corollary 7.6 with $r = 3$.*

If $G$ is $K_4$-free on $9$ vertices, then $2e(G) \le 2t_3(9) = \frac23\cdot 81 - \frac{s(r-s)}{r}$ with $9 = 3\cdot3+0$, so $2e(G) \le 54$ and the average degree is at most $54/9 = 6$. Some vertex has degree at most the average, so some vertex has degree at most $6$ ✓.

The Turán graph $T_3(9)$ has parts $3,3,3$; each vertex is adjacent to the $6$ vertices outside its own part, so every degree equals $6$. The bound is therefore attained ✓.

**11.** *Method: apply the theorem and inspect comparability.*

Sperner for $n = 3$: the largest antichain in $2^{[3]}$ has $\binom{3}{1} = 3$ members.

Extremal antichains: the three $2$-sets $\{1,2\}, \{1,3\}, \{2,3\}$, or the three $1$-sets $\{1\},\{2\},\{3\}$.

Largest antichain containing $\{1\}$: a set comparable with $\{1\}$ is either $\{1\}$ itself or a superset, so all other members must avoid containing $1$ and must not be contained in $\{1\}$ (which only excludes $\varnothing$). Among $\{2\},\{3\},\{2,3\}$ the only comparable pair is $\{2\} \subset \{2,3\}$, so at most two of them can be chosen. Hence the maximum is $1 + 2 = 3$, attained by $\{\{1\},\{2\},\{3\}\}$ ✓.

**12.** *Method: substitute into EKR.*

For $n = 5$, $k = 2$ the hypothesis $n \ge 2k$ reads $5 \ge 4$ ✓, and the bound is

$$\binom{n-1}{k-1} = \binom41 = 4 .$$

A star attaining it: all $2$-subsets containing $1$, namely $\{1,2\}, \{1,3\}, \{1,4\}, \{1,5\}$ — four sets, and any two meet in $1$ ✓.

## Intermediate

**13.** *Method: describe the colouring, then verify both colour classes.*

Vertices $\mathbb{Z}_8$; red edges are the cycle edges $i(i+1)$ and the diameters $i(i+4)$; blue edges are the remaining ones.

*Red edge count:* $8$ cycle edges plus $4$ diameters $= 12$ ✓.

*No red triangle.* A triangle either has all three edges from the cycle — impossible, a cycle has no triangle — or uses a diameter $\{i, i+4\}$. A third vertex adjacent to both $i$ and $i+4$ must be in $\{i-1,i+1\}$ (neighbours of $i$ on the cycle) and in $\{i+3, i+5\}$ (neighbours of $i+4$); these two sets are disjoint ✓.

*No blue $K_4$.* The blue graph is the complement of the red graph, so a blue $K_4$ is an independent set of size $4$ in the red graph. An independent $4$-set in the cycle $C_8$ must alternate around the cycle, so it is $\{0,2,4,6\}$ or $\{1,3,5,7\}$. The first contains the red diameters $04$ and $26$, the second the red diameters $15$ and $37$. Hence the red independence number is at most $3$, and the blue graph has no $K_4$ ✓.

So $K_8$ admits a colouring with no red triangle and no blue $K_4$, i.e. $R(3,4) > 8$ ✓. (Total check: $12 + 16 = 28 = \binom82$ ✓.)

**14.** *Method: degrees at a vertex plus parity.*

Suppose a two-colouring of $K_9$ has no red triangle and no blue $K_4$.

*(1) Red degrees are at most $3$.* For any vertex $v$, the red neighbourhood $N_R(v)$ contains no red edge, since such an edge with $v$ would form a red triangle. Hence $N_R(v)$ is a blue clique, and it has at most $3$ vertices because there is no blue $K_4$. So $d_R(v) \le 3$ for every $v$.

*(2) Some vertex has red degree at most $2$.* If every vertex had $d_R(v) = 3$, then $\sum_v d_R(v) = 27$; but by the handshake lemma applied to the red graph this sum equals $2e_R$, an even number. Contradiction. So some $v$ has $d_R(v) \le 2$.

*(3) Conclusion.* For that $v$, $d_B(v) = 8 - d_R(v) \ge 6$. Choose six blue neighbours of $v$. The colouring restricted to these six vertices is a two-colouring of $K_6$, so by $R(3,3) = 6$ it contains a monochromatic triangle. A red triangle is impossible in the whole colouring; a blue triangle, together with $v$ (which is joined to all six in blue), is a blue $K_4$ — impossible. Contradiction ✓.

Hence $R(3,4) \le 9$, and with Exercise 13, $R(3,4) = 9$.

*Where each ingredient is used:* the handshake lemma rules out the "all degrees equal $3$" case and so produces the vertex of blue degree at least $6$; the value $R(3,3) = 6$ converts six blue neighbours into a blue $K_4$.

**15.** *Method: substitute into $\binom{r+s-2}{r-1}$.*

$R(3,5) \le \binom{3+5-2}{3-1} = \binom62 = 15$, against the exact value $14$: the bound is off by $1$ ✓.

$R(4,4) \le \binom{4+4-2}{4-1} = \binom63 = 20$, against the exact value $18$: the bound is off by $2$ ✓.

In both cases the Erdős–Szekeres bound is nearly sharp at these small sizes; asymptotically it is far from sharp, since it grows like $4^k$ while the truth grows like $2^k$ up to subexponential factors.

**16.** *Method: look at one vertex of a colouring of $K_N$.*

Let $N = R(r-1,s) + R(r,s-1)$ and consider any two-colouring of $K_N$. Fix a vertex $v$; let $d_R$ and $d_B$ be its numbers of red and blue neighbours, so $d_R + d_B = N - 1$. Hence $d_R \ge R(r-1,s)$ or $d_B \ge R(r,s-1)$.

If $d_R \ge R(r-1,s)$, choose a set $S$ of $R(r-1,s)$ red neighbours. By the definition of $R(r-1,s)$, the colouring on $S$ contains a red $K_{r-1}$ — which with $v$ forms a red $K_r$ — or a blue $K_s$. Either way the required monochromatic clique exists.

If $d_B \ge R(r,s-1)$, choose $R(r,s-1)$ blue neighbours; by definition they contain a blue $K_{s-1}$ (with $v$: a blue $K_s$) or a red $K_r$. Again done.

So every colouring of $K_N$ has the required clique, i.e. $R(r,s) \le R(r-1,s) + R(r,s-1)$ ✓.

**17.** *Method: compute $\sum_A 1/\binom{n}{\lvert A\rvert}$.*

(a) All $3$-subsets of $[6]$: there are $\binom63 = 20$, and each contributes $1/\binom63 = 1/20$. Sum: $20\cdot\frac1{20} = 1$. LYM is satisfied with equality, consistent with this being a full level (and the largest antichain in $2^{[6]}$).

(b) The star at $1$ inside $\binom{[6]}{3}$: there are $\binom52 = 10$ sets, each of size $3$, so the sum is $10\cdot\frac{1}{20} = \frac12 \le 1$ ✓. LYM gives no contradiction, as expected: the star is an antichain (all members have the same size).

Note what LYM does *not* say: it does not forbid a family from having sum $\frac12$; it only forbids exceeding $1$. A family whose LYM sum exceeds $1$ cannot be an antichain, which is exactly how the inequality is used.

**18.** *Method: split into stars and triangles.*

Let $\mathcal{F}$ be a family of $2$-subsets of $[n]$ in which every two meet, with $n \ge 4$.

*Case 1: all edges share a common vertex.* Then $\lvert\mathcal{F}\rvert \le n-1$, since a star at $x$ has exactly $n-1$ edges.

*Case 2: no common vertex.* Then there are edges $ab$ and $ac$ with $b \ne c$. Every other edge must meet both $ab$ and $ac$, so it contains $a$, or it is $bc$, or it is $ad$ — in all cases it is one of $ab, ac, bc$. Hence $\lvert\mathcal{F}\rvert \le 3 \le n-1$ because $n \ge 4$ ✓.

Either way $\lvert\mathcal{F}\rvert \le n-1$, which is the EKR bound $\binom{n-1}{1}$ for $k = 2$ ✓.

**19.** *Method: exhibit, then apply the defect formula.*

Take $A = \{a_1,a_2,a_3\}$, $B = \{b_1,b_2\}$, and join every $a_i$ to both $b_j$.

Then $N(A) = B$, so $\lvert N(A)\rvert = 2 < 3 = \lvert A\rvert$: Hall's condition fails, and indeed at most two of the three $a_i$ can be matched, because each matching edge uses a distinct vertex of $B$.

Defect: for $S = A$, $\lvert S\rvert - \lvert N(S)\rvert = 3 - 2 = 1$; for $S$ of size $1$, $1 - 2 = -1$; for $S$ of size $2$, $2 - 2 = 0$. So $\max_S(\lvert S\rvert - \lvert N(S)\rvert) = 1$, and the defect formula predicts a maximum matching of $\lvert A\rvert - 1 = 2$ ✓, which matches the obvious matching $\{a_1b_1, a_2b_2\}$.

**20.** *Method: double count edges and apply Hall.*

Let $G$ be $k$-regular with parts $A,B$, $k \ge 1$. Counting edges by their endpoint in $A$ and by their endpoint in $B$ gives $k\lvert A\rvert = e(G) = k\lvert B\rvert$, hence $\lvert A\rvert = \lvert B\rvert$.

For $S \subseteq A$: the edges with an endpoint in $S$ number $k\lvert S\rvert$, and all of them end in $N(S)$, where each vertex is incident with at most $k$ of them. Hence $k\lvert N(S)\rvert \ge k\lvert S\rvert$, i.e. $\lvert N(S)\rvert \ge \lvert S\rvert$ ✓. Hall's theorem gives a matching saturating $A$; it has $\lvert A\rvert = \lvert B\rvert$ edges and is therefore perfect ✓.

**21.** *Method: union bound.*

Colour each edge of $K_{15}$ independently red or blue with probability $\frac12$ each. For a $6$-set $S$, the event $A_S$ that $S$ is monochromatic has probability $2^{1-\binom62} = 2^{-14}$. By the union bound,

$$\Pr\Big(\bigcup_S A_S\Big) \le \binom{15}{6}2^{-14} = \frac{5005}{16384} \approx 0.305 < 1 .$$

So with positive probability no $6$-set is monochromatic, i.e. there is a colouring of $K_{15}$ with no monochromatic $K_6$ ✓. (The arithmetic: $\binom{15}{6} = 5005$ ✓.)

**22.** *Method: Theorem 7.15 at $n = 64$.*

Take $p = 64^{-1/2} = \frac18$ and $G \sim G(64,p)$. Then

$$\mathbb{E}[\text{edges}] = \binom{64}{2}\cdot\frac18 = 2016\cdot\frac18 = 252, \qquad \mathbb{E}[\text{triangles}] = \binom{64}{3}\cdot\frac{1}{512} = 41664\cdot\frac{1}{512} = 81.375 .$$

So some graph satisfies $X - Y \ge 252 - 81.375 = 170.625$; since $X - Y$ is an integer, $X - Y \ge 171$. Deleting one edge per triangle leaves at least

$$252 - 81.375 = 170.625$$

edges, i.e. at least $171$ edges, and the graph is triangle-free.

The general bound of Theorem 7.15 reads $\frac13\cdot 64^{3/2} - \frac12\cdot 8 = \frac{512}{3} - 4 \approx 166.67$, so at least $166$ edges ✓, consistent with the sharper direct computation.

Mantel's exact value is $\lfloor 64^2/4\rfloor = 1024$, so the alteration bound is about $17\%$ of the truth: it certifies existence, not optimality ✓.

**23.** *Method: Mantel and Turán.*

$\operatorname{ex}(9,K_3) = \lfloor 81/4\rfloor = 20$, attained by $K_{4,5}$ ✓ (parts $4,5$, edges $4\cdot5 = 20$).

$\operatorname{ex}(9,K_4) = t_3(9)$ by Turán with $r = 3$; parts $3,3,3$, so $t_3(9) = \binom92 - 3\binom32 = 36 - 9 = 27$ ✓, attained by $T_3(9)$.

**24.** *Method: equality in the convexity lemma.*

Let $G$ be a complete $r$-partite graph on $n$ vertices with part sizes $n_1,\dots,n_r$ summing to $n$, and suppose $e(G) = t_r(n) = \binom n2 - \sum_i\binom{n_i^*}{2}$, where $n_i^*$ are the balanced sizes.

Since $e(G) = \binom n2 - \sum_i\binom{n_i}{2}$, the equality says $\sum_i\binom{n_i}{2} = \sum_i\binom{n_i^*}{2}$, the minimum of the convex function $\sum_i\binom{n_i}{2}$ over compositions of $n$ into $r$ parts. By the smoothing argument of Lemma 7.2, the minimum is attained only at the balanced vector (up to order), so $\{n_1,\dots,n_r\} = \{n_1^*,\dots,n_r^*\}$ as multisets. A complete $r$-partite graph is determined by its vertex partition, so $G \cong T_r(n)$ ✓.

## Advanced

**25.** *Method: sum an inequality over the edges, then use Cauchy–Schwarz.*

Let $G$ be triangle-free with $n$ vertices, $m$ edges and degrees $d_v$.

*Step 1.* For an edge $uv$, no vertex is adjacent to both $u$ and $v$: such a vertex $w$ would give the triangle $uvw$. The $d(u)$ neighbours of $u$ and the $d(v)$ neighbours of $v$ are therefore disjoint except for $u$ and $v$ themselves, so $d(u) + d(v) \le n$. (In detail: $N(u)\setminus\{v\}$ and $N(v)\setminus\{u\}$ are disjoint subsets of the $n-2$ remaining vertices, so $(d(u)-1)+(d(v)-1) \le n-2$.)

*Step 2.* Sum over the edges:

$$\sum_{uv\in E}\big(d(u)+d(v)\big) = \sum_{v}d(v)\cdot d(v) = \sum_v d(v)^2 \le mn .$$

The equality holds because $v$ appears in the sum once for each of its $d(v)$ incident edges.

*Step 3.* Cauchy–Schwarz:

$$\Big(\sum_v d(v)\Big)^2 \le n\sum_v d(v)^2 \le n\cdot mn = mn^2 .$$

*Step 4.* Since $\sum_v d(v) = 2m$, Step 3 gives $4m^2 \le mn^2$. If $m > 0$, divide by $m$: $4m \le n^2$, i.e. $m \le n^2/4$. Since $m$ is an integer, $m \le \lfloor n^2/4\rfloor$. If $m = 0$ the conclusion is trivial ✓.

*Why the floor matters.* For odd $n$, $n^2/4$ is not an integer: at $n = 5$ it gives $6.25$, and the true maximum is $6 = \lfloor 25/4\rfloor$, attained by $K_{2,3}$ ✓.

**26.** *Method: apply Turán with $r = 3$.*

A graph is $K_4$-free exactly when it has no $K_{3+1}$, so Turán's theorem with $r = 3$ gives $e(G) \le t_3(n)$ for every $K_4$-free $G$ on $n$ vertices, and $T_3(n)$ attains it. Hence $\operatorname{ex}(n,K_4) = t_3(n)$ ✓.

$n = 7$: $7 = 2\cdot3+1$, parts $3,2,2$:

$$t_3(7) = 21 - 3 - 1 - 1 = 16 .$$

$n = 10$: $10 = 3\cdot3+1$, parts $4,3,3$:

$$t_3(10) = 45 - 6 - 3 - 3 = 33 .$$

So $\operatorname{ex}(7,K_4) = 16$ and $\operatorname{ex}(10,K_4) = 33$ ✓.

**27.** *Method: induction on $r+s$ with the recursion of Exercise 16.*

*Base cases.* $R(1,s) = 1 = \binom{s-1}{0}$ ✓ and $R(2,s) = s = \binom{s}{1}$ ✓ (Proposition 7.8).

*Inductive step.* Let $r,s \ge 2$ and assume the bound for all pairs with smaller sum. By Exercise 16 and Pascal's identity,

$$R(r,s) \le R(r-1,s) + R(r,s-1) \le \binom{r+s-3}{r-2} + \binom{r+s-3}{r-1} = \binom{r+s-2}{r-1},$$

where the first inequality is the recursion and the second is the induction hypothesis applied to the pairs $(r-1,s)$ and $(r,s-1)$ ✓.

*Consequence.* Since $\binom{2k-2}{k-1} \le 2^{2k-2} = 4^{k-1}$, we get $R(k,k) < 4^k$, so Ramsey numbers are finite ✓. (The middle binomial coefficient is one term of the sum $\sum_j\binom{2k-2}{j} = 2^{2k-2}$.)

**28.** *Method: union bound over the "bad" events.*

Let $n = \lfloor 2^{k/2}\rfloor$ and colour the edges of $K_n$ independently, each colour with probability $\frac12$.

*Step 1: probability a fixed $k$-set is monochromatic.* The $k$-set spans $\binom k2$ edges, all independent; the all-red and the all-blue event each have probability $2^{-\binom k2}$, and they are disjoint. So

$$\Pr(A_S) = 2\cdot 2^{-\binom k2} = 2^{1-\binom k2} .$$

*Step 2: union bound.* By Lemma 7.13,

$$\Pr(\text{some monochromatic } K_k) \le \binom nk 2^{1-\binom k2} .$$

*Step 3: estimate the binomial coefficient.* For $n \ge k$, $\binom nk = \frac{n(n-1)\cdots(n-k+1)}{k!} \le \frac{n^k}{k!}$ (each of the $k$ factors in the numerator is at most $n$).

*Step 4: combine, using $n \le 2^{k/2}$:*

$$\binom nk 2^{1-\binom k2} \le \frac{n^k}{k!}2^{1-\frac{k(k-1)}{2}} \le \frac{2^{k^2/2}}{k!}2^{1-\frac{k(k-1)}{2}} = \frac{2^{1+\frac{k}{2}}}{k!} .$$

*Step 5: the inequality $2^{1+k/2} < k!$ for $k \ge 3$.* At $k = 3$: $2^{2.5} = 4\sqrt2 \approx 5.657 < 6 = 3!$ ✓. If it holds for $k$, then

$$\frac{2^{1+(k+1)/2}}{(k+1)!} = \frac{2^{1+k/2}}{k!}\cdot\frac{\sqrt2}{k+1} < \frac{2^{1+k/2}}{k!} < 1$$

because $\sqrt2/(k+1) < 1$ for $k \ge 1$ ✓. So the inequality holds for all $k \ge 3$.

*Step 6: conclusion.* The union bound is less than $1$, so with positive probability no $k$-set is monochromatic. Such a colouring exists, hence $R(k,k) > n = \lfloor 2^{k/2}\rfloor$, i.e. $R(k,k) \ge \lfloor 2^{k/2}\rfloor + 1 > 2^{k/2}$ ✓.

**29.** *Method: put the starting points in order.*

A cyclic order of $n$ elements determines $n$ intervals of length $k$: $I_i = \{i, i+1, \dots, i+k-1\}$ (indices modulo $n$). Let $\mathcal{I}$ be a family of pairwise intersecting intervals and let $S \subseteq \mathbb{Z}_n$ be the set of their starting points, so $\lvert\mathcal{I}\rvert = \lvert S\rvert = m$. Write $S = \{i_1 < i_2 < \cdots < i_m\}$ in $\{0,1,\dots,n-1\}$.

*Case 1: $i_m - i_1 \le k-1$.* Then all starting points lie in the arc $\{i_1, i_1+1, \dots, i_m\}$ of $i_m - i_1 + 1 \le k$ positions, so $m \le k$ ✓.

*Case 2: $i_m - i_1 \ge k$.* Since $I_{i_1}$ and $I_{i_m}$ must intersect and their starting points are at distance $\ge k$ in the forward direction, they can meet only across the point $0$: $I_{i_m}$ runs from $i_m$ past $n-1$ to $i_m + k - 1 - n < n$, and it meets $I_{i_1} = \{i_1,\dots,i_1+k-1\}$ only if $i_1 \le i_m + k - 1 - n$, i.e.

$$i_1 + n - i_m \le k-1 .$$

Then every starting point lies in the arc from $i_m$ through $n-1, 0$ to $i_1$, which has $n - i_m + i_1 + 1 \le k$ positions; so $m \le k$ ✓.

Hence in every case $m \le k$ ✓.

**30.** *Method: random maximal chain; then compare binomial coefficients.*

*Proof of LYM.* A maximal chain of $2^{[n]}$ is $\varnothing \subset \{x_1\} \subset \{x_1,x_2\} \subset \cdots \subset [n]$, determined by the ordering $x_1,\dots,x_n$, so there are $n!$ of them; choose one uniformly at random. A set $A$ of size $a$ lies on the chain exactly when the first $a$ elements of the random ordering are the elements of $A$ in some order, which has probability

$$\Pr(A \in \text{chain}) = \frac{a!\,(n-a)!}{n!} = \frac{1}{\binom na} .$$

If $\mathcal{F}$ is an antichain, a chain contains at most one member of $\mathcal{F}$ (a chain is totally ordered, and two comparable members would violate the antichain property). Hence the events are disjoint:

$$1 \ge \Pr\Big(\bigcup_{A\in\mathcal{F}}\{A \in \text{chain}\}\Big) = \sum_{A\in\mathcal{F}}\frac{1}{\binom{n}{\lvert A\rvert}},$$

which is LYM ✓.

*Deduction of Sperner.* For every $A$ we have $\binom{n}{\lvert A\rvert} \le \binom{n}{\lfloor n/2\rfloor}$, because binomial coefficients increase up to the middle. Hence each term satisfies $1/\binom{n}{\lvert A\rvert} \ge 1/\binom{n}{\lfloor n/2\rfloor}$, and LYM gives

$$1 \ge \frac{\lvert\mathcal{F}\rvert}{\binom{n}{\lfloor n/2\rfloor}}, \qquad\text{so}\qquad \lvert\mathcal{F}\rvert \le \binom{n}{\lfloor n/2\rfloor} ✓.$$

*Why it is not an equivalence.* LYM is strictly stronger. For $n = 4$, the family consisting of the four $3$-sets together with the two $1$-sets $\{1\},\{2\}$ has LYM sum $4\cdot\frac14 + 2\cdot\frac14 = 1.5 > 1$ but size $6 = \binom42$, which satisfies Sperner's bound. So Sperner's bound can hold for a non-antichain, while LYM fails; LYM therefore detects more than the size bound does.

**31.** *Method: add dummy vertices and apply Hall.*

Let $d = \max_{S\subseteq A}(\lvert S\rvert - \lvert N(S)\rvert)$; note $d \ge 0$ since $S = A$ is allowed. Form $G^+$ by adding $d$ new vertices to $B$, each adjacent to every vertex of $A$.

*Hall's condition holds in $G^+$.* For $S = \varnothing$ it is trivial. For $S \ne \varnothing$, the new vertices are all in $N_{G^+}(S)$, so $\lvert N_{G^+}(S)\rvert \ge \lvert N_G(S)\rvert + d \ge \lvert N_G(S)\rvert + (\lvert S\rvert - \lvert N_G(S)\rvert) = \lvert S\rvert$ ✓.

By Hall there is a matching $M^+$ of $G^+$ saturating $A$. At most $d$ of its edges use new vertices, so deleting those leaves at least $\lvert A\rvert - d$ edges of $G$ — a matching of size at least $\lvert A\rvert - d$ ✓.

*Upper bound.* Let $M$ be any matching and $S \subseteq A$. At most $\lvert N(S)\rvert$ edges of $M$ have their $A$-endpoint in $S$, and at most $\lvert A\rvert - \lvert S\rvert$ have it in $A\setminus S$. So

$$\lvert M\rvert \le \lvert N(S)\rvert + \lvert A\rvert - \lvert S\rvert = \lvert A\rvert - \big(\lvert S\rvert - \lvert N(S)\rvert\big) \le \lvert A\rvert - d .$$

Hence the maximum matching size is exactly $\lvert A\rvert - d$ ✓.

**32.** *Method: induction on $k$, removing one perfect matching at a time.*

Let $G$ be $k$-regular bipartite with $k \ge 1$. By Corollary 7.23, $G$ has a perfect matching $M_1$. Delete the edges of $M_1$: every vertex loses exactly one incident edge (because $M_1$ is perfect), so the remaining graph is $(k-1)$-regular and bipartite.

If $k - 1 \ge 1$, apply Corollary 7.23 again to find a perfect matching $M_2$ of the remainder, and continue. After $k$ steps the graph is $0$-regular, i.e. all edges have been removed, and the edge sets $M_1,\dots,M_k$ are pairwise disjoint perfect matchings whose union is $E(G)$ ✓.

*Consequence.* Edge-colouring $G$ with $k$ colours by giving $M_i$ colour $i$: this is a proper $k$-edge-colouring, and since every vertex has degree $k$ it uses exactly $k$ colours — König's line-colouring theorem for regular bipartite graphs ✓.

## Challenge

**33.** *Method: the recursion with exact values.*

By the recursion of Exercise 16 with $r = s = 4$,

$$R(4,4) \le R(3,4) + R(4,3) = 9 + 9 = 18,$$

using $R(3,4) = 9$ (Theorem 7.10) and the symmetry $R(4,3) = R(3,4)$ ✓.

So every two-colouring of $K_{18}$ contains a monochromatic $K_4$; the bound is sharp since $R(4,4) = 18$, a value whose lower bound requires a colouring of $K_{17}$ that is not constructed here.

*Remark.* The recursion alone gives $R(k,k) \le 4^{k}$ up to polynomial factors, which is the same order as the Erdős–Szekeres bound; improving the exponent is the central open problem referred to in Section 7.4.

**34.** *Method: alter a random graph.*

Let $p = n^{-1/2}$, $G \sim G(n,p)$, $X = e(G)$, $Y$ = number of triangles.

$$\mathbb{E}[X] = \binom n2 p = \frac{n(n-1)}{2\sqrt n} = \frac{n^{3/2}}{2} - \frac{\sqrt n}{2}, \qquad \mathbb{E}[Y] = \binom n3 p^3 \le \frac{n^3}{6}\cdot n^{-3/2} = \frac{n^{3/2}}{6} .$$

Hence $\mathbb{E}[X - Y] \ge \frac{n^{3/2}}{3} - \frac{\sqrt n}{2}$, which is positive exactly when $\frac{n^{3/2}}{3} > \frac{\sqrt n}{2}$, i.e. $n > \frac32$, so for all $n \ge 2$ ✓.

Since the expectation of $X - Y$ is positive, some graph $G_0$ satisfies $X(G_0) - Y(G_0) \ge \frac{n^{3/2}}{3} - \frac{\sqrt n}{2}$. Delete one edge from each triangle of $G_0$: at most $Y(G_0)$ edges are lost, no triangle survives (every triangle contained one of the deleted edges), and at least $X(G_0) - Y(G_0) \ge \frac{n^{3/2}}{3} - \frac{\sqrt n}{2}$ edges remain, and the resulting graph is triangle-free ✓.

*At $n = 10^4$:* $n^{3/2} = 10^6$ and $\sqrt n = 100$, so the guarantee is

$$\frac{10^6}{3} - 50 = 333333.33\ldots - 50 = 333283.33,$$

i.e. at least $333\,284$ edges. Mantel's exact value is $10^8/4 = 25\,000\,000$, so the alteration bound is about $1.3\%$ of the truth ✓ — a striking illustration of the method's generality and its bluntness.

**35.** *Method: Katona's circle argument.*

Let $n \ge 2k$ and let $\mathcal{F} \subseteq \binom{[n]}{k}$ be intersecting.

*Step 1: random cyclic order.* Choose uniformly at random one of the $(n-1)!$ cyclic orders of $[n]$. In a fixed order there are exactly $n$ intervals of length $k$, namely the sets of $k$ consecutive elements, and they are distinct $k$-sets. By symmetry over the $\binom nk$ possible $k$-sets, a fixed $k$-set $A$ is an interval with probability

$$\Pr(A \text{ interval}) = \frac{n}{\binom nk} .$$

*Step 2: expectation.* Let $Z$ be the number of members of $\mathcal{F}$ that are intervals of the random order. By linearity of expectation,

$$\mathbb{E}[Z] = \sum_{A\in\mathcal{F}}\Pr(A \text{ interval}) = \lvert\mathcal{F}\rvert\cdot\frac{n}{\binom nk} .$$

*Step 3: deterministic bound.* In every cyclic order, the intervals belonging to $\mathcal{F}$ are pairwise intersecting (because $\mathcal{F}$ is intersecting), so by the lemma of Exercise 29 there are at most $k$ of them. Hence $Z \le k$ for every outcome, and $\mathbb{E}[Z] \le k$ ✓.

*Step 4: conclude.*

$$\lvert\mathcal{F}\rvert\cdot\frac{n}{\binom nk} = \mathbb{E}[Z] \le k \quad\Longrightarrow\quad \lvert\mathcal{F}\rvert \le \frac{k\binom nk}{n} = \binom{n-1}{k-1},$$

using $k\binom nk = n\binom{n-1}{k-1}$ ✓.

*Equality.* For $n > 2k$ the stars attain the bound, and they are the only extremal families. For $n = 2k$, choosing one set from each complementary pair also attains it — and one checks the two constructions coincide only when the family is a star.

**36.** *Method: count common neighbours, then apply convexity.*

Let $G$ be $C_4$-free on $n$ vertices with $m$ edges and degrees $d_x$.

*Step 1: any two vertices have at most one common neighbour.* If distinct $u,v$ had two common neighbours $x \ne y$, then $u\,x\,v\,y\,u$ would be a $4$-cycle ✓.

*Step 2: count pairs.* Count the pairs $(x, \{u,v\})$ where $u \ne v$ are both neighbours of $x$. On one hand, each vertex $x$ contributes $\binom{d_x}{2}$ such pairs. On the other hand, a pair $\{u,v\}$ is counted once for each common neighbour of $u$ and $v$, hence at most once. Therefore

$$\sum_{x}\binom{d_x}{2} \le \binom n2 .$$

*Step 3: convexity.* The function $t \mapsto \binom t2 = t(t-1)/2$ is convex, so by Jensen (or directly by the smoothing argument)

$$\sum_x \binom{d_x}{2} \ge n\binom{\bar d}{2}, \qquad \bar d = \frac{2m}{n} .$$

*Step 4: solve the inequality.* Combining Steps 2 and 3,

$$n\binom{\bar d}{2} \le \binom n2 \;\Longrightarrow\; \frac{n\,\bar d(\bar d - 1)}{2} \le \frac{n(n-1)}{2} \;\Longrightarrow\; \bar d(\bar d - 1) \le n - 1 .$$

The positive root of $t^2 - t - (n-1) = 0$ is $\frac{1+\sqrt{4n-3}}{2}$, so

$$\bar d \le \frac{1+\sqrt{4n-3}}{2}, \qquad\text{hence}\qquad m = \frac{n\bar d}{2} \le \frac n4\big(1+\sqrt{4n-3}\big) ✓.$$

*Order of growth.* The bound is $\frac n4\sqrt{4n} + O(n) = \frac12 n^{3/2} + O(n)$, so $\operatorname{ex}(n,C_4) = O(n^{3/2})$ ✓. The matching lower bound of order $n^{3/2}$ comes from incidence graphs of projective planes, so $\operatorname{ex}(n,C_4) = \Theta(n^{3/2})$ — the extremal order for a bipartite forbidden graph is genuinely smaller than the $\Theta(n^2)$ of the non-bipartite case.

*Check at small $n$.* For $n = 5$ the bound gives $\frac54(1+\sqrt{17}) = 6.40$, and indeed $\operatorname{ex}(5,C_4) = 6$: the two triangles sharing one vertex have $5$ vertices, $6$ edges and no $4$-cycle, while every $7$-edge graph on $5$ vertices contains one. For $n = 6$ the bound gives $8.37$ against the true value $7$ (verified by exhaustive search over the $2^{15}$ graphs on six vertices) ✓.
