# Recurrence Relations — Exercises

> [Recurrence Relations](README.md) · 36 problems · Beginner → Challenge · Solutions: [solutions.md](solutions.md)

Attempt every problem in writing before looking at [solutions.md](solutions.md). Each problem names the section of the tutorial that supplies the method. For every closed form you obtain, verify it numerically at the first few values of $n$ and then prove it by induction.

Notation: $F_0 = 0$, $F_1 = 1$, $F_n = F_{n-1}+F_{n-2}$; $\varphi = \frac{1+\sqrt5}{2}$, $\psi = \frac{1-\sqrt5}{2}$; $L_n = \varphi^n+\psi^n$ are the Lucas numbers; $T(n)$ denotes the running time of an algorithm on an input of size $n$, with $T(1) = \Theta(1)$ unless stated otherwise. In master-theorem problems, "solve" means "give the tight $\Theta$ bound and name the case".

## Beginner

**1.** *(§7.2)* Solve $a_n = a_{n-1}+3$ with $a_0 = 2$ by iteration. Give the closed form, compute $a_0, \ldots, a_4$, and verify the formula by induction.

**2.** *(§7.2)* Solve $a_n = 2a_{n-1}$ with $a_1 = 5$. State the first four terms and the closed form, and say which initial condition you used and why one is enough.

**3.** *(§7.2)* Solve $a_n = 3a_{n-1}$ with $a_0 = 2$. Then explain in one sentence why the answer is not $3^{n+1}$.

**4.** *(§7.2)* Solve $a_n = a_{n-1}+n$ with $a_1 = 1$. Give the closed form and check it at $n = 1, 2, 3, 4$.

**5.** *(§7.2)* Solve $a_n = a_{n-1}+2^n$ with $a_0 = 0$. Give the closed form and verify it at $n = 0, 1, 2, 3$.

**6.** *(§7.3)* Solve $a_n = 5a_{n-1}-6a_{n-2}$ with $a_0 = 1$, $a_1 = 2$. (The answer is unusually simple; explain why.)

**7.** *(§7.3, §7.7)* The Lucas numbers are defined by $L_0 = 2$, $L_1 = 1$ and $L_n = L_{n-1}+L_{n-2}$. Compute $L_0, \ldots, L_5$, find the closed form $L_n = \varphi^n+\psi^n$, and verify that it reproduces your six values.

**8.** *(§7.4)* Solve $a_n = 4a_{n-1}-4a_{n-2}$ with $a_0 = 1$, $a_1 = 4$. State the characteristic root and its multiplicity, and verify the formula at $n = 2, 3, 4$.

**9.** *(§7.2)* Solve $a_n - a_{n-1} = \dfrac{1}{n(n+1)}$ with $a_0 = 0$ by telescoping. Check the answer at $n = 1, 2, 3$.

**10.** *(§7.2)* Solve $a_n = n\,a_{n-1}$ with $a_0 = 1$. What is the name of the resulting sequence, and why is the recurrence "linear with variable coefficients" rather than "non-linear"?

**11.** *(§5.1)* For each recurrence, state its order (if defined), and whether it is linear, homogeneous, and has constant coefficients.
(a) $a_n = 7a_{n-1}-12a_{n-2}$;
(b) $a_n = a_{n-1}+n^2$;
(c) $a_n = n^2a_{n-1}$;
(d) $a_n = a_{n-1}+a_{n-2}+a_{n-3}$;
(e) $a_n = a_{n-1}^2$;
(f) $T(n) = 3T(n/2)+n$.

**12.** *(§5.1)* Compute the first six terms of $a_n = a_{n-1}+2a_{n-2}$ with $a_0 = 1$, $a_1 = 1$. Then compute the first six terms of the candidate closed form $a_n = \frac{2^{n+1}+(-1)^n}{3}$ and check that the two lists agree.

## Intermediate

**13.** *(§7.2, §7.12)* The merge-sort recurrence is $T(n) = 2T(n/2)+n$ with $T(1) = 1$. Solve it by iteration for $n = 2^k$, obtaining $T(n) = n\log_2 n + n$, and verify the formula at $n = 2, 4, 8$ by direct computation.

**14.** *(§7.8)* Solve the non-homogeneous recurrence $a_n = 2a_{n-1}+n$ with $a_0 = 0$. Find a particular solution of the form $an+b$, then add the homogeneous solution and fit the initial condition.

**15.** *(§7.8)* Solve $a_n = 3a_{n-1}+2\cdot 3^n$ with $a_0 = 1$. Note that $3$ is a characteristic root of the homogeneous recurrence, so the trial must be multiplied by $n$.

**16.** *(§7.8)* Solve $a_n = 2a_{n-1}+2^n$ with $a_1 = 3$. State clearly why the trial $C2^n$ fails and $Cn2^n$ succeeds.

**17.** *(§7.2, §7.12)* Solve $T(n) = T(n/2)+1$ with $T(1) = 0$ by iteration, for $n = 2^k$. Check the answer at $n = 2, 4, 8, 16$.

**18.** *(§7.10)* Use the master theorem to solve $T(n) = 4T(n/2)+n$ with $T(1) = 1$. Identify $a$, $b$, $\log_ba$, the case, and the resulting $\Theta$ bound.

**19.** *(§7.10)* Use the master theorem to solve $T(n) = 2T(n/2)+n^2$. Verify the regularity condition explicitly, and check the answer against the recursion-tree level costs.

**20.** *(§7.10)* Use the master theorem to solve $T(n) = 7T(n/2)+n^2$. Give the exponent $\log_2 7$ to three decimal places and compare the result with the naive matrix-multiplication bound $\Theta(n^3)$.

**21.** *(§7.8)* Solve $a_n = 5a_{n-1}-6a_{n-2}+3^n$ with $a_0 = 1$, $a_1 = 6$. The forcing base $3$ is a simple characteristic root; find the particular solution first.

**22.** *(§7.11)* Solve $a_n = 2a_{n-1}+1$ with $a_0 = 1$ using a generating function. Set up the equation for $G(x) = \sum a_nx^n$, solve it, use partial fractions, and read off the coefficients.

## Advanced

**23.** *(§7.4)* Solve $a_n = 2a_{n-1}-a_{n-2}$ with $a_0 = 1$, $a_1 = 3$. The characteristic equation has a repeated root; explain why the answer is linear in $n$.

**24.** *(§7.5)* Solve $a_n = 2a_{n-1}-2a_{n-2}$ with $a_0 = 0$, $a_1 = 2$. Express the answer in the form $\rho^n(C\cos n\theta + D\sin n\theta)$ and state $\rho$ and $\theta$ exactly.

**25.** *(§7.4)* Solve $a_n = 6a_{n-1}-9a_{n-2}$ with $a_0 = 1$, $a_1 = 0$. Verify the formula at $n = 2, 3, 4$.

**26.** *(§7.11)* Solve $a_n = a_{n-1}+2a_{n-2}$ with $a_0 = 1$, $a_1 = 1$ using a generating function. Show the partial-fraction decomposition and read off the coefficients.

**27.** *(§7.11)* The Catalan numbers satisfy $C_0 = 1$ and $C_n = \sum_{k=0}^{n-1}C_kC_{n-1-k}$. Derive $C(x) = \frac{1-\sqrt{1-4x}}{2x}$ from $C(x) = 1+xC(x)^2$, then use the binomial expansion of $\sqrt{1-4x}$ to obtain $C_n = \frac{1}{n+1}\binom{2n}{n}$. Verify $C_0, \ldots, C_4$.

**28.** *(§7.10)* Prove by summing the recursion-tree levels that $T(n) = 2T(n/2)+n\log_2 n$ satisfies $T(n) = \Theta(n\log^2 n)$. This is the extended second case of the master theorem; state which case applies and why.

**29.** *(§7.8)* Solve $a_n = 3a_{n-1}-2a_{n-2}+2^n$ with $a_0 = 0$, $a_1 = 1$. Identify the homogeneous roots, the particular solution, and verify at $n = 2, 3$.

**30.** *(§5.2)* Prove Theorem 5.6: a linear recurrence of order $k$ together with $k$ initial values determines exactly one sequence. Your proof must cover both existence and uniqueness, and must cite the recursion theorem or give an explicit induction.

## Challenge

**31.** *(§7.3, §7.4)* Solve $a_n = 4a_{n-1}-a_{n-2}$ with $a_0 = 2$, $a_1 = 4$, obtaining $a_n = (2+\sqrt3)^n+(2-\sqrt3)^n$. Prove that $a_n$ is even for every $n \ge 0$, without expanding the binomial powers.

**32.** *(§7.10)* Prove Case 1 of the master theorem for $n = b^k$: if $f(n) = O(n^{\log_ba-\varepsilon})$ with $\varepsilon > 0$, then $T(n) = \Theta(n^{\log_ba})$. Include the upper bound from the geometric sum and the lower bound from the leaves.

**33.** *(§7.9, §7.10)* Solve $T(n) = 2T(\sqrt n)+\log_2 n$ by the substitution $n = 2^m$. State the domain on which the substitution is valid and give the final answer in terms of $n$.

**34.** *(§7.7)* Let $L_n = \varphi^n+\psi^n$. Prove that $F_{2n} = F_nL_n$ for every $n \ge 0$, and prove that $F_n = \left\lfloor \frac{\varphi^n}{\sqrt5}+\frac12\right\rfloor$. Check both statements at $n = 4$.

**35.** *(§7.11)* Derive Binet's formula from the generating function $G(x) = \dfrac{x}{1-x-x^2}$ by partial fractions, factor by factor, without using the characteristic equation.

**36.** *(§7.13)* The Tribonacci sequence satisfies $a_0 = a_1 = 0$, $a_2 = 1$, $a_n = a_{n-1}+a_{n-2}+a_{n-3}$. Its characteristic polynomial is $P(r) = r^3-r^2-r-1$. Show that $P$ has exactly one real root $\alpha \approx 1.8392867$, that the other two roots are complex conjugates of modulus $1/\sqrt\alpha$, and deduce that $a_n = \Theta(\alpha^n)$.
