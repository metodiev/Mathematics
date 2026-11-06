# Set Theory — Exercises

> [Set Theory](README.md) · 34 problems · Beginner → Challenge · Solutions: [solutions.md](solutions.md)

Work through the problems in order. Every problem is solvable with the definitions and theorems of
the tutorial; the section reference in each problem tells you where to look. Do not consult
[solutions.md](solutions.md) until you have written an attempt — the attempt is where the learning
happens.

Notation follows the tutorial: $\mathbb{N} = \{0,1,2,\dots\}$, complements are taken in the universe
named in the problem, and $\mathcal{P}(A)$ is the power set of $A$.

## Beginner

**1.** *(§7.2)*
(a) Write $S = \{x \in \mathbb{Z} : -2 \le x < 3\}$ in roster form.
(b) Write $T = \{1, 4, 9, 16, 25\}$ in set-builder notation in two essentially different ways.
(c) Describe the set $\{x \in \mathbb{N} : x + 5 = 3\}$ in words and in roster form.

**2.** *(§7.1)* Decide whether each statement is true or false, and justify in one line.
(a) $2 \in \{1, \{2,3\}\}$
(b) $\{2\} \in \{1, \{2,3\}\}$
(c) $\varnothing \subseteq \{\varnothing\}$
(d) $\varnothing \in \{\varnothing\}$
(e) $\{\varnothing\} \subseteq \{\varnothing, \{\varnothing\}\}$
(f) $\{1\} \subseteq \{1, \{1\}\}$

**3.** *(§7.3)* Let $A = \{1,2,3\}$. List every subset of $A$. How many subsets are there in total,
and how many of them are proper subsets?

**4.** *(§7.3)*
(a) How many subsets does a set with $6$ elements have?
(b) Compute $\mathcal{P}(\mathcal{P}(\varnothing))$ explicitly, list its elements, and state
$|\mathcal{P}(\mathcal{P}(\varnothing))|$.

**5.** *(§7.4)* Let $U = \{1,2,3,4,5,6,7,8\}$, $A = \{1,2,3,5,8\}$ and $B = \{2,4,6,8\}$. Compute
$A \cup B$, $A \cap B$, $A \setminus B$, $B \setminus A$, $A^{c}$ and $A \mathbin{\triangle} B$.

**6.** *(§7.7)* Let $A = \{1,2\}$ and $B = \{a,b\}$.
(a) List the elements of $A \times B$, $B \times A$ and $A \times A$.
(b) Compute $|A \times B \times A|$ without listing all the triples.
(c) Is $A \times B = B \times A$? Justify your answer by naming an element of one set that is not in
the other.

**7.** *(§7.3)* Prove the following for arbitrary sets $A$ and $B$.
(a) $\varnothing \subseteq A$.
(b) $A \cap B \subseteq A$ and $A \subseteq A \cup B$.

**8.** *(§7.8)* Compute $\displaystyle\bigcup_{n=1}^{4}\left[\frac{1}{n},\,1\right]$ and
$\displaystyle\bigcap_{n=1}^{4}\left[\frac{1}{n},\,1\right]$, expressing each as a single interval.

**9.** *(§7.4)* Decide whether each statement is true for all sets $A$; justify each answer.
(a) $A \cup \varnothing = A$
(b) $A \cap \varnothing = A$
(c) $A \mathbin{\triangle} \varnothing = A$
(d) $A \mathbin{\triangle} A = \varnothing$
(e) $A \setminus A = \varnothing$
(f) $A \setminus \varnothing = A$

**10.** *(§7.10)* Classify each set as finite, countably infinite, or uncountable:
(a) $\{1,2,3\}$; (b) $\mathbb{Z}$; (c) $\mathbb{Q}$; (d) $\mathbb{R}$;
(e) $\mathcal{P}(\mathbb{N})$; (f) the set of prime numbers.

**11.** *(§7.4)* Let $U = \{1,2,\dots,10\}$, $A = \{2,4,6,8,10\}$ and $B = \{1,2,3,4,5\}$.
Compute $A \mathbin{\triangle} B$, then verify explicitly that
$A \mathbin{\triangle} B = (A \cup B) \setminus (A \cap B)$.

## Intermediate

**12.** *(§8.4)* Prove that for all sets $A$ and $B$,
$$A \subseteq B \quad \Longleftrightarrow \quad A \cup B = B.$$

**13.** *(§7.6)* Prove that for all sets $A$, $B$, $C$,
$$A \cap (B \setminus C) = (A \cap B) \setminus (A \cap C).$$

**14.** *(§7.6)* Prove that for all sets $A$, $B$, $C$,
$$(A \cup B) \setminus C = (A \setminus C) \cup (B \setminus C).$$

**15.** *(§7.4, §7.6)*
(a) Prove that $A \mathbin{\triangle} B = (A \cup B) \setminus (A \cap B)$.
(b) Deduce that $A \mathbin{\triangle} B = \varnothing$ if and only if $A = B$.

**16.** *(§7.3)* Prove that for all sets $A$ and $B$,
$$A \subseteq B \quad \Longleftrightarrow \quad \mathcal{P}(A) \subseteq \mathcal{P}(B).$$

**17.** *(§7.7)* Prove that for all sets $A$ and $B$ the map
$$f : A \times B \to B \times A, \qquad f(a,b) = (b,a)$$
is a bijection, and deduce $|A \times B| = |B \times A|$.

**18.** *(§8.2)* Using a truth table with all $8$ membership patterns for three sets, prove
$$A \cup (B \cap C) = (A \cup B) \cap (A \cup C).$$

**19.** *(§7.8)* Let $A, B, C$ be subsets of a universe $U$. Prove
$$(A \cup B \cup C)^{c} = A^{c} \cap B^{c} \cap C^{c}.$$

**20.** *(§7.9)*
(a) Prove that if $A \subseteq B$ then $|A| \le |B|$.
(b) Give an example of sets $A \subsetneq B$ with $|A| = |B|$, exhibiting an explicit bijection.

**21.** *(§7.10)* Prove that the function $f : \mathbb{N} \to \mathbb{Z}$ defined by
$$f(2k) = k, \qquad f(2k+1) = -(k+1) \quad (k \ge 0)$$
is a bijection.

## Advanced

**22.** *(§7.12)*
(a) Prove that no set $A$ satisfies $\mathcal{P}(A) \subseteq A$.
(b) Deduce that there is no set of all sets.
(c) State exactly where your argument uses Cantor's theorem.

**23.** *(§7.11)* Prove that the open interval $(0,1)$ is uncountable. Use a diagonal argument and
make sure your constructed number really lies in $(0,1)$. State and prove the lemma on decimal
expansions that you use.

**24.** *(§7.10)* Prove that the union of two countably infinite sets is countably infinite by
constructing an explicit bijection. Then deduce that every finite union of countable sets is
countable.

**25.** *(§7.8)* For $n \ge 2$ let $I_n = \left[1 + \frac{1}{n},\ 3 - \frac{1}{n}\right]$. Prove
$$\bigcup_{n \ge 2} I_n = (1,3) \qquad \text{and} \qquad \bigcap_{n \ge 2} I_n = \left[\frac32, \frac52\right].$$
Which property of $\mathbb{R}$ do you use, and where?

**26.** *(§7.8)* Let $\{A_i\}_{i \in I}$ be a family of subsets of a universe $U$.
(a) Prove the generalized De Morgan law
$$U \setminus \bigcap_{i \in I} A_i = \bigcup_{i \in I} (U \setminus A_i).$$
(b) Explain what the two generalized De Morgan laws say when $I = \varnothing$, and check that both
reductions are correct.

**27.** *(§7.12, §7.13)* Let $X$ be a set and let $R = \{x \in X : x \notin x\}$.
(a) Prove that $R \notin X$.
(b) Deduce that no set contains all sets.
(c) Explain where the Axiom of Separation is used, and why Russell's original argument is not a
valid proof in ZFC.

**28.** *(§7.11)* Prove that $|\mathbb{N} \times \mathbb{N}| = |\mathbb{N}|$ by exhibiting an explicit
bijection. (Suggestion: use the fundamental theorem of arithmetic — unique prime factorisation — and
write every positive integer as $2^{m}$ times an odd number.)

**29.** *(§7.10)* Let $A$ be an uncountable set with $A \subseteq B$. Prove that $B$ is uncountable.
Deduce that $\mathbb{R} \setminus \mathbb{Q}$ is uncountable, given that $\mathbb{Q}$ is countable.

**30.** *(§7.9)* Prove that if $|A| = |B|$ then $|\mathcal{P}(A)| = |\mathcal{P}(B)|$.

## Challenge

**31.** *(§7.10, §7.12)*
(a) Prove that the set of all finite subsets of $\mathbb{N}$ is countable.
(b) Deduce that the set of finite binary strings is countable, while the set of infinite binary
sequences is uncountable.

**32.** *(§7.9, §7.11)* Construct an explicit bijection $(0,1] \to (0,1)$ and an explicit bijection
$[0,1] \to (0,1)$, and prove that each is bijective. (Hint: the sets are equal except for a
countable "queue" of points; shift along the queue.)

**33.** *(§7.12)* Using the Cantor–Schröder–Bernstein theorem (Theorem 7.6), prove
$$|\mathcal{P}(\mathbb{N})| = |\mathbb{R}|.$$
You may use the standard facts that between any two distinct real numbers there is a rational
number, and that every real number has a base-3 expansion.

**34.** *(§7.14)* The Axiom of Foundation states that every nonempty set $S$ has an element $x$ with
$x \cap S = \varnothing$. Using it, prove that no set is an element of itself: for all sets $x$,
$x \notin x$. Explain why this makes the property used in Russell's paradox unsatisfiable in ZFC.
