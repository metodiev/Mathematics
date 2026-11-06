# Relations and Functions — Exercises

> Part of [Relations and Functions](README.md) · 33 problems · Full solutions: [solutions.md](solutions.md)

Write out your reasoning, not only the final answer. For every "decide whether" question, give
either a proof or an explicit counterexample.

---

## Beginner

**1.** Let $A = \{1,2\}$ and $B = \{a,b,c\}$. List $A \times B$ and $B \times A$. How many elements
does each have, and are the two sets equal?

**2.** Let $A = \{1,2,3,4\}$, $B = \{2,4,6\}$ and $R = \{(a,b) \in A \times B : b = 2a\}$. List $R$,
and find $\operatorname{dom} R$, $\operatorname{ran} R$ and $R^{-1}$.

**3.** Let $R = \{(x,y) \in \mathbb{Z} \times \mathbb{Z} : x^2 + y^2 = 25\}$. List every element of
$R$, and state $\operatorname{dom} R$ and $\operatorname{ran} R$.

**4.** On $A = \{1,2,3\}$ let $R = \{(1,1),(2,2),(3,3),(1,2),(2,1)\}$. Decide which of the four
properties reflexive, symmetric, antisymmetric, transitive hold, and justify each answer.

**5.** On $A = \{1,2,3,4\}$ let $R = \{(a,b) : a \mid b\}$. List $R$ as a set of pairs, and decide
which of the four properties hold. Is $R$ total?

**6.** Which of the following are functions from $\{1,2,3\}$ to $\{p,q,r\}$? Explain each answer.

(a) $\{(1,p),(2,q),(3,r)\}$;

(b) $\{(1,p),(2,p),(3,p)\}$;

(c) $\{(1,p),(2,q)\}$;

(d) $\{(1,p),(1,q),(2,r),(3,r)\}$;

(e) $\{(1,q),(2,p),(3,q)\}$.

**7.** Let $f : \{1,2,3,4\} \to \{a,b,c\}$ be given by $f(1) = a$, $f(2) = c$, $f(3) = a$,
$f(4) = b$. Find the image of $f$, and decide whether $f$ is injective and whether it is surjective.

**8.** On $\mathbb{R}$ let $f(x) = x + 2$ and $g(x) = 3x$. Compute $g \circ f$ and $f \circ g$, and
evaluate both at $x = 1$.

**9.** Let $f : \mathbb{R} \to \mathbb{R}$, $f(x) = 5x - 2$. Prove that $f$ is bijective, find
$f^{-1}$, and verify both identities $f^{-1}(f(x)) = x$ and $f(f^{-1}(y)) = y$.

**10.** For congruence modulo $4$ on $\mathbb{Z}$, describe the four equivalence classes and list the
members of each class that lie between $-4$ and $8$ inclusive.

**11.** On $D = \{1,2,4,8\}$ order by divisibility. Describe the order, decide whether it is total,
and draw the Hasse diagram.

**12.** How many functions are there from a $3$-element set to a $4$-element set? How many of them
are injective?

---

## Intermediate

**13.** Let $R$ be an equivalence relation on a set $A$. Prove that $R^{-1}$ is also an equivalence
relation on $A$.

**14.** On $\mathbb{Z}$ define $a \sim b$ iff $a \equiv b \pmod 6$.

(a) Prove that $\sim$ is an equivalence relation.

(b) List the members of $[2]$ that lie between $-10$ and $20$ inclusive.

(c) Explain why there are exactly six equivalence classes.

**15.** On $\mathbb{R}$ define $x \sim y$ iff $x - y \in \mathbb{Z}$.

(a) Prove that $\sim$ is an equivalence relation.

(b) Describe the classes $[0]$, $[1/2]$ and $[\sqrt2]$, and explain why they are distinct.

**16.** Let $f : A \to B$ and $g : B \to C$.

(a) Prove that if $g \circ f$ is injective, then $f$ is injective.

(b) Give an explicit example in which $g \circ f$ is injective but $g$ is not.

**17.** Let $f : \mathbb{R} \to \mathbb{R}$, $f(x) = x^2$. Compute $f([-3,2])$, $f^{-1}([1,9])$ and
$f^{-1}((-1,0])$.

**18.** Let $R$ be a relation on a set $A$.

(a) Prove that $R$ is symmetric if and only if $R^{-1} = R$.

(b) Prove that $R$ is reflexive if and only if $\operatorname{id}_A \subseteq R$.

**19.** Let $f : A \to B$ and let $X, Y \subseteq A$.

(a) Prove that $f(X \cup Y) = f(X) \cup f(Y)$.

(b) Give an explicit example in which $f(X \cap Y) \ne f(X) \cap f(Y)$.

**20.** Let $R$ be an antisymmetric and transitive relation on $A$. Define $x < y$ to mean $x \, R \, y$
and $x \ne y$. Prove that $<$ is irreflexive and transitive.

**21.** Let $f : \mathbb{R} \to \mathbb{R}$, $f(x) = (x+1)^2$. Decide whether $f$ is injective and
whether it is surjective, find $f(\mathbb{R})$, and exhibit a restriction of $f$ that is bijective
onto its image, together with the inverse of that restriction.

**22.** List every partition of $\{1,2,3,4\}$, and for each one describe the equivalence relation it
determines. How many are there, and how does the number compare with the number of partitions of a
$4$-element set given by the Bell number $B_4$?

---

## Advanced

**23.** Let $f : A \to B$. Prove that $f$ is injective if and only if
$f(X \cap Y) = f(X) \cap f(Y)$ for all $X, Y \subseteq A$.

**24.** Let $A$ and $B$ be finite sets with $|A| = |B| = n$, and let $f : A \to B$. Prove that the
following are equivalent: $f$ is injective; $f$ is surjective; $f$ is bijective.

**25.** Let $R$ be a relation on a set $A$. Prove that $R$ is transitive if and only if
$R \circ R \subseteq R$.

**26.** Let $R$ be a relation on $A$ that is symmetric and transitive. Prove that $R$ is reflexive on
its field $\operatorname{fld} R$. Show by example that $R$ need not be reflexive on all of $A$.

**27.** Let $\mathcal{P}$ be a partition of $A$. Define $a \sim b$ iff $a$ and $b$ lie in the same
block of $\mathcal{P}$. Prove that $\sim$ is an equivalence relation and that its equivalence
classes are exactly the blocks of $\mathcal{P}$.

**28.** Let $|A| = n$. Count (a) the reflexive relations on $A$, (b) the symmetric relations on $A$,
(c) the irreflexive relations on $A$. Justify each count by saying which pairs are free.

**29.** Prove that composition of relations is associative: for relations
$R \subseteq A \times B$, $S \subseteq B \times C$ and $T \subseteq C \times D$,

$$(T \circ S) \circ R = T \circ (S \circ R).$$

---

## Challenge

**30.** (a) Prove Cantor's theorem: there is no surjection from $A$ onto its power set
$\mathcal{P}(A)$.

(b) Deduce that $|A| < |\mathcal{P}(A)|$ for every set $A$, where $|X| \le |Y|$ means that there is
an injection $X \to Y$.

(c) Explain why $|\mathcal{P}(A)| = |\{0,1\}^A|$.

**31.** A **derangement** is a bijection $f : \{1,\dots,n\} \to \{1,\dots,n\}$ with $f(i) \ne i$ for
every $i$.

(a) List all derangements of $\{1,2,3\}$ and count them.

(b) List all derangements of $\{1,2,3,4\}$ and count them.

(c) Explain why the number of derangements of a $4$-element set is not $4! - 4 \cdot 3!$.

**32.** On $\mathbb{N}^{+}$ define $a \sim b$ iff $b = 2^k a$ for some $k \in \mathbb{Z}$.

(a) Prove that $\sim$ is an equivalence relation.

(b) Describe the class $[1]$ and the class $[3]$.

(c) Show that each class contains exactly one odd number, and deduce how many classes there are.

**33.** (a) Prove that every finite nonempty partially ordered set has a minimal element.

(b) Deduce that every finite nonempty total order has a least element.

(c) Give an example of an infinite poset with no minimal element, and one with a minimal element but
no least element.
