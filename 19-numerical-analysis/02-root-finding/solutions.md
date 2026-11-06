# Root Finding — Solutions

> [Tutorial](README.md) · [Exercises](exercises.md) · Complete solutions to all 36 problems

Proposition and theorem numbers refer to the [tutorial](README.md). Every iteration quoted below was
computed, and the tables carry enough digits to make the order visible.

## Beginner

### Solution 1

*Strategy.* Check the signs, then halve the interval keeping the sign change.

$f(2)=8-4-5=-1$ and $f(3)=27-6-5=16$, so $[2,3]$ brackets a root. The steps:

| $n$ | $a_n$ | $b_n$ | $x_n$ | $f(x_n)$ |
|---|---|---|---|---|
| 0 | $2$ | $3$ | $2.5$ | $+5.625$ |
| 1 | $2$ | $2.5$ | $2.25$ | $+1.890625$ |
| 2 | $2$ | $2.25$ | $2.125$ | $+0.3457031$ |

After three midpoints the bracket is $[2,2.125]$, of width $0.125$, so the guaranteed error is
$0.125/2=0.0625$; the true root is $2.0945514815$, and the last midpoint is off by $0.03045$ ✓.

### Solution 2

*Answer.* $26$ steps.

*Method.* Proposition 8.1 gives $\lvert x_n-r\rvert\le(b-a)/2^{n+1}$. With $b-a=1$ and
$\varepsilon=10^{-8}$,
$$
2^{-(n+1)}\le10^{-8}\iff n+1\ge\log_2 10^{8}=26.575\iff n\ge25.575,
$$
so $n=26$ midpoints suffice (the bracket width is then $2^{-26}=1.49\times10^{-8}$).

*Pitfall.* The width criterion $2^{-n}\le10^{-8}$ gives $n=27$; the error criterion is one step weaker
because the midpoint sits in the centre. Both are safe, but only the second is sharp.

### Solution 3

*Method.* $f(0)=-1$, $f(1)=0.4597$.

| $n$ | $a_n$ | $b_n$ | $x_n$ | $f(x_n)$ |
|---|---|---|---|---|
| 0 | $0$ | $1$ | $0.5$ | $-0.377583$ |
| 1 | $0.5$ | $1$ | $0.75$ | $+0.018311$ |
| 2 | $0.5$ | $0.75$ | $0.625$ | $-0.185963$ |

*Answer.* Final bracket $[0.625,0.75]$, width $0.125$; the error of $x_2=0.625$ is at most $0.125$ (its
true error is $0.114$). The next midpoint $0.6875$ would have error at most $0.0625$.

### Solution 4

*Map into itself.* For $x\in[1,2]$, $g(x)=\sqrt{x+2}$ increases, so
$g([1,2])=[\sqrt3,\sqrt4]=[1.732,2]\subset[1,2]$ ✓.

*Contraction.* $g'(x)=1/(2\sqrt{x+2})$, decreasing, so on $[1,2]$
$$
\lvert g'(x)\rvert\le\frac{1}{2\sqrt3}=0.288675=L<1 .
$$
The mean value theorem gives $\lvert g(x)-g(y)\rvert\le L\lvert x-y\rvert$.

*Fixed point.* $x=\sqrt{x+2}$ implies $x^{2}=x+2$, i.e. $x=2$ or $x=-1$; only $x=2$ is in $[1,2]$.
Theorem 7.1 then guarantees convergence from every $x_0\in[1,2]$ with
$\lvert x_n-2\rvert\le L^{n}\lvert x_0-2\rvert$.

### Solution 5

*Hypotheses.* $g(x)=\cos x$ is continuous; for $x\in[0,1]$, $\cos x\in[\cos1,1]=[0.5403,1]\subset[0,1]$ ✓;
$\lvert g'(x)\rvert=\sin x\le\sin1=0.841471=L<1$ ✓.

*Conclusions for $x_0=0.5$.* There is a unique fixed point $r=0.739085\ldots$; the iterates converge;
$\lvert x_n-r\rvert\le0.8415^{n}\cdot0.2391$; the a posteriori bound
$\lvert x_n-r\rvert\le\frac{0.8415}{0.1585}\lvert x_n-x_{n-1}\rvert=5.31\lvert x_n-x_{n-1}\rvert$.

*Remark.* The global constant $0.8415$ is pessimistic: the actual ratios settle at $\lvert g'(r)\rvert=\sin r=0.6736$.
With the global bound, six correct digits need $n$ with $0.8415^{n}\cdot0.239<10^{-6}$, i.e. $n\ge75$;
the actual iteration needs about $35$.

### Solution 6

*Method.* $f'=2x$, so $x_{n+1}=x_n-(x_n^{2}-3)/(2x_n)=\tfrac12(x_n+3/x_n)$.

From $x_0=2$:
$$
x_1=\tfrac12(2+1.5)=1.75,\qquad x_2=\tfrac12(1.75+1.7142857\ldots)=1.7321428571 .
$$

*Errors.* With $\sqrt3=1.7320508075688772$: $\lvert x_1-\sqrt3\rvert=1.7949\times10^{-2}$ and
$\lvert x_2-\sqrt3\rvert=9.205\times10^{-5}$. The error has been squared ($0.0179^{2}=3.2\times10^{-4}$,
and the constant $C=1/(2\sqrt3)=0.2887$ gives $0.2887\cdot0.0179^{2}=9.2\times10^{-5}$ ✓).

### Solution 7

*Method.* $f'=3x^{2}$, $x_{n+1}=x_n-(x_n^{3}-8)/(3x_n^{2})=\tfrac23x_n+\tfrac{8}{3x_n^{2}}$.

From $x_0=3$:
$$
x_1=\tfrac23\cdot3+\tfrac{8}{27}=2.2962962963,\qquad x_2=2.0365874025 .
$$

*Check.* $2.2962962963^{3}=12.1083$, and the next iterate brings the cube to $8.4471$; the third
iterate is $2.0006533585$, already within $6.5\times10^{-4}$. The convergence is quadratic with constant
$\lvert f''(2)\rvert/(2\lvert f'(2)\rvert)=12/24=0.5$.

### Solution 8

*(a)* Ratios: $1.6/4.0=0.40$, $0.64/1.6=0.40$, $0.256/0.64=0.40$. Constant ratio $\Rightarrow$ **linear
convergence with rate $0.4$** (order $1$).

*(b)* Ratios: $10^{-2}$, $10^{-4}$, $10^{-8}$ — not constant. Ratios of squares:
$10^{-4}/(10^{-2})^{2}=1$, $10^{-8}/(10^{-4})^{2}=1$, $10^{-16}/(10^{-8})^{2}=1$. Constant
$\lvert e_{n+1}\rvert/\lvert e_n\rvert^{2}$ $\Rightarrow$ **quadratic convergence with constant $1$**.

*Rule.* Constant ratio $\Rightarrow$ order $1$; constant ratio of squares $\Rightarrow$ order $2$; a
ratio that decreases geometrically (as in (b)'s first column) is the signature of superlinear
convergence.

### Solution 9

*Values.* At $r=\sqrt3$:
- $g(x)=x^{2}+x-3$: $g'=2x+1$, so $g'(\sqrt3)=4.464>1$ — **diverges**.
- $g(x)=3/x$: $g'=-3/x^{2}$, so $g'(\sqrt3)=-1$ — the borderline case. The iteration oscillates with
  period two ($x\mapsto3/x\mapsto x$) and does not converge; the error ratio tends to $1$.
- $g(x)=(x+3/x)/2$: $g'=(1-3/x^{2})/2$, so $g'(\sqrt3)=0$ — **quadratic** convergence (this is Newton's
  method for $x^{2}-3$).

*Conclusion.* The reformulation decides both whether the iteration converges and how fast; $\lvert g'(r)\rvert$
is the discriminator, and $g'(r)=0$ gives the fastest rate.

### Solution 10

*Method.* The secant through $(1,-1)$ and $(2,2)$ has slope $(2-(-1))/(2-1)=3$, so
$$
x_2=2-\frac{2}{3}=\frac43=1.3333333333 .
$$
*Check.* $f(x_2)=16/9-2=-0.2222$, much closer to zero than $f(x_1)=2$; the method has halved the
distance to $\sqrt2$ in one step because the secant slope (3) approximates $f'(\sqrt2)=2.828$ well.

### Solution 11

*Answer.* Multiplicity $3$; linear convergence with rate $1-\tfrac13=\tfrac23$.

*Reason.* $f(x)=(x-2)^{3}(x+1)$ and $h(x)=x+1$ has $h(2)=3\ne0$, so $m=3$. By Proposition 8.5 the
Newton map has derivative $1-1/m=2/3$ at the root, so the error shrinks by a factor $2/3$ per step — about
$0.18$ decimal digits per step, against the doubling of digits at a simple root.

### Solution 12

*Method.* $f=(x-1)^{2}$, $f'=2(x-1)$, so
$$
x_{n+1}=x_n-\frac{(x_n-1)^{2}}{2(x_n-1)}=x_n-\frac{x_n-1}{2}=\frac{x_n+1}{2}.
$$
From $x_0=3$: $x_1=2$, $x_2=1.5$.

*Rate.* The errors are $2,1,0.5$: $\lvert e_{n+1}\rvert=\tfrac12\lvert e_n\rvert$ — linear with rate
$\tfrac12=1-1/m$ for $m=2$ ✓. Convergence is guaranteed but needs about $3.3$ steps per decimal digit.

### Solution 13

*The numbers.* At $x=1+10^{-9}$: $f(x)=1000\cdot10^{-9}=10^{-6}$, while the error is $10^{-9}$. The
residual is *small* in absolute terms and the error is smaller still — but only because $f'=1000$ is
large. The relation is
$$
f(x)\approx f'(1)(x-1)=1000(x-1),
$$
so $\lvert x-1\rvert\approx\lvert f(x)\rvert/1000$.

*The general rule.* A residual tolerance $\varepsilon$ certifies an error $\varepsilon/\inf\lvert f'\rvert$
only if a lower bound for $\lvert f'\rvert$ near the root is known. A sound test is therefore
$\lvert f(x_n)\rvert\le\varepsilon\,S$ with $S$ a known scale of $f$, or a relative step test
$\lvert x_n-x_{n-1}\rvert\le\delta\lvert x_n\rvert$, which needs no derivative bound.

## Intermediate

### Solution 14

*Steps.* $\log_2(1/10^{-4})=13.29$, so $n=14$ midpoints give an error at most $2^{-14}=6.1\times10^{-5}$
(and a bracket width $2^{-14}$).

*Computed result.* After 14 bisection steps the bracket is $[0.73907470703125,0.7391357421875]$ and the
midpoint is $x=0.739105224609375$. Its error is
$\lvert0.739105224609375-0.7390851332151607\rvert=2.01\times10^{-5}$, inside the bound
$6.1\times10^{-5}$ ✓.

*Comparison.* Fourteen evaluations of $f$ for five correct digits — Newton needs three for fifteen.

### Solution 15

*Iterates.* $g(x)=\sqrt{x+2}$, $x_0=1$, root $r=2$:

| $n$ | $x_n$ | $\lvert x_n-2\rvert$ | ratio |
|---|---|---|---|
| 1 | $1.7320508076$ | $2.679\times10^{-1}$ | — |
| 2 | $1.9318516526$ | $6.815\times10^{-2}$ | $0.254$ |
| 3 | $1.9828897227$ | $1.711\times10^{-2}$ | $0.251$ |
| 4 | $1.9957178465$ | $4.282\times10^{-3}$ | $0.250$ |
| 5 | $1.9989291750$ | $1.071\times10^{-3}$ | $0.250$ |

*Answer.* The ratios converge to $\lvert g'(2)\rvert=1/(2\sqrt4)=\tfrac14=0.25$, matching the contraction
constant $L=1/(2\sqrt3)=0.2887$ as an upper bound. With $L=0.2887$ and $\lvert x_0-2\rvert=1$, the a
priori bound after five steps is $L^{5}=2.0\times10^{-3}$, which holds but is seven times the truth.

### Solution 16

*Derivatives.* $g'(x)=2x/3$, so $g'(1)=\tfrac23<1$ (attracting) and $g'(2)=\tfrac43>1$ (repelling).

*Iterates from $1.1$:* $1.07$, $1.0483$, $1.033$, $1.0223$, $1.0151$ — decreasing to $1$, with ratios
about $\tfrac23$.

*Iterates from $1.9$:* $1.87$, $1.8323$, $1.7858$, $1.7297$, $1.6639$ — also decreasing, and also
converging to $1$, because the repelling fixed point at $2$ pushes every nearby point away from it and
the only other fixed point is the attracting one.

*Lesson.* A repelling fixed point is not a limit of the iteration from nearby starts; the contraction
condition is about the eigenvalue $g'(r)$, and it decides everything locally.

### Solution 17

*Iterates from $2.1$.*

| $n$ | $x_n$ | $\lvert x_n-r\rvert$ |
|---|---|---|
| 1 | $2.0945681211$ | $1.664\times10^{-5}$ |
| 2 | $2.0945514817$ | $1.6\times10^{-10}$ |
| 3 | $2.0945514815$ | $0$ |

*Comparison.* From $2.5$ the first step already overshoots to $2.164$ and four steps are needed for
$10^{-11}$; from $2.1$ two steps suffice. The step is quadratic, so a factor $50$ improvement in the
initial error becomes a factor $2500$ in the work.

*Practical note.* Both runs converge because both stay in the interval where $f$ is convex and the
tangent stays on one side; starting at $1$ would send the first iterate to a much worse point.

### Solution 18

*Iteration.* $f=x^{3}$, $f'=3x^{2}$, so
$$
x_{n+1}=x_n-\frac{x_n^{3}}{3x_n^{2}}=\tfrac23x_n .
$$
From $x_0=1$: $1,\ \tfrac23,\ \tfrac49,\ \tfrac{8}{27},\dots$ — the error is exactly $(2/3)^{n}$.

*Order and rate.* The ratio $\lvert e_{n+1}\rvert/\lvert e_n\rvert=\tfrac23$ is constant, so the order is
$1$ and the rate $\tfrac23$. This agrees with Proposition 8.5: $0$ is a root of multiplicity $3$ and
$1-1/3=\tfrac23$.

*Diagnosis.* A table in which the iterates approach the root geometrically, with constant ratio, means a
multiple root (or a nearly flat crossing) — not a bug in the code.

### Solution 19

*Iterates.*

| $n$ | $x_n$ | $\lvert x_n-r\rvert$ | $\lvert e_n\rvert/(\lvert e_{n-1}\rvert\lvert e_{n-2}\rvert)$ |
|---|---|---|---|
| 0 | $2$ | $9.455\times10^{-2}$ | — |
| 1 | $3$ | $9.055\times10^{-1}$ | — |
| 2 | $2.0588235294$ | $3.573\times10^{-2}$ | $0.417$ |
| 3 | $2.0812636598$ | $1.329\times10^{-2}$ | $0.411$ |
| 4 | $2.0948241461$ | $2.727\times10^{-4}$ | $0.574$ |
| 5 | $2.0945494310$ | $2.051\times10^{-6}$ | $0.566$ |

*Answer.* The quotients settle near $0.57$, so $e_{n+1}\approx0.57\,e_ne_{n-1}$, confirming the secant
error relation. The predicted constant is
$$
C=\frac{f''(r)}{2f'(r)}=\frac{6r}{2(3r^{2}-2)}=\frac{12.5673}{22.3229}=0.5630
$$
✓. The order constant $\lvert e_{n+1}\rvert/\lvert e_n\rvert^{\varphi}$ is still drifting
($1.20$, then $0.50$) because these iterates are not yet in the asymptotic regime; the product relation
is the more robust check at finite precision.

### Solution 20

*Iterates from $x_0=0$, $x_1=1$.*

| $n$ | $x_n$ | $\lvert x_n-r\rvert$ | $\lvert e_n\rvert/(\lvert e_{n-1}\rvert\lvert e_{n-2}\rvert)$ |
|---|---|---|---|
| 2 | $0.6850733573$ | $5.401\times10^{-2}$ | $0.280$ |
| 3 | $0.7362989976$ | $2.786\times10^{-3}$ | $0.198$ |
| 4 | $0.7391193619$ | $3.423\times10^{-5}$ | $0.228$ |
| 5 | $0.7390851121$ | $2.109\times10^{-8}$ | $0.221$ |

*Answer.* The errors fall by factors $19$ and $81$, and the quotients $e_n/(e_{n-1}e_{n-2})$ settle near
$0.22$ — the signature of order $\varphi=1.618$. Four steps from a crude start give eight correct digits,
against about twenty-six bisection steps.

*Remark.* The secant method needs one new evaluation per step, so this is eight digits for five
evaluations.

### Solution 21

*Modified iteration.* $x_{n+1}=x_n-2f(x_n)/f'(x_n)$ for $f=x^{3}-3x+2$, $f'=3x^{2}-3$.

| $n$ | modified Newton from $0.5$ | error | plain Newton from $0.5$ | error |
|---|---|---|---|---|
| 1 | $1.0555555556$ | $5.556\times10^{-2}$ | $0.7777777778$ | $2.222\times10^{-1}$ |
| 2 | $1.0005005005$ | $5.005\times10^{-4}$ | $0.8935185185$ | $1.065\times10^{-1}$ |
| 3 | $1.0000000417$ | $4.174\times10^{-8}$ | $0.9477572520$ | $5.224\times10^{-2}$ |
| 4 | $0.9999999992$ | $8.184\times10^{-10}$ | $0.9741121685$ | $2.589\times10^{-2}$ |

*Answer.* The modified iteration is quadratic (errors $5.6\times10^{-2}$, $5.0\times10^{-4}$,
$4.2\times10^{-8}$), the plain one linear with rate $\tfrac12$ (errors halving). The modified iteration
then stalls near $10^{-9}$: the residual is quadratic in the error at a double root, so double precision
cannot resolve the location better than about $\sqrt u$ (Section 7.7).

### Solution 22

*Newton from $3.2$.* $p'=3x^{2}-12x+11$:

| $n$ | $x_n$ | $p(x_n)$ |
|---|---|---|
| 1 | $3.0409638554$ | $0.08703$ |
| 2 | $3.0022976499$ | $0.004611$ |
| 3 | $3.0000078766$ | $1.575\times10^{-5}$ |
| 4 | $3.0000000001$ | $2.0\times10^{-10}$ |

*Deflation.* Synthetic division by $(x-3)$: coefficients $1$, $-6+3=-3$, $11+3(-3)=2$, remainder
$-6+3\cdot2=0$. So $q(x)=x^{2}-3x+2=(x-1)(x-2)$.

*Answer.* The roots are $3$, $2$, $1$; the deflation is exact here because the division has no rounding
(the root $3$ was computed to full precision) and the remaining roots are simple and separated.

*Check.* $p(1)=1-6+11-6=0$, $p(2)=8-24+22-6=0$ ✓.

### Solution 23

| $n$ | $x_n$ | $\lvert x_n-r\rvert$ | $\lvert x_n-x_{n-1}\rvert$ |
|---|---|---|---|
| 1 | $1.4166666667$ | $2.453\times10^{-3}$ | $8.333\times10^{-2}$ |
| 2 | $1.4142156863$ | $2.124\times10^{-6}$ | $2.451\times10^{-3}$ |
| 3 | $1.4142135624$ | $1.595\times10^{-12}$ | $2.124\times10^{-6}$ |
| 4 | $1.4142135624$ | $0$ | $1.595\times10^{-12}$ |

*Observation.* The step $\lvert x_n-x_{n-1}\rvert$ equals the previous error almost exactly, and the new
error is about $C$ times the square of the step. So the step is a reliable estimate of the error *before*
the step, and a very conservative one *after* it.

*Consequence for stopping.* Testing $\lvert x_n-x_{n-1}\rvert\le\delta$ guarantees an error of about
$\delta$ (slightly less), which is the reason this is the standard Newton criterion. It fails near a
multiple root, where the step and the error are proportional only up to $m$.

### Solution 24

*Derivative.* Implicit differentiation of $r^{2}-2+\varepsilon=0$:
$$
2r\frac{dr}{d\varepsilon}+1=0\quad\Longrightarrow\quad\frac{dr}{d\varepsilon}=-\frac{1}{2r}=-\frac{1}{2\sqrt2}=-0.353553 .
$$
At $\varepsilon=0$ the change is therefore $\Delta r\approx-0.353553\cdot10^{-10}=-3.536\times10^{-11}$.

*Check.* $\sqrt{2-10^{-10}}-\sqrt2=-3.53555\times10^{-11}$ ✓, a relative change of $2.5\times10^{-11}$,
i.e. about $10^{5}$ times the unit roundoff times the condition factor.

*Interpretation.* By Proposition 8.8 the root is well conditioned here because $f'(r)=2\sqrt2$ is not
small; the amplification is $1/(2\sqrt2)=0.354<1$. A flat crossing ($f'(r)\to0$) is what makes a root
sensitive.

## Advanced

### Solution 25

*Statement.* Let $g:[a,b]\to[a,b]$ be continuous with $\lvert g(x)-g(y)\rvert\le L\lvert x-y\rvert$,
$0\le L<1$. Then there is exactly one fixed point $r$, and $x_{n+1}=g(x_n)$ converges to it from any
$x_0\in[a,b]$ with the three estimates of Proposition 8.3.

*Existence.* $h(x)=g(x)-x$ is continuous, $h(a)=g(a)-a\ge0$ and $h(b)=g(b)-b\le0$; the intermediate value
theorem gives $h(r)=0$.

*Uniqueness.* If $r\ne s$ are fixed points, $\lvert r-s\rvert=\lvert g(r)-g(s)\rvert\le L\lvert r-s\rvert<\lvert r-s\rvert$,
a contradiction.

*Convergence.* The interval is invariant, so the iterates are defined; and
$\lvert x_{n+1}-r\rvert=\lvert g(x_n)-g(r)\rvert\le L\lvert x_n-r\rvert\le L^{n+1}\lvert x_0-r\rvert\to0$.

*A priori bound.* From $\lvert x_0-r\rvert\le\lvert x_0-x_1\rvert+\lvert x_1-r\rvert\le\lvert x_0-x_1\rvert+L\lvert x_0-r\rvert$,
$$
\lvert x_0-r\rvert\le\frac{\lvert x_1-x_0\rvert}{1-L}\quad\Longrightarrow\quad\lvert x_n-r\rvert\le\frac{L^{n}}{1-L}\lvert x_1-x_0\rvert .
$$

*A posteriori bound.* $\lvert x_n-r\rvert\le L\lvert x_{n-1}-r\rvert\le L\lvert x_{n-1}-x_n\rvert+L\lvert x_n-r\rvert$,
so $\lvert x_n-r\rvert\le\frac{L}{1-L}\lvert x_n-x_{n-1}\rvert$. $\blacksquare$

*Remark.* The proof uses only completeness of $\mathbb{R}$ through the intermediate value theorem; the
same argument in a complete metric space is the Banach fixed point theorem.

### Solution 26

*Hypotheses.* $f\in C^{2}$ on an interval containing $r$, $f(r)=0$, $f'(r)\ne0$.

*Step 1: $f'$ is bounded away from zero near $r$.* By continuity choose $\delta_0>0$ with
$\lvert f'(x)\rvert\ge m_1>0$ on $(r-\delta_0,r+\delta_0)$.

*Step 2: the error identity.* Taylor with Lagrange remainder at $x_n$:
$$
0=f(r)=f(x_n)+f'(x_n)(r-x_n)+\tfrac12f''(\xi_n)(r-x_n)^{2}.
$$
Hence $f'(x_n)(x_n-r)-f(x_n)=\tfrac12f''(\xi_n)(x_n-r)^{2}$, and dividing by $f'(x_n)$,
$$
x_{n+1}-r=x_n-r-\frac{f(x_n)}{f'(x_n)}=\frac{f''(\xi_n)}{2f'(x_n)}(x_n-r)^{2}.
$$

*Step 3: the quadratic bound.* With $M=\sup\lvert f''\rvert$ over the interval,
$\lvert x_{n+1}-r\rvert\le C\lvert x_n-r\rvert^{2}$ with $C=M/(2m_1)$.

*Step 4: the iterates stay close.* Choose $\delta\le\delta_0$ with $C\delta<1$. If $\lvert x_n-r\rvert\le\delta$
then $\lvert x_{n+1}-r\rvert\le C\delta^{2}<\delta$, and by induction
$\lvert x_n-r\rvert\le\delta(C\delta)^{n-1}\to0$. $\blacksquare$

*Sharpness remark.* The constant is asymptotically $\lvert f''(r)\rvert/(2\lvert f'(r)\rvert)$, and it is
attained: for $f=x^{2}-2$, $C=1/(2\sqrt2)=0.3536$, matching the ratios of Example 9.3.

### Solution 27

*Error relation.* By the divided-difference form of the interpolation error, there are points
$\xi_n$ between $x_{n-1}$ and $x_n$ and $\eta_n$ in the interval spanned by the iterates and $r$ with
$$
e_{n+1}=\frac{f''(\xi_n)}{2f'(\eta_n)}\,e_ne_{n-1}.
$$
(Equivalently: the secant method is Newton's method with $f'(x_n)$ replaced by
$f[x_{n-1},x_n]=f'(\eta_n)$, and $f'(\eta_n)-f'(x_n)=f''(\xi_n)(\eta_n-x_n)$ produces the product term.)

*Order.* Suppose $\lvert e_{n+1}\rvert=A\lvert e_n\rvert^{p}$ and $\lvert e_n\rvert=A\lvert e_{n-1}\rvert^{p}$;
then $\lvert e_{n-1}\rvert=(e_n/A)^{1/p}$ and the relation becomes
$$
A\lvert e_n\rvert^{p}=C\lvert e_n\rvert^{1+1/p}\quad\Longrightarrow\quad p=1+\frac1p .
$$
The positive root of $p^{2}-p-1=0$ is $\varphi=(1+\sqrt5)/2=1.618034$. Consistency of the constants gives
$A^{p}=C$, hence $A=C^{1/p}=C^{\varphi-1}=C^{0.618}$ and
$\lvert e_{n+1}\rvert=C^{1-1/\varphi}\lvert e_n\rvert^{\varphi}$. $\blacksquare$

*Numerical confirmation.* Solution 19 gives $C\approx0.565$ and the observed order constant
$0.565^{0.382}=0.80$ ✓.

### Solution 28

*Linear rate.* Write $f=(x-r)^{m}h$ with $h(r)\ne0$. Then
$f'=m(x-r)^{m-1}h+(x-r)^{m}h'$, so
$$
\frac{f}{f'}=\frac{(x-r)h}{mh+(x-r)h'}=\frac{x-r}{m}\cdot\frac{1}{1+(x-r)h'/(mh)}=\frac{x-r}{m}\left(1+O(x-r)\right).
$$
Therefore
$$
\Phi(x)-r=(x-r)-\frac{f}{f'}=\left(1-\frac1m\right)(x-r)+O((x-r)^{2}),
$$
which is linear convergence with rate $\lvert1-1/m\rvert<1$; the $O((x-r)^{2})$ term is what a table shows
as a slowly drifting ratio.

*Modified iteration.* Let $\Psi(x)=x-mf(x)/f'(x)$. Using the expansion above,
$$
\Psi(x)-r=(x-r)-m\cdot\frac{x-r}{m}\left(1+O(x-r)\right)=O((x-r)^{2}),
$$
so $\Psi'(r)=0$ and the iteration is quadratic by the same argument as Theorem 7.2 applied to $\Psi$.
$\blacksquare$

*What if $m$ is unknown.* One estimates it from $m\approx\dfrac{u}{u-f/f'}$ evaluated near the root, or
from the observed ratio $\rho=e_{n+1}/e_n=1-1/m$, giving $m\approx1/(1-\rho)$.

### Solution 29

*Convergence when $\lvert g'(r)\rvert<1$.* Choose $L$ with $\lvert g'(r)\rvert<L<1$. By continuity of
$g'$, there is $\delta>0$ with $\lvert g'(x)\rvert\le L$ for $\lvert x-r\rvert\le\delta$. For such $x$,
the mean value theorem gives $\lvert g(x)-r\rvert=\lvert g(x)-g(r)\rvert\le L\lvert x-r\rvert\le\delta$,
so the interval is invariant and $g$ is a contraction there; Theorem 7.1 gives convergence with rate at
most $L$. Refining, the asymptotic rate is exactly $\lvert g'(r)\rvert$:
$$
\frac{\lvert x_{n+1}-r\rvert}{\lvert x_n-r\rvert}=\frac{\lvert g(x_n)-g(r)\rvert}{\lvert x_n-r\rvert}\longrightarrow\lvert g'(r)\rvert .
$$

*Divergence when $\lvert g'(r)\rvert>1$.* Choose $L$ with $1<L<\lvert g'(r)\rvert$; near $r$,
$\lvert g(x)-g(r)\rvert\ge L\lvert x-r\rvert$, so $\lvert x_{n+1}-r\rvert\ge L\lvert x_n-r\rvert$ and the
error grows geometrically — unless some iterate lands exactly on $r$, which for $x_0\ne r$ requires
$x_0$ to be a preimage of $r$ and is not generic. Hence the iteration diverges from every nearby start
not in that exceptional set. $\blacksquare$

*Example.* $g=2x-1$ has $g'(1)=2$: from $0$ the errors $2,4,8,\dots$ double. $g=(x+1)/2$ represents the
same fixed point with $g'=\tfrac12$ and converges.

### Solution 30

*Bound.* Proposition 8.1 gives $\lvert x_n-r\rvert\le(b-a)/2^{n+1}$.

*Attainment of the bound.* Fix $n$ and $\varepsilon>0$. Let $[a_n,b_n]$ be the interval that the method
would produce, and let $f$ be strictly increasing and continuous with its zero at $r=b_n-\varepsilon$
(just inside the right endpoint). Then $f(a)f(b)<0$, the bisection decisions are the same as for any
increasing function, and $\lvert x_n-r\rvert=(b_n-a_n)/2-\varepsilon=(b-a)/2^{n+1}-\varepsilon$. Letting
$\varepsilon\to0$ makes the error approach the bound.

*Conclusion.* The bound is the supremum of $\lvert x_n-r\rvert$ over continuous bracketed $f$; it cannot
be improved by any argument that uses only continuity. To do better one needs more information — a bound
on $\lvert f'\rvert$, for instance, converts the interval bound into a much tighter error bound by the
mean value theorem. $\blacksquare$

### Solution 31

*Babylonian iteration.* For $f=x^{2}-a$, $f'=2x$ and
$$
x_{n+1}=x_n-\frac{x_n^{2}-a}{2x_n}=\frac12\left(x_n+\frac{a}{x_n}\right).
$$

*Convergence for every $x_0>0$.* By AM–GM, $x_{n+1}\ge\sqrt a$ for all $n\ge1$. For $x_n\ge\sqrt a$,
$$
x_{n+1}-x_n=\frac{a-x_n^{2}}{2x_n}\le0,
$$
so from $n=1$ the sequence is decreasing and bounded below by $\sqrt a$; it converges, and the limit $L$
satisfies $L=\tfrac12(L+a/L)$, hence $L^{2}=a$ and $L=\sqrt a$.

*Order.* $f''/(2f')=2/(2\cdot2\sqrt a)=1/(2\sqrt a)$, so the convergence is quadratic with that constant;
equivalently $x_{n+1}-\sqrt a=\dfrac{(x_n-\sqrt a)^{2}}{2x_n}$. $\blacksquare$

### Solution 32

*Setup.* $f(a)<0<f(b)$, $f$ convex ($f''\ge0$) and increasing ($f'>0$) on $[a,b]$; $r$ is the unique
root.

*Step 1: the first iterate lands in $[r,b]$.* Convexity gives $f(x)\ge f(b)+f'(b)(x-b)$ for all $x$. The
tangent at $b$ crosses zero at $x_1=b-f(b)/f'(b)<b$, and at that point
$f(x_1)\ge f(b)+f'(b)(x_1-b)=0$. Since $f$ is increasing, $f(x_1)\ge0$ implies $x_1\ge r$. Hence
$x_1\in[r,b]\subseteq[a,b]$.

*Step 2: monotone decrease.* Suppose $x_n\in[r,b]$. Then $f(x_n)\ge0$ and $f'(x_n)>0$, so
$x_{n+1}=x_n-f(x_n)/f'(x_n)\le x_n$; the same convexity argument as in Step 1 applied at $x_n$ gives
$f(x_{n+1})\ge0$, hence $x_{n+1}\ge r$. By induction the sequence decreases and stays in $[r,b]$.

*Step 3: the limit is the root.* A decreasing sequence bounded below converges to some $L\ge r$; since
$f'\ge f'(r)>0$ is bounded away from zero on $[r,b]$ and $f$ is continuous, passing to the limit in
$x_{n+1}=x_n-f(x_n)/f'(x_n)$ gives $f(L)=0$, so $L=r$.

*Step 4: quadratic rate.* Theorem 7.2 applies, since $f'(r)>0$ and $f''$ is bounded on $[a,b]$.
$\blacksquare$

*Remark.* This is the reason Newton is safe for Kepler's equation and for convex one-dimensional
problems: the bracket is preserved and convergence is monotone from the end where $f>0$.

## Challenge

### Solution 33

*Cycle.* With $f(x)=x^{3}-2x+2$ and $f'(x)=3x^{2}-2$:
$$
x_1=0-\frac{2}{-2}=1,\qquad x_2=1-\frac{1}{1}=0,\qquad x_3=1,\ \dots
$$
so the orbit is $0,1,0,1,\dots$, a two-cycle.

*Why the theorem is not contradicted.* Theorem 7.2 is local: it asserts convergence only for $x_0$
inside an interval where $f'\ne0$ and the error is small enough that $C\lvert e_0\rvert<1$. The two-cycle
points lie at distance about $>1$ from the root $r=-1.769292\ldots$ ($f(r)=0$), far outside any such
neighbourhood. The map $\Phi$ is perfectly smooth there; the orbit simply never enters the basin of $r$.

*Extra.* The cycle is *superattracting* for $\Phi$: since $\Phi'(x)=f f''/(f')^{2}$,
$\Phi'(0)=0$ and $\Phi'(1)=6$, so the derivative of $\Phi^{2}$ at $0$ is
$\Phi'(1)\Phi'(0)=0$. A nearby start is drawn into the cycle, which is why the failure is so stable under
small perturbations of the data.

### Solution 34

*The symmetry equation.* $\Phi(x)=x-(1+x^{2})\arctan x$. Setting $\Phi(x)=-x$ gives
$2x=(1+x^{2})\arctan x$.

*Numerical boundary.* Solving $2x-(1+x^{2})\arctan x=0$ on $(0,2)$ gives
$x=1.3917452003$. For $\lvert x_0\rvert$ below this value the iterates converge to $0$; above it, the
orbit is repelled.

*Just past the boundary.* From $x_0=1.4$ the iterates are
$$
-1.4136186488,\ 1.4501293146,\ -1.5506259756,\ 1.8470540842,\ -2.8935623931,\ 8.7103258470,\ -103.2497737719,\ 16540.5638272386,
$$
with growing amplitude: the orbit crosses to the other side, where $\lvert\Phi'(x)\rvert$ exceeds $1$, and
the error multiplies by an increasing factor each time. Note $\Phi'(0)=0$, so $0$ is superattracting but
its basin is bounded.

*Lesson.* "Newton converges locally" is not a formality: the basin here is a bounded interval, and a start
$0.6\%$ outside it destroys the computation.

### Solution 35

*Formula.* For $p(x)=(x-1)(x-2)(x-3)=x^{3}-6x^{2}+11x-6$ and a perturbation $\Delta a_0=-10^{-10}$
(so $p$ becomes $p-10^{-10}$), the root moves by
$$
\Delta r\approx-\frac{\Delta a_0}{p'(r)}=\frac{10^{-10}}{p'(r)} .
$$
With $p'(1)=2$, $p'(2)=-1$, $p'(3)=2$:
$$
\Delta r_1=+5.0\times10^{-11},\qquad \Delta r_2=-1.0\times10^{-10},\qquad \Delta r_3=+5.0\times10^{-11}.
$$

*Numerical check.* The roots of $x^{3}-6x^{2}+11x-6-10^{-10}$ are
$3+5.0\times10^{-11}$, $2-1.0\times10^{-10}$, $1+5.0\times10^{-11}$ ✓.

*Why root $2$ is most sensitive.* It has the smallest $\lvert p'\rvert$: the graph crosses the axis most
flatly there. The sensitivity is $1/\lvert p'(r)\rvert$, exactly the conditioning of Proposition 8.8 —
not a property of any algorithm.

### Solution 36

*Bisection.* To reach $\lvert x_n-r\rvert\le10^{-12}$ from $b-a=1$ we need $2^{-(n+1)}\le10^{-12}$, i.e.
$n+1\ge39.86$, so $n=39$ evaluations of $f$.

*Newton from $2.5$.* Errors $4.05\times10^{-1}$, $6.96\times10^{-2}$, $2.58\times10^{-3}$,
$3.75\times10^{-6}$, $7.9\times10^{-12}$, $0$: five steps reach $10^{-12}$. Each step uses $f$ and $f'$,
counted separately: $10$ evaluations.

*Secant from $2,3$.* Errors $3.57\times10^{-2}$, $1.33\times10^{-2}$, $2.73\times10^{-4}$,
$2.05\times10^{-6}$, $3.15\times10^{-10}$, $4.4\times10^{-16}$: five new points after the two starting
values give $3.15\times10^{-10}$, so $7$ evaluations (two initial, five new) reach $10^{-12}$.

*Answer.* Secant $7$, Newton $10$, bisection $39$. The secant method wins because it needs no derivative
and gains $1.618$ digits per evaluation; Newton's advantage in *steps* is offset by its factor-two cost
per step. Bisection loses by a factor of five in evaluations but is the only one of the three that is
guaranteed to converge.
