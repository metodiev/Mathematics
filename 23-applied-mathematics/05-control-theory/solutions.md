# Control Theory — Solutions

> [Control Theory](README.md) · Solutions to the 36 problems in [exercises.md](exercises.md)

Each solution gives the strategy, every significant step and a check. Matrices act on column vectors;
$I$ is the identity of the appropriate size.

## Beginner

**1.** *(Strategy: the phase variables are position and velocity.)*

Set $x_1=x$, $x_2=\dot x$. Then $\dot x_1=x_2$ and, from the ODE, $\dot x_2=-2x_1-3x_2+u$. With $y=x_1$,

$$A=\begin{bmatrix}0&1\\-2&-3\end{bmatrix}, \qquad B=\begin{bmatrix}0\\1\end{bmatrix}, \qquad
C=\begin{bmatrix}1&0\end{bmatrix}, \qquad D=0.$$

*Check.* $\ddot x = \dot x_2 = -2x-3\dot x+u$, which is the original ODE ✓.

**2.** *(Strategy: characteristic polynomial.)*

$\det(\lambda I-A) = \lambda(\lambda+3)+2 = \lambda^2+3\lambda+2 = (\lambda+1)(\lambda+2)$. The eigenvalues
are $-1$ and $-2$, both with negative real part, so the equilibrium is asymptotically stable.

*Check.* Both roots are real and negative; the solution is a sum of $e^{-t}$ and $e^{-2t}$ terms. ✓

**3.** *(Strategy: separate variables.)*

$\dot x=2x$ with $x(0)=1$ gives $x(t)=e^{2t}$. Since $2>0$, the solution grows without bound, so the
origin is unstable.

*Check.* The eigenvalue of $A=2$ is positive; Theorem 7.1 applies. ✓

**4.** *(Strategy: diagonal matrices exponentiate entrywise.)*

$$e^{At} = \begin{bmatrix}e^{-t}&0\\0&e^{-3t}\end{bmatrix}, \qquad
x(t) = e^{At}\begin{bmatrix}1\\2\end{bmatrix} = \begin{bmatrix}e^{-t}\\2e^{-3t}\end{bmatrix}.$$

*Check.* At $t=0$, $x=(1,2)$ ✓; both components decay, with the second faster.

**5.** *(Strategy: use the oscillator formula with $\omega=2$.)*

$$e^{At} = \begin{bmatrix}\cos2t&\tfrac12\sin2t\\-2\sin2t&\cos2t\end{bmatrix}.$$

The solution rotates in the phase plane: $4x_1^2+x_2^2$ is constant, so trajectories are ellipses about
the origin. The eigenvalues are $\pm2j$, purely imaginary and semisimple, so the origin is Lyapunov stable
but **not** asymptotically stable.

*Check.* Differentiating at $t=0$ gives $\begin{bmatrix}0&1\\-4&0\end{bmatrix}=A$ ✓.

**6.** *(Strategy: Kalman matrix.)*

$$\mathcal{C} = \begin{bmatrix}B&AB\end{bmatrix} = \begin{bmatrix}1&1\\1&2\end{bmatrix}, \qquad \det\mathcal{C}=1\ne0.$$

The rank is $2=n$, so the pair is controllable.

*Check.* The PBH test at $\lambda=1$: $[\lambda I-A\ \ B] = \begin{bmatrix}0&0&1\\0&-1&1\end{bmatrix}$ has rank
$2$; at $\lambda=2$: $\begin{bmatrix}-1&0&1\\0&0&1\end{bmatrix}$ has rank $2$ ✓.

**7.** *(Strategy: observability matrix.)*

$$\mathcal{O} = \begin{bmatrix}C\\CA\end{bmatrix} = \begin{bmatrix}1&0\\1&2\end{bmatrix}, \qquad \det\mathcal{O}=2\ne0.$$

The rank is $2=n$, so the pair is observable. Intuitively, $y=x_1$ reveals $x_1$, and $\dot y=x_1+2x_2$
then reveals $x_2$.

*Check.* The PBH test at $\lambda=3$: $[\lambda I-A;C] = \begin{bmatrix}2&-2\\0&0\\1&0\end{bmatrix}$ has rank $2$ ✓.

**8.** *(Strategy: substitute the control law into the plant.)*

(a) $1000\dot v = 450(r-v)-50v$, so

$$\dot v = -\frac{500}{1000}v + \frac{450}{1000}r = -0.5v+0.45r.$$

The closed-loop pole is $-0.5\ \mathrm{s^{-1}}$, a time constant of $2\ \mathrm{s}$.

(b) At steady state $0=-0.5v+0.45(25)$, so $v=22.5\ \mathrm{m/s}$. The error is
$25-22.5=2.5\ \mathrm{m/s}$, that is $10\%$.

*Check.* The general formula $v_\infty=Kr/(b+K)=450(25)/500=22.5$ ✓. The error $br/(b+K)=50(25)/500=2.5$ ✓.

**9.** *(Strategy: $G(s)=C(sI-A)^{-1}B+D$.)*

For scalars, $G(s)=3(s+2)^{-1}\cdot1 = \dfrac{3}{s+2}$. The pole is $-2$, the DC gain is $3/2=1.5$.

*Check.* A unit step input gives $y(t)=1.5(1-e^{-2t})$, with final value $1.5$ ✓.

**10.** *(Strategy: final-value theorem.)*

$L(s)=G(s)$ in unity feedback. $L(0)=1/2$, so for a unit step

$$e_{ss} = \frac{1}{1+L(0)} = \frac{1}{1.5} = \frac23.$$

*Check.* The closed-loop transfer function is $1/(s+3)$, whose DC gain is $1/3$; the error is $1-1/3=2/3$ ✓.

**11.** *(Strategy: Routh array.)*

$$s^3:\ 1,\ 2; \qquad s^2:\ 1,\ 8; \qquad s^1:\ \frac{1\cdot2-1\cdot8}{1}=-6,\ 0; \qquad s^0:\ 8.$$

The first column is $1,1,-6,8$ with two sign changes, so there are two right-half-plane roots and the
polynomial is not Hurwitz. The roots are $-2$ and $0.5\pm1.9365j$.

*Check.* The coefficient condition $a_2a_1=1\cdot2=2$ is not greater than $a_3a_0=8$, so the cubic test
already detects instability ✓.

**12.** *(Strategy: place the scalar closed-loop pole.)*

With $u=-Kx$, $\dot x=(1-2K)x$. Setting $1-2K=-3$ gives $K=2$.

*Check.* $1-2(2)=-3$ ✓. Positive feedback would be needed for a negative plant gain; here the plant gain
is positive, so the feedback is negative.

**13.** *(Strategy: solve $\lvert G(j\omega)\rvert=1$ and evaluate the phase.)*

$\lvert G(j\omega)\rvert = 2/\sqrt{1+\omega^2}=1$ gives $\omega_c=\sqrt3=1.732\ \mathrm{rad/s}$. The phase
is $-\arctan(\sqrt3)=-60^\circ$, so $\mathrm{PM}=180^\circ-60^\circ=120^\circ$. The phase tends to
$-90^\circ$ and never reaches $-180^\circ$, so the gain margin is infinite.

*Check.* The closed-loop characteristic polynomial is $s+1+2=s+3$, stable for all positive gain; a $120^\circ$
phase margin is consistent with a very well damped first-order loop ✓.

## Intermediate

**14.** *(Strategy: phase variables, then the transfer-function formula.)*

(a) With $x_1=x$, $x_2=\dot x$: $\dot x_2=-5x_1-2x_2+3u$, so

$$A=\begin{bmatrix}0&1\\-5&-2\end{bmatrix}, \qquad B=\begin{bmatrix}0\\3\end{bmatrix}, \qquad
C=\begin{bmatrix}1&1\end{bmatrix}, \qquad D=0.$$

(b) $sI-A = \begin{bmatrix}s&-1\\5&s+2\end{bmatrix}$ and $\det = s^2+2s+5$. Also

$$(sI-A)^{-1}B = \frac{1}{\det}\begin{bmatrix}s+2&1\\-5&s\end{bmatrix}\begin{bmatrix}0\\3\end{bmatrix}
= \frac{1}{\det}\begin{bmatrix}3\\3s\end{bmatrix}.$$

Applying $C=[1,1]$ gives $G(s)=\dfrac{3s+3}{s^2+2s+5}$. The poles are $-1\pm2j$.

(c) The real parts are $-1<0$, so the system is asymptotically stable.

*Check.* $G(0)=3/5=0.6$. Directly, $-A=\begin{bmatrix}0&-1\\5&2\end{bmatrix}$ has determinant $5$ and
inverse $\frac15\begin{bmatrix}2&1\\-5&0\end{bmatrix}=\begin{bmatrix}0.4&0.2\\-1&0\end{bmatrix}$; then
$C(-A)^{-1}B=[1,1]\begin{bmatrix}0.4&0.2\\-1&0\end{bmatrix}\begin{bmatrix}0\\3\end{bmatrix}=[1,1]\begin{bmatrix}0.6\\0\end{bmatrix}=0.6$ ✓.

**15.** *(Strategy: the matrix is a Jordan block, so use the nilpotent part.)*

$A+I = \begin{bmatrix}1&1\\-1&-1\end{bmatrix}$ and $(A+I)^2=0$. Hence
$e^{At}=e^{-t}e^{(A+I)t}=e^{-t}\bigl[I+(A+I)t\bigr]$, that is

$$e^{At}=e^{-t}\begin{bmatrix}1+t&t\\-t&1-t\end{bmatrix}.$$

It is not diagonal times an exponential because $A$ is not diagonalisable: it has a repeated eigenvalue
with a single eigenvector, which produces the factor $(1+t)$.

*Check.* At $t=0$ this is $I$; the derivative at $t=0$ is
$\frac{d}{dt}[e^{-t}(I+(A+I)t)]_{0} = -I+(A+I)=A$ ✓.

**16.** *(Strategy: write the symmetric system and solve.)*

Let $P=\begin{bmatrix}p&q\\q&r\end{bmatrix}$. With $A=\begin{bmatrix}0&1\\-1&-2\end{bmatrix}$ and
$A^{\mathsf T}=\begin{bmatrix}0&-1\\1&-2\end{bmatrix}$,

$$A^{\mathsf T}P+PA = \begin{bmatrix}-2q&p-2q-r\\p-2q-r&2q-4r\end{bmatrix} = \begin{bmatrix}-1&0\\0&-1\end{bmatrix}.$$

From the $(1,1)$ entry, $-2q=-1$, so $q=\tfrac12$. From $(2,2)$, $2q-4r=-1$, so $1-4r=-1$ and $r=\tfrac12$.
From $(1,2)$, $p-2q-r=0$, so $p=1+\tfrac12=\tfrac32$.

$$P=\begin{bmatrix}3/2&1/2\\1/2&1/2\end{bmatrix}.$$

Positive definiteness: $3/2>0$ and $\det P = (3/2)(1/2)-(1/2)^2 = 3/4-1/4 = 1/2>0$. Hence $P\succ0$,
confirming stability.

*Check.* $\det(\lambda I-A)=\lambda(\lambda+2)+1=\lambda^2+2\lambda+1=(\lambda+1)^2$: a repeated eigenvalue
$-1$, so $A$ is stable and a positive definite solution must exist ✓.

**17.** *(Strategy: match the characteristic polynomial.)*

With $K=[k_1\ k_2]$, $A-BK=\begin{bmatrix}0&1\\-k_1&-k_2\end{bmatrix}$ and
$\det(sI-A+BK)=s^2+k_2s+k_1$. The desired polynomial is $(s+2-2j)(s+2+2j)=s^2+4s+8$. Hence $k_1=8$,
$k_2=4$, and $K=[8\ \ 4]$.

*Check.* $A-BK=\begin{bmatrix}0&1\\-8&-4\end{bmatrix}$ has eigenvalues $-2\pm2j$ ✓.

**18.** *(Strategy: compare coefficients.)*

The plant characteristic polynomial is $s^2+5s+6$; the desired one is
$(s+4)(s+7)=s^2+11s+28$. With $A-BK=\begin{bmatrix}0&1\\-(6+k_1)&-(5+k_2)\end{bmatrix}$ we need
$6+k_1=28$ and $5+k_2=11$, so $k_1=22$, $k_2=6$.

*Check.* $A-BK=\begin{bmatrix}0&1\\-28&-11\end{bmatrix}$, trace $-11$, determinant $28$, characteristic
$s^2+11s+28$ ✓.

**19.** *(Strategy: the scalar CARE is a quadratic.)*

With $a=-1$, $b=1$, $q=4$, $r=1$: $2aP-Pb^2P/r+q = -2P-P^2+4=0$, so $P^2+2P-4=0$ and
$P=-1+\sqrt5=1.2361$ (the positive root). Then $K=R^{-1}B^{\mathsf T}P=P=1.2361$ and the closed-loop
pole is $a-bK=-2.2361=-\sqrt5$.

*Check.* The general formula $-\sqrt{a^2+qb^2/r}=-\sqrt{1+4}=-\sqrt5$ ✓.

**20.** *(Strategy: the same three equations as in the tutorial example with $q_1=q_2=1$.)*

Write $P=\begin{bmatrix}p_{11}&p_{12}\\p_{12}&p_{22}\end{bmatrix}$. The CARE gives
$-p_{12}^2+1=0$, $p_{11}-p_{12}p_{22}=0$ and $2p_{12}-p_{22}^2+1=0$. Hence $p_{12}=1$,
$p_{22}=\sqrt3=1.7321$ and $p_{11}=\sqrt3$. Thus

$$P=\begin{bmatrix}\sqrt3&1\\1&\sqrt3\end{bmatrix}, \qquad K=\begin{bmatrix}1&\sqrt3\end{bmatrix}.$$

$A-BK=\begin{bmatrix}0&1\\-1&-\sqrt3\end{bmatrix}$ has characteristic polynomial $s^2+\sqrt3s+1$, so
$\omega_n=1$ and $\zeta=\sqrt3/2=0.866$; the poles are $-0.866\pm0.5j$.

*Check.* Substituting $P$ into the CARE gives zero; $\det P=3-1=2>0$ ✓.

**21.** *(Strategy: final-value theorem.)*

(a) $G(0)=1/2$. With $K_p=8$ the loop gain at zero frequency is $4$, so
$e_{ss}=1/(1+4)=0.2$.

(b) With an integral term the loop becomes type 1, so the steady-state error to a step is zero: the
integrator keeps changing $u$ until the error is exactly zero. The cost is a modified characteristic
polynomial: $1+(K_p+K_i/s)G(s)=0$ becomes

$$s(s+1)(s+2)+(K_ps+K_i)=s^3+3s^2+(2+K_p)s+K_i=0,$$

so $0<K_i<3(2+K_p)=30$ for $K_p=8$. The integral gain must be chosen inside that range.

*Check.* With $K_i=10$ the polynomial $s^3+3s^2+10s+10$ satisfies $3\cdot10>10$, so it is Hurwitz; the
final-value theorem then applies and gives zero error ✓.

**22.** *(Strategy: cubic Routh.)*

Here $a_3=1$, $a_2=2$, $a_1=3$, $a_0=K$. The conditions are $2>0$, $3>0$, $K>0$ and $a_2a_1>a_3a_0$, that is
$6>K$. Hence the polynomial is Hurwitz exactly for $0<K<6$.

*Check.* At $K=6$, $s^3+2s^2+3s+6=(s+2)(s^2+3)$, whose roots are $-2$ and $\pm j\sqrt3$: marginal
stability, the boundary case ✓. At $K=1$ the roots all have negative real parts.

**23.** *(Strategy: substitute the numerical parameters.)*

(a) With $x=(\omega,i)$:

$$A=\begin{bmatrix}-b/J&K_t/J\\-K_e/L&-R/L\end{bmatrix}
=\begin{bmatrix}-0.1&5\\-10&-200\end{bmatrix}, \qquad B=\begin{bmatrix}0\\1/L\end{bmatrix}=\begin{bmatrix}0\\100\end{bmatrix}, \qquad C=\begin{bmatrix}1&0\end{bmatrix}.$$

(b) $\operatorname{tr}A=-200.1$, $\det A=(-0.1)(-200)-(5)(-10)=70$, so
$\lambda^2+200.1\lambda+70=0$ and $\lambda=-0.3504,\,-199.75$: stable, with a slow mechanical pole and a
fast electrical pole. The transfer function is

$$G(s)=\frac{500}{s^2+200.1s+70}, \qquad G(0)=\frac{500}{70}=7.143\ \mathrm{rad/s\ per\ V}.$$

*Check.* The numerator is $K_t/(JL)=0.1/(0.02\cdot0.01)=500$ ✓, and the denominator constant term is
$(bR+K_tK_e)/(JL)= (0.004+0.01)/0.0002 = 70$ ✓.

**24.** *(Strategy: frequency response of the loop.)*

$\lvert L(j\omega)\rvert = 10/[\omega\sqrt{1+\omega^2}]$ and
$\angle L=-90^\circ-\arctan\omega$.

Gain crossover: $\omega\sqrt{1+\omega^2}=10$, so $\omega^4+\omega^2-100=0$ and
$\omega_c=3.084\ \mathrm{rad/s}$. The phase is $-90^\circ-72.04^\circ=-162.04^\circ$, giving
$\mathrm{PM}=17.96^\circ$. The phase never reaches $-180^\circ$ at finite frequency, so the gain margin is
infinite. The closed-loop polynomial is $s^2+s+10$, with $\zeta=1/(2\sqrt{10})=0.158$.

*Check.* The small phase margin and the small damping ratio agree; both say the loop is lightly damped ✓.

## Advanced

**25.** *(Strategy: a left null vector of the Kalman matrix produces a direction the input cannot move.)*

Suppose $\operatorname{rank}\mathcal{C}<n$ with
$\mathcal{C}=[B\ AB\ \cdots\ A^{n-1}B]$. Then there is a nonzero $v\in\mathbb{R}^n$ with
$v^{\mathsf T}\mathcal{C}=0$, that is

$$v^{\mathsf T}A^kB=0, \qquad k=0,1,\dots,n-1.$$

The Cayley–Hamilton theorem says $A^n+\alpha_{n-1}A^{n-1}+\cdots+\alpha_0I=0$. Multiplying by
$v^{\mathsf T}A^{k}$ on the left for any $k\ge0$ expresses $v^{\mathsf T}A^{n+k}B$ as a linear combination
of $v^{\mathsf T}A^{j}B$ with $j<n+k$, so by induction on $k$, $v^{\mathsf T}A^kB=0$ for every $k\ge0$.

Therefore

$$v^{\mathsf T}e^{At}B = \sum_{k=0}^\infty\frac{t^k}{k!}v^{\mathsf T}A^kB = 0 \qquad\text{for all }t.$$

Start at $x(0)=0$ and apply any input $u$. The solution is
$x(T)=\int_0^Te^{A(T-\tau)}Bu(\tau)d\tau$, so

$$v^{\mathsf T}x(T) = \int_0^T v^{\mathsf T}e^{A(T-\tau)}B\,u(\tau)\,d\tau = 0.$$

Thus every state reachable from the origin lies in the proper subspace $v^{\mathsf T}x=0$. The state
$x_1=v$, which satisfies $v^{\mathsf T}x_1=\lVert v\rVert^2\ne0$, is not reachable. Hence the system is
not controllable. $\blacksquare$

**26.** *(Strategy: an energy function for (a); an integral formula for (b).)*

(a) Let $V(x)=x^{\mathsf T}Px$. Since $P\succ0$,
$\lambda_{\min}(P)\lVert x\rVert^2\le V(x)\le\lambda_{\max}(P)\lVert x\rVert^2$. Along $\dot x=Ax$,

$$\dot V = x^{\mathsf T}(A^{\mathsf T}P+PA)x = -x^{\mathsf T}Qx\le-\lambda_{\min}(Q)\lVert x\rVert^2.$$

Hence $\dot V\le-cV$ with $c=\lambda_{\min}(Q)/\lambda_{\max}(P)>0$, so $V(x(t))\le V(x(0))e^{-ct}$ and

$$\lVert x(t)\rVert^2\le\frac{\lambda_{\max}(P)}{\lambda_{\min}(P)}\lVert x(0)\rVert^2e^{-ct}.$$

Thus $x(t)\to0$ exponentially, and by Theorem 7.1 every eigenvalue of $A$ has negative real part.

(b) Suppose $A$ is Hurwitz and $Q\succ0$. Since $\lVert e^{At}\rVert\le Me^{-\mu t}$ for some $M,\mu>0$, the
integral $P=\int_0^\infty e^{A^{\mathsf T}t}Qe^{At}dt$ converges. It is symmetric, and for $x\ne0$ the
integrand $x^{\mathsf T}e^{A^{\mathsf T}t}Qe^{At}x=(e^{At}x)^{\mathsf T}Q(e^{At}x)$ is positive for every
$t$ (because $e^{At}$ is invertible), so $P\succ0$. Moreover

$$A^{\mathsf T}P+PA=\int_0^\infty\frac{d}{dt}\bigl[e^{A^{\mathsf T}t}Qe^{At}\bigr]dt
=\bigl[e^{A^{\mathsf T}t}Qe^{At}\bigr]_0^\infty=-Q.$$

Uniqueness: if $P_1,P_2$ are two solutions, $\Delta P=P_1-P_2$ satisfies
$A^{\mathsf T}\Delta P+\Delta PA=0$, so $e^{A^{\mathsf T}t}\Delta Pe^{At}$ is constant in $t$. At $t=0$ it
is $\Delta P$, and as $t\to\infty$ it tends to $0$ because $A$ is Hurwitz; hence $\Delta P=0$.
$\blacksquare$

**27.** *(Strategy: a null vector of the observability matrix is an invisible initial state.)*

Suppose $\operatorname{rank}\mathcal{O}<n$. Then there is a nonzero $v$ with
$CA^kv=0$ for $k=0,\dots,n-1$; by Cayley–Hamilton, $CA^kv=0$ for all $k\ge0$, so $Ce^{At}v=0$ for all
$t\ge0$.

Take $u=0$ and the two initial states $x_a(0)=0$ and $x_b(0)=v$. Their outputs are

$$y_a(t)=Ce^{At}0=0, \qquad y_b(t)=Ce^{At}v=0,$$

identical for all $t$. Since the input and output histories are the same but the initial states differ,
no observer can determine the initial state. Hence the pair is not observable. $\blacksquare$

**28.** *(Strategy: apply the left eigenvector to $A-BK$.)*

Let $v\ne0$ satisfy $v^{\mathsf T}A=\lambda v^{\mathsf T}$ and $v^{\mathsf T}B=0$. Then

$$v^{\mathsf T}(A-BK)=v^{\mathsf T}A-(v^{\mathsf T}B)K=\lambda v^{\mathsf T}-0=\lambda v^{\mathsf T}.$$

So $v$ is a left eigenvector of $A-BK$ with the same eigenvalue $\lambda$, for every $K$. Equivalently,
$v^{\mathsf T}$ is orthogonal to every column of $\mathcal{C}=[B\ AB\ \cdots]$, so the mode is
uncontrollable.

If $\operatorname{Re}\lambda\ge0$, then every $A-BK$ has an eigenvalue in the closed right half-plane, so
no state feedback can stabilise the system. Controllability of the unstable part — *stabilisability* — is
necessary and sufficient for stabilisation by state feedback. $\blacksquare$

**29.** *(Strategy: minimise the Hamiltonian pointwise.)*

Seek $V(x)=x^{\mathsf T}Px$ with $P=P^{\mathsf T}$. The Hamilton–Jacobi–Bellman equation for

$$J=\int_0^\infty(x^{\mathsf T}Qx+u^{\mathsf T}Ru)dt, \qquad \dot x=Ax+Bu,$$

is

$$0=\min_u\Bigl[x^{\mathsf T}Qx+u^{\mathsf T}Ru+\nabla V^{\mathsf T}(Ax+Bu)\Bigr].$$

With $\nabla V=2Px$ and $R\succ0$, the bracket is a strictly convex quadratic in $u$:
$u^{\mathsf T}Ru+2x^{\mathsf T}PBu+\text{(terms without }u)$. The minimiser solves
$2Ru+2B^{\mathsf T}Px=0$, so

$$u^*=-R^{-1}B^{\mathsf T}Px.$$

Substituting,

$$0=x^{\mathsf T}Qx+x^{\mathsf T}PBR^{-1}B^{\mathsf T}Px+2x^{\mathsf T}P(Ax-BR^{-1}B^{\mathsf T}Px)
=x^{\mathsf T}\bigl(Q+A^{\mathsf T}P+PA-PBR^{-1}B^{\mathsf T}P\bigr)x.$$

Since this must hold for every $x$, the CARE follows. With $K=R^{-1}B^{\mathsf T}P$, the closed loop is
$A-BK$, and

$$\frac{d}{dt}(x^{\mathsf T}Px)=x^{\mathsf T}\bigl[(A-BK)^{\mathsf T}P+P(A-BK)\bigr]x
=-x^{\mathsf T}\bigl(Q+PBR^{-1}B^{\mathsf T}P\bigr)x<0$$

for $x\ne0$ when $Q\succ0$. Hence $V$ is a Lyapunov function and the closed loop is stable.
$\blacksquare$

**30.** *(Strategy: compute the array and read the sign conditions.)*

For $a_3s^3+a_2s^2+a_1s+a_0$ with $a_3>0$:

$$s^3:\ a_3,\ a_1; \qquad s^2:\ a_2,\ a_0; \qquad s^1:\ \frac{a_2a_1-a_3a_0}{a_2},\ 0; \qquad s^0:\ a_0.$$

The first column is $a_3$, $a_2$, $(a_2a_1-a_3a_0)/a_2$, $a_0$. With $a_3>0$, all entries are positive
exactly when $a_2>0$, $a_0>0$ and $a_2a_1>a_3a_0$ (which forces $a_1>0$). Hence the cubic is Hurwitz iff

$$a_2,a_1,a_0>0 \quad\text{and}\quad a_2a_1>a_3a_0.$$

For the PID loop, $a_3=1$, $a_2=3+K_d$, $a_1=2+K_p$, $a_0=K_i$. With $K_p=2$, $K_d=1$:
$a_2=4$, $a_1=4$, so the condition is $4\cdot4>K_i$ and $K_i>0$, that is $0<K_i<16$.

*Check.* At $K_i=16$ the $s^1$ entry vanishes and the roots are $-4,\pm2j$: the boundary case ✓.

**31.** *(Strategy: exhibit the Kalman matrix explicitly.)*

For $n=3$, $B_c=e_3$ and

$$A_cB_c=\begin{bmatrix}0\\1\\-a_2\end{bmatrix}=e_2-a_2e_3, \qquad
A_c^2B_c=e_1-a_2e_2+(a_2^2-a_1)e_3.$$

Hence

$$\mathcal{C}=\begin{bmatrix}0&0&1\\0&1&-a_2\\1&-a_2&a_2^2-a_1\end{bmatrix},$$

which is upper anti-triangular with ones on the anti-diagonal and therefore has determinant $-1\ne0$. For
general $n$ the same computation gives columns $e_n, e_{n-1}+\cdots, \dots, e_1+\cdots$, an anti-triangular
matrix with ones on the anti-diagonal; its determinant is $\pm1$. Thus $\operatorname{rank}\mathcal{C}=n$
for every choice of the $a_i$, so the canonical form is always controllable. $\blacksquare$

**32.** *(Strategy: $\mathrm{PM}=45^\circ$ means the phase at crossover is $-135^\circ$.)*

(a) $\angle L(j\omega)=-90^\circ-\arctan\omega=-135^\circ$ gives $\arctan\omega=45^\circ$, so
$\omega_c=1\ \mathrm{rad/s}$. At crossover $\lvert L(j\omega_c)\rvert=K/[\omega_c\sqrt{1+\omega_c^2}]=K/\sqrt2=1$,
so $K=\sqrt2=1.4142$.

(b) The closed loop is $s^2+s+K=0$, so $\omega_n=\sqrt K=1.189$ and
$\zeta=1/(2\sqrt K)=1/(2\cdot1.189)=0.4204$. The rule of thumb predicts
$\zeta\approx45/100=0.45$, close to the exact value.

*Check.* $\mathrm{PM}=180^\circ-135^\circ=45^\circ$ ✓, and $\zeta=0.42$ corresponds to about $23\%$
overshoot, a reasonable response.

## Challenge

**33.** *(Strategy: write Newton's laws for the cart and the pendulum, then eliminate $\ddot x$.)*

(a) Let $x$ be the cart position and $\theta$ the angle from the upright. The horizontal momentum balance
for the whole system and the pendulum's angular equation are

$$(M+m)\ddot x+m l\ddot\theta=u, \qquad m l^2\ddot\theta=mgl\sin\theta-ml\ddot x\cos\theta.$$

The second equation is the torque balance about the pivot: gravity contributes $mgl\sin\theta$, and the
fictitious force from the cart's acceleration contributes $-ml\ddot x\cos\theta$. For small angles,
$\sin\theta\approx\theta$ and $\cos\theta\approx1$, so
$l\ddot\theta=g\theta-\ddot x$.

(b) Substituting $\ddot x=g\theta-l\ddot\theta$ into the first equation:

$$(M+m)(g\theta-l\ddot\theta)+ml\ddot\theta=u \quad\Longrightarrow\quad -Ml\ddot\theta+(M+m)g\theta=u,$$

so

$$\ddot\theta=\frac{(M+m)g}{Ml}\theta-\frac{1}{Ml}u, \qquad
\ddot x=-\frac{mg}{M}\theta+\frac{1}{M}u.$$

With $M=1$, $m=0.2$, $l=0.5$, $g=9.81$: $mg/M=1.962$, $(M+m)g/(Ml)=1.2(9.81)/0.5=23.544$,
$1/M=1$, $1/(Ml)=2$. Hence, with state $(x,\dot x,\theta,\dot\theta)$,

$$A=\begin{bmatrix}0&1&0&0\\0&0&-1.962&0\\0&0&0&1\\0&0&23.544&0\end{bmatrix}, \qquad
B=\begin{bmatrix}0\\1\\0\\-2\end{bmatrix}.$$

(c) The controllability matrix is

$$\mathcal{C}=\begin{bmatrix}0&1&0&3.924\\1&0&3.924&0\\0&-2&0&-47.088\\-2&0&-47.088&0\end{bmatrix},$$

whose rank is $4$: the system is controllable.

(d) Pole placement at $-2,-3,-4,-5$ gives

$$K=\begin{bmatrix}-6.116&-7.849&-50.330&-10.925\end{bmatrix}.$$

The negative first entry is not an error: pushing the cart one way moves the pendulum the other way, so
the position feedback has the opposite sign to the angle feedback.

*Check.* Substituting $K$ into $A-BK$ gives the characteristic polynomial
$(s+2)(s+3)(s+4)(s+5)$; the eigenvalues are $-2,-3,-4,-5$ ✓.

**34.** *(Strategy: solve the scalar CARE and differentiate.)*

(a) The CARE is $2aP-b^2P^2/r+q=0$, that is $b^2P^2-2arP-qr=0$. The positive root is

$$P=\frac{ar+\sqrt{a^2r^2+qb^2r}}{b^2}.$$

Since $R=r$ and $B=b$, $K=R^{-1}B^{\mathsf T}P=bP/r$.

(b) $bK=b^2P/r=\dfrac{ar+\sqrt{a^2r^2+qb^2r}}{r}=a+\sqrt{a^2+\dfrac{qb^2}{r}}$, so

$$a-bK=-\sqrt{a^2+\frac{qb^2}{r}}.$$

(c) Differentiate with respect to $q$:

$$\frac{d}{dq}\Bigl(-\sqrt{a^2+\frac{qb^2}{r}}\Bigr)=-\frac{b^2}{2r\sqrt{a^2+qb^2/r}}<0.$$

So increasing the state weight always moves the closed-loop pole further left — but with diminishing
returns (the derivative behaves like $q^{-1/2}$).

(d) With $a=b=r=1$: $q=1$ gives pole $-\sqrt2=-1.4142$; $q=9$ gives pole $-\sqrt{10}=-3.1623$.

*Check.* The formula at $q=0$ gives $a-|a|$, which is $0$ for $a>0$: with no state penalty the optimal
gain vanishes and the closed-loop pole is the open-loop one ✓.

**35.** *(Strategy: clear denominators and apply the cubic test.)*

With $G=1/[(s+1)(s+2)]$, the characteristic polynomial is
$s(s+1)(s+2)+(K_ds^2+K_ps+K_i)=s^3+(3+K_d)s^2+(2+K_p)s+K_i$.

(a) With $K_d=0$: $a_3=1$, $a_2=3$, $a_1=2+K_p$, $a_0=K_i$. The conditions are $K_i>0$, $2+K_p>0$
and $3(2+K_p)>K_i$. So the stability region is

$$K_p>-2, \qquad 0<K_i<3(2+K_p).$$

(b) With $K_d=1$: $a_2=4$ and the region is

$$K_p>-2, \qquad 0<K_i<4(2+K_p).$$

The derivative term enlarges the admissible integral gain because it adds damping (it increases $a_2$).

(c) $K_p=2$, $K_i=10$, $K_d=1$: $4(2+2)=16>10$, so the loop is stable. The roots are $-3.6543$ and
$-0.1729\pm1.6452j$: stable but lightly damped ($\zeta\approx0.10$ for the complex pair). The design is
acceptable for stability but would ring; increasing $K_d$ or reducing $K_i$ would improve damping.

*Check.* At $K_i=12$ with $K_d=1$, $K_p=2$: $16>12$ still stable; at $K_i=16$ the roots are $-4,\pm2j$,
the boundary ✓.

**36.** *(Strategy: duality — place the eigenvalues of $A^{\mathsf T}-C^{\mathsf T}L^{\mathsf T}$.)*

The observer is $\dot{\hat x}=A\hat x+Bu+L(y-\hat y)$, $\hat y=C\hat x$. With $e=x-\hat x$,

$$\dot e=(A-LC)e,$$

so the error decays exactly when $A-LC$ is Hurwitz. By duality, $(C,A)$ observable implies
$(A^{\mathsf T},C^{\mathsf T})$ controllable, and placing the eigenvalues of $A-LC$ is the same as placing
those of $A^{\mathsf T}-C^{\mathsf T}L^{\mathsf T}$; the gains are transposes.

Desired polynomial: $(s+5)(s+6)=s^2+11s+30$. With $L=\begin{bmatrix}\ell_1\\\ell_2\end{bmatrix}$,

$$A-LC=\begin{bmatrix}-\ell_1&1\\-2-\ell_2&-3\end{bmatrix},$$

whose characteristic polynomial is $s^2+(3+\ell_1)s+(3\ell_1+2+\ell_2)$. Matching: $3+\ell_1=11$, so
$\ell_1=8$; and $24+2+\ell_2=30$, so $\ell_2=4$. Hence $L=\begin{bmatrix}8\\4\end{bmatrix}$.

*Check.* $A-LC=\begin{bmatrix}-8&1\\-6&-3\end{bmatrix}$ has trace $-11$ and determinant $30$, hence
characteristic polynomial $s^2+11s+30$ and eigenvalues $-5,-6$ ✓.

**Separation principle.** The state-feedback gain $K$ and the observer gain $L$ can be designed
independently: the closed-loop system with $u=-K\hat x$ has eigenvalues
$\sigma(A-BK)\cup\sigma(A-LC)$. The reason is that in coordinates $(x,e)$ the system matrix is block
triangular,
$\begin{bmatrix}A-BK&BK\\0&A-LC\end{bmatrix}$, whose eigenvalues are the union of the diagonal blocks. Thus
the controller poles and the observer poles can be placed separately, and the observer is made faster than
the controller so that the estimation error decays before it can disturb the state response.
