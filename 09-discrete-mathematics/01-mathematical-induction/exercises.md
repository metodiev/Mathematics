# Mathematical Induction — Exercises

> [Mathematical Induction](README.md) · 36 problems · Beginner → Challenge · Solutions: [solutions.md](solutions.md)

Attempt every problem in writing before looking at [solutions.md](solutions.md). Each problem names the section of the tutorial that supplies the technique, so that a stuck reader knows where to reread.

Notation: $\mathbb{N} = \{1,2,3,\dots\}$, $\mathbb{N}_0 = \{0,1,2,3,\dots\}$; $a \mid b$ means that $b = ak$ for some integer $k$; $\sum_{k=1}^{n} a_k$ is the sum $a_1 + \cdots + a_n$; $F_1 = F_2 = 1$ and $F_n = F_{n-1} + F_{n-2}$ for $n \ge 3$ defines the Fibonacci numbers. Unless a problem says otherwise, a complete solution must state the claim, the base case, the inductive hypothesis, the step and the conclusion.

## Beginner

**1.** *(§7.1)* Prove by induction that for every $n \ge 1$,
$$\sum_{k=1}^{n} (2k-1) = n^2 .$$
Write the proof in the five-part template of Section 7.1, and say explicitly where the inductive hypothesis is used.

**2.** *(§8.2)* Prove by induction that for every $n \ge 1$,
$$\sum_{k=1}^{n} (4k-3) = n(2n-1).$$

**3.** *(§7.3)* Prove by induction that for every $n \ge 1$,
$$\sum_{k=0}^{n-1} 3^k = \frac{3^n - 1}{2}.$$
(Theorem 7.3.1 is the general statement; here you are asked to carry out the proof with the numbers displayed.)

**4.** *(§7.10)* Prove that $3 \mid n^3 - n$ for every integer $n \ge 1$. Compute the first four values of $n^3-n$ and check that each is divisible by $3$ before you start.

**5.** *(§7.10)* Prove that $8 \mid 3^{2n} - 1$ for every integer $n \ge 1$.

**6.** *(§7.9)* Prove that $2^n > n$ for every integer $n \ge 1$.

**7.** *(§8.3)* Prove that for every $n \ge 1$,
$$\sum_{k=1}^{n} \frac{1}{k(k+1)} = \frac{n}{n+1}.$$
Both a direct induction and a telescoping argument are possible; give the induction, then remark on the second method.

**8.** *(§8.5)* Prove by induction that a finite set with $n$ elements has exactly $2^n$ subsets, for every $n \ge 0$. Your proof must explain why the two classes "subsets containing $x$" and "subsets not containing $x$" are disjoint and exhaustive.

**9.** *(§7.9)* Prove that $n! \ge 2^{\,n-1}$ for every integer $n \ge 1$. Determine for which $n$ equality holds.

**10.** *(§7.10)* Prove that $11 \mid 2^{10n} - 1$ for every integer $n \ge 1$. (You may use $2^{10} = 1024 = 11\cdot 93 + 1$.)

**11.** *(§11)* The following "proof" is wrong. Identify the exact error, and explain why the argument still looks convincing.

> **Claim.** For every $n \ge 1$, the number $n^2 + n$ is odd.
>
> **Proof.** Assume that $k^2 + k$ is odd for some $k \ge 1$. Then
> $$(k+1)^2 + (k+1) = k^2 + 2k + 1 + k + 1 = (k^2 + k) + 2(k+1),$$
> which is a sum of an odd number and an even number, hence odd. $\square$

**12.** *(§7.1, §7.9)* Consider the claim: for every integer $n \ge 2$, $\;n^2 \ge 2n$.
(a) Write down the base case, the inductive hypothesis and the goal in the template of Section 7.1.
(b) Complete the proof.
(c) Explain why the same argument fails for the claim $n^2 > 2n$ for every $n \ge 2$.

## Intermediate

**13.** *(§7.3, §8.3)* Prove that for every $n \ge 1$,
$$\sum_{k=1}^{n} k\cdot k! = (n+1)! - 1 .$$
*Hint:* compare $(k+1)!$ with $k\cdot k!$ before you begin.

**14.** *(§7.10)* Prove that $6 \mid n^3 + 5n$ for every integer $n \ge 1$.

**15.** *(§7.9)* (a) Prove by induction that $(1+x)^n \ge 1 + nx$ for every real $x \ge 0$ and every $n \in \mathbb{N}_0$.
(b) Identify the exact line of your proof where the weaker hypothesis $x \ge -1$ suffices, and explain what goes wrong at that line when $x < -1$.
(c) Give a counterexample with $n = 3$ and $x < -1$, showing that the hypothesis $x \ge -1$ cannot be dropped.

**16.** *(§7.9)* Prove that for every $n \ge 1$,
$$\sum_{k=1}^{n} \frac{1}{\sqrt{k}} \ge \sqrt{n}.$$
*Hint for the step:* you will need to show $\sqrt{k} + \dfrac{1}{\sqrt{k+1}} \ge \sqrt{k+1}$; clear denominators and square carefully, or note that $\sqrt{k(k+1)} \ge k$.

**17.** *(§7.3)* Prove that for every $n \ge 1$,
$$\sum_{k=1}^{n} k\,2^{k} = (n-1)2^{\,n+1} + 2 .$$

**18.** *(§7.10)* Let $a$ and $b$ be integers with $a \ne b$. Prove that $a - b$ divides $a^n - b^n$ for every $n \ge 1$.
*Hint:* write $a^{k+1} - b^{k+1} = a(a^k - b^k) + b^k(a-b)$.

**19.** *(§7.11)* Prove that for every $n \ge 1$,
$$F_2 + F_4 + \cdots + F_{2n} = F_{2n+1} - 1 .$$
Check the identity at $n = 1, 2, 3$ before proving it.

**20.** *(§7.5)* Prove that $n^2 < 2^n$ for every integer $n \ge 5$.
*Hint:* the step needs the auxiliary fact $2k + 1 \le 2^k$ for $k \ge 5$; prove that fact by induction as a lemma, or verify it directly and explain why it is enough.

**21.** *(§7.4)* Prove by strong induction that every integer $n \ge 18$ can be written as a sum of $4$s and $7$s. (Repetitions are allowed: $18 = 4 + 7 + 7$.)

**22.** *(§7.4)* Prove by strong induction that every integer $n \ge 1$ can be written as a sum of distinct powers of $2$ (a sum with no repeated summand). This is the existence half of the binary representation theorem; you are not asked to prove uniqueness.

## Advanced

**23.** *(§7.12)* Suppose $n$ lines are drawn in the plane in **general position**: no two are parallel and no three pass through a common point. Prove by induction that the lines divide the plane into
$$R(n) = \frac{n(n+1)}{2} + 1$$
regions. Check $R(0), R(1), R(2), R(3)$ against a sketch.

**24.** *(§7.6, §7.12)* A **tree** is a connected graph with no cycles. Prove that every tree with $n \ge 1$ vertices has exactly $n - 1$ edges. You may use, and should prove, the **leaf lemma**: every tree with at least two vertices has a vertex of degree $1$. (*Hint for the leaf lemma:* take a longest path and examine an endpoint.)

**25.** *(§7.12)* Let $G$ be a finite graph with maximum degree $\Delta(G)$. Prove by induction on the number of vertices that $G$ has a proper colouring with at most $\Delta(G) + 1$ colours. Explain why the same induction does **not** give a 2-colouring of a tree, and why the bound is nevertheless correct for trees.

**26.** *(§7.6)* A **propositional formula** is built from variables $p, q, r, \ldots$ by the rules: every variable is a formula; if $\varphi$ is a formula then $(\neg\varphi)$ is a formula; if $\varphi$ and $\psi$ are formulas then $(\varphi \wedge \psi)$ and $(\varphi \vee \psi)$ are formulas. Prove by structural induction that every formula contains equally many left and right brackets.

**27.** *(§8.2)* Prove that for every $n \ge 1$,
$$\sum_{k=1}^{n} (-1)^{k-1} k^2 = (-1)^{n-1}\,\frac{n(n+1)}{2}.$$
Check the identity at $n = 1, 2, 3, 4$.

**28.** *(§7.11)* Prove **Cassini's identity**:
$$F_{n+1}F_{n-1} - F_n^2 = (-1)^{n} \qquad (n \ge 1).$$
*Hint for the step:* replace $F_{n+2}$ by $F_{n+1} + F_n$ and use the hypothesis to rewrite $F_{n+1}F_{n-1}$.

**29.** *(§7.5)* Prove that $3^n \ge n^3$ for every integer $n \ge 1$. Note that equality occurs at $n = 3$, so the step cannot be strictly monotone there. State carefully which base cases you use and for which $k$ the step is valid.

**30.** *(§7.9)* Prove by induction on $n$ that if $x_1, \ldots, x_n$ are positive real numbers with $x_1x_2\cdots x_n = 1$, then $x_1 + \cdots + x_n \ge n$. (*Hints:* the base case $n = 2$ is $(\sqrt{x_1}-\sqrt{x_2})^2 \ge 0$. For the step from $n$ to $n+1$ with $n+1 \ge 3$, use the pigeonhole principle to find two of the numbers on the same side of $1$ — or one equal to $1$ — so that $(x_i-1)(x_j-1) \ge 0$; replace those two numbers by the single number $x_ix_j$ and apply the inductive hypothesis to the resulting $n$ numbers.)

## Challenge

**31.** *(§7.4)* Prove by strong induction that every integer $n \ge 1$ can be written as a sum of **distinct** Fibonacci numbers. (This is the existence half of Zeckendorf's theorem; uniqueness is not asked for.) *Hint:* if $F_k \le n < F_{k+1}$, consider $n - F_k$ and show it is smaller than $F_{k-1}$.

**32.** *(§7.4)* Let $a, b$ be coprime positive integers. Prove that every integer $n \ge (a-1)(b-1)$ can be written as $n = ax + by$ with integers $x, y \ge 0$.
*Hint:* show first that the $a$ consecutive integers $(a-1)(b-1), \ldots, (a-1)(b-1) + a - 1$ are all representable, then induct by adding $a$. For the first part, use that $0, b, 2b, \ldots, (a-1)b$ are pairwise incongruent modulo $a$.

**33.** *(§8.2)* Prove the **hockey-stick identity**: for integers $n \ge r \ge 0$,
$$\sum_{i=r}^{n} \binom{i}{r} = \binom{n+1}{r+1}.$$
Use Pascal's rule $\binom{n+1}{r+1} = \binom{n}{r+1} + \binom{n}{r}$ in the step. Check the case $r = 1$ against the formula for $1 + 2 + \cdots + n$.

**34.** *(§7.11)* Let $a_0 = 3$ and $a_{n+1} = a_n^2 - 2$ for $n \ge 0$. Prove by induction that if $x + x^{-1} = 3$ with $x > 1$, then
$$a_n = x^{\,2^n} + x^{-2^n}$$
for every $n \ge 0$. Deduce that $a_n = \lceil x^{2^n} \rceil$ and compute $a_0, a_1, a_2, a_3$ as integers.

**35.** *(§7.13)* Prove that $\displaystyle\sum_{k=1}^{n} \frac{1}{k^2} < 2$ for every $n \ge 1$. The direct induction does not close; strengthen the statement to $\sum_{k=1}^{n} k^{-2} \le 2 - 1/n$ and prove that instead. Explain in one sentence why the stronger statement implies the weaker one.

**36.** *(§7.4, §7.6)* Prove by induction that for every $n \ge 1$ and every integer $m \ge 0$, the product of the $n$ consecutive integers $m, m+1, \ldots, m+n-1$ is divisible by $n!$. (*Hint:* the proof needs two nested inductions. For fixed $n$, induct on $m$ using
$$(m+1)(m+2)\cdots(m+n) - m(m+1)\cdots(m+n-1) = n\,(m+1)(m+2)\cdots(m+n-1),$$
and the outer induction on $n$ supplies the divisibility of the right-hand product by $(n-1)!$.)
