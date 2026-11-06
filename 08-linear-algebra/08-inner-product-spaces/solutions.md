# Inner Product Spaces — Solutions

> [Tutorial](README.md) · [Exercises](exercises.md)

Each solution gives the strategy, the computation with every step, and a check. Proofs are complete; the
axiom or theorem used is named at each step.

## Beginner

**1.** *Answer:* $\langle\mathbf{u},\mathbf{v}\rangle = 11$, $\lVert\mathbf{u}\rVert = 5$,
$\lVert\mathbf{v}\rVert = 3$, $\cos\theta = \tfrac{11}{15}$, so $\theta \approx 42.8^\circ$.

$$
\langle\mathbf{u},\mathbf{v}\rangle = 3\cdot1 + 4\cdot2 + 0\cdot2 = 11,
\qquad
\lVert\mathbf{u}\rVert = \sqrt{9+16+0} = 5,
\qquad
\lVert\mathbf{v}\rVert = \sqrt{1+4+4} = 3 .
$$

Since $\cos\theta = \frac{\langle\mathbf{u},\mathbf{v}\rangle}{\lVert\mathbf{u}\rVert\lVert\mathbf{v}\rVert} = \frac{11}{15} \approx 0.7333$,
$\theta = \arccos(0.7333) \approx 42.8^\circ$. Cauchy–Schwarz requires
$11 \le 5\cdot3 = 15$ ✓, and the inequality is strict because the vectors are not parallel.

**2.** *Answer:* $\langle\mathbf{u},\mathbf{v}\rangle = -4$, $\lVert\mathbf{u}\rVert = \lVert\mathbf{v}\rVert = 3$,
$\lVert\mathbf{u}+\mathbf{v}\rVert = \sqrt{10} \approx 3.162$.

$$
\langle\mathbf{u},\mathbf{v}\rangle = 1\cdot2 + (-2)\cdot1 + 2\cdot(-2) = 2 - 2 - 4 = -4,
$$

$$
\lVert\mathbf{u}\rVert = \sqrt{1+4+4} = 3, \qquad \lVert\mathbf{v}\rVert = \sqrt{4+1+4} = 3 .
$$

Cauchy–Schwarz: $\lvert -4\rvert = 4 \le 9$ ✓. Since $\langle\mathbf{u},\mathbf{v}\rangle < 0$ the angle is
obtuse. For the triangle inequality, $\mathbf{u}+\mathbf{v} = (3,-1,0)$ so
$\lVert\mathbf{u}+\mathbf{v}\rVert = \sqrt{10} \approx 3.162 \le 3+3 = 6$ ✓.

*Remark.* The bound is far from tight here, as it must be when the vectors are nearly orthogonal
($\cos\theta = -4/9$).

**3.** *Answer:* (a) orthogonal; (b) orthogonal; (c) not orthogonal; (d) orthogonal.

(a) $1\cdot2 + 2\cdot(-1) + 3\cdot0 = 2 - 2 + 0 = 0$ ✓.
(b) $1\cdot1 + 1\cdot(-1) + 0\cdot1 = 0$ ✓.
(c) $1\cdot2 + 2\cdot1 = 4 \neq 0$ ✗ — the two vectors make an acute angle.
(d) With the convention $\langle\mathbf{z},\mathbf{w}\rangle = \sum z_j\overline{w_j}$,

$$
\langle(1,i),(i,1)\rangle = 1\cdot\overline{i} + i\cdot\overline{1} = -i + i = 0 ✓ .
$$

*Warning:* with the other convention (conjugate in the first slot) the answer is the same here, but the
intermediate value is $\overline{0} = 0$; the two conventions never disagree about *whether* an inner
product vanishes.

**4.** *Answer:* (a) $(3,4)/5 = (0.6,0.8)$; (b) $(1,1,1)/\sqrt3$; (c) $(1,-2,2)/3$; (d) $(1,i)/\sqrt2$.

Divide each vector by its norm.

(a) $\lVert(3,4)\rVert = \sqrt{9+16} = 5$.
(b) $\lVert(1,1,1)\rVert = \sqrt3$.
(c) $\lVert(1,-2,2)\rVert = \sqrt{1+4+4} = 3$.
(d) $\lVert(1,i)\rVert = \sqrt{1\cdot\bar1 + i\bar i} = \sqrt{1 + \lvert i\rvert^2} = \sqrt2$.

*Check:* each result has norm $1$; for instance $\lVert(1,i)/\sqrt2\rVert^2 = (1+1)/2 = 1$ ✓.

**5.** *Answer:* $d(\mathbf{u},\mathbf{v}) = \sqrt2$, $d(\mathbf{u},\mathbf{w}) = d(\mathbf{w},\mathbf{v}) = 1$,
and $\sqrt2 \le 2$ ✓.

$$
\mathbf{u}-\mathbf{v} = (1,-1,0) \Rightarrow d(\mathbf{u},\mathbf{v}) = \sqrt2 \approx 1.414,
$$
$$
\mathbf{u}-\mathbf{w} = (0,-1,0) \Rightarrow d(\mathbf{u},\mathbf{w}) = 1,
\qquad
\mathbf{w}-\mathbf{v} = (1,0,0) \Rightarrow d(\mathbf{w},\mathbf{v}) = 1 .
$$

Hence $d(\mathbf{u},\mathbf{v}) = 1.414 \le 1 + 1 = 2$ ✓. The inequality is strict, as it must be:
$\mathbf{w} = (1,1,1)$ does not lie on the segment from $\mathbf{u}$ to $\mathbf{v}$, whose points are
$(1-t,\ t,\ 1)$ with $0 \le t \le 1$, and equality in the triangle inequality occurs only when the three
points are collinear in the order $\mathbf{u},\mathbf{w},\mathbf{v}$ (Exercise 32).

**6.** *Answer:* $\langle\mathbf{z},\mathbf{w}\rangle = 4i$, $\langle\mathbf{w},\mathbf{z}\rangle = -4i$,
$\lVert\mathbf{z}\rVert = \sqrt3$, $\lVert\mathbf{w}\rVert = \sqrt6$, and
$\lvert 4i\rvert = 4 \le \sqrt{18} \approx 4.243$ ✓.

$$
\langle\mathbf{z},\mathbf{w}\rangle = (1+i)\overline{(1-i)} + i\,\bar2 = (1+i)(1+i) + 2i = (1 + 2i + i^2) + 2i = 2i + 2i = 4i,
$$

$$
\langle\mathbf{w},\mathbf{z}\rangle = (1-i)\overline{(1+i)} + 2\,\bar i = (1-i)(1-i) - 2i = (1 - 2i + i^2) - 2i = -4i = \overline{\langle\mathbf{z},\mathbf{w}\rangle} ✓ .
$$

Norms: $\lVert\mathbf{z}\rVert^2 = \lvert1+i\rvert^2 + \lvert i\rvert^2 = 2+1 = 3$;
$\lVert\mathbf{w}\rVert^2 = \lvert1-i\rvert^2 + 4 = 2+4 = 6$. Cauchy–Schwarz:
$\lvert 4i\rvert = 4 \le \sqrt3\sqrt6 = \sqrt{18} \approx 4.243$ ✓ (strict, since the vectors are not
complex-proportional).

**7.** *Answer:* yes, it is orthonormal.

The three conditions are: unit norms, pairwise orthogonality, and no zero vector (implied by the norms).
Let $\mathbf{u}_1 = (1,0,0)$, $\mathbf{u}_2 = (0,1,1)/\sqrt2$, $\mathbf{u}_3 = (0,1,-1)/\sqrt2$.

*Norms:* $\lVert\mathbf{u}_1\rVert = 1$; $\lVert\mathbf{u}_2\rVert^2 = (0+1+1)/2 = 1$;
$\lVert\mathbf{u}_3\rVert^2 = (0+1+1)/2 = 1$.

*Orthogonality:*
$\mathbf{u}_1\cdot\mathbf{u}_2 = 0$ and $\mathbf{u}_1\cdot\mathbf{u}_3 = 0$ because both latter vectors have
first coordinate $0$; and
$\mathbf{u}_2\cdot\mathbf{u}_3 = (0\cdot0 + 1\cdot1 + 1\cdot(-1))/2 = 0$ ✓.

**8.** *Answer:* $\mathbf{p} = (\tfrac72,\tfrac72)$, and the distance is $\tfrac{1}{\sqrt2} \approx 0.707$.

The projection onto the line spanned by $\mathbf{u} = (1,1)$ is

$$
\mathbf{p} = \frac{\langle\mathbf{b},\mathbf{u}\rangle}{\langle\mathbf{u},\mathbf{u}\rangle}\mathbf{u}
= \frac{3+4}{2}(1,1) = \frac72(1,1) = \left(\tfrac72,\tfrac72\right).
$$

Residual $\mathbf{b}-\mathbf{p} = (-\tfrac12,\tfrac12)$, and
$\langle(-\tfrac12,\tfrac12),(1,1)\rangle = -\tfrac12+\tfrac12 = 0$ ✓.
Distance: $\lVert\mathbf{b}-\mathbf{p}\rVert = \sqrt{\tfrac14+\tfrac14} = \tfrac{1}{\sqrt2} \approx 0.707$.

*Interpretation:* the point of the line $y = x$ closest to $(3,4)$ is $(3.5,3.5)$; the distance is the
length of the perpendicular, and $0.707 = \lvert 4-3\rvert/\sqrt2$ as the distance-from-a-line formula
predicts.

**9.** *Answer:* (a) $0$; (b) $\pi$; (c) $\pi$; (d) $0$.

(a) $\sin x\cos x = \tfrac12\sin 2x$, an odd function integrated over a symmetric interval: $0$.
(b) $\sin^2x = \tfrac12(1-\cos 2x)$, so $\int_{-\pi}^{\pi}\sin^2x\,dx = \tfrac12(2\pi) - \tfrac12\cdot0 = \pi$.
(c) Similarly $\cos^2x = \tfrac12(1+\cos 2x)$ gives $\pi$.
(d) $\sin x\sin 2x = \tfrac12[\cos(x) - \cos(3x)]$, and both cosines integrate to $0$ over $[-\pi,\pi]$.

These are exactly the statements that make
$\{1/\sqrt{2\pi},\ \cos kx/\sqrt\pi,\ \sin kx/\sqrt\pi\}$ orthonormal: (b) and (c) give the norms
$\sqrt\pi$, while (a) and (d) give the pairwise orthogonality.

**10.** *Answer:* $Q^{\mathsf{T}}Q = I$, $\det Q = -1$, and $Q$ is the reflection in the line $y = x$.

$$
Q^{\mathsf{T}}Q = \frac12\begin{pmatrix}1&1\\1&-1\end{pmatrix}\begin{pmatrix}1&1\\1&-1\end{pmatrix}
= \frac12\begin{pmatrix}1+1 & 1-1\\ 1-1 & 1+1\end{pmatrix} = I ✓ .
$$

$\det Q = \frac12\big(1\cdot(-1) - 1\cdot1\big) = \frac12(-2) = -1$.

*Geometry:* $Q(1,1) = \frac{1}{\sqrt2}(2,0) = (\sqrt2,0)$, which is a positive multiple of $(1,1)$;
$Q(1,-1) = \frac{1}{\sqrt2}(0,2) = (0,\sqrt2)$, which is the negative of $(1,-1)/\sqrt2$. So $Q$ fixes the
line $y = x$ pointwise and reverses the perpendicular direction: a reflection.

*Norms preserved:* $\lVert(1,0)\rVert = 1$ and $\lVert Q(1,0)\rVert = \lVert \tfrac{1}{\sqrt2}(1,1)\rVert = 1$ ✓;
$\lVert(1,1)\rVert = \sqrt2$ and $\lVert Q(1,1)\rVert = \sqrt2$ ✓.

**11.** *Answer:* $\langle 1,x\rangle = \tfrac12$, $\lVert1\rVert = 1$, $\lVert x\rVert = \tfrac{1}{\sqrt3}$,
and the angle is $30^\circ$.

$$
\langle 1,x\rangle = \int_0^1 x\,dx = \frac12,
\qquad
\lVert1\rVert^2 = \int_0^1 1\,dx = 1,
\qquad
\lVert x\rVert^2 = \int_0^1 x^2\,dx = \frac13 .
$$

Then $\cos\theta = \dfrac{1/2}{1\cdot 1/\sqrt3} = \dfrac{\sqrt3}{2}$, so $\theta = 30^\circ$. That is a
pleasant surprise: the functions $1$ and $x$ are not "close" in the function-space sense, but they are
much closer than orthogonal.

**12.** *Answer:* $\dfrac{(1,1)}{\sqrt2}$ and $\dfrac{(1,-1)}{\sqrt2}$.

$\mathbf{v}_1 = (1,1)$ with $\lVert\mathbf{v}_1\rVert^2 = 2$. Then

$$
\mathbf{v}_2 = (1,0) - \frac{\langle(1,0),(1,1)\rangle}{2}(1,1) = (1,0) - \tfrac12(1,1) = \left(\tfrac12,-\tfrac12\right),
\qquad \lVert\mathbf{v}_2\rVert^2 = \tfrac14+\tfrac14 = \tfrac12 .
$$

Normalising: $\mathbf{u}_1 = (1,1)/\sqrt2$ and
$\mathbf{u}_2 = \left(\tfrac12,-\tfrac12\right)/\tfrac{1}{\sqrt2} = (1,-1)/\sqrt2$.

*Checks:* $\lVert\mathbf{u}_1\rVert = \lVert\mathbf{u}_2\rVert = 1$ and
$\mathbf{u}_1\cdot\mathbf{u}_2 = (1-1)/2 = 0$ ✓. The span of the two is $\mathbb{R}^2$, as expected from
the span-preservation property of Gram–Schmidt.

## Intermediate

**13.** *Answer:*

$$
\mathbf{u}_1 = \frac{(1,1,1)}{\sqrt3}, \qquad
\mathbf{u}_2 = \frac{(1,1,-2)}{\sqrt6}, \qquad
\mathbf{u}_3 = \frac{(1,-1,0)}{\sqrt2} .
$$

*Step 1.* $\mathbf{v}_1 = (1,1,1)$, $\lVert\mathbf{v}_1\rVert^2 = 3$.

*Step 2.* $\langle\mathbf{a}_2,\mathbf{v}_1\rangle = 1+1+0 = 2$, so

$$
\mathbf{v}_2 = (1,1,0) - \frac{2}{3}(1,1,1) = \left(\tfrac13,\tfrac13,-\tfrac23\right),
\qquad \lVert\mathbf{v}_2\rVert^2 = \tfrac19+\tfrac19+\tfrac49 = \tfrac23 .
$$

*Step 3.* $\langle\mathbf{a}_3,\mathbf{v}_1\rangle = 1$ and $\langle\mathbf{a}_3,\mathbf{v}_2\rangle = \tfrac13$, so

$$
\mathbf{v}_3 = (1,0,0) - \frac{1}{3}(1,1,1) - \frac{1/3}{2/3}\left(\tfrac13,\tfrac13,-\tfrac23\right)
= \left(1 - \tfrac13 - \tfrac16,\ -\tfrac13-\tfrac16,\ -\tfrac13+\tfrac13\right) = \left(\tfrac12,-\tfrac12,0\right),
$$

with $\lVert\mathbf{v}_3\rVert^2 = \tfrac12$.

*Normalise.* $\mathbf{v}_2 = \tfrac13(1,1,-2)$ has norm $\tfrac13\sqrt6$; dividing gives $(1,1,-2)/\sqrt6$.
$\mathbf{v}_3 = \tfrac12(1,-1,0)$ gives $(1,-1,0)/\sqrt2$.

*Checks:* $\mathbf{u}_1\cdot\mathbf{u}_2 = (1+1-2)/\sqrt{18} = 0$ ✓,
$\mathbf{u}_1\cdot\mathbf{u}_3 = (1-1+0)/\sqrt6 = 0$ ✓,
$\mathbf{u}_2\cdot\mathbf{u}_3 = (1-1+0)/\sqrt{12} = 0$ ✓, and all three norms are $1$ ✓.

**14.** *Answer:*

$$
Q = \begin{pmatrix}\tfrac{1}{\sqrt2} & \tfrac{1}{\sqrt3}\\[2pt] \tfrac{1}{\sqrt2} & -\tfrac{1}{\sqrt3}\\[2pt] 0 & \tfrac{1}{\sqrt3}\end{pmatrix},
\qquad
R = \begin{pmatrix}\sqrt2 & \sqrt2\\ 0 & \sqrt3\end{pmatrix}.
$$

The columns of $A$ are $\mathbf{a}_1 = (1,1,0)$ and $\mathbf{a}_2 = (2,0,1)$. Gram–Schmidt:

$$
\mathbf{q}_1 = \frac{(1,1,0)}{\sqrt2}, \qquad
r_{12} = \langle\mathbf{a}_2,\mathbf{q}_1\rangle = \frac{2}{\sqrt2} = \sqrt2,
$$
$$
\mathbf{v}_2 = (2,0,1) - \sqrt2\cdot\frac{(1,1,0)}{\sqrt2} = (2,0,1) - (1,1,0) = (1,-1,1),
\qquad \lVert\mathbf{v}_2\rVert = \sqrt3,
$$

so $\mathbf{q}_2 = (1,-1,1)/\sqrt3$ and $r_{22} = \sqrt3$. Also
$r_{11} = \lVert\mathbf{a}_1\rVert = \sqrt2$ and $r_{21} = 0$ (upper triangular).

*Check* $Q^{\mathsf{T}}Q = I$: $\lVert\mathbf{q}_1\rVert = \lVert\mathbf{q}_2\rVert = 1$ and
$\mathbf{q}_1\cdot\mathbf{q}_2 = (1-1+0)/\sqrt6 = 0$ ✓.
*Check* $QR = A$: first column $\sqrt2\,\mathbf{q}_1 = (1,1,0)$ ✓; second column
$\sqrt2\,\mathbf{q}_1 + \sqrt3\,\mathbf{q}_2 = (1,1,0) + (1,-1,1) = (2,0,1)$ ✓.

**15.** *Answer:* $y = -0.5 + 1.6x$.

The design matrix and data vector are

$$
A = \begin{pmatrix}1&1\\1&2\\1&3\\1&4\end{pmatrix}, \qquad \mathbf{y} = \begin{pmatrix}1\\3\\4\\6\end{pmatrix}.
$$

Then $S_t = 1+2+3+4 = 10$, $S_{tt} = 1+4+9+16 = 30$, $S_y = 14$, $S_{ty} = 1+6+12+24 = 43$, so

$$
A^{\mathsf{T}}A = \begin{pmatrix}4&10\\10&30\end{pmatrix}, \qquad
A^{\mathsf{T}}\mathbf{y} = \begin{pmatrix}14\\43\end{pmatrix}.
$$

The determinant is $120 - 100 = 20$, hence

$$
b = \frac{4\cdot43 - 10\cdot14}{20} = \frac{172-140}{20} = 1.6, \qquad
a = \frac{30\cdot14 - 10\cdot43}{20} = \frac{420-430}{20} = -0.5 .
$$

*Residual:* $r_i = y_i - (-0.5+1.6t_i)$ gives $(-0.1,\ 0.3,\ -0.3,\ 0.1)$. Checks:
$\sum r_i = 0$ ✓ and $\sum t_ir_i = -0.1+0.6-0.9+0.4 = 0$ ✓ — precisely the two normal equations.

**16.** *Answer:* $y = 1.45 + 0.35x + 0.75x^2$.

The design matrix is $A = \begin{pmatrix}1&-1&1\\1&0&0\\1&1&1\\1&2&4\end{pmatrix}$ and
$\mathbf{y} = (2,1,3,5)^{\mathsf{T}}$. The normal equations $A^{\mathsf{T}}A\mathbf{c} = A^{\mathsf{T}}\mathbf{y}$ are

$$
\begin{pmatrix}4&2&6\\ 2&6&8\\ 6&8&18\end{pmatrix}\begin{pmatrix}a\\b\\c\end{pmatrix}
= \begin{pmatrix}11\\11\\25\end{pmatrix},
$$

since $\sum x = 2$, $\sum x^2 = 6$, $\sum x^3 = 8$, $\sum x^4 = 18$, $\sum y = 11$, $\sum xy = 11$,
$\sum x^2y = 25$. Solving: from the first equation $b = (11-4a-6c)/2$; substituting into the second gives
$a+c = 2.2$, and into the third gives $10a+6c = 19$. Hence $c = 0.75$, $a = 1.45$, $b = 0.35$.

*Check* $A^{\mathsf{T}}(\mathbf{y}-A\mathbf{c}) = \mathbf{0}$: the residuals are
$(0.15,\ -0.45,\ 0.45,\ -0.15)$, with

$$
\textstyle\sum r_i = 0, \qquad \sum x_ir_i = -0.15+0+0.45-0.30 = 0, \qquad \sum x_i^2r_i = 0.15+0+0.45-0.60 = 0 ✓ .
$$

**17.** *Answer:* $\mathbf{p} = \left(\tfrac23,\tfrac73,\tfrac53\right)$, residual
$\left(\tfrac43,-\tfrac43,\tfrac43\right)$.

With $M = \begin{pmatrix}1&0\\1&1\\0&1\end{pmatrix}$ (columns $(1,1,0)$ and $(0,1,1)$),

$$
M^{\mathsf{T}}M = \begin{pmatrix}2&1\\1&2\end{pmatrix}, \qquad
M^{\mathsf{T}}\mathbf{b} = \begin{pmatrix}2+1\\1+3\end{pmatrix} = \begin{pmatrix}3\\4\end{pmatrix}.
$$

Solving $2c_1+c_2 = 3$, $c_1+2c_2 = 4$ gives $c_1 = \tfrac23$, $c_2 = \tfrac53$, so

$$
\mathbf{p} = \tfrac23(1,1,0) + \tfrac53(0,1,1) = \left(\tfrac23,\ \tfrac23+\tfrac53,\ \tfrac53\right) = \left(\tfrac23,\tfrac73,\tfrac53\right).
$$

*Check:* $\mathbf{b}-\mathbf{p} = \left(\tfrac43,-\tfrac43,\tfrac43\right)$, and
$\langle\mathbf{b}-\mathbf{p},(1,1,0)\rangle = \tfrac43-\tfrac43 = 0$ ✓,
$\langle\mathbf{b}-\mathbf{p},(0,1,1)\rangle = -\tfrac43+\tfrac43 = 0$ ✓. The distance is
$\lVert\mathbf{b}-\mathbf{p}\rVert = \sqrt{3\cdot\tfrac{16}{9}} = \tfrac{4}{\sqrt3} \approx 2.309$.

**18.** *Answer:* $W^{\perp} = \{(x,y,z) : x+y+z = 0\}$, of dimension $2$, with basis
$(1,-1,0)$, $(1,0,-1)$.

By definition $\mathbf{v} \in W^{\perp}$ iff $\langle\mathbf{v},(1,1,1)\rangle = 0$, i.e. $x+y+z = 0$:
a single linear equation in three unknowns, so the solution space has dimension $3-1 = 2$.

Two independent solutions are $(1,-1,0)$ and $(1,0,-1)$: both satisfy $x+y+z=0$, and they are not
multiples of one another. *Checks:*
$\langle(1,-1,0),(1,1,1)\rangle = 0$ ✓, $\langle(1,0,-1),(1,1,1)\rangle = 0$ ✓, and
$\dim W + \dim W^{\perp} = 1 + 2 = 3 = \dim\mathbb{R}^3$ ✓, in agreement with Corollary 7.15.

**19.** *Answer:* $a_0 = \dfrac{2\pi^2}{3}$, $a_k = \dfrac{4(-1)^k}{k^2}$, $b_k = 0$ for all $k \ge 1$;
in particular $a_1 = -4$, $a_2 = 1$, $a_3 = -\tfrac49$.

Since $x^2\sin kx$ is odd, $b_k = 0$. For $a_0$,

$$
a_0 = \frac{1}{\pi}\int_{-\pi}^{\pi}x^2dx = \frac{1}{\pi}\cdot\frac{2\pi^3}{3} = \frac{2\pi^2}{3}.
$$

For $k \ge 1$, integrate by parts twice:

$$
\int x^2\cos kx\,dx = \frac{x^2\sin kx}{k} + \frac{2x\cos kx}{k^2} - \frac{2\sin kx}{k^3},
$$

and the sine terms vanish at $\pm\pi$, leaving

$$
a_k = \frac{1}{\pi}\left[\frac{2x\cos kx}{k^2}\right]_{-\pi}^{\pi}
= \frac{1}{\pi}\cdot\frac{4\pi\cos k\pi}{k^2} = \frac{4(-1)^k}{k^2}.
$$

*Checks:* $a_1 = -4$, $a_2 = 4/4 = 1$, $a_3 = -4/9$ ✓. So
$x^2 \sim \dfrac{\pi^2}{3} - 4\cos x + \cos 2x - \dfrac49\cos 3x + \cdots$.

**20.** *Proof.* Parseval's identity for $f(x) = x^2$ reads

$$
\frac{1}{\pi}\int_{-\pi}^{\pi}x^4dx = \frac{a_0^2}{2} + \sum_{k\ge1}a_k^2
$$

(because every $b_k = 0$). The left side is $\dfrac{1}{\pi}\cdot\dfrac{2\pi^5}{5} = \dfrac{2\pi^4}{5}$. On the
right, $\dfrac{a_0^2}{2} = \dfrac12\cdot\dfrac{4\pi^4}{9} = \dfrac{2\pi^4}{9}$ and
$\sum a_k^2 = \sum\dfrac{16}{k^4}$. Hence

$$
\frac{2\pi^4}{5} = \frac{2\pi^4}{9} + 16\sum_{k\ge1}\frac{1}{k^4}
\;\Longrightarrow\;
16\sum_{k\ge1}\frac{1}{k^4} = 2\pi^4\left(\frac15-\frac19\right) = \frac{8\pi^4}{45},
$$

so $\sum_{k\ge1}\frac{1}{k^4} = \frac{\pi^4}{90}$ ✓. $\blacksquare$

**21.** *Answer:*

$$
Q = \frac{1}{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}, \qquad
D = \begin{pmatrix}4&0\\0&2\end{pmatrix}.
$$

$p_A(\lambda) = \lambda^2 - 6\lambda + 8 = (\lambda-4)(\lambda-2)$, so $A$ has eigenvalues $4$ and $2$. For
$\lambda = 4$: $A - 4I = \begin{pmatrix}-1&1\\1&-1\end{pmatrix}$ gives $x = y$, so $\mathbf{q}_1 = (1,1)/\sqrt2$.
For $\lambda = 2$: $A - 2I = \begin{pmatrix}1&1\\1&1\end{pmatrix}$ gives $x = -y$, so
$\mathbf{q}_2 = (1,-1)/\sqrt2$. Orthogonality is automatic (symmetric matrix, distinct eigenvalues) and can
be checked: $\mathbf{q}_1\cdot\mathbf{q}_2 = (1-1)/2 = 0$ ✓.

*Verification by $AQ = QD$:*
$AQ = \frac{1}{\sqrt2}\big(A(1,1)\mid A(1,-1)\big) = \frac{1}{\sqrt2}\big((4,4)\mid(2,-2)\big)$ and
$QD = \frac{1}{\sqrt2}\big(4(1,1)\mid 2(1,-1)\big)$, which are equal ✓. Hence $Q^{\mathsf{T}}AQ = D$ with
$Q^{-1} = Q^{\mathsf{T}}$.

**22.** *Answer:* maximum $4$, attained at $\pm(1,1)/\sqrt2$; minimum $2$, attained at
$\pm(1,-1)/\sqrt2$.

Write $\mathbf{x} = (x,y)$. Then

$$
R(\mathbf{x}) = \frac{3x^2+2xy+3y^2}{x^2+y^2} = \frac{3(x^2+y^2) + 2xy}{x^2+y^2}.
$$

Use the eigenbasis of Exercise 21: set $u = (x+y)/\sqrt2$, $v = (x-y)/\sqrt2$, so that
$x^2+y^2 = u^2+v^2$ and $2xy = u^2-v^2$. Then

$$
R = \frac{3(u^2+v^2) + (u^2-v^2)}{u^2+v^2} = \frac{4u^2+2v^2}{u^2+v^2} .
$$

This is a weighted average of $4$ and $2$ with weights $u^2/(u^2+v^2)$ and $v^2/(u^2+v^2)$, hence
$2 \le R \le 4$. The value $4$ requires $v = 0$, i.e. $x = y$; the value $2$ requires $u = 0$, i.e.
$x = -y$. Both are attained, at the normalised vectors of Exercise 21.

*Consistency with the spectral theorem:* the extreme values of the Rayleigh quotient are the extreme
eigenvalues, and the extremisers are the corresponding eigenvectors.

## Advanced

**23.** Expand both squares using linearity and symmetry (the space is real, so
$\langle\mathbf{u},\mathbf{v}\rangle = \langle\mathbf{v},\mathbf{u}\rangle$):

$$
\lVert\mathbf{u}+\mathbf{v}\rVert^2 = \langle\mathbf{u}+\mathbf{v},\mathbf{u}+\mathbf{v}\rangle
= \lVert\mathbf{u}\rVert^2 + 2\langle\mathbf{u},\mathbf{v}\rangle + \lVert\mathbf{v}\rVert^2,
$$

$$
\lVert\mathbf{u}-\mathbf{v}\rVert^2 = \langle\mathbf{u}-\mathbf{v},\mathbf{u}-\mathbf{v}\rangle
= \lVert\mathbf{u}\rVert^2 - 2\langle\mathbf{u},\mathbf{v}\rangle + \lVert\mathbf{v}\rVert^2 .
$$

Subtracting the second from the first cancels the norm terms and leaves
$4\langle\mathbf{u},\mathbf{v}\rangle$, so

$$
\langle\mathbf{u},\mathbf{v}\rangle = \tfrac14\left(\lVert\mathbf{u}+\mathbf{v}\rVert^2 - \lVert\mathbf{u}-\mathbf{v}\rVert^2\right).
$$

*Deduction.* The right-hand side is computed from the norm alone. Hence two inner products on the same
space that induce the same norm must coincide: for every pair $(\mathbf{u},\mathbf{v})$ the value
$\langle\mathbf{u},\mathbf{v}\rangle$ is determined by $\lVert\cdot\rVert$. (In the complex case the
corresponding formula is
$\langle\mathbf{u},\mathbf{v}\rangle = \tfrac14\sum_{k=0}^{3}i^k\lVert\mathbf{u}+i^k\mathbf{v}\rVert^2$,
which again uses only the norm.) $\blacksquare$

**24.** *(a)* Expand as in Exercise 23 and add:

$$
\lVert\mathbf{u}+\mathbf{v}\rVert^2 + \lVert\mathbf{u}-\mathbf{v}\rVert^2
= 2\lVert\mathbf{u}\rVert^2 + 2\lVert\mathbf{v}\rVert^2 . \qquad\blacksquare
$$

*(b)* Take $\mathbf{u} = (1,0)$, $\mathbf{v} = (0,1)$.

*For $\lVert\cdot\rVert_1$:* $\mathbf{u}+\mathbf{v} = (1,1)$ and $\mathbf{u}-\mathbf{v} = (1,-1)$, both of
$\ell^1$-norm $2$. Left side: $2^2 + 2^2 = 8$. Right side: $2\cdot1^2 + 2\cdot1^2 = 4$. Since $8 \neq 4$,
the parallelogram law fails, so by (a) no inner product induces $\lVert\cdot\rVert_1$.

*For $\lVert\cdot\rVert_\infty$:* both $(1,1)$ and $(1,-1)$ have $\ell^\infty$-norm $1$. Left side:
$1 + 1 = 2$; right side: $2 + 2 = 4$. Again $2 \neq 4$, so no inner product induces
$\lVert\cdot\rVert_\infty$. $\blacksquare$

*Remark.* The parallelogram law is not merely necessary but also sufficient (Jordan–von Neumann): a norm
satisfying it comes from an inner product defined by the polarization identity.

**25.** *(a)* $\lVert\mathbf{u}+\mathbf{v}\rVert^2 = \lVert\mathbf{u}\rVert^2 + 2\langle\mathbf{u},\mathbf{v}\rangle + \lVert\mathbf{v}\rVert^2$
and the middle term vanishes. For several vectors, expand
$\lVert\sum_i\mathbf{v}_i\rVert^2 = \sum_{i,j}\langle\mathbf{v}_i,\mathbf{v}_j\rangle$; every term with
$i \neq j$ vanishes by pairwise orthogonality, leaving $\sum_i\lVert\mathbf{v}_i\rVert^2$.

*(b)* Write $\mathbf{b} = \mathbf{p} + \mathbf{q}$ with $\mathbf{p} = P_W\mathbf{b} \in W$ and
$\mathbf{q} = \mathbf{b}-\mathbf{p} \in W^{\perp}$ (Theorem 7.14). These are orthogonal, so by (a)

$$
\lVert\mathbf{b}\rVert^2 = \lVert\mathbf{p}\rVert^2 + \lVert\mathbf{q}\rVert^2 \ge \lVert\mathbf{p}\rVert^2 = \lVert P_W\mathbf{b}\rVert^2 .
$$

Taking square roots gives $\lVert P_W\mathbf{b}\rVert \le \lVert\mathbf{b}\rVert$, with equality iff
$\mathbf{b} \in W$. $\blacksquare$

**26.** *Proof by induction on $j$.* For $j = 1$: $\mathbf{v}_1 = \mathbf{a}_1 \neq \mathbf{0}$ since
$\mathbf{a}_1$ is part of an independent set, $\mathbf{u}_1 = \mathbf{v}_1/\lVert\mathbf{v}_1\rVert$ is a
unit vector, and $\operatorname{span}\{\mathbf{u}_1\} = \operatorname{span}\{\mathbf{a}_1\}$.

Assume the statement for $j-1$. Write
$\mathbf{v}_j = \mathbf{a}_j - \sum_{i<j}\langle\mathbf{a}_j,\mathbf{u}_i\rangle\mathbf{u}_i$ (equivalent to
the displayed formula, since $\mathbf{v}_i = \lVert\mathbf{v}_i\rVert\mathbf{u}_i$).

*Nonzero:* if $\mathbf{v}_j = \mathbf{0}$ then
$\mathbf{a}_j = \sum_{i<j}\langle\mathbf{a}_j,\mathbf{u}_i\rangle\mathbf{u}_i \in \operatorname{span}\{\mathbf{u}_1,\dots,\mathbf{u}_{j-1}\} = \operatorname{span}\{\mathbf{a}_1,\dots,\mathbf{a}_{j-1}\}$,
contradicting independence. So $\mathbf{u}_j$ is well defined.

*Orthogonality:* for $i < j$,
$\langle\mathbf{v}_j,\mathbf{u}_i\rangle = \langle\mathbf{a}_j,\mathbf{u}_i\rangle - \sum_{l<j}\langle\mathbf{a}_j,\mathbf{u}_l\rangle\langle\mathbf{u}_l,\mathbf{u}_i\rangle = \langle\mathbf{a}_j,\mathbf{u}_i\rangle - \langle\mathbf{a}_j,\mathbf{u}_i\rangle = 0$,
using $\langle\mathbf{u}_l,\mathbf{u}_i\rangle = \delta_{li}$. Hence $\mathbf{u}_j \perp \mathbf{u}_i$.

*Spans:* $\mathbf{v}_j$ is $\mathbf{a}_j$ minus a combination of $\mathbf{u}_1,\dots,\mathbf{u}_{j-1}$,
hence lies in $\operatorname{span}\{\mathbf{a}_1,\dots,\mathbf{a}_j\}$; conversely
$\mathbf{a}_j = \mathbf{v}_j + \sum_{i<j}\langle\mathbf{a}_j,\mathbf{u}_i\rangle\mathbf{u}_i$ lies in
$\operatorname{span}\{\mathbf{u}_1,\dots,\mathbf{u}_j\}$. The two spans have the same dimension and one
contains the other, so they coincide. $\blacksquare$

**27.** *(a)* Suppose first that $P^2 = P = P^{\mathsf{T}}$. For any $\mathbf{b}$,
$\mathbf{p} = P\mathbf{b} \in \operatorname{col}(P)$, and for any $\mathbf{v} = P\mathbf{u} \in \operatorname{col}(P)$,

$$
\langle\mathbf{b}-\mathbf{p},\mathbf{v}\rangle = (\mathbf{b}-P\mathbf{b})^{\mathsf{T}}P\mathbf{u}
= \mathbf{b}^{\mathsf{T}}P\mathbf{u} - \mathbf{b}^{\mathsf{T}}P^{\mathsf{T}}P\mathbf{u}
= \mathbf{b}^{\mathsf{T}}P\mathbf{u} - \mathbf{b}^{\mathsf{T}}P^2\mathbf{u} = 0,
$$

using $P^{\mathsf{T}} = P$ and $P^2 = P$. So $\mathbf{b}-P\mathbf{b} \perp \operatorname{col}(P)$, which by
the projection theorem (Theorem 7.14) says $P\mathbf{b}$ is the orthogonal projection of $\mathbf{b}$ onto
$\operatorname{col}(P)$.

Conversely, if $P$ is the orthogonal projection onto $W = \operatorname{col}(P)$, then $P\mathbf{b} \in W$
and $P\mathbf{w} = \mathbf{w}$ for $\mathbf{w} \in W$, so $P^2\mathbf{b} = P(P\mathbf{b}) = P\mathbf{b}$ and
$P^2 = P$. For symmetry, let $\mathbf{u},\mathbf{v}$ be arbitrary and use
$\mathbf{v} - P\mathbf{v} \perp W \ni P\mathbf{u}$ and $\mathbf{u} - P\mathbf{u} \perp W \ni P\mathbf{v}$:

$$
\langle P\mathbf{u},\mathbf{v}\rangle = \langle P\mathbf{u},P\mathbf{v}\rangle + \langle P\mathbf{u},\mathbf{v}-P\mathbf{v}\rangle = \langle P\mathbf{u},P\mathbf{v}\rangle,
$$
$$
\langle\mathbf{u},P\mathbf{v}\rangle = \langle P\mathbf{u},P\mathbf{v}\rangle + \langle\mathbf{u}-P\mathbf{u},P\mathbf{v}\rangle = \langle P\mathbf{u},P\mathbf{v}\rangle,
$$

so $\langle P\mathbf{u},\mathbf{v}\rangle = \langle\mathbf{u},P\mathbf{v}\rangle$ for all $\mathbf{u},\mathbf{v}$,
which is the statement $P^{\mathsf{T}} = P$. $\blacksquare$

*(b)* Take $P = \begin{pmatrix}1&1\\0&0\end{pmatrix}$. Then

$$
P^2 = \begin{pmatrix}1&1\\0&0\end{pmatrix}\begin{pmatrix}1&1\\0&0\end{pmatrix} = \begin{pmatrix}1&1\\0&0\end{pmatrix} = P,
$$

so $P$ is idempotent, but $P^{\mathsf{T}} = \begin{pmatrix}1&0\\1&0\end{pmatrix} \neq P$. Geometrically
$P(x,y) = (x+y,0)$: the image is the $x$-axis and the kernel is $\{(x,y) : x+y = 0\} = \operatorname{span}\{(1,-1)\}$.
So $P$ projects onto the $x$-axis **along the direction** $(1,-1)$ — an *oblique* projection. It is not the
orthogonal projection (which would be $\operatorname{diag}(1,0)$), and correspondingly it does not decrease
norms: $P(1,-1) = (0,0)$ but $P(1,1) = (2,0)$ has norm $2 > \sqrt2$. $\blacksquare$

**28.** *(a)* If the columns of $A$ are independent and $A^{\mathsf{T}}A\mathbf{x} = \mathbf{0}$, then

$$
0 = \mathbf{x}^{\mathsf{T}}A^{\mathsf{T}}A\mathbf{x} = (A\mathbf{x})^{\mathsf{T}}(A\mathbf{x}) = \lVert A\mathbf{x}\rVert^2,
$$

so $A\mathbf{x} = \mathbf{0}$ and independence gives $\mathbf{x} = \mathbf{0}$. A square matrix whose only
kernel vector is $\mathbf{0}$ is invertible, so $A^{\mathsf{T}}A$ is invertible.

Conversely, if the columns are dependent there is $\mathbf{x} \neq \mathbf{0}$ with $A\mathbf{x} = \mathbf{0}$,
hence $A^{\mathsf{T}}A\mathbf{x} = \mathbf{0}$ and $A^{\mathsf{T}}A$ is singular.

*(b)* Let $F(\mathbf{x}) = \lVert A\mathbf{x}-\mathbf{b}\rVert^2 = (A\mathbf{x}-\mathbf{b})^{\mathsf{T}}(A\mathbf{x}-\mathbf{b})$.
Expanding,

$$
F(\mathbf{x}) = \mathbf{x}^{\mathsf{T}}A^{\mathsf{T}}A\mathbf{x} - 2\mathbf{x}^{\mathsf{T}}A^{\mathsf{T}}\mathbf{b} + \mathbf{b}^{\mathsf{T}}\mathbf{b},
$$

whose gradient is $\nabla F = 2A^{\mathsf{T}}A\mathbf{x} - 2A^{\mathsf{T}}\mathbf{b}$ and whose Hessian is
$2A^{\mathsf{T}}A$, a positive semidefinite matrix (since $\mathbf{z}^{\mathsf{T}}A^{\mathsf{T}}A\mathbf{z} = \lVert A\mathbf{z}\rVert^2 \ge 0$).
So $F$ is convex and its critical points are global minima; setting $\nabla F = \mathbf{0}$ gives
$A^{\mathsf{T}}A\mathbf{x} = A^{\mathsf{T}}\mathbf{b}$, which is unique when $A^{\mathsf{T}}A$ is
invertible by (a). $\blacksquare$

**29.** *(a)* From $Q^{\mathsf{T}}Q = I$,

$$
1 = \det I = \det(Q^{\mathsf{T}}Q) = \det(Q^{\mathsf{T}})\det Q = (\det Q)^2,
$$

so $\det Q = \pm1$. If $Q\mathbf{v} = \lambda\mathbf{v}$ with $\mathbf{v} \neq \mathbf{0}$, then by
Theorem 7.16(d), $\lVert\mathbf{v}\rVert = \lVert Q\mathbf{v}\rVert = \lvert\lambda\rvert\lVert\mathbf{v}\rVert$,
so $\lvert\lambda\rvert = 1$.

*(b)* Write $Q = \begin{pmatrix}a&b\\c&d\end{pmatrix}$. Orthonormal columns give $a^2+c^2 = 1$, so
$(a,c) = (\cos\theta,\sin\theta)$ for a unique $\theta$. The second column $(b,d)$ is a unit vector
orthogonal to $(a,c)$; in $\mathbb{R}^2$ the only unit vectors orthogonal to $(a,c)$ are
$\pm(-\sin\theta,\cos\theta)$. Hence

$$
Q = \begin{pmatrix}\cos\theta & -\sin\theta\\ \sin\theta & \cos\theta\end{pmatrix}
\quad(\det Q = 1,\ \text{rotation by } \theta),
\qquad
Q = \begin{pmatrix}\cos\theta & \sin\theta\\ \sin\theta & -\cos\theta\end{pmatrix}
\quad(\det Q = -1,\ \text{reflection}).
$$

For the second form, $Q^2 = I$ and $Q$ fixes the line spanned by $(\cos\tfrac\theta2,\sin\tfrac\theta2)$,
so it is the reflection in that line. $\blacksquare$

**30.** *(a)* Let $\mathbf{p} = \sum_{i=1}^{m}\langle\mathbf{x},\mathbf{u}_i\rangle\mathbf{u}_i$. For each $j$,

$$
\langle\mathbf{x}-\mathbf{p},\mathbf{u}_j\rangle = \langle\mathbf{x},\mathbf{u}_j\rangle - \sum_i\langle\mathbf{x},\mathbf{u}_i\rangle\langle\mathbf{u}_i,\mathbf{u}_j\rangle = \langle\mathbf{x},\mathbf{u}_j\rangle - \langle\mathbf{x},\mathbf{u}_j\rangle = 0,
$$

so $\mathbf{x}-\mathbf{p} \perp \operatorname{span}\{\mathbf{u}_1,\dots,\mathbf{u}_m\}$. By Pythagoras
(Exercise 25) and Theorem 7.10,

$$
\lVert\mathbf{x}\rVert^2 = \lVert\mathbf{p}\rVert^2 + \lVert\mathbf{x}-\mathbf{p}\rVert^2
= \sum_{i=1}^{m}\lvert\langle\mathbf{x},\mathbf{u}_i\rangle\rvert^2 + \lVert\mathbf{x}-\mathbf{p}\rVert^2
\ge \sum_{i=1}^{m}\lvert\langle\mathbf{x},\mathbf{u}_i\rangle\rvert^2 .
$$

*(b)* Equality holds iff $\lVert\mathbf{x}-\mathbf{p}\rVert^2 = 0$, i.e. $\mathbf{x} = \mathbf{p}$, i.e.
$\mathbf{x}$ lies in the span of the $\mathbf{u}_i$. In that case the coefficients are the coordinates of
$\mathbf{x}$ and the identity is Parseval. $\blacksquare$

**31.** Let $A = \begin{pmatrix}a&b\\b&d\end{pmatrix}$, so $A$ is symmetric.

*Case $b = 0$:* $A = \operatorname{diag}(a,d)$ is already diagonal; take $Q = I$.

*Case $b \neq 0$:* then

$$
p_A(\lambda) = (a-\lambda)(d-\lambda) - b^2 = \lambda^2 - (a+d)\lambda + (ad - b^2),
$$

with discriminant

$$
\Delta = (a+d)^2 - 4(ad-b^2) = (a-d)^2 + 4b^2 > 0,
$$

so there are two distinct real eigenvalues $\lambda_1 \neq \lambda_2$. Choose nonzero eigenvectors
$\mathbf{v}_1,\mathbf{v}_2$. By Lemma 7.20 (which applies because $A$ is symmetric),

$$
(\lambda_1-\lambda_2)\langle\mathbf{v}_1,\mathbf{v}_2\rangle = \langle A\mathbf{v}_1,\mathbf{v}_2\rangle - \langle\mathbf{v}_1,A\mathbf{v}_2\rangle = 0,
$$

and $\lambda_1 \neq \lambda_2$ gives $\langle\mathbf{v}_1,\mathbf{v}_2\rangle = 0$. Normalising,
$\mathbf{q}_i = \mathbf{v}_i/\lVert\mathbf{v}_i\rVert$ are orthonormal, so $Q = (\mathbf{q}_1\mid\mathbf{q}_2)$
is orthogonal, and $Q^{\mathsf{T}}AQ = \operatorname{diag}(\lambda_1,\lambda_2)$ because the columns are
eigenvectors. $\blacksquare$

## Challenge

**32.** *Proof.* Squaring both sides of $\lVert\mathbf{u}+\mathbf{v}\rVert = \lVert\mathbf{u}\rVert+\lVert\mathbf{v}\rVert$
(both are nonnegative) and expanding,

$$
\lVert\mathbf{u}\rVert^2 + 2\operatorname{Re}\langle\mathbf{u},\mathbf{v}\rangle + \lVert\mathbf{v}\rVert^2
= \lVert\mathbf{u}\rVert^2 + 2\lVert\mathbf{u}\rVert\lVert\mathbf{v}\rVert + \lVert\mathbf{v}\rVert^2,
$$

so equality is equivalent to

$$
\operatorname{Re}\langle\mathbf{u},\mathbf{v}\rangle = \lVert\mathbf{u}\rVert\lVert\mathbf{v}\rVert .
$$

Because $\operatorname{Re}\langle\mathbf{u},\mathbf{v}\rangle \le \lvert\langle\mathbf{u},\mathbf{v}\rangle\rvert \le \lVert\mathbf{u}\rVert\lVert\mathbf{v}\rVert$
(Cauchy–Schwarz), this forces both inequalities to be equalities: $\langle\mathbf{u},\mathbf{v}\rangle$ is a
real number equal to $\lVert\mathbf{u}\rVert\lVert\mathbf{v}\rVert \ge 0$.

If $\mathbf{u} = \mathbf{0}$ or $\mathbf{v} = \mathbf{0}$ the claim is trivial ($\mathbf{v} = c\mathbf{0}$
with $c \ge 0$, or $\mathbf{u} = 0\cdot\mathbf{v}$). Otherwise both are nonzero, and equality in
Cauchy–Schwarz gives $\mathbf{v} = c\mathbf{u}$ for some scalar $c$. Then
$\langle\mathbf{u},\mathbf{v}\rangle = \bar c\lVert\mathbf{u}\rVert^2$ and
$\lVert\mathbf{u}\rVert\lVert\mathbf{v}\rVert = \lvert c\rvert\lVert\mathbf{u}\rVert^2$; since both equal
the same nonnegative number, $\bar c = \lvert c\rvert$, which forces $c \ge 0$.

Conversely, if $\mathbf{v} = c\mathbf{u}$ with $c \ge 0$, then
$\lVert\mathbf{u}+\mathbf{v}\rVert = (1+c)\lVert\mathbf{u}\rVert = \lVert\mathbf{u}\rVert+\lVert\mathbf{v}\rVert$ ✓.
$\blacksquare$

*Consequence.* Equality in Cauchy–Schwarz holds iff the vectors are dependent (Theorem 7.4); equality in
the triangle inequality is the *sharper* statement that the dependence has a **nonnegative** factor, i.e.
the vectors point in the same direction.

**33.** *Answer:* the orthogonal (unnormalised) polynomials are

$$
q_0 = 1, \qquad q_1 = x, \qquad q_2 = x^2 - \tfrac13, \qquad q_3 = x^3 - \tfrac35x,
$$

with squared norms $2$, $\tfrac23$, $\tfrac{8}{45}$, $\tfrac{8}{175}$.

*Step 1.* $\langle1,1\rangle = \int_{-1}^1 1\,dx = 2$, so $q_0 = 1$.

*Step 2.* $\langle x,1\rangle = \int_{-1}^1x\,dx = 0$ (odd), so $q_1 = x$; $\lVert x\rVert^2 = \int_{-1}^1x^2dx = \tfrac23$.

*Step 3.* $\langle x^2,1\rangle = \int_{-1}^1x^2dx = \tfrac23$, so
$q_2 = x^2 - \tfrac{2/3}{2}\cdot1 = x^2 - \tfrac13$. Its norm:
$\int_{-1}^1(x^2-\tfrac13)^2dx = \int x^4 - \tfrac23x^2 + \tfrac19 = \tfrac25 - \tfrac49 + \tfrac29 = \tfrac{8}{45}$.

*Step 4.* $\langle x^3,1\rangle = 0$ (odd) and
$\langle x^3,x\rangle = \int_{-1}^1x^4dx = \tfrac25$, so
$q_3 = x^3 - \tfrac{2/5}{2/3}x = x^3 - \tfrac35x$. Its norm:
$\int_{-1}^1x^6dx = \tfrac27$, $\int x^3\cdot\tfrac35x = \tfrac35\cdot\tfrac25 = \tfrac6{25}$, and
$\int\tfrac9{25}x^2 = \tfrac9{25}\cdot\tfrac23 = \tfrac6{25}$; so
$\lVert q_3\rVert^2 = \tfrac27 - 2\cdot\tfrac6{25} + \tfrac6{25} = \tfrac27 - \tfrac6{25} = \tfrac{50-42}{175} = \tfrac{8}{175}$.

*Orthogonality checks:* $\langle q_0,q_1\rangle = 0$ and $\langle q_0,q_3\rangle = 0$ by oddness;
$\langle q_0,q_2\rangle = \tfrac23 - \tfrac13\cdot2 = 0$ ✓;
$\langle q_1,q_2\rangle = \int x(x^2-\tfrac13) = 0$ by oddness ✓;
$\langle q_1,q_3\rangle = \int x(x^3-\tfrac35x) = \tfrac25 - \tfrac35\cdot\tfrac23 = 0$ ✓;
$\langle q_2,q_3\rangle = \int (x^2-\tfrac13)(x^3-\tfrac35x)dx$: the integrand expands to
$x^5 - \tfrac35x^3 - \tfrac13x^3 + \tfrac15x = x^5 - \tfrac{14}{15}x^3 + \tfrac15x$, a combination of odd
powers, so the integral over $[-1,1]$ is $0$ ✓.

The normalised versions are the first four **Legendre polynomials** up to sign:
$\sqrt{\tfrac12}$, $\sqrt{\tfrac32}x$, $\sqrt{\tfrac{45}{8}}(x^2-\tfrac13)$, $\sqrt{\tfrac{175}{8}}(x^3-\tfrac35x)$.

**34.** *Derivation.* With the design matrix columns $\mathbf{1}$ and $\mathbf{t}$, the Gram matrix is
$A^{\mathsf{T}}A = \begin{pmatrix}m&S_t\\ S_t&S_{tt}\end{pmatrix}$ and
$A^{\mathsf{T}}\mathbf{y} = \begin{pmatrix}S_y\\ S_{ty}\end{pmatrix}$, so the normal equations are

$$
ma + bS_t = S_y, \qquad aS_t + bS_{tt} = S_{ty}.
$$

The determinant is $D = mS_{tt} - S_t^2$. Cramer's rule gives

$$
b = \frac{mS_{ty} - S_tS_y}{D}, \qquad a = \frac{S_{tt}S_y - S_tS_{ty}}{D} = \frac{S_y - bS_t}{m},
$$

where the last equality is a rearrangement: $S_{tt}S_y - S_tS_{ty} = S_{tt}S_y - S_t(mS_{ty}-S_tS_y)/m = (S_y(mS_{tt}-S_t^2))/m$.

*Positivity.* Let $\bar t = S_t/m$. Then

$$
mS_{tt} - S_t^2 = m\sum_i t_i^2 - \Big(\sum_i t_i\Big)^2 = m\sum_i (t_i-\bar t)^2 ,
$$

which is a sum of squares and is therefore $\ge 0$; it is $0$ exactly when every $t_i = \bar t$, i.e. all
$t_i$ are equal (in which case the line is not determined by the data, and indeed the two normal equations
coincide up to a factor).

*Correlation.* Centre the data: $t_i' = t_i - \bar t$, $y_i' = y_i - \bar y$, and let
$S'_{tt} = \sum(t_i')^2$, $S'_{yy} = \sum(y_i')^2$, $S'_{ty} = \sum t_i'y_i'$. Cauchy–Schwarz applied to the
vectors $(t_1',\dots,t_m')$ and $(y_1',\dots,y_m')$ in $\mathbb{R}^m$ gives

$$
\lvert S'_{ty}\rvert \le \sqrt{S'_{tt}\,S'_{yy}},
\qquad\text{i.e.}\qquad
\lvert r\rvert = \frac{\lvert S'_{ty}\rvert}{\sqrt{S'_{tt}S'_{yy}}} \le 1 .
$$

Equality $\lvert r\rvert = 1$ occurs exactly when the centred vectors are proportional, i.e. when the data
lie exactly on a line. $\blacksquare$

**35.** *Coefficients.* $f$ is odd, so $a_k = 0$ for all $k \ge 0$. For $k \ge 1$,

$$
b_k = \frac{1}{\pi}\int_{-\pi}^{\pi}f(x)\sin kx\,dx = \frac{2}{\pi}\int_0^{\pi}\sin kx\,dx
= \frac{2}{\pi}\cdot\frac{1-\cos k\pi}{k}
= \frac{2\big(1-(-1)^k\big)}{k\pi} .
$$

Hence $b_k = \dfrac{4}{k\pi}$ for odd $k$ and $b_k = 0$ for even $k$, and

$$
f(x) \sim \frac{4}{\pi}\left(\sin x + \frac{\sin 3x}{3} + \frac{\sin 5x}{5} + \cdots\right).
$$

*Parseval.* $\frac{1}{\pi}\int_{-\pi}^{\pi}f(x)^2dx = \frac{1}{\pi}\cdot 2\pi = 2$ (the square is $1$
everywhere except at the two jumps, which do not affect the integral). Parseval gives

$$
2 = \sum_{k\ge1}b_k^2 = \frac{16}{\pi^2}\sum_{k\ \text{odd}}\frac{1}{k^2},
\qquad\text{so}\qquad
\sum_{k\ \text{odd}}\frac{1}{k^2} = \frac{2\pi^2}{16} = \frac{\pi^2}{8} ✓ .
$$

Since $\sum_{k\ge1}k^{-2} = \pi^2/6$ (Example 9.6) and the even terms sum to
$\tfrac14\sum_{k\ge1}k^{-2} = \pi^2/24$, the odd terms sum to $\pi^2/6 - \pi^2/24 = 3\pi^2/24 = \pi^2/8$ ✓,
which confirms the computation independently. $\blacksquare$
