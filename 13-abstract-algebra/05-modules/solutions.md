# Modules — Solutions

> [Tutorial](README.md) · [Exercises](exercises.md) · 36 worked solutions

Each solution states the strategy, carries out every step, names the theorem used with its hypotheses,
and ends with a check where an independent one exists.

## Beginner

**1.** *Strategy: the submodule test $x+ry\in N$ (Definition 5.4).*

(a) $2\mathbb{Z}$: for $x=2m$, $y=2n$ and $r\in\mathbb{Z}$, $x+ry=2(m+rn)\in2\mathbb{Z}$, and $2\mathbb{Z}\ne\varnothing$. A submodule.

(b) The odd integers: $1+1\cdot1=2$ is even, so the set is not closed under $x+ry$. It also lacks $0$. Not a submodule (not even a subgroup).

(c) $N=\{(a,b):a+b\ \text{even}\}$: for $(a,b),(c,d)\in N$ and $r\in\mathbb{Z}$,
$(a,b)+r(c,d)=(a+rc,\,b+rd)$ and $(a+rc)+(b+rd)=(a+b)+r(c+d)$ is even. Nonempty since $(0,0)\in N$. A submodule.

(d) $N=\{0,3,6,9\}\subseteq\mathbb{Z}/12$: every element is $3k$ with $k\in\mathbb{Z}$, so
$3k+r\cdot3l=3(k+rl)\in N$, and $N\ne\varnothing$. A submodule; indeed $N=3\mathbb{Z}/12\mathbb{Z}\cong\mathbb{Z}/4$.

*Check.* $9+9=18\equiv6\in N$ and $6+9=15\equiv3\in N$, consistent with closure.

**2.** *Strategy: compare the definitions.* An ideal is an additive subgroup closed under multiplication by every ring element, which is exactly the definition of a submodule of the regular module $R$. So the two notions coincide.

Submodules of $\mathbb{Z}/20$ correspond by Theorem 7.9 to the subgroups of the cyclic group of order $20$, hence to the divisors $d$ of $20$, the submodule being $d\mathbb{Z}/20\mathbb{Z}\cong\mathbb{Z}/(20/d)$:
$$0\ (\text{order }1),\quad\mathbb{Z}/2\ (d=10),\quad\mathbb{Z}/4\ (d=5),\quad\mathbb{Z}/5\ (d=4),\quad\mathbb{Z}/10\ (d=2),\quad\mathbb{Z}/20\ (d=1).$$
Inclusions follow divisibility of orders: $0\subset\mathbb{Z}/2\subset\mathbb{Z}/4\subset\mathbb{Z}/20$,
$0\subset\mathbb{Z}/2\subset\mathbb{Z}/10\subset\mathbb{Z}/20$, $0\subset\mathbb{Z}/5\subset\mathbb{Z}/10$,
$0\subset\mathbb{Z}/5\subset\mathbb{Z}/20$; the submodules $\mathbb{Z}/4$ and $\mathbb{Z}/10$ are
incomparable and meet in $\mathbb{Z}/2$.

**3.** *Strategy: a cyclic module is $R/\operatorname{Ann}$.* Every class in $\mathbb{Z}/n$ is $k\cdot\bar1$, so
$\mathbb{Z}/n=\mathbb{Z}\bar1$ and $\mathbb{Z}/n\cong\mathbb{Z}/\operatorname{Ann}(\bar1)$ with
$\operatorname{Ann}(\bar1)=n\mathbb{Z}$.

In $\mathbb{Z}/12$: $\operatorname{Ann}(\bar4)=\{r:12\mid4r\}=3\mathbb{Z}$;
$\operatorname{Ann}(\bar6)=\{r:12\mid6r\}=2\mathbb{Z}$; and
$\operatorname{Ann}(M)=\bigcap_{k}\operatorname{Ann}(\bar k)\subseteq\operatorname{Ann}(\bar1)=12\mathbb{Z}$,
so $\operatorname{Ann}(M)=12\mathbb{Z}$ (also $\operatorname{Ann}(\mathbb{Z}/12)=(12)$, as Proposition 7.17 gives with $d_k=12$).

**4.** *Strategy: use unique coordinates.* Let $F$ be free with basis $B$ and let $x=\sum_br_bb\ne0$ have
$rx=0$. Uniqueness of coordinates applied to $rx=\sum_b(rr_b)b=0$ gives $rr_b=0$ for every $b$; choosing
$b$ with $r_b\ne0$ and using that $R$ is a domain gives $r=0$. So $F$ is torsion-free.

In $\mathbb{Q}/\mathbb{Z}$ every element has finite order: $q=a/b$ gives $b\cdot(q+\mathbb{Z})=\mathbb{Z}$.
The group is nonzero and torsion, so it cannot be a nonzero free module, and it is not zero; hence it is
not free.

**5.** (a) Every polynomial is a finite sum $\sum a_ix^i$ with $a_i\in R$, and the coefficients are unique;
this is exactly the definition of a basis. (b) $(x)=\{xp(x)\}=\{r\cdot x: r\in R\}$, so $\{x\}$ is a basis
and $(x)\cong R$ as $R$-modules. (c) The evaluation map $R[x]\to R$, $p\mapsto p(0)$, is a surjective ring
map with kernel $(x)$, so $R[x]/(x)\cong R$ by the first isomorphism theorem.

**6.** In $\mathbb{Z}/2\oplus\mathbb{Z}/2$ every element satisfies $2x=0$, so no element has order $4$;
a cyclic group of order $4$ would have one, so the group is not cyclic. In $\mathbb{Z}/2\oplus\mathbb{Z}/3$
the element $(1,1)$ has order $\operatorname{lcm}(2,3)=6$, the order of the group, so
$(1,1)$ generates and $\mathbb{Z}/2\oplus\mathbb{Z}/3\cong\mathbb{Z}/6$.

**7.** The submodules of $\mathbb{Z}/6$ are $0$, $(2)=\{0,2,4\}\cong\mathbb{Z}/3$,
$(3)=\{0,3\}\cong\mathbb{Z}/2$, and $\mathbb{Z}/6$. The lattice is a diamond
$0\subset(2)\subset\mathbb{Z}/6$, $0\subset(3)\subset\mathbb{Z}/6$, with $(2)\cap(3)=0$ and
$(2)+(3)=\mathbb{Z}/6$ because $2-3=-1$ is a unit times a generator. Hence
$\mathbb{Z}/6=(2)\oplus(3)\cong\mathbb{Z}/3\oplus\mathbb{Z}/2$: all four submodules are direct summands
($0$ and $\mathbb{Z}/6$ trivially).

**8.** *Strategy: a $\mathbb{Z}$-linear map out of $\mathbb{Z}$ is free, one into $\mathbb{Z}$ is constrained.*
$\operatorname{Hom}_{\mathbb{Z}}(\mathbb{Z},\mathbb{Z}/n)\cong\mathbb{Z}/n$ via $f\mapsto f(1)$, and any
$a\in\mathbb{Z}/n$ occurs ($f(k)=ka$).
$\operatorname{Hom}_{\mathbb{Z}}(\mathbb{Z}/n,\mathbb{Z})=0$: if $f(\bar1)=m$ then
$0=f(n\bar1)=nm$, so $m=0$. Equivalently, the image of a finite-order element has finite order and
$\mathbb{Z}$ has none.

**9.** *Strategy: check well-definedness first.* If $\bar k=\bar k'$ in $\mathbb{Z}/4$, then $k-k'=4t$ and
$f(\bar k)-f(\bar k')=2(k-k')=8t\equiv0$ in $\mathbb{Z}/8$, so $f$ is well defined. Now
$\ker f=\{\bar k:2k\equiv0\pmod 8\}=\{\bar k:4\mid k\}=\{0\}$, and
$\operatorname{im}f=\{0,2,4,6\}=2\mathbb{Z}/8\mathbb{Z}\cong\mathbb{Z}/4$. The first isomorphism theorem
reads $\mathbb{Z}/4\big/\{0\}\cong\operatorname{im}f$, true. The map is injective and not surjective: an
injective module homomorphism between finite modules need not be an isomorphism, which is impossible for
finite-dimensional vector spaces of the same dimension.

**10.** Linearity: $f(m+n)=2(m+n)=f(m)+f(n)$ and $f(rm)=2rm=r(2m)=rf(m)$. Injectivity: $2n=0$ gives $n=0$.
Image $2\mathbb{Z}$, so $\operatorname{coker}f=\mathbb{Z}/2\mathbb{Z}=\mathbb{Z}/2$. The failing theorem is
"an injective linear endomorphism of a finite-dimensional space is an isomorphism": over $\mathbb{Z}$ an
injective endomorphism of the free module of rank $1$ need not be onto, because $2$ is not invertible.

**11.** $M_{\mathrm{tor}}=\{(0,\bar0),(0,\bar1)\}\cong\mathbb{Z}/2$: an element $(a,\bar b)$ is killed by
$r\ne0$ iff $ra=0$ in $\mathbb{Z}$ iff $a=0$. $\operatorname{Ann}(M)=\operatorname{Ann}(\mathbb{Z})\cap\operatorname{Ann}(\mathbb{Z}/2)=0\cap2\mathbb{Z}=0$.
Finally $M/M_{\mathrm{tor}}\cong\mathbb{Z}\oplus0\cong\mathbb{Z}$, the torsion summand having died, exactly
as Proposition 7.16 predicts for the quotient by the torsion submodule.

**12.** (a) Not free: $\mathbb{Z}/6$ is torsion and a nonzero free group is torsion-free (Exercise 4).
(b) Free of rank $1$: $\mathbb{Z}/6=R\cdot\bar1$ with annihilator $0$ in $R=\mathbb{Z}/6$ (only
$r=0$ kills $\bar1$).
(c) $\mathbb{Z}$ carries no $\mathbb{Z}/6$-module structure at all: an $R$-module satisfies $6m=0$ for
every $m$, but $6\cdot1=6\ne0$. Hence it is not free — the question does not even arise.
(d) Not free: Failure 1 (divisibility).
(e) Free of rank $1$ with basis $\{1\}$.

## Intermediate

**13.** *Strategy: the number is $\prod p(a_i)$.* Since $200=2^3\cdot5^2$ and $p(3)=3$, $p(2)=2$, there
are $6$ groups. The $2$-part is $\mathbb{Z}/8$, $\mathbb{Z}/4\oplus\mathbb{Z}/2$ or
$\mathbb{Z}/2\oplus\mathbb{Z}/2\oplus\mathbb{Z}/2$; the $5$-part is $\mathbb{Z}/25$ or
$\mathbb{Z}/5\oplus\mathbb{Z}/5$. The six elementary-divisor forms are
$$\mathbb{Z}/8\oplus\mathbb{Z}/25,\quad \mathbb{Z}/8\oplus\mathbb{Z}/5\oplus\mathbb{Z}/5,\quad
\mathbb{Z}/4\oplus\mathbb{Z}/2\oplus\mathbb{Z}/25,\quad \mathbb{Z}/4\oplus\mathbb{Z}/2\oplus\mathbb{Z}/5\oplus\mathbb{Z}/5,\quad
\mathbb{Z}/2^3\oplus\mathbb{Z}/25,\quad \mathbb{Z}/2^3\oplus\mathbb{Z}/5^2 .$$
In invariant-factor form they are $\mathbb{Z}/200$; $\mathbb{Z}/40\oplus\mathbb{Z}/5$;
$\mathbb{Z}/100\oplus\mathbb{Z}/2$; $\mathbb{Z}/20\oplus\mathbb{Z}/10$;
$\mathbb{Z}/50\oplus\mathbb{Z}/2\oplus\mathbb{Z}/2$; $\mathbb{Z}/10\oplus\mathbb{Z}/10\oplus\mathbb{Z}/2$.
*Check.* Each product of invariant factors is $200$.

**14.** (a) $10^6=2^6\cdot5^6$ and $p(6)=11$, so there are $11^2=121$ abelian groups of order $10^6$.
(b) $4$ and $9$ are coprime, so the Chinese remainder theorem gives
$\mathbb{Z}/4\oplus\mathbb{Z}/9\cong\mathbb{Z}/36$. For the second pair, $\mathbb{Z}/2\oplus\mathbb{Z}/18$
has invariant factors $2\mid18$ and contains an element of order $18$; $\mathbb{Z}/6\oplus\mathbb{Z}/6$
has invariant factors $6\mid6$ and exponent $6$. Distinct invariant factors mean non-isomorphic groups
(Theorem 7.25).

**15.** *Strategy: determinantal divisors.* Here $\Delta_1=1$ (the matrix has an entry $1$),
$\Delta_2=1$ (the minor $2\cdot0-1\cdot1=-1$ occurs), and $\Delta_3=|\det A|=|-5|=5$. Hence
$d_1=1$, $d_2=1$, $d_3=5$, and $\mathbb{Z}^3/A\mathbb{Z}^3\cong\mathbb{Z}/5$, a cyclic group of order
$5$, even though the presentation has three generators and three relations.
*Check.* The order of the cokernel is $|\det A|=5$ once the Smith normal form is diagonal with one
nonunit, consistent with $d_1d_2d_3=5$.

**16.** *Strategy: Smith normal form of a diagonal matrix.* The module is the cokernel of
$\operatorname{diag}(a,b)$. Its determinantal divisors are $\Delta_1=\gcd(a,b)=:g$ and
$\Delta_2=ab$, so $d_1=g$ and $d_2=ab/g=\operatorname{lcm}(a,b)=:l$, and
$\mathbb{Z}/a\oplus\mathbb{Z}/b\cong\mathbb{Z}/g\oplus\mathbb{Z}/l$. This is the module form of the
identity $ab=g\,l$.

**17.** (a) $\mathbb{Z}/\gcd(8,12)=\mathbb{Z}/4$. (b) $\mathbb{Z}/\gcd(6,4)=\mathbb{Z}/2$.
(c) $0$, since $\mathbb{Q}$ is divisible and $2$ is invertible on it. (d) $\mathbb{Z}/5$.
*Check.* The order of $\mathbb{Z}/m\otimes\mathbb{Z}/n$ is $\gcd(m,n)$, as Example 7.43(a) states.

**18.** $\mathbb{Q}/\mathbb{Z}$ is divisible, so for every $x$ and every $n$ there is $y$ with $ny=x$;
hence $n(\mathbb{Q}/\mathbb{Z})=\mathbb{Q}/\mathbb{Z}$ and
$(\mathbb{Q}/\mathbb{Z})\otimes\mathbb{Z}/n\cong(\mathbb{Q}/\mathbb{Z})/n(\mathbb{Q}/\mathbb{Z})=0$
by Proposition 7.40(d). Tensoring with $\mathbb{Q}/\mathbb{Z}$ therefore annihilates every finite cyclic
group.

**19.** For ideals $I,J$ of a commutative ring, $A/I\otimes_AA/J\cong A/(I+J)$; here
$I+J=(x^2-1,x-1)=(x-1)$, so the tensor product is $\mathbb{R}[x]/(x-1)\cong\mathbb{R}$. Next,
$\mathbb{C}\otimes_{\mathbb{R}}\mathbb{R}[x]\cong\mathbb{C}[x]$, because extension of scalars along
$\mathbb{R}\to\mathbb{C}$ is base change of the polynomial ring and commutes with the free construction.

**20.** *Strategy: exhibit a bilinear map and its inverse.* The map
$B:\mathbb{Z}[x]\times\mathbb{Z}[y]\to\mathbb{Z}[x,y]$, $B(p,q)=p(x)q(y)$, is bilinear, so it induces
$\Phi:\mathbb{Z}[x]\otimes\mathbb{Z}[y]\to\mathbb{Z}[x,y]$ with $\Phi(p\otimes q)=p(x)q(y)$, which is
surjective since the monomials $x^iy^j$ are hit. Define
$\Psi:\mathbb{Z}[x,y]\to\mathbb{Z}[x]\otimes\mathbb{Z}[y]$ on the basis by
$x^iy^j\mapsto x^i\otimes y^j$ and extend $\mathbb{Z}$-linearly. Then
$\Phi\Psi(x^iy^j)=x^iy^j$ and $\Psi\Phi(x^i\otimes y^j)=x^i\otimes y^j$; both sides are linear and agree
on generators, so $\Psi=\Phi^{-1}$.

**21.** (a) **Splits.** The map $s(b)=(0,b)$ is linear and $(a,b)\mapsto b$ sends $(0,b)\mapsto b$, so
$g\circ s=\mathrm{id}$; the sequence is the standard split sequence $0\to A\to A\oplus C\to C\to0$ with
$A=C=\mathbb{Z}$.
(b) **Does not split.** If it did, Theorem 7.34 would give $\mathbb{Z}/4\cong\mathbb{Z}/2\oplus\mathbb{Z}/2$,
but the left side has an element of order $4$ and the right side does not.
(c) **Splits.** $\mathbb{Z}/6\cong(3)\oplus(2)\cong\mathbb{Z}/2\oplus\mathbb{Z}/3$ by the Chinese
remainder theorem, and the given maps are the structural inclusion and projection.

**22.** Suppose $j:\mathbb{Z}\to\mathbb{Z}/n$ is the projection and $\mathrm{id}:\mathbb{Z}/n\to\mathbb{Z}/n$.
A lift $\tilde f:\mathbb{Z}/n\to\mathbb{Z}$ would satisfy $j\circ\tilde f=\mathrm{id}$, in particular
$\tilde f(\bar1)$ would have to be a preimage of $\bar1$; but $\tilde f$ is a group homomorphism from a
torsion group to a torsion-free group, hence zero (Exercise 8). Contradiction. So $\mathbb{Z}/n$ is not
projective for $n\ge2$; note that $\mathbb{Z}/n$ *is* free, hence projective, over the ring $\mathbb{Z}/n$.

**23.** A map $\mathbb{Z}/6\to\mathbb{Z}/10$ is determined by $a=f(\bar1)$ with $6a\equiv0\pmod{10}$,
i.e. $5\mid3a$, i.e. $5\mid a$: the solutions are $\bar a\in\{0,5\}$, so
$|\operatorname{Hom}(\mathbb{Z}/6,\mathbb{Z}/10)|=2=\gcd(6,10)$.
A map $\mathbb{Z}/12\to\mathbb{Z}/18$ needs $18\mid12a$, i.e. $3\mid2a$, i.e. $3\mid a$: the solutions are
$\bar a\in\{0,3,6,9,12,15\}$, six maps, and $\gcd(12,18)=6$. In both cases the Hom group is cyclic, the
map $f\mapsto f(\bar1)$ identifying it with the subgroup of elements killed by $m$.

## Advanced

**24.** *Second theorem.* Let $S,T\subseteq M$ be submodules. The map $\varphi:S\to(S+T)/T$,
$s\mapsto s+T$, is $R$-linear and onto. Its kernel is $\{s\in S:s\in T\}=S\cap T$. By the first
isomorphism theorem (Proposition 7.7), $S/(S\cap T)\cong(S+T)/T$. Both sides are modules over $R$, and
$S\cap T$ and $T$ are indeed submodules, so the statement is legitimate.

*Third theorem.* Let $N\subseteq L\subseteq M$ be submodules. The map
$\psi:M/N\to M/L$, $m+N\mapsto m+L$, is well defined (since $N\subseteq L$), linear and onto, with kernel
$L/N$. Hence $(M/N)/(L/N)\cong M/L$.

**25.** *Strategy: use a section to lift, a retraction to extend.* Let $p:M\to N$ be onto and
$f:P\to N$ linear. The sequence $0\to\ker p\to M\to N\to0$ splits by hypothesis, so there is
$s:N\to M$ with $p\circ s=\mathrm{id}_N$; then $\tilde f=s\circ f$ satisfies
$p\circ\tilde f=f$, so $P$ is projective.

Now let $i:A\to B$ be injective and $f:A\to I$ linear. The sequence
$0\to A\to B\to B/i(A)\to0$ splits, so there is $r:B\to A$ with $r\circ i=\mathrm{id}_A$; then
$\tilde f=f\circ r$ satisfies $\tilde f\circ i=f$, so $I$ is injective. Hence every module is projective
and injective.

**26.** *Strategy: identify the two statements.* For any $P$, the functor $\operatorname{Hom}_R(P,-)$ is
left exact: given $0\to A\xrightarrow{i}B\xrightarrow{p}C$, the sequence
$0\to\operatorname{Hom}(P,A)\to\operatorname{Hom}(P,B)\to\operatorname{Hom}(P,C)$ is exact, because a map
$P\to A$ that dies in $\operatorname{Hom}(P,C)$ lands in $\ker p=\operatorname{im}i$, and injectivity of
$i$ makes the induced map on Hom's injective. Exactness at $\operatorname{Hom}(P,C)$ means that every
$f:P\to C$ is $p\circ g$ for some $g:P\to B$, which is precisely the lifting property defining
projectivity. Hence the functor is exact iff $P$ is projective.

**27.** If $P$ is finitely generated and projective, choose generators $x_1,\dots,x_n$ and the surjection
$\pi:R^n\to P$, $e_i\mapsto x_i$. By Theorem 7.47(iii) the surjection splits, so $R^n\cong P\oplus\ker\pi$
and $P$ is a direct summand of the finitely generated free module $R^n$. Conversely, a direct summand of
$R^n$ is projective by Theorem 7.47(iv), and it is finitely generated as a quotient of $R^n$.

**28.** *Strategy: Nakayama twice.* Let $k=R/\mathfrak m$ and $n=\dim_k(M/\mathfrak mM)$.

*Lower bound.* If $x_1,\dots,x_d$ generate $M$, their images span $M/\mathfrak mM$, so $d\ge n$: no
generating set has fewer than $n$ elements.

*Existence.* Choose $x_1,\dots,x_n\in M$ whose images form a basis of $M/\mathfrak mM$. Their images span,
so by Corollary 7.58(b) they generate $M$.

*Minimality.* Suppose $y_1,\dots,y_m$ generate $M$ with $m<n$. Their images span $M/\mathfrak mM$, a
vector space of dimension $n$, so $m\ge n$ by linear algebra — a contradiction. Hence $n$ is the minimum,
and every minimal generating set has $n$ elements: a generating set with more than $n$ elements is not
minimal because the $n$ elements above already generate.

**29.** *Strategy: localise at all nonzero scalars.* Let $K=\operatorname{Frac}R$ and use that
$R/(d)\otimes_RK=K/dK=0$ for $d\ne0$.

If $M$ is torsion, Theorem 7.21 gives $M\cong\bigoplus_iR/(d_i)$, hence
$M\otimes_RK\cong\bigoplus_iK/d_iK=0$.
Conversely, if $M\otimes_RK=0$, apply $-\otimes_RK$ to $0\to M_{\mathrm{tor}}\to M\to M/M_{\mathrm{tor}}\to0$:
since $K$ is flat (a localisation, hence a filtered colimit of free modules), the sequence stays exact, so
$(M/M_{\mathrm{tor}})\otimes_RK=0$. But $M/M_{\mathrm{tor}}\cong R^r$ by Corollary 7.23, so this is $K^r$,
which is zero only if $r=0$. Hence $M=M_{\mathrm{tor}}$.

**30.** (a) If $\mathbb{Z}$ were injective, the map $f:\mathbb{Z}\to\mathbb{Z}$ with $f(n)=n$ would extend
along the injection $\mathbb{Z}\xrightarrow{\times2}\mathbb{Z}$ to $h:\mathbb{Z}\to\mathbb{Z}$ with
$h(2n)=n$. Taking $n=1$ gives $2h(1)=1$, impossible in $\mathbb{Z}$. So $\mathbb{Z}$ is not injective.
(Equivalently the sequence $0\to\mathbb{Z}\xrightarrow{2}\mathbb{Z}\to\mathbb{Z}/2\to0$ would have to
split, which it does not.)
(b) For $x=q+\mathbb{Z}$ and $n\ge1$, the element $y=\frac qn+\mathbb{Z}$ satisfies $ny=x$; so
$\mathbb{Q}/\mathbb{Z}$ is divisible. By Proposition 7.54 a $\mathbb{Z}$-module is injective iff it is
divisible, so $\mathbb{Q}/\mathbb{Z}$ is injective.

**31.** *Strategy: lift a basis.* Let $C$ be free with basis $\{c_i\}_{i\in I}$ and let the sequence be
$0\to A\to M\xrightarrow{g}C\to0$. For each $i$ choose $m_i\in M$ with $g(m_i)=c_i$; this is possible
because $g$ is onto. By Theorem 7.11 the assignment $c_i\mapsto m_i$ extends uniquely to a linear map
$s:C\to M$, and $g\circ s=\mathrm{id}_C$ because the two sides agree on the basis. By Theorem 7.34 the
sequence splits and $M\cong A\oplus C$. The hypothesis that $C$ is free is used exactly at the step
"extend from the basis"; for a general $C$ the lifting may fail, as
$0\to\mathbb{Z}\xrightarrow{2}\mathbb{Z}\to\mathbb{Z}/2\to0$ shows.

## Challenge

**32.** *Strategy: minimal generators plus Nakayama.* Let $k=R/\mathfrak m$ and $n=\dim_k(P/\mathfrak mP)$.
Choose $x_1,\dots,x_n\in P$ whose images are a basis; they generate $P$ by Nakayama. Let
$\varphi:R^n\to P$ be the corresponding surjection. Since $P$ is projective, $\varphi$ splits
(Theorem 7.47(iii)), so $R^n\cong P\oplus Q$ for some finitely generated $Q$. Tensoring with $k$ and using
right exactness,
$$k^n\cong P/\mathfrak mP\oplus Q/\mathfrak mQ,$$
so $\dim_k(Q/\mathfrak mQ)=n-n=0$, i.e. $Q=\mathfrak mQ$. By Nakayama's lemma (Theorem 7.57) applied to
the finitely generated module $Q$, this forces $Q=0$. Hence $\varphi$ is an isomorphism and $P\cong R^n$
is free. (The hypothesis of finite generation cannot be dropped, and the conclusion fails over
non-local rings, as Example 7.51 shows.)

**33.** *Strategy: a presentation whose kernel is visibly free, then localise.* Write $R=k[x,y]$ and
$I=(x,y)$. The map $\pi:R^2\to I$, $\pi(a,b)=ax+by$, is onto, and
$$\ker\pi=\{(a,b):ax=-by\}.$$
Since $k[x,y]$ is a UFD and $\gcd(x,y)=1$, the relation $ax=-by$ forces $x\mid b$ and $y\mid a$: write
$b=xc$, then $ax=-xyc$ gives $a=-yc$. So $\ker\pi=R\cdot(-y,x)\cong R$, and
$$0\longrightarrow R\xrightarrow{\ c\mapsto(-yc,\,xc)\ }R^2\xrightarrow{\ \pi\ }I\longrightarrow0$$
is exact.

Suppose $I$ were projective. Then $\pi$ splits, so $R^2\cong R\oplus I$. Localise at the maximal ideal
$\mathfrak m=(x,y)$: $R_{\mathfrak m}^2\cong R_{\mathfrak m}\oplus I_{\mathfrak m}$, so $I_{\mathfrak m}$ is
a finitely generated projective module over the local ring $R_{\mathfrak m}$, hence free by Exercise 32.
Its rank is $1$ (an ideal in a domain has rank $1$: any two elements $f,g$ satisfy $gf-fg=0$), so
$I_{\mathfrak m}\cong R_{\mathfrak m}$ and $I_{\mathfrak m}$ needs one generator. On the other hand
$I_{\mathfrak m}/\mathfrak mI_{\mathfrak m}=\mathfrak m/\mathfrak m^2$ has $k$-basis the classes of $x$
and $y$, so by Nakayama it needs two generators. Contradiction. Hence $(x,y)$ is not projective.

*Remark.* The second part uses only Nakayama and the rank of an ideal, not the deep theorem that
finitely generated projectives over $k[x,y]$ are free.

**34.** (⇒) If $R$ is a field, every module is a vector space, and every vector space has a basis
(Zorn's lemma, or the standard basis-extension argument); so every module is free.

(⇐) Suppose every $R$-module is free and $R$ is not a field. Then there is a nonzero element $a$ that is
not a unit: if every nonzero element were a unit, $R$ would be a field. The principal ideal $I=(a)$ is
proper and nonzero, and $R/I\ne0$. By hypothesis $R/I$ is free, so it has a basis $(e_j)$. Pick a basis
element $e=e_{j_0}\ne0$; its annihilator is zero, since $\sum r_je_j=0$ with $r_{j_0}\ne0$ would violate
uniqueness of coordinates. But $a\cdot e=0$ in $R/I$ with $a\ne0$. Contradiction. Hence $R$ is a field.

**35.** Suppose $\mathbb{Q}$ were projective. Over the PID $\mathbb{Z}$ every projective module is free
(Theorem 7.49), so $\mathbb{Q}$ would be free, contradicting Failure 1: a nonzero free abelian group is
not divisible, while $\mathbb{Q}$ is divisible. Hence $\mathbb{Q}$ is not projective.

*Second approach.* If $\mathbb{Q}$ were projective, it would be a direct summand of a free module
$F=\mathbb{Z}^{(I)}$, say $F=\mathbb{Q}\oplus N$. Choose a nonzero $q\in\mathbb{Q}$ and write
$q=(x)+(y)$ with $x\in\mathbb{Z}^{(I)}$, $y\in N$. Choose a prime $p$ and write $q=pq'$; splitting
$q'=x'+y'$, multiplying by $p$ and comparing coordinates in the direct sum gives $x=px'$, so every
coordinate of $x$ is divisible by every prime, hence $x=0$; then $q=y\in N$, so $\mathbb{Q}\subseteq N$
and $\mathbb{Q}\cap N=\mathbb{Q}\ne0$, contradiction.

**36.** *Strategy: recover the invariants from the quotients.* Write
$G\cong\mathbb{Z}^r\oplus T_G$ and $H\cong\mathbb{Z}^s\oplus T_H$ with $T_G,T_H$ finite
(Theorem 7.25). Since tensoring with $\mathbb{Z}/n$ is right exact and $\mathbb{Z}/n$ is finitely
presented, $G/nG\cong(\mathbb{Z}/n)^r\oplus T_G/nT_G$, so
$$|G/nG|=n^r\cdot|T_G/nT_G|,\qquad |T_G/nT_G|\le|T_G| .$$
Hence $r=\lim_{n\to\infty}\bigl(\log|G/nG|/\log n\bigr)$, because the second factor is bounded; the same
formula for $H$ shows that $G/nG\cong H/nH$ for all $n$ forces $r=s$.

Now fix a prime $p$, let $T_p$ be the $p$-primary part of $T_G$, and put
$|T_p|=\prod_ip^{a_i}$ with $a_1\ge a_2\ge\cdots$ (the partition of the exponent). From the displayed
isomorphism, $T_p/p^kT_p\cong(G/p^kG)/(\mathbb{Z}/p^k)^r$, and
$$|T_p/p^kT_p|=p^{\sum_i\min(a_i,k)} .$$
The right side is determined by the given groups $G/p^kG$, so the numbers $\sum_i\min(a_i,k)$ are known
for all $k$; subtracting consecutive values recovers the number of $a_i\ge k$, hence the partition
$(a_i)$, hence $T_p$ up to isomorphism (Theorem 7.22). Doing this for every prime determines $T_G$, and
with $r=s$ we get $G\cong H$. The converse is immediate since an isomorphism preserves $G/nG$.
