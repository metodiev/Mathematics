# Vector Spaces — Exercises

> [Tutorial](README.md) · [Solutions](solutions.md) · Level: Advanced

Thirty-five problems, numbered continuously. The levels are cumulative: some Advanced problems reuse the
constructions of Beginner ones.

**How to use this set.**

* Attempt each problem before opening [solutions.md](solutions.md). For a proof, write the complete
  argument first and only then compare.
* Every time you claim that a set is a subspace, check all three conditions of the subspace test, unless
  you quote a theorem that does the work.
* Every time you claim a dimension, name a basis. A dimension asserted without a basis is a guess.
* Unless stated otherwise, $V$ is a vector space over a field $K$ (take $K = \mathbb{R}$ if you prefer),
  all dimensions are finite, and subspaces are non-empty.

## Beginner

**1.** Which of the following are subspaces of $\mathbb{R}^2$? Justify each answer.

$$
\text{(a) } \{(x,y) : x = 0\}, \quad
\text{(b) } \{(x,y) : x \geq 0\}, \quad
\text{(c) } \{(x,y) : xy = 0\}, \quad
\text{(d) } \{(x,y) : x + y = 0\}, \quad
\text{(e) } \{(x,y) : x + y = 1\}.
$$

**2.** Prove that every subspace of a vector space contains the zero vector. Explain why the hypothesis
"$W \neq \varnothing$" in the subspace test cannot be dropped, even though the empty set is vacuously
closed under addition and scalar multiplication.

**3.** Is $W = \{(x,y,z) \in \mathbb{R}^3 : x - 3y + 2z = 0\}$ a subspace of $\mathbb{R}^3$? If so, find a
basis of $W$ and state $\dim W$ with justification.

**4.** Express $(6,2)$ as a linear combination of $(1,1)$ and $(1,-1)$, and verify the coefficients.

**5.** Are $(1,2,3)$, $(0,1,4)$, $(1,3,7)$ linearly independent in $\mathbb{R}^3$? Justify your answer.

**6.** Is $(2,-1,3)$ in $\operatorname{span}\{(1,0,1),\, (0,1,-1)\}$? If so, exhibit the coefficients.

**7.** Prove that $\operatorname{span}\{(1,0), (0,1)\} = \mathbb{R}^2$ by proving both inclusions.

**8.** Is $\{(1,0,0), (0,1,0)\}$ a basis of $\mathbb{R}^3$? Explain.

**9.** Find $\dim\operatorname{span}\{(1,2), (2,4)\}$ in $\mathbb{R}^2$, with a basis.

**10.** Find the coordinates of $(7,-4)$ relative to the basis $B = \bigl((2,1), (1,1)\bigr)$ of
$\mathbb{R}^2$.

**11.** Which of the following are bases of $\mathbb{R}^2$? Justify each answer.

$$
B_1 = \{(1,1), (1,-1)\}, \quad
B_2 = \{(1,2), (2,4)\}, \quad
B_3 = \{(1,0), (0,1), (1,1)\}, \quad
B_4 = \{(1,0)\}.
$$

**12.** Find a basis of $W = \{(x_1,x_2,x_3,x_4) \in \mathbb{R}^4 : x_1 + x_2 + x_3 + x_4 = 0\}$ and
determine $\dim W$.

**13.** Show that $\{1, x, x^2\}$ is a basis of the space $P_2$ of polynomials of degree at most $2$.

## Intermediate

**14.** For

$$
A = \begin{pmatrix}1 & 2 & 0 & 1\\ 0 & 1 & 1 & 1\\ 1 & 3 & 1 & 2\end{pmatrix}
$$

find bases of $\operatorname{null}A$ and $\operatorname{Col}A$, and verify rank–nullity.

**15.** Let $U = \{(x,y,0) : x, y \in \mathbb{R}\}$ and $W = \operatorname{span}\{(0,0,1)\}$ in
$\mathbb{R}^3$. Prove that $\mathbb{R}^3 = U \oplus W$. Then prove that
$\mathbb{R}^2 = \operatorname{span}\{(1,1)\} \oplus \operatorname{span}\{(1,-1)\}$.

**16.** Prove that for subspaces $U, W \leq V$, the union $U \cup W$ is a subspace of $V$ if and only if
$U \subseteq W$ or $W \subseteq U$.

**17.** Let $U = \operatorname{span}\{(1,1,0), (0,1,1)\}$ and $W = \operatorname{span}\{(1,0,1), (1,2,1)\}$
in $\mathbb{R}^3$. Compute $\dim U$, $\dim W$, $\dim(U \cap W)$ and $\dim(U + W)$, and check the dimension
formula.

**18.** Let $\mathrm{Sym}_2 = \{A \in M_2 : A^{\mathsf{T}} = A\}$ and
$\mathrm{Skew}_2 = \{A \in M_2 : A^{\mathsf{T}} = -A\}$. Show that both are subspaces of $M_2$, find a basis
and the dimension of each, and show that $M_2 = \mathrm{Sym}_2 \oplus \mathrm{Skew}_2$.

**19.** For

$$
A = \begin{pmatrix}1 & 1 & 2 & 1 & 1\\ 2 & 2 & 5 & 3 & 3\\ 1 & 1 & 3 & 3 & 3\end{pmatrix}
$$

find $\operatorname{rank}A$, $\operatorname{nullity}A$, a basis of $\operatorname{null}A$ and a basis of
$\operatorname{Col}A$.

**20.** Extend $\{(1,1,0,0), (0,0,1,1)\}$ to a basis of $\mathbb{R}^4$, and verify that your four vectors
are linearly independent.

**21.** Prove that if $\{v_1, v_2, v_3\}$ is linearly independent in $V$, then
$\{v_1 + v_2,\ v_2 + v_3,\ v_3 + v_1\}$ is linearly independent. Where does the argument use the
hypothesis on the field?

**22.** Find the coordinates of $p(x) = 3 - x + 2x^2$ relative to the basis $(1,\ 1+x,\ 1+x+x^2)$ of $P_2$.

**23.** Consider the real vector space of functions $\mathbb{R} \to \mathbb{R}$.

1. Prove that $\{1, e^x\}$ is linearly independent.
2. Prove that $\{1, \sin^2 x, \cos^2 x\}$ is linearly dependent, and find a basis of its span.

**24.** Prove that $\operatorname{span}S = \bigcap\{W \leq V : S \subseteq W\}$; that is, the span is the
intersection of all subspaces containing $S$.

## Advanced

**25.** Prove the subspace test: if $W \subseteq V$ is non-empty and closed under addition and scalar
multiplication, then $W$ is a vector space.

**26.** Prove the Steinitz exchange lemma: if $\{v_1, \dots, v_m\}$ is linearly independent and
$\{w_1, \dots, w_n\}$ spans $V$, then $m \leq n$.

**27.** Prove that in a finite-dimensional space every spanning set contains a basis.

**28.** Prove that in a finite-dimensional space every linearly independent set extends to a basis.

**29.** Prove the rank–nullity theorem for linear maps: if $T : V \to W$ is linear and $V$ is
finite-dimensional, then $\dim\ker T + \dim\operatorname{im}T = \dim V$.

**30.** Prove that $\dim(U + W) = \dim U + \dim W - \dim(U \cap W)$ for finite-dimensional subspaces
$U, W$ of a vector space $V$.

**31.** Let $V$ be finite-dimensional with $\dim V = n$, and let $W \leq V$. Prove that $\dim W \leq n$,
with equality if and only if $W = V$.

## Challenge

**32.** Let $U, W \leq V$ with $V = U + W$ and $\dim V = \dim U + \dim W$. Prove that
$V = U \oplus W$.

**33.** Let $V$ be a finite-dimensional vector space over an infinite field $K$, and let
$V_1, \dots, V_m$ be proper subspaces. Prove that $V \neq V_1 \cup \cdots \cup V_m$.

**34.** Prove that the space $P$ of *all* polynomials (of every degree) is infinite-dimensional, over any
field.

**35.** Let $U, V, W$ be subspaces of a finite-dimensional space. Give an explicit example showing that

$$
\dim(U + V + W) \neq \dim U + \dim V + \dim W - \dim(U \cap V) - \dim(V \cap W) - \dim(U \cap W) + \dim(U \cap V \cap W),
$$

and prove that $\dim(U + V + W) = \dim(U + V) + \dim W - \dim((U + V) \cap W)$.
