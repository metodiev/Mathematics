# Proof Techniques — Solutions

> [Proof Techniques](README.md) · Solutions to the 34 problems in [exercises.md](exercises.md)

Each solution states the strategy, then carries out every significant step. Proof problems receive
complete proofs. Where a problem is designed to expose an error, the faulty step is identified
precisely.

## Beginner

**1.** *Strategy: make the quantifier explicit, then put the statement into the form "if [hypothesis] then
[conclusion]". Statements about "every" object need a quantifier over that object's type.*

(a) **For all integers $n$: if $6 \mid n$, then $3 \mid n$.**
Hypothesis: $6 \mid n$. Conclusion: $3 \mid n$.

(b) "Every prime greater than $2$ is odd" means: **for all integers $n$, if $n$ is prime and $n > 2$,
then $n$ is odd.** Hypothesis: $n$ is prime and $n > 2$. Conclusion: $n$ is odd.

(c) "The sum of two rational numbers is rational" means: **for all real numbers $x$ and $y$, if $x$
and $y$ are rational, then $x + y$ is rational.** Hypothesis: $x \in \mathbb{Q}$ and
$y \in \mathbb{Q}$. Conclusion: $x + y \in \mathbb{Q}$.

*Remark:* the quantifier is part of the statement, not decoration. Part (b) is not a statement about
one odd integer, and part (c) is not a statement about two particular rationals. Dropping the
quantifier changes what must be proved.

**2.** *Strategy: name $P$ and $Q$, then apply Definition 5.4 mechanically. Only the contrapositive is
equivalent to the original; check the truth table of §8.1 if in doubt.*

(a) $P$: it rains. $Q$: the ground is wet.

* **Converse:** if the ground is wet, then it rained ($Q \Rightarrow P$).
* **Contrapositive:** if the ground is not wet, then it did not rain ($\neg Q \Rightarrow \neg P$).
* **Negation:** it rains and the ground is not wet ($P \wedge \neg Q$).

Equivalent to the original: **the contrapositive**.

(b) $P$: the number is divisible by $9$. $Q$: the number is divisible by $3$.

* **Converse:** if the number is divisible by $3$, then it is divisible by $9$.
* **Contrapositive:** if the number is not divisible by $3$, then it is not divisible by $9$.
* **Negation:** the number is divisible by $9$ and not divisible by $3$.

Equivalent to the original: **the contrapositive**.

*Remark:* in (b) the converse is false ($6$ is divisible by $3$ but not by $9$), which shows that
converse and original are genuinely different statements. The original is true: if $9 \mid n$ then
$n = 9k = 3(3k)$, so $3 \mid n$. Its contrapositive is the same argument read backwards, and it is
also the form in which the statement is usually applied.

**3.** *Strategy: unpack "odd" by definition in both numbers, add, and repackage the result as twice an
integer.*

Let $m$ and $n$ be odd integers. By definition there exist integers $a$ and $b$ with $m = 2a + 1$ and
$n = 2b + 1$. Then

$$m + n = (2a + 1) + (2b + 1) = 2a + 2b + 2 = 2(a + b + 1).$$

Since $a + b + 1$ is an integer, $m + n$ is even. $\square$

**4.** *Strategy: write both divisibilities as equations and combine the equations; the conclusion is again
an equation of the same shape.*

Assume $a \mid b$ and $a \mid c$. By definition there exist integers $k$ and $\ell$ with $b = ak$ and
$c = a\ell$. Then

$$b + c = ak + a\ell = a(k + \ell), \qquad b - c = ak - a\ell = a(k - \ell).$$

Since $k + \ell$ and $k - \ell$ are integers, $a \mid (b+c)$ and $a \mid (b-c)$. $\square$

*Edge case:* if $a = 0$, then $0 \mid b$ forces $b = 0$ and $0 \mid c$ forces $c = 0$, so
$b \pm c = 0 = 0 \cdot 0$, and the conclusion still holds. The argument above covers this case too,
with $k = \ell = 0$.

**5.** *Strategy: write the two consecutive integers as $n$ and $n+1$, then split into the two cases "n even"
and "n odd" — one of the factors is always the even one.*

Let the integers be $n$ and $n+1$. Their product is $n(n+1)$. Every integer is even or odd, so there
are two cases.

*Case 1: $n$ is even.* Write $n = 2k$. Then $n(n+1) = 2k(n+1) = 2\bigl(k(n+1)\bigr)$, which is even.

*Case 2: $n$ is odd.* Write $n = 2k+1$; then $n+1 = 2k+2 = 2(k+1)$, so
$n(n+1) = n \cdot 2(k+1) = 2\bigl(n(k+1)\bigr)$, which is even.

In both cases the product is even. $\square$

*Alternative:* among two consecutive integers exactly one is even, so the product contains a factor
$2$; the case analysis above is the rigorous form of that sentence.

**6.** *Strategy: move the negation inward one quantifier or connective at a time, using §8.2. For (c),
remember that negating an implication gives "hypothesis and not conclusion".*

(a) **Negation:** $\exists x \in \mathbb{R},\ x^2 < 0$. The original is **true**: squares of real
numbers are non-negative, so no such $x$ exists.

(b) **Negation:** $\forall n \in \mathbb{N},\ n^2 \neq 2$. The original is **false**: $n = 0$ and
$n = 1$ give $n^2 = 0, 1$, and for $n \ge 2$ we have $n^2 \ge 4$; no natural number squares to $2$.
Hence the negation is true.

(c) **Negation:**
$$\exists \varepsilon > 0\ \forall \delta > 0\ \exists x\ \bigl(|x| < \delta \wedge |f(x)| \ge \varepsilon\bigr).$$
The truth **depends on $f$**. For $f(x) = 0$ for all $x$, the original is true: given
$\varepsilon > 0$, any $\delta$ (say $\delta = 1$) works, because $|f(x)| = 0 < \varepsilon$. For
$f(x) = 1$ for all $x$, the original is false: take $\varepsilon = \tfrac12$; for every $\delta > 0$
and every $x$ with $|x| < \delta$ (for instance $x = 0$) we have $|f(x)| = 1 \ge \tfrac12$. So the
statement is a genuine property of $f$ — in fact it is the definition of continuity of $f$ at $0$.

**7.** *Strategy: distinguish "is there an object?" (an example suffices) from "do all objects have the
property?" (an example never suffices, a counterexample refutes).*

(a) **A single example settles it.** The statement is existential; $2$ is prime and even, so it is
true. (Indeed $2$ is the only even prime, but that is not needed for the truth of the statement.)

(b) **A single counterexample settles it.** $2$ is prime and not odd, so the universal statement is
false.

(c) **Neither in practice.** This is Goldbach's conjecture. A single example confirms one even number
but cannot establish all of them; a single counterexample would refute the conjecture, but none is
known. Settling it requires a general proof (or a counterexample, which would also settle it).
It is a *conjecture*, not a theorem, and may not be used as one.

(d) **A single counterexample settles it.** $x = 0$ gives $x^2 = 0$, and $0 > 0$ is false. So the
statement is false. (Checking many positive $x$ would only show that the statement often holds.)

*Moral:* examples confirm existentials and refute universals; they do nothing for universals in the
positive direction.

**8.** *Strategy: test boundary values — $0$, $1$, negatives, the smallest primes — and verify the
counterexample numerically.*

(a) $n = 2$: $2$ is prime, but $2$ is even, so it is not odd. Hence the statement fails.

(b) $x = -1$: then $x^2 = 1 > -1 = x$, so the hypothesis holds; but $-1 > 1$ is false. Hence the
statement fails. (Note that $x = 0$ is not a counterexample: there $x^2 > x$ is false, so the
hypothesis fails.)

(c) $3$: the only squares of integers not exceeding $3$ are $0$ and $1$, and their possible sums are
$0, 1, 2$. Since $3 \notin \{0,1,2\}$, $3$ is not a sum of two squares. Hence the statement fails.

*Pitfall:* in (b) one must check that the *hypothesis* is satisfied before claiming a counterexample.
A value where the hypothesis fails proves nothing.

**9.** *Strategy: look for small integer solutions by trying $x = -1$ or $y = 1$; then present the witness and
verify it.*

Take $x = -1$ and $y = 2$. Then

$$13(-1) + 7(2) = -13 + 14 = 1.$$

So the required integers exist. $\square$

The proof is **constructive**: it exhibits the specific pair $(-1,2)$, and the verification is a
direct computation. (How one *finds* such a pair is another matter; the extended Euclidean algorithm
produces it systematically.)

**10.** *Strategy: "same parity" is proved by two implications — even gives even, odd gives odd — or, more
efficiently, by one case analysis covering all integers.*

Let $n$ be an integer. Every integer is even or odd.

*Case 1: $n$ is even.* Write $n = 2k$. Then $n^2 = 4k^2 = 2(2k^2)$, which is even — the same parity
as $n$.

*Case 2: $n$ is odd.* Write $n = 2k+1$. Then
$n^2 = 4k^2 + 4k + 1 = 2(2k^2 + 2k) + 1$, which is odd — again the same parity as $n$.

The cases are exhaustive, so $n^2$ has the same parity as $n$ for every integer $n$. $\square$

**11.** *Strategy: check every algebraic step and every division. A division is legal only when the divisor is
known to be nonzero.*

The algebra up to $(a-b)(a+b) = b(a-b)$ is correct: starting from $a = b$, we get $a^2 = ab$, then
subtract $b^2$ from both sides. The errors are the two divisions.

1. **Dividing by $a - b$.** Since $a = b$, we have $a - b = 0$. Division by zero is not defined, and
   the step from $(a-b)(a+b) = b(a-b)$ to $a+b = b$ is invalid. This is the fatal error: the equation
   before the division is true (both sides are $0$), and the equation after it is not implied.
2. **Dividing by $b$.** After the invalid step one has $a + b = b$, i.e. $a = 0$; with $a = b$ this
   gives $b = 0$, so the later division by $b$ is also division by zero.

What the argument actually proves is: if $a = b$, then $(a-b)(a+b) = b(a-b)$ holds trivially, and the
only conclusion legitimately available is $0 = 0$. The statement $1 = 2$ is not derived. $\square$

*Moral:* cancelling a factor requires knowing it is nonzero. In a proof, that knowledge must come from
a hypothesis, not from hope.

## Intermediate

**12.** *Strategy: copy the structure of the $\sqrt2$ proof (Theorem 7.8). The role played by "2 is prime" is
now played by "3 is prime", so we need the lemma: if $3 \mid m^2$ then $3 \mid m$.*

**Lemma.** For every integer $m$, if $3 \mid m^2$ then $3 \mid m$.

*Proof of the lemma.* We prove the contrapositive: if $3 \nmid m$ then $3 \nmid m^2$. If $3 \nmid m$,
then $m \equiv 1$ or $m \equiv 2 \pmod 3$. In the first case $m^2 \equiv 1 \pmod 3$; in the second
$m^2 \equiv 4 \equiv 1 \pmod 3$. In either case $m^2 \equiv 1 \not\equiv 0 \pmod 3$, i.e.
$3 \nmid m^2$. $\square$

**Theorem.** $\sqrt3$ is irrational.

*Proof.* Suppose, for contradiction, that $\sqrt3$ is rational. Write $\sqrt3 = p/q$ with
$p, q \in \mathbb{Z}$, $q \neq 0$, and $\gcd(p,q) = 1$ (lowest terms). Squaring gives

$$3 = \frac{p^2}{q^2}, \qquad \text{so} \qquad p^2 = 3q^2. \qquad (\ast)$$

Thus $3 \mid p^2$, and by the lemma $3 \mid p$. Write $p = 3m$. Substituting into $(\ast)$,

$$9m^2 = 3q^2, \qquad q^2 = 3m^2.$$

So $3 \mid q^2$, and by the lemma again $3 \mid q$. Hence $3$ divides both $p$ and $q$, contradicting
$\gcd(p,q) = 1$. Therefore $\sqrt3$ is irrational. $\square$

*Remark:* the lemma is false with $3$ replaced by a composite number. For instance $4 \mid 6^2 = 36$
but $4 \nmid 6$. The primality of $3$ is exactly what makes the argument work.

**13.** *Strategy: the contrapositive of "$5n + 3$ odd $\Rightarrow$ $n$ even" is "$n$ odd $\Rightarrow$
$5n + 3$ even", which is a direct computation.*

We prove the contrapositive: for every integer $n$, if $n$ is odd then $5n + 3$ is even.

Let $n = 2k + 1$ with $k \in \mathbb{Z}$. Then

$$5n + 3 = 5(2k + 1) + 3 = 10k + 5 + 3 = 10k + 8 = 2(5k + 4).$$

Since $5k + 4$ is an integer, $5n + 3$ is even. This proves the contrapositive, hence the original
implication. $\square$

*Remark:* since the contrapositive is equivalent to the original, the proof is complete. Note the
hypothesis of the original statement is "$5n+3$ is odd", not "$n$ is odd"; proving the implication in
the other direction would establish only the converse (which happens to be true here, but is not what
was asked).

**14.** *Strategy: the conclusion is a disjunction, and the negation of "$x > 1$ or $y > 1$" is
"$x \le 1$ and $y \le 1$", which is easy to combine. Use the contrapositive.*

We prove the contrapositive: if $x \le 1$ and $y \le 1$, then $x + y \le 2$.

Assume $x \le 1$ and $y \le 1$. Adding the inequalities (addition preserves order) gives
$x + y \le 1 + 1 = 2$, as required.

Since the contrapositive is equivalent to the original statement, for all real $x,y$: if $x + y > 2$,
then $x > 1$ or $y > 1$. $\square$

*Alternative (contradiction):* suppose $x + y > 2$ but $x \le 1$ and $y \le 1$; then $x + y \le 2$,
contradiction. The two proofs are the same argument viewed differently.

**15.** *Strategy: division by $3$ gives three possible remainders, so the cases are $n = 3k$, $n = 3k+1$,
$n = 3k+2$. These are exhaustive and mutually exclusive by the division algorithm.*

Let $n$ be an integer. By the division algorithm, $n = 3k + r$ for some $k \in \mathbb{Z}$ and
$r \in \{0,1,2\}$.

*Case $r = 0$:* $n = 3k$, so $n^2 = 9k^2 = 3(3k^2)$, hence $n^2 \equiv 0 \pmod 3$.

*Case $r = 1$:* $n = 3k+1$, so
$n^2 = 9k^2 + 6k + 1 = 3(3k^2 + 2k) + 1$, hence $n^2 \equiv 1 \pmod 3$.

*Case $r = 2$:* $n = 3k+2$, so
$n^2 = 9k^2 + 12k + 4 = 3(3k^2 + 4k + 1) + 1$, hence $n^2 \equiv 1 \pmod 3$.

In every case $n^2 \equiv 0$ or $1 \pmod 3$. $\square$

*Remark:* since $n^2 \equiv 1 \pmod 3$ in the case $r = 2$ as well, the residues $0, 1$ are the only
possibilities; in particular $n^2 \equiv 2 \pmod 3$ has no solution. That observation is the key to
proving that $3$ has no square root in $\mathbb{Q}$, again.

**16.** *Strategy: existence by exhibiting a solution; uniqueness by assuming a solution exists and deriving it
uniquely. The second equation is convenient for expressing $y$ in terms of $x$.*

**Existence.** Take $x = 1$ and $y = 2$. Then
$x + 2y = 1 + 4 = 5$ and $3x - y = 3 - 2 = 1$. ✓

**Uniqueness.** Let $(x,y)$ be any pair of integers satisfying both equations. From $3x - y = 1$ we get
$y = 3x - 1$. Substituting into $x + 2y = 5$,

$$x + 2(3x - 1) = 5, \qquad x + 6x - 2 = 5, \qquad 7x = 7, \qquad x = 1.$$

Then $y = 3 \cdot 1 - 1 = 2$. So every solution equals $(1,2)$; combined with existence, there is
exactly one solution. $\square$

*Remark:* this is a linear system, so uniqueness could also be argued from the nonzero determinant
$1 \cdot (-1) - 2 \cdot 3 = -7 \neq 0$. The substitution argument is more elementary and equally
complete.

**17.** *Strategy: the forward direction needs Theorem 7.6 (if $n^2$ is even then $n$ is even); the backward
direction is a direct computation.*

**($\Leftarrow$)** Assume $n$ is even: $n = 2k$ with $k \in \mathbb{Z}$. Then
$n^2 = 4k^2 = 4(k^2)$, so $4 \mid n^2$.

**($\Rightarrow$)** Assume $4 \mid n^2$. Then $n^2 = 4k$ for some $k$, so $n^2$ is even (it is
$2 \cdot 2k$). By Theorem 7.6, $n$ is even.

Both directions hold, so $4 \mid n^2 \Longleftrightarrow n$ is even. $\square$

*Pitfall:* the forward direction is *not* immediate from "$4 \mid n^2$" by taking square roots — that
would assume what is to be proved. The route through "$n^2$ even" and Theorem 7.6 is the valid one.

**18.** *Strategy: one direction is immediate; for the other, use that $A \cap B \subseteq A \subseteq A \cup B$,
so equality of the two extremes forces everything in between to coincide.*

**($\Leftarrow$)** Assume $A = B$. Then $A \cap B = A \cap A = A$ and $A \cup B = A \cup A = A$, so
$A \cap B = A \cup B$.

**($\Rightarrow$)** Assume $A \cap B = A \cup B$. We prove $A \subseteq B$. Let $x \in A$. Then
$x \in A \cup B$, so $x \in A \cap B$ by the assumption, and therefore $x \in B$. Hence
$A \subseteq B$. The same argument with $A$ and $B$ exchanged gives $B \subseteq A$. Therefore
$A = B$. $\square$

*Remark:* the chain $A \cap B \subseteq A \subseteq A \cup B$ always holds (Exercise 7 of
[Set Theory](../03-set-theory/README.md)); the hypothesis makes the two ends equal, so all three sets
coincide.

**19.** *Strategy: for (a) and (b), pick a familiar irrational and use it twice with opposite signs or with
itself; verify irrationality by contradiction from Theorem 7.8. For (c), analyse what the case
argument of Theorem 7.12 does and does not produce.*

(a) Take $x = \sqrt2$ and $y = -\sqrt2$. Then $x + y = 0$, which is rational.

*Both are irrational.* Theorem 7.8 says $\sqrt2 \notin \mathbb{Q}$. If $-\sqrt2$ were rational, say
$-\sqrt2 = q \in \mathbb{Q}$, then $\sqrt2 = -q \in \mathbb{Q}$ (the negative of a rational is
rational), contradicting Theorem 7.8. So $-\sqrt2$ is irrational too.

(b) Take $x = y = \sqrt2$. Then $xy = \sqrt2 \cdot \sqrt2 = 2$, which is rational, and both factors are
irrational by Theorem 7.8.

(c) Theorem 7.12 splits on the statement "$\alpha = \sqrt2^{\sqrt2}$ is rational". In the first case it
uses the pair $(\sqrt2, \sqrt2)$; in the second, the pair $(\sqrt2^{\sqrt2}, \sqrt2)$. It proves that
one of these two pairs has the required property, without determining which.

The proof is **non-constructive** because it does not identify a witness: no specific pair of
irrationals with rational power is exhibited, and the argument gives no procedure for deciding which
case applies. It is nevertheless a **complete** proof because the law of excluded middle guarantees
that one of the two cases holds, and in *each* case the existential statement is verified. A
non-constructive proof establishes truth; it merely withholds a witness. In ordinary mathematics that
is enough.

**20.** *Strategy: $n! + 1$ is not divisible by any of $2, 3, \dots, n$; any prime divisor of it must therefore
be larger than $n$. Use Lemma 7.10 to get a prime divisor.*

Let $n$ be a positive integer and put $N = n! + 1$. Then $N > 1$, so by Lemma 7.10 (every integer
greater than $1$ has a prime divisor) there is a prime $p$ with $p \mid N$.

We show $p > n$. Suppose instead that $p \le n$. Then $p$ is one of the factors of
$n! = 1 \cdot 2 \cdots n$, so $p \mid n!$. Since also $p \mid N = n! + 1$, it follows that
$p \mid \bigl(N - n!\bigr) = 1$, which is impossible for a prime $p \ge 2$. Hence $p > n$.

Finally $p \le N$ because $p$ divides the positive integer $N$, so $p \le n! + 1$. Therefore
$n < p \le n! + 1$, as required. $\square$

*Example:* for $n = 4$, $n! + 1 = 25$ and the prime $p = 5$ satisfies $4 < 5 \le 25$. Note that
$n! + 1$ itself need not be prime, which is why the lemma is applied to it rather than asserted of it.

**21.** *Strategy: one direction is immediate; for the other, a positive integer that divides every integer
divides $1$, which forces it to be $1$.*

First, $1$ divides every integer: for any $n \in \mathbb{Z}$ we have $n = 1 \cdot n$.

Conversely, let $a$ be a positive integer that divides every integer. In particular $a \mid 1$, so
$1 = ak$ for some $k \in \mathbb{Z}$. Since $a \ge 1$, if $k \le 0$ then $ak \le 0 < 1$, impossible;
hence $k \ge 1$. Then $1 = ak \ge a \ge 1$, so all three quantities are equal and $a = 1$. $\square$

## Advanced

**22.** *Strategy: use unique factorisation to count how many times $p$ appears in $a$ and in $a^2$. The
hypothesis $p \mid a^2$ forces that count to be positive.*

By the fundamental theorem of arithmetic, write

$$a = p^{k} m$$

where $k \ge 0$ is an integer and $p \nmid m$. (If $p \nmid a$ then $k = 0$ and $m = a$; if $p \mid a$,
$k$ is the exponent of $p$ in the factorisation of $a$.) Then

$$a^2 = p^{2k} m^2.$$

Since $p \nmid m$, unique factorisation gives $p \nmid m^2$: the exponent of $p$ in $m^2$ is twice its
exponent in $m$, which is $0$. Hence the exponent of $p$ in $a^2$ is exactly $2k$.

Now assume $p \mid a^2$. Then the exponent of $p$ in $a^2$ is at least $1$, i.e. $2k \ge 1$. Since $k$
is an integer, $k \ge 1$, which means exactly that $p \mid a$. $\square$

*Remark:* primality is essential. With $p = 4$ the analogue fails: $4 \mid 6^2 = 36$ but $4 \nmid 6$.

**23.** *Strategy: square the assumed rational sum. If $s = \sqrt2 + \sqrt3$ were rational, then $\sqrt6$ would
be rational, which it is not. So the proof reduces to the irrationality of $\sqrt6$.*

**Lemma.** $\sqrt6$ is irrational.

*Proof.* Suppose $\sqrt6 = p/q$ with $p, q \in \mathbb{Z}$, $q \neq 0$, $\gcd(p,q) = 1$. Then
$p^2 = 6q^2 = 2(3q^2)$, so $p^2$ is even; by Theorem 7.6, $p$ is even. Write $p = 2m$. Then
$4m^2 = 6q^2$, i.e. $2m^2 = 3q^2$. The right side $3q^2$ equals the even number $2m^2$, so $3q^2$ is
even; since $3$ is odd, $q^2$ is even, and by Theorem 7.6 again $q$ is even. Thus $2 \mid p$ and
$2 \mid q$, contradicting $\gcd(p,q) = 1$. Hence $\sqrt6 \notin \mathbb{Q}$. $\square$

**Theorem.** $\sqrt2 + \sqrt3$ is irrational.

*Proof.* Suppose, for contradiction, that $s = \sqrt2 + \sqrt3$ is rational. Squaring,

$$s^2 = (\sqrt2)^2 + 2\sqrt2\,\sqrt3 + (\sqrt3)^2 = 2 + 2\sqrt6 + 3 = 5 + 2\sqrt6.$$

Solving for $\sqrt6$,

$$\sqrt6 = \frac{s^2 - 5}{2}.$$

The right side is a quotient of rational numbers with nonzero denominator $2$, hence rational; so
$\sqrt6$ would be rational. This contradicts the lemma. Therefore $s$ is irrational. $\square$

*Results used:* the irrationality of $\sqrt2$ (Theorem 7.8), Theorem 7.6 ($n^2$ even implies $n$ even),
and the closure of $\mathbb{Q}$ under arithmetic operations.

**24.** *Strategy: evaluate at $n = 41$ (or $n = 40$) to get a square; then use a congruence to manufacture
infinitely many failures at once.*

Let $f(n) = n^2 + n + 41$.

**One failure.** At $n = 40$,
$$f(40) = 1600 + 40 + 41 = 1681 = 41^2,$$
which is composite. So the statement fails.

**Infinitely many failures.** Let $n = 41k$ with $k \ge 1$. Then

$$f(41k) = 41^2 k^2 + 41k + 41 = 41\bigl(41k^2 + k + 1\bigr).$$

Both factors are integers greater than $1$: the first is $41$, and $41k^2 + k + 1 \ge 41 + 1 + 1 = 43$.
Hence $f(41k)$ is composite for every $k \ge 1$, so the statement fails for infinitely many $n$.
$\square$

*What is really going on:* modulo $41$, $f(n) \equiv n^2 + n = n(n+1)$. So $f(n) \equiv 0 \pmod{41}$
whenever $n \equiv 0$ or $n \equiv -1 \pmod{41}$, which gives infinitely many $n$ whose value is
divisible by $41$. The same idea shows $n^2 - n + 41$ fails at $n = 41$ (discussed in the tutorial,
Example 7.18). A finite check up to $n = 39$ — where Euler's polynomial is indeed prime — would never
reveal this.

**25.** *Strategy: $(n+1)!$ is divisible by every integer from $2$ to $n+1$. Adding $k$ to it produces a number
divisible by $k$, and bigger than $k$, hence composite.*

Let $n \ge 2$ and consider the $n$ consecutive integers

$$(n+1)! + 2,\quad (n+1)! + 3,\quad \dots,\quad (n+1)! + (n+1).$$

For each $k \in \{2, 3, \dots, n+1\}$, the number $k$ divides $(n+1)!$ (it is one of the factors of the
factorial), and $k$ divides $k$ itself. Hence

$$k \mid \bigl((n+1)! + k\bigr).$$

Moreover $(n+1)! + k > k$, because $(n+1)! \ge 3! = 6 > 0$. So $(n+1)! + k$ has a divisor $k$ with
$1 < k < (n+1)! + k$, which means it is composite. Thus all $n$ numbers listed are composite. $\square$

*Example:* for $n = 3$, the numbers $4! + 2 = 26$, $4! + 3 = 27$, $4! + 4 = 28$ are three consecutive
composites.

*Remark:* the numbers produced are enormous, but the argument is constructive — it exhibits the block
explicitly.

**26.** *Strategy: factor the difference of squares. The two factors are integers with constrained size or
parity, and those constraints are contradictory.*

(a) Suppose $x, y$ are positive integers with $x^2 - y^2 = 1$. Factoring,

$$(x - y)(x + y) = 1.$$

Both factors are integers. Since $y \ge 1$, we have $x + y \ge x + 1 \ge 2$, so the second factor is at
least $2$. A product of integers equal to $1$ requires both factors to be $1$ or both $-1$; since
$x + y \ge 2$, neither is possible. Contradiction. Hence there is no solution in positive integers.
$\square$

(b) Suppose integers $x, y$ satisfy $x^2 - y^2 = 2$, i.e. $(x-y)(x+y) = 2$. Add the two factors:

$$(x + y) + (x - y) = 2x,$$

which is even. Hence $x + y$ and $x - y$ have the same parity: either both are even, or both are odd.
If both are odd, their product is odd, but $2$ is even. If both are even, their product is divisible by
$4$, but $2$ is not. Neither alternative is possible, so there is no integer solution. $\square$

*Remark:* the same parity argument shows $x^2 - y^2 = 2m$ has no solution when $m$ is odd, because the
two factors of $x^2 - y^2$ always have the same parity.

**27.** *Strategy: prove both statements by contradiction, isolating the irrational as a difference or a
quotient of rationals. The closure of $\mathbb{Q}$ under $+$, $-$, $\times$ and division by a nonzero
rational does the rest.*

(a) Let $q \in \mathbb{Q}$ and let $r$ be irrational. Suppose, for contradiction, that $q + r$ is
rational; call it $s$. Then

$$r = s - q.$$

Now $s$ and $q$ are rational, and the difference of two rationals is rational: if $s = a/b$ and
$q = c/d$ with $b, d \neq 0$, then $s - q = (ad - bc)/(bd)$ with $bd \neq 0$. Hence $r$ would be
rational, contradicting the hypothesis. Therefore $q + r$ is irrational. $\square$

(b) Let $q \in \mathbb{Q}$ with $q \neq 0$ and let $r$ be irrational. Suppose $qr$ is rational; call it
$s$. Since $q \neq 0$,

$$r = \frac{s}{q}.$$

A quotient of two rationals with nonzero denominator is rational (if $s = a/b$, $q = c/d$ with
$b, c, d \neq 0$, then $s/q = ad/(bc)$ with $bc \neq 0$). Hence $r \in \mathbb{Q}$, contradiction.
Therefore $qr$ is irrational. $\square$

*Why the hypothesis $q \neq 0$ is needed:* $0 \cdot \sqrt2 = 0$ is rational. The statement with
"nonzero" removed is false.

**28.** *Strategy: bring everything to one side and factor. The positivity hypothesis rules out the factor
$x + y = 0$.*

Assume $x > 0$, $y > 0$ and $x^2 = y^2$. Then

$$x^2 - y^2 = 0, \qquad (x - y)(x + y) = 0.$$

A product of real numbers is zero only if one of the factors is zero (zero-product property). So
$x - y = 0$ or $x + y = 0$.

But $x + y > 0$, because $x > 0$ and $y > 0$ and the sum of positive reals is positive. Hence
$x + y \neq 0$, so the second alternative fails. Therefore $x - y = 0$, i.e. $x = y$. $\square$

*Remark:* without the positivity hypothesis the conclusion is false: $x = 1$ and $y = -1$ satisfy
$x^2 = y^2$ but $x \neq y$.

**29.** *Strategy: suppose $\log_2 3$ is rational, exponentiate, and compare the parity of the two sides.*

First note that $\log_2 3 > 0$: since $2^0 = 1 < 3$ and $x \mapsto 2^x$ is strictly increasing,
$\log_2 3 > \log_2 1 = 0$.

Suppose, for contradiction, that $\log_2 3$ is rational. Then $\log_2 3 = p/q$ for integers $p, q$
with $q > 0$. Because $\log_2 3 > 0$, we have $p > 0$. By definition of the logarithm,

$$2^{p/q} = 3.$$

Raising both sides to the power $q$ (a positive integer) gives

$$2^{p} = 3^{q}.$$

The left side is even: $p \ge 1$, so $2^p$ is divisible by $2$. The right side is odd: $3^q$ is a
product of odd numbers. An even integer cannot equal an odd one, a contradiction. Hence $\log_2 3$ is
irrational. $\square$

*Remark:* the same argument shows $\log_2 n$ is irrational for every integer $n$ that is not a power of
$2$, and more generally that $\log_a b$ is irrational when $a$ and $b$ are integers $> 1$ with no common
power.

**30.** *Strategy: the inequality is equivalent to $(x-1)^2 \ge 0$, which is a square and therefore automatic.
Work backwards to find the proof, then write it forwards.*

Let $x > 0$. For every real $x$,

$$(x - 1)^2 \ge 0,$$

because a square of a real number is non-negative. Expanding,

$$x^2 - 2x + 1 \ge 0, \qquad x^2 + 1 \ge 2x.$$

Dividing both sides by $x > 0$ (division by a positive number preserves the inequality direction),

$$x + \frac{1}{x} \ge 2.$$

This is the required inequality.

**Equality.** The chain of equivalences is reversible, so equality holds exactly when $(x-1)^2 = 0$,
i.e. $x = 1$. Direct check: $1 + 1/1 = 2$. ✓

*Remark:* the hypothesis $x > 0$ is essential both for dividing by $x$ with the inequality preserved
and for the truth of the claim: for $x = -1$, $x + 1/x = -2 < 2$.

## Challenge

**31.** *Strategy: mimic Euclid's proof, but arrange the constructed number to be congruent to $3$ modulo $4$.
The key observation is that a product of primes all congruent to $1$ modulo $4$ is again $1$ modulo $4$,
so a number congruent to $3$ must have a prime factor congruent to $3$.*

**Lemma.** If $a \equiv b \pmod 4$ and $c \equiv d \pmod 4$, then $ac \equiv bd \pmod 4$. In particular,
a product of integers each congruent to $1$ modulo $4$ is congruent to $1$ modulo $4$.

*Proof.* Write $a = b + 4m$ and $c = d + 4n$. Then
$ac = bd + 4(bn + dm + 4mn)$, so $ac \equiv bd \pmod 4$. Iterating the result gives the statement about
products. $\square$

**Theorem.** There are infinitely many primes congruent to $3$ modulo $4$.

*Proof.* Suppose, for contradiction, that there are only finitely many; list them all:
$p_1, \dots, p_n$. The list is nonempty, since $3$ is such a prime. Define

$$N = 4p_1p_2\cdots p_n - 1.$$

Then $N \equiv -1 \equiv 3 \pmod 4$, and $N \ge 4\cdot 3 - 1 = 11 > 1$. By Lemma 7.10, $N$ has a
prime divisor $q$. Since $N$ is odd, $q$ is odd, so $q \equiv 1$ or $3 \pmod 4$.

If every prime divisor of $N$ were congruent to $1$ modulo $4$, then $N$ — being a product of its prime
divisors, with multiplicity — would be congruent to $1$ modulo $4$ by the lemma, contradicting
$N \equiv 3 \pmod 4$. Hence $N$ has a prime divisor $q$ with $q \equiv 3 \pmod 4$.

Because the list $p_1,\dots,p_n$ contains all primes congruent to $3$ modulo $4$, we have $q = p_i$ for
some $i$. Then $p_i \mid N$ and $p_i \mid 4p_1\cdots p_n$, so $p_i$ divides their difference:

$$p_i \mid \bigl(4p_1\cdots p_n - N\bigr) = 1.$$

This is impossible since $p_i \ge 3$. Therefore the list cannot be complete, and there are infinitely
many such primes. $\square$

*Remark:* the trick of forcing the congruence $3 \pmod 4$ is what makes the argument work; the naive
$p_1\cdots p_n + 1$ does not control the residue modulo $4$.

**32.** *Strategy: start from a rational point inside the interval (density of $\mathbb{Q}$) and move towards
the right endpoint by an irrational fraction of the remaining distance. Distinct fractions give
distinct points, and rational plus irrational is irrational.*

Let $a < b$ be real numbers. By the density of $\mathbb{Q}$ in $\mathbb{R}$, there is a rational $q$
with $a < q < b$. Put $d = b - q > 0$ and, for each $n \ge 1$, define

$$x_n = q + \frac{d}{n\sqrt2}.$$

**(i) Each $x_n$ is irrational.** The number $\sqrt2$ is irrational (Theorem 7.8), hence
$1/\sqrt2 = \sqrt2/2$ is irrational (if it were rational, multiplying by $2$ would make $\sqrt2$
rational). Then $1/(n\sqrt2)$ is irrational, because a nonzero rational $n$ times an irrational is
irrational (Exercise 27(b)). Finally $d/(n\sqrt2)$ is a nonzero rational $d/n$ times the irrational
$1/\sqrt2$, so it is irrational, and $x_n$ is the sum of the rational $q$ and an irrational, hence
irrational (Exercise 27(a)).

**(ii) Each $x_n$ lies in $(a,b)$.** Since $n\sqrt2 > 1$ for every $n \ge 1$, we have
$0 < \dfrac{d}{n\sqrt2} < d$. Therefore

$$a < q < x_n < q + d = b.$$

**(iii) The $x_n$ are pairwise distinct.** If $m \neq n$ then the two numbers $\dfrac{d}{m\sqrt2}$ and
$\dfrac{d}{n\sqrt2}$ are different, because $d > 0$, so $x_m \neq x_n$.

Hence the interval $(a,b)$ contains the infinitely many distinct irrational numbers $x_1, x_2, \dots$.
$\square$

*Facts used:* density of $\mathbb{Q}$ in $\mathbb{R}$ (between any two distinct reals there is a
rational), Theorem 7.8, and the closure properties of $\mathbb{Q}$ proved in Exercise 27.

**33.** *Strategy: prove the contrapositive. If $n$ is composite, $n = ab$ with $a, b > 1$, and the algebraic
identity $x^b - 1 = (x-1)(x^{b-1} + \cdots + 1)$ factors $2^n - 1$ nontrivially.*

Let $n \ge 1$ and suppose that $2^n - 1$ is prime. Then $2^n - 1 > 1$, which forces $n \ge 2$ (for
$n = 1$, $2^1 - 1 = 1$ is not prime). We prove that $n$ is prime by contrapositive: if $n$ is
composite, then $2^n - 1$ is composite.

Suppose $n = ab$ with integers $1 < a < n$ and $1 < b < n$. By the identity

$$x^{b} - 1 = (x - 1)\bigl(x^{b-1} + x^{b-2} + \cdots + x + 1\bigr),$$

valid for every real $x$ and every integer $b \ge 1$, substitute $x = 2^a$:

$$2^{n} - 1 = 2^{ab} - 1 = (2^a)^{b} - 1
= (2^a - 1)\bigl(2^{a(b-1)} + 2^{a(b-2)} + \cdots + 2^{a} + 1\bigr).$$

Both factors are integers greater than $1$:

* $2^a - 1 \ge 2^2 - 1 = 3$, since $a \ge 2$;
* the second factor has $b \ge 2$ terms, each a positive integer, so it is at least $2$.

Hence $2^n - 1$ is a product of two integers greater than $1$, i.e. it is composite. This proves the
contrapositive, and therefore the original statement. $\square$

*Example:* $n = 4$ gives $2^4 - 1 = 15 = 3 \cdot 5$, in agreement with the factorisation
$(2^2 - 1)(2^2 + 1) = 3 \cdot 5$.

*Remark:* the converse is false — $n$ prime does not force $2^n - 1$ prime. For instance $n = 11$ is
prime, but $2^{11} - 1 = 2047 = 23 \cdot 89$.

**34.** *Strategy: check the algebra, supply the missing justification for "$k(k+1)$ is even", and then test the
claimed generalisation at the smallest odd square that could fail.*

(a) **The argument is correct, but it has a gap: it asserts without proof that $k(k+1)$ is even.** The
missing justification is one line: $k$ and $k+1$ are consecutive integers, so one of them is even
(Exercise 5), hence their product is even. Once $k(k+1) = 2m$ with $m \in \mathbb{Z}$, the computation

$$n^2 = 4k(k+1) + 1 = 4 \cdot 2m + 1 = 8m + 1$$

is valid and shows $n^2 \equiv 1 \pmod 8$. So the claim is true, and the repaired proof is complete.

(b) **The method does not give the result modulo $16$, and the result is false.** For $n = 3$:
$n^2 = 9$, and $9 \equiv 9 \pmod{16}$, not $1$.

What goes wrong: the argument produces $n^2 = 8m + 1$ where $m = k(k+1)/2$. Whether $8m \equiv 0$ or
$8 \pmod{16}$ depends on the parity of $m$, and $m$ can be odd: for $k = 1$ (that is, $n = 3$),
$m = 1$, giving $n^2 = 9$. There is no reason for $k(k+1)$ to be divisible by $4$: for $k = 1$,
$k(k+1) = 2$, and $4 \nmid 2$. So the single factor of $2$ extracted from $k(k+1)$ is all that is
available, and it yields exactly one factor of $8$ in $n^2 - 1$, not two.

*Moral:* the strength of a proof is exactly what its inequalities and divisibilities deliver. The
mod-$8$ statement is the best possible of its kind; asking for mod $16$ requires a stronger hypothesis
about $k$, which fails for $n = 3$. Working modulo $16$ directly, the odd squares are $1$ or $9$: one
checks $n^2 \equiv 1 \pmod{16}$ exactly when $n \equiv \pm 1 \pmod 8$, i.e. $n \equiv 1$ or $7$, and
$n^2 \equiv 9 \pmod{16}$ when $n \equiv 3$ or $5 \pmod 8$.

