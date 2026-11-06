# Riemann Integration — Solutions

> [Riemann Integration](README.md) · Solutions to the 36 problems in [exercises.md](exercises.md)

Each solution states the strategy first, then carries out every step. Computations from the definition are
closed with a certified gap between an upper and a lower sum, and proof problems receive complete proofs.
Where a second route exists it is given as a remark.

## Beginner

**1.** *Strategy: on each subinterval the function $2x$ is increasing, so the infimum sits at the left
endpoint and the supremum at the right one; compute the four sums term by term.*

For $P = \{0,\tfrac12,1\}$ there are two subintervals, both of length $\tfrac12$:

* on $[0,\tfrac12]$: $m_1 = 2\cdot 0 = 0$, $M_1 = 2\cdot\tfrac12 = 1$;
* on $[\tfrac12,1]$: $m_2 = 1$, $M_2 = 2$.

Hence

$$L(f,P) = 0\cdot\tfrac12 + 1\cdot\tfrac12 = \tfrac12, \qquad U(f,P) = 1\cdot\tfrac12 + 2\cdot\tfrac12 = \tfrac32 .$$

For $Q = \{0,\tfrac14,\tfrac12,\tfrac34,1\}$ there are four subintervals, all of length $\tfrac14$, and the
same monotonicity gives $m_i = 2x_{i-1}$, $M_i = 2x_i$:

$$L(f,Q) = \tfrac14\bigl(0 + \tfrac12 + 1 + \tfrac32\bigr) = \tfrac14\cdot 3 = \tfrac34, \qquad
U(f,Q) = \tfrac14\bigl(\tfrac12 + 1 + \tfrac32 + 2\bigr) = \tfrac14\cdot 5 = \tfrac54 .$$

Therefore

$$L(f,P) = \tfrac12 \le \tfrac34 = L(f,Q) \le \tfrac54 = U(f,Q) \le \tfrac32 = U(f,P),$$

which is exactly the chain of Lemma 7.2. Note also that $\int_0^1 2x\,dx = 1$ lies in both intervals
$[\tfrac12,\tfrac32]$ and $[\tfrac34,\tfrac54]$, and that the second interval is the shorter one: refinement
improved the estimate.

**2.** *Strategy: compute the infimum and supremum of $x^2$ on each of the two subintervals, then compare
the gap with $\varepsilon = 1$.*

On $[0,1]$ we have $m_1 = 0^2 = 0$ and $M_1 = 1^2 = 1$; on $[1,2]$, $m_2 = 1$ and $M_2 = 4$. Both
subintervals have length $1$, so

$$L(f,P) = 0\cdot 1 + 1\cdot 1 = 1, \qquad U(f,P) = 1\cdot 1 + 4\cdot 1 = 5 .$$

Since $1 \le \tfrac83 \le 5$, the sandwich inequality is confirmed. But

$$U(f,P) - L(f,P) = 4 \ge 1 = \varepsilon,$$

so this partition does **not** certify integrability at level $\varepsilon = 1$. The criterion requires a
partition with gap $< 1$. For the uniform partition with $n$ parts of $[0,2]$, the telescoping computation
$U - L = h\sum_i (x_i^2 - x_{i-1}^2) = \frac{2}{n}\cdot 4 = \frac{8}{n}$ shows that $n \ge 9$ parts suffice.
A single partition that happens to give a small gap proves nothing on its own; what is needed is a
partition for every $\varepsilon$.

**3.** *Strategy: for a constant function the infimum and supremum on every subinterval coincide, so every
lower and every upper sum equals $c(b-a)$.*

Let $P = \{x_0,\dots,x_n\}$ be any partition of $[a,b]$. For each $i$ and every $t \in I_i$ we have
$f(t) = c$, so

$$m_i(f,P) = \inf_{I_i} f = c, \qquad M_i(f,P) = \sup_{I_i} f = c .$$

Therefore

$$L(f,P) = \sum_{i=1}^n c\,\Delta x_i = c\sum_{i=1}^n \Delta x_i = c(b-a), \qquad U(f,P) = c(b-a),$$

where the telescoping $\sum_i (x_i - x_{i-1}) = b - a$ was used. This holds for **every** $P$, so the set of
lower sums is the singleton $\{c(b-a)\}$ and its supremum is $c(b-a)$; likewise the infimum of the upper
sums is $c(b-a)$. The two integrals agree, so $f$ is integrable with $\int_a^b f = c(b-a)$.

**4.** *Strategy: bound the infimum and supremum on each subinterval by the global infimum and supremum,
then multiply by the positive lengths and sum.*

Fix a partition $P$. For every $i$ and every $t \in I_i \subseteq [a,b]$,

$$m = \inf_{[a,b]} f \le f(t) \le \sup_{[a,b]} f = M,$$

so $m$ is a lower bound and $M$ an upper bound for $f$ on $I_i$. Hence

$$m \le m_i(f,P) \le M_i(f,P) \le M .$$

Multiplying by $\Delta x_i > 0$ and summing over $i$,

$$m\sum_{i=1}^n \Delta x_i \le \sum_{i=1}^n m_i \Delta x_i \le \sum_{i=1}^n M_i\Delta x_i \le M\sum_{i=1}^n \Delta x_i,$$

that is

$$m(b-a) \le L(f,P) \le U(f,P) \le M(b-a).$$

For the integrals: $m(b-a)$ is a lower bound for the set of all lower sums, so it is at most that set's
supremum, giving $m(b-a) \le \underline{\int_a^b} f$. Similarly $M(b-a)$ is an upper bound for the set of
all upper sums, so $\overline{\int_a^b} f \le M(b-a)$. Finally $\underline{\int_a^b} f \le
\overline{\int_a^b} f$ is Corollary 7.3.

**5.** *Strategy: compute the right-endpoint Riemann sum exactly, take the limit, and then certify the value
with the Darboux sums of the same partition; confirm independently with the fundamental theorem.*

With $x_i = i/n$ and $t_i = x_i$, and $\Delta x_i = 1/n$,

$$S(f,P_n,(t_i)) = \sum_{i=1}^n \Bigl(1 + \frac{3i}{n}\Bigr)\frac1n = \frac1n\sum_{i=1}^n 1 + \frac{3}{n^2}\sum_{i=1}^n i = 1 + \frac{3}{n^2}\cdot\frac{n(n+1)}{2} = 1 + \frac{3(n+1)}{2n}.$$

As $n\to\infty$ this tends to $1 + \tfrac32 = \tfrac52$. To conclude that the *integral* is $\tfrac52$ we do
not rely on the Riemann sum alone: since $f$ is increasing, $m_i = f(x_{i-1})$ and $M_i = f(x_i)$, so the
same computation with $i-1$ in place of $i$ gives

$$L(f,P_n) = 1 + \frac{3(n-1)}{2n} \le \int_0^1 f \le 1 + \frac{3(n+1)}{2n} = U(f,P_n)$$

for every $n$ (the integral lies between the sums), and both bounds tend to $\tfrac52$. Hence
$\int_0^1 (1+3x)\,dx = \tfrac52$.

*Check with Theorem 7.21.* The integrand is continuous, hence integrable (Theorem 7.8). The polynomial
$F(x) = x + \tfrac32 x^2$ is an antiderivative, continuous on $[0,1]$ and differentiable with
$F' = 1 + 3x$. By Theorem 7.21, $\int_0^1 (1+3x)\,dx = F(1) - F(0) = \tfrac52$. ✓

**6.** *Strategy: uniform partition with $h = 2/n$; use monotonicity of $x \mapsto x$ for the infimum and
supremum on each strip; the sums telescope.*

With $h = 2/n$ and $x_i = ih$, we have $m_i = x_{i-1}$ and $M_i = x_i$. Hence

$$L(f,P_n) = \sum_{i=1}^n (i-1)h\cdot h = h^2\sum_{i=1}^n (i-1) = \frac{4}{n^2}\cdot\frac{n(n-1)}{2} = \frac{2(n-1)}{n},$$

$$U(f,P_n) = \sum_{i=1}^n ih\cdot h = h^2\sum_{i=1}^n i = \frac{4}{n^2}\cdot\frac{n(n+1)}{2} = \frac{2(n+1)}{n}.$$

Their difference is $U - L = \frac{4}{n}$, which tends to $0$, so by Theorem 7.4 the function is integrable.
Moreover $L(f,P_n) \le \int_0^2 x\,dx \le U(f,P_n)$ for every $n$, and both bounds tend to $2$; hence
$\int_0^2 x\,dx = 2$. (This agrees with the area of the triangle of base $2$ and height $2$.)

**7.** *Strategy: substitute the two values of $c$ into the identity and read off the conventions.*

Let $f$ be integrable on the relevant intervals.

* $c = a$: the identity reads $\int_a^b f = \int_a^a f + \int_a^b f = 0 + \int_a^b f$. ✓
* $c = b$: it reads $\int_a^b f = \int_a^b f + \int_b^b f = \int_a^b f + 0$. ✓

Both hold, and each holds *because* of the convention $\int_a^a f = 0$: any other value would break
additivity at the endpoints. Similarly, for $c$ outside $[a,b]$, say $c > b$, the convention
$\int_b^c f = \int_a^c f - \int_a^b f$ (equivalently $\int_a^c = \int_a^b + \int_b^c$) is exactly what makes
$\int_a^b = \int_a^c + \int_c^b = \int_a^c - \int_b^c$ true. The conventions are chosen so that the
additivity identity of Theorem 7.13 holds for **all** orderings of the three points, with no case analysis.

**8.** *Strategy: use density of $\mathbb{Q}$ and of its complement to evaluate every infimum and supremum.*

Let $P$ be any partition of $[0,2]$ into subintervals of positive length. Each $I_i$ contains a rational
number, where $D = 1$, and an irrational number, where $D = 0$. Hence

$$m_i(D,P) = 0, \qquad M_i(D,P) = 1$$

for every $i$, and therefore

$$L(D,P) = \sum_{i=1}^n 0\cdot\Delta x_i = 0, \qquad U(D,P) = \sum_{i=1}^n 1\cdot\Delta x_i = 2 .$$

Since this holds for every partition,

$$\underline{\int_0^2} D = \sup_P L(D,P) = 0, \qquad \overline{\int_0^2} D = \inf_P U(D,P) = 2 .$$

The two differ, so $D$ is **not** Riemann integrable on $[0,2]$. Equivalently, Theorem 7.24 holds with
$\varepsilon_0 = 2$: every partition has $U - L = 2$. No refinement can help, because a subinterval of
positive length always contains both a rational and an irrational.

**9.** *Strategy: prove the two sup/inf identities, apply them to every subinterval, and compare the
resulting lower and upper integrals.*

*Claim 1:* for a bounded $g$ on a nonempty set $I$, $\sup_I(-g) = -\inf_I g$. Let $\ell = \inf_I g$. For all
$x \in I$, $g(x) \ge \ell$, hence $-g(x) \le -\ell$: so $-\ell$ is an upper bound of $-g$ on $I$. If $u$ is
any upper bound of $-g$, then $-g(x) \le u$ for all $x$, i.e. $g(x) \ge -u$ for all $x$, so $-u \le \ell$,
i.e. $u \ge -\ell$. Thus $-\ell$ is the least upper bound. ∎

*Claim 2:* $\inf_I(-g) = -\sup_I g$, by the same argument with the inequalities reversed (or by applying
Claim 1 to $-g$). ∎

Now let $P$ be a partition. Applying the claims on each $I_i$,

$$m_i(-f,P) = \inf_{I_i}(-f) = -M_i(f,P), \qquad M_i(-f,P) = \sup_{I_i}(-f) = -m_i(f,P).$$

Multiplying by $\Delta x_i$ and summing,

$$L(-f,P) = -\sum_i M_i(f,P)\Delta x_i = -U(f,P), \qquad U(-f,P) = -\sum_i m_i(f,P)\Delta x_i = -L(f,P).$$

Therefore, using $\sup(-A) = -\inf A$ for a set $A$ of real numbers,

$$\underline{\int_a^b}(-f) = \sup_P\bigl(-U(f,P)\bigr) = -\inf_P U(f,P) = -\int_a^b f, \qquad
\overline{\int_a^b}(-f) = \inf_P\bigl(-L(f,P)\bigr) = -\sup_P L(f,P) = -\int_a^b f .$$

The two are equal, so $-f$ is integrable with $\int_a^b(-f) = -\int_a^b f$. (This is Theorem 7.10 with
$c=-1$; the point of the exercise is that the sup/inf reversal has to be checked.)

**10.** *Strategy: name an antiderivative, verify the hypotheses of Theorem 7.21 one by one, then check by a
second computation.*

The integrand $f(x) = (x+1)^2$ is continuous on $[0,1]$, hence Riemann integrable by Theorem 7.8. The
function

$$F(x) = \frac{(x+1)^3}{3}$$

is a polynomial, hence continuous on $[0,1]$ and differentiable on $(0,1)$ with

$$F'(x) = \frac{3(x+1)^2}{3} = (x+1)^2 = f(x).$$

All hypotheses of Theorem 7.21 are satisfied, so

$$\int_0^1 (x+1)^2\,dx = F(1) - F(0) = \frac{2^3}{3} - \frac{1^3}{3} = \frac{8}{3} - \frac{1}{3} = \frac73 .$$

*Second computation.* Expand: $(x+1)^2 = x^2 + 2x + 1$. Each term is integrable (polynomials are
continuous), and by Theorems 7.10 and 7.11,

$$\int_0^1 (x^2 + 2x + 1) = \int_0^1 x^2 + 2\int_0^1 x + \int_0^1 1 = \frac13 + 2\cdot\frac12 + 1 = \frac13 + 1 + 1 = \frac73 .$$

✓ Both routes agree. (The values $\int_0^1 x^2 = \tfrac13$ and $\int_0^1 x = \tfrac12$ were computed from
the definition in Examples 9.2 and 9.1.)

## Intermediate

**11.** *Strategy: show that translating $f$ by a constant translates every lower and upper sum by
$c(b-a)$, then read off the integrals.*

*Claim:* for a bounded $g$ on a nonempty set $I$ and any constant $c$, $\sup_I(g + c) = \sup_I g + c$ and
$\inf_I(g+c) = \inf_I g + c$. Indeed, $g(x) + c \le \sup_I g + c$ for all $x$, so $\sup_I g + c$ is an upper
bound; and if $u$ is any upper bound of $g+c$, then $g(x) \le u - c$ for all $x$, so $\sup_I g \le u - c$ and
$u \ge \sup_I g + c$. Hence the least upper bound is $\sup_I g + c$. The infimum statement is the same with
reversed inequalities. ∎

Apply this on each subinterval of a partition $P$: $m_i(f+c,P) = m_i(f,P) + c$ and $M_i(f+c,P) = M_i(f,P)+c$.
Since $\sum_i \Delta x_i = b-a$,

$$L(f+c,P) = L(f,P) + c(b-a), \qquad U(f+c,P) = U(f,P) + c(b-a).$$

Now let $\varepsilon>0$. Because $f$ is integrable, there is $P$ with $U(f,P) - L(f,P) < \varepsilon$ and
also $L(f,P) > \int_a^b f - \varepsilon$, $U(f,P) < \int_a^b f + \varepsilon$ (characterisation of sup and
inf). For this $P$,

$$U(f+c,P) - L(f+c,P) = U(f,P) - L(f,P) < \varepsilon,$$

so $f+c$ is integrable by Theorem 7.4, and

$$\int_a^b f + c(b-a) - \varepsilon < L(f,P) + c(b-a) = L(f+c,P) \le \int_a^b (f+c) \le U(f+c,P) < \int_a^b f + c(b-a) + \varepsilon .$$

Since $\varepsilon>0$ is arbitrary, $\int_a^b (f+c) = \int_a^b f + c(b-a)$.

**12.** *Strategy: compare the infimum on each subinterval, sum, and take suprema; integrability identifies
the supremum of the lower sums with the integral.*

Since $f(x) \le g(x)$ for every $x$, for each partition $P$ and each $i$ the number $m_i(f,P) = \inf_{I_i} f$
is a lower bound of $g$ on $I_i$, hence

$$m_i(f,P) \le \inf_{I_i} g = m_i(g,P).$$

Multiplying by $\Delta x_i > 0$ and summing gives

$$L(f,P) \le L(g,P) \qquad \text{for every partition } P .$$

Taking the supremum over all partitions and using integrability of both functions to replace those suprema
by the integrals,

$$\int_a^b f = \sup_P L(f,P) \le \sup_P L(g,P) = \int_a^b g . \qquad \blacksquare$$

*Remark.* The same conclusion follows from the upper sums: $M_i(f,P) \le M_i(g,P)$ gives $U(f,P) \le U(g,P)$
for all $P$, and taking infima gives $\int f \le \int g$. Both routes are valid because integrability means
that each of the two suprema/infima equals the integral.

**13.** *Strategy: take an $\varepsilon$-partition for $[a,b]$, force it to contain the endpoints of
$[u,v]$, restrict, and observe that the restricted gap is a sub-sum of the total gap.*

Let $\varepsilon>0$. By Theorem 7.4 there is a partition $P$ of $[a,b]$ with $U(f,P) - L(f,P) < \varepsilon$.
Let $P' = P \cup \{u,v\}$. By Lemma 7.2, $P'$ refines $P$, so

$$U(f,P') - L(f,P') \le U(f,P) - L(f,P) < \varepsilon .$$

Now restrict $P'$ to $[u,v]$: this gives a partition $P''$ of $[u,v]$ whose subintervals are exactly the
subintervals of $P'$ that lie inside $[u,v]$. Hence

$$U(f,P'') - L(f,P'') = \sum_{I \subseteq [u,v]} \omega(f,I)\,\lvert I\rvert \le \sum_{I \in P'} \omega(f,I)\,\lvert I\rvert = U(f,P') - L(f,P') < \varepsilon,$$

because all omitted terms are $\ge 0$. Since $\varepsilon>0$ was arbitrary, the Riemann criterion gives
$f \in \mathcal{R}[u,v]$. (If $u = v$ the statement is vacuous: the interval is a point and
$\int_u^u f = 0$ by convention.)

*Remark.* This is the content of Theorem 7.13(1); the only point is that restriction *decreases* the gap,
never increases it, because the gap is a sum of non-negative contributions.

**14.** *Strategy: continuity at a point where $f$ is positive forces $f$ to be bounded below on a small
interval; monotonicity and additivity then force a positive integral.*

Let $x_0 \in [a,b]$ be a continuity point of $f$ and suppose, for contradiction, that $f(x_0) > 0$. Put
$\eta = f(x_0)/2 > 0$. By continuity at $x_0$ there is $\delta>0$ such that

$$\lvert x - x_0\rvert < \delta, \ x \in [a,b] \ \Longrightarrow\ \lvert f(x) - f(x_0)\rvert < \eta,$$

so $f(x) > f(x_0) - \eta = \eta$ on the set $J = (x_0 - \delta, x_0+\delta) \cap [a,b]$. Write
$J = [u,v]$ with $u<v$; its length is $\ell = v - u > 0$ because $x_0$ is an interior point of $J$ in
$[a,b]$ (if $x_0$ is an endpoint, take the corresponding half-interval, which still has positive length).

On $[u,v]$ we have $f \ge \eta$, so by monotonicity and the constant-integral computation,

$$\int_u^v f \ge \int_u^v \eta = \eta\,\ell > 0 .$$

Since $f \ge 0$ everywhere, Theorem 7.13 and monotonicity give

$$\int_a^b f = \int_a^u f + \int_u^v f + \int_v^b f \ge \int_u^v f > 0,$$

contradicting $\int_a^b f = 0$. Hence $f(x_0) = 0$.

*Remark.* Nothing is claimed about the points where $f$ is discontinuous: a function such as
$\mathbf{1}_{\{1/2\}}$ on $[0,1]$ is non-negative with integral $0$ and is nonzero at its discontinuity.

**15.** *Strategy: the set $\{1/n\}$ has one accumulation point, $0$; isolate the finitely many large terms
in very short intervals and absorb everything near $0$ into one short interval.*

Let $\varepsilon>0$. Choose $N \in \mathbb{N}$ with $1/N < \varepsilon/2$. The points
$1, \tfrac12, \dots, \tfrac1N$ are $N$ points, all lying in $[1/N, 1]$. Enclose them in $N$ disjoint closed
intervals of total length less than $\varepsilon/2$; this is possible because finitely many points can be
covered by arbitrarily short intervals.

Let $P$ be a partition of $[0,1]$ whose points include $0$, $1/N$, $1$, and all endpoints of those $N$
intervals. Its subintervals fall into three groups.

* Subintervals contained in $[0, 1/N]$: their total length is $1/N < \varepsilon/2$, and since
  $0 \le h \le 1$ the contribution to $U - L$ is at most $1\cdot\varepsilon/2$.
* Subintervals contained in one of the small enclosing intervals: total length $<\varepsilon/2$, contribution
  at most $\varepsilon/2$.
* All remaining subintervals: they contain no point of $\{1/n : n \in \mathbb{N}\}$ in their closure, and they
  avoid $[0,1/N]$, so $h \equiv 0$ on them and the contribution is $0$.

Hence $U(h,P) - L(h,P) < \varepsilon$, so $h$ is integrable by Theorem 7.4. Moreover every subinterval of
every partition contains a point where $h = 0$ (the set $\{1/n\}$ is countable, an interval is uncountable),
so $m_i(h,P) = 0$ and $L(h,P) = 0$ for every $P$. Therefore

$$0 \le \int_0^1 h = \sup_P L(h,P) = 0 . \qquad \blacksquare$$

**16.** *Strategy: (a) quote Proposition 7.18; (b) exhibit tags near the singularity that make a Riemann sum
arbitrarily large for any mesh.*

**(a)** The function $g$ is unbounded on $[0,1]$: $g(x) = 1/x \to +\infty$ as $x \to 0^+$. By Proposition
7.18, an unbounded function on $[a,b]$ satisfies no Riemann-type limit condition, so $g$ is not Riemann
integrable.

**(b)** Let $I \in \mathbb{R}$ and $\delta>0$ be arbitrary; we exhibit a tagged partition with mesh $<\delta$
and Riemann sum exceeding $\lvert I\rvert + 1$. Let $P = \{0, x_1, \dots, x_n\}$ be any partition with
$\lVert P\rVert < \delta$ and $x_1 < 1$ (for instance a uniform partition with $n$ large). Choose tags
$t_i = x_i$ for $i \ge 2$ and $t_1 \in (0,x_1)$ so small that

$$\frac{1}{t_1} > \frac{\lvert I\rvert + 1 + \sum_{i\ge2}\lvert g(t_i)\rvert\Delta x_i}{\Delta x_1}.$$

Such $t_1$ exists because $1/t_1 \to \infty$ as $t_1 \to 0^+$. Then, as in the proof of Proposition 7.18,

$$\bigl\lvert S(g,P,(t_i))\bigr\rvert \ge \frac{1}{t_1}\Delta x_1 - \sum_{i\ge2}\lvert g(t_i)\rvert\Delta x_i > \lvert I\rvert + 1 .$$

So every candidate $I$ and every $\delta$ are violated, and $g$ satisfies Definition 5.7 for no $I$.
$\blacksquare$

*Remark.* The failure is local: $g$ is continuous, hence integrable, on every $[\eta, 1]$ with $\eta>0$. This
is precisely the situation the improper integral $\lim_{\eta\to0^+}\int_\eta^1 1/x\,dx$ is designed to handle,
and that limit diverges as well.

**17.** *Strategy: write the difference as a step function vanishing on the open subintervals, then use
integrability of step functions and linearity.*

Let $D = \{d_1,\dots,d_k\}$ be the finite set of points where $g \ne f$, and let $h = g - f$; then $h$ vanishes
off $D$. Order the points of $D \cup \{a,b\}$ increasingly and call them $y_0 = a < y_1 < \cdots < y_m = b$;
this is a partition $P_0$ of $[a,b]$. On each open interval $(y_{j-1}, y_j)$ the function $h$ is identically
$0$, so $h$ is a step function in the sense of Definition 5.8 (its values at the partition points, where it
may be nonzero, are irrelevant to that definition). By Lemma 7.26, $h$ is integrable and

$$\int_a^b h = \sum_{j=1}^m 0\cdot(y_j - y_{j-1}) = 0 .$$

Now $g = f + h$ with $f$ integrable and $h$ integrable, so $g$ is integrable by Theorem 7.11 and

$$\int_a^b g = \int_a^b f + \int_a^b h = \int_a^b f . \qquad \blacksquare$$

*Remark (direct $\varepsilon$-proof).* If one does not want to quote linearity, take a partition $P$ with
$U(f,P) - L(f,P) < \varepsilon$ and refine it so that every point of $D$ lies in the interior of a distinct
subinterval of total length $< \varepsilon/(4B)$, where $B$ bounds $\lvert f\rvert$ and $\lvert g\rvert$. The
contribution of those subintervals is at most $2B\cdot\varepsilon/(4B) = \varepsilon/2$, and on the others
$g$ agrees with $f$ except possibly at endpoints, which changes each oscillation by at most $2B$ on at most
$2k$ intervals — this last point is what makes the direct argument fiddly and the step-function argument
preferable.

**18.** *Strategy: use $\lvert\sqrt s - \sqrt t\rvert \le \sqrt{\lvert s-t\rvert}$, split the subintervals
into those with small oscillation of $f$ and those with large oscillation but small total length.*

First note the inequality. For $s,t \ge 0$,

$$\lvert \sqrt s - \sqrt t\rvert\,(\sqrt s + \sqrt t) = \lvert s - t\rvert,$$

and $\sqrt s + \sqrt t \ge \lvert\sqrt s - \sqrt t\rvert$, so
$\lvert\sqrt s - \sqrt t\rvert^2 \le \lvert s - t\rvert$.

Since $f$ is integrable it is bounded; let $0 \le f \le B$. Let $\varepsilon>0$. Choose a partition $P$ with
$U(f,P) - L(f,P) < \varepsilon^2$ (Theorem 7.4 applied with the tolerance $\varepsilon^2$; if
$\varepsilon^2 > $ anything, that is harmless). Write $\omega_i = \omega(f,I_i)$ and let

$$S = \{i : \omega_i \ge \varepsilon\}, \qquad S^c = \{i : \omega_i < \varepsilon\}.$$

Then $\varepsilon\sum_{i\in S}\Delta x_i \le \sum_{i\in S}\omega_i\Delta x_i \le U(f,P)-L(f,P) < \varepsilon^2$,
so $\sum_{i \in S}\Delta x_i < \varepsilon$.

On $S^c$, the inequality gives $\omega(\sqrt f, I_i) \le \sqrt{\omega_i} < \sqrt\varepsilon$. On $S$, we have
$\omega(\sqrt f,I_i) \le \sqrt{2B}$ because $0 \le \sqrt f \le \sqrt B$ (so $\omega(\sqrt f, I_i) \le \sqrt B \le \sqrt{2B}$).
Therefore

$$U(\sqrt f,P) - L(\sqrt f,P) = \sum_{S^c}\omega(\sqrt f,I_i)\Delta x_i + \sum_{S}\omega(\sqrt f,I_i)\Delta x_i \le \sqrt{\varepsilon}\,(b-a) + \sqrt{2B}\,\varepsilon .$$

Given $\varepsilon'>0$, choose $\varepsilon>0$ with $\sqrt\varepsilon(b-a) + \sqrt{2B}\,\varepsilon < \varepsilon'$
(possible since the left side tends to $0$ with $\varepsilon$). Then the criterion gives
$\sqrt f \in \mathcal{R}[a,b]$.

*Remark.* The composition $x \mapsto \sqrt x$ is continuous, so this is a special case of Exercise 27; the
direct proof is included because the estimate is instructive.

**19.** *Strategy: compute the integral and the average, solve $f(c) = $ average, and separately exhibit a
function for which the equation has no solution.*

**(a)** By Theorem 7.21 with $F(x) = 4x - x^3/3$ (a polynomial with $F' = 4 - x^2$),

$$\int_0^2 (4 - x^2)\,dx = \left[4x - \frac{x^3}{3}\right]_0^2 = 8 - \frac83 = \frac{16}{3}.$$

The average value is $\frac{1}{2}\cdot\frac{16}{3} = \frac83$. So we need $c \in [0,2]$ with

$$4 - c^2 = \frac83 \iff c^2 = 4 - \frac83 = \frac43 \iff c = \pm\frac{2}{\sqrt3}.$$

Only $c = \frac{2}{\sqrt3} = \frac{2\sqrt3}{3} \approx 1.1547$ lies in $[0,2]$ (the negative root is
$-1.1547 \notin [0,2]$). ✓ Check: $f(c) = 4 - \frac43 = \frac83$ ✓.

**(b)** Let $f = \mathbf{1}_{[0,1/3]}$ on $[0,1]$. It is a step function, hence integrable (Lemma 7.26), and

$$\int_0^1 f = 1\cdot\tfrac13 + 0\cdot\tfrac23 = \tfrac13,$$

so the average value is $\tfrac13$. But $f$ takes only the values $0$ and $1$: there is no $c$ with
$f(c) = \tfrac13$. The intermediate value theorem is exactly the missing hypothesis; continuity is not a
technicality here but the whole content of Theorem 7.16.

**20.** *Strategy: take an $\varepsilon$-partition and add the single point $c$; the gap can only shrink.*

Let $\varepsilon>0$. By Theorem 7.4 there is a partition $P_0$ of $[a,b]$ with $U(f,P_0) - L(f,P_0) < \varepsilon$.
Put $P = P_0 \cup \{c\}$. Then $c \in P$, and by Lemma 7.2 (a refinement can only raise $L$ and lower $U$),

$$U(f,P) - L(f,P) \le U(f,P_0) - L(f,P_0) < \varepsilon . \qquad \blacksquare$$

This little lemma is used silently whenever a partition must be split at a prescribed point, for instance in
the proof of additivity (Theorem 7.13) and in the fundamental theorem.

## Advanced

**21.** *Strategy: uniform limits of integrable functions are integrable (Theorem 7.30); continuous functions
are uniform limits of step functions.*

**(a)** Let $s_n$ be step functions on $[a,b]$ with $s_n \to f$ uniformly. Each $s_n$ is integrable by Lemma
7.26, so Theorem 7.30 applies and gives $f \in \mathcal{R}[a,b]$.

**(b)** Let $f$ be continuous on $[a,b]$ and let $\varepsilon>0$. By uniform continuity there is $\delta>0$
such that $\lvert x - y\rvert < \delta$ implies $\lvert f(x) - f(y)\rvert < \varepsilon$. Choose $n$ with
$(b-a)/n < \delta$ and let $x_i = a + i(b-a)/n$. Define

$$s_n(t) = f(x_i) \quad \text{for } t \in [x_{i-1}, x_i), \qquad i = 1,\dots,n, \qquad s_n(b) = f(b).$$

This is a step function (its partition is $\{x_0,\dots,x_n\}$, and the value at the single point $b$ is
irrelevant). For $t \in [x_{i-1},x_i)$ we have $\lvert t - x_i\rvert \le (b-a)/n < \delta$, so

$$\lvert f(t) - s_n(t)\rvert = \lvert f(t) - f(x_i)\rvert < \varepsilon .$$

Hence $\sup_{[a,b]}\lvert f - s_n\rvert \le \varepsilon$ for every $n$ with $(b-a)/n<\delta$; that is,
$s_n \to f$ uniformly as $n\to\infty$. By part (a), $f$ is integrable. $\blacksquare$

*Remark.* This is a second proof of Theorem 7.8, independent of the direct estimate $U - L \le \varepsilon$.
It shows where the uniform continuity is really used: to make *one* step function close to $f$ everywhere at
once, rather than merely close on average.

**22.** *Strategy: for a monotone function on a uniform partition the sums telescope, so the gap is a fixed
multiple of the mesh.*

**(a)** Suppose $f$ is decreasing on $[a,b]$ and put $h = (b-a)/n$, $x_i = a + ih$. On $I_i$ a decreasing
function has supremum $f(x_{i-1})$ and infimum $f(x_i)$, so

$$U(f,P_n) - L(f,P_n) = \sum_{i=1}^{n}\bigl(f(x_{i-1}) - f(x_i)\bigr)h = h\bigl(f(a) - f(b)\bigr) = \frac{(b-a)\bigl(f(a)-f(b)\bigr)}{n} \longrightarrow 0 .$$

By Theorem 7.4, $f$ is integrable. ∎

**(b)** Suppose $f$ is non-decreasing. Then $m_i = f(x_{i-1})$ and $M_i = f(x_i)$, and the same telescoping
gives

$$U(f,P_n) - L(f,P_n) = h\sum_{i=1}^n \bigl(f(x_i) - f(x_{i-1})\bigr) = \frac{b-a}{n}\bigl(f(b) - f(a)\bigr),$$

where $\sum_{i=1}^n (f(x_i)-f(x_{i-1})) = f(x_n) - f(x_0) = f(b)-f(a)$. ∎

**(c)** Let

$$f(x) = x + \sum_{n \in \mathbb{N},\, 1/n \le x} 2^{-n}, \qquad x \in (0,1], \qquad f(0) = 0 .$$

Both terms are non-decreasing in $x$, so $f$ is non-decreasing. At $x = 1/k$ the sum gains the term $2^{-k}$,
so $f$ has a jump of size $2^{-k}$ there; hence $f$ is discontinuous at each of the infinitely many points
$1/k$. The formula of part (b) uses only monotonicity — never continuity — and $f(1) = 1 + \sum_{n\ge1}2^{-n} = 2$
is finite, so

$$U(f,P_n) - L(f,P_n) = \frac{1}{n}\bigl(f(1) - f(0)\bigr) = \frac{2}{n} \longrightarrow 0,$$

and $f$ is integrable. This is the content of Theorem 7.9: monotone functions may have infinitely many jumps,
provided their total size $f(b)-f(a)$ is finite.

**23.** *Strategy: prove integrability by gluing the two partitions at $c$, then prove the value identity by
comparing the integrals with sums over partitions that contain $c$.*

Assume $a<c<b$, $f$ bounded on $[a,b]$, and $f$ integrable on $[a,c]$ and on $[c,b]$.

**Integrability on $[a,b]$.** Let $\varepsilon>0$. By Theorem 7.4 choose a partition $P_1$ of $[a,c]$ with
$U(f,P_1) - L(f,P_1) < \varepsilon$ and a partition $P_2$ of $[c,b]$ with $U(f,P_2) - L(f,P_2) < \varepsilon$.
Put $P = P_1 \cup P_2$; it is a partition of $[a,b]$ and its subintervals are exactly the subintervals of
$P_1$ together with those of $P_2$. Therefore

$$L(f,P) = L(f,P_1) + L(f,P_2), \qquad U(f,P) = U(f,P_1) + U(f,P_2),$$

and hence

$$U(f,P) - L(f,P) = \bigl[U(f,P_1)-L(f,P_1)\bigr] + \bigl[U(f,P_2)-L(f,P_2)\bigr] < 2\varepsilon .$$

By Theorem 7.4 (with $2\varepsilon$), $f$ is integrable on $[a,b]$.

**The value.** Put $A = \int_a^c f + \int_c^b f$. Let $P$ be a partition of $[a,b]$ containing $c$, and put
$P_1 = P \cap [a,c]$, $P_2 = P \cap [c,b]$. Then, by the definitions of the integrals on the two subintervals,

$$L(f,P) = L(f,P_1) + L(f,P_2) \le \int_a^c f + \int_c^b f = A, \qquad U(f,P) = U(f,P_1)+U(f,P_2) \ge A .$$

Now let $P$ range over **all** partitions. For an arbitrary $P$, the partition $P \cup \{c\}$ refines $P$, so
$L(f,P) \le L(f,P\cup\{c\}) \le A$ by Lemma 7.2 and the previous display. Also $L(f,P) \le \int_a^b f$ for all
$P$ by definition. Conversely, given any $P$ containing $c$ we have $L(f,P) \le A$, and these $P$ are cofinal.
Hence

$$\int_a^b f = \sup_P L(f,P) = \sup_{P \ni c} L(f,P) \le A .$$

Applying the same reasoning to upper sums, $\int_a^b f = \inf_P U(f,P) = \inf_{P\ni c}U(f,P) \ge A$. Therefore
$\int_a^b f = A$. $\blacksquare$

**24.** *Strategy: (a) estimate the difference quotient by the average of $f - f(x_0)$; (b) compute the
accumulation function of a step function; (c) integrate a bounded function over a short interval.*

**(a)** Let $f \in \mathcal{R}[a,b]$, $f$ bounded with $\lvert f\rvert \le B$, and let $x_0 \in (a,b)$ be a
continuity point of $f$. For $h \ne 0$ with $x_0 + h \in [a,b]$, additivity gives
$F(x_0+h) - F(x_0) = \int_{x_0}^{x_0+h} f$ and $\int_{x_0}^{x_0+h} f(x_0)\,dt = f(x_0)h$. Hence

$$\frac{F(x_0+h)-F(x_0)}{h} - f(x_0) = \frac1h\int_{x_0}^{x_0+h}\bigl(f(t) - f(x_0)\bigr)dt .$$

Let $\varepsilon>0$ and choose $\delta>0$ with $\lvert t - x_0\rvert < \delta \Rightarrow \lvert f(t) - f(x_0)\rvert < \varepsilon$.
For $0<\lvert h\rvert<\delta$,

$$\left\lvert \frac{F(x_0+h)-F(x_0)}{h} - f(x_0)\right\rvert \le \frac{1}{\lvert h\rvert}\int_{\min(x_0,x_0+h)}^{\max(x_0,x_0+h)}\lvert f(t)-f(x_0)\rvert\,dt \le \frac{1}{\lvert h\rvert}\cdot\varepsilon\lvert h\rvert = \varepsilon .$$

So $F'(x_0) = f(x_0)$. At $x_0 = a$ the same computation with $h>0$ only gives the right-hand derivative
$f(a)$; at $x_0 = b$ with $h<0$ it gives the left-hand derivative $f(b)$. ∎

**(b)** For the step function $f = 1$ on $[0,1)$ and $f = 2$ on $[1,2]$, additivity gives

$$F(x) = \int_0^x f = \begin{cases} x, & 0 \le x \le 1, \\ 1 + 2(x-1) = 2x - 1, & 1 < x \le 2 .\end{cases}$$

Both branches equal $1$ at $x = 1$, so $F$ is continuous there (and it is evidently continuous elsewhere, being
linear on each piece). The left-hand difference quotient at $1$ is $\frac{F(1)-F(1-h)}{h} = \frac{1-(1-h)}{h} = 1$;
the right-hand one is $\frac{F(1+h)-F(1)}{h} = \frac{(1+2h)-1}{h} = 2$. They differ, so $F'(1)$ does not exist.
Consistent with (a): $f$ is discontinuous at $1$, and exactly there the differentiability fails.

**(c)** If $\lvert f\rvert \le B$ then for $x<y$,

$$\lvert F(y) - F(x)\rvert = \left\lvert\int_x^y f\right\rvert \le \int_x^y\lvert f\rvert \le B(y-x),$$

using Theorem 7.14 and monotonicity; the case $y<x$ is symmetric. Hence $F$ is Lipschitz with constant $B$,
in particular uniformly continuous.

**25.** *Strategy: the antiderivative $F$ of the continuous $f$ exists; the chain rule makes $F\circ\varphi$
an antiderivative of $f(\varphi)\varphi'$; the product of a continuous and an integrable function is
integrable, so Theorem 7.21 applies.*

Let $J$ be an interval containing $\varphi([a,b])$, fix $u_0 \in J$ and set $F(u) = \int_{u_0}^u f$. Since
$f$ is continuous on $J$, Theorem 7.20 gives $F' = f$ on the interior of $J$.

Let $G = F\circ\varphi$. By the chain rule (valid because $F$ is differentiable on an interval containing the
range of $\varphi$ and $\varphi$ is differentiable), $G$ is differentiable on $(a,b)$ with

$$G'(t) = f(\varphi(t))\,\varphi'(t).$$

Now $f\circ\varphi$ is continuous on $[a,b]$, hence Riemann integrable by Theorem 7.8; $\varphi'$ is integrable
by hypothesis; so their product $G'$ is integrable by Theorem 7.15. Since $G$ is differentiable, it is
continuous, so all hypotheses of Theorem 7.21 hold for $G$ on $[a,b]$:

$$\int_a^b f(\varphi(t))\,\varphi'(t)\,dt = \int_a^b G' = G(b) - G(a) = F(\varphi(b)) - F(\varphi(a)).$$

On the other hand, $f$ is continuous hence integrable on the interval with endpoints $\varphi(a)$ and
$\varphi(b)$, so Theorem 7.21 applied to $F$ gives, with the orientation convention,

$$\int_{\varphi(a)}^{\varphi(b)} f(u)\,du = F(\varphi(b)) - F(\varphi(a)).$$

The right-hand sides coincide, hence so do the integrals. $\blacksquare$

*Remark.* The $C^1$ version in Theorem 7.23 is the case where $\varphi'$ is continuous. The argument above
shows that continuity of $\varphi'$ is used only to know that $G'$ is integrable, and that this follows more
generally from the integrability of $\varphi'$ together with Theorem 7.15.

**26.** *Strategy: the product rule gives $(fg)' = f'g + fg'$; each term on the right is a product of an
integrable function and a continuous one, hence integrable; apply Theorem 7.21 to $fg$.*

Suppose $f,g$ are differentiable on $[a,b]$ with $f', g' \in \mathcal{R}[a,b]$. Differentiable functions are
continuous, so $f$ and $g$ are continuous, hence integrable; and $f',g'$ are integrable by hypothesis. By
Theorem 7.15,

$$f'g \in \mathcal{R}[a,b] \quad (\text{integrable} \times \text{continuous}), \qquad fg' \in \mathcal{R}[a,b] .$$

By the product rule, $(fg)' = f'g + fg'$ everywhere on $(a,b)$, and this is integrable by Theorem 7.11. Also
$fg$ is differentiable, hence continuous on $[a,b]$, and it is an antiderivative of $(fg)'$. Theorem 7.21
therefore gives

$$\int_a^b \bigl(f'g + fg'\bigr) = (fg)(b) - (fg)(a) = f(b)g(b) - f(a)g(a).$$

By linearity (Theorem 7.11), $\int_a^b f'g + \int_a^b fg' = f(b)g(b) - f(a)g(a)$, and rearranging,

$$\int_a^b fg' = f(b)g(b) - f(a)g(a) - \int_a^b f'g . \qquad \blacksquare$$

**27.** *Strategy: uniform continuity of $g$ on the range of $f$ turns small oscillation of $f$ into small
oscillation of $g\circ f$; split the subintervals according to whether the oscillation of $f$ is small.*

Since $f$ is integrable it is bounded: $\lvert f\rvert \le B$ for some $B$, so $f([a,b]) \subseteq [-B,B]$. The
continuous function $g$ is uniformly continuous on the compact interval $[-B,B]$: given $\varepsilon>0$ there
is $\delta>0$ with

$$s,t \in [-B,B],\ \lvert s-t\rvert < \delta \ \Longrightarrow\ \lvert g(s)-g(t)\rvert < \varepsilon .$$

Choose a partition $P$ with $U(f,P) - L(f,P) < \delta\varepsilon$ (Theorem 7.4). Write $\omega_i = \omega(f,I_i)$
and split the index set into $S = \{i : \omega_i \ge \delta\}$ and its complement. On $S^c$, any two values of
$f$ on $I_i$ differ by less than $\delta$, so any two values of $g\circ f$ differ by less than $\varepsilon$;
hence $\omega(g\circ f,I_i) \le \varepsilon$. On $S$, we use the crude bound $\omega(g\circ f,I_i) \le 2M_g$,
where $M_g = \sup_{[-B,B]}\lvert g\rvert$. Also

$$\delta\sum_{i\in S}\Delta x_i \le \sum_{i\in S}\omega_i\Delta x_i \le U(f,P) - L(f,P) < \delta\varepsilon
\quad\Longrightarrow\quad \sum_{i\in S}\Delta x_i < \varepsilon .$$

Therefore

$$U(g\circ f,P) - L(g\circ f,P) \le \varepsilon\sum_{i\in S^c}\Delta x_i + 2M_g\sum_{i\in S}\Delta x_i < \varepsilon(b-a) + 2M_g\varepsilon .$$

Given $\varepsilon'>0$, first choose $\varepsilon>0$ with $\varepsilon(b-a) + 2M_g\varepsilon < \varepsilon'$, then
$\delta$ and $P$ as above. The criterion gives $g\circ f \in \mathcal{R}[a,b]$. $\blacksquare$

**28.** *Strategy: the map $x \mapsto 1/x$ is Lipschitz on $[m,\infty)$, so oscillation is controlled by the
oscillation of $f$.*

Since $f \ge m > 0$ and $f$ is bounded, $m \le f \le B$ for some $B$. For $s, t$ in a set $I$,

$$\left\lvert \frac{1}{f(s)} - \frac{1}{f(t)}\right\rvert = \frac{\lvert f(t) - f(s)\rvert}{f(s)f(t)} \le \frac{\lvert f(s)-f(t)\rvert}{m^2},$$

because $f(s)f(t) \ge m^2$. Taking suprema over $s,t \in I$,

$$\omega(1/f, I) \le \frac{1}{m^2}\,\omega(f,I).$$

Hence for every partition $P$,

$$U(1/f,P) - L(1/f,P) \le \frac{1}{m^2}\bigl[U(f,P) - L(f,P)\bigr].$$

Given $\varepsilon>0$, choose $P$ with $U(f,P)-L(f,P) < m^2\varepsilon$; then the left side is $<\varepsilon$,
and Theorem 7.4 gives $1/f \in \mathcal{R}[a,b]$. $\blacksquare$

**29.** *Strategy: (a) squeeze $fg$ between $mg$ and $Mg$ and apply the intermediate value theorem; (b) use
continuity to produce an interval where $f$ is bounded below; (c) a single-point indicator.*

**(a)** Let $m = \min_{[a,b]} f$ and $M = \max_{[a,b]} f$, which exist by the extreme value theorem. Since
$g \ge 0$, we have $mg \le fg \le Mg$ pointwise, so by monotonicity (Theorem 7.12) and Theorem 7.10,

$$m\int_a^b g = \int_a^b mg \le \int_a^b fg \le \int_a^b Mg = M\int_a^b g .$$

If $\int_a^b g = 0$, then $\int_a^b fg = 0$ and the identity $\int_a^b fg = f(c)\int_a^b g$ holds for every
$c \in [a,b]$. If $\int_a^b g > 0$, divide by it:

$$m \le \frac{\int_a^b fg}{\int_a^b g} \le M,$$

and since $f$ is continuous and attains $m$ and $M$, the intermediate value theorem gives $c \in [a,b]$ with
$f(c)$ equal to the quotient. ∎

**(b)** Suppose $f \ge 0$ is continuous and $\int_a^b f = 0$. If $f(x_0)>0$ for some $x_0$, then by continuity
there are $\eta>0$ and an interval $[u,v]$ of positive length around $x_0$ with $f \ge \eta$ on $[u,v]$. Then,
as in Exercise 14, $\int_a^b f \ge \eta(v-u) > 0$, a contradiction. Hence $f \equiv 0$. ∎

**(c)** Let $f = \mathbf{1}_{\{1/2\}}$ on $[0,1]$: it is a step function, hence integrable, with
$\int_0^1 f = 0$ (Lemma 7.26). It is non-negative and not identically zero, but it is discontinuous at
$1/2$, which is exactly the hypothesis used in (b).

**30.** *Strategy: uniform convergence bounds $\lvert f - f_n\rvert$ pointwise, hence bounds its integral; the
converse fails for $x^n$, where convergence is not uniform at $1$.*

**(a)** Let $\eta>0$ and choose $N$ with $\lvert f(t) - f_n(t)\rvert < \eta$ for all $t \in [a,b]$ and all
$n \ge N$. Then by monotonicity and the constant integral,

$$\int_a^b \lvert f - f_n\rvert \le \int_a^b \eta = \eta(b-a) < \varepsilon$$

provided $\eta < \varepsilon/(b-a)$. Hence $\int_a^b\lvert f - f_n\rvert \to 0$. ∎

**(b)** Let $f_n(x) = x^n$ and $f = 0$ on $[0,1]$. Each $f_n$ is continuous, hence integrable, and

$$\int_0^1 \lvert f - f_n\rvert = \int_0^1 x^n\,dx = \frac{1}{n+1} \longrightarrow 0 .$$

But $\sup_{[0,1]}\lvert f_n - f\rvert = \sup_{[0,1]}x^n = 1$ for every $n$, so $f_n$ does not converge to $0$
uniformly (the convergence is not uniform near $x = 1$: for $x_n = 2^{-1/n}$ we have $f_n(x_n) = \tfrac12$).
So convergence in the integral sense is strictly weaker than uniform convergence. $\blacksquare$

## Challenge

**31.** *Strategy: one direction is the quantitative refinement lemma; the other direction produces a
partition of small mesh from the hypothesis and applies the criterion.*

**Claim.** A bounded $f$ on $[a,b]$ is integrable if and only if

$$\forall \varepsilon>0\ \exists \delta>0\ \forall P:\ \lVert P\rVert<\delta \ \Longrightarrow\ U(f,P)-L(f,P)<\varepsilon .$$

**(⇒)** Assume $f$ integrable, let $\varepsilon>0$, and put $B = \sup_{[a,b]}\lvert f\rvert + 1 > 0$. By Theorem
7.4 choose $P_0$ with $U(f,P_0)-L(f,P_0) < \varepsilon/2$; let $r$ be the number of points of $P_0$ and set
$\delta = \varepsilon/(8Br)$ (any $\delta>0$ if $r=0$). Let $P$ be a partition with $\lVert P\rVert<\delta$. By
Lemma 7.6 applied with $R = P_0$,

$$U(f,P) \le U(f,P\cup P_0) + 2Br\lVert P\rVert \le U(f,P_0) + \frac{\varepsilon}{4}, \qquad
L(f,P) \ge L(f,P_0) - \frac{\varepsilon}{4}.$$

Hence $U(f,P)-L(f,P) \le \bigl[U(f,P_0)-L(f,P_0)\bigr] + \varepsilon/2 < \varepsilon$.

**(⇐)** Suppose the displayed condition holds. Given $\varepsilon>0$, take $\delta$ from it and let $P$ be any
partition with $\lVert P\rVert<\delta$ — for instance the uniform partition with $n > (b-a)/\delta$ parts. Then
$U(f,P)-L(f,P)<\varepsilon$, and since such a $P$ exists for every $\varepsilon$, Theorem 7.4 gives
integrability. $\blacksquare$

*Remark.* The point of the mesh form is that it is *uniform in the partition*: no knowledge of $f$ is needed
beyond $\lVert P\rVert$, which is what a numerical algorithm actually controls. Note that the $\delta$ depends
on $f$ (through $r$ and $B$), and that the direction (⇒) is not a triviality — it is Lemma 7.6 that converts
"some partition is good" into "all sufficiently fine partitions are good".

**32.** *Strategy: (⇒) use the step functions built from the infima and suprema of a good partition;
(⇐) squeeze the Darboux sums of a partition refining both step functions.*

**(⇒)** Let $f$ be integrable. For each $k \in \mathbb{N}$ choose a partition $P_k = \{x_0^{(k)},\dots,x_{n_k}^{(k)}\}$
with $U(f,P_k) - L(f,P_k) < 1/k$ (Theorem 7.4). Define step functions

$$s_k(t) = m_i(f,P_k), \quad t \in [x_{i-1}^{(k)}, x_i^{(k)}), \qquad t_k(t) = M_i(f,P_k), \quad t \in [x_{i-1}^{(k)}, x_i^{(k)}),$$

with arbitrary values at $b$. By definition of infimum and supremum, $s_k \le f \le t_k$ everywhere. Each is a
step function, so by Lemma 7.26,

$$\int_a^b (t_k - s_k) = \sum_i \bigl(M_i(f,P_k) - m_i(f,P_k)\bigr)\Delta x_i = U(f,P_k) - L(f,P_k) < \frac1k \longrightarrow 0 .$$

**(⇐)** Suppose $s_k \le f \le t_k$ with $\int(t_k - s_k) \to 0$. Let $\varepsilon>0$ and choose $k$ with
$\int_a^b(t_k - s_k) < \varepsilon$. Let $P$ be a partition refining both the partition of $s_k$ and that of
$t_k$. On each subinterval $I$ of $P$, $s_k$ and $t_k$ are constant; writing $c_I$ and $C_I$ for those values,

$$\inf_I f \ge \inf_I s_k = c_I, \qquad \sup_I f \le \sup_I t_k = C_I .$$

Hence

$$U(f,P) - L(f,P) = \sum_{I \in P}\bigl(\sup_I f - \inf_I f\bigr)\lvert I\rvert \le \sum_{I\in P}(C_I - c_I)\lvert I\rvert = \int_a^b (t_k - s_k) < \varepsilon .$$

By Theorem 7.4, $f$ is integrable. $\blacksquare$

*Remark.* The condition is a "squeezing by step functions" criterion. It is strictly weaker than being a
uniform limit of step functions (which would force $f$ to be a uniform limit of functions constant on
intervals, and such a limit is a regulated function, not an arbitrary integrable one). Thomae's function
satisfies the criterion — the step functions of Proposition 7.28's construction squeeze it — yet it is
discontinuous at every rational.

**33.** *Strategy: compute each integral from Lemma 7.26, verify pointwise convergence at each point
separately (including $x=0$), and identify the failing hypothesis.*

Each $f_n$ is constant on the open intervals of the partition $\{0, 1/n, 1\}$ (value $n$ on $(0,1/n)$, value
$0$ on $(1/n,1)$), so it is a step function and, by Lemma 7.26,

$$\int_0^1 f_n = n\cdot\frac1n + 0\cdot\Bigl(1 - \frac1n\Bigr) = 1 .$$

*Pointwise convergence.* Fix $x \in [0,1]$. If $x = 0$ then $f_n(0) = 0$ for all $n$. If $x>0$, choose
$N > 1/x$; then for all $n \ge N$ we have $1/n < x$, so $x \notin (0,1/n)$ and $f_n(x) = 0$. Hence
$f_n(x) \to 0$ for every $x$, i.e. $f_n \to 0$ pointwise.

Yet $\int_0^1 f_n = 1$ for every $n$, so $\int_0^1 f_n \to 1 \ne 0 = \int_0^1 0$. The hypothesis that fails
is *uniform* convergence: $\sup_{[0,1]}\lvert f_n\rvert = n \to \infty$, so the convergence is as far from
uniform as possible. Theorem 7.30 therefore does not apply, and indeed its conclusion is false here.

*Remark.* The example also shows that no domination by an integrable function is available: the functions are
bounded by $n$, and any function dominating all of them is unbounded, hence not Riemann integrable. This is
precisely the hypothesis that Lebesgue's dominated convergence theorem supplies in the measure-theoretic
setting.

**34.** *Strategy: (⇒) a large oscillation on a set of large length forces a large gap; (⇐) sum the gap over
the two classes of subintervals, using that the "bad" ones have small total length and the "good" ones have
small oscillation.*

**Claim.** A bounded $f$ on $[a,b]$ is integrable if and only if

$$\forall \varepsilon>0\ \forall \eta>0\ \exists P:\ \sum_{i:\,\omega(f,I_i)\ge\varepsilon}\Delta x_i < \eta .$$

**(⇒)** Suppose $f$ is integrable, and let $\varepsilon,\eta>0$. Choose $P$ with $U(f,P)-L(f,P) < \varepsilon\eta$.
Let $S = \{i : \omega(f,I_i)\ge\varepsilon\}$. Then

$$\varepsilon\sum_{i\in S}\Delta x_i \le \sum_{i\in S}\omega(f,I_i)\Delta x_i \le U(f,P)-L(f,P) < \varepsilon\eta,$$

so $\sum_{i\in S}\Delta x_i < \eta$. ∎

**(⇐)** Suppose the condition holds, and let $\varepsilon'>0$. Let $B>0$ bound $\lvert f\rvert$, so that every
$\omega(f,I_i)\le 2B$. Apply the condition with $\varepsilon = \varepsilon'/(2(b-a))$ and
$\eta = \varepsilon'/(4B)$: there is a partition $P$ for which the subintervals with
$\omega(f,I_i)\ge\varepsilon$ have total length less than $\eta$. Splitting the gap into the two classes,

$$U(f,P)-L(f,P) = \sum_{\omega_i<\varepsilon}\omega_i\Delta x_i + \sum_{\omega_i\ge\varepsilon}\omega_i\Delta x_i \le \varepsilon(b-a) + 2B\eta < \frac{\varepsilon'}{2} + \frac{\varepsilon'}{2} = \varepsilon' .$$

By Theorem 7.4, $f$ is integrable. $\blacksquare$

*Remark.* This is Riemann's original formulation. It says that integrability is the statement that the set
where the oscillation exceeds any fixed level can be covered by intervals of arbitrarily small total length —
the first appearance of the idea of a set of measure zero, which is exactly what Lebesgue's criterion makes
precise (Remark 7.31).

**35.** *Strategy: differentiate by the product and chain rules away from $0$ and by the definition at $0$;
then produce a sequence along which the derivative tends to infinity, and invoke Proposition 7.18.*

**(a)** For $x \ne 0$, the function $x \mapsto x^2\sin(1/x^2)$ is a composition and product of differentiable
functions, so

$$F'(x) = 2x\sin\frac{1}{x^2} + x^2\cos\frac{1}{x^2}\cdot\left(-\frac{2}{x^3}\right) = 2x\sin\frac{1}{x^2} - \frac{2}{x}\cos\frac{1}{x^2}.$$

At $x = 0$, the difference quotient is

$$\frac{F(h) - F(0)}{h} = \frac{h^2\sin(1/h^2)}{h} = h\sin\frac{1}{h^2},$$

and $\lvert h\sin(1/h^2)\rvert \le \lvert h\rvert \to 0$ as $h\to0$. Hence $F'(0) = 0$ and $F$ is
differentiable everywhere on $[-1,1]$.

**(b)** Take $x_n = (2\pi n)^{-1/2}$, so $1/x_n^2 = 2\pi n$ and therefore $\cos(1/x_n^2) = 1$,
$\sin(1/x_n^2) = 0$. Then

$$F'(x_n) = 0 - \frac{2}{x_n}\cdot 1 = -2\sqrt{2\pi n} \longrightarrow -\infty .$$

So $F'$ is unbounded on $[-1,1]$; by Proposition 7.18 it is not Riemann integrable on $[-1,1]$.

**(c)** Theorem 7.21 requires $f = F'$ to be Riemann integrable on $[-1,1]$, and by (b) it is not. Hence the
identity $\int_{-1}^1 F' = F(1) - F(-1)$ has no meaning as a Riemann-integral statement: the left-hand side
does not exist. What fails is not the fundamental theorem but its hypothesis.

*Remark.* The improper integral does converge here, because $F$ is continuous at $0$:
$\int_{-1}^{-\delta}F' = F(-\delta) - F(-1) \to F(0) - F(-1)$ and $\int_{\delta}^{1} F' = F(1) - F(\delta) \to F(1) - F(0)$
as $\delta\downarrow0$, so the sum tends to $F(1) - F(-1)$. This is a striking illustration that the improper
integral is a different object from the Riemann integral, defined by a limit of integrals over intervals on
which $F'$ *is* bounded and integrable.

**36.** *Strategy: approximate $f$ from below by the step function built from the infima of a good partition,
then round its corners off by linear interpolation.*

Let $f \in \mathcal{R}[a,b]$ and $\varepsilon>0$. By Theorem 7.4 there is a partition
$P = \{x_0,\dots,x_n\}$ with $U(f,P) - L(f,P) < \varepsilon/2$. Let $B = \sup_{[a,b]}\lvert f\rvert + 1$ and
define the step function

$$s(t) = m_i(f,P) \quad \text{for } t \in (x_{i-1}, x_i), \qquad s(x_i) = m_i \ (i \ge 1), \qquad s(x_0) = m_1 .$$

Then $s \le f$ on $(x_{i-1},x_i)$ and $\lvert s\rvert \le B$. Therefore, by Lemma 7.26 and monotonicity,

$$\int_a^b \lvert f - s\rvert = \int_a^b (f - s) = \int_a^b f - \int_a^b s = \sum_{i=1}^n\int_{I_i}\bigl(f - m_i\bigr) \le \sum_{i=1}^n \bigl(M_i - m_i\bigr)\Delta x_i = U(f,P)-L(f,P) < \frac{\varepsilon}{2}.$$

Now make $s$ continuous. For each interior partition point $x_i$ choose $\delta_i>0$ so small that the intervals
$(x_i - \delta_i, x_i + \delta_i)$ are disjoint and lie inside $(a,b)$, and so small that
$\sum_i 2\delta_i < \varepsilon/(8B)$. Define $h$ to agree with $s$ outside the union of these intervals and to
be linear (interpolating between the two constant values) on each $(x_i-\delta_i,x_i)$ and
$(x_i, x_i+\delta_i)$, and set $h = s$ near $a$ and $b$. Then $h$ is continuous on $[a,b]$, and $h \ne s$ only
on a set of total length less than $\varepsilon/(4B)$, where both are bounded by $B$ in absolute value. Hence

$$\int_a^b \lvert s - h\rvert \le 2B\cdot\frac{\varepsilon}{4B} = \frac{\varepsilon}{2}.$$

Combining, $\int_a^b\lvert f - h\rvert \le \int_a^b\lvert f - s\rvert + \int_a^b\lvert s - h\rvert < \varepsilon$. $\blacksquare$

*Why the uniform version fails.* If $\sup_{[a,b]}\lvert f - h\rvert < \varepsilon$ with $h$ continuous and
$\varepsilon \le \tfrac12$, then $f$ would be a uniform limit of continuous functions (take $\varepsilon = 1/k$),
hence continuous. So an integrable discontinuous function cannot be uniformly approximated by continuous
functions. For $f = \mathbf{1}_{[0,1/2]}$ on $[0,1]$ and any continuous $h$, taking $x_n \uparrow \tfrac12$ and
$y_n \downarrow \tfrac12$ gives

$$\lvert f(x_n) - h(x_n)\rvert + \lvert f(y_n)-h(y_n)\rvert \longrightarrow \lvert 1 - h(\tfrac12)\rvert + \lvert h(\tfrac12)\rvert \ge 1,$$

so $\sup\lvert f - h\rvert \ge \tfrac12$ for every continuous $h$. The integral norm, unlike the sup norm,
does not see a single jump, which is why the $L^1$ statement is the right one.
