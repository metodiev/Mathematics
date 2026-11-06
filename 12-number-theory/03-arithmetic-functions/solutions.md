# Arithmetic Functions — Solutions

> [Arithmetic Functions](README.md) · Solutions to the 36 problems in [exercises.md](exercises.md)

Every solution names the strategy and the theorem used, and displays the arithmetic. Numerical answers are checked by a second method wherever one exists. Section references point into the [tutorial](README.md).

## Beginner

**1.** *Strategy: factorise, then apply $d(n)=\prod(a_i+1)$, $\sigma(n)=\prod\frac{p^{a+1}-1}{p-1}$, $\varphi(n)=n\prod_{p\mid n}(1-1/p)$.*

(a) $18 = 2\cdot 3^{2}$.

$$d(18) = (1+1)(2+1) = 6, \qquad \sigma(18) = \frac{2^{2}-1}{1}\cdot\frac{3^{3}-1}{2} = 3\cdot13 = 39, \qquad \varphi(18) = 18\cdot\frac12\cdot\frac23 = 6.$$

*Check:* divisors $1,2,3,6,9,18$ — six of them, summing to $39$; and the numbers $\le 18$ coprime to $18$ are $1,5,7,11,13,17$, six of them. ✓

(b) $45 = 3^{2}\cdot 5$.

$$d(45) = 3\cdot2 = 6, \qquad \sigma(45) = 13\cdot 6 = 78, \qquad \varphi(45) = 45\cdot\frac23\cdot\frac45 = 24.$$

*Check:* $1+3+5+9+15+45 = 78$ ✓; $\varphi(45) = \varphi(9)\varphi(5) = 6\cdot4 = 24$ ✓.

(c) $100 = 2^{2}\cdot 5^{2}$.

$$d(100) = 3\cdot3 = 9, \qquad \sigma(100) = 7\cdot31 = 217, \qquad \varphi(100) = 100\cdot\frac12\cdot\frac45 = 40.$$

*Check:* divisors $1,2,4,5,10,20,25,50,100$ sum to $217$ ✓; $\varphi(100) = 100 - 50 - 20 + 10 = 40$ by inclusion–exclusion ✓.

(d) $210 = 2\cdot3\cdot5\cdot7$.

$$d(210) = 2^{4} = 16, \qquad \sigma(210) = 3\cdot4\cdot6\cdot8 = 576, \qquad \varphi(210) = 210\cdot\frac12\cdot\frac23\cdot\frac45\cdot\frac67 = 48.$$

*Check:* $210$ is squarefree, so $d = 2^{4} = 16$ and $\varphi = (2-1)(3-1)(5-1)(7-1) = 48$ ✓.

**2.** *Strategy: test $f(4)$ against $f(2)^{2}$ for complete multiplicativity, and $f(m)f(n)$ against $f(mn)$ at a non-coprime pair. For additivity, test $\omega(4)$ and $\Omega(4)$.*

(a) **$d$: multiplicative, not completely.** Multiplicativity is Theorem 7.3.1 (a product over distinct primes). Failure: $d(4) = 3 \ne d(2)d(2) = 4$.

(b) **$\sigma$: multiplicative, not completely.** Theorem 7.3.2. Failure: $\sigma(4) = 7 \ne \sigma(2)^{2} = 9$.

(c) **$\varphi$: multiplicative, not completely.** Theorem 7.4.3. Failure: $\varphi(4) = 2 \ne \varphi(2)^{2} = 1$.

(d) **$\mu$: multiplicative, not completely.** Lemma 7.5.2. Failure: $\mu(4) = 0 \ne \mu(2)^{2} = 1$.

(e) **$n\mapsto n^{3}$: completely multiplicative**, since $(mn)^{3} = m^{3}n^{3}$ for all $m,n$.

(f) **$\omega$: additive, not completely additive.** For coprime $m,n$ the prime sets are disjoint, so $\omega(mn) = \omega(m)+\omega(n)$ — this is **not** a multiplicative function, because $\omega(1) = 0 \ne 1$; indeed $\omega(1\cdot n) = \omega(n)$ but $0\cdot\omega(n) = 0$. Failure of complete additivity: $\omega(4) = 1 \ne 2 = 2\omega(2)$.

(g) **$\Omega$: completely additive.** Every prime factor of $mn$ is a prime factor of $m$ or of $n$, counted with the sum of multiplicities, so $\Omega(mn) = \Omega(m)+\Omega(n)$ for all $m,n$. Not multiplicative, again because $\Omega(1) = 0$.

(h) **$n \mapsto (-1)^{n}$: none of these.** Multiplicativity fails at $m=3$, $n=5$: $(-1)^{15} = -1$ but $(-1)^{3}(-1)^{5} = (+1)$. (It passes accidentally at $m=2,n=3$ because both sides are $+1$ — a warning about testing a claim on one example.)

(i) **$n\mapsto 2^{\omega(n)}$: multiplicative, not completely.** For coprime $m,n$, $2^{\omega(mn)} = 2^{\omega(m)+\omega(n)} = 2^{\omega(m)}2^{\omega(n)}$. Failure: $2^{\omega(4)} = 2$, but $2^{\omega(2)}2^{\omega(2)} = 4$.

**3.** *Strategy: $\mu(n)=0$ exactly when $n$ has a square factor; otherwise compute $(-1)^{\omega(n)}$.*

(a) Using the factorisations $1,2,3,2^2,5,2\cdot3,7,2^3,3^2,2\cdot5,11,2^2\cdot3,13,2\cdot7,3\cdot5,2^4,17,2\cdot3^2,19,2^2\cdot5$:

| $n$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ | $7$ | $8$ | $9$ | $10$ | $11$ | $12$ | $13$ | $14$ | $15$ | $16$ | $17$ | $18$ | $19$ | $20$ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| $\mu(n)$ | $1$ | $-1$ | $-1$ | $0$ | $-1$ | $1$ | $-1$ | $0$ | $0$ | $1$ | $-1$ | $0$ | $-1$ | $1$ | $1$ | $0$ | $-1$ | $0$ | $-1$ | $0$ |

(b) $\mu(n) = -1$ for $n \in \{2,3,5,7,11,13,17,19\}$ — the primes $\le 20$, since a prime has $\omega = 1$ and is squarefree. $\mu(n) = 0$ for $n\in\{4,8,9,12,16,18,20\}$ — exactly the numbers with a square divisor $>1$.

(c) Because $\mu(6) = 1$ and $6 = 2\cdot3$ is composite: $\mu$ measures the presence of a repeated prime factor, not the number of factors. Similarly $\mu(30) = -1$.

**4.** *Strategy: the same three formulas, with the factorisations given.*

(a) $720 = 2^{4}\cdot3^{2}\cdot5$:

$$d(720) = (4+1)(2+1)(1+1) = 30,$$
$$\sigma(720) = \frac{2^{5}-1}{1}\cdot\frac{3^{3}-1}{2}\cdot\frac{5^{2}-1}{4} = 31\cdot13\cdot6 = 2418,$$
$$\varphi(720) = 720\cdot\frac12\cdot\frac23\cdot\frac45 = 720\cdot\frac{8}{30} = 192.$$

(b) $1001 = 7\cdot11\cdot13$ (all exponents $1$):

$$d(1001) = 8, \qquad \sigma(1001) = 8\cdot12\cdot14 = 1344, \qquad \varphi(1001) = 6\cdot10\cdot12 = 720.$$

*Independent check for $\sigma$.* The eight divisors are $1,7,11,13,77,91,143,1001$. Pairing $d$ with $1001/d$: $1+1001 = 1002$, $7+143 = 150$, $11+91 = 102$, $13+77 = 90$; total $1002+150+102+90 = 1344$ ✓. Also $\varphi(1001) = 720 = 6!$ is a pleasant coincidence, not an identity.

**5.** *Strategy: $\varphi(p^{a}) = p^{a}-p^{a-1}$ for prime powers, $\varphi = \varphi(p_1^{a_1})\cdots$ for the rest.*

* $12 = 2^{2}\cdot3$: $\varphi(12) = 2\cdot2 = 4$.
* $25 = 5^{2}$: $\varphi(25) = 25-5 = 20$.
* $36 = 2^{2}\cdot3^{2}$: $\varphi(36) = 2\cdot6 = 12$.
* $60 = 2^{2}\cdot3\cdot5$: $\varphi(60) = 2\cdot2\cdot4 = 16$.
* $97$ prime: $\varphi(97) = 96$.
* $128 = 2^{7}$: $\varphi(128) = 128-64 = 64$.

*Listing check for $25$:* the numbers $1\le k\le25$ not coprime to $25$ are the multiples of $5$, namely $5,10,15,20,25$ — five of them. Hence $\varphi(25) = 25-5 = 20$ ✓.

*Check for $36$:* $\varphi(36) = 36\cdot\frac12\cdot\frac23 = 12$, and the coprimes are $1,5,7,11,13,17,19,23,25,29,31,35$ — twelve ✓.

**6.** *Strategy: compare $\sigma(n)$ with $2n$.*

| $n$ | factorisation | $\sigma(n)$ | $2n$ | verdict |
|---|---|---|---|---|
| $6$ | $2\cdot3$ | $1+2+3+6 = 12$ | $12$ | **perfect** |
| $16$ | $2^{4}$ | $31$ | $32$ | deficient |
| $28$ | $2^{2}\cdot7$ | $7\cdot8 = 56$ | $56$ | **perfect** |
| $45$ | $3^{2}\cdot5$ | $13\cdot6 = 78$ | $90$ | deficient |
| $496$ | $2^{4}\cdot31$ | $31\cdot32 = 992$ | $992$ | **perfect** |
| $945$ | $3^{3}\cdot5\cdot7$ | $40\cdot6\cdot8 = 1920$ | $1890$ | **abundant** |

The smallest odd abundant number is $945$: an enumeration of the odd numbers below $945$ gives $\sigma(n) < 2n$ for every one of them, and $\sigma(945) = 1920 > 1890$. Note $945 = 3^{3}\cdot5\cdot7$ has abundancy index $\frac{1920}{1890} = \frac{64}{63}\cdot\frac{1890}{1890}\approx 2.032$.

**7.** *Strategy: write out all divisors of $10$ — namely $1,2,5,10$ — and use $\mu(1)=1$, $\mu(2)=\mu(5)=-1$, $\mu(10)=+1$, $d(1)=1$, $d(2)=d(5)=2$, $d(10)=4$, $\varphi(1)=1$, $\varphi(2)=1$, $\varphi(5)=4$, $\varphi(10)=4$.*

(a) $(d*\mu)(10) = d(1)\mu(10) + d(2)\mu(5) + d(5)\mu(2) + d(10)\mu(1) = 1\cdot1 + 2\cdot(-1) + 2\cdot(-1) + 4\cdot1 = 1 - 2 - 2 + 4 = 1$.

This confirms $d*\mu = 1$: since $d = 1*1$, we get $d*\mu = (1*1)*\mu = 1*(1*\mu) = 1*\varepsilon = 1$.

(b) $(\varphi*1)(10) = \varphi(1)+\varphi(2)+\varphi(5)+\varphi(10) = 1+1+4+4 = 10$.

This confirms Corollary 7.4.4, $\sum_{d\mid n}\varphi(d) = n$, at $n=10$.

(c) $(\mu*\mu)(10) = \mu(1)\mu(10)+\mu(2)\mu(5)+\mu(5)\mu(2)+\mu(10)\mu(1) = 1 + 1 + 1 + 1 = 4$.

This confirms the multiplicativity of $\mu*\mu$ together with $(\mu*\mu)(p) = \mu(1)\mu(p)+\mu(p)\mu(1) = -2$: at $n = pq$ the value is $(-2)(-2) = 4$.

**8.** *Strategy: list divisors and totients, then explain the fraction bijection.*

Divisors of $20$: $1,2,4,5,10,20$. Their totients: $\varphi(1)=1$, $\varphi(2)=1$, $\varphi(4)=2$, $\varphi(5)=4$, $\varphi(10)=4$, $\varphi(20)=8$. Sum:

$$1+1+2+4+4+8 = 20. ✓$$

*Bijective reason.* Consider the $20$ fractions $\frac{1}{20},\frac{2}{20},\dots,\frac{20}{20}$. Reduce each to lowest terms: the reduced fractions with denominator $d$ are exactly those $\frac{k}{d}$ with $1\le k\le d$ and $\gcd(k,d)=1$, and there are $\varphi(d)$ of them. Since $d$ must divide $20$ (it is the denominator after reduction of $\frac{m}{20}$), every fraction is counted exactly once by some $d \mid 20$. Hence $\sum_{d\mid20}\varphi(d) = 20$. The same argument proves Corollary 7.4.4 for every $n$.

**9.** *Strategy: $d(n) = \prod(a_i+1) = 4$ forces the multiset of exponents either $\{3\}$ or $\{1,1\}$.*

Since $4 = 4$ or $4 = 2\cdot2$, the exponent pattern is either a single exponent $3$, giving $n = p^{3}$, or two exponents $1$, giving $n = pq$ with $p\ne q$ prime. (The patterns $\{1,1,1,\dots\}$ give $d = 2^{r}$, which equals $4$ only for $r=2$.)

List with this structure, up to $50$:

* cubes of primes: $2^{3} = 8$, $3^{3} = 27$ (and $5^{3} = 125 > 50$);
* products of two distinct primes: $2\cdot3 = 6$, $2\cdot5 = 10$, $2\cdot7 = 14$, $2\cdot11 = 22$, $2\cdot13 = 26$, $2\cdot17 = 34$, $2\cdot19 = 38$, $2\cdot23 = 46$; $3\cdot5 = 15$, $3\cdot7 = 21$, $3\cdot11 = 33$, $3\cdot13 = 39$; $5\cdot7 = 35$.

Altogether

$$n \in \{6, 8, 10, 14, 15, 21, 22, 26, 27, 33, 34, 35, 38, 39, 46\}.$$

*Check:* direct enumeration of $d(n)$ for $n \le 50$ returns exactly this list, and $n = 50 = 2\cdot5^{2}$ has $d = 6$, correctly excluded.

**10.** *Strategy: $\sigma(2^{a}) = 2^{a+1}-1$ is a geometric sum; $\sigma(3^{a}) = 1+3+\dots+3^{a}$ has $a+1$ odd terms.*

$$\sigma(2^{10}) = \frac{2^{11}-1}{2-1} = 2047.$$

The divisors of $2^{a}$ are $1,2,4,\dots,2^{a}$, and

$$\sigma(2^{a}) = 1+2+\cdots+2^{a} = 2^{a+1}-1,$$

which is odd because $2^{a+1}$ is even. For $3^{a}$ the sum $1+3+\cdots+3^{a}$ has $a+1$ **odd** terms, so it is odd iff $a+1$ is odd, i.e. iff $a$ is even. Indeed $\sigma(3^{0}) = 1$, $\sigma(3^{1}) = 4$, $\sigma(3^{2}) = 13$, $\sigma(3^{3}) = 40$. This is the parity mechanism behind Corollary 7.3.5: for odd $p$, the parity of $\sigma(p^{a})$ is the parity of $a+1$.

**11.** *Strategy: compute $\varphi(8)$, $\varphi(9)$, $\varphi(72)$ and compare; then exhibit a non-coprime pair.*

$\varphi(8) = 8-4 = 4$, $\varphi(9) = 9-3 = 6$, and $72 = 2^{3}3^{2}$ gives $\varphi(72) = 72\cdot\frac12\cdot\frac23 = 24$. Since $24 = 4\cdot6$, multiplicativity holds at $(8,9)$, as it must because $\gcd(8,9)=1$.

At $(2,4)$: $\varphi(2) = 1$, $\varphi(4) = 2$, so $\varphi(2)\varphi(4) = 2$, but $\varphi(8) = 4$. Multiplicativity fails. The violated hypothesis is $\gcd(m,n)=1$: here $\gcd(2,4) = 2$. Note the failure is not small — the product is off by a factor of $2$ — and it is caused by the prime $2$ being counted twice in $2\cdot4$.

**12.** *Strategy: $\mu$ vanishes on $4 \mid d$; the surviving divisors of $36$ are $1,2,3,6,9,18$ with $\mu$ values $1,-1,-1,1,0,0$.*

$$\sum_{d\mid36}\mu(d) = 1 - 1 - 1 + 1 + 0 + 0 = 0,$$

as Lemma 7.5.2 requires since $36 > 1$ (the binomial sum $(1-1)^{2} = 0$ uses the two distinct primes $2,3$).

$$\sum_{d\mid36}\mu^{2}(d) = 1+1+1+1+0+0 = 4.$$

The squarefree divisors of $36$ are $1,2,3,6$ — four of them, and $2^{\omega(36)} = 2^{2} = 4$. The two counts agree because $\mu^{2}(d) = |\mu(d)|$ for every $d$: both are $1$ exactly for squarefree $d$ and $0$ otherwise.

## Intermediate

**13.** *Strategy: multiplicativity of $f$ applies to $m^{2}$ and $n^{2}$ because $\gcd(m,n)=1$ implies $\gcd(m^{2},n^{2})=1$.*

Let $\gcd(m,n)=1$. Then $\gcd(m^{2},n^{2}) = \gcd(m,n)^{2} = 1$, so

$$g(mn) = f\big((mn)^{2}\big) = f(m^{2}n^{2}) = f(m^{2})f(n^{2}) = g(m)g(n).$$

Hence $g$ is multiplicative. For $f = \mu$: if $n > 1$ then $n^{2}$ has a square divisor $p^{2}$ for any prime $p\mid n$, so $\mu(n^{2}) = 0$; and $\mu(1^{2}) = 1$. Therefore $g(n) = [n=1] = \varepsilon(n)$.

*Remark.* The same argument shows $n\mapsto f(n^{k})$ is multiplicative for every $k\ge1$. It does **not** show that $f(n^{2}) = f(n)^{2}$; indeed for $f=\mu$ we have $\mu(2^{2}) = 0 \ne 1 = \mu(2)^{2}$. In the language of §7.6, $n\mapsto f(n^{2})$ is the composition of $f$ with the completely multiplicative map $n \mapsto n^{2}$.

**14.** *Strategy: both directions are inductions on the number $r$ of distinct primes.*

(⇒) Suppose $f$ is multiplicative. If $f$ is not identically zero, Lemma 5.2.3 gives $f(1)=1$. For $r=1$ there is nothing to prove. For $r \ge 2$, put $m = p_1^{a_1}\cdots p_{r-1}^{a_{r-1}}$ and $P = p_r^{a_r}$. Then $\gcd(m,P)=1$, so

$$f\!\left(p_1^{a_1}\cdots p_r^{a_r}\right) = f(mP) = f(m)f(P),$$

and by induction $f(m) = \prod_{i<r}f(p_i^{a_i})$. This is Theorem 7.1.1.

(⇐) Suppose $f(1)=1$ and $f$ is multiplicative on factorisations of the stated form. Let $\gcd(m,n)=1$, with $m = p_1^{a_1}\cdots p_r^{a_r}$ and $n = q_1^{b_1}\cdots q_s^{b_s}$; coprimality says the $p_i$ and $q_j$ are all distinct. Then $mn = p_1^{a_1}\cdots p_r^{a_r}q_1^{b_1}\cdots q_s^{b_s}$ is a factorisation into distinct primes, so by hypothesis

$$f(mn) = \prod_i f(p_i^{a_i})\prod_j f(q_j^{b_j}) = f(m)f(n).$$

Hence $f$ is multiplicative. $\blacksquare$

**15.** *Strategy: pair each divisor $d < \sqrt n$ with $n/d > \sqrt n$.*

For each divisor $d$ of $n$ the number $n/d$ is again a divisor, and $d\cdot(n/d) = n$. The map $d\mapsto n/d$ is an involution on the divisor set. Its fixed points satisfy $d = n/d$, i.e. $n = d^{2}$. Hence the divisors split into fixed points (at most one, present iff $n$ is a square) and two-element orbits $\{d, n/d\}$. Therefore

$$d(n) = 2\cdot(\text{number of orbits of size }2) + [n \text{ is a square}],$$

which is odd exactly when $n$ is a square.

The $n\le100$ with $d(n)$ odd are the squares

$$1, 4, 9, 16, 25, 36, 49, 64, 81, 100,$$

ten of them, exactly as many as there are squares up to $100$ (namely $\lfloor\sqrt{100}\rfloor = 10$). ✓

**16.** *Strategy: $\sigma$ is multiplicative, so reduce to prime powers, and count odd terms.*

Since $\sigma$ is multiplicative (Theorem 7.3.2), $\sigma(n)$ is odd iff $\sigma(p^{a})$ is odd for every prime power $p^{a} \parallel n$.

* $p = 2$: $\sigma(2^{a}) = 2^{a+1}-1$ is always odd.
* $p$ odd: $\sigma(p^{a}) = 1+p+\cdots+p^{a}$ is a sum of $a+1$ odd terms, hence odd iff $a$ is even.

So $\sigma(n)$ is odd iff every odd prime occurs to an even exponent, i.e. iff $n = 2^{a}u^{2}$ with $u$ odd. If $a$ is even this is a square, $n = (2^{a/2}u)^{2}$; if $a$ is odd it is twice a square, $n = 2(2^{(a-1)/2}u)^{2}$.

*Checks.* $18 = 2\cdot3^{2}$: twice a square ($9$), and $\sigma(18) = 3\cdot13 = 39$, odd ✓. $50 = 2\cdot5^{2}$: twice a square ($25$), and $\sigma(50) = 3\cdot31 = 93$, odd ✓. Contrast $n = 12 = 2^{2}\cdot3$: the odd prime $3$ has exponent $1$, so $\sigma(12) = 28$ is even ✓.

**17.** *Strategy: squarefree divisors correspond to subsets of the set of primes dividing $n$.*

Let $P$ be the set of distinct primes dividing $n$, so $\lvert P\rvert = \omega(n)$. A divisor $d$ of $n$ is squarefree iff every prime in $d$ occurs to the first power iff $d = \prod_{p\in S}p$ for a unique $S\subseteq P$. Distinct subsets give distinct products (uniqueness of factorisation), and every subset gives a divisor. Hence there are $2^{\omega(n)}$ squarefree divisors.

For $360 = 2^{3}3^{2}5$ we have $\omega(360) = 3$, so there are $8$ squarefree divisors: $1,2,3,5,6,10,15,30$. Therefore

$$\sum_{d\mid360}\mu^{2}(d) = 8, \qquad \sum_{d\mid360}|\mu(d)| = 8.$$

The two sums are equal for **every** $n$, because $\mu^{2}(d) = |\mu(d)|$: both equal $1$ if $d$ is squarefree and $0$ otherwise.

**18.** *Strategy: reindex the divisor sum by the complementary divisor.*

In $(f*g)(n) = \sum_{d\mid n}f(d)g(n/d)$ put $b = n/d$. As $d$ runs over the divisors of $n$, $b$ runs over the divisors of $n$ as well (the map $d\mapsto n/d$ is a bijection of the divisor set), and $d = a$ with $ab = n$. Hence

$$(f*g)(n) = \sum_{ab=n}f(a)g(b),$$

the sum over ordered pairs, since the order matters ($f(a)g(b) \ne f(b)g(a)$ in general).

Now $d*d = (1*1)*(1*1) = 1*1*1*1$ by associativity, and unravelling the definition four times gives

$$(d*d)(n) = \sum_{abce = n}1 = \#\{(a,b,c,e)\in\mathbb{N}^{4} : abce = n\} = \tau_4(n).$$

For $n=12$, the convolution formula gives

$$(d*d)(12) = \sum_{d\mid12}d(d)\,d(12/d) = 1\cdot6 + 2\cdot4 + 2\cdot3 + 3\cdot2 + 4\cdot2 + 6\cdot1 = 6+8+6+6+8+6 = 40.$$

*Independent count of the quadruples.* Group by the first coordinate $a\mid 12$. For fixed $a$, the remaining three coordinates satisfy $bce = 12/a$, and the number of such triples is $\tau_3(12/a) = \sum_{b\mid 12/a}d(12/(ab))$:

| $a$ | $1$ | $2$ | $3$ | $4$ | $6$ | $12$ |
|---|---|---|---|---|---|---|
| $12/a$ | $12$ | $6$ | $4$ | $3$ | $2$ | $1$ |
| $\tau_3(12/a)$ | $6+4+3+2+2+1 = 18$ | $4+2+2+1 = 9$ | $3+2+1 = 6$ | $2+1 = 3$ | $2+1 = 3$ | $1$ |

Total $18+9+6+3+3+1 = 40$ ✓, matching the convolution. Two sanity values: $\tau_3(12) = 18$ counts the ordered triples with product $12$ (e.g. $(1,1,12)$ through $(12,1,1)$), and $(d*d)(12) = 40 = \tau_4(12)$ counts the quadruples. Note also that $(d*d)(12) \ne \tau_3(12)$ — conflating $\tau_3$ with $\tau_4$ is a common slip.

**19.** *Strategy: pair $k$ with $n-k$ for the parity; for the equations, bound the number of prime factors.*

*Parity.* If $\gcd(k,n)=1$ then $\gcd(n-k,n) = \gcd(k,n) = 1$. The map $k\mapsto n-k$ is an involution of $\{1,\dots,n\}$ onto itself, and it has a fixed point only if $k = n-k$, i.e. $n = 2k$; then $\gcd(k,n) = k$, so a fixed point is a unit only when $k=1$ and $n=2$. Hence for $n\ge3$ the units come in pairs and $\varphi(n)$ is even.

*$\varphi(n)=2$.* If $n$ has $r$ distinct prime factors then $\varphi(n)\ge\prod_{p\mid n}(p-1)$; for a prime $p\ge5$ this factor is at least $4$, and for three distinct primes it is at least $1\cdot2\cdot4 = 8$. So $r\le2$ and any odd prime factor is $3$ or $5$.

* one prime: $\varphi(p^{a}) = p^{a-1}(p-1) = 2$ gives $p=2,a=2$ (so $n=4$), $p=3,a=1$ (so $n=3$), and nothing else since $p\ge5$ makes $p-1\ge4$;
* two primes, $n = 2^{a}3^{b}$: $\varphi = 2^{a-1}\cdot2\cdot3^{b-1} = 2^{a}3^{b-1} = 2$ forces $b=1$ and $a=1$, so $n=6$; any other pair has $\varphi \ge 1\cdot4 = 4$.

Hence $\{n : \varphi(n) = 2\} = \{3,4,6\}$.

*$\varphi(n)=4$.* Again $r\le 2$ (three distinct primes give $\varphi\ge8$).

* one prime: $p^{a-1}(p-1)=4$ gives $p=2,a=3$ ($n=8$), $p=5,a=1$ ($n=5$); $p=3$ gives $3^{a-1}\cdot2 = 4$, impossible; $p\ge7$ gives $p-1\ge6>4$;
* two primes: if both are odd then $\varphi\ge2\cdot2 = 4$ with equality only at $p=3,q=3$, not distinct; and $(3-1)(5-1) = 8$. So one prime is $2$: $n = 2^{a}q^{b}$ with $q$ odd. Since $q \mid \varphi(n)$ when $b\ge2$, we need $b=1$; then $2^{a-1}(q-1) = 4$ gives $(a,q) = (1,5)$ i.e. $n=10$, or $(a,q)=(2,3)$ i.e. $n=12$.

Hence $\{n : \varphi(n)=4\} = \{5,8,10,12\}$.

*Check:* $\varphi(3)=\varphi(4)=\varphi(6)=2$ ✓ and $\varphi(5)=\varphi(8)=\varphi(10)=\varphi(12)=4$ ✓, and a scan of $n\le100$ returns exactly these lists.

**20.** *Strategy: substitute $d\mapsto n/d$ in the definition of $\sigma$.*

$$\sigma(n) = \sum_{d\mid n}d = \sum_{d\mid n}\frac{n}{n/d} = n\sum_{d\mid n}\frac{1}{n/d} = n\sum_{e\mid n}\frac1e,$$

where $e = n/d$ runs over the divisors of $n$. For $n=360$:

$$\frac{\sigma(360)}{360} = \frac{1170}{360} = \frac{13}{4} = 3.25,$$

and indeed $\sum_{d\mid360}\frac1d$ over the $24$ divisors $1,2,3,4,5,6,8,9,10,12,15,18,20,24,30,36,40,45,60,72,90,120,180,360$ equals $3.25$.

*Remark.* The quantity $\sigma(n)/n = \sum_{d\mid n}1/d$ is the abundancy index; the equation $\sigma(n)/n = 2$ is the definition of perfection, and $\sigma(n)/n = 3$ (a "multiply perfect" or $3$-perfect number) holds for $120$ and $672$, among others.

**21.** *Strategy: pull the completely multiplicative factor $f(n)$ out of every term.*

No coprimality is needed — complete multiplicativity holds for all arguments. Compute:

$$\big((f\cdot g)*(f\cdot h)\big)(n) = \sum_{d\mid n}f(d)g(d)\,f\!\left(\frac nd\right)h\!\left(\frac nd\right) = \sum_{d\mid n}f(n)\,g(d)h\!\left(\frac nd\right) = f(n)\,(g*h)(n),$$

where the middle step uses $f(d)f(n/d) = f(d\cdot n/d) = f(n)$, which is exactly complete multiplicativity applied to the pair $(d, n/d)$ — **not** necessarily coprime. For merely multiplicative $f$ the step fails; take $f=\mu$, $d=2$, $n=4$: $\mu(2)\mu(2) = 1 \ne 0 = \mu(4)$.

With $f = \operatorname{id}$ (completely multiplicative, nowhere zero), $g = h = 1$:

$$\operatorname{id}*\operatorname{id} = (\operatorname{id}\cdot 1)*(\operatorname{id}\cdot 1) = \operatorname{id}\cdot(1*1) = \operatorname{id}\cdot d,$$

i.e. $\sum_{d\mid n}d\cdot\frac nd = n\,d(n)$.

*Check at $n=6$:* the left side is $1\cdot6 + 2\cdot3 + 3\cdot2 + 6\cdot1 = 6+6+6+6 = 24$, and the right side is $6\cdot d(6) = 6\cdot4 = 24$ ✓.

**22.** *Strategy: compute the convolution of $\mu\cdot\operatorname{id}$ with $\operatorname{id}$ term by term.*

$$\big((\mu\cdot\operatorname{id})*\operatorname{id}\big)(n) = \sum_{d\mid n}\mu(d)\,d\cdot\frac nd = n\sum_{d\mid n}\mu(d) = n\,\varepsilon(n) = \varepsilon(n),$$

since $\sum_{d\mid n}\mu(d) = \varepsilon(n)$ (Lemma 7.5.2) and $n\cdot\varepsilon(n) = \varepsilon(n)$ — both sides vanish for $n>1$ and equal $1$ at $n=1$. Hence $(\mu\cdot\operatorname{id})*\operatorname{id} = \varepsilon$, so $\operatorname{id}^{-1} = \mu\cdot\operatorname{id}$.

*Recursion check at $n=12$.* With $g=\operatorname{id}^{-1}$: $g(1) = 1$;

* $g(2) = -\operatorname{id}(2)g(1) = -2$;
* $g(3) = -\operatorname{id}(3)g(1) = -3$;
* $g(4) = -[\operatorname{id}(4)g(1)+\operatorname{id}(2)g(2)] = -[4 + 2(-2)] = 0$;
* $g(6) = -[\operatorname{id}(6)g(1)+\operatorname{id}(3)g(2)+\operatorname{id}(2)g(3)] = -[6-6-6] = 6$;
* $g(12) = -[\operatorname{id}(12)g(1)+\operatorname{id}(6)g(2)+\operatorname{id}(4)g(3)+\operatorname{id}(3)g(4)+\operatorname{id}(2)g(6)] = -[12-12-12+0+12] = 0$.

The formula gives $\mu(12)\cdot 12 = 0\cdot12 = 0$ ✓, because $4 \mid 12$.

*Cross-check.* $(\operatorname{id}*\operatorname{id}^{-1})(12) = 1\cdot0 + 2\cdot6 + 3\cdot0 + 4\cdot(-3) + 6\cdot(-2) + 12\cdot1 = 0+12+0-12-12+12 = 0 = \varepsilon(12)$ ✓.

**23.** *Strategy: Möbius inversion applied to $\sum_{d\mid n}\varphi(d)=n$.*

Let $g(n) = \sum_{d\mid n}\varphi(d) = n$ (Corollary 7.4.4). Theorem 7.5.3 gives

$$\varphi(n) = \sum_{d\mid n}\mu(d)\,g\!\left(\frac nd\right) = \sum_{d\mid n}\mu(d)\cdot\frac nd = \sum_{d\mid n}\mu(d)\left\lfloor\frac nd\right\rfloor,$$

the floor being redundant because $d \mid n$ makes $n/d$ an integer.

*Check at $n=100$.* The divisors of $100$ are $1,2,4,5,10,20,25,50,100$, and $\mu$ of them is $1,-1,0,-1,1,0,0,0,0$. Hence

$$\sum_{d\mid100}\mu(d)\frac{100}{d} = 100 - 50 + 0 - 20 + 10 + 0+0+0+0 = 40 = \varphi(100). ✓$$

**24.** *Strategy: $d = 1*1$, and the inverse of a product is the product of the inverses.*

Since $1$ is invertible with $1^{-1} = \mu$ (Lemma 7.5.2), and since in a commutative ring $(f*g)*(f^{-1}*g^{-1}) = (f*f^{-1})*(g*g^{-1}) = \varepsilon$ by associativity and commutativity (so $(f*g)^{-1} = f^{-1}*g^{-1}$),

$$d^{-1} = (1*1)^{-1} = \mu*\mu.$$

*Values at prime powers.* Since $\mu*\mu$ is multiplicative (Corollary 7.2.2), compute at $p^{a}$:

* $a=0$: $(\mu*\mu)(1) = 1$;
* $a=1$: $\mu(1)\mu(p)+\mu(p)\mu(1) = -1-1 = -2$;
* $a=2$: divisors $1,p,p^{2}$ give $\mu(1)\mu(p^{2})+\mu(p)\mu(p)+\mu(p^{2})\mu(1) = 0+1+0 = 1$;
* $a=3$: the pairs $(d,p^{3}/d)$ are $(1,p^{3}),(p,p^{2}),(p^{2},p),(p^{3},1)$, and in each pair at least one entry has $\mu = 0$; so the value is $0$;
* $a \ge 3$: the same argument — one of $d$, $p^{a}/d$ is divisible by $p^{2}$ — gives $0$.

So $\mu*\mu$ takes the values $1,-2,1,0,0,\dots$ on $1,p,p^{2},p^{3},p^{4},\dots$.

*At squarefree $n$ with $r = \omega(n)$ primes:* $d$ runs over the $2^{r}$ subsets and $\mu(d)\mu(n/d) = (-1)^{r}$ in every term, so $(\mu*\mu)(n) = (-1)^{r}2^{r} = \mu(n)\,2^{\omega(n)}$.

*Value at $12$.* $12 = 2^{2}\cdot3$, so $d^{-1}(12) = (\mu*\mu)(4)\cdot(\mu*\mu)(3) = 1\cdot(-2) = -2$.

*Verification of $(d*d^{-1})(12) = \varepsilon(12)$.* With $(\mu*\mu)(1)=1$, $(2) = -2$, $(3)=-2$, $(4)=1$, $(6)=4$, $(12)=-2$:

$$\sum_{d\mid12}d(d)\,(\mu*\mu)\!\left(\frac{12}{d}\right) = 1(-2)+2(4)+2(1)+3(-2)+4(-2)+6(1) = -2+8+2-6-8+6 = 0 = \varepsilon(12). ✓$$

## Advanced

**25.** *Strategy: count lattice points under the hyperbola $dm \le N$ in two ways.*

Let $S = \{(d,m)\in\mathbb{N}^{2} : dm\le N\}$. Grouping by $n = dm$,

$$\lvert S\rvert = \sum_{n\le N}\#\{(d,m) : dm = n\} = \sum_{n\le N}d(n).$$

Grouping by $d$ instead, $\lvert S\rvert = \sum_{d\le N}\lfloor N/d\rfloor$ — the same number, computed differently.

Now define

$$A = \{(d,m)\in S : d\le\sqrt N\}, \qquad B = \{(d,m)\in S : m\le\sqrt N\}.$$

*Claim: $A\cup B = S$.* If $(d,m)\in S$ and $(d,m)\notin A$, then $d > \sqrt N$. If also $(d,m)\notin B$ then $m > \sqrt N$, and then $dm > \sqrt N\cdot\sqrt N = N$, contradicting $dm \le N$ (note $dm$ is an integer, so $dm\le N$ and $dm > N$ are incompatible). Hence every point is in $A$ or in $B$.

Counting: $A$ consists of all pairs with $d\le\sqrt N$ and $m \le N/d$, so

$$\lvert A\rvert = \sum_{d\le\sqrt N}\left\lfloor\frac Nd\right\rfloor.$$

The map $(d,m)\mapsto(m,d)$ is a bijection $A\to B$ (it preserves $dm$ and swaps the two constraints), so $\lvert B\rvert = \lvert A\rvert$. Finally

$$A\cap B = \{(d,m) : d\le\sqrt N,\ m\le\sqrt N\}$$

— the constraint $dm\le N$ is then automatic — so $\lvert A\cap B\rvert = \lfloor\sqrt N\rfloor^{2}$.

Inclusion–exclusion gives

$$\sum_{n\le N}d(n) = \lvert S\rvert = \lvert A\rvert+\lvert B\rvert-\lvert A\cap B\rvert = 2\sum_{d\le\sqrt N}\left\lfloor\frac Nd\right\rfloor - \left\lfloor\sqrt N\right\rfloor^{2}. \blacksquare$$

*At $N=50$:* $\lfloor\sqrt{50}\rfloor = 7$ and

$$\sum_{k=1}^{7}\left\lfloor\frac{50}{k}\right\rfloor = 50+25+16+12+10+8+7 = 128,$$

so the formula gives $2\cdot128 - 49 = 256-49 = 207$. Direct enumeration of $d(n)$ for $n\le50$ gives $207$ ✓.

**26.** *Strategy: write the squarefree indicator as a divisor sum, then swap the order of summation.*

**Lemma.** $\mu^{2}(n) = \sum_{d^{2}\mid n}\mu(d)$.

*Proof.* Both sides are multiplicative in $n$, so by Corollary 7.1.2 it suffices to check prime powers. For $n = p^{a}$ the divisors $d^{2}$ of $p^{a}$ come from $d = 1$ (always) and $d = p$ (only if $a\ge2$). So the right side is $1$ for $a = 0,1$ and $1-1 = 0$ for $a\ge2$, which is exactly $\mu^{2}(p^{a})$. $\blacksquare$

Now

$$\sum_{n\le x}\mu^{2}(n) = \sum_{n\le x}\sum_{d^{2}\mid n}\mu(d) = \sum_{d\le\sqrt x}\mu(d)\left\lfloor\frac{x}{d^{2}}\right\rfloor,$$

interchanging the sums: the pair $(n,d)$ satisfies $d^{2}\mid n\le x$, hence $d\le\sqrt x$, and for each such $d$ there are exactly $\lfloor x/d^{2}\rfloor$ multiples of $d^{2}$ up to $x$.

Write $\lfloor x/d^{2}\rfloor = x/d^{2} + O(1)$. Then

$$\sum_{n\le x}\mu^{2}(n) = x\sum_{d\le\sqrt x}\frac{\mu(d)}{d^{2}} + O\!\left(\sqrt x\right) = x\left(\frac{6}{\pi^{2}} + O\!\left(\frac{1}{\sqrt x}\right)\right) + O(\sqrt x) = \frac{6}{\pi^{2}}x + O(\sqrt x),$$

where the tail estimate is $\left\lvert\sum_{d>\sqrt x}\mu(d)/d^{2}\right\rvert \le \sum_{d>\sqrt x}1/d^{2} \le 1/\sqrt x$, and $x\cdot O(1/\sqrt x) = O(\sqrt x)$. $\blacksquare$

*At $x=100$:* $\frac{6}{\pi^{2}}\cdot100 = 60.79$, while the exact count of squarefree $n\le100$ is $61$ — an error of $0.21$, well inside $O(\sqrt x) = 10$ ✓.

**27.** *Strategy: look at the smallest index where each factor is nonzero.*

Let $f,g\ne0$, and let $m$ be the least $n$ with $f(n)\ne0$, $l$ the least $n$ with $g(n)\ne0$. In

$$(f*g)(ml) = \sum_{d\mid ml}f(d)\,g\!\left(\frac{ml}{d}\right)$$

consider any divisor $d$ of $ml$. If $d < m$ then $f(d) = 0$; if $d > m$ then $ml/d < l$, so $g(ml/d) = 0$. Hence only $d = m$ survives, and

$$(f*g)(ml) = f(m)g(l) \ne 0,$$

since a product of nonzero complex numbers is nonzero. Therefore $f*g \ne 0$: the ring has no zero divisors. Equivalently (contrapositive), $f*g = 0$ implies $f=0$ or $g=0$.

*Contrast.* In the ring of all functions $\mathbb{N}\to\mathbb{Z}$ with **pointwise** multiplication, take

$$f(n) = \begin{cases}1 & n \text{ even}\\ 0 & n\text{ odd}\end{cases}, \qquad g(n) = \begin{cases}0 & n \text{ even}\\ 1 & n\text{ odd}\end{cases}.$$

Both are nonzero, but $(fg)(n) = 0$ for every $n$. So the absence of zero divisors is a property of the convolution product, not of the underlying set of functions.

**28.** *Strategy: apply Theorem 7.1.1 to $mn$, which does not require $m$ and $n$ to be coprime.*

Write $m = \prod_p p^{a_p}$ and $n = \prod_p p^{b_p}$ (finitely many nonzero exponents). Then $mn = \prod_p p^{a_p+b_p}$, and Theorem 7.1.1 applied to the factorisation of $mn$ gives

$$f(mn) = \prod_p f\!\left(p^{a_p+b_p}\right) = \prod_p f(p)^{a_p+b_p} = \left(\prod_p f(p)^{a_p}\right)\left(\prod_p f(p)^{b_p}\right) = f(m)f(n),$$

using the hypothesis $f(p^{c}) = f(p)^{c}$ twice and the laws of exponents. Hence $f$ is completely multiplicative. $\blacksquare$

*Examples.* $d$ fails the hypothesis ($d(4) = 3 \ne d(2)^{2}$) and is not completely multiplicative; $\mu$ fails it too ($\mu(4) = 0 \ne 1$). The completely multiplicative functions are exactly the multiplicative functions whose prime-power values are powers of the prime value.

**29.** *Strategy: invert the factorisation $\varphi = \mu*\operatorname{id}$.*

Since $\mu$ and $\operatorname{id}$ are units ($\mu(1) = 1 \ne 0$, $\operatorname{id}(1)=1$), their product $\varphi$ is a unit, and by Exercise 22 and $\mu^{-1} = 1$,

$$\varphi^{-1} = \mu^{-1}*\operatorname{id}^{-1} = 1*(\mu\cdot\operatorname{id}),$$

so

$$\varphi^{-1}(n) = \sum_{d\mid n}\mu(d)\,d.$$

*Value at $n=30$ from the formula.* The divisors of $30 = 2\cdot3\cdot5$ are $1,2,3,5,6,10,15,30$, all squarefree, with $\mu = 1,-1,-1,-1,1,1,1,-1$. Then

$$\varphi^{-1}(30) = 1 - 2 - 3 - 5 + 6 + 10 + 15 - 30 = -8.$$

*From the recursion.* With $g=\varphi^{-1}$: $g(1)=1$, $g(2) = -1$, $g(3) = -2$, $g(5) = -4$, and

$$g(6) = -\big[\varphi(6)g(1)+\varphi(3)g(2)+\varphi(2)g(3)\big] = -[2-2-2] = 2,$$
$$g(10) = -\big[\varphi(10)g(1)+\varphi(5)g(2)+\varphi(2)g(5)\big] = -[4-4-4] = 4,$$
$$g(15) = -\big[\varphi(15)g(1)+\varphi(5)g(3)+\varphi(3)g(5)\big] = -[8-8-8] = 8,$$
$$g(30) = -\big[\varphi(30)g(1)+\varphi(15)g(2)+\varphi(10)g(3)+\varphi(6)g(5)+\varphi(5)g(6)+\varphi(3)g(10)+\varphi(2)g(15)\big]$$
$$= -\big[8 - 8 - 8 - 8 + 8 + 8 + 8\big] = -8,$$

which agrees with the formula ✓.

**30.** *Strategy: split $N = 2^{k-1}m$ with $m$ odd, use multiplicativity of $\sigma$, and compare sizes.*

Let $N$ be even and perfect, so $\sigma(N) = 2N$. Write $N = 2^{k-1}m$ with $k\ge2$ and $m$ odd — possible because $N$ is even, and unique because the exponent of $2$ in $N$ is determined.

(i) Since $\gcd(2^{k-1},m)=1$, multiplicativity and $\sigma(2^{k-1}) = 2^{k}-1$ give

$$2^{k}m = 2N = \sigma(N) = (2^{k}-1)\,\sigma(m). \tag{$*$}$$

Now $\gcd(2^{k}-1,2^{k}) = 1$ and $2^{k}-1$ divides the left side $2^{k}m$; being coprime to $2^{k}$, it must divide $m$. So $m = (2^{k}-1)M$ for some integer $M \ge 1$.

(ii) Substituting $m = (2^k-1)M$ into $(*)$:

$$2^{k}(2^{k}-1)M = (2^{k}-1)\sigma(m) \implies \sigma(m) = 2^{k}M.$$

If $M > 1$, then $1$, $M$ and $m = (2^{k}-1)M$ are three **distinct** divisors of $m$ (distinct because $M>1$ and $2^{k}-1\ge3$), so

$$\sigma(m)\ge 1+M+m = 1 + M + (2^{k}-1)M = 1+2^{k}M > 2^{k}M = \sigma(m),$$

a contradiction. Hence $M = 1$, $m = 2^{k}-1$, and $\sigma(m) = 2^{k} = m+1$. Since $\sigma(m) = m+1$ means the only divisors of $m$ are $1$ and $m$, $m$ is prime.

(iii) If $k = ab$ with $a,b\ge2$, then $2^{a}-1$ divides $2^{ab}-1$ (because $x-1 \mid x^{b}-1$ at $x = 2^{a}$) and satisfies $1 < 2^{a}-1 < 2^{k}-1 = m$, contradicting the primality of $m$. Hence $k$ is prime. Putting $p = k$: $N = 2^{p-1}(2^{p}-1)$ with $2^{p}-1$ prime. $\blacksquare$

**31.** *Strategy: $h(n)=\sum_{d\mid n}\mu(d)\sigma(d)$ is multiplicative, so compute it at prime powers.*

$\mu\cdot\sigma$ is multiplicative (a product of two multiplicative functions) with value $1$ at $1$, so by Theorem 7.2.1 the function $h = (\mu\cdot\sigma)*1$ is multiplicative. At a prime power,

$$h(p^{a}) = \sum_{j=0}^{a}\mu(p^{j})\sigma(p^{j}) = 1 - \sigma(p) + 0 + \cdots + 0 = 1 - (1+p) = -p,$$

since $\mu(p^{j}) = 0$ for $j\ge2$ and $\sigma(p) = 1+p$. Therefore, for $n = \prod_{i=1}^{r}p_i^{a_i}$ with $r = \omega(n)$,

$$h(n) = \prod_{i=1}^{r}(-p_i) = (-1)^{r}\prod_{i=1}^{r}p_i = (-1)^{\omega(n)}\operatorname{rad}(n). \blacksquare$$

*Check at $n=12$:* $12 = 2^{2}\cdot3$ has $\omega = 2$ and $\operatorname{rad} = 6$, so the formula predicts $6$. Directly: the divisors $1,2,3,4,6,12$ have $\mu = 1,-1,-1,0,1,0$ and $\sigma = 1,3,4,7,12,28$, so the sum is $1 - 3 - 4 + 0 + 12 + 0 = 6$ ✓.

*Check at $n=720$:* $\omega = 3$ and $\operatorname{rad}(720) = 2\cdot3\cdot5 = 30$, so the formula predicts $-30$; direct enumeration of $\sum_{d\mid720}\mu(d)\sigma(d)$ gives $-30$ ✓.

## Challenge

**32.** *Strategy: $\varphi = \mu*\operatorname{id}$ turns the sum into a sum of triangular numbers, which is then compared with $\frac{x^{2}}{2}$ times a convergent series.*

*Step 1: rewrite the sum.* By Example 7.5.4, $\varphi(n) = \sum_{d\mid n}\mu(d)\frac nd$, so

$$\sum_{n\le x}\varphi(n) = \sum_{n\le x}\sum_{d\mid n}\mu(d)\frac nd = \sum_{d\le x}\mu(d)\sum_{m\le x/d}m = \sum_{d\le x}\mu(d)\,T\!\left(\left\lfloor\frac xd\right\rfloor\right),$$

where $T(y) = \frac{y(y+1)}{2}$; the inner sum runs over $m = n/d \le x/d$, i.e. up to $\lfloor x/d\rfloor$.

*Step 2: expand $T$.* For $y \ge 0$, $T(y) = \frac{y^{2}}{2} + \frac y2$, so

$$\sum_{n\le x}\varphi(n) = \frac12\sum_{d\le x}\mu(d)\left\lfloor\frac xd\right\rfloor^{2} + \frac12\sum_{d\le x}\mu(d)\left\lfloor\frac xd\right\rfloor. \tag{1}$$

*Step 3: bound the second term.* $\left\lvert\sum_{d\le x}\mu(d)\lfloor x/d\rfloor\right\rvert \le \sum_{d\le x}\lfloor x/d\rfloor \le x\sum_{d\le x}\frac1d = O(x\log x)$.

*Step 4: expand the first term.* Write $\lfloor x/d\rfloor = x/d + O(1)$, so $\lfloor x/d\rfloor^{2} = x^{2}/d^{2} + O(x/d) + O(1)$. Then

$$\sum_{d\le x}\mu(d)\left\lfloor\frac xd\right\rfloor^{2} = x^{2}\sum_{d\le x}\frac{\mu(d)}{d^{2}} + O\!\left(x\sum_{d\le x}\frac1d\right) + O(x) = x^{2}\sum_{d\le x}\frac{\mu(d)}{d^{2}} + O(x\log x),$$

using $\left\lvert\mu(d)\right\rvert\le1$.

*Step 5: the series.* $\sum_{d\le x}\mu(d)/d^{2} = \sum_{d\ge1}\mu(d)/d^{2} + O\!\left(\sum_{d>x}1/d^{2}\right) = \frac{6}{\pi^{2}} + O(1/x)$, because the tail of a series with terms bounded by $1/d^{2}$ is $O(1/x)$. Hence

$$\sum_{d\le x}\mu(d)\left\lfloor\frac xd\right\rfloor^{2} = \frac{6}{\pi^{2}}x^{2} + O(x) + O(x\log x) = \frac{6}{\pi^{2}}x^{2} + O(x\log x).$$

*Step 6: conclude.* Substituting into (1),

$$\sum_{n\le x}\varphi(n) = \frac12\cdot\frac{6}{\pi^{2}}x^{2} + O(x\log x) = \frac{3}{\pi^{2}}x^{2} + O(x\log x). \blacksquare$$

*Where $6/\pi^{2}$ comes from.* $\sum_{d\ge1}\mu(d)/d^{2} = \prod_p\left(1-\frac{1}{p^{2}}\right) = \frac{1}{\zeta(2)} = \frac{6}{\pi^{2}}$ by the Euler product (Theorem 7.9.2) and Euler's evaluation $\zeta(2)=\pi^{2}/6$ (Theorem 7.9.4). The constant $\frac{3}{\pi^{2}}\approx 0.30396$ is also the density of coprime pairs, and indeed $\sum_{n\le x}\varphi(n)$ counts the lattice points in $[1,x]^{2}$ visible from the origin (each primitive vector $(a,b)$ with $\gcd(a,b)=1$ contributes, up to scaling, exactly one point visible along its ray).

**33.** *Strategy: prove multiplicativity of convolution first, then define the inverse on prime powers and check.*

**Step 1.** If $f,g$ are multiplicative then $f*g$ is multiplicative (Corollary 7.2.2). The proof is the divisor-pair bijection: for $\gcd(m,n)=1$, every $d \mid mn$ is uniquely $d_1d_2$ with $d_1\mid m$, $d_2\mid n$; then $f(d) = f(d_1)f(d_2)$ and $g(mn/d) = g(m/d_1)g(n/d_2)$, and the double sum factorises.

**Step 2.** Let $f$ be multiplicative with $f(1)=1$, and let $g = f^{-1}$ (which exists since $f(1)\ne0$). Define $h$ by $h(1)=1$ and, for $a\ge1$,

$$h(p^{a}) = -\frac{1}{f(1)}\sum_{\substack{d\mid p^{a}\\ d<p^{a}}}f\!\left(\frac{p^{a}}{d}\right)h(d),$$

then extend $h$ multiplicatively: $h\!\left(\prod p_i^{a_i}\right) = \prod h(p_i^{a_i})$.

**Step 3.** For each prime $p$ and $a\ge0$ the recursion defining $f^{-1}$ at $p^{a}$ involves only the values $f(p^{j})$, $f^{-1}(p^{j})$ with $j\le a$, because every divisor of $p^{a}$ is a power of $p$. Comparing with the recursion defining $h$, induction on $a$ gives $h(p^{a}) = f^{-1}(p^{a})$ for all $p,a$.

**Step 4.** By Step 1, $f*h$ is multiplicative (both factors are). At a prime power,

$$(f*h)(p^{a}) = \sum_{j=0}^{a}f(p^{a-j})h(p^{j}) = (f*f^{-1})(p^{a}) = \varepsilon(p^{a}),$$

by Step 3 and the definition of the inverse. A multiplicative function is determined by its prime-power values (Theorem 7.1.1), and $\varepsilon$ is multiplicative with $\varepsilon(p^{a}) = 0$ for $a\ge1$; hence $f*h = \varepsilon$.

**Step 5.** So $h$ is an inverse of $f$; by uniqueness (Theorem 7.6.2) $h = f^{-1}$, which is multiplicative by construction. $\blacksquare$

*Why there is no circularity.* Step 1 uses only the multiplicativity of $f$ and $h$ — a property of the two functions, not of the inverse operation. Step 4 concludes $f*h = \varepsilon$ from prime-power data, which needs $f*h$ multiplicative (Step 1) and nothing more. Only after $f*h = \varepsilon$ is established do we invoke uniqueness to identify $h$ with $f^{-1}$. Nowhere do we assume that $f^{-1}$ is multiplicative before proving it.

**34.** *Strategy: compare the parity of $\sigma(n)$ with the parity of $2n$.*

Suppose $n$ is perfect and $n = m^{2}$ is a square. Then $\sigma(n) = 2n$, which is **even**.

But by Corollary 7.3.5, $\sigma(n)$ is odd whenever $n$ is a square: all exponents in $m^{2}$ are even, so every $\sigma(p^{a})$ is odd (for $p=2$ always, for odd $p$ because $a$ is even), and a product of odd numbers is odd. Hence $\sigma(n)$ is odd.

An integer cannot be both even and odd, a contradiction. Therefore no perfect number is a square. $\blacksquare$

*Remark.* The argument uses only parity. It shows in particular that a *hypothetical* odd perfect number cannot be a square either — consistent with Euler's form $p^{a}m^{2}$ of Exercise 36, where $a$ is odd.

**35.** *Strategy: compute $2^{p-1}$ and $2^{p}-1$ modulo $10$, splitting on $p \bmod 4$.*

The perfect number is $N = 2^{p-1}(2^{p}-1)$ with $p$ prime and $2^{p}-1$ prime (Theorem 7.8.1).

*Case $p=2$:* $N = 2\cdot3 = 6$, which ends in $6$.

*Case $p$ odd.* The powers of $2$ modulo $10$ satisfy $2^{1}\equiv2$, $2^{2}\equiv4$, $2^{3}\equiv8$, $2^{4}\equiv6$, and then repeat with period $4$ (because $2^{4} = 16 \equiv 6$ and $6\cdot2 = 12\equiv 2$, restarting the cycle). So for $j \equiv 1,2,3,0 \pmod 4$ the value $2^{j} \bmod 10$ is $2,4,8,6$ respectively.

* $p \equiv 1 \pmod 4$: then $p-1\equiv0 \pmod 4$, so $2^{p-1}\equiv6$; and $p \equiv 1$ gives $2^{p}\equiv2$, so $2^{p}-1\equiv1 \pmod{10}$. Hence $N \equiv 6\cdot1 = 6 \pmod{10}$.
* $p \equiv 3 \pmod 4$: then $p-1\equiv2 \pmod 4$, so $2^{p-1}\equiv4$; and $2^{p}\equiv8$, so $2^{p}-1\equiv7 \pmod{10}$. Hence $N \equiv 4\cdot7 = 28 \equiv 8 \pmod{10}$.

Either way $N$ ends in $6$ or $8$. $\blacksquare$

*Check.* $6$ ends in $6$; $28$ in $8$ ($p=3\equiv3$); $496$ in $6$ ($p=5\equiv1$); $8128$ in $8$ ($p=7\equiv3$); $33550336$ in $6$ ($p=13\equiv1$); $8589869056$ in $6$ ($p=17\equiv1$) ✓.

**36.** *Strategy: use $\sigma(n)=2n$, count the even factors among the $\sigma(p^{a})$, then compute modulo $4$.*

Let $n$ be odd and perfect, $n = \prod_{i=1}^{r}p_i^{a_i}$ with all $p_i$ odd. Then

$$\sigma(n) = \prod_{i=1}^{r}\sigma(p_i^{a_i}) = 2n.$$

*Step 1: exactly one factor is even, and it is $\equiv2 \pmod 4$.* Since $n$ is odd, $2n \equiv 2 \pmod 4$. The factors $\sigma(p_i^{a_i})$ are positive integers, so a product is $\equiv 2 \pmod 4$ iff exactly one factor is even and that factor is $\equiv 2 \pmod 4$, all other factors being odd.

*Step 2: even factors correspond to odd exponents.* For odd $p$, $\sigma(p^{a}) = 1+p+\cdots+p^{a}$ is a sum of $a+1$ odd terms, hence even iff $a+1$ is even, i.e. iff $a$ is odd.

So there is a unique prime $p$ with exponent $a$ odd, and all other exponents are even. Therefore

$$n = p^{a}\,m^{2}, \qquad m = \prod_{q \ne p}q^{a_q/2},$$

and $\gcd(p,m) = 1$ because $p$ appears in $n$ with exponent $a$ and in $m^{2}$ with exponent $0$.

*Step 3: $p \equiv 1 \pmod 4$.* Since $a$ is odd, $a+1$ is even and the terms of $\sigma(p^{a})$ can be grouped in pairs:

$$\sigma(p^{a}) = 1+p+p^{2}+\cdots+p^{a} = (1+p)\left(1+p^{2}+p^{4}+\cdots+p^{a-1}\right).$$

If $p \equiv 3 \pmod 4$ then $1+p \equiv 0 \pmod 4$, so $\sigma(p^{a}) \equiv 0 \pmod 4$, contradicting $\sigma(p^{a}) \equiv 2 \pmod 4$ from Step 1. Hence $p \equiv 1 \pmod 4$.

*Step 4: $a \equiv 1 \pmod 4$.* With $p\equiv1\pmod 4$ every $p^{j}\equiv1$, so $\sigma(p^{a}) = \sum_{j=0}^{a}p^{j} \equiv a+1 \pmod 4$. Step 1 gives $a+1 \equiv 2 \pmod 4$, i.e. $a \equiv 1 \pmod 4$. $\blacksquare$

*Where oddness is used.* (i) To conclude $2n \equiv 2 \pmod 4$ — if $n$ were even then $2n$ would be divisible by $4$ and the parity bookkeeping of Step 1 would collapse. (ii) To know that every $p_i$ is odd, which makes each $\sigma(p_i^{a_i})$ odd or even according to the parity of $a_i+1$.

*Why this does not construct an odd perfect number.* The argument proves a **necessary** condition: any odd perfect number must have the Euler form $p^{a}m^{2}$ with $p \equiv a \equiv 1 \pmod 4$. It says nothing about existence. For example $3^{1}\cdot 5^{2} = 75$ has the shape $p^{a}m^{2}$ with $a=1$, but $p = 3 \equiv 3$, so it fails even the congruence condition; and $5^{1}\cdot3^{2} = 45$ has $p = 5 \equiv 1$, $a = 1 \equiv 1$, yet $\sigma(45) = 78 \ne 90$, so $45$ is not perfect. The condition is a filter, not a construction. It is not known whether any odd perfect number exists; the best known computational result is that none is below $10^{1500}$.

