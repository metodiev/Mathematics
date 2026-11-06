# Conditional Probability and Independence — Exercises

> [Conditional Probability and Independence](README.md) · 36 problems · Beginner → Challenge · Solutions: [solutions.md](solutions.md)

Work through the problems in order. Every problem is solvable with the definitions and theorems of the
tutorial, and the section reference tells you where to look. Do not consult [solutions.md](solutions.md)
until you have written an attempt.

**Conventions.** Dice are fair and independent, coins are fair, a deck is a standard $52$-card deck, and
"uniformly at random" means the uniform measure on the sample space described. Conditional probabilities
are written $\Pr(A\mid B)$ and are defined only when $\Pr(B)>0$; where a problem introduces a
conditioning event of probability zero, say so.

## Beginner

**1.** *(§7.1)* In a group of $200$ students, $120$ take mathematics, $90$ take physics and $50$ take
both. A student is chosen uniformly at random. Compute

(a) $\Pr(M)$ and $\Pr(P)$, where $M$ and $P$ are the events of taking mathematics and physics;
(b) $\Pr(M\mid P)$ and $\Pr(P\mid M)$;
(c) $\Pr(M\mid P^{\complement})$.

**2.** *(§7.7)* For events $A$ and $B$ suppose $\Pr(A)=0.6$, $\Pr(B)=0.3$ and $\Pr(A\cap B)=0.18$.
Compute $\Pr(A\mid B)$, $\Pr(B\mid A)$, $\Pr(A\cup B)$ and $\Pr(A^{\complement}\cap B^{\complement})$,
and decide whether $A$ and $B$ are independent, justifying your answer.

**3.** *(§7.2)* Three cards are drawn without replacement from a standard deck. Find the probability
that

(a) all three are hearts;
(b) at least one is a heart.

**4.** *(§7.4)* Line 1 produces $60\%$ of a factory's output with a $2\%$ defect rate; line 2 produces
$40\%$ with a $5\%$ defect rate. An item is chosen uniformly from the output. Find the probability that
it is defective, and the probability that a defective item came from line 1.

**5.** *(§7.5)* Urn A contains $3$ red and $7$ blue balls; urn B contains $6$ red and $4$ blue balls. An
urn is chosen uniformly at random and one ball is drawn. Given that the ball is red, find the probability
that urn A was chosen.

**6.** *(§7.7)* Two fair dice are rolled. Let $A$ be "the sum is $7$" and, for $k=1,\dots,6$, let $B_k$
be "the first die shows $k$". Show that $A$ is independent of each $B_k$, and deduce by finite additivity
that $A$ is independent of every event determined by the first die alone.

**7.** *(§7.5)* A disease has prevalence $1\%$. A test has sensitivity $90\%$ and specificity $90\%$.
Find the probability that a person who tests positive has the disease.

**8.** *(§7.5)* In a city, $\Pr(\text{rain})=0.2$, $\Pr(\text{clouds})=0.5$ and
$\Pr(\text{clouds}\mid\text{rain})=0.9$. Find $\Pr(\text{rain}\mid\text{clouds})$.

**9.** *(§7.7)* A fair die is rolled three times. Find the probability of at least one six.

**10.** *(§9)* A two-state Markov chain has transition matrix
$P=\begin{pmatrix}0.7&0.3\\0.4&0.6\end{pmatrix}$, with state $1$ today.

(a) Find the distribution after one step.
(b) Find the probability of state $2$ two days from now.
(c) Find the probability of state $2$ three days from now.

## Intermediate

**11.** *(§7.4)* Three machines produce $50\%$, $30\%$ and $20\%$ of a factory's output, with defect rates
$1\%$, $2\%$ and $4\%$ respectively. An item is defective. Find the probability that it came from
machine 3.

**12.** *(§7.5)* A disease has prevalence $2\%$. A test has sensitivity $90\%$ and specificity $95\%$.
Find the probability that a person who tests positive has the disease, and check your answer with natural
frequencies per $10\,000$ people.

**13.** *(§7.4)* An urn holds $5$ red and $5$ blue balls; two are drawn without replacement. Show that
$\Pr(\text{second is red})=\tfrac12$, and compute $\Pr(\text{first is red}\mid\text{second is red})$.
Explain the direction of the inequality between the two numbers.

**14.** *(§7.7)* Prove that if $A$ and $B$ are independent, then $A$ and $B^{\complement}$ are
independent. Deduce that $A^{\complement}$ and $B^{\complement}$ are independent.

**15.** *(§7.8)* Let $\Omega=\{1,\dots,8\}$ be uniform and let
$A=\{1,2,3,4\}$, $B=\{1,2,5,6\}$, $C=\{1,3,5,7\}$. Verify that $A,B,C$ are pairwise independent and
mutually independent, by computing all four required probabilities.

**16.** *(§7.9)* Two fair coins are tossed. Let $A$ be "first coin heads", $B$ "second coin heads" and
$C$ "the coins differ". Compute $\Pr(A\cap B\mid C)$ and $\Pr(A\mid C)\Pr(B\mid C)$, and state what the
comparison shows.

**17.** *(§7.10)* In a version of Monty Hall with $100$ doors, the contestant picks one door, the host
(who knows where the prize is) opens $98$ other doors showing goats, and offers a switch to the one
remaining closed door. Find the probability that switching wins.

**18.** *(§7.7)* A family has two children, with independent sexes and $\Pr(\text{boy})=\tfrac12$. Find
the probability that both are boys given

(a) at least one is a boy;
(b) the elder is a boy.

**19.** *(§7.12)* A fair coin has landed tails ten times in a row.

(a) Find the probability of heads on the next toss.
(b) Find the probability of at least one tail in the next two tosses.
(c) Given those ten tails, find the expected proportion of heads over the $1010$ tosses in total, and use
it to explain why the law of large numbers does not "repay" the deficit.

**20.** *(§7.7)* Let $A$, $B$, $C$ be events with $A$ independent of $B$, $A$ independent of $C$, and
$B\cap C=\varnothing$. Prove that $A$ is independent of $B\cup C$.

**21.** *(§9)* For the transition matrix $P=\begin{pmatrix}0.7&0.3\\0.4&0.6\end{pmatrix}$, compute $P^2$,
and find the stationary distribution $\pi$ by solving $\pi P=\pi$. Verify your answer by substitution.

## Advanced

**22.** *(§7.4)* Let $\{B_1,B_2,\dots\}$ be a countable partition of $\Omega$ with $\Pr(B_i)>0$ for every
$i$. Prove carefully that $\Pr(A)=\sum_i\Pr(A\mid B_i)\Pr(B_i)$ for every event $A$, indicating exactly
where countable additivity and the multiplication rule are used.

**23.** *(§7.5)* Prove Bayes' theorem for a finite proper partition, and prove that the posterior
probabilities sum to $1$: $\sum_j\Pr(B_j\mid A)=1$ whenever $\Pr(A)>0$.

**24.** *(§7.1, §7.9)*

(a) Prove that for fixed $C$ with $\Pr(C)>0$, the map $A\mapsto\Pr(A\mid C)$ satisfies Kolmogorov's three
axioms.
(b) Show that, when $\Pr(C)>0$ and $\Pr(B\cap C)>0$, conditional independence of $A$ and $B$ given $C$ is
equivalent to $\Pr(A\mid B\cap C)=\Pr(A\mid C)$.

**25.** *(§7.7)* Let $0<\Pr(B)<1$. Prove that $A$ is independent of $B$ if and only if
$\Pr(A\mid B)=\Pr(A\mid B^{\complement})$.

**26.** *(§7.8)* Verify in full that the events $A=\{\text{first coin heads}\}$,
$B=\{\text{second coin heads}\}$ and $C=\{\text{the coins differ}\}$ are pairwise independent but not
mutually independent. Write out the four product conditions and evaluate each side.

**27.** *(§7.8)* Let $\Omega=\{1,\dots,8\}$ be uniform and let $A=\{1,2,3,4\}$, $B=\{1,2,3,5\}$,
$C=\{1,5,6,7\}$. Show that $\Pr(A\cap B\cap C)=\Pr(A)\Pr(B)\Pr(C)$ but that $A$ and $B$ are not
independent. What does this show about the number of conditions in Definition 5.3?

**28.** *(§7.2)* Prove the chain rule by induction:
$$\Pr(A_1\cap\cdots\cap A_n)=\Pr(A_1)\Pr(A_2\mid A_1)\cdots\Pr(A_n\mid A_1\cap\cdots\cap A_{n-1}),$$
stating the hypothesis needed at each step.

**29.** *(§7.5)* A test has sensitivity $S$ and specificity $T$, and the disease prevalence is $p$.
Derive the condition on $p$ under which a positive result is more likely to be a false positive than a
true one, i.e. $\Pr(D\mid+)<\tfrac12$. Evaluate the threshold when $S=T=0.95$, and interpret it.

**30.** *(§7.7)* The Chevalier de Méré compared two bets: at least one six in four rolls of a die, and at
least one double six in twenty-four rolls of two dice.

(a) Compute both probabilities exactly, and their decimal values to four places.
(b) Explain why the two probabilities differ although the expected number of successes is the same
($\tfrac23$) in both games.

**31.** *(§9)* Let $P=\begin{pmatrix}p_{11}&p_{12}\\p_{21}&p_{22}\end{pmatrix}$ be a stochastic matrix for
a two-state chain with $p_{12}+p_{21}>0$.

(a) Prove that $\pi=(\pi_1,\pi_2)$ with $\pi_1=\dfrac{p_{21}}{p_{12}+p_{21}}$ and
$\pi_2=\dfrac{p_{12}}{p_{12}+p_{21}}$ satisfies $\pi P=\pi$ and $\pi_1+\pi_2=1$.
(b) Prove that it is the only stationary distribution.

## Challenge

**32.** *(§7.11)* A family has two children. Assume that each child's sex is independent with
$\Pr(\text{boy})=\tfrac12$, and that each child's birth day is uniformly distributed over the seven days
of the week, independently of everything else. Given that at least one child is a boy born on a Tuesday,
find the probability that both children are boys.

**33.** *(§7.10)* In the Monty Hall setup with three doors, suppose the host does *not* know where the
prize is and opens one of the two doors not chosen by the contestant uniformly at random. The door he
opens happens to show a goat.

(a) Compute the probability that switching wins, given that the opened door shows a goat.
(b) Compare with the standard protocol, where the host always opens a goat door, and explain why the
answers differ although the observed information ("a goat behind the opened door") is the same.

**34.** *(§7.5)* The following table reports success rates for two treatments for kidney stones, split by
stone size (the figures are the well-known Charig–Webb–Payne data):

| | Treatment A | Treatment B |
|---|---|---|
| small stones | $81/87$ | $234/270$ |
| large stones | $192/263$ | $55/80$ |
| both combined | $273/350$ | $289/350$ |

(a) Compute the success rate of each treatment within each stratum, and overall.
(b) Show that treatment A has the higher success rate in both strata but the lower rate overall.
(c) Explain, using the language of conditional probability, how this is possible and what it implies
about combining conditional probabilities.

**35.** *(§7.7)* Independent trials each succeed with probability $p\in(0,1]$.

(a) Show that the probability of no success in the first $n$ trials is $(1-p)^n$.
(b) Using continuity from below, prove that the probability of at least one success eventually is $1$.

**36.** *(§7.5)* Three prisoners A, B and C are told that exactly one will be pardoned, with each equally
likely. A asks the guard, who knows the outcome, to name one of the other two prisoners who will be
executed. The guard names B. Find the probability that A is pardoned, and compare it with the
probability that C is pardoned. Explain the result.
