# Sequences and Series — Solutions

> [Tutorial](README.md) · [Exercises](exercises.md) · 34 worked solutions

Each solution states the strategy, carries out every step, and ends with an answer and a check. Proofs
state the statement, the base case, the inductive hypothesis and the conclusion.

## Beginner

**1.**

**Strategy.** Substitute $n = 1, 2, 3, 4, 5$ into $a_n = 3n-1$.

$$a_1 = 2,\quad a_2 = 5,\quad a_3 = 8,\quad a_4 = 11,\quad a_5 = 14.$$

**Answer.** $2,\ 5,\ 8,\ 11,\ 14$. The sequence is arithmetic with $d = 3$.

**Check.** The differences are all $3$, and $a_1 = 3(1)-1 = 2$. $\checkmark$

**2.**

**Strategy.** Arithmetic with $a_1 = 5$ and $d = 9-5 = 4$; use $a_n = a_1+(n-1)d$.

$$a_{20} = 5+19\cdot4 = 5+76 = 81.$$

**Answer.** $a_{20} = 81$.

**Check.** The sequence is $5, 9, 13, \dots$; the first term with $n=1$ is $5$, and $19$ steps of $4$
from $5$ gives $81$. $\checkmark$

**3.**

**Strategy.** Arithmetic with $a_1 = 2$, $d = 3$; find $a_{30}$ then apply $S_n = \frac{n}{2}(a_1+a_n)$.

$$a_{30} = 2+29\cdot3 = 2+87 = 89, \qquad S_{30} = \frac{30(2+89)}{2} = 15\cdot91 = 1365.$$

**Answer.** $1365$.

**Check.** Using the other form, $S_{30} = \frac{30}{2}\left(2\cdot2+29\cdot3\right) = 15(4+87) = 15\cdot91 = 1365$.
$\checkmark$

**4.**

**Strategy.** Geometric with $a_1 = 3$ and $r = 6/3 = 2$.

$$a_8 = 3\cdot2^{7} = 3\cdot128 = 384, \qquad S_8 = 3\,\frac{2^{8}-1}{2-1} = 3(255) = 765.$$

**Answer.** $a_8 = 384$ and $S_8 = 765$.

**Check.** The terms are $3, 6, 12, 24, 48, 96, 192, 384$; their sum is $765$ (add the first four:
$45$; the last four: $720$; total $765$). $\checkmark$

**5.**

**Strategy.** Use $\sum_{k=1}^{n}k = \frac{n(n+1)}{2}$ with $n = 10$.

$$\sum_{k=1}^{10}k = \frac{10\cdot11}{2} = 55.$$

**Answer.** $55$.

**Check.** Gauss pairing: five pairs each summing to $11$. $\checkmark$

**6.**

**Strategy.** Split by linearity and count the terms: there are $10$ terms in $\sum_{k=1}^{10}2$.

$$\sum_{k=1}^{10}(3k+2) = 3\sum_{k=1}^{10}k+2\cdot10 = 3(55)+20 = 165+20 = 185.$$

**Answer.** $185$.

**Check.** The terms are $5, 8, 11, \dots, 32$, ten of them; $S = \frac{10(5+32)}{2} = 5\cdot37 = 185$. $\checkmark$

**7.**

**Strategy.** This is a geometric sum with $a_1 = 2$, $r = 2$ and $6$ terms.

$$\sum_{k=1}^{6}2^{k} = 2\,\frac{2^{6}-1}{2-1} = 2(63) = 126.$$

**Answer.** $126$.

**Check.** $2+4+8+16+32+64 = 126$. $\checkmark$ Note that the sum starts at $2^1$, not $2^0$, which is
why the answer is $2(2^6-1)$ and not $2^7-1 = 127$.

**8.**

**Strategy.** Use $\sum_{k=1}^{n}k^2 = \frac{n(n+1)(2n+1)}{6}$ with $n = 20$.

$$\sum_{k=1}^{20}k^2 = \frac{20\cdot21\cdot41}{6} = \frac{17220}{6} = 2870.$$

**Answer.** $2870$.

**Check.** $\sum_{k=1}^{20}k = 210$ and $\sum k^3 = 210^2 = 44100$; the square sum must lie between them,
and $2870$ does. $\checkmark$

**9.**

**Strategy.** Use the factorial formula.

$$\binom{7}{3} = \frac{7!}{3!\,4!} = \frac{5040}{6\cdot24} = \frac{5040}{144} = 35, \qquad \binom{7}{4} = \frac{7!}{4!\,3!} = 35.$$

**Answer.** Both are $35$.

**Why they agree.** Choosing the $3$ elements that are *in* a subset is the same act as choosing the
$4$ elements that are *out*, so $\binom{n}{k} = \binom{n}{n-k}$; the factorial formula shows it because
the two denominators are interchanged. $\checkmark$

**10.**

**Strategy.** Apply the binomial theorem with $n=3$, and read the coefficients from row $3$ of Pascal's
triangle, $1, 3, 3, 1$.

$$(x+2)^3 = \binom30 x^3 + \binom31 x^2(2)+\binom32 x(2)^2+\binom33(2)^3 = x^3+6x^2+12x+8.$$

**Answer.** $x^3+6x^2+12x+8$.

**Check.** Put $x=1$: the expansion gives $1+6+12+8 = 27 = 3^3$ ✓. Put $x=-2$: the expansion gives
$-8+24-24+8 = 0 = (0)^3$ ✓.

**11.**

**Strategy.** The general term of $(1+2x)^6$ is $\binom{6}{k}1^{6-k}(2x)^k$; the power of $x$ is $k$, so
take $k=4$.

$$\binom{6}{4}(2x)^4 = 15\cdot16x^4 = 240x^4.$$

**Answer.** $240x^4$.

**Check.** $\binom64 = 15$ from row $6$ of Pascal's triangle, and $2^4 = 16$; $15\cdot16 = 240$. $\checkmark$

**12.**

**Strategy.** Write the decimal as a geometric series.

$$0.\overline{5} = \frac{5}{10}+\frac{5}{100}+\frac{5}{1000}+\cdots = \frac{5/10}{1-1/10} = \frac{1/2}{9/10} = \frac{5}{9}.$$

**Answer.** $\dfrac59$.

**Check.** $5/9 = 0.5555\dots$ by long division ✓. Multiplying by $9$: $9\cdot0.5555\dots = 4.9995\dots = 5$ ✓.

## Intermediate

**13.**

**Strategy.** Reindex with $j = k-2$, so $k = j+2$, and the new lower limit is $j=1$.

$$\sum_{k=3}^{n+2}(4k-1) = \sum_{j=1}^{n}\left(4(j+2)-1\right) = \sum_{j=1}^{n}(4j+7).$$

There are $n$ terms in both sums, as there must be: $(n+2)-3+1 = n$. Now

$$\sum_{j=1}^{n}(4j+7) = 4\cdot\frac{n(n+1)}{2}+7n = 2n^2+2n+7n = 2n^2+9n.$$

At $n = 10$: $2(100)+90 = 290$.

**Direct check.** The terms are those of $k = 3,4,\dots,12$, namely $11, 15, \dots, 47$: ten terms of
an arithmetic progression with average $\frac{11+47}{2} = 29$, so the sum is $290$. $\checkmark$

**Answer.** $\displaystyle\sum_{j=1}^{n}(4j+7) = 2n^2+9n$, which is $290$ at $n=10$.

**14.**

**Strategy.** Split the sum and use the power sums; alternatively note that $2k-1$ is arithmetic with
$d=2$.

$$\sum_{k=1}^{n}(2k-1) = 2\sum_{k=1}^{n}k-\sum_{k=1}^{n}1 = 2\cdot\frac{n(n+1)}{2}-n = n^2+n-n = n^2.$$

**Second method.** The terms $1, 3, 5, \dots, 2n-1$ form an arithmetic progression with first term $1$,
last term $2n-1$ and $n$ terms, so the sum is $\frac{n}{2}\left(1+(2n-1)\right) = \frac{n(2n)}{2} = n^2$.

**Answer.** $n^2$ — the sum of the first $n$ odd numbers.

**Check.** $n=4$: $1+3+5+7 = 16 = 4^2$ ✓.

**15.**

**Strategy.** Split into two power sums and substitute $n = 50$.

$$\sum_{k=1}^{50}\left(k^2-k\right) = \frac{50\cdot51\cdot101}{6}-\frac{50\cdot51}{2} = 42925-1275 = 41650.$$

**Answer.** $41650$.

**Check.** Factor the answer: $41650 = 50\cdot833$, and $833 = \frac{51\cdot98}{6} = \frac{4998}{6}$, so
$41650 = 50\cdot51\cdot\frac{98}{6} = 50\cdot51\left(\frac{101}{6}-\frac12\right)$, which is the closed
form $\frac{n(n+1)(2n+1)}{6}-\frac{n(n+1)}{2}$ at $n=50$ ✓.

**16.**

**Strategy.** Write out the cancellation; this is a telescoping sum of the form $b_k-b_{k+1}$ with
$b_k = \frac{1}{k+1}$.

$$\sum_{k=1}^{n}\left(\frac{1}{k+1}-\frac{1}{k+2}\right) = \left(\frac12-\frac13\right)+\left(\frac13-\frac14\right)+\cdots+\left(\frac{1}{n+1}-\frac{1}{n+2}\right) = \frac12-\frac{1}{n+2}.$$

As $n\to\infty$, $\frac{1}{n+2}\to0$, so the infinite series converges to $\frac12$.

**Answer.** $\dfrac12-\dfrac{1}{n+2}$, with limit $\dfrac12$.

**Check.** $n=1$: the single term is $\frac12-\frac13 = \frac16$, and the formula gives
$\frac12-\frac13 = \frac16$ ✓.

**17.**

**Strategy.** Geometric series with $a = 3$ and $r = \frac14$; since $|r|<1$ use $\frac{a}{1-r}$.

$$\sum_{k=1}^{\infty}3\left(\frac14\right)^{k-1} = \frac{3}{1-\frac14} = \frac{3}{3/4} = 4.$$

**Answer.** $4$.

**Check.** The partial sums are $3,\ 3.75,\ 3.9375,\ 3.984375,\dots$, increasing toward $4$. $\checkmark$

**18.**

**Strategy.** Use $S = \frac{a}{1-r}$ with $a = 8$ and $S = 12$.

$$\frac{8}{1-r} = 12 \quad\Longrightarrow\quad 1-r = \frac{8}{12} = \frac23 \quad\Longrightarrow\quad r = \frac13.$$

Since $\left|\frac13\right|<1$, the convergence condition is satisfied — as it must be, since a finite
sum of an infinite geometric series requires it.

**Answer.** $r = \dfrac13$.

**Check.** $\frac{8}{1-1/3} = \frac{8}{2/3} = 12$ ✓.

**19.**

**Strategy.** The positive multiples of $7$ are $7\cdot1, 7\cdot2, \dots$; factor out the $7$ and use the
arithmetic sum.

$$\sum_{k=1}^{15}7k = 7\cdot\frac{15\cdot16}{2} = 7\cdot120 = 840.$$

**Answer.** $840$.

**Check.** Arithmetic with first term $7$, last term $105$ and $15$ terms: $\frac{15(7+105)}{2} = \frac{15(112)}{2} = 840$ ✓.

**20.**

**Statement.** $P(n)$: $\displaystyle\sum_{k=1}^{n}(2k-1) = n^2$.

**Base case.** $n=1$: the left side is $2(1)-1 = 1$ and the right side is $1^2 = 1$. ✓

**Inductive hypothesis.** Assume $P(n)$: $\sum_{k=1}^{n}(2k-1) = n^2$, for some $n\ge1$.

**Step.** Then

$$\sum_{k=1}^{n+1}(2k-1) = \sum_{k=1}^{n}(2k-1)+\big(2(n+1)-1\big) = n^2+2n+1 = (n+1)^2,$$

which is $P(n+1)$.

**Conclusion.** By the principle of induction, $P(n)$ holds for every $n\ge1$. $\blacksquare$

**Check.** $n=5$: $1+3+5+7+9 = 25 = 5^2$ ✓.

**21.**

**Strategy.** The general term of $(2x-3)^7$ is $\binom{7}{k}(2x)^{7-k}(-3)^k$. For $x^5$ take $7-k = 5$,
i.e. $k = 2$.

$$\binom{7}{2}(2x)^{5}(-3)^{2} = 21\cdot32x^5\cdot9 = 6048\,x^5.$$

**Answer.** $6048$.

**Check.** $\binom72 = 21$, $2^5 = 32$, $(-3)^2 = 9$, and $21\cdot32\cdot9 = 6048$ ✓. The exponent count is
$5+2 = 7$ ✓.

**22.**

**Strategy.** Write the general term and force the exponent of $x$ to be $0$.

$$\binom{6}{k}\left(x^2\right)^{6-k}\left(\frac{2}{x}\right)^{k} = \binom{6}{k}2^{k}x^{12-2k-k} = \binom{6}{k}2^{k}x^{12-3k}.$$

The exponent vanishes when $12-3k = 0$, i.e. $k = 4$. The term is

$$\binom{6}{4}2^{4} = 15\cdot16 = 240.$$

**Answer.** $240$.

**Check.** $\binom64 = \binom62 = 15$; $2^4 = 16$; $15\cdot16 = 240$ ✓. The exponents $2(6-4) = 4$ and
$4$ (from $x^{-4}$) cancel ✓.

## Advanced

**23.**

**Statement.** $P(n)$: $\displaystyle\sum_{k=1}^{n}k(k+1) = \frac{n(n+1)(n+2)}{3}$.

**Base case.** $n=1$: left side $1\cdot2 = 2$; right side $\frac{1\cdot2\cdot3}{3} = 2$. ✓

**Inductive hypothesis.** Assume $P(n)$ for some $n\ge1$.

**Step.** Add the next term:

$$\begin{aligned}
\sum_{k=1}^{n+1}k(k+1) &= \frac{n(n+1)(n+2)}{3}+(n+1)(n+2) \\
&= (n+1)(n+2)\left(\frac{n}{3}+1\right) = \frac{(n+1)(n+2)(n+3)}{3},
\end{aligned}$$

which is $P(n+1)$.

**Conclusion.** By induction, $P(n)$ holds for all $n\ge1$. $\blacksquare$

**Check.** $n=5$: $2+6+12+20+30 = 70$, and $\frac{5\cdot6\cdot7}{3} = 70$ ✓.

**24.**

**Strategy.** Partial fractions, then telescope.

Since

$$\frac{1}{2k-1}-\frac{1}{2k+1} = \frac{(2k+1)-(2k-1)}{(2k-1)(2k+1)} = \frac{2}{(2k-1)(2k+1)},$$

we have $\dfrac{1}{(2k-1)(2k+1)} = \dfrac12\left(\dfrac{1}{2k-1}-\dfrac{1}{2k+1}\right)$. Summing,

$$\begin{aligned}
\sum_{k=1}^{n}\frac{1}{(2k-1)(2k+1)} &= \frac12\left[\left(1-\frac13\right)+\left(\frac13-\frac15\right)+\cdots+\left(\frac{1}{2n-1}-\frac{1}{2n+1}\right)\right] \\
&= \frac12\left(1-\frac{1}{2n+1}\right) = \frac12\cdot\frac{2n}{2n+1} = \frac{n}{2n+1}.
\end{aligned}$$

As $n\to\infty$ the sum tends to $\frac12$.

**Answer.** $\dfrac{n}{2n+1}$, with infinite sum $\dfrac12$.

**Check.** $n=3$: $\frac13+\frac1{15}+\frac1{35} = \frac{35+7+3}{105} = \frac{45}{105} = \frac37$, and
$\frac{3}{7}$ is the formula's value ✓.

**25.**

**(i) By the binomial theorem.** Put $x = y = 1$ in $(x+y)^n = \sum_k\binom{n}{k}x^{n-k}y^k$. The left side
is $2^n$ and the right side is $\sum_k\binom{n}{k}$. $\blacksquare$

**(ii) By counting.** Let $S$ be a set with $n$ elements. Counting its subsets by size gives
$\sum_{k=0}^{n}\binom{n}{k}$ subsets. Counting them by choices gives $2^n$: each of the $n$ elements is
in or out, independently. Both count the same collection, so the totals are equal. $\blacksquare$

**(iii) The alternating sum.** Put $x = 1$ and $y = -1$ in the binomial theorem:

$$(1-1)^n = \sum_{k=0}^{n}\binom{n}{k}(-1)^k .$$

For $n\ge1$ the left side is $0$, which proves $\sum_k(-1)^k\binom{n}{k} = 0$. Equivalently, a non-empty
set has equally many even-sized as odd-sized subsets, since toggling a fixed element pairs them up.

**Check.** $n=3$: $1-3+3-1 = 0$ ✓. $n=4$: $1-4+6-4+1 = 0$ ✓.

**26.**

**Strategy.** Compare with the geometric series and bound the partial sums from below by the first term.

For every $k\ge1$, $2^k+1>2^k$, so

$$0<\frac{1}{2^k+1}<\frac{1}{2^k}.$$

The series $\sum_{k\ge1}\frac{1}{2^k}$ converges to $1$ (geometric with $a=r=\frac12$). Since the partial
sums $S_n$ of $\sum\frac{1}{2^k+1}$ are increasing (all terms are positive) and bounded above by $1$,
the monotone convergence theorem (Section 7.13) gives convergence, and $S\le1$. Strictly, $S<1$ because
the first term is already strictly smaller than $\frac12$ and the bounding series sums to $1$.

For the lower bound, all terms are positive, so $S>S_1 = \frac{1}{3}$.

**Answer.** The series converges, with $\frac13<S<1$. (Numerically $S\approx0.7645$.)

**Check.** The first four partial sums are $0.3333$, $0.5333$, $0.6444$, $0.7032$, rising and staying below
$1$ ✓.

**27.**

**Strategy.** Sum the geometric series (first term $2$, ratio $1.05$, $n$ terms) and solve the inequality
for $n$, using logarithms.

$$S_n = 2\,\frac{(1.05)^n-1}{1.05-1} = 40\left((1.05)^n-1\right).$$

The condition $S_n>50$ becomes $40\left((1.05)^n-1\right)>50$, i.e. $(1.05)^n>1+\frac{50}{40} = 2.25$. Taking
logarithms,

$$n > \frac{\ln 2.25}{\ln 1.05} \approx \frac{0.81093}{0.04879} \approx 16.62.$$

So the smallest integer is $n = 17$.

**Check.** $(1.05)^{16} \approx 2.18287$ and $(1.05)^{17}\approx 2.29202$, so
$S_{16}\approx 40(1.18287) = 47.31<50$ and $S_{17}\approx 40(1.29202) = 51.68>50$ ✓.

**Answer.** $n = 17$.

**28.**

**Statement.** For integers $1\le k\le n$,

$$\binom{n}{k} = \binom{n-1}{k-1}+\binom{n-1}{k},$$

with the conventions $\binom{m}{0} = 1$ and $\binom{m}{m} = 1$.

**Proof.** Put the two terms on the right over the common denominator $k!\,(n-k)!$. For the first,

$$\binom{n-1}{k-1} = \frac{(n-1)!}{(k-1)!\,(n-k)!} = \frac{(n-1)!\cdot k}{(k-1)!\cdot k\cdot(n-k)!} = \frac{k\,(n-1)!}{k!\,(n-k)!},$$

and for the second,

$$\binom{n-1}{k} = \frac{(n-1)!}{k!\,(n-1-k)!} = \frac{(n-1)!\cdot(n-k)}{k!\,(n-k)!}.$$

Adding the numerators, $k+(n-k) = n$, so

$$\binom{n-1}{k-1}+\binom{n-1}{k} = \frac{n\,(n-1)!}{k!\,(n-k)!} = \frac{n!}{k!\,(n-k)!} = \binom{n}{k}. \qquad\blacksquare$$

**Range.** The identity holds for $1\le k\le n-1$ with both terms defined by the factorial formula; at
the endpoints $k=0$ and $k=n$ it is the convention $\binom{n}{0} = \binom{n}{n} = 1$ together with
$\binom{n-1}{-1} = \binom{n-1}{n} = 0$. Those zero conventions are what make the binomial-theorem proof
work without checking the end terms separately.

**Check.** $n=5$, $k=2$: $\binom52 = 10$, and $\binom41+\binom42 = 4+6 = 10$ ✓.

**29.**

**Strategy.** Count the pairs $(A,x)$ with $A\subseteq S$, $|A| = k$ and $x \in A$, in two ways.

Let $S$ be a set with $n$ elements.

*Count by size of $A$.* For each $k$, there are $\binom{n}{k}$ subsets of size $k$, and for each such
subset there are $k$ choices of $x \in A$. So the number of pairs is $\sum_{k=0}^{n}k\binom{n}{k}$.

*Count by the element $x$.* There are $n$ choices of $x$. Once $x$ is fixed, $A$ must contain $x$, and
each of the remaining $n-1$ elements may be in or out of $A$ independently: $2^{n-1}$ choices. So the
number of pairs is $n\,2^{n-1}$.

The two counts agree, so $\sum_k k\binom{n}{k} = n2^{n-1}$. $\blacksquare$

**Check.** $n=4$: $0\cdot1+1\cdot4+2\cdot6+3\cdot4+4\cdot1 = 4+12+12+4 = 32 = 4\cdot2^3$ ✓.

**30.**

**Strategy.** Group the terms into blocks whose sums are each at least $\frac12$, and show that the
partial sums are unbounded.

Write the series as

$$1+\frac12+\left(\frac13+\frac14\right)+\left(\frac15+\frac16+\frac17+\frac18\right)+\left(\frac19+\cdots+\frac1{16}\right)+\cdots,$$

where the $j$-th block (for $j\ge1$) contains the $2^{j-1}$ terms from $\frac{1}{2^{j-1}+1}$ to
$\frac{1}{2^{j}}$. Every term in that block is at least $\frac{1}{2^{j}}$ (the smallest term is the
last), so the block's total is at least

$$2^{j-1}\cdot\frac{1}{2^{j}} = \frac12 .$$

Therefore the partial sum up to the end of block $J$ satisfies

$$S_{2^{J}} \ge 1+\frac12+\frac12+\cdots+\frac12 = 1+\frac{J}{2},$$

using $J$ blocks each contributing at least $\frac12$. As $J\to\infty$ the right side tends to infinity,
so the partial sums are unbounded and the series diverges. $\blacksquare$

**Remark.** This is why the $n$-th term test cannot be reversed: $\frac1n\to0$ and yet $\sum\frac1n$
diverges. Convergence depends on how *fast* the terms shrink, not merely on their shrinking.

**Check.** $S_1 = 1$, $S_2 = 1.5$, $S_4\ge2$, $S_8\ge2.5$, $S_{16}\ge3$ (actually $S_{16}\approx3.38$) —
the bound $1+J/2$ is true but not tight. $\checkmark$

## Challenge

**31.**

**Strategy.** Write the summand as a difference of consecutive terms of the sequence
$b_k = \dfrac{1}{k(k+1)}$, then telescope.

First decompose into partial fractions. Suppose
$\dfrac{1}{k(k+1)(k+2)} = \dfrac{A}{k}+\dfrac{B}{k+1}+\dfrac{C}{k+2}$. Clearing denominators,

$$1 = A(k+1)(k+2)+Bk(k+2)+Ck(k+1).$$

At $k=0$: $1 = 2A$, so $A = \frac12$. At $k=-1$: $1 = -B$, so $B = -1$. At $k=-2$: $1 = 2C$, so
$C = \frac12$. Hence

$$\frac{1}{k(k+1)(k+2)} = \frac12\left(\frac1k-\frac{2}{k+1}+\frac{1}{k+2}\right) = \frac12\left[\left(\frac1k-\frac1{k+1}\right)-\left(\frac1{k+1}-\frac1{k+2}\right)\right].$$

So with $b_k = \dfrac{1}{k(k+1)}$ the summand is $\frac12\left(b_k-b_{k+1}\right)$, and

$$\sum_{k=1}^{n}\frac{1}{k(k+1)(k+2)} = \frac12\left(b_1-b_{n+1}\right) = \frac12\left(\frac12-\frac{1}{(n+1)(n+2)}\right).$$

As $n\to\infty$ the second term vanishes, leaving $\frac12\cdot\frac12 = \frac14$.

**Answer.** $\dfrac14$.

**Check.** The first terms are $\frac16+\frac1{24}+\frac1{60}+\frac1{120} = \frac{20+5+2+1}{120} = \frac{28}{120} = 0.2333$, and
the limit $\frac14 = 0.25$ is slightly above it ✓. Numerically the series sums to $0.250000$ ✓.

**32.**

**Strategy.** Partial fractions with a lag of three, then count the survivors at each end.

$$\frac{1}{k(k+3)} = \frac13\left(\frac1k-\frac1{k+3}\right),$$

because $\frac{(k+3)-k}{k(k+3)} = \frac{3}{k(k+3)}$. Summing from $k=1$ to $n$:

$$\sum_{k=1}^{n}\frac{1}{k(k+3)} = \frac13\sum_{k=1}^{n}\left(\frac1k-\frac1{k+3}\right).$$

Writing out the terms, the positive parts are $\frac11,\frac12,\frac13,\frac14,\dots,\frac1n$ and the
negative parts are $\frac14,\frac15,\dots,\frac1{n+3}$. Each $\frac1j$ with $4\le j\le n$ cancels. The
survivors are the first three positives and the last three negatives:

$$\sum_{k=1}^{n}\frac{1}{k(k+3)} = \frac13\left(1+\frac12+\frac13-\frac{1}{n+1}-\frac{1}{n+2}-\frac{1}{n+3}\right).$$

Since $1+\frac12+\frac13 = \frac{11}{6}$, the sum is $\frac13\left(\frac{11}{6}-\frac{1}{n+1}-\frac{1}{n+2}-\frac{1}{n+3}\right)$, and as
$n\to\infty$ it tends to $\frac{11}{18}$.

**Why six survive.** The gap between $k$ and $k+3$ is three, so three positive terms at the start find no
partner among the negatives of earlier terms, and three negative terms at the end never cancel.

**Check.** $n=3$: the terms are $\frac14+\frac1{10}+\frac1{18} = 0.25+0.1+0.05556 = 0.40556$. The formula
gives $\frac13\left(\frac{11}{6}-\frac14-\frac15-\frac16\right) = \frac13\left(1.83333-0.61667\right) = \frac13(1.21667) = 0.40556$ ✓.

**Answer.** $\dfrac13\left(\dfrac{11}{6}-\dfrac{1}{n+1}-\dfrac{1}{n+2}-\dfrac{1}{n+3}\right)\to\dfrac{11}{18}$.

**33.**

**Strategy.** Solve the recurrence by unrolling, set $B_{180} = 0$, and solve for $M$.

The monthly rate is $i = 0.048/12 = 0.004$ and there are $n = 180$ payments. The balance after $m$
payments satisfies $B_m = (1+i)B_{m-1}-M$ with $B_0 = 150000$. Unrolling:

$$\begin{aligned}
B_1 &= B_0(1+i)-M, \\
B_2 &= B_0(1+i)^2-M(1+i)-M, \\
&\ \vdots \\
B_n &= B_0(1+i)^n - M\left[(1+i)^{n-1}+(1+i)^{n-2}+\cdots+1\right] \\
&= B_0(1+i)^n - M\,\frac{(1+i)^n-1}{i},
\end{aligned}$$

where the bracket was summed as a geometric series with $n$ terms, first term $1$ and ratio $1+i$.
Setting $B_n = 0$ and solving for $M$:

$$M = B_0\,\frac{i(1+i)^n}{(1+i)^n-1}.$$

Now $(1.004)^{180} \approx 2.051485$, so

$$M = 150000\cdot\frac{0.004(2.051485)}{1.051485} \approx 150000\cdot\frac{0.00820594}{1.051485} \approx 150000(0.0078041) \approx 1170.62.$$

Total repaid $= 180(1170.62) = \$210{,}711.60$; total interest $= \$210{,}711.60-\$150{,}000 = \$60{,}711.60$.

**Check.** Back-substitute at $m=180$:
$B_{180} = 150000(2.051485)-1170.62\cdot\frac{1.051485}{0.004} = 307{,}722.75-1170.62(262.871)$.
Now $1170.62\times262.871 \approx 307{,}722$, so $B_{180}\approx0$ ✓. Also, a single payment after one
month leaves $150000(1.004)-1170.62 = 150{,}600-1170.62 = \$149{,}429.38$, a fall of about $\$571$, which
is small compared with the payment because $\$600$ of it went to interest ✓.

**Answer.** $M \approx \$1170.62$ per month; total repaid $\approx\$210{,}712$; total interest
$\approx\$60{,}712$.

**34.**

**Strategy.** Count $n$-person committees from a group of $n$ women and $n$ men, by composition and by
selection.

Let $W$ be a set of $n$ women and $M$ a set of $n$ men, with $W$ and $M$ disjoint, so that $W\cup M$ has
$2n$ people.

*Count by selection.* The number of $n$-person committees chosen from the $2n$ people is
$\binom{2n}{n}$.

*Count by composition.* Suppose the committee contains exactly $k$ women. Then it contains $n-k$ men.
There are $\binom{n}{k}$ ways to choose the women and $\binom{n}{n-k}$ ways to choose the men, and these
choices are independent, so there are $\binom{n}{k}\binom{n}{n-k} = \binom{n}{k}^2$ such committees, the
last equality because $\binom{n}{n-k} = \binom{n}{k}$. Summing over the possible values $k = 0,1,\dots,n$
counts every committee exactly once, giving $\sum_{k=0}^{n}\binom{n}{k}^2$.

Both expressions count the same set of committees, so

$$\sum_{k=0}^{n}\binom{n}{k}^{2} = \binom{2n}{n}. \qquad\blacksquare$$

**Check.** $n=3$: the left side is $1^2+3^2+3^2+1^2 = 20$, and $\binom63 = 20$ ✓. $n=4$:
$1+16+36+16+1 = 70 = \binom84$ ✓.

**Remark.** This is the case $m = n$ of Vandermonde's identity
$\sum_k\binom{m}{k}\binom{n}{n-k} = \binom{m+n}{n}$, which the same argument proves with $m$ men instead
of $n$.