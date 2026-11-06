# Boolean Algebra — Solutions

> [Boolean Algebra](README.md) · Solutions to the 36 problems in [exercises.md](exercises.md)

Each solution states the strategy, carries out every step and checks the result — by truth table, by evaluation on all assignments, or against the axioms. Theorem numbers refer to the tutorial.

## Beginner

**1.** *Strategy: evaluate the two subexpressions column by column.*

| $x$ | $y$ | $z$ | $x \lor y$ | $\bar z$ | $f$ | |
|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 1 | 0 | |
| 0 | 0 | 1 | 0 | 0 | 0 | |
| 0 | 1 | 0 | 1 | 1 | 1 | $m_2$ |
| 0 | 1 | 1 | 1 | 0 | 0 | |
| 1 | 0 | 0 | 1 | 1 | 1 | $m_4$ |
| 1 | 0 | 1 | 1 | 0 | 0 | |
| 1 | 1 | 0 | 1 | 1 | 1 | $m_6$ |
| 1 | 1 | 1 | 1 | 0 | 0 | |

The true rows are $2, 4, 6$, so $f = \Sigma m(2,4,6)$, and the canonical DNF is
$$f = \bar x y \bar z \lor x \bar y \bar z \lor x y \bar z = (\bar x y \lor x\bar y \lor xy)\bar z = (x \lor y)\bar z,$$
using the identity $\bar x y \lor x \bar y \lor xy = x \lor y$ (Exercise 16).

**2.** *Strategy: XOR is associative, and its value is the parity of the number of ones.*

| $x$ | $y$ | $z$ | $x \oplus y$ | $f = (x \oplus y) \oplus z$ |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 0 | 1 |
| 0 | 1 | 0 | 1 | 1 |
| 0 | 1 | 1 | 1 | 0 |
| 1 | 0 | 0 | 1 | 1 |
| 1 | 0 | 1 | 1 | 0 |
| 1 | 1 | 0 | 0 | 0 |
| 1 | 1 | 1 | 0 | 1 |

The function is true exactly when the number of $1$s among $x,y,z$ is odd: four rows ($1, 2, 4, 7$). In words, it is the *parity* (or three-input XOR) of the variables.

**3.** *Strategy: match each equality to the axiom or derived law that licenses it.*

* $(x \land x) \lor (x \land y)$ from $x \land (x \lor y)$: distributivity of $\land$ over $\lor$ (B3), read right to left.
* $x \lor (x \land y)$ from $(x \land x) \lor (x \land y)$: idempotence of $\land$.
* $(x \land 1) \lor (x \land y)$ from $x \lor (x \land y)$: identity $x \land 1 = x$ (B4).
* $x \land (1 \lor y)$ from $(x \land 1) \lor (x \land y)$: distributivity (B3), right to left.
* $x \land 1$ from $x \land (1 \lor y)$: domination $1 \lor y = 1$.
* $x$ from $x \land 1$: identity (B4).

The chain is a proof of the absorption law; every step replaces a subexpression by an equal one, so equality is preserved.

**4.** *Strategy: use the complement axiom to create a $1$, then distribute.*

$$\begin{aligned}
x \land x &= (x \land x) \lor 0 && \text{(identity)}\\
&= (x \land x) \lor (x \land \neg x) && \text{(complement)}\\
&= x \land (x \lor \neg x) && \text{(distributivity, right to left)}\\
&= x \land 1 && \text{(complement)}\\
&= x && \text{(identity).}
\end{aligned}$$

No absorption is used, so the proof is not circular.

**5.** *Strategy: exhibit $x \land 0$ as a complement of something, or compute directly.*

$$\begin{aligned}
x \land 0 &= x \land (x \land \neg x) && \text{(complement)}\\
&= (x \land x) \land \neg x && \text{(associativity)}\\
&= x \land \neg x && \text{(idempotence, Exercise 4)}\\
&= 0 && \text{(complement).}
\end{aligned}$$

**6.** *Strategy: one De Morgan step at a time, outermost first.*

$$\neg(x \land \neg y \land z) = \neg x \lor \neg\neg y \lor \neg z = \neg x \lor y \lor \neg z.$$

The first step uses the generalised De Morgan law for $\land$ with three factors, the second uses involution $\neg\neg y = y$.

**7.** *Strategy: read the true rows $1, 2, 5, 7$ off the binary indices.*

$1 = 001$, $2 = 010$, $5 = 101$, $7 = 111$, so

$$f = \bar x\bar y z \lor \bar x y \bar z \lor x \bar y z \lor xyz.$$

Check row $5$: the third minterm is $x\bar y z = 1\cdot1\cdot1 = 1$ ✓. Check row $3$ ($011$): no minterm matches ($\bar x\bar y z$ needs $y=0$, $\bar x y\bar z$ needs $z=0$), so $f = 0$ ✓.

**8.** *Strategy: the maxterms correspond to the false rows, which are $0, 3, 4, 6$.*

$$f = (x \lor y \lor z)(x \lor \bar y \lor \bar z)(\bar x \lor y \lor z)(\bar x \lor \bar y \lor z).$$

Check row $3$ ($011$): the second clause is $x \lor \bar y \lor \bar z = 0 \lor 0 \lor 0 = 0$, so the product is $0$ ✓. Check row $0$ ($000$): the first clause is $0 \lor 0 \lor 0 = 0$ ✓. Check row $1$ ($001$): first clause $0\lor0\lor1 = 1$, second $0\lor1\lor0 = 1$, third $1\lor0\lor1 = 1$, fourth $1\lor1\lor1 = 1$, so $f = 1$ ✓.

**9.** *Strategy: list the true rows for the DNF and the false rows for the CNF.*

$x \oplus y$ is true at $01$ and $10$, so

$$x \oplus y = \bar x y \lor x \bar y \quad \text{(DNF)},$$
$$x \oplus y = (x \lor y)(\bar x \lor \bar y) \quad \text{(CNF)},$$

the second from the false rows $00$ and $11$. Check the CNF at $01$: $(0\lor1)(1\lor0) = 1$ ✓; at $11$: $(1)(0) = 0$ ✓; at $00$: $(0)(1) = 0$ ✓.

**10.** *Strategy: a function is a truth-table column, so count columns.*

A Boolean function of $n$ variables is determined by the $2^n$ entries of its truth table, and each entry can be $0$ or $1$. Hence there are $2^{2^n}$ functions. For $n = 3$: $2^{2^3} = 2^8 = 256$. For $n = 4$: $2^{2^4} = 2^{16} = 65\,536$.

**11.** *Strategy: transcribe the DNF into a two-level circuit.*

$f = x\bar y \lor z$ needs an inverter for $y$, an AND for $x\bar y$, and an OR combining that product with $z$:

```
t = NOT(y)
u = AND(x, t)
f = OR(u, z)
```

Three gates (one NOT, one AND, one 2-input OR), and depth three: the signal for $y$ passes through NOT, then AND, then OR. In a NAND-only process the same function costs three NAND gates (Exercise 21 is the analogous case $x \lor yz$).

**12.** *Strategy: find an invariant preserved by $\land$ and $\lor$ but not by negation.*

No. Every function expressible from $\land$ and $\lor$ is monotone: if $a \le b$ componentwise then $f(a) \le f(b)$ (Theorem 7.8). The negation satisfies $\neg 0 = 1 > 0 = \neg 1$, so it is not monotone and cannot be expressed.

## Intermediate

**13.** *Strategy: truth table first, then the algebraic chain.*

*(a) Truth table.*

| $x$ | $y$ | $x \land y$ | $x \lor (x \land y)$ | $x$ |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 0 | 0 |
| 1 | 0 | 0 | 1 | 1 |
| 1 | 1 | 1 | 1 | 1 |

The fourth and fifth columns agree ✓.

*(b) Algebra:*
$$\begin{aligned}
x \lor (x \land y) &= (x \land 1) \lor (x \land y) && \text{(identity)}\\
&= x \land (1 \lor y) && \text{(distributivity)}\\
&= x \land 1 && (1 \lor y = 1)\\
&= x && \text{(identity).}
\end{aligned}$$

**14.** *Strategy: evaluate both sides on all eight rows.*

With $f_1 = x \lor (y \land z)$ and $f_2 = (x \lor y) \land (x \lor z)$:

| $x$ | $y$ | $z$ | $y \land z$ | $f_1$ | $x \lor y$ | $x \lor z$ | $f_2$ |
|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 |
| 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 |
| 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 1 | 0 | 0 | 0 | 1 | 1 | 1 | 1 |
| 1 | 0 | 1 | 0 | 1 | 1 | 1 | 1 |
| 1 | 1 | 0 | 0 | 1 | 1 | 1 | 1 |
| 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |

Columns $f_1$ and $f_2$ agree on every row ✓. This is the distributive law that has no counterpart in ordinary arithmetic.

**15.** *Strategy: factor $\bar x$ out of the last two terms.*

$$\begin{aligned}
f &= x \lor \bar x y \lor \bar x \bar y \\
&= x \lor \bar x(y \lor \bar y) && \text{(distributivity)}\\
&= x \lor \bar x \cdot 1 && \text{(complement)}\\
&= x \lor \bar x && \text{(identity)}\\
&= 1 && \text{(complement).}
\end{aligned}$$

Check at $x = 0$: $0 \lor 1\cdot y \lor 1\cdot\bar y = y \lor \bar y = 1$ ✓; at $x = 1$ the first term alone is $1$ ✓.

**16.** *Strategy: group the two terms that share $y$, then absorb.*

$$\begin{aligned}
xy \lor \bar x y \lor x\bar y &= y(x \lor \bar x) \lor x\bar y && \text{(distributivity)}\\
&= y \cdot 1 \lor x\bar y && \text{(complement)}\\
&= y \lor x\bar y && \text{(identity)}\\
&= (y \lor x)(y \lor \bar y) && \text{(distributivity)}\\
&= x \lor y && \text{(complement, identity).}
\end{aligned}$$

Verification: $(0,0) \to 0$ and $x \lor y = 0$ ✓; $(0,1) \to 1$ ✓; $(1,0) \to 1$ ✓; $(1,1) \to 1$ ✓.

**17.** *Strategy: multiply out, then remove the consensus term.*

$$\begin{aligned}
(x \lor y)(\bar x \lor z) &= x\bar x \lor xz \lor \bar x y \lor yz && \text{(distributivity)}\\
&= 0 \lor xz \lor \bar x y \lor yz && (x\bar x = 0)\\
&= xz \lor \bar x y \lor yz && \text{(identity)}\\
&= xz \lor \bar x y && \text{(consensus).}
\end{aligned}$$

Check row $011$ (which is $x=0,y=1,z=1$): original $(0\lor1)(1\lor1) = 1$; simplified $\bar x y = 1$ ✓. Row $110$: original $(1\lor1)(0\lor0) = 0$; simplified $xz = 0$ and $\bar x y = 0$ ✓.

**18.** *Strategy: look for the variable that is constant on all true rows.*

The minterms $0, 2, 4, 6$ are $ABCD = 0000, 0010, 0100, 0110$. In all four, $A = 0$ and $D = 0$, while $B$ and $C$ take all four combinations: the true rows are exactly $\{A = 0,\ D = 0\}$.

The K-map confirms it: columns $CD = 00$ and $10$ of rows $AB = 00$ and $01$ are all $1$, forming the group of four cells with $A = 0$ and $D = 0$. Hence

$$f = \bar A \bar D.$$

Check $m_2$ ($0010$): $\bar A = 1$, $\bar D = 1$ ✓. Check $m_{12}$ ($1100$): $\bar A = 0$ ✗ and it is not in the list ✓.

**19.** *Strategy: list the ones on the map and test every possible group of four.*

The ones are $m_0, m_1, m_2, m_5, m_6, m_7$, displayed with rows $x$ and columns $yz$:

| $x \backslash yz$ | 00 | 01 | 11 | 10 |
|---|---|---|---|---|
| 0 | 1 | 1 | 0 | 1 |
| 1 | 0 | 1 | 1 | 1 |

No group of four exists. A group of four would be one full row (row $0$ has a $0$ at column $11$; row $1$ has a $0$ at column $00$) or one full column (column $00$ is $1,0$; $01$ is $1,1$; $11$ is $0,1$; $10$ is $1,1$) or a two-by-two block (each of the four blocks contains a $0$: $\{m_0,m_1,m_4,m_5\}$ has $m_4=0$, $\{m_1,m_3,m_5,m_7\}$ has $m_3=0$, $\{m_3,m_2,m_7,m_6\}$ has $m_3=0$, and the wrap-around block $\{m_2,m_0,m_6,m_4\}$ has $m_4=0$).

So every group has size at most two, and six ones require at least three groups. A cover with three groups is

$$\{m_0,m_1\} \to \bar x\bar y, \qquad \{m_2,m_6\} \to y\bar z, \qquad \{m_5,m_7\} \to xz,$$

so $f = \bar x\bar y \lor y\bar z \lor xz$.

*Verification.* $m_0$: $\bar x\bar y = 1$ ✓. $m_2$: $y\bar z = 1$ ✓. $m_5$: $xz = 1$ ✓. $m_6$: $y\bar z = 1$ ✓. $m_7$: $xz = 1$ ✓. Zeros: $m_3$ ($011$): $\bar x\bar y = 0$, $y\bar z = 0$, $xz = 0$ ✓; $m_4$ ($100$): all three $0$ ✓.

**20.** *Strategy: use the don't care to complete the column $z = 1$.*

Map with rows $x$ and columns $yz$:

| $x \backslash yz$ | 00 | 01 | 11 | 10 |
|---|---|---|---|---|
| 0 | 0 | 1 | X | 0 |
| 1 | 0 | 1 | 1 | X |

Treating $m_3$ as $1$ completes the four cells with $z = 1$: $m_1, m_3, m_5, m_7$. They form a group of four, giving

$$f = z.$$

*Verification on the care set.* $m_1$ ($001$): $z = 1$ ✓. $m_5$ ($101$): $z = 1$ ✓. $m_7$ ($111$): $z = 1$ ✓. Zeros: $m_0$ ($000$): $z = 0$ ✓; $m_2$ ($010$): $0$ ✓; $m_4$ ($100$): $0$ ✓. The don't cares receive $m_3 \to 1$ and $m_6 \to 0$, both permitted ✓.

Without the don't care, the ones $m_1, m_5, m_7$ would need the two terms $\bar y z$ and $xz$ (or similar), so the don't care saves an entire term.

**21.** *Strategy: express the OR as a NAND of two negations, then push the negation into the product.*

$$f = x \lor yz = \neg\bigl(\bar x \land \neg(yz)\bigr) = \mathrm{NAND}\bigl(\mathrm{NAND}(x,x),\ \mathrm{NAND}(y,z)\bigr).$$

Circuit:

```
g1 = NAND(x, x)    # ¬x
g2 = NAND(y, z)    # ¬(yz)
f  = NAND(g1, g2)  # x ∨ yz
```

Three gates, depth three.

| $x$ | $y$ | $z$ | $g_1$ | $g_2$ | $f$ | $x \lor yz$ |
|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 1 | 1 | 0 | 0 ✓ |
| 0 | 0 | 1 | 1 | 1 | 0 | 0 ✓ |
| 0 | 1 | 0 | 1 | 1 | 0 | 0 ✓ |
| 0 | 1 | 1 | 1 | 0 | 1 | 1 ✓ |
| 1 | 0 | 0 | 0 | 1 | 1 | 1 ✓ |
| 1 | 0 | 1 | 0 | 1 | 1 | 1 ✓ |
| 1 | 1 | 0 | 0 | 1 | 1 | 1 ✓ |
| 1 | 1 | 1 | 0 | 0 | 1 | 1 ✓ |

**22.** *Strategy: dualise every symbol and then check the claim on one awkward row.*

The dual of $xy \lor \bar x z \lor yz = xy \lor \bar x z$ is

$$(x \lor y)(\bar x \lor z)(y \lor z) = (x \lor y)(\bar x \lor z).$$

By the duality principle (Theorem 7.1) it is a theorem of every Boolean algebra, since the consensus identity is.

*Direct justification.* The left side is the right side multiplied by $(y \lor z)$. The extra factor is redundant: whenever $(x\lor y)(\bar x\lor z) = 1$ we cannot have $y = 0$ and $z = 0$ simultaneously, because then $(x \lor 0)(\bar x \lor 0) = x\bar x = 0$. Hence the product implies $y \lor z = 1$, and multiplying by a factor that is $1$ whenever the product is $1$ changes nothing.

Check the row $x = 0, y = 1, z = 0$: left side $(1)(1)(1) = 1$, right side $(1)(1) = 1$ ✓; row $x=0,y=0,z=0$: both sides $0$ ✓.

**23.** *Strategy: fill the two truth tables and compare columns.*

*Distributivity of $\land$ over $\oplus$:*

| $x$ | $y$ | $z$ | $y \oplus z$ | $x \land (y \oplus z)$ | $x \land y$ | $x \land z$ | $(x\land y) \oplus (x \land z)$ |
|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 |
| 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 1 | 0 | 1 | 1 | 1 | 0 | 1 | 1 |
| 1 | 1 | 0 | 1 | 1 | 1 | 0 | 1 |
| 1 | 1 | 1 | 0 | 0 | 1 | 1 | 0 |

The fifth and eighth columns agree ✓.

*Ring addition versus disjunction:*

| $x$ | $y$ | $x \oplus y$ | $x \land y$ | $x \oplus y \oplus (x\land y)$ | $x \lor y$ |
|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 0 ✓ |
| 0 | 1 | 1 | 0 | 1 | 1 ✓ |
| 1 | 0 | 1 | 0 | 1 | 1 ✓ |
| 1 | 1 | 0 | 1 | $0 + 1 = 1$ | 1 ✓ |

**24.** *Strategy: tabulate the selected input and read off the canonical forms.*

| $s$ | $a$ | $b$ | $z = \bar s a \lor s b$ |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 0 |
| 0 | 1 | 0 | 1 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 0 |
| 1 | 0 | 1 | 1 |
| 1 | 1 | 0 | 0 |
| 1 | 1 | 1 | 1 |

The ones are $m_2, m_3, m_5, m_7$. With the variable order $(s,a,b)$, $m_2 = \bar s a\bar b$, $m_3 = \bar s ab$, $m_5 = s\bar a b$, $m_7 = sab$, so

$$z = \bar s a\bar b \lor \bar s ab \lor s\bar a b \lor sab = \bar s a \lor sb,$$

which is the defining expression ✓.

*CNF.* The zeros are $m_0, m_1, m_4, m_6$, i.e. $(s,a,b) = 000, 001, 100, 110$. The minimal cover by zeros pairs $m_0, m_1$ (differ in $b$) giving $(s \lor a)$, and $m_4, m_6$ (differ in $a$) giving $(\bar s \lor b)$. Hence

$$z = (s \lor a)(\bar s \lor b).$$

Check $s=0,a=0$: $(0)(1) = 0$, and the multiplexer outputs $a = 0$ ✓. Check $s=1,b=1$: $(1)(1) = 1$, output $b = 1$ ✓. Check $s=1,b=0$: $(1)(0) = 0$ ✓.

*Interpretation.* When $s = 0$ the first factor $s \lor a = a$ decides, and the second factor is $1$; when $s = 1$ the second factor $\bar s \lor b = b$ decides. The circuit therefore outputs $a$ when $s = 0$ and $b$ when $s = 1$ — "if $s$ then $b$ else $a$".

## Advanced

**25.** *Strategy: prove each statement by showing that a candidate satisfies the two complement axioms, then invoke uniqueness.*

*$\neg 0 = 1$.* Check that $1$ is a complement of $0$:
$$0 \lor 1 = 1 \quad\text{(identity with } x = 1\text{)}, \qquad 0 \land 1 = 0 \quad\text{(identity with } x = 0\text{)}.$$
So $1$ satisfies $0 \lor a = 1$ and $0 \land a = 0$ with $a = 1$, and by Theorem 8.1 the complement is unique. Hence $\neg 0 = 1$.

*$\neg 1 = 0$.* Similarly $1 \lor 0 = 1$ and $1 \land 0 = 0$, so $0$ is a complement of $1$, hence $\neg 1 = 0$.

*Order reversal.* Recall that $x \le y$ means $x \land y = x$, equivalently $x \lor y = y$ (the two are equivalent in a lattice). Assume $x \le y$, so $x \lor y = y$. Then by De Morgan
$$\bar y \land \bar x = \neg(y \lor x) = \neg(x \lor y) = \neg y = \bar y.$$
Hence $\bar y \land \bar x = \bar y$, which is exactly $\bar y \le \bar x$ ✓.

*Check on $B_2$.* $0 \le 1$ and $\bar 1 = 0 \le 1 = \bar 0$ ✓.

**26.** *Strategy: evaluate the proposed product at an arbitrary assignment, using the defining property of maxterms.*

*Statement.* For an $n$-ary function $f$ with assignment $a_j$ of binary value $j$ and maxterm $M_j$ (false only at $a_j$),
$$f = \bigwedge_{j\,:\,f(a_j)=0} M_j.$$

*Proof.* Fix an assignment $a_k$. A maxterm $M_j$ evaluates to $1$ at $a_k$ whenever $j \ne k$, because $M_j$ is false only at $a_j$. The only factor that can vanish at $a_k$ is $M_k$, and it does vanish there. Therefore the conjunction evaluates to $0$ if $k$ belongs to the index set $\{j : f(a_j) = 0\}$ and to $1$ otherwise. That is exactly $f(a_k)$ in both cases. Since $k$ was arbitrary, the two functions agree on every assignment. $\blacksquare$

*Uniqueness.* Suppose $f = \bigwedge_{j \in S} M_j$ with $S \subseteq \{0,\dots,2^n-1\}$ and distinct maxterms. Evaluating at $a_k$ gives $f(a_k) = 0 \iff k \in S$, because the other factors are $1$ and $M_k = 0$. Hence $S = \{j : f(a_j) = 0\}$ is determined by $f$. $\blacksquare$

*Consistency check with duality.* The dual of the minterm statement (Theorem 7.3) is exactly this theorem; the direct proof confirms that duality is not being used circularly.

**27.** *Strategy: express the complete set $\{\neg, \lor, \land\}$ using only $\Rightarrow$ and the constant $0$.*

Recall $x \Rightarrow y = \neg x \lor y$.

* Negation: $x \Rightarrow 0 = \neg x \lor 0 = \neg x$.
* Disjunction: using negation just derived,
$$x \lor y = \neg\neg x \lor y = \neg x \Rightarrow y = (x \Rightarrow 0) \Rightarrow y.$$
* Conjunction: by De Morgan and the two rules above,
$$x \land y = \neg(\neg x \lor \neg y) = \neg\bigl((x \Rightarrow 0) \Rightarrow (y \Rightarrow 0)\bigr) = \bigl((x \Rightarrow 0) \Rightarrow (y \Rightarrow 0)\bigr) \Rightarrow 0.$$

Since $\neg$, $\lor$ and $\land$ are definable, every formula of propositional logic is definable, so $\{\Rightarrow, 0\}$ is complete. $\blacksquare$

*Check at $x = y = 0$:* $x \Rightarrow 0 = 1$, $y \Rightarrow 0 = 1$, $1 \Rightarrow 1 = 1$, $1 \Rightarrow 0 = 0 = x \land y$ ✓.

**28.** *Strategy: obtain negation, then disjunction; conjunction is already available.*

* Negation: $x \oplus 1 = (x \land \neg 1) \lor (\neg x \land 1) = \neg x$, so $\neg x = x \oplus 1$.
* Disjunction: by Theorem 7.11, in the Boolean ring with addition $\oplus$,
$$x \lor y = x \oplus y \oplus (x \land y).$$
* Conjunction is the connective $\land$ itself.

Hence $\{\neg, \lor, \land\}$ is definable, and that set is complete by Theorem 7.5. Therefore $\{\oplus, \land, 1\}$ is complete. $\blacksquare$

*Check at $x = y = 1$:* $1 \oplus 1 \oplus (1 \land 1) = 0 \oplus 1 = 1$ ✓.

**29.** *Strategy: show that a non-prime product can always be shortened without changing the function.*

*Definitions.* A product $P$ (a conjunction of literals) *implies* $f$ if every assignment satisfying $P$ satisfies $f$. It is a *prime implicant* of $f$ if it implies $f$ and deleting any literal from $P$ produces a product that no longer implies $f$.

*Claim.* Every minimal sum-of-products expression for $f$ consists of prime implicants.

*Proof.* Let $P_1 \lor \cdots \lor P_m$ be a minimal expression (minimal in the number of literals, so no term can be shortened and no term can be deleted). Fix a term $P_i$ and suppose it is not prime. Then some literal $\ell$ of $P_i$ can be deleted, producing a shorter product $P_i'$ that still implies $f$. Since $P_i$ implies $P_i'$ (removing a conjunct weakens the product), we have
$$f = P_1 \lor \cdots \lor P_i \lor \cdots \lor P_m \;\le\; P_1 \lor \cdots \lor P_i' \lor \cdots \lor P_m \;\le\; f,$$
because $P_i'$ implies $f$ and each $P_j$ implies $f$. Hence all three expressions are equal, and replacing $P_i$ by $P_i'$ gives an expression for $f$ with strictly fewer literals — contradicting minimality. So each $P_i$ is prime. $\blacksquare$

*Why minimisation is still hard.* The theorem reduces the search to prime implicants, but a function can have exponentially many of them, and choosing a smallest subset that covers all true rows is the **set-cover problem**, which is $\mathrm{NP}$-hard. A K-map is a visual device that works for at most five or six variables because it makes adjacency visible; beyond that one uses heuristics or exact algorithms such as Quine–McCluskey, which is exponential in the worst case.

**30.** *Strategy: prove the redundancy algebraically, then interpret the extra factor as a hazard fix.*

*Proof.* Let $L = (x \lor y)(\bar x \lor z)$. We show $L(y \lor z) = L$ by showing $L \le y \lor z$. If $L = 1$ then both factors are $1$; were $y = z = 0$, the factors would be $x$ and $\bar x$, whose product is $0$, a contradiction. Hence $L = 1$ forces $y \lor z = 1$, i.e. $L \le y \lor z$. Multiplying by a factor that is $1$ whenever $L$ is $1$ leaves $L$ unchanged:
$$L(y \lor z) = L.$$
Expanding the left side gives the dual consensus identity. $\blacksquare$

*Hazard interpretation.* With $y = z = 0$ the circuit computes $x \cdot \bar x$, which is $0$ for both values of $x$. If $x$ rises from $0$ to $1$ while the inverter has not yet responded, both factors are momentarily $1$ and the output glitches to $1$ — a **static-0 hazard**. The extra factor $y \lor z$ equals $0$ throughout this transition, so including it holds the output at $0$ and removes the glitch.

*Check.* At $x=0,y=1,z=1$: $L = (1)(1)(1) = 1$; at $x=0,y=0,z=0$: $L = (0)(1)(0) = 0$ ✓.

**31.** *Strategy: map each divisor to the set of primes that divide it.*

The divisors of $30 = 2\cdot3\cdot5$ are
$$1,\ 2,\ 3,\ 5,\ 6,\ 10,\ 15,\ 30.$$
Map $d$ to $S(d) = \{p \in \{2,3,5\} : p \mid d\}$:

| $d$ | 1 | 2 | 3 | 5 | 6 | 10 | 15 | 30 |
|---|---|---|---|---|---|---|---|---|
| $S(d)$ | $\varnothing$ | $\{2\}$ | $\{3\}$ | $\{5\}$ | $\{2,3\}$ | $\{2,5\}$ | $\{3,5\}$ | $\{2,3,5\}$ |

This is a bijection onto $\mathcal{P}(\{2,3,5\})$, and under it
$$\operatorname{lcm}(d,e) \leftrightarrow S(d) \cup S(e), \qquad \gcd(d,e) \leftrightarrow S(d) \cap S(e), \qquad \frac{30}{d} \leftrightarrow \{2,3,5\} \setminus S(d).$$
Check: $\operatorname{lcm}(6,10) = 30 \leftrightarrow \{2,3\} \cup \{2,5\} = \{2,3,5\}$ ✓; $\gcd(6,10) = 2 \leftrightarrow \{2,3\}\cap\{2,5\} = \{2\}$ ✓; $30/6 = 5 \leftrightarrow \{5\}$ ✓.

The algebra has $2^3 = 8$ elements, one per subset, and the atoms are $2, 3, 5$ — exactly the primes. A Boolean algebra with five atoms has $2^5 = 32$ elements (Theorem 8.6).

**32.** *Strategy: compute both parenthesisations on the same arguments.*

$$(1 \uparrow 1) \uparrow 0 = \neg(1\land1) \uparrow 0 = 0 \uparrow 0 = \neg(0 \land 0) = 1,$$
$$1 \uparrow (1 \uparrow 0) = 1 \uparrow \neg(1 \land 0) = 1 \uparrow 1 = \neg(1\land1) = 0.$$

The values differ, so $\uparrow$ is not associative.

*Which functions are computed.* Using $x \uparrow y = \neg(xy)$:
$$(x \uparrow y) \uparrow z = \neg\bigl(\neg(xy)\cdot z\bigr) = xy \lor \bar z, \qquad x \uparrow (y \uparrow z) = \neg\bigl(x \cdot \neg(yz)\bigr) = \bar x \lor yz.$$
These are different functions — for instance at $x=0,y=0,z=0$ the first is $0 \lor 1 = 1$ and the second is $1 \lor 0 = 1$; at $x=1,y=0,z=0$ the first is $0 \lor 1 = 1$ and the second is $0 \lor 0 = 0$ ✓, confirming they differ.

## Challenge

**33.** *Strategy: tabulate all sixteen connectives and attach to each a property that its clone preserves.*

A set contained in one of Post's five clones cannot be complete: if every generator preserves a property and the property is preserved by composition, then every expressible function preserves it, while some function (for example $\neg$) does not. The five properties and their closures are:

* $T_0$: $f(0,\dots,0) = 0$; the variables and constant $0$ are in $T_0$, and $f \circ g$ is in $T_0$ when $f, g$ are.
* $T_1$: $f(1,\dots,1) = 1$; same closure argument.
* $M$: monotone; the composition of monotone functions is monotone.
* $D$: self-dual, $f(\bar x) = \overline{f(x)}$; self-dual functions compose to self-dual functions.
* $L$: affine over $\mathbb{F}_2$, that is $f = c_0 \oplus c_1x_1 \oplus \cdots \oplus c_nx_n$; affine functions compose to affine functions.

For two variables, write the four values as $(f(0,0), f(0,1), f(1,0), f(1,1))$:

| Function | Values | Preserved property |
|---|---|---|
| $0$ | 0000 | $T_0$, $M$, $L$ |
| $x \land y$ | 0001 | $T_0$, $T_1$, $M$ |
| $x \land \bar y$ | 0010 | $T_0$ |
| $x$ | 0011 | $T_0$, $T_1$, $M$, $D$, $L$ |
| $\bar x \land y$ | 0100 | $T_0$ |
| $y$ | 0101 | $T_0$, $T_1$, $M$, $D$, $L$ |
| $x \oplus y$ | 0110 | $T_0$, $L$ |
| $x \lor y$ | 0111 | $T_0$, $T_1$, $M$ |
| $x \downarrow y$ | 1000 | **none** |
| $x \odot y$ | 1001 | $T_1$, $L$ |
| $\bar y$ | 1010 | $T_1$, $D$, $L$ |
| $y \Rightarrow x$ | 1011 | $T_1$ |
| $\bar x$ | 1100 | $T_1$, $D$, $L$ |
| $x \Rightarrow y$ | 1101 | $T_1$ |
| $x \uparrow y$ | 1110 | **none** |
| $1$ | 1111 | $T_1$, $M$, $L$ |

Each of the fourteen rows other than the two marked **none** exhibits a property, so the corresponding singleton set is contained in a maximal clone and cannot be complete. The two remaining functions pass all five tests and are indeed complete (Theorem 7.6 and its dual). This is precisely Post's theorem in action: completeness fails exactly when all five properties are avoided.

*Spot checks of the table.* $x \land \bar y$ has $f(0,0) = 0$, so it is in $T_0$; it is not monotone since $f(1,0) = 1 > f(1,1) = 0$. $x \odot y$ has $f(1,1) = 1$, so it is in $T_1$, and it is affine because $x \odot y = 1 \oplus x \oplus y$. NAND has $f(0,0) = 1$ (not $T_0$), $f(1,1) = 0$ (not $T_1$), and is neither monotone, self-dual nor affine.

**34.** *Strategy: one direction is structural induction; the other builds a negation-free DNF.*

*(⇒) Monotone implies negation-free.* Let $f$ be monotone. For each assignment $a$ with $f(a) = 1$ define the **positive product**
$$p_a = \bigwedge_{i\,:\,a_i = 1} x_i,$$
the conjunction of the variables that $a$ sets to $1$ (if $a$ is the all-zero assignment, $p_a$ is the empty conjunction, i.e. the constant $1$). We claim

$$f = \bigvee_{a\,:\,f(a)=1} p_a.$$

*Every $p_a$ implies $f$.* The product $p_a$ is true exactly on the assignments $b$ with $b \ge a$ componentwise. Since $f$ is monotone and $f(a) = 1$, such a $b$ satisfies $f(b) \ge f(a) = 1$. Hence $p_a \le f$.

*Every true assignment is covered.* If $f(b) = 1$, then $p_b(b) = 1$ because all conjuncts $b_i = 1$ are satisfied. Hence the disjunction is $1$ at $b$.

Therefore the disjunction equals $f$, and it uses only variables, $\land$, $\lor$ and the constant $1$ — no negation.

*(⇐) Negation-free implies monotone.* Induct on the formula. Variables and constants are monotone. If $g$ and $h$ are monotone, then so are $g \land h$ and $g \lor h$: if $a \le b$ then $g(a) \le g(b)$ and $h(a) \le h(b)$, so both the minimum and the maximum of the pair are monotone in $a$. Hence every formula built from variables, $\land$, $\lor$ and constants is monotone. $\blacksquare$

*Example.* For $f = xy \lor yz \lor xz$ (majority), the construction gives $p_{011} = yz$, $p_{101} = xz$, $p_{110} = xy$, $p_{111} = xyz$; the last is absorbed, recovering $xy \lor xz \lor yz$ ✓.

**35.** *Strategy: existence by induction on the number of variables (Shannon expansion over $\mathbb{F}_2$), uniqueness by counting.*

*Existence.* Every function of $n$ variables can be expanded in its last variable:
$$f(x_1,\dots,x_n) = (1 + x_n)\,f_0(x_1,\dots,x_{n-1}) + x_n\,f_1(x_1,\dots,x_{n-1}) \pmod 2,$$
where $f_0 = f(x_1,\dots,x_{n-1},0)$ and $f_1 = f(x_1,\dots,x_{n-1},1)$. This is the Shannon expansion translated into $\mathbb{F}_2$, using $1 + x_n = \bar x_n$. By induction $f_0$ and $f_1$ have multilinear polynomials, and multiplying either by $(1 + x_n)$ or by $x_n$ preserves multilinearity. Hence $f$ has a multilinear polynomial
$$f(x) = \sum_{S \subseteq \{1,\dots,n\}} c_S \prod_{i \in S} x_i, \qquad c_S \in \mathbb{F}_2.$$

*Uniqueness by counting.* A multilinear polynomial is determined by its $2^n$ coefficients $c_S$, so there are at most $2^{2^n}$ of them. By Theorem 8.5 there are exactly $2^{2^n}$ Boolean functions. Existence shows that the map from coefficient vectors to functions is surjective; a surjection between finite sets of the same size is a bijection, so distinct coefficient vectors give distinct functions. $\blacksquare$

*Computations.* In $\mathbb{F}_2$, subtraction and addition coincide, and $x_i^2 = x_i$:

* $x \oplus y = x + y$ (already multilinear, coefficients $c_{\{1\}} = c_{\{2\}} = 1$);
* $x \land y = xy$;
* $x \lor y = x + y + xy$ (Theorem 7.11).

The last identity is the reason the algebraic normal form of OR has degree $2$, while XOR has degree $1$. The degree of the ANF is a measure of algebraic complexity: it is $1$ exactly for affine functions, which is the property $L$ of Exercise 33.

**36.** *Strategy: show that no proper product can appear in a DNF for parity.*

Let $\varphi$ be a DNF computing $f = x_1 \oplus \cdots \oplus x_n$. Each term of $\varphi$ is a conjunction of literals; if it contains both $x_i$ and $\bar x_i$ it is identically $0$ and may be deleted. Otherwise let $k$ be the number of distinct variables occurring in the term. The term is true exactly on the subcube of assignments that agree with its literals on those $k$ variables — a subcube of dimension $n - k$.

*Claim: every non-zero term has $k = n$.* If $k < n$, the subcube has dimension at least $1$, so it contains two assignments $a, b$ differing in exactly one free variable. Parity changes when a single bit changes, so $f(a) \ne f(b)$. But the term is true at both $a$ and $b$, so $\varphi$ (an OR of terms) is true at both — contradicting that $\varphi$ computes the parity function. Hence $k = n$ for every term that can contribute, i.e. every term is a full minterm.

*Counting.* A DNF for parity must therefore be a disjunction of minterms. It must be true at each of the $2^{n-1}$ assignments with an odd number of $1$s, and a minterm is true at exactly one assignment; so at least $2^{n-1}$ distinct minterms are needed. The canonical DNF, which has exactly one minterm per odd assignment, attains this bound. $\blacksquare$

*Consequence.* The minimal DNF size of parity is exactly $2^{n-1}$, exponential in $n$, even though parity can be computed by a chain of $n-1$ XOR gates. DNF size is therefore a poor measure of circuit complexity, and this gap is the starting point of circuit complexity theory.

