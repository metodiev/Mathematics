# Sequences and Series — Exercises

> [Sequences and Series](README.md) · 40 problems · Beginner → Challenge · Solutions: [solutions.md](solutions.md)

Work through the problems in order. Each cites the section of the tutorial it draws on. Before using a test,
write down its hypotheses; several problems are designed to punish a skipped hypothesis. Unless stated
otherwise, all series start at $n=1$ or at the index shown, logarithms are natural, and a numerical
"sanity check" (a few partial sums) is expected wherever a convergence claim is made.

Notation follows [MATHEMATICAL_NOTATION.md](../../MATHEMATICAL_NOTATION.md).

## Beginner

**1.** *(§7.1)* Compute $\displaystyle\lim_{n\to\infty}\frac{3n^2+2}{n^2-n+1}$, justifying each step with a
limit law.

**2.** *(§7.1)* Compute $\displaystyle\lim_{n\to\infty}\left(1+\frac{2}{n}\right)^n$.

**3.** *(§7.2)* Find $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n(n+3)}$ by computing the partial sums.

**4.** *(§7.2)* Evaluate $\displaystyle\sum_{n=1}^{\infty}\left(-\frac35\right)^n$.

**5.** *(§7.2)* Show that $\displaystyle\sum_{n=1}^{\infty}\frac{n}{2n+1}$ diverges, naming the test used.

**6.** *(§7.4)* Decide whether each series converges: (a) $\displaystyle\sum_{n=1}^{\infty}\frac{1}{\sqrt[3]{n^2}}$;
(b) $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n^{4/3}}$.

**7.** *(§7.5)* Show that $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n^2+1}$ converges and that its sum is less
than $2$.

**8.** *(§7.5)* Decide whether $\displaystyle\sum_{n=1}^{\infty}\frac{2n+1}{n^3+1}$ converges.

**9.** *(§7.6)* Decide whether $\displaystyle\sum_{n=1}^{\infty}\frac{n^2}{3^n}$ converges.

**10.** *(§7.7)* Decide whether $\displaystyle\sum_{n=1}^{\infty}\left(\frac{n}{3n+1}\right)^{n}$ converges.

**11.** *(§7.8)* For $\displaystyle\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{2n-1}$, decide convergence and whether
it is absolute or conditional.

**12.** *(§7.9)* Find the radius and the interval of convergence of
$\displaystyle\sum_{n=0}^{\infty}\frac{x^n}{(n+1)!}$.

## Intermediate

**13.** *(§7.2)* Evaluate $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n^2+3n+2}$.

**14.** *(§7.5)* Decide whether $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n\sqrt{n+1}}$ converges.

**15.** *(§7.4)* Decide whether $\displaystyle\sum_{n=3}^{\infty}\frac{1}{n\ln n\ln\ln n}$ converges.

**16.** *(§7.8)* For $\displaystyle\sum_{n=1}^{\infty}\frac{(-1)^n n}{n^2+1}$, decide convergence and whether
it is absolute or conditional.

**17.** *(§7.6)* Decide whether $\displaystyle\sum_{n=1}^{\infty}\frac{n!}{n^n}$ converges.

**18.** *(§7.7)* Decide whether $\displaystyle\sum_{n=2}^{\infty}\left(1-\frac1n\right)^{n^2}$ converges.

**19.** *(§7.9)* Find the interval of convergence of $\displaystyle\sum_{n=1}^{\infty}\frac{(x+2)^n}{n\,4^n}$,
testing both endpoints.

**20.** *(§7.9)* Find the radius of convergence of $\displaystyle\sum_{n=1}^{\infty}\frac{n!\,x^n}{n^n}$.

**21.** *(§7.11)* Write the Maclaurin series of $f(x)=x^2e^{-x}$, state its radius of convergence, and
compute $f^{(5)}(0)$.

**22.** *(§7.12)* Evaluate $\displaystyle\lim_{x\to0}\frac{1-\cos x}{x^2}$ using series.

**23.** *(§7.12)* Evaluate $\displaystyle\lim_{x\to0}\frac{x-\sin x}{x^3}$ using series.

**24.** *(§7.12)* Use the binomial series to approximate $\sqrt{1.1}$ by $1+\frac{x}{2}-\frac{x^2}{8}$ at
$x=0.1$, and bound the error with the alternating series estimate.

## Advanced

**25.** *(§7.5)* Let $a_n>0$ and suppose $\sum a_n$ converges. Prove that $\sum a_n^2$ converges. Show by
example that the converse fails.

**26.** *(§7.8)* Give an example of a convergent series whose series of absolute values diverges, prove that
your example has both properties, and state what this implies about rearrangements.

**27.** *(§7.2)* Prove that the harmonic series diverges by grouping terms into blocks of lengths
$1,1,2,4,8,\dots$, and deduce that $\sum_{n\ge1}\frac{1}{2n-1}$ diverges.

**28.** *(§7.5)* Prove the case $c=0$ of the limit comparison test: if $a_n>0$, $b_n>0$, $a_n/b_n\to0$ and
$\sum b_n$ converges, then $\sum a_n$ converges. Apply it to $\sum_{n\ge1}\ln\left(1+\frac{1}{n^2}\right)$,
using $\ln(1+u)\le u$ for $u\ge0$.

**29.** *(§7.6, §7.7)* Let $a_n>0$ and suppose $a_{n+1}/a_n\to L$. Prove that $a_n^{1/n}\to L$. Then exhibit a
sequence for which the root test proves convergence while the ratio test is inconclusive. *Hint for the
first part:* write $\ln a_n$ as a sum of logarithms of ratios and use the fact that the averages of a
convergent sequence converge to the same limit.

**30.** *(§7.8)* For $\displaystyle\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{n^3}$, find the least $N$ such that
the alternating-series bound guarantees $|S-S_N|<10^{-3}$, and compute $S_{10}$.

**31.** *(§7.9)* Find the interval of convergence of
$\displaystyle\sum_{n=1}^{\infty}\frac{(2x-1)^n}{n\,3^n}$, testing both endpoints.

**32.** *(§7.12)* Derive the Maclaurin series of $F(x)=\displaystyle\int_0^x e^{-t^2}dt$ and use it to
estimate $F(1)$ with error less than $10^{-3}$.

**33.** *(§7.9, §7.10)* Prove that $\sum_{n\ge0}c_nx^n$ and its term-by-term derivative
$\sum_{n\ge1}nc_nx^{n-1}$ have the same radius of convergence. You may use Hadamard's formula, but you must
prove that $n^{1/n}\to1$.

## Challenge

**34.** *(§7.11)* Prove that $e$ is irrational. *Hint:* assume $e=p/q$, multiply the series by $q!$, and show
that the tail lies strictly between $0$ and $1$.

**35.** *(§7.5)* Let $a_n\ge0$ and suppose $\sum a_n$ converges. Prove that
$\displaystyle\sum_{n=1}^{\infty}\frac{\sqrt{a_n}}{n}$ converges. *Hint:* $2\sqrt{a_n}/n\le a_n+1/n^2$.

**36.** *(§7.8)* Define $b_n=\frac1n$ for odd $n$ and $b_n=\frac{1}{n^2}$ for even $n$, and let
$a_n=(-1)^nb_n$. Show that the terms alternate in sign and satisfy $|a_n|\to0$, but that $\sum a_n$
diverges. Which hypothesis of the alternating series test fails?

**37.** *(§7.8)* Let $H_N=1+\frac12+\cdots+\frac1N$, and take as known that
$\sum_{n\ge1}\frac{(-1)^{n+1}}{n}=\ln2$ and that $H_N-\ln N$ converges to a constant. Prove that the
rearrangement

$$1+\frac13-\frac12+\frac15+\frac17-\frac14+\frac19+\frac1{11}-\frac16+\cdots,$$

whose $k$-th block is $\frac{1}{4k-3}+\frac{1}{4k-1}-\frac{1}{2k}$, converges to $\frac32\ln2$. *Hint:* the
sum of the first $N$ blocks is $H_{4N}-\frac12H_{2N}-\frac12H_N$.

**38.** *(§7.12)* Starting from the binomial series for $(1-u)^{-1/2}$, derive the Maclaurin series of
$\arcsin x$, give the first three nonzero terms, and state the interval on which the identity holds.

**39.** *(§7.11, §7.12)* Solve $y''=xy$ with $y(0)=1$, $y'(0)=0$ by a power series: find the recursion for
the coefficients, write the terms up to $x^9$, and explain why the radius of convergence is infinite.
(The solution is the Airy-type function $\operatorname{Ai}$-related series; no closed form is required.)

**40.** *(§7.11)* Let $f(x)=\frac{\sin x}{x}$ for $x\ne0$ and $f(0)=1$. Show that $f$ is infinitely
differentiable at $0$, find $f^{(2n)}(0)$, and use uniqueness of power-series coefficients to write the
Maclaurin series of $f$ and its radius of convergence.
