# Improper Integrals — Exercises

> [Improper Integrals](README.md) · 36 problems · Beginner → Challenge · Solutions: [solutions.md](solutions.md)

Decide convergence before you integrate, and write every improper integral as a limit at least once. For
each problem, name the type (first kind, second kind, or both), locate every singularity, and state the
test you are using. A bare value with no convergence argument is not a solution.

Notation: logarithms are natural, $\Gamma$ is the gamma function, and $s$ is a real Laplace parameter.
Constants of integration are not needed in definite integrals.

## Beginner

**1.** *(§7.5)* Evaluate $\displaystyle\int_1^{\infty}\frac{dx}{x^3}$.

**2.** *(§7.5)* Decide whether $\displaystyle\int_1^{\infty}\frac{dx}{\sqrt x}$ converges.

**3.** *(§7.6)* Evaluate $\displaystyle\int_0^1\frac{dx}{\sqrt[3]{x}}$.

**4.** *(§7.6)* Decide whether $\displaystyle\int_0^1\frac{dx}{x^2}$ converges.

**5.** *(§7.2)* Evaluate $\displaystyle\int_1^{\infty}e^{-2x}dx$.

**6.** *(§7.2)* Evaluate $\displaystyle\int_0^{\infty}e^{-x/3}dx$.

**7.** *(§7.2)* Evaluate $\displaystyle\int_{-\infty}^{-1}\frac{dx}{x^2}$.

**8.** *(§7.5)* Evaluate $\displaystyle\int_1^{\infty}\frac{dx}{x^{3/2}}$.

**9.** *(§7.3)* Evaluate $\displaystyle\int_0^4\frac{dx}{\sqrt{4-x}}$.

**10.** *(§7.2)* Evaluate $\displaystyle\int_0^{\infty}\frac{dx}{x^2+1}$.

**11.** *(§7.2)* Evaluate $\displaystyle\int_0^{\infty}xe^{-x^2}dx$.

**12.** *(§7.5)* Evaluate $\displaystyle\int_2^{\infty}\frac{dx}{x^{5/2}}$.

## Intermediate

**13.** *(§7.2)* Evaluate $\displaystyle\int_0^{\infty}\frac{dx}{x^2+4}$.

**14.** *(§7.2)* Evaluate $\displaystyle\int_0^{\infty}\frac{x}{(x^2+1)^2}\,dx$.

**15.** *(§7.2)* Evaluate $\displaystyle\int_0^{\infty}x^2e^{-x}dx$.

**16.** *(§7.3)* Evaluate $\displaystyle\int_0^1\sqrt x\,\ln x\,dx$.

**17.** *(§7.3)* Evaluate $\displaystyle\int_0^1x\ln x\,dx$.

**18.** *(§7.2)* Evaluate $\displaystyle\int_1^{\infty}\frac{\ln x}{x^2}\,dx$.

**19.** *(§7.2)* Evaluate $\displaystyle\int_0^{\infty}e^{-\sqrt x}dx$.

**20.** *(§7.2)* Evaluate $\displaystyle\int_0^{\infty}\frac{dx}{x^2+x+1}$.

**21.** *(§7.7)* Show that $\displaystyle\int_1^{\infty}\frac{\sin^2x}{x^2}\,dx$ converges.

**22.** *(§7.7)* Show that $\displaystyle\int_1^{\infty}\frac{dx}{x+e^x}$ converges.

## Advanced

**23.** *(§7.7, §8.3)* Show that $\displaystyle\int_2^{\infty}\frac{(\ln x)^p}{x^2}\,dx$ converges for every real $p$.

**24.** *(§7.10)* Show that $\displaystyle\int_0^{\infty}x^ae^{-x}dx$ converges exactly when $a>-1$, and express the value in terms of $\Gamma$.

**25.** *(§7.5, §7.6)* Show that $\displaystyle\int_0^{\infty}\frac{dx}{1+x^p}$ converges exactly when $p>1$.

**26.** *(§7.9)* Show that $\displaystyle\int_1^{\infty}\frac{\cos x}{x}\,dx$ converges conditionally.

**27.** *(§7.3, §7.7)* Show that $\displaystyle\int_0^1\ln(\sin x)\,dx$ converges.

**28.** *(§7.3, §7.10)* Show that $\displaystyle\int_0^{\infty}e^{-x}\ln x\,dx$ converges.

**29.** *(§7.2, §8.5)* Evaluate $\displaystyle\int_1^{\infty}\frac{dx}{x\sqrt{x+1}}$.

**30.** *(§7.12)* For $s>0$, derive $\mathcal{L}\{\cos\omega t\}(s)=\dfrac{s}{s^2+\omega^2}$.

**31.** *(§7.2, §8.5)* Evaluate $\displaystyle\int_0^{\infty}\frac{dx}{\sqrt x\,(1+x)}$.

## Challenge

**32.** *(§7.8)* Prove the limit-comparison test in all three cases: $0<L<\infty$, $L=0$, and $L=\infty$. State precisely what each case allows you to conclude, and give an example showing that $L=0$ together with a divergent comparison integral gives no information.

**33.** *(§7.10, §7.11)* Prove that $\Gamma\left(\frac12\right)=\sqrt\pi$, including the convergence of the gamma integral at $0$ and at infinity, the substitution $x=t^2$, and the evaluation of the Gaussian integral by squaring and polar coordinates.

**34.** *(§7.7)* Construct a continuous function $f>0$ on $[0,\infty)$ such that $\int_0^{\infty}f(x)\,dx$ converges but $f(x)$ does not tend to $0$ as $x\to\infty$. Prove both properties of your construction.

**35.** *(§7.9)* Prove: if $f$ is uniformly continuous on $[0,\infty)$ and $\int_0^{\infty}f(x)\,dx$ converges, then $f(x)\to0$ as $x\to\infty$. Show by example that uniform continuity cannot be dropped.

**36.** *(§7.5, §7.6)* For which real $p$ does $\displaystyle\int_0^{\infty}\frac{x^{p-1}}{1+x}\,dx$ converge? For $p=\frac12$, evaluate the integral.
