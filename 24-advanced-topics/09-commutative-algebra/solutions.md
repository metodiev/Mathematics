# Commutative Algebra — Solutions

> [Commutative Algebra](README.md) · Solutions to the 36 problems in [exercises.md](exercises.md)

Each solution states the strategy first, then carries out every step and names the theorem used. Numbers in
parentheses such as (§7.2) refer to the section of the [tutorial](README.md) where the relevant result is proved.
Where a second route exists it is mentioned; likely pitfalls are flagged where they occur.

## Beginner

**1.** *Strategy: check the defining properties of an ideal — additive subgroup, and closure under multiplication
by arbitrary ring elements.*

(a) Let $\{\mathfrak{a}_i\}_{i\in I}$ be ideals and $\mathfrak{a}=\bigcap_i\mathfrak{a}_i$. It is an additive
subgroup because each $\mathfrak{a}_i$ is one and the intersection of subgroups is a subgroup. If $a\in\mathfrak{a}$
and $r\in A$ then $ra\in\mathfrak{a}_i$ for every $i$, so $ra\in\mathfrak{a}$. Hence $\mathfrak{a}$ is an ideal.

(b) For ideals $\mathfrak{a},\mathfrak{b}$, the sum $\mathfrak{a}+\mathfrak{b}=\{a+b\}$ is an additive subgroup
(sum of subgroups), and for $r\in A$, $r(a+b)=ra+rb\in\mathfrak{a}+\mathfrak{b}$. So it is an ideal. It is the
smallest ideal containing both, since any ideal containing $\mathfrak{a}$ and $\mathfrak{b}$ contains all sums.

(c) In $k[x,y]$ take $I=(x)$ and $J=(y)$. Then $x\in I\cup J$ and $y\in I\cup J$, but $x+y\notin I\cup J$: if
$x+y\in(x)$ then $y=x(f-1)\in(x)$, which is false because $k[x,y]/(x)\cong k[y]$ is a domain and $y\ne0$ there;
similarly $x+y\notin(y)$. So $I\cup J$ is not closed under addition. The smallest ideal containing $I\cup J$ is
$I+J=(x,y)$. $\blacksquare$

**2.** *Strategy: compute the quotient to prove maximality, then use degree considerations to rule out a single
generator.*

The third isomorphism theorem gives
$$
\mathbb{Z}[x]/(2,x)\cong\big(\mathbb{Z}[x]/(2)\big)\big/\big((2,x)/(2)\big)\cong\mathbb{F}_{2}[x]/(x)\cong\mathbb{F}_{2},
$$
because $\mathbb{Z}[x]/(2)\cong\mathbb{F}_{2}[x]$ and the image of $x$ in that ring generates $(x)$. A quotient by
$\mathfrak{a}$ is a field exactly when $\mathfrak{a}$ is maximal (Proposition 7.1), so $(2,x)$ is maximal.

*Not principal.* Suppose $(2,x)=(f)$. Then $f\mid2$, so $f$ is a constant or has degree $0$ times… more precisely,
$2=fg$ forces $\deg f=0$ or $\deg g=0$; and $x=fh$ forces $\deg f\le1$. If $\deg f=1$, then $f$ cannot divide the
non-zero constant $2$ in $\mathbb{Z}[x]$ (a degree-one polynomial times anything has degree at least one). So $f$
is a constant, hence $f=\pm1$ or $f=\pm2$. The first gives $(f)=\mathbb{Z}[x]$, the second gives $(f)=(2)$, which
does not contain $x$. So no single $f$ generates $(2,x)$.

$\mathbb{Z}[x]$ is Noetherian by the Hilbert basis theorem (Theorem 7.17), applied to the Noetherian ring
$\mathbb{Z}$. It is not a PID because $(2,x)$ is not principal. $\blacksquare$

*Remark.* A noetherian ring can have ideals requiring several generators; what noetherianity forbids is an ideal
requiring *infinitely* many.

**3.** *Strategy: translate primeness and maximality into properties of the quotient, using the bijection between
ideals of $A/\mathfrak{a}$ and ideals of $A$ containing $\mathfrak{a}$.*

If $\mathfrak{a}$ is prime and $\bar a\bar b=0$ in $A/\mathfrak{a}$, then $ab\in\mathfrak{a}$, so $a\in\mathfrak{a}$
or $b\in\mathfrak{a}$, i.e. $\bar a=0$ or $\bar b=0$: the quotient is a domain. Conversely, if the quotient is a
domain, then $ab\in\mathfrak{a}$ means $\bar a\bar b=0$, so $\bar a=0$ or $\bar b=0$, i.e. $a\in\mathfrak{a}$ or
$b\in\mathfrak{a}$. Also $\mathfrak{a}\ne A$ corresponds to the quotient being non-zero.

For maximality, ideals of $A/\mathfrak{a}$ correspond to ideals $\mathfrak{b}$ with $\mathfrak{a}\subseteq\mathfrak{b}\subseteq A$.
So $\mathfrak{a}$ is maximal (no proper intermediate ideal) iff $A/\mathfrak{a}$ has no proper non-zero ideal, iff
every non-zero element of $A/\mathfrak{a}$ generates the unit ideal, iff it is a field.

(a) In $\mathbb{Z}$, $(0)$ is prime because $\mathbb{Z}$ is a domain, and not maximal because
$(0)\subsetneq(2)\subsetneq\mathbb{Z}$.

(b) In $k[x,y]$, $(x)$ is prime because $k[x,y]/(x)\cong k[y]$ is a domain, and not maximal because
$(x)\subsetneq(x,y)\subsetneq k[x,y]$. $\blacksquare$

**4.** *Strategy: primes of a quotient correspond to primes of $\mathbb{Z}$ containing $6$.*

An ideal $\mathfrak{p}$ of $\mathbb{Z}/6\mathbb{Z}$ is prime iff it is of the form $P/(6)$ with $P$ a prime of
$\mathbb{Z}$ containing $6$. The primes containing $6=2\cdot3$ are $(2)$ and $(3)$, so
$$
\operatorname{Spec}(\mathbb{Z}/6\mathbb{Z})=\{(2),(3)\}.
$$
The closed sets are $V(0)=\{(2),(3)\}$, $V(2)=\{(2)\}$, $V(3)=\{(3)\}$ and $V(1)=\varnothing$: all subsets are
closed. Both points are closed (their complements are open), so the space is discrete.

A finite discrete space is Hausdorff, so in this example the answer is *yes*. The contrast with
$\operatorname{Spec}\mathbb{Z}$ is the point: there the generic point $(0)$ is dense and the space is not
Hausdorff. $\blacksquare$

**5.** *Strategy: use the definition of equality in the localisation.*

By Definition 5.7, $1/1=0/1$ in $S^{-1}A$ iff there is $t\in S$ with $t(1\cdot1-0\cdot1)=0$, i.e. $t=0$. So
$S^{-1}A=0$ iff $0\in S$. (If $0\in S$ then taking $t=0$ makes every fraction equal to zero.)

*Example.* $A=\mathbb{Z}$ and $S=\{0,1\}$: this is multiplicative ($1\cdot1=1$, and any product involving $0$ is
$0\in S$), and $\mathbb{Z}_S=0$. Note that $\{0\}$ alone is not multiplicative, since it does not contain $1$; this
is why the definition of multiplicative set insists on $1\in S$. $\blacksquare$

**6.** *Strategy: rewrite the localisation explicitly in a domain, where fractions are compared by cross
multiplication.*

Since $\mathbb{Z}$ is a domain, $a/s=a'/s'$ in $\mathbb{Z}_{(p)}$ iff $as'=a's$ as rational numbers. So
$$
\mathbb{Z}_{(p)}=\left\{\frac ab\in\mathbb{Q}: p\nmid b\right\}.
$$
It contains $\mathbb{Z}$ and is contained in $\mathbb{Q}$. The ideal
$$
\mathfrak{m}=\left\{\frac ab:p\mid a,\ p\nmid b\right\}=p\mathbb{Z}_{(p)}
$$
is proper, and every element outside it has $p\nmid a$, hence is a unit with inverse $b/a\in\mathbb{Z}_{(p)}$. So
every proper ideal is contained in $\mathfrak{m}$: the ring is local with maximal ideal $\mathfrak{m}$.

The residue field is $\mathbb{Z}_{(p)}/p\mathbb{Z}_{(p)}\cong\mathbb{F}_{p}$, by the map $a/b\mapsto ab^{-1}\bmod p$
(well defined because $b\not\equiv0$).

The units are exactly the fractions with $p\nmid a$, i.e. $\mathbb{Z}_{(p)}^{\times}=\mathbb{Z}_{(p)}\setminus\mathfrak{m}$,
in agreement with Problem 7. $\blacksquare$

**7.** *Strategy: an element generates a proper ideal exactly when it lies in some maximal ideal; in a local ring
there is only one.*

If $a\notin\mathfrak{m}$ then $(a)\not\subseteq\mathfrak{m}$; since $\mathfrak{m}$ is the unique maximal ideal and
every proper ideal is contained in a maximal ideal, $(a)$ cannot be proper, so $(a)=A$ and $a$ is a unit.
Conversely a unit lies in no proper ideal, so it is not in $\mathfrak{m}$. Hence
$A^{\times}=A\setminus\mathfrak{m}$.

Since $\mathfrak{m}$ is an ideal, the sum of two elements of $\mathfrak{m}$ lies in $\mathfrak{m}$, i.e. the sum of
two non-units is a non-unit. $\blacksquare$

*Pitfall.* The last statement fails in non-local rings: in $\mathbb{Z}$, $3$ and $-2$ are non-units but their sum
$1$ is a unit. So the property is genuinely a local-ring phenomenon, and it is equivalent to the complement of the
non-units being closed under addition, which is exactly the statement that the set of non-units is an ideal.

**8.** *Strategy: define the map and count elements.*

Define $\varphi:\mathbb{Z}/6\mathbb{Z}\to\mathbb{Z}/2\mathbb{Z}\times\mathbb{Z}/3\mathbb{Z}$ by
$\varphi(\bar n)=(\bar n,\bar n)$. It is well defined (if $n\equiv m\bmod6$ then $n\equiv m$ modulo $2$ and $3$), and
it is a ring homomorphism. Its kernel is $\{n:2\mid n\ \text{and}\ 3\mid n\}=\{n:6\mid n\}=0$ in $\mathbb{Z}/6\mathbb{Z}$.
Both source and target have $6$ elements, so an injective map between them is bijective.

For a product of rings, ideals of $A\times B$ are exactly of the form $I\times J$ with $I\subseteq A$,
$J\subseteq B$ ideals: the projection maps are ring homomorphisms. And
$$
(A\times B)/(I\times J)\cong A/I\times B/J
$$
is a domain iff one factor is the zero ring and the other is a domain. So the primes of $A\times B$ are
$\mathfrak{p}\times B$ and $A\times\mathfrak{q}$ for primes $\mathfrak{p}\subseteq A$, $\mathfrak{q}\subseteq B$;
in other words
$$
\operatorname{Spec}(A\times B)\cong\operatorname{Spec}A\ \sqcup\ \operatorname{Spec}B
$$
as topological spaces (a disjoint union of clopen pieces). For $\mathbb{Z}/6\mathbb{Z}$ this recovers the two points
$(2)$ and $(3)$ of Problem 4. $\blacksquare$

**9.** *Strategy: classify the ideals of a product of two fields directly.*

An ideal $I\subseteq k_1\times k_2$ is determined by its behaviour on the two idempotents $e_1=(1,0)$, $e_2=(0,1)$.
Since $e_1e_2=0$ and $e_1+e_2=1$, one checks that $I$ is one of
$$
0,\qquad k_1\times0,\qquad 0\times k_2,\qquad k_1\times k_2 .
$$
Indeed if $(a,b)\in I$ with $a\ne0$ then $e_1=(a^{-1},0)(a,b)\in I$; similarly for $b\ne0$.

The prime ideals are $k_1\times0$ and $0\times k_2$: their quotients are $k_2$ and $k_1$, both fields. The zero
ideal is not prime, since $(1,0)(0,1)=0$. Both primes are maximal, so $\dim A=0$.

The closed sets are $\varnothing$, $\{k_1\times0\}$, $\{0\times k_2\}$ and the whole space: the topology is
discrete on two points. $\blacksquare$

**10.** *Strategy: apply Proposition 7.1 with $\mathfrak{a}=(0)$.*

Since $A/(0)\cong A$, the statements are immediate: $(0)$ is prime iff $A$ is a domain; $(0)$ is maximal iff $A$ is
a field.

Examples: in $\mathbb{Z}$, $(0)$ is prime but not maximal. In $\mathbb{Z}/6\mathbb{Z}$, $(0)$ is neither: the ring
has zero divisors, and the ideal is properly contained in $(2)$. $\blacksquare$

## Intermediate

**11.** *Strategy: check the three clauses of Theorem 7.4 in the concrete case.*

The reduction map $\varphi:\mathbb{Z}\to\mathbb{F}_p$ sends $S=\mathbb{Z}\setminus(p)$ into
$\mathbb{F}_p^{\times}$: if $p\nmid n$ then $n$ is invertible mod $p$. So $\varphi$ inverts $S$, and Theorem 7.4
supplies a unique $\psi:\mathbb{Z}_{(p)}\to\mathbb{F}_p$ with $\psi(a/1)=\varphi(a)$.

Concretely $\psi(a/b)=\varphi(a)\varphi(b)^{-1}=(a\bmod p)(b\bmod p)^{-1}$, the reduction of the fraction. It is
well defined: if $a/b=a'/b'$ in $\mathbb{Z}_{(p)}$ then $ab'=a'b$ as integers, so $ab'\equiv a'b\pmod p$, and since
$b,b'$ are invertible mod $p$ we get $ab^{-1}\equiv a'b'^{-1}\pmod p$.

*Uniqueness.* Any $\psi'$ with $\psi'\iota=\varphi$ must satisfy $\psi'(a/1)=\varphi(a)$ and, since $\psi'$ is a
ring homomorphism, $\psi'(1/b)=\varphi(b)^{-1}$; therefore $\psi'(a/b)=\varphi(a)\varphi(b)^{-1}=\psi(a/b)$. So
$\psi'=\psi$. $\blacksquare$

**12.** *Strategy: apply the exact functor $S^{-1}$ to the defining exact sequence of the quotient, then use the
first isomorphism theorem.*

The sequence
$$
0\longrightarrow I\longrightarrow A\longrightarrow A/I\longrightarrow0
$$
is exact. By Theorem 7.7 the localised sequence
$$
0\longrightarrow S^{-1}I\longrightarrow S^{-1}A\longrightarrow S^{-1}(A/I)\longrightarrow0
$$
is exact, so $S^{-1}(A/I)\cong S^{-1}A/S^{-1}I$ by the first isomorphism theorem. The only hypothesis is that $S$
is multiplicative; exactness holds for every such $S$ and every ring. The place where $S$ is used is the proof of
exactness *at the middle*, where one needs $t\in S$ to pass from "$f(m')/s=0$" to "$tf(m')=0$". $\blacksquare$

**13.** *Strategy: prove the three exactness conditions separately, using the definition of equality in a
localised module.*

**Injectivity.** If $f_S(m'/s)=0$ in $S^{-1}M$, then $f(m')/s=0$, so by definition of the localisation there is
$t\in S$ with $t\,f(m')=0$. Then $f(tm')=0$, and $f$ is injective, so $tm'=0$ in $M'$, whence $m'/s=0$ in
$S^{-1}M'$. (This is the only place where $S$ enters.)

**Kernel equals image.** $g_Sf_S=0$ because $gf=0$. Conversely, if $g_S(m/s)=0$, then $g(m)/s=0$, so there is
$t\in S$ with $t\,g(m)=0$, i.e. $g(tm)=0$. Hence $tm\in\ker g=\operatorname{im}f$, say $tm=f(m')$. Then
$$
\frac ms=\frac{tm}{ts}=\frac{f(m')}{ts}=f_S\!\left(\frac{m'}{ts}\right).
$$

**Surjectivity.** For $m''/s\in S^{-1}M''$, write $m''=g(m)$ and observe $m''/s=g_S(m/s)$. $\blacksquare$

**14.** *Strategy: for the non-trivial direction, choose a non-zero element and a maximal ideal containing its
annihilator.*

If $M=0$ then all localisations vanish. Conversely suppose $M\ne0$ and pick $0\ne m\in M$. Then
$\operatorname{Ann}(m)=\{a:am=0\}$ is a proper ideal (it does not contain $1$), so it is contained in a maximal
ideal $\mathfrak{m}$ (Proposition 7.2). In $M_{\mathfrak{m}}$, the element $m/1$ is non-zero: if $m/1=0$ there is
$s\notin\mathfrak{m}$ with $sm=0$, so $s\in\operatorname{Ann}(m)\subseteq\mathfrak{m}$, contradiction. Hence
$M_{\mathfrak{m}}\ne0$, and in particular $M_{\mathfrak{p}}\ne0$ for the prime $\mathfrak{p}=\mathfrak{m}$.

*The single-prime statement fails.* Take $A=\mathbb{Z}$, $M=\mathbb{Z}/2\mathbb{Z}$ and $\mathfrak{p}=(3)$. Then
$M_{\mathfrak{p}}=0$, because $2$ is a unit in $\mathbb{Z}_{(3)}$ and hence acts invertibly on $M_{(3)}$: indeed
$\bar1/1=\bar1/1\cdot(2\cdot2^{-1})=0$ since $2\bar1=0$. But $M\ne0$. So vanishing at one prime says nothing.
$\blacksquare$

**15.** *Strategy: follow the structure of the proof of Theorem 7.17, verifying each claim.*

Let $I\subseteq A[x]$. Define $L\subseteq A$ as the set of leading coefficients of elements of $I$, together with
$0$.

*$L$ is an ideal.* If $a,b\in L$ arise from $f,g\in I$ of degrees $m\le n$, then $x^{n-m}f+g$ has degree $\le n$ and
leading coefficient $a+b$ when $a+b\ne0$ (and is $0$ otherwise), so $a+b\in L$. If $r\in A$ then $rf\in I$ has
leading coefficient $ra$. So $L$ is closed under addition and under multiplication by $A$.

Since $A$ is Noetherian, $L=(a_1,\dots,a_n)$. Choose $f_i\in I$ with leading coefficient $a_i$ and degree $d_i$,
let $d=\max d_i$, and let $M=I\cap(A+Ax+\dots+Ax^{d-1})$. This $M$ is an $A$-submodule of the finitely generated
free module $A^{d}$, hence is finitely generated (Proposition 7.16(iii)); say $M=(g_1,\dots,g_m)_A$.

*The claim.* $I=M+(f_1,\dots,f_n)$. The inclusion $\supseteq$ is clear. For $\subseteq$, let $f\in I$ have degree
$e$ and leading coefficient $a$. If $e<d$ then $f\in M$. If $e\ge d$, write $a=\sum r_ia_i$ and put
$g=f-\sum r_ix^{e-d_i}f_i$. The degree-$e$ terms cancel, so $\deg g<e$, and $g\in I$. By induction on $e$ we get
$g\in M+(f_1,\dots,f_n)$, hence so is $f$. So $I$ is finitely generated and $A[x]$ is Noetherian. $\blacksquare$

**16.** *Strategy: invoke Nakayama's lemma and then apply the general criterion for generation.*

That $M=\mathfrak{m}M$ implies $M=0$ is Theorem 7.20 with $I=\mathfrak{m}\subseteq\operatorname{Jac}(A)$ (a local
ring has a unique maximal ideal, so $\operatorname{Jac}(A)=\mathfrak{m}$).

For the generation criterion: if $m_1,\dots,m_r$ have images spanning $M/\mathfrak{m}M$, then
$M=(m_1,\dots,m_r)+\mathfrak{m}M$; applying Corollary 7.21(i) with $N=(m_1,\dots,m_r)$ gives $M=(m_1,\dots,m_r)$.
Conversely a generating set surjects onto $M/\mathfrak{m}M$, so it spans. In particular
$\dim_kM/\mathfrak{m}M$ is the minimal number of generators. $\blacksquare$

**17.** *Strategy: identify the primes as those containing $xy$, then use the dimension formula for quotients.*

$A=k[x,y]/(xy)$ is not a domain, because the images of $x$ and $y$ are non-zero and multiply to zero.

*Primes.* Primes of $A$ correspond to primes $\mathfrak{p}$ of $k[x,y]$ containing $(xy)$, i.e. containing $x$ or
containing $y$ (since $(xy)\subseteq\mathfrak{p}$ and $\mathfrak{p}$ is prime). The minimal such primes are $(x)$
and $(y)$; the others are the maximal ideals $(x,y)$, $(x,y-b)$ with $b\ne0$, and $(x-a,y)$ with $a\ne0$.

*Dimension.* $A/(x)\cong k[y]$, of dimension $1$, and $A/(y)\cong k[x]$, of dimension $1$. Since every prime
contains a minimal prime, and the chains have length at most $1$ above a minimal prime, $\dim A=1$; explicitly
$(x)\subsetneq(x,y)$ is a chain of length $1$.

*Localisations at the minimal primes.* Localising at $(x)$ inverts $y$ (which is not in $(x)$), so $xy=0$ forces
$x=0$ in the localisation; hence $A_{(x)}\cong k[y,y^{-1}]$ localised at the zero ideal, i.e. the fraction field
$k(y)$. Similarly $A_{(y)}\cong k(x)$. These are fields: the local ring at the generic point of an irreducible
component is the function field of that component. $\blacksquare$

*Pitfall.* The local ring at a *minimal* prime always has dimension $0$; the interesting local rings of this
example sit at the maximal ideals, where the two lines meet.

**18.** *Strategy: (a) a field cannot be integral over a proper subring that is not a field (Fact 7.27b); (b) over a
field, integrality implies algebraicity, and an algebraic element has an inverse that is a polynomial in it.*

(a) This is Fact 7.27b.

(b) Let $A$ be a field and $B$ an integral domain, integral over $A$. Take $0\ne b\in B$. By integrality, $b$
satisfies a monic equation $b^{n}+a_{n-1}b^{n-1}+\cdots+a_0=0$ with $a_i\in A$. Since $B$ is a domain and $b\ne0$,
we may take $n$ minimal; then $a_0\ne0$ (otherwise $b(b^{n-1}+\cdots+a_1)=0$ and the bracket vanishes, contradicting
minimality). Rearranging,
$$
b\left(b^{n-1}+a_{n-1}b^{n-2}+\cdots+a_1\right)=-a_0\in A^{\times},
$$
so $b$ has the inverse $-(b^{n-1}+\cdots+a_1)a_0^{-1}\in B$. Hence every non-zero element of $B$ is a unit.

*The domain hypothesis is needed.* Let $A=\mathbb{Q}$ and $B=\mathbb{Q}\times\mathbb{Q}$. Every element $(a,b)\in B$
is integral over $\mathbb{Q}$: it satisfies $X^{2}-(a+b)X+ab=0$, a monic polynomial with coefficients in
$\mathbb{Q}$ (embedded diagonally). But $B$ is not a field, since $(1,0)(0,1)=0$. $\blacksquare$

**19.** *Strategy: use the structure of ideals in a DVR (Proposition 7.42), then compare with $\mathbb{Z}$.*

If $(A,\mathfrak{m})$ is a DVR with $\mathfrak{m}=(\pi)$, then every non-zero ideal is $(\pi^{n})$ by Proposition
7.42, so every ideal is principal and $A$ is a PID. The primes are $(0)$ and $(\pi)$, which is unique among the
non-zero primes.

$\mathbb{Z}$ is a PID (every ideal is $(n)$ with $n\ge0$), but it is not local: $(2)$ and $(3)$ are distinct maximal
ideals. Equivalently, it has infinitely many non-zero prime ideals, whereas a DVR has exactly one. So $\mathbb{Z}$
is a PID that is not a DVR, and "DVR" is strictly stronger than "PID". $\blacksquare$

**20.** *Strategy: prove the three defining properties of a Dedekind domain and see which one fails.*

$A=k[x,y]/(y^{2}-x^{3})$.

*Domain.* If $y^{2}-x^{3}$ factored in $k[x,y]$, then viewing it as a quadratic in $y$ we would have
$(y+a)(y+b)$ with $a,b\in k[x]$, $a+b=0$, $ab=-x^{3}$, i.e. $-a^{2}=-x^{3}$, so $a^{2}=x^{3}$, impossible in the
UFD $k[x]$ (the exponent of $x$ on the left is even and on the right is $3$).

*Dimension.* In the fraction field, $y^{2}=x^{3}$, so $(y/x)^{2}=x$: setting $t=y/x$ gives $x=t^{2}$, $y=t^{3}$, and
$\operatorname{Frac}A=k(t)$. Hence $\operatorname{trdeg}_k\operatorname{Frac}A=1$ and $\dim A=1$ by Theorem 7.37.

*Not integrally closed.* $t=y/x$ lies in $\operatorname{Frac}A$ and satisfies $t^{2}=x\in A$, so it is integral over
$A$. But $t\notin A$: as a subring of $k[t]$, $A$ is $k[t^{2},t^{3}]$, whose elements are the polynomials
$\sum c_nt^{n}$ with $n=0$ or $n\ge2$ (since $2$ and $3$ generate all integers $\ge2$), and $t$ has degree $1$.

So $A$ is Noetherian and one-dimensional but not integrally closed, hence not a Dedekind domain. Its integral
closure is $k[t]$. $\blacksquare$

## Advanced

**21.** *Strategy: (a) repeat the Hilbert basis argument; (b) use induction and quotients; (c) exhibit an explicit
strictly increasing chain of ideals in the subring.*

(a) Let $A$ be Noetherian and $I\subseteq A[x]$. The set $L$ of leading coefficients of elements of $I$ (together
with $0$) is an ideal: if $a,b\in L$ come from $f,g$ of degrees $m\le n$, then $x^{n-m}f+g\in I$ has leading
coefficient $a+b$, and $rf$ has leading coefficient $ra$. Write $L=(a_1,\dots,a_n)$, choose $f_i\in I$ with
leading coefficient $a_i$, let $d=\max\deg f_i$ and $M=I\cap(A+\dots+Ax^{d-1})$, which is finitely generated as an
$A$-submodule of $A^{d}$. Then $I=M+(f_1,\dots,f_n)$: given $f\in I$ of degree $e\ge d$ with leading coefficient
$a=\sum r_ia_i$, the element $f-\sum r_ix^{e-d_i}f_i\in I$ has degree $<e$, and induction on $e$ finishes. So $A[x]$
is Noetherian.

(b) By induction, $A[x_1,\dots,x_n]$ is Noetherian; a finitely generated $A$-algebra is a quotient of such a ring,
and quotients of Noetherian rings are Noetherian by Proposition 7.16(i).

(c) Let $R=k[x,xy,xy^{2},\dots]\subseteq k[x,y]$. Its elements are the polynomials whose monomials are $x^{a}y^{b}$
with $a\ge1$, together with the constants: indeed a product of generators is $x^{a}\prod_i(xy^{j_i})=x^{a+m}y^{\sum j_i}$
with $m$ factors, which is divisible by $x$ when $m\ge1$, and the remaining monomials are the powers $x^{a}$; so
$$
R=k+x\,k[x,y].
$$
Consider
$$
I_n=(xy,xy^{2},\dots,xy^{n})\subseteq R .
$$
The chain $I_1\subsetneq I_2\subsetneq\cdots$ is strictly increasing. For if $xy^{n+1}\in I_n$, then
$xy^{n+1}=\sum_{k=1}^{n}f_kxy^{k}$ with $f_k\in R$; dividing by $x$ in the domain $k[x,y]$ gives
$y^{n+1}=\sum_k f_ky^{k}$. Write $f_k=c_k+xg_k$ with $c_k\in k$ and $g_k\in k[x,y]$ (possible since $R=k+xk[x,y]$)
and reduce modulo $(x)$: this gives $y^{n+1}=\sum_{k=1}^{n}c_ky^{k}$ in $k[y]$, impossible because the two sides
have different degrees. Hence $R$ is not Noetherian.

This does not contradict (b), because (b) is a statement about quotients and polynomial extensions of $A$, and
noetherianity is *not* inherited by subrings. $\blacksquare$

**22.** *Strategy: prove the unit criterion first, then run the minimal-generating-set argument.*

(i)$\Rightarrow$(ii): If $1-xy$ were not a unit, it would be a proper ideal, hence contained in a maximal ideal
$\mathfrak{m}$. Then $xy\in\mathfrak{m}$; since $y\notin\mathfrak{m}$ (otherwise $1\in\mathfrak{m}$) and
$\mathfrak{m}$ is prime, $x\in\mathfrak{m}$, so $x\notin\operatorname{Jac}(A)$ — contradiction. (This direction
needs only that $\operatorname{Jac}(A)$ is an intersection of primes and that maximal ideals are prime.)

(ii)$\Rightarrow$(i): If $x\notin\operatorname{Jac}(A)$, there is a maximal ideal $\mathfrak{m}$ with $x\notin\mathfrak{m}$.
Then $\mathfrak{m}+(x)=A$, so $m+xy=1$ for some $m\in\mathfrak{m}$, $y\in A$; thus $1-xy=m$ is a non-unit.

*Nakayama.* Let $I\subseteq\operatorname{Jac}(A)$ and $M\ne0$ finitely generated with $IM=M$. Choose a generating
set $m_1,\dots,m_n$ of minimal size. Since $m_n\in IM$,
$$
m_n=\sum_{i=1}^{n}a_im_i,\qquad a_i\in I,
$$
so $(1-a_n)m_n=\sum_{i<n}a_im_i$. As $a_n\in I\subseteq\operatorname{Jac}(A)$, the element $1-a_n$ is a unit by the
criterion; hence $m_n\in(m_1,\dots,m_{n-1})$, contradicting minimality. Therefore $M=0$.

*Fibre form.* For $(A,\mathfrak{m})$ local and $M$ finitely generated with $M/\mathfrak{m}M=0$, we get
$M=\mathfrak{m}M$, so $M=0$. $\blacksquare$

**23.** *Strategy: factor an integer and use the comaximality of the prime-power ideals.*

Let $A$ be a PID and $(a)\subsetneq A$ a non-zero proper ideal. Factor
$$
a=u\,p_1^{e_1}\cdots p_r^{e_r}
$$
with $u$ a unit, $p_i$ pairwise non-associate primes and $e_i\ge1$. We claim
$$
(a)=(p_1^{e_1})\cap\cdots\cap(p_r^{e_r}).
$$
The inclusion $\subseteq$ is clear. Conversely, if $x$ is divisible by each $p_i^{e_i}$, then for each $i$,
$v_{p_i}(x)\ge e_i$, and since the $p_i$ are distinct primes, $v_{p_i}(a)=e_i$; so $a\mid x$. (Here $v_p$ is the
exponent of $p$ in the factorisation, which is well defined by unique factorisation in the PID $A$.) Hence
$(a)=\bigcap_i(p_i^{e_i})$.

Each $(p^{e})$ is primary: if $xy\in(p^{e})$ and $x\notin(p^{e})$, then $v_p(x)<e$ and
$v_p(x)+v_p(y)\ge e$, so $v_p(y)\ge1$, i.e. $y\in(p)=\sqrt{(p^{e})}$. The radicals $\sqrt{(p_i^{e_i})}=(p_i)$ are
distinct primes, and the decomposition is irredundant. Uniqueness: the set $\{(p_i)\}$ is exactly the set of
minimal primes of $(a)$, i.e. the primes containing $a$, and each exponent is $v_{p_i}(a)$, so both are determined
by $(a)$.

This verifies the Lasker–Noether theorem completely *in the special case of a PID* — existence and both uniqueness
clauses. It does not verify the general theorem, because the argument uses the existence and uniqueness of
factorisation into primes, which is exactly what a general Noetherian ring does not provide; the general proof
proceeds by Noetherian induction on irreducible ideals (Problem 31). $\blacksquare$

**24.** *Strategy: clear denominators and use the coprimality of numerator and denominator for $\mathbb{Z}$; use the
explicit minimal polynomial for $\mathbb{Z}[\sqrt5]$.*

*$\mathbb{Z}$ is integrally closed in $\mathbb{Q}$.* Let $x=a/b$ with $\gcd(a,b)=1$ and $b>0$, and suppose
$$
x^{n}+c_{n-1}x^{n-1}+\cdots+c_0=0,\qquad c_i\in\mathbb{Z}.
$$
Multiplying by $b^{n}$,
$$
a^{n}=-b\left(c_{n-1}a^{n-1}+c_{n-2}a^{n-2}b+\cdots+c_0b^{n-1}\right),
$$
so $b\mid a^{n}$. Since $\gcd(a,b)=1$, this forces $b=1$, hence $x=a\in\mathbb{Z}$. So the integral closure of
$\mathbb{Z}$ in $\mathbb{Q}$ is $\mathbb{Z}$.

*$\mathbb{Z}[\sqrt5]$ is not integrally closed.* Let $\alpha=\frac{1+\sqrt5}{2}$. Then $\alpha^{2}=\alpha+1$, so
$\alpha$ is a root of the monic polynomial $X^{2}-X-1\in\mathbb{Z}[X]$ and is therefore integral over
$\mathbb{Z}[\sqrt5]$. But $\alpha=\frac12+\frac12\sqrt5\notin\mathbb{Z}[\sqrt5]=\{a+b\sqrt5:a,b\in\mathbb{Z}\}$.
The integral closure of $\mathbb{Z}[\sqrt5]$ in $\mathbb{Q}(\sqrt5)$ is
$$
\mathbb{Z}[\alpha]=\left\{\frac{m+n\sqrt5}{2}:m,n\in\mathbb{Z},\ m\equiv n\ (\mathrm{mod}\ 2)\right\},
$$
the ring of integers of $\mathbb{Q}(\sqrt5)$. $\blacksquare$

**25.** *Strategy: use the bijection between primes of $A_{\mathfrak{p}}$ and primes of $A$ contained in
$\mathfrak{p}$, and extend chains to maximal ideals.*

By Theorem 7.5, primes of $A_{\mathfrak{p}}$ correspond to primes of $A$ contained in $\mathfrak{p}$, and the
correspondence preserves inclusions. Hence chains of primes below $\mathfrak{p}$ in $A$ correspond exactly to
chains of primes in $A_{\mathfrak{p}}$, so $\operatorname{ht}\mathfrak{p}=\dim A_{\mathfrak{p}}$.

For the global statement, every chain $\mathfrak{p}_0\subsetneq\cdots\subsetneq\mathfrak{p}_n$ in $A$ can be
extended at the top to a chain ending at a maximal ideal $\mathfrak{m}$ without changing its length (Proposition
7.2 supplies a maximal ideal containing $\mathfrak{p}_n$). Hence
$$
\dim A=\sup_{\mathfrak{m}}\operatorname{ht}\mathfrak{m}=\sup_{\mathfrak{m}}\dim A_{\mathfrak{m}} .
$$

Finally, $\dim A=0$ means that no strict inclusion of primes exists, i.e. every prime is maximal. $\blacksquare$

**26.** *Strategy: localise at $\mathfrak{p}$ to reduce to the case of a local ring, take a maximal ideal there,
and contract.*

We need the lemma: *if $A\subseteq B$ is integral and $B$ is a field, then $A$ is a field.* Proof: for
$0\ne a\in A$, the element $a^{-1}\in B$ is integral over $A$, so
$(a^{-1})^{n}+c_{n-1}(a^{-1})^{n-1}+\cdots+c_0=0$ with $c_i\in A$; multiplying by $a^{n-1}$ gives
$a^{-1}=-(c_{n-1}+c_{n-2}a+\cdots+c_0a^{n-1})\in A$.

Now let $\mathfrak{p}$ be a prime of $A$ and $S=A\setminus\mathfrak{p}$. Then $A_{\mathfrak{p}}\subseteq S^{-1}B$ is
integral (divide a monic equation by a common denominator). Choose a maximal ideal $\mathfrak{n}$ of $S^{-1}B$ and
put $\mathfrak{q}=\mathfrak{n}\cap B$. Then $S^{-1}B/\mathfrak{n}$ is a field, integral over the subring
$A_{\mathfrak{p}}/(\mathfrak{n}\cap A_{\mathfrak{p}})$, so that subring is a field by the lemma. Hence
$\mathfrak{n}\cap A_{\mathfrak{p}}$ is maximal in $A_{\mathfrak{p}}$, and the only maximal ideal there is
$\mathfrak{p}A_{\mathfrak{p}}$ (Corollary 7.6). Contracting to $A$ gives
$$
\mathfrak{q}\cap A=(\mathfrak{n}\cap A)=\mathfrak{p}.\qquad\blacksquare
$$

**27.** *Strategy: going up produces chains of the same length in $B$; incomparability prevents chains in $B$ from
being longer than their contractions.*

Let $\mathfrak{p}_0\subsetneq\cdots\subsetneq\mathfrak{p}_n$ be a chain in $A$. Choose $\mathfrak{q}_0$ over
$\mathfrak{p}_0$ by lying over, then apply going up repeatedly to obtain
$\mathfrak{q}_0\subsetneq\mathfrak{q}_1\subsetneq\cdots\subsetneq\mathfrak{q}_n$ with $\mathfrak{q}_i$ over
$\mathfrak{p}_i$; strictness follows because $\mathfrak{q}_i=\mathfrak{q}_{i+1}$ would contradict
$\mathfrak{p}_i\ne\mathfrak{p}_{i+1}$. Hence $\dim B\ge\dim A$.

Conversely, let $\mathfrak{q}_0\subsetneq\cdots\subsetneq\mathfrak{q}_m$ be a chain in $B$. Its contractions
$\mathfrak{p}_i=\mathfrak{q}_i\cap A$ form a chain, and by incomparability (Theorem 7.30) the inclusions remain
strict: if $\mathfrak{p}_i=\mathfrak{p}_{i+1}$ then two distinct primes of $B$ lie over the same prime of $A$,
which is forbidden. So $\dim A\ge\dim B$. Therefore $\dim A=\dim B$. $\blacksquare$

**28.** *Strategy: dimension $1$ means no strict inclusions among non-zero primes; then quote the characterisation
$A_{\mathfrak{p}}$ is a DVR.*

Let $A$ be a Dedekind domain, so $\dim A=1$ by definition. If $\mathfrak{p}\ne0$ is prime and
$\mathfrak{p}\subsetneq\mathfrak{q}$ for a prime $\mathfrak{q}$, then $(0)\subsetneq\mathfrak{p}\subsetneq\mathfrak{q}$
is a chain of length $2$, contradicting $\dim A=1$. So every non-zero prime is maximal.

Since every non-zero prime is maximal, Theorem 7.44 applies with $\mathfrak{m}=\mathfrak{p}$ and gives that
$A_{\mathfrak{p}}$ is a discrete valuation ring.

$\mathbb{Z}[x]$ is not a Dedekind domain because $\dim\mathbb{Z}[x]=2$: the chain
$$
(0)\subsetneq(2)\subsetneq(2,x)
$$
consists of primes ($\mathbb{Z}[x]/(2)\cong\mathbb{F}_2[x]$ is a domain, and $\mathbb{Z}[x]/(2,x)\cong\mathbb{F}_2$
is a field) and has length $2$. A Dedekind domain has dimension exactly $1$. $\blacksquare$

**29.** *Strategy: identify $\mathbb{Z}_p$ as the completion of $\mathbb{Z}_{(p)}$, then verify the DVR axioms
directly.*

By definition $\mathbb{Z}_p=\varprojlim_n\mathbb{Z}/p^{n}\mathbb{Z}$. The map $x\mapsto(x\bmod p)$ is a ring
homomorphism onto $\mathbb{F}_p$; its kernel is the set of elements whose first digit is zero, i.e. $(p)$. An
element $x$ with $x\not\equiv0\pmod p$ has an inverse: each component $x_n$ is a unit of $\mathbb{Z}/p^{n}$ and the
inverses are compatible, so they define an element of $\mathbb{Z}_p$. Hence $\mathbb{Z}_p$ is local with maximal
ideal $(p)$ and residue field $\mathbb{F}_p$.

It is Noetherian (completion of the Noetherian ring $\mathbb{Z}_{(p)}$, Theorem 7.49), of dimension $1$ (Theorem
7.49(iv), or directly: $(0)\subsetneq(p)$ is the only chain), and its maximal ideal is principal; so it is a DVR.

$p$ is not nilpotent: $p^{n}$ has digit $1$ in position $n$ and $0$ elsewhere, so $p^{n}\ne0$. Hence
$\mathbb{Z}_p$ is not a field and not reduced at $p$.

*Uncountable.* The map $\{0,1,\dots,p-1\}^{\mathbb{N}}\to\mathbb{Z}_p$, $(c_k)\mapsto\sum_kc_kp^{k}$, is injective:
two distinct digit sequences differ first at some index $k$, and the partial sums then differ modulo $p^{k+1}$.
The set of sequences is uncountable (Cantor), so $\mathbb{Z}_p$ is uncountable. This is compatible with being an
inverse limit of the finite rings $\mathbb{Z}/p^{n}$ because inverse limits of finite *discrete* spaces can be
uncountable — indeed $\{0,1\}^{\mathbb{N}}=\varprojlim\{0,1\}^{n}$ — and the maps in the system do not collapse
everything. $\blacksquare$

**30.** *Strategy: compute the quotients $\mathfrak{m}^{n}/\mathfrak{m}^{n+1}$ and identify the inverse limit with
the ring of formal power series.*

Let $A=k[x]_{(x)}$ and $\mathfrak{m}=(x)$. Every element of $A$ is $f/g$ with $g(0)\ne0$, and such a $g$ is a unit
modulo $x^{n}$ for every $n$. Hence the natural map $A/\mathfrak{m}^{n}=k[x]_{(x)}/(x^{n})\to k[x]/(x^{n})$ is an
isomorphism. Therefore
$$
\widehat{A}=\varprojlim_nA/\mathfrak{m}^{n}\cong\varprojlim_nk[x]/(x^{n})=k[[x]],
$$
the last being the definition of the formal power series ring as the inverse limit of the truncation maps.

The composite $\iota:A\to k[[x]]$ sends $f/g$ to the Taylor series of $f/g$ at $0$. It is injective because the
kernel is $\bigcap_n\mathfrak{m}^{n}=0$ (Krull's intersection theorem, Theorem 7.49(i)); equivalently, a non-zero
rational function has a non-zero Taylor expansion at a point where its denominator does not vanish. The image is
the subring of rational functions regular at $0$,
$$
\iota(A)=\left\{\frac{f}{g}:f,g\in k[x],\ g(0)\ne0\right\},
$$
which is strictly smaller than $k[[x]]$: for instance $\sum_{n\ge0}x^{n!}$ is a formal power series whose
coefficients do not satisfy a linear recurrence, so it is not the Taylor series of a rational function. $\blacksquare$

## Challenge

**31.** *Strategy: Noetherian induction reduces existence to irreducibility, and a stable ascending chain of
colon ideals reduces irreducibility to primeness of the radical.*

**(a) Every ideal is a finite intersection of irreducible ideals.** Suppose not, and let $\mathfrak{a}$ be a
maximal counterexample, which exists by Theorem 7.15(ii). Then $\mathfrak{a}$ is reducible: $\mathfrak{a}=\mathfrak{b}\cap\mathfrak{c}$
with $\mathfrak{b},\mathfrak{c}\supsetneq\mathfrak{a}$. By maximality, $\mathfrak{b}$ and $\mathfrak{c}$ are finite
intersections of irreducible ideals, hence so is $\mathfrak{a}$ — contradiction.

**(b) Every irreducible ideal is primary.** Let $\mathfrak{q}$ be irreducible and suppose $xy\in\mathfrak{q}$,
$x\notin\mathfrak{q}$ and $y\notin\sqrt{\mathfrak{q}}$; we derive a contradiction. Consider the ascending chain
$$
(\mathfrak{q}:y)\subseteq(\mathfrak{q}:y^{2})\subseteq\cdots,
$$
which stabilises because $A$ is Noetherian: say $(\mathfrak{q}:y^{n})=(\mathfrak{q}:y^{n+1})$ for all
$n\ge n_0$. Put $n=n_0$. Then $y^{n}\notin\mathfrak{q}$ (since $y\notin\sqrt{\mathfrak{q}}$), so
$\mathfrak{q}+(y^{n})\supsetneq\mathfrak{q}$, and $x\notin\mathfrak{q}$ gives
$\mathfrak{q}+(x)\supsetneq\mathfrak{q}$.

*Claim:* $\mathfrak{q}=(\mathfrak{q}+(x))\cap(\mathfrak{q}+(y^{n}))$. The inclusion $\subseteq$ is clear. For
$\supseteq$, let $z=q_1+ax=q_2+by^{n}$ with $q_i\in\mathfrak{q}$, $a,b\in A$. Then
$$
zy^{n}=q_1y^{n}+axy^{n}\in\mathfrak{q},
$$
because $xy\in\mathfrak{q}$ implies $xy^{n}\in\mathfrak{q}$. Also $z=q_2+by^{n}$, so
$zy^{n}=q_2y^{n}+by^{2n}\in\mathfrak{q}$, which forces $by^{2n}\in\mathfrak{q}$, i.e.
$b\in(\mathfrak{q}:y^{2n})=(\mathfrak{q}:y^{n})$; hence $by^{n}\in\mathfrak{q}$ and
$z=q_2+by^{n}\in\mathfrak{q}$, as claimed.

The claim expresses $\mathfrak{q}$ as an intersection of two strictly larger ideals, contradicting
irreducibility. Hence $\mathfrak{q}$ is primary: whenever $xy\in\mathfrak{q}$ and $y\notin\sqrt{\mathfrak{q}}$, we
must have $x\in\mathfrak{q}$. $\blacksquare$

**32.** *Strategy: clear denominators in a monic equation and use the absence of a common prime factor.*

Let $A$ be a UFD with fraction field $K$, and let $x=a/b\in K$ be integral over $A$; write $a,b\in A$ with no
common prime factor (equivalently, $\gcd(a,b)=1$ in the UFD sense) and $b\ne0$. From
$$
x^{n}+c_{n-1}x^{n-1}+\cdots+c_0=0,\qquad c_i\in A,
$$
multiplying by $b^{n}$ yields
$$
a^{n}=-b\left(c_{n-1}a^{n-1}+c_{n-2}a^{n-2}b+\cdots+c_0b^{n-1}\right),
$$
so $b\mid a^{n}$. If $p$ is a prime dividing $b$, then $p\mid a^{n}$, hence $p\mid a$ (primality), contradicting the
choice of $a,b$. So $b$ has no prime divisor, i.e. $b$ is a unit, and $x=a/b\in A$.

Hence $A$ is integrally closed. (This argument is Gauss's lemma applied to the monic polynomial $X^{n}+\cdots$: a
monic polynomial over a UFD factors over the fraction field exactly as it factors over the ring, so its roots in
$K$ that are algebraic integers lie in $A$.)

Since $k$ is a field, $k[x]$ is a UFD, and by Gauss's theorem $k[x,y]=k[x][y]$ is a UFD; likewise
$\mathbb{Z}[x]$ is a UFD because $\mathbb{Z}$ is. So both are integrally closed in their fraction fields.
$\blacksquare$

**33.** *Strategy: exhibit a module that is divisible, hence satisfies $\mathfrak{m}M=M$, but is not finitely
generated.*

Let $A=\mathbb{Z}_{(p)}$, with maximal ideal $\mathfrak{m}=pA$, and let $M=\mathbb{Q}$, viewed as an
$A$-module. For every $x\in\mathbb{Q}$, the element $x/p\in\mathbb{Q}$ satisfies $p\cdot(x/p)=x$; hence
$$
\mathfrak{m}M=p\mathbb{Q}=\mathbb{Q}=M,
$$
while $M\ne0$. But $M$ is not finitely generated over $A$: a finitely generated submodule of $\mathbb{Q}$ is
contained in $\frac1N\mathbb{Z}$ for some $N$ (clear for a finite number of generators $a_i/b_i$, taking
$N=\operatorname{lcm}(b_i)$), and $\mathbb{Q}\ne\frac1N\mathbb{Z}$.

*Where the proof breaks.* Theorem 7.20 begins by choosing a generating set $m_1,\dots,m_n$ of minimal size, and
this step requires finite generation. With no minimal generating set there is no $m_n$ to isolate, and the
computation $(1-a_n)m_n=\sum_{i<n}a_im_i$ has no content: for $M=\mathbb{Q}$ one could take $n=1$ and
$a_1=1$, giving $(1-1)m_1=0$, which is true but carries no contradiction. $\blacksquare$

**34.** *Strategy: Noether normalisation makes $A$ a finite module over a polynomial ring; if there were a
variable, that polynomial ring would be a non-field over which a field cannot be integral.*

Let $A$ be a finitely generated $k$-algebra that is a field. By Noether normalisation (Theorem 7.35) there are
algebraically independent $y_1,\dots,y_n\in A$ such that $A$ is a finitely generated module over
$B=k[y_1,\dots,y_n]$.

If $n\ge1$, then $B$ is not a field: $y_1\ne0$ has no inverse in $k[y_1,\dots,y_n]$, since a relation
$y_1\cdot h=1$ with $h\in k[y_1,\dots,y_n]$ is impossible by comparing degrees in $y_1$. But $A$ is a field and is
integral over $B$, so by Fact 7.27b (a field integral over a subring forces the subring to be a field) $B$ would be
a field — contradiction. Hence $n=0$.

With $n=0$, $A$ is a finitely generated $k$-module, i.e. a finite-dimensional $k$-vector space. Since $A$ is a
field, it is a finite algebraic extension of $k$. $\blacksquare$

*Remark.* This is the algebraic form of the Nullstellensatz; the geometric consequence is that the maximal ideals
of $k[x_1,\dots,x_n]$ over an algebraically closed $k$ are the ideals of points.

**35.** *Strategy: an element of an associated prime multiplies a complementary intersection to zero; conversely a
zero divisor must lie in the radical of some primary component.*

Write $(0)=\mathfrak{q}_1\cap\cdots\cap\mathfrak{q}_n$ irredundant with $\mathfrak{p}_i=\sqrt{\mathfrak{q}_i}$.

*Lemma.* If $\mathfrak{q}$ is $\mathfrak{p}$-primary and $y\notin\mathfrak{q}$, then $\sqrt{(\mathfrak{q}:y)}=\mathfrak{p}$.
Proof: if $z\in(\mathfrak{q}:y)$ then $zy\in\mathfrak{q}$, and $y\notin\mathfrak{q}$ with $\mathfrak{q}$ primary
gives $z\in\sqrt{\mathfrak{q}}=\mathfrak{p}$; so $(\mathfrak{q}:y)\subseteq\mathfrak{p}$ and
$\sqrt{(\mathfrak{q}:y)}\subseteq\mathfrak{p}$. Conversely, if $z\in\mathfrak{p}$ then $z^{m}\in\mathfrak{q}$ for
some $m$, hence $z^{m}y\in\mathfrak{q}$ and $z\in\sqrt{(\mathfrak{q}:y)}$.

*Every $\mathfrak{p}_i$ consists of zero divisors.* Let $x\in\mathfrak{p}_i$. By irredundance there is
$y\in\bigcap_{j\ne i}\mathfrak{q}_j$ with $y\notin\mathfrak{q}_i$; in particular $y\ne0$. By the lemma,
$x\in\sqrt{(\mathfrak{q}_i:y)}$, so $x^{k}y\in\mathfrak{q}_i$ for some $k\ge1$. For $j\ne i$, $y\in\mathfrak{q}_j$,
so $x^{k}y\in\mathfrak{q}_j$. Hence $x^{k}y\in\bigcap_j\mathfrak{q}_j=(0)$, i.e. $x^{k}y=0$ with $y\ne0$, so $x^{k}$
is a zero divisor, and therefore $x$ is one: if $x^{k}y=0$ and $y\ne0$ then either $xy=0$, or $xy\ne0$ and
$x(x^{k-1}y)=0$.

*Every zero divisor lies in some $\mathfrak{p}_i$.* Let $xy=0$ with $y\ne0$. Since $y\ne0=\bigcap_j\mathfrak{q}_j$,
there is $i$ with $y\notin\mathfrak{q}_i$. Then $xy=0\in\mathfrak{q}_i$ and $y\notin\mathfrak{q}_i$; since
$\mathfrak{q}_i$ is primary, $x\in\sqrt{\mathfrak{q}_i}=\mathfrak{p}_i$.

Hence $\operatorname{Zerodiv}(A)=\bigcup_i\mathfrak{p}_i$, the union of the associated primes of $(0)$.
$\blacksquare$

**36.** *Strategy: from any element outside $A$, a DVR produces a uniformiser and hence everything; and
$\mathbb{Z}[1/2]$ is a subring of $\mathbb{Q}$ strictly between $\mathbb{Z}$ and $\mathbb{Q}$.*

(a) Let $(A,\mathfrak{m})$ be a DVR with $\mathfrak{m}=(\pi)$ and fraction field $K$, and let
$A\subsetneq B\subseteq K$ be a ring. Choose $x\in B\setminus A$; then $x\in K$ and $x\notin A$, so
$x=u\pi^{-k}$ for some unit $u\in A$ and some $k\ge1$. Hence $\pi^{-k}=xu^{-1}\in B$, and then
$$
\pi^{-1}=\pi^{k-1}\cdot\pi^{-k}\in B
$$
since $\pi^{k-1}\in A\subseteq B$. Every element of $K$ is of the form $a\pi^{-m}$ with $a\in A$ and $m\ge0$,
hence lies in $B$. So $B=K$: no ring lies strictly between $A$ and $K$.

(b) For $\mathbb{Z}$, take $B=\mathbb{Z}[1/2]=\{a/2^{n}:a\in\mathbb{Z},\ n\ge0\}$. Then
$\mathbb{Z}\subsetneq B\subsetneq\mathbb{Q}$: the first inclusion is strict because $1/2\notin\mathbb{Z}$, and the
second is strict because $1/3\notin B$ (the denominator of a rational number in $B$ is a power of $2$, and
$1/3$ has denominator $3$). So $\mathbb{Z}$ is not maximal in its fraction field, in contrast with a DVR.
$\blacksquare$

<!--END-->

