# Partitions and Compositions — Solutions

> [Partitions and Compositions](README.md) · Solutions to the 36 problems in [exercises.md](exercises.md)

Every solution states the method first, then carries out every step. Numbers are checked against the tables of the tutorial wherever possible.

## Beginner

**1.** *Method: list both families and compare the counts with the formulas.*

Compositions of $4$ (order matters):

$$4,\quad 3+1,\quad 1+3,\quad 2+2,\quad 2+1+1,\quad 1+2+1,\quad 1+1+2,\quad 1+1+1+1 .$$

There are eight, and $2^{4-1} = 8$ ✓.

Partitions of $4$ (order does not matter):

$$4,\quad 3+1,\quad 2+2,\quad 2+1+1,\quad 1+1+1+1 .$$

There are five, and $p(4) = 5$ ✓.

The passage from the first list to the second merges $3+1$ with $1+3$ and $2+1+1$, $1+2+1$, $1+1+2$ into one partition each: $8 - 1 - 2 = 5$.

**2.** *Method: Theorem 7.1, count by length.*

$$c(10,4) = \binom{10-1}{4-1} = \binom93 = \frac{9\cdot 8\cdot 7}{3\cdot2\cdot1} = 84 .$$

*Why.* A composition with four parts is determined by its three partial sums $s_1 < s_2 < s_3$ chosen from $\{1,\dots,9\}$, and conversely each such triple gives parts $s_1$, $s_2-s_1$, $s_3-s_2$, $10-s_3$.

**3.** *Method: Theorem 7.1 with $k = 2$.*

$$c(7,2) = \binom{7-1}{2-1} = \binom61 = 6 .$$

The six compositions are

$$1+6,\quad 2+5,\quad 3+4,\quad 4+3,\quad 5+2,\quad 6+1,$$

one for each split point, as expected.

**4.** *Method: read multiplicities.*

$3+3+2+1+1+1 = 3^2\,2^1\,1^3$, so $\lvert\lambda\rvert = 3\cdot2 + 2\cdot1 + 1\cdot3 = 11$ and $\ell(\lambda) = 2+1+3 = 6$.

For $1^3 2^1 3^2$: $\lvert\lambda\rvert = 1\cdot3 + 2\cdot1 + 3\cdot2 = 3+2+6 = 11$ and $\ell(\lambda) = 3+1+2 = 6$ as well. The two partitions have the same size and the same length, but they are not conjugates: the column heights of $3,3,2,1,1,1$ are $6, 3, 2$ (column $1$ meets all six rows, column $2$ meets the two $3$s and the $2$, column $3$ meets the two $3$s), so the conjugate of $1^3 2^1 3^2$ is $(6,3,2)$. Equal length and equal size is a coincidence here, not a structural fact.

**5.** *Method: systematic listing, then Theorem 7.18 for the check.*

The partitions of $8$, grouped by largest part:

$$\begin{aligned}
&8;\ 7+1;\ 6+2,\ 6+1+1;\ 5+3,\ 5+2+1,\ 5+1+1+1;\ 4+4,\ 4+3+1,\ 4+2+2,\ 4+2+1+1,\ 4+1^4;\\
&3+3+2,\ 3+3+1+1,\ 3+2+2+1,\ 3+2+1^3,\ 3+1^5;\ 2^4,\ 2^3+1^2,\ 2^2+1^4,\ 2+1^6;\ 1^8 .
\end{aligned}$$

Counting: $1 + 1 + 2 + 3 + 5 + 5 + 4 + 1 = 22$ ✓ (the groups are for largest part $8,7,6,5,4,3,2,1$).

Exactly three parts: $6+1+1$, $5+2+1$, $4+3+1$, $4+2+2$, $3+3+2$, so $p(8,3) = 5$. Check by Theorem 7.18: $p(8,3) = p_{\le3}(5)$, and the partitions of $5$ with at most three parts are $5$, $4+1$, $3+2$, $3+1+1$, $2+2+1$, again five ✓.

**6.** *Method: count column heights.*

The column heights of $\lambda = (6,3,1)$ are: column 1 meets all three rows, column 2 meets the rows of lengths $6$ and $3$, column 3 likewise, columns 4, 5, 6 meet only the row of length $6$. So

$$\lambda' = (3,2,2,1,1,1).$$

Diagrams:

```text
λ = (6,3,1)                      λ' = (3,2,2,1,1,1)

● ● ● ● ● ●                      ● ● ●
● ● ●                            ● ●
●                                ● ●
                                 ●
                                 ●
                                 ●
```

Both have size $10$. And $\ell(\lambda) = 3 = \lambda'_1$, $\lambda_1 = 6 = \ell(\lambda')$ ✓, as Corollary 7.7 requires.

**7.** *Method: compute conjugates.*

For $(4,2,1)$ the column heights are $3,2,1,1$, so $(4,2,1)' = (3,2,1,1) \ne (4,2,1)$: not self-conjugate.

For $(4,3,2,1)$ the column heights are $4,3,2,1$, so $(4,3,2,1)' = (4,3,2,1)$: self-conjugate ✓.

*Sanity check.* A self-conjugate partition must have $\lambda_1 = \ell(\lambda)$; indeed $4 = 4$ here, whereas $4 \ne 3$ for $(4,2,1)$.

**8.** *Method: the halving bijection.*

Map a partition of $10$ with all parts even, $\lambda = (2\mu_1, \dots, 2\mu_k)$, to $\mu = (\mu_1,\dots,\mu_k)$, a partition of $5$. The map is invertible (double every part), hence a bijection, so the count is $p(5) = 7$.

The seven partitions of $10$ into even parts are

$$10,\quad 8+2,\quad 6+4,\quad 6+2+2,\quad 4+4+2,\quad 4+2+2+2,\quad 2^5,$$

which are exactly the doubles of the seven partitions of $5$: $5$, $4+1$, $3+2$, $3+1+1$, $2+2+1$, $2+1^3$, $1^5$ ✓.

**9.** *Method: Theorem 7.17.*

The partitions of $11$ with no part equal to $1$ number $p(11) - p(10) = 56 - 42 = 14$. Listed:

$$11,\ 9+2,\ 8+3,\ 7+4,\ 7+2+2,\ 6+5,\ 6+3+2,\ 5+4+2,\ 5+3+3,\ 5+2+2+2,\ 4+4+3,\ 4+3+2+2,\ 3+3+3+2,\ 3+2^4,$$

fourteen ✓.

**10.** *Method: list both families and apply Glaisher's rule.*

Partitions of $5$ into odd parts: $5$, $3+1+1$, $1^5$ — three.

Partitions of $5$ into distinct parts: $5$, $4+1$, $3+2$ — three ✓.

Glaisher's images: $5 \mapsto 5$ (multiplicity $1$); $3+1+1 \mapsto 3+2$ (the two copies of $1$ become one part $2$); $1^5 \mapsto 4+1$ (five copies of $1$ become $4+1$, since $5 = 4+1$ in binary). The images are the three distinct-part partitions ✓.

**11.** *Method: the pentagonal recurrence with signs $+,+,-,-,+,+$.*

For $n = 12$ the pentagonal numbers at most $12$ are $1,2,5,7,12$ with signs $+,+,-,-,+$. Hence

$$p(12) = p(11) + p(10) - p(7) - p(5) + p(0) = 56 + 42 - 15 - 7 + 1 = 77,$$

in agreement with the table ✓.

**12.** *Method: Theorem 7.16.*

$$p_{\le2}(13) = \left\lfloor \frac{13}{2}\right\rfloor + 1 = 6 + 1 = 7 .$$

The seven partitions: $13$, $12+1$, $11+2$, $10+3$, $9+4$, $8+5$, $7+6$ ✓.

## Intermediate

**13.** *Method: the last-part recursion for odd parts, cross-checked with the generating function.*

Let $e(n)$ be the number of compositions of $n$ into odd parts. Deleting the last part, which is odd, gives

$$e(n) = e(n-1) + e(n-3) + e(n-5) + \cdots .$$

Subtracting the same identity at $n-2$ cancels all common terms and leaves $e(n) - e(n-2) = e(n-1)$, i.e. $e(n) = e(n-1)+e(n-2)$, with $e(1) = 1$ (just $1$) and $e(2) = 1$ (just $1+1$). Hence $e(n) = F_n$ and $e(9) = F_9 = 34$.

*Cross-check by generating functions.* Compositions into odd parts are sequences of odd parts, so their generating function is

$$\frac{1}{1 - (x + x^3 + x^5 + \cdots)} = \frac{1}{1 - \frac{x}{1-x^2}} = \frac{1-x^2}{1-x-x^2}.$$

Since $\frac{1}{1-x-x^2} = \sum_{m\ge0}F_{m+1}x^m$, the coefficient of $x^9$ is $F_{10} - F_8 = 55 - 21 = 34$ ✓.

**14.** *Method: last-part recursion, then induction.*

Let $d(n)$ be the number of compositions of $n$ into parts $\ge 2$, with $d(0) = 1$ (the empty composition) and $d(1) = 0$. Deleting the last part $j \ge 2$ gives the bijection

$$d(n) = \sum_{j\ge2} d(n-j) = d(n-2) + d(n-3) + \cdots,$$

and subtracting the same identity at $n-1$ gives $d(n) - d(n-1) = d(n-2)$, i.e.

$$d(n) = d(n-1) + d(n-2) \qquad (n \ge 3).$$

With $d(1) = 0 = F_0$ (taking $F_0 = 0$) and $d(2) = 1 = F_1$, induction gives $d(n) = F_{n-1}$ for $n \ge 1$. $\blacksquare$

**15.** *Method: conjugation exchanges the two statistics.*

Conjugation is a bijection of the partitions of $n$ onto themselves (Theorem 7.6) and satisfies $\ell(\mu') = \mu_1$ for every $\mu$ (Corollary 7.7). Hence the bijection $\lambda \mapsto \lambda'$ maps

$$\{\lambda \vdash n : \lambda_1 = k\} \longrightarrow \{\mu \vdash n : \ell(\mu) = k\}$$

and back, because $\ell(\lambda') = \lambda_1 = k$ and conversely a partition $\mu$ with $\ell(\mu) = k$ is the conjugate of some $\lambda$ with $\lambda_1 = k$, namely $\lambda = \mu'$. Therefore the two sets have equal size, which is the claim. $\blacksquare$

*Alternative.* Both counts equal $p_{\le k}(n) - p_{\le k-1}(n)$: partitions with exactly $k$ parts are those with at most $k$ but not at most $k-1$, and partitions with largest part exactly $k$ are those with largest part at most $k$ but not at most $k-1$; by Corollary 7.7 the two difference sets correspond.

**16.** *Method: interpret the coefficient, then list.*

$$\frac{1}{(1-x)(1-x^2)(1-x^3)} = \prod_{i=1}^{3}\frac{1}{1-x^i} = \sum_{n\ge0} p_{\le3}(n)\,x^n,$$

so the coefficient of $x^9$ is $p_{\le3}(9) = 12$. Listed, the twelve partitions of $9$ with all parts at most $3$ (equivalently at most three parts) are

$$3^3,\ 3^2 2 1,\ 3^2 1^3,\ 3\,2^3,\ 3\,2^2 1^2,\ 3\,2\,1^4,\ 3\,1^6,\ 2^4 1,\ 2^3 1^3,\ 2^2 1^5,\ 2\,1^7,\ 1^9,$$

twelve ✓. The closed form gives the check $(9+3)^2/12 = 12$ exactly.

**17.** *Method: multiply and telescope.*

Let $r(n)$ be the number of partitions of $n$ in which every part occurs at most twice, and $s(n)$ the number of partitions into parts not divisible by $3$. Then

$$\sum_{n\ge0} r(n)x^n = \prod_{k\ge1}(1 + x^k + x^{2k}) = \prod_{k\ge1}\frac{1-x^{3k}}{1-x^k} .$$

In the last product the numerator runs over the multiples of $3$ and the denominator over all positive integers, so the multiples of $3$ cancel:

$$\prod_{k\ge1}\frac{1-x^{3k}}{1-x^k} = \frac{1}{\prod_{3 \nmid k}(1-x^k)} = \sum_{n\ge0} s(n)x^n .$$

Equal generating functions force $r(n) = s(n)$ for all $n$. $\blacksquare$

**18.** *Method: pentagonal recurrence, signs $+,+,-,-,+,+$.*

For $n = 18$ the pentagonal numbers at most $18$ are $1, 2, 5, 7, 12, 15$, with signs $+,+,-,-,+,+$. Therefore

$$\begin{aligned}
p(18) &= p(17) + p(16) - p(13) - p(11) + p(6) + p(3) \\
&= 297 + 231 - 101 - 56 + 11 + 3 \\
&= 528 - 157 + 14 \\
&= 385,
\end{aligned}$$

matching the table ✓.

**19.** *Method: substitute $a_i = 2b_i + 1$ and use stars and bars.*

A composition of $n$ into $k$ odd parts is a $k$-tuple $(a_1,\dots,a_k)$ of odd positive integers with $\sum a_i = n$. Write $a_i = 2b_i+1$ with $b_i \in \mathbb{N}_0$. Then $\sum a_i = 2\sum b_i + k = n$, so a solution exists only if $n - k$ is even and non-negative, i.e. $n \equiv k \pmod 2$ and $n \ge k$; in that case the $b_i$ are non-negative integers with

$$b_1 + \cdots + b_k = \frac{n-k}{2} =: m,$$

and by stars and bars the number of solutions is $\binom{m+k-1}{k-1}$.

For $n = 11$, $k = 3$: $m = (11-3)/2 = 4$, so the count is $\binom{4+3-1}{3-1} = \binom62 = 15$ ✓. (For $n = 12$, $k = 3$ the parity condition fails and the count is $0$, which matches the empty list of partitions of $12$ into three odd parts.)

**20.** *Method: multiply out and interpret.*

$$(1+x)(1+x^2)(1+x^3) = (1 + x + x^2 + x^3)(1+x^3) = 1 + x + x^2 + 2x^3 + x^4 + x^5 + x^6 .$$

Each choice of a subset $S \subseteq \{1,2,3\}$ contributes $x^{\sum_{i \in S} i}$, so the coefficient of $x^j$ counts partitions of $j$ into **distinct** parts all at most $3$. E.g. the coefficient of $x^3$ is $2$ because $3$ and $2+1$ both qualify. The coefficient of $x^5$ is $1$, coming from $3+2$.

**21.** *Method 1: direct count. Method 2: Ferrers and conjugation.*

*Direct.* A partition of $n$ into exactly two parts is $a+b$ with $a \ge b \ge 1$ and $a+b = n$. For each $b \in \{1,\dots,\lfloor n/2\rfloor\}$ there is exactly one $a = n-b$, and these are all the possibilities. Count: $\lfloor n/2\rfloor$. $\blacksquare$

*Ferrers.* By Theorem 7.6 and Corollary 7.7 it suffices to count partitions whose largest part is exactly $2$. Such a partition has the form $2^b 1^a$ with $b \ge 1$, $a \ge 0$ and $2b + a = n$; for each $b \in \{1,\dots,\lfloor n/2\rfloor\}$ the value $a = n - 2b$ is a non-negative integer, and distinct $b$ give distinct partitions. Count: $\lfloor n/2\rfloor$, as before. $\blacksquare$

**22.** *Method: Theorem 7.1 style recursion, cross-checked with the generating function.*

Let $d(n)$ be the number of compositions of $12$ (or of $n$) into parts $\ge 2$. By Exercise 14, $d(n) = F_{n-1}$, so $d(12) = F_{11} = 89$.

*Cross-check.* The generating function is $\frac{1}{1-(x^2+x^3+\cdots)} = \frac{1-x}{1-x-x^2}$, whose coefficient of $x^n$ is $F_{n+1} - F_n = F_{n-1}$. At $n = 12$: $233 - 144 = 89$ ✓.

**23.** *Method: divide the Euler product by the factors $k = 1,2$.*

We have

$$\prod_{k\ge3}\frac{1}{1-x^k} = (1-x)(1-x^2)\prod_{k\ge1}\frac{1}{1-x^k} = \big(1 - x - x^2 + x^3\big)\sum_{n\ge0}p(n)x^n .$$

Multiplying out and reading the coefficient of $x^n$ gives

$$p(n) - p(n-1) - p(n-2) + p(n-3),$$

which is therefore the number of partitions of $n$ with all parts at least $3$. $\blacksquare$

At $n = 10$: $42 - 30 - 22 + 15 = 5$. Listed, the partitions of $10$ with all parts $\ge 3$ are

$$10,\quad 7+3,\quad 6+4,\quad 5+5,\quad 4+3+3,$$

five ✓.

## Advanced

**24.** *Method: multiply the two series and compare coefficients.*

Let $P(x) = \prod_{k\ge1}(1-x^k) = \sum_{j\ge0}c_jx^j$ and $F(x) = \sum_{m\ge0}p(m)x^m$. By Theorem 7.4, $F(x) = 1/P(x)$ as formal power series, so $P(x)F(x) = 1$.

The hypothesis (pentagonal number theorem) says $c_j = (-1)^k$ when $j = g_k$ for some $k \in \mathbb{Z}$ and $c_j = 0$ otherwise; in particular $c_0 = 1$, and each $j$ corresponds to at most one $k$ (the numbers $g_k$ are distinct, indeed strictly increasing in $|k|$).

Now extract the coefficient of $x^n$ in $P(x)F(x) = 1$. For $n \ge 1$,

$$0 = [x^n]\big(P(x)F(x)\big) = \sum_{j=0}^{n} c_j\,p(n-j) = p(n) + \sum_{k \ne 0}(-1)^k p(n - g_k),$$

where the last sum is over those $k \ne 0$ with $g_k \le n$, and terms with $n - g_k < 0$ are absent. Two points must be noted:

* the sum is finite, so no convergence issue arises (formal power series);
* the convention $p(m) = 0$ for $m < 0$ lets us drop the restriction $g_k \le n$.

Rearranging,

$$p(n) = -\sum_{k\ne0}(-1)^k p(n-g_k) = \sum_{k\ne0}(-1)^{k+1}p(n-g_k).$$

Split the sum into $k > 0$ and $k < 0$. For $k > 0$ the sign is $(-1)^{k+1}$. For $k < 0$, write $k = -j$ with $j > 0$: the sign is $(-1)^{-j+1} = (-1)^{j+1}$ (because $(-1)^{-j} = (-1)^j$), and $g_{-j} = j(3j+1)/2$. Hence

$$p(n) = \sum_{k\ge1}(-1)^{k+1}\big[p(n-g_k) + p(n-g_{-k})\big] = \sum_{k\ge1}(-1)^{k-1}\big[p(n-g_k) + p(n-g_{-k})\big],$$

using $(-1)^{k+1} = (-1)^{k-1}$. This is the stated recurrence. $\blacksquare$

*Where each hypothesis is used.* The product identity $F = 1/P$ uses Theorem 7.4 (so: the definition of $p(n)$ as a coefficient of Euler's product). The sparsity of $P$ is exactly the pentagonal number theorem. The convention $p(m) = 0$ for $m<0$ is used to terminate the sum. The identity $(-1)^{-j} = (-1)^{j}$ is used to align the signs of the two families.

**25.** *Method: apply the recurrence, listing each pentagonal number with its sign.*

The generalised pentagonal numbers at most $25$ are

$$g_1 = 1,\quad g_{-1} = 2,\quad g_2 = 5,\quad g_{-2} = 7,\quad g_3 = 12,\quad g_{-3} = 15,\quad g_4 = 22,$$

since $g_{-4} = 26 > 25$ and $g_5 = 35 > 25$. The signs $(-1)^{k-1}$ are $+, +, -, -, +, +, -$. Therefore

$$\begin{aligned}
p(25) &= p(24) + p(23) - p(20) - p(18) + p(13) + p(10) - p(3) \\
&= 1575 + 1255 - 627 - 385 + 101 + 42 - 3 \\
&= 2830 - 1012 + 140 \\
&= 1958,
\end{aligned}$$

using $2830 = 1575+1255$, $1012 = 627+385$ and $140 = 101+42-3$. The result agrees with the table entry $p(25) = 1958$ ✓.

**26.** *Method: extract coefficients from the partial fractions and check the six residue classes.*

Set $n \ge 0$ and abbreviate $A(n) = p_{\le3}(n)$. From the decomposition,

$$A(n) = \frac{1}{6}\binom{n+2}{2} + \frac{n+1}{4} + \frac{1}{4}\cdot\frac{1+(-1)^n}{2} + \frac{1}{3}\cdot[3 \mid n],$$

because $[x^n](1-x)^{-3} = \binom{n+2}{2}$, $[x^n](1-x)^{-2} = n+1$, $[x^n](1-x^2)^{-1}$ is $1$ for even $n$ and $0$ for odd $n$, and $[x^n](1-x^3)^{-1}$ is $1$ when $3 \mid n$ and $0$ otherwise. Since

$$\frac{1}{6}\binom{n+2}{2} + \frac{n+1}{4} = \frac{(n+2)(n+1) + 3(n+1)}{12} = \frac{(n+1)(n+5)}{12},$$

we may write

$$A(n) = \frac{(n+1)(n+5)}{12} + \frac{1+(-1)^n}{8} + \frac{[3\mid n]}{3}.$$

Now write $n = 6m + r$ with $0 \le r \le 5$, so that $(n+3)^2 \equiv (r+3)^2 \pmod{12}$, and use

$$\frac{(n+1)(n+5)}{12} = \frac{(n+3)^2 - 4}{12}.$$

Case by case, with $k$ denoting the integer part of $(n+3)^2/12$:

| $r$ | $\dfrac{(n+3)^2}{12}$ | $A(n)$ | nearest integer to $\dfrac{(n+3)^2}{12}$ |
|---|---|---|---|
| $0$ | $k+\frac34$ | $\frac{(n+3)^2}{12}+\frac14 = k+1$ | $k+1$ ✓ |
| $1$ | $k+\frac13$ | $\frac{(n+3)^2}{12}-\frac13 = k$ | $k$ ✓ |
| $2$ | $k+\frac1{12}$ | $\frac{(n+3)^2}{12}-\frac1{12} = k$ | $k$ ✓ |
| $3$ | $k$ | $\frac{(n+3)^2}{12} = k$ | $k$ ✓ |
| $4$ | $k+\frac1{12}$ | $\frac{(n+3)^2}{12}-\frac1{12} = k$ | $k$ ✓ |
| $5$ | $k+\frac13$ | $\frac{(n+3)^2}{12}-\frac13 = k$ | $k$ ✓ |

The third column comes from $A(n) = \frac{(n+3)^2}{12} - \frac13 + \frac{1+(-1)^n}{8} + \frac{[3\mid n]}{3}$, together with $(-1)^n = +1$ for $r$ even and $-1$ for $r$ odd, and $[3 \mid n] = 1$ for $r = 0,3$. For example at $r = 0$ both corrections apply: $-\frac13+\frac14+\frac13 = +\frac14$, giving $k+\frac34+\frac14 = k+1$. At $r = 2$ only the parity correction applies: $-\frac13+\frac14 = -\frac1{12}$, giving $k$. At $r = 5$ neither applies: $-\frac13$, giving $k$. In every class the fractional part of $(n+3)^2/12$ is $0$, $\frac1{12}$, $\frac13$ or $\frac34$ — never $\frac12$ — so the nearest integer is unambiguous, and it equals $A(n)$. $\blacksquare$

*Check.* At $n = 10$: $(13)^2/12 = 14.08$, nearest integer $14 = A(10)$ ✓. At $n = 11$: $(14)^2/12 = 16.33$, nearest integer $16 = A(11)$ ✓, and $A(11) = p_{\le3}(11) = 16$ from the table.

**27.** *Method: substitute $q \mapsto q^{-1}$ in the product formula.*

By definition,

$$\binom{n}{k}_q = \prod_{i=1}^{k}\frac{1-q^{n-k+i}}{1-q^i}.$$

Substituting $q^{-1}$ for $q$ and multiplying numerator and denominator by $q^{n-k+i}$ and $q^{i}$ respectively,

$$\binom{n}{k}_{q^{-1}} = \prod_{i=1}^{k}\frac{1-q^{-(n-k+i)}}{1-q^{-i}} = \prod_{i=1}^{k}\frac{q^{-(n-k+i)}\big(q^{n-k+i}-1\big)}{q^{-i}\big(q^{i}-1\big)} = \prod_{i=1}^{k}q^{-(n-k)}\cdot\frac{1-q^{n-k+i}}{1-q^{i}},$$

where the last step uses $\frac{q^{a}-1}{q^{b}-1} = \frac{1-q^{a}}{1-q^{b}}$. The powers contribute $q^{-k(n-k)}$ and the remaining product is $\binom{n}{k}_q$, so

$$\binom{n}{k}_{q^{-1}} = q^{-k(n-k)}\binom{n}{k}_q, \qquad\text{equivalently}\qquad \binom{n}{k}_q = q^{k(n-k)}\binom{n}{k}_{q^{-1}}.$$

For the palindromic consequence, write $\binom{n}{k}_q = \sum_{j=0}^{d}a_jq^j$ with $d = k(n-k)$ (the degree, since the numerator has degree $\sum_{i=1}^k (n-k+i) = k(n-k) + k(k+1)/2$ and the denominator degree $k(k+1)/2$). Then $\binom{n}{k}_{q^{-1}} = \sum_j a_j q^{-j}$, and the identity gives

$$\sum_j a_j q^j = q^{d}\sum_j a_j q^{-j} = \sum_j a_j q^{d-j}.$$

Comparing coefficients of $q^j$ gives $a_j = a_{d-j}$: the coefficient sequence is palindromic ✓.

*Check.* $\binom42_q = 1 + q + 2q^2 + q^3 + q^4$ has $d = 4$ and coefficients $1,1,2,1,1$, palindromic ✓.

**28.** *Method: solve the inequality defining which pentagonal numbers are at most $n$.*

A nonzero term of the recurrence corresponds to an integer $k \ne 0$ with $g_k \le n$, i.e. $|k|(3|k|-1)/2 \le n$; these summands have pairwise distinct lags because the numbers $g_k$ are all different. We count them.

Set $j = |k| \ge 1$. The condition $j(3j-1)/2 \le n$ is implied by $j(3j+1)/2 \le n$, which is equivalent to

$$3j^2 + j - 2n \le 0 \iff j \le \frac{-1+\sqrt{1+24n}}{6}.$$

Let $J = \lfloor(\sqrt{24n+1}-1)/6\rfloor$, so the values $j = 1,\dots,J$ certainly contribute both $g_j$ and $g_{-j}$: that is $2J$ terms. A further term appears exactly when $g_{J+1} = (J+1)(3J+2)/2 \le n$ (while $g_{-(J+1)} > n$ by definition of $J$). Hence the number of summands is

$$2J \quad\text{or}\quad 2J+1 .$$

Since $J \le (\sqrt{24n+1}-1)/6 < \sqrt{2n/3}$, the number of terms is $O(\sqrt n)$ ✓.

*Values.* For $n = 25$: $\sqrt{601} = 24.515\ldots$, so $J = \lfloor 23.515/6\rfloor = \lfloor 3.919\rfloor = 3$; and $g_4 = 22 \le 25$, so the count is $2\cdot3+1 = 7$ ✓ (the terms $1,2,5,7,12,15,22$ of Solution 25).

For $n = 100$: $\sqrt{2401} = 49$, so $J = \lfloor 48/6\rfloor = 8$; and $g_9 = 117 > 100$, so the count is $16$ ✓ (the terms $1,2,5,7,12,15,22,26,35,40,51,57,70,77,92,100$).

**29.** *Method: condition on the last part.*

A composition of $n$ into parts from $\{1,2,3\}$ has last part $j \in \{1,2,3\}$ (for $n \ge 1$), and deleting it leaves a composition of $n-j$ into parts from $\{1,2,3\}$. This is a bijection, so

$$a_n = a_{n-1} + a_{n-2} + a_{n-3} \qquad (n \ge 3),$$

with $a_0 = 1$ (the empty composition), $a_1 = 1$, $a_2 = 2$ ($2$ and $1+1$). Computing:

| $n$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| $a_n$ | 1 | 1 | 2 | 4 | 7 | 13 | 24 | 44 | 81 | 149 | 274 |

Hence $a_{10} = 274$ ✓.

*Cross-check.* The generating function is $1/(1-x-x^2-x^3)$, whose expansion begins $1 + x + 2x^2 + 4x^3 + 7x^4 + \cdots$, consistent with the table.

**30.** *Method: multiply and telescope; then interpret the algebra bijectively.*

Let $r_d(n)$ count partitions of $n$ in which every part occurs at most $d$ times. Then

$$\sum_{n\ge0}r_d(n)x^n = \prod_{k\ge1}\big(1 + x^k + x^{2k} + \cdots + x^{dk}\big) = \prod_{k\ge1}\frac{1-x^{(d+1)k}}{1-x^k}.$$

The numerator is the product over multiples of $d+1$, so those factors cancel against the same factors in the denominator:

$$\prod_{k\ge1}\frac{1-x^{(d+1)k}}{1-x^k} = \prod_{\substack{k\ge1\\ (d+1)\nmid k}}\frac{1}{1-x^k},$$

which is the generating function for partitions into parts not divisible by $d+1$. Equal generating functions give $r_d(n) = s(n)$ for all $n$. $\blacksquare$

*Combinatorial form (Glaisher).* The algebra has a bijective shadow. Given a partition into parts not divisible by $d+1$, group equal parts: for each part $m$ with multiplicity $c_m$, write $c_m$ in base $d+1$, say $c_m = \sum_i \varepsilon_i (d+1)^i$ with digits $0 \le \varepsilon_i \le d$, and replace the $c_m$ copies of $m$ by $\varepsilon_i$ copies of $(d+1)^i m$ for each $i$. Since $m$ is not divisible by $d+1$, the numbers $(d+1)^im$ have $m$ as their $(d+1)$-free part, so parts coming from different $m$ are distinct, and each multiplicity is at most $d$. The inverse recovers $c_m$ by summing $\varepsilon_i(d+1)^i$ over the parts with $(d+1)$-free part $m$. For $d = 1$ this is Glaisher's proof of Euler's identity (binary expansion, Section 7.5); for $d = 2$ it is Exercise 17.

**31.** *Method: take logarithms of the Euler product, expand, and differentiate.*

Since the coefficient of $x^n$ involves only finitely many factors, we may compute formally:

$$\log\prod_{k\ge1}\frac{1}{1-x^k} = \sum_{k\ge1}-\log(1-x^k) = \sum_{k\ge1}\sum_{j\ge1}\frac{x^{kj}}{j}.$$

Collecting the coefficient of $x^m$: the pairs $(k,j)$ with $kj = m$ contribute $\sum_{j \mid m}\frac{1}{j} = \frac{\sigma(m)}{m}$, because the divisors $j$ of $m$ correspond to the factorisations $m = kj$. Hence

$$\log\prod_{k\ge1}\frac{1}{1-x^k} = \sum_{m\ge1}\frac{\sigma(m)}{m}x^m,$$

which is the stated identity.

Differentiating with respect to $x$ (formally, term by term) gives

$$\frac{F'(x)}{F(x)} = \sum_{m\ge1}\sigma(m)x^{m-1}, \qquad F(x) = \sum_{n\ge0}p(n)x^n .$$

Multiplying by $F$: $F'(x) = F(x)\sum_{m\ge1}\sigma(m)x^{m-1}$. Comparing coefficients of $x^{n-1}$ on both sides, and using $F'(x) = \sum_n n\,p(n)x^{n-1}$,

$$n\,p(n) = \sum_{m=1}^{n}\sigma(m)\,p(n-m).$$

*Check at $n = 6$.* Here $\sigma(1),\dots,\sigma(6) = 1,3,4,7,6,12$ and $p(5),p(4),\dots,p(0) = 7,5,3,2,1,1$. Hence

$$\sum_{m=1}^{6}\sigma(m)p(6-m) = 1\cdot7 + 3\cdot5 + 4\cdot3 + 7\cdot2 + 6\cdot1 + 12\cdot1 = 7+15+12+14+6+12 = 66 = 6\cdot 11 = 6\,p(6),$$

✓ as required.

## Challenge

**32.** *Method: cut the diagram into diagonal hooks.*

For a partition $\lambda$ let $d = \#\{i : \lambda_i \ge i\}$ be the number of diagonal cells. The **hook** of the diagonal cell $(i,i)$ is

$$H_i = \{(i,j) : i \le j \le \lambda_i\} \cup \{(k,i) : i \le k \le \lambda'_i\},$$

with arm length $\lambda_i - i$ and leg length $\lambda'_i - i$; its size is the hook length

$$\lvert H_i\rvert = \lambda_i + \lambda'_i - 2i + 1 .$$

The hooks $H_1,\dots,H_d$ are pairwise disjoint and their union is the whole diagram $D(\lambda)$: a cell $(a,b)$ with $b > a$ lies in the arm of $H_a$, a cell with $b < a$ lies in the leg of $H_b$, and the diagonal cell $(i,i)$ lies in $H_i$.

*The map.* Given a self-conjugate $\lambda \vdash n$, put

$$o_i = \lvert H_i\rvert = \lambda_i + \lambda'_i - 2i + 1 = 2(\lambda_i - i) + 1 \qquad (1 \le i \le d),$$

using $\lambda_i = \lambda'_i$. Each $o_i$ is odd and positive. They are **distinct**: $\lambda_i - i$ is strictly decreasing in $i$, because $\lambda_i \ge \lambda_{i+1}$ gives $\lambda_i - i > \lambda_{i+1} - (i+1)$. And $\sum_{i=1}^d o_i = \sum_i \lvert H_i\rvert = n$, because the hooks partition the diagram. So $o_1 > o_2 > \cdots > o_d$ is a partition of $n$ into distinct odd parts.

*The inverse map.* Given a partition of $n$ into distinct odd parts $o_1 > \cdots > o_d$, set $a_i = (o_i-1)/2$ and let $\mu$ be the union of the hooks

$$H_i' = \{(i,j) : i \le j \le i+a_i\} \cup \{(k,i) : i \le k \le i+a_i\}$$

for $i = 1,\dots,d$. Each $H_i'$ is symmetric about the diagonal and has $2a_i + 1 = o_i$ cells, so the union has $n$ cells and is symmetric, i.e. $\mu = \mu'$ provided it is a Ferrers diagram. That it is: for $k \le d$ the $k$-th row consists of the arm of $H_k'$ together with the legs of $H_i'$ for $i < k$ with $i + a_i \ge k$, so its length is $k + a_k$ (the arm reaches further than any such leg, since $i < k$); for $k > d$ the $k$-th row is the set of columns $i \le d$ with $i + a_i \ge k$. Row lengths are non-increasing: for $k < d$, $k + a_k \ge k + 1 + a_{k+1}$ because $a_k \ge a_{k+1}+1$ (distinct odd numbers differ by at least $2$); and for $k \ge d$ the set $\{i : i + a_i \ge k\}$ shrinks as $k$ grows. Finally the diagonal hooks of $\mu$ are exactly $H_1',\dots,H_d'$, so the two constructions are inverse to each other.

Therefore self-conjugate partitions of $n$ correspond bijectively to partitions of $n$ into distinct odd parts. $\blacksquare$

*Example at $n = 10$.* Distinct odd partitions: $9+1$ and $7+3$.

* $o = (9,1)$: $a = (4,0)$. Hook $1$ is a $5\times5$ cross (arm and leg $4$), hook $2$ is the single cell $(2,2)$. The rows are $5,\ 2,\ 1,\ 1,\ 1$, so $\mu = (5,2,1,1,1)$ — self-conjugate ✓.
* $o = (7,3)$: $a = (3,1)$. Rows: $1+3 = 4$; $2+1 = 3$; $2$ (column $2$ of the second leg and column $1$ of the first); $1$. So $\mu = (4,3,2,1)$ — self-conjugate ✓.

Both were found by the direct enumeration of Exercise 7, and the counts agree: $2 = 2$ ✓.

**33.** *Method: partial fractions, then estimate the contributions of the poles.*

Let $F_k(x) = \prod_{i=1}^{k}(1-x^i)^{-1} = \sum_n p_{\le k}(n)x^n$. As a rational function, $F_k$ has poles only at roots of unity.

*The pole at $1$.* Each factor satisfies $\frac{1-x^i}{1-x} \to i$ as $x \to 1$, so

$$(1-x)^kF_k(x) = \prod_{i=1}^{k}\frac{1-x}{1-x^i} \longrightarrow \prod_{i=1}^{k}\frac{1}{i} = \frac{1}{k!}$$

as $x \to 1$. Hence the principal part at $x = 1$ is $\dfrac{1}{k!\,(1-x)^k}$ plus terms of order at most $(1-x)^{-(k-1)}$.

*The other poles.* If $\zeta \ne 1$ is a root of unity and the pole at $\zeta$ has order $m$, then $m = \#\{i \le k : \zeta^i = 1\}$. Since $\zeta \ne 1$ the index $i=1$ does not contribute, so $m \le k-1$ ✓.

*Coefficient extraction.* A term $c/(1-\zeta x)^m$ contributes $c\binom{n+m-1}{m-1}\zeta^n = O(n^{m-1})$. Hence all poles other than $1$ contribute $O(n^{k-2})$, and

$$p_{\le k}(n) = \frac{1}{k!}\binom{n+k-1}{k-1} + O(n^{k-2}) = \frac{1}{k!}\cdot\frac{n^{k-1}}{(k-1)!} + O(n^{k-2}),$$

because $\binom{n+k-1}{k-1} = \frac{n^{k-1}}{(k-1)!} + O(n^{k-2})$. $\blacksquare$

*Check at $k = 3$, $n = 100$.* The leading term is $\frac{100^2}{6\cdot 2} = \frac{10000}{12} = 833.33\ldots$, while the exact value is $p_{\le3}(100) = 884$ (nearest integer to $103^2/12 = 884.08$). The difference $50.7$ is $O(n) = O(100)$ ✓, consistent with the error term.

**34.** *Method: induction on $n$ with a $q$-Pascal recurrence.*

First the recurrence. From the product formula,

$$\binom{n-1}{k}_q = \frac{(q;q)_{n-1}}{(q;q)_k(q;q)_{n-1-k}}, \qquad \binom{n-1}{k-1}_q = \frac{(q;q)_{n-1}}{(q;q)_{k-1}(q;q)_{n-k}},$$

so their ratio is $\dfrac{(q;q)_{k-1}(q;q)_{n-k}}{(q;q)_k(q;q)_{n-1-k}} = \dfrac{1-q^{n-k}}{1-q^k}$. Therefore

$$\binom{n-1}{k}_q + q^{n-k}\binom{n-1}{k-1}_q = \binom{n-1}{k-1}_q\left(\frac{1-q^{n-k}}{1-q^k} + q^{n-k}\right) = \binom{n-1}{k-1}_q\cdot\frac{1-q^n}{1-q^k} = \binom{n}{k}_q,$$

using $\binom{n}{k}_q = \frac{1-q^n}{1-q^k}\binom{n-1}{k-1}_q$ ✓.

Now let $P_n(x) = \prod_{i=0}^{n-1}(1+xq^i)$ and $S_n(x) = \sum_{k=0}^{n}q^{k(k-1)/2}\binom{n}{k}_q x^k$. We prove $P_n = S_n$ by induction on $n$.

*Base $n = 1$.* $P_1 = 1+x$ and $S_1 = \binom{1}{0}_q + \binom{1}{1}_q x = 1+x$ ✓.

*Step.* Assume $P_{n-1} = S_{n-1}$. Since $P_n = P_{n-1}(1+xq^{n-1})$,

$$[x^k]P_n = q^{k(k-1)/2}\binom{n-1}{k}_q + q^{n-1}\cdot q^{(k-1)(k-2)/2}\binom{n-1}{k-1}_q .$$

Now

$$n-1 + \frac{(k-1)(k-2)}{2} = \frac{k(k-1)}{2} + (n-k),$$

as one checks by expanding both sides, so

$$[x^k]P_n = q^{k(k-1)/2}\left[\binom{n-1}{k}_q + q^{n-k}\binom{n-1}{k-1}_q\right] = q^{k(k-1)/2}\binom{n}{k}_q = [x^k]S_n,$$

by the recurrence just proved. Hence $P_n = S_n$ ✓, completing the induction. $\blacksquare$

*Check at $n = 3$.* The left side is

$$(1+x)(1+xq)(1+xq^2) = 1 + x(1+q+q^2) + x^2(q+q^2+q^3) + x^3q^3,$$

and the right side gives

$$k=0:\ 1;\quad k=1:\ \binom31_q x = (1+q+q^2)x;\quad k=2:\ q\binom32_q x^2 = q(1+q+q^2)x^2;\quad k=3:\ q^3x^3,$$

which is the same expansion ✓.

**35.** *Method: strip the staircase $k, k-1, \dots, 1$ from the parts.*

Let $p_{\text{dist}}(n,k)$ be the number of partitions of $n$ into exactly $k$ distinct parts, written $\lambda_1 > \lambda_2 > \cdots > \lambda_k \ge 1$. Define

$$\mu_i = \lambda_i - (k - i + 1) \qquad (1 \le i \le k).$$

Then $\mu_i \ge 0$, because $\lambda_i \ge \lambda_k + (k-i) \ge 1 + k - i$, i.e. $\lambda_i \ge k-i+1$. Also $\mu_1 \ge \mu_2 \ge \cdots \ge \mu_k$, since $\lambda_i - \lambda_{i+1} \ge 1$ gives $\mu_i - \mu_{i+1} = \lambda_i - \lambda_{i+1} - 1 \ge 0$. So $\mu$ is a partition (possibly with zero parts) of

$$\sum_i \mu_i = n - \sum_{i=1}^{k}(k-i+1) = n - \frac{k(k+1)}{2},$$

with at most $k$ parts.

The map is invertible: given $\mu$ with at most $k$ parts, pad it with zeros to length $k$ and set $\lambda_i = \mu_i + (k-i+1)$; then $\lambda$ is strictly decreasing (because $\mu_i \ge \mu_{i+1}$ forces $\lambda_i \ge \lambda_{i+1}+1$) with $\lambda_k \ge 1$, so $\lambda$ has exactly $k$ distinct parts and size $\lvert\mu\rvert + k(k+1)/2$. The two maps are inverse ✓.

Therefore

$$p_{\text{dist}}(n,k) = p_{\le k}\left(n - \frac{k(k+1)}{2}\right),$$

and summing over $n$ with the generating function of $p_{\le k}$ (Section 7.8),

$$\sum_{n\ge0}p_{\text{dist}}(n,k)x^n = \frac{x^{k(k+1)/2}}{(1-x)(1-x^2)\cdots(1-x^k)}.$$

*Example $n = 12$, $k = 3$.* The count is $p_{\le3}(12 - 6) = p_{\le3}(6) = 7$, and the seven partitions are

$$9+2+1,\quad 8+3+1,\quad 7+4+1,\quad 7+3+2,\quad 6+5+1,\quad 6+4+2,\quad 5+4+3,$$

seven ✓. The generating function evaluates to $x^6/((1-x)(1-x^2)(1-x^3))$, whose coefficient of $x^{12}$ is $[x^6]\,p_{\le3}$-series $= p_{\le3}(6) = 7$ ✓.

**36.** *Method: a rational generating function forces coefficients of polynomial-times-exponential form, incompatible with the known growth of $p(n)$.*

Suppose, for contradiction, that $F(x) = \sum_{n\ge0}p(n)x^n$ is a rational function $P(x)/Q(x)$ with $P,Q \in \mathbb{C}[x]$, $Q \ne 0$, and $Q(0) \ne 0$ (true after cancelling common factors, since $F$ is finite at $0$). Factor $Q$ over $\mathbb{C}$ and apply partial fractions: there are roots $\rho_1,\dots,\rho_s \ne 0$, positive integers $m_i$ and polynomials $P_i$ of degree $< m_i$ with

$$F(x) = \sum_{i=1}^{s}\frac{P_i(1/x)}{(1-\rho_i x)^{m_i}}\quad\text{and hence}\quad p(n) = \sum_{i=1}^{s}P_i(n)\,\rho_i^{\,n}.$$

Let $R = \max_i \lvert\rho_i\rvert$ and $D = \max_i \deg P_i$. Then

$$\lvert p(n)\rvert \le C\,n^{D}R^{\,n}$$

for a constant $C$ and all $n$.

*If $R > 1$:* then for every $R' > R$ we have $p(n) \le C n^D R^n \le (R')^n$ eventually, so $p(n)$ grows at most exponentially with base $R$. But by Theorem 7.15, $p(n) \sim \frac{1}{4n\sqrt3}e^{\pi\sqrt{2n/3}}$, and $e^{\pi\sqrt{2n/3}}/(R')^n \to 0$ for every fixed $R' > 1$: $p(n)$ is *subexponential*, so no such $R$ can occur.

*If $R \le 1$:* then $p(n) \le Cn^D$, a polynomial bound. But $p(n) \ge e^{c\sqrt n}$ eventually for some $c > 0$ (again from Theorem 7.15), and $e^{c\sqrt n}/n^D \to \infty$: $p(n)$ is not polynomially bounded.

Both cases are impossible, so $F$ is not rational ✓.

Finally, if $p(n)$ satisfied a linear recurrence with constant coefficients, say $p(n) = \sum_{j=1}^{r}c_jp(n-j)$ for $n \ge r$, then multiplying the generating function by $1 - \sum_{j=1}^{r}c_jx^j$ produces a polynomial (all coefficients beyond the first $r$ vanish), so $F$ would be rational — contradicting what was just proved. Hence no such recurrence exists ✓.

*Remark.* The argument also shows why Euler's pentagonal recurrence escapes the objection: its coefficients are not constant in the sense required (the set of lags $g_k$ grows with $n$, so the recurrence has unbounded order), and the number of terms grows like $\sqrt n$.

