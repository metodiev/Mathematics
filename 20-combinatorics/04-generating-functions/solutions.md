# Generating Functions — Solutions

> [Generating Functions](README.md) · Solutions to the 36 problems in [exercises.md](exercises.md)

Each solution states the strategy, performs every algebraic step, and checks the first terms numerically. All identities are identities in $\mathbb{K}[[x]]$; no convergence is assumed.

## Beginner

**1.** *Geometric series: $\dfrac{1}{1-cx} = \sum_nc^nx^n$.*

* $[x^6]\dfrac{1}{1-2x} = 2^6 = 64$.
* $[x^5]\dfrac{1}{1+3x} = (-3)^5 = -243$, since $\frac{1}{1+3x} = \frac{1}{1-(-3)x}$.
* $[x^0]\dfrac{1}{1-5x} = (-5)^0 = 1$: the constant term of every unit is $1/1 = 1$.

*Check.* The second series begins $1 - 3x + 9x^2 - 27x^3 + 81x^4 - 243x^5$, so the coefficient of $x^5$ is $-243$. ✓

**2.** *Binomial series.*

* $[x^4](1+x)^{10} = \dbinom{10}{4} = \dfrac{10\cdot9\cdot8\cdot7}{24} = 210$.
* $[x^4]\dfrac{1}{(1-x)^3} = \dbinom{4+2}{2} = \dbinom62 = 15$, by the table entry $[x^n]\,(1-x)^{-k} = \binom{n+k-1}{k-1}$.
* $[x^2]\dfrac{1}{1+x} = (-1)^2 = 1$, since $\frac{1}{1+x} = 1 - x + x^2 - \cdots$.

*Check.* $\frac{1}{(1-x)^3} = 1 + 3x + 6x^2 + 10x^3 + 15x^4 + \cdots$, whose coefficients are $\binom{n+2}{2}$. ✓

**3.** *Shift and known series.*

$[x^3]\dfrac{1}{(1-x)^2} = 3 + 1 = 4$, since $\frac{1}{(1-x)^2} = \sum_n(n+1)x^n$.

For $n \ge 3$, $[x^n]\dfrac{x^3}{(1-x)^2} = [x^{n-3}]\dfrac{1}{(1-x)^2} = (n-3)+1 = n-2$.

*Check.* At $n=3$ the formula gives $1$, and indeed $x^3/(1-x)^2$ begins $x^3 + 2x^4 + 3x^5 + \cdots$. ✓

**4.** *The "multiples of $m$" series.* $\dfrac{1}{1-x^2} = 1 + x^2 + x^4 + \cdots$, so the coefficient of $x^m$ is $1$ when $m$ is even and $0$ when $m$ is odd. Hence $[x^5] = 0$ and $[x^6] = 1$. And $\dfrac{x}{1-x^2} = x + x^3 + x^5 + \cdots$, so $[x^7] = 1$.

*Check.* $[x^3]x/(1-x^2) = 1$ and $[x^4]x/(1-x^2) = 0$ ✓.

**5.** *Convolution.* Write $\frac{1}{(1-x)(1-2x)} = \left(\sum_kx^k\right)\left(\sum_j2^jx^j\right)$, so

$$[x^3] = \sum_{k=0}^{3}1\cdot2^{3-k} = 8 + 4 + 2 + 1 = 15 .$$

*Check by multiplication.* $(1+x+x^2+x^3)(1+2x+4x^2+8x^3)$ has $x^3$-coefficient $1\cdot8 + 1\cdot4 + 1\cdot2 + 1\cdot1 = 15$. ✓ (Terms beyond $x^3$ in either factor cannot contribute.)

**6.** *Product of a series and its alternating version.*

$$\left(\sum_nx^n\right)\left(\sum_n(-1)^nx^n\right) = \frac{1}{1-x}\cdot\frac{1}{1+x} = \frac{1}{1-x^2} = 1 + x^2 + x^4 + \cdots .$$

The coefficients of $x^0,x^1,x^2,x^3$ are $1, 0, 1, 0$.

*Check by convolution.* $[x^3] = \sum_{k=0}^{3}1\cdot(-1)^{3-k} = -1+1-1+1 = 0$ ✓. In general the coefficient is $\sum_{k=0}^{n}(-1)^{n-k}$, which is $1$ for even $n$ and $0$ for odd $n$. ✓

**7.** *Binet's formula.* With $\varphi = 1.6180339887\ldots$ and $\psi = -0.6180339887\ldots$:

$$\varphi^{10} = 122.991869\ldots,\quad \psi^{10} = 0.0081306\ldots,\quad F_{10} = \frac{122.983739\ldots}{2.2360679\ldots} = 55.000000\ldots$$

$$\varphi^{12} = 321.996894\ldots,\quad \psi^{12} = 0.0031056\ldots,\quad F_{12} = \frac{321.993789\ldots}{2.2360679\ldots} = 144.000000\ldots$$

*Check with the recurrence.* $0,1,1,2,3,5,8,13,21,34,55,89,144$: the tenth term (counting from $F_0$) is $55$ and the twelfth is $144$. ✓

Note how small $\lvert\psi\rvert^{12} = 0.0031\ldots$ is: for $n \ge 4$ the nearest integer to $\varphi^n/\sqrt5$ is $F_n$, which is Corollary 7.8 of the tutorial.

**8.** *Catalan numbers.* From the recurrence: $C_0 = 1$, $C_1 = 1$, $C_2 = 2$, $C_3 = 5$, $C_4 = 14$, $C_5 = 42$, $C_6 = 132$.

Verify $C_5$ from the recurrence:

$$C_5 = \sum_{k=0}^{4}C_kC_{4-k} = C_0C_4 + C_1C_3 + C_2C_2 + C_3C_1 + C_4C_0 = 14 + 5 + 4 + 5 + 14 = 42 .$$

From the closed form: $C_5 = \frac16\dbinom{10}{5} = \frac{252}{6} = 42$ ✓, and $C_6 = \frac17\dbinom{12}{6} = \frac{924}{7} = 132$ ✓.

**9.** *Bell numbers.* $B_n = \sum_kS(n,k)$, with rows $S(0,\cdot) = (1)$, $S(4,\cdot) = (1,7,6,1)$ and $S(5,\cdot) = (1,15,25,10,1)$:

$$B_0 = 1,\ B_1 = 1,\ B_2 = 2,\ B_3 = 5,\ B_4 = 1+7+6+1 = 15,\ B_5 = 1+15+25+10+1 = 52 .$$

From the EGF: $\exp(e^x-1) = 1 + x + x^2 + \frac56x^3 + \frac58x^4 + \frac{13}{30}x^5+\cdots$ (computed by the recursion $p_{n+1} = \frac{1}{n+1}\sum_kp_{n-k}/k!$ of Example 9.6). Then $B_4 = 24\cdot\frac58 = 15$ ✓ and $B_5 = 120\cdot\frac{13}{30} = 52$ ✓.

**10.** *Partitions.* $p(0),\dots,p(8) = 1,1,2,3,5,7,11,15,22$.

Pentagonal recurrence, with pentagonal numbers $1,2,5,7$ and signs $+,+,-,-$:

$$p(9) = p(8)+p(7)-p(4)-p(2) = 22+15-5-2 = 30,$$
$$p(10) = p(9)+p(8)-p(5)-p(3)+p(0)\cdot 0 = 30+22-7-3 = 42 .$$

(The term $p(10-12) = p(-2) = 0$ is omitted.) Both values agree with the table of Section 7.9. ✓

**11.** *EGF of $n^2$.* Split $n^2 = n(n-1) + n$:

$$\sum_{n\ge0}n^2\frac{x^n}{n!} = \sum_{n\ge0}n(n-1)\frac{x^n}{n!} + \sum_{n\ge0}n\frac{x^n}{n!} = x^2\sum_{n\ge2}\frac{x^{n-2}}{(n-2)!} + x\sum_{n\ge1}\frac{x^{n-1}}{(n-1)!} = x^2e^x + xe^x .$$

*Check.* Expand $e^x(x+x^2) = (1+x+\frac{x^2}{2}+\frac{x^3}{6}+\cdots)(x+x^2)$; the coefficient of $x^3$ is $\frac12 + 1 = \frac32$. Multiply by $3! = 6$: $9 = 3^2$ ✓. The coefficient of $x^4$ is $\frac16 + \frac12 = \frac23$; times $24$ gives $16 = 4^2$ ✓.

**12.** *First-order recurrence.* $A(x) = \sum a_nx^n$, and summing $a_n = 3a_{n-1}$ times $x^n$ over $n \ge 1$ gives $A - a_0 = 3xA$, so $A(1-3x) = 2$ and

$$A(x) = \frac{2}{1-3x} = \sum_{n\ge0}2\cdot3^nx^n, \qquad a_n = 2\cdot3^n .$$

*Check.* $a_0 = 2$, $a_1 = 6$, $a_2 = 18$: each is three times the previous ✓.

## Intermediate

**13.** *Second-order recurrence with a cancelling root.* Sum $a_n = 5a_{n-1}-6a_{n-2}$ times $x^n$ over $n \ge 2$: the left side is $A - 1 - 3x$, the right side is $5x(A-1) - 6x^2A$. Hence

$$A - 1 - 3x = 5x(A-1) - 6x^2A \ \Longrightarrow\ A(1-5x+6x^2) = 1 + 3x - 5x = 1 - 2x,$$

$$A(x) = \frac{1-2x}{(1-2x)(1-3x)} = \frac{1}{1-3x} = \sum_{n\ge0}3^nx^n .$$

*Check.* $a_2 = 5\cdot3 - 6\cdot1 = 9 = 3^2$ ✓; $a_3 = 5\cdot9 - 6\cdot3 = 27 = 3^3$ ✓.

*Remark.* The characteristic roots are $2$ and $3$; the initial conditions make the coefficient of $2^n$ vanish, which is exactly the cancellation of the factor $1-2x$.

**14.** *Deriving the $n$ and $n^2$ series.* Start from $\frac{1}{1-x} = \sum_nx^n$ and apply $x\frac{d}{dx}$, which sends $x^n\mapsto nx^n$:

$$x\frac{d}{dx}\cdot\frac{1}{1-x} = x\cdot\frac{1}{(1-x)^2} = \frac{x}{(1-x)^2} = \sum_{n\ge0}nx^n .$$

Apply $x\frac{d}{dx}$ again:

$$x\frac{d}{dx}\cdot\frac{x}{(1-x)^2} = x\cdot\frac{(1-x)^2 + 2x(1-x)}{(1-x)^4} = x\cdot\frac{1-x+2x}{(1-x)^3} = \frac{x(1+x)}{(1-x)^3} = \sum_{n\ge0}n^2x^n .$$

*Check at $n=3$.* $\frac{x}{(1-x)^2} = x(1 + 2x + 3x^2 + 4x^3+\cdots)$, so the coefficient of $x^3$ is $3$ ✓. And $\frac{x(1+x)}{(1-x)^3} = (x+x^2)(1+3x+6x^2+10x^3+\cdots)$, so the coefficient of $x^3$ is $6 + 3 = 9 = 3^2$ ✓.

**15.** *Non-homogeneous recurrence.* Sum $a_n = 2a_{n-1}+3$ times $x^n$ over $n \ge 1$, using $a_0 = 1$ and $\sum_{n\ge1}x^n = x/(1-x)$:

$$A - 1 = 2xA + \frac{3x}{1-x} \ \Longrightarrow\ A(1-2x) = 1 + \frac{3x}{1-x} = \frac{1-x+3x}{1-x} = \frac{1+2x}{1-x},$$

$$A(x) = \frac{1+2x}{(1-x)(1-2x)} .$$

Partial fractions: $\frac{1+2x}{(1-x)(1-2x)} = \frac{P}{1-x} + \frac{Q}{1-2x}$, so $1+2x = P(1-2x) + Q(1-x)$. At $x=1$: $3 = -P$, so $P = -3$. At $x=\frac12$: $2 = \frac12Q$, so $Q = 4$. Hence

$$A(x) = -\frac{3}{1-x} + \frac{4}{1-2x}, \qquad a_n = 4\cdot2^n - 3 = 2^{n+2} - 3 .$$

*Check.* $a_0 = 4-3 = 1$ ✓; $a_1 = 2\cdot1+3 = 5$ and $8-3 = 5$ ✓; $a_2 = 2\cdot5+3 = 13$ and $16-3 = 13$ ✓.

*Remark.* The fixed point of the map $a\mapsto2a+3$ is $a = -3$, which is exactly the coefficient of $1/(1-x)$: the constant particular solution. The homogeneous part $4\cdot2^n$ is fixed by the initial condition.

**16.** *Central binomial coefficients from a differential equation.*

Write $A = \sum_na_nx^n$ with $a_0 = 1$ and impose $(1-4x)A'(x) = 2A(x)$ coefficient-wise.

*Left side.* $A'(x) = \sum_{n\ge0}(n+1)a_{n+1}x^n$, so

$$(1-4x)A'(x) = \sum_{n\ge0}(n+1)a_{n+1}x^n - 4\sum_{n\ge1}n\,a_nx^n .$$

*Comparing coefficients of $x^n$.* The right side contributes $2a_n$. For $n = 0$ this gives $a_1 = 2a_0 = 2$. For $n \ge 1$:

$$(n+1)a_{n+1} - 4n\,a_n = 2a_n \ \Longrightarrow\ (n+1)a_{n+1} = (4n+2)a_n \ \Longrightarrow\ a_{n+1} = \frac{2(2n+1)}{n+1}\,a_n .$$

*A uniqueness argument.* The recursion determines every $a_{n+1}$ from $a_0 = 1$, so there is at most one solution. To see that $b_n := \binom{2n}{n}$ is that solution, check the ratio:

$$\frac{b_{n+1}}{b_n} = \frac{(2n+2)(2n+1)}{(n+1)^2} = \frac{2(2n+1)}{n+1}, \qquad\text{since } \binom{2n+2}{n+1} = \frac{(2n+2)(2n+1)}{(n+1)^2}\binom{2n}{n}.$$

So $a_n = \binom{2n}{n}$ for every $n$.

*Identifying the series.* A series with $A(0)=1$ satisfying the first-order equation is unique, and $(1-4x)^{-1/2}$ is such a series because

$$\frac{d}{dx}(1-4x)^{-1/2} = 2(1-4x)^{-3/2}, \qquad (1-4x)\cdot 2(1-4x)^{-3/2} = 2(1-4x)^{-1/2}. ✓$$

Hence $A(x) = (1-4x)^{-1/2}$, that is $\sum_n\binom{2n}{n}x^n = (1-4x)^{-1/2}$.

*Value.* $a_4 = \binom84 = 70$; the recursion gives $a_1 = 2$, $a_2 = \frac{2\cdot3}{2}\cdot2 = 6$, $a_3 = \frac{2\cdot5}{3}\cdot6 = 20$, $a_4 = \frac{2\cdot7}{4}\cdot20 = 70$ ✓.

**17.** *Snake oil for $\sum_k\binom nk2^k$.* Using $\sum_{n\ge k}\binom nkx^n = x^k/(1-x)^{k+1}$ and interchanging,

$$\sum_{n\ge0}\left(\sum_k\binom nk2^k\right)x^n = \sum_{k\ge0}2^k\frac{x^k}{(1-x)^{k+1}} = \frac{1}{1-x}\sum_{k\ge0}\left(\frac{2x}{1-x}\right)^k = \frac{1}{1-x}\cdot\frac{1}{1-\frac{2x}{1-x}} = \frac{1}{1-3x}.$$

Hence $\sum_k\binom nk2^k = 3^n$.

*Check.* At $n = 3$: $1 + 3\cdot2 + 3\cdot4 + 8 = 27 = 3^3$ ✓.

**18.** *EGF of cyclic arrangements.* A cyclic arrangement of $n$ labels is a permutation consisting of a single cycle; there are $(n-1)!$ of them for $n \ge 1$. Hence

$$\sum_{n\ge1}(n-1)!\frac{x^n}{n!} = \sum_{n\ge1}\frac{x^n}{n} = -\ln(1-x),$$

using the formal logarithm $-\ln(1-x) = \sum_{n\ge1}x^n/n$.

*Check.* $[x^4](-\ln(1-x)) = \frac14$, and $4!\cdot\frac14 = 6 = (4-1)!$ ✓.

**19.** *Catalan recurrence.*

$$C_5 = C_0C_4 + C_1C_3 + C_2C_2 + C_3C_1 + C_4C_0 = 14+5+4+5+14 = 42 .$$

The closed form gives $\frac{1}{5+1}\dbinom{10}{5} = \frac{252}{6} = 42$ ✓.

*Check.* $C_4 = 14 = \frac15\binom84 = \frac{70}{5}$ ✓.

**20.** *Compositions into parts $1,2,3$.* A composition is a sequence of parts, so the generating function is the sequence construction applied to the "parts" series $x + x^2 + x^3$:

$$\frac{1}{1-(x+x^2+x^3)} = \frac{1}{1-x-x^2-x^3} .$$

The coefficients satisfy $a_n = a_{n-1}+a_{n-2}+a_{n-3}$ with $a_0 = 1$, $a_1 = 1$, $a_2 = 2$, giving

$$a_3 = 4,\ a_4 = 7,\ a_5 = 13,\ a_6 = 24 .$$

*Direct check at $n=3$.* The compositions of $3$ into parts $1,2,3$ are $1+1+1$, $1+2$, $2+1$, $3$ — four ✓.

**21.** *Partitions into distinct parts.* Each part size $k$ may be used at most once, so the factor is $1+x^k$:

$$\prod_{k\ge1}(1+x^k) = (1+x)(1+x^2)(1+x^3)\cdots .$$

The partitions of $8$ into distinct parts are $8$, $7+1$, $6+2$, $5+3$, $5+2+1$, $4+3+1$: six of them.

The partitions of $8$ into odd parts are $7+1$, $5+3$, $5+1+1+1$, $3+3+1+1$, $3+1+1+1+1+1$, $1^8$: also six.

The equality is not a coincidence: it is Euler's theorem, proved in Exercise 33 by the identity $\prod(1+x^k) = \prod_{m\text{ odd}}(1-x^m)^{-1}$.

**22.** *$1/(1-x-x^2)$.* Dividing the Fibonacci series $F(x) = x/(1-x-x^2) = \sum_nF_nx^n$ by $x$ shifts the coefficients:

$$\frac{1}{1-x-x^2} = \sum_{n\ge0}F_{n+1}x^n .$$

*Check at $n=5$.* The series begins $1 + x + 2x^2 + 3x^3 + 5x^4 + 8x^5+\cdots$, so the coefficient is $8 = F_6$ ✓.

**23.** *Partitions into exactly two blocks.* A partition of $[n]$ into two non-empty blocks is determined by the block containing the element $1$, which may be any subset $S$ of $\{2,\dots,n\}$ except $\{2,\dots,n\}$ itself (which would leave the second block empty). There are $2^{n-1}-1$ choices. At $n=6$: $2^5-1 = 31$.

*Check.* This is $S(n,2)$; the recurrence gives $S(6,2) = 2S(5,2)+S(5,1) = 2\cdot15+1 = 31$ ✓.

**24.** *$D_5$ from the EGF.*

$$D_5 = 5!\,[x^5]\frac{e^{-x}}{1-x} = 120\sum_{k=0}^{5}\frac{(-1)^k}{k!} = 120\left(1 - 1 + \frac12 - \frac16 + \frac1{24} - \frac1{120}\right).$$

Compute the bracket: $1-1 = 0$; $+\frac12$; $-\frac16 = \frac13$; $+\frac{1}{24} = \frac{3}{8}$; $-\frac{1}{120} = \frac{44}{120} = \frac{11}{30}$. Hence $D_5 = 120\cdot\frac{11}{30} = 44$.

*Check.* The derangement formula gives $120 - 120 + 60 - 20 + 5 - 1 = 44$ ✓.

## Advanced

**25.** *A double root.* Sum $a_n = 4a_{n-1}-4a_{n-2}$ times $x^n$ over $n\ge2$:

$$A - 1 - 4x = 4x(A-1) - 4x^2A \ \Longrightarrow\ A(1-4x+4x^2) = 1 + 4x - 4x = 1,$$

$$A(x) = \frac{1}{(1-2x)^2} = \sum_{n\ge0}(n+1)2^nx^n, \qquad a_n = (n+1)2^n .$$

*Check.* $a_2 = 16-4 = 12 = 3\cdot4$ ✓; $a_3 = 48-16 = 32 = 4\cdot8$ ✓.

*Remark.* The characteristic polynomial $(t-2)^2$ has a double root, and the double pole of $A$ at $x = \frac12$ produces the polynomial factor $n+1$ — the general phenomenon described after Theorem 8.1.

**26.** *Lucas numbers.*

*The functional equation.* Sum $L_n = L_{n-1}+L_{n-2}$ times $x^n$ over $n \ge 2$. The left side is $L(x) - L_0 - L_1x = L(x) - 2 - x$; the first sum on the right is $x(L - L_0) = x(L-2)$; the second is $x^2L$. Hence

$$L - 2 - x = x(L-2) + x^2L \ \Longrightarrow\ L(1-x-x^2) = 2 + x - 2x = 2 - x, \qquad L(x) = \frac{2-x}{1-x-x^2} .$$

*Partial fractions.* With $1-x-x^2 = (1-\varphi x)(1-\psi x)$, seek

$$\frac{2-x}{(1-\varphi x)(1-\psi x)} = \frac{P}{1-\varphi x} + \frac{Q}{1-\psi x}, \qquad 2 - x = P(1-\psi x) + Q(1-\varphi x).$$

Comparing coefficients: $P + Q = 2$ and $-P\psi - Q\varphi = -1$. Substituting $Q = 2 - P$ into the second relation:

$$-P\psi - (2-P)\varphi = -1 \ \Longrightarrow\ P(\varphi-\psi) = 2\varphi - 1 \ \Longrightarrow\ P = \frac{2\varphi-1}{\sqrt5} = \frac{\sqrt5}{\sqrt5} = 1,$$

using $2\varphi - 1 = (1+\sqrt5) - 1 = \sqrt5$ and $\varphi - \psi = \sqrt5$. Hence $Q = 1$ and

$$L(x) = \frac{1}{1-\varphi x} + \frac{1}{1-\psi x} = \sum_{n\ge0}\left(\varphi^n+\psi^n\right)x^n, \qquad L_n = \varphi^n+\psi^n .$$

*Check.* The series begins $2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123$, matching the recurrence. At $n = 10$: $\varphi^{10} = 122.991869\ldots$ and $\psi^{10} = 0.008130\ldots$; their sum is $122.999999\ldots = 123$ ✓. (The tiny shortfall is the truncation of the decimals; the exact sum is the integer $123$.)

*Relation to Fibonacci.* $L_n = F_{n-1}+F_{n+1}$ and $L_n = \varphi^n+\psi^n$ is the "Binet formula without the $\sqrt5$", because the numerator $2-x$ is exactly the combination that makes the two partial-fraction coefficients equal.

**27.** *Domino tilings of a $2\times n$ rectangle.*

*Structural recurrence.* Look at the leftmost column of the $2\times n$ rectangle. Either it is covered by one **vertical** domino, leaving a $2\times(n-1)$ rectangle, or it is covered by two **horizontal** dominoes stacked, which forces the next column as well and leaves a $2\times(n-2)$ rectangle. These cases are exhaustive and disjoint, so

$$a_n = a_{n-1} + a_{n-2} \qquad (n \ge 2), \qquad a_0 = 1,\ a_1 = 1 .$$

*Generating function.* Solving as in Theorem 7.7 (or by the formula for a second-order recurrence with these initial values):

$$A(x) = \frac{a_0 + (a_1-a_0)x}{1-x-x^2} = \frac{1}{1-x-x^2} = \sum_{n\ge0}F_{n+1}x^n,$$

where the last identity is the Fibonacci series divided by $x$ (Exercise 22). Hence $a_n = F_{n+1}$.

*Check.* The first values are $1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89$ for $n = 0,\dots,10$, so $a_{10} = 89 = F_{11}$ ✓. Directly for $n = 3$ there are exactly three tilings: three vertical dominoes; two horizontal dominoes followed by one vertical; one vertical followed by two horizontal. ✓

**28.** *Snake oil for $k(k-1)$.* Use $\sum_{n\ge k}\binom nkx^n = x^k/(1-x)^{k+1}$ and $y = x/(1-x)$:

$$\sum_{n\ge0}\left(\sum_k k(k-1)\binom nk\right)x^n = \sum_{k\ge0}k(k-1)\frac{x^k}{(1-x)^{k+1}} = \frac{1}{1-x}\sum_{k\ge0}k(k-1)y^k .$$

Now $\sum_k k(k-1)y^k = y^2\frac{d^2}{dy^2}\frac{1}{1-y} = \frac{2y^2}{(1-y)^3}$. Substituting $y = \frac{x}{1-x}$, $1-y = \frac{1-2x}{1-x}$:

$$\frac{1}{1-x}\cdot\frac{2x^2}{(1-x)^2}\cdot\frac{(1-x)^3}{(1-2x)^3} = \frac{2x^2}{(1-2x)^3} .$$

Hence

$$\sum_k k(k-1)\binom nk = 2\left[x^{n-2}\right]\,(1-2x)^{-3} = 2\binom{n}{2}2^{n-2} = n(n-1)2^{n-2} .$$

*Check at $n=4$.* $\sum_k k(k-1)\binom4k = 0+0+2\cdot6+6\cdot4+12\cdot1 = 12+24+12 = 48$, and $4\cdot3\cdot2^2 = 48$ ✓.

**29.** *Compositions with allowed parts $S$.* A composition is a sequence (possibly empty) of parts from $S$. The generating function of a single allowed part is $p(x) = \sum_{s\in S}x^s$ (with no constant term, since $0 \notin S$). A sequence of parts has generating function $\frac{1}{1-p(x)}$, by the sequence construction. Hence the number of compositions of $n$ is

$$\left[x^n\right]\frac{1}{1-\sum_{s\in S}x^s} .$$

For $S = \{2,3\}$: $\frac{1}{1-x^2-x^3}$, whose coefficients satisfy $a_n = a_{n-2}+a_{n-3}$ with $a_0 = 1$, $a_1 = 0$, $a_2 = 1$. Computing: $a_3 = 1$, $a_4 = 1$, $a_5 = 2$, $a_6 = 2$, $a_7 = 3$, $a_8 = 4$, $a_9 = 5$, $a_{10} = 7$.

*Direct check at $n=6$.* Compositions of $6$ into $2$s and $3$s: $3+3$, $2+2+2$ — two ✓, matching $a_6 = 2$.

**30.** *Bell EGF and $B_6$.* A set partition of $[n]$ is an unordered collection of non-empty blocks. A non-empty block is a non-empty set of labels, with EGF $e^x-1$. A **set** of blocks has EGF $\exp$ of the block EGF (the factor $1/k!$ in $\exp$ forgets the order of the $k$ blocks). Hence

$$\hat B(x) = \exp\left(e^x-1\right) = \sum_{n\ge0}B_n\frac{x^n}{n!} .$$

A partition into exactly $k$ ordered blocks has EGF $(e^x-1)^k$, so $S(n,k) = [x^n]\,(e^x-1)^k/k!$, and summing over $k$ recovers $B_n = \sum_kS(n,k)$.

For $B_6$: $S(6,\cdot) = (1, 31, 90, 65, 15, 1)$, so $B_6 = 1+31+90+65+15+1 = 203$.

*Check via the series.* Using $p_{n+1} = \frac{1}{n+1}\sum_kp_{n-k}/k!$ from Example 9.6 with $p_5 = 13/30$, one obtains $p_6 = \frac{1}{6}\left(p_5 + p_4 + \frac{p_3}{2} + \frac{p_2}{6} + \frac{p_1}{24} + \frac{p_0}{120}\right)$, and $6!\,p_6 = 203$; indeed $\exp(e^x-1) = 1+x+x^2+\frac56x^3+\frac58x^4+\frac{13}{30}x^5+\frac{203}{720}x^6+\cdots$, and $720\cdot\frac{203}{720} = 203$ ✓.

**31.** *Derangement EGF, two ways.*

*From inclusion–exclusion.* Divide $D_n = \sum_{k=0}^{n}(-1)^k\binom nk(n-k)!$ by $n!$; since $\frac1{n!}\binom nk(n-k)! = \frac1{k!}$,

$$\frac{D_n}{n!} = \sum_{k=0}^{n}\frac{(-1)^k}{k!} = \sum_{k=0}^{n}u_kv_{n-k}, \qquad u_k = \frac{(-1)^k}{k!},\ v_m = 1 .$$

This is a convolution, so the EGF is the product of $\sum_ku_kx^k = e^{-x}$ and $\sum_mv_mx^m = \frac{1}{1-x}$:

$$\hat D(x) = \frac{e^{-x}}{1-x} .$$

*From the combinatorial decomposition.* A permutation is determined by its set of fixed points (a set of atoms, EGF $e^x$) together with a derangement on the remaining labels (EGF $\hat D(x)$). The labelled product gives $\frac{1}{1-x} = e^x\hat D(x)$, hence $\hat D(x) = e^{-x}/(1-x)$ ✓.

*Extracting coefficients.* $[x^n]\hat D = \sum_{k=0}^{n}\frac{(-1)^k}{k!}$, so $D_n = n!\sum_{k\le n}(-1)^k/k!$, which is the formula of the [Inclusion–Exclusion](../02-inclusion-exclusion/README.md) tutorial. ✓

**32.** *Coefficients of $(1-x)^{-k}$.* *Claim:* $[x^n]\,(1-x)^{-k} = \binom{n+k-1}{k-1}$ for $k \ge 1$, $n \ge 0$.

*Proof by induction on $k$.* For $k=1$, $(1-x)^{-1} = \sum x^n$ and $\binom n0 = 1$ ✓. If the formula holds for $k$, then $(1-x)^{-(k+1)} = (1-x)^{-k}\cdot(1-x)^{-1}$ gives

$$\left[x^n\right]\,(1-x)^{-(k+1)} = \sum_{j=0}^{n}\binom{j+k-1}{k-1} = \binom{n+k}{k},$$

by the hockey-stick identity $\sum_{j=0}^{n}\binom{j+r}{r} = \binom{n+r+1}{r+1}$ with $r = k-1$. This is the formula for $k+1$. $\blacksquare$

*Weak compositions.* A solution of $e_1+\cdots+e_5 = 7$ in non-negative integers is a choice, for each of the $5$ variables, of a non-negative integer, recorded by the factor $\frac{1}{1-x}$; the number is

$$\left[x^7\right]\frac{1}{(1-x)^5} = \binom{7+4}{4} = \binom{11}{4} = 330 .$$

*Check.* Stars and bars gives $\binom{7+5-1}{5-1} = \binom{11}{4} = 330$ ✓.

## Challenge

**33.** *Euler's theorem: distinct parts equal odd parts.*

**Claim.** $\displaystyle\prod_{k\ge1}(1+x^k) = \prod_{m\ \text{odd}}\frac{1}{1-x^m}$.

*Proof.* Multiply numerator and denominator by $\prod_k(1-x^k)$:

$$\prod_{k\ge1}(1+x^k) = \prod_{k\ge1}\frac{(1+x^k)(1-x^k)}{1-x^k} = \frac{\prod_{k\ge1}(1-x^{2k})}{\prod_{k\ge1}(1-x^k)} .$$

In the numerator, the factors are $(1-x^m)$ over the **even** $m$; in the denominator, over **all** $m$. The quotient cancels every even factor and leaves

$$\frac{1}{\prod_{m\ \text{odd}}(1-x^m)},$$

which is the generating function for partitions into odd parts. The left side counts partitions into distinct parts, because each factor $1+x^k$ offers the choice "no part $k$" or "one part $k$". Hence the two families have equal size for every $n$. $\blacksquare$

*Verification at $n = 8$.* Distinct parts: $8$, $7+1$, $6+2$, $5+3$, $5+2+1$, $4+3+1$ — six. Odd parts: $7+1$, $5+3$, $5+1+1+1$, $3+3+1+1$, $3+1+1+1+1+1$, $1^8$ — six. ✓ (The lists are genuinely different; only the counts agree.)

**34.** *Lagrange inversion and the Catalan numbers.*

**Theorem (Lagrange inversion).** Let $\varphi(t) \in \mathbb{K}[[t]]$ with $\varphi(0) \ne 0$. Then there is a unique $w \in \mathbb{K}[[x]]$ with $w(0) = 0$ and $w = x\varphi(w)$, and for $n \ge 1$ and any $H \in \mathbb{K}[[t]]$,

$$\left[x^n\right]H\bigl(w(x)\bigr) = \frac1n\left[t^{n-1}\right]H'(t)\,\varphi(t)^n .$$

In particular, with $H(t) = t$: $[x^n]w = \frac1n[t^{n-1}]\varphi(t)^n$.

*Proof of the case $H(t) = t$ (following the general residue argument).* Write $\operatorname{Res}_x f := [x^{-1}]f$ for Laurent series. Two standard facts are used: the residue of a derivative is $0$, and the substitution rule $\operatorname{Res}_xF(x)\,dx = \operatorname{Res}_wF(x(w))\,x'(w)\,dw$ valid for $x(w) = w/\varphi(w)$.

For $n \ge 1$,

$$\left[x^n\right]w = \operatorname{Res}_x\,w(x)\,x^{-n-1}\,dx .$$

Substituting $x = w/\varphi(w)$, so that $x^{-n-1} = \varphi(w)^{n+1}/w^{n+1}$ and $dx = \frac{\varphi(w)-w\varphi'(w)}{\varphi(w)^2}\,dw$:

$$\left[x^n\right]w = \operatorname{Res}_w\,\frac{w\,\varphi(w)^{n-1}\bigl(\varphi(w)-w\varphi'(w)\bigr)}{w^{n+1}}\,dw .$$

Now use $\varphi^{n-1}(\varphi - w\varphi') = \varphi^n - \frac{w}{n}(\varphi^n)'$, which follows from $(\varphi^n)' = n\varphi^{n-1}\varphi'$. Then

$$\frac{w\varphi^{n-1}(\varphi - w\varphi')}{w^{n+1}} = \frac{\varphi^n}{w^n} - \frac{(\varphi^n)'}{n\,w^{n-1}} = \frac{\varphi^n}{w^n} - \frac1n\frac{d}{dw}\left(\frac{\varphi^n}{w^{n-1}}\right) - (n-1)\frac{\varphi^n}{n\,w^n},$$

where the last step differentiates the quotient. Combining the non-derivative terms,

$$\left(1 - \frac{n-1}{n}\right)\frac{\varphi^n}{w^n} = \frac1n\cdot\frac{\varphi^n}{w^n},$$

and the derivative term has residue $0$. Hence

$$\left[x^n\right]w = \frac1n\operatorname{Res}_w\frac{\varphi(w)^n}{w^n}\,dw = \frac1n\left[w^{n-1}\right]\varphi(w)^n . \qquad \blacksquare$$

*Application.* Put $w = C - 1$, so that $w = x(1+w)^2$ and $\varphi(t) = (1+t)^2$. For $n \ge 1$,

$$C_n = \left[x^n\right]C = \left[x^n\right]w = \frac1n\left[t^{n-1}\right]\,(1+t)^{2n} = \frac1n\binom{2n}{n-1} .$$

*Agreement with the other form.* Since $\frac1n\binom{2n}{n-1} = \frac{(2n)!}{n\,(n-1)!\,(n+1)!} = \frac{(2n)!}{n!\,(n+1)!} = \frac{1}{n+1}\binom{2n}{n}$ ✓.

*Check at $n=4$.* $\frac14\binom83 = \frac{56}{4} = 14 = C_4$ ✓.

**35.** *Asymptotics of the Catalan numbers.*

Start from $C_n = \frac{(2n)!}{(n+1)(n!)^2}$ and Stirling's formula $n! \sim \sqrt{2\pi n}\,(n/e)^n$:

$$(2n)! \sim \sqrt{4\pi n}\left(\frac{2n}{e}\right)^{2n}, \qquad (n!)^2 \sim 2\pi n\left(\frac ne\right)^{2n}.$$

Therefore

$$C_n \sim \frac{\sqrt{4\pi n}\,(2n/e)^{2n}}{(n+1)\cdot2\pi n\,(n/e)^{2n}} = \frac{\sqrt{4\pi n}}{2\pi n}\cdot\frac{1}{n+1}\cdot4^n = \frac{4^n}{\sqrt{\pi n}\,(n+1)} .$$

Finally $\frac{1}{\sqrt{\pi n}(n+1)} = \frac{1}{\sqrt\pi\,n^{3/2}}\cdot\frac{1}{1+1/n} \sim \frac{1}{\sqrt\pi\,n^{3/2}}$, so

$$C_n \sim \frac{4^n}{n^{3/2}\sqrt\pi} . \qquad \blacksquare$$

*Numerical check.* At $n=10$: $C_{10} = 16\,796$, while $4^{10}/(10^{3/2}\sqrt\pi) = 1\,048\,576/(31.6228\times1.77245) = 18\,706$. The ratio is $0.898$, consistent with a relative error of order $1/n = 0.1$. At $n = 100$ the ratio is about $0.990$. ✓

The exponent $3/2$ is not accidental: it is $\frac12$ (from the square root in $C(x)$) plus $1$ (from the simple pole structure of the extraction), which is the standard signature of a square-root singularity in the Flajolet–Odlyzko theory.

**36.** *Permutations with all cycles of odd length.*

*Derivation.* A single cycle of odd length $k$ has $(k-1)!$ realisations on $k$ labels, hence EGF contribution $\frac{(k-1)!}{k!}x^k = \frac{x^k}{k}$. Summing over odd $k$,

$$\sum_{k\ \text{odd}}\frac{x^k}{k} = \frac12\left[\sum_{k\ge1}\frac{x^k}{k} - \sum_{k\ge1}\frac{(-x)^k}{k}\right] = \frac12\left[-\ln(1-x) + \ln(1+x)\right] = \frac12\ln\frac{1+x}{1-x},$$

where $\ln(1+x) = \sum_{k\ge1}(-1)^{k+1}x^k/k$ and $-\ln(1-x) = \sum_{k\ge1}x^k/k$.

A permutation with all cycles odd is a **set** of odd cycles, so its EGF is the exponential of the block EGF:

$$\hat A(x) = \exp\left(\frac12\ln\frac{1+x}{1-x}\right) = \sqrt{\frac{1+x}{1-x}} . \qquad \blacksquare$$

*Values.* Instead of multiplying the two binomial series by hand, use a differential equation. Since $\hat A = \exp(A)$ with $A = \frac12\ln\frac{1+x}{1-x}$ and $A' = \frac{1}{1-x^2}$,

$$(1-x^2)\,\hat A'(x) = \hat A(x).$$

Writing $\hat A = \sum e_nx^n$ and comparing coefficients of $x^n$ gives

$$(n+1)e_{n+1} - (n-1)e_{n-1} = e_n \qquad (n \ge 0),$$

where the second term is absent when $n \le 1$. Starting from $e_0 = 1$:

$$e_1 = 1,\qquad e_2 = \tfrac12,\qquad e_3 = \tfrac12,\qquad e_4 = \tfrac38,\qquad e_5 = \tfrac38,\qquad e_6 = \tfrac{5}{16}.$$

For example, at $n=5$: $6e_6 - 4e_4 = e_5$ gives $6e_6 - \frac32 = \frac38$, so $e_6 = \frac{15}{48} = \frac{5}{16}$. Multiplying by $n!$ gives the counts

| $n$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|---|
| $a_n$ | 1 | 1 | 1 | 3 | 9 | 45 | 225 |

*Check by cycle types.* For $n=4$ the allowed cycle types are $(3,1)$ and $(1^4)$: there are $8$ permutations of type $(3,1)$ and $1$ of type $(1^4)$, total $9$ ✓ (4-cycles are excluded because $4$ is even). For $n=5$: types $(5)$, $(3,1,1)$, $(1^5)$ give $24 + 20 + 1 = 45$ ✓.
