# The Pigeonhole Principle — Exercises

> [The Pigeonhole Principle](README.md) · 36 problems · Beginner → Challenge · Solutions: [solutions.md](solutions.md)

Attempt every problem in writing before looking at [solutions.md](solutions.md). Each problem names the section of the tutorial that supplies the technique.

Notation: $[n] = \{1,2,\dots,n\}$; $\mathbb{N} = \{1,2,3,\dots\}$; $\lceil x\rceil$ is the least integer $\ge x$. "Sharp" or "optimal" means that the stated number of objects is the smallest that works: a proof must be accompanied by an example with one object fewer that avoids the conclusion. A **block** of a sequence means a set of consecutive terms.

Unless a problem says otherwise, a complete solution must name the objects, name the boxes, count both, and state which form of the principle is used.

## Beginner

**1.** *(§7.4)* Prove that among any $13$ people two were born in the same month, and explain in one sentence why the number $13$ cannot be replaced by $12$.

**2.** *(§7.4)* Prove that among any $367$ people two share a birthday. Why is the number $366$, rather than $365$, the relevant count of boxes?

**3.** *(§5.2, §7.2)* (a) Show that if $100$ pigeons occupy $9$ holes then some hole contains at least $12$ pigeons.
(b) Find the smallest number of pigeons that forces $12$ in some hole, and explain why $99$ pigeons do not suffice.

**4.** *(§7.2)* A drawer contains socks in $4$ colours. How many socks must be taken, without looking, to be certain of holding two of the same colour? Justify both the sufficiency and the necessity of your number.

**5.** *(§7.2)* How many cards must be drawn from a standard $52$-card deck to be certain of having two of the same suit? What if the target is three of the same suit?

**6.** *(§7.1)* Prove that among any $11$ integers, two have the same final digit. Is $11$ optimal?

**7.** *(§7.1)* Prove that among any $4$ integers, two have a difference divisible by $3$. Give an example of $3$ integers without such a pair.

**8.** *(§7.1)* Prove that among any $6$ integers, two have a difference divisible by $5$. Is $6$ optimal?

**9.** *(§7.1)* Prove that among any $19$ two-digit numbers, two have the same digit sum. (The digit sum of $47$ is $11$.) Is $19$ optimal?

**10.** *(§7.3)* Prove that among any $5$ integers, two have a sum divisible by $7$. Exhibit $4$ integers with no such pair.

**11.** *(§7.2)* A class of $25$ students is split into $8$ project groups. Prove that some group has at least $4$ students, and give a split showing that the number $4$ cannot be improved.

**12.** *(§7.6)* Prove that among any $5$ points in a square of side $2$, two are at distance at most $\sqrt2$. Show that $4$ points can be placed so that every pairwise distance exceeds $\sqrt2$.

## Intermediate

**13.** *(§7.3, §7.7)* Prove that among any $\lceil 3n/2\rceil + 1$ integers chosen from $\{1,2,\dots,3n\}$ there are two, one of which divides the other, and show that the bound is sharp.

**14.** *(§7.3, §7.7)* (a) Prove that among any $n+1$ integers chosen from $\{1,\dots,2n\}$, two are coprime.
(b) Determine the largest size of a subset of $\{1,\dots,2n\}$ containing no two coprime elements, and prove your answer.

**15.** *(§7.7)* Prove that for any $n$ integers $a_1,\dots,a_n$, some non-empty block of consecutive terms has a sum divisible by $n$. Show that $n-1$ terms do not suffice.

**16.** *(§7.2)* Prove that among any $5$ integers there are $3$ whose sum is divisible by $3$. Show that $4$ integers do not suffice, and that $3$ integers do not suffice either.

**17.** *(§7.6)* Prove that among any $5$ points in an equilateral triangle of side $1$, two are at distance at most $1/2$. Show that $4$ points can be placed so that all pairwise distances exceed $1/2$.

**18.** *(§7.6)* Prove that among any $9$ points with integer coordinates in three-dimensional space, two have a midpoint with integer coordinates. Show that $8$ points do not suffice.

**19.** *(§7.1, §7.3)* Prove that among any $7$ integers, two have a sum or a difference divisible by $10$. Give $6$ integers with no such pair.

**20.** *(§7.3)* Prove that among any $51$ numbers chosen from $\{1,2,\dots,100\}$, two are consecutive. Deduce that two are coprime.

**21.** *(§7.10)* Prove that among any $6$ people there are either three who all know each other or three who are all strangers to each other. (Assume "knowing" is mutual.)

**22.** *(§7.10)* Prove that any sequence of $10$ distinct real numbers contains an increasing subsequence of length $4$ or a decreasing subsequence of length $4$. Then find such a subsequence explicitly in $4, 9, 1, 8, 2, 7, 3, 6, 5, 10$.

**23.** *(§7.4)* Determine the smallest number of people that guarantees three of them were born in the same month, and the smallest number that guarantees four. Prove both answers and give the extremal examples.

**24.** *(§7.6)* Prove that among any $7$ points in a rectangle measuring $3$ by $4$, two are at distance at most $\sqrt5$. Explain the choice of the pieces in your partition.

## Advanced

**25.** *(§5.2)* (a) Prove the generalised pigeonhole principle: if $N$ objects are placed in $k$ pairwise disjoint boxes and $k \ge 1$, some box contains at least $\lceil N/k\rceil$ objects.
(b) Show the bound is attained: for every $N$ and $k$ there is a distribution in which no box contains more than $\lceil N/k\rceil$ objects.
(c) Show that the hypothesis $N > k(m-1)$ cannot be relaxed to $N = k(m-1)$: give a distribution of $k(m-1)$ objects with no box containing $m$.

**26.** *(§7.10)* State and prove the Erdős–Szekeres theorem: every sequence of $rs+1$ distinct real numbers contains an increasing subsequence of length $r+1$ or a decreasing subsequence of length $s+1$. Deduce that every sequence of $n^2+1$ distinct reals has a monotone subsequence of length $n+1$.

**27.** *(§7.8)* Prove Dirichlet's approximation theorem: for every real $\alpha$ and every integer $N \ge 1$ there are integers $p,q$ with $1 \le q \le N$ and $\lvert q\alpha - p\rvert < 1/N$. Where exactly is the strict inequality lost or gained?

**28.** *(§5.4, §7.11)* State and prove the infinite pigeonhole principle. Deduce that every infinite sequence of real numbers has an infinite monotone subsequence, and explain why the finite Erdős–Szekeres theorem does not give this directly.

**29.** *(§7.9)* (a) Prove that the maximum of a finite list of real numbers is at least their average, and deduce the generalised pigeonhole principle from it.
(b) Edges of $K_6$ are coloured red or blue independently with probability $1/2$. Compute the expected number of monochromatic triangles, and deduce that some colouring has at least that many and some colouring has at most that many.

**30.** *(§7.8)* Let $m_1,\dots,m_k$ be pairwise coprime positive integers and $M = m_1\cdots m_k$. Prove that the map $\Phi : \mathbb{Z}/M\mathbb{Z} \to \prod_{i=1}^{k}\mathbb{Z}/m_i\mathbb{Z}$, $\Phi(x) = (x \bmod m_1, \dots, x \bmod m_k)$, is a bijection, and explain which counting facts are used.

**31.** *(§7.3)* Prove that among any $10$ distinct two-digit numbers there are two disjoint non-empty sets of them with equal sums. Where is the hypothesis "distinct" used, and why are two digits rather than three essential to the count?

## Challenge

**32.** *(§7.10)* Seventeen people correspond by mail, each pair exchanging letters on exactly one of three topics. Prove that there are three people who all write to each other on the same topic. (This is IMO 1964, Problem 4.)

**33.** *(§7.3, §7.7)* A student has $11$ weeks to prepare for an examination. She studies at least one problem every day and at most $12$ problems per week. Prove that there is a period of consecutive days during which she solves exactly $21$ problems. Why is the number $21$ the natural target here?

**34.** *(§7.10)* Show that the Erdős–Szekeres bound $rs+1$ is sharp: for every $n \ge 1$ construct a sequence of $n^2$ distinct real numbers with no increasing subsequence of length $n+1$ and no decreasing subsequence of length $n+1$. Verify your construction for $n=2$ and $n=3$.

**35.** *(§7.9)* Prove that there is a red/blue colouring of the edges of $K_6$ with no monochromatic $K_4$. Use the union bound, and give the two counts that make it work.

**36.** *(§7.6)* Prove that among any $19$ points with integer coordinates in the plane, there are three whose centroid has integer coordinates. Show that $18$ points do not suffice.

## Hints for the harder problems

* **13.** Write each integer as $2^v$ times an odd number, and count the odd numbers up to $3n$.
* **14 (b).** Look at the even numbers; for the upper bound, use the pairs $\{1,2\},\{3,4\},\dots$.
* **19.** The boxes are the six classes $\{0\},\{5\},\{1,9\},\{2,8\},\{3,7\},\{4,6\}$ of residues modulo $10$ up to sign.
* **27.** Use the $N+1$ fractional parts $\{j\alpha\}$ for $j = 0,\dots,N$, and $N$ half-open intervals of length $1/N$.
* **31.** Consider all $1024$ subsets and bound their sums.
* **33.** Consider the partial sums $s_1,\dots,s_{77}$ and the shifted values $s_i + 21$.
* **35.** Count colourings of $K_6$ and colourings containing a monochromatic $K_4$.
