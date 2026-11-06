# Diophantine Equations — Solutions

> [Diophantine Equations](README.md) · Solutions to the 36 problems in [exercises.md](exercises.md)

Every solution names the strategy and the theorem used, and displays the arithmetic. Numerical answers are checked by a second method wherever one exists. Section references point into the [tutorial](README.md).

## Beginner

**1.** *Strategy: compute $g=\gcd(a,b)$ and test $g\mid c$ (Theorem 7.1.1); when solvable, find one solution and apply Theorem 7.1.2.*

(a) $6x+9y=21$. $g = 3$ and $3 \mid 21$: solvable. Divide by $3$: $2x+3y = 7$. A solution is $(x_0,y_0) = (2,1)$, since $4+3 = 7$. By Theorem 7.1.2 with $g=3$,

$$x = 2+\frac{9}{3}t = 2+3t, \qquad y = 1-\frac{6}{3}t = 1-2t, \qquad t\in\mathbb{Z}.$$

*Check* at $t = -1$: $(x,y) = (-1,3)$ and $-6+27 = 21$ ✓.

(b) $15x+21y = 100$. $g = 3$, and $100 = 3\cdot33+1$ is not divisible by $3$. **No solution.** (Consistently: $15x+21y$ is always divisible by $3$, and $100$ is not.)

(c) $8x+12y=4$. $g = 4 \mid 4$: solvable. Divide by $4$: $2x+3y = 1$, solved by $(-1,1)$. Hence

$$x = -1+\frac{12}{4}t = -1+3t, \qquad y = 1-\frac{8}{4}t = 1-2t.$$

*Check* at $t=1$: $(2,-1)$ and $16-12 = 4$ ✓.

(d) $7x+11y = 1$. $g=1$: solvable. Euclidean algorithm: $11 = 7+4$, $7 = 4+3$, $4 = 3+1$, so

$$1 = 4-3 = 4-(7-4) = 2\cdot4-7 = 2(11-7)-7 = 2\cdot11-3\cdot7,$$

giving $(x_0,y_0) = (-3,2)$: $-21+22 = 1$ ✓. All solutions:

$$x = -3+11t, \qquad y = 2-7t.$$

**2.** *Strategy: run the extended Euclidean algorithm on $25$ and $17$.*

$25 = 17+8$, $17 = 2\cdot8+1$, so

$$1 = 17-2\cdot8 = 17-2(25-17) = 3\cdot17-2\cdot25.$$

Thus $(x_0,y_0) = (3,-2)$: $51-50 = 1$ ✓. All solutions:

$$x = 3+25t, \qquad y = -2-17t.$$

The condition $0\le x\le 24$ forces $t = 0$, so the unique such solution is $(3,-2)$.

*Check:* the next solutions in either direction are $(28,-19)$ and $(-22,15)$, whose $x$-coordinates leave the required range ✓.

**3.** *Strategy: solve the congruence for $y$ modulo $5$, then bound $y$.*

From $5x = 100-7y$ we need $7y\equiv100\equiv0\pmod 5$, i.e. $2y\equiv0\pmod5$, i.e. $y\equiv0\pmod 5$. Put $y = 5s$; then $5x = 100-35s$, so $x = 20-7s$. Non-negativity gives $s\ge0$ and $s\le\frac{20}{7} = 2.85\ldots$, so $s\in\{0,1,2\}$ and

$$(x,y) = (20,0),\quad (13,5),\quad (6,10).$$

*Check:* $100$ ✓; $65+35 = 100$ ✓; $30+70 = 100$ ✓. The next value $s=3$ would give $x = -1$.

**4.** *Strategy: solve the associated equation with right side $1$ and use linearity.*

(a) $3\cdot(-1)+4\cdot1 = 1$, so $(x_0,y_0) = (-1,1)$ and

$$x = -1+4t, \qquad y = 1-3t, \quad t\in\mathbb{Z}.$$

(b) For $3x+4y=25$ take $25\cdot(-1,1) = (-25,25)$ as a particular solution; then $x = -25+4t$, $y = 25-3t$. Non-negativity requires $25-3t\ge0$ (so $t\le8$) and $4t\ge25$ (so $t\ge7$). For $t=7$: $(3,4)$; for $t=8$: $(7,1)$. So

$$(x,y)\in\{(7,1),\,(3,4)\}.$$

*Check:* $21+4 = 25$ ✓; $9+16 = 25$ ✓.

**5.** *Strategy: compute $ab-a-b$ and $\frac{(a-1)(b-1)}{2}$ and verify by listing.*

With $a=3$, $b=4$: $ab-a-b = 12-3-4 = 5$, and $\frac{2\cdot3}{2} = 3$. Representable amounts: $3,4,6,7,8,9,\dots$ (all $n\ge6$: $6 = 2\cdot3$, $7 = 3+4$, $8 = 2\cdot4$, and then add $3$'s). Unpayable: $1,2,5$ — three of them, the largest being $5$ ✓. Both formulas hold.

**6.** *Strategy: the same, with a direct listing.*

$ab-a-b = 35-5-7 = 23$ and $\frac{(a-1)(b-1)}{2} = \frac{4\cdot6}{2} = 12$. Listing $1\le n\le 23$:

| unpayable | $1,\ 2,\ 3,\ 4,\ 6,\ 8,\ 9,\ 11,\ 13,\ 16,\ 18,\ 23$ |
|---|---|
| payable | $5,\ 7,\ 10,\ 12,\ 14,\ 15,\ 17,\ 19,\ 20,\ 21,\ 22$ |

Twelve unpayable, largest $23$, and everything from $24$ on is payable ($24 = 10+14$, $25 = 5\cdot5$, $26 = 5+21$, $27 = 20+7$, $28 = 4\cdot7$, then add $5$-coins) ✓.

**7.** *Strategy: substitute into $(m^{2}-n^{2},\,2mn,\,m^{2}+n^{2})$ and verify the Pythagoras identity.*

| $(m,n)$ | $m^{2}-n^{2}$ | $2mn$ | $m^{2}+n^{2}$ | check |
|---|---|---|---|---|
| $(2,1)$ | $3$ | $4$ | $5$ | $9+16 = 25$ ✓ |
| $(3,2)$ | $5$ | $12$ | $13$ | $25+144 = 169$ ✓ |
| $(4,1)$ | $15$ | $8$ | $17$ | $225+64 = 289$ ✓ |
| $(5,2)$ | $21$ | $20$ | $29$ | $441+400 = 841$ ✓ |

Each pair satisfies $m>n$, $\gcd(m,n)=1$ and $m+n$ odd, so each triple is primitive by Theorem 7.3.1.

**8.** *Strategy: identify the even leg $2mn$ and solve for $m,n$.*

$(20,21,29)$: the even leg is $20$, so $mn = 10$, and the odd leg is $m^{2}-n^{2} = 21$. The factorisations of $10$ are $(10,1)$ and $(5,2)$; the first gives $100-1 = 99\ne21$, the second gives $25-4 = 21$ ✓. So $m=5$, $n=2$, and $\gcd(5,2)=1$, $m+n = 7$ odd, $z = 25+4 = 29$ ✓. Primitive since $\gcd(20,21,29)=1$.

$(12,35,37)$: the even leg is $12$, so $mn = 6$, and $m^{2}-n^{2} = 35$. From $(6,1)$: $36-1 = 35$ ✓; from $(3,2)$: $9-4 = 5\ne35$. So $m=6$, $n=1$; $\gcd=1$, $m+n = 7$ odd, $z = 36+1 = 37$ ✓. Primitive.

**9.** *Strategy: factorise and check whether every prime $\equiv3\pmod4$ has an even exponent (Theorem 7.4.1).*

| $n$ | factorisation | verdict | representation |
|---|---|---|---|
| $21$ | $3\cdot7$ | **no** | $7\equiv3\pmod4$ occurs to the odd power $1$ |
| $45$ | $3^{2}\cdot5$ | yes | $3^{2}+6^{2} = 9+36$ |
| $50$ | $2\cdot5^{2}$ | yes | $1^{2}+7^{2} = 5^{2}+5^{2}$ |
| $65$ | $5\cdot13$ | yes | $1^{2}+8^{2} = 4^{2}+7^{2}$ |
| $90$ | $2\cdot3^{2}\cdot5$ | yes | $3^{2}+9^{2} = 9+81$ |

**10.** *Strategy: apply the algorithm of §7.5.2.*

$a_0 = \lfloor\sqrt3\rfloor = 1$, $m_0 = 0$, $d_0 = 1$. Then $m_1 = 1\cdot1-0 = 1$, $d_1 = (3-1)/1 = 2$, $a_1 = \lfloor(1+1)/2\rfloor = 1$; $m_2 = 2\cdot1-1 = 1$, $d_2 = (3-1)/2 = 1$, $a_2 = \lfloor 2/1\rfloor = 2$; and then the state $(m,d) = (1,2)$ recurs, so the period is $(1,2)$:

$$\sqrt3 = [1;\overline{1,2}].$$

Convergents: $p_0 = 1$, $q_0 = 1$; $p_1 = 1\cdot1+1 = 2$, $q_1 = 1\cdot1+0 = 1$; $p_2 = 2\cdot2+1 = 5$, $q_2 = 2\cdot1+1 = 3$; $p_3 = 1\cdot5+2 = 7$, $q_3 = 1\cdot3+1 = 4$; $p_4 = 2\cdot7+5 = 19$, $q_4 = 2\cdot4+3 = 11$. So

$$\frac11,\ \frac21,\ \frac53,\ \frac74,\ \frac{19}{11}, \qquad p^{2}-3q^{2} = -2,\ 1,\ -2,\ 1,\ -2.$$

The period length is $\ell = 2$, even, so $p_{\ell-1}/q_{\ell-1} = 2/1$ gives the fundamental solution: $4-3 = 1$ ✓. Indeed $(2,1)$ is the smallest solution.

**11.** *Strategy: multiply elements of $\mathbb{Z}[\sqrt2]$ and use $N(\alpha\beta)=N(\alpha)N(\beta)$.*

(a) $1^{2}-2\cdot1^{2} = -1$ ✓.

(b) $(1+\sqrt2)^{2} = 1+2\sqrt2+2 = 3+2\sqrt2$, so $(x,y) = (3,2)$ and $9-2\cdot4 = 1$ ✓.

(c) $(1+\sqrt2)^{3} = (3+2\sqrt2)(1+\sqrt2) = 3+3\sqrt2+2\sqrt2+4 = 7+5\sqrt2$: $49-2\cdot25 = -1$, so $(7,5)$ solves the **negative** equation. $(1+\sqrt2)^{4} = (7+5\sqrt2)(1+\sqrt2) = 7+7\sqrt2+5\sqrt2+10 = 17+12\sqrt2$: $289-2\cdot144 = 1$, so $(17,12)$ solves the positive equation.

So the powers alternate: odd powers solve $-1$, even powers solve $+1$, exactly as $N(1+\sqrt2) = -1$ predicts.

**12.** *Strategy: enumerate $a$ with $a^{2}\le n$ and check whether $n-a^{2}$ is a square.*

$n = 25$: $a = 0$ gives $25 = 5^{2}$ ✓; $a=1$ gives $24$ ✗; $a=2$ gives $21$ ✗; $a=3$ gives $16 = 4^{2}$ ✓; $a=4$ gives $9 = 3^{2}$ ✓; $a=5$ gives $0 = 0^{2}$ ✓. So, with $0\le a\le b$: $(0,5)$, $(3,4)$; allowing both orders, four non-negative solutions $(0,5),(3,4),(4,3),(5,0)$.

$n=65$: $a=0$: $65$ ✗; $a=1$: $64 = 8^{2}$ ✓; $a=2$: $61$ ✗; $a=3$: $56$ ✗; $a=4$: $49 = 7^{2}$ ✓; $a=5$: $40$ ✗; $a=6$: $29$ ✗; $a=7$: $16 = 4^{2}$ ✓; $a=8$: $1 = 1^{2}$ ✓. Non-negative solutions: $(1,8),(4,7),(7,4),(8,1)$ — four.

*Why these counts.* Jacobi's formula $r_2(n) = 4(d_1(n)-d_3(n))$, where $d_1,d_3$ count the divisors $\equiv1,\equiv3\pmod4$ (quoted; see Section 16 of the tutorial), gives the number of **signed ordered** representations. For $25$ the divisors $1,5,25$ are all $\equiv1\pmod4$, so $r_2(25) = 4\cdot3 = 12$; indeed $(\pm5,0)$ and $(0,\pm5)$ contribute $4$, and $(\pm3,\pm4)$, $(\pm4,\pm3)$ contribute $8$. For $65$ the divisors $1,5,13,65$ are all $\equiv1$, so $r_2(65) = 4\cdot4 = 16 = 8+8$, i.e. exactly two unordered pairs ✓.

## Intermediate

**13.** *Strategy: prove that representability of $n$ forbids representability of $N-n$, then use the canonical form to prove the converse direction.*

Let $N = ab-a-b$ and let $n$ be any integer.

*At most one.* Suppose both $n = ax_1+by_1$ and $N-n = ax_2+by_2$ with non-negative coefficients. Adding,

$$N = a(x_1+x_2)+b(y_1+y_2),$$

which contradicts Theorem 7.2.1. So at most one of the pair is representable.

*At least one.* If $n$ is representable, we are done. Otherwise write $n$ in the canonical form $n = aq+br$ with $0\le r\le a-1$ (Theorem 7.2.2). Since $n$ is not representable, $q\le-1$. Then

$$N-n = ab-a-b-aq-br = a(-1-q) + b(a-1-r),$$

and both coefficients are non-negative: $-1-q\ge0$ because $q\le-1$, and $a-1-r\ge0$ because $r\le a-1$. So $N-n$ is representable. (Check the algebra: $a(-1-q)+b(a-1-r) = -a-aq + ab-b-br = ab-a-b - aq-br$ ✓.)

*Verification for $(3,5)$*, $N = 7$:

| $n$ | $0$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ | $7$ |
|---|---|---|---|---|---|---|---|---|
| $n$ representable? | ✓ | · | · | ✓ | · | ✓ | ✓ | · |
| $7-n$ representable? | · | ✓ | ✓ | · | ✓ | · | · | ✓ |

Exactly one ✓ in each column.

**14.** *Strategy: use the parametrisation, then check divisibility by $2$ and by $3$.*

By Theorem 7.3.1 a primitive triangle has legs $m^{2}-n^{2}$ and $2mn$, so its area is

$$A = \frac{(m^{2}-n^{2})(2mn)}{2} = mn(m^{2}-n^{2}) = mn(m-n)(m+n).$$

*Divisibility by $2$:* $m+n$ is odd, so $m$ and $n$ have opposite parity, so one of them is even and $2\mid mn$.

*Divisibility by $3$:* if $3\nmid m$ and $3\nmid n$, then $m^{2}\equiv n^{2}\equiv1\pmod3$, so $3\mid(m^{2}-n^{2})$. In every case $3 \mid mn(m^{2}-n^{2})$.

Since $2$ and $3$ are coprime, $6 \mid A$ ✓.

*Area $30$:* solve $mn(m^{2}-n^{2}) = 30$. Try $m=3$, $n=2$: $3\cdot2\cdot5 = 30$ ✓, giving the triple $(5,12,13)$, whose area is $\frac{5\cdot12}{2} = 30$ ✓.

**15.** *Strategy: congruence modulo $4$ for the parity; a separate mod-$3$ argument for the factor $3$.*

*Parity.* If both legs were even then $2\mid z$, contradicting primitivity. If both were odd, $x^{2}+y^{2}\equiv1+1\equiv2\pmod 4$, but $z^{2}\equiv0$ or $1\pmod4$. So exactly one leg is even. Then $z^{2} = x^{2}+y^{2}$ is odd (odd + even), so $z$ is odd.

*Divisibility by $3$.* Suppose $3\nmid x$ and $3\nmid y$. Squares modulo $3$ are $0,1$, so $x^{2}\equiv y^{2}\equiv1\pmod3$ and $z^{2} = x^{2}+y^{2}\equiv2\pmod3$ — impossible. Hence $3\mid x$ or $3\mid y$.

**16.** *Strategy: expand both sides; then multiply representations pairwise.*

*Identity.* $(ac-bd)^{2}+(ad+bc)^{2} = a^{2}c^{2}-2abcd+b^{2}d^{2}+a^{2}d^{2}+2abcd+b^{2}c^{2} = a^{2}c^{2}+b^{2}d^{2}+a^{2}d^{2}+b^{2}c^{2} = (a^{2}+b^{2})(c^{2}+d^{2})$ ✓. Replacing $d$ by $-d$ gives the second form $(ac+bd)^{2}+(ad-bc)^{2}$.

*Numerical check.* $(1^{2}+2^{2})(3^{2}+4^{2}) = 5\cdot25 = 125$. First form with $(a,b) = (1,2)$, $(c,d) = (3,4)$: $(3-8)^{2}+(4+6)^{2} = 25+100 = 125$ ✓. Second form: $(3+8)^{2}+(4-6)^{2} = 121+4 = 125$ ✓.

*Representations of $1105$.* Since $5 = 1^{2}+2^{2}$, $13 = 2^{2}+3^{2}$, $17 = 1^{2}+4^{2}$, multiply $5\cdot13$ first:

$$(1^{2}+2^{2})(2^{2}+3^{2}) = (2-6)^{2}+(3+4)^{2} = 16+49 = 65, \qquad (2+6)^{2}+(3-4)^{2} = 64+1 = 65.$$

Now multiply each by $17 = 1^{2}+4^{2}$:

* from $65 = 4^{2}+7^{2}$: $(4-28)^{2}+(16+7)^{2} = 576+529 = 1105$, and $(4+28)^{2}+(16-7)^{2} = 1024+81 = 1105$;
* from $65 = 1^{2}+8^{2}$: $(1-32)^{2}+(4+8)^{2} = 961+144 = 1105$, and $(1+32)^{2}+(4-8)^{2} = 1089+16 = 1105$.

Hence

$$1105 = 4^{2}+33^{2} = 9^{2}+32^{2} = 12^{2}+31^{2} = 23^{2}+24^{2}.$$

All four are genuine and distinct ✓; by Jacobi's formula $r_2(1105) = 4\cdot8 = 32$ and each unordered pair of nonzero unequal entries accounts for $8$, so there are exactly four.

**17.** *Strategy: suppose $p\nmid a$ and derive a contradiction with Fermat's little theorem.*

Let $p\equiv3\pmod4$ be prime with $p\mid a^{2}+b^{2}$. If $p\nmid a$, then $a$ is invertible mod $p$; from $a^{2}\equiv-b^{2}$,

$$\left(ba^{-1}\right)^{2}\equiv-1 \pmod p.$$

Raise to the power $(p-1)/2$, which is **odd** because $p\equiv3\pmod4$:

$$1 \equiv \left(ba^{-1}\right)^{p-1} = \left[\left(ba^{-1}\right)^{2}\right]^{(p-1)/2} \equiv (-1)^{(p-1)/2} = -1 \pmod p,$$

where the first congruence is Fermat's little theorem applied to $c = ba^{-1}\not\equiv0$. Then $p \mid 2$, impossible. So $p\mid a$; then $p\mid b^{2}$ gives $p\mid b$. $\blacksquare$

**18.** *Strategy: Wilson's theorem, pairing $k$ with $p-k$.*

By Wilson, $(p-1)!\equiv-1\pmod p$. Pairing,

$$(p-1)! = \prod_{k=1}^{(p-1)/2}k(p-k) \equiv (-1)^{(p-1)/2}\left(\left(\tfrac{p-1}{2}\right)!\right)^{2}\pmod p.$$

Since $p\equiv1\pmod4$, the exponent $(p-1)/2$ is even, so $(-1)^{(p-1)/2} = 1$ and, with $u = \left(\frac{p-1}{2}\right)!$,

$$u^{2}\equiv-1\pmod p.$$

*Illustrations.*

* $p=5$: $u = 2! = 2$ and $2^{2} = 4\equiv-1\pmod5$ ✓.
* $p=13$: $u = 6! = 720 = 13\cdot55+5$, so $u\equiv5$ and $5^{2} = 25\equiv12\equiv-1\pmod{13}$ ✓.
* $p=17$: $u = 8! = 40320 = 17\cdot2371+13$, so $u\equiv13$ and $13^{2} = 169 = 17\cdot9+16\equiv-1\pmod{17}$ ✓.

**19.** *Strategy: exhibit an infinite family of powers with norm $-1$.*

Recall $N(x+y\sqrt2) = x^{2}-2y^{2}$ and $N(\alpha\beta) = N(\alpha)N(\beta)$ (Lemma 7.5.7). Since $N(1+\sqrt2) = 1-2 = -1$, every **odd** power has norm $-1$:

$$N\left((1+\sqrt2)^{2k+1}\right) = (-1)^{2k+1} = -1.$$

Write $(1+\sqrt2)^{n} = x_n+y_n\sqrt2$. The recursion $(x+y\sqrt2)(1+\sqrt2) = (x+2y)+(x+y)\sqrt2$ shows by induction that $x_n,y_n$ are positive integers for all $n\ge1$. Hence each odd power gives a solution of $x^{2}-2y^{2}=-1$ in positive integers, and the solutions are distinct because $(1+\sqrt2)^{n}$ is strictly increasing in $n$.

The first four:

$$(1+\sqrt2)^{1} = 1+\sqrt2 \Rightarrow (1,1),$$
$$(1+\sqrt2)^{3} = 7+5\sqrt2 \Rightarrow (7,5),$$
$$(1+\sqrt2)^{5} = 41+29\sqrt2 \Rightarrow (41,29),$$
$$(1+\sqrt2)^{7} = 239+169\sqrt2 \Rightarrow (239,169).$$

*Checks:* $1-2 = -1$ ✓; $49-50 = -1$ ✓; $1681-1682 = -1$ ✓; $57121-57122 = -1$ ✓.

**20.** *Strategy: reduce $x^{2}+1 = Dy^{2}$ modulo $4$.*

If $x^{2}-Dy^{2} = -1$ then $x^{2}+1 = Dy^{2}$. With $D\equiv3\pmod4$:

* if $y$ is even, $Dy^{2}\equiv0\pmod4$, so $x^{2}\equiv-1\equiv3\pmod 4$ — impossible, since squares are $0,1\pmod4$;
* if $y$ is odd, $Dy^{2}\equiv3\pmod4$, so $x^{2}\equiv2\pmod4$ — also impossible.

Hence there is no solution. $\blacksquare$

*Examples:* $D = 3$ and $D = 7$ (both $\equiv3\pmod4$). Indeed $x^{2}-3y^{2}=-1$ has no solution — the values of $x^{2}-3y^{2}$ near small solutions are $-2,+1,-2,+1,\dots$ — and $x^{2}-7y^{2}=-1$ likewise.

**21.** *Strategy: compute the square of $x_1+y_1\sqrt D$ and use multiplicativity of the norm.*

$$\left(x_1^{2}+Dy_1^{2}\right)^{2}-D\left(2x_1y_1\right)^{2} = x_1^{4}+2Dx_1^{2}y_1^{2}+D^{2}y_1^{4}-4Dx_1^{2}y_1^{2} = x_1^{4}-2Dx_1^{2}y_1^{2}+D^{2}y_1^{4} = \left(x_1^{2}-Dy_1^{2}\right)^{2} = 1.$$

So $(x_1^{2}+Dy_1^{2},\,2x_1y_1)$ is again a solution ✓.

*Iteration for $D=3$ from $(2,1)$:* $x_1^{2}+3y_1^{2} = 4+3 = 7$ and $2x_1y_1 = 4$, giving $(7,4)$; check $49-3\cdot16 = 49-48 = 1$ ✓. Next: $49+3\cdot16 = 97$ and $2\cdot7\cdot4 = 56$, giving $(97,56)$; check $9409-3\cdot3136 = 9409-9408 = 1$ ✓.

**22.** *Strategy: complete the square to reduce to a Pell equation.*

$T_n = m^{2}$ means $\frac{n(n+1)}{2} = m^{2}$, i.e. $n^{2}+n = 2m^{2}$. Multiplying by $4$: $4n^{2}+4n = 8m^{2}$, and adding $1$,

$$(2n+1)^{2} = 8m^{2}+1, \qquad\text{i.e.}\qquad x^{2}-8y^{2} = 1$$

with $x = 2n+1$ (odd) and $y = m$. Conversely any solution with $x$ odd and $y>0$ gives $n = (x-1)/2$ and $m = y$.

The fundamental solution of $x^{2}-8y^{2}=1$ is $(3,1)$: $9-8 = 1$ ✓. Multiplying repeatedly by $3+\sqrt8$:

| $k$ | $(x_k,y_k)$ | $n = (x-1)/2$ | $m$ | $T_n$ |
|---|---|---|---|---|
| $1$ | $(3,1)$ | $1$ | $1$ | $1 = 1^{2}$ |
| $2$ | $(17,6)$ | $8$ | $6$ | $36 = 6^{2}$ |
| $3$ | $(99,35)$ | $49$ | $35$ | $1225 = 35^{2}$ |
| $4$ | $(577,204)$ | $288$ | $204$ | $41616 = 204^{2}$ |

The recursion used is $(x,y)\mapsto(3x+8y,\,x+3y)$, obtained by multiplying by $3+\sqrt8$: $(17,6)$ from $(3,1)$ ✓, $(99,35)$ from $(17,6)$ ✓, $(577,204)$ from $(99,35)$ ✓.

So the first three square triangular numbers are $T_1 = 1$, $T_8 = 36$, $T_{49} = 1225$, and there are infinitely many.

**23.** *Strategy: a congruence for the first, a Pell equation for the second.*

*$3x^{2}+2 = y^{2}$.* Modulo $3$ this reads $y^{2}\equiv2\pmod3$, but the squares modulo $3$ are $0$ and $1$. No solution ✓.

*$3x^{2}+1 = y^{2}$* is $y^{2}-3x^{2} = 1$, with $x$ in the role of $y$ in the standard notation. The convergents of $\sqrt3$ give the solutions: from Exercise 10, $p^{2}-3q^{2} = 1$ at $(2,1)$, $(7,4)$, $(26,15)$, $(97,56)$ (each obtained from the previous by $(p,q)\mapsto(2p+3q,\,p+2q)$). In the notation of the exercise, $(x,y) = (q,p)$:

$$(1,2),\quad (4,7),\quad (15,26),\quad (56,97).$$

*Checks:* $3+1 = 4 = 2^{2}$ ✓; $48+1 = 49 = 7^{2}$ ✓; $675+1 = 676 = 26^{2}$ ✓; $9408+1 = 9409 = 97^{2}$ ✓.

**24.** *Strategy: substitute $b = a+1$ into both formulas, then verify by listing.*

$ab-a-b = a(a+1)-a-(a+1) = a^{2}+a-2a-1 = a^{2}-a-1$ ✓, and $\frac{(a-1)(b-1)}{2} = \frac{(a-1)a}{2}$ ✓.

*$a=3$, $b=4$:* the largest unpayable is $9-3-1 = 5$ and the count is $\frac{2\cdot3}{2} = 3$, matching the list $1,2,5$ of Exercise 5 ✓.

*$a=4$, $b=5$:* the largest is $16-4-1 = 11$ and the count is $\frac{3\cdot4}{2} = 6$. Listing: payable are $4,5,8,9,10,12,13,14,15,\dots$; unpayable are $1,2,3,6,7,11$ — six of them, largest $11$ ✓.

## Advanced

**25.** *Strategy: subtract the two equations and use Euclid's lemma after dividing by $g$.*

Let $g = \gcd(a,b)$, suppose $ax_0+by_0 = c$, and let $(x,y)$ be any integer solution.

*The displayed family consists of solutions.* For every $t\in\mathbb{Z}$,

$$a\left(x_0+\frac bg t\right)+b\left(y_0-\frac ag t\right) = ax_0+by_0+\frac{ab}{g}t-\frac{ab}{g}t = c.$$

*Every solution is in the family.* Subtracting the two equations,

$$a(x-x_0)+b(y-y_0) = 0. \tag{$*$}$$

Divide $(*)$ by $g$: $\frac ag(x-x_0) = -\frac bg(y-y_0)$. By definition of $g$, $\gcd\!\left(\frac ag,\frac bg\right) = 1$ — this is the only place coprimality is used, and it is why one must divide **first** and apply Euclid's lemma **second**. Since $\frac ag$ and $\frac bg$ are coprime, $\frac bg \mid (x-x_0)$: there is $t\in\mathbb{Z}$ with

$$x - x_0 = \frac bg t.$$

Substituting into $(*)$: $\frac ag\cdot\frac bg t = -\frac bg(y-y_0)$. If $b\ne0$ we may cancel $\frac bg$, getting $y-y_0 = -\frac ag t$. If $b = 0$ then $g = \lvert a\rvert$ and $(*)$ reads $a(x-x_0) = 0$, so $x = x_0$ and $y$ is arbitrary — the family $\left(x_0+\frac0g t,\, y_0-\frac ag t\right) = (x_0, y_0-\frac{a}{\lvert a\rvert}t)$ runs over all $y\in\mathbb{Z}$ as $t$ varies, and the claim still holds. $\blacksquare$

**26.** *Strategy: for non-representability, a congruence; for representability, the canonical form.*

Write $N = ab-a-b$.

*$N$ is not representable.* Suppose $N = ax+by$ with $x,y\ge0$. Then $ab = a(x+1)+b(y+1)$. Reducing modulo $a$: $b(y+1)\equiv0\pmod a$. Since $\gcd(a,b)=1$, this gives $a \mid (y+1)$. As $y+1\ge1$, we get $y+1\ge a$, hence $b(y+1)\ge ab$, hence $a(x+1)\le0$, hence $x\le-1$ — contradicting $x\ge0$.

*Every $n>N$ is representable.* Fix $n>N$. Because $\gcd(a,b)=1$, $b$ is invertible modulo $a$, so there is a unique $y\in\{0,1,\dots,a-1\}$ with $by\equiv n\pmod a$. Then $a\mid(n-by)$; let $x = (n-by)/a\in\mathbb{Z}$, so that $n = ax+by$. If $x\le-1$ then

$$n = ax+by \le -a+b(a-1) = ab-a-b = N,$$

contradicting $n>N$. Hence $x\ge0$, and $(x,y)$ is the required representation. $\blacksquare$

**27.** *Strategy: the canonical form $n = aq+br$, and a floor identity proved by a permutation argument.*

*Canonical form.* Every integer $n$ can be written uniquely as $n = aq+br$ with $q\in\mathbb{Z}$ and $0\le r\le a-1$: the residue $r$ is determined by $br\equiv n\pmod a$ (unique since $b$ is invertible mod $a$), and then $q = (n-br)/a$.

*$n$ is representable iff $q\ge0$.* If $n = ax+by$ with $x,y\ge0$, apply the transformation $(x,y)\mapsto(x+b,\,y-a)$ repeatedly until the $b$-coefficient lies in $[0,a-1]$; this preserves $ax+by$, leaves the $a$-coefficient $\ge0$ throughout (it only increases), and terminates. The resulting representation is the canonical one, so its $q$ is $\ge0$. Conversely $q\ge0$ exhibits a representation with non-negative coefficients.

*Counting.* For $n\ge0$ non-representable we need $q\le-1$. Fix $r\in[0,a-1]$; the values $n = aq+br$ with $q\le-1$ and $n\ge0$ correspond to $1\le\lvert q\rvert\le br/a$, so there are exactly $\left\lfloor br/a\right\rfloor$ of them. Hence

$$\#\{\text{non-representable } n\ge0\} = \sum_{r=0}^{a-1}\left\lfloor\frac{br}{a}\right\rfloor.$$

*The floor identity.* Since $\gcd(a,b)=1$, the residues $br \bmod a$ for $r = 0,\dots,a-1$ are a permutation of $0,\dots,a-1$. Therefore

$$\sum_{r=0}^{a-1}\left\{\frac{br}{a}\right\} = \sum_{r=0}^{a-1}\frac{r}{a} = \frac{a-1}{2}, \qquad\text{and}\qquad \sum_{r=0}^{a-1}\frac{br}{a} = \frac{b(a-1)}{2}.$$

Subtracting, using $\lfloor x\rfloor = x-\{x\}$ term by term,

$$\sum_{r=0}^{a-1}\left\lfloor\frac{br}{a}\right\rfloor = \frac{b(a-1)}{2}-\frac{a-1}{2} = \frac{(a-1)(b-1)}{2}.$$

Since $0$ is representable ($0 = a\cdot0+b\cdot0$), the non-representable non-negative integers are all positive, so this is also the number of positive non-representable integers. $\blacksquare$

**28.** *Strategy: sufficiency by direct verification, necessity by factoring $y^{2} = z^{2}-x^{2}$.*

*Sufficiency.* Let $m>n\ge1$, $\gcd(m,n)=1$, $m+n$ odd, and put $x = m^{2}-n^{2}$, $y = 2mn$, $z = m^{2}+n^{2}$. Then

$$x^{2}+y^{2} = m^{4}-2m^{2}n^{2}+n^{4}+4m^{2}n^{2} = m^{4}+2m^{2}n^{2}+n^{4} = z^{2}.$$

Primitivity: if a prime $p$ divides $x,y,z$, then for odd $p$ we get $p \mid 2m^{2}$ and $p \mid 2n^{2}$ from $x+z = 2m^{2}$ and $z-x = 2n^{2}$, so $p\mid m$ and $p\mid n$ — impossible; for $p=2$, $2\mid z$ and $2\mid 2mn$ force $m^{2}+n^{2}$ even, i.e. $m,n$ of the same parity, contradicting $m+n$ odd. So the triple is primitive.

*Necessity.* Let $(x,y,z)$ be primitive with positive entries.

(i) Not both legs even (else $2\mid z$, contradicting primitivity). Not both odd (else $x^{2}+y^{2}\equiv2\pmod4$, impossible for a square). So exactly one leg is even; assume $y$ even, so $x,z$ odd.

(ii) Set $u = (z+x)/2$ and $v = (z-x)/2$. These are positive integers with $u>v$, $u+v = z$, $u-v = x$, and

$$uv = \frac{z^{2}-x^{2}}{4} = \frac{y^{2}}{4} = \left(\frac y2\right)^{2}.$$

(iii) $\gcd(u,v)=1$: a common divisor divides $u+v = z$ and $u-v = x$, hence divides $\gcd(x,z)$; and $\gcd(x,z)=1$ because a prime dividing both divides $z^{2}-x^{2} = y^{2}$ and hence $y$, contradicting primitivity.

(iv) By Lemma 7.6.1, two coprime integers with square product are squares: $u = m^{2}$, $v = n^{2}$ with $m>n\ge1$, $\gcd(m,n)=1$. Then $z = m^{2}+n^{2}$, $x = m^{2}-n^{2}$, $y = 2mn$, and $m+n$ odd because $x = m^{2}-n^{2}$ is odd. $\blacksquare$

**29.** *Strategy: peel off one prime at a time.*

Let $n = a^{2}+b^{2}$ and let $p\equiv3\pmod4$ be a prime divisor of $n$. By Exercise 17 (Lemma 7.4.2), $p\mid a$ and $p\mid b$. Write $a = pa'$, $b = pb'$; then

$$n = p^{2}\left(a'^{2}+b'^{2}\right),$$

so $p^{2}\mid n$ and $n/p^{2} = a'^{2}+b'^{2}$ is again a sum of two squares. Iterating, each time we divide by $p^{2}$ until $p$ no longer divides the remaining number (which is still a sum of two squares, hence if $p$ divides it, $p$ divides both its coordinates, so the division can continue). The process must stop, and when it does the residual number is not divisible by $p$. Hence the total exponent of $p$ in $n$ is even.

Since this holds for every prime $p\equiv3\pmod4$, the necessity direction is proved. $\blacksquare$

**30.** *Strategy: Wilson produces a square root of $-1$; the pigeonhole produces $c,d$ with $p\mid c^{2}+d^{2}$ and $c^{2}+d^{2}<2p$.*

Let $p\equiv1\pmod4$ be prime. By Exercise 18 there is $u$ with $u^{2}\equiv-1\pmod p$.

Let $M = \lfloor\sqrt p\rfloor$. Consider the $(M+1)^{2}$ integers $a+ub$ with $0\le a,b\le M$. Since $(M+1)^{2}>p$, two distinct pairs give the same residue modulo $p$:

$$a_1+ub_1\equiv a_2+ub_2\pmod p.$$

Put $c = a_1-a_2$, $d = b_1-b_2$, not both zero, with $\lvert c\rvert,\lvert d\rvert\le M<\sqrt p$. Then $c\equiv-ud\pmod p$, so

$$c^{2}\equiv u^{2}d^{2}\equiv-d^{2}\pmod p, \qquad\text{i.e.}\qquad p\mid c^{2}+d^{2}.$$

Now $0<c^{2}+d^{2}<2p$: the strict upper bound holds because each of $c^{2},d^{2}$ is at most $M^{2}<p$, and they are not both zero. The only positive multiple of $p$ strictly below $2p$ is $p$ itself, so $c^{2}+d^{2} = p$. Taking $a = \lvert c\rvert$, $b = \lvert d\rvert$ gives $p = a^{2}+b^{2}$. $\blacksquare$

*Why $c^{2}+d^{2}$ cannot be $2p$ or larger:* the bound $\lvert c\rvert,\lvert d\rvert\le M$ with $M = \lfloor\sqrt p\rfloor$ gives $c^{2}+d^{2}\le 2M^{2}<2p$, and since each term is $<p$ the sum is in fact $<2p$; the value $2p$ would require $c^{2} = d^{2} = p$, impossible. This is exactly the point where the choice of $\lfloor\sqrt p\rfloor$ (rather than a larger bound) matters.

**31.** *Strategy: induction for (a); the straddling property of convergents for (b).*

(a) For $k=0$: $p_0q_{-1}-p_{-1}q_0 = a_0\cdot0-1\cdot1 = -1 = (-1)^{-1}$ ✓. For $k\ge1$,

$$p_kq_{k-1}-p_{k-1}q_k = (a_kp_{k-1}+p_{k-2})q_{k-1}-p_{k-1}(a_kq_{k-1}+q_{k-2}) = p_{k-2}q_{k-1}-p_{k-1}q_{k-2},$$

which is the negative of the same expression with $k$ replaced by $k-1$. Hence the value is multiplied by $-1$ at each step, giving $(-1)^{k-1}$ ✓. (Consequently $\gcd(p_k,q_k)=1$, since any common divisor divides $\pm1$.)

(b) The convergents straddle $\alpha$: $\alpha$ lies strictly between $p_k/q_k$ and $p_{k+1}/q_{k+1}$. Hence

$$\left\lvert\alpha-\frac{p_k}{q_k}\right\rvert < \left\lvert\frac{p_{k+1}}{q_{k+1}}-\frac{p_k}{q_k}\right\rvert = \frac{\lvert p_{k+1}q_k-p_kq_{k+1}\rvert}{q_kq_{k+1}} = \frac{1}{q_kq_{k+1}},$$

using (a) in the last step.

*Monotonicity.* $q_0 = 1$, $q_1 = a_1\ge1$, and for $k\ge2$ we have $q_k = a_kq_{k-1}+q_{k-2}$ with $a_k\ge1$ and $q_{k-2}\ge1$, so $q_k\ge q_{k-1}+1>q_{k-1}$. Hence $q_k$ is strictly increasing for $k\ge1$, and $q_{k+1}>q_k$ gives

$$\left\lvert\alpha-\frac{p_k}{q_k}\right\rvert < \frac{1}{q_kq_{k+1}} < \frac{1}{q_k^{2}}. \qquad \blacksquare$$

**32.** *Strategy: minimal counterexample, the classification of primitive triples, and a second application of it.*

Suppose $x^{4}+y^{4}=z^{2}$ has a solution in positive integers and choose one with $z$ minimal.

(i) *$\gcd(x,y)=1$.* Otherwise a prime $p$ divides $x$ and $y$; then $p^{4}\mid z^{2}$, so $p^{2}\mid z$, and $(x/p,y/p,z/p^{2})$ is a solution with a smaller third coordinate. Contradiction.

(ii) *$y$ may be assumed even.* If $x,y$ were both odd, $x^{4}+y^{4}\equiv1+1\equiv2\pmod{16}$ (odd fourth powers are $\equiv1\pmod{16}$), but squares are $0,1,4,9\pmod{16}$. So exactly one is even; rename so that $y$ is even, $x$ and $z$ odd.

(iii) *First triple.* $(x^{2})^{2}+(y^{2})^{2} = z^{2}$ with $\gcd(x^{2},y^{2})=1$ is primitive, and the even leg is $y^{2}$. By Theorem 7.3.1 there are $m>n\ge1$ with $\gcd(m,n)=1$, $m+n$ odd, and

$$x^{2} = m^{2}-n^{2}, \qquad y^{2} = 2mn, \qquad z = m^{2}+n^{2}.$$

Since $x^{2} = m^{2}-n^{2}$ is odd, $m,n$ have opposite parity; $m$ is odd and $n$ is even.

(iv) *Second triple.* $x^{2}+n^{2} = m^{2}$ with $\gcd(n,m)=1$ is primitive, and its even leg is $n$ (as $m,x$ are odd, $n^{2} = m^{2}-x^{2}\equiv1-1\equiv0\pmod 8$). So there are $u>v\ge1$ with $\gcd(u,v)=1$, $u+v$ odd, and

$$n = 2uv, \qquad x = u^{2}-v^{2}, \qquad m = u^{2}+v^{2}.$$

(v) *A smaller solution.* Then

$$y^{2} = 2mn = 2\left(u^{2}+v^{2}\right)(2uv) = 4uv\left(u^{2}+v^{2}\right),$$

so $(y/2)^{2} = uv(u^{2}+v^{2})$. The three factors are pairwise coprime: $\gcd(u,v)=1$, $\gcd(u,u^{2}+v^{2}) = \gcd(u,v^{2})=1$, $\gcd(v,u^{2}+v^{2}) = \gcd(v,u^{2}) = 1$. By Lemma 7.6.1 each is a square:

$$u = r^{2}, \qquad v = s^{2}, \qquad u^{2}+v^{2} = t^{2}.$$

Then $r^{4}+s^{4} = u^{2}+v^{2} = t^{2}$, so $(r,s,t)$ is a solution, and

$$t^{2} = u^{2}+v^{2} = m < m^{2}+n^{2} = z,$$

so $t<z$, contradicting minimality.

Hence no solution exists. For the deduction: given $x^{4}+y^{4} = z^{4}$ with $xyz\ne0$, the triple $(x,y,z^{2})$ solves $X^{4}+Y^{4}=Z^{2}$ with $Z = z^{2}>0$, impossible. $\blacksquare$

**33.** *Strategy: divide an arbitrary solution by the largest power of $\varepsilon$ that does not exceed it, and show the quotient must be $1$.*

Let $\varepsilon = x_1+y_1\sqrt D>1$ be minimal among solutions of $x^{2}-Dy^{2}=1$ with $x,y\in\mathbb{N}$. Let $\alpha = x+y\sqrt D>1$ be any solution.

*Choice of $n$.* Since $\varepsilon>1$, the powers $\varepsilon^{n}$ increase without bound, so there is a unique $n\ge1$ with $\varepsilon^{n}\le\alpha<\varepsilon^{n+1}$.

*The quotient is of the right shape.* $\varepsilon^{-n} = (x_1-y_1\sqrt D)^{n}$ is of the form $u+v\sqrt D$ with $u,v\in\mathbb{Z}$ (binomial expansion). So $\beta = \alpha\varepsilon^{-n}$ is also of the form $u+v\sqrt D$ with integers. Also $N(\beta) = N(\alpha)N(\varepsilon)^{-n} = 1$, and $\beta\bar\beta = 1$ forces $\bar\beta = 1/\beta$, so

$$u = \frac{\beta+\beta^{-1}}{2}, \qquad v = \frac{\beta-\beta^{-1}}{2\sqrt D}, \qquad u\ge1 \text{ by AM–GM}.$$

*The quotient is $1$.* If $v\ne0$ then $\lvert v\rvert\ge1$ and

$$\beta = u+v\sqrt D\ge u+\sqrt D\ge1+\sqrt D.$$

But $\varepsilon = x_1+y_1\sqrt D\ge1+\sqrt D$ (as $x_1,y_1\ge1$), so $\beta\ge\varepsilon$, contradicting $\beta<\varepsilon$. Hence $v = 0$, $u^{2} = 1$, and $\beta = 1$.

*Conclusion.* $\alpha = \varepsilon^{n}$, so every positive solution is a power. Conversely each $\varepsilon^{n} = x_n+y_n\sqrt D$ has $x_n,y_n\in\mathbb{N}$: it is an integer combination and $\varepsilon^{n}\cdot\varepsilon^{-n} = 1$ with $\varepsilon^{-n}\in(0,1]$ gives $x_n>0$ and $x_n-y_n\sqrt D>0$, so $y_n>0$. The exponent $n$ is unique because $n\mapsto\varepsilon^{n}$ is strictly increasing. $\blacksquare$

## Challenge

**34.** *Strategy: factor $y^{2}+2$ in $\mathbb{Z}[\sqrt{-2}]$, show the factors are coprime, and compare coefficients of a cube.*

The equation is $y^{2}+2 = x^{3}$, i.e. $\left(y+\sqrt{-2}\right)\left(y-\sqrt{-2}\right) = x^{3}$.

*Step 1: $x$ and $y$ are odd.* If $y$ were even, then $y^{2}+2\equiv2\pmod4$, so $x^{3}\equiv2\pmod 4$; but a cube congruent to $2$ modulo $4$ would force $x$ even, and then $x^{3}\equiv0\pmod 8$, contradicting $x^{3}\equiv2\pmod4$. So $y$ is odd, and $y^{2}+2\equiv1+2 = 3\pmod 8$, so $x^{3}\equiv3\pmod8$, which forces $x$ odd.

*Step 2: the factors are coprime.* Let $\pi$ divide both $y+\sqrt{-2}$ and $y-\sqrt{-2}$ in $\mathbb{Z}[\sqrt{-2}]$. Then $\pi$ divides their difference $2\sqrt{-2}$ and their sum $2y$, so

$$N(\pi) \mid N(2\sqrt{-2}) = 8, \qquad N(\pi)\mid N(2y) = 4y^{2}.$$

Since $y$ is odd, $\gcd(8,4y^{2}) = 4$, so $N(\pi)\in\{1,2,4\}$.

* If $N(\pi) = 2$, then $\pi$ is associate to $\sqrt{-2}$ (the only elements of norm $2$ are $\pm\sqrt{-2}$), so $\sqrt{-2}\mid y+\sqrt{-2}$, hence $\sqrt{-2}\mid y$, i.e. $2\mid y$ — impossible.
* If $N(\pi)=4$, then $\pi$ is associate to $2 = -(\sqrt{-2})^{2}$, so again $\sqrt{-2}\mid\pi\mid y+\sqrt{-2}$ and $2\mid y$ — impossible.

Hence $N(\pi)=1$ and $\pi$ is a unit: the factors are coprime.

*Step 3: each factor is a cube.* In the unique factorisation domain $\mathbb{Z}[\sqrt{-2}]$ the units are $\pm1$, and $-1 = (-1)^{3}$ is a cube. Since the two coprime factors have a cube as product, every irreducible exponent in each is divisible by $3$; so there are $a,b\in\mathbb{Z}$ with

$$y+\sqrt{-2} = \left(a+b\sqrt{-2}\right)^{3}.$$

*Step 4: expand and compare.* As computed in Theorem 7.7.4,

$$\left(a+b\sqrt{-2}\right)^{3} = \left(a^{3}-6ab^{2}\right)+\left(3a^{2}b-2b^{3}\right)\sqrt{-2}.$$

Comparing the $\sqrt{-2}$-coefficients and the rational parts:

$$1 = b\left(3a^{2}-2b^{2}\right), \qquad y = a\left(a^{2}-6b^{2}\right).$$

The first equation forces $b = \pm1$: if $b = 1$ then $3a^{2}-2 = 1$ gives $a^{2} = 1$, so $a = \pm1$; if $b = -1$ then $3a^{2}-2 = -1$ gives $3a^{2} = 1$, impossible.

*Step 5: read off.* With $a = 1$, $b = 1$: $y = 1\cdot(1-6) = -5$ and $x^{3} = N(a+b\sqrt{-2}) = 1+2 = 3$, so $x = 3$ and $(x,y) = (3,-5)$. With $a = -1$, $b=1$: $y = -1\cdot(1-6) = 5$ and $x = 3$, giving $(3,5)$. These exhaust the possibilities. $\blacksquare$

*Check:* $5^{2}+2 = 27 = 3^{3}$ ✓.

**35.** *Strategy: the identity $2(a^{2}+b^{2}) = (a+b)^{2}+(a-b)^{2}$ and its converse.*

*If $n = a^{2}+b^{2}$* then

$$2n = 2a^{2}+2b^{2} = (a+b)^{2}+(a-b)^{2},$$

a sum of two squares ✓.

*Conversely,* suppose $2n = c^{2}+d^{2}$. Modulo $2$, $c^{2}+d^{2}\equiv c+d\equiv0$, so $c$ and $d$ have the same parity. Then $c+d$ and $c-d$ are both even, so

$$n = \frac{c^{2}+d^{2}}{2} = \left(\frac{c+d}{2}\right)^{2}+\left(\frac{c-d}{2}\right)^{2},$$

a sum of two squares ✓.

*Closure under multiplication* is Lemma 7.4.3: $(a^{2}+b^{2})(c^{2}+d^{2}) = (ac-bd)^{2}+(ad+bc)^{2}$.

*Closure under multiplication by a square:* $n\cdot k^{2} = (ak)^{2}+(bk)^{2}$ if $n = a^{2}+b^{2}$ ✓.

These three facts together reprove the sufficiency half of Theorem 7.4.1: writing $n = 2^{e}\prod p_i^{a_i}\prod q_j^{2c_j}$ with $p_i\equiv1\pmod4$ and $q_j\equiv3\pmod4$, each factor is a sum of two squares, so $n$ is.

**36.** *Strategy: (a) the mod-$8$ obstruction plus a descent by $4$; (b) a direct search; (c) statement.*

(a) *No number $\equiv7\pmod 8$ is a sum of three squares.* Squares modulo $8$ are $0,1,4$, so a sum of three squares modulo $8$ lies in

$$\{0+0+0,\ 0+0+1,\ 0+0+4,\ 0+1+1,\ 0+1+4,\ 0+4+4,\ 1+1+1,\ 1+1+4,\ 1+4+4,\ 4+4+4\} \equiv \{0,1,2,3,4,5,6\},$$

never $7$. (Explicitly the possible residues are $0,1,2,3,4,5,6$; the value $7$ is absent.)

*Descent by $4$.* Suppose $4m = x^{2}+y^{2}+z^{2}$. Squares modulo $4$ are $0,1$, and a sum of three of them is $\equiv0\pmod4$ only if all three are $\equiv0$ (sums $1,2,3$ are also possible but congruent to $1,2,3$). So $x,y,z$ are all even, and

$$m = \left(\frac x2\right)^{2}+\left(\frac y2\right)^{2}+\left(\frac z2\right)^{2}$$

is a sum of three squares. By contraposition: if $m$ is not a sum of three squares, neither is $4m$. Inducting on $a$, if $8b+7$ is not a sum of three squares then neither is $4^{a}(8b+7)$.

(b) Checking $1\le n\le40$, the numbers that are **not** sums of three squares are

$$7,\ 15,\ 23,\ 28,\ 31,\ 39.$$

Indeed $7 = 8\cdot0+7$, $15 = 8\cdot1+7$, $23 = 8\cdot2+7$, $28 = 4\cdot(8\cdot0+7)$, $31 = 8\cdot3+7$, $39 = 8\cdot4+7$ — all of the form $4^{a}(8b+7)$. Every other $n\le40$ has an explicit representation, for instance $1 = 1+0+0$, $2 = 1+1+0$, $3 = 1+1+1$, $4 = 4+0+0$, $5 = 4+1+0$, $6 = 4+1+1$, $8 = 4+4+0$, $9 = 4+4+1$, $10 = 9+1+0$, $11 = 9+1+1$, $12 = 4+4+4$, $13 = 9+4+0$, $14 = 9+4+1$, $16 = 16+0+0$, $17 = 16+1+0$, $18 = 16+1+1$, $19 = 9+9+1$, $20 = 16+4+0$, $21 = 16+4+1$, $22 = 9+9+4$, $24 = 16+4+4$, $25 = 16+9+0$, $26 = 25+1+0$, $27 = 25+1+1$, $29 = 25+4+0$, $30 = 25+4+1$, $32 = 16+16+0$, $33 = 25+4+4$, $34 = 25+9+0$, $35 = 25+9+1$, $36 = 36+0+0$, $37 = 36+1+0$, $38 = 25+9+4$, $40 = 36+4+0$.

(c) **Legendre's three-square theorem.** A positive integer $n$ is a sum of three integer squares if and only if $n$ is **not** of the form $4^{a}(8b+7)$ with $a,b\ge0$.

Part (a) proves the "only if" direction — the obstruction. The "if" direction, that every other $n$ is representable, is the hard half and needs the theory of ternary quadratic forms; it is quoted, not proved here. Note the asymmetry: for two squares the criterion (Theorem 7.4.1) is proved in both directions in this chapter, whereas for three squares only the obstruction is elementary. For four squares there is no obstruction at all (Theorem 7.4.6).

