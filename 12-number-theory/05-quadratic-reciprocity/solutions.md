# Quadratic Residues and Reciprocity — Solutions

> [Quadratic Residues and Reciprocity](README.md) · Solutions to the 36 problems in [exercises.md](exercises.md)

Every solution names the strategy and the theorem used, and displays the reciprocity steps. Numerical answers are checked by a second method where one is available. Section references point into the [tutorial](README.md).

## Beginner

**1.** *Strategy: square $1,\dots,11$; the pairs $x$ and $23-x$ give the same square.*

$$
\begin{aligned}
1^2&=1, & 2^2&=4, & 3^2&=9, & 4^2&=16,\\
5^2&=25\equiv2, & 6^2&=36\equiv13, & 7^2&=49\equiv3, & 8^2&=64\equiv18,\\
9^2&=81\equiv12, & 10^2&=100\equiv8, & 11^2&=121\equiv6.
\end{aligned}
$$

Thus

$$
\operatorname{QR}_{23}=\{1,2,3,4,6,8,9,12,13,16,18\},
$$

with $11=(23-1)/2$ elements, and

$$
\operatorname{QNR}_{23}=\{5,7,10,11,14,15,17,19,20,21,22\}.
$$

Each residue has exactly two roots, $x$ and $23-x$: for example, $2$ has roots $5$ and $18$, since $5^2\equiv2$ and $18^2\equiv2$.

**2.** *Strategy: list the nonzero squares modulo each prime.*

(a) Squares modulo $7$: $1,4,2$. Since $3$ is not in the list, $\left(\frac{3}{7}\right)=-1$.

(b) Squares modulo $11$: $1,3,4,5,9$. Since $5$ is in the list, $\left(\frac{5}{11}\right)=1$.

(c) Squares modulo $13$: $1,3,4,9,10,12$. Since $2$ is not in the list, $\left(\frac{2}{13}\right)=-1$.

(d) Squares modulo $7$: $1,4,2$. Since $6$ is not in the list, $\left(\frac{6}{7}\right)=-1$.

(e) $(-1)^2=1\equiv-1\pmod5$? More directly, $-1\equiv4=2^2\pmod5$, so $\left(\frac{-1}{5}\right)=1$.

(f) Squares modulo $7$ do not include $6\equiv-1$, so $\left(\frac{-1}{7}\right)=-1$. This agrees with $7\equiv3\pmod4$.

**3.** *Strategy: Euler's criterion, computing the power by repeated squaring.*

(a) $2^8$: $2^2=4$, $2^4=16\equiv-1$, $2^8\equiv1$. Hence $\left(\frac{2}{17}\right)=1$. Check: $6^2=36\equiv2$.

(b) $3^8$: $3^2=9$, $3^4=81\equiv13$, $3^8\equiv13^2=169\equiv16\equiv-1$. Hence $\left(\frac{3}{17}\right)=-1$.

(c) $5^8$: $5^2=25\equiv8$, $5^4\equiv8^2=64\equiv13$, $5^8\equiv13^2=169\equiv16\equiv-1$. Hence $\left(\frac{5}{17}\right)=-1$.

The squares modulo $17$ are $1,4,9,16,8,2,15,13$; indeed $2$ is present, while $3$ and $5$ are not.

**4.** *Strategy: the first supplementary law depends on $p\bmod4$; the second on $p\bmod8$.*

| $p$ | $p\bmod4$ | $p\bmod8$ | $\left(\frac{-1}{p}\right)$ | $\left(\frac{2}{p}\right)$ |
|---|---|---|---|---|
| $7$ | $3$ | $7$ | $-1$ | $1$ |
| $13$ | $1$ | $5$ | $1$ | $-1$ |
| $17$ | $1$ | $1$ | $1$ | $1$ |
| $29$ | $1$ | $5$ | $1$ | $-1$ |

For example, $\left(\frac{-1}{13}\right)=1$ because $13\equiv1\pmod4$, and $5^2=25\equiv-1\pmod{13}$. Also $\left(\frac{2}{7}\right)=1$ because $7\equiv7\pmod8$, and $3^2=9\equiv2\pmod7$.

**5.** *Strategy: multiplicativity and the values from Problem 2.*

(a) $\left(\frac{6}{13}\right)=\left(\frac{2}{13}\right)\left(\frac{3}{13}\right)=(-1)(1)=-1$.

(b) $\left(\frac{10}{13}\right)=\left(\frac{2}{13}\right)\left(\frac{5}{13}\right)=(-1)(-1)=1$.

The squares modulo $13$ are $1,3,4,9,10,12$; $6$ is absent and $10$ is present, confirming both answers.

**6.** *Strategy: list the residues, sum them, and compare with the total sum of all nonzero classes.*

Modulo $19$, the residues are $1,4,5,6,7,9,11,16,17$, whose sum is

$$
1+4+5+6+7+9+11+16+17=76=4\cdot19.
$$

The sum of all nonzero classes is $1+\cdots+18=171=9\cdot19$, so the non-residues sum to $171-76=95=5\cdot19$.

Modulo $23$, the residues are $1,2,3,4,6,8,9,12,13,16,18$, whose sum is

$$
1+2+3+4+6+8+9+12+13+16+18=92=4\cdot23.
$$

The total is $1+\cdots+22=253=11\cdot23$, so the non-residues sum to $253-92=161=7\cdot23$.

**7.** *Strategy: combine the conditions $p\equiv1\pmod4$ and $p\equiv\pm1\pmod8$.*

The condition $\left(\frac{-1}{p}\right)=1$ is $p\equiv1\pmod4$, and $\left(\frac{2}{p}\right)=1$ is $p\equiv1$ or $7\pmod8$. The common solution is

$$
p\equiv1\pmod8.
$$

The primes below $50$ congruent to $1$ modulo $8$ are $17$ and $41$. Check: $\left(\frac{-1}{17}\right)=\left(\frac{2}{17}\right)=1$, and $17\equiv1\pmod8$; similarly $41\equiv1\pmod8$.

**8.** *Strategy: solve by inspection or use the list of squares modulo $11$.*

(a) $x^2\equiv9\pmod{11}$: $3^2=9$ and $8^2=64\equiv9$, so $x\equiv3,8\pmod{11}$.

(b) $x^2\equiv0\pmod{11}$: $x\equiv0\pmod{11}$ only, since $11$ is prime.

(c) $x^2\equiv2\pmod{11}$: the squares modulo $11$ are $1,3,4,5,9$, so there is no solution.

**9.** *Strategy: find a square root of $-1$ modulo $13$; use the first supplementary law for $7$.*

Since $5^2=25\equiv-1\pmod{13}$, the solutions are $x\equiv5,8\pmod{13}$. For $p=7$, $7\equiv3\pmod4$, so $\left(\frac{-1}{7}\right)=-1$ and there is no solution; equivalently, the squares modulo $7$ are $1,2,4$, not $6$.

**10.** *Strategy: use the definition of the Jacobi symbol as a product of Legendre symbols.*

(a) $\left(\frac{2}{9}\right)=\left(\frac{2}{3}\right)^2=(-1)^2=1$.

(b) $\left(\frac{5}{9}\right)=\left(\frac{5}{3}\right)^2$. Since $5\equiv2\pmod3$ and $2$ is a non-residue modulo $3$, the factor is $(-1)^2=1$.

(c) $\left(\frac{7}{15}\right)=\left(\frac{7}{3}\right)\left(\frac{7}{5}\right)$. Now $7\equiv1\pmod3$, so the first factor is $1$; and $7\equiv2\pmod5$, which is a non-residue modulo $5$, so the second factor is $-1$. Thus the product is $-1$.

**11.** *Strategy: compute the Jacobi symbol and compare with the list of squares.*

$$
\left(\frac{2}{15}\right)=\left(\frac{2}{3}\right)\left(\frac{2}{5}\right)=(-1)(-1)=1.
$$

The squares modulo $15$ are $0,1,4,6,9,10$. The number $2$ is not among them, so it is not a square modulo $15$. This shows that a Jacobi symbol of $1$ is necessary but not sufficient for a square when the denominator is composite.

**12.** *Strategy: square all residues modulo $15$.*

The squares modulo $15$ are

$$
0^2=0,\quad1^2=1,\quad2^2=4,\quad3^2=9,\quad4^2=16\equiv1,\quad5^2=25\equiv10,
$$
$$
6^2=36\equiv6,\quad7^2=49\equiv4,\quad8^2=64\equiv4,\quad9^2=81\equiv6,\quad10^2=100\equiv10,
$$
and the remaining residues repeat by symmetry. Thus the distinct squares are

$$
\{0,1,4,6,9,10\},
$$

six in total. The prime formula $(p-1)/2$ counts nonzero squares in a field, where every nonzero element is either a square or a non-square and the squaring map is exactly two-to-one. For $n=15$, the ring $\mathbb{Z}/15\mathbb{Z}$ is not a field and has zero divisors, so the count is different. Excluding $0$, there are five nonzero squares, not $(15-1)/2=7$.

## Intermediate

**13.** *Strategy: Gauss's lemma: list $aj$, reduce to least positive residues, and count those exceeding $p/2$.*

For $p=13$, $(p-1)/2=6$.

(a) $a=3$: the residues of $3,6,9,12,15,18$ are $3,6,9,12,2,5$. Those exceeding $6.5$ are $9,12$, so $m=2$ and $\left(\frac{3}{13}\right)=1$.

(b) $a=5$: the residues of $5,10,15,20,25,30$ are $5,10,2,7,12,4$. Those exceeding $6.5$ are $10,7,12$, so $m=3$ and $\left(\frac{5}{13}\right)=-1$.

(c) $a=7$: the residues of $7,14,21,28,35,42$ are $7,1,8,2,9,3$. Those exceeding $6.5$ are $7,8,9$, so $m=3$ and $\left(\frac{7}{13}\right)=-1$.

The squares modulo $13$ are $1,3,4,9,10,12$; this confirms $3$ is a residue and $5,7$ are not.

**14.** *Strategy: apply reciprocity, then reduce the numerator modulo the new denominator.*

(a) $19\equiv3\pmod4$ and $29\equiv1\pmod4$, so the sign is $+$:

$$
\left(\frac{19}{29}\right)=\left(\frac{29}{19}\right)=\left(\frac{10}{19}\right).
$$

Now

$$
\left(\frac{10}{19}\right)=\left(\frac{2}{19}\right)\left(\frac{5}{19}\right).
$$

Since $19\equiv3\pmod8$, $\left(\frac{2}{19}\right)=-1$. Since $5\equiv1\pmod4$,
$\left(\frac{5}{19}\right)=\left(\frac{19}{5}\right)=\left(\frac{4}{5}\right)=1$.
Therefore $\left(\frac{19}{29}\right)=(-1)(1)=-1$.

(b) $31\equiv3\pmod4$ and $43\equiv3\pmod4$, so the sign is $-$:

$$
\left(\frac{31}{43}\right)=-\left(\frac{43}{31}\right)=-\left(\frac{12}{31}\right).
$$

Now

$$
\left(\frac{12}{31}\right)=\left(\frac{3}{31}\right)\left(\frac{4}{31}\right)=\left(\frac{3}{31}\right).
$$

Again $3\equiv3$ and $31\equiv3\pmod4$, so

$$
\left(\frac{3}{31}\right)=-\left(\frac{31}{3}\right)=-\left(\frac{1}{3}\right)=-1.
$$

Hence $\left(\frac{31}{43}\right)=-(-1)=1$.

**15.** *Strategy: factor the numerator, apply reciprocity to each prime factor, and use the supplementary law for $2$ if needed.*

$$
\left(\frac{77}{101}\right)=\left(\frac{7}{101}\right)\left(\frac{11}{101}\right).
$$

For $7$: $7\equiv3\pmod4$ and $101\equiv1\pmod4$, so no sign. Also $101\equiv3\pmod7$. Thus

$$
\left(\frac{7}{101}\right)=\left(\frac{101}{7}\right)=\left(\frac{3}{7}\right)=-1.
$$

For $11$: $11\equiv3\pmod4$ and $101\equiv1\pmod4$, so no sign. Also $101\equiv2\pmod{11}$. Thus

$$
\left(\frac{11}{101}\right)=\left(\frac{101}{11}\right)=\left(\frac{2}{11}\right)=-1,
$$

because $11\equiv3\pmod8$. Therefore $\left(\frac{77}{101}\right)=(-1)(-1)=1$. This is a Jacobi symbol of $1$; it does not by itself prove that $77$ is a square modulo $101$.

**16.** *Strategy: Tonelli-Shanks with $p=13$, $a=10$.*

Write $p-1=12=3\cdot2^2$, so $Q=3$ and $S=2$. The element $z=2$ is a non-residue modulo $13$ because $13\equiv5\pmod8$. Set

$$
c=z^Q=2^3=8,\qquad t=a^Q=10^3=1000\equiv-1\pmod{13},
$$
$$
R=a^{(Q+1)/2}=10^2=100\equiv9\pmod{13}.
$$

Since $t\not\equiv1$, find the least $i$ with $t^{2^i}\equiv1$: $t=-1$, so $i=1$. Then

$$
b=c^{2^{M-i-1}}=c^{2^{0}}=8,
$$
$$
M=1,\qquad c=b^2=64\equiv-1,\qquad t=tc\equiv(-1)(-1)=1,\qquad R=Rb=9\cdot8=72\equiv7.
$$

Now $t=1$, so the roots are $R$ and $-R$, namely $7$ and $6$ modulo $13$. Check:
$7^2=49\equiv10$ and $6^2=36\equiv10$.

**17.** *Strategy: list the squares of $1,\dots,8$; the other roots are their negatives.*

The squares modulo $17$ are

$$
1,4,9,16,8,2,15,13.
$$

Since $8$ occurs as $5^2$, the roots are $x\equiv5$ and $x\equiv17-5=12\pmod{17}$. Check: $5^2=25\equiv8$ and $12^2=144\equiv8$.

**18.** *Strategy: solve modulo $5$ and $7$, then combine all pairs with the Chinese remainder theorem.*

Modulo $5$: $x^2\equiv9\equiv4$, so $x\equiv\pm2$, i.e. $x\equiv2,3\pmod5$. Modulo $7$: $x^2\equiv9\equiv2$, and the squares modulo $7$ are $1,4,2$, so $x\equiv\pm3$, i.e. $x\equiv3,4\pmod7$.

Combine:

* $x\equiv2\pmod5$, $x\equiv3\pmod7$: $x=2+5k$, $2+5k\equiv3\pmod7$, $5k\equiv1\pmod7$, $k\equiv3\pmod7$, so $x\equiv17\pmod{35}$.
* $x\equiv2\pmod5$, $x\equiv4\pmod7$: $5k\equiv2\pmod7$, $k\equiv6\pmod7$, so $x\equiv32\pmod{35}$.
* $x\equiv3\pmod5$, $x\equiv3\pmod7$: $k\equiv0\pmod7$, so $x\equiv3\pmod{35}$.
* $x\equiv3\pmod5$, $x\equiv4\pmod7$: $5k\equiv1\pmod7$, $k\equiv3\pmod7$, so $x\equiv18\pmod{35}$.

The roots are $3,17,18,32$. The theory predicts $2^{\omega(35)}=2^2=4$ roots. Check: $3^2=9$, $17^2=289\equiv9$, $18^2=324\equiv9$, $32^2=1024\equiv9$ modulo $35$.

**19.** *Strategy: solve modulo $5$, then apply the Hensel lift formula.*

Modulo $5$, $x^2\equiv6\equiv1$, so the roots are $r\equiv1$ and $r\equiv4$.

For $r=1$: $(a-r^2)/5=(6-1)/5=1$, and $(2r)^{-1}=2^{-1}\equiv3\pmod5$. Thus $t\equiv3$, and

$$
r'=r+5t=1+15=16.
$$

Check: $16^2=256\equiv6\pmod{25}$.

For $r=4$: $(a-r^2)/5=(6-16)/5=-2\equiv3\pmod5$, and $(2r)^{-1}=8^{-1}\equiv3^{-1}\equiv2\pmod5$. Thus $t\equiv3\cdot2=6\equiv1$, and

$$
r'=4+5=9.
$$

Check: $9^2=81\equiv6\pmod{25}$. The two roots are $9$ and $16$.

**20.** *Strategy: use the Chinese remainder theorem and count roots modulo each prime.*

Since $105=3\cdot5\cdot7$, a solution modulo $105$ is equivalent to a triple of solutions modulo $3$, $5$, and $7$. Modulo each prime, $x^2\equiv1$ has exactly two roots: modulo $3$, $x\equiv\pm1$; modulo $5$, $x\equiv\pm1$; modulo $7$, $x\equiv\pm1$. Each choice is independent, so the number of solutions is

$$
2\cdot2\cdot2=2^{\omega(105)}=2^3=8.
$$

They can be listed as $1,29,34,41,64,71,76,104$ modulo $105$.

**21.** *Strategy: use multiplicativity and the fact that a non-residue has symbol $-1$.*

Let $a,b$ be quadratic non-residues modulo $p$. Then $\left(\frac{a}{p}\right)=\left(\frac{b}{p}\right)=-1$. By multiplicativity,

$$
\left(\frac{ab}{p}\right)=\left(\frac{a}{p}\right)\left(\frac{b}{p}\right)=(-1)(-1)=1,
$$

so $ab$ is a residue. For the quotient, if $b$ is a non-residue then $b$ is invertible modulo $p$ and
$\left(\frac{b^{-1}}{p}\right)=\left(\frac{b}{p}\right)=-1$ (because the symbol of an inverse equals the symbol of the element). Hence

$$
\left(\frac{a/b}{p}\right)=\left(\frac{a}{p}\right)\left(\frac{b^{-1}}{p}\right)=(-1)(-1)=1.
$$

**22.** *Strategy: reciprocity with $5\equiv1\pmod4$ makes the symbol symmetric.*

Since $5\equiv1\pmod4$,

$$
\left(\frac{5}{p}\right)=\left(\frac{p}{5}\right)
$$

for every odd prime $p\ne5$. The nonzero squares modulo $5$ are $1$ and $4$, so $\left(\frac{p}{5}\right)=1$ exactly when $p\equiv1$ or $4\pmod5$. Thus

$$
\left(\frac{5}{p}\right)=1
\iff p\equiv\pm1\pmod5.
$$

For $p=5$, the symbol is $\left(\frac{5}{5}\right)=0$, so $p=5$ is not included. The primes are therefore $p\equiv1,4\pmod5$, $p\ne5$.

## Advanced

**23.** *Strategy: split into residue and non-residue cases; use Fermat and the root bound for a polynomial over a field.*

First suppose $a$ is a quadratic residue, so $a\equiv x^2\pmod p$ with $p\nmid x$. Fermat's little theorem gives $x^{p-1}\equiv1$, hence

$$
a^{(p-1)/2}\equiv x^{p-1}\equiv1=\left(\frac{a}{p}\right)\pmod p.
$$

Now suppose $a$ is a non-residue. By Fermat, $a^{p-1}\equiv1$, so
$\left(a^{(p-1)/2}\right)^2\equiv1$. The polynomial $T^2-1$ has only the roots $\pm1$ in the field $\mathbb{F}_p$, so $a^{(p-1)/2}\equiv\pm1$.

We must rule out $+1$. The polynomial $f(T)=T^{(p-1)/2}-1$ has degree $(p-1)/2$, hence at most $(p-1)/2$ roots in $\mathbb{F}_p$. Every nonzero quadratic residue is a root: if $a\equiv x^2$, then $a^{(p-1)/2}\equiv x^{p-1}\equiv1$. There are exactly $(p-1)/2$ nonzero residues, so they exhaust the roots. A non-residue is not a root, so $a^{(p-1)/2}\not\equiv1$. Therefore $a^{(p-1)/2}\equiv-1=\left(\frac{a}{p}\right)$.

In both cases the two sides are $\pm1$ and congruent modulo the odd prime $p$, so they are equal. $\blacksquare$

**24.** *Strategy: pair each residue with its least absolute value; show distinctness by a congruence argument; compare products.*

Let $p$ be an odd prime, $p\nmid a$, and for $i=1,\dots,(p-1)/2$ let $r_i$ be the least positive residue of $ai$ modulo $p$. Define

$$
s_i=\min(r_i,p-r_i)\in\left\{1,\dots,\frac{p-1}{2}\right\},
\qquad
m=\#\{i:r_i>p/2\}.
$$

The $s_i$ are pairwise distinct. If $s_i=s_j$, then $r_i\equiv r_j$ or $r_i\equiv-r_j\pmod p$. In the first case $a(i-j)\equiv0$, so $i\equiv j\pmod p$; since $1\le i,j\le(p-1)/2<p$, this gives $i=j$. In the second case $a(i+j)\equiv0$, so $p\mid i+j$; but $2\le i+j\le p-1$, a contradiction. Hence the $s_i$ are $(p-1)/2$ distinct integers in a set of that size, so they are a permutation of $\{1,\dots,(p-1)/2\}$.

Taking products modulo $p$,

$$
\prod_i r_i\equiv a^{(p-1)/2}\left(\frac{p-1}{2}\right)!.
$$

Also, each $r_i$ equals $s_i$ except when $r_i>p/2$, in which case $r_i=p-s_i\equiv-s_i$. Therefore

$$
\prod_i r_i\equiv(-1)^m\prod_i s_i=(-1)^m\left(\frac{p-1}{2}\right)!.
$$

The factorial is invertible modulo $p$, so cancelling gives $a^{(p-1)/2}\equiv(-1)^m$. Euler's criterion then gives $\left(\frac{a}{p}\right)=(-1)^m$. $\blacksquare$

**25.** *Strategy: Euler's criterion at $a=-1$; both sides are $\pm1$.*

By Euler's criterion with $a=-1$,

$$
(-1)^{(p-1)/2}\equiv\left(\frac{-1}{p}\right)\pmod p.
$$

Both sides belong to $\{1,-1\}$ and $p$ is odd, so congruence implies equality:

$$
\left(\frac{-1}{p}\right)=(-1)^{(p-1)/2}.
$$

The exponent is even exactly when $p\equiv1\pmod4$. Hence $-1$ is a quadratic residue modulo $p$ exactly for primes $p\equiv1\pmod4$; for $p\equiv3\pmod4$ it is a non-residue. $\blacksquare$

**26.** *Strategy: Gauss's lemma with $a=2$; count residues exceeding $p/2$.*

For $a=2$ and $1\le j\le(p-1)/2$, the least positive residue of $2j$ is $2j$ itself, since $2j\le p-1<p$. Thus $m$ is the number of $j$ with $2j>p/2$, i.e. $j>p/4$:

$$
m=\left\lfloor\frac{p-1}{2}\right\rfloor-\left\lfloor\frac p4\right\rfloor.
$$

Write $p=8k+r$ with $r\in\{1,3,5,7\}$:

| $p$ | $\lfloor(p-1)/2\rfloor$ | $\lfloor p/4\rfloor$ | $m$ | parity |
|---|---|---|---|---|
| $8k+1$ | $4k$ | $2k$ | $2k$ | even |
| $8k+3$ | $4k+1$ | $2k$ | $2k+1$ | odd |
| $8k+5$ | $4k+2$ | $2k+1$ | $2k+1$ | odd |
| $8k+7$ | $4k+3$ | $2k+1$ | $2k+2$ | even |

By Gauss's lemma, $\left(\frac{2}{p}\right)=(-1)^m$, which is $1$ exactly for $p\equiv1,7\pmod8$. The formula $(-1)^{(p^2-1)/8}$ gives the same values, since $(p^2-1)/8$ is even exactly for those two classes. $\blacksquare$

**27.** *Strategy: compare $q_i=\lfloor ai/p\rfloor$ with the large-residue count $m$ modulo $2$.*

Let $p$ be odd, $a$ odd, $p\nmid a$. Write $ai=pq_i+r_i$ with $1\le r_i\le p-1$ and
$q_i=\lfloor ai/p\rfloor$. Let $m$ be the number of $i$ with $r_i>p/2$. By Gauss's lemma,
$\left(\frac{a}{p}\right)=(-1)^m$. We show $\sum_i q_i\equiv m\pmod2$.

Let $s_i=\min(r_i,p-r_i)$ and let $\varepsilon_i=1$ if $r_i>p/2$, and $0$ otherwise. From Gauss's lemma, the $s_i$ are a permutation of $\{1,\dots,(p-1)/2\}$. Since $a$ and $p$ are odd,

$$
r_i=ai-pq_i\equiv i-q_i\equiv i+q_i\pmod2.
$$

If $r_i<p/2$, then $r_i=s_i$; if $r_i>p/2$, then $r_i=p-s_i\equiv1+s_i\pmod2$. Thus in all cases
$r_i\equiv s_i+\varepsilon_i\pmod2$. Summing,

$$
\sum_i r_i\equiv\sum_i s_i+m\equiv\sum_i i+m\pmod2.
$$

On the other hand, summing $ai=pq_i+r_i$ gives $p\sum_i q_i=a\sum_i i-\sum_i r_i$. Reducing modulo $2$ (where $p\equiv a\equiv1$),

$$
\sum_i q_i\equiv\sum_i i-\sum_i r_i
\equiv\sum_i i-\left(\sum_i i+m\right)
\equiv m\pmod2.
$$

Therefore

$$
\left(\frac{a}{p}\right)=(-1)^m=(-1)^{\sum_i q_i}. \qquad\blacksquare
$$

**28.** *Strategy: factor $m$ and $n$, apply prime reciprocity to each pair, and collect the exponent.*

Write $m=\prod_i p_i^{a_i}$ and $n=\prod_j q_j^{b_j}$. By multiplicativity in the numerator and denominator,

$$
\left(\frac{m}{n}\right)\left(\frac{n}{m}\right)
=\prod_{i,j}\left[\left(\frac{p_i}{q_j}\right)\left(\frac{q_j}{p_i}\right)\right]^{a_i b_j}.
$$

For each pair of odd primes, quadratic reciprocity gives

$$
\left(\frac{p_i}{q_j}\right)\left(\frac{q_j}{p_i}\right)
=(-1)^{\frac{p_i-1}{2}\cdot\frac{q_j-1}{2}}.
$$

Therefore

$$
\left(\frac{m}{n}\right)\left(\frac{n}{m}\right)
=(-1)^{\sum_{i,j}a_i b_j\frac{p_i-1}{2}\cdot\frac{q_j-1}{2}}
=(-1)^{\left(\sum_i a_i\frac{p_i-1}{2}\right)\left(\sum_j b_j\frac{q_j-1}{2}\right)}.
$$

For an odd positive integer $N=\prod \ell^{e}$, the parity identity

$$
\frac{N-1}{2}\equiv\sum e\frac{\ell-1}{2}\pmod2
$$

holds: indeed $N\equiv\prod(1+2\frac{\ell-1}{2})^{e}\equiv1+2\sum e\frac{\ell-1}{2}\pmod4$, so $(N-1)/2\equiv\sum e(\ell-1)/2\pmod2$. Applying this to $m$ and $n$ gives

$$
\left(\frac{m}{n}\right)\left(\frac{n}{m}\right)
=(-1)^{\frac{m-1}{2}\cdot\frac{n-1}{2}}. \qquad\blacksquare
$$

**29.** *Strategy: raise the candidate to the square and use Euler's criterion.*

Since $p\equiv3\pmod4$, the integer $(p+1)/4$ is an integer. Let
$x=a^{(p+1)/4}$. Then

$$
x^2=a^{(p+1)/2}=a\cdot a^{(p-1)/2}\equiv a\cdot1=a\pmod p,
$$

where Euler's criterion was used (because $\left(\frac{a}{p}\right)=1$). Thus $x$ is a root. The other root is $-x$; it is distinct from $x$ because $2x\not\equiv0\pmod p$ ($x\not\equiv0$ as $p\nmid a$ and $p$ is odd). Since a quadratic congruence modulo a prime has at most two roots, these are all.

For $p=11$, $a=5$: $(p+1)/4=3$, so $x=5^3=125\equiv4\pmod{11}$. The roots are $4$ and $-4\equiv7$. Check: $4^2=16\equiv5$ and $7^2=49\equiv5$.

**30.** *Strategy: Chinese remainder theorem and the prime-power root count.*

Let $n=\prod_{i=1}^{r}p_i^{e_i}$ with the $p_i$ distinct odd primes. The Chinese remainder theorem gives a ring isomorphism

$$
\mathbb{Z}/n\mathbb{Z}\;\cong\;\prod_{i=1}^{r}\mathbb{Z}/p_i^{e_i}\mathbb{Z},
\qquad
x\mapsto(x\bmod p_1^{e_1},\dots,x\bmod p_r^{e_r}).
$$

Therefore $x^2\equiv a\pmod n$ is equivalent to the system
$x^2\equiv a\pmod{p_i^{e_i}}$ for all $i$. If one local congruence has no solution, the system has none. If every local congruence is solvable, the global solutions are exactly the tuples of local solutions.

Because $\gcd(a,n)=1$, we have $p_i\nmid a$ for every $i$. For an odd prime $p_i$ and $p_i\nmid a$, Hensel lifting gives exactly two roots modulo $p_i^{e_i}$ whenever a root exists modulo $p_i$. (Starting from two roots modulo $p_i$, each lifts uniquely at every stage; see Lemma 7.9.2.) Thus each local solution set has size $2$, and the number of tuples is

$$
\prod_{i=1}^{r}2=2^{r}=2^{\omega(n)}.
$$

Each tuple corresponds to exactly one residue class modulo $n$ by the Chinese remainder theorem, so there are exactly $2^{\omega(n)}$ solutions. $\blacksquare$

**31.** *Strategy: factor $(-3/p)$ into $(-1/p)(3/p)$, apply reciprocity to $(3/p)$, and use the supplementary law.*

For $p\ne3$,

$$
\left(\frac{-3}{p}\right)=\left(\frac{-1}{p}\right)\left(\frac{3}{p}\right).
$$

By the first supplementary law, $\left(\frac{-1}{p}\right)=(-1)^{(p-1)/2}$. By quadratic reciprocity, since $3\equiv3\pmod4$,

$$
\left(\frac{3}{p}\right)=(-1)^{(p-1)/2}\left(\frac{p}{3}\right).
$$

Multiplying, the two signs cancel:

$$
\left(\frac{-3}{p}\right)=(-1)^{(p-1)/2}\cdot(-1)^{(p-1)/2}\left(\frac{p}{3}\right)
=\left(\frac{p}{3}\right).
$$

The nonzero squares modulo $3$ are just $1$, so $\left(\frac{p}{3}\right)=1$ exactly when $p\equiv1\pmod3$, and it is $-1$ when $p\equiv2\pmod3$. Therefore

$$
\left(\frac{-3}{p}\right)=1\iff p\equiv1\pmod3.
$$

The case $p=3$ is excluded because the denominator would equal the numerator's prime factor. $\blacksquare$

**32.** *Strategy: count $y$-solutions for each $x$ using the Legendre symbol, then evaluate a character sum by counting points on a hyperbola.*

For fixed $x$, the number of $y\in\mathbb{F}_p$ with $y^2=1-x^2$ is $1+\chi(1-x^2)$: it is $1$ when $1-x^2=0$ (only $y=0$), $2$ when $1-x^2$ is a nonzero square, and $0$ when it is a nonsquare. Hence

$$
N=\sum_{x\in\mathbb{F}_p}\left(1+\chi(1-x^2)\right)=p+S,
\qquad
S=\sum_x\chi(1-x^2).
$$

We evaluate $S$. Since $1-x^2=-(x^2-1)$ and $\chi(-1)=\pm1$,

$$
S=\chi(-1)\sum_x\chi(x^2-1).
$$

We claim $\sum_x\chi(x^2-a)=-1$ for every $a\ne0$. To prove it, count the solutions of $y^2=x^2-a$. For each $x$, the number of $y$ is $1+\chi(x^2-a)$, so the total number is $p+\sum_x\chi(x^2-a)$. On the other hand,

$$
y^2=x^2-a
\iff (x-y)(x+y)=a.
$$

The map $(x,y)\mapsto(u,v)=(x-y,x+y)$ is a bijection of $\mathbb{F}_p^2$ (since $2$ is invertible modulo the odd prime $p$), and it sends the equation to $uv=a$. For each of the $p-1$ choices $u\in\mathbb{F}_p^\times$, there is exactly one $v=a/u$. Hence there are $p-1$ solutions. Therefore

$$
p+\sum_x\chi(x^2-a)=p-1
\implies
\sum_x\chi(x^2-a)=-1.
$$

Taking $a=1$, we get $S=\chi(-1)(-1)=-\chi(-1)$, and therefore

$$
N=p-\chi(-1).
$$

For example, for $p=5$, $\chi(-1)=1$ and $N=4$; the solutions are $(\pm1,0)$ and $(0,\pm1)$. For $p=7$, $\chi(-1)=-1$ and $N=8$. $\blacksquare$

## Challenge

**33.** *Strategy: assume finitely many primes $1\bmod4$, build $N$ whose prime divisors must be new and $1\bmod4$.*

Suppose, for contradiction, that $p_1,\dots,p_k$ are all the primes congruent to $1$ modulo $4$. Let $P=p_1p_2\cdots p_k$ (the empty product is $1$ if $k=0$) and set

$$
N=(2P)^2+1=4P^2+1.
$$

Then $N$ is odd and $N>1$, so it has an odd prime divisor $q$. Modulo $q$,

$$
(2P)^2\equiv-1,
$$

so $-1$ is a quadratic residue modulo $q$. By the first supplementary law, $q\equiv1\pmod4$. But $N\equiv1\pmod{p_i}$ for every $i$, because $N=4P^2+1$ and $p_i\mid P$. Hence $q$ is not any of the $p_i$, contradicting the assumption that the list was complete. Therefore there are infinitely many primes $1$ modulo $4$. $\blacksquare$

**34.** *Strategy: assume finitely many primes $1\bmod8$, build $N=x^4+1$, and show every prime divisor has an element of order $8$, hence is $1\bmod8$.*

Suppose $p_1,\dots,p_k$ are all the primes congruent to $1$ modulo $8$. Let $P=p_1\cdots p_k$ and $x=2P$, and set

$$
N=x^4+1.
$$

Then $N$ is odd and $N>1$. Let $q$ be a prime divisor of $N$. Then $q\ne2$ and $q\nmid x$ (if $q\mid x$, then $N\equiv1\pmod q$, contradiction). Modulo $q$,

$$
x^4\equiv-1,
\qquad
x^8\equiv1.
$$

Thus the multiplicative order $d$ of $x$ modulo $q$ divides $8$. It does not divide $4$, because $x^4\equiv-1\not\equiv1$ (as $q$ is odd, $-1\ne1$). Hence $d=8$. By Lagrange's theorem, $d\mid(q-1)$, so $8\mid(q-1)$ and $q\equiv1\pmod8$.

Also $N=x^4+1\equiv1\pmod{p_i}$ for every $i$, because $p_i\mid P\mid x$. Hence $q$ is not among the $p_i$, contradicting the assumption that the list was complete. Therefore there are infinitely many primes congruent to $1$ modulo $8$. $\blacksquare$

**35.** *Strategy: view the sign of a permutation as a homomorphism on $\mathbb{F}_p^\times$, show its kernel contains the squares, and show it is not everything by using a primitive root.*

Let $\pi_a$ be the permutation of $\{0,1,\dots,p-1\}$ induced by multiplication by $a$ modulo $p$. It fixes $0$, so its sign equals the sign of the induced permutation of the $p-1$ nonzero residues.

Define

$$
\operatorname{sgn}:\mathbb{F}_p^\times\to\{\pm1\},
\qquad
\operatorname{sgn}(a)=\text{sign of }\pi_a.
$$

This is a group homomorphism because $\pi_{ab}=\pi_a\circ\pi_b$ and the sign of a composition is the product of signs.

Every square lies in the kernel: if $a=b^2$, then $\pi_a=\pi_b\circ\pi_b$, so
$\operatorname{sgn}(a)=\operatorname{sgn}(b)^2=1$.

The kernel is therefore a subgroup containing the subgroup of squares, which has index $2$ in $\mathbb{F}_p^\times$. Hence the kernel is either all of $\mathbb{F}_p^\times$ or exactly the squares. It is not all: let $g$ be a generator of the cyclic group $\mathbb{F}_p^\times$. Multiplication by $g$ permutes the $p-1$ nonzero elements in a single cycle of length $p-1$, whose sign is

$$
(-1)^{(p-1)-1}=(-1)^{p-2}=-1
$$

because $p$ is odd. Thus $\operatorname{sgn}(g)=-1\ne1$, so the kernel is a proper subgroup. It must therefore equal the subgroup of squares. Consequently,

$$
\operatorname{sgn}(\pi_a)=1\iff a\text{ is a square mod }p
\iff\left(\frac{a}{p}\right)=1,
$$

and $\operatorname{sgn}(\pi_a)=-1$ exactly when $\left(\frac{a}{p}\right)=-1$. Hence
$\operatorname{sgn}(\pi_a)=\left(\frac{a}{p}\right)$. $\blacksquare$

**36.** *Strategy: handle $k=1,2$ directly; for $k\ge3$, prove the four roots of $1$ and use induction on $k$.*

For $k=1$, every odd $a$ satisfies $a\equiv1\pmod2$, and $x^2\equiv1\pmod2$ has the unique solution $x\equiv1\pmod2$.

For $k=2$, odd squares are $1$ modulo $4$: $(2m+1)^2=4m(m+1)+1\equiv1\pmod4$. If $a\equiv1\pmod4$, the roots are $x\equiv1,3\pmod4$; if $a\equiv3\pmod4$, there are none.

Now let $k\ge3$. Every odd square is $1$ modulo $8$: if $x=2m+1$, then
$x^2=4m(m+1)+1$ and $m(m+1)$ is even, so $8\mid(x^2-1)$. Hence $a\equiv1\pmod8$ is necessary.

Assume $a\equiv1\pmod8$. We first determine the square roots of $1$ modulo $2^k$. If $u^2\equiv1\pmod{2^k}$, then

$$
(u-1)(u+1)\equiv0\pmod{2^k}.
$$

Both factors are even, and $\gcd(u-1,u+1)=\gcd(u-1,2)=2$ because $u$ is odd. Therefore one of the two factors is divisible by $2^{k-1}$ and the other by exactly $2$. Equivalently, $u\equiv1$ or $u\equiv-1\pmod{2^{k-1}}$. This gives exactly four residues modulo $2^k$:

$$
u\equiv1,\quad -1,\quad 1+2^{k-1},\quad -1+2^{k-1}\pmod{2^k}.
$$

Now prove by induction that $x^2\equiv a\pmod{2^k}$ has exactly four solutions. For $k=3$, every odd $x$ satisfies $x^2\equiv1\pmod8$, so the four odd residues are the solutions when $a\equiv1\pmod8$.

Assume there are exactly four solutions modulo $2^k$, and let $r$ be one of them. The four solutions are $ru$ as $u$ runs over the four roots of $1$; write them as $r,-r,r(1+2^{k-1}),-r(1+2^{k-1})$. A lift of a root $r$ to modulo $2^{k+1}$ has the form $r+t2^k$ with $t\in\{0,1\}$, and

$$
(r+t2^k)^2=r^2+2^{k+1}rt+t^22^{2k}\equiv r^2+2^{k+1}rt\pmod{2^{k+1}},
$$

since $2k\ge k+1$ for $k\ge1$. Write $r^2-a=2^kc$. The lift works exactly when $c+2rt$ is even, i.e. when $c$ is even; if $c$ is even, both lifts work, and if $c$ is odd, neither does.

For $r$ and $r(1+2^{k-1})$, the corresponding values of $c$ have opposite parity. Indeed, with $c=(r^2-a)/2^k$,

$$
\frac{\left(r(1+2^{k-1})\right)^2-a}{2^k}
=c+r^2+r^22^{k-2}\equiv c+1\pmod2,
$$

because $r$ is odd and $2^{k-2}$ is even for $k\ge3$. The same parity statement holds for $-r$ and $-r(1+2^{k-1})$. Hence exactly two of the four roots modulo $2^k$ lift, and each has exactly two lifts, giving exactly four roots modulo $2^{k+1}$. By induction, there are exactly four roots modulo $2^k$ for every $k\ge3$ when $a\equiv1\pmod8$.

This completes all cases. $\blacksquare$
