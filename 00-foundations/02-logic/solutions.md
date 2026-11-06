# Solutions: Propositional and First-Order Logic

> Companion to [exercises.md](exercises.md) and the [tutorial](README.md).

Every truth table below has one column per subformula. Where an argument can be settled by a law instead
of a table, both routes are noted.

## Beginner

### Solution 1

* (a) **Statement**, true: $7$ has no divisors other than $1$ and $7$.
* (b) **Not a statement**: $x$ is a free variable, so the sentence is a predicate. It becomes a
  statement only when $x$ is assigned a value (or bound by a quantifier), and its truth value then
  depends on that value.
* (c) **Not a statement**: it is a command, so it has no truth value.
* (d) **Statement**, false: $5 > 2$.
* (e) **Not a statement.** If it were true, then what it says would be the case, so it would be false;
  if it were false, then it would be true. No consistent truth value exists.
* (f) **Statement**: Goldbach's conjecture. Its truth value is unknown, but it is determined; "unknown"
  is an epistemic fact about us, not a third truth value.
* (g) **Not a statement**: it is a question.

### Solution 2

**Strategy.** Compute both columns; compare row by row.

| $P$ | $Q$ | $\neg P$ | $\neg P \lor Q$ | $P \to Q$ |
|---|---|---|---|---|
| T | T | F | T | T |
| T | F | F | F | F |
| F | T | T | T | T |
| F | F | T | T | T |

The last two columns agree in all four rows, so

$$
P \to Q \;\equiv\; \neg P \lor Q.
$$

**Conclusion.** Implication is not a new connective at the level of truth functions: it is definable
from negation and disjunction. This is Proposition 4 of the tutorial and the algebraic reason the
implication table is what it is.

### Solution 3

**Strategy.** Eight rows; compute the inner columns first.

| $P$ | $Q$ | $R$ | $Q \lor R$ | $P \land (Q \lor R)$ | $P \land Q$ | $P \land R$ | $(P \land Q) \lor (P \land R)$ |
|---|---|---|---|---|---|---|---|
| T | T | T | T | T | T | T | T |
| T | T | F | T | T | T | F | T |
| T | F | T | T | T | F | T | T |
| T | F | F | F | F | F | F | F |
| F | T | T | T | F | F | F | F |
| F | T | F | T | F | F | F | F |
| F | F | T | T | F | F | F | F |
| F | F | F | F | F | F | F | F |

The fifth and eighth columns are identical, so

$$
P \land (Q \lor R) \;\equiv\; (P \land Q) \lor (P \land R).
$$

**Conclusion.** Conjunction distributes over disjunction. The dual law,
$P \lor (Q \land R) \equiv (P \lor Q) \land (P \lor R)$, holds as well; it follows from the duality
principle (interchange $\land$ and $\lor$) and can be checked by an eight-row table.

### Solution 4

(a) **Tautology.** $P \lor \neg P$ is T in both rows: if $P$ is T the first disjunct is true; if $P$ is
F the second is true.

(b) **Contradiction.** $P \land \neg P$ is F in both rows: one conjunct is always false.

(c) **Tautology.** If $P$ is true then $P \lor Q$ is true, so the implication is true; if $P$ is false
the implication is vacuously true. Table:

| $P$ | $Q$ | $P \lor Q$ | $P \to (P \lor Q)$ |
|---|---|---|---|
| T | T | T | T |
| T | F | T | T |
| F | T | T | T |
| F | F | F | T |

(d) **Tautology.**

| $P$ | $Q$ | $P \to Q$ | $Q \to P$ | $(P \to Q) \lor (Q \to P)$ |
|---|---|---|---|---|
| T | T | T | T | T |
| T | F | F | T | T |
| F | T | T | F | T |
| F | F | T | T | T |

**Remark.** (d) says that for any two statements, at least one implies the other. This is a
peculiarity of material implication: it holds because a conditional with a false antecedent is true,
not because of any genuine logical connection between $P$ and $Q$.

### Solution 5

(a) In symbols: $\neg(\text{"}5 \text{ is even"})$. In English: "$5$ is not even", equivalently "$5$ is
odd". **True** (the original is false).

(b) Original: $\forall p\,(\operatorname{Prime}(p) \to \operatorname{Odd}(p))$. Negation:
$\exists p\,(\operatorname{Prime}(p) \land \neg\operatorname{Odd}(p))$, i.e. "some prime is not odd".
**True**: $2$ is prime and even.

(c) Original: $\exists x \in \mathbb{Z},\ x < 0$. Negation:
$\forall x \in \mathbb{Z},\ x \ge 0$, i.e. "no integer is negative". **False**, since $-1 < 0$.

### Solution 6

**Strategy.** Compute the table, then look for a simple equivalent by inspection.

| $P$ | $Q$ | $P \lor Q$ | $\neg P$ | $(P \lor Q) \land \neg P$ |
|---|---|---|---|---|
| T | T | T | F | F |
| T | F | T | F | F |
| F | T | T | T | T |
| F | F | F | T | F |

The formula is true only in the third row, where $P$ is false and $Q$ is true. Therefore

$$
(P \lor Q) \land \neg P \;\equiv\; \neg P \land Q.
$$

**Verification.** $\neg P \land Q$ is F, F, T, F in the four rows, matching the fifth column.

**Reading.** "Either $P$ or $Q$, but not $P$" leaves "$Q$, and not $P$" — the disjunctive syllogism
in formula form.

### Solution 7

Let $P(n)$ be "$6 \mid n$" and $Q(n)$ be "$n$ is even".

(a) The four statements are:

* Conditional: $P \to Q$ — "if $6 \mid n$ then $n$ is even".
* Converse: $Q \to P$ — "if $n$ is even then $6 \mid n$".
* Inverse: $\neg P \to \neg Q$ — "if $6 \nmid n$ then $n$ is odd".
* Contrapositive: $\neg Q \to \neg P$ — "if $n$ is odd then $6 \nmid n$".

(b) *Conditional*: **true**. If $n = 6k$ then $n = 2(3k)$, so $n$ is even.

*Converse*: **false**. $n = 2$ is even but $6 \nmid 2$.

*Inverse*: **false**. $n = 2$ satisfies $6 \nmid 2$ but is not odd.

*Contrapositive*: **true**. It is equivalent to the conditional; directly: if $n$ is odd, then $n$ is
not even, so $6 \mid n$ would force $n$ even, a contradiction. Hence $6 \nmid n$.

**Check on the logic.** The conditional and contrapositive agree (both true), and the converse and
inverse agree (both false), exactly as the table of Section 7.5 of the tutorial predicts.

### Solution 8

(a) **$\neg P$.** By modus tollens: $P \to Q$ is equivalent to $\neg Q \to \neg P$, and with the premise
$\neg Q$, modus ponens gives $\neg P$.

(b) **Nothing follows.** From $P \to Q$ and $Q$ one cannot infer $P$: take $P$ false and $Q$ true. The
premises hold ($P \to Q$ is vacuously true) and the conclusion is false. The pattern is *affirming the
consequent*, a fallacy.

### Solution 9

**Symbolisation.** With $R$: it rains, $U$: I have an umbrella, $W$: I get wet,

$$
(R \land \neg U) \to W.
$$

**Negation.** Using $\neg(A \to B) \equiv A \land \neg B$:

$$
\neg\bigl((R \land \neg U) \to W\bigr) \;\equiv\; R \land \neg U \land \neg W.
$$

In English: "it rains, I have no umbrella, and I do not get wet". Note that the negation is a
conjunction, not a conditional: this is the single most common translation error with implications.

### Solution 10

**Strategy.** Three variables would be $8$ rows; here there are two variables, so $4$ rows. Compute the
inner implication first.

| $P$ | $Q$ | $Q \to P$ | $P \to (Q \to P)$ |
|---|---|---|---|
| T | T | T | T |
| T | F | T | T |
| F | T | F | T |
| F | F | T | T |

The final column is all T, so the formula is a tautology.

**Reason without a table.** Either $P$ is true — then $Q \to P$ is true, so $P \to (Q \to P)$ is true —
or $P$ is false, and the outer implication is vacuously true. This is the *positive paradox of material
implication*: a true statement is implied by anything.

### Solution 11

**Formalisation.** Let $U(x)$: "$x$ is a unicorn", $K(x)$: "$x$ is pink". The statement is

$$
\forall x\,(U(x) \to K(x)).
$$

**Why it is true.** In the actual world, $U(x)$ is false for every object $x$, so for every $x$ the
conditional $U(x) \to K(x)$ has a false antecedent and is therefore true (the truth table has T in the
rows with $P$ false). A universal statement whose instances are all true is true. So the statement is
vacuously true.

**Consequence for existence.** This statement does **not** assert that unicorns exist; it asserts only
that nothing is a non-pink unicorn. The false statement would be
$\exists x\,(U(x) \land K(x))$, which additionally claims a witness. This is the $\forall$ with $\to$
versus $\exists$ with $\land$ distinction in action.

### Solution 12

(a) Negation:

$$
\neg\,\forall x > 0,\ x^2 > 0 \;\equiv\; \exists x > 0,\ x^2 \le 0.
$$

**False**: for every real $x$, $x^2 \ge 0$; if $x^2 \le 0$ then $x^2 = 0$ and $x = 0$, which is not
$> 0$. So the original statement is true and its negation is false.

(b) Negation:

$$
\neg\,\exists x \in \mathbb{R},\ x^2 = -1 \;\equiv\; \forall x \in \mathbb{R},\ x^2 \neq -1.
$$

**True**: squares of reals are non-negative.

## Intermediate

### Solution 13

**Strategy.** One table with both sides computed.

| $P$ | $Q$ | $P \land Q$ | $\neg(P \land Q)$ | $\neg P$ | $\neg Q$ | $\neg P \lor \neg Q$ |
|---|---|---|---|---|---|---|
| T | T | T | F | F | F | F |
| T | F | F | T | F | T | T |
| F | T | F | T | T | F | T |
| F | F | F | T | T | T | T |

Columns four and seven agree, so $\neg(P \land Q) \equiv \neg P \lor \neg Q$.

**Dual law.** $\neg(P \lor Q) \equiv \neg P \land \neg Q$. Verify the row $P = \mathrm{T}$,
$Q = \mathrm{F}$: $P \lor Q$ is T, so the left side is F; $\neg P$ is F and $\neg Q$ is T, so the right
side is F. Agreement in this row; the other three rows are checked the same way, and the full table is
in Example 2 of the tutorial.

### Solution 14

**Strategy.** Two columns, one for each conditional.

| $P$ | $Q$ | $P \to Q$ | $\neg Q$ | $\neg P$ | $\neg Q \to \neg P$ |
|---|---|---|---|---|---|
| T | T | T | F | F | T |
| T | F | F | T | F | F |
| F | T | T | F | T | T |
| F | F | T | T | T | T |

Columns three and six agree in all rows.

**Why this matters.** To prove $P \to Q$ it is enough to prove $\neg Q \to \neg P$: assume $\neg Q$ and
derive $\neg P$. This is proof by contrapositive. It is often easier because the hypothesis $\neg Q$ is
a negative statement with more content to use (for example "$n$ is odd" in place of "$n$ is even"), and
the conclusion $\neg P$ is correspondingly concrete. The equivalence guarantees that no generality is
lost: the two statements have identical truth tables, so a proof of one *is* a proof of the other.

### Solution 15

**Strategy.** Compute the two implications and their conjunction, and compare with the biconditional.

| $P$ | $Q$ | $P \to Q$ | $Q \to P$ | $(P \to Q) \land (Q \to P)$ | $P \leftrightarrow Q$ |
|---|---|---|---|---|---|
| T | T | T | T | T | T |
| T | F | F | T | F | F |
| F | T | T | F | F | F |
| F | F | T | T | T | T |

The last two columns agree, so $(P \to Q) \land (Q \to P) \equiv P \leftrightarrow Q$.

**Consequence for proofs.** To prove an "if and only if" statement, prove both directions. Conversely,
when a biconditional is a hypothesis, both implications are available. This is Proposition 8 of the
tutorial.

### Solution 16

**Strategy.** Work backwards from $\neg R$ using modus tollens twice.

The argument is valid. Derivation:

1. $P \to Q$ (premise).
2. $Q \to R$ (premise).
3. $\neg R$ (premise).
4. $\neg Q$ from 2 and 3 by **modus tollens** (since $Q \to R \equiv \neg R \to \neg Q$).
5. $\neg P$ from 1 and 4 by **modus tollens**.

**Check by countermodel search.** Suppose a valuation made the premises true and $\neg P$ false, i.e.
$P$ true. Then $P \to Q$ forces $Q$ true, then $Q \to R$ forces $R$ true, contradicting $\neg R$. No
such valuation exists, so the argument is valid.

### Solution 17

**Strategy.** Seek a valuation with both premises true and the conclusion false; then identify the form.

The argument is **invalid**. Take $P = \mathrm{F}$, $Q = \mathrm{T}$: then $P \to Q$ is T (false
antecedent), $Q$ is T, and $P$ is F. Both premises are true and the conclusion is false.

The form is **affirming the consequent**. Its invalidity is the same fact as the non-equivalence of
$P \to Q$ and $Q \to P$: the argument would be valid only if the converse were a consequence of the
conditional, which it is not.

### Solution 18

**Formalisation.**

$$
\forall x\,\bigl(S(x) \to \exists y\,(P(y) \land R(x,y))\bigr).
$$

**Negation, step by step.**

$$
\begin{aligned}
\neg \forall x\,\bigl(S(x) \to \exists y\,(P(y) \land R(x,y))\bigr)
&\equiv \exists x\, \neg\bigl(S(x) \to \exists y\,(P(y) \land R(x,y))\bigr) && \text{(quantifier negation)}\\
&\equiv \exists x\, \bigl(S(x) \land \neg \exists y\,(P(y) \land R(x,y))\bigr) && (\neg(A \to B) \equiv A \land \neg B)\\
&\equiv \exists x\, \bigl(S(x) \land \forall y\, \neg(P(y) \land R(x,y))\bigr) && \text{(quantifier negation)}\\
&\equiv \exists x\, \bigl(S(x) \land \forall y\, (P(y) \to \neg R(x,y))\bigr) && \text{(De Morgan + implication)}
\end{aligned}
$$

**English.** "Some student has no professor as a supervisor" — more literally, "there is a student such
that every professor fails to supervise that student".

**Check.** The negation is not "no student has a professor as a supervisor", which would be the
negation of an existential claim. The original is universal, so its negation is existential.

### Solution 19

(a) **True.** Let $x \in \mathbb{N}$ be arbitrary. Take $y = x + 1 \in \mathbb{N}$; then $x < y$.
Since $x$ was arbitrary, $\forall x \exists y\,(x<y)$ holds. The witness depends on $x$: this is
essential and is exactly what the quantifier order permits.

(b) **False.** Suppose $y_0 \in \mathbb{N}$ satisfied $x < y_0$ for every $x \in \mathbb{N}$. Taking
$x = y_0$ gives $y_0 < y_0$, a contradiction. Hence no such $y_0$ exists.

**Moral.** $(a) \Rightarrow (b)$ in general, but not conversely: a uniform witness is stronger than a
witness depending on the parameter.

### Solution 20

**Original statement.** $\forall x \in \mathbb{R}\, \exists y \in \mathbb{R},\ y^2 = x$.

**False.** Take $x = -1$. For every real $y$, $y^2 \ge 0 > -1$, so no $y$ satisfies $y^2 = -1$. One
counterexample refutes the universal statement.

**Restricted statement.** $\forall x \in \mathbb{R}_{\ge 0}\, \exists y \in \mathbb{R},\ y^2 = x$.

**True.** For $x \ge 0$, take $y = \sqrt{x}$, the non-negative square root, which exists by the
completeness property of $\mathbb{R}$ (its construction is treated in real analysis). Then
$y^2 = x$.

**Remark.** The restriction changes the truth value, which shows that the domain is part of the
statement. It also shows why quantifier order matters in analysis: a statement of the form
$\forall x \exists y$ allows the witness to depend on $x$, as $\sqrt{x}$ does.

### Solution 21

**Strategy.** Eliminate the implication using $\neg(A \to B) \equiv A \land \neg B$, then push the
negation through the conjunction by De Morgan.

$$
\begin{aligned}
\neg\bigl(P \to (Q \land R)\bigr)
&\equiv P \land \neg(Q \land R) && \text{(negated implication)}\\
&\equiv P \land (\neg Q \lor \neg R) && \text{(De Morgan)}
\end{aligned}
$$

The result uses only $\land$ and $\lor$, and negations apply only to single variables. That is its
*negation normal form*.

**Check by table logic.** The original is false exactly when $P$ is true and $Q \land R$ is false,
i.e. when $P$ is true and at least one of $Q, R$ is false — which is what
$P \land (\neg Q \lor \neg R)$ says.

### Solution 22

Derivation:

1. $P$ (premise).
2. $P \to Q$ (premise).
3. $Q$ from 1 and 2 by **modus ponens**.
4. $Q \to R$ (premise).
5. $R$ from 3 and 4 by **modus ponens**.

**Alternative.** Combine premises 2 and 4 by **hypothetical syllogism** to get $P \to R$, then apply
modus ponens with premise 1 to obtain $R$. Both derivations are correct; the second is shorter.

## Advanced

### Solution 23

(a) **Strategy.** A case argument on $P$, which is the propositional analogue of a truth-table check.

Assume both premises are true. Either $P$ is true or $P$ is false (law of excluded middle).

* If $P$ is true, then $\neg P$ is false; since $\neg P \lor R$ is true, $R$ must be true. Hence
  $Q \lor R$ is true.
* If $P$ is false, then $P \lor Q$ forces $Q$ true. Hence $Q \lor R$ is true.

In both cases the conclusion is true, so the entailment holds. $\blacksquare$

(b) **Strategy.** Resolve pairs of clauses on complementary literals, keeping the resolvent.

1. $P \lor Q$ (premise).
2. $\neg P \lor R$ (premise).
3. $\neg Q \lor S$ (premise).
4. $\neg R \lor S$ (premise).
5. $Q \lor R$ from 1 and 2 by resolution on $P$.
6. $R \lor S$ from 5 and 3 by resolution on $Q$.
7. $S \lor S \equiv S$ from 6 and 4 by resolution on $R$.

Hence the four premises entail $S$.

**Check.** Taking $S$ false and all premises true would require: from 4, $\neg R$; from 3, $\neg Q$;
from 1, $P$; from 2, $R$ — a contradiction. So no countermodel exists.

### Solution 24

(a) **Strategy.** Prove both directions of the biconditional by the meaning of $\forall$.

*($\Rightarrow$)* Assume $\forall x\,(P(x) \land Q(x))$, and let $c$ be an arbitrary element of the
domain. Then $P(c) \land Q(c)$ holds, so $P(c)$ holds by simplification; since $c$ was arbitrary,
$\forall x\,P(x)$. Similarly $Q(c)$ holds, so $\forall x\,Q(x)$. Hence the conjunction
$\forall x\,P(x) \land \forall x\,Q(x)$ holds.

*($\Leftarrow$)* Assume $\forall x\,P(x) \land \forall x\,Q(x)$, and let $c$ be arbitrary. Then $P(c)$
holds and $Q(c)$ holds, so $P(c) \land Q(c)$; since $c$ was arbitrary,
$\forall x\,(P(x) \land Q(x))$.

Both directions hold, so the formulas are equivalent. $\blacksquare$

(b) **Countermodel.** Domain $\mathbb{N}$; $P(x)$: "$x$ is even"; $Q(x)$: "$x$ is odd".

* $\forall x\,(P(x) \lor Q(x))$ is **true**: every natural number is even or odd.
* $\forall x\,P(x)$ is false (not every natural is even) and $\forall x\,Q(x)$ is false (not every
  natural is odd), so $\forall x\,P(x) \lor \forall x\,Q(x)$ is **false**.

Hence the two formulas differ in this interpretation and are not equivalent.

**Why the quantifier cannot distribute.** In $\forall x\,(P \lor Q)$, the *same* $x$ may satisfy
different disjuncts for different $x$; in $\forall x\,P \lor \forall x\,Q$, one disjunct must work
uniformly. The situation is the same as with $\forall\exists$ versus $\exists\forall$.

### Solution 25

**Strategy.** Use the equivalence $A \to B \equiv \neg A \lor B$ in reverse, together with De Morgan.

*Conjunction.*

$$
\neg(P \to \neg Q) \;\equiv\; \neg(\neg P \lor \neg Q) \;\equiv\; P \land Q.
$$

So $P \land Q$ is expressed as $\neg(P \to \neg Q)$, using only $\neg$ and $\to$.

*Disjunction.*

$$
\neg P \to Q \;\equiv\; \neg\neg P \lor Q \;\equiv\; P \lor Q.
$$

So $P \lor Q$ is expressed as $\neg P \to Q$.

**Verification of the first by table.**

| $P$ | $Q$ | $\neg Q$ | $P \to \neg Q$ | $\neg(P \to \neg Q)$ | $P \land Q$ |
|---|---|---|---|---|---|
| T | T | F | F | T | T |
| T | F | T | T | F | F |
| F | T | F | T | F | F |
| F | F | T | T | F | F |

The last two columns agree.

**Conclusion.** Every formula can be written using $\neg, \land, \lor, \to, \leftrightarrow$; the last
three are eliminable in favour of $\neg$ and $\to$; hence $\{\neg, \to\}$ is functionally complete.

### Solution 26

**Strategy.** Push the negation inward one quantifier at a time, then eliminate the implication.

$$
\begin{aligned}
\neg \forall x\,\bigl(P(x) \to Q(x)\bigr)
&\equiv \exists x\, \neg\bigl(P(x) \to Q(x)\bigr) && \text{(quantifier negation: } \neg\forall \equiv \exists\neg\text{)}\\
&\equiv \exists x\, \bigl(P(x) \land \neg Q(x)\bigr) && \text{(negated implication: } \neg(A \to B) \equiv A \land \neg B\text{)}
\end{aligned}
$$

$\blacksquare$

**Meaning.** "Not all $P$'s are $Q$'s" is "some $P$ is not a $Q$". The two steps are exactly the two
rules that students most often skip; writing them out prevents the incorrect
"$\exists x\,(P(x) \to \neg Q(x))$", which would be true as soon as some object fails to be $P$.

**Check with a concrete case.** "Not every student passed" means "some student did not pass", not
"every student failed".

### Solution 27

**Strategy.** Try to build a one-element domain in which the premises hold and the conclusion fails.

Let the domain be $\{a\}$. Define:

* $M(a)$: false — $a$ is not a mathematician;
* $C(a)$: true — $a$ is careful;
* $Po(a)$: true — $a$ is a poet.

Check the premises.

* "All mathematicians are careful": $\forall x(M(x) \to C(x))$. The only instance is
  $M(a) \to C(a) = \mathrm{F} \to \mathrm{T} = \mathrm{T}$. True.
* "Some careful people are poets": $\exists x(C(x) \land Po(x))$; the witness $a$ gives
  $\mathrm{T} \land \mathrm{T} = \mathrm{T}$. True.

Conclusion: "some poets are mathematicians", $\exists x(Po(x) \land M(x))$; the only instance is
$\mathrm{T} \land \mathrm{F} = \mathrm{F}$. False.

Both premises are true and the conclusion false, so the argument is **invalid**. $\blacksquare$

**Diagnosis.** The second premise says some careful people are poets; it does not say that these poets
are mathematicians. In syllogistic terms, the middle term "careful" is not distributed: being careful
is necessary for being a mathematician, but not sufficient.

### Solution 28

**Strategy.** Make $Q$ true of something that is not $P$.

Domain $\{a\}$; let $P(a)$ be false and $Q(a)$ be true.

* $\forall x(P(x) \to Q(x))$: the only instance is $\mathrm{F} \to \mathrm{T} = \mathrm{T}$. True.
* $\exists x\,Q(x)$: witness $a$, $Q(a) = \mathrm{T}$. True.
* $\exists x\,P(x)$: the only instance is false. False.

So the argument is **invalid**.

**Diagnosis.** The premises assert that $Q$ holds of something and that $P$ implies $Q$; that is
compatible with $P$ holding of nothing. The attempted inference treats a necessary condition ($Q$) as
sufficient for $P$ — the quantifier form of affirming the consequent.

**Correct neighbouring argument.** $\forall x(P \to Q)$ together with $\exists x\,P(x)$ does entail
$\exists x\,Q(x)$: take the witness for $P$ and apply the conditional.

### Solution 29

**Formalisation.** Let $Q(x)$ mean "$x$ is rational", for $x \in \mathbb{R}$. The statement is

$$
\forall x\, \forall y\, \bigl((Q(x) \land Q(y)) \to Q(x+y)\bigr).
$$

**Proof.** Let $x, y \in \mathbb{R}$ be arbitrary and assume $Q(x)$ and $Q(y)$. By definition of
rationality, there exist integers $a, b, c, d$ with $b \neq 0$, $d \neq 0$ and

$$
x = \frac{a}{b}, \qquad y = \frac{c}{d}.
$$

Then

$$
x + y = \frac{a}{b} + \frac{c}{d} = \frac{ad + bc}{bd}.
$$

The numerator $ad + bc$ is an integer and the denominator $bd$ is a nonzero integer (a product of
nonzero integers is nonzero). Hence $x + y$ is a quotient of integers with nonzero denominator, i.e.
$Q(x+y)$. Since $x, y$ were arbitrary, the universal statement holds. $\blacksquare$

**Negation.** Pushing the negation inward:

$$
\neg \forall x \forall y\,\bigl((Q(x) \land Q(y)) \to Q(x+y)\bigr)
\equiv \exists x \exists y\, \bigl(Q(x) \land Q(y) \land \neg Q(x+y)\bigr).
$$

In English: "there exist a rational $x$ and a rational $y$ whose sum is not rational". This is false,
which is what the proof shows.

**Pitfall.** The negation is not "the sum of two irrationals is irrational", nor does it concern
irrational inputs at all: the hypothesis $Q(x) \land Q(y)$ survives the negation as a conjunction.

## Challenge

### Solution 30

**Strategy.** Characterize the formulas built from $\leftrightarrow$ and $\oplus$ algebraically, then
show that $P \land Q$ is not in that class.

Work over $\{0,1\}$ with addition modulo $2$, writing $\oplus$ for addition. Then

$$
P \oplus Q = P + Q, \qquad P \leftrightarrow Q = 1 + P + Q,
$$

because the biconditional is the negation of the exclusive or.

*Claim 1.* Every formula $\varphi$ built from variables using only $\leftrightarrow$ and $\oplus$ is
*affine*: there is a constant $c \in \{0,1\}$ and a set $S$ of variables such that

$$
\varphi \;\equiv\; c \oplus \bigoplus_{P_i \in S} P_i .
$$

*Proof of Claim 1 by induction on the formula.*

*Base.* A variable $P$ is affine with $c = 0$, $S = \{P\}$. (Constants are definable:
$P \leftrightarrow P \equiv \top$ and $P \oplus P \equiv \bot$.)

*Step.* Suppose $\varphi = c \oplus \bigoplus_{i \in S} P_i$ and
$\psi = d \oplus \bigoplus_{j \in T} P_j$. Then

$$
\varphi \oplus \psi = (c + d) \oplus \bigoplus_{i \in S \triangle T} P_i,
$$

where $S \triangle T$ is the symmetric difference: variables occurring in both sets cancel because
$P_i \oplus P_i \equiv \bot$. This is affine. Also

$$
\varphi \leftrightarrow \psi = 1 \oplus \varphi \oplus \psi
= (1 + c + d) \oplus \bigoplus_{i \in S \triangle T} P_i,
$$

which is affine. Hence every formula built from $\leftrightarrow$ and $\oplus$ is affine.
$\blacksquare$

*Claim 2.* No affine function equals $P \land Q$.

*Proof.* Let $f$ be affine, $f = c \oplus (a \cdot P) \oplus (b \cdot Q)$ with $a, b \in \{0,1\}$
(indicating whether the variable occurs). Evaluate the alternating sum over the four rows:

$$
f(\mathrm{T},\mathrm{T}) \oplus f(\mathrm{T},\mathrm{F}) \oplus f(\mathrm{F},\mathrm{T}) \oplus f(\mathrm{F},\mathrm{F})
= 4c \oplus 2a \oplus 2b = 0 \oplus 0 \oplus 0 = 0,
$$

since $4c$ and $2a$, $2b$ are even. For $P \land Q$ the same combination is

$$
1 \oplus 0 \oplus 0 \oplus 0 = 1 \neq 0.
$$

So $P \land Q$ is not affine, and by Claim 1 it cannot be expressed. $\blacksquare$

**Remark.** Negation *is* affine: $\neg P \equiv 1 \oplus P$, and also
$\neg P \equiv P \leftrightarrow \bot$ with $\bot := P \oplus P$. So the affine test does not exclude
it. This is consistent: the set
$\{\leftrightarrow, \oplus\}$ can express $\neg$, but Claim 2 shows it cannot express $\land$, so it is
not functionally complete. Being able to express negation is not enough.

### Solution 31

(a) **Strategy.** Suppose both formulas are valid and show that $Q$ is true in an arbitrary valuation.

Let $v$ be any valuation. Since $\models P \to Q$, we have $v(P \to Q) = \mathrm{T}$; since
$\models P$, we have $v(P) = \mathrm{T}$. Look at the truth table of implication: the row with $P$ true
and $P \to Q$ true is the row $(P,Q) = (\mathrm{T},\mathrm{T})$. Hence $v(Q) = \mathrm{T}$. Since $v$
was arbitrary, $\models Q$. $\blacksquare$

(b) **Strategy.** Strong induction on the position in the derivation.

Let $\varphi_1, \dots, \varphi_m$ be a derivation from premises $\Gamma$, and let $v$ be a valuation with
$v \models \gamma$ for every $\gamma \in \Gamma$. Claim: $v \models \varphi_i$ for every
$i = 1, \dots, m$.

*Base and step (combined).* Fix $i$ and assume $v \models \varphi_j$ for all $j < i$. The formula
$\varphi_i$ is either a premise, in which case $v \models \varphi_i$ by hypothesis, or it follows from
some earlier formulas $\varphi_{j_1}, \dots, \varphi_{j_k}$ ($j_1, \dots, j_k < i$) by a rule of
inference. By the induction hypothesis those earlier formulas are true in $v$; by soundness of the
rule, $\varphi_i$ is true in $v$.

By induction, every formula in the derivation is true in $v$, in particular the last one,
$\varphi_m$. Since $v$ was an arbitrary valuation satisfying the premises, every model of $\Gamma$
satisfies $\varphi_m$: $\Gamma \models \varphi_m$. $\blacksquare$

**Comment.** This is the soundness theorem in miniature. It explains why a long proof is trustworthy
even though no one checks it as a whole: each step is local, and truth is preserved at every step.

### Solution 32

(a) **The game.** Think of $\forall x$ as a move by an adversary, who may choose any element of the
domain, and $\exists y$ as a move by you. You win the play if $\varphi(x,y)$ is true of the chosen
values. A *winning strategy* is a rule that tells you which $y$ to play in response to every possible
adversary move. The statement $\forall x \exists y\,\varphi(x,y)$ is true exactly when such a rule
exists: the rule is precisely the function $x \mapsto y(x)$ whose existence the quantifiers assert.
If the statement is false, then for some adversary choice no response works, so the adversary has a
winning strategy. (For alternations of three or more quantifiers the same reading applies, with the
players alternating.)

(b) **First statement:** $\forall \varepsilon > 0\ \exists N\ \forall n > N,\ 1/n < \varepsilon$, with
$\varepsilon$ ranging over the positive reals and $N, n$ over the positive integers.

**True.** Given $\varepsilon > 0$, the Archimedean property of $\mathbb{R}$ provides a positive integer
$N$ with $N > 1/\varepsilon$ (equivalently $1/N < \varepsilon$). Then for every integer $n > N$,
$1/n < 1/N < \varepsilon$. (The Archimedean property is a standard consequence of the completeness of
$\mathbb{R}$ and is proved in real analysis.)

**Second statement:** $\exists N\ \forall \varepsilon > 0\ \forall n > N,\ 1/n < \varepsilon$.

**False.** Suppose $N$ worked. Take $n = N + 1 > N$ and $\varepsilon = \dfrac{1}{2(N+1)} > 0$. Then

$$
\frac{1}{n} = \frac{1}{N+1} = 2\varepsilon > \varepsilon,
$$

contradicting the claimed inequality. So no such $N$ exists.

**Moral.** The witness $N$ must depend on $\varepsilon$; the second statement demands a single $N$ that
works for all $\varepsilon$, which is impossible because the inequalities $1/n < \varepsilon$ become
arbitrarily demanding as $\varepsilon \to 0$.

(c) **Negation of the first statement.** Push the negation inward:

$$
\neg \forall \varepsilon > 0\ \exists N\ \forall n > N,\ \frac{1}{n} < \varepsilon
\;\equiv\; \exists \varepsilon > 0\ \forall N\ \exists n > N,\ \frac{1}{n} \ge \varepsilon.
$$

In words: "there is a positive $\varepsilon$ such that for every $N$ there is some $n > N$ with
$1/n \ge \varepsilon$". This is false, as expected, since the original is true.

### Solution 33

**Strategy.** Find a property preserved by implication and violated by negation.

Call a formula *1-preserving* if it evaluates to T whenever every variable is assigned T.

*Claim.* Every formula built from variables using only $\to$ is 1-preserving.

*Proof by induction on the formula.* A variable $P$ is T under the all-T assignment, so the base case
holds. If $\varphi$ and $\psi$ are 1-preserving, then under the all-T assignment $\varphi$ is T and
$\psi$ is T, so $\varphi \to \psi$ evaluates to $\mathrm{T} \to \mathrm{T} = \mathrm{T}$. Hence
$\varphi \to \psi$ is 1-preserving. $\blacksquare$

Now consider $\neg P$. Under the assignment $P = \mathrm{T}$, it evaluates to F, so it is not
1-preserving. Therefore no formula built from $P$ using only $\to$ is equivalent to $\neg P$; in
particular $\{\to\}$ is not functionally complete.

**Additional remark.** The constant $\bot$ is also not 1-preserving (it is false under every
assignment), so it cannot be expressed either. By contrast $\top$ is 1-preserving and is expressible:
$P \to P$.

### Solution 34

**Formalisation.** Let $\operatorname{Prime}(p)$ abbreviate

$$
p > 1 \;\land\; \forall d\,\bigl((d \mid p) \to (d = 1 \lor d = p)\bigr).
$$

The statement to prove is

$$
\forall n \in \mathbb{N}\ \exists p\,\bigl(\operatorname{Prime}(p) \land p > n\bigr).
$$

**Lemma.** Every integer $N > 1$ has a prime divisor.

*Proof.* Let $S = \{d \in \mathbb{N} : d > 1 \text{ and } d \mid N\}$. The set is nonempty because
$N \in S$. By the well-ordering principle, $S$ has a least element $p$. If $p$ were not prime, there
would exist $a, b$ with $1 < a < p$, $1 < b < p$, and $p = ab$. Then $a \mid p$ and $p \mid N$, so
$a \mid N$ with $a > 1$, contradicting the minimality of $p$. Hence $p$ is prime. $\blacksquare$

**Proof of the statement.** Let $n \in \mathbb{N}$ be arbitrary, and set $N = n! + 1$. Then $N \ge 2$,
so by the lemma $N$ has a prime divisor $p$.

Suppose $p \le n$. Then $p$ is one of the factors of $n! = 1 \cdot 2 \cdots n$, so $p \mid n!$. Since
$p \mid N = n! + 1$ as well, we get

$$
p \mid \bigl((n! + 1) - n!\bigr) = 1,
$$

which is impossible for a prime $p > 1$. Therefore $p > n$. Since $n$ was arbitrary,

$$
\forall n\, \exists p\,(\operatorname{Prime}(p) \land p > n).
$$

$\blacksquare$

**How this encodes infinitude.** The usual phrase "there are infinitely many primes" means that the set
of primes is not finite. A subset of $\mathbb{N}$ is finite exactly when it is bounded, so "the primes
are infinite" is equivalent to "the primes are unbounded", which is the displayed statement. Formally,
the negation of the displayed statement is

$$
\exists n\, \forall p\,\bigl(\operatorname{Prime}(p) \to p \le n\bigr),
$$

i.e. "all primes are at most $n$", which is precisely finiteness (a bounded set of natural numbers is
finite). The proof above shows that this negation is false, so its negation — the displayed
statement — is true.

**Remark.** Euclid's argument is usually phrased with the product of a finite list of primes rather
than with $n!$; both work. Using $n!$ avoids having to assume that the list is complete: every prime
up to $n$ divides $n!$, so $n! + 1$ is coprime to all of them.
