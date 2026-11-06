# Continuity and Limits of Functions — Exercises

> [Tutorial](README.md) · 36 problems · Levels: Beginner, Intermediate, Advanced, Challenge

Every problem asks for a proof unless it explicitly asks for a computation; for computations you must
also justify the answer (by the algebra of limits and the continuity of the standard functions, or, when
the problem says so, directly from the definition). You may use any result proved in the
[tutorial](README.md) and in [The Real Numbers and Completeness](../01-real-numbers-and-completeness/README.md),
and the standard facts about $\sin$, $\cos$, $\lvert x\rvert$ and $\lfloor x\rfloor$ from elementary
calculus: $\lvert\sin t\rvert \le 1$, $\lvert\sin t\rvert \le \lvert t\rvert$, $\cos(\pi/2) = 0$, and
continuity of $\sin$ and $\cos$. Do not use the derivative: differentiation is the next topic.

Full solutions are in [solutions.md](solutions.md). Do not open that file until you have attempted the
problems.

## Beginner

**1.** Prove from Definition 5.2 that
$$
\lim_{x \to 1} (5x - 2) = 3 .
$$

**2.** Prove from Definition 5.2 that
$$
\lim_{x \to -2} (x^2 + 3x) = -2 .
$$
(You will need to restrict $\lvert x + 2\rvert$ before estimating the second factor.)

**3.** Prove from Definition 5.2 that
$$
\lim_{x \to 2} \frac{1}{x} = \frac{1}{2} .
$$

**4.** Prove from Definition 5.2 that
$$
\lim_{x \to 9} \sqrt{x} = 3 .
$$

**5.** Prove that
$$
\lim_{x \to 0} x\cos\frac{1}{x} = 0 .
$$

**6.** Compute $\displaystyle\lim_{x \to 2} \frac{x^3 - 8}{x - 2}$, justifying every step with a theorem from the tutorial.

**7.** Let $f(x) = \lfloor x \rfloor$. Compute $\displaystyle\lim_{x \to 1^-} f(x)$ and $\displaystyle\lim_{x \to 1^+} f(x)$, and decide whether $\displaystyle\lim_{x \to 1} f(x)$ exists. Justify your answer with Theorem 7.7.

**8.** Explain why $\displaystyle\lim_{x \to 4} \frac{x^2 - 16}{x - 4}$ exists although the formula is undefined at $x = 4$, and compute the limit.

**9.** Determine the set of points at which
$$
f(x) = \frac{x^2 - 1}{x^2 - 4}
$$
is continuous. At which of the points where $f$ is undefined does a continuous extension exist? Give the extension where it does.

**10.** Prove that $f(x) = \lvert x - 3\rvert$ is continuous at every point of $\mathbb{R}$.

**11.** Using Theorem 7.9 and Corollary 7.11 (not the definition), prove that $p(x) = 2x^3 - 5x + 1$ is continuous at every point of $\mathbb{R}$.

**12.** Prove that $f(x) = \sqrt{x^2 + 1}$ is continuous on $\mathbb{R}$.

## Intermediate

**13.** Let $f : A \to \mathbb{R}$ and suppose $\lim_{x\to a} f(x) = L$. Prove that $\lim_{x \to a}\lvert f(x)\rvert = \lvert L\rvert$. Show by example that the converse is false.

**14.** (Order and squeeze for functions.) Let $a$ be a cluster point of $A$, and let $f, g : A \to \mathbb{R}$ with $\lim_{x\to a} f(x) = L$ and $\lim_{x \to a} g(x) = M$.

(a) Suppose there is $\delta_0 > 0$ such that $f(x) \le g(x)$ for all $x \in A$ with $0 < \lvert x-a\rvert < \delta_0$. Prove that $L \le M$.

(b) Deduce: if $\lvert f(x) - L\rvert \le g(x)$ for all $x$ near $a$ and $\lim_{x\to a} g(x) = 0$, then $\lim_{x\to a} f(x) = L$.

**15.** Prove, using the sequential criterion (Theorem 7.3), that $\displaystyle\lim_{x \to 0} \sin\frac{1}{x}$ does not exist.

**16.** Define $f : \mathbb{R} \setminus \{0\} \to \mathbb{R}$ by $f(x) = x/\lvert x\rvert$. Prove that $\lim_{x\to 0^+} f(x)$ and $\lim_{x\to 0^-} f(x)$ both exist, that they differ, and that $\lim_{x\to 0} f(x)$ does not exist.

**17.** Let $f$ be continuous on $[a,b]$ and suppose $f(x) \ne 0$ for every $x \in [a,b]$. Prove that $f$ has constant sign on $[a,b]$: either $f(x) > 0$ for all $x$, or $f(x) < 0$ for all $x$.

**18.** Prove that the equation $x = \cos x$ has a solution in the interval $(0, \pi/2)$.

**19.** Let $f:[0,1] \to \mathbb{R}$ be continuous, and suppose that $f(x) \in \mathbb{Q}$ for every $x \in [0,1]$. Prove that $f$ is constant.

**20.** Let $f:[0,1] \to \mathbb{R}$ be continuous with $f(0) = f(1) = 0$. Prove that there exists $c \in [0, 1/2]$ with
$$
f(c) = f\Bigl(c + \tfrac12\Bigr).
$$

**21.** Prove from Definition 7.21 that
$$
\lim_{x \to \infty} \frac{2x+1}{x-3} = 2 .
$$
State the value of $M$ you use as a function of $\varepsilon$.

**22.** Prove that the function
$$
f(x) = \begin{cases} x^2 \sin\dfrac1x, & x \ne 0,\\[4pt] 0, & x = 0, \end{cases}
$$
is continuous at $0$, and that $g(x) = 1/f(x)$ (defined where $f(x) \ne 0$) is not bounded on any interval $(-\delta, \delta)$.

## Advanced

**23.** Prove that every polynomial of odd degree has at least one real root. (You may use Definition 7.21 and the algebra of limits.)

**24.** Let $f$ be continuous on $[a,b]$, and put
$$
m := \min_{x \in [a,b]} f(x), \qquad M := \max_{x \in [a,b]} f(x),
$$
which exist by the extreme value theorem. Prove that $f\bigl[[a,b]\bigr] = [m, M]$.

**25.** Prove directly from Definition 5.6 (without invoking Theorem 7.18) that $f(x) = x^2$ is uniformly continuous on $[0,2]$. Then prove that $x^2$ is not uniformly continuous on $\mathbb{R}$.

**26.** Prove that $f(x) = 1/x$ is not uniformly continuous on $(0,1)$, but is uniformly continuous on $[1,\infty)$.

**27.** Prove directly from Definition 5.6 (without using Corollary 7.11) that $f(x) = \sqrt{x}$ is uniformly continuous on $[0,\infty)$.

**28.** Let $-\infty < a < b < \infty$ and suppose $f$ is uniformly continuous on $(a,b)$. Prove that the one-sided limits
$$
\lim_{x \to a^+} f(x), \qquad \lim_{x \to b^-} f(x)
$$
both exist in $\mathbb{R}$. (You may use the Cauchy completeness theorem, Theorem 7.33 of [The Real Numbers and Completeness](../01-real-numbers-and-completeness/README.md).)

**29.** Let $f(x) = \sin(1/x)$ on $(0,1)$. Prove that $f$ is continuous on $(0,1)$, that $f$ is not uniformly continuous on $(0,1)$, and that there is no continuous function $F : [0,1] \to \mathbb{R}$ extending $f$.

**30.** Let $f : [a,b] \to \mathbb{R}$ be nondecreasing. For $n \in \mathbb{N}$ let
$$
D_n := \Bigl\{c \in (a,b) : f(c^+) - f(c^-) \ge \tfrac1n\Bigr\},
$$
where $f(c^-) = \sup\{f(x) : a < x < c\}$ and $f(c^+) = \inf\{f(x) : c < x < b\}$.

(a) Prove that $D_n$ is finite; more precisely, prove that $D_n$ has at most $n\bigl(f(b)-f(a)\bigr) + 1$ elements.

(b) Deduce that the set of discontinuity points of $f$ is at most countable.

## Challenge

**31.** (Thomae's function.) Define $f : \mathbb{R} \to \mathbb{R}$ by
$$
f(x) := \begin{cases} \dfrac1q, & x = \dfrac pq \text{ in lowest terms with } p \in \mathbb{Z},\ q \in \mathbb{N},\\[8pt] 0, & x \notin \mathbb{Q}. \end{cases}
$$
Prove that $f$ is continuous at every irrational number and discontinuous at every rational number.

**32.** Prove that there is no continuous function $f : [0,1] \to \mathbb{R}$ whose image is exactly the open interval $(0,1)$.

**33.** Let $f : [a,b] \to \mathbb{R}$ be continuous and injective. Prove that $f$ is strictly monotone.

**34.** Let $f : [0,1] \to [0,1]$ be continuous. Prove that the set
$$
F := \{x \in [0,1] : f(x) = x\}
$$
is nonempty, and that it is *sequentially closed*: if $x_n \in F$ for all $n$ and $x_n \to x$, then $x \in F$.

**35.** (a) Give an example of a bounded continuous function on $(0,1)$ that is not uniformly continuous on $(0,1)$, and prove all the claimed properties.

(b) Conversely, prove that if $f$ is continuous on $(0,1)$ and both one-sided limits $\lim_{x\to 0^+} f(x)$ and $\lim_{x\to 1^-} f(x)$ exist in $\mathbb{R}$, then $f$ is uniformly continuous on $(0,1)$.

**36.** Let $f : \mathbb{R} \to \mathbb{R}$ be continuous and suppose that $f(f(x)) = x$ for every $x \in \mathbb{R}$. Prove that $f$ has a fixed point.
