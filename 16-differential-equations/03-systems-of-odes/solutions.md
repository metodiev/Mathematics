# Systems of ODEs — Solutions

> [Systems of ODEs](README.md) · Solutions to the 36 problems in [exercises.md](exercises.md)

Each solution states the strategy, carries out the steps, and ends with a verification: the answer is
substituted back, or the hypotheses of the theorem used are checked. Where a choice was made (a
generalised eigenvector, a Lyapunov function, a Dulac multiplier), the reason for the choice is given.

## Beginner

### Solution 1

*Strategy: apply Theorem 7.1 with $x_1 = y$, $x_2 = y'$.*

From $x_1' = y' = x_2$ and $x_2' = y'' = -2y - 3y' = -2x_1 - 3x_2$,

$$\mathbf{x}' = \begin{pmatrix}0&1\\-2&-3\end{pmatrix}\mathbf{x} = A\mathbf{x}.$$

The characteristic polynomial is

$$\det(A-\lambda I) = \begin{vmatrix}-\lambda & 1\\ -2 & -3-\lambda\end{vmatrix} = -\lambda(-3-\lambda) + 2 = \lambda^2 + 3\lambda + 2 = (\lambda+1)(\lambda+2),$$

so the eigenvalues are $\lambda = -1$ and $\lambda = -2$. The original equation has characteristic equation $r^2+3r+2 = 0$ with the same roots. Agreement is guaranteed: by Definition 7.1 and the determinant identity of §7.1, $\det(A-\lambda I) = (-1)^2 p(\lambda) = p(\lambda)$.

*Check.* $A\binom{1}{-1} = \binom{-1}{1} = -1\cdot\binom{1}{-1}$ ✓ and $A\binom{1}{-2} = \binom{-2}{4} = -2\binom{1}{-2}$ ✓.

### Solution 2

*Strategy: stack $x_1 = y$, $x_2 = y'$, $x_3 = y''$.*

$x_1' = x_2$, $x_2' = x_3$, $x_3' = y''' = y = x_1$, so

$$A = \begin{pmatrix}0&1&0\\0&0&1\\1&0&0\end{pmatrix}.$$

Expanding along the first row,

$$\det(A-\lambda I) = \begin{vmatrix}-\lambda&1&0\\0&-\lambda&1\\1&0&-\lambda\end{vmatrix} = -\lambda(\lambda^2) - 1\cdot(0\cdot(-\lambda) - 1\cdot 1) + 0 = 1-\lambda^3 .$$

Hence $\lambda^3 = 1$, i.e.

$$\lambda = 1, \qquad \lambda = -\tfrac12 \pm \tfrac{\sqrt3}{2}i .$$

*Check.* $\det A = 1 = \lambda_1\lambda_2\lambda_3 = 1\cdot\left(\tfrac14+\tfrac34\right) = 1$ ✓, and $\operatorname{tr}A = 0 = 1 + \left(-\tfrac12+\tfrac12\right) = 0$ ✓. The scalar equation $y''' - y = 0$ has characteristic roots $\lambda^3 - 1 = 0$, matching.

### Solution 3

With $x_1 = y$, $x_2 = y'$: $x_1' = x_2$ and $x_2' = y'' = -4y + \cos t = -4x_1 + \cos t$, so

$$\mathbf{x}' = \begin{pmatrix}0&1\\-4&0\end{pmatrix}\mathbf{x} + \binom{0}{\cos t}.$$

*Check.* The first component reproduces $x_2 = y'$; the second, $x_2' = -4x_1+\cos t$, is the original equation with $x_1 = y$. ✓

### Solution 4

$\tau = 3$, $\delta = 1\cdot2 - 3\cdot2 = -4$, so $\lambda^2 - 3\lambda - 4 = 0$ and $\lambda = 4,-1$.

For $\lambda = 4$: $(A-4I)\mathbf{v} = \begin{pmatrix}-3&3\\2&-2\end{pmatrix}\mathbf{v} = \mathbf{0}$, so $-3v_1+3v_2 = 0$ and $\mathbf{v}_1 = (1,1)^{\mathsf T}$.

For $\lambda = -1$: $(A+I)\mathbf{v} = \begin{pmatrix}2&3\\2&3\end{pmatrix}\mathbf{v} = \mathbf{0}$, so $2v_1+3v_2 = 0$ and $\mathbf{v}_2 = (3,-2)^{\mathsf T}$.

$$\mathbf{x}(t) = c_1e^{4t}\binom{1}{1} + c_2e^{-t}\binom{3}{-2}.$$

*Check.* $A\binom{1}{1} = \binom{4}{4}$ ✓; $A\binom{3}{-2} = \binom{3-6}{6-4} = \binom{-3}{2} = -1\binom{3}{-2}$ ✓.

### Solution 5

Impose $\mathbf{x}(0) = (5,0)^{\mathsf T}$:

$$c_1\binom{1}{1} + c_2\binom{3}{-2} = \binom{5}{0} \Longrightarrow \begin{cases}c_1+3c_2 = 5\\ c_1-2c_2 = 0\end{cases} \Longrightarrow c_1 = 2c_2,\ 5c_2 = 5,$$

so $c_2 = 1$ and $c_1 = 2$. Hence

$$\mathbf{x}(t) = 2e^{4t}\binom{1}{1} + e^{-t}\binom{3}{-2}.$$

*Check.* At $t = 0$: $(2+3,\ 2-2) = (5,0)$ ✓. Differentiating, $\mathbf{x}' = 8e^{4t}(1,1) - e^{-t}(3,-2)$, while $A\mathbf{x} = 2e^{4t}(4,4) + e^{-t}(-3,2)$, which agree ✓. As $t\to\infty$ the dominant term is $2e^{4t}(1,1)$: the solution leaves along the unstable eigenline.

### Solution 6

The system is decoupled: $x_1' = 2x_1$, $x_2' = -3x_2$, so

$$x_1 = c_1e^{2t}, \qquad x_2 = c_2e^{-3t}, \qquad \mathbf{x}(0) = (1,4)^{\mathsf T} \Longrightarrow \mathbf{x}(t) = \binom{e^{2t}}{4e^{-3t}}.$$

*Check.* $x_1' = 2e^{2t} = 2x_1$ ✓, $x_2' = -12e^{-3t} = -3x_2$ ✓, and $\mathbf{x}(0) = (1,4)$ ✓.

$\tau = -1$, $\delta = -6<0$: a **saddle**. The stable eigendirection is $\mathbf{e}_2$, the unstable one is $\mathbf{e}_1$.

### Solution 7

$A^2 = \begin{pmatrix}0&1\\0&0\end{pmatrix}\begin{pmatrix}0&1\\0&0\end{pmatrix} = \begin{pmatrix}0&0\\0&0\end{pmatrix}$, so every term of the series with $k\ge2$ vanishes and

$$e^{At} = I + At = \begin{pmatrix}1&t\\0&1\end{pmatrix}.$$

*Check.* At $t=0$ this is $I$ ✓; $\dfrac{d}{dt}e^{At} = \begin{pmatrix}0&1\\0&0\end{pmatrix} = A = Ae^{At}$ ✓ (since $A^2 = 0$).

With $\mathbf{x}(0) = (a,b)^{\mathsf T}$, $\mathbf{x}(t) = (a+bt,\ b)^{\mathsf T}$: the orbits are the horizontal lines $x_2 = b$, traversed to the right for $b>0$ and to the left for $b<0$. The $x_1$-axis consists entirely of equilibria ($\delta = 0$: a line of equilibria, and $A$ is nilpotent).

### Solution 8

$A = \begin{pmatrix}0&1\\-1&0\end{pmatrix}$ satisfies $A^2 = -I$, so as in Example 9.3,

$$e^{At} = (\cos t)I + (\sin t)A = \begin{pmatrix}\cos t & \sin t\\ -\sin t & \cos t\end{pmatrix}, \qquad \mathbf{x}(t) = e^{At}\binom{1}{0} = \binom{\cos t}{-\sin t}.$$

*Check.* $\mathbf{x}(0) = (1,0)$ ✓; $\mathbf{x}' = (-\sin t, -\cos t)$ and $A\mathbf{x} = (-\sin t, -\cos t)$ ✓. The orbit is the unit circle $x_1^2+x_2^2 = 1$.

$\tau = 0$ and $\delta = 1$: a **centre**, stable but not attracting. At $t=0$ the point is at $(1,0)$ with velocity $(0,-1)$, so the motion is **clockwise**.

### Solution 9

| | $\tau$ | $\delta$ | $\Delta$ | Eigenvalues | Type |
|---|---|---|---|---|---|
| (a) | $-3$ | $2$ | $1>0$ | $-1,-2$ | stable node |
| (b) | $3$ | $2$ | $1>0$ | $1,2$ | unstable node |
| (c) | $0$ | $-1$ | $4>0$ | $1,-1$ | saddle |
| (d) | $0$ | $1$ | $-4<0$ | $\pm i$ | centre |
| (e) | $2$ | $2$ | $-4<0$ | $1\pm i$ | unstable spiral |

Stability: (a) asymptotically stable; (b) and (c) unstable; (d) stable but not attracting; (e) unstable. For (e), $\alpha = \tau/2 = 1>0$ makes the spiral expand; the rotation is by $\beta = 1$.

### Solution 10

Eigenvalues: $\lambda = -2$ and $\lambda = -3$, since the matrix is triangular. Eigenvectors: for $\lambda = -2$, $(A+2I) = \begin{pmatrix}0&1\\0&-1\end{pmatrix}$ gives $v_2 = 0$, so $\mathbf{v}_1 = (1,0)^{\mathsf T}$; for $\lambda = -3$, $(A+3I) = \begin{pmatrix}1&1\\0&0\end{pmatrix}$ gives $v_1+v_2 = 0$, so $\mathbf{v}_2 = (1,-1)^{\mathsf T}$.

$$\mathbf{x}(t) = c_1e^{-2t}\binom{1}{0} + c_2e^{-3t}\binom{1}{-1}.$$

$\tau = -5$, $\delta = 6>0$, $\Delta = 1>0$: a **stable node**. Because $-3<-2$, the mode $e^{-3t}$ decays faster; the ratio of the second component to the first is dominated by $c_2e^{-3t}/(-c_2e^{-3t}) = -1$ initially but the $e^{-2t}$ mode survives longest, so every orbit approaches the origin **tangent to $\mathbf{v}_1 = (1,0)$**, the slow eigendirection.

*Check.* $A\binom{1}{0} = \binom{-2}{0}$ ✓ and $A\binom{1}{-1} = \binom{-3}{3} = -3\binom{1}{-1}$ ✓.

### Solution 11

Set $x'=0$, $y'=0$: $x-y+1 = 0$ and $2x+4 = 0$, so $x = -2$ and $y = x+1 = -1$. The equilibrium is $(-2,-1)$.

Shift: $u = x+2$, $v = y+1$, so $x = u-2$, $y = v-1$. Then

$$u' = x' = x-y+1 = (u-2)-(v-1)+1 = u-v, \qquad v' = y' = 2x+4 = 2(u-2)+4 = 2u,$$

so $\mathbf{u}' = \begin{pmatrix}1&-1\\2&0\end{pmatrix}\mathbf{u}$.

Here $\tau = 1$, $\delta = 2$, $\Delta = 1-8 = -7<0$: $\lambda = \tfrac12 \pm \tfrac{\sqrt7}{2}i$, an **unstable spiral**.

*Check.* At $(x,y) = (-2,-1)$: $x-y+1 = -2+1+1 = 0$ ✓ and $2x+4 = 0$ ✓. In the shifted variables the origin is an equilibrium: $u-v = 0$, $2u = 0$ ✓.

### Solution 12

From $x_2 = x_1'$ and $x_2' = -x_1+1$, differentiate the first: $x_1'' = x_2' = -x_1+1$, i.e.

$$x_1''+x_1 = 1.$$

A particular solution is $x_1 = 1$; the homogeneous solution is $A\cos t + B\sin t$. Thus $x_1 = 1 + A\cos t + B\sin t$. The conditions $x_1(0) = 0$ and $x_1'(0) = x_2(0) = 0$ give $1+A = 0$, i.e. $A = -1$, and $B = 0$. Hence

$$x_1 = 1-\cos t, \qquad x_2 = x_1' = \sin t.$$

*Check.* $x_1(0) = 0$, $x_2(0) = 0$ ✓. $x_1' = \sin t = x_2$ ✓. $x_2' = \cos t$ and $-x_1+1 = -(1-\cos t)+1 = \cos t$ ✓.

## Intermediate

### Solution 13

$\tau = 2$, $\delta = 1+4 = 5$, $\Delta = 4-20 = -16<0$, so $\lambda = 1\pm 2i$.

For $\lambda = 1+2i$,

$$A-\lambda I = \begin{pmatrix}1-(1+2i) & -2\\ 2 & 1-(1+2i)\end{pmatrix} = \begin{pmatrix}-2i&-2\\2&-2i\end{pmatrix}.$$

The first row gives $-2iv_1-2v_2 = 0$, i.e. $v_2 = -iv_1$; the second row gives $2v_1-2iv_2 = 2v_1-2i(-iv_1) = 2v_1-2v_1 = 0$, consistent. Take

$$\mathbf{v} = \binom{1}{-i} = \underbrace{\binom{1}{0}}_{\mathbf{p}} + i\underbrace{\binom{0}{-1}}_{\mathbf{q}} .$$

By Theorem 7.11 with $\alpha = 1$, $\beta = 2$:

$$\mathbf{x}(t) = e^{t}\left[\binom{1}{0}\cos 2t - \binom{0}{-1}\sin 2t\right] = e^{t}\binom{\cos 2t}{\sin 2t},$$

$$\mathbf{y}(t) = e^{t}\left[\binom{1}{0}\sin 2t + \binom{0}{-1}\cos 2t\right] = e^{t}\binom{\sin 2t}{-\cos 2t}.$$

The initial condition $(1,0)^{\mathsf T}$ selects the first:

$$\mathbf{x}(t) = e^{t}\binom{\cos 2t}{\sin 2t}.$$

*Check.* $\mathbf{x}' = e^t\binom{\cos 2t - 2\sin 2t}{\sin 2t + 2\cos 2t}$ and

$$A\mathbf{x} = e^t\begin{pmatrix}1&-2\\2&1\end{pmatrix}\binom{\cos 2t}{\sin 2t} = e^t\binom{\cos 2t-2\sin 2t}{2\cos 2t+\sin 2t} ✓.$$

In polar coordinates $r = e^t$ and $\theta = 2t$, so $r = e^{\theta/2}$: an **outward spiral**, anticlockwise, one revolution per $\pi$ time units. $\tau = 2>0$ with $\delta>0$ and $\Delta<0$ confirms an unstable spiral.

### Solution 14

$\tau = 2$, $\delta = 1$, so $(\lambda-1)^2 = 0$: the eigenvalue $\lambda = 1$ is double.

*Eigenvector.* $(A-I) = \begin{pmatrix}0&2\\0&0\end{pmatrix}$ gives $v_2 = 0$, so $\mathbf{v} = (1,0)^{\mathsf T}$; the eigenspace is one-dimensional, so $A$ is defective.

*Generalised eigenvector.* Solve $(A-I)\mathbf{u} = \mathbf{v}$: the first row gives $2u_2 = 1$, so $\mathbf{u} = (0,\tfrac12)^{\mathsf T}$ works.

*General solution.* By Theorem 7.12,

$$\mathbf{x}(t) = c_1e^{t}\binom{1}{0} + c_2e^{t}\left[\binom{0}{1/2} + t\binom{1}{0}\right] = e^{t}\binom{c_1+c_2t}{c_2/2}.$$

*Exponential.* The columns are the solutions with $\mathbf{x}(0) = \mathbf{e}_1$ (giving $c_1 = 1$, $c_2 = 0$) and $\mathbf{e}_2$ (giving $c_1 = 0$, $c_2 = 2$):

$$e^{At} = e^{t}\begin{pmatrix}1 & 2t\\ 0 & 1\end{pmatrix} = e^{t}\left(I+tN\right), \qquad N = \begin{pmatrix}0&2\\0&0\end{pmatrix},\quad N^2 = 0 .$$

*Initial condition.* $\mathbf{x}(0) = (1,2)^{\mathsf T}$ gives $c_1 = 1$ and $c_2/2 = 2$, so $c_2 = 4$:

$$\mathbf{x}(t) = e^{t}\binom{1+4t}{2}.$$

*Check.* $\mathbf{x}(0) = (1,2)$ ✓. $\mathbf{x}' = e^{t}\binom{1+4t+4}{2} = e^{t}\binom{5+4t}{2}$, while

$$A\mathbf{x} = e^{t}\begin{pmatrix}1&2\\0&1\end{pmatrix}\binom{1+4t}{2} = e^{t}\binom{1+4t+4}{2} ✓.$$

All orbits approach the origin tangent to the eigenline spanned by $(1,0)$ — the degenerate node of §7.5.

### Solution 15

Eigenvalues: $\tau = 3$, $\delta = 2$, so $\lambda = 1,2$. Eigenvectors: for $\lambda = 1$, $(A-I) = \begin{pmatrix}0&1\\0&1\end{pmatrix}$ gives $v_2 = 0$, $\mathbf{v}_1 = (1,0)^{\mathsf T}$; for $\lambda = 2$, $(A-2I) = \begin{pmatrix}-1&1\\0&0\end{pmatrix}$ gives $v_1 = v_2$, $\mathbf{v}_2 = (1,1)^{\mathsf T}$.

Thus $A = PDP^{-1}$ with

$$P = \begin{pmatrix}1&1\\0&1\end{pmatrix}, \qquad D = \begin{pmatrix}1&0\\0&2\end{pmatrix}, \qquad P^{-1} = \begin{pmatrix}1&-1\\0&1\end{pmatrix},$$

so

$$e^{At} = P\begin{pmatrix}e^t&0\\0&e^{2t}\end{pmatrix}P^{-1} = \begin{pmatrix}e^t & e^{2t}-e^t\\ 0 & e^{2t}\end{pmatrix}.$$

*Check.* At $t=0$: $\begin{pmatrix}1&1-1\\0&1\end{pmatrix} = I$ ✓. Differentiating: $\begin{pmatrix}e^t & 2e^{2t}-e^t\\0&2e^{2t}\end{pmatrix}$, while

$$Ae^{At} = \begin{pmatrix}1&1\\0&2\end{pmatrix}\begin{pmatrix}e^t&e^{2t}-e^t\\0&e^{2t}\end{pmatrix} = \begin{pmatrix}e^t & e^{2t}-e^t+e^{2t}\\ 0&2e^{2t}\end{pmatrix} ✓.$$

### Solution 16

The matrix is block diagonal, $A = \operatorname{diag}(B,-2)$ with $B = \begin{pmatrix}1&1\\0&1\end{pmatrix} = I+N$ and $N = \begin{pmatrix}0&1\\0&0\end{pmatrix}$, $N^2 = 0$. The exponential of a block-diagonal matrix is the block-diagonal matrix of the exponentials, so

$$e^{At} = \begin{pmatrix}e^{Bt}&0\\0&e^{-2t}\end{pmatrix} = \begin{pmatrix}e^{t} & te^{t} & 0\\ 0 & e^{t} & 0\\ 0 & 0 & e^{-2t}\end{pmatrix}.$$

*Why the blocks decouple.* The system is $x_1' = x_1+x_2$, $x_2' = x_2$, $x_3' = -2x_3$: the third equation involves only $x_3$, and the first two only $x_1,x_2$.

*Initial condition.* $\mathbf{x}(0) = (0,1,1)^{\mathsf T}$ selects the second column in the first two entries and the third diagonal entry:

$$\mathbf{x}(t) = \begin{pmatrix}te^{t}\\ e^{t}\\ e^{-2t}\end{pmatrix}.$$

*Check.* $\mathbf{x}(0) = (0,1,1)$ ✓. $\mathbf{x}' = \begin{pmatrix}(1+t)e^{t}\\ e^{t}\\ -2e^{-2t}\end{pmatrix}$, while

$$A\mathbf{x} = \begin{pmatrix}x_1+x_2\\ x_2\\ -2x_3\end{pmatrix} = \begin{pmatrix}te^t+e^t\\ e^t\\ -2e^{-2t}\end{pmatrix} ✓.$$

### Solution 17

The system decouples but is nonhomogeneous:

$$x_2' = 2x_2+e^{2t}, \qquad x_1' = x_1+e^{2t}.$$

*Second equation.* The forcing $e^{2t}$ is at the natural frequency, so try $x_2 = Ate^{2t}$: $(A+2At)e^{2t} = 2Ate^{2t}+e^{2t}$ gives $A = 1$. Hence $x_2 = (c_2+t)e^{2t}$.

*First equation.* Try $x_1 = Be^{2t}$: $2Be^{2t} = Be^{2t}+e^{2t}$ gives $B = 1$, so $x_1 = c_1e^{t}+e^{2t}$.

*Initial conditions.* $x_1(0) = c_1+1 = 0$, so $c_1 = -1$; $x_2(0) = c_2 = 0$. Therefore

$$\mathbf{x}(t) = \binom{e^{2t}-e^{t}}{te^{2t}}.$$

*Check.* $\mathbf{x}(0) = (0,0)$ ✓. $x_1' = 2e^{2t}-e^t = x_1+e^{2t}$ ✓. $x_2' = e^{2t}+2te^{2t} = 2x_2+e^{2t}$ ✓.

### Solution 18

$A = \begin{pmatrix}0&1\\-1&0\end{pmatrix}$ has $e^{At} = \begin{pmatrix}\cos t&\sin t\\-\sin t&\cos t\end{pmatrix}$ (Example 9.3 with $\alpha = 0$, $\beta = 1$).

*Variation of constants.*

$$\mathbf{x}(t) = \int_0^t e^{A(t-s)}\binom{0}{\sin s}\,ds = \int_0^t\binom{\sin(t-s)\sin s}{\cos(t-s)\sin s}\,ds .$$

*First component.* Use the product-to-sum identity $\sin(t-s)\sin s = \frac12\left[\cos(t-2s)-\cos t\right]$:

$$\int_0^t\sin(t-s)\sin s\,ds = \frac12\left[\frac{\sin(t-2s)}{-2}\right]_0^t-\frac{t\cos t}{2} = \frac12\cdot\frac{-\sin t-\sin t}{-2}-\frac{t\cos t}{2} = \frac{\sin t}{2}-\frac{t\cos t}{2}.$$

*Second component.* $x_2 = x_1' = \frac12\left(\cos t-\cos t+t\sin t\right) = \dfrac{t\sin t}{2}$.

*Answer.*

$$\mathbf{x}(t) = \frac12\binom{\sin t-t\cos t}{t\sin t}.$$

*Check.* $\mathbf{x}(0) = \mathbf{0}$ ✓. $x_1' = \frac12(\cos t-\cos t+t\sin t) = \frac{t\sin t}{2} = x_2$ ✓. $x_2' = \frac12(\sin t+t\cos t)$, and $-x_1+\sin t = -\frac12(\sin t-t\cos t)+\sin t = \frac12(\sin t+t\cos t)$ ✓.

*Why the amplitude grows.* The forcing $\sin t$ oscillates at the natural frequency of the homogeneous system ($\omega = 1$). Each push arrives in phase with the motion and adds energy, so the amplitude grows linearly — the resonance of [Second-Order Linear ODEs](../02-second-order-linear-odes/README.md) in system form. A forcing at any other frequency would produce bounded oscillation.

### Solution 19

The system is $\theta' = \omega$, $\omega' = -\frac{g}{L}\sin\theta-b\omega$ with $g/L = 9.81/2 = 4.905$ and $b = 0.4$.

*Bottom, $(\theta,\omega) = (0,0)$.* The Jacobian is

$$J = \begin{pmatrix}0&1\\ -\frac{g}{L}\cos\theta & -b\end{pmatrix}_{(0,0)} = \begin{pmatrix}0&1\\-4.905&-0.4\end{pmatrix},$$

with $\tau = -0.4$, $\delta = 4.905>0$, $\Delta = 0.16-19.62<0$. A **stable spiral**, with eigenvalues

$$\lambda = \frac{-0.4\pm i\sqrt{19.46}}{2} = -0.2\pm 2.2057i .$$

The quasi-period is $2\pi/2.2057 \approx 2.849\ \mathrm{s}$. The undamped period would be $2\pi/\sqrt{4.905} = 2\pi/2.2147 \approx 2.837\ \mathrm{s}$; damping lengthens it slightly. The decay time is $1/0.2 = 5\ \mathrm{s}$.

*Top, $(\theta,\omega) = (\pi,0)$.* Now $\cos\pi = -1$, so

$$J = \begin{pmatrix}0&1\\ 4.905&-0.4\end{pmatrix}, \qquad \tau = -0.4,\ \delta = -4.905<0,$$

a **saddle**, with eigenvalues

$$\lambda = \frac{-0.4\pm\sqrt{0.16+19.62}}{2} = \frac{-0.4\pm 4.4458}{2}, \qquad \lambda_1 \approx 2.023,\quad \lambda_2\approx -2.423 .$$

*Check.* The product of the eigenvalues is $-4.905 = \delta$ ✓ and their sum is $-0.4 = \tau$ ✓. The saddle is unstable for every damping $b$, because $\delta<0$ is independent of $b$; damping only tilts the eigenlines.

### Solution 20

*Equilibrium.* $x(3-2y) = 0$ and $y(x-1) = 0$ with $x,y>0$ give $y = 3/2$ and $x = 1$: the point $(1,\tfrac32)$.

*Linearisation.* With $f_1 = x(3-2y)$, $f_2 = y(x-1)$,

$$J(x,y) = \begin{pmatrix}3-2y & -2x\\ y & x-1\end{pmatrix}, \qquad J\left(1,\tfrac32\right) = \begin{pmatrix}0&-2\\ \tfrac32&0\end{pmatrix}.$$

$\tau = 0$, $\delta = 3>0$, $\Delta = -12<0$: eigenvalues $\pm i\sqrt3$.

*Consequence.* The angular frequency is $\sqrt3$ and the period of the linearised oscillation $2\pi/\sqrt3\approx 3.63$. The linearisation shows a **centre**: it proves nothing about stability, because a centre is non-hyperbolic and Hartman–Grobman does not apply — the nonlinear orbits could spiral in or out.

*What actually happens.* The function $H(x,y) = x-\ln x-3\ln y+2y$ satisfies

$$\dot H = \left(1-\frac1x\right)x(3-2y)+\left(2-\frac3y\right)y(x-1) = (x-1)(3-2y)+(2y-3)(x-1) = 0,$$

so orbits lie on level curves of $H$. $H\to\infty$ at the boundary of the quadrant and has a unique critical point at $(1,3/2)$ (from $1-1/x = 0$, $2-3/y = 0$), which is a strict minimum since the Hessian there is $\operatorname{diag}(1, 3/y^2) = \operatorname{diag}(1,4/3)$. The level sets are therefore closed curves: every positive orbit is periodic and the equilibrium is a genuine centre.

### Solution 21

*Equilibria.* From $x(3-2x-y) = 0$ and $y(2-x-2y) = 0$:

* $x = 0$, $y = 0$: $(0,0)$;
* $x = 0$ and $2-x-2y = 0$: $(0,1)$;
* $y = 0$ and $3-2x-y = 0$: $(\tfrac32,0)$;
* both factors zero: $3-2x-y = 0$, $2-x-2y = 0$. From the second, $x = 2-2y$; substituting, $3-2(2-2y)-y = -1+3y = 0$, so $y = \tfrac13$ and $x = \tfrac43$. The interior equilibrium is $(\tfrac43,\tfrac13)$.

*Jacobian.*

$$J(x,y) = \begin{pmatrix}3-4x-y & -x\\ -y & 2-x-4y\end{pmatrix}.$$

*Classifications.*

* $(0,0)$: $J = \begin{pmatrix}3&0\\0&2\end{pmatrix}$, eigenvalues $3,2>0$ — **unstable node**.
* $(\tfrac32,0)$: $J = \begin{pmatrix}-3&-\tfrac32\\0&\tfrac12\end{pmatrix}$, eigenvalues $-3$ and $\tfrac12$ — **saddle** ($\delta = -\tfrac32<0$).
* $(0,1)$: $J = \begin{pmatrix}2&0\\-1&-2\end{pmatrix}$, eigenvalues $2$ and $-2$ — **saddle** ($\delta = -4<0$).
* $(\tfrac43,\tfrac13)$: $J = \begin{pmatrix}-\tfrac83&-\tfrac43\\-\tfrac13&-\tfrac23\end{pmatrix}$, $\tau = -\tfrac{10}{3}<0$, $\delta = \tfrac{16}{9}-\tfrac{4}{9} = \tfrac43>0$, $\Delta = \tfrac{100}{9}-\tfrac{48}{9} = \tfrac{52}{9}>0$ — **stable node**, with eigenvalues $\frac{-5\pm\sqrt{13}}{3} \approx -0.465$ and $-2.869$.

*Check.* Each Jacobian's trace and determinant equal the sum and product of the listed eigenvalues ✓. Substituting $(\tfrac43,\tfrac13)$: $3-\tfrac83-\tfrac13 = 0$ ✓ and $2-\tfrac43-\tfrac23 = 0$ ✓.

*Ecology.* Both monocultures are saddles, so each species can invade a stand of the other; the interior equilibrium is a stable node, so the species **coexist** at $(4/3,\,1/3)$, with species $x$ the more abundant. There is no bistability here: whatever the (positive) initial densities, the outcome is the same coexistence state.

### Solution 22

$V(x,y) = x^2+y^2$ is a polynomial, hence $C^1$; $V(0,0) = 0$ and $V>0$ elsewhere, so it is positive definite. Along solutions,

$$\dot V = \frac{\partial V}{\partial x}x'+\frac{\partial V}{\partial y}y' = 2x(-x+2y)+2y(-2x-y) = -2x^2+4xy-4xy-2y^2 = -2\left(x^2+y^2\right) = -2V .$$

Since $\dot V<0$ for $(x,y)\ne(0,0)$, $V$ is a strict Lyapunov function and Theorem 7.14(2) gives **asymptotic stability** of the origin.

*Check.* The claim is consistent with the linear analysis: $\tau = -2$, $\delta = 2$, $\Delta<0$, so the eigenvalues are $-1\pm i$ with negative real part, a stable spiral. Integrating the identity $\dot V = -2V$ gives $V(t) = V(0)e^{-2t}$, i.e. $r(t) = r_0e^{-t}$, an exponential decay at the rate predicted by $\operatorname{Re}\lambda = -1$.

### Solution 23

$V = \frac12(x^2+y^2)$ is positive definite and $C^1$. Along solutions,

$$\dot V = x\,y + y\left(-x-y^3\right) = xy-xy-y^4 = -y^4\le0 .$$

By Theorem 7.14(1) the origin is **stable**. For asymptotic stability, apply LaSalle's invariance principle. The set where $\dot V = 0$ is $\{y = 0\}$. If an orbit stays in this set, then $y\equiv0$, hence $y'\equiv0$, and the second equation gives $-x-0 = 0$, i.e. $x\equiv0$. So the largest invariant subset of $\{\dot V = 0\}$ is $\{(0,0)\}$.

The orbit is bounded because $V$ is non-increasing, so its $\omega$-limit set is nonempty, compact and invariant; by LaSalle it lies in $\{(0,0)\}$, hence $\mathbf{x}(t)\to\mathbf{0}$.

*Check.* Linearising: $J = \begin{pmatrix}0&1\\-1&-3y^2\end{pmatrix}_{(0,0)} = \begin{pmatrix}0&1\\-1&0\end{pmatrix}$, eigenvalues $\pm i$ — a **centre**. The linearisation is inconclusive, which is exactly why the Lyapunov argument is needed; it shows that the cubic term makes the origin asymptotically stable, in contrast to the linear centre. (A centre is only linearly neutral; the nonlinearity here supplies the missing dissipation.)

## Advanced

### Solution 24

*Strategy: prove uniform convergence of the series and of its formal derivative, then invoke the theorem on term-by-term differentiation.*

Let $M = \lVert A\rVert$ and fix $T>0$. For $|t|\le T$ and $k\ge1$,

$$\left\lVert\frac{A^kt^k}{k!}\right\rVert \le \frac{M^kT^k}{k!}, \qquad \left\lVert\frac{kA^kt^{k-1}}{k!}\right\rVert = \left\lVert\frac{A^kt^{k-1}}{(k-1)!}\right\rVert\le\frac{M^kT^{k-1}}{(k-1)!}.$$

The series $\sum M^kT^k/k! = e^{MT}$ and $\sum M^kT^{k-1}/(k-1)! = Me^{MT}$ both converge. By the Weierstrass $M$-test, the series for $e^{At}$ converges uniformly on $[-T,T]$, and so does the series of term-by-term derivatives. Since every term is $C^1$ and the derivative series converges uniformly, the standard theorem permits differentiating term by term:

$$\frac{d}{dt}e^{At} = \sum_{k=1}^{\infty}\frac{kA^kt^{k-1}}{k!} = A\sum_{k=1}^{\infty}\frac{A^{k-1}t^{k-1}}{(k-1)!} = A\sum_{j=0}^{\infty}\frac{A^jt^j}{j!} = Ae^{At}.$$

*Check.* The same argument with $A$ replaced by $A^2$ shows that the derivative itself is differentiable, so $e^{At}$ is $C^\infty$ and $e^{At}$ solves $\Phi' = A\Phi$ with $\Phi(0) = I$; by uniqueness it is the principal fundamental matrix. For $n=1$, $A = a$, the statement reduces to $\frac{d}{dt}e^{at} = ae^{at}$ ✓.

### Solution 25

*Strategy: multiply the two absolutely convergent series and rearrange.*

For fixed $s,t$, the double series $\sum_{k,j\ge0}\frac{A^kt^k}{k!}\frac{A^js^j}{j!}$ is absolutely convergent because

$$\sum_{k,j\ge0}\frac{\lVert A\rVert^{k+j}|t|^k|s|^j}{k!\,j!} = e^{\lVert A\rVert(|t|+|s|)}<\infty .$$

Hence it may be rearranged arbitrarily, and grouping by $m = k+j$ gives

$$e^{At}e^{As} = \sum_{m\ge0}\frac{A^m}{m!}\sum_{k=0}^{m}\binom{m}{k}t^ks^{m-k} = \sum_{m\ge0}\frac{A^m(t+s)^m}{m!} = e^{A(t+s)},$$

where the inner sum is the binomial theorem (legitimate because $A^kt^ k$ and $A^js^j$ are powers of the *same* matrix $A$, hence commute).

Setting $s = -t$ gives $e^{At}e^{-At} = e^{A\cdot0} = I$, so $e^{At}$ is invertible with inverse $e^{-At}$.

*Where absolute convergence is used:* in the rearrangement of the double series and in the binomial grouping; without it the order of summation would not be interchangeable. Note that the argument never needs $A$ to commute with anything except itself.

*Check.* With $A = \begin{pmatrix}2&0\\0&-3\end{pmatrix}$, $e^{At} = \operatorname{diag}(e^{2t},e^{-3t})$ and $e^{At}e^{As} = \operatorname{diag}(e^{2(t+s)},e^{-3(t+s)}) = e^{A(t+s)}$ ✓.

### Solution 26

*Powers.* $A^2 = \begin{pmatrix}0&1\\0&0\end{pmatrix}^2 = 0$ and $B^2 = \begin{pmatrix}0&0\\1&0\end{pmatrix}^2 = 0$, so

$$e^{A} = I+A = \begin{pmatrix}1&1\\0&1\end{pmatrix}, \qquad e^{B} = I+B = \begin{pmatrix}1&0\\1&1\end{pmatrix}.$$

*Product.* $e^{A}e^{B} = \begin{pmatrix}2&1\\1&1\end{pmatrix}$.

*Sum.* $A+B = \begin{pmatrix}0&1\\1&0\end{pmatrix}$ satisfies $(A+B)^2 = I$, so the even and odd parts of the series sum separately:

$$e^{A+B} = \cosh(1)I + \sinh(1)(A+B) = \begin{pmatrix}\cosh 1 & \sinh 1\\ \sinh 1 & \cosh 1\end{pmatrix}\approx\begin{pmatrix}1.5431&1.1752\\1.1752&1.5431\end{pmatrix}.$$

These are different: for instance $e^Ae^B$ has top-left entry $2$, while $e^{A+B}$ has top-left entry $\cosh 1\approx1.543$.

*Which hypothesis fails.* $AB = \begin{pmatrix}1&0\\0&0\end{pmatrix}$ but $BA = \begin{pmatrix}0&0\\0&1\end{pmatrix}$, so $AB\ne BA$. The binomial theorem for $(A+B)^m$ is exactly what fails: the cross terms $AB$ and $BA$ do not combine into $2AB$.

*Check.* $\det e^{A+B} = \cosh^2 1-\sinh^2 1 = 1 = e^{\operatorname{tr}(A+B)} = e^0$ ✓, and $\det(e^Ae^B) = 1\cdot1 = 1$ ✓ — both are consistent with Theorem 7.9(5), which does not require commutativity.

### Solution 27

*(a) By triangularisation.* Over $\mathbb{C}$ every matrix is similar to an upper triangular matrix $T$ (Schur triangularisation), and the diagonal entries of $T$ are the eigenvalues $\lambda_1,\dots,\lambda_n$. If $A = PTP^{-1}$, then $A^k = PT^kP^{-1}$ and

$$e^{At} = Pe^{Tt}P^{-1}.$$

Powers of an upper triangular matrix are upper triangular, with diagonal entries $\lambda_i^k$; hence $e^{Tt}$ is upper triangular with diagonal entries $\sum_k(\lambda_it)^k/k! = e^{\lambda_it}$. Therefore

$$\det e^{At} = \det e^{Tt} = \prod_{i=1}^{n}e^{\lambda_it} = \exp\left(t\sum_i\lambda_i\right) = e^{t\operatorname{tr}A},$$

using $\operatorname{tr}A = \sum_i\lambda_i$ (the trace is the sum of the roots of the characteristic polynomial).

*(b) By Abel's formula.* $\Phi(t) = e^{At}$ is a fundamental matrix with $\Phi(0) = I$, so Theorem 7.6 gives

$$\det\Phi(t) = \det\Phi(0)\exp\left(\int_0^t\operatorname{tr}A\,ds\right) = 1\cdot e^{t\operatorname{tr}A}.$$

*Check.* For $A = \begin{pmatrix}1&1\\0&2\end{pmatrix}$, $e^{At} = \begin{pmatrix}e^t&e^{2t}-e^t\\0&e^{2t}\end{pmatrix}$, so $\det = e^{3t} = e^{t\operatorname{tr}A}$ ✓.

### Solution 28

*Strategy: differentiate along the solution and dominate by the slowest exponential.*

Let $\alpha = \max_i\operatorname{Re}\lambda_i<0$. In Jordan form $A = PJP^{-1}$, and each block of size $m$ contributes entries $t^ke^{\lambda_it}/k!$ with $0\le k\le m-1$. Hence there is a constant $K$ with

$$\left\lVert e^{Jt}\right\rVert\le K(1+t)^{n-1}e^{\alpha t}\qquad(t\ge0).$$

Choose $\mu$ with $0<\mu<-\alpha$. The function $t\mapsto(1+t)^{n-1}e^{(\alpha+\mu)t}$ is continuous on $[0,\infty)$ and tends to $0$ as $t\to\infty$ (because $\alpha+\mu<0$), so it is bounded by some $C_1$. Thus

$$\left\lVert e^{At}\right\rVert\le\lVert P\rVert\,\lVert P^{-1}\rVert\,K\,C_1e^{-\mu t} =: Ce^{-\mu t}.$$

Consequently, for any $\mathbf{x}_0$,

$$\left\lVert\mathbf{x}(t)\right\rVert = \left\lVert e^{At}\mathbf{x}_0\right\rVert\le Ce^{-\mu t}\lVert\mathbf{x}_0\rVert\longrightarrow0,$$

which is asymptotic stability (stability itself follows from $\lVert\mathbf{x}(t)\rVert\le C\lVert\mathbf{x}_0\rVert$ near $t=0$; more simply, choose $\delta = \varepsilon/C$).

*Check.* For $A = \begin{pmatrix}-1&1\\0&-2\end{pmatrix}$, $\alpha = -1$ and $e^{At} = \begin{pmatrix}e^{-t}&e^{-t}-e^{-2t}\\0&e^{-2t}\end{pmatrix}$ has $\lVert e^{At}\rVert\le 3e^{-t}$ for $t\ge0$, so $C = 3$, $\mu = 1$ ✓.

### Solution 29

*(⇒)* Suppose $\mathbf{x}(t)$ is a nonconstant solution with period $T>0$.

*Distinct real eigenvalues $\lambda_1\ne\lambda_2$.* Then $\mathbf{x}(t) = c_1e^{\lambda_1t}\mathbf{v}_1+c_2e^{\lambda_2t}\mathbf{v}_2$. Periodicity at $t=0$ gives $c_1(e^{\lambda_1T}-1)\mathbf{v}_1+c_2(e^{\lambda_2T}-1)\mathbf{v}_2 = \mathbf{0}$; by independence, $c_i(e^{\lambda_iT}-1) = 0$ for each $i$. If $c_i\ne0$ then $\lambda_i = 0$. Since $\lambda_1\ne\lambda_2$, at most one $c_i$ is nonzero; then $\mathbf{x} = c_i\mathbf{v}_i$ is constant, contradicting nonconstancy.

*Repeated eigenvalue $\lambda$.* If $A = \lambda I$, $\mathbf{x} = e^{\lambda t}\mathbf{x}_0$ is periodic only when $\lambda = 0$ (constant) or $\mathbf{x}_0 = \mathbf{0}$. If $A$ is defective, $\mathbf{x}(t) = e^{\lambda t}(c_1\mathbf{v}+c_2(\mathbf{u}+t\mathbf{v}))$; periodicity forces $c_2 = 0$ and $e^{\lambda T} = 1$, so $\lambda = 0$ and again $\mathbf{x}$ is constant.

*Complex eigenvalues $\alpha\pm i\beta$, $\beta\ne0$.* The general solution is $e^{\alpha t}$ times a $2\pi/\beta$-periodic vector. Periodicity forces $e^{\alpha T} = 1$, hence $\alpha = 0$. Then $\tau = 2\alpha = 0$ and $\delta = \alpha^2+\beta^2 = \beta^2>0$.

*Degenerate case $\delta = 0$.* One eigenvalue is $0$ and the other is $\tau$; if $\tau\ne0$ the nonzero mode is exponential and cannot be periodic; if $\tau = 0$ then $A^2 = 0$ and $\mathbf{x}(t) = \mathbf{x}_0+tA\mathbf{x}_0$, periodic only if $A\mathbf{x}_0 = \mathbf{0}$, i.e. constant.

In every case a nonconstant periodic solution forces $\tau = 0$ and $\delta>0$.

*(⇐)* If $\tau = 0$ and $\delta>0$ then $\Delta = -4\delta<0$ and the eigenvalues are $\pm i\sqrt\delta$ with $\sqrt\delta>0$. A real $2\times2$ matrix with eigenvalues $\pm i\beta$ is similar to $\begin{pmatrix}0&-\beta\\ \beta&0\end{pmatrix}$, whose exponential is $\begin{pmatrix}\cos\beta t&-\sin\beta t\\ \sin\beta t&\cos\beta t\end{pmatrix}$, of period $2\pi/\beta$. Hence every solution is periodic with that period.

*Check.* $A = \begin{pmatrix}0&-2\\2&0\end{pmatrix}$: $\tau = 0$, $\delta = 4$, solutions have period $\pi$, and indeed $e^{At} = \begin{pmatrix}\cos 2t&-\sin 2t\\ \sin 2t&\cos 2t\end{pmatrix}$ ✓.

### Solution 30

Let $\varepsilon>0$. Shrinking $U$ if necessary, assume $\overline{B_\varepsilon(\mathbf{0})}\subseteq U$. The boundary sphere $S_\varepsilon = \{\lVert\mathbf{x}\rVert = \varepsilon\}$ is compact and $V>0$ on it, so

$$m := \min_{\mathbf{x}\in S_\varepsilon}V(\mathbf{x})>0 .$$

Since $V(\mathbf{0}) = 0$ and $V$ is continuous at $\mathbf{0}$, there is $\delta\in(0,\varepsilon)$ with $V(\mathbf{x})<m$ whenever $\lVert\mathbf{x}\rVert<\delta$.

Now take $\mathbf{x}_0$ with $\lVert\mathbf{x}_0\rVert<\delta$ and let $\mathbf{x}(t)$ be the maximal solution with $\mathbf{x}(0) = \mathbf{x}_0$, defined on $[0,T_{\max})$. For $t\in[0,T_{\max})$,

$$\frac{d}{dt}V(\mathbf{x}(t)) = \nabla V(\mathbf{x}(t))\cdot\mathbf{x}'(t) = \nabla V(\mathbf{x}(t))\cdot\mathbf{f}(\mathbf{x}(t)) = \dot V(\mathbf{x}(t))\le0,$$

so $t\mapsto V(\mathbf{x}(t))$ is non-increasing and

$$V(\mathbf{x}(t))\le V(\mathbf{x}_0)<m \qquad\text{for all } t\in[0,T_{\max}).$$

If for some $t$ we had $\lVert\mathbf{x}(t)\rVert = \varepsilon$, then $V(\mathbf{x}(t))\ge m$, a contradiction. By continuity of $t\mapsto\lVert\mathbf{x}(t)\rVert$ and the fact that it starts below $\varepsilon$, it can never reach $\varepsilon$; hence $\lVert\mathbf{x}(t)\rVert<\varepsilon$ for all $t\in[0,T_{\max})$. In particular the orbit stays in the compact set $\overline{B_\varepsilon}$, so by the extension theorem $T_{\max} = +\infty$.

Since $\varepsilon>0$ was arbitrary, for every $\varepsilon$ there is $\delta$ with $\lVert\mathbf{x}_0\rVert<\delta\Rightarrow\lVert\mathbf{x}(t)\rVert<\varepsilon$ for all $t\ge0$: the origin is Lyapunov stable. $\blacksquare$

*Check of the logic.* The proof uses only: compactness of the sphere, continuity of $V$ at the origin, and $\dot V\le0$. It does **not** need $\dot V<0$, which is why a centre (with $V = r^2$ and $\dot V = 0$) is stable. It also does not prove attraction: for a centre, $V$ stays constant and the orbit never reaches the origin.

### Solution 31

*Strategy: change to the eigenbasis, where the system is diagonal, and read off the coordinates.*

Let $\mathbf{v}_1,\mathbf{v}_2$ be eigenvectors for $\lambda_1<0<\lambda_2$; they are independent, so $P = (\mathbf{v}_1\ \mathbf{v}_2)$ is invertible. Put $\mathbf{x} = P\mathbf{y}$. Then

$$\mathbf{y}' = P^{-1}AP\mathbf{y} = \begin{pmatrix}\lambda_1&0\\0&\lambda_2\end{pmatrix}\mathbf{y}, \qquad y_1(t) = c_1e^{\lambda_1t},\quad y_2(t) = c_2e^{\lambda_2t}.$$

The map $\mathbf{x}\mapsto P\mathbf{y}$ is a linear bijection, so it preserves boundedness in both directions.

*Bounded as $t\to+\infty$.* If $c_2\ne0$, then $|y_2(t)| = |c_2|e^{\lambda_2t}\to\infty$. Hence boundedness forces $c_2 = 0$, i.e. $y_2\equiv0$, which is the $\mathbf{v}_1$-axis — the stable eigenline. Conversely every point with $c_2 = 0$ gives $y_1 = c_1e^{\lambda_1t}\to0$, which is bounded.

*Bounded as $t\to-\infty$.* If $c_1\ne0$, then $|y_1(t)| = |c_1|e^{\lambda_1t}\to\infty$ as $t\to-\infty$ (since $\lambda_1<0$). Hence boundedness forces $c_1 = 0$: the unstable eigenline.

*All other orbits.* If $c_1c_2\ne0$, then $|y_2|\to\infty$ as $t\to+\infty$ and $|y_1|\to\infty$ as $t\to-\infty$; the orbit is unbounded in each direction (in the eigen-coordinates, hence in the original ones). If one coefficient vanishes, the orbit lies on an eigenline and is unbounded in exactly one direction (away from the origin).

*The four special orbits.* The two half-lines of the stable eigenline are the only orbits with $\mathbf{x}(t)\to\mathbf{0}$ as $t\to+\infty$; the two half-lines of the unstable eigenline the only ones with $\mathbf{x}(t)\to\mathbf{0}$ as $t\to-\infty$. These are $W^{s}$ and $W^{u}$ of Theorem 7.17, and in the linear case they are exactly the eigenlines. $\blacksquare$

*Check.* $A = \begin{pmatrix}1&2\\3&2\end{pmatrix}$ has $\lambda_1 = -1<0<\lambda_2 = 4$; the orbit $c_1e^{-t}(1,-1)+c_2e^{4t}(2,3)$ with both coefficients nonzero leaves along $(2,3)$ as $t\to\infty$ and along $(1,-1)$ as $t\to-\infty$ ✓.

## Challenge

### Solution 32

*Part 1: the $3\times3$ matrix.* $A = -I+N$ with $N = \begin{pmatrix}0&1&0\\0&0&1\\0&0&0\end{pmatrix}$, $N^2 = \begin{pmatrix}0&0&1\\0&0&0\\0&0&0\end{pmatrix}$, $N^3 = 0$. Since $-I$ commutes with $N$,

$$e^{At} = e^{-t}\left(I+tN+\frac{t^2}{2}N^2\right) = e^{-t}\begin{pmatrix}1&t&t^2/2\\0&1&t\\0&0&1\end{pmatrix}.$$

*Part 2: the general Jordan block.* Let $N$ be the $m\times m$ matrix with ones on the superdiagonal and zeros elsewhere. Then $N^k$ has ones on the $k$-th superdiagonal and zeros elsewhere (induction: $(N^k)_{ij} = 1$ iff $j-i = k$), and $N^m = 0$. Because $\lambda I$ commutes with $N$,

$$e^{Jt} = e^{(\lambda I+N)t} = e^{\lambda t}e^{Nt} = e^{\lambda t}\sum_{k=0}^{\infty}\frac{t^kN^k}{k!} = e^{\lambda t}\sum_{k=0}^{m-1}\frac{t^k}{k!}N^k,$$

the last equality because $N^k = 0$ for $k\ge m$. Explicitly, the $(i,j)$ entry is $e^{\lambda t}\dfrac{t^{j-i}}{(j-i)!}$ when $j\ge i$ and $0$ otherwise.

*Verification.* For $m=2$, $e^{Jt} = e^{\lambda t}\begin{pmatrix}1&t\\0&1\end{pmatrix}$, whose derivative is $e^{\lambda t}\begin{pmatrix}\lambda&1+\lambda t\\0&\lambda\end{pmatrix}$, while

$$Je^{Jt} = e^{\lambda t}\begin{pmatrix}\lambda&1\\0&\lambda\end{pmatrix}\begin{pmatrix}1&t\\0&1\end{pmatrix} = e^{\lambda t}\begin{pmatrix}\lambda&1+\lambda t\\0&\lambda\end{pmatrix} ✓.$$

For $m=3$ with $\lambda = -1$, the derivative of the first row $(e^{-t}, te^{-t}, \tfrac{t^2}{2}e^{-t})$ is $e^{-t}(-1, 1-t, t-\tfrac{t^2}{2})$, and $A e^{At}$ has first row $e^{-t}(-1\cdot1 + 1\cdot t,\ -1\cdot t + 1\cdot1,\ -1\cdot\tfrac{t^2}{2}+1\cdot t)$ — the same ✓.

### Solution 33

*Part (a): the interior equilibrium is a stable node.* At $(x,y) = (\tfrac43,\tfrac13)$,

$$J = \begin{pmatrix}3-4x-y&-x\\-y&2-x-4y\end{pmatrix} = \begin{pmatrix}-\tfrac83&-\tfrac43\\-\tfrac13&-\tfrac23\end{pmatrix}.$$

$\tau = -\tfrac{10}{3}<0$, $\delta = \tfrac{16}{9}-\tfrac{4}{9} = \tfrac43>0$, $\Delta = \tfrac{100}{9}-\tfrac{48}{9} = \tfrac{52}{9}>0$, so the eigenvalues are real, distinct and negative: $\frac{-5\pm\sqrt{13}}{3}\approx-0.465$ and $-2.869$. A stable node.

*Part (b): the axial equilibria are saddles.* $J(\tfrac32,0) = \begin{pmatrix}-3&-\tfrac32\\0&\tfrac12\end{pmatrix}$ has eigenvalues $-3,\tfrac12$ and $J(0,1) = \begin{pmatrix}2&0\\-1&-2\end{pmatrix}$ has eigenvalues $2,-2$; both have $\delta<0$.

*Part (c): no periodic orbit.* Let $f_1 = x(3-2x-y)$, $f_2 = y(2-x-2y)$ and $B(x,y) = \dfrac{1}{xy}>0$ on the open quadrant. Then

$$\frac{\partial(Bf_1)}{\partial x}+\frac{\partial(Bf_2)}{\partial y} = \frac{\partial}{\partial x}\left(\frac{3-2x-y}{y}\right)+\frac{\partial}{\partial y}\left(\frac{2-x-2y}{x}\right) = -\frac{2}{y}-\frac{2}{x}<0 .$$

The divergence has one sign and does not vanish, so by the Bendixson–Dulac criterion there is **no** periodic orbit in the open first quadrant.

*Part (d): convergence.* First, orbits are eventually trapped in the rectangle $R = [0,\tfrac32]\times[0,1]$. On $x = \tfrac32$: $x' = \tfrac32(3-3-y) = -\tfrac32y\le0$. On $y = 1$: $y' = 1\cdot(2-x-2) = -x\le0$. On the axes the flow is tangent. So $R$ is positively invariant. Moreover, outside $R$: if $x>\tfrac32$ then $x' = x(3-2x-y)<0$, so $x$ decreases; if $y>1$ then $y' = y(2-x-2y)<0$, so $y$ decreases. Hence every orbit with positive data enters $R$ and stays there.

By the Poincaré–Bendixson theorem, the $\omega$-limit set of such an orbit is either an equilibrium or a closed orbit; closed orbits are excluded by Part (c). The equilibria in $R$ are $(0,0)$, $(\tfrac32,0)$, $(0,1)$ and $(\tfrac43,\tfrac13)$. The origin is an unstable node, so it cannot be an $\omega$-limit set of a nearby orbit. The stable eigenvector at $(\tfrac32,0)$ is $(1,0)$ (from $(J+3I)\mathbf{v} = \begin{pmatrix}0&-\tfrac32\\0&\tfrac72\end{pmatrix}\mathbf{v} = \mathbf{0}$), i.e. the $x$-axis, and the stable eigenvector at $(0,1)$ is $(0,1)$ (from $(J+2I)\mathbf{v} = \begin{pmatrix}4&0\\-1&0\end{pmatrix}\mathbf{v} = \mathbf{0}$), i.e. the $y$-axis. An orbit with $x>0,y>0$ cannot lie on an axis, so neither saddle is an $\omega$-limit set either.

The only remaining equilibrium is the stable node $(\tfrac43,\tfrac13)$, so every orbit with $x_0>0$, $y_0>0$ converges to it. $\blacksquare$

*Check.* The divergence computation: $\partial_x[(3-2x-y)/y] = -2/y$ ✓ and $\partial_y[(2-x-2y)/x] = -2/x$ ✓. The conclusion agrees with Part (a): the node is attracting, and the Dulac argument rules out the alternative that orbits circulate forever.

### Solution 34

*Part (a): the fundamental matrix.* Solve componentwise. $y' = 2y$ gives $y = c_2e^{2t}$. Then

$$x' = x+ty = x+c_2te^{2t}, \qquad\text{so}\qquad \left(xe^{-t}\right)' = c_2te^{t},$$

using the integrating factor $e^{-t}$. Since $\int te^t\,dt = (t-1)e^t$, we get $xe^{-t} = c_2(t-1)e^{t}+c_1$, i.e.

$$x = c_1e^{t}+c_2(t-1)e^{2t}.$$

With $(x,y)(0) = (x_0,y_0)$: $y_0 = c_2$ and $x_0 = c_1-c_2$, so $c_1 = x_0+y_0$ and

$$x = (x_0+y_0)e^{t}+y_0(t-1)e^{2t}.$$

The columns for $(1,0)$ and $(0,1)$ give

$$\Phi(t) = \begin{pmatrix}e^{t} & e^{t}+(t-1)e^{2t}\\ 0&e^{2t}\end{pmatrix}, \qquad \Phi(0) = \begin{pmatrix}1&1-1\\0&1\end{pmatrix} = I ✓.$$

*Part (b): the exponential of the integral.* $\int_0^tA(s)\,ds = \begin{pmatrix}t&t^2/2\\0&2t\end{pmatrix}$. For an upper triangular matrix $\begin{pmatrix}a&b\\0&c\end{pmatrix}$ with $a\ne c$ one has $\exp = \begin{pmatrix}e^a & b\dfrac{e^c-e^a}{c-a}\\0&e^c\end{pmatrix}$ (verify by solving $\alpha' = a\alpha$, $\beta' = a\beta+b e^{ct}$), so

$$\exp\left(\int_0^tA\right) = \begin{pmatrix}e^{t} & \dfrac{t^2}{2}\cdot\dfrac{e^{2t}-e^{t}}{t}\\ 0&e^{2t}\end{pmatrix} = \begin{pmatrix}e^{t} & \dfrac{t}{2}\left(e^{2t}-e^{t}\right)\\ 0&e^{2t}\end{pmatrix}.$$

This differs from $\Phi(t)$ (compare the top-right entries: $e^t+(t-1)e^{2t}$ versus $\tfrac t2(e^{2t}-e^t)$; at $t=1$ they are $e\approx2.718$ and $\tfrac12(e^2-e)\approx2.952$).

*Direct check that it is not a fundamental matrix.* Let $E(t) = \exp\left(\int_0^tA\right)$ with top-right entry $\tfrac t2(e^{2t}-e^t)$. Then

$$E'-AE = \begin{pmatrix}0&\frac{d}{dt}\left[\frac t2(e^{2t}-e^t)\right]-\left[\frac t2(e^{2t}-e^t)+te^{2t}\right]\\0&0\end{pmatrix}\ne0,$$

since the bracket is $\frac12(e^{2t}-e^t)+\frac t2(2e^{2t}-e^t) - \frac t2(e^{2t}-e^t) - te^{2t} = \frac12(e^{2t}-e^t) \ne 0$. So $E$ does not solve $\Phi' = A\Phi$.

*Part (c): which hypothesis fails.* The identity $e^{\int A} = \Phi$ would follow from Theorem 7.9(3) only if the matrices $A(s)$ commuted with $\int_0^tA(s)ds$ — and, more fundamentally, the theorem is about *constant* matrices. Here $A(t)$ does not commute with $A(s)$ for $s\ne t$: $A(t)A(s)\ne A(s)A(t)$ when the off-diagonal entry $t$ is nonzero (compute $[A(t),A(s)] = (s-t)\begin{pmatrix}0&-1\\0&0\end{pmatrix}$). For non-commuting matrices the exponent of the integral is not the fundamental matrix; the correct object is the time-ordered exponential.

*Check.* The computed $\Phi$ satisfies $\Phi(0) = I$ and $\Phi' = A\Phi$ (verified by construction); the alternative $E$ fails already at first order. The lesson is that Theorem 7.9(3) is a statement about one matrix, not a recipe for non-autonomous systems.

### Solution 35

*Proof.* Put $A$ in Jordan form $A = PJP^{-1}$ with blocks $J_j = \lambda_jI+N_j$ of size $m_j$. Then

$$e^{At} = Pe^{Jt}P^{-1}, \qquad \left(e^{J_jt}\right)_{rs} = \begin{cases}\dfrac{t^{r-s}}{(r-s)!}e^{\lambda_jt}, & r\ge s,\\[2mm] 0, & r<s.\end{cases}$$

Boundedness of all solutions on $\mathbb{R}$ is invariant under the similarity $P$ (since $P$ and $P^{-1}$ are fixed), so $e^{Jt}$ must be bounded on $\mathbb{R}$.

*Eigenvalues on the imaginary axis.* If $\operatorname{Re}\lambda_j>0$, the diagonal entry $e^{\lambda_jt}$ is unbounded as $t\to+\infty$. If $\operatorname{Re}\lambda_j<0$, it is unbounded as $t\to-\infty$. Since the entries of a bounded matrix are bounded, $\operatorname{Re}\lambda_j = 0$ for every $j$.

*No Jordan blocks of size $\ge2$.* If $m_j\ge2$, the entry $(1,2)$ equals $te^{\lambda_jt}$, whose modulus $|t|$ is unbounded as $t\to\pm\infty$. So every $m_j = 1$, i.e. $A$ is diagonalisable over $\mathbb{C}$.

*Example showing $[0,\infty)$ is weaker.* $A = -I$: every solution is $\mathbf{x}_0e^{-t}$, bounded on $[0,\infty)$, but the eigenvalue $-1$ has negative real part, so $A$ is not of the purely imaginary type. More dramatically, $A = \begin{pmatrix}-1&1\\0&-1\end{pmatrix}$ has a Jordan block of size $2$ with $\operatorname{Re}\lambda = -1$; its exponential $\begin{pmatrix}e^{-t}&te^{-t}\\0&e^{-t}\end{pmatrix}$ is bounded on $[0,\infty)$ but not diagonalisable and unbounded as $t\to-\infty$.

*Where $t\to-\infty$ is used.* In the first bullet ($\operatorname{Re}\lambda<0$ gives unboundedness only in the past) and in the second ($te^{\lambda t}$ with $\operatorname{Re}\lambda = 0$ is unbounded in *both* directions, but with $\operatorname{Re}\lambda<0$ it is unbounded only as $t\to-\infty$). Boundedness on the half-line therefore constrains only positive real parts, not negative ones.

*Check.* $A = \begin{pmatrix}0&-1\\1&0\end{pmatrix}$ is diagonalisable with eigenvalues $\pm i$; $e^{At}$ is a rotation matrix, bounded on $\mathbb{R}$ ✓. $A = \begin{pmatrix}0&1\\0&0\end{pmatrix}$ is nilpotent with eigenvalue $0$ but defective; $e^{At} = I+At = \begin{pmatrix}1&t\\0&1\end{pmatrix}$ is unbounded ✓.

### Solution 36

*(a) Polar form.* With $x = r\cos\theta$, $y = r\sin\theta$ and $f_1 = -y+x(x^2+y^2)$, $f_2 = x+y(x^2+y^2)$,

$$r\dot r = x\dot x+y\dot y = x\left(-y+xr^2\right)+y\left(x+yr^2\right) = -xy+xy+r^2(x^2+y^2) = r^4,$$

$$r^2\dot\theta = x\dot y-y\dot x = x\left(x+yr^2\right)-y\left(-y+xr^2\right) = x^2+y^2+xy r^2 - xy r^2 = r^2 .$$

For $r>0$: $\dot r = r^3$ and $\dot\theta = 1$ ✓.

*(b) Linearisation.* $D\mathbf{f}(\mathbf{0}) = \begin{pmatrix}\partial_xf_1&\partial_yf_1\\ \partial_xf_2&\partial_yf_2\end{pmatrix}_{\mathbf{0}}$. Since $\partial_x f_1 = (x^2+y^2)+2x^2 = 3x^2+y^2$, $\partial_yf_1 = -1+2xy$, $\partial_xf_2 = 1+2xy$, $\partial_yf_2 = 3y^2+x^2$, at the origin

$$J = \begin{pmatrix}0&-1\\1&0\end{pmatrix}, \qquad \text{eigenvalues } \pm i .$$

So the linearisation is a centre.

*(c) Solving the nonlinear system.* $\dot r = r^3$ separates: $\int r^{-3}dr = t+C$, so $-\frac{1}{2r^2} = t+C$ and

$$r(t) = \frac{r_0}{\sqrt{1-2r_0^2t}}, \qquad \theta(t) = \theta_0+t,$$

for $0\le t<1/(2r_0^2)$. The radius increases monotonically and blows up at the finite time $t_* = 1/(2r_0^2)$: the origin is an **unstable spiral** (an outward spiral that escapes to infinity in finite time), not a centre.

*(d) The role of hyperbolicity.* Hartman–Grobman requires that no eigenvalue of the Jacobian has zero real part. Here the eigenvalues are $\pm i$, exactly on the boundary, so the theorem is silent — and indeed the nonlinear portrait (expanding spiral) is qualitatively different from the linear one (closed circles). The example shows that a centre is a genuine borderline case: the smallest nonlinear perturbation can turn it into a stable or an unstable spiral, and the linearisation cannot decide which.

*Check.* Differentiate $r^2 = r_0^2/(1-2r_0^2t)$: $\frac{d}{dt}r^2 = 2r_0^4/(1-2r_0^2t)^2 = 2r^4$ ✓, so $2r\dot r = 2r^4$ and $\dot r = r^3$ ✓. And $x = r\cos\theta$ with $\theta = t$ reproduces $x' = -y+xr^2$ by construction from the polar computation ✓.
