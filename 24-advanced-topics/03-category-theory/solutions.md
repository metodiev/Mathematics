# Category Theory — Solutions

> [Category Theory](README.md) · Solutions to [exercises.md](exercises.md) · 40 problems

Each solution states the strategy, then carries out every step. Section references point into
[README.md](README.md). The notation is that of the exercises: composition is right to left,
$\mathbb{N}_0=\{0,1,2,\dots\}$, and $\mathbf{Ring}$ means rings with $1$ and unital homomorphisms.

## Beginner

**1.** **Strategy.** Use Definition 5.2.2: one object, morphisms are the elements of $M$, composition
is multiplication.

**Data.** The category $\mathbf{B}M$ has one object $*$. Its morphisms $*\to*$ are the two elements
$0$ and $1$. The identity is $1$. Composition is
$$ 1\circ1=1,\qquad 1\circ0=0,\qquad 0\circ1=0,\qquad 0\circ0=0. $$

**Axioms.** Multiplication in $M$ is associative, so composition is associative; $1$ is the
two-sided identity. Hence $\mathbf{B}M$ is a category.

**Groupoid?** A morphism $m$ is an isomorphism iff there is $n$ with $mn=1$. The element $0$ has no
inverse: $0\cdot n=0\ne1$ for both $n$. Thus $0$ is not an isomorphism, and $\mathbf{B}M$ is not a
groupoid.

**Functors to $\mathbf{Set}$.** A functor $F:\mathbf{B}M\to\mathbf{Set}$ consists of a set
$X=F(*)$ and an endomorphism $e=F(0):X\to X$, with $F(1)=\operatorname{id}_X$. Functoriality requires
$$ F(0\circ0)=F(0)=e=e\circ e=F(0)\circ F(0), $$
so $e^2=e$: the endomorphism is idempotent. Conversely, every set with an idempotent endomorphism
gives such a functor. Thus functors $\mathbf{B}M\to\mathbf{Set}$ are exactly sets equipped with an
idempotent.

**2.** **Strategy.** An initial object has a unique map out of it; a terminal object has a unique map
into it; a zero object is both.

* $\mathbf{Set}$: $\varnothing$ is initial (the empty function is the unique map $\varnothing\to X$);
  any singleton $\{\ast\}$ is terminal. There is no zero object, because no set is both empty and a
  singleton.
* $\mathbf{Top}$: $\varnothing$ with the empty topology is initial; a one-point space is terminal.
  There is no zero object for the same reason as in $\mathbf{Set}$.
* $\mathbf{Grp}$: the trivial group $\{e\}$ is initial and terminal, hence a zero object. The unique
  map from it is the constant homomorphism; the unique map to it is the trivial homomorphism.
* $\mathbf{Pos}$: the empty poset is initial (the empty map is monotone); a one-point poset is
  terminal. There is no zero object: the empty poset is not terminal, and a one-point poset is not
  initial when the target has more than one element, because there are several monotone maps from a
  point into such a poset.
* $\mathbf{Ring}$: $\mathbb{Z}$ is initial, because a unital ring homomorphism
  $\mathbb{Z}\to R$ must send $n$ to $n\cdot1_R$; the zero ring is terminal, because the only unital
  homomorphism $R\to\{0\}$ sends every element to $0$. There is no zero object: the zero ring is not
  initial, since there is no unital homomorphism from it to a nontrivial ring (it would force
  $1=0$).

**3.** **Objects.** $1,2,3$.

**Morphisms.** Since the order is total, there is a unique morphism $x\to y$ exactly when $x\le y$.
Thus the morphisms are
$$ \operatorname{id}_1:1\to1,\quad \operatorname{id}_2:2\to2,\quad \operatorname{id}_3:3\to3,\quad
1\to2,\quad 1\to3,\quad 2\to3. $$

**Composites.** $(1\to2)\circ\operatorname{id}_1=1\to2$; the composite of $1\to2$ with $2\to3$ is
$1\to3$. Also $(1\to3)\circ\operatorname{id}_1=1\to3$ and
$\operatorname{id}_3\circ(2\to3)=2\to3$.

**Isomorphisms.** A morphism $x\to y$ is an isomorphism iff there is a morphism $y\to x$, i.e. iff
$x\le y$ and $y\le x$, hence iff $x=y$. Therefore only the three identities are isomorphisms.

**4.** **Strategy.** Use the fact that a poset category has at most one morphism between any two
objects.

**Monic.** Let $g,h:z\to x$ with $f\circ g=f\circ h$, where $f:x\to y$ is the unique arrow. The
hom-set $\mathcal{P}(z,x)$ has at most one element, so $g=h$ automatically. Hence $f$ is monic.

**Epic.** Let $u,v:y\to w$ with $u\circ f=v\circ f$. The hom-set $\mathcal{P}(y,w)$ has at most one
element, so $u=v$. Hence $f$ is epic.

**Not an isomorphism.** An inverse would be a morphism $y\to x$. But $y\le x$ is false because
$x<y$, so no such morphism exists. Hence $f$ is not an isomorphism. This is a bimorphism that is not
an isomorphism.

**5.** **Strategy.** In $\mathbf{Set}$, monic means injective and epic means surjective.

**Image.** $f(1)=a$, $f(2)=b$, $f(3)=b$, $f(4)=c$, so the image is $\{a,b,c\}$. Hence $f$ is
surjective and therefore epic.

**Epic directly.** If $u\circ f=v\circ f$ for $u,v:\{a,b,c\}\to X$, then
$$ u(a)=u(f(1))=v(f(1))=v(a),\quad u(b)=u(f(2))=v(f(2))=v(b),\quad u(c)=u(f(4))=v(f(4))=v(c), $$
so $u=v$.

**Not monic.** $f(2)=f(3)=b$ with $2\ne3$. Let $g,h:\{\ast\}\to\{1,2,3,4\}$ be $g(\ast)=2$,
$h(\ast)=3$. Then $f\circ g=f\circ h$ because both send $\ast$ to $b$, but $g\ne h$. Hence $f$ is
not monic.

**6.** **Product.** $A\times B$ has the six ordered pairs
$$ (1,x),(1,y),(1,z),(2,x),(2,y),(2,z). $$
The projections are $\pi_A(a,b)=a$ and $\pi_B(a,b)=b$.

**Coproduct.** Model the disjoint union as
$$ A\sqcup B=(A\times\{0\})\cup(B\times\{1\}), $$
so its five elements are $(1,0),(2,0),(x,1),(y,1),(z,1)$. The injections are
$\iota_A(a)=(a,0)$ and $\iota_B(b)=(b,1)$.

**Cardinalities.** $|A\times B|=2\cdot3=6$ and $|A\sqcup B|=2+3=5$.

**Why not equal.** The elements of $A\times B$ are ordered pairs with a first coordinate in $A$ and a
second in $B$; the elements of $A\sqcup B$ are tagged elements remembering only which summand they
came from. For example, $(1,x)$ is not an element of $A\sqcup B$, and $(1,0)$ is not an element of
$A\times B$. The two constructions have different universal properties: maps *into* $A\times B$ are
pairs of maps into $A$ and $B$; maps *out of* $A\sqcup B$ are pairs of maps out of $A$ and $B$.

**7.** **Product.** Let $V\times W$ have coordinatewise addition and scalar multiplication. The
projections $\pi_V(v,w)=v$, $\pi_W(v,w)=w$ are linear. Given linear maps $T:X\to V$ and
$S:X\to W$, define $h:X\to V\times W$ by $h(x)=(T(x),S(x))$. Then $h$ is linear and
$\pi_V h=T$, $\pi_W h=S$. If $h'$ is another such map, then for every $x$,
$$ h'(x)=(\pi_V h'(x),\pi_W h'(x))=(T(x),S(x))=h(x), $$
so $h'=h$. Hence $V\times W$ is a product.

**Coproduct.** Define $i_V(v)=(v,0)$ and $i_W(w)=(0,w)$. They are linear. Given linear maps
$T:V\to X$ and $S:W\to X$, define $h:V\times W\to X$ by $h(v,w)=T(v)+S(w)$. Then $h$ is linear,
$h(i_V(v))=T(v)$ and $h(i_W(w))=S(w)$. If $h'$ is another such map, then
$$ h'(v,w)=h'(i_V(v)+i_W(w))=h'(i_V(v))+h'(i_W(w))=T(v)+S(w)=h(v,w), $$
so $h'=h$. Hence $V\times W$ is a coproduct.

**Finiteness.** The same formulas work for any finite family. For an infinite family, the product is
the full direct product, while the coproduct is the direct sum of tuples with only finitely many
nonzero entries; the two are different. The argument above uses that every element of the product is
a *finite* sum of its coordinate pieces, which fails for infinite families.

**8.** **Covariant.** For $S\subseteq A$,
$$ \mathcal{P}(\operatorname{id}_A)(S)=\operatorname{id}_A[S]=S, $$
so identities are preserved. For $f:A\to B$, $g:B\to C$ and $S\subseteq A$,
$$ \mathcal{P}(g\circ f)(S)=(g\circ f)[S]=\{g(f(s)):s\in S\}=g[f[S]]=\mathcal{P}(g)(\mathcal{P}(f)(S)). $$
Hence $\mathcal{P}$ is a covariant functor.

**Contravariant.** For $T\subseteq B$,
$$ \mathcal{P}(\operatorname{id}_B)(T)=\operatorname{id}_B^{-1}[T]=T. $$
For $f:A\to B$, $g:B\to C$ and $T\subseteq C$,
$$ \mathcal{P}(g\circ f)(T)=(g\circ f)^{-1}[T]=\{a\in A:g(f(a))\in T\}=f^{-1}[g^{-1}[T]]
=\mathcal{P}(f)(\mathcal{P}(g)(T)). $$
The order of $f$ and $g$ is reversed, which is exactly contravariance.

**Order reversal.** If $S\subseteq T\subseteq B$, then $f^{-1}[S]\subseteq f^{-1}[T]$; preimage is
monotone but reverses the direction of the morphism $f:A\to B$ to $f^{-1}:\mathcal{P}(B)\to\mathcal{P}(A)$.

**9.** **Strategy.** Naturality is the equation
$\det_S(\mathrm{GL}_n(\varphi)(A))=\varphi(\det_R(A))$ for every ring homomorphism
$\varphi:R\to S$ and every $A\in\mathrm{GL}_n(R)$.

**Functors.** For a commutative ring $R$, $\mathrm{GL}_n(R)$ is a group under matrix multiplication,
and a ring homomorphism $\varphi:R\to S$ induces a group homomorphism
$\mathrm{GL}_n(\varphi):\mathrm{GL}_n(R)\to\mathrm{GL}_n(S)$ by applying $\varphi$ entrywise. This
preserves identities and composition because $\varphi$ preserves $1$, addition and multiplication.
The unit group $(-)^\times$ is also a functor: $\varphi$ restricts to a group homomorphism
$R^\times\to S^\times$, since units map to units with inverse $\varphi(a^{-1})$.

**Naturality.** The determinant is a polynomial with integer coefficients in the entries:
$$ \det(A)=\sum_{\sigma\in S_n}\operatorname{sgn}(\sigma)\prod_{i=1}^n a_{i,\sigma(i)}. $$
A ring homomorphism preserves finite sums and products, so
$$ \det(\varphi(A))=\sum_{\sigma}\operatorname{sgn}(\sigma)\prod_i\varphi(a_{i,\sigma(i)})
=\varphi\!\left(\sum_{\sigma}\operatorname{sgn}(\sigma)\prod_i a_{i,\sigma(i)}\right)
=\varphi(\det(A)). $$
This is exactly the naturality square
$$ \begin{array}{ccc}
\mathrm{GL}_n(R) & \xrightarrow{\det_R} & R^\times\\
{\scriptstyle \mathrm{GL}_n(\varphi)}\downarrow & & \downarrow{\scriptstyle \varphi|_{R^\times}}\\
\mathrm{GL}_n(S) & \xrightarrow{\det_S} & S^\times.
\end{array} $$
Thus $\det$ is a natural transformation. (For $n=0$ both groups are trivial and the statement is
also true; the interesting case is $n\ge1$.)

**10.** **Strategy.** Use the uniqueness of the map from a terminal object to itself.

Let $1$ and $1'$ be terminal. There is a unique morphism $u:1\to1'$ and a unique morphism
$v:1'\to1$. Then $v\circ u:1\to1$ is a morphism from $1$ to itself. The identity
$\operatorname{id}_1$ is another, and terminality says there is exactly one morphism $1\to1$; hence
$v\circ u=\operatorname{id}_1$. Similarly $u\circ v=\operatorname{id}_{1'}$. Thus $u$ is an
isomorphism.

**Uniqueness.** If $u':1\to1'$ is any isomorphism, it is in particular a morphism $1\to1'$; by
terminality of $1'$ there is only one such morphism, namely $u$. Hence $u'=u$.

**11.** **Preservation.** Let $f:A\to B$ be an isomorphism with inverse $g$. Then
$$ F(f)\circ F(g)=F(f\circ g)=F(\operatorname{id}_B)=\operatorname{id}_{F(B)},\qquad
F(g)\circ F(f)=F(g\circ f)=F(\operatorname{id}_A)=\operatorname{id}_{F(A)}. $$
Hence $F(f)$ is an isomorphism with inverse $F(g)$.

**Converse failure.** Let $X$ be $\mathbb{R}$ with the discrete topology and $Y$ be $\mathbb{R}$ with
the usual topology. The identity function $f:X\to Y$ is continuous: every subset of $X$ is open, so
the preimage of every open set is open. It is bijective. Its inverse $Y\to X$ is not continuous,
because $\{0\}$ is open in $X$ but not open in $Y$ (every neighbourhood of $0$ in $Y$ contains
points other than $0$). Hence $f$ is a continuous bijection but not a homeomorphism.

The forgetful functor $\mathbf{Top}\to\mathbf{Set}$ sends $f$ to the identity function on
$\mathbb{R}$, which is an isomorphism in $\mathbf{Set}$. But $f$ is not an isomorphism in
$\mathbf{Top}$. Therefore the converse of "functors preserve isomorphisms" fails.

**12.** **Strategy.** Verify the universal property of Definition 7.4.1.

Let $P=A\times B$ with projections $\pi_A(a,b)=a$ and $\pi_B(a,b)=b$.

**Existence.** Given $f:X\to A$ and $g:X\to B$, define $h:X\to P$ by
$h(x)=(f(x),g(x))$. Then for every $x$,
$$ \pi_A(h(x))=f(x),\qquad \pi_B(h(x))=g(x), $$
so $\pi_A\circ h=f$ and $\pi_B\circ h=g$.

**Uniqueness.** If $h':X\to P$ also satisfies $\pi_A\circ h'=f$ and $\pi_B\circ h'=g$, then for every
$x$,
$$ h'(x)=(\pi_A(h'(x)),\pi_B(h'(x)))=(f(x),g(x))=h(x). $$
Hence $h'=h$.

Therefore $(P,\pi_A,\pi_B)$ is a product of $A$ and $B$ in $\mathbf{Set}$.

## Intermediate

**13.** **Strategy.** For monomorphisms, use maps out of $\mathbb{Z}$; for epimorphisms, use the
quotient by the image.

**Monic $\Leftrightarrow$ injective.** If $f$ is injective and $f\circ g=f\circ h$, then
$f(g(x))=f(h(x))$ for all $x$, so $g=h$. Conversely, suppose $f(a)=f(b)$ with $a\ne b$. Define
$g,h:\mathbb{Z}\to A$ by $g(1)=a$ and $h(1)=b$. These are group homomorphisms because $\mathbb{Z}$ is
cyclic, and $g\ne h$. But $f\circ g=f\circ h$ since both send $1$ to $f(a)=f(b)$. Hence $f$ is not
monic.

**Epic $\Leftrightarrow$ surjective.** If $f$ is surjective and $g\circ f=h\circ f$, then for every
$b\in B$ choose $a$ with $f(a)=b$ and conclude $g(b)=h(b)$; so $g=h$. Conversely, suppose $f$ is
epic and let $K=\operatorname{im}f$. Since $A$ is abelian, $K$ is a subgroup of $B$ and the quotient
$B/K$ is an abelian group. Let $q:B\to B/K$ be the quotient map and let $0:B\to B/K$ be the zero
homomorphism. For every $a\in A$, $q(f(a))=0$ because $f(a)\in K$; hence $q\circ f=0\circ f$. By
epicity, $q=0$. Therefore every element of $B$ lies in $K$, so $K=B$ and $f$ is surjective.

**14.** **Strategy.** Injectivity gives monicity; the inverse equation gives epicity.

**Monic.** The inclusion $i:\mathbb{Q}_{\ge0}\to\mathbb{Q}$ is injective. If $f\circ i=g\circ i$ for
monoid homomorphisms $f,g:\mathbb{Q}\to M$, then $f(q)=g(q)$ for every $q\ge0$. This is not yet all
of $\mathbb{Q}$; monicity is proved directly: if $i$ is injective and $i\circ u=i\circ v$ for
$u,v:N\to\mathbb{Q}_{\ge0}$, then $u(n)=v(n)$ for every $n$, so $u=v$. Hence $i$ is monic.

**Not surjective.** Negative rationals are not in the image.

**Epic.** Let $u,v:\mathbb{Q}\to M$ be monoid homomorphisms with $u\circ i=v\circ i$. Thus
$u(q)=v(q)$ for every $q\ge0$. For $q<0$, put $p=-q>0$. Then
$$ u(q)u(p)=u(q+p)=u(0)=e_M, $$
so $u(q)$ is an inverse of $u(p)$ in $M$; similarly $v(q)$ is an inverse of $v(p)=u(p)$. Inverses in
a monoid are unique: if $xa=e$ and $ay=e$, then $x=xe=x(ay)=(xa)y=ey=y$. Hence $u(q)=v(q)$. Every
rational is non-negative or negative, so $u=v$. Therefore $i$ is epic.

**Not an isomorphism.** An isomorphism in $\mathbf{Mon}$ has an inverse function, hence is
bijective; $i$ is not surjective. So $i$ is a bimorphism that is not an isomorphism, and
$\mathbf{Mon}$ is not balanced.

**15.** **Equalizer.** Let
$$ E=\{a\in A:f(a)=g(a)\} $$
and let $e:E\to A$ be the inclusion. Then $f\circ e=g\circ e$. If $h:X\to A$ satisfies
$f\circ h=g\circ h$, then every $h(x)$ lies in $E$, so $h$ factors as $h=e\circ k$ with
$k:X\to E$, $k(x)=h(x)$. The map $k$ is unique because $e$ is injective. Thus $(E,e)$ is the
equalizer.

**Coequalizer.** Let $\sim$ be the equivalence relation on $B$ generated by the pairs
$f(a)\sim g(a)$ for $a\in A$. Let $Q=B/\!\sim$ and let $q:B\to Q$ be the quotient map. Then
$q\circ f=q\circ g$ because $f(a)$ and $g(a)$ are equivalent for every $a$.

Given $h:B\to X$ with $h\circ f=h\circ g$, define a relation $R$ on $B$ by $xRy$ iff $h(x)=h(y)$.
This is an equivalence relation, and it contains every generating pair $f(a)\sim g(a)$ because
$h(f(a))=h(g(a))$. Hence $R$ contains the generated equivalence relation $\sim$. Therefore $h$ is
constant on $\sim$-classes, so there is a unique function $k:Q\to X$ with $k\circ q=h$. Thus
$(Q,q)$ is the coequalizer.

**16.** **Compute $P$.** $P=\{(a,b)\in A\times B:f(a)=g(b)\}$.

For $a=1$, $f(1)=0$; the only $b$ with $g(b)=0$ is $v$, so $(1,v)\in P$.
For $a=2$, $f(2)=1$; $g(u)=1$ and $g(w)=1$, so $(2,u),(2,w)\in P$.
For $a=3$, $f(3)=0$; again $(3,v)\in P$.
For $a=4$, $f(4)=1$; $(4,u),(4,w)\in P$.

Thus
$$ P=\{(1,v),(2,u),(2,w),(3,v),(4,u),(4,w)\}. $$

**Square.** Let $p:P\to A$, $q:P\to B$ be the coordinate projections. For every $(a,b)\in P$,
$f(p(a,b))=f(a)=g(b)=g(q(a,b))$ by the definition of $P$. Hence $f\circ p=g\circ q$.

**Universal property.** Let $X$ be a set with maps $u:X\to A$, $v:X\to B$ satisfying
$f\circ u=g\circ v$. Define $h:X\to P$ by $h(x)=(u(x),v(x))$. The equation ensures
$h(x)\in P$. Then $p(h(x))=u(x)$ and $q(h(x))=v(x)$. If $h'$ also satisfies $p\circ h'=u$ and
$q\circ h'=v$, then
$$ h'(x)=(p(h'(x)),q(h'(x)))=(u(x),v(x))=h(x), $$
so $h'=h$. Thus $P$ is the pullback. As a test, take $X=\{\ast\}$, let $u:X\to A$ send $\ast$ to
$2$, and let $v:X\to B$ send $\ast$ to the element $u\in B$; then $f(2)=1=g(u)$, and the unique
map sends $\ast$ to $(2,u)$.

**17.** **Functors.** The category $\mathbf{2}$ has objects $0,1$, identities $\operatorname{id}_0$,
$\operatorname{id}_1$, and one non-identity morphism $u:0\to1$. A functor $F:\mathbf{2}\to\mathcal{C}$
is determined by the objects $A=F(0)$, $B=F(1)$ and the morphism $f=F(u):A\to B$. There are no
nontrivial composites to check: the only composites are $u\circ\operatorname{id}_0=u$ and
$\operatorname{id}_1\circ u=u$, which are automatic. Thus functors $\mathbf{2}\to\mathcal{C}$ are
exactly morphisms $f:A\to B$ of $\mathcal{C}$.

**Natural transformations.** Let $F,G:\mathbf{2}\to\mathcal{C}$ correspond to $f:A\to B$ and
$g:C\to D$. A natural transformation $\eta:F\Rightarrow G$ has components
$\eta_0:A\to C$ and $\eta_1:B\to D$. The only non-identity morphism of $\mathbf{2}$ is $u:0\to1$,
so the only naturality square is
$$ \begin{array}{ccc}
A & \xrightarrow{f} & B\\
{\scriptstyle \eta_0}\downarrow & & \downarrow{\scriptstyle \eta_1}\\
C & \xrightarrow{g} & D.
\end{array} $$
It commutes exactly when $\eta_1\circ f=g\circ\eta_0$. Thus natural transformations are exactly
commutative squares.

**The functor category.** $[\mathbf{2},\mathcal{C}]$ is the **arrow category** $\mathcal{C}^{\to}$:
objects are morphisms of $\mathcal{C}$; morphisms are commutative squares; composition is
componentwise. The identity on $f:A\to B$ is the square with both components identities.

**18.** **Functoriality.** For $T:V\to W$, the transpose $T^*:W^*\to V^*$ is
$T^*(\varphi)=\varphi\circ T$. For composable $S:U\to V$, $T:V\to W$,
$$ (T\circ S)^*(\varphi)=\varphi\circ T\circ S=S^*(T^*(\varphi))=(S^*\circ T^*)(\varphi), $$
so $D(T\circ S)=D(S)\circ D(T)$: $D$ is contravariant. Also $(\operatorname{id}_V)^*=\operatorname{id}_{V^*}$.
Thus $D\circ D$ is covariant.

**Naturality.** For $v\in V$ and $\psi\in W^*$,
$$ \operatorname{ev}_W(T(v))(\psi)=\psi(T(v)), $$
while
$$ (T^{**}(\operatorname{ev}_V(v)))(\psi)=\operatorname{ev}_V(v)(T^*(\psi))
=T^*(\psi)(v)=\psi(T(v)). $$
Hence $\operatorname{ev}_W(T(v))=T^{**}(\operatorname{ev}_V(v))$, i.e.
$\operatorname{ev}_W\circ T=T^{**}\circ\operatorname{ev}_V$. This is the naturality square
$$ \begin{array}{ccc}
V & \xrightarrow{\operatorname{ev}_V} & V^{**}\\
{\scriptstyle T}\downarrow & & \downarrow{\scriptstyle T^{**}}\\
W & \xrightarrow{\operatorname{ev}_W} & W^{**}.
\end{array} $$

**Finite-dimensional case.** If $v\ne0$, extend $\{v\}$ to a basis of $V$ and define a linear
functional $\varphi$ with $\varphi(v)=1$ and $\varphi=0$ on the other basis elements. Then
$\operatorname{ev}_V(v)(\varphi)=1\ne0$, so $\operatorname{ev}_V$ is injective. In finite dimension,
$\dim V^{**}=\dim V^*=\dim V$, so an injective linear map $V\to V^{**}$ between spaces of the same
finite dimension is an isomorphism.

**Infinite-dimensional case.** The map is still injective by the same basis argument (extend a
nonzero vector to a basis). It is not surjective. To see this, identify $V$ with the direct sum
$\bigoplus_{b\in B}k$ for an infinite basis $B$. Then $V^*=W:=\prod_{b\in B}k$, and $V^{**}$ is the
dual of $W$. Let $U=\bigoplus_{b\in B}k\subseteq W$ be the subspace of finite-support functions.
Since $B$ is infinite, $W/U\ne0$; choose a nonzero linear functional $\lambda:W/U\to k$ (extend a
nonzero element of the quotient to a basis and define $\lambda$ on the basis). Let
$\Phi=\lambda\circ q:W\to k$, where $q:W\to W/U$ is the quotient map. Then $\Phi\in V^{**}$ and
$\Phi$ vanishes on $U$. But for every nonzero $v\in V$, the evaluation functional
$\operatorname{ev}_V(v):W\to k$ does not vanish on all of $U$: choose $b$ with $v_b\ne0$ and let
$u\in U$ be the function with $u(b)=1$ and $u(b')=0$ for $b'\ne b$; then
$\operatorname{ev}_V(v)(u)=u(v)=v_b\ne0$. Hence $\Phi\ne\operatorname{ev}_V(v)$ for every $v\in V$,
so $\operatorname{ev}_V$ is not surjective. (This argument uses a basis of the quotient, hence the
axiom of choice.)

**19.** **Bijection.** Define
$$ \Phi:\mathbf{Set}(A\times B,C)\to\mathbf{Set}(A,C^B),\qquad
\Phi(f)(a)(b)=f(a,b). $$
Its inverse is
$$ \Psi:\mathbf{Set}(A,C^B)\to\mathbf{Set}(A\times B,C),\qquad
\Psi(g)(a,b)=g(a)(b). $$
Then $\Phi(\Psi(g))=g$ and $\Psi(\Phi(f))=f$ by the definitions of currying and evaluation, so
$\Phi$ is a bijection.

**Naturality.** For $h:A'\to A$, $f:A\times B\to C$ and $a'\in A'$,
$$ \Phi(f\circ(h\times\operatorname{id}_B))(a')(b)=f(h(a'),b)=\Phi(f)(h(a'))(b), $$
so $\Phi$ is natural in $A$. For $k:C\to C'$,
$$ \Phi(k\circ f)(a)(b)=k(f(a,b))=k(\Phi(f)(a)(b)), $$
so $\Phi$ is natural in $C$. Hence $F(A)=A\times B$ is left adjoint to $G(C)=C^B$.

**Unit and counit.** The unit is
$$ \eta_A:A\to(A\times B)^B,\qquad \eta_A(a)(b)=(a,b). $$
The counit is
$$ \varepsilon_C:C^B\times B\to C,\qquad \varepsilon_C(g,b)=g(b). $$

**Triangle identities.** First,
$$ \varepsilon_{A\times B}\circ(\eta_A\times\operatorname{id}_B)(a,b)
=\varepsilon_{A\times B}(\eta_A(a),b)=\eta_A(a)(b)=(a,b), $$
so $\varepsilon_{F(A)}\circ F(\eta_A)=\operatorname{id}_{F(A)}$.
Second,
$$ (G(\varepsilon_C)\circ\eta_{G(C)})(g)(b)
=\varepsilon_C(g,b)=g(b), $$
so $G(\varepsilon_C)\circ\eta_{G(C)}=\operatorname{id}_{G(C)}$. Both triangles hold.

**20.** **Set-up.** The one-object category $\mathbf{B}M$ has a unique object $*$; its hom-set
$\mathbf{B}M(*,*)$ is $M$. A functor $F:\mathbf{B}M\to\mathbf{Set}$ is a set $X=F(*)$ with a function
$F(m):X\to X$ for each $m\in M$, subject to $F(e)=\operatorname{id}_X$ and
$F(mn)=F(m)\circ F(n)$; this is a left $M$-action, written $m\cdot x=F(m)(x)$.

**Hom functor.** The covariant hom functor $\mathbf{B}M(*,-)$ sends the unique object to
$\mathbf{B}M(*,*)=M$; on a morphism $m:*\to*$ it sends $g:*\to*$ to $m\circ g=m\cdot g$. Thus it is
the regular left action of $M$ on itself.

**Yoneda bijection.** By the Yoneda lemma,
$$ \operatorname{Nat}\big(\mathbf{B}M(*,-),F\big)\cong F(*)=X. $$
The bijection sends a natural transformation $\alpha$ to $x=\alpha_*(\operatorname{id}_*)\in X$.
Conversely, an element $x\in X$ gives
$$ \alpha_m=\alpha^{(x)}_m=F(m)(x)=m\cdot x. $$
Thus natural transformations from the regular action to $F$ are exactly the maps
$m\mapsto m\cdot x$ for $x\in X$; these are precisely the $M$-equivariant maps
$M\to X$ from the regular action. Hence they correspond bijectively to elements of $X=F(*)$.

**21.** **Terminal object.** The empty diagram has no objects and no morphisms. A cone over it is
just an object $X$ (there are no structure maps to choose). A limit is an object $1$ such that every
$X$ has a unique morphism $X\to1$. That is exactly a terminal object.

**Product.** Let $\mathcal{J}$ be the discrete category with two objects $1,2$. A diagram is a pair
$A_1,A_2$. A cone over it is an object $X$ with morphisms $x_1:X\to A_1$ and $x_2:X\to A_2$. A limit
is an object $A_1\times A_2$ with projections $\pi_i$ such that every such pair $(x_1,x_2)$ factors
uniquely through the projections. That is exactly the product.

**Equalizer.** Let $\mathcal{J}$ be the parallel pair $\bullet\rightrightarrows\bullet$ with two
parallel morphisms $f,g:A\to B$. A cone over it is a morphism $h:X\to A$ with $f\circ h=g\circ h$.
A limit is an object $E$ with $e:E\to A$ such that every such $h$ factors uniquely through $e$. That
is exactly the equalizer.

**Pullback.** Let $\mathcal{J}$ be the cospan $1\to2\leftarrow3$, i.e. a diagram
$A\xrightarrow{f}C\xleftarrow{g}B$. A cone over it is an object $X$ with maps $u:X\to A$,
$v:X\to B$ such that $f\circ u=g\circ v$. A limit is an object $P$ with $p:P\to A$, $q:P\to B$ such
that every such pair $(u,v)$ factors uniquely through $(p,q)$. That is exactly the pullback.

In each case, the limit cone is unique up to unique isomorphism by Theorem 8.2.1.

**22.** **Strategy.** Use the hom-set adjunction and the universal property of the product in
$\mathcal{D}$.

Let $A,B\in\mathcal{D}$. We show that $G(A\times B)$ satisfies the universal property of
$G(A)\times G(B)$ in $\mathcal{C}$. The candidate projections are
$$ G(\pi_A):G(A\times B)\to G(A),\qquad G(\pi_B):G(A\times B)\to G(B), $$
where $\pi_A:A\times B\to A$ and $\pi_B:A\times B\to B$ are the product projections.

Let $X\in\mathcal{C}$ and let $f:X\to G(A)$, $g:X\to G(B)$ be morphisms. Transpose them under the
adjunction to obtain $f^\#:F(X)\to A$ and $g^\#:F(X)\to B$. By the universal property of the product
$A\times B$, there is a unique $h:F(X)\to A\times B$ with
$$ \pi_A\circ h=f^\#,\qquad \pi_B\circ h=g^\#. $$
Transpose $h$ back to $k=h^\#:X\to G(A\times B)$. By naturality of the adjunction,
$$ G(\pi_A)\circ k=( \pi_A\circ h)^\#=(f^\#)^\#=f, $$
and similarly $G(\pi_B)\circ k=g$. Thus $k$ factors $(f,g)$ through the projections.

If $k'$ is another such morphism, then its transpose $k'^\#:F(X)\to A\times B$ satisfies
$\pi_A\circ k'^\#=f^\#$, $\pi_B\circ k'^\#=g^\#$, so $k'^\#=h$ by uniqueness in the product, and
hence $k'=k$. Therefore $G(A\times B)$ with $G(\pi_A),G(\pi_B)$ is a product of $G(A)$ and $G(B)$.
The isomorphism is natural in $A,B$ because the construction uses only the adjunction and the
universal property. This is a special case of Theorem 8.7.1.

**23.** **Functor.** For $f:X\to Y$, $\mathcal{P}(f)(S)=f[S]$. Then
$\mathcal{P}(\operatorname{id}_X)(S)=S$ and
$\mathcal{P}(g\circ f)(S)=(g\circ f)[S]=g[f[S]]=\mathcal{P}(g)(\mathcal{P}(f)(S))$. So
$\mathcal{P}$ is an endofunctor.

**Naturality of $\eta$.** For $x\in X$,
$$ \mathcal{P}(f)(\eta_X(x))=\mathcal{P}(f)(\{x\})=\{f(x)\}=\eta_Y(f(x)). $$

**Naturality of $\mu$.** Let $\mathfrak{A}\subseteq\mathcal{P}(X)$ and $f:X\to Y$. Then
$$ \mathcal{P}(f)(\mu_X(\mathfrak{A}))
=\mathcal{P}(f)\Big(\bigcup_{A\in\mathfrak{A}}A\Big)
=\bigcup_{A\in\mathfrak{A}}f[A]
=\bigcup_{B\in\mathcal{P}(f)(\mathfrak{A})}B
=\mu_Y(\mathcal{P}(\mathcal{P}(f))(\mathfrak{A})).
 $$

**Associativity.** Let $\mathfrak{A}\subseteq\mathcal{P}(\mathcal{P}(X))$. Both
$\mu_X(\mu_{\mathcal{P}(X)}(\mathfrak{A}))$ and
$\mu_X(\mathcal{P}(\mu_X)(\mathfrak{A}))$ are the union of all sets that occur at the bottom level of
$\mathfrak{A}$; unions are associative, so the two are equal.

**Unit laws.** For $S\subseteq X$,
$$ \mu_X(\mathcal{P}(\eta_X)(S))=\mu_X(\{\{x\}:x\in S\})=\bigcup_{x\in S}\{x\}=S, $$
and
$$ \mu_X(\eta_{\mathcal{P}(X)}(S))=\mu_X(\{S\})=S. $$
Hence $\mu\circ\mathcal{P}\eta=\operatorname{id}=\mu\circ\eta\mathcal{P}$. Therefore
$(\mathcal{P},\eta,\mu)$ is a monad.

**24.** **Monic versus epic in the opposite.** A morphism $f:A\to B$ in $\mathcal{C}$ is monic iff
for all $g,h:C\to A$,
$$ f\circ g=f\circ h\Longrightarrow g=h. $$
In $\mathcal{C}^{\mathrm{op}}$, the same $f$ is a morphism $f^{\mathrm{op}}:B\to A$. It is epic iff
for all $g^{\mathrm{op}},h^{\mathrm{op}}:A\to C$,
$$ g^{\mathrm{op}}\circ_{\mathrm{op}}f^{\mathrm{op}}
=h^{\mathrm{op}}\circ_{\mathrm{op}}f^{\mathrm{op}}\Longrightarrow g^{\mathrm{op}}=h^{\mathrm{op}}. $$
But $g^{\mathrm{op}}\circ_{\mathrm{op}}f^{\mathrm{op}}=f\circ g$ and
$h^{\mathrm{op}}\circ_{\mathrm{op}}f^{\mathrm{op}}=f\circ h$. So the epic condition is exactly the
monic condition. Hence $f$ is monic in $\mathcal{C}$ iff $f$ is epic in
$\mathcal{C}^{\mathrm{op}}$.

**Dual statements.**

| Notion | Dual |
|---|---|
| initial object | terminal object |
| product | coproduct |
| equalizer | coequalizer |
| pullback | pushout |
| monomorphism | epimorphism |
| left adjoint | right adjoint |

## Advanced

**25.** **Strategy.** Use the characterisations of monic and epic in each category.

**$\mathbf{Set}$ is balanced.** In $\mathbf{Set}$, monic means injective and epic means surjective, by
Proposition 7.2.4. A bimorphism is therefore a bijection. Every bijection has a two-sided inverse
function, so it is an isomorphism. Hence every bimorphism is an isomorphism.

**$\mathbf{Mon}$ is not balanced.** By Exercise 14, the inclusion
$i:\mathbb{Q}_{\ge0}\to\mathbb{Q}$ is monic and epic but not surjective. An isomorphism in
$\mathbf{Mon}$ is bijective (its inverse is a function), so $i$ is not an isomorphism. Hence
$\mathbf{Mon}$ has a bimorphism that is not an isomorphism.

**$\mathbf{Top}$ is not balanced.** Let $X$ be $\mathbb{R}$ with the discrete topology and $Y$ be
$\mathbb{R}$ with the usual topology. The identity function $f:X\to Y$ is a continuous bijection, so
it is monic and epic in $\mathbf{Top}$ by Proposition 7.2.8. But its inverse is not continuous, so
$f$ is not a homeomorphism. Hence $\mathbf{Top}$ has a bimorphism that is not an isomorphism.

**26.** **Statement.** Let $\mathcal{C}$ be a locally small category, $F:\mathcal{C}\to\mathbf{Set}$
a functor, and $A\in\mathcal{C}$. Then
$$ \Phi_{A,F}:\operatorname{Nat}(\mathcal{C}(A,-),F)\to F(A),\qquad
\Phi_{A,F}(\alpha)=\alpha_A(\operatorname{id}_A), $$
is a bijection. Its inverse sends $x\in F(A)$ to the natural transformation
$$ \alpha^{(x)}_B:\mathcal{C}(A,B)\to F(B),\qquad \alpha^{(x)}_B(f)=F(f)(x). $$

**Well-defined inverse.** For $g:B\to C$ and $f:A\to B$,
$$ F(g)(\alpha^{(x)}_B(f))
=F(g)(F(f)(x))
=F(g\circ f)(x)
=\alpha^{(x)}_C(g\circ f), $$
so $\alpha^{(x)}$ is natural. Also
$\alpha^{(x)}_A(\operatorname{id}_A)=F(\operatorname{id}_A)(x)=x$.

**Injectivity.** Let $\alpha:\mathcal{C}(A,-)\Rightarrow F$ be natural. For every $f:A\to B$, apply
naturality to $f$:
$$ \begin{array}{ccc}
\mathcal{C}(A,A) & \xrightarrow{\alpha_A} & F(A)\\
{\scriptstyle f\circ -}\downarrow & & \downarrow{\scriptstyle F(f)}\\
\mathcal{C}(A,B) & \xrightarrow{\alpha_B} & F(B).
\end{array} $$
Chasing $\operatorname{id}_A$ gives
$$ \alpha_B(f)=F(f)(\alpha_A(\operatorname{id}_A)). $$
Thus $\alpha$ is completely determined by $\alpha_A(\operatorname{id}_A)$. If
$\alpha_A(\operatorname{id}_A)=\beta_A(\operatorname{id}_A)$, then $\alpha_B(f)=\beta_B(f)$ for all
$B,f$, so $\alpha=\beta$.

**Surjectivity.** For $x\in F(A)$, $\alpha^{(x)}$ satisfies
$\alpha^{(x)}_A(\operatorname{id}_A)=x$, so $\Phi_{A,F}(\alpha^{(x)})=x$. Hence $\Phi$ is bijective.

**Naturality in $A$.** Let $h:A'\to A$. The square
$$ \begin{array}{ccc}
\operatorname{Nat}(\mathcal{C}(A,-),F) & \xrightarrow{\Phi_{A,F}} & F(A)\\
{\scriptstyle -\circ\mathcal{C}(h,-)}\downarrow & & \downarrow{\scriptstyle F(h)}\\
\operatorname{Nat}(\mathcal{C}(A',-),F) & \xrightarrow{\Phi_{A',F}} & F(A')
\end{array} $$
commutes: the left-bottom composite sends $\alpha$ to
$(\alpha\circ\mathcal{C}(h,-))_{A'}(\operatorname{id}_{A'})=\alpha_{A'}(h)$, while the top-right
composite sends it to $F(h)(\alpha_A(\operatorname{id}_A))=\alpha_{A'}(h)$ by naturality of
$\alpha$.

**Naturality in $F$.** For $\theta:F\Rightarrow G$, both composites in
$$ \begin{array}{ccc}
\operatorname{Nat}(\mathcal{C}(A,-),F) & \xrightarrow{\Phi_{A,F}} & F(A)\\
{\scriptstyle \theta\circ -}\downarrow & & \downarrow{\scriptstyle \theta_A}\\
\operatorname{Nat}(\mathcal{C}(A,-),G) & \xrightarrow{\Phi_{A,G}} & G(A)
\end{array} $$
send $\alpha$ to $\theta_A(\alpha_A(\operatorname{id}_A))$.

**Size.** Since $\mathcal{C}$ is locally small, each $\mathcal{C}(A,B)$ is a set and each $F(B)$ is
a set. A natural transformation $\alpha$ is determined by the single element
$\alpha_A(\operatorname{id}_A)\in F(A)$; hence the collection
$\operatorname{Nat}(\mathcal{C}(A,-),F)$ is in bijection with the set $F(A)$, and is therefore a
set. This is the sense in which the Yoneda lemma is a statement about sets.

**27.** **Statement.** Let $F:\mathcal{C}\to\mathcal{D}$ be left adjoint to
$G:\mathcal{D}\to\mathcal{C}$. Then $G$ preserves all limits that exist in $\mathcal{D}$, and $F$
preserves all colimits that exist in $\mathcal{C}$.

**Proof for limits.** Let $D:\mathcal{J}\to\mathcal{D}$ be a diagram with limit cone
$(L,(\pi_j))$ in $\mathcal{D}$. We prove that $(G(L),(G\pi_j))$ is a limit of $G\circ D$ in
$\mathcal{C}$.

Let $(X,(x_j))$ be a cone over $G\circ D$. Transpose each $x_j:X\to G(D(j))$ to
$x_j^\#:F(X)\to D(j)$. For every $f:j\to k$ in $\mathcal{J}$,
$$ D(f)\circ x_j^\#
=\varphi^{-1}\big(G(D(f))\circ x_j\big)
=\varphi^{-1}(x_k)
=x_k^\#, $$
where the first equality is naturality of $\varphi^{-1}$ in the second variable, the second is the
cone condition $G(D(f))\circ x_j=x_k$, and the third is the definition of the transpose. Hence
$(F(X),(x_j^\#))$ is a cone over $D$. By the universal property of $L$, there is a unique
$h:F(X)\to L$ with
$$ \pi_j\circ h=x_j^\#\qquad\text{for all }j. $$
Let $k=\varphi(h):X\to G(L)$. For each $j$,
$$ \varphi(G(\pi_j)\circ k)=\pi_j\circ h=x_j^\#, $$
and $\varphi(x_j)=x_j^\#$. Since $\varphi$ is injective, $G(\pi_j)\circ k=x_j$. Thus $k$ factors the
cone through $(G(L),(G\pi_j))$.

For uniqueness, suppose $k':X\to G(L)$ also satisfies $G(\pi_j)\circ k'=x_j$ for all $j$. Then
$\varphi(k'):F(X)\to L$ satisfies $\pi_j\circ\varphi(k')=x_j^\#$ for all $j$. By uniqueness of $h$,
$\varphi(k')=h$, so $k'=k$. Therefore $(G(L),(G\pi_j))$ is a limit cone, and $G$ preserves limits.

**Proof for colimits.** The dual argument, or apply the limit statement to
$F^{\mathrm{op}}\dashv G^{\mathrm{op}}$ in the opposite categories, shows that $F$ preserves
colimits. Explicitly, if $(L,(\iota_j))$ is a colimit of $D:\mathcal{J}\to\mathcal{C}$, then
$(F(L),(F\iota_j))$ is a colimit of $F\circ D$, because the universal property is the same with all
arrows reversed.

**28.** **The embedding.** Define
$$ y:\mathcal{C}\to[\mathcal{C}^{\mathrm{op}},\mathbf{Set}],\qquad
y(A)=\mathcal{C}(-,A). $$
On a morphism $f:A\to B$, define $y(f):\mathcal{C}(-,A)\Rightarrow\mathcal{C}(-,B)$ by
$$ y(f)_C:\mathcal{C}(C,A)\to\mathcal{C}(C,B),\qquad g\mapsto f\circ g. $$
For $h:D\to C$, the square
$$ \begin{array}{ccc}
\mathcal{C}(C,A) & \xrightarrow{f\circ -} & \mathcal{C}(C,B)\\
{\scriptstyle -\circ h}\downarrow & & \downarrow{\scriptstyle -\circ h}\\
\mathcal{C}(D,A) & \xrightarrow{f\circ -} & \mathcal{C}(D,B)
\end{array} $$
commutes because $(f\circ g)\circ h=f\circ(g\circ h)$. Thus $y(f)$ is natural. Functoriality is
$y(\operatorname{id}_A)_C(g)=\operatorname{id}_A\circ g=g$ and
$y(g\circ f)_C(h)=(g\circ f)\circ h=g\circ(f\circ h)$, so $y(g\circ f)=y(g)\circ y(f)$.

**Fullness.** Let $\alpha:\mathcal{C}(-,A)\Rightarrow\mathcal{C}(-,B)$ be natural. Set
$f=\alpha_A(\operatorname{id}_A):A\to B$. For $g:C\to A$, naturality of $\alpha$ applied to $g$
gives
$$ \alpha_C(g)=\alpha_C(\operatorname{id}_A\circ g)
=\alpha_A(\operatorname{id}_A)\circ g
=f\circ g, $$
using the square
$$ \begin{array}{ccc}
\mathcal{C}(A,A) & \xrightarrow{\alpha_A} & \mathcal{C}(A,B)\\
{\scriptstyle -\circ g}\downarrow & & \downarrow{\scriptstyle -\circ g}\\
\mathcal{C}(C,A) & \xrightarrow{\alpha_C} & \mathcal{C}(C,B).
\end{array} $$
Thus $\alpha=y(f)$. Hence $y$ is full.

**Faithfulness.** If $y(f)=y(g)$, evaluate at $A$ on $\operatorname{id}_A$:
$$ f=y(f)_A(\operatorname{id}_A)=y(g)_A(\operatorname{id}_A)=g. $$
Hence $y$ is faithful.

**Representables unique.** If $\mathcal{C}(-,A)\cong\mathcal{C}(-,B)$, fullness gives a morphism
$f:A\to B$ with $y(f)$ an isomorphism. Since $y$ is full and faithful, it reflects isomorphisms:
if $y(f)$ has inverse $y(g)$, then $y(g\circ f)=\operatorname{id}$ and $y(f\circ g)=\operatorname{id}$,
so $g\circ f=\operatorname{id}$ and $f\circ g=\operatorname{id}$ by faithfulness. Hence $f$ is an
isomorphism. If $f'$ is another, then $y(f)=y(f')$, so $f=f'$; the isomorphism is unique.

**29.** **Free group.** For a set $X$, let $F(X)$ be the set of reduced finite words in the alphabet
$X\sqcup X^{-1}$, where $X^{-1}=\{x^{-1}:x\in X\}$ and reducing means cancelling adjacent pairs
$x x^{-1}$ and $x^{-1}x$. Concatenation followed by reduction makes $F(X)$ a group, with the empty
word as identity and the reversed word with inverted letters as inverse. The inclusion
$\eta_X:X\to U(F(X))$, $x\mapsto[x]$, exhibits $X$ as a generating set.

**Universal property.** Let $G$ be a group and $f:X\to U(G)$ a function. Define
$\bar f:F(X)\to G$ on a reduced word $x_1^{\varepsilon_1}\cdots x_n^{\varepsilon_n}$ by
$$ \bar f(x_1^{\varepsilon_1}\cdots x_n^{\varepsilon_n})
=f(x_1)^{\varepsilon_1}\cdots f(x_n)^{\varepsilon_n}, $$
where $f(x)^{-1}$ means the inverse in $G$. This is a group homomorphism: concatenation becomes
multiplication, and the reduction relations are respected because $f(x)f(x)^{-1}=e=f(x)^{-1}f(x)$.
It extends $f$ because $\bar f([x])=f(x)$. If $\psi:F(X)\to G$ is any homomorphism with
$\psi([x])=f(x)$ for all $x$, then $\psi$ agrees with $\bar f$ on every generator and hence on every
word, so $\psi=\bar f$. Thus every function $X\to U(G)$ extends uniquely to a homomorphism
$F(X)\to G$.

**Adjunction.** The bijection is
$$ \Phi_{X,G}:\mathbf{Grp}(F(X),G)\to\mathbf{Set}(X,U(G)),\qquad
\Phi(\varphi)=\varphi\circ\eta_X, $$
with inverse $f\mapsto\bar f$. Naturality in $X$ and $G$ is immediate from the definitions: a
function $h:X'\to X$ composes with $\eta$, and a homomorphism $G\to G'$ composes with $\varphi$.

**Unit and counit.** The unit is $\eta_X:X\to U(F(X))$, $x\mapsto[x]$. The counit is
$$ \varepsilon_G:F(U(G))\to G, $$
the unique homomorphism extending $\operatorname{id}_{U(G)}:U(G)\to U(G)$; equivalently, it
evaluates a reduced word in elements of $G$ by multiplying them in $G$.

**Triangle identities.** The first is
$$ U(\varepsilon_G)\circ\eta_{U(G)}=\operatorname{id}_{U(G)}, $$
because for $g\in U(G)$, $\eta(g)=[g]$ and $\varepsilon_G([g])=g$. The second is
$$ \varepsilon_{F(X)}\circ F(\eta_X)=\operatorname{id}_{F(X)}, $$
because $F(\eta_X)$ sends a generator $x$ to the one-letter word $[x]$ in
$F(U(F(X)))$, and $\varepsilon_{F(X)}$ evaluates it to $x$; both sides are homomorphisms that agree
on the generators of the free group, hence they are equal.

**30.** **Set-up.** Let $T=G\circ F$, with unit $\eta:\operatorname{id}_{\mathcal{C}}\Rightarrow G F$
and multiplication $\mu=G\varepsilon F:G F G F\Rightarrow G F$.

**Unit laws.** Using the triangle identity $\varepsilon F\circ F\eta=\operatorname{id}_F$,
$$ \mu\circ T\eta
=(G\varepsilon F)\circ(G F\eta)
=G(\varepsilon F\circ F\eta)
=G(\operatorname{id}_F)
=\operatorname{id}_{G F}. $$
Using $G\varepsilon\circ\eta G=\operatorname{id}_G$ whiskered by $F$,
$$ \mu\circ\eta T
=(G\varepsilon F)\circ(\eta G F)
=(G\varepsilon\circ\eta G)F
=\operatorname{id}_G F
=\operatorname{id}_{G F}. $$

**Associativity.** Both composites
$$ \mu\circ T\mu=(G\varepsilon F)\circ(G F G\varepsilon F),\qquad
\mu\circ\mu T=(G\varepsilon F)\circ(G\varepsilon F G F) $$
are equal to $G(\varepsilon\circ F G\varepsilon)F$ and
$G(\varepsilon\circ\varepsilon F G)F$, respectively. These two natural transformations
$F G F G\Rightarrow F G$ agree by naturality of $\varepsilon$: for every object $X$,
$$ \varepsilon_{X}\circ F G\varepsilon_X
=\varepsilon_X\circ\varepsilon_{F G X}, $$
which is the naturality square of $\varepsilon$ at the morphism $\varepsilon_X$. Hence
$\mu\circ T\mu=\mu\circ\mu T$. Therefore $(T,\eta,\mu)$ is a monad.

**31.** **Set-up.** Consider a commutative diagram
$$ \begin{array}{ccccc}
A & \xrightarrow{f} & B & \xrightarrow{g} & C\\
{\scriptstyle h}\downarrow & & {\scriptstyle k}\downarrow & & {\scriptstyle l}\downarrow\\
A' & \xrightarrow{f'} & B' & \xrightarrow{g'} & C'
\end{array} $$
so $k\circ f=f'\circ h$ and $l\circ g=g'\circ k$; hence the outer rectangle commutes:
$l\circ g\circ f=g'\circ f'\circ h$.

**Part 1: right + outer pullback implies left pullback.** Assume the right square (vertices
$B,B',C,C'$) and the outer rectangle (vertices $A,A',C,C'$) are pullbacks. We prove that the left
square (vertices $A,A',B,B'$) is a pullback.

Let $X$ be an object with morphisms $r:X\to B$ and $p:X\to A'$ such that
$k\circ r=f'\circ p$. Put $q=g\circ r:X\to C$. Then
$$ g'\circ f'\circ p=g'\circ k\circ r=l\circ g\circ r=l\circ q, $$
so $(p,q)$ satisfies the outer pullback condition. The outer pullback gives a unique
$s:X\to A$ with
$$ g\circ f\circ s=q,\qquad h\circ s=p. $$
Now $f\circ s:X\to B$ satisfies
$$ g\circ(f\circ s)=q=g\circ r,\qquad
k\circ(f\circ s)=f'\circ h\circ s=f'\circ p=k\circ r. $$
The right pullback gives a unique morphism $X\to B$ with these two composites; both $f\circ s$ and
$r$ have them, so $f\circ s=r$. Hence $s$ satisfies $f\circ s=r$ and $h\circ s=p$.

If $s'$ also satisfies $f\circ s'=r$ and $h\circ s'=p$, then
$g\circ f\circ s'=g\circ r=q$ and $h\circ s'=p$, so $s'=s$ by uniqueness in the outer pullback.
Thus the left square is a pullback.

**Part 2: left + right pullback implies outer pullback.** Assume the left and right squares are
pullbacks. Let $X$ be an object with $p:X\to A'$ and $q:X\to C$ such that
$g'\circ f'\circ p=l\circ q$. The right pullback applied to the maps $f'\circ p:X\to B'$ and
$q:X\to C$ gives a unique $r:X\to B$ with
$$ g\circ r=q,\qquad k\circ r=f'\circ p. $$
The left pullback applied to $r:X\to B$ and $p:X\to A'$ gives a unique $s:X\to A$ with
$$ f\circ s=r,\qquad h\circ s=p. $$
Then $g\circ f\circ s=g\circ r=q$ and $h\circ s=p$, so $(p,q)$ factors through the outer square.

If $s'$ also satisfies $g\circ f\circ s'=q$ and $h\circ s'=p$, then $f\circ s'$ and $r$ both satisfy
$$ g\circ(f\circ s')=q,\qquad k\circ(f\circ s')=f'\circ h\circ s'=f'\circ p, $$
so $f\circ s'=r$ by uniqueness in the right pullback. Then $s'$ and $s$ both satisfy
$f\circ s'=r$ and $h\circ s'=p$, so $s'=s$ by uniqueness in the left pullback. Hence the outer
rectangle is a pullback.

**32.** **Set-up.** Let $\mathcal{J}$ be finite, with objects $j_1,\dots,j_n$ and morphisms
$u_1,\dots,u_m$. For each morphism $u:i\to j$, let $d(u)=i$ and $c(u)=j$. Form the products
$$ P=\prod_{j\in\operatorname{Ob}(\mathcal{J})}D(j),\qquad
Q=\prod_{u\in\operatorname{Mor}(\mathcal{J})}D(c(u)), $$
with projections $\pi_j:P\to D(j)$ and $\rho_u:Q\to D(c(u))$. Define morphisms $s,t:P\to Q$ by
their components
$$ s_u=\rho_u\circ s=\pi_{c(u)},\qquad
t_u=\rho_u\circ t=D(u)\circ\pi_{d(u)}. $$
Let $e:E\to P$ be the equalizer of $s$ and $t$.

**Cone.** For each object $j$, set $\lambda_j=\pi_j\circ e:E\to D(j)$. For a morphism $u:i\to j$,
$$ D(u)\circ\lambda_i
=D(u)\circ\pi_i\circ e
=t_u\circ e
=s_u\circ e
=\pi_j\circ e
=\lambda_j, $$
because $e$ equalizes $s$ and $t$. Thus $(E,(\lambda_j))$ is a cone over $D$.

**Universal property.** Let $(X,(x_j))$ be any cone over $D$. Define $h:X\to P$ by its components
$\pi_j\circ h=x_j$. For every morphism $u:i\to j$,
$$ s_u\circ h=\pi_j\circ h=x_j,\qquad
t_u\circ h=D(u)\circ\pi_i\circ h=D(u)\circ x_i=x_j, $$
using the cone condition. Hence $s\circ h=t\circ h$. By the universal property of the equalizer,
there is a unique $k:X\to E$ with $e\circ k=h$. Then
$$ \lambda_j\circ k=\pi_j\circ e\circ k=\pi_j\circ h=x_j $$
for every $j$.

For uniqueness, if $k'$ satisfies $\lambda_j\circ k'=x_j$ for all $j$, then
$e\circ k':X\to P$ has components $x_j$, hence $e\circ k'=h$. Since $e$ is the equalizer of $s,t$
and both $e\circ k$ and $e\circ k'$ equal $h$, uniqueness in the equalizer gives $k=k'$. Therefore
$(E,(\lambda_j))$ is a limit of $D$. Since $\mathcal{J}$ was arbitrary finite, $\mathcal{C}$ has all
finite limits.

**33.** **Monic.** The inclusion $i:\mathbb{Z}\to\mathbb{Q}$ is injective as a function. If
$i\circ u=i\circ v$ for ring homomorphisms $u,v:R\to\mathbb{Z}$, then $u(r)=v(r)$ for every $r$, so
$u=v$. Hence $i$ is monic.

**Epic.** Let $R$ be a ring and let $u,v:\mathbb{Q}\to R$ be unital ring homomorphisms with
$u\circ i=v\circ i$. Thus $u(n)=v(n)$ for every $n\in\mathbb{Z}$. In particular
$u(1)=v(1)=1_R$, and for $n\ge1$,
$$ u(n)=n\cdot1_R=v(n). $$
Also
$$ u(1/n)u(n)=u(1/n\cdot n)=u(1)=1_R, $$
so $u(1/n)$ is a multiplicative inverse of $u(n)$; similarly $v(1/n)$ is an inverse of
$v(n)=u(n)$. Inverses in a ring are unique: if $ab=1=ba$ and $ac=1=ca$, then
$b=b(ac)=(ba)c=c$. Hence $u(1/n)=v(1/n)$ for every $n\ge1$. For $m,n\in\mathbb{Z}$ with $n\ne0$,
$$ u(m/n)=u(m)u(1/n)=v(m)v(1/n)=v(m/n), $$
so $u=v$. Therefore $i$ is epic.

**Not an isomorphism.** It is not surjective, since $1/2\notin\mathbb{Z}$; an isomorphism of rings is
bijective. So $i$ is a bimorphism but not an isomorphism.

**Use of unitality.** The proof uses $u(1)=1_R$ and hence $u(n)=n\cdot1_R$; this is exactly
unitality. For non-unital ring homomorphisms the statement can fail, and the inclusion need not be
epic.

**34.** **Strategy.** Compare the two hom-set adjunctions and use the uniqueness of representing
objects.

For every $A\in\mathcal{C}$ and $B\in\mathcal{D}$,
$$ \mathcal{D}(F(A),B)\cong\mathcal{C}(A,G(B))\cong\mathcal{D}(F'(A),B), $$
and these bijections are natural in $B$ (and in $A$). Thus, for each fixed $A$, the functors
$\mathcal{D}(F(A),-)$ and $\mathcal{D}(F'(A),-)$ are naturally isomorphic. By the Yoneda lemma /
uniqueness of representing objects (Corollary 8.5.3), there is an isomorphism
$\alpha_A:F(A)\to F'(A)$, and it is unique. Naturality in $A$ follows from naturality of the
hom-set isomorphisms: for $f:A\to A'$, the square
$$ \begin{array}{ccc}
F(A) & \xrightarrow{\alpha_A} & F'(A)\\
{\scriptstyle F(f)}\downarrow & & \downarrow{\scriptstyle F'(f)}\\
F(A') & \xrightarrow{\alpha_{A'}} & F'(A')
\end{array} $$
commutes, because both composites represent the same natural transformation between hom functors.
Hence $\alpha:F\Rightarrow F'$ is a natural isomorphism.

**Uniqueness.** Any natural isomorphism $\beta:F\Rightarrow F'$ induces, by composition with
$\beta$, a natural isomorphism $\mathcal{D}(F'(A),B)\cong\mathcal{D}(F(A),B)$; together with the
adjunction isomorphisms it gives a natural automorphism of the representable functor
$\mathcal{D}(F(A),-)$. Representable functors have a unique representing-object isomorphism, so
$\beta_A=\alpha_A$ for every $A$. Thus the natural isomorphism is unique.

## Challenge

**35.** **Categorical Cayley theorem.** The Yoneda embedding
$y:\mathcal{C}\to[\mathcal{C}^{\mathrm{op}},\mathbf{Set}]$ is fully faithful (Exercise 28). A fully
faithful functor embeds its domain as a full subcategory of its codomain: it is injective on
hom-sets and reflects isomorphisms, so no information about morphisms is lost. Hence every small
category embeds fully faithfully into the category of presheaves on it.

**Monoid case.** Let $M$ be a monoid and $\mathbf{B}M$ its one-object category. The Yoneda embedding
sends the unique object $*$ to the presheaf $y(*)=\mathbf{B}M(-,*)$, whose underlying set is $M$ with
the right regular action $x\mapsto x\cdot m$. Since $y$ is fully faithful, $\mathbf{B}M$ embeds fully
faithfully into presheaves; in particular, endomorphisms of $y(*)$ correspond to morphisms
$*\to*$ in $\mathbf{B}M$, i.e. elements of $M$. Concretely, the map
$$ M\to\operatorname{End}_{\mathbf{Set}}(M,M),\qquad m\mapsto(x\mapsto m\cdot x) $$
is an injective monoid homomorphism: it preserves multiplication because
$L_m\circ L_n=L_{mn}$, and if $m\cdot x=n\cdot x$ for all $x$, taking $x=e$ gives $m=n$. Thus
$M$ embeds into the monoid of endofunctions of its underlying set. This is the classical Cayley
theorem for monoids.

**36.** **Category of elements.** Define $\int F$ as in the exercise. Its identity on $(C,x)$ is
$\operatorname{id}_C$; composition is composition in $\mathcal{C}$, and $F$ is a functor, so
composites are morphisms in $\int F$.

**Representable $\Rightarrow$ initial.** Suppose $\alpha:\mathcal{C}(A,-)\cong F$ is a natural
isomorphism. Let $x=\alpha_A(\operatorname{id}_A)\in F(A)$. For any object $(C,y)$ of $\int F$,
because $\alpha_C:\mathcal{C}(A,C)\to F(C)$ is bijective, there is a unique
$f:A\to C$ with $\alpha_C(f)=y$. By naturality,
$$ \alpha_C(f)=F(f)(\alpha_A(\operatorname{id}_A))=F(f)(x). $$
Thus there is a unique $f:A\to C$ with $F(f)(x)=y$, which is exactly the statement that
$(A,x)$ is initial in $\int F$.

**Initial $\Rightarrow$ representable.** Conversely, suppose $(A,x)$ is initial in $\int F$. For each
$C$, define
$$ \alpha_C:\mathcal{C}(A,C)\to F(C),\qquad \alpha_C(f)=F(f)(x). $$
The defining property of an initial object says that for every $y\in F(C)$ there is a unique
$f:A\to C$ with $F(f)(x)=y$. Hence $\alpha_C$ is a bijection. Naturality: for $h:C\to D$ and
$f:A\to C$,
$$ F(h)(\alpha_C(f))=F(h)(F(f)(x))=F(h\circ f)(x)=\alpha_D(h\circ f), $$
so $\alpha$ is a natural isomorphism $\mathcal{C}(A,-)\cong F$. Hence $F$ is representable.

**37.** **Right adjoints preserve monomorphisms.** Let $F\dashv G$ with
$F:\mathcal{C}\to\mathcal{D}$, $G:\mathcal{D}\to\mathcal{C}$. Let $f:A\to B$ be monic in
$\mathcal{D}$. To show $G(f):G(A)\to G(B)$ is monic in $\mathcal{C}$, let $g,h:X\to G(A)$ with
$G(f)\circ g=G(f)\circ h$. Transpose:
$$ f\circ g^\#=\varphi(G(f)\circ g)=\varphi(G(f)\circ h)=f\circ h^\#, $$
where $\varphi$ is the adjunction bijection. Since $f$ is monic, $g^\#=h^\#$, hence
$g=h$. Thus $G(f)$ is monic.

**Left adjoints preserve epimorphisms.** Let $f:A\to B$ be epic in $\mathcal{C}$. Let
$g,h:F(B)\to X$ with $g\circ F(f)=h\circ F(f)$. Transpose:
$$ g^\#\circ f=\varphi(g\circ F(f))=\varphi(h\circ F(f))=h^\#\circ f. $$
Since $f$ is epic, $g^\#=h^\#$, hence $g=h$. Thus $F(f)$ is epic.

**Counterexample.** The forgetful functor $U:\mathbf{Ring}\to\mathbf{Set}$ is right adjoint to the
free-ring functor (a left adjoint). By Exercise 33, $i:\mathbb{Z}\to\mathbb{Q}$ is an epimorphism in
$\mathbf{Ring}$. Its image under $U$ is the inclusion function $\mathbb{Z}\to\mathbb{Q}$, which is
injective and not surjective. In $\mathbf{Set}$, epimorphisms are surjections, so this function is
not an epimorphism. Hence a right adjoint need not preserve epimorphisms.

**38.** **The monad.** Let $F:\mathbf{Set}\to\mathbf{Mon}$ be the free monoid functor and
$U:\mathbf{Mon}\to\mathbf{Set}$ the forgetful functor. The adjunction $F\dashv U$ gives the monad
$T=U\circ F$, so $T(X)=X^*$. Its unit is $\eta_X(x)=[x]$, and its multiplication is
$\mu=U\varepsilon F$, where $\varepsilon_M:M^*\to M$ is the multiplication map
$[m_1,\dots,m_n]\mapsto m_1\cdots m_n$. At $X$, $\varepsilon_{F(X)}:(X^*)^*\to X^*$ is concatenation
of a list of lists. Hence the monad is exactly the list monad.

**Kleisli category.** Objects of $\mathbf{Set}_T$ are sets. A morphism $A\to B$ is a function
$f:A\to B^*$; the identity is $\eta_A$, and composition is
$$ (g\circ_T f)(a)=\mu_B(T(g)(f(a)))=\operatorname{concat}(\operatorname{map}(g,f(a))). $$

**Equivalence with free monoids.** Let $\mathbf{FreeMon}$ be the full subcategory of
$\mathbf{Mon}$ whose objects are the free monoids $X^*$. Define a functor
$K:\mathbf{Set}_T\to\mathbf{FreeMon}$ by

* on objects: $K(A)=A^*$;
* on a morphism $f:A\to B^*$: $K(f):A^*\to B^*$ is the unique monoid homomorphism extending
  $f:A\to B^*\subseteq B^*$; on a word,
  $K(f)([a_1,\dots,a_n])=f(a_1)\cdots f(a_n)$ (concatenation in $B^*$).

**Functoriality.** $K(\eta_A)$ is the monoid homomorphism extending $a\mapsto[a]$, which is the
identity on $A^*$. For composable $f:A\to B^*$, $g:B\to C^*$,
$$ K(g\circ_T f)([a])=(g\circ_T f)(a)
=\operatorname{concat}(\operatorname{map}(g,f(a)))
=K(g)(f(a))
=K(g)(K(f)([a])). $$
Both sides are monoid homomorphisms $A^*\to C^*$ that agree on the generators $[a]$, so they are
equal. Hence $K$ is a functor.

**Fully faithful.** A monoid homomorphism $\varphi:A^*\to B^*$ is determined by its restriction
$f:A\to B^*$, $f(a)=\varphi([a])$, and $K(f)=\varphi$. Hence the map
$\mathbf{Set}_T(A,B)\to\mathbf{FreeMon}(A^*,B^*)$ is bijective for all $A,B$. Thus $K$ is fully
faithful.

**Essentially surjective.** Every object of $\mathbf{FreeMon}$ is $A^*=K(A)$ for some set $A$.
Therefore $K$ is an equivalence of categories.

**39.** **Objects and morphisms.** The Kleisli category $\mathbf{Set}_{\mathcal{P}}$ has sets as
objects. A morphism $A\to B$ is a function $f:A\to\mathcal{P}(B)$, which is the same data as a
relation $R_f\subseteq A\times B$:
$$ a\,R_f\,b\iff b\in f(a). $$

**Identities.** The Kleisli identity is $\eta_A(a)=\{a\}$, corresponding to the equality relation
$\{(a,a):a\in A\}$.

**Composition.** For $f:A\to\mathcal{P}(B)$ and $g:B\to\mathcal{P}(C)$,
$$ (g\circ_T f)(a)=\mu_C(\mathcal{P}(g)(f(a)))=\bigcup_{b\in f(a)}g(b). $$
Under the relation dictionary, $c\in(g\circ_T f)(a)$ iff there is $b\in f(a)$ with $c\in g(b)$, i.e.
$$ a\,(R_g\circ R_f)\,c\iff\exists b\in B\ (a\,R_f\,b\text{ and }b\,R_g\,c). $$
This is exactly relational composition.

**Isomorphism.** The map $f\mapsto R_f$ is a bijection on each hom-set, preserves identities and
composition, and is the identity on objects. Hence it is an isomorphism of categories
$\mathbf{Set}_{\mathcal{P}}\cong\mathbf{Rel}$. (If one only asks for an equivalence, this is
certainly one.)

**40.** **Set-up.** Let $D:\mathcal{J}\to\mathcal{C}$ have a limit cone $(L,(\pi_j))$. We must show
that $y(L)$ with the natural transformations $y(\pi_j):y(L)\Rightarrow y(D(j))$ is a limit of
$y\circ D$ in $[\mathcal{C}^{\mathrm{op}},\mathbf{Set}]$.

**Pointwise limits.** Limits in a presheaf category are computed objectwise: a cone over $y\circ D$
is a limit cone iff for every object $X$ of $\mathcal{C}$ the induced cone of sets over
$X\mapsto y(D(j))(X)=\mathcal{C}(X,D(j))$ is a limit cone. This is the standard fact that limits in
functor categories are pointwise (dual to the colimit statement; it follows by applying the
universal property at each object $X$).

**Identify the pointwise limit.** For fixed $X$, the cone is
$$ \mathcal{C}(X,L)\xrightarrow{\;\mathcal{C}(X,\pi_j)\;}\mathcal{C}(X,D(j)). $$
The universal property of the limit $(L,(\pi_j))$ says exactly that for every cone
$(x_j:X\to D(j))$ there is a unique $h:X\to L$ with $\pi_j\circ h=x_j$. In other words, the map
$$ \mathcal{C}(X,L)\to\lim_j\mathcal{C}(X,D(j)),\qquad h\mapsto(\pi_j\circ h)_j, $$
is a bijection, and it is natural in $X$. Hence $y(L)(X)=\mathcal{C}(X,L)$ is the limit of the
functors $X\mapsto\mathcal{C}(X,D(j))$, and the maps $y(\pi_j)$ are the projections. Therefore
$y(L)$ is a limit of $y\circ D$.

**Reflection.** Since $y$ is fully faithful (Exercise 28), it reflects limits: if $y$ sends a cone
over $D$ to a limit cone over $y\circ D$, then the original cone is a limit cone. Indeed, given any
cone $(X,(x_j))$ over $D$, its image under $y$ is a cone over $y\circ D$, so it factors uniquely
through $y(L)$; by full faithfulness, this factorisation comes from a unique morphism $X\to L$ in
$\mathcal{C}$ factoring the original cone. Thus $y$ both preserves and reflects limits.

**Conclusion.** The Yoneda embedding preserves all limits that exist in $\mathcal{C}$ (and reflects
them). In particular, it preserves products, pullbacks, equalizers and terminal objects.
