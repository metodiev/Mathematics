# Game Theory — Exercises

> [Game Theory](README.md) · 36 problems · Beginner → Challenge · Solutions: [solutions.md](solutions.md)

Work through the problems in order. Every problem is solvable with the definitions and theorems of the
tutorial, and the section reference says where to look. Attempt each problem in writing before opening
[solutions.md](solutions.md).

**Conventions.** All games are finite. Player 1 is the **row** player and player 2 the **column**
player; a cell $(x,y)$ lists player 1's payoff $x$ and player 2's payoff $y$. A mixed strategy of player
$i$ is written $\sigma_i$, and $\operatorname{supp}\sigma_i$ is the set of pure strategies used with
positive probability. In zero-sum games only player 1's payoff matrix is displayed, player 2 receiving
its negative. For repeated games, $\delta\in[0,1)$ is the discount factor and payoffs are total
discounted sums unless the problem says "average payoff". A subgame-perfect equilibrium is abbreviated
SPE, and a Nash equilibrium NE.

## Beginner

**1.** *(§5.3, §7.3)* In the game below, player 1 chooses $T$ or $B$, player 2 chooses $L$ or $R$.

| | $L$ | $R$ |
|---|---|---|
| $T$ | $(4,3)$ | $(1,1)$ |
| $B$ | $(2,2)$ | $(3,4)$ |

(a) Does either player have a strictly dominant strategy? Explain.
(b) Find every pure-strategy Nash equilibrium by best-response analysis.
(c) Find the mixed-strategy equilibrium and the expected payoff of each player in it.

**2.** *(§7.5)* Two firms choose simultaneously between *Cooperate* $(C)$ and *Defect* $(D)$.

| | $C$ | $D$ |
|---|---|---|
| $C$ | $(2,2)$ | $(0,3)$ |
| $D$ | $(3,0)$ | $(1,1)$ |

(a) Show that $D$ is strictly dominant for both players and find the unique NE.
(b) Compare the NE payoff vector with $(C,C)$ and define the **price of anarchy** as the ratio of the
best symmetric feasible total payoff to the NE total payoff. Compute it.
(c) Is the NE Pareto efficient? Justify.

**3.** *(§7.1)* Carry out iterated elimination of strictly dominated strategies (IESDS) in the game

| | $L$ | $C$ | $R$ |
|---|---|---|---|
| $T$ | $(4,1)$ | $(1,3)$ | $(2,0)$ |
| $M$ | $(3,2)$ | $(1,4)$ | $(1,1)$ |
| $B$ | $(2,0)$ | $(0,2)$ | $(0,1)$ |

(a) Identify a strictly dominated strategy and eliminate it.
(b) In the reduced game, identify a strictly dominated strategy of the other player and eliminate it.
(c) Continue until no strategy can be eliminated, and find every pure NE of the reduced game.
(d) Verify that each NE you found is also a NE of the original game.

**4.** *(§7.4)* In a zero-sum game player 1 has payoff matrix

$$
A=\begin{pmatrix}3&0\\0&1\end{pmatrix}.
$$

(a) Show that there is no pure saddle point.
(b) Find the optimal mixed strategy of each player and the value of the game.
(c) Verify that player 1 guarantees the value and player 2 holds player 1 to it.

**5.** *(§7.4)* In a zero-sum game

$$
A=\begin{pmatrix}2&-1\\-1&1\end{pmatrix}.
$$

(a) Find the value and the optimal mixed strategies.
(b) What is the probability that player 1 plays the first row? Is it greater or smaller than $\tfrac12$,
and why does that make sense?

**6.** *(§5.2, §5.3)* Answer with a proof or a counterexample.

(a) If a player has a strictly dominant strategy, is it necessarily played in every NE?
(b) If a strategy profile is a NE, must each player's strategy be strictly dominant?
(c) Can a game have a NE in which one player uses a weakly dominated strategy? Give an example.

**7.** *(§5.1)* In the game of Exercise 1, player 1 uses $\sigma_1=(0.3,0.7)$ and player 2 uses
$\sigma_2=(0.6,0.4)$.

(a) Compute the probability of each of the four pure profiles.
(b) Compute the expected payoff of each player.
(c) Without solving the game again, explain why the expected payoff of player 1 must lie between the
smallest and largest entries of player 1's payoff matrix.

**8.** *(§7.9)* A single indivisible object is sold by a second-price sealed-bid auction. Three bidders
have private values $50$, $30$ and $20$.

(a) What are the equilibrium bids, the winner, the price and the winner's utility?
(b) What happens if the bidder with value $50$ bids $45$? What if she bids $25$?
(c) Explain in one sentence why bidding above one's value can only hurt.

**9.** *(§7.8)* A two-player cooperative game has $v(\{1\})=2$, $v(\{2\})=1$ and $v(\{1,2\})=5$.

(a) Compute the Shapley value by averaging marginal contributions over the two orderings.
(b) Verify efficiency.
(c) Is the Shapley value in the core? (The core consists of allocations $(x_1,x_2)$ with
$x_1+x_2=v(\{1,2\})$, $x_1\ge v(\{1\})$ and $x_2\ge v(\{2\})$.)

**10.** *(§7.7)* In a repeated prisoner's dilemma the stage payoffs are $T=4$ (temptation), $R=3$
(reward for mutual cooperation), $P=1$ (punishment) and $S=0$ (sucker).

(a) Derive the condition on $\delta$ under which grim trigger sustains cooperation.
(b) Evaluate the condition numerically and check whether $\delta=0.5$ works.
(c) What happens as $\delta\to1$? Interpret the result.

**11.** *(§7.6)* An entrant $E$ chooses *Out* or *In*. If $E$ stays out, payoffs are $(0,2)$. If $E$
enters, the incumbent $I$ chooses *Fight* or *Accommodate*; payoffs are $(-1,0)$ after Fight and $(1,1)$
after Accommodate, listed as $(E,I)$.

(a) Draw the game tree.
(b) Write the normal form and find every pure NE.
(c) Which NE are subgame perfect? Identify the non-credible threat.

**12.** *(§5.2)* Consider

| | $L$ | $R$ |
|---|---|---|
| $T$ | $(1,1)$ | $(1,0)$ |
| $B$ | $(0,0)$ | $(1,1)$ |

(a) Show that $T$ weakly dominates $B$ but does not strictly dominate it.
(b) Find every pure NE.
(c) Which NE involves a weakly dominated strategy? Why does this not contradict the result that a
strictly dominated strategy is never played in a NE?

## Intermediate

**13.** *(§7.3)* Two firms compete à la Cournot. Inverse demand is $P(Q)=120-Q$ with $Q=q_1+q_2$, and
each firm has constant marginal cost $c=30$ and no fixed cost.

(a) Derive each firm's best-response function.
(b) Find the symmetric Cournot NE: quantities, price and profits.
(c) Compute total surplus and compare it with the monopoly outcome (one firm producing the monopoly
quantity at the same cost).

**14.** *(§7.6)* In the Stackelberg version of Exercise 13, firm 1 chooses $q_1$ first and firm 2
observes it and then chooses $q_2$.

(a) Solve the follower's problem by backward induction.
(b) Solve the leader's problem and find the SPE quantities, price and profits.
(c) Compare with Cournot. Who gains and who loses? Does the leader's ability to commit help or hurt
consumers?

**15.** *(§7.5)* The Battle of the Sexes is

| | Opera | Football |
|---|---|---|
| Opera | $(3,2)$ | $(0,0)$ |
| Football | $(0,0)$ | $(2,3)$ |

(a) Find both pure NE and their payoffs.
(b) Find the mixed NE. Show all steps.
(c) Compute each player's expected payoff in the mixed NE and compare with the pure equilibria.
(d) Which equilibrium would you predict, and on what does the prediction depend?

**16.** *(§7.5)* The Stag Hunt is

| | Stag | Hare |
|---|---|---|
| Stag | $(4,4)$ | $(0,3)$ |
| Hare | $(3,0)$ | $(3,3)$ |

(a) Find the pure NE and the mixed NE.
(b) Define **payoff dominance** and **risk dominance** for two pure equilibria, and determine which
equilibrium has each property. (Use the deviation-loss criterion: the risk-dominant equilibrium is the
one with the larger product of the two players' losses from deviating.)
(c) Explain in words why this game models a problem of trust.

**17.** *(§7.3)* Each of two players chooses $A$, $B$ or $C$. A player receives $2$ if the two choices
agree and $0$ otherwise.

(a) Find the three pure NE.
(b) Show that the uniform mixture $\left(\tfrac13,\tfrac13,\tfrac13\right)$ is a NE and compute its
payoff.
(c) Show that any mixture supported on exactly two strategies with weights $\left(\tfrac12,\tfrac12\right)$
is a NE, and compute its payoff.
(d) Explain why the game has a continuum of equilibria and why the pure ones are the natural
predictions.

**18.** *(§7.3)* Two firms sell an identical product and choose prices simultaneously. Demand at the
lower price is $D(p)=100-p$; at equal prices the firms split demand. Marginal cost is $10$ and there are
no fixed costs.

(a) Show that $p_1=p_2=10$ is a NE.
(b) Show that no profile with $p_1=p_2>10$ is a NE.
(c) Show that no profile with $p_1\ne p_2$ is a NE (consider undercutting by a small amount).
(d) Explain why this "Bertrand paradox" differs sharply from Cournot competition.

**19.** *(§7.7)* In the repeated prisoner's dilemma of Exercise 10, both players use **tit-for-tat**:
cooperate in period $1$, and in every later period copy the opponent's previous action.

(a) Derive the condition on $\delta$ under which cooperation is sustained against a one-shot deviation.
(b) Evaluate it for $T=5$, $R=3$, $P=1$, $S=0$.
(c) Compare with the grim-trigger threshold and explain the difference.

**20.** *(§7.8)* Three players form a majority. A coalition is winning if it contains at least two
players; a winning coalition has value $1$, a losing one value $0$.

(a) Write down $v(S)$ for every coalition.
(b) Compute the Shapley value by listing all six orderings and the marginal contribution of each player.
(c) Interpret the answer.

**21.** *(§7.8)* A weighted majority game has players with weights $(2,1,1)$ and quota $3$: a coalition
is winning if its total weight is at least $3$. Compute the Shapley value and explain why the large
player gets more than twice the value of a small player.

**22.** *(§7.9)* Three risk-neutral bidders have values independently and uniformly distributed on
$[0,1]$ in a symmetric independent-private-values auction.

(a) In a second-price auction, what is the expected revenue?
(b) In a first-price auction with symmetric equilibrium bidding $b(v)=\frac{n-1}{n}v$ for $n=3$, what is
the expected revenue?
(c) Verify revenue equivalence in this example.
(d) Which auction would a risk-averse bidder prefer, and why?

**23.** *(§7.9)* Show that truthful bidding is not an equilibrium of a first-price sealed-bid auction
with two bidders by exhibiting a profitable deviation in the profile in which both bid their values.
Use values $10$ and $8$.

**24.** *(§7.5, §12)* In the Hawk–Dove game a resource is worth $V=4$; two Hawks who meet fight and each
bears injury cost $C=6$ with probability $\tfrac12$, so each gets $(V-C)/2$. A Hawk meeting a Dove gets
$V$, a Dove meeting a Hawk gets $0$, and two Doves split the resource.

(a) Write the payoff matrix.
(b) Find the mixed NE and interpret the mixture as an evolutionarily stable population state.
(c) Compute the equilibrium payoff.
(d) What happens as $C\to V$ from above and as $C\to\infty$?

## Advanced

**25.** *(§7.4)* Prove the **indifference principle**: a mixed strategy $\sigma_i$ is a best response
to $\sigma_{-i}$ if and only if every pure strategy in $\operatorname{supp}\sigma_i$ is a best response
to $\sigma_{-i}$.

**26.** *(§7.4)* Let $u(p,q)=p^{\mathsf T}Aq$ be the payoff of the row player in a finite zero-sum game.

(a) Prove the weak duality inequality
$$\max_{p\in\Delta(S_1)}\min_{q\in\Delta(S_2)}u(p,q)\le \min_{q\in\Delta(S_2)}\max_{p\in\Delta(S_1)}u(p,q).$$
(b) For a $2\times2$ game with no pure saddle point and $D=a-b-c+d\ne0$, verify that the mixed
strategies $p=(p,1-p)$ and $q=(q,1-q)$ with
$$p=\frac{d-c}{D},\qquad q=\frac{d-b}{D}$$
make the opponent indifferent and yield the value $v=(ad-bc)/D$.
(c) Explain why this proves equality of the two sides of (a) in this case.

**27.** *(§7.1)* Prove that a strictly dominated pure strategy is played with probability zero in every
Nash equilibrium (pure or mixed).

**28.** *(§7.9)* Prove that truthful bidding is a weakly dominant strategy in a second-price sealed-bid
auction with private values. Treat all cases for the highest competing bid, including ties, and state
the tie-breaking assumption you use.

**29.** *(§7.8)* Prove that the Shapley value is the unique function on transferable-utility games
satisfying efficiency, symmetry, the dummy axiom and additivity.

**30.** *(§7.7)* Derive the grim-trigger condition for the repeated prisoner's dilemma and show that, if
the condition fails, a player can profitably deviate once and then follow the punishment path.

**31.** *(§7.9)* A single indivisible good is to be allocated to one of $n$ bidders. Each bidder $i$ has
a private value $v_i$ and utility $v_i-p_i$ if she receives the good and $-p_i$ otherwise. The VCG
mechanism allocates the good to a bidder with the highest value and makes the winner pay the highest
value among the other bidders.

(a) Prove that truthful bidding is a weakly dominant strategy.
(b) Prove individual rationality: a truthful bidder's utility is never negative.
(c) Compute the payments and allocation when $v=(12,9,4)$.

## Challenge

**32.** *(§7.3)* Prove Nash's theorem: every finite game in normal form has at least one mixed-strategy
Nash equilibrium. Use Brouwer's fixed-point theorem and the excess-payoff map
$$g_i(s_i;\sigma)=\max\{0,\;u_i(s_i,\sigma_{-i})-u_i(\sigma)\},\qquad
\sigma_i'(s_i)=\frac{\sigma_i(s_i)+g_i(s_i;\sigma)}{1+\sum_{t_i\in S_i}g_i(t_i;\sigma)}.$$
Show that $\sigma'$ is a continuous map of the product of simplices into itself, that a fixed point
exists, and that every fixed point is a NE.

**33.** *(§7.3)* Find every Nash equilibrium of

| | $L$ | $R$ |
|---|---|---|
| $T$ | $(3,1)$ | $(0,0)$ |
| $M$ | $(2,2)$ | $(2,3)$ |
| $B$ | $(1,0)$ | $(5,1)$ |

Use support enumeration: for each pair of supports, solve the indifference equations, then check the
best-response inequalities. State all equilibria and their payoffs.

**34.** *(§7.7)* In a repeated prisoner's dilemma with stage payoffs $T=5$, $R=3$, $P=1$, $S=0$, a public
randomisation device selects $C$ with probability $\tfrac34$ and $D$ with probability $\tfrac14$ at the
start of every period. Both players are instructed to play the device's recommendation while the
history contains no deviation, and to play $D$ forever after any deviation.

(a) Show that the long-run average payoff of the cooperative phase is $(2.5,2.5)$.
(b) Compute the payoff from deviating once, optimally, and the continuation payoff after deviation.
(c) Find the smallest $\delta$ for which this is an SPE.
(d) Does this contradict the folk theorem? Explain.

**35.** *(§7.9)* In a first-price sealed-bid auction there are $n\ge2$ symmetric risk-neutral bidders
with independent private values uniformly distributed on $[0,1]$.

(a) Suppose all rivals bid according to a strictly increasing differentiable function $b(\cdot)$ with
$b(0)=0$. Write the expected payoff of a bidder with value $v$ who bids $b(x)$.
(b) Derive the first-order condition and solve the differential equation for the symmetric equilibrium.
(c) Compute the seller's expected revenue and verify revenue equivalence with the second-price auction.
(d) Show that the equilibrium bid is increasing in $n$ and explain the intuition.

**36.** *(§7.5, §12)* In the Hawk–Dove game with $V<C$, let $x$ be the fraction of Hawks in an infinite
population and suppose individuals are randomly matched. Payoffs are as in Exercise 24.

(a) Write the replicator equation $\dot x=x(1-x)(\bar u_H-\bar u_D)$ explicitly.
(b) Find all rest points in $[0,1]$ and determine their stability.
(c) Show that the interior rest point equals the mixed NE probability of playing Hawk.
(d) Interpret the result biologically and compare with the notion of an evolutionarily stable strategy.
