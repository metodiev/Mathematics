# Second-Order Linear ODEs — Solutions

> [Second-Order Linear ODEs](README.md) · Solutions to the 34 problems in [exercises.md](exercises.md)

Each solution states the strategy, carries out every step and verifies the result by substitution. The
verification is not a formality: in this topic a sign error in the characteristic equation, a missing
factor $x$ in a resonant trial, or a lost factor $x^{2}$ in a Cauchy–Euler equation is invisible until
the answer is differentiated.

## Beginner

**1.** *(a)* $y'' + 3y' + 2y = 0$: **order 2**; **linear**; **homogeneous** ($g \equiv 0$); **constant coefficients**.

*(b)* $y'' + y^{2} = 0$: **order 2**; **nonlinear**, because of the term $y^{2}$ — the operator is not linear and superposition fails. Since the equation is not linear, the words homogeneous/non-homogeneous (in the linear sense) do not apply; the right side happens to be zero, but that is not enough to make the solution set a vector space. It is autonomous (no $x$ appears) and has constant coefficients in the informal sense that nothing depends on $x$.

*(c)* $x^{2}y'' + xy' + y = 0$: **order 2**; **linear**; **homogeneous**; **variable coefficients** — specifically a Cauchy–Euler equation, since the coefficient of $y^{(k)}$ is a constant multiple of $x^{k}$.

*(d)* $y'' + y = \sin x$: **order 2**; **linear**; **non-homogeneous** ($g = \sin x \ne 0$); **constant coefficients**.

The classification matters because each label selects a method: (a) and (d) go to the characteristic equation, (c) to the Cauchy–Euler substitution, and (b) to none of the linear theory at all.

*Check of the labels by the superposition test.* For (b), $L[y] = y'' + y^{2}$: with $y \equiv 1$ we get $L[1] = 1$, but $L[2] = 0 + 4 = 4 \ne 2\cdot1$ ✗, which is precisely the failure of linearity. For (a) and (d) the operator is $y'' + py' + qy$ with $p, q$ constant, so $L[c_{1}y_{1} + c_{2}y_{2}] = c_{1}L[y_{1}] + c_{2}L[y_{2}]$ ✓; the presence of the right side $g = \sin x$ in (d) makes the equation non-homogeneous but does not affect linearity ✓. For (c), $L[y] = x^{2}y'' + xy' + y$ is linear with coefficients depending on $x$ ✓, and $L[x^{m}] = [m(m-1) + m + 1]x^{m}$ exhibits the indicial structure that §7.6 exploits.

**2.** *Strategy: constant coefficients, so write the characteristic equation.*

$$r^{2} - 5r + 6 = (r-2)(r-3) = 0 \;\Longrightarrow\; r_{1} = 2, \; r_{2} = 3 .$$

Distinct real roots, so the fundamental set is $e^{2x}, e^{3x}$ and

$$y = c_{1}e^{2x} + c_{2}e^{3x}, \qquad x \in \mathbb{R} .$$

*Check:* $W = 3e^{5x} - 2e^{5x} = e^{5x} \ne 0$ ✓. Substituting $y = e^{rx}$ gives $(r^{2} - 5r + 6)e^{rx} = 0$ for $r = 2, 3$ ✓, and superposition handles the constants ✓.

*Behaviour:* both roots are positive, so every nonzero solution grows like $e^{3x}$ as $x \to \infty$; the equation is unstable.

**3.** *Strategy: constant coefficients; the characteristic equation has no real roots.*

$$r^{2} + 9 = 0 \;\Longrightarrow\; r = \pm 3i, \qquad \alpha = 0, \; \beta = 3 .$$

Complex roots with zero real part give pure oscillation:

$$y = c_{1}\cos 3x + c_{2}\sin 3x, \qquad x \in \mathbb{R} .$$

*Check:* $W(\cos 3x, \sin 3x) = 3\cos^{2}3x + 3\sin^{2}3x = 3 \ne 0$ ✓; and $(\cos 3x)'' + 9\cos 3x = -9\cos 3x + 9\cos 3x = 0$ ✓, likewise for $\sin 3x$.

*Amplitude–phase form:* $y = R\cos(3x - \varphi)$ with $R = \sqrt{c_{1}^{2}+c_{2}^{2}}$; the motion is periodic with period $2\pi/3$.

**4.** *Strategy: the discriminant vanishes, so this is the repeated-root case.*

$$r^{2} - 4r + 4 = (r-2)^{2} = 0 \;\Longrightarrow\; r = 2 \text{ (double)} .$$

By §7.2 a fundamental set is $e^{2x}$ and $xe^{2x}$, hence

$$y = \left(c_{1} + c_{2}x\right)e^{2x}, \qquad x \in \mathbb{R} .$$

*Check:* with $y = xe^{2x}$ we computed $y' = (1+2x)e^{2x}$ and $y'' = (4+4x)e^{2x}$, so

$$y'' - 4y' + 4y = \left[(4+4x) - 4(1+2x) + 4x\right]e^{2x} = 0 \;\checkmark$$

and $W(e^{2x}, xe^{2x}) = e^{4x} \ne 0$ ✓.

*Remark:* the factor $x$ is the derivative $\partial_{r}e^{rx}$ at $r = 2$; it is not an extra guess but the limit of the two distinct exponentials as their roots coalesce.

**5.** *Characteristic equation.* $r^{2} + 1 = 0$, so $r = \pm i$ and

$$y = c_{1}\cos x + c_{2}\sin x .$$

*Initial conditions.* $y(0) = c_{1} = 2$; $y' = -c_{1}\sin x + c_{2}\cos x$ gives $y'(0) = c_{2} = -1$. Hence

$$y = 2\cos x - \sin x, \qquad x \in \mathbb{R} .$$

*Check:* $y' = -2\sin x - \cos x$ and $y'' = -2\cos x + \sin x = -y$ ✓; $y(0) = 2$ ✓, $y'(0) = -1$ ✓.

*Amplitude–phase form:* $R = \sqrt{4+1} = \sqrt5$ and

$$y = \sqrt5\cos\left(x - \varphi\right), \qquad \tan\varphi = \frac{c_{2}}{c_{1}} = -\frac12, \quad \varphi \approx -0.464 .$$

The motion has amplitude $\sqrt5 \approx 2.24$ and period $2\pi$.

**6.** *Characteristic equation.* $r^{2} - r - 2 = (r-2)(r+1) = 0$, so $r_{1} = 2$, $r_{2} = -1$ and

$$y = c_{1}e^{2x} + c_{2}e^{-x} .$$

*Initial conditions.* $y(0) = c_{1} + c_{2} = 0$ and $y'(0) = 2c_{1} - c_{2} = 3$. From the first, $c_{2} = -c_{1}$; substituting, $3c_{1} = 3$, so $c_{1} = 1$ and $c_{2} = -1$:

$$y = e^{2x} - e^{-x}, \qquad x \in \mathbb{R} .$$

*Check:* $y' = 2e^{2x} + e^{-x}$ and $y'' = 4e^{2x} - e^{-x}$, so $y'' - y' - 2y = (4 - 2 - 2)e^{2x} + (-1 - 1 + 2)e^{-x} = 0$ ✓; $y(0) = 0$ ✓ and $y'(0) = 3$ ✓.

*Remark:* the two roots have opposite signs, so the solution is a difference of a growing and a decaying exponential; it grows without bound as $x \to \infty$ and as $x \to -\infty$ (where $-e^{-x}$ dominates), so it is unbounded on both sides.

**7.** *(a)* $y_{1} = e^{2x}$, $y_{2} = e^{3x}$:

$$W = e^{2x}\cdot 3e^{3x} - 2e^{2x}\cdot e^{3x} = \left(3-2\right)e^{5x} = e^{5x} \ne 0 .$$

The pair is a **fundamental set** for $y'' - 5y' + 6y = 0$ — the equation whose characteristic roots are $2$ and $3$.

*(b)* $y_{1} = x$, $y_{2} = 2x$:

$$W = x\cdot 2 - 1\cdot 2x = 0 .$$

The pair is **not** a fundamental set; indeed $y_{2} = 2y_{1}$, so they are linearly dependent and span only a line in the solution space. (They are both solutions of any equation having $x$ as a solution, for instance $x^{2}y'' - xy' + y = 0$.)

*(c)* $y_{1} = \cos 2x$, $y_{2} = \sin 2x$:

$$W = \cos 2x\cdot 2\cos 2x - \left(-2\sin 2x\right)\sin 2x = 2\left(\cos^{2}2x + \sin^{2}2x\right) = 2 \ne 0 .$$

The pair is a **fundamental set** for $y'' + 4y = 0$.

*Consistency with Abel.* For (a), $p = -5$ and $W = W_{0}e^{-\int p} = e^{5x}$ ✓; for (c), $p = 0$ and $W$ is constant ✓. In (b) the Wronskian is identically zero, which by Abel can only happen if the pair is everywhere dependent ✓.

**8.** *Verification.* For $y_{1} = e^{x}$: $y_{1}' = y_{1}'' = e^{x}$, so $y_{1}'' - 2y_{1}' + y_{1} = (1 - 2 + 1)e^{x} = 0$ ✓.

For $y_{2} = xe^{x}$: $y_{2}' = (1+x)e^{x}$ and $y_{2}'' = (2+x)e^{x}$, so

$$y_{2}'' - 2y_{2}' + y_{2} = \left[(2+x) - 2(1+x) + x\right]e^{x} = 0 \;\checkmark$$

*Independence.* $W = e^{x}(1+x)e^{x} - e^{x}\cdot xe^{x} = e^{2x} \ne 0$ for every $x$, so the pair is linearly independent on $\mathbb{R}$.

*Which theorem.* **Theorem 7.1** (the solution space of a second-order homogeneous linear equation is two-dimensional): two independent solutions already span a two-dimensional subspace of a space of dimension $2$, so they span everything. Concretely, every solution can be written $\left(c_{1} + c_{2}x\right)e^{x}$.

*Remark:* this is the repeated-root case of $r^{2} - 2r + 1 = (r-1)^{2} = 0$, and the pair $\{e^{x}, xe^{x}\}$ is exactly the fundamental set that §7.2 produces from $r = 1$.

**9.** *Homogeneous part.* $r^{2} - 3r + 2 = (r-1)(r-2) = 0$, so $y_{h} = c_{1}e^{x} + c_{2}e^{2x}$.

*Particular solution.* The forcing is a polynomial of degree $1$ and $0$ is not a root, so try $y_{p} = Ax + B$. Then $y_{p}' = A$, $y_{p}'' = 0$ and

$$0 - 3A + 2\left(Ax + B\right) = 2Ax + \left(2B - 3A\right) \overset{!}{=} 4x .$$

Matching coefficients: $2A = 4$, so $A = 2$; and $2B - 3A = 0$, so $B = 3$. Hence $y_{p} = 2x + 3$ and

$$y = c_{1}e^{x} + c_{2}e^{2x} + 2x + 3 .$$

*Check:* $y_{p}'' - 3y_{p}' + 2y_{p} = 0 - 6 + 2(2x+3) = 4x$ ✓. A useful check on the rules: the trial had the same degree as the forcing and was not multiplied by $x$, because $0$ is not a characteristic root ✓.

**10.** *Homogeneous part.* $r^{2} + 4 = 0$, so $y_{h} = c_{1}\cos 2x + c_{2}\sin 2x$.

*Particular solution.* The forcing is the constant $8$, a polynomial of degree $0$, and $0$ is not a root, so try the constant $y_{p} = A$:

$$0 + 4A = 8 \;\Longrightarrow\; A = 2 .$$

Hence

$$y = c_{1}\cos 2x + c_{2}\sin 2x + 2 .$$

*Check:* $y_{p}'' + 4y_{p} = 0 + 8 = 8$ ✓.

*Reading the answer:* the constant $2$ is the equilibrium position the spring would take under a constant force $8$ with stiffness $4$ — the static deflection $F/k$, as expected from the amplitude formula at $\omega = 0$ ✓.

**11.** *Homogeneous part.* $r^{2} - 1 = 0$, so $y_{h} = c_{1}e^{x} + c_{2}e^{-x}$.

*Particular solution.* $g = e^{2x}$ is $P_{0}e^{\alpha x}$ with $\alpha = 2$, which is not a root ($\pm1$ are the roots), so $s = 0$ and the trial is $y_{p} = Ae^{2x}$:

$$4Ae^{2x} - Ae^{2x} = 3Ae^{2x} \overset{!}{=} e^{2x} \;\Longrightarrow\; A = \tfrac13 .$$

Hence

$$y = c_{1}e^{x} + c_{2}e^{-x} + \tfrac13 e^{2x} .$$

*Check:* $y_{p}'' - y_{p} = \tfrac43e^{2x} - \tfrac13e^{2x} = e^{2x}$ ✓.

*Remark:* the coefficient is $1/(\alpha^{2} - 1) = 1/(4-1)$, that is $1/P(\alpha)$ where $P$ is the characteristic polynomial — the general formula for the non-resonant exponential case.

**12.** *Strategy: Cauchy–Euler, so try $y = x^{m}$.*

$$y' = mx^{m-1}, \quad y'' = m(m-1)x^{m-2} \;\Longrightarrow\; x^{2}y'' - 3xy' + 4y = \left[m(m-1) - 3m + 4\right]x^{m} .$$

The indicial equation is

$$m^{2} - 4m + 4 = (m-2)^{2} = 0,$$

a double root $m = 2$. By §7.6 the fundamental set is $x^{2}$ and $x^{2}\ln x$, so

$$y = \left(c_{1} + c_{2}\ln x\right)x^{2}, \qquad x > 0 .$$

*Check:* with $y = x^{2}$: $y' = 2x$, $y'' = 2$, and $2x^{2} - 6x^{2} + 4x^{2} = 0$ ✓. With $y = x^{2}\ln x$: $y' = 2x\ln x + x$, $y'' = 2\ln x + 3$, and

$$x^{2}\left(2\ln x + 3\right) - 3x\left(2x\ln x + x\right) + 4x^{2}\ln x = x^{2}\left(2\ln x + 3 - 6\ln x - 3 + 4\ln x\right) = 0 \;\checkmark$$

*Remark:* the double root produces $\ln x$ exactly as $t = \ln x$ predicts — in the $t$-variable the equation is $\ddot{y} - 4\dot{y} + 4y = 0$, whose repeated root contributes $te^{2t} = x^{2}\ln x$.

## Intermediate

**13.** *Homogeneous part.* $r^{2} - 3r + 2 = (r-1)(r-2) = 0$, so $y_{h} = c_{1}e^{x} + c_{2}e^{2x}$.

*Particular solution.* The forcing is $e^{3x}$, i.e. $P_{0}e^{\alpha x}$ with $\alpha = 3$. Since $3$ is not a root, $s = 0$ and $y_{p} = Ae^{3x}$:

$$9Ae^{3x} - 9Ae^{3x} + 2Ae^{3x} = 2Ae^{3x} \overset{!}{=} e^{3x} \;\Longrightarrow\; A = \tfrac12 .$$

Hence

$$y = c_{1}e^{x} + c_{2}e^{2x} + \tfrac12 e^{3x} .$$

*Check:* $\left(\tfrac12e^{3x}\right)'' - 3\left(\tfrac12e^{3x}\right)' + 2\left(\tfrac12e^{3x}\right) = \tfrac92e^{3x} - \tfrac92e^{3x} + e^{3x} = e^{3x}$ ✓. The coefficient is $1/P(3)$ with $P(r) = r^{2}-3r+2$, that is $1/(9-9+2) = \tfrac12$ ✓.

**14.** *Homogeneous part.* $r^{2} + 9 = 0$ gives $y_{h} = c_{1}\cos 3x + c_{2}\sin 3x$.

*Why this is resonant.* The forcing is $6\cos 3x$, and $\pm 3i$ are the characteristic roots, so the naive trial $A\cos 3x + B\sin 3x$ is annihilated by $L$ and cannot equal $6\cos 3x$. This is $s = 1$ in Theorem 8.4, and the trial must be

$$y_{p} = x\left(A\cos 3x + B\sin 3x\right).$$

*Substitution.* Differentiating the product,

$$y_{p}' = \left(A + 3Bx\right)\cos 3x + \left(B - 3Ax\right)\sin 3x,$$

$$y_{p}'' = \left(6B - 9Ax\right)\cos 3x - \left(6A + 9Bx\right)\sin 3x,$$

so

$$y_{p}'' + 9y_{p} = 6B\cos 3x - 6A\sin 3x \overset{!}{=} 6\cos 3x \;\Longrightarrow\; B = 1, \; A = 0 .$$

Hence $y_{p} = x\sin 3x$ and

$$y = c_{1}\cos 3x + c_{2}\sin 3x + x\sin 3x .$$

*Check:* $y_{p}' = \sin 3x + 3x\cos 3x$, $y_{p}'' = 6\cos 3x - 9x\sin 3x$, and $y_{p}'' + 9y_{p} = 6\cos 3x$ ✓.

*Reading the answer:* the amplitude of the resonant term grows linearly, and the response is a $\sin$ while the forcing is a $\cos$ — a quarter-period phase lag, the finite-damping version of the $\pi/2$ lag at $\omega = \omega_{0}$. The factor $x$ is the algebraic fingerprint of resonance.

**15.** *Homogeneous part.* $y_{1} = \cos 2x$, $y_{2} = \sin 2x$, and $W = 2$.

*Variation of parameters.* With $g = \csc 2x$,

$$u_{1}' = -\frac{y_{2}g}{W} = -\frac{\sin 2x\cdot\csc 2x}{2} = -\frac12, \qquad u_{2}' = \frac{y_{1}g}{W} = \frac{\cos 2x}{2\sin 2x} = \frac12\cot 2x .$$

Hence $u_{1} = -\tfrac{x}{2}$ and $u_{2} = \tfrac14\ln\left\lvert\sin 2x\right\rvert$, so

$$y_{p} = -\frac{x}{2}\cos 2x + \frac14\sin 2x\,\ln\left\lvert\sin 2x\right\rvert,$$

and the general solution on any interval where $\sin 2x > 0$ is

$$y = c_{1}\cos 2x + c_{2}\sin 2x - \frac{x}{2}\cos 2x + \frac14\sin 2x\,\ln\left(\sin 2x\right) .$$

*Check:* with $y_{p} = -\tfrac{x}{2}\cos 2x + \tfrac14\sin 2x\ln\sin 2x$,

$$y_{p}' = -\tfrac12\cos 2x + x\sin 2x + \tfrac12\cos 2x\ln\sin 2x + \tfrac12\cos 2x = x\sin 2x + \tfrac12\cos 2x\ln\sin 2x,$$

$$y_{p}'' = \sin 2x + 2x\cos 2x - \sin 2x\ln\sin 2x + \frac{\cos^{2}2x}{\sin 2x}.$$

Adding $4y_{p} = -2x\cos 2x + \sin 2x\ln\sin 2x$, the $x\cos 2x$ and $\ln\sin 2x$ terms cancel and

$$y_{p}'' + 4y_{p} = \sin 2x + \frac{\cos^{2}2x}{\sin 2x} = \frac{\sin^{2}2x + \cos^{2}2x}{\sin 2x} = \frac{1}{\sin 2x} = \csc 2x \;\checkmark$$

*Remark:* undetermined coefficients is not available here, because $\csc 2x$ is not a polynomial times an exponential times a sine or cosine. The solution contains $\ln(\sin 2x)$, a new function, which is exactly what the integrals in the formula produce.

**16.** *Homogeneous part.* $y_{1} = \cos x$, $y_{2} = \sin x$, $W = 1$.

*Variation of parameters.* With $g = \sec x$,

$$u_{1}' = -\frac{\sin x\sec x}{1} = -\tan x \;\Longrightarrow\; u_{1} = \ln\left\lvert\cos x\right\rvert, \qquad u_{2}' = \frac{\cos x\sec x}{1} = 1 \;\Longrightarrow\; u_{2} = x .$$

Therefore

$$y_{p} = \cos x\,\ln\left\lvert\cos x\right\rvert + x\sin x, \qquad y = c_{1}\cos x + c_{2}\sin x + \cos x\ln\left(\cos x\right) + x\sin x,$$

where the logarithm is real on $\left(-\tfrac{\pi}{2},\tfrac{\pi}{2}\right)$, since $\cos x > 0$ there.

*Check:* $y_{p}' = -\sin x\ln\cos x - \sin x + \sin x + x\cos x = -\sin x\ln\cos x + x\cos x$ and

$$y_{p}'' = -\cos x\ln\cos x + \frac{\sin^{2}x}{\cos x} + \cos x - x\sin x,$$

so

$$y_{p}'' + y_{p} = \frac{\sin^{2}x}{\cos x} + \cos x = \frac{\sin^{2}x + \cos^{2}x}{\cos x} = \sec x \;\checkmark$$

*Remark:* the term $x\sin x$ is a resonant-looking response, and indeed $\sec x$ has no Fourier component problem here — the logarithmic term is the non-resonant part, the linear one the resonant. Compare with Example 9.4, where a pure cosine forcing at the natural frequency produced $x\sin x$ alone.

**17.** *Standard form.* Dividing $x^{2}y'' - 3xy' + 4y = 0$ by $x^{2}$ gives $y'' - \dfrac{3}{x}y' + \dfrac{4}{x^{2}}y = 0$, so $p = -3/x$ and

$$e^{-\int p\,dx} = e^{3\ln x} = x^{3} .$$

*Reduction of order.* With $y_{1} = x^{2}$,

$$y_{2} = y_{1}\int\frac{x^{3}}{x^{4}}\,dx = x^{2}\int\frac{dx}{x} = x^{2}\ln x .$$

*Check:* $y_{2}' = 2x\ln x + x$, $y_{2}'' = 2\ln x + 3$, and

$$x^{2}\left(2\ln x + 3\right) - 3x\left(2x\ln x + x\right) + 4x^{2}\ln x = 0 \;\checkmark$$

$W(x^{2}, x^{2}\ln x) = x^{2}\left(2x\ln x + x\right) - 2x\cdot x^{2}\ln x = x^{3} \ne 0$ ✓, so

$$y = \left(c_{1} + c_{2}\ln x\right)x^{2}, \qquad x > 0 .$$

*Consistency checks:* this agrees with problem 12, as it must — the same equation — and it agrees with what the indicial equation predicts, $m = 2$ double ✓. The Wronskian $x^{3}$ also matches Abel's formula, $W = W_{0}e^{-\int p} = W_{0}x^{3}$ ✓.

**18.** *Homogeneous part.* The indicial equation is $m(m-1) + m - 1 = m^{2} - 1 = 0$, so $m = \pm1$ and $y_{h} = c_{1}x + \dfrac{c_{2}}{x}$.

*Particular solution.* The right side $x = x^{1}$ is itself a homogeneous solution (the indicial root $m = 1$), so the naive trial $Ax$ is annihilated. The next attempt is the power times a logarithm,

$$y_{p} = Ax\ln x \;\Longrightarrow\; y_{p}' = A\left(\ln x + 1\right), \quad y_{p}'' = \frac{A}{x} .$$

Then

$$x^{2}\cdot\frac{A}{x} + x\cdot A\left(\ln x + 1\right) - Ax\ln x = Ax + Ax\ln x + Ax - Ax\ln x = 2Ax \overset{!}{=} x \;\Longrightarrow\; A = \tfrac12 .$$

Hence

$$y = c_{1}x + \frac{c_{2}}{x} + \frac{x\ln x}{2}, \qquad x > 0 .$$

*Check by the $t$-route.* With $x = e^{t}$ the equation becomes $\ddot{y} - y = e^{t}$, and since $e^{t}$ solves the homogeneous equation the trial is $Ate^{t}$, which gives $2Ae^{t} = e^{t}$, so $A = \tfrac12$ and $y_{p} = \tfrac12te^{t} = \tfrac12x\ln x$ ✓.

*Remark:* the factor $\ln x$ appears for the same reason as in problem 12 — a degeneracy of the indicial equation with the forcing's exponent. Here the double root is between the homogeneous power and the forcing, which is the Cauchy–Euler analogue of resonance.

**19.** *Characteristic equation.* $r^{2} + 2r + 5 = 0$, so

$$r = \frac{-2 \pm \sqrt{4 - 20}}{2} = -1 \pm 2i .$$

Hence

$$y = e^{-x}\left(c_{1}\cos 2x + c_{2}\sin 2x\right), \qquad x \in \mathbb{R} .$$

*Damping ratio.* Comparing with $\ddot{y} + 2\zeta\omega_{0}\dot{y} + \omega_{0}^{2}y = 0$ gives $\omega_{0}^{2} = 5$ and $2\zeta\omega_{0} = 2$, so

$$\omega_{0} = \sqrt5 \approx 2.236\ \mathrm{rad/s}, \qquad \zeta = \frac{2}{2\sqrt5} = \frac{1}{\sqrt5} \approx 0.447 .$$

Since $0 < \zeta < 1$ the system is **underdamped**: it oscillates with damped frequency $\omega_{d} = \omega_{0}\sqrt{1-\zeta^{2}} = 2$, inside an envelope decaying like $e^{-x}$ with time constant $1/(\zeta\omega_{0}) = 1$.

*Amplitude–phase form.* $y = Re^{-x}\cos\left(2x - \varphi\right)$ with $R = \sqrt{c_{1}^{2}+c_{2}^{2}}$ and $\tan\varphi = c_{2}/c_{1}$.

*Check:* for $y = e^{-x}\cos 2x$, $y' = -e^{-x}\cos 2x - 2e^{-x}\sin 2x$ and $y'' = e^{-x}\left(-3\cos 2x + 4\sin 2x\right)$, so $y'' + 2y' + 5y = e^{-x}\left(-3\cos + 4\sin - 2\cos - 4\sin + 5\cos\right) = 0$ ✓.

**20.** *Homogeneous part.* $r^{2} + 2r + 1 = (r+1)^{2} = 0$, so $y_{h} = \left(c_{1} + c_{2}x\right)e^{-x}$.

*Particular solution.* Neither $i$ nor $-i$ is a root, so $s = 0$ and $y_{p} = A\cos x + B\sin x$:

$$y_{p}'' + 2y_{p}' + y_{p} = \left(-A\cos x - B\sin x\right) + 2\left(-A\sin x + B\cos x\right) + \left(A\cos x + B\sin x\right) = 2B\cos x - 2A\sin x .$$

Matching $4\cos x$ gives $B = 2$ and $A = 0$, so $y_{p} = 2\sin x$ and

$$y = \left(c_{1} + c_{2}x\right)e^{-x} + 2\sin x .$$

*Check:* $y_{p}'' + 2y_{p}' + y_{p} = -2\sin x + 4\cos x + 2\sin x = 4\cos x$ ✓.

*Reading the answer:* the forcing is at frequency $1$ and the homogeneous frequency is $1$ as well (critical damping, roots $-1$), yet there is no resonance: resonance requires the *complex* forcing frequency $i\omega$ to be a characteristic root, and the only root is $-1$. The response is bounded, and the $2\sin x$ is a phase-shifted multiple of the forcing.

**21.** *Homogeneous part.* $r^{2} + 4r + 5 = 0$ gives $r = -2 \pm i$, so $y_{h} = e^{-2t}\left(c_{1}\cos t + c_{2}\sin t\right)$.

*Particular solution.* The forcing frequency is $1$; the roots are $-2 \pm i$, which are not $\pm i$, so $s = 0$ and $y_{p} = A\cos t + B\sin t$:

$$y_{p}'' + 4y_{p}' + 5y_{p} = \left(-A\cos t - B\sin t\right) + 4\left(-A\sin t + B\cos t\right) + 5\left(A\cos t + B\sin t\right) = \left(4A + 4B\right)\cos t + \left(4B - 4A\right)\sin t .$$

Matching $10\cos t$: $A + B = \tfrac52$ and $B - A = 0$, so $A = B = \tfrac54$ and

$$y = e^{-2t}\left(c_{1}\cos t + c_{2}\sin t\right) + \tfrac54\left(\cos t + \sin t\right) .$$

*Steady-state amplitude and phase.* Combining, $\tfrac54\left(\cos t + \sin t\right) = \tfrac{5\sqrt2}{4}\cos\left(t - \tfrac{\pi}{4}\right)$, so the amplitude is $\tfrac{5\sqrt2}{4} \approx 1.77$ and the lag is $\varphi = \tfrac{\pi}{4}$.

*Check against the formula.* $F_{0}/m = 10$, $\omega_{0}^{2} = 5$, $2\zeta\omega_{0} = 4$, $\omega = 1$: $A = \dfrac{10}{\sqrt{(5-1)^{2} + 4^{2}}} = \dfrac{10}{\sqrt{32}} = \dfrac{10}{4\sqrt2} = \dfrac{5\sqrt2}{4}$ ✓ and $\tan\varphi = \dfrac{4}{4} = 1$, so $\varphi = \pi/4$ ✓.

*Remark:* although the forcing frequency equals the *damped* frequency, this is not resonance. The steady state is finite, and its amplitude is exactly what the impedance formula predicts.

**22.** *Homogeneous part.* $y_{h} = c_{1}\cos 3t + c_{2}\sin 3t$.

*Particular solution.* The forcing is $5\sin 2t$ and $\pm 2i$ are not roots, so $y_{p} = A\sin 2t$:

$$-4A\sin 2t + 9A\sin 2t = 5A\sin 2t \overset{!}{=} 5\sin 2t \;\Longrightarrow\; A = 1 .$$

*Initial conditions.* $y = c_{1}\cos 3t + c_{2}\sin 3t + \sin 2t$, so $y(0) = c_{1} = 0$ and $y'(0) = 3c_{2} + 2 = 0$, giving $c_{2} = -\tfrac23$. Hence

$$y = \sin 2t - \tfrac23\sin 3t .$$

*Check:* $y'' = -4\sin 2t + 6\sin 3t$ and $9y = 9\sin 2t - 6\sin 3t$, so $y'' + 9y = 5\sin 2t$ ✓; $y(0) = 0$ ✓; $y'(0) = 2 - 2 = 0$ ✓.

*Shape of the graph.* The two frequencies are $2$ and $3$ rad/s, so

$$\sin 2t - \tfrac23\sin 3t = \underbrace{\sin 2t - \sin 3t}_{\text{beats}} + \underbrace{\tfrac13\sin 3t}_{\text{drift}} .$$

The beat part is $2\sin\left(-\tfrac{t}{2}\right)\cos\left(\tfrac{5t}{2}\right)$, a fast oscillation at the mean frequency $2.5$ inside an envelope of period $4\pi$; the small extra $\tfrac13\sin 3t$ spoils exact periodicity but not the visible "fast inside slow" pattern. Since the forcing frequency $2$ differs from the natural frequency $3$, there is no resonant growth: the motion stays bounded, with maximum amplitude $1 + \tfrac23 = \tfrac53$ by the triangle inequality.

## Advanced

**23.** *Strategy: prove the three vector-space axioms, then the two dimension inequalities separately.*

Let $I$ be an interval and $p, q : I \to \mathbb{R}$ continuous. Put
$\mathcal{S} = \{y \in C^{2}(I) : y'' + py' + qy = 0 \text{ on } I\}$, where $C^{2}(I)$ is the set of twice continuously differentiable functions on $I$.

**(1) $\mathcal{S}$ is a subspace.** The zero function lies in $\mathcal{S}$. If $y_{1}, y_{2} \in \mathcal{S}$ and $c_{1}, c_{2} \in \mathbb{R}$, then

$$L[c_{1}y_{1} + c_{2}y_{2}] = c_{1}L[y_{1}] + c_{2}L[y_{2}] = 0 + 0 = 0,$$

because differentiation and multiplication by the fixed functions $p, q$ are linear. So $\mathcal{S}$ is closed under linear combinations and is a vector space.

**(2) $\dim \mathcal{S} \le 2$.** Let $y_{1}, y_{2} \in \mathcal{S}$ be a fundamental set and fix $x_{0} \in I$. Given $y \in \mathcal{S}$, consider

$$c_{1}y_{1}(x_{0}) + c_{2}y_{2}(x_{0}) = y(x_{0}), \qquad c_{1}y_{1}'(x_{0}) + c_{2}y_{2}'(x_{0}) = y'(x_{0}).$$

This $2 \times 2$ system has determinant $W(y_{1},y_{2})(x_{0}) \ne 0$, so it has a unique solution $(c_{1}, c_{2})$. The function $\tilde{y} = c_{1}y_{1} + c_{2}y_{2}$ lies in $\mathcal{S}$ and satisfies $\tilde{y}(x_{0}) = y(x_{0})$, $\tilde{y}'(x_{0}) = y'(x_{0})$. Both $y$ and $\tilde{y}$ solve the same initial value problem, so by Theorem 5.1 (uniqueness) they are equal. Hence $y \in \operatorname{span}\{y_{1},y_{2}\}$.

**(3) $\dim \mathcal{S} \ge 2$.** By Theorem 5.1, the IVP with data $y(x_{0}) = 1$, $y'(x_{0}) = 0$ has a solution $y_{1} \in \mathcal{S}$, and the IVP with data $y(x_{0}) = 0$, $y'(x_{0}) = 1$ has a solution $y_{2} \in \mathcal{S}$. Then

$$W(y_{1},y_{2})(x_{0}) = y_{1}(x_{0})y_{2}'(x_{0}) - y_{1}'(x_{0})y_{2}(x_{0}) = 1\cdot1 - 0\cdot0 = 1 \ne 0,$$

so $y_{1}, y_{2}$ are linearly independent. Therefore $\dim \mathcal{S} \ge 2$.

Combining (2) and (3), $\dim \mathcal{S} = 2$. $\blacksquare$

*Remark on where each hypothesis is used.* Continuity of $p, q$ is used only through the existence–uniqueness theorem in (2) and (3); linearity is used in (1). Drop continuity and the dimension can drop: the equation $x^{2}y'' - 2y = 0$ on an interval containing $0$ has coefficients that blow up at the origin, and solutions defined across $0$ are constrained. Its general solution on either half-line is $c_{1}x^{2} + c_{2}/x$, and only the term $x^{2}$ survives at the origin, so the space of solutions defined on an interval about $0$ is only one-dimensional.

*Check on the model example.* For $y'' - y = 0$ with $x_{0} = 0$, the proof's two special solutions are $\cosh x$ (data $1, 0$) and $\sinh x$ (data $0, 1$), and

$$W\left(\cosh x, \sinh x\right) = \cosh^{2}x - \sinh^{2}x = 1 \ne 0 \;\checkmark$$

so they are a basis, and indeed every solution is $c_{1}\cosh x + c_{2}\sinh x = A e^{x} + B e^{-x}$ ✓.

**24.** *Abel's identity.* Let $y_{1}, y_{2}$ solve $y'' + p(x)y' + q(x)y = 0$. Differentiate $W = y_{1}y_{2}' - y_{1}'y_{2}$:

$$W' = y_{1}'y_{2}' + y_{1}y_{2}'' - y_{1}''y_{2} - y_{1}'y_{2}' = y_{1}y_{2}'' - y_{1}''y_{2} .$$

Substituting $y_{i}'' = -py_{i}' - qy_{i}$,

$$W' = y_{1}\left(-py_{2}' - qy_{2}\right) - \left(-py_{1}' - qy_{1}\right)y_{2} = -p\left(y_{1}y_{2}' - y_{1}'y_{2}\right) = -pW .$$

This is a first-order linear equation for $W$, solved by separation:

$$\frac{W'}{W} = -p \;\Longrightarrow\; \ln\left\lvert W\right\rvert = -\int p\,dx + \text{const} \;\Longrightarrow\; W(x) = W(x_{0})e^{-\int_{x_{0}}^{x}p(s)\,ds} .$$

*The dichotomy.* An exponential is never zero, so:

* if $W(x_{0}) = 0$, then $W(x) = 0$ for every $x \in I$;
* if $W(x_{0}) \ne 0$, then $W(x) \ne 0$ for every $x \in I$.

There is no intermediate case: the Wronskian of two solutions of a second-order linear equation either vanishes identically or never vanishes.

*The vanishing corollary.* Suppose $y_{1}, y_{2}$ solve the same homogeneous equation and $y_{1}(x_{0}) = y_{2}(x_{0}) = 0$. Then

$$W(x_{0}) = y_{1}(x_{0})y_{2}'(x_{0}) - y_{1}'(x_{0})y_{2}(x_{0}) = 0 - 0 = 0,$$

so $W \equiv 0$ on $I$ by the dichotomy, which is exactly the criterion for linear dependence of two solutions. Equivalently: both solve the IVP with data $(0, y_{1}'(x_{0}))$ and $(0, y_{2}'(x_{0}))$; if the derivatives differ, uniqueness fails, which is impossible; so one is a multiple of the other. $\blacksquare$

*Remark:* the second argument is instructive — the Wronskian criterion and uniqueness are not independent theorems but two views of the same fact.

*Check on examples.* For $y'' - y = 0$ we have $p = 0$, so $W$ must be constant: indeed $W(e^{x}, e^{-x}) = e^{x}(-e^{-x}) - e^{x}e^{-x} = -2$ ✓. For $x^{2}y'' - 2xy' + 2y = 0$ we have $p = -2/x$, so $W = W_{0}e^{2\ln x} = W_{0}x^{2}$; directly, $W(x, x^{2}) = x\cdot2x - 1\cdot x^{2} = x^{2}$ ✓. In the second example $W$ vanishes at $x = 0$ but not on either half-line $x > 0$ or $x < 0$ — a reminder that Abel's identity is stated on an interval that avoids the singular point ✓.

**25.** *Standard form.* Dividing $m\ddot{y} + c\dot{y} + ky = F_{0}\cos\omega t$ by $m$ and setting

$$\omega_{0} = \sqrt{\frac{k}{m}}, \qquad \zeta = \frac{c}{2\sqrt{mk}} \;\left(\text{so } 2\zeta\omega_{0} = \frac{c}{m}\right),$$

gives $\ddot{y} + 2\zeta\omega_{0}\dot{y} + \omega_{0}^{2}y = \dfrac{F_{0}}{m}\cos\omega t$.

*Complex ansatz.* Write the forcing as $\operatorname{Re}\left[(F_{0}/m)e^{i\omega t}\right]$ and seek $y_{p} = \operatorname{Re}\left[Ye^{i\omega t}\right]$. Substituting, $e^{i\omega t}\left(-\omega^{2} + 2i\zeta\omega_{0}\omega + \omega_{0}^{2}\right)Y = \dfrac{F_{0}}{m}e^{i\omega t}$, so

$$Y = \frac{F_{0}/m}{\left(\omega_{0}^{2}-\omega^{2}\right) + 2i\zeta\omega_{0}\omega} .$$

*Amplitude and phase.* Taking modulus and argument,

$$A(\omega) = \left\lvert Y\right\rvert = \frac{F_{0}/m}{\sqrt{\left(\omega_{0}^{2}-\omega^{2}\right)^{2} + \left(2\zeta\omega_{0}\omega\right)^{2}}}, \qquad \tan\varphi = \frac{2\zeta\omega_{0}\omega}{\omega_{0}^{2}-\omega^{2}} .$$

*Resonance frequency.* Let $u = \omega^{2}$. The squared denominator is

$$D(u) = \left(\omega_{0}^{2}-u\right)^{2} + 4\zeta^{2}\omega_{0}^{2}u = u^{2} - 2\omega_{0}^{2}\left(1-2\zeta^{2}\right)u + \omega_{0}^{4},$$

a convex quadratic in $u$, minimal at $u_{*} = \omega_{0}^{2}\left(1-2\zeta^{2}\right)$. A positive $u_{*}$ exists exactly when $\zeta < 1/\sqrt{2}$, and then

$$\omega_{r} = \omega_{0}\sqrt{1-2\zeta^{2}}, \qquad D(u_{*}) = 4\zeta^{2}\omega_{0}^{4}\left(1-\zeta^{2}\right), \qquad A_{\max} = \frac{F_{0}/m}{2\zeta\omega_{0}^{2}\sqrt{1-\zeta^{2}}} .$$

*Numbers.* $m = 1\ \mathrm{kg}$, $k = 25\ \mathrm{N/m}$, $c = 4\ \mathrm{N{\cdot}s/m}$, $F_{0} = 10\ \mathrm{N}$, $\omega = 4\ \mathrm{rad/s}$:

$$\omega_{0} = \sqrt{25} = 5\ \mathrm{rad/s}, \qquad \zeta = \frac{4}{2\sqrt{25}} = 0.4, \qquad \omega_{r} = 5\sqrt{1-0.32} \approx 4.12\ \mathrm{rad/s} .$$

At the driving frequency $\omega = 4$,

$$A = \frac{10}{\sqrt{\left(25-16\right)^{2} + \left(2\cdot0.4\cdot5\cdot4\right)^{2}}} = \frac{10}{\sqrt{81 + 256}} = \frac{10}{\sqrt{337}} \approx 0.545\ \mathrm{m},$$

$$\varphi = \arctan\frac{16}{9} \approx 1.058\ \mathrm{rad} \approx 60.6^{\circ} .$$

At resonance, $A_{\max} = \dfrac{10}{2\cdot0.4\cdot25\cdot\sqrt{1-0.16}} = \dfrac{10}{18.33} \approx 0.5455\ \mathrm{m}$.

*Checks.* The static response should be $A(0) = \dfrac{F_{0}/m}{\omega_{0}^{2}} = \dfrac{10}{25} = 0.4\ \mathrm{m} = \dfrac{F_{0}}{k}$ ✓. Since $\omega = 4$ is close to $\omega_{r} = 4.12$, the amplitude $0.545$ is within a tenth of a percent of $A_{\max}$ ✓. The phase $60.6^{\circ}$ exceeds $45^{\circ}$ because the driving frequency lies beyond the knee of the response ✓.

**26.** *Strategy: Cauchy–Euler with a complex indicial pair.*

Try $y = x^{m}$; then $x^{2}y'' + 3xy' + 5y = \left[m(m-1) + 3m + 5\right]x^{m}$, so the indicial equation is

$$m^{2} + 2m + 5 = 0 \;\Longrightarrow\; m = -1 \pm 2i, \qquad \alpha = -1, \; \beta = 2 .$$

By §7.6 the fundamental set is $x^{-1}\cos(2\ln x)$ and $x^{-1}\sin(2\ln x)$, so

$$y = x^{-1}\left(c_{1}\cos\left(2\ln x\right) + c_{2}\sin\left(2\ln x\right)\right), \qquad x > 0 .$$

*Check.* With $y = x^{-1}\cos(2\ln x)$: $y' = -x^{-2}\cos(2\ln x) - 2x^{-2}\sin(2\ln x)$ and

$$y'' = 2x^{-3}\cos + 2x^{-3}\sin + 4x^{-3}\sin - 4x^{-3}\cos = x^{-3}\left(-2\cos + 6\sin\right),$$

so

$$x^{2}y'' + 3xy' + 5y = x^{-1}\left(-2\cos + 6\sin\right) + 3x^{-1}\left(-\cos - 2\sin\right) + 5x^{-1}\cos = x^{-1}\left(-2 - 3 + 5\right)\cos + x^{-1}\left(6 - 6\right)\sin = 0 \;\checkmark$$

*Consistency with $t = \ln x$.* The equation becomes $\ddot{y} + 2\dot{y} + 5y = 0$, whose roots are $-1 \pm 2i$; converting $e^{-t}\cos 2t$ back gives $x^{-1}\cos(2\ln x)$ ✓.

*Behaviour:* the solution oscillates with "frequency" $2$ in $\ln x$ — that is, the oscillations become denser as $x \to 0^{+}$ — inside an envelope $x^{-1}$ that blows up at the origin. The singular point $x = 0$ is where the coefficients degenerate.

**27.** *Bending moment.* For a simply supported beam of length $L$ with uniform load $w_{0}$, each reaction is $w_{0}L/2$, so at distance $x$ from the left support

$$M(x) = \frac{w_{0}Lx}{2} - \frac{w_{0}x^{2}}{2} = \frac{w_{0}x\left(L-x\right)}{2},$$

sagging positive. With $y$ measured downward, $EI\,y'' = -M$.

*Two integrations.*

$$EI\,y' = -\frac{w_{0}}{2}\left(\frac{Lx^{2}}{2} - \frac{x^{3}}{3}\right) + A, \qquad EI\,y = -\frac{w_{0}}{2}\left(\frac{Lx^{3}}{6} - \frac{x^{4}}{12}\right) + Ax + B .$$

*Support conditions.* $y(0) = 0$ gives $B = 0$; $y(L) = 0$ gives

$$-\frac{w_{0}}{2}\cdot\frac{L^{4}}{12} + AL = 0 \;\Longrightarrow\; A = \frac{w_{0}L^{3}}{24} .$$

Therefore

$$y(x) = \frac{w_{0}}{24EI}\left(L^{3}x - 2Lx^{3} + x^{4}\right) = \frac{w_{0}x}{24EI}\left(L^{3} - 2Lx^{2} + x^{3}\right).$$

*Maximum.* At $x = L/2$, the bracket is $L^{3} - \frac{L^{3}}{2} + \frac{L^{3}}{8} = \frac{5L^{3}}{8}$, so

$$y_{\max} = \frac{w_{0}}{24EI}\cdot\frac{L}{2}\cdot\frac{5L^{3}}{8} = \frac{5w_{0}L^{4}}{384EI} .$$

*Numbers.* $E = 200\ \mathrm{GPa} = 2\times10^{11}\ \mathrm{Pa}$, $I = 8\times10^{-5}\ \mathrm{m^{4}}$, so

$$EI = 1.6\times10^{7}\ \mathrm{N{\cdot}m^{2}}, \qquad w_{0} = 1.5\times10^{4}\ \mathrm{N/m}, \qquad L^{4} = 256\ \mathrm{m^{4}},$$

$$y_{\max} = \frac{5\cdot1.5\times10^{4}\cdot256}{384\cdot1.6\times10^{7}} = \frac{1.92\times10^{7}}{6.144\times10^{9}} \approx 3.13\times10^{-3}\ \mathrm{m} = 3.13\ \mathrm{mm}.$$

*Checks.* Units: $\dfrac{(\mathrm{N/m})\,\mathrm{m^{4}}}{\mathrm{N\,m^{2}}} = \mathrm{m}$ ✓. $y(0) = y(L) = 0$ ✓. Differentiating twice, $EI\,y'' = \dfrac{w_{0}}{24}\left(-12Lx + 12x^{2}\right) = -\dfrac{w_{0}x(L-x)}{2} = -M$ ✓. The deflection is small compared with the span ($3\ \mathrm{mm}$ against $4\ \mathrm{m}$), which justifies the small-deflection hypothesis of the Euler–Bernoulli theory ✓.

**28.** *Model.* $m = 2\ \mathrm{kg}$, $k = 10\ \mathrm{N/m}$, $c = 4\ \mathrm{N{\cdot}s/m}$, so

$$2\ddot{y} + 4\dot{y} + 10y = 0 \;\Longleftrightarrow\; \ddot{y} + 2\dot{y} + 5y = 0, \qquad y(0) = 0.05, \; \dot{y}(0) = 0 .$$

*Roots.* $r^{2} + 2r + 5 = 0$ gives $r = -1 \pm 2i$; hence

$$y = e^{-t}\left(A\cos 2t + B\sin 2t\right).$$

*Initial conditions.* $y(0) = A = 0.05$; $\dot{y} = -y + e^{-t}\left(-2A\sin 2t + 2B\cos 2t\right)$, so $\dot{y}(0) = -A + 2B = 0$ and $B = 0.025$. Hence

$$y(t) = e^{-t}\left(0.05\cos 2t + 0.025\sin 2t\right)\ \mathrm{m} = 0.0559\,e^{-t}\cos\left(2t - 0.4636\right)\ \mathrm{m}.$$

*Parameters.* $\omega_{0} = \sqrt{k/m} = \sqrt5 \approx 2.236\ \mathrm{rad/s}$, $\zeta = \dfrac{c}{2\sqrt{mk}} = \dfrac{4}{2\sqrt{20}} = \dfrac{1}{\sqrt5} \approx 0.447$, $\omega_{d} = \omega_{0}\sqrt{1-\zeta^{2}} = 2\ \mathrm{rad/s}$ — underdamped. Logarithmic decrement:

$$\delta = \frac{2\pi\zeta}{\sqrt{1-\zeta^{2}}} = \frac{2\pi/\sqrt5}{2/\sqrt5} = \pi \approx 3.142,$$

so the amplitude ratio between consecutive cycles is $e^{-\delta} = e^{-\pi} \approx 0.0432$: each cycle retains about $4.3\%$ of the previous amplitude.

*Checks.* $y(0) = 0.05$ ✓ and $y'(0) = -0.05 + 2(0.025) = 0$ ✓. For the differential equation, use the identity valid for $y = e^{\alpha t}\left(A\cos\beta t + B\sin\beta t\right)$:

$$y'' + 2y' + 5y = e^{\alpha t}\left[\left(\alpha^{2}-\beta^{2}+2\alpha+5\right)\left(A\cos\beta t + B\sin\beta t\right) + \left(2\alpha\beta+2\beta\right)\left(B\cos\beta t - A\sin\beta t\right)\right],$$

and with $\alpha = -1$, $\beta = 2$ both brackets vanish: $\alpha^{2}-\beta^{2}+2\alpha+5 = 1-4-2+5 = 0$ and $2\alpha\beta+2\beta = 2\beta(\alpha+1) = 0$ ✓.

*Remark:* the logarithmic decrement is the quantity measured in a vibration test: from the ratio of successive peaks one reads off $\delta$, then $\zeta = \delta/\sqrt{4\pi^{2}+\delta^{2}}$. Here $\delta = \pi$ gives $\zeta = 1/\sqrt5$ ✓.

**29.** *Model.* With $L = 2\ \mathrm{H}$, $R = 8\ \Omega$, $C = 0.02\ \mathrm{F}$ and $E = 0$,

$$2\ddot{q} + 8\dot{q} + \frac{q}{0.02} = 0 \;\Longleftrightarrow\; \ddot{q} + 4\dot{q} + 25q = 0, \qquad q(0) = 10^{-3}, \; i(0) = \dot{q}(0) = 0 .$$

*Roots and solution.* $r^{2} + 4r + 25 = 0$ gives $r = -2 \pm i\sqrt{21}$, so $\omega_{0} = 5\ \mathrm{rad/s}$, $\zeta = 2/5 = 0.4$ (underdamped) and $\omega_{d} = \sqrt{21} \approx 4.583\ \mathrm{rad/s}$. Thus

$$q(t) = e^{-2t}\left(A\cos\sqrt{21}\,t + B\sin\sqrt{21}\,t\right).$$

*Initial conditions.* $q(0) = A = 10^{-3}$. Since $i = \dot{q} = -2q + e^{-2t}\left(-A\sqrt{21}\sin\sqrt{21}t + B\sqrt{21}\cos\sqrt{21}t\right)$, we get

$$i(0) = -2\cdot10^{-3} + B\sqrt{21} = 0 \;\Longrightarrow\; B = \frac{2\times10^{-3}}{\sqrt{21}} \approx 4.36\times10^{-4}.$$

Hence

$$q(t) = e^{-2t}\left(10^{-3}\cos\sqrt{21}\,t + \frac{2\times10^{-3}}{\sqrt{21}}\sin\sqrt{21}\,t\right)\ \mathrm{C} = 1.09\times10^{-3}e^{-2t}\cos\left(\sqrt{21}\,t - 0.411\right)\ \mathrm{C}.$$

*First zero of the charge.* The exponential never vanishes, so $q(t) = 0$ when

$$\cos\left(\sqrt{21}\,t - 0.411\right) = 0 \;\Longrightarrow\; \sqrt{21}\,t - 0.411 = \frac{\pi}{2} \;\Longrightarrow\; t = \frac{\frac{\pi}{2} + 0.411}{\sqrt{21}} \approx \frac{1.982}{4.583} \approx 0.433\ \mathrm{s}.$$

*Checks.* $q(0) = 10^{-3}$ ✓ and $i(0) = 0$ ✓. Units: $L\ddot{q}$ is $\mathrm{H\cdot C/s^{2}} = \mathrm{V}$, $R\dot{q}$ is $\mathrm{\Omega\cdot A} = \mathrm{V}$, $q/C$ is $\mathrm{C/F} = \mathrm{V}$ ✓. The time constant of the envelope is $1/2\ \mathrm{s}$, and $0.433\ \mathrm{s}$ is a little less than one quarter of the damped period $2\pi/\sqrt{21} \approx 1.37\ \mathrm{s}$ — as expected, since the charge starts at a maximum and reaches zero near a quarter-period later, slightly early because of the damping ✓.

**30.** *Derivation.* Let $y_{1}$ be a nonzero solution of $y'' + p(x)y' + q(x)y = 0$ on $I$ and put $y = v y_{1}$. Then

$$y' = v'y_{1} + vy_{1}', \qquad y'' = v''y_{1} + 2v'y_{1}' + vy_{1}'' .$$

Substituting into the equation:

$$v''y_{1} + 2v'y_{1}' + vy_{1}'' + p\left(v'y_{1} + vy_{1}'\right) + qvy_{1} = v''y_{1} + v'\left(2y_{1}' + py_{1}\right) + v\underbrace{\left(y_{1}'' + py_{1}' + qy_{1}\right)}_{=0} = 0 .$$

The $v$-coefficient vanishes because $y_{1}$ is a solution, so with $w = v'$,

$$w'y_{1} + w\left(2y_{1}' + py_{1}\right) = 0 \;\Longrightarrow\; \frac{w'}{w} = -2\frac{y_{1}'}{y_{1}} - p \;\Longrightarrow\; \ln\left\lvert w\right\rvert = -2\ln\left\lvert y_{1}\right\rvert - \int p\,dx .$$

Hence

$$w = \frac{e^{-\int p\,dx}}{y_{1}^{2}}, \qquad v = \int\frac{e^{-\int p\,dx}}{y_{1}^{2}}\,dx, \qquad y_{2} = y_{1}\int\frac{e^{-\int p\,dx}}{y_{1}^{2}}\,dx .$$

*Independence.* $W(y_{1}, y_{2}) = y_{1}y_{2}' - y_{1}'y_{2} = y_{1}\left(y_{1}'v + y_{1}v'\right) - y_{1}'y_{1}v = y_{1}^{2}w = e^{-\int p\,dx} \ne 0$, which is Abel's identity again ✓.

*Application.* For $y'' + y = 0$ we have $p = 0$, so $e^{-\int p} = 1$; with $y_{1} = \cos x$,

$$y_{2} = \cos x\int\frac{dx}{\cos^{2}x} = \cos x\cdot\tan x = \sin x ,$$

which is exactly the second member of the fundamental set, and $W(\cos x, \sin x) = 1$ ✓.

*Remark:* the formula is not a trick but the normal form of the equation. The substitution $y = v y_{1}$ removes the $v$-term because $y_{1}$ solves the equation; what remains is a first-order equation for $v'$, which always integrates.

## Challenge

**31.** *The solution.* For $\omega \ne \omega_{0}$, the particular solution has the form $y_{p} = C\cos\omega t + D\cos\omega_{0}t$: the forcing is $\cos\omega t$ and the homogeneous part must be added to satisfy the initial conditions. Substituting, $C\left(\omega_{0}^{2}-\omega^{2}\right) = F_{0}$, so $C = \dfrac{F_{0}}{\omega_{0}^{2}-\omega^{2}}$, and then

$$y(0) = C + D = 0 \;\Longrightarrow\; D = -C, \qquad y'(0) = -C\omega\sin 0 - D\omega_{0}\sin 0 = 0 \;\checkmark$$

so

$$y(t) = \frac{F_{0}}{\omega_{0}^{2}-\omega^{2}}\left(\cos\omega t - \cos\omega_{0}t\right).$$

*Verification.* $L[y] = \dfrac{F_{0}}{\omega_{0}^{2}-\omega^{2}}\left[\left(\omega_{0}^{2}-\omega^{2}\right)\cos\omega t - 0\right] = F_{0}\cos\omega t$ ✓, and the initial conditions hold as shown ✓.

*Beats.* Using $\cos A - \cos B = -2\sin\frac{A+B}{2}\sin\frac{A-B}{2}$,

$$y(t) = \frac{2F_{0}}{\omega_{0}^{2}-\omega^{2}}\,\sin\left(\frac{\omega_{0}+\omega}{2}t\right)\sin\left(\frac{\omega_{0}-\omega}{2}t\right),$$

a fast oscillation at the mean frequency $\frac{\omega_{0}+\omega}{2}$ multiplied by a slow envelope $\sin\left(\frac{\omega_{0}-\omega}{2}t\right)$ of period $\frac{4\pi}{\lvert\omega_{0}-\omega\rvert}$. For $\omega$ close to $\omega_{0}$ the envelope is very slow and the amplitude appears to pulsate between $0$ and $\frac{2F_{0}}{\omega_{0}^{2}-\omega^{2}}$.

*The resonant limit.* Write $\omega = \omega_{0} + \epsilon$ and expand:

$$\cos\left(\left(\omega_{0}+\epsilon\right)t\right) - \cos\omega_{0}t = -2\sin\left(\omega_{0}t + \frac{\epsilon t}{2}\right)\sin\frac{\epsilon t}{2} \approx -\epsilon t\sin\omega_{0}t,$$

while $\omega_{0}^{2} - \omega^{2} = -\epsilon\left(2\omega_{0}+\epsilon\right) \approx -2\epsilon\omega_{0}$. Hence

$$y(t) \longrightarrow \frac{F_{0}}{-2\epsilon\omega_{0}}\left(-\epsilon t\sin\omega_{0}t\right) = \frac{F_{0}}{2\omega_{0}}\,t\sin\omega_{0}t .$$

*Legitimacy of the limit.* For each $\omega \ne \omega_{0}$ the displayed $y$ is the unique solution of the IVP. The solution of a linear equation with constant coefficients depends continuously on its parameters (equivalently, the explicit formula is a continuous function of $\omega$), so the limit as $\omega \to \omega_{0}$ exists; and since it satisfies $y(0) = y'(0) = 0$ and $y'' + \omega_{0}^{2}y = F_{0}\cos\omega_{0}t$ (check: $y = \frac{F_{0}}{2\omega_{0}}t\sin\omega_{0}t$ gives $y'' + \omega_{0}^{2}y = F_{0}\cos\omega_{0}t$ directly), uniqueness identifies it as the resonant solution. The growth is linear in $t$, the hallmark of resonance without damping.

**32.** *Setting up.* Let $y \not\equiv 0$ solve $y'' + qy = 0$ with $q \ge m^{2} > 0$, and let $a < b$ be consecutive zeros. On $(a,b)$ the solution has a constant sign; replacing $y$ by $-y$ if necessary, take $y(x) > 0$ on $(a,b)$.

Suppose, for contradiction, that $b - a > \pi/m$, and put $c = a + \pi/m$, so $a < c < b$. Define $u(x) = \sin m(x-a)$ on $[a,c]$; then $u > 0$ on $(a,c)$, $u(a) = u(c) = 0$, $u'(a) = m$ and $u'(c) = -m$, and $u'' + m^{2}u = 0$.

*The Wronskian.* Let $W = uy' - u'y$ on $[a,c]$. Then

$$W' = u'y' + uy'' - u''y - u'y' = uy'' - u''y = u\left(-qy\right) - \left(-m^{2}u\right)y = \left(m^{2}-q\right)uy \le 0,$$

since $m^{2} - q \le 0$ and $uy > 0$ on $(a,c)$. So $W$ is nonincreasing on $[a,c]$.

*Values at the endpoints.* At $x = a$: $u(a) = 0$ and $y(a) = 0$, so $W(a) = 0$. At $x = c$: $u(c) = 0$ and $y(c) > 0$ (because $c < b$ and $y > 0$ on $(a,b)$), so

$$W(c) = u(c)y'(c) - u'(c)y(c) = 0 + m\,y(c) > 0 .$$

A nonincreasing function cannot go from $0$ at $a$ to a positive value at $c$. Contradiction. Hence $b - a \le \pi/m$. $\blacksquare$

*Interpretation.* The equation $y'' + m^{2}y = 0$ has solutions with zeros exactly $\pi/m$ apart, so the bound is sharp. Stated physically: a restoring force stronger than $m^{2}y$ makes the motion stiffer and its zeros closer together — the frequency of oscillation is at least $m$. For $y'' + q(x)y = 0$ with $q$ unbounded, this says the zeros accumulate, which is the mechanism behind the infinitely many zeros of oscillatory equations.

*Check.* With $q \equiv m^{2}$ the comparison equation is the equation itself, and $y = \sin(mx)$ has consecutive zeros at $0$ and $\pi/m$: equality in the bound, so the constant cannot be improved ✓. With $q \equiv 4$ and $m = 1$, the solution $\sin 2x$ has zeros $\pi/2$ apart, and $\pi/2 \le \pi$ ✓ — a stronger restoring force gives zeros at most half as far apart.

**33.** *The energy identity.* With $E = \tfrac12\left(\dot{y}^{2} + \omega_{0}^{2}y^{2}\right)$ and $\ddot{y} = -2\zeta\omega_{0}\dot{y} - \omega_{0}^{2}y$,

$$\dot{E} = \dot{y}\ddot{y} + \omega_{0}^{2}y\dot{y} = \dot{y}\left(\ddot{y} + \omega_{0}^{2}y\right) = \dot{y}\left(-2\zeta\omega_{0}\dot{y}\right) = -2\zeta\omega_{0}\dot{y}^{2} \le 0 .$$

So $E$ is nonincreasing for every $\zeta \ge 0$, and strictly decreasing whenever $\zeta > 0$ and $\dot{y} \ne 0$.

*Stability for every $\zeta \ge 0$.* From $E(t) \le E(0)$ and $\tfrac12\omega_{0}^{2}y(t)^{2} \le E(t)$,

$$\left\lvert y(t)\right\rvert \le \frac{\sqrt{2E(0)}}{\omega_{0}} = \sqrt{y(0)^{2} + \frac{\dot{y}(0)^{2}}{\omega_{0}^{2}}} ,$$

and the right side tends to $0$ with the initial data. Given $\varepsilon > 0$, choose initial data with $\left\lvert y(0)\right\rvert < \varepsilon/\sqrt2$ and $\left\lvert\dot{y}(0)\right\rvert < \omega_{0}\varepsilon/\sqrt2$; then $\left\lvert y(t)\right\rvert < \varepsilon$ for all $t \ge 0$. So the zero solution is stable.

*No asymptotic stability when $\zeta = 0$.* Then $E$ is constant and the solution is $y = R\cos\left(\omega_{0}t - \varphi\right)$ with $R = \sqrt{y(0)^{2} + \dot{y}(0)^{2}/\omega_{0}^{2}}$; it returns to its initial amplitude forever, so it does not converge to $0$ unless $R = 0$.

*Asymptotic stability when $\zeta > 0$.* Integrating $\dot{E} = -2\zeta\omega_{0}\dot{y}^{2}$ from $0$ to $T$,

$$\int_0^{T}\dot{y}(s)^{2}\,ds = \frac{E(0) - E(T)}{2\zeta\omega_{0}} \le \frac{E(0)}{2\zeta\omega_{0}},$$

so $\dot{y} \in L^{2}(0,\infty)$. Also $\ddot{y} = -2\zeta\omega_{0}\dot{y} - \omega_{0}^{2}y$ is bounded, since $E$ bounds both $\left\lvert y\right\rvert$ and $\left\lvert\dot{y}\right\rvert$; hence $\dot{y}$ is uniformly continuous, and a uniformly continuous function with finite square integral tends to $0$. Therefore $\dot{y}(t) \to 0$.

Now $E$ is nonincreasing and bounded below by $0$, so $E(t) \to L \ge 0$. Since $\dot{y} \to 0$ and $E \to L$, we get $y(t)^{2} \to 2L/\omega_{0}^{2}$. If $L > 0$, then $\left\lvert y(t)\right\rvert$ tends to a positive constant; but $\ddot{y}$ is bounded (as noted), so $y$ cannot jump between $\pm\sqrt{2L}/\omega_{0}$, and continuity forces $y \to c$ with $c \ne 0$; then $\ddot{y} \to -\omega_{0}^{2}c \ne 0$, contradicting $\dot{y} \to 0$. Hence $L = 0$ and $y(t) \to 0$. $\blacksquare$

*Remark.* The function $E$ is a Lyapunov function: it is positive definite and its derivative along solutions is negative semidefinite. This is the standard route to stability for mechanical systems, and it generalises to nonlinear oscillators, where the linearisation test of the first-order theory is not available.

*Check.* For $\zeta = 0$ the explicit solution is $y = R\cos(\omega_{0}t - \varphi)$ with $\dot{y} = -R\omega_{0}\sin(\omega_{0}t - \varphi)$, so

$$E = \tfrac12\left(R^{2}\omega_{0}^{2}\sin^{2} + \omega_{0}^{2}R^{2}\cos^{2}\right) = \tfrac12\omega_{0}^{2}R^{2},$$

constant in $t$, and $\dot{E} = 0$ ✓. For $\zeta > 0$ the formula $\dot{E} = -2\zeta\omega_{0}\dot{y}^{2}$ is negative except at the turning points, where $\dot{y} = 0$ instantaneously; this is why $E$ can decrease while never having a strictly negative derivative on an interval — the integral argument above is what converts the pointwise statement into convergence ✓.

**34.** *Homogeneous part.* The indicial equation is

$$m(m-1) - 3m + 4 = m^{2} - 4m + 4 = (m-2)^{2} = 0,$$

a double root $m = 2$, so $y_{h} = \left(c_{1} + c_{2}\ln x\right)x^{2}$.

*Convert to constant coefficients.* With $x = e^{t}$ we have $x^{2}y'' = \ddot{y} - \dot{y}$ and $xy' = \dot{y}$, so the equation becomes

$$\left(\ddot{y} - \dot{y}\right) - 3\dot{y} + 4y = e^{2t}\,t \;\Longleftrightarrow\; \ddot{y} - 4\dot{y} + 4y = t\,e^{2t} .$$

*Resonant particular solution.* The operator is $L = (D-2)^{2}$, and for $y = e^{2t}u(t)$,

$$L\left[e^{2t}u\right] = e^{2t}\ddot{u},$$

because the factorisation shifts the exponential away. So the equation becomes $e^{2t}\ddot{u} = te^{2t}$, that is $\ddot{u} = t$, and

$$u = \frac{t^{3}}{6}, \qquad y_{p} = \frac{t^{3}}{6}e^{2t} = \frac{x^{2}\left(\ln x\right)^{3}}{6} .$$

Hence

$$y = \left(c_{1} + c_{2}\ln x\right)x^{2} + \frac{x^{2}\left(\ln x\right)^{3}}{6}, \qquad x > 0 .$$

*Check.* Write $y_{p} = e^{2t}u$ with $u = t^{3}/6$, so that $u' = t^{2}/2$ and $u'' = t$. Then

$$\dot{y}_{p} = e^{2t}\left(2u + u'\right), \qquad \ddot{y}_{p} = e^{2t}\left(4u + 4u' + u''\right),$$

and therefore

$$\ddot{y}_{p} - 4\dot{y}_{p} + 4y_{p} = e^{2t}\left[\left(4u + 4u' + u''\right) - 4\left(2u + u'\right) + 4u\right] = e^{2t}u'' = t\,e^{2t} \;\checkmark$$

Undoing the substitution, $te^{2t} = x^{2}\ln x$ ✓, which is exactly the forcing.

*Remark.* The factor $\left(\ln x\right)^{3}$ — not $\ln x$ — is the signature of a *double* resonance: the forcing $x^{2}\ln x$ corresponds to a polynomial of degree $1$ times $e^{2t}$, and a double root raises the required degree by $2$, from $1$ to $3$. In the constant-coefficient language this is the rule $x^{s}Q_{n}$ with $s = 2$ and $n = 1$.


