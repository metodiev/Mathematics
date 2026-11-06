# Counting Principles — Exercises

> [Counting Principles](README.md) · 36 problems · Beginner → Challenge · Solutions: [solutions.md](solutions.md)

Attempt every problem in writing before looking at [solutions.md](solutions.md). Each problem names the section of the tutorial that supplies the technique, so a stuck reader knows where to reread.

Notation: $[n] = \{1,2,\dots,n\}$; $\binom{n}{k}$ is the number of $k$-subsets of an $n$-set; $\binom{n}{m_1,\dots,m_r} = \dfrac{n!}{m_1!\cdots m_r!}$ with $\sum m_i = n$; by convention $\binom{n}{k} = 0$ unless $0 \le k \le n$. "Distinct" means "no repetition allowed"; "string" and "word" mean order matters and repetition is allowed unless stated otherwise. A **monotone lattice path** uses only the steps $(1,0)$ and $(0,1)$, and $\binom{p+q}{p}$ counts the paths from $(0,0)$ to $(p,q)$.

Every numerical answer must be accompanied by a check at a smaller case, as in Section 9 of the tutorial.

## Beginner

**1.** *(§5.2, §5.3)* A restaurant offers $4$ starters, $6$ main courses and $3$ desserts.
(a) How many three-course meals (starter, main, dessert) are there?
(b) How many meals are there if the starter is optional?
(c) A diner who is still hungry may have either one dessert or two desserts, where two desserts form an **unordered** pair chosen from the three kinds with repetition allowed. How many meals (starter, main, dessert or desserts) are there now?

**2.** *(§5.3, §7.2)* A password consists of two uppercase letters (A–Z, repetition allowed) followed by three digits, and the first digit may not be $0$. How many passwords are there? Then check the method on the smaller problem "one letter from $\{A,B\}$ followed by two digits from $\{1,2,3\}$" by listing all its answers.

**3.** *(§7.4)* (a) How many $4$-element subsets does a $10$-element set have? (b) How many $6$-element subsets? Explain why the two answers agree without computing the second one.

**4.** *(§7.5)* How many distinguishable arrangements are there of the letters of the word LEVEL? Check the method by listing the arrangements of the smaller multiset $\{E,E,V\}$.

**5.** *(§7.6)* In how many ways can $7$ people be seated around a circular table, if two seatings that differ only by a rotation are considered the same? What is the answer if reflections are also considered the same?

**6.** *(§7.2, §7.10)* A committee of $5$ is to be formed from $5$ women and $7$ men, and must contain exactly $2$ women and $3$ men. How many committees are possible? Compute the same number a second way, by counting all committees of $5$ and subtracting the ones that fail.

**7.** *(§7.3)* Let $\lvert A\rvert = 4$ and $\lvert B\rvert = 6$.
(a) How many functions $A \to B$ are there?
(b) How many are injective?
(c) How many injective functions $B \to A$ are there?
(d) How many bijections $A \to A$ are there?

**8.** *(§7.1, §7.12)* How many subsets of $[8]$ contain $3$ and do not contain $5$? How many contain at least one of $3$ and $5$?

**9.** *(§7.11)* How many solutions in non-negative integers does $x_1+x_2+x_3+x_4 = 12$ have? Check your formula by counting the solutions of $x_1+x_2+x_3 = 4$ directly.

**10.** *(§7.11)* How many solutions in **positive** integers does $x+y+z = 9$ have?

**11.** *(§5.3)* How many positive divisors does $720$ have? ($720 = 2^4\cdot 3^2 \cdot 5$.) How many of them are divisible by $6$?

**12.** *(§7.7)* (a) What is the coefficient of $x^3y^4$ in $(x+y)^7$? (b) What is the sum of all the coefficients of $(x+y)^7$, and why?

## Intermediate

**13.** *(§7.5)* How many distinguishable arrangements are there of the letters of MISSISSIPPI? (There are $11$ letters: M once, I four times, S four times, P twice.)

**14.** *(§7.2)* How many $5$-letter strings over a $26$-letter alphabet contain **exactly one** A? Explain carefully why the answer is not $5\cdot 26^4$.

**15.** *(§7.13)* (a) Prove the **absorption identity**
$$\binom{n}{k}\binom{k}{j} = \binom{n}{j}\binom{n-j}{k-j}$$
for $0 \le j \le k \le n$, both algebraically and by a combinatorial argument.
(b) Deduce that
$$\sum_{k=j}^{n}\binom{n}{k}\binom{k}{j} = \binom{n}{j}2^{\,n-j},$$
and check the case $n=4$, $j=2$.

**16.** *(§7.10)* Evaluate $\displaystyle\sum_{k=0}^{5}\binom{10}{k}\binom{10}{5-k}$, name the identity you used, and check the answer against a direct computation of $\binom{20}{5}$.

**17.** *(§7.13)* (a) Prove the hockey-stick identity $\displaystyle\sum_{i=r}^{n}\binom{i}{r} = \binom{n+1}{r+1}$.
(b) Use it to evaluate $\displaystyle\sum_{k=3}^{10}\binom{k}{3}$, and verify the value by adding the eight terms.

**18.** *(§7.3, §7.10)* How many monotone lattice paths run from $(0,0)$ to $(5,5)$ without passing through $(2,2)$? Count the paths through $(2,2)$ as a product and subtract.

**19.** *(§7.11)* In how many ways can $12$ identical balls be placed in $5$ distinct boxes so that no box is empty? Then answer the same question if empty boxes are allowed, and check that the difference is what the sum rule predicts.

**20.** *(§7.1, §7.2)* In how many ways can $5$ boys and $5$ girls be arranged in a row so that no two girls are adjacent? Explain why one arranges the boys first.

**21.** *(§7.3)* How many surjective functions are there from a $5$-element set to a $3$-element set? Compute the number twice: once by partitioning into fibres, and once by inclusion–exclusion. Explain why the two answers must agree.

**22.** *(§7.6)* In how many ways can $10$ people be seated around a circular table so that two particular people, A and B, are **not** adjacent?

**23.** *(§7.5)* How many distinguishable arrangements are there of the multiset $\{A,A,B,B,B,C,D\}$? How many of them begin with A?

**24.** *(§7.12)* Prove by a bijection that for $n \ge 1$ the number of subsets of $[n]$ with an even number of elements equals the number with an odd number of elements, and that each count is $2^{n-1}$. Verify at $n=4$.

## Advanced

**25.** *(§7.9)* (a) Prove Pascal's identity $\binom{n}{k} = \binom{n-1}{k-1}+\binom{n-1}{k}$ twice: combinatorially, and by algebra on the factorial formula.
(b) Use Pascal's identity and induction on $n$ to prove that $\displaystyle\sum_{k=0}^{n}\binom{n}{k} = 2^n$ for every $n \ge 0$. State clearly where the convention $\binom{n}{k}=0$ for $k\notin[0,n]$ is needed.

**26.** *(§7.13)* (a) Prove by double counting that
$$\sum_{k=0}^{n} k(k-1)\binom{n}{k} = n(n-1)\,2^{\,n-2} \qquad (n \ge 2).$$
(b) Prove the same identity by differentiating $(1+y)^n = \sum_k \binom{n}{k}y^k$ twice.
(c) Check both sides at $n=3$.

**27.** *(§7.10)* State and prove the generalised Vandermonde identity for three families of sizes $n_1, n_2, n_3$. Evaluate
$$\sum_{k_1+k_2+k_3=4}\binom{3}{k_1}\binom{4}{k_2}\binom{5}{k_3}$$
and check against $\binom{12}{4}$.

**28.** *(§7.10)* (a) Deduce from Vandermonde's identity that $\displaystyle\sum_{k=0}^{n}\binom{n}{k}^2 = \binom{2n}{n}$.
(b) Deduce also that $\displaystyle\sum_{k=0}^{n-1}\binom{n}{k}\binom{n}{k+1} = \binom{2n}{n-1}$.
(c) Check both at $n=3$.

**29.** *(§7.12)* (a) Prove by a bijection that the number of compositions of $n \ge 1$ is $2^{n-1}$.
(b) How many compositions of $6$ are there? How many have exactly three parts? Relate the second answer to a binomial coefficient and check it by listing.

**30.** *(§7.13)* Prove that for $n \ge 0$ and $m \ge 0$,
$$\sum_{k=0}^{m}\binom{n+k}{k} = \binom{n+m+1}{m},$$
once by induction on $m$ using Pascal's identity, and once by recognising it as a hockey stick. Check at $n=2$, $m=3$.

**31.** *(§7.3, §7.12)* Show that the number of monotone lattice paths from $(0,0)$ to $(n,n)$ that never go above the line $y=x$ is $\binom{2n}{n}-\binom{2n}{n+1}$. Evaluate this for $n=1,2,3,4,5$ and identify the sequence. Say precisely what the reflection does to a bad path.

## Challenge

**32.** *(§7.1, §7.2, §7.4)* How many $5$-card hands, dealt from a standard $52$-card deck ($4$ suits, $13$ ranks), use cards from **exactly two** suits? Answer twice: once by counting all hands from a fixed pair of suits and excluding the monochromatic ones, and once by splitting into suit patterns $4+1$ and $3+2$. (This is an AIME-style problem; the answer is a five-digit number.)

**33.** *(§7.12)* (a) Prove that the number of $k$-element subsets $\{a_1<\cdots<a_k\}$ of $[n]$ with $a_{i+1} \ge a_i+2$ for all $i$ is $\binom{n-k+1}{k}$.
(b) Evaluate it for $n=10$, $k=4$; then check the formula by listing the case $n=6$, $k=3$.
(c) Evaluate it for $n=2m$, $k=3$, and simplify the resulting expression.

**34.** *(§7.12)* Let $S_n$ be the number of subsets of $[n]$ containing no two consecutive integers. Prove that $S_n = F_{n+2}$, where $F_1=F_2=1$ and $F_n = F_{n-1}+F_{n-2}$. Compute $S_1, \dots, S_6$ and check.

**35.** *(§7.7, §7.13)* Prove that for every $n \ge 0$,
$$\sum_{k=0}^{n}\frac{1}{\binom{n}{k}} = \frac{n+1}{2^{\,n+1}}\sum_{k=1}^{n+1}\frac{2^k}{k}.$$
*Hint:* first prove $\dfrac{1}{\binom{n}{k}} = \dfrac{n+1}{n+2}\left(\dfrac{1}{\binom{n+1}{k}}+\dfrac{1}{\binom{n+1}{k+1}}\right)$, then sum over $k$ and induct.

**36.** *(§5.3, §7.5)* Twelve people are to be split into three groups of four, with the groups unlabelled (so that the split $\{1,2,3,4\},\{5,6,7,8\},\{9,10,11,12\}$ is the same as any reordering of the three blocks).
(a) How many such splits are there? Explain carefully why division by $3!$ is justified.
(b) How many splits put two particular people A and B in the same group?
(c) Check that the answers to (a) and (b) are consistent by computing the probability that A and B are in the same group in two ways.
