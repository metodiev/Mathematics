# Conditional Probability and Independence — Solutions

> [Conditional Probability and Independence](README.md) · Solutions to the 36 problems in [exercises.md](exercises.md)

Each solution states the strategy, carries out every significant step, and ends with an independent check
where one exists. For proof problems the proof is complete.

## Beginner

**1.** *(Strategy: fill in the whole contingency table first; conditional probabilities are then ratios of
cells.)*

The given data fill two cells and the margins; the rest follow by subtraction.

| | mathematics | no mathematics | total |
|---|---|---|---|
| physics | 50 | 40 | 90 |
| no physics | 70 | 40 | 110 |
| total | 120 | 80 | 200 |

(a) $\Pr(M)=120/200=0.6$ and $\Pr(P)=90/200=0.45$.

(b) $\Pr(M\mid P)=\dfrac{\Pr(M\cap P)}{\Pr(P)}=\dfrac{50/200}{90/200}=\dfrac{50}{90}=\dfrac59\approx0.5556$,
and $\Pr(P\mid M)=\dfrac{50}{120}=\dfrac{5}{12}\approx0.4167$.

(c) $\Pr(M\mid P^{\complement})=\dfrac{70}{110}=\dfrac{7}{11}\approx0.6364$.

*Check.* The two conditional probabilities in (b) differ, and each lies between the marginal probabilities
in the natural way; all cells sum to $200$ ($50+40+70+40=200$). Also
$\Pr(M)=\Pr(M\mid P)\Pr(P)+\Pr(M\mid P^{\complement})\Pr(P^{\complement})
=\tfrac59\cdot0.45+\tfrac7{11}\cdot0.55=0.25+0.35=0.6$, recovering the marginal by total
probability. $\checkmark$

**2.** *(Strategy: apply the definitions directly; independence is checked by comparing $\Pr(A\cap B)$
with $\Pr(A)\Pr(B)$.)*

* $\Pr(A\mid B)=\dfrac{0.18}{0.3}=0.6$ and $\Pr(B\mid A)=\dfrac{0.18}{0.6}=0.3$.
* $\Pr(A\cup B)=0.6+0.3-0.18=0.72$.
* By De Morgan, $\Pr(A^{\complement}\cap B^{\complement})=1-\Pr(A\cup B)=1-0.72=0.28$.
* Since $\Pr(A)\Pr(B)=0.6\cdot0.3=0.18=\Pr(A\cap B)$, the events are independent.

*Check.* Independence is equivalent to $\Pr(A\mid B)=\Pr(A)$, and indeed $0.6=0.6$; also
$\Pr(B\mid A)=0.3=\Pr(B)$. The complement probability $0.28$ equals
$\Pr(A^{\complement})\Pr(B^{\complement})=0.4\cdot0.7$, as Proposition 7.11 requires. $\checkmark$

**3.** *(Strategy: multiply conditional fractions for the intersection; use the complement for "at least
one".)*

(a) The first card is a heart with probability $13/52$; given that, $12$ of $51$ remain hearts, and then
$11$ of $50$:
$$\Pr(\text{all hearts})=\frac{13}{52}\cdot\frac{12}{51}\cdot\frac{11}{50}=\frac{1716}{132\,600}=\frac{11}{850}\approx0.01294.$$

(b) The complement is "no heart", meaning all three cards come from the $39$ non-hearts:
$$\Pr(\text{at least one heart})=1-\frac{39}{52}\cdot\frac{38}{51}\cdot\frac{37}{50}=1-\frac{54\,834}{132\,600}=\frac{77\,766}{132\,600}=\frac{12\,961}{22\,100}\approx0.5865.$$

*Check by combinations.* Unordered: $\Pr(\text{at least one heart})=1-\binom{39}{3}/\binom{52}{3}
=1-9139/22\,100=12\,961/22\,100$, the same fraction. $\checkmark$

**4.** *(Strategy: total probability for the defect rate; Bayes for the reverse direction.)*

Let $L_1,L_2$ be the lines and $D$ defective. Then $\Pr(L_1)=0.6$, $\Pr(L_2)=0.4$,
$\Pr(D\mid L_1)=0.02$, $\Pr(D\mid L_2)=0.05$, so

$$\Pr(D)=0.6\cdot0.02+0.4\cdot0.05=0.012+0.020=0.032,$$

and

$$\Pr(L_1\mid D)=\frac{\Pr(D\mid L_1)\Pr(L_1)}{\Pr(D)}=\frac{0.012}{0.032}=0.375.$$

*Check.* $\Pr(L_2\mid D)=0.020/0.032=0.625$, and the two posteriors sum to $1$. The defective item is more
likely to come from line 2 even though line 1 makes more items, because line 2's defect rate is more than
twice as high. $\checkmark$

**5.** *(Strategy: Bayes with the partition $\{A,B\}$; the denominator is the total probability of red.)*

$$\Pr(R)=0.5\cdot\frac{3}{10}+0.5\cdot\frac{6}{10}=0.15+0.30=0.45,\qquad
\Pr(A\mid R)=\frac{0.5\cdot0.3}{0.45}=\frac{0.15}{0.45}=\frac13.$$

*Check.* $\Pr(B\mid R)=0.30/0.45=\tfrac23$, and the posteriors sum to $1$. The prior $\tfrac12$ has
fallen because urn B is twice as rich in red, so a red ball is evidence for B. $\checkmark$

**6.** *(Strategy: each $B_k$ has six outcomes, and $A\cap B_k$ has exactly one; then extend to all events
built from the first die by additivity.)*

There are $36$ equally likely ordered pairs, so $\Pr(A)=6/36=\tfrac16$ and
$\Pr(B_k)=6/36=\tfrac16$ for each $k$. The only outcome in $A\cap B_k$ is $(k,7-k)$, so
$\Pr(A\cap B_k)=\tfrac1{36}=\Pr(A)\Pr(B_k)$; hence $A$ is independent of each $B_k$.

Now let $E$ be any event determined by the first die alone, i.e. $E=\bigcup_{k\in S}B_k$ for some set $S$
of values. The $B_k$ are disjoint, so
$$\Pr(A\cap E)=\sum_{k\in S}\Pr(A\cap B_k)=\sum_{k\in S}\Pr(A)\Pr(B_k)=\Pr(A)\Pr(E),$$
using finite additivity and then independence term by term. Hence $A$ is independent of every such $E$.

*Check.* Intuitively, whatever the first die shows, exactly one value of the second die makes the sum $7$,
so the conditional probability is always $\tfrac16$. The calculation confirms that the sum and the first
die are independent, and by symmetry the sum is independent of the second die too. $\checkmark$

**7.** *(Strategy: Bayes with the partition $\{D,D^{\complement}\}$.)*

$$\Pr(D\mid+)=\frac{0.01\cdot0.90}{0.01\cdot0.90+0.99\cdot0.10}=\frac{0.009}{0.009+0.099}=\frac{0.009}{0.108}=\frac1{12}\approx0.0833.$$

*Check.* In a population of $1200$: $12$ diseased, of whom $10.8$ test positive on average; $1188$
healthy, of whom $118.8$ test positive falsely — the ratio $10.8:129.6=1:12$. Proportional counts confirm
$1/12$. $\checkmark$

**8.** *(Strategy: Bayes, or simply the definition of conditional probability twice.)*

$$\Pr(\text{rain}\mid\text{clouds})=\frac{\Pr(\text{clouds}\mid\text{rain})\Pr(\text{rain})}{\Pr(\text{clouds})}=\frac{0.9\cdot0.2}{0.5}=\frac{0.18}{0.5}=0.36.$$

*Check.* $\Pr(\text{clouds}\mid\text{rain})=0.9$ but $\Pr(\text{rain}\mid\text{clouds})=0.36$: clouds are
common, rain is not, and the two numbers answer different questions. From the other side,
$\Pr(\text{rain}\cap\text{clouds})=0.18$ is consistent with
$0.2\cdot0.9=0.18=0.5\cdot0.36$. $\checkmark$

**9.** *(Strategy: complement and independence across rolls.)*

$$\Pr(\text{no six in three rolls})=\Bigl(\frac56\Bigr)^{3}=\frac{125}{216},\qquad
\Pr(\text{at least one six})=1-\frac{125}{216}=\frac{91}{216}\approx0.4213.$$

*Check.* Direct count by the binomial coefficients: exactly one six $\binom31(1/6)(5/6)^2=75/216$,
exactly two $\binom32(1/6)^2(5/6)=15/216$, exactly three $1/216$; total $91/216$. $\checkmark$

**10.** *(Strategy: distributions evolve by $\pi'=\pi P$, so compute successive rows.)*

(a) $\pi_0=(1,0)$, so $\pi_1=(1,0)P=(0.7,0.3)$.

(b) The probability of state $2$ after two steps is $\pi_1$'s second coordinate after another step:
$0.7\cdot0.3+0.3\cdot0.6=0.21+0.18=0.39$. (The probability of state $2$ *one* day ahead is $0.3$.)

(c) Two-step matrix: $P^2=\begin{pmatrix}0.61&0.39\\0.52&0.48\end{pmatrix}$. From state $1$,
the distribution after two steps is $(0.61,0.39)$; after three steps it is
$(0.61,0.39)P=(0.61\cdot0.7+0.39\cdot0.4,\ 0.61\cdot0.3+0.39\cdot0.6)=(0.427+0.156,\ 0.183+0.234)=(0.583,0.417)$.
So the probability of state $2$ in three days is $0.417$.

*Check.* Compute $P^3$ directly: $0.61\cdot0.3+0.39\cdot0.6=0.183+0.234=0.417$, matching. The sequence
$0.3,\,0.39,\,0.417$ increases towards the stationary probability $3/7\approx0.4286$, as expected.
$\checkmark$

## Intermediate

**11.** *(Strategy: total probability for the defect rate, then Bayes for machine 3.)*

With $M_i$ = "made by machine $i$" and $D$ = "defective",
$$\Pr(D)=0.5\cdot0.01+0.3\cdot0.02+0.2\cdot0.04=0.005+0.006+0.008=0.019.$$
Then
$$\Pr(M_3\mid D)=\frac{\Pr(D\mid M_3)\Pr(M_3)}{\Pr(D)}=\frac{0.008}{0.019}=\frac{8}{19}\approx0.4211.$$

*Check.* The other posteriors are $0.005/0.019=5/19$ and $0.006/0.019=6/19$, and
$\tfrac{5+6+8}{19}=1$. Machine 3 is the least productive but contributes the largest share of defects,
because its defect rate is four times machine 1's. $\checkmark$

**12.** *(Strategy: Bayes, then recount in natural frequencies as a check.)*

$$\Pr(D\mid+)=\frac{0.02\cdot0.90}{0.02\cdot0.90+0.98\cdot0.05}=\frac{0.018}{0.018+0.049}=\frac{18}{67}\approx0.2687.$$

Per $10\,000$ people: $200$ diseased, of whom $180$ test positive; $9800$ healthy, of whom
$5\%=490$ test positive falsely. The $670$ positives contain $180$ true ones, so the predictive value is
$180/670=18/67\approx26.9\%$.

*Check.* The two computations agree, and the answer lies between the prevalence $2\%$ and the sensitivity
$90\%$, as it must: a positive result raises the probability substantially but not to the sensitivity.
$\checkmark$

**13.** *(Strategy: total probability over the first draw; then the multiplication rule in reverse order.)*

The partition $\{R_1,B_1\}$ gives
$$\Pr(R_2)=\Pr(R_2\mid R_1)\Pr(R_1)+\Pr(R_2\mid B_1)\Pr(B_1)=\frac49\cdot\frac12+\frac59\cdot\frac12=\frac12.$$
Then
$$\Pr(R_1\mid R_2)=\frac{\Pr(R_2\mid R_1)\Pr(R_1)}{\Pr(R_2)}=\frac{(4/9)(1/2)}{1/2}=\frac49.$$

*Check.* Exchangeability of the two draws forces $\Pr(R_2)=\Pr(R_1)=\tfrac12$. The conditional probability
$\tfrac49$ is *smaller* than $\tfrac12$: knowing the second ball is red means one red ball has been used,
so the first draw faced a slightly redder urn than an unconstrained draw. $\checkmark$

**14.** *(Strategy: write $A$ as a disjoint union according to $B$, then use additivity.)*

Because $A=(A\cap B)\sqcup(A\cap B^{\complement})$,
$$\Pr(A\cap B^{\complement})=\Pr(A)-\Pr(A\cap B)=\Pr(A)-\Pr(A)\Pr(B)=\Pr(A)\bigl(1-\Pr(B)\bigr)=\Pr(A)\Pr(B^{\complement}),$$
where independence was used in the second equality. Hence $A\perp\!\!\!\perp B^{\complement}$. Applying the
result with $B$ replaced by $B^{\complement}$ gives $A\perp\!\!\!\perp(B^{\complement})^{\complement}=B$,
and applying it once more with $A$ replaced by $A^{\complement}$ gives $A^{\complement}\perp\!\!\!\perp B^{\complement}$.

*Check.* The identity is a special case of Proposition 7.11, and for numbers it reads: if
$\Pr(A\cap B)=\Pr(A)\Pr(B)$, then $\Pr(A\cap B^{\complement})=\Pr(A)-\Pr(A)\Pr(B)$. With
$\Pr(A)=0.5$, $\Pr(B)=0.4$: $\Pr(A\cap B)=0.2$, so $\Pr(A\cap B^{\complement})=0.3=0.5\cdot0.6$.
$\checkmark$

**15.** *(Strategy: compute all four product conditions from the eight equally likely outcomes.)*

Each of $A,B,C$ has four elements, so each has probability $\tfrac12$. The pairwise intersections:

| pair | set | probability | product of marginals |
|---|---|---|---|
| $A\cap B$ | $\{1,2\}$ | $2/8=1/4$ | $1/4$ |
| $A\cap C$ | $\{1,3\}$ | $2/8=1/4$ | $1/4$ |
| $B\cap C$ | $\{1,5\}$ | $2/8=1/4$ | $1/4$ |

and the triple intersection is $A\cap B\cap C=\{1\}$, with probability $\tfrac18=(\tfrac12)^3$. All four
conditions of Definition 5.3 hold, so the events are mutually independent (and in particular pairwise
independent).

*Check.* The four conditions are exactly the $2^3-3-1=4$ conditions required for three events; verifying
only the triple product would not have sufficed, but here every condition holds. $\checkmark$

**16.** *(Strategy: compute the conditional probabilities inside the event $C$.)*

The event $C=\{\text{coins differ}\}=\{HT,TH\}$ has probability $\tfrac12$, and inside it the two outcomes
are equally likely. Hence $\Pr(A\mid C)=\tfrac12$ and $\Pr(B\mid C)=\tfrac12$, so the product is
$\tfrac14$. But $A\cap B=\{HH\}$ is disjoint from $C$, so $\Pr(A\cap B\mid C)=0$.

*Check.* $0\ne\tfrac14$, so $A$ and $B$ are *not* conditionally independent given $C$, although they are
independent unconditionally ($\Pr(A\cap B)=\tfrac14=\tfrac12\cdot\tfrac12$). Conditioning on a common
effect — "the coins differ" — creates dependence between two independent causes. $\checkmark$

**17.** *(Strategy: switching wins exactly when the original choice was wrong; the host can always open
goat doors, so the information cannot change that.)*

The prize is behind the chosen door with probability $\tfrac1{100}$. If it is, the host can open $98$ of
the other $99$ doors showing goats, and switching loses. If it is not — probability $\tfrac{99}{100}$ —
the host is forced to leave the prize door closed, and switching wins. Hence
$$\Pr(\text{switch wins})=\frac{99}{100}.$$

*Check by Bayes.* Let $C$ be the original choice and $R$ the single unopened door. Before the host acts,
$\Pr(C)=\tfrac1{100}$ and the remaining probability $\tfrac{99}{100}$ is spread over the $99$ other doors.
The host's action removes $98$ of them without changing the total probability attached to the group,
because he can always perform it. So the probability concentrates on $R$: $\Pr(R)=\tfrac{99}{100}$.
$\checkmark$

**18.** *(Strategy: write the four equally likely ordered outcomes and condition.)*

The sample space is $\{BB,BG,GB,GG\}$, each with probability $\tfrac14$.

(a) $\{BB,BG,GB\}$ has probability $\tfrac34$, and $BB$ has $\tfrac14$, so
$\Pr(BB\mid\text{at least one boy})=\tfrac{1/4}{3/4}=\tfrac13$.

(b) $\{BB,BG\}$ has probability $\tfrac12$, so $\Pr(BB\mid\text{elder is a boy})=\tfrac{1/4}{1/2}=\tfrac12$.

*Check.* In (a) the information excludes only $GG$, leaving three equally likely cases; in (b) it fixes the
elder child and leaves the younger free, giving two equally likely cases. The difference is exactly the
difference between conditioning on an event and conditioning on a coordinate. $\checkmark$

**19.** *(Strategy: independence makes the history irrelevant for future tosses; the law of large numbers
acts on proportions, not on counts.)*

(a) By independence, $\Pr(\text{heads on toss }11\mid\text{ten tails})=\Pr(\text{heads})=\tfrac12$.

(b) The next two tosses are independent of the past, so
$\Pr(\text{at least one tail})=1-\Pr(\text{both heads})=1-\tfrac14=\tfrac34$.

(c) Given the first ten tails, the expected number of heads among the next $1000$ tosses is $500$, so
the expected proportion of heads over all $1010$ tosses is $\frac{500}{1010}\approx0.4950$. The count
shortfall is fixed — ten tails yield $0$ heads where fair tosses would have yielded $5$ on average — but
the denominator keeps growing, so the proportion converges to $\tfrac12$. The law of large numbers
dilutes the imbalance; it does not repay it.

*Check.* $0.5-0.49505=0.00495=5/1010$: the fixed shortfall of five expected heads divided by the growing
total, which tends to $0$ as the number of later tosses grows. $\checkmark$

**20.** *(Strategy: expand $A\cap(B\cup C)$ into disjoint pieces.)*

Since $B\cap C=\varnothing$, the events $A\cap B$ and $A\cap C$ are disjoint and their union is
$A\cap(B\cup C)$. Hence, by finite additivity and the two independence assumptions,
$$\Pr\bigl(A\cap(B\cup C)\bigr)=\Pr(A\cap B)+\Pr(A\cap C)=\Pr(A)\Pr(B)+\Pr(A)\Pr(C)=\Pr(A)\bigl(\Pr(B)+\Pr(C)\bigr)=\Pr(A)\Pr(B\cup C).$$
So $A\perp\!\!\!\perp(B\cup C)$.

*Check.* The result is a special case of the fact that independence is preserved under finite disjoint
unions. The hypothesis $B\cap C=\varnothing$ is exactly what makes $A\cap B$ and $A\cap C$ disjoint, so
that their probabilities can be added without correction. $\checkmark$

**21.** *(Strategy: matrix multiplication for $P^2$; solve the two linear equations for stationarity.)*

$$P^2=\begin{pmatrix}0.7&0.3\\0.4&0.6\end{pmatrix}\begin{pmatrix}0.7&0.3\\0.4&0.6\end{pmatrix}
=\begin{pmatrix}0.49+0.12 & 0.21+0.18\\ 0.28+0.24 & 0.12+0.36\end{pmatrix}
=\begin{pmatrix}0.61&0.39\\0.52&0.48\end{pmatrix}.$$

For stationarity, $\pi_1=0.7\pi_1+0.4\pi_2$ and $\pi_1+\pi_2=1$. The first equation gives
$0.3\pi_1=0.4\pi_2$, so $\pi_1=\tfrac43\pi_2$; substituting into the second,
$\tfrac43\pi_2+\pi_2=1$, hence $\pi_2=\tfrac37$ and $\pi_1=\tfrac47$.

*Check.* $\pi P=\bigl(\tfrac47\cdot0.7+\tfrac37\cdot0.4,\ \tfrac47\cdot0.3+\tfrac37\cdot0.6\bigr)
=\bigl(0.4+\tfrac{1.2}{7},\ \tfrac{1.2}{7}+\tfrac{1.8}{7}\bigr)=\bigl(\tfrac47,\tfrac37\bigr)=\pi$, and
the entries sum to $1$. Also each row of $P^2$ sums to $1$, as it must. $\checkmark$

## Advanced

**22.** *(Strategy: split $A$ into the disjoint pieces cut out by the partition, then apply K3 and the
multiplication rule.)*

Let $\{B_1,B_2,\dots\}$ be a countable partition with $\Pr(B_i)>0$ for all $i$, and let $A$ be any event.

*Step 1: the pieces are disjoint and cover $A$.* If $\omega\in(A\cap B_i)\cap(A\cap B_j)$ with $i\ne j$,
then $\omega\in B_i\cap B_j=\varnothing$, a contradiction; so the $A\cap B_i$ are pairwise disjoint. Also
$\bigcup_i(A\cap B_i)=A\cap\bigcup_iB_i=A\cap\Omega=A$.

*Step 2: countable additivity.* Since $\mathcal{F}$ is a $\sigma$-algebra and the sets are measurable,
K3 applies:
$$\Pr(A)=\sum_i\Pr(A\cap B_i).$$

*Step 3: multiplication rule.* For each $i$, $\Pr(B_i)>0$, so Theorem 7.3 gives
$\Pr(A\cap B_i)=\Pr(A\mid B_i)\Pr(B_i)$. Substituting into Step 2,
$$\Pr(A)=\sum_i\Pr(A\mid B_i)\Pr(B_i). \qquad\blacksquare$$

If the partition is finite, Step 2 uses finite additivity, which is itself a consequence of K3 (topic 1,
§7.2); if it is infinite, convergence is not an issue because all terms are non-negative.

**23.** *(Strategy: apply the multiplication rule to the numerator and the total probability theorem to
the denominator, then sum the posteriors.)*

Let $\{B_1,\dots,B_n\}$ be a finite proper partition and $\Pr(A)>0$. For each $j$,
$$\Pr(B_j\mid A)=\frac{\Pr(A\cap B_j)}{\Pr(A)}=\frac{\Pr(A\mid B_j)\Pr(B_j)}{\Pr(A)},$$
and Theorem 7.6 gives $\Pr(A)=\sum_i\Pr(A\mid B_i)\Pr(B_i)$. Substituting proves the formula.

For the sum,
$$\sum_{j=1}^{n}\Pr(B_j\mid A)=\frac{\sum_j\Pr(A\mid B_j)\Pr(B_j)}{\Pr(A)}=\frac{\Pr(A)}{\Pr(A)}=1,$$
again by Theorem 7.6. $\blacksquare$

*Remark.* Positivity of the posterior numerators follows from K1, so the posterior is a distribution on the
same index set — which is why Bayes' theorem can be applied repeatedly, feeding one posterior in as the
next prior.

**24.** *(Strategy: check the three axioms one at a time; for (b), write every conditional probability as a
ratio with denominator $\Pr(C)$.)*

(a) Fix $C$ with $\Pr(C)>0$ and define $Q(A)=\Pr(A\mid C)$.

* K1: $Q(A)=\Pr(A\cap C)/\Pr(C)\ge0$ because both numerator and denominator are non-negative.
* K2: $Q(\Omega)=\Pr(\Omega\cap C)/\Pr(C)=\Pr(C)/\Pr(C)=1$.
* K3: if $A_1,A_2,\dots$ are pairwise disjoint, then so are $A_i\cap C$, and
  $\bigcup_i(A_i\cap C)=(\bigcup_iA_i)\cap C$. Hence
  $$Q\Bigl(\bigcup_iA_i\Bigr)=\frac{\Pr\bigl((\bigcup_iA_i)\cap C\bigr)}{\Pr(C)}
  =\frac{\sum_i\Pr(A_i\cap C)}{\Pr(C)}=\sum_iQ(A_i).$$

So $Q$ is a probability measure.

(b) Assume $\Pr(C)>0$ and $\Pr(B\cap C)>0$, so that $\Pr(B\mid C)>0$. By definition,
$$\Pr(A\cap B\mid C)=\frac{\Pr(A\cap B\cap C)}{\Pr(C)},$$
while
$$\Pr(A\mid B\cap C)\Pr(B\mid C)=\frac{\Pr(A\cap B\cap C)}{\Pr(B\cap C)}\cdot\frac{\Pr(B\cap C)}{\Pr(C)}=\frac{\Pr(A\cap B\cap C)}{\Pr(C)}.$$
Hence the conditional independence identity $\Pr(A\cap B\mid C)=\Pr(A\mid C)\Pr(B\mid C)$ is equivalent to
$\Pr(A\mid B\cap C)\Pr(B\mid C)=\Pr(A\mid C)\Pr(B\mid C)$, and dividing by the positive number
$\Pr(B\mid C)$ gives $\Pr(A\mid B\cap C)=\Pr(A\mid C)$. $\blacksquare$

**25.** *(Strategy: prove each implication separately; the forward one uses total probability with the
partition $\{B,B^{\complement}\}$.)*

*($\Rightarrow$)* Suppose $\Pr(A\mid B)=\Pr(A\mid B^{\complement})=:c$. By Theorem 7.6 with the partition
$\{B,B^{\complement}\}$,
$$\Pr(A)=c\,\Pr(B)+c\,\Pr(B^{\complement})=c\bigl(\Pr(B)+\Pr(B^{\complement})\bigr)=c.$$
Hence $\Pr(A\mid B)=c=\Pr(A)$, and Proposition 7.10 gives independence.

*($\Leftarrow$)* If $A\perp\!\!\!\perp B$, then $\Pr(A\mid B)=\Pr(A)$ by Proposition 7.10, and
$\Pr(A\mid B^{\complement})=\Pr(A)$ because $A\perp\!\!\!\perp B^{\complement}$ (Proposition 7.11). Hence
the two conditional probabilities are equal. $\blacksquare$

*Remark.* The condition $0<\Pr(B)<1$ guarantees that both conditional probabilities are defined and that
neither conditioning event is the whole space.

**26.** *(Strategy: enumerate the four equally likely outcomes and evaluate each condition.)*

The sample space is $\{HH,HT,TH,TT\}$, each outcome with probability $\tfrac14$. The events are
$A=\{HH,HT\}$, $B=\{HH,TH\}$, $C=\{HT,TH\}$, so each has probability $\tfrac12$.

| condition | left side | right side |
|---|---|---|
| $A,B$ | $\Pr(\{HH\})=\tfrac14$ | $\tfrac12\cdot\tfrac12=\tfrac14$ |
| $A,C$ | $\Pr(\{HT\})=\tfrac14$ | $\tfrac14$ |
| $B,C$ | $\Pr(\{TH\})=\tfrac14$ | $\tfrac14$ |
| $A,B,C$ | $\Pr(\varnothing)=0$ | $\tfrac12\cdot\tfrac12\cdot\tfrac12=\tfrac18$ |

The first three conditions hold, so the events are pairwise independent; the fourth fails, so they are not
mutually independent. $\blacksquare$

*Why the failure is structural.* Given $C$ (the coins differ), the first coin determines the second, so
knowing $A$ tells you $B$; conditioning on the common effect destroys the independence of the causes.

**27.** *(Strategy: compute the triple product and one pairwise product.)*

All eight outcomes are equally likely. Each of $A,B,C$ has four elements, so
$\Pr(A)=\Pr(B)=\Pr(C)=\tfrac12$ and the right side of the triple condition is $\tfrac18$. The triple
intersection is $A\cap B\cap C=\{1\}$, so the left side is also $\tfrac18$: the triple product condition
holds.

But $A\cap B=\{1,2,3\}$ has probability $\tfrac38$, while
$\Pr(A)\Pr(B)=\tfrac14$; the pair $A,B$ is not independent.

*What this shows.* Definition 5.3 lists $2^n-n-1$ conditions for a reason. For $n=3$ there are four
conditions: the three pairwise ones and the triple one. Knowing that the triple product holds tells you
nothing about the pairwise products; both kinds are needed. $\blacksquare$

**28.** *(Strategy: induction on $n$, with the multiplication rule as the induction step.)*

For $n=1$ the formula reads $\Pr(A_1)=\Pr(A_1)$. For $n=2$ it is Theorem 7.3. Assume the formula for
$n-1$, and let $B=A_1\cap\cdots\cap A_{n-1}$; the hypothesis guarantees $\Pr(B)>0$, and also that each
earlier conditioning event has positive probability. Then
$$\Pr(A_1\cap\cdots\cap A_n)=\Pr(B\cap A_n)=\Pr(B)\Pr(A_n\mid B),$$
by Theorem 7.3 applied to $B$ and $A_n$. Substituting the induction hypothesis for $\Pr(B)$ gives
$$\Pr(A_1\cap\cdots\cap A_n)=\Bigl[\Pr(A_1)\cdots\Pr(A_{n-1}\mid A_1\cap\cdots\cap A_{n-2})\Bigr]\Pr(A_n\mid A_1\cap\cdots\cap A_{n-1}),$$
which is the stated product. $\blacksquare$

*Hypothesis.* At each step one needs $\Pr(A_1\cap\cdots\cap A_{k})>0$ for $k=1,\dots,n-1$; otherwise some
conditional probability is undefined. In applications each conditional probability is computed in a model
where the preceding event has positive probability, so the hypothesis is automatic.

**29.** *(Strategy: compare the two terms of the Bayes numerator; the denominator cancels.)*

A positive result is more likely to be false than true exactly when
$$\Pr(D^{\complement}\mid+)>\Pr(D\mid+).$$
Using Bayes with the partition $\{D,D^{\complement}\}$ and writing $p=\Pr(D)$,
$$\Pr(D\mid+)=\frac{pS}{pS+(1-p)(1-T)},\qquad \Pr(D^{\complement}\mid+)=\frac{(1-p)(1-T)}{pS+(1-p)(1-T)}.$$
The denominators are equal and positive, so the inequality is
$$pS<(1-p)(1-T)\iff pS<(1-T)-p(1-T)\iff p\bigl(S+1-T\bigr)<1-T\iff p<\frac{1-T}{S+1-T}.$$

With $S=T=0.95$ the threshold is
$$p<\frac{0.05}{0.95+0.05}=\frac{0.05}{1}=0.05,$$
so a positive result is more likely false than true whenever the prevalence is below $5\%$.

*Check.* At $p=0.05$ the predictive value is
$\frac{0.05\cdot0.95}{0.05\cdot0.95+0.95\cdot0.05}=\frac{0.0475}{0.095}=0.5$, exactly even odds, as the
threshold predicts. $\checkmark$

**30.** *(Strategy: complement plus independence for each game; then compare with the expectation.)*

(a) *Game 1.* No six in four rolls has probability $(5/6)^4$, so
$$\Pr(\text{at least one six})=1-\Bigl(\frac56\Bigr)^4=\frac{1296-625}{1296}=\frac{671}{1296}\approx0.5177.$$

*Game 2.* No double six in one roll has probability $35/36$, so
$$\Pr(\text{at least one double six in }24)=1-\Bigl(\frac{35}{36}\Bigr)^{24}\approx0.4914.$$

(b) The expected number of successes is $4\cdot\tfrac16=\tfrac23$ in game 1 and
$24\cdot\tfrac1{36}=\tfrac23$ in game 2. But the probability of at least one success is not the expected
number of successes: $\Pr(\text{at least one})=1-(1-p)^n$, and for fixed $np$ this decreases as $p$
decreases and $n$ increases, because the successes become spread over more trials and can overlap. The
linear approximation $1-(1-p)^n\approx np-\binom n2p^2$ shows the correction: the second-order term is
larger in game 2 ($\binom{24}{2}(1/36)^2\approx0.213$) than in game 1
($\binom42(1/6)^2\approx0.167$).

*Check.* For small $p$, $1-(1-p)^n\approx np-\tfrac12n(n-1)p^2$. With $np=2/3$, game 1 gives
$0.667-0.167=0.500$ (exact $0.518$) and game 2 gives $0.667-0.213=0.454$ (exact $0.491$); both
approximations are on the correct side, and the ordering matches. $\checkmark$

**31.** *(Strategy: solve the stationarity equations directly, then show the solution is forced.)*

(a) Write $p_{11}=1-p_{12}$ and $p_{22}=1-p_{21}$, since the rows sum to $1$. Let
$D=p_{12}+p_{21}>0$ and $\pi_1=p_{21}/D$, $\pi_2=p_{12}/D$; then $\pi_1+\pi_2=1$ and both are non-negative
(the entries are non-negative and $D>0$). Compute the first coordinate of $\pi P$:

$$(\pi P)_1=\pi_1p_{11}+\pi_2p_{21}=\frac{p_{21}(1-p_{12})}{D}+\frac{p_{12}p_{21}}{D}=\frac{p_{21}}{D}=\pi_1,$$

and similarly $(\pi P)_2=\pi_1p_{12}+\pi_2p_{22}=\pi_2$. So $\pi P=\pi$.

(b) Suppose $\mu=(\mu_1,\mu_2)$ is stationary with $\mu_1+\mu_2=1$. The first coordinate equation is
$$\mu_1=\mu_1(1-p_{12})+(1-\mu_1)p_{21}\iff \mu_1p_{12}=(1-\mu_1)p_{21}\iff \mu_1(p_{12}+p_{21})=p_{21},$$
so $\mu_1=p_{21}/D=\pi_1$ because $D>0$, and then $\mu_2=1-\mu_1=\pi_2$. Hence the stationary distribution
is unique. $\blacksquare$

*Remark.* The condition $p_{12}+p_{21}>0$ excludes the identity matrix, for which every distribution is
stationary.

## Challenge

**32.** *(Strategy: count equally likely (sex, weekday) pairs for the two children, then condition.)*

Model each child by one of $2\times7=14$ equally likely (sex, weekday) labels, and the two children
independently, so there are $14^2=196$ equally likely ordered pairs.

Let $E$ = "at least one child is a boy born on Tuesday" and $F$ = "both children are boys".

*Counting $E$:* the complement is that neither child is a Tuesday boy. Each child has $13$ labels other
than (boy, Tuesday), so the complement has $13^2=169$ outcomes, and $\lvert E\rvert=196-169=27$.

*Counting $F\cap E$:* both are boys gives $7\times7=49$ outcomes; among these, the pairs where neither boy
is a Tuesday boy number $6\times6=36$, so $\lvert F\cap E\rvert=49-36=13$.

Therefore
$$\Pr(F\mid E)=\frac{13/196}{27/196}=\frac{13}{27}\approx0.4815.$$

*Check by likelihood ratios.* Given that a family has two boys, the chance of seeing at least one Tuesday
boy is $1-(6/7)^2=13/49$. Given one boy and one girl, the chance is $1/7=7/49$. The prior odds of $BB$
against a mixed family are $1:2$, so the posterior odds are
$$\frac{13/49}{7/49}\cdot\frac12=\frac{13}{7}\cdot\frac12=\frac{13}{14},$$
giving $\Pr(BB)=13/(13+14)=13/27$. Both routes agree. $\checkmark$

*Interpretation.* Without the weekday information the answer is $\tfrac13$; with it the answer is
$\tfrac{13}{27}<\tfrac12$. The weekday detail is more likely to be observed in a two-boy family, so it
raises the probability of two boys — but not to $\tfrac12$. As the extra category becomes rarer (a
specific minute of birth, say), the answer approaches $\tfrac12$.

**33.** *(Strategy: compute the joint probability of the observed event under each placement, then
normalise.)*

Let $C_i$ be "prize behind door $i$", each with probability $\tfrac13$, and let $G$ be the observed event
"the host opens door 3 and it shows a goat". The contestant has picked door $1$, and the host opens one of
$\{2,3\}$ uniformly at random, without knowledge.

* If $C_1$: both doors $2,3$ hide goats, so $G$ occurs with probability $\tfrac12$ (the host must choose
  door $3$).
* If $C_2$: door $3$ hides a goat and door $2$ the prize, so $G$ occurs with probability $\tfrac12$.
* If $C_3$: door $3$ hides the prize, so $G$ is impossible.

Hence
$$\Pr(G)=\tfrac13\cdot\tfrac12+\tfrac13\cdot\tfrac12+\tfrac13\cdot0=\tfrac13,$$
and
$$\Pr(C_2\mid G)=\frac{\tfrac13\cdot\tfrac12}{\tfrac13}=\frac12,\qquad \Pr(C_1\mid G)=\frac{\tfrac13\cdot\tfrac12}{\tfrac13}=\frac12.$$

(a) Switching wins with probability $\tfrac12$.

(b) Under the standard protocol, the same observation has likelihoods $\tfrac12$ under $C_1$, $1$ under
$C_2$ and $0$ under $C_3$, which is what produces the posterior $\tfrac13$ versus $\tfrac23$. The
difference is not that the observation is uninformative in one protocol, but that the *likelihoods* differ:
a host who must open a goat door is forced to open door $3$ whenever the prize is behind door $2$, so that
observation is twice as likely under $C_2$ as under $C_1$. A host who opens a door at random has the same
chance $\tfrac12$ of opening door $3$ under $C_1$ and under $C_2$, so the observation does not favour
either. Changing the protocol changes $\Pr(\text{observation}\mid C_i)$, not the prior.

*Check.* In the random protocol the posterior probabilities over $\{C_1,C_2,C_3\}$ given $G$ are
$\tfrac12,\tfrac14,\tfrac14$, which sum to $1$; the probability of winning by switching is
$\tfrac14+\tfrac14=\tfrac12$. $\checkmark$

**34.** *(Strategy: compute each conditional success rate as a ratio, then compare weighted averages with
different weights.)*

(a) The rates are:

| | Treatment A | Treatment B |
|---|---|---|
| small stones | $81/87\approx93.1\%$ | $234/270\approx86.7\%$ |
| large stones | $192/263\approx73.0\%$ | $55/80=68.75\%$ |
| combined | $273/350=78.0\%$ | $289/350\approx82.6\%$ |

(b) In each stratum A exceeds B ($93.1>86.7$ and $73.0>68.75$), yet overall B exceeds A
($82.6>78.0$).

(c) The overall rate is a weighted average of the stratum rates, but the weights are the stratum shares
*within each treatment*, and these differ drastically:

$$\Pr(\text{success}\mid A)=\sum_{s}\Pr(\text{success}\mid A,s)\Pr(s\mid A),\qquad
\Pr(\text{success}\mid B)=\sum_s\Pr(\text{success}\mid B,s)\Pr(s\mid B).$$

Here $\Pr(\text{large}\mid A)=263/350\approx75.1\%$ while
$\Pr(\text{large}\mid B)=80/350\approx22.9\%$: treatment A was given mostly to the harder cases. Since
large stones have lower success rates under both treatments, A's overall average is dragged down by its
case mix. This is *Simpson's paradox*: a conditional comparison can reverse when the conditioning variable
is ignored.

*Check.* A's overall successes are $81+192=273$ out of $350$; the stratum decomposition
$\frac{87}{350}\cdot\frac{81}{87}+\frac{263}{350}\cdot\frac{192}{263}=\frac{81+192}{350}$ confirms that the
overall rate is exactly the stratum-weighted average with A's own weights. Recomputing A's overall rate
with B's weights would give a different, higher number — which is the mathematical core of the paradox.
$\checkmark$

**35.** *(Strategy: complement and independence for (a); monotone continuity for (b).)*

(a) The trials are independent, so the event "no success in the first $n$ trials" is the intersection of
$n$ independent events each of probability $1-p$:
$$\Pr(\text{no success in first }n)=(1-p)^n.$$

(b) Let $E_n$ = "at least one success in the first $n$ trials". Then
$E_1\subseteq E_2\subseteq\cdots$, and $\bigcup_nE_n$ is "at least one success eventually". By (a),
$\Pr(E_n)=1-(1-p)^n$. Since $p\in(0,1]$, we have $0\le1-p<1$, so $(1-p)^n\to0$ and
$\Pr(E_n)\to1$. Theorem 7.9 (continuity from below) gives
$$\Pr(\text{at least one success eventually})=\lim_{n\to\infty}\Pr(E_n)=1.$$

*Check by a direct series.* The event "first success at trial $k$" has probability $(1-p)^{k-1}p$, and
these events are disjoint with union "some success eventually". Their probabilities sum to a geometric
series:
$$\sum_{k\ge1}(1-p)^{k-1}p=p\cdot\frac{1}{1-(1-p)}=1,$$
in agreement with the continuity argument. For $p=1$ the first trial succeeds with probability $1$ and the
formula is immediate. $\checkmark$

**36.** *(Strategy: condition on the three equally likely pardons and compute the probability of the
guard's answer under each.)*

Let $P_A,P_B,P_C$ be the events that A, B, C are pardoned, each with probability $\tfrac13$. Let $N_B$ be
the event that the guard names B. The guard names one of the two prisoners *other than A* who will be
executed, and chooses uniformly when both are to be executed (so when A is pardoned).

* If $P_A$: both B and C are executed, and the guard names B with probability $\tfrac12$.
* If $P_B$: B is pardoned, so the guard cannot name B; he names C.
* If $P_C$: B is executed and C pardoned, so the guard must name B.

Hence
$$\Pr(N_B)=\frac13\cdot\frac12+\frac13\cdot0+\frac13\cdot1=\frac16+\frac13=\frac12,$$
and
$$\Pr(P_A\mid N_B)=\frac{1/6}{1/2}=\frac13,\qquad \Pr(P_C\mid N_B)=\frac{1/3}{1/2}=\frac23.$$

*Check.* The posteriors over $\{P_A,P_B,P_C\}$ given $N_B$ are $\tfrac13,0,\tfrac23$, summing to $1$: B
cannot be pardoned once the guard has named him as one who will be executed. A's probability is unchanged
at $\tfrac13$, while C's has doubled. $\checkmark$

*Why the answer is not $\tfrac12$.* A's probability would be $\tfrac12$ if the guard had chosen a name
uniformly from the two prisoners other than A *regardless of the outcome*, but he is constrained to name
someone who will be executed. The constraint makes the answer informative: when C is pardoned the guard is
forced to name B, whereas when A is pardoned he names B only half the time. So the naming of B is evidence
for C, not for A.



