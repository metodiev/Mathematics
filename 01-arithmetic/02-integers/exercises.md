# Integers and Negative Numbers — Exercises

> Companion to [the tutorial](README.md). Attempt every problem before opening
> [the solutions](solutions.md).

Thirty-five problems, numbered continuously and grouped by difficulty. Problems marked with a star
($\star$) are longer; none requires ideas beyond the tutorial.

## Beginner

**1.** Arrange the integers $-3,\ 5,\ -7,\ 0,\ 2,\ -1$ in increasing order. Then state which of them
have the same absolute value as another number in the list, if any.

**2.** Compute: (a) $|-8|$; (b) $|12|$; (c) $|0|$; (d) $-|-5|$; (e) $|-5| + |3|$.

**3.** Find the distance between (a) $-4$ and $7$; (b) $-9$ and $-2$; (c) $6$ and $6$.

**4.** Compute: (a) $-7 + 3$; (b) $-5 + (-9)$; (c) $8 + (-14)$; (d) $-6 + 6$.

**5.** Compute: (a) $4 - 9$; (b) $-3 - 7$; (c) $-5 - (-8)$; (d) $2 - (-6)$.

**6.** Compute: (a) $(-6)(7)$; (b) $(-4)(-9)$; (c) $8 \div (-2)$; (d) $-45 \div (-5)$.

**7.** Compute: (a) $(-2)^5$; (b) $(-3)^3$; (c) $(-1)^{100}$; (d) $-5^2$; (e) $(-5)^2$.

**8.** Evaluate, respecting the order of operations: (a) $6 - 3 \cdot 4$; (b) $-2 + 4 \cdot (-3)$;
(c) $20 \div (-4) + 3$.

**9.** Evaluate: (a) $2 - (3 - 8)$; (b) $-(4 - 9) + 2$.

**10.** The temperature at noon is $3$ °C and then drops by $10$ °C. What is the new temperature?
Later in the week the temperature is $-8$ °C and rises by $13$ °C. What is it then?

**11.** A bank account holds \$45. A withdrawal of \$80 is made. What is the balance, and what does
the sign of the answer mean in words?

**12.** A diver is at $-18$ m relative to the surface and rises $7$ m. A hiker is at $1200$ m above
sea level and descends $1500$ m. Give both final elevations relative to sea level.

## Intermediate

**13.** Simplify $-3 + 7 - 5 + 2 - 8$ by converting every subtraction to addition and then grouping
the positive and the negative terms.

**14.** Evaluate $(-2)^3 \cdot (-3)^2 - (-4)$.

**15.** Evaluate

$$
\dfrac{(-6)(-4)}{-3} + \dfrac{18}{-6}.
$$

**16.** Evaluate $(-5)^2 - 3(7 - 12) \div (-3)$.

**17.** Evaluate $-(2 - 6)^2 + (-3)^3 \div 9$.

**18.** Evaluate $a^2b - ab^2$ at $a = -2$ and $b = 6$. Check your answer by factoring the expression
first.

**19.** Without computing either product, decide which is larger: $-7 \cdot 12$ or $-7 \cdot 11$.
Justify the decision using a property of order from the tutorial, then confirm by computing.

**20.** Find integers $q$ and $r$ with $-47 = 6q + r$ and $0 \le r < 6$. Then give the quotient and
remainder that a C program would report for `-47 / 6` and `-47 % 6`.

**21.** Complete the table of multiples of $-5$ and use the pattern to deduce the missing entries.

| $n$ | $4$ | $3$ | $2$ | $1$ | $0$ | $-1$ | $-2$ | $-3$ |
|---|---|---|---|---|---|---|---|---|
| $n \cdot (-5)$ | $-20$ | $-15$ | $-10$ | $-5$ | $0$ | ? | ? | ? |

State the general rule the table illustrates, and explain in one sentence why the pattern cannot
continue in any other way.

**22.** Say whether each statement is true or false, giving a proof or a counterexample.

(a) $-a$ is always negative.
(b) $|a| = |-a|$ for every integer $a$.
(c) If $a < b$ then $a^2 < b^2$.
(d) $|a + b| = |a| + |b|$ for all integers $a$ and $b$.

**23.** A submarine is at $-120$ m. It descends $35$ m and then rises at a constant $12$ m per minute
for $5$ minutes. What is its final depth?

**24.** An account holds \$250. Three debits are made, of \$90, \$90 and \$150, followed by a deposit
of \$60. What is the balance? If the bank then charges an overdraft fee of \$35, what is the final
balance?

## Advanced

**25.** Using axioms (Z1)–(Z7) only, prove that $0 \cdot a = 0$ for every integer $a$. Name each
axiom at the step where you use it.

**26.** Prove that $(-a)b = -(ab)$ for all integers $a, b$, and deduce that $(-a)(-b) = ab$.

**27.** Prove that $(-1)(-1) = 1$, using only distributivity, the existence of additive inverses and
the identity $0 \cdot a = 0$. Then explain in two or three sentences what breaks if one assumes
instead that $(-1)(-1) = -1$.

**28.** (a) Prove that if $n$ is odd then $n^2$ is odd. (b) Prove that $n^2 + n$ is even for every
integer $n$.

**29.** (a) Prove that $|ab| = |a|\,|b|$ for all integers $a, b$. (b) Prove that if $a < b$ and
$c < 0$ then $ac > bc$.

**30.** Prove the triangle inequality $|a + b| \le |a| + |b|$ for all integers $a, b$, and determine
exactly when equality holds.

**31.** $\star$ (a) Prove that the product of any two consecutive integers is even. (b) Prove that
the product of any three consecutive integers is divisible by $6$. (Hint for (b): one of the three
factors leaves remainder $0$ on division by $3$; use also part (a) and the fact that a number
divisible by $2$ and by $3$ is divisible by $6$.)

**32.** An 8-bit two's complement integer type represents the values $-128$ to $127$.

(a) Compute $100 + 50$ in this type.
(b) Compute $-120 - 20$ in this type.
(c) Explain why $127 + 1$ yields $-128$.
(d) Explain why the expression $-(-128)$ cannot produce a correct result in this type.

## Challenge

**33.** Prove that there are no nonzero integers $a$ and $b$ satisfying $a^2 = 2b^2$. Structure the
proof as an argument by contradiction with an infinite descent on $|b|$. (This is the arithmetic
heart of the classical proof that $\sqrt{2}$ is irrational.)

**34.** Find all pairs of integers $(a, b)$ satisfying $a^2 - b^2 = 12$. Justify that your list is
complete, and verify each pair.

**35.** Using division with remainder by $4$, prove that among any five integers there are always two
whose difference is divisible by $4$. Then give an explicit example of five integers that *does not*
have the same property for division by $5$.
