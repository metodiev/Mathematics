# Algebraic Geometry — Exercises

> [Algebraic Geometry](README.md) · 36 problems · Beginner → Challenge · Solutions: [solutions.md](solutions.md)

Attempt every problem in writing before consulting [solutions.md](solutions.md). Problems marked *(proof)* require
a complete argument with all hypotheses stated. Section references point into [README.md](README.md).

**Notation.** $k$ is a field, $\mathbb{A}^n = k^n$ with the Zariski topology, $\mathbb{P}^n$ is projective
$n$-space, $V(S)$ and $I(X)$ are as in the tutorial, $\sqrt J$ is the radical of $J$, and $A(X) =
k[x_1,\dots,x_n]/I(X)$. "Alg. closed" means that $k$ is algebraically closed. $f_{\mathrm{red}}$ denotes the
product of the distinct irreducible factors of a nonzero polynomial $f$. The Legendre symbol is written
$\left(\frac{a}{p}\right)$ and equals $+1$ for a nonzero square, $-1$ for a nonsquare, and $0$ for $a \equiv 0$.

## Beginner

**1.** Compute $V(x^2+y^2-1) \cap V(y-x)$ in $\mathbb{A}^2(\mathbb{R})$ and in $\mathbb{A}^2(\mathbb{C})$. State the
number of points in each case and check the answers by substitution.

**2.** Let $I = (xy, y^2) \subseteq k[x,y]$. Show that $V(I) = V(y)$, that $I \subsetneq (y)$, and decide whether
$I$ is radical. Explain in one sentence why this does not contradict the Nullstellensatz.

**3.** Show that $(x^2+1)$ is a maximal ideal of $\mathbb{R}[x]$ but that $V(x^2+1) \subseteq \mathbb{A}^1(\mathbb{R})$
is empty. Then show that $(x^2+1)$ is not maximal in $\mathbb{C}[x]$ and compute its zero set there.

**4.** *(proof)* Let $S \subseteq k[x_1,\dots,x_n]$ and $X \subseteq \mathbb{A}^n$. Prove that
$V(S) = V(\langle S\rangle)$ and that $I(X)$ is a radical ideal.

**5.** *(proof)* Let $k$ be infinite. Prove that the Zariski closed subsets of $\mathbb{A}^1$ are exactly the finite
subsets and $\mathbb{A}^1$ itself. What happens when $k = \mathbb{F}_2$?

**6.** For $k$ algebraically closed, decide whether each of the following ideals of $k[x,y]$ is radical:
$(xy)$, $(x^2)$, $(x^2-y^2)$, $(x^2+y^2)$, $(x^2, xy)$. Justify each answer.

**7.** Let $X = \{(0,0), (1,0)\} \subseteq \mathbb{A}^2$. Compute $I(X)$, the coordinate ring $A(X)$, and exhibit an
explicit isomorphism $A(X) \cong k \times k$.

**8.** *(proof)* Show that $\{0\} \subseteq \mathbb{A}^2$ is Zariski closed, and that any two nonempty Zariski open
subsets of $\mathbb{A}^2$ have nonempty intersection. Deduce that the Zariski topology on $\mathbb{A}^2$ is not
Hausdorff.

**9.** Let $\psi : \mathbb{A}^1 \to \mathbb{A}^2$, $t \mapsto (t^2,t^5)$. Show that the image is $V(y^2-x^5)$, that
$\psi$ is bijective onto its image, and that $\psi$ is not an isomorphism onto its image.

**10.** *(proof)* Prove that $\mathbb{A}^1$ is irreducible over any field, and that $\mathbb{A}^n$ is irreducible
when $k$ is infinite. Deduce that $k[x_1,\dots,x_n]$ is an integral domain.

**11.** Describe $V(xy, xz) \subseteq \mathbb{A}^3$ as a union of two irreducible closed sets, compute its ideal,
and identify the irreducible components.

**12.** Compute the projective closure in $\mathbb{P}^2$ of the affine curve $C = V(y^2 - x^3 + x) \subseteq
\mathbb{A}^2$ and determine its points at infinity.

## Intermediate

**13.** *(proof)* Prove that $V(I) \cup V(J) = V(IJ) = V(I \cap J)$ for ideals $I, J \subseteq k[x_1,\dots,x_n]$,
and give an explicit example with $V(I) \cup V(J) \ne V(I+J)$.

**14.** *(proof)* Let $X$ be a nonempty algebraic set. Prove that $X$ is irreducible if and only if $A(X)$ has no
zero divisors. Prove also that if $k$ is algebraically closed, $X = X_1 \cup X_2$ with the $X_i$ closed, and
$X_1 \cap X_2 = \varnothing$, then $A(X) \cong A(X_1) \times A(X_2)$ and $A(X)$ contains an idempotent different
from $0$ and $1$.

**15.** Let $J = (x^2, xy) \subseteq k[x,y]$ with $k$ algebraically closed. Compute $\sqrt J$, $V(J)$ and
$I(V(J))$, and verify the Nullstellensatz in this case.

**16.** *(proof)* Let $0 \ne f \in k[x,y]$ have no repeated irreducible factor. Prove that $\dim V(f) = 1$, and find
all singular points of $C = V(y^2 - x^2(x+1))$.

**17.** *(proof)* Let $\varphi : X \to Y$ be a morphism of affine algebraic sets. Prove that $\varphi$ is continuous
for the Zariski topologies.

**18.** Let $C = V_p(X^2+Y^2-Z^2)$ and $L = V_p(X+Y-Z)$ over an algebraically closed field of characteristic
$\ne 2$. Compute $C \cap L$ with multiplicities and verify Bézout's theorem.

**19.** *(proof)* Consider the conic $C = V_p(XZ - Y^2) \subseteq \mathbb{P}^2$ and the map
$$\nu : \mathbb{P}^1 \to C, \qquad [S:T] \mapsto [S^2 : ST : T^2].$$
Prove that $\nu$ is a well-defined morphism and that it is bijective onto $C$, with inverse given by
$[X:Y:Z] \mapsto [X:Y]$ on the open set $X \ne 0$ and by $[X:Y:Z] \mapsto [Y:Z]$ on the open set $Z \ne 0$.
Deduce $C \cong \mathbb{P}^1$.

**20.** Let $X = V(x^2 - yz) \subseteq \mathbb{A}^3$ over an algebraically closed field. Compute $A(X)$, show that it
is a domain, and determine $\dim X$.

**21.** *(proof)* Prove that $\mathcal O_{\mathbb{P}^1}(\mathbb{P}^1) = k$, that is, every morphism
$\mathbb{P}^1 \to \mathbb{A}^1$ is constant. Deduce that $\mathbb{P}^1$ is not isomorphic to an affine variety.

**22.** *(proof)* Let $X$ be an irreducible affine variety and $U \subseteq X$ a nonempty open subset. Prove that
$U$ is dense in $X$ and that the restriction map $A(X) \to \mathcal O_X(U)$ is injective.

**23.** *(proof)* For an ideal $J \trianglelefteq k[x_1,\dots,x_n]$, prove that $\sqrt J$ is an ideal containing
$J$, that $\sqrt{\sqrt J} = \sqrt J$, and that $V(\sqrt J) = V(J)$. Give an example where $J \subsetneq \sqrt J$.

## Advanced

**24.** *(proof)* Prove the ideal–variety correspondence over an algebraically closed field: the maps $J \mapsto
V(J)$ and $X \mapsto I(X)$ are mutually inverse inclusion-reversing bijections between radical ideals and algebraic
sets, prime ideals correspond to irreducible algebraic sets, and maximal ideals correspond to points. Identify
exactly where algebraic closure is used.

**25.** *(proof)* Let $k$ be algebraically closed and let $0 \ne f \in k[x,y]$. Prove that
$$I(V(f)) = (f_{\mathrm{red}}).$$
Deduce that $V(f)$ is irreducible if and only if $f$ is a power of an irreducible polynomial.

**26.** *(proof)* Let $X \subseteq \mathbb{A}^n$ and $Y \subseteq \mathbb{A}^m$ be affine varieties over an
algebraically closed field. Prove that $A(X \times Y) \cong A(X) \otimes_k A(Y)$ and that $X \times Y$ is
irreducible.

**27.** *(proof)* Prove that $\mathbb{A}^1 \setminus \{0\}$ is isomorphic to $V(xy-1) \subseteq \mathbb{A}^2$, that
its ring of regular functions is $k[t,t^{-1}]$, and that it is not isomorphic to $\mathbb{A}^1$.

**28.** *(proof)* Let $k$ be algebraically closed and let $C, D \subseteq \mathbb{P}^2$ be projective plane curves of
degrees $m, n \ge 1$ with no common irreducible component. Prove, without assuming Bézout's theorem, that
$C \cap D$ has at most $mn$ points.

**29.** *(proof)* Let $E : y^2 = x^3+ax+b$ with $\Delta \ne 0$ over a field of characteristic $\ne 2,3$. Using the
chord–tangent definition and the explicit formulas, prove that (i) $O$ is an identity, (ii) $P + (-P) = O$,
(iii) the operation is commutative, (iv) $2P = O$ if and only if the $y$-coordinate of $P$ is $0$, and (v) $3P = O$
if and only if the tangent line at $P$ meets $E$ only at $P$. Derive the formulas for $x_3$ and $y_3$ from the
equation of the line.

**30.** Let $p = 11$ and $E : y^2 = x^3 + x + 1$ over $\mathbb{F}_p$. Compute $\#E(\mathbb{F}_p)$ using
$$\#E(\mathbb{F}_p) = p + 1 + \sum_{x \in \mathbb{F}_p} \left(\frac{f(x)}{p}\right), \qquad f(x) = x^3+x+1,$$
verify Hasse's bound, and determine the order of the point $P = (0,1)$.

**31.** *(proof)* Let $k$ be a field of characteristic $0$ and let $f \in k[x_1,\dots,x_n]$ be nonconstant with no
repeated irreducible factor. Prove that the singular locus of $X = V(f)$ is the closed set
$V\bigl(f, \partial f/\partial x_1, \dots, \partial f/\partial x_n\bigr)$ and that it is a proper subset of $X$.

## Challenge

**32.** *(proof)* Prove Zariski's lemma: a field that is finitely generated as a $k$-algebra is algebraic over $k$.
Deduce the weak Nullstellensatz for algebraically closed $k$, and explain precisely which step fails for
$k = \mathbb{R}$.

**33.** *(proof)* Let $E$ be a smooth projective cubic with a chosen point $O$, and let $\operatorname{Pic}^0(E)$ be
the group of degree-zero divisors modulo principal divisors. Prove that
$$\Phi : E(k) \to \operatorname{Pic}^0(E), \qquad P \mapsto \operatorname{cl}\bigl((P)-(O)\bigr)$$
is a bijection, and that the group structure transported from $\operatorname{Pic}^0(E)$ is the chord–tangent law.
You may use Riemann–Roch in the form: for a smooth projective curve of genus $1$ and a divisor $D$ of degree
$\ge 1$, the $k$-vector space of rational functions $f$ with $\operatorname{div}(f) + D \ge 0$ has dimension
$\deg D$. Deduce that the chord–tangent law is associative.

**34.** *(proof)* Prove that every automorphism of $\mathbb{P}^1$ (as a variety) is induced by a Möbius
transformation $[X:Y] \mapsto [aX+bY : cX+dY]$ with $ad-bc \ne 0$, and conversely.

**35.** *(proof)* Prove that any regular function on $\mathbb{A}^2 \setminus \{(0,0)\}$ extends to a polynomial on
$\mathbb{A}^2$. Deduce that $\mathbb{A}^2 \setminus \{(0,0)\}$ is not an affine variety.

**36.** *(proof)* Let $E : y^2 = x^3+ax+b$ have integer coefficients and let $p$ be a prime not dividing $2\Delta$.
Show that reduction modulo $p$ defines a group homomorphism $E(\mathbb{Q})_{\mathrm{good}} \to E(\mathbb{F}_p)$ on
the subgroup of points whose coordinates have denominators prime to $p$, and deduce that if $P \in E(\mathbb{Q})$ has
finite order $N$ with $p \nmid N$, then its reduction also has order $N$.
