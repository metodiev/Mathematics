# Polynomial and Rational Functions — Solutions

> [Tutorial](README.md) · [Exercises](exercises.md) · 38 worked solutions

Every solution states the strategy, shows the significant steps, and checks the result by expansion,
substitution or a limit. Division problems record the identity $P=DQ+R$, because the identity is the
content of the division algorithm.

## Beginner

### Solution 1

**(a)** $3x^4-2x+7$: degree $4$, leading coefficient $3$, constant term $7$. Even degree with positive
leading coefficient, so $y \to +\infty$ at both ends.

**(b)** $-x^5+4x^3-x$: degree $5$, leading coefficient $-1$, constant term $0$. Odd degree with negative
leading coefficient, so $y \to +\infty$ as $x \to -\infty$ and $y \to -\infty$ as $x \to +\infty$.

**(c)** $2x^2-8x+1$: degree $2$, leading coefficient $2$, constant term $1$. Both ends go to $+\infty$.

**(d)** $-4x^3+x^2$: degree $3$, leading coefficient $-4$, constant term $0$. As $x \to -\infty$,
$-4x^3 \to +\infty$; as $x \to +\infty$, $-4x^3 \to -\infty$.

**Method.** End behaviour depends only on the degree (parity) and the sign of the leading coefficient
(Proposition 8.6); the other coefficients affect the middle of the graph, not its ends.

### Solution 2

Divide leading terms, multiply and subtract:

* $x^3/x=x^2$; subtract $x^2(x-1)=x^3-x^2$, leaving $-x^2+4x-5$.
* $-x^2/x=-x$; subtract $-x(x-1)=-x^2+x$, leaving $3x-5$.
* $3x/x=3$; subtract $3(x-1)=3x-3$, leaving $-2$.

Hence $x^3-2x^2+4x-5=(x-1)(x^2-x+3)-2$.

**Check** by expansion: $(x-1)(x^2-x+3)=x^3-x^2+3x-x^2+x-3=x^3-2x^2+4x-3$, and subtracting $2$ gives
$x^3-2x^2+4x-5$ ✓. The remainder is $-2$, which equals $P(1)=1-2+4-5=-2$, as the remainder theorem
requires.

### Solution 3

The coefficients of $x^3-7x+6$ are $1,0,-7,6$ — the missing $x^2$ term must be present as $0$.

$$\begin{array}{r|rrrr}
2 & 1 & 0 & -7 & 6\\
  &   & 2 &  4 & -6\\
\hline
  & 1 & 2 & -3 & 0
\end{array}$$

Quotient $x^2+2x-3$, remainder $0$. Factor the quotient: $x^2+2x-3=(x+3)(x-1)$. Hence

$$x^3-7x+6=(x-2)(x+3)(x-1),$$

with roots $2,1,-3$.

**Check.** $P(2)=8-14+6=0$ ✓; the product $(x-2)(x+3)(x-1)$ has constant term
$(-2)(3)(-1)=6$ ✓ and leading coefficient $1$ ✓.

### Solution 4

By the remainder theorem, $P(3)$ is the remainder on division by $x-3$. Directly,

$$P(3)=2(27)-4(9)+3-5=54-36+3-5=16 .$$

Synthetic division confirms it:

$$\begin{array}{r|rrrr}
3 & 2 & -4 & 1 & -5\\
  &   &  6 & 6 & 21\\
\hline
  & 2 &  2 & 7 & 16
\end{array}$$

The quotient is $2x^2+2x+7$ and the remainder $16$.

### Solution 5

**(a)** $P(2)=8-12+4=0$, so $x-2$ is a factor. Indeed $x^3-3x^2+4=(x-2)^2(x+1)$, so $x-2$ divides twice:
the root $2$ has multiplicity $2$.

**(b)** $P(2)=8+4-8=4 \ne 0$, so $x-2$ is not a factor. The remainder on division by $x-2$ is $4$.

**(c)** $P(2)=16-16+12-16+4=0$, so $x-2$ is a factor. Division gives
$x^4-2x^3+3x^2-8x+4=(x-2)(x^3+3x-2)$.

**Method.** The factor theorem turns "is $x-2$ a factor?" into the single evaluation $P(2)$ — no division
needed to answer the yes/no question, though division is needed to find the cofactor.

### Solution 6

$P(x)=x^3(x-2)^2(x+1)$.

* Degree: $3+2+1=6$; leading coefficient $1$ (the product of the leading coefficients, all $1$).
* Zeros: $x=0$ with multiplicity $3$, $x=2$ with multiplicity $2$, $x=-1$ with multiplicity $1$.
* Behaviour: at $0$ the multiplicity is odd, so the graph **crosses**, with a horizontal tangent because
  the multiplicity is at least $3$; at $2$ the multiplicity is even, so the graph **touches** and turns
  back; at $-1$ the multiplicity is $1$, so the graph **crosses** transversally.
* End behaviour: even degree, positive leading coefficient, so $+\infty$ at both ends.

### Solution 7

$f(x)=-2(x-1)(x+3)^2(x-4)$ has leading term $-2x^4$.

* End behaviour: $y \to -\infty$ as $x \to \pm\infty$.
* At $x=1$ (multiplicity $1$): crosses.
* At $x=-3$ (multiplicity $2$): touches and turns back; since $f$ is negative at both ends and the other
  factors are $-(x-1)(x-4)$, let us check the sign: at $x=-3$ the factor $(x-1)(x-4)=(-4)(-7)=28>0$, so
  near $-3$ the value $-2\cdot28\cdot(x+3)^2<0$: the graph touches the axis from below.
* At $x=4$ (multiplicity $1$): crosses.

**Check of signs.** At $x=0$: $f(0)=-2(-1)(9)(-4)=-72<0$ ✓, consistent with being below the axis between
$-3$ and $4$.

### Solution 8

**(a)** $x^2-9=(x-3)(x+3) \ne 0$: domain $\mathbb{R}\setminus\{-3,3\}$.

**(b)** $x^2+1 \ge 1>0$ for all $x$: domain $\mathbb{R}$.

**(c)** $x^2-2x=x(x-2) \ne 0$: domain $\mathbb{R}\setminus\{0,2\}$.

**(d)** $x^2+4>0$: domain $\mathbb{R}$.

**Principle.** Only zeros of the denominator are excluded; a numerator that vanishes creates an
$x$-intercept (or a hole), never a domain restriction.

### Solution 9

**(a)** $x-3=0$ gives $x=3$; the numerator at $3$ is $7 \ne 0$, so $x=3$ is a vertical asymptote.

**(b)** $x^2-4=(x-2)(x+2)$; the numerator $x$ is nonzero at both $\pm2$, so $x=2$ and $x=-2$ are vertical
asymptotes.

**(c)** $h(x)=\dfrac{x-1}{(x-1)^2}=\dfrac{1}{x-1}$ for $x \ne 1$. The single remaining zero of the
denominator is $x=1$, so $x=1$ is a vertical asymptote. There is *no* hole here: the factor cancels only
once, and the denominator still vanishes to first order.

### Solution 10

**(a)** Equal degrees ($2$), leading coefficients $3$ and $1$: $y=3$.

**(b)** Numerator degree $1$, denominator degree $3$: $y=0$.

**(c)** Numerator degree $3$, denominator degree $2$: there is no horizontal asymptote. Division gives
$\dfrac{x^3}{x^2+1}=x-\dfrac{x}{x^2+1}$, so the graph has the slant asymptote $y=x$.

**(d)** Equal degrees ($1$), leading coefficients $5$ and $2$: $y=\dfrac52$.

### Solution 11

Factor both:

$$f(x)=\frac{(x-3)(x+3)}{(x-3)(x-2)} .$$

Domain: $x \ne 3,2$. The factor $x-3$ cancels, so

$$\lim_{x\to3}f(x)=\frac{3+3}{3-2}=6,$$

and the hole is at $(3,6)$. The factor $x-2$ does not cancel, and the reduced numerator at $x=2$ is
$2+3=5 \ne 0$, so $x=2$ is a vertical asymptote.

**Check.** $f$ is undefined at $3$, yet values near $3$ are near $6$: for example $f(3.1)=\frac{6.1}{1.1}
=5.545\ldots$, close to $6$ ✓.

### Solution 12

**(a)** Divide numerator and denominator by $x^2$:
$\dfrac{4x^2-3}{2x^2+x}=\dfrac{4-3/x^2}{2+1/x}\to\dfrac42=2$ as $x\to\infty$.

**(b)** As $x \to 2^+$, $x-2 \to 0^+$, so $\dfrac{1}{x-2}\to+\infty$.

**(c)** As $x \to 1^-$, the numerator $x \to 1>0$ and the denominator $x-1 \to 0^-$, so the quotient
$\to-\infty$.

**Comment.** In (b) and (c) the sign of the denominator decides the direction; a two-sided limit does not
exist, which is exactly what a vertical asymptote means.

### Solution 13

The zeros are $-2,1,3$, all simple, so the sign changes at each.

| Interval | $x+2$ | $x-1$ | $x-3$ | Product |
|---|---|---|---|---|
| $x<-2$ | $-$ | $-$ | $-$ | $-$ |
| $-2<x<1$ | $+$ | $-$ | $-$ | $+$ |
| $1<x<3$ | $+$ | $+$ | $-$ | $-$ |
| $x>3$ | $+$ | $+$ | $+$ | $+$ |

The product is positive on $(-2,1)\cup(3,\infty)$. Endpoints are excluded because the inequality is
strict.

**Check.** $x=0$ gives $(2)(-1)(-3)=6>0$ ✓; $x=2$ gives $(4)(1)(-1)=-4<0$ ✓.

## Intermediate

### Solution 14

Divide leading terms, with $x^3$ present as $0x^3$:

* $3x^4/x^2=3x^2$; subtract $3x^2(x^2-2)=3x^4-6x^2$, leaving $4x^2+x-5$.
* $4x^2/x^2=4$; subtract $4(x^2-2)=4x^2-8$, leaving $x+3$.

The remainder $x+3$ has degree $1<2$, so the process stops:

$$3x^4-2x^2+x-5=(x^2-2)(3x^2+4)+(x+3).$$

**Check.** $(x^2-2)(3x^2+4)=3x^4+4x^2-6x^2-8=3x^4-2x^2-8$, and adding $x+3$ gives
$3x^4-2x^2+x-5$ ✓.

### Solution 15

Synthetic division with $c=-3$: bring down $2$; multiply by $-3$ to get $-6$ and add to $3$ to get $-3$;
multiply $-3$ by $-3$ to get $9$ and add to $-11$ to get $-2$; multiply $-2$ by $-3$ to get $6$ and add
to $-6$ to get $0$.

$$\begin{array}{r|rrrr}
-3 & 2 & 3 & -11 & -6\\
   &   & -6 & 9 & 6\\
\hline
   & 2 & -3 & -2 & 0
\end{array}$$

Quotient $2x^2-3x-2=(2x+1)(x-2)$, remainder $0$. Hence

$$2x^3+3x^2-11x-6=(x+3)(2x+1)(x-2),$$

with roots $-3,-\tfrac12,2$.

**Check** by expansion: $(x+3)(2x^2-3x-2)=2x^3-3x^2-2x+6x^2-9x-6=2x^3+3x^2-11x-6$ ✓.

### Solution 16

Synthetic division by $x-\tfrac12$: bring down $2$; $\tfrac12\cdot2=1$ and $-3+1=-2$;
$\tfrac12\cdot(-2)=-1$ and $4-1=3$; $\tfrac12\cdot3=\tfrac32$ and $-5+\tfrac32=-\tfrac72$.

$$\begin{array}{r|rrrr}
\tfrac12 & 2 & -3 & 4 & -5\\
          &   & 1 & -1 & \tfrac32\\
\hline
          & 2 & -2 & 3 & -\tfrac72
\end{array}$$

Thus $P(x)=\left(x-\tfrac12\right)(2x^2-2x+3)-\tfrac72$. Dividing the quotient by $2$ and using
$2\left(x-\tfrac12\right)=2x-1$,

$$2x^3-3x^2+4x-5=(2x-1)\left(x^2-x+\tfrac32\right)-\tfrac72 .$$

**Check.** $(2x-1)(x^2-x+\tfrac32)=2x^3-2x^2+3x-x^2+x-\tfrac32=2x^3-3x^2+4x-\tfrac32$, and subtracting
$\tfrac72$ gives $2x^3-3x^2+4x-5$ ✓.

### Solution 17

Candidates: $\pm1,\pm2,\pm3,\pm6$ and $\pm\tfrac12,\pm\tfrac32$.

Test $x=2$: $2(8)+4-14-6=16+4-14-6=0$. Synthetic division:

$$\begin{array}{r|rrrr}
2 & 2 & 1 & -7 & -6\\
  &   & 4 & 10 & 6\\
\hline
  & 2 & 5 & 3 & 0
\end{array}$$

Quotient $2x^2+5x+3=(2x+3)(x+1)$. Hence

$$2x^3+x^2-7x-6=(x-2)(2x+3)(x+1),$$

with roots $2,-\tfrac32,-1$.

**Check.** $P(-1)=-2+1+7-6=0$ ✓; $P\left(-\tfrac32\right)=2\left(-\tfrac{27}{8}\right)+\tfrac94+\tfrac{21}{2}-6
=-\tfrac{27}{4}+\tfrac94+\tfrac{42}{4}-\tfrac{24}{4}=0$ ✓.

### Solution 18

**(a)** $P(x)=x^5-3x^4+2x^2-x+7$ has signs $+,-,+,-,+$: four sign changes, so the number of positive roots
is $4$, $2$ or $0$. For $P(-x)=-x^5-3x^4+2x^2+x+7$ the signs are $-, -, +, +, +$: one sign change, so
there is exactly one negative root.

**(b)** $Q(x)=x^4+3x^2+2$ has signs $+,+,+,+$: no sign change, so no positive roots. $Q(-x)=x^4+3x^2+2$ is
the same polynomial, so no negative roots either. Since a quartic has four complex roots counted with
multiplicity, all four are non-real. Indeed $Q(x)=(x^2+1)(x^2+2)$, whose roots are $\pm i$ and
$\pm i\sqrt2$.

**Reading the rule correctly.** Descartes gives a list of *possible* counts with a fixed parity; only in
case (b) does the list collapse to a certainty.

### Solution 19

By the conjugate root theorem, $3+2i$ is also a root. The quadratic with these roots is

$$(x-(3-2i))(x-(3+2i))=(x-3)^2-(2i)^2=(x-3)^2+4=x^2-6x+13 .$$

Its coefficients are real and its discriminant is $36-52=-16<0$, so it has no real roots, consistent with
the pair being genuinely complex.

### Solution 20

The roots must be $2$, $1+i$ and — by the conjugate theorem — $1-i$. Hence

$$P(x)=(x-2)\bigl((x-1)^2+1\bigr)=(x-2)(x^2-2x+2).$$

Expanding: $x^3-2x^2+2x-2x^2+4x-4=x^3-4x^2+6x-4$.

**Check.** $P(2)=8-16+12-4=0$ ✓. Also $P(1+i)$: with $(x-1)^2+1$ vanishing at $x=1+i$ (since
$(i)^2+1=0$), the product vanishes ✓.

### Solution 21

**Domain.** $x^2-4 \ne 0$, so $x \ne \pm2$.

**Intercepts.** Numerator zero at $x=1$: $x$-intercept $(1,0)$. $y$-intercept $f(0)=\dfrac{-1}{-4}=\dfrac14$.

**Asymptotes.** $x=2$ and $x=-2$ are vertical asymptotes (the numerator is $-1$ and $3$ there, nonzero).
The numerator has degree $1$ and the denominator degree $2$, so $y=0$ is a horizontal asymptote.

**Sign chart.**

| Interval | $x-1$ | $x^2-4$ | $f(x)$ |
|---|---|---|---|
| $x<-2$ | $-$ | $+$ | $-$ |
| $-2<x<1$ | $-$ | $-$ | $+$ |
| $1<x<2$ | $+$ | $-$ | $-$ |
| $x>2$ | $+$ | $+$ | $+$ |

**Check.** $f(0)=\tfrac14>0$ ✓ (inside $(-2,1)$); $f(3)=\tfrac25>0$ ✓ (inside $(2,\infty)$);
$f(1.5)=\tfrac{0.5}{-1.75}<0$ ✓.

### Solution 22

Divide:

$$2x^2-3x+1=(x+1)(2x-5)+6,$$

so $f(x)=2x-5+\dfrac{6}{x+1}$. As $x\to\pm\infty$ the fraction tends to $0$, so $y=2x-5$ is the slant
asymptote.

**Verification of the definition:**

$$f(x)-(2x-5)=\frac{6}{x+1}\longrightarrow 0 \quad (x\to\pm\infty).$$

**Check.** $f(0)=1$ and $2(0)-5=-5$, so the graph is $6$ units above the asymptote at $x=0$, matching
$\dfrac{6}{0+1}=6$ ✓.

### Solution 23

Subtract $2$ from both sides:

$$\frac{x-3}{x+1}-2=\frac{x-3-2x-2}{x+1}=\frac{-x-5}{x+1}\le0 .$$

Critical numbers: $-5$ (numerator, included) and $-1$ (denominator, excluded).

| Interval | $-x-5$ | $x+1$ | Quotient |
|---|---|---|---|
| $x<-5$ | $+$ | $-$ | $-$ |
| $-5<x<-1$ | $-$ | $-$ | $+$ |
| $x>-1$ | $-$ | $+$ | $-$ |

The solution is $(-\infty,-5]\cup(-1,\infty)$.

**Check.** $x=-6$: $\dfrac{-9}{-5}=1.8\le2$ ✓, and $-6\le-5$ ✓. $x=-3$: $\dfrac{-6}{-2}=3>2$ ✗, and
$-3\in(-5,-1)$ ✓ (correctly excluded). $x=0$: $-3\le2$ ✓, and $0>-1$ ✓.

### Solution 24

Factor: $x^3-4x=x(x-2)(x+2)$. The zeros are $-2,0,2$, all simple, so the sign alternates. Signs:

| Interval | $x$ | $x-2$ | $x+2$ | Product |
|---|---|---|---|---|
| $x<-2$ | $-$ | $-$ | $-$ | $-$ |
| $-2<x<0$ | $-$ | $-$ | $+$ | $+$ |
| $0<x<2$ | $+$ | $-$ | $+$ | $-$ |
| $x>2$ | $+$ | $+$ | $+$ | $+$ |

Including the zeros (the inequality is non-strict): $(-\infty,-2]\cup[0,2]$.

**Check.** $x=1$: $1-4=-3\le0$ ✓; $x=3$: $27-12=15>0$ ✗ outside ✓; $x=-1$: $-1+4=3>0$ ✗ outside ✓.

### Solution 25

$$A(x)=\frac{0.1x^2+8x+500}{x}=0.1x+8+\frac{500}{x}, \qquad x>0 .$$

The remainder term $\dfrac{500}{x}\to0$, so the slant asymptote is $y=0.1x+8$: average cost grows
linearly, driven by the quadratic term in the cost. At $x=100$,

$$A(100)=0.1(100)+8+\frac{500}{100}=10+8+5=23\ \text{dollars per item}.$$

**Check** directly: $C(100)=0.1(10000)+800+500=1000+800+500=2300$, and $2300/100=23$ ✓.

### Solution 26

**Domain.** $x \ge 0$, since a volume of water cannot be negative; $c$ is defined for all $x \ge 0$.

**Horizontal asymptote.** $\lim_{x\to\infty}\dfrac{20}{100+x}=0$: the concentration tends to zero as the
solution is diluted without bound.

**Values.** $c(100)=\dfrac{20}{200}=0.1$ kg/L.

**Solving $c(x)\le 0.05$.** Since $100+x>0$, multiply without reversing:

$$\frac{20}{100+x}\le\frac{1}{20} \;\Longleftrightarrow\; 400 \le 100+x
\;\Longleftrightarrow\; x \ge 300 .$$

So $300$ litres of water are needed, giving a total volume of $400$ L with $20$ kg of salt, i.e.
$0.05$ kg/L.

**Check.** $c(300)=20/400=0.05$ ✓; $c(299)=20/399\approx0.0501>0.05$ ✓.

## Advanced

### Solution 27

**Remainder theorem.** Let $P$ be a polynomial and $c$ a real number. By the division algorithm
(Theorem 8.1) applied to the divisor $x-c$,

$$P(x)=(x-c)Q(x)+R,$$

where $R$ is a constant because $\deg R<\deg(x-c)=1$. Substituting $x=c$ kills the first term and gives
$P(c)=R$. Hence the remainder is $P(c)$. $\blacksquare$

**Factor theorem.** If $(x-c)\mid P$, then $P(x)=(x-c)Q(x)$ and $P(c)=0$. Conversely, if $P(c)=0$, then the
remainder just computed is $0$, so $P(x)=(x-c)Q(x)$ and $(x-c)\mid P$. $\blacksquare$

**Remark.** Both proofs use only the division algorithm, which itself is proved by induction on the
degree. Nothing about the particular polynomial enters.

### Solution 28

Let $P(x)=\sum_{k=0}^{n}a_kx^k$ with $a_k \in \mathbb{R}$ and let $z$ be a root. Conjugation satisfies
$\overline{u+v}=\bar u+\bar v$, $\overline{uv}=\bar u\bar v$ and $\bar a=a$ for real $a$. Hence

$$P(\bar z)=\sum_k a_k\bar z^k=\sum_k\overline{a_kz^k}=\overline{\sum_k a_kz^k}=\overline{P(z)}
=\overline0=0,$$

so $\bar z$ is a root.

For the multiplicity, write $P(x)=(x-z)^mQ(x)$ with $Q(z)\ne0$ and $m\ge1$ (Definition 5.4). Conjugating
each coefficient of this identity gives $P(x)=(x-\bar z)^m\bar Q(x)$, where $\bar Q$ has the conjugated
coefficients. Since $\bar Q(\bar z)=\overline{Q(z)}\ne0$, the factor $x-\bar z$ occurs exactly $m$ times,
so the multiplicity of $\bar z$ equals that of $z$. $\blacksquare$

### Solution 29

Let $P$ have odd degree $n$ and leading coefficient $a_n>0$; the case $a_n<0$ is symmetric (multiply by
$-1$). By Proposition 8.6, $P(x)/(a_nx^n)\to1$ as $|x|\to\infty$, and since $n$ is odd,
$a_nx^n \to -\infty$ as $x\to-\infty$ and $a_nx^n\to+\infty$ as $x\to+\infty$. Therefore $P(x)\to-\infty$
as $x\to-\infty$ and $P(x)\to+\infty$ as $x\to+\infty$.

Choose $a<0$ with $P(a)<0$ and $b>0$ with $P(b)>0$; such $a,b$ exist because of the limits. $P$ is
continuous, so the intermediate value property gives $c\in(a,b)$ with $P(c)=0$. Hence $P$ has a real
root. $\blacksquare$

**Second proof.** By the fundamental theorem of algebra and the conjugate root theorem, the non-real roots
of $P$ occur in pairs, so the number of real roots has the same parity as $\deg P=n$, which is odd. An odd
number is at least $1$. $\blacksquare$

### Solution 30

**Claim.** A nonzero polynomial of degree $n$ has at most $n$ real roots counted with multiplicity.

*Base case.* If $n=0$, $P$ is a nonzero constant, so it has no roots, and $0 \le 0$.

*Inductive step.* Suppose the claim holds for degree $n-1$, and let $P$ have degree $n$. If $P$ has no
real roots there is nothing to prove. Otherwise let $c$ be a real root. By the factor theorem,
$P(x)=(x-c)Q(x)$ with $\deg Q=n-1$. A root $r \ne c$ of $P$ satisfies $(r-c)Q(r)=0$, hence $Q(r)=0$; so
the roots of $P$ other than $c$ are roots of $Q$. By the induction hypothesis $Q$ has at most $n-1$ real
roots counted with multiplicity, so $P$ has at most $1+(n-1)=n$. $\blacksquare$

**Remark.** Counting with multiplicity means that a root $c$ found above may itself be a root of $Q$; the
induction accounts for that automatically, because the multiplicities add.

### Solution 31

Let $P(x)=a_nx^n+\cdots+a_0$ with integer coefficients, $a_n\ne0$, and let $\frac pq$ be a root in lowest
terms with $q>0$. Substituting and multiplying by $q^n$:

$$a_np^n+a_{n-1}p^{n-1}q+\cdots+a_1pq^{n-1}+a_0q^n=0 .$$

Every term except $a_0q^n$ contains the factor $p$, so

$$a_0q^n=-p\bigl(a_np^{n-1}+a_{n-1}p^{n-2}q+\cdots+a_1q^{n-1}\bigr),$$

which shows that $p\mid a_0q^n$. Because $\gcd(p,q)=1$, also $\gcd(p,q^n)=1$, and Euclid's lemma gives
$p\mid a_0$.

Similarly, every term except $a_np^n$ contains $q$, so $q\mid a_np^n$. Since $\gcd(q,p^n)=1$, Euclid's
lemma gives $q\mid a_n$. $\blacksquare$

**Why lowest terms matter.** Without $\gcd(p,q)=1$ the conclusion fails: $\frac46$ is a root only when
$\frac23$ is, and $4 \nmid 3$.

### Solution 32

Let $P(x)=a x^{d_p}+\cdots$ and $Q(x)=b x^{d_q}+\cdots$ with $a,b\ne0$, and $d_q \ge 1$ or $d_q=0$; in
every case $Q(x)\ne0$ for large $|x|$. Divide numerator and denominator by $x^{d_q}$:

$$f(x)=\frac{a x^{d_p-d_q}+(\text{terms with negative powers of }x)}
{b+(\text{terms with negative powers of }x)} .$$

If $d_p<d_q$, every term in the numerator contains a negative power of $x$ and tends to $0$, while the
denominator tends to $b\ne0$; hence $f(x)\to0$.

If $d_p=d_q$, the numerator tends to $a$ and the denominator to $b$, so $f(x)\to a/b$. $\blacksquare$

**Remark.** The same computation shows that when $d_p>d_q$ the quotient grows like
$\frac abx^{d_p-d_q}$, which is the basis for the slant-asymptote case.

### Solution 33

Factor the numerator: $x^2+3x+2=(x+1)(x+2)$. Hence, for $x\ne-1$,

$$f(x)=\frac{(x+1)(x+2)}{x+1}=x+2 .$$

**Domain.** $x \ne -1$ (the original formula is undefined there).

**Hole.** $\lim_{x\to-1}f(x)=-1+2=1$, so the graph is the line $y=x+2$ with the point $(-1,1)$ removed.

**No vertical asymptote.** A vertical asymptote requires $\lvert f(x)\rvert\to\infty$; here the limit is
the finite number $1$. The zero of the denominator is cancelled by a zero of the numerator, so the
singularity is removable.

### Solution 34

Write

$$f(x)=\frac{x^2-1}{x^2+1}=\frac{(x^2+1)-2}{x^2+1}=1-\frac{2}{x^2+1}.$$

Since $x^2+1 \ge 1$, we have $0<\dfrac{2}{x^2+1}\le2$, so

$$-1 \le f(x)<1,$$

with $f(0)=-1$ (the lower endpoint is attained) and $f(x)\to1$ but $f(x)\ne1$ (the upper endpoint is
not attained, since $\frac{2}{x^2+1}>0$).

**Horizontal asymptote.** As $x\to\pm\infty$, $\dfrac{2}{x^2+1}\to0$, so $f(x)\to1$: the line $y=1$ is a
horizontal asymptote, and the graph lies below it.

**Crossing the axis.** $f(x)=0$ exactly when $x^2-1=0$, i.e. $x=\pm1$: the graph crosses the $x$-axis at
$(\pm1,0)$.

**Is $0$ in the range?** Yes, attained at $x=\pm1$; the range is $[-1,1)$.

## Challenge

### Solution 35

**(a)** By the binomial theorem,

$$(x+1)^4=\sum_{k=0}^{4}\binom{4}{k}x^k1^{4-k}=x^4+4x^3+6x^2+4x+1 .$$

So $x^4+4x^3+6x^2+4x+1=(x+1)^4$.

**(b)** The factorisation exhibits the root $x=-1$ four times, so the multiplicity is $4$: by the
definition, $(x+1)^4$ divides the polynomial and $(x+1)^5$ does not (it has degree $5>4$). With even
multiplicity the graph **touches** the axis at $(-1,0)$ and turns back, lying above the axis on both
sides because $(x+1)^4 \ge 0$. The graph is extremely flat there: at $x=-0.9$ the value is
$(0.1)^4=0.0001$, and at $x=-0.5$ it is $0.0625$.

**Check.** $(-1+1)^4=0$ ✓; the expansion at $x=1$ gives $16$, and $2^4=16$ ✓.

### Solution 36

**Claim.** If $P$ has degree $n$ and $n$ real roots $r_1,\dots,r_n$ counted with multiplicity, then
$P(x)=a_n\prod_{k=1}^{n}(x-r_k)$.

*Proof.* Induct on $n$. For $n=0$ the polynomial is the constant $a_0=a_n$ and the empty product is $1$.

For $n \ge 1$, let $r_1$ be a root. By the factor theorem, $P(x)=(x-r_1)Q(x)$ with $\deg Q=n-1$. A root of
$P$ other than $r_1$ is a root of $Q$, and the multiplicity of $r_1$ as a root of $P$ is one more than its
multiplicity as a root of $Q$; hence $Q$ has $n-1$ real roots counted with multiplicity, namely
$r_2,\dots,r_n$ (with $r_1$ repeated one fewer time). By induction
$Q(x)=a_n\prod_{k=2}^{n}(x-r_k)$, and multiplying by $x-r_1$ gives the claim. $\blacksquare$

**Consequence.** A degree-$n$ polynomial with $n$ real roots is completely determined by its leading
coefficient and its roots.

### Solution 37

Take

$$f(x)=\frac{3(x-2)(x^2+1)}{(x-2)(x+1)^2} .$$

**Hole at $x=2$.** The factor $x-2$ appears in both numerator and denominator, so the function is
undefined at $2$, while

$$\lim_{x\to2}f(x)=\frac{3(2^2+1)}{(2+1)^2}=\frac{3\cdot5}{9}=\frac53,$$

a finite limit. Hence the hole is at $\left(2,\tfrac53\right)$.

**Vertical asymptote $x=-1$.** After cancellation, $f(x)=\dfrac{3(x^2+1)}{(x+1)^2}$ near $-1$; the
numerator tends to $6\ne0$ while the denominator tends to $0^+$, so $f(x)\to+\infty$. No other zero of the
denominator remains, so $x=-1$ is the only vertical asymptote.

**Horizontal asymptote $y=3$.** The numerator has degree $3$ with leading coefficient $3$; the
denominator $(x-2)(x+1)^2$ has degree $3$ with leading coefficient $1$. By Proposition 8.14 the limit is
$3/1=3$.

**No $x$-intercepts.** $f(x)=0$ requires $3(x-2)(x^2+1)=0$, i.e. $x=2$ (since $x^2+1>0$), but $x=2$ is
excluded from the domain. Hence the graph never meets the $x$-axis.

**Check.** $f(0)=\dfrac{3(-2)(1)}{(-2)(1)}=3$, on the horizontal asymptote ✓.

### Solution 38

**(a)** Suppose $f$ had both a horizontal asymptote $y=L$ and a slant asymptote $y=mx+k$ with $m\ne0$.
Then, by definition,

$$\lim_{x\to+\infty}\bigl(f(x)-L\bigr)=0, \qquad \lim_{x\to+\infty}\bigl(f(x)-(mx+k)\bigr)=0 .$$

Subtracting the two relations,

$$\bigl(f(x)-L\bigr)-\bigl(f(x)-(mx+k)\bigr)=mx+k-L \longrightarrow 0 .$$

But $mx+k-L$ is a non-constant linear function (since $m\ne0$), and $|mx+k-L|\to+\infty$. A function
cannot converge to both $0$ and $+\infty$; contradiction. Hence no such pair exists. $\blacksquare$

**(b)** Suppose $y=m_1x+k_1$ and $y=m_2x+k_2$ are both slant asymptotes of $f$. Subtracting the two limit
relations,

$$(m_1-m_2)x+(k_1-k_2)=\bigl(f(x)-(m_2x+k_2)\bigr)-\bigl(f(x)-(m_1x+k_1)\bigr)\longrightarrow 0 .$$

A linear function tends to $0$ only if its slope is $0$: if $m_1\ne m_2$, its magnitude is unbounded.
Hence $m_1=m_2$, and then $k_1-k_2\to0$ forces $k_1=k_2$. So the slant asymptote is unique. $\blacksquare$

**Remark.** Part (b) is the same uniqueness argument as for limits: two objects that both differ from
$f$ by quantities tending to zero must differ from each other by zero.
