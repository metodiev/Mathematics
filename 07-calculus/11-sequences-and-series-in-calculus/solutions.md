# Sequences and Series — Solutions

> [Sequences and Series](README.md) · Solutions to the 40 problems in [exercises.md](exercises.md)

Each solution states the strategy, carries out every step, and — where a numerical claim is made — checks it
with a few partial sums. Pitfalls are flagged where the problem is designed to expose them.

## Beginner

**1.** Answer: $3$.

*Strategy: divide by the highest power $n^2$ so that every remaining term tends to a constant.*

$$\frac{3n^2+2}{n^2-n+1}=\frac{3+\dfrac{2}{n^2}}{1-\dfrac1n+\dfrac{1}{n^2}} .$$

Since $1/n\to0$ and $1/n^2\to0$ (squeeze: $0\le1/n^2\le1/n$ for $n\ge1$), the numerator tends to $3$ and the
denominator to $1-0+0=1\ne0$. The quotient law (Theorem 7.1) applies and gives the limit $3/1=3$.

*Check.* At $n=1000$ the quotient is $(3.000002)/(0.999001)\approx3.003$, approaching $3$. ✓

**2.** Answer: $e^2$.

*Strategy: reduce to the standard limit $(1+u)^{1/u}\to e$ as $u\to0$.*

Put $u=2/n\to0^+$. Then

$$\left(1+\frac2n\right)^n=\left[(1+u)^{1/u}\right]^{2},$$

because $n=2/u$, so $n=2\cdot(1/u)$ and $(1+u)^{n}=\bigl((1+u)^{1/u}\bigr)^2$. Since
$(1+u)^{1/u}\to e$ and $t\mapsto t^2$ is continuous, the limit is $e^2$.

*Equivalently,* take logarithms: $n\ln(1+2/n)=2\cdot\dfrac{\ln(1+u)}{u}\to2\cdot1=2$, so the sequence tends to
$e^2$ by continuity of the exponential.

*Check.* At $n=1000$ the value is $(1.002)^{1000}=7.3743\ldots$ and $e^2=7.3891\ldots$ ✓.

**3.** Answer: $\dfrac{11}{18}$.

*Strategy: split into partial fractions so that almost every term cancels.*

$$\frac{1}{n(n+3)}=\frac13\left(\frac1n-\frac{1}{n+3}\right),$$

since $\frac13\bigl(\frac{n+3-n}{n(n+3)}\bigr)=\frac{1}{n(n+3)}$. Hence

$$S_N=\frac13\sum_{n=1}^{N}\left(\frac1n-\frac{1}{n+3}\right)
=\frac13\left(1+\frac12+\frac13-\frac{1}{N+1}-\frac{1}{N+2}-\frac{1}{N+3}\right),$$

because all intermediate terms cancel in triples. Letting $N\to\infty$,

$$\sum_{n=1}^{\infty}\frac{1}{n(n+3)}=\frac13\left(1+\frac12+\frac13\right)=\frac13\cdot\frac{11}{6}=\frac{11}{18}.$$

*Check.* $S_{10}=0.5274\ldots$ and $11/18=0.6111\ldots$; the remainder is
$\frac13(\frac1{11}+\frac1{12}+\frac1{13})\approx0.0838$, and indeed $0.5274+0.0838=0.6112$ ✓.

*Pitfall:* the three leftover terms matter. Leaving only $1$ instead of $1+\frac12+\frac13$ is the usual
error in this family.

**4.** Answer: $-\dfrac38$.

This is geometric with first term $a=-\frac35$ and ratio $r=-\frac35$. Since $|r|=\frac35<1$, Theorem 7.9
gives

$$\sum_{n=1}^{\infty}\left(-\frac35\right)^n=\frac{a}{1-r}=\frac{-3/5}{1+3/5}
=\frac{-3/5}{8/5}=-\frac38 .$$

*Check.* Partial sums: $-0.6,\ -0.24,\ -0.384,\ -0.3696,\ldots$ oscillating towards $-0.375$ ✓.

**5.** The series diverges, by the **divergence test** (Theorem 7.10).

*Strategy: check the terms first; it is the cheapest test.*

$$\frac{n}{2n+1}=\frac{1}{2+1/n}\longrightarrow\frac12\ne0 .$$

Since the terms do not tend to $0$, the series diverges. No other test is needed, and none would help: the
terms behave like $1/2$, so the partial sums grow like $n/2$.

*Check.* $S_{100}=48.855\ldots$, close to $100/2=50$ ✓.

**6.** (a) Diverges. (b) Converges.

(a) $\dfrac{1}{\sqrt[3]{n^2}}=\dfrac{1}{n^{2/3}}$ is a $p$-series with $p=\frac23\le1$, so it diverges by
Corollary 7.15.1. Equivalently, comparison with the harmonic series: $n^{-2/3}\ge n^{-1}$ for $n\ge1$, and
$\sum1/n$ diverges.

(b) $p=\frac43>1$, so the $p$-series converges.

*Check.* For (a), $\sum_{n\le1000}n^{-2/3}\approx27.56$, growing without bound (it behaves like
$3N^{1/3}=30$ at $N=1000$) ✓. For (b), $\sum_{n\le1000}n^{-4/3}<1+\int_1^\infty x^{-4/3}dx=4$ ✓.

**7.** *Strategy: compare with the convergent $p$-series $\sum1/n^2$, then bound the sum by an integral.*

For every $n\ge1$, $n^2+1>n^2$, so

$$0<\frac{1}{n^2+1}<\frac{1}{n^2}.$$

Since $\sum1/n^2$ converges, Theorem 7.16 gives convergence. For the bound, separate the first term and use
the integral comparison for the rest:

$$\sum_{n=1}^{\infty}\frac{1}{n^2+1}<\frac12+\sum_{n=2}^{\infty}\frac{1}{n^2}
\le\frac12+\int_1^{\infty}\frac{dx}{x^2}=\frac12+1=\frac32<2 .$$

(The inequality $\sum_{n\ge2}f(n)\le\int_1^\infty f$ holds for positive decreasing $f$, as in the proof of
Theorem 7.15.)

*Check.* The sum is $1.0767\ldots$, well below $2$ ✓.

**8.** Converges.

*Strategy: the numerator is $\sim2n$ and the denominator $\sim n^3$, so compare with $1/n^2$.*

With $a_n=\dfrac{2n+1}{n^3+1}>0$ and $b_n=\dfrac1{n^2}$,

$$\frac{a_n}{b_n}=\frac{n^2(2n+1)}{n^3+1}=\frac{2+1/n}{1+1/n^3}\longrightarrow2\in(0,\infty).$$

Since $\sum1/n^2$ converges, Theorem 7.17 gives convergence.

*Direct alternative:* $2n+1\le3n$ and $n^3+1\ge n^3$ give $a_n\le3/n^2$.

*Check.* $S_{10}=2.7150\ldots$, $S_{100}=2.8898\ldots$, $S_{1000}=2.9078\ldots$; the partial sums increase
slowly and stay bounded, consistent with convergence ✓.

**9.** Converges.

*Strategy: a power of $n$ over an exponential — the ratio test is the natural choice.*

$$\frac{a_{n+1}}{a_n}=\frac{(n+1)^2}{3^{n+1}}\cdot\frac{3^n}{n^2}
=\frac13\left(1+\frac1n\right)^2\longrightarrow\frac13<1 .$$

By Theorem 7.18 the series converges absolutely.

*Remark.* The sum can be computed: differentiating $\sum x^n=1/(1-x)$ twice gives
$\sum n^2x^n=\frac{x(1+x)}{(1-x)^3}$, so at $x=1/3$ the sum is $\frac{(1/3)(4/3)}{(2/3)^3}=\frac32$.

*Check.* $S_{10}=1.49887\ldots$, approaching $1.5$ ✓ (convergence is extremely fast).

**10.** Converges.

*Strategy: the whole term is an $n$-th power, so take the $n$-th root.*

$$\left|a_n\right|^{1/n}=\frac{n}{3n+1}\longrightarrow\frac13<1 .$$

By Theorem 7.19 the series converges absolutely. The ratio test would also work but would require
estimating $\bigl(\frac{n+1}{3n+4}\bigr)^{n+1}\big/\bigl(\frac{n}{3n+1}\bigr)^n$, which is messier.

*Check.* $S_{10}=0.37206\ldots$; the terms decay like $3^{-n}$, so the sum is already close to its first term
$1/4$ plus $(2/7)^2\approx0.0816$, and the total is $0.37206\ldots$ ✓.

**11.** Converges conditionally (and its sum is $\pi/4$).

*Strategy: use the alternating test for convergence, then test the absolute series.*

Take $b_n=\dfrac{1}{2n-1}$. Then $b_n>0$; $b_{n+1}=\frac{1}{2n+1}<\frac{1}{2n-1}=b_n$; and
$b_n\to0$. Theorem 7.20 gives convergence, and $|S-S_N|\le\frac{1}{2N+1}$.

For absolute convergence, $\sum\lvert a_n\rvert=\sum\frac{1}{2n-1}$, and
$\frac{1}{2n-1}\ge\frac{1}{2n}$, so comparison with $\frac12\sum1/n=\infty$ shows divergence. Hence the
series converges conditionally.

The sum $\pi/4$ follows from the arctangent series at $x=1$ (§7.12). Numerically $S_{1000}\approx0.78515$ and
$\pi/4=0.78540$ ✓.

**12.** Radius $R=\infty$; interval $(-\infty,\infty)$.

*Strategy: the factorial in the denominator makes the ratio tend to $0$ for every $x$.*

With $c_n=\frac{1}{(n+1)!}$,

$$\left|\frac{c_{n+1}}{c_n}\right|=\frac{(n+1)!}{(n+2)!}=\frac{1}{n+2},$$

so for fixed $x\ne0$ the ratio of consecutive terms of $\sum c_nx^n$ is $\frac{|x|}{n+2}\to0<1$. The ratio
test gives absolute convergence for every $x$, so $R=\infty$ and the interval is all of $\mathbb{R}$.

*Remark.* The sum is $\sum_{n\ge0}\frac{x^n}{(n+1)!}=\frac{e^x-1}{x}$ for $x\ne0$ and $1$ at $x=0$.

*Check.* At $x=10$ the terms grow until $n\approx10$ and then decay factorially; $S_{30}$ already agrees with
$(e^{10}-1)/10=2202.546\ldots$ to many digits ✓.

## Intermediate

**13.** Answer: $\dfrac12$.

*Strategy: the denominator factors as $(n+1)(n+2)$, which telescopes.*

$$\frac{1}{n^2+3n+2}=\frac{1}{(n+1)(n+2)}=\frac{1}{n+1}-\frac{1}{n+2}.$$

Therefore

$$S_N=\sum_{n=1}^{N}\left(\frac{1}{n+1}-\frac{1}{n+2}\right)=\frac12-\frac{1}{N+2}
\longrightarrow\frac12 .$$

*Check.* $S_{10}=0.4167\ldots$ with remainder $1/12=0.0833$, total $0.5$ ✓.

**14.** Converges.

*Strategy: the term behaves like $n^{-3/2}$, so compare with that $p$-series.*

With $a_n=\dfrac{1}{n\sqrt{n+1}}$ and $b_n=n^{-3/2}$,

$$\frac{a_n}{b_n}=\frac{n^{3/2}}{n\sqrt{n+1}}=\sqrt{\frac{n}{n+1}}\longrightarrow1\in(0,\infty).$$

Since $\sum n^{-3/2}$ converges ($p=\frac32>1$), Theorem 7.17 gives convergence.

*Check.* $S_{100}=1.9848\ldots$, $S_{1000}=2.1208\ldots$, $S_{10^6}=2.1820\ldots$: increasing slowly towards a
limit between $2.18$ and $2.19$ (the tail beyond $10^6$ is about $\int_{10^6}^\infty x^{-3/2}dx=0.002$) ✓.

**15.** Diverges.

*Strategy: successive substitutions $u=\ln x$, $v=\ln u$ reduce the integral to a logarithm.*

Let $f(x)=\dfrac{1}{x\ln x\ln\ln x}$ on $[3,\infty)$. It is continuous and positive, and its denominator
$x\ln x\ln\ln x$ has derivative $\ln x\ln\ln x+\ln\ln x+1>0$ for $x\ge3$, so $f$ is decreasing. With
$u=\ln x$ and then $v=\ln u$,

$$\int_3^{R}\frac{dx}{x\ln x\ln\ln x}=\int_{\ln3}^{\ln R}\frac{du}{u\ln u}
=\Bigl[\ln\ln u\Bigr]_{\ln3}^{\ln R}=\ln\ln\ln R-\ln\ln\ln 3\longrightarrow\infty .$$

By Theorem 7.15 the series diverges. (The growth is fantastically slow: the partial sum to $10^6$ is about
$5.63$.)

*Check.* $S_{10^3}\approx5.32$, $S_{10^6}\approx5.63$: increasing, consistent with
$\ln\ln\ln N$ growth ✓.

**16.** Converges conditionally.

*Convergence.* Let $b_n=\dfrac{n}{n^2+1}$. Then $b_n>0$ and $b_n\to0$ (divide by $n^2$). Monotonicity:

$$b_{n+1}\le b_n\iff (n+1)(n^2+1)\le n\bigl((n+1)^2+1\bigr)
\iff n^3+n^2+n+1\le n^3+2n^2+2n\iff n^2+n-1\ge0,$$

which holds for all $n\ge1$. So Theorem 7.20 gives convergence.

*Absolute convergence.* $\dfrac{n}{n^2+1}$ behaves like $\dfrac1n$: with $b_n'=1/n$,

$$\frac{n/(n^2+1)}{1/n}=\frac{n^2}{n^2+1}\longrightarrow1,$$

and $\sum1/n$ diverges, so $\sum\frac{n}{n^2+1}$ diverges. Hence the convergence is conditional.

*Check.* Partial sums of the alternating series: $S_{10}=-0.2225$, $S_{100}=-0.2646$,
$S_{10^4}=-0.26956$, settling at about $-0.2696$ ✓; the absolute series' partial sums grow like $\frac12\ln N$
✓.

*Pitfall:* the signs here are $(-1)^n$, so the first term is $-1/2$ and the sum is negative. The alternating
test is indifferent to the starting sign, but numerical checks are not.

**17.** Converges.

*Strategy: factorials over $n$-th powers — the ratio of consecutive terms simplifies to a power of
$n/(n+1)$.*

$$\frac{a_{n+1}}{a_n}=\frac{(n+1)!}{(n+1)^{n+1}}\cdot\frac{n^n}{n!}
=\frac{n^n}{(n+1)^n}=\left(\frac{n}{n+1}\right)^n\longrightarrow\frac1e<1 .$$

By Theorem 7.18 the series converges absolutely.

*Check.* $S_1=1$, $S_2=1.5$, $S_3=1.7222$, $S_5=1.8544$, $S_{10}=1.87963\ldots$, the sum being
$1.879854\ldots$ ✓.

**18.** Converges.

*Strategy: the whole expression is built from an $n$-th power, so the root test is direct.*

For $n\ge2$ the terms are positive, and

$$\left|a_n\right|^{1/n}=\left(1-\frac1n\right)^{n}\longrightarrow\frac1e<1 .$$

Theorem 7.19 gives absolute convergence.

*Equivalently,* $\ln a_n=n^2\ln(1-1/n)=n^2\bigl(-1/n-O(1/n^2)\bigr)=-n+O(1)$, so $a_n=O(e^{-n})$ and
comparison with a geometric series gives convergence.

*Check.* $a_{10}=(0.9)^{100}=2.66\times10^{-5}$; the sum of the first few terms is about $0.1046$ ✓.

**19.** Interval of convergence: $[-6,\,2)$.

*Radius.* With $c_n=\frac{1}{n4^n}$,

$$R=\lim\left|\frac{c_n}{c_{n+1}}\right|=\lim\frac{(n+1)4^{n+1}}{n4^n}=4 .$$

So the series converges absolutely for $|x+2|<4$, i.e. $-6<x<2$, and diverges for $x<-6$ or $x>2$.

*Endpoint $x=2$:* the series is $\sum\frac{4^n}{n4^n}=\sum\frac1n$, which diverges (harmonic).

*Endpoint $x=-6$:* the series is $\sum\frac{(-4)^n}{n4^n}=\sum\frac{(-1)^n}{n}$, which converges by the
alternating test (conditionally).

*Conclusion.* The interval is $[-6,2)$. Exactly one endpoint is included, so the ratio test's open interval is
strictly smaller than the actual interval of convergence.

*Check.* At the interior point $x=0$ the series is $\sum\frac{2^n}{n4^n}=\sum\frac{(1/2)^n}{n}=-\ln(1-\frac12)=\ln2\approx0.693$, a convergent value $\ln2$ ✓. At $x=3$ (outside) the terms are $\frac{5^n}{n4^n}$, growing geometrically, so divergence is expected ✓.

**20.** Radius of convergence: $R=e$.

*Strategy: the ratio formula, since the coefficients contain a factorial.*

$$R=\lim_{n\to\infty}\left|\frac{c_n}{c_{n+1}}\right|
=\lim_{n\to\infty}\frac{n!}{n^n}\cdot\frac{(n+1)^{n+1}}{(n+1)!}
=\lim_{n\to\infty}\frac{(n+1)^{n}}{n^n}
=\lim_{n\to\infty}\left(1+\frac1n\right)^n=e .$$

*Check.* At $x=e/2$ the terms behave like $(e/2)^n\sqrt{2\pi n}/e^n=(1/2)^n\sqrt{2\pi n}$, summable; at
$x=3e$ they grow, consistent with $R=e$ ✓.

*Remark.* At $|x|=e$ the terms are asymptotic to $\sqrt{2\pi n}$ (Stirling), so they do not tend to $0$ and
the endpoints are excluded; proving this needs Stirling's formula, which is why only the radius is asked.

**21.** $\displaystyle x^2e^{-x}=\sum_{n=0}^{\infty}\frac{(-1)^nx^{n+2}}{n!}$, radius $\infty$, and
$f^{(5)}(0)=-20$.

*Strategy: substitute $-x$ into the exponential series and multiply by $x^2$.*

For every $x$, $e^{-x}=\sum_{n\ge0}\frac{(-x)^n}{n!}=\sum_{n\ge0}\frac{(-1)^nx^n}{n!}$, so multiplying by
$x^2$ (which shifts the index but cannot change the radius) gives

$$f(x)=\sum_{n=0}^{\infty}\frac{(-1)^nx^{n+2}}{n!}=x^2-x^3+\frac{x^4}{2}-\frac{x^5}{6}+\cdots .$$

The radius is $\infty$ because the exponential series converges for all $x$.

By uniqueness of coefficients (Theorem 7.24), the coefficient of $x^5$ equals
$\frac{f^{(5)}(0)}{5!}$. The $x^5$ term corresponds to $n=3$:

$$\frac{(-1)^3}{3!}=-\frac16=\frac{f^{(5)}(0)}{120}\quad\Longrightarrow\quad f^{(5)}(0)=-\frac{120}{6}=-20 .$$

*Check.* Differentiating directly gives $f^{(5)}(x)=-(x^2-10x+20)e^{-x}$, so $f^{(5)}(0)=-20$ ✓.

**22.** Answer: $\dfrac12$.

*Strategy: replace $\cos x$ by its Maclaurin series and divide.*

$$\cos x=1-\frac{x^2}{2}+\frac{x^4}{24}-O(x^6),$$

so

$$\frac{1-\cos x}{x^2}=\frac{\frac{x^2}{2}-\frac{x^4}{24}+O(x^6)}{x^2}
=\frac12-\frac{x^2}{24}+O(x^4)\longrightarrow\frac12 .$$

No L'Hôpital is needed, and the series also shows the rate of approach: the difference from $\frac12$ is
about $-x^2/24$.

**23.** Answer: $\dfrac16$.

$$\sin x=x-\frac{x^3}{6}+\frac{x^5}{120}-O(x^7),$$

hence

$$\frac{x-\sin x}{x^3}=\frac{\frac{x^3}{6}-\frac{x^5}{120}+O(x^7)}{x^3}
=\frac16-\frac{x^2}{120}+O(x^4)\longrightarrow\frac16 .$$

*Check.* At $x=0.1$: $(0.1-0.0998334)/0.001=0.1666\ldots$, close to $1/6=0.16667$ ✓.

**24.** $\sqrt{1.1}\approx1.04875$ with error at most $6.25\times10^{-5}$.

*Strategy: the binomial series with $\alpha=\frac12$ and $x=0.1$ is alternating with decreasing terms, so
the first omitted term bounds the error.*

$$\sqrt{1+x}=1+\frac{x}{2}-\frac{x^2}{8}+\frac{x^3}{16}-\frac{5x^4}{128}+\cdots$$

At $x=0.1$:

$$1+\frac{0.1}{2}-\frac{0.01}{8}=1+0.05-0.00125=1.04875 .$$

The next term is $\frac{x^3}{16}=\frac{0.001}{16}=6.25\times10^{-5}>0$, so by Theorem 7.20

$$\left|\sqrt{1.1}-1.04875\right|\le6.25\times10^{-5}.$$

*Check.* $\sqrt{1.1}=1.048808848\ldots$, and $1.048808848-1.04875=5.885\times10^{-5}$, inside the bound ✓.

*Pitfall:* the terms of the binomial series decrease for $0<x<1$ because for $n\ge1$
$\bigl|\binom{1/2}{n+1}x^{n+1}\bigr|\big/\bigl|\binom{1/2}{n}x^n\bigr|=x\,\frac{2n-1}{2n+2}<x<1$. For $x>1$
that inequality fails and the alternating bound cannot be used.

## Advanced

**25.** *Claim:* if $a_n>0$ and $\sum a_n$ converges, then $\sum a_n^2$ converges.

*Strategy: convergence forces $a_n\to0$, hence $a_n\le1$ eventually, and then squaring only makes the terms
smaller.*

Since $\sum a_n$ converges, $a_n\to0$ (Theorem 7.10). Take $\varepsilon=1$: there is $N$ with $a_n<1$ for all
$n\ge N$. Then for $n\ge N$,

$$0<a_n^2=a_n\cdot a_n<a_n .$$

By Theorem 7.16, $\sum_{n\ge N}a_n^2$ converges, hence so does the whole series (finitely many extra terms).
$\blacksquare$

*The converse fails.* Take $a_n=1/n>0$: then $\sum a_n^2=\sum1/n^2=\pi^2/6$ converges, while $\sum a_n=\sum1/n$
diverges. So $\sum a_n^2<\infty$ does **not** imply $\sum a_n<\infty$; the hypothesis $a_n\to0$ is not
symmetric between the two series.

*Remark.* Positivity is essential in the forward direction: $a_n=(-1)^{n+1}/\sqrt n$ has $\sum a_n<\infty$ but
$\sum a_n^2=\sum1/n=\infty$ (exercise 26).

**26.** Example: $\displaystyle\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{\sqrt n}$.

*Convergence.* Let $b_n=n^{-1/2}$. Then $b_n>0$; $b_{n+1}=\frac{1}{\sqrt{n+1}}<\frac{1}{\sqrt n}=b_n$; and
$b_n\to0$. Theorem 7.20 gives convergence, with $|S-S_N|\le\frac{1}{\sqrt{N+1}}$.

*Divergence of the absolute series.* $\sum|a_n|=\sum n^{-1/2}$ is a $p$-series with $p=\frac12\le1$, so it
diverges (Corollary 7.15.1).

Hence the series converges conditionally. By Theorem 7.22 (Riemann), some rearrangement of these same terms
converges to any prescribed real number, and some rearrangement diverges; only the given order has sum $S$.
Numerically $S_{100}=0.5550\ldots$, $S_{10^4}=0.5999\ldots$, $S=0.604899\ldots$ ✓.

*Why this example matters.* It shows that "$\sum a_n$ converges" is not a licence to reorder, regroup or
split into positive and negative parts. Every such manipulation requires absolute convergence.

**27.** *Step 1: grouping.* Group the harmonic series into blocks of lengths $1,1,2,4,\dots$:

$$H_{2^m}=1+\frac12+\left(\frac13+\frac14\right)+\left(\frac15+\cdots+\frac18\right)+\cdots
+\left(\frac{1}{2^{m-1}+1}+\cdots+\frac{1}{2^m}\right).$$

The $k$-th block (for $k\ge1$) runs from $2^{k-1}+1$ to $2^k$ and contains $2^{k-1}$ terms, each at least
$\frac{1}{2^k}$. Therefore each block contributes at least $2^{k-1}\cdot\frac{1}{2^k}=\frac12$, and

$$H_{2^m}\ge1+\frac m2\longrightarrow\infty .$$

Since $(H_N)$ is increasing (all terms are positive), it is unbounded; by Theorem 7.14 the harmonic series
diverges. $\blacksquare$

*Step 2: the odd harmonic series.* For every $n\ge1$, $\frac{1}{2n-1}\ge\frac{1}{2n}$, hence

$$\sum_{n=1}^{N}\frac{1}{2n-1}\ \ge\ \sum_{n=1}^{N}\frac{1}{2n}=\frac12H_N\longrightarrow\infty .$$

By Theorem 7.16 (or simply because the partial sums are increasing and unbounded), $\sum\frac{1}{2n-1}$
diverges. (This is what makes exercise 11 conditional rather than absolute.)

**28.** *Proof of the $c=0$ case.* Since $a_n/b_n\to0$, choose $N$ such that $a_n/b_n\le1$ for all $n\ge N$
(take $\varepsilon=1$ in the definition of the limit). Then $0<a_n\le b_n$ for $n\ge N$, and Theorem 7.16
gives convergence of $\sum_{n\ge N}a_n$ because $\sum b_n$ converges. Adding the finitely many earlier terms
preserves convergence. $\blacksquare$

*Application.* First, $\ln(1+u)\le u$ for $u\ge0$: the function $g(u)=u-\ln(1+u)$ satisfies $g(0)=0$ and
$g'(u)=1-\frac{1}{1+u}=\frac{u}{1+u}\ge0$, so $g$ is increasing and non-negative. Hence

$$0<\ln\left(1+\frac{1}{n^2}\right)\le\frac{1}{n^2},$$

and $\sum1/n^2$ converges, so the series converges by direct comparison. To see the $c=0$ case in action,
compare instead with $b_n=n^{-3/2}$: then

$$\frac{\ln(1+1/n^2)}{n^{-3/2}}=n^{3/2}\ln\left(1+\frac{1}{n^2}\right)\sim n^{3/2}\cdot\frac{1}{n^2}
=\frac{1}{n^{1/2}}\longrightarrow0,$$

and $\sum n^{-3/2}$ converges, so the $c=0$ case gives convergence directly.

**29.** *Part 1: ratio limit implies root limit.*

First recall the **Cesàro lemma**: if $c_k\to c$, then $\frac1n\sum_{k=1}^{n}c_k\to c$. Indeed, given
$\varepsilon>0$, choose $K$ with $|c_k-c|<\varepsilon$ for $k>K$; then for $n>K$,
$\bigl|\frac1n\sum_{k\le n}c_k-c\bigr|\le\frac1n\sum_{k\le K}|c_k-c|+\varepsilon$, and the first term tends
to $0$ as $n\to\infty$.

Now let $a_n>0$ and $a_{n+1}/a_n\to L>0$ (the cases $L=0$ and $L=\infty$ follow by the same argument or by
taking limits). Put $c_k=\ln\frac{a_{k+1}}{a_k}$, so $c_k\to\ln L$ by continuity of $\ln$. Then

$$\frac1n\ln a_n=\frac1n\left(\ln a_1+\sum_{k=1}^{n-1}c_k\right)\longrightarrow\ln L$$

by the Cesàro lemma, so $\ln a_n^{1/n}\to\ln L$ and, by continuity of the exponential,
$a_n^{1/n}\to e^{\ln L}=L$. $\blacksquare$

(If $L=0$, then $c_k\to-\infty$, the averages tend to $-\infty$, and $a_n^{1/n}\to0$; if $L=\infty$, the
averages tend to $+\infty$ and $a_n^{1/n}\to\infty$.)

*Part 2: an example where only the root test works.* Define

$$a_n=\begin{cases}2^{-n}, & n \text{ even},\\[1mm] 2^{-n+1}, & n \text{ odd}.\end{cases}$$

Then $a_n^{1/n}\to\frac12$: for even $n$, $a_n^{1/n}=2^{-1}$; for odd $n$, $a_n^{1/n}=2^{-1+1/n}\to\frac12$.
Since $\frac12<1$, the root test proves convergence (the series is $\frac53$: the pair
$a_{2k-1}+a_{2k}=4\cdot4^{-k}+4^{-k}=5\cdot4^{-k}$ sums to $5\cdot\frac{1/4}{3/4}=\frac53$).

The ratios alternate:

$$\frac{a_{2k}}{a_{2k-1}}=\frac{4^{-k}}{4\cdot4^{-k}}=\frac14,\qquad
\frac{a_{2k+1}}{a_{2k}}=\frac{4\cdot4^{-(k+1)}}{4^{-k}}=1 .$$

So the ratio sequence has no limit (its values are $\frac14,1,\frac14,1,\dots$); in particular
$\limsup=1$ and $\liminf=\frac14$, and the ratio test is inconclusive while the root test decides. This is
Remark 7.19.1 made concrete.

*Check.* Partial sums: $1,\ 1.25,\ 1.5,\ 1.5625,\dots,\ 1.6650,\dots$, converging to $1.6\overline{6}$ ✓.

**30.** Least $N=10$, and $S_{10}=0.901116\ldots$.

*Bound.* By Theorem 7.20, $|S-S_N|\le b_{N+1}=\dfrac{1}{(N+1)^3}$. We need

$$\frac{1}{(N+1)^3}<10^{-3}\iff(N+1)^3>1000\iff N+1>10\iff N\ge10 .$$

So ten terms suffice, and nine do not (for $N=9$ the bound is exactly $10^{-3}$, not strictly smaller).

*Value.*

$$S_{10}=1-\frac{1}{8}+\frac{1}{27}-\frac{1}{64}+\frac{1}{125}-\frac{1}{216}
+\frac{1}{343}-\frac{1}{512}+\frac{1}{729}-\frac{1}{1000}=0.901116\ldots$$

*Check.* The true sum is $0.9015427\ldots$, so the actual error is $4.26\times10^{-4}$, comfortably below the
bound $1/1331=7.51\times10^{-4}$ ✓. Note that the bound is not tight here because the terms decrease
smoothly; it is nevertheless the only bound available without knowing the limit.

**31.** Interval of convergence: $[-1,\,2)$.

*Substitution.* Put $u=2x-1$. The series is $\sum u^n/(n3^n)$, whose radius in $u$ is $3$ (geometric ratio
$1/3$): with $c_n=1/(n3^n)$, $\lim|c_n/c_{n+1}|=3$. So it converges for $|2x-1|<3$, i.e.
$-3<2x-1<3$, i.e. $-1<x<2$, and diverges for $x<-1$ or $x>2$.

*Endpoint $x=2$:* $u=3$, and the series is $\sum\frac{3^n}{n3^n}=\sum\frac1n$, divergent.

*Endpoint $x=-1$:* $u=-3$, and the series is $\sum\frac{(-3)^n}{n3^n}=\sum\frac{(-1)^n}{n}$, convergent
(conditionally).

Hence the interval is $[-1,2)$.

*Check.* At $x=1.9$, $u=2.8$, the terms decay like $(2.8/3)^n/n=(0.933)^n/n$, summable ✓; at $x=2.1$, $u=3.2$,
the terms grow like $(1.067)^n/n$, so divergence is expected ✓.

**32.** Maclaurin series and the estimate.

*Derivation.* The exponential series gives, for all $t$,

$$e^{-t^2}=\sum_{n=0}^{\infty}\frac{(-t^2)^n}{n!}=\sum_{n=0}^{\infty}\frac{(-1)^nt^{2n}}{n!}.$$

A power series may be integrated term by term inside its interval of convergence (Theorem 7.26; here the
radius is $\infty$), so

$$F(x)=\int_0^x e^{-t^2}dt=\sum_{n=0}^{\infty}\frac{(-1)^nx^{2n+1}}{n!\,(2n+1)},\qquad R=\infty .$$

*Estimate at $x=1$.* The series is $\sum_{n\ge0}\frac{(-1)^n}{n!(2n+1)}$, which alternates with terms
decreasing in magnitude (from $n=1$ on). Five terms ($n=0,\dots,4$) give

$$F(1)\approx1-\frac13+\frac{1}{10}-\frac{1}{42}+\frac{1}{216}=0.7474868\ldots$$

and the first omitted term is $\frac{1}{5!\cdot11}=\frac{1}{1320}=7.58\times10^{-4}<10^{-3}$, so the error is
below $10^{-3}$.

*Check.* Numerically $F(1)=0.7468241\ldots$, so the actual error is $6.63\times10^{-4}$ ✓. Note that $F$ has no
elementary antiderivative — the series is the practical way to compute it, as discussed in
[Techniques of Integration](../08-techniques-of-integration/README.md).

**33.** *Claim:* $\sum c_nx^n$ and $\sum nc_nx^{n-1}$ have the same radius.

*Step 1: $n^{1/n}\to1$.* Write $n^{1/n}=1+h_n$ with $h_n\ge0$. For $n\ge2$,
$n=(1+h_n)^n\ge1+\binom{n}{2}h_n^2=\frac{n(n-1)}{2}h_n^2+1$, so $n-1\ge\frac{n(n-1)}{2}h_n^2$ and
$0\le h_n\le\sqrt{\frac{2}{n}}$; the squeeze theorem gives $h_n\to0$. $\blacksquare$

*Step 2: the radii agree.* The derivative series has coefficients $d_n=(n+1)c_{n+1}$ (shifting the index),
and

$$|d_n|^{1/n}=\bigl((n+1)|c_{n+1}|\bigr)^{1/n}=(n+1)^{1/n}\cdot|c_{n+1}|^{1/n}.$$

The first factor tends to $1$ by Step 1. For the second, the sequence $|c_{n+1}|^{1/n}$ has the same limit
superior as $|c_n|^{1/n}$ (shifting the index does not change the set of subsequential limits). Hence

$$\limsup|d_n|^{1/n}=1\cdot\limsup|c_n|^{1/n},$$

and Hadamard's formula (Theorem 7.23) gives the same radius $R$ for both series, including the conventions
$R=0$ and $R=\infty$. $\blacksquare$

*Remark.* Equal radii do not mean equal intervals: $\sum x^n/n^2$ converges at $x=1$, while its derivative
$\sum x^{n-1}/n$ diverges there. The theorem is about the open interval, exactly as Theorem 7.25 states.

## Challenge

**34.** *Proof that $e$ is irrational.*

First, $2<e<3$: the series gives $e>1+1=2$, and

$$e=1+1+\frac{1}{2!}+\frac{1}{3!}+\cdots\le2+\sum_{k=1}^{\infty}\frac{1}{2^k}=3,$$

with strict inequality because $\frac{1}{3!}<\frac14$ and the comparison is strict from $k=3$ onward. In
particular $e$ is not an integer.

Suppose, for contradiction, that $e=p/q$ with $p,q\in\mathbb{N}$ and $q\ge2$. Then $q!\,e=p\,(q-1)!$ is an
integer. On the other hand, split the series at $n=q$:

$$q!\,e=\underbrace{\sum_{n=0}^{q}\frac{q!}{n!}}_{A\ \in\ \mathbb{N}}
+\underbrace{\sum_{n=q+1}^{\infty}\frac{q!}{n!}}_{T}.$$

The first sum is an integer because $n!\mid q!$ for $n\le q$. For the tail, write $n=q+k$ with $k\ge1$:

$$T=\sum_{k=1}^{\infty}\frac{1}{(q+1)(q+2)\cdots(q+k)} .$$

Each term is positive, so $T>0$; and each denominator is at least $(q+1)^k$, so

$$0<T\le\sum_{k=1}^{\infty}\frac{1}{(q+1)^k}=\frac{1}{q}\le\frac12<1 .$$

Therefore $q!\,e=A+T$ is strictly between the consecutive integers $A$ and $A+1$, contradicting the fact that
it is an integer. Hence no such $p/q$ exists and $e$ is irrational. $\blacksquare$

*Remark.* The same argument with $e^{r}$ for rational $r\ne0$ proves that $e^r$ is irrational; the stronger
theorem that $e$ is transcendental is due to Hermite (1873).

**35.** *Proof.* For every $n$, the identity $(x-y)^2\ge0$ with $x=\sqrt{a_n}$ and $y=\frac1n$ gives

$$a_n-\frac{2\sqrt{a_n}}{n}+\frac{1}{n^2}\ge0
\quad\Longrightarrow\quad
\frac{\sqrt{a_n}}{n}\le\frac12\left(a_n+\frac{1}{n^2}\right).$$

All terms are non-negative, so the partial sums of $\sum\frac{\sqrt{a_n}}{n}$ are increasing and bounded
above by

$$\frac12\left(\sum_{n=1}^{\infty}a_n+\sum_{n=1}^{\infty}\frac{1}{n^2}\right)<\infty .$$

By Theorem 7.14 the series converges. $\blacksquare$

*Remark.* The inequality is the arithmetic–geometric mean inequality $2xy\le x^2+y^2$. It also shows the
bound $\sum\frac{\sqrt{a_n}}{n}\le\frac12\bigl(\sum a_n+\frac{\pi^2}{6}\bigr)$.

**36.** *Setup.* The terms are $a_n=(-1)^nb_n$ with

$$b_1=1,\ b_2=\frac14,\ b_3=\frac13,\ b_4=\frac1{16},\ b_5=\frac15,\ b_6=\frac1{36},\dots$$

*Signs and magnitudes.* The sign of $a_n$ is $(-1)^n$, so signs alternate; and $|a_n|=b_n\to0$ because
$b_n\le\frac1n$ for odd $n$ and $b_n=\frac1{n^2}$ for even $n$.

*Divergence.* Split the partial sums into even and odd contributions:

$$S_N=\sum_{\substack{n\le N\\ n\ \text{even}}}\frac{1}{n^2}
\;-\;\sum_{\substack{n\le N\\ n\ \text{odd}}}\frac{1}{n}
=P_N-Q_N .$$

The positive part $P_N$ increases and is bounded by $\sum_{k\ge1}\frac{1}{4k^2}<\infty$, so $P_N\to P$. The
negative part $Q_N=\sum_{2k-1\le N}\frac{1}{2k-1}\to\infty$ by exercise 27. Hence
$S_N=P_N-Q_N\to-\infty$: the series diverges (to $-\infty$).

*Which hypothesis fails.* Monotonicity. Indeed $b_2=\frac14<\frac13=b_3$, so $(b_n)$ is not decreasing
(and it is not eventually decreasing either, since $b_{2k}=1/(4k^2)<b_{2k+1}=1/(2k+1)$ for all $k$). The
alternating test genuinely needs $b_{n+1}\le b_n$; alternation plus $b_n\to0$ does not suffice.

*Check.* Partial sums: $S_{10}=-1.4214$, $S_{100}=-2.5315$, $S_{10^3}=-3.6783$, $S_{10^4}=-4.8292$,
$S_{10^5}=-5.9804$; they decrease by about $\frac12\ln10\approx1.15$ per decade, consistent with
$S_N\approx-\frac12\ln N$ ✓.

**37.** *Proof.* Let $B_k=\frac{1}{4k-3}+\frac{1}{4k-1}-\frac{1}{2k}$ be the $k$-th block, and let
$S_N=B_1+\cdots+B_N$ be the sum of the first $N$ blocks.

*Step 1: rewrite $S_N$.* The odd integers up to $4N-1$ are exactly the numbers $4k-3$ and $4k-1$ for
$k=1,\dots,N$. Hence

$$\sum_{k=1}^{N}\left(\frac{1}{4k-3}+\frac{1}{4k-1}\right)=\sum_{\substack{m\le 4N\\ m\ \text{odd}}}\frac1m
=H_{4N}-\frac12H_{2N},$$

since $H_{4N}$ is the sum of all reciprocals up to $4N$, of which the even ones sum to $\frac12H_{2N}$.
Therefore

$$S_N=H_{4N}-\frac12H_{2N}-\frac12H_{N}.$$

*Step 2: pass to the limit.* By hypothesis $H_n=\ln n+c+\varepsilon_n$ with $\varepsilon_n\to0$. Then

$$\begin{aligned}
S_N&=\bigl(\ln 4N+c+\varepsilon_{4N}\bigr)
-\frac12\bigl(\ln 2N+c+\varepsilon_{2N}\bigr)
-\frac12\bigl(\ln N+c+\varepsilon_N\bigr)\\
&=\ln 4+\ln N-\frac12\ln2-\frac12\ln N-\frac12\ln N
+\Bigl(c-\frac c2-\frac c2\Bigr)+o(1)\\
&=\ln 4-\frac12\ln 2+o(1)=\Bigl(2-\frac12\Bigr)\ln2+o(1)=\frac32\ln2+o(1).
\end{aligned}$$

Hence $S_N\to\frac32\ln2$, as required. $\blacksquare$

*Why this is not a contradiction.* The original series $\sum(-1)^{n+1}/n$ converges to $\ln2$; the
rearrangement converges to $\frac32\ln2$. Both statements are correct because the convergence is conditional
(Theorem 7.22): different orders of the same terms have different sums.

*Check.* Block sums at $N=10^4$ give $1.039696$, against $\frac32\ln2=1.039721$; the convergence is slow
(the $N$-th remainder is about $\frac{1}{4N}$) ✓.

**38.** *Derivation.* Start from the binomial series with $\alpha=-\frac12$ and $u=x^2$:

$$(1-u)^{-1/2}=\sum_{n=0}^{\infty}\binom{-1/2}{n}(-u)^n .$$

Now $\binom{-1/2}{n}(-1)^n=\dfrac{(2n)!}{4^n(n!)^2}=\dfrac{1}{4^n}\binom{2n}{n}$, because

$$\binom{-1/2}{n}=\frac{(-\frac12)(-\frac32)\cdots(-\frac12-n+1)}{n!}
=\frac{(-1)^n\,1\cdot3\cdots(2n-1)}{2^n\,n!}
=\frac{(-1)^n(2n)!}{2^n\,n!\,2^n\,n!}=\frac{(-1)^n}{4^n}\binom{2n}{n}.$$

Hence

$$\frac{1}{\sqrt{1-x^2}}=\sum_{n=0}^{\infty}\frac{1}{4^n}\binom{2n}{n}x^{2n},\qquad |x|<1 .$$

*Integration.* For $|x|<1$, $\arcsin x=\int_0^x\frac{dt}{\sqrt{1-t^2}}$, so by Theorem 7.26

$$\arcsin x=\sum_{n=0}^{\infty}\frac{1}{4^n(2n+1)}\binom{2n}{n}x^{2n+1}
=x+\frac{x^3}{6}+\frac{3x^5}{40}+\cdots$$

*Interval.* The identity holds on $[-1,1]$. At $x=\pm1$ the terms are bounded by
$\frac{1}{(2n+1)4^n}\binom{2n}{n}\le\frac{1}{(2n+1)\sqrt{n+1}}$ (the inequality
$\binom{2n}{n}/4^n\le1/\sqrt{n+1}$ is proved by induction from
$\binom{2n+2}{n+1}/4^{n+1}=\binom{2n}{n}/4^n\cdot\frac{2n+1}{2n+2}$), so the series of absolute values is
dominated by a multiple of $\sum n^{-3/2}$ and converges uniformly on $[-1,1]$ by the Weierstrass $M$-test.
Since $\arcsin$ is continuous, the identity extends to the endpoints by taking limits. (At $x=1$ it gives
$\frac{\pi}{2}=\sum_{n\ge0}\binom{2n}{n}/(4^n(2n+1))$, a slowly converging series for $\pi$.)

*Check.* At $x=\frac12$: $x+\frac{x^3}{6}+\frac{3x^5}{40}=0.5+0.0208333+0.0023438=0.5231771$, and
$\arcsin\frac12=\frac{\pi}{6}=0.5235988$; the next term is positive and of size
$\frac{5}{112}\cdot\frac{1}{128}\approx0.000349$, so the partial sums increase towards the limit ✓.

**39.** *Setup.* Let $y=\sum_{n\ge0}c_nx^n$. Then

$$y''=\sum_{n\ge0}(n+2)(n+1)c_{n+2}x^n,\qquad xy=\sum_{n\ge1}c_{n-1}x^n .$$

*Recursion.* Equating coefficients (Theorem 7.24):

$$n=0:\quad 2c_2=0;\qquad n\ge1:\quad (n+2)(n+1)c_{n+2}=c_{n-1}.$$

*Initial conditions.* $y(0)=1$ gives $c_0=1$; $y'(0)=0$ gives $c_1=0$. Then
$c_2=0$, $c_3=\frac{c_0}{3\cdot2}=\frac16$, $c_4=\frac{c_1}{4\cdot3}=0$, $c_5=\frac{c_2}{5\cdot4}=0$,
$c_6=\frac{c_3}{6\cdot5}=\frac{1}{180}$, $c_7=c_8=0$, $c_9=\frac{c_6}{9\cdot8}=\frac{1}{12960}$.

So

$$y(x)=1+\frac{x^3}{6}+\frac{x^6}{180}+\frac{x^9}{12960}+\cdots .$$

*Check of the ODE.* Differentiating twice, $y''=x+\frac{x^4}{6}+\frac{x^7}{180}+\cdots$, while
$xy=x+\frac{x^4}{6}+\frac{x^7}{180}+\cdots$ ✓. The first terms satisfy the equation term by term.

*Radius.* The recursion links $c_{n+2}$ to $c_{n-1}$, so the nonzero coefficients occur at indices
$n=3k$ (since $c_1=c_2=0$), with

$$\frac{c_{3k}}{c_{3k-3}}=\frac{1}{(3k)(3k-1)}\longrightarrow0 .$$

The ratio of consecutive nonzero coefficients tends to $0$, so for every fixed $x$ the terms
$|c_{3k}||x|^{3k}$ are eventually dominated by a geometric sequence; hence the series converges for all $x$
and $R=\infty$. (The solution is an Airy-type entire function, not an elementary one.)

**40.** *Part 1: smoothness at $0$.*

For $x\ne0$, the sine series gives

$$f(x)=\frac{\sin x}{x}=\frac{1}{x}\sum_{n=0}^{\infty}\frac{(-1)^nx^{2n+1}}{(2n+1)!}
=\sum_{n=0}^{\infty}\frac{(-1)^nx^{2n}}{(2n+1)!}=:g(x).$$

The series defining $g$ converges for every $x$ (ratio $\frac{x^2}{(2n+2)(2n+3)}\to0$), so $g$ is a power
series with infinite radius; in particular $g$ is infinitely differentiable on $\mathbb{R}$, and
$g(0)=1=f(0)$. Since $f=g$ for $x\ne0$ and both are continuous at $0$ with the same value, $f=g$ on
$\mathbb{R}$. Hence $f$ is infinitely differentiable everywhere, in particular at $0$.

*Part 2: derivatives at $0$.* By uniqueness of coefficients (Theorem 7.24),

$$\frac{f^{(2n)}(0)}{(2n)!}=\frac{(-1)^n}{(2n+1)!}
\quad\Longrightarrow\quad
f^{(2n)}(0)=\frac{(-1)^n(2n)!}{(2n+1)!}=\frac{(-1)^n}{2n+1},$$

and $f^{(2n+1)}(0)=0$ because only even powers appear.

*Part 3: Maclaurin series and radius.*

$$f(x)=\sum_{n=0}^{\infty}\frac{(-1)^nx^{2n}}{(2n+1)!}=1-\frac{x^2}{6}+\frac{x^4}{120}-\frac{x^6}{5040}+\cdots,
\qquad R=\infty .$$

*Check.* $f''(0)=2\cdot\frac{-1}{3!}=\frac{-1}{3}$; differentiating $f=1-\frac{x^2}{6}+\frac{x^4}{120}-\cdots$
twice gives $-\frac13+\frac{x^2}{10}-\cdots$, whose value at $0$ is $-\frac13$ ✓. Also
$f^{(4)}(0)=4!\cdot\frac{1}{120}=\frac15$, matching $\frac{1}{5}$ from the formula $\frac{(-1)^2}{5}$ ✓.

