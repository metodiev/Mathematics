# Set Theory — Solutions

> [Set Theory](README.md) · Solutions to the 34 problems in [exercises.md](exercises.md)

Each solution begins with the strategy, then carries out every step. For proof problems the proof is
complete. Where a second approach exists it is shown after the first.

## Beginner

**1.** *Strategy: for roster form, test the defining inequality on integers; for set-builder form, find the
pattern and then pin down the range; for (c), solve the equation first and only then test
membership.*

(a) The integers satisfying $-2 \le x < 3$ are $-2,-1,0,1,2$, so
$S = \{-2,-1,0,1,2\}$.

(b) Two correct descriptions:

$$T = \{\,n^2 : n \in \{1,2,3,4,5\}\,\}, \qquad
T = \{\,x \in \mathbb{N} : \exists n \in \mathbb{N},\ 1 \le n \le 5 \text{ and } x = n^2\,\}.$$

The first is shorter; the second makes explicit that $x$ is a natural number and that the witness $n$
is bounded. Both are legitimate because both specify exactly the five numbers $1,4,9,16,25$.

(c) The equation $x + 5 = 3$ has the single solution $x = -2$, and $-2 \notin \mathbb{N}$. Hence
$\{x \in \mathbb{N} : x + 5 = 3\} = \varnothing$: it is the set of natural numbers equal to $-2$,
and there are none.

*Pitfall:* the set is not $\{-2\}$. The domain restriction $x \in \mathbb{N}$ is part of the
definition and removes the solution.

**2.** *Strategy: for each statement decide whether the object on the left of $\in$ (or $\subseteq$) is
literally an element (or subset) of the set on the right, listing the elements when necessary.*

The set $\{1,\{2,3\}\}$ has exactly two elements: the number $1$ and the set $\{2,3\}$.

(a) **False.** $2$ is not $1$, and $2$ is not the set $\{2,3\}$. It is an element of the *element*
$\{2,3\}$, not an element of the whole set.

(b) **False.** Same reason: the elements of $\{1,\{2,3\}\}$ are $1$ and $\{2,3\}$. The set $\{2\}$ is
neither of them. (It is the set $\{2,3\}$ that belongs, not $\{2\}$.)

(c) **True.** $\varnothing$ has no elements, so every statement of the form "if $x \in \varnothing$
then …" is vacuously true; in particular $\varnothing \subseteq \{\varnothing\}$.

(d) **True.** $\{\varnothing\}$ has exactly one element, namely $\varnothing$.

(e) **True.** The only element of $\{\varnothing\}$ is $\varnothing$, and
$\varnothing \in \{\varnothing,\{\varnothing\}\}$.

(f) **True.** $1 \in \{1,\{1\}\}$, so the set $\{1\}$ has all its elements (just $1$) in
$\{1,\{1\}\}$.

*Pitfall:* parts (a) and (b) are the classic trap. Reading the elements aloud avoids it: "the
elements are $1$ and $\{2,3\}$; is $\{2\}$ one of them? No." Note also that (d) and (c) are both
true even though $\varnothing$ and $\{\varnothing\}$ are different objects.

**3.** *Strategy: build the subsets by size. There is one of size $0$, three of size $1$, three of size $2$,
and one of size $3$ — the pattern $1,3,3,1$.*

The subsets of $A = \{1,2,3\}$ are

$$\varnothing, \quad \{1\}, \{2\}, \{3\}, \quad \{1,2\}, \{1,3\}, \{2,3\}, \quad \{1,2,3\}.$$

There are $8 = 2^3$ in total, in agreement with Theorem 7.1. A proper subset is a subset different
from $A$ itself, so all but $\{1,2,3\}$ qualify: $8 - 1 = 7$ proper subsets. Note that
$\varnothing$ is a proper subset, because $\varnothing \neq \{1,2,3\}$.

**4.** *Strategy: use $|\mathcal{P}(A)| = 2^{|A|}$ twice, and remember that $\mathcal{P}(\varnothing)$ is
not empty.*

(a) $|\mathcal{P}(A)| = 2^{6} = 64$.

(b) First, $\mathcal{P}(\varnothing) = \{\varnothing\}$, a set with one element. Then
$\mathcal{P}(\mathcal{P}(\varnothing)) = \mathcal{P}(\{\varnothing\})$, whose elements are the
subsets of $\{\varnothing\}$, namely $\varnothing$ and $\{\varnothing\}$:

$$\mathcal{P}(\mathcal{P}(\varnothing)) = \{\,\varnothing,\ \{\varnothing\}\,\}, \qquad
|\mathcal{P}(\mathcal{P}(\varnothing))| = 2 = 2^{2^{0}}.$$

*Check:* the outer power set has $2^{|\mathcal{P}(\varnothing)|} = 2^{1} = 2$ elements. ✓

**5.** *Strategy: apply each membership criterion in Definition 5.6 separately; do not try to guess the
answers from a picture.*

With $U = \{1,2,3,4,5,6,7,8\}$, $A = \{1,2,3,5,8\}$ and $B = \{2,4,6,8\}$:

| Expression | Value | How |
|---|---|---|
| $A \cup B$ | $\{1,2,3,4,5,6,8\}$ | all elements of either set |
| $A \cap B$ | $\{2,8\}$ | elements in both |
| $A \setminus B$ | $\{1,3,5\}$ | in $A$, not in $B$ (remove $2$ and $8$) |
| $B \setminus A$ | $\{4,6\}$ | in $B$, not in $A$ |
| $A^{c}$ | $\{4,6,7\}$ | in $U$, not in $A$ |
| $A \triangle B$ | $\{1,3,4,5,6\}$ | exactly one of the two sets |

*Check:* $A \triangle B$ should equal $(A \setminus B) \cup (B \setminus A)$, which is
$\{1,3,5\} \cup \{4,6\} = \{1,3,4,5,6\}$. ✓ And $|A \cup B| = 7 = 5 + 4 - 2$. ✓

**6.** *Strategy: write ordered pairs with round brackets, first coordinate from the first factor. For (c),
find a single element that belongs to one product but cannot belong to the other.*

(a)

$$A \times B = \{(1,a),(1,b),(2,a),(2,b)\},$$
$$B \times A = \{(a,1),(a,2),(b,1),(b,2)\},$$
$$A \times A = \{(1,1),(1,2),(2,1),(2,2)\}.$$

(b) The product $A \times B \times A$ consists of triples. By the product rule (Theorem 7.2
iterated), $|A \times B \times A| = 2 \cdot 2 \cdot 2 = 8$. Explicitly, they are
$(1,a,1),(1,a,2),(1,b,1),(1,b,2),(2,a,1),(2,a,2),(2,b,1),(2,b,2)$.

(c) **No.** The element $(1,a)$ belongs to $A \times B$. If $(1,a) \in B \times A$, then its first
coordinate would have to lie in $B = \{a,b\}$, but $1 \notin \{a,b\}$. Hence
$(1,a) \notin B \times A$ and the two products are different sets.

**7.** *Strategy: prove inclusions by taking an arbitrary element of the smaller set and unpacking the
definitions; the first part is a vacuous implication.*

(a) We must show $\forall x\,(x \in \varnothing \rightarrow x \in A)$. Let $x$ be arbitrary. The
hypothesis $x \in \varnothing$ is false by definition of $\varnothing$, so the implication is true
(vacuously). Since $x$ was arbitrary, $\varnothing \subseteq A$.

(b) For the first inclusion, let $x \in A \cap B$. By definition of intersection, $x \in A$ and
$x \in B$; in particular $x \in A$. Hence $A \cap B \subseteq A$. For the second, let $x \in A$. Then
the statement "$x \in A$ or $x \in B$" is true (the first disjunct holds), so $x \in A \cup B$ by
Definition 5.6. Hence $A \subseteq A \cup B$.

*Remark:* both inclusions are special cases of the lattice picture in §10: the intersection is the
smallest set containing both, the union the largest.

**8.** *Strategy: compute the four intervals and observe that one of them contains all others; the union of
nested sets is the largest, the intersection the smallest.*

For $n = 1,2,3,4$ the intervals are $[1,1]$, $[\tfrac12, 1]$, $[\tfrac13,1]$, $[\tfrac14,1]$, and

$$\left[\tfrac14,1\right] \supseteq \left[\tfrac13,1\right] \supseteq \left[\tfrac12,1\right] \supseteq [1,1].$$

Therefore

$$\bigcup_{n=1}^{4}\left[\frac1n,1\right] = \left[\frac14,1\right], \qquad
\bigcap_{n=1}^{4}\left[\frac1n,1\right] = [1,1] = \{1\}.$$

The union is the largest member of a nested family and the intersection is the smallest. In general,
for a nested family $J_1 \supseteq J_2 \supseteq \cdots \supseteq J_m$, the union is $J_1$ and the
intersection is $J_m$.

**9.** *Strategy: substitute each candidate into the definitions; when a statement is false, produce a
concrete counterexample.*

(a) **True.** $x \in A \cup \varnothing$ iff $x \in A$ or $x \in \varnothing$; the second disjunct is
always false, so this is equivalent to $x \in A$.

(b) **False.** $x \in A \cap \varnothing$ iff $x \in A$ and $x \in \varnothing$; the second conjunct
is always false, so $A \cap \varnothing = \varnothing$, not $A$ (unless $A = \varnothing$).
Counterexample: $A = \{1\}$ gives $\{1\} \cap \varnothing = \varnothing \neq \{1\}$.

(c) **True.** $A \triangle \varnothing$ collects the elements in exactly one of $A$ and
$\varnothing$; no element is in $\varnothing$, so this is exactly $A$.

(d) **True.** No $x$ can be in exactly one of $A$ and $A$: either it is in both or in neither.

(e) **True.** $x \in A \setminus A$ would require $x \in A$ and $x \notin A$.

(f) **True.** $x \in A \setminus \varnothing$ iff $x \in A$ and $x \notin \varnothing$; the second
condition is automatic.

**10.** *Strategy: quote the results of §7.10–7.12 and, for (f), use that an infinite subset of
$\mathbb{N}$ is countably infinite.*

(a) $\{1,2,3\}$: **finite**, with three elements.
(b) $\mathbb{Z}$: **countably infinite** (Theorem 7.12; an explicit bijection is Exercise 21).
(c) $\mathbb{Q}$: **countably infinite** (Theorem 7.12).
(d) $\mathbb{R}$: **uncountable** (Corollary 7.15).
(e) $\mathcal{P}(\mathbb{N})$: **uncountable** (Cantor's theorem gives
$|\mathbb{N}| < |\mathcal{P}(\mathbb{N})|$).
(f) The primes: **countably infinite**. The set is infinite (Euclid's theorem, proved in
[Proof Techniques](../04-proof-techniques/README.md)) and it is an infinite subset of
$\mathbb{N}$, hence countable by Lemma 7.8.

**11.** *Strategy: compute $A \triangle B$ from the definition, then compute the right-hand side
independently and compare.*

The elements in exactly one of $A = \{2,4,6,8,10\}$ and $B = \{1,2,3,4,5\}$ are:

* in $A$ but not $B$: $6, 8, 10$;
* in $B$ but not $A$: $1, 3, 5$.

Hence $A \triangle B = \{1,3,5,6,8,10\}$.

Now independently: $A \cup B = \{1,2,3,4,5,6,8,10\}$ (the number $7$ and $9$ belong to neither set)
and $A \cap B = \{2,4\}$. Therefore

$$(A \cup B) \setminus (A \cap B) = \{1,2,3,4,5,6,8,10\} \setminus \{2,4\} = \{1,3,5,6,8,10\},$$

which agrees with the direct computation. ✓

## Intermediate

**12.** *Strategy: an "if and only if" needs two directions. For $A \subseteq B \Rightarrow A \cup B = B$
prove two inclusions; one of them is automatic. For the converse, chase an element of $A$.*

**($\Rightarrow$)** Assume $A \subseteq B$.

* $B \subseteq A \cup B$ holds for any two sets, since every element of $B$ satisfies "$x \in A$ or
  $x \in B$" (cf. Exercise 7).
* For $A \cup B \subseteq B$: let $x \in A \cup B$. Then $x \in A$ or $x \in B$. In the first case
  $x \in B$ by the hypothesis $A \subseteq B$; in the second case $x \in B$ trivially. Either way
  $x \in B$.

Both inclusions give $A \cup B = B$.

**($\Leftarrow$)** Assume $A \cup B = B$. Let $x \in A$. Then $x \in A \cup B$ by definition of
union, hence $x \in B$ by the assumption. Therefore $A \subseteq B$. $\square$

*Remark:* the hypothesis $A \subseteq B$ is used exactly once, in the first case of the second
bullet. Without it the inclusion $A \cup B \subseteq B$ fails: take $A = \{1\}$, $B = \varnothing$.

**13.** *Strategy: double inclusion, unpacking "difference" as "and not". The only subtle point is turning
$x \notin A \cap C$ into $x \notin C$, which uses $x \in A$.*

**($\subseteq$)** Let $x \in A \cap (B \setminus C)$. Then $x \in A$, and $x \in B \setminus C$, which
means $x \in B$ and $x \notin C$. From $x \in A$ and $x \in B$ we get $x \in A \cap B$. Also
$x \notin A \cap C$: if $x$ were in $A \cap C$ it would be in $C$, contradicting $x \notin C$.
Therefore $x \in (A \cap B) \setminus (A \cap C)$.

**($\supseteq$)** Let $x \in (A \cap B) \setminus (A \cap C)$. Then $x \in A \cap B$, so $x \in A$
and $x \in B$; and $x \notin A \cap C$. Since $x \in A$, the statement $x \in A \cap C$ is equivalent
to $x \in C$; as it is false, $x \notin C$. Hence $x \in B \setminus C$, and with $x \in A$ this
gives $x \in A \cap (B \setminus C)$. $\square$

**Second approach (algebraic).** Using $X \setminus Y = X \cap Y^{c}$ and distributivity,

$$(A \cap B) \setminus (A \cap C) = (A \cap B) \cap (A \cap C)^{c}
= (A \cap B) \cap (A^{c} \cup C^{c}) = \bigl[(A \cap B) \cap A^{c}\bigr] \cup \bigl[(A \cap B) \cap C^{c}\bigr].$$

The first bracket is empty because $(A \cap B) \cap A^{c} \subseteq A \cap A^{c} = \varnothing$.
The second is $A \cap (B \cap C^{c}) = A \cap (B \setminus C)$. So the two sides agree. This route
uses the identities of §8.1 instead of element chasing; both are acceptable.

**14.** *Strategy: double inclusion. An element of the left side is in one of $A,B$ and outside $C$; split
into the two cases.*

**($\subseteq$)** Let $x \in (A \cup B) \setminus C$. Then $x \in A \cup B$ and $x \notin C$. Since
$x \in A \cup B$, either $x \in A$ or $x \in B$.

* If $x \in A$, then $x \in A \setminus C$.
* If $x \in B$, then $x \in B \setminus C$.

In either case $x \in (A \setminus C) \cup (B \setminus C)$.

**($\supseteq$)** Let $x \in (A \setminus C) \cup (B \setminus C)$. Then $x \in A \setminus C$ or
$x \in B \setminus C$. In the first case $x \in A \subseteq A \cup B$ and $x \notin C$; in the second
$x \in B \subseteq A \cup B$ and $x \notin C$. In both cases $x \in (A \cup B) \setminus C$. $\square$

*Remark:* the identity expresses that difference distributes over union. The analogous statement with
$\cup$ replaced by $\cap$, namely $(A \cap B) \setminus C = (A \setminus C) \cap (B \setminus C)$, is
also true, so difference distributes over both operations. What fails is putting the difference
*inside*: $(A \setminus B) \cup C$ and $(A \cup C) \setminus (B \cup C)$ differ in general (take
$A = \{1\}$, $B = \varnothing$, $C = \{2\}$).

**15.** *Strategy: for (a), both sides express "exactly one of $x \in A$, $x \in B$"; make that precise with
a case analysis. For (b), use (a) and the fact that a set is empty iff it has no elements.*

(a) Let $x$ be arbitrary. By definition, $x \in A \triangle B$ iff exactly one of
$x \in A$, $x \in B$ holds. On the other hand,

$$x \in (A \cup B) \setminus (A \cap B) \iff (x \in A \text{ or } x \in B) \text{ and } \neg(x \in A \text{ and } x \in B).$$

The right-hand condition says: at least one holds, and not both — which is exactly "exactly one
holds". Hence the two membership conditions are equivalent for every $x$, and the sets are equal.

(b) **($\Leftarrow$)** If $A = B$, then $A \triangle B = A \triangle A$, which is empty,
because no element can be in exactly one of $A$ and $A$ (Exercise 9(d)).

**($\Rightarrow$)** Assume $A \triangle B = \varnothing$. We prove $A \subseteq B$; the
other inclusion is symmetric. Let $x \in A$. If $x \notin B$, then $x$ is in exactly one of $A$, $B$,
so $x \in A \triangle B = \varnothing$ — impossible. Hence $x \in B$. Therefore
$A \subseteq B$, and by the same argument $B \subseteq A$, so $A = B$. $\square$

*Alternative for (b):* by (a), $A \triangle B = \varnothing$ iff
$(A \cup B) \setminus (A \cap B) = \varnothing$ iff $A \cup B \subseteq A \cap B$ (Proposition 8.2),
which forces $A \cup B = A \cap B$ and hence $A = B$.

**16.** *Strategy: the forward direction is a direct element chase through the definition of the power set.
The reverse direction has a one-line trick: $A$ is itself an element of $\mathcal{P}(A)$.*

**($\Rightarrow$)** Assume $A \subseteq B$. Let $S \in \mathcal{P}(A)$. By definition of the power
set, $S \subseteq A$; with $A \subseteq B$ and transitivity of inclusion (§7.3), $S \subseteq B$, so
$S \in \mathcal{P}(B)$. Hence $\mathcal{P}(A) \subseteq \mathcal{P}(B)$.

**($\Leftarrow$)** Assume $\mathcal{P}(A) \subseteq \mathcal{P}(B)$. Since $A \subseteq A$, we have
$A \in \mathcal{P}(A)$. By the assumption, $A \in \mathcal{P}(B)$, which means $A \subseteq B$.
$\square$

*Remark:* this is a good example of a converse that is *true*. Many implications in set theory
reverse only under extra hypotheses; here the "trick" of applying the hypothesis to the set $A$
itself settles it. Notice that the argument uses no property of $A$ other than $A \subseteq A$.

**17.** *Strategy: check the two defining properties of a bijection, using the characterisation
$(u,v) = (u',v') \iff u = u' \text{ and } v = v'$ of ordered pairs.*

**Well-defined:** for $(a,b) \in A \times B$ we have $b \in B$ and $a \in A$, so
$(b,a) \in B \times A$; thus $f$ maps into the stated codomain.

**Injective:** suppose $f(a_1,b_1) = f(a_2,b_2)$, i.e. $(b_1,a_1) = (b_2,a_2)$. By Definition 5.7,
$b_1 = b_2$ and $a_1 = a_2$, hence $(a_1,b_1) = (a_2,b_2)$.

**Surjective:** let $(b,a) \in B \times A$ be arbitrary. Then $(a,b) \in A \times B$ and
$f(a,b) = (b,a)$. Hence every element of $B \times A$ is in the image.

Therefore $f$ is a bijection, and by Definition 7.5, $|A \times B| = |B \times A|$. This holds for
infinite sets as well, since no counting is involved.

*Remark:* $f$ is its own inverse, since swapping twice returns the original pair.

**18.** *Strategy: build all eight membership patterns for $(A,B,C)$ and evaluate both sides in each row.
Agreement in all eight rows is a proof, because the rows exhaust the possibilities for any element.*

| $A$ | $B$ | $C$ | $B \cap C$ | $A \cup (B \cap C)$ | $A \cup B$ | $A \cup C$ | $(A \cup B) \cap (A \cup C)$ |
|---|---|---|---|---|---|---|---|
| 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 1 | 1 | 0 | 0 | 1 | 1 | 1 | 1 |
| 1 | 0 | 1 | 0 | 1 | 1 | 1 | 1 |
| 1 | 0 | 0 | 0 | 1 | 1 | 1 | 1 |
| 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 |
| 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 |
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

Columns 5 and 8 are identical in all eight rows. Since any $x$ falls into exactly one row, the
membership conditions are the same for all $x$, so the sets are equal. $\square$

*Remark:* the distributive law is the mirror image of the logical equivalence
$P \vee (Q \wedge R) \equiv (P \vee Q) \wedge (P \vee R)$. Adding the row labels $A,B,C$ in the first
three columns and reading $1$ as "true" makes this literally a truth table.

**19.** *Strategy: either chase elements using quantifier negation, or apply the two-set De Morgan law twice.
Both are shown; the second is shorter.*

**Direct chase.** Let $x \in U$. Then

$$x \in (A \cup B \cup C)^{c} \iff x \notin A \cup B \cup C
\iff \neg(x \in A \text{ or } x \in B \text{ or } x \in C)
\iff x \notin A \text{ and } x \notin B \text{ and } x \notin C
\iff x \in A^{c} \cap B^{c} \cap C^{c}.$$

**Two-step derivation.** Treat $A \cup B \cup C$ as $(A \cup B) \cup C$ and apply the two-set law
twice:

$$(A \cup B \cup C)^{c} = \bigl((A \cup B) \cup C\bigr)^{c} = (A \cup B)^{c} \cap C^{c}
= (A^{c} \cap B^{c}) \cap C^{c} = A^{c} \cap B^{c} \cap C^{c}.$$

Each equality is an instance of the two-set De Morgan law, which was proved by truth table in §8.2.
$\square$

*Remark:* the general form, for any finite number of sets, is
$\left(\bigcup_{i=1}^{n} A_i\right)^{c} = \bigcap_{i=1}^{n} A_i^{c}$, proved by induction; Exercise 26
does the infinite case.

**20.** *Strategy: (a) is a matter of exhibiting an injection; the inclusion map is the only natural
candidate. For (b), remove one element from $\mathbb{N}$ and shift.*

(a) Define $\iota : A \to B$ by $\iota(a) = a$; this makes sense because $A \subseteq B$. If
$\iota(a_1) = \iota(a_2)$ then $a_1 = a_2$, so $\iota$ is injective. Hence there is an injection
$A \to B$, which is exactly $|A| \le |B|$ by Definition 7.5.

(b) Take $A = \mathbb{N} \setminus \{0\} = \{1,2,3,\dots\}$ and $B = \mathbb{N} = \{0,1,2,\dots\}$.
Then $A \subsetneq B$. Define

$$f : A \to B, \qquad f(n) = n - 1.$$

*Injective:* if $n - 1 = m - 1$ then $n = m$.
*Surjective:* given $k \in B$, the element $k+1$ lies in $A$ and $f(k+1) = k$.
So $f$ is a bijection and $|A| = |B|$, even though $A$ is a proper subset of $B$. $\square$

*Remark:* this is impossible for finite sets. It is the first hint that "same size" for infinite sets
means something different from "has as many elements" in the counting sense. Exercise 32 carries the
idea further.

**21.** *Strategy: check injectivity by splitting into the two parity cases, and surjectivity by handling
non-negative and negative integers separately.*

First note that every natural number is either of the form $2k$ or of the form $2k+1$ with $k \ge 0$,
and these cases are exclusive, so $f$ is defined on all of $\mathbb{N}$.

**Injective.** Suppose $f(m) = f(n)$.

* If $m = 2k$ and $n = 2l$ are both even, then $k = l$, so $m = n$.
* If $m = 2k+1$ and $n = 2l+1$ are both odd, then $-(k+1) = -(l+1)$, so $k = l$, so $m = n$.
* If one index is even and the other odd, then one value of $f$ is $\ge 0$ (the even case: $k \ge 0$)
  and the other is $\le -1$ (the odd case: $-(k+1) \le -1$), so they cannot be equal.

Hence $f$ is injective.

**Surjective.** Let $z \in \mathbb{Z}$.

* If $z \ge 0$, then $z = f(2z)$ with $2z \in \mathbb{N}$.
* If $z < 0$, write $z = -j$ with $j \ge 1$ and put $k = j - 1 \ge 0$. Then
  $f(2k+1) = -(k+1) = -j = z$, and $2k+1 \in \mathbb{N}$.

Hence every integer is in the image, and $f$ is surjective. Therefore $f$ is a bijection and
$|\mathbb{N}| = |\mathbb{Z}|$. $\square$

*Remark:* the listing is $0, -1, 1, -2, 2, -3, 3, \dots$. The first few values are
$f(0) = 0$, $f(1) = -1$, $f(2) = 1$, $f(3) = -2$, $f(4) = 2$, confirming the pattern.

## Advanced

**22.** *Strategy: from $\mathcal{P}(A) \subseteq A$ build a surjection $A \to \mathcal{P}(A)$; this directly
contradicts Cantor's theorem without needing any cardinal arithmetic.*

(a) Suppose, for contradiction, that $\mathcal{P}(A) \subseteq A$. Then every subset of $A$ is an
element of $A$. Define

$$f : A \to \mathcal{P}(A), \qquad f(a) = a \cap A.$$

This is well defined: in ZFC every object is a set, so $a \cap A$ is a set, and it is a subset of $A$,
hence an element of $\mathcal{P}(A)$. It is surjective: given $S \in \mathcal{P}(A)$ we have
$S \subseteq A$, so $S \in A$ by the hypothesis, and then

$$f(S) = S \cap A = S.$$

Thus $f$ is a surjection $A \to \mathcal{P}(A)$, contradicting Theorem 7.17, which says no such
surjection exists. Hence $\mathcal{P}(A) \not\subseteq A$. $\square$

(b) If a set $U$ of all sets existed, then every subset of $U$ would be a set (by the Axiom of Power
Set it is already an element of $\mathcal{P}(U)$), hence an element of $U$ because $U$ contains all
sets. Therefore $\mathcal{P}(U) \subseteq U$, contradicting part (a). So no set of all sets
exists. $\square$

(c) Cantor's theorem is used in (a) as the statement "there is no surjection $A \to \mathcal{P}(A)$"
(Theorem 7.17). The rest of the argument is a direct construction: from the assumed inclusion we
manufacture such a surjection. Note that (b) is a second, independent proof of Corollary 7.19.

*Common pitfall:* writing "$\mathcal{P}(A) \subseteq A$ gives $|\mathcal{P}(A)| \le |A|$, but Cantor
gives $|A| < |\mathcal{P}(A)|$, so contradiction". That is correct but relies on the
Cantor–Schröder–Bernstein theorem to rule out the simultaneous inequalities. The construction above
is more elementary and avoids that detour.

**23.** *Strategy: run the diagonal argument inside $(0,1)$, choosing digits in $\{1,\dots,8\}$ so that the
constructed number cannot be $0$ or $1$ and cannot suffer the $0.4999\dots = 0.5$ ambiguity.*

**Lemma.** Every real number in $(0,1)$ has a decimal expansion $0.a_1a_2\cdots$ that is not
eventually all $9$s, and this expansion is unique: two digit sequences which are not eventually all
$9$s and which represent the same number are identical.

*Proof of the lemma.* The existence is the standard fact that every real in $[0,1]$ has a decimal
expansion, with the convention of choosing the terminating expansion when one exists (for instance
$0.5$ rather than $0.4999\dots$). For uniqueness, suppose $(a_n)$ and $(b_n)$ are distinct, neither
eventually $9$, and let $k$ be the least index with $a_k \neq b_k$; say $a_k < b_k$. Then
$b_k \ge a_k + 1$, so

$$\sum_{n \ge 1}\frac{b_n}{10^n} - \sum_{n \ge 1}\frac{a_n}{10^n}
\ge \frac{1}{10^k} - \sum_{n > k}\frac{9}{10^n}
= \frac{1}{10^k} - \frac{1}{10^k} = 0.$$

Equality requires $b_k - a_k = 1$ and $b_n - a_n = -9$ for every $n > k$, that is $a_n = 9$ and
$b_n = 0$ for all $n > k$, which forces $(a_n)$ to end in all $9$s. Since it does not, the difference
is strictly positive and the numbers are different. $\square$

**Proof of the theorem.** Suppose, for contradiction, that $(0,1)$ is countable. It is not finite, so
there is an enumeration $(0,1) = \{x_1, x_2, x_3, \dots\}$ with all $x_k$ distinct. For each $k$
choose a decimal expansion $x_k = 0.a_{k1}a_{k2}a_{k3}\cdots$ that is not eventually $9$ (possible by
the lemma).

Choose digits $d_n \in \{1,2,\dots,8\}$ with $d_n \neq a_{nn}$; this is possible because
$\{1,\dots,8\}$ has eight elements and at most one of them is forbidden. Define

$$x = 0.d_1d_2d_3\cdots.$$

Every digit of $x$ lies between $1$ and $8$, so

$$0.111\cdots \le x \le 0.888\cdots$$

and both endpoints lie strictly inside $(0,1)$; hence $x \in (0,1)$.

Since the enumeration covers $(0,1)$, there is some $k$ with $x = x_k$. The sequence $(d_n)$ is not
eventually $9$ (it contains no $9$ at all), and $(a_{kn})_n$ was chosen not eventually $9$. By the
uniqueness part of the lemma, the two expansions must coincide digit by digit; but at position $k$
they differ: the $k$-th digit of $x$ is $d_k \neq a_{kk}$. Contradiction.

Therefore no enumeration of $(0,1)$ exists, and $(0,1)$ is uncountable. $\square$

*Why the digit range matters:* had we allowed $d_n = 0$, the number $0.000\cdots = 0$ would lie
outside $(0,1)$; had we allowed $d_n = 9$, the constructed expansion could be the "all 9s" alias of a
number whose other expansion is on the list. Restricting to $\{1,\dots,8\}$ removes both problems at
once.

**24.** *Strategy: interleave two enumerations, then delete repetitions. The deletion step is what turns the
surjection into an injection; it must be defined carefully.*

(a) Let $A$ and $B$ be countably infinite, and fix enumerations
$A = \{a_0,a_1,a_2,\dots\}$, $B = \{b_0,b_1,b_2,\dots\}$ with distinct terms within each list
(possible because each set is in bijection with $\mathbb{N}$). Define the interleaved sequence

$$c_0 = a_0,\ c_1 = b_0,\ c_2 = a_1,\ c_3 = b_1,\ \dots, \quad \text{i.e. } c_{2k} = a_k,\ c_{2k+1} = b_k.$$

Its range is exactly $A \cup B$, so $k \mapsto c_k$ is a surjection $\mathbb{N} \to A \cup B$.

Now define $\varphi : \mathbb{N} \to A \cup B$ recursively by

$$\varphi(0) = c_0, \qquad \varphi(n+1) = c_{m(n)},$$

where $m(n)$ is the least index $m$ with $c_m \notin \{\varphi(0),\dots,\varphi(n)\}$. The definition
is legitimate: the set $\{\varphi(0),\dots,\varphi(n)\}$ is finite, while $A \cup B$ is infinite
(it contains the infinite set $A$), so the range of $(c_m)$ — which is $A \cup B$ — is not contained
in that finite set, and such an $m$ exists.

*$\varphi$ is injective:* by construction $\varphi(n+1)$ is different from all previous values, so
all values are pairwise distinct.

*$\varphi$ is surjective:* we show by induction on $m$ that every $c_m$ occurs among the values. For
$m = 0$, $c_0 = \varphi(0)$. For the step, assume $c_0,\dots,c_{m-1}$ all occur, and let $N$ be a
stage by which all of them have occurred. If $c_m$ has occurred by stage $N$, we are done. Otherwise
$c_m$ has not occurred by stage $N$. Every index $j < m$ has been used by stage $N$, while the index
$m$ has not, so the least unused index at stage $N+1$ is exactly $m$; hence
$\varphi(N+1) = c_m$. By induction every $c_m$ occurs, and since every element of $A \cup B$ is some
$c_m$, the map $\varphi$ is surjective.

Therefore $\varphi$ is a bijection $\mathbb{N} \to A \cup B$, so $A \cup B$ is countably infinite.
$\square$

(b) Let $S_1,\dots,S_n$ be countable sets. We prove by induction on $n$ that
$S_1 \cup \dots \cup S_n$ is countable. For $n = 1$ this is the hypothesis. For the step, write
$T = S_1 \cup \dots \cup S_{n-1}$, which is countable by the inductive hypothesis, and note
$S_1 \cup \dots \cup S_n = T \cup S_n$. If both $T$ and $S_n$ are finite, the union is finite. If at
least one of them is infinite and both are countable, then either it is countably infinite — and the
union is countably infinite by part (a) if the other is infinite, or by the padding argument of
Lemma 7.10 if the other is finite. In all cases the union is countable. $\square$

*Pitfall:* the interleaved sequence alone is not a bijection — if $A \cap B \neq \varnothing$ it
repeats elements, and if one set is finite it stalls. That is why the deletion step (or the surjection
lemma) is needed.

**25.** *Strategy: for the union, every point strictly between $1$ and $3$ must lie in some $I_n$, which needs
the Archimedean property; for the intersection, look for the smallest member of the family.*

**The union.** First, every $I_n$ is contained in $(1,3)$: if $x \in I_n$ then
$1 < 1 + \frac1n \le x \le 3 - \frac1n < 3$. Hence $\bigcup_{n \ge 2} I_n \subseteq (1,3)$.

Conversely, let $x \in (1,3)$. Put $\delta = \min\{x - 1,\ 3 - x\} > 0$. By the Archimedean property
of $\mathbb{R}$ there is an integer $n$ with $n \ge 2$ and $\frac1n \le \delta$ (take $n$ larger than
both $2$ and $1/\delta$). Then $\frac1n \le x - 1$ and $\frac1n \le 3 - x$, i.e.
$1 + \frac1n \le x \le 3 - \frac1n$. Hence $x \in I_n \subseteq \bigcup_{n \ge 2} I_n$. Therefore the
union is $(1,3)$.

**The intersection.** We show that $I_2$ is contained in every $I_n$ with $n \ge 2$. Since $n \ge 2$
gives $\frac1n \le \frac12$,

$$1 + \frac1n \le 1 + \frac12 = \frac32, \qquad 3 - \frac1n \ge 3 - \frac12 = \frac52.$$

So every $x \in I_2 = \left[\frac32, \frac52\right]$ satisfies $1 + \frac1n \le \frac32 \le x$ and
$x \le \frac52 \le 3 - \frac1n$, hence lies in $I_n$. Thus
$I_2 \subseteq \bigcap_{n \ge 2} I_n$. Since $I_2$ is itself one of the sets in the family, the
intersection is contained in $I_2$. Hence

$$\bigcap_{n \ge 2} I_n = I_2 = \left[\frac32, \frac52\right].$$

**Property used.** The Archimedean property — for every real $\delta > 0$ there is a positive integer
$n$ with $\frac1n \le \delta$ — is used in the union computation. The intersection needs no such
property: the family has a smallest member, $I_2$. $\square$

*Remark:* the family is *not* nested in the direction one might expect — $I_2$ is the smallest member
and the sets grow as $n$ increases — so the intersection is simply the smallest member, while the
union is the limiting open interval $(1,3)$, which is strictly larger than every $I_n$.

**26.** *Strategy: for (a), translate both sides into quantified statements and use the logical equivalence
$\neg\forall i\, P(i) \equiv \exists i\, \neg P(i)$. For (b), substitute $I = \varnothing$ and use the
conventions of Definition 5.8.*

(a) Let $x \in U$. Then

$$x \in U \setminus \bigcap_{i \in I} A_i
\iff x \in U \text{ and } x \notin \bigcap_{i \in I} A_i
\iff x \in U \text{ and } \neg\bigl(\forall i \in I,\ x \in A_i\bigr)$$
$$\iff x \in U \text{ and } \exists i \in I,\ x \notin A_i
\iff \exists i \in I,\ \bigl(x \in U \text{ and } x \notin A_i\bigr)
\iff \exists i \in I,\ x \in U \setminus A_i
\iff x \in \bigcup_{i \in I}(U \setminus A_i).$$

Since the chain holds for every $x \in U$, the two sets are equal. $\square$

(b) With $I = \varnothing$ the conventions are $\bigcup_{i \in \varnothing} A_i = \varnothing$ and
$\bigcap_{i \in \varnothing} A_i = U$.

*First law* $U \setminus \bigcup_{i \in I} A_i = \bigcap_{i \in I}(U \setminus A_i)$ becomes
$U \setminus \varnothing = U$ on the left and $\bigcap_{i \in \varnothing}(U \setminus A_i) = U$ on
the right (empty intersection of subsets of $U$). Both sides are $U$. ✓

*Second law* becomes $U \setminus U = \varnothing$ on the left and
$\bigcup_{i \in \varnothing}(U \setminus A_i) = \varnothing$ on the right. Both sides are
$\varnothing$. ✓

So the empty index set does not create an exception; this is precisely why the conventions for the
empty union and empty intersection are chosen the way they are. Choosing
$\bigcap_{i \in \varnothing} A_i = \varnothing$ instead would break the second law.

*Remark:* the two laws are "the same" statement in complementary form; each follows from the other by
replacing every $A_i$ with $U \setminus A_i$ and using $(U \setminus A_i)^{c} = A_i$ (double
complement).

**27.** *Strategy: the key computation is $R \in R \iff R \notin R$, obtained by substituting $R$ into its own
defining property. Everything else is bookkeeping about which set is being quantified over.*

(a) Let $X$ be a set and $R = \{x \in X : x \notin x\}$, which is a set by Separation. Suppose, for
contradiction, that $R \in X$. Then, unfolding the definition of $R$ at the element $R$,

$$R \in R \iff \bigl(R \in X \text{ and } R \notin R\bigr).$$

By the supposition $R \in X$, so the right side is equivalent to $R \notin R$. Hence
$R \in R \iff R \notin R$, which is impossible. Therefore the supposition is false and $R \notin X$.
$\square$

(b) Suppose some set $V$ contained every set. Apply (a) to $X = V$: the set
$R = \{x \in V : x \notin x\}$ satisfies $R \notin V$. But $R$ is a set, and $V$ contains every set,
so $R \in V$ — a contradiction. Hence no set contains all sets. $\square$

(c) Separation is used in the very first line, to know that
$R = \{x \in X : x \notin x\}$ is a set: the comprehension is restricted to elements of the
already-existing set $X$. Russell's original argument formed $\{x : x \notin x\}$ with no restriction,
which is exactly the principle ZFC rejects. In ZFC there is no set of all sets that are not elements
of themselves; for each $X$ there is a *different* set $R_X$, and part (a) shows $R_X$ escapes $X$.
So the paradox becomes a theorem about the unboundedness of the set-theoretic universe, not a
contradiction.

**28.** *Strategy: use unique factorisation to turn a pair of natural numbers into a single positive integer,
then shift by one to land in $\mathbb{N}$.*

**Claim.** $g : \mathbb{N} \times \mathbb{N} \to \mathbb{Z}_{>0}$, $g(m,n) = 2^{m}(2n+1)$, is a
bijection.

*Well-defined:* $2^m \ge 1$ and $2n+1 \ge 1$, so $g(m,n)$ is a positive integer.

*Injective:* suppose $2^{m}(2n+1) = 2^{m'}(2n'+1)$. By the fundamental theorem of arithmetic
(unique prime factorisation), the exponent of the prime $2$ on both sides is the same, so $m = m'$;
cancelling $2^m$ gives $2n+1 = 2n'+1$, hence $n = n'$.

*Surjective:* let $N \in \mathbb{Z}_{>0}$. Write $N = 2^{m} q$ with $q$ odd; this is possible by
dividing out all factors of $2$, and $m \ge 0$. Since $q$ is odd and positive, $q = 2n+1$ for a
unique $n \ge 0$. Then $g(m,n) = 2^m(2n+1) = N$.

Now define

$$f : \mathbb{N} \times \mathbb{N} \to \mathbb{N}, \qquad f(m,n) = g(m,n) - 1.$$

The map $k \mapsto k-1$ is a bijection $\mathbb{Z}_{>0} \to \mathbb{N}$, so the composition $f$ is a
bijection. Explicitly, $f(0,0) = 0$, $f(0,1) = 2$, $f(1,0) = 1$, $f(0,2) = 4$, $f(1,1) = 5$,
$f(2,0) = 3$, and so on. Therefore $|\mathbb{N} \times \mathbb{N}| = |\mathbb{N}|$. $\square$

**Second approach (diagonal enumeration).** The listing of Theorem 7.11,
$(0,0);(0,1),(1,0);(0,2),(1,1),(2,0);\dots$, is already a bijection; its inverse sends a pair to its
position in the list. That proof uses no number theory, but the formula above is more explicit.

*Pitfall:* the map $(m,n) \mapsto 2^m 3^n$ is injective but not surjective; the factor $2n+1$ is what
makes the formula hit every positive integer exactly once.

**29.** *Strategy: an uncountable set cannot inject into $\mathbb{N}$; a subset of a countable set does.*

**First part.** Let $A$ be uncountable and $A \subseteq B$. Suppose, for contradiction, that $B$ is
countable. Then there is a bijection $B \to S$ onto a subset $S \subseteq \mathbb{N}$ if $B$ is
countably infinite, or $B$ is finite. In either case the restriction of that map to $A \subseteq B$
is an injection $A \to \mathbb{N}$ (compose with the inclusion $S \subseteq \mathbb{N}$). An
injection $A \to \mathbb{N}$ makes $A$ equinumerous with a subset of $\mathbb{N}$, which is countable
by Lemma 7.8. That contradicts the uncountability of $A$. Hence $B$ is uncountable. $\square$

**Deduction.** We know $\mathbb{Q}$ is countable (Theorem 7.12) and $\mathbb{R}$ is uncountable
(Corollary 7.15). Suppose $\mathbb{R} \setminus \mathbb{Q}$ were countable. Then

$$\mathbb{R} = \mathbb{Q} \cup (\mathbb{R} \setminus \mathbb{Q})$$

would be the union of two countable sets, hence countable by Lemma 7.10. This contradicts the
uncountability of $\mathbb{R}$. Therefore $\mathbb{R} \setminus \mathbb{Q}$ is uncountable. $\square$

*Alternative for the deduction:* applying the first part to the set of irrationals as $A$ and to
$\mathbb{R}$ as $B$ gives nothing (it goes the wrong way); the union argument is the right one.
Alternatively, use
$|\mathbb{Q}| < |\mathbb{R}|$ together with the fact that removing a countable set from an
uncountable one leaves an uncountable set, which is exactly what the union argument proves.

**30.** *Strategy: transport subsets along the given bijection. The image map $S \mapsto f(S)$ is the natural
candidate; both inverse properties follow from $f$ being bijective.*

Let $f : A \to B$ be a bijection (it exists because $|A| = |B|$). Define

$$F : \mathcal{P}(A) \to \mathcal{P}(B), \qquad F(S) = \{\,f(s) : s \in S\,\}.$$

*Well-defined:* $F(S) \subseteq B$ for $S \subseteq A$, so $F(S) \in \mathcal{P}(B)$.

*Injective:* suppose $F(S) = F(T)$. Applying $f^{-1}$ to both sides gives
$f^{-1}(F(S)) = f^{-1}(F(T))$. For any subset $U \subseteq A$ we have
$f^{-1}(F(U)) = \{a \in A : f(a) \in f(U)\} = U$, because $f$ is injective. Hence $S = T$.

*Surjective:* let $T \in \mathcal{P}(B)$ and put $S = f^{-1}(T) \subseteq A$. Since $f$ is
surjective, $f(S) = T$. Hence $F(S) = T$.

Therefore $F$ is a bijection and $|\mathcal{P}(A)| = |\mathcal{P}(B)|$. $\square$

*Remark:* the same argument shows that equinumerous sets have equinumerous power sets, function
spaces, and products. It is the standard way to transfer cardinality statements across a bijection.

## Challenge

**31.** *Strategy: encode a finite subset of $\mathbb{N}$ as a binary numeral with ones exactly at the
elements of the subset. Uniqueness of binary representation makes the encoding injective, so the set
of finite subsets injects into $\mathbb{N}$.*

(a) For a finite set $S \subseteq \mathbb{N}$ define

$$c(S) = \sum_{i \in S} 2^{i},$$

with the empty sum equal to $0$. This is a natural number.

*$c$ is injective.* Suppose $S \neq T$ and, without loss of generality, $S \not\subseteq T$. Let $k$ be
the largest element of the symmetric difference $S \triangle T$, and suppose $k \in S$.
Then $c(S) - c(T) = 2^{k} + \sum_{i \in S,\, i<k} 2^i - \sum_{i \in T,\, i<k} 2^i$. The lower-order
terms contribute at least $-2^{k} + 1$ in total (the sum of all powers $2^i$ with $i < k$ is
$2^{k} - 1$), so

$$c(S) - c(T) \ge 2^{k} - (2^{k} - 1) = 1 > 0.$$

Hence $c(S) \neq c(T)$, and $c$ is injective. (Equivalently: the binary expansion of $c(S)$ has a $1$
exactly in the positions belonging to $S$, and binary expansions are unique.)

So $c$ is an injection from the set of finite subsets of $\mathbb{N}$ into $\mathbb{N}$. A set that
injects into $\mathbb{N}$ is countable by Lemma 7.8. $\square$

(b) *Finite binary strings.* Map the string $b_1 b_2 \cdots b_n$ (each $b_j \in \{0,1\}$) to the
number whose binary expansion is $1b_1b_2\cdots b_n$. This is injective (the leading $1$ marks the
length, and binary expansions are unique), so the set of finite binary strings injects into
$\mathbb{N}$ and is countable. It is infinite, so it is countably infinite.

*Infinite binary sequences.* By Example 9.5, the set $\{0,1\}^{\mathbb{N}}$ of infinite binary
sequences is in bijection with $\mathcal{P}(\mathbb{N})$, which is uncountable by Cantor's theorem.
Hence the set of infinite binary sequences is uncountable.

*Remark:* the contrast is sharp. Every individual finite string is describable by finitely many
bits, and all such descriptions can be listed; the infinite sequences form a strictly larger
totality. The same distinction underlies the difference between the computable and the non-computable
real numbers.

**32.** *Strategy: $(0,1]$ and $(0,1)$ differ by the single point $1$ — but $1$ has nowhere to go, so a
bijection must "make room" by shifting an entire countable sequence. Use the sequence
$1, \frac12, \frac13, \dots$ as a queue and push every term one step along it.*

**(a) A bijection $f : (0,1] \to (0,1)$.** Let $Q = \{\frac1n : n \ge 1\} \subseteq (0,1]$, and define

$$f(x) = \begin{cases} \dfrac{1}{n+1} & \text{if } x = \dfrac1n \in Q, \\[2mm] x & \text{if } x \in (0,1] \setminus Q. \end{cases}$$

*$f$ maps into $(0,1)$:* if $x = \frac1n$ then $f(x) = \frac{1}{n+1} \in (0,1)$; if $x \notin Q$ then
$x \neq 1$ (because $1 = \frac11 \in Q$), so $x \in (0,1)$ and $f(x) = x \in (0,1)$.

*Injective:* on $Q$ the map $\frac1n \mapsto \frac{1}{n+1}$ is injective; on $(0,1] \setminus Q$ it is
the identity, hence injective; and the two images are disjoint. The image of $Q$ is
$\{\frac{1}{n+1} : n \ge 1\} = \{\frac12, \frac13, \dots\}$, which is contained in $Q$ and disjoint
from $(0,1] \setminus Q$. So $f$ is injective.

*Surjective:* let $y \in (0,1)$. If $y = \frac{1}{n+1}$ for some $n \ge 1$, then
$y = f(\frac1n)$. Otherwise $y$ is not of the form $\frac1m$ with $m \ge 2$; since $y \in (0,1)$, $y$
is also not of the form $\frac11 = 1$. Hence $y \notin Q$, and $f(y) = y$. So every $y \in (0,1)$ is
attained.

Therefore $f$ is a bijection. $\square$

**(b) A bijection $g : [0,1] \to (0,1)$.** Now two points, $0$ and $1$, need to be absorbed, so use a
longer queue. Let $Q' = \{0\} \cup \{\frac1n : n \ge 1\}$ and define

$$g(x) = \begin{cases} \dfrac12 & \text{if } x = 0, \\[2mm] \dfrac{1}{n+2} & \text{if } x = \dfrac1n,\ n \ge 1, \\[2mm] x & \text{if } x \in [0,1] \setminus Q'. \end{cases}$$

*$g$ maps into $(0,1)$:* the images of $0$ and of the points $\frac1n$ form the sequence
$\frac12, \frac13, \frac14, \dots$, all in $(0,1)$; a point $x \notin Q'$ is neither $0$ nor $1$
(as $1 = \frac11 \in Q'$), so $x \in (0,1)$ and $g(x) = x$.

*Injective:* the queue map sends $0 \mapsto \frac12$ and $\frac1n \mapsto \frac{1}{n+2}$; these
values are $\frac12, \frac13, \frac14, \dots$ and are all distinct. The fixed points are distinct from
each other, and the set $\{\frac1n : n \ge 2\} \cup \{\frac12\}$ is contained in $Q'$, hence disjoint
from the fixed-point set. So $g$ is injective.

*Surjective:* let $y \in (0,1)$. If $y = \frac12$, then $g(0) = y$. If $y = \frac{1}{n+2}$ for some
$n \ge 1$, then $g(\frac1n) = y$. Otherwise $y$ is not of the form $\frac1m$ with $m \ge 2$ and
$y \neq \frac12$; since $y \in (0,1)$, $y \neq 1 = \frac11$ as well, so $y \notin Q'$ and
$g(y) = y$. So $g$ is surjective.

Therefore $g$ is a bijection and $|[0,1]| = |(0,1)|$. $\square$

*Common pitfall:* "define $f(x) = x/2$" is injective but not surjective onto $(0,1)$, and
"$f(1) = \frac12$, $f(\frac12) = \frac14$, …" leaves infinitely many points without preimages. The
queue must be shifted by exactly one position along a set that is closed under the shift in the right
direction; that is what makes the definition total and surjective.

**33.** *Strategy: use Cantor–Schröder–Bernstein. For the injection from $\mathcal{P}(\mathbb{N})$ to
$\mathbb{R}$ use base-3 numerals with digits $0,1$ — no digit $2$ means no ambiguity. For the
injection from $\mathbb{R}$ to $\mathcal{P}(\mathbb{N})$ use Dedekind cuts and the countability of
$\mathbb{Q}$.*

**Injection $\mathcal{P}(\mathbb{N}) \to \mathbb{R}$.** For $S \subseteq \mathbb{N}$ define

$$x_S = \sum_{k \in S} 3^{-(k+1)},$$

the real number whose base-3 expansion is $0.d_0d_1d_2\cdots$ with $d_k = 1$ for $k \in S$ and
$d_k = 0$ otherwise. To see that $S \mapsto x_S$ is injective, let $S \neq T$ and let $k$ be the least
index in the symmetric difference, say $k \in S$. Then

$$x_S - x_T \ge 3^{-(k+1)} - \sum_{j > k} 3^{-(j+1)}
= 3^{-(k+1)} - \frac{3^{-(k+2)}}{1 - \frac13}
= 3^{-(k+1)} - \frac{3^{-(k+1)}}{2} > 0.$$

So distinct subsets give distinct reals. (The point of base $3$ with digits $0,1$: the ambiguous
binary case $0.0111\cdots = 0.1000\cdots$ cannot occur, because a digit $2$ would be needed for the
carry.)

**Injection $\mathbb{R} \to \mathcal{P}(\mathbb{N})$.** For $r \in \mathbb{R}$ define

$$C(r) = \{\,q \in \mathbb{Q} : q < r\,\} \subseteq \mathbb{Q}.$$

If $r < s$, density of $\mathbb{Q}$ gives a rational $q$ with $r < q < s$; then $q \in C(s)$ but
$q \notin C(r)$, so $C(r) \neq C(s)$. Hence $C : \mathbb{R} \to \mathcal{P}(\mathbb{Q})$ is
injective. Since $\mathbb{Q}$ is countably infinite, fix a bijection $h : \mathbb{N} \to \mathbb{Q}$;
the induced map $\mathcal{P}(\mathbb{N}) \to \mathcal{P}(\mathbb{Q})$, $S \mapsto \{h(n) : n \in S\}$,
is a bijection (Exercise 30). Composing its inverse with $C$ gives an injection
$\mathbb{R} \to \mathcal{P}(\mathbb{N})$.

**Conclusion.** We have injections in both directions:

$$|\mathcal{P}(\mathbb{N})| \le |\mathbb{R}| \quad \text{and} \quad |\mathbb{R}| \le |\mathcal{P}(\mathbb{N})|.$$

By the Cantor–Schröder–Bernstein theorem (Theorem 7.6), $|\mathcal{P}(\mathbb{N})| = |\mathbb{R}|$.
$\square$

*Remark:* combining this with Cantor's theorem gives $|\mathbb{N}| < |\mathbb{R}|$, a second proof
that the reals are uncountable, independent of the decimal diagonal argument.

**34.** *Strategy: apply Foundation to the singleton $\{x\}$. Its only element is $x$, so Foundation must
produce $x$ itself, and then the disjointness condition contradicts $x \in x$.*

Let $x$ be any set and suppose, for contradiction, that $x \in x$. Consider the set $S = \{x\}$,
which is nonempty. By the Axiom of Foundation there exists $y \in S$ with $y \cap S = \varnothing$.
Since $S$ has the single element $x$, we must have $y = x$. Hence $x \cap \{x\} = \varnothing$.

But $x \in x$ by hypothesis and $x \in \{x\}$ by definition of the singleton, so
$x \in x \cap \{x\}$. This contradicts $x \cap \{x\} = \varnothing$. Therefore $x \notin x$. $\square$

**Consequence for Russell's paradox.** In ZFC the property $x \notin x$ holds for *every* set $x$.
Hence, for any set $X$, the set $R_X = \{x \in X : x \notin x\}$ is simply $X$ itself. Russell's
paradoxical collection $\{x : x \notin x\}$ would therefore have to be the collection of all sets,
which is not a set (Corollary 7.19, and Exercise 27). The paradox is thus converted into the
statement "there is no universal set", and no contradiction remains: the argument of §7.13 cannot be
run because its comprehension is not licensed by Separation.
