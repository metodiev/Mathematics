# Exponential and Logarithmic Functions — Solutions

> [Tutorial](README.md) · [Exercises](exercises.md) · 40 worked solutions

Every solution states the strategy, shows each significant step, and checks the result — by
substitution, by a numerical estimate that brackets the answer, or by verifying the inverse identity.
Decimal answers are rounded only at the end.

## Beginner

**1.**

$$\begin{aligned}
2^5 &= 32,\\
3^{-2} &= \frac{1}{3^2} = \frac19,\\
16^{3/4} &= \left(16^{1/4}\right)^3 = 2^3 = 8,\\
27^{1/3} &= 3 \quad\text{(because } 3^3=27\text{)},\\
\left(\tfrac14\right)^{-1/2} &= 4^{1/2} = 2 .
\end{aligned}$$

The general principle is $a^{m/n}=\left(\sqrt[n]{a}\right)^m$: take the root first (small numbers),
then the power. The last line uses $\left(a^{-1}\right)^{-1/2}=a^{1/2}$.

**2.**

**(a)** Multiply before dividing:

$$\frac{a^3a^{-5}}{a^{-1}} = \frac{a^{3-5}}{a^{-1}} = \frac{a^{-2}}{a^{-1}} = a^{-2-(-1)} = a^{-1}.$$

**(b)** $\left(2x^2\right)^3 = 2^3\left(x^2\right)^3 = 8x^6$, so

$$\left(2x^2\right)^3x^{-4} = 8x^6\cdot x^{-4} = 8x^{2}.$$

**Check (b)** with $x=2$: $\left(2\cdot4\right)^3\cdot 2^{-4} = 8^3/16 = 512/16 = 32$, and $8\cdot2^2=32$ ✓.

**3.**

* Domain: $\mathbb{R}$ — every real exponent is defined for the positive base $3$.
* Range: $(0,\infty)$ — a positive power of a positive number is positive, and every positive value
  occurs.
* $y$-intercept: $(0,1)$, since $3^0=1$.
* Horizontal asymptote: $y=0$, approached as $x\to-\infty$.
* Monotonicity: strictly increasing, since $3>1$. Equivalently, $3^{x_2}=3^{x_1}3^{x_2-x_1}>3^{x_1}$
  when $x_2>x_1$.
* The graph never meets the $x$-axis, because $3^x>0$ for every real $x$. The axis is an asymptote,
  not a crossing.

**4.**

Since $\left(\tfrac13\right)^x=3^{-x}$:

* Domain: $\mathbb{R}$.
* Range: $(0,\infty)$.
* $y$-intercept: $(0,1)$.
* Horizontal asymptote: $y=0$, now approached as $x\to+\infty$.
* Monotonicity: strictly decreasing, since $0<\tfrac13<1$; indeed
  $\left(\tfrac13\right)^{x_2}=\left(\tfrac13\right)^{x_1}\left(\tfrac13\right)^{x_2-x_1}<
  \left(\tfrac13\right)^{x_1}$ for $x_2>x_1$.

**Relation between the graphs.** Replacing $x$ by $-x$ in $3^x$ gives $3^{-x}=\left(\tfrac13\right)^x$,
so the second graph is the first reflected in the $y$-axis. The two graphs are mirror images and meet
only at $(0,1)$.

**5.**

$$\begin{aligned}
\log_3 81 &= 4 && (3^4=81),\\
\log_2 \tfrac18 &= -3 && \left(2^{-3}=\tfrac18\right),\\
\log_{16}4 &= \tfrac12 && \left(16^{1/2}=4\right),\\
\log_5 5 &= 1 && (5^1=5),\\
\ln 1 &= 0 && (e^0=1).
\end{aligned}$$

The method is always the same: write the argument as a power of the base and read off the exponent.

**6.**

**(a)** $2^7=128 \iff \log_2 128=7$.

**(b)** $10^{-3}=0.001 \iff \log_{10}0.001=-3$.

**(c)** $\log_4 64=3 \iff 4^3=64$.

**(d)** $\log_{1/2}8=-3 \iff \left(\tfrac12\right)^{-3}=8$.

In each case the logarithm *is* the exponent: $y=\log_a x$ means $a^y=x$.

**7.**

All four follow from $a^{\log_a x}=x$ (for $x>0$) and $\log_a a^x=x$ (for all real $x$):

$$e^{\ln 5}=5, \qquad 10^{\log_{10}7}=7, \qquad \ln e^{3}=3, \qquad \log_2 2^{9}=9.$$

A numerical check of the third: $e^3\approx20.0855$ and $\ln 20.0855\approx3.000$ ✓.

**8.**

Use the product and quotient laws:

$$\log_2 6+\log_2 4-\log_2 3 = \log_2\frac{6\cdot4}{3} = \log_2 8 = 3 .$$

**Check.** $\log_2 6\approx2.585$, $\log_2 4=2$, $\log_2 3\approx1.585$; the combination is
$2.585+2-1.585=3.000$ ✓.

**9.**

**(a)**

$$\log_a\left(x^2y^3\right)=\log_a x^2+\log_a y^3 = 2\log_a x+3\log_a y .$$

**(b)**

$$\log_a\frac{\sqrt{x}}{y} = \log_a x^{1/2}-\log_a y = \tfrac12\log_a x-\log_a y .$$

Both expansions use the product (or quotient) law first and the power law second.

**10.**

Change of base to base $2$:

$$\log_8 32 = \frac{\log_2 32}{\log_2 8} = \frac{5}{3}.$$

**Check.** $8^{5/3}=\left(\sqrt[3]{8}\right)^5 = 2^5 = 32$ ✓. Note that $5/3\approx1.667$ lies between
$1$ (where $\log_8 8=1$) and $2$ (where $\log_8 64=2$), as it must, since $8<32<64$.

**11.**

**(a)** $32=2^5$, so $2^x=2^5$ and, since $2^x$ is one-to-one, $x=5$.

**(b)** $\dfrac{1}{27}=3^{-3}$, so $x=-3$.

**(c)** $125=5^3$, so $5^{2x}=5^3$, hence $2x=3$, hence $x=\dfrac32$.

The step "equate the exponents" is licensed by Theorem 8.4: for a fixed base, distinct exponents give
distinct powers.

**12.**

$$A = 1000\left(1+\frac{0.05}{12}\right)^{12\cdot 2} = 1000\left(1+\frac{0.05}{12}\right)^{24}.$$

Now $1+\dfrac{0.05}{12}=1.0041\overline{6}$, and

$$\ln\left(1.0041\overline{6}\right)\approx0.00415801, \qquad 24(0.00415801)=0.0997923,$$

$$e^{0.0997923}\approx1.1049413 .$$

Hence $A\approx 1000(1.1049413)=\$1104.94$.

**Check.** Simple interest would give $\$100$ over two years; compounding monthly adds about $\$4.94$,
which is the right order of magnitude for $5\%$ over two years ✓.

**13.**

$60$ years is $\dfrac{60}{20}=3$ half-lives, so the remaining fraction is

$$\left(\frac12\right)^3=\frac18=12.5\% .$$

Equivalently, $N(60)=N_0\,2^{-60/20}=N_0\,2^{-3}=N_0/8$.

## Intermediate

**14.**

**(a)** $27^{2/3}=\left(\sqrt[3]{27}\right)^2=3^2=9$ and $9^{1/2}=3$, so the product is $9\cdot3=27$.

**(b)** $8^{-2/3}=\dfrac{1}{8^{2/3}}=\dfrac{1}{\left(\sqrt[3]8\right)^2}=\dfrac{1}{4}$.

**Check (a).** $27^{2/3}\cdot 9^{1/2} = 27^{2/3}\cdot 27^{1/3} = 27^{1} = 27$ ✓ — a slicker route using
$9^{1/2}=3=27^{1/3}$ and the product law.

**15.**

$$\begin{aligned}
\ln\frac{x^2\sqrt{y}}{z^3}
&= \ln x^2+\ln y^{1/2}-\ln z^3\\
&= 2\ln x+\tfrac12\ln y-3\ln z .
\end{aligned}$$

Every step requires $x,y,z>0$, which is exactly the condition under which all the displayed logarithms
exist.

**16.**

$$\begin{aligned}
3\log x-\tfrac12\log y+\log z
&= \log x^3-\log y^{1/2}+\log z\\
&= \log\frac{x^3}{\sqrt{y}}+\log z\\
&= \log\frac{x^3z}{\sqrt{y}} .
\end{aligned}$$

**Check** with $x=y=z=10$: the left side is $3-\tfrac12+1=3.5$; the right side is
$\log_{10}\dfrac{1000\cdot10}{10^{1/2}}=\log_{10}10^{3.5}=3.5$ ✓.

**17.**

Take $\ln$ of both sides:

$$\begin{aligned}
5^{2x-1} &= 40\\
(2x-1)\ln 5 &= \ln 40\\
2x-1 &= \frac{\ln 40}{\ln 5}\approx\frac{3.688879}{1.609438}=2.292030\\
2x &= 3.292030\\
x &= 1.646015\ldots
\end{aligned}$$

Hence $x=\dfrac12\left(1+\dfrac{\ln40}{\ln5}\right)\approx1.6460$.

**Check.** $5^{2(1.6460)-1}=5^{2.2920}$. Now $2.2920\ln5=2.2920(1.609438)=3.68884$, and
$e^{3.68884}\approx40.00$ ✓.

**18.**

Since $9^x=\left(3^2\right)^x=\left(3^x\right)^2$, substitute $t=3^x$. Then $t>0$ and

$$t^2-4t+3=0 \quad\Longrightarrow\quad (t-1)(t-3)=0 \quad\Longrightarrow\quad t=1 \text{ or } t=3 .$$

Both are positive, so neither is rejected. Recover $x$:

* $3^x=1=3^0 \Rightarrow x=0$;
* $3^x=3=3^1 \Rightarrow x=1$.

**Check.** $x=0$: $1-4+3=0$ ✓. $x=1$: $9-12+3=0$ ✓.

**19.**

Substitute $t=e^x>0$:

$$t^2-3t-4=0 \quad\Longrightarrow\quad (t-4)(t+1)=0 \quad\Longrightarrow\quad t=4 \text{ or } t=-1 .$$

The root $t=-1$ is rejected, because $e^x>0$ for every real $x$. Hence $e^x=4$ and

$$x=\ln 4=2\ln 2\approx1.3863 .$$

**Check.** $e^{2x}=e^{2\ln4}=16$ and $3e^x=12$, so $16-12-4=0$ ✓.

The rejection of $t=-1$ is a domain check, not a formality: it is the only reason the equation has one
solution rather than two.

**20.**

**Domain.** Both logarithms need positive arguments: $x+2>0$ and $x>0$, so $x>0$.

**Solve.** Combine:

$$\log_3\bigl(x(x+2)\bigr)=1 \quad\Longrightarrow\quad x^2+2x=3^1=3 .$$

$$x^2+2x-3=0 \quad\Longrightarrow\quad (x+3)(x-1)=0 \quad\Longrightarrow\quad x=1 \text{ or } x=-3 .$$

**Check the domain.** $x=1>0$ ✓. $x=-3$ fails: $\log_3(-3+2)=\log_3(-1)$ is undefined.

**Answer.** $x=1$. Verify: $\log_3 3+\log_3 1=1+0=1$ ✓.

**21.**

**Domain.** $x>0$ and $x-3>0$, so $x>3$.

**Solve.**

$$\log_2\frac{x}{x-3}=2 \quad\Longrightarrow\quad \frac{x}{x-3}=2^2=4 .$$

$$x=4(x-3) \;\Longrightarrow\; x=4x-12 \;\Longrightarrow\; 3x=12 \;\Longrightarrow\; x=4 .$$

**Check the domain.** $4>3$ ✓. **Check the equation.** $\log_2 4-\log_2 1=2-0=2$ ✓.

The numerator and denominator both had to be positive; had the solution come out below $3$ it would
have to be discarded even though it satisfies the cleared equation.

**22.**

**Domain.** $x+3>0$ and $x>0$, so $x>0$.

**Solve.**

$$\log\bigl(x(x+3)\bigr)=1 \quad\Longrightarrow\quad x^2+3x=10^1=10 .$$

$$x^2+3x-10=0 \quad\Longrightarrow\quad (x+5)(x-2)=0 \quad\Longrightarrow\quad x=2 \text{ or } x=-5 .$$

**Check the domain.** $x=2>0$ ✓; $x=-5$ fails both conditions, so it is extraneous.

**Answer.** $x=2$. Verify: $\log 5+\log 2=\log 10=1$ ✓.

**23.**

Rewrite everything with the same bases:

$$2^x\cdot4^y = 2^x\cdot 2^{2y}=2^{x+2y}, \qquad 32=2^5,$$

so $x+2y=5$. Next,

$$\frac{3^x}{9^y}=3^x\cdot3^{-2y}=3^{x-2y}, \qquad \frac13=3^{-1},$$

so $x-2y=-1$. The system is linear:

$$\begin{cases} x+2y=5,\\ x-2y=-1 .\end{cases}$$

Adding gives $2x=4$, so $x=2$; substituting gives $2+2y=5$, so $y=\dfrac32$.

**Check.** $2^2\cdot4^{3/2}=4\cdot8=32$ ✓; $\dfrac{3^2}{9^{3/2}}=\dfrac{9}{27}=\dfrac13$ ✓.

**24.**

Model: fraction remaining $=2^{-t/8}$. Set it equal to $0.15$:

$$0.15=2^{-t/8} \;\Longrightarrow\; \ln 0.15=-\frac{t}{8}\ln 2
\;\Longrightarrow\; t=\frac{8\ln(1/0.15)}{\ln 2}.$$

Now $\ln(1/0.15)=\ln 6.6667\approx1.897120$ and $\ln 2\approx0.693147$, so

$$t=8\cdot\frac{1.897120}{0.693147}=8(2.736966)=21.8957\ldots\approx21.9\ \text{days}.$$

**Check by bracketing.** Two half-lives (16 days) leave $25\%$, three half-lives (24 days) leave
$12.5\%$. The answer $21.9$ lies between $16$ and $24$ ✓.

**25.**

$$0.45=2^{-t/5730} \;\Longrightarrow\; \ln 0.45=-\frac{t}{5730}\ln2
\;\Longrightarrow\; t=\frac{5730\ln(1/0.45)}{\ln 2}.$$

$$\ln(1/0.45)=\ln 2.2222\approx0.798508, \qquad t=5730\cdot\frac{0.798508}{0.693147}
=5730(1.152003)=6600.98\ldots$$

So the bone is about $6601$ years old, i.e. about $6600$ years to the nearest ten.

**Check.** $6601/5730\approx1.152$ half-lives; $2^{-1.152}=e^{-1.152(0.693147)}=e^{-0.7985}=0.45$ ✓.

**26.**

**(a)** The difference in magnitude is $6.5-4.5=2$. Since $M=\log_{10}(A/A_0)$,

$$M_2-M_1=\log_{10}\frac{A_2}{A_1} \;\Longrightarrow\; \frac{A_2}{A_1}=10^{2}=100 .$$

The amplitude is $100$ times greater.

**(b)** With $E\propto A^{3/2}$,

$$\frac{E_2}{E_1}=\left(\frac{A_2}{A_1}\right)^{3/2}=100^{3/2}=\left(10^2\right)^{3/2}=10^{3}=1000 .$$

So about $1000$ times more energy — the standard rule that one magnitude step is a factor of about
$31.6$ in energy, and two steps a factor of $1000$.

**27.**

**(a)** For levels differing by $\Delta L$ decibels,

$$\Delta L = 10\log_{10}\frac{I_2}{I_1} \;\Longrightarrow\; \frac{I_2}{I_1}=10^{\Delta L/10}.$$

Here $\Delta L=85-65=20$, so the ratio is $10^{2}=100$: the louder sound carries $100$ times the
intensity.

**(b)**

$$L=10\log_{10}\frac{10^{-5}}{10^{-12}}=10\log_{10}\left(10^{7}\right)=10\cdot7=70\ \text{dB}.$$

**Check.** $70$ dB is a normal conversation level, which matches $10^{-5}$ W/m$^2$ — a plausible
intensity for speech at close range ✓.

## Advanced

**28.**

Throughout, $a>0$, $a\ne1$, $x>0$.

**Step 1: positive integers.** We prove $\log_a(x^n)=n\log_a x$ by induction on $n$. For $n=1$ both
sides equal $\log_a x$. If the statement holds for $n$, then by the product law

$$\log_a\left(x^{n+1}\right)=\log_a\left(x^n\cdot x\right)=\log_a x^n+\log_a x
= n\log_a x+\log_a x=(n+1)\log_a x .$$

So it holds for all $n\in\mathbb{N}$.

**Step 2: $r=1/n$.** Put $y=\log_a\left(x^{1/n}\right)$, so that $x^{1/n}=a^y$. Raising to the $n$-th
power gives $x=a^{ny}$, hence $\log_a x=ny$ and

$$y=\frac1n\log_a x .$$

**Step 3: rational $r=m/n$.** Write $x^{m/n}=\left(x^{1/n}\right)^m$ and apply Steps 1 and 2:

$$\log_a\left(x^{m/n}\right)=m\log_a\left(x^{1/n}\right)=m\cdot\frac1n\log_a x=\frac mn\log_a x .$$

**Step 4: negative $r$.** For $r>0$, $x^{-r}=1/x^{r}$, so by the quotient law and Step 3,

$$\log_a\left(x^{-r}\right)=\log_a 1-\log_a\left(x^{r}\right)=0-r\log_a x .$$

$\blacksquare$

**29.**

Let $y=\log_b x$, so $b^{y}=x$ by Definition 7.5. Apply $\log_a$ to both sides:

$$\log_a\left(b^{y}\right)=\log_a x .$$

By the power law (Solution 28), the left side is $y\log_a b$. Hence

$$y\log_a b=\log_a x .$$

It remains to divide. Since $b\ne1$ and $\log_a$ is one-to-one with $\log_a 1=0$, we have
$\log_a b\ne0$. Therefore

$$y=\frac{\log_a x}{\log_a b}, \qquad\text{i.e.}\qquad \log_b x=\frac{\log_a x}{\log_a b} .$$

$\blacksquare$

**Deduction.** Put $x=a$ in the formula:

$$\log_b a=\frac{\log_a a}{\log_a b}=\frac{1}{\log_a b},$$

so $\log_a b=\dfrac{1}{\log_b a}$ (both bases differ from $1$, so both logarithms are nonzero).

**Numerical check.** $\log_2 8=3$ and $\log_8 2=1/3$: reciprocals ✓.

**30.**

By the binomial theorem,

$$a_n=\left(1+\frac1n\right)^n=\sum_{k=0}^{n}\binom{n}{k}\frac{1}{n^k}
=\sum_{k=0}^{n}\frac{1}{k!}\prod_{j=0}^{k-1}\left(1-\frac jn\right),$$

because

$$\binom{n}{k}\frac{1}{n^k}=\frac{n(n-1)\cdots(n-k+1)}{k!\,n^k}
=\frac{1}{k!}\prod_{j=0}^{k-1}\left(1-\frac jn\right).$$

**Bounded above by $3$.** Each factor $\left(1-\frac jn\right)$ lies in $[0,1]$, so the product is at
most $1$ and

$$a_n \le \sum_{k=0}^{n}\frac{1}{k!} .$$

For $k\ge1$ we have $k! = 1\cdot2\cdot3\cdots k \ge 2^{k-1}$ (each factor from the third onward is at
least $2$), so $\dfrac{1}{k!}\le\dfrac{1}{2^{k-1}}$ and

$$a_n \le 1+\sum_{k=1}^{n}\frac{1}{2^{k-1}}=1+2\left(1-2^{-n}\right)<3 .$$

**Why existence follows.** The sequence is also increasing: each factor $\left(1-\frac jn\right)$
increases when $n$ is replaced by $n+1$, and $a_{n+1}$ has one extra positive term, so $a_{n+1}>a_n$.
An increasing sequence that is bounded above converges, by the completeness property of $\mathbb{R}$.
That limit is $e$. $\blacksquare$

**Numerically.** $a_{10}=2.5937\ldots$, $a_{100}=2.7048\ldots$, $a_{1000}=2.7169\ldots$, all below
$3$ and increasing toward $e=2.71828\ldots$ ✓.

**31.**

Write everything base $2$. Using $\log_{a^n}x=\frac1n\log_a x$ (Corollary 8.3):

$$\log_4 x=\frac12\log_2 x, \qquad \log_8 x=\frac13\log_2 x .$$

Let $L=\log_2 x$. The equation becomes

$$L+\frac L2+\frac L3=11 \quad\Longrightarrow\quad L\left(\frac{6+3+2}{6}\right)=11
\quad\Longrightarrow\quad \frac{11L}{6}=11 \quad\Longrightarrow\quad L=6 .$$

Hence $x=2^{6}=64$.

**Check.** $\log_2 64=6$, $\log_4 64=3$, $\log_8 64=2$, and $6+3+2=11$ ✓.

**32.**

The expression is defined for $x>0$. Take $\log_2$ of both sides:

$$\log_2\left(x^{\log_2 x}\right)=\log_2 8=3 .$$

By the power law the left side is $\left(\log_2 x\right)\left(\log_2 x\right)=\left(\log_2 x\right)^2$.
Hence

$$\left(\log_2 x\right)^2=3 \quad\Longrightarrow\quad \log_2 x=\pm\sqrt3
\quad\Longrightarrow\quad x=2^{\sqrt3}\ \text{ or }\ x=2^{-\sqrt3}.$$

Numerically, $2^{\sqrt3}\approx3.3220$ and $2^{-\sqrt3}\approx0.3010$; both are positive, so neither is
rejected.

**Checks.**

* $x=2^{\sqrt3}$: $\log_2 x=\sqrt3$, and $\left(2^{\sqrt3}\right)^{\sqrt3}=2^{3}=8$ ✓.
* $x=2^{-\sqrt3}$: $\log_2 x=-\sqrt3$, and $\left(2^{-\sqrt3}\right)^{-\sqrt3}=2^{3}=8$ ✓.

**Note.** The two solutions are reciprocals, which is expected: replacing $x$ by $1/x$ changes
$\log_2 x$ to $-\log_2 x$, and squaring removes the sign.

**33.**

**(a)** Convert every logarithm to a common base, say $\ln$, using Theorem 8.2:

$$\log_a b=\frac{\ln b}{\ln a}, \qquad \log_b c=\frac{\ln c}{\ln b}, \qquad \log_c a=\frac{\ln a}{\ln c}.$$

All three denominators are nonzero because none of $a,b,c$ equals $1$. Multiplying,

$$\log_a b\cdot\log_b c\cdot\log_c a
=\frac{\ln b}{\ln a}\cdot\frac{\ln c}{\ln b}\cdot\frac{\ln a}{\ln c}=1 .$$

$\blacksquare$

**(b)** By the change-of-base formula and then the power law,

$$\log_{a^n}\left(b^m\right)=\frac{\ln\left(b^m\right)}{\ln\left(a^n\right)}
=\frac{m\ln b}{n\ln a}=\frac mn\cdot\frac{\ln b}{\ln a}=\frac mn\log_a b .$$

$\blacksquare$

**Check (b)** with $a=2$, $b=2$, $m=3$, $n=2$: $\log_{4}8=\tfrac32$ and $\tfrac32\log_2 2=\tfrac32$ ✓.

**34.**

**Ages.** With $f$ the remaining fraction and $T_{1/2}=5730$,

$$t=T_{1/2}\frac{\ln(1/f)}{\ln 2}.$$

* $f=0.30$: $\ln(1/0.30)=\ln 3.3333\approx1.203973$, so
  $t=5730\cdot\dfrac{1.203973}{0.693147}=5730(1.736966)\approx9952.8$, i.e. about $9950$ years.
* $f=0.90$: $\ln(1/0.90)=\ln 1.1111\approx0.105361$, so
  $t=5730\cdot\dfrac{0.105361}{0.693147}=5730(0.152003)\approx871.0$, i.e. about $870$ years.

**Why the $90\%$ estimate is less reliable.** The age depends on $f$ through $\ln(1/f)$, and that
function changes very rapidly near $f=1$:

$$\frac{dt}{df}=-\frac{T_{1/2}}{\ln 2}\cdot\frac{1}{f}, \qquad\text{so}\qquad
\left|\Delta t\right|\approx\frac{T_{1/2}}{\ln 2}\cdot\frac{\left|\Delta f\right|}{f}.$$

For a measurement error of $\Delta f=0.01$:

* at $f=0.90$: $\left|\Delta t\right|\approx\dfrac{5730}{0.693147}\cdot\dfrac{0.01}{0.90}\approx
  8268(0.01111)\approx92$ years, which is about $10.5\%$ of the $871$-year age;
* at $f=0.30$: $\left|\Delta t\right|\approx8268\cdot\dfrac{0.01}{0.30}\approx276$ years, which is
  about $2.8\%$ of the $9953$-year age.

So although the *absolute* uncertainty is smaller for the young sample, the *relative* uncertainty is
nearly four times larger. A sample a few centuries old is also contaminated by any modern carbon and by
variations in the historical atmospheric ratio, which the simple half-life model ignores; those effects
matter precisely when the true age is small.

**35.**

Because $f$ is continuous and not identically zero, Theorem 7.1 applies with $a=f(1)=3$.

* $f(0)=1$: this was proved in Theorem 7.1(1) from $f(0)=f(0)^2$ and the non-triviality of $f$.
* $f(2)=f(1+1)=f(1)f(1)=3\cdot3=9$.
* $f(-1)$: from $f(1)f(-1)=f(0)=1$ we get $f(-1)=\dfrac{1}{3}$.
* $f\!\left(\tfrac12\right)$: from $f\!\left(\tfrac12\right)^2=f(1)=3$ and $f>0$ we get
  $f\!\left(\tfrac12\right)=\sqrt3\approx1.7321$.
* $f\!\left(\tfrac32\right)=f\!\left(1+\tfrac12\right)=f(1)f\!\left(\tfrac12\right)=3\sqrt3\approx5.1962$.

By Theorem 7.1(3), $f(x)=3^{x}$ for every real $x$.

**Consistency check.** $f\!\left(\tfrac32\right)=3^{3/2}=\sqrt{27}=3\sqrt3$ ✓, and
$f(-1)=3^{-1}=1/3$ ✓.

**36.**

**Transformations.** From $y=3^{x}$: shift right $1$ (giving $3^{x-1}$), stretch vertically by $2$,
reflect in the $x$-axis (together giving $-2\cdot3^{x-1}$), then shift up $4$.

**Properties.**

* Domain: $\mathbb{R}$; the formula is defined for every $x$.
* Range: since $3^{x-1}>0$, we have $-2\cdot3^{x-1}<0$, so $y<4$; as $x\to-\infty$ the term
  $3^{x-1}\to0$ and $y\to4$ from below, while as $x\to+\infty$ it tends to $-\infty$. Hence the range is
  $(-\infty,4)$.
* Horizontal asymptote: $y=4$.
* $y$-intercept: at $x=0$, $y=-2\cdot3^{-1}+4=-\tfrac23+4=\tfrac{10}{3}\approx3.33$.
* $x$-intercept: solve $-2\cdot3^{x-1}+4=0$, i.e. $3^{x-1}=2$. Then
  $x-1=\log_3 2=\dfrac{\ln2}{\ln3}\approx0.6309$, so $x\approx1.631$.
* Monotonicity: $3^{x-1}$ is strictly increasing, multiplying by $-2$ reverses the order, and adding
  $4$ preserves it, so $y$ is **strictly decreasing**.

**Checks.** $x=1$: $y=-2+4=2$. $x=2$: $y=-6+4=-2$. Decreasing ✓, and $2$ lies in $(-\infty,4)$ ✓.

**37.**

**Properties.**

* Domain: $x-2>0$, so $(2,\infty)$.
* Range: $\mathbb{R}$ — a logarithm attains every real value.
* Vertical asymptote: $x=2$, approached as $x\to2^{+}$ (where $\ln(x-2)\to-\infty$).
* $x$-intercept: solve $\ln(x-2)+1=0$, so $\ln(x-2)=-1$ and $x-2=e^{-1}$, giving
  $x=2+\dfrac1e\approx2.368$.
* $y$-intercept: none, since $0$ is not in the domain.

**Inverse.** Write $y=\ln(x-2)+1$ and solve:

$$y-1=\ln(x-2) \;\Longrightarrow\; x-2=e^{y-1} \;\Longrightarrow\; x=2+e^{y-1}.$$

Hence $f^{-1}(x)=2+e^{x-1}$, with domain $\mathbb{R}$ and range $(2,\infty)$ — the domain and range of
$f$, exchanged, as they must be.

**Checks.** $f(3)=\ln 1+1=1$ and $f^{-1}(1)=2+e^{0}=3$ ✓. Also $f\!\left(2+\tfrac1e\right)=
\ln\left(\tfrac1e\right)+1=-1+1=0$ ✓.

## Challenge

**38.**

**(a)** At $t=0$, $e^{-r\cdot0}=1$, so

$$P(0)=\frac{K}{1+A} .$$

Setting $P(0)=P_0$ and solving, $1+A=\dfrac{K}{P_0}$, hence

$$A=\frac{K}{P_0}-1=\frac{K-P_0}{P_0}.$$

This is positive exactly when $P_0<K$, which is why the model is stated for $0<P_0<K$.

**(b) Strict increase.** Let $t_1<t_2$. Since $r>0$, $-rt_1>-rt_2$; since $e^{u}$ is strictly
increasing, $e^{-rt_1}>e^{-rt_2}$; multiplying by $A>0$ and adding $1$ preserves the inequality:

$$1+Ae^{-rt_1}>1+Ae^{-rt_2}>0 .$$

Taking reciprocals reverses the inequality, and multiplying by $K>0$ preserves the new order:

$$\frac{K}{1+Ae^{-rt_1}}<\frac{K}{1+Ae^{-rt_2}}, \qquad\text{i.e.}\qquad P(t_1)<P(t_2).$$

So $P$ is strictly increasing. $\blacksquare$

**(c) Limit.** Write $e^{-rt}=\left(e^{-r}\right)^{t}$ with $0<e^{-r}<1$. A number in $(0,1)$ raised to
a large power tends to $0$; hence $e^{-rt}\to0$ as $t\to\infty$, so

$$P(t)=\frac{K}{1+Ae^{-rt}}\longrightarrow\frac{K}{1+0}=K .$$

$\blacksquare$

**(d) The halfway time.** Set $P(t)=\dfrac K2$:

$$\frac{K}{1+Ae^{-rt}}=\frac K2 \;\Longrightarrow\; 1+Ae^{-rt}=2 \;\Longrightarrow\; Ae^{-rt}=1
\;\Longrightarrow\; e^{rt}=A \;\Longrightarrow\; t=\frac{\ln A}{r}.$$

**Why growth is fastest there.** The absolute growth rate of a logistic population is proportional to
$P(K-P)$, the product of the current population and the remaining room. The quadratic $P(K-P)$ is a
downward parabola with roots at $P=0$ and $P=K$, maximal at its vertex $P=K/2$. So the steepest part of
the S-curve is at half the carrying capacity — which is exactly the time just found. (Calculus confirms
this by locating the inflection point.)

**Check with numbers.** $K=1000$, $P_0=100$ gives $A=9$ and $P(0)=1000/10=100$ ✓; the halfway time is
$t=\ln 9/r$, and $P=500$ there ✓.

**39.**

**Domain.** The logarithm requires $3^x-1>0$, i.e. $3^x>1$, i.e. $x>0$.

**Solving.** Convert to exponential form:

$$\log_2\left(3^x-1\right)=x \;\Longrightarrow\; 3^x-1=2^{x} \;\Longrightarrow\; 3^{x}-2^{x}=1 .$$

Try $x=1$: $3-2=1$ ✓. So $x=1$ is a solution.

**Uniqueness.** For $x>0$ write

$$3^{x}-2^{x}=2^{x}\left[\left(\tfrac32\right)^{x}-1\right].$$

* $2^{x}$ is strictly increasing and positive on $(0,\infty)$.
* $\left(\tfrac32\right)^{x}$ is strictly increasing because $\tfrac32>1$ (Theorem 8.4), so
  $\left(\tfrac32\right)^{x}-1$ is strictly increasing and positive on $(0,\infty)$.

The product of two positive strictly increasing functions is strictly increasing: if $0<x_1<x_2$ then
both factors at $x_2$ exceed the corresponding factors at $x_1$, and all four numbers are positive, so
the product at $x_2$ is larger. Therefore $3^{x}-2^{x}$ is strictly increasing on $(0,\infty)$ and can
equal $1$ at most once.

Since $x=1$ is a solution, it is the only one. $\blacksquare$

**Check.** $\log_2\left(3^{1}-1\right)=\log_2 2=1$ ✓.

**Remark.** For $x\le0$ the domain condition already fails, so no further candidates need checking; and
indeed $3^{x}-2^{x}\le0$ there.

**40.**

Suppose, for contradiction, that $\log_2 3$ is rational. Since $2^1<3<2^2$, we have $1<\log_2 3<2$, so
we may write

$$\log_2 3=\frac pq$$

with integers $p,q>0$. By Definition 7.5, $2^{p/q}=3$. Raising both sides to the power $q$ gives

$$2^{p}=3^{q}.$$

Now $2^p$ is a product of $2$'s, so its only prime divisor is $2$; $3^q$ is a product of $3$'s, so its
only prime divisor is $3$. Two positive integers with different sets of prime divisors cannot be equal
(unique prime factorisation). Equivalently, $2^p$ is even while $3^q$ is odd.

This contradiction shows that $\log_2 3$ is irrational. $\blacksquare$

**Consequence.** The change of base formula $\log_2 3=\dfrac{\ln3}{\ln2}$ therefore expresses an
irrational number as a ratio of two transcendental ones; nothing about the *form* of an expression
guarantees that its value is rational.

**Numerical check.** $\log_2 3=1.5849625\ldots$, whose continued fraction begins $1, 1, 1, 2, 2, 3,
1, 5,\dots$ — an infinite, non-repeating expansion, consistent with irrationality.
