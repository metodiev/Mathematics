# Introduction to Algebraic Topology — Exercises

> [Introduction to Algebraic Topology](README.md) · 37 problems · Beginner → Challenge · Solutions: [solutions.md](solutions.md)

Every problem is a proof or a computation; "compute" means "give the group together with a justification", and
"state" means "write the statement with all hypotheses". You may use anything proved in the
[tutorial](README.md), and you may quote van Kampen's theorem, the homotopy lifting theorem, the classification
of coverings and the Euler–Poincaré formula where a problem says so. Do not open
[solutions.md](solutions.md) before writing an attempt.

Notation: $I = [0,1]$; $S^1 = \{z\in\mathbb{C} : \lvert z\rvert = 1\}$; $p : \mathbb{R}\to S^1$,
$p(t) = e^{2\pi it}$; $D^n$ is the closed unit ball in $\mathbb{R}^n$; $F_n$ is the free group on $n$
generators; $[\gamma]$ is the path homotopy class of $\gamma$; $\chi$ is the Euler characteristic.

## Beginner

**1.** Let $f, g, h : X \to Y$ be continuous. Prove from the definition that $\simeq$ is an equivalence
relation on the set of continuous maps $X\to Y$: write down the three homotopies and check continuity,
including continuity of the glued homotopy used for transitivity.

**2.** Let $C\subseteq\mathbb{R}^n$ be convex and non-empty. Prove that any two continuous maps $f,g : X\to C$
are homotopic. Deduce that $\mathbb{R}^n$ and $D^n$ are contractible.

**3.** Let $X$ be a discrete space and $x_0\in X$. Prove that every path $I\to X$ is constant and that
$\pi_1(X,x_0) = \{1\}$.

**4.** Let $\gamma$ be a path from $x$ to $y$ and $\delta$ a path from $y$ to $z$. Prove that
$\overline{\gamma*\delta}\simeq_p \bar\delta*\bar\gamma$, where $\bar\gamma(t) = \gamma(1-t)$.

**5.** In $\mathbb{C}^\times$ let $\gamma(s) = e^{2\pi i s}$ and $\delta(s) = e^{-2\pi i s}$. Write down the
concatenations $\gamma*\delta$ and $\delta*\gamma$, exhibit explicit path homotopies from each to the constant
loop at $1$, and say what this shows about $[\gamma]$ in $\pi_1(\mathbb{C}^\times,1)$.

**6.** Let $C\subseteq\mathbb{R}^n$ be convex, $\gamma$ a loop in $C$ at $x_0\in C$. Write down an explicit
homotopy rel $\{0,1\}$ from $\gamma$ to the constant loop, and check the three conditions $H(s,0) = \gamma(s)$,
$H(s,1) = x_0$, $H(0,t) = H(1,t) = x_0$.

**7.** Compute $\pi_1(\ast,x_0)$ and $\pi_1(X,x_0)$ where $X = \{a,b\}$ is a two-point discrete space. Justify
both answers from the definition (not by quoting a theorem).

**8.** For $\gamma_n(s) = e^{2\pi i n s}$ and its reverse $\bar\gamma_n$, compute $\deg\gamma_n$,
$\deg\bar\gamma_n$ and $\deg(\gamma_n*\bar\gamma_n)$ directly from the definition via lifts.

**9.** Compute the degrees of (a) $\gamma(t) = e^{2\pi i(3t+\sin 2\pi t)}$; (b) $\eta(t) = e^{2\pi i \cdot 5t^2}$;
(c) the loop $t\mapsto \gamma(t)\eta(t)$ where $\gamma$ is as in (a). Justify by exhibiting lifts.

**10.** Prove that $r(x) = x/\lVert x\rVert$ is a deformation retraction of $\mathbb{R}^n\setminus\{0\}$ onto
$S^{n-1}$, verifying that the homotopy never takes the value $0$. Deduce that
$\pi_1(\mathbb{R}^n\setminus\{0\})\cong\pi_1(S^{n-1})$ for $n\ge1$.

## Intermediate

**11.** Let $f : X\to Y$ be continuous, $x_0\in X$. Prove that
$f_* : \pi_1(X,x_0)\to\pi_1(Y,f(x_0))$, $[\gamma]\mapsto[f\circ\gamma]$, is well defined and is a group
homomorphism, checking the class of a concatenation explicitly.

**12.** Prove that $(g\circ f)_* = g_*\circ f_*$ and $(\operatorname{id}_X)_* =
\operatorname{id}_{\pi_1(X,x_0)}$ for continuous composable maps.

**13.** Let $H : X\times I\to Y$ be a homotopy from $f$ to $g$ with $H(x_0,t) = f(x_0)$ for all $t$. Prove that
$f_* = g_*$ on $\pi_1(X,x_0)$, writing out the homotopy of loops.

**14.** Let $\gamma$ be a path in $X$ from $x_0$ to $x_1$. Prove that
$\gamma_\#([\alpha]) = [\gamma*\alpha*\bar\gamma]$ defines a group isomorphism
$\pi_1(X,x_1)\to\pi_1(X,x_0)$, and identify its inverse.

**15.** Prove that $\pi_1(X\times Y,(x_0,y_0))\cong\pi_1(X,x_0)\times\pi_1(Y,y_0)$.

**16.** Deduce from Exercise 15 that $\pi_1(T^2,(1,1))\cong\mathbb{Z}^2$ and that the cylinder
$S^1\times[0,1]$ has fundamental group $\mathbb{Z}$.

**17.** Lift $\gamma(t) = e^{2\pi i t^2}$ through $p(t) = e^{2\pi i t}$, starting at $0$. Give the lift
explicitly, compute its endpoint, and hence $\deg\gamma$. Then do the same for $\gamma(t) = e^{2\pi i \sqrt t}$.

**18.** Let $p : \tilde X\to X$ be a covering and $\tilde x_0\in p^{-1}[\{x_0\}]$. Using unique path lifting
and the homotopy lifting theorem, prove that $p_* : \pi_1(\tilde X,\tilde x_0)\to\pi_1(X,x_0)$ is injective.

**19.** Prove that $\deg : \pi_1(S^1,1)\to\mathbb{Z}$ is a surjective group homomorphism, and that
$\deg\gamma = 0$ implies that $\gamma$ is null-homotopic. Conclude $\pi_1(S^1,1)\cong\mathbb{Z}$.

**20.** Prove that a continuous map $f : S^1\to S^1$ is null-homotopic if and only if $\deg f = 0$. (You may
use that $\deg$ is a homomorphism and that $f_*([\gamma_1]) = [f\circ\gamma_1]$.)

## Advanced

**21.** Prove Brouwer's fixed point theorem in dimension $2$: every continuous $f : D^2\to D^2$ has a fixed
point. Include the construction of the retraction $D^2\to S^1$ and the proof that it is continuous.

**22.** Prove the fundamental theorem of algebra using $\pi_1$.

**23.** Using the fundamental group of punctured spaces, prove that $\mathbb{R}^2$ is not homeomorphic to
$\mathbb{R}^n$ for $n\ge3$. Explain why counting components of punctured spaces is not enough and which
invariant you used instead.

**24.** Let $\Gamma$ be a connected graph with $V$ vertices and $E$ edges. Prove that
$\pi_1(\Gamma)\cong F_{E-V+1}$. (Use a spanning tree and a deformation retraction onto a wedge of circles.)

**25.** Compute the Euler characteristic of (a) the tetrahedron, (b) the cube, (c) the octahedron, (d) the torus
from its square model, (e) the Klein bottle from its square model, (f) $\mathbb{RP}^2$ from the square with
antipodal boundary identification. Verify for (a) and (d) that the result equals $\sum_k(-1)^kb_k$.

**26.** Let $X$ be a finite CW complex with subcomplexes $A, B$ such that $X = A\cup B$. Prove
$\chi(X) = \chi(A)+\chi(B)-\chi(A\cap B)$ by splitting the cellular chain complex.

**27.** Prove that $\chi(X\times Y) = \chi(X)\chi(Y)$ for finite CW complexes, by counting product cells.

**28.** Let $p : \tilde X\to X$ be an $n$-sheeted covering of finite CW complexes. Prove
$\chi(\tilde X) = n\chi(X)$. Deduce $\chi(S^2) = 2\chi(\mathbb{RP}^2)$ and verify both values.

**29.** Let $X$ be simply connected, path connected and locally path connected. Prove that every connected
covering $p : \tilde X\to X$ is a homeomorphism.

**30.** Using van Kampen's theorem, compute $\pi_1(S^1\vee S^1)$ and $\pi_1(S^1\times S^1)$, and prove that the
two groups are not isomorphic. What does this show about the two spaces?

## Challenge

**31.** Prove in full detail that $\pi_1(S^1,1)\cong\mathbb{Z}$: state and prove the path lifting lemma for
$p(t) = e^{2\pi it}$, define the degree, prove that it is a homotopy invariant and a homomorphism, and prove
surjectivity and injectivity.

**32.** Let $G$ be a topological group with identity $e$. Prove that $\pi_1(G,e)$ is abelian. (Hint: use the
multiplication $G\times G\to G$ and the Eckmann–Hilton style argument on the two loop compositions.)

**33.** Prove that every finitely presented group $G = \langle g_1,\dots,g_n \mid r_1,\dots,r_m\rangle$ is
isomorphic to the fundamental group of a finite $2$-dimensional CW complex. (Construct a "presentation
complex": one vertex, one $1$-cell per generator, one $2$-cell per relation.)

**34.** Prove that $\pi_1(\mathbb{RP}^2)\cong\mathbb{Z}/2$, using the double cover $S^2\to\mathbb{RP}^2$ and the
lifting criterion.

**35.** Prove that $SO(3)$ is homeomorphic to $\mathbb{RP}^3$, and deduce $\pi_1(SO(3))\cong\mathbb{Z}/2$. (A
careful construction of the homeomorphism is required; you may quote that $\pi_1(\mathbb{RP}^3)\cong
\mathbb{Z}/2$ from Exercise 34.)

**36.** Prove that $S^2$ is simply connected. State the values of $\pi_2(S^2)$ and $\pi_3(S^2)$, explain why
$\pi_3(S^2)\cong\mathbb{Z}$ is surprising (the Hopf fibration), and explain what this says about the difficulty
of computing homotopy groups in general. Cite your sources for the values you state.

**37.** Show that the fundamental group of the Klein bottle has the presentation
$\langle a, b \mid abab^{-1}\rangle$, that it is not abelian, and deduce that the Klein bottle is not
homeomorphic to the torus — even though both are closed surfaces with Euler characteristic $0$.
