# Techniques of Integration — Exercises

> [Techniques of Integration](README.md) · 36 problems · Beginner → Challenge · Solutions: [solutions.md](solutions.md)

Work through the problems in order; each cites the section of the tutorial it draws on. The set is
designed so that every technique of §§7–8 appears at least three times. Do not consult
[solutions.md](solutions.md) until you have written an attempt, and **differentiate your answer** before
you do: most errors in this topic are visible immediately in the check.

Notation: all angles are in radians, logarithms are natural, and constants of integration are required in
every indefinite integral.

## Beginner

**1.** *(§7.1)* Evaluate $\displaystyle\int 2x\left(x^2+1\right)^5dx$.

**2.** *(§7.1)* Evaluate $\displaystyle\int x e^{x^2}dx$.

**3.** *(§7.1)* Evaluate $\displaystyle\int \cos(3x)\,dx$.

**4.** *(§7.1)* Evaluate $\displaystyle\int\frac{x}{x^2+1}\,dx$.

**5.** *(§7.2)* Evaluate $\displaystyle\int x\ln x\,dx$ for $x>0$.

**6.** *(§7.2)* Evaluate $\displaystyle\int x\cos x\,dx$.

**7.** *(§7.3)* Evaluate $\displaystyle\int\sin^2x\,dx$.

**8.** *(§7.5)* Evaluate $\displaystyle\int\frac{dx}{x^2-1}$.

**9.** *(§8.3)* Evaluate $\displaystyle\int\frac{dx}{x^2+9}$.

**10.** *(§8.3)* Evaluate $\displaystyle\int\frac{dx}{\sqrt{9-x^2}}$.

**11.** *(§7.1)* Evaluate $\displaystyle\int\frac{2x+1}{x^2+x+1}\,dx$.

**12.** *(§7.2, §7.4)* Evaluate $\displaystyle\int_0^1 xe^x\,dx$.

## Intermediate

**13.** *(§7.3)* Evaluate $\displaystyle\int\sin^3x\cos^3x\,dx$.

**14.** *(§7.3)* Evaluate $\displaystyle\int\sec^4x\,dx$.

**15.** *(§7.2)* Evaluate $\displaystyle\int x^2e^{-x}dx$.

**16.** *(§7.2)* Evaluate $\displaystyle\int\arctan x\,dx$.

**17.** *(§7.5)* Evaluate $\displaystyle\int\frac{x^3+x^2+1}{x^2+1}\,dx$.

**18.** *(§7.5)* Evaluate $\displaystyle\int\frac{dx}{x^3+x}$.

**19.** *(§7.5)* Evaluate $\displaystyle\int\frac{dx}{x^2+2x+5}$.

**20.** *(§7.4)* Evaluate $\displaystyle\int\sqrt{9-x^2}\,dx$.

**21.** *(§7.4)* Evaluate $\displaystyle\int\frac{dx}{x\sqrt{x^2-1}}$ for $x>1$.

**22.** *(§7.6)* Evaluate $\displaystyle\int\frac{dx}{1+\sqrt x}$.

**23.** *(§7.7)* Approximate $\displaystyle\int_0^1\frac{dx}{1+x^2}$ by Simpson's rule with $n=4$, and
bound the error using $\left|f^{(4)}\right|\le 24$ on $[0,1]$.

**24.** *(§7.5)* Evaluate $\displaystyle\int\frac{x}{x^2+4x+5}\,dx$.

## Advanced

**25.** *(§7.5)* Evaluate $\displaystyle\int\frac{dx}{x^4-1}$.

**26.** *(§7.6)* Evaluate $\displaystyle\int\frac{\sqrt{x^2+4}}{x}\,dx$ using the substitution
$u = \sqrt{x^2+4}$.

**27.** *(§7.3, §7.6)* Evaluate $\displaystyle\int\frac{dx}{\sin x+\cos x}$.

**28.** *(§7.1, §7.2)* Evaluate $\displaystyle\int x^3e^{x^2}dx$.

**29.** *(§8.4)* Prove that $\displaystyle I_n = \int_0^{\pi/2}\sin^n x\,dx$ satisfies
$I_n = \frac{n-1}{n}I_{n-2}$ for $n\ge2$, and use it to compute $I_5$.

**30.** *(§7.6)* Evaluate $\displaystyle\int\frac{dx}{1+x^{1/3}}$.

**31.** *(§7.7)* Approximate $\displaystyle\int_0^1 e^{-x^2}dx$ by Simpson's rule with $n=4$, and bound
the error using $\left|f^{(4)}\right|\le 20$ on $[0,1]$. Compare with the value $0.746824$ (six
decimals).

**32.** *(§7.4)* Evaluate $\displaystyle\int\frac{dx}{\left(x^2+1\right)^{3/2}}$ and verify the answer by
differentiation.

## Challenge

**33.** *(§7.1)* State and prove the substitution theorem for definite integrals from the Fundamental
Theorem of Calculus, including all hypotheses. Explain where each hypothesis is used.

**34.** *(§7.7)* Prove that Simpson's rule is exact for every cubic polynomial: on a panel $[-h,h]$ with
nodes $-h,0,h$, show that
$\frac h3\left[f(-h)+4f(0)+f(h)\right] = \int_{-h}^{h}f(x)\,dx$ for $f(x) = 1,x,x^2,x^3$, and deduce it
for all cubics.

**35.** *(§7.6)* Evaluate $\displaystyle\int\frac{dx}{2+\sin x}$ by the Weierstrass substitution, stating
carefully the intervals on which the formula is valid and what happens at odd multiples of $\pi$.

**36.** *(§7.1, §7.3)* Show that $\displaystyle\int_0^{\pi/2}\ln(\sin x)\,dx = -\frac{\pi}{2}\ln 2$.
The integral is improper at $0$; work with $\int_\varepsilon^{\pi/2}$ and let
$\varepsilon\to0^+$ at the end.
