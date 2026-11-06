# Derivatives — Exercises

> [Tutorial](README.md) · [Solutions](solutions.md)

Work without a calculator unless the problem explicitly asks for a decimal answer; where a decimal is wanted
it is marked $\approx$. Give every derivative you are asked for *from the definition* when the problem says
"from the definition" — otherwise the elementary formulas of Section 7.6 and linearity may be used. Problems
25–31 are proofs, and problems 32–36 are deliberately hard: a complete answer there is a proof or a
fully justified construction, not only a number.

## Beginner

**1.** For $f(x) = x^2$, compute the average rate of change on $[1,3]$ and then $f'(1)$ from the definition.
Explain why the two numbers differ.

**2.** Differentiate $f(x) = 4 - 5x$ from the definition. What does the answer say about the graph, and what
is the average rate of change on $[0,2]$?

**3.** Differentiate $f(x) = 2x^2 - 3x + 1$ from the definition, and evaluate $f'(2)$.

**4.** Differentiate $f(x) = \dfrac1x$ at $x = 3$ from the definition.

**5.** Differentiate $f(x) = \sqrt{x}$ at $x = 25$ from the definition.

**6.** Using the power rule, find $f'(x)$ for $f(x) = x^4$, and hence $f'(-2)$.

**7.** Find the tangent line to $y = x^2 - 4x$ at $x = 3$. Verify that the line meets the curve only at the
point of tangency, counted with multiplicity.

**8.** Show that $f(x) = \lvert x+1\rvert$ is not differentiable at $x = -1$, by computing both one-sided
derivatives.

**9.** Find the tangent line to $y = x^3$ at $x = -1$.

**10.** For $f(x) = \sin x$, state $f'(x)$ and evaluate $f'(\pi/3)$, $f'(\pi/2)$ and $f'(\pi)$.

**11.** For $f(x) = e^x$, state $f'(x)$, evaluate $f'(0)$ and $f'(\ln 5)$, and write the tangent line at
$x = 0$.

**12.** For $f(x) = \ln x$, state $f'(x)$ and its domain, evaluate $f'(1)$ and $f'(e^2)$, and write the
tangent line at $x = 1$.

## Intermediate

**13.** Differentiate $f(x) = \dfrac{x}{x+1}$ at $x = 1$ from the definition. (Combine the two fractions over
a common denominator before dividing by $h$.)

**14.** Find $m$ and $c$ so that

$$f(x) = \begin{cases} x^2, & x \le 2,\\ mx + c, & x > 2\end{cases}$$

is differentiable at $x = 2$. Explain which condition fixes which constant.

**15.** Explain why $f(x) = x^{2/3}$ has no derivative at $x = 0$. Compute both one-sided limits of the
difference quotient and describe the graph near the origin.

**16.** For $f(x) = x^5 - 3x^3 + 2x$, compute $f'$, $f''$, $f'''$, $f^{(4)}$, $f^{(5)}$ and $f^{(6)}$.

**17.** A particle moves on a line with $s(t) = t^3 - 6t^2 + 9t$ metres at time $t$ seconds. Find $v(t)$ and
$a(t)$, evaluate both at $t = 2$, and find all times at which the velocity is zero.

**18.** A stone is dropped from a height of $45$ m, so its height is $h(t) = 45 - 4.9t^2$ metres after $t$
seconds. Find the velocity function, the velocity at $t = 1$, the time of impact, and the speed at impact.
Give decimal answers to two places.

**19.** Use the linearisation of $f(x) = \sqrt x$ at $x = 100$ to estimate $\sqrt{101}$. Compare with the true
value and state the sign and size of the error.

**20.** Use the tangent at $x = 0$ to estimate $\sin(0.1)$ and $\sin(0.5)$, and compare each with the true
value. Why is the second estimate so much worse?

**21.** The edge of a cube is measured as $5$ cm with a possible error of $\pm 0.05$ cm. Use differentials to
estimate the maximum error in the computed volume, both absolutely and as a percentage. Compare with the
exact change when the edge is $5.05$ cm.

**22.** A manufacturer's cost function is $C(q) = 0.02q^3 - 0.5q^2 + 40q + 100$ dollars for $q$ units. Find
the marginal cost at $q = 10$ and compare it with the actual cost of producing the eleventh unit.

**23.** A spherical balloon is inflated so that its radius passes through the values $2$ cm to $2.1$ cm.
Compute the average rate of change of the surface area $A(r) = 4\pi r^2$ on $[2, 2.1]$ and the instantaneous
rate $A'(2)$, in cm² per cm.

**24.** Let $f(x) = x\lvert x\rvert$. Show from the definition that $f'(0)$ exists and equals $0$, and show
that $f'(x) = 2\lvert x\rvert$ for $x \ne 0$.

## Advanced

**25.** Prove from the definition that $(\cos x)' = -\sin x$, including a proof of the limit
$\lim_{h\to0}\dfrac{\cos h - 1}{h} = 0$.

**26.** Define $g(0) = 0$ and $g(x) = x^3\sin(1/x)$ for $x \ne 0$. Prove that $g$ is differentiable
everywhere, that $g'$ is continuous at $0$, and that $g''(0)$ does not exist. (For $x\ne0$ the derivative may
be computed with the product and chain rules of
[Differentiation Rules](../04-differentiation-rules/README.md), or directly from the definition.)

**27.** Prove that if $f$ is differentiable at $a$, then there are $\delta>0$ and $M>0$ such that
$\lvert f(x) - f(a)\rvert \le M\lvert x - a\rvert$ whenever $\lvert x - a\rvert < \delta$.

**28.** Prove that if $f$ is differentiable on $\mathbb{R}$ and even (that is $f(-x) = f(x)$ for all $x$),
then $f'$ is odd. State and prove the corresponding statement for an odd $f$.

**29.** Find all tangent lines to the parabola $y = x^2$ that pass through the point $(1,-3)$. (The point is
not on the parabola.)

**30.** Suppose $f'(a) > 0$. Prove that there is a $\delta > 0$ such that $f(x) > f(a)$ for
$a < x < a+\delta$ and $f(x) < f(a)$ for $a-\delta < x < a$. Explain why this does *not* say that $f$ is
increasing on $(a-\delta, a+\delta)$.

**31.** Let $f(x) = \lvert x\rvert + \lvert x-1\rvert$. Show that $f$ is continuous everywhere, give a
formula for $f$ on each of the intervals $(-\infty,0)$, $(0,1)$ and $(1,\infty)$, and determine at which
points $f$ is not differentiable.

## Challenge

**32.** Define $f(0) = 0$ and $f(x) = x^2\sin(1/x^2)$ for $x \ne 0$. Prove that $f$ is differentiable at
every point, compute $f'(x)$ for $x \ne 0$, and prove that $f'$ is unbounded on every interval containing
$0$. (Thus a derivative can exist everywhere and still be wildly discontinuous.) As in Problem 26, the
product and chain rules may be used away from $0$.

**33.** Let $W$ be the Weierstrass function of Section 7.5, which is continuous everywhere and differentiable
nowhere, and let $F(x) = x^2W(x)$. Prove that $F$ is continuous everywhere, differentiable at $0$ with
$F'(0) = 0$, and differentiable at no other point.

**34.** Let $f$ be differentiable at $a$ with $f(a) = 0$. Prove that $\lvert f\rvert$ is differentiable at
$a$ if and only if $f'(a) = 0$, and that in that case $(\lvert f\rvert)'(a) = 0$. Then show that if
$f(a) \ne 0$, then $\lvert f\rvert$ is differentiable at $a$ without any extra hypothesis.

**35.** Newton's method finds a root of $f$ by following the tangent line at a current guess. Derive the
iteration

$$x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}.$$

Apply it to $f(x) = x^2 - 2$ starting from $x_0 = 1$, compute $x_1, x_2, x_3$ exactly as fractions, and
compare $x_3$ with $\sqrt2$ to how many decimal places?

**36.** Prove that if $f'(a)$ exists then the **symmetric difference quotient** satisfies

$$\lim_{h\to0}\frac{f(a+h) - f(a-h)}{2h} = f'(a).$$

Then show that the converse fails, by computing the symmetric quotient for $f(x) = \lvert x\rvert$ at $a = 0$.
What does this example warn you about numerical differentiation?
