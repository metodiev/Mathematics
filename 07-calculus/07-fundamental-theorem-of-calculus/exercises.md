# The Fundamental Theorem of Calculus — Exercises

> [The Fundamental Theorem of Calculus](README.md) · 36 problems · Beginner → Challenge · Solutions: [solutions.md](solutions.md)

Work through the problems in order. Each problem cites the section of the tutorial it draws on. Every
problem is solvable from §§5–8 alone; the challenge problems ask for a little more persistence, not for
extra theory. Do not open [solutions.md](solutions.md) until you have written an attempt.

Notation: $\int_a^b f$ is the definite integral, $\int f(x)\,dx$ the indefinite integral, and
$F_{\mathrm{avg}}$ or $f_{\mathrm{avg}}$ denotes an average value. Angles are in radians.

## Beginner

**1.** *(§7.3, §7.4)* Evaluate $\displaystyle\int_0^2\left(3x^2 - 4x + 1\right)dx$ and check the answer by
differentiating the antiderivative.

**2.** *(§7.4)* Evaluate $\displaystyle\int_1^4\frac{dt}{\sqrt{t}}$.

**3.** *(§7.4)* Evaluate $\displaystyle\int_0^{\pi/2}\cos x\,dx$.

**4.** *(§7.4)* Evaluate $\displaystyle\int_{-1}^{1}\left(x^3 + x\right)dx$ twice: once from an
antiderivative, and once from a symmetry argument.

**5.** *(§7.3)* Differentiate $\displaystyle F(x) = \int_0^x \frac{t^2+1}{t^2+2}\,dt$.

**6.** *(§7.3)* Differentiate $\displaystyle G(x) = \int_2^x \sqrt{t^3+1}\,dt$, stating the interval of
validity.

**7.** *(§7.8)* Differentiate $\displaystyle H(x) = \int_0^{x^2}\sin t\,dt$.

**8.** *(§7.8)* Differentiate $\displaystyle K(x) = \int_x^{5}\cos\left(t^2\right)dt$.

**9.** *(§7.6)* Find $\displaystyle\int\left(3x^2 - \frac{2}{x}\right)dx$ on the interval $x>0$, and verify
the answer by differentiation.

**10.** *(§7.6)* Find the antiderivative $F$ of $f(x) = 4x^3$ with $F(1) = 5$.

**11.** *(§7.2)* Find the average value of $f(x) = x$ on $[0,4]$, and find every $c \in [0,4]$ with
$f(c) = f_{\mathrm{avg}}$.

**12.** *(§7.7)* A quantity $Q$ changes at the rate $r(t) = 2t + 1$. Find the net change of $Q$ from
$t = 0$ to $t = 3$.

## Intermediate

**13.** *(§7.8)* Differentiate $\displaystyle F(x) = \int_{x}^{x^2}\sqrt{1+t^3}\,dt$, stating the interval
on which the formula is valid, and evaluate $F'(1)$.

**14.** *(§7.8)* Differentiate $\displaystyle G(x) = \int_{\sin x}^{\cos x} e^{t^2}dt$.

**15.** *(§7.8)* Let $f$ be continuous. Prove that

$$\frac{d}{dx}\int_0^x (x-t)f(t)\,dt = \int_0^x f(t)\,dt,$$

and deduce that the second derivative of the left side is $f(x)$.

**16.** *(§7.3)* Let $\displaystyle F(x) = \int_1^x \frac{t^2-4}{t^2+1}\,dt$. Find the intervals on which
$F$ is increasing and decreasing, and classify its local extrema. (Values of $F$ are not required.)

**17.** *(§7.2)* Find every $c \in [0,2]$ with $f(c) = f_{\mathrm{avg}}$ for $f(x) = x^3$ on $[0,2]$.

**18.** *(§7.2)* Find every $c \in [1,3]$ with $f(c) = f_{\mathrm{avg}}$ for $f(x) = 1/x$ on $[1,3]$, and
confirm numerically that $1 \le c \le 3$.

**19.** *(§7.7)* A particle has velocity $v(t) = t^2 - 2t$ on $0 \le t \le 3$. Find its displacement and
the total distance travelled.

**20.** *(§7.2)* Find the average value of $v(t) = 3t^2$ on $[0,2]$, and find the point where it is
attained.

**21.** *(§7.3)* Find a continuous $f$ such that
(a) $\displaystyle\int_0^x f(t)\,dt = x^3 + x$ for all $x$;
(b) $\displaystyle\int_1^x f(t)\,dt = \ln x$ for all $x>0$.

**22.** *(§7.3, §9)* Compute $\displaystyle\lim_{x\to 0}\frac{1}{x}\int_0^x \cos\left(t^2\right)dt$.

**23.** *(§7.3, §9)* Compute $\displaystyle\lim_{x\to 0}\frac{1}{x^2}\int_0^x\left(e^{t}-1\right)dt$.

**24.** *(§7.3, §7.9)* Let $f(t) = t$ for $0 \le t < 1$, $f(t) = 3 - t$ for $1 \le t \le 2$, and
$f(t) = 0$ otherwise. Let $\displaystyle F(x) = \int_0^x f(t)\,dt$. Compute $F(1)$, $F(3/2)$, $F(2)$ and
$F(3)$, then state at which points the identity $F'(x) = f(x)$ fails.

## Advanced

**25.** *(§7.3, §8.2)* Prove: if $f$ is continuous on $[a,b]$ and $\int_a^x f(t)\,dt = 0$ for every
$x \in [a,b]$, then $f(x) = 0$ for every $x \in [a,b]$.

**26.** *(§7.1, §8.10)* Let $f$ be continuous on $[a,b]$ and $M = \max_{[a,b]}|f|$. Prove that
$F(x) = \int_a^x f(t)\,dt$ satisfies $|F(y)-F(x)| \le M|y-x|$ for all $x,y \in [a,b]$, and conclude that
$F$ is uniformly continuous on $[a,b]$.

**27.** *(§7.2, §7.3)* Let $f$ be continuous on $[a,b]$. Prove that there exists $c \in [a,b]$ such that
$\int_a^c f = \int_c^b f$.

**28.** *(§8.9)* Let $f$ be continuous and non-negative on $[a,b]$, with $\int_a^b f = 0$. Prove that
$f(x) = 0$ for every $x \in [a,b]$. Show by an example that continuity is needed.

**29.** *(§7.2)* Let $f$ be continuous on $[0,1]$. Prove that there exists $c \in [0,1]$ with

$$\int_0^1 x^2 f(x)\,dx = \frac{f(c)}{3}.$$

**30.** *(§7.8)* Let $f$ be continuous on $\mathbb{R}$ and periodic with period $p>0$, so
$f(t+p) = f(t)$ for all $t$. Prove that $\int_a^{a+p} f(t)\,dt = \int_0^p f(t)\,dt$ for every real $a$.

**31.** *(§7.3, §7.8)* Let $f$ be continuous on $\mathbb{R}$ and $F(x) = \int_0^x f(t)\,dt$. Prove:
(i) $F$ is even if and only if $f$ is odd; (ii) $F$ is odd if and only if $f$ is even.

**32.** *(§7.9)* Define $G(x) = -\arctan(1/x)$ for $x \ne 0$ and $G(0) = 0$. Show that
$G'(x) = \dfrac{1}{1+x^2}$ for every $x \ne 0$, that $G$ is not continuous at $0$, and that using
$G(1) - G(-1)$ to compute $\displaystyle\int_{-1}^{1}\frac{dx}{1+x^2}$ gives the wrong sign. Explain
which hypothesis of Theorem 7.4.1 fails.

## Challenge

**33.** *(§7.3, §7.4)* Let $f$ be continuous on $[0,1]$ and suppose that
$\int_0^x f(t)\,dt = \int_x^1 f(t)\,dt$ for every $x \in [0,1]$. Determine $f$ completely, with proof.

**34.** *(§7.9)* Define $F(x) = x^2\sin\left(1/x^2\right)$ for $x>0$ and $F(0) = 0$.
(a) Show that $F$ is differentiable on $[0,1]$ and compute $F'(x)$ for $x>0$.
(b) Show that $F'$ is unbounded on $[0,1]$ and explain why the Net Change Theorem does not apply to it.
(c) Does the conclusion $\int_0^1 F'(t)\,dt = F(1)-F(0)$ hold in any extended sense?

**35.** *(§8.9, §8.11)* Prove: if $f$ is continuous on $[a,b]$ and
$\int_a^b f(x)g(x)\,dx = 0$ for every continuous $g$ on $[a,b]$, then $f \equiv 0$ on $[a,b]$.

**36.** *(§7.1, §7.3)* Let $f$ be continuous on $[0,1]$. Prove that

$$\lim_{n\to\infty}\int_0^1 f\left(x^n\right)dx = f(0).$$
