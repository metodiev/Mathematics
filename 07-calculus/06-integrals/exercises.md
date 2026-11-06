# Exercises: Integrals

> Companion to the [tutorial](README.md). Solutions are in [solutions.md](solutions.md).

Write the partition and $\Delta x$ explicitly before writing any sum. For every area problem, sketch the
region and find the intersections before integrating. Problems are numbered continuously so that the
solutions file mirrors them exactly.

## Beginner

**1.** Evaluate each sum directly, using the formulas of Section 7.3:

(a) $\displaystyle\sum_{k=1}^{10}(2k+1)$; (b) $\displaystyle\sum_{k=1}^{5}k^2$;
(c) $\displaystyle\sum_{k=1}^{4}(k^3-k)$.

**2.** Express $3+7+11+\cdots+99$ in sigma notation and evaluate the sum.

**3.** Compute $\displaystyle\sum_{k=1}^{n}(4k-1)$ in closed form, and check the result at $n=3$.

**4.** Compute $\displaystyle\sum_{k=1}^{n}(k^2-k)$ in closed form, and check the result at $n=4$.

**5.** For $[0,2]$ with $n=4$ equal subintervals, list the partition points and the midpoints, and compute
the midpoint sum $M_4$ for $f(x)=x^2$.

**6.** For the same interval and the same function, compute $L_4$ and $R_4$, and verify that
$L_4\le\int_0^2x^2\,dx\le R_4$ using the known value $\frac83$.

**7.** Compute $L_3$ and $R_3$ for $f(x)=\dfrac1x$ on $[1,4]$, and say which is larger and why.

**8.** Use the definition of the integral to compute $\displaystyle\int_0^2x\,dx$ from right-endpoint
sums.

**9.** Evaluate, citing the appropriate property of the integral:
(a) $\displaystyle\int_1^3 5\,dx$; (b) $\displaystyle\int_2^2x^3\,dx$.

**10.** Suppose $\displaystyle\int_0^5f=12$, $\displaystyle\int_0^2f=3$ and
$\displaystyle\int_0^5g=7$. Evaluate (a) $\displaystyle\int_2^5f$; (b) $\displaystyle\int_5^0f$;
(c) $\displaystyle\int_0^5(2f-3g)$; (d) $\displaystyle\int_5^2f$.

**11.** Compute the trapezoidal approximation $T_4$ for $f(x)=x$ on $[0,2]$, and explain why it equals
the exact value.

**12.** Estimate $\displaystyle\int_0^1x^3\,dx$ with $T_4$, compute the error, and compare it with the
bound of Theorem 5 using $\lvert f''(x)\rvert\le6$ on $[0,1]$.

## Intermediate

**13.** Compute $\displaystyle\int_0^1(x^2+x)\,dx$ from the definition, using right endpoints.

**14.** Using additivity and the known value $\displaystyle\int_0^bx^2\,dx=\frac{b^3}{3}$, compute
$\displaystyle\int_1^2x^2\,dx$.

**15.** Show from the definition that $\displaystyle\int_{-1}^{1}x^3\,dx=0$, by pairing the contributions
of symmetric subintervals.

**16.** Find the area of the region bounded by $y=x^2$ and $y=x+2$.

**17.** Find the average value of $f(x)=x^3$ on $[0,2]$ and the point $c$ guaranteed by the mean value
theorem for integrals.

**18.** Find the average value of $f(x)=x$ on $[a,b]$ with $a<b$, and the point where it is attained. What
does this say about the midpoint rule for a linear function?

**19.** Compute $T_4$ for $\displaystyle\int_0^2x^2\,dx$, the exact error, and the bound of Theorem 5.
Compare.

**20.** A car's speed is measured every $10$ seconds: $0$, $5$, $12$, $20$ and $25$ m/s at
$t=0,10,20,30,40$ s. Estimate the distance travelled with the trapezoidal rule.

**21.** Water flows into a tank at $r(t)=4-t^2$ litres per minute for $0\le t\le2$. Find the total volume
delivered.

**22.** Without computing them, order the three integrals
$\displaystyle\int_0^1x\,dx$, $\displaystyle\int_0^1x^2\,dx$ and $\displaystyle\int_0^1x^3\,dx$. Then
compute them and confirm the order.

## Advanced

**23.** Prove from the definition that
$\displaystyle\int_a^b\alpha f=\alpha\int_a^bf$ for a constant $\alpha$, treating both $\alpha\ge0$ and
$\alpha<0$.

**24.** Prove from the definition that $\displaystyle\int_a^bf+\int_b^cf=\int_a^cf$ for $a<b<c$.

**25.** Prove from the definition that if $f\le g$ on $[a,b]$, then
$\displaystyle\int_a^bf\le\int_a^bg$.

**26.** Prove that $\left\lvert\displaystyle\int_a^bf\right\rvert\le\displaystyle\int_a^b\lvert f\rvert$,
including the fact that $\lvert f\rvert$ is integrable whenever $f$ is.

**27.** Prove that every increasing function on $[a,b]$ is Riemann integrable, giving the telescoping
estimate for the uniform partition explicitly.

**28.** Explain and prove, using oriented partitions, why
$\displaystyle\int_b^af=-\int_a^bf$ for $a<b$.

**29.** Show that the function $f$ defined by $f(x)=1$ when $x$ is rational and $f(x)=0$ when $x$ is
irrational is not Riemann integrable on $[0,1]$.

**30.** Prove that if $f$ is continuous, $f(x)\ge0$ on $[a,b]$ and $\displaystyle\int_a^bf=0$, then
$f(x)=0$ for every $x\in[a,b]$.

## Challenge

**31.** Compute $\displaystyle\int_0^1x(1-x)\,dx$ from the definition, using right endpoints and the sums
of $k$ and $k^2$.

**32.** Prove that a Riemann integrable function on $[a,b]$ must be bounded.

**33.** Prove that if $f$ is continuous on $[a,b]$ and $\displaystyle\int_a^xf(t)\,dt=0$ for every
$x\in[a,b]$, then $f\equiv0$ on $[a,b]$.

**34.** (a) Show that the trapezoidal rule is exact for every linear function.
(b) For $f(x)=x^2$ on $[0,b]$, show that $T_n=\dfrac{b^3}{3}+\dfrac{b^3}{6n^2}$.
(c) Deduce that the error bound of Theorem 5 holds with equality for this function.

**35.** For $f(x)=x^2$ on $[0,1]$ with the uniform partition into $n$ parts, compute $L_n$, $U_n$ and
$U_n-L_n$ explicitly, and deduce integrability from the Darboux criterion.

**36.** For $f(x)=x^2$ on $[0,b]$, compute the midpoint approximation $M_n$ and compare it with $T_n$.
Explain the signs of the two errors using concavity.
