# Limits — Exercises

> [Tutorial](README.md) · 36 problems · Levels: Beginner, Intermediate, Advanced, Challenge

Show every step, name the theorem or law you are using, and state explicitly when a limit does not
exist. For $\varepsilon$-$\delta$ problems, exhibit a $\delta$ (as a function of $\varepsilon$) and
verify the implication; a numerical table is not a proof. Full solutions are in
[solutions.md](solutions.md); do not open that file until you have attempted the problems.

## Beginner

**1.** Compute $\displaystyle\lim_{x\to3}\left(x^2-2x+5\right)$.

**2.** Compute $\displaystyle\lim_{x\to-2}\left(x^3+4x-1\right)$.

**3.** Compute $\displaystyle\lim_{x\to4}\frac{x^2-16}{x-4}$.

**4.** Compute $\displaystyle\lim_{x\to2}\frac{x^2-x-2}{x^2-4}$.

**5.** Compute $\displaystyle\lim_{x\to0}\frac{3x^2+x}{x}$.

**6.** Compute $\displaystyle\lim_{x\to-1}\frac{x^2-1}{x+1}$.

**7.** Let
$$
f(x)=\begin{cases}x+3, & x<0,\\ x^2+1, & x\ge0.\end{cases}
$$
Find $\displaystyle\lim_{x\to0^-}f(x)$, $\displaystyle\lim_{x\to0^+}f(x)$, and decide whether $\displaystyle\lim_{x\to0}f(x)$ exists.

**8.** Let
$$
g(x)=\begin{cases}x^2, & x<2,\\ 5-x, & x>2.\end{cases}
$$
Find both one-sided limits at $2$ and decide whether the two-sided limit exists.

**9.** Compute $\displaystyle\lim_{x\to\infty}\frac{4x^2-3}{2x^2+x}$.

**10.** Compute $\displaystyle\lim_{x\to-\infty}\frac{5x^3+x}{x^3-2}$.

**11.** Compute $\displaystyle\lim_{x\to\infty}\left(\frac{2}{x}+\frac{3}{x^2}\right)$.

**12.** Compute $\displaystyle\lim_{x\to0}\frac{\sin 5x}{x}$.

**13.** Compute $\displaystyle\lim_{x\to0}\frac{1-\cos x}{x^2}$.

**14.** Compute $\displaystyle\lim_{x\to0}\frac{\tan 2x}{x}$.

## Intermediate

**15.** Compute $\displaystyle\lim_{x\to0}\frac{\sqrt{x+9}-3}{x}$.

**16.** Compute $\displaystyle\lim_{x\to4}\frac{\sqrt{2x+1}-3}{x-4}$.

**17.** Compute $\displaystyle\lim_{x\to\infty}\left(\sqrt{4x^2+3x}-2x\right)$.

**18.** Compute $\displaystyle\lim_{x\to-\infty}\left(\sqrt{x^2+2x}+x\right)$.

**19.** Compute $\displaystyle\lim_{x\to\infty}\frac{3x^3-2x+1}{x^3+x^2-5}$.

**20.** Compute $\displaystyle\lim_{x\to0}\frac{\sin 3x}{\sin 7x}$.

**21.** Compute $\displaystyle\lim_{x\to0}\frac{1-\cos 3x}{x^2}$.

**22.** Compute $\displaystyle\lim_{x\to0}\frac{e^{2x}-1}{x}$.

**23.** Prove from the $\varepsilon$-$\delta$ definition that $\displaystyle\lim_{x\to1}(4x-1)=3$. Give an explicit $\delta$ in terms of $\varepsilon$ and verify the definition.

**24.** Prove from the $\varepsilon$-$\delta$ definition that $\displaystyle\lim_{x\to2}x^2=4$. Give an explicit $\delta$ in terms of $\varepsilon$ and verify the definition.

**25.** Prove from the $\varepsilon$-$\delta$ definition that $\displaystyle\lim_{x\to4}\sqrt{x}=2$. Give an explicit $\delta$ in terms of $\varepsilon$ and verify the definition.

## Advanced

**26.** Let $\lim_{x\to a}f(x)=L$ and $\lim_{x\to a}g(x)=M$. Prove from the $\varepsilon$-$\delta$ definition that $\lim_{x\to a}\bigl(f(x)+g(x)\bigr)=L+M$.

**27.** Prove that $\displaystyle\lim_{x\to0}x\sin\frac1x=0$ for $x\neq0$, state clearly which theorem you use, and explain why the same argument does not apply to $\sin(1/x)$.

**28.** Prove that $\displaystyle\lim_{x\to0}\sin\frac1x$ does not exist by exhibiting two sequences $(x_n)$ and $(y_n)$ with $x_n\to0$, $y_n\to0$, $x_n\neq0$, $y_n\neq0$, and different limits of the function values. State the theorem you use.

**29.** Compute $\displaystyle\lim_{x\to0}\frac{x-\sin x}{x^3}$ using L'Hôpital's rule. Verify the hypotheses at every application, and state why the computation does not run into a circularity.

**30.** Consider $f(x)=\dfrac{x}{x-2}$. Show that $\displaystyle\lim_{x\to2^+}f(x)=+\infty$ directly from Definition 5.4 (find $\delta$ for a given $M$), and determine $\displaystyle\lim_{x\to2^-}f(x)$.

**31.** (a) Prove the sign-preservation lemma: if $\lim_{x\to a}f(x)=L>0$, then there is $\delta>0$ with $f(x)>L/2>0$ whenever $0<\lvert x-a\rvert<\delta$. (b) Prove the order-comparison lemma: if $\lim f=L$, $\lim g=M$ and $L<M$, then $f(x)<g(x)$ on some punctured neighbourhood of $a$.

**32.** (a) Prove that if $\lim_{x\to a}f(x)=L$, then $\lim_{x\to a}\lvert f(x)\rvert=\lvert L\rvert$. (b) Show that the converse fails, by giving a function $f$ and a point $a$ for which $\lvert f\rvert$ has a limit but $f$ does not.

## Challenge

**33.** Prove the squeeze theorem in full: if $f(x)\le g(x)\le h(x)$ for $0<\lvert x-a\rvert<\delta_0$ and $\lim_{x\to a}f(x)=\lim_{x\to a}h(x)=L$, then $\lim_{x\to a}g(x)=L$. Then state and prove the one-sided version for $x\to a^+$.

**34.** Prove that if $f$ is bounded on a punctured neighbourhood of $a$ and $\lim_{x\to a}g(x)=0$, then $\lim_{x\to a}f(x)g(x)=0$. Deduce that $x^n\sin(1/x)\to0$ as $x\to0$ for every $n\ge1$, and explain why the result does not require $\lim_{x\to a}f(x)$ to exist.

**35.** (a) Prove the sequential criterion: $\lim_{x\to a}f(x)=L$ if and only if for every sequence $(x_n)$ in the domain with $x_n\neq a$ and $x_n\to a$, one has $f(x_n)\to L$. (b) Use it to prove that $\displaystyle\lim_{x\to0}\cos\frac1x$ does not exist.

**36.** (a) Prove that if $\lim_{x\to\infty}f(x)=L$, then the sequence $a_n=f(n)$ converges to $L$. (b) Give an example of a function $f$ for which $f(n)\to0$ but $\lim_{x\to\infty}f(x)$ does not exist. (c) Compute $\displaystyle\lim_{x\to\infty}x^{1/x}$, justifying each step by a theorem from the tutorial.
