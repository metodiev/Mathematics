# Laplace Transforms — Solutions

> [Laplace Transforms](README.md) · Solutions to the 36 problems in [exercises.md](exercises.md)

Each solution states the strategy, carries out every step, and ends with a verification: substitution
into the equation, a value theorem, or a limiting check. Regions of convergence are stated where the
problem asks for them.

## Beginner

### Solution 1

*Strategy: integrate the definition and take the limit.*

$$\mathcal{L}\{3\} = 3\lim_{R\to\infty}\int_0^Re^{-st}dt = 3\lim_{R\to\infty}\frac{1-e^{-sR}}{s} = \frac3s, \qquad \operatorname{Re}s>0 .$$

The limit of $e^{-sR}$ is $0$ precisely when $\operatorname{Re}s>0$, since $\lvert e^{-sR}\rvert = e^{-(\operatorname{Re}s)R}$.

$$\mathcal{L}\{t\} = \lim_{R\to\infty}\int_0^Rte^{-st}dt = \lim_{R\to\infty}\left(\left[-\frac{te^{-st}}{s}\right]_0^R+\frac1s\int_0^Re^{-st}dt\right) = 0+\frac{1}{s}\cdot\frac1s = \frac{1}{s^2},$$

with the same region: the boundary term vanishes because $te^{-(\operatorname{Re}s)t}\to0$ for $\operatorname{Re}s>0$.

*Check.* Both agree with the table of §7.2, and $\mathcal{L}\{t\}$ is the $-F'(s)$ of $\mathcal{L}\{1\}$: $-\frac{d}{ds}\frac1s = \frac{1}{s^2}$ ✓ (Theorem 7.5).

### Solution 2

$$\mathcal{L}\{e^{-2t}\} = \int_0^{\infty}e^{-st}e^{-2t}dt = \int_0^{\infty}e^{-(s+2)t}dt = \frac{1}{s+2}, \qquad \operatorname{Re}s>-2 .$$

The ROC is shifted by the growth rate $-2$: the function decays, so the transform exists even for some negative $\sigma$, down to $\sigma>-2$.

If $f$ grows faster than every exponential — for example $f(t) = e^{t^2}$ — the region is empty. For any $\sigma$, $e^{t^2-\sigma t}\to\infty$, so the integral diverges; there is no $s$ for which the transform exists.

*Check.* At $s = 0$ the formula gives $1/2$, and indeed $\int_0^\infty e^{-2t}dt = 1/2$ ✓.

### Solution 3

Integrate by parts with $u = t^2$, $dv = e^{-st}dt$:

$$\int_0^{\infty}t^2e^{-st}dt = \left[-\frac{t^2e^{-st}}{s}\right]_0^\infty+\frac{2}{s}\int_0^{\infty}te^{-st}dt .$$

The boundary term is zero for $\operatorname{Re}s>0$ (exponential beats quadratic), and the remaining integral is $\mathcal{L}\{t\} = 1/s^2$ by Solution 1. Hence

$$\mathcal{L}\{t^2\} = \frac{2}{s}\cdot\frac{1}{s^2} = \frac{2}{s^3}, \qquad \operatorname{Re}s>0,$$

which is $n!/s^{n+1}$ with $n=2$ ✓.

*Check.* The recursion $I_n = \frac{n}{s}I_{n-1}$ gives $I_2 = \frac2s\cdot\frac1{s^2}$; and $-\frac{d}{ds}\left(\frac{1}{s^2}\right) = \frac{2}{s^3} = \mathcal{L}\{t\cdot t\}$ ✓ (Theorem 7.5).

### Solution 4

Let $I = \int_0^\infty e^{-st}\sin 3t\,dt$ and $J = \int_0^\infty e^{-st}\cos 3t\,dt$. Integrating $I$ by parts with $u = \sin 3t$, $dv = e^{-st}dt$:

$$I = \underbrace{\left[-\frac{e^{-st}\sin 3t}{s}\right]_0^\infty}_{=\,0}+\frac3s\int_0^\infty e^{-st}\cos 3t\,dt = \frac3sJ .$$

Integrating $J$ by parts with $u = \cos 3t$:

$$J = \underbrace{\left[-\frac{e^{-st}\cos 3t}{s}\right]_0^\infty}_{=\,1/s}-\frac3s\int_0^\infty e^{-st}\sin 3t\,dt = \frac1s-\frac3sI .$$

Substituting $J = \frac1s-\frac3sI$ into $I = \frac3sJ$:

$$I = \frac3s\left(\frac1s-\frac3sI\right) \Longrightarrow I\left(1+\frac{9}{s^2}\right) = \frac{3}{s^2} \Longrightarrow I = \frac{3}{s^2+9}.$$

*Check at $s\to\infty$.* $\dfrac{3}{s^2+9}\sim\dfrac{3}{s^2}$, and $\sin 3t\approx 3t$ for small $t$, whose transform is $3/s^2$ ✓. At $s = 0$ the formula gives $1/3$, and indeed $\int_0^\infty\sin 3t\,dt$ does not converge — so the formula is only asserted for $\operatorname{Re}s>0$ ✓.

### Solution 5

Using $\cosh 2t = \frac12\left(e^{2t}+e^{-2t}\right)$ and linearity,

$$\mathcal{L}\{\cosh 2t\} = \frac12\left(\frac{1}{s-2}+\frac{1}{s+2}\right) = \frac12\cdot\frac{(s+2)+(s-2)}{(s-2)(s+2)} = \frac{s}{s^2-4}, \qquad \operatorname{Re}s>2 .$$

The ROC must contain both poles' right sides: $\operatorname{Re}s>2$ and $\operatorname{Re}s>-2$, hence $\operatorname{Re}s>2$.

*Check.* Combine the two exponentials directly: $\mathcal{L}\{t\cosh 2t\} = \frac12\left[\frac{1}{(s-2)^2}+\frac{1}{(s+2)^2}\right] = \frac{(s+2)^2+(s-2)^2}{2(s^2-4)^2} = \frac{s^2+4}{(s^2-4)^2}$, which is exactly $-\frac{d}{ds}\frac{s}{s^2-4}$ ✓ (Theorem 7.5). Also $sF(s)\to1$ as $s\to\infty$, matching $\cosh 0 = 1$ ✓.

### Solution 6

By linearity and the table, with $\operatorname{Re}s>\max(0,2) = 2$:

$$\mathcal{L}\left\{4t^2-3e^{2t}+5\sin t\right\} = 4\cdot\frac{2!}{s^3}-3\cdot\frac{1}{s-2}+5\cdot\frac{1}{s^2+1} = \frac{8}{s^3}-\frac{3}{s-2}+\frac{5}{s^2+1}.$$

*Check.* As $s\to\infty$ the leading term is $8/s^3$, consistent with $f(t)\approx 4t^2$ near $0$ and $\mathcal{L}\{4t^2\} = 8/s^3$ ✓. The pole at $s=2$ is the growth rate of the $e^{2t}$ term, and indeed the ROC is $\operatorname{Re}s>2$ ✓.

### Solution 7

With $f(t) = t^3$, $F(s) = 3!/s^4 = 6/s^4$. The first shifting theorem with $a = 2$ gives

$$\mathcal{L}\{t^3e^{2t}\} = F(s-2) = \frac{6}{(s-2)^4}, \qquad \operatorname{Re}s>2 .$$

*Check.* At $t=0$ the function vanishes to third order; correspondingly $sF(s) = 6s/(s-2)^4\to0$ as $s\to\infty$ ✓.

### Solution 8

With $f(t) = \cos 3t$, $F(s) = s/(s^2+9)$. First shifting with $a = -1$:

$$\mathcal{L}\{e^{-t}\cos 3t\} = F(s+1) = \frac{s+1}{(s+1)^2+9}, \qquad \operatorname{Re}s>-1 .$$

*Check.* At $t=0$ the function is $1$; the initial value theorem gives $\lim_{s\to\infty}\frac{s(s+1)}{(s+1)^2+9} = 1$ ✓.

### Solution 9

The step switches on at $t = 2$:

$$\mathcal{L}\{u(t-2)\} = \int_2^{\infty}e^{-st}dt = \frac{e^{-2s}}{s}, \qquad \operatorname{Re}s>0 .$$

For $(t-2)u(t-2)$, use the second shifting theorem with $f(t) = t$, $F(s) = 1/s^2$, $a = 2$:

$$\mathcal{L}\{(t-2)u(t-2)\} = e^{-2s}\cdot\frac{1}{s^2} = \frac{e^{-2s}}{s^2}.$$

*Check by definition.* $\int_2^\infty(t-2)e^{-st}dt = \int_0^\infty ue^{-s(u+2)}du = e^{-2s}/s^2$ ✓ (substitute $u = t-2$).

### Solution 10

From Definition 5.5 and the limit-of-pulses construction of §7.5, with rectangular pulses $\delta_\varepsilon(t-3) = \varepsilon^{-1}\mathbf{1}_{[3,3+\varepsilon)}$:

$$\mathcal{L}\{\delta_\varepsilon(t-3)\} = \frac1\varepsilon\int_3^{3+\varepsilon}e^{-st}dt = e^{-3s}\cdot\frac{1-e^{-\varepsilon s}}{\varepsilon s}\xrightarrow[\varepsilon\to0^+]{}e^{-3s}.$$

So $\mathcal{L}\{\delta(t-3)\} = e^{-3s}$, valid for every $s$ (the ROC is the whole plane).

*Why the integral definition cannot be applied directly.* $\delta$ is not a function: there is no ordinary $f$ with $f(t) = 0$ for $t\ne3$, $f(3) = \infty$ and $\int f = 1$. The integral $\int_0^\infty e^{-st}\delta(t-3)dt$ is meaningful only as the distributional pairing $\langle\delta(t-3),e^{-st}\rangle = e^{-3s}$, which is the same as the limit computed above. Using the "function" picture leads to meaningless expressions such as $\delta(3)\cdot e^{-3s}$.

*Check.* $\mathcal{L}\{\delta\} = 1$, the neutral element of multiplication, matching that $\delta$ is the identity for convolution: $\delta*f = f$ ✓.

### Solution 11

*(a)* $\dfrac{1}{s-4}$ matches $\dfrac{1}{s-a}$ with $a = 4$: the inverse is $e^{4t}$.

*(b)* $\dfrac{3}{s^2+9}$ matches $\dfrac{a}{s^2+a^2}$ with $a = 3$: the inverse is $\sin 3t$.

*(c)* $\dfrac{s}{s^2+16}$ matches $\dfrac{s}{s^2+a^2}$ with $a = 4$: the inverse is $\cos 4t$.

*Check.* At $t = 0$ the three inverses are $1,0,1$, and the initial value theorem gives $\lim sF$ equal to $1,0,1$ respectively ✓.

### Solution 12

*(a)* Split:

$$\frac{2s+1}{s^2+1} = 2\cdot\frac{s}{s^2+1}+1\cdot\frac{1}{s^2+1} \Longrightarrow f(t) = 2\cos t+\sin t .$$

*(b)* $\dfrac{1}{s^2}$ inverts to $t$ and $\dfrac{1}{s+1}$ to $e^{-t}$, so $f(t) = t-e^{-t}$.

*Check.* (a) at $t=0$: $f(0) = 2$, and $\lim_{s\to\infty}\frac{s(2s+1)}{s^2+1} = 2$ ✓. (b) at $t=0$: $f(0) = -1$, while $\lim_{s\to\infty}s\left(\frac1{s^2}-\frac1{s+1}\right) = 0-1 = -1$ ✓.

## Intermediate

### Solution 13

*Transform.* With $y(0) = 0$, $y'(0) = 1$:

$$\left(s^2Y-0\cdot s-1\right)+3\left(sY-0\right)+2Y = 0 \Longrightarrow \left(s^2+3s+2\right)Y = 1 .$$

*Algebra.* $s^2+3s+2 = (s+1)(s+2)$, so

$$Y(s) = \frac{1}{(s+1)(s+2)} = \frac{1}{s+1}-\frac{1}{s+2},$$

using the cover-up rule: $\frac{1}{-1+2} = 1$ and $\frac{1}{-2+1} = -1$.

*Invert.* $y(t) = e^{-t}-e^{-2t}$.

*Check.* $y(0) = 1-1 = 0$ ✓. $y' = -e^{-t}+2e^{-2t}$, so $y'(0) = 1$ ✓. And

$$y''+3y'+2y = \left(e^{-t}-4e^{-2t}\right)+3\left(-e^{-t}+2e^{-2t}\right)+2\left(e^{-t}-e^{-2t}\right) = (1-3+2)e^{-t}+(-4+6-2)e^{-2t} = 0 ✓.$$

### Solution 14

*Transform.* $\left(sY-0\right)-Y = \dfrac{1}{s-2}$, so $(s-1)Y = \dfrac{1}{s-2}$.

*Algebra.* $Y = \dfrac{1}{(s-1)(s-2)} = \dfrac{1}{s-2}-\dfrac{1}{s-1}$ (cover-up: $\frac{1}{2-1} = 1$ and $\frac{1}{1-2} = -1$).

*Invert.* $y(t) = e^{2t}-e^{t}$.

*Check.* $y(0) = 0$ ✓. $y'-y = \left(2e^{2t}-e^{t}\right)-\left(e^{2t}-e^{t}\right) = e^{2t}$ ✓.

### Solution 15

*Transform.* $\left(s^2+4\right)Y = \dfrac{s}{s^2+4}$, so

$$Y(s) = \frac{s}{(s^2+4)^2}.$$

*Invert by convolution.* Write $Y = \dfrac{s}{s^2+4}\cdot\dfrac{1}{s^2+4}$, the product of the transforms of $\cos 2t$ and $\frac12\sin 2t$. Then

$$y(t) = \int_0^t\cos(2\tau)\cdot\frac12\sin\left(2(t-\tau)\right)d\tau .$$

Expand $\sin(2t-2\tau) = \sin 2t\cos 2\tau-\cos 2t\sin 2\tau$:

$$y = \frac12\sin 2t\int_0^t\cos^2 2\tau\,d\tau-\frac12\cos 2t\int_0^t\sin 2\tau\cos 2\tau\,d\tau .$$

Now $\int_0^t\cos^22\tau\,d\tau = \frac t2+\frac{\sin 4t}{8}$ and $\int_0^t\sin2\tau\cos2\tau\,d\tau = \frac{\sin^22t}{4}$, so

$$y = \frac12\sin2t\left(\frac t2+\frac{\sin4t}{8}\right)-\frac12\cos2t\cdot\frac{\sin^22t}{4} = \frac{t\sin2t}{4},$$

because $\frac{\sin2t\sin4t}{16} = \frac{\sin^22t\cos2t}{8}$ cancels the last term.

*Answer.* $y(t) = \dfrac{t\sin 2t}{4}$.

*Check.* $y(0) = 0$ ✓; $y' = \frac14\left(\sin2t+2t\cos2t\right)$, so $y'(0) = 0$ ✓; and

$$y'' = \frac14\left(2\cos2t+2\cos2t-4t\sin2t\right) = \cos2t-t\sin2t, \qquad y''+4y = \cos2t-t\sin2t+t\sin2t = \cos2t ✓.$$

*Why the amplitude grows.* The forcing $\cos 2t$ oscillates at the natural frequency of the homogeneous equation $y''+4y = 0$. Each cycle adds energy in phase with the motion, so the amplitude grows linearly — resonance, exactly as in §9.10.

### Solution 16

*Partial fractions.* $F = \dfrac{A}{s-1}+\dfrac{B}{s+2}+\dfrac{C}{s+3}$ with

$$A = \frac{1+1}{(1+2)(1+3)} = \frac{2}{12} = \frac16, \qquad B = \frac{-2+1}{(-2-1)(-2+3)} = \frac{-1}{-3} = \frac13, \qquad C = \frac{-3+1}{(-3-1)(-3+2)} = \frac{-2}{4} = -\frac12 .$$

*Invert.*

$$f(t) = \frac16e^{t}+\frac13e^{-2t}-\frac12e^{-3t}.$$

*Check at $t=0$.* $f(0) = \frac16+\frac13-\frac12 = \frac{1+2-3}{6} = 0$. The initial value theorem gives $\lim_{s\to\infty}sF(s) = \lim\dfrac{s^2+\cdots}{s^3+\cdots} = 0$ ✓.

*Check by recombining.* Putting the three fractions over the common denominator,

$$\frac{\frac16(s+2)(s+3)+\frac13(s-1)(s+3)-\frac12(s-1)(s+2)}{(s-1)(s+2)(s+3)},$$

whose numerator is $\frac16\left(s^2+5s+6\right)+\frac13\left(s^2+2s-3\right)-\frac12\left(s^2+s-2\right) = \frac{1+2-3}{6}s^2+\frac{5+4-3}{6}s+\frac{6-6+6}{6} = s+1$ ✓, which is the original numerator.

### Solution 17

*Transform.* $(s+1)Y = \dfrac{e^{-s}}{s}$, so

$$Y(s) = e^{-s}\cdot\frac{1}{s(s+1)} = e^{-s}\left(\frac1s-\frac{1}{s+1}\right).$$

*Invert.* By the second shifting theorem, $e^{-s}G(s)$ inverts to $g(t-1)u(t-1)$ with $g(t) = 1-e^{-t}$:

$$y(t) = \left[1-e^{-(t-1)}\right]u(t-1) = \begin{cases}0, & 0\le t<1,\\ 1-e^{-(t-1)}, & t\ge1.\end{cases}$$

*Description.* Nothing happens until $t=1$; then the solution rises from $0$ towards $1$ with time constant $1$. The solution is continuous at $t=1$, while $y'$ jumps from $0$ to $1$: for a first-order equation $y' = -y+u$, the derivative inherits the jump of the input ✓.

*Check.* For $t>1$: $y'+y = e^{-(t-1)}+\left(1-e^{-(t-1)}\right) = 1$ ✓. $y(0) = 0$ ✓.

### Solution 18

$$G(s) = \frac{1}{s^2+4} \longleftrightarrow g(t) = \frac12\sin 2t, \qquad\text{so}\qquad \mathcal{L}^{-1}\left\{\frac{e^{-2s}}{s^2+4}\right\} = g(t-2)u(t-2) = \frac12\sin\left(2(t-2)\right)u(t-2).$$

*What the factor does.* The factor $e^{-2s}$ delays the signal by $2$ and switches it on at $t=2$: the answer is zero for $t<2$ and then the sine starts from its value $0$ at $t=2$. Without the $u(t-2)$ the expression $\frac12\sin(2(t-2))$ would be nonzero for $t<2$, which would violate causality.

*Check.* At $t=2$ the value is $0$ and the derivative is $\cos 0 = 1$, so the delayed signal starts with unit slope, as the undelayed one does at $0$ ✓. The initial value theorem applied to the *undelayed* factor gives $\lim s\cdot\frac{1}{s^2+4} = 0$ ✓.

### Solution 19

*Transform.* $(s+1)^2Y = \dfrac{e^{-2s}}{s}$, so

$$Y = e^{-2s}\cdot\frac{1}{s(s+1)^2}.$$

*Partial fractions.*

$$\frac{1}{s(s+1)^2} = \frac1s-\frac{1}{s+1}-\frac{1}{(s+1)^2},$$

verified by combining: $\frac{(s+1)^2-s(s+1)-s}{s(s+1)^2} = \frac{s^2+2s+1-s^2-s-s}{s(s+1)^2} = \frac{1}{s(s+1)^2}$ ✓.

*Invert the undelayed factor.* $g(t) = 1-e^{-t}-te^{-t}$.

*Apply the shift.*

$$y(t) = \left[1-e^{-(t-2)}-(t-2)e^{-(t-2)}\right]u(t-2).$$

*Continuity at $t=2$.* $g(0) = 1-1-0 = 0$ ✓, and $g'(t) = e^{-t}-e^{-t}+te^{-t} = te^{-t}$, so $g'(0) = 0$ ✓. Hence $y(2) = 0$ and $y'(2) = 0$: both $y$ and $y'$ are continuous at the switch, as required for a second-order equation with a bounded input.

*Check for $t>2$.* With $u = t-2$, $y = 1-e^{-u}-ue^{-u}$, $y' = ue^{-u}$, $y'' = e^{-u}-ue^{-u}$, so

$$y''+2y'+y = \left(e^{-u}-ue^{-u}\right)+2ue^{-u}+\left(1-e^{-u}-ue^{-u}\right) = 1 ✓.$$

### Solution 20

*Convolution.* $\dfrac{1}{s^2}$ inverts to $t$ and $\dfrac{1}{s+1}$ to $e^{-t}$, so

$$f(t) = \int_0^t\tau\,e^{-(t-\tau)}d\tau = e^{-t}\int_0^t\tau e^{\tau}d\tau .$$

Since $\int\tau e^\tau d\tau = (\tau-1)e^\tau$,

$$\int_0^t\tau e^\tau d\tau = (t-1)e^t+1, \qquad f(t) = e^{-t}\left[(t-1)e^t+1\right] = t-1+e^{-t}.$$

*Partial fractions.*

$$\frac{1}{s^2(s+1)} = \frac{A}{s}+\frac{B}{s^2}+\frac{C}{s+1}, \qquad 1 = As(s+1)+B(s+1)+Cs^2 .$$

At $s=0$: $B = 1$. At $s=-1$: $C = 1$. Comparing $s^2$: $0 = A+C$, so $A = -1$. Thus

$$f(t) = -1+t+e^{-t} ✓.$$

*Check.* $f(0) = -1+0+1 = 0$ ✓, and $sF(s) = \frac{1}{s(s+1)}\to0$ ✓. Also $f'(t) = 1-e^{-t}$ and $f''(t) = e^{-t}$, so $f''+f' = 1$. Transforming that identity with $f(0) = f'(0) = 0$ gives $(s^2+s)F = 1/s$, i.e. $F = \frac{1}{s^2(s+1)}$ — the transform we started from ✓.

### Solution 21

*Transfer function.* With zero initial conditions, $\left(s^2+4s+13\right)Y = F$, so

$$H(s) = \frac{1}{s^2+4s+13} = \frac{1}{(s+2)^2+9}.$$

*Impulse response.* From the table with $a = -2$, $b = 3$ and a factor $\frac13$:

$$h(t) = \frac13e^{-2t}\sin 3t .$$

*Step response.* $Y = \dfrac{H(s)}{s} = \dfrac{1}{s\left((s+2)^2+9\right)}$. Decompose:

$$\frac{1}{s\left((s+2)^2+9\right)} = \frac{1}{13}\left(\frac1s-\frac{s+4}{(s+2)^2+9}\right),$$

verified by combining: $\frac{(s+2)^2+9-s(s+4)}{13s((s+2)^2+9)} = \frac{s^2+4s+13-s^2-4s}{13s(\cdots)} = \frac{13}{13s(\cdots)}$ ✓. Since $s+4 = (s+2)+2$,

$$\mathcal{L}^{-1}\left\{\frac{s+4}{(s+2)^2+9}\right\} = e^{-2t}\cos 3t+\frac23e^{-2t}\sin 3t,$$

so

$$y_{\text{step}}(t) = \frac{1}{13}\left[1-e^{-2t}\cos 3t-\frac23e^{-2t}\sin 3t\right].$$

*Check.* $y_{\text{step}}(0) = \frac{1}{13}(1-1-0) = 0$ ✓. Differentiating the bracket gives $2e^{-2t}\cos3t+3e^{-2t}\sin3t+\frac23\left(2e^{-2t}\sin3t-3e^{-2t}\cos3t\right)$, which simplifies to $\frac{13}{3}e^{-2t}\sin3t$; multiplying by $\frac{1}{13}$ gives $\frac13e^{-2t}\sin3t = h(t)$ ✓, as the theory requires. The final value is $H(0) = \frac{1}{13}$, and indeed $y_{\text{step}}\to\frac{1}{13}$ ✓.

### Solution 22

*One period.* For $f(t) = t$ on $[0,1)$,

$$\int_0^1te^{-st}dt = \left[-\frac{te^{-st}}{s}\right]_0^1+\frac1s\int_0^1e^{-st}dt = -\frac{e^{-s}}{s}+\frac{1-e^{-s}}{s^2} = \frac{1-(1+s)e^{-s}}{s^2}.$$

*Theorem 8.1.* With $T = 1$,

$$F(s) = \frac{1}{1-e^{-s}}\cdot\frac{1-(1+s)e^{-s}}{s^2} = \frac{1-(1+s)e^{-s}}{s^2\left(1-e^{-s}\right)}, \qquad \operatorname{Re}s>0 .$$

*Check.* For large $s$, the numerator is $1+O(se^{-s})$ and the denominator is $s^2(1+O(e^{-s}))$, so $F\sim1/s^2$: consistent with $f(0^+) = 0$ and $f'(0^+) = 1$, i.e. $f(t)\approx t$ near $0$ ✓. As $s\to0^+$, expand: numerator $= 1-(1+s)(1-s+s^2/2-\cdots) = s^2/2+O(s^3)$ and denominator $= s^2(1-(1-s+\cdots)) = s^3+O(s^4)$; hence $sF\to\frac12$, the mean of the sawtooth over its period ✓ (Abel's theorem).

### Solution 23

*Transform.* The integral is the convolution $y*\sin t$, so its transform is $Y(s)\cdot\dfrac{1}{s^2+1}$. Hence

$$Y(s) = \frac{1}{s^2}+Y(s)\frac{1}{s^2+1} \Longrightarrow Y(s)\left(1-\frac{1}{s^2+1}\right) = \frac{1}{s^2} \Longrightarrow Y(s)\frac{s^2}{s^2+1} = \frac{1}{s^2},$$

so

$$Y(s) = \frac{s^2+1}{s^4} = \frac{1}{s^2}+\frac{1}{s^4} \Longrightarrow y(t) = t+\frac{t^3}{6}.$$

*Check.* $y(0) = 0$ ✓. The convolution must equal $y(t)-t = t^3/6$:

$$\int_0^t\left(\tau+\frac{\tau^3}{6}\right)\sin(t-\tau)\,d\tau = \frac{t^3}{6},$$

which is confirmed by expanding $\sin(t-\tau)$ and using $\int_0^t\tau\sin\tau\,d\tau = \sin t-t\cos t$ and $\int_0^t\tau^3\sin\tau\,d\tau = \left(3t^2-6\right)\sin t-\left(t^3-6t\right)\cos t$; the trigonometric terms cancel and the polynomial terms give $t^3/6$ ✓.

A second check by differentiation: differentiating the integral equation gives $y' = 1+\int_0^ty(\tau)\cos(t-\tau)d\tau$, and with $y = t+t^3/6$ the integral equals $t^2/2$, so $y' = 1+t^2/2$ ✓, which is the derivative of $t+t^3/6$.

## Advanced

### Solution 24

*Hypotheses.* $f$ continuous on $[0,\infty)$, $f'$ piecewise continuous on $[0,\infty)$, and both $f$ and $f'$ of exponential order: $\lvert f(t)\rvert\le M_0e^{\sigma_0t}$ and $\lvert f'(t)\rvert\le M_1e^{\sigma_1t}$ for $t\ge T$. Let $\sigma_0' = \max(\sigma_0,\sigma_1)$.

*Proof.* Fix $s$ with $\operatorname{Re}s>\sigma_0'$ and integrate by parts on $[0,R]$:

$$\int_0^Re^{-st}f'(t)\,dt = \left[e^{-st}f(t)\right]_0^R+s\int_0^Re^{-st}f(t)\,dt = e^{-sR}f(R)-f(0)+s\int_0^Re^{-st}f(t)\,dt.$$

*The boundary term.* $\lvert e^{-sR}f(R)\rvert\le M_0e^{-(\operatorname{Re}s-\sigma_0)R}\to0$ because $\operatorname{Re}s>\sigma_0$.

*The integral.* $\int_0^Re^{-st}f(t)dt\to F(s)$ by definition, and the convergence is absolute for $\operatorname{Re}s>\sigma_0$ by Theorem 7.1.

*The left side.* Since $f'$ is piecewise continuous and of exponential order, the integral $\int_0^\infty e^{-st}f'(t)dt$ converges absolutely for $\operatorname{Re}s>\sigma_1$ (split at the finitely many discontinuities and apply Theorem 7.1 on each piece). Letting $R\to\infty$ in the identity gives

$$\mathcal{L}\{f'\}(s) = 0-f(0)+sF(s). \qquad\blacksquare$$

*Iteration.* Applying the result to $f'$, which must now be continuous with $f''$ piecewise continuous, gives $\mathcal{L}\{f''\} = s\mathcal{L}\{f'\}-f'(0) = s^2F-sf(0)-f'(0)$; induction gives the $n$-th formula of Theorem 7.3.

*Check.* With $f(t) = e^{at}$: $f' = ae^{at}$, and the rule gives $s\cdot\frac{1}{s-a}-1 = \frac{s-(s-a)}{s-a} = \frac{a}{s-a}$ ✓.

### Solution 25

*First proof (from the derivative rule).* Let $g(t) = \int_0^tf(\tau)d\tau$. Then $g$ is continuous, $g' = f$ wherever $f$ is continuous, and $g(0) = 0$. Applying Theorem 7.3 to $g$:

$$F(s) = \mathcal{L}\{g'\}(s) = sG(s)-g(0) = sG(s), \qquad\text{so}\qquad G(s) = \frac{F(s)}{s}.$$

The hypotheses transfer: $g$ is of exponential order because $\lvert g(t)\rvert\le\int_0^t\lvert f\rvert\le\frac{M}{\sigma_0}\left(e^{\sigma_0t}-1\right)$ for $\sigma_0>0$, and $g' = f$ is piecewise continuous. $\blacksquare$

*Second proof (Fubini).* Write $1/s = \int_0^\infty e^{-su}du$ for $\operatorname{Re}s>0$ and compute

$$\frac{F(s)}{s} = \int_0^\infty e^{-su}du\int_0^\infty e^{-s\tau}f(\tau)d\tau = \int_0^\infty\!\!\int_0^\infty e^{-s(u+\tau)}f(\tau)\,du\,d\tau .$$

The integrand is absolutely integrable on the quadrant when $\operatorname{Re}s>\max(0,\sigma_0)$, so Fubini applies. Substitute $t = u+\tau$ for fixed $\tau$: the region $u\ge0,\tau\ge0$ becomes $0\le\tau\le t<\infty$, and

$$\frac{F(s)}{s} = \int_0^\infty e^{-st}\left(\int_0^tf(\tau)d\tau\right)dt = \mathcal{L}\left\{\int_0^tf\right\}(s). \qquad\blacksquare$$

*Check.* With $f = 1$: $\int_0^t1\,d\tau = t$, and $\mathcal{L}\{t\} = 1/s^2 = (1/s)/s$ ✓.

### Solution 26

*Statement.* If $F(s) = \mathcal{L}\{f\}(s)$ for $\operatorname{Re}s>\sigma_0$, then for any constant $a$,

$$\mathcal{L}\{e^{at}f(t)\}(s) = F(s-a), \qquad \operatorname{Re}(s-a)>\sigma_0 .$$

*Proof.* Compute from the definition:

$$\mathcal{L}\{e^{at}f(t)\}(s) = \int_0^\infty e^{-st}e^{at}f(t)\,dt = \int_0^\infty e^{-(s-a)t}f(t)\,dt .$$

The last integral is the definition of $F$ evaluated at the argument $s-a$, so it equals $F(s-a)$, and it converges exactly when $\operatorname{Re}(s-a)>\sigma_0$, i.e. $\operatorname{Re}s>\sigma_0+\operatorname{Re}a$. $\blacksquare$

*Consequence for the ROC.* The pole at $s = p$ of $F$ becomes a pole at $s = p+a$: multiplication by $e^{at}$ translates the whole pole pattern by $a$. For example $F(s) = 1/s$ has a pole at $0$, and $e^{3t}$ has transform $1/(s-3)$ with a pole at $3$ ✓.

*Check with a concrete case.* $\mathcal{L}\{\cos 2t\} = s/(s^2+4)$; the theorem gives $\mathcal{L}\{e^{-t}\cos2t\} = (s+1)/((s+1)^2+4)$. Directly, $\int_0^\infty e^{-(s+1)t}\cos2t\,dt$ is the same integral with $s$ replaced by $s+1$ ✓.

### Solution 27

*Statement and proof.* If $F = \mathcal{L}\{f\}$ and $a>0$, then

$$\mathcal{L}\{f(t-a)u(t-a)\}(s) = \int_0^\infty e^{-st}f(t-a)u(t-a)\,dt = \int_a^\infty e^{-st}f(t-a)\,dt .$$

Substitute $u = t-a$, so $t = u+a$, $dt = du$, and the limits $t = a,\infty$ become $u = 0,\infty$:

$$= \int_0^\infty e^{-s(u+a)}f(u)\,du = e^{-as}\int_0^\infty e^{-su}f(u)\,du = e^{-as}F(s). \qquad\blacksquare$$

*Why $u(t-a)$ cannot be omitted.* Take $f(t) = t$ and $a = 1$. Then

$$\mathcal{L}\{f(t-1)\} = \mathcal{L}\{t-1\} = \frac{1}{s^2}-\frac{1}{s}, \qquad \mathcal{L}\{f(t-1)u(t-1)\} = e^{-s}\cdot\frac{1}{s^2}.$$

These are different functions of $s$: the first corresponds to a signal that is negative for $0<t<1$ (the function $t-1$ continues backwards), the second to a signal that is zero until $t=1$. The second is the delayed signal; the first is not, and its inverse is not a delay of $f$. Any piecewise-defined forcing must therefore be written with steps before the second shifting theorem is applied.

*Check.* For $f\equiv1$ the theorem gives $\mathcal{L}\{u(t-a)\} = e^{-as}/s$, which agrees with the direct computation of §7.5 ✓.

### Solution 28

*Statement.* If $f,g$ are piecewise continuous and of exponential order, with transforms $F,G$ converging for $\operatorname{Re}s>\sigma_0$, then $\mathcal{L}\{f*g\} = FG$.

*Proof.* By Definition 5.2 and the product of the two integrals,

$$F(s)G(s) = \int_0^\infty e^{-su}f(u)\,du\int_0^\infty e^{-sv}g(v)\,dv = \iint_{[0,\infty)^2}e^{-s(u+v)}f(u)g(v)\,du\,dv .$$

*Interchange.* The double integral is absolutely convergent for $\operatorname{Re}s>\sigma_0$: by the exponential-order bounds, $\lvert f(u)g(v)e^{-s(u+v)}\rvert\le M^2e^{-(\operatorname{Re}s-\sigma_0)(u+v)}$, which is integrable on the quadrant. **Tonelli's theorem** (or Fubini's, since absolute convergence holds) therefore permits writing the product as an iterated integral in either order and making a change of variables.

*Change of variables.* Put $t = u+v$ and $\tau = u$. The map $(u,v)\mapsto(t,\tau)$ has Jacobian $\begin{vmatrix}\partial t/\partial u&\partial t/\partial v\\ \partial\tau/\partial u&\partial\tau/\partial v\end{vmatrix} = \begin{vmatrix}1&1\\1&0\end{vmatrix} = -1$, of modulus $1$, and it maps the quadrant $u\ge0,v\ge0$ onto the region $0\le\tau\le t<\infty$. Hence

$$F(s)G(s) = \int_0^\infty e^{-st}\left(\int_0^tf(\tau)g(t-\tau)\,d\tau\right)dt = \mathcal{L}\{(f*g)(t)\}(s). \qquad\blacksquare$$

*Check.* With $f = g = 1$: $(f*g)(t) = t$, and $\mathcal{L}\{t\} = 1/s^2 = (1/s)(1/s)$ ✓.

### Solution 29

*Statement.* If $F(s) = \mathcal{L}\{f\}(s)$ exists for $\operatorname{Re}s>\sigma_0$, then $F$ is differentiable there and

$$F'(s) = -\mathcal{L}\{tf(t)\}(s).$$

*Proof.* Fix $s$ with $\sigma = \operatorname{Re}s>\sigma_0$ and choose $\varepsilon>0$ with $\sigma-\varepsilon>\sigma_0$. For $h$ complex with $\lvert h\rvert<\varepsilon$ and $t\ge0$,

$$\left\lvert\frac{e^{-(s+h)t}-e^{-st}}{h}\right\rvert = e^{-\sigma t}\left\lvert\frac{e^{-ht}-1}{h}\right\rvert\le e^{-\sigma t}\cdot t\,e^{\lvert h\rvert t}\le te^{-(\sigma-\varepsilon)t},$$

using $\lvert e^{z}-1\rvert\le\lvert z\rvert e^{\lvert z\rvert}$. The dominating function $t\mapsto t\lvert f(t)\rvert e^{-(\sigma-\varepsilon)t}$ is integrable because $f$ is of exponential order and $\sigma-\varepsilon>\sigma_0$. By the **dominated convergence theorem** (applied to the difference quotients), the limit $h\to0$ may be taken inside the integral:

$$F'(s) = \lim_{h\to0}\int_0^\infty\frac{e^{-(s+h)t}-e^{-st}}{h}f(t)\,dt = \int_0^\infty\left(-te^{-st}\right)f(t)\,dt = -\mathcal{L}\{tf\}(s). \qquad\blacksquare$$

Iterating gives $F^{(n)}(s) = (-1)^n\mathcal{L}\{t^nf(t)\}(s)$.

*Check.* $F(s) = 1/s$ gives $F'(s) = -1/s^2 = -\mathcal{L}\{t\}$ ✓.

### Solution 30

*Initial value theorem.* Suppose $f$ is continuous on $(0,\infty)$, piecewise smooth, of exponential order, and $f(0^+) = \lim_{t\to0^+}f(t)$ exists. Then $\lim_{s\to+\infty}sF(s) = f(0^+)$.

*Proof.* By Theorem 7.3, $sF(s)-f(0^+) = \mathcal{L}\{f'\}(s) = \int_0^\infty e^{-st}f'(t)dt$. Since $\lvert f'(t)\rvert\le Me^{\sigma_0t}$ for $t\ge T$ and $f'$ is bounded on $[0,T]$ (piecewise continuous on a compact interval), there is $M'$ with $\lvert f'(t)\rvert\le M'e^{\sigma_0t}$ for all $t\ge0$. Then $\lvert e^{-st}f'(t)\rvert\le M'e^{-(s-\sigma_0)t}$, integrable for $s>\sigma_0$, and dominated convergence gives $\mathcal{L}\{f'\}(s)\to0$ as $s\to+\infty$. Hence $sF(s)\to f(0^+)$. $\blacksquare$

*Final value theorem.* Suppose $f$ is piecewise smooth and of exponential order, and $L = \lim_{t\to\infty}f(t)$ exists. Then $\lim_{s\to0^+}sF(s) = L$.

*Proof.* The derivative rule gives $sF(s)-f(0) = \mathcal{L}\{f'\}(s) = \int_0^\infty e^{-st}f'(t)dt$. Since $f(t)\to L$, the improper integral $\int_0^\infty f'(t)dt$ converges and equals $L-f(0)$. **Abel's theorem** for Laplace integrals — if $\int_0^\infty g$ converges then $\lim_{s\to0^+}\int_0^\infty e^{-st}g(t)dt = \int_0^\infty g(t)dt$ — applied to $g = f'$ gives $sF(s)-f(0)\to L-f(0)$, hence $sF(s)\to L$. $\blacksquare$

*Counterexample.* For $f(t) = \sin t$, $F(s) = 1/(s^2+1)$ and $sF(s) = s/(s^2+1)\to0$ as $s\to0^+$, yet $\sin t$ has no limit as $t\to\infty$. The hypothesis of the final value theorem therefore genuinely fails, and its conclusion is false: the limit of $sF(s)$ is not the limit of $f$. (Similarly $f = e^t$ gives $sF = s/(s-1)\to0$ while $f\to\infty$.)

*Correct use.* To apply the theorem in practice, check that $sF(s)$ has all its poles in $\operatorname{Re}s<0$, with at most a simple pole at $s=0$; then the final value is the residue at $0$, i.e. $\lim_{s\to0}sF(s)$. For $F = \frac{1}{s(s+1)}$: $sF = \frac{1}{s+1}\to1$, and indeed $f = 1-e^{-t}\to1$ ✓.

### Solution 31

*Part 1: the ROC is a right half-plane.* Suppose $F(s_0)$ converges. Put $g(t) = \int_0^te^{-s_0u}f(u)du$; convergence of the improper integral makes $g$ bounded, $\lvert g(t)\rvert\le K$. For $\operatorname{Re}s>\operatorname{Re}s_0$, integration by parts gives

$$\int_0^Re^{-(s-s_0)t}\,dg(t) = e^{-(s-s_0)R}g(R)-g(0)+(s-s_0)\int_0^Re^{-(s-s_0)t}g(t)\,dt,$$

where the boundary term at $R$ is bounded by $Ke^{-(\operatorname{Re}s-\operatorname{Re}s_0)R}\to0$ and the integral is absolutely convergent (dominated by $Ke^{-(\operatorname{Re}s-\operatorname{Re}s_0)t}$). Hence $\int_0^\infty e^{-st}f(t)dt$ converges for every such $s$: the ROC is a right half-plane. $\blacksquare$

*Part 2: analyticity.* Fix $s_1$ in the ROC and let $\rho = \operatorname{Re}s_1-\sigma_c>0$. On the disc $\lvert s-s_1\rvert<\rho/2$ we have $\operatorname{Re}s\ge\sigma$ for a fixed $\sigma>\sigma_c$, so $\lvert f(t)e^{-st}\rvert\le\lvert f(t)\rvert e^{-\sigma t}$, which is integrable by Theorem 7.1. The function $s\mapsto e^{-st}f(t)$ is entire for each $t$, so by the dominated convergence theorem (or Morera's theorem with the same domination) $F$ is analytic on the disc. As the disc is arbitrary inside the ROC, $F$ is analytic on the whole ROC. Differentiating under the integral, as in Solution 29, gives

$$F'(s) = -\int_0^\infty te^{-st}f(t)\,dt = -\mathcal{L}\{tf(t)\}(s). \qquad\blacksquare$$

*Consequence.* A Laplace transform cannot have a pole inside its ROC; all poles lie on or to the left of the abscissa of convergence. This is why poles of a rational transform determine the ROC: the region is the half-plane to the right of the rightmost pole.

*Check.* $F(s) = 1/(s-1)$ is analytic on $\operatorname{Re}s>1$ and has its pole at $s=1$, on the boundary ✓.

## Challenge

### Solution 32

*First transform.* For $s>0$ substitute $u = st$, so $t = u/s$ and $dt = du/s$:

$$\mathcal{L}\left\{t^{-1/2}\right\} = \int_0^\infty t^{-1/2}e^{-st}dt = \int_0^\infty\left(\frac us\right)^{-1/2}e^{-u}\frac{du}{s} = s^{-1/2}\int_0^\infty u^{-1/2}e^{-u}du = \frac{\Gamma\left(\frac12\right)}{\sqrt s} = \sqrt{\frac{\pi}{s}},$$

using $\Gamma\left(\frac12\right) = \sqrt\pi$. The region is $\operatorname{Re}s>0$.

*Second transform.* Similarly,

$$\mathcal{L}\left\{t^{1/2}\right\} = s^{-3/2}\Gamma\left(\frac32\right) = s^{-3/2}\cdot\frac12\Gamma\left(\frac12\right) = \frac{\sqrt\pi}{2s^{3/2}},$$

using $\Gamma(z+1) = z\Gamma(z)$ with $z = \frac12$.

*The Gaussian integral.* Evaluate the first identity at $s = 1$:

$$\int_0^\infty t^{-1/2}e^{-t}dt = \sqrt{\pi}.$$

Substitute $t = x^2$, so $dt = 2x\,dx$ and $t^{-1/2} = 1/x$:

$$\int_0^\infty\frac{1}{x}e^{-x^2}\,2x\,dx = 2\int_0^\infty e^{-x^2}dx = \sqrt\pi \Longrightarrow \int_0^\infty e^{-x^2}dx = \frac{\sqrt\pi}{2}.$$

*Check.* $\Gamma\left(\frac12\right) = \int_0^\infty u^{-1/2}e^{-u}du = 2\int_0^\infty e^{-x^2}dx$ under $u = x^2$, so the two computations are the same identity ✓. Numerically $\sqrt\pi/2\approx0.8862$.

### Solution 33

*Transform.* Since $\mathcal{L}\left\{\int_0^ty\right\} = Y(s)/s$ and $y(0) = 0$,

$$sY(s) = \frac1s-\frac{Y(s)}{s} \Longrightarrow Y(s)\left(s+\frac1s\right) = \frac1s \Longrightarrow Y(s)\cdot\frac{s^2+1}{s} = \frac1s \Longrightarrow Y(s) = \frac{1}{s^2+1}.$$

*Invert.* $y(t) = \sin t$.

*Check.* $y(0) = 0$ ✓; $y' = \cos t$; and

$$1-\int_0^ty(\tau)d\tau = 1-\int_0^t\sin\tau\,d\tau = 1-\left[-\cos\tau\right]_0^t = 1+\cos t-1 = \cos t ✓.$$

*Second check by differentiating.* Differentiating $y' = 1-\int_0^ty$ gives $y'' = -y$, i.e. $y''+y = 0$, with $y(0) = 0$ and $y'(0) = 1$; the solution of that initial value problem is $\sin t$ ✓.

### Solution 34

*Transform.* $\left(s^2+4\right)Y = 3e^{-2s}$, so

$$Y(s) = 3e^{-2s}\cdot\frac{1}{s^2+4} \Longrightarrow y(t) = \frac32\sin\left(2(t-2)\right)u(t-2).$$

*Continuity at $t=2$.* $y(2^-) = 0$ and $y(2^+) = \frac32\sin0 = 0$ ✓: the displacement is continuous, as it must be for an impulse (a finite momentum change in zero time produces no displacement jump).

*Jump of the velocity.* For $t>2$, $y' = 3\cos\left(2(t-2)\right)$, so $y'(2^+) = 3$, while $y'(2^-) = 0$: the jump is $3$, the coefficient of the delta ✓. This is confirmed by integrating the equation across $t=2$:

$$y'(2^+)-y'(2^-)+4\int_{2-\varepsilon}^{2+\varepsilon}y\,dt = 3\int_{2-\varepsilon}^{2+\varepsilon}\delta(t-2)dt = 3,$$

and the integral of the bounded function $y$ tends to $0$ with $\varepsilon$ ✓.

*Check for $t\ne2$.* $y''+4y = 0$: with $u = t-2$, $y = \frac32\sin2u$, $y'' = -6\sin2u$, and $y''+4y = -6\sin2u+6\sin2u = 0$ ✓. And $y(0) = y'(0) = 0$ ✓.

### Solution 35

*Proof.* Suppose $\mathcal{L}\{e^{t^2}\}(s)$ exists for some $s = \sigma+i\omega$. Then

$$\int_0^\infty\left\lvert e^{-st}e^{t^2}\right\rvert dt = \int_0^\infty e^{t^2-\sigma t}dt .$$

The exponent $t^2-\sigma t = \left(t-\frac\sigma2\right)^2-\frac{\sigma^2}{4}$ tends to $+\infty$, so for $t$ larger than some $T$ it exceeds $1$. Hence

$$\int_T^\infty e^{t^2-\sigma t}dt\ge\int_T^\infty1\,dt = \infty,$$

and the integral diverges. Since $\sigma$ was arbitrary, no $s$ works: the ROC is empty.

*A fortiori the transform does not exist as an improper integral for any $s$, and the divergence is not merely at the boundary: the function grows faster than any exponential.*

*What it says about Theorem 7.1.* The theorem assumes $f$ is of exponential order, i.e. $\lvert f(t)\rvert\le Me^{\sigma_0t}$ for some finite $\sigma_0$. The function $e^{t^2}$ violates this for every $\sigma_0$ (since $t^2-\sigma_0t\to\infty$), so the hypothesis fails; the theorem is not contradicted, it is simply inapplicable. Every transform in this topic that is computed by the table satisfies the hypothesis, which is why the ROC can be stated as a right half-plane in each case.

### Solution 36

*Two-sided transform.* Split at $0$:

$$\mathcal{L}_2\{f\}(s) = \int_{-\infty}^0e^{-st}e^{at}dt+\int_0^\infty e^{-st}e^{-at}dt .$$

For the first integral, $\int_{-\infty}^0e^{(a-s)t}dt = \frac{1}{a-s}$ provided $\operatorname{Re}(a-s)>0$, i.e. $\operatorname{Re}s<a$. For the second, $\int_0^\infty e^{-(a+s)t}dt = \frac{1}{a+s}$ provided $\operatorname{Re}s>-a$. Hence

$$\mathcal{L}_2\{f\}(s) = \frac{1}{a-s}+\frac{1}{a+s} = \frac{2a}{a^2-s^2}, \qquad -a<\operatorname{Re}s<a .$$

The ROC is the vertical strip $-a<\operatorname{Re}s<a$ — not a right half-plane, because the function is not causal: it grows exponentially as $t\to-\infty$, so the transform needs decay in *both* directions.

*Fourier transform.* $f$ is integrable, so

$$\widehat f(\omega) = \int_{-\infty}^\infty e^{-i\omega t}e^{-a\lvert t\rvert}dt = 2\int_0^\infty e^{-at}\cos\omega t\,dt = \frac{2a}{a^2+\omega^2}.$$

Setting $s = i\omega$ in the two-sided transform, i.e. $s^2 = -\omega^2$, gives $\frac{2a}{a^2+\omega^2}$ — the same expression ✓, because the imaginary axis lies in the strip.

*Why the one-sided transform differs.* The one-sided transform ignores $t<0$:

$$\mathcal{L}\{f\}(s) = \int_0^\infty e^{-(s+a)t}dt = \frac{1}{s+a}, \qquad \operatorname{Re}s>-a .$$

The term $\frac{1}{a-s}$ is missing; it represents the contribution of the past. On $s = i\omega$ the one-sided transform gives $\frac{1}{a+i\omega}$, whose modulus is $\frac{1}{\sqrt{a^2+\omega^2}}$, not the Fourier transform $\frac{2a}{a^2+\omega^2}$: the one-sided transform of a non-causal function is simply a different object. This is the precise sense in which "the Laplace transform generalises the Fourier transform": the generalisation is the *two-sided* transform, and the one-sided version is adapted to causal signals and initial value problems.
