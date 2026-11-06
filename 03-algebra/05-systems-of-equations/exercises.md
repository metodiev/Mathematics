# Systems of Linear Equations — Exercises

> [Tutorial](README.md) · [Solutions](solutions.md) · Level: Intermediate

Thirty-five problems, numbered continuously. Work through them in order; the levels are cumulative, not
independent.

**How to use this set.**

* Attempt each problem on paper before opening [solutions.md](solutions.md). Reading a solution feels
  like learning and is not.
* For every system, **check your answer in the original equations**. Checking is part of the problem,
  not an optional extra.
* When a solution set is infinite, an answer is only complete when it is written as a parametrised
  family, e.g. $\{(2 - t,\ 1,\ t) : t \in \mathbb{R}\}$, together with the statement that every solution
  has that form.
* Problems that ask for a proof should be answered in complete sentences, naming every theorem used.
* Unless stated otherwise, all variables range over $\mathbb{R}$.

## Beginner

**1.** Decide whether $(3, -2)$ is a solution of the system

$$
\begin{cases}
2x + 5y = -4\\
x - y = 5 .
\end{cases}
$$

**2.** Solve by substitution:

$$
\begin{cases}
y = 2x - 1\\
3x + 2y = 12 .
\end{cases}
$$

**3.** Solve by substitution:

$$
\begin{cases}
x + y = 7\\
2x - y = 2 .
\end{cases}
$$

**4.** Solve by elimination:

$$
\begin{cases}
x + y = 10\\
x - y = 4 .
\end{cases}
$$

**5.** Solve by elimination:

$$
\begin{cases}
3x + 2y = 16\\
5x - 2y = 8 .
\end{cases}
$$

**6.** Solve, or explain why there is no unique solution:

$$
\begin{cases}
2x + 3y = 12\\
4x + 6y = 24 .
\end{cases}
$$

**7.** Solve, or explain why there is no solution:

$$
\begin{cases}
3x - y = 4\\
6x - 2y = 9 .
\end{cases}
$$

**8.** Solve:

$$
\begin{cases}
5x + 2y = 16\\
3x + 4y = 18 .
\end{cases}
$$

**9.** Solve the system in three unknowns:

$$
\begin{cases}
x + y + z = 6\\
x - y = 2\\
y + z = 4 .
\end{cases}
$$

**10.** Solve:

$$
\begin{cases}
x + y + z = 3\\
x - y + z = 1\\
x + y - z = 1 .
\end{cases}
$$

**11.** The sum of two numbers is $15$ and their difference is $3$. Set up a system, solve it, and
identify the two numbers.

**12.** Write the augmented matrix of the system

$$
\begin{cases}
2x - y = 4\\
x + 3y = 9 .
\end{cases}
$$

State the coefficient matrix, the number of equations, and the number of unknowns.

## Intermediate

**13.** Solve:

$$
\begin{cases}
\dfrac{x}{2} + \dfrac{y}{3} = 5\\[6pt]
\dfrac{x}{3} + \dfrac{y}{2} = 5 .
\end{cases}
$$

**14.** Solve:

$$
\begin{cases}
3x + 4y = 11\\
5x - 2y = 1 .
\end{cases}
$$

**15.** Classify the system as having one solution, no solution, or infinitely many; if it has
infinitely many, give the general solution with a parameter:

$$
\begin{cases}
4x - 6y = 8\\
-6x + 9y = -12 .
\end{cases}
$$

**16.** How many litres of a $25\%$ acid solution and of a $50\%$ acid solution are needed to make
$30$ litres of a $40\%$ solution?

**17.** A light aircraft flies $600$ km with a tailwind in $2$ hours and makes the return trip against
the same wind in $3$ hours. Find the aircraft's airspeed and the wind speed.

**18.** Two kilograms of apples and three kilograms of pears cost $\$13$, while four kilograms of apples
and one kilogram of pears cost $\$11$. Find the price per kilogram of each fruit.

**19.** Solve:

$$
\begin{cases}
x + y + z = 4\\
3x + 2y - z = 1\\
x - 4y + 2z = 12 .
\end{cases}
$$

**20.** Solve:

$$
\begin{cases}
2x + y - z = 3\\
x - y + 2z = 1\\
3x + 2y + z = 8 .
\end{cases}
$$

**21.** For which values of the real parameter $k$ does the system

$$
\begin{cases}
kx + y = 3\\
x + ky = 3
\end{cases}
$$

have (a) exactly one solution, (b) no solution, (c) infinitely many solutions? Give the solution set in
each case.

**22.** Carry out row reduction on the augmented matrix

$$
\left(\begin{array}{ccc|c}
1 & 2 & 1 & 1\\
2 & 5 & 3 & 4\\
1 & 1 & -1 & 0
\end{array}\right)
$$

and read off the solution. State the rank of the coefficient matrix and the number of free parameters.

## Advanced

**23.** Let $(x_1, y_1) \neq (x_2, y_2)$ be two solutions of a $2 \times 2$ linear system. Prove that for
every real $t$ the point
$\bigl(x_1 + t(x_2 - x_1),\; y_1 + t(y_2 - y_1)\bigr)$ is also a solution. Deduce that the system has
infinitely many solutions.

**24.** Give an example of a system of **three** equations in **two** unknowns that is consistent, and an
example with the same left-hand sides that is inconsistent. Explain in one sentence why more equations
than unknowns does not by itself force inconsistency.

**25.** Determine the value of $m$ for which

$$
\begin{cases}
2x + 3y = 5\\
4x + 6y = m
\end{cases}
$$

has infinitely many solutions. What happens for other values of $m$?

**26.** Use the rank criterion to show that

$$
\begin{cases}
x + y = 2\\
2x + 2y = 5\\
3x - y = 0
\end{cases}
$$

is inconsistent. Compute both $\operatorname{rank} A$ and $\operatorname{rank}[A \mid b]$ explicitly.

**27.** Solve the system and describe its solution set geometrically:

$$
\begin{cases}
x + 2y + z = 4\\
2x + 4y + 2z = 8\\
x - y + z = 1 .
\end{cases}
$$

**28.** Prove that each of the three elementary operations (exchange two equations; multiply an equation
by a nonzero constant; add a multiple of one equation to another) produces a system with the same
solution set.

**29.** Prove that the system

$$
\begin{cases}
a_1x + b_1y = c_1\\
a_2x + b_2y = c_2
\end{cases}
$$

has exactly one solution if and only if $a_1b_2 - a_2b_1 \neq 0$, and that in that case

$$
x = \frac{c_1b_2 - c_2b_1}{a_1b_2 - a_2b_1}, \qquad
y = \frac{a_1c_2 - a_2c_1}{a_1b_2 - a_2b_1} .
$$

**30.** An investor splits $\$5000$ between two accounts paying $3\%$ and $5\%$ simple interest per year.
The total annual interest is $\$210$. How much is in each account?

## Challenge

**31.** A two-digit number has digits summing to $12$. Reversing the digits increases the number by
$36$. Find the number. (Let the tens digit be $a$ and the units digit be $b$; the number is $10a + b$.)

**32.** For each real value of $a$, solve

$$
\begin{cases}
ax + y + z = 1\\
x + ay + z = a\\
x + y + az = a^2 .
\end{cases}
$$

Your answer must treat the exceptional values of $a$ separately, and must say what the solution set is
in each exceptional case.

**33.** Worker A and worker B together finish a job in $12$ days, B and C together in $15$ days, and
A and C together in $20$ days. How long would each take working alone? (Let $u = 1/a$, $v = 1/b$,
$w = 1/c$ be the rates in jobs per day.)

**34.** Consider

$$
\begin{cases}
x + y + z = 10\\
x - y + 2z = 4\\
2x + 3z = 14 .
\end{cases}
$$

(a) Show that the third equation is a consequence of the first two.

(b) Write the general solution with one parameter.

(c) Find all solutions in which $x, y, z$ are non-negative integers.

**35.** An alloy supplier blends three master alloys containing $10\%$, $30\%$ and $50\%$ copper. A
customer orders $100$ kg of alloy containing $26\%$ copper. Let $x, y, z$ be the masses taken from the
three master alloys.

(a) Write the two equations expressing total mass and copper content.

(b) Show that there are infinitely many feasible blends and describe them with a parameter, including
the range of the parameter for which all three masses are non-negative.

(c) Among the feasible blends, find the one that uses equal masses of the $10\%$ and $30\%$ alloys.
