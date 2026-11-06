# Stochastic Processes — Solutions

> [Stochastic Processes](README.md) · Solutions to [exercises.md](exercises.md) · 40 problems

Each solution gives the strategy first, then every significant step, then a check. Notation is that of the
tutorial; "§" refers to its sections.

## Beginner

**1.** *(a)* Since each row must sum to $1$, $p_{11}=0.75$ and $p_{22}=0.5$, so
$P=\begin{pmatrix}0.75&0.25\\0.5&0.5\end{pmatrix}$.

*(b)* Matrix multiplication, entry by entry:
$p^{(2)}_{11}=0.75\cdot0.75+0.25\cdot0.5=0.5625+0.125=0.6875$,
$p^{(2)}_{12}=0.75\cdot0.25+0.25\cdot0.5=0.1875+0.125=0.3125$,
$p^{(2)}_{21}=0.5\cdot0.75+0.5\cdot0.5=0.625$,
$p^{(2)}_{22}=0.5\cdot0.25+0.5\cdot0.5=0.375$.
Hence $\Pr(X_2=2\mid X_0=1)=0.3125$.

*(c)* Chapman–Kolmogorov with the intermediate state:
$p^{(2)}_{12}=p_{11}p_{12}+p_{12}p_{22} =0.75(0.25)+0.25(0.5)=0.1875+0.125=0.3125$, agreeing.
Check: each row of $P^{2}$ sums to $1$ ($0.6875+0.3125=1$, $0.625+0.375=1$).

**2.** *(a)* $p^{(2)}_{13}=\sum_kp_{1k}p_{k3}=0.1(0.3)+0.6(0.3)+0.3(0.2)=0.03+0.18+0.06=0.27$.

*(b)* Rowwise, $p^{(2)}_{ij}=\sum_kp_{ik}p_{kj}$: $(0.25,0.48,0.27)$, $(0.24,0.49,0.27)$,
$(0.20,0.52,0.28)$; e.g. $p^{(2)}_{11}=0.1(0.1)+0.6(0.2)+0.3(0.4) =0.01+0.12+0.12=0.25$. The third
entry of the first row is $0.27$, as in (a).

*(c)* If $X_0=1$ then $X_2$ has law $(0.25,0.48,0.27)$. Check: each row of $P^{2}$ sums to $1$
($0.25+0.48+0.27=1$, $0.24+0.49+0.27=1$, $0.20+0.52+0.28=1$).

**3.** Since $p_{11}=0$,
$p^{(2)}_{11}=\sum_kp_{1k}p_{k1}=0\cdot0+1\cdot\tfrac12+0\cdot0=\tfrac12$. Then $p^{(3)}_{11}=\sum_kp^{(2)}_{1k}p_{k1}=0.5(0)+0(0.5)+0.5(0)=0$, and
$p^{(4)}_{11}=\sum_kp^{(2)}_{1k}p^{(2)}_{k1}=0.5(0.5)+0+0.5(0.5)=0.5$. So the values are
$0,\,0.5,\,0,\,0.5$. Every return takes an even number of steps and returns at $2$ steps occur, so the
period is $2$ (gcd of $\{2,4,6,\dots\}$). The limit does not exist: the sequence alternates between $0$ and
$0.5$. (Its Cesàro mean is $0.25=\pi_1$, consistent with Corollary 7.10.)

**4.** *(a)* From $1$ one reaches $2$, from $2$ one reaches $1$ or $3$, from $3$ one reaches $4$, from $4$
one reaches $3$ or $5$, and $5$ is absorbing. The classes are $\{1,2\}$, $\{3,4\}$ and $\{5\}$.

*(b)* Only $\{5\}$ is closed: from $\{1,2\}$ the chain can move to $3$, and from $\{3,4\}$ it can move to $5$.

*(c)* State $5$ is recurrent (it returns to itself with probability $1$ at every step). The class $\{5\}$ is
finite and closed, hence recurrent. Since $1\to3$ and $3$ cannot return to $1$, the states $1,2,3,4$ are
transient (positive probability of never returning).

*(d)* On $\{1,2\}$ every return takes an even number of steps and $p^{(2)}_{11}=0.25>0$, so $d=2$. On
$\{3,4\}$ the same argument gives $d=2$. On $\{5\}$ we have $p_{55}=1>0$, so $d=1$.

**5.** Write $\pi P=\pi$ in components:
$$\pi_1=0.2\pi_1+0.6\pi_2+0.3\pi_3,\quad
\pi_2=0.3\pi_1+0.1\pi_2+0.3\pi_3,\quad
\pi_3=0.5\pi_1+0.3\pi_2+0.4\pi_3.$$
The second and third equations give
$0.9\pi_2=0.3(\pi_1+\pi_3)$, i.e. $\pi_2=(\pi_1+\pi_3)/3$, and
$0.6\pi_3=0.5\pi_1+0.3\pi_2$. Substituting the first into the second,
$3\pi_2=\pi_1+\tfrac56\pi_1+\tfrac12\pi_2$, so $\tfrac52\pi_2=\tfrac{11}{6}\pi_1$ and
$\pi_2=\tfrac{11}{15}\pi_1$; then
$\pi_3=\tfrac56\pi_1+\tfrac12\cdot\tfrac{11}{15}\pi_1=\tfrac{36}{30}\pi_1=\tfrac65\pi_1$.
Normalising, $\pi_1\bigl(1+\tfrac{11}{15}+\tfrac65\bigr)=\tfrac{44}{15}\pi_1=1$, so
$\pi=\bigl(\tfrac{15}{44},\tfrac{11}{44},\tfrac{18}{44}\bigr)\approx(0.3409,0.25,0.4091)$.
Verification of the first equation: $\frac{0.2(15)+0.6(11)+0.3(18)}{44}=\frac{3+6.6+5.4}{44}=\frac{15}{44}$.
The chain is irreducible (all entries positive), so by Theorem 7.9 this is the only stationary law.

**6.** *(a)* From $\pi_1=(1-a)\pi_1+b\pi_2$ we get $a\pi_1=b\pi_2$, so $\pi_1:\pi_2=b:a$ and, since the
coordinates sum to $1$, $\pi=\bigl(\frac{b}{a+b},\frac{a}{a+b}\bigr)$. Both coordinates are positive because
$0<a,b<1$.

*(b)* Let $\lambda=1-a-b$ and let $\Pi$ have both rows equal to $\pi$. First,
$P-\Pi=\lambda(I-\Pi)$: the $(1,1)$ entry is
$(1-a)-\frac{b}{a+b}=\frac{(1-a)(a+b)-b}{a+b}=\frac{a(1-a-b)}{a+b}=\lambda\frac{a}{a+b} =\lambda(1-\pi_1)$,
and the $(1,2)$ entry is
$a-\frac{a}{a+b}=\frac{a(a+b-1)}{a+b}=-\lambda\frac{a}{a+b} =-\lambda\pi_2$; the second row is
analogous. Also $\Pi(I-\Pi)=0=(I-\Pi)\Pi$ and $\Pi^{2}=\Pi$, $(I-\Pi)^{2}=I-\Pi$. Expanding,
$P^{n}=\bigl(\Pi+\lambda(I-\Pi)\bigr)^{n}=\Pi+\lambda^{n}(I-\Pi)$ because every mixed term
vanishes.

*(c)* Since $\lvert\lambda\rvert=\lvert1-a-b\rvert<1$ for $a,b\in(0,1)$ (as $0<a+b<2$), $P^{n}\to\Pi$ and
$p^{(n)}_{ij}\to\pi_j$ geometrically. If $a+b=1$ then $\lambda=0$ and $P=\Pi$, so the limit is reached at
$n=1$: the rows of $P$ are then $(b,a)$ and $(b,a)$.

**7.** *(a)* $\deg(1)=3$ (neighbours $2,3,4$), $\deg(2)=2$, $\deg(3)=2$, $\deg(4)=1$; total degree $8$, that
is $\lvert E\rvert=4$.

*(b)* By the graph formula $\pi_v=\deg(v)/(2\lvert E\rvert)$,
$\pi=(\tfrac38,\tfrac28,\tfrac28,\tfrac18)$.

*(c)* Kac's formula: $\mathbb{E}_4[T^{+}_4]=1/\pi_4=8$ and $\mathbb{E}_1[T^{+}_1]=1/\pi_1=8/3\approx2.667$.
Independent check for vertex $4$: let $u_v=\mathbb{E}_v[T_4]$, so $u_4=0$ and, by the symmetry between
$2$ and $3$, $u_2=u_3$. From the first-step equations, $u_2=1+\tfrac12u_1+\tfrac12u_2$ gives $u_2=2+u_1$, and
$u_1=1+\tfrac13u_2+\tfrac13u_3+\tfrac13u_4=1+\tfrac23u_2=1+\tfrac23(2+u_1)$ gives $u_1=7$; hence
$\mathbb{E}_4[T^{+}_4]=1+u_1=8$, as Kac predicts.

*(d)* Aperiodic. The triangle is a closed walk of length $3$, so $p^{(3)}_{11}>0$, while $p^{(2)}_{11}>0$ as
well; hence the gcd of return times is $1$. Equivalently, the graph is not bipartite.

**8.** *(a)* $h_4=0$, $h_5=1$. First-step analysis for the remaining states:
$h_3=0.5h_3+0.5h_5$, so $h_3=1$;
$h_2=0.25h_2+0.5h_3+0.25h_4=0.25h_2+0.5$, so $h_2=\tfrac23$;
$h_1=0.5h_1+0.5h_2$, so $h_1=\tfrac23$.

*(b)* $k_4=k_5=0$, and
$k_3=1+0.5k_3+0.5k_4\Rightarrow k_3=2$;
$k_2=1+0.25k_2+0.5k_3\Rightarrow0.75k_2=2\Rightarrow k_2=\tfrac83$;
$k_1=1+0.5k_1+0.5k_2\Rightarrow0.5k_1=\tfrac73\Rightarrow k_1=\tfrac{14}{3}\approx4.667$.

*(c)* Absorption is certain: from every state there is a path of positive probability into $\{4,5\}$ and the
state space is finite (Theorem 7.17(1)). As a check, $h_1=\tfrac23$ is the probability of absorption at $5$,
so $1-\tfrac23=\tfrac13$ is the probability of absorption at $4$, and the two add to $1$.

**9.** *(a)* $N(3)\sim\operatorname{Pois}(6)$, so
$\Pr(N(3)=4)=e^{-6}6^{4}/4!=1296e^{-6}/24=54e^{-6}=0.1339$.

*(b)* $\Pr(N(1)=0)=e^{-2}=0.1353$.

*(c)* Mean and variance of a Poisson variable are both $\lambda t=6$.

*(d)* By independent increments, $N(2)-N(1)$ is independent of $N(1)$, so
$\Pr(N(2)=0\mid N(1)=0)=\Pr(N(2)-N(1)=0)=e^{-2}=0.1353$.

**10.** *(a)* $\Pr(T_1>4)=\Pr(N(4)=0)=e^{-2}=0.1353$.

*(b)* $\mathbb{E}[A_3]=3/\lambda=6$ minutes.

*(c)* $A_3\sim\text{Gamma}(3,0.5)$ with density $\tfrac{\lambda^3x^{2}e^{-\lambda x}}{2}$, so
$$\Pr(A_3\le6)=\int_0^6\frac{0.125x^{2}e^{-0.5x}}{2}dx=1-e^{-3}\Bigl(1+3+\frac{9}{2}\Bigr)=1-8.5e^{-3}=0.5768.$$
The count version: $\{A_3\le6\}=\{N(6)\ge3\}$ and $N(6)\sim\operatorname{Pois}(3)$, so
$\Pr(N(6)\ge3)=1-e^{-3}(1+3+4.5)$, the same number.

*(d)* $\{T_3>6\}$ means at most two arrivals by time $6$:
$\Pr(T_3>6)=\Pr(N(6)\le2)=e^{-3}(1+3+4.5)=0.4232$, which is $1-0.5768$.

**11.** *(a)* Superposition: $3+5=8$ per hour.

*(b)* A randomly chosen arrival of the merged stream is from the first with probability proportional to its
rate, $3/8=0.375$. (Formally, the merged process thins into the two streams with retention probabilities
$3/8$ and $5/8$.)

*(c)* By thinning, the number from the first stream given $4$ arrivals is $\operatorname{Bin}(4,3/8)$.

*(d)* Thinning multiplies the rate: $0.2\cdot3=0.6$ per hour.

**12.** *(a)* By independence of the increment $X_{n+1}$ from $\mathcal{F}_n$,
$\mathbb{E}[S_{n+1}^{2}\mid\mathcal{F}_n]=S_n^{2}+2S_n\mathbb{E}[X]+0+\mathbb{E}[X^{2}]=S_n^{2}+1$. Hence
$\mathbb{E}[M_{n+1}\mid\mathcal{F}_n]=S_n^{2}+1-(n+1)=S_n^{2}-n=M_n$.

*(b)*
$\mathbb{E}\bigl[(q/p)^{S_{n+1}}\mid\mathcal{F}_n\bigr]=(q/p)^{S_n}\bigl[p(q/p)+q(p/q)\bigr] =(q/p)^{S_n}(q+p)=(q/p)^{S_n}$,
since $p(q/p)=q$ and $q(p/q)=p$.

*(c)* $\mathbb{E}[S_{n+1}\mid\mathcal{F}_n]=S_n+\mu$, so
$\mathbb{E}[M_{n+1}\mid\mathcal{F}_n] =S_n+\mu-(n+1)\mu=S_n-n\mu=M_n$. In all three cases
integrability is automatic for finite $n$; for an infinite horizon one needs
$\mathbb{E}\lvert X\rvert<\infty$.

**13.** *(a)* From $\pi Q=0$: $-2\pi_1+3\pi_2=0$ and $2\pi_1-3\pi_2=0$, which are the same equation, so
$\pi_1=3\pi_2/2$ and $\pi=(\tfrac35,\tfrac25)$.

*(b)* The holding time in state $1$ is exponential with rate $-q_{11}=2$, and in state $2$ exponential with
rate $3$ (Proposition 7.24).

*(c)* The jump chain is deterministic (each state has one possible target): $1\to2\to1\to\cdots$, with
$p_{12}=2/2=1$ and $p_{21}=3/3=1$.

*(d)* The equations are $p_{11}'=-2p_{11}+2p_{21}$ and $p_{21}'=3p_{11}-3p_{21}$ with
$p_{11}(0)=1$, $p_{21}(0)=0$. Eliminating $p_{21}$ gives $p_{11}''+5p_{11}'=0$, hence
$p_{11}=A+Be^{-5t}$; the conditions $p_{11}(0)=1$ and $p_{11}'(0)=-2$ give $B=\tfrac25$, $A=\tfrac35$:
$$p_{11}(t)=\tfrac35+\tfrac25e^{-5t}\longrightarrow\tfrac35=\pi_1.$$

## Intermediate

**14.** *(a)* The second eigenvalue of a two-state chain is $1-a-b=1-0.1-0.3=0.6$, and
$\pi=\bigl(\tfrac{b}{a+b},\tfrac{a}{a+b}\bigr)=(0.75,0.25)$ by Exercise 6.

*(b)* $P^{n}=\Pi+0.6^{n}(I-\Pi)$, so
$p^{(n)}_{11}=0.75+0.25(0.6)^{n}$ and $p^{(n)}_{21}=0.75-0.75(0.6)^{n}$. Check $n=1$:
$0.75+0.15=0.90$ and $0.75-0.45=0.30$.

*(c)* The two rows of $I-\Pi$ are $(0.25,-0.25)$ and $(-0.75,0.75)$, so
$\lVert p^{(n)}_{1\cdot}-\pi\rVert_{TV}=0.25(0.6)^{n}$ and
$\lVert p^{(n)}_{2\cdot}-\pi\rVert_{TV} =0.75(0.6)^{n}$. The maximum is below $0.01$ when
$0.6^{n}<0.01333$, i.e. $n>\ln(0.01333)/\ln(0.6)=8.45$; so $n=9$ (the value is $0.00756$; at $n=8$
it is $0.01260$).

*(d)* At $n=5$ the distance is $0.75(0.6)^{5}=0.05832$, which is larger than Example 9.1's bound
$\tfrac23(0.4)^{5}=0.00683$. That is not a contradiction: the bound belongs to a *different* chain, whose
second eigenvalue is $0.4$. A bound transfers only through the hypotheses it uses.

**15.** *(a)* Check detailed balance:
$\pi_up_{uv}=\frac{\deg u}{2\lvert E\rvert}\cdot\frac{1}{\deg u} =\frac{1}{2\lvert E\rvert}=\pi_vp_{vu}$.
By Proposition 7.11, $\pi$ is stationary. (It is the unique one because the walk is irreducible.)

*(b)* If $G$ is bipartite with parts $V_0,V_1$, every step changes part, so every closed walk has even length
and all return times are even; since $2$-step returns exist, the period is $2$. If $G$ is not bipartite it
contains an odd cycle, hence a closed walk of odd length through its vertices, so some odd $n$ has
$p^{(n)}_{vv}>0$; even return times also occur, so the period is $1$.

*(c)* $K_4$ has $4$ vertices of degree $3$ and $\lvert E\rvert=6$, so $\pi_v=3/12=\tfrac14$ for every $v$
and $\mathbb{E}_v[T^{+}_v]=4$.

**16.** Inverting $I-Q$ for $Q=\begin{pmatrix}0.5&0.5&0\\0&0.25&0.5\\0&0&0.5\end{pmatrix}$:
$$N=(I-Q)^{-1}=\begin{pmatrix}2&\tfrac43&\tfrac43\\ 0&\tfrac43&\tfrac43\\ 0&0&2\end{pmatrix}.$$

*(a)* $N\mathbf 1=\bigl(2+\tfrac43+\tfrac43,\ \tfrac83,\ 2\bigr)=\bigl(\tfrac{14}{3},\tfrac83,2\bigr)$,
exactly the expected times of Exercise 8(b).

*(b)* $N_{12}=\tfrac43$ is the expected number of visits to state $2$ before absorption, starting from
state $1$; $N_{23}=\tfrac43$ is the expected number of visits to $3$ starting from $2$. (Visits to the
starting state are counted at time $0$.)

*(c)* Let $r$ be the vector of one-step probabilities into state $5$: $r=(0,0,\tfrac12)$ on states
$(1,2,3)$. Then
$h=Nr=\bigl(\tfrac43\cdot\tfrac12,\ \tfrac43\cdot\tfrac12,\ 2\cdot\tfrac12\bigr) =\bigl(\tfrac23,\tfrac23,1\bigr)$,
matching Exercise 8(a).

**17.** *(a)* Here $p=0.45$, $q=0.55$, $\rho=q/p=\tfrac{11}{9}\approx1.2222$, $N=10$, $i=4$. Theorem 7.28:
$$h_4=\frac{1-\rho^{4}}{1-\rho^{10}}=\frac{1-2.2315}{1-7.4386}=\frac{-1.2315}{-6.4386}=0.1913 .$$
(The numerator and denominator are both negative because $\rho>1$; the ratio is positive.)

*(b)* Theorem 7.29:
$k_4=\frac{4}{q-p}-\frac{10}{q-p}(0.1913)=40-100(0.1913)=20.87$ rounds.

*(c)* In the fair game $h_4=0.4$ and $k_4=4\cdot6=24$. Both are larger than the biased values: the bias
reduces the chance of success and also shortens the game, because ruin tends to happen quickly. Note the two
effects go in opposite directions relative to a naive intuition ("a shorter game should favour the
underdog") — the success probability falls even though the game is shorter.

**18.** *(a)* $\{A_1>t\}=\{N(t)=0\}$ because paths are non-decreasing and jump by $1$, and
$\Pr(N(t)=0)=e^{-\lambda t}(\lambda t)^{0}/0!=e^{-\lambda t}$.

*(b)* For $0\le a\le t$,
$$\Pr(A_1\le a\mid N(t)=1)=\frac{\Pr(N(a)=1,\,N(t)-N(a)=0)}{\Pr(N(t)=1)}
=\frac{\lambda a\,e^{-\lambda a}\cdot e^{-\lambda(t-a)}}{\lambda t\,e^{-\lambda t}}=\frac{a}{t},$$
using independent increments; this is the uniform CDF on $[0,t]$.

*(c)* A uniform variable on $[0,1]$ has mean $\tfrac12$, so $\mathbb{E}[A_1\mid N(1)=1]=\tfrac12$; and
$\Pr\bigl(A_1\le\tfrac12\mid N(1)=1\bigr)=\tfrac12$.

**19.** *(a)* The merged stream has rate $10$; each arrival is of type $A$ with probability $6/10$, so the
answer is $0.6$.

*(b)* The wait for the next arrival of the merged stream is exponential with rate $10$ per hour, mean
$1/10$ hour $=6$ minutes.

*(c)* In $10$ minutes $=\tfrac16$ hour the merged count is $\operatorname{Pois}(10/6)$, so
$\Pr(\text{none})=e^{-5/3}=0.1889$.

*(d)* Given two arrivals, each is independently of type $A$ with probability $0.6$, so the answer is
$0.6^{2}=0.36$.

**20.** *(a)* $Q=\begin{pmatrix}-\lambda&\lambda\\ \mu&-\mu\end{pmatrix}$, and from $P'=QP$,
$$p_{11}'=-\lambda p_{11}+\lambda p_{21},\qquad p_{21}'=\mu p_{11}-\mu p_{21}.$$

*(b)* Eliminating $p_{21}$ gives $p_{11}''+(\lambda+\mu)p_{11}'=0$, so $p_{11}=A+Be^{-(\lambda+\mu)t}$;
$p_{11}(0)=1$ and $p_{11}'(0)=-\lambda$ give $B=\frac{\lambda}{\lambda+\mu}$ and
$A=\frac{\mu}{\lambda+\mu}$:
$$p_{11}(t)=\frac{\mu}{\lambda+\mu}+\frac{\lambda}{\lambda+\mu}e^{-(\lambda+\mu)t}.$$
Similarly $p_{21}(t)=\frac{\mu}{\lambda+\mu}\bigl(1-e^{-(\lambda+\mu)t}\bigr)$.

*(c)* $\pi Q=0$ gives $-\lambda\pi_1+\mu\pi_2=0$, so
$\pi=\bigl(\frac{\mu}{\lambda+\mu},\frac{\lambda}{\lambda+\mu}\bigr)$, which is exactly
$\lim_{t\to\infty}p_{11}(t)$ for the first coordinate and $1-p_{11}(t)$ for the second.

*(d)* The holding time in state $1$ is exponential with rate $\lambda$, mean $1/\lambda$.

**21.** *(a)* Two steps return to the origin only by going out and back along the same axis: $4$ choices of
axis-direction and then a forced return, out of $4^{2}=16$ equally likely pairs, so $u_2=\tfrac14$. For four
steps, a closed walk uses one axis twice (both directions) or two axes once each; counting gives $36$
closed walks out of $4^{4}=256$, so $u_4=\tfrac{36}{256}=0.140625$.

*(b)* $\binom21^{2}4^{-2}=4/16=\tfrac14$ and $\binom42^{2}4^{-4}=36/256=\tfrac{9}{64}$, both matching.

*(c)* In general the walk is a product of independent one-dimensional walks in the two coordinates, which
gives $u_{2n}=\binom{2n}{n}^{2}4^{-2n}$. By Stirling, $\binom{2n}{n}\sim4^{n}/\sqrt{\pi n}$, so
$u_{2n}\sim16^{n}/(\pi n)\cdot16^{-n}=1/(\pi n)$. Since $\sum n^{-1}$ diverges, Theorem 7.4 (applied to the
irreducible walk) makes the origin recurrent, and by irreducibility every state is.

**22.** *(a)* $S_{n\wedge T}$ is bounded by $\max(a,b)$ and $T<\infty$ a.s., so Theorem 7.32 gives
$\mathbb{E}[S_T]=0$. Hence $b\,p-a(1-p)=0$ with $p=\Pr(S_T=b)$, that is $p=\frac{a}{a+b}$.

*(b)* With $M_n=S_n^{2}-n$, the same theorem gives $\mathbb{E}[S_T^{2}]=\mathbb{E}[T]$. Now
$\mathbb{E}[S_T^{2}]=b^{2}\frac{a}{a+b}+a^{2}\frac{b}{a+b}=\frac{ab(a+b)}{a+b}=ab$, so
$\mathbb{E}[T]=ab$.

*(c)* Starting at $i=a$ in the state space $\{0,a+b\}$ gives $h=\frac{i}{N}=\frac{a}{a+b}$ and
$k=i(N-i)=a(a+b-a)=ab$, identical.

**23.** For even $n$, $p^{(n)}_{1\cdot}=(\tfrac12,0,\tfrac12)$ (from $P^{2}$), whose distance to
$\pi=(\tfrac14,\tfrac12,\tfrac14)$ is $\tfrac12(0.25+0.5+0.25)=\tfrac12$. For odd $n$,
$p^{(n)}_{1\cdot}=(0,1,0)$, whose distance is again $\tfrac12$. So the distance is constantly $\tfrac12$ and
does not tend to $0$: the chain is periodic and $p^{(n)}_{11}=0$ on odd $n$ while $\pi_1=\tfrac14$.

The Cesàro average is
$\frac1n\sum_{k<n}p^{(k)}_{1\cdot}\to\tfrac12\bigl[(\tfrac12,0,\tfrac12)+(0,1,0)\bigr] =(\tfrac14,\tfrac12,\tfrac14)=\pi$.

**24.** From Exercise 6 with $a=0.25$, $b=0.5$: $\pi_1=\frac{0.5}{0.75}=\tfrac23$, so $1/\pi_1=\tfrac32$.

Direct computation. $\Pr(T^{+}_1>n)=\Pr(X_1\ne1,\dots,X_n\ne1)$: to avoid state $1$ for $n$ steps the chain
must move to $2$ at the first step (probability $0.25$) and then stay in $2$ for the remaining $n-1$ steps
(probability $0.5^{n-1}$), so $\Pr(T^{+}_1>n)=0.25\cdot0.5^{n-1}$ for $n\ge1$. Hence
$$\mathbb{E}[T^{+}_1]=\sum_{n\ge0}\Pr(T^{+}_1>n)=1+\sum_{n\ge1}0.25\cdot0.5^{n-1}
=1+0.25\cdot2=1.5=\frac{1}{\pi_1},$$
confirming Kac's formula.

## Advanced

**25.** *(a)* $\leftrightarrow$ is an equivalence relation (reflexivity by $p^{(0)}_{ii}=1$, symmetry by
definition, transitivity by Chapman–Kolmogorov), so $S$ is partitioned into communicating classes. Contract
each class to a vertex; the relation "$C$ leads to $D$" is a directed graph with no cycles (a cycle would
merge the classes), hence a finite DAG, which has at least one sink: a class from which no other class is
reachable. That class is closed.

*(b)* Restricted to a closed class $C$, the chain never leaves, and $C$ is finite and irreducible, so
Theorem 7.6 makes every state of $C$ recurrent (returns computed in the sub-chain coincide with returns in
the full chain, since the chain never leaves $C$). For a state $i$ outside every closed class, there is a
path of positive probability from $i$ into a closed class $C$; once in $C$ the chain never returns to $i$.
Hence with positive probability the chain never returns to $i$, so $i$ is transient.

*(c)* Let $\pi$ be stationary. Transient states carry no mass: for $T$ the set of transient states,
$\sum_{j\in T}p^{(n)}_{ij}\to0$ as $n\to\infty$ for each $i$ (transient states are visited finitely often,
so the probability of being there tends to $0$), hence by dominated convergence
$\sum_{j\in T}\pi_j=\sum_i\pi_i\sum_{j\in T}p^{(n)}_{ij}\to0$.
On a closed class $C$, $\pi$ restricted to $C$ satisfies
$\pi_j=\sum_{i\in C}\pi_ip_{ij}$ (classes cannot feed $C$ from outside), so it is stationary for the
irreducible chain on $C$, and by Theorem 7.9 it equals $\lambda_C\pi^{C}$ with
$\lambda_C=\sum_{j\in C}\pi_j\ge0$. Summing over closed classes, $\pi=\sum_C\lambda_C\pi^{C}$ with
$\sum_C\lambda_C=1$; conversely any such combination is stationary. The set is a singleton exactly when there
is one closed class.

**26.** *(a)* Theorem 7.5 gives $d(i)=d(j)$ for communicating states. Choose $s$ with $p^{(s)}_{ji}>0$. If
$p^{(n)}_{ij}>0$ and $p^{(m)}_{ij}>0$, then by Chapman–Kolmogorov
$p^{(s+n)}_{jj}\ge p^{(s)}_{ji}p^{(n)}_{ij}>0$ and $p^{(s+m)}_{jj}\ge p^{(s)}_{ji}p^{(m)}_{ij}>0$, so $d$ divides
both $s+n$ and $s+m$, hence divides their difference $n-m$.

*(b)* Fix $i_0$ and define $C_r=\{j:p^{(n)}_{i_0j}>0\text{ for some }n\equiv r\pmod d\}$ for
$r=0,\dots,d-1$. By (a) the definition is unambiguous, and irreducibility puts every state in exactly one
$C_r$. If $i\in C_r$ and $p_{ij}>0$, extend a path of length $n\equiv r$ from $i_0$ to $i$ by one step:
$p^{(n+1)}_{i_0j}\ge p^{(n)}_{i_0i}p_{ij}>0$, so $j\in C_{r+1}$.

*(c)* If $p^{(n)}_{ii}>0$ and $i\in C_r$, then by (b) applied to the path of length $n$ from $i$ to $i$,
$i\in C_{r+n}$ as well; hence $r\equiv r+n\pmod d$ and $d\mid n$. So returns occur only at multiples of
$d$, which is why $p^{(n)}_{ii}=0$ unless $d\mid n$.

**27.** *(a)* The limit $\Pi$ exists by Corollary 7.10 and has all rows equal to $\pi$. Then
$$\Pi P=\lim_n\frac1n\sum_{k=0}^{n-1}P^{k+1}=\lim_n\frac1n\Bigl(\sum_{k=1}^{n}P^{k}\Bigr)=\Pi,$$
because the two averages differ by $(P^{n}-I)/n\to0$; similarly $P\Pi=\Pi$. Finally
$\Pi^{2}=\Pi\Pi$ has rows $\pi\Pi=(\sum_j\pi_j)\pi=\pi$, so $\Pi^{2}=\Pi$: $\Pi$ is a projection onto the
stationary vector.

*(b)* If $P$ is aperiodic, Theorem 7.14 gives $P^{n}\to\Pi$. If $P$ has period $d\ge2$ then by Exercise 26,
$p^{(n)}_{ii}=0$ whenever $d\nmid n$, whereas $\pi_i>0$ by Proposition 7.8; so $p^{(n)}_{ii}$ cannot converge
to $\pi_i$ and $P^{n}$ has no limit.

*(c)* For Example 9.2, $P^{2n}=P^{2}$ and $P^{2n+1}=P$, so the two subsequential limits are
$$P^{2}=\begin{pmatrix}\tfrac12&0&\tfrac12\\ 0&1&0\\ \tfrac12&0&\tfrac12\end{pmatrix},\qquad
P=\begin{pmatrix}0&1&0\\ \tfrac12&0&\tfrac12\\ 0&1&0\end{pmatrix},$$
which differ; their average is $\Pi$.

**28.** *(a)* For $f,g\in\ell^{2}(\pi)$,
$$\langle Pf,g\rangle_\pi=\sum_j\pi_jg(j)\sum_ip_{ij}f(i)=\sum_if(i)\pi_i\sum_jp_{ij}g(j)=\langle f,Pg\rangle_\pi,$$
where the middle equality uses $\pi_ip_{ij}=\pi_jp_{ji}$. So $P$ is self-adjoint for the inner product
$\langle f,g\rangle_\pi=\sum_j\pi_jf(j)g(j)$, hence orthogonally diagonalisable with real eigenvalues; they lie
in $[-1,1]$ because $P$ is stochastic, and irreducibility makes $1$ a simple eigenvalue with eigenfunction
$\mathbf 1$. A remaining eigenvalue can have modulus $1$ only when the chain is periodic (for instance
$\lambda=-1$ for a bipartite walk), so $\lvert\lambda_k\rvert<1$ for $k\ge2$ exactly in the aperiodic case.

*(b)* Let $\phi_k$ be orthonormal eigenfunctions with $\phi_1\equiv1$. The spectral decomposition gives
$p^{(n)}_{ij}=\pi_j\sum_k\lambda_k^{n}\phi_k(i)\phi_k(j)$, so
$$\sum_j\frac{(p^{(n)}_{ij}-\pi_j)^{2}}{\pi_j}=\sum_j\pi_j\Bigl(\sum_{k\ge2}\lambda_k^{n}\phi_k(i)\phi_k(j)
\Bigr)^{2}\le\lambda_*^{2n}\sum_j\pi_j\Bigl(\sum_{k\ge2}\phi_k(i)\phi_k(j)\Bigr)^{2}.$$
Using completeness $\sum_k\phi_k(i)\phi_k(j)=\delta_{ij}/\pi_i$ and dropping the $k=1$ term,
$\sum_j\pi_j(\sum_{k\ge2}\phi_k(i)\phi_k(j))^{2}\le\sum_j\pi_j(\delta_{ij}/\pi_i)^{2}=1/\pi_i$; hence the
bound.

*(c)* By Cauchy–Schwarz,
$\lVert p^{(n)}_{i\cdot}-\pi\rVert_{TV}=\tfrac12\sum_j\pi_j\lvert h_j\rvert \le\tfrac12\bigl(\sum_j\pi_jh_j^{2}\bigr)^{1/2}$
with $h_j=p^{(n)}_{ij}/\pi_j-1$, which is exactly $\tfrac12$ times the square root of the
chi-squared quantity, hence at most $\tfrac12\lambda_*^{n}/\sqrt{\pi_i}$.

**29.** *(a)* For the chain of Exercise 1 every entry of $P$ is positive, so $N=1$ works (and $N=1$ is
minimal).

*(b)* With $N=1$, $\delta=\min_{a,c}p_{ac}=0.25$, so the coupling bound is
$\Pr(T>m)\le(1-\delta)^{m}=0.75^{m}$ and hence
$\lVert p^{(n)}_{i\cdot}-\pi\rVert_{TV}\le0.75^{n}$.

*(c)* The bound $0.75^{n}<0.01$ requires $n>\ln(100)/\ln(4/3)=16.0$, so the coupling guarantees mixing by
$n=16$. The exact computation gives $0.6^{n}$ decay — using the second eigenvalue $\lambda_2=0.25$ of this
chain, $p^{(n)}_{21}=0.75-0.75(0.25)^{n}$, so the exact distance is $0.75(0.25)^{n}$ and $n=4$ suffices.
The coupling bound is thus off by a factor of about four in $n$, which is typical: coupling uses only the
worst-case one-step overlap, not the spectrum.

**30.** *(a)* Conditioning on the first step, and noting that $k^{(j)}_j=0$,
$k^{(j)}_i=1+\sum_lp_{il}k^{(j)}_l=1+\sum_{l\ne j}p_{il}k^{(j)}_l$ for $i\ne j$.

*(b)* The system is $(I-Q)k=\mathbf 1$ where $Q=(p_{il})_{i,l\ne j}$. Since the chain is finite and
irreducible, $j$ is reachable from every state, so Theorem 7.17 applies: $I-Q$ is invertible and the solution
is unique, equal to $N\mathbf 1$ with $N=\sum_nQ^{n}$.

*(c)* For the chain of Exercise 1: from state $1$ the chance of moving to $2$ at each step is $p_{12}=0.25$
independently, so $T_2$ is geometric with success probability $0.25$ and $\mathbb{E}_1[T_2]=4$. Similarly
$\mathbb{E}_2[T_1]=1/p_{21}=2$. Direct check of the first: $k_1=1+0.75k_1$ gives $k_1=4$; of the second:
$k_2=1+0.5k_2$ gives $k_2=2$.

*(d)* $1/\pi_j$ is the mean return time *starting from $j$* (Kac), while $k^{(j)}_i$ starts from $i\ne j$.
Here $\pi_2=\tfrac13$ so $1/\pi_2=3$, but $\mathbb{E}_1[T_2]=4$: hitting times depend on the start, return
times do not.

**31.** *(a)* Let $N=N_1+N_2$. For $0\le z\le1$, independence gives
$\mathbb{E}[z^{N(t)}]=e^{\lambda_1t(z-1)}e^{\lambda_2t(z-1)}=e^{(\lambda_1+\lambda_2)t(z-1)}$, the
generating function of $\operatorname{Pois}((\lambda_1+\lambda_2)t)$; generating functions determine laws on
$\mathbb{N}_0$. Increments over disjoint intervals are sums of independent increments of $N_1$ and $N_2$, so
they are independent, and the stationary property is inherited. Hence $N$ is a Poisson process of the summed
rate.

*(b)* Let $N_1,N_2$ count kept and discarded arrivals. Condition on $N(t)=n$ and expand:
$$\mathbb{E}\bigl[z_1^{N_1(t)}z_2^{N_2(t)}\bigr]
=\sum_{n\ge0}e^{-\lambda t}\frac{(\lambda t)^{n}}{n!}\bigl(pz_1+(1-p)z_2\bigr)^{n}
=e^{-\lambda t}e^{\lambda t(pz_1+(1-p)z_2)}
=e^{p\lambda t(z_1-1)}e^{(1-p)\lambda t(z_2-1)}.$$
The factorisation is the product of the generating functions of $\operatorname{Pois}(p\lambda t)$ and
$\operatorname{Pois}((1-p)\lambda t)$, which proves the marginals and independence simultaneously; increments
are handled by applying the same computation on each interval.

**32.** *(a)* To be at $0$ after $2n$ steps the walk must take exactly $n$ up-steps among $2n$, so
$u_{2n}=\binom{2n}{n}2^{-2n}=\binom{2n}{n}4^{-n}$. Stirling's formula gives
$\binom{2n}{n}\sim\frac{(2n)^{2n}e^{-2n}\sqrt{4\pi n}}{n^{2n}e^{-2n}(2\pi n)}=\frac{4^{n}}{\sqrt{\pi n}}$,
hence $u_{2n}\sim(\pi n)^{-1/2}$.

*(b)* $\sum_nn^{-1/2}=\infty$ (comparison with $\int x^{-1/2}dx$), and odd terms vanish, so
$\sum_nu_n=\infty$; by Theorem 7.4 and irreducibility the walk is recurrent.

*(c)* Suppose $\mathbb{E}_0[T^{+}_0]=m<\infty$. The regenerative argument of Theorem 7.16 (the cycles between
returns are i.i.d.) gives $\frac1n\sum_{k<n}u_k\to1/m>0$. But $u_k\to0$ by (a), and a sequence tending to $0$
has Cesàro means tending to $0$. Contradiction, so $m=\infty$: the walk is null recurrent.

**33.** *(a)* Local limit theorem. Let $X_i$ be i.i.d. lattice variables with finite mean $\mu$, finite non-singular
covariance $\Sigma$, and span $h$ (the largest $h$ such that the walk lives on a coset of $h\mathbb{Z}^{d}$
after centring). Then uniformly in $x$,
$$\Pr(S_n=x)\sim\frac{h^{d}}{(2\pi n)^{d/2}\sqrt{\det\Sigma}}
\exp\Bigl(-\frac{1}{2n}(x-n\mu)^{T}\Sigma^{-1}(x-n\mu)\Bigr).$$
For the simple symmetric walk $\mu=0$, $\Sigma=\frac1dI$, and the parity constraint gives span $2$; evaluating
at $x=0$ gives $u_{2n}\sim C_dn^{-d/2}$ with $C_d>0$.

*(b)* Consequently there are $C<\infty$ and $n_0$ with $u_{2n}\le Cn^{-3/2}$ for $n\ge n_0$; since
$\sum_{n\ge n_0}n^{-3/2}<\infty$ and $u_{2n+1}=0$,
$\sum_nu_n<\infty$.

*(c)* By Theorem 7.4 the walk is transient. Dimension three is the threshold because the return probability
decays like $n^{-d/2}$ and $\sum n^{-d/2}$ converges exactly when $d/2>1$, i.e. $d\ge3$.

**34.** *(a)* Write $M_T=M_0+\sum_{k=0}^{K-1}(M_{k+1}-M_k)\mathbf 1\{T>k\}$, legitimate because $T\le K$ makes
the sum finite. Since $\{T>k\}=\{T\le k\}^{c}\in\mathcal{F}_k$,
$$\mathbb{E}\bigl[(M_{k+1}-M_k)\mathbf 1\{T>k\}\bigr]
=\mathbb{E}\bigl[\mathbf 1\{T>k\}\,\mathbb{E}[M_{k+1}-M_k\mid\mathcal{F}_k]\bigr]=0.$$
Summing over $k$ gives $\mathbb{E}[M_T]=\mathbb{E}[M_0]$.

*(b)* For a stopping time with $T<\infty$ a.s., apply (a) to $T\wedge n$:
$\mathbb{E}[M_{T\wedge n}] =\mathbb{E}[M_0]$. If $\lvert M_{n\wedge T}\rvert\le Y$ with
$\mathbb{E}Y<\infty$, dominated convergence gives $\mathbb{E}[M_{T\wedge n}]\to\mathbb{E}[M_T]$.
If instead the increments are bounded by $C$ and $\mathbb{E}T<\infty$, then
$\lvert M_{n\wedge T}\rvert\le\lvert M_0\rvert+CT$ is integrable, so the dominated version
applies.

*(c)* For $T=\inf\{n:S_n=1\}$ the hypothesis $\mathbb{E}T<\infty$ fails: by the reflection principle for the
walk, $\Pr(T>n)\approx c\,n^{-1/2}$, so $\mathbb{E}T=\sum_n\Pr(T>n)=\infty$. Equivalently there is no
integrable dominating variable, since $S_{n\wedge T}$ is unbounded below. And indeed
$\mathbb{E}[S_T]=1\ne0=\mathbb{E}[S_0]$.

## Challenge

**35.** *(a)* Each row of $dP+(1-d)\frac1n\mathbf{1}\mathbf{1}^{\mathsf T}$ is a convex combination of a
probability row and the uniform row, so entries are non-negative and rows sum to $1$: $G$ is stochastic. Every
entry satisfies $G_{ij}\ge(1-d)/n>0$, so every state is reachable from every state in one step: irreducible
and aperiodic (each $G_{ii}\ge(1-d)/n>0$).

*(b)* Finite, irreducible and aperiodic, so by Theorems 7.9 and 7.14 there is a unique stationary law and
$G^{n}\to\Pi$; that law is the PageRank vector.

*(c)* With $P$ having rows $(0,1,0),(1,0,0),(1,0,0)$ and $d=0.85$, $(1-d)/3=\frac1{20}$, so
$$G=\begin{pmatrix}0.05&0.9&0.05\\ 0.9&0.05&0.05\\ 0.9&0.05&0.05\end{pmatrix}.$$
The third column equation gives $\pi_3=0.05(\pi_1+\pi_2+\pi_3)=0.05$. The first two are
$0.95\pi_1=0.9\pi_2+0.045$ and $0.95\pi_2=0.9\pi_1+0.0025$. Solving,
$\pi_1=0.486486$, $\pi_2=0.463514$, $\pi_3=0.05$. Note page $3$ has no in-links but still receives
$5\%$ of the mass, all of it from the damping term.

*(d)* Since every entry of $G$ is at least $(1-d)/n$,
$\pi_j=\sum_i\pi_iG_{ij}\ge\sum_i\pi_i(1-d)/n=(1-d)/n>0$.

**36.** *(a)* Let $Y_k=(B_{k t/2^{n}}-B_{(k-1)t/2^{n}})^{2}$. Each $Y_k$ has mean $t/2^{n}$ and, because
$B_{h}\sim\mathcal{N}(0,h)$ has fourth moment $3h^{2}$, variance $2(t/2^{n})^{2}$. The increments are
independent, so $\mathbb{E}Q_n=t$ and
$\operatorname{Var}(Q_n)=2^{n}\cdot2t^{2}4^{-n}=2t^{2}2^{-n}\to0$; hence $Q_n\to t$ in $L^{2}$, and along a
subsequence almost surely.

*(b)* If $B$ were $C^{1}$ on $[0,t]$ with $\lvert B'\rvert\le M$, the mean value theorem would give, for any
partition of mesh $\delta$,
$$\sum_k(\Delta_kB)^{2}\le\max_k\lvert\Delta_kB\rvert\sum_k\lvert\Delta_kB\rvert\le M\delta\cdot Mt\to0,$$
contradicting the limit $t>0$ along dyadic partitions.

*(c)* $B_{n\wedge T}$ is bounded by $\max(a,b)$ and $T<\infty$ a.s. (the walk cannot avoid both barriers
forever), so optional stopping with $B_t$ gives $bp-a(1-p)=0$, i.e. $p=\frac{a}{a+b}$. With $B_t^{2}-t$,
$\mathbb{E}[B_T^{2}]=\mathbb{E}[T]$, and
$\mathbb{E}[B_T^{2}]=b^{2}\frac{a}{a+b}+a^{2}\frac{b}{a+b}=ab$.

*(d)* The hitting-time density $f_{T_a}(t)=\frac{a}{\sqrt{2\pi}}t^{-3/2}e^{-a^{2}/(2t)}$ has a tail like
$t^{-3/2}$, and $\int t\cdot t^{-3/2}dt=\int t^{-1/2}dt=\infty$. There is no contradiction with (c): on a
bounded interval the path is trapped between two barriers and exits quickly, whereas a one-sided level can be
avoided by arbitrarily long negative excursions, and those excursions dominate the mean.

**37.** *(a)* Let $q_n=\Pr(Z_n=0)$. Given $Z_1=k$, the $k$ lines descending from generation $1$ are
independent copies, each extinct at generation $n$ with probability $q_{n-1}$, so
$q_n=\sum_kp_kq_{n-1}^{k}=G(q_{n-1})$. The events $\{Z_n=0\}$ increase with $n$, so $q_n\uparrow q$, and
continuity of $G$ on $[0,1]$ gives $q=G(q)$.

*(b)* If $s\in[0,1]$ satisfies $G(s)=s$, then $q_0=0\le s$ and, $G$ being increasing, $q_n\le s$ for all $n$;
hence $q\le s$. So $q$ is the smallest fixed point.

*(c)* $G$ is convex and increasing with $G(1)=1$ and $G'(1)=\mu$. If $\mu\le1$ and $G(s)=s$ for some $s<1$,
convexity forces the secant slope from $s$ to $1$, which equals $1$, to be at most $G'(1)=\mu\le1$; equality
throughout forces $G$ to be the identity on $[0,1]$, the degenerate case. So for a non-degenerate offspring law
with $\mu\le1$ the only fixed point is $1$ and $q=1$. If $\mu>1$ then $G(s)<s$ for $s$ just below $1$ while
$G(0)\ge0$, so by continuity there is a fixed point in $[0,1)$, and $q<1$.

*(d)* $\mathbb{E}[Z_{n+1}\mid\mathcal{F}_n]=\mathbb{E}\bigl[\sum_{k\le Z_n}\xi_{n,k}\mid Z_n\bigr]=\mu Z_n$,
so $\mathbb{E}[Z_{n+1}/\mu^{n+1}\mid\mathcal{F}_n]=Z_n/\mu^{n}$: it is a non-negative martingale, hence
converges a.s. to a limit $W$ with $\mathbb{E}W\le1$. On extinction $W=0$; on survival $W>0$ and equals the
exponential growth rate of the population, normalised — this is the branching-process analogue of a
likelihood ratio.

**38.** *(a)* The nonzero rates are $q_{n,n+1}=\lambda$ and $q_{n,n-1}=\mu$ for $n\ge1$, with
$q_{00}=-\lambda$ and $q_{nn}=-(\lambda+\mu)$ for $n\ge1$. Acting on $f$,
$Qf(n)=\sum_mq_{nm}f(m)=\lambda f(n+1)+\mu f(n-1)-(\lambda+\mu)f(n)$ for $n\ge1$, and
$Qf(0)=\lambda(f(1)-f(0))$.

*(b)* $\pi Q=0$ in components reads, for $n\ge1$,
$\lambda\pi_{n-1}+\mu\pi_{n+1}-(\lambda+\mu)\pi_n=0$ and for $n=0$, $-\lambda\pi_0+\mu\pi_1=0$. The first
relation rearranges to $\mu(\pi_{n+1}-\pi_n)=\lambda(\pi_n-\pi_{n-1})$, so by induction
$\pi_n=\rho^{n}\pi_0$; normalisation gives $\pi_0=1-\rho$, hence $\pi_n=(1-\rho)\rho^{n}$, a probability law
exactly when $\rho<1$.

*(c)* If $\lambda\ge\mu$ then $\rho\ge1$ and $\sum_n\rho^{n}=\infty$ unless $\pi_0=0$, so no probability
vector solves $\pi Q=0$; equivalently the queue is null recurrent ($\rho=1$) or transient ($\rho>1$) and
wanders to infinity.

*(d)* $\mathbb{E}[\text{number}]=\sum_nn(1-\rho)\rho^{n}=\frac{\rho}{1-\rho}=2$ for $\rho=\tfrac23$. The mean
time in the system follows from the same geometric structure, $W=\frac{1}{\mu-\lambda}=1$ hour, and Little's
law $L=\lambda W$ reads $2=2\cdot1$.

**39.** *(a)* $\{T_a\le t\}=\{\sup_{s\le t}B_s\ge a\}$ by continuity. Splitting $\{B_t\ge a\}$ according to
whether $T_a\le t$ and using the strong Markov property at $T_a$,
$\Pr(B_t\ge a\mid T_a\le t)=\Pr(B_t-B_{T_a}\ge0)=\tfrac12$, so
$\Pr(B_t\ge a)=\tfrac12\Pr(T_a\le t)$.

*(b)* Reflect the path after $T_a$ about the level $a$; this is a measure-preserving bijection between paths
with $T_a\le t$ and $B_t\le x$ and paths with $T_a\le t$ and $B_t\ge2a-x$. For $x\le a$ we have $2a-x\ge a$,
so the event $\{B_t\ge2a-x\}$ already implies $T_a\le t$, giving
$\Pr(T_a\le t,\,B_t\le x)=\Pr(B_t\ge2a-x)$.

*(c)* With $a=1$, $x=0$: $\Pr(T_1\le1,\,B_1\le0)=\Pr(B_1\ge2)=1-\Phi(2)=0.02275$. The naive product is
$\Pr(T_1\le1)\Pr(B_1\le0)=2(1-\Phi(1))\cdot\tfrac12=0.1587$, seven times too large: the two events are
strongly negatively dependent, since hitting level $1$ early tends to push the endpoint up.

*(d)* By (b) with $a=1$, the conditional law of $B_1$ given $T_1\le1$ is symmetric about $1$ (the reflection
exchanges paths ending above and below $1$), so $\mathbb{E}[B_1\mid T_1\le1]=1$. Directly,
$$\mathbb{E}[B_1\mathbf 1\{T_1\le1\}]=\int_{-\infty}^{1}x\,\phi(2-x)dx+\int_{1}^{\infty}x\,\phi(x)dx
=\bigl[2(1-\Phi(1))-\phi(1)\bigr]+\phi(1)=0.3173,$$
which divided by $\Pr(T_1\le1)=0.3173$ gives $1$.

**40.** *(a)* For $0<a_1<\cdots<a_n<t$ the joint density of $(A_1,\dots,A_n)$ and $\{N(t)=n\}$ is
$\prod_{k}\lambda e^{-\lambda(a_k-a_{k-1})}\cdot e^{-\lambda(t-a_n)}=\lambda^{n}e^{-\lambda t}$, constant on
the simplex $0<a_1<\cdots<a_n<t$. Dividing by $\Pr(N(t)=n)=e^{-\lambda t}(\lambda t)^{n}/n!$ gives the
constant density $n!/t^{n}$, which is the joint density of the order statistics of $n$ independent uniforms.

*(b)* The $k$-th order statistic of $n$ uniforms on $[0,t]$ has mean $kt/(n+1)$ (by symmetry, the $n+1$
spacings have equal mean $t/(n+1)$). Hence $\mathbb{E}[A_n\mid N(t)=n]=nt/(n+1)$.

*(c)* Let $L$ be a gap length; $L\sim\operatorname{Exp}(\lambda)$ with $\mathbb{E}L=1/\lambda$ and
$\mathbb{E}L^{2}=2/\lambda^{2}$. A uniformly chosen instant is more likely to fall in a long gap: the chance
that $U$ lies in a given gap is proportional to that gap's length, so the length of the gap containing $U$ has
the size-biased law with mean
$$\frac{\int l\cdot l\,dF(l)}{\int l\,dF(l)}=\frac{\mathbb{E}[L^{2}]}{\mathbb{E}[L]}=\frac{2/\lambda^{2}}{1/\lambda}=\frac{2}{\lambda}.$$
(The factor $2$ is exact in the limit $T\to\infty$ because the boundary gaps contribute $o(T)$.) This is the
inspection paradox: the mean gap is $1/\lambda$, but the mean *experienced* gap is twice that, since long
gaps occupy more of the time line.
