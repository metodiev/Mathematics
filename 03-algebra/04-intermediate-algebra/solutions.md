# Intermediate Algebra — Solutions

> [Tutorial](README.md) · [Exercises](exercises.md) · 36 worked solutions

Every solution shows the algebra and a check. For radical equations the check is performed in the
original equation, since squaring can create extraneous candidates.

## Beginner

**1.**

Use the definition of a negative exponent:
$$3^{-2}=\frac{1}{3^2}=\frac19,\qquad 2^{-1}=\frac{1}{2^1}=\frac12.$$
Then
$$\frac19+\frac12=\frac{2}{18}+\frac{9}{18}=\boxed{\frac{11}{18}}.$$

**2.**

Use the quotient law for each variable separately:
$$\frac{x^4y^{-2}}{x^2y^3}=x^{4-2}y^{-2-3}=x^2y^{-5}.$$
Since $y\neq0$, this may be written
$$\boxed{\frac{x^2}{y^5}}.$$
Check with $x=2$, $y=2$: the original is $\frac{16\cdot\frac14}{4\cdot8}=\frac{4}{32}=\frac18$;
the simplified expression is $\frac{4}{32}=\frac18$. They agree.

**3.**

Extract the largest square factor from each radicand:
$$\sqrt{50}=\sqrt{25\cdot2}=5\sqrt2,\qquad
\sqrt{18}=\sqrt{9\cdot2}=3\sqrt2,\qquad
\sqrt8=\sqrt{4\cdot2}=2\sqrt2.$$
All three are like radicals, so add their coefficients:
$$5\sqrt2+3\sqrt2-2\sqrt2=(5+3-2)\sqrt2=\boxed{6\sqrt2}.$$
Check numerically: $\sqrt{50}\approx7.071$, $\sqrt{18}\approx4.243$, $\sqrt8\approx2.828$, and
$7.071+4.243-2.828=8.486$, while $6\sqrt2\approx8.485$. The small difference is rounding.

**4.**

Extract perfect cubes:
$$\sqrt[3]{54}=\sqrt[3]{27\cdot2}=3\sqrt[3]{2},\qquad
\sqrt[3]{16}=\sqrt[3]{8\cdot2}=2\sqrt[3]{2}.$$
Therefore
$$3\sqrt[3]{2}-2\sqrt[3]{2}=\boxed{\sqrt[3]{2}}.$$
Check: $\sqrt[3]{54}\approx3.780$, $\sqrt[3]{16}\approx2.520$, and the difference is
$\approx1.260$, while $\sqrt[3]{2}\approx1.260$.

**5.**

Multiply numerator and denominator by $\sqrt3$:
$$\frac{6}{\sqrt3}=\frac{6\sqrt3}{\sqrt3\cdot\sqrt3}=\frac{6\sqrt3}{3}=\boxed{2\sqrt3}.$$
Check numerically: $6/\sqrt3\approx3.464$, and $2\sqrt3\approx3.464$.

**6.**

Multiply by the conjugate $\sqrt5-1$:
$$\begin{aligned}
\frac{2}{\sqrt5+1}
&=\frac{2(\sqrt5-1)}{(\sqrt5+1)(\sqrt5-1)}\\
&=\frac{2(\sqrt5-1)}{5-1}\\
&=\frac{2(\sqrt5-1)}{4}\\
&=\boxed{\frac{\sqrt5-1}{2}}.
\end{aligned}$$
Check numerically: $\sqrt5\approx2.236$, so the original is $2/3.236\approx0.618$, and
$(\sqrt5-1)/2\approx0.618$.

**7.**

Factor both polynomials:
$$x^2-9=(x-3)(x+3),$$
$$x^2+x-12=(x+4)(x-3).$$
The domain excludes $x=-4$ and $x=3$, where the denominator vanishes. For $x\neq-4,3$,
$$\frac{(x-3)(x+3)}{(x+4)(x-3)}=\boxed{\frac{x+3}{x+4}}.$$
The domain is $\mathbb{R}\setminus\{-4,3\}$. Check with $x=0$: the original is
$\frac{-9}{-12}=\frac34$, and the simplified expression is $\frac34$.

**8.**

Multiply numerators and denominators:
$$\frac{3}{x}\cdot\frac{x^2}{9}=\frac{3x^2}{9x}=\frac{x}{3},$$
where $x\neq0$. Therefore
$$\boxed{\frac{x}{3}}.$$
Check with $x=6$: the original is $\frac36\cdot\frac{36}{9}=\frac12\cdot4=2$, and $\frac63=2$.

**9.**

Rewrite division as multiplication by the reciprocal:
$$\frac{x^2-1}{x+2}\div\frac{x-1}{x^2-4}
=\frac{x^2-1}{x+2}\cdot\frac{x^2-4}{x-1}.$$
Factor everything:
$$=\frac{(x-1)(x+1)}{x+2}\cdot\frac{(x-2)(x+2)}{x-1}.$$
Cancel the common factors $x-1$ and $x+2$:
$$=(x+1)(x-2)=x^2-x-2.$$
The excluded values are $x=-2$ (first denominator), $x=2$ and $x=-2$ (second denominator), and
$x=1$ (numerator of the divisor). Hence
$$\boxed{x^2-x-2,\quad x\neq-2,1,2}.$$
Check with $x=0$: the original is $\frac{-1}{2}\div\frac{-1}{-4}=-\frac12\div\frac14=-2$; the
simplified expression is $0-0-2=-2$.

**10.**

Use synthetic division with $c=-2$ and coefficients $2,1,-5,2$:

| $c=-2$ | $2$ | $1$ | $-5$ | $2$ |
|---|---|---|---|---|
| bring down | $2$ |  |  |  |
| multiply and add |  | $2(-2)+1=-3$ |  |  |
| multiply and add |  |  | $(-3)(-2)+(-5)=1$ |  |
| multiply and add |  |  |  | $1(-2)+2=0$ |

The bottom row is $2,-3,1,0$, so the quotient is
$$\boxed{2x^2-3x+1}$$
and the remainder is $\boxed{0}$. Check by multiplying:
$$(x+2)(2x^2-3x+1)=2x^3-3x^2+x+4x^2-6x+2=2x^3+x^2-5x+2.$$

**11.**

The remainder theorem says the remainder upon division by $x+2=x-(-2)$ is the value at $c=-2$.
Compute
$$f(-2)=(-2)^3+2(-2)^2-5(-2)+1=-8+8+10+1=\boxed{11}.$$
Check by synthetic division with $c=-2$:
$$1,\ 2,\ -5,\ 1\ \longrightarrow\ 1,\ 0,\ -5,\ 11,$$
so the remainder is indeed $11$.

**12.**

Use $(a+b)^3=a^3+3a^2b+3ab^2+b^3$ with $a=2x$ and $b=-1$:
$$\begin{aligned}
(2x-1)^3
&=(2x)^3+3(2x)^2(-1)+3(2x)(-1)^2+(-1)^3\\
&=8x^3-12x^2+6x-1.
\end{aligned}$$
$$\boxed{8x^3-12x^2+6x-1}$$
Check with $x=1$: $(2-1)^3=1$, and $8-12+6-1=1$.

## Intermediate

**13.**

Apply the power of a product and the power of a power:
$$(8x^6)^{2/3}=8^{2/3}\left(x^6\right)^{2/3}=4x^4,$$
because $8^{2/3}=(\sqrt[3]{8})^2=2^2=4$. Also
$$(4x^4)^{1/2}=4^{1/2}\left(x^4\right)^{1/2}=2x^2,$$
where $x>0$ allows us to write $\sqrt{x^4}=x^2$. Therefore
$$\frac{4x^4}{2x^2}=\boxed{2x^2}.$$
Check with $x=1$: the original is $8^{2/3}/4^{1/2}=4/2=2$, and $2x^2=2$.

**14.**

Use $\sqrt[4]{a^4}=|a|$ and $\sqrt[4]{a^8}=a^2$ for the even powers:
$$\sqrt[4]{16x^4y^8}=16^{1/4}\sqrt[4]{x^4}\sqrt[4]{y^8}=2|x|\,y^2.$$
$$\boxed{2|x|y^2}$$
The absolute value on $x$ is necessary because $x^4$ does not remember the sign of $x$, while the
fourth root is nonnegative. The factor $y^2$ is already nonnegative, so no absolute value is needed
there. Check with $x=-2$, $y=1$: the radicand is $16\cdot(-2)^4\cdot1^8=16\cdot16=256$, and
$\sqrt[4]{256}=4$; the simplified expression gives $2|{-2}|\cdot1=4$. They agree.

**15.**

Let $a=\sqrt[3]{2}$. Use the identity
$$(a-1)(a^2+a+1)=a^3-1.$$
Since $a^3=2$, the denominator of
$$\frac{1}{a-1}=\frac{a^2+a+1}{(a-1)(a^2+a+1)}$$
becomes $2-1=1$. Therefore
$$\boxed{\sqrt[3]{4}+\sqrt[3]{2}+1}.$$
Check numerically: $\sqrt[3]{2}\approx1.2599$, so the original is $1/0.2599\approx3.847$; the answer
is $1.5874+1.2599+1\approx3.847$.

**16.**

The common denominator is $(x-2)(x+2)=x^2-4$:
$$\begin{aligned}
\frac{1}{x-2}+\frac{3}{x+2}
&=\frac{x+2}{(x-2)(x+2)}+\frac{3(x-2)}{(x-2)(x+2)}\\
&=\frac{x+2+3x-6}{x^2-4}\\
&=\frac{4x-4}{x^2-4}\\
&=\boxed{\frac{4(x-1)}{(x-2)(x+2)}},\qquad x\neq\pm2.
\end{aligned}$$
Check with $x=0$: the original is $-\frac12+\frac32=1$, and the answer is $\frac{-4}{-4}=1$.

**17.**

Combine the numerator and denominator into single fractions:
$$\frac{1+\frac1x}{1-\frac1x}
=\frac{\frac{x+1}{x}}{\frac{x-1}{x}}
=\frac{x+1}{x}\cdot\frac{x}{x-1}
=\boxed{\frac{x+1}{x-1}},$$
with $x\neq0,1$. Check with $x=3$: the original is $\frac{1+1/3}{1-1/3}=\frac{4/3}{2/3}=2$, and
$\frac{3+1}{3-1}=2$.

**18.**

Simplify the numerator first:
$$\frac{x}{x-1}-1=\frac{x-(x-1)}{x-1}=\frac{1}{x-1}.$$
Therefore
$$\frac{\frac{1}{x-1}}{\frac{1}{x-1}}=1,$$
with $x\neq1$. The answer is $\boxed{1}$ (for $x\neq1$). Check with $x=2$: the numerator is
$\frac21-1=1$, the denominator is $\frac11=1$, and the quotient is $1$.

**19.**

The domain requires $3x+1\ge0$, so $x\ge-\frac13$. Since the left side is nonnegative, any solution
must also have $x-1\ge0$, that is, $x\ge1$. Square both sides:
$$\begin{aligned}
3x+1&=(x-1)^2\\
3x+1&=x^2-2x+1\\
0&=x^2-5x\\
0&=x(x-5).
\end{aligned}$$
The candidates are $x=0$ and $x=5$. The candidate $x=0$ violates $x\ge1$ and is extraneous. Check
$x=5$:
$$\sqrt{3\cdot5+1}=\sqrt{16}=4,\qquad 5-1=4.$$
The only solution is $\boxed{x=5}$.

**20.**

The domain requires $x\ge-5$, and the right side must be nonnegative, so $x\ge1$. Square:
$$\begin{aligned}
x+5&=(x-1)^2\\
x+5&=x^2-2x+1\\
0&=x^2-3x-4\\
0&=(x-4)(x+1).
\end{aligned}$$
The candidates are $x=4$ and $x=-1$. At $x=-1$ the right side is $-2$, so it cannot equal a
nonnegative square root; it is extraneous. At $x=4$,
$$\sqrt{9}=3=4-1,$$
so the solution is $\boxed{x=4}$.

**21.**

Cube both sides. Cubing is one-to-one on $\mathbb{R}$, so no extraneous solutions can arise:
$$\begin{aligned}
\sqrt[3]{2x-1}&=-3\\
2x-1&=(-3)^3=-27\\
2x&=-26\\
x&=-13.
\end{aligned}$$
$$\boxed{x=-13}$$
Check: $2(-13)-1=-27$, and $\sqrt[3]{-27}=-3$.

**22.**

Use synthetic division with $c=2$ and coefficients $3,-5,2,-7$:

| $c=2$ | $3$ | $-5$ | $2$ | $-7$ |
|---|---|---|---|---|
| bring down | $3$ |  |  |  |
| multiply and add |  | $6+(-5)=1$ |  |  |
| multiply and add |  |  | $2+2=4$ |  |
| multiply and add |  |  |  | $8+(-7)=1$ |

The quotient is $\boxed{3x^2+x+4}$ and the remainder is $\boxed{1}$. Check by the remainder theorem:
$$3(2)^3-5(2)^2+2(2)-7=24-20+4-7=1.$$

**23.**

Since $x=2$ is a root, divide by $x-2$. The coefficients of $x^3+2x^2-5x-6$ are $1,2,-5,-6$;
synthetic division with $c=2$ gives:
$$1,\ 2,\ -5,\ -6\ \longrightarrow\ 1,\ 4,\ 3,\ 0.$$
Thus
$$x^3+2x^2-5x-6=(x-2)(x^2+4x+3).$$
Factor the quadratic:
$$x^2+4x+3=(x+3)(x+1).$$
Therefore
$$\boxed{(x-2)(x+3)(x+1)}.$$
Check with $x=2$: the original is $8+8-10-6=0$, and the factor $x-2$ is zero. Expanding
$(x-2)(x+3)(x+1)$ gives $(x-2)(x^2+4x+3)=x^3+2x^2-5x-6$, as required.

**24.**

Group the first two and last two terms:
$$\begin{aligned}
3x^3-2x^2-12x+8
&=x^2(3x-2)-4(3x-2)\\
&=(3x-2)(x^2-4)\\
&=(3x-2)(x-2)(x+2).
\end{aligned}$$
$$\boxed{(3x-2)(x-2)(x+2)}$$
Check by expanding:
$$(3x-2)(x^2-4)=3x^3-2x^2-12x+8.$$

## Advanced

**25.**

Use the binomial theorem with $a=2x$, $b=-3$ and $n=4$. The coefficients are $1,4,6,4,1$:
$$\begin{aligned}
(2x-3)^4
&=(2x)^4+4(2x)^3(-3)+6(2x)^2(-3)^2+4(2x)(-3)^3+(-3)^4\\
&=16x^4-96x^3+216x^2-216x+81.
\end{aligned}$$
$$\boxed{16x^4-96x^3+216x^2-216x+81}$$
Check with $x=1$: $(2-3)^4=1$, and $16-96+216-216+81=1$.

**26.**

The general term is
$$\binom8k(2x)^{8-k}(-1)^k.$$
The power of $x$ is $8-k$, so set $8-k=5$, giving $k=3$. The coefficient is
$$\binom83 2^5(-1)^3=56\cdot32\cdot(-1)=-1792.$$
$$\boxed{-1792}$$
Check: the term is $-1792x^5$, and the sign is negative because $k=3$ is odd.

**27.**

Let $u=x^{1/3}$. Then $x^{2/3}=u^2$, and the equation becomes
$$u^2+u-2=0\iff(u+2)(u-1)=0.$$
Thus $u=-2$ or $u=1$. Cubing is one-to-one, so
$$x=(-2)^3=-8\quad\text{or}\quad x=1^3=1.$$
$$\boxed{x=-8\text{ or }x=1}$$
Check: $(-8)^{2/3}=4$ and $(-8)^{1/3}=-2$, so $4-2-2=0$. Also $1^{2/3}=1$ and $1^{1/3}=1$, so
$1+1-2=0$.

**28.**

The domain requires $x\ge1$. Isolate one radical:
$$\sqrt{x+4}=1+\sqrt{x-1}.$$
Both sides are nonnegative, so squaring is reversible:
$$\begin{aligned}
x+4&=1+2\sqrt{x-1}+(x-1)\\
x+4&=x+2\sqrt{x-1}\\
4&=2\sqrt{x-1}\\
2&=\sqrt{x-1}\\
4&=x-1\\
x&=5.
\end{aligned}$$
$$\boxed{x=5}$$
Check: $\sqrt{5+4}-\sqrt{5-1}=3-2=1$. No other candidate arose, and $x=5$ satisfies the domain.

**29.**

Factor the difference of squares and the difference of cubes:
$$x^2-4=(x-2)(x+2),\qquad x^3-8=(x-2)(x^2+2x+4).$$
The first fraction simplifies, for $x\neq2$:
$$\frac{x^2-4}{x^3-8}
=\frac{(x-2)(x+2)}{(x-2)(x^2+2x+4)}
=\frac{x+2}{x^2+2x+4}.$$
Then
$$\frac{x+2}{x^2+2x+4}\div\frac{x+2}{x^2+2x+4}=1,$$
provided $x+2\neq0$ and $x^2+2x+4\neq0$. The quadratic has discriminant $4-16=-12<0$, so it is
never zero. The domain exclusions are $x=2$ (original denominator) and $x=-2$ (divisor's numerator).
Therefore
$$\boxed{1,\quad x\neq\pm2}.$$
Check with $x=0$: the original is $\frac{-4}{-8}\div\frac{2}{4}=\frac12\div\frac12=1$.

**30.**

By the factor theorem, $x-3$ is a factor exactly when $f(3)=0$. Compute
$$f(3)=2(3)^3-5(3)^2+k(3)-3=54-45+3k-3=6+3k.$$
Set $6+3k=0$:
$$3k=-6\iff k=-2.$$
$$\boxed{k=-2}$$
Check: with $k=-2$, $f(3)=54-45-6-3=0$, so $x-3$ is indeed a factor.

**31.**

Suppose, for contradiction, that $\sqrt2$ is rational. Then we can write
$$\sqrt2=\frac pq,$$
where $p,q$ are positive integers with $\gcd(p,q)=1$ (the fraction is in lowest terms). Squaring
gives
$$2=\frac{p^2}{q^2}\iff p^2=2q^2.$$
Thus $p^2$ is even. If $p$ were odd, then $p=2k+1$ for some integer $k$, and
$$p^2=4k^2+4k+1=2(2k^2+2k)+1$$
would be odd, a contradiction. Hence $p$ is even; write $p=2m$. Substituting:
$$(2m)^2=2q^2\iff4m^2=2q^2\iff q^2=2m^2.$$
The same argument shows $q$ is even. But then $p$ and $q$ are both divisible by $2$, contradicting
$\gcd(p,q)=1$. Therefore no such integers exist, and $\sqrt2$ is irrational. $\square$

## Challenge

**32.**

Look for a square of the form $(a+b)^2=a^2+2ab+b^2$ with $2ab=2\sqrt2$. Taking $a=\sqrt2$ and $b=1$
gives
$$(\sqrt2+1)^2=2+2\sqrt2+1=3+2\sqrt2.$$
Since $\sqrt2+1>0$, it is the principal square root:
$$\boxed{\sqrt{3+2\sqrt2}=\sqrt2+1}.$$
Similarly,
$$(\sqrt2-1)^2=2-2\sqrt2+1=3-2\sqrt2,$$
and $\sqrt2-1>0$ because $\sqrt2>1$. Therefore
$$\boxed{\sqrt{3-2\sqrt2}=\sqrt2-1}.$$
Check numerically: $\sqrt2+1\approx2.414$, and $2.414^2\approx5.828=3+2\sqrt2$. Also
$\sqrt2-1\approx0.414$, and $0.414^2\approx0.172=3-2\sqrt2$.

**33.**

The domain requires $x\ge1$. Isolate the radical:
$$\sqrt{x-1}=3-x.$$
The left side is nonnegative, so any solution must satisfy $3-x\ge0$, i.e. $x\le3$. Square:
$$\begin{aligned}
x-1&=(3-x)^2\\
x-1&=9-6x+x^2\\
0&=x^2-7x+10\\
0&=(x-2)(x-5).
\end{aligned}$$
The candidates are $x=2$ and $x=5$. The candidate $x=5$ violates $x\le3$; check it directly:
$5+\sqrt4=7\neq3$, so it is extraneous. The candidate $x=2$ gives $2+\sqrt1=3$, so it works.
$$\boxed{x=2}$$

**34.**

Let $u=x^{1/3}$. Then $x^{2/3}=u^2$, and the equation becomes
$$2u^2+u-1=0.$$
Factor:
$$(2u-1)(u+1)=0,$$
so $u=\frac12$ or $u=-1$. Cubing gives
$$x=\left(\frac12\right)^3=\frac18\quad\text{or}\quad x=(-1)^3=-1.$$
$$\boxed{x=\frac18\text{ or }x=-1}$$
Check: for $x=\frac18$, $x^{2/3}=\frac14$ and $x^{1/3}=\frac12$, so
$2\cdot\frac14+\frac12-1=\frac12+\frac12-1=0$. For $x=-1$, $x^{2/3}=1$ and $x^{1/3}=-1$, so
$2-1-1=0$. Both are valid.

**35.**

**Combinatorial argument.** Let $S=\{1,2,\dots,n\}$. Every subset of $S$ has exactly one size $k$,
where $0\le k\le n$, and there are $\binom nk$ subsets of size $k$. Therefore the total number of
subsets is
$$\sum_{k=0}^{n}\binom nk.$$
On the other hand, each of the $n$ elements can be either included or excluded independently, giving
$2$ choices per element and hence $2^n$ subsets. The two counts describe the same collection, so
$$\sum_{k=0}^{n}\binom nk=2^n.$$

**Algebraic argument.** In the binomial theorem
$$(a+b)^n=\sum_{k=0}^{n}\binom nk a^{n-k}b^k,$$
substitute $a=1$ and $b=1$. Then $a^{n-k}=1$ and $b^k=1$ for every $k$, so
$$2^n=(1+1)^n=\sum_{k=0}^{n}\binom nk.$$
Both arguments prove the same identity. $\square$

**36.**

Complete the square by adding and subtracting $4x^2$:
$$\begin{aligned}
x^4+4
&=x^4+4x^2+4-4x^2\\
&=(x^2+2)^2-(2x)^2.
\end{aligned}$$
This is a difference of squares, so
$$x^4+4=(x^2+2-2x)(x^2+2+2x)=(x^2-2x+2)(x^2+2x+2).$$
$$\boxed{(x^2-2x+2)(x^2+2x+2)}$$
Check by expanding:
$$(x^2+2)^2-(2x)^2=x^4+4x^2+4-4x^2=x^4+4.$$
Each quadratic factor has discriminant $(-2)^2-4(1)(2)=-4$ or $2^2-4(1)(2)=-4$, so neither factors
further over the real numbers.
