# Category Theory — Exercises

> [Category Theory](README.md) · 40 problems · Beginner → Challenge · Solutions: [solutions.md](solutions.md)

Attempt every problem in writing before looking at [solutions.md](solutions.md). Problems marked
*(proof)* require a complete argument with all hypotheses stated. Section references point into
[README.md](README.md).

**Notation.** $\mathcal{C}(A,B)$ is the set of morphisms $A\to B$; $\operatorname{id}_A$ is the
identity; composition is right to left. $\mathbf{Set}$, $\mathbf{Grp}$, $\mathbf{Ring}$ (rings with
$1$), $\mathbf{Top}$, $\mathbf{Vect}_k$, $\mathbf{Pos}$ and $\mathbf{Mon}$ are the categories of
sets, groups, rings, spaces, vector spaces over $k$, posets and monoids. $\mathbb{N}_0=\{0,1,2,\dots\}$.
A **bimorphism** is a morphism that is both monic and epic. A category is **balanced** if every
bimorphism is an isomorphism.

## Beginner

**1.** Let $M=(\{0,1\},\cdot)$ be the multiplicative monoid with $0\cdot0=0$, $0\cdot1=1\cdot0=0$
and $1\cdot1=1$. Describe the one-object category $\mathbf{B}M$: its object, morphisms, identity and
composition. Is it a groupoid? What is a functor $\mathbf{B}M\to\mathbf{Set}$?

**2.** Determine an initial object and a terminal object, if they exist, in each of
$\mathbf{Set}$, $\mathbf{Top}$, $\mathbf{Grp}$, $\mathbf{Pos}$ and $\mathbf{Ring}$. State whether a
zero object exists.

**3.** Let $P=\{1,2,3\}$ with the usual order. Regard $P$ as a category. List all objects, all
morphisms, all identities and two nontrivial composites. Which morphisms are isomorphisms?

**4.** *(proof)* Let $x<y$ in a poset, and regard the poset as a category. Prove that the unique
morphism $x\to y$ is monic and epic, but not an isomorphism.

**5.** Let $f:\{1,2,3,4\}\to\{a,b,c\}$ be $f(1)=a$, $f(2)=b$, $f(3)=b$, $f(4)=c$. Decide whether
$f$ is monic and whether it is epic in $\mathbf{Set}$. For each failure, exhibit two maps that
witness it, and verify the equations.

**6.** Let $A=\{1,2\}$ and $B=\{x,y,z\}$ in $\mathbf{Set}$. List the elements of $A\times B$ and
$A\sqcup B$, state the projections and injections, and give the cardinalities. Explain why
$A\times B$ is not $A\sqcup B$ as a set.

**7.** Let $V,W$ be vector spaces over $k$. Show that $V\times W$ with coordinatewise operations,
together with the coordinate projections, is a product in $\mathbf{Vect}_k$. Show also that it is a
coproduct, with the evident injections. Where does the argument use finiteness?

**8.** For a function $f:A\to B$, define the covariant power-set functor on objects by
$\mathcal{P}(A)$ and on morphisms by $S\mapsto f[S]$, and the contravariant one by
$T\mapsto f^{-1}[T]$. Prove the functor laws in both cases, including the order reversal for the
contravariant case.

**9.** *(proof)* For a commutative ring $R$, let $\mathrm{GL}_n(R)$ be the group of invertible
$n\times n$ matrices and $R^\times$ its group of units. Show that
$\det:\mathrm{GL}_n(R)\to R^\times$ is a natural transformation
$\mathrm{GL}_n\Rightarrow(-)^\times$ of functors $\mathbf{CRing}\to\mathbf{Grp}$.

**10.** *(proof)* Prove that any two terminal objects of a category are isomorphic by a unique
isomorphism.

**11.** *(proof)* Prove that a functor sends isomorphisms to isomorphisms. Show that the converse
fails by considering the forgetful functor $\mathbf{Top}\to\mathbf{Set}$ and the identity map from
$\mathbb{R}$ with the discrete topology to $\mathbb{R}$ with the usual topology.

**12.** *(proof)* Prove that the Cartesian product $A\times B$ with the coordinate projections is a
product of $A$ and $B$ in $\mathbf{Set}$.

## Intermediate

**13.** *(proof)* In the category $\mathbf{Ab}$ of abelian groups, prove that a homomorphism is monic
if and only if it is injective, and epic if and only if it is surjective.

**14.** *(proof)* Let $i:\mathbb{Q}_{\ge0}\to\mathbb{Q}$ be the inclusion of the additive monoid of
non-negative rationals into the additive monoid of rationals. Prove that $i$ is a monomorphism and an
epimorphism in $\mathbf{Mon}$, but not an isomorphism. Conclude that $\mathbf{Mon}$ is not balanced.

**15.** *(proof)* In $\mathbf{Set}$, describe the equalizer and coequalizer of two functions
$f,g:A\to B$, and verify both universal properties.

**16.** Let $A=\{1,2,3,4\}$, $B=\{u,v,w\}$, $C=\{0,1\}$, with $f:A\to C$ given by $f(1)=0$,
$f(2)=1$, $f(3)=0$, $f(4)=1$, and $g:B\to C$ given by $g(u)=1$, $g(v)=0$, $g(w)=1$. Compute the
pullback $P=\{(a,b):f(a)=g(b)\}$, list its elements, and verify the universal property on a test
object $X$ with two maps satisfying the equation.

**17.** *(proof)* Let $\mathbf{2}$ be the category with two objects $0,1$ and one non-identity
morphism $u:0\to1$. Show that a functor $\mathbf{2}\to\mathcal{C}$ is exactly a morphism of
$\mathcal{C}$, and that a natural transformation between two such functors is exactly a commutative
square in $\mathcal{C}$. Describe the functor category $[\mathbf{2},\mathcal{C}]$.

**18.** *(proof)* Let $D:\mathbf{Vect}_k^{\mathrm{op}}\to\mathbf{Vect}_k$ be the dual-space functor
$V\mapsto V^*$, $T\mapsto T^*$. Show that $\operatorname{ev}_V:V\to V^{**}$,
$\operatorname{ev}_V(v)(\varphi)=\varphi(v)$, is a natural transformation
$\operatorname{id}\Rightarrow D\circ D$. Prove that it is an isomorphism for finite-dimensional $V$
and injective but not surjective for infinite-dimensional $V$.

**19.** *(proof)* For a fixed set $B$, verify the product-hom adjunction
$\mathbf{Set}(A\times B,C)\cong\mathbf{Set}(A,C^B)$. Give the unit, the counit and both triangle
identities.

**20.** *(proof)* Let $M$ be a monoid and let $F:\mathbf{B}M\to\mathbf{Set}$ be a functor, regarded as
a set with an $M$-action. Use the Yoneda lemma to prove that natural transformations from the regular
action $\mathbf{B}M(*,-)$ to $F$ correspond bijectively to elements of $F(*)$. Describe the
correspondence explicitly.

**21.** *(proof)* Explain how each of the following is a limit of a diagram: a terminal object, a
product $A\times B$, an equalizer of $f,g:A\to B$, and a pullback of $A\to C\leftarrow B$. State the
shape and the universal property in each case.

**22.** *(proof)* Let $F\dashv G$ with $F:\mathcal{C}\to\mathcal{D}$ and
$G:\mathcal{D}\to\mathcal{C}$. Suppose $\mathcal{D}$ has binary products. Prove that $G$ preserves
them: $G(A\times B)\cong G(A)\times G(B)$ naturally in $A,B$. Use the hom-set adjunction and the
Yoneda lemma, or a direct universal-property argument.

**23.** *(proof)* Let $T=\mathcal{P}:\mathbf{Set}\to\mathbf{Set}$ be the power-set functor, with
$\eta_X(x)=\{x\}$ and $\mu_X(\mathfrak{A})=\bigcup_{A\in\mathfrak{A}}A$ for
$\mathfrak{A}\subseteq\mathcal{P}(X)$. Prove that $(T,\eta,\mu)$ is a monad.

**24.** *(proof)* Prove that a morphism $f:A\to B$ is monic in $\mathcal{C}$ if and only if it is epic
in $\mathcal{C}^{\mathrm{op}}$. Then write the dual statements of: initial object, product, equalizer,
pullback, monomorphism, and left adjoint.

## Advanced

**25.** *(proof)* A category is **balanced** if every bimorphism is an isomorphism. Prove that
$\mathbf{Set}$ is balanced, and show that $\mathbf{Mon}$ and $\mathbf{Top}$ are not.

**26.** *(proof)* State and prove the Yoneda lemma, including naturality in $A$ and in $F$. Be explicit
about the local-smallness hypothesis and why the collection of natural transformations is a set.

**27.** *(proof)* Prove that right adjoints preserve limits and left adjoints preserve colimits. State
the theorem precisely, including which limits and colimits are assumed to exist.

**28.** *(proof)* Prove that the Yoneda embedding
$y:\mathcal{C}\to[\mathcal{C}^{\mathrm{op}},\mathbf{Set}]$, $A\mapsto\mathcal{C}(-,A)$, is fully
faithful. Deduce that if $\mathcal{C}(-,A)\cong\mathcal{C}(-,B)$ then $A\cong B$, with a unique
isomorphism.

**29.** *(proof)* Construct the free group functor $F:\mathbf{Set}\to\mathbf{Grp}$ and prove that it is
left adjoint to the forgetful functor $U:\mathbf{Grp}\to\mathbf{Set}$. Identify the unit, the counit
and verify both triangle identities.

**30.** *(proof)* Let $F\dashv G$ with $F:\mathcal{C}\to\mathcal{D}$ and
$G:\mathcal{D}\to\mathcal{C}$, unit $\eta$ and counit $\varepsilon$. Prove that
$T=G\circ F$, $\eta$ and $\mu=G\varepsilon F$ satisfy the monad laws.

**31.** *(proof)* Prove the pullback pasting lemma: in a commutative diagram of three objects in each
row and two squares, if the right square and the outer rectangle are pullbacks, then the left square
is a pullback; conversely, if the left and right squares are pullbacks, then the outer rectangle is a
pullback.

**32.** *(proof)* Let $\mathcal{C}$ have finite products and equalizers. Prove that $\mathcal{C}$ has
all finite limits, by constructing the limit of a finite diagram $D:\mathcal{J}\to\mathcal{C}$ as an
equalizer of two maps between products.

**33.** *(proof)* In $\mathbf{Ring}$, prove that the inclusion $\mathbb{Z}\to\mathbb{Q}$ is a
monomorphism and an epimorphism but not an isomorphism. Where does the argument use that the
homomorphisms are unital?

**34.** *(proof)* Prove that adjoints are unique up to natural isomorphism: if $F\dashv G$ and
$F'\dashv G$, then $F$ and $F'$ are naturally isomorphic. Explain in what sense the isomorphism is
unique.

## Challenge

**35.** *(proof)* Use the Yoneda embedding to prove the categorical Cayley theorem: every small
category embeds fully faithfully into a category of presheaves. Deduce that every monoid embeds into
the monoid of endofunctions of its underlying set.

**36.** *(proof)* For a functor $F:\mathcal{C}\to\mathbf{Set}$, define its **category of elements**
$\int F$: objects are pairs $(C,x)$ with $x\in F(C)$, and morphisms $(C,x)\to(D,y)$ are morphisms
$f:C\to D$ with $F(f)(x)=y$. Prove that $F$ is representable if and only if $\int F$ has an initial
object.

**37.** *(proof)* Prove that right adjoints preserve monomorphisms and left adjoints preserve
epimorphisms. Show that the forgetful functor $\mathbf{Ring}\to\mathbf{Set}$ is a right adjoint but
does not preserve epimorphisms, using $\mathbb{Z}\to\mathbb{Q}$.

**38.** *(proof)* Show that the list monad is the monad induced by the free-monoid adjunction
$F\dashv U$, and prove that its Kleisli category is equivalent to the category of free monoids.

**39.** *(proof)* Let $T=\mathcal{P}$ be the power-set monad. Prove that its Kleisli category is
isomorphic to the category $\mathbf{Rel}$ of sets and relations.

**40.** *(proof)* Prove that the Yoneda embedding preserves all limits that exist: if
$D:\mathcal{J}\to\mathcal{C}$ has a limit $(L,(\pi_j))$, then
$(y(L),(y(\pi_j)))$ is a limit of $y\circ D$. Explain why full faithfulness then implies that $y$
also reflects limits.
