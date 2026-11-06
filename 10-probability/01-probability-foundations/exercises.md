# Probability Foundations — Exercises

> [Probability Foundations](README.md) · 36 problems · Beginner → Challenge · Solutions: [solutions.md](solutions.md)

Work through the problems in order. Every problem is solvable with the definitions and theorems of the
tutorial, and the section reference in each problem tells you where to look. Do not consult
[solutions.md](solutions.md) until you have written an attempt: the attempt is where the learning
happens.

**Conventions.** Dice are fair and independent, a deck is a standard $52$-card deck, and "uniformly at
random" means the uniform measure on the sample space described in the problem. $\mathbb{N}=\{1,2,3,\dots\}$
and $A^{\complement}$ is the complement of $A$ in the sample space under discussion.

## Beginner

**1.** *(§7.1)* Two fair dice are rolled and the ordered pair of results is recorded.

(a) Write down the sample space $\Omega$ and state $\lvert\Omega\rvert$.
(b) Let $A$ be "the sum is $7$". List the outcomes in $A$ and compute $\Pr(A)$.
(c) Let $B$ be "the first die shows $3$". List the outcomes in $B$ and compute $\Pr(B)$.
(d) Let $C$ be "the sum is at least $10$". Compute $\Pr(C)$.
(e) Compute $\Pr(A\cap B)$ and $\Pr(A\cup C)$.

**2.** *(§7.2)* For events $A$ and $B$ suppose $\Pr(A)=0.37$, $\Pr(B)=0.45$ and $\Pr(A\cap B)=0.12$.
Compute $\Pr(A^{\complement})$, $\Pr(A\cup B)$, $\Pr(A^{\complement}\cap B^{\complement})$ and
$\Pr(A\setminus B)$, stating which axiom or theorem you use at each step.

**3.** *(§7.2)* Decide which of the following assignments define a probability measure on
$\Omega=\{1,2,3\}$. For each that does, compute $\Pr(\{2,3\})$.

(a) $p(1)=\tfrac12$, $p(2)=\tfrac13$, $p(3)=\tfrac16$;
(b) $p(1)=p(2)=p(3)=\tfrac12$;
(c) $p(1)=0.4$, $p(2)=0.6$, $p(3)=0$;
(d) $p(1)=1.1$, $p(2)=-0.1$, $p(3)=0$;
(e) $p(1)=\tfrac12$, $p(2)=\tfrac14$, $p(3)=\tfrac14$.

**4.** *(§7.1)* A fair die is rolled twice. Find

(a) the probability that the sum is at least $10$;
(b) the probability that the sum is even;
(c) the probability that the sum is $12$ or the first roll is $1$.

**5.** *(§7.7)* Two cards are drawn from a well-shuffled deck without replacement. Find the probability
that

(a) both are aces;
(b) at least one is an ace;
(c) exactly one is an ace.

**6.** *(§7.5)* A password of length $4$ is formed from the $26$ letters of the alphabet.

(a) How many passwords are possible if letters may repeat?
(b) How many if all four letters must be distinct?
(c) How many begin with a vowel (A, E, I, O, U) if letters may repeat after the first?

**7.** *(§7.6)* Five cards are dealt from a standard deck.

(a) How many different hands are possible?
(b) How many hands contain exactly two aces?
(c) What is the probability that a hand contains exactly two aces?

**8.** *(§7.7)* An ice-cream shop offers $10$ flavours and sells a cone of $3$ scoops. How many
different orders are there if

(a) the order of the scoops matters and flavours may repeat;
(b) the order matters and the three flavours must be distinct;
(c) the order does not matter and flavours may repeat;
(d) the order does not matter and the flavours must be distinct?

**9.** *(§7.6)* The eleven letters of `STATISTICS` are arranged uniformly at random.

(a) How many distinct arrangements are there?
(b) What is the probability that an arrangement begins with `S`?
(c) What is the probability that it begins with `SS`?

**10.** *(§7.8)* A point is chosen uniformly at random in the unit square $[0,1]^2$. Find the
probability that

(a) it lies within distance $\tfrac12$ of the centre $(\tfrac12,\tfrac12)$;
(b) its distance to the nearest side of the square is less than $\tfrac14$.

**11.** *(§7.2)* Prove that $\Pr(A)\le 1$ for every event $A$, using only the axioms and the results of
§7.2. Say explicitly which results you use.

## Intermediate

**12.** *(§7.3)* For events $A$, $B$, $C$ suppose
$\Pr(A)=0.5$, $\Pr(B)=0.4$, $\Pr(C)=0.3$, $\Pr(A\cap B)=0.2$, $\Pr(A\cap C)=0.1$,
$\Pr(B\cap C)=0.15$ and $\Pr(A\cap B\cap C)=0.05$. Compute

(a) $\Pr(A\cup B\cup C)$;
(b) the probability that none of the three events occurs;
(c) the probability that exactly one of the three occurs.

**13.** *(§7.3)* An integer is chosen uniformly from $\{1,2,\dots,300\}$. Find the probability that it is
divisible by at least one of $3$, $5$, $7$, and check your answer by counting the complement.

**14.** *(§7.6)* Five cards are dealt from a standard deck. Count the hands that contain exactly one
pair (two cards of one rank, and three cards of three other distinct ranks) and compute the probability
of being dealt such a hand.

**15.** *(§7.7)* Ten identical candies are distributed among four children.

(a) In how many ways can this be done with no restriction?
(b) In how many ways if every child receives at least one candy?

**16.** *(§7.6)* In a group of $30$ people, assuming $365$ equally likely and independent birthdays,
compute the probability that all $30$ birthdays are distinct and hence the probability that at least two
people share a birthday. Give both answers to four decimal places and describe the computation you
would perform (a product is acceptable) rather than only the final number.

**17.** *(§7.8)* Two people arrive independently and uniformly between noon and 1 p.m. Each waits
$20$ minutes for the other. Find the probability that they meet, and explain which region of which square
you are measuring.

**18.** *(§8)* Prove that for any two events $A$ and $B$,
$$\Pr(A\cap B)\ge \Pr(A)+\Pr(B)-1.$$
Show by example that the bound can be attained.

**19.** *(§8)* Prove that for any two events $A$ and $B$,
$$\Pr(A\triangle B)=\Pr(A)+\Pr(B)-2\Pr(A\cap B),$$
where $A\triangle B=(A\setminus B)\cup(B\setminus A)$.

**20.** *(§7.6)* Four letters are placed uniformly at random into four addressed envelopes, one letter per
envelope. Find the probability that exactly one letter is in its correct envelope. (Count the
derangements of three objects explicitly.)

**21.** *(§7.6)* Two cards are drawn from a standard deck. Compute the probability that they have the same
suit (a) using an ordered sample space and (b) using an unordered sample space, and check that the two
answers agree.

**22.** *(§8)* Let $A$, $B$, $C$ be pairwise disjoint events. Prove that
$\Pr(A\cup B\cup C)=\Pr(A)+\Pr(B)+\Pr(C)$, and prove also that
$\Pr(A\cup B)+\Pr(A\cap B)=\Pr(A)+\Pr(B)$ for arbitrary events $A$, $B$.

**23.** *(§7.3)* A fair coin is tossed repeatedly, and the first head is awaited.

(a) Show that the probability that the first head occurs at toss $k$ is $2^{-k}$, and verify that these
probabilities sum to $1$.
(b) Using continuity from below, show that the probability that a head eventually occurs is $1$.

## Advanced

**24.** *(§8)* Use inclusion–exclusion to count surjections. Let $n,k\in\mathbb{N}$ and let $N(n,k)$ be the
number of functions from an $n$-element set onto a $k$-element set. Prove that
$$N(n,k)=\sum_{j=0}^{k}(-1)^{j}\binom{k}{j}(k-j)^{n},$$
and check the formula for $n=4$, $k=2$ by an independent count.

**25.** *(§8)* Prove by induction that for events $A_1,\dots,A_n$,
$$\Pr\Bigl(\bigcup_{i=1}^{n}A_i\Bigr)\le\sum_{i=1}^{n}\Pr(A_i).$$
Give an example with $n=2$ where the inequality is strict, and say exactly when equality holds.

**26.** *(§8)* Prove the three-event Bonferroni inequality
$$\Pr(A\cap B\cap C)\ge \Pr(A)+\Pr(B)+\Pr(C)-2$$
for arbitrary events $A$, $B$, $C$. (Hint: bound the probability of the union of the complements.)

**27.** *(§7.7)*

(a) Prove carefully that the stars-and-bars encoding is a bijection between multisets of size $k$ chosen
from $n$ types and arrangements of $k$ stars and $n-1$ bars.
(b) Deduce that the number of non-decreasing sequences $1\le a_1\le a_2\le\cdots\le a_k\le n$ is
$\binom{n+k-1}{k}$.
(c) Evaluate this for $n=6$, $k=3$, and confirm the count by listing the sequences grouped by the
value of $a_1$ and checking that the group sizes sum to $\binom{8}{3}$.

**28.** *(§7.6)* Each of $n$ distinct balls is thrown independently and uniformly at random into one of
$n$ boxes.

(a) Prove that the probability that no box is empty is $n!/n^{n}$.
(b) Evaluate this probability for $n=4$ and check it by listing the favourable outcomes.
(c) Explain why the answer tends to $0$ as $n\to\infty$ (a short argument suffices).

**29.** *(§7.4)* Prove that there is no probability measure on $\Omega=\mathbb{N}$ that assigns the same
probability to every singleton $\{n\}$. (This is why "choose a random natural number uniformly" is
meaningless.)

**30.** *(§7.8)* Three points are chosen independently and uniformly on a circle. Prove that the
probability that all three lie in some semicircle is $\tfrac34$. (Hint: for each point $P_i$ let $A_i$ be
the event that all three points lie in the semicircle that starts at $P_i$ and runs clockwise; compute
$\Pr(A_i)$ and show that, outside a probability-zero set, at most one $A_i$ can occur.)

**31.** *(§7.3)* Prove continuity from above: if $A_1\supseteq A_2\supseteq\cdots$ are events, then
$$\Pr\Bigl(\bigcap_{n\ge1}A_n\Bigr)=\lim_{n\to\infty}\Pr(A_n).$$
State clearly where the hypothesis $\Pr(A_1)<\infty$ enters, and explain why it is automatic for a
probability measure but not for a general measure.

## Challenge

**32.** *(§7.6)* Fix $n\ge1$ and let $D_n$ be the event that $n$ independent uniform birthdays (from
$365$ days) are all distinct, so that $\Pr(D_n)=\prod_{k=0}^{n-1}\bigl(1-\tfrac{k}{365}\bigr)$.

(a) Using $1-x\le e^{-x}$ for real $x$, prove that $\Pr(D_n)\le e^{-n(n-1)/730}$.
(b) Deduce that $23$ people suffice for the probability of a shared birthday to exceed $\tfrac12$. You
may use $\ln 2\approx 0.6931472$ and $\tfrac{506}{730}\approx 0.6931507$.
(c) Explain why the bound does not settle the case $n=22$, and what additional work would be needed.

**33.** *(§7.8)* Two points $X$ and $Y$ are chosen independently and uniformly in $[0,1]$. They cut the
segment into three pieces.

(a) Prove that the three pieces form a triangle if and only if each piece has length less than
$\tfrac12$.
(b) Compute the probability that the three pieces form a triangle, using the region
$\{(x,y):0<x<y<1\}$ and its area.

**34.** *(§8)* A random permutation $\sigma$ of $\{1,\dots,n\}$ is chosen uniformly. A *fixed point* is a
value $i$ with $\sigma(i)=i$.

(a) Prove that $\Pr(\sigma\text{ has no fixed point})=\displaystyle\sum_{k=0}^{n}\frac{(-1)^{k}}{k!}$.
(b) Evaluate this for $n=4$ and confirm that the probability of at least one fixed point is
$\tfrac58$.
(c) Using $e=\sum_{k\ge0}1/k!$, show that the probability of no fixed point tends to $e^{-1}$ as
$n\to\infty$.

**35.** *(§7.4)* A chord of a circle of radius $1$ is chosen "at random". Compare the following three
mechanisms, in each case computing the probability that the chord is longer than a side of the inscribed
equilateral triangle (whose side is $\sqrt3$).

(a) Choose both endpoints independently and uniformly on the circumference; equivalently fix one
endpoint and let the other be uniform.
(b) Choose the midpoint of the chord uniformly in the disk.
(c) Choose the distance of the chord from the centre uniformly in $(0,1)$, the chord being perpendicular
to a fixed diameter.

Explain what the example shows about the classical definition of probability.

**36.** *(§7.7)* A fair die is rolled $12$ times. Find the probability that all six faces appear at least
once. Give the exact result as a fraction in lowest terms and its decimal value to four places, and
verify the formula by an independent recursive computation of $p(n,m)$, the probability that exactly
$m$ distinct faces have appeared after $n$ rolls, using
$$p(n,m)=p(n-1,m)\cdot\frac{m}{6}+p(n-1,m-1)\cdot\frac{7-m}{6}.$$
