# Stochastic Processes — Exercises

> [Stochastic Processes](README.md) · 40 problems · Beginner → Challenge · Solutions: [solutions.md](solutions.md)

Work through the problems in order. Every problem is solvable with the definitions and theorems of the
tutorial, and the section reference tells you where to look. Do not consult [solutions.md](solutions.md)
until you have written an attempt.

**Conventions.** $P$ is a transition matrix and $P^{n}=(p^{(n)}_{ij})$ its $n$-th power; $\pi$ is a stationary
distribution; $T_A=\inf\{n\ge0:X_n\in A\}$. For Poisson processes, $\lambda$ is the rate and $T_n$ the
$n$-th interarrival time. $B$ is a standard Brownian motion. Numerical answers should be given to four
significant figures.

## Beginner

**1.** *(§7.3–7.4)* A two-state chain has $p_{12}=0.25$ and $p_{21}=0.5$.

(a) Write $P$ and check that its rows sum to $1$.
(b) Compute $P^{2}$ and hence $\Pr(X_2=2\mid X_0=1)$.
(c) Recompute $p^{(2)}_{12}$ from the Chapman–Kolmogorov sum and compare.

**2.** *(§7.4)* Let
$$P=\begin{pmatrix}0.1&0.6&0.3\\ 0.2&0.5&0.3\\ 0.4&0.4&0.2\end{pmatrix}.$$

(a) Compute $p^{(2)}_{13}$ as a sum over the intermediate state.
(b) Compute the whole matrix $P^{2}$ and verify your answer to (a).
(c) If $X_0=1$, give the law of $X_2$.

**3.** *(§7.5)* For
$$P=\begin{pmatrix}0&1&0\\ \tfrac12&0&\tfrac12\\ 0&1&0\end{pmatrix}$$
compute $p^{(n)}_{11}$ for $n=1,2,3,4$. What is the period of state $1$? Does $\lim_np^{(n)}_{11}$ exist?

**4.** *(§7.5)* A chain on $\{1,2,3,4,5\}$ has transitions $1\to2$, $2\to1$ or $3$ (each with probability
$\tfrac12$), $3\to4$, $4\to3$ or $5$ (each with probability $\tfrac12$), and $5\to5$.

(a) Find all communicating classes.
(b) Which classes are closed?
(c) Which states are recurrent, and which are transient?
(d) Give the period of each state that has one.

**5.** *(§7.6)* Find the stationary distribution of
$$P=\begin{pmatrix}0.2&0.3&0.5\\ 0.6&0.1&0.3\\ 0.3&0.3&0.4\end{pmatrix}$$
and verify it by computing $\pi P$ entry by entry.

**6.** *(§7.6)* Let $P=\begin{pmatrix}1-a&a\\ b&1-b\end{pmatrix}$ with $0<a,b<1$.

(a) Prove that the stationary distribution is $\pi=\bigl(\frac{b}{a+b},\frac{a}{a+b}\bigr)$.
(b) Prove that $P^{n}=\Pi+(1-a-b)^{n}(I-\Pi)$, where $\Pi$ has both rows equal to $\pi$.
(c) Deduce $\lim_nP^{n}$ and say for which $a,b$ the limit is reached in one step.

**7.** *(§7.6)* Let $G$ be the graph obtained from a triangle on $\{1,2,3\}$ by attaching a pendant vertex
$4$ to vertex $1$. A token performs the simple random walk on $G$: from a vertex it moves to a uniformly
chosen neighbour.

(a) Give the degree of each vertex and the total degree.
(b) Find the stationary distribution.
(c) Compute the expected return time to vertex $4$, and to vertex $1$.
(d) Is the walk aperiodic? Justify.

**8.** *(§7.8)* A chain on $\{1,2,3,4,5\}$ has
$$P=\begin{pmatrix}0.5&0.5&0&0&0\\ 0&0.25&0.5&0.25&0\\ 0&0&0.5&0&0.5\\ 0&0&0&1&0\\ 0&0&0&0&1\end{pmatrix}.$$
States $4$ and $5$ are absorbing. Let $h_i=\Pr_i(X_T=5)$ and $k_i=\mathbb{E}_i[T]$ with
$T=\inf\{n:X_n\in\{4,5\}\}$.

(a) Write down the equations for $h_i$ and solve them.
(b) Write down the equations for $k_i$ and solve them.
(c) Check that absorption is certain.

**9.** *(§7.9)* Arrivals form a Poisson process of rate $\lambda=2$ per day. Compute

(a) $\Pr(N(3)=4)$; (b) $\Pr(N(1)=0)$; (c) $\mathbb{E}[N(3)]$ and $\operatorname{Var}(N(3))$;
(d) $\Pr\bigl(N(2)=0\mid N(1)=0\bigr)$.

**10.** *(§7.9)* A Poisson process has rate $\lambda=0.5$ per minute. Let $A_n=T_1+\cdots+T_n$.

(a) Compute $\Pr(T_1>4)$.
(b) Compute $\mathbb{E}[A_3]$.
(c) Compute $\Pr(A_3\le6)$ two ways: from the gamma distribution of $A_3$, and from the Poisson count.
(d) Compute $\Pr(T_3>6)$.

**11.** *(§7.9)* Two independent Poisson streams have rates $3$ and $5$ per hour.

(a) What is the rate of the merged stream?
(b) What is the probability that the next arrival comes from the first stream?
(c) Given that exactly $4$ arrivals occur in an hour, what is the distribution of the number from the first
stream?
(d) If each arrival of the first stream is kept independently with probability $0.2$, what is the rate of the
kept stream?

**12.** *(§7.12)* Let $S_n$ be a random walk with i.i.d. increments.

(a) Show that $M_n=S_n^{2}-n$ is a martingale when $\mathbb{E}X_i=0$ and $\operatorname{Var}(X_i)=1$.
(b) Show that $M_n=(q/p)^{S_n}$ is a martingale when $X_i=+1$ with probability $p$ and $-1$ with
probability $q=1-p$, $p\ne q$.
(c) Show that $M_n=S_n-n\mu$ is a martingale when $\mathbb{E}X_i=\mu$.

**13.** *(§7.10)* A two-state CTMC has generator $Q=\begin{pmatrix}-2&2\\ 3&-3\end{pmatrix}$.

(a) Find the stationary distribution by solving $\pi Q=0$.
(b) Give the distribution of the holding time in each state.
(c) Describe the jump chain.
(d) Solve for $p_{11}(t)$ and check its limit as $t\to\infty$.

## Intermediate

**14.** *(§7.7)* Let $P=\begin{pmatrix}0.9&0.1\\ 0.3&0.7\end{pmatrix}$.

(a) Find $\pi$ and the second eigenvalue.
(b) Write $P^{n}$ explicitly.
(c) Compute $\lVert p^{(n)}_{i\cdot}-\pi\rVert_{TV}$ for each $i$ and find the smallest $n$ for which both
distances are below $0.01$.
(d) Compare the distance at $n=5$ with the bound $\frac23(0.4)^{n}$ of Example 9.1 and explain the
difference.

**15.** *(§7.6–7.7)* Let $G$ be a finite connected undirected graph and let $X$ be the simple random walk on
it.

(a) Prove that $\pi_v=\deg(v)/(2\lvert E\rvert)$ is stationary.
(b) Show that the walk has period $2$ if and only if $G$ is bipartite, and is aperiodic otherwise.
(c) For the complete graph $K_4$, compute $\pi$ and the expected return time to each vertex.

**16.** *(§7.8)* For the chain of Exercise 8, compute $N=(I-Q)^{-1}$ with $Q$ the transient block.

(a) Verify that $k=N\mathbf{1}$ reproduces your answer to Exercise 8(b).
(b) Interpret $N_{12}$ and $N_{23}$ as expected visit counts.
(c) Use $N$ to compute the probability of being absorbed at $5$, starting from $1$.

**17.** *(§7.11)* A gambler starts with $\$4$, stakes $\$1$ per round with winning probability $p=0.45$, and
stops at $\$0$ or $\$10$.

(a) Compute the probability of reaching $\$10$.
(b) Compute the expected number of rounds.
(c) Compare with the fair-game values and comment on both directions of the comparison.

**18.** *(§7.9)* Let $N$ be a Poisson process of rate $\lambda$ and $A_1$ its first arrival.

(a) Prove directly from the definition that $\Pr(A_1>t)=e^{-\lambda t}$.
(b) Prove that, conditionally on $N(t)=1$, $A_1$ is uniform on $[0,t]$.
(c) Compute $\mathbb{E}[A_1\mid N(1)=1]$ and $\Pr\bigl(A_1\le\tfrac12\mid N(1)=1\bigr)$.

**19.** *(§7.9)* Buses of route $A$ arrive as a Poisson process of rate $6$ per hour, and of route $B$ at
rate $4$ per hour, independently.

(a) What is the probability that the first bus to arrive is an $A$?
(b) What is the expected waiting time for any bus?
(c) What is the probability that no bus arrives in the next $10$ minutes?
(d) Given that exactly two buses arrive in an hour, what is the probability that both are $A$?

**20.** *(§7.10)* A two-state CTMC jumps $1\to2$ at rate $\lambda$ and $2\to1$ at rate $\mu$.

(a) Write $Q$ and the backward equations for $p_{11}$ and $p_{21}$.
(b) Solve them, with $p_{11}(0)=1$.
(c) Find the stationary distribution and verify it is the limit of $p_{11}(t)$.
(d) Compute the expected holding time in state $1$.

**21.** *(§7.11)* For the simple symmetric random walk on $\mathbb{Z}^{2}$:

(a) Compute $u_2=\Pr(S_2=0)$ and $u_4=\Pr(S_4=0)$ by counting.
(b) Verify that $u_{2n}=\binom{2n}{n}^{2}4^{-2n}$ in these two cases.
(c) Use Stirling's formula to show $u_{2n}\sim 1/(\pi n)$ and conclude recurrence.

**22.** *(§7.12)* Let $S_n$ be the symmetric random walk and $T=\inf\{n:S_n\in\{-a,b\}\}$ with $a,b>0$ and
$S_0=0$.

(a) Use the martingale $S_n$ to compute $\Pr(S_T=b)$.
(b) Use $S_n^{2}-n$ to compute $\mathbb{E}[T]$.
(c) Reconcile both answers with Theorems 7.28 and 7.29.

**23.** *(§7.7)* For the chain of Example 9.2, compute $\lVert p^{(n)}_{1\cdot}-\pi\rVert_{TV}$ for even $n$
and for odd $n$, and show that it does not tend to $0$. Compute the Cesàro average
$\frac1n\sum_{k<n}p^{(k)}_{1\cdot}$ in the limit $n\to\infty$ and compare with $\pi$.

**24.** *(§7.6)* For the chain of Exercise 1, compute $\mathbb{E}_1[T^{+}_1]$ directly and verify Kac's
formula $\mathbb{E}_1[T^{+}_1]=1/\pi_1$.

## Advanced

**25.** *(§7.5–7.6)* Let $P$ be a stochastic matrix on a finite set $S$.

(a) Prove that $S$ decomposes into communicating classes and that at least one of them is closed.
(b) Prove that the states of a closed class are recurrent, and that states which can leave their class are
transient.
(c) Deduce that the set of stationary distributions is the set of convex combinations of the stationary
distributions of the closed classes, and that it is a singleton exactly when there is one closed class.

**26.** *(§7.5)* Let $P$ be irreducible with period $d\ge2$.

(a) Prove that $d(i)=d(j)$ for all $i,j$ and that if $p^{(n)}_{ij}>0$ and $p^{(m)}_{ij}>0$ then
$n\equiv m\pmod d$.
(b) Deduce that $S$ splits into $d$ cyclic classes $C_0,\dots,C_{d-1}$ with $p_{ij}>0$ only if $i\in C_r$ and
$j\in C_{r+1}$ (indices mod $d$).
(c) Deduce $p^{(n)}_{ii}=0$ unless $d\mid n$.

**27.** *(§7.6–7.7)* Let $P$ be irreducible on finite $S$ with stationary law $\pi$ and Cesàro limit
$\Pi=\lim_n\frac1n\sum_{k<n}P^{k}$.

(a) Prove $\Pi P=P\Pi=\Pi$ and $\Pi^{2}=\Pi$, and that every row of $\Pi$ is $\pi$.
(b) Prove that $P^{n}\to\Pi$ if and only if $P$ is aperiodic.
(c) Give a finite irreducible periodic chain for which $P^{2n}$ and $P^{2n+1}$ converge to different
matrices, and compute both limits.

**28.** *(§7.7)* Let $P$ be reversible with respect to $\pi$ and irreducible on finite $S$.

(a) Prove that $P$ is self-adjoint on $\ell^{2}(\pi)$, hence diagonalisable with real eigenvalues
$1=\lambda_1\ge\lvert\lambda_2\rvert\ge\cdots\ge\lvert\lambda_m\rvert$ (with $\lvert\lambda_2\rvert<1$ when
$P$ is aperiodic).
(b) Prove the chi-squared bound
$\sum_j\bigl(p^{(n)}_{ij}-\pi_j\bigr)^{2}/\pi_j\le\lambda_*^{2n}/\pi_i$ with
$\lambda_*=\max_{k\ge2}\lvert\lambda_k\rvert$.
(c) Deduce $\lVert p^{(n)}_{i\cdot}-\pi\rVert_{TV}\le\frac12\lambda_*^{n}/\sqrt{\pi_i}$.

**29.** *(§7.7)* For the chain of Exercise 1, carry out Lemma 7.13 explicitly.

(a) Find the smallest $N$ with $p^{(N)}_{ij}>0$ for all $i,j$.
(b) Compute $\delta=\min_{a,c}p^{(N)}_{ac}$ and the consequent bound
$\Pr(T>mN)\le(1-\delta)^{m}$ for the coupling.
(c) Compare the resulting mixing-time bound with the exact value, computed as in Exercise 14, for this chain.

**30.** *(§7.8)* Let $P$ be irreducible on finite $S$ and fix $j\in S$. Let
$k^{(j)}_i=\mathbb{E}_i[T_j]$ with $T_j=\inf\{n\ge0:X_n=j\}$.

(a) Show that $k^{(j)}_j=0$ and $k^{(j)}_i=1+\sum_{l\ne j}p_{il}k^{(j)}_l$ for $i\ne j$.
(b) Show that this system has a unique solution.
(c) Solve it for the two-state chain of Exercise 1, for both choices of $j$.
(d) Explain why $k^{(j)}_i$ need not equal $1/\pi_j$.

**31.** *(§7.9)* Prove both closure properties of Poisson processes.

(a) Show that the superposition of two independent Poisson processes of rates $\lambda_1,\lambda_2$ is Poisson
of rate $\lambda_1+\lambda_2$, including independence of increments.
(b) Show that thinning a rate-$\lambda$ process with retention probability $p$ gives a Poisson process of
rate $p\lambda$, and that the kept and discarded streams are independent.

**32.** *(§7.11)* Let $S_n$ be the simple symmetric random walk on $\mathbb{Z}$.

(a) Prove $u_{2n}=\binom{2n}{n}4^{-n}$ and $u_{2n}\sim(\pi n)^{-1/2}$.
(b) Prove $\sum_nu_n=\infty$, hence recurrence.
(c) Prove $\mathbb{E}_0[T^{+}_0]=\infty$, i.e. the walk is null recurrent.

**33.** *(§7.11)* Let $S_n$ be the simple symmetric random walk on $\mathbb{Z}^{3}$.

(a) State the local limit theorem you use, with its hypotheses.
(b) Prove $u_{2n}\le Cn^{-3/2}$ for large $n$, hence $\sum_nu_n<\infty$.
(c) Conclude transience and explain in one sentence why dimension three is the threshold.

**34.** *(§7.12)* Prove the optional stopping theorem and examine its hypotheses.

(a) Prove $\mathbb{E}[M_T]=\mathbb{E}[M_0]$ for a martingale $M$ and a bounded stopping time $T\le K$.
(b) Deduce the dominated version and the corollary for bounded increments with $\mathbb{E}T<\infty$.
(c) For the symmetric walk and $T=\inf\{n:S_n=1\}$, identify exactly which hypothesis fails and compute
$\mathbb{E}[S_T]$.

## Challenge

**35.** *(§7.6, §12)* PageRank. Let $P$ be the transition matrix of the random walk on a finite directed graph
(with rows corresponding to vertices of out-degree $0$ replaced by the uniform distribution), and let
$$G=dP+(1-d)\tfrac1n\mathbf{1}\mathbf{1}^{\mathsf T},\qquad 0<d<1 .$$

(a) Prove that $G$ is stochastic, irreducible and aperiodic.
(b) Prove that the PageRank vector $\pi$ (the stationary law of $G$) is unique.
(c) Compute $\pi$ for the graph $1\to2$, $2\to1$, $3\to1$ with $n=3$ and $d=0.85$.
(d) Prove that every vertex has $\pi_j\ge(1-d)/n$, so no page can have PageRank zero.

**36.** *(§7.13)* Brownian motion.

(a) Prove that the dyadic squared increments over $[0,t]$ converge to $t$ in $L^{2}$.
(b) Deduce that $B$ is almost surely not $C^{1}$ on any interval.
(c) For $T=\inf\{t:B_t\in\{-a,b\}\}$ with $B_0=0$, prove $\Pr(B_T=b)=a/(a+b)$ and $\mathbb{E}[T]=ab$.
(d) Explain why $\mathbb{E}[T_a]=\infty$ for the one-sided hitting time $T_a=\inf\{t:B_t=a\}$, and reconcile
this with (c).

**37.** *(§12, §7.12)* Galton–Watson branching. Let $Z_0=1$ and $Z_{n+1}=\sum_{k=1}^{Z_n}\xi_{n,k}$ with
$\xi_{n,k}$ i.i.d. on $\mathbb{N}_0$, mean $\mu\in(0,\infty)$, and let $G(s)=\mathbb{E}[s^{\xi}]$ and
$q=\Pr(Z_n=0\text{ for some }n)$.

(a) Prove $q=\lim_nq_n$ where $q_{n+1}=G(q_n)$, $q_0=0$.
(b) Prove that $q$ is the smallest fixed point of $G$ in $[0,1]$.
(c) Prove that $q=1$ if $\mu\le1$ and $q<1$ if $\mu>1$.
(d) Show that $Z_n/\mu^{n}$ is a martingale, and explain what it computes when $\mu>1$.

**38.** *(§7.10, §12)* The M/M/1 queue with arrival rate $\lambda$ and service rate $\mu$.

(a) Write the generator and verify that it acts as $Qf(n)=\lambda(f(n+1)-f(n))+\mu(f(n-1)-f(n))$ for $n\ge1$
and $Qf(0)=\lambda(f(1)-f(0))$.
(b) Prove that $\pi_n=(1-\rho)\rho^{n}$ with $\rho=\lambda/\mu$ satisfies $\pi Q=0$ when $\rho<1$.
(c) Prove that no stationary distribution exists when $\lambda\ge\mu$.
(d) Compute the mean number in the system, the mean time in the system, and verify Little's law.

**39.** *(§7.13)* Reflection.

(a) Prove $\Pr(T_a\le t)=2\Pr(B_t\ge a)$ for $a>0$.
(b) Prove the joint form $\Pr(T_a\le t,\,B_t\le x)=\Pr(B_t\ge 2a-x)$ for $x\le a$.
(c) Compute $\Pr(T_1\le1,\,B_1\le0)$ and compare with the naive answer $\Pr(T_1\le1)\Pr(B_1\le0)$.
(d) Compute $\mathbb{E}[B_1\mid T_1\le1]$.

**40.** *(§7.9)* Order statistics and the inspection paradox. Let $N$ be a Poisson process of rate $\lambda$.

(a) Prove that, conditionally on $N(t)=n$, the arrival epochs are the order statistics of $n$ independent
uniform variables on $[0,t]$.
(b) Deduce $\mathbb{E}[A_n\mid N(t)=n]=nt/(n+1)$.
(c) A time $U$ is chosen uniformly in $[0,T]$ independently of $N$. Prove that the mean length of the
interarrival gap containing $U$ tends to $2/\lambda$ as $T\to\infty$, and explain why this is larger than
$1/\lambda$.
