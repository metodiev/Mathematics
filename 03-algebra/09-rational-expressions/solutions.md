# Rational Expressions — Solutions

> [Tutorial](README.md) · [Exercises](exercises.md) · 36 worked solutions

Each solution states the domain first, shows every significant algebraic step, and ends with a check
by substitution. When a candidate is rejected, the reason is named: excluded by the domain, or
impossible for the physical model.

## Beginner

### Solution 1

The denominator is zero only when $x-7=0$, that is $x=7$. Hence

$$
\operatorname{dom}=\mathbb{R}\setminus\{7\}=\{x\in\mathbb{R}:x\ne7\}.
$$

### Solution 2

Factor the denominator: $x^2-9=(x-3)(x+3)$. It is zero at $x=3$ and $x=-3$, so

$$
\operatorname{dom}=\mathbb{R}\setminus\{-3,3\}.
$$

Check: at $x=0$ the expression is $\frac{2}{-9}$, defined; at $x=3$ it is $\frac{5}{0}$, undefined.

### Solution 3

For every real $x$, $x^2\ge0$, hence $x^2+4\ge4>0$. The denominator never vanishes, so
$\operatorname{dom}=\mathbb{R}$. The numerator $3x-1$ is irrelevant to the domain — only the
denominator matters.

### Solution 4

Factor the numbers and the powers of each variable:

$$
\frac{12x^3y}{18xy^4}=\frac{2\cdot6\cdot x\cdot x^2\cdot y}{3\cdot6\cdot x\cdot y\cdot y^3}
=\frac{2x^2}{3y^3}.
$$

The original denominators are $18xy^4$, which vanishes when $x=0$ or $y=0$. Therefore the domain is
$x\ne0$ and $y\ne0$, and the answer is $\frac{2x^2}{3y^3}$ with $x,y\ne0$.

Check at $x=y=1$: original $\frac{12}{18}=\frac23$; simplified $\frac{2}{3}$. Check at $x=2,y=1$:
original $\frac{96}{36}=\frac83$; simplified $\frac{8}{3}$.

### Solution 5

Factor the numerator as a difference of squares: $x^2-25=(x-5)(x+5)$. For $x\ne5$,

$$
\frac{x^2-25}{x-5}=\frac{(x-5)(x+5)}{x-5}=x+5 .
$$

The excluded value is $x=5$, because the original denominator vanishes there. At $x=5$ the simplified
expression equals $5+5=10$, but the original is $\frac{0}{0}$, which is undefined. The number $10$ is
the height of the hole, not a value of the function.

Check at $x=6$: original $\frac{36-25}{1}=11$; simplified $6+5=11$.

### Solution 6

Factor both parts: $x^2+7x+12=(x+3)(x+4)$ and $x^2-9=(x-3)(x+3)$. For $x\ne\pm3$,

$$
\frac{(x+3)(x+4)}{(x-3)(x+3)}=\frac{x+4}{x-3}.
$$

Domain: $x\ne3$ and $x\ne-3$ (both come from the original denominator $x^2-9$). Note that $x=-3$ is
cancelled but remains excluded; $x=3$ is a vertical asymptote, $x=-3$ is a hole.

Check at $x=0$: original $\frac{12}{-9}=-\frac43$; simplified $\frac{4}{-3}=-\frac43$.

### Solution 7

$$
\frac{3}{x}\cdot\frac{x^2}{9}=\frac{3x^2}{9x}=\frac{x}{3},
\qquad x\ne0 .
$$

Check at $x=6$: original $\frac36\cdot\frac{36}{9}=\frac12\cdot4=2$; simplified $\frac63=2$.

### Solution 8

Division is multiplication by the reciprocal:

$$
\frac{x}{4}\div\frac{x^2}{8}=\frac{x}{4}\cdot\frac{8}{x^2}=\frac{8x}{4x^2}=\frac{2}{x},
\qquad x\ne0 .
$$

Check at $x=2$: original $\frac24\div\frac48=\frac12\div\frac12=1$; simplified $\frac22=1$.

### Solution 9

The fractions already share the denominator $x$:

$$
\frac{2}{x}+\frac{3}{x}=\frac{2+3}{x}=\frac{5}{x},
\qquad x\ne0 .
$$

Check at $x=5$: $\frac25+\frac35=1=\frac55$.

### Solution 10

$$
\frac{5}{x-1}-\frac{2}{x-1}=\frac{5-2}{x-1}=\frac{3}{x-1},
\qquad x\ne1 .
$$

Check at $x=4$: $\frac53-\frac23=1=\frac33$.

### Solution 11

A proportion may be cross-multiplied because both denominators, $3$ and $5$, are nonzero:

$$
\frac{x}{3}=\frac{4}{5}\iff 5x=12\iff x=\frac{12}{5}.
$$

Check: $\frac{12/5}{3}=\frac{12}{15}=\frac45$.

### Solution 12

Cross-multiply (valid for $x\ne0$ and $x+3\ne0$, i.e. $x\ne-3$):

$$
2(x+3)=5x \;\Longrightarrow\; 2x+6=5x \;\Longrightarrow\; 6=3x \;\Longrightarrow\; x=2 .
$$

The candidate $x=2$ is not excluded. Check: $\frac22=1$ and $\frac{5}{5}=1$. The solution set is
$\{2\}$.

## Intermediate

### Solution 13

Factor: $x^2-x-6=(x-3)(x+2)$ and $x^2-4x+3=(x-3)(x-1)$. For $x\ne3,1$,

$$
\frac{(x-3)(x+2)}{(x-3)(x-1)}=\frac{x+2}{x-1}.
$$

Domain: $x\ne3$ and $x\ne1$. Check at $x=0$: original $\frac{-6}{3}=-2$; simplified $\frac{2}{-1}=-2$.

### Solution 14

Factor everything:

$$
x^2-1=(x-1)(x+1),\quad x^2+2x=x(x+2),\quad x^2-4=(x-2)(x+2),\quad x^2+x-2=(x+2)(x-1).
$$

The product is

$$
\frac{(x-1)(x+1)}{x(x+2)}\cdot\frac{(x-2)(x+2)}{(x+2)(x-1)}
=\frac{(x+1)(x-2)}{x(x+2)} .
$$

Domain: $x\ne0$, $x\ne-2$ (denominator factors) and $x\ne1$ (from $x^2+x-2$). Check at $x=3$:
original $\frac{8}{15}\cdot\frac{5}{10}=\frac{4}{15}$; result $\frac{4\cdot1}{3\cdot5}=\frac{4}{15}$.

### Solution 15

Invert the divisor and factor:

$$
\frac{(x-3)(x+3)}{(x+2)^2}\cdot\frac{x+2}{x-3}=\frac{x+3}{x+2}.
$$

Domain: $x\ne-2$ (denominator), $x\ne3$ (divisor vanishes at $3$). Check at $x=0$:
original $\frac{-9}{4}\div\frac{-3}{2}=\frac{-9}{4}\cdot\frac{2}{-3}=\frac32$; result $\frac32$.

### Solution 16

Method A. Write numerator and denominator over their common denominators:

$$
\frac{\frac1x+\frac1y}{\frac1x-\frac1y}
=\frac{\frac{y+x}{xy}}{\frac{y-x}{xy}}
=\frac{y+x}{xy}\cdot\frac{xy}{y-x}
=\frac{x+y}{y-x}.
$$

Domain: $x\ne0$, $y\ne0$ and $x\ne y$. Check at $x=1$, $y=2$: original $\frac{1+0.5}{1-0.5}=3$;
result $\frac{3}{1}=3$.

### Solution 17

Combine the numerator and denominator separately:

$$
1-\frac{9}{x^2}=\frac{x^2-9}{x^2}=\frac{(x-3)(x+3)}{x^2},
\qquad
1+\frac3x=\frac{x+3}{x}.
$$

Divide:

$$
\frac{(x-3)(x+3)}{x^2}\cdot\frac{x}{x+3}=\frac{x-3}{x}.
$$

Domain: $x\ne0$ and $x\ne-3$ (both make an inner denominator vanish). Check at $x=1$:
original $\frac{1-9}{1+3}=\frac{-8}{4}=-2$; result $\frac{-2}{1}=-2$.

### Solution 18

The LCD is $(x-2)(x+3)$, and the domain excludes $2$ and $-3$:

$$
\frac{3}{x-2}+\frac{2}{x+3}
=\frac{3(x+3)+2(x-2)}{(x-2)(x+3)}
=\frac{3x+9+2x-4}{(x-2)(x+3)}
=\frac{5x+5}{(x-2)(x+3)} .
$$

This may be written $\frac{5(x+1)}{(x-2)(x+3)}$. Check at $x=0$: original $-\frac32+\frac23=-\frac56$;
result $\frac{5}{-6}=-\frac56$.

### Solution 19

Use $x^2-9=(x-3)(x+3)$; the LCD is $(x-3)(x+3)$:

$$
\frac{x}{(x-3)(x+3)}-\frac{x+3}{(x-3)(x+3)}
=\frac{x-(x+3)}{(x-3)(x+3)}
=\frac{-3}{(x-3)(x+3)}=-\frac{3}{x^2-9}.
$$

Domain: $x\ne\pm3$. Check at $x=0$: original $0-\frac{1}{-3}=\frac13$; result
$-\frac{3}{-9}=\frac13$.

### Solution 20

Factor $x^2-3x=x(x-3)$; the domain is $x\ne0,3$ and the LCD is $x(x-3)$. Multiply every term:

$$
\frac{x}{x-3}\cdot x(x-3)=x^2,\qquad
\frac{9}{x(x-3)}\cdot x(x-3)=9,\qquad
\frac1x\cdot x(x-3)=x-3 .
$$

The cleared equation is

$$
x^2-9=x-3 \;\Longrightarrow\; x^2-x-6=0 \;\Longrightarrow\; (x-3)(x+2)=0,
$$

so $x=3$ or $x=-2$. The candidate $x=3$ makes the LCD zero and is extraneous; it must be discarded
even though it satisfies the cleared equation. The only solution is $x=-2$.

Check in the original: $\frac{-2}{-5}-\frac{9}{4+6}=\frac25-\frac{9}{10}=\frac{4-9}{10}=-\frac12$ and
$\frac{1}{-2}=-\frac12$. The solution set is $\{-2\}$.

### Solution 21

Cross-multiply, valid for $x\ne-5$ and $x\ne0$:

$$
x(3x-2)=2(x+5) \;\Longrightarrow\; 3x^2-2x=2x+10 \;\Longrightarrow\; 3x^2-4x-10=0 .
$$

The quadratic formula gives

$$
x=\frac{4\pm\sqrt{16+120}}{6}=\frac{4\pm\sqrt{136}}{6}=\frac{4\pm2\sqrt{34}}{6}=\frac{2\pm\sqrt{34}}{3}.
$$

Both values lie in the domain. Check numerically: $\sqrt{34}\approx5.8310$, so the roots are
$2.6103$ and $-1.2770$. For $x=2.6103$: left side $\frac{5.8309}{7.6103}\approx0.7662$, right side
$\frac{2}{2.6103}\approx0.7662$. For $x=-1.2770$: left side $\frac{-5.8310}{3.7230}\approx-1.5662$,
right side $\frac{2}{-1.2770}\approx-1.5662$. The solution set is
$\left\{\frac{2-\sqrt{34}}{3},\frac{2+\sqrt{34}}{3}\right\}$.

### Solution 22

Let $t$ be Ben's time in hours and $t+4$ Ana's. Their rates are $\frac1t$ and $\frac{1}{t+4}$; together
they complete $\frac13$ per hour:

$$
\frac1t+\frac{1}{t+4}=\frac13 .
$$

Multiply by $3t(t+4)$ (legitimate because $t>0$):

$$
3(t+4)+3t=t(t+4) \;\Longrightarrow\; 6t+12=t^2+4t \;\Longrightarrow\; t^2-2t-12=0 .
$$

The quadratic formula gives

$$
t=\frac{2\pm\sqrt{4+48}}{2}=\frac{2\pm\sqrt{52}}{2}=1\pm\sqrt{13}.
$$

The negative root is rejected because a time must be positive. Hence Ben needs $1+\sqrt{13}\approx4.61$
hours and Ana needs $5+\sqrt{13}\approx8.61$ hours.

Check exactly:

$$
\frac{1}{1+\sqrt{13}}+\frac{1}{5+\sqrt{13}}
=\frac{(5+\sqrt{13})+(1+\sqrt{13})}{(1+\sqrt{13})(5+\sqrt{13})}
=\frac{6+2\sqrt{13}}{18+6\sqrt{13}}
=\frac{2(3+\sqrt{13})}{6(3+\sqrt{13})}
=\frac13 .
$$

## Advanced

### Solution 23

Combine the numerator over the LCD $(x-2)(x+2)$:

$$
\frac{1}{x-2}-\frac{2}{x^2-4}
=\frac{x+2-2}{(x-2)(x+2)}=\frac{x}{(x-2)(x+2)} .
$$

Dividing by $\frac{1}{x+2}$ multiplies by $x+2$:

$$
\frac{x}{(x-2)(x+2)}\cdot(x+2)=\frac{x}{x-2}.
$$

Domain: $x\ne2$ and $x\ne-2$. Check at $x=3$: numerator $\frac11-\frac25=0.6$; denominator
$\frac15=0.2$; quotient $3$; result $\frac31=3$.

### Solution 24

Convert to positive exponents:

$$
\frac{x^{-1}-y^{-1}}{x^{-1}+y^{-1}}
=\frac{\frac1x-\frac1y}{\frac1x+\frac1y}
=\frac{\frac{y-x}{xy}}{\frac{y+x}{xy}}
=\frac{y-x}{xy}\cdot\frac{xy}{y+x}
=\frac{y-x}{y+x}.
$$

Domain: $x\ne0$, $y\ne0$, $x\ne-y$. Check at $x=2$, $y=3$:
original $\frac{0.5-0.3333}{0.5+0.3333}=\frac{0.1667}{0.8333}=0.2$; result $\frac{1}{5}=0.2$.

### Solution 25

The LCD is $x^2-1=(x-1)(x+1)$ and the domain is $x\ne\pm1$. Rewrite the right side over the LCD:

$$
\frac{1}{x-1}-\frac{2}{x+1}
=\frac{(x+1)-2(x-1)}{(x-1)(x+1)}
=\frac{x+1-2x+2}{x^2-1}
=\frac{3-x}{x^2-1}.
$$

The equation becomes $\frac{6}{x^2-1}=\frac{3-x}{x^2-1}$, so, on the domain, $6=3-x$, giving $x=-3$.

The candidate is admissible. Check: left side $\frac{6}{9-1}=\frac34$; right side
$\frac{1}{-4}-\frac{2}{-2}=-\frac14+1=\frac34$. The solution set is $\{-3\}$.

### Solution 26

Factor $x^2+x-2=(x-1)(x+2)$; the domain is $x\ne1,-2$. Combine the left side over that LCD:

$$
\frac{3}{x-1}-\frac{2}{x+2}
=\frac{3(x+2)-2(x-1)}{(x-1)(x+2)}
=\frac{3x+6-2x+2}{(x-1)(x+2)}
=\frac{x+8}{(x-1)(x+2)}.
$$

The equation is $\frac{x+8}{(x-1)(x+2)}=\frac{5}{(x-1)(x+2)}$, hence $x+8=5$ and $x=-3$.

The candidate is admissible. Check: $\frac{3}{-4}-\frac{2}{-1}=-0.75+2=1.25$; right side
$\frac{5}{9-3-2}=\frac54=1.25$. The solution set is $\{-3\}$.

### Solution 27

(a) Inverse variation with the square means $y=\frac{k}{x^2}$. Substituting $x=2$, $y=3$ gives
$3=\frac{k}{4}$, so $k=12$.

(b) $y=\frac{12}{6^2}=\frac{12}{36}=\frac13$.

(c) Solve $\frac{12}{x^2}=\frac34$. Since $x^2>0$, multiply by $x^2$: $12=\frac34x^2$, so $x^2=16$
and $x=\pm4$.

Checks: at $x=2$, $\frac{12}{4}=3$; at $x=4$, $\frac{12}{16}=\frac34$; at $x=-4$ the same.

### Solution 28

(a) $\bar C(100)=\frac{8000+600}{100}=\frac{8600}{100}=86$ dollars;
$\bar C(1000)=\frac{8000+6000}{1000}=14$ dollars.

(b) Write $\bar C(x)=\frac{8000}{x}+6$. As $x$ grows, $\frac{8000}{x}$ becomes arbitrarily small, so
$y=6$ is a horizontal asymptote: with very many units the average cost approaches the variable cost
of $\$6$ per unit. The line $x=0$ is a vertical asymptote of the formula, but $x=0$ is excluded from
the domain because production is positive.

(c) Since $x>0$, multiplying $\frac{8000+6x}{x}\le8$ by $x$ preserves the inequality:

$$
8000+6x\le8x \;\Longrightarrow\; 8000\le2x \;\Longrightarrow\; x\ge4000 .
$$

Check: $\bar C(4000)=\frac{8000+24000}{4000}=8$; $\bar C(3000)=\frac{8000+18000}{3000}=\frac{26}{3}>8$.

### Solution 29

Factor: $3x^2-3=3(x-1)(x+1)$ and $x^2+2x-3=(x+3)(x-1)$. Hence

$$
R(x)=\frac{3(x-1)(x+1)}{(x+3)(x-1)}=\frac{3(x+1)}{x+3},
\qquad x\ne1,\ -3 .
$$

* Domain: $\mathbb{R}\setminus\{1,-3\}$.
* Hole: the factor $x-1$ cancels, so the point $\left(1,\frac{3\cdot2}{4}\right)=\left(1,\frac32\right)$
  is missing from the graph.
* Vertical asymptote: $x=-3$, from the uncancelled factor $x+3$.
* Horizontal asymptote: degrees are equal and leading coefficients are $3$ and $1$, so $y=3$.
* Zeros: $3(x+1)=0$ gives $x=-1$, which is in the domain.

Check at $x=0$: original $\frac{-3}{-3}=1$; reduced $\frac{3}{3}=1$.
Check at $x=2$: original $\frac{9}{5}=1.8$; reduced $\frac{9}{5}=1.8$.

### Solution 30

**Claim.** For $a,b,c,d\in\mathbb{R}$ with $b\ne0$ and $d\ne0$, $\frac ab=\frac cd$ if and only if
$ad=bc$.

*Proof of ($\Rightarrow$).* Assume $\frac ab=\frac cd$. Since $b\ne0$ and $d\ne0$, the product $bd$ is
nonzero, so multiplying both sides by $bd$ is legitimate:
$\frac{abd}{b}=\frac{cbd}{d}$. Simplifying with the cancellation law gives $ad=bc$.

*Proof of ($\Leftarrow$).* Assume $ad=bc$. Since $bd\ne0$, it has an inverse $\frac{1}{bd}$.
Multiplying both sides by $\frac{1}{bd}$ gives $\frac{ad}{bd}=\frac{bc}{bd}$, that is $\frac ab=\frac cd$
(using Proposition 8.1 of the tutorial with $k=d$ on the left and $k=b$ on the right).

*Where the hypotheses are used.* $b\ne0$ makes $\frac ab$ defined and is needed when dividing by $b$;
$d\ne0$ does the same for $\frac cd$; together they make $bd\ne0$, which is what allows multiplication
by $bd$ to be reversed. If $b=0$ or $d=0$ the expressions are undefined and the statement has no
meaning — for example $ad=bc$ can hold with $b=0$ while no proportion exists. $\blacksquare$

## Challenge

### Solution 31

The domain is $x\ne2$. Multiply both sides by $x-2$:

$$
x=k+3(x-2)=k+3x-6 \;\Longrightarrow\; -2x=k-6 \;\Longrightarrow\; x=\frac{6-k}{2}.
$$

For a given $k$ there is exactly one candidate, $x=\frac{6-k}{2}$. The equation has no solution
exactly when this candidate is excluded, that is when $\frac{6-k}{2}=2$. Solving: $6-k=4$, so $k=2$.

For every $k\ne2$ the candidate satisfies $x\ne2$, and substituting it into the cleared equation is
reversible there (the multiplier $x-2$ is nonzero), so it is a genuine solution and it is unique.

Check $k=2$: the equation is $\frac{x}{x-2}=\frac{2}{x-2}+3$; clearing gives $x=2+3x-6$, so $x=2$,
which is excluded. No solution. Check $k=4$: $x=1$, and $\frac{1}{-1}=-1$ while
$\frac{4}{-1}+3=-1$. Correct. Answer: $k=2$.

### Solution 32

Factor numerator and denominator:

$$
x^3-x=x(x^2-1)=x(x-1)(x+1),
\qquad
x^2+x-2=(x+2)(x-1).
$$

For $x\ne1,-2$,

$$
R(x)=\frac{x(x-1)(x+1)}{(x+2)(x-1)}=\frac{x(x+1)}{x+2}.
$$

* Domain: $\mathbb{R}\setminus\{1,-2\}$.
* Hole: at $x=1$, with height $\frac{1\cdot2}{3}=\frac23$.
* Vertical asymptote: $x=-2$.
* Zeros: $x=0$ and $x=-1$, both in the domain.
* Slant asymptote: divide $x^2+x$ by $x+2$:

$$
x^2+x=(x+2)(x-1)+2,
\qquad
R(x)=x-1+\frac{2}{x+2}.
$$

  So $y=x-1$ is the slant asymptote.

Check at $x=2$: original $\frac{8-2}{4+2-2}=\frac64=1.5$; reduced $\frac{2\cdot3}{4}=1.5$.
Check at $x=-3$: original $\frac{-27+3}{9-3-2}=\frac{-24}{4}=-6$; reduced $\frac{(-3)(-2)}{-1}=-6$.

### Solution 33

Let $t$ be the time of the faster pipe in hours; the other needs $t+2$. The combined time is
$2$ hours $24$ minutes $=2+\frac{24}{60}=\frac{12}{5}$ hours, so the combined rate is $\frac{5}{12}$:

$$
\frac1t+\frac{1}{t+2}=\frac{5}{12}.
$$

Multiply by $12t(t+2)$, legitimate for $t>0$:

$$
12(t+2)+12t=5t(t+2)
\;\Longrightarrow\;
24t+24=5t^2+10t
\;\Longrightarrow\;
5t^2-14t-24=0 .
$$

The discriminant is $196+480=676=26^2$, so

$$
t=\frac{14\pm26}{10}.
$$

Thus $t=4$ or $t=-\frac65$. The negative value is rejected because a time is positive. The pipes need
$4$ hours and $6$ hours alone.

Check: $\frac14+\frac16=\frac{3}{12}+\frac{2}{12}=\frac{5}{12}$, and $\frac{12}{5}$ hours is
$2$ hours $24$ minutes.

### Solution 34

Let $x$ be the litres of pure acid added. Initially the tank holds $0.30\cdot60=18$ litres of acid.
After adding $x$ litres of acid, the acid amount is $18+x$ and the volume is $60+x$. The required
concentration is $50\%=\frac12$:

$$
\frac{18+x}{60+x}=\frac12 .
$$

Cross-multiply (valid because $60+x>0$):

$$
2(18+x)=60+x \;\Longrightarrow\; 36+2x=60+x \;\Longrightarrow\; x=24 .
$$

Check: $18+24=42$ litres of acid in $60+24=84$ litres of solution, and $\frac{42}{84}=\frac12=50\%$.

### Solution 35

**Claim.** Let $M$ be a rational expression and $a\in\operatorname{dom}M$ with $M(a)\ne0$. Then for
expressions $A,B$ defined at $a$,
$$A(a)=B(a)\iff A(a)M(a)=B(a)M(a).$$

*Proof.* ($\Rightarrow$) If $A(a)=B(a)$, multiplying that equality by the number $M(a)$ gives
$A(a)M(a)=B(a)M(a)$. ($\Leftarrow$) If $A(a)M(a)=B(a)M(a)$, multiply by the number
$\frac{1}{M(a)}$, which exists because $M(a)\ne0$:
$A(a)M(a)\cdot\frac{1}{M(a)}=B(a)M(a)\cdot\frac{1}{M(a)}$, that is $A(a)=B(a)$. $\blacksquare$

**Deduction.** Let $x=a$ be a solution of $A(x)M(x)=B(x)M(x)$. If $M(a)\ne0$ (and $M$ is defined at
$a$), the equivalence above gives $A(a)=B(a)$, so $a$ solves the original equation. The only other
possibility is $M(a)=0$. Hence every solution of the multiplied equation either solves the original
or makes the multiplier zero.

When $M$ is the LCD of the denominators of a rational equation, a value with $M(a)=0$ is a value at
which some original denominator vanishes; the original equation is not defined there, so such a
candidate cannot be a solution. This is exactly why every candidate must be tested in the original
equation after clearing denominators.

### Solution 36

The domain is $x\ne1,2,3$. Multiply by the LCD $(x-1)(x-2)(x-3)$:

$$
(x-2)(x-3)+(x-1)(x-3)+(x-1)(x-2)=0 .
$$

Expand each product:

$$
(x^2-5x+6)+(x^2-4x+3)+(x^2-3x+2)=0,
$$

so

$$
3x^2-12x+11=0 .
$$

The quadratic formula gives

$$
x=\frac{12\pm\sqrt{144-132}}{6}=\frac{12\pm\sqrt{12}}{6}=\frac{12\pm2\sqrt3}{6}=2\pm\frac{\sqrt3}{3}.
$$

Both candidates lie in the domain: $\frac{\sqrt3}{3}\approx0.577$, so the roots are approximately
$2.577$ and $1.423$, neither of which is $1$, $2$ or $3$.

Check exactly for $x=2+s$ with $s=\frac{\sqrt3}{3}$ (so $s^2=\frac13$):

$$
\frac{1}{1+s}+\frac1s-\frac{1}{1-s}
=\left(\frac{1}{1+s}-\frac{1}{1-s}\right)+\frac1s
=\frac{-2s}{1-s^2}+\frac1s
=\frac{-2s}{2/3}+\frac{3}{\sqrt3}
=-3s+\sqrt3
=-\sqrt3+\sqrt3=0 .
$$

The other root $x=2-s$ is handled by symmetry: the expression changes sign under $s\mapsto-s$ in the
first and third terms, and the computation is the same. The solution set is
$\left\{2-\frac{\sqrt3}{3},\,2+\frac{\sqrt3}{3}\right\}$.
