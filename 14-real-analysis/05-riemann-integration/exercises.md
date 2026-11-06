# Riemann Integration — Exercises

> [Riemann Integration](README.md) · 36 problems · Beginner → Challenge · Solutions: [solutions.md](solutions.md)

Every problem is a proof unless it explicitly asks for a computation. For computations of integrals from
the definition, an upper and a lower sum with a certified gap is a complete answer; a value obtained from
an antiderivative alone is not. You may use anything proved in the [tutorial](README.md), but not results
from later topics. Do not open [solutions.md](solutions.md) before writing an attempt.

Notation: $P, Q$ are partitions of the interval under discussion, $L(f,P)$ and $U(f,P)$ are the lower and
upper Darboux sums, $\omega(f,I) = \sup_I f - \inf_I f$, and $\mathcal{R}[a,b]$ is the set of Riemann
integrable functions on $[a,b]$.

## Beginner

**1.** *(§7.2)* Let $f(x) = 2x$ on $[0,1]$ and let

$$
P = \left\{0, \tfrac12, 1\right\}, \qquad Q = \left\{0, \tfrac14, \tfrac12, \tfrac34, 1\right\}.
$$

Compute $L(f,P)$, $U(f,P)$, $L(f,Q)$, $U(f,Q)$ and verify that $L(f,P) \le L(f,Q) \le U(f,Q) \le U(f,P)$.

**2.** *(§7.2, §7.4)* Let $f(x) = x^2$ on $[0,2]$ and $P = \{0,1,2\}$. Compute $L(f,P)$ and $U(f,P)$.
Taking $\int_0^2 x^2\,dx = \tfrac83$ as known, verify that $L(f,P) \le \int_0^2 x^2\,dx \le U(f,P)$. Is $P$
good enough to certify integrability by the Riemann criterion with $\varepsilon = 1$? Explain.

**3.** *(§7.4)* Let $f(x) = c$ for all $x \in [a,b]$. Prove from Definitions 5.3 and 5.5 that
$f \in \mathcal{R}[a,b]$ and $\int_a^b f = c(b-a)$.

**4.** *(§7.9)* Let $f$ be bounded on $[a,b]$ with $m = \inf_{[a,b]} f$ and $M = \sup_{[a,b]} f$. Prove that
for every partition $P$,

$$
m(b-a) \le L(f,P) \le U(f,P) \le M(b-a),
$$

and deduce that $m(b-a) \le \underline{\int_a^b} f \le \overline{\int_a^b} f \le M(b-a)$.

**5.** *(§7.4, §7.14)* Using the uniform partition $P_n$ of $[0,1]$ into $n$ equal parts and right-hand
endpoint tags $t_i = x_i$, compute $S(f,P_n,(t_i))$ for $f(x) = 1 + 3x$, show that it converges, and
conclude $\int_0^1 (1+3x)\,dx = \tfrac52$. Confirm the value with Theorem 7.21.

**6.** *(§7.4)* For $f(x) = x$ on $[0,2]$ and the uniform partition $P_n$ into $n$ equal parts, compute
$L(f,P_n)$ and $U(f,P_n)$, verify $U - L \to 0$, and determine $\int_0^2 x\,dx$.

**7.** *(§5, §7.10)* The conventions are $\int_a^a f = 0$ and $\int_b^a f = -\int_a^b f$. Check that the
identity $\int_a^b f = \int_a^c f + \int_c^b f$ holds (for integrable $f$) when $c = a$ and when $c = b$,
and explain why the conventions were chosen this way.

**8.** *(§7.19)* Let $D$ be Dirichlet's function on $[0,2]$: $D(x)=1$ for rational $x$ and $D(x)=0$
otherwise. Determine $\underline{\int_0^2} D$ and $\overline{\int_0^2} D$, and decide whether $D$ is
integrable.

**9.** *(§7.8)* Let $f \in \mathcal{R}[a,b]$. Prove from the definitions that $-f \in \mathcal{R}[a,b]$ and
$\int_a^b (-f) = -\int_a^b f$. You may use, but must state and prove, the facts $\sup_I(-g) = -\inf_I g$
and $\inf_I(-g) = -\sup_I g$ for a bounded $g$.

**10.** *(§7.15)* Compute $\int_0^1 (x+1)^2\,dx$ using Theorem 7.21, naming the antiderivative and
verifying each hypothesis of the theorem. Then check the answer by expanding $(x+1)^2$ and integrating
term by term with Theorem 7.10 and Theorem 7.11.

## Intermediate

**11.** *(§7.8)* Let $f \in \mathcal{R}[a,b]$ and $c \in \mathbb{R}$. Prove that $f + c \in \mathcal{R}[a,b]$
and $\int_a^b (f+c) = \int_a^b f + c(b-a)$, by a direct $\varepsilon$-argument on Darboux sums. (Do not
quote Theorem 7.11.)

**12.** *(§7.9)* Let $f, g \in \mathcal{R}[a,b]$ with $f(x) \le g(x)$ for all $x$. Prove
$\int_a^b f \le \int_a^b g$ directly from the definition of the integral as a supremum, without quoting
Theorem 7.12.

**13.** *(§7.10)* Let $f \in \mathcal{R}[a,b]$ and let $[u,v] \subseteq [a,b]$. Prove directly from the
Riemann criterion that $f \in \mathcal{R}[u,v]$. (Do not quote Theorem 7.13.)

**14.** *(§7.9, §7.11)* Let $f \in \mathcal{R}[a,b]$ with $f \ge 0$ and $\int_a^b f = 0$. Prove that
$f(x) = 0$ at every point $x \in [a,b]$ at which $f$ is continuous.

**15.** *(§7.19, §7.18)* Let $h:[0,1]\to\mathbb{R}$ be defined by $h(x) = 1$ if $x = 1/n$ for some
$n \in \mathbb{N}$, and $h(x) = 0$ otherwise. Prove that $h \in \mathcal{R}[0,1]$ and $\int_0^1 h = 0$,
by constructing a partition for each $\varepsilon > 0$.

**16.** *(§7.13, §7.18)* Define $g:[0,1]\to\mathbb{R}$ by $g(0) = 0$ and $g(x) = 1/x$ for $0 < x \le 1$.
Prove that $g$ is not Riemann integrable on $[0,1]$, in two ways: (a) from Proposition 7.18, and (b) by
exhibiting tags whose Riemann sums are arbitrarily large for every mesh.

**17.** *(§7.19)* Let $f \in \mathcal{R}[a,b]$ and let $g$ agree with $f$ except at finitely many points of
$[a,b]$. Prove that $g \in \mathcal{R}[a,b]$ and $\int_a^b g = \int_a^b f$.

**18.** *(§7.9, §7.11)* Let $f \in \mathcal{R}[a,b]$ with $f \ge 0$. Prove that $\sqrt f \in \mathcal{R}[a,b]$,
using the inequality $\lvert \sqrt s - \sqrt t\rvert \le \sqrt{\lvert s - t\rvert}$ for $s,t \ge 0$.

**19.** *(§7.12)* **(a)** Let $f(x) = 4 - x^2$ on $[0,2]$. Compute $\int_0^2 f$ and find every $c \in [0,2]$
with $f(c)$ equal to the average value of $f$. **(b)** Show that the conclusion of Theorem 7.16 fails for
the step function $f = \mathbf{1}_{[0,1/3]}$ on $[0,1]$.

**20.** *(§7.4)* Let $f \in \mathcal{R}[a,b]$ and let $c \in [a,b]$. Prove that for every $\varepsilon>0$
there is a partition $P$ of $[a,b]$ with $c \in P$ and $U(f,P) - L(f,P) < \varepsilon$.

## Advanced

**21.** *(§7.6, §7.5)* Prove that the uniform limit of a sequence of step functions on $[a,b]$ is Riemann
integrable, and deduce that every continuous function on $[a,b]$ is Riemann integrable by approximating it
uniformly by step functions. (This gives a second proof of Theorem 7.8.)

**22.** *(§7.7)* **(a)** Prove the decreasing case of Theorem 7.9 directly, with a uniform partition.
**(b)** For a non-decreasing $f$ on $[a,b]$ and the uniform partition $P_n$ into $n$ parts, prove
$U(f,P_n) - L(f,P_n) = \frac{b-a}{n}\bigl(f(b) - f(a)\bigr)$. **(c)** Give an example of a non-decreasing
function on $[0,1]$ that is discontinuous at infinitely many points and explain why **(b)** still applies
to it.

**23.** *(§7.10)* Prove Theorem 7.13(2) in full: if $a<c<b$ and $f \in \mathcal{R}[a,c] \cap \mathcal{R}[c,b]$,
then $f \in \mathcal{R}[a,b]$ and $\int_a^b f = \int_a^c f + \int_c^b f$. Give all details of the
partition-splitting argument.

**24.** *(§7.14)* **(a)** Prove Theorem 7.20 for $x_0 \in (a,b)$ and for the endpoints. **(b)** Let $f$ be
the step function of Example 9.3 on $[0,2]$; compute $F(x) = \int_0^x f$ explicitly and show that $F$ is
continuous but not differentiable at $x = 1$. **(c)** Prove that $F$ is Lipschitz when $f$ is bounded.

**25.** *(§7.17)* Prove the substitution theorem under the weaker hypothesis: $\varphi:[a,b]\to\mathbb{R}$
is differentiable with $\varphi'$ Riemann integrable on $[a,b]$, and $f$ is continuous on an interval
containing $\varphi([a,b])$. Conclude
$\int_a^b f(\varphi(t))\varphi'(t)\,dt = \int_{\varphi(a)}^{\varphi(b)} f(u)\,du$.

**26.** *(§7.16)* Prove integration by parts in the following form: if $f, g$ are differentiable on
$[a,b]$ with $f', g' \in \mathcal{R}[a,b]$, then $f'g$ and $fg'$ are integrable and

$$
\int_a^b f g' = f(b)g(b) - f(a)g(a) - \int_a^b f' g .
$$

**27.** *(§7.6, §7.11)* Let $f \in \mathcal{R}[a,b]$ and let $g:\mathbb{R}\to\mathbb{R}$ be continuous.
Prove that $g \circ f \in \mathcal{R}[a,b]$.

**28.** *(§7.11)* Let $f \in \mathcal{R}[a,b]$ and suppose there is $m>0$ with $f(x) \ge m$ for all $x$.
Prove that $1/f \in \mathcal{R}[a,b]$.

**29.** *(§7.12)* **(a)** Prove Theorem 7.17 (weighted mean value theorem). **(b)** Deduce that if
$f:[a,b]\to[0,\infty)$ is continuous and $\int_a^b f = 0$, then $f \equiv 0$. **(c)** Show by example that
**(b)** fails without continuity.

**30.** *(§7.20)* **(a)** Prove that if $f_n \in \mathcal{R}[a,b]$ and $f_n \to f$ uniformly, then
$\int_a^b \lvert f - f_n\rvert \to 0$. **(b)** Show that $\int_a^b \lvert f - f_n\rvert \to 0$ does not
imply uniform convergence, using $f_n(x) = x^n$ on $[0,1]$ and $f = 0$.

## Challenge

**31.** *(§7.4, §7.5)* Prove the **mesh form** of the Riemann criterion: a bounded $f$ on $[a,b]$ is
integrable if and only if for every $\varepsilon>0$ there is $\delta>0$ such that every partition $P$ with
$\lVert P\rVert < \delta$ satisfies $U(f,P) - L(f,P) < \varepsilon$. (One direction is Lemma 7.6; the
other needs care.)

**32.** *(§7.5, §7.19)* Prove that a bounded $f$ on $[a,b]$ is Riemann integrable if and only if there are
sequences of step functions $(s_k)$ and $(t_k)$ with $s_k \le f \le t_k$ on $[a,b]$ for every $k$ and
$\int_a^b (t_k - s_k) \to 0$.

**33.** *(§7.20)* For $n \in \mathbb{N}$ let $f_n:[0,1]\to\mathbb{R}$ be $f_n(x) = n$ for
$x \in (0, 1/n)$ and $f_n(x) = 0$ otherwise. Prove that each $f_n \in \mathcal{R}[0,1]$,
$\int_0^1 f_n = 1$ for every $n$, and $f_n(x) \to 0$ for every $x \in [0,1]$, yet
$\int_0^1 f_n \not\to 0$. Explain which hypothesis of Theorem 7.30 fails.

**34.** *(§7.18)* Prove Riemann's oscillation criterion: a bounded $f$ on $[a,b]$ is integrable if and only
if for all $\varepsilon>0$ and $\eta>0$ there is a partition $P$ such that the total length of the
subintervals $I_i$ of $P$ with $\omega(f,I_i) \ge \varepsilon$ is less than $\eta$.

**35.** *(§7.15, §7.13)* Define $F:[-1,1]\to\mathbb{R}$ by $F(0)=0$ and $F(x) = x^2\sin(1/x^2)$ for
$x \ne 0$. **(a)** Prove that $F$ is differentiable everywhere and compute $F'(x)$ for $x \ne 0$.
**(b)** Prove that $F'$ is unbounded on $[-1,1]$, hence not Riemann integrable. **(c)** Explain why
Theorem 7.21 cannot be applied on $[-1,1]$ and what statement fails.

**36.** *(§7.6, §7.20)* Prove that if $f \in \mathcal{R}[a,b]$ and $\varepsilon>0$, there is a continuous
$h$ on $[a,b]$ with

$$
\int_a^b \lvert f - h\rvert < \varepsilon .
$$

Explain why the corresponding statement with $\sup_{[a,b]}\lvert f - h\rvert < \varepsilon$ is false for
some integrable $f$.
