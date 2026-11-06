# Quadratic Residues and Reciprocity — Exercises

> [Quadratic Residues and Reciprocity](README.md) · 36 problems · Beginner → Challenge · Solutions: [solutions.md](solutions.md)

Attempt every problem in writing before looking at [solutions.md](solutions.md). Each problem names the section of the tutorial that supplies the method. Unless stated otherwise, $p$ and $q$ are odd primes, and $(a/p)$ is the Legendre symbol.

Where a problem asks for a proof, a complete proof is expected, including the hypotheses. Where it asks for a computation, show the reciprocity steps; a bare numerical answer is not sufficient.

## Beginner

**1.** *(§7.1)* List the nonzero quadratic residues and non-residues modulo $23$. Count each set and verify that each residue has exactly two square roots.

**2.** *(§5.2, §7.3)* Evaluate the following Legendre symbols by direct enumeration of squares, not by reciprocity:

(a) $\left(\frac{3}{7}\right)$
(b) $\left(\frac{5}{11}\right)$
(c) $\left(\frac{2}{13}\right)$
(d) $\left(\frac{6}{7}\right)$
(e) $\left(\frac{-1}{5}\right)$
(f) $\left(\frac{-1}{7}\right)$

**3.** *(§7.2)* Use Euler's criterion to compute

(a) $\left(\frac{2}{17}\right)$,
(b) $\left(\frac{3}{17}\right)$,
(c) $\left(\frac{5}{17}\right)$.

Check each answer against the list of squares modulo $17$.

**4.** *(§7.3, §7.7)* Use the supplementary laws to compute $\left(\frac{-1}{p}\right)$ and $\left(\frac{2}{p}\right)$ for $p=7,13,17,29$. Present the answers in a table and state the relevant residue of $p$ modulo $4$ and modulo $8$.

**5.** *(§7.3)* Using multiplicativity and the values from Problem 2, compute

(a) $\left(\frac{6}{13}\right)$,
(b) $\left(\frac{10}{13}\right)$.

Verify each answer by listing the squares modulo $13$.

**6.** *(§7.1)* Compute the sum of all nonzero quadratic residues modulo $19$ and modulo $23$, and the sum of all non-residues. Show that both sums are divisible by $p$ in each case.

**7.** *(§7.3, §7.7)* Find all primes $p<50$ such that $\left(\frac{-1}{p}\right)=1$ and $\left(\frac{2}{p}\right)=1$. Express the condition on $p$ modulo $8$.

**8.** *(§7.9)* Solve each congruence, or explain why there is no solution:

(a) $x^2\equiv9\pmod{11}$,
(b) $x^2\equiv0\pmod{11}$,
(c) $x^2\equiv2\pmod{11}$.

**9.** *(§7.9)* Solve $x^2\equiv-1\pmod{13}$. Then explain why $x^2\equiv-1\pmod7$ has no solution.

**10.** *(§5.3, §7.8)* Compute the Jacobi symbols

(a) $\left(\frac{2}{9}\right)$,
(b) $\left(\frac{5}{9}\right)$,
(c) $\left(\frac{7}{15}\right)$.

**11.** *(§7.8)* Show that $\left(\frac{2}{15}\right)=1$, yet $2$ is not a square modulo $15$. List all squares modulo $15$ to justify your answer.

**12.** *(§7.1)* List all squares modulo $15$, including $0$. How many are there, and why does the formula $(p-1)/2$ for primes not apply?

## Intermediate

**13.** *(§7.4)* Use Gauss's lemma to compute

(a) $\left(\frac{3}{13}\right)$,
(b) $\left(\frac{5}{13}\right)$,
(c) $\left(\frac{7}{13}\right)$.

In each case list the least positive residues and count those exceeding $13/2$.

**14.** *(§7.6)* Use quadratic reciprocity and the supplementary laws to compute

(a) $\left(\frac{19}{29}\right)$,
(b) $\left(\frac{31}{43}\right)$.

Show every flip of the symbol and every reduction modulo the new denominator.

**15.** *(§7.8)* Compute the Jacobi symbol $\left(\frac{77}{101}\right)$, where $77=7\cdot11$. State clearly which properties you use.

**16.** *(§7.9)* Use the Tonelli-Shanks algorithm to solve $x^2\equiv10\pmod{13}$. Show the values of $Q$, $S$, $z$, $c$, $t$, and $R$ at every stage.

**17.** *(§7.9)* Solve $x^2\equiv8\pmod{17}$ by listing squares, and verify that there are exactly two roots.

**18.** *(§7.9)* Solve $x^2\equiv9\pmod{35}$ by solving modulo $5$ and modulo $7$, then combining with the Chinese remainder theorem. How many roots does the general theory predict?

**19.** *(§7.9)* Use Hensel lifting to solve $x^2\equiv6\pmod{25}$. Start from the two roots modulo $5$, lift each to a root modulo $25$, and verify both answers.

**20.** *(§7.9)* Without listing all solutions, determine the number of solutions of $x^2\equiv1\pmod{105}$. Explain the role of the factorisation $105=3\cdot5\cdot7$.

**21.** *(§7.3)* Prove that the product of two quadratic non-residues modulo an odd prime $p$ is a quadratic residue, and that the quotient of two non-residues is a residue. Use the Legendre symbol.

**22.** *(§7.6)* Find all primes $p$ such that $\left(\frac{5}{p}\right)=1$. Express the answer as congruence conditions on $p$ modulo $5$, and say what happens at $p=5$.

## Advanced

**23.** *(§7.2)* Prove Euler's criterion: for an odd prime $p$ and $p\nmid a$,
$$
a^{(p-1)/2}\equiv\left(\frac{a}{p}\right)\pmod p.
$$
Your proof must justify why a non-residue cannot satisfy $a^{(p-1)/2}\equiv1\pmod p$.

**24.** *(§7.4)* State and prove Gauss's lemma. In the proof, explain carefully why the integers $s_i=\min(r_i,p-r_i)$ are pairwise distinct and why this forces them to be a permutation of $\{1,\dots,(p-1)/2\}$.

**25.** *(§7.3)* Prove the first supplementary law:
$$
\left(\frac{-1}{p}\right)=(-1)^{(p-1)/2}.
$$
Then use it to characterise the primes for which $-1$ is a quadratic residue.

**26.** *(§7.7)* Prove the second supplementary law:
$$
\left(\frac{2}{p}\right)=(-1)^{(p^2-1)/8}.
$$
Use Gauss's lemma with $a=2$ and treat the four cases $p\equiv1,3,5,7\pmod8$.

**27.** *(§7.5)* State and prove Eisenstein's lemma. Your proof should show explicitly that the parity of $\sum_i\lfloor ai/p\rfloor$ equals the number $m$ of large least positive residues.

**28.** *(§7.8)* Prove the Jacobi reciprocity law: for coprime positive odd integers $m,n$,
$$
\left(\frac{m}{n}\right)\left(\frac{n}{m}\right)=(-1)^{\frac{m-1}{2}\cdot\frac{n-1}{2}}.
$$
Deduce it from quadratic reciprocity for primes and multiplicativity.

**29.** *(§7.9)* Let $p\equiv3\pmod4$ be prime and suppose $\left(\frac{a}{p}\right)=1$. Prove that the two solutions of $x^2\equiv a\pmod p$ are
$$
x\equiv\pm a^{(p+1)/4}\pmod p.
$$
Then solve $x^2\equiv5\pmod{11}$ using this formula and check both roots.

**30.** *(§7.9)* Let $n$ be odd and $\gcd(a,n)=1$. Prove that $x^2\equiv a\pmod n$ is solvable if and only if it is solvable modulo every prime power dividing $n$, and that when solvable it has exactly $2^{\omega(n)}$ solutions modulo $n$.

**31.** *(§7.6)* Prove that for an odd prime $p\ne3$,
$$
\left(\frac{-3}{p}\right)=1
\iff p\equiv1\pmod3.
$$
Use quadratic reciprocity and the first supplementary law.

**32.** *(§7.10)* Let $\chi(a)=\left(\frac{a}{p}\right)$ for $a\not\equiv0\pmod p$ and $\chi(0)=0$. Prove that the number of solutions of
$$
x^2+y^2\equiv1\pmod p
$$
is $p-\chi(-1)$. You may use the identity $\sum_{x\in\mathbb{F}_p}\chi(x^2-a)=-1$ for $a\ne0$, but you must prove that identity.

## Challenge

**33.** *(§7.1, §7.6)* Prove that there are infinitely many primes congruent to $1$ modulo $4$. Use a Euclid-style argument with $N=(2p_1p_2\cdots p_k)^2+1$, and justify why every prime divisor of $N$ is $1$ modulo $4$.

**34.** *(§7.1, §7.7)* Prove that there are infinitely many primes congruent to $1$ modulo $8$. Consider $N=(2p_1p_2\cdots p_k)^4+1$ and show that every prime divisor $q$ of $N$ satisfies $q\equiv1\pmod8$ by studying the order of $2p_1\cdots p_k$ modulo $q$.

**35.** *(§7.3, §7.6)* Zolotarev's lemma. Let $p$ be an odd prime and $p\nmid a$. Let $\pi_a$ be the permutation of $\{0,1,\dots,p-1\}$ defined by $\pi_a(x)\equiv ax\pmod p$. Prove that the sign of $\pi_a$ equals $\left(\frac{a}{p}\right)$. You may use the fact that $\mathbb{F}_p^\times$ is cyclic.

**36.** *(§7.9)* Let $a$ be odd and $k\ge1$. Prove that
$$
\#\{x\bmod2^k:x^2\equiv a\pmod{2^k}\}=
\begin{cases}
1, & k=1,\\
2, & k=2\text{ and }a\equiv1\pmod4,\\
0, & k=2\text{ and }a\equiv3\pmod4,\\
4, & k\ge3\text{ and }a\equiv1\pmod8,\\
0, & k\ge3\text{ and }a\not\equiv1\pmod8.
\end{cases}
$$
For the case $k\ge3$, you may use the fact that the solutions of $u^2\equiv1\pmod{2^k}$ are exactly $u\equiv\pm1,\pm(1+2^{k-1})\pmod{2^k}$; prove this fact as part of your solution.
