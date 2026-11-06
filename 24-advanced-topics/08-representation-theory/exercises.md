# Representation Theory — Exercises

> [Representation Theory](README.md) · 36 problems · Beginner → Challenge · Solutions: [solutions.md](solutions.md)

Every problem names the section of the [tutorial](README.md) that supplies the method. Unless stated
otherwise $G$ is finite and all representations are over $\mathbb{C}$. The inner product is always
$\langle\chi,\psi\rangle_G = \frac{1}{\lvert G\rvert}\sum_{g}\chi(g)\overline{\psi(g)}$. Do not open
[solutions.md](solutions.md) before writing an attempt.

Notation: $\mathbb{1}$ is the trivial character, $\varepsilon$ the sign character, $\omega_n =
e^{2\pi i/n}$, $V_i$ the $i$-th irreducible representation, $d_i = \dim V_i$, and $\chi_\rho$ the
character of $\rho$. For $S_3$ the classes are written $e$, $\mathrm{tr}$ (transpositions) and
$3\mathrm{c}$ ($3$-cycles).

## Beginner

**1.** *(§5)* Let $C_3 = \langle r\rangle$ act on $\mathbb{R}^2$ by rotation through $120^\circ$. Write
down the matrix of $\rho(r)$, verify that $r \mapsto \rho(r)$ defines a homomorphism, and compute the
character on each element. Decide whether the complexification is irreducible.

**2.** *(§5, §7.8)* Write down the three matrices of the left regular representation of $C_3$ in the basis
$(e, r, r^2)$ and compute its character. Why does the answer not depend on the group?

**3.** *(§7.5)* Let $D_4$ act on the four vertices of a square (numbered $1,2,3,4$ cyclically). Compute
the character of the permutation representation on each of the five classes, and decompose it using the
table of Example 9.4.

**4.** *(§7.5)* For a one-dimensional representation $\chi$ of a finite group, prove that
$\chi(g^{-1}) = \overline{\chi(g)}$ directly from the definition, and verify it for the character
$\chi_1$ of $C_4$ with $\chi_1(r) = i$.

**5.** *(§7.6)* For the permutation character $\chi = (3,1,0)$ of $S_3$, compute $\langle\chi,\chi\rangle$
and explain why the answer is consistent with the decomposition $\mathbb{1}\oplus\chi_3$.

**6.** *(§7.6)* Using only the table of Example 7.27, verify that
$\langle\chi_3,\chi_3\rangle = 1$ and $\langle\chi_1,\chi_3\rangle = 0$, showing every term.

**7.** *(§7.3)* Let $V$ be a representation. Show that the fixed-point set
$V^{G} = \{v : \rho(g)v = v \ \forall g\in G\}$ is an invariant subspace, and compute $V^{G}$ for the
permutation representation of $S_3$ on $\mathbb{C}^3$.

**8.** *(§7.4)* Show that $V\mapsto V^{*}$ is an involution on isomorphism classes of representations, and
compute the character of $V^{*}$ for the two-dimensional rotation representation of $C_4$.

**9.** *(§7.8)* Compute the regular character of $C_5$ and decompose the regular representation into
irreducibles. Verify $\sum m_i^2 = \lvert C_5\rvert$.

**10.** *(§7.6)* For $S_3$ and the class function with values $(2,0,-1)$, compute
$\langle\chi,\chi\rangle$ and decide whether it is irreducible. Repeat for the class function with
values $(2,1,-2)$.

**11.** *(§7.2)* Let $C_2 = \langle s\rangle$ act on $\mathbb{C}^2$ by $\rho(s) =
\operatorname{diag}(1,-1)$. Exhibit two invariant lines and the corresponding decomposition. Is the
representation irreducible?

**12.** *(§7.9)* In $R(S_3)$, compute the products $[\varepsilon]\cdot[\chi_3]$ and $[\chi_3]^{2}$, and
verify associativity on the triple $([\mathbb{1}]+[\varepsilon])\cdot[\chi_3]\cdot[\chi_3]$.

## Intermediate

**13.** *(§7.11)* Write the full character table of $C_3\times C_3$ (nine characters) and verify row
orthogonality for one pair of rows and column orthogonality for one pair of columns by explicit
arithmetic.

**14.** *(§7.7)* The permutation character of $S_4$ on four letters is $\chi = (4,2,0,1,0)$ on the classes
$e$, transposition, double transposition, $3$-cycle, $4$-cycle. Compute $\langle\chi,\chi\rangle$ and
$\langle\chi,\mathbb{1}\rangle$, and deduce that the standard representation $V = \{x : \sum x_i = 0\}$ is
irreducible of dimension $3$. Why is this argument shorter than using the full character table?

**15.** *(§7.10)* Induce the trivial character of $C_2 = \{e,(12)\}\subset S_3$ to $S_3$. Compute the
induced character from the character formula and decompose it.

**16.** *(§7.11)* Write down all eight characters of $C_2\times C_4$ (with generators $a$ of order $2$ and
$b$ of order $4$) and verify that two distinct rows are orthogonal.

**17.** *(§7.7)* Compute the character table of $S_3\times C_2$ from the tables of $S_3$ and $C_2$,
and verify $\sum_i d_i^2 = 12$ and the number of classes.

**18.** *(§7.10)* Let $H = A_3\subset S_3$ and let $\psi$ be the one-dimensional representation of $A_3$
with $\psi((123)) = \omega_3$. Compute $\operatorname{Ind}_{H}^{S_3}\psi$ from the character formula and
identify it with an irreducible of $S_3$.

**19.** *(§7.5)* Prove that a one-dimensional representation is irreducible, that its character is a
homomorphism $G\to\mathbb{C}^{\times}$, and that $\chi(g)$ is a root of unity whose order divides
$\operatorname{ord}(g)$.

**20.** *(§8)* For the two-dimensional irreducible $E$ of $D_4$, compute the characters of
$\operatorname{Sym}^2E$ and $\Lambda^2E$ with Theorem 8.6 and decompose both using the table of
Example 9.4.

**21.** *(§7.9)* Show that the augmentation $\varepsilon : R(G)\to\mathbb{Z}$ is a ring homomorphism and
compute $\varepsilon$ on the element $[\chi_3]-[\mathbb{1}]\in R(S_3)$. Show that $\varepsilon$ has no
multiplicative inverse in $R(S_3)$.

**22.** *(§7.6)* Let $\chi$ be a one-dimensional character. Prove that $\chi\overline{\chi} = \mathbb{1}$
and that $\langle\chi,\mathbb{1}\rangle = 1$ if and only if $\chi = \mathbb{1}$.

**23.** *(§7.11)* For $G = C_6$, write the character table as a $6\times6$ matrix and compute the Fourier
transform of the delta function $\delta_e$ (the function equal to $1$ at $e$ and $0$ elsewhere). Verify
Fourier inversion for this function.

## Advanced

**24.** *(§7.4)* Let $\rho$ be an irreducible representation of dimension $d$ of a finite group $G$. Prove
that every element of the centre $Z(G)$ acts by a scalar, and deduce $d^{2}\le [G:Z(G)]$.

**25.** *(§7.8)* Prove that a finite group $G$ is abelian if and only if all its irreducible characters
have degree $1$. (Use $\sum_i d_i^2 = \lvert G\rvert$ and the number of conjugacy classes.)

**26.** *(§7.10)* Prove that induction is transitive:
$\operatorname{Ind}_{K}^{G}\bigl(\operatorname{Ind}_{H}^{K}W\bigr)\cong\operatorname{Ind}_{H}^{G}W$ for
$H\le K\le G$.

**27.** *(§7.10)* Prove that $\operatorname{Ind}_{H}^{G}\mathbb{1}_H$ is the permutation representation of
$G$ on $G/H$; that is, its character at $g$ equals the number of cosets fixed by $g$.

**28.** *(§7.11)* Prove that the number of one-dimensional representations of $G$ equals
$\lvert G/[G,G]\rvert$.

**29.** *(§7.5)* Let $\rho$ be an irreducible faithful representation with character $\chi$. Prove that
$\lvert\chi(g)\rvert = \chi(e)$ implies $g\in Z(G)$.

**30.** *(§7.12)* Verify the orthogonality of the $SO(3)$ characters for $l,m\in\{0,1,2\}$ by explicit
integration with the measure $\frac{2}{\pi}\sin^{2}(\theta/2)\,d\theta$ on $[0,\pi]$. Also verify the
identity $\chi_2^{2} = \chi_0+\chi_1+\chi_2+\chi_3+\chi_4$ at $\theta = 0.5$.

**31.** *(§7.7)* Prove that the character table of $C_n$, scaled by $1/\sqrt n$, is a unitary matrix, and
deduce Fourier inversion for functions on $C_n$ from the unitarity.

## Challenge

**32.** *(§7.7)* Compute the character table of $S_4$ from scratch: list the five classes with sizes,
determine the degrees, construct the characters (trivial, sign, standard, standard twisted by sign, and
one more), and verify both orthogonality relations.

**33.** *(§7.5)* Prove that every character of a finite group $G$ is real-valued if and only if every
element of $G$ is conjugate to its inverse.

**34.** *(§7.3, §12)* Count the colourings of the six faces of a cube with $2$ colours, and then with $3$
colours, up to rotation, by writing the permutation character of the rotation group on the faces and
applying Burnside's lemma. Check that the answers are $10$ and $57$.

**35.** *(§7.4)* The group $A_5$ has five conjugacy classes of sizes $1,15,20,12,12$ and irreducible
degrees $1,3,3,4,5$. Using only this data, prove that $A_5$ is simple.

**36.** *(§7.12)* Let $S^{1}$ act on $L^{2}(S^{1})$ by left translation. Show that each character
$z\mapsto z^{n}$ spans a one-dimensional invariant subspace, that distinct characters are orthogonal,
and explain why this is the infinite-dimensional analogue of Theorem 7.31. Compute the Fourier
coefficients of $f(z) = z + \bar z$ and verify Parseval's identity for it.
