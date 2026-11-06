# Mathematical Induction — Solutions

> [Mathematical Induction](README.md) · Solutions to the 36 problems in [exercises.md](exercises.md)

Each solution states the strategy, then carries out the base case and the inductive step with every significant algebraic move displayed. Proof problems receive complete proofs, and every numerical claim is checked at small values before the induction is written down.

## Beginner

**1.** *Strategy: follow the five-part template literally. The only content is the algebraic identity $(k+1)^2 = k^2 + 2k + 1$.*

**Claim.** For every $n \ge 1$, $\;\sum_{k=1}^{n}(2k-1) = n^2$.

**Base case** $n = 1$: the left side is $2\cdot 1 - 1 = 1$; the right side is $1^2 = 1$. ✓

**Inductive hypothesis.** Let $k \ge 1$ and assume $\sum_{j=1}^{k}(2j-1) = k^2$.

**Goal.** Show $\sum_{j=1}^{k+1}(2j-1) = (k+1)^2$.

**Step.** Splitting off the last term,

$$\sum_{j=1}^{k+1}(2j-1) = \sum_{j=1}^{k}(2j-1) + \bigl(2(k+1)-1\bigr) = k^2 + (2k+1) = (k+1)^2 .$$

The second equality uses the inductive hypothesis; the third is the binomial expansion. The hypothesis is used exactly once, at the moment the sum of $k$ terms is replaced by $k^2$.

**Conclusion.** By the principle of induction, the formula holds for every $n \ge 1$. $\square$

*Check.* $n = 2$: $1 + 3 = 4 = 2^2$ ✓; $n = 3$: $1+3+5 = 9 = 3^2$ ✓.

**2.** *Strategy: same template; the only work is factoring the cubic-free expression $2k^2 + 3k + 1$.*

**Claim.** For every $n \ge 1$, $\;\sum_{k=1}^{n}(4k-3) = n(2n-1)$.

**Base case** $n = 1$: left $= 1$, right $= 1\cdot 1 = 1$. ✓

**Inductive hypothesis.** $\sum_{j=1}^{k}(4j-3) = k(2k-1)$ for some $k \ge 1$.

**Goal.** $\sum_{j=1}^{k+1}(4j-3) = (k+1)(2k+1)$.

**Step.**

$$\sum_{j=1}^{k+1}(4j-3) = k(2k-1) + \bigl(4(k+1)-3\bigr) = 2k^2 - k + 4k + 1 = 2k^2 + 3k + 1 = (k+1)(2k+1).$$

Indeed $(k+1)(2k+1) = 2k^2 + k + 2k + 1 = 2k^2 + 3k + 1$. $\square$

*Check.* $n = 3$: $1 + 5 + 9 = 15$ and $3\cdot 5 = 15$ ✓.

**3.** *Strategy: this is Theorem 7.3.1 with $r = 3$; the step multiplies by $3$ rather than by a symbolic $r$.*

**Claim.** For every $n \ge 1$, $\;\sum_{k=0}^{n-1}3^k = \dfrac{3^n-1}{2}$.

**Base case** $n = 1$: left $= 3^0 = 1$; right $= (3-1)/2 = 1$. ✓

**Inductive hypothesis.** $\sum_{j=0}^{k-1}3^j = \dfrac{3^k-1}{2}$ for some $k \ge 1$.

**Goal.** $\sum_{j=0}^{k}3^j = \dfrac{3^{k+1}-1}{2}$.

**Step.**

$$\sum_{j=0}^{k}3^j = \frac{3^k-1}{2} + 3^k = \frac{3^k - 1 + 2\cdot 3^k}{2} = \frac{3\cdot 3^k - 1}{2} = \frac{3^{k+1}-1}{2}. \qquad \square$$

*Check.* $n = 3$: $1 + 3 + 9 = 13$ and $(27-1)/2 = 13$ ✓.

**4.** *Strategy: the standard divisibility device. Expand $(k+1)^3-(k+1)$ and force $(k^3-k)$ to appear; the leftover must be a multiple of $3$.*

*Values.* $n=1$: $0$; $n=2$: $6$; $n=3$: $24$; $n=4$: $60$. All divisible by $3$. ✓

**Claim.** $3 \mid n^3-n$ for every $n \ge 1$.

**Base case** $n = 1$: $1^3 - 1 = 0 = 3\cdot 0$. ✓

**Inductive hypothesis.** $3 \mid k^3-k$ for some $k \ge 1$, say $k^3 - k = 3m$.

**Step.**

$$(k+1)^3 - (k+1) = k^3 + 3k^2 + 3k + 1 - k - 1 = (k^3 - k) + 3k^2 + 3k = (k^3-k) + 3k(k+1).$$

The first term is $3m$ by hypothesis; the second is $3$ times the integer $k(k+1)$. Hence

$$(k+1)^3-(k+1) = 3\bigl(m + k(k+1)\bigr),$$

a multiple of $3$. $\square$

*Remark.* The same computation also gives $6 \mid n^3-n$, because $k(k+1)$ is even; Exercise 14 is the close relative $6 \mid n^3+5n$.

**5.** *Strategy: write $3^{2(k+1)} = 9\cdot 3^{2k}$ and force the old expression to appear by subtracting and adding $1$.*

*Values.* $n=1$: $9-1 = 8$; $n=2$: $81-1 = 80 = 8\cdot 10$; $n=3$: $729-1 = 728 = 8\cdot 91$. ✓

**Claim.** $8 \mid 3^{2n}-1$ for every $n \ge 1$.

**Base case** $n = 1$: $3^2 - 1 = 8$. ✓

**Inductive hypothesis.** $3^{2k}-1 = 8m$ for some integer $m$, with $k \ge 1$.

**Step.**

$$3^{2(k+1)} - 1 = 9\cdot 3^{2k} - 1 = 9\bigl(3^{2k}-1\bigr) + 9 - 1 = 9\cdot 8m + 8 = 8(9m+1). \qquad \square$$

**6.** *Strategy: an inequality with a threshold at $1$. The step only needs $k \ge 1$, so a base case at $n=1$ is enough.*

**Claim.** $2^n > n$ for every $n \ge 1$.

**Base case** $n = 1$: $2 > 1$. ✓

**Inductive hypothesis.** $2^k > k$ for some $k \ge 1$.

**Step.**

$$2^{k+1} = 2\cdot 2^k > 2k \ge k+1,$$

where $2k \ge k+1$ is equivalent to $k \ge 1$. Both inequalities are strict or non-strict as required, so $2^{k+1} > k+1$. $\square$

**7.** *Strategy: direct induction first; the partial-fraction identity gives a telescoping proof as a cross-check.*

**Claim.** $\displaystyle\sum_{k=1}^{n}\frac{1}{k(k+1)} = \frac{n}{n+1}$ for every $n \ge 1$.

**Base case** $n = 1$: $\frac{1}{1\cdot 2} = \frac12 = \frac{1}{2}$. ✓

**Inductive hypothesis.** $\sum_{j=1}^{k}\frac{1}{j(j+1)} = \frac{k}{k+1}$.

**Step.**

$$\sum_{j=1}^{k+1}\frac{1}{j(j+1)} = \frac{k}{k+1} + \frac{1}{(k+1)(k+2)} = \frac{k(k+2) + 1}{(k+1)(k+2)} = \frac{k^2+2k+1}{(k+1)(k+2)} = \frac{(k+1)^2}{(k+1)(k+2)} = \frac{k+1}{k+2}. \qquad \square$$

*Second method.* Since $\frac{1}{j(j+1)} = \frac1j - \frac{1}{j+1}$, the sum telescopes:

$$\sum_{j=1}^{n}\left(\frac1j - \frac1{j+1}\right) = 1 - \frac{1}{n+1} = \frac{n}{n+1}.$$

The telescoping proof is shorter but needs the partial-fraction identity; the induction needs only algebra. Both are complete proofs.

**8.** *Strategy: split the subsets according to whether they contain a fixed element, and count each class with the inductive hypothesis.*

**Claim.** A set with $n$ elements has exactly $2^n$ subsets, for every $n \ge 0$.

**Base case** $n = 0$: the empty set $\varnothing$ has exactly one subset, namely $\varnothing$, and $2^0 = 1$. ✓

**Inductive hypothesis.** Every set with $k$ elements has $2^k$ subsets.

**Step.** Let $S$ be a set with $k+1$ elements and fix $x \in S$. Put $S' = S\setminus\{x\}$, a set with $k$ elements. Every subset $T \subseteq S$ falls into exactly one of two classes:

* $x \notin T$: then $T \subseteq S'$, and there are $2^k$ such $T$ by the hypothesis;
* $x \in T$: then $T = \{x\} \cup U$ with $U \subseteq S'$, and $U \mapsto \{x\}\cup U$ is a bijection onto this class, so there are again $2^k$ such $T$.

The classes are disjoint (one contains $x$, the other does not) and exhaustive (every subset either contains $x$ or not). Hence $S$ has $2^k + 2^k = 2^{k+1}$ subsets. $\square$

*Check.* A two-element set $\{a,b\}$ has the subsets $\varnothing, \{a\}, \{b\}, \{a,b\}$: four, as predicted.

**9.** *Strategy: the step multiplies by $k+1$; the key observation is $k+1 \ge 2$.*

**Claim.** $n! \ge 2^{\,n-1}$ for every $n \ge 1$.

**Base case** $n = 1$: $1! = 1 = 2^0$. ✓

**Inductive hypothesis.** $k! \ge 2^{k-1}$ for some $k \ge 1$.

**Step.**

$$(k+1)! = (k+1)\,k! \ge (k+1)\,2^{k-1} \ge 2\cdot 2^{k-1} = 2^{k},$$

since $k + 1 \ge 2$. $\square$

*Equality.* At $n = 1$: $1 = 1$ ✓. At $n = 2$: $2! = 2 = 2^1$ ✓. For $n \ge 3$ both inequalities in the step are strict ($k+1 \ge 4 > 2$ once $k \ge 3$), so equality holds exactly for $n \in \{1,2\}$. Check: $3! = 6 > 4$ ✓.

**10.** *Strategy: the induction hypothesis is "$11$ divides $2^{10k}-1$"; the step factors $2^{10}$ out and corrects with $2^{10}-1 = 1023$, which is itself divisible by $11$.*

**Claim.** $11 \mid 2^{10n}-1$ for every $n \ge 1$.

**Base case** $n = 1$: $2^{10} - 1 = 1024 - 1 = 1023 = 11\cdot 93$. ✓

**Inductive hypothesis.** $2^{10k}-1 = 11m$ for some integer $m$.

**Step.**

$$2^{10(k+1)} - 1 = 2^{10}\cdot 2^{10k} - 1 = 2^{10}\bigl(2^{10k}-1\bigr) + \bigl(2^{10}-1\bigr) = 1024\cdot 11m + 1023 = 11(1024m + 93). \qquad \square$$

**11.** *Strategy: separate the two things a proof by induction must supply. Here the step is a valid theorem; the base case is missing.*

*Diagnosis.* The inductive step is **correct**: if $k^2+k$ were odd, then $(k+1)^2+(k+1) = (k^2+k) + 2(k+1)$ would indeed be odd. What is missing is the **base case**. And the claim is false: at $n = 1$, $n^2+n = 2$, which is even. Since no value of $n$ satisfies the hypothesis, the step is vacuously true and proves nothing.

*Why it looks convincing.* The algebra is right, the parity reasoning ("odd plus even is odd") is right, and the conclusion is written in the standard form. The error is an omission rather than a false statement, which is exactly the kind of error a template is designed to catch: writing "**Base case.**" as a heading forces the author to fill it in, and the attempt fails immediately at $n = 1$.

*Correct statement.* $n^2+n = n(n+1)$ is always even, because one of two consecutive integers is even. Parity alternates with period $2$, not with period $1$, so an induction with step $+1$ can never prove it; one would induct on $n$ with step $+2$, or prove it by cases. This is a useful warning: a true statement may still be false for the induction you are trying to run.

**12.** *Strategy: part (a) is pure template; part (b) is the algebra; part (c) shows how a strict inequality can fail at the base even when the weak one holds.*

**(a)** Claim: $n^2 \ge 2n$ for every $n \ge 2$.

* Base case: $n = 2$; verify $2^2 \ge 2\cdot 2$, i.e. $4 \ge 4$.
* Inductive hypothesis: for some $k \ge 2$, $k^2 \ge 2k$.
* Goal: $(k+1)^2 \ge 2(k+1)$.

**(b)** Using the hypothesis and then expanding,

$$(k+1)^2 = k^2 + 2k + 1 \ge 2k + 2k + 1 = 4k + 1 \ge 2k + 2,$$

where the last inequality is $2k \ge 1$, true for $k \ge 1$. So $(k+1)^2 \ge 2(k+1)$, and by induction the claim holds for all $n \ge 2$. $\square$

**(c)** For the strict claim $n^2 > 2n$, the base case $n = 2$ fails ($4 > 4$ is false), and the computation in (b) gives only $\ge$ at that point. The strict statement is true for $n \ge 3$: the base case $n = 3$ gives $9 > 6$ ✓, and the same step yields $(k+1)^2 \ge 4k+1 > 2k+2$ for $k \ge 1$. So the repair is to start the induction at $n = 3$. A single failing base case does not make a statement false for all $n$; it makes the chosen starting point wrong.

## Intermediate

**13.** *Strategy: the step should turn $k\cdot k!$ into a difference of two factorials. Note that $(k+1)! = (k+1)\cdot k!$, so $k\cdot k! = (k+1)! - k!$.*

**Claim.** $\displaystyle\sum_{k=1}^{n} k\cdot k! = (n+1)! - 1$ for every $n \ge 1$.

**Base case** $n = 1$: $1\cdot 1! = 1$ and $(1+1)! - 1 = 2-1 = 1$. ✓

**Inductive hypothesis.** $\sum_{j=1}^{k} j\cdot j! = (k+1)! - 1$.

**Step.**

$$\sum_{j=1}^{k+1} j\cdot j! = (k+1)! - 1 + (k+1)(k+1)! = (k+1)!\bigl(1 + k + 1\bigr) - 1 = (k+2)! - 1. \qquad \square$$

*Alternative view.* Since $k\cdot k! = (k+1)! - k!$, the sum telescopes:

$$\sum_{k=1}^{n}\bigl((k+1)! - k!\bigr) = (n+1)! - 1!.$$

*Check.* $n = 3$: $1 + 4 + 18 = 23 = 24 - 1$ ✓.

**14.** *Strategy: expand $(k+1)^3 + 5(k+1)$, isolate $(k^3+5k)$, and show the remainder is a multiple of $6$ by splitting it into $3k(k+1)$ and $6$.*

**Claim.** $6 \mid n^3+5n$ for every $n \ge 1$.

*Values.* $n=1$: $6$; $n=2$: $18$; $n=3$: $42$; $n=4$: $84$. ✓

**Base case** $n = 1$: $1 + 5 = 6$. ✓

**Inductive hypothesis.** $k^3+5k = 6m$ for some integer $m$.

**Step.**

$$(k+1)^3 + 5(k+1) = k^3 + 3k^2 + 3k + 1 + 5k + 5 = (k^3+5k) + 3k^2 + 3k + 6 = (k^3+5k) + 3k(k+1) + 6.$$

Now $k(k+1)$ is even, being a product of consecutive integers, so $3k(k+1)$ is divisible by $6$. Hence the whole expression is $6m + 6t + 6 = 6(m+t+1)$. $\square$

**15.** *Strategy: the only delicate point is the multiplication step; everything else is expansion.*

**(a)** **Claim.** For every real $x \ge 0$ and every $n \in \mathbb{N}_0$, $(1+x)^n \ge 1+nx$.

**Base case** $n = 0$: $(1+x)^0 = 1 = 1 + 0\cdot x$. ✓

**Inductive hypothesis.** $(1+x)^k \ge 1+kx$ for some $k \ge 0$.

**Step.** Since $x \ge 0$ we have $1+x \ge 1 > 0$, so multiplying the hypothesis by $1+x$ preserves the inequality:

$$(1+x)^{k+1} = (1+x)^k(1+x) \ge (1+kx)(1+x) = 1 + (k+1)x + kx^2 \ge 1 + (k+1)x,$$

because $kx^2 \ge 0$. $\square$

**(b)** The hypothesis is needed in the line "multiplying the hypothesis by $1+x$ preserves the inequality": that step requires $1+x \ge 0$, i.e. $x \ge -1$. For $x < -1$ the factor $1+x$ is negative, the inequality reverses, and the chain breaks. (The same proof does work for every $x \ge -1$; the weaker hypothesis $x \ge 0$ was assumed in part (a) to make the sign discussion trivial. This is Theorem 7.9.1.)

**(c)** Take $n = 3$ and $x = -4$, so $1+x = -3$. Then $(1+x)^3 = -27$, while $1 + 3x = 1 - 12 = -11$. Since $-27 < -11$, the inequality fails. So the hypothesis $x \ge -1$ cannot be dropped.

*Remark.* For even $n$ the inequality happens to hold for every real $x$ (the left side is non-negative and the right side is $1+nx$, which is negative for $x < -1/n$); the failure for odd $n$ is what makes the hypothesis necessary.

**16.** *Strategy: prove the step by clearing the positive denominator $\sqrt{k+1}$; the key estimate is $\sqrt{k(k+1)} \ge k$.*

**Claim.** $\displaystyle\sum_{j=1}^{n}\frac{1}{\sqrt j} \ge \sqrt n$ for every $n \ge 1$.

**Base case** $n = 1$: $1 \ge 1$. ✓

**Inductive hypothesis.** $\sum_{j=1}^{k}\frac{1}{\sqrt j} \ge \sqrt k$ for some $k \ge 1$.

**Step.**

$$\sum_{j=1}^{k+1}\frac{1}{\sqrt j} \ge \sqrt{k} + \frac{1}{\sqrt{k+1}}.$$

We claim $\sqrt k + \frac{1}{\sqrt{k+1}} \ge \sqrt{k+1}$. Multiply both sides by $\sqrt{k+1} > 0$: the claim becomes $\sqrt{k(k+1)} + 1 \ge k+1$, i.e. $\sqrt{k(k+1)} \ge k$, which holds because $k(k+1) \ge k^2$ for $k \ge 0$. Hence the sum is at least $\sqrt{k+1}$. $\square$

*Check.* $n = 4$: $1 + 0.7071 + 0.5774 + 0.5 = 2.7845 \ge 2$ ✓.

**17.** *Strategy: the step adds $(k+1)2^{k+1}$; factor $2^{k+1}$ out of the two terms involving it.*

**Claim.** $\displaystyle\sum_{j=1}^{n} j\,2^j = (n-1)2^{n+1} + 2$ for every $n \ge 1$.

**Base case** $n = 1$: $1\cdot 2 = 2$ and $(0)\cdot 4 + 2 = 2$. ✓

**Inductive hypothesis.** $\sum_{j=1}^{k} j\,2^j = (k-1)2^{k+1}+2$.

**Step.**

$$\sum_{j=1}^{k+1} j\,2^j = (k-1)2^{k+1} + 2 + (k+1)2^{k+1} = 2^{k+1}\bigl[(k-1)+(k+1)\bigr] + 2 = k\,2^{k+2} + 2,$$

which is the formula at $k+1$, since $\bigl((k+1)-1\bigr)2^{k+2} + 2 = k\,2^{k+2}+2$. $\square$

*Check.* $n = 3$: $2 + 8 + 24 = 34$ and $2\cdot 16 + 2 = 34$ ✓.

**18.** *Strategy: force $a^k-b^k$ to appear by writing $a^{k+1}-b^{k+1} = a(a^k-b^k) + b^k(a-b)$. This is the one-line source of every "$a-b$ divides ..." theorem.*

**Claim.** For integers $a \ne b$ and every $n \ge 1$, $a-b \mid a^n-b^n$.

**Base case** $n = 1$: $a^1-b^1 = (a-b)\cdot 1$. ✓

**Inductive hypothesis.** $a^k - b^k = (a-b)q$ for some integer $q$.

**Step.**

$$a^{k+1} - b^{k+1} = a^{k+1} - ab^k + ab^k - b^{k+1} = a\bigl(a^k-b^k\bigr) + b^k(a-b) = a(a-b)q + b^k(a-b) = (a-b)\bigl(aq + b^k\bigr). \qquad \square$$

*Remark.* The quotient is the geometric sum $a^{k}+a^{k-1}b+\cdots+b^{k}$; the identity
$a^{n}-b^{n} = (a-b)\sum_{j=0}^{n-1}a^{n-1-j}b^{j}$ can also be proved directly by expanding the product, and the induction above is the shortest route to it. Taking $b = 1$ gives $a-1 \mid a^n-1$, which is Theorems 7.10.2 and 7.10.3.

**19.** *Strategy: the step adds $F_{2k+2}$ and uses the defining recurrence once.*

**Claim.** $F_2 + F_4 + \cdots + F_{2n} = F_{2n+1}-1$ for every $n \ge 1$.

*Values.* $n=1$: $F_2 = 1$ and $F_3 - 1 = 2-1 = 1$ ✓. $n=2$: $1 + 3 = 4$ and $F_5-1 = 5-1 = 4$ ✓. $n=3$: $4 + 8 = 12$ and $F_7 - 1 = 13-1 = 12$ ✓.

**Base case** $n = 1$: checked. ✓

**Inductive hypothesis.** $F_2 + \cdots + F_{2k} = F_{2k+1}-1$ for some $k \ge 1$.

**Step.**

$$F_2 + \cdots + F_{2k} + F_{2k+2} = \bigl(F_{2k+1}-1\bigr) + F_{2k+2} = F_{2k+3} - 1,$$

because $F_{2k+1} + F_{2k+2} = F_{2k+3}$ by the recurrence. $\square$

**20.** *Strategy: prove the lemma $2k+1 \le 2^k$ for $k \ge 5$ by its own induction, then use it in the main step. This is an honest two-part proof: the main induction cannot close without the estimate.*

**Lemma.** For every integer $k \ge 5$, $2k+1 \le 2^k$.

*Proof.* Base $k = 5$: $11 \le 32$. ✓ Step: if $2k+1 \le 2^k$ and $k \ge 5$, then

$$2(k+1)+1 = 2k + 3 \le 2(2k+1) = 4k+2 \le 2\cdot 2^k = 2^{k+1},$$

where $2k+3 \le 4k+2$ is $1 \le 2k$, true for $k \ge 1$. $\square$

**Claim.** $n^2 < 2^n$ for every $n \ge 5$.

**Base case** $n = 5$: $25 < 32$. ✓

**Inductive hypothesis.** $k^2 < 2^k$ for some $k \ge 5$.

**Step.** By the lemma, $2k+1 \le 2^k$, so

$$(k+1)^2 = k^2 + 2k + 1 < 2^k + 2^k = 2^{k+1}. \qquad \square$$

*Check.* $n = 6$: $36 < 64$ ✓; $n = 10$: $100 < 1024$ ✓.

**21.** *Strategy: strong induction with four base cases, because the step subtracts $4$.*

**Claim.** Every integer $n \ge 18$ is a sum of $4$s and $7$s.

**Base cases.**

$$18 = 7+7+4, \qquad 19 = 7+4+4+4, \qquad 20 = 4+4+4+4+4, \qquad 21 = 7+7+7.$$

✓

**Inductive step.** Let $k \ge 21$ and assume every integer $m$ with $18 \le m \le k$ is a sum of $4$s and $7$s. Then $k+1-4 = k-3 \ge 18$, so by the hypothesis $k-3$ is a sum of $4$s and $7$s; appending one more $4$ represents $k+1 = (k-3)+4$. $\square$

*Why four base cases?* The step reaches back exactly $4$, so the induction covers a residue class modulo $4$ from each base case. The four values $18, 19, 20, 21$ are one complete set of residues, and every $n \ge 18$ is congruent to one of them modulo $4$.

*Remark.* $17$ is not representable, so $18$ is the true threshold. This is the two-coin case of Exercise 32 with $a = 4$, $b = 7$, where $(a-1)(b-1) = 18$.

**22.** *Strategy: strong induction. If $n$ is not a power of $2$, subtract the largest power of $2$ below it; the remainder is smaller than that power, so its representation cannot already use it.*

**Claim.** Every integer $n \ge 1$ is a sum of distinct powers of $2$.

**Base case** $n = 1 = 2^0$. ✓

**Inductive step.** Let $n \ge 2$ and assume every $m$ with $1 \le m < n$ is a sum of distinct powers of $2$. Choose $j \ge 0$ with $2^j \le n < 2^{j+1}$.

* If $n = 2^j$, then $n$ is a single power of $2$.
* Otherwise $1 \le m := n - 2^j < 2^{j+1} - 2^j = 2^j$. By the inductive hypothesis $m$ is a sum of distinct powers of $2$; every summand is at most $m < 2^j$, so no summand equals $2^j$. Hence $n = 2^j + m$ is a sum of distinct powers of $2$.

$\square$

*Check.* $5 = 4+1$, $6 = 4+2$, $7 = 4+2+1$, $11 = 8+2+1$ ✓.

*Remark.* Uniqueness is a separate statement: it follows from the fact that the largest power of $2$ not exceeding $n$ is forced. The division algorithm in [Natural Numbers](../../01-arithmetic/01-natural-numbers/README.md), Section 8.10, proves the full base-$b$ expansion theorem.

## Advanced

**23.** *Strategy: find a recurrence by looking at the last line drawn. The $n$-th line is cut by the previous $n-1$ lines into $n$ pieces, each of which creates one new region.*

**Claim.** $n$ lines in general position divide the plane into $R(n) = \dfrac{n(n+1)}{2} + 1$ regions.

*Small cases.* $R(0) = 1$ (no lines, one region); $R(1) = 2$; $R(2) = 4$ (two crossing lines give four sectors); $R(3) = 7$ (a triangle with its three outer regions). ✓

**Recurrence.** Suppose $k$ lines are already drawn and a $(k+1)$-st line is added. Since no two lines are parallel, the new line meets each of the $k$ old lines; since no three are concurrent, those $k$ intersection points are distinct. They cut the new line into $k+1$ pieces (two rays and $k-1$ bounded segments). Each piece lies entirely inside one old region and splits it into two, so exactly $k+1$ regions are gained:

$$R(k+1) = R(k) + (k+1).$$

**Induction.** Base case $n = 0$: $R(0) = 1 = \frac{0\cdot 1}{2}+1$. ✓ Step: assume $R(k) = \frac{k(k+1)}{2}+1$. Then

$$R(k+1) = \frac{k(k+1)}{2} + 1 + (k+1) = \frac{k(k+1) + 2(k+1)}{2} + 1 = \frac{(k+1)(k+2)}{2} + 1. \qquad \square$$

*Remark.* The same computation with $n$ circles in general position (no two tangent, no three concurrent) gives $n^2 - n + 2$ regions, and the general technique — "count the pieces of the new curve" — is Euler's formula in disguise.

**24.** *Strategy: prove the leaf lemma first by looking at an endpoint of a longest path, then induct by pruning a leaf.*

**Lemma (leaf lemma).** Every tree with at least two vertices has a vertex of degree $1$.

*Proof.* Let $T$ be a tree with $n \ge 2$ vertices. Since $T$ is connected, it has at least one edge, so choose a longest path $v_0v_1\cdots v_m$ with $m \ge 1$. Suppose $v_m$ has a neighbour $w \ne v_{m-1}$.

* If $w \notin \{v_0, \ldots, v_m\}$, then $v_0 \cdots v_m w$ is a path longer than the chosen one, contradicting maximality.
* If $w = v_i$ for some $0 \le i \le m-2$, then $v_i v_{i+1} \cdots v_m v_i$ is a cycle of length at least $3$, contradicting acyclicity.

Hence $v_m$ has no neighbour other than $v_{m-1}$, so $\deg(v_m) = 1$. $\square$

**Claim.** Every tree with $n \ge 1$ vertices has exactly $n-1$ edges.

**Base case** $n = 1$: a single vertex has no edges, and $1 - 1 = 0$. ✓

**Inductive step.** Let $T$ be a tree with $n+1 \ge 2$ vertices. By the lemma, $T$ has a leaf $v$; let $u$ be its unique neighbour. Then $T - v$ is connected (any two remaining vertices were joined by a path in $T$, and a path can contain $v$ only as an endpoint, since $\deg(v)=1$; deleting that endpoint leaves the rest) and acyclic (deleting a vertex cannot create a cycle). So $T-v$ is a tree with $n$ vertices, hence has $n-1$ edges by the inductive hypothesis. Since $T$ has exactly one edge more than $T-v$, namely $uv$,

$$|E(T)| = (n-1) + 1 = n = (n+1) - 1. \qquad \square$$

*Check.* A path with $4$ vertices has $3$ edges; a star with $5$ vertices has $4$ edges. ✓

**25.** *Strategy: remove a vertex, colour the rest by induction, and put the vertex back using a colour that none of its at most $\Delta$ neighbours uses.*

**Claim.** Every finite graph $G$ has a proper colouring with at most $\Delta(G)+1$ colours.

**Base case** $|V| = 1$: one colour suffices, and $1 \le \Delta + 1$. ✓

**Inductive step.** Let $G$ have $n+1$ vertices and choose any vertex $v$; put $G' = G - v$. Since $\Delta(G') \le \Delta(G)$, the inductive hypothesis gives a proper colouring of $G'$ with $\Delta(G)+1$ colours. The vertex $v$ has at most $\Delta(G)$ neighbours, and each of them displays one colour, so at most $\Delta(G)$ colours are forbidden at $v$. At least one of the $\Delta(G)+1$ colours is therefore available; assign it to $v$. Adjacent vertices now have different colours, since the restriction to $G'$ was already proper. $\square$

**Why this does not give a 2-colouring of a tree.** The induction fixes the palette size at $\Delta+1$ before the argument starts. For a star, $\Delta = n-1$, so the method offers $n$ colours; and even if we tried to run it with only $2$ colours, the extension step would fail whenever $v$ has two neighbours of different colours. The extra information in a tree is structural — leaves have only one neighbour — and Theorem 7.12.3 exploits it by always removing a leaf rather than an arbitrary vertex. The greedy bound is true but not tight; a bound can be correct and still useless for a particular class of graphs.

*Check.* The cycle $C_5$ has $\Delta = 2$ and $\chi = 3 = \Delta+1$, so the bound is attained. The complete graph $K_4$ has $\Delta = 3$ and $\chi = 4 = \Delta+1$, also attained.

**26.** *Strategy: structural induction. Every formula is built by one of the three rules, so it suffices to check the rules and to see that each rule adds the same number of left and right brackets.*

**Claim.** Every propositional formula contains equally many left and right brackets.

**Base case.** A formula that is a single variable symbol $p$ contains no brackets, so it has $0$ left and $0$ right. ✓

**Inductive step, negation.** Let $\varphi$ be a formula with $L$ left and $R$ right brackets, and suppose $L = R$. The formula $(\neg\varphi)$ is the string consisting of a left bracket, the symbol $\neg$, the string of $\varphi$, and a right bracket. Its bracket counts are $L+1$ and $R+1$, which are equal. ✓

**Inductive step, binary connective.** Let $\varphi$ and $\psi$ be formulas with $L_\varphi = R_\varphi$ and $L_\psi = R_\psi$. For $\circ \in \{\wedge, \vee\}$, the formula $(\varphi \circ \psi)$ adds exactly one left bracket (at the front) and one right bracket (at the end) to the concatenation of the two strings. Its counts are $L_\varphi + L_\psi + 1$ and $R_\varphi + R_\psi + 1$, which are equal. ✓

Since these are the only formation rules, every formula has equally many left and right brackets. $\square$

*Remark.* The converse fails: the string `)(` has one of each and is not a formula. Structural induction proves a necessary condition cheaply, which is often all a parser needs.

**27.** *Strategy: factor $(-1)^k$ out of both terms in the step. The relation $(-1)^{k-1} = -(-1)^k$ is the whole trick.*

**Claim.** $\displaystyle\sum_{j=1}^{n}(-1)^{j-1}j^2 = (-1)^{n-1}\frac{n(n+1)}{2}$ for every $n \ge 1$.

*Values.* $n=1$: $1$ and $1\cdot\frac{1\cdot2}{2} = 1$ ✓. $n=2$: $1-4 = -3$ and $(-1)\cdot 3 = -3$ ✓. $n=3$: $-3+9 = 6$ and $6$ ✓. $n=4$: $6-16 = -10$ and $-10$ ✓.

**Base case** $n = 1$: checked. ✓

**Inductive hypothesis.** $\sum_{j=1}^{k}(-1)^{j-1}j^2 = (-1)^{k-1}\frac{k(k+1)}{2}$.

**Step.**

$$\sum_{j=1}^{k+1}(-1)^{j-1}j^2 = (-1)^{k-1}\frac{k(k+1)}{2} + (-1)^{k}(k+1)^2 = (-1)^k\left[-\frac{k(k+1)}{2} + (k+1)^2\right].$$

The bracket simplifies to

$$(k+1)\left[-\frac{k}{2} + (k+1)\right] = (k+1)\cdot\frac{-k+2k+2}{2} = \frac{(k+1)(k+2)}{2},$$

so the sum equals $(-1)^k\frac{(k+1)(k+2)}{2} = (-1)^{(k+1)-1}\frac{(k+1)(k+2)}{2}$. $\square$

**28.** *Strategy: rewrite $F_{n+2}$ as $F_{n+1}+F_n$ and then use $F_{n+1}-F_n = F_{n-1}$ to expose the inductive hypothesis exactly.*

We use $F_0 = 0$ (so $F_2 = F_1 + F_0$ is consistent with the recurrence).

**Claim.** $F_{n+1}F_{n-1} - F_n^2 = (-1)^n$ for every $n \ge 1$.

**Base case** $n = 1$: $F_2F_0 - F_1^2 = 1\cdot 0 - 1 = -1 = (-1)^1$. ✓

**Inductive hypothesis.** $F_{k+1}F_{k-1} - F_k^2 = (-1)^k$ for some $k \ge 1$.

**Step.** The quantity at $k+1$ is $F_{k+2}F_k - F_{k+1}^2$. Using $F_{k+2} = F_{k+1} + F_k$,

$$F_{k+2}F_k - F_{k+1}^2 = F_{k+1}F_k + F_k^2 - F_{k+1}^2 = F_k^2 - F_{k+1}\bigl(F_{k+1} - F_k\bigr).$$

Now $F_{k+1} - F_k = F_{k-1}$, so

$$F_{k+2}F_k - F_{k+1}^2 = F_k^2 - F_{k+1}F_{k-1} = -\bigl(F_{k+1}F_{k-1} - F_k^2\bigr) = -(-1)^k = (-1)^{k+1}. \qquad \square$$

*Check.* $n = 4$: $F_5F_3 - F_4^2 = 5\cdot 2 - 9 = 1 = (-1)^4$ ✓.

**29.** *Strategy: three base cases and a step valid for $k \ge 3$. The estimate $3k^3 \ge (k+1)^3$ is the only real work, and it is proved by bounding $3k \le k^2$ and $1 \le k^2$.*

**Claim.** $3^n \ge n^3$ for every integer $n \ge 1$.

**Base cases.**

$$n = 1:\ 3 \ge 1, \qquad n = 2:\ 9 \ge 8, \qquad n = 3:\ 27 = 27.$$

✓

**Lemma.** For every integer $k \ge 3$, $\;3k^3 \ge (k+1)^3$.

*Proof.* Expand:

$$3k^3 - (k+1)^3 = 3k^3 - k^3 - 3k^2 - 3k - 1 = 2k^3 - 3k^2 - 3k - 1.$$

For $k \ge 3$ we have $3k \le k^2$ and $1 \le k^2$, so

$$2k^3 - 3k^2 - 3k - 1 \;\ge\; 2k^3 - 3k^2 - k^2 - k^2 = 2k^3 - 5k^2 = k^2(2k-5) > 0,$$

since $k \ge 3$ gives $2k - 5 \ge 1 > 0$. Hence $3k^3 \ge (k+1)^3$. $\square$

**Inductive step.** Let $k \ge 3$ and assume $3^k \ge k^3$. Then

$$3^{k+1} = 3\cdot 3^k \ge 3k^3 \ge (k+1)^3$$

by the hypothesis and the lemma. So the statement holds at $k+1$ for every $k \ge 3$, and the base cases $n = 1, 2, 3$ cover the remaining values. $\square$

*Remark.* The inequality is sharp at $n = 3$; a strict version $3^n > n^3$ would be false there. This is why the step is stated with $\ge$ and the base cases include $n = 3$ rather than starting at $n = 4$.

**30.** *Strategy: strong induction in the form "reduce $n+1$ numbers to $n$ numbers by merging two of them". The pigeonhole principle supplies the pair whose merge does not decrease the sum.*

**Claim.** If $x_1, \ldots, x_n > 0$ and $x_1x_2\cdots x_n = 1$, then $x_1 + \cdots + x_n \ge n$.

**Base cases.**

* $n = 1$: $x_1 = 1$, so $x_1 \ge 1$. ✓
* $n = 2$: $x_1x_2 = 1$ gives $x_1 + x_2 \ge 2\sqrt{x_1x_2} = 2$, because $(\sqrt{x_1}-\sqrt{x_2})^2 \ge 0$ expands to $x_1 + x_2 \ge 2\sqrt{x_1x_2}$. ✓

**Inductive step.** Let $n \ge 2$ and assume the claim for $n$; consider $n+1$ positive numbers $x_1,\ldots,x_{n+1}$ with product $1$.

*First, find a good pair.* If some $x_i = 1$, then for any $j \ne i$ we have $(x_i-1)(x_j-1) = 0$. If no $x_i$ equals $1$, then each is either above or below $1$, and by the pigeonhole principle among $n+1 \ge 3$ numbers two lie on the same side of $1$. In either case there are distinct indices $i, j$ with

$$(x_i - 1)(x_j - 1) \ge 0, \qquad \text{equivalently} \qquad x_i + x_j \ge 1 + x_ix_j.$$

*Then merge them.* The $n$ numbers obtained from $x_1,\ldots,x_{n+1}$ by deleting $x_i$ and $x_j$ and inserting the single number $x_ix_j$ have product $1$, so by the inductive hypothesis

$$\sum_{l \notin \{i,j\}} x_l \;+\; x_ix_j \;\ge\; n.$$

Therefore

$$\sum_{l=1}^{n+1} x_l = \sum_{l \notin \{i,j\}} x_l + x_i + x_j \;\ge\; \sum_{l \notin \{i,j\}} x_l + 1 + x_ix_j \;\ge\; n + 1. \qquad \square$$

*Check.* For $n = 3$ and $(x_1,x_2,x_3) = (2, 3, \tfrac16)$: the product is $1$ and the sum is $5.1\overline{6} \ge 3$ ✓.

*Remark.* This is AM–GM in the special case of product $1$; dividing each $a_i$ by the geometric mean recovers the general statement, which is Corollary 7.9.3. The merge step is the standard "smoothing" argument: replacing two numbers by their product keeps the product and never increases the sum.

## Challenge

**31.** *Strategy: strong induction on $n$, subtracting the largest Fibonacci number not exceeding $n$. The remainder is less than $F_{k-1}$, so its summands cannot reach $F_k$ or $F_{k-1}$, which keeps the representation distinct.*

**Claim.** Every integer $n \ge 1$ is a sum of distinct Fibonacci numbers $F_1, F_2, F_3, \ldots$ with $F_1 = F_2 = 1$.

**Base case** $n = 1 = F_2$. ✓

**Inductive step.** Let $n \ge 2$ and assume every $m$ with $1 \le m < n$ is a sum of distinct Fibonacci numbers. Choose $k \ge 2$ with

$$F_k \le n < F_{k+1}.$$

(Such a $k$ exists because $F_2 = 1 \le n$ and the Fibonacci numbers are unbounded.)

* If $n = F_k$, then $n$ is a single Fibonacci number, and we are done.
* Otherwise $m := n - F_k$ satisfies $1 \le m < F_{k+1} - F_k = F_{k-1}$. By the inductive hypothesis, $m$ is a sum of distinct Fibonacci numbers. Every summand is at most $m < F_{k-1}$, so every summand has index at most $k-2$. Hence $n = F_k + m$ expresses $n$ as a sum of distinct Fibonacci numbers, and $F_k$ does not appear among the summands of $m$.

$\square$

*Check.* $1 = F_2$; $2 = F_3$; $3 = F_4$; $4 = F_4 + F_2 = 3+1$; $5 = F_5$; $6 = F_5 + F_2 = 5+1$; $7 = F_5 + F_3 = 5+2$; $8 = F_6$; $11 = F_6 + F_4 = 8+3$; $12 = F_6 + F_4 + F_2 = 8+3+1$. ✓

*Remark.* The representation is not unique: $6 = 5 + 1 = 3 + 2 + 1$. Zeckendorf's theorem states that requiring the indices to be **non-consecutive** makes the representation unique; that is a separate and harder statement, and the argument above does not prove it.

**32.** *Strategy: first represent a whole block of $a$ consecutive integers, then step upwards adding $a$. The block exists because multiples of $b$ run through all residues modulo $a$.*

**Claim.** Let $a, b$ be coprime positive integers and $N_0 = (a-1)(b-1)$. Every integer $n \ge N_0$ has the form $n = ax + by$ with integers $x, y \ge 0$.

**Step 1: all residues modulo $a$ are available.** Because $\gcd(a,b) = 1$, the $a$ numbers

$$0\cdot b,\; 1\cdot b,\; 2\cdot b,\; \ldots,\; (a-1)\cdot b$$

are pairwise incongruent modulo $a$: if $ib \equiv jb \pmod a$ with $0 \le i < j \le a-1$, then $a \mid (j-i)b$, and since $\gcd(a,b)=1$ we get $a \mid (j-i)$, impossible because $0 < j - i < a$. So they represent all $a$ residue classes.

**Step 2: the block $N_0, N_0+1, \ldots, N_0+a-1$ is representable.** Fix such an $n$. Choose $j \in \{0, 1, \ldots, a-1\}$ with $jb \equiv n \pmod a$. Then $a \mid (n - jb)$, so write $n - jb = ax$ with $x \in \mathbb{Z}$; we must check $x \ge 0$. Now

$$n - jb \;\ge\; N_0 - (a-1)b = (a-1)(b-1) - (a-1)b = -(a-1) > -a .$$

A multiple of $a$ that is greater than $-a$ is at least $0$, so $x \ge 0$; and $y := j \ge 0$. Hence each of the $a$ numbers in the block is representable.

**Step 3: induction.** We prove by strong induction on $n \ge N_0$ that $n$ is representable. The base cases are the $a$ numbers $N_0, \ldots, N_0+a-1$ from Step 2. For $n \ge N_0 + a$ we have $n - a \ge N_0$, so by the inductive hypothesis $n - a = ax + by$ with $x, y \ge 0$, and then $n = a(x+1) + by$. $\square$

*Check.* For $a = 4$, $b = 7$: $N_0 = 3\cdot 6 = 18$, and indeed $18 = 4+7+7$, $19 = 4+4+4+7$, $20 = 5\cdot 4$, $21 = 3\cdot 7$, after which adding $4$ covers everything. Exercise 21 is this case.

*Remark.* The threshold $(a-1)(b-1)$ is optimal: $(a-1)(b-1) - 1 = ab - a - b$ is not representable. (If $ab - a - b = ax + by$, reduce modulo $a$ to get $by \equiv -b \pmod a$, so $y \equiv -1 \pmod a$; the smallest such $y \ge 0$ is $a - 1$, giving $ax = ab - a - b - (a-1)b = -a$, i.e. $x = -1 < 0$.) The full statement — that $ab - a - b$ is the largest non-representable integer — is the **Frobenius coin problem** for two coins.

**33.** *Strategy: induct on $n$ with $r$ fixed. Pascal's rule is exactly the identity needed to merge the new term with the old sum.*

**Claim.** For integers $n \ge r \ge 0$, $\displaystyle\sum_{i=r}^{n}\binom{i}{r} = \binom{n+1}{r+1}$.

**Base case** $n = r$: the sum is $\binom{r}{r} = 1$ and $\binom{r+1}{r+1} = 1$. ✓

**Inductive hypothesis.** $\sum_{i=r}^{k}\binom{i}{r} = \binom{k+1}{r+1}$ for some $k \ge r$.

**Step.** By Pascal's rule,

$$\sum_{i=r}^{k+1}\binom{i}{r} = \binom{k+1}{r+1} + \binom{k+1}{r} = \binom{k+2}{r+1}. \qquad \square$$

*Check with $r = 1$.* The identity reads $\sum_{i=1}^{n} i = \binom{n+1}{2} = \frac{n(n+1)}{2}$, which is Theorem 8.2. ✓

*Combinatorial reading.* The number of ways to choose $r+1$ elements from $\{1, \ldots, n+1\}$ is counted by the largest element chosen: if it is $i+1$, the remaining $r$ are chosen from $\{1,\ldots,i\}$, giving $\binom{i}{r}$.

**34.** *Strategy: the recurrence $a_{n+1} = a_n^2 - 2$ is the squaring identity for $x + x^{-1}$. Check that $(t + t^{-1})^2 - 2 = t^2 + t^{-2}$, then iterate it.*

**Claim.** Let $x > 1$ satisfy $x + x^{-1} = 3$, and let $a_0 = 3$, $a_{n+1} = a_n^2 - 2$. Then $a_n = x^{2^n} + x^{-2^n}$ for every $n \ge 0$.

**Base case** $n = 0$: $x^{1} + x^{-1} = 3 = a_0$. ✓

**Inductive step.** Assume $a_k = x^{2^k} + x^{-2^k}$. Then, writing $t = x^{2^k}$,

$$a_{k+1} = a_k^2 - 2 = (t + t^{-1})^2 - 2 = t^2 + 2 + t^{-2} - 2 = t^2 + t^{-2} = x^{2^{k+1}} + x^{-2^{k+1}}. \qquad \square$$

**Consequence.** Since $x > 1$, we have $0 < x^{-2^n} < 1$, so $a_n = x^{2^n} + x^{-2^n}$ is the integer immediately above $x^{2^n}$:

$$a_n = \bigl\lceil x^{2^n} \bigr\rceil .$$

**Values.** $x$ solves $x^2 - 3x + 1 = 0$, so $x = \frac{3+\sqrt5}{2} \approx 2.618$. Then

$$a_0 = 3, \qquad a_1 = 3^2-2 = 7, \qquad a_2 = 7^2-2 = 47, \qquad a_3 = 47^2 - 2 = 2207.$$

Check: $x^{2} = \frac{7+3\sqrt5}{2} \approx 6.854$, so $\lceil x^2 \rceil = 7$ ✓; $x^4 \approx 46.98$, so $\lceil x^4\rceil = 47$ ✓.

**35.** *Strategy: the direct hypothesis "$< 2$" has no slack, so the step cannot absorb the next term. Strengthen to "$2 - 1/n$", which decreases by exactly the amount needed.*

**Strengthened claim.** $\displaystyle\sum_{k=1}^{n}\frac{1}{k^2} \le 2 - \frac{1}{n}$ for every $n \ge 1$.

**Base case** $n = 1$: $\frac{1}{1} = 1 = 2 - 1$. ✓

**Inductive hypothesis.** $\sum_{k=1}^{m}\frac{1}{k^2} \le 2 - \frac{1}{m}$ for some $m \ge 1$.

**Step.**

$$\sum_{k=1}^{m+1}\frac{1}{k^2} \;\le\; 2 - \frac{1}{m} + \frac{1}{(m+1)^2} \;\le\; 2 - \frac{1}{m+1},$$

provided $\frac{1}{(m+1)^2} \le \frac{1}{m} - \frac{1}{m+1} = \frac{1}{m(m+1)}$, which is equivalent to $m \le (m+1)^2$ and holds for every $m \ge 0$. ✓

**Conclusion.** The strengthened claim holds for all $n \ge 1$. Since $2 - \frac1n < 2$, it implies $\sum_{k=1}^{n} k^{-2} < 2$ for every $n \ge 1$. $\square$

*Why the stronger statement implies the weaker one.* $2 - 1/n < 2$ for every $n \ge 1$, so an upper bound by $2 - 1/n$ is also an upper bound by $2$.

*Diagnosis of the direct attempt.* From $S_k < 2$ one can only conclude $S_{k+1} < 2 + 1/(k+1)^2$, which does not prove $S_{k+1} < 2$. The strengthened hypothesis records how much room is left, and that room shrinks at exactly the rate the new term consumes.

**36.** *Strategy: two nested inductions. The outer (strong) induction on $n$ allows the claim for $n-1$ to be used at all values of $m$; the inner induction on $m$ then steps from one block of $n$ consecutive integers to the next.*

**Claim.** For every $n \ge 1$ and every integer $m \ge 0$, $\;n! \mid m(m+1)\cdots(m+n-1)$.

**Outer induction on $n$.**

*Base case* $n = 1$: the product is $m$, and $1! = 1$ divides it. ✓

*Inductive step.* Let $n \ge 2$ and assume the claim for every $j$ with $1 \le j \le n-1$ (in particular for $n-1$, and for all $m \ge 0$).

Fix $n$ and prove by induction on $m \ge 0$ that $P(m): n! \mid m(m+1)\cdots(m+n-1)$.

* *Base case* $m = 0$: the product is $0\cdot 1\cdots(n-1) = 0 = n!\cdot 0$. ✓
* *Inductive step.* Assume $P(m)$ and consider

$$P(m+1) = (m+1)(m+2)\cdots(m+n).$$

The difference identity

$$(m+1)\cdots(m+n) - m(m+1)\cdots(m+n-1) = (m+1)\cdots(m+n-1)\bigl[(m+n) - m\bigr] = n\,(m+1)\cdots(m+n-1)$$

exhibits $P(m+1)$ as $P(m)$ plus $n$ times a product of $n-1$ consecutive integers. That product is divisible by $(n-1)!$ by the outer inductive hypothesis, so $n$ times it is divisible by $n\cdot(n-1)! = n!$. Since $P(m)$ is divisible by $n!$ by the inner hypothesis, $P(m+1)$ is divisible by $n!$. ✓

Hence $P(m)$ holds for every $m \ge 0$, and since $n$ was arbitrary, the claim holds for every $n \ge 1$. $\square$

*Check.* $n = 4$, $m = 2$: the product $2\cdot3\cdot4\cdot5 = 120 = 5!$ and $4! = 24$ divides $120$ ✓. $n = 3$, $m = 7$: $7\cdot 8\cdot 9 = 504 = 3!\cdot 84$ ✓.

*Remark.* The statement is equivalent to "$\binom{m+n-1}{n}$ is an integer for all $m \ge 0$" — the binomial coefficient is exactly this product divided by $n!$ — so the exercise gives a self-contained proof that the binomial coefficients are integers, independent of any combinatorial interpretation.
