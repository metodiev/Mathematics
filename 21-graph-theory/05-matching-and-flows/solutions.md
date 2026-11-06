# Matching and Flows — Solutions

> [Matching and Flows](README.md) · Solutions to the 36 problems in [exercises.md](exercises.md)

Each solution states its strategy, then carries out every step. Proofs name the theorem they invoke,
because most errors in this subject come from using König or Hall outside their hypotheses.

## Beginner

**1.** *Strategy: a matching has at most $\lfloor n/2\rfloor$ edges, and a perfect matching needs an even
number of vertices.*

(a) $P_7$: pair $12,34,56$, leaving $7$; $\alpha'=3=\lfloor 7/2\rfloor$. Seven vertices is odd, so **no**
perfect matching. (b) $C_6$: $\alpha'=3$, and $\{12,34,56\}$ is perfect. (c) $K_{1,5}$: every edge
contains the centre, so $\alpha'=1$; the five leaves cannot be matched. (d) $K_{3,4}$: $\alpha'=\min(3,4)=3$;
a perfect matching would need $\lvert V\rvert=7$ even, so none. (e) $K_4$: $\alpha'=2$ and
$\{12,34\}$ is perfect.

**2.** *Strategy: count by the "smallest unused vertex chooses a partner" recursion; a perfect matching
needs an even number of vertices and equal sides.*

* $K_6$: $5!!=5\cdot3\cdot1=15$.
* $K_{4,4}$: $4!=24$ (each permutation is a perfect matching).
* $C_8$: exactly $2$ (take alternate edges, or the complementary alternate set).
* $P_8$: exactly $1$: vertex $1$ has only the neighbour $2$, so $12\in M$; then $3$ has only $4$ left,
  and so on.
* $K_{2,3}$: $0$, because $5$ vertices is odd (and $\lvert A\rvert\ne\lvert B\rvert$).

**3.** *Strategy: take one perfect matching and rotate the indices.*

$$M_1=\{a_1b_1,a_2b_2,a_3b_3\},\quad M_2=\{a_1b_2,a_2b_3,a_3b_1\},\quad M_3=\{a_1b_3,a_2b_1,a_3b_2\}.$$

Each $M_i$ has three edges with all six endpoints distinct, and every one of the nine edges of $K_{3,3}$
appears exactly once, so $K_{3,3}=M_1\cup M_2\cup M_3$. This is Corollary 7.5.2 with $k=3$.

**4.** *Strategy: build a matching whose endpoints saturate every edge, then compare with the bound
$\lfloor 6/2\rfloor=3$.*

$M=\{23,45\}$ is a matching of size $2$. It is maximal: the edges are $12,23,34,45,56,26$, and each meets
$2$, $3$, $4$ or $5$ — all saturated. $M^*=\{12,34,56\}$ has size $3=\lfloor 6/2\rfloor$, so it is maximum
(and perfect).

Augmenting path for $M$: vertex $1$ is free and vertex $6$ is free ($6$ meets only $5$ and $2$, both
saturated). The path $1$–$2$–$3$–$4$–$5$–$6$ uses $12\notin M$, $23\in M$, $34\notin M$, $45\in M$,
$56\notin M$: alternating, both ends free, hence $M$-augmenting. Indeed
$M\triangle P=\{12,34,56\}=M^*$.

**5.** *Strategy: find two free vertices joined by an alternating path.*

$M=\{12,45\}$ leaves $3$ and $6$ free. The path $3$–$4$–$5$–$6$ has $34\notin M$, $45\in M$,
$56\notin M$: alternating with both endpoints free. Hence
$$M\triangle P=\{12,45\}\triangle\{34,45,56\}=\{12,34,56\},$$
a perfect matching of $C_6$ (the other perfect matching is $\{23,45,61\}$).

**6.** *Strategy: search for a deficient set; if one exists, apply the defect formula.*

The set $S=\{a_1,a_2,a_3\}$ has $N(S)=\{b_1,b_2\}$, so $\lvert N(S)\rvert=2<3=\lvert S\rvert$: Hall's
condition fails, and no perfect matching exists. Note how the failure is invisible on small sets: every
singleton has $2$ or $3$ neighbours, and every pair has $2$ or $3$, so all singletons and all pairs pass.

Deficiency: $d=\max_S(\lvert S\rvert-\lvert N(S)\rvert)$. For $S=\{a_1,a_2,a_3\}$ it is $3-2=1$; for
$S=A$ it is $4-4=0$; for every other $S$ it is $\le0$. Hence $d=1$ and, by Theorem 7.5.3,
$\alpha'(G)=4-1=3$. A matching of size $3$ is $\{a_1b_1,\ a_2b_2,\ a_4b_3\}$; size $4$ is impossible
because three $A$-vertices compete for two neighbours.

**7.** *Strategy: run the directed BFS of Algorithm 7.3.1 from the free $A$-vertices.*

Free $A$-vertices: $a_2,a_3$. Start at $a_2$. Non-matching edges from $a_2$: only $a_2b_1$. From $b_1$,
the matching edge $b_1a_1$. From $a_1$, the non-matching edge $a_1b_2$. The vertex $b_2$ is free, so
$$a_2\to b_1\to a_1\to b_2$$
is augmenting, and $M'=\{a_2b_1,\ a_1b_2\}$ has size $2$. A second round adds $a_3b_3$ (both endpoints
free), giving the perfect matching $\{a_2b_1,\ a_1b_2,\ a_3b_3\}$.

**8.** *Strategy: apply Hall's condition to the sets $\{s_i\}$; a violated set certifies failure.*

Take $S=\{s_1,s_2,s_5\}$. Their allowed projects are $\{p_1,p_2\}\cup\{p_1,p_2\}\cup\{p_1\}=\{p_1,p_2\}$,
so $\lvert N(S)\rvert=2<3=\lvert S\rvert$: no system of distinct representatives exists.

Maximum number served: the defect formula gives
$d=\max_S(\lvert S\rvert-\lvert N(S)\rvert)=1$ (attained at the set above), so at most $5-1=4$ students
can be served. Indeed $s_5p_1$, $s_1p_2$, $s_3p_3$, $s_4p_4$ serves four, leaving $s_2$ out.

**9.** *Strategy: apply the construction of Theorem 7.6.1 to a maximum matching, then check the cover
directly.*

Take $M=\{a_1b_1,\ a_2b_2,\ a_4b_3\}$, maximum by Problem 6. The only free $A$-vertex is $a_3$, so
$U=\{a_3\}$. Alternating traversal from $a_3$:
$$a_3\to b_1\to a_1\to b_2\to a_2,$$
and neither $a_1$ nor $a_2$ has a further edge outside $M$ into an unvisited vertex. Hence
$Z=\{a_3,b_1,a_1,b_2,a_2\}$ and
$$C=(A\setminus Z)\cup(B\cap Z)=\{a_4\}\cup\{b_1,b_2\}=\{a_4,b_1,b_2\}.$$
Check: $a_1b_1$ and $a_2b_1$ and $a_3b_1$ are covered by $b_1$; $a_1b_2$, $a_2b_2$, $a_3b_2$, $a_4b_2$ by
$b_2$ (or $a_4$); $a_4b_3$ and $a_4b_4$ by $a_4$. So $C$ is a cover with $\lvert C\rvert=3=\lvert M\rvert$,
confirming König's equality. A cover of size $2$ is impossible, since $\alpha'=3$.

**10.** *Strategy: check the two constraints arc by arc, sum the value, then look for an augmenting path
in the residual network.*

Capacities: $f(sa)=3\le4$, $f(sb)=2\le2$, $f(ab)=0\le1$, $f(at)=3\le3$, $f(bt)=2\le3$ — all satisfied.
Conservation at $a$: in $3$, out $3+0=3$. At $b$: in $2$, out $0+2=2$. So $f$ is feasible with
$\lvert f\rvert=3+2=5$.

Residual capacities: $sa:1$, $sb:0$, $ab:1$, $at:0$, $bt:1$. The residual path $s\to a\to b\to t$ has
$\delta=\min(1,1,1)=1$, so push $1$: $f(sa)=4$, $f(ab)=1$, $f(bt)=3$, value $6$.

Optimality: the cut $S=\{s,a,b\}$, $T=\{t\}$ has capacity $c(at)+c(bt)=3+3=6=\lvert f\rvert$, so by
Theorem 7.9.1 the flow is maximum and the cut is minimum.

**11.** *Strategy: enumerate the four cuts with $s\in S$, $t\notin S$.*

| $S$ | arcs from $S$ to $T$ | capacity |
|---|---|---|
| $\{s\}$ | $sa:3$, $sb:1$ | $4$ |
| $\{s,a\}$ | $sb:1$, $ab:2$, $at:1$ | $4$ |
| $\{s,b\}$ | $sa:3$, $bt:3$ | $6$ |
| $\{s,a,b\}$ | $at:1$, $bt:3$ | $4$ |

Minimum capacity $4$. A flow of value $4$: $sa=3$, $sb=1$, $at=1$, $ab=2$, $bt=3$. Check $a$: in $3$, out
$1+2=3$; $b$: in $1+2=3$, out $3$. Value $3+1=4$. By Theorem 7.9.1 both are optimal, so the max flow is
$4$ and the min cut is $4$.

**12.** *Strategy: settle each claim by a theorem or a concrete counterexample.*

(a) **False.** In $P_6$ the matching $\{23,45\}$ is maximal but has $2$ edges against the maximum $3$
(Problem 4). (b) **True.** A perfect matching has $n/2=\lfloor n/2\rfloor$ edges, the largest possible.
(c) **True.** Every vertex is covered by an edge, and each edge covers two vertices, so $\lvert V\rvert=2\lvert M\rvert$.
(d) **False.** Two disjoint copies of $K_4$ have $n=8$ and $\alpha'=2+2=4=n/2$, yet the graph is
disconnected. (e) **False.** Let $A=\{a_1,a_2\}$, $B=\{b_1,b_2,b_3\}$ with edges $a_1b_1,a_2b_1,a_1b_2,a_2b_2$.
Hall holds for $A$ ($\lvert N(\{a_i\})\rvert=2$, $\lvert N(A)\rvert=2$), but for $B$ the set $\{b_3\}$ has
$N(\{b_3\})=\varnothing$.

## Intermediate

**13.** *Strategy: a perfect matching restricts to a perfect matching of each component.*

If $M$ is perfect and $C$ is a component, every edge of $M$ incident with a vertex of $C$ has both
endpoints in $C$ (an edge cannot leave a component). Hence $M\cap E(C)$ is a perfect matching of $C$, so
$\lvert V(C)\rvert=2\lvert M\cap E(C)\rvert$ is even.

The converse fails, even for trees: $K_{1,3}$ has $4$ vertices and $\alpha'=1$, and more generally a star
with $2k$ vertices has no perfect matching for $k\ge2$.

**14.** *Strategy: verify Hall's condition, splitting into $S\leq n/2$ and $S>n/2$.*

Let $S\subseteq A$. If $\lvert S\rvert\le n/2$, then picking any $a\in S$ gives
$\lvert N(S)\rvert\ge\deg(a)\ge n/2\ge\lvert S\rvert$. If $\lvert S\rvert>n/2$, suppose some $b\in B$ has
no neighbour in $S$; then all $\ge n/2$ neighbours of $b$ lie in $A\setminus S$, so
$\lvert A\setminus S\rvert\ge n/2$, i.e. $\lvert S\rvert\le n/2$ — a contradiction. Hence $N(S)=B$ and
$\lvert N(S)\rvert=n\ge\lvert S\rvert$. Hall's condition holds, so by Corollary 7.4.2 (with
$\lvert A\rvert=\lvert B\rvert$) there is a perfect matching.

**15.** *Strategy: rewrite the defect formula algebraically.*

By Theorem 7.5.3, $\alpha'=\lvert A\rvert-\max_{S}(\lvert S\rvert-\lvert N(S)\rvert)$. Since
$\lvert A\rvert$ is constant and $-\max_S f(S)=\min_S(-f(S))$,
$$\alpha'=\min_{S\subseteq A}\Bigl(\lvert A\rvert-\bigl(\lvert S\rvert-\lvert N(S)\rvert\bigr)\Bigr)
=\min_{S\subseteq A}\bigl(\lvert A\rvert-\lvert S\rvert+\lvert N(S)\rvert\bigr).$$

Check on Problem 6 (here $\lvert A\rvert=4$): $S=\{a_1,a_2,a_3\}$ gives $4-3+2=3$; $S=A$ gives
$4-4+4=4$; $S=\{a_4\}$ gives $4-1+3=6$; the minimum is $3$, matching $\alpha'=3$. Intuitively
$\lvert A\rvert-\lvert S\rvert+\lvert N(S)\rvert$ is the size of the cover "$(A\setminus S)\cup N(S)$",
and the minimum over $S$ is $\tau(G)$.

**16.** *Strategy: use the $1$-factorisation of Corollary 7.5.2.*

By Corollary 7.5.2 the edge set splits into $k$ perfect matchings $M_1,\dots,M_k$. They are pairwise
distinct (they partition a non-empty edge set and $k\ge1$), so there are at least $k$ perfect matchings.
Given an edge $e$, it lies in exactly one class $M_i$ of the partition, and $M_i$ is perfect; hence every
edge lies in some perfect matching.

**17.** *Strategy: unit-capacity network, integral flow, and a careful reading of the minimum cut.*

Given bipartite $G$ with sides $A,B$, build $N$: arcs $s\to a$ of capacity $1$ for $a\in A$; arcs $a\to b$
of capacity $1$ for each edge $ab\in E$; arcs $b\to t$ of capacity $1$ for $b\in B$.

*Flows are matchings.* Let $f$ be an integral feasible flow. The set
$M_f=\{ab\in E: f(a,b)=1\}$ is a matching: the capacity-$1$ arc $s\to a$ forces at most one unit out of
$a$, and $b\to t$ at most one unit into $t$ from $b$. Conversely a matching $M$ gives the flow $f=1$ on
$s\to a$, $a\to b$, $b\to t$ for $ab\in M$ and $0$ elsewhere. Hence the maximum flow value equals
$\alpha'(G)$.

*The cut yields a cover.* Let $(S,T)$ be the minimum cut produced by residual reachability from a maximum
flow, so every arc from $S$ to $T$ is saturated (Theorem 7.9.1). Its capacity is
$$c(S,T)=\lvert A\setminus S\rvert+\bigl\lvert\{ab\in E: a\in S,\ b\notin S\}\bigr\rvert+\lvert B\cap S\rvert .$$
No edge joins $A\cap S$ to $B\setminus S$. Indeed, suppose $ab\in E$ with $a\in A\cap S$ and $b\in B\cap T$.
Since $a\in S$ it is reachable in the residual network, and since only the arc $s\to a$ enters $a$,
conservation gives $\sum_{b'}f(ab')=f(sa)\le1$. If $f(sa)=0$ then $f(ab)=0$, so the arc $a\to b$ has
residual capacity $1$ and $b$ would be reachable. If $f(sa)=1$, the single unit leaves $a$ along one arc
$a b'$; $a$ is reachable only through the backward arc $b'\to a$, so $b'\in S$ and $f(ab')=1$. Hence
$f(ab)=0$ again, and $b$ would be reachable. Both cases contradict $b\in T$.

Therefore $C=(A\setminus S)\cup(B\cap S)$ covers every edge: an edge with $a\in A\setminus S$ is covered by
$a$, and an edge with $a\in A\cap S$ has its other endpoint in $B\cap S$. Also every arc $s\to a$ with
$a\notin S$ is saturated, so $f(sa)=1$ for each of the $\lvert A\setminus S\rvert$ vertices of
$A\setminus S$; summing these units gives $\lvert A\setminus S\rvert\le\lvert f\rvert=\alpha'(G)$, and
similarly each $b\in B\cap S$ has $f(bt)=1$. Since $c(S,T)=\alpha'(G)$ and the last two groups of arcs are
all saturated while no edge crosses from $A\cap S$ to $B\setminus S$,
$$\lvert C\rvert=\lvert A\setminus S\rvert+\lvert B\cap S\rvert=c(S,T)=\alpha'(G).$$
So $\tau\le\alpha'$, and with $\alpha'\le\tau$ for all graphs, $\tau=\alpha'$ — König's theorem.

**18.** *Strategy: reduce rows, reduce columns, match zeros, and read off duals.*

Row minima are $1,2,4$; subtract them:
$$\begin{pmatrix}4&8&0\\8&1&0\\4&3&0\end{pmatrix}.$$
Column minima are $4,1,0$; subtract them:
$$\begin{pmatrix}0&7&0\\4&0&0\\0&2&0\end{pmatrix}.$$
The zeros $(1,1),(1,3),(2,2),(2,3),(3,1),(3,3)$ contain the perfect matching
$R_1C_3,\ R_2C_2,\ R_3C_1$. The corresponding assignment $1\to3$, $2\to2$, $3\to1$ costs
$1+3+8=12$.

*Certificate.* The row reductions contribute $u=(1,2,4)$ and, since the column minima are $4,1,0$, they
contribute $v=(4,1,0)$. Then $u_i+v_j\le c_{ij}$ on all nine cells (for instance $1+4=5\le5$,
$1+1=2\le9$, $1+0=1\le1$; $2+4=6\le10$, $2+1=3\le3$, $2+0=2\le2$; $4+4=8\le8$, $4+1=5\le7$,
$4+0=4\le4$), and the three chosen cells are tight: $1+0=1$, $2+1=3$, $4+4=8$. Moreover
$\sum u+\sum v=7+5=12$ equals the assignment cost, so by Lemma 7.7.2 both are optimal.

**19.** *Strategy: compare two assignments term by term.*

Let $c'_{ij}=c_{ij}+a_i$ where $a_i=c$ for one fixed row $i_0$ and $a_i=0$ otherwise. For any permutation
$\sigma$, $\sum_i c'_{i,\sigma(i)}=\sum_i c_{i,\sigma(i)}+\sum_i a_i$: every assignment cost increases by
the same constant $\sum_i a_i$. So the ordering of assignments by cost is unchanged and the set of
minimisers is the same. The same argument works for a column, and iterating it shows that adding any
row-constant or column-constant matrix leaves the optimal assignments unchanged — which is why the
Hungarian algorithm may reduce rows and columns freely.

**20.** *Strategy: induction on the number of arcs carrying positive flow.*

If $f\equiv0$ there is nothing to prove. Otherwise pick an arc with $f>0$. Walk backwards from it: if the
current vertex $u$ is internal, conservation gives
$\sum_{\text{into }u}f=\sum_{\text{out of }u}f>0$, so some arc enters $u$ with positive flow, and the walk
continues. Since $V$ is finite, either the walk revisits a vertex — producing a directed cycle $C$, every
arc of which carries positive flow — or it terminates at $s$ (it cannot terminate at an internal vertex,
by the conservation just used, nor at $t$, which is never reached backwards from an arc leaving it with
positive flow unless a cycle closes first).

*Cycle case.* Put $\delta=\min_{e\in C}f(e)>0$ and subtract $\delta$ around $C$. Every vertex of $C$ loses
as much as it gains, so conservation is preserved, capacities are respected ($f-\delta\ge0$), and at least
one arc becomes $0$.

*Path case.* From the arc we started with, extend the walk forward: an internal vertex with positive inflow
has positive outflow, so we can continue until we reach $t$ or revisit a vertex (in which case a cycle
closes and we extract it first). This produces an $s$–$t$ path $P$ with $f>0$ on all its arcs. Put
$\delta=\min_{e\in P}f(e)>0$ and subtract $\delta$ along $P$; feasibility is preserved, the value drops by
$\delta$, and at least one arc of $P$ becomes $0$.

In both cases the number of arcs with positive flow strictly decreases, so after finitely many steps $f$ is
written as a sum of path flows and cycle flows, each with its own non-negative value. If $f$ is integral,
all the extracted values are positive integers.

**21.** *Strategy: push flow until the residual network disconnects $s$ from $t$, then read the cut.*

Push $2$ along $s\to a\to t$ (bottleneck $\min(3,2)=2$), then $1$ along $s\to b\to t$
($\min(2,3)=1$), then $1$ along $s\to a\to b\to t$ ($\min(1,1,2)=1$). Total flow: $sa=3$, $ab=1$, $at=2$,
$sb=1$, $bt=2$, value $5$. Check $a$: in $3$, out $1+2=3$; $b$: in $1+1=2$, out $2$.

The cut $S=\{s,a,b\}$ has capacity $c(at)+c(bt)=2+3=5$, equal to the flow value, so by Theorem 7.9.1 both
are optimal: max flow $=5=$ min cut.

**22.** *Strategy: make every augmenting path carry exactly one unit, and make all paths disjoint.*

Take $k$ internally disjoint paths $s\to u_i\to t$ with all capacities equal to $1$ (vertices $u_1,\dots,u_k$).
Every feasible flow has value at most $k$ (the cut $\{s\}$ has capacity $k$), and sending $1$ along each
path achieves $k$, so $\lvert f^*\rvert=k$. Every augmenting path has bottleneck $1$ and saturates a
whole path, so Ford–Fulkerson performs exactly $k$ augmentations, whatever order it chooses. With
$n=2+k$ vertices this shows that the bound of Theorem 7.10.2 is attained, and, since $k$ is encoded in
unary here, it also illustrates why the bound is not polynomial in the input size when capacities are
large.

**23.** *Strategy: compute a maximum flow, then perform residual reachability.*

The total capacity into $t$ is $c(at)+c(bt)=3+1=4$, so no flow exceeds $4$. The flow $sa=3$, $at=3$,
$sb=1$, $bt=1$, $ab=0$ is feasible (at $b$: in $1$, out $1$) and has value $4$; so the maximum value is
$4$.

Residual capacities: $sa:0$, $sb:1$, $at:0$, $bt:0$, $ab:2$. Reachable from $s$: $s$, then $b$ (residual
$1$); from $b$ nothing is reachable ($bt$ residual $0$; the backward arc $b\to a$ has capacity
$f(ab)=0$). Hence $S=\{s,b\}$, $T=\{a,t\}$ and
$$c(S,T)=c(sa)+c(bt)=3+1=4,$$
in agreement with the flow value. Note that the minimum cut is not $\{s\}$ (capacity $5$) — the bottleneck
is the arc $bt$, not the source.

**24.** *Strategy: model as a bipartite matching and apply the defect formula.*

Jobs $J_1..J_4$ on one side, machines $M_1,M_2,M_3$ on the other, with edges
$J_1M_1,\ J_2M_1,\ J_2M_2,\ J_3M_2,\ J_4M_2,\ J_4M_3$. A schedule with three jobs:
$J_1M_1$, $J_3M_2$, $J_4M_3$ — and $J_2$ cannot be added, since its machines are taken. So the maximum is
$3$, which is also forced by Hall: for $S=\{J_1,J_2,J_3\}$ we have $N(S)=\{M_1,M_2\}$ and
$\lvert N(S)\rvert=2<3$, a deficient set. The defect formula gives
$\alpha'=4-\max_S(\lvert S\rvert-\lvert N(S)\rvert)=4-1=3$, matching the construction.

## Advanced

**25.** *Strategy: reduce to Hall's theorem by adding dummy vertices.*

*($\Leftarrow$)* Add $\lvert A\rvert-k$ new vertices to $B$, each adjacent to all of $A$, forming $G^*$.
For $S\subseteq A$ the new neighbourhood has size $\lvert N_G(S)\rvert+(\lvert A\rvert-k)\ge\lvert S\rvert$
by hypothesis, so Hall's condition holds in $G^*$ and Theorem 7.4.1 gives a matching $M^*$ saturating $A$.
$M^*$ has $\lvert A\rvert$ edges and at most $\lvert A\rvert-k$ of them use new vertices (there are only
that many), so at least $k$ edges lie inside $G$.

*($\Rightarrow$)* Suppose $M$ is a matching with $\lvert M\rvert\ge k$ and let $S\subseteq A$. At most
$\lvert A\rvert-\lvert M\rvert\le\lvert A\rvert-k$ vertices of $A$ are unmatched by $M$, and the vertices
of $S$ that are matched go injectively into $N(S)$. Hence
$\lvert N(S)\rvert\ge\lvert S\rvert-(\lvert A\rvert-k)$, as claimed.

**26.** *Strategy: the endpoints of a maximal matching form a cover; a union of triangles attains the
ratio.*

Let $M$ be maximal. By maximality every edge has at least one endpoint saturated by $M$, so the set $C$ of
saturated vertices is a vertex cover of size $2\lvert M\rvert\le2\alpha'(G)$. Therefore
$\tau(G)\le2\alpha'(G)$.

Sharpness: for $k$ disjoint triangles, each triangle contributes $\alpha'=1$ (any single edge) and
$\tau=2$ (two vertices cover all three edges), so $\alpha'=k$ and $\tau=2k$; the ratio is exactly $2$. Since
$k$ is arbitrary, no constant $c<2$ can satisfy $\tau\le c\,\alpha'$ for all graphs.

**27.** *Strategy: unit capacities turn max-flow min-cut into edge Menger.*

Give every arc capacity $1$ (replace parallel arcs by their multiplicity). Let $\nu$ be the maximum flow
value.

*Every family of arc-disjoint paths is bounded by every cut*: each path must use at least one arc of any
$s$–$t$ cut, and distinct paths use distinct arcs, so the number of paths is at most the cut capacity.
Hence $\#$paths $\le\lambda(N)$.

*Conversely*, let $f$ be an integral maximum flow, which exists by Theorem 7.10.2. By the decomposition of
Problem 20, $f$ is a sum of flows on $s$–$t$ paths and on cycles; cycle flows use arcs unnecessarily, so
delete them. The remaining path flows have integer values and the total flow on each arc is at most $1$,
so the paths carrying flow are pairwise arc-disjoint, and there are $\nu$ of them (each path carrying at
least one unit). Therefore $\#$paths $\ge\nu=\lambda(N)$ by Theorem 7.9.1.

Together: the maximum number of arc-disjoint $s$–$t$ paths equals the minimum number of arcs whose
deletion disconnects $s$ from $t$.

**28.** *Strategy: count augmentations by the matching size, not by the general $O(VE)$ bound.*

In the network of Remark 7.9.3 every capacity is $1$, so every augmentation has $\delta=1$ and raises the
flow value — hence the matching size — by exactly one. The matching size is at most $n$, so there are at
most $n$ augmentations. Each augmentation is one breadth-first search on a graph with
$V=n+n+2=O(n)$ vertices and $E=m+2n=O(m+n)$ arcs, costing $O(m+n)$. Total: $O\bigl(n(m+n)\bigr)$.

The augmenting paths found are exactly the directed paths of Algorithm 7.3.1: non-matching arcs run
$s\to A\to B\to t$ and matching arcs supply the backward steps $B\to A$ of the residual network (a
matching arc $a b$ carrying flow $1$ has residual capacity $1$ in the direction $b\to a$). Since BFS
finds shortest paths, this is the shortest-augmenting-path algorithm, which is precisely Algorithm 7.3.1
run in rounds.

The general bound $O(VE^2)$ inserted into these values would give $O\bigl(n(m+n)^2\bigr)$, weaker by a
factor $m+n$; the general bound ignores that here every augmentation increases the value by $1$ and the
number of augmentations is bounded by the matching size.

**29.** *Strategy: a greedy construction for (a); a perturbation along a cycle for (b).*

(a) *Northwest corner.* Set $i=j=1$, $r=a_1$, $s=b_1$. While $i\le p$ and $j\le q$: put
$x_{ij}=\min(r,s)$; if $r=s$ move to $(i+1,j+1)$, if $r<s$ move to $(i+1,j)$ with $s\leftarrow s-r$, if
$r>s$ move to $(i,j+1)$ with $r\leftarrow r-s$. Every step fills a row or a column completely, so the
process ends after at most $p+q-1$ steps, all row sums equal $a_i$ and all column sums equal $b_j$, and
$\sum a_i=\sum b_j$ guarantees that rows and columns are exhausted simultaneously. Hence a feasible
solution exists.

(b) Suppose a feasible solution $x$ has more than $p+q-1$ positive entries. Consider the bipartite graph
$H$ on the $p+q$ suppliers and customers with an edge for each positive $x_{ij}$; it has more than
$p+q-1$ edges, hence contains a cycle $i_1j_1i_2j_2\cdots i_rj_ri_1$ (with distinct vertices along the
cycle, $r\ge2$). Define $x^+$ by adding $\varepsilon$ to $x_{i_tj_t}$ and subtracting $\varepsilon$ from
$x_{i_{t+1}j_t}$ for each $t$ (indices mod $r$), and $x^-$ by the opposite signs. Along the cycle every
supplier row and every customer column gains one $\varepsilon$ and loses one $\varepsilon$, so all row
and column sums are preserved. For $\varepsilon$ small enough, all entries of both $x^+$ and $x^-$ are
non-negative (the entries changed are the positive ones along the cycle), and
$x=\tfrac12(x^++x^-)$ with $x^+\ne x^-$. A point that is the midpoint of two distinct feasible points is
not an extreme point. Hence every vertex of the feasible polytope has at most $p+q-1$ positive entries.

**30.** *Strategy: expand the definition of the permanent.*

$$\operatorname{per}(M)=\sum_{\sigma\in S_n}\prod_{i=1}^{n}m_{i,\sigma(i)} .$$
Every product is $0$ or $1$, and it equals $1$ exactly when $m_{i,\sigma(i)}=1$ for all $i$, i.e. when
$\{a_ib_{\sigma(i)}: i=1,\dots,n\}$ is a perfect matching. Distinct permutations give distinct matchings,
and every perfect matching arises from exactly one permutation. Hence
$\#\{\text{perfect matchings}\}=\operatorname{per}(M)$.

The permanent looks like the determinant but has no signs, hence no row-reduction algorithm: computing it
is $\#$P-complete (Valiant, 1979), so no polynomial-time algorithm is known (and none exists unless
$\mathrm{FP}=\#\mathrm{P}$). Deciding whether a perfect matching exists is a different question — it asks
only whether $\operatorname{per}(M)>0$ — and Hall's theorem plus Algorithm 7.3.1 answers it in polynomial
time. This is the standard example of a decision problem in P whose counting version is hard.

**31.** *Strategy: the two inequalities of weak duality, with equality only on tight edges.*

Let $\sigma$ be a permutation and $(u,v)$ dual feasible. Summing $u_i+v_{\sigma(i)}\le c_{i,\sigma(i)}$
gives $\sum_i u_i+\sum_j v_j\le\sum_i c_{i,\sigma(i)}$, with equality **if and only if** every one of the
$n$ summed inequalities is an equality, i.e. every edge $i\sigma(i)$ is tight.

Consequently: if $\sigma$ and $(u,v)$ are both optimal, the two objective values are equal, so every used
edge is tight. Conversely, if $\sigma$ uses only tight edges and $(u,v)$ is dual feasible, then the two
objective values coincide and, by weak duality, each is optimal (Lemma 7.7.2). This is precisely
complementary slackness for the assignment problem, and it is the invariant the Hungarian algorithm
maintains: it keeps $(u,v)$ dual feasible and searches for a perfect matching inside the equality graph.

## Challenge

**32.** *Strategy: the cut capacity dominates the size of a deficient set.*

Build the unit-capacity network of Remark 7.9.3 and let $\nu$ be the maximum flow value. If Hall's
condition fails, then no matching saturates $A$, so $\nu<\lvert A\rvert$. Let $(S,T)$ be a minimum cut
with $s\in S$, $t\in T$ and $\nu=c(S,T)$. Put $X=A\cap S$. The arcs crossing the cut are
$$s\to a\ (a\in A\setminus S),\qquad a\to b\ (a\in X,\ b\in B\setminus S),\qquad b\to t\ (b\in B\cap S),$$
so
$$c(S,T)=\lvert A\setminus X\rvert+\bigl\lvert E(X,B\setminus S)\bigr\rvert+\lvert B\cap S\rvert .$$
Every neighbour of $X$ lies in $(B\setminus S)\cup(B\cap S)$, and
$\lvert E(X,B\setminus S)\bigr\rvert\ge\lvert N(X)\setminus S\rvert$, so
$$c(S,T)\ \ge\ \lvert A\rvert-\lvert X\rvert+\lvert N(X)\setminus S\rvert+\lvert B\cap S\rvert
\ \ge\ \lvert A\rvert-\lvert X\rvert+\lvert N(X)\rvert,$$
where the last step uses
$\lvert N(X)\setminus S\rvert+\lvert B\cap S\rvert\ge\lvert N(X)\cap(B\setminus S)\rvert+\lvert N(X)\cap S\rvert=\lvert N(X)\rvert$.
Since $c(S,T)=\nu<\lvert A\rvert$, we get $\lvert N(X)\rvert<\lvert X\rvert$: the set $X$ is deficient.
Taking the contrapositive, Hall's condition implies $\nu=\lvert A\rvert$, i.e. a matching saturating $A$.

**33.** *Strategy: count permutations with no fixed point by inclusion–exclusion.*

Perfect matchings of $K_{n,n}$ are permutations $\sigma$. Fix the perfect matching
$M_0=\{a_ib_i\}$; a perfect matching avoids $M_0$ exactly when $\sigma(i)\ne i$ for all $i$ — a
derangement. Let $A_i=\{\sigma:\sigma(i)=i\}$. For a set $I$ of $k$ indices, the permutations fixing all
of $I$ are the $(n-k)!$ permutations of the rest, so $\lvert\cap_{i\in I}A_i\rvert=(n-k)!$, and there are
$\binom{n}{k}$ such sets. Inclusion–exclusion gives
$$D_n=\sum_{k=0}^{n}(-1)^k\binom{n}{k}(n-k)!=n!\sum_{k=0}^{n}\frac{(-1)^k}{k!}.$$
For $n=3$: $6(1-1+\tfrac12-\tfrac16)=2$; for $n=4$: $24(1-1+\tfrac12-\tfrac16+\tfrac1{24})=9$. Both agree with
a direct count.

**34.** *Strategy: contract the matching and use acyclicity to find a degree-$1$ vertex.*

Let $M=\{a_ib_i: i=1,\dots,n\}$ be the unique perfect matching, with $A=\{a_1,\dots,a_n\}$ and
$B=\{b_1,\dots,b_n\}$. Every edge not in $M$ has the form $a_ib_j$ with $i\ne j$. Build a digraph $D$ on
$\{1,\dots,n\}$ with an arc $i\to j$ for every such edge.

If $D$ contained a directed cycle $i_1\to i_2\to\cdots\to i_r\to i_1$, then
$\{a_{i_1}b_{i_2},a_{i_2}b_{i_3},\dots,a_{i_r}b_{i_1}\}$ would be a cycle of $G$ alternating between
non-matching edges and edges of $M$, and swapping $M$ along it would produce a *second* perfect matching,
contradicting uniqueness. Hence $D$ is acyclic, so $D$ has a sink $i^*$ (a vertex with no outgoing arc).
By construction $a_{i^*}$ is adjacent only to $b_{i^*}$: any other edge $a_{i^*}b_j$ with $j\ne i^*$
would be an arc out of $i^*$. Hence $\deg(a_{i^*})=1$ and the edge $a_{i^*}b_{i^*}\in M$ is a bridge (its
deletion isolates $a_{i^*}$). So the unique perfect matching contains a bridge.

**35.** *Strategy: split vertices, then quote max-flow min-cut.*

Assume $s$ and $t$ are not adjacent. Build a network $N$: replace each $v\in V\setminus\{s,t\}$ by
$v^-$ and $v^+$ joined by an arc $v^-\to v^+$ of capacity $1$; replace each arc $uv$ of $D$ by
$u^{\text{out}}\to v^{\text{in}}$ of capacity $\infty$ (any capacity exceeding $\lvert V\rvert$ will do),
where $s^{\text{out}}=s$, $t^{\text{in}}=t$ and the split vertices supply $v^{\text{out}}=v^+$,
$v^{\text{in}}=v^-$.

*Paths correspond.* An $s$–$t$ path in $N$ alternates split arcs $v^-\to v^+$ with original arcs, and
uses each split arc of a vertex at most once. Conversely an $s$–$t$ path of $D$ lifts to a path in $N$ that
uses exactly the split arcs of its internal vertices. Two paths of $N$ that are arc-disjoint use distinct
split arcs, so the corresponding paths of $D$ share no internal vertex; and internally vertex-disjoint
paths of $D$ give arc-disjoint paths of $N$. Since all capacities are integral, the maximum flow $\nu$
equals the maximum number of arc-disjoint $s$–$t$ paths in $N$, which equals the maximum number of
internally vertex-disjoint $s$–$t$ paths in $D$.

*A vertex cut gives a cut of the same capacity.* If $X\subseteq V\setminus\{s,t\}$ separates $s$ from $t$
in $D$, deleting the arcs $v^-\to v^+$ for $v\in X$ destroys all $s$–$t$ paths in $N$; the set of heads of
those arcs is an $S$ with $s\in S$, $t\notin S$ and $c(S,T)=\lvert X\rvert$. So $\nu\le\kappa$, where
$\kappa$ is the minimum size of such a vertex set.

*A minimum cut gives a vertex cut.* Take a minimum cut $(S,T)$ of $N$ of capacity $\nu<\infty$. It cannot
contain an infinite-capacity arc $u^{\text{out}}\to v^{\text{in}}$, so all arcs from $S$ to $T$ are split
arcs $v^-\to v^+$. Let $X=\{v: v^-\in S,\ v^+\in T\}$. Removing $X$ from $D$ destroys every $s$–$t$ path:
a surviving path would lift to a path of $N$ avoiding all split arcs from $S$ to $T$, hence lying in $S$
up to $t\notin S$ — impossible. And $\lvert X\rvert=\nu$, since each split arc of the cut corresponds to
exactly one vertex. So $\kappa\le\nu$.

Therefore $\nu=\kappa$: maximum number of internally vertex-disjoint $s$–$t$ paths equals the minimum size
of a vertex set separating them.

**36.** *Strategy: read $M$ as the adjacency matrix of a $k$-regular bipartite graph and apply the
$1$-factorisation.*

Let $G$ be the bipartite graph with sides $A=\{a_1,\dots,a_n\}$, $B=\{b_1,\dots,b_n\}$ and $a_ib_j\in E$
iff $m_{ij}=1$. Row sums are $k$, so every $a_i$ has degree $k$; column sums are $k$, so every $b_j$ has
degree $k$. Thus $G$ is $k$-regular bipartite, and by Corollary 7.5.2 its edges split into $k$ perfect
matchings $M_1,\dots,M_k$.

Each perfect matching $M_t$ is the graph of a permutation $\sigma_t$: $M_t=\{a_ib_{\sigma_t(i)}: i\}$,
because every $a_i$ is matched exactly once and every $b_j$ is used exactly once. Let $P_t$ be the
permutation matrix of $\sigma_t$, i.e. $(P_t)_{ij}=1$ iff $j=\sigma_t(i)$. Then
$m_{ij}=\lvert\{t: j=\sigma_t(i)\}\rvert=\sum_t (P_t)_{ij}$, since $a_ib_j$ belongs to exactly one of the
$k$ matchings when it is an edge and to none otherwise. Hence $M=P_1+\cdots+P_k$ with each $P_t$ a
permutation matrix.

Induction on $k$ gives the same result (extract one perfect matching, subtract its permutation matrix,
and repeat on the remaining $(k-1)$-regular graph), which is exactly Corollary 7.5.2 applied to matrices.
