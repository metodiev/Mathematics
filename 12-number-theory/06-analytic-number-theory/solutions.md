# Analytic Number Theory — Solutions

> [Analytic Number Theory](README.md) · Solutions to the 36 problems in [exercises.md](exercises.md)

Each solution states the strategy first, then carries out every step and names the theorem used. Numbers in
parentheses such as (§7.2) refer to the section of the [tutorial](README.md) where the relevant result is proved.
Where a second route exists it is given as a remark; likely pitfalls are flagged where they occur.

## Beginner

**1.** *Strategy: factor $360$ into primes and apply the multiplicative formulas; the check is the identity
$\sum_{d\mid n}\varphi(d)=n$ applied prime-power by prime-power.*

$360=2^{3}\cdot3^{2}\cdot5$. Since $\tau$, $\sigma$ and $\varphi$ are multiplicative and their values at prime
powers are
$$
\tau(p^{a})=a+1,\qquad \sigma(p^{a})=1+p+\dots+p^{a},\qquad \varphi(p^{a})=p^{a}-p^{a-1},
$$
we get
$$
\tau(360)=(3+1)(2+1)(1+1)=4\cdot3\cdot2=24,
$$
$$
\sigma(360)=(1+2+4+8)(1+3+9)(1+5)=15\cdot13\cdot6=1170,
$$
$$
\varphi(360)=360\left(1-\tfrac12\right)\left(1-\tfrac13\right)\left(1-\tfrac15\right)=360\cdot\tfrac12\cdot\tfrac23\cdot\tfrac45=96 .
$$
Finally $\mu(360)=0$, because $2^{2}\mid360$: a cube-free condition is not needed, but squarefreeness is, and it
fails.

*Check.* For $n=p^{a}$, $\sum_{d\mid p^{a}}\varphi(d)=1+\sum_{k=1}^{a}p^{k-1}(p-1)=1+(p^{a}-1)=p^{a}$. The sum
is multiplicative in $n$ (it is $\varphi*\mathbf{1}$), so
$$
\sum_{d\mid360}\varphi(d)=2^{3}\cdot3^{2}\cdot5=360,
$$
as it must be. $\blacksquare$

**2.** *Strategy: multiplicativity is a statement about coprime factorisations, so every proof must split a
divisor $d$ of $mn$ into its $m$-part and its $n$-part.*

(a) For all $m,n$, $(mn)^{2}=m^{2}n^{2}$, so $f(n)=n^{2}$ satisfies the defining identity for all pairs, not
only coprime ones: $f$ is completely multiplicative. Also $f(1)=1$.

(b) If $f$ and $g$ are multiplicative and $\gcd(m,n)=1$, then
$$
(fg)(mn)=f(mn)g(mn)=f(m)f(n)g(m)g(n)=(fg)(m)(fg)(n).
$$
Also $(fg)(1)=f(1)g(1)=1$. Note that the argument only proves multiplicativity, not complete multiplicativity:
$f(n)=n^{2}$ and $g=\tau$ have product $n^{2}\tau(n)$, which is not completely multiplicative because $\tau$ is
not.

(c) Let $\gcd(m,n)=1$. Every divisor $d$ of $mn$ is uniquely $d=d_{1}d_{2}$ with $d_{1}\mid m$ and $d_{2}\mid n$,
because $m$ and $n$ share no prime. Then $mn/d=(m/d_{1})(n/d_{2})$ with $\gcd(m/d_{1},n/d_{2})=1$. Hence
$$
(f*g)(mn)=\sum_{d\mid mn}f(d)g\!\left(\frac{mn}{d}\right)
=\sum_{d_{1}\mid m}\sum_{d_{2}\mid n}f(d_{1})f(d_{2})\,g\!\left(\frac{m}{d_{1}}\right)g\!\left(\frac{n}{d_{2}}\right),
$$
which is the product of $\sum_{d_{1}\mid m}f(d_{1})g(m/d_{1})=(f*g)(m)$ and the analogous sum for $n$. Also
$(f*g)(1)=f(1)g(1)=1$. So $f*g$ is multiplicative. $\blacksquare$

*Remark.* Part (c) is the reason multiplicativity is such a powerful tool: it reduces every statement about
$f*g$ at $n=\prod p^{a_p}$ to the prime-power case $m=p^{a}$, which is a finite computation.

**3.** *Strategy: $\mu(d)\ne0$ only for squarefree $d$, so the divisor sum becomes a sum over subsets of the prime
divisors.*

Let $n=\prod_{i=1}^{k}p_i^{e_i}$ with $e_i\ge1$. A divisor $d$ with $\mu(d)\ne0$ must be a product of distinct
primes among $p_1,\dots,p_k$, and then $\mu(d)=(-1)^{\#\text{of its primes}}$. Therefore
$$
(\mu*\mathbf{1})(n)=\sum_{d\mid n}\mu(d)=\sum_{S\subseteq\{1,\dots,k\}}(-1)^{|S|}=\sum_{j=0}^{k}\binom{k}{j}(-1)^{j}=(1-1)^{k}.
$$
For $k=0$ (that is $n=1$) the sum is the empty product $(1-1)^{0}=1=\varepsilon(1)$; for $k\ge1$ it is $0=\varepsilon(n)$.
Hence $\mu*\mathbf{1}=\varepsilon$.

Now $\varphi=\mu*\operatorname{id}$ gives, for $n=12=2^{2}\cdot3$,
$$
\varphi(12)=\sum_{d\mid12}\mu(d)\frac{12}{d}
=\mu(1)\cdot12+\mu(2)\cdot6+\mu(3)\cdot4+\mu(4)\cdot3+\mu(6)\cdot2+\mu(12)\cdot1 .
$$
The values are $\mu(1)=1$, $\mu(2)=\mu(3)=\mu(6)=-1$ (a single prime, and $6=2\cdot3$ is squarefree with two
primes), $\mu(4)=\mu(12)=0$. Hence
$$
\varphi(12)=12-6-4+0+2-0=4,
$$
matching the direct count $\{1,5,7,11\}$. $\blacksquare$

**4.** *Strategy: $\Lambda(n)\ne0$ exactly at prime powers, where it equals $\log p$; group by prime.*

$$
\sum_{n\le10}\Lambda(n)=\Lambda(2)+\Lambda(3)+\Lambda(4)+\Lambda(5)+\Lambda(7)+\Lambda(8)+\Lambda(9)
=\log2+\log3+\log2+\log5+\log7+\log2+\log3 .
$$
Collecting, the sum is $3\log2+2\log3+\log5+\log7=\log(2^{3}\cdot3^{2}\cdot5\cdot7)=\log2520$.

And $\operatorname{lcm}(1,\dots,10)=2^{3}\cdot3^{2}\cdot5\cdot7=2520$: the least common multiple uses, for each
prime $p\le10$, the largest power $p^{k}\le10$, and $\psi$ sums precisely $\log p$ over those powers. In general
$$
\psi(x)=\sum_{p^{k}\le x}\log p=\log\prod_{p^{k}\le x}p=\log\operatorname{lcm}(1,2,\dots,\lfloor x\rfloor).
$$
$\blacksquare$

**5.** *Strategy: bound each term $1/n$ between two integrals over adjacent unit intervals.*

For $n\ge1$ and $t\in[n,n+1]$ we have $1/(n+1)\le1/t\le1/n$, hence
$$
\frac{1}{n+1}=\int_n^{n+1}\frac{dt}{n+1}\le\int_n^{n+1}\frac{dt}{t}\le\frac1n .
$$
Summing the right inequality over $n=1,\dots,N$ gives
$$
\sum_{n=1}^{N}\frac1n\ \ge\ \sum_{n=1}^{N}\int_n^{n+1}\frac{dt}{t}=\log(N+1).
$$
Summing the left inequality over $n=1,\dots,N-1$ gives $\sum_{n=2}^{N}1/n\le\log N$, hence
$\sum_{n=1}^{N}1/n\le1+\log N$. Replacing $N$ by $\lfloor x\rfloor$ and using $\log\lfloor x\rfloor\le\log x\le\log(\lfloor x\rfloor+1)$,
$$
\log x\ \le\ \log(\lfloor x\rfloor+1)\le\sum_{n\le x}\frac1n\le1+\log\lfloor x\rfloor\le1+\log x .
$$
So the difference $\sum_{n\le x}1/n-\log x$ lies in $[0,1]$: $\sum_{n\le x}1/n=\log x+O(1)$ with implied constant
$1$. $\blacksquare$

*Remark.* The sharper statement $\log x+\gamma+O(1/x)$ needs the convergent series of Example 9.1; the two-sided
bound above is the right first step and is all that many arguments require.

**6.** *Strategy: compare the direct count with the lattice-point count, which is the hyperbola identity.*

The divisor counts for $1\le n\le20$ are
$$
1,2,2,3,2,4,2,4,3,4,2,6,2,4,4,5,2,6,2,6,
$$
with sum $66$.

For the hyperbola method, $\lfloor\sqrt{20}\rfloor=4$ and
$$
\sum_{d=1}^{4}\left\lfloor\frac{20}{d}\right\rfloor=20+10+6+5=41,
$$
so Theorem 7.7 gives $2\cdot41-4^{2}=82-16=66$, in agreement.

The asymptotic $x\log x+(2\gamma-1)x$ at $x=20$ equals $20\cdot2.995732+0.154431\cdot20=59.9146+3.0886=63.00$,
so the error is $3.00$, inside the bound $\sqrt{20}\approx4.47$. $\blacksquare$

**7.** *Strategy: the Euler product for $1/\zeta$ is a product of geometric series with ratio $-p^{-s}$; expanding
it produces exactly the Möbius weights.*

For $\operatorname{Re}s>1$ the Euler product $\zeta(s)=\prod_p(1-p^{-s})^{-1}$ converges absolutely (Theorem 7.1),
and every factor is a non-zero complex number. Hence we may invert and multiply out:
$$
\frac{1}{\zeta(s)}=\prod_p\left(1-p^{-s}\right)=\sum_{n\ \text{squarefree}}(-1)^{\omega(n)}n^{-s}=\sum_{n\ge1}\mu(n)n^{-s},
$$
where the expansion is legitimate because $\sum_p|p^{-s}|<\infty$, so the product $\prod_p(1+a_p)$ with
$a_p=-p^{-s}$ converges absolutely and may be expanded in any order; the coefficient of $n^{-s}$ is $\prod_{p\mid n}(-1)=\mu(n)$
for squarefree $n$ and $0$ otherwise. Setting $s=2$,
$$
\sum_{n\ge1}\frac{\mu(n)}{n^{2}}=\frac{1}{\zeta(2)}=\frac{6}{\pi^{2}}=0.607927\dots
$$
The same expansion read as a density statement says that the "probability" that a random integer is not divisible
by any $p^{2}$ should be $\prod_p(1-1/p^{2})=6/\pi^{2}$; making this rigorous requires
$\sum_{n\le x}\mu^{2}(n)=\frac{6}{\pi^{2}}x+O(\sqrt x)$, which is Problem 34. $\blacksquare$

**8.** *Strategy: absolute convergence is decided by $\sum n^{-\sigma}$; conditional convergence by the
alternating-series test.*

The series is $\sum a_n n^{-s}$ with $a_n=(-1)^{n}$. Absolute convergence at $s=\sigma$ is convergence of
$\sum n^{-\sigma}$, which holds exactly for $\sigma>1$: so $\sigma_a=1$.

For $0<\sigma\le1$ the terms $(-1)^{n}n^{-\sigma}$ alternate in sign with modulus $n^{-\sigma}$ decreasing to $0$,
so the series converges by the alternating-series test; hence $\sigma_c\le0$. At $s=0$ the terms are $(-1)^{n}$,
which do not tend to $0$, so the series diverges; hence $\sigma_c=0$.

For $\operatorname{Re}s>1$,
$$
\sum_{n\ge1}\frac{(-1)^{n}}{n^{s}}=-\sum_{n\ge1}\frac{(-1)^{n-1}}{n^{s}}=-\left(1-2^{1-s}\right)\zeta(s),
$$
the factor $1-2^{1-s}$ arising from subtracting twice the even terms. The right side is holomorphic for
$\operatorname{Re}s>0$ except at $s=1$, where $1-2^{1-s}$ vanishes and cancels the pole of $\zeta$; this is the
analytic continuation of the series beyond its abscissa of absolute convergence.

The two abscissae differ because convergence at $\sigma\in(0,1]$ is conditional: the cancellation between positive
and negative terms is what makes the series converge, and cancellation is destroyed by taking absolute values.
$\blacksquare$

**9.** *Strategy: compare the sum with the integral of the same decreasing function on both sides.*

For $s>1$ the function $x\mapsto x^{-s}$ is positive and decreasing on $[1,\infty)$. Therefore, for $n\ge1$,
$$
\int_n^{n+1}x^{-s}\,dx\ \le\ n^{-s}\ \le\ \int_{n-1}^{n}x^{-s}\,dx\quad(n\ge2),
$$
the left inequality because $x^{-s}\le n^{-s}$ on $[n,n+1]$, the right because $x^{-s}\ge n^{-s}$ on $[n-1,n]$.
Summing the left inequality over $n\ge1$ and the right over $n\ge2$,
$$
\int_1^\infty x^{-s}dx\ \le\ \sum_{n\ge1}n^{-s}\ \le\ 1+\int_1^\infty x^{-s}dx,
$$
that is $\frac{1}{s-1}\le\zeta(s)\le1+\frac{1}{s-1}$. Multiplying by $s-1>0$,
$$
1\le(s-1)\zeta(s)\le(s-1)+1\longrightarrow1,
$$
so $\zeta(s)=O(1/(s-1))$ and in fact $(s-1)\zeta(s)\to1$. $\blacksquare$

*Pitfall.* Do not conclude $\zeta(1)=1$ or "$\zeta(1)=\infty$": the limit statement is about the product
$(s-1)\zeta(s)$, and $\zeta$ has a pole at $s=1$.

**10.** *Strategy: dominate the prime sum by the full series, and compare exponents.*

Since every prime is an integer at least $2$,
$$
\sum_p\frac{1}{p^{2}}\ \le\ \sum_{n=2}^{\infty}\frac{1}{n^{2}}=\zeta(2)-1=\frac{\pi^{2}}{6}-1=0.644934\dots,
$$
and the majorant converges, so the prime sum converges (its terms are positive, so bounded partial sums suffice).

There is no contradiction with $\sum_p1/p=\infty$: the two series have different exponents. For $p\ge2$,
$p^{-2}\le\frac12p^{-1}$, so convergence of $\sum p^{-2}$ is *weaker* than convergence of $\sum p^{-1}$ and says
nothing about it. The general principle is that $\sum_p p^{-\sigma}$ converges if and only if $\sigma>1$
(Theorem 7.1 with real $s=\sigma$), so the boundary case $\sigma=1$ is the divergent one. $\blacksquare$

## Intermediate

**11.** *Strategy: expand the product $\prod_{p\mid n}(1-1/p)$ and recognise the Möbius weights.*

For $n=\prod_{i=1}^{k}p_i^{e_i}$,
$$
\prod_{p\mid n}\left(1-\frac1p\right)=\sum_{S\subseteq\{1,\dots,k\}}(-1)^{|S|}\prod_{i\in S}\frac{1}{p_i}
=\sum_{\substack{d\mid n\\ d\ \text{squarefree}}}\frac{\mu(d)}{d}=\sum_{d\mid n}\frac{\mu(d)}{d},
$$
since $\mu(d)=0$ when $d$ is not squarefree. Multiplying by $n$,
$$
\varphi(n)=n\prod_{p\mid n}\left(1-\frac1p\right)=n\sum_{d\mid n}\frac{\mu(d)}{d}=\sum_{d\mid n}\mu(d)\frac{n}{d}=(\mu*\operatorname{id})(n).
$$
$\blacksquare$

*Remark.* The identity $\varphi=n\sum_{d\mid n}\mu(d)/d$ is the most useful form for asymptotics: it writes
$\varphi$ as a Dirichlet convolution, which is what Theorem 7.9 exploits.

**12.** *Strategy: (a) is one line of convolution algebra; (b) is a counting argument that identifies the two
sides as two ways of counting the same finite set.*

(a) Using Problem 11 in the form $\varphi=\mu*\operatorname{id}$ and Theorem 7.6,
$$
\varphi*\mathbf{1}=(\mu*\operatorname{id})*\mathbf{1}=\operatorname{id}*(\mu*\mathbf{1})=\operatorname{id}*\varepsilon=\operatorname{id}.
$$
Evaluating at $n$ gives $\sum_{d\mid n}\varphi(d)=n$.

(b) Consider the $n$ fractions $\frac1n,\frac2n,\dots,\frac nn$. Each reduces uniquely to $\frac ab$ in lowest
terms with $b\mid n$ and $1\le a\le b$, $\gcd(a,b)=1$. For a fixed $b\mid n$, the number of fractions that
reduce to denominator exactly $b$ is $\varphi(b)$, since the admissible numerators are the $\varphi(b)$ integers
$a\in\{1,\dots,b\}$ coprime to $b$. Summing over $b\mid n$ counts all $n$ fractions:
$$
n=\sum_{b\mid n}\varphi(b).\qquad\blacksquare
$$
*Pitfall.* In (b) the fraction $n/n$ reduces to $1/1$, which is counted by $b=1$; omitting it loses the term
$\varphi(1)=1$.

**13.** *Strategy: reduce every statement to the least index at which a function is non-zero.*

That $(\mathcal{A},+,*)$ is a commutative ring with identity $\varepsilon$ is Theorem 7.5: commutativity and
associativity follow by writing $(f*g)(n)=\sum_{de=n}f(d)g(e)$, distributivity is immediate, and $\varepsilon$ is
the identity.

*Integral domain.* Let $f,g\ne0$ and let $m$, $n$ be the least integers with $f(m)\ne0$, $g(n)\ne0$. In
$$
(f*g)(mn)=\sum_{d\mid mn}f(d)g\!\left(\frac{mn}{d}\right)
$$
a term with $f(d)\ne0$ has $d\ge m$ by minimality of $m$; a term with $g(mn/d)\ne0$ has $mn/d\ge n$, i.e.
$d\le m$. Hence the only possibly non-zero term is $d=m$, and it equals $f(m)g(n)\ne0$. So $f*g\ne0$.

*Units.* If $f*g=\varepsilon$ then $f(1)g(1)=1$, so $f(1)\ne0$. Conversely, if $f(1)\ne0$, define $g$
recursively by $g(1)=1/f(1)$ and, for $n>1$,
$$
g(n)=-\frac{1}{f(1)}\sum_{\substack{d\mid n\\ d<n}}f\!\left(\frac nd\right)g(d).
$$
Then $(f*g)(1)=1$ and, for $n>1$, $(f*g)(n)=f(1)g(n)+\sum_{d\mid n,d<n}f(n/d)g(d)=0$ by the recursion; so
$f*g=\varepsilon$.

*Examples.* The inverse of $\mathbf{1}$ is $\mu$ (Theorem 7.6). The inverse of $\operatorname{id}$ is
$n\mapsto\mu(n)n$: indeed its Dirichlet series is $\sum\mu(n)n\cdot n^{-s}=\sum\mu(m)m^{-(s-1)}=1/\zeta(s-1)$,
which is the reciprocal of $\zeta(s-1)=\sum n\cdot n^{-s}$, and the Dirichlet series of a convolution is the
product of the Dirichlet series. Directly, for $n=p$: $1\cdot\mu(p)p+p\cdot\mu(1)= -p+p=0$; for $n=p^{2}$:
$\mu(p^{2})p^{2}+p\mu(p)p+p^{2}\mu(1)=0-1\cdot p^{2}+p^{2}=0$; and multiplicativity handles the rest.
$\blacksquare$

**14.** *Strategy: summation by parts, i.e. write $a_n=A(n)-A(n-1)$ and telescope.*

Let $N=\lfloor x\rfloor$. Then
$$
\sum_{n\le x}a_nf(n)=\sum_{n=1}^{N}\left(A(n)-A(n-1)\right)f(n)
=A(N)f(N)+\sum_{n=1}^{N-1}A(n)\left(f(n)-f(n+1)\right),
$$
where $A(0)=0$ was used and the second step is a rearrangement of the telescoping sum. Since
$f(n)-f(n+1)=-\int_n^{n+1}f'(t)\,dt$ and $A(t)=A(n)$ on $[n,n+1)$,
$$
\sum_{n=1}^{N-1}A(n)\left(f(n)-f(n+1)\right)=-\int_1^{N}A(t)f'(t)\,dt .
$$
Also $A(N)=A(x)$, since there is no integer in $(N,x]$. Hence
$$
\sum_{n\le x}a_nf(n)=A(x)f(x)-\int_1^{x}A(t)f'(t)\,dt,
$$
because $\int_N^xA(t)f'(t)dt=0$ (the interval contains no integer, and $A$ is constant there while the integral of
$f'$ over the remaining piece is absorbed in $A(x)f(x)-A(N)f(N)$, which is zero). $\blacksquare$

*Remark.* The same identity is the Riemann–Stieltjes integration-by-parts formula
$\int_{1^-}^{x}f\,dA= A(x)f(x)-\int_1^xA\,df$, and it is the engine behind almost every estimate in §7.5.

**15.** *Strategy: apply Problem 14 with $a_n=1$, so that $A(t)=\lfloor t\rfloor$, then split
$\lfloor t\rfloor=t-\{t\}$.*

With $A(t)=\lfloor t\rfloor$ and $f(t)=\log t$, $f'(t)=1/t$:
$$
\sum_{n\le x}\log n=\lfloor x\rfloor\log x-\int_1^{x}\frac{\lfloor t\rfloor}{t}\,dt
=\lfloor x\rfloor\log x-\int_1^{x}dt+\int_1^{x}\frac{\{t\}}{t}\,dt .
$$
Now $\lfloor x\rfloor\log x=x\log x+O(\log x)$, $\int_1^xdt=x-1$, and
$0\le\int_1^x\{t\}/t\,dt\le\int_1^xdt/t=\log x$. Therefore
$$
\sum_{n\le x}\log n=x\log x-x+O(\log x).
$$
$\blacksquare$

*Check.* At $x=10$: $\sum_{n\le10}\log n=\log(3628800)=15.1044$, while
$x\log x-x=23.0259-10=13.0259$; the difference $2.0785$ is indeed $O(\log10=2.3026)$. Stirling's formula
$\log(n!)=n\log n-n+O(\log n)$ is the same statement.

**16.** *Strategy: bound each term $\log p$ by $\log x$; for the reverse inequality, discard the small primes so
that each surviving prime contributes at least $\frac12\log x$.*

For $p\le x$ we have $\log p\le\log x$, so
$$
\theta(x)=\sum_{p\le x}\log p\le\pi(x)\log x .
$$
Conversely, restricting to primes $\sqrt x<p\le x$,
$$
\theta(x)\ \ge\ \sum_{\sqrt x<p\le x}\log p\ \ge\ \left(\pi(x)-\pi(\sqrt x)\right)\frac{\log x}{2}\ \ge\ \left(\pi(x)-\sqrt x\right)\frac{\log x}{2},
$$
because each such prime satisfies $\log p>\frac12\log x$ and $\pi(\sqrt x)\le\sqrt x$. Rearranging,
$$
\pi(x)\ \le\ \frac{2\theta(x)}{\log x}+\sqrt x .
$$
Combining: from $\theta(x)\le3x\log2$ (Theorem 7.19(a)) we get $\pi(x)\le6\log2\cdot x/\log x+\sqrt x\le C_2x/\log x$ for
$x\ge4$, since $\sqrt x\le x/\log x$ there. From $\theta(x)\ge\frac{\log2}{8}x$ for $x$ large (the lower bound of
Theorem 7.19 combined with $\psi=\theta+O(\sqrt x\log x)$), the inequality $\theta\le\pi\log x$ gives
$\pi(x)\ge\frac{\log2}{8}x/\log x$. Adjusting the constant to cover $2\le x<x_0$, we get $\pi(x)\asymp x/\log x$.
$\blacksquare$

*Pitfall.* The upper bound on $\theta$ gives the upper bound on $\pi$, and the lower bound on $\theta$ gives the
lower bound on $\pi$; mixing them up produces a non-existent proof of the prime number theorem, which needs the
sharp constant $1$, not merely two-sided bounds.

**17.** *Strategy: group the terms of $\psi$ according to the exponent $k$ in $p^{k}$.*

Every term $\log p$ of $\psi(x)$ comes from a unique pair $(p,k)$ with $p^{k}\le x$. Grouping by $k$,
$$
\psi(x)=\sum_{k\ge1}\sum_{\substack{p\\ p^{k}\le x}}\log p=\sum_{k\ge1}\theta\!\left(x^{1/k}\right),
$$
the inner sum being $\theta(x^{1/k})$ because $p^{k}\le x\iff p\le x^{1/k}$ (both sides positive). The sum is
finite: $p^{k}\le x$ with $p\ge2$ forces $k\le\log_2x$, so only $k\le\lfloor\log_2x\rfloor$ terms are non-zero.

For the estimate, the terms with $k\ge2$ number at most $\log_2x$, and each is at most
$\theta(x^{1/2})\le3x^{1/2}\log2$ by Theorem 7.19(a). Hence
$$
0\le\psi(x)-\theta(x)=\sum_{k\ge2}\theta(x^{1/k})\ \le\ 3\log2\cdot(\log_2x)\sqrt x=O\!\left(\sqrt x\log x\right).
$$
$\blacksquare$

*Remark.* The bound uses $\theta(y)\le Cy$, i.e. Chebyshev's upper bound. With only the trivial bound
$\theta(y)\le y\log y$ one gets $O(\sqrt x(\log x)^{2})$, still enough for the asymptotic equivalence
$\psi\sim x\iff\theta\sim x$.

**18.** *Strategy: interchange the order of summation, then sum the inner arithmetic progression explicitly.*

$$
\sum_{n\le x}\sigma(n)=\sum_{n\le x}\sum_{d\mid n}d=\sum_{d\le x}d\sum_{\substack{n\le x\\ d\mid n}}1=\sum_{d\le x}d\left\lfloor\frac xd\right\rfloor .
$$
Now put $q=\lfloor x/d\rfloor$ and sum over $q$ instead: for fixed $q$, $d$ runs through $x/(q+1)<d\le x/q$, so
$d\le x/q$ and
$$
\sum_{d\le x}d\left\lfloor\frac xd\right\rfloor=\sum_{q\le x}\ \sum_{d\le x/q}d=\sum_{q\le x}\left(\frac12\left(\frac xq\right)^{2}+O\!\left(\frac xq\right)\right),
$$
using $\sum_{d\le y}d=\frac12y^{2}+O(y)$. Therefore
$$
\sum_{n\le x}\sigma(n)=\frac{x^{2}}{2}\sum_{q\le x}\frac{1}{q^{2}}+O\!\left(x\sum_{q\le x}\frac1q\right)
=\frac{x^{2}}{2}\left(\zeta(2)+O\!\left(\frac1x\right)\right)+O(x\log x)=\frac{\pi^{2}}{12}x^{2}+O(x\log x),
$$
where $\sum_{q>x}q^{-2}=O(1/x)$ was used. $\blacksquare$

**19.** *Strategy: pair the term $n=3k+1$ with $n=3k+2$; each pair is a positive difference.*

Since $\chi_{3}(3k)=0$, the series groups into blocks of three, and within a block only the first two terms
survive:
$$
L(1,\chi_{3})=\sum_{k\ge0}\left(\frac{1}{3k+1}-\frac{1}{3k+2}\right)
=\sum_{k\ge0}\frac{(3k+2)-(3k+1)}{(3k+1)(3k+2)}=\sum_{k\ge0}\frac{1}{(3k+1)(3k+2)} .
$$
Every term of the last series is strictly positive, and the series converges because the general term is
$O(k^{-2})$. Hence $L(1,\chi_{3})>0$. In fact $L(1,\chi_{3})=\pi/(3\sqrt3)=0.604599\dots$, but the positivity is
all that Dirichlet's theorem requires. $\blacksquare$

*Pitfall.* The grouping is legitimate because the series converges (absolutely or by grouping into pairs whose
partial sums converge). Grouping a divergent series is not allowed; here convergence holds, so the value is the
sum of the groups.

**20.** *Strategy: invert the Euler product factor by factor and expand absolutely.*

For $\operatorname{Re}s>1$, Theorem 7.1 gives $\zeta(s)=\prod_p(1-p^{-s})^{-1}$ with absolute convergence, so
$$
\frac{1}{\zeta(s)}=\prod_p\left(1-p^{-s}\right).
$$
Each factor is a finite sum $1+(-p^{-s})$ and $\sum_p|p^{-s}|<\infty$, so the product converges absolutely and
$$
\prod_p\left(1-p^{-s}\right)=\sum_{n\ge1}\left(\prod_{p\mid n}(-1)\right)n^{-s}=\sum_{n\ge1}\mu(n)n^{-s},
$$
the coefficient of $n^{-s}$ being $(-1)^{\omega(n)}$ for squarefree $n$ and $0$ otherwise, which is exactly
$\mu(n)$.

Since $|\mu(n)|\le1$, absolute convergence holds for $\operatorname{Re}s>1$ and fails for $\operatorname{Re}s\le1$
(where the series reduces to at least the harmonic series in modulus), so $\sigma_a=1$. For $\sigma_c$: if the
series converged on a half-plane containing a neighbourhood of $s=1$, it would define a holomorphic function there;
but its sum equals $1/\zeta(s)$ for $\operatorname{Re}s>1$, and $1/\zeta$ has a pole at $s=1$ because $\zeta$ has
a zero-free simple pole there. Hence $\sigma_c\ge1$, and with $\sigma_a=1$ we get $\sigma_c=\sigma_a=1$.
$\blacksquare$

*Remark.* The fact that the series converges at $s=1$ as well is equivalent to the prime number theorem in the form
$\sum_{n\le x}\mu(n)=o(x)$; that equivalence is far deeper than the value of $\sigma_c$ computed here.

## Advanced

**21.** *Strategy: extract $\psi(2n)$ from the prime factorisation of the central binomial coefficient, then use
the elementary lower bound for that coefficient.*

**(a) The upper bound for $\log\binom{2n}{n}$ in terms of $\psi$.** By Legendre's formula,
$$
\log\binom{2n}{n}=\sum_{p^{k}\le2n}\left(\left\lfloor\frac{2n}{p^{k}}\right\rfloor-2\left\lfloor\frac{n}{p^{k}}\right\rfloor\right)\log p .
$$
For every real $y$, $\lfloor2y\rfloor-2\lfloor y\rfloor=\lfloor2\{y\}\rfloor\in\{0,1\}$. Hence each exponent is $0$
or $1$, and
$$
\log\binom{2n}{n}\ \le\ \sum_{p^{k}\le2n}\log p=\psi(2n).
$$

**(b) The lower bound for $\log\binom{2n}{n}$.** The $2n+1$ coefficients $\binom{2n}{k}$ sum to $2^{2n}$; the
central one is the largest (the ratio $\binom{2n}{k+1}/\binom{2n}{k}=(2n-k)/(k+1)$ decreases in $k$ and crosses
$1$ at $k=n$). Therefore
$$
\binom{2n}{n}\ \ge\ \frac{2^{2n}}{2n+1}.
$$

**(c) Combining.** From (a) and (b),
$$
\psi(2n)\ \ge\ 2n\log2-\log(2n+1).
$$
We claim this is at least $n\log2$ for $n\ge3$, i.e. $n\log2\ge\log(2n+1)$. At $n=3$ this reads
$2.0794\ge1.9459$; and the function $g(n)=n\log2-\log(2n+1)$ has derivative $\log2-\frac{2}{2n+1}\ge\log2-\frac23>0$
for $n\ge1$, so it is increasing and the inequality persists. Hence
$$
\psi(2n)\ \ge\ n\log2=\frac{\log2}{2}\,(2n)\qquad(n\ge3).
$$

**(d) Odd arguments.** The construction produces bounds at the *even* arguments $2n$ only, because it counts
prime powers up to $2n$ through the binomial coefficient $\binom{2n}{n}$. For odd $x\ge7$ we use monotonicity:
$$
\psi(x)=\psi(x-1)\ \ge\ \frac{\log2}{2}(x-1)\ \ge\ \frac{\log2}{4}x,
$$
since $x-1\ge x/2$ for $x\ge2$. Combining with the trivial bound $\psi(x)\ge\log2$ for $2\le x<7$ gives
$\psi(x)\ge\frac{\log2}{4}x$ for all $x\ge2$, which is the lower bound of Theorem 7.19. $\blacksquare$

**22.** *Strategy: the partial product over primes $\le x$ already contains every $n\le x$ as a term of its
expansion; then take logarithms and estimate the prime-power tail.*

Every integer $n\le x$ has all its prime factors at most $x$. Expanding the finite product,
$$
\prod_{p\le x}\left(1-\frac1p\right)^{-1}=\prod_{p\le x}\sum_{k\ge0}p^{-k}=\sum_{\substack{n\ge1\\ P(n)\le x}}\frac1n\ \ge\ \sum_{n\le x}\frac1n .
$$
Now take logarithms. For $|z|<1$, $-\log(1-z)=\sum_{k\ge1}z^{k}/k$, so
$$
\log\prod_{p\le x}\left(1-\frac1p\right)^{-1}=\sum_{p\le x}\sum_{k\ge1}\frac{1}{k\,p^{k}}
=\sum_{p\le x}\frac1p+R,\qquad
R:=\sum_{p\le x}\sum_{k\ge2}\frac{1}{k\,p^{k}} .
$$
Bound $R$ by extending the sum to all primes and dropping the condition $p\le x$:
$$
R\ \le\ \sum_{p}\sum_{k\ge2}\frac{1}{k\,p^{k}}\ \le\ \sum_p\frac12\sum_{k\ge2}p^{-k}
=\sum_p\frac{1}{2p(p-1)}\ \le\ \frac12\sum_{n\ge2}\frac{1}{n(n-1)}=\frac12,
$$
the last sum telescoping: $\sum_{n=2}^{N}\frac{1}{n(n-1)}=\sum_{n=2}^{N}\left(\frac1{n-1}-\frac1n\right)=1-\frac1N\to1$.

Also $\sum_{n\le x}1/n\ge\int_1^{x+1}dt/t=\log(x+1)>\log x$, so
$$
\log\log x\ <\ \log\sum_{n\le x}\frac1n\ \le\ \log\prod_{p\le x}\left(1-\frac1p\right)^{-1}
=\sum_{p\le x}\frac1p+R\ \le\ \sum_{p\le x}\frac1p+\frac12 .
$$
Hence $\sum_{p\le x}1/p\ge\log\log x-\frac12$, which tends to infinity. $\blacksquare$

*Remark.* This proof is self-contained: it uses only unique factorisation and the harmonic estimate. It is weaker
than Mertens' asymptotic formula of Theorem 7.4 by an additive constant, which is irrelevant for divergence.

**23.** *Strategy: approximate $\lfloor x\rfloor$ by $x$ on each unit interval and telescope.*

For $\sigma>1$ and $N\ge2$, on $[n,n+1)$ we have $\lfloor x\rfloor=n$, so
$$
s\int_1^{N}\lfloor x\rfloor x^{-s-1}dx=\sum_{n=1}^{N-1}n\int_n^{n+1}sx^{-s-1}dx=\sum_{n=1}^{N-1}n\left(n^{-s}-(n+1)^{-s}\right).
$$
Write the sum as $\sum_{n=1}^{N-1}n^{1-s}-\sum_{n=1}^{N-1}n(n+1)^{-s}$ and reindex the second sum with $m=n+1$:
$$
\sum_{n=1}^{N-1}n\left(n^{-s}-(n+1)^{-s}\right)=\sum_{n=1}^{N-1}n^{1-s}-\sum_{m=2}^{N}(m-1)m^{-s}
=1+\sum_{n=2}^{N-1}\left(n-(n-1)\right)n^{-s}-(N-1)N^{-s},
$$
so
$$
s\int_1^{N}\lfloor x\rfloor x^{-s-1}dx=\sum_{n=1}^{N-1}n^{-s}-(N-1)N^{-s}=\sum_{n\le N-1}n^{-s}+O\!\left(N^{1-\sigma}\right).
$$
Since $\sigma>1$, $N^{1-\sigma}\to0$, so letting $N\to\infty$,
$$
\zeta(s)=s\int_1^{\infty}\lfloor x\rfloor x^{-s-1}dx .
$$
Now insert $\lfloor x\rfloor=x-\{x\}$:
$$
\zeta(s)=s\int_1^\infty x\cdot x^{-s-1}dx-s\int_1^\infty\{x\}x^{-s-1}dx=\frac{s}{s-1}-s\int_1^\infty\{x\}x^{-s-1}dx .
$$
Finally, multiply by $(s-1)$ and let $s\to1^{+}$: $(s-1)\cdot\frac{s}{s-1}\to1$, while
$$
\left|(s-1)s\int_1^\infty\{x\}x^{-s-1}dx\right|\le|s|(s-1)\int_1^\infty x^{-s-1}dx=|s|(s-1)\cdot\frac{1}{s}\longrightarrow0 .
$$
Hence $\lim_{s\to1}(s-1)\zeta(s)=1$: the pole is simple with residue $1$. $\blacksquare$

**24.** *Strategy: the asymmetric formula is an identity of meromorphic functions, so at points where one factor is
singular it must be read as a limit.*

Direct substitution at $s=-1$ is legitimate, because every factor is finite there ($\sin(-\pi/2)=-1$,
$\Gamma(2)=1$, $\zeta(2)=\pi^{2}/6$):
$$
\zeta(-1)=2^{-1}\pi^{-2}\sin\!\left(-\frac{\pi}{2}\right)\Gamma(2)\,\zeta(2)
=\frac{1}{2\pi^{2}}\cdot(-1)\cdot1\cdot\frac{\pi^{2}}{6}=-\frac{1}{12}.
$$

At $s=0$ substitution gives $2^{0}\pi^{-1}\sin(0)\Gamma(1)\zeta(1)=0\cdot\infty$, which is meaningless because
$\zeta$ has a pole at $1$. Take the limit instead, using $\sin(\pi s/2)=\frac{\pi s}{2}+O(s^{3})$,
$\Gamma(1-s)=1+O(s)$ and $\zeta(1-s)=-\frac1s+O(1)$ (the Laurent expansion of $\zeta$ at its pole):
$$
\zeta(s)=2^{s}\pi^{s-1}\left(\frac{\pi s}{2}+O(s^{3})\right)\left(1+O(s)\right)\left(-\frac1s+O(1)\right)
=-\frac12\cdot 2^{s}\pi^{s}\left(1+O(s)\right)\longrightarrow-\frac12 .
$$
So $\zeta(0)=-\frac12$. $\blacksquare$

*Pitfall.* The limit is not "obvious" from the formula: the zero of $\sin$ and the pole of $\zeta$ are of the same
order, and the finite value $-1/2$ is their ratio. The same mechanism produces the pole at $s=1$: there $\Gamma(1-s)$
has a pole while $\zeta(1-s)$ is finite.

**25.** *Strategy: the Euler product settles $\operatorname{Re}s>1$; the functional equation transfers the
information to $\operatorname{Re}s<0$, with the zeros of $\sin$ producing the trivial zeros.*

For $\operatorname{Re}s>1$, $\zeta(s)=\prod_p(1-p^{-s})^{-1}$ with every factor non-zero and the product
absolutely convergent, so $\zeta(s)\ne0$.

For $\operatorname{Re}s<0$, use the functional equation in the form
$$
\zeta(s)=2^{s}\pi^{s-1}\sin\!\left(\frac{\pi s}{2}\right)\Gamma(1-s)\,\zeta(1-s).
$$
Examine the factors:

* $2^{s}\pi^{s-1}$ is finite and non-zero everywhere.
* $\Gamma(1-s)$ is holomorphic and non-zero on $\operatorname{Re}s<0$, because its poles are at $1-s=0,-1,-2,\dots$,
  i.e. $s=1,2,3,\dots$, all with $\operatorname{Re}s>0$.
* $\zeta(1-s)$ has no zeros when $\operatorname{Re}(1-s)>1$, i.e. $\operatorname{Re}s<0$, by the first part.
* $\sin(\pi s/2)$ vanishes exactly at the even integers $s=2k$.

Hence on $\operatorname{Re}s<0$ the only zeros of the right side are at even integers $s=2k<0$, i.e.
$s=-2,-4,-6,\dots$; and each of these is genuinely a zero because the other factors at $s=-2k$ are finite and
non-zero. So the zeros of $\zeta$ with $\operatorname{Re}s<0$ are exactly $-2,-4,-6,\dots$, the trivial zeros.

The point $s=0$ is even but is *not* a zero: it lies on the boundary between the two regions, and there the zero of
$\sin$ is cancelled by the pole of $\zeta(1-s)$ at $s=1$, giving $\zeta(0)=-\frac12$ (Problem 24). Similarly the
remaining zeros must lie in $0<\operatorname{Re}s<1$. $\blacksquare$

**26.** *Strategy: three non-negative weights make a trigonometric polynomial that cannot vanish, and the
singularity of $\zeta$ at $s=1$ is strong enough to force a contradiction with it.*

**(a) Term-by-term logarithm.** For $\sigma>1$ the series $\sum_p p^{-s}$ converges absolutely and uniformly on
compact subsets of $\{\sigma>1\}$, and $\zeta$ has no zeros there (Problem 25). Hence $\log\zeta(s)$ is
holomorphic, and differentiating the uniformly convergent series
$\log\zeta(s)=\sum_p\sum_{k\ge1}\frac{1}{k}p^{-ks}$ term by term is legitimate by the Weierstrass theorem; each
term is holomorphic, and the differentiated series converges uniformly on compact subsets because
$\sum_{p,k}(\log p)p^{-k\sigma}\le\sum_n(\log n)n^{-\sigma}<\infty$ for $\sigma>1$.

**(b) The trigonometric identity.** Expanding $\cos2\theta=2\cos^{2}\theta-1$,
$$
3+4\cos\theta+\cos2\theta=3+4\cos\theta+2\cos^{2}\theta-1=2\left(1+2\cos\theta+\cos^{2}\theta\right)=2(1+\cos\theta)^{2}\ge0 .
$$

**(c) The limit at a hypothetical zero.** For $\sigma>1$ and real $t$, taking real parts,
$$
\log|\zeta(\sigma+it)|=\operatorname{Re}\sum_{p,k}\frac{p^{-k(\sigma+it)}}{k}
=\sum_{p,k}\frac{p^{-k\sigma}}{k}\cos\!\left(kt\log p\right).
$$
Apply (b) with $\theta=kt\log p$ and weight $p^{-k\sigma}/k>0$:
$$
3\log|\zeta(\sigma)|+4\log|\zeta(\sigma+it)|+\log|\zeta(\sigma+2it)|\ \ge\ 0,
\qquad\text{i.e.}\qquad
\left|\zeta(\sigma)\right|^{3}\left|\zeta(\sigma+it)\right|^{4}\left|\zeta(\sigma+2it)\right|\ \ge\ 1 .
$$
Suppose $\zeta(1+it_{0})=0$ with $t_{0}\ne0$. As $\sigma\downarrow1$:

* $|\zeta(\sigma)|^{3}\sim(\sigma-1)^{-3}$, from the simple pole;
* $|\zeta(\sigma+it_{0})|^{4}=O\left((\sigma-1)^{4}\right)$, since $\zeta$ has a zero at $1+it_{0}$ and is
  holomorphic there, so $\zeta(\sigma+it_{0})=O(\sigma-1)$;
* $|\zeta(\sigma+2it_{0})|=O(1)$, since $1+2it_{0}\ne1$ and $\zeta$ is holomorphic at $1+2it_{0}$.

Multiplying gives $O\left((\sigma-1)^{-3}(\sigma-1)^{4}\right)=O(\sigma-1)\to0$, contradicting the bound $\ge1$.

**(d) The case $t_{0}=0$.** At $s=1$ the function $\zeta$ has a pole, not a zero: $|\zeta(\sigma)|\to\infty$. So
there is no zero to exclude, and the argument of (c) is not needed. $\blacksquare$

**27.** *Strategy: the indicator of a residue class is averaged over characters; then only the principal character
contributes a singularity.*

For odd $n$, $\chi_{4}(n)=1$ if $n\equiv1$ and $-1$ if $n\equiv3\pmod4$, so
$\frac{1+\chi_{4}(n)}{2}=\mathbf{1}_{n\equiv1(4)}$. Multiplying by $n^{-s}$ and summing over odd $n$ (the primes
$p>2$ are odd, and $p=2$ contributes to neither class),
$$
\sum_{p\equiv1(4)}\frac{1}{p^{s}}=\frac12\sum_{p>2}\frac{1}{p^{s}}+\frac12\sum_{p>2}\frac{\chi_{4}(p)}{p^{s}} .
$$
For the second sum, the Euler product of $L(s,\chi_{4})$ gives, for $s>1$,
$$
\log L(s,\chi_{4})=\sum_p\sum_{k\ge1}\frac{\chi_{4}(p)^{k}}{k\,p^{ks}}=\sum_{p>2}\frac{\chi_{4}(p)}{p^{s}}+O(1),
$$
because $|\chi_{4}|\le1$ and the terms with $k\ge2$ are bounded in modulus by
$\sum_p\sum_{k\ge2}p^{-k\sigma}\le\sum_n n^{-2}=O(1)$ uniformly for $\sigma\ge1$. Since
$L(1,\chi_{4})=\frac{\pi}{4}\ne0$ (Example 9.7) and $L(s,\chi_{4})$ is continuous and non-zero near $s=1$, we have
$\log L(s,\chi_{4})=O(1)$ as $s\downarrow1$; hence $\sum_{p>2}\chi_{4}(p)/p^{s}=O(1)$.

The first sum is $\frac12\log\frac{1}{s-1}+O(1)$ by the principal-character computation (Theorem 7.28). Therefore
$$
\sum_{p\equiv1(4)}\frac{1}{p^{s}}=\frac12\log\frac{1}{s-1}+O(1)\longrightarrow\infty .
$$
The non-vanishing of $L(1,\chi_{4})$ enters exactly at the step $\log L(s,\chi_{4})=O(1)$: if $L(1,\chi_{4})$ were
$0$, the logarithm would blow up like $\log\frac{1}{s-1}$ with a negative coefficient, and the two classes would not
split the divergence evenly. $\blacksquare$

**28.** *Strategy: (a) is the observation that primes in $(n,2n]$ divide $\binom{2n}{n}$; (b) is an iteration of
(a); (c) converts the $\theta$-bound into a $\psi$-bound via Lemma 7.18.*

**(a)** A prime $p$ with $n<p\le2n$ divides $(2n)!$ but divides neither $n!$ nor the other $n!$, so $p$ divides
$\binom{2n}{n}$. Therefore
$$
\theta(2n)-\theta(n)=\sum_{n<p\le2n}\log p\ \le\ \log\binom{2n}{n}\ \le\ \log 2^{2n}=2n\log2,
$$
the middle inequality because $\binom{2n}{n}$ is one of the $2n+1$ terms summing to $2^{2n}$.

**(b)** Let $x\ge2$ and $n=\lfloor x/2\rfloor$. Then $x<2n+2$ and $\theta(x)\le\theta(2n)+\log x$ (the only prime
that could lie in $(2n,x]$ is $2n+1$). With (a),
$$
\theta(x)\le\theta(n)+2n\log2+\log x\le\theta\!\left(\frac x2\right)+x\log2+\log x .
$$
Iterate: after $k$ steps, while $x/2^{k}\ge2$,
$$
\theta(x)\le\sum_{j=0}^{k-1}\frac{x}{2^{j}}\log2+k\log x\le 2x\log2+k\log x .
$$
Choosing $k=\lfloor\log_2x\rfloor$ gives $k\log x\le(\log x)^{2}/\log2\le x\log2$ for $x\ge16$, so
$\theta(x)\le3x\log2$. For $2\le x<16$, check the inequality at the jump points $x=2,3,5,7,11,13$ of $\theta$; the largest value is $\theta(13)=\log(2\cdot3\cdot5\cdot7\cdot11\cdot13)=10.309\dots$, against $3\cdot13\cdot\log2=27.03\dots$, and the smaller jump points are further from the bound. So $\theta(x)\le3x\log2$ for all $x\ge2$.

**(c)** By Lemma 7.18 and (b), with $K=\lfloor\log_2x\rfloor$,
$$
\psi(x)=\sum_{k=1}^{K}\theta(x^{1/k})\le3\log2\sum_{k=1}^{K}x^{1/k}\le3\log2\left(x+K\sqrt x\right).
$$
For $x\ge16$ we have $K\le\sqrt x$, so $K\sqrt x\le x$ and $\psi(x)\le6x\log2\le6x$. For $2\le x<16$,
$\psi(x)\le\psi(15)=10.309\dots\le6x$. $\blacksquare$

**29.** *Strategy: the first implication is immediate from Lemma 7.18; the second is Abel summation, where the
integral term is $o(x/\log x)$ because $\theta(t)\ll t$.*

Since $\psi(x)=\theta(x)+O(\sqrt x\log x)$ and $\sqrt x\log x=o(x)$, $\psi(x)\sim x$ implies
$\theta(x)/x=\psi(x)/x+O(\sqrt x\log x/x)\to1$.

For the second, Abel summation (Problem 14) with $a_n=\log p$ for primes $p$ (and $0$ otherwise), so that
$A(t)=\theta(t)$, and $f(t)=1/\log t$ gives
$$
\pi(x)=\sum_{p\le x}\frac{1}{\log p}\log p=\frac{\theta(x)}{\log x}+\int_2^{x}\frac{\theta(t)}{t(\log t)^{2}}\,dt .
$$
Assume $\theta(t)\sim t$. Then $\theta(x)/\log x\sim x/\log x$. For the integral, fix $\varepsilon>0$ and use
$\theta(t)\le(1+\varepsilon)t$ for $t\ge T$:
$$
\int_T^{x}\frac{\theta(t)}{t(\log t)^{2}}dt\le(1+\varepsilon)\int_T^{x}\frac{dt}{(\log t)^{2}}
\le(1+\varepsilon)\frac{x}{(\log x)^{2}} ,
$$
the last inequality because $1/(\log t)^{2}$ is decreasing and the integral is dominated by the last interval
($\int_T^x dt/(\log t)^2\le x/(\log x)^2$ for $x\ge T\ge e$). The remaining piece $\int_2^T$ is a constant. Hence
the integral is $o(x/\log x)$, and
$$
\pi(x)=\frac{x}{\log x}+o\!\left(\frac{x}{\log x}\right)\sim\frac{x}{\log x}.
$$
$\blacksquare$

**30.** *Strategy: write $\varphi=\mu*\operatorname{id}$, interchange the two summations, and insert the asymptotics
of $\sum_{k\ge1}\mu(k)/k^{2}$.*

By Problem 11, $\varphi(n)=\sum_{d\mid n}\mu(d)\frac nd$. Hence
$$
\sum_{n\le x}\varphi(n)=\sum_{n\le x}\sum_{d\mid n}\mu(d)\frac nd=\sum_{d\le x}\mu(d)\sum_{m\le x/d}m .
$$
For $y\ge1$, $\sum_{m\le y}m=\frac12\lfloor y\rfloor(\lfloor y\rfloor+1)=\frac12y^{2}+O(y)$, so
$$
\sum_{n\le x}\varphi(n)=\frac{x^{2}}{2}\sum_{d\le x}\frac{\mu(d)}{d^{2}}+O\!\left(x\sum_{d\le x}\frac1d\right)
=\frac{x^{2}}{2}\sum_{d\le x}\frac{\mu(d)}{d^{2}}+O(x\log x).
$$
Now $\sum_{d\ge1}\mu(d)d^{-2}=1/\zeta(2)=6/\pi^{2}$ (Problem 7), and $|\mu(d)|\le1$ gives
$$
\left|\sum_{d>x}\frac{\mu(d)}{d^{2}}\right|\le\sum_{d>x}\frac{1}{d^{2}}=O\!\left(\frac1x\right),
$$
so the first term is $\frac{x^{2}}{2}\left(\frac{6}{\pi^{2}}+O\left(\frac1x\right)\right)=\frac{3}{\pi^{2}}x^{2}+O(x)$.
Combining,
$$
\sum_{n\le x}\varphi(n)=\frac{3}{\pi^{2}}x^{2}+O(x\log x).
$$
*Numerical check at $x=10$:* the values $\varphi(1),\dots,\varphi(10)$ are $1,1,2,2,4,2,6,4,6,4$, with sum $32$;
the formula gives $\frac{3}{\pi^{2}}\cdot100=30.396$, so the error is $1.604$, well inside $O(x\log x)$. $\blacksquare$

## Challenge

**31.** *Strategy: assume the reciprocal sum converges, cut off the tail, and show that the integers with all small
prime factors are too few to fill even half of $\{1,\dots,x\}$.*

Assume, for contradiction, that $\sum_p1/p=C<\infty$. Choose $N$ so large that
$$
\sum_{p>N}\frac1p<\frac12 ,
$$
and let $p_1<\dots<p_k$ be the primes at most $N$. Fix an integer $x\ge1$ and split
$$
A=\{1\le n\le x:\ \text{every prime factor of }n\text{ is }\le N\},\qquad
B=\{1,\dots,\lfloor x\rfloor\}\setminus A .
$$

**Size of $B$.** Each $n\in B$ is divisible by at least one prime $q>N$. Therefore
$$
\#B\ \le\ \sum_{\substack{q>N\\ q\le x}}\#\{n\le x:q\mid n\}
=\sum_{\substack{q>N\\ q\le x}}\left\lfloor\frac xq\right\rfloor
\le\ x\sum_{q>N}\frac1q\ <\ \frac x2 .
$$

**Size of $A$.** Write each $n\in A$ as $n=ab^{2}$ with $a$ squarefree: given the prime factorisation
$n=\prod_{p\le N}p^{e_p}$, take $b=\prod p^{\lfloor e_p/2\rfloor}$ and $a=\prod p^{e_p\bmod2}$. Then $a$ is
squarefree with all prime factors at most $N$, so there are at most $2^{k}$ choices for $a$; and $b\le\sqrt n\le\sqrt x$,
so there are at most $\sqrt x$ choices for $b$. The map $n\mapsto(a,b)$ is injective (indeed bijective onto its
image), hence
$$
\#A\ \le\ 2^{k}\sqrt x .
$$

**Contradiction.** If the integer $x$ satisfies $x\ge4\cdot4^{k}$ then $2^{k}\sqrt x\le\frac x2$, so
$$
x=\#A+\#B<\frac x2+\frac x2=x,
$$
which is absurd. Hence $\sum_p1/p$ diverges.

**Why divergence and not merely infinitude.** The argument uses the *tail* $\sum_{p>N}1/p$ being small, which is a
statement about the size of the reciprocal sum, not about the number of primes. Replacing the hypothesis by
"finitely many primes" would make the estimate $\#B\le x\sum_{q>N}1/q$ vacuous, since no such $q$ would exist and
$\#B=0$; the counting argument would then prove nothing. The strength comes from being able to choose $N$ with the
tail below $1/2$, which is exactly convergence of the series. $\blacksquare$

**32.** *Strategy: (a)–(c) treat real characters, where the Dirichlet series of $\zeta L(\chi)$ has non-negative
coefficients and Landau's theorem forbids a zero at $1$; (d) reduces the general case to a product with the same
property.*

**(a)** For real $\chi$ and $n=\prod p^{e_p}$,
$$
a_n=\sum_{d\mid n}\chi(d)=\prod_{p^{e}\parallel n}\left(1+\chi(p)+\dots+\chi(p)^{e}\right),
$$
by multiplicativity of $\chi$ and the bijection between divisors of $n$ and tuples of exponents. Each local factor
is non-negative: it is $e+1$ if $\chi(p)=1$, it is $1$ or $0$ if $\chi(p)=-1$ (the alternating sum $1-1+\dots$),
and it is $1$ if $\chi(p)=0$. Hence $a_n\ge0$. If $n=m^{2}$ then every $e_p$ is even, and the local factor is
$e_p+1\ge1$ or $1$; so $a_{m^{2}}\ge1$.

**(b)** Since $\zeta(s)L(s,\chi)=\left(\sum_n n^{-s}\right)\left(\sum_n\chi(n)n^{-s}\right)$ and both series
converge absolutely for $\operatorname{Re}s>1$, the product is $\sum_n a_nn^{-s}$. If $L(1,\chi)=0$, then the
simple pole of $\zeta$ at $s=1$ is cancelled by the zero of $L$, so $\zeta L(\chi)$ is holomorphic at $s=1$. It has
no other pole (the only pole of $\zeta$ is at $1$, and $L(s,\chi)$ is entire for non-principal $\chi$), so it is
entire.

**(c)** The series $\sum a_nn^{-s}$ converges for $\operatorname{Re}s>1$ and its sum extends holomorphically to
every real point (the entire function). By Theorem 7.13, applied at $\sigma=-1$, the series converges at $s=-1$.
Then $\sum_na_nn^{-1}<\infty$ forces $a_n/n\to0$, hence $a_n=0$ for all large $n$, contradicting $a_{m^{2}}\ge1$.
So $L(1,\chi)\ne0$.

**(d)** Let $\chi$ have order $d$ and put $G(s)=\prod_{j=0}^{d-1}L(s,\chi^{j})$. At a prime $p$ with
$\chi(p)\ne0$, write $\chi(p)=\zeta^{m}$ for a primitive $d$-th root of unity $\zeta$; the local factor of $G$ is
$$
\prod_{j=0}^{d-1}\left(1-\zeta^{mj}p^{-s}\right)^{-1}.
$$
The multiset $\{\zeta^{mj}:0\le j<d\}$ consists of the $(d/g)$-th roots of unity, each repeated $g=\gcd(m,d)$
times, so the local factor is $\left(1-p^{-(d/g)s}\right)^{-g}=\sum_{l\ge0}\binom{l+g-1}{g-1}p^{-(d/g)ls}$, whose
coefficients are non-negative. If $\chi(p)=0$ the local factor is $1$. Hence $G(s)=\sum c_nn^{-s}$ with $c_n\ge0$.

Because $\chi^{0}=\chi_0$ is principal and $\chi^{j}$ is non-principal for $1\le j<d$, the factor $L(s,\chi_0)$ has
a simple pole at $s=1$ and the other factors are holomorphic there; so $G$ has a simple pole at $s=1$. If some
$L(1,\chi^{j})$ vanished for $j\ge1$, the pole would be cancelled and $G$ would be holomorphic at $s=1$; since all
its factors are entire (the principal one having its only pole cancelled), $G$ would be entire. By Theorem 7.13
the series would converge at $s=-1$, forcing $c_n=0$ eventually, contradicting the pole. Hence no
$L(1,\chi^{j})$ vanishes at $1$, and in particular $L(1,\chi)\ne0$. $\blacksquare$

**33.** *Strategy: write $2^{\omega(n)}$ as a divisor sum, interchange summations, and use the squarefree
asymptotic of Problem 34.*

Every $n$ has exactly $2^{\omega(n)}$ squarefree divisors — the products of subsets of its distinct primes — so
$$
2^{\omega(n)}=\sum_{\substack{d\mid n\\ d\ \text{squarefree}}}1=\sum_{d\mid n}\mu^{2}(d).
$$
Therefore, with $\lfloor x/d\rfloor=x/d+O(1)$,
$$
\sum_{n\le x}2^{\omega(n)}=\sum_{n\le x}\sum_{d\mid n}\mu^{2}(d)=\sum_{d\le x}\mu^{2}(d)\left\lfloor\frac xd\right\rfloor
=x\sum_{d\le x}\frac{\mu^{2}(d)}{d}+O(x),
$$
the error being $O\left(\sum_{d\le x}1\right)=O(x)$.

For the remaining sum, use $\mu^{2}(d)=\sum_{k^{2}\mid d}\mu(k)$ (Problem 34) and interchange:
$$
\sum_{d\le x}\frac{\mu^{2}(d)}{d}=\sum_{k\le\sqrt x}\mu(k)\sum_{m\le x/k^{2}}\frac{1}{k^{2}m}
=\sum_{k\le\sqrt x}\frac{\mu(k)}{k^{2}}\left(\log\frac{x}{k^{2}}+\gamma+O\!\left(\frac{k^{2}}{x}\right)\right).
$$
Now $\sum_{k\le\sqrt x}\mu(k)k^{-2}=6/\pi^{2}+O(1/\sqrt x)$ and $\sum_k\mu(k)(\log k)k^{-2}$ converges absolutely,
so
$$
\sum_{d\le x}\frac{\mu^{2}(d)}{d}=\frac{6}{\pi^{2}}\log x+C+O\!\left(\frac{\log x}{\sqrt x}\right)
$$
for a constant $C$. Substituting,
$$
\sum_{n\le x}2^{\omega(n)}=x\left(\frac{6}{\pi^{2}}\log x+C+O\!\left(\frac{\log x}{\sqrt x}\right)\right)+O(x)
=\frac{6}{\pi^{2}}x\log x+O(x).
$$
$\blacksquare$

**34.** *Strategy: the indicator of squarefree integers is $\mu^{2}=\mu*\mathbf{1}$ evaluated at $n$, i.e.
$\mu^{2}(n)=\sum_{k^{2}\mid n}\mu(k)$; interchange the summation to get a main term plus a short tail.*

For every $n$, $\sum_{k^{2}\mid n}\mu(k)=\sum_{k\mid n}\mu(k)\cdot\mathbf{1}_{k\ \text{is a square}}$; more directly,
$\mu^{2}(n)=\prod_{p}\left(1-\mathbf{1}_{p^{2}\mid n}\right)=\sum_{k^{2}\mid n}\mu(k)$, the last equality because
the product over primes of $(1-\mathbf{1}_{p^{2}|n})$ expands over square divisors $k^{2}$ with coefficient
$\mu(k)$.

Hence, for $x\ge1$,
$$
\sum_{n\le x}\mu^{2}(n)=\sum_{n\le x}\sum_{k^{2}\mid n}\mu(k)=\sum_{k\le\sqrt x}\mu(k)\sum_{\substack{n\le x\\ k^{2}\mid n}}1
=\sum_{k\le\sqrt x}\mu(k)\left\lfloor\frac{x}{k^{2}}\right\rfloor .
$$
The interchange is legitimate because the sum has finitely many terms (only $k\le\sqrt x$ can contribute) and all
terms are finite. Now $\lfloor x/k^{2}\rfloor=x/k^{2}+O(1)$, so
$$
\sum_{n\le x}\mu^{2}(n)=x\sum_{k\le\sqrt x}\frac{\mu(k)}{k^{2}}+O\!\left(\sqrt x\right)
=x\left(\frac{6}{\pi^{2}}+O\!\left(\sum_{k>\sqrt x}\frac{1}{k^{2}}\right)\right)+O(\sqrt x).
$$
Finally $\sum_{k>\sqrt x}k^{-2}=O(1/\sqrt x)$, so both error terms are $O(\sqrt x)$ and
$$
\sum_{n\le x}\mu^{2}(n)=\frac{6}{\pi^{2}}x+O(\sqrt x).
$$
$\blacksquare$

**35.** *Strategy: compute the first two moments of $\omega$ over $\{1,\dots,x\}$, then apply Chebyshev's
inequality to the deviation from the mean.*

**(a)** Since $\omega(n)=\sum_{p\mid n}1$,
$$
\sum_{n\le x}\omega(n)=\sum_{p\le x}\left\lfloor\frac xp\right\rfloor
=x\sum_{p\le x}\frac1p+O(\pi(x))=x\left(\log\log x+M+O\!\left(\frac{1}{\log x}\right)\right)+O\!\left(\frac{x}{\log x}\right),
$$
using Mertens' estimate (Theorem 7.4) and $\pi(x)=O(x/\log x)$ (Chebyshev). Hence
$\sum_{n\le x}\omega(n)=x\log\log x+O(x)$.

**(b)** Similarly,
$$
\sum_{n\le x}\omega(n)^{2}=\sum_{n\le x}\sum_{p\mid n}\sum_{q\mid n}1=\sum_{p,q\le x}\left\lfloor\frac{x}{pq}\right\rfloor .
$$
Separate the diagonal $p=q$ and the off-diagonal:
$$
\sum_{p\le x}\left\lfloor\frac xp\right\rfloor=O(x\log\log x),\qquad
\sum_{\substack{p,q\le x\\ p\ne q}}\left\lfloor\frac{x}{pq}\right\rfloor
=x\sum_{\substack{p,q\le x\\ p\ne q}}\frac{1}{pq}+O\left(\#\{(p,q):pq\le x\}\right).
$$
The first sum is bounded by the computation of (a). For the second, $\sum_{p\ne q}1/(pq)=\left(\sum_{p\le x}1/p\right)^{2}-\sum_{p\le x}1/p^{2}=(\log\log x)^{2}+O(\log\log x)$,
and the number of pairs with $pq\le x$ is $O(x\log\log x)$: for $p\le\sqrt x$ use
$\pi(x/p)\le2x/(p\log x)$, summing to $O(x\log\log x/\log x)$, and for $p>\sqrt x$ (hence $q<\sqrt x$) count by $q$,
getting $\sum_{q<\sqrt x}\pi(x/q)\le x\sum_{q<\sqrt x}1/q=O(x\log\log x)$. Combining,
$$
\sum_{n\le x}\omega(n)^{2}=x(\log\log x)^{2}+O(x\log\log x).
$$

**(c)** The mean of $\omega$ over $\{1,\dots,x\}$ is $\mu_{x}=\frac1x\sum_{n\le x}\omega(n)=\log\log x+O(1)$, so
$$
\frac1x\sum_{n\le x}\left(\omega(n)-\log\log x\right)^{2}
=\frac1x\sum_{n\le x}\omega(n)^{2}-\left(\frac1x\sum_{n\le x}\omega(n)\right)^{2}+O(1)=O(\log\log x).
$$
By Chebyshev's inequality, for fixed $\varepsilon>0$,
$$
\frac{1}{x}\#\left\{n\le x:|\omega(n)-\log\log x|>\varepsilon\log\log x\right\}
\le\frac{O(\log\log x)}{\varepsilon^{2}(\log\log x)^{2}}=O\!\left(\frac{1}{\varepsilon^{2}\log\log x}\right)\to0 .
$$
So the exceptional set has density $0$, which is the Hardy–Ramanujan theorem.

**(d)** If $\varepsilon=\varepsilon(x)\to0$, the bound becomes $O(1/(\varepsilon^{2}\log\log x))$, which need not
tend to $0$ — for $\varepsilon=(\log\log x)^{-1/2}$ it is $O(1)$, and for smaller $\varepsilon$ it diverges. The
second-moment method therefore gives the correct normal order but not the distribution of the normalised
deviation. The Erdős–Kac theorem requires a genuine central limit theorem, i.e. control of all moments (or of the
characteristic function) of the dependent sum $\sum_{p\mid n}1$. $\blacksquare$

**36.** *Strategy: $\tau*\tau=\tau_{4}$, so the sum in question is a double divisor sum; estimate the inner
summatory function and then a weighted harmonic sum.*

Since $\tau=\mathbf{1}*\mathbf{1}$, associativity and commutativity of $*$ give
$$
\tau*\tau=(\mathbf{1}*\mathbf{1})*(\mathbf{1}*\mathbf{1})=\mathbf{1}*\mathbf{1}*\mathbf{1}*\mathbf{1}=\tau_{4}.
$$
Therefore
$$
\sum_{n\le x}\tau(n)^{2}=\sum_{n\le x}(\tau*\tau)(n)=\sum_{d\le x}\tau(d)\sum_{m\le x/d}\tau(m).
$$
Two elementary estimates are needed.

*(i) $\sum_{m\le y}\tau(m)\le Cy\log y$ for $y\ge2$.* Indeed $\sum_{m\le y}\tau(m)=\sum_{d\le y}\lfloor y/d\rfloor\le y\sum_{d\le y}1/d\le y(1+\log y)$
(Problem 5).

*(ii) $\sum_{d\le x}\tau(d)/d\le C'(\log x)^{2}$ for $x\ge2$.* Indeed
$$
\sum_{d\le x}\frac{\tau(d)}{d}=\sum_{d\le x}\frac1d\sum_{e\mid d}1=\sum_{e\le x}\frac1e\sum_{m\le x/e}\frac1m
\le\sum_{e\le x}\frac{1+\log(x/e)}{e}\le(1+\log x)\sum_{e\le x}\frac1e\le(1+\log x)^{2}.
$$

Combining (i) with $y=x/d$, and noting that $\log(x/d)\le\log x$,
$$
\sum_{n\le x}\tau(n)^{2}\ \le\ C\sum_{d\le x}\tau(d)\cdot\frac xd\log\frac xd
\ \le\ Cx\log x\sum_{d\le x}\frac{\tau(d)}{d}
\ \le\ CC'\,x(\log x)^{3}.
$$
Hence $\sum_{n\le x}\tau(n)^{2}\ll x(\log x)^{3}$. $\blacksquare$

*Remark.* In fact $\sum_{n\le x}\tau(n)^{2}\sim\frac{1}{\pi^{2}}x(\log x)^{3}$; the constant requires the
asymptotic $\sum_{d\le x}\tau(d)/d=\frac12(\log x)^{2}+O(\log x)$, obtained by refining (ii) with
$\sum_{m\le y}1/m=\log y+\gamma+O(1/y)$. The problem only asks for the order of magnitude.

<!--END-->

