# Continuity and Limits of Functions — Solutions

> [Tutorial](README.md) · [Exercises](exercises.md) · 36 complete solutions

Every solution below is complete: the quantifier choices are displayed, every use of a theorem is
named, and the algebraic steps are shown. Where a problem admits a second natural approach, the
alternative is indicated at the end.

Throughout, $\lvert\sin t\rvert \le 1$, $\lvert \sin t\rvert \le \lvert t\rvert$ and $\cos(\pi/2) = 0$
are used without comment, as permitted in the problem set.

## Beginner

**1.**

We must show: for every $\varepsilon > 0$ there is $\delta > 0$ such that $0 < \lvert x-1\rvert < \delta$
implies $\lvert (5x-2) - 3\rvert < \varepsilon$.

**Scratch work.** $\lvert (5x-2) - 3\rvert = \lvert 5x - 5\rvert = 5\lvert x - 1\rvert$. We need
$5\lvert x-1\rvert < \varepsilon$, i.e. $\lvert x-1\rvert < \varepsilon/5$.

**Proof.** Let $\varepsilon > 0$ and set $\delta := \varepsilon/5$. For every $x \in \mathbb{R}$ with
$0 < \lvert x-1\rvert < \delta$,
$$
\lvert (5x-2) - 3\rvert = 5\lvert x - 1\rvert < 5 \cdot \frac{\varepsilon}{5} = \varepsilon .
$$
By Definition 5.2, $\lim_{x\to 1}(5x-2) = 3$. $\blacksquare$

*Remark.* The value $f(1) = 3$ was never used; the same $\delta$ proves that any function agreeing with
$5x-2$ except at $x = 1$ has limit $3$ there.

**2.**

Here $f(x) = x^2 + 3x$ and $f(-2) = 4 - 6 = -2$, so
$$
\lvert f(x) - (-2)\rvert = \lvert x^2 + 3x + 2\rvert = \lvert (x+2)(x+1)\rvert = \lvert x+2\rvert\,\lvert x+1\rvert .
$$
The factor $\lvert x+1\rvert$ must be bounded before the product can be made small.

**Bound the factor.** If $\lvert x+2\rvert < 1$ then $-3 < x < -1$, so $-2 < x + 1 < 0$ and hence
$\lvert x+1\rvert < 2$.

**Choose $\delta$.** Let $\varepsilon > 0$ and set $\delta := \min\{1, \varepsilon/2\}$. For
$0 < \lvert x+2\rvert < \delta$ we have both $\lvert x+2\rvert < 1$, hence $\lvert x+1\rvert < 2$, and
$\lvert x+2\rvert < \varepsilon/2$, hence
$$
\lvert f(x) - (-2)\rvert = \lvert x+2\rvert\,\lvert x+1\rvert < \frac{\varepsilon}{2}\cdot 2 = \varepsilon .
$$
Therefore $\lim_{x\to -2}(x^2+3x) = -2$. $\blacksquare$

*Why the restriction is not optional.* Without it, $\lvert x+1\rvert$ grows with $\lvert x\rvert$, and
no fixed $\delta$ could control the product; the condition $\delta \le 1$ is what converts a global
problem into a local one.

**3.**

Here $a = 2$, $L = 1/2$ and the domain is $\mathbb{R} \setminus \{0\}$. For $x \ne 0$,
$$
\left\lvert \frac1x - \frac12\right\rvert = \left\lvert \frac{2 - x}{2x}\right\rvert = \frac{\lvert x - 2\rvert}{2\lvert x\rvert} .
$$
**Bound the denominator away from $0$.** If $\lvert x - 2\rvert < 1$ then $1 < x < 3$, so $\lvert x\rvert > 1$
and therefore
$$
\left\lvert \frac1x - \frac12\right\rvert \le \frac{\lvert x-2\rvert}{2}.
$$
**Choose $\delta$.** Let $\varepsilon > 0$ and set $\delta := \min\{1, 2\varepsilon\}$. For
$0 < \lvert x-2\rvert < \delta$ the preliminary bound applies and
$$
\left\lvert \frac1x - \frac12\right\rvert \le \frac{\lvert x-2\rvert}{2} < \frac{2\varepsilon}{2} = \varepsilon .
$$
Hence $\lim_{x\to 2} 1/x = 1/2$. $\blacksquare$

*Pitfall.* Writing $\lvert 1/x - 1/2\rvert = \lvert x-2\rvert/(2\lvert x\rvert) \le \lvert x-2\rvert/2$
without justification is invalid near $x = 0$; the restriction $\delta \le 1$ is exactly what supplies
$\lvert x\rvert > 1$.

**4.**

The domain is $[0,\infty)$ and $9$ is an interior point of it. For $x \ge 0$ with $x \ne 9$, rationalise:
$$
\lvert \sqrt x - 3\rvert = \left\lvert \frac{x - 9}{\sqrt x + 3}\right\rvert = \frac{\lvert x-9\rvert}{\sqrt x + 3} \le \frac{\lvert x-9\rvert}{3},
$$
because $\sqrt x \ge 0$ forces $\sqrt x + 3 \ge 3$. Let $\varepsilon > 0$ and set $\delta := 3\varepsilon$.
For $x \in [0,\infty)$ with $0 < \lvert x-9\rvert < \delta$,
$$
\lvert \sqrt x - 3\rvert \le \frac{\lvert x-9\rvert}{3} < \frac{3\varepsilon}{3} = \varepsilon .
$$
Hence $\lim_{x\to 9}\sqrt x = 3$. $\blacksquare$

*Remark.* The estimate $\sqrt x + 3 \ge 3$ degrades as the base point shrinks; at $a = 0$ the same
computation gives $\lvert\sqrt x - 0\rvert \le \sqrt{\lvert x\rvert}$, and $\delta = \varepsilon^2$ is
required. Uniformity over the base point is precisely what fails for the *reciprocal* of this estimate,
as Solution 27 shows.

**5.**

For $x \ne 0$, $\lvert \cos(1/x)\rvert \le 1$, hence
$$
0 \le \left\lvert x\cos\frac1x\right\rvert \le \lvert x\rvert .
$$
Let $g(x) := 0$ and $h(x) := \lvert x\rvert$. Both have limit $0$ at $0$: for $g$ any $\delta$ works, and
for $h$, given $\varepsilon > 0$ take $\delta := \varepsilon$, so that $0 < \lvert x\rvert < \delta$
gives $\lvert h(x) - 0\rvert = \lvert x\rvert < \varepsilon$. Since $g \le x\cos(1/x) \le h$ pointwise off
$0$, the squeeze theorem (Theorem 7.6) gives
$$
\lim_{x\to 0} x\cos\frac1x = 0 . \qquad \blacksquare
$$
*Direct alternative.* Given $\varepsilon > 0$, take $\delta := \varepsilon$; then
$\lvert x\cos(1/x) - 0\rvert \le \lvert x\rvert < \varepsilon$ for $0 < \lvert x\rvert < \delta$.

**6.**

Factor the difference of cubes: $x^3 - 8 = (x-2)(x^2 + 2x + 4)$. For $x \ne 2$,
$$
\frac{x^3-8}{x-2} = x^2 + 2x + 4 .
$$
The cancellation is legitimate because $x \ne 2$, and Definition 5.2 quantifies only over points with
$0 < \lvert x-2\rvert$. The right-hand side is a polynomial, hence continuous at $2$ by Corollary 7.11(a),
so
$$
\lim_{x\to 2}\frac{x^3-8}{x-2} = \lim_{x\to 2}(x^2+2x+4) = 2^2 + 2\cdot 2 + 4 = 12 .
$$
$\blacksquare$

*Why this is not circular.* We do not claim the original function is continuous at $2$ — it is not
defined there. We claim that off $2$ it agrees with a continuous function, and a limit depends only on
the punctured neighbourhood.

**7.**

For $x \in (0,1)$ we have $\lfloor x\rfloor = 0$, so the function is constant $0$ on that interval;
hence
$$
\lim_{x\to 1^-}\lfloor x\rfloor = 0 .
$$
Indeed, given $\varepsilon > 0$ take $\delta := 1$: for $1 - 1 < x < 1$ we have $\lfloor x\rfloor = 0$
and $\lvert 0 - 0\rvert = 0 < \varepsilon$.

For $x \in (1,2)$ we have $\lfloor x\rfloor = 1$, so similarly
$$
\lim_{x\to 1^+}\lfloor x\rfloor = 1 .
$$
The one-sided limits exist but are different. By Theorem 7.7 (contrapositive of the "only if" direction),
the two-sided limit $\lim_{x\to 1}\lfloor x\rfloor$ does **not** exist. $\blacksquare$

*Remark.* At a non-integer point $a$, $\lfloor x\rfloor$ is constant on a neighbourhood of $a$, hence
continuous there; at every integer it has a jump of size $1$. This is the model example of a jump
discontinuity (Section 7.10).

**8.**

The formula is a quotient whose denominator vanishes at $x = 4$, so the expression is undefined there.
But Definition 5.2 for the limit at $4$ quantifies only over $x$ with $0 < \lvert x-4\rvert$, i.e. over
points where the formula *is* defined. For such $x$,
$$
\frac{x^2-16}{x-4} = \frac{(x-4)(x+4)}{x-4} = x + 4 .
$$
The function $x \mapsto x+4$ is a polynomial, hence continuous at $4$, so
$$
\lim_{x\to 4}\frac{x^2-16}{x-4} = \lim_{x\to 4}(x+4) = 8 .
$$
$\blacksquare$

The graph is the line $y = x+4$ with the single point $(4,8)$ removed; the limit is the height of the
missing point, and defining $f(4) := 8$ fills the hole continuously.

**9.**

Write
$$
f(x) = \frac{(x-1)(x+1)}{(x-2)(x+2)} .
$$
$f$ is a quotient of polynomials. By Theorem 7.9 and Corollary 7.11(b), it is continuous at every point
where the denominator is nonzero, i.e. on $\mathbb{R} \setminus \{-2, 2\}$; and it is undefined at
$\pm 2$, so it cannot be continuous there.

*At $x = 1$.* The limit is obtained by substituting, since numerator and denominator are polynomials
and the denominator does not vanish:
$$
\lim_{x\to 1} f(x) = \frac{(1-1)(1+1)}{(1-2)(1+2)} = \frac{0}{-3} = 0 .
$$
Hence $f$ has a removable discontinuity at $1$, and $\tilde f(1) := 0$ extends $f$ continuously to $1$
(Definition 5.4 is met because the limit exists and equals the assigned value).

*At $x = -1$.* Numerator and denominator are polynomials and the denominator does not vanish, so
substitution is valid:
$$
\lim_{x\to -1} f(x) = \frac{(-1-1)(-1+1)}{(-1-2)(-1+2)} = \frac{(-2)(0)}{(-3)(1)} = 0 ,
$$
and $\tilde f(-1) := 0$ is a continuous extension.

*At $x = 2$.* Here $\lvert f(x)\rvert \to +\infty$: for $x$ near $2$ with $x \ne 2$, the numerator tends
to $3 > 0$ and $\lvert x+2\rvert$ tends to $4$, while $\lvert x - 2\rvert \to 0$, so
$$
\lvert f(x)\rvert = \frac{\lvert x^2-1\rvert}{\lvert x-2\rvert\,\lvert x+2\rvert} \ge \frac{2}{5\lvert x-2\rvert}
$$
for $x$ close enough to $2$ (using $\lvert x^2 - 1\rvert \ge 2$ and $\lvert x+2\rvert \le 5$ near $2$).
Suppose a continuous extension $F$ existed at $2$. Then by Lemma 7.2 (applied to $f$ with limit $F(2)$)
there would be $\delta > 0$ and $M$ with $\lvert f(x)\rvert \le M$ for $0 < \lvert x-2\rvert < \delta$,
contradicting the lower bound above (which exceeds $M$ for $x$ close enough to $2$). So no continuous
extension exists at $2$. The same argument, with $\lvert x - (-2)\rvert$ in the denominator, shows no
continuous extension at $-2$. $\blacksquare$

Conclusion: $f$ is continuous exactly on $\mathbb{R}\setminus\{-2,2\}$; it extends continuously to
$x = \pm 1$ (with value $0$) and not to $x = \pm 2$.

**10.**

Let $a \in \mathbb{R}$. By the reverse triangle inequality,
$$
\bigl\lvert\,\lvert x - 3\rvert - \lvert a - 3\rvert\,\bigr\rvert \le \lvert (x-3) - (a-3)\rvert = \lvert x - a\rvert .
$$
Given $\varepsilon > 0$, take $\delta := \varepsilon$. Then $\lvert x - a\rvert < \delta$ implies
$\lvert f(x) - f(a)\rvert < \varepsilon$. Hence $f$ is continuous at $a$, and since $a$ was arbitrary, on
$\mathbb{R}$. $\blacksquare$

*Alternative.* $f = \lvert\cdot\rvert \circ (x \mapsto x-3)$; the identity is continuous, translations of
continuous functions are continuous, and $\lvert\cdot\rvert$ is continuous by Corollary 7.11(c), so
Theorem 7.10 applies.

**11.**

We build $p$ from the two basic continuous functions $x \mapsto x$ and $x \mapsto c$ (constants).
Let $f(x) := x$; then $\lvert f(x) - f(a)\rvert = \lvert x-a\rvert$, so $f$ is continuous at every $a$
with $\delta = \varepsilon$. Constants are continuous with any $\delta$.

* $x \mapsto x^2 = x \cdot x$ is continuous by Theorem 7.9 (product).
* $x \mapsto x^3 = x^2\cdot x$ is continuous by Theorem 7.9 again.
* $x \mapsto 2x^3$ is continuous by Theorem 7.9 (constant multiple).
* $x \mapsto -5x$ is continuous by Theorem 7.9 (constant multiple).
* $p = 2x^3 + (-5x) + 1$ is continuous by Theorem 7.9 (sum), applied twice.

Hence $p$ is continuous at every point of $\mathbb{R}$. $\blacksquare$

The same induction on degree shows that every polynomial is continuous; this is Corollary 7.11(a), and
the point of the exercise is to see the induction performed once explicitly.

**12.**

Let $u(x) := x^2 + 1$. By Solution 11 (or Corollary 7.11(a)), $u$ is a polynomial, hence continuous on
$\mathbb{R}$. Also $u(x) \ge 1 > 0$ for all $x$, so $u[\mathbb{R}] \subseteq [0,\infty)$, which is the
domain of $\sqrt{\cdot}$. By Corollary 7.11(d), $\sqrt{\cdot}$ is continuous on $[0,\infty)$, in
particular at every point $u(a)$. Theorem 7.10 (continuity of a composition) now gives that
$f = \sqrt{\cdot} \circ u$ is continuous at every $a \in \mathbb{R}$. $\blacksquare$

*Direct check at a point $a$.* $\lvert f(x)-f(a)\rvert = \lvert u(x)-u(a)\rvert/(\sqrt{u(x)}+\sqrt{u(a)})
\le \lvert u(x)-u(a)\rvert/\sqrt{u(a)}$, and $u$ is continuous; this is the same argument unwound.

## Intermediate

**13.**

**The limit of $\lvert f\rvert$.** Let $\varepsilon > 0$. By hypothesis there is $\delta > 0$ such that
$0 < \lvert x-a\rvert < \delta$ implies $\lvert f(x)-L\rvert < \varepsilon$. For such $x$, the reverse
triangle inequality gives
$$
\bigl\lvert\,\lvert f(x)\rvert - \lvert L\rvert\,\bigr\rvert \le \lvert f(x) - L\rvert < \varepsilon .
$$
Hence $\lim_{x\to a}\lvert f(x)\rvert = \lvert L\rvert$. $\blacksquare$

**The converse fails.** Define
$$
f(x) := \begin{cases} 1, & x \ge 0,\\ -1, & x < 0,\end{cases}
\qquad a := 0 .
$$
Then $\lvert f(x)\rvert = 1$ for all $x$, so $\lim_{x\to 0}\lvert f(x)\rvert = 1 = \lvert 1\rvert$. But
$\lim_{x\to 0} f(x)$ does not exist: the sequences $x_n = 1/n$ and $y_n = -1/n$ both tend to $0$ with
$f(x_n) = 1 \to 1$ and $f(y_n) = -1 \to -1$, and Corollary 7.4 applies because $1 \ne -1$.
$\blacksquare$

*Moral.* Taking absolute values destroys sign information, and a limit can fail purely by sign
oscillation. What *is* true is that $f \to L$ implies $\lvert f\rvert \to \lvert L\rvert$, and that
$\lvert f\rvert \to 0$ implies $f \to 0$ (because $\lvert f(x) - 0\rvert = \lvert f(x)\rvert$).

**14.**

**(a)** Suppose, for contradiction, that $L > M$. Put $\varepsilon := (L-M)/3 > 0$. By the two limit
statements there are $\delta_1, \delta_2 > 0$ with
$$
0<\lvert x-a\rvert<\delta_1 \Rightarrow \lvert f(x)-L\rvert<\varepsilon,
\qquad
0<\lvert x-a\rvert<\delta_2 \Rightarrow \lvert g(x)-M\rvert<\varepsilon .
$$
Let $\delta := \min\{\delta_0,\delta_1,\delta_2\}$. Since $a$ is a cluster point of $A$, there is
$x \in A$ with $0 < \lvert x-a\rvert < \delta$. For this $x$,
$$
f(x) > L - \varepsilon = \frac{2L+M}{3} > \frac{L+2M}{3} = M + \varepsilon > g(x),
$$
contradicting $f(x) \le g(x)$. Hence $L \le M$. $\blacksquare$

**(b)** The hypothesis says $-g(x) \le f(x) - L \le g(x)$ for all $x$ near $a$. By Theorem 7.5(b),
$\lim_{x\to a}(-g(x)) = 0$ and $\lim_{x\to a} g(x) = 0$. The squeeze theorem (Theorem 7.6) applied to
the triple $-g \le f - L \le g$ gives $\lim_{x\to a}\bigl(f(x)-L\bigr) = 0$. By Theorem 7.5(a) with the
constant function $L$,
$$
\lim_{x\to a} f(x) = \lim_{x\to a}\bigl[(f(x)-L) + L\bigr] = 0 + L = L . \qquad \blacksquare
$$

*Remark.* Part (a) is the function version of "limits preserve weak inequalities"; strict inequalities
do **not** survive: $f(x) = 0 < g(x) = \lvert x\rvert$ for $x \ne 0$, yet both limits at $0$ are $0$.

**15.**

We exhibit two sequences tending to $0$ whose images have different limits, and invoke Corollary 7.4.

Let $x_n := \dfrac{1}{2n\pi}$ and $y_n := \dfrac{1}{2n\pi + \pi/2}$. Both are nonzero for $n \ge 1$,
both tend to $0$ (their denominators tend to $+\infty$), and
$$
\sin\frac{1}{x_n} = \sin(2n\pi) = 0,
\qquad
\sin\frac{1}{y_n} = \sin\Bigl(2n\pi + \frac{\pi}{2}\Bigr) = 1 .
$$
Hence $f(x_n) \to 0$ and $f(y_n) \to 1$. Since $0 \ne 1$, Corollary 7.4 shows that
$\lim_{x\to 0}\sin(1/x)$ does not exist. $\blacksquare$

*Alternative.* The images of the two sequences are constant, so the sequential criterion gives
immediately that no single $L$ can serve both. A direct $\varepsilon$-$\delta$ proof of failure would
have to produce, for every $\delta$, a point where $\lvert\sin(1/x)\rvert \ge 1$; the sequence
construction is exactly the choice of such points.

**16.**

**Right limit.** For $x > 0$, $\lvert x\rvert = x$, so $f(x) = x/x = 1$. The function is constant $1$ on
$(0,\infty)$, hence $\lim_{x\to 0^+} f(x) = 1$: given $\varepsilon > 0$, any $\delta > 0$ works because
$\lvert f(x)-1\rvert = 0 < \varepsilon$.

**Left limit.** For $x < 0$, $\lvert x\rvert = -x$, so $f(x) = x/(-x) = -1$, and
$\lim_{x\to 0^-} f(x) = -1$.

**Two-sided limit.** The one-sided limits exist but $1 \ne -1$. By Theorem 7.7, $\lim_{x\to 0} f(x)$
does not exist. $\blacksquare$

*Consistency check with the sequential criterion.* $1/n \to 0$ has images $1$; $-1/n \to 0$ has images
$-1$; Corollary 7.4 gives the same conclusion.

**17.**

Suppose, for contradiction, that $f$ takes both a positive and a negative value on $[a,b]$. Then there
are $u, v \in [a,b]$ with $f(u) > 0 > f(v)$. If $u < v$, apply the intermediate value theorem
(Theorem 7.12) to $f$ on $[u,v]$ with $y = 0$: since $f(v) < 0 < f(u)$, the theorem (in the form for
$f(u) > f(v)$, obtained by applying it to $-f$) provides $c \in (u,v)$ with $f(c) = 0$. If $v < u$, the
same argument on $[v,u]$ applies. In either case there is a point of $[a,b]$ where $f$ vanishes,
contradicting the hypothesis.

Therefore $f$ cannot take both signs; since $f$ never vanishes, it takes exactly one sign, and it is
either everywhere positive or everywhere negative on $[a,b]$. $\blacksquare$

*Remark.* The interval is essential: $f(x) = 1/x$ is continuous and never zero on $\mathbb{R}\setminus\{0\}$
but takes both signs there, because the domain is not an interval.

**18.**

Let $g(x) := x - \cos x$. The functions $x \mapsto x$ and $\cos$ are continuous, so $g$ is continuous on
$[0,\pi/2]$ by Theorem 7.9. Evaluate:
$$
g(0) = 0 - \cos 0 = 0 - 1 = -1 < 0,
\qquad
g\Bigl(\frac{\pi}{2}\Bigr) = \frac{\pi}{2} - \cos\frac{\pi}{2} = \frac{\pi}{2} - 0 = \frac{\pi}{2} > 0 .
$$
By the intermediate value theorem (Theorem 7.12) applied on $[0,\pi/2]$ with $y = 0$, there is
$c \in (0,\pi/2)$ with $g(c) = 0$, i.e. $c = \cos c$. $\blacksquare$

*Remark.* The solution is not unique a priori — the IVT does not claim uniqueness — and indeed the
equation $x = \cos x$ has exactly one solution, but proving that needs monotonicity of $x - \cos x$,
which is a differentiation argument and belongs to the next topic.

**19.**

Suppose $f$ is not constant. Then there are $x, y \in [0,1]$ with $f(x) \ne f(y)$; relabel so that
$f(x) < f(y)$. Choose an irrational $t$ with
$$
f(x) < t < f(y),
$$
which is possible by the density of the irrationals in $\mathbb{R}$ (Proposition 7.27 of
[The Real Numbers and Completeness](../01-real-numbers-and-completeness/README.md)). The function $f$
is continuous on the interval with endpoints $x$ and $y$, and $t$ lies strictly between the endpoint
values, so the intermediate value theorem (Theorem 7.12, applied on $[x,y]$ if $x<y$ and on $[y,x]$
otherwise, with $-f$ if necessary) gives $c$ between $x$ and $y$ with $f(c) = t$. But $t$ is irrational
and the hypothesis says $f(c) \in \mathbb{Q}$; contradiction.

Hence $f$ is constant. $\blacksquare$

*Remark.* The same argument shows that a continuous function on an interval whose values lie in any
"gap-free-free" set with no intermediate points — for instance $\mathbb{Z}$ — is constant.

**20.**

Define
$$
g(x) := f\Bigl(x + \frac12\Bigr) - f(x), \qquad x \in \Bigl[0, \frac12\Bigr] .
$$
This is well defined because $x + \frac12 \in [\frac12, 1] \subseteq [0,1]$. It is continuous on
$[0,\frac12]$: $x \mapsto x + \frac12$ is continuous, $f$ is continuous on $[0,1]$, so $f(x+\frac12)$ is a
composition of continuous functions (Theorem 7.10), and the difference of continuous functions is
continuous (Theorem 7.9).

Evaluate at the endpoints:
$$
g(0) = f\Bigl(\frac12\Bigr) - f(0) = f\Bigl(\frac12\Bigr),
\qquad
g\Bigl(\frac12\Bigr) = f(1) - f\Bigl(\frac12\Bigr) = -f\Bigl(\frac12\Bigr).
$$
If $f(\frac12) = 0$, take $c := 0$: then $f(0) = 0 = f(\frac12) = f(c + \frac12)$.

Otherwise $g(0)$ and $g(\frac12)$ are nonzero with opposite signs. By the intermediate value theorem on
$[0,\frac12]$ there is $c \in (0,\frac12)$ with $g(c) = 0$, i.e. $f(c) = f(c+\frac12)$.
$\blacksquare$

*Remark.* The hypothesis $f(0) = f(1) = 0$ was used only to make $g$ change sign; any continuous $f$
with $f(0) = f(1)$ satisfies the same conclusion.

**21.**

We must find, for each $\varepsilon > 0$, a number $M$ such that $x > M$ implies
$$
\left\lvert \frac{2x+1}{x-3} - 2 \right\rvert < \varepsilon .
$$
Compute
$$
\frac{2x+1}{x-3} - 2 = \frac{2x+1 - 2(x-3)}{x-3} = \frac{2x+1-2x+6}{x-3} = \frac{7}{x-3} .
$$
For $x > 6$ we have $x - 3 > x/2$, hence
$$
\left\lvert \frac{2x+1}{x-3} - 2 \right\rvert = \frac{7}{x-3} < \frac{14}{x} .
$$
Choose
$$
M := \max\Bigl\{6, \frac{14}{\varepsilon}\Bigr\} .
$$
Then for $x > M$ we have $x > 6$, so the bound applies, and $x > 14/\varepsilon$, so the expression is
$< \varepsilon$. By Definition 7.21, $\lim_{x\to\infty}\dfrac{2x+1}{x-3} = 2$. $\blacksquare$

*Remark.* The constant $6$ is not special; any $\alpha > 3$ would do, at the cost of replacing $14$ by
an adjusted constant. The structure — "make $x$ large enough that the denominator is comparable to $x$,
then make $x$ large enough for the tolerance" — is the same as the two-step device in Solution 2.

**22.**

**Continuity at $0$.** For $x \ne 0$,
$$
\lvert f(x) - f(0)\rvert = \left\lvert x^2\sin\frac1x\right\rvert \le x^2 = \lvert x\rvert^2 .
$$
Given $\varepsilon > 0$, choose $\delta := \sqrt{\varepsilon}$ (or $\min\{1,\varepsilon\}$, both work).
Then $0 < \lvert x\rvert < \delta$ gives $\lvert f(x)\rvert \le x^2 < \varepsilon$; and at $x = 0$ the
difference is $0$. Hence $f$ is continuous at $0$. Continuity at every $x \ne 0$ follows from
Theorem 7.9: $x^2$ is continuous, $1/x$ is continuous there, $\sin$ is continuous, and a product and
composition of continuous functions is continuous.

**Unboundedness of $1/f$ near $0$.** Put
$$
x_n := \frac{1}{n\pi + \frac1n}, \qquad n \ge 2 .
$$
Then $x_n > 0$ and $x_n \to 0$. Moreover
$$
\sin\frac{1}{x_n} = \sin\Bigl(n\pi + \frac1n\Bigr) = (-1)^n \sin\frac1n \ne 0,
$$
because $0 < 1/n < \pi$. Hence $f(x_n) \ne 0$ and
$$
\left\lvert \frac{1}{f(x_n)}\right\rvert = \frac{1}{x_n^2\,\lvert\sin(1/x_n)\rvert}
= \frac{(n\pi + 1/n)^2}{\sin(1/n)} .
$$
Since $\sin(1/n) \le 1$ and $(n\pi+1/n)^2 \to \infty$, this tends to $+\infty$. Therefore $1/f$ is
unbounded on every interval $(-\delta,\delta)$: given $\delta > 0$, choose $n$ with $x_n < \delta$, then
$\lvert 1/f(x_n)\rvert$ exceeds any prescribed bound for large $n$. $\blacksquare$

*Remark.* $f$ itself is bounded by $1$ near $0$; it is the *relative* smallness of $f$ that makes the
reciprocal blow up. This is the phenomenon behind ill-conditioned division and behind the failure of
uniform continuity of $1/x$ near $0$ (Solution 26).

## Advanced

**23.**

Let
$$
p(x) = a_nx^n + a_{n-1}x^{n-1} + \cdots + a_1x + a_0, \qquad a_n \ne 0,
$$
with $n$ odd. For $x \ne 0$ factor out $x^n$:
$$
p(x) = x^n\bigl(a_n + r(x)\bigr), \qquad r(x) := \frac{a_{n-1}}{x} + \frac{a_{n-2}}{x^2} + \cdots + \frac{a_0}{x^n} .
$$

**Step 1: $r(x)$ is small for large $\lvert x\rvert$.** Let $\eta := \lvert a_n\rvert/2 > 0$. Choose
$M \ge 1$ so large that
$$
\sum_{k=1}^{n} \frac{\lvert a_{n-k}\rvert}{M^k} < \eta .
$$
(This is possible because the left-hand side tends to $0$ as $M \to \infty$; explicitly, each term
decreases and only finitely many terms are involved.) For $\lvert x\rvert > M$,
$$
\lvert r(x)\rvert \le \sum_{k=1}^{n}\frac{\lvert a_{n-k}\rvert}{\lvert x\rvert^k} < \sum_{k=1}^{n}\frac{\lvert a_{n-k}\rvert}{M^k} < \eta = \frac{\lvert a_n\rvert}{2}.
$$
Consequently $a_n + r(x)$ has the sign of $a_n$, because it differs from $a_n$ by less than
$\lvert a_n\rvert/2$ in absolute value, and $\lvert a_n + r(x)\rvert \ge \lvert a_n\rvert/2 > 0$.

**Step 2: $p$ takes both signs.** If $x > M$, then $x^n > 0$, so
$$
\operatorname{sign} p(x) = \operatorname{sign}\bigl(a_n + r(x)\bigr) = \operatorname{sign} a_n .
$$
If $x < -M$, then $x^n < 0$ because $n$ is odd, so
$$
\operatorname{sign} p(x) = -\operatorname{sign} a_n .
$$
Take $X := M + 1$. Then $p(X)$ and $p(-X)$ are nonzero with opposite signs.

**Step 3: apply the IVT.** $p$ is a polynomial, hence continuous on $\mathbb{R}$ (Corollary 7.11(a)), so
it is continuous on the closed interval with endpoints $-X$ and $X$. The value $0$ lies strictly between
$p(-X)$ and $p(X)$, so Theorem 7.12 (applied to $p$ or to $-p$ according to the sign of $a_n$) gives
$c \in (-X, X)$ with $p(c) = 0$. $\blacksquare$

*Why oddness is essential.* For $p(x) = x^2 + 1$ (even degree) the two tails have the same sign, and no
root need exist. The algebraic content of the odd case is $x^n \to \pm\infty$ with opposite signs at the
two ends, which is exactly what Step 2 records.

**24.**

**One inclusion.** By definition of $m$ and $M$, $m \le f(x) \le M$ for every $x \in [a,b]$; hence
$f\bigl[[a,b]\bigr] \subseteq [m,M]$.

**The reverse inclusion.** Let $y \in [m,M]$. By the extreme value theorem there are $u, v \in [a,b]$
with $f(u) = m$ and $f(v) = M$. Since $m \le M$, two cases arise.

*If $y = m$*, then $y = f(u) \in f[[a,b]]$. *If $y = M$*, then $y = f(v) \in f[[a,b]]$.

*If $m < y < M$*, then $u \ne v$. If $u < v$, apply Theorem 7.12 to $f$ on $[u,v]$: $f(u) = m < y < M = f(v)$,
so there is $c \in (u,v)$ with $f(c) = y$. If $v < u$, apply Theorem 7.12 to $f$ on $[v,u]$ with the
roles of the endpoint values exchanged (equivalently, apply it to $-f$): again there is $c$ with
$f(c) = y$. In all cases $y \in f[[a,b]]$.

Hence $[m,M] \subseteq f[[a,b]]$, and the two inclusions give equality. $\blacksquare$

*Remark.* The result says that the image of a closed bounded interval under a continuous function is
again a closed bounded interval, and that its endpoints are the minimum and maximum. This is the
one-dimensional case of the statement "the continuous image of a compact connected set is compact and
connected".

**25.**

**Uniform continuity on $[0,2]$.** For $x, y \in [0,2]$,
$$
\lvert x^2 - y^2\rvert = \lvert x+y\rvert\,\lvert x-y\rvert \le 4\lvert x-y\rvert,
$$
because $0 \le x, y \le 2$ gives $0 \le x + y \le 4$. Given $\varepsilon > 0$, set
$\delta := \varepsilon/4$. Then $\lvert x-y\rvert < \delta$ implies $\lvert x^2-y^2\rvert \le 4\delta = \varepsilon$.
Since $\delta$ does not depend on $x$ or $y$, $x^2$ is uniformly continuous on $[0,2]$. $\blacksquare$

**Failure on $\mathbb{R}$.** Let
$$
x_n := n, \qquad y_n := n + \frac1n .
$$
Then $\lvert x_n - y_n\rvert = 1/n \to 0$, but
$$
\lvert x_n^2 - y_n^2\rvert = \lvert x_n + y_n\rvert\,\lvert x_n - y_n\rvert
= \Bigl(2n + \frac1n\Bigr)\frac1n = 2 + \frac{1}{n^2} \ge 2 .
$$
Take $\varepsilon := 2$ in Definition 5.6. For every $\delta > 0$ choose $n > 1/\delta$; then
$\lvert x_n - y_n\rvert < \delta$ while $\lvert x_n^2 - y_n^2\rvert \ge 2 = \varepsilon$. Hence no $\delta$
works for this $\varepsilon$, and $x^2$ is not uniformly continuous on $\mathbb{R}$. $\blacksquare$

*Diagnosis.* The bound $\lvert x+y\rvert \le 4$ used compactness of $[0,2]$; on $\mathbb{R}$ the factor
$\lvert x+y\rvert$ can be arbitrarily large while $\lvert x-y\rvert$ is small, and that is exactly what
the sequence pair exhibits.

**26.**

**Not uniformly continuous on $(0,1)$.** With
$$
x_n := \frac1n, \qquad y_n := \frac{1}{n+1},
$$
both lie in $(0,1)$ for $n \ge 1$, and
$$
\lvert x_n - y_n\rvert = \frac{1}{n} - \frac{1}{n+1} = \frac{1}{n(n+1)} \longrightarrow 0,
$$
while
$$
\lvert f(x_n) - f(y_n)\rvert = \lvert n - (n+1)\rvert = 1 .
$$
Taking $\varepsilon = 1$ in the negation of Definition 5.6, no $\delta > 0$ can work: for every $\delta$
choose $n > 1/\sqrt{\delta}$, then $\lvert x_n - y_n\rvert < \delta$ but the images differ by $1 \ge \varepsilon$.
Hence $1/x$ is not uniformly continuous on $(0,1)$. $\blacksquare$

**Uniformly continuous on $[1,\infty)$.** For $x, y \ge 1$,
$$
\left\lvert \frac1x - \frac1y \right\rvert = \frac{\lvert y - x\rvert}{xy} \le \lvert x - y\rvert,
$$
because $xy \ge 1$. Given $\varepsilon > 0$, take $\delta := \varepsilon$; then $\lvert x-y\rvert < \delta$
implies $\lvert 1/x - 1/y\rvert < \varepsilon$. The choice of $\delta$ is independent of the point, so
$1/x$ is uniformly continuous on $[1,\infty)$. $\blacksquare$

*Moral.* The same function, on two different sets. What changes is whether the set contains points where
the function's slope is unbounded *and* the points can approach each other while remaining in the set.

**27.**

For $x, y \ge 0$,
$$
\bigl\lvert\sqrt x - \sqrt y\bigr\rvert^2
= \bigl\lvert\sqrt x - \sqrt y\bigr\rvert\cdot\bigl\lvert\sqrt x - \sqrt y\bigr\rvert
\le \bigl\lvert\sqrt x - \sqrt y\bigr\rvert\bigl(\sqrt x + \sqrt y\bigr)
= \lvert x - y\rvert,
$$
where the inequality uses $\lvert\sqrt x - \sqrt y\rvert \le \sqrt x + \sqrt y$ (both terms are
nonnegative). Taking square roots,
$$
\bigl\lvert\sqrt x - \sqrt y\bigr\rvert \le \sqrt{\lvert x-y\rvert}.
$$
Given $\varepsilon > 0$, set $\delta := \varepsilon^2$. Then $\lvert x-y\rvert < \delta$ implies
$\lvert\sqrt x - \sqrt y\rvert < \sqrt{\varepsilon^2} = \varepsilon$. Hence $\sqrt{\cdot}$ is uniformly
continuous on $[0,\infty)$. $\blacksquare$

*Remark.* The estimate is sharp: for $y = 0$ and $x = \varepsilon^2$ the left side equals
$\varepsilon$, so no larger modulus of the form $C\lvert x-y\rvert^{\alpha}$ with $\alpha < 1/2$ works.
The function is not Lipschitz on $[0,\infty)$ because $\sqrt x/x = 1/\sqrt x \to \infty$ as $x \to 0^+$;
this is the example promised in Section 7.9.

**28.**

Let $\varepsilon > 0$. By uniform continuity there is $\delta > 0$ such that
$$
x, y \in (a,b), \ \lvert x-y\rvert < \delta \ \Rightarrow\ \lvert f(x)-f(y)\rvert < \varepsilon .
$$
Set $c := \min\{\delta/2, (b-a)/2\} > 0$ and define
$$
x_n := a + \frac{c}{n} \in (a,b), \qquad n \ge 2 .
$$
Then $x_n \to a$ and, for $m, n \ge N$,
$$
\lvert x_n - x_m\rvert = c\,\Bigl\lvert \frac1n - \frac1m\Bigr\rvert \le \frac{c}{N} \le \frac{\delta}{2} < \delta,
$$
so $\lvert f(x_n) - f(x_m)\rvert < \varepsilon$. Hence $(f(x_n))$ is a Cauchy sequence, and by Cauchy
completeness (Theorem 7.33 of [The Real Numbers and Completeness](../01-real-numbers-and-completeness/README.md))
it converges to some $L \in \mathbb{R}$.

**Claim: $\lim_{x\to a^+} f(x) = L$.** Let $\varepsilon > 0$ and let $\delta_1 > 0$ be the modulus
provided by uniform continuity for the tolerance $\varepsilon/2$. Choose $N$ so large that
$$
\frac{c}{N} < \delta_1 \qquad\text{and}\qquad \lvert f(x_N) - L\rvert < \frac{\varepsilon}{2}.
$$
For any $x \in (a,b)$ with $0 < x - a < \delta_1$ we have $x \in (a, a+\delta_1)$ and also
$x_N \in (a, a + c/N) \subseteq (a, a+\delta_1)$, hence $\lvert x - x_N\rvert < \delta_1$ and therefore
$$
\lvert f(x) - f(x_N)\rvert < \frac{\varepsilon}{2}, \qquad
\lvert f(x) - L\rvert \le \lvert f(x)-f(x_N)\rvert + \lvert f(x_N)-L\rvert < \varepsilon .
$$
By Definition 5.3, $\lim_{x\to a^+} f(x) = L$. The proof for $x \to b^-$ is the same with
$x_n := b - c/n$. $\blacksquare$

*Remark.* The argument shows more: uniform continuity on $(a,b)$ is *equivalent* to the existence of both
one-sided limits together with continuity on $(a,b)$ (Exercise 35(b) proves the converse). This is the
one-dimensional prototype of the theorem that a uniformly continuous function on a dense subset extends
uniquely to the completion.

**29.**

**Continuity on $(0,1)$.** On $(0,1)$ the function $x \mapsto 1/x$ is a rational function with
nonvanishing denominator, hence continuous by Corollary 7.11(b); the sine function is continuous; so
$f = \sin\circ(1/x)$ is continuous on $(0,1)$ by Theorem 7.10. $\blacksquare$

**Not uniformly continuous.** Let
$$
x_n := \frac{1}{2n\pi}, \qquad y_n := \frac{1}{2n\pi + \pi/2}, \qquad n \ge 1 .
$$
Both lie in $(0,1)$ since $2\pi > 1$. Their distance is
$$
\lvert x_n - y_n\rvert = \frac{\pi/2}{2n\pi\,(2n\pi + \pi/2)} \longrightarrow 0,
$$
while
$$
f(x_n) = \sin(2n\pi) = 0, \qquad f(y_n) = \sin\Bigl(2n\pi + \frac{\pi}{2}\Bigr) = 1 .
$$
So $\lvert f(x_n)-f(y_n)\rvert = 1$ for all $n$ although $\lvert x_n-y_n\rvert \to 0$; with
$\varepsilon = 1$, Definition 5.6 fails. $\blacksquare$

**No continuous extension to $[0,1]$.** Suppose $F : [0,1] \to \mathbb{R}$ is continuous with
$F(x) = f(x)$ for $x \in (0,1)$. By Theorem 7.18, $F$ is uniformly continuous on $[0,1]$. Then its
restriction $f = F|_{(0,1)}$ is uniformly continuous on $(0,1)$: the defining condition for $F$
quantifies over all pairs in $[0,1]$, hence in particular over pairs in $(0,1)$. This contradicts the
previous paragraph. Hence no such $F$ exists. $\blacksquare$

*Alternative.* Directly: continuity of $F$ at $0$ would force
$F(0) = \lim_{n} F(x_n) = 0$ and also $F(0) = \lim_n F(y_n) = 1$, impossible. This is shorter but uses
two sequences rather than the compactness theorem; both arguments are worth knowing.

**30.**

Throughout, $f$ is nondecreasing on $[a,b]$ and $c \in (a,b)$.

**(a) Disjoint jumps.** First note two monotonicity facts:

* For $a < c < b$, the set $\{f(x) : a < x < c\}$ is nonempty and bounded above by $f(c)$, so
  $f(c^-) = \sup\{f(x) : a<x<c\}$ exists and satisfies $f(c^-) \le f(c)$. Similarly
  $f(c^+) = \inf\{f(x) : c<x<b\}$ exists and $f(c^+) \ge f(c)$.
* If $c < d$, then $f(c^+) \le f(d^-)$. Indeed, pick any $t \in (c,d)$; then
  $$
  f(c^+) = \inf_{c<x<b} f(x) \le f(t) \le \sup_{a<x<d} f(x) = f(d^-),
  $$
  using that $f$ is nondecreasing.

Consequently, for $c_1 < c_2 < \cdots < c_m$ in $D_n$, the open intervals
$$
\bigl(f(c_j^-),\ f(c_j^+)\bigr), \qquad j = 1, \dots, m,
$$
are pairwise disjoint: the right endpoint of the $j$-th is $f(c_j^+) \le f(c_{j+1}^-)$, the left endpoint
of the next. Each has length $f(c_j^+)-f(c_j^-) \ge 1/n$ because $c_j \in D_n$. All of them are contained
in $[f(a), f(b)]$: indeed $f(c_j^-) \ge f(a)$ (the supremum is over $x > a$) and $f(c_j^+) \le f(b)$.
Therefore
$$
\frac{m}{n} \le \sum_{j=1}^{m}\bigl(f(c_j^+)-f(c_j^-)\bigr) \le f(b)-f(a),
$$
so $m \le n\bigl(f(b)-f(a)\bigr)$. In particular $D_n$ has at most $n(f(b)-f(a)) + 1$ elements (the $+1$
allows for the case $f(b) = f(a)$ and for the endpoints of $[a,b]$). $\blacksquare$

**(b) The discontinuity set is countable.** Let $D$ be the set of points of $(a,b)$ at which $f$ is
discontinuous.

*If $f$ is continuous at $c$*, then $f(c^-) = f(c) = f(c^+)$ (both one-sided limits equal the value, by
continuity and Theorem 7.7 applied to the restrictions), so the jump $f(c^+)-f(c^-)$ is $0$.

*If $f(c^+) = f(c^-)$*, then since $f(c^-) \le f(c) \le f(c^+)$ all three numbers are equal. Given
$\varepsilon > 0$, choose $u \in (a,c)$ with $f(u) > f(c^-) - \varepsilon = f(c) - \varepsilon$ (possible
because $f(c^-)$ is the supremum) and $v \in (c,b)$ with $f(v) < f(c^+) + \varepsilon = f(c) + \varepsilon$
(possible because $f(c^+)$ is the infimum). For any $x \in (u,v)$ with $x \in (a,b)$,
$$
f(c) - \varepsilon < f(u) \le f(x) \le f(v) < f(c) + \varepsilon
$$
by monotonicity, so $\lvert f(x)-f(c)\rvert < \varepsilon$. Hence $f$ is continuous at $c$.

Therefore
$$
D = \{c \in (a,b) : f(c^+)-f(c^-) > 0\} = \bigcup_{n \in \mathbb{N}} D_n :
$$
the inclusion "$\subseteq$" holds because a positive jump is at least $1/n$ for some $n$, and
"$\supseteq$" because points of $D_n$ have jump at least $1/n > 0$ and are therefore discontinuities.
Each $D_n$ is finite by part (a), and a countable union of finite sets is countable (Theorem 7.45 of
[The Real Numbers and Completeness](../01-real-numbers-and-completeness/README.md), or simply by
enumerating each finite set in order of $n$). Hence $D$ is at most countable. $\blacksquare$

## Challenge

**31.**

Recall the conventions: every rational $x \ne 1$ can be written uniquely as $x = p/q$ with $p \in \mathbb{Z}$,
$q \in \mathbb{N}$, $\gcd(\lvert p\rvert, q) = 1$, and $q$ minimal; integers have $q = 1$, and
$f(0) = f(0/1) = 1$. In every case $f(x) > 0$ for rational $x$ and $f(x) = 0$ for irrational $x$; in
particular $f \ge 0$.

**At a rational point $a = p/q$.** Then $f(a) = 1/q > 0$. By density of the irrationals there is, for
each $n$, an irrational $t_n$ with $\lvert t_n - a\rvert < 1/n$; then $t_n \to a$ and $f(t_n) = 0$ for all
$n$. Thus $f(t_n) \to 0 \ne f(a)$, and the sequential criterion (Theorem 7.8) shows that $f$ is
discontinuous at $a$. $\blacksquare$

**At an irrational point $a$.** Then $f(a) = 0$. Let $\varepsilon > 0$ and choose $N \in \mathbb{N}$ with
$1/N < \varepsilon$. Consider the set
$$
S := \Bigl\{\, \frac pq \in (a-1, a+1) : p \in \mathbb{Z},\ q \in \mathbb{N},\ \gcd(\lvert p\rvert,q)=1,\ q \le N \,\Bigr\}.
$$
This set is finite: for each $q \le N$, the inequality $\lvert p/q - a\rvert < 1$ gives
$\lvert p\rvert < q(\lvert a\rvert + 1) \le N(\lvert a\rvert+1)$, so only finitely many integers $p$ are
possible, and there are only finitely many $q$. Moreover $a \notin S$ because $a$ is irrational and
elements of $S$ are rational, so
$$
\delta := \min\{\lvert r - a\rvert : r \in S\} > 0
$$
is a minimum of finitely many strictly positive numbers. (If $S$ is empty, take $\delta := 1$.)

Now let $x \in \mathbb{R}$ with $\lvert x - a\rvert < \delta$. If $x$ is irrational, then
$\lvert f(x)-f(a)\rvert = 0 < \varepsilon$. If $x = p/q$ is rational in lowest terms, then
$x \in (a-1,a+1)$ and $x \notin S$ (since $\lvert x-a\rvert < \delta \le \lvert r-a\rvert$ for all $r \in S$
and $x \ne a$), so necessarily $q > N$; hence
$$
\lvert f(x) - f(a)\rvert = f(x) = \frac1q < \frac1N < \varepsilon .
$$
By Definition 5.4, $f$ is continuous at $a$. $\blacksquare$

*Remark.* The proof is a quantifier exercise in miniature: continuity at $a$ requires controlling *all*
rationals with small denominators near $a$, and there are only finitely many of them, so the minimum
distance to them is positive. Near a rational point the opposite happens: rationals with large
denominators crowd arbitrarily close and have small values, but the value at the rational point itself is
bounded away from $0$. Thomae's function is continuous exactly on the irrationals — the complement of
the pattern in Example 9.7.

**32.**

Suppose, for contradiction, that $f : [0,1] \to \mathbb{R}$ is continuous and $f\bigl[[0,1]\bigr] = (0,1)$.

By the extreme value theorem (Theorem 7.17), $f$ attains a maximum $M$ at some point of $[0,1]$; that is,
$M = f(v)$ for some $v$ and $f(x) \le M$ for all $x \in [0,1]$. Since $f[[0,1]] = (0,1)$ and $M \in f[[0,1]]$,
we have $M \in (0,1)$, so $(M+1)/2$ satisfies
$$
0 < M < \frac{M+1}{2} < 1 .
$$
Because $f[[0,1]] = (0,1)$, the number $(M+1)/2$ is attained: there is $x \in [0,1]$ with
$f(x) = (M+1)/2 > M$. This contradicts the maximality of $M$. Hence no such continuous $f$ exists.
$\blacksquare$

*Remark.* Equivalently, a continuous image of the compact interval $[0,1]$ is compact — here, by
Solution 24, a closed interval $[m,M]$ — and $(0,1)$ is not of that form. The argument above avoids
naming compactness and uses only the EVT.

**33.**

Let $f : [a,b] \to \mathbb{R}$ be continuous and injective. Since $f$ is injective, $f(a) \ne f(b)$.

**Reduce to the increasing case.** If $f(a) < f(b)$ we prove that $f$ is strictly increasing; if
$f(a) > f(b)$, apply the same argument to $-f$, which is continuous, injective, and satisfies
$(-f)(a) < (-f)(b)$; if $-f$ is strictly increasing then $f$ is strictly decreasing.

So assume $f(a) < f(b)$. We show that $u < v$ implies $f(u) < f(v)$. Suppose, for contradiction, that
$u < v$ but $f(u) > f(v)$.

*Case 1: $f(v) > f(a)$.* Then $f(a) < f(v) < f(u)$. Apply the intermediate value theorem to the
continuous function $f$ on the interval $[a,u]$: the value $f(v)$ lies strictly between $f(a)$ and
$f(u)$, so there is $w \in (a,u)$ with $f(w) = f(v)$. Since $w < u < v$, we have $w \ne v$, contradicting
injectivity.

*Case 2: $f(v) < f(a)$.* Then $f(v) < f(a) < f(b)$. Apply the intermediate value theorem to $f$ on
$[v,b]$: the value $f(a)$ lies strictly between $f(v)$ and $f(b)$, so there is $w \in (v,b)$ with
$f(w) = f(a)$. Since $w > v \ge u \ge a$ and $w > a$, we have $w \ne a$, contradicting injectivity.

*Case 3: $f(v) = f(a)$.* Then $v \ne a$ (as $v > u \ge a$), contradicting injectivity directly.

All cases lead to a contradiction, so $f(u) < f(v)$ for all $u < v$: $f$ is strictly increasing.
$\blacksquare$

*Remark.* Injectivity alone is far from monotonicity (a bijection of $[0,1]$ onto itself can be wild),
and continuity alone is far from it ($\sin$ on $[0, 2\pi]$ is not injective). It is the combination that
forces order preservation. The result is used in the next topic to show that a differentiable function
with $f' \ne 0$ on an interval is strictly monotone, and later to prove that a continuous bijection on a
compact interval has a continuous inverse (the one-dimensional inverse function theorem).

**34.**

**Nonemptiness.** This is Corollary 7.13(b): $g(x) := f(x) - x$ is continuous on $[0,1]$,
$g(0) = f(0) - 0 \ge 0$ (as $f(0) \in [0,1]$) and $g(1) = f(1) - 1 \le 0$. If either endpoint value is
$0$ we are done; otherwise $g(1) < 0 < g(0)$ and the intermediate value theorem gives $c \in (0,1)$ with
$g(c) = 0$, i.e. $f(c) = c$. Hence $F \ne \varnothing$.

**Sequential closedness.** Let $x_n \in F$ with $x_n \to x$. Since $[0,1]$ is closed under limits of
sequences (if $0 \le x_n \le 1$ then $0 \le x \le 1$), $x \in [0,1]$. By continuity of $f$ at $x$ and the
sequential criterion (Theorem 7.8), $f(x_n) \to f(x)$. But $f(x_n) = x_n$ for all $n$, so $f(x_n) \to x$.
Uniqueness of limits of sequences (Lemma 7.15(c)) gives $f(x) = x$, i.e. $x \in F$. $\blacksquare$

*Remark.* The set $F$ can be a single point (for $f(x) = 1 - x$ on $[0,1]$, $F = \{1/2\}$), a finite set,
or an interval (for $f = \mathrm{id}$, $F = [0,1]$); it can even be a Cantor-like closed set. What the
exercise shows is that it is always nonempty and closed *relative to* $[0,1]$ — a topological statement
proved here with sequences.

**35.**

**(a) The example.** Let
$$
f(x) := \sin\frac1x, \qquad x \in (0,1).
$$
*Bounded:* $\lvert f(x)\rvert \le 1$ for all $x$.
*Continuous:* $x \mapsto 1/x$ is continuous and nowhere zero on $(0,1)$, $\sin$ is continuous, so the
composition is continuous by Theorem 7.10.
*Not uniformly continuous:* let $x_n = 1/(2n\pi)$ and $y_n = 1/(2n\pi + \pi/2)$, as in Solution 29. Then
$\lvert x_n-y_n\rvert \to 0$ while $\lvert f(x_n)-f(y_n)\rvert = 1$. Hence Definition 5.6 fails with
$\varepsilon = 1$. $\blacksquare$

**(b) The converse.** Suppose $f$ is continuous on $(0,1)$ and
$$
L_0 := \lim_{x\to 0^+} f(x) \in \mathbb{R}, \qquad L_1 := \lim_{x\to 1^-} f(x) \in \mathbb{R}
$$
both exist. Define $F : [0,1] \to \mathbb{R}$ by
$$
F(x) := \begin{cases} L_0, & x = 0,\\ f(x), & 0 < x < 1,\\ L_1, & x = 1 . \end{cases}
$$
Then $F$ is continuous at every interior point by hypothesis, at $0$ because $\lim_{x\to 0^+} f(x) = L_0 = F(0)$,
and at $1$ because $\lim_{x\to 1^-} f(x) = L_1 = F(1)$. Hence $F$ is continuous on the closed bounded
interval $[0,1]$, and Theorem 7.18 gives that $F$ is uniformly continuous on $[0,1]$. The restriction of
a uniformly continuous function to a subset is uniformly continuous (the condition for $F$ quantifies
over all pairs in $[0,1]$, hence over all pairs in $(0,1)$), so $f$ is uniformly continuous on $(0,1)$.
$\blacksquare$

*Remark.* Together with Solution 28, this gives the characterisation: *a continuous $f$ on $(a,b)$ is
uniformly continuous if and only if both one-sided limits at $a$ and $b$ exist in $\mathbb{R}$.* Boundedness
alone is not enough (part (a)), and neither is continuity alone (Solution 26).

**36.**

Suppose, for contradiction, that $f$ has no fixed point. Then $g(x) := f(x) - x$ is continuous on
$\mathbb{R}$ (Theorem 7.9) and $g(x) \ne 0$ for every $x$.

**Step 1: $g$ has constant sign.** If there were $u, v$ with $g(u) > 0 > g(v)$, the intermediate value
theorem applied to $g$ on the interval with endpoints $u$ and $v$ would give $c$ between them with
$g(c) = 0$, contradicting $g \ne 0$. Hence either $g(x) > 0$ for all $x$, or $g(x) < 0$ for all $x$.

**Step 2: both alternatives contradict the involution identity.**

*If $g > 0$* then $f(t) > t$ for every real $t$. Apply this with $t := f(x)$:
$$
f(f(x)) > f(x) .
$$
By hypothesis $f(f(x)) = x$, so $x > f(x)$. But $g(x) > 0$ says $f(x) > x$. Contradiction.

*If $g < 0$* then $f(t) < t$ for every $t$. With $t := f(x)$,
$$
f(f(x)) < f(x), \qquad\text{i.e.}\qquad x < f(x),
$$
contradicting $f(x) < x$.

Both alternatives are impossible, so the assumption was false: there is $c \in \mathbb{R}$ with
$f(c) = c$. $\blacksquare$

*Remark.* No monotonicity of $f$ was used, only continuity. The identity $f \circ f = \mathrm{id}$ makes
$f$ a bijection equal to its own inverse; a continuous involution of $\mathbb{R}$ that is increasing has
infinitely many fixed points, and one that is decreasing has exactly one, but the argument above shows
only that at least one exists in either case. The same argument, with $\mathbb{R}$ replaced by any
interval, shows that every continuous involution of an interval has a fixed point.
