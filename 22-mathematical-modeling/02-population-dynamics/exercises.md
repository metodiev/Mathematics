# Population Dynamics — Exercises

> [Population Dynamics](README.md) · 38 problems · Beginner → Challenge · Solutions: [solutions.md](solutions.md)

Attempt every problem in writing before consulting [solutions.md](solutions.md). Each problem names the section of the tutorial that supplies the technique. Problems marked *(open)* have a defensible answer rather than a unique one; the solution gives a model answer and the criteria for judging one.

**Notation.** $N$ is population size, $r$ the intrinsic growth rate, $K$ the carrying capacity, $H$ a constant harvest, $E$ effort, $q$ catchability, $x_t$ the scaled population of a discrete model, $L$ a Leslie matrix, and $\lambda_1$ its Perron eigenvalue. For the Lotka–Volterra system the constants are $a,b,\delta,c$; for competition they are $r_1,r_2,K_1,K_2,\alpha,\beta$; $A$ is the Allee threshold. Unless stated otherwise all parameters are positive and populations are non-negative.

## Beginner

**1.** *(§7.1)* Compute the doubling time, exactly and by the rule of 70, for (a) $r = 0.01$ yr⁻¹, (b) $r = 0.03$ yr⁻¹, (c) $r = 0.10$ yr⁻¹.

**2.** *(§7.1)* A population grows fivefold in 20 years. Assuming exponential growth, find $r$ and the doubling time.

**3.** *(§7.1)* A bacterial culture doubles every 30 minutes, starting from $100$ cells. How many cells are there after 6 hours? How long until the count first exceeds one million?

**4.** *(§7.2)* A population obeys the logistic equation with $r = 0.3$ yr⁻¹, $K = 500$ and $N_0 = 20$. Compute (a) $N(10)$; (b) the time of the inflection; (c) the maximum growth rate.

**5.** *(§7.2)* A logistic population with $K = 1000$ doubles from $N = 100$ to $N = 200$. Find the elapsed time as a multiple of $1/r$, and explain why the answer does not depend on $K$ beyond the initial ratio.

**6.** *(§7.3)* For each rate law, draw the sign diagram, list the equilibria, and classify each as stable or unstable: (a) $f(N) = N(1-N)(N-2)$; (b) $f(N) = (N-1)(3-N)$; (c) $f(N) = N(2-N)$.

**7.** *(§7.3)* Use the explicit logistic solution to show that $K$ is globally asymptotically stable on $(0,\infty)$, without using the derivative test.

**8.** *(§7.4)* A stock obeys the logistic law with $r = 0.2$ yr⁻¹ and $K = 10^4$. (a) Compute the MSY and the stock at which it is achieved. (b) For $H = 400$, find both equilibria and say which is stable.

**9.** *(§7.4)* Prove that for any admissible quota $0 < H < rK/4$ the stable equilibrium exceeds $K/2$ and the unstable one lies below $K/2$.

**10.** *(§7.6)* For $x_{t+1} = 2x_t(1-x_t)$: (a) find the nonzero fixed point and its multiplier; (b) iterate from $x_0 = 0.1$ for four steps and describe the approach.

**11.** *(§7.7)* For $L = \begin{pmatrix}0&3\\0.5&0\end{pmatrix}$: (a) find the eigenvalues; (b) decide whether $L$ is primitive; (c) state what the answer to (b) implies for the long-run age distribution.

**12.** *(§7.8)* For the Lotka–Volterra system with $a=1$, $b=0.02$, $\delta=0.004$, $c=0.4$, find the interior equilibrium and verify that it lies on both nullclines.

**13.** *(§7.8)* For the first integral $H = \delta x - c\ln x + by - a\ln y$: (a) compute $\partial_xH$ and $\partial_yH$; (b) find the unique stationary point; (c) show that it is a minimum by computing the second partial derivatives.

**14.** *(§7.9)* For the competition model with $K_1 = 2000$, $K_2 = 1500$, $\alpha = 0.8$, $\beta = 0.9$: compute both invasion criteria, decide the outcome, and confirm by computing the interior equilibrium.

## Intermediate

**15.** *(§7.1, §7.2)* Show that a logistic population with $N_0 = 0.01K$ stays within $5\%$ of the exponential curve $N_0e^{rt}$ until $rt \approx 1.835$. Interpret the result.

**16.** *(§7.4)* A stock has $r = 0.4$ yr⁻¹ and $K = 2000$. (a) Compute the MSY. (b) Find the equilibria for $H = 150$. (c) Find the largest quota for which the stable equilibrium is at least $0.7K$.

**17.** *(§7.5)* A stock has $r = 0.8$ yr⁻¹, $K = 5000$ and $q = 0.002$. Compute the equilibrium stock and the sustainable yield at $E = 100$, $200$, $300$ and $400$, and identify the critical effort.

**18.** *(§7.5)* An open-access fishery has $p = 500$ per tonne, $c = 3000$ per vessel-year, $q = 10^{-4}$, $K = 2\times10^6$ tonnes. (a) Compute the open-access stock. (b) Compute the fraction of $K$ it represents and compare with the MSY stock.

**19.** *(§7.6)* For $x_{t+1} = 2.8x_t(1-x_t)$: (a) find the fixed point and its multiplier; (b) iterate six times from $x_0 = 0.3$ and describe the pattern.

**20.** *(§7.6)* For $R = 3.4$: find the exact 2-cycle, compute its multiplier, and decide whether it is attracting. Confirm by iterating from a nearby point.

**21.** *(§7.7)* For $L = \begin{pmatrix}1.5&2\\0.4&0\end{pmatrix}$: (a) find both eigenvalues; (b) find the stable age distribution; (c) confirm with the Euler–Lotka equation.

**22.** *(§7.5)* Show that the sustainable yield of an effort-harvested logistic stock is $Y(E) = qEK(1-qE/r)$ and that its maximum is $rK/4$, attained at $E = r/(2q)$.

**23.** *(§7.8)* For $a=1$, $b=0.02$, $\delta=0.004$, $c=0.4$: (a) compute the time averages $\bar x$ and $\bar y$; (b) compute the small-amplitude period; (c) explain why the averages do not depend on the amplitude while the period does.

**24.** *(§7.8)* In the Lotka–Volterra model, suppose the prey is harvested at rate $hx$ so that $\dot x = ax - bxy - hx$. Find the new interior equilibrium and explain the result: which species is harmed?

## Advanced

**25.** *(§7.3)* Prove both parts of Theorem 7.3.1: if $f'(N^*)<0$ the equilibrium is asymptotically stable, and if $f'(N^*)>0$ it is unstable. State precisely where continuity of $f'$ is used.

**26.** *(§7.8)* Prove that the Lotka–Volterra orbits are closed curves. Your proof should establish that $H$ is strictly convex, that it has a unique minimum at the interior equilibrium, and that no orbit on a positive level set can terminate.

**27.** *(§7.4)* Put $N = K/2 + u$ and $H = rK/4 - \mu$ in the harvested logistic equation and derive the normal form $\dot u = \mu - ru^2/K$. Deduce the square-root dependence of the equilibrium on the distance to the fold, and explain why the return rate vanishes at the fold.

**28.** *(§7.10)* For the Allee model with $r=1$, $K=1000$, $A=200$: (a) verify the three equilibria and their stability; (b) find the largest sustainable constant harvest by maximising $f$ on $[A,K]$, and compare with the logistic MSY $rK/4$.

**29.** *(§7.9)* Prove that in Case 1 ($K_1>\alpha K_2$ and $K_2>\beta K_1$) one has $\alpha\beta<1$, and that in Case 2 ($K_1<\alpha K_2$ and $K_2<\beta K_1$) one has $\alpha\beta>1$. Deduce that the interior equilibrium is positive exactly in Cases 1 and 2, that it is stable exactly in Case 1, and that in Case 2 it is a saddle whose stable manifold separates the basins of the two monocultures.

**30.** *(§7.6)* Derive the 2-cycle $x_\pm = \frac{R+1\pm\sqrt{(R-3)(R+1)}}{2R}$ and the multiplier $\mu = 4+2R-R^2$ of the logistic map.

**31.** *(§7.2)* Show that the logistic solution can be written
$$N(t) = \frac{K}{2}\left[1 + \tanh\left(\frac{r}{2}\left(t - t_{\text{infl}}\right)\right)\right],$$
and use it to show that $N$ is antisymmetric about $(t_{\text{infl}}, K/2)$ in the sense that $N(t_{\text{infl}}+s) + N(t_{\text{infl}}-s) = K$.

**32.** *(§7.5)* Derive the open-access equilibrium of the Gordon–Schaefer model, including the stock $c/(pq)$, and prove that the open-access yield satisfies $Y_{oa} \le Y_{\mathrm{MSY}}$, with equality only when $c/(pqK) = 1/2$.

## Challenge

**33.** *(§7.4)* For $r = 0.4$, $K = 2000$, compute the normalised sensitivity $S_H$ of the stable equilibrium at $H = 100$, $150$ and $195$, and explain the pattern. State a management conclusion that does not require more data.

**34.** *(§7.7)* The matrix
$$L = \begin{pmatrix}0.2&1&1.2\\ 0.5&0&0\\ 0&0.5&0\end{pmatrix}$$
has $\lambda_1 = 1$. (a) Verify this with the Euler–Lotka equation. (b) Starting from $\mathbf n(0) = (0,100,0)$, compute $\mathbf n(1)$, $\mathbf n(2)$, $\mathbf n(3)$ and the totals. (c) Explain why the total rises although $\lambda_1=1$. (d) Find the stable age distribution.

**35.** *(§7.11, open)* A paper reports that a 40-year annual census of a bird population shows chaotic dynamics. State three alternative explanations that the author should have excluded, and describe the analysis you would require before accepting the claim.

**36.** *(§7.5)* A fishery is managed not by effort but by an annual quota of $Q = 100\,000$ tonnes, with $r = 0.5$ yr⁻¹ and $K = 10^6$ tonnes. (a) Find the two equilibrium stocks. (b) Compare the stable one with the open-access stock $2\times10^5$ (Example 9.4) and the sole-owner stock $6\times10^5$. (c) Explain why the quota regime and the open-access regime give different answers for the same biology.

**37.** *(§7.8)* Add prey self-limitation to the Lotka–Volterra model: $\dot x = ax(1-x/K) - bxy$. (a) Find the interior equilibrium. (b) Compute the Jacobian and show that the equilibrium is asymptotically stable for every admissible parameter choice. (c) Explain what this says about the neutral cycles of the original model.

**38.** *(§7.6)* (a) Prove the identity $4\sin^2(\pi\theta)\cos^2(\pi\theta) = \sin^2(2\pi\theta)$ and hence that $x\mapsto4x(1-x)$ is conjugate to $\theta\mapsto2\theta \bmod 1$ on $[0,1]$. (b) Deduce that exactly $2^n$ points of $[0,1]$ are fixed by the $n$-fold iterate, and hence compute the number of points whose *exact* period is $n$, for $n = 1,2,3,4$. (c) Deduce that the periodic points are dense.
