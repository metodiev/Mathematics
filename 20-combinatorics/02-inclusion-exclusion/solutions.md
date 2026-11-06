# Inclusion–Exclusion — Solutions

> [Inclusion–Exclusion](README.md) · Solutions to the 36 problems in [exercises.md](exercises.md)

Each solution names the universe and the bad properties, computes a general intersection, performs the alternating sum, and checks the answer on a small case. Where a problem has a second approach, it is given or indicated.

## Beginner

**1.** *Universe: $A \cup B$. Two sets, one correction.*

$$\lvert A \cup B\rvert = \lvert A\rvert + \lvert B\rvert - \lvert A\cap B\rvert = 14 + 23 - 9 = 28 .$$

The difference sets are computed by the same identity rearranged:

$$\lvert A \setminus B\rvert = \lvert A\rvert - \lvert A\cap B\rvert = 14 - 9 = 5, \qquad \lvert B\setminus A\rvert = 23 - 9 = 14 .$$

Elements in exactly one set number $5 + 14 = 19$.

*Check.* The three disjoint pieces have sizes $5$, $9$, $14$ and sum to $28 = \lvert A\cup B\rvert$. ✓ Also $19 + 9 = 28$. ✓

**2.** *Universe: the $40$ students. Bad properties: "does not study French", equivalently count the positives.*

$$\lvert F \cup G\rvert = 26 + 21 - 12 = 35 .$$

At least one language: $35$. Exactly one: $(26-12) + (21-12) = 14 + 9 = 23$. Neither: $40 - 35 = 5$.

The four Venn regions are French only $14$, German only $9$, both $12$, neither $5$.

*Check.* $14 + 12 = 26 = \lvert F\rvert$; $9 + 12 = 21 = \lvert G\rvert$; $14+9+12+5 = 40$. ✓ Also exactly one plus both equals the union: $23 + 12 = 35$. ✓

**3.** *Universe: $A\cup B\cup C$. Three sets, three corrections.*

$$\lvert A\cup B\cup C\rvert = 20 + 17 + 13 - (8 + 6 + 5) + 3 = 50 - 19 + 3 = 34 .$$

The seven non-empty regions, computed from the inside out:

| Region | Size | Reason |
|---|---|---|
| $A\cap B\cap C$ | $3$ | given |
| $(A\cap B)\setminus C$ | $8 - 3 = 5$ | remove the triple |
| $(A\cap C)\setminus B$ | $6 - 3 = 3$ | remove the triple |
| $(B\cap C)\setminus A$ | $5 - 3 = 2$ | remove the triple |
| $A$ only | $20 - 5 - 3 - 3 = 9$ | subtract the three parts inside $A$ |
| $B$ only | $17 - 5 - 2 - 3 = 7$ | subtract the three parts inside $B$ |
| $C$ only | $13 - 3 - 2 - 3 = 5$ | subtract the three parts inside $C$ |

Their sum is $9+7+5+5+3+2+3 = 34$. ✓

*Check.* $\lvert A\rvert = 9+5+3+3 = 20$, $\lvert B\rvert = 5+7+2+3 = 17$, $\lvert C\rvert = 3+2+5+3 = 13$. ✓

**4.** *Universe: $[100]$; bad sets: multiples of $3$ and multiples of $5$.*

Multiples of $3$: $\lfloor 100/3\rfloor = 33$. Multiples of $5$: $\lfloor 100/5\rfloor = 20$. Multiples of both, that is of $\operatorname{lcm}(3,5) = 15$: $\lfloor 100/15\rfloor = 6$. Hence

$$\lvert A_3 \cup A_5\rvert = 33 + 20 - 6 = 47 .$$

Divisible by neither: $100 - 47 = 53$.

*Check.* The multiples of $15$ are $15,30,45,60,75,90$ — six of them, consistent. ✓

**5.** *Universe: $[500]$; bad sets: multiples of $4$ and of $6$.*

$$\left\lfloor\frac{500}{4}\right\rfloor = 125, \qquad \left\lfloor\frac{500}{6}\right\rfloor = 83, \qquad \left\lfloor\frac{500}{12}\right\rfloor = 41,$$

so the count is $125 + 83 - 41 = 167$.

The correction must count integers divisible by both $4$ and $6$, which are exactly the multiples of $\operatorname{lcm}(4,6) = 12$. It is *not* $\lfloor 500/24\rfloor$: $24$ is the product, and multiples of $12$ such as $12$ and $36$ are divisible by both $4$ and $6$ without being divisible by $24$. The expression $\lfloor500/4\rfloor\lfloor500/6\rfloor/500$ has no meaning as a count of a set — an intersection is not estimated by dividing a product of counts by the size of the universe. (Numerically it gives $125\cdot 83/500 = 20.75$, which is not even an integer; the correct count is $41$.)

*Check.* Using $500 = 41\cdot12 + 8$: each full block of $12$ contains the multiples $4,6,8,12$ of $4$ or $6$ — four of them. So the count is $41\cdot 4 + (\text{multiples of } 4 \text{ or } 6 \text{ in } 493,\dots,500) = 164 + 3 = 167$, the last three being $496$, $498$, $500$. ✓

**6.** *Universe: the $9000$ four-digit integers. Bad property: the digit $7$ appears.*

Count the complement. The first digit has $8$ choices ($1,\dots,9$ except $7$), and each of the remaining three digits has $9$ choices ($0,\dots,9$ except $7$). So the four-digit numbers with no $7$ are

$$8\cdot 9^3 = 8\cdot 729 = 5832,$$

and the answer is $9000 - 5832 = 3168$.

*Check.* The same computation for two-digit numbers: $90 - 8\cdot 9 = 90 - 72 = 18$ numbers contain a $7$ (namely $17,27,\dots,97$ — nine with units digit $7$ — plus $70,\dots,79$ — ten — minus the double count $77$: $9+10-1 = 18$). ✓ The inclusion–exclusion check confirms the method.

**7.** *Universe: $S_4$. Bad properties: $\sigma(i) = i$.*

From $D_n = n!\sum_{k=0}^n(-1)^k/k!$ with $n = 4$:

$$D_4 = 24\left(1 - 1 + \frac12 - \frac16 + \frac{1}{24}\right) = 24 - 24 + 12 - 4 + 1 = 9 .$$

Equivalently by the sieve: $S_0 = 24$, $S_1 = 4\cdot 6 = 24$, $S_2 = 6\cdot 2 = 12$, $S_3 = 4\cdot 1 = 4$, $S_4 = 1$, and $24-24+12-4+1 = 9$.

The nine derangements, in one-line notation:

$$2143,\quad 2341,\quad 2413,\quad 3142,\quad 3412,\quad 3421,\quad 4123,\quad 4312,\quad 4321 .$$

*Check.* Each has no entry equal to its position: $2143$ is $(2,1,4,3)$ and indeed no coordinate equals its index. ✓ There are nine, matching the formula.

**8.** *Universe: $S_6$, $S_7$. Recurrence $D_n = nD_{n-1}+(-1)^n$.*

$$D_5 = 5D_4 + (-1)^5 = 5\cdot 9 - 1 = 44, \qquad D_6 = 6D_5 + (-1)^6 = 6\cdot 44 + 1 = 265,$$
$$D_7 = 7D_6 + (-1)^7 = 7\cdot 265 - 1 = 1854 .$$

*Check.* Directly from the closed formula, $D_6 = 720\left(1-1+\frac12-\frac16+\frac1{24}-\frac1{120}+\frac1{720}\right) = 720 - 720 + 360 - 120 + 30 - 6 + 1 = 265$. ✓ And $D_6/6! = 265/720 = 0.36805\ldots$, close to $1/e = 0.367879\ldots$ and slightly above it, as expected since the last term has sign $+$. ✓

**9.** *Universe: all $3^6$ functions; bad sets: functions missing a given value.*

$$\operatorname{Surj}(6,3) = 3^6 - \binom31 2^6 + \binom32 1^6 - \binom33 0^6 = 729 - 192 + 3 - 0 = 540 .$$

Via Stirling numbers: $3!\,S(6,3) = 6\cdot 90 = 540$. ✓

*Check.* On the smaller case $m = 4$, $n = 3$: $81 - 48 + 3 = 36 = 6\cdot 6 = 3!\,S(4,3)$. ✓

**10.** *Totient, two ways.*

(a) $84 = 2^2\cdot3\cdot7$, so the distinct primes are $2,3,7$:

$$\varphi(84) = 84\left(1-\frac12\right)\left(1-\frac13\right)\left(1-\frac17\right) = 84\cdot\frac12\cdot\frac23\cdot\frac67 = 84\cdot\frac{2}{7} = 24 .$$

Direct count by inclusion–exclusion over $2,3,7$: the multiples up to $84$ number $42$, $28$, $12$; the pairwise intersections $14$, $6$, $4$; and the triple intersection $2$. Hence the union has $42+28+12-14-6-4+2 = 60$ elements, and $\varphi(84) = 84 - 60 = 24$. ✓

(b) $720 = 2^4\cdot3^2\cdot5$, so the distinct primes are $2,3,5$:

$$\varphi(720) = 720\left(1-\frac12\right)\left(1-\frac13\right)\left(1-\frac15\right) = 720\cdot\frac12\cdot\frac23\cdot\frac45 = 720\cdot\frac{4}{15} = 192 .$$

Direct count: $360 + 240 + 144 - 120 - 72 - 48 + 24 = 528$ integers up to $720$ are divisible by $2$, $3$ or $5$, so $\varphi(720) = 720 - 528 = 192$. ✓

**11.** *Universe: $[1000]$; bad sets: multiples of $2$, $3$, $7$.*

$$\begin{aligned}
N_0 &= 1000 - (500+333+142) + (166+71+47) - 23\\
&= 1000 - 975 + 284 - 23 = 286 .
\end{aligned}$$

Here $\lfloor1000/2\rfloor = 500$, $\lfloor1000/3\rfloor = 333$, $\lfloor1000/7\rfloor = 142$; the pairwise terms use $\operatorname{lcm}(2,3) = 6$, $\operatorname{lcm}(2,7) = 14$ and $\operatorname{lcm}(3,7) = 21$; the triple term uses $42$.

*Period check.* $1000 = 23\cdot42 + 34$. Each block of $42$ consecutive integers contains $\varphi(42) = 12$ integers coprime to $42$, giving $23\cdot12 = 276$; among $1,\dots,34$ the coprime ones are $1,5,11,13,17,19,23,25,29,31$ — ten of them. Total $276 + 10 = 286$. ✓

**12.** *Three events, three corrections.*

$$\Pr(A\cup B\cup C) = 0.5+0.4+0.3 - (0.2+0.15+0.1) + 0.05 = 1.2 - 0.45 + 0.05 = 0.8 .$$

None occurs with probability $1 - 0.8 = 0.2$.

*Check.* All probabilities lie in $[0,1]$ and the pairwise probabilities are each at most the corresponding single ones ($0.2 \le 0.4$, $0.15 \le 0.3$, $0.1 \le 0.3$), so the data are consistent. ✓

## Intermediate

**13.** *$D_8$ two ways.*

From the closed formula,

$$D_8 = 40\,320\left(1 - 1 + \frac12 - \frac16 + \frac1{24} - \frac1{120} + \frac1{720} - \frac1{5040} + \frac1{40\,320}\right).$$

Multiplying out: $40\,320 - 40\,320 + 20\,160 - 6720 + 1680 - 336 + 56 - 8 + 1 = 14\,833$.

From the recurrence: $D_8 = 8D_7 + 1 = 8\cdot 1854 + 1 = 14\,833$. ✓

*Check.* $D_8/8! = 14\,833/40\,320 = 0.367882\ldots$, within $10^{-4}$ of $1/e = 0.367879\ldots$, and slightly above it because the last retained term is positive. ✓

**14.** *Exactly two fixed points among permutations of $[6]$.*

Choose the two fixed points in $\binom62 = 15$ ways; the remaining four elements must form a derangement, in $D_4 = 9$ ways. So the count is $15\cdot 9 = 135$, and the probability is

$$\frac{135}{720} = \frac{3}{16} = 0.1875 .$$

*Check by exhaustion.* Summing $\binom6k D_{6-k}$ over $k$ must give $720$:

$$265 + 6\cdot44 + 15\cdot9 + 20\cdot2 + 15\cdot1 + 6\cdot0 + 1\cdot1 = 265+264+135+40+15+0+1 = 720 . ✓$$

The individual terms are also the numbers of permutations with $0,1,2,3,4,5,6$ fixed points.

**15.** *Universe: $[10\,000]$; bad sets: multiples of $6$, $10$, $15$.*

Sizes: $\lfloor10000/6\rfloor = 1666$, $\lfloor10000/10\rfloor = 1000$, $\lfloor10000/15\rfloor = 666$.

Pairwise intersections use least common multiples: $\operatorname{lcm}(6,10) = 30$, $\operatorname{lcm}(6,15) = 30$, $\operatorname{lcm}(10,15) = 30$, each giving $\lfloor10000/30\rfloor = 333$. The triple intersection uses $\operatorname{lcm}(6,10,15) = 30$, again $333$. Hence

$$\lvert A\cup B\cup C\rvert = 1666+1000+666 - 999 + 333 = 2666,$$

and the number divisible by none is $10\,000 - 2666 = 7334$.

*Check.* Divisibility by each of $6,10,15$ depends only on the residue modulo $30$. In one period $1,\dots,30$ the multiples are $6,10,12,15,18,20,24,30$ — eight numbers — so $22$ of every $30$ are divisible by none. Since $10\,000 = 333\cdot30 + 10$ and the residues $1,\dots,10$ contribute the eight integers $1,2,3,4,5,7,8,9$, the total is $333\cdot22 + 8 = 7326+8 = 7334$. ✓

**16.** *Exactly $m$, for $m = 1,2,3$, in a survey.*

The elementary symmetric sums are $S_1 = 60+50+40 = 150$, $S_2 = 30+25+20 = 75$, $S_3 = 10$.

$$N_1 = S_1 - 2S_2 + 3S_3 = 150 - 150 + 30 = 30,$$
$$N_2 = S_2 - 3S_3 = 75 - 30 = 45, \qquad N_3 = S_3 = 10 .$$

The union has $150 - 75 + 10 = 85$ people, so $100 - 85 = 15$ read none.

*Check by regions.* The given data determine every Venn region: the exactly-two regions are $30-10 = 20$ (in $A\cap B$ only), $25-10 = 15$ ($B\cap C$ only) and $20-10 = 10$ ($A\cap C$ only); then $\lvert A\rvert = 60$ forces $x_A = 60 - 20 - 10 - 10 = 20$ for $A$ only, $\lvert B\rvert = 50$ forces $x_B = 50 - 20 - 15 - 10 = 5$, and $\lvert C\rvert = 40$ forces $x_C = 40 - 10 - 15 - 10 = 5$. Hence exactly one is $20+5+5 = 30$, exactly two is $20+15+10 = 45$, exactly three is $10$, and none is $100 - (30+45+10) = 15$. ✓ All numbers are non-negative, so the survey data are consistent.

**17.** *Surjections from a $6$-set onto a $4$-set.*

$$\operatorname{Surj}(6,4) = 4^6 - \binom41 3^6 + \binom42 2^6 - \binom43 1^6 + 0 = 4096 - 2916 + 384 - 4 = 1560 .$$

Hence $S(6,4) = 1560/4! = 1560/24 = 65$.

*Check.* The Stirling recurrence $S(6,4) = 4S(5,4) + S(5,3) = 4\cdot10 + 25 = 65$. ✓

**18.** *Three couples in a row, no spouses adjacent.*

The formula announced in the problem is $\sum_{k=0}^{n}(-1)^k\binom{n}{k}2^k(2n-k)!$: the $k$-th term accounts for $k$ chosen couples being treated as blocks, each block having $2$ internal orders, and the blocks then arranged with the remaining individuals.

For $n = 3$:

$$6! - \binom31 2\cdot 5! + \binom32 2^2\cdot 4! - \binom33 2^3 \cdot 3! = 720 - 720 + 288 - 48 = 240 .$$

For $n = 2$, by hand: six arrangements of $A,a,B,b$ in a row with $A$ not next to $a$ and $B$ not next to $b$. Total $24$. Those with $A,a$ adjacent: treat as a block, $2$ internal orders and $3! = 6$ orders of the block with $B,b$: $12$. Same for $B,b$: $12$. Those with both couples adjacent: two blocks, $2\cdot2\cdot2! = 8$. Hence $24 - 12 - 12 + 8 = 8$. The formula gives $24 - 2\cdot2\cdot6 + 4\cdot2 = 24-24+8 = 8$. ✓

*Check.* At $n=1$ the formula gives $2 - 2\cdot1 = 0$, correct: a single couple in a row of two always sits together. ✓

**19.** *Rook polynomial for four people and four tasks.*

The forbidden board has the $2\times2$ block in rows $\{1,2\}$ and columns $\{1,2\}$, together with the single cell $(3,3)$. The block lies in rows and columns disjoint from row $3$ and column $3$, so the rook polynomials multiply:

$$R_B(x) = (1 + 4x + 2x^2)(1 + x) = 1 + 5x + 6x^2 + 2x^3 .$$

By the rook theorem,

$$N_0 = 4! - 5\cdot3! + 6\cdot2! - 2\cdot1! = 24 - 30 + 12 - 2 = 4 .$$

*Check by listing.* Person $1$ and person $2$ must take tasks $3$ and $4$ in some order; person $3$ must then take task $1$ or $2$, and person $4$ takes the remaining one. The four legal assignments $(\sigma(1),\sigma(2),\sigma(3),\sigma(4))$ are

$$(3,4,1,2),\quad (3,4,2,1),\quad (4,3,1,2),\quad (4,3,2,1). ✓$$

**20.** *$\varphi(1001)$.*

Since $1001 = 7\cdot11\cdot13$ is squarefree,

$$\varphi(1001) = 1001\left(1-\frac17\right)\left(1-\frac1{11}\right)\left(1-\frac1{13}\right) = 1001\cdot\frac{6}{7}\cdot\frac{10}{11}\cdot\frac{12}{13} = \frac{1001\cdot720}{1001} = 720 .$$

The simplification is structural: for squarefree $n = p_1p_2\cdots p_r$,

$$\varphi(n) = n\prod\left(1-\frac1{p_i}\right) = \prod p_i\prod\frac{p_i-1}{p_i} = \prod_{i=1}^{r}(p_i-1),$$

so $\varphi(1001) = 6\cdot10\cdot12 = 720$. The exponents of a non-squarefree $n$ would break this telescoping.

*Check.* $720 = 1001 - 281$; the number of integers in $[1001]$ divisible by $7$, $11$ or $13$ is $143 + 91 + 77 - 13 - 11 - 7 + 1 = 281$, and $1001 - 281 = 720$. ✓

**21.** *Coupon collector with ten rolls.*

By the sieve applied to the six events "face $j$ never appears",

$$\Pr = \sum_{k=0}^{6}(-1)^k\binom6k\left(\frac{6-k}{6}\right)^{10} = \frac{16\,435\,440}{6^{10}},$$

since $6^{10} = 60\,466\,176$ and the six terms are

$$60\,466\,176 - 6\cdot9\,765\,625 + 15\cdot1\,048\,576 - 20\cdot59\,049 + 15\cdot1024 - 6 = 16\,435\,440 .$$

Reducing, $\frac{16\,435\,440}{60\,466\,176} = \frac{38\,045}{139\,968}$, and numerically

$$\frac{38\,045}{139\,968} = 0.2718121\ldots \approx 0.2718 .$$

*Check.* The value must lie between $\Pr(\text{all six appear in } 6 \text{ rolls}) = 5/324 = 0.01543$ and $1$, and must increase with $n$; it does. ✓

**22.** *At least one letter in its own envelope.*

$$\Pr(\text{at least one}) = 1 - \frac{D_{10}}{10!} = 1 - \frac{1\,334\,961}{3\,628\,800} = \frac{28\,319}{44\,800} \approx 0.632121 .$$

*Check.* The complementary probability $16\,481/44\,800 = 0.36787946\ldots$ is within $3\times10^{-8}$ of $1/e$, as Theorem 7.5 and the bound of Section 7.8 predict. ✓

**23.** *Bonferroni for five events of probability $0.9$.*

Apply the probability form of the even-case Bonferroni inequality to the complements $B_i^{\complement}$, or directly: by inclusion–exclusion,

$$\Pr\left(\bigcup_i B_i^{\complement}\right) \le \sum_i \Pr(B_i^{\complement}) = 5\cdot 0.1 = 0.5,$$

so $\Pr(\bigcap_i B_i) \ge 0.5$.

Equivalently, using the standard form $\Pr(\bigcap B_i) \ge \sum\Pr(B_i) - (n-1) = 4.5 - 4 = 0.5$.

*Sharpness.* Let $\Omega = \{1,\dots,10\}$ with equal probabilities and $B_i = \Omega\setminus\{i\}$ for $i = 1,\dots,5$. Then $\Pr(B_i) = 9/10$ and $\bigcap_{i=1}^5 B_i = \{6,7,8,9,10\}$ has probability $0.5$. ✓

**24.** *Divisible by $6$ or $10$ but not $15$.*

First, $\lvert A\cup B\rvert$ for $A$ = multiples of $6$ and $B$ = multiples of $10$ in $[1000]$:

$$166 + 100 - 33 = 233,$$

since $A\cap B$ is the multiples of $30$.

Now subtract the multiples of $15$ inside $A\cup B$:

$$\lvert(A\cup B)\cap C\rvert = \lvert(A\cap C)\cup(B\cap C)\rvert = 33 + 33 - 33 = 33,$$

because $A\cap C$ is the multiples of $\operatorname{lcm}(6,15) = 30$, $B\cap C$ is the multiples of $\operatorname{lcm}(10,15) = 30$, and their intersection is again the multiples of $30$.

Hence the answer is $233 - 33 = 200$.

*Check.* A multiple of $15$ in $A\cup B$ must be divisible by $6$ or by $10$; since $15$ is coprime to both $6/3$ and $10/5$, this forces divisibility by $30$ in either case. So exactly the $33$ multiples of $30$ are removed, and $233 - 33 = 200$. ✓

## Advanced

**25.** *The "exactly $m$" formula.*

**Claim.** $N_m = \sum_{k=m}^{n}(-1)^{k-m}\binom{k}{m}S_k$, where $N_m$ is the number of elements belonging to exactly $m$ of the sets.

*Proof.* Count contributions element by element. An element $x$ with $m(x) = j$ contributes $\binom{j}{k}$ to $S_k$, because $x$ lies in $\bigcap_{i\in I}A_i$ exactly for the $\binom{j}{k}$ index sets $I$ of size $k$ that are contained in the $j$ sets containing $x$. Hence its total contribution to the right-hand side is

$$T(j) := \sum_{k=m}^{n}(-1)^{k-m}\binom{k}{m}\binom{j}{k} = \binom{j}{m}\sum_{k=m}^{n}(-1)^{k-m}\binom{j-m}{k-m} = \binom{j}{m}\sum_{r=0}^{j-m}(-1)^r\binom{j-m}{r},$$

where the identity $\binom{k}{m}\binom{j}{k} = \binom{j}{m}\binom{j-m}{k-m}$ was used, and terms with $k > j$ vanish.

* If $j = m$, the inner sum is $\binom00 = 1$, so $T(m) = \binom mm\cdot 1 = 1$.
* If $j > m$, the inner sum is $(1-1)^{j-m} = 0$, so $T(j) = 0$.
* If $j < m$, every term has $k \ge m > j$ and vanishes, so $T(j) = 0$.

Therefore the right-hand side counts exactly the elements with $j = m$, once each. $\blacksquare$

*Check.* For $m = 0$ the formula gives $N_0 = \sum_k(-1)^kS_k$, the sieve. For $m = n$ it gives $N_n = S_n$. For the three sets of Example 7.10's style, i.e. $A = [10]$, $B = \{3,4,5,6,11,12\}$, $C = \{5,6,7,13\}$ with $S_1 = 20$, $S_2 = 9$, $S_3 = 2$: $N_1 = 20-18+6 = 8$, $N_2 = 9-6 = 3$, $N_3 = 2$, and direct inspection gives $8, 3, 2$. ✓

**26.** *Bonferroni inequalities.*

**Claim.** For $1 \le t \le n$, with $P_t := S_1 - S_2 + \cdots + (-1)^{t+1}S_t$: if $t$ is odd then $\lvert\bigcup_i A_i\rvert \le P_t$; if $t$ is even then $\lvert\bigcup_i A_i\rvert \ge P_t$.

*Proof.* Let $x$ have membership count $m = m(x)$. Its contribution to $P_t$ is

$$Q_t(m) := \sum_{k=1}^{t}(-1)^{k+1}\binom{m}{k} = 1 - \sum_{k=0}^{t}(-1)^k\binom{m}{k} = 1 - (-1)^t\binom{m-1}{t},$$

where Proposition 8.2 was used, with the convention $\binom{m-1}{t} = 0$ for $t > m-1$. Note that $Q_t(0) = 0$ for every $t \ge 1$, since $\binom{0}{k} = 0$ for $k \ge 1$: an element outside the union contributes nothing to any partial sum.

* If $m \ge 1$ and $t$ is odd, $Q_t(m) = 1 + \binom{m-1}{t} \ge 1$.
* If $m \ge 1$ and $t$ is even, $Q_t(m) = 1 - \binom{m-1}{t} \le 1$.

Summing over $x$, and noting that only elements of the union contribute,

$$P_t = \sum_{x\,:\,m(x)\ge1}Q_t\big(m(x)\big) \;\begin{cases}\ge \sum_{m(x)\ge1}1 = \lvert\bigcup_i A_i\rvert, & t \text{ odd},\\[2pt] \le \sum_{m(x)\ge1}1 = \lvert\bigcup_i A_i\rvert, & t \text{ even}.\end{cases}$$

Equivalently, the difference $P_t - \lvert\bigcup_iA_i\rvert = \sum_{m(x)\ge1}\big(Q_t(m(x))-1\big)$ equals $\sum_{m(x)\ge1}(-1)^{t+1}\binom{m(x)-1}{t}$, which is a sum of non-negative terms for odd $t$ and of non-positive terms for even $t$. $\blacksquare$

*Check at $t = n$.* Then $\binom{m-1}{n} = 0$ for every $m \le n$, so $Q_n(m) = 1$ for $m \ge 1$ and $Q_n(0) = 0$; both bounds are equalities, as they must be, because $P_n$ is the full alternating sum. ✓

**27.** *Two derangement recurrences.*

(a) *From the closed form.* Start from $D_n = n!\sum_{k=0}^{n}(-1)^k/k!$ and note

$$nD_{n-1} = n\,(n-1)!\sum_{k=0}^{n-1}\frac{(-1)^k}{k!} = n!\sum_{k=0}^{n-1}\frac{(-1)^k}{k!} = D_n - n!\cdot\frac{(-1)^n}{n!} = D_n - (-1)^n,$$

hence $D_n = nD_{n-1} + (-1)^n$. (For $n \ge 1$; at $n = 1$ this reads $D_1 = 1\cdot D_0 - 1 = 0$.) ✓

(b) *Combinatorially.* Let $\sigma$ be a derangement of $[n]$ and put $j = \sigma(n)$, so $j \ne n$ and there are $n-1$ choices of $j$. Fix $j$.

*Case 1: $\sigma(j) = n$.* Then $\sigma$ transposes $n$ and $j$. The restriction of $\sigma$ to the remaining $n-2$ elements is a permutation of them with no fixed point: $D_{n-2}$ possibilities.

*Case 2: $\sigma(j) \ne n$.* Let $i = \sigma^{-1}(n)$; then $i \notin\{j,n\}$. Define $\tau : [n-1]\to[n-1]$ by $\tau(i) = j$ and $\tau(x) = \sigma(x)$ for $x \ne i$. This is well defined: for $x \ne i$, $\sigma(x) \ne n$ (as $i$ is the unique preimage of $n$), so $\tau(x) \in [n-1]$; and $\sigma(x) \ne j$ for $x \in [n-1]$ (as $j = \sigma(n)$ is already a value), so $\tau$ is injective on $[n-1]\setminus\{i\}$ with image $[n-1]\setminus\{j\}$, and $\tau(i) = j$ makes it a bijection. It is a derangement: $\tau(i) = j \ne i$, and $\tau(x) = \sigma(x)\ne x$ for $x \ne i$. The map $\sigma \mapsto \tau$ is a bijection onto the derangements of $[n-1]$, with inverse: given a derangement $\tau$, take $i = \tau^{-1}(j)$, set $\sigma(n) = j$, $\sigma(i) = n$ and $\sigma = \tau$ elsewhere. So Case 2 has $D_{n-1}$ possibilities.

Summing over the $n-1$ choices of $j$: $D_n = (n-1)(D_{n-1}+D_{n-2})$. $\blacksquare$

*Check.* $n = 4$: $3(2+1) = 9 = D_4$. ✓ $n = 5$: $4(9+2) = 44 = D_5$. ✓

**28.** *The rook theorem.*

**Claim.** If $B\subseteq[n]\times[n]$ and $r_k$ is the number of $k$-element subsets of $B$ with all rows and columns distinct, then the number of permutations avoiding $B$ is $\sum_k(-1)^kr_k(n-k)!$.

*Proof.* Let $U = S_n$, so $\lvert U\rvert = n!$. For $b = (i,j)\in B$ let $A_b = \{\sigma : \sigma(i) = j\}$, the permutations that use $b$. A permutation avoids $B$ exactly when it lies in no $A_b$, so the sieve gives

$$N_0 = \sum_{S\subseteq B}(-1)^{\lvert S\rvert}\left\lvert\bigcap_{b\in S}A_b\right\rvert .$$

For a subset $S$: if two cells of $S$ lie in the same row, say $(i,j)$ and $(i,j')$ with $j\ne j'$, then a permutation in the intersection would need $\sigma(i) = j$ and $\sigma(i) = j'$, impossible, so the intersection is empty; similarly if two cells share a column. If $S$ is non-attacking, then the constraints $\sigma(i)=j$ for $(i,j)\in S$ specify $\lvert S\rvert$ distinct values at $\lvert S\rvert$ distinct points, and the remaining $n - \lvert S\rvert$ values can be assigned arbitrarily: $(n-\lvert S\rvert)!$ permutations.

Grouping the subsets by size, the number of non-attacking subsets of size $k$ is $r_k$, so the coefficient of $(-1)^k$ is $r_k(n-k)!$, which proves the claim. $\blacksquare$

*Check.* The diagonal board has $r_k = \binom nk$, giving $D_n$; and the empty board has $r_0 = 1$ and $r_k = 0$ for $k\ge1$, giving $n!$. Both are correct. ✓

**29.** *Euler's totient.*

(a) *Product formula.* Let $p_1,\dots,p_r$ be the distinct primes dividing $n$. Take $U = [n]$ and $A_i$ = multiples of $p_i$ in $[n]$. For $I\subseteq[r]$, the intersection $\bigcap_{i\in I}A_i$ consists of the multiples of $\prod_{i\in I}p_i$ (distinct primes, so this product is the least common multiple), hence has $n/\prod_{i\in I}p_i$ elements. The sieve gives

$$\varphi(n) = \sum_{I\subseteq[r]}(-1)^{\lvert I\rvert}\frac{n}{\prod_{i\in I}p_i} = n\prod_{i=1}^{r}\left(1-\frac1{p_i}\right),$$

since expanding the product generates exactly one term per subset $I$. $\blacksquare$

(b) *Divisor sum.* Consider the $n$ fractions $k/n$ for $k = 1,\dots,n$, and reduce each to lowest terms. If $\gcd(k,n) = g$ and $d = n/g$, then

$$\frac{k}{n} = \frac{k/g}{d}, \qquad \gcd(k/g,\,d) = 1, \qquad 1 \le k/g \le d .$$

Conversely, every reduced fraction $a/d$ with $d \mid n$ and $1\le a\le d$, $\gcd(a,d)=1$, arises from exactly one $k$, namely $k = a\,(n/d)$. So the fractions with denominator exactly $d$ number $\varphi(d)$, and summing over the divisors of $n$ counts all $n$ fractions:

$$\sum_{d\mid n}\varphi(d) = n . \qquad \blacksquare$$

*Check.* $n = 6$: $1/6, 5/6$ (denominator $6$, $\varphi(6) = 2$), $1/3, 2/3$ ($d=3$, $\varphi(3)=2$), $1/2$ ($d=2$, $\varphi(2)=1$), $1/1$ ($d=1$, $\varphi(1)=1$); total $2+2+1+1 = 6 = \sum_{d\mid6}\varphi(d)$. ✓

**30.** *Fixed points are asymptotically Poisson with parameter $1$.*

*Step 1: $F(n,k) = \binom nk D_{n-k}$.* A permutation with exactly $k$ fixed points is determined by choosing the fixed set $T$ ($\binom nk$ choices) and a derangement of $[n]\setminus T$ ($D_{n-k}$ choices), and these choices are independent. ✓

*Step 2: the limit.* Therefore

$$\frac{F(n,k)}{n!} = \frac{\binom nk D_{n-k}}{n!} = \frac{1}{k!}\cdot\frac{D_{n-k}}{(n-k)!} \longrightarrow \frac{1}{k!}\cdot\frac1e \qquad (n\to\infty),$$

because $D_m/m! \to 1/e$ as $m \to \infty$ (Section 7.8) and $n-k\to\infty$. $\blacksquare$

*Check.* $k = 2$, $n = 10$: $F(10,2)/10! = \binom{10}2D_8/10! = 667\,485/3\,628\,800 = 0.1839410\ldots$, against $e^{-1}/2 = 0.1839397\ldots$. ✓

**31.** *Legendre's formula.*

*Claim.* With $a = \pi(\sqrt x)$ and $\Phi(x,a)$ counting the integers in $[x]$ divisible by none of $p_1,\dots,p_a$, we have $\pi(x) = \Phi(x,a) + a - 1$.

*Proof.* By inclusion–exclusion,

$$\Phi(x,a) = \sum_{I\subseteq[a]}(-1)^{\lvert I\rvert}\left\lfloor\frac{x}{\prod_{i\in I}p_i}\right\rfloor .$$

Every composite $m \le x$ has a prime divisor $\le\sqrt m\le\sqrt x$, so it is divisible by one of $p_1,\dots,p_a$ and is therefore *not* counted by $\Phi$. The integers not counted out are $1$ and the primes $> \sqrt x$; the primes $\le\sqrt x$ are exactly $p_1,\dots,p_a$, so the count is

$$\Phi(x,a) = 1 + (\pi(x) - a) \quad\Longrightarrow\quad \pi(x) = \Phi(x,a) + a - 1 . \qquad \blacksquare$$

For $x = 1000$: $\sqrt{1000}\approx31.6$, so $a = \pi(31) = 11$ (primes $2,3,5,7,11,13,17,19,23,29,31$). Given $\Phi(1000,11) = 158$,

$$\pi(1000) = 158 + 11 - 1 = 168 .$$

*Check.* The known value is $\pi(1000) = 168$, and $\pi(100) = 22+4-1 = 25$ from the computation in Section 7.11. ✓

**32.** *Binomial inversion, and the "exactly $m$" formula.*

*Inversion.* Suppose $a_n = \sum_{k\le n}\binom nk b_k$ for all $n$. Then

$$\begin{aligned}
\sum_{k=0}^{n}(-1)^{n-k}\binom nk a_k
&= \sum_{k=0}^{n}(-1)^{n-k}\binom nk\sum_{j=0}^{k}\binom kj b_j
= \sum_{j=0}^{n}b_j\sum_{k=j}^{n}(-1)^{n-k}\binom nk\binom kj\\
&= \sum_{j=0}^{n}b_j\binom nj\sum_{k=j}^{n}(-1)^{n-k}\binom{n-j}{k-j}
= \sum_{j=0}^{n}b_j\binom nj(1-1)^{n-j} = b_n,
\end{aligned}$$

because $\binom nk\binom kj = \binom nj\binom{n-j}{k-j}$ and $(1-1)^{n-j}$ is $1$ only when $j = n$. $\blacksquare$

*Deduction of the "exactly $m$" formula.* The relation between the two sequences is

$$S_k = \sum_{m\ge k}\binom mk N_m,$$

i.e. the transpose of the inversion hypothesis (the sum runs over the *upper* index). Applying the same binomial identity in the other direction,

$$\begin{aligned}
\sum_{k\ge m}(-1)^{k-m}\binom km S_k
&= \sum_{k\ge m}(-1)^{k-m}\binom km\sum_{j\ge k}\binom jk N_j
= \sum_{j\ge m}N_j\sum_{k=m}^{j}(-1)^{k-m}\binom km\binom jk\\
&= \sum_{j\ge m}N_j\binom jm\sum_{r=0}^{j-m}(-1)^r\binom{j-m}{r} = \sum_{j\ge m}N_j\binom jm\,\delta_{jm} = N_m . \ \blacksquare
\end{aligned}$$

*Check.* With $m = 1$ and the three sets $S_1 = 20$, $S_2 = 9$, $S_3 = 2$: $N_1 = 20 - 2\cdot9 + 3\cdot2 = 8$, matching the direct count. ✓

## Challenge

**33.** *Permutations with no succession.*

A **succession** is a position $i$ with $\sigma(i+1) = \sigma(i)+1$. Consider the board

$$B = \{(i,\,i+1) : 1 \le i \le n-1\} \subseteq [n]\times[n],$$

whose cells correspond to successions: $\sigma$ has a succession at $i$ exactly when it uses the cell $(i,i+1)$.

*The rook numbers.* The $n-1$ cells of $B$ lie in the $n-1$ distinct rows $1,\dots,n-1$ and in the $n-1$ distinct columns $2,\dots,n$. Any subset of $k$ cells therefore has distinct rows and distinct columns, so every $k$-subset is non-attacking and

$$r_k = \binom{n-1}{k} \qquad (0 \le k \le n-1), \qquad r_k = 0 \text{ for } k \ge n .$$

*The count.* By the rook theorem (Exercise 28, or Theorem 7.7),

$$N_0 = \sum_{k=0}^{n-1}(-1)^k\binom{n-1}{k}(n-k)! .$$

*Values.*

| $n$ | $1$ | $2$ | $3$ | $4$ | $5$ |
|---|---|---|---|---|---|
| count | $1$ | $1$ | $3$ | $11$ | $53$ |

Computations: $n=3$ gives $6 - 2\cdot2 + 1 = 3$; $n=4$ gives $24 - 3\cdot6 + 3\cdot2 - 1 = 11$; $n=5$ gives $120 - 4\cdot24 + 6\cdot6 - 4\cdot2 + 1 = 120 - 96 + 36 - 8 + 1 = 53$.

*Verification for $n = 4$.* Listing the $11$ permutations of $1234$ with no succession:

$$1324,\ 1432,\ 2143,\ 2413,\ 2431,\ 3142,\ 3214,\ 3241,\ 4132,\ 4213,\ 4321 .$$

For example, in $\sigma = 1324$ the three possible successions would require $\sigma(2) = \sigma(1)+1 = 2$, $\sigma(3) = \sigma(2)+1 = 4$ and $\sigma(4) = \sigma(3)+1 = 3$; none of these holds, so this permutation has no succession. ✓ And $1234$ is excluded because every position is a succession.

**34.** *Jordan's formula for "at least $r$".*

**Claim.** $N_{\ge r} = \sum_{k=r}^{n}(-1)^{k-r}\binom{k-1}{r-1}S_k$.

*Proof.* Sum the "exactly $m$" formula over $m \ge r$:

$$N_{\ge r} = \sum_{m=r}^{n}N_m = \sum_{m=r}^{n}\sum_{k=m}^{n}(-1)^{k-m}\binom km S_k = \sum_{k=r}^{n}S_k\sum_{m=r}^{k}(-1)^{k-m}\binom km .$$

The inner sum is evaluated with Proposition 8.2:

$$\sum_{m=r}^{k}(-1)^{k-m}\binom km = (-1)^k\sum_{m=r}^{k}(-1)^{m}\binom km = (-1)^k\left(-\sum_{m=0}^{r-1}(-1)^m\binom km\right) = (-1)^{k+1}(-1)^{r-1}\binom{k-1}{r-1},$$

and $(-1)^{k+1+r-1} = (-1)^{k+r} = (-1)^{k-r}$ because $2r$ is even. Hence the inner sum equals $(-1)^{k-r}\binom{k-1}{r-1}$, as claimed. $\blacksquare$

*Check on $A = [10]$, $B = \{3,4,5,6,11,12\}$, $C = \{5,6,7,13\}$.* Here $S_1 = 20$, $S_2 = 9$, $S_3 = 2$.

* $r = 1$: $S_1 - S_2 + S_3 = 20 - 9 + 2 = 13$, which is $\lvert A\cup B\cup C\rvert = \lvert\{1,\dots,13\}\rvert = 13$. ✓
* $r = 2$: $S_2 - \binom11\cdot 2S_3 = 9 - 4 = 5$; directly, the elements in at least two sets are $\{3,4,7\}$ (exactly two) and $\{5,6\}$ (all three): five. ✓
* $r = 3$: $S_3 = 2$; directly $\{5,6\}$. ✓

**35.** *A recurrence for surjections.*

**Claim.** For $m,n \ge 2$, $\operatorname{Surj}(m,n) = n\,\operatorname{Surj}(m-1,n) + n\,\operatorname{Surj}(m-1,n-1)$.

*Proof.* Let $f : [m]\to[n]$ be a surjection and let $g = f|_{[m-1]}$.

*Case 1: $g$ is onto.* Then $f(m)$ is unconstrained: $n$ choices for $f(m)$ and $\operatorname{Surj}(m-1,n)$ choices for $g$, giving $n\,\operatorname{Surj}(m-1,n)$.

*Case 2: $g$ is not onto.* Since $f$ is onto and only the value $f(m)$ is missing from $g$'s image, the image of $g$ is exactly $[n]\setminus\{j\}$ for a single $j$, and necessarily $f(m) = j$. For each of the $n$ choices of $j$, the map $g$ is a surjection from $[m-1]$ onto a set of size $n-1$, of which there are $\operatorname{Surj}(m-1,n-1)$. Giving $n\,\operatorname{Surj}(m-1,n-1)$.

The two cases exhaust all surjections and are disjoint, so the claim follows. $\blacksquare$

*Check at $(m,n) = (4,3)$.* The recurrence gives $3\operatorname{Surj}(3,3) + 3\operatorname{Surj}(3,2) = 3\cdot6 + 3\cdot6 = 36$. The inclusion–exclusion formula gives $3^4 - 3\cdot2^4 + 3\cdot1^4 - 0 = 81 - 48 + 3 = 36$. ✓

**36.** *Natural density of integers avoiding a finite set of primes.*

*Claim.* For a finite set of primes $P$, the set $S$ of integers divisible by no prime of $P$ has natural density $\prod_{p\in P}(1-1/p)$.

*Proof.* For $N \ge 1$, by inclusion–exclusion applied to the sets $A_p = \{m \le N : p \mid m\}$,

$$\Phi_P(N) := \#\{m \le N : m \in S\} = \sum_{I\subseteq P}(-1)^{\lvert I\rvert}\left\lfloor\frac{N}{m_I}\right\rfloor, \qquad m_I := \prod_{p\in I}p .$$

Write $\lfloor N/m_I\rfloor = N/m_I - \varepsilon_I$ with $0 \le \varepsilon_I < 1$. Then

$$\Phi_P(N) = N\sum_{I\subseteq P}\frac{(-1)^{\lvert I\rvert}}{m_I} - \sum_{I\subseteq P}(-1)^{\lvert I\rvert}\varepsilon_I = N\prod_{p\in P}\left(1-\frac1p\right) - E(N),$$

where the expansion of the product produces exactly the sum over subsets, and

$$\lvert E(N)\rvert \le \sum_{I\subseteq P}1 = 2^{\lvert P\rvert}$$

is bounded independently of $N$. Dividing by $N$ and letting $N\to\infty$,

$$\frac{\Phi_P(N)}{N} = \prod_{p\in P}\left(1-\frac1p\right) + O\!\left(\frac{2^{\lvert P\rvert}}{N}\right) \longrightarrow \prod_{p\in P}\left(1-\frac1p\right). \qquad \blacksquare$$

*For $P = \{2,3,5,7\}$:* the density is

$$\frac12\cdot\frac23\cdot\frac45\cdot\frac67 = \frac{48}{210} = \frac{8}{35} \approx 0.2285714 .$$

Up to $1000$ the exact count is $228$ (computed in Example 9.6), while $1000\cdot\frac{8}{35} = 228.571\ldots$; the difference $0.571$ is well inside the bound $2^4 = 16$. ✓

Note that this argument also shows the count is $\frac{8}{35}N + O(1)$ with an absolute error bound, which is stronger than the density statement: the discrepancy does not grow with $N$. In particular, the count of integers up to $N$ coprime to $210$ is always within $16$ of $\frac{8}{35}N$ — a genuinely useful estimate in sieve theory.
