# Counting Principles — Solutions

> [Counting Principles](README.md) · Solutions to the 36 problems in [exercises.md](exercises.md)

Each solution states the strategy, then carries out every significant step; every numerical answer is checked at a small case. Proof problems receive complete proofs, and where a second method exists it is shown or described.

## Beginner

**1.** *Strategy: three independent choices, so multiply — but be careful about what counts as a "choice" in part (b).*

(a) A meal is a triple (starter, main, dessert), and the three entries are chosen independently, so the product rule gives
$$4 \cdot 6 \cdot 3 = 72 .$$

(b) The starter is optional, which means there are $4+1 = 5$ options at the first stage (the four starters, plus "none"), not $4$. Hence
$$5 \cdot 6 \cdot 3 = 90 .$$
The tempting answer $72$ fails because it omits the $18$ meals with no starter; the sum rule justifies adding them, since the "with starter" and "without starter" classes are disjoint.

(c) The number of desserts is now the number of multisets of size $1$ or $2$ from $3$ kinds. Size $1$: $3$. Size $2$, by stars and bars (Theorem 7.11.1): $\binom{3+2-1}{2-1} = \binom42 = 6$. The six are $\{1,1\},\{1,2\},\{1,3\},\{2,2\},\{2,3\},\{3,3\}$. So there are $3 + 6 = 9$ dessert possibilities, and the total is
$$4 \cdot 6 \cdot 9 = 216 .$$

*Check.* With $2$ starters, $1$ main and $2$ desserts, the three parts give $2$, $1$, $2+\binom32 = 5$, so $10$ meals; listing them is a matter of writing down the five dessert multisets $\{a\}, \{b\}, \{a,a\}, \{a,b\}, \{b,b\}$ for each of the two starters. ✓

**2.** *Strategy: product rule, with the restricted position chosen first.*

Two letters, each any of $26$: $26^2 = 676$. The first digit has $9$ options ($1$–$9$), the next two have $10$ each: $9 \cdot 10^2 = 900$. Independent, so

$$676 \cdot 900 = 608\,400 .$$

*Check (small case).* With letters from $\{A,B\}$ and digits from $\{1,2,3\}$, the count is $2\cdot 3\cdot 3 = 18$. Listing by first letter and then by the two digits: $A11, A12, A13, A21, A22, A23, A31, A32, A33$ and the same nine with $B$; that is $18$. ✓

**3.** *Strategy: the definition of $\binom{n}{k}$, plus the complement bijection.*

(a) $\binom{10}{4} = \dfrac{10!}{4!\,6!} = \dfrac{10\cdot 9\cdot 8\cdot 7}{24} = 210$.

(b) $\binom{10}{6} = \binom{10}{4} = 210$. No computation is needed: complementation $A \mapsto [10]\setminus A$ maps $4$-subsets bijectively to $6$-subsets (it is its own inverse), so the two collections are equinumerous.

*Check.* $\binom{10}{4} = 210$ also follows from the recurrence: $\binom{10}{4} = \binom94 + \binom93 = 126 + 84 = 210$. ✓

**4.** *Strategy: multiset permutation (Theorem 7.5.1).*

LEVEL has five letters with L twice and E twice, so

$$\frac{5!}{2!\,2!} = \frac{120}{4} = 30 .$$

*Why $2!\,2!$:* labelling the two L's and the two E's distinguishes $2\cdot 2 = 4$ orderings per visible word, and the division principle removes exactly that overcount.

*Check.* The multiset $\{E,E,V\}$ has $3!/2! = 3$ arrangements: $EEV$, $EVE$, $VEE$. ✓

**5.** *Strategy: fix one person to kill the rotational symmetry (Theorem 7.6.1).*

Seat one named person anywhere. The remaining $6$ people occupy the remaining $6$ seats, and distinct orderings give distinct seatings, so there are

$$6! = 720 .$$

This is $(7-1)!$.

With reflections also identified, each seating is paired with a different mirror image (possible because $7 \ge 3$ and all people are distinct), so the count halves:

$$\frac{720}{2} = 360 .$$

*Check.* Four people: $3! = 6$ seatings, $6/2 = 3$ necklaces. Listing with A fixed: $ABCD$, $ABDC$, $ACBD$ are the three, and each of the other three is a mirror image of one of them. ✓

**6.** *Strategy: choose the two classes independently (product rule), then check by the complement.*

$$\binom52\binom73 = 10 \cdot 35 = 350 .$$

*Second method.* There are $\binom{12}{5} = 792$ committees in total. Those failing the requirement have $0,1,3,4$ or $5$ women:

$$\binom50\binom75 + \binom51\binom74 + \binom53\binom72 + \binom54\binom71 + \binom55\binom70 = 21 + 175 + 210 + 35 + 1 = 442 .$$

Hence $792 - 442 = 350$. ✓ The five classes are disjoint (each committee has a definite number of women), so the sum rule applies.

*Check.* With $2$ women and $2$ men and a committee of $2$ containing exactly one of each: $\binom21\binom21 = 4$, and indeed $W_1M_1, W_1M_2, W_2M_1, W_2M_2$. ✓

**7.** *Strategy: Theorems 7.3.1–7.3.3.*

(a) $6^4 = 1296$.

(b) $6\cdot 5\cdot 4\cdot 3 = 360$, that is $6!/2!$.

(c) $0$: an injection from a $6$-element set into a $4$-element set would give $6$ distinct values inside a $4$-element set, impossible. Algebraically the falling factorial $4^{\underline{6}}$ contains the factor $4-4 = 0$.

(d) $4! = 24$: bijections of a $4$-element set with itself are its permutations.

*Check.* For $\lvert A\rvert = 2$, $\lvert B\rvert = 3$: $3^2 = 9$ functions; listing them as pairs $(f(1),f(2))$ gives $3\cdot3 = 9$; injective ones are the $3\cdot2 = 6$ pairs with distinct entries. ✓

**8.** *Strategy: each free element independently in or out (product rule).*

To contain $3$ and not contain $5$, the membership of $3$ and $5$ is forced, and the other six elements ($1,2,4,6,7,8$) are free:

$$2^6 = 64 .$$

For "at least one of $3$ and $5$", take the complement: subsets containing neither are exactly the $2^6 = 64$ above, so

$$2^8 - 2^6 = 256 - 64 = 192 .$$

*Check (inclusion–exclusion).* $128 + 128 - 64 = 192$, where $128 = 2^7$ counts subsets containing $3$ and $128$ those containing $5$. ✓

**9.** *Strategy: stars and bars (Theorem 7.11.1) with $k=4$, $n=12$.*

$$\binom{12+4-1}{4-1} = \binom{15}{3} = \frac{15\cdot14\cdot13}{6} = 455 .$$

*Check.* For $x_1+x_2+x_3 = 4$ the formula gives $\binom{6}{2} = 15$. Directly: $x_1 = 0$ allows $x_2 \in \{0,\dots,4\}$, five solutions; $x_1 = 1$ gives four; and so on down to one, for $5+4+3+2+1 = 15$. ✓

**10.** *Strategy: shift to non-negative variables (Theorem 7.11.2).*

With $x,y,z \ge 1$ put $x' = x-1$, $y' = y-1$, $z' = z-1$. Then $x'+y'+z' = 6$ in non-negative integers, so

$$\binom{6+3-1}{3-1} = \binom82 = 28 .$$

*Check.* For $x+y+z = 4$ positive, the formula gives $\binom32 = 3$: the solutions $(1,1,2),(1,2,1),(2,1,1)$. ✓

**11.** *Strategy: a divisor of $2^4 3^2 5$ is $2^a3^b5^c$ with $0\le a\le4$, $0\le b\le2$, $0\le c\le1$; independent choices.*

$$(4+1)(2+1)(1+1) = 30 .$$

Divisible by $6 = 2\cdot3$: need $a \ge 1$ and $b \ge 1$, giving $4 \cdot 2 \cdot 2 = 16$.

*Check.* $720/6 = 120 = 2^3\cdot3\cdot5$ has $4\cdot2\cdot2 = 16$ divisors, and dividing by $6$ matches divisors $d$ of $720$ that are multiples of $6$ with $720/d$. ✓

**12.** *Strategy: the binomial theorem (Theorem 7.7.1).*

(a) The coefficient of $x^ky^{7-k}$ is $\binom{7}{k}$, so with $k=3$:
$$\binom73 = 35 .$$

(b) Setting $x = y = 1$ gives the sum of all coefficients: $(1+1)^7 = 128 = 2^7$.

*Check.* Row $7$ of Pascal's triangle is $1,7,21,35,35,21,7,1$; the entry $35$ is in the middle, and the sum is $128$. ✓

## Intermediate

**13.** *Strategy: multiset permutation with four letters.*

Counts: M $1$, I $4$, S $4$, P $2$, total $11$. So

$$\frac{11!}{4!\,4!\,2!} = \frac{39\,916\,800}{24\cdot 24\cdot 2} = \frac{39\,916\,800}{1152} = 34\,650 .$$

*Check.* For BANANA, counts $3,2,1$ give $6!/(3!\,2!) = 60$; for the two-letter multiset $\{I,I\}$ the formula gives $2!/2! = 1$, correctly, since there is only one visible word $II$. ✓

**14.** *Strategy: choose the position of the A, then fill the rest from the $25$ non-A letters.*

There are $5$ positions for the single A, and each of the remaining four positions is filled by one of $25$ letters:

$$5 \cdot 25^4 = 5 \cdot 390\,625 = 1\,953\,125 .$$

The answer is **not** $5\cdot 26^4$: that product counts strings with two or more A's several times, once for each A that is nominated as "the" A. Since the positions of the A's are not distinguished by a unique label, the recipe is not a bijection.

*Check.* The two-letter analogue: strings of length $2$ with exactly one A: $2\cdot 25 = 50$; listing, the strings are $Ax$ and $xA$ for $x$ a non-A letter, which is $25 + 25$. ✓

**15.** (a) *Algebraic proof.* Both sides equal $\dfrac{n!}{j!\,(k-j)!\,(n-k)!}$:
$$\binom{n}{k}\binom{k}{j} = \frac{n!}{k!\,(n-k)!}\cdot\frac{k!}{j!\,(k-j)!} = \frac{n!}{j!\,(k-j)!\,(n-k)!},$$
$$\binom{n}{j}\binom{n-j}{k-j} = \frac{n!}{j!\,(n-j)!}\cdot\frac{(n-j)!}{(k-j)!\,(n-k)!} = \frac{n!}{j!\,(k-j)!\,(n-k)!}.$$

*Combinatorial proof.* Count the pairs $(J,K)$ with $J \subseteq K \subseteq [n]$, $\lvert J\rvert = j$, $\lvert K\rvert = k$.
By $K$ first: choose $K$ in $\binom{n}{k}$ ways, then $J \subseteq K$ in $\binom{k}{j}$ ways — left-hand side.
By $J$ first: choose $J$ in $\binom{n}{j}$ ways, then add $k-j$ further elements from the remaining $n-j$ to form $K$, in $\binom{n-j}{k-j}$ ways — right-hand side.
Both count the same set of pairs. $\square$

(b) Summing (a) over $k$,
$$\sum_{k=j}^{n}\binom{n}{k}\binom{k}{j} = \binom{n}{j}\sum_{k=j}^{n}\binom{n-j}{k-j} = \binom{n}{j}\sum_{i=0}^{n-j}\binom{n-j}{i} = \binom{n}{j}2^{\,n-j},$$
where $i = k-j$ and the last step is the row sum for the $(n-j)$-set. Equivalently, this is the double count of Section 7.13: choose $J$, then each remaining element is in $K$ or not.

*Check.* $n=4$, $j=2$: left side $= \binom42\binom22 + \binom43\binom32 + \binom44\binom42 = 6 + 12 + 6 = 24$; right side $= \binom42 2^2 = 24$. ✓

**16.** *Strategy: Vandermonde's identity (Theorem 7.10.1) with $m=n=10$ and $r=5$.*

$$\sum_{k=0}^{5}\binom{10}{k}\binom{10}{5-k} = \binom{20}{5} = 15\,504 .$$

Term by term: $252 + 2100 + 5400 + 5400 + 2100 + 252 = 15\,504$. ✓ (The terms are $\binom{10}{0}\binom{10}{5} = 252$, $\binom{10}{1}\binom{10}{4} = 2100$, $\binom{10}{2}\binom{10}{3} = 5400$, and the mirror images.)

*Meaning.* Choosing $5$ people from $10$ men and $10$ women, classified by the number of men.

*Check.* The small case $m=n=2$, $r=2$: $\binom20\binom22 + \binom21\binom21 + \binom22\binom20 = 1+4+1 = 6 = \binom42$. ✓

**17.** (a) *Proof.* Count $(r+1)$-subsets of $[n+1]$ by their largest element. If the largest is $i+1$, the remaining $r$ elements lie in $[i]$, giving $\binom{i}{r}$; as $i$ runs from $r$ to $n$ these classes are disjoint and exhaust all $(r+1)$-subsets. Hence $\sum_{i=r}^{n}\binom{i}{r} = \binom{n+1}{r+1}$. $\square$

(b) With $r=3$, $n=10$:
$$\sum_{k=3}^{10}\binom{k}{3} = \binom{11}{4} = 330 .$$
Directly: $1 + 4 + 10 + 20 + 35 + 56 + 84 + 120 = 330$. ✓

*Check (small case).* $r=1$, $n=4$: $1+2+3+4 = 10 = \binom52$. ✓

**18.** *Strategy: count all paths, subtract those through the forbidden point.*

All monotone paths $(0,0)\to(5,5)$: $\binom{10}{5} = 252$. A path through $(2,2)$ splits into an independent prefix $(0,0)\to(2,2)$ and suffix $(2,2)\to(5,5)$; by the product rule there are
$$\binom42\binom63 = 6\cdot 20 = 120 .$$
Hence the number avoiding $(2,2)$ is $252 - 120 = 132$.

*Check.* The analogous count $(0,0)\to(2,2)$ avoiding $(1,1)$: $\binom42 - \binom21\binom21 = 6-4 = 2$, namely the paths $RRUU$ and $UURR$. ✓

**19.** *Strategy: stars and bars in its positive form, then subtract.*

Non-empty boxes: by Theorem 7.11.2 with $n=12$, $k=5$,
$$\binom{11}{4} = 330 .$$
Empty boxes allowed: by Theorem 7.11.1,
$$\binom{12+5-1}{5-1} = \binom{16}{4} = 1820 .$$
The difference is $1820 - 330 = 1490$, which by the sum rule is exactly the number of distributions having at least one empty box, since every distribution either has no empty box or has one.

*Check.* Two balls in two boxes: non-empty $\binom11 = 1$; empty allowed $\binom32 = 3$; difference $2$, the distributions with an empty box. ✓

**20.** *Strategy: handle the restrictive condition by arranging the other class first.*

Arrange the five boys in a row: $5! = 120$ ways. This creates six gaps (before the first boy, between consecutive boys, after the last). To keep girls apart, each girl must occupy a different gap, so choose five of the six gaps and order the five distinct girls in them:
$$\binom65 \cdot 5! = 6\cdot 120 = 720 .$$
By the product rule the total is
$$120 \cdot 720 = 86\,400 .$$

*Check.* Two boys and one girl: $2!\cdot\binom31\cdot1! = 6$, which matches the six arrangements $GBB, BGB, BBG$ with the boys distinguishable. ✓

*Why boys first.* The condition "no two girls adjacent" constrains where girls may go relative to boys; once the boys are fixed, the admissible positions for girls are exactly the gaps, and the constraint becomes "at most one girl per gap" — a selection problem, not a difficult sequential one.

**21.** *Strategy: partition into fibres, then label the fibres.*

A surjection $f : [5]\to[3]$ partitions $[5]$ into three non-empty fibres, one per target. The number of partitions of a $5$-set into $3$ non-empty blocks is the Stirling number $S(5,3)$, computed from the recurrence $S(n,k) = kS(n-1,k) + S(n-1,k-1)$ with $S(n,1) = S(n,n) = 1$:
$$S(3,3)=1,\quad S(4,2) = 2S(3,2)+S(3,1) = 2\cdot3+1 = 7,\quad S(5,3) = 3S(4,3)+S(4,2) = 3\cdot6+7 = 25 .$$
Assigning the three blocks to the three targets can be done in $3! = 6$ ways, so there are $25\cdot 6 = 150$ surjections.

*Second method (inclusion–exclusion).*
$$3^5 - \binom31 2^5 + \binom32 1^5 = 243 - 96 + 3 = 150 .$$
Here $3^5$ counts all functions, and the corrections remove those missing at least one target.

*Why the two agree.* The inclusion–exclusion formula counts surjections directly. The Stirling route counts the same set by grouping surjections according to their fibre partition: each partition supports exactly $3!$ surjections, one for each way of assigning its blocks to the targets, and the assignments are distinct. Both are correct counts of one set, so they are equal.

*Check.* Surjections $[4]\to[3]$: $81 - 48 + 3 = 36$, and $3!\,S(4,3) = 6\cdot 6 = 36$. ✓

**22.** *Strategy: complement.*

Total circular seatings of $10$ distinct people: $9! = 362\,880$. Seating with A and B adjacent: treat them as one block, giving $9$ objects around the circle, arranged in $8!$ ways, with $2$ internal orders for the block:
$$2\cdot 8! = 2\cdot 40\,320 = 80\,640 .$$
Hence
$$9! - 2\cdot 8! = 362\,880 - 80\,640 = 282\,240 .$$

*Check.* Four people, A and B not adjacent: total $3! = 6$; adjacent $2\cdot 2! = 4$; difference $2$. Listing with A fixed: $ACBD$ and $ADBC$ are the two. ✓

**23.** *Strategy: multiset permutation, then the same with one letter fixed.*

Counts: A twice, B three times, C once, D once, total $7$.
$$\frac{7!}{2!\,3!\,1!\,1!} = \frac{5040}{12} = 420 .$$

Beginning with A: fix the first letter as A, leaving the multiset $\{A,B,B,B,C,D\}$ with counts $1,3,1,1$ and total $6$:
$$\frac{6!}{1!\,3!\,1!\,1!} = \frac{720}{6} = 120 .$$

*Check.* The positions of the three B's can be chosen in $\binom73 = 35$ ways and the remaining four positions filled with A,A,C,D in $4!/2! = 12$ ways, giving $35\cdot12 = 420$. ✓

**24.** *Strategy: exhibit an involution that swaps parity.*

Define $T(A) = A\triangle\{1\}$ for $A\subseteq[n]$, the symmetric difference with the singleton $\{1\}$, i.e. toggle membership of the element $1$. Then:

* $T$ is a function $\mathcal{P}([n])\to\mathcal{P}([n])$;
* $\lvert T(A)\rvert = \lvert A\rvert \pm 1$, so $T$ maps even-sized subsets to odd-sized ones and conversely;
* $T(T(A)) = A$, so $T$ is injective (indeed bijective) with itself as inverse.

Restricting $T$ to even subsets gives a bijection onto the odd subsets, so the two classes are equinumerous. Since they partition the $2^n$ subsets, each has $2^{n-1}$ elements.

*Check.* $n=4$: even subsets $1 + 6 + 1 = 8$ (sizes $0,2,4$), odd subsets $4+4 = 8$ (sizes $1,3$). ✓

*Second proof (for reference).* $\sum_k(-1)^k\binom nk = (1-1)^n = 0$ is the difference of the two counts, and their sum is $2^n$; solving gives $2^{n-1}$ each.

## Advanced

**25.** (a) *Combinatorial proof.* Let $\lvert S\rvert = n$ and fix $x\in S$. Every $k$-subset of $S$ either contains $x$ or does not; the two classes are disjoint and cover all $k$-subsets. The ones containing $x$ correspond bijectively to $(k-1)$-subsets of $S\setminus\{x\}$ (delete $x$), and the ones omitting $x$ are the $k$-subsets of $S\setminus\{x\}$. By the sum rule, $\binom nk = \binom{n-1}{k-1}+\binom{n-1}{k}$. $\square$

*Algebraic proof.*
$$\binom{n-1}{k-1}+\binom{n-1}{k} = \frac{(n-1)!}{(k-1)!(n-k)!}+\frac{(n-1)!}{k!(n-k-1)!},$$
and over the common denominator $k!(n-k)!$,
$$= \frac{(n-1)!\,k + (n-1)!\,(n-k)}{k!(n-k)!} = \frac{(n-1)!\,n}{k!(n-k)!} = \binom nk . \qquad\square$$

(b) *Claim.* $\sum_{k=0}^{n}\binom nk = 2^n$ for all $n\ge0$.

*Base.* $n=0$: the left side is $\binom00 = 1 = 2^0$.

*Step.* Assume the claim for $n$. Then, using Pascal's identity term by term,
$$\sum_{k=0}^{n+1}\binom{n+1}{k} = \sum_{k=0}^{n+1}\left[\binom{n}{k-1}+\binom{n}{k}\right] = \sum_{k=0}^{n+1}\binom{n}{k-1} + \sum_{k=0}^{n+1}\binom{n}{k}.$$
The second sum equals $2^n$ by the inductive hypothesis, because the terms with $k = n+1$ vanish. The first sum, after $j = k-1$, is $\sum_{j=-1}^{n}\binom{n}{j}$, which equals $\sum_{j=0}^{n}\binom{n}{j} = 2^n$ because the term $j=-1$ is $\binom{n}{-1} = 0$. Hence the total is $2^n + 2^n = 2^{n+1}$.

*Conclusion.* By induction the identity holds for all $n \ge 0$. $\square$

The convention $\binom nk = 0$ outside $0\le k\le n$ is used twice: to discard $\binom{n}{n+1}$ and to discard $\binom{n}{-1}$. Without it, the two sums would have different index ranges and the shift would need separate bookkeeping.

*Check.* $n=3$: $1+3+3+1 = 8 = 2^3$. ✓

**26.** (a) *Double counting.* Count the pairs $\bigl(A,(x,y)\bigr)$ where $A\subseteq[n]$ and $(x,y)$ is an ordered pair of **distinct** elements of $A$.

By subsets: a subset of size $k$ contains $k(k-1)$ ordered pairs of distinct elements, so the total is $\sum_k k(k-1)\binom nk$.

By pairs: choose the ordered pair first, in $n(n-1)$ ways; then $x, y$ are in $A$ and the other $n-2$ elements are each free, giving $2^{n-2}$ subsets per pair. The total is $n(n-1)2^{n-2}$.

Both count the same set, so the identity holds. $\square$

(b) *Differentiation.* Let $f(y) = (1+y)^n = \sum_k\binom nk y^k$. Differentiating twice,
$$f''(y) = n(n-1)(1+y)^{n-2} = \sum_k k(k-1)\binom nk y^{k-2}.$$
At $y=1$ the left side is $n(n-1)2^{n-2}$ and the right side is $\sum_k k(k-1)\binom nk$, since $1^{k-2}=1$. $\square$

(c) $n=3$: the left side is $0 + 0 + 2\cdot1\cdot3 + 6\cdot1\cdot1 = 12$; the right side is $3\cdot2\cdot2^{1} = 12$. ✓

*Remark.* Both proofs need $n\ge2$; for $n=1$ the identity reads $0 = 0$, and the double-counting argument still works because there are no ordered pairs of distinct elements.

**27.** *Statement.* For $n_1,n_2,n_3,r\in\mathbb{N}_0$,
$$\binom{n_1+n_2+n_3}{r} = \sum_{\substack{k_1+k_2+k_3 = r\\ k_i \ge 0}} \binom{n_1}{k_1}\binom{n_2}{k_2}\binom{n_3}{k_3}.$$

*Combinatorial proof.* Let $S_1,S_2,S_3$ be pairwise disjoint sets of sizes $n_1,n_2,n_3$. An $r$-subset of $S_1\cup S_2\cup S_3$ is determined by the triple $(k_1,k_2,k_3)$ of its intersections with the three parts, and $k_1+k_2+k_3 = r$ necessarily. For a fixed triple there are $\binom{n_1}{k_1}\binom{n_2}{k_2}\binom{n_3}{k_3}$ such subsets, by the product rule; the classes for different triples are disjoint and exhaustive, so the sum rule gives the total, which is also $\binom{n_1+n_2+n_3}{r}$. $\square$

*Algebraic proof.* Compare coefficients of $x^r$ in $(1+x)^{n_1+n_2+n_3} = (1+x)^{n_1}(1+x)^{n_2}(1+x)^{n_3}$. Alternatively apply Theorem 7.10.1 twice.

*Evaluation.* The triple sums to $4$, so the total is the coefficient of $x^4$ in $(1+x)^{3+4+5} = (1+x)^{12}$, namely $\binom{12}{4} = 495$.

*Spot check.* The triples $(k_1,k_2,k_3)$ summing to $4$ include $(3,1,0)$ contributing $\binom33\binom41\binom50 = 4$ and $(0,4,0)$ contributing $\binom30\binom44\binom50 = 1$; summing all $\binom{6}{2} = 15$ triples gives $495$. ✓

**28.** (a) In Theorem 7.10.1 take $m = n$ and $r = n$:
$$\binom{2n}{n} = \sum_{k=0}^{n}\binom nk\binom{n}{n-k} = \sum_{k=0}^{n}\binom nk^2,$$
using the symmetry $\binom{n}{n-k} = \binom nk$.

(b) Take $r = n-1$:
$$\binom{2n}{n-1} = \sum_{j=0}^{n-1}\binom nj\binom{n}{n-1-j}.$$
Substituting $k = n-1-j$, so that $j = n-1-k$ and $\binom nj = \binom{n}{n-1-k} = \binom{n}{k+1}$, while $\binom{n}{n-1-j} = \binom nk$:
$$\binom{2n}{n-1} = \sum_{k=0}^{n-1}\binom{n}{k+1}\binom nk .$$

(c) $n=3$: (a) reads $1+9+9+1 = 20 = \binom63$; (b) reads $\binom30\binom31 + \binom31\binom32 + \binom32\binom33 = 3+9+3 = 15 = \binom62$. ✓

*Interpretation.* (a) counts $n$-subsets of $2n$ objects split into two equal halves, by the number taken from the first half; (b) counts $(n-1)$-subsets the same way.

**29.** (a) A composition of $n$ is a solution of $x_1+\cdots+x_k = n$ in positive integers for some $k$. Write $n$ unit blocks in a row; there are $n-1$ gaps between consecutive blocks. Choosing a set $S$ of gaps and cutting there produces a composition, whose parts are the block-counts of the resulting segments. Conversely, a composition determines its cut positions. The two operations are inverse, so compositions of $n$ correspond bijectively to subsets of an $(n-1)$-set, and there are $2^{n-1}$. $\square$

(b) Compositions of $6$: $2^{5} = 32$. With exactly three parts: by Theorem 7.11.2, $\binom{6-1}{3-1} = \binom52 = 10$. Listing by part multiplicities: $(1,1,4)$ in $3$ orders, $(1,2,3)$ in $6$ orders, $(2,2,2)$ in $1$ order; total $3+6+1 = 10$. ✓

*Check.* Compositions of $4$: $2^3 = 8$, listed in Example 7.12.3 of the tutorial. ✓

**30.** *Induction.* Base $m=0$: the left side is $\binom n0 = 1$ and the right side is $\binom{n+1}{0} = 1$. Step: assume the identity for $m-1$. Then
$$\sum_{k=0}^{m}\binom{n+k}{k} = \binom{n+m+1}{m-1} + \binom{n+m}{m}$$
by the inductive hypothesis, and Pascal's identity converts the right side into
$$\binom{n+m+1}{m-1}+\binom{n+m}{m} = \binom{n+m+1}{m},$$
since $\binom{N}{m-1}+\binom{N}{m} = \binom{N+1}{m}$ with $N = n+m$. $\square$

*Hockey stick.* Because $\binom{n+k}{k} = \binom{n+k}{n}$, the sum is $\sum_{k=0}^{m}\binom{n+k}{n}$, which is the hockey stick (Example 7.13.3) with $i$ running from $n$ to $n+m$:
$$\sum_{i=n}^{n+m}\binom{i}{n} = \binom{n+m+1}{n+1} = \binom{n+m+1}{m}. \qquad\square$$

*Check.* $n=2$, $m=3$: $1 + 3 + 6 + 10 = 20 = \binom63$. ✓

**31.** *The reflection.* Let $P$ be a path from $(0,0)$ to $(n,n)$ that reaches the line $y = x+1$; let $A$ be the **first** point of $P$ on that line. Reflect the initial segment of $P$ from $(0,0)$ to $A$ in the line $y = x+1$, leaving the rest unchanged. The image starts at $(-1,1)$ and ends at $(n,n)$; it has $n+1$ horizontal and $n-1$ vertical steps. Conversely, any monotone path from $(-1,1)$ to $(n,n)$ must meet $y=x+1$ (it starts with $y-x = 2$ and ends with $y - x = 0$), and reflecting its first such segment back returns a bad path. The two maps are inverse, so bad paths are in bijection with paths from $(-1,1)$ to $(n,n)$, which number $\binom{2n}{n+1}$.

*Conclusion.* The good paths number
$$\binom{2n}{n} - \binom{2n}{n+1} = \frac{1}{n+1}\binom{2n}{n}.$$

*Values.*
| $n$ | $\binom{2n}{n}$ | $\binom{2n}{n+1}$ | difference |
|---|---|---|---|
| 1 | 2 | 1 | 1 |
| 2 | 6 | 4 | 2 |
| 3 | 20 | 15 | 5 |
| 4 | 70 | 56 | 14 |
| 5 | 252 | 210 | 42 |

The sequence $1, 2, 5, 14, 42$ is the Catalan numbers $C_1,\dots,C_5$. ✓

## Challenge

**32.** *First method: choose the suit pair, then exclude monochromatic hands.*

Choose the two suits: $\binom42 = 6$. From the $26$ cards of those suits, a $5$-card hand must use **both** suits, so exclude the hands entirely within one of them:
$$\binom{26}{5} - 2\binom{13}{5} = 65\,780 - 2\cdot 1287 = 65\,780 - 2574 = 63\,206 .$$
Total:
$$6 \cdot 63\,206 = 379\,236 .$$

*Second method: split by suit pattern.*

Within a fixed suit pair the patterns are $4+1$ and $3+2$. For $4+1$: choose which suit supplies $4$ ($2$ ways), then $4$ cards of its $13$ and $1$ of the other $13$:
$$2\binom{13}{4}\cdot 13 = 2\cdot 715\cdot 13 = 18\,590 .$$
For $3+2$: choose which suit supplies $3$ ($2$ ways), then $\binom{13}{3}$ and $\binom{13}{2}$:
$$2\binom{13}{3}\binom{13}{2} = 2\cdot 286\cdot 78 = 44\,616 .$$
Per suit pair: $18\,590 + 44\,616 = 63\,206$, and over the six suit pairs $6\cdot 63\,206 = 379\,236$. ✓ Both methods agree.

*Check (scale).* For $2$-card hands from exactly two suits, the first method gives $6\left[\binom{26}{2} - 2\binom{13}{2}\right] = 6[325 - 156] = 1014$. Directly, such a hand is one card from each of two suits: $6\cdot 13\cdot 13 = 1014$. ✓ The second method must include the pattern $1+1$ for this hand size, which is the point of the pattern list being exhaustive.

**33.** (a) *Proof.* Let $a_1<\cdots<a_k$ satisfy $a_{i+1}\ge a_i+2$ inside $[n]$, and set $b_i = a_i-(i-1)$. Then $b_{i+1}-b_i = a_{i+1}-a_i-1 \ge 1$, so $b_1<\cdots<b_k$; also $b_1 = a_1\ge1$ and $b_k = a_k-(k-1)\le n-k+1$. Hence $\{b_1,\dots,b_k\}$ is a $k$-subset of $[n-k+1]$. Conversely, given $b_1<\cdots<b_k$ in $[n-k+1]$, set $a_i = b_i + (i-1)$; then $a_{i+1}-a_i \ge 2$ and $a_k \le n$. The two operations are inverse, so the count is $\binom{n-k+1}{k}$. $\square$

(b) $n=10$, $k=4$: $\binom{7}{4} = 35$. Check with $n=6$, $k=3$: $\binom43 = 4$, and the four subsets are $\{1,3,5\}$, $\{1,3,6\}$, $\{1,4,6\}$, $\{2,4,6\}$. ✓

(c) $n=2m$, $k=3$: $\binom{2m-2}{3} = \dfrac{(2m-2)(2m-3)(2m-4)}{6} = \dfrac{2}{3}(m-1)(m-2)(2m-3)$.

*Check.* $m=4$: $\binom63 = 20$, and $\tfrac23\cdot3\cdot2\cdot5 = 20$. ✓

**34.** *Recurrence.* Let $S_n$ be the number of subsets of $[n]$ with no two consecutive elements. Classify by whether $n$ belongs to the subset.

* If $n$ is not in the subset, the subset is any admissible subset of $[n-1]$: $S_{n-1}$ of them.
* If $n$ is in the subset, then $n-1$ is not, and the remaining elements form any admissible subset of $[n-2]$: $S_{n-2}$ of them.

The classes are disjoint and exhaustive, so $S_n = S_{n-1}+S_{n-2}$ for $n \ge 3$.

*Initial values.* $S_1 = 2$ (namely $\varnothing$ and $\{1\}$); $S_2 = 3$ ($\varnothing$, $\{1\}$, $\{2\}$).

*Conclusion.* The recurrence with these initial values is the Fibonacci recurrence, so by induction $S_n = F_{n+2}$ where $F_1 = F_2 = 1$: indeed $S_1 = 2 = F_3$ and $S_2 = 3 = F_4$, and if $S_{n-1} = F_{n+1}$ and $S_{n-2} = F_n$ then $S_n = F_{n+1}+F_n = F_{n+2}$. $\square$

*Values.* $S_1,\dots,S_6 = 2, 3, 5, 8, 13, 21$; enumerating the $21$ admissible subsets of $[6]$ directly confirms the last value. ✓

**35.** *Step 1: the recurrence for reciprocal binomial coefficients.* For $0\le k\le n$,
$$\frac{1}{\binom{n+1}{k}}+\frac{1}{\binom{n+1}{k+1}} = \frac{k!\,(n+1-k)!}{(n+1)!}+\frac{(k+1)!\,(n-k)!}{(n+1)!} = \frac{k!\,(n-k)!}{(n+1)!}\bigl[(n+1-k)+(k+1)\bigr] = \frac{(n+2)\,k!\,(n-k)!}{(n+1)!}.$$
Since $\dfrac{1}{\binom nk} = \dfrac{k!\,(n-k)!}{n!}$,
$$\frac{1}{\binom nk} = \frac{n+1}{n+2}\left(\frac{1}{\binom{n+1}{k}}+\frac{1}{\binom{n+1}{k+1}}\right).$$

*Step 2: summing.* Write $S_n = \sum_{k=0}^{n}\dfrac{1}{\binom nk}$. Summing the recurrence over $k = 0,\dots,n$,
$$S_n = \frac{n+1}{n+2}\left[\sum_{k=0}^{n}\frac{1}{\binom{n+1}{k}}+\sum_{k=0}^{n}\frac{1}{\binom{n+1}{k+1}}\right].$$
The first bracket is $S_{n+1}-\dfrac{1}{\binom{n+1}{n+1}} = S_{n+1}-1$; the second is $S_{n+1}-\dfrac{1}{\binom{n+1}{0}} = S_{n+1}-1$. Hence
$$S_n = \frac{n+1}{n+2}\bigl(2S_{n+1}-2\bigr), \qquad\text{equivalently}\qquad S_{n+1} = \frac{n+2}{2(n+1)}S_n + 1 .$$

*Step 3: induction.* Write $T_m = \sum_{k=1}^{m}\dfrac{2^k}{k}$ and claim $S_n = \dfrac{n+1}{2^{n+1}}T_{n+1}$.

Base $n=0$: $S_0 = 1$ and $\dfrac{1}{2}T_1 = \dfrac12\cdot 2 = 1$.

Step: assume the claim for $n$. Then
$$S_{n+1} = \frac{n+2}{2(n+1)}\cdot\frac{n+1}{2^{n+1}}T_{n+1}+1 = \frac{(n+2)T_{n+1}}{2^{n+2}}+1 = \frac{(n+2)T_{n+1}+2^{n+2}}{2^{n+2}} = \frac{(n+2)T_{n+2}}{2^{n+2}},$$
using $T_{n+2} = T_{n+1}+\dfrac{2^{n+2}}{n+2}$, i.e. $(n+2)T_{n+2} = (n+2)T_{n+1}+2^{n+2}$. This is the claim with $n$ replaced by $n+1$. $\square$

*Check.* $n=1$: left side $1+1 = 2$; right side $\dfrac{2}{4}\left(\dfrac21+\dfrac42\right) = \dfrac12\cdot 4 = 2$. ✓ $n=2$: left $1+\tfrac12+1 = 2.5$; right $\dfrac38\left(2+2+\dfrac83\right) = \dfrac38\cdot\dfrac{20}{3} = 2.5$. ✓

**36.** (a) *Labelled groups first.* Assign the twelve people to three named groups $X, Y, Z$ of four: the number of ordered triples of disjoint $4$-sets covering everybody is the multinomial coefficient
$$\frac{12!}{4!\,4!\,4!} = 34\,650 .$$
Every unlabelled split into three blocks of four arises from exactly $3! = 6$ of these assignments, one for each bijection between the three blocks and the labels $X,Y,Z$. The blocks are non-empty and disjoint, so a non-trivial relabelling always produces a *different* labelled assignment: the division principle applies with class size exactly $6$. Hence
$$\frac{12!}{(4!)^3\,3!} = \frac{34\,650}{6} = 5775 .$$

(b) *With A and B together.* Their group must be $\{A,B\}$ together with two of the other ten people: $\binom{10}{2} = 45$ choices. The remaining eight people are split into two unlabelled groups of four: labelled pairs give $\frac{8!}{4!\,4!} = 70$, and each unlabelled split is counted $2! = 2$ times, so there are $35$. Total:
$$45\cdot 35 = 1575 .$$

(c) *Consistency.* The probability that A and B share a group is, from the counts, $\dfrac{1575}{5775} = \dfrac{3}{11}$. Directly: place A in some group; the other three members of that group are chosen uniformly from the eleven other people, and B is among them with probability $\dfrac{3}{11}$. The two agree. ✓
