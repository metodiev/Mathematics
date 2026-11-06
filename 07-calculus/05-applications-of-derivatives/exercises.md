# Exercises: Applications of Derivatives

> Companion to the [tutorial](README.md). Solutions are in [solutions.md](solutions.md).

For every sign chart, mark the zeros of the derivative on a number line before choosing test points.
For every closed-interval problem, tabulate the values at all candidates — the endpoints are candidates
too. For every optimisation problem, write the feasible interval before differentiating. Problems are
numbered continuously so that the solutions file mirrors them exactly.

## Beginner

**1.** Find all critical points of $f(x)=x^2-6x+5$ and classify each one using a sign chart of $f'$.

**2.** Determine the intervals on which $f(x)=x^3-12x$ is increasing and decreasing, and locate its
local extrema.

**3.** Determine the intervals of concavity of $f(x)=x^3-6x^2+5x$ and find its inflection points.

**4.** Use the second derivative test to classify the critical points of $f(x)=x^3+3x^2-9x$.

**5.** Find and classify the critical points of $f(x)=x^4-4x^3$. At one of them the second derivative
test is inconclusive; say which and decide the case another way.

**6.** Find the absolute maximum and minimum of $f(x)=x^2-4x+3$ on $[0,3]$.

**7.** Find the absolute maximum and minimum of $f(x)=x^3-3x$ on $[-2,2]$.

**8.** Find the absolute maximum and minimum of $f(x)=\dfrac{1}{x}$ on $[1,4]$. Explain why the method
finds no critical point, and why the extrema nevertheless exist.

**9.** Evaluate $\displaystyle\lim_{x\to0}\frac{\sin 3x}{x}$, stating which indeterminate form occurs.

**10.** Evaluate $\displaystyle\lim_{x\to0}\frac{e^x-1-x}{x^2}$.

**11.** Evaluate $\displaystyle\lim_{x\to\infty}\frac{\ln x}{x}$.

**12.** The radius of a circle increases at $2$ cm/s. How fast is its area increasing when the radius
is $5$ cm?

## Intermediate

**13.** Sketch the graph of $f(x)=x^3-3x^2$: domain, intercepts, monotonicity, local extrema,
concavity, and inflection point.

**14.** Verify the mean value theorem for $f(x)=\sqrt{x}$ on $[1,4]$ by finding the value (or values)
of $c$ that the theorem guarantees.

**15.** Prove that the equation $x^3+3x-1=0$ has exactly one real solution.

**16.** Prove that $e^x\ge1+x$ for every real $x$, and determine where equality holds.

**17.** Evaluate both limits: (a) $\displaystyle\lim_{x\to0}\frac{1-\cos x}{x^2}$;
(b) $\displaystyle\lim_{x\to0}\frac{\tan x-x}{x^3}$.

**18.** Consider $\displaystyle\lim_{x\to0}\frac{x^2\sin(1/x)}{x}$. Compute $f'(x)$ for
$f(x)=x^2\sin(1/x)$ and explain why L'Hôpital's rule cannot be applied, then evaluate the limit by
another method.

**19.** A $10$ m ladder leans against a wall and its top slides down at $1$ m/s. How fast is the foot
moving away from the wall when the top is $6$ m above the ground?

**20.** An inverted conical tank has top radius $2$ m and height $4$ m. Water is poured in at
$2\ \text{m}^3/\text{min}$. How fast is the water level rising when the water is $2$ m deep?

**21.** A rectangular pen is to be built against a straight river, using $100$ m of fencing for the
three land sides. What dimensions maximise the enclosed area?

**22.** A rectangle is inscribed in a circle of radius $5$, with sides parallel to the axes. What is
the largest possible area?

## Advanced

**23.** An open-top box with a square base must hold $8\ \text{m}^3$. The base material costs $2$ per
square metre and the side material $1$ per square metre. Find the dimensions that minimise the cost,
and the minimum cost.

**24.** Find the point on the parabola $y=x^2$ that is closest to $(0,3)$, and the distance.

**25.** An aircraft flies horizontally at $3$ km altitude and $400$ km/h, passing directly over a
tracking station. How fast is the straight-line distance from the station changing when the aircraft is
$4$ km past the station horizontally? State the sign and its meaning.

**26.** A firm faces demand $p=120-3q$ and total cost $C(q)=30q+500$, with $0\le q\le40$. Find the
profit-maximising quantity and price, verify that marginal revenue equals marginal cost there, and
compare with the endpoints.

**27.** Prove the monotonicity criterion: if $f$ is continuous on $[a,b]$, differentiable on $(a,b)$,
and $f'(x)>0$ for all $x\in(a,b)$, then $f$ is strictly increasing on $[a,b]$.

**28.** Prove that if $f'(x)=0$ for all $x$ in an interval $I$, then $f$ is constant on $I$. Deduce that
if $f'=g'$ on $I$ then $f-g$ is constant.

**29.** Prove that $\lvert\sin a-\sin b\rvert\le\lvert a-b\rvert$ for all real $a,b$, and deduce that
$\sin x<x$ for every $x>0$.

**30.** Evaluate: (a) $\displaystyle\lim_{x\to0^+}x\ln x$;
(b) $\displaystyle\lim_{x\to0}\left(\frac{1}{\sin x}-\frac{1}{x}\right)$.

## Challenge

**31.** Give three counterexamples showing that the hypotheses of Rolle's theorem and of the mean value
theorem cannot be dropped:

(a) a function with $f(a)=f(b)$ that is differentiable on $(a,b)$ but not continuous at an endpoint,
for which no interior critical point exists;

(b) a function continuous on $[-1,1]$ with $f(-1)=f(1)$ that is not differentiable at one interior
point, for which no interior critical point exists;

(c) a function that is differentiable on $(0,1)$ but not continuous at the right endpoint, for which
the conclusion of the mean value theorem fails.

**32.** Prove that if $f$ is differentiable on an interval $(a,b)$ and $f'(x)\ne0$ for every
$x\in(a,b)$, then $f$ has at most one zero in $(a,b)$. Show by example that $f$ need not have any zero.

**33.** Prove that if $f$ is differentiable on an interval $I$ and $f'(x)=f(x)$ for all $x\in I$, then
there is a constant $C$ with $f(x)=Ce^x$ on $I$.

**34.** Apply Newton's method to $f(x)=x^3-2$ starting from $x_0=1$. Compute $x_1,x_2,x_3$ exactly and
as decimals, compare with $\sqrt[3]{2}\approx1.259921$, and verify numerically that the errors roughly
satisfy $e_{n+1}\approx\dfrac{f''(r)}{2f'(r)}e_n^2$ with $r=\sqrt[3]{2}$.

**35.** A pipeline must run from a point $A$ on one bank of a river to a point $B$ on the opposite bank,
$2$ km wide, and $6$ km downstream from the point directly opposite $A$. Laying pipe under the river
costs $5$ units per km, and over land $3$ units per km. Where should the pipeline come ashore to
minimise the cost, and what is the minimum cost? Compare with the two extreme strategies.

**36.** Prove that if $f$ is twice differentiable on an open interval and has three distinct zeros
there, then $f''$ has at least one zero there. Show that the converse fails: give a twice
differentiable function with exactly one zero whose second derivative has a zero.
