# Exercises: Propositional and First-Order Logic

> Companion to the [tutorial](README.md). Solutions are in [solutions.md](solutions.md).

Write every truth table with one column per subformula, and check the row count before you start:
$n$ variables give $2^n$ rows. For quantifier problems, state the domain before deciding truth values.
Problems are numbered continuously so that the solutions file mirrors them exactly.

## Beginner

**1.** Decide which of the following are statements. For each, say why or why not.

(a) $7$ is prime.
(b) $x + 1 = 3$.
(c) Solve for $x$.
(d) $5 < 2$.
(e) This sentence is false.
(f) Every even integer greater than $2$ is a sum of two primes.
(g) Is $2$ prime?

**2.** Build the truth table of $\neg P \lor Q$ and compare it with the truth table of $P \to Q$. What
do you conclude?

**3.** Build the truth tables of $P \land (Q \lor R)$ and $(P \land Q) \lor (P \land R)$. Compare the
final columns and state the law that the comparison establishes.

**4.** Classify each formula as a tautology, a contradiction, or a contingency:

(a) $P \lor \neg P$;
(b) $P \land \neg P$;
(c) $P \to (P \lor Q)$;
(d) $(P \to Q) \lor (Q \to P)$.

**5.** Write the negation of each statement, both in symbols and in English:

(a) "$5$ is even";
(b) "all primes are odd";
(c) "some integers are negative".

**6.** Build the truth table of $(P \lor Q) \land \neg P$, then find a simpler formula equivalent to it
and verify the equivalence with a second table.

**7.** For the statement "if $n$ is divisible by $6$, then $n$ is even":

(a) write its converse, its inverse, and its contrapositive;
(b) decide the truth value of each of the four statements, with a proof or a counterexample.

**8.** (a) From the premises $P \to Q$ and $\neg Q$, what can be concluded? Name the rule.
(b) From the premises $P \to Q$ and $Q$, what can be concluded? Name the situation.

**9.** Translate into symbols: "If it rains and I have no umbrella, then I get wet." Use $R$, $U$, $W$
for the three atomic statements. Then write the negation in symbols and in English.

**10.** Is $P \to (Q \to P)$ a tautology? Justify with a truth table.

**11.** Explain why "all unicorns are pink" is true even though there are no unicorns. Write the
statement in symbols with a predicate $U(x)$ for "is a unicorn" and $K(x)$ for "is pink", and use the
truth table of implication.

**12.** Negate each statement and say whether the negation is true.

(a) $\forall x > 0,\ x^2 > 0$ (domain $\mathbb{R}$);
(b) $\exists x \in \mathbb{R},\ x^2 = -1$.

## Intermediate

**13.** Prove $\neg(P \land Q) \equiv \neg P \lor \neg Q$ by truth table. State the dual law and verify
one of its rows explicitly.

**14.** Prove $P \to Q \equiv \neg Q \to \neg P$ by truth table. Then explain in one paragraph why this
equivalence justifies proof by contrapositive.

**15.** Show that $(P \to Q) \land (Q \to P) \equiv P \leftrightarrow Q$.

**16.** Decide whether the following argument is valid; if it is, give a derivation naming each rule.

$$
P \to Q,\quad Q \to R,\quad \neg R \quad \therefore \quad \neg P.
$$

**17.** Decide whether the following argument is valid. If it is not, give a countermodel and name the
fallacy.

$$
P \to Q,\quad Q \quad \therefore \quad P.
$$

**18.** Using $S(x)$ for "$x$ is a student", $P(y)$ for "$y$ is a professor", and $R(x,y)$ for
"$y$ supervises $x$", formalise "every student has a supervisor who is a professor". Then negate it,
pushing the negation inward step by step, and translate the result into English.

**19.** Over the domain $\mathbb{N}$, decide the truth value of each statement and justify:

(a) $\forall x\, \exists y\, (x < y)$;
(b) $\exists y\, \forall x\, (x < y)$.

**20.** Over the domain $\mathbb{R}$, decide whether $\forall x\, \exists y\, (y^2 = x)$ is true. Then
restrict the statement to $x \ge 0$ and decide again.

**21.** Simplify $\neg\bigl(P \to (Q \land R)\bigr)$ so that negations apply only to single variables.
Justify each step by naming the law used.

**22.** Give a derivation of $R$ from the premises $P$, $P \to Q$, and $Q \to R$, naming each rule of
inference.

## Advanced

**23.** (a) Prove that resolution is sound: $(P \lor Q) \land (\neg P \lor R) \models Q \lor R$.
(b) Use resolution repeatedly to show
$\{P \lor Q,\ \neg P \lor R,\ \neg Q \lor S,\ \neg R \lor S\} \models S$.

**24.** (a) Prove $\forall x\,(P(x) \land Q(x)) \equiv \forall x\,P(x) \land \forall x\,Q(x)$ by a
semantic argument.
(b) Show that $\forall x\,(P(x) \lor Q(x)) \not\equiv \forall x\,P(x) \lor \forall x\,Q(x)$ by
exhibiting a domain and predicates.

**25.** The set $\{\neg, \to\}$ is functionally complete. Show this by expressing $P \land Q$ and
$P \lor Q$ using only $\neg$ and $\to$. Verify each expression with a truth table or an equivalence
law.

**26.** Prove

$$
\neg \forall x\,(P(x) \to Q(x)) \equiv \exists x\,(P(x) \land \neg Q(x)),
$$

naming every law or quantifier rule used.

**27.** Test the argument: "All mathematicians are careful. Some careful people are poets. Therefore
some poets are mathematicians." If it is invalid, give a countermodel with a one-element domain.

**28.** Test the argument: "$\forall x\,(P(x) \to Q(x))$, and $\exists x\,Q(x)$; therefore
$\exists x\,P(x)$." If it is invalid, give a countermodel and identify the quantifier error.

**29.** Formalise "the sum of two rational numbers is rational" using a predicate $Q(x)$ for "$x$ is
rational" and quantifiers over $\mathbb{R}$. Prove the formal statement, then write its negation
correctly in symbols and in English.

## Challenge

**30.** Prove that no formula built only from the connectives $\leftrightarrow$ and $\oplus$ can express
$P \land Q$. (Show that every such formula is an affine function of its variables over
$\{0,1\}$: $f = c \oplus \bigoplus_{i \in S} P_i$, and that $P \land Q$ is not of this form.)

**31.** (a) Prove that modus ponens is sound: if $\models P \to Q$ and $\models P$, then
$\models Q$.
(b) Prove by induction on the length of a derivation that if every premise is true in a valuation $v$
and every rule is sound, then every formula occurring in the derivation is true in $v$. Conclude that a
derivation from true premises has a true conclusion.

**32.** Interpret $\forall x\, \exists y\, \varphi(x,y)$ as a two-player game: the adversary chooses
$x$, you choose $y$, and you win if $\varphi(x,y)$ holds.

(a) Explain why the statement is true exactly when you have a winning strategy.
(b) Over the positive reals, with $\varphi(\varepsilon, N)$ meaning "$\forall n > N,\ 1/n < \varepsilon$"
where $\varepsilon$ ranges over the positive reals and $N, n$ over the positive integers, decide the
truth of $\forall \varepsilon\, \exists N\, \varphi(\varepsilon, N)$ and of
$\exists N\, \forall \varepsilon\, \varphi(\varepsilon, N)$. Justify both.
(c) State the negation of the first statement, with the quantifiers pushed all the way in.

**33.** Prove that the connective $\to$ alone is not functionally complete. (Show by induction that every
formula built from variables using only $\to$ is true when every variable is assigned T; then exhibit a
truth function that does not have this property.)

**34.** Formalise and prove: for every natural number $n$ there is a prime $p$ with $p > n$. Use the
number $n! + 1$, and state separately the lemma that every integer greater than $1$ has a prime
divisor. Explain how the quantifier structure of your statement encodes "there are infinitely many
primes".
