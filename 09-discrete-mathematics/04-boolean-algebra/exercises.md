# Boolean Algebra — Exercises

> [Boolean Algebra](README.md) · 36 problems · Beginner → Challenge · Solutions: [solutions.md](solutions.md)

Attempt every problem in writing before consulting [solutions.md](solutions.md). Each problem names the section of the tutorial that supplies the method. Unless stated otherwise, variables range over $\{0,1\}$, juxtaposition denotes $\land$, $+$ denotes $\lor$, $\bar x$ denotes $\neg x$, and $m_j$ / $M_j$ are the minterm and maxterm of the assignment whose binary value is $j$ (with $x$ as the most significant variable).

## Beginner

**1.** *(§7.1)* Construct the truth table of $f(x,y,z) = (x \lor y) \land \bar z$, list the minterms where $f = 1$, and state $\Sigma m(\cdot)$ for $f$.

**2.** *(§7.1)* Compute the truth table of $f = x \oplus y \oplus z$ and describe in words what the function computes. How many rows are true?

**3.** *(§7.2, §7.4)* Name the law used at each step of
$$x \land (x \lor y) = (x \land x) \lor (x \land y) = x \lor (x \land y) = (x \land 1) \lor (x \land y) = x \land (1 \lor y) = x \land 1 = x.$$

**4.** *(§7.2)* Prove algebraically that $x \land x = x$. Do not use absorption.

**5.** *(§7.2)* Prove algebraically that $x \land 0 = 0$.

**6.** *(§7.5)* Apply De Morgan's laws repeatedly to write $\neg\bigl(x \land \neg y \land z\bigr)$ with negation applied only to single variables.

**7.** *(§7.6)* Write the canonical DNF of $f = \Sigma m(1,2,5,7)$ on variables $x,y,z$.

**8.** *(§7.6)* Write the canonical CNF of the same function $f = \Sigma m(1,2,5,7)$.

**9.** *(§7.6)* Write $x \oplus y$ in canonical DNF and in canonical CNF.

**10.** *(§5.2, §8.5)* How many Boolean functions of three variables are there? How many of four variables? Justify with a counting argument.

**11.** *(§7.10)* Draw (describe in words or pseudocode) a circuit for $f = x\bar y \lor z$ using AND, OR and NOT gates, and count its gates and depth.

**12.** *(§7.7)* Is $\{\land, \lor\}$ functionally complete? Answer yes or no and justify in one sentence.

## Intermediate

**13.** *(§7.4, §8.1)* Prove the absorption law $x \lor (x \land y) = x$ (a) by truth table and (b) algebraically from the axioms.

**14.** *(§7.4)* Prove the distributive law $x \lor (y \land z) = (x \lor y) \land (x \lor z)$ by truth table.

**15.** *(§7.4, §9.4)* Simplify $f = x \lor \bar x y \lor \bar x\bar y$ to a constant, justifying each step.

**16.** *(§7.4)* Simplify $f = xy \lor \bar x y \lor x\bar y$ to a two-literal expression and verify the result on all four assignments.

**17.** *(§7.6)* Convert $f = (x \lor y)(\bar x \lor z)$ to disjunctive normal form and simplify it to a sum of two two-literal products.

**18.** *(§7.8)* Use a Karnaugh map to simplify $f = \Sigma m(0,2,4,6)$ on four variables $A,B,C,D$.

**19.** *(§7.8)* Use a Karnaugh map to find a minimal sum of products for $f = \Sigma m(0,1,2,5,6,7)$ on three variables. Explain why no group of four is available and why three terms are therefore necessary.

**20.** *(§7.9)* Use a Karnaugh map with don't cares to simplify $f = \Sigma m(1,5,7)$ with $d(3,6)$ on three variables. Verify the result on the care set.

**21.** *(§7.7, §7.10)* Implement $f = x \lor yz$ using only NAND gates. Give the circuit, the gate count and a truth-table verification.

**22.** *(§7.4, §8.1)* State the dual of the consensus theorem and prove it by duality from $xy \lor \bar xz \lor yz = xy \lor \bar xz$.

**23.** *(§7.11)* Verify the ring distributivity law $x \land (y \oplus z) = (x \land y) \oplus (x \land z)$ on all eight assignments, and confirm that $x \lor y = x \oplus y \oplus (x \land y)$ on all four assignments of two variables.

**24.** *(§7.10, §7.12)* A $2{:}1$ multiplexer computes $z = \bar s a \lor s b$. Write its truth table, give an equivalent CNF, and explain why it implements "if $s$ then $b$ else $a$".

## Advanced

**25.** *(§8.1)* Prove from the axioms that $\neg 0 = 1$ and $\neg 1 = 0$, and that complementation reverses order: $x \le y \Rightarrow \bar y \le \bar x$, where $x \le y$ means $x \land y = x$.

**26.** *(§7.6, §8.2)* Prove the canonical CNF theorem directly (without invoking duality): every $n$-ary Boolean function equals the conjunction of the maxterms of its false rows, and the representation is unique.

**27.** *(§7.7)* Prove that $\{\Rightarrow, 0\}$ is functionally complete by expressing $\neg$, $\lor$ and $\land$ in terms of $\Rightarrow$ and the constant $0$.

**28.** *(§7.7)* Prove that $\{\oplus, \land, 1\}$ is functionally complete.

**29.** *(§8.4)* Prove carefully that every minimal sum-of-products expression for a function consists of prime implicants. Explain why this does not make K-map minimisation easy in general.

**30.** *(§7.4, §7.8)* Prove the dual consensus theorem $(x \lor y)(\bar x \lor z)(y \lor z) = (x \lor y)(\bar x \lor z)$ algebraically, and explain its role in eliminating a static-1 hazard.

**31.** *(§7.11, §8.6)* For $N = 30$, list the divisors and exhibit the isomorphism between the divisor Boolean algebra and the power set of the prime factors. Then state how many elements a Boolean algebra with five atoms has.

**32.** *(§7.7)* Show that NAND is not associative by computing $(1 \uparrow 1) \uparrow 0$ and $1 \uparrow (1 \uparrow 0)$. Which parenthesisation computes which function?

## Challenge

**33.** *(§7.7, §7.9)* Using Post's theorem, show that each of the fourteen two-input connectives other than NAND and NOR fails to be complete by identifying a property it preserves ($T_0$: $f(0,\dots,0) = 0$; $T_1$: $f(1,\dots,1) = 1$; monotone; self-dual: $f(\bar x) = \overline{f(x)}$; affine over $\mathbb{F}_2$).

**34.** *(§7.6, §7.7)* Prove that a Boolean function is monotone (in the sense of Theorem 7.8) if and only if it can be expressed by a formula using only variables, $\land$, $\lor$ and the constants $0, 1$ — that is, without negation.

**35.** *(§7.11)* Prove that every Boolean function of $n$ variables has a unique representation as a multilinear polynomial over $\mathbb{F}_2$ (its *algebraic normal form*), and compute the ANF of $x \oplus y$, of $x \land y$ and of $x \lor y$.

**36.** *(§7.6, §8.4)* Prove that any DNF computing the parity function $x_1 \oplus \cdots \oplus x_n$ must contain at least $2^{n-1}$ terms, and that the canonical DNF attains this bound.
