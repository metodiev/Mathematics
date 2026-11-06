# Advanced Algebra — Solutions

> [Tutorial](README.md) · [Exercises](exercises.md) · 38 worked solutions

Each solution states the strategy, carries out every step, and finishes with a check that is
independent of the method used.

## Beginner

**1.** Use synthetic division with the root $2$ and the coefficient list $1,-5,7,-2$, including a
zero for any missing power (none is missing here): bring down $1$; multiply by $2$ and add to $-5$
to get $-3$; multiply by $2$ and add to $7$ to get $1$; multiply by $2$ and add to $-2$ to get $0$.
Hence
$$x^3-5x^2+7x-2 = (x-2)\left(x^2-3x+1\right) + 0.$$
**Check.** $(x-2)(x^2-3x+1) = x^3-3x^2+x-2x^2+6x-2 = x^3-5x^2+7x-2$. The quotient is $x^2-3x+1$ and
the remainder is $0$; the remaining roots are $\frac{3\pm\sqrt5}{2}$.

**2.** By the remainder theorem the remainder is $P(-1)$ for $P(x) = 2x^3-x^2+4x-3$:
$$P(-1) = 2(-1)^3-(-1)^2+4(-1)-3 = -2-1-4-3 = -10.$$
**Check by division.** Synthetic division with $-1$ on $2,-1,4,-3$ gives quotient
$2x^2-3x+7$ and remainder $-10$, since $(x+1)(2x^2-3x+7) = 2x^3-x^2+4x+7$ and subtracting $10$ gives
$2x^3-x^2+4x-3$. Agrees.

**3.** Look for two integers with product $12$ and sum $7$: they are $3$ and $4$. Hence
$$x^2-7x+12 = (x-3)(x-4),$$
so the roots are $x = 3$ and $x = 4$.
**Check.** $(x-3)(x-4) = x^2-4x-3x+12 = x^2-7x+12$. Correct.

**4.** Each factor $(x-r)^m$ contributes the root $r$ with multiplicity $m$:
$$x = 1 \text{ with multiplicity } 3, \qquad x = -2 \text{ with multiplicity } 2, \qquad x = 5 \text{ with multiplicity } 1.$$
The degree is the sum of the multiplicities, $3+2+1 = 6$, which also equals the sum of the degrees of
the factors.
**Check.** $P$ has leading term $x^3\cdot x^2\cdot x = x^6$, so $\deg P = 6$. Agrees.

**5.** Two distinct linear factors give one constant numerator each:
$$\frac{x+1}{(x-1)(x+4)} = \frac{A}{x-1}+\frac{B}{x+4}.$$
No quadratic term is needed because both factors are linear and neither is repeated.

**6.** Write
$$\frac{5x+1}{(x-1)(x+2)} = \frac{A}{x-1}+\frac{B}{x+2}.$$
Clearing denominators: $5x+1 = A(x+2)+B(x-1)$. Set $x=1$: $6 = 3A$, so $A = 2$. Set $x=-2$:
$-9 = -3B$, so $B = 3$. Therefore
$$\frac{5x+1}{(x-1)(x+2)} = \frac{2}{x-1}+\frac{3}{x+2}.$$
**Check by recombining.** $\dfrac{2(x+2)+3(x-1)}{(x-1)(x+2)} = \dfrac{2x+4+3x-3}{(x-1)(x+2)} = \dfrac{5x+1}{(x-1)(x+2)}$. Correct.

**7.** For an arithmetic sequence, $a_n = a_1+(n-1)d$ with $a_1 = 3$ and $d = 7-3 = 4$. Hence
$$a_{10} = 3+9\cdot4 = 39.$$
**Check.** The terms are $3,7,11,15,19,23,27,31,35,39$: the tenth is indeed $39$, and the difference
between consecutive terms is always $4$.

**8.** Pair the first term with the last, the second with the second-to-last, and so on: each of the
$50$ pairs sums to $101$. Hence
$$1+2+\cdots+100 = 50\cdot101 = 5050.$$
**Check with the formula.** $S_n = \frac{n(n+1)}{2} = \frac{100\cdot101}{2} = 5050$. Agrees.

**9.** This is geometric with $a_1 = 2$ and $r = 3$, so
$$a_8 = 2\cdot3^{7} = 2\cdot2187 = 4374.$$
**Check.** $2,6,18,54,162,486,1458,4374$: each term is three times the previous, and the eighth is
$4374$.

**10.** This is geometric with $a_1 = 1$ and $r = \frac12$. Since $\lvert r\rvert<1$ the series
converges, and
$$S = \frac{a_1}{1-r} = \frac{1}{1-\frac12} = 2.$$
**Check.** $1+\frac12+\frac14+\frac18 = \frac{15}{8} = 1.875$; the next term $\frac1{16}$ brings the
total to $1.9375$; the partial sums increase to $2$, consistent with the formula.

**11.** Compute the four terms directly:
$$k=1:\ 0, \quad k=2:\ 3, \quad k=3:\ 8, \quad k=4:\ 15, \qquad \text{sum} = 26.$$
**Check with the standard sums.** $\sum_{k=1}^{4}k^2-4 = \frac{4\cdot5\cdot9}{6}-4 = 30-4 = 26$. Agrees.

**12.** If $x$ and $y$ have sum $5$ and product $6$, they are the roots of
$$t^2-5t+6 = 0 \implies (t-2)(t-3) = 0 \implies t = 2 \text{ or } t = 3.$$
So $\{x,y\} = \{2,3\}$, giving the ordered solutions $(2,3)$ and $(3,2)$.
**Check.** $2+3 = 5$ and $2\cdot3 = 6$; the ordered pair $(3,2)$ also satisfies both by symmetry.
Correct.

## Intermediate

**13.** Candidates are $\pm1,\pm2,\pm3,\pm6$. Testing,
$$P(2) = 8+8-10-6 = 0,$$
so $x-2$ is a factor. Dividing,
$$x^3+2x^2-5x-6 = (x-2)\left(x^2+4x+3\right) = (x-2)(x+1)(x+3).$$
The roots are $2,-1,-3$.
**Check by Vieta.** Sum $= 2-1-3 = -2 = -a_2/a_3$; product $= 2\cdot(-1)\cdot(-3) = 6 = -a_0/a_3 = -(-6)$.
Both hold.

**14.** With $a_3 = 3$ and $a_0 = -3$, candidates are $\pm1,\pm3,\pm\frac13$. Testing $x = 3$:
$$3\cdot27-5\cdot9-33-3 = 81-45-33-3 = 0.$$
Dividing by $x-3$ gives $3x^2+4x+1$, and
$$3x^2+4x+1 = (3x+1)(x+1).$$
So the rational roots are $3, -\frac13, -1$.
**Check by Vieta.** Sum $= 3-\frac13-1 = \frac53 = -a_2/a_3 = \frac53$; product
$= 3\cdot\left(-\frac13\right)\cdot(-1) = 1 = -a_0/a_3 = \frac33$. Both agree, and by the rational
root theorem these are the only rational roots.

**15.** The coefficient signs of $P(x) = x^4-3x^3+2x^2+x-1$ are $+,-,+,+,-$: the changes occur at
$+\to-$, $-\to+$ and $+\to-$ (the repeated $+$ is not a change), so there are $3$ sign changes and
$P$ has $3$ or $1$ positive roots. For
$$P(-x) = x^4+3x^3+2x^2-x-1$$
the signs are $+,+,+,-,-$, with exactly one change, so $P$ has exactly $1$ negative root.
**Check by factorisation.** $P(x) = (x-1)^2(x^2-x-1)$, whose roots are $1$ (double),
$\frac{1+\sqrt5}{2}\approx1.618$ (positive) and $\frac{1-\sqrt5}{2}\approx-0.618$ (negative). So there
are $3$ positive roots counted with multiplicity and $1$ negative, matching the rule.

**16.** With a repeated linear factor, include both powers:
$$\frac{x+5}{(x-1)^2} = \frac{A}{x-1}+\frac{B}{(x-1)^2}.$$
Clearing denominators: $x+5 = A(x-1)+B$. Comparing coefficients, $A = 1$ and $B-A = 5$, so $B = 6$.
Therefore
$$\frac{x+5}{(x-1)^2} = \frac{1}{x-1}+\frac{6}{(x-1)^2}.$$
**Check.** $\dfrac{(x-1)+6}{(x-1)^2} = \dfrac{x+5}{(x-1)^2}$. Correct. (Equivalently, the cover-up
rule at $x=1$ gives $B = 1+5 = 6$.)

**17.** Write
$$\frac{3x^2+2x+1}{x(x^2+1)} = \frac{A}{x}+\frac{Bx+C}{x^2+1}.$$
Clearing denominators:
$$3x^2+2x+1 = A(x^2+1)+(Bx+C)x = (A+B)x^2+Cx+A.$$
Comparing coefficients: $A = 1$, $C = 2$, $A+B = 3$ so $B = 2$. Hence
$$\frac{3x^2+2x+1}{x(x^2+1)} = \frac1x+\frac{2x+2}{x^2+1}.$$
**Check.** $\dfrac{(x^2+1)+x(2x+2)}{x(x^2+1)} = \dfrac{x^2+1+2x^2+2x}{x(x^2+1)} = \dfrac{3x^2+2x+1}{x(x^2+1)}$. Correct.

**18.** The fraction is improper ($\deg$ numerator $3$ > $\deg$ denominator $2$), so divide first:
$$x^3+1 = x\left(x^2-1\right)+(x+1), \qquad\text{so}\qquad \frac{x^3+1}{x^2-1} = x+\frac{x+1}{x^2-1}.$$
Now $x^2-1 = (x-1)(x+1)$, so
$$\frac{x+1}{(x-1)(x+1)} = \frac{1}{x-1} \qquad (x\neq-1),$$
and therefore
$$\frac{x^3+1}{x^2-1} = x+\frac{1}{x-1}$$
for $x \neq \pm1$ (the original expression is undefined at both points).
**Check.** $x+\dfrac{1}{x-1} = \dfrac{x(x-1)+1}{x-1} = \dfrac{x^2-x+1}{x-1}$, and multiplying
numerator and denominator by $x+1$ gives $\dfrac{(x+1)(x^2-x+1)}{x^2-1} = \dfrac{x^3+1}{x^2-1}$.
Correct.

**19.** From $x+y = 7$ we get $y = 7-x$. Substituting,
$$x^2+(7-x)^2 = 25 \implies 2x^2-14x+49 = 25 \implies x^2-7x+12 = 0 \implies x = 3 \text{ or } x = 4.$$
Then $y = 4$ or $y = 3$, so the solutions are $(3,4)$ and $(4,3)$.
**Check.** $9+16 = 25$ and $3+4 = 7$; $16+9 = 25$ and $4+3 = 7$. Correct.

**20.** Factor the difference of squares:
$$x^2-y^2 = (x-y)(x+y) = 16.$$
Since $x-y = 2 \neq 0$, we may divide: $x+y = 8$. Solving $x-y = 2$, $x+y = 8$ gives $x = 5$, $y = 3$.
**Check.** $5^2-3^2 = 25-9 = 16$ and $5-3 = 2$. Correct.

**21.** The multiples are $7, 14, \dots, 196$, an arithmetic sequence with $a_1 = 7$, $d = 7$ and
$$196 = 7n \implies n = 28.$$
The sum is
$$S_{28} = \frac{28}{2}(7+196) = 14\cdot203 = 2842.$$
**Check.** By the other form, $S_n = \frac n2(2a_1+(n-1)d) = 14(14+27\cdot7) = 14(14+189) = 14\cdot203 = 2842$.
Agrees.

**22.** Here $a_1 = 3$ and $r = \frac12$.
(a) The series converges because $\lvert r\rvert<1$, and
$$S = \frac{3}{1-\frac12} = 6.$$
(b) $S_6 = 3\cdot\dfrac{1-\left(\frac12\right)^6}{1-\frac12} = 6\left(1-\frac1{64}\right) = \frac{378}{64} = \frac{189}{32}$.
**Check.** The six terms are $3, 1.5, 0.75, 0.375, 0.1875, 0.09375$, whose sum is $5.90625$, and
$189/32 = 5.90625$. Agrees.

**23.** Since $\dfrac{1}{k}-\dfrac{1}{k+1} = \dfrac{(k+1)-k}{k(k+1)} = \dfrac{1}{k(k+1)}$, the sum
telescopes:
$$\sum_{k=1}^{n}\frac{1}{k(k+1)} = \sum_{k=1}^{n}\left(\frac1k-\frac{1}{k+1}\right)
= 1-\frac{1}{n+1} = \frac{n}{n+1}.$$
For $n = 99$ this is $\frac{99}{100}$.
**Check for $n=2$.** $\frac12+\frac16 = \frac23 = \frac{2}{3}$. Agrees; and for $n=99$ the partial
sum is $0.99$, just below the limit $1$.

**24.** From the first equation, $z = 6-x-y$. Substituting into the second,
$$2x-y+(6-x-y) = 3 \implies x-2y = -3.$$
Substituting into the third,
$$x+2y-(6-x-y) = 2 \implies 2x+3y = 8.$$
Now solve $x = 2y-3$ in the second: $2(2y-3)+3y = 8$, so $7y = 14$, $y = 2$ and $x = 1$. Then
$z = 6-1-2 = 3$.
**Check.** $1+2+3 = 6$; $2-2+3 = 3$; $1+4-3 = 2$. All three original equations hold, so the solution
is $(1,2,3)$.

## Advanced

**25.** Since $x-2$ is a double factor, divide twice. First division by $x-2$:
$$x^4-6x^3+9x^2+4x-12 = (x-2)\left(x^3-4x^2+x+6\right),$$
and a second division by $x-2$:
$$x^3-4x^2+x+6 = (x-2)\left(x^2-2x-3\right) = (x-2)(x-3)(x+1).$$
Therefore
$$x^4-6x^3+9x^2+4x-12 = (x-2)^2(x-3)(x+1),$$
and the roots are $2$ (multiplicity $2$), $3$ and $-1$.
**Check.** $(x-2)^2(x-3)(x+1)$: at $x=0$ this is $4\cdot(-3)\cdot1 = -12$, matching the constant term;
the leading coefficient is $1$; and the degree is $4$. Correct.

**26.** Real coefficients force the conjugate $1-i$ to be a root as well (conjugate root theorem), so
the minimum degree is
$$2+3+1+1 = 7.$$
The factored form is
$$P(x) = a(x-2)^2(x+1)^3\bigl(x-(1+i)\bigr)\bigl(x-(1-i)\bigr) = a(x-2)^2(x+1)^3\left((x-1)^2+1\right),$$
that is $P(x) = a(x-2)^2(x+1)^3(x^2-2x+2)$ with $a \neq 0$.
**Check.** The quadratic factor has discriminant $4-8 = -4<0$, so it is irreducible over $\mathbb{R}$,
and its roots are $1\pm i$. The degree is $2+3+2 = 7$. Correct.

**27.** For $P(x) = x^3+x+1$ the signs are $+,+,+$: no sign change, so there are no positive real
roots. For
$$P(-x) = -x^3-x+1$$
the signs are $-, -, +$: exactly one sign change, so there is exactly one negative real root. Since a
cubic has three roots over $\mathbb{C}$ (fundamental theorem of algebra), and one is real, the other
two form a nonreal conjugate pair.
**Check.** Numerically the roots are $\approx -0.6823$ and $\approx 0.3412 \pm 1.1615i$: one negative
real, two nonreal. Agrees.

**28.** Write
$$\frac{3x^2+x}{(x+1)(x^2+1)} = \frac{A}{x+1}+\frac{Bx+C}{x^2+1}.$$
Clearing denominators,
$$3x^2+x = A(x^2+1)+(Bx+C)(x+1) = (A+B)x^2+(B+C)x+(A+C).$$
Comparing: $A+B = 3$, $B+C = 1$, $A+C = 0$. From the third $C = -A$; then $B = 1-C = 1+A$; and
$A+(1+A) = 3$ gives $A = 1$, $B = 2$, $C = -1$. Hence
$$\frac{3x^2+x}{(x+1)(x^2+1)} = \frac{1}{x+1}+\frac{2x-1}{x^2+1}.$$
**Check by recombining.** $(x^2+1)+(2x-1)(x+1) = x^2+1+2x^2+2x-x-1 = 3x^2+x$. Correct.

**29.** Square the sum:
$$(x+y)^2 = x^2+2xy+y^2 = 10+2\cdot3 = 16 \implies x+y = \pm4.$$
If $x+y = 4$, then $x$ and $y$ are the roots of $t^2-4t+3 = 0$, i.e. $\{1,3\}$. If $x+y = -4$, they
are the roots of $t^2+4t+3 = 0$, i.e. $\{-1,-3\}$. Hence
$$(1,3),\quad (3,1),\quad (-1,-3),\quad (-3,-1).$$
**Check.** For $(1,3)$: $1+9 = 10$ and $1\cdot3 = 3$. For $(-3,-1)$: $9+1 = 10$ and $(-3)(-1) = 3$.
All four pairs satisfy the system, and a circle and a hyperbola can meet in at most four points.

**30.** The first partial sum is the first term: $a_1 = S_1 = 3+5 = 8$. The second partial sum is
$S_2 = 12+10 = 22$, so $a_2 = S_2-S_1 = 14$ and $d = 14-8 = 6$.
**Check.** $S_n = \frac n2\left(2a_1+(n-1)d\right) = \frac n2\left(16+6(n-1)\right) = \frac n2(6n+10) = 3n^2+5n$,
which is the given formula. Correct.

**31.** The sum to infinity is $\dfrac{a_1}{1-r} = \dfrac{5}{1-r} = 20$, so $1-r = \frac14$ and
$r = \frac34$. Then
$$S_4 = 5\cdot\frac{1-\left(\frac34\right)^4}{1-\frac34} = 20\left(1-\frac{81}{256}\right) = 20\cdot\frac{175}{256} = \frac{3500}{256} = \frac{875}{64}.$$
**Check.** The first four terms are $5, 3.75, 2.8125, 2.109375$, whose sum is $13.671875$, and
$875/64 = 13.671875$. Agrees.

**32.** Use partial fractions:
$$\frac{1}{(2k-1)(2k+1)} = \frac12\left(\frac{1}{2k-1}-\frac{1}{2k+1}\right),$$
since $\dfrac{1}{2k-1}-\dfrac{1}{2k+1} = \dfrac{(2k+1)-(2k-1)}{(2k-1)(2k+1)} = \dfrac{2}{(2k-1)(2k+1)}$.
Summing telescopes:
$$\sum_{k=1}^{n}\frac{1}{(2k-1)(2k+1)} = \frac12\left(1-\frac{1}{2n+1}\right) = \frac12\cdot\frac{2n}{2n+1} = \frac{n}{2n+1}.$$
As $n\to\infty$ this tends to $\frac12$.
**Check for $n=1$.** The sum is $\frac{1}{1\cdot3} = \frac13$ and the formula gives $\frac13$. For
$n=2$: $\frac13+\frac{1}{15} = \frac{6}{15} = \frac25$, and $\frac{2}{5}$. Both agree.

**33.** The second equation is twice the first on the left:
$$2x+4y-2z = 2(x+2y-z) = 2\cdot3 = 6.$$
But the right-hand side is $7$, so the second equation requires $6 = 7$, a contradiction. Therefore
the system is **inconsistent** and has no solution. Repetition of the elimination confirms it:
subtracting twice the first equation from the second gives $0 = 1$.
Geometrically the first and second equations describe parallel planes.

**34.** The second equation is twice the first on the left, so for consistency its right-hand side
must be twice $2$:
$$k = 4.$$
With $k = 4$ the second equation is redundant. The third gives $x = y$; substituting into the first,
$2x+z = 2$, so $z = 2-2x$. The solution set is the line
$$\left\{(t,\ t,\ 2-2t) : t\in\mathbb{R}\right\}.$$
**Check.** For $t = 1$: $(1,1,0)$ gives $1+1+0 = 2$, $2+2+0 = 4$, $1-1 = 0$. Correct. For $k\neq4$
the system has no solution, because the first two equations contradict each other.

## Challenge

**35.** Use the identity $x^3+y^3 = (x+y)^3-3xy(x+y)$ with $x+y = 3$:
$$9 = 27-9xy \implies 9xy = 18 \implies xy = 2.$$
So $x$ and $y$ are the roots of $t^2-3t+2 = 0$, namely $1$ and $2$. Hence the solutions are
$$(1,2) \quad\text{and}\quad (2,1).$$
**Check.** $1^3+2^3 = 1+8 = 9$ and $1+2 = 3$; the second solution is the same pair in the other order.
Correct. (The system has only these two complex solutions, since $x,y$ are roots of a quadratic whose
roots are determined.)

**36.** A repeated root $r$ satisfies both $P(r) = 0$ and $P'(r) = 0$. Here
$$P'(x) = 3x^2-6x = 3x(x-2),$$
so $r = 0$ or $r = 2$.
* $P(0) = a$, so $a = 0$.
* $P(2) = 8-12+a = a-4$, so $a = 4$.

Therefore $a \in \{0,4\}$. For $a = 0$,
$$x^3-3x^2 = x^2(x-3),$$
a double root at $0$ and a simple root at $3$. For $a = 4$,
$$x^3-3x^2+4 = (x-2)^2(x+1),$$
a double root at $2$ and a simple root at $-1$.
**Check.** Expand $(x-2)^2(x+1) = (x^2-4x+4)(x+1) = x^3+x^2-4x^2-4x+4x+4 = x^3-3x^2+4$. Correct.

**37.** *Rational roots.* The only candidates are $\pm1$. Since
$$P(1) = 1-1-1 = -1 \neq 0, \qquad P(-1) = -1+1-1 = -1 \neq 0,$$
there is no rational root.

*Descartes.* The coefficients of $P(x) = x^5-x-1$ have signs $+,-,-$, with exactly one change, so
there is exactly one positive real root. For $P(-x) = -x^5+x-1$ the signs are $-,+,-$, with two
changes, so there are $2$ or $0$ negative real roots. The degree is $5$, so the remaining roots are
nonreal and come in conjugate pairs; numerically the roots are one positive real value
$\approx1.1673$ and two conjugate pairs.

*Solvability.* Existence of roots is guaranteed by the fundamental theorem of algebra, but the Galois
group of $x^5-x-1$ over $\mathbb{Q}$ is the symmetric group $S_5$. Since $A_5$ is simple, $S_5$ is not
a solvable group, and Galois's criterion (equivalently the Abel–Ruffini theorem) says that a
polynomial is solvable by radicals exactly when its Galois group is solvable. Hence $x^5-x-1$ is not
solvable by radicals, even though its roots exist and can be approximated numerically.

**38.** If $\alpha,\beta,\gamma$ are the roots of a monic cubic $x^3+a_2x^2+a_1x+a_0$, then
$$\sum\frac{1}{\alpha} = \frac{\alpha\beta+\beta\gamma+\gamma\alpha}{\alpha\beta\gamma}
= \frac{a_1}{-a_0}, \qquad
\sum\frac{1}{\alpha\beta} = \frac{\alpha+\beta+\gamma}{\alpha\beta\gamma} = \frac{-a_2}{-a_0}, \qquad
\frac{1}{\alpha\beta\gamma} = -\frac{1}{a_0}.$$
Here $a_2 = -6$, $a_1 = 11$, $a_0 = -6$, so
$$\sum\frac1\alpha = \frac{11}{6}, \qquad \sum\frac{1}{\alpha\beta} = \frac{6}{6} = 1, \qquad
\frac{1}{\alpha\beta\gamma} = \frac16.$$
The monic cubic with these elementary symmetric functions is
$$x^3-\frac{11}{6}x^2+x-\frac16.$$
**Check directly from the roots.** The reciprocals are $1, \frac12, \frac13$; their sum is
$\frac{6+3+2}{6} = \frac{11}{6}$, their pairwise products sum to
$\frac12+\frac13+\frac16 = 1$, and their product is $\frac16$. These match the coefficients, so
$$x^3-\frac{11}{6}x^2+x-\frac16 = (x-1)\left(x-\frac12\right)\left(x-\frac13\right).$$
The reversed-coefficient rule $a_3x^3+a_2x^2+a_1x+a_0 \mapsto a_0x^3+a_1x^2+a_2x+a_3$ gives
$-6x^3+11x^2-6x+1$, which is $-6$ times the answer above.
