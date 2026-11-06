# Probability Foundations — Solutions

> [Probability Foundations](README.md) · Solutions to the 36 problems in [exercises.md](exercises.md)

Each solution states the strategy first, then carries out every significant step, and ends with an
independent check where one exists. For proof problems the proof is complete. Pitfalls are flagged
where a problem is designed to expose one.

## Beginner

**1.** *(Strategy: write the sample space explicitly, then read each event off the $6\times6$ table.)*

(a) The outcome is the ordered pair of results, so
$\Omega=\{(i,j):1\le i,j\le6\}$ and $\lvert\Omega\rvert=6\cdot6=36$. Each pair is equally likely, so the
model is classical.

(b) $A=\{(1,6),(2,5),(3,4),(4,3),(5,2),(6,1)\}$ has $6$ outcomes, hence $\Pr(A)=6/36=1/6$.

(c) $B=\{(3,1),(3,2),(3,3),(3,4),(3,5),(3,6)\}$ has $6$ outcomes, hence $\Pr(B)=6/36=1/6$.

(d) Sums at least $10$ are $10$, $11$, $12$, with $3+2+1=6$ outcomes:
$\{(4,6),(5,5),(6,4)\}\cup\{(5,6),(6,5)\}\cup\{(6,6)\}$. So $\Pr(C)=6/36=1/6$.

(e) $A\cap B=\{(3,4)\}$, a single outcome, so $\Pr(A\cap B)=1/36$. The events $A$ ("sum $7$") and $C$
("sum at least $10$") are disjoint, so by finite additivity
$\Pr(A\cup C)=\Pr(A)+\Pr(C)=6/36+6/36=12/36=1/3$.

*Check:* direct count of $A\cup C$ gives the six outcomes of $A$ and the six of $C$, no overlap, twelve
outcomes, $12/36=1/3$. $\checkmark$

**2.** *(Strategy: express each requested event in terms of $A$, $B$, $A\cap B$ and use the algebra of
§7.2 rather than drawing anything.)*

* $\Pr(A^{\complement})=1-\Pr(A)=1-0.37=0.63$ by the complement rule (Theorem 7.3).
* $\Pr(A\cup B)=\Pr(A)+\Pr(B)-\Pr(A\cap B)=0.37+0.45-0.12=0.70$ by inclusion–exclusion (Theorem 7.6).
* $A^{\complement}\cap B^{\complement}=(A\cup B)^{\complement}$ by De Morgan, so the probability is
  $1-0.70=0.30$ by the complement rule applied to $A\cup B$.
* $\Pr(A\setminus B)=\Pr(A)-\Pr(A\cap B)=0.37-0.12=0.25$ by the difference rule (Theorem 7.4), since
  $A\cap B\subseteq A$.

*Check:* the four regions have probabilities $0.25$ ($A$ only), $0.12$ (both), $0.33$ ($B$ only) and
$0.30$ (neither); they sum to $1$. Also $0.25+0.12+0.33=0.70=\Pr(A\cup B)$. $\checkmark$

**3.** *(Strategy: a probability measure on a finite space is exactly a list of non-negative weights
summing to $1$ — Proposition 7.2 and Definition 5.5.)*

(a) $p(1)+p(2)+p(3)=\tfrac12+\tfrac13+\tfrac16=1$ and all weights are non-negative, so this is a
probability measure. Then $\Pr(\{2,3\})=p(2)+p(3)=\tfrac13+\tfrac16=\tfrac12$.

(b) The weights sum to $\tfrac32\ne1$, so K2 fails and this is not a probability measure.

(c) $0.4+0.6+0=1$ with non-negative weights, so it is a probability measure and
$\Pr(\{2,3\})=0.6+0=0.6$.

(d) $p(2)=-0.1<0$, so K1 fails and this is not a probability measure.

(e) $\tfrac12+\tfrac14+\tfrac14=1$, so it is a probability measure and
$\Pr(\{2,3\})=\tfrac14+\tfrac14=\tfrac12$.

*Check:* in each valid case, $\Pr(\{2,3\})=1-p(1)$, which gives $\tfrac12$, $0.6$ and $\tfrac12$
respectively. $\checkmark$

**4.** *(Strategy: enumerate the $36$ equally likely ordered pairs; for parity, use a structural
argument instead of listing.)*

(a) Sums at least $10$ give $3+2+1=6$ outcomes (as in Solution 1(d)), so the probability is
$6/36=1/6$.

(b) The sum is even exactly when the two dice have the same parity. There are $3$ odd and $3$ even
faces on each die, giving $3\cdot3+3\cdot3=18$ outcomes, so the probability is $18/36=1/2$.

(c) "Sum is $12$" is $\{(6,6)\}$; "first roll is $1$" is $\{(1,1),\dots,(1,6)\}$. These events are
disjoint because a pair starting with $1$ cannot sum to $12$. Hence the probability is
$\tfrac1{36}+\tfrac6{36}=\tfrac7{36}$.

*Check:* the complement of (c) is $29/36$; direct count of "sum $12$ or first roll $1$" gives $1+6=7$
outcomes. $\checkmark$

**5.** *(Strategy: for "without replacement", multiply conditional fractions along the draws; for "at
least one", take the complement.)*

(a) The first card is an ace with probability $4/52$; given that, $3$ of the remaining $51$ cards are
aces, so
$$\Pr(\text{both aces})=\frac{4}{52}\cdot\frac{3}{51}=\frac{12}{2652}=\frac{1}{221}\approx0.00452.$$

(b) Complement: no ace. Then both cards come from the $48$ non-aces, so
$$\Pr(\text{at least one ace})=1-\frac{48}{52}\cdot\frac{47}{51}=1-\frac{2256}{2652}=1-\frac{188}{221}=\frac{33}{221}\approx0.1493.$$

(c) Exactly one ace means (ace, non-ace) or (non-ace, ace):
$$\Pr(\text{exactly one ace})=2\cdot\frac{4}{52}\cdot\frac{48}{51}=\frac{384}{2652}=\frac{32}{221}\approx0.1448.$$

*Check:* $\Pr(\text{at least one})=\Pr(\text{exactly one})+\Pr(\text{both})=\frac{32}{221}+\frac{1}{221}=\frac{33}{221}$.
$\checkmark$

**6.** *(Strategy: multiplication principle; decide for each part whether repetition is allowed.)*

(a) Four independent positions, $26$ choices each: $26^4=456\,976$.

(b) Ordered without replacement: $26\cdot25\cdot24\cdot23=358\,800$.

(c) The first letter is a vowel ($5$ choices), the other three are arbitrary ($26$ choices each):
$5\cdot26^3=5\cdot17\,576=87\,880$.

*Check:* (b) $< (a)$, as it must since forbidding repetition can only remove strings. Numerically
$358\,800<456\,976$. $\checkmark$

**7.** *(Strategy: the hand is an unordered $5$-subset, so both numerator and denominator must be
counts of unordered hands; choose the ranks and then the suits.)*

(a) $\binom{52}{5}=2\,598\,960$.

(b) Choose the two aces: $\binom42=6$; choose the three other cards from the $48$ non-aces:
$\binom{48}{3}=17\,296$. Product: $6\cdot17\,296=103\,776$.

(c) $\Pr=\dfrac{103\,776}{2\,598\,960}\approx0.03993$.

*Check by a sequential computation.* Fix positions for the two aces in $\binom52=10$ ways; for one
pattern the probability is
$\frac{4}{52}\cdot\frac{3}{51}\cdot\frac{48}{50}\cdot\frac{47}{49}\cdot\frac{46}{48}
= \frac{25\,944}{6\,497\,400}$, and $10\cdot\frac{25\,944}{6\,497\,400}\approx0.03993$. $\checkmark$

**8.** *(Strategy: locate each question in the four-cell table of §7.7.)*

(a) Ordered, with repetition: $10^3=1000$.

(b) Ordered, without repetition: $10\cdot9\cdot8=720$.

(c) Unordered, with repetition: $\binom{10+3-1}{3}=\binom{12}{3}=220$.

(d) Unordered, without repetition: $\binom{10}{3}=120$.

*Check:* $120<220<720<1000$; each step relaxes a restriction, so the counts must increase in that
order. $\checkmark$

**9.** *(Strategy: multinomial coefficient for (a); for (b) and (c), either count arrangements with a
fixed prefix or use exchangeability of the letters.)*

(a) The multiplicities in `STATISTICS` are $S:3$, $T:3$, $A:1$, $I:2$, $C:1$, totalling $10$. The number
of distinct arrangements is
$$\frac{10!}{3!\,3!\,1!\,2!\,1!}=\frac{3\,628\,800}{6\cdot6\cdot2}=50\,400.$$

(b) Arrangements beginning with `S`: place one `S` first and arrange the remaining $9$ letters, which
have multiplicities $2,3,1,2,1$. Count: $\frac{9!}{2!\,3!\,2!\,1!\,1!}=\frac{362\,880}{24}=15\,120$.
Hence the probability is $\frac{15\,120}{50\,400}=\frac{3}{10}$.

(c) Beginning with `SS`: $\frac{8!}{1!\,3!\,2!\,1!\,1!}=\frac{40\,320}{12}=3360$ arrangements, so the
probability is $\frac{3360}{50\,400}=\frac{1}{15}$.

*Check.* Exchangeability: a uniformly random arrangement has its first letter equal to `S` with
probability $3/10$, since three of the ten positions in a random permutation of the labelled letters are
occupied by `S`. Multiplying, $\Pr(\text{first two are }S)=\frac{3}{10}\cdot\frac{2}{9}=\frac{1}{15}$,
in agreement with (c). $\checkmark$

**10.** *(Strategy: uniform in the square means probability is area; draw the region and compute its
area.)*

(a) The set of points within distance $\tfrac12$ of the centre is the closed disk of radius $\tfrac12$
centred at $(\tfrac12,\tfrac12)$. Its distance to each side is exactly $\tfrac12$, so the disk lies
entirely inside the square. Its area is $\pi(\tfrac12)^2=\tfrac{\pi}{4}$, and the square has area $1$,
so the probability is $\tfrac{\pi}{4}\approx0.7854$.

(b) "Distance to the nearest side at least $\tfrac14$" means $x\in[\tfrac14,\tfrac34]$ and
$y\in[\tfrac14,\tfrac34]$, a square of side $\tfrac12$ and area $\tfrac14$. Hence
$$\Pr(\text{distance to nearest side}<\tfrac14)=1-\tfrac14=\tfrac34.$$

*Check:* in (a) the favourable region touches all four sides, so its area $\pi/4\approx0.785$ must be
less than $1$; in (b) the answer $0.75$ is smaller than (a)'s $0.785$, which is consistent because the
inscribed disk of radius $1/2$ is not contained in the band of points at distance $\ge 1/4$.
$\checkmark$

**11.** *(Strategy: monotonicity plus normalisation.)*

Since $A\subseteq\Omega$ for every event $A$, monotonicity (Theorem 7.4) gives $\Pr(A)\le\Pr(\Omega)$,
and K2 states $\Pr(\Omega)=1$. Hence $\Pr(A)\le1$. Together with K1, which gives $\Pr(A)\ge0$, this
yields $0\le\Pr(A)\le1$. No other axiom is used.

*Remark.* The proof uses the difference rule of Theorem 7.4, which itself is derived from finite
additivity and K1; nothing circular is involved.

## Intermediate

**12.** *(Strategy: use the three-event inclusion–exclusion formula, then the complement, and finally
decompose into the seven regions of the Venn diagram.)*

(a) By Theorem 7.7,
$$\Pr(A\cup B\cup C)=0.5+0.4+0.3-0.2-0.1-0.15+0.05=1.2-0.45+0.05=0.8.$$

(b) "None occurs" is $(A\cup B\cup C)^{\complement}$, so its probability is $1-0.8=0.2$ by the
complement rule.

(c) Decompose into regions. Using $A$ only $=\Pr(A)-\Pr(A\cap B)-\Pr(A\cap C)+\Pr(A\cap B\cap C)$:

* $A$ only: $0.5-0.2-0.1+0.05=0.25$;
* $B$ only: $0.4-0.2-0.15+0.05=0.10$;
* $C$ only: $0.3-0.1-0.15+0.05=0.10$.

Hence $\Pr(\text{exactly one})=0.25+0.10+0.10=0.45$.

*Alternative for (c).* The general identity for "exactly one" is
$\sum\Pr(A_i)-2\sum_{i<j}\Pr(A_i\cap A_j)+3\Pr(A\cap B\cap C)$, because an outcome in exactly one event
is counted once by the first sum and never subtracted, an outcome in exactly two is counted twice then
subtracted twice (net $0$), and an outcome in all three is counted three times, subtracted six times and
then added three times (net $0$). Substituting: $1.2-2(0.45)+3(0.05)=1.2-0.9+0.15=0.45$. $\checkmark$

*Check.* The regions sum to $0.25+0.10+0.10$ (exactly one) $+0.15+0.05+0.10$ (exactly two)
$+0.05$ (all three) $+0.20$ (none), and
$0.45+0.30+0.05+0.20=1$. $\checkmark$

**13.** *(Strategy: inclusion–exclusion with three events, then an independent count of the
complement by blocks.)*

In $\{1,\dots,300\}$ the multiples of $d$ number $\lfloor 300/d\rfloor$. Let $A_d$ be "divisible by $d$".
Then

$$\lvert A_3\rvert=100,\quad \lvert A_5\rvert=60,\quad \lvert A_7\rvert=42,$$
$$\lvert A_3\cap A_5\rvert=\lvert A_{15}\rvert=20,\quad \lvert A_3\cap A_7\rvert=\lvert A_{21}\rvert=14,\quad \lvert A_5\cap A_7\rvert=\lvert A_{35}\rvert=8,$$
$$\lvert A_3\cap A_5\cap A_7\rvert=\lvert A_{105}\rvert=2.$$

By Theorem 7.7 the number of integers divisible by at least one of $3,5,7$ is
$$100+60+42-20-14-8+2=202-42+2=162,$$
so the probability is $\frac{162}{300}=\frac{27}{50}=0.54$.

*Check by the complement.* Count integers coprime to $105=3\cdot5\cdot7$. Each block of $105$
consecutive integers contains $\varphi(105)=105\cdot\frac23\cdot\frac45\cdot\frac67=48$ of them. Now
$300=2\cdot105+90$, so the first $210$ integers contain $2\cdot48=96$ coprime numbers. Among
$1,\dots,90$, the multiples of $3,5,7$ number $30+18+12-6-4-2+0=48$, so $90-48=42$ are coprime. Total:
$96+42=138$ coprime, hence $300-138=162$ divisible by at least one of $3,5,7$. $\checkmark$

**14.** *(Strategy: choose the rank of the pair, the two suits, the three other ranks, and one suit for
each of those three cards — then compare with all five-card hands.)*

The number of hands is $\binom{52}{5}=2\,598\,960$. For exactly one pair:

* the rank of the pair: $13$ choices;
* the two suits of the pair: $\binom42=6$ choices;
* the three other ranks, all different from the pair rank: $\binom{12}{3}=220$ choices;
* one suit for each of those three cards: $4^3=64$ choices.

The count is
$$13\cdot6\cdot220\cdot64=78\cdot220\cdot64=17\,160\cdot64=1\,098\,240,$$
so the probability is
$$\frac{1\,098\,240}{2\,598\,960}\approx0.42257.$$

*Check.* The hand is determined by the pair rank, the pair suits and the three kickers, and no hand is
counted twice because exactly one rank appears twice. As a sanity bound, the answer is below $1/2$,
which is plausible since "no pair and no better" hands make up a large share of the rest. A second
check: if the three kickers were allowed to include a pair, the product $13\cdot6\cdot\binom{12}{3}4^3$
would overcount; the restriction to three distinct ranks is exactly what "exactly one pair" requires.
$\checkmark$

**15.** *(Strategy: think of distributing $10$ identical objects into $4$ labelled boxes; this is the
stars-and-bars count $\binom{n+k-1}{k}$ with $n=4$, $k=10$.)*

(a) The number of non-negative integer solutions of $x_1+x_2+x_3+x_4=10$ is
$\binom{10+4-1}{10}=\binom{13}{10}=\binom{13}{3}=286$.

(b) If every child receives at least one, put $y_i=x_i-1\ge0$; then
$y_1+y_2+y_3+y_4=10-4=6$, whose solutions number $\binom{6+3}{3}=\binom93=84$.

*Check by inclusion–exclusion.* Count solutions with no box empty. With $j$ prescribed boxes empty,
$10$ objects go into $4-j$ boxes, giving $\binom{10+(4-j)-1}{(4-j)-1}=\binom{13-j}{3-j}$ solutions. Hence
$$\sum_{j=0}^{4}(-1)^j\binom4j\binom{13-j}{3-j}=286-4\cdot66+6\cdot11-4\cdot1+0=286-264+66-4=84,$$
in agreement with (b). $\checkmark$

**16.** *(Strategy: compute the complement — all birthdays distinct — as an ordered sample with
replacement.)*

Model the $30$ birthdays as an ordered $30$-tuple of days, so there are $365^{30}$ equally likely
tuples. The tuples with all entries distinct number $365\cdot364\cdots(365-29)=365^{\underline{30}}$.
Hence
$$\Pr(\text{all distinct})=\prod_{k=0}^{29}\Bigl(1-\frac{k}{365}\Bigr)=\frac{365\cdot364\cdots336}{365^{30}}\approx0.2937,$$
and therefore
$$\Pr(\text{at least one shared birthday})\approx1-0.2937=0.7063.$$

*Check.* The exponential approximation
$\prod_{k=0}^{29}e^{-k/365}=\exp\bigl(-\frac{435}{365}\bigr)=e^{-1.1918}\approx0.3037$ is within about
$0.01$ of the exact product, which is the accuracy expected from $1-x\approx e^{-x}$ for small $x$.
$\checkmark$

**17.** *(Strategy: geometric probability in the square of arrival times.)*

Let $X,Y$ be the arrival times in minutes after noon, uniform and independent on $[0,60]$, so $(X,Y)$ is
uniform in a square of area $3600$. They meet iff $\lvert X-Y\rvert\le20$. The complement consists of
$Y>X+20$ and $X>Y+20$, two congruent triangles with legs $40$, each of area
$\tfrac12\cdot40\cdot40=800$. The total excluded area is $1600$, so
$$\Pr(\text{they meet})=1-\frac{1600}{3600}=1-\frac49=\frac59\approx0.5556.$$

*Check.* With a waiting time of $0$ the formula gives $1-1=0$; with a waiting time of $60$ it gives
$1-0=1$. Both extremes are correct, and the answer increases with the waiting time. $\checkmark$

**18.** *(Strategy: solve the inclusion–exclusion identity for $\Pr(A\cap B)$ and bound the union by
$1$.)*

By Theorem 7.6, $\Pr(A\cap B)=\Pr(A)+\Pr(B)-\Pr(A\cup B)$. Since $A\cup B\subseteq\Omega$ and
$\Pr(\Omega)=1$, monotonicity gives $\Pr(A\cup B)\le1$. Therefore
$$\Pr(A\cap B)=\Pr(A)+\Pr(B)-\Pr(A\cup B)\ge\Pr(A)+\Pr(B)-1.$$

*Attainment.* Take $A=B=\Omega$. Then $\Pr(A\cap B)=1$ and $\Pr(A)+\Pr(B)-1=1+1-1=1$, so equality
holds. A less trivial example: $\Omega=\{1,2,3,4\}$ uniform, $A=\{1,2,3\}$, $B=\{1,2,4\}$; then
$\Pr(A)=\Pr(B)=\tfrac34$, $A\cup B=\Omega$, and $\Pr(A\cap B)=\tfrac12=\tfrac34+\tfrac34-1$. $\checkmark$

**19.** *(Strategy: split the symmetric difference into two disjoint pieces.)*

The events $A\setminus B=A\cap B^{\complement}$ and $B\setminus A=B\cap A^{\complement}$ are disjoint, and
their union is $A\triangle B$ by definition. Finite additivity gives
$$\Pr(A\triangle B)=\Pr(A\setminus B)+\Pr(B\setminus A).$$
By the difference rule, $\Pr(A\setminus B)=\Pr(A)-\Pr(A\cap B)$ (since $A\cap B\subseteq A$) and
$\Pr(B\setminus A)=\Pr(B)-\Pr(A\cap B)$. Adding,
$$\Pr(A\triangle B)=\Pr(A)+\Pr(B)-2\Pr(A\cap B).$$

*Check.* If $A=B$, both sides are $0$: the left because $A\triangle A=\varnothing$, the right because
$\Pr(A)+\Pr(A)-2\Pr(A)=0$. If $A\cap B=\varnothing$, the formula reduces to
$\Pr(A\triangle B)=\Pr(A)+\Pr(B)=\Pr(A\cup B)$, which is correct since the union is disjoint.
$\checkmark$

**20.** *(Strategy: choose the letter that is correctly placed, then require a derangement of the
remaining three.)*

Choose which of the four letters is correct: $4$ ways. The other three must all be in wrong envelopes: a
derangement of three objects. List them: if the objects are $a,b,c$, the derangements are $(b,c,a)$ and
$(c,a,b)$, so there are $2$. Hence the number of favourable placements is $4\cdot2=8$, out of
$4!=24$ total placements, and
$$\Pr(\text{exactly one correct})=\frac{8}{24}=\frac13.$$

*Check by complementary counting.* The permutations of four with exactly one fixed point: choose it in
$4$ ways and derange the rest in $2$ ways, giving $8$; those with exactly two fixed points number
$\binom42\cdot1=6$ (the other two must be swapped); exactly three fixed points is impossible (a
permutation fixing three points fixes the fourth); exactly four gives $1$; and no fixed points gives
$9$ (Solution 9.7). Total $8+6+0+1+9=24$. $\checkmark$

**21.** *(Strategy: compute the same event in two sample spaces; the answers must agree because both
models are uniform.)*

(a) *Ordered.* The first card can be anything, and the second must match its suit: there are $12$
remaining cards of that suit among $51$, so
$$\Pr(\text{same suit})=\frac{12}{51}=\frac{4}{17}\approx0.2353.$$

(b) *Unordered.* There are $\binom{52}{2}=1326$ hands. For each of the $4$ suits there are
$\binom{13}{2}=78$ pairs in that suit, so the count is $4\cdot78=312$ and
$$\Pr(\text{same suit})=\frac{312}{1326}=\frac{4}{17}.$$

*Check.* $\frac{12}{51}=\frac{4}{17}$ and $\frac{312}{1326}=\frac{4}{17}$; both equal
$0.2353$. The agreement is forced: the unordered space is the ordered space with the two orders of each
hand identified, so the ratio of favourable to total is unchanged. $\checkmark$

**22.** *(Strategy: two applications of finite additivity, and one inclusion–exclusion identity.)*

*First claim.* Since $A$ and $B$ are disjoint, $A\cup B$ is disjoint from $C$: if $\omega\in(A\cup B)\cap C$
then $\omega\in A\cap C=\varnothing$ or $\omega\in B\cap C=\varnothing$, a contradiction. Hence
$$\Pr(A\cup B\cup C)=\Pr(A\cup B)+\Pr(C)=\Pr(A)+\Pr(B)+\Pr(C),$$
using finite additivity twice.

*Second claim.* By Theorem 7.6, $\Pr(A\cup B)=\Pr(A)+\Pr(B)-\Pr(A\cap B)$; adding $\Pr(A\cap B)$ to both
sides gives $\Pr(A\cup B)+\Pr(A\cap B)=\Pr(A)+\Pr(B)$.

*Check.* The second identity is often written $\Pr(A\cup B)=1-\Pr(A^{\complement}\cap B^{\complement})$;
combining with the first gives a useful pair of "inclusion–exclusion" and "complement" forms. For
$A=B=\Omega$ the second identity reads $1+1=1+1$. $\checkmark$

**23.** *(Strategy: describe the countable sample space, then use continuity from below for the
"eventually" statement.)*

(a) The event "first head at toss $k$" is the single word $T^{k-1}H$, whose probability is
$\bigl(\tfrac12\bigr)^{k-1}\cdot\tfrac12=2^{-k}$, because the tosses are independent. The sum is a
geometric series:
$$\sum_{k\ge1}2^{-k}=2^{-1}\cdot\frac{1}{1-\tfrac12}=1.$$
So the weights of all the words $T^{k-1}H$ total $1$, and the remaining word $TTT\cdots$ must be given
weight $0$ if the measure is to satisfy K2.

(b) Let $E_n$ be "a head appears among the first $n$ tosses". Then $E_1\subseteq E_2\subseteq\cdots$ and
$\bigcup_nE_n$ is "a head eventually occurs". The complement of $E_n$ is the set of words beginning with
$n$ tails, of total weight $\sum_{j\ge n+1}2^{-j}=2^{-n}$, so $\Pr(E_n)=1-2^{-n}$. Theorem 7.9 gives
$$\Pr(\text{heads eventually})=\lim_{n\to\infty}\Pr(E_n)=\lim_{n\to\infty}\bigl(1-2^{-n}\bigr)=1.$$

*Check.* The alternative route uses continuity from above on $F_n$ = "no head in the first $n$ tosses",
which decrease to the all-tails word and satisfy $\Pr(F_n)=2^{-n}\to0$; Corollary 7.10 gives
$\Pr(\text{never heads})=0$. Both routes agree, and neither claims that the all-tails word is
impossible. $\checkmark$

## Advanced

**24.** *(Strategy: count all functions, then subtract those that miss at least one point of the
codomain, using inclusion–exclusion over the missed points.)*

Let $X$ be an $n$-element set, $Y$ a $k$-element set, and $Y=\{y_1,\dots,y_k\}$. There are $k^n$
functions $X\to Y$ in total. For each $j$ let $B_j$ be the set of functions whose image does not contain
$y_j$; a function is onto exactly when it lies outside $\bigcup_{j=1}^kB_j$.

For a non-empty $S\subseteq Y$, a function lies in $\bigcap_{j\in S}B_j$ exactly when its image avoids
every element of $S$, i.e. it maps into $Y\setminus S$, a set of size $k-\lvert S\rvert$; there are
$(k-\lvert S\rvert)^n$ such functions. By Theorem 8.1,

$$\Bigl\lvert\bigcup_{j=1}^kB_j\Bigr\rvert=\sum_{j=1}^{k}(-1)^{j+1}\binom kj(k-j)^n,$$

and therefore

$$N(n,k)=k^n-\sum_{j=1}^{k}(-1)^{j+1}\binom kj(k-j)^n=\sum_{j=0}^{k}(-1)^{j}\binom kj(k-j)^n.$$

*Check with $n=4$, $k=2$.* The formula gives $2^4-2\cdot1^4+1\cdot0^4=16-2=14$. Independently: there are
$16$ functions $\{1,2,3,4\}\to\{a,b\}$, and the non-surjective ones are the two constant functions, so
$16-2=14$. $\checkmark$

*Remark.* With $n=k$ the formula gives the number of bijections, $n!$: the only surjection between
$n$-element sets is a bijection. This is used in Exercise 28.

**25.** *(Strategy: induction on $n$, with the two-event bound as the induction step.)*

For $n=1$, $\Pr(A_1)\le\Pr(A_1)$. Assume the claim for $n-1$ and let $B=\bigcup_{i=1}^{n-1}A_i$. Then
$B\cup A_n=\bigcup_{i=1}^{n}A_i$, and Corollary 7.8 gives

$$\Pr\Bigl(\bigcup_{i=1}^{n}A_i\Bigr)=\Pr(B\cup A_n)\le\Pr(B)+\Pr(A_n)\le\sum_{i=1}^{n-1}\Pr(A_i)+\Pr(A_n),$$

the last step by the induction hypothesis. $\blacksquare$

*Strictness.* Let $\Pr(A)=\Pr(B)=0.6$ and $\Pr(A\cap B)=0.2$. Then
$\Pr(A\cup B)=0.6+0.6-0.2=1.0<1.2$.

*When equality holds.* Write $N(\omega)$ for the number of the events $A_1,\dots,A_n$ containing
$\omega$, and let $p_j=\Pr(N=j)$ for $j=0,\dots,n$. Then
$\Pr(\bigcup_i A_i)=\sum_{j\ge1}p_j$ while $\sum_i\Pr(A_i)=\sum_{j\ge1}jp_j$, so

$$\sum_{i=1}^{n}\Pr(A_i)-\Pr\Bigl(\bigcup_{i=1}^{n}A_i\Bigr)=\sum_{j\ge2}(j-1)p_j\ge0.$$

Equality holds exactly when $p_j=0$ for every $j\ge2$: almost surely, no outcome belongs to two of the
events. $\checkmark$

**26.** *(Strategy: pass to complements, then apply the union bound.)*

By De Morgan, $(A\cap B\cap C)^{\complement}=A^{\complement}\cup B^{\complement}\cup C^{\complement}$.
The union bound (Exercise 25, or Corollary 7.8 twice) gives

$$\Pr(A^{\complement}\cup B^{\complement}\cup C^{\complement})\le\Pr(A^{\complement})+\Pr(B^{\complement})+\Pr(C^{\complement})=(1-\Pr(A))+(1-\Pr(B))+(1-\Pr(C)).$$

Therefore

$$\Pr(A\cap B\cap C)=1-\Pr\bigl((A\cap B\cap C)^{\complement}\bigr)\ge1-\bigl[3-\Pr(A)-\Pr(B)-\Pr(C)\bigr]=\Pr(A)+\Pr(B)+\Pr(C)-2.$$

*Check.* For $A=B=C=\Omega$ the inequality reads $1\ge1$, with equality. For three events each of
probability $0.9$, it gives $\Pr(A\cap B\cap C)\ge0.7$, which is sharp: three sets of probability $0.9$
can miss $0.1$ each of the space and still cover it. $\checkmark$

**27.** *(Strategy: build an explicit bijection, then read the formula off the number of strings.)*

(a) For a vector $x=(x_1,\dots,x_n)$ of non-negative integers with $\sum_ix_i=k$, define $\Phi(x)$ to be
the word with $x_1$ stars, then a bar, then $x_2$ stars, then a bar, …, then $x_n$ stars, using exactly
$n-1$ bars. This word contains $k$ stars and $n-1$ bars.

*Injectivity:* from a word produced by $\Phi$, the number of stars between the $(i-1)$-th and $i$-th bar
recovers $x_i$, so distinct vectors give distinct words. *Surjectivity:* given any word with $k$ stars
and $n-1$ bars, split it at the bars into $n$ blocks (possibly empty) and let $x_i$ be the number of
stars in block $i$; then $\sum x_i=k$ and $\Phi(x)$ is that word. Hence $\Phi$ is a bijection, and the
number of vectors equals the number of such words. Choosing the $k$ positions of the stars among the
$(n-1)+k$ positions gives $\binom{n+k-1}{k}$ words.

(b) A non-decreasing sequence $1\le a_1\le\cdots\le a_k\le n$ is determined by how many of its terms
equal each value: put $x_i=\#\{j:a_j=i\}$, so $\sum x_i=k$ and $x_i\ge0$. Conversely, a vector $x$
determines the sequence by listing $x_1$ copies of $1$, then $x_2$ copies of $2$, and so on. This is a
bijection, so the number of non-decreasing sequences is also $\binom{n+k-1}{k}$.

(c) For $n=6$, $k=3$: $\binom{8}{3}=56$. Group the triples $(a_1,a_2,a_3)$ by $a_1$:

| $a_1$ | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| possible $(a_2,a_3)$ with $a_1\le a_2\le a_3\le6$ | 21 | 15 | 10 | 6 | 3 | 1 |

For instance with $a_1=1$ the pairs $(a_2,a_3)$ number $6+5+4+3+2+1=21$ (fix $a_2=1,\dots,6$ and let
$a_3$ range from $a_2$ to $6$), and similarly for the other columns. The total is
$21+15+10+6+3+1=56$. $\checkmark$

**28.** *(Strategy: count assignments as functions from balls to boxes, then use the fact that a
surjection between $n$-element sets is a bijection.)*

(a) An assignment of $n$ distinct balls to $n$ distinct boxes is a function from the set of balls to the
set of boxes; there are $n^n$ such functions, all equally likely. "No box is empty" says the function is
onto. Since domain and codomain both have $n$ elements, an onto function is a bijection, and there are
$n!$ bijections. Hence the probability is $n!/n^n$.

(b) For $n=4$, $4!/4^4=24/256=3/32=0.09375$. Listing: the favourable assignments are exactly the $24$
permutations of the four balls among the four boxes, out of $4^4=256$ ordered assignments. $\checkmark$

(c) Write
$$\frac{n!}{n^n}=\prod_{k=1}^{n}\frac{k}{n}.$$
For every $k\le\lfloor n/2\rfloor$ the factor $k/n$ is at most $\tfrac12$, and all other factors are at
most $1$. Hence
$$\frac{n!}{n^n}\le\Bigl(\frac12\Bigr)^{\lfloor n/2\rfloor}\longrightarrow0.$$

*Remark.* Stirling's formula gives the sharper $n!/n^n\sim\sqrt{2\pi n}\,e^{-n}$.

**29.** *(Strategy: suppose all singletons have the same weight $c$ and split into the cases $c>0$ and
$c=0$.)*

Suppose $\Pr(\{n\})=c$ for every $n\in\mathbb{N}$. By K1, $c\ge0$.

*If $c>0$:* for every $N$, the sets $\{1\},\dots,\{N\}$ are disjoint, so finite additivity gives
$\Pr(\{1,\dots,N\})=Nc$. Choosing $N>1/c$ makes this exceed $1$, contradicting Corollary 7.5
($\Pr\le1$).

*If $c=0$:* countable additivity applied to the disjoint singletons gives
$\Pr(\mathbb{N})=\sum_{n\ge1}\Pr(\{n\})=\sum_{n\ge1}0=0$, contradicting K2 ($\Pr(\mathbb{N})=1$).

Both cases are impossible, so no such measure exists. $\blacksquare$

*Remark.* The argument uses only K1, K2, K3 and finite additivity. It is the precise content of the
statement that "a uniformly random natural number" does not exist; models on $\mathbb{N}$ must use
non-uniform weights such as $p(n)=2^{-n}$.

**30.** *(Strategy: for each point consider the clockwise semicircle starting there; these events are
pairwise disjoint almost surely, and their union is the event of interest.)*

Label the points $P_1,P_2,P_3$ and write $B_i$ for the event that all three points lie in the clockwise
half-open semicircle starting at $P_i$, that is, in the arc of length $\pi$ that begins at $P_i$ and
proceeds clockwise.

*Probability of $B_i$.* Condition on $P_i$. The other two points are independent and uniform on the
circle, and each falls in that arc with probability $\tfrac12$; hence
$\Pr(B_i)=\tfrac12\cdot\tfrac12=\tfrac14$.

*The $B_i$ are pairwise disjoint.* If $B_i$ holds, all points lie in the arc starting at $P_i$ of length
$\pi$, so no point lies in the open semicircle immediately preceding $P_i$; hence $P_i$ is the
counterclockwise-most point of the smallest arc containing all three points. That point is unique when
the three points are distinct, an event of probability $1$ (the points coincide with probability $0$).
So at most one $B_i$ can occur.

*The union is the event of interest.* If all three points lie in some semicircle, let $P_j$ be the
counterclockwise-most point of the smallest arc containing them; then $B_j$ occurs. Conversely $B_i$
plainly implies that all points lie in a semicircle.

Therefore, by finite additivity,

$$\Pr(\text{all in some semicircle})=\Pr\Bigl(\bigcup_{i=1}^{3}B_i\Bigr)=\sum_{i=1}^{3}\Pr(B_i)=3\cdot\frac14=\frac34.$$

*Check.* For $n$ points the same argument gives $n/2^{n-1}$, which is $1$ for $n=1$ and $n=2$ (two points
always lie in a semicircle) and $3/4$ for $n=3$. For $n=4$ it gives $1/2$, which is less than $3/4$ as
expected. $\checkmark$

**31.** *(Strategy: complement the decreasing sequence to an increasing one and apply Theorem 7.9.)*

Let $B_n=A_1\setminus A_n$. Since $A_n\supseteq A_{n+1}$, we have $B_n\subseteq B_{n+1}$; the $B_n$
increase. Also

$$\bigcup_{n\ge1}B_n=A_1\setminus\bigcap_{n\ge1}A_n,$$

because $\omega\in A_1$ fails to lie in $\bigcap_nA_n$ exactly when it lies outside some $A_n$. By
Theorem 7.9, $\Pr\bigl(\bigcup_nB_n\bigr)=\lim_n\Pr(B_n)$. Using the difference rule (valid because
$A_n\subseteq A_1$ and $\Pr(A_1)<\infty$),

$$\Pr(A_1)-\Pr\Bigl(\bigcap_{n\ge1}A_n\Bigr)=\lim_{n\to\infty}\bigl(\Pr(A_1)-\Pr(A_n)\bigr)=\Pr(A_1)-\lim_{n\to\infty}\Pr(A_n).$$

Subtracting the finite number $\Pr(A_1)$ gives the claim. $\blacksquare$

*Where finiteness enters.* The subtraction of $\Pr(A_1)$ requires $\Pr(A_1)<\infty$; for a probability
measure this is automatic since $\Pr(A_1)\le1$. For a general measure it can fail: on $\mathbb{R}$ with
Lebesgue measure, $A_n=[n,\infty)$ decrease to $\varnothing$, yet $\Pr(A_n)=\infty$ for every $n$ and
the limit is $\infty\ne0$.

## Challenge

**32.** *(Strategy: turn the product into an exponential using $1-x\le e^{-x}$, then compare
exponents.)*

(a) For $0\le k\le n-1$ we have $k/365\ge0$, so $1-\frac{k}{365}\le e^{-k/365}$. Multiplying these
inequalities for $k=0,\dots,n-1$,

$$\Pr(D_n)=\prod_{k=0}^{n-1}\Bigl(1-\frac{k}{365}\Bigr)\le\prod_{k=0}^{n-1}e^{-k/365}=\exp\Bigl(-\frac{1}{365}\sum_{k=0}^{n-1}k\Bigr)=\exp\Bigl(-\frac{n(n-1)}{730}\Bigr).$$

(b) For $n=23$, $n(n-1)=506$ and $506/730\approx0.6931507$, while $\ln2\approx0.6931472$. Since the
exponent exceeds $\ln2$,

$$\Pr(D_{23})\le e^{-506/730}<e^{-\ln2}=\tfrac12,$$

so $\Pr(\text{shared birthday})=1-\Pr(D_{23})>\tfrac12$. Hence $23$ people suffice.

(c) For $n=22$ the exponent is $462/730\approx0.6329$, so the bound only gives
$\Pr(D_{22})\le e^{-0.6329}\approx0.531>1/2$, which does not decide the question. The exact product

$$\prod_{k=0}^{21}\Bigl(1-\frac{k}{365}\Bigr)\approx0.5243$$

exceeds $\tfrac12$, so $22$ people do not suffice. Since $\Pr(D_n)$ decreases in $n$ (each additional
person can only create a coincidence), the threshold is exactly $n=23$.

*Remark.* Part (b) shows that a crude analytic bound can settle a threshold question, while (c) shows
that such a bound is not automatically sharp; both techniques — estimation and exact computation — are
part of probabilistic reasoning.

**33.** *(Strategy: translate the triangle inequalities into conditions on the pieces, then measure a
region in the triangle $\{0<x<y<1\}$.)*

(a) Let the pieces have lengths $a,b,c>0$ with $a+b+c=1$. They form a (non-degenerate) triangle exactly
when $a+b>c$, $a+c>b$ and $b+c>a$. Since $a+b=1-c$, the first inequality is $1-c>c$, i.e. $c<\tfrac12$;
the other two are $a<\tfrac12$ and $b<\tfrac12$ in the same way. Hence a triangle is formed exactly when
each piece has length less than $\tfrac12$.

(b) Let $0<X<Y<1$ be the two cut points, so the pieces are $X$, $Y-X$ and $1-Y$. The point $(X,Y)$ is
uniform in the triangle $T=\{0<x<y<1\}$, of area $\tfrac12$. The favourable conditions are

$$X<\tfrac12,\qquad Y-X<\tfrac12,\qquad 1-Y<\tfrac12\ \Longleftrightarrow\ Y>\tfrac12.$$

So the favourable region is
$$F=\{(x,y):0<x<\tfrac12,\ \tfrac12<y<x+\tfrac12\},$$
noting that $x+\tfrac12<1$ for $x<\tfrac12$, so the upper limit is $x+\tfrac12$ rather than $1$. Its area is

$$\operatorname{area}(F)=\int_0^{1/2}\bigl[(x+\tfrac12)-\tfrac12\bigr]\,dx=\int_0^{1/2}x\,dx=\frac12\cdot\frac14=\frac18.$$

Therefore

$$\Pr(\text{the pieces form a triangle})=\frac{\operatorname{area}(F)}{\operatorname{area}(T)}=\frac{1/8}{1/2}=\frac14.$$

*Check.* Equivalently, "not a triangle" means some piece is at least $\tfrac12$, and the three events
(which piece is the long one) are disjoint except on a null set; each has probability $\tfrac14$ by the
same integral, and $3\cdot\tfrac14=\tfrac34$ complements $\tfrac14$. $\checkmark$

**34.** *(Strategy: inclusion–exclusion over the fixed points, using that fixing $k$ specified values
leaves $(n-k)!$ permutations.)*

(a) Let $A_i=\{\sigma(i)=i\}$. There are $n!$ permutations, and for a set $S$ of $k$ values,
$\Pr(\bigcap_{i\in S}A_i)=\frac{(n-k)!}{n!}$. By Theorem 8.1,

$$\Pr\Bigl(\bigcup_{i=1}^{n}A_i\Bigr)=\sum_{k=1}^{n}(-1)^{k+1}\binom nk\frac{(n-k)!}{n!}=\sum_{k=1}^{n}\frac{(-1)^{k+1}}{k!},$$

because $\binom nk\frac{(n-k)!}{n!}=\frac{n!}{k!(n-k)!}\cdot\frac{(n-k)!}{n!}=\frac{1}{k!}$. Hence

$$\Pr(\text{no fixed point})=1-\Pr\Bigl(\bigcup_{i=1}^{n}A_i\Bigr)=1+\sum_{k=1}^{n}\frac{(-1)^{k}}{k!}=\sum_{k=0}^{n}\frac{(-1)^{k}}{k!}.$$

(b) For $n=4$:
$$\sum_{k=0}^{4}\frac{(-1)^k}{k!}=1-1+\frac12-\frac16+\frac1{24}=\frac{12-4+1}{24}=\frac9{24}=\frac38,$$
so $\Pr(\text{at least one fixed point})=1-\tfrac38=\tfrac58$, matching the enumeration of nine
derangements among $24$ permutations in the tutorial.

(c) The partial sums $\sum_{k=0}^{n}(-1)^k/k!$ converge to the power series of $e^{x}$ at $x=-1$,
namely $e^{-1}$: the remainder after $n$ terms is bounded by $1/(n+1)!$, which tends to $0$. Hence
$$\lim_{n\to\infty}\Pr(\text{no fixed point})=e^{-1}\approx0.3679,$$
so about $63.2\%$ of permutations of a large set have at least one fixed point. $\checkmark$

**35.** *(Strategy: fix the geometry, then compute the probability of the same event under three
different measures on the set of chords.)*

The side of the inscribed equilateral triangle in the unit circle is $\sqrt3$. A chord at distance $d$
from the centre has length $2\sqrt{1-d^{2}}$, and it exceeds $\sqrt3$ exactly when
$1-d^{2}>\tfrac34$, i.e. $d<\tfrac12$.

(a) *Random endpoints.* Fix one endpoint and let the other be uniform on the circle. The central angle
$\theta$ between the endpoints is uniform on $(0,\pi)$ (taking the shorter arc), and the chord has length
$2\sin(\theta/2)$. The condition $2\sin(\theta/2)>\sqrt3$ is $\sin(\theta/2)>\sqrt3/2$, i.e.
$\theta/2>\pi/3$, i.e. $\theta>2\pi/3$. Therefore
$$\Pr=\frac{\pi-2\pi/3}{\pi}=\frac13.$$

(b) *Random midpoint.* The midpoint is uniform in the unit disk of area $\pi$, and the chord is longer
than $\sqrt3$ exactly when the midpoint lies in the concentric disk of radius $\tfrac12$, of area
$\pi/4$. Hence
$$\Pr=\frac{\pi/4}{\pi}=\frac14.$$

(c) *Random distance.* The distance $d$ is uniform on $(0,1)$, and the condition is $d<\tfrac12$, so
$$\Pr=\frac{1/2}{1}=\frac12.$$

*What the example shows.* All three mechanisms give the same set of chords and all are invariant under
rotations of the circle, yet they assign different probabilities. The "classical" definition —
favourable over total cases, all cases equally likely — is therefore incomplete: on an infinite
continuum there is no canonical uniform choice, and the probability depends on the mechanism, not only
on the sample space. A probability model must specify the measure, exactly as Definition 5.4 demands.
$\checkmark$

**36.** *(Strategy: inclusion–exclusion over the faces that are missing, then an independent recursive
computation.)*

There are $6^{12}$ equally likely ordered outcomes. Let $B_j$ be "face $j$ never appears". For a set $S$
of $j$ faces, the outcomes missing all of them are the $12$-tuples over the other $6-j$ faces, so
$\lvert\bigcap_{i\in S}B_i\rvert=(6-j)^{12}$. By Theorem 8.1,

$$\Pr(\text{some face missing})=\sum_{j=1}^{6}(-1)^{j+1}\binom6j\Bigl(\frac{6-j}{6}\Bigr)^{12},$$

hence

$$\Pr(\text{all six appear})=\sum_{j=0}^{6}(-1)^{j}\binom6j\Bigl(\frac{6-j}{6}\Bigr)^{12}.$$

Computing the numerator over $6^{12}$:

$$6^{12}-6\cdot5^{12}+15\cdot4^{12}-20\cdot3^{12}+15\cdot2^{12}-6\cdot1^{12}
=2\,176\,782\,336-1\,464\,843\,750+251\,658\,240-10\,628\,820+61\,440-6=953\,029\,440.$$

With $6^{12}=2\,176\,782\,336$ and dividing numerator and denominator by $576$,

$$\Pr(\text{all six appear})=\frac{953\,029\,440}{2\,176\,782\,336}=\frac{1\,654\,565}{3\,779\,136}\approx0.4378.$$

*Independent check by recursion.* Let $p(n,m)$ be the probability that exactly $m$ distinct faces have
appeared after $n$ rolls. Then $p(0,0)=1$, $p(n,m)=0$ for $m>n$, and a roll from state $m$ either repeats
a seen face (probability $m/6$) or shows a new one (probability $(7-m)/6$):

$$p(n,m)=p(n-1,m)\cdot\frac{m}{6}+p(n-1,m-1)\cdot\frac{7-m}{6}.$$

Carrying this out gives the following values (rounded to six places):

| $n$ \ $m$ | 3 | 4 | 5 | 6 |
|---|---|---|---|---|
| 10 | 0.018516 | 0.203052 | 0.506366 | 0.271812 |
| 11 | 0.009427 | 0.144626 | 0.489656 | 0.356206 |
| 12 | 0.004770 | 0.101131 | 0.456255 | 0.437816 |

Each row sums to $1$ together with its omitted entries, and the last entry $p(12,6)\approx0.437816$
agrees with the exact fraction above. $\checkmark$



