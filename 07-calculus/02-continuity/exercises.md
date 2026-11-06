# Continuity — Exercises

> [Tutorial](README.md) · 36 problems · Levels: Beginner, Intermediate, Advanced, Challenge

Justify each answer by a definition or a named theorem, and verify the hypotheses of any theorem you
use. For existence statements, exhibit the interval and the sign change (or the fixed-point
inequality); for non-existence statements, give sequences or an explicit obstruction. Full solutions
are in [solutions.md](solutions.md); do not open that file until you have attempted the problems.

## Beginner

**1.** Test $f(x)=x^2-3x+2$ for continuity at $x=2$ by checking the three conditions explicitly.

**2.** Is $f(x)=\dfrac{x^2-1}{x-1}$ continuous at $x=1$? If not, what type of discontinuity is it, and
what value at $x=1$ would make the function continuous there?

**3.** What type of discontinuity does $f(x)=\dfrac{1}{x-3}$ have at $x=3$?

**4.** Find both one-sided limits of $f(x)=\dfrac{\lvert x\rvert}{x}$ at $0$ and classify the
discontinuity.

**5.** Find both one-sided limits of $f(x)=\lfloor x\rfloor$ at $x=2$ and classify the discontinuity.

**6.** What type of discontinuity does $f(x)=\sin\dfrac1x$ have at $x=0$? Justify your answer.

**7.** Let
$$
f(x)=\begin{cases}x^2, & x<1,\\ 2x-1, & x\ge1.\end{cases}
$$
Determine whether $f$ is continuous at $x=1$.

**8.** Let
$$
g(x)=\begin{cases}x+2, & x\le0,\\ x^2+2, & x>0.\end{cases}
$$
Determine whether $g$ is continuous at $x=0$.

**9.** State the intervals on which $f(x)=\dfrac{1}{x^2-4}$ is continuous, and justify your answer.

**10.** State the interval on which $f(x)=\sqrt{x-5}$ is continuous, and justify your answer.

**11.** Using the algebra of continuous functions, explain why $f(x)=x^3$ is continuous at $x=-1$.

**12.** Is the discontinuity of $f(x)=\dfrac{x^2-4}{x+2}$ at $x=-2$ removable? If so, give the
continuous extension.

**13.** What type of discontinuity does $f(x)=\tan x$ have at $x=\dfrac{\pi}{2}$?

**14.** Describe the behaviour of $f(x)=e^{1/x}$ as $x\to0^-$ and as $x\to0^+$, and classify its
discontinuity at $0$.

## Intermediate

**15.** Find the constant $k$ for which
$$
f(x)=\begin{cases}\dfrac{x^2-9}{x-3}, & x\neq3,\\ k, & x=3\end{cases}
$$
is continuous at $x=3$.

**16.** Find $a$ and $b$ for which
$$
f(x)=\begin{cases}x+1, & x<1,\\ ax+b, & 1\le x<3,\\ x^2-1, & x\ge3\end{cases}
$$
is continuous on $\mathbb{R}$.

**17.** Show that $p(x)=x^3+x-1$ has a root in $(0,1)$, then use two bisection steps to locate a root
to within $1/4$.

**18.** Show that the equation $x^3=3x-1$ has a root in $(0,1)$.

**19.** Show that the equation $\cos x=x$ has a root in $(0,1)$.

**20.** Show that $x^2=2$ has a root in $[1,2]$, and use one bisection step to locate a root to within
$1/4$.

**21.** Explain why $f(x)=\dfrac1x$ has no maximum on $(0,1)$, and why this does not contradict the
extreme value theorem.

**22.** Does $f(x)=x^2$ attain a maximum and a minimum on $(-1,1)$? Explain, referring to the
hypotheses of the extreme value theorem.

**23.** Let $f:[0,1]\to[0,1]$, $f(x)=\dfrac{x+1}{2}$. Prove that $f$ has a fixed point and find it.

**24.** Prove that $f(x)=5x-2$ is uniformly continuous on $\mathbb{R}$ by exhibiting a $\delta$ for
each $\varepsilon$.

**25.** Prove that $f(x)=\dfrac1x$ is uniformly continuous on $[2,\infty)$ by exhibiting a $\delta$ for
each $\varepsilon$.

**26.** Prove that $f(x)=x^2$ is not uniformly continuous on $[0,\infty)$ by exhibiting two sequences.

## Advanced

**27.** Let $f$ and $g$ be continuous at $a$. Prove directly from the $\varepsilon$-$\delta$
definition that $f+g$ is continuous at $a$.

**28.** Prove the composition theorem: if $g$ is continuous at $a$ and $f$ is continuous at $g(a)$,
then $f\circ g$ is continuous at $a$. Explain where each hypothesis is used.

**29.** Let $f$ be continuous on $[a,b]$ and suppose $f(x)>0$ for every $x\in[a,b]$. Prove that there
is a constant $m>0$ with $f(x)\ge m$ for all $x\in[a,b]$.

**30.** Let $f$ be continuous on $[a,b]$ with $f(a)<f(b)$. Prove that the range of $f$ contains the
whole interval $[f(a),f(b)]$.

**31.** Let $f:[0,1]\to[0,1]$ be continuous. Prove that $f$ has a fixed point.

**32.** Prove that uniform continuity preserves Cauchy sequences: if $f$ is uniformly continuous on
$A$ and $(x_n)$ is a Cauchy sequence in $A$, then $(f(x_n))$ is a Cauchy sequence.

**33.** Prove that $f(x)=x^2$ is uniformly continuous on $[0,3]$ by exhibiting an explicit $\delta$ in
terms of $\varepsilon$.

## Challenge

**34.** Let $f$ be continuous on $[0,1]$ with $f(0)=f(1)$. Prove that there exists $x\in\left[0,\frac12\right]$
with
$$
f(x)=f\left(x+\frac12\right).
$$

**35.** Prove that a continuous injective function on an interval is strictly monotone. (You may use
the intermediate value theorem.)

**36.** Let $f$ be continuous on $[a,b]$ and suppose that $f(x)\in\mathbb{Q}$ for every $x\in[a,b]$.
Prove that $f$ is constant.
