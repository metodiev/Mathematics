# Arithmetic Functions — Exercises

> [Arithmetic Functions](README.md) · 36 problems · Beginner → Challenge · Solutions: [solutions.md](solutions.md)

Attempt every problem in writing before looking at [solutions.md](solutions.md). Each problem names the section of the tutorial that supplies the technique.

Notation: $d(n)$ is the number of positive divisors of $n$; $\sigma(n)$ the sum of the positive divisors; $\varphi$ Euler's totient; $\mu$ the Möbius function; $\omega(n)$ the number of distinct prime factors and $\Omega(n)$ the number counted with multiplicity; $\operatorname{rad}(n) = \prod_{p\mid n}p$ is the radical (product of the distinct primes). Convolution is $(f*g)(n)=\sum_{d\mid n}f(d)g(n/d)$, and $\varepsilon$ is the convolution identity $\varepsilon(n)=[n=1]$. All functions are multiplicative or completely multiplicative **in the sense of Definition 5.2.1**, and "multiplicative" excludes the zero function.

Where a problem asks you to *prove* something, a complete proof is expected; where it asks you to *compute*, show the factorisation you used.

## Beginner

**1.** *(§7.3, §7.4)* For each $n$, compute $d(n)$, $\sigma(n)$ and $\varphi(n)$ from the prime factorisation, showing the three formulas you use.

(a) $n = 18$
(b) $n = 45$
(c) $n = 100$
(d) $n = 210$

**2.** *(§5.2)* Classify each function as (i) multiplicative but not completely multiplicative, (ii) completely multiplicative, (iii) additive but not completely additive, (iv) completely additive, or (v) none of these. Justify each answer, giving an explicit numerical counterexample whenever the stronger property fails.

(a) $d(n)$
(b) $\sigma(n)$
(c) $\varphi(n)$
(d) $\mu(n)$
(e) $n \mapsto n^{3}$
(f) $\omega(n)$
(g) $\Omega(n)$
(h) $n \mapsto (-1)^{n}$
(i) $n \mapsto 2^{\omega(n)}$

**3.** *(§7.5)*

(a) Tabulate $\mu(n)$ for $1 \le n \le 20$.
(b) List the $n \le 20$ with $\mu(n) = -1$, and the $n \le 20$ with $\mu(n) = 0$.
(c) Explain in one sentence why $\mu(n) = 0$ does not mean that $n$ is composite.

**4.** *(§7.3, §7.4)* Compute $d(n)$, $\sigma(n)$ and $\varphi(n)$ for

(a) $n = 720 = 2^{4}\cdot 3^{2}\cdot 5$,
(b) $n = 1001 = 7\cdot 11\cdot 13$.

For (b) also verify $\sigma(1001)$ by an independent method (for instance, by pairing divisors or by enumerating them).

**5.** *(§7.4)* Compute $\varphi(n)$ for $n = 12,\ 25,\ 36,\ 60,\ 97,\ 128$. Then verify $\varphi(25) = 20$ by listing the integers in $\{1,\dots,25\}$ that are coprime to $25$.

**6.** *(§5.5, §7.8)* Classify each of $6,\ 16,\ 28,\ 45,\ 496,\ 945$ as perfect, abundant or deficient, computing $\sigma(n)$ in each case. Which of these numbers is the smallest odd abundant number?

**7.** *(§5.4, §7.3, §7.5)* Compute, showing every term of each convolution sum:

(a) $(d*\mu)(10)$
(b) $(\varphi*1)(10)$
(c) $(\mu*\mu)(10)$

For each answer, say which general identity it confirms.

**8.** *(§7.4)* Verify $\sum_{d\mid 20}\varphi(d) = 20$ by listing all divisors of $20$ and their totients. Then explain the bijective reason why the identity must hold in general (the argument with fractions in lowest terms).

**9.** *(§7.3)* Find **all** $n \le 50$ with $d(n) = 4$. Then prove that $d(n) = 4$ if and only if $n = p^{3}$ or $n = pq$ for distinct primes $p, q$.

**10.** *(§7.3)* Compute $\sigma(2^{10})$. Prove that $\sigma(2^{a})$ is odd for every $a \ge 0$, and contrast this with $\sigma(3^{a})$, which is odd exactly when $a$ is even.

**11.** *(§7.4)* Verify multiplicativity of $\varphi$ at $(m,n) = (8,9)$ by computing all three numbers. Then show that multiplicativity fails at $(m,n) = (2,4)$, and explain which hypothesis of Theorem 7.4.3 is violated.

**12.** *(§7.5)* Compute $\sum_{d\mid 36}\mu(d)$, $\sum_{d\mid 36}\mu^{2}(d)$, and the number of squarefree divisors of $36$. Check that your last two answers agree, and explain why they must.

## Intermediate

**13.** *(§7.1)* Let $f$ be multiplicative and define $g(n) = f(n^{2})$. Prove that $g$ is multiplicative. Then compute $g$ for $f = \mu$, and identify $g$ among the standard functions.

**14.** *(§7.1)* Prove the following criterion: an arithmetic function $f$ is multiplicative if and only if $f(1) = 1$ and

$$f\!\left(p_1^{a_1}\cdots p_r^{a_r}\right) = f(p_1^{a_1})\cdots f(p_r^{a_r})$$

for every choice of distinct primes $p_1,\dots,p_r$ and exponents $a_i \ge 1$. Both directions are required.

**15.** *(§7.3)* Prove that $d(n)$ is odd if and only if $n$ is a perfect square, using the **pairing** argument ($d$ paired with $n/d$) rather than the product formula. Then list all $n \le 100$ with $d(n)$ odd, and check the count against the list of squares.

**16.** *(§7.3)* Prove that $\sigma(n)$ is odd if and only if $n$ is a perfect square or twice a perfect square. Then check the criterion at $n = 18$ and at $n = 50$, computing $\sigma$ both times.

**17.** *(§7.5)* Prove that the number of squarefree divisors of $n$ is $2^{\omega(n)}$, and compute $\sum_{d\mid 360}\mu^{2}(d)$ and $\sum_{d\mid 360}|\mu(d)|$. Are the two sums always equal?

**18.** *(§5.4)* Prove that $(f*g)(n) = \sum_{ab=n}f(a)g(b)$, where the sum runs over ordered pairs of positive integers with product $n$. Deduce that $d*d$ is the function $\tau_4$ counting ordered quadruples $(a,b,c,e)$ of positive integers with $abce = n$, and compute $\tau_4(12)$ both by the convolution formula $\sum_{d\mid 12}d(d)\,d(12/d)$ and by listing the quadruples.

**19.** *(§7.4)* Prove that $\varphi(n)$ is even for every $n \ge 3$. Then solve $\varphi(n) = 2$ and $\varphi(n) = 4$ completely, proving that your lists are exhaustive.

**20.** *(§7.6)* Prove that $\sigma(n) = n\sum_{d\mid n}\frac{1}{d}$ for every $n \ge 1$. Use it to compute $\sigma(360)/360$ and check the answer against $\sigma(360) = 1170$.

**21.** *(§7.6)* Let $f$ be completely multiplicative and nowhere zero. Prove that

$$(f\cdot g)*(f\cdot h) = f\cdot(g*h)$$

for all $g,h$. Deduce that $\operatorname{id}*\operatorname{id} = \operatorname{id}\cdot d$, i.e. $\sum_{d\mid n}d\cdot\frac nd = n\,d(n)$, and verify the identity at $n = 6$.

**22.** *(§7.6)* Prove that the Dirichlet inverse of $\operatorname{id}$ is $n\mapsto \mu(n)n$. Then compute $\operatorname{id}^{-1}(12)$ from the recursion of Theorem 7.6.2 and confirm it agrees with $\mu(12)\cdot 12$.

**23.** *(§7.5)* Prove that $\sum_{d\mid n}\mu(d)\left\lfloor\frac nd\right\rfloor = \varphi(n)$ for every $n\ge1$, and verify it for $n = 100$.

**24.** *(§7.6)* Prove that the Dirichlet inverse of $d$ is $\mu*\mu$. Determine $\mu*\mu$ at every prime power, deduce its value at squarefree $n$, compute $d^{-1}(12)$, and verify $(d*d^{-1})(12) = \varepsilon(12)$ term by term.

## Advanced

**25.** *(§7.7)* Prove the exact formula

$$\sum_{n\le N}d(n) = 2\sum_{k\le\sqrt N}\left\lfloor\frac Nk\right\rfloor - \left\lfloor\sqrt N\right\rfloor^{2},$$

including a careful justification that the union of the two regions is the whole lattice-point set. Then compute $\sum_{n\le 50}d(n)$ with it and check against direct enumeration.

**26.** *(§7.7, §7.9)* Prove that $\sum_{n\le x}\mu^{2}(n) = \frac{6}{\pi^{2}}x + O(\sqrt x)$, where $\mu^{2}$ is the indicator of squarefree numbers. (You may quote $\sum_{d\ge1}\mu(d)/d^{2} = 6/\pi^{2}$, which follows from the Euler product at $s=2$.) Evaluate the formula at $x = 100$ against the true count.

**27.** *(§7.6)* Prove that the ring $\mathcal{A}$ of arithmetic functions has no zero divisors, and deduce that $f*g = 0$ implies $f=0$ or $g=0$. Then exhibit a zero divisor in the *different* ring consisting of all functions $\mathbb{N}\to\mathbb{Z}$ with pointwise multiplication, to show that the property is a feature of convolution and not of the underlying set.

**28.** *(§7.1)* Let $f$ be multiplicative and suppose $f(p^{a}) = f(p)^{a}$ for every prime $p$ and every $a\ge1$. Prove that $f$ is completely multiplicative.

**29.** *(§7.6)* Prove that the Dirichlet inverse of $\varphi$ is $n\mapsto\sum_{d\mid n}\mu(d)\,d$, and verify the value at $n = 30$ in two ways: from the formula and from the recursion.

**30.** *(§7.8)* Prove the "only if" direction of the Euclid–Euler theorem: if $N$ is even and perfect, then $N = 2^{p-1}(2^{p}-1)$ with $2^{p}-1$ prime. Your proof must justify (i) that $2^{p}-1$ divides the odd part of $N$, (ii) that the cofactor is $1$, and (iii) that $p$ is prime.

**31.** *(§7.6)* Prove that for $n \ge 2$,

$$\sum_{d\mid n}\mu(d)\,\sigma(d) = (-1)^{\omega(n)}\operatorname{rad}(n).$$

Check the formula at $n = 12$ and at $n = 720$.

## Challenge

**32.** *(§7.7, §7.9)* Prove that $\sum_{n\le x}\varphi(n) = \frac{3}{\pi^{2}}x^{2} + O(x\log x)$ in full, starting from $\varphi = \mu*\operatorname{id}$ and using $\sum_{d\le x}1/d^{2} = \pi^{2}/6 + O(1/x)$. Be explicit about where each error term comes from.

**33.** *(§7.6)* Prove that the Dirichlet inverse of a multiplicative function is multiplicative. Give a complete proof — including the claim that $f*g$ is multiplicative when $f$ and $g$ are — and explain why the argument is *not* circular.

**34.** *(§7.3, §7.8)* Prove that a perfect number is never a perfect square. (Use the parity criterion of Corollary 7.3.5.)

**35.** *(§7.8)* Prove that every even perfect number ends in the digit $6$ or the digit $8$. (Hint: split according to $p \bmod 4$ and compute $2^{p-1}$ and $2^{p}-1$ modulo $10$.)

**36.** *(§7.8)* Prove Euler's form of an odd perfect number: if $n$ is odd and perfect, then $n = p^{a}m^{2}$ where $p$ is an odd prime, $\gcd(p,m)=1$, and $p \equiv a \equiv 1 \pmod 4$. Explain clearly where the assumption that $n$ is odd is used, and why the argument does not produce any odd perfect number.
