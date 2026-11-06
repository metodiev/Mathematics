# Laplace Transforms — Exercises

> [Laplace Transforms](README.md) · 36 problems · Beginner → Challenge · Solutions: [solutions.md](solutions.md)

Work through the problems in order; each cites the section of the tutorial it draws on. Problems 1–12
build fluency with the definition, the table and simple inverses; 13–23 solve initial value problems,
discontinuous and impulsive forcing, integral equations and transfer functions; 24–31 prove the rules;
32–36 are challenge problems. Attempt every problem before opening [solutions.md](solutions.md), and
finish each one by **substituting the answer back** into the equation or by checking it with a value
theorem.

Conventions: $\mathcal{L}\{f\}(s) = \int_0^\infty e^{-st}f(t)\,dt$, $u(t-a)$ is the unit step and
$\delta(t-a)$ the Dirac delta at $a$. Every answer must state the region of convergence when the
question asks for a transform.

## Beginner

**1.** *(§7.1, §7.2)* From the definition, compute $\mathcal{L}\{3\}$ and $\mathcal{L}\{t\}$, stating the region of convergence in each case.

**2.** *(§7.2)* From the definition, compute $\mathcal{L}\{e^{-2t}\}$ and state its region of convergence. Which growth rate of $f$ would make the region empty?

**3.** *(§7.2)* From the definition, compute $\mathcal{L}\{t^2\}$ by integrating by parts twice, and compare with the formula $n!/s^{n+1}$.

**4.** *(§7.2)* From the definition, compute $\mathcal{L}\{\sin 3t\}$ by integrating by parts twice. Check the result at $s\to\infty$ against the small-$t$ behaviour of $\sin 3t$.

**5.** *(§7.2)* Compute $\mathcal{L}\{\cosh 2t\}$ from the definition (or from the exponential representation) and state the region of convergence.

**6.** *(§7.2)* Use linearity to compute $\mathcal{L}\{4t^2-3e^{2t}+5\sin t\}$, stating the region of convergence.

**7.** *(§7.4)* Compute $\mathcal{L}\{t^3e^{2t}\}$ using the first shifting theorem, and state the region of convergence.

**8.** *(§7.4)* Compute $\mathcal{L}\{e^{-t}\cos 3t\}$.

**9.** *(§7.5)* Compute $\mathcal{L}\{u(t-2)\}$ and $\mathcal{L}\{(t-2)u(t-2)\}$.

**10.** *(§7.5)* Compute $\mathcal{L}\{\delta(t-3)\}$, and explain why the ordinary integral definition cannot be applied to $\delta$ directly.

**11.** *(§7.7)* Find the inverse transforms of (a) $\dfrac{1}{s-4}$, (b) $\dfrac{3}{s^2+9}$, (c) $\dfrac{s}{s^2+16}$.

**12.** *(§7.7)* Find the inverse transforms of (a) $\dfrac{2s+1}{s^2+1}$, (b) $\dfrac{1}{s^2}-\dfrac{1}{s+1}$.

## Intermediate

**13.** *(§7.3, §7.8)* Solve $y''+3y'+2y = 0$ with $y(0) = 0$, $y'(0) = 1$.

**14.** *(§7.3, §7.8)* Solve $y'-y = e^{2t}$ with $y(0) = 0$.

**15.** *(§7.3, §7.8, §9.10)* Solve $y''+4y = \cos 2t$ with $y(0) = y'(0) = 0$. Why is the amplitude growing?

**16.** *(§7.7)* Find the inverse transform of $F(s) = \dfrac{s+1}{(s-1)(s+2)(s+3)}$ by partial fractions, and check the value at $t = 0$ against the initial value theorem.

**17.** *(§7.5, §7.8)* Solve $y'+y = u(t-1)$ with $y(0) = 0$. Describe the solution before and after $t = 1$.

**18.** *(§7.5, §7.7)* Find the inverse transform of $\dfrac{e^{-2s}}{s^2+4}$, and sketch (in words) what the factor $e^{-2s}$ does to the answer.

**19.** *(§7.5, §7.8)* Solve $y''+2y'+y = u(t-2)$ with $y(0) = y'(0) = 0$. Check that $y$ and $y'$ are continuous at $t = 2$.

**20.** *(§7.6, §7.7)* Invert $F(s) = \dfrac{1}{s^2(s+1)}$ by convolution, and confirm the result by partial fractions.

**21.** *(§7.9)* For $y''+4y'+13y = f(t)$, find the transfer function, the impulse response and the step response. Verify that the derivative of the step response is the impulse response.

**22.** *(§8.1)* Find the Laplace transform of the sawtooth wave with period $1$ defined by $f(t) = t$ on $[0,1)$ and extended periodically.

**23.** *(§7.6)* Solve the integral equation
$$y(t) = t+\int_0^ty(\tau)\sin(t-\tau)\,d\tau .$$

## Advanced

**24.** *(§7.3)* Prove the derivative rule $\mathcal{L}\{f'\} = sF(s)-f(0^+)$ with all hypotheses stated, including the justification of the limit of the boundary term.

**25.** *(§7.3)* Prove the integral rule $\mathcal{L}\left\{\int_0^tf\right\} = F(s)/s$ in two ways: from the derivative rule, and by interchanging the order of integration.

**26.** *(§7.4)* Prove the first shifting theorem, including the statement about how the region of convergence changes.

**27.** *(§7.4)* Prove the second shifting theorem. Then explain, with a concrete example, why the factor $u(t-a)$ cannot be omitted.

**28.** *(§7.6)* Prove the convolution theorem. State precisely which theorem permits the interchange of the two integrals and which change of variables is made.

**29.** *(§8.1)* Prove that $\mathcal{L}\{tf(t)\} = -F'(s)$, justifying the differentiation under the integral sign.

**30.** *(§8.1)* Prove the initial value theorem and the final value theorem, stating the hypotheses. Give a function for which $\lim_{s\to0^+}sF(s)$ exists but $\lim_{t\to\infty}f(t)$ does not.

**31.** *(§7.1)* Prove that the region of convergence is a right half-plane, and that $F$ is analytic there with $F'(s) = -\mathcal{L}\{tf(t)\}(s)$.

## Challenge

**32.** *(§7.2)* Using the substitution $u = st$ and the Gamma integral, show that
$$\mathcal{L}\left\{t^{-1/2}\right\} = \sqrt{\frac{\pi}{s}}, \qquad \mathcal{L}\left\{t^{1/2}\right\} = \frac{\sqrt\pi}{2s^{3/2}},$$
and deduce that $\displaystyle\int_0^{\infty}e^{-x^2}dx = \frac{\sqrt\pi}{2}$.

**33.** *(§7.3, §7.6)* Solve the integro-differential equation
$$y'(t) = 1-\int_0^ty(\tau)\,d\tau, \qquad y(0) = 0 .$$
Verify the answer by differentiating the equation.

**34.** *(§7.5)* Solve $y''+4y = 3\delta(t-2)$ with $y(0) = y'(0) = 0$. Verify that $y$ is continuous at $t = 2$ and that $y'$ jumps by exactly $3$.

**35.** *(§7.1)* Prove that $f(t) = e^{t^2}$ has no Laplace transform for any complex $s$. What does this say about the hypothesis of Theorem 7.1?

**36.** *(§7.10)* Compute the two-sided Laplace transform of $f(t) = e^{-a\lvert t\rvert}$ with $a>0$, state its region of convergence, and show that on $s = i\omega$ it equals the Fourier transform. Explain why the one-sided transform of the same function is different.
