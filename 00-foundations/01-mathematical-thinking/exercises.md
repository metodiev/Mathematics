# Exercises: Mathematical Thinking and Problem Solving

> Companion to the [tutorial](README.md). Solutions are in [solutions.md](solutions.md).

Work on paper, not in your head. For each problem, write down (i) what is given, (ii) what is asked,
(iii) the strategy you are trying, before you compute anything. If you are stuck for more than twenty
minutes, read only the first line of the corresponding solution and continue on your own.

Problems are numbered continuously so that the solutions file mirrors them exactly. Level labels
indicate the amount of synthesis required, not the length of the answer.

## Beginner

**1.** Compute $1 + 2 + 3 + \cdots + 60$ using the pairing method. State which algebraic property of
addition makes the pairing legitimate, and check your answer with the formula from the tutorial.

**2.** Prove that $n(n+1)$ is even for every integer $n$. Use a case distinction on the parity of $n$,
and say explicitly which parity lemma you use in each case.

**3.** Find a counterexample to the statement: "For every integer $n \ge 2$, the number $2^n - 1$ is
prime." Find the smallest such $n$ and factor $2^n - 1$.

**4.** A number machine performs, in order: multiply by $3$; add $5$; double; subtract $4$. The output
is $30$. Work backwards to find the input, then verify by running the machine forwards.

**5.** Consider the claim "for every integer $n \ge 0$, the number $n^2 + n + 41$ is prime".

(a) Verify the claim for $n = 0, 1, 2, 3$.
(b) Evaluate it at $n = 40$ and exhibit a factorization.
(c) Explain, without further computation, why $n = 41$ also gives a composite number.

**6.** Compute $1 + 3 + 5 + \cdots + 49$ using the theorem on sums of odd numbers. Then verify the
result by a second method of your choice.

**7.** Decide which is larger, $2^{100}$ or $10^{30}$, without computing either number exactly. Quote
the estimate that you use and justify it.

**8.** A student writes $49 \times 51 = 2399$. Find the error using an algebraic identity, and give the
correct value. Which of the two values passes the "last digit" test?

**9.** (a) Is the sum of seven odd integers odd or even? (b) Is their product odd or even? Justify both
answers with the parity lemmas, and state whether either answer depends on the particular odd integers
chosen.

**10.** For the statement "if $n$ is divisible by $4$, then $n$ is even":

(a) write its converse and its contrapositive;
(b) decide which of the three statements (original, converse, contrapositive) are true, giving a proof
or a counterexample for each.

**11.** Can a $5 \times 5$ board be tiled by $1 \times 2$ dominoes? Answer with a colour count, and
state precisely which quantity is invariant.

**12.** Estimate the number of seconds in a year to one significant figure, using $365$ days. Compare
your estimate with $\pi \times 10^{7}$ and comment on the agreement.

## Intermediate

**13.** Prove that $\sum_{k=1}^{n} 2k = n(n+1)$ for every integer $n \ge 1$ in two different ways: one
using the theorem on $1 + 2 + \cdots + n$, and one by a direct pairing or induction argument.

**14.** Prove that if $n$ is an odd integer, then $8$ divides $n^2 - 1$. Show where the parity of
$k(k+1)$ is used.

**15.** A number $x$ is processed as follows: double it, add $7$, take the non-negative square root,
subtract $1$; the result is $4$. Find every real $x$ that produces this result. Explain why squaring
does not introduce an extraneous solution here, although squaring is not injective on $\mathbb{R}$.

**16.** The numbers $1, 2, \dots, 10$ are written on a board. A move erases two numbers $a, b$ and
writes $a + b$.

(a) Prove that the final number is $55$, regardless of the order of the moves.
(b) Now suppose the move instead erases $a, b$ and writes $|a - b|$. Is the final number determined?
Prove what you can (for instance, a parity statement) and give two different play sequences with
different final numbers.

**17.** Show that the equation $x^2 + y^2 = 1234567$ has no solutions in integers. State the theorem
about squares modulo $4$ that you use.

**18.** At a party, each of nine people claims to have shaken hands with exactly three other people.
Prove that this is impossible. Name the general theorem you are using and check its hypotheses.

**19.** (a) Prove that if $n^2$ is even then $n$ is even.
(b) Explain the role of this statement in the proof that $\sqrt{2}$ is irrational, and what would go
wrong if it were false.

**20.** Find all integers $n$ such that $n^2 + n + 1$ is a perfect square. Justify completeness: show
that no other $n$ works.

**21.** A "proof" runs as follows. Let $a = b$. Then $a^2 = ab$, so $a^2 - b^2 = ab - b^2$, hence
$(a-b)(a+b) = b(a-b)$, and dividing by $a - b$ gives $a + b = b$, so $2b = b$ and therefore $2 = 1$.
Identify the flaw precisely, and state which hypothesis a correct argument would need.

**22.** Estimate the number of piano tuners in a city of three million people. Write down every
assumption, compute a central estimate, and give a plausible range. Explain which assumption dominates
the uncertainty.

## Advanced

**23.** Prove that among any five integers there exist three whose sum is divisible by $3$. (Consider
the residues modulo $3$ and use the pigeonhole principle, including the case where the five integers
occupy at most two residue classes.)

**24.** Prove that a $6 \times 6$ board cannot be tiled by $1 \times 4$ bars. Use the colouring in
which cell $(i,j)$ receives colour $(i+j) \bmod 4$, count the colours on the board, and explain why
every bar covers one cell of each colour.

**25.** Prove that $\sqrt{3}$ is irrational. Follow the structure of the $\sqrt{2}$ proof, but replace
the parity argument by a divisibility-by-$3$ argument, and state the lemma you need about squares
divisible by $3$.

**26.** Prove that $6$ divides $n^3 - n$ for every integer $n$. Use a factorization and explain why both
$2$ and $3$ divide the product.

**27.** Let $n \ge 1$. Prove that among any $n+1$ integers chosen from $\{1, 2, \dots, 2n\}$, there are
two such that one divides the other. (Write each integer as $2^a$ times an odd number.)

**28.** Prove that for every integer $n \ge 1$,

$$
\sum_{k=1}^{n} \frac{1}{k^2} < 2.
$$

Use the inequality $\frac{1}{k^2} < \frac{1}{k(k-1)}$ for $k \ge 2$ and a telescoping sum. Explain why
the strict inequality survives the summation.

**29.** Prove that for every integer $n \ge 2$, the number

$$
H_n = 1 + \frac{1}{2} + \frac{1}{3} + \cdots + \frac{1}{n}
$$

is not an integer. Let $2^m$ be the largest power of $2$ not exceeding $n$, multiply $H_n$ by
$\operatorname{lcm}(1, 2, \dots, n)$, and examine the $2$-adic parity of the terms.

## Challenge

**30.** Prove that the equation $x^2 + y^2 = 3z^2$ has no solution in integers with $x, y, z$ not all
zero. Use arithmetic modulo $3$ and an infinite descent: from a solution, construct a smaller one.

**31.** A pancake is cut by $n$ straight lines, no two of them parallel and no three passing through a
single point. Let $P(n)$ be the number of pieces.

(a) Compute $P(0), P(1), P(2), P(3), P(4)$ by drawing.
(b) Explain why the $n$-th line increases the number of pieces by exactly $n$.
(c) Prove by induction that $P(n) = \dfrac{n^2 + n + 2}{2}$.

**32.** Prove that among any six people there are either three mutual acquaintances or three mutual
strangers (acquaintance is symmetric). This is the statement $R(3,3) = 6$.

**33.** Prove that for every integer $m \ge 0$,

$$
H_{2^m} = 1 + \frac{1}{2} + \frac{1}{3} + \cdots + \frac{1}{2^m} \ge 1 + \frac{m}{2},
$$

and deduce that the harmonic series diverges: for every real bound $B$ there is an $n$ with $H_n > B$.
