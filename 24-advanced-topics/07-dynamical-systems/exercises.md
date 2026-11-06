# Dynamical Systems and Chaos — Exercises

> [Dynamical Systems and Chaos](README.md) · 36 problems · Beginner → Challenge · Solutions: [solutions.md](solutions.md)

Work through the problems in order. The section reference in italics says where the necessary material
is proved in the tutorial. Attempt every problem in writing before opening [solutions.md](solutions.md).

**Conventions.** Flows are written $\dot x = f(x)$; maps $x_{n+1} = f(x_n)$; $Df(p)$ is the Jacobian at
$p$; a fixed point is hyperbolic if no eigenvalue of $Df(p)$ has zero real part (flows) or modulus one
(maps). The logistic map is $f_\mu(x) = \mu x(1-x)$ on $[0,1]$; the tent map is
$T(x) = 2x$ for $x\le\frac12$ and $T(x)=2-2x$ for $x>\frac12$; the quadratic family is
$f_c(x) = x^2+c$. Numerical answers to three significant figures unless exact values are requested.

## Beginner

**1.** *(§7.2)* For each one-dimensional flow find all fixed points, determine their stability, and
sketch the flow on the line.

(a) $\dot x = x^2 - 4$
(b) $\dot x = \sin x$
(c) $\dot x = x^3 - x$

**2.** *(§7.1, §7.2)* Solve $\dot x = x(1-x)$ with $x(0) = x_0$, find the fixed points, and verify that
the explicit solution behaves as the linear stability analysis predicts.

**3.** *(§7.2, §8)* Classify the origin for each linear system by computing $\tau = \operatorname{tr}A$,
$\Delta = \det A$ and the eigenvalues.

(a) $A = \begin{pmatrix}-3&0\\0&-1\end{pmatrix}$
(b) $A = \begin{pmatrix}1&0\\0&-1\end{pmatrix}$
(c) $A = \begin{pmatrix}0&1\\-1&0\end{pmatrix}$
(d) $A = \begin{pmatrix}-1&1\\0&-1\end{pmatrix}$

**4.** *(§7.2)* For $\dot x = x - x^3$, $\dot y = -y$, find all fixed points, linearise at each, and
classify. Which conclusions are reliable and which are not?

**5.** *(§7.2)* For the Lotka–Volterra system $\dot x = x(2-y)$, $\dot y = y(x-1)$ with $x,y>0$, find the
fixed points and linearise at each. What does the linearisation fail to decide, and what is the actual
behaviour?

**6.** *(§7.7)* For the logistic map with $\mu = 2$: find the fixed points and their multipliers, and
compute the first four iterates from $x_0 = 0.1$. Where does the orbit end up?

**7.** *(§7.8)* Compute $T^2(x)$ explicitly for the tent map, find all points of period $2$, and verify
that they form one 2-cycle.

**8.** *(§7.5)* Show that $\dot x = -x^3$ is asymptotically stable but not exponentially stable, using
the Lyapunov function $V = x^2$.

**9.** *(§7.2, §7.5)* For $\dot x = -x + y^2$, $\dot y = -y + x^2$: linearise at the origin, then use
$V = x^2 + y^2$ to prove local asymptotic stability. Why is the result only local?

**10.** *(§7.6)* Find the bifurcation value and type for $\dot x = x^2 - 2x + \mu$, and sketch the
bifurcation diagram.

**11.** *(§7.8)* For the doubling map $D(x) = 2x \bmod 1$ on the circle: how many fixed points does
$D^n$ have, and what is the Lyapunov exponent at a typical point?

**12.** *(§7.8)* Compute the Lyapunov exponent of (a) $f(x) = rx$ on $[1,\infty)$ with $r>1$, and
(b) $f(x) = x^2$ on $[2,\infty)$. Explain the difference.

## Intermediate

**13.** *(§7.3, §7.4)* For $\dot x = -2x$, $\dot y = 3y + x^2$: verify that the origin is hyperbolic,
write down $E^s$ and $E^u$, find the stable manifold as an exact graph $y = h(x)$, and state what
Hartman–Grobman does and does not guarantee here.

**14.** *(§7.5)*

(a) Prove that the origin is globally asymptotically stable for $\dot x = y - x^3$, $\dot y = -x - y^3$
using $V = \frac12(x^2+y^2)$.
(b) Explain, with the example $V(x) = x^2/(1+x^2)$ on $\mathbb{R}$, why radial unboundedness is needed
in part 3 of Theorem 7.5.

**15.** *(§7.3, §7.6)* Let $\dot x = f(x,\mu)$ be $C^1$ and suppose $f(p_0,\mu_0)=0$ with $D_xf(p_0,\mu_0)$
hyperbolic. Prove that there are neighbourhoods $U\ni\mu_0$ and $V\ni p_0$ and a $C^1$ curve
$p(\mu)\in V$ of fixed points, and that hyperbolicity persists for $\mu$ near $\mu_0$.

**16.** *(§7.7)* For the quadratic family $f_c(x) = x^2+c$: find the fixed points, show that the
period-2 orbit is $x_\pm = \frac12\left(-1\pm\sqrt{-4c-3}\right)$, compute its multiplier, and deduce
that it is attracting exactly for $-\frac54 < c < -\frac34$.

**17.** *(§7.7)* The logistic bifurcation parameters are $\mu_1 = 3$, $\mu_2 = 3.449490$,
$\mu_3 = 3.544090$, $\mu_4 = 3.564407$, $\mu_5 = 3.568759$. Compute the three ratios
$(\mu_n-\mu_{n-1})/(\mu_{n+1}-\mu_n)$ for $n = 2,3,4$ and compare with $\delta = 4.6692$.

**18.** *(§7.8)* Find all points of period exactly $3$ for the tent map, count them, and check the count
against the formula $2^3 - 2$. How many orbits of exact period $3$ are there?

**19.** *(§7.9)* For the tent map, let $f_0(y) = y/2$ and $f_1(y) = 1-y/2$ be the inverses of the two
branches.

(a) Show that the point whose itinerary is the periodic word $\overline{001}$ satisfies
$x = f_0(f_0(f_1(x)))$, and solve for $x$.
(b) Verify the answer by iterating $T$ three times.

**20.** *(§7.10)* For $\dot r = r(1-r^2)$, $\dot\theta = 1$ in polar coordinates, compute the Poincaré
map $P$ on the ray $\theta = 0$, find its fixed point and derivative there, and interpret.

**21.** *(§7.10)* For the Lorenz system with $\sigma = 10$, $\beta = 8/3$: find the fixed points as
functions of $\rho$, determine the stability of the origin, and compute the Hopf value $\rho_H$.

**22.** *(§7.10)* Explain why a hyperbolic periodic orbit of a planar flow corresponds to a hyperbolic
fixed point of its Poincaré map, and why the Floquet multipliers of the orbit are the eigenvalues of
$DP$ together with the trivial multiplier $1$.

**23.** *(§7.3, §7.4)* Prove that the doubling map $D(x) = 2x \bmod 1$ of the circle is chaotic, and
deduce that transitivity and density of periodic points hold for the tent map (you may use the
semiconjugacy $\sin^2(\pi\theta)$ between $D$ and $f_4$ and the conjugacy between $f_4$ and $T$).

**24.** *(§7.6, §7.8)* Bendixson–Dulac criterion: let $f$ be $C^1$ on a simply connected region
$D\subseteq\mathbb{R}^2$ and suppose $\operatorname{div}f$ has constant sign and is not identically
zero on $D$. Prove that there is no closed orbit lying entirely in $D$. Apply it to
$\dot x = -y + x^3$, $\dot y = x + y^3$ to rule out limit cycles.

## Advanced

**25.** *(§7.5)* Prove part 1 of Theorem 7.5 (Lyapunov stability) in full detail, stating exactly where
continuity and compactness are used.

**26.** *(§7.5)* Prove the LaSalle invariance principle: with $\Omega$ compact and forward invariant,
$V\in C^1$, $\dot V\le0$, every orbit starting in $\Omega$ tends to the largest invariant subset $M$ of
$E = \{\dot V = 0\}$.

**27.** *(§7.2)* Let $A$ have all eigenvalues with negative real part and let $P$ be the symmetric matrix
$P = \int_0^\infty e^{A^{\mathsf T}t}e^{At}dt$. Prove that $P$ is well defined, symmetric, positive
definite and satisfies $A^{\mathsf T}P + PA = -I$. Deduce that $V = x^{\mathsf T}Px$ gives exponential
stability with an explicit rate.

**28.** *(§7.3)* Prove that hyperbolicity of a fixed point is an open condition: if
$\lvert\lambda_j\rvert\ne1$ for all eigenvalues of $Df(p)$, then for every $C^1$ map $g$ sufficiently
close to $f$ in $C^1$ norm, every fixed point near $p$ is hyperbolic.

**29.** *(§7.8, §7.9)* Prove that the shift map $\sigma$ on $\Sigma_2$ is chaotic, and deduce, via the
itinerary map, that the tent map is chaotic.

**30.** *(§7.8)* Prove that the tent map has exactly $2^n$ fixed points of $T^n$, and deduce that the
number of orbits of exact period $n$ is $\frac1n\sum_{d\mid n}\mu(d)2^{n/d}$, where $\mu$ is the Möbius
function.

**31.** *(§7.10)* Let $\gamma$ be a closed orbit of a planar $C^1$ flow and let $\Sigma$ be a transverse
segment through a point of $\gamma$. Prove that the Poincaré map is a local diffeomorphism and that the
periodic orbit is asymptotically stable if and only if the fixed point of $P$ is.

**32.** *(§7.3)* Show that $\dot x = -x$ and $\dot x = -x^3$ are topologically conjugate, but that no
conjugacy between them is $C^1$. What does this say about the sharpness of Hartman–Grobman?

## Challenge

**33.** *(§7.10)* For the Lorenz system prove that the function
$V = \rho x^2 + \sigma y^2 + \sigma(z-2\rho)^2$ satisfies
$\dot V = -2\sigma\rho x^2 - 2\sigma y^2 - 2\sigma\beta(z-\rho)^2 + 2\sigma\beta\rho^2$, and deduce that
every orbit eventually enters a fixed bounded ellipsoid. Conclude that the attractor is compact and has
zero volume.

**34.** *(§7.7)* For $f_c(x) = x^2+c$:

(a) Show that at $c = -\frac74$ the polynomial $f_c^3(x)-x$ has the factor
$\left(8x^3+4x^2-18x-1\right)^2/256$ (together with the fixed-point factor).
(b) Deduce that a period-3 cycle is born in a tangent (saddle-node) bifurcation at $c=-\frac74$, and
find the three points of the cycle numerically.
(c) Explain what happens for $c$ slightly less than $-\frac74$.

**35.** *(§7.8)* Prove that a continuous map $f : I\to I$ of a compact interval with a point of period 3
has points of every period. (Li–Yorke, special case.) Suggested route: from a 3-cycle
$x_1<x_2<x_3$ with $f(x_1)=x_2$, $f(x_2)=x_3$, $f(x_3)=x_1$, construct closed intervals
$I_1 = [x_1,x_2]$ and $I_2 = [x_2,x_3]$ with $f(I_1)\supseteq I_2$ and $f(I_2)\supseteq I_1\cup I_2$;
then use the covering lemma: if $J_0,\dots,J_{n-1}$ are closed intervals with
$f(J_k)\supseteq J_{k+1}$ and $f(J_{n-1})\supseteq J_0$, there is a point $x$ with $f^k(x)\in J_k$ and
$f^n(x) = x$.

**36.** *(§7.7, §7.8)* Prove that $h(x) = \sin^2(\pi x/2)$ conjugates the tent map $T$ to
$f_4(x) = 4x(1-x)$, deduce that $f_4$ is chaotic, and compute its Lyapunov exponent. Explain why the
conjugacy is not $C^1$ at the endpoints, and why that does not affect either conclusion.
