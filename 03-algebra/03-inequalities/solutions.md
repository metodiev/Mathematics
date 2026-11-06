# Inequalities — Solutions

> [Tutorial](README.md) · [Exercises](exercises.md) · 36 worked solutions

Each solution states the strategy, carries out every significant step, and checks the result at a
boundary point or with a test value. Boundary points are checked explicitly because that is where
interval notation is most often wrong.

## Beginner

**1.**

The condition is $-3\le x<5$. The left endpoint $-3$ is included because the inequality is
non-strict; the right endpoint $5$ is excluded because the inequality is strict. Therefore the set
is
$$\boxed{[-3,5)}.$$

**2.**

The interval $(-\infty,2]$ contains exactly the real numbers less than or equal to $2$, so
$$\boxed{x\le 2}.$$
The square bracket at $2$ is what makes the inequality non-strict.

**3.**

$$\begin{aligned}
4x+7 &< 23\\
4x &< 16 && \text{subtract }7\\
x &< 4 && \text{divide by }4>0.
\end{aligned}$$
The solution is $\boxed{(-\infty,4)}$. Check: $x=0$ gives $7<23$, true; $x=4$ gives $23<23$,
false, so $4$ is correctly excluded.

**4.**

$$\begin{aligned}
5-3x &\ge -7\\
-3x &\ge -12 && \text{subtract }5\\
x &\le 4 && \text{divide by }-3<0\text{; reverse}.
\end{aligned}$$
The solution is $\boxed{(-\infty,4]}$. Check: $x=4$ gives $5-12=-7\ge -7$, true with equality;
$x=5$ gives $-10\ge -7$, false.

**5.**

$$\begin{aligned}
\frac{x}{4}+2 &\le 5\\
\frac{x}{4} &\le 3 && \text{subtract }2\\
x &\le 12 && \text{multiply by }4>0.
\end{aligned}$$
The solution is $\boxed{(-\infty,12]}$. Check: $x=12$ gives $3+2=5\le 5$, true.

**6.**

$$\begin{aligned}
-2(x-3) &> 8\\
-2x+6 &> 8 && \text{distribute}\\
-2x &> 2 && \text{subtract }6\\
x &< -1 && \text{divide by }-2<0\text{; reverse}.
\end{aligned}$$
The solution is $\boxed{(-\infty,-1)}$. Check: $x=-2$ gives $-2(-5)=10>8$, true; $x=0$ gives
$6>8$, false.

**7.**

Subtract $5$ from all three parts:
$$2-5\le x\le 9-5,$$
so
$$-3\le x\le 4.$$
The solution is $\boxed{[-3,4]}$. Both endpoints are included because both inequalities are
non-strict. Check: $x=-3$ gives $2\le 2\le 9$, true; $x=4$ gives $2\le 9\le 9$, true.

**8.**

$$\begin{aligned}
-1 &< 3x-4\le 5\\
3 &< 3x\le 9 && \text{add }4\text{ to all parts}\\
1 &< x\le 3 && \text{divide all parts by }3>0.
\end{aligned}$$
The solution is $\boxed{(1,3]}$. Check: $x=1$ gives $-1< -1$, false, so $1$ is excluded; $x=3$
gives $-1<5\le 5$, true, so $3$ is included.

**9.**

The inequality $|x|\le 7$ says that the distance from $x$ to $0$ is at most $7$. By Theorem 7.7 it
is equivalent to
$$-7\le x\le 7,$$
so the solution is $\boxed{[-7,7]}$.

**10.**

By Theorem 7.7,
$$|x-3|<2 \iff -2<x-3<2.$$
Adding $3$ to all parts gives
$$1<x<5.$$
The solution is $\boxed{(1,5)}$. Check: $x=1$ gives $|{-2}|=2<2$, false, so $1$ is excluded; $x=3$
gives $0<2$, true.

**11.**

By Theorem 7.8,
$$|x+1|\ge 4 \iff x+1\le -4 \ \text{or}\ x+1\ge 4.$$
The first gives $x\le -5$; the second gives $x\ge 3$. Therefore
$$\boxed{(-\infty,-5]\cup[3,\infty)}.$$
Check: $x=-5$ gives $|{-4}|=4\ge 4$, true; $x=0$ gives $1\ge 4$, false.

**12.**

Solve each inequality separately.

First:
$$3x-2<7 \iff 3x<9 \iff x<3.$$
Second:
$$x+1\ge 0 \iff x\ge -1.$$
The system requires both, so the solution is the intersection
$$(-\infty,3)\cap[-1,\infty)=[-1,3).$$
$$\boxed{[-1,3)}$$
Check: $x=-1$ satisfies both ($-5<7$ and $0\ge 0$), so it is included; $x=3$ makes the first
inequality $7<7$, false, so it is excluded.

## Intermediate

**13.**

Expand the left side first:
$$3(2x-1)-4(x+2)=6x-3-4x-8=2x-11.$$
Thus
$$\begin{aligned}
2x-11 &\le 5x+6\\
-3x &\le 17 && \text{subtract }5x\text{ and add }11\\
x &\ge -\frac{17}{3} && \text{divide by }-3<0\text{; reverse}.
\end{aligned}$$
The solution is $\boxed{\left[-\frac{17}{3},\infty\right)}$.

Check at $x=-5$: the left side is $3(-11)-4(-3)=-33+12=-21$; the right side is $-25+6=-19$; and
$-21\le -19$ is true. At $x=-6$: the left side is $3(-13)-4(-4)=-39+16=-23$; the right side is
$-30+6=-24$; and $-23\le -24$ is false. Since $-6<-17/3\approx-5.667$, consistent.

**14.**

Multiply by the positive common denominator $6$:
$$\begin{aligned}
6\left(\frac{2x-1}{3}\right)-6\left(\frac{x+2}{2}\right) &> 6\\
2(2x-1)-3(x+2) &> 6\\
4x-2-3x-6 &> 6\\
x-8 &> 6\\
x &> 14.
\end{aligned}$$
The solution is $\boxed{(14,\infty)}$. Check: $x=15$ gives
$$\frac{29}{3}-\frac{17}{2}=\frac{58-51}{6}=\frac{7}{6}>1,$$
true. At $x=14$ the left side is $9-8=1$, not greater than $1$, so $14$ is excluded.

**15.**

$$\begin{aligned}
-4 &\le \frac{2-5x}{3}<6\\
-12 &\le 2-5x<18 && \text{multiply all parts by }3>0\\
-14 &\le -5x<16 && \text{subtract }2\\
\frac{14}{5} &\ge x>-\frac{16}{5} && \text{divide by }-5<0\text{; reverse both signs}.
\end{aligned}$$
Read from right to left:
$$-\frac{16}{5}<x\le\frac{14}{5}.$$
The solution is $\boxed{\left(-\frac{16}{5},\frac{14}{5}\right]}$.

Check: $x=0$ gives $-4\le \frac23<6$, true. At $x=\frac{14}{5}=2.8$, the middle expression is
$\frac{2-14}{3}=-4$, and the left inequality is an equality, so $2.8$ is included. At
$x=-\frac{16}{5}=-3.2$, the middle expression is $\frac{2+16}{3}=6$, and the right inequality is
strict, so $-3.2$ is excluded.

**16.**

By Theorem 7.7,
$$-9\le 4x+1\le 9.$$
Subtract $1$:
$$-10\le 4x\le 8.$$
Divide by $4>0$:
$$-\frac{5}{2}\le x\le 2.$$
The solution is $\boxed{\left[-\frac{5}{2},2\right]}$. Check: $x=2$ gives $|9|=9\le 9$, true;
$x=-3$ gives $|{-11}|=11\le 9$, false; $x=0$ gives $|1|=1\le 9$, true.

**17.**

By Theorem 7.8, $|5-2x|>1$ is equivalent to
$$5-2x>1 \quad\text{or}\quad 5-2x<-1.$$
First:
$$5-2x>1 \iff -2x>-4 \iff x<2.$$
Second:
$$5-2x<-1 \iff -2x<-6 \iff x>3.$$
Therefore the solution is
$$\boxed{(-\infty,2)\cup(3,\infty)}.$$
Check: $x=0$ gives $5>1$, true; $x=2$ gives $1>1$, false; $x=2.5$ gives $0>1$, false; $x=3$
gives $1>1$, false; $x=4$ gives $3>1$, true.

**18.**

Isolate the absolute value:
$$\begin{aligned}
2|x+3|-5 &< 3\\
2|x+3| &< 8 && \text{add }5\\
|x+3| &< 4 && \text{divide by }2>0.
\end{aligned}$$
By Theorem 7.7,
$$-4<x+3<4,$$
and subtracting $3$ gives
$$-7<x<1.$$
The solution is $\boxed{(-7,1)}$. Check: $x=0$ gives $2(3)-5=1<3$, true; $x=1$ gives
$2(4)-5=3<3$, false, so $1$ is excluded.

**19.**

Factor:
$$x^2-5x+6=(x-2)(x-3).$$
The roots are $2$ and $3$. The sign chart is:

| Interval | $x-2$ | $x-3$ | Product |
|---|---|---|---|
| $x<2$ | $-$ | $-$ | $+$ |
| $2<x<3$ | $+$ | $-$ | $-$ |
| $x>3$ | $+$ | $+$ | $+$ |

The product is negative between the roots and zero at the roots. Because the inequality is
non-strict, both roots are included:
$$\boxed{[2,3]}.$$
Check: $x=2.5$ gives $6.25-12.5+6=-0.25\le 0$, true; $x=1$ gives $2>0$, false.

**20.**

Factor:
$$x^2+2x-8=(x+4)(x-2).$$
The roots are $-4$ and $2$. The sign chart is:

| Interval | $x+4$ | $x-2$ | Product |
|---|---|---|---|
| $x<-4$ | $-$ | $-$ | $+$ |
| $-4<x<2$ | $+$ | $-$ | $-$ |
| $x>2$ | $+$ | $+$ | $+$ |

The product is positive outside the roots. The inequality is strict, so the roots are excluded:
$$\boxed{(-\infty,-4)\cup(2,\infty)}.$$
Check: $x=-5$ gives $25-10-8=7>0$, true; $x=0$ gives $-8>0$, false; $x=3$ gives $9+6-8=7>0$,
true.

**21.**

The numerator is zero at $x=3$; the denominator is zero at $x=-2$, where the expression is
undefined. The sign chart is:

| Interval | $x-3$ | $x+2$ | Quotient |
|---|---|---|---|
| $x<-2$ | $-$ | $-$ | $+$ |
| $-2<x<3$ | $-$ | $+$ | $-$ |
| $x>3$ | $+$ | $+$ | $+$ |

The quotient is nonnegative on $(-\infty,-2)$ and on $[3,\infty)$. The point $3$ is included
because the quotient equals zero there; $-2$ is never included. Hence
$$\boxed{(-\infty,-2)\cup[3,\infty)}.$$
Check: $x=0$ gives $\frac{-3}{2}<0$, false; $x=4$ gives $\frac16\ge 0$, true; $x=-3$ gives
$\frac{-6}{-1}=6\ge 0$, true; $x=-2$ is undefined.

**22.**

First inequality:
$$3x-1<8 \iff 3x<9 \iff x<3.$$
Second inequality:
$$2x+5\ge 1 \iff 2x\ge -4 \iff x\ge -2.$$
The system is the intersection
$$(-\infty,3)\cap[-2,\infty)=[-2,3).$$
$$\boxed{[-2,3)}$$
Check: $x=-2$ gives $-7<8$ and $1\ge 1$, both true; $x=3$ gives $8<8$, false.

**23.**

The condition $|L-75|\le 0.05$ is equivalent to
$$-0.05\le L-75\le 0.05.$$
Adding $75$ to all parts gives
$$74.95\le L\le 75.05.$$
The acceptable interval is $\boxed{[74.95,75.05]}$ millimetres. Check: $L=74.95$ gives
$|{-0.05}|=0.05\le 0.05$, true; $L=75.06$ gives $0.06\le 0.05$, false.

**24.**

The cost inequality is
$$3+2d\le 25,$$
and the travel requirement is $d\ge 4$. Solving the cost inequality:
$$2d\le 22 \iff d\le 11.$$
The system is therefore
$$4\le d\le 11,$$
so the possible distances are $\boxed{[4,11]}$ kilometres. Check: $d=4$ costs $3+8=11\le 25$;
$d=11$ costs $3+22=25\le 25$. A distance of $12$ km would cost $\$27$, which exceeds the budget.

## Advanced

**25.**

The domain excludes $x=-4$. Subtract $1$ from both sides so that the right side becomes zero:
$$\begin{aligned}
\frac{x-1}{x+4}-1 &\le 0\\
\frac{x-1-(x+4)}{x+4} &\le 0\\
\frac{-5}{x+4} &\le 0.
\end{aligned}$$
The numerator is the negative constant $-5$. A fraction with negative numerator is at most zero
exactly when its denominator is positive:
$$x+4>0 \iff x>-4.$$
The solution is $\boxed{(-4,\infty)}$. The endpoint $-4$ is excluded because the original expression
is undefined there.

Check: $x=-5$ gives $\frac{-6}{-1}=6\le 1$, false; $x=0$ gives $-\frac14\le 1$, true. At $x=-3.9$
the fraction is $\frac{-4.9}{0.1}=-49\le 1$, true, consistent with the interval starting just to the
right of $-4$.

**26.**

Move all terms to the left:
$$x^2-2x-3\ge 0.$$
Factor:
$$(x-3)(x+1)\ge 0.$$
The roots are $3$ and $-1$. The sign chart is:

| Interval | $x-3$ | $x+1$ | Product |
|---|---|---|---|
| $x<-1$ | $-$ | $-$ | $+$ |
| $-1<x<3$ | $-$ | $+$ | $-$ |
| $x>3$ | $+$ | $+$ | $+$ |

The product is nonnegative outside the roots, and the inequality is non-strict, so both roots are
included:
$$\boxed{(-\infty,-1]\cup[3,\infty)}.$$
Check: $x=-1$ gives $1+2-3=0\ge 0$, true; $x=0$ gives $-3\ge 0$, false; $x=4$ gives
$16-8-3=5\ge 0$, true.

**27.**

Both sides are nonnegative, so squaring preserves the inequality:
$$(x-1)^2<(2x+1)^2.$$
Expand:
$$x^2-2x+1<4x^2+4x+1.$$
Subtract the left side from both sides:
$$0<3x^2+6x,$$
that is,
$$3x(x+2)>0.$$
The roots are $0$ and $-2$. A product of two linear factors with positive leading coefficient is
positive outside its roots, so
$$x<-2 \quad\text{or}\quad x>0.$$
The solution is $\boxed{(-\infty,-2)\cup(0,\infty)}$.

Check: $x=-3$: $|{-4}|=4<|{-5}|=5$, true. $x=-1$: $|{-2}|=2<|{-1}|=1$, false. $x=0$:
$|{-1}|=1<|1|=1$, false, so $0$ is excluded. $x=1$: $0<3$, true.

**Alternative.** The difference of squares factors:
$$(2x+1)^2-(x-1)^2=\bigl((2x+1)-(x-1)\bigr)\bigl((2x+1)+(x-1)\bigr)=(x+2)(3x).$$
The inequality $(x-1)^2<(2x+1)^2$ is equivalent to this difference being positive, which gives the
same factorization $3x(x+2)>0$.

**28.**

The domain excludes $x=2$ and $x=-3$. Subtract the right side:
$$\frac{1}{x-2}-\frac{1}{x+3}\ge 0.$$
Combine over the common denominator:
$$\frac{(x+3)-(x-2)}{(x-2)(x+3)}=\frac{5}{(x-2)(x+3)}\ge 0.$$
The numerator is the positive constant $5$, so the fraction is nonnegative exactly when the
denominator is positive:
$$(x-2)(x+3)>0.$$
This product is positive outside its roots $-3$ and $2$, so
$$\boxed{(-\infty,-3)\cup(2,\infty)}.$$
The endpoints are excluded because the original expressions are undefined there.

Check: $x=-4$ gives $-\frac16\ge -1$, true; $x=0$ gives $-\frac12\ge \frac13$, false; $x=3$ gives
$1\ge \frac16$, true.

**29.**

The square of a real number is nonnegative, and $(x-2)^2=0$ exactly when $x-2=0$. Therefore
$(x-2)^2>0$ holds for every real $x$ except $x=2$:
$$\boxed{(-\infty,2)\cup(2,\infty)}.$$
Check: $x=0$ gives $4>0$, true; $x=2$ gives $0>0$, false; $x=3$ gives $1>0$, true.

A common error is to take a square root and write $x-2>0$, which would lose all solutions with
$x<2$. Squaring is not one-to-one, so it cannot be undone without a sign condition.

**30.**

Factor the numerator:
$$\frac{(x-2)(x+2)}{x-1}\ge 0.$$
The critical values are $-2$, $1$ and $2$. The denominator zero $x=1$ is excluded. The sign chart is:

| Interval | $x-2$ | $x+2$ | $x-1$ | Quotient |
|---|---|---|---|---|
| $x<-2$ | $-$ | $-$ | $-$ | $-$ |
| $-2<x<1$ | $-$ | $+$ | $-$ | $+$ |
| $1<x<2$ | $-$ | $+$ | $+$ | $-$ |
| $x>2$ | $+$ | $+$ | $+$ | $+$ |

The quotient is nonnegative on $(-\infty,-2]$ and on $[2,\infty)$, but $x=1$ must be removed from
the middle positive interval. Therefore
$$\boxed{[-2,1)\cup[2,\infty)}.$$
Check: $x=-2$ gives $0\ge 0$, true; $x=0$ gives $\frac{-4}{-1}=4\ge 0$, true; $x=1.5$ gives
$\frac{2.25-4}{0.5}=-3.5\ge 0$, false; $x=2$ gives $0\ge 0$, true.

**31.**

Assume $0<a<b$.

**First claim: $a^2<b^2$.** By Theorem 7.1, $a<b$ gives $b-a>0$. Since $a>0$ and $b>0$, their sum
$b+a$ is positive (add $0<a$ and $0<b$ using (O3)). The difference of squares factors as
$$b^2-a^2=(b-a)(b+a).$$
Both factors are positive, so their product is positive by Theorem 7.5. Hence $b^2-a^2>0$, which by
Theorem 7.1 gives $a^2<b^2$.

**Second claim: $\dfrac1a>\dfrac1b$.** Since $a>0$ and $b>0$, the product $ab$ is positive, so by
Theorem 7.4 its reciprocal $1/(ab)$ is positive. Multiply the inequality $a<b$ by the positive
number $1/(ab)$; by axiom (O4) the direction is preserved:
$$\frac{a}{ab}<\frac{b}{ab}.$$
Simplifying gives
$$\frac1b<\frac1a,$$
which is the same as $\frac1a>\frac1b$.

**Alternative for the second claim.** Compute
$$\frac1a-\frac1b=\frac{b-a}{ab}.$$
The numerator $b-a$ is positive and the denominator $ab$ is positive, so the difference is positive,
again giving $1/a>1/b$. This uses the sign rule for quotients rather than multiplying an
inequality, and is often less error-prone.

Both claims are proved. $\square$

## Challenge

**32.**

The absolute values change behaviour at $x=-1$ and $x=3$, so split the line into three cases.

**Case 1: $x<-1$.** Then $x-3<0$ and $x+1<0$, so
$$|x-3|+|x+1|=(3-x)+(-x-1)=2-2x.$$
The inequality becomes
$$2-2x<6 \iff -2x<4 \iff x>-2.$$
Intersecting with $x<-1$ gives
$$-2<x<-1.$$

**Case 2: $-1\le x<3$.** Then $x-3\le 0$ and $x+1\ge 0$, so
$$|x-3|+|x+1|=(3-x)+(x+1)=4.$$
The inequality $4<6$ is true for every $x$ in this interval, so the whole interval
$[-1,3)$ is part of the solution.

**Case 3: $x\ge 3$.** Then both expressions are nonnegative, so
$$|x-3|+|x+1|=(x-3)+(x+1)=2x-2.$$
The inequality becomes
$$2x-2<6 \iff 2x<8 \iff x<4.$$
Intersecting with $x\ge 3$ gives
$$3\le x<4.$$

Taking the union of the three pieces:
$$(-2,-1)\cup[-1,3)\cup[3,4)=(-2,4).$$
$$\boxed{(-2,4)}$$
Check: $x=0$ gives $3+1=4<6$, true; $x=-2$ gives $5+1=6<6$, false; $x=4$ gives $1+5=6<6$,
false. The endpoints are correctly excluded.

**Geometric reading.** The sum $|x-3|+|x+1|$ is the sum of the distances from $x$ to $3$ and to
$-1$. The distance between the two fixed points is $4$, so every point between them has sum $4$.
Moving a distance $d$ outside the interval $[-1,3]$ adds $2d$ to the sum; the sum is less than $6$
exactly when $d<1$, giving $(-2,4)$.

**33.**

The domain excludes $x=1$ and $x=2$. Move all terms to the left:
$$\frac{1}{x-1}+\frac{1}{x-2}-1\ge 0.$$
Combine over the common denominator $(x-1)(x-2)$:
$$\begin{aligned}
\frac{(x-2)+(x-1)-(x-1)(x-2)}{(x-1)(x-2)} &\ge 0\\
\frac{2x-3-(x^2-3x+2)}{(x-1)(x-2)} &\ge 0\\
\frac{-x^2+5x-5}{(x-1)(x-2)} &\ge 0.
\end{aligned}$$
The numerator is zero when
$$x^2-5x+5=0 \iff x=\frac{5\pm\sqrt{25-20}}{2}=\frac{5\pm\sqrt5}{2}.$$
Write
$$\alpha=\frac{5-\sqrt5}{2}\approx1.382,\qquad \beta=\frac{5+\sqrt5}{2}\approx3.618.$$
The numerator $-x^2+5x-5$ is a downward-opening parabola, so it is positive between its roots and
negative outside them. The denominator is positive on $(-\infty,1)\cup(2,\infty)$ and negative on
$(1,2)$. The sign chart is:

| Interval | Numerator | Denominator | Quotient |
|---|---|---|---|
| $(-\infty,1)$ | $-$ | $+$ | $-$ |
| $(1,\alpha)$ | $-$ | $-$ | $+$ |
| $(\alpha,2)$ | $+$ | $-$ | $-$ |
| $(2,\beta)$ | $+$ | $+$ | $+$ |
| $(\beta,\infty)$ | $-$ | $+$ | $-$ |

The quotient is nonnegative on $(1,\alpha]$ and on $(2,\beta]$. The roots $\alpha,\beta$ are
included because the quotient equals zero there; $1$ and $2$ are excluded because the original
expression is undefined. Therefore
$$\boxed{\left(1,\frac{5-\sqrt5}{2}\right]\cup\left(2,\frac{5+\sqrt5}{2}\right]}.$$

Check with test points. $x=1.2$: $\frac{1}{0.2}+\frac{1}{-0.8}=5-1.25=3.75\ge 1$, true.
$x=1.5$: $2+\frac{1}{-0.5}=0\ge 1$, false. $x=3$: $\frac12+1=1.5\ge 1$, true. $x=4$:
$\frac13+\frac12=\frac56<1$, false. These agree with the sign chart.

**34.**

The inequality $|x^2-4|<3$ is equivalent to
$$-3<x^2-4<3.$$
Add $4$ to all parts:
$$1<x^2<7.$$
This is the conjunction $x^2>1$ and $x^2<7$.

* $x^2>1$ means $|x|>1$, so $x<-1$ or $x>1$.
* $x^2<7$ means $|x|<\sqrt7$, so $-\sqrt7<x<\sqrt7$.

Intersecting the two sets gives
$$(-\sqrt7,-1)\cup(1,\sqrt7).$$
$$\boxed{(-\sqrt7,-1)\cup(1,\sqrt7)}$$
Check: $x=0$ gives $|{-4}|=4<3$, false; $x=2$ gives $|0|=0<3$, true; $x=-2$ gives $0<3$, true.
At $x=1$ and $x=-1$, $|x^2-4|=3$, so the strict inequality excludes them; at
$x=\pm\sqrt7$, $|x^2-4|=3$ as well, so those endpoints are also excluded.

**35.**

**Proof of the triangle inequality.** For every real $x$, the definition of absolute value gives
$$-|x|\le x\le |x|,$$
because if $x\ge 0$ then $-|x|=-x\le 0\le x=|x|$, and if $x<0$ then
$-|x|=x<0\le -x=|x|$. Similarly,
$$-|y|\le y\le |y|.$$
Adding the two chains (using (O3) twice) gives
$$-(|x|+|y|)\le x+y\le |x|+|y|.$$
By Theorem 7.7, with $a=|x|+|y|\ge 0$, the statement $-a\le x+y\le a$ is exactly
$$|x+y|\le |x|+|y|.$$
This proves the triangle inequality.

**Equality case.** Compare the squares:
$$\begin{aligned}
(|x|+|y|)^2 &= x^2+2|x||y|+y^2,\\
(x+y)^2 &= x^2+2xy+y^2.
\end{aligned}$$
The difference is
$$(|x|+|y|)^2-(x+y)^2=2\bigl(|xy|-xy\bigr).$$
Since $|xy|\ge xy$ for all real $x,y$, the difference is nonnegative, which gives another proof
that $|x+y|^2\le(|x|+|y|)^2$ and hence $|x+y|\le|x|+|y|$. Equality holds exactly when the
difference is zero, that is, when
$$|xy|=xy.$$
This happens exactly when $xy\ge 0$: the product is nonnegative. Therefore equality holds exactly
when $x$ and $y$ have the same sign, or at least one of them is zero. $\square$

For example, $x=2$, $y=3$ gives $|5|=5=2+3$; $x=2$, $y=-3$ gives $|{-1}|=1<5$, strict.

**36.**

The expressions inside the absolute values change sign at $1$, $2$ and $3$, so split the line into
four cases.

**Case 1: $x<1$.** All three quantities are negative, so
$$|x-1|+|x-2|+|x-3|=(1-x)+(2-x)+(3-x)=6-3x.$$
The inequality becomes
$$6-3x\le 4 \iff -3x\le -2 \iff x\ge \frac23.$$
Intersecting with $x<1$ gives
$$\frac23\le x<1.$$

**Case 2: $1\le x<2$.** Here $x-1\ge0$ while $x-2<0$ and $x-3<0$, so
$$(x-1)+(2-x)+(3-x)=4-x.$$
The inequality becomes
$$4-x\le 4 \iff x\ge 0,$$
which is true throughout $1\le x<2$. So this whole interval is in the solution.

**Case 3: $2\le x<3$.** Now $x-1\ge0$, $x-2\ge0$ and $x-3<0$, so
$$(x-1)+(x-2)+(3-x)=x.$$
The inequality becomes
$$x\le 4,$$
which is true throughout $2\le x<3$. So this whole interval is in the solution.

**Case 4: $x\ge3$.** All three quantities are nonnegative, so
$$(x-1)+(x-2)+(x-3)=3x-6.$$
The inequality becomes
$$3x-6\le4 \iff 3x\le10 \iff x\le\frac{10}{3}.$$
Intersecting with $x\ge3$ gives
$$3\le x\le\frac{10}{3}.$$

Taking the union:
$$\left[\frac23,1\right)\cup[1,2)\cup[2,3)\cup\left[3,\frac{10}{3}\right]
=\left[\frac23,\frac{10}{3}\right].$$
$$\boxed{\left[\frac23,\frac{10}{3}\right]}$$
Check: $x=\frac23$ gives $\frac13+\frac43+\frac73=4$, true with equality; $x=\frac{10}{3}$ gives
$\frac73+\frac43+\frac13=4$, true with equality; $x=0$ gives $1+2+3=6>4$, false; $x=4$ gives
$3+2+1=6>4$, false. Both endpoints are included because the inequality is non-strict.

