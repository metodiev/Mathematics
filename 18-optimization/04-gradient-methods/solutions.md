# Gradient Methods — Solutions

> [Tutorial](README.md) · [Exercises](exercises.md) · 36 complete solutions

Each solution states the strategy, carries out the computation or proof step by step, and checks the result
numerically where that is meaningful. Theorem numbers refer to the [tutorial](README.md).

## Beginner

**1.**

*Strategy.* The quadratic model at $x$ is $f(x)+f'(x)v+\tfrac L2v^2$; its minimiser is $v=-f'(x)/L$, and replacing
$1/L$ by $\alpha$ gives the update.

With $f(x)=x^2-4x$ we have $f'(x)=2x-4$. The model
$x^2-4x+(2x-4)v+\tfrac L2v^2$ is minimised at $v=-(2x-4)/L$, so the update is
$x_{k+1}=x_k-\alpha(2x_k-4)$.

With $\alpha=0.2$: $x_1=0-0.2(-4)=0.8$, then $x_2=0.8-0.2(1.6-4)=0.8+0.48=1.28$. The recursion is
$x_{k+1}=0.6x_k+0.8$, whose fixed point is $x=2$ and whose closed form is $x_k=2-2(0.6)^k$.

*Check.* $f(0)=0$, $f(0.8)=-2.56$, $f(1.28)=-3.4816$, and the minimum is $f(2)=-4$: decreasing towards the
minimiser. ✓

**2.**

*Strategy.* For $f(x)=x^2$ the update is $x_{k+1}=x_k-2\alpha x_k=(1-2\alpha)x_k$, a geometric recursion.

With $\alpha=0.1$ the factor is $1-0.2=0.8$, so $x_k=0.8^k$: $x_1=0.8$, $x_2=0.64$, $x_3=0.512$. Then
$f(x_3)=0.512^2=0.262144$.

*Check.* $f(x_3)/f(x_0)=0.262144=0.8^6$, that is the squared factor, as expected because $f$ is quadratic in $x$.
✓

**3.**

*Strategy.* Read $L$ and $\mu$ off the second derivative of a quadratic, then apply the scalar recursion
$x_{k+1}=(1-\alpha\lambda)x_k$.

$f(x)=\tfrac32x^2$ has $f''=3$, so $L=\mu=3$ and $\kappa=1$.

$\alpha=\tfrac13=1/L$: factor $1-3\cdot\tfrac13=0$, so $x_1=0$ and the method converges in one step.

$\alpha=\tfrac23=2/L$: factor $1-2=-1$, so $x_{k+1}=-x_k$: the iterates oscillate forever between $\pm x_0$ and
do not converge. The point is that the sufficient condition $\alpha\le1/L$ is not the exact stability bound;
for a quadratic the latter is $\alpha<2/L$. ✓

**4.**

*Strategy.* The recursion for $f(x)=\tfrac12x^2$ is $x_{k+1}=(1-\alpha)x_k$, so convergence is
$\lvert1-\alpha\rvert<1$, that is $0<\alpha<2$.

| $\alpha$ | factor | behaviour |
|---|---|---|
| $0.05$ | $0.95$ | convergence, rate $0.95$ |
| $0.5$ | $0.5$ | convergence, rate $0.5$ |
| $1$ | $0$ | one-step convergence |
| $2$ | $-1$ | oscillation, no convergence |

✓ Note that $\alpha=1=1/L$ is optimal and $\alpha=2$ is the boundary of stability.

**5.**

*Strategy.* Expand $f$ and identify the Hessian with $A^{\mathsf T}A$.

$f(x)=\tfrac12\lVert Ax-b\rVert^2=\tfrac12(x^{\mathsf T}A^{\mathsf T}Ax-2b^{\mathsf T}Ax+b^{\mathsf T}b)$, so
$$
\nabla f(x)=A^{\mathsf T}(Ax-b)=\binom{x_1-1}{4x_2-2},\qquad
\nabla^2f=A^{\mathsf T}A=\begin{pmatrix}1&0\\0&4\end{pmatrix}.
$$
Hence $L=4$, $\mu=1$, $\kappa=4$, and the minimiser is $x^\star=(1,\tfrac12)$ with $f(x^\star)=0$.

*Check.* At $x=(0,0)$, $Ax-b=(-1,-1)$ and $A^{\mathsf T}(-1,-1)=(-1,-2)$; the formula gives
$(0-1,\,0-2)=(-1,-2)$ ✓.

**6.**

*Strategy.* Show the derivative is unbounded, then compute the scalar recursion.

$f'(x)=4x^3$, and $\lvert f'(x)-f'(y)\rvert/\lvert x-y\rvert$ is unbounded as $x,y\to\infty$: no finite $L$ works,
so Lemma 7.2.1 cannot be applied globally.

With $\alpha=0.5$ the iteration is $x_{k+1}=x_k-2x_k^3$. From $x_0=1$: $x_1=1-2=-1$, $x_2=-1+2=1$, $x_3=-1$. The
iterates form a period-two cycle; the function values are $f(1)=f(-1)=1$ and never decrease.

*Diagnosis.* Near $x=0$ the Hessian $12x^2$ is small, so a large step is safe; far from $0$ it is large, so the
same step is unstable. A constant step cannot be safe for a function with no global $L$; a decaying step inside a
trust region, or a line search, is required.

**7.**

*Strategy.* For $x\ne0$ the "gradient" is the sign, so every step has length exactly $\alpha$ and the sign
alternates once the iterate crosses zero.

Iterates: $2,\,1.7,\,1.4,\,1.1,\,0.8,\,0.5,\,0.2$ (six steps). Continuing: $-0.1,\,0.2,\,-0.1,\dots$, so after
crossing zero the sequence alternates between $0.2$ and $-0.1$.

No $L$ exists because the difference quotient $\lvert\operatorname{sign}x-\operatorname{sign}y\rvert/\lvert x-y\rvert$
is unbounded as $y\uparrow x$. The descent lemma therefore has no constant and the sufficient-decrease theorem
does not apply; the method oscillates with amplitude at most $\alpha$.

*Check.* $\lvert x_k\rvert\le0.3$ for $k\ge6$ and $f(x_k)\le0.3$: the noise floor is of order $\alpha$, consistent
with Corollary 7.7.4. ✓

**8.**

*Strategy.* Compute $G_1=g_1\odot g_1$, take the elementwise square root, and divide.

$G_1=(1,4)$, $\sqrt{G_1}=(1,2)$, so $g_1/\sqrt{G_1}=(1,-1)$ and the displacement is $0.5\cdot(1,-1)=(0.5,-0.5)$.
Hence $x_1=(0,0)-(0.5,-0.5)=(-0.5,\,0.5)$.

*Check.* Each coordinate has moved by $0.5=\alpha$, independent of the gradient magnitude — the defining property
of AdaGrad. ✓

**9.**

*Strategy.* Update the second-moment average first, then divide.

$v_1=0.9\cdot0+0.1\cdot(1,4)=(0.1,0.4)$, so $\sqrt{v_1}=(0.3162,0.6325)$ and
$g_1/\sqrt{v_1}=(3.162,3.162)$. The displacement is $0.1\cdot(3.162,3.162)=(0.3162,0.3162)$, so
$x_1=(-0.3162,-0.3162)$.

*Check.* Both coordinates moved the same distance although the second gradient is twice the first: the
normalisation has removed the scale difference. ✓

**10.**

*Strategy.* At the first step the bias corrections are exactly $1-\beta_1=0.1$ and $1-\beta_2=0.001$, which are
precisely the weights used in the averages.

$m_1=0.1\cdot(1,1)=(0.1,0.1)$, $v_1=0.001\cdot(1,1)=(0.001,0.001)$. Then $\hat m_1=m_1/0.1=(1,1)$ and
$\hat v_1=v_1/0.001=(1,1)$. The displacement is $0.01\cdot(1,1)/\sqrt{(1,1)}=(0.01,0.01)$, so
$x_1=(-0.01,-0.01)$.

*Why the magnitude does not matter.* If $g_1=c\,u$ with $u$ a unit vector, then $\hat m_1=c\,u$ and
$\hat v_1=c^2u^2$, so $\hat m_1/\sqrt{\hat v_1}=u$: the first Adam step has length $\alpha$ in the direction of the
gradient, whatever its size. ✓

**11.**

*Strategy.* Induction, using the closed form of a geometric series.

If the gradient is constantly $g$, then $m_k=\beta_1m_{k-1}+(1-\beta_1)g$ with $m_0=0$. Dividing by $g$ reduces
this to $u_k=\beta_1u_{k-1}+(1-\beta_1)$ with $u_0=0$, whose solution is
$u_k=(1-\beta_1)(1+\beta_1+\dots+\beta_1^{k-1})=1-\beta_1^k$. Hence $m_k=(1-\beta_1^k)g$ and
$\hat m_k=m_k/(1-\beta_1^k)=g$. The same computation with $g^2$ in place of $g$ gives $v_k=(1-\beta_2^k)g^2$ and
$\hat v_k=g^2$. $\blacksquare$

*Check.* With $\beta_1=0.9$ and $k=1$: $m_1=0.1g$ and $\hat m_1=g$ ✓. With $k=10$: $m_{10}=0.6513g$ and
$\hat m_{10}=g$ ✓.

**12.**

*Strategy.* Independent averages divide the variance by the batch size.

| $B$ | variance $\sigma^2/B$ | standard deviation |
|---|---|---|
| $1$ | $3.2$ | $1.789$ |
| $8$ | $0.4$ | $0.632$ |
| $64$ | $0.05$ | $0.224$ |

The variance falls linearly in $B$ and the standard deviation as $1/\sqrt B$: quadrupling the batch halves the
noise. ✓

## Intermediate

**13.**

*Strategy.* For a diagonal quadratic, $\mu$ and $L$ are the extreme diagonal entries, and the contraction is
$(\kappa-1)/(\kappa+1)$.

$\mu=1$, $L=9$, $\kappa=9$, $\alpha=2/(L+\mu)=0.2$. The factor is $(9-1)/(9+1)=0.8$, so the error norm decays as
$0.8^k$ and $k\ge\ln(10^{-6})/\ln(0.8)=61.9$, that is $62$ iterations.

*Check.* With $\alpha=0.2$ the factors are $\lvert1-0.2\lambda\rvert$: for $\lambda=1$, $0.8$; for $\lambda=4$,
$0.2$; for $\lambda=9$, $0.8$. The worst is $0.8$, attained twice, so the bound is tight. ✓

**14.**

*Strategy.* Minimise the right side of the strong-convexity inequality over $y$; the minimum is an explicit
quadratic.

Strong convexity gives, for all $y$,
$$
f(y)\ge f(x)+\nabla f(x)^{\mathsf T}(y-x)+\frac{\mu}{2}\lVert y-x\rVert^2 .
$$
The right side is a convex quadratic in $y$ with gradient $\nabla f(x)+\mu(y-x)$, minimised at
$y=x-\nabla f(x)/\mu$, where its value is $f(x)-\lVert\nabla f(x)\rVert^2/(2\mu)$. Since $f^\star\le f(y)$ for
every $y$, in particular for this one:
$f^\star\ge f(x)-\lVert\nabla f(x)\rVert^2/(2\mu)$, which rearranges to the claim. $\blacksquare$

*Check.* For $f(x)=\tfrac{\mu}{2}x^2$ both sides equal $\mu^2x^2=2\mu\cdot\tfrac{\mu}{2}x^2$ ✓.

**15.**

*Strategy.* Write the difference as an integral of gradient differences and bound the integrand by the Lipschitz
condition.

With $\varphi(t)=f(x+tv)$, the fundamental theorem of calculus gives
$$
f(x+v)-f(x)=\varphi(1)-\varphi(0)=\int_0^1\nabla f(x+tv)^{\mathsf T}v\,dt .
$$
Subtracting $\nabla f(x)^{\mathsf T}v=\int_0^1\nabla f(x)^{\mathsf T}v\,dt$,
$$
f(x+v)-f(x)-\nabla f(x)^{\mathsf T}v=\int_0^1\bigl[\nabla f(x+tv)-\nabla f(x)\bigr]^{\mathsf T}v\,dt
\le\int_0^1\bigl\lVert\nabla f(x+tv)-\nabla f(x)\bigr\rVert\lVert v\rVert\,dt
\le\int_0^1Lt\lVert v\rVert^2dt=\frac L2\lVert v\rVert^2 .
$$
Cauchy–Schwarz is used in the first inequality and the Lipschitz condition in the second. $\blacksquare$

**16.**

*Strategy.* Minimise the one-dimensional function $\varphi(\alpha)=f(x-\alpha g)$ and solve $\varphi'(\alpha)=0$.

For a quadratic, $f(x-\alpha g)=f(x)-\alpha g^{\mathsf T}g+\tfrac{\alpha^2}{2}g^{\mathsf T}Qg$, so
$\varphi'(\alpha)=-g^{\mathsf T}g+\alpha g^{\mathsf T}Qg=0$ gives
$\alpha=\dfrac{g^{\mathsf T}g}{g^{\mathsf T}Qg}$, which is positive and is a minimum because
$\varphi''=g^{\mathsf T}Qg>0$.

At $x=(1,1)$ with $Q=\operatorname{diag}(1,4)$: $g=Qx=(1,4)$, $g^{\mathsf T}g=17$, $g^{\mathsf T}Qg=1+64=65$, so
$\alpha=17/65=0.2615$. Compare $1/L=0.25$ and $2/(L+\mu)=0.4$: the exact line-search step lies between them and is
optimal for this particular $x$, but it changes from step to step — it is a method, not a constant.

**17.**

*Strategy.* Insert a trial solution $e_k=r^k$ into the linear recursion.

The heavy ball for one coordinate is $e_{k+1}=e_k-\alpha\lambda e_k+\beta(e_k-e_{k-1})$, that is
$e_{k+1}=(1-\alpha\lambda+\beta)e_k-\beta e_{k-1}$. Substituting $e_k=r^k$ and dividing by $r^{k-1}$ gives
$$
r^2-(1-\alpha\lambda+\beta)r+\beta=0 .
$$
The roots are inside the unit disc (next exercise for the criterion) exactly when $\beta<1$ and
$\lvert1-\alpha\lambda+\beta\rvert<1+\beta$. The left inequality of the absolute value gives $\alpha\lambda>0$; the
right gives $1-\alpha\lambda+\beta>-1-\beta$, that is $\alpha\lambda<2(1+\beta)$, hence
$\alpha<2(1+\beta)/\lambda$. ✓

*Check.* With $\beta=0$ the condition reduces to $\alpha<2/\lambda$, the known GD bound. ✓

**18.**

*Strategy.* Apply the recursion with $\alpha=1/L=0.25$ and $\beta_k=k/(k+3)$.

$f(x)=\tfrac12(4x_1^2+x_2^2)$, $\nabla f=(4x_1,x_2)$, $x_0=y_0=(1,1)$.

$k=1$: $x_1=y_0-0.25(4,1)=(0,0.75)$; then $y_1=x_1+\tfrac14(x_1-x_0)=(0,0.75)+\tfrac14(-1,-0.25)=(-0.25,0.6875)$.

$k=2$: $\nabla f(y_1)=(-1,0.6875)$ and $x_2=y_1-0.25(-1,0.6875)=(-0.25+0.25,\ 0.6875-0.171875)=(0,0.515625)$;
then $y_2=x_2+\tfrac25(x_2-x_1)=(0,0.515625)+\tfrac25(0,-0.234375)=(0,0.421875)$.

$k=3$: $\nabla f(y_2)=(0,0.421875)$ and $x_3=(0,0.421875-0.105469)=(0,0.316406)$; then
$y_3=x_3+\tfrac12(x_3-x_2)=(0,0.216797)$.

*Function values.* $f(x_1)=0.5(0+0.5625)=0.28125$; $f(x_2)=0.5(0.265869)=0.132935$;
$f(x_3)=0.5(0.100113)=0.050056$.

*Comparison with the bound.* $2L\lVert x_0\rVert^2/(k+1)^2=16/(k+1)^2$ equals $4$, $1.778$ and $1.000$ at
$k=1,2,3$; all three values are below the bound. ✓

*Observation.* The stiff coordinate is annihilated at the first step because $\alpha\lambda_1=1$; the whole
problem reduces to the flat coordinate, which is why the numbers look like a one-dimensional recursion.

**19.**

*Strategy.* Set $x_{k+1}=x_k$ in the recursion and solve.

With $g=x+0.2$ and step $\alpha$, $x_{k+1}=x_k-\alpha(x_k+0.2)=(1-\alpha)x_k-0.2\alpha$. The fixed point is
$x=-0.2$, whatever $\alpha$ is (for $0<\alpha<2$). There,
$f=\tfrac12(0.04)=0.02$, while $f^\star=0$: the suboptimality is $0.02$.

The bias does not average out because it is present at *every* step. Averaging over samples reduces the variance
(the deviation of each estimate from its mean) but leaves the mean of the estimates where it is; only unbiased
estimators have fixed points at $\nabla f=0$. Formally, the fixed point satisfies
$\mathbb{E}[g(x)]=0$, that is $\nabla f(x)=-b$. ✓

**20.**

*Strategy.* The standard deviation of an average of $B$ independent estimates is $\sigma/\sqrt B$.

$\sigma=4$: for $B=16$ the standard deviation is $4/4=1$. For a target of $0.5$ we need $\sqrt B=8$, that is
$B=64$. ✓

*Remark.* This is the statistical side only; the cost per iteration grows linearly in $B$, so the total work for
a target variance is constant (Section 7.8).

**21.**

*Strategy.* Accumulate the squares coordinatewise and compare the denominators.

After $k$ steps, $G_{k,1}=k$ and $G_{k,2}=1$. The effective steps are $\alpha/\sqrt k$ and $\alpha/1$: the
frequent coordinate slows down like $1/\sqrt k$, while the rare coordinate keeps its original step. This is the
design intent: features that appear rarely keep learning, features that appear constantly are protected from
overshooting.

*Check.* With $\alpha=0.1$: at $k=100$ the steps are $0.01$ and $0.1$, a factor of ten apart. ✓

*Warning.* The same mechanism is why AdaGrad stalls on long runs: the denominators only grow, so every coordinate
eventually freezes (Section 7.9).

**22.**

*Strategy.* Track $g$ through the update and use homogeneity.

Replace $g$ by $cg$ with $c>0$. Then $v$ is replaced by $c^2v$, so $\sqrt v$ by $c\sqrt v$, and
$g/\sqrt v$ by $cg/(c\sqrt v)=g/\sqrt v$: the update is unchanged. Plain gradient descent sends
$g\mapsto cg$ and hence the displacement is multiplied by $c$, so a step tuned for one loss scale is wrong by the
factor $c$ for another.

*Consequence.* Adaptive methods transfer between objectives whose gradients differ by a constant factor (a change
of units, a rescaling of the loss by the batch size), whereas the learning rate of SGD must be retuned. The price
is that adaptive methods also ignore a genuine signal: the magnitude of the gradient, which near a minimum
encodes the distance to it. ✓

**23.**

*Strategy.* Substitute $\beta_1=\beta_2=0$ into the definitions and cancel.

$m_k=(1-0)g_k=g_k$ and $v_k=(1-0)g_k^2=g_k^2$. The corrections are $1-0^k=1$, so $\hat m_k=g_k$ and
$\hat v_k=g_k^2$, giving $x_{k+1}=x_k-\alpha g_k/(\lvert g_k\rvert+\varepsilon)$ elementwise.

In one dimension with $\lvert g_k\rvert\gg\varepsilon$ the displacement is $\pm\alpha$: a pure sign step. Such a
method does not converge to the minimiser — it oscillates within $\alpha$ of it — and it is not a descent method
for any fixed step, because it ignores how far away the minimum is.

## Advanced

**24.**

*Strategy.* Combine the sufficient-decrease inequality with the distance recursion, then telescope.

Let $g_k=\nabla f(x_k)$, $\delta_k=f(x_k)-f^\star$, $r_k=\lVert x_k-x^\star\rVert$. Theorem 7.2.2 gives
$$
\frac{\alpha}{2}\lVert g_k\rVert^2\le\delta_k-\delta_{k+1}\qquad\text{(gain inequality)} .
$$
Expanding and using convexity $g_k^{\mathsf T}(x_k-x^\star)\ge\delta_k$,
$$
r_{k+1}^2=r_k^2-2\alpha g_k^{\mathsf T}(x_k-x^\star)+\alpha^2\lVert g_k\rVert^2\le r_k^2-2\alpha\delta_k+\alpha^2\lVert g_k\rVert^2 .
$$
Hence $2\alpha\delta_k\le r_k^2-r_{k+1}^2+\alpha^2\lVert g_k\rVert^2$, and the gain inequality bounds
$\alpha^2\lVert g_k\rVert^2\le2\alpha(\delta_k-\delta_{k+1})$. Substituting,
$$
2\alpha\delta_k\le r_k^2-r_{k+1}^2+2\alpha\delta_k-2\alpha\delta_{k+1}
\quad\Longrightarrow\quad 2\alpha\delta_{k+1}\le r_k^2-r_{k+1}^2 .
$$
Summing over $k<K$ telescopes: $2\alpha\sum_{k<K}\delta_{k+1}\le r_0^2-r_K^2\le r_0^2$. By the gain inequality
$\delta_k$ is nonincreasing, so $K\delta_K\le\sum_{k<K}\delta_{k+1}$ and
$\delta_K\le r_0^2/(2\alpha K)$. $\blacksquare$

**25.**

*Strategy.* Chain the sufficient-decrease bound with the gradient lower bound of Lemma 7.5.1.

With $\alpha=1/L$, Theorem 7.2.2 gives $\delta_{k+1}\le\delta_k-\tfrac{1}{2L}\lVert g_k\rVert^2$. Lemma 7.5.1
gives $\lVert g_k\rVert^2\ge2\mu\delta_k$. Therefore
$$
\delta_{k+1}\le\delta_k-\frac{1}{2L}\cdot2\mu\delta_k=\Bigl(1-\frac{\mu}{L}\Bigr)\delta_k .
$$
Induction gives $\delta_k\le(1-\mu/L)^k\delta_0=(1-1/\kappa)^k\delta_0$. $\blacksquare$

*Tightness.* For $f(x)=\tfrac12x^{\mathsf T}Qx$ with $\mu$ the smallest and $L$ the largest eigenvalue, the exact
contracting factor along the flat eigendirection is $1-\alpha\mu=1-\mu/L$, so the bound is attained. ✓

**26.**

*Strategy.* Diagonalise and bound $\lvert1-\alpha\lambda\rvert$ uniformly on $[\mu,L]$.

In the eigenbasis $e_k^{(i)}=(1-\alpha\lambda_i)^ke_0^{(i)}$, so
$\lVert e_k\rVert\le\max_i\lvert1-\alpha\lambda_i\rvert^k\lVert e_0\rVert$. With $\alpha=2/(L+\mu)$,
$$
1-\alpha\mu=\frac{L-\mu}{L+\mu}=c,\qquad 1-\alpha L=-\frac{L-\mu}{L+\mu}=-c .
$$
The function $\lambda\mapsto1-\alpha\lambda$ is affine, so its values on $[\mu,L]$ fill the interval with
endpoints $\pm c$; hence $\lvert1-\alpha\lambda\rvert\le c$ for all $\lambda\in[\mu,L]$, with equality at both
ends. That equality at both ends is why the factor cannot be improved: one eigenvalue gives $+c$ and the other
$-c$, and both attain the bound. Therefore
$\lVert e_k\rVert\le c^k\lVert e_0\rVert$. $\blacksquare$

**27.**

*Strategy.* Two inequalities: descent in function value, and the distance recursion; eliminate the gradient norm
between them.

Let $\delta_k=\mathbb{E}[f(x_k)-f^\star]$, $r_k^2=\mathbb{E}\lVert x_k-x^\star\rVert^2$.

*Descent.* By the descent lemma with $x_{k+1}=x_k-\alpha g_k$ and
$\mathbb{E}\lVert g_k\rVert^2=\lVert\nabla f(x_k)\rVert^2+\mathbb{E}\lVert g_k-\nabla f(x_k)\rVert^2\le\lVert\nabla f(x_k)\rVert^2+\sigma^2$,
$$
\mathbb{E}[f(x_{k+1})\mid x_k]\le f(x_k)-\alpha\lVert\nabla f(x_k)\rVert^2+\frac{L\alpha^2}{2}\bigl(\lVert\nabla f(x_k)\rVert^2+\sigma^2\bigr)
\le f(x_k)-\frac{\alpha}{2}\lVert\nabla f(x_k)\rVert^2+\frac{L\alpha^2\sigma^2}{2},
$$
using $L\alpha\le1$. Taking expectations and rearranging,
$$
\mathbb{E}\lVert\nabla f(x_k)\rVert^2\le\frac{2}{\alpha}(\delta_k-\delta_{k+1})+L\alpha\sigma^2 .
$$

*Distance.* Using $\mathbb{E}[g_k\mid x_k]=\nabla f(x_k)$ and convexity,
$$
r_{k+1}^2=r_k^2-2\alpha\mathbb{E}\langle\nabla f(x_k),x_k-x^\star\rangle+\alpha^2\mathbb{E}\lVert g_k\rVert^2
\le r_k^2-2\alpha\delta_k+\alpha^2\bigl(\mathbb{E}\lVert\nabla f(x_k)\rVert^2+\sigma^2\bigr).
$$

*Elimination.* Substitute the first into the second:
$$
2\alpha\delta_k\le r_k^2-r_{k+1}^2+2\alpha(\delta_k-\delta_{k+1})+\alpha^2\sigma^2(1+L\alpha)
\quad\Longrightarrow\quad
2\alpha\delta_{k+1}\le r_k^2-r_{k+1}^2+\alpha^2\sigma^2(1+L\alpha).
$$
Summing over $k<K$ and using that the minimum is at most the average gives
$\min_{k<K}\delta_k\le R^2/(2\alpha K)+\alpha\sigma^2(1+L\alpha)/2$. $\blacksquare$

**28.**

*Strategy.* Insert $\alpha_k=\alpha/\sqrt k$ into the telescoping bound and estimate the two sums.

Starting from the same expansion with a varying step,
$$
2\alpha_k\bigl(f(x_k)-f^\star\bigr)\le r_k^2-r_{k+1}^2+\alpha_k^2G^2,
$$
and summing over $k=1,\dots,K$,
$$
2\sum_{k=1}^K\alpha_k\bigl(f(x_k)-f^\star\bigr)\le R^2+G^2\sum_{k=1}^K\alpha_k^2 .
$$
For $\alpha_k=\alpha/\sqrt k$,
$\sum_{k\le K}\alpha_k=\alpha\sum_{k\le K}k^{-1/2}\ge\alpha\int_1^{K+1}t^{-1/2}dt=2\alpha(\sqrt{K+1}-1)$
and $\sum_{k\le K}\alpha_k^2=\alpha^2H_K\le\alpha^2(1+\ln K)$. Hence
$$
\min_{k\le K}\bigl(f(x_k)-f^\star\bigr)\le\frac{R^2+G^2\alpha^2(1+\ln K)}{4\alpha(\sqrt{K+1}-1)}=O\!\left(\frac{\ln K}{\sqrt K}\right).
$$
The logarithm comes from $\sum_k\alpha_k^2=\alpha^2\sum_k1/k$, the harmonic sum; the $\sqrt K$ comes from
$\sum_k\alpha_k\asymp2\alpha\sqrt K$. $\blacksquare$

*Remark.* The extra $\ln K$ is an artefact of this proof technique; the sharp rate for $\alpha_k\asymp1/\sqrt k$
is $O(1/\sqrt K)$ under the bounded-second-moment assumption.

**29.**

*Strategy.* Apply the stated criterion to $a=1-\alpha\lambda+\beta$, $b=\beta$.

The criterion is $\lvert b\rvert<1$ and $\lvert a\rvert<1+b$. Here $b=\beta$, so the first condition is $\beta<1$.
The second is
$$
-1-\beta<1-\alpha\lambda+\beta<1+\beta .
$$
The right inequality reduces to $\alpha\lambda>0$, which holds. The left reduces to
$1-\alpha\lambda+\beta>-1-\beta$, that is $\alpha\lambda<2+2\beta$, that is $\alpha<2(1+\beta)/\lambda$. Hence
stability is exactly $\beta<1$ and $\alpha<2(1+\beta)/\lambda$. $\blacksquare$

*Check.* For $\beta=0.5$ and $\lambda=1$ the bound is $\alpha<3$; direct substitution of $\alpha=2.9$ gives
$a=1-2.9+0.5=-1.4$ and $\lvert a\rvert=1.4<1.5=1+b$ ✓, while $\alpha=3.1$ gives $a=-1.6$ and $\lvert a\rvert>1.5$
✗. ✓

**30.**

*Strategy.* Track a change of coordinates through the recursion: write $z=Ax$ and compare gradient descent in
$z$-coordinates with gradient descent in $x$-coordinates.

*Orthogonal case.* Let $U$ be orthogonal, $U^{\mathsf T}U=I$, and define $g(z)=f(U^{\mathsf T}z)$, so that
$\nabla g(z)=U\nabla f(U^{\mathsf T}z)$. If $z_k=Ux_k$ then $U^{\mathsf T}z_k=x_k$ and
$$
z_{k+1}=z_k-\alpha U\nabla f(U^{\mathsf T}z_k)=Ux_k-\alpha U\nabla f(x_k)=U\bigl(x_k-\alpha\nabla f(x_k)\bigr)=Ux_{k+1}.
$$
By induction $z_k=Ux_k$ for all $k$, so the two trajectories are related by the orthogonal map: nothing changes.

*General case.* Let $A$ be invertible and define $g(z)=f(A^{-1}z)$, so $\nabla g(z)=A^{-\mathsf T}\nabla f(A^{-1}z)$.
With $z_k=Ax_k$,
$$
z_{k+1}=z_k-\alpha A^{-\mathsf T}\nabla f(x_k)
\quad\Longrightarrow\quad
x_{k+1}=A^{-1}z_{k+1}=x_k-\alpha\,A^{-1}A^{-\mathsf T}\nabla f(x_k).
$$
The effective step is now the matrix $\alpha A^{-1}A^{-\mathsf T}$, not the scalar $\alpha$: the method is
*preconditioned* gradient descent. The convergence rate is governed by the eigenvalues of
$A^{-1}A^{-\mathsf T}$ times those of $\nabla^2f$, that is by the condition number of the transformed Hessian
$A^{-\mathsf T}\nabla^2f\,A^{-1}$.

*Consequence.* Two parameterisations of the same problem can have wildly different $\kappa$, and choosing $A$ so
that $A^{-\mathsf T}\nabla^2fA^{-1}$ is close to the identity is exactly what preconditioning means. Orthogonal
changes cannot help, because for them $A^{-1}A^{-\mathsf T}=I$: only anisotropy, not rotation, matters.

**31.**

*Strategy.* Telescope the sufficient-decrease inequality and use that $f$ is bounded below.

Theorem 7.2.2 gives $\tfrac{\alpha}{2}\lVert g_k\rVert^2\le f(x_k)-f(x_{k+1})$. Summing over $k=0,\dots,K-1$,
$$
\frac{\alpha}{2}\sum_{k=0}^{K-1}\lVert g_k\rVert^2\le f(x_0)-f(x_K)\le f(x_0)-f^\star<+\infty,
$$
because $f(x_K)\ge f^\star$. Since the partial sums are increasing and bounded above, the series converges:
$\sum_k\lVert g_k\rVert^2<+\infty$. The terms of a convergent series tend to zero, so $\lVert g_k\rVert\to0$ and
$\nabla f(x_k)\to0$. $\blacksquare$

*Remark.* The conclusion is weak: it says the gradients vanish, not that the iterates converge to a minimiser.
The missing step is exactly the one supplied by strong convexity or by a Kurdyka–Łojasiewicz-type inequality.

## Challenge

**32.**

*Strategy.* Run the Adam recursions for eleven steps with the given gradient sequence and compare the sign of the
step with the sign of the current gradient.

For $k\le10$ the gradient is $+1$, so $m_k=1-0.9^k$ and $v_k=1-0.999^k$; the bias-corrected values are
$\hat m_k=1$ and $\hat v_k=1$, and every step is $-0.1$ in $x$.

At $k=11$: $m_{11}=0.9\,m_{10}+0.1(-1)=0.9(0.651322)-0.1=0.486190$, and
$1-0.9^{11}=1-0.313811=0.686189$, so $\hat m_{11}=0.486190/0.686189=0.708535$. Next,
$v_{11}=0.999\,v_{10}+0.001\cdot1=0.999(0.009955)+0.001=0.010945$ and
$1-0.999^{11}=0.010945$, so $\hat v_{11}=1.000$ and $\sqrt{\hat v_{11}}=1$. The step is
$0.1\cdot0.708535=0.0708535$ in the direction $-x$.

The current gradient is $-1$, so the descent direction is $+x$; the step goes in $-x$, which is *uphill*. For a
locally linear objective with gradient $-1$, the increase is
$\lvert\nabla f\rvert\times\lvert\text{step}\rvert=1\times0.07085=0.07085$.

*Conclusion.* Adam is not a descent method: its momentum can point against the current gradient for several steps
after a sign change. This is one reason it has no general convergence guarantee (Section 7.9).

**33.**

*Strategy.* Write $T(B)=K_1(c/B+m)$ and evaluate.

$T(B)=2\times10^5\,(5/B+0.05)$:

| $B$ | $T(B)$ in ms |
|---|---|
| $1$ | $1.01\times10^6$ |
| $10$ | $1.10\times10^5$ |
| $100$ | $2.0\times10^4$ |
| $1000$ | $1.10\times10^4$ |
| $10^4$ | $1.01\times10^4$ |

The limit is $K_1m=10^4$ ms $=10$ s. Being within $5\%$ means $5/B+0.05\le0.0525$, that is $B\ge2000$. So
$B=2000$ is the smallest batch whose time is within $5\%$ of the best possible in this model.

*Comment.* The optimum is at $B=c/m=100$ in the sense that the two terms are equal there, but the *total* is still
twice the limit; the last factor of two costs a batch twenty times larger. This is why very large batches are
rarely worth it.

**34.**

*Strategy.* Use the stability bound $2/L$ and the sufficient bound $1/L$ to bracket the grid; use the loss curve
shapes of Section 7.10 to read the result.

With $L=50$ the threshold is $2/L=0.04$ and the recommended safe rate is $1/L=0.02$. Grid:
$\{10^{-4},3\cdot10^{-4},10^{-3},3\cdot10^{-3},10^{-2},3\cdot10^{-2},10^{-1}\}$. I expect divergence for
$\alpha\ge0.04$, monotone decrease for $\alpha\le0.02$, and oscillation in between.

*What to look for.* The best rate is the largest one whose curve decreases fastest without spikes; the curve for
$\alpha=0.1$ should rise immediately; $\alpha=0.03$ should show a sawtooth.

*If there is a large noise floor.* The loss will flatten at a value proportional to $\alpha\sigma^2$ instead of
decreasing. Then the sweep must be judged on the *floor*, not the initial slope: run each rate long enough to see
where it settles, and prefer a schedule (decay or cosine) that drives $\alpha$ down at the end. A quick check is to
halve the rate: if the final loss halves, the floor dominates; if it is unchanged, the rate is not the limitation.

**35.**

*Strategy.* Convert each rate into an iteration count with logarithms: $k=\ln(1/\varepsilon)/\ln(1/\text{factor})$.

(a) GD with step $1/L$: factor $1-1/\kappa=1-10^{-4}$, so $k\approx\kappa\ln(1/\varepsilon)=10^4\ln(1/\varepsilon)$.

(b) Accelerated: factor $1-1/\sqrt\kappa=0.99$, so $k\approx\sqrt\kappa\ln(1/\varepsilon)=100\ln(1/\varepsilon)$.

| $\varepsilon$ | GD | accelerated | ratio |
|---|---|---|---|
| $10^{-3}$ | $6.9\times10^4$ | $687$ | $100$ |
| $10^{-6}$ | $1.4\times10^5$ | $1374$ | $100$ |
| $10^{-9}$ | $2.1\times10^5$ | $2062$ | $100$ |

The ratio is $\sqrt\kappa=100$, independent of $\varepsilon$: acceleration multiplies the iteration budget by
$\sqrt\kappa$, which for $\kappa=10^4$ is two orders of magnitude. ✓

**36.**

*Strategy.* Match each log to a signature in the table of Section 7.10.

*Run A* $(2.0,1.6,1.55,1.54)$: a small decrease that stalls after step 10 at $1.54$. The stall is either the noise
floor (step too large relative to the gradient noise) or a genuine limitation of the model. The decisive test is to
halve the step: if the loss settles lower, it was the floor; if it stays at $1.54$, the model cannot do better.
A secondary test is to increase the batch, which lowers the floor without changing the model.

*Run B* $(2.0,0.9,0.4,0.39)$: healthy, with a rate that is possibly slightly conservative; the loss falls by a
factor of five and then flattens at $0.39$. The flattening is again a floor question, and a decay schedule would
push it lower. If it flattens at the same value with a smaller step, the remaining error is model bias.

*Run C* $(2.0,3.1,\text{nan},\text{nan})$: divergence. The loss increased from the first step and then overflowed,
so the rate exceeds $2/L$ (or a few samples produce huge gradients). Halve the rate, clip the gradient norm, and
add a warmup; if $L$ can be estimated, set $\alpha\le1/L$.

*The extra measurement.* For "noise floor versus model limitation", the cleanest single measurement is the
**gradient-noise-to-signal ratio**: estimate $\sigma^2$ from the variance of per-sample gradients and compare
$\alpha\sigma^2(1+L\alpha)/2$ with the observed excess loss. If they agree in order of magnitude, the floor is the
cause; if the observed excess is much larger, the model or the features limit performance.
