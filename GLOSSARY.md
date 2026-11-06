# Glossary

This glossary fixes the vocabulary used throughout the repository. Each entry gives a precise
definition in one or two sentences and, where a genuine confusion exists, states the distinction
that is most often missed. Where the repository teaches the term in depth, the entry ends with a
link to that tutorial. Terms are listed alphabetically under their initial letter, and terms that
share a bare name are disambiguated by a parenthetical field, as in basis (of a topology) and basis
(of a vector space). All symbols follow [MATHEMATICAL_NOTATION.md](MATHEMATICAL_NOTATION.md).

## A

- **abelian group** — A group $(G,*)$ whose operation is commutative, so that $a*b=b*a$ for all
  $a,b\in G$. Not to be confused with a general group, where commutativity is not assumed, or with a ring,
  which carries two operations.
- **absolute continuity** — $f:[a,b]\to\mathbb{R}$ is absolutely continuous when for every $\varepsilon>0$
  there is $\delta>0$ such that $\sum_i\lvert f(b_i)-f(a_i)\rvert<\varepsilon$ for every finite family of
  pairwise disjoint subintervals of $[a,b]$ whose total length is less than $\delta$. Not to be confused
  with uniform continuity, which constrains one interval at a time and permits unbounded variation.
- **absolute value** — For $x\in\mathbb{R}$, $\lvert x\rvert=x$ when $x\ge0$ and $\lvert x\rvert=-x$ when
  $x<0$; it is the distance from $x$ to $0$. [Full treatment](01-arithmetic/02-integers/README.md) Not to
  be confused with the determinant $\lvert A\rvert$ of a matrix, despite the identical bars.
- **algebra over a field** — A vector space $A$ over a field $K$ equipped with a bilinear multiplication
  $A\times A\to A$. Not to be confused with a σ-algebra, which is a family of sets closed under
  complements and countable unions.
- **algebraic number** — A complex number that is a root of some nonzero polynomial with rational
  coefficients. Not to be confused with a transcendental number such as $\pi$, which is the root of no
  such polynomial.
- **almost everywhere** — A property holds almost everywhere with respect to a measure $\mu$ when the set
  on which it fails has measure zero.
- **alternating series** — A series whose terms alternate in sign, written $\sum_n(-1)^n a_n$; it
  converges whenever $a_n$ decreases to $0$ (Leibniz test). Not to be confused with a series that merely
  has some negative terms.
- **amplitude** — For $f(x)=A\sin(bx+c)+d$, the non-negative number $\lvert A\rvert$, which is half the
  distance between the maximum and minimum values.
- **angle** — The figure formed by two rays with a common endpoint, measured in radians as intercepted arc
  length divided by radius.
- **antiderivative** — A function $F$ with $F'(x)=f(x)$ on an interval; any two antiderivatives of $f$ on
  that interval differ by a constant. Not to be confused with the definite integral $\int_a^b f$, which is
  a number.
- **argument** — For $z\ne0$, an angle $\theta$ with $z=\lvert z\rvert(\cos\theta+i\sin\theta)$; it is
  determined only modulo $2\pi$ unless a branch is chosen. Not to be confused with the argument of a
  function, which is its input.
- **arithmetic mean** — The average $\frac{1}{n}(x_1+\dots+x_n)$ of $n$ numbers. Not to be confused with
  the geometric mean $(\prod_i x_i)^{1/n}$ or with the median.
- **associativity** — A binary operation is associative when $(a*b)*c=a*(b*c)$ for all $a,b,c$. Not to be
  confused with commutativity, which concerns the order of the operands rather than their grouping.
- **axiom** — A statement assumed without proof as part of the definition of a formal system; its
  consequences are the theorems of that system.
- **axiom of choice** — Every family of nonempty sets admits a choice function selecting one element from
  each member; it is independent of the other Zermelo–Fraenkel axioms and equivalent to Zorn's lemma.

## B

- **ball** — In a metric space, $B_r(x)=\{y:d(x,y)<r\}$ is the open ball of radius $r$ about $x$, and the
  closed ball uses $\le r$. Not to be confused with a sphere, which is the set $d(x,y)=r$ alone.
- **basis (of a topology)** — A family $\mathcal{B}$ of open sets whose unions are exactly the open sets
  of the topology.
- **basis (of a vector space)** — A linearly independent spanning set, so that every vector is a unique
  finite linear combination of its elements. Not to be confused with a basis of a topology.
- **Bayes' theorem** — For events with $\Pr(B)>0$, $\Pr(A\mid B)=\Pr(B\mid A)\Pr(A)/\Pr(B)$, which
  converts one conditional probability into the reverse conditional.
- **Bézout's identity** — For integers $a,b$ not both zero there exist integers $x,y$ with
  $ax+by=\gcd(a,b)$. [Full treatment](01-arithmetic/01-natural-numbers/README.md)
- **biconditional** — The statement $P\Leftrightarrow Q$, true exactly when $P$ and $Q$ have the same
  truth value; it asserts both implication directions at once.
- **bijection** — A map that is both injective and surjective, so every element of the codomain has
  exactly one preimage; these are precisely the maps that possess an inverse.
- **binomial coefficient** — $\binom{n}{k}=\frac{n!}{k!(n-k)!}$, the number of $k$-element subsets of an
  $n$-element set.
- **binomial distribution** — The law of the number of successes in $n$ independent trials with success
  probability $p$, with mass function $\binom{n}{k}p^k(1-p)^{n-k}$.
- **bipartite graph** — A graph whose vertices split into two classes such that every edge joins a vertex
  of one class to a vertex of the other.
- **bisection method** — A root-finding algorithm that repeatedly halves a sign-changing interval of a
  continuous function, always bracketing a root and converging linearly.
- **Bolzano–Weierstrass theorem** — Every bounded sequence of real numbers has a convergent subsequence;
  equivalently, every bounded infinite subset of $\mathbb{R}^n$ has a limit point.
- **Boolean algebra** — A complemented distributive lattice; the power set of a set under union,
  intersection and complement is the standard example.
- **boundary** — A point belongs to the boundary $\partial S$ when every neighbourhood of it meets both
  $S$ and the complement of $S$.
- **bounded set** — A subset of a metric space that lies inside some ball of finite radius; in
  $\mathbb{R}$ this means $\lvert x\rvert\le M$ for all elements. Not to be confused with compactness,
  which coincides with closed and bounded only in $\mathbb{R}^n$.

## C

- **cardinality** — The cardinality $\lvert A\rvert$ is the size of $A$ up to bijection, so two sets have
  equal cardinality exactly when a bijection joins them.
  [Full treatment](00-foundations/03-set-theory/README.md)
- **Cartesian product** — $A\times B=\{(a,b):a\in A,\ b\in B\}$, the set of ordered pairs with first
  coordinate in $A$ and second in $B$. [Full treatment](00-foundations/03-set-theory/README.md) Not to be
  confused with the union, which collects elements rather than pairing them.
- **category** — A collection of objects with morphisms between them, an identity morphism on each object,
  and associative composition of morphisms.
- **Cauchy sequence** — A sequence with $d(x_m,x_n)<\varepsilon$ for all $m,n\ge N$, where $N$ depends on
  $\varepsilon$. Not to be confused with a convergent sequence: convergence implies the Cauchy property,
  but the converse requires completeness.
- **central limit theorem** — For independent identically distributed $X_i$ with mean $\mu$ and finite
  variance $\sigma^2$, the standardised sums $\sqrt{n}(\bar X_n-\mu)/\sigma$ converge in distribution to
  $\mathcal{N}(0,1)$.
- **chromatic number** — The least number of colours needed to colour the vertices of a graph so that
  adjacent vertices receive different colours.
- **closed set** — A subset whose complement is open, equivalently one that contains all its limit points.
  Not to be confused with compactness, which additionally demands a finite subcover of every open cover.
- **closure** — The smallest closed set containing $S$, namely $S$ together with all its limit points.
- **codomain** — The set $B$ in a declaration $f:A\to B$, into which $f$ is declared to map. Not to be
  confused with the range $f[A]$, which may be a strictly smaller subset of $B$.
- **coefficient** — The numerical factor multiplying the variables in a term, as $7$ in $7x^2y$.
  [Full treatment](02-pre-algebra/02-variables-and-expressions/README.md)
- **combination** — A $k$-element subset chosen from $n$ objects without regard to order, of which there
  are $\binom{n}{k}$. Not to be confused with a permutation, which records order and is larger by a factor
  $k!$.
- **compactness** — Every open cover of the space has a finite subcover. Not to be confused with being
  closed and bounded, which is equivalent only in $\mathbb{R}^n$; in a general metric space compactness is
  strictly stronger.
- **complement (of a set)** — $A^{\complement}=\{x\in U:x\notin A\}$ relative to a fixed universe $U$.
  [Full treatment](00-foundations/03-set-theory/README.md)
- **complete metric space** — A metric space in which every Cauchy sequence converges.
- **complex number** — A number $a+bi$ with $a,b\in\mathbb{R}$ and $i^2=-1$; the complex numbers form the
  field $\mathbb{C}$.
- **composite number** — A natural number $n>1$ having a positive divisor other than $1$ and $n$. Not to
  be confused with $1$, which is neither prime nor composite.
- **conditional convergence** — A series that converges while the series of its absolute values diverges;
  by Riemann's rearrangement theorem its terms can be reordered to produce any sum.
- **conditional probability** — $\Pr(A\mid B)=\Pr(A\cap B)/\Pr(B)$ for $\Pr(B)>0$, the probability of $A$
  given that $B$ has occurred.
- **congruence (geometry)** — Two figures are congruent when an isometry maps one onto the other,
  preserving all distances and angles. Not to be confused with similarity, which permits a change of
  scale.
- **congruence (modular arithmetic)** — $a\equiv b\pmod n$ means $n\mid(a-b)$. Not to be confused with
  geometric congruence.
- **connected space** — A space that is not the union of two disjoint nonempty open sets. Not to be
  confused with path-connectedness, which implies connectedness but is not implied by it in general.
- **consistent system** — A system of equations possessing at least one solution.
  [Full treatment](03-algebra/05-systems-of-equations/README.md) Not to be confused with a homogeneous
  system, which is always consistent.
- **constant** — A quantity that does not vary in the expression or discussion at hand.
  [Full treatment](02-pre-algebra/02-variables-and-expressions/README.md) Not to be confused with a
  coefficient, which multiplies a variable.
- **continuous function** — $f$ is continuous at $a$ when for every neighbourhood $V$ of $f(a)$ some
  neighbourhood $U$ of $a$ satisfies $f[U]\subseteq V$; in metric spaces this is the
  $\varepsilon$-$\delta$ condition. Not to be confused with uniform continuity, which requires a single
  $\delta$ valid at all points.
- **contradiction** — A formula false under every truth assignment; its negation is a tautology. Not to be
  confused with a contingent formula, which is true under some assignments and false under others.
- **contrapositive** — The contrapositive of $P\Rightarrow Q$ is $\neg Q\Rightarrow\neg P$, which is
  logically equivalent to it. Not to be confused with the converse $Q\Rightarrow P$, which need not be
  equivalent.
- **convergent sequence** — A sequence with a limit $L$: for every $\varepsilon>0$ there is $N$ with
  $d(x_n,L)<\varepsilon$ for all $n\ge N$.
- **converse** — The converse of $P\Rightarrow Q$ is $Q\Rightarrow P$, which need not have the same truth
  value. Not to be confused with the contrapositive, which is equivalent to the original implication.
- **convex function** — A function with $f(tx+(1-t)y)\le tf(x)+(1-t)f(y)$ for all $x,y$ and $t\in[0,1]$;
  its epigraph is a convex set.
- **convex set** — A set that contains the line segment joining any two of its points.
- **correlation** — The correlation $\rho=\operatorname{Cov}(X,Y)/(\sigma_X\sigma_Y)$ is a number in
  $[-1,1]$ measuring linear association. Not to be confused with a causal relation, which correlation
  alone never establishes.
- **cosine** — The function $\cos\theta$ giving the $x$-coordinate of the point where the unit circle
  meets the ray at angle $\theta$ from the positive $x$-axis.
- **countable set** — A set that is finite or in bijection with $\mathbb{N}$, hence listable as a
  sequence. [Full treatment](00-foundations/03-set-theory/README.md) Not to be confused with dense, which
  concerns approximation rather than enumeration.
- **critical point** — A point where $f'(x)=0$ or where $f'(x)$ fails to exist; not every critical point
  is a local extremum.

## D

- **decimal** — A base-ten positional representation of a real number whose digits after the point stand
  for tenths, hundredths and so on. [Full treatment](01-arithmetic/04-decimals/README.md) Not to be
  confused with a rational number, which is a value rather than a notation.
- **degree (of a polynomial)** — The largest exponent whose coefficient is nonzero; the zero polynomial is
  conventionally left without a degree.
- **degree (of a vertex)** — The number of edges incident with a vertex, with loops counted twice.
- **dense set** — A subset whose closure is the whole space, equivalently one that meets every nonempty
  open set.
- **derivative** — $f'(a)=\lim_{h\to0}\frac{f(a+h)-f(a)}{h}$ when the limit exists, the instantaneous rate
  of change of $f$ at $a$.
- **determinant** — The scalar $\det A=\sum_\sigma\operatorname{sgn}(\sigma)\prod_i a_{i,\sigma(i)}$
  attached to a square matrix; it is the signed volume scaling factor and is nonzero exactly when $A$ is
  invertible.
- **diagonalisable** — A matrix is diagonalisable when $A=PDP^{-1}$ for some invertible $P$ and diagonal
  $D$, that is, when its eigenvectors span the space. Not to be confused with invertible, which is an
  unrelated property.
- **differentiable** — Having a derivative at the point in question. Not to be confused with continuous:
  differentiability implies continuity, never the reverse.
- **differential equation** — An equation relating an unknown function to some of its derivatives; its
  order is that of the highest derivative present.
- **dimension** — The cardinality of any basis of a vector space, which is independent of the basis
  chosen.
- **discriminant** — For $ax^2+bx+c=0$, the quantity $\Delta=b^2-4ac$, whose sign decides whether the
  roots are two distinct reals, one repeated real, or a non-real conjugate pair.
- **disjoint sets** — Sets with empty intersection; a family is pairwise disjoint when every two distinct
  members are disjoint. Not to be confused with independent events, which is a probabilistic condition.
- **distribution function** — $F_X(x)=\Pr(X\le x)$, which is nondecreasing and right-continuous with
  limits $0$ and $1$. Not to be confused with the density $f_X$, which exists only when $F_X$ is
  absolutely continuous.
- **divergent series** — A series whose sequence of partial sums fails to converge. Not to be confused
  with a series whose terms fail to tend to zero, which is one way, but not the only way, to diverge.
- **divisibility** — $a\mid b$ means $b=ak$ for some integer $k$.
  [Full treatment](01-arithmetic/01-natural-numbers/README.md) Not to be confused with the quotient $a/b$,
  which is a number.
- **division algorithm** — For integers $a$ and $b>0$ there exist unique integers $q,r$ with $a=bq+r$ and
  $0\le r<b$. [Full treatment](01-arithmetic/01-natural-numbers/README.md)
- **divisor** — An integer $d$ with $d\mid n$, also called a factor of $n$.
  [Full treatment](01-arithmetic/01-natural-numbers/README.md) Not to be confused with a multiple, which
  is the reverse relation.
- **domain** — The set $A$ on which a function $f:A\to B$ is defined. Not to be confused with the codomain
  $B$ or with the range $f[A]$.
- **dominated convergence theorem** — If $f_n\to f$ pointwise almost everywhere and
  $\lvert f_n\rvert\le g$ for an integrable $g$, then $\int f_n\to\int f$.
- **duality (optimisation)** — The association of a dual linear program to a primal one, whose optimal
  value bounds the primal value and equals it under constraint qualifications.

## E

- **edge** — An element of the edge set of a graph, joining two vertices, or one vertex in the case of a
  loop.
- **eigenvalue** — A scalar $\lambda$ for which $Av=\lambda v$ has a nonzero solution $v$, equivalently a
  root of $\det(A-\lambda I)=0$. Not to be confused with an eigenvector, which is the vector $v$ itself.
- **eigenvector** — A nonzero vector $v$ with $Av=\lambda v$ for some scalar $\lambda$; the zero vector is
  excluded by definition.
- **empty set** — The set $\varnothing$ with no elements; it is a subset of every set and is unique.
- **entire function** — A function holomorphic on all of $\mathbb{C}$; by Liouville's theorem a bounded
  entire function is constant.
- **equation** — A statement that two expressions are equal, to be solved for the values of its variables
  that make it true. [Full treatment](02-pre-algebra/01-order-of-operations/README.md) Not to be confused
  with an identity, which holds for every value of its variables.
- **equivalence class** — The set $[a]=\{x:x\sim a\}$ of all elements equivalent to $a$ under an
  equivalence relation.
- **equivalence relation** — A relation that is reflexive, symmetric and transitive; its equivalence
  classes partition the underlying set.
- **estimator** — A statistic used to estimate an unknown parameter; it is a random variable, and its
  realised value is called an estimate.
- **Euclidean algorithm** — The repeated use of the division algorithm, $\gcd(a,b)=\gcd(b,a\bmod b)$,
  which computes the greatest common divisor. [Full treatment](01-arithmetic/01-natural-numbers/README.md)
- **Euler characteristic** — For a finite graph, $\chi=V-E$; for a surface, $V-E+F$ of any triangulation,
  which is a topological invariant equal to $2-2g$ for a closed orientable surface of genus $g$.
- **Euler tour** — A closed walk using every edge of a graph exactly once; one exists exactly when all
  vertices of nonzero degree lie in one component and every vertex has even degree.
- **Euler's formula** — $e^{i\theta}=\cos\theta+i\sin\theta$, which links the exponential and
  trigonometric functions; the case $\theta=\pi$ yields $e^{i\pi}+1=0$.
- **Euler's totient function** — The function $\varphi(n)$ counting the integers $1\le k\le n$ with
  $\gcd(k,n)=1$.
- **event** — A subset of a sample space, that is, a measurable set of outcomes.
- **expectation** — The expected value $\mathbb{E}[X]=\sum_k k\Pr(X=k)$ in the discrete case and
  $\int_{\mathbb{R}}x f_X(x)\,dx$ in the continuous case, whenever the sum or integral converges
  absolutely.
- **exponential function** — The map $x\mapsto e^x$, the unique function equal to its own derivative with
  $e^0=1$ and the inverse of the natural logarithm.
- **expression** — A combination of numbers, variables and operations that denotes a value.
  [Full treatment](02-pre-algebra/02-variables-and-expressions/README.md) Not to be confused with an
  equation, which asserts equality between two expressions.
- **extreme value theorem** — A continuous real function on a nonempty compact set attains a maximum and a
  minimum there. Not to be confused with the intermediate value theorem, which concerns intermediate
  values rather than extrema.

## F

- **factorial** — The product $n!=1\cdot2\cdots n$ for $n\ge1$, with $0!=1$; it counts the permutations of
  $n$ objects.
- **feasible region** — The set of points satisfying all constraints of an optimisation problem.
- **Fermat's little theorem** — If $p$ is prime and $p\nmid a$, then $a^{p-1}\equiv1\pmod p$; equivalently
  $a^p\equiv a\pmod p$ for every integer $a$.
- **field** — A commutative ring with identity in which every nonzero element has a multiplicative
  inverse; $\mathbb{Q}$, $\mathbb{R}$, $\mathbb{C}$ and $\mathbb{F}_p$ are fields. Not to be confused with
  a ring, which need not have inverses.
- **floating point** — A representation of a real number as $\pm m\cdot\beta^{e}$ with a fixed number of
  significand digits, so that representable numbers are finite in number and unevenly spaced.
- **Fourier series** — The expansion of a periodic function as $a_0+\sum_{n\ge1}(a_n\cos nx+b_n\sin nx)$,
  studied for its convergence and used to solve linear partial differential equations.
- **fraction** — A quotient $a/b$ of integers with $b\ne0$, denoting the rational number $a\cdot b^{-1}$.
  Not to be confused with a ratio, which compares two quantities and need not be a number.
- **function** — A rule assigning to each element of a set $A$ exactly one element of a set $B$; formally
  a subset of $A\times B$ containing exactly one pair with each first coordinate. Not to be confused with
  a relation, which may assign none or several values.
- **functor** — A map between categories sending objects to objects and morphisms to morphisms while
  preserving identities and composition.
- **fundamental group** — The group $\pi_1(X,x_0)$ of homotopy classes of loops based at $x_0$, with
  concatenation as the operation; it records holes that cannot be filled in.
- **fundamental theorem of arithmetic** — Every integer $n>1$ factors into primes, uniquely up to the
  order of the factors. [Full treatment](01-arithmetic/01-natural-numbers/README.md) Not to be confused
  with the fundamental theorem of algebra, which states that every nonconstant complex polynomial has a
  root.
- **fundamental theorem of calculus** — If $f$ is continuous on $[a,b]$ and $F(x)=\int_a^x f$, then
  $F'=f$; and if $G'=f$ there, then $\int_a^b f=G(b)-G(a)$. It links the two central operations of
  calculus.

## G

- **Galois group** — The group of automorphisms of a field extension that fix the base field; it measures
  the symmetry of the extension and decides solvability by radicals.
- **Gaussian elimination** — The systematic use of row operations to reduce a matrix to row echelon form,
  thereby solving a linear system.
- **generating function** — A formal power series $\sum_{n\ge0}a_nx^n$ encoding a sequence $(a_n)$, so
  that algebraic operations on the series mirror combinatorial operations on the sequence.
- **genus** — For a connected closed orientable surface, the number of handles attached to a sphere; it
  equals $(2-\chi)/2$ for Euler characteristic $\chi$.
- **geometric series** — A series $\sum_{n\ge0}ar^n$, which converges to $a/(1-r)$ when $\lvert r\rvert<1$
  and diverges otherwise.
- **gradient** — The vector $\nabla f=(\partial f/\partial x_1,\dots,\partial f/\partial x_n)$ of partial
  derivatives, pointing in the direction of steepest increase.
- **graph (of a function)** — The set $\{(x,f(x)):x\in A\}$ as a subset of $A\times B$.
- **graph (of a network)** — A pair $G=(V,E)$ consisting of a vertex set and an edge set whose elements
  join pairs of vertices.
- **greatest common divisor** — The largest positive integer $\gcd(a,b)$ dividing both $a$ and $b$.
  [Full treatment](01-arithmetic/01-natural-numbers/README.md) Not to be confused with the least common
  multiple.
- **group** — A set with an associative binary operation, an identity element, and an inverse for every
  element. Not to be confused with a ring, which has two operations and need not admit multiplicative
  inverses.

## H

- **Hamiltonian cycle** — A cycle in a graph that visits every vertex exactly once and returns to its
  starting point. Not to be confused with an Euler tour, which uses every edge exactly once instead.
- **harmonic function** — A twice-differentiable function with $\nabla^2u=0$; its value at a point equals
  the average of its values on surrounding spheres.
- **Hausdorff space** — A topological space in which any two distinct points have disjoint neighbourhoods;
  limits of sequences are then unique.
- **Heine–Borel theorem** — A subset of $\mathbb{R}^n$ is compact if and only if it is closed and bounded.
- **holomorphic function** — A complex function differentiable in a neighbourhood of each point of its
  domain; such functions are analytic, being given locally by power series.
- **homeomorphism** — A continuous bijection whose inverse is continuous, the isomorphism of topological
  spaces. Not to be confused with a homomorphism, which need not be bijective, or with an isometry, which
  preserves distances.
- **homogeneous system** — A system whose equations all have zero right-hand side, $Ax=0$; it is always
  consistent because $x=0$ is a solution. [Full treatment](03-algebra/05-systems-of-equations/README.md)
- **homomorphism** — A map between algebraic structures of the same kind that preserves the operations, as
  $f(ab)=f(a)f(b)$ for groups. Not to be confused with an isomorphism, which is a bijective homomorphism.
- **hypothesis test** — A decision procedure that rejects or fails to reject a null hypothesis according
  to whether a test statistic falls in a specified critical region.

## I

- **ideal** — A subset $I$ of a ring $R$ that is a subgroup under addition and is closed under
  multiplication by every element of $R$ on both sides; these are exactly the kernels of ring
  homomorphisms. Not to be confused with a subgroup, the corresponding notion for groups.
- **identity element** — An element $e$ with $e*a=a*e=a$ for every $a$; it is unique when it exists.
- **identity (equation)** — An equality that holds for every value of its variables, such as
  $\sin^2x+\cos^2x=1$. Not to be confused with an equation, which holds only for particular values and
  poses a problem.
- **image (of a function)** — For $f:A\to B$ and $S\subseteq A$, the set $f[S]=\{f(x):x\in S\}$; the image
  of the whole domain is the range. Not to be confused with the preimage $f^{-1}[T]$, which is a subset of
  the domain.
- **improper integral** — A limit of proper integrals, either $\lim_{b\to\infty}\int_a^b f$ or
  $\int_a^b f$ where $f$ is unbounded at an endpoint; it converges when that limit exists and is finite.
- **inclusion–exclusion** — The identity
  $\lvert A\cup B\rvert=\lvert A\rvert+\lvert B\rvert-\lvert A\cap B\rvert$, extended to $n$ sets by
  alternating sums of intersections.
- **independent events** — Events with $\Pr(A\cap B)=\Pr(A)\Pr(B)$, equivalently $\Pr(A\mid B)=\Pr(A)$
  when $\Pr(B)>0$. Not to be confused with mutually exclusive events, which satisfy $A\cap B=\varnothing$
  and are dependent whenever both have positive probability.
- **induction** — To prove $P(n)$ for all $n\ge n_0$, prove $P(n_0)$ and prove that $P(n)$ implies
  $P(n+1)$; the principle is equivalent to well-ordering of $\mathbb{N}$.
  [Full treatment](01-arithmetic/01-natural-numbers/README.md)
- **inequality** — A statement that one quantity is less than, at most, greater than or at least another,
  such as $2x+1\le7$. [Full treatment](03-algebra/03-inequalities/README.md) Not to be confused with an
  equation, which asserts equality.
- **infimum** — The greatest lower bound of a set $S$, written $\inf S$; it need not belong to $S$. Not to
  be confused with the minimum, which must be an element of $S$.
- **injection** — A map $f:A\to B$ with $f(x)=f(y)\Rightarrow x=y$, so distinct inputs have distinct
  images; also called one-to-one. Not to be confused with a surjection, which concerns coverage of the
  codomain.
- **inner product** — A map $\langle\cdot,\cdot\rangle$ on a real or complex vector space that is bilinear
  or sesquilinear, symmetric or Hermitian, and positive definite; it induces the norm
  $\lVert v\rVert=\sqrt{\langle v,v\rangle}$.
- **integer** — A whole number $\dots,-2,-1,0,1,2,\dots$; the integers form the ring $\mathbb{Z}$.
  [Full treatment](01-arithmetic/02-integers/README.md)
- **integrable function** — A function for which a specified integral exists; Riemann integrability and
  Lebesgue integrability are different conditions, and every Riemann integrable function is Lebesgue
  integrable.
- **integral domain** — A commutative ring with identity and no zero divisors; every field is an integral
  domain, but $\mathbb{Z}$ is an integral domain that is not a field.
- **interior** — The largest open set contained in $S$, written $S^\circ$, consisting of the points having
  a neighbourhood inside $S$. Not to be confused with the closure, the smallest closed set containing $S$.
- **intermediate value theorem** — A continuous real function on an interval attains every value lying
  between any two of its values.
- **interpolation** — The construction of a function, usually a polynomial, passing through a given finite
  set of points.
- **intersection** — The set $A\cap B=\{x:x\in A\ \text{and}\ x\in B\}$.
  [Full treatment](00-foundations/03-set-theory/README.md)
- **interval** — A subset of $\mathbb{R}$ containing every point between any two of its points, written
  $[a,b]$, $(a,b)$, $[a,b)$ or $(a,b]$. [Full treatment](03-algebra/03-inequalities/README.md)
- **inverse function** — For a bijection $f:A\to B$, the map $f^{-1}:B\to A$ with $f^{-1}(f(x))=x$ and
  $f(f^{-1}(y))=y$. Not to be confused with the reciprocal $1/f(x)$, which differs even for real
  functions.
- **irrational number** — A real number that is not rational, such as $\sqrt2$ or $\pi$; its decimal
  expansion neither terminates nor becomes eventually periodic.
- **isomorphism** — A bijective structure-preserving map; two structures are isomorphic when such a map
  exists, and they are then indistinguishable in the language of that structure.

## J

- **Jacobian** — The matrix $J_f$ of partial derivatives of $f:\mathbb{R}^n\to\mathbb{R}^m$; when $m=n$,
  its determinant measures the local volume scaling factor of $f$.
- **Jordan canonical form** — A block-diagonal form of a complex square matrix, unique up to order of the
  blocks, in which each block records one eigenvalue together with the size of its generalised eigenspace.

## K

- **kernel** — For a group homomorphism $f:G\to H$, the set $\ker f=\{g:f(g)=e_H\}$; for a linear map, its
  kernel is the null space. Not to be confused with the image, which lies in the codomain.
- **Kolmogorov axioms** — The axioms of a probability measure: $\Pr(\Omega)=1$, countable additivity on
  disjoint events, and non-negativity.
- **Kronecker delta** — The symbol $\delta_{ij}$, equal to $1$ when $i=j$ and to $0$ otherwise.

## L

- **Lagrange multipliers** — A method for constrained extrema of $f$ subject to $g=0$: at a regular
  extremum $\nabla f=\lambda\nabla g$. Not to be confused with the unconstrained condition $\nabla f=0$,
  which is insufficient when constraints are present.
- **Lagrange's theorem** — For a finite group $G$ and a subgroup $H$,
  $\lvert G\rvert=\lvert H\rvert\cdot[G:H]$, so the order of every element divides $\lvert G\rvert$.
- **Laplace transform** — The map $\mathcal{L}\{f\}(s)=\int_0^\infty e^{-st}f(t)\,dt$, which turns linear
  differential equations with initial conditions into algebraic equations.
- **Laurent series** — The expansion $\sum_{n=-\infty}^{\infty}a_n(z-z_0)^n$ of a function holomorphic in
  an annulus about $z_0$; the coefficient $a_{-1}$ is the residue.
- **law of large numbers** — For independent identically distributed $X_i$ with finite mean $\mu$, the
  sample average $\bar X_n$ converges to $\mu$ in probability (weak law) and almost surely (strong law).
- **least common multiple** — The smallest positive integer divisible by both $a$ and $b$, written
  $\operatorname{lcm}(a,b)$. [Full treatment](01-arithmetic/01-natural-numbers/README.md) Not to be
  confused with the greatest common divisor.
- **Lebesgue integral** — The integral defined for $f\ge0$ by $\int f=\int_0^\infty\mu(\{f>t\})\,dt$ and
  extended by $f=f^+-f^-$; it agrees with the Riemann integral where the latter exists but integrates many
  more functions.
- **Lebesgue measure** — The unique translation-invariant complete measure on $\mathbb{R}$ that extends
  length on intervals.
- **l'Hôpital's rule** — If $f$ and $g$ both tend to $0$ or both tend to $\pm\infty$ at $a$, and $f'/g'$
  has a limit there, then $\lim_{x\to a}f(x)/g(x)=\lim_{x\to a}f'(x)/g'(x)$.
- **limit** — $\lim_{x\to a}f(x)=L$ when for every $\varepsilon>0$ there is $\delta>0$ such that
  $0<\lvert x-a\rvert<\delta$ implies $\lvert f(x)-L\rvert<\varepsilon$; the value $f(a)$ is irrelevant.
  Not to be confused with continuity, which additionally requires the limit to equal $f(a)$.
- **limit point** — A point every neighbourhood of which contains a point of $S$ other than itself. Not to
  be confused with an isolated point of $S$, which has a neighbourhood meeting $S$ only at that point.
- **line** — A straight one-dimensional Euclidean figure determined by two distinct points and extending
  without end in both directions. Not to be confused with a line segment, which has two endpoints, or a
  ray, which has one.
- **linear combination** — A sum $\sum_i c_iv_i$ of vectors with scalar coefficients.
- **linear independence** — Vectors $v_1,\dots,v_k$ are linearly independent when $\sum_i c_iv_i=0$ forces
  every $c_i=0$. Not to be confused with orthogonality, a metric condition: orthogonal nonzero vectors are
  independent, but independent vectors need not be orthogonal.
- **linear map** — A map $T:U\to V$ with $T(au+bv)=aT(u)+bT(v)$ for all scalars $a,b$ and vectors $u,v$.
  Not to be confused with an affine map, which may also translate.
- **linear programming** — The optimisation of a linear objective function subject to finitely many linear
  inequality constraints.
- **Lipschitz continuity** — $f$ is $L$-Lipschitz when $d(f(x),f(y))\le L\,d(x,y)$ for all $x,y$; this
  implies uniform continuity, and the case $L<1$ makes $f$ a contraction.
- **logarithm** — $\log_a x$ is the exponent to which $a$ must be raised to give $x$; it is the inverse of
  the exponential $a^x$ and is defined for $x>0$.

## M

- **machine epsilon** — The difference between $1$ and the next larger floating-point number; it bounds
  the relative rounding error of a single operation.
- **manifold** — A topological space locally homeomorphic to $\mathbb{R}^n$; a smooth manifold carries an
  atlas whose transition maps are smooth.
- **Markov chain** — A sequence of random variables with
  $\Pr(X_{n+1}\in A\mid X_0,\dots,X_n)=\Pr(X_{n+1}\in A\mid X_n)$, the Markov or memoryless property.
- **matrix** — A rectangular array $A=(a_{ij})$ of scalars, which represents a linear map once bases are
  fixed.
- **maximum** — An element $m\in S$ with $m\ge x$ for every $x\in S$; it need not exist even when $S$ is
  bounded above. Not to be confused with the supremum, which exists under weaker hypotheses but may lie
  outside $S$.
- **mean value theorem** — If $f$ is continuous on $[a,b]$ and differentiable on $(a,b)$, then
  $f'(c)=\frac{f(b)-f(a)}{b-a}$ for some $c\in(a,b)$.
- **measurable function** — A function $f:(X,\mathcal{A})\to(Y,\mathcal{B})$ with
  $f^{-1}[B]\in\mathcal{A}$ for every $B\in\mathcal{B}$.
- **measure** — A countably additive function $\mu$ on a σ-algebra with $\mu(\varnothing)=0$ and
  $\mu(A)\ge0$ for every measurable $A$.
- **median** — A value splitting ordered data into two halves of equal size; for an even count it is
  conventionally the mean of the two central values.
- **metric space** — A set with a distance $d:X\times X\to[0,\infty)$ that is positive definite, symmetric
  and satisfies the triangle inequality.
- **minimum** — An element of $S$ that is less than or equal to every element of $S$. Not to be confused
  with the infimum, which may lie outside $S$.
- **Möbius transformation** — A map $z\mapsto\frac{az+b}{cz+d}$ with $ad-bc\ne0$; it is a bijection of the
  Riemann sphere sending circles and lines to circles and lines.
- **modulus (of a complex number)** — The number $\lvert z\rvert=\sqrt{a^2+b^2}$ for $z=a+bi$, the
  distance from $z$ to the origin. Not to be confused with the modulus of a congruence, which is a
  positive integer in modular arithmetic.
- **monotone convergence theorem** — A nondecreasing sequence bounded above converges, and for measurable
  $f_n\uparrow f\ge0$ one has $\int f_n\to\int f$.
- **morphism** — An arrow of a category, that is, a structure-preserving map between objects in the
  categorical sense.
- **mutually exclusive events** — Events $A,B$ with $A\cap B=\varnothing$, so that
  $\Pr(A\cup B)=\Pr(A)+\Pr(B)$. Not to be confused with independent events: mutually exclusive events of
  positive probability are never independent.

## N

- **natural number** — An element of $\mathbb{N}=\{1,2,3,\dots\}$, this repository writing $\mathbb{N}_0$
  when $0$ is included, characterised by the Peano axioms.
  [Full treatment](01-arithmetic/01-natural-numbers/README.md)
- **neighbourhood** — A set containing an open set that contains $x$; in a metric space the balls $B_r(x)$
  are the basic neighbourhoods.
- **Newton's method** — The iteration $x_{n+1}=x_n-f(x_n)/f'(x_n)$, which converges quadratically near a
  simple root but may diverge or cycle otherwise.
- **norm** — A function on a vector space that is positive definite, homogeneous and satisfies the
  triangle inequality; it induces the metric $d(x,y)=\lVert x-y\rVert$.
- **normal distribution** — The law $\mathcal{N}(\mu,\sigma^2)$ with density
  $\frac{1}{\sigma\sqrt{2\pi}}e^{-(x-\mu)^2/(2\sigma^2)}$.
- **normal subgroup** — A subgroup $N\le G$ with $gNg^{-1}=N$ for every $g\in G$; these are exactly the
  subgroups for which $G/N$ is a group.
- **null set** — A set of measure zero, that is, one coverable by open sets of arbitrarily small total
  measure.
- **nullity** — The dimension of the kernel of a linear map $T$; it satisfies
  $\operatorname{nullity}T+\operatorname{rank}T=\dim V$.

## O

- **objective function** — The function to be maximised or minimised in an optimisation problem.
- **open set** — A member of a topology; in a metric space, a set $U$ such that every point of $U$ has a
  ball $B_r(x)\subseteq U$. Not to be confused with a closed set, which is the complement of an open set:
  a set can be both, or neither.
- **order (of a group element)** — The least $n>0$ with $g^n=e$, or infinity when no such $n$ exists; for
  a finite group it divides $\lvert G\rvert$.
- **order of operations** — The convention that grouping symbols come first, then exponentiation, then
  multiplication and division left to right, then addition and subtraction left to right.
  [Full treatment](02-pre-algebra/01-order-of-operations/README.md)
- **ordinal** — A set that is transitive and well-ordered by membership; ordinals extend the natural
  numbers into the transfinite and measure the order type of well-ordered sets.
- **orthogonal matrix** — A real square matrix with $Q^{\mathsf T}Q=I$; it preserves the dot product and
  represents a rotation or a reflection.
- **orthonormal basis** — A basis whose vectors are pairwise orthogonal and of unit length; coordinates in
  such a basis are given by inner products.

## P

- **parabola** — The locus of points equidistant from a focus and a directrix; the graph of a quadratic
  $y=ax^2+bx+c$ is a parabola.
- **parameter** — A quantity fixed within one instance of a problem but varying across a family of
  problems. Not to be confused with the variable of an equation, which is what one solves for.
- **partial derivative** — The derivative $\partial f/\partial x_i$ with respect to $x_i$ holding the
  other variables fixed. Not to be confused with the total derivative, which accounts for every
  dependence.
- **partition (of a set)** — A family of pairwise disjoint nonempty subsets whose union is the whole set;
  partitions correspond exactly to equivalence relations.
- **percentage** — A ratio expressed with denominator $100$ and written with the symbol $\%$.
- **permutation** — A bijection of a finite set to itself, or an ordered arrangement of $k$ objects chosen
  from $n$, of which there are $n!/(n-k)!$. Not to be confused with a combination, which ignores order.
- **Picard–Lindelöf theorem** — If $f(t,y)$ is continuous and Lipschitz in $y$ near $(t_0,y_0)$, then the
  initial value problem $y'=f(t,y)$, $y(t_0)=y_0$ has a unique solution on some interval about $t_0$.
- **pigeonhole principle** — If $n$ objects are placed in $m<n$ boxes, then some box contains at least two
  objects.
- **place value** — The value a digit carries by virtue of its position, each position being ten times the
  one to its right in base ten. [Full treatment](01-arithmetic/04-decimals/README.md)
- **pointwise convergence** — $f_n\to f$ pointwise when $f_n(x)\to f(x)$ for each $x$ separately. Not to
  be confused with uniform convergence, which requires one rate of convergence valid for all $x$.
- **pole** — An isolated singularity $z_0$ at which $\lvert f(z)\rvert\to\infty$ as $z\to z_0$; locally
  $f(z)=g(z)/(z-z_0)^m$ with $g$ holomorphic and $g(z_0)\ne0$.
- **polynomial** — A finite sum $\sum_{k=0}^{n}a_kx^k$ with non-negative integer exponents, of degree $n$
  when $a_n\ne0$.
- **population** — The entire set of units about which a statistical inference is to be made. Not to be
  confused with a sample, the subset actually observed.
- **power series** — A series $\sum_{n\ge0}a_n(z-z_0)^n$, which converges absolutely on an open disc and
  defines a holomorphic function there.
- **power set** — The set $\mathcal{P}(A)$ of all subsets of $A$, which has $2^{\lvert A\rvert}$ elements
  when $A$ is finite. [Full treatment](00-foundations/03-set-theory/README.md)
- **prime number** — An integer $p>1$ whose only positive divisors are $1$ and $p$.
  [Full treatment](01-arithmetic/01-natural-numbers/README.md) Not to be confused with a composite number;
  $1$ is neither prime nor composite.
- **probability density function** — A non-negative $f_X$ with $\Pr(a\le X\le b)=\int_a^bf_X(x)\,dx$ for a
  continuous random variable. Not to be confused with a probability mass function, and note that $f_X(x)$
  is not a probability and may exceed $1$.
- **probability mass function** — The function $p_X(k)=\Pr(X=k)$ of a discrete random variable.
- **probability space** — A triple $(\Omega,\mathcal{F},\Pr)$ consisting of a sample space, a σ-algebra of
  events, and a probability measure.
- **proportion** — A statement that two ratios are equal, $a/b=c/d$.
  [Full treatment](01-arithmetic/06-ratios-and-proportions/README.md)
- **proposition** — A declarative statement that is either true or false, and not both.
- **p-value** — The probability, computed under the null hypothesis, that a test statistic is at least as
  extreme as the value observed.

## Q

- **quadratic equation** — An equation $ax^2+bx+c=0$ with $a\ne0$, whose solutions over $\mathbb{C}$ are
  $\frac{-b\pm\sqrt{b^2-4ac}}{2a}$.
- **quantifier** — The symbol $\forall$ (for all) or $\exists$ (there exists); the order of quantifiers
  changes meaning, since $\forall x\exists y$ and $\exists y\forall x$ differ.
- **quotient group** — For a normal subgroup $N\trianglelefteq G$, the group $G/N$ of cosets with
  multiplication $(aN)(bN)=abN$.
- **quotient topology** — The finest topology on a quotient set that makes the quotient map continuous.

## R

- **radian** — The angle subtended at the centre of a circle by an arc whose length equals the radius; a
  full turn is $2\pi$ radians. Not to be confused with degrees, of which a full turn is $360$.
- **radius of convergence** — For a power series $\sum a_n(z-z_0)^n$, the number
  $R=\sup\{r\ge0:\sum\lvert a_n\rvert r^n<\infty\}$, inside which the series converges absolutely and
  outside which it diverges.
- **random variable** — A measurable function $X:\Omega\to\mathbb{R}$ on a probability space, which
  transports the probability measure to a distribution on the real line.
- **range** — The set $f[A]=\{f(x):x\in A\}$ of values actually taken by $f:A\to B$. Not to be confused
  with the codomain $B$, which is the declared target and may be strictly larger.
- **rank** — The dimension of the image of a linear map; for a matrix, the dimension of its column space,
  equal to the number of pivots in row echelon form.
- **rank–nullity theorem** — For a linear map $T:V\to W$ with $V$ finite-dimensional,
  $\dim\ker T+\dim\operatorname{im}T=\dim V$.
- **ratio** — A comparison of two quantities by division, written $a:b$ or $a/b$.
  [Full treatment](01-arithmetic/06-ratios-and-proportions/README.md) Not to be confused with a fraction,
  which denotes a single rational number.
- **rational number** — A number expressible as $p/q$ with integers $p,q$ and $q\ne0$; its decimal
  expansion terminates or eventually repeats. Not to be confused with a decimal numeral, which is only one
  way of writing it.
- **real number** — An element of the complete ordered field $\mathbb{R}$, obtainable as a limit of Cauchy
  sequences of rationals; every real number has a decimal expansion and every decimal expansion defines a
  real number. [Full treatment](01-arithmetic/04-decimals/README.md)
- **recurrence relation** — An equation expressing each term of a sequence in terms of earlier terms, such
  as $a_{n+1}=a_n+a_{n-1}$.
- **regression** — The modelling of the conditional mean of a response variable as a function of
  predictors, usually by minimising squared error within a parametric family.
- **relation** — A subset $R\subseteq A\times B$; a relation on $A$ is a subset of $A\times A$. Not to be
  confused with a function, which is a relation with exactly one second component for each first
  component.
- **residue** — The coefficient $a_{-1}$ in the Laurent expansion of $f$ about an isolated singularity
  $z_0$, written $\operatorname{Res}(f,z_0)$.
- **residue theorem** — For a function meromorphic inside a closed contour $\gamma$,
  $\oint_\gamma f(z)\,dz=2\pi i\sum_k\operatorname{Res}(f,z_k)$, summed over the enclosed singularities.
- **Riemann integral** — The limit of Riemann sums $\sum_i f(\xi_i)(x_i-x_{i-1})$ over partitions as the
  mesh tends to zero, when that limit exists independently of the tags $\xi_i$.
- **ring** — A set with two operations, the first forming an abelian group and the second associative and
  distributive over the first. Not to be confused with a group, which has one operation, or with a field,
  which is a commutative ring in which every nonzero element has a multiplicative inverse.
- **Rolle's theorem** — If $f$ is continuous on $[a,b]$, differentiable on $(a,b)$ and $f(a)=f(b)$, then
  $f'(c)=0$ for some $c\in(a,b)$.
- **root (of a polynomial)** — A value $r$ with $p(r)=0$; over $\mathbb{C}$ a polynomial of degree $n$ has
  exactly $n$ roots counted with multiplicity. Not to be confused with the root of a number, such as
  $\sqrt2$, which is an algebraic operation on a value.
- **row echelon form** — A form of a matrix in which the leading nonzero entry of each row lies strictly
  to the right of the leading entry of the row above, and all entries below a leading entry are zero.

## S

- **saddle point** — A stationary point that is not a local extremum; for a smooth function it is a point
  where the Hessian has both positive and negative eigenvalues.
- **sample** — The subset of a population that is actually observed. Not to be confused with a sample
  space, which is the set of all possible outcomes of an experiment.
- **sample space** — The set $\Omega$ of all outcomes of a probabilistic experiment.
- **satisfiable** — A propositional formula is satisfiable when some truth assignment makes it true, and
  valid when every assignment does.
- **sequence** — A function from $\mathbb{N}$, or a subset of it, to a set, written $(a_n)$. Not to be
  confused with a series, which is defined through the partial sums of a sequence.
- **series** — The formal sum $\sum_n a_n$ together with the limit of its partial sums
  $s_N=\sum_{n\le N}a_n$; it converges when that limit exists. Not to be confused with a sequence, whose
  terms are merely listed rather than added.
- **set** — A collection of distinct objects regarded as a single entity, with membership written
  $x\in A$. [Full treatment](00-foundations/03-set-theory/README.md)
- **σ-algebra** — A family $\mathcal{A}$ of subsets of $X$ containing $X$ and closed under complements and
  countable unions; its members are the measurable sets. Not to be confused with an algebra over a field.
- **similar triangles** — Triangles with equal corresponding angles, and hence proportional corresponding
  sides; similarity preserves shape but not size. Not to be confused with congruence, which preserves size
  as well.
- **sine** — The function $\sin\theta$ giving the $y$-coordinate of the point where the unit circle meets
  the ray at angle $\theta$ from the positive $x$-axis.
- **singularity** — A point at which a function fails to be holomorphic; an isolated singularity is
  removable, a pole, or essential.
- **span** — The set of all finite linear combinations of a set of vectors, which is the smallest subspace
  containing them.
- **spanning tree** — A subgraph that is a tree and contains every vertex of the graph.
- **standard deviation** — The square root of the variance, in the same units as the data; for a sample,
  $s=\sqrt{\frac{1}{n-1}\sum_i(x_i-\bar x)^2}$.
- **statistic** — A function of the observed sample that does not depend on unknown parameters. Not to be
  confused with a parameter, which describes the population.
- **subsequence** — A sequence obtained by deleting terms of a sequence while preserving the order of
  those retained.
- **subset** — $A\subseteq B$ when every element of $A$ is an element of $B$.
  [Full treatment](00-foundations/03-set-theory/README.md) Not to be confused with a proper subset
  $A\subsetneq B$, which excludes equality.
- **subspace** — A subset of a vector space closed under addition and scalar multiplication, or a subset
  of a topological space carrying the subspace topology.
- **supremum** — The least upper bound of a set $S$, written $\sup S$, that is, the smallest $u$ with
  $x\le u$ for all $x\in S$. Not to be confused with the maximum, which must belong to $S$.
- **surjection** — A map $f:A\to B$ with $f[A]=B$, so every element of the codomain is hit; also called
  onto. Not to be confused with an injection, which concerns distinctness of images.
- **symmetric difference** — The set $A\triangle B=(A\setminus B)\cup(B\setminus A)$ of elements belonging
  to exactly one of $A$ and $B$.
- **symmetric group** — The group $S_n$ of all permutations of an $n$-element set under composition, of
  order $n!$.
- **system of linear equations** — A finite collection of linear equations to be satisfied simultaneously
  by one tuple of unknowns. [Full treatment](03-algebra/05-systems-of-equations/README.md) Not to be
  confused with a single linear equation, whose solution set is one hyperplane rather than an intersection
  of hyperplanes.

## T

- **tangent line** — The line through a point of a curve whose slope is the derivative there, the best
  linear approximation to the curve at that point. Not to be confused with the tangent function
  $\tan\theta=\sin\theta/\cos\theta$.
- **tautology** — A formula true under every truth assignment, such as $P\lor\neg P$.
- **Taylor series** — The power series $\sum_{n\ge0}\frac{f^{(n)}(a)}{n!}(x-a)^n$ of a smooth function
  about $a$; it represents $f$ on a neighbourhood only when the remainder tends to zero.
- **Taylor's theorem** — The identity $f(x)=\sum_{k=0}^{n}\frac{f^{(k)}(a)}{k!}(x-a)^k+R_n(x)$, with the
  remainder $R_n$ given in Lagrange or integral form under suitable hypotheses.
- **term** — A summand of an expression, consisting of a coefficient multiplied by a product of variables.
  [Full treatment](02-pre-algebra/02-variables-and-expressions/README.md)
- **terminating decimal** — A decimal expansion that ends after finitely many digits; these are exactly
  the rationals whose lowest-terms denominator has the form $2^a5^b$.
  [Full treatment](01-arithmetic/04-decimals/README.md) Not to be confused with a repeating decimal, which
  continues periodically for ever.
- **theorem** — A statement proved from axioms and previously established results.
- **topology** — A family $\tau$ of subsets of $X$ containing $\varnothing$ and $X$ and closed under
  arbitrary unions and finite intersections; its members are the open sets.
- **total order** — A partial order in which any two elements are comparable. Not to be confused with a
  partial order, where some pairs may be incomparable.
- **trace** — The sum of the diagonal entries of a square matrix, equal to the sum of its eigenvalues
  counted with algebraic multiplicity.
- **transcendental number** — A number that is the root of no nonzero polynomial with rational
  coefficients, such as $e$ or $\pi$. Not to be confused with an irrational number, since $\sqrt2$ is
  irrational yet algebraic.
- **transpose** — The matrix $A^{\mathsf T}$ obtained by interchanging rows and columns, so that
  $(A^{\mathsf T})_{ij}=a_{ji}$.
- **tree** — A connected graph with no cycle; equivalently a connected graph on $n$ vertices with exactly
  $n-1$ edges.
- **triangle inequality** — The condition $d(x,z)\le d(x,y)+d(y,z)$ in a metric space, and the inequality
  $\lVert x+y\rVert\le\lVert x\rVert+\lVert y\rVert$ in a normed space.
- **trigonometric identity** — An equation between trigonometric expressions that holds for every angle,
  such as $\sin2\theta=2\sin\theta\cos\theta$.
- **truth table** — A table listing every truth assignment to the atomic propositions of a formula
  together with the resulting truth value, thereby determining the formula's semantics.

## U

- **unbiased estimator** — An estimator $\hat\theta$ with $\mathbb{E}[\hat\theta]=\theta$ for every
  admissible value of the parameter $\theta$.
- **uncountable set** — An infinite set that is not in bijection with $\mathbb{N}$; the real numbers are
  uncountable by Cantor's diagonal argument. [Full treatment](00-foundations/03-set-theory/README.md) Not
  to be confused with a countable set, which can be listed.
- **uniform convergence** — $f_n\to f$ uniformly when $\sup_x\lvert f_n(x)-f(x)\rvert\to0$, so one index
  works for all $x$ simultaneously. Not to be confused with pointwise convergence, which allows the index
  to depend on $x$.
- **uniformly continuous** — $f:X\to Y$ is uniformly continuous when for every $\varepsilon>0$ there is
  $\delta>0$ such that $d(x,y)<\delta$ implies $d(f(x),f(y))<\varepsilon$ for all $x,y\in X$. Not to be
  confused with continuity, where $\delta$ may depend on $x$ as well as on $\varepsilon$.
- **union** — The set $A\cup B=\{x:x\in A\ \text{or}\ x\in B\}$.
  [Full treatment](00-foundations/03-set-theory/README.md)
- **unit circle** — The circle $x^2+y^2=1$ in the plane, on which the trigonometric functions are defined
  as coordinates.
- **universal property** — A characterisation of an object by the existence and uniqueness of morphisms
  into or out of it, which determines the object up to unique isomorphism.

## V

- **variable** — A symbol standing for an unspecified or varying element of a set.
  [Full treatment](02-pre-algebra/02-variables-and-expressions/README.md) Not to be confused with an
  unknown, which is a fixed but not yet determined value.
- **variance** — The quantity
  $\operatorname{Var}(X)=\mathbb{E}[(X-\mathbb{E}X)^2]=\mathbb{E}[X^2]-(\mathbb{E}X)^2$, measured in
  squared units.
- **vector** — An element of a vector space; in $\mathbb{R}^n$ it is identified with a tuple and depicted
  geometrically as an arrow from the origin.
- **vector space** — An abelian group $V$ with scalar multiplication by a field $K$, subject to the usual
  distributivity and associativity laws.
- **vertex** — An element of the vertex set of a graph, that is, one of the objects the graph connects.

## W

- **walk** — A sequence of vertices and edges of a graph moving along the edges; a walk may repeat
  vertices and edges. Not to be confused with a path, which by one widespread convention repeats neither.
- **well-ordering principle** — Every nonempty subset of $\mathbb{N}$ has a least element; the principle
  is equivalent to mathematical induction. [Full treatment](01-arithmetic/01-natural-numbers/README.md)
- **Wronskian** — The determinant $W(y_1,\dots,y_n)$ of the matrix of successive derivatives of $n$
  functions; for solutions of a linear differential equation it vanishes identically or nowhere.

## Y

- **Yoneda lemma** — For a functor $F:\mathcal{C}\to\mathbf{Set}$ and an object $A$, the natural
  transformations from the hom functor $\mathcal{C}(A,-)$ to $F$ correspond bijectively to the elements of
  $F(A)$.

## Z

- **Zermelo–Fraenkel axioms** — The standard axioms of set theory, which with the axiom of choice form ZFC
  and avoid the known paradoxes while permitting the construction of the objects of ordinary mathematics.
- **zero divisor** — A nonzero element $a$ of a ring for which some nonzero $b$ satisfies $ab=0$; an
  integral domain is a commutative ring with identity and no zero divisors.
- **Zorn's lemma** — A partially ordered set in which every chain has an upper bound possesses a maximal
  element; it is equivalent to the axiom of choice.
