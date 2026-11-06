# The Pigeonhole Principle — Solutions

> [The Pigeonhole Principle](README.md) · Solutions to the 36 problems in [exercises.md](exercises.md)

Each solution names the objects and the boxes, counts both, states which form of the principle is used, and — where the problem asks for sharpness — exhibits the extremal configuration.

## Beginner

**1.** *Objects: $13$ people. Boxes: the $12$ months. Form: basic.*

Since $13 > 12$, two people fall in the same month.

$12$ cannot be replaced by a smaller number: with exactly one person born in each month the boxes each hold one object, so no repetition is forced. The number $13$ is exactly $k(m-1)+1$ with $k = 12$, $m = 2$.

**2.** *Objects: $367$ people. Boxes: the $366$ possible birthdays. Form: basic.*

There are $366$ dates, because $29$ February is a possible birthday. Since $367 > 366$, two people share a date.

$366$ is the right count because a person born on $29$ February occupies a box that the other $365$ dates do not cover; using $365$ would give a correct but weaker statement. Sharpness: $366$ people, one born on each date, avoid a repetition.

**3.** (a) *Objects: $100$ pigeons. Boxes: $9$ holes. Form: generalised.*

$$\left\lceil \frac{100}{9}\right\rceil = 12,$$
because $9\cdot 11 = 99 < 100$. So some hole contains at least $12$ pigeons.

(b) The threshold form with $k = 9$, $m = 12$ gives
$$N = k(m-1)+1 = 9\cdot 11 + 1 = 100 .$$
So $100$ pigeons are necessary as well as sufficient: $99 = 9\cdot 11$ pigeons can be distributed with exactly $11$ in each hole, and then no hole has $12$.

*Check.* The same computation with $m=2$ gives $9\cdot1+1 = 10$ pigeons to force a pair; $9$ pigeons, one per hole, avoid it. ✓

**4.** *Objects: socks. Boxes: $4$ colours. Form: threshold with $m=2$.*

$4\cdot 1 + 1 = 5$ socks force two of the same colour, since $\lceil 5/4\rceil = 2$.

*Necessity.* Four socks, one of each colour, contain no pair. So $5$ is the smallest.

*Check.* With $1$ colour, $2$ socks force a pair; with $2$ colours, $3$ socks. The formula gives $1+1 = 2$ and $2+1 = 3$. ✓

**5.** *Objects: cards. Boxes: $4$ suits.*

Two of the same suit: $4\cdot 1+1 = 5$ cards, since $\lceil 5/4\rceil = 2$.

Three of the same suit: $4\cdot 2+1 = 9$ cards, since $\lceil 9/4\rceil = 3$.

*Necessity.* Four cards can be one of each suit; eight cards can be two of each suit. Both avoid the respective conclusion, so the numbers are optimal. (The deck has $13$ cards per suit, so these configurations exist.)

**6.** *Objects: $11$ integers. Boxes: the $10$ final digits.*

Two of the eleven share a final digit.

*Optimality.* The ten integers $0,1,\dots,9$ have ten distinct final digits, so $10$ do not suffice; hence $11$ is the smallest.

**7.** *Objects: $4$ integers. Boxes: the $3$ residues modulo $3$.*

Two have the same residue, hence a difference divisible by $3$.

*Necessity.* The three integers $1,2,3$ have residues $1,2,0$; their pairwise differences are $1,1,2$, none divisible by $3$.

**8.** *Objects: $6$ integers. Boxes: the $5$ residues modulo $5$.*

Two share a residue mod $5$, so their difference is divisible by $5$.

*Optimality.* $0,1,2,3,4$ have pairwise differences with absolute value in $\{1,2,3,4\}$, none divisible by $5$.

**9.** *Objects: $19$ two-digit numbers. Boxes: the $18$ possible digit sums $1,2,\dots,18$.*

A two-digit number $10a+b$ has digit sum $a+b$ with $1 \le a \le 9$ and $0\le b\le 9$, so the sum lies between $1$ and $18$, and every value in that range occurs. With $19$ numbers in $18$ boxes, two share a digit sum.

*Optimality.* Here are $18$ two-digit numbers with pairwise distinct digit sums:
$$10,11,12,13,14,15,16,17,18,19,29,39,49,59,69,79,89,99,$$
with digit sums $1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18$. So $18$ numbers do not suffice.

**10.** *Objects: $5$ integers. Boxes: the four classes $\{0\},\{1,6\},\{2,5\},\{3,4\}$ of residues modulo $7$ up to sign.*

If two integers lie in the same class, their residues are either equal (difference divisible by $7$) or opposite (sum divisible by $7$). With $5$ integers in $4$ classes, this happens.

*Necessity.* The integers $1,2,3,7$ have residues $1,2,3,0$. Their pairwise sums are $3,4,8,5,9,10$, and modulo $7$ these are $3,4,1,5,2,3$; none is $0$. So $4$ integers do not suffice. (Equivalently: take one residue from each class, choosing $0,1,2,3$, and check that no two are equal or opposite.)

**11.** *Objects: $25$ students. Boxes: $8$ groups. Form: generalised.*

$$\left\lceil \frac{25}{8}\right\rceil = 4,$$
since $8\cdot 3 = 24 < 25$. So some group has at least $4$ students.

*Sharpness.* $24$ students in $8$ groups of $3$ have no group of $4$.

**12.** *Objects: $5$ points. Boxes: the four $1\times 1$ squares obtained by bisecting the sides.*

Two points lie in the same unit square, whose diameter is $\sqrt{1^2+1^2} = \sqrt2$.

*Sharpness.* The four corners of the $2\times 2$ square are at mutual distances $2, 2, 2, 2, 2\sqrt2$, all strictly greater than $\sqrt2$. So $4$ points can avoid the conclusion, and $5$ is optimal.

## Intermediate

**13.** *Objects: the chosen integers. Boxes: their odd parts.*

Write each chosen integer as $a = 2^{v}m$ with $m$ odd. Since $a \le 3n$, the odd part $m$ is an odd number not exceeding $3n$; there are
$$\left\lceil \frac{3n}{2}\right\rceil$$
such odd numbers (one for each odd integer in $\{1,\dots,3n\}$).

The number of chosen integers is $\lceil 3n/2\rceil + 1$, which exceeds the number of boxes, so two integers share an odd part: $a = 2^rm$, $b = 2^sm$. If $r<s$ then $a \mid b$; if $s<r$ then $b \mid a$.

*Sharpness.* Let $t = \lfloor 3n/2\rfloor + 1$ and consider the top segment $\{t, t+1, \dots, 3n\}$, whose size is
$$3n - t + 1 = 3n - \left\lfloor \tfrac{3n}{2}\right\rfloor = \left\lceil \tfrac{3n}{2}\right\rceil .$$
No member divides another, because $2t > 3n$: indeed $2t = 2\lfloor 3n/2\rfloor + 2 > 3n$. Hence $\lceil 3n/2\rceil$ integers can avoid a divisible pair, and the bound is sharp.

*Check.* $n=2$: the bound is $\lceil 3\rceil + 1 = 4$ integers from $\{1,\dots,6\}$. Any $4$ of them contain a divisible pair (checked in the tutorial's Example 9.6), and $\{4,5,6\}$ of size $3 = \lceil 3n/2\rceil$ does not. ✓ $n=3$: bound $\lceil 4.5\rceil + 1 = 6$ from $\{1,\dots,9\}$; sharp example $\{5,6,7,8,9\}$ of size $5$. ✓

**14.** (a) *Objects: the chosen integers. Boxes: the $n$ pairs $\{1,2\},\{3,4\},\dots,\{2n-1,2n\}$.*

Two of the $n+1$ integers lie in the same pair, hence are consecutive, hence coprime: if $d$ divides both $k$ and $k+1$ then $d \mid 1$.

(b) The even numbers $\{2,4,\dots,2n\}$ have size $n$ and share the common divisor $2$, so no two of them are coprime. By (a), any $n+1$ elements contain a coprime pair. Hence the maximum size is exactly $n$.

**15.** *Objects: the $n+1$ partial sums $s_0, s_1, \dots, s_n$ with $s_0 = 0$ and $s_j = a_1+\cdots+a_j$. Boxes: the $n$ residues modulo $n$.*

Two partial sums, say $s_i$ and $s_j$ with $i<j$, share a residue, so $s_j - s_i = a_{i+1}+\cdots+a_j$ is divisible by $n$: a block of consecutive terms has sum divisible by $n$.

*Sharpness.* Take $n-1$ terms, all equal to $1$. The partial sums are $1,2,\dots,n-1$, none divisible by $n$, and every block sum is a positive integer less than $n$. So $n-1$ terms do not suffice.

*Check.* $n = 4$, sequence $3, 1, 4, 2$: partial sums $0,3,4,8,10$; residues $0,3,0,0,2$; $s_0 = s_2 = 0$ gives the block $3+1 = 4$ ✓.

**16.** *Objects: $5$ integers. Boxes: the $3$ residue classes modulo $3$, with class sizes $n_0,n_1,n_2$ and $n_0+n_1+n_2 = 5$.*

If some class has at least $3$ members, three of them have sum $3r \equiv 0 \pmod 3$.

Otherwise all class sizes are at most $2$, and since they sum to $5$ they must be $2,2,1$ in some order. Take one integer from each class: their residues are $0,1,2$, whose sum is $3 \equiv 0 \pmod 3$.

*Necessity of $5$.* Four integers: $\{1,1,2,2\}$ has $3$-subsets with sums $1+1+2 = 4$ and $1+2+2 = 5$, neither divisible by $3$. Three integers: $\{1,1,2\}$ has only the total $4$, not divisible by $3$.

**17.** *Objects: $5$ points. Boxes: the four equilateral triangles of side $1/2$ obtained by joining the midpoints of the sides.*

Two points lie in the same small triangle, whose diameter is $1/2$.

*Sharpness.* Take the three vertices and the centre of the triangle. The centre is at distance $1/\sqrt3 \approx 0.577 > 1/2$ from each vertex, and the vertices are $1$ apart. So four points can have all pairwise distances exceeding $1/2$.

**18.** *Objects: $9$ lattice points. Boxes: the $8$ parity classes of $\mathbb{Z}^3$, indexed by the parities of the three coordinates.*

Two points lie in the same class, so their three coordinate differences are all even, and the midpoint has integer coordinates.

*Sharpness.* The eight points $(0,0,0)$, $(1,0,0)$, $(0,1,0)$, $(1,1,0)$, $(0,0,1)$, $(1,0,1)$, $(0,1,1)$, $(1,1,1)$ are one per class. Any two differ by an odd amount in at least one coordinate, so no pair has an integral midpoint.

**19.** *Objects: $7$ integers. Boxes: the six classes $\{0\},\{5\},\{1,9\},\{2,8\},\{3,7\},\{4,6\}$ of residues modulo $10$ up to sign.*

Each class consists of a residue and its negative modulo $10$. Two integers in the same class either have equal residues — difference divisible by $10$ — or opposite residues — sum divisible by $10$. With $7$ objects in $6$ boxes, this occurs.

*Necessity.* The six integers $10,11,12,13,14,15$ have residues $0,1,2,3,4,5$. Their pairwise sums lie between $21$ and $29$ and their pairwise differences between $1$ and $5$; modulo $10$ these are never $0$. So $6$ integers can avoid the conclusion.

*Check.* Why six classes and not ten: the relation "$a \equiv \pm b \pmod{10}$" has the six orbits listed above. ✓

**20.** *Objects: $51$ numbers. Boxes: the $50$ pairs $\{1,2\},\{3,4\},\dots,\{99,100\}$.*

Two chosen numbers lie in the same pair and are therefore consecutive, hence coprime.

*Check.* The bound is optimal: the $50$ odd numbers have no consecutive pair. (They are not pairwise non-coprime — for instance $3$ and $9$ — so this only shows that the *consecutive* conclusion is sharp, not that the coprime conclusion is.)

**21.** *Objects: the five other people, viewed from a fixed person $P$. Boxes: "knows $P$" and "does not know $P$". Form: generalised with $k=2$.*

Fix a person $P$. The other five people split into those who know $P$ and those who do not. By the generalised principle with $5$ objects and $2$ boxes, one of these classes has at least $\lceil 5/2\rceil = 3$ members. Say three people $A,B,C$ all know $P$.

* If some two of $A,B,C$ know each other, those two together with $P$ form three mutual acquaintances.
* Otherwise $A,B,C$ are pairwise strangers, giving three mutual strangers.

The other case (three people who do not know $P$) is symmetric, with "know" and "do not know" interchanged.

*Sharpness.* Five people arranged in a cycle, where each knows exactly their two neighbours, contain no three mutual acquaintances and no three mutual strangers. (This is the statement $R(3,3) = 6$.)

**22.** *$10 = 3\cdot 3 + 1$, so the Erdős–Szekeres theorem with $r = s = 3$ applies: an increasing subsequence of length $4$ or a decreasing one of length $4$.*

For the sequence $4,9,1,8,2,7,3,6,5,10$, here are the run-length labels $(I_i,D_i)$:

| $i$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| $a_i$ | 4 | 9 | 1 | 8 | 2 | 7 | 3 | 6 | 5 | 10 |
| $I_i$ | 1 | 2 | 1 | 2 | 2 | 3 | 3 | 4 | 4 | 5 |
| $D_i$ | 1 | 1 | 2 | 2 | 3 | 3 | 4 | 4 | 5 | 1 |

The increasing subsequence $1, 2, 3, 5, 10$ has length $5$, so in particular there is one of length $4$. ✓

*Why the labels prove the theorem in general.* If all $I_i \le 3$ and all $D_i \le 3$, the $10$ labels would be distinct members of a $9$-element set, impossible. Distinctness is proved as in Theorem 7.10.1: for $i<j$, either $a_i<a_j$, which forces $I_j \ge I_i+1$, or $a_i>a_j$, which forces $D_j\ge D_i+1$.

**23.** *Three sharing a month.* Threshold form with $k = 12$, $m = 3$: $12\cdot 2 + 1 = 25$ people. With $24$ people, two per month, no month has three.

*Four sharing a month.* $12\cdot 3 + 1 = 37$ people. With $36$ people, three per month, no month has four.

*Check.* $\lceil 25/12\rceil = 3$ and $\lceil 37/12\rceil = 4$: $25/12 = 2.08\ldots$ and $37/12 = 3.08\ldots$. ✓

**24.** *Objects: $7$ points. Boxes: six rectangles of size $1\times 2$.*

Cut the $3\times 4$ rectangle into three horizontal strips of height $1$ and, within each strip, into two rectangles of width $2$. This gives $3\cdot 2 = 6$ pieces, each measuring $1\times 2$, with diameter $\sqrt{1^2+2^2} = \sqrt5$. With $7$ points in $6$ pieces, two are in the same piece, so their distance is at most $\sqrt5$.

*Why this partition.* A partition into pieces of small diameter is the only thing that matters; the number of pieces must be less than the number of points. Splitting the long side into two halves and the short side into three strips uses $3\cdot 2 = 6$ pieces, one fewer than $7$, and the pieces are as square-like as the integer dimensions allow.

## Advanced

**25.** (a) *Proof by contradiction.* Suppose $\lvert B_i\rvert \le \lceil N/k\rceil - 1$ for every $i$. For every real $x$ the ceiling satisfies $\lceil x\rceil - 1 < x$; applying this with $x = N/k$ gives $\lceil N/k\rceil - 1 < N/k$, and multiplying by $k>0$,
$$\sum_{i=1}^{k}\lvert B_i\rvert \le k\left(\left\lceil\frac Nk\right\rceil - 1\right) < k\cdot\frac Nk = N .$$
But the boxes are disjoint and cover $S$, so the sum is $\lvert S\rvert = N$ — a contradiction. $\square$

(b) Write $N = kq + r$ with $0 \le r < k$. Put $q+1$ objects in $r$ of the boxes and $q$ objects in the remaining $k-r$ boxes. The total is $r(q+1)+(k-r)q = kq + r = N$, and the largest box holds $q+1$ if $r>0$, else $q$; in both cases the maximum is $\lceil N/k\rceil$. So the bound is attained, not merely approached.

(c) Put $m-1$ objects in each of the $k$ boxes: the total is $k(m-1)$ and no box holds $m$. Hence the threshold $N > k(m-1)$ cannot be weakened to $N \ge k(m-1)$.

*Check.* $N=10$, $k=4$: $\lceil 2.5\rceil = 3$, attained by $3,3,2,2$ ✓. $N=8$, $k=4$: $\lceil 2\rceil = 2$, attained by $2,2,2,2$ ✓; and $k(m-1) = 4\cdot1 = 4$ objects can be spread as $1,1,1,1$ with no box holding $2$ ✓.

**26.** *Statement.* For $r,s\ge1$, every sequence $a_1,\dots,a_{rs+1}$ of distinct reals has an increasing subsequence of length $r+1$ or a decreasing subsequence of length $s+1$.

*Proof.* For each index $i$ let $I_i$ be the length of the longest increasing subsequence ending at $a_i$ and $D_i$ the length of the longest decreasing subsequence ending at $a_i$. Assume for contradiction that $I_i \le r$ and $D_i\le s$ for all $i$, so every label $(I_i,D_i)$ lies in the $rs$-element set $[r]\times[s]$.

The labels are pairwise distinct. Indeed, for $i<j$: if $a_i<a_j$, then a longest increasing subsequence ending at $a_i$, followed by $a_j$, is increasing, so $I_j \ge I_i + 1 > I_i$; if $a_i>a_j$ (equality is impossible, the terms being distinct), the same argument with decreasing subsequences gives $D_j \ge D_i+1 > D_i$. Either way the labels differ.

So $i \mapsto (I_i,D_i)$ injects an $(rs+1)$-element set into an $rs$-element set, contradicting the pigeonhole principle. $\square$

*Deduction.* With $r = s = n$ the statement reads: every sequence of $n^2+1$ distinct reals has an increasing or a decreasing subsequence of length $n+1$, i.e. a monotone subsequence of that length.

**27.** *Objects: the $N+1$ fractional parts $\{j\alpha\}$ for $j = 0,1,\dots,N$. Boxes: the $N$ half-open intervals $\left[\frac{i}{N},\frac{i+1}{N}\right)$ for $i = 0,\dots,N-1$.*

These intervals partition $[0,1)$, so two of the $N+1$ numbers lie in the same one, say $\{j\alpha\}$ and $\{k\alpha\}$ with $j<k$.

*Step 1: the size of the difference.* Two points of the same half-open interval of length $1/N$ differ by less than $1/N$ in absolute value. This is where the **strict** inequality comes from: if the difference equalled exactly $1/N$, the two points would be the two endpoints of the interval, but the right endpoint is excluded from a half-open interval. So $\lvert \{k\alpha\}-\{j\alpha\}\rvert < 1/N$.

*Step 2: removing the fractional parts.* We have $\{k\alpha\} - \{j\alpha\} = (k-j)\alpha - \bigl(\lfloor k\alpha\rfloor - \lfloor j\alpha\rfloor\bigr)$. Set $q = k - j$, which satisfies $1 \le q \le N$ because $0\le j<k\le N$, and $p = \lfloor k\alpha\rfloor-\lfloor j\alpha\rfloor \in \mathbb{Z}$. Then $\lvert q\alpha - p\rvert < 1/N$. $\square$

**28.** *Statement.* If infinitely many objects are placed in finitely many boxes, some box contains infinitely many.

*Proof.* Suppose every box contains only finitely many objects. A finite union of finite sets is finite — induction on the number of boxes, each step using that $\lvert B_1\cup\cdots\cup B_{r}\rvert \le \lvert B_1\rvert + \cdots + \lvert B_r\rvert$. Then there would be only finitely many objects in total, contradicting the hypothesis. $\square$

*Application: infinite monotone subsequence.* Call $i$ a **peak** if $a_i \ge a_j$ for all $j>i$.

* If infinitely many peaks exist, list them $i_1<i_2<\cdots$. Since $i_k$ is a peak, $a_{i_k} \ge a_{i_{k+1}}$, so $(a_{i_k})$ is an infinite non-increasing subsequence.
* If only finitely many peaks exist, choose $N$ beyond the last peak. Then no $i>N$ is a peak, so for each $i>N$ there is $j>i$ with $a_j>a_i$; starting at $N+1$ and iterating produces indices $i_1<i_2<\cdots$ with $a_{i_1}<a_{i_2}<\cdots$.

Each case gives an infinite monotone subsequence. $\square$ (Equivalently, split the indices into two boxes, "peak" and "not a peak"; the infinite pigeonhole principle puts infinitely many in one.)

*Why Erdős–Szekeres does not give this directly.* For each $n$ the finite theorem produces a monotone subsequence of length $n$, but the subsequence found for $n+1$ need not extend the one found for $n$. A diagonal argument would be needed to extract a nested chain, and no such chain is available in general — which is why the peak argument (or an equivalent compactness argument) is required.

**29.** (a) Let $x_1,\dots,x_t$ be real numbers with mean $\bar x = \frac1t\sum_i x_i$. If every $x_i < \bar x$ then $\sum_i x_i < t\bar x = \sum_i x_i$, a contradiction; hence $\max_i x_i \ge \bar x$.

Apply this to the box counts $b_1,\dots,b_k$ of a distribution of $N$ objects: their mean is $N/k$, so some $b_i \ge N/k$. Since $b_i$ is an integer, $b_i \ge \lceil N/k\rceil$ — the generalised pigeonhole principle.

(b) There are $\binom63 = 20$ triangles. For a fixed triangle, its three edges are all red or all blue with probability $2\cdot(1/2)^3 = 1/4$. By linearity of expectation, with $X$ the number of monochromatic triangles,
$$\mathbb{E}[X] = 20\cdot \tfrac14 = 5 .$$
Since the average over all $2^{15}$ colourings is $5$, some colouring has $X \ge 5$ and some has $X \le 5$.

*Check.* The distribution of $X$ over the $32\,768$ colourings has mean $5$; an exhaustive check shows the minimum is $2$ and the maximum $20$ (the two monochromatic colourings). The averaging argument proves the existence of colourings on both sides of $5$ without identifying them. ✓

**30.** *Well-definedness.* Adding a multiple of $M$ to $x$ changes $x$ by a multiple of every $m_i$, so the tuple $(x \bmod m_1,\dots,x\bmod m_k)$ is unchanged: $\Phi$ is a function on residue classes.

*Injectivity.* If $\Phi(x) = \Phi(y)$ then $x \equiv y \pmod{m_i}$ for every $i$, i.e. $m_i \mid (x-y)$. Each prime power dividing $M$ divides some $m_i$ (pairwise coprimality), hence divides $x-y$; so $M \mid (x-y)$ and $x\equiv y \pmod M$.

*Counting.* $\lvert\mathbb{Z}/M\mathbb{Z}\rvert = M$. By the product rule, $\lvert\prod_{i}\mathbb{Z}/m_i\mathbb{Z}\rvert = \prod_i m_i = M$.

An injective map between finite sets of equal cardinality is bijective (Section 5.3). Hence $\Phi$ is a bijection, which is exactly the Chinese remainder theorem: every tuple of residues is attained by exactly one class modulo $M$. $\square$

*The counting facts used.* (i) the cardinality of $\mathbb{Z}/n\mathbb{Z}$ is $n$; (ii) the product rule for the cardinality of a Cartesian product; (iii) the pigeonhole corollary that an injection between finite sets of equal size is a bijection.

*Check.* $m_1 = 3$, $m_2 = 5$, $M = 15$: the map is a bijection from $15$ classes to $3\cdot5 = 15$ pairs, and indeed $x = 7$ corresponds to $(1,2)$ and is the unique class with those residues. ✓

**31.** *Objects: the $2^{10} = 1024$ subsets of the ten numbers. Boxes: the possible values of the sum of a subset.*

The ten numbers are distinct two-digit numbers, so the largest possible sum is at most $99+98+\cdots+90 = 945$, and the smallest is $0$ (empty set). Thus there are at most $946$ possible sums.

Since $1024 > 946$, two distinct subsets $A \ne B$ have equal sums. Remove their intersection: the sets $A\setminus B$ and $B\setminus A$ are disjoint, and
$$\sum_{a\in A\setminus B} a = \sum_{a\in A}a - \sum_{a\in A\cap B}a = \sum_{b\in B}b - \sum_{a\in A\cap B}a = \sum_{b\in B\setminus A} b .$$
Neither is empty: if $A\setminus B = \varnothing$ then $A\subseteq B$ and the equal sums force $\sum_{b\in B\setminus A} b = 0$, impossible since all ten numbers are positive. So the two disjoint non-empty sets have equal sums. $\square$

*Where "distinct" is used.* It sharpens the maximum sum from the trivial $10\cdot 99 = 990$ to $945$; both are below $1023$, so the argument also works without distinctness. Its real role is to make the bound as strong as possible.

*Why two digits.* With three-digit numbers the maximum sum would be $999+\cdots+990 = 9945$, far more than $1023$ possible sums, and the pigeonhole gives nothing. So the argument depends on the numbers having few digits, i.e. on the sum range being smaller than the number of subsets.

## Challenge

**32.** *Objects and boxes: a two-stage argument.*

Fix a person $P$. The other $16$ people each correspond with $P$ about one of $3$ topics, so by the generalised principle some topic is used by at least
$$\left\lceil \frac{16}{3}\right\rceil = 6$$
of them. Say $P$ corresponds with $A_1,\dots,A_6$ on topic $T$.

Now consider the $\binom62 = 15$ pairs among $A_1,\dots,A_6$.

* If any pair corresponds on $T$, that pair together with $P$ is a triple all of whose letters are on $T$.
* Otherwise every pair corresponds on one of the remaining two topics. Colour each edge of $K_6$ with the topic used. By the $R(3,3)=6$ argument (Exercise 21), there are three of the $A_i$ pairwise corresponding on the same topic — and that topic is one of the two, so together with nothing else they already form the required triple (the three write to each other on the same topic).

Either way, three people correspond pairwise on the same topic. $\square$

*Check of the numbers.*$16 = 3\cdot 5+1$, so $6$ is forced: five people per topic is $3\cdot5 = 15 < 16$. ✓

**33.** Let $a_i$ be the number of problems solved on day $i$, for $i = 1,\dots,77$, so $a_i \ge 1$. Let $s_j = a_1+\cdots+a_j$ be the partial sums; these are strictly increasing positive integers.

*Bound on the total.* At most $12$ problems per week over $11$ weeks gives $s_{77}\le 132$.

*The shift trick.* Consider the $154$ integers
$$s_1,\dots,s_{77}, \quad s_1+21,\dots,s_{77}+21 .$$
All lie in $\{1,2,\dots,153\}$, since $s_{77}+21 \le 132+21 = 153$. With $154$ integers in $153$ slots, two are equal.

The $s_i$ are pairwise distinct and the $s_i+21$ are pairwise distinct, so the coincidence must be $s_i = s_j + 21$ with $j<i$. Then
$$s_i - s_j = a_{j+1}+\cdots+a_i = 21,$$
so on days $j+1$ through $i$ she solved exactly $21$ problems. $\square$

*Why $21$.* The argument needs $s_{77} + 21 \le 2\cdot 77 - 1 = 153$, i.e. $21 \le 153 - s_{77}$, and $s_{77}\le 132$ gives $21 \le 21$. So $21$ is the largest target this argument can reach with the given data; a target of $22$ would require $154$ numbers in $154$ slots and the pigeonhole would fail.

**34.** *Construction.* For $n\ge1$ consider the $n$ blocks
$$B_t = \bigl((t-1)n + n,\ (t-1)n + n - 1,\ \dots,\ (t-1)n + 1\bigr), \qquad t = 1,\dots,n,$$
so $B_t$ lists the $n$ numbers in $((t-1)n,\ tn]$ in decreasing order, and the concatenation $B_1B_2\cdots B_n$ has length $n^2$.

*No long increasing subsequence.* Every term of $B_t$ is at most $tn$, and every term of $B_{t'}$ with $t'>t$ is greater than $tn$. An increasing subsequence can take at most one term from each block, because within a block the terms decrease. Hence it has length at most $n$.

*No long decreasing subsequence.* A decreasing subsequence cannot move to a later block: every later term exceeds every earlier one. So it lies inside a single block, of length $n$.

*Conclusion.* The sequence has length $n^2$ and no monotone subsequence of length $n+1$; by Erdős–Szekeres the bound $n^2+1$ is therefore sharp.

*Verification.* $n=2$: the sequence $2,1,4,3$ has longest increasing subsequence $2$ and longest decreasing subsequence $2$. ✓ $n=3$: $3,2,1,6,5,4,9,8,7$ has both longest lengths $3$. ✓

**35.** *The two counts.*

Total colourings of the $15$ edges of $K_6$: $2^{15} = 32\,768$.

For a fixed $4$-set of vertices, a colouring that makes it monochromatic is determined by the colour ($2$ choices) and the colours of the remaining $15-6 = 9$ edges ($2^9$ choices): $2\cdot 2^9 = 1024$ colourings.

*Union bound.* There are $\binom64 = 15$ four-sets, so the number of colourings having at least one monochromatic $K_4$ is at most
$$15\cdot 1024 = 15\,360 < 32\,768 .$$
Since the bad colourings do not exhaust all $32\,768$, some colouring of $K_6$ has no monochromatic $K_4$. $\square$

*Remark.* The union bound counts colourings with two monochromatic $K_4$'s twice, so $15\,360$ is an overcount of the bad colourings; that is harmless, since an upper bound below the total is all that is needed. The conclusion is the lower bound $R(4,4) > 6$.

**36.** *Objects: $19$ lattice points. Boxes: the $9$ classes of $\mathbb{Z}^2$ modulo $3$, indexed by the pair of residues $(\bar x,\bar y)$.*

$$\left\lceil \frac{19}{9}\right\rceil = 3,$$
so some class contains three of the points, say $P_1,P_2,P_3$. Their coordinates satisfy $x_1\equiv x_2\equiv x_3 \pmod 3$ and $y_1\equiv y_2\equiv y_3\pmod 3$. Hence
$$x_1+x_2+x_3 \equiv 3x_1 \equiv 0 \pmod 3, \qquad y_1+y_2+y_3 \equiv 3y_1 \equiv 0 \pmod 3,$$
so both coordinates of the centroid are integers. $\square$

*Sharpness.* Place exactly two points in each of the nine residue classes modulo $3$ (for example $2\cdot 9 = 18$ points drawn from the $3\times 3$ block and its translates). Then no class contains three points, so no three are congruent modulo $3$ in both coordinates, so no three have an integral centroid. Hence $18$ points do not suffice.
