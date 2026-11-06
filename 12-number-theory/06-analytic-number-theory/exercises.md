# Analytic Number Theory — Exercises

> [Analytic Number Theory](README.md) · 36 problems · Beginner → Challenge · Solutions: [solutions.md](solutions.md)

Every problem is a proof unless it asks for a computation. A computation is complete only when the estimate or
identity used is named and its hypotheses are checked; a proof is complete only when every quoted theorem is
stated precisely enough to be applied. You may use anything proved in the [tutorial](README.md). Results that the
tutorial only states — Mertens' estimates (Theorem 7.4), the prime number theorem, the explicit formula
(Theorem 7.23), the Wiener–Ikehara theorem, the classical zero-free region — may be quoted, but only by name and
with their hypotheses verified. Problems that ask you to supply the details of a quoted proof say so explicitly.

Notation is that of the tutorial: $\zeta$ is the Riemann zeta function, $\mu$ the Möbius function, $\Lambda$ the
von Mangoldt function, $\tau=\mathbf{1}*\mathbf{1}$, $\sigma=\operatorname{id}*\mathbf{1}$,
$\varphi=\mu*\operatorname{id}$, $\theta(x)=\sum_{p\le x}\log p$, $\psi(x)=\sum_{n\le x}\Lambda(n)$,
$\pi(x)=\sum_{p\le x}1$, and $\gamma=0.5772156649\dots$ is Euler's constant. The reference *(§7.k)* points to the
section of the tutorial that the problem exercises.

Do not open [solutions.md](solutions.md) before writing an attempt of your own.

## Beginner

**1.** *(§7.2)* Compute $\tau(360)$, $\sigma(360)$, $\varphi(360)$ and $\mu(360)$, showing the factorisation you
use. Verify $\sum_{d\mid360}\varphi(d)=360$ for the value you obtain.

**2.** *(§7.2)* (a) Prove that $f(n)=n^{2}$ is completely multiplicative. (b) Prove that if $f$ and $g$ are
multiplicative then so is their pointwise product $fg$, and that $f(1)=g(1)=1$. (c) Prove that if $f$ and $g$ are
multiplicative then $f*g$ is multiplicative.

**3.** *(§7.2)* Prove directly from Definition 5.4 that $(\mu*\mathbf{1})(n)=\varepsilon(n)$ for all $n$, and use
the identity $\varphi=\mu*\operatorname{id}$ to compute $\varphi(12)$ as a sum over divisors of $12$.

**4.** *(§7.5)* Compute $\sum_{n\le10}\Lambda(n)$ and check that it equals $\log\operatorname{lcm}(1,2,\dots,10)$.
Then state the general identity relating $\psi(x)$ to a least common multiple.

**5.** *(§7.1)* Using only the comparison of $\sum_{n\le x}1/n$ with $\int_1^{x+1}dt/t$ and $\int_1^{x}dt/t$, prove
that
$$
\log x\le\sum_{n\le x}\frac1n\le 1+\log x\qquad(x\ge1).
$$
Deduce $\sum_{n\le x}1/n=\log x+O(1)$ with an explicit constant in the $O$.

**6.** *(§7.2)* Compute $\sum_{n\le20}\tau(n)$ twice: once by counting divisors of each $n\le20$, and once by the
hyperbola identity of Theorem 7.7. Compare with $x\log x+(2\gamma-1)x$.

**7.** *(§7.4)* Prove that $\sum_{n\ge1}\mu(n)n^{-2}=1/\zeta(2)=6/\pi^{2}$ by comparing Euler products, stating
precisely the half-plane in which the manipulation is legitimate. Deduce that the density of squarefree integers
would be $6/\pi^{2}$ if the limit defining density exists.

**8.** *(§7.3)* For the Dirichlet series $\sum_{n\ge1}(-1)^{n}n^{-s}$, determine $\sigma_{c}$ and $\sigma_{a}$ and
identify the sum as a simple multiple of $\zeta(s)$. Explain why the two abscissae differ.

**9.** *(§7.4)* Prove that for $s>1$,
$$
1+\frac{1}{s-1}\ \ge\ \zeta(s)\ \ge\ \frac{1}{s-1},
$$
and deduce $\zeta(s)=O\!\left(\frac{1}{s-1}\right)$ as $s\downarrow1$.

**10.** *(§7.1)* Prove that $\sum_{p}1/p^{2}$ converges and that its value is at most $\pi^{2}/6-1$. Explain why
this does not contradict the divergence of $\sum_{p}1/p$.

## Intermediate

**11.** *(§7.2)* Prove that for $n\ge1$,
$$
\varphi(n)=n\sum_{d\mid n}\frac{\mu(d)}{d},
$$
and deduce $\varphi=\mu*\operatorname{id}$.

**12.** *(§7.2)* Prove that $\sum_{d\mid n}\varphi(d)=n$ for every $n\ge1$, both (a) by Möbius inversion from
Problem 11 and (b) by counting the fractions $1/n,2/n,\dots,n/n$ according to their denominator in lowest terms.

**13.** *(§7.2)* Prove that the set $\mathcal{A}$ of arithmetic functions is an integral domain under Dirichlet
convolution, and that $f$ is a unit if and only if $f(1)\ne0$. Exhibit the inverse of $\mathbf{1}$ and the inverse
of $\operatorname{id}$.

**14.** *(§7.2)* Prove the Abel summation formula: if $(a_{n})_{n\ge1}$ is a sequence of complex numbers,
$A(x)=\sum_{n\le x}a_{n}$, and $f:[1,\infty)\to\mathbb{C}$ is continuously differentiable, then
$$
\sum_{n\le x}a_{n}f(n)=A(x)f(x)-\int_1^{x}A(t)f'(t)\,dt .
$$

**15.** *(§7.2)* Use Abel summation with $a_{n}=1$ and $f(t)=\log t$ to prove
$$
\sum_{n\le x}\log n=x\log x-x+O(\log x).
$$

**16.** *(§7.5)* Prove that $\theta(x)\le\pi(x)\log x$, and prove that
$$
\pi(x)\ \le\ \frac{2\,\theta(x)}{\log x}+\sqrt x .
$$
Deduce from Chebyshev's bounds that $\pi(x)\asymp x/\log x$, being explicit about which bound gives which
inequality.

**17.** *(§7.5)* Prove that for $x\ge2$,
$$
\psi(x)=\sum_{k\ge1}\theta\!\left(x^{1/k}\right),\qquad \psi(x)=\theta(x)+O\!\left(\sqrt x\log x\right),
$$
stating where the bound on $\theta$ is used and why the sum is finite.

**18.** *(§7.2)* Prove that
$$
\sum_{n\le x}\sigma(n)=\sum_{d\le x}d\left\lfloor\frac xd\right\rfloor,
$$
and deduce $\sum_{n\le x}\sigma(n)=\frac{\pi^{2}}{12}x^{2}+O(x\log x)$.

**19.** *(§7.7)* Let $\chi_{3}$ be the non-principal character modulo $3$, so $\chi_{3}(n)=1$ if $n\equiv1$,
$\chi_{3}(n)=-1$ if $n\equiv2$, and $\chi_{3}(n)=0$ if $3\mid n$. Prove that $L(1,\chi_{3})>0$ by grouping the
series in pairs, and identify the resulting series as a sum of positive terms.

**20.** *(§7.3)* Prove that $\sum_{n\ge1}\mu(n)n^{-s}=1/\zeta(s)$ for $\operatorname{Re}s>1$, justifying the
manipulation of the Euler product. What are $\sigma_{c}$ and $\sigma_{a}$ of this series?

## Advanced

**21.** *(§7.5)* Prove in full that for $n\ge3$,
$$
\psi(2n)\ \ge\ 2n\log2-\log(2n+1)\ \ge\ n\log2,
$$
and deduce $\psi(x)\ge\frac{\log2}{2}x$ for even $x\ge6$. Explain precisely why the argument gives nothing for
odd $x$ and how the odd case is recovered.

**22.** *(§7.1)* Prove that
$$
\prod_{p\le x}\left(1-\frac1p\right)^{-1}\ \ge\ \sum_{n\le x}\frac1n,
$$
and deduce
$$
\sum_{p\le x}\frac1p\ \ge\ \log\log x-\frac12\qquad(x\ge3).
$$
This gives a second, quantitative proof that $\sum_{p}1/p$ diverges.

**23.** *(§7.4)* Prove that for $\operatorname{Re}s>1$,
$$
\zeta(s)=\frac{s}{s-1}-s\int_1^{\infty}\{x\}\,x^{-s-1}\,dx,
$$
by summing the identity $s\int_{n}^{n+1}\lfloor x\rfloor x^{-s-1}dx=n\left(n^{-s}-(n+1)^{-s}\right)$ over $n$, and
deduce $\lim_{s\to1}(s-1)\zeta(s)=1$.

**24.** *(§7.4)* Using the functional equation, compute $\zeta(0)$ and $\zeta(-1)$. Explain why substituting
$s=0$ directly into the asymmetric form is not legitimate, and perform the necessary limit.

**25.** *(§7.4)* Prove that $\zeta(s)\ne0$ for $\operatorname{Re}s>1$, and use the functional equation together
with the pole structure of $\Gamma$ to prove that every zero of $\zeta$ with $\operatorname{Re}s<0$ is one of
$-2,-4,-6,\dots$.

**26.** *(§7.6)* Supply the details of the proof that $\zeta(s)\ne0$ when $\operatorname{Re}s=1$: (a) justify
differentiating the logarithm of the Euler product term by term; (b) verify the identity
$3+4\cos\theta+\cos2\theta=2(1+\cos\theta)^{2}$; (c) carry out the limiting argument at a hypothetical zero
$1+it_{0}$ with $t_{0}\ne0$; (d) explain why $t_{0}=0$ is not a zero.

**27.** *(§7.7)* For the character $\chi_{4}$ modulo $4$ (defined in Example 9.7 of the tutorial), prove carefully
that
$$
\sum_{p\equiv1\ (4)}\frac{1}{p^{s}}=\frac12\sum_{p>2}\frac{1}{p^{s}}+\frac12\sum_{p>2}\frac{\chi_{4}(p)}{p^{s}},
$$
and deduce that the left side equals $\frac12\log\frac{1}{s-1}+O(1)$ as $s\downarrow1$. State where the
non-vanishing of $L(1,\chi_{4})$ enters.

**28.** *(§7.5)* Complete the details of the upper bound in Chebyshev's theorem: (a) prove
$\theta(2n)-\theta(n)\le2n\log2$; (b) prove by iteration that $\theta(x)\le3x\log2$ for $x\ge16$, and check
$2\le x<16$ directly; (c) prove $\psi(x)\le6x$ for $x\ge2$.

**29.** *(§7.5)* Prove that $\psi(x)\sim x$ implies $\theta(x)\sim x$, and that $\theta(x)\sim x$ implies
$\pi(x)\sim x/\log x$. In the second part use Abel summation explicitly and show that the integral term is
$o(x/\log x)$.

**30.** *(§7.2)* Prove $\sum_{n\le x}\varphi(n)=\frac{3}{\pi^{2}}x^{2}+O(x\log x)$ with all error terms
controlled, and check the formula numerically at $x=10$.

## Challenge

**31.** *(§7.1)* Write out Erdős's elementary proof that $\sum_{p}1/p$ diverges in full detail: state the choice
of $N$, prove that at most $x/2$ integers $\le x$ have a prime factor exceeding $N$, prove that at most
$2^{k}\sqrt x$ integers $\le x$ have all prime factors at most $N$, and explain why a contradiction follows for
large $x$. Then explain why this argument proves *divergence* and not merely infinitude.

**32.** *(§7.7)* Prove that $L(1,\chi)\ne0$ for every non-principal character $\chi$ by the following steps.
(a) For real $\chi$, set $a_{n}=\sum_{d\mid n}\chi(d)$ and prove $a_{n}\ge0$ with $a_{m^{2}}\ge1$. (b) Show that
$\zeta(s)L(s,\chi)=\sum a_{n}n^{-s}$ and that if $L(1,\chi)=0$ then this function is entire. (c) Use Theorem 7.13
at $s=-1$ to derive a contradiction. (d) For a general $\chi$ of order $d$, consider
$G(s)=\prod_{j=0}^{d-1}L(s,\chi^{j})$ and prove that its Dirichlet coefficients are non-negative; then repeat
the argument.

**33.** *(§7.9)* Prove that
$$
\sum_{n\le x}2^{\omega(n)}=\frac{6}{\pi^{2}}\,x\log x+O(x).
$$
You may use Problem 34 and the estimate $\sum_{n\le x}1/n=\log x+\gamma+O(1/x)$.

**34.** *(§7.9)* Prove that
$$
\sum_{n\le x}\mu^{2}(n)=\frac{6}{\pi^{2}}x+O\!\left(\sqrt x\right),
$$
by writing $\mu^{2}(n)=\sum_{k^{2}\mid n}\mu(k)$ and interchanging the order of summation. Justify the
interchange and the tail estimate.

**35.** *(§7.9)* (Turán's proof.) Let $\omega(n)$ be the number of distinct prime factors of $n$.
(a) Prove $\sum_{n\le x}\omega(n)=x\log\log x+O(x)$ using Mertens' estimate for $\sum_{p\le x}1/p$.
(b) Prove $\sum_{n\le x}\omega(n)^{2}=x(\log\log x)^{2}+O(x\log\log x)$.
(c) Deduce by Chebyshev's inequality that for every fixed $\varepsilon>0$,
$$
\#\{n\le x:\ |\omega(n)-\log\log x|>\varepsilon\log\log x\}=o(x).
$$
(d) Explain which step fails if $\varepsilon$ is allowed to depend on $x$, and why the argument therefore does not
prove the Erdős–Kac theorem.

**36.** *(§7.9)* Prove that
$$
\sum_{n\le x}\tau(n)^{2}\ \ll\ x(\log x)^{3},
$$
by using $\tau*\tau=\tau_{4}=\mathbf{1}*\mathbf{1}*\mathbf{1}*\mathbf{1}$ and estimating the resulting double sum.
State the two elementary estimates you need and prove them.

<!--END-->
