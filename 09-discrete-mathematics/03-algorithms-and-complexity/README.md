# Algorithms and Complexity

> [Mathematics](../../README.md) › [Discrete Mathematics](../README.md) › Algorithms and Complexity · Level: Advanced · Prerequisites: [Mathematical Induction](../01-mathematical-induction/README.md), [Recurrence Relations](../02-recurrence-relations/README.md), [Proof Techniques](../../00-foundations/04-proof-techniques/README.md), [Logic](../../00-foundations/02-logic/README.md), [Graph Basics](../../21-graph-theory/01-graph-basics/README.md) · Estimated time: 300 min

## 1. Introduction

An **algorithm** is a finite, unambiguous procedure that transforms an input into an output. Algorithms are older than computers — Euclid's algorithm for the greatest common divisor is 2300 years old — but the modern subject begins when we stop asking *"does this procedure give the right answer?"* and start asking *"how much of a resource does it consume, as a function of the size of its input?"*

That shift produces two distinct mathematical theories, and this topic develops both.

The first is **asymptotic analysis**. A running time is a function $T(n)$, and the interesting question is not the value at one $n$ but the *shape* of the function: does doubling the input double the work, quadruple it, or multiply it by a constant more? The vocabulary for this — $O$, $\Omega$, $\Theta$ — is a precise calculus of bounds, with quantifiers, witnesses and proof obligations. It lets us say that merge sort and insertion sort are both correct, but that one is useless for a million records and the other is not, without ever mentioning a machine, a compiler or a clock.

The second is **structural complexity theory**: a classification of problems themselves, not of algorithms. Some problems admit algorithms whose running time is polynomial in the length of the input; others appear to require time exponential in that length, and the difference between the two categories is the difference between a computation that finishes and one that does not. The classes $\mathrm{P}$ and $\mathrm{NP}$, the notion of $\mathrm{NP}$-completeness, and the Cook–Levin theorem are the backbone of this theory. They are also where mathematics meets one of the most famous open problems: is $\mathrm{P} = \mathrm{NP}$?

Beyond both lies a hard boundary. Some problems admit no algorithm at all, not merely no fast one. The **halting problem** is the canonical example: Turing proved in 1936 that no program can decide, for an arbitrary program and input, whether that program terminates. The diagonal argument behind the proof is the same one Cantor used for the uncountability of the reals, and it is the reason no compiler can warn you about every infinite loop.

This tutorial is not a programming course. Algorithms appear as mathematical objects — sets of instructions over a formally specified machine — so that statements about them can be *proved*. The pseudocode below is notation, not code; every complexity claim is a theorem with a proof or a cited result.

## 2. Prerequisites

* **Mathematical induction, including strong induction.** Every loop invariant is maintained by induction over iterations, and every recurrence solution is certified by induction. Taught in [Mathematical Induction](../01-mathematical-induction/README.md), Sections 7.4 and 7.11.
* **Recurrence relations and the master theorem.** Divide-and-conquer running times are recurrences; this tutorial states the master theorem once, applies it repeatedly and links to the full treatment instead of repeating it. Taught in [Recurrence Relations](../02-recurrence-relations/README.md), Sections 7.2–7.10.
* **Proof techniques: direct, contrapositive, contradiction, and the structure of "for all there exists".** The definitions of $O$, $\Omega$ and $\Theta$ are quantified statements, and nearly every exercise asks for a proof or a disproof of one. Taught in [Proof Techniques](../../00-foundations/04-proof-techniques/README.md).
* **Propositional logic and quantifier negation.** Disproving $f = O(g)$ means proving $\forall c\ \forall n_0\ \exists n \ge n_0 : f(n) > c\,g(n)$; manipulating such statements fluently is essential. Taught in [Logic](../../00-foundations/02-logic/README.md), Section 5.
* **Functions, sets and cardinality.** Decision problems are sets of strings; the halting problem proof uses a bijection between programs and natural numbers. Taught in [Relations and Functions](../../00-foundations/05-relations-and-functions/README.md) and [Set Theory](../../00-foundations/03-set-theory/README.md).
* **Logarithms and exponentials.** $\log_b n$, change of base, $b^{\log_b n} = n$, and the standard limits $\log n / n \to 0$, $n^k/2^n \to 0$. Taught in [Exponential and Logarithmic Functions](../../03-algebra/12-exponential-and-logarithmic-functions/README.md).
* **Elementary graph theory.** Degree, path, cycle, connectivity, trees, and the handshake lemma. Taught in [Graph Basics](../../21-graph-theory/01-graph-basics/README.md).
* **Basic counting.** Permutations, subsets, the product rule, and $\binom{n}{2} = n(n-1)/2$. Taught in [Counting Principles](../../20-combinatorics/01-counting-principles/README.md).

## 3. Learning Objectives

By the end of this tutorial you will be able to:

1. Explain what a formal model of computation is, and why running time must be defined relative to one.
2. Distinguish **partial** from **total correctness**, and prove both for a loop using an invariant and a variant.
3. State a loop invariant that is strong enough to imply the postcondition, and identify invariants that are true but useless.
4. Give the $\varepsilon$-free definitions of $O$, $\Omega$, $\Theta$, $o$ and $\omega$, and prove or disprove asymptotic statements from the definition.
5. Apply the limit test, the max rule, transitivity and the growth hierarchy correctly, and explain why "=" in $f = O(g)$ is an abuse of notation.
6. Compute the running time of an iterative algorithm by summing per-iteration costs, and of a recursive one by a recurrence.
7. Analyse insertion sort, merge sort, quicksort and heapsort in the best, average and worst cases, with proofs.
8. Explain the comparison model and prove the $\Omega(n\log n)$ lower bound for comparison sorting by a decision-tree counting argument.
9. State exact or tight comparison counts for binary search, insertion sort and merge sort on restricted input sizes, and check them numerically.
10. Analyse the standard graph algorithms — BFS, DFS, topological sort, Dijkstra, Bellman–Ford, Floyd–Warshall, Kruskal, Prim — and justify each complexity bound from the data structure used.
11. Define $\mathrm{P}$, $\mathrm{NP}$, $\mathrm{coNP}$, polynomial-time reduction, $\mathrm{NP}$-hard and $\mathrm{NP}$-complete precisely.
12. State the Cook–Levin theorem and prove that $\mathrm{CLIQUE}$ is $\mathrm{NP}$-complete by reduction from $\mathrm{3SAT}$.
13. Explain why $\mathrm{NP}$-hardness is a worst-case statement, and describe approximation, parameterisation and SAT solving as responses to it.
14. Prove that the halting problem is undecidable by diagonalisation, and explain what that implies for program verification.

## 4. Intuition

### 4.1 The recipe and the ruler

A recipe tells a cook what to do; it does not tell you how long dinner will take. For that you need a *ruler* — a way of measuring work that does not depend on the particular kitchen. Complexity theory supplies that ruler.

The unit is deliberately crude: one **elementary step**, meaning one comparison, one arithmetic operation, one memory access. Nobody cares whether a comparison costs one nanosecond or three. What matters is how the number of steps changes when the input grows. Ten times more data turning into ten times more work is a very different world from ten times more data turning into a hundred times more work, and the difference is visible long before any constant factor matters.

### 4.2 Why growth beats stopwatch timing

Suppose algorithm $A$ takes $n^2$ steps and algorithm $B$ takes $50n$ steps. For $n < 50$, $A$ wins; for $n > 50$, $B$ wins, and the gap widens without bound. A benchmark on a small input can therefore rank the algorithms backwards. Worse, a benchmark measures *this* machine, *this* compiler and *this* input distribution, while the asymptotic answer is a property of the algorithm alone.

Three practical illustrations of the same point:

* A factor of two in the constant is a hardware upgrade; a factor of $n/\log n$ is not.
* Sorting one million records: insertion sort does about $5 \times 10^{11}$ comparisons, merge sort about $2 \times 10^7$. At $10^8$ comparisons per second that is 90 minutes against 0.2 seconds.
* An algorithm that examines all $2^n$ subsets is fine for $n = 20$ and hopeless for $n = 60$, no matter how fast the hardware becomes; doubling processor speed only buys one extra element.

### 4.3 The adversarial view

"How fast is this algorithm?" is really two questions. *Upper bounds* come from analysing a specific algorithm: merge sort always finishes within $n\lceil \log_2 n\rceil$ comparisons. *Lower bounds* say something about **every possible algorithm** for the problem, and they cannot be proved by analysing one program. They need an adversary or a counting argument.

The cleanest example is comparison sorting. An algorithm that only asks "is $a < b$?" learns one bit per comparison, and it must distinguish $n!$ possible orderings. Since $k$ yes/no questions distinguish at most $2^k$ cases, $2^k \ge n!$ forces $k \ge \log_2 n! = \Theta(n\log n)$. No cleverness escapes this: it is a bound on information, not on ingenuity.

### 4.4 Two kinds of hardness

There are two entirely different reasons why a problem may be difficult, and conflating them is the most common conceptual error in the subject.

* **Tractable but slow, or intractable in the complexity sense.** A problem is in $\mathrm{P}$ if some algorithm solves it in polynomial time. Problems outside $\mathrm{P}$ (if $\mathrm{P} \ne \mathrm{NP}$) still have algorithms — brute force — but those algorithms take exponential time. The barrier is *computational resources*.
* **Undecidable.** A problem is undecidable if **no algorithm whatsoever** solves it, however much time and memory are allowed. The halting problem is of this kind. The barrier is *logic*, not resources.

The first barrier is conjectural and quantitative; the second is a theorem and absolute. Section 7.10–7.12 treat the first, Section 7.13 the second.

### 4.5 How to read the rest of this tutorial

Sections 5 and 6 fix the language: machines, running times, the five asymptotic symbols, and the formal definitions of $\mathrm{P}$, $\mathrm{NP}$ and reduction. Section 7 is the body: correctness, growth, sorting, searching, lower bounds, graphs, tractability, completeness and computability. Section 8 collects the theorems with their proofs, Section 9 works nine examples from routine to hard, and the remaining sections provide the usual apparatus — diagrams, pitfalls, applications, exercises and summary.

## 5. Formal Definition

### 5.1 The machine model

Statements about running time are meaningless without a model of computation, because "one step" is not a mathematical notion. The standard model in algorithm analysis is the **random-access machine** (RAM).

**Definition 5.1** (RAM). A *random-access machine* consists of a finite program, a finite number of registers that hold integers, and an unbounded array of memory cells indexed by integers. In one step it may

* load a constant into a register, or copy a register;
* add, subtract, multiply or divide two integers;
* compare two integers and branch;
* read or write the memory cell whose index is in a register.

Its input is a finite string over a finite alphabet $\Sigma$, placed in consecutive memory cells; the **input size** is $n = |x|$, the number of symbols. (If $\Sigma = \{0,1\}$ we may identify $n$ with the number of bits.)

The model is a fiction in one respect: registers hold integers of *unbounded* size and arithmetic on them costs one step. This is the **unit-cost** model. The **bit-cost** model charges in proportion to the number of bits touched. The two can disagree dramatically: computing $2^{2^k}$ by repeated squaring takes $k$ unit-cost steps but produces a number with $2^k$ bits, so the bit cost is exponential. For sorting, searching and graph problems every integer handled is bounded by the input size and the models agree up to a polynomial factor; for number-theoretic problems (Section 7.10) the distinction is essential, which is why complexity classes are defined over *encodings*.

All logarithms in complexity statements are base $2$ unless a base is written; changing base multiplies by a constant and does not affect any $\Theta$ class.

### 5.2 Running time

**Definition 5.2** (Running time). Fix a RAM $M$ that halts on every input. For an input $x$, let $T_M(x)$ be the number of steps $M$ executes. The **worst-case running time** on inputs of size $n$ is

$$T_M(n) \;=\; \max\{\,T_M(x) : |x| = n\,\},$$

the **best-case** time is the corresponding minimum, and the **average-case** time is $\mathbb{E}[T_M(x)]$ where $x$ is drawn from a specified distribution on inputs of size $n$. An algorithm runs *in polynomial time* when $T_M(n) = O(n^k)$ for some constant $k$.

Worst-case time is the default because it is a guarantee: it holds for every input, and it composes (a program that calls a polynomial-time subroutine on polynomially many subproblems of polynomial size is still polynomial). Average-case time is the right notion when inputs have a known distribution, but it is only as meaningful as the distribution — quicksort is fast on random permutations and slow on sorted ones.

### 5.3 Asymptotic notation

Let $f, g : \mathbb{N} \to \mathbb{R}$ with $g(n) > 0$ for all sufficiently large $n$.

**Definition 5.3** (The five symbols).

$$f(n) = O(g(n)) \iff \exists c > 0\ \exists n_0\ \forall n \ge n_0:\ 0 \le f(n) \le c\,g(n),$$
$$f(n) = \Omega(g(n)) \iff \exists c > 0\ \exists n_0\ \forall n \ge n_0:\ f(n) \ge c\,g(n) \ge 0,$$
$$f(n) = \Theta(g(n)) \iff f(n) = O(g(n)) \text{ and } f(n) = \Omega(g(n)),$$
$$f(n) = o(g(n)) \iff \forall c > 0\ \exists n_0\ \forall n \ge n_0:\ 0 \le f(n) < c\,g(n),$$
$$f(n) = \omega(g(n)) \iff \forall c > 0\ \exists n_0\ \forall n \ge n_0:\ f(n) > c\,g(n) \ge 0.$$

Each symbol defines a *set* of functions, and $f(n) = O(g(n))$ is shorthand for $f \in O(g)$. This is why the notation is not symmetric: $O(g)$ is a whole class, so writing $O(g) = f$ is meaningless and $f = O(g) = h$ does not mean $f = h$. The relation $\Theta$ is an equivalence relation on positive functions; $O$ and $\Omega$ are preorders, and $o$ and $\omega$ are strict versions.

### 5.4 Correctness

Correctness is a statement about a *specification*, not about an output in isolation.

**Definition 5.4** (Hoare triple; partial and total correctness). Let $A$ be an algorithm, $P$ a predicate on inputs (the **precondition**) and $Q$ a predicate on inputs and outputs (the **postcondition**). The triple $\{P\}\,A\,\{Q\}$ holds *partially* when: for every input satisfying $P$, if $A$ terminates then its output satisfies $Q$. It holds *totally* when, in addition, $A$ terminates on every input satisfying $P$.

A **loop invariant** is a predicate $I$ that holds at the start of every iteration of a loop. Section 7.2 gives the proof obligations that turn an invariant into a correctness proof.

### 5.5 Decision problems

Complexity theory classifies *problems*, and the cleanest problems are those with a yes/no answer.

**Definition 5.5** (Decision problem, encoding). An *encoding* is an injective map from a set of objects (graphs, formulas, integers) to $\{0,1\}^*$. A *decision problem* is a function $f : \{0,1\}^* \to \{0,1\}$; its **language** is $L_f = \{x : f(x) = 1\}$. An algorithm *decides* $L$ if it halts on every input $x$ with output $1$ when $x \in L$ and $0$ otherwise. The input size is always the length of the encoding, never a numeric value appearing in it: writing an integer $N$ takes $\lceil \log_2(N+1) \rceil$ bits, so an algorithm running in time $O(N)$ runs in time exponential in its input size.

When we say "the problem of deciding whether a graph has a clique of size $k$", the encoding is implicit and must be fixed (adjacency list, adjacency matrix, or a binary string). Polynomial-time solvability is encoding-independent as long as the encodings are polynomially related, which is the case for all standard graph, formula and integer encodings.

**Definition 5.6** ($\mathrm{P}$).

$$\mathrm{P} = \{\, L \subseteq \{0,1\}^* : L \text{ is decided by a deterministic RAM in time } O(n^k) \text{ for some } k \,\}.$$

### 5.6 Verification and NP

$\mathrm{NP}$ is *not* "not polynomial". The letters stand for **nondeterministic polynomial time**, and the class has two equivalent definitions: one by nondeterministic machines, one by polynomial-time verification. The second is the working definition.

**Definition 5.7** ($\mathrm{NP}$, verifier). A *verifier* for a language $L$ is an algorithm $V(x, w)$ that takes a candidate $x$ and a **certificate** (or witness) $w$. It is a *polynomial-time verifier* if $V$ runs in time $O(|x|^k)$ for some fixed $k$. Then

$$L \in \mathrm{NP} \iff \exists \text{ a polynomial-time verifier } V\ \exists \text{ a polynomial } p\ \forall x:\ x \in L \iff \exists w,\ |w| \le p(|x|),\ V(x,w) = 1.$$

The certificate must be short: a witness of exponential length could not even be read in polynomial time. A decision problem is in $\mathrm{NP}$ when a *yes* answer can be checked quickly, not when it can be found quickly. For example, "does this graph have a clique of size $k$?" is in $\mathrm{NP}$ because the $k$ vertices of a clique can be exhibited and checked in $O(k^2)$ time; nobody knows how to find such a clique quickly.

### 5.7 Reductions and completeness

**Definition 5.8** (Polynomial-time reduction). $L_1 \le_{\mathrm{p}} L_2$ ("$L_1$ reduces to $L_2$") if there is a function $f : \{0,1\}^* \to \{0,1\}^*$, computable in polynomial time, such that for all $x$,

$$x \in L_1 \iff f(x) \in L_2.$$

The reduction need not be injective; it only has to preserve membership in both directions. Its purpose is the contrapositive: a fast decider for $L_2$ yields a fast decider for $L_1$ (compute $f(x)$, then decide), so if $L_1$ is hard then $L_2$ is at least as hard.

**Definition 5.9** ($\mathrm{NP}$-hard, $\mathrm{NP}$-complete).

$$L \text{ is } \mathrm{NP}\text{-hard} \iff \forall L' \in \mathrm{NP}:\ L' \le_{\mathrm{p}} L,$$
$$L \text{ is } \mathrm{NP}\text{-complete} \iff L \in \mathrm{NP} \text{ and } L \text{ is } \mathrm{NP}\text{-hard}.$$

An $\mathrm{NP}$-complete problem is simultaneously the hardest kind of problem in $\mathrm{NP}$ (everything reduces to it) and a member of $\mathrm{NP}$ (so it has a short certificate). Proving one problem $\mathrm{NP}$-complete from scratch requires quantifying over all of $\mathrm{NP}$; after the first one, reductions do the work, because $\le_{\mathrm{p}}$ is transitive (Theorem 8.2).

## 6. Mathematical Notation

| Symbol | Read as | Meaning |
|---|---|---|
| $T(n)$ | running time | number of elementary steps on inputs of size $n$ |
| $O(g)$, $\Omega(g)$, $\Theta(g)$ | big-O, big-Omega, big-Theta | sets of functions bounded above, below, both |
| $o(g)$, $\omega(g)$ | little-o, little-omega | strictly smaller / strictly larger growth |
| $f \prec g$ | $f$ grows slower than $g$ | $f = o(g)$ |
| $\lg n$ | log base 2 | $\log_2 n$; base changes are $\Theta(1)$ factors |
| $H_n$ | $n$-th harmonic number | $\sum_{k=1}^{n} 1/k = \ln n + \gamma + O(1/n)$ |
| $\lceil x \rceil$, $\lfloor x \rfloor$ | ceiling, floor | least integer $\ge x$, greatest integer $\le x$ |
| $n!$ | factorial | number of permutations of $n$ items |
| $|x|$ | length of $x$ | number of bits or symbols in the encoding |
| $V(x,w)$ | verifier output | $1$ if $w$ certifies $x$, else $0$ |
| $L_1 \le_{\mathrm{p}} L_2$ | $L_1$ reduces to $L_2$ | polynomial-time many-one reduction |
| $\mathrm{P}$, $\mathrm{NP}$, $\mathrm{coNP}$ | complexity classes | see Sections 5.6 and 7.10 |
| $\mathrm{NP}$-hard, $\mathrm{NP}$-complete | hardness notions | Definitions 5.9 |
| $V$, $E$ | vertex, edge counts | $|V| = n$, $|E| = m$ in graph analyses |
| $\delta(s,v)$ | graph distance | fewest edges on a path from $s$ to $v$ |
| $\alpha(n)$, $\operatorname{inv}$ Ackermann | inverse Ackermann | effectively constant; union-find bound |
| $\{P\}\,A\,\{Q\}$ | Hoare triple | partial correctness of $A$ w.r.t. $P$, $Q$ |
| $\blacksquare$ | end of proof | — |

## 7. Core Concepts

### 7.1 Algorithms as mathematical objects

An algorithm is specified by three ingredients: the **set of legal inputs** (with a size measure), the **output**, and the **transition rules** that produce the output. Formally, a deterministic algorithm computes a partial function $A : \{0,1\}^* \rightharpoonup \{0,1\}^*$; the domain of $A$ is the set of inputs on which it halts.

The natural specification of Euclid's algorithm is typical. On input $(a,b) \in \mathbb{N}_0^2$ with $a + b > 0$, it outputs $\gcd(a,b)$:

```
Euclid(a, b):
    while b > 0:
        (a, b) = (b, a mod b)
    return a
```

Three mathematical questions can be asked about it, and they are independent.

1. **Partial correctness.** If it halts, is the answer $\gcd(a,b)$?
2. **Termination.** Does it halt on every legal input?
3. **Complexity.** How many divisions does it perform, as a function of the number of bits of $a$ and $b$?

The answers are: yes, because $\gcd(a,b) = \gcd(b, a \bmod b)$; yes, because $b$ is replaced by a strictly smaller non-negative integer, so after at most $b$ iterations it reaches $0$; and $O(\log(\min(a,b)))$ divisions, a result of Lamé from 1844 (the worst case is a pair of consecutive Fibonacci numbers). Each answer is a mathematical statement about a mathematical object, not an empirical report about a computer.

### 7.2 Correctness proofs and loop invariants

For an iterative algorithm the standard instrument is the **loop invariant**: a predicate $I$ that is true at the start of every iteration. Three obligations must be discharged.

| Obligation | What to prove | Why it is needed |
|---|---|---|
| **Initialisation** | $I$ holds before the first iteration | gives the induction base |
| **Maintenance** | if $I$ holds before an iteration and the iteration runs, then $I$ holds after it | the induction step |
| **Termination** | when the loop ends, $I$ together with the exit condition implies the postcondition | converts the invariant into the goal |

This is ordinary induction over the iteration count. It proves *partial* correctness only. *Total* correctness also needs a **variant**: an integer-valued quantity that is non-negative, strictly decreases on every iteration, and therefore cannot decrease forever. For insertion sort the variant is $n - i$ in the outer loop and $j$ in the inner loop; for Euclid's algorithm it is $b$.

**The invariant must be strong enough.** Consider linear search for a value $v$ in $A[1..n]$ with the loop `while i <= n and A[i] != v: i = i + 1`. The predicate "$i \le n+1$" is a genuine invariant and survives termination, but it does not imply the postcondition "$A[i] = v$ or $v \notin A$". A correct invariant records what has been *examined*:

$$I:\quad 1 \le i \le n+1 \ \text{ and }\ v \notin \{A[1], \dots, A[i-1]\}.$$

Now termination with $i \le n$ gives $A[i] = v$, and termination with $i = n+1$ gives $v \notin A$. Choosing the invariant is the creative part; verifying it is mechanical.

**Worked proof: insertion sort.** The pseudocode is

```
InsertionSort(A, n):
    for i = 2 to n:
        key = A[i]
        j = i - 1
        while j >= 1 and A[j] > key:
            A[j+1] = A[j]
            j = j - 1
        A[j+1] = key
```

*Outer invariant.* At the start of the iteration with index $i$, the prefix $A[1..i-1]$ is a permutation of the original first $i-1$ entries and is sorted in non-decreasing order.

*Initialisation.* For $i = 2$ the prefix has one element, trivially sorted.

*Maintenance.* Assume the invariant for $i$. The inner loop moves every entry of $A[1..i-1]$ that exceeds `key` one position to the right, preserving their relative order, and stops at the first position $j$ with $A[j] \le$ `key` (or at $j = 0$). Inserting `key` at $j+1$ therefore yields a sorted permutation of the first $i$ original entries — the invariant for $i+1$.

*Termination.* The outer loop ends with $i = n+1$, so $A[1..n]$ is a sorted permutation of the input. Hence the output is a sorted version of the input.

*Total correctness.* The inner loop decreases $j$ by one each pass and stops at $j = 0$ at the latest; the outer loop advances $i$ from $2$ to $n+1$. Both terminate.

The same method certifies binary search. With `lo`, `hi` and the sorted array $A[1..n]$, the invariant is

$$I:\quad 1 \le lo \le hi+1 \le n+1 \quad\text{and}\quad \bigl(v \in A[1..n] \Rightarrow v \in A[lo..hi]\bigr),$$

with the convention that the range is empty when $lo = hi+1$. Each comparison discards a half that provably does not contain $v$, and termination with an empty range proves absence.

### 7.3 Growth of functions

The definitions of Section 5.3 are the whole theory; everything else is technique. There are four standard techniques for establishing a bound.

**(i) Direct witness construction.** To prove $f = O(g)$, exhibit $c$ and $n_0$ and verify the inequality for all $n \ge n_0$. Often it helps to bound each term separately: if $f(n) = 3n^2 + 2n + 1$, then for $n \ge 1$,

$$3n^2 + 2n + 1 \le 3n^2 + 2n^2 + n^2 = 6n^2,$$

so $f = O(n^2)$ with $c = 6$, $n_0 = 1$. To *disprove* $f = O(g)$ one must show that no witnesses exist: assume $f(n) \le c\,g(n)$ for all $n \ge n_0$ and derive a contradiction for some $n > \max(n_0, \text{threshold}(c))$.

**(ii) The limit test.** If $g(n) > 0$ eventually and $L = \lim_{n\to\infty} f(n)/g(n)$ exists in $[0,\infty]$, then

$$L < \infty \Rightarrow f = O(g), \qquad L > 0 \Rightarrow f = \Omega(g), \qquad 0 < L < \infty \Rightarrow f = \Theta(g),$$
$$L = 0 \Rightarrow f = o(g), \qquad L = \infty \Rightarrow f = \omega(g).$$

For instance $\lim_{n\to\infty} \frac{3n^2+2n+1}{n^2} = 3$, so the function is $\Theta(n^2)$; and $\lim_{n\to\infty} \frac{n^2}{n\log n} = \infty$, so $n^2 = \omega(n\log n)$.

**(iii) Induction.** Used when the bound is proved for a recursively defined quantity — the running time of a recursive algorithm, for example — or when a bound such as $n^k = O(2^n)$ is proved by induction on $k$.

**(iv) Summation bounds.** For loops and series: bound each term, or compare a sum with an integral. The harmonic sum satisfies

$$\ln(n+1) \le H_n = \sum_{k=1}^{n}\frac1k \le 1 + \ln n,$$

which is how $H_n = \Theta(\log n)$ is proved.

**The growth hierarchy.** For constants $0 < \varepsilon$ and $k > 0$,

$$1 \ \prec\ \log\log n \ \prec\ \log n \ \prec\ n^{\varepsilon} \ \prec\ n \ \prec\ n\log n \ \prec\ n^2 \ \prec\ n^3 \ \prec\ 2^n \ \prec\ n! \ \prec\ n^n,$$

where $f \prec g$ means $f = o(g)$. Every strict inequality in this chain is a theorem; the two non-obvious ones, $\log n \prec n^\varepsilon$ and $n^k \prec 2^n$, are proved in Section 8.

**Algebra of bounds.** For non-negative functions: $O(f) + O(g) = O(f+g) = O(\max(f,g))$; $O(f)\cdot O(g) = O(fg)$; $f = O(g)$ and $g = O(h)$ imply $f = O(h)$; and $\Theta$ is transitive and symmetric. The max rule is the one used constantly: the running time of a sequence of phases is the maximum, not the sum, of their orders, because the largest term dominates.

### 7.4 Cost models and how to count

Every complexity statement is relative to a model and to a chosen *cost measure*. Three measures recur:

* **Comparisons.** For sorting and searching arbitrary keys, comparisons are the only operations that extract information about the order; counting them gives model-independent lower bounds (Section 7.8).
* **Arithmetic operations.** For number-theoretic algorithms one counts multiplications and divisions, but the bit cost may be much larger (multiplying two $n$-bit numbers is not $O(1)$ in reality).
* **Memory accesses / graph traversals.** For graph algorithms one counts operations in terms of $V$ and $E$, which requires fixing a representation: adjacency lists use $\Theta(V+E)$ space and scan a vertex's neighbourhood in time proportional to its degree; an adjacency matrix uses $\Theta(V^2)$ space and answers "is there an edge?" in $O(1)$.

A subtlety that decides many graph bounds: an algorithm running in $O(V^2)$ time is *linear* in the size of an adjacency-matrix input but *quadratic* in the size of an adjacency-list input. Always state which representation the bound assumes. Similarly, an $O(n)$ algorithm for a problem whose input contains an integer $N$ is exponential in the input length $\log N$; such algorithms are called **pseudo-polynomial** and are treated in Section 7.12.

### 7.5 Recurrences revisited

The running time of a divide-and-conquer algorithm satisfies a recurrence. The full theory — iteration, characteristic roots, generating functions and the proof of the master theorem — is the subject of [Recurrence Relations](../02-recurrence-relations/README.md), Sections 7.2–7.10; this section only restates the result used repeatedly below and records the standard applications. Nothing here is proved again.

**Master theorem** (for $T(n) = aT(n/b) + f(n)$, with $a \ge 1$, $b > 1$, $f$ non-negative, $n = b^k$; let $c = \log_b a$):

1. if $f(n) = O(n^{c-\varepsilon})$ for some $\varepsilon > 0$, then $T(n) = \Theta(n^{c})$;
2. if $f(n) = \Theta(n^{c})$, then $T(n) = \Theta(n^{c}\log n)$;
3. if $f(n) = \Omega(n^{c+\varepsilon})$ for some $\varepsilon > 0$ *and* $a\,f(n/b) \le \delta f(n)$ for some $\delta < 1$ and all large $n$, then $T(n) = \Theta(f(n))$.

| Recurrence | $a$ | $b$ | $c = \log_b a$ | Case | Solution |
|---|---|---|---|---|---|
| $T(n) = 2T(n/2) + n$ | 2 | 2 | 1 | 2 | $\Theta(n\log n)$ |
| $T(n) = 2T(n/2) + 1$ | 2 | 2 | 1 | 1 | $\Theta(n)$ |
| $T(n) = 2T(n/2) + n^2$ | 2 | 2 | 1 | 3 | $\Theta(n^2)$ |
| $T(n) = 4T(n/2) + n$ | 4 | 2 | 2 | 1 | $\Theta(n^2)$ |
| $T(n) = 4T(n/2) + n^2$ | 4 | 2 | 2 | 2 | $\Theta(n^2\log n)$ |
| $T(n) = T(n/2) + 1$ | 1 | 2 | 0 | 2 | $\Theta(\log n)$ |
| $T(n) = 8T(n/2) + n^2$ | 8 | 2 | 3 | 1 | $\Theta(n^3)$ |

The intuition is the **recursion tree**: level $j$ contains $a^j$ subproblems of size $n/b^j$, doing total work $a^j f(n/b^j) = n^{c} f(n/b^j)/f(n)\cdot f(n)$; whichever of the root cost and the leaves cost dominates decides the case. For the substitution method, guess the answer and verify it by induction with an explicit constant — Section 9.5 does this for merge sort.

### 7.6 Analysis of sorting

In the **comparison model** an algorithm may compare two elements, move them, and nothing else; it learns about the input only through the outcomes of comparisons. All the classical sorting algorithms live in this model, and Section 7.8 shows that no algorithm in it can beat $\Omega(n\log n)$.

**Insertion sort.** The pseudocode and the invariant are in Section 7.2. The inner loop performs one comparison per position scanned. In the worst case — input in decreasing order — the iteration $i$ performs exactly $i-1$ comparisons and moves, so

$$C_{\text{worst}}(n) = \sum_{i=2}^{n}(i-1) = \frac{n(n-1)}{2} = \Theta(n^2).$$

In the best case (already sorted) the inner loop performs one comparison per $i$, so $C_{\text{best}}(n) = n-1 = \Theta(n)$. The number of comparisons in *every* case is exactly the number of **inversions** of the input plus the number of iterations in which the inner loop stopped because $A[j] \le \textit{key}$; since each pair is an inversion with probability $1/2$ under a uniformly random permutation,

$$\mathbb{E}[C] = \binom{n}{2}\cdot\frac12 + O(n) = \frac{n(n-1)}{4} + O(n) = \Theta(n^2).$$

Insertion sort is stable, in place ($\Theta(1)$ extra space) and adaptive: it is linear on nearly sorted data, which is why it is used inside library sorts for small subarrays.

**Merge sort.** Split the array in half, sort each half recursively, merge the two sorted halves in linear time. Merging lists of total length $m$ uses at most $m-1$ comparisons (each comparison emits one element, and when one list empties the rest is copied). The recursion tree has $\lceil \lg n\rceil$ levels, and the merges at each level touch disjoint subarrays whose total length is $n$; hence

$$C_{\text{merge}}(n) \le n\lceil \lg n\rceil = O(n\log n).$$

The recurrence is $T(n) = 2T(n/2) + \Theta(n)$, which the master theorem (case 2) solves as $\Theta(n\log n)$; for $n$ a power of two the exact worst case is $n\lg n - n + 1$ comparisons. Merge sort is stable, has no bad inputs, and needs $\Theta(n)$ auxiliary space.

**Quicksort.** Choose a pivot, partition the other elements into those smaller and those larger (one comparison per element), then recurse on both sides. Partition of a subarray of length $m$ uses exactly $m-1$ comparisons.

*Worst case.* If the pivot is always the smallest or the largest element, the recursion is $T(n) = T(n-1) + (n-1)$ with $T(1) = 0$, hence $T(n) = n(n-1)/2 = \Theta(n^2)$. This happens for a sorted or reverse-sorted array when the pivot is always the first or last element.

*Best case.* Perfectly balanced partitions give $T(n) = 2T(n/2) + (n-1) = \Theta(n\log n)$ by the master theorem.

*Average case.* With a uniformly random pivot (equivalently, a uniformly random permutation and any fixed pivot rule), the expected number of comparisons is

$$\mathbb{E}[C_n] = 2(n+1)H_n - 4n = \Theta(n\log n),$$

which is about $1.39\,n\lg n$. Theorem 8.8 proves this by indicator random variables. The average case is only a statement about the distribution: adversarial or accidentally sorted inputs still trigger the quadratic worst case unless the pivot is randomised.

**Heapsort.** Build a max-heap in $O(n)$ time, then repeatedly extract the maximum in $O(\log n)$ time; the total is $\Theta(n\log n)$ in every case, in place, but the algorithm is not stable and has poor cache behaviour. It is the standard example of an algorithm that meets the lower bound without being the fastest in practice.

| Algorithm | Best | Average | Worst | Extra space | Stable |
|---|---|---|---|---|---|
| Insertion sort | $\Theta(n)$ | $\Theta(n^2)$ | $\Theta(n^2)$ | $\Theta(1)$ | yes |
| Selection sort | $\Theta(n^2)$ | $\Theta(n^2)$ | $\Theta(n^2)$ | $\Theta(1)$ | no |
| Merge sort | $\Theta(n\log n)$ | $\Theta(n\log n)$ | $\Theta(n\log n)$ | $\Theta(n)$ | yes |
| Heapsort | $\Theta(n\log n)$ | $\Theta(n\log n)$ | $\Theta(n\log n)$ | $\Theta(1)$ | no |
| Quicksort | $\Theta(n\log n)$ | $\Theta(n\log n)$ expected | $\Theta(n^2)$ | $\Theta(\log n)$ stack | no |
| Counting sort | $\Theta(n+k)$ | $\Theta(n+k)$ | $\Theta(n+k)$ | $\Theta(n+k)$ | yes |

Counting sort is not a comparison sort: it assumes keys are integers in $\{0,\dots,k-1\}$ and counts occurrences. Its linear time does not contradict the $\Omega(n\log n)$ bound, because that bound is about the comparison model only. Radix sort achieves $\Theta(d(n+k))$ for $d$-digit keys; for keys of $O(\log n)$ bits it is linear.

### 7.7 Analysis of searching

**Linear search.** Scanning an unordered array performs at most $n$ comparisons, exactly $n$ when the value is absent, and $(n+1)/2$ on average for a successful search under the uniform distribution. It is optimal in the comparison model for unordered data: an adversary can answer "not equal" to every query until only one unexamined element remains, so $\Omega(n)$ comparisons are necessary (Section 7.8).

**Binary search.** On a sorted array, compare with the middle element and discard the half that cannot contain the target. The recurrence is $T(n) = T(\lfloor n/2\rfloor) + 1$ with $T(0) = 0$, whose solution is

$$T(n) = \lfloor \lg n\rfloor + 1 \quad (n \ge 1).$$

Check: $n = 1$ gives $1$; $n = 2$ gives $2$; $n = 3$ gives $2$ (the middle element is found in one comparison, and either end in two); $n = 10$ gives $4$. The lower bound for searching $n$ ordered items is $\lceil \lg(n+1)\rceil$ comparisons when absence is a possible outcome, since the decision tree has $n+1$ leaves; binary search is therefore optimal up to one comparison.

**Hash tables and search trees.** A hash table with $n$ keys in $m$ slots and load factor $\alpha = n/m$ supports search in $\Theta(1+\alpha)$ expected time under simple uniform hashing, but $\Theta(n)$ in the worst case. A binary search tree supports search in $\Theta(h)$ where $h$ is the height: $\Theta(\log n)$ if balanced, $\Theta(n)$ if degenerate. These structures trade the ordering information of a sorted array for different cost profiles; they are analysed in data-structures courses and only their complexity is used here.

### 7.8 Lower bounds by decision trees

A **decision tree** models any algorithm whose only access to the input is a sequence of comparisons. Each internal node is a comparison with two outcomes; each leaf is an output. An execution on a particular input is a root-to-leaf path, so the number of comparisons is the depth of the leaf, and the worst case is the height of the tree.

**Theorem 7.1** (Comparison-sorting lower bound). Every comparison-based sorting algorithm uses at least $\lceil \log_2(n!)\rceil$ comparisons in the worst case on inputs of size $n$, hence $\Omega(n\log n)$ comparisons.

*Proof.* There are $n!$ possible orderings of $n$ distinct keys. If two different orderings reached the same leaf, the algorithm would output the same permutation for both, and that permutation would be wrong for at least one of them. So the tree has at least $n!$ leaves. A binary tree of height $h$ has at most $2^h$ leaves, so $2^h \ge n!$ and $h \ge \log_2(n!)$. Finally

$$\log_2(n!) = \sum_{k=1}^{n}\log_2 k \;\ge\; \sum_{k=\lceil n/2\rceil}^{n}\log_2\frac{n}{2} \;\ge\; \frac{n}{2}\log_2\frac{n}{2} = \Omega(n\log n),$$

using that at least $n/2$ of the factors are at least $n/2$. $\blacksquare$

The bound is tight to within a constant: merge sort uses at most $n\lceil\lg n\rceil$ comparisons, and more elaborate algorithms (merge–insertion, Ford–Johnson) achieve $\log_2(n!) + O(n)$, which is optimal. For small $n$ the exact values are informative: $n = 3$ needs $3$ comparisons, $n = 4$ needs $5$, $n = 5$ needs $7$, $n = 6$ needs $10$, because $\lceil \lg 6\rceil = 3$, $\lceil \lg 24\rceil = 5$, $\lceil \lg 120\rceil = 7$ and $\lceil \lg 720\rceil = 10$.

**Searching.** A comparison-based search among $n$ ordered items has at least $n$ leaves (one per successful outcome) and, if absence must be reported, $n+1$ leaves. Hence its height is at least $\lceil \lg(n+1)\rceil = \Omega(\log n)$, matching binary search.

**What the bound does not say.** It says nothing about algorithms that use arithmetic on keys (counting and radix sort), about parallel algorithms, or about problems where the input is known to be nearly sorted. It is a statement about one model, and models matter.

### 7.9 Graph algorithms and their complexity

Graph algorithms are analysed in terms of $V = |V|$ and $E = |E|$, always with a stated representation. Two facts drive most bounds: a vertex's neighbourhood is scanned in time proportional to its degree (adjacency list), and $\sum_{v}\deg(v) = 2E$ (the handshake lemma, [Graph Basics](../../21-graph-theory/01-graph-basics/README.md)).

**Breadth-first search.** Starting from $s$, BFS explores vertices in order of their distance from $s$, using a queue. Each vertex is enqueued and dequeued at most once, and each edge is examined at most twice, so the total is $O(V+E)$. Correctness rests on the invariant that the queue holds vertices of distance $d$ followed by vertices of distance $d+1$; hence the first time a vertex is reached, it is reached by a shortest path. This makes BFS a shortest-path algorithm for *unweighted* graphs.

**Depth-first search.** DFS explores as deep as possible before backtracking. Its running time is $O(V+E)$, and the DFS forest classifies each edge of a directed graph as a tree, back, forward or cross edge. A directed graph has a cycle if and only if DFS produces a back edge; this gives $O(V+E)$ cycle detection.

**Topological sorting.** A topological order of a directed graph lists every vertex before all of its successors. It exists if and only if the graph is acyclic, and Kahn's algorithm — repeatedly remove a vertex of in-degree zero — computes one in $O(V+E)$.

**Dijkstra's algorithm.** For non-negative edge weights, Dijkstra grows a set $S$ of vertices whose shortest distance is final, repeatedly adding the vertex of least tentative distance. With a binary heap the cost is $O((V+E)\log V)$; with a plain array it is $O(V^2 + E) = O(V^2)$, which is better for dense graphs; with a Fibonacci heap it is $O(E + V\log V)$.

*Why it is correct.* When the vertex $u \notin S$ of minimum tentative distance is chosen, every path from $s$ to $u$ that leaves $S$ must pass through some vertex $x \notin S$ first, and its length is already at least $d(u)$; non-negative weights ensure the rest of the path cannot shorten it. So $d(u)$ is final. $\square$

*Why non-negative weights are essential.* Take $s \to a$ of weight $2$, $s \to b$ of weight $5$, and $b \to a$ of weight $-4$. Dijkstra settles $a$ at distance $2$; the true distance is $5 - 4 = 1$. The exchange argument fails because a later edge can reduce a settled distance.

**Bellman–Ford.** Relax every edge $V-1$ times. After the $k$-th pass, all shortest paths using at most $k$ edges are correct, so after $V-1$ passes all distances are final; a $V$-th pass that still improves some distance certifies a negative cycle. The cost is $O(VE)$.

**Floyd–Warshall.** All-pairs shortest paths by dynamic programming over allowed intermediate vertices:

$$d^{(k)}_{ij} = \min\bigl(d^{(k-1)}_{ij},\ d^{(k-1)}_{ik} + d^{(k-1)}_{kj}\bigr).$$

The cost is $O(V^3)$ time and $O(V^2)$ space, and the algorithm tolerates negative edges as long as there is no negative cycle.

**Minimum spanning trees.** Kruskal's algorithm sorts the edges and adds each one that does not create a cycle, using a union-find structure to test that condition; with the near-linear union-find bound the total is $O(E\log E) = O(E\log V)$. Prim's algorithm grows a tree from one vertex using a priority queue, at $O(E\log V)$ with a binary heap or $O(V^2)$ with an array. Both are correct by the **cut property**: the lightest edge crossing any cut belongs to some minimum spanning tree.

| Problem | Algorithm | Time | Assumptions |
|---|---|---|---|
| Unweighted shortest paths | BFS | $O(V+E)$ | unweighted |
| Connected components | BFS or DFS | $O(V+E)$ | undirected |
| Cycle detection | DFS | $O(V+E)$ | directed or undirected |
| Topological order | Kahn / DFS | $O(V+E)$ | DAG |
| Single-source shortest paths | Dijkstra (binary heap) | $O((V+E)\log V)$ | weights $\ge 0$ |
| Single-source shortest paths | Bellman–Ford | $O(VE)$ | no negative cycle |
| All-pairs shortest paths | Floyd–Warshall | $O(V^3)$ | no negative cycle |
| Minimum spanning tree | Kruskal | $O(E\log V)$ | undirected |
| Minimum spanning tree | Prim (binary heap) | $O(E\log V)$ | undirected |
| Strongly connected components | Tarjan / Kosaraju | $O(V+E)$ | directed |
| Maximum flow | Edmonds–Karp | $O(VE^2)$ | capacities |

A numerical illustration of why the representation matters: for $V = 10^4$ and $E = 10^5$, Dijkstra with an array costs about $10^8$ operations, while the heap version costs about $(1.1\times10^5)\cdot 14 \approx 1.5\times 10^6$ — a factor of nearly $70$. On a dense graph with $E \approx V^2/2$, the same comparison reverses, because $\log V$ grows while the array version stays $V^2$.

### 7.10 Tractability, P and NP

**Why polynomial time?** Three reasons make "solvable in time $O(n^k)$" the accepted formalisation of *tractable*.

1. **Robustness.** Every reasonable sequential model of computation — RAM, Turing machine, lambda calculus, cellular automaton — simulates every other with polynomial overhead. A problem in $\mathrm{P}$ on one model is in $\mathrm{P}$ on all of them, so the class is a property of the problem, not of the machine.
2. **Closure.** Polynomial-time algorithms compose: a polynomial number of calls to polynomial-time subroutines is still polynomial. This is what makes algorithm design modular.
3. **Scaling.** A $2^n$ algorithm stops being usable when $n$ increases by a few dozen, whatever the hardware; an $n^3$ algorithm keeps working. Empirical growth, not elegance, is the criterion.

**Decision problems in and around $\mathrm{P}$.**

* In $\mathrm{P}$: sorting, shortest paths, minimum spanning trees, maximum flow, linear programming, primality testing (the AKS algorithm, 2002), and context-free grammar membership (CYK, $O(n^3)$).
* In $\mathrm{NP}$ but not known to be in $\mathrm{P}$: $\mathrm{SAT}$, $\mathrm{3SAT}$, $\mathrm{CLIQUE}$, $\mathrm{VERTEX}$-$\mathrm{COVER}$, $\mathrm{HAMILTONIAN}$-$\mathrm{CYCLE}$, $\mathrm{TSP}$ (decision version), $\mathrm{SUBSET}$-$\mathrm{SUM}$, graph $3$-colouring.
* In $\mathrm{NP} \cap \mathrm{coNP}$, not known to be in $\mathrm{P}$: integer factorisation (decide whether $N$ has a divisor $d$ with $2 \le d \le k$).
* Outside $\mathrm{NP}$ (under standard assumptions): problems requiring exponential certificates, and all undecidable problems.

**Theorem 7.2.** $\mathrm{P} \subseteq \mathrm{NP} \subseteq \mathrm{EXP}$, where $\mathrm{EXP} = \bigcup_k \mathrm{DTIME}(2^{n^k})$.

*Proof.* A polynomial-time decider is a polynomial-time verifier that ignores its certificate, so $\mathrm{P} \subseteq \mathrm{NP}$. For the second inclusion, a verifier running in time $p(n)$ accepts some certificate of length at most $p(n)$; trying all $2^{p(n)+1}-1$ binary strings is a deterministic computation in time $O(2^{p(n)}\cdot p(n))$, which is exponential. $\blacksquare$

Both inclusions are believed strict, but neither strictness is proved. $\mathrm{P} \ne \mathrm{EXP}$ *is* proved (time hierarchy theorem), so at least one of the two is strict.

**coNP.** $\mathrm{coNP} = \{L : \overline{L} \in \mathrm{NP}\}$: problems whose *no* instances have short certificates. A problem in $\mathrm{NP} \cap \mathrm{coNP}$ has short certificates for both answers, which is why such problems are considered unlikely to be $\mathrm{NP}$-complete: if an $\mathrm{NP}$-complete problem lay in $\mathrm{coNP}$, then $\mathrm{NP} = \mathrm{coNP}$, which is believed false.

**Theorem 7.3** (Ladner, 1975). If $\mathrm{P} \ne \mathrm{NP}$, then there exist problems in $\mathrm{NP} \setminus \mathrm{P}$ that are not $\mathrm{NP}$-complete.

These are the **$\mathrm{NP}$-intermediate** problems; factoring and graph isomorphism are the usual candidates. Ladner's theorem is existential — it does not exhibit a natural intermediate problem.

### 7.11 NP-completeness

Reductions convert one hardness result into another. If $L_1$ is $\mathrm{NP}$-hard and $L_1 \le_{\mathrm{p}} L_2$, then $L_2$ is $\mathrm{NP}$-hard: any algorithm for $L_2$ decides $L_1$ with polynomial overhead, and every problem in $\mathrm{NP}$ reduces to $L_1$ and then to $L_2$. To prove a new problem $L$ $\mathrm{NP}$-complete one therefore

1. shows $L \in \mathrm{NP}$ (exhibit a short certificate and a polynomial-time verifier);
2. chooses a known $\mathrm{NP}$-complete problem $L_0$ and constructs a polynomial-time reduction $L_0 \le_{\mathrm{p}} L$.

The direction is the most common error: reducing $L$ *to* a known hard problem proves nothing about $L$.

**Theorem 7.4** (Cook 1971; Levin 1973). $\mathrm{SAT}$ — the set of satisfiable Boolean formulas in conjunctive normal form — is $\mathrm{NP}$-complete.

*Proof idea.* $\mathrm{SAT} \in \mathrm{NP}$ because a satisfying assignment is a certificate checkable in linear time. For hardness, let $L \in \mathrm{NP}$ be decided by a nondeterministic machine in time $p(n)$. For each input $x$ one writes a CNF formula $\varphi_x$ whose variables describe the tape contents, head position and state at each of the $p(n)$ time steps, and whose clauses assert that the computation starts correctly, that every step follows the transition relation, and that the machine accepts. The formula has $O(p(n)^2)$ variables and clauses and is computable in polynomial time, and it is satisfiable exactly when the machine accepts $x$. Hence $L \le_{\mathrm{p}} \mathrm{SAT}$. $\blacksquare$

The formula in that proof is a *circuit-to-CNF* encoding of a computation; it is the prototype of every later reduction.

**$\mathrm{3SAT}$** is the special case in which every clause has exactly three literals. It is $\mathrm{NP}$-complete: $\mathrm{SAT} \le_{\mathrm{p}} \mathrm{3SAT}$ by splitting a clause $(l_1 \vee \dots \vee l_k)$ with $k > 3$ into $k-2$ clauses using fresh variables $y_1,\dots,y_{k-3}$,

$$(l_1 \vee l_2 \vee y_1)\,(\neg y_1 \vee l_3 \vee y_2)\cdots(\neg y_{k-3} \vee l_{k-1} \vee l_k),$$

which is satisfiable for exactly the assignments that satisfy the original clause; clauses of length $1$ and $2$ are padded with a literal repeated. The construction is polynomial and preserves satisfiability in both directions.

**Theorem 7.5.** $\mathrm{CLIQUE} = \{(G,k) : G \text{ has a clique of size } k\}$ is $\mathrm{NP}$-complete.

*Membership.* A certificate is a list of $k$ vertices; checking that they are pairwise adjacent takes $O(k^2) \le O(V^2)$ time.

*Hardness.* Reduce $\mathrm{3SAT}$ to $\mathrm{CLIQUE}$. Let $\varphi = C_1 \wedge \dots \wedge C_m$ be a 3-CNF formula over variables $x_1,\dots,x_r$. Create one vertex for each literal occurrence, so $3m$ vertices, labelled by their clause and their literal. Join two vertices by an edge exactly when they lie in **different clauses** and their literals are **not complementary** (not $x_i$ and $\neg x_i$). The graph has $3m$ vertices and $O(m^2)$ edges and is built in polynomial time. Set $k = m$.

*($\Rightarrow$)* If $\varphi$ is satisfied by an assignment $\alpha$, choose in each clause one literal true under $\alpha$. These $m$ literals lie in distinct clauses and no two are complementary (both are true under $\alpha$), so the corresponding vertices form a clique of size $m$.

*($\Leftarrow$)* If the graph has a clique of size $m$, it contains at most one vertex per clause (no edges inside a clause) and there are exactly $m$ clauses, so exactly one vertex per clause. No two chosen literals are complementary, so the partial assignment that sets all of them to true is consistent and can be extended to all variables; every clause then contains a true literal, so $\varphi$ is satisfiable. $\blacksquare$

Section 9.8 carries out the construction on a concrete formula and on an unsatisfiable one.

| Problem | Statement | Reduction used classically |
|---|---|---|
| $\mathrm{SAT}$ | is a CNF formula satisfiable? | Cook–Levin (from any $L \in \mathrm{NP}$) |
| $\mathrm{3SAT}$ | is a 3-CNF formula satisfiable? | $\mathrm{SAT} \le_{\mathrm{p}} \mathrm{3SAT}$ |
| $\mathrm{CLIQUE}$ | has $G$ a clique of size $k$? | $\mathrm{3SAT} \le_{\mathrm{p}} \mathrm{CLIQUE}$ |
| $\mathrm{INDEPENDENT}$-$\mathrm{SET}$ | has $G$ an independent set of size $k$? | $\mathrm{CLIQUE}$ on the complement graph |
| $\mathrm{VERTEX}$-$\mathrm{COVER}$ | has $G$ a vertex cover of size $k$? | complement of an independent set |
| $\mathrm{HAMILTONIAN}$-$\mathrm{CYCLE}$ | has $G$ a cycle through every vertex? | $\mathrm{3SAT} \le_{\mathrm{p}} \mathrm{HAMILTONIAN}$-$\mathrm{CYCLE}$ |
| $\mathrm{TSP}$ (decision) | is there a tour of length $\le L$? | $\mathrm{HAMILTONIAN}$-$\mathrm{CYCLE} \le_{\mathrm{p}} \mathrm{TSP}$ |
| $\mathrm{SUBSET}$-$\mathrm{SUM}$ | is there a subset summing to $T$? | $\mathrm{3SAT} \le_{\mathrm{p}} \mathrm{SUBSET}$-$\mathrm{SUM}$ |
| $3$-$\mathrm{COLORING}$ | can $G$ be coloured with 3 colours? | $\mathrm{3SAT} \le_{\mathrm{p}} 3$-$\mathrm{COLORING}$ |

Karp's 1972 paper exhibited twenty-one such problems, and thousands are known today. They are all equivalent under polynomial-time reductions: a polynomial-time algorithm for any one of them would give one for all.

### 7.12 What "hard" means in practice

$\mathrm{NP}$-hardness is a **worst-case** statement about a whole problem, and it does not imply that every instance is difficult. Four honest qualifications:

* **Instance structure.** Industrial $\mathrm{SAT}$ instances arising from hardware verification or planning often have millions of variables and are solved in seconds by conflict-driven clause-learning solvers, even though random 3-CNF formulas near the ratio $m/n \approx 4.267$ are hard for every known method. Friedgut proved in 1999 that random 3-$\mathrm{SAT}$ has a sharp satisfiability threshold, but its exact location is still open.
* **Approximation.** For an optimisation problem one can ask for a solution within a factor $\rho$ of optimal. $\mathrm{VERTEX}$-$\mathrm{COVER}$ has a 2-approximation (take a maximal matching and both endpoints of every matched edge); metric $\mathrm{TSP}$ has the 1.5-approximation of Christofides; set cover has an $H_n$-approximation. Some problems admit no such scheme: the PCP theorem implies that $\mathrm{MAX}$-$3\mathrm{SAT}$ cannot be approximated within $7/8 + \varepsilon$ unless $\mathrm{P} = \mathrm{NP}$ (Håstad, 2001), and set cover cannot be approximated within $(1-\varepsilon)\ln n$ (Feige, 1998).
* **Parameterisation.** An algorithm running in $O(2^k \cdot n)$ for a parameter $k$ is practical when $k$ is small even if $n$ is large. This is **fixed-parameter tractability**; vertex cover, for instance, admits an FPT algorithm parameterised by the solution size.
* **Exact exponential algorithms.** $\mathrm{3SAT}$ can be solved in about $1.3^n$ time by branching, far better than $2^n$; the **Exponential Time Hypothesis** of Impagliazzo and Paturi (2001) conjectures that no $2^{o(n)}$ algorithm exists, which would make such improvements impossible in the limit.

None of this contradicts $\mathrm{NP}$-hardness: a hardness theorem forbids one algorithm (polynomial-time, exact, worst-case), not every algorithm, approximation or heuristic. Conversely, a heuristic that works on your instances is not a theorem — which is why the distinction between "fast in practice" and "polynomial-time" is maintained so carefully.

### 7.13 Computability and the halting problem

Complexity theory asks how much time a solution needs. Computability theory asks whether a solution exists at all, and the answer for some perfectly well-posed problems is no.

The counting argument is immediate. Programs are finite strings over a finite alphabet, hence countable; languages are subsets of $\{0,1\}^*$, hence uncountable (Cantor). So almost every language is undecidable — there are not enough programs to decide them all. Exhibiting a *natural* undecidable problem is the content of the next theorem.

**Theorem 7.6** (Turing, 1936). The **halting problem**

$$H = \{\langle P, x\rangle : P \text{ is a program that halts on input } x\}$$

is undecidable.

*Proof.* Suppose a program $H$ decides $H$: on input $\langle P,x\rangle$ it prints "halts" or "loops" and always terminates. Construct a program $D$ that takes a program $P$ as input and does the following: run $H$ on $\langle P, P\rangle$; if $H$ says "halts", loop forever; if $H$ says "loops", halt. Now ask whether $D$ halts on input $D$.

* If $D$ halts on $D$, then $H$ said "loops" on $\langle D,D\rangle$, so by definition of $H$ the program $D$ loops on $D$ — contradiction.
* If $D$ loops on $D$, then $H$ said "halts" on $\langle D,D\rangle$, so by definition of $H$ the program $D$ halts on $D$ — contradiction.

Both cases are impossible, so no such $H$ exists. $\blacksquare$

The argument is diagonal: $D$ is designed to disagree with the hypothetical decider on the diagonal case $\langle P,P\rangle$, exactly as Cantor's diagonal number differs from every listed real.

Three consequences deserve emphasis.

1. **The halting set is recognisable but not decidable.** A program that simulates $P$ on $x$ and accepts if it halts is a *semi-decision procedure*: it says "yes" correctly but may run forever on a "no" instance. The halting problem is recursively enumerable, and its complement is not.
2. **Rice's theorem.** Every non-trivial semantic property of programs is undecidable: if a property holds for some programs and fails for others, and depends only on the input–output behaviour, no algorithm decides it. "Does this program ever divide by zero?", "Is its output always positive?", "Is it equivalent to this other program?" are all undecidable in general.
3. **Verification tools are necessarily incomplete.** A static analyser can be sound (never misses a bug) or complete (never reports a false alarm), not both, for any property rich enough to encode halting. Real tools choose soundness with false positives, or completeness on a restricted subset of programs.

The undecidability barrier is not about $\mathrm{P}$ versus $\mathrm{NP}$: it is a different, absolute wall. It also explains why complexity theory is stated for total functions and decidable languages — otherwise every statement about "running time" would have to hedge on inputs where the algorithm never stops.

## 8. Formulas and Properties

This section states the results used above with their hypotheses and proofs. Throughout, $f$ and $g$ are functions $\mathbb{N} \to \mathbb{R}$ with $g(n) > 0$ for all sufficiently large $n$, and complexity results refer to the RAM model of Definition 5.1.

**Theorem 8.1** (Limit test). Suppose $\lim_{n\to\infty} f(n)/g(n) = L \in [0,\infty]$. Then:

1. $L < \infty \Rightarrow f = O(g)$;
2. $L > 0 \Rightarrow f = \Omega(g)$;
3. $0 < L < \infty \Rightarrow f = \Theta(g)$;
4. $L = 0 \Rightarrow f = o(g)$;
5. $L = \infty \Rightarrow g = o(f)$.

*Proof.* (1) If $L < \infty$, then for all sufficiently large $n$, $f(n)/g(n) \le L + 1$, so $f(n) \le (L+1)g(n)$; take $c = L+1$. (2) If $L > 0$, then eventually $f(n)/g(n) \ge L/2 > 0$, so $f(n) \ge (L/2)g(n)$. If $L = \infty$, then for every $c$ eventually $f/g > c$, which is the definition of $\omega$ and hence of $\Omega$. (3) follows from (1) and (2). (4) For every $c > 0$ eventually $f/g < c$, i.e. $f < cg$. (5) Apply (4) to $g/f$, whose limit is $0$. $\blacksquare$

The converse of (1) fails: $f = O(g)$ does not imply that $f/g$ has a limit (take $f(n) = 1 + (-1)^n$ and $g \equiv 1$). The limit test is a convenience, not a definition.

**Theorem 8.2** (Composition of reductions). If $L_1 \le_{\mathrm{p}} L_2$ and $L_2 \le_{\mathrm{p}} L_3$, then $L_1 \le_{\mathrm{p}} L_3$. Consequently, if some $\mathrm{NP}$-hard problem reduces to $L$, then $L$ is $\mathrm{NP}$-hard.

*Proof.* Let $f$ reduce $L_1$ to $L_2$ in time $O(n^a)$ and $g$ reduce $L_2$ to $L_3$ in time $O(n^b)$. Then $x \in L_1 \iff f(x) \in L_2 \iff g(f(x)) \in L_3$. The map $g \circ f$ is computable in time $O(n^{ab})$: computing $f(x)$ takes $O(n^a)$ and produces an output of length $O(n^a)$ (a machine running in time $t$ cannot write more than $t$ symbols), and $g$ on that output takes $O((n^a)^b) = O(n^{ab})$. Composition of two polynomial-time maps is polynomial-time. For the consequence: every $L' \in \mathrm{NP}$ satisfies $L' \le_{\mathrm{p}} L_1 \le_{\mathrm{p}} L$, so $L' \le_{\mathrm{p}} L$, which is the definition of $\mathrm{NP}$-hardness. $\blacksquare$

**Theorem 8.3** (Algebra of bounds). For non-negative functions:

1. $f = O(g)$ and $g = O(h)$ imply $f = O(h)$ (transitivity);
2. $f = O(g)$ and $f' = O(g')$ imply $f + f' = O(g + g')$ and $f f' = O(g g')$;
3. $\max(f,g) = \Theta(f+g)$;
4. $f = \Theta(g) \iff f = O(g)$ and $g = O(f)$.

*Proof.* (1) $f \le c_1 g \le c_1c_2 h$ for $n \ge \max(n_1,n_2)$. (2) $f + f' \le c g + c' g' \le \max(c,c')(g+g')$, and $ff' \le cc'gg'$. (3) Since $f, g \le \max(f,g)$, we get $f + g \le 2\max(f,g)$, while $\max(f,g) \le f+g$; so $\frac12(f+g) \le \max(f,g) \le f+g$. (4) is immediate from Definition 5.3. $\blacksquare$

Part (3) is the formal justification of "the running time of a sequence of phases is the largest order, not the sum".

**Theorem 8.4** (The growth hierarchy). For every fixed $\varepsilon > 0$ and every fixed integer $k \ge 0$:

$$\log n = o(n^{\varepsilon}), \qquad n^k = o(2^n), \qquad 2^n = o(n!).$$

*Proof.* Write $n = 2^{t}$. Then $\log_2 n = t$ and $n^{\varepsilon} = 2^{\varepsilon t}$, so $\log_2 n / n^{\varepsilon} = t/2^{\varepsilon t} \to 0$ because exponentials dominate polynomials.

For the second, $2^n = \sum_{j=0}^{n}\binom{n}{j} \ge \binom{n}{k+1}$, and for $n \ge 2k+2$ each of the $k+1$ factors $n, n-1, \dots, n-k$ is at least $n/2$, so

$$\binom{n}{k+1} = \frac{n(n-1)\cdots(n-k)}{(k+1)!} \ge \frac{(n/2)^{k+1}}{(k+1)!}.$$

Hence $\dfrac{n^k}{2^n} \le \dfrac{2^{k+1}(k+1)!}{n} \to 0$.

For the third, for $n \ge 4$,

$$\frac{n!}{2^n} = \prod_{j=1}^{n}\frac{j}{2} = \frac12 \cdot 1 \cdot \frac32 \cdot \prod_{j=4}^{n}\frac{j}{2} \ge \frac34 \cdot 2^{\,n-3} \longrightarrow \infty,$$

since each factor with $j \ge 4$ is at least $2$. $\blacksquare$

**Theorem 8.5** (Insertion sort). On inputs of size $n$, insertion sort performs exactly $\sum_{i=2}^{n} c_i$ comparisons, where $c_i$ is the number of entries among $A[1..i-1]$ that exceed the key $A[i]$, plus possibly one final comparison when the scan stops at a non-zero index. In particular the worst case is exactly $n(n-1)/2$ comparisons and $\Theta(n^2)$ moves, and the best case is $n-1$ comparisons.

*Proof.* The inner loop compares the key with $A[j]$ for $j = i-1, i-2, \dots$ and stops either when $A[j] \le \textit{key}$ (one comparison that fails) or when $j = 0$ (the condition $j \ge 1$ fails and no further comparison is made). Every entry greater than the key is shifted exactly once, so the count is as claimed. The maximum $c_i = i-1$ is attained when the first $i$ entries are in decreasing order, and summing gives $\sum_{i=2}^n (i-1) = n(n-1)/2$. The minimum is attained on a sorted array, where each inner loop fails immediately. $\blacksquare$

**Theorem 8.6** (Merge sort). Merging two sorted lists of total length $m$ needs at most $m-1$ comparisons. Hence merge sort uses at most $n\lceil \lg n\rceil$ comparisons and runs in $\Theta(n\log n)$ time. If $n = 2^k$, the worst case is exactly $n\lg n - n + 1$ comparisons.

*Proof.* Each comparison outputs one element, and once one list is exhausted the remaining elements are copied without comparison; at most $m-1$ comparisons can occur before that. The recursion tree has depth $\lceil\lg n\rceil$; the subarrays at depth $d$ are disjoint and total length $n$, and merging them costs at most their total length, so each level costs at most $n$ comparisons. The recurrence $T(n) = 2T(n/2) + \Theta(n)$ gives $\Theta(n\log n)$.

For the exact count when $n = 2^k$, the worst case satisfies $T(n) = 2T(n/2) + (n-1)$ with $T(1) = 0$. Dividing by $n$: with $S(k) = T(2^k)/2^k$, the recurrence becomes $S(k) = S(k-1) + 1 - 2^{-k}$, so $S(k) = k - 1 + 2^{-k}$ and $T(2^k) = k2^k - 2^k + 1 = n\lg n - n + 1$. $\blacksquare$

**Theorem 8.7** (Quicksort). With a fixed first-or-last pivot rule, quicksort performs $\Theta(n^2)$ comparisons in the worst case and $\Theta(n\log n)$ in the best case. On a sorted array with the last element as pivot the worst case is exactly $n(n-1)/2$ comparisons.

*Proof.* Partitioning a subarray of length $m$ uses exactly $m-1$ comparisons. A pivot that is always extreme gives $T(n) = T(n-1) + (n-1)$, $T(1) = 0$, hence $T(n) = \sum_{m=2}^{n}(m-1) = n(n-1)/2$. This is realised by the sorted array with the last element as pivot, since every partition then splits off a single element. Balanced partitions give $T(n) = 2T(n/2) + (n-1)$, which is $\Theta(n\log n)$ by case 2 of the master theorem. $\blacksquare$

**Theorem 8.8** (Expected comparisons of quicksort). With uniformly random pivots, the expected number of comparisons performed by quicksort on $n$ distinct keys is

$$\mathbb{E}[C_n] = 2(n+1)H_n - 4n = \Theta(n\log n),$$

where $H_n = \sum_{k=1}^{n} 1/k$.

*Proof.* Let $z_1 < z_2 < \dots < z_n$ be the keys in sorted order and let $X_{ij}$, for $i < j$, be the indicator of the event that $z_i$ and $z_j$ are compared at some point. Then $C_n = \sum_{i<j} X_{ij}$.

*Claim: $\Pr(X_{ij} = 1) = 2/(j-i+1)$.* Consider the set $Z = \{z_i, \dots, z_j\}$ of $j-i+1$ keys. Two keys are compared only when one of them is the pivot of the subarray containing both; once a pivot is chosen, that pivot is separated from the rest forever. So $z_i$ and $z_j$ are compared exactly when the first key of $Z$ chosen as a pivot is $z_i$ or $z_j$. Under random pivoting every key of $Z$ is equally likely to be the first chosen from $Z$, so the probability is $2/|Z| = 2/(j-i+1)$.

By linearity of expectation (no independence is needed),

$$\mathbb{E}[C_n] = \sum_{1 \le i < j \le n}\frac{2}{j-i+1} = \sum_{d=1}^{n-1}(n-d)\frac{2}{d+1}.$$

Substituting $k = d+1$:

$$\mathbb{E}[C_n] = \sum_{k=2}^{n}\frac{2(n+1-k)}{k} = 2(n+1)\sum_{k=2}^{n}\frac1k - 2(n-1) = 2(n+1)(H_n - 1) - 2n + 2 = 2(n+1)H_n - 4n.$$

Since $H_n = \ln n + \gamma + O(1/n) = \Theta(\log n)$, the expectation is $\Theta(n\log n)$; more precisely $2n\ln n + O(n) = \frac{2}{\ln 2}n\lg n + O(n) \approx 1.39\,n\lg n$. $\blacksquare$

**Theorem 8.9** (Binary search). On a sorted array of $n \ge 1$ elements, binary search performs at most $\lfloor \lg n\rfloor + 1$ comparisons, and this bound is attained.

*Proof.* The recurrence is $T(0) = 0$ and $T(n) = T(\lfloor n/2\rfloor) + 1$. The claim is $T(n) = \lfloor\lg n\rfloor + 1$ for $n \ge 1$. For $n = 1$: $T(1) = T(0)+1 = 1 = \lfloor \lg 1\rfloor + 1$. For $n \ge 2$, using $\lfloor\lg\lfloor n/2\rfloor\rfloor = \lfloor\lg(n/2)\rfloor = \lfloor\lg n\rfloor - 1$,

$$T(n) = T(\lfloor n/2\rfloor) + 1 = \bigl(\lfloor\lg(n/2)\rfloor + 1\bigr) + 1 = \lfloor\lg n\rfloor + 1.$$

Attainment: searching for the last element of the array (or for a value larger than all elements) always follows the longer branch. $\blacksquare$

| Result | Statement | Section |
|---|---|---|
| Decision-tree bound | comparison sorting needs $\lceil\lg(n!)\rceil = \Omega(n\log n)$ comparisons | 7.8 |
| Insertion sort, worst | exactly $n(n-1)/2$ comparisons | 8.5 |
| Merge sort | $\le n\lceil\lg n\rceil$; exactly $n\lg n - n + 1$ when $n = 2^k$ | 8.6 |
| Quicksort, worst | exactly $n(n-1)/2$ on a sorted array with an end pivot | 8.7 |
| Quicksort, expected | $2(n+1)H_n - 4n = \Theta(n\log n)$ | 8.8 |
| Binary search | exactly $\lfloor\lg n\rfloor + 1$ comparisons | 8.9 |
| $\mathrm{P} \subseteq \mathrm{NP} \subseteq \mathrm{EXP}$ | inclusions; both believed strict | 7.10 |
| Cook–Levin | $\mathrm{SAT}$ is $\mathrm{NP}$-complete | 7.11 |
| Halting problem | undecidable | 7.13 |

<!-- CHUNK-END -->
