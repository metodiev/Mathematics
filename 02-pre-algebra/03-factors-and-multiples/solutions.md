# Factors, Multiples, GCD and LCM — Solutions

> [Tutorial](README.md) · [Exercises](exercises.md)

Computational solutions show the method, not only the answer. Proof solutions state the definitions and properties used; a proof that only checks examples is not a proof.

## Beginner

**1.** Pair the divisors: $1\cdot36$, $2\cdot18$, $3\cdot12$, $4\cdot9$, $6\cdot6$. The positive divisors are
$$1,2,3,4,6,9,12,18,36.$$
There are nine of them. Pairing is efficient because each divisor $d$ below $\sqrt{36}=6$ has a partner $36/d$ above it, with $6$ paired with itself.

**2.** Multiply $7$ by $1,2,3,4,5$:
$$7,14,21,28,35.$$

**3.** The digit sum is $4+5+7+2=18$.

* By $3$: $18$ is divisible by $3$, so $4{,}572$ is.
* By $9$: $18$ is divisible by $9$, so $4{,}572$ is.
* By $6$: the number is even (last digit $2$) and divisible by $3$, and $\gcd(2,3)=1$, so it is divisible by $6$.

Check: $4{,}572=6\cdot762=9\cdot508$.

**4.** The last digit is $5$ and the digit sum is $7+2+1+5=15$.

* By $5$: yes, last digit $5$.
* By $10$: no, last digit is not $0$.
* By $3$: yes, $15$ is divisible by $3$.
* By $9$: no, $15$ is not divisible by $9$.

Check: $7{,}215=5\cdot1{,}443=3\cdot2{,}405$, and $2{,}405$ has digit sum $11$, so it is not divisible by $3$.

**5.** Factor step by step:
$$84=4\cdot21=2^2\cdot3\cdot7.$$
All three primes are distinct, so this is the canonical form.

**6.**
$$180=18\cdot10=(2\cdot3^2)(2\cdot5)=2^2\cdot3^2\cdot5.$$

**7.** $51=3\cdot17$, composite. $91=7\cdot13$, composite (a common trap: $91$ has no divisor $2,3,5$, but $7$ works). $97$ is prime: test primes up to $\sqrt{97}<10$, namely $2,3,5,7$; $97$ is odd, its digit sum $16$ is not divisible by $3$, it does not end in $0$ or $5$, and $7\cdot13=91<97<7\cdot14=98$.

**8.** Factor:
$$18=2\cdot3^2,\qquad 24=2^3\cdot3.$$
Take the minimum exponent of each common prime:
$$\gcd(18,24)=2^1\cdot3^1=6.$$

**9.** $6=2\cdot3$ and $8=2^3$. Take the maximum exponent of each prime:
$$\operatorname{lcm}(6,8)=2^3\cdot3=24.$$

**10.** $35=5\cdot7$ and $50=2\cdot5^2$.
$$\gcd(35,50)=5,\qquad \operatorname{lcm}(35,50)=2\cdot5^2\cdot7=350.$$
Check with Property 7: $5\cdot350=1{,}750=35\cdot50$.

**11.** $14=2\cdot7$ and $25=5^2$. They share no prime factor, so their only common positive divisor is $1$:
$$\gcd(14,25)=1.$$
They are coprime.

## Intermediate

**12.**
$$1{,}000=10^3=(2\cdot5)^3=2^3\cdot5^3.$$
$$1{,}001=7\cdot143=7\cdot11\cdot13.$$
The second is a standard counterexample to "looks prime": it is just above a round power of $10$ and has three distinct prime factors.

**13.** Write both numbers with the same primes displayed:
$$2^3\cdot3^2\cdot5^1,\qquad 2^2\cdot3^5\cdot5^0.$$
Minimum exponents: $2^2\cdot3^2\cdot5^0=4\cdot9=36$. Maximum exponents: $2^3\cdot3^5\cdot5^1=8\cdot243\cdot5=9{,}720$. Therefore
$$\gcd=36,\qquad \operatorname{lcm}=9{,}720.$$
Check: $36\cdot9{,}720=349{,}920$ and $(2^3\cdot3^2\cdot5)(2^2\cdot3^5)=2^5\cdot3^7\cdot5=32\cdot2{,}187\cdot5=349{,}920$.

**14.** Apply the Euclidean algorithm:
$$\begin{aligned}
1{,}078&=1\cdot546+532\\
546&=1\cdot532+14\\
532&=38\cdot14+0
\end{aligned}$$
The last nonzero remainder is $14$, so $\gcd(1{,}078,546)=14$. Check by factorization: $546=2\cdot3\cdot7\cdot13$ and $1{,}078=2\cdot7\cdot7\cdot11=2\cdot7^2\cdot11$; the common part is $2\cdot7=14$.

**15.** Repeated division:
$$\begin{aligned}
13&=1\cdot8+5\\
8&=1\cdot5+3\\
5&=1\cdot3+2\\
3&=1\cdot2+1\\
2&=2\cdot1+0
\end{aligned}$$
The last nonzero remainder is $1$. Since $13$ is prime and does not divide $8$, the answer $1$ is expected.

**16.** Factor each:
$$12=2^2\cdot3,\qquad 18=2\cdot3^2,\qquad 30=2\cdot3\cdot5.$$
The lcm takes the maximum exponent of every prime:
$$\operatorname{lcm}(12,18,30)=2^2\cdot3^2\cdot5=180.$$
Check: $180/12=15$, $180/18=10$, $180/30=6$.

**17.** The side of the largest square tile must divide both $48$ and $60$; the largest such side is
$$\gcd(48,60)=12\text{ cm}.$$
Along the $48$ cm side there are $48/12=4$ tiles and along the $60$ cm side $60/12=5$ tiles, so the number of tiles is
$$4\cdot5=20.$$

**18.** The common departure times are common multiples of $15$ and $20$:
$$\operatorname{lcm}(15,20)=60.$$
They next leave together $60$ minutes after 8:00, at 9:00. (Factor check: $15=3\cdot5$, $20=2^2\cdot5$, lcm $=2^2\cdot3\cdot5=60$.)

**19.** Compute the gcd:
$$\begin{aligned}
126&=1\cdot84+42\\
84&=2\cdot42+0
\end{aligned}$$
so $\gcd(84,126)=42$. Divide both parts:
$$\dfrac{84}{126}=\dfrac{84/42}{126/42}=\dfrac{2}{3}.$$
Because $\gcd(2,3)=1$, the fraction is in lowest terms.

**20.** The least common denominator is $\operatorname{lcm}(12,8)=24$:
$$\dfrac{5}{12}=\dfrac{10}{24},\qquad \dfrac{3}{8}=\dfrac{9}{24},$$
so
$$\dfrac{5}{12}+\dfrac{3}{8}=\dfrac{10}{24}+\dfrac{9}{24}=\dfrac{19}{24}.$$
Since $19$ is prime and does not divide $24$, the result is in lowest terms.

**21.** Digit sum: $4+9+1+7=21$.

* By $3$: $21$ is divisible by $3$, so yes.
* By $9$: $21$ is not divisible by $9$, so no.
* By $11$: alternating sum from the units digit, $7-1+9-4=11$, which is divisible by $11$, so yes.

Check: $4{,}917=3\cdot1{,}639=11\cdot447$.

## Advanced

**22.** Let $n$ be a positive integer with decimal digits $d_0,d_1,\dots,d_k$, so that
$$n=d_0+d_1\cdot10+d_2\cdot10^2+\cdots+d_k10^k=\sum_{i=0}^k d_i10^i.$$
Subtract the digit sum:
$$n-\sum_{i=0}^k d_i=\sum_{i=0}^k d_i(10^i-1).$$
For every $i\ge1$,
$$10^i-1=(10-1)(10^{i-1}+10^{i-2}+\cdots+1)=9(10^{i-1}+\cdots+1),$$
which is divisible by $9$; for $i=0$ the term is $0$, also divisible by $9$. Hence $9$ divides $n-\sum d_i$, which means $n$ and its digit sum differ by a multiple of $9$. Therefore
$$9\mid n\iff 9\mid\sum d_i.$$
The same argument with $3$ in place of $9$ (since $3\mid9$) proves the rule for $3$.

**23.** Write $n=100q+r$, where $r$ is the number formed by the last two digits, so $0\le r<100$. Since
$$100=4\cdot25,$$
$4\mid100q$ for every $q$. Therefore
$$n\equiv r\pmod4,$$
so $4\mid n$ exactly when $4\mid r$. (If $n$ has fewer than two digits, take $q=0$ and $r=n$.) Example: $4{,}572=100\cdot45+72$, and $72=4\cdot18$, so $4\mid4{,}572$.

**24.** Let $a=bq+r$ with $r=a-qb$. We show that the common divisors of $a$ and $b$ are exactly the common divisors of $b$ and $r$.

If $d\mid a$ and $d\mid b$, then $d\mid(a-qb)=r$, so $d$ is a common divisor of $b$ and $r$.

If $d\mid b$ and $d\mid r$, then $d\mid(qb+r)=a$, so $d$ is a common divisor of $a$ and $b$.

The two sets of common divisors are equal, so their greatest elements are equal:
$$\gcd(a,b)=\gcd(b,r)=\gcd(b,a-qb).$$
(The argument works for any integer $q$, and signs do not matter because $d\mid x\iff d\mid(-x)$.)

In the Euclidean algorithm one takes $q$ to be the quotient and $r$ the remainder with $0\le r<b$. Each step replaces $(a,b)$ by $(b,r)$ without changing the gcd. The remainders strictly decrease and are non-negative, so the process reaches $r=0$; then $\gcd(b,0)=b$, the last nonzero remainder. Hence the algorithm is correct and terminates.

**25.** Let $g=\gcd(a,b)$ and write
$$a=gA,\qquad b=gB.$$
Then $\gcd(A,B)=1$: any common divisor of $A$ and $B$ would multiply by $g$ to give a common divisor of $a$ and $b$ larger than $g$.

The number $gAB$ is a common multiple, since $gAB=aB=bA$. Now let $m$ be any common multiple, so $m=ak=bl$ for integers $k,l$. Substituting,
$$gAk=gBl\implies Ak=Bl.$$
Since $A\mid Bl$ and $\gcd(A,B)=1$, we get $A\mid l$: indeed, by Bézout there are integers $x,y$ with $Ax+By=1$, and multiplying by $l$ gives
$$l=A(lx)+B(ly),$$
where $A$ divides both terms ($A\mid Bl$ by assumption). Write $l=Am'$. Then
$$m=gBl=gBAm'=gABm'\ge gAB,$$
because $m'>0$. Thus $gAB$ is the least common multiple, and
$$\gcd(a,b)\operatorname{lcm}(a,b)=g\cdot gAB=g^2AB=ab.$$

**26.** Let $p$ be prime and $p\mid ab$. If $p\mid a$, there is nothing to prove. Otherwise $p\nmid a$. The positive divisors of $p$ are only $1$ and $p$, so the common divisors of $p$ and $a$ are just $1$; hence
$$\gcd(p,a)=1.$$
By Bézout's identity there are integers $x,y$ with
$$px+ay=1.$$
Multiply both sides by $b$:
$$b=pbx+aby.$$
The first term $pbx$ is divisible by $p$. The second term $aby$ is divisible by $p$ because $p\mid ab$. Therefore $p$ divides their sum, which is $b$. So either $p\mid a$ or $p\mid b$.

**27.** Suppose, for contradiction, that $\sqrt2$ is rational. Then there are positive integers $p,q$ with
$$\sqrt2=\dfrac pq,\qquad \gcd(p,q)=1.$$
Squaring gives $2q^2=p^2$.

Since $p^2=2q^2$ is even, $p^2$ is even. If $p$ were odd, say $p=2k+1$, then
$$p^2=4k^2+4k+1=2(2k^2+2k)+1$$
would be odd; so $p$ must be even. Write $p=2k$. Then
$$2q^2=(2k)^2=4k^2\implies q^2=2k^2,$$
so $q^2$ is even, and the same parity argument shows that $q$ is even.

Thus $2\mid p$ and $2\mid q$, contradicting $\gcd(p,q)=1$. Therefore no such $p,q$ exist, and $\sqrt2$ is irrational.

*Alternative using the fundamental theorem of arithmetic.* The exponent of $2$ in $p^2$ is even, while the exponent of $2$ in $2q^2$ is one more than an even number, hence odd. Unique factorization forbids the equality $p^2=2q^2$.

**28.** For $360=2^3\cdot3^2\cdot5^1$, every positive divisor has the form
$$2^a3^b5^c,\qquad 0\le a\le3,\quad0\le b\le2,\quad0\le c\le1.$$
There are $4$ choices for $a$, $3$ for $b$ and $2$ for $c$, hence
$$\tau(360)=4\cdot3\cdot2=24.$$

For $1{,}071=3^2\cdot7^1\cdot17^1$:
$$\tau(1{,}071)=3\cdot2\cdot2=12.$$

Why exactly once: every divisor is a product of the same primes with exponents no larger than those in $n$ (otherwise it would not divide $n$), so it corresponds to an exponent tuple. Conversely, every tuple in the stated ranges gives a divisor. Distinct tuples give distinct integers by uniqueness of prime factorization, so the correspondence is a bijection, and the number of tuples is the product. The divisors of $1{,}071$ are $1,3,7,9,17,21,51,63,119,153,357,1{,}071$.

## Challenge

**29.** Write $n=6k$. Since $84=6\cdot14$,
$$\gcd(n,84)=\gcd(6k,6\cdot14)=6\gcd(k,14).$$
(A common factor can be pulled out of a gcd: $6$ divides both arguments.) We need
$$6\gcd(k,14)=6\iff\gcd(k,14)=1.$$
Also $n<100$ gives $6k<100$, so $k\le16$.

Now $14=2\cdot7$, so $\gcd(k,14)=1$ exactly when $k$ is odd and not divisible by $7$. Among $1\le k\le16$ these are
$$1,3,5,9,11,13,15.$$
Therefore
$$n\in\{6,18,30,54,66,78,90\}.$$
There are seven solutions. No others exist: any solution must be a multiple of $6$ with $k\le16$ and $\gcd(k,14)=1$, and the list exhausts those $k$. Check one: $n=90=2\cdot3^2\cdot5$ and $84=2^2\cdot3\cdot7$, so $\gcd=2\cdot3=6$.

**30.** Suppose, for contradiction, that there are only finitely many primes. List them all:
$$p_1,p_2,\dots,p_n.$$
Consider
$$N=p_1p_2\cdots p_n+1.$$
Then $N>1$. Every integer greater than $1$ has a prime divisor (by the existence part of the fundamental theorem of arithmetic, or by taking the smallest divisor greater than $1$). Let $q$ be a prime divisor of $N$.

Since the list contains all primes, $q=p_i$ for some $i$. But $p_i$ divides the product $p_1\cdots p_n$, and $p_i$ also divides $N$, so $p_i$ divides
$$N-p_1\cdots p_n=1.$$
No prime divides $1$, a contradiction. Hence the assumption of finitely many primes is false: there are infinitely many primes.

**31.** If $n=p_1^{e_1}\cdots p_k^{e_k}$, then $\tau(n)=(e_1+1)\cdots(e_k+1)=10$. Since $10=10$ or $10=2\cdot5$, the exponent pattern is either

* one prime with $e_1+1=10$, so $n=p^9$; the smallest is $2^9=512$; or
* two primes with exponents $4$ and $1$, so $n=p^4q$ with distinct primes $p,q$.

For the second pattern, compare the possibilities: $2^4\cdot3=48$, $2^4\cdot5=80$, $3^4\cdot2=162$, and larger primes give larger values. The minimum is $48$.

Since every $n$ with $\tau(n)=10$ has one of these two forms, and every number of the first form is at least $512>48$, the smallest is
$$n=48=2^4\cdot3,\qquad \tau(48)=(4+1)(1+1)=10.$$
Its divisors are $1,2,3,4,6,8,12,16,24,48$, ten in total. No smaller integer works because the case analysis covers all exponent patterns that multiply to $10$.

**32.** Suppose $n>1$ is composite. Then $n=ab$ with integers $1<a\le b<n$. Multiplying the inequality $a\le b$ by $a>0$ gives
$$a^2\le ab=n,$$
so $a\le\sqrt n$. Thus every composite $n$ has a divisor $a$ with
$$2\le a\le\sqrt n.$$

Consequently, if no integer $d$ with $2\le d\le\sqrt n$ divides $n$, then $n$ cannot be written as a product of two smaller factors, so $n$ is prime. This is the contrapositive of the statement above.

A trial-division loop implements exactly this test:

```python
def is_prime(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True
```

The condition `d*d <= n` is the inequality $d\le\sqrt n$ written without computing a square root, which avoids floating-point rounding. If a divisor exists, the first one found is at most $\sqrt n$, so the loop returns `False`; if the loop finishes, no divisor up to $\sqrt n$ exists and `True` is returned. The loop runs at most about $\sqrt n$ iterations, which is why trial division is practical for $n$ up to roughly $10^{12}$ but not for cryptographic-size numbers.
