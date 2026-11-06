# Numerical Integration — Exercises

> [Numerical Integration](README.md) · 36 problems · Beginner → Challenge · Solutions: [solutions.md](solutions.md)

Every problem refers to the section of the [tutorial](README.md) that supplies the method. The error of a
rule always means $I-Q$, exact minus computed, as in Definition 5.1. When a problem asks for a bound, the
bound must follow from the stated theorem. Do not open [solutions.md](solutions.md) before writing an
attempt.

Notation: $T$, $M$, $S$ are the one-panel trapezoid, midpoint and Simpson rules; $T_m$, $S_m$ are the
composite rules with $m$ subintervals of length $h$; $Q_n$ is the $n$-point Gauss–Legendre rule on
$[-1,1]$; $R_{k,j}$ are the Romberg entries.

## Beginner

**1.** *(§7.2)* Compute the trapezoid rule for $\int_0^1x^2dx$ with one panel and with two panels. In
each case compute the error and compare it with the bound of Theorem 7.1. Why is the bound attained
exactly?

**2.** *(§7.3)* Apply Simpson's rule to $\int_0^2x^3dx$ and verify that the result is exact. Then apply it
to $\int_0^2x^2dx$ and check the result against the exact value.

**3.** *(§7.4)* Apply the midpoint rule to $\int_0^1e^{-x}dx$. Compute the error and check it against the
bound of Theorem 7.3. Does the rule over- or underestimate?

**4.** *(§7.1)* Derive the trapezoid weights $w_0=w_1=(b-a)/2$ by integrating the two Lagrange basis
polynomials on $[a,b]$.

**5.** *(§7.1)* Derive Simpson's weights for the nodes $0,\tfrac12,1$ by integrating the three Lagrange
basis polynomials. Verify that the weights sum to the length of the interval.

**6.** *(§7.4)* Determine the degree of exactness of the trapezoid rule. Verify that it is exact for
$1$ and $x$ and compute its error for $x^2$ on $[0,1]$; compare with the error term.

**7.** *(§7.5)* Compute the composite trapezoid rule with $m=4$ for $\int_0^1\frac{dx}{1+x}=\ln2$.
Compute the error, the bound of Theorem 7.4, and check the sign.

**8.** *(§7.5)* Compute the composite Simpson rule with $m=4$ for the same integral. Compute the error and
the bound, and compare with the trapezoid result of Problem 7.

**9.** *(§7.7)* Verify that the two-point Gauss rule with nodes $\pm1/\sqrt3$ and weights $1,1$ satisfies
the four moment equations for degrees $0,1,2,3$. Show that it fails for degree $4$.

**10.** *(§7.6)* For $\int_0^1\frac{4}{1+x^2}dx$ the trapezoid values are $T(1)=3.0$ and $T(0.5)=3.1$.
Compute the first Romberg extrapolation and compare with $\pi$.

**11.** *(§7.5)* For $\int_0^1\frac{dx}{1+x}$ we have $T_4=0.697024$ and $T_8=0.694122$. Use Richardson
extrapolation with the known order $2$ to estimate the integral, and compare with $\ln2$.

**12.** *(§7.9)* For $\int_0^1\sqrt x\,dx$ the one-panel and two-panel Simpson values are $S_1=0.638071$
and $S_2=0.656526$. Compute the local error estimate and the corrected value, and decide whether a
tolerance of $10^{-2}$ would accept the panel.

## Intermediate

**13.** *(§7.5)* Compute the composite Simpson rule with $m=6$ for $\int_0^\pi\sin x\,dx=2$. Compute the
error and the bound of Theorem 7.4, and comment on their ratio.

**14.** *(§7.5)* Using the bound for the composite trapezoid rule, find the smallest number of panels
that guarantees an error below $10^{-6}$ for $\int_0^1e^xdx$.

**15.** *(§7.5)* Repeat Problem 14 for composite Simpson. Compare the two answers and the work required.

**16.** *(§7.6)* Build the Romberg tableau for $\int_0^1e^xdx$ with $k=0,1,2$ (three rows) and compare the
diagonal entries with $e-1$.

**17.** *(§7.4)* Derive the weights of Simpson's $3/8$ rule on $[0,3]$ and verify the rule on $x^3$
(exact) and on $x^4$ (compute the error and compare with $-\frac{3h^5}{80}f^{(4)}$).

**18.** *(§7.4)* Derive Boole's weights on $[0,4]$ and verify the rule on $x^5$ (exact) and on $x^6$
(compute the error and compare with $-\frac{8h^7}{945}f^{(6)}$).

**19.** *(§7.8)* Apply the three-point Gauss rule to $\int_{-1}^1x^6dx$. Compute the error and confirm
that the rule is exact through degree $5$ but not degree $6$.

**20.** *(§7.7)* Apply the two-point Gauss rule on $[-1,1]$, transformed to $[0,1]$, to
$\int_0^1\sqrt x\,dx$. Compute the error and compare it with Simpson's rule on the same interval.

**21.** *(§7.10)* Compare four rules on $\int_0^1\frac{4}{1+x^2}dx=\pi$: composite trapezoid with $m=4$,
composite Simpson with $m=4$, two-panel Gauss–2, and one-panel Gauss–3. Tabulate evaluations and errors,
and rank the methods by accuracy per evaluation.

**22.** *(§7.9)* Apply adaptive Simpson to $\int_0^1e^{-x^2}dx$ with tolerance $10^{-8}$. Report the
value, the number of panels, and the error against $\frac{\sqrt\pi}{2}\operatorname{erf}(1)$.

**23.** *(§7.2)* Prove from the error terms that the trapezoid rule overestimates a convex integrand and
the midpoint rule underestimates it. What can be said for a concave integrand?

**24.** *(§7.5)* Derive the composite Simpson error term by summing the panel errors and applying the
intermediate value theorem. State the hypotheses precisely.

## Advanced

**25.** *(§7.2)* Prove the trapezoid error theorem: for $f\in C^2[a,b]$ there is $\eta\in(a,b)$ with
$I-T=-\frac{(b-a)^3}{12}f''(\eta)$.

**26.** *(§7.3)* Prove the Simpson error theorem using cubic Hermite interpolation. In particular, prove
that Simpson's rule equals the integral of the Hermite cubic that matches $f$ at $a,m,b$ and $f'$ at $m$.

**27.** *(§7.1)* Prove that the interpolatory weights satisfy $\sum_iw_i=b-a$, that the rule has degree of
exactness at least $n$, and that its error equals the integral of the interpolation error.

**28.** *(§7.8)* State and prove the Gauss exactness theorem, including the proof that no $n$-point rule
has degree of exactness greater than $2n-1$.

**29.** *(§7.7)* Derive the two-point Gauss rule from the four moment equations without assuming symmetry
in advance, and prove that no two-point rule can have degree of exactness $4$.

**30.** *(§7.6)* Prove that the Romberg recursion cancels the $h^{2j}$ term, that is
$R_{k,j}=I+O(h_k^{2j+2})$ whenever the Euler–Maclaurin expansion is valid to that order.

**31.** *(§7.4)* Using the Peano kernel $K(t)=E[(x-t)_+^3]$, derive the error constant $-\frac{3h^5}{80}$
of Simpson's $3/8$ rule on an interval of length $3h$. Verify that the kernel has one sign.

## Challenge

**32.** *(§7.5)* Prove that composite Simpson converges as $O(h^4)$ for $f\in C^4$, and show that the
constant is sharp by computing the exact error for $f(x)=x^4$ on $[0,1]$ with $m$ panels.

**33.** *(§7.8)* Derive the two-point Gauss error constant on $[-1,1]$ from the Peano kernel, proving that
$K(t)\ge0$ and that $E[f]=f^{(4)}(\xi)/135$.

**34.** *(§7.9)* Derive the adaptive Simpson error estimate $I-S_2\approx(S_2-S_1)/15$ from the $h^4$
scaling of the Simpson error, and show that the corrected value $S_2+(S_2-S_1)/15$ has local error
$O(h^6)$.

**35.** *(§7.6)* Derive the leading term of the Euler–Maclaurin expansion for the trapezoid rule by
integration by parts on a single panel, and verify the resulting $h^2$ coefficient numerically for
$\int_0^1e^xdx$.

**36.** *(§7.11)* Using a substitution and a Gauss–Legendre rule, compute $\int_0^\infty e^{-x^2}dx$ to
an accuracy of $10^{-8}$. Report the transformation used, the values for two successive $n$, and the
error against $\sqrt\pi/2$.
