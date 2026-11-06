# Root Finding — Exercises

> [Tutorial](README.md) · 36 problems · Levels: Beginner, Intermediate, Advanced, Challenge

Numbers should be given to the precision stated; "about" means three significant digits. For every
iteration you are asked to perform, tabulate the iterates. Theorem numbers refer to the
[tutorial](README.md). Full solutions are in [solutions.md](solutions.md).

## Beginner

**1.** Verify that $[2,3]$ brackets a root of $f(x)=x^{3}-2x-5$, and perform three bisection steps,
tabulating $a_n$, $b_n$, $x_n$ and $f(x_n)$.

**2.** How many bisection steps on $[1,2]$ guarantee an error of at most $10^{-8}$?

**3.** For $f(x)=x-\cos x$ on $[0,1]$, perform three bisection steps. Give the final interval and the
guaranteed error bound.

**4.** Show that $g(x)=\sqrt{x+2}$ maps $[1,2]$ into $[1,2]$ and is a contraction there. Give the best
constant $L$ you can, and the fixed point.

**5.** For $g(x)=\cos x$ on $[0,1]$, verify the hypotheses of the contraction mapping theorem and state
what the theorem guarantees for $x_0=0.5$.

**6.** Apply two Newton steps to $f(x)=x^{2}-3$ from $x_0=2$. Give the iterates and their errors.

**7.** Apply two Newton steps to $f(x)=x^{3}-8$ from $x_0=3$.

**8.** Classify the order of convergence from each error sequence: (a) $4.0\times10^{-1}$,
$1.6\times10^{-1}$, $6.4\times10^{-2}$, $2.56\times10^{-2}$; (b) $10^{-2}$, $10^{-4}$, $10^{-8}$,
$10^{-16}$.

**9.** For $x^{2}-3=0$, compute $g'(\sqrt3)$ for $g(x)=x^{2}+x-3$, $g(x)=3/x$ and $g(x)=(x+3/x)/2$.
Which iterations converge from a nearby start, and how fast?

**10.** Perform one secant step for $f(x)=x^{2}-2$ with $x_0=1$, $x_1=2$, and give $x_2$.

**11.** What is the multiplicity of the root $2$ of $f(x)=(x-2)^{3}(x+1)$, and what linear rate does
Newton's method have there?

**12.** Apply two Newton steps to $f(x)=(x-1)^{2}$ from $x_0=3$, and state the convergence rate.

**13.** For $f(x)=1000(x-1)$ at $x=1+10^{-9}$ the residual is $10^{-6}$. Explain why this does not mean
the error is small, and what a sound stopping test would be.

## Intermediate

**14.** Bisect $f(x)=x-\cos x$ on $[0,1]$ until the bracket width is at most $10^{-4}$. How many steps
are needed, what is the final midpoint, and what is its actual error?

**15.** Iterate $x_{n+1}=\sqrt{x_n+2}$ from $x_0=1$ five times. Tabulate the errors, the ratios, and
compare the ratios with the contraction constant.

**16.** For $g(x)=(x^{2}+2)/3$, show that $1$ is attracting and $2$ is repelling, and iterate from
$x_0=1.1$ and from $x_0=1.9$ for five steps. Explain the difference.

**17.** Apply Newton's method to $f(x)=x^{3}-2x-5$ from $x_0=2.1$, tabulating four steps. Compare the
number of steps needed with the run from $x_0=2.5$ (four steps to $10^{-11}$).

**18.** Apply Newton's method to $f(x)=x^{3}$ from $x_0=1$ and determine the order and rate. Explain
the result using the multiplicity.

**19.** Apply the secant method to $f(x)=x^{3}-2x-5$ with $x_0=2$, $x_1=3$ for four steps, and check the
relation $e_{n+1}\approx Ce_ne_{n-1}$.

**20.** Apply the secant method to $f(x)=x-\cos x$ with $x_0=0$, $x_1=1$ for four steps. What order of
convergence do the errors suggest?

**21.** Apply the modified Newton iteration with $m=2$ to $f(x)=x^{3}-3x+2$ from $x_0=0.5$ for four
steps, and compare with the plain Newton iterates from the same start.

**22.** Apply Newton's method to $p(x)=x^{3}-6x^{2}+11x-6$ from $x_0=3.2$ until convergence, then
deflate and solve the resulting quadratic. Verify the roots.

**23.** For Newton's method on $x^{2}-2$ from $x_0=1.5$, tabulate $\lvert x_n-r\rvert$ and
$\lvert x_n-x_{n-1}\rvert$. How do they compare, and what does that imply for a stopping test?

**24.** Let $r(\varepsilon)$ be the positive root of $x^{2}-2+\varepsilon=0$. Compute $dr/d\varepsilon$
at $\varepsilon=0$ and estimate the change in the root for $\varepsilon=10^{-10}$. Compare with the
direct computation.

## Advanced

**25.** Prove the contraction mapping theorem on an interval: existence, uniqueness, geometric
convergence, and both error estimates.

**26.** Prove that Newton's method converges quadratically at a simple root, with the constant
$\lvert f''(r)\rvert/(2\lvert f'(r)\rvert)$.

**27.** Derive the secant error relation $e_{n+1}\approx Ce_ne_{n-1}$ and deduce that the order is
$\varphi=(1+\sqrt5)/2$.

**28.** Prove that Newton's method converges linearly with rate $1-1/m$ at a root of multiplicity $m$,
and that the modified iteration with the known $m$ is quadratic.

**29.** Let $g$ be continuously differentiable at a fixed point $r$. Prove that the fixed-point
iteration converges locally if $\lvert g'(r)\rvert<1$ and diverges from any nearby start if
$\lvert g'(r)\rvert>1$.

**30.** Prove that the bisection error bound $\lvert x_n-r\rvert\le(b-a)/2^{n+1}$ is best possible in the
sense that for each $n$ there is a continuous $f$ on $[a,b]$ for which the bound is attained.

**31.** Show that Newton's method for $f(x)=x^{2}-a$ with $a>0$ is the Babylonian iteration
$x_{n+1}=\tfrac12(x_n+a/x_n)$, prove that it converges for every $x_0>0$, and determine its order.

**32.** Let $f$ be convex and increasing on $[a,b]$ with $f(a)<0<f(b)$. Prove that Newton's method
started at $b$ produces a decreasing sequence converging to the root, and that it never leaves $[a,b]$.

## Challenge

**33.** Prove that Newton's method for $f(x)=x^{3}-2x+2$ cycles with period two between $0$ and $1$,
and explain why this does not contradict the quadratic convergence theorem.

**34.** For $f(x)=\arctan x$, show that $\Phi(x)=x-(1+x^{2})\arctan x$ satisfies $\Phi(x)=-x$ exactly
when $2x=(1+x^{2})\arctan x$, and determine the boundary of the basin of attraction numerically. What
happens to the iterates started just beyond it?

**35.** For $p(x)=(x-1)(x-2)(x-3)$, the constant coefficient is perturbed by $10^{-10}$. Use
$\partial r/\partial a_0=-1/p'(r)$ to predict the shift of each root, and verify by computing the roots
of the perturbed polynomial numerically. Which root is most sensitive, and why?

**36.** For $f(x)=x^{3}-2x-5$ on $[2,3]$, compare bisection, Newton from $x_0=2.5$, and the secant
method from $x_0=2,x_1=3$ by the number of *function evaluations* needed to reach an error of
$10^{-12}$. Which method wins, and by how much?
