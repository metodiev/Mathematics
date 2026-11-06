# Vector Spaces — Solutions

> [Tutorial](README.md) · [Exercises](exercises.md)

Every exercise is solved in full. Strategies are stated before computations, dimensions are always backed
by a named basis, and every proof quotes the theorem it uses.

## Beginner

**1.** *Answer:* only (a) and (d) are subspaces.

*(a)* $W = \{(x,y) : x = 0\}$ is the $y$-axis. It contains $(0,0)$; if $(0,y_1), (0,y_2) \in W$ then their
sum $(0, y_1 + y_2) \in W$; and $c(0,y) = (0, cy) \in W$. Subspace.

*(b)* Not a subspace: $(1,0) \in W$ but $(-1)(1,0) = (-1,0) \notin W$. Failure of closure under scalar
multiplication. (It is closed under addition, which shows that one closure alone is not enough.)

*(c)* Not a subspace: $(1,0) \in W$ and $(0,1) \in W$, but $(1,0) + (0,1) = (1,1) \notin W$ since
$xy = 1 \neq 0$. The set is the union of the two axes, which is not a subspace.

*(d)* $W = \{(x,y) : x + y = 0\}$ is the line $y = -x$. It contains $(0,0)$; if $x_1 + y_1 = 0$ and
$x_2 + y_2 = 0$ then $(x_1 + x_2) + (y_1 + y_2) = 0$; and $(cx) + (cy) = c(x + y) = 0$. Subspace.

*(e)* Not a subspace: $(0,0) \notin W$ because $0 + 0 \neq 1$. Any subspace must contain the zero vector.

**2.** *Proof.* Let $W \leq V$. Since $W$ is a vector space in its own right, it has an additive identity
$z \in W$ with $z + w = w$ for every $w \in W$. Choose any $w \in W$ (possible since $W \neq \varnothing$).
The equality $z + w = w$ holds in $V$; adding the inverse $-w \in V$ to both sides gives $z = \mathbf{0}$.
Hence $\mathbf{0} \in W$. $\blacksquare$

The empty set is closed under addition and scalar multiplication *vacuously* — every universally quantified
statement about its elements is true — yet it is not a vector space, because it has no element at all and
so no zero. The hypothesis $W \neq \varnothing$ is exactly what supplies an element $w$ from which
$\mathbf{0} = 0\cdot w$ is manufactured in the subspace test.

**3.** *Answer:* yes; basis $\{(3,1,0), (-2,0,1)\}$, so $\dim W = 2$.

*Subspace.* $\mathbf{0}$ satisfies $0 - 0 + 0 = 0$. If $x_i - 3y_i + 2z_i = 0$ for $i = 1, 2$, then
$(x_1 + x_2) - 3(y_1 + y_2) + 2(z_1 + z_2) = 0 + 0 = 0$. And
$(cx) - 3(cy) + 2(cz) = c(x - 3y + 2z) = 0$. By the subspace test, $W \leq \mathbb{R}^3$.

*Basis.* Solving for $x$: every element of $W$ is
$(3y - 2z,\ y,\ z) = y(3,1,0) + z(-2,0,1)$, so the two vectors span. They are independent: if
$a(3,1,0) + b(-2,0,1) = \mathbf{0}$ then the second coordinate gives $a = 0$ and the third gives $b = 0$.
Hence $\dim W = 2$.

*Check:* $(3,1,0)$ gives $3 - 3 + 0 = 0$ ✓ and $(-2,0,1)$ gives $-2 - 0 + 2 = 0$ ✓.

**4.** *Answer:* $(6,2) = 4(1,1) + 2(1,-1)$.

Solve $a(1,1) + b(1,-1) = (6,2)$, that is $a + b = 6$ and $a - b = 2$. Adding gives $2a = 8$, so $a = 4$;
then $b = 2$. *Check:* $4(1,1) + 2(1,-1) = (4,4) + (2,-2) = (6,2)$ ✓.

The two vectors are independent (neither is a multiple of the other), so the coefficients are unique; no
other combination gives $(6,2)$.

**5.** *Answer:* dependent.

$(1,3,7) = (1,2,3) + (0,1,4)$, so the relation

$$
1\cdot(1,2,3) + 1\cdot(0,1,4) - 1\cdot(1,3,7) = (0,0,0)
$$

has a nonzero coefficient. Hence the three vectors are linearly dependent. Equivalently, the matrix with
these rows has echelon form with a zero row.

**6.** *Answer:* yes, $(2,-1,3) = 2(1,0,1) - 1(0,1,-1)$.

*Check:* $2(1,0,1) + (-1)(0,1,-1) = (2,0,2) + (0,-1,1) = (2,-1,3)$ ✓. The coefficients are found by
reading coordinates: the first coordinate forces the coefficient of $(1,0,1)$ to be $2$; the second forces
the coefficient of $(0,1,-1)$ to be $-1$; the third then agrees automatically, which is what makes the
vector lie in the span.

**7.** *Proof.* Write $S = \{(1,0), (0,1)\}$.

*$\subseteq$.* Every element of $\operatorname{span}S$ has the form $a(1,0) + b(0,1) = (a,b)$ with
$a, b \in \mathbb{R}$, hence lies in $\mathbb{R}^2$.

*$\supseteq$.* Every $(a,b) \in \mathbb{R}^2$ equals $a(1,0) + b(0,1)$, a linear combination of elements of
$S$, hence lies in $\operatorname{span}S$.

Therefore $\operatorname{span}S = \mathbb{R}^2$. $\blacksquare$

**8.** *Answer:* no.

The set is linearly independent, but it does not span $\mathbb{R}^3$: $(0,0,1)$ is not of the form
$(a,b,0)$. A basis must both span and be independent, so this set is not a basis. (It is a basis of the
subspace $\{(x,y,0)\}$.)

**9.** *Answer:* $\dim = 1$, basis $\{(1,2)\}$.

$(2,4) = 2(1,2)$, so the second vector is redundant and
$\operatorname{span}\{(1,2),(2,4)\} = \operatorname{span}\{(1,2)\}$. A single nonzero vector is
independent (Lemma 7.5(3)), so it is a basis and the dimension is $1$.

**10.** *Answer:* $[(7,-4)]_B = (11, -15)^{\mathsf{T}}$.

Solve $a(2,1) + b(1,1) = (7,-4)$: the equations are $2a + b = 7$ and $a + b = -4$. Subtracting gives
$a = 11$, then $b = -15$. *Check:* $11(2,1) - 15(1,1) = (22 - 15,\ 11 - 15) = (7,-4)$ ✓.

**11.** *Answer:* only $B_1$ is a basis.

*$B_1$.* Two vectors in $\mathbb{R}^2$, neither a multiple of the other, hence independent (Lemma 7.5(4));
two independent vectors in a space of dimension $2$ form a basis.

*$B_2$.* $(2,4) = 2(1,2)$: dependent, so not a basis.

*$B_3$.* Three vectors in a two-dimensional space are necessarily dependent, so not a basis. (They do span,
which shows that spanning alone is not enough.)

*$B_4$.* One vector cannot span $\mathbb{R}^2$: $(0,1) \notin \operatorname{span}\{(1,0)\}$.

**12.** *Answer:* basis $\{(-1,1,0,0), (-1,0,1,0), (-1,0,0,1)\}$, so $\dim W = 3$.

Solving $x_1 = -x_2 - x_3 - x_4$ gives

$$
(x_1,x_2,x_3,x_4) = x_2(-1,1,0,0) + x_3(-1,0,1,0) + x_4(-1,0,0,1),
$$

so the three vectors span $W$. They are independent: a combination equal to $\mathbf{0}$ has second, third
and fourth coordinates $x_2, x_3, x_4$, which must therefore all be zero. Hence they form a basis and
$\dim W = 3$.

*Sanity check:* $W$ is the null space of the $1 \times 4$ matrix $(1\ 1\ 1\ 1)$ of rank $1$, so
$\dim W = 4 - 1 = 3$ by rank–nullity. ✓

**13.** *Proof.* *Spans.* By definition, $P_2$ consists of the polynomials $a + bx + cx^2$ with
$a, b, c \in \mathbb{R}$; each is a linear combination $a\cdot 1 + b\cdot x + c\cdot x^2$ of the three given
polynomials.

*Independent.* Suppose $a + bx + cx^2$ is the zero polynomial, that is, it vanishes at every real $x$. Two
polynomials are equal exactly when their coefficients agree, so $a = b = c = 0$; equivalently, evaluate at
$x = 0, 1, -1$ to obtain $a = 0$, $a + b + c = 0$ and $a - b + c = 0$, which force $b = c = 0$.

Hence $\{1, x, x^2\}$ is a basis and $\dim P_2 = 3$. $\blacksquare$

## Intermediate

**14.** *Answer:* $\operatorname{rank}A = 2$, $\operatorname{nullity}A = 2$; null basis
$\{(2,-1,1,0), (1,-1,0,1)\}$; column basis $\{(1,0,1), (2,1,3)\}$.

Row-reduce: $R_3 \leftarrow R_3 - R_1$ gives $(0,1,1,1)$, which equals $R_2$, so $R_3 \leftarrow R_3 - R_2$
gives a zero row. Then $R_1 \leftarrow R_1 - 2R_2$ gives $(1,0,-2,-1)$. The RREF is

$$
\begin{pmatrix}1 & 0 & -2 & -1\\ 0 & 1 & 1 & 1\\ 0 & 0 & 0 & 0\end{pmatrix}.
$$

*Null space.* Free columns $3$ and $4$. With $x_3 = 1, x_4 = 0$: $x_1 = 2$, $x_2 = -1$, giving $(2,-1,1,0)$.
With $x_3 = 0, x_4 = 1$: $x_1 = 1$, $x_2 = -1$, giving $(1,-1,0,1)$. These are independent (their third and
fourth coordinates form an identity block) and span the null space, so they are a basis.

*Column space.* The pivot columns are $1$ and $2$, so a basis of $\operatorname{Col}A$ consists of the
first two columns **of $A$**:

$$
(1,0,1)^{\mathsf{T}}, \qquad (2,1,3)^{\mathsf{T}}.
$$

*Verification of rank–nullity:* $2 + 2 = 4 = n$ ✓. *Verification of the null vectors:*
$A(2,-1,1,0)^{\mathsf{T}} = 2(1,0,1) - (2,1,3) + (0,1,1) = (0,0,0)$ ✓, and
$A(1,-1,0,1)^{\mathsf{T}} = (1,0,1) - (2,1,3) + (1,1,2) = (0,0,0)$ ✓.

**15.** *Proof.* *(i)* $\mathbb{R}^3 = U \oplus W$.

Every $(x,y,z) \in \mathbb{R}^3$ equals $(x,y,0) + (0,0,z)$, with $(x,y,0) \in U$ and $(0,0,z) \in W$; so
$\mathbb{R}^3 = U + W$. If a vector lies in $U \cap W$ then it is $(x,y,0)$ and $(0,0,z)$ at once, so
$x = y = 0$ and the vector is $(0,0,z)$ with $z$ arbitrary — but also $z = 0$ because the vector is in $U$.
Hence $U \cap W = \{\mathbf{0}\}$ and the sum is direct by Theorem 7.18. (Dimensions: $2 + 1 = 3$ ✓.)

*(ii)* $\mathbb{R}^2 = \operatorname{span}\{(1,1)\} \oplus \operatorname{span}\{(1,-1)\}$.

Every $(a,b) = \tfrac{a+b}{2}(1,1) + \tfrac{a-b}{2}(1,-1)$, so the sum is $\mathbb{R}^2$. If
$t(1,1) = s(1,-1)$ then $t = s$ from the first coordinate and $t = -s$ from the second, so $t = s = 0$ and
the intersection is $\{\mathbf{0}\}$. Hence the sum is direct. $\blacksquare$

**16.** *Proof.* ($\Leftarrow$) If $U \subseteq W$ then $U \cup W = W$, a subspace; similarly if
$W \subseteq U$.

($\Rightarrow$) Suppose $U \cup W$ is a subspace and, for contradiction, that neither contains the other.
Choose $u \in U \setminus W$ and $w \in W \setminus U$. Since $U \cup W$ is closed under addition,
$u + w \in U \cup W$. If $u + w \in U$ then $w = (u + w) - u \in U$ (as $U$ is a subspace and both terms lie
in $U$), contradicting $w \notin U$. If $u + w \in W$ then $u = (u + w) - w \in W$, contradicting
$u \notin W$. Either way we reach a contradiction, so one subspace contains the other. $\blacksquare$

**17.** *Answer:* $\dim U = 2$, $\dim W = 2$, $\dim(U \cap W) = 1$, $\dim(U + W) = 3$.

*The parts.* Neither spanning set consists of multiples, so each is independent (Lemma 7.5(4)) and
$\dim U = \dim W = 2$.

*Description of $U$.* A typical element is $a(1,1,0) + b(0,1,1) = (a, a + b, b)$, and
$x - y + z = a - (a+b) + b = 0$. Conversely, if $x - y + z = 0$ then $y = x + z$ and
$(x,y,z) = x(1,1,0) + z(0,1,1)$. So $U = \{(x,y,z) : x - y + z = 0\}$.

*The intersection.* $(1,2,1) \in W$ satisfies $1 - 2 + 1 = 0$, so $(1,2,1) \in U \cap W$; but
$(1,0,1) \in W$ has $1 - 0 + 1 = 2 \neq 0$, so $W \not\subseteq U$. Thus $U \cap W$ is a proper subspace of
the two-dimensional space $W$ containing a nonzero vector, hence $\dim(U \cap W) = 1$ with basis
$\{(1,2,1)\}$.

*The formula.* $\dim(U + W) = 2 + 2 - 1 = 3$, so $U + W = \mathbb{R}^3$. *Check* directly: the three
vectors $(1,1,0), (0,1,1), (1,0,1)$ are independent (their matrix has three pivots), and they all lie in
$U + W$, so $\dim(U + W) \geq 3$. ✓

**18.** *Proof.* *Subspaces.* Both contain the zero matrix. Since $(A + B)^{\mathsf{T}} = A^{\mathsf{T}} + B^{\mathsf{T}}$
and $(cA)^{\mathsf{T}} = cA^{\mathsf{T}}$, a sum or scalar multiple of symmetric matrices is symmetric, and
likewise for skew-symmetric ones. Hence both are subspaces.

*Dimensions.* A symmetric $2 \times 2$ matrix has the form
$\begin{pmatrix}a & b\\ b & c\end{pmatrix} = aE_{11} + b(E_{12} + E_{21}) + cE_{22}$, and the three
coefficient matrices are independent (look at the entries $(1,1)$, $(1,2)$ and $(2,2)$ in turn). So
$\dim\mathrm{Sym}_2 = 3$. A skew-symmetric matrix has the form
$\begin{pmatrix}0 & t\\ -t & 0\end{pmatrix} = t(E_{12} - E_{21})$, so $\dim\mathrm{Skew}_2 = 1$.

*Direct sum.* For any $A$,

$$
A = \tfrac12(A + A^{\mathsf{T}}) + \tfrac12(A - A^{\mathsf{T}}),
$$

where the first summand is symmetric and the second skew-symmetric; hence $M_2 = \mathrm{Sym}_2 + \mathrm{Skew}_2$.
If $A$ is both symmetric and skew then $A = A^{\mathsf{T}} = -A$, so $2A = 0$ and $A = 0$; the intersection is
$\{\mathbf{0}\}$. Therefore the sum is direct, and the dimensions agree: $3 + 1 = 4 = \dim M_2$ ✓.
$\blacksquare$

**19.** *Answer:* $\operatorname{rank}A = 3$, $\operatorname{nullity}A = 2$; null basis
$\{(-1,1,0,0,0), (0,0,0,-1,1)\}$; column basis $\{(1,2,1), (2,5,3), (1,3,3)\}$.

Row-reduce. $R_2 \leftarrow R_2 - 2R_1$ gives $(0,0,1,1,1)$; $R_3 \leftarrow R_3 - R_1$ gives
$(0,0,1,2,2)$; then $R_3 \leftarrow R_3 - R_2$ gives $(0,0,0,1,1)$. Finally
$R_2 \leftarrow R_2 - R_3$ gives $(0,0,1,0,0)$, and $R_1 \leftarrow R_1 - 2R_2 - R_3$ gives $(1,1,0,0,0)$.
The RREF is

$$
\begin{pmatrix}1 & 1 & 0 & 0 & 0\\ 0 & 0 & 1 & 0 & 0\\ 0 & 0 & 0 & 1 & 1\end{pmatrix}.
$$

Pivots in columns $1, 3, 4$, so $\operatorname{rank}A = 3$ and $\operatorname{nullity}A = 5 - 3 = 2$.

*Null space.* Free columns $2$ and $5$. With $x_2 = 1, x_5 = 0$: $x_1 = -1$, $x_3 = x_4 = 0$, giving
$(-1,1,0,0,0)$. With $x_2 = 0, x_5 = 1$: $x_4 = -1$, $x_1 = x_3 = 0$, giving $(0,0,0,-1,1)$.

*Column space.* Pivot columns $1, 3, 4$ **of $A$**: $(1,2,1)$, $(2,5,3)$, $(1,3,3)$.

*Check:* $A(-1,1,0,0,0)^{\mathsf{T}} = -(1,2,1) + (1,2,1) = \mathbf{0}$ ✓ and
$A(0,0,0,-1,1)^{\mathsf{T}} = -(1,3,3) + (1,3,3) = \mathbf{0}$ ✓.

**20.** *Answer:* $\{(1,1,0,0),\ (0,0,1,1),\ (0,1,0,0),\ (0,0,1,0)\}$ is a basis of $\mathbb{R}^4$.

*Independence.* Suppose $a(1,1,0,0) + b(0,0,1,1) + c(0,1,0,0) + d(0,0,1,0) = \mathbf{0}$. Reading
coordinates: the first gives $a = 0$; the fourth gives $b = 0$; the second gives $a + c = 0$, so $c = 0$;
the third gives $b + d = 0$, so $d = 0$. All coefficients vanish.

Four independent vectors in a space of dimension $4$ form a basis (an independent set of size
$\dim V$ spans, by Lemma 7.7 or by Theorem 7.10(2)). Hence the set is a basis of $\mathbb{R}^4$.

*Remark on method.* Why add $(0,1,0,0)$ first? It is not in the span of the two given vectors, because a
combination $a(1,1,0,0) + b(0,0,1,1)$ has second coordinate equal to its first and fourth equal to its
third; $(0,1,0,0)$ has $0 \neq 1$ in those positions. Then $(0,0,1,0)$ is not in the span of the three
already chosen. This is exactly the constructive step of Theorem 7.10(2).

**21.** *Proof.* Suppose

$$
a(v_1 + v_2) + b(v_2 + v_3) + c(v_3 + v_1) = \mathbf{0}.
$$

Rearranging, $(a + c)v_1 + (a + b)v_2 + (b + c)v_3 = \mathbf{0}$. Since $\{v_1, v_2, v_3\}$ is independent,

$$
a + c = 0, \qquad a + b = 0, \qquad b + c = 0 .
$$

From the first two, $c = -a$ and $b = -a$; substituting into the third gives $-2a = 0$, so $a = 0$ and then
$b = c = 0$. Hence the three combinations are independent. $\blacksquare$

*The field hypothesis.* The last step divides by $2$, which requires $2 \neq 0$ in $K$; that is, the field
must not have characteristic $2$. Over $\mathbb{F}_2$ the statement is false:
$(v_1 + v_2) + (v_2 + v_3) + (v_3 + v_1) = 2(v_1 + v_2 + v_3) = \mathbf{0}$ is a non-trivial relation with
all coefficients equal to $1$.

**22.** *Answer:* $[p] = (4, -3, 2)^{\mathsf{T}}$.

Solve $a\cdot 1 + b(1 + x) + c(1 + x + x^2) = 3 - x + 2x^2$. Comparing coefficients: $x^2$ gives $c = 2$;
$x$ gives $b + c = -1$, so $b = -3$; the constant term gives $a + b + c = 3$, so $a = 4$.
*Check:* $4 - 3(1 + x) + 2(1 + x + x^2) = 4 - 3 - 3x + 2 + 2x + 2x^2 = 3 - x + 2x^2$ ✓.

**23.** *Proof.* *(1)* Suppose $a\cdot 1 + b\,e^x = 0$ as functions, that is $a + be^x = 0$ for every real
$x$. Evaluating at $x = 0$ gives $a + b = 0$; evaluating at $x = 1$ gives $a + be = 0$. Subtracting,
$b(e - 1) = 0$, and since $e \neq 1$ we get $b = 0$, hence $a = 0$. So $\{1, e^x\}$ is independent.

*(2)* The identity $\sin^2 x + \cos^2 x = 1$ gives the non-trivial relation
$1\cdot 1 - 1\cdot\sin^2 x - 1\cdot\cos^2 x = 0$, so the three functions are dependent.

*A basis of the span.* $\{1, \sin^2 x\}$ is independent: if $a + b\sin^2x = 0$ for all $x$, then $x = 0$
gives $a = 0$ and $x = \pi/2$ gives $a + b = 0$, so $b = 0$. It spans the same space as
$\{1, \sin^2, \cos^2\}$ because $\cos^2 x = 1 - \sin^2 x$. Hence $\{1, \sin^2 x\}$ is a basis and the span
has dimension $2$. $\blacksquare$

**24.** *Proof.* Let $\mathcal{W} = \{W \leq V : S \subseteq W\}$.

*$\subseteq$.* By Theorem 7.4, $\operatorname{span}S$ is a subspace containing $S$, so
$\operatorname{span}S \in \mathcal{W}$; hence $\bigcap \mathcal{W} \subseteq \operatorname{span}S$.

*$\supseteq$.* Let $W \in \mathcal{W}$ and let $x \in \operatorname{span}S$, say
$x = a_1s_1 + \cdots + a_ks_k$ with $s_i \in S$. Each $s_i \in W$, and $W$ is closed under addition and
scalar multiplication, so $x \in W$ by induction on $k$ (starting from $\mathbf{0} \in W$ for $k = 0$).
Hence $\operatorname{span}S \subseteq W$ for every $W \in \mathcal{W}$, so
$\operatorname{span}S \subseteq \bigcap\mathcal{W}$.

Therefore $\operatorname{span}S = \bigcap\mathcal{W}$. $\blacksquare$

## Advanced

**25.** *Proof.* Let $W \subseteq V$ be non-empty and closed under addition and scalar multiplication. We
verify the ten axioms.

(A1) and (S1) are the two closure hypotheses. (A2), (A3), (S2), (S3), (S4), (S5) are equations that hold
for all elements of $V$; since every element of $W$ is an element of $V$ and the operations on $W$ are the
restrictions of those on $V$, each of these identities holds in $W$ without further work.

(A4): choose $w \in W$ (possible as $W \neq \varnothing$). By (S1) with $a = 0$,
$0\cdot w \in W$, and $0 \cdot w = \mathbf{0}$ by Theorem 7.1(3). So $\mathbf{0} \in W$ and serves as the
additive identity of $W$.

(A5): for $w \in W$, (S1) with $a = -1$ gives $(-1)w \in W$, and $(-1)w = -w$ by Theorem 7.1(5). So each
element of $W$ has its inverse in $W$.

Hence $W$ satisfies all ten axioms and is a vector space. $\blacksquare$

**26.** *Proof.* Induct on $m$.

*Base $m = 0$:* $0 \le n$ trivially.

*Step.* Assume the result for $m - 1 \geq 0$, and let $v_1, \dots, v_m$ be independent and
$w_1, \dots, w_n$ span $V$. Since $v_1 \neq \mathbf{0}$ (independence forbids zero vectors) and the $w_j$
span, there are scalars with $v_1 = \sum_j a_jw_j$, and not all $a_j$ are zero. Relabel so that $a_1 \neq 0$.
Then

$$
w_1 = a_1^{-1}\bigl(v_1 - a_2w_2 - \cdots - a_nw_n\bigr),
$$

so $w_1 \in \operatorname{span}\{v_1, w_2, \dots, w_n\}$ and therefore
$V = \operatorname{span}\{v_1, w_2, \dots, w_n\}$: this set contains $w_1$ in its span, hence all $w_j$, hence
all of $V$.

Now $\{v_2, \dots, v_m\}$ is independent (Lemma 7.5(2)) and $\{v_1, w_2, \dots, w_n\}$ is a spanning set
with $n$ elements. The induction hypothesis applies to these two families and gives $m - 1 \le n - 1$,
hence $m \le n$. $\blacksquare$

**27.** *Proof.* Let $T$ be a finite spanning set of $V$; enumerate $T = \{t_1, \dots, t_n\}$ and set
$S = T$. Consider the following procedure: if some $s \in S$ lies in $\operatorname{span}(S \setminus \{s\})$,
delete it; otherwise stop.

*The result still spans.* If $s \in \operatorname{span}(S \setminus \{s\})$, then
$\operatorname{span}(S \setminus \{s\}) = \operatorname{span}S = V$: the inclusion $\subseteq$ is clear,
and $s$ is recoverable from the rest, so nothing is lost. By induction on the number of deletions, the
current set always spans $V$.

*The procedure terminates* because each step lowers $|S|$ by one, and $S$ cannot become empty unless
$V = \{\mathbf{0}\}$ (the empty set spans only $\{\mathbf{0}\}$).

*At termination, $S$ is independent:* if $S$ were dependent, some $s \in S$ would be a non-trivial
combination of other elements of $S$ (take a relation $\sum a_is_i = \mathbf{0}$ with some $a_j \neq 0$ and
solve for $s_j$), contradicting the stopping condition. Hence the final $S$ is independent and spans, that
is, it is a basis. $\blacksquare$

**28.** *Proof.* Let $I$ be a linearly independent subset of the finite-dimensional space $V$, with
$n = \dim V$. If $I$ spans, it is a basis and we are done. Otherwise choose $v \notin \operatorname{span}I$;
by Lemma 7.5(5), $I \cup \{v\}$ is independent. Repeat this step.

*Termination.* Each step increases $|I|$ by one, and every independent set has at most $n$ elements: if
$J$ were independent with $|J| > n$, Lemma 7.7 applied with $S = J$ and $T$ a basis of $V$ would give
$|J| \le n$, a contradiction. So the process stops after at most $n - |I|$ steps, and it can stop only when
$I$ spans. Then $I$ is independent and spanning, that is, a basis. $\blacksquare$

**29.** *Proof.* Let $\{u_1, \dots, u_k\}$ be a basis of $\ker T$ and extend it, by Exercise 28, to a basis

$$
\{u_1, \dots, u_k,\ v_1, \dots, v_m\}
$$

of $V$; then $\dim V = k + m$. We show that $\{T(v_1), \dots, T(v_m)\}$ is a basis of $\operatorname{im}T$.

*It spans.* Let $w \in \operatorname{im}T$, say $w = T(x)$. Write
$x = \sum_i a_iu_i + \sum_j b_jv_j$. Then, by linearity and $T(u_i) = \mathbf{0}$,

$$
w = T(x) = \sum_i a_iT(u_i) + \sum_j b_jT(v_j) = \sum_j b_jT(v_j).
$$

*It is independent.* If $\sum_j b_jT(v_j) = \mathbf{0}$ then
$T\bigl(\sum_j b_jv_j\bigr) = \mathbf{0}$, so $\sum_j b_jv_j \in \ker T$ and there are scalars $a_i$ with
$\sum_j b_jv_j = \sum_i a_iu_i$. Hence $\sum_j b_jv_j - \sum_i a_iu_i = \mathbf{0}$, and independence of the
basis of $V$ forces every $b_j = 0$ (and every $a_i = 0$).

Therefore $\dim\operatorname{im}T = m$ and $\dim\ker T = k$, so
$\dim\ker T + \dim\operatorname{im}T = k + m = \dim V$. $\blacksquare$

**30.** *Proof.* Let $\{z_1, \dots, z_k\}$ be a basis of $U \cap W$. By Exercise 28 it extends to a basis
$\{z_1, \dots, z_k, u_1, \dots, u_m\}$ of $U$ and to a basis $\{z_1, \dots, z_k, w_1, \dots, w_\ell\}$ of
$W$; thus $\dim U = k + m$, $\dim W = k + \ell$ and $\dim(U \cap W) = k$.

*Claim:* $\mathcal{B} = \{z_1, \dots, z_k, u_1, \dots, u_m, w_1, \dots, w_\ell\}$ is a basis of $U + W$.

*Spans.* An element of $U + W$ is $u + w$ with $u \in U$, $w \in W$. Expressing $u$ in the basis of $U$ and
$w$ in the basis of $W$ and adding gives a combination of $\mathcal{B}$.

*Independent.* Suppose $\sum_i \alpha_iz_i + \sum_j \beta_ju_j + \sum_t \gamma_tw_t = \mathbf{0}$. Then

$$
\sum_t \gamma_tw_t = -\Bigl(\sum_i \alpha_iz_i + \sum_j \beta_ju_j\Bigr) \in W \cap U = U \cap W,
$$

so $\sum_t \gamma_tw_t = \sum_i \delta_iz_i$ for suitable $\delta_i$. Hence
$\sum_t \gamma_tw_t - \sum_i \delta_iz_i = \mathbf{0}$, and since
$\{z_1, \dots, z_k, w_1, \dots, w_\ell\}$ is a basis of $W$ it is independent, so all $\gamma_t = 0$ and all
$\delta_i = 0$. Then $\sum_i \alpha_iz_i + \sum_j \beta_ju_j = \mathbf{0}$, and independence of the basis of
$U$ gives all $\alpha_i = 0$, $\beta_j = 0$.

Consequently $\dim(U + W) = k + m + \ell$, and

$$
k + m + \ell = (k + m) + (k + \ell) - k = \dim U + \dim W - \dim(U \cap W). \qquad \blacksquare
$$

**31.** *Proof.* Let $W \leq V$ with $\dim V = n$. By Exercise 28, a basis $\{w_1, \dots, w_k\}$ of $W$
extends to a basis of $V$; hence $k \le n$, that is, $\dim W \le \dim V$, and $W$ is finite-dimensional.

If $k = n$, the basis of $W$ already has $n = \dim V$ elements and is independent, so it is a basis of $V$
(Lemma 7.7 with both sets of size $n$, or Theorem 7.8); in particular it spans $V$, and since all its
elements lie in $W$ we get $V = \operatorname{span}\{w_1, \dots, w_n\} \subseteq W$, so $W = V$.

Conversely if $W = V$ then trivially $\dim W = n$. $\blacksquare$

## Challenge

**32.** *Proof.* By the dimension formula (Theorem 7.19),

$$
\dim V = \dim(U + W) = \dim U + \dim W - \dim(U \cap W).
$$

The hypothesis $\dim V = \dim U + \dim W$ therefore forces $\dim(U \cap W) = 0$. A subspace of dimension $0$
has an empty basis, so it equals $\{\mathbf{0}\}$: indeed, any nonzero vector would be an independent
one-element set, giving dimension at least $1$. Hence $U \cap W = \{\mathbf{0}\}$, and by Theorem 7.18 the sum
is direct. $\blacksquare$

*Why the hypothesis $V = U + W$ is needed:* in $\mathbb{R}^3$ take $U = \operatorname{span}\{e_1\}$ and
$W = \operatorname{span}\{e_2\}$; then $\dim U + \dim W = 2 < 3 = \dim V$, but the two-span sum is only a
plane, and $U \cap W = \{\mathbf{0}\}$ does not produce $V$.

**33.** *Proof.* Induct on $m \geq 1$.

*$m = 1$:* a proper subspace satisfies $V_1 \neq V$, so $V \neq V_1$.

*Step.* Assume the statement for $m - 1$ proper subspaces. Let $V_1, \dots, V_m$ be proper. By the
induction hypothesis there is

$$
u \notin V_1 \cup \cdots \cup V_{m-1}.
$$

If $u \notin V_m$ we are done. Otherwise $u \in V_m$. Since $V_m$ is proper, choose $v \notin V_m$, and
consider the line

$$
\ell = \{v + tu : t \in K\}.
$$

*$\ell$ misses $V_m$:* if $v + tu \in V_m$ for some $t$, then $v = (v + tu) - tu \in V_m$ because
$u \in V_m$, contradicting the choice of $v$.

*$\ell$ meets each $V_i$ ($i < m$) in at most one point:* if $v + tu$ and $v + su$ both lie in $V_i$ with
$t \neq s$, then $(t - s)u = (v + su) - (v + tu) \in V_i$, so $u \in V_i$ (as $t - s \neq 0$), contradicting
the choice of $u$.

Hence at most $m - 1$ values of $t$ give a point of $\bigcup_{i<m} V_i$, and no value gives a point of
$V_m$. Since the field $K$ is infinite, choose $t$ avoiding those finitely many values; then
$v + tu \notin V_1 \cup \cdots \cup V_m$. Therefore the union is not all of $V$. $\blacksquare$

**34.** *Proof.* Let $P$ be the space of all polynomials over $K$. Suppose, for contradiction, that $P$ is
finite-dimensional; by Theorem 7.10(1) it has a finite spanning set $S = \{p_1, \dots, p_k\}$.

Let $N = \max\{\deg p_i : i = 1, \dots, k\}$ (with $N = 0$ if all $p_i$ are zero). Every linear combination
$\sum a_ip_i$ has degree at most $N$: the degree of a sum is at most the larger of the degrees, and
multiplying by a nonzero scalar does not change the degree. Hence

$$
P = \operatorname{span}S \subseteq \{p : \deg p \le N\} = P_N .
$$

But $x^{N+1} \in P$ has degree $N + 1 > N$, so $x^{N+1} \notin P_N$, a contradiction.

Therefore $P$ is not finitely spanned, that is, infinite-dimensional. $\blacksquare$

*Remark.* The argument shows more: any finite set of polynomials has a degree ceiling, so no finite set
spans $P$. The infinite set $\{1, x, x^2, \dots\}$ is linearly independent (a polynomial relation is an
identity, so all coefficients vanish), which is the other half of a basis.

**35.** *Answer (counterexample).* In $\mathbb{R}^2$ let

$$
U = \operatorname{span}\{(1,0)\}, \qquad V = \operatorname{span}\{(0,1)\}, \qquad W = \operatorname{span}\{(1,1)\}.
$$

Then $\dim U = \dim V = \dim W = 1$, and the pairwise intersections are all $\{\mathbf{0}\}$ (distinct lines
through the origin in $\mathbb{R}^2$ meet only at the origin), as is the triple intersection. The
right-hand side of the displayed formula is therefore $1 + 1 + 1 - 0 - 0 - 0 + 0 = 3$, while
$U + V + W = \mathbb{R}^2$ has dimension $2$. The formula fails.

*Why it fails.* Inclusion–exclusion counts each point of a union with a weight that sums to $1$; a sum of
subspaces is not a set-theoretic union, and a vector lying in $U + V$ need not lie in any one of the
subspaces. Here $(1,1) = (1,0) + (0,1)$ lies in $U + V$, and the three one-dimensional subspaces are not
independent of one another.

*Proof of the correct formula.* Apply Theorem 7.19 to the pair of subspaces $U + V$ and $W$ (both are
subspaces, and $U + V$ is finite-dimensional because $U$ and $V$ are):

$$
\dim\bigl((U + V) + W\bigr) = \dim(U + V) + \dim W - \dim\bigl((U + V) \cap W\bigr).
$$

Since $(U + V) + W = U + V + W$, this is the stated identity. Applying Theorem 7.19 once more to $U$ and $V$
turns it into

$$
\dim(U + V + W) = \dim U + \dim V - \dim(U \cap V) + \dim W - \dim\bigl((U + V) \cap W\bigr),
$$

which is the form in which the formula is usually used: the third term cannot be replaced by
$\dim(V \cap W) + \dim(U \cap W) - \dim(U \cap V \cap W)$. $\blacksquare$
