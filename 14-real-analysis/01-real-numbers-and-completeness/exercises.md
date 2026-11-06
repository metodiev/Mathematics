# The Real Numbers and Completeness — Exercises

> [Tutorial](README.md) · 36 problems · Levels: Beginner, Intermediate, Advanced, Challenge

Every problem below is a proof problem unless it explicitly asks for a computation. For computations,
prove that your candidate really is the supremum or infimum: an upper bound alone is not an answer.
You may use any result proved in the [tutorial](README.md), but not results from later topics. Full
solutions are in [solutions.md](solutions.md); do not open that file until you have attempted the
problems.

## Beginner

**1.** Find $\sup S$, $\inf S$, $\max S$ and $\min S$ (where they exist) for
$$
S = \left\{1 - \frac1n : n \in \mathbb{N}\right\}.
$$

**2.** Find $\sup S$, $\inf S$, $\max S$ and $\min S$ for $S = \{x \in \mathbb{R} : x^2 \le 9\}$.

**3.** Find $\sup S$, $\inf S$, $\max S$ and $\min S$ for
$$
S = \left\{3 + \frac{(-1)^n}{n} : n \in \mathbb{N}\right\}.
$$

**4.** Find $\sup S$ and $\inf S$ for $S = \{q \in \mathbb{Q} : 1 < q < 2\}$, regarded as a subset of $\mathbb{R}$. Do $\max S$ and $\min S$ exist?

**5.** Find $\sup S$, $\inf S$, $\max S$ and $\min S$ for
$$
S = \left\{\frac{n}{n+1} : n \in \mathbb{N}\right\}.
$$

**6.** Let $A = \{2, 5, 7\}$. Compute $\sup A$, $\inf A$, $\max A$, $\min A$.

**7.** True or false: every nonempty subset of $\mathbb{R}$ that is bounded above has a maximum. Justify your answer with a proof or a counterexample.

**8.** Find $\sup S$, $\inf S$, $\max S$ and $\min S$ for
$$
S = \left\{3 - \frac2n : n \in \mathbb{N}\right\}.
$$

**9.** Prove: if $u$ is an upper bound of a nonempty set $S \subseteq \mathbb{R}$ and $u \in S$, then $u = \sup S$.

**10.** Prove: if $S \subseteq T$ are nonempty subsets of $\mathbb{R}$ and $T$ is bounded above, then $\sup S \le \sup T$.

**11.** Let $S = \{1/n : n \in \mathbb{N}\}$ and $-S = \{-s : s \in S\}$. Compute $\sup(-S)$ and $\inf(-S)$ from the definitions, and verify that $\sup(-S) = -\inf S$ and $\inf(-S) = -\sup S$ in this example.

**12.** Find $\sup S$ and $\inf S$ for $S = \{x \in \mathbb{R} : x^3 < 8\}$, stating clearly whether $S$ is bounded below.

## Intermediate

**13.** Let $S \subseteq \mathbb{R}$ be nonempty and bounded above, and let $\alpha \in \mathbb{R}$. Prove that $\alpha = \sup S$ if and only if

* $\alpha$ is an upper bound of $S$, and
* for every $n \in \mathbb{N}$ there exists $s \in S$ with $s > \alpha - 1/n$.

**14.** Let $S = \{x \in \mathbb{R} : x^2 - 4x + 1 < 0\}$. Find $\sup S$ and $\inf S$ by completing the square, and prove your answer. (You may use the existence of $\sqrt 3$, proved by the method of Theorem 7.24.)

**15.** Let $S \ne \varnothing$ be bounded above and let $c \in \mathbb{R}$. Prove that
$$
\sup(c + S) = c + \sup S, \qquad c + S := \{c + s : s \in S\}.
$$

**16.** Let $A, B \subseteq (0, \infty)$ be nonempty and bounded above. Prove that
$$
\sup(AB) = (\sup A)(\sup B), \qquad AB := \{ab : a \in A,\ b \in B\}.
$$
Explain where the hypothesis $A, B \subseteq (0,\infty)$ is used.

**17.** Let $S$ be nonempty and bounded above, and let $T \subseteq S$ be nonempty.
(a) Prove that $\sup T \le \sup S$.
(b) Give an example with $T \subsetneq S$ and $\sup T = \sup S$.

**18.** Prove that the set of dyadic rationals
$$
D = \left\{\frac{m}{2^k} : m \in \mathbb{Z},\ k \in \mathbb{N}_0\right\}
$$
is dense in $\mathbb{R}$: between any two reals there is a dyadic rational.

**19.** Prove that every nonempty open interval $(x, y)$ contains infinitely many irrational numbers.

**20.** Prove the ceiling lemma: for every $x \in \mathbb{R}$ there is exactly one $n \in \mathbb{Z}$ with
$$
x \le n < x + 1 .
$$

**21.** Let $S \subseteq \mathbb{R}$ be nonempty and bounded. Prove that $\inf S \le \sup S$, and that equality holds if and only if $S$ has exactly one element.

**22.** Let $S \subseteq [0,\infty)$ be nonempty and bounded above. Prove that
$$
\sup\{s^2 : s \in S\} = (\sup S)^2 .
$$

## Advanced

**23.** Prove that there is a unique positive real number $\alpha$ with $\alpha^2 = 3$, using the supremum method. Then prove that $\alpha$ is irrational.

**24.** (a) Prove that $\bigcap_{n=1}^{\infty} [0, 1/n] = \{0\}$.
(b) Give an example of nested nonempty *open* intervals with empty intersection, and explain which hypothesis of the nested interval theorem fails.

**25.** Prove that every nonempty subset of $\mathbb{Z}$ that is bounded above has a greatest element.

**26.** Prove that every subset of a countable set is countable or finite.

**27.** Prove that $\mathbb{Q} \times \mathbb{Q}$ is countably infinite.

**28.** Let $2^{\mathbb{N}}$ denote the set of all functions $\mathbb{N} \to \{0,1\}$. Prove that $2^{\mathbb{N}}$ is uncountable, and that there is a bijection $2^{\mathbb{N}} \to \mathcal{P}(\mathbb{N})$.

**29.** A real number is **algebraic** if it is a root of a nonzero polynomial with integer coefficients. Prove that the set of algebraic numbers is countable. (You may use the fact that a nonzero polynomial of degree $d$ has at most $d$ real roots.)

**30.** Prove the converse direction of Theorem 7.13: if every nonempty subset of an ordered field $F$ that is bounded below has a greatest lower bound in $F$, then every nonempty subset that is bounded above has a least upper bound in $F$.

## Challenge

**31.** (a) Exhibit an explicit bijection $f : [0,1] \to (0,1)$ and prove that it is a bijection.
(b) Explain why the map $x \mapsto x$ is not such a bijection, and which property of infinite sets makes (a) possible.

**32.** Prove that there exists at least one real number that is not algebraic (a *transcendental* number). Your proof must not assume that any particular number such as $e$ or $\pi$ is transcendental.

**33.** A Dedekind cut is a set $\alpha \subseteq \mathbb{Q}$ that is nonempty, not all of $\mathbb{Q}$, downward closed, and has no largest element (Definition 7.35). For such an $\alpha$ define
$$
\sigma(\alpha) := \sup \alpha \quad (\text{supremum taken in } \mathbb{R}).
$$
(a) Prove that $\sigma(\alpha)$ exists for every cut $\alpha$.
(b) Prove that $\alpha = \{q \in \mathbb{Q} : q < \sigma(\alpha)\}$.
(c) Prove that $\sigma$ is a bijection from the set of all cuts onto $\mathbb{R}$.

**34.** Let
$$
F = \left\{\frac{p}{q} : p, q \in \mathbb{R}[t],\ q \ne 0\right\}
$$
be the field of rational functions in one indeterminate, and for $f = p/q \ne 0$ declare $f > 0$ if and only if $f(x) > 0$ for all sufficiently large real $x$.
(a) Prove that this is a well-defined total order making $F$ an ordered field.
(b) Prove that the element $t$ satisfies $t > n$ for every $n \in \mathbb{N}$, so $F$ is not Archimedean.
(c) Deduce that $F$ is not complete.

**35.** For $S \subseteq \mathbb{N}$ define
$$
\Phi(S) := \sup\left\{\sum_{n \in F} 3^{-n} : F \subseteq S \text{ finite}\right\},
$$
where the sum over the empty set is $0$.
(a) Prove that the supremum exists and that $0 \le \Phi(S) \le 1/2$.
(b) Prove that $\Phi$ is injective.
(c) Deduce that $\mathcal{P}(\mathbb{N})$ is uncountable and that $\lvert\mathcal{P}(\mathbb{N})\rvert \le \lvert\mathbb{R}\rvert$.

**36.** Prove that there is no order isomorphism between $(\mathbb{R}, <)$ and $(\mathbb{Q}, <)$, i.e. no bijection $f : \mathbb{R} \to \mathbb{Q}$ such that $x < y \iff f(x) < f(y)$.
