# Linear Transformations — Exercises

> [Tutorial](README.md) · [Solutions](solutions.md) · Level: Advanced

Thirty-eight problems, numbered continuously. The levels are cumulative: an Advanced problem may use a
Beginner technique, and nothing in a later level is needed earlier.

**How to use this set.**

* Attempt each problem on paper before opening [solutions.md](solutions.md). Reading a solution feels
  like learning and is not.
* For every map you claim is linear, verify **both** axioms with arbitrary inputs and arbitrary scalars.
  One example never proves linearity; one counterexample always disproves it.
* For every kernel and image, give a **basis**, not just a description, and check the rank–nullity
  identity $\dim V = \operatorname{nullity} + \operatorname{rank}$.
* Proof problems need complete sentences, every theorem named, and both inclusions whenever a set
  equality is claimed.
* Unless stated otherwise, vector spaces are over $\mathbb{R}$, bases are ordered, and coordinates are
  columns.

## Beginner

**1.** Decide whether each map is linear, giving a one-line reason in each case:

(a) $T(x,y) = (3x - y,\ 2y)$;
(b) $S(x,y) = (x^2 + y,\ y)$;
(c) $F(x,y) = (x - 1,\ y)$;
(d) $G(x,y) = (2xy,\ x)$.

**2.** Show from the definition that $T(x,y) = (x + 2y,\ 3x - y)$ is linear, and write its matrix
relative to the standard bases of $\mathbb{R}^2$.

**3.** For $T(x,y,z) = (x - y,\ y - z)$, find a basis of $\ker T$ and of $\operatorname{im}T$, and
verify rank–nullity.

**4.** Let $T(x,y,z) = (2x + y,\ y - z,\ x + z)$. Compute $T(1,-2,3)$, find $\ker T$, and decide from
the kernel whether $T$ is injective.

**5.** Write the matrix of rotation of the plane by $60^\circ$ counter-clockwise, and compute the images
of $\mathbf{e}_1$ and $\mathbf{e}_2$.

**6.** Write the matrix of reflection in the line $y = -x$. Apply it to $(2,3)$ and verify that the
matrix squared is the identity.

**7.** Write the matrix of orthogonal projection onto the $y$-axis, find its kernel and image, and verify
$P^2 = P$.

**8.** For the shear $T(x,y) = (x + 3y,\ y)$: give the matrix, the image of the unit square (list the
four vertices), and the kernel.

**9.** A linear map $T : \mathbb{R}^2 \to \mathbb{R}^2$ satisfies $T(1,0) = (2,-1)$ and
$T(0,1) = (3,4)$. Write its matrix and compute $T(2,5)$.

**10.** For differentiation $D$ on $\mathcal{P}_2 = \operatorname{span}(1,x,x^2)$ in the basis
$(1,x,x^2)$: write $[D]$, compute $D(3 - 2x + x^2)$ using the matrix, and give $\ker D$ and
$\operatorname{im}D$.

**11.** For $A = \begin{pmatrix}1&2\\2&4\end{pmatrix}$, describe $\ker T_A$ and $\operatorname{im}T_A$ as
lines in the plane and decide whether $T_A$ is injective.

**12.** Compute $[T]_C^B$ for $T(x,y) = (x+y,\ x-y)$, where $B = ((1,1),(1,-1))$ and $C$ is the standard
basis of $\mathbb{R}^2$.

## Intermediate

**13.** For $T(x,y,z) = (x+y,\ y+z,\ z+x)$: write the matrix, find the kernel, and decide whether $T$ is
an isomorphism.

**14.** For $A = \begin{pmatrix}1&2&3\\2&4&6\\1&1&1\end{pmatrix}$, find bases of $\ker T_A$ and
$\operatorname{im}T_A$ and verify rank–nullity.

**15.** For $a \in \mathbb{R}$ let $T_a(x,y,z) = (x + ay,\ y + az,\ ax + z)$. Determine exactly those
$a$ for which $T_a$ is an isomorphism, by solving $T_a(x,y,z) = \mathbf{0}$.

**16.** Let $S(x,y) = (x - y,\ 2y)$ and $T(x,y) = (3x,\ x + y)$. Compute the matrices of $T\circ S$ and
$S\circ T$, show they differ, and decide whether $T\circ S$ is injective.

**17.** For $T(x,y) = (3x + y,\ -x + 2y)$ and $B = ((1,1),(2,1))$, compute $[T]_B$ and verify the
columns against $T(\mathbf{b}_1)$ and $T(\mathbf{b}_2)$.

**18.** For $A = \begin{pmatrix}4&2\\1&3\end{pmatrix}$ and $P = \begin{pmatrix}1&1\\1&-1\end{pmatrix}$,
compute $P^{-1}AP$ and compare traces.

**19.** Let $D$ be differentiation on $\mathcal{P}_2$ and $B = (1+x,\ 1-x,\ x^2)$. Compute $[D]_B$, then
compute $[D]_B^2$ and compare with the matrix of $D^2$ in the same basis. Check rank–nullity for $D$.

**20.** Let $T$ be reflection in the line $y = x$ followed by rotation by $90^\circ$ counter-clockwise
(rotation applied second). Compute the matrix of $T$, identify $T$ geometrically, and state $\ker T$.

**21.** On $M_2(\mathbb{R})$, define $T(X) = X - X^{\mathsf{T}}$. Show that $T$ is linear, find
$\ker T$ and $\operatorname{im}T$, and verify rank–nullity with $\dim M_2(\mathbb{R}) = 4$.

**22.** Find the matrix of orthogonal projection onto the line spanned by $(3,4)$, verify $P^2 = P$, and
give $\ker P$ and $\operatorname{im}P$.

**23.** Construct a linear map $T : \mathbb{R}^3 \to \mathbb{R}^3$ whose kernel is
$\operatorname{span}\{(1,1,0)\}$ and whose image is
$\operatorname{span}\{(1,0,1),(0,1,1)\}$, and verify both properties.

## Advanced

**24.** Prove that for a linear $T : V \to W$ and any $S \subseteq V$,
$T(\operatorname{span}S) = \operatorname{span}T[S]$.

**25.** Let $T : V \to W$ be linear. Prove that $T[U]$ is a subspace of $W$ for every subspace
$U \subseteq V$, and that $T^{-1}[U']$ is a subspace of $V$ for every subspace $U' \subseteq W$.

**26.** Prove that a linear map $T : V \to W$ is injective if and only if it sends every linearly
independent list in $V$ to a linearly independent list in $W$.

**27.** Prove that if $T : V \to W$ is linear and $T(\mathbf{v}_1),\dots,T(\mathbf{v}_k)$ are linearly
independent, then $\mathbf{v}_1,\dots,\mathbf{v}_k$ are linearly independent. Give a counterexample to
the converse.

**28.** Prove that if $T : V \to V$ is linear over a finite-dimensional $V$ with $T^2 = 0$, then
$\operatorname{im}T \subseteq \ker T$ and $\operatorname{rank}T \le \tfrac12\dim V$. Construct such a
$T$ on $\mathbb{R}^4$ with $\operatorname{rank}T = 2$.

**29.** Let $T : V \to W$ be linear and $U \subseteq V$ a subspace, with $V$ finite-dimensional. Prove

$$
\dim T[U] = \dim U - \dim(U \cap \ker T),
$$

and deduce $\dim T[U] \le \dim U$.

**30.** Let $B$ be an ordered basis of the $n$-dimensional space $V$ and let $Q$ be an invertible
$n\times n$ matrix. Prove that there is exactly one ordered basis $B'$ of $V$ with
$[\operatorname{id}_V]_B^{B'} = Q$, and deduce that every matrix similar to $[T]_B$ is $[T]_{B'}$ for
some ordered basis $B'$.

**31.** Prove that a linear map $T : V \to W$, with $V$ finite-dimensional, is injective if and only if
there exists a linear $S : W \to V$ with $S\circ T = \operatorname{id}_V$.

**32.** Prove that two $n\times n$ matrices are similar if and only if they represent the same linear
map $V \to V$ relative to two bases of $V$. Deduce that
$\begin{pmatrix}1&1\\0&1\end{pmatrix}$ is not similar to $I_2$.

**33.** Let $T : V \to V$ be linear with $T^2 = T + 2\operatorname{id}_V$ and $V$ finite-dimensional.
Prove that $T$ is invertible, find $T^{-1}$ as a polynomial in $T$, and prove
$V = \ker(T - 2\operatorname{id}_V) \oplus \ker(T + \operatorname{id}_V)$.

## Challenge

**34.** Construct a linear map $T : \mathbb{R}^4 \to \mathbb{R}^4$ with
$\ker T = \operatorname{span}\{(1,1,1,1)\}$ and
$\operatorname{im}T = \{(x_1,x_2,x_3,x_4) : x_1 + x_2 + x_3 + x_4 = 0\}$. Write its matrix and verify
both properties.

**35.** On the space $V$ of real sequences $(x_1,x_2,x_3,\dots)$, let $R(x_1,x_2,\dots) =
(0,x_1,x_2,\dots)$ and $L(x_1,x_2,\dots) = (x_2,x_3,\dots)$. Prove that $R$ is injective but not
surjective, that $L$ is surjective but not injective, that $L\circ R = \operatorname{id}_V$, and that
$R\circ L \neq \operatorname{id}_V$. Explain why this does not contradict Corollary 7.13.

**36.** Let $T : V \to V$ be linear over $\mathbb{R}$ with $T^2 = -\operatorname{id}_V$ and $V$ finite-
dimensional. Prove that $T$ is an isomorphism and that $\mathbf{v}, T(\mathbf{v})$ are linearly
independent for every $\mathbf{v} \neq \mathbf{0}$. Then prove $\dim V$ is even, by the following
guided route: for $U = \operatorname{span}\{\mathbf{v}, T(\mathbf{v})\}$ and any projection $\pi$ onto
$U$, show that $\pi' = \tfrac12(\pi + T^{-1}\pi T)$ is a projection onto $U$ commuting with $T$, so that
$V = U \oplus \ker\pi'$ with both summands $T$-invariant; conclude by induction on $\dim V$.

**37.** Let $V$ be finite-dimensional, $T : V \to V$ linear, and suppose there is a linear
$S : V \to V$ with $S\circ T = \operatorname{id}_V$. Prove that $T$ is an isomorphism and that
$S = T^{-1}$. Show by an example that finite dimension is essential.

**38.** Determine every $2\times 2$ real matrix $A$ with $A^2 = I_2$. Prove your classification, and
interpret the non-obvious cases geometrically.
