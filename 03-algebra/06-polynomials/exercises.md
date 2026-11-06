# Polynomials — Exercises

> [Tutorial](README.md) · [Solutions](solutions.md) · Level: Intermediate

Thirty-five problems, numbered continuously. The levels are cumulative: the proofs in the advanced
section use exactly the results practised in the beginner and intermediate sections.

**How to use this set.**

* Attempt each problem before opening [solutions.md](solutions.md).
* **Verify every expansion by expanding back.** Factoring is a search; expansion is a proof. A factorisation
  that has not been re-expanded is only a conjecture.
* For proof problems, write complete sentences and state which theorem each step uses.
* All polynomials have real coefficients unless a problem says otherwise.

## Beginner

**1.** Write $p(x) = 7 - 4x^2 + x^5 - 2x^3$ in standard form and state its degree, its leading
coefficient, and its constant term.

**2.** Write $q(x) = 3x^4 - x + 8 - x^4 + 2x^4$ in standard form and state its degree, its leading
coefficient, and its constant term. (Collect like terms first.)

**3.** Add: $(5x^2 - 3x + 1) + (-2x^2 + 8x - 6)$.

**4.** Subtract: $(x^3 - 4x + 2) - (3x^3 + 2x^2 - 5)$.

**5.** Multiply: $(x - 5)(x + 8)$.

**6.** Multiply: $(4x + 1)(2x - 3)$.

**7.** Expand $(x - 7)^2$.

**8.** Expand $(5x + 2)^2$.

**9.** Expand $(3x - 4)(3x + 4)$.

**10.** Factor $16x^2 - 25y^2$.

**11.** State the end behaviour of $p(x) = 3x^5 - x^2 + 4$: describe $p(x)$ as $x \to -\infty$ and as
$x \to +\infty$.

**12.** Evaluate $p(x) = 2x^3 - 5x^2 + x - 3$ at $x = -1$.

## Intermediate

**13.** Multiply: $(2x^2 - x + 3)(x^2 + 3x - 2)$.

**14.** Expand $(x - 3)^3$.

**15.** Expand $(2x + 1)^3$.

**16.** Factor $x^3 + 64$ and $27x^3 - 8$.

**17.** Divide $8x^3 - 6x^2 - x + 2$ by $2x + 1$, stating the quotient and the remainder.

**18.** Divide $3x^3 + 2x^2 - 4x + 1$ by $x^2 - x + 2$, stating the quotient and the remainder.

**19.** Find the remainder when $x^4 - 3x^3 + 2x - 7$ is divided by $x - 2$.

**20.** Show that $x - 4$ is a factor of $x^3 - 2x^2 - 11x + 12$, and factor the cubic completely.

**21.** Without solving the equation $2x^2 - 7x + 3 = 0$, write down the sum and the product of its
roots. Then factor the quadratic and verify both values.

**22.** Find the monic cubic polynomial whose roots are $-1$, $2$ and $5$. Expand it and verify Vieta's
formulas for your answer.

## Advanced

**23.** Prove that for nonzero polynomials $p$ and $q$ over $\mathbb{R}$,
$\deg(pq) = \deg p + \deg q$. State explicitly where the proof uses the fact that $\mathbb{R}$ has no
zero divisors.

**24.** (a) Prove that a nonzero polynomial of degree $n$ has at most $n$ distinct real roots.

(b) Working modulo $8$ (two integers are identified when their difference is divisible by $8$), show that
$x^2 - 1$ has the four roots $1, 3, 5, 7$. Why does this not contradict part (a)?

**25.** Find $k$ such that $x - 3$ is a factor of $x^3 - kx^2 + 2x - 6$, then factor the polynomial
completely for that value of $k$.

**26.** The remainder when $x^3 + ax^2 - 3x + 5$ is divided by $x + 1$ is $9$. Find $a$.

**27.** Solve $2x^3 + 3x^2 - 11x - 6 = 0$, using the rational root theorem. Verify your roots with
Vieta's formulas.

**28.** Factor completely over $\mathbb{R}$: (a) $x^4 - 16$; (b) $x^4 + 2x^3 - x - 2$.

**29.** Factor $x^6 - 1$ completely over $\mathbb{R}$, using $x^6 - 1 = (x^3 - 1)(x^3 + 1)$ and the sum
and difference of cubes.

**30.** For $p(x) = x^4 - 2x^3 - 3x^2 + 8x - 4$: factor completely, list each root with its
multiplicity, state the sign of $p$ on each interval between consecutive roots, and describe the
behaviour of the graph at each root.

## Challenge

**31.** Prove that if $p$ has real coefficients and $z \in \mathbb{C}$ satisfies $p(z) = 0$, then also
$p(\overline{z}) = 0$. Deduce that a real polynomial of odd degree has at least one real root, and that
the number of non-real roots of any real polynomial is even.

**32.** (a) Prove Sophie Germain's identity

$$
a^4 + 4b^4 = \left(a^2 + 2ab + 2b^2\right)\left(a^2 - 2ab + 2b^2\right).
$$

(b) Use it to factor $x^4 + 4$ and $x^4 + 64$ over $\mathbb{R}$.

**33.** (a) Let $p$ be a polynomial and let $a \neq b$. Prove that the remainder on dividing $p(x)$ by
$(x - a)(x - b)$ is the unique linear polynomial $L$ with $L(a) = p(a)$ and $L(b) = p(b)$.

(b) Use the result to find the remainder when $x^3 - 2x + 1$ is divided by $(x - 1)(x - 2)$, and verify
by carrying out the division.

**34.** Let $p(x) = x^3 - 3x^2 + kx - 1$ have roots $a, b, c$.

(a) Prove that $a^2 + b^2 + c^2 = (a + b + c)^2 - 2(ab + bc + ca)$.

(b) Given that $a^2 + b^2 + c^2 = 7$, find $k$.

**35.** Let $p$ have integer coefficients, and suppose $p(0)$ and $p(1)$ are both odd. Prove that $p$ has
no integer root.
