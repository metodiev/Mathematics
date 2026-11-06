# Diophantine Equations — Exercises

> [Diophantine Equations](README.md) · 36 problems · Beginner → Challenge · Solutions: [solutions.md](solutions.md)

Attempt every problem in writing before looking at [solutions.md](solutions.md). Each problem names the section of the tutorial that supplies the technique.

Notation: an equation is solved over $\mathbb{Z}$ unless "non-negative", "positive" or "natural" is stated. $[a_0;a_1,a_2,\dots]$ is a continued fraction and $p_k/q_k$ its $k$-th convergent; $\ell$ is the period length of the continued fraction of $\sqrt D$; $g = \gcd(a,b)$; a triple is primitive when $\gcd(x,y,z)=1$; $T_n = n(n+1)/2$ is the $n$-th triangular number. "Representable" always means representable as $ax+by$ with $x,y\ge0$.

Where a problem asks for a proof, a complete proof is expected; where it asks for a computation, show every step.

## Beginner

**1.** *(§7.1)* Decide whether each equation has an integer solution; where it does, give one solution and the complete solution set.

(a) $6x+9y = 21$
(b) $15x+21y = 100$
(c) $8x+12y = 4$
(d) $7x+11y = 1$

**2.** *(§7.1)* Find one solution of $17x+25y=1$ by the extended Euclidean algorithm, write the complete solution set, and state the unique solution whose $x$-coordinate lies in $\{0,1,\dots,24\}$.

**3.** *(§7.1)* Find all solutions in non-negative integers of $5x+7y = 100$.

**4.** *(§7.1)* (a) Solve $3x+4y=1$ completely. (b) Hence find all non-negative solutions of $3x+4y=25$.

**5.** *(§7.2)* For coins of $3$ and $4$: list every positive amount that cannot be paid, state the largest such amount, and check it against $ab-a-b$ and against $\frac{(a-1)(b-1)}{2}$.

**6.** *(§7.2)* Repeat for coins of $5$ and $7$: list all unpayable amounts, count them, and verify both formulas.

**7.** *(§7.3)* Use the parametrisation to write down the primitive triple for $(m,n) = (2,1)$, $(3,2)$, $(4,1)$, $(5,2)$, and verify $x^{2}+y^{2}=z^{2}$ in each case.

**8.** *(§7.3)* For each of the triples $(20,21,29)$ and $(12,35,37)$: check that it is primitive, find the $m,n$ that produce it, and verify the parametrisation.

**9.** *(§7.4)* Which of $21,\ 45,\ 50,\ 65,\ 90$ are sums of two integer squares? For each that is, give a representation; for each that is not, name the obstruction.

**10.** *(§7.5)* Expand $\sqrt3$ as a continued fraction, compute the first five convergents, and read off the fundamental solution of $x^{2}-3y^{2}=1$. Verify it.

**11.** *(§7.5)* (a) Verify that $(1,1)$ solves $x^{2}-2y^{2}=-1$. (b) Square $1+\sqrt2$ to obtain a solution of $x^{2}-2y^{2}=1$. (c) Compute $(1+\sqrt2)^{3}$ and $(1+\sqrt2)^{4}$ and check which equation each solves.

**12.** *(§7.4)* List all solutions in non-negative integers of $x^{2}+y^{2}=25$, and of $x^{2}+y^{2}=65$. In each case say how many there are and why.

## Intermediate

**13.** *(§7.2)* Let $\gcd(a,b)=1$, $a,b\ge2$, and $N = ab-a-b$. Prove that for every integer $n$, exactly one of $n$ and $N-n$ is representable. Verify the statement for $(a,b) = (3,5)$ by listing both rows for $0\le n\le7$.

**14.** *(§7.3)* Prove that the area of a primitive Pythagorean triangle is divisible by $6$, and find a primitive triple whose area is $30$.

**15.** *(§7.3)* Prove that in a primitive Pythagorean triple exactly one leg is even and the hypotenuse is odd. Then prove that $3$ divides one of the legs.

**16.** *(§7.4)* Prove the Brahmagupta–Fibonacci identity in both forms. Then compute $(1^{2}+2^{2})(3^{2}+4^{2})$ both ways, and find all representations of $1105 = 5\cdot13\cdot17$ as $a^{2}+b^{2}$ with $0\le a\le b$.

**17.** *(§7.4)* Prove: if $p\equiv3\pmod4$ is prime and $p\mid a^{2}+b^{2}$, then $p\mid a$ and $p\mid b$. (Use Fermat's little theorem.)

**18.** *(§7.4)* Prove that $x^{2}\equiv-1\pmod p$ has a solution whenever $p\equiv1\pmod4$ is prime. (Use Wilson's theorem.) Illustrate with $p = 5, 13, 17$.

**19.** *(§7.5)* Prove that $x^{2}-2y^{2}=-1$ has infinitely many solutions, and list the first four.

**20.** *(§7.5)* Prove that $x^{2}-Dy^{2}=-1$ has no integer solution when $D\equiv3\pmod4$. Give two examples of $D$ to which this applies.

**21.** *(§7.5)* Let $(x_1,y_1)$ be a solution of $x^{2}-Dy^{2}=1$. Prove that $(x_1^{2}+Dy_1^{2},\,2x_1y_1)$ is also a solution. Starting from $(2,1)$ for $D=3$, iterate twice and verify each result.

**22.** *(§7.5)* A triangular number $T_n$ is *square* if $T_n = m^{2}$. Prove that $T_n$ is a square iff $(2n+1)^{2}-8m^{2}=1$, and use the solutions of $x^{2}-8y^{2}=1$ to find the first three square triangular numbers.

**23.** *(§7.5)* Prove that $3x^{2}+2 = y^{2}$ has no integer solution, and find the first four positive solutions of $3x^{2}+1 = y^{2}$.

**24.** *(§7.2)* Show that the Frobenius number of the pair $(a,a+1)$ is $a^{2}-a-1$ and that the number of unpayable amounts is $\frac{a(a-1)}{2}$. Check both formulas for $a = 3$ and $a = 4$ by listing.

## Advanced

**25.** *(§7.1)* Prove Theorem 7.1.2 in full: if $(x_0,y_0)$ solves $ax+by=c$ then every integer solution is $(x_0,y_0)+t\left(\frac bg,-\frac ag\right)$, and conversely. Explain where $\gcd(a,b)=1$ (after dividing) is used.

**26.** *(§7.2)* Prove both halves of the Frobenius theorem: that $ab-a-b$ is not representable, and that every $n>ab-a-b$ is.

**27.** *(§7.2)* Prove that exactly $\frac{(a-1)(b-1)}{2}$ positive integers are not representable, including a proof of the floor identity $\sum_{r=0}^{a-1}\left\lfloor \frac{br}{a}\right\rfloor = \frac{(a-1)(b-1)}{2}$.

**28.** *(§7.3)* Prove the classification of primitive Pythagorean triples in both directions.

**29.** *(§7.4)* Prove the necessity direction of the two-square theorem, starting from the lemma in Exercise 17.

**30.** *(§7.4)* Prove that every prime $p\equiv1\pmod4$ is a sum of two squares, by combining Exercise 18 (a square root of $-1$) with a pigeonhole argument. Be explicit about why the constructed $c^{2}+d^{2}$ equals $p$ rather than some larger multiple of $p$.

**31.** *(§7.5)* Prove (a) the determinant identity $p_kq_{k-1}-p_{k-1}q_k = (-1)^{k-1}$ for convergents, and (b) the error bound $\left\lvert\alpha-\frac{p_k}{q_k}\right\rvert < \frac{1}{q_kq_{k+1}}$ for irrational $\alpha$. Deduce that $q_k$ is strictly increasing for $k\ge1$ and that $\left\lvert\alpha - p_k/q_k\right\rvert<1/q_k^{2}$.

**32.** *(§7.6)* Prove Fermat's theorem in full: $x^{4}+y^{4}=z^{2}$ has no solution in positive integers. Then deduce that $x^{4}+y^{4}=z^{4}$ has no solution with $xyz\ne0$.

**33.** *(§7.5)* Prove that every positive solution of $x^{2}-Dy^{2}=1$ is a power of the fundamental solution.

## Challenge

**34.** *(§7.7)* Prove that the only integer solutions of $y^{2}=x^{3}-2$ are $(3,5)$ and $(3,-5)$, assuming the lemma that $\mathbb{Z}[\sqrt{-2}]$ is Euclidean for the norm $a^{2}+2b^{2}$ and hence a unique factorisation domain.

**35.** *(§7.4)* Prove that $2n$ is a sum of two integer squares if and only if $n$ is. Deduce that the set of sums of two squares is closed under multiplication and under multiplication by a square.

**36.** *(§7.4)* (a) Prove that no integer of the form $4^{a}(8b+7)$ is a sum of three integer squares. (b) Determine which $n\le40$ are sums of three squares and check that the failures are exactly the numbers of that form. (c) State Legendre's theorem and explain why part (a) is only one direction of it.
