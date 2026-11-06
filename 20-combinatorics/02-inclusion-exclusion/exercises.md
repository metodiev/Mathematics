# Inclusion–Exclusion — Exercises

> [Inclusion–Exclusion](README.md) · 36 problems · Beginner → Challenge · Solutions: [solutions.md](solutions.md)

Attempt every problem in writing before looking at [solutions.md](solutions.md). Each problem names, in italics, the section of the tutorial that supplies the technique.

Notation: $[n] = \{1,2,\dots,n\}$; $\mathbb{N} = \{1,2,3,\dots\}$; $\binom{n}{k}$ is the number of $k$-element subsets of an $n$-element set; $D_n$ is the number of derangements of $[n]$; $\varphi$ is Euler's totient; $\operatorname{Surj}(m,n)$ is the number of surjective functions from an $m$-element set to an $n$-element set; $S(m,n)$ is the Stirling number of the second kind.

Unless a problem says otherwise, a complete solution must name the universe, name the bad properties, compute a general intersection, and then add and subtract. A numerical answer unsupported by such an argument will not be accepted, and every numerical answer should be checked on a small case.

## Beginner

**1.** *(§7.1)* Let $\lvert A\rvert = 14$, $\lvert B\rvert = 23$ and $\lvert A \cap B\rvert = 9$. Compute $\lvert A \cup B\rvert$, $\lvert A \setminus B\rvert$, $\lvert B \setminus A\rvert$ and the number of elements lying in exactly one of $A$ and $B$.

**2.** *(§7.1)* In a class of $40$ students, $26$ study French, $21$ study German and $12$ study both. How many study at least one of the two languages, how many study exactly one, and how many study neither? Draw the four regions of the Venn diagram with their sizes.

**3.** *(§7.2)* Three sets satisfy $\lvert A\rvert = 20$, $\lvert B\rvert = 17$, $\lvert C\rvert = 13$, $\lvert A\cap B\rvert = 8$, $\lvert A\cap C\rvert = 6$, $\lvert B\cap C\rvert = 5$ and $\lvert A\cap B\cap C\rvert = 3$. Compute $\lvert A\cup B\cup C\rvert$ and verify the answer by computing the seven non-empty regions of the Venn diagram.

**4.** *(§7.6)* How many integers in $[100]$ are divisible by $3$ or by $5$? How many are divisible by neither?

**5.** *(§7.6)* How many integers in $[500]$ are divisible by $4$ or by $6$? Explain why $\lfloor 500/12\rfloor$ is the right correction term, and why neither $\lfloor 500/24\rfloor$ nor the expression $\lfloor 500/4\rfloor\cdot\lfloor 500/6\rfloor/500$ is.

**6.** *(§7.6)* How many four-digit positive integers (from $1000$ to $9999$) contain the digit $7$ at least once? (Count the complement.)

**7.** *(§7.7)* Compute $D_4$ from the formula $D_n = n!\sum_{k=0}^{n}(-1)^k/k!$, and list the nine derangements of $[4]$ explicitly.

**8.** *(§7.7)* Compute $D_6$ and $D_7$ from the recurrence $D_n = nD_{n-1} + (-1)^n$, starting from $D_4 = 9$.

**9.** *(§7.9)* How many functions from a $6$-element set onto a $3$-element set are there? Verify the answer using $\operatorname{Surj}(m,n) = n!\,S(m,n)$, given $S(6,3) = 90$.

**10.** *(§7.11)* Compute $\varphi(84)$ and $\varphi(720)$ in two ways: from the product formula, and by a direct count of the residues coprime to each modulus.

**11.** *(§7.6)* How many integers in $[1000]$ are coprime to $42$? Check the answer against the period $42$.

**12.** *(§7.12)* Three events satisfy $\Pr(A) = 0.5$, $\Pr(B) = 0.4$, $\Pr(C) = 0.3$, $\Pr(A\cap B) = 0.2$, $\Pr(A \cap C) = 0.15$, $\Pr(B\cap C) = 0.1$ and $\Pr(A\cap B\cap C) = 0.05$. Compute $\Pr(A\cup B\cup C)$ and the probability that none of the three occurs.

## Intermediate

**13.** *(§7.7)* Compute $D_8$ from the closed formula and check it with the recurrence $D_n = nD_{n-1}+(-1)^n$.

**14.** *(§7.7)* How many permutations of $[6]$ have exactly two fixed points? What is the probability that a uniformly random permutation of $[6]$ has exactly two fixed points?

**15.** *(§7.6)* How many integers in $[10\,000]$ are divisible by none of $6$, $10$, $15$? (The moduli are not pairwise coprime; use least common multiples.)

**16.** *(§7.14)* In a survey of $100$ people, $60$ read newspaper $A$, $50$ read $B$, $40$ read $C$, $30$ read $A$ and $B$, $25$ read $B$ and $C$, $20$ read $A$ and $C$, and $10$ read all three. How many read exactly one, exactly two, exactly three, and none?

**17.** *(§7.9)* How many functions from a $6$-element set onto a $4$-element set are there? Deduce $S(6,4)$.

**18.** *(§7.6)* In how many ways can three married couples be seated in a row of six seats so that no husband sits next to his wife? (Use the formula $\sum_k(-1)^k\binom{n}{k}2^k(2n-k)!$ for $n$ couples, and check the case $n = 2$ separately by hand.)

**19.** *(§7.10)* In how many ways can four people be assigned to four distinct tasks if persons $1$ and $2$ both refuse tasks $1$ and $2$, person $3$ refuses task $3$, and person $4$ accepts any task? Build the rook polynomial (using the product rule for boards in disjoint rows and columns), apply the rook theorem, and check by listing.

**20.** *(§7.11)* Compute $\varphi(1001)$ using $1001 = 7\cdot 11\cdot 13$. Explain why the answer is so much simpler than the general formula suggests.

**21.** *(§7.12)* A fair die is rolled $10$ times. What is the exact probability that every face appears at least once? Give the answer as a fraction and as a decimal to four significant figures.

**22.** *(§7.12)* Ten letters are inserted at random into ten addressed envelopes, one per envelope. What is the probability that at least one letter reaches its own envelope? Give an exact fraction and a decimal.

**23.** *(§7.13)* Five events each have probability $0.9$. Prove that $\Pr(B_1 \cap \cdots \cap B_5) \ge 0.5$, and exhibit a probability space in which equality holds.

**24.** *(§7.6)* How many integers in $[1000]$ are divisible by $6$ or by $10$ but not by $15$? Be careful: "divisible by $6$ or $10$" and "not divisible by $15$" interact.

## Advanced

**25.** *(§7.14)* Prove that the number of elements lying in exactly $m$ of the sets $A_1,\dots,A_n$ is
$$N_m = \sum_{k=m}^{n}(-1)^{k-m}\binom{k}{m}S_k .$$

**26.** *(§7.13)* Prove the Bonferroni inequalities: for $1 \le t \le n$, the partial sum $S_1 - S_2 + \cdots + (-1)^{t+1}S_t$ is an upper bound for $\lvert \bigcup_i A_i\rvert$ when $t$ is odd and a lower bound when $t$ is even.

**27.** *(§7.7)* (a) Derive $D_n = nD_{n-1} + (-1)^n$ from the closed formula $D_n = n!\sum_{k=0}^{n}(-1)^k/k!$.
(b) Prove $D_n = (n-1)(D_{n-1}+D_{n-2})$ combinatorially, by classifying derangements according to the image and preimage of $n$.

**28.** *(§7.10)* Prove the rook theorem: if $B \subseteq [n]\times[n]$ and $r_k$ is the number of ways to choose $k$ non-attacking cells of $B$, then the number of permutations of $[n]$ avoiding every cell of $B$ is $\sum_k(-1)^k r_k(n-k)!$.

**29.** *(§7.11)* (a) Prove that $\varphi(n) = n\prod_{p\mid n}(1-1/p)$, the product being over the distinct prime divisors of $n$.
(b) Deduce that $\sum_{d\mid n}\varphi(d) = n$.

**30.** *(§7.7, §7.14)* Let $F(n,k)$ be the number of permutations of $[n]$ with exactly $k$ fixed points. Prove that $F(n,k) = \binom{n}{k}D_{n-k}$ and deduce that $F(n,k)/n! \to e^{-1}/k!$ as $n \to \infty$ for each fixed $k$.

**31.** *(§7.11)* Prove Legendre's formula $\pi(x) = \Phi(x,a) + a - 1$ where $a = \pi(\sqrt{x})$ and $\Phi(x,a)$ counts the integers in $[x]$ divisible by none of the first $a$ primes. Given $\Phi(1000,11) = 158$, compute $\pi(1000)$.

**32.** *(§8.4)* Prove the binomial inversion formula: if $a_n = \sum_{k=0}^{n}\binom{n}{k}b_k$ for all $n$, then $b_n = \sum_{k=0}^{n}(-1)^{n-k}\binom{n}{k}a_k$. Deduce the "exactly $m$" formula from the relation $S_k = \sum_{m\ge k}\binom{m}{k}N_m$.

## Challenge

**33.** *(§7.10)* A permutation $\sigma$ of $[n]$ has a **succession** at $i$ when $\sigma(i+1) = \sigma(i)+1$, for $1 \le i \le n-1$. Prove that the number of permutations with no succession is
$$\sum_{k=0}^{n-1}(-1)^k\binom{n-1}{k}(n-k)! ,$$
compute the values for $n = 1,2,3,4,5$, and verify the case $n = 4$ by listing.

**34.** *(§7.14)* Prove Jordan's formula: the number of elements lying in at least $r$ of the sets $A_1,\dots,A_n$ is
$$N_{\ge r} = \sum_{k=r}^{n}(-1)^{k-r}\binom{k-1}{r-1}S_k .$$
Check it on the three sets $A = [10]$, $B = \{3,4,5,6,11,12\}$, $C = \{5,6,7,13\}$ for $r = 1, 2, 3$.

**35.** *(§7.9)* Prove combinatorially that $\operatorname{Surj}(m,n) = n\,\operatorname{Surj}(m-1,n) + n\,\operatorname{Surj}(m-1,n-1)$ for $m,n \ge 2$, and check the identity at $(m,n) = (4,3)$ against the inclusion–exclusion formula.

**36.** *(§7.11)* Let $P$ be a finite set of primes. Prove that the natural density of the integers divisible by no prime in $P$ exists and equals $\prod_{p\in P}(1-1/p)$. Evaluate the density for $P = \{2,3,5,7\}$ and compare with the exact count up to $1000$.
