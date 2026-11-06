# Connectedness — Exercises

> [Connectedness](README.md) · 36 problems · Beginner → Challenge · Solutions: [solutions.md](solutions.md)

Every problem is a proof unless it asks for a decision or a computation. You may use anything proved in the
[tutorial](README.md). "Decide" means: state whether the property holds and justify the answer with a proof or
an explicit separation. Do not open [solutions.md](solutions.md) before writing an attempt.

Notation: $X, Y$ are topological spaces; subsets carry the subspace topology; $S^n = \{x \in \mathbb{R}^{n+1} :
\lVert x\rVert = 1\}$ and $D^n = \{x \in \mathbb{R}^n : \lVert x\rVert \le 1\}$; $\overline A$, $A^{\circ}$ and
$\partial A$ are closure, interior and boundary; a *separation* of a space $Z$ is a pair of disjoint non-empty
open sets whose union is $Z$.

## Beginner

**1.** Decide which of the following subsets of $\mathbb{R}$ are connected, quoting the interval theorem:
(a) $\{0,1\}$; (b) $[0,1]\cup[2,3]$; (c) $[0,2]\setminus\{1\}$; (d) $\mathbb{Q}\cap(0,1)$; (e) $\mathbb{Z}$;
(f) $(0,1)\cup\{2\}$; (g) $\mathbb{R}\setminus\mathbb{Z}$; (h) $\{1/n : n \in \mathbb{N}\}$; (i) $[0,\infty)$;
(j) $\mathbb{R}\setminus\mathbb{Q}$.

**2.** Prove that the empty space and every one-point space are connected, that every space with the
indiscrete topology is connected, and that a discrete space is connected if and only if it has at most one
point.

**3.** Let $X = \{a,b\}$ with $a \neq b$. List every topology on $X$ and decide for each whether $(X,\mathcal{T})$
is connected.

**4.** Let $X$ be connected and let $A \subseteq X$ be non-empty and clopen. Working directly from the
definition of a separation (do not cite Theorem 7.2.1), prove that $A = X$.

**5.** Let $X = \{a,b,c\}$ with topology $\mathcal{T} = \{\varnothing,\{a\},\{b\},\{a,b\},X\}$. Decide whether $X$
is connected, and determine its components and its path components.

**6.** Compute the components and the path components of $A = [0,1]\cup[2,3]\cup\{5\} \subseteq \mathbb{R}$.

**7.** (a) Exhibit a separation of $\mathbb{R}\setminus\{0\}$. (b) Prove that $\mathbb{C}\setminus\{0\}$ is path
connected by writing down an explicit path from any $z \neq 0$ to $1$, and check that your formula never
vanishes.

**8.** Let $X$ be connected and let $f : X \to \mathbb{Z}$ be continuous, where $\mathbb{Z}$ carries the
discrete topology. Prove that $f$ is constant.

**9.** Let $X$ be connected and let $f : X \to Y$ be a continuous surjection. Prove that $Y$ is connected.

**10.** Decide, with proof, whether the following spaces are connected and whether they are path connected:
(a) $S^1$; (b) $S^0 = \{-1,1\}$; (c) $S^1 \cup \{0\} \subseteq \mathbb{C}$.

**11.** Let $A = \{(x,0) : x \in \mathbb{R}\} \cup \{(0,y) : y \in \mathbb{R}\} \subseteq \mathbb{R}^2$ be the
union of the two coordinate axes. Prove that $A$ is connected and path connected.

## Intermediate

**12.** Let $A \subseteq X$ be connected and suppose $A \subseteq B \subseteq \overline A$. Prove that $B$ is
connected, using the characterisation "the only clopen subsets are $\varnothing$ and the whole space". Say
exactly where the hypothesis $B \subseteq \overline A$ is used.

**13.** (a) Prove that if $\{A_i\}_{i\in I}$ is a family of connected subsets of $X$ with
$\bigcap_{i\in I} A_i \neq \varnothing$, then $\bigcup_{i\in I} A_i$ is connected. (b) Give an example of two
connected subsets of $\mathbb{R}^2$ whose union is disconnected, and prove that the union is disconnected.
(c) Deduce that a union $A_1\cup\cdots\cup A_n$ of connected sets with $A_i \cap A_{i+1} \neq \varnothing$ is
connected.

**14.** Prove that a space $X$ is connected if and only if for every pair of points $x, y \in X$ there is a
connected subset $C \subseteq X$ with $x, y \in C$. Explain why this does *not* say that $X$ is path connected.

**15.** Let $q : X \to Y$ be a quotient map. Prove that if $X$ is connected then $Y$ is connected. Deduce that
the circle $\mathbb{R}/\mathbb{Z}$, obtained from $\mathbb{R}$ by identifying all integers to a single point,
is connected.

**16.** Let $X$ be connected and $f : X \to \mathbb{R}$ continuous. Prove that $f[X]$ is an interval, and
deduce the following general intermediate value theorem: if $a, b \in X$ and $y \in \mathbb{R}$ lies between
$f(a)$ and $f(b)$, then $f(x) = y$ for some $x \in X$.

**17.** A map $f : X \to Y$ is *locally constant* if every point of $X$ has a neighbourhood on which $f$ is
constant. Prove that if $X$ is connected, then every locally constant $f : X \to Y$ is constant.

**18.** Let $f : S^1 \to \mathbb{R}$ be continuous. Prove that there is $x \in S^1$ with $f(x) = f(-x)$.
(Hint: consider $g(t) = f(e^{2\pi i t}) - f(e^{2\pi i(t+1/2)})$ on $[0,\tfrac12]$.)

**19.** Prove that $S^n$ is path connected for every $n \ge 1$, and that $S^0$ is not connected.

**20.** Prove that $\mathbb{R}^n\setminus\{0\}$ is path connected for $n \ge 2$ by an explicit construction.
Show that $\mathbb{R}\setminus\{0\}$ is not connected, and deduce that $\mathbb{R} \not\cong \mathbb{R}^n$ for
$n \ge 2$ using the removal of a point.

**21.** Prove that if $X$ and $Y$ are path connected then $X\times Y$ is path connected. Deduce that the torus
$T^2 = S^1\times S^1$, the cylinder $S^1\times[0,1]$ and $\mathbb{R}^n$ are path connected.

## Advanced

**22.** Let $G = \{(x,\sin(1/x)) : 0 < x \le 1\}$ and $T = G\cup(\{0\}\times[-1,1]) \subseteq \mathbb{R}^2$.
Prove that $T$ is connected and that $T$ is not path connected. (Show that no path can join a point of
$\{0\}\times[-1,1]$ to a point of $G$; the argument must explain why $\sin(1/x)$ has two different limits along
the path.)

**23.** With $T$ as in Exercise 22, prove that $T$ is compact, that $T$ has exactly one component, and that $T$
has exactly two path components. Which of those path components is closed in $T$?

**24.** Prove that a connected and locally path connected space is path connected. State every hypothesis you
use, and explain why neither hypothesis can be dropped.

**25.** Prove that a space $X$ is locally connected if and only if for every open $U \subseteq X$ and every
component $C$ of $U$, the set $C$ is open in $X$.

**26.** Prove that every open subset of $\mathbb{R}^n$ is locally path connected, and deduce that its
components are exactly its path components and are open. Conclude that every connected open subset of
$\mathbb{R}^n$ is path connected, and explain why the word "open" cannot be replaced by "closed" (you may quote
Exercise 22).

**27.** Prove that every non-empty open subset of $\mathbb{R}$ is a countable disjoint union of open intervals.
(Show that the components are open intervals and that there are only countably many of them.)

**28.** Prove that the product of two connected spaces is connected, and extend the result to finite products
by induction. Where exactly is the non-emptiness of the factors needed?

**29.** Prove that an arbitrary product of non-empty connected spaces is connected. (Use that the set of points
differing from a fixed point in finitely many coordinates is connected and dense.)

**30.** Prove that a connected metric space with at least two points is uncountable. Deduce that $\mathbb{Q}$
and $\mathbb{R}\setminus\mathbb{Q}$, with the usual metric, are not connected.

## Challenge

**31.** The *deleted comb space* is
$C = \bigl([0,1]\times\{0\}\bigr) \cup \bigcup_{n\ge1}\bigl(\{1/n\}\times[0,1]\bigr) \cup \{(0,1)\}$.
Prove that $C$ is connected and that $C$ is not path connected. (The union without the point $(0,1)$ is the
*comb space*.)

**32.** Prove that there is no continuous injection $f : S^1 \to \mathbb{R}$. Deduce that $S^1$ is not
homeomorphic to $[0,1]$ and not homeomorphic to $\mathbb{R}$.

**33.** Use the removal of a single point to prove that $\mathbb{R}$ is not homeomorphic to $\mathbb{R}^n$ for
$n \ge 2$. Then explain precisely why the same method cannot distinguish $\mathbb{R}^2$ from $\mathbb{R}^3$.
(What would one have to compute instead?)

**34.** Prove that the topologist's sine curve $T$ of Exercise 22 is not locally connected at any point of
$\{0\}\times[-1,1]$.

**35.** Let $K \subseteq [0,1]$ be the Cantor set. Prove that $K$ is totally disconnected, that $K$ has no
isolated points, and that $K$ is not locally connected. Deduce that "totally disconnected" does not imply
"discrete" and that "compact and totally disconnected" does not imply "locally connected".

**36.** Prove that every interval of $\mathbb{R}$ containing at least two points has cardinality
$2^{\aleph_0}$. Deduce that every connected subset of $\mathbb{R}$ with at least two points has cardinality
$2^{\aleph_0}$, and compare with Exercise 30.
