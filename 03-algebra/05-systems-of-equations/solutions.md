# Systems of Linear Equations — Solutions

> [Tutorial](README.md) · [Exercises](exercises.md)

Every exercise is solved in full. Each solution states the strategy, shows the algebra, and checks the
answer in the original equations.

## Beginner

**1.** *Answer: yes.*

Substitute $x = 3$, $y = -2$ into both equations:

$$
2(3) + 5(-2) = 6 - 10 = -4 \ \checkmark, \qquad 3 - (-2) = 5 \ \checkmark .
$$

Both equations hold, so $(3,-2)$ is a solution. Note that the *order* matters: $(3,-2)$ means $x = 3$,
$y = -2$.

**2.** *Answer: $(2, 3)$.*

The first equation is already solved for $y$, so substitute $y = 2x - 1$ into the second:

$$
3x + 2(2x - 1) = 12
\;\Longrightarrow\;
3x + 4x - 2 = 12
\;\Longrightarrow\;
7x = 14
\;\Longrightarrow\;
x = 2 .
$$

Then $y = 2(2) - 1 = 3$. Check: $3(2) + 2(3) = 12$ and $y = 2x - 1 = 3$. Hence $S = \{(2,3)\}$.

**3.** *Answer: $(3, 4)$.*

From the first equation, $y = 7 - x$. Substitute into the second:

$$
2x - (7 - x) = 2
\;\Longrightarrow\;
3x - 7 = 2
\;\Longrightarrow\;
3x = 9
\;\Longrightarrow\;
x = 3 .
$$

Then $y = 7 - 3 = 4$. Check: $3 + 4 = 7$ and $2(3) - 4 = 2$. *Pitfall:* the minus sign before
$(7 - x)$ must apply to both terms; writing $2x - 7 - x = 2$ instead would give $x = 9$, a wrong answer
that still "looks" consistent.

**4.** *Answer: $(7, 3)$.*

Adding the equations eliminates $y$:

$$
(x + y) + (x - y) = 10 + 4 \;\Longrightarrow\; 2x = 14 \;\Longrightarrow\; x = 7 .
$$

Then $7 + y = 10$ gives $y = 3$. Check both: $7 + 3 = 10$, $7 - 3 = 4$.

**5.** *Answer: $(3, \tfrac72)$.*

The coefficients of $y$ are $+2$ and $-2$, so adding eliminates $y$:

$$
(3x + 2y) + (5x - 2y) = 16 + 8 \;\Longrightarrow\; 8x = 24 \;\Longrightarrow\; x = 3 .
$$

Then $3(3) + 2y = 16$, so $2y = 7$ and $y = \tfrac72$. Check the second equation:
$5(3) - 2\left(\tfrac72\right) = 15 - 7 = 8$. Hence $S = \{(3, \tfrac72)\}$. It is perfectly normal for a
system with integer coefficients to have a fractional solution.

**6.** *Answer: infinitely many; $S = \{(3t,\ 4 - 2t) : t \in \mathbb{R}\}$.*

The second equation is exactly twice the first: $4x + 6y = 2(2x + 3y) = 2 \cdot 12 = 24$. So the second
equation is automatically satisfied whenever the first is, and the solution set is the line
$2x + 3y = 12$.

Solve the first for $y$: $3y = 12 - 2x$, so $y = 4 - \tfrac{2x}{3}$. To avoid fractions, put
$x = 3t$; then $y = 4 - 2t$ and

$$
S = \{(3t,\ 4 - 2t) : t \in \mathbb{R}\}.
$$

Check: $2(3t) + 3(4 - 2t) = 6t + 12 - 6t = 12$ and $4(3t) + 6(4 - 2t) = 12t + 24 - 12t = 24$. Every
solution has this form because every solution satisfies $2x + 3y = 12$, hence lies on the line.

**7.** *Answer: no solution.*

Multiply the first equation by $2$: $6x - 2y = 8$. Subtract the second equation:

$$
(6x - 2y) - (6x - 2y) = 8 - 9 \;\Longrightarrow\; 0 = -1 ,
$$

which is false for every $(x,y)$. Hence $S = \varnothing$. Geometrically both lines have slope $3$
(from $y = 3x - 4$ and $y = 3x - \tfrac92$), so they are parallel and distinct.

**8.** *Answer: $(2, 3)$.*

Multiply the first equation by $2$ so that the $y$-coefficients match:

$$
10x + 4y = 32 .
$$

Subtract the second equation from this:

$$
(10x + 4y) - (3x + 4y) = 32 - 18 \;\Longrightarrow\; 7x = 14 \;\Longrightarrow\; x = 2 .
$$

Then $5(2) + 2y = 16$, so $y = 3$. Check: $10 + 6 = 16$ and $6 + 12 = 18$.

**9.** *Answer: $(2, 0, 4)$.*

From the second equation $x = y + 2$. Substitute into the first and into the third:

$$
(y + 2) + y + z = 6 \;\Longrightarrow\; 2y + z = 4, \qquad y + z = 4 .
$$

Subtracting the second relation from the first gives $y = 0$, hence $z = 4$ and $x = 2$. Check all
three: $2 + 0 + 4 = 6$, $2 - 0 = 2$, $0 + 4 = 4$.

**10.** *Answer: $(1, 1, 1)$.*

Adding the second and third equations eliminates both $y$ and $z$:

$$
(x - y + z) + (x + y - z) = 1 + 1 \;\Longrightarrow\; 2x = 2 \;\Longrightarrow\; x = 1 .
$$

With $x = 1$, the first equation gives $y + z = 2$ and the second gives $-y + z = 0$, i.e. $z = y$.
Hence $2y = 2$, so $y = 1$ and $z = 1$. Check: $1+1+1 = 3$, $1-1+1 = 1$, $1+1-1 = 1$.

**11.** *Answer: $9$ and $6$.*

Let the numbers be $x$ (larger) and $y$ (smaller). The sentences translate to

$$
\begin{cases}
x + y = 15\\
x - y = 3 .
\end{cases}
$$

Adding: $2x = 18$, so $x = 9$. Then $y = 15 - 9 = 6$. Check: $9 + 6 = 15$ and $9 - 6 = 3$. Note that
"sum and difference" systems are always solved instantly by adding and subtracting the two equations.

**12.** *Answer:* the augmented matrix is

$$
\left(\begin{array}{cc|c}
2 & -1 & 4\\
1 & 3 & 9
\end{array}\right),
$$

the coefficient matrix is $\begin{pmatrix}2 & -1\\ 1 & 3\end{pmatrix}$, there are $2$ equations and
$2$ unknowns. The first column belongs to $x$, the second to $y$, and the column after the bar holds the
right-hand sides. The determinant of the coefficient matrix is $2 \cdot 3 - 1 \cdot (-1) = 7 \neq 0$, so
the system has a unique solution (it is $(3,2)$, though the exercise does not ask for it).

## Intermediate

**13.** *Answer: $(6, 6)$.*

Clear denominators first: multiply the first equation by $6$ and the second by $6$:

$$
3x + 2y = 30, \qquad 2x + 3y = 30 .
$$

Subtracting the second from the first gives $x - y = 0$, so $x = y$. Substituting into either equation,
$5x = 30$, hence $x = y = 6$. Check in the originals: $\tfrac62 + \tfrac63 = 3 + 2 = 5$ and
$\tfrac63 + \tfrac62 = 2 + 3 = 5$.

*Remark:* clearing denominators is an application of operation (E2) with $c = 6 \neq 0$, so it does not
change the solution set.

**14.** *Answer: $(1, 2)$.*

Multiply the second equation by $2$ to match the $y$-coefficients:

$$
10x - 4y = 2 .
$$

Adding this to the first equation:

$$
(3x + 4y) + (10x - 4y) = 11 + 2 \;\Longrightarrow\; 13x = 13 \;\Longrightarrow\; x = 1 .
$$

Then $3(1) + 4y = 11$, so $y = 2$. Check: $3 + 8 = 11$ and $5 - 4 = 1$.

**15.** *Answer: infinitely many solutions;
$S = \{(2 + 3t,\ 2t) : t \in \mathbb{R}\}$.*

Check proportionality of the coefficients: $(-6, 9) = -\tfrac32 (4, -6)$, and for the right-hand sides
$-12 = -\tfrac32 \cdot 8$. So the second equation is $-\tfrac32$ times the first, and the two equations
describe the same line. Dividing $4x - 6y = 8$ by $2$ gives the simpler $2x - 3y = 4$.

Solve for $x$: $2x = 4 + 3y$, so $x = 2 + \tfrac{3y}{2}$. Put $y = 2t$ to avoid fractions. Then

$$
S = \{(2 + 3t,\ 2t) : t \in \mathbb{R}\}.
$$

Check in the *second* equation: $-6(2 + 3t) + 9(2t) = -12 - 18t + 18t = -12$. *Pitfall:* if the
right-hand sides had not been in the same ratio, the system would have been inconsistent. Always test the
right-hand sides, not just the coefficients.

**16.** *Answer: $12$ litres of the $25\%$ solution and $18$ litres of the $50\%$ solution.*

Let $x$ be the litres of $25\%$ solution and $y$ the litres of $50\%$ solution. Conserve total volume
and total acid:

$$
\begin{cases}
x + y = 30\\
0.25x + 0.50y = 0.40 \cdot 30 = 12 .
\end{cases}
$$

Substituting $x = 30 - y$ into the second equation:

$$
0.25(30 - y) + 0.50y = 12
\;\Longrightarrow\;
7.5 + 0.25y = 12
\;\Longrightarrow\;
y = 18 .
$$

Then $x = 12$. Check: $12 + 18 = 30$ and $0.25(12) + 0.50(18) = 3 + 9 = 12$, and $12/30 = 0.40$.
*Sanity check:* the target $40\%$ lies $15$ percentage points above $25\%$ but only $10$ below $50\%$,
so the stronger solution must be used in the larger amount — and indeed $18 > 12$.

**17.** *Answer: airspeed $250$ km/h, wind speed $50$ km/h.*

Let $p$ be the airspeed and $w$ the wind speed, both in km/h, with $p > w > 0$. With the wind the ground
speed is $p + w$; against it, $p - w$. Using distance $=$ speed $\times$ time:

$$
\begin{cases}
2(p + w) = 600\\
3(p - w) = 600
\end{cases}
\qquad\Longrightarrow\qquad
\begin{cases}
p + w = 300\\
p - w = 200 .
\end{cases}
$$

Adding: $2p = 500$, so $p = 250$. Subtracting: $2w = 100$, so $w = 50$. Check:
$2(250 + 50) = 600$ and $3(250 - 50) = 600$.

**18.** *Answer: apples $\$2$ per kg, pears $\$3$ per kg.*

Let $a$ be the price of apples and $p$ the price of pears, in dollars per kilogram:

$$
\begin{cases}
2a + 3p = 13\\
4a + p = 11 .
\end{cases}
$$

From the second equation $p = 11 - 4a$. Substituting:

$$
2a + 3(11 - 4a) = 13
\;\Longrightarrow\;
2a + 33 - 12a = 13
\;\Longrightarrow\;
-10a = -20
\;\Longrightarrow\;
a = 2 .
$$

Then $p = 11 - 8 = 3$. Check: $2(2) + 3(3) = 13$ and $4(2) + 3 = 11$.

**19.** *Answer: $(2, -1, 3)$.*

Eliminate $x$ using the first equation. Subtract $3 \times$ (equation 1) from equation 2:

$$
(3x + 2y - z) - 3(x + y + z) = 1 - 12
\;\Longrightarrow\;
-y - 4z = -11
\;\Longrightarrow\;
y + 4z = 11 . \qquad\text{(A)}
$$

Subtract equation 1 from equation 3:

$$
(x - 4y + 2z) - (x + y + z) = 12 - 4
\;\Longrightarrow\;
-5y + z = 8
\;\Longrightarrow\;
z = 8 + 5y . \qquad\text{(B)}
$$

Substituting (B) into (A):

$$
y + 4(8 + 5y) = 11
\;\Longrightarrow\;
y + 32 + 20y = 11
\;\Longrightarrow\;
21y = -21
\;\Longrightarrow\;
y = -1 .
$$

Then $z = 8 - 5 = 3$ and $x = 4 - y - z = 4 + 1 - 3 = 2$. Check:
$2 - 1 + 3 = 4$; $3(2) + 2(-1) - 3 = 1$; $2 - 4(-1) + 2(3) = 12$.

**20.** *Answer: $(1, 2, 1)$.*

Solve the second equation for $x$: $x = 1 + y - 2z$. Substitute into the first and third:

$$
2(1 + y - 2z) + y - z = 3
\;\Longrightarrow\;
3y - 5z = 1, \qquad\text{(A)}
$$

$$
3(1 + y - 2z) + 2y + z = 8
\;\Longrightarrow\;
5y - 5z = 5
\;\Longrightarrow\;
y - z = 1 . \qquad\text{(B)}
$$

From (B), $y = z + 1$. Substituting into (A):

$$
3(z + 1) - 5z = 1
\;\Longrightarrow\;
-2z + 3 = 1
\;\Longrightarrow\;
z = 1 .
$$

Then $y = 2$ and $x = 1 + 2 - 2 = 1$. Check: $2 + 2 - 1 = 3$; $1 - 2 + 2 = 1$; $3 + 4 + 1 = 8$.

**21.** *Answer:*
*(a) if $k \neq \pm 1$, exactly one solution
$\left(\dfrac{3}{k+1}, \dfrac{3}{k+1}\right)$;*
*(b) if $k = -1$, no solution;*
*(c) if $k = 1$, infinitely many solutions, namely $\{(t, 3 - t) : t \in \mathbb{R}\}$.*

The determinant is $D = k \cdot k - 1 \cdot 1 = k^2 - 1 = (k-1)(k+1)$.

*Case $k \neq \pm 1$.* Then $D \neq 0$ and Theorem 8.1 of the tutorial gives a unique solution.
Subtracting the second equation from the first:

$$
(k - 1)x + (1 - k)y = 0
\;\Longrightarrow\;
(k - 1)(x - y) = 0 .
$$

Since $k \neq 1$, we may divide by $k - 1$ — this is legitimate *only* because $k \neq 1$ — to get
$x = y$. Then the first equation reads $(k+1)x = 3$, and since $k \neq -1$, $x = \dfrac{3}{k+1}$. Hence
$S = \left\{\left(\dfrac{3}{k+1}, \dfrac{3}{k+1}\right)\right\}$.

*Case $k = 1$.* Both equations read $x + y = 3$, so $S = \{(t, 3 - t) : t \in \mathbb{R}\}$.

*Case $k = -1$.* The system is $-x + y = 3$ and $x - y = 3$. Adding gives $0 = 6$, so $S = \varnothing$.

*Remark on method.* Dividing by $k - 1$ without discussing $k = 1$ would lose the infinite family; this
is the classic error with parameters (see §11 of the tutorial, mistake 4).

**22.** *Answer: $(-4, 3, -1)$, with $\operatorname{rank} A = 3$ and no free parameters.*

$$
\left(\begin{array}{ccc|c}
1 & 2 & 1 & 1\\
2 & 5 & 3 & 4\\
1 & 1 & -1 & 0
\end{array}\right)
\xrightarrow{R_2 \leftarrow R_2 - 2R_1}
\left(\begin{array}{ccc|c}
1 & 2 & 1 & 1\\
0 & 1 & 1 & 2\\
1 & 1 & -1 & 0
\end{array}\right)
$$

$$
\xrightarrow{R_3 \leftarrow R_3 - R_1}
\left(\begin{array}{ccc|c}
1 & 2 & 1 & 1\\
0 & 1 & 1 & 2\\
0 & -1 & -2 & -1
\end{array}\right)
\xrightarrow{R_3 \leftarrow R_3 + R_2}
\left(\begin{array}{ccc|c}
1 & 2 & 1 & 1\\
0 & 1 & 1 & 2\\
0 & 0 & -1 & 1
\end{array}\right).
$$

The last row gives $-z = 1$, so $z = -1$. The second row gives $y + z = 2$, so $y = 3$. The first gives
$x + 2y + z = 1$, so $x = 1 - 6 + 1 = -4$.

Check: $2(-4) + 5(3) + 3(-1) = -8 + 15 - 3 = 4$; $(-4) + 3 - (-1) = 0$.

The echelon form has three pivots, so $\operatorname{rank} A = 3 = n$ and there are $0$ free parameters
(Theorem 7.3).

## Advanced

**23.** *Proof.*

Let the system be

$$
a_1x + b_1y = c_1, \qquad a_2x + b_2y = c_2 ,
$$

and let $(x_1,y_1)$ and $(x_2,y_2)$ be solutions. Fix $t \in \mathbb{R}$ and put

$$
x(t) = x_1 + t(x_2 - x_1), \qquad y(t) = y_1 + t(y_2 - y_1).
$$

For the first equation,

$$
\begin{aligned}
a_1x(t) + b_1y(t)
&= a_1x_1 + b_1y_1 + t\bigl[a_1(x_2 - x_1) + b_1(y_2 - y_1)\bigr]\\
&= c_1 + t\bigl[(a_1x_2 + b_1y_2) - (a_1x_1 + b_1y_1)\bigr]\\
&= c_1 + t\,(c_1 - c_1) = c_1 .
\end{aligned}
$$

The same computation with the index $2$ shows that the second equation holds. Hence $(x(t), y(t))$ is a
solution for every $t$.

It remains to show that distinct $t$ give distinct points. If $(x(t), y(t)) = (x(s), y(s))$, then
$(t - s)(x_2 - x_1) = 0$ and $(t - s)(y_2 - y_1) = 0$. Since $(x_1,y_1) \neq (x_2,y_2)$, at least one of
$x_2 - x_1$, $y_2 - y_1$ is nonzero, so $t = s$. Therefore $t \mapsto (x(t), y(t))$ is injective and the
solution set is infinite. $\blacksquare$

*Interpretation:* the solution set contains the whole line through any two of its points. This is the
geometry behind Theorem 7.2 of the tutorial.

**24.** *Answer: one example of each.*

*Consistent:*

$$
\begin{cases}
x + y = 2\\
x - y = 0\\
2x = 2 .
\end{cases}
$$

The third equation is the sum of the first two, so it adds no constraint; the solution is $(1,1)$.

*Inconsistent, with the same left-hand sides:*

$$
\begin{cases}
x + y = 2\\
x - y = 0\\
2x = 3 .
\end{cases}
$$

The first two equations force $x = 1$, but the third demands $x = \tfrac32$; no tuple satisfies all
three. Equivalently, adding the first two equations gives $2x = 2$, contradicting $2x = 3$.

*Why more equations than unknowns is not fatal:* extra equations may be **linear combinations** of the
others, in which case they are automatically satisfied. Consistency fails only when the right-hand sides
are inconsistent with those same combinations — which is exactly the rank criterion of Theorem 7.3.

**25.** *Answer: $m = 10$.*

The left-hand sides satisfy $(4, 6) = 2(2, 3)$, so the determinant is $2 \cdot 6 - 4 \cdot 3 = 0$ and the
system never has a unique solution. If $m = 2 \cdot 5 = 10$, the second equation is exactly twice the
first; the solution set is the line $2x + 3y = 5$, i.e.
$\{(3t, \tfrac{5 - 6t}{3}) : t \in \mathbb{R}\}$ — infinitely many solutions.

If $m \neq 10$, multiplying the first equation by $2$ gives $4x + 6y = 10$, which contradicts
$4x + 6y = m$; the system is inconsistent.

**26.** *Proof that the system is inconsistent.*

The coefficient matrix and augmented matrix are

$$
A = \begin{pmatrix} 1 & 1\\ 2 & 2\\ 3 & -1\end{pmatrix},
\qquad
[A \mid b] = \left(\begin{array}{cc|c} 1 & 1 & 2\\ 2 & 2 & 5\\ 3 & -1 & 0\end{array}\right).
$$

For $A$: the second row is twice the first, but the first and third rows are independent since
$1 \cdot (-1) - 3 \cdot 1 = -4 \neq 0$. Hence $\operatorname{rank} A = 2$.

For $[A \mid b]$: apply $R_2 \leftarrow R_2 - 2R_1$ to get the row $(0, 0 \mid 1)$, which is a pivot in
the right-hand column. The three rows are therefore independent (the first and third span the first two
coordinates, and the second produces a new pivot), so $\operatorname{rank}[A \mid b] = 3$.

Since $2 = \operatorname{rank} A \neq \operatorname{rank}[A \mid b] = 3$, Theorem 7.3 says the system is
inconsistent. Directly: the first two equations give $x + y = 2$ and $2(x+y) = 5$, i.e. $x + y = 2.5$,
a contradiction. $\blacksquare$

**27.** *Answer: $S = \{(2 - t,\ 1,\ t) : t \in \mathbb{R}\}$; the three planes share the line through
$(2,1,0)$ and $(1,1,1)$.*

The second equation is exactly twice the first ($2x + 4y + 2z = 2 \cdot 4 = 8$), so it carries no extra
information and may be deleted. Subtracting the first equation from the third:

$$
(x - y + z) - (x + 2y + z) = 1 - 4
\;\Longrightarrow\;
-3y = -3
\;\Longrightarrow\;
y = 1 .
$$

Then the first equation gives $x + z = 2$, i.e. $x = 2 - z$. With the parameter $t = z$,

$$
S = \{(2 - t,\ 1,\ t) : t \in \mathbb{R}\}.
$$

Check in the third equation: $(2 - t) - 1 + t = 1$. Here $n = 3$, $\operatorname{rank} A = 2$, so
Theorem 7.3 predicts $3 - 2 = 1$ free parameter, as found.

**28.** *Proof.*

Let the system be $E_1, \dots, E_m$ with solution set $S$, and let $S'$ be the solution set after one
operation.

*(E1) Exchange two equations.* "Satisfies every equation in the list" is a condition on the set of
equations, not on their order, so $S' = S$.

*(E2) Multiply equation $i$ by $c \neq 0$.* If a tuple satisfies every $E_j$, it satisfies $cE_i$
because a true equality may be multiplied by any number. Conversely, if it satisfies every equation of
the new system, then in particular $cE_i$ holds; multiplying by $1/c$ (legitimate since $c \neq 0$) gives
$E_i$. The other equations are unchanged, so $S' = S$.

*(E3) Replace $E_2$ by $E_2 + cE_1$.* Suppose a tuple satisfies $E_1$ and $E_2$. Adding the true
equalities $E_2$ and $c \cdot E_1$ gives a true equality, so $E_2 + cE_1$ holds; hence the tuple is in
$S'$. Conversely, suppose it satisfies $E_1$ and $E_2 + cE_1$. Since $E_1$ holds, $cE_1$ holds;
subtracting it from $E_2 + cE_1$ gives $E_2$. So the tuple is in $S$. Therefore $S' = S$.
$\blacksquare$

*Note.* The hypothesis $c \neq 0$ in (E2) is essential: multiplying by $0$ turns $E_i$ into $0 = 0$,
which is satisfied by every tuple, and the solution set can only grow.

**29.** *Proof.*

*Existence.* Define

$$
x_0 = \frac{c_1b_2 - c_2b_1}{D}, \qquad y_0 = \frac{a_1c_2 - a_2c_1}{D},
\qquad D = a_1b_2 - a_2b_1 \neq 0 .
$$

Then

$$
\begin{aligned}
a_1x_0 + b_1y_0
&= \frac{a_1(c_1b_2 - c_2b_1) + b_1(a_1c_2 - a_2c_1)}{D}\\
&= \frac{a_1b_2c_1 - a_1b_1c_2 + a_1b_1c_2 - a_2b_1c_1}{D}
= \frac{c_1(a_1b_2 - a_2b_1)}{D} = c_1 .
\end{aligned}
$$

The verification of the second equation is identical with the indices exchanged (or note that
$a_2x_0 + b_2y_0$ is the same expression with $1$ and $2$ swapped, giving $c_2$). So a solution exists.

*Uniqueness.* Let $(x,y)$ and $(x',y')$ be solutions and set $\Delta x = x - x'$,
$\Delta y = y - y'$. Subtracting gives

$$
a_1\Delta x + b_1\Delta y = 0, \qquad a_2\Delta x + b_2\Delta y = 0 .
$$

Multiply the first by $b_2$ and the second by $b_1$ and subtract:
$(a_1b_2 - a_2b_1)\Delta x = 0$, so $D\Delta x = 0$ and $\Delta x = 0$. Similarly, multiplying the first
by $a_2$ and the second by $a_1$ and subtracting gives $(a_2b_1 - a_1b_2)\Delta y = 0$, so
$\Delta y = 0$. Hence $(x,y) = (x',y')$.

*Converse.* If $D = 0$ we must exhibit either no solution or more than one. Since not all coefficients
of the first equation vanish, say $(a_1,b_1) \neq (0,0)$. Then $(a_2,b_2) = \lambda(a_1,b_1)$: if
$a_1 \neq 0$ take $\lambda = a_2/a_1$, and $D = 0$ gives $b_2 = a_2b_1/a_1 = \lambda b_1$; if $a_1 = 0$
then $b_1 \neq 0$ and $D = -a_2b_1 = 0$ forces $a_2 = 0$, so take $\lambda = b_2/b_1$. If
$c_2 = \lambda c_1$ the two equations are the same and every solution of the first is a solution of the
system, so there are infinitely many; otherwise $0 = c_2 - \lambda c_1 \neq 0$ is a contradiction and
there are none. So $D = 0$ never gives a unique solution. $\blacksquare$

**30.** *Answer: $\$2000$ at $3\%$ and $\$3000$ at $5\%$.*

Let $x$ and $y$ be the amounts in dollars. Then

$$
\begin{cases}
x + y = 5000\\
0.03x + 0.05y = 210 .
\end{cases}
$$

Substituting $y = 5000 - x$:

$$
0.03x + 0.05(5000 - x) = 210
\;\Longrightarrow\;
0.03x + 250 - 0.05x = 210
\;\Longrightarrow\;
-0.02x = -40
\;\Longrightarrow\;
x = 2000 .
$$

Then $y = 3000$. Check: $0.03(2000) + 0.05(3000) = 60 + 150 = 210$.

*Alternative reasoning:* if the whole $\$5000$ earned $3\%$, the interest would be $\$150$. Each dollar
moved to the $5\%$ account adds $2$ cents, and the extra interest is $\$60$, so $6000$ cents' worth of
moves are needed — that is, $\$3000$ moved. Same answer, no algebra.

## Challenge

**31.** *Answer: $48$.*

Let the tens digit be $a$ and the units digit be $b$, with $a \in \{1,\dots,9\}$ and
$b \in \{0,\dots,9\}$. The number is $10a + b$; the reversed number is $10b + a$. The two conditions are

$$
\begin{cases}
a + b = 12\\
(10b + a) - (10a + b) = 36 .
\end{cases}
$$

Simplify the second: $9b - 9a = 36$, i.e. $b - a = 4$. Adding this to $a + b = 12$ gives $2b = 16$, so
$b = 8$ and $a = 4$. The number is $48$; check $84 - 48 = 36$.

*Note.* The condition $b - a = 4$ is equivalent to "the digits differ by $4$", which is the natural way
to see that $48$ is the answer; the algebra merely justifies it.

**32.** *Answer:*

* if $a \notin \{1, -2\}$:
$S = \left\{\left(-\dfrac{a+1}{a+2},\ \dfrac{1}{a+2},\ \dfrac{(a+1)^2}{a+2}\right)\right\}$;
* if $a = 1$: $S = \{(1 - s - t,\ s,\ t) : s, t \in \mathbb{R}\}$, a plane;
* if $a = -2$: $S = \varnothing$.

*Derivation.* Subtract the second equation from the first:

$$
(a - 1)x + (1 - a)y = 1 - a
\;\Longrightarrow\;
(a - 1)(x - y) = 1 - a = -(a - 1).
$$

If $a \neq 1$, divide by $a - 1 \neq 0$: $x - y = -1$, i.e. $y = x + 1$.

Subtract the third equation from the first:

$$
(a - 1)x + (1 - a)z = 1 - a^2 = (1 - a)(1 + a)
\;\Longrightarrow\;
(a - 1)(x - z) = (1 - a)(1 + a).
$$

For $a \neq 1$ this gives $x - z = -(1 + a)$, i.e. $z = x + 1 + a$.

Substituting $y = x + 1$ and $z = x + 1 + a$ into the first equation:

$$
ax + (x + 1) + (x + 1 + a) = 1
\;\Longrightarrow\;
(a + 2)x + (a + 2) = 1
\;\Longrightarrow\;
(a + 2)x = -(a + 1).
$$

If $a \neq -2$, $x = -\dfrac{a+1}{a+2}$, and then

$$
y = x + 1 = \frac{-(a+1) + (a+2)}{a+2} = \frac{1}{a+2},
\qquad
z = x + 1 + a = \frac{(a+1)^2}{a+2}.
$$

*Exceptional case $a = 1$.* All three equations become $x + y + z = 1$, so the solution set is the plane
$\{(1 - s - t,\ s,\ t)\}$.

*Exceptional case $a = -2$.* Adding the three equations gives $(a + 2)(x + y + z) = 1 + a + a^2$, i.e.
$0 = 1 - 2 + 4 = 3$, which is impossible; so $S = \varnothing$.

*Check with $a = 3$:* the formula gives $x = -\tfrac45$, $y = \tfrac15$, $z = \tfrac{16}{5}$. Substituting
into the first equation: $3\left(-\tfrac45\right) + \tfrac15 + \tfrac{16}{5} = \tfrac{-12 + 1 + 16}{5} = 1$
✓. This matches a direct solve of the system with $a = 3$.

**33.** *Answer: A alone $30$ days, B alone $20$ days, C alone $60$ days.*

Let $u, v, w$ be the rates of A, B, C in jobs per day, so that a worker who needs $d$ days alone has rate
$1/d$. "A and B together finish in $12$ days" means their combined rate is $\tfrac{1}{12}$:

$$
u + v = \frac{1}{12}, \qquad v + w = \frac{1}{15}, \qquad u + w = \frac{1}{20}.
$$

This is a linear system in $u, v, w$. Add all three equations:

$$
2(u + v + w) = \frac{1}{12} + \frac{1}{15} + \frac{1}{20} = \frac{5 + 4 + 3}{60} = \frac{12}{60} = \frac15,
$$

so $u + v + w = \tfrac{1}{10}$. Then

$$
u = \frac{1}{10} - (v + w) = \frac{1}{10} - \frac{1}{15} = \frac{3 - 2}{30} = \frac{1}{30},
$$

$$
v = \frac{1}{10} - (u + w) = \frac{1}{10} - \frac{1}{20} = \frac{1}{20},
\qquad
w = \frac{1}{10} - (u + v) = \frac{1}{10} - \frac{1}{12} = \frac{1}{60}.
$$

Hence A needs $30$ days, B needs $20$ days, C needs $60$ days. Check: $u + v = \tfrac{1}{30} + \tfrac{1}{20}
= \tfrac{2 + 3}{60} = \tfrac{1}{12}$ ✓; $v + w = \tfrac{1}{20} + \tfrac{1}{60} = \tfrac{4}{60} =
\tfrac{1}{15}$ ✓; $u + w = \tfrac{1}{30} + \tfrac{1}{60} = \tfrac{3}{60} = \tfrac{1}{20}$ ✓.

*Remark.* The system is linear in the *reciprocals* — a "linear system in disguise". The substitution
$u = 1/a$ is legitimate because the rates are positive, so no solutions are lost.

**34.** *(a) Redundancy. (b) $S = \left\{\left(7 - \tfrac{3t}{2},\ 3 + \tfrac{t}{2},\ t\right) : t \in
\mathbb{R}\right\}$. (c) $(7,3,0)$, $(4,4,2)$, $(1,5,4)$.*

*(a)* Add the first two equations:

$$
(x + y + z) + (x - y + 2z) = 10 + 4 \;\Longrightarrow\; 2x + 3z = 14,
$$

which is exactly the third equation. So every solution of the first two satisfies the third, and the
third may be deleted.

*(b)* From the first equation, $y = 10 - x - z$. Substituting into the second:

$$
x - (10 - x - z) + 2z = 4
\;\Longrightarrow\;
2x + 3z = 14
\;\Longrightarrow\;
x = 7 - \frac{3z}{2}.
$$

Then

$$
y = 10 - \left(7 - \frac{3z}{2}\right) - z = 3 + \frac{z}{2}.
$$

With $z = t$, the solution set is
$\{(7 - \tfrac{3t}{2},\ 3 + \tfrac{t}{2},\ t) : t \in \mathbb{R}\}$. Check in the second equation:
$\left(7 - \tfrac{3t}{2}\right) - \left(3 + \tfrac{t}{2}\right) + 2t = 4 - 2t + 2t = 4$ ✓.

*(c)* Non-negativity requires

$$
7 - \frac{3t}{2} \geq 0 \ \Longrightarrow\ t \leq \frac{14}{3}, \qquad
3 + \frac{t}{2} \geq 0 \ \Longrightarrow\ t \geq -6, \qquad t \geq 0 .
$$

So $0 \leq t \leq \tfrac{14}{3}$. For $z = t$ to be an integer, $t$ must be an integer; for
$x = 7 - \tfrac{3t}{2}$ to be an integer, $t$ must be even. Hence $t \in \{0, 2, 4\}$, giving

$$
t = 0: (7, 3, 0), \qquad t = 2: (4, 4, 2), \qquad t = 4: (1, 5, 4).
$$

Each satisfies the system and has non-negative integer entries. The bound $t \leq \tfrac{14}{3}$ excludes
$t = 6$, where $x = 7 - 9 = -2 < 0$.

**35.** *(a) $x + y + z = 100$ and $0.1x + 0.3y + 0.5z = 26$.
(b) $S = \{(20 + t,\ 80 - 2t,\ t) : 0 \leq t \leq 40\}$.
(c) $40$ kg of the $10\%$ alloy, $40$ kg of the $30\%$ alloy, and $20$ kg of the $50\%$ alloy.*

*(a)* Total mass: $x + y + z = 100$. Total copper: $0.1x + 0.3y + 0.5z = 0.26 \cdot 100 = 26$.

*(b)* Multiplying the copper equation by $10$ gives $x + 3y + 5z = 260$. Subtracting the mass equation:

$$
(x + 3y + 5z) - (x + y + z) = 260 - 100
\;\Longrightarrow\;
2y + 4z = 160
\;\Longrightarrow\;
y = 80 - 2z .
$$

Then $x = 100 - y - z = 100 - 80 + 2z - z = 20 + z$. With $z = t$,

$$
(x, y, z) = (20 + t,\ 80 - 2t,\ t).
$$

The masses must be non-negative: $t \geq 0$; $80 - 2t \geq 0$ gives $t \leq 40$; and $20 + t \geq 0$ holds
automatically. Hence $0 \leq t \leq 40$, a one-parameter family of recipes — the two constraints cannot
pin down three masses.

*(c)* Setting $x = y$:

$$
20 + t = 80 - 2t
\;\Longrightarrow\;
3t = 60
\;\Longrightarrow\;
t = 20,
$$

so $(x, y, z) = (40, 40, 20)$. Check the copper content:
$0.1(40) + 0.3(40) + 0.5(20) = 4 + 12 + 10 = 26$, and the mass is $100$ kg. The blend is $26\%$ copper ✓.

*Remark.* Uniqueness would require a third independent constraint — for instance a cost condition. The
existence of a whole interval of feasible answers is the typical situation in blending problems, and it
is exactly what Theorem 7.3 quantifies: $n - r = 3 - 2 = 1$ free parameter.
