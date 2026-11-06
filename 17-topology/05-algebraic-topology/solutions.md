# Introduction to Algebraic Topology — Solutions

> [Introduction to Algebraic Topology](README.md) · Solutions to the 37 problems in [exercises.md](exercises.md)

Each solution states the strategy, then verifies every hypothesis before quoting a theorem. Computations of
degrees are done by writing down lifts, computations of fundamental groups by exhibiting deformation
retractions or by van Kampen, and computations of Euler characteristics by counting cells.

## Beginner

**1.** *Strategy: copy the three constructions of Proposition 7.1.1 and check continuity of the glued
homotopy with the pasting lemma for closed sets.*

*Reflexive.* $H : X\times I\to Y$, $H(x,t) = f(x)$, is continuous (it is the composite of the projection
$X\times I\to X$ with $f$) and $H(x,0) = H(x,1) = f(x)$.

*Symmetric.* If $H$ joins $f$ to $g$, put $\tilde H(x,t) = H(x,1-t)$. The map $(x,t)\mapsto (x,1-t)$ is
continuous, so $\tilde H$ is continuous; $\tilde H(x,0) = H(x,1) = g(x)$ and $\tilde H(x,1) = H(x,0) = f(x)$.

*Transitive.* Let $H_1$ join $f$ to $g$ and $H_2$ join $g$ to $h$. Define

$$H(x,t) = \begin{cases} H_1(x,2t), & 0\le t\le \tfrac12,\\ H_2(x,2t-1), & \tfrac12\le t\le1.\end{cases}$$

The sets $A = X\times[0,\tfrac12]$ and $B = X\times[\tfrac12,1]$ are closed in $X\times I$ and cover it; $H|_A$
and $H|_B$ are continuous (composites of continuous maps with the continuous maps $(x,t)\mapsto(x,2t)$ and
$(x,t)\mapsto(x,2t-1)$); and they agree on $A\cap B = X\times\{\tfrac12\}$, where both equal $g(x)$. By the
pasting lemma for a finite closed cover, $H$ is continuous. Its values at $t=0$ and $t=1$ are $f(x)$ and
$h(x)$. If all homotopies are constant on $A_0\subseteq X$, so is $H$. $\blacksquare$

**2.** *Strategy: the straight-line homotopy stays in a convex set.*

Define $H(x,t) = (1-t)f(x)+tg(x)$. For each fixed $(x,t)$ this is a convex combination of two points of $C$,
hence lies in $C$; $H$ is continuous because addition and scalar multiplication in $\mathbb{R}^n$ are
continuous; and $H(x,0) = f(x)$, $H(x,1) = g(x)$.

For $\mathbb{R}^n$: taking $X = \mathbb{R}^n$, $f = \operatorname{id}$, $g$ the constant map at $0$ gives
$H(x,t) = (1-t)x$, a homotopy from the identity to a constant, so $\mathbb{R}^n$ is contractible. The same
formula with $C = D^n$ (also convex, and $0\in D^n$) shows $D^n$ is contractible. $\blacksquare$

**3.** *Strategy: the image of a connected set under a continuous map is connected, and a discrete space has
no non-trivial connected subsets.*

Let $\gamma : I\to X$ be a path. $I$ is connected, so $\gamma[I]$ is connected (Theorem 7.4.1 of
[Connectedness](../04-connectedness/README.md)); a connected subset of a discrete space is a single point
(Proposition 7.1.4 of [Connectedness](../04-connectedness/README.md)). So $\gamma$ is constant, and every loop
at $x_0$ is the constant loop at $x_0$. Hence $\pi_1(X,x_0)$ has exactly one element, the class of the constant
loop, which is therefore the trivial group. $\blacksquare$

**4.** *Strategy: compute the reverse of a concatenation pointwise; here the two paths are equal, not merely
homotopic.*

For $0\le s\le\frac12$: $\overline{\gamma*\delta}(s) = (\gamma*\delta)(1-s)$ with $1-s\ge\frac12$, so
$(\gamma*\delta)(1-s) = \delta(2(1-s)-1) = \delta(1-2s) = \bar\delta(2s)$.

For $\frac12\le s\le1$: $1-s\le\frac12$, so $(\gamma*\delta)(1-s) = \gamma(2(1-s)) = \gamma(2-2s) =
\bar\gamma(2s-1)$.

The right-hand sides are exactly the two pieces defining $\bar\delta*\bar\gamma$. Hence
$\overline{\gamma*\delta} = \bar\delta*\bar\gamma$ as paths, so in particular they are path homotopic.
$\blacksquare$

**5.** *Strategy: contract the two halves of the loop simultaneously in the parameter $t$, using the explicit
homotopy of Theorem 7.3.2.*

Here $\gamma(s) = e^{2\pi i s}$ and $\delta = \bar\gamma$. The concatenation $\gamma*\delta$ equals
$s\mapsto\gamma(2s)$ for $s\le\frac12$ and $s\mapsto \gamma(2-2s)$ for $s\ge\frac12$. Define

$$H(s,t) = \begin{cases} \gamma\bigl((1-t)\,2s\bigr), & 0\le s\le\tfrac12,\\[2pt]
\gamma\bigl((1-t)(2-2s)\bigr), & \tfrac12\le s\le 1.\end{cases}$$

Both pieces agree at $s = \tfrac12$ (both give $\gamma(1-t)$), so $H$ is continuous. Moreover
$H(s,0) = \gamma(2s)$ or $\gamma(2-2s)$, i.e. $(\gamma*\delta)(s)$; $H(s,1) = \gamma(0) = 1$;
$H(0,t) = \gamma(0) = 1$ and $H(1,t) = \gamma(0) = 1$. Hence $\gamma*\delta\simeq_p c_1$. The same formula
with $\gamma$ replaced by $\bar\gamma$ shows $\delta*\gamma\simeq_p c_1$. Therefore
$[\gamma][\delta] = [\delta][\gamma] = [c_1]$: the class $[\gamma]$ is invertible with inverse
$[\delta] = [\gamma]^{-1}$, as the group axioms require. $\blacksquare$

**6.** *Strategy: straight-line contraction to the basepoint.*

$H(s,t) = (1-t)\gamma(s) + tx_0$. Convexity gives $H(s,t)\in C$; continuity is clear. Then
$H(s,0) = \gamma(s)$, $H(s,1) = x_0$, and $H(0,t) = (1-t)x_0+tx_0 = x_0 = H(1,t)$ since
$\gamma(0) = \gamma(1) = x_0$. So $H$ is a path homotopy from $\gamma$ to the constant loop at $x_0$.
$\blacksquare$

**7.** *Strategy: enumerate the loops.*

If $X = \{x_0\}$, the only map $I\to X$ is the constant one, so there is exactly one path homotopy class; the
group is trivial.

If $X = \{a,b\}$ is discrete, every path is constant (Exercise 3). Hence the only loop based at $a$ is the
constant loop, and $\pi_1(X,a) = \{1\}$; similarly at $b$. Note that $X$ is disconnected, so this does not
contradict the fact that $\pi_1$ of a path connected space is independent of the basepoint. $\blacksquare$

**8.** *Strategy: write the lifts.*

$\gamma_n(s) = e^{2\pi i n s}$ has the lift $\tilde\gamma_n(s) = ns$ with $\tilde\gamma_n(0) = 0$. So
$\deg\gamma_n = n - 0 = n$.

$\bar\gamma_n(s) = e^{-2\pi i n s}$ has the lift $\tilde{\bar\gamma}_n(s) = -ns$, so
$\deg\bar\gamma_n = -n$.

$\gamma_n*\bar\gamma_n$ has the lift $\tilde\gamma_n * \tilde{\bar\gamma}_n$: it runs from $0$ to $n$ during
the first half and back from $n$ to $0$ during the second half. Its endpoint is $0$, so
$\deg(\gamma_n*\bar\gamma_n) = 0$. Consistently, $\deg(\gamma_n*\bar\gamma_n) = \deg\gamma_n +
\deg\bar\gamma_n = n + (-n) = 0$, and indeed this loop is null-homotopic by Exercise 5. $\blacksquare$

**9.** *Strategy: exhibit a continuous function $\theta$ with $\gamma = e^{2\pi i\theta}$ and $\theta(0) = 0$;
then $\deg\gamma = \theta(1)$.*

(a) $\theta(t) = 3t + \sin 2\pi t$ is continuous, satisfies $\theta(0) = 0$ and $\theta(1) = 3$. Hence
$e^{2\pi i\theta(t)} = \gamma(t)$ and $\deg\gamma = 3$.

(b) $\theta(t) = 5t^2$ is continuous with $\theta(0) = 0$, $\theta(1) = 5$, and
$e^{2\pi i\theta(t)} = e^{2\pi i\cdot 5t^2} = \eta(t)$. Hence $\deg\eta = 5$.

(c) For $\gamma\eta$ (pointwise product), $\theta(t) = 3t+\sin 2\pi t + 5t^2$ satisfies
$e^{2\pi i\theta(t)} = \gamma(t)\eta(t)$, $\theta(0) = 0$, $\theta(1) = 3+0+5 = 8$. Hence
$\deg(\gamma\eta) = 8 = \deg\gamma + \deg\eta$, in accordance with additivity. $\blacksquare$

**10.** *Strategy: verify the deformation retraction and identify the homotopy.*

Define $r : \mathbb{R}^n\setminus\{0\}\to S^{n-1}$ by $r(x) = x/\lVert x\rVert$; this is continuous (the
denominator is a non-vanishing continuous function) and $r(x) = x$ for $\lVert x\rVert = 1$, so $r$ is a
retraction. Define

$$H(x,t) = (1-t)x + t\,\frac{x}{\lVert x\rVert} = x\Bigl((1-t) + \frac{t}{\lVert x\rVert}\Bigr).$$

The scalar factor is a convex combination of $1$ and $1/\lVert x\rVert > 0$, hence is $\ge
\min\{1,1/\lVert x\rVert\} > 0$, so $H(x,t)\neq0$ and $H$ takes values in $\mathbb{R}^n\setminus\{0\}$. It is
continuous, $H(x,0) = x$, $H(x,1) = r(x)$, and for $\lVert x\rVert = 1$ the factor equals $1$, so
$H(x,t) = x$: the homotopy is relative to $S^{n-1}$. Hence $r$ is a deformation retraction, and by
Proposition 7.1.6 and Corollary 7.5.4, $\pi_1(\mathbb{R}^n\setminus\{0\})\cong\pi_1(S^{n-1})$ for $n\ge1$ (for
$n=1$ this says $\pi_1(\mathbb{R}\setminus\{0\}) = \pi_1(S^0)$, both trivial). $\blacksquare$

## Intermediate

**11.** *Strategy: (a) post-compose the homotopy; (b) compare the two piecewise definitions.*

*Well defined.* If $\gamma\simeq_p\gamma'$ via $H : I\times I\to X$, then $f\circ H : I\times I\to Y$ is
continuous and satisfies $f\circ H(s,0) = f(\gamma(s))$, $f\circ H(s,1) = f(\gamma'(s))$, and
$f\circ H(0,t) = f(\gamma(0)) = f(\gamma'(0))$, $f\circ H(1,t) = f(\gamma(1))$; so $f\circ\gamma\simeq_p
f\circ\gamma'$.

*Homomorphism.* Let $\gamma,\delta$ be loops at $x_0$. By definition,
$(f\circ(\gamma*\delta))(s)$ equals $f(\gamma(2s))$ for $s\le\frac12$ and $f(\delta(2s-1))$ for
$s\ge\frac12$. The concatenation $(f\circ\gamma)*(f\circ\delta)$ has exactly the same two pieces. Hence
$f\circ(\gamma*\delta) = (f\circ\gamma)*(f\circ\delta)$ as paths, and therefore

$$f_*([\gamma][\delta]) = [f\circ(\gamma*\delta)] = [(f\circ\gamma)*(f\circ\delta)] =
[f\circ\gamma]\,[f\circ\delta] = f_*([\gamma])\,f_*([\delta]). \quad\blacksquare$$

**12.** *Strategy: both sides act by composing with the same map.*

For a loop $\gamma$ at $x_0$ and composable continuous maps $f : X\to Y$, $g : Y\to Z$:

$$(g\circ f)_*([\gamma]) = [g\circ f\circ\gamma] = g_*\bigl([f\circ\gamma]\bigr) =
g_*\bigl(f_*([\gamma])\bigr) = (g_*\circ f_*)([\gamma]).$$

Also $(\operatorname{id}_X)_*([\gamma]) = [\operatorname{id}_X\circ\gamma] = [\gamma]$. Since the classes
$[\gamma]$ generate $\pi_1(X,x_0)$, the identities of homomorphisms follow. $\blacksquare$

**13.** *Strategy: feed the loop into the homotopy.*

Let $\gamma$ be a loop at $x_0$ and define $K(s,t) = H(\gamma(s),t)$. It is continuous. Then
$K(s,0) = f(\gamma(s))$ and $K(s,1) = g(\gamma(s))$; moreover
$K(0,t) = H(\gamma(0),t) = H(x_0,t) = f(x_0)$, and $H(x_0,1) = g(x_0)$, so the hypothesis gives
$f(x_0) = g(x_0)$ and $K(0,t) = K(1,t) = f(x_0)$. Hence $K$ is a path homotopy from $f\circ\gamma$ to
$g\circ\gamma$, and $f_*([\gamma]) = g_*([\gamma])$. $\blacksquare$

**14.** *Strategy: conjugation by a path, with the group laws of Theorem 7.3.2 doing the work.*

Define $\gamma_\#([\alpha]) = [\gamma*\alpha*\bar\gamma]$ for a loop $\alpha$ at $x_1$; this is a loop at $x_0$.

*Well defined:* if $\alpha\simeq_p\alpha'$, then by Lemma 7.2.3 the loops
$\gamma*\alpha*\bar\gamma$ and $\gamma*\alpha'*\bar\gamma$ are path homotopic.

*Homomorphism:* let $\alpha,\beta$ be loops at $x_1$. Using associativity and
$\bar\gamma*\gamma\simeq_p c_{x_1}$,

$$\gamma_\#([\alpha])\,\gamma_\#([\beta])
= [\gamma*\alpha*\bar\gamma]\,[\gamma*\beta*\bar\gamma]
= [\gamma*\alpha*\bar\gamma*\gamma*\beta*\bar\gamma]
\simeq_p [\gamma*\alpha*\beta*\bar\gamma]
= \gamma_\#([\alpha][\beta]).$$

*Inverse:* the same computation with $\gamma$ replaced by $\bar\gamma$ gives
$\bar\gamma_\#\circ\gamma_\# = \operatorname{id}$ and
$\gamma_\#\circ\bar\gamma_\# = \operatorname{id}$. Hence $\gamma_\#$ is an isomorphism with inverse
$\bar\gamma_\#$. $\blacksquare$

**15.** *Strategy: a loop in a product is a pair of loops, and so is a homotopy.*

Let $p_1 : X\times Y\to X$ and $p_2 : X\times Y\to Y$ be the projections. Define

$$\Phi : \pi_1(X\times Y,(x_0,y_0))\to\pi_1(X,x_0)\times\pi_1(Y,y_0), \qquad
\Phi([\gamma]) = \bigl((p_1)_*[\gamma], (p_2)_*[\gamma]\bigr).$$

*Well defined and a homomorphism:* each $(p_i)_*$ is (Theorem 7.5.2), and a map into a product of groups is a
homomorphism iff its components are.

*Bijective.* Write $\gamma(t) = (\gamma_1(t),\gamma_2(t))$ with $\gamma_i = p_i\circ\gamma$. The map
$\Psi([\alpha],[\beta]) = [\eta]$ where $\eta(t) = (\alpha(t),\beta(t))$ is well defined: a pair of path
homotopies $(\alpha\simeq_p\alpha')$, $(\beta\simeq_p\beta')$ assembles, by continuity of maps into a product,
into a path homotopy $\eta\simeq_p\eta'$. Since a map into a product is continuous iff both components are,
$\eta$ is a loop at $(x_0,y_0)$; and $\Phi\circ\Psi\bigl(([\alpha],[\beta])\bigr) = ([\alpha],[\beta])$,
$\Psi\circ\Phi([\gamma]) = [\gamma]$. So $\Phi$ is a bijective homomorphism, i.e. an isomorphism.
$\blacksquare$

**16.** *Strategy: apply Exercise 15 with the fundamental group of the circle and of an interval.*

$\pi_1(T^2,(1,1))\cong\pi_1(S^1,1)\times\pi_1(S^1,1)\cong\mathbb{Z}\times\mathbb{Z} = \mathbb{Z}^2$ by
Exercise 15 and Theorem 7.6.4.

For the cylinder, $\pi_1(S^1\times[0,1])\cong\mathbb{Z}\times\pi_1([0,1])\cong\mathbb{Z}\times1\cong\mathbb{Z}$
because $[0,1]$ is convex, hence simply connected (Proposition 7.4.3). $\blacksquare$

**17.** *Strategy: guess the lift and verify the two defining properties.*

(a) $\gamma(t) = e^{2\pi i t^2}$. The map $\tilde\gamma(t) = t^2$ is continuous,
$p(\tilde\gamma(t)) = e^{2\pi i t^2} = \gamma(t)$, and $\tilde\gamma(0) = 0$. By uniqueness of lifts
(Lemma 7.6.1) it is *the* lift. Its endpoint is $\tilde\gamma(1) = 1$, so $\deg\gamma = 1$.

(b) $\gamma(t) = e^{2\pi i\sqrt t}$. The map $\tilde\gamma(t) = \sqrt t$ is continuous on $[0,1]$,
$p\circ\tilde\gamma = \gamma$ and $\tilde\gamma(0) = 0$; the endpoint is $1$, so $\deg\gamma = 1$. (Both loops
wind once, as expected: the reparametrisation $t\mapsto t^2$ or $t\mapsto\sqrt t$ does not change the degree,
in accordance with Lemma 7.2.2 and Lemma 7.6.3(a).) $\blacksquare$

**18.** *Strategy: lift a null-homotopy and read off that the lifted loop is null-homotopic.*

Let $\tilde\gamma$ be a loop at $\tilde x_0$ and suppose $p_*[\tilde\gamma] = 1$, i.e. $p\circ\tilde\gamma$ is
path homotopic to the constant loop at $x_0$. Let $H : I\times I\to X$ be such a homotopy. By the homotopy
lifting theorem (Theorem 7.7.3, with $Y = I$ and initial lift $\tilde\gamma$) there is a lift
$\tilde H : I\times I\to\tilde X$ with $\tilde H(s,0) = \tilde\gamma(s)$.

Since $H(0,t) = H(1,t) = x_0$ and $H(0,0) = x_0$, the paths $t\mapsto\tilde H(0,t)$ and
$t\mapsto\tilde H(1,t)$ lift the constant path at $x_0$; by uniqueness of path lifting they are constant (equal
to $\tilde H(0,0) = \tilde x_0$ and to $\tilde H(1,0) = \tilde\gamma(1) = \tilde x_0$ respectively). Hence
$\tilde H$ is a path homotopy from $\tilde\gamma$ to a constant loop, so $[\tilde\gamma] = 1$. Therefore
$\ker p_* = \{1\}$. $\blacksquare$

**19.** *Strategy: assemble Lemma 7.6.3 and the contractibility of $\mathbb{R}$.*

*Surjective homomorphism:* Lemma 7.6.3(b) gives additivity, i.e. $\deg$ is a homomorphism; Lemma 7.6.3(c)
gives $\deg\gamma_n = n$, so it is onto.

*Kernel.* Suppose $\deg\gamma = 0$ and take the lift with $\tilde\gamma(0) = 0$. Then
$\tilde\gamma(1) = \deg\gamma = 0$, so $\tilde\gamma$ is a loop at $0$ in $\mathbb{R}$. Since $\mathbb{R}$ is
convex, $H(s,t) = (1-t)\tilde\gamma(s)$ is a path homotopy from $\tilde\gamma$ to the constant loop
(Exercise 6). Composing with $p$ gives a path homotopy from $p\circ\tilde\gamma = \gamma$ to the constant loop
at $1$. So $\ker\deg = \{[c_1]\}$.

*Conclusion.* A surjective homomorphism with trivial kernel is an isomorphism, so
$\pi_1(S^1,1)\cong\mathbb{Z}$. $\blacksquare$

**20.** *Strategy: translate null-homotopy into the vanishing of the induced map on $\pi_1$ and use that
$\pi_1(S^1)$ is generated by the class of $\gamma_1(s) = e^{2\pi i s}$.*

If $f$ is null-homotopic, say $f\simeq c$ with $c$ constant, then $f\circ\gamma_1$ is freely homotopic to a
constant loop; a free homotopy class of loops is a conjugacy class in $\pi_1(S^1,f(1))$, and $\pi_1$ is
abelian, so the class of $f\circ\gamma_1$ is trivial and $\deg f = 0$. (Equivalently, $f_*$ factors through
$\pi_1$ of a point and is therefore zero.)

Conversely, suppose $\deg f = 0$. Then $f_*([\gamma_1]) = [f\circ\gamma_1]$ is trivial, and since
$[\gamma_1]$ generates $\pi_1(S^1,1) = \mathbb{Z}$, the homomorphism $f_*$ is zero. But
$f_*([\gamma_1]) = [f\circ\gamma_1] = [f]$ under the identification of maps $S^1\to S^1$ with loops at $f(1)$;
so $[f] = 1$ in $\pi_1(S^1,f(1))$, i.e. $f$ is homotopic to the constant map rel basepoint, in particular
null-homotopic. $\blacksquare$

## Advanced

**21.** *Strategy: a fixed-point-free self-map of the disc would produce a retraction onto the circle, which
$\pi_1$ forbids.*

Suppose $f : D^2\to D^2$ is continuous with $f(x)\neq x$ for all $x$. Put $v(x) = x - f(x)\neq0$ and let
$r(x) = x + t(x)v(x)$ where $t(x)\ge0$ is chosen so that $\lVert r(x)\rVert = 1$.

*Existence and uniqueness of $t(x)$.* The quadratic
$q(t) = \lVert x + tv(x)\rVert^2 - 1 = \lVert v(x)\rVert^2t^2 + 2\langle x,v(x)\rangle t + \lVert x\rVert^2-1$
satisfies $q(0) = \lVert x\rVert^2 - 1\le0$ and $q(t)\to+\infty$ as $t\to+\infty$. The product of the two roots
is $(\lVert x\rVert^2-1)/\lVert v(x)\rVert^2\le0$, so the roots have opposite signs or one is zero; hence there
is exactly one non-negative root. Solving,

$$t(x) = \frac{-\langle x,v(x)\rangle + \sqrt{\langle x,v(x)\rangle^2 + \lVert v(x)\rVert^2
\bigl(1-\lVert x\rVert^2\bigr)}}{\lVert v(x)\rVert^2}.$$

*Continuity.* The function $x\mapsto\lVert v(x)\rVert = \lVert x - f(x)\rVert$ is continuous and strictly
positive on the compact set $D^2$, so it has a positive minimum $\delta$; both numerator and denominator are
continuous and the denominator is bounded below by $\delta^2 > 0$. Hence $t$ is continuous and $r$ is
continuous.

*$r$ is a retraction.* By construction $\lVert r(x)\rVert = 1$, so $r$ maps into $S^1$. If $x\in S^1$, then
$q(0) = 0$ and the other root is $-2\langle x,v(x)\rangle/\lVert v(x)\rVert^2 \le 0$ (as
$\langle x,v(x)\rangle = \langle x, x\rangle - \langle x,f(x)\rangle \ge \lVert x\rVert^2 -
\lVert x\rVert\lVert f(x)\rVert \ge 0$), so the non-negative root is $0$ and $r(x) = x$.

*Contradiction.* So $r : D^2\to S^1$ satisfies $r\circ i = \operatorname{id}_{S^1}$, where $i$ is the
inclusion. Applying $\pi_1$: $r_*\circ i_* = \operatorname{id}_\mathbb{Z}$. But $D^2$ is convex, so
$\pi_1(D^2) = 1$ and $i_* : \mathbb{Z}\to1$ is zero, hence $r_*\circ i_* = 0\neq\operatorname{id}_\mathbb{Z}$.
Contradiction. Hence $f$ has a fixed point. $\blacksquare$

**22.** *Strategy: the loop $p(re^{2\pi is})$ has degree $n$ for large $r$, but as the image of a loop in the
contractible space $\mathbb{C}$ it must have degree $0$.*

Let $p(z) = z^n + a_{n-1}z^{n-1}+\cdots+a_0$ with $n\ge1$, and suppose $p(z)\neq0$ for every $z$.
By Corollary 7.5.5, $\pi_1(\mathbb{C}) = 1$, so $p_* : \pi_1(\mathbb{C})\to\pi_1(\mathbb{C}^\times)$ is the
trivial homomorphism.

Choose $r>0$ so large that $\sum_{k=0}^{n-1}\lvert a_k\rvert r^k < r^n$; this is possible because the left
side is a polynomial in $r$ of degree $n-1$. On the circle $\lvert z\rvert = r$,
$\lvert p(z) - z^n\rvert \le \sum_{k<n}\lvert a_k\rvert r^k < r^n = \lvert z^n\rvert$, so
$p(z)\neq0$.

Define $H(s,t) = p(re^{2\pi is}) - t\sum_{k=0}^{n-1}a_k (re^{2\pi is})^k$. Then
$H(s,0) = p(re^{2\pi is})$ and $H(s,1) = (re^{2\pi is})^n$, and
$\lvert H(s,t)\rvert \ge \lvert (re^{2\pi is})^n\rvert - t\sum_k\lvert a_k\rvert r^k > r^n - r^n = 0$; so $H$
is a homotopy in $\mathbb{C}^\times$. Hence the loop $\gamma_r(s) = p(re^{2\pi is})$ is homotopic in
$\mathbb{C}^\times$ to $\eta_r(s) = r^n e^{2\pi i n s}$, whose degree is $n\neq0$ (Lemma 7.6.3).

On the other hand $\gamma_r = p\circ\sigma_r$ where $\sigma_r(s) = re^{2\pi is}$ is a loop in $\mathbb{C}$;
so $[\gamma_r] = p_*[\sigma_r] = 1$ because $\pi_1(\mathbb{C}) = 1$. Hence $\deg\gamma_r = 0$, contradicting
$\deg\gamma_r = n$. Therefore $p$ has a zero. $\blacksquare$

**23.** *Strategy: a homeomorphism restricts to a homeomorphism of punctured spaces, and $\pi_1$ of a
punctured space is computable.*

Suppose $h : \mathbb{R}^2\to\mathbb{R}^n$ is a homeomorphism, $n\ge3$, and put $p = h(0)$. Then $h$ restricts
to a homeomorphism $\mathbb{R}^2\setminus\{0\}\to\mathbb{R}^n\setminus\{p\}$.

By Exercise 10, $\mathbb{R}^2\setminus\{0\}\simeq S^1$, so $\pi_1(\mathbb{R}^2\setminus\{0\}) = \mathbb{Z}$,
whereas $\mathbb{R}^n\setminus\{p\}\cong\mathbb{R}^n\setminus\{0\}\simeq S^{n-1}$ and
$\pi_1(S^{n-1}) = 1$ for $n-1\ge2$ (van Kampen: $S^{k}$ is the union of two contractible open sets
$S^k\setminus\{N\}$ and $S^k\setminus\{S\}$ whose intersection is homeomorphic to $S^{k-1}\times\mathbb{R}$,
which is path connected for $k\ge2$; so $\pi_1(S^k) = 1$).

A homeomorphism induces an isomorphism on $\pi_1$ (Corollary 7.5.4), so $\mathbb{Z}\cong1$ — contradiction.
Hence $\mathbb{R}^2\not\cong\mathbb{R}^n$.

*Why counting components is not enough:* removing a point from $\mathbb{R}^m$ with $m\ge2$ leaves a path
connected space, so both punctured spaces have one component and the count agrees. One must use a finer
invariant; $\pi_1$ suffices for $\mathbb{R}^2$ versus $\mathbb{R}^n$ ($n\ge3$) because it distinguishes the
punctured spaces, and homology $H_{n-1}$ is needed for the general case. $\blacksquare$

**24.** *Strategy: collapse a spanning tree.*

Let $\Gamma$ be a connected graph, $V$ vertices and $E$ edges. Choose a spanning tree $T\subseteq\Gamma$; it has
$V-1$ edges (a tree on $V$ vertices has exactly $V-1$ edges) and is contractible (every tree deformation
retracts onto any of its vertices, by pruning leaves one at a time).

The quotient $\Gamma/T$ collapses a contractible subcomplex, so the quotient map $q : \Gamma \to \Gamma/T$ is a
homotopy equivalence (standard: collapsing a contractible subcomplex of a CW pair is a homotopy equivalence;
see Hatcher, Proposition 0.17). The quotient $\Gamma/T$ has a single vertex and the
$E - (V-1) = E-V+1$ remaining edges, each of which becomes a loop: it is a wedge of $E-V+1$ circles.

By van Kampen (Theorem 7.10.4), applied to the wedge of circles as the union of one circle plus the rest, the
fundamental group of a wedge of $k$ circles is the free group $F_k$. Hence
$\pi_1(\Gamma)\cong\pi_1(\Gamma/T)\cong F_{E-V+1}$. (For a tree, $E = V-1$ and the group is trivial, as it
should be.) $\blacksquare$

**25.** *Strategy: count cells of the given CW structures, then check Euler–Poincaré using the Betti numbers.*

(a) Tetrahedron: $V=4$, $E=6$, $F=4$, so $\chi = 4-6+4 = 2$.
(b) Cube: $V=8$, $E=12$, $F=6$, so $\chi = 8-12+6 = 2$.
(c) Octahedron: $V=6$, $E=12$, $F=8$, so $\chi = 6-12+8 = 2$.
(d) Torus: the square model has one $0$-cell, two $1$-cells (the identified edge classes) and one $2$-cell, so
$\chi = 1-2+1 = 0$.
(e) Klein bottle: same count, one $0$-cell, two $1$-cells, one $2$-cell: $\chi = 0$.
(f) $\mathbb{RP}^2$: the square with antipodal boundary identification has one $0$-cell, one $1$-cell and one
$2$-cell, so $\chi = 1-1+1 = 1$.

*Checks.* For $S^2\cong$ tetrahedron: $b_0 = 1$, $b_1 = 0$, $b_2 = 1$, so $\sum_k(-1)^kb_k = 1-0+1 = 2 = \chi$.
For $T^2$: $b_0 = 1$, $b_1 = 2$, $b_2 = 1$, so $\sum_k(-1)^kb_k = 1-2+1 = 0 = \chi$. Both agree with
Theorem 7.9.1. Also $\chi(\mathbb{RP}^2) = 1$ is consistent with the double cover
$\chi(S^2) = 2\chi(\mathbb{RP}^2) = 2$. $\blacksquare$

**26.** *Strategy: split each chain group by the cells that lie in $A$, in $B$ and in neither.*

For each $k$, the set of $k$-cells of $X$ is the union of the $k$-cells of $A$ and those of $B$, and the
$k$-cells lying in $A\cap B$ are exactly those in both (a cell of a subcomplex either lies entirely in the
subcomplex or misses it, since cells are attached along their boundaries). Hence, counting basis elements of
the cellular chain groups,

$$c_k(X) = c_k(A) + c_k(B) - c_k(A\cap B).$$

Multiplying by $(-1)^k$ and summing over $k$,

$$\chi(X) = \sum_k(-1)^kc_k(X)
= \sum_k(-1)^k c_k(A) + \sum_k(-1)^kc_k(B) - \sum_k(-1)^kc_k(A\cap B)
= \chi(A)+\chi(B)-\chi(A\cap B).$$

No property of the boundary maps is needed: the identity is at the level of chain groups, hence holds for the
alternating sums. $\blacksquare$

**27.** *Strategy: product cells.*

Give $X$ and $Y$ their CW structures. The product $X\times Y$ has a CW structure whose open $k$-cells are the
products $e^i\times e^{k-i}$ of open cells of $X$ and $Y$ with $i + (k-i) = k$; this is the standard product
cell decomposition (Hatcher, Theorem 2.10 and the discussion of products). Hence

$$c_k(X\times Y) = \sum_{i=0}^{k} c_i(X)\,c_{k-i}(Y).$$

Therefore

$$\chi(X\times Y) = \sum_k(-1)^k\sum_i c_i(X)c_{k-i}(Y)
= \Bigl(\sum_i(-1)^ic_i(X)\Bigr)\Bigl(\sum_j(-1)^jc_j(Y)\Bigr) = \chi(X)\chi(Y),$$

using the Cauchy product of the two finite alternating sums. $\blacksquare$

**28.** *Strategy: make the covering cellular, then count lifts of cells.*

Because $X$ is a finite CW complex and $p$ is a covering, there is a CW structure on $X$ with respect to which
$p$ is cellular, i.e. $p$ maps the $k$-skeleton of $\tilde X$ to the $k$-skeleton of $X$ and maps each open
$k$-cell of $\tilde X$ homeomorphically onto an open $k$-cell of $X$ (subdivide $X$ so that each cell lies in an
evenly covered set; then lift the subdivision). With this structure, $p^{-1}$ of each open $k$-cell $e$ is a
disjoint union of $n$ open $k$-cells, one in each sheet over an evenly covered neighbourhood of $e$. Hence
$c_k(\tilde X) = n\,c_k(X)$ for every $k$, and

$$\chi(\tilde X) = \sum_k(-1)^k c_k(\tilde X) = n\sum_k(-1)^kc_k(X) = n\chi(X).$$

*Application.* The antipodal covering $S^2\to\mathbb{RP}^2$ is $2$-sheeted, so
$\chi(S^2) = 2\chi(\mathbb{RP}^2)$; with $\chi(S^2) = 2$ this gives $\chi(\mathbb{RP}^2) = 1$, matching the
cell count $1-1+1$ of Exercise 25. $\blacksquare$

**29.** *Strategy: use that $p_*$ is injective and that $\pi_1(X)$ is trivial, then show the fibre is a single
point.*

By Exercise 18, $p_* : \pi_1(\tilde X,\tilde x_0)\to\pi_1(X,x_0)$ is injective; since $\pi_1(X,x_0) = 1$, we get
$\pi_1(\tilde X,\tilde x_0) = 1$.

*The fibre has one point.* Let $x\in X$ and let $\tilde x,\tilde x'\in p^{-1}[\{x\}]$. The space $\tilde X$ is
connected and locally path connected (it is locally homeomorphic to the locally path connected space $X$), so
it is path connected; choose a path $\tilde\alpha$ in $\tilde X$ from $\tilde x$ to $\tilde x'$. Then
$\alpha = p\circ\tilde\alpha$ is a loop in $X$ at $x$, and $[\alpha] = p_*[\tilde\alpha] = 1$ because
$\pi_1(\tilde X) = 1$. By uniqueness of path lifting, the lift of $\alpha$ starting at $\tilde x$ is
$\tilde\alpha$, and the lift of the constant loop is constant; hence $\tilde\alpha$ is constant and
$\tilde x' = \tilde x$.

So $p$ is a continuous bijection. A covering map is a local homeomorphism, and a bijective local homeomorphism
is a homeomorphism. $\blacksquare$

**30.** *Strategy: van Kampen with two open sets whose intersection is contractible (wedge) or an annulus
(torus).*

*The wedge.* Let $X = S^1\vee S^1$, with the two circles meeting at $v$. Take $U$ to be the first circle
together with a small open neighbourhood of $v$ in the second circle, and $V$ the mirror image; then $U$ and
$V$ are open and path connected, $U\cup V = X$, and $U\cap V$ is a small open interval around $v$, which is
contractible. By van Kampen,
$\pi_1(X)\cong\pi_1(U)*_{\pi_1(U\cap V)}\pi_1(V) = \mathbb{Z}*\mathbb{Z} = F_2$, free on two generators
(the classes of the two loops).

*The torus.* The product formula of Exercise 15 applied to $T^2 = S^1\times S^1$ gives
$\pi_1(T^2)\cong\mathbb{Z}\times\mathbb{Z}$. (Van Kampen gives the same answer: write
$T^2 = U\cup V$ with $U$ the complement of a small closed disc, which deformation retracts onto $S^1\vee S^1$
and has $\pi_1 = F_2 = \langle a,b\rangle$, $V$ an open disc with trivial group, and $U\cap V$ an annulus with
$\pi_1 = \mathbb{Z}$ generated by the boundary loop, which in $U$ represents the commutator $aba^{-1}b^{-1}$;
amalgamating kills exactly that commutator, so $\pi_1(T^2) = F_2/\langle\!\langle [a,b]\rangle\!\rangle =
\mathbb{Z}^2$.)

*Not isomorphic.* $F_2$ is not abelian: in $\langle a,b\rangle$ the elements $ab$ and $ba$ are distinct (a free
group has a homomorphism onto $S_3$, or onto $\mathbb{Z}^2$, sending $a\mapsto(1,0)$, $b\mapsto(0,1)$; there
$ab\neq ba$... careful: in $\mathbb{Z}^2$ they are equal; use the free-group property with $a\mapsto$ a
transposition $\tau$ and $b\mapsto$ a 3-cycle $\sigma$ in $S_3$: then $ab\mapsto\tau\sigma\neq\sigma\tau$, so
$ab\ne ba$). But $\mathbb{Z}^2$ is abelian. Hence $\pi_1(S^1\vee S^1)\ncong\pi_1(T^2)$, so by Corollary 7.5.6
the figure-eight and the torus are not homotopy equivalent (in particular not homeomorphic). $\blacksquare$

## Challenge

**31.** *Strategy: lift loops to $\mathbb{R}$, define the degree as the change of the lift, and verify the
group isomorphism by the three lemmas.*

*Step 1: path lifting.* Let $\gamma : I\to S^1$ be continuous and $t_0\in\mathbb{R}$ with
$p(t_0) = \gamma(0)$. Since $I$ is compact and $\gamma$ is uniformly continuous, choose $n$ such that
$\lvert s - s'\rvert\le 1/n$ implies $\lvert\gamma(s)-\gamma(s')\rvert < 1$ (Euclidean distance in
$\mathbb{C}$). On each subinterval $I_k = [k/n,(k+1)/n]$ the image $\gamma[I_k]$ has diameter $<1$, so it is
contained in $S^1\setminus\{z_k\}$ for some $z_k$ (take $z_k = -\gamma(k/n)$: every point of $\gamma[I_k]$ is at
distance $<1$ from $\gamma(k/n)$, hence cannot be $-\gamma(k/n)$). Now
$p^{-1}(S^1\setminus\{z_k\}) = \mathbb{R}\setminus(t_k+\mathbb{Z})$ is a disjoint union of open intervals on
each of which $p$ is a homeomorphism; lifting successively along $I_0,I_1,\dots$ gives a continuous
$\tilde\gamma$ with $\tilde\gamma(0) = t_0$ and $p\circ\tilde\gamma = \gamma$.

*Step 2: uniqueness.* If $\tilde\gamma_1,\tilde\gamma_2$ are two lifts with the same value at $0$, then
$E = \{s : \tilde\gamma_1(s) = \tilde\gamma_2(s)\}$ is non-empty and closed; it is open because near a point of
$E$ both lifts take values in a single sheet, on which $p$ is injective. So $E = I$.

*Step 3: degree.* For a loop $\gamma$, set $\deg\gamma = \tilde\gamma(1)-\tilde\gamma(0)$. This is an integer
($p$ of both endpoints equals $\gamma(0)$) and independent of the lift (two lifts differ by a continuous
integer-valued function, hence a constant).

*Step 4: homotopy invariance.* Let $H : I\times I\to S^1$ be a path homotopy. Applying Step 1 on a fine grid of
small squares (or the two-dimensional lifting theorem) gives a lift $\tilde H$ of $H$ with
$\tilde H(0,0) = \tilde\gamma(0)$. Since $H(0,\cdot)$ and $H(1,\cdot)$ are constant, their lifts are constant
(Step 2). Hence
$\deg\gamma' = \tilde H(1,1)-\tilde H(0,1) = \tilde H(1,0)-\tilde H(0,0) = \deg\gamma$.

*Step 5: homomorphism.* Given loops $\gamma,\delta$, let $\tilde\gamma$ be a lift of $\gamma$ and let
$\tilde\delta$ be the lift of $\delta$ starting at $\tilde\gamma(1)$. Then
$\tilde\gamma*\tilde\delta$ is a lift of $\gamma*\delta$, so
$\deg(\gamma*\delta) = \tilde\delta(1)-\tilde\gamma(0) = \deg\delta+\deg\gamma$.

*Step 6: surjective.* $\deg(\gamma_n) = n$ for $\gamma_n(s) = e^{2\pi ins}$, whose lift is $ns$.

*Step 7: injective.* If $\deg\gamma = 0$, the lift with $\tilde\gamma(0) = 0$ is a loop at $0$ in $\mathbb{R}$.
Since $\mathbb{R}$ is convex, $F(s,t) = (1-t)\tilde\gamma(s)$ is a path homotopy from $\tilde\gamma$ to the
constant loop (Exercise 6), and $p\circ F$ is a path homotopy from $\gamma$ to the constant loop at $1$.

Steps 4–7 show that $[\gamma]\mapsto\deg\gamma$ is a well-defined surjective homomorphism with trivial kernel,
hence an isomorphism $\pi_1(S^1,1)\cong\mathbb{Z}$. $\blacksquare$

**32.** *Strategy: use the multiplication map on the square and read off the commutator as the boundary of the
square, which is null-homotopic.*

Let $m : G\times G\to G$ be the multiplication (continuous by definition of a topological group) and $e$ the
identity. Let $\alpha,\beta$ be loops in $G$ at $e$ and define

$$\Phi : I\times I\to G, \qquad \Phi(s,t) = \alpha(s)\,\beta(t) = m\bigl(\alpha(s),\beta(t)\bigr).$$

$\Phi$ is continuous, being a composite of continuous maps. Consider the loop $\partial\Phi$ obtained by
traversing the boundary of the square once, starting at $(0,0)$ and going along the bottom, the right side, the
top (backwards) and the left side (downwards). Its four pieces are

$$\alpha(s)\,\beta(0) = \alpha(s), \qquad \alpha(1)\,\beta(t) = \beta(t), \qquad
\alpha(s)\,\beta(1) = \alpha(s), \qquad \alpha(0)\,\beta(t) = \beta(t),$$

so, up to the standard reparametrisation of the four sides by $[0,1]$, $\partial\Phi$ is the concatenation
$\alpha*\beta*\bar\alpha*\bar\beta$ (Theorem 7.3.2 and Lemma 7.2.2 identify reparametrised concatenations in
$\pi_1$).

Because the square $I\times I$ is convex, its boundary loop is null-homotopic in $I\times I$; composing that
null-homotopy with $\Phi$ shows that $\partial\Phi$ is null-homotopic in $G$. Hence, in the group
$\pi_1(G,e)$,

$$[\alpha]\,[\beta]\,[\alpha]^{-1}[\beta]^{-1} = [\partial\Phi] = 1,
\qquad\text{so}\qquad [\alpha][\beta] = [\beta][\alpha].$$

Therefore $\pi_1(G,e)$ is abelian.

*Remark.* The same computation can be phrased as the Eckmann–Hilton argument: the pointwise product of loops
$(\alpha\cdot\beta)(s) = \alpha(s)\beta(s)$ and the concatenation are two group structures on $\pi_1(G,e)$
satisfying the interchange law $(\alpha*\beta)\cdot(\gamma*\delta) =
(\alpha\cdot\gamma)*(\beta\cdot\delta)$, which forces both to be commutative. $\blacksquare$

**33.** *Strategy: build the presentation complex and use that attaching a $2$-cell kills the normal closure of
the attaching word.*

Let $G = \langle g_1,\dots,g_n \mid r_1,\dots,r_m\rangle$. Build a CW complex $X$ as follows: one $0$-cell $v$;
$n$ $1$-cells $e_1,\dots,e_n$, each attached to $v$ at both ends, so that the $1$-skeleton $X^{(1)}$ is a wedge
of $n$ circles; and $m$ $2$-cells $D_1,\dots,D_m$, where $D_j$ is attached by a loop in $X^{(1)}$ that spells
the word $r_j$ in the letters $g_i^{\pm1}$ (traverse $e_i$ forwards for $g_i$, backwards for $g_i^{-1}$).

By van Kampen, applied to $X^{(1)}$ as a union of one circle and the rest, with contractible intersections,
$\pi_1(X^{(1)},v)\cong F_n = \langle a_1,\dots,a_n\rangle$, where $a_i$ is the class of $e_i$.

*Attaching a $2$-cell.* Let $Y$ be a space and $\varphi : S^1\to Y$ a loop with $[\varphi] = w$. Then the space
$Y\cup_\varphi D^2$ obtained by attaching a $2$-cell has
$\pi_1(Y\cup_\varphi D^2)\cong\pi_1(Y)/\langle\!\langle w\rangle\!\rangle$, where
$\langle\!\langle w\rangle\!\rangle$ is the normal closure. Indeed, applying van Kampen to the union of a small
open neighbourhood of $Y$ and the interior of the attached disc (which is contractible), with intersection an
open annulus whose fundamental group is $\mathbb{Z}$ generated by $w$, the amalgamated product is
$\pi_1(Y) *_{\mathbb{Z}} 1 = \pi_1(Y)/\langle\!\langle w\rangle\!\rangle$.

Applying this successively to the $m$ two-cells (attaching cells in any order; each attachment adds the normal
closure of one relation) gives

$$\pi_1(X,v)\cong F_n\big/\langle\!\langle r_1,\dots,r_m\rangle\!\rangle
= \langle g_1,\dots,g_n\mid r_1,\dots,r_m\rangle = G.$$

So every finitely presented group is the fundamental group of a finite $2$-complex. $\blacksquare$

**34.** *Strategy: the double cover $S^2\to\mathbb{RP}^2$ together with the classification of coverings gives the
order of the group.*

$\mathbb{RP}^2 = S^2/\{x\sim -x\}$ is the quotient by the antipodal action, and the quotient map
$p : S^2\to\mathbb{RP}^2$ is a $2$-sheeted covering (each point has an evenly covered neighbourhood given by the
image of a small open hemisphere).

$S^2$ is simply connected: write $S^2 = U\cup V$ with $U = S^2\setminus\{N\}$, $V = S^2\setminus\{S\}$; both are
homeomorphic to $\mathbb{R}^2$, hence contractible, and $U\cap V\cong S^1\times\mathbb{R}\cong\mathbb{R}^2
\setminus\{0\}$ is path connected. Van Kampen gives
$\pi_1(S^2) = \pi_1(U)*_{\pi_1(U\cap V)}\pi_1(V) = 1*_11 = 1$.

Now $p_*$ is injective (Theorem 7.7.4) with trivial domain, so $p_*\pi_1(S^2) = 1$. By Theorem 7.7.6 the number
of sheets equals the index of this subgroup in $\pi_1(\mathbb{RP}^2)$, so
$[\pi_1(\mathbb{RP}^2):1] = 2$, i.e. $\lvert\pi_1(\mathbb{RP}^2)\rvert = 2$. The only group with two elements
is $\mathbb{Z}/2$, so $\pi_1(\mathbb{RP}^2)\cong\mathbb{Z}/2$.

(The same conclusion follows from van Kampen: $\mathbb{RP}^2$ is a Möbius band $M\simeq S^1$ glued to a disc
along their boundary circles; the boundary of $M$ represents twice a generator of $\pi_1(M) = \mathbb{Z}$, so
$\pi_1(\mathbb{RP}^2) = \mathbb{Z}/2\mathbb{Z}$.) $\blacksquare$

**35.** *Strategy: unit quaternions act on the imaginary quaternions by conjugation; the kernel is $\{\pm1\}$, so
the rotation group is the antipodal quotient of $S^3$, which is $\mathbb{RP}^3$.*

Let $\mathbb{H} = \{a+bi+cj+dk\}$ be the quaternions, with conjugation
$\overline{a+bi+cj+dk} = a-bi-cj-dk$ and $\lvert q\rvert^2 = q\bar q$. Identify $\mathbb{R}^3$ with the imaginary
quaternions $V = \{q : \bar q = -q\} = \operatorname{span}\{i,j,k\}$, and let $S^3 = \{q : \lvert q\rvert = 1\}$.

Define $\Phi : S^3\to GL(V)$ by $\Phi(q)(v) = qv\bar q$.

*Well defined and orthogonal.* If $v$ is imaginary then $\operatorname{Re}(qv\bar q) = 0$ (conjugation by a
quaternion preserves the real part, and the real part of $v$ is $0$), so $\Phi(q)(v)\in V$; and
$\lvert qv\bar q\rvert = \lvert q\rvert\lvert v\rvert\lvert\bar q\rvert = \lvert v\rvert$, so $\Phi(q)$ is an
orthogonal map of $V\cong\mathbb{R}^3$ with $\det = +1$ (as $S^3$ is connected and $\det\Phi$ is a continuous
map to $\{\pm1\}$ with value $1$ at $q=1$). So $\Phi(q)\in SO(3)$.

*Homomorphism and continuity.* $\Phi(qq')(v) = qq'v\overline{qq'} = q(q'v\bar q')\bar q =
\Phi(q)\bigl(\Phi(q')(v)\bigr)$; and the entries of the matrix of $\Phi(q)$ are quadratic polynomials in the
coordinates of $q$, so $\Phi$ is continuous.

*Kernel.* If $qv\bar q = v$ for all $v\in V$, then $qv = vq$ for all imaginary $v$, hence $q$ commutes with
every quaternion (as $1$ and $V$ generate $\mathbb{H}$), so $q$ lies in the centre $\mathbb{R}$ of $\mathbb{H}$;
with $\lvert q\rvert = 1$ this gives $q = \pm1$.

*Surjectivity.* A rotation of $\mathbb{R}^3$ with unit axis $u\in V$ and angle $\theta$ is conjugation by
$q = \cos\frac\theta2 + \sin\frac\theta2\,u$ (the Euler–Rodrigues formula); every rotation has such a form.

Hence $\Phi$ induces a continuous bijection $\bar\Phi : S^3/\{\pm1\}\to SO(3)$. The quotient $S^3/\{\pm1\}$ is by
definition $\mathbb{RP}^3$, which is compact; $SO(3)$ is Hausdorff. A continuous bijection from a compact space
to a Hausdorff space is a homeomorphism, so $SO(3)\cong\mathbb{RP}^3$.

Finally $\pi_1(SO(3))\cong\pi_1(\mathbb{RP}^3)\cong\mathbb{Z}/2$ by the argument of Exercise 34 (the double cover
$S^3\to\mathbb{RP}^3$ has two sheets and $S^3$ is simply connected). $\blacksquare$

**36.** *Strategy: van Kampen for simple connectivity, Hurewicz for $\pi_2$, the Hopf fibration for $\pi_3$, and a
discussion of why the general computation is hard.*

*$S^2$ is simply connected.* Write $S^2 = U\cup V$ with $U = S^2\setminus\{N\}\cong\mathbb{R}^2$ and
$V = S^2\setminus\{S\}\cong\mathbb{R}^2$, both contractible, and
$U\cap V\cong S^1\times\mathbb{R}$, which is path connected. Van Kampen gives
$\pi_1(S^2)\cong 1 *_1 1 = 1$.

*$\pi_2(S^2)\cong\mathbb{Z}$.* The Hurewicz theorem states that if $X$ is path connected and $(n-1)$-connected
with $n\ge2$, then $\pi_n(X)\cong H_n(X)$. $S^2$ is simply connected, i.e. $1$-connected, and $H_2(S^2)\cong
\mathbb{Z}$, so $\pi_2(S^2)\cong\mathbb{Z}$. The generator is the identity map
$\operatorname{id} : S^2\to S^2$, and the isomorphism sends it to the fundamental class.

*$\pi_3(S^2)\cong\mathbb{Z}$.* The Hopf fibration is a fibre bundle $S^1\to S^3\xrightarrow{\eta} S^2$ (explicitly,
$\eta(z_0,z_1) = [z_0:z_1]\in\mathbb{CP}^1\cong S^2$ for $(z_0,z_1)\in S^3\subseteq\mathbb{C}^2$). Its long exact
sequence of homotopy groups contains

$$\pi_3(S^1)\to\pi_3(S^3)\xrightarrow{\eta_*}\pi_3(S^2)\to\pi_2(S^1).$$

Now $\pi_3(S^1) = 0$ and $\pi_2(S^1) = 0$ (the universal cover of $S^1$ is $\mathbb{R}$, so all higher homotopy
groups of $S^1$ vanish), while $\pi_3(S^3)\cong\mathbb{Z}$; hence $\eta_*$ is an isomorphism and
$\pi_3(S^2)\cong\mathbb{Z}$.

*Why this is surprising.* One expects $\pi_k(S^n) = 0$ for $k<n$ — there is no room for a sphere of dimension
$k$ to wrap around one of dimension $n$ — and indeed $\pi_2(S^2) = \mathbb{Z}$ with the identity as generator,
while $\pi_1(S^2) = 0$. The pattern "$\pi_n(S^n) = \mathbb{Z}$, everything below vanishes" suggests that
$\pi_3(S^2)$ might vanish; instead, the Hopf map $\eta$ is essential: the attaching map of the $4$-cell in
$\mathbb{CP}^2$ is $\eta$, and the ring structure $H^*(\mathbb{CP}^2) = \mathbb{Z}[x]/(x^3)$ with $\deg x = 2$
forces $\eta$ to be non-trivial (its Hopf invariant is $1$). So homotopy groups can be non-zero above the
dimension of the space, and they are not visible to $H_*$ in a naive way (though $\pi_3(S^2)\cong H_3(S^2)=0$:
the Hurewicz theorem only applies below the connectivity range).

*What this says about difficulty.* $\pi_k(S^n)$ for $k>n$ is a subtle unstable invariant: the values
$\pi_{n+1}(S^n)\cong\mathbb{Z}/2$ for $n\ge3$, $\pi_4(S^3)\cong\mathbb{Z}/2$, $\pi_5(S^2)\cong\mathbb{Z}/2$ and
$\pi_6(S^3)\cong\mathbb{Z}/12$ show no simple pattern. The stable range is governed by the Freudenthal suspension
theorem, and stable homotopy groups of spheres are still not known in closed form. See Hatcher, *Algebraic
Topology*, Chapter 4 (in particular §4.1–§4.2 and the tables in §4.1), and Toda, *Composition Methods in
Homotopy Groups of Spheres*, for the classical computations. $\blacksquare$

**37.** *Strategy: read the presentation off the square model, then map to the infinite dihedral group to prove
non-abelianness.*

*The presentation.* Model the Klein bottle $K$ as the quotient of $[0,1]^2$ by $(0,y)\sim(1,1-y)$ and
$(x,0)\sim(x,1)$. This gives a CW structure with one $0$-cell $v$, two $1$-cells $a$ (image of the horizontal
edges) and $b$ (image of the vertical edges, with the twist), and one $2$-cell attached along the boundary loop,
which spells the word $a\,b\,a\,b^{-1}$. Hence $K^{(1)} = S^1\vee S^1$ with
$\pi_1 = F_2 = \langle a,b\rangle$, and by the argument of Exercise 33 (attaching a $2$-cell kills the normal
closure of the attaching word),

$$\pi_1(K,v)\cong\langle a,b \mid abab^{-1}\rangle.$$

*Non-abelian.* Let $D_\infty$ be the group of isometries of $\mathbb{R}$, generated by the translation
$t(x) = x+1$ and the reflection $s(x) = -x$, so $s^2 = 1$ and $sts = t^{-1}$. Define
$\varphi : \langle a,b\rangle\to D_\infty$ by $\varphi(a) = t$, $\varphi(b) = s$. Then
$\varphi(abab^{-1}) = t\,s\,t\,s^{-1} = t\,s\,t\,s$; computing on $x$: $s: -x$, then $t$: $1-x$, then $s$:
$x-1$, then $t$: $x$. So $\varphi(abab^{-1}) = \operatorname{id}$ and $\varphi$ factors through the quotient
$\pi_1(K)$. But
$\varphi(a)\varphi(b) = t\circ s$ sends $x\mapsto 1-x$, while $\varphi(b)\varphi(a) = s\circ t$ sends
$x\mapsto -x-1$; these differ, so $\varphi(ab)\neq\varphi(ba)$ and hence $ab\neq ba$ in $\pi_1(K)$.

*Consequence.* $\pi_1(T^2)\cong\mathbb{Z}^2$ is abelian, while $\pi_1(K)$ is not; by Corollary 7.5.6 the Klein
bottle is not homeomorphic to the torus. Both are closed connected surfaces and both have Euler characteristic
$0$ (Exercise 25), which is exactly why a sharper invariant — the fundamental group — is needed.
$\blacksquare$