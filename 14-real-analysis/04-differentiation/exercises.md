# Differentiation — Exercises

> [Tutorial](README.md) · 36 problems · Levels: Beginner, Intermediate, Advanced, Challenge

Every problem asks for a proof or for a computation with a justification: when you differentiate, name
the rule you use; when you apply L'Hôpital's rule or Taylor's theorem, verify the hypotheses. You may
use anything proved in the [tutorial](README.md) and in
[Continuity and Limits of Functions](../03-continuity-and-limits/README.md), together with the standard
derivatives of $\sin$, $\cos$, $\tan$, $\exp$ and $\log$ from elementary calculus (these are the entries
in the table of Section 8 of the tutorial).

Full solutions are in [solutions.md](solutions.md). Do not open that file until you have attempted the
problems.

## Beginner

**1.** Using Definition 5.1, prove that $f(x) = x^2$ is differentiable at $a = 3$ with $f'(3) = 6$, and find the equation of the tangent line at $(3,9)$.

**2.** Using Definition 5.1, prove that $f(x) = 1/x$ is differentiable at every $a \ne 0$, and compute $f'(a)$.

**3.** Using Definition 5.1, prove that $f(x) = \sqrt x$ is differentiable at $a = 4$, and compute $f'(4)$.

**4.** Differentiate $f(x) = (x^2+1)(x^3-2x)$ with the product rule, then expand the product and differentiate the expansion; check that the answers agree.

**5.** Differentiate $\displaystyle f(x) = \frac{2x+1}{x^2+1}$ with the quotient rule.

**6.** Differentiate, naming the rule used at each step:
$$
\text{(a) } (3x^2+1)^5, \qquad \text{(b) } \sin(x^3), \qquad \text{(c) } \sqrt{x^2+3}.
$$

**7.** Let $f(x) = x^4 - 2x^3 + x$. Compute $f'$, $f''$ and $f'''$, and evaluate all three at $x = 1$.

**8.** Let $f(x) = \lvert x - 2\rvert$. Compute the one-sided derivatives $f'_-(2)$ and $f'_+(2)$, and determine the set of points at which $f$ is differentiable.

**9.** Let $f(x) = x^{1/3} = \sqrt[3]{x}$. Compute $f'(a)$ for $a \ne 0$ from the definition, and prove that $f$ is not differentiable at $0$.

**10.** Let $f(x) = x\lvert x\rvert$. Prove that $f$ is differentiable at every point of $\mathbb{R}$, and compute $f'(x)$.

**11.** Find the tangent line to $y = x^3 - 3x$ at $x = 2$, and find all points at which the tangent is horizontal.

**12.** The area of a disc of radius $r$ is $A(r) = \pi r^2$. Compute $A'(3)$ and interpret the number geometrically.

## Intermediate

**13.** Prove that $\dfrac{d}{dx}\tan x = \sec^2 x$ at every $x$ with $\cos x \ne 0$, stating every rule used.

**14.** Let $f$ be differentiable on $(-a,a)$.

(a) If $f$ is even, that is $f(-x) = f(x)$ for all $x$, prove that $f'$ is odd.

(b) If $f$ is odd, that is $f(-x) = -f(x)$ for all $x$, prove that $f'$ is even.

**15.** Let $f, g$ be twice differentiable at $a$. Prove the Leibniz formula
$$
(fg)''(a) = f''(a)g(a) + 2f'(a)g'(a) + f(a)g''(a).
$$

**16.** Let $f$ be differentiable at $a$ and suppose $f(a) = 0$. Prove that $\lvert f\rvert$ is differentiable at $a$ if and only if $f'(a) = 0$, and that in that case $(\lvert f\rvert)'(a) = 0$.

**17.** Define
$$
f(x) = \begin{cases} x^2, & x \in \mathbb{Q},\\ 0, & x \notin \mathbb{Q}.\end{cases}
$$
Prove that $f$ is differentiable at $0$ with $f'(0) = 0$, and is not differentiable at any $a \ne 0$. (You may use the density of $\mathbb{Q}$ and of the irrationals.)

**18.** Prove that for every $x > 0$,
$$
\frac{x}{1+x} < \ln(1+x) < x .
$$

**19.** Compute the following limits, verifying the hypotheses of L'Hôpital's rule at each application:
$$
\text{(a) } \lim_{x\to 0}\frac{e^x - 1 - x}{x^2}, \qquad \text{(b) } \lim_{x\to 0}\frac{\tan x - x}{x^3}.
$$

**20.** Compute:
$$
\text{(a) } \lim_{x\to 0^+} x\ln x, \qquad \text{(b) } \lim_{x\to\infty} x^{1/x}.
$$

**21.** Prove that for all $a, b \in \mathbb{R}$,
$$
\lvert\sin a - \sin b\rvert \le \lvert a-b\rvert, \qquad \lvert\cos a - \cos b\rvert \le \lvert a-b\rvert .
$$

**22.** Let $f$ be differentiable on $(0,\infty)$ with $f'(x) = 1/x$ for all $x > 0$ and $f(1) = 0$. Prove that
$$
f(xy) = f(x) + f(y) \qquad \text{for all } x, y > 0,
$$
and that $f$ is strictly increasing.

## Advanced

**23.** (Darboux's theorem.) Let $f$ be differentiable on $[a,b]$ and suppose $f'(a) < \lambda < f'(b)$. Prove that there exists $c \in (a,b)$ with $f'(c) = \lambda$. *Hint:* apply the extreme value theorem and Fermat's lemma to $g(x) = f(x) - \lambda x$, and show that the minimum of $g$ is attained neither at $a$ nor at $b$.

**24.** (a) Prove that if $f$ is differentiable on an interval $I$ and $\lvert f'(x)\rvert \le M$ for all interior $x$, then $f$ is uniformly continuous on $I$.

(b) Show by example that the converse fails: a uniformly continuous differentiable function whose derivative is unbounded. Prove all claims about your example.

**25.** (Bernoulli's inequality.) Prove that for every $n \in \mathbb{N}$ and every $x \ge -1$,
$$
(1+x)^n \ge 1 + nx .
$$

**26.** Let $f$ be differentiable on $[0,\infty)$ with $f(0) = 0$ and
$$
\lvert f'(x)\rvert \le \lvert f(x)\rvert \qquad \text{for all } x \ge 0 .
$$
Prove that $f(x) = 0$ for all $x \ge 0$. *Hint:* let $M$ be the maximum of $\lvert f\rvert$ on $[0,1/2]$ and apply the mean value theorem on $[0,c]$ where $c$ is a point at which the maximum is attained.

**27.** Prove that for every $x \in [0,1]$,
$$
\left\lvert e^x - \left(1 + x + \frac{x^2}{2}\right)\right\rvert \le \frac{e\,x^3}{6}.
$$

**28.** Let $f$ be twice differentiable on $[0,1]$ with $f(0) = f(1) = 0$ and $f''(x) > 0$ for all $x \in (0,1)$. Prove that $f(x) < 0$ for every $x \in (0,1)$.

**29.** Let $f$ be differentiable and convex on an interval $I$. Prove the tangent-line inequality
$$
f(y) \ge f(x) + f'(x)(y-x) \qquad \text{for all } x, y \in I .
$$

**30.** Let $f$ be differentiable on $\mathbb{R}$ and suppose there is $m > 0$ with $f'(x) \ge m$ for all $x$.

(a) Prove that $f$ is a bijection of $\mathbb{R}$ onto $\mathbb{R}$.

(b) Let $g = f^{-1}$. Prove that $g$ is differentiable and that $g'(y) = 1/f'(g(y))$ for all $y$, without assuming that $f'$ is continuous.

(c) Prove that $\lvert g(y) - g(y')\rvert \le \lvert y-y'\rvert/m$ for all $y, y'$.

## Challenge

**31.** Define
$$
f(x) = \begin{cases} x^2\sin\dfrac1x, & x \ne 0,\\ 0, & x = 0.\end{cases}
$$
Prove that $f$ is differentiable at every point of $\mathbb{R}$, that $f'$ is discontinuous at $0$, and that $f$ is not monotone on any open interval containing $0$.

**32.** Prove that there is no differentiable function $f : \mathbb{R} \to \mathbb{R}$ such that
$$
f'(x) = 1 \text{ for } x \ne 0, \qquad f'(0) = 0 .
$$

**33.** Let $f$ be differentiable on $(M_0, \infty)$ and suppose $\lim_{x\to\infty} f'(x) = L \in \mathbb{R}$. Prove that
$$
\lim_{x\to\infty}\frac{f(x)}{x} = L .
$$

**34.** Let $f$ be twice differentiable on a neighbourhood of $a$, with $f''$ continuous at $a$. Prove the *Young form* of Taylor's theorem of order two:
$$
f(x) = f(a) + f'(a)(x-a) + \frac{f''(a)}{2}(x-a)^2 + o\bigl((x-a)^2\bigr) \qquad (x \to a),
$$
that is, prove that
$$
\lim_{x\to a}\frac{f(x)-f(a)-f'(a)(x-a)-\frac12 f''(a)(x-a)^2}{(x-a)^2} = 0 .
$$

**35.** Let $f$ be differentiable on $[0,\infty)$ with $f(0) = 0$ and $f'(x) \le f(x)$ for all $x \ge 0$. Prove that $f(x) \le 0$ for all $x \ge 0$.

**36.** Let $f$ be differentiable on an interval $I$ and suppose that $f'(x) \in \mathbb{Z}$ for every $x \in I$. Prove that $f$ is affine: there are constants $A, B \in \mathbb{R}$ with $f(x) = Ax + B$ on $I$.
