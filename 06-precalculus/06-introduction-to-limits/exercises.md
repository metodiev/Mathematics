# Introduction to Limits — Exercises

> [Tutorial](README.md) · 36 problems · Levels: Beginner, Intermediate, Advanced, Challenge

Work each problem completely, and check every numerical answer by a second route — a table of values, a
factorisation, or an estimate from the graph's shape. For every limit you claim *does not exist*, name
the mechanism (jump, oscillation, or unboundedness) and say why the definition cannot be satisfied. For
every $\varepsilon$-$\delta$ problem, write the scratch work separately from the proof. Do not open
[solutions.md](solutions.md) until you have attempted the problems.

## Beginner

**1.** Find the average rate of change of $f(x) = x^{2}+1$ on $[1,3]$.

**2.** A body falls $s(t) = 5t^{2}$ metres in $t$ seconds. Find its average velocity over the interval
$[1,3]$, with units.

**3.** Find the slope of the secant line through the graph of $f(x) = x^{2}-3x$ at $x=2$ and $x=5$.

**4.** Build a table of values at $x = 2.9,\ 2.99,\ 3.01,\ 3.1$ for
$f(x) = \dfrac{x^{2}-9}{x-3}$, and use it to conjecture $\displaystyle\lim_{x\to3}f(x)$. Then prove
your conjecture.

**5.** Evaluate $\displaystyle\lim_{x\to1}\left(3x^{2}-2x+4\right)$.

**6.** Evaluate $\displaystyle\lim_{x\to-2}\left(x^{3}+4x\right)$.

**7.** Evaluate $\displaystyle\lim_{x\to0}\frac{x^{2}+2x}{x}$.

**8.** Let $f(x) = 2x+1$ for $x<2$ and $f(x) = x^{2}-1$ for $x\ge2$. Find both one-sided limits at
$x=2$, and decide whether the two-sided limit exists.

**9.** Evaluate $\displaystyle\lim_{x\to4}\frac{x^{2}-16}{x-4}$.

**10.** Evaluate $\displaystyle\lim_{h\to0}\frac{(3+h)^{2}-9}{h}$.

**11.** Evaluate $\displaystyle\lim_{x\to-1}\frac{x^{2}-1}{x+1}$.

**12.** Evaluate $\displaystyle\lim_{x\to0}|x|$ and $\displaystyle\lim_{x\to0}\frac{|x|}{x}$. Explain
why one exists and the other does not.

**13.** For $f(x) = \dfrac{x^{2}-9}{x-3}$: find $\displaystyle\lim_{x\to3}f(x)$, state whether $f$ is
defined at $3$, and state whether $f$ is continuous at $3$. Name the kind of discontinuity.

## Intermediate

**14.** Evaluate $\displaystyle\lim_{x\to2}\frac{x^{2}-5x+6}{x^{2}-4}$.

**15.** Evaluate $\displaystyle\lim_{x\to0}\frac{\sqrt{4+x}-2}{x}$.

**16.** Evaluate $\displaystyle\lim_{x\to3}\frac{\sqrt{x+1}-2}{x-3}$.

**17.** Evaluate $\displaystyle\lim_{h\to0}\frac{(2+h)^{3}-8}{h}$.

**18.** Evaluate $\displaystyle\lim_{x\to1}\frac{x^{3}-1}{x^{2}-1}$.

**19.** Using the definition of the derivative as a limit of difference quotients, find $f'(2)$ for
$f(x) = \dfrac1x$.

**20.** Find the slope of the tangent to $y=\sqrt{x}$ at $x=9$ from the difference quotient.

**21.** Let $f(x) = ax+1$ for $x<1$ and $f(x) = x^{2}+2$ for $x\ge1$. Find the value of $a$ for which
$\displaystyle\lim_{x\to1}f(x)$ exists, and give the limit.

**22.** Classify the discontinuity of each function at the stated point: (a) $\dfrac{x^{2}-4}{x-2}$ at
$x=2$; (b) $\dfrac{1}{x-3}$ at $x=3$; (c) $\dfrac{|x-1|}{x-1}$ at $x=1$.

**23.** Evaluate $\displaystyle\lim_{x\to0}\frac{\dfrac{1}{x+2}-\dfrac12}{x}$.

**24.** Find the largest intervals on which $f(x) = \dfrac{\sqrt{x-3}}{x-5}$ is continuous.

## Advanced

**25.** Using the definition $f'(a) = \displaystyle\lim_{h\to0}\frac{f(a+h)-f(a)}{h}$, find the slope
of the tangent to $f(x) = x^{2}-3x$ at $x=2$.

**26.** Find the tangent slope to $y=\sqrt{x}$ at $x=4$ from the definition, and give the equation of
the tangent line.

**27.** Prove from Definition 5.2 of the tutorial that $\displaystyle\lim_{x\to1}(4x-3) = 1$, exhibiting
$\delta$ as a function of $\varepsilon$.

**28.** Prove from the definition that $\displaystyle\lim_{x\to-2}(3x+5) = -1$.

**29.** Prove from the definition that $\displaystyle\lim_{x\to3}x^{2} = 9$, using a restriction of the
form $|x-3|<1$.

**30.** Prove that $\displaystyle\lim_{x\to0}\cos\frac1x$ does not exist, by exhibiting two sequences
tending to $0$ along which the function has different limits.

**31.** Prove the sign-preservation property: if $\displaystyle\lim_{x\to a}f(x) = L$ with $L>0$, then
there is $\delta>0$ such that $f(x)>0$ whenever $0<|x-a|<\delta$. (Use $\varepsilon = L/2$.)

## Challenge

**32.** Prove from the definition that $\displaystyle\lim_{x\to2}\left(x^{2}+3x\right) = 10$, giving an
explicit $\delta = \delta(\varepsilon)$ and justifying every inequality in the chain. State clearly
where the restriction $|x-2|<1$ is used.

**33.** Using right-endpoint Riemann sums with $n$ equal subintervals, show that the area under
$y=x^{2}$ from $0$ to $b$ (with $b>0$) is $\dfrac{b^{3}}{3}$, and check the result for $b=2$ against
the value $\dfrac83$.

**34.** Prove that a function has at most one limit at a point: if
$\lim_{x\to a}f(x) = L$ and $\lim_{x\to a}f(x) = M$, then $L = M$. Make explicit where the existence of
points $x\ne a$ arbitrarily close to $a$ is used.

**35.** Prove the squeeze theorem: if $g(x)\le f(x)\le h(x)$ for all $x$ in some punctured
neighbourhood of $a$, and $\lim_{x\to a}g(x) = \lim_{x\to a}h(x) = L$, then
$\lim_{x\to a}f(x) = L$. Then use it to evaluate $\displaystyle\lim_{x\to0}x\sin\frac1x$, and explain
why the same argument does **not** apply to $\displaystyle\lim_{x\to0}\frac{1}{x}\sin\frac1x$.

**36.** A student produces the following table for $\displaystyle\lim_{x\to0}\frac{\sin x}{x}$ and
concludes that the limit is $1$ "because the numbers converge".

| $x$ | $0.1$ | $0.01$ | $0.001$ | $0.0001$ |
|---|---|---|---|---|
| $\sin x/x$ | $0.998334$ | $0.999983$ | $1.000000$ | $1.000000$ |

(a) Explain why the third and fourth entries print as exactly $1.000000$ at six decimal places, and
what that rounding hides about the true error $1 - \sin x/x$. (b) State what additional information
would be needed to turn the conjecture into a proof. (c) The table cannot distinguish the limit $1$
from a limit of $1.0000004$; explain why, and say what this shows about the status of numerical
evidence in the definition of a limit.
