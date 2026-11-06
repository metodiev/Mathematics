# Computability and Decidability — Solutions

> [Computability and Decidability](README.md) · Solutions to [exercises.md](exercises.md) · 36 problems

Every solution states the strategy, then carries out the steps. Theorem numbers refer to
[README.md](README.md); Exercise numbers to [exercises.md](exercises.md).

## Beginner

**1.** **Strategy.** Match each set against the definitions, using one theorem per item.

(a) **Decidable.** The division algorithm decides $\{\langle n,k\rangle : k \mid n\}$: compute $n = qk + r$ with $0 \le r < k$ and test $r = 0$. (Convention for $k = 0$: $0 \mid 0$ is true and $0 \nmid n$ for $n \ne 0$; in either convention the answer is a finite computation.)

(b) **Decidable.** Simulate $M$ on $\varepsilon$ for exactly $10$ steps and inspect the result. The bound makes the simulation finite even if $M$ never halts.

(c) $K$ is **c.e. but not decidable**: Theorem 7.11 and Theorem 7.12.

(d) **Decidable.** Test divisibility by all integers from $2$ to $\sqrt n$.

(e) $\{e : W_e = \mathbb{N}\}$ is **neither**. It is an index set (it depends only on $\varphi_e$) and nontrivial, so it is undecidable by Rice (Theorem 7.26). It is not c.e.: the reduction $e \mapsto$ index of the program "on input $x$, run $\varphi_e(0),\dots,\varphi_e(x)$ each for $x$ steps and halt if all halt" gives $\mathrm{TOT} \le_m \{e : W_e = \mathbb{N}\}$, and TOT is not c.e. (Example 9.7). (Equivalently, it is $\Pi^0_2$-complete by Theorem 7.51.)

**2.** **Strategy.** Each $1$ cycles the state $p_0 \to p_1 \to p_2 \to p_0$; $0$s do not change the state; a blank always leads to $p_{\mathrm{acc}}$.

Traces (the head moves right at every step, so the tape is unchanged):

| input | states visited | final transition |
|---|---|---|
| $\varepsilon$ | $p_0$ | $\delta(p_0,\sqcup) = (p_{\mathrm{acc}},\sqcup,R)$ |
| $1$ | $p_0, p_1$ | $\delta(p_1,\sqcup) = (p_{\mathrm{acc}},\sqcup,R)$ |
| $111$ | $p_0,p_1,p_2,p_0$ | accept from $p_0$ |
| $11111$ | $p_0,p_1,p_2,p_0,p_1,p_2$ | accept from $p_2$ |

**Answer.** The machine halts and accepts on *every* input, including the empty one, so $L(M) = \{0,1\}^*$. The state on arrival at the blank is $p_r$ where $r \equiv \lvert w\rvert_1 \pmod 3$: the machine counts the number of $1$s modulo $3$ and then discards the count. It never enters $p_{\mathrm{rej}}$, and it halts on every input because the head moves right at every step and so reaches a blank after $\lvert w\rvert + 1$ steps.

**3.** **Strategy.** Two states record whether $0$ or $1$ ones have been seen; the second $1$ accepts. States $\{q_0,q_1,q_{\mathrm{acc}},q_{\mathrm{rej}}\}$, tape alphabet $\{0,1,\sqcup\}$, start $q_0$.

| state | $0$ | $1$ | $\sqcup$ |
|---|---|---|---|
| $q_0$ | $(q_0,0,R)$ | $(q_1,1,R)$ | $(q_{\mathrm{rej}},\sqcup,R)$ |
| $q_1$ | $(q_1,0,R)$ | $(q_{\mathrm{acc}},1,R)$ | $(q_{\mathrm{rej}},\sqcup,R)$ |

**Correctness.** After $k$ steps the machine is in $q_j$, where $j = \min(2, \text{number of } 1\text{s among the first } k \text{ symbols})$. This is true initially ($k=0$, $j=0$); a $0$ leaves $j$ unchanged and a $1$ increases $\min(2,\cdot)$, exactly as the table prescribes. The head moves right at every step, so the machine reaches the blank after $\lvert w\rvert$ steps and halts: accepting if the state is $q_{\mathrm{acc}}$ (at least two $1$s), rejecting otherwise. Hence the machine halts on every input and accepts exactly $L$.

**4.** **Strategy.** A finite language has a finite list of members; compare the input with each member in turn.

Let $L = \{w_1,\dots,w_k\} \subseteq \Sigma^*$. If $k = 0$ the machine that immediately rejects decides $L$. Otherwise, let $N = \max_i \lvert w_i\rvert$. The machine first scans right for $N+1$ cells; if it finds a non-blank symbol beyond position $N$, it rejects (the input is too long to be in $L$). Otherwise the input is one of the finitely many strings of length $\le N$, and the machine compares it with $w_1$, then $w_2$, …, using a fixed finite table of states for each comparison; it accepts if all comparisons succeed for some $w_i$ and rejects after the last one fails.

**Correctness.** If $w \in L$ then $\lvert w\rvert \le N$ and the comparison with $w = w_i$ succeeds, so the machine accepts. If $w \notin L$ then either $\lvert w\rvert > N$ (rejected in the first phase) or every comparison fails (rejected at the end). The machine halts after finitely many steps in every case. Hence $L$ is decidable.

*Remark.* The argument is uniform in the list but not in the language: the table depends on the particular finite set, which is why "every finite language is decidable" does not give a single algorithm deciding all finite languages (there are countably many finite languages but the uniform question "is $w$ in the finite set coded by $e$" is just membership in $W_e$, which is undecidable).

**5.** **Strategy.** Cross off one symbol in each of the three blocks per round, always the leftmost remaining one, then verify that everything has been crossed off.

Use the tape alphabet $\{0,1,X,Y,Z,\sqcup\}$, where $X$ marks a crossed-off $0$ of the first block, $Y$ a crossed-off $1$, and $Z$ a crossed-off $0$ of the last block.

*One round.* From the left end, skip the $X$s, cross off the leftmost remaining $0$ as $X$ (if the next symbol is $Y$ or $\sqcup$, all first-block $0$s are gone: go to verification). Scan right through the remaining $0$s and then through crossed-off $Y$s; cross off the leftmost remaining $1$ as $Y$ (if a $Z$ or $\sqcup$ appears first, reject). Scan right through the remaining $1$s and crossed-off $Z$s; cross off the leftmost remaining $0$ as $Z$ (if $\sqcup$ appears first, reject). Return to the left end.

*Verification.* Skip all $X$s, then all $Y$s, then all $Z$s; accept on a blank and reject on any remaining $0$ or $1$.

**Termination.** Each round either crosses off exactly three symbols or halts, and each sweep traverses a finite portion of the tape, so a round takes finitely many steps. There are $n + m + p$ non-blank symbols, so at most $\min(n,m,p) + 1$ rounds occur. Hence the machine halts on every input.

**Correctness.** After $k$ completed rounds the tape reads $X^k 0^{n-k} Y^k 1^{m-k} Z^k 0^{p-k}$, provided no rejection has occurred; this is an induction on $k$, since each round crosses off the leftmost remaining symbol of each block. Verification is reached only when the first block is exhausted, i.e. $k = n$. It accepts exactly when the remaining blocks are empty, i.e. $m = k$ and $p = k$. Hence the machine accepts exactly when $n = m = p \ge 1$, as required.

**6.** **Strategy.** Run the deciders one after the other and combine their answers.

Let $D_A$ and $D_B$ be machines deciding $A$ and $B$. Both halt on every input by hypothesis.

*For $A \cup B$:* on input $w$, run $D_A$ on $w$; if it accepts, accept. Otherwise run $D_B$ on $w$ and accept iff it accepts. The machine halts because both simulations halt. It accepts iff $w \in A$ or $w \in B$.

*For $A \cap B$:* on input $w$, run $D_A(w)$; if it rejects, reject. Otherwise run $D_B(w)$ and return its answer. It accepts iff $w \in A$ and $w \in B$.

Both constructions are effective (they use only the descriptions of $D_A$ and $D_B$), so $A \cup B$ and $A \cap B$ are decidable. Note that *sequential* running is legitimate here precisely because deciders always halt; for recognisers it is not, which is why Theorem 7.8(2) uses dovetailing.

**7.** **Strategy.** Dynamic programming over prefixes: record which prefix lengths can be decomposed into words of $A$.

Let $w = a_1a_2\cdots a_n$ with $n \ge 0$. Define $S_0 := \{0\}$ and, for $i \ge 0$,
$$S_{i+1} := S_i \cup \{\, j : \text{there is } i' \in S_i \text{ with } i' < j \le n \text{ and } a_{i'+1}\cdots a_j \in A \,\}.$$
Each $S_i$ is a finite subset of $\{0,1,\dots,n\}$. Since $A$ is decidable and there are finitely many pairs $(i',j)$, each $S_{i+1}$ is computable from $S_i$; a machine can compute the sequence $S_0,S_1,\dots,S_n$ step by step and then test whether $n \in S_n$.

**Correctness.** By induction on $i$, $j \in S_i$ if and only if the prefix $a_1\cdots a_j$ is a concatenation of at most $i$ words of $A$ (where "at most $0$" means $j = 0$). The induction step is the displayed recurrence. Since $w$ has length $n$, any decomposition uses at most $n$ nonempty words, so $w \in A^*$ iff $n \in S_n$. Hence $A^*$ is decidable.

*Remark.* The same argument shows that $A^*$ is c.e. when $A$ is c.e., but *not* by this recurrence: with a recogniser for $A$, a negative answer never terminates, and indeed $A^*$ may fail to be decidable (take $A = K$ with a padding symbol).

**8.** **Strategy.** Imitate Machine C of Example 9.2.

Tape alphabet $\{0,1,\sqcup\}$, states $\{p_0,p_1,p_{\mathrm{acc}},p_{\mathrm{rej}}\}$ with
$$\delta(p_0,0) = (p_0,0,R),\quad \delta(p_0,1) = (p_{\mathrm{acc}},1,R),\quad \delta(p_0,\sqcup) = (p_1,\sqcup,L),$$
$$\delta(p_1,0) = (p_1,0,L),\quad \delta(p_1,1) = (p_1,1,L),\quad \delta(p_1,\sqcup) = (p_1,\sqcup,R).$$

On an input containing a $1$ the machine scans right until it finds one and accepts. On an input $0^n$ it reaches the blank in state $p_0$, moves left to $p_1$, and then oscillates forever between the blank at the left end and the first cell of the tape (in state $p_1$ it always moves left on a symbol, and right on the blank). Hence it halts on exactly the strings containing a $1$ and accepts exactly those. So it recognises $L$.

It does not decide $L$: the inputs $0^n$ are outside $L$, and the machine does not halt on them, so it fails the requirement of Definition 5.6 that a decider halt on every input.

**9.** **Strategy.** Use the universal machine.

By Theorem 7.5 the universal machine $\mathcal{U}$ on input $\langle e, 0\rangle$ halts and accepts exactly when $\varphi_e(0)\!\downarrow$, i.e. exactly when $0 \in W_e$. Hence $\mathcal{U}$ recognises $\{e : 0 \in W_e\}$, which is therefore c.e. $\blacksquare$

**10.** **Strategy.** Decide a syntactic property of the description.

A machine description is a finite string listing states, alphabets, transitions, and start and halting states. The predicates "is a well-formed machine description", "has at most $5$ states" and "has exactly $k$ states" are decidable by inspecting the string. Hence the deciding machine reads the description, parses it, counts the states and answers accordingly. (If the input is not a well-formed description, it rejects.) $\blacksquare$

*Contrast.* The same question with "states" replaced by "runs in at most $10^{10}$ steps on every input" is not decidable, and "computes a total function" is not decidable (Exercise 18); the first is not an index set, the second is.

**11.** **Strategy.** A bounded simulation is finite.

Simulate $M$ on input $0$ for at most $2^{100}$ steps. If $M$ has halted by then, answer accordingly; if not, reject. The simulation performs a fixed finite number of steps, so the procedure always terminates. Decidability is a statement about existence of a terminating procedure, not about feasibility: $2^{100}$ steps is beyond any physical computer, but it is a finite bound.

*Remark.* Replacing $2^{100}$ by "any finite number of steps" destroys decidability: this is exactly the halting problem.

**12.** **Strategy.** Unwind the definition of many-one reduction to the constant set $\{0\}$.

($\Rightarrow$) If $A$ is decidable, define $f(n) = 0$ for $n \in A$ and $f(n) = 1$ for $n \notin A$. Then $f$ is total computable and $n \in A \iff f(n) \in \{0\}$.

($\Leftarrow$) If $A \le_m \{0\}$ via $f$, then for every $n$,
$$n \in A \iff f(n) = 0,$$
and the right-hand side is decidable because $f$ is total computable. Hence $A$ is decidable. $\blacksquare$

*Remark.* The same argument shows $A \le_m \varnothing$ iff $A = \varnothing$, and $A \le_m \Sigma^*$ iff $A = \Sigma^*$; so the trivial sets are m-degrees of their own, both equal to $\mathbf{0}$ (they are computable).

## Intermediate

**13.** **Strategy.** Reduce in both directions using the "ignore the input" gadget.

Write $A := \{e : \varphi_e(0)\!\downarrow\}$.

*$A \le_m K$.* Let $f(e)$ be an index of the program "on input $y$: ignore $y$ and run $M_e$ on $0$; halt iff that halts". Then
$$\varphi_{f(e)}(y)\!\downarrow \iff \varphi_e(0)\!\downarrow \quad \text{for every } y,$$
so in particular $\varphi_{f(e)}(f(e))\!\downarrow \iff \varphi_e(0)\!\downarrow$, i.e. $f(e) \in K \iff e \in A$. The map $f$ is total computable by the s-m-n theorem.

*$K \le_m A$.* Let $g(e)$ be an index of the program "on input $y$: ignore $y$ and run $M_e$ on $e$; halt iff that halts". Then $\varphi_{g(e)}(0)\!\downarrow \iff \varphi_e(e)\!\downarrow$, i.e. $g(e) \in A \iff e \in K$. Again $g$ is total computable.

Hence $A \equiv_m K$. $\blacksquare$

*Remark.* Both reductions have the same shape; the only difference is which of the two arguments is fixed. This is the "constant function" gadget, and it is the most-used tool in the subject.

**14.** **Strategy.** Build a program whose enumeration stops exactly when $\varphi_e(e)$ halts, so that its domain is an initial segment.

Define $f(e)$ to be an index of the following program $P_e$:

> for $y = 0,1,2,\dots$: simulate $M_e$ on $e$ for $y$ steps; if the simulation has halted by then, stop; otherwise enumerate $y$ into the output and continue.

Then
$$W_{f(e)} = \{\, y : M_e(e) \text{ has not halted within } y \text{ steps} \,\}.$$
If $e \in K$, let $s$ be the number of steps after which $M_e(e)$ halts; then $W_{f(e)} = \{0,1,\dots,s-1\}$, a finite set. If $e \notin K$, then no simulation ever halts and $W_{f(e)} = \mathbb{N}$, which is infinite. Hence
$$e \in K \iff f(e) \in \mathrm{Fin} = \{e : W_e \text{ finite}\}.$$
The map $f$ is total computable by the s-m-n theorem, so $K \le_m \mathrm{Fin}$ and Fin is undecidable. $\blacksquare$

**15.** **Strategy.** Two proofs: a reduction, and an application of Rice.

*Reduction.* Let $f(e)$ be an index of the program "on input $y$: ignore $y$; run $M_e$ on $e$; halt when it halts". Then
$$W_{f(e)} = \begin{cases} \mathbb{N} & e \in K,\\ \varnothing & e \notin K,\end{cases}$$
so $e \in K \iff f(e) \in \{e : W_e = \mathbb{N}\}$. The map $f$ is total computable, and $K$ is undecidable, so the set is undecidable.

*Rice.* The set is an index set: if $\varphi_e = \varphi_{e'}$ then $W_e = W_{e'}$. It is nontrivial: the constant-zero function has domain $\mathbb{N}$, while the function defined only at $0$ has domain $\{0\}$. By Theorem 7.26 it is undecidable. $\blacksquare$

*Remark.* The two proofs give different information. The reduction exhibits the exact gadget that encodes $K$; Rice's theorem certifies that no smarter encoding could ever make the problem decidable.

**16.** **Strategy.** An increasing enumeration is a decision procedure; conversely, a decidable infinite set can be enumerated in increasing order by scanning.

($\Leftarrow$) Let $A$ be the range of a strictly increasing total computable $f$. Given $n$, compute $f(0), f(1), f(2), \dots$ until a value $> n$ appears; this happens after finitely many steps because $f$ is strictly increasing and therefore unbounded. Let $k$ be the last index computed. Then $n \in A$ iff $n = f(i)$ for some $i \le k$, which is a finite test. Hence $A$ is decidable.

($\Rightarrow$) Let $A$ be infinite and decidable. Define $f(k)$ to be the $k$-th smallest element of $A$: compute it by scanning $n = 0,1,2,\dots$, testing membership with the decider, and stopping when the counter reaches $k$. This terminates for every $k$ because $A$ is infinite, and the resulting function is total computable, strictly increasing, and has range $A$. $\blacksquare$

*Remark.* Exercise 36 uses the same idea to extract an infinite decidable subset from any infinite c.e. set, where a monotone enumeration of *all* of $A$ is not available.

**17.** **Strategy.** Encode the question "$e \in K$" as a question about inclusion of two c.e. sets, using a set that is either $\{0\}$ or $\mathbb{N}$.

Define total computable functions $u, v$ by:
$$W_{u(e)} = \begin{cases} \{0\} & e \in K,\\ \mathbb{N} & e \notin K,\end{cases} \qquad W_{v(e)} = \{0\}.$$
Concretely, $u(e)$ is an index of the program "on input $y$: if $y = 0$ then halt; else run $M_e$ on $e$ and halt when it does", and $v(e)$ is an index of the program "on input $y$: halt iff $y = 0$".

Then:
* if $e \in K$, $W_{u(e)} = \{0\} \subseteq W_{v(e)}$;
* if $e \notin K$, $W_{u(e)} = \mathbb{N} \not\subseteq \{0\}$.

Hence $e \in K \iff W_{u(e)} \subseteq W_{v(e)} \iff \langle u(e), v(e)\rangle$ lies in the set. The map $e \mapsto \langle u(e), v(e)\rangle$ is total computable, so $K$ reduces to $\{\langle e_1,e_2\rangle : W_{e_1}\subseteq W_{e_2}\}$, which is therefore undecidable. $\blacksquare$

*Remark.* The set is not an index set in a single variable, so Rice's theorem does not apply directly; but the same idea works — a nontrivial property of a pair of c.e. sets is undecidable whenever it can be "switched" by an encoding of $K$.

**18.** **Strategy.** Rice's theorem.

Let $P = \{e : \varphi_e \text{ injective}\}$. If $\varphi_e = \varphi_{e'}$ then $\varphi_e$ is injective iff $\varphi_{e'}$ is, so $P$ is an index set. It is nontrivial: the identity function (index of $x \mapsto x$) is injective, and the constant-zero function is not. By Theorem 7.26, $P$ is undecidable. $\blacksquare$

*Remark.* The same proof applies to "$\varphi_e$ is surjective", "$\varphi_e$ is strictly increasing", "$\varphi_e$ has finite range", and any other nontrivial property of the function.

**19.** **Strategy.** Rice's theorem.

$\{e : \lvert W_e\rvert = 3\}$ is an index set, since $W_e$ is determined by $\varphi_e$. It is nontrivial: the function defined exactly on $\{0,1,2\}$ has $W_e = \{0,1,2\}$ of size $3$, while the identity has infinite domain. By Theorem 7.26, the set is undecidable. $\blacksquare$

*Remark.* Do not try to decide this by "running the machine and counting": a machine with a domain of size $3$ may take arbitrarily long to reveal its third element, and a machine with infinite domain will never reveal that fact.

**20.** **Strategy.** Unwind the definitions and use composition of computable functions.

*Transitivity.* Let $A \le_m B$ via $f$ and $B \le_m C$ via $g$. Then $g \circ f$ is total computable (composition of total computable functions is total computable) and
$$x \in A \iff f(x) \in B \iff g(f(x)) \in C,$$
so $A \le_m C$ via $g\circ f$.

*Complements.* Let $A \le_m B$ via $f$. Then for every $x$,
$$x \in \overline A \iff x \notin A \iff f(x) \notin B \iff f(x) \in \overline B,$$
so the same $f$ is a reduction $\overline A \le_m \overline B$.

*Deduction.* If $A \equiv_m B$, apply the second part to both reductions: $\overline A \le_m \overline B$ and $\overline B \le_m \overline A$, i.e. $\overline A \equiv_m \overline B$. $\blacksquare$

*Caution.* The complement of a *Turing* reduction is also a Turing reduction (negate the answer), but the complement operation does not preserve $\le_T$ in the naive way: $A \le_T B$ always implies $\overline A \le_T B$, so there is nothing to prove. The many-one statement above is the one that requires the same function.

**21.** **Strategy.** Rice's theorem twice, then a conceptual remark.

*Fin.* Let $\mathrm{Fin} = \{e : W_e \text{ finite}\}$. It is an index set, since $W_e$ depends only on $\varphi_e$. It is nontrivial: the empty function has finite domain, the identity has infinite domain. By Theorem 7.26, Fin is undecidable.

*Decidability of $W_e$.* Let $P = \{e : W_e \text{ decidable}\}$. It is an index set. It is nontrivial: the empty set is decidable, and $K$ is not (Theorem 7.12); take $e$ with $W_e = K$ — such an $e$ exists because $K$ is c.e. By Rice, $P$ is undecidable.

*Why no contradiction.* Rice's theorem asserts the nonexistence of a *uniform* procedure that answers the question for every $e$. It does not assert that any particular instance is hard: for a fixed $e$, the question "is $W_e$ finite" has a definite answer, and for many concrete $e$ the answer is provable. What fails is a single algorithm that handles all indices. $\blacksquare$

**22.** **Strategy.** Identify an index set and apply Rice; then compare with the syntactic case.

Let $P = \{e : \varphi_e \text{ is defined on every } w \text{ with } \lvert w\rvert \le 10\}$. If $\varphi_e = \varphi_{e'}$ then $\varphi_e$ has this property iff $\varphi_{e'}$ does, because the property depends only on the domain of the function, restricted to a fixed finite set of inputs. So $P$ is an index set. It is nontrivial: the identity function is defined everywhere (so it qualifies), and the function defined only on strings of length $11$ does not. By Theorem 7.26, $P$ is undecidable.

*Why the finiteness of the input set is irrelevant.* There are only finitely many strings of length $\le 10$, and for each *machine* $M_e$ the question "does $M_e$ halt on $w$" is a halting question. But $P$ quantifies over all machines realising the same function: the same $\varphi_e$ has indices that halt quickly, indices that halt slowly, and indices that loop before halting. A procedure deciding $P$ would have to see through the encoding of the program, which is exactly what Rice's theorem forbids.

*Contrast with Example 9.5(d).* There the condition was "halts on input $0$ within $100$ steps", a property of the *program's run*, not of the function; it is decidable by simulation and is not an index set. The difference is not the size of the input set but whether the condition is extensional. $\blacksquare$

## Advanced

**23.** **Strategy.** Hardwire the first argument into the program, and check that the hardwiring is uniform and total.

Let $\psi : \mathbb{N}^2 \rightharpoonup \mathbb{N}$ be partial computable. By definition there is a Turing machine $P$ computing $\psi$: on input $\langle x, y\rangle$ it halts with output $\psi(x,y)$ when that is defined and diverges otherwise.

For each $x \in \mathbb{N}$ define a machine $P_x$ as follows. On input $y$: write $x$ in a reserved block of the tape (a block that $P$'s simulation will not touch), move the head back to the beginning of the input $y$, and run $P$ on the pair $\langle x, y\rangle$ encoded in the tape layout that $P$ expects. Then
$$\varphi_{s(x)}(y) = \psi(x,y) \quad \text{for all } x,y, \qquad \text{where } s(x) := \langle P_x\rangle.$$

*Where the hypotheses are used.*

* $\psi$ **partial computable**: this is what produces $P$. Without it there is no program to hardwire.
* **Effectiveness**: the map $x \mapsto \langle P_x\rangle$ must be computable. It is: the only part of $P_x$ that depends on $x$ is the finitely many instructions writing the digits of $x$, and those are generated mechanically from $x$.
* **Totality of $s$**: $P_x$ is defined for every $x$, including $x = 0$ and $x$ requiring no digits. So $s$ is total. (Totality of $s$ is essential in the recursion theorem, where $s$ is composed with other total functions.)
* **$s$ need not be injective** in this formulation. The padding lemma (Lemma 7.7) supplies an injective variant when one is needed, for instance in Corollary 7.22(1).

The general $s^m_n$ version is obtained by the same construction with $m$ hardwired arguments and $n$ remaining ones. $\blacksquare$

**24.** **Strategy.** Reduce $K$ to the given index set; separate the two cases according to whether the empty function lies in the class.

Let $\mathcal{C}$ be a nontrivial class of partial computable functions and $P = \{e : \varphi_e \in \mathcal{C}\}$. Choose $g \in \mathcal{C}$ (possible because $\mathcal{C} \ne \varnothing$); since $\mathcal{C}$ is not the class of all partial computable functions, there is also $h \notin \mathcal{C}$. Note that $g \ne h$, so at least one of them is not the empty function.

**Case 1: the empty function $\varnothing \notin \mathcal{C}$.** Then $g \ne \varnothing$. Define $F(e)$ to be an index of the program

> on input $y$: run $M_e$ on $e$; if that halts, run the fixed program for $g$ on $y$ and output its result; if it does not halt, diverge.

This program is built uniformly from $e$ (s-m-n), so $F$ is total computable. If $e \in K$ then the first simulation halts, so $\varphi_{F(e)} = g \in \mathcal{C}$. If $e \notin K$ then the first simulation never halts, so $\varphi_{F(e)} = \varnothing \notin \mathcal{C}$. Therefore
$$e \in K \iff F(e) \in P,$$
so $K \le_m P$ and $P$ is undecidable.

**Case 2: $\varnothing \in \mathcal{C}$.** Then $h \ne \varnothing$ and $h \notin \mathcal{C}$. Define $F(e)$ to be an index of the program

> on input $y$: run $M_e$ on $e$; if that halts, run the fixed program for $h$ on $y$; if it does not halt, diverge.

The same analysis gives $\varphi_{F(e)} = h \notin \mathcal{C}$ when $e \in K$, and $\varphi_{F(e)} = \varnothing \in \mathcal{C}$ when $e \notin K$. Hence
$$e \in K \iff F(e) \notin P,$$
so $K \le_m \overline P$. If $P$ were decidable then $\overline P$ would be decidable, and then $K$ would be decidable, a contradiction. Hence $P$ is undecidable.

**Both cases together** cover every nontrivial $\mathcal{C}$, so every nontrivial index set is undecidable. $\blacksquare$

*Second approach (recursion theorem).* Suppose $P$ decidable with decider $D$. Define a total computable $t$ by: $t(e) = $ an index of $h$ if $D$ accepts $e$, and an index of $g$ if $D$ rejects $e$. By Theorem 7.21 there is $e$ with $\varphi_e = \varphi_{t(e)}$. If $e \in P$ then $\varphi_e \in \mathcal{C}$, but $\varphi_{t(e)} = h \notin \mathcal{C}$ and $\varphi_e = \varphi_{t(e)}$, contradiction; if $e \notin P$ then $\varphi_e \notin \mathcal{C}$ but $\varphi_{t(e)} = g \in \mathcal{C}$, again a contradiction. This proof is shorter and unifies the two cases, at the cost of a heavier tool.

**25.** **Strategy.** Diagonalise against the hypothetical enumeration of $\overline K$.

Suppose, for contradiction, that $\overline K = W_j$ for some $j$. Then for every $e$,
$$\varphi_e(e)\!\uparrow \iff e \in \overline K \iff e \in W_j \iff \varphi_j(e)\!\downarrow. \tag{$*$}$$
Apply $(*)$ with $e = j$:
$$\varphi_j(j)\!\uparrow \iff \varphi_j(j)\!\downarrow,$$
which is impossible: exactly one of the two alternatives holds, so one side of the equivalence is true and the other false. Hence no such $j$ exists and $\overline K$ is not c.e. $\blacksquare$

*Remark.* The proof uses only the definition of $W_j$ as the domain of $\varphi_j$; Theorem 7.8(4) is not needed. The same diagonalisation shows that no set that "separates" a machine from its own index can be c.e. in a way that contradicts the definition — the pattern recurs in the proof that $A' \not\le_T A$ (Exercise 33).

**26.** **Strategy.** Diagonalise against the alleged enumeration by adding one.

Suppose $g : \mathbb{N}\to\mathbb{N}$ is total computable and $\{\varphi_{g(n)} : n \in \mathbb{N}\}$ is exactly the set of total computable functions. Define
$$h(x) := \varphi_{g(x)}(x) + 1.$$
The function $h$ is total computable: $g$ is total computable, $\varphi_{g(x)}$ is total by hypothesis, and adding one is computable. Hence $h$ is a total computable function, so by hypothesis $h = \varphi_{g(n)}$ for some $n$. Evaluating at $x = n$:
$$\varphi_{g(n)}(n) = h(n) = \varphi_{g(n)}(n) + 1,$$
a contradiction in $\mathbb{N}$. Hence no such $g$ exists. $\blacksquare$

*Remark.* This is Cantor's diagonal argument transplanted to an effective setting: the "table" is the matrix $(\varphi_{g(i)}(j))_{i,j}$ and $h$ is the diagonal plus one. The argument also shows that the set of indices of total functions is not the range of any total computable function, which is consistent with that set being $\Pi^0_2$-complete (Theorem 7.51).

**27.** **Strategy.** Apply the recursion theorem to a padded version of $t$, so that the fixed point can be forced to be large.

Let $p$ be the padding function of Lemma 7.7: $\varphi_{p(e,n)} = \varphi_e$ for all $e,n$, the map $(e,n)\mapsto p(e,n)$ is total computable and injective in its second argument, and we may take $p(e,n) > n$ (add $n$ dummy steps to the program coded by $e$).

Fix $n \in \mathbb{N}$ and define
$$t_n(e) := t\bigl(p(e,n)\bigr).$$
This is total computable, so by Theorem 7.21 there is $e_n$ with $\varphi_{e_n} = \varphi_{t_n(e_n)}$. Then
$$\varphi_{p(e_n,n)} = \varphi_{e_n} = \varphi_{t_n(e_n)} = \varphi_{t(p(e_n,n))},$$
so $p(e_n,n)$ is a fixed point of $t$. Since $p(e_n,n) > n$, the fixed point exceeds $n$.

As $n$ was arbitrary, $t$ has a fixed point larger than every prescribed bound, hence infinitely many fixed points. $\blacksquare$

*Remark.* Applying Theorem 7.21 directly to $t$ gives one fixed point; the padding is what converts existence into infinitude. Note that "fixed point" means $\varphi_e = \varphi_{t(e)}$, not $e = t(e)$: the numerical equation is neither expected nor true.

**28.** **Strategy.** Oracle machines can negate answers; the many-one gap comes from c.e.-ness.

*$A \equiv_T \overline A$.* A machine with oracle $A$ decides $\overline A$ by asking the oracle for $A$ and swapping accept/reject; and symmetrically. Both directions are Turing reductions, so $A \equiv_T \overline A$.

*$K \not\equiv_m \overline K$.* Suppose $K \equiv_m \overline K$. Then in particular $\overline K \le_m K$. Since $K$ is c.e. (Theorem 7.11) and $\le_m$ preserves c.e.-ness (Lemma 7.17(5)), $\overline K$ would be c.e. But $K$ is c.e. and undecidable, so $\overline K$ is not c.e. (Corollary 7.13). Contradiction. Hence $K \not\equiv_m \overline K$. $\blacksquare$

*Remark.* This is the standard example separating $\le_T$ from $\le_m$: Turing reducibility is insensitive to complementation, many-one reducibility is not. The same argument shows that no c.e. set is m-equivalent to its complement.

**29.** **Strategy.** C.e.-ness by enumerating proofs; undecidability by reducing $K$ through $\Sigma_1$-completeness.

Let $T = \mathrm{PA}$ and $\operatorname{Thm}(T) = \{\ulcorner\sigma\urcorner : T \vdash \sigma\}$.

*C.e.* Enumerate all strings in order of length; for each, decide whether it codes a proof in $T$ (this is decidable, since the axioms of PA are decidable and the inference rules are mechanical); if it does, output the code of its last line. The range of this procedure is exactly $\operatorname{Thm}(T)$.

*Undecidable.* For each $e$ let $\sigma_e$ be the $\Sigma_1$ sentence expressing "$\varphi_e(e)\!\downarrow$" (Theorem 7.33 and Definition 7.31 give such a sentence, uniformly computable in $e$). Then
$$e \in K \iff \varphi_e(e)\!\downarrow \iff \sigma_e \text{ is true} \iff T \vdash \sigma_e .$$
The second equivalence is the standard-model semantics of a $\Sigma_1$ sentence. The forward direction of the third uses $\Sigma_1$-completeness of $Q \subseteq T$ (Theorem 7.33); the backward direction uses that all axioms of PA are true in $\mathbb{N}$, so every theorem of $T$ is true (soundness). Hence $K \le_m \operatorname{Thm}(T)$ via $e \mapsto \ulcorner\sigma_e\urcorner$, and $\operatorname{Thm}(T)$ is undecidable. $\blacksquare$

*Remark.* The reduction uses soundness, not merely consistency. Rosser's theorem gives undecidability of the theorems for any consistent recursively axiomatised $T \supseteq Q$ by a more delicate argument; see Theorem 7.37.

**30.** **Strategy.** Write the definition with explicit quantifiers and identify the outermost block.

$W_e$ is infinite iff for every $n$ there is an element of $W_e$ greater than $n$:
$$W_e \text{ infinite} \iff \forall n\, \exists x\, \bigl(x > n \ \land\ x \in W_e\bigr).$$
Replace $x \in W_e$ by its defining $\Sigma_1$ form (Theorem 8.2): $x \in W_e \iff \exists s\, T_1(e,x,s)$. Then
$$W_e \text{ infinite} \iff \forall n\, \exists x\, \exists s\, \bigl(x > n \ \land\ T_1(e,x,s)\bigr).$$
The two adjacent existential quantifiers collapse into one, so the formula has the form $\forall\,\exists$ over a primitive recursive (hence computable) matrix: it is $\Pi_2$. Hence $\operatorname{Inf} \in \Pi^0_2$, and $\operatorname{Fin} = \mathbb{N}\setminus\operatorname{Inf} \in \Sigma^0_2$. $\blacksquare$

*Remark.* The order of the quantifiers is the whole content: $\forall n\exists x$ is not the same as $\exists x\forall n$, and the latter (boundedness) is the statement that $W_e$ is finite, which is $\Sigma_2$ rather than $\Pi_2$. Both Fin and Inf are complete at their levels (Theorem 7.51).

**31.** **Strategy.** Recursion theorem: a function equal to its own complement is impossible.

Suppose $f$ is total computable with $W_{f(e)} = \mathbb{N}\setminus W_e$ for all $e$. By Theorem 7.21 applied to $f$, there is $e$ with $\varphi_e = \varphi_{f(e)}$, hence $W_e = W_{f(e)}$. Therefore
$$W_e = \mathbb{N}\setminus W_e.$$
Taking any $x$: $x \in W_e \iff x \in \mathbb{N}\setminus W_e \iff x \notin W_e$, a contradiction. Hence no such $f$ exists. $\blacksquare$

*Remark.* The obstruction is not "computability" but the algebraic fact that no set equals its own complement. The same argument shows that there is no total computable $f$ with $W_{f(e)} = \overline{W_e}$ for all $e$, even if $f$ is allowed to depend on the *index* rather than the set — which is exactly the content of the recursion theorem's fixed points. Note also that a *partial* computable such $f$ cannot exist either, since partiality is not the issue.

## Challenge

**32.** **Strategy.** If $\mathrm{BB}$ were computable, it would give a step bound that decides the halting problem; the domination statement follows by building machines that first simulate the computation of $f(n)$.

*Setup.* Fix a machine model with a binary tape alphabet, one tape and a single halting state, and let $\mathrm{BB}(n)$ be the maximum, over all $n$-state machines that halt on the empty input, of the number of steps performed. The maximum exists because there are finitely many $n$-state machines; if none halts, set $\mathrm{BB}(n) := 0$. The function is nondecreasing.

*Non-computability.* Suppose $\mathrm{BB}$ is computable. We decide $\mathrm{HALT}$ as follows. Given $\langle M, w\rangle$, construct a machine $M'$ that first writes $w$ on the tape and then simulates $M$; if $M$ has $n$ states and $w$ has $k$ symbols, then $M'$ has $n + c(k + 1)$ states for a constant $c$ depending only on the encoding ($c$ states per symbol written, plus a fixed controller). Now simulate $M'$ on the empty input for $\mathrm{BB}(n')$ steps, where $n'$ is the number of states of $M'$. If $M'$ has not halted within that many steps, then $M'$ never halts — because a halting $n'$-state machine halts within $\mathrm{BB}(n')$ steps by definition. So the procedure decides whether $M$ halts on $w$, i.e. decides $\mathrm{HALT}$, contradicting Theorem 7.14. Hence $\mathrm{BB}$ is not computable.

*Domination.* Let $f$ be any total computable function. Fix $n$ and let $N(n)$ be the number of states of a machine that writes $n$ on the empty tape (this is $O(\log n)$ states, since $n$ is written in binary). Let $C$ be a machine computing $f$, with $c$ states. Construct a machine that writes $n$, simulates $C$ on $n$ to obtain $f(n)$, and then performs exactly $f(n)$ additional dummy steps before halting; the dummy phase can be implemented by counting to $f(n)$ and takes at most a constant number of extra states (using the value $f(n)$ already written on the tape as a counter). This machine has at most $c + N(n) + c'$ states and halts after at least $f(n)$ steps on the empty input. Therefore
$$\mathrm{BB}\bigl(c + N(n) + c'\bigr) \ge f(n)$$
for every $n$, i.e. $\mathrm{BB}(n + c'') \ge f(n)$ for a constant $c''$ depending on $f$ but not on $n$. So $\mathrm{BB}$ eventually dominates every total computable function. $\blacksquare$

*Remark.* The domination statement is stronger than non-computability: it says $\mathrm{BB}$ outruns every computable function, so its non-computability is "as strong as possible". Small values illustrate the growth: $\mathrm{BB}(1) = 1$, $\mathrm{BB}(2) = 6$, $\mathrm{BB}(3) = 21$, $\mathrm{BB}(4) = 107$, and $\mathrm{BB}(5) \ge 47{,}176{,}870$; $\mathrm{BB}(6)$ is unknown but enormous. These values depend on the exact conventions of the machine model, so no value above should be quoted without fixing the model.

**33.** **Strategy.** Diagonalise against the alleged oracle computation.

Let $A \subseteq \mathbb{N}$ and let $A' = \{e : \varphi_e^A(e)\!\downarrow\}$, where $\varphi^A_e$ denotes the $e$-th oracle machine run with oracle $A$.

Suppose, for contradiction, that $A' \le_T A$. Then $\overline{A'} \le_T A$ as well, because a Turing reduction can negate its answer. So there is an oracle machine $N$ with oracle $A$ that decides $\overline{A'}$: for every $e$, $N^A(e)$ halts and accepts iff $e \notin A'$, i.e. iff $\varphi_e^A(e)\!\uparrow$.

Let $j$ be an index of $N$. Since $N^A$ is total, $\varphi_j^A(j)$ halts, so $j \in A'$ by definition of $A'$. But by the defining property of $N$, $N^A(j)$ accepts iff $j \notin A'$, i.e. iff $j \in \overline{A'}$. So $j \in A'$ and $j \in \overline{A'}$, a contradiction. Hence $A' \not\le_T A$. $\blacksquare$

*Deduction of strictness.* Iterate: $\emptyset^{(0)} = \emptyset$, $\emptyset^{(n+1)} = (\emptyset^{(n)})'$. The result gives $\emptyset^{(n+1)} \not\le_T \emptyset^{(n)}$ for all $n$. By Post's theorem (Theorem 7.53), $A \in \Delta^0_{n+1}$ iff $A \le_T \emptyset^{(n)}$, so $\emptyset^{(n+1)} \in \Sigma^0_{n+1} \setminus \Delta^0_{n+1}$. Hence $\Sigma^0_{n+1} \ne \Delta^0_{n+1}$, which is the strictness of the hierarchy (Theorem 7.52). $\blacksquare$

*Remark.* The proof is the halting problem relativised: $A'$ is the halting problem "in the world where $A$ is computable", and the argument is the same diagonalisation, carried out relative to an oracle whose answers we never inspect.

**34.** **Strategy.** A complete c.e. consistent theory is decidable; Th(ℕ) is complete and consistent, so it cannot be c.e. without contradicting Rosser.

Let $\mathcal{T} = \operatorname{Th}(\mathbb{N}) = \{\ulcorner\sigma\urcorner : \mathbb{N}\models\sigma\}$.

*Consistency and completeness.* $\mathcal{T}$ is consistent, because $\mathbb{N}$ is a model of it: no sentence and its negation are both true in $\mathbb{N}$. It is complete: for every sentence $\sigma$, either $\mathbb{N} \models \sigma$ or $\mathbb{N} \models \neg\sigma$, so $\sigma \in \mathcal{T}$ or $\neg\sigma \in \mathcal{T}$.

*$\mathcal{T}$ contains $Q$.* Every axiom of $Q$ is true in $\mathbb{N}$ (this is an elementary verification of each of the eight axioms), so $Q \subseteq \mathcal{T}$.

*A complete c.e. theory is decidable.* Let $T$ be consistent, complete and c.e. To decide whether $\sigma \in T$, enumerate theorems of $T$ and simultaneously enumerate theorems of $T$; since $T$ is complete, some finite stage produces either $\sigma$ or $\neg\sigma$ (exactly one of them, by consistency), and the answer is then known. More carefully: enumerate all theorems (which is possible because $T$ is c.e. and closed under consequence, and we may enumerate the c.e. set of theorems directly), and test each against $\sigma$ and $\neg\sigma$.

*Conclusion.* Suppose $\mathcal{T}$ were c.e. Then by the previous paragraph it would be decidable. Being decidable, its set of theorems is c.e.; take as axioms the set $\mathcal{T}$ itself (a decidable, hence c.e., set of sentences): then $\mathcal{T}$ is a recursively axiomatised theory, it is consistent, and it contains $Q$. Moreover it is complete. But Theorem 7.37 (Rosser) says every consistent recursively axiomatised theory containing $Q$ is incomplete. Contradiction. Hence $\mathcal{T}$ is not c.e. $\blacksquare$

*Remark.* This is the semantic counterpart of the first incompleteness theorem: it is not merely that some axiom system misses truths, but that the set of *all* arithmetical truths cannot be effectively enumerated.

**35.** **Strategy.** The second recursion theorem is exactly the negation of a fixed-point-free map.

*No such $f$.* Suppose $f$ is total computable with $\varphi_{f(e)} \ne \varphi_e$ for every $e$. By Theorem 7.21, applied to $f$, there is $e$ with $\varphi_e = \varphi_{f(e)}$, contradicting the hypothesis. Hence no such $f$ exists.

*Equivalence.* Let (RT) be the statement of Theorem 7.21 and (NF) the statement "no total computable $f$ satisfies $\varphi_{f(e)} \ne \varphi_e$ for all $e$".

(RT) $\Rightarrow$ (NF): given total computable $f$, (RT) supplies $e$ with $\varphi_e = \varphi_{f(e)}$, so $f$ is not fixed-point-free.

(NF) $\Rightarrow$ (RT): let $t$ be total computable. If $t$ had no fixed point, then $\varphi_{t(e)} \ne \varphi_e$ for all $e$, so $t$ would be a total computable fixed-point-free map, contradicting (NF). Hence $t$ has a fixed point, which is (RT).

So the two statements are equivalent. $\blacksquare$

*Remark.* (NF) looks like a trivial reformulation, but it is the form in which the recursion theorem is used: it converts "there is a program that behaves like its own transform" into "no program can always differ from its own transform", and the latter is often easier to apply. Note that a *partial* computable fixed-point-free map can exist, because Theorem 7.21 requires totality of $t$ — this is the hypothesis that cannot be dropped.

**36.** **Strategy.** Dovetail a recogniser to enumerate a c.e. set; then thin the enumeration to make it strictly increasing.

*Part 1: c.e. sets are ranges.* Let $A$ be c.e., $A = W_e$, and assume $A \ne \varnothing$; choose $a \in A$. Define $f : \mathbb{N}\to\mathbb{N}$ by: decode the input as a pair $\langle x, s\rangle$; if $x \in W_{e,s}$ (i.e. if the $s$-th stage of the enumeration of $W_e$ has already enumerated $x$), output $x$; otherwise output $a$. The relation $x \in W_{e,s}$ is decidable (one simulates $M_e$ on $x$ for $s$ steps), so $f$ is total computable, and its range is exactly $A$: every $x \in A$ appears at some stage, and every output is either $a$ or an element of $A$. Conversely, the range of a total computable function is c.e. by Definition 5.9. If $A = \varnothing$ there is no total function with range $A$, which is why the statement excludes that case.

*Part 2: thinning.* Let $A$ be infinite and c.e. Enumerate $A$ as $a_0, a_1, a_2, \dots$ by dovetailing a recogniser for $A$ over all inputs (Definition 5.9 and Theorem 7.8). Define $b_0 := a_{s(0)}$ where $s(0)$ is the least index such that $a_{s(0)}$ exists; and recursively, $b_{n+1} := a_{s(n+1)}$ where $s(n+1)$ is the least index $> s(n)$ such that $a_{s(n+1)} > b_n$. Such an index exists because $A$ is infinite, so the enumeration contains elements larger than $b_n$; and it can be found by continuing the enumeration until one appears. Hence the sequence $(b_n)$ is total computable and strictly increasing, and $B := \{b_n : n \in \mathbb{N}\} \subseteq A$ is infinite.

*Part 3: $B$ is decidable.* To decide whether $m \in B$, compute $b_0, b_1, \dots$ until a value $> m$ appears; since $(b_n)$ is strictly increasing and therefore unbounded, this terminates after finitely many steps. Then $m \in B$ iff $m$ equals one of the computed values. This is a decision procedure, so $B$ is decidable. $\blacksquare$

*Remark.* Part 3 also follows from Exercise 16, since $B$ is the range of the strictly increasing total computable function $n \mapsto b_n$. The construction cannot be applied to $A$ itself: producing an increasing enumeration of *all* of $A$ would make $A$ decidable, which is impossible for e.g. $A = K$. The thinning is exactly the point at which information is lost.

