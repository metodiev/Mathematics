# Algebraic Topology — Exercises

> [Algebraic Topology](README.md) · 36 problems · Beginner → Challenge · Solutions: [solutions.md](solutions.md)

Attempt every problem in writing before consulting [solutions.md](solutions.md). Problems marked
*(proof)* require a complete argument with all hypotheses stated. Section references point into
[README.md](README.md).

**Notation.** $D^n$ is the closed unit disk, $S^n$ the unit sphere, $T^2 = S^1 \times S^1$ the torus,
$K$ the Klein bottle, $\mathbb{R}P^n$ real projective space and $\mathbb{C}P^n$ complex projective
space. $\Sigma_g$ is the closed orientable surface of genus $g$ and $N_g$ the closed non-orientable
surface of genus $g$. $H_n(X) = H_n(X;\mathbb{Z})$ unless coefficients are displayed. $\tilde H_n$ is
reduced homology. $\chi$ is the Euler characteristic and $L(f)$ the Lefschetz number.

## Beginner

**1.** *(proof)* Let $X$ be path-connected and let $\alpha$ be a path in $X$ from $x_0$ to $x_1$.
Define $\varphi_\alpha : \pi_1(X,x_1) \to \pi_1(X,x_0)$ by $\varphi_\alpha([\gamma]) = [\alpha * \gamma * \bar\alpha]$.
Prove that $\varphi_\alpha$ is a group isomorphism and that it depends only on the homotopy class of
$\alpha$ relative to its endpoints.

**2.** For $k \in \mathbb{Z}$, let $f_k : S^1 \to S^1$ be $f_k(z) = z^k$. Compute $\deg(f_k)$ and the
induced homomorphism $(f_k)_* : H_1(S^1) \to H_1(S^1)$, including the cases $k = 0$ and $k < 0$.
Justify your answer.

**3.** Let $X$ be the boundary of a square, with vertices $v_0,v_1,v_2,v_3$ in cyclic order and edges
$e_{01}, e_{12}, e_{23}, e_{30}$. Compute $H_*^\Delta(X)$ directly from the simplicial chain complex.

**4.** Compute $H_*(X)$ and $\chi(X)$ for $X = S^1 \sqcup S^1 \sqcup \{\mathrm{pt}\}$. State which
theorem gives $H_0$ and verify the answer directly.

**5.** *(proof)* Prove that if $X$ is contractible, then $\tilde H_n(X) = 0$ for every $n \ge 0$.

**6.** Consider the chain complex
$$0 \to \mathbb{Z} \xrightarrow{\ \partial_2\ } \mathbb{Z} \xrightarrow{\ \partial_1\ } \mathbb{Z} \to 0$$
with $\partial_2$ multiplication by $2$ and $\partial_1 = 0$. Compute $H_0, H_1, H_2$.

**7.** *(proof)* Let $f : (C_*,\partial) \to (D_*,\partial')$ be a chain map. Prove that $f$ induces a
well-defined homomorphism $f_* : H_n(C_*) \to H_n(D_*)$, and that this construction is functorial:
$(g \circ f)_* = g_* \circ f_*$ and $(\operatorname{id})_* = \operatorname{id}$.

**8.** *(proof)* Let $X$ be nonempty and path-connected. Prove directly from the definition of singular
homology that $H_0(X) \cong \mathbb{Z}$, without quoting Theorem 7.4.1.

**9.** Compute $\chi(S^2)$, $\chi(T^2)$, $\chi(\mathbb{R}P^2)$ and $\chi(K)$ in two ways: from a CW
decomposition and from the Betti numbers.

**10.** Classify all connected covering spaces of $S^1$ up to isomorphism over $S^1$. For each one,
state the corresponding subgroup of $\pi_1(S^1)$ and the deck group.

**11.** *(proof)* Prove that the constant map $S^n \to S^n$ has degree $0$ and the identity has degree
$1$. Then exhibit a nonconstant map $S^1 \to S^1$ of degree $0$, and prove that its degree really is
$0$.

**12.** Compute $H_*(S^0)$ from the singular chain complex, and compute $\tilde H_*(S^0)$.

## Intermediate

**13.** *(proof)* Show that the Möbius band deformation retracts onto its core circle, and deduce its
homology and Euler characteristic.

**14.** Compute $H_*(X)$ for $X = S^2 \vee S^2 \vee S^1$. Justify each summand.

**15.** Let $X$ be the union of two copies of $S^2$ together with an arc joining a point of one sphere
to a point of the other. Compute $H_*(X)$ and $\chi(X)$.

**16.** Compute $H_*(\mathbb{R}P^4;\mathbb{Z})$ from the cellular chain complex. State the general
formula for $H_k(\mathbb{R}P^n;\mathbb{Z})$.

**17.** Compute $H_*(S^1 \times S^2;\mathbb{Z})$ in two ways: by the Künneth formula and by a direct
Mayer–Vietoris argument.

**18.** *(proof)* Use Mayer–Vietoris to compute $H_*(\Sigma_2)$, the closed orientable surface of genus
$2$. Verify the answer with the Euler characteristic and the classification of surfaces.

**19.** *(proof)* Let $f : S^n \to S^n$ have degree $d$. Prove that the induced map
$f^* : H^n(S^n;\mathbb{Z}) \to H^n(S^n;\mathbb{Z})$ is multiplication by $d$.

**20.** *(proof)* Prove that a map $f : S^n \to S^n$ of degree $1$ is surjective and is not
null-homotopic. Does the same conclusion hold for degree $-1$?

**21.** *(proof)* Prove that $\mathbb{R}P^n$ is orientable if and only if $n$ is odd.

**22.** *(proof)* Determine the number of connected $2$-sheeted covering spaces of $S^1 \vee S^1$ up to
isomorphism, and describe their total spaces.

**23.** *(proof)* Let $X$ be a connected graph with $V$ vertices and $E$ edges. Prove that
$H_1(X;\mathbb{Z}) \cong \mathbb{Z}^{E-V+1}$ and that $H_n(X) = 0$ for $n \ge 2$.

**24.** *(proof)* Let $X$ and $Y$ be finite CW complexes. Prove that $\chi(X \times Y) = \chi(X)\chi(Y)$
using the Künneth formula with field coefficients.

## Advanced

**25.** *(proof)* Prove that $\tilde H_k(S^n) \cong \mathbb{Z}$ for $k = n$ and vanishes otherwise, by
induction on $n$ using the reduced Mayer–Vietoris sequence. State every hypothesis you use.

**26.** *(proof)* Prove that the following two statements are equivalent: (i) every continuous map
$D^n \to D^n$ has a fixed point; (ii) there is no continuous retraction $D^n \to S^{n-1}$.

**27.** *(proof)* Let $A \in M_2(\mathbb{Z})$ with $\det A \ne 0$, and let $f_A : T^2 \to T^2$ be the
induced endomorphism. Prove that $L(f_A) = \det(I-A)$. If $\det(I-A) \ne 0$, prove that $f_A$ has
exactly $|\det(I-A)|$ fixed points.

**28.** *(proof)* Let $(C_*,\partial)$ be a finite chain complex of finite-dimensional vector spaces
over a field. Prove that
$$\sum_i (-1)^i \dim C_i = \sum_i (-1)^i \dim H_i(C_*).$$

**29.** *(proof)* Let $X$ be a finite simplicial complex with $\chi(X) \ne 0$. Prove that every continuous map
$f : X \to X$ homotopic to $\operatorname{id}_X$ has a fixed point. (More generally, the statement holds for
any compact triangulable space.)

**30.** *(proof)* Let $f : S^n \to S^n$ be fixed-point-free. Prove that
$\deg(f) = (-1)^{n+1}$. Show that the converse fails.

**31.** *(proof)* Prove that $H^n(X;\mathbb{Q}) \cong \operatorname{Hom}_{\mathbb{Q}}(H_n(X;\mathbb{Q}),\mathbb{Q})$
for every space $X$, and compute the Betti numbers of $T^2 \times S^2$.

**32.** *(proof)* Let $p : E \to B$ be a covering with $B$ path-connected and $E$ simply connected.
Prove that the deck group is isomorphic to $\pi_1(B,b_0)$ and that the covering is normal.

## Challenge

**33.** *(proof)* Prove the Lefschetz fixed point theorem for simplicial maps of a finite simplicial
complex: if $f : K \to K$ is simplicial and has no fixed simplex, then $L(f) = 0$. Deduce that a
continuous self-map of a compact triangulable space with $L(f) \ne 0$ has a fixed point. You may use
the simplicial approximation theorem.

**34.** *(proof)* The lens space $L(p,1)$ is the quotient of $S^3 \subset \mathbb{C}^2$ by the free
action of $\mathbb{Z}/p$ generated by $\zeta \cdot (z_1,z_2) = (\zeta z_1, \zeta z_2)$, where $\zeta$
is a primitive $p$-th root of unity. Using the standard CW structure with one cell in each dimension
$0,1,2,3$, compute $H_*(L(p,1);\mathbb{Z})$. Explain why the answer does not depend on the choice of
the generator $\zeta$.

**35.** *(proof)* Prove that $H^*(T^3;\mathbb{Z})$ is isomorphic, as a graded ring, to the exterior
algebra $\Lambda_{\mathbb{Z}}(\alpha,\beta,\gamma)$ on three generators of degree $1$. Compute all cup
products and verify that the ring is not commutative in the ordinary sense.

**36.** Let $X$ be a finite CW complex and let $f : X \to X$ be continuous. The **mapping torus** is
$$T_f = \frac{X \times [0,1]}{(x,0) \sim (f(x),1)}.$$
*(a)* State the Wang sequence relating $H_*(T_f;\mathbb{Q})$ to $H_*(X;\mathbb{Q})$ and $f_*$.
*(b)* Prove that, over $\mathbb{Q}$,
$$H_n(T_f;\mathbb{Q}) \cong \operatorname{coker}\bigl(f_* - \operatorname{id} \mid H_n(X;\mathbb{Q})\bigr) \oplus \ker\bigl(f_* - \operatorname{id} \mid H_{n-1}(X;\mathbb{Q})\bigr).$$
*(c)* Compute $H_*(T_f;\mathbb{Q})$ for $X = S^2$ and $f$ the antipodal map.
