# Interpolation and Approximation — Exercises

> [Interpolation and Approximation](README.md) · 36 problems · Beginner → Challenge · Solutions: [solutions.md](solutions.md)

Every problem refers to the section of the [tutorial](README.md) that supplies the method. Unless a
problem says otherwise, all arithmetic is exact or is to be carried to six significant figures; when a
problem asks for a bound, the bound must follow from the stated theorem, not from a comparison with the
true value. Do not open [solutions.md](solutions.md) before writing an attempt.

Notation: $p_n$ is the interpolant in $\Pi_n$, $\omega(x)=\prod_i(x-x_i)$, $\ell_i$ are the Lagrange
basis polynomials, $M_i=S''(x_i)$ are the spline moments, and $L_n$ is the interpolation operator.

## Beginner

**1.** *(§7.2)* Find the polynomial $p\in\Pi_2$ through $(0,2)$, $(1,3)$, $(3,1)$ using the Lagrange
form. Expand it, and verify that $p$ takes the three prescribed values.

**2.** *(§7.2)* For the nodes $0,1,2$, write down $\ell_0,\ell_1,\ell_2$ explicitly and verify the
identities $\sum_i\ell_i(x)=1$ and $\sum_i x_i\ell_i(x)=x$ at $x=3$.

**3.** *(§7.3)* Build the divided-difference table for the data $(1,1)$, $(2,4)$, $(4,16)$, write the
Newton form, and show that it reduces to $x^2$. Explain what the next divided difference of $x^2$ would
be and why.

**4.** *(§7.3)* Find the polynomial of degree at most $2$ with $p(0)=1$, $p(1)=0$, $p(2)=3$, using
Newton's form. Check the result at all three nodes.

**5.** *(§7.4)* Bound the error of linear interpolation of $f(x)=\ln x$ on $[1,2]$ at the interpolation
nodes $1$ and $2$. Then find the point where the actual error is largest and its value.

**6.** *(§7.9)* Hermite interpolation is applied at four distinct nodes, with values and first
derivatives prescribed at each. How many conditions are imposed, what is the degree of the resulting
polynomial, and what is the correct error term? Justify the count.

**7.** *(§7.7)* Interpolate $f(x)=e^x$ on $[0,1]$ piecewise linearly with knots $0,\tfrac12,1$. State the
theorem that bounds the error, compute the bound, and compute the actual maximum error on each of the two
panels. On which panel is it larger, and why?

**8.** *(§7.5)* For $n=2$ (three nodes) on $[-1,1]$, compute the Chebyshev nodes, write the node
polynomial, and verify that its maximum modulus equals $2^{-n}$. Compare with the three equispaced nodes
$-1,0,1$.

**9.** *(§7.9)* Construct the cubic Hermite interpolant with $H(0)=1$, $H'(0)=0$, $H(1)=2$, $H'(1)=1$.
Verify all four conditions and state the error term that would apply if the data came from a function
$f\in C^4$.

**10.** *(§7.8)* Construct the natural cubic spline through $(0,0)$, $(1,1)$, $(2,0)$. Write both cubic
pieces, verify interpolation and the $C^2$ conditions, and compute $\int_0^2(S'')^2dx$.

**11.** *(§7.10)* Fit the line $b=c_1+c_2t$ to the data $(0,0)$, $(1,1)$, $(2,3)$, $(3,4)$ by least
squares. Write the normal equations, solve them, and compute the residual sum of squares.

**12.** *(§7.12)* Compute the DFT of $y=(2,0,2,0)$ with $N=4$. Write the trigonometric interpolant and
verify that it reproduces all four data values. Which real function does it equal on the grid?

## Intermediate

**13.** *(§7.3, §7.4)* Interpolate $f(x)=1/x$ at $1,2,3,4$ in Newton form. Evaluate the result at
$x=2.5$ and compare with $0.4$. Bound the error on $[1,4]$ using $f^{(4)}(x)=24/x^5$.

**14.** *(§7.4)* Interpolate $\cos x$ linearly at the endpoints of $[0,\pi/4]$. Bound the error, then
find the point where the actual error is maximal and its value. Is the bound sharp?

**15.** *(§7.5, §7.6)* Interpolate $f(x)=e^{-x}$ on $[-1,1]$ at five nodes, once equispaced and once
Chebyshev. Compute $\max\lvert\omega\rvert$ for both choices, the two error bounds, and the two actual
maximum errors (a fine grid is acceptable). Which is better and by what factor?

**16.** *(§7.2)* Prove that $\sum_i\ell_i(x)=1$ for every $x$, and deduce that the Lebesgue constant
satisfies $\Lambda_n\ge1$ for every choice of nodes. When is $\Lambda_n=1$?

**17.** *(§7.7)* For $f(x)=\sin x$ on $[0,\pi]$, how many equal panels are needed so that the piecewise
linear error bound is at most $10^{-4}$? Give the smallest admissible number and the resulting bound.

**18.** *(§7.8)* Construct the natural cubic spline through $(0,0)$, $(1,1)$, $(2,0)$, $(3,0)$ with
$h_i=1$. Solve the moment system exactly in fractions, write all three pieces, and verify $C^2$
continuity at $x=1$ and $x=2$.

**19.** *(§7.9)* Construct the cubic Hermite interpolant of $f(x)=\ln x$ at $1$ and $2$. Evaluate it at
$x=1.5$, compare with $\ln 1.5$, and check the error against the Hermite bound.

**20.** *(§7.10)* Fit $b=c_1+c_2x+c_3x^2$ to $(0,1)$, $(1,3)$, $(2,4)$, $(3,7)$ by least squares. Write
the normal equations, solve them, and compute the residual sum of squares. Verify that the residual is
orthogonal to all three columns of $A$.

**21.** *(§7.11)* Find the best $L^2$ linear approximation to $e^x$ on $[-1,1]$ using $P_0$ and $P_1$.
Compute $\lVert e^x-p^\ast\rVert_2$ and check it against the error formula.

**22.** *(§7.11)* Find the best $L^2$ linear approximation to $x^2$ on $[-1,1]$ and its squared error.
Explain why the linear coefficient vanishes.

**23.** *(§7.12)* Compute the DFT of $y=(1,2,3,4)$ with $N=4$, then recover $y$ from the coefficients
using the inverse formula. Verify that the coefficients satisfy $c_{N-k}=\overline{c_k}$.

**24.** *(§7.13)* Compute the Lebesgue constant for the three equispaced nodes $-1,0,1$ by maximising
$\lvert\ell_0\rvert+\lvert\ell_1\rvert+\lvert\ell_2\rvert$ explicitly. Show that the maximum is $5/4$,
and identify where it is attained.

## Advanced

**25.** *(§7.1)* Prove that $\det V=\prod_{0\le i<j\le n}(x_j-x_i)$ for the Vandermonde matrix, and
deduce that the interpolation problem with distinct nodes has exactly one solution for every right-hand
side.

**26.** *(§7.4)* Prove the interpolation error formula: if $f\in C^{n+1}[a,b]$ and $p_n$ interpolates $f$
at distinct $x_0,\dots,x_n$, then for each $x$ there is $\xi$ in the hull of $x,x_0,\dots,x_n$ with
$f(x)-p_n(x)=\frac{f^{(n+1)}(\xi)}{(n+1)!}\omega(x)$.

**27.** *(§7.5)* Prove the Chebyshev minimax theorem: among monic polynomials of degree $m$, the minimum
of $\max_{[-1,1]}\lvert q\rvert$ is $2^{1-m}$, attained only by $2^{1-m}T_m$.

**28.** *(§7.3)* Prove that divided differences are symmetric in their nodes, and use this to prove the
Newton interpolation formula. State clearly where each hypothesis is used.

**29.** *(§7.8)* Derive the tridiagonal moment system for the natural cubic spline, and prove that it is
nonsingular. Deduce that the natural cubic spline through any data is unique.

**30.** *(§7.10)* Derive the normal equations $A^{\mathsf T}Ac=A^{\mathsf T}b$ in two ways — by
differentiating $\Phi$, and by orthogonality of the residual — and prove that the minimiser is unique
exactly when the columns of $A$ are linearly independent.

**31.** *(§7.11)* Prove that $p^\ast=\sum_{k=0}^{n}c_kP_k$ with $c_k=\langle f,P_k\rangle/\langle P_k,P_k\rangle$
minimises $\lVert f-q\rVert_2$ over $q\in\Pi_n$, and prove the error formula
$\lVert f-p^\ast\rVert_2^2=\lVert f\rVert_2^2-\sum_kc_k^2\lVert P_k\rVert_2^2$.

## Challenge

**32.** *(§7.6)* Numerically study Runge's function $f(x)=1/(1+25x^2)$ on $[-1,1]$. For
$n=4,8,12,16$, compute the maximum interpolation error over a fine grid for equispaced and for Chebyshev
nodes, and the error at $x=0.95$. Estimate the factor by which the equispaced error grows when $n$
increases by $4$, and the factor by which the Chebyshev error decays. Explain both factors using the
error formula and the pole locations $\pm i/5$.

**33.** *(§7.12)* Prove that for $N$ even and $x_j=2\pi j/N$, $\cos(kx_j)=\cos((N-k)x_j)$ and
$\sin(kx_j)=-\sin((N-k)x_j)$ for every integer $k$. Deduce that $N$ real samples determine a real
trigonometric polynomial of degree at most $N/2$, and explain why they cannot determine one of higher
degree.

**34.** *(§7.5, §7.11)* Prove that the best uniform (minimax) linear approximation to $\lvert x\rvert$ on
$[-1,1]$ is the constant $\tfrac12$, and that its maximum error is $\tfrac12$. Compare with the best
$L^2$ linear approximation and its error.

**35.** *(§7.2)* Derive the barycentric interpolation formula from the Lagrange formula. Compute the
barycentric weights for the nodes $0,1,2,3$, use them to evaluate the interpolant of the data
$(0,1,4,9)$ at $x=1.5$, and explain why the formula is numerically more stable than expanding the
monomial coefficients.

**36.** *(§7.3)* Prove that if $f$ is a polynomial of degree $n$ with leading coefficient $a_n$, then
$f[x_0,\dots,x_n]=a_n$ for any $n+1$ distinct nodes, and that every divided difference of order $n+1$
vanishes. Use this to explain why interpolating a cubic at five distinct points produces a zero fourth
divided difference, and what this implies for the Newton form.
