# Computability and Decidability — Exercises

> [Computability and Decidability](README.md) · 36 problems · Beginner → Challenge · Solutions: [solutions.md](solutions.md)

Attempt every problem in writing before looking at the answers. Problems marked *(proof)* require a
complete argument with every hypothesis stated. Section and theorem numbers refer to
[README.md](README.md).

**Notation.** $\varphi_e$ is the $e$-th partial computable function and $W_e = \operatorname{dom}\varphi_e$
its domain; $K = \{e : \varphi_e(e)\!\downarrow\}$ and $\mathrm{HALT} = \{\langle e,w\rangle : \varphi_e(w)\!\downarrow\}$.
$A \le_m B$ denotes many-one reducibility and $A \le_T B$ Turing reducibility. $M_e$ is the machine with
index $e$, and $\langle \cdot,\cdot\rangle$ is a fixed computable pairing of strings. "Decidable" means
"has a Turing machine that halts on every input with the correct yes/no answer"; "c.e." means
"computably enumerable". $\operatorname{Fin} = \{e : W_e \text{ finite}\}$ and
$\operatorname{Inf} = \{e : W_e \text{ infinite}\}$. A set is *nontrivial* if it is neither
$\varnothing$ nor the whole universe.

## Beginner

**1.** For each set, say whether it is decidable, c.e. but not decidable, or neither, and justify in
one sentence: (a) $\{\langle n,k\rangle : k \text{ divides } n\}$; (b) $\{\langle M\rangle : M \text{ halts on } \varepsilon \text{ within } 10 \text{ steps}\}$;
(c) $K$; (d) the set of primes; (e) $\{e : W_e = \mathbb{N}\}$.

**2.** Consider the machine with states $\{p_0,p_1,p_2,p_{\mathrm{acc}},p_{\mathrm{rej}}\}$, tape alphabet
$\{0,1,\sqcup\}$, start state $p_0$, and transitions
$$\delta(p_0,0) = (p_0,0,R),\ \delta(p_0,1) = (p_1,1,R),\ \delta(p_0,\sqcup) = (p_{\mathrm{acc}},\sqcup,R),$$
$$\delta(p_1,0) = (p_1,0,R),\ \delta(p_1,1) = (p_2,1,R),\ \delta(p_1,\sqcup) = (p_{\mathrm{acc}},\sqcup,R),$$
$$\delta(p_2,0) = (p_2,0,R),\ \delta(p_2,1) = (p_0,1,R),\ \delta(p_2,\sqcup) = (p_{\mathrm{acc}},\sqcup,R).$$
Trace it on $\varepsilon$, on $1$, on $111$ and on $11111$. Which strings does it accept, and what does
the final state record?

**3.** Design a Turing machine over $\Gamma = \{0,1,X,Y,\sqcup\}$ that decides
$L = \{w \in \{0,1\}^* : w \text{ contains at least two } 1\text{s}\}$. Give the full transition table
and a one-paragraph correctness argument.

**4.** *(proof)* Prove that every finite language is decidable, by describing the machine explicitly.

**5.** Describe (in words, not necessarily as a full table) a Turing machine that decides
$L = \{0^n1^n0^n : n \ge 1\}$, and explain why your machine halts on every input.

**6.** *(proof)* Let $A, B \subseteq \Sigma^*$ be decidable. Prove that $A \cup B$ and $A \cap B$ are
decidable by constructing the deciding machines from deciders for $A$ and $B$.

**7.** *(proof)* Let $A \subseteq \Sigma^*$ be decidable. Prove that $A^* = \{w_1w_2\cdots w_k : k \ge 0,\ w_i \in A\}$
is decidable. (The empty string belongs to $A^*$ because $k = 0$ is allowed.)

**8.** Give a machine that *recognises* $L = \{w : w \text{ contains a } 1\}$ but does not decide it, and
explain exactly which inputs distinguish the two notions.

**9.** *(proof)* Prove that $\{e : 0 \in W_e\}$ is c.e.

**10.** *(proof)* Prove that $\{\langle M\rangle : M \text{ has at most } 5 \text{ states}\}$ is decidable.

**11.** Explain why $\{\langle M\rangle : M \text{ halts on input } 0 \text{ within } 2^{100} \text{ steps}\}$ is
decidable, even though $2^{100}$ is astronomically large.

**12.** *(proof)* Prove that $A \le_m \{0\}$ if and only if $A$ is decidable, where $\{0\} \subseteq \mathbb{N}$
and $A \subseteq \mathbb{N}$.

## Intermediate

**13.** *(proof)* Prove that $\{e : \varphi_e(0)\!\downarrow\} \equiv_m K$, by exhibiting both reductions.

**14.** *(proof)* Prove that $K \le_m \{e : W_e \text{ finite}\}$, by constructing an explicit reduction.

**15.** *(proof)* Prove that $\{e : W_e = \mathbb{N}\}$ is undecidable in two different ways: by an explicit
reduction from $K$, and by Rice's theorem.

**16.** *(proof)* Let $A \subseteq \mathbb{N}$ be infinite. Prove that $A$ is decidable if and only if $A$ is
the range of a strictly increasing total computable function.

**17.** *(proof)* Prove that $\{\langle e_1,e_2\rangle : W_{e_1} \subseteq W_{e_2}\}$ is undecidable, by
reducing $K$ to it. (Rice's theorem does not apply directly, because the set is not an index set in a
single variable.)

**18.** *(proof)* Prove that $\{e : \varphi_e \text{ is injective}\}$ is undecidable.

**19.** *(proof)* Prove that $\{e : \lvert W_e\rvert = 3\}$ is undecidable.

**20.** *(proof)* Prove that $\le_m$ is transitive and that $A \le_m B$ implies $\overline A \le_m \overline B$.
Deduce that $A \equiv_m B$ implies $\overline A \equiv_m \overline B$.

**21.** *(proof)* Prove that $\{e : W_e \text{ is finite}\}$ and $\{e : W_e \text{ is decidable}\}$ are both
undecidable. Explain why this does not contradict the fact that many particular sets $W_e$ are decidable.

**22.** Explain why $\{e : \varphi_e \text{ is defined on every input of length at most } 10\}$ is
undecidable, even though it is a finite conjunction of halting questions. Contrast with Example 9.5(d)
of the tutorial.

## Advanced

**23.** *(proof)* Prove the s-m-n theorem: for every partial computable $\psi : \mathbb{N}^2 \rightharpoonup \mathbb{N}$
there is a total computable $s$ with $\varphi_{s(x)}(y) = \psi(x,y)$ for all $x,y$. State clearly where
each hypothesis is used.

**24.** *(proof)* Prove Rice's theorem in full, including the reduction of the general case to the case of a
class containing the empty function or not.

**25.** *(proof)* Prove that $K$ is not co-c.e. by a direct diagonal argument that does not cite
Theorem 7.8(4).

**26.** *(proof)* Prove that there is no total computable $g$ whose range is the set of all total
computable functions, in the following precise sense: there is no total computable $g : \mathbb{N} \to \mathbb{N}$
such that $\{\varphi_{g(n)} : n \in \mathbb{N}\}$ is exactly the set of total computable functions.

**27.** *(proof)* Prove that for every total computable $t$ there are infinitely many $e$ with
$\varphi_e = \varphi_{t(e)}$.

**28.** *(proof)* Prove that $A \equiv_T \overline A$ for every $A$, and that $K \not\equiv_m \overline K$.

**29.** *(proof)* Prove that the set of theorems of PA is c.e. but not decidable.

**30.** *(proof)* Prove that $\operatorname{Inf} = \{e : W_e \text{ infinite}\}$ is $\Pi^0_2$, by writing the
defining formula with the quantifiers in the correct order.

**31.** *(proof)* Prove that there is no total computable $f$ with $W_{f(e)} = \mathbb{N}\setminus W_e$ for all $e$.
(Equivalently: no program computes the complement of an arbitrary c.e. set, uniformly.)

## Challenge

**32.** *(proof)* Fix a binary tape alphabet and let $\mathrm{BB}(n)$ be the largest number of steps
performed by any halting $n$-state machine on the empty input, with $\mathrm{BB}(n) := 0$ if no
$n$-state machine halts on the empty input. Prove that $\mathrm{BB}$ is not computable, and that for
every total computable $f$ there is a constant $c$ with $\mathrm{BB}(n+c) \ge f(n)$ for all sufficiently
large $n$.

**33.** *(proof)* For $A \subseteq \mathbb{N}$ let $A' := \{e : \varphi_e^A(e)\!\downarrow\}$ be the jump of
$A$, where $\varphi_e^A$ denotes the $e$-th machine with an oracle for $A$. Prove that $A' \not\le_T A$ for
every $A$. Deduce that the arithmetical hierarchy is strict.

**34.** *(proof)* Prove that $\operatorname{Th}(\mathbb{N})$, the set of codes of sentences true in the
standard model of arithmetic, is not c.e. You may use Theorem 7.37 and the fact that a consistent c.e.
theory that decides every sentence is decidable.

**35.** *(proof)* Prove that there is no total computable $f$ such that $\varphi_{f(e)} \ne \varphi_e$ for every $e$.
Then prove that this statement is *equivalent* to Kleene's second recursion theorem.

**36.** *(proof)* Prove that $A \subseteq \mathbb{N}$ is c.e. if and only if $A = \varnothing$ or $A$ is the range of a
total computable function. Then prove that every infinite c.e. set $A$ contains an infinite subset $B$ that
is the range of a strictly increasing total computable function, and deduce that $B$ is decidable.
