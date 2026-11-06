# Systems of ODEs — Exercises

> [Systems of ODEs](README.md) · 36 problems · Beginner → Challenge · Solutions: [solutions.md](solutions.md)

Work through the problems in order; each cites the section of the tutorial it draws on. Problems 1–12
build fluency with conversion, eigenpairs, the matrix exponential and the trace–determinant
classification; 13–23 apply the three eigenvalue cases and analyse the model systems; 24–31 are proofs;
32–36 are challenge problems. Attempt every problem before opening [solutions.md](solutions.md), and
finish each one by **substituting the answer back** into the system or checking the hypotheses of the
theorem you used.

Conventions: primes denote $d/dt$, vectors are columns, and $\tau = \operatorname{tr}A$,
$\delta = \det A$, $\Delta = \tau^2 - 4\delta$ for a $2\times2$ matrix $A$. All matrices are real.

## Beginner

**1.** *(§7.1)* Write $y'' + 3y' + 2y = 0$ as a first-order system $\mathbf{x}' = A\mathbf{x}$. Give $A$, its eigenvalues, and the characteristic roots of the original equation. Why do they agree?

**2.** *(§7.1)* Write $y''' - y = 0$ as a first-order system and give the companion matrix $A$. Compute $\det(A - \lambda I)$ and hence the eigenvalues.

**3.** *(§7.1)* Write $y'' + 4y = \cos t$ as a first-order system in normal form, stating the matrix $A$ and the vector $\mathbf{b}(t)$.

**4.** *(§7.4)* Find the eigenvalues and eigenvectors of $A = \begin{pmatrix}1&3\\2&2\end{pmatrix}$ and write the general solution of $\mathbf{x}' = A\mathbf{x}$.

**5.** *(§7.4)* Using the matrix of Problem 4, solve the initial value problem with $\mathbf{x}(0) = (5,0)^{\mathsf T}$.

**6.** *(§7.4, §7.5)* Solve $\mathbf{x}' = \begin{pmatrix}2&0\\0&-3\end{pmatrix}\mathbf{x}$ with $\mathbf{x}(0) = (1,4)^{\mathsf T}$ and classify the equilibrium.

**7.** *(§7.3)* Compute $e^{At}$ for $A = \begin{pmatrix}0&1\\0&0\end{pmatrix}$ by summing the series. Describe the orbits of $\mathbf{x}' = A\mathbf{x}$.

**8.** *(§7.3, §7.5)* Solve $\mathbf{x}' = \begin{pmatrix}0&1\\-1&0\end{pmatrix}\mathbf{x}$ with $\mathbf{x}(0) = (1,0)^{\mathsf T}$, and identify the type of equilibrium and the sense of rotation.

**9.** *(§7.5)* For each matrix, compute $\tau$ and $\delta$, then classify the equilibrium and state its stability:
(a) $\begin{pmatrix}-1&0\\0&-2\end{pmatrix}$;
(b) $\begin{pmatrix}1&0\\0&2\end{pmatrix}$;
(c) $\begin{pmatrix}0&1\\1&0\end{pmatrix}$;
(d) $\begin{pmatrix}0&-1\\1&0\end{pmatrix}$;
(e) $\begin{pmatrix}1&-1\\1&1\end{pmatrix}$.

**10.** *(§7.5)* For $A = \begin{pmatrix}-2&1\\0&-3\end{pmatrix}$ find the eigenvalues and eigenvectors, write the general solution, and describe the phase portrait. Which eigendirection do the orbits approach at the origin?

**11.** *(§7.5)* Find the equilibrium of the affine system
$$x' = x - y + 1, \qquad y' = 2x + 4,$$
shift the equilibrium to the origin, and classify it.

**12.** *(§7.2, §7.8)* Solve $\mathbf{x}' = \begin{pmatrix}0&1\\-1&0\end{pmatrix}\mathbf{x} + \binom{0}{1}$ with $\mathbf{x}(0) = \mathbf{0}$, by converting it to a second-order equation for $x_1$.

## Intermediate

**13.** *(§7.4)* Solve $\mathbf{x}' = \begin{pmatrix}1&-2\\2&1\end{pmatrix}\mathbf{x}$ with $\mathbf{x}(0) = (1,0)^{\mathsf T}$. Give the solution in real form and describe the orbit in polar coordinates.

**14.** *(§7.4)* Solve $\mathbf{x}' = \begin{pmatrix}1&2\\0&1\end{pmatrix}\mathbf{x}$ with $\mathbf{x}(0) = (1,2)^{\mathsf T}$, using a generalised eigenvector. Find $e^{At}$ as well.

**15.** *(§7.3)* Compute $e^{At}$ for $A = \begin{pmatrix}1&1\\0&2\end{pmatrix}$ by diagonalising $A$, and verify the result at $t = 0$ and by differentiating.

**16.** *(§7.3, §7.4)* Compute $e^{At}$ for $A = \begin{pmatrix}1&1&0\\0&1&0\\0&0&-2\end{pmatrix}$ and solve $\mathbf{x}' = A\mathbf{x}$ with $\mathbf{x}(0) = (0,1,1)^{\mathsf T}$. Why does the block structure simplify the computation?

**17.** *(§7.2, §7.4)* Solve $\mathbf{x}' = \begin{pmatrix}1&0\\0&2\end{pmatrix}\mathbf{x} + \binom{e^{2t}}{e^{2t}}$ with $\mathbf{x}(0) = \mathbf{0}$.

**18.** *(§7.6, §7.8)* Solve $\mathbf{x}' = \begin{pmatrix}0&1\\-1&0\end{pmatrix}\mathbf{x} + \binom{0}{\sin t}$ with $\mathbf{x}(0) = \mathbf{0}$, using variation of constants. Why is the amplitude growing?

**19.** *(§7.7, §7.8)* A pendulum of length $L = 2\ \mathrm{m}$ with $g = 9.81\ \mathrm{m/s^2}$ and damping $b = 0.4\ \mathrm{s^{-1}}$ obeys $\theta'' + b\theta' + (g/L)\sin\theta = 0$. Linearise at $(\theta,\omega) = (0,0)$ and at $(\pi,0)$; classify both; compute the period of small oscillations at the bottom and the decay time.

**20.** *(§7.7, §7.8)* For the predator–prey system
$$x' = x(3 - 2y), \qquad y' = y(x - 1),$$
find the positive equilibrium, linearise there, find the angular frequency of the linearised oscillation, and state what the linearisation alone does and does not prove.

**21.** *(§7.7, §7.8)* For the competing-species system
$$x' = x(3 - 2x - y), \qquad y' = y(2 - x - 2y),$$
find all four equilibria in the closed first quadrant, classify each, and interpret the result ecologically. Which species wins, if either?

**22.** *(§7.6)* Use $V(x,y) = x^2 + y^2$ to prove that the origin is asymptotically stable for
$$x' = -x + 2y, \qquad y' = -2x - y.$$
State exactly which theorem you are applying.

**23.** *(§7.6)* Consider $x' = y$, $y' = -x - y^3$. Show that $V = \frac12(x^2 + y^2)$ satisfies $\dot V \le 0$, and use LaSalle's invariance principle to prove that the origin is asymptotically stable.

## Advanced

**24.** *(§7.3)* Prove from the series definition that $\dfrac{d}{dt}e^{At} = Ae^{At}$ for every real $t$, justifying the term-by-term differentiation.

**25.** *(§7.3)* Prove that $e^{A(t+s)} = e^{At}e^{As}$ for all $s,t$, and deduce that $e^{At}$ is invertible for every $t$ with inverse $e^{-At}$. Where exactly is absolute convergence used?

**26.** *(§7.3)* Let $A = \begin{pmatrix}0&1\\0&0\end{pmatrix}$ and $B = \begin{pmatrix}0&0\\1&0\end{pmatrix}$. Compute $e^{A}$, $e^{B}$, $e^{A+B}$ and $e^{A}e^{B}$, and conclude that $e^{A+B} = e^{A}e^{B}$ fails when $AB\ne BA$. Which hypothesis of Theorem 7.9(3) is violated?

**27.** *(§7.3, §8.3)* Prove that $\det e^{At} = e^{t\operatorname{tr}A}$ in two ways: (a) by triangularising $A$ over $\mathbb{C}$; (b) by applying Abel's formula to $\Phi(t) = e^{At}$.

**28.** *(§7.6)* Suppose every eigenvalue of $A$ has negative real part. Prove that there are constants $C>0$ and $\mu>0$ with
$$\left\lVert e^{At}\mathbf{x}_0\right\rVert \le Ce^{-\mu t}\left\lVert\mathbf{x}_0\right\rVert \qquad (t\ge0),$$
and deduce asymptotic stability of the origin without invoking Theorem 7.13.

**29.** *(§7.5)* Prove that the planar linear system $\mathbf{x}' = A\mathbf{x}$ has a nonconstant periodic solution if and only if $\tau = 0$ and $\delta>0$. (You may use the classification of §7.5.)

**30.** *(§7.6)* Prove part 1 of the Lyapunov stability theorem in full detail: if $V$ is continuously differentiable, $V(\mathbf{0}) = 0$, $V>0$ off $\mathbf{0}$, and $\dot V\le0$, then $\mathbf{0}$ is Lyapunov stable.

**31.** *(§7.5, §7.7)* Let $A$ have eigenvalues $\lambda_1<0<\lambda_2$ (a saddle). Prove that the only orbits that stay bounded as $t\to+\infty$ are those on the stable eigenline, that the only orbits that stay bounded as $t\to-\infty$ are those on the unstable eigenline, and that every other orbit is unbounded both as $t\to+\infty$ and as $t\to-\infty$ in at least one coordinate.

## Challenge

**32.** *(§7.4)* For the $3\times3$ matrix $A = \begin{pmatrix}-1&1&0\\0&-1&1\\0&0&-1\end{pmatrix}$, compute $e^{At}$. Then prove that for an $m\times m$ Jordan block $J = \lambda I + N$ with $N$ the shift matrix,
$$e^{Jt} = e^{\lambda t}\sum_{k=0}^{m-1}\frac{t^k}{k!}N^k .$$

**33.** *(§7.8)* For the competition model of Problem 21, prove that the interior equilibrium is a stable node, that the two axial equilibria are saddles, and that **no** periodic orbit exists in the open first quadrant. Then use the Poincaré–Bendixson theorem to conclude that every orbit with $x_0>0$, $y_0>0$ converges to the interior equilibrium. *(Bendixson–Dulac criterion, which you may use: if $B(x,y)$ is $C^1$ and $\dfrac{\partial(Bf_1)}{\partial x} + \dfrac{\partial(Bf_2)}{\partial y}$ has one constant sign in a simply connected region, then the system has no periodic orbit there.)* Try $B = 1/(xy)$.

**34.** *(§7.2)* Let $A(t) = \begin{pmatrix}1&t\\0&2\end{pmatrix}$. (a) Compute the fundamental matrix $\Phi(t)$ with $\Phi(0) = I$. (b) Compute $\exp\left(\int_0^t A(s)\,ds\right)$ and show that it is **not** a fundamental matrix. (c) Which hypothesis of Theorem 7.9(3) fails here, and why does that matter?

**35.** *(§7.6)* Prove: if every solution of $\mathbf{x}' = A\mathbf{x}$ is bounded on the whole line $\mathbb{R}$, then $A$ is diagonalisable over $\mathbb{C}$ and every eigenvalue has real part zero. Show by example that "bounded on $[0,\infty)$" is a strictly weaker hypothesis, and say exactly where the proof uses $t\to-\infty$.

**36.** *(§7.7)* Consider
$$x' = -y + x(x^2 + y^2), \qquad y' = x + y(x^2 + y^2).$$
(a) Show that in polar coordinates $r' = r^3$, $\theta' = 1$. (b) Show that the linearisation at the origin has eigenvalues $\pm i$ and is therefore a centre. (c) Solve the nonlinear system and show that the origin is an unstable spiral. (d) What does this example say about the role of the hyperbolicity hypothesis in the Hartman–Grobman theorem?
