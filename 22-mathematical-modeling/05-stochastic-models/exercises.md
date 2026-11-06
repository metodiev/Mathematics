# Stochastic Models — Exercises

> [Stochastic Models](README.md) · 40 problems · Beginner → Challenge · Solutions: [solutions.md](solutions.md)

Work through the problems in order. Every problem can be solved with the definitions, theorems and techniques of the [tutorial](README.md); the section reference tells you where to look. Attempt every problem in writing before consulting [solutions.md](solutions.md).

**Conventions.** Losses are positive; time is in hours unless stated. VaR and ES are at the stated level. Give numerical answers to four significant figures, and state any assumption you add.

## Beginner

**1.** *(§7.1)* For each item, say whether the uncertainty is aleatory or epistemic, and whether a stochastic model is the right tool.

(a) The number of customers arriving at a shop tomorrow.
(b) The average lifetime of a batch of bearings, estimated from a sample.
(c) The number showing on the next die roll.
(d) Whether a new drug will work in a patient.
(e) The true failure rate of a new component, before any tests.

**2.** *(§7.6)* A product is graded A, B or C with probabilities $0.15$, $0.55$ and $0.30$. A simulation draws the uniforms $0.83$, $0.07$, $0.62$ and $0.99$.

(a) Give the grade for each draw, using inverse transform with the values A $=90$, B $=75$, C $=60$.
(b) Compute the mean and variance of the grade.

**3.** *(§7.6)* Inter-arrival times are exponential with rate $\lambda = 0.25$ per minute.

(a) Write the inverse transform formula.
(b) Compute the inter-arrival time for $u = 0.1$, $0.5$ and $0.9$.
(c) Verify that the mean of the distribution is 4 minutes.

**4.** *(§7.2)* Eight independent simulation runs of a daily cost gave $42, 38, 51, 45, 47, 39, 44, 40$ (k€).

(a) Compute the sample mean and sample standard deviation.
(b) Compute the standard error and a 95 % confidence interval for the mean.
(c) How many runs would be needed to halve the width of the interval?

**5.** *(§7.2, §7.3)* A simulation has a per-run standard deviation of $2.5$.

(a) Compute the standard error for $n = 100$, $1000$, $10^4$ and $10^6$.
(b) How many runs are needed for a standard error of at most $0.01$?
(c) Explain why the answer does not depend on the mean.

**6.** *(§7.7)* An M/M/1 queue has arrival rate $\lambda = 4$ and service rate $\mu = 6$ per hour.

(a) Compute $\rho$ and verify stability.
(b) Compute $P_0$, $L$, $L_q$, $W$, $W_q$.
(c) Compute $\Pr(N \ge 3)$.

**7.** *(§7.8)* A shop has on average 12 customers present, and each spends on average 15 minutes.

(a) What is the arrival rate implied by Little's law?
(b) If the arrival rate rises to 60 per hour and the average time in the shop stays 15 minutes, what is the average number present?
(c) State one assumption needed for each answer.

**8.** *(§7.9)* A fair random walk starts at 30 with absorbing barriers at 0 and 50.

(a) Compute the probability of ruin.
(b) Compute the expected duration.
(c) Explain why the ruin probability depends only on the relative positions of the start and the barriers, while the expected number of steps would fall by a factor of four if each step were $\pm 2$ instead of $\pm 1$.

**9.** *(§7.12)* A portfolio's daily loss is normal with mean $\mu = 2$ and standard deviation $\sigma = 5$ (both in €m).

(a) Compute $\operatorname{VaR}_{0.99}$ and $\operatorname{ES}_{0.99}$.
(b) Compute both at the 97.5 % level.
(c) Explain why ES exceeds VaR and by how much in each case.

**10.** *(§7.12)* A loss is $0$ with probability $0.9$ and $50$ with probability $0.1$.

(a) Compute $\operatorname{VaR}_{0.9}$ and $\operatorname{ES}_{0.9}$.
(b) Explain the difference in one sentence, and say which you would report to a regulator.

**11.** *(§7.6)* To sample from $f(x) = 2x$ on $[0,1]$, use the uniform envelope $g = 1$ with $M = 2$.

(a) Write the acceptance test.
(b) Compute the acceptance probability and the expected number of proposals for 1000 accepted draws.
(c) Show that the accepted draws have mean $2/3$.

**12.** *(§7.10)* A share price follows geometric Brownian motion with $S_0 = 50$, $\mu = 0.08$, $\sigma = 0.25$ and $T = 2$ years.

(a) Compute $\mathbb{E}[S_T]$ and the median of $S_T$.
(b) Compute $\Pr(S_T < S_0)$.
(c) Explain why the mean and the median differ, and which one a long-term investor should quote.

## Intermediate

**13.** *(§7.4)* Estimate $\theta = \int_0^1 u^2\,du$ by Monte Carlo.

(a) Compute $\operatorname{Var}(U^2)$.
(b) Compute the variance of the antithetic pair average $\frac12(U^2 + (1-U)^2)$.
(c) Compute the variance ratio for the same number of function evaluations, and the equivalent speed-up.

**14.** *(§7.5)* Let $X \sim \mathrm{Exp}(1)$ and estimate $p = \Pr(X > 3) = e^{-3} = 0.049787$ by importance sampling with proposal $\mathrm{Exp}(\lambda)$.

(a) Derive the weight and verify unbiasedness.
(b) Compute the second moment of the estimator as a function of $\lambda$, and find the $\lambda$ that minimises it.
(c) Compute the variance ratio at the optimal $\lambda$ against naive sampling.

**15.** *(§7.7)* Customers arrive at $\lambda = 10$ per hour at a single server.

(a) Find the smallest service rate $\mu$ for which the average wait $W_q$ is at most $0.05$ h.
(b) Compute $L$ and $L_q$ at that $\mu$.
(c) Explain why the required capacity is twice the load.

**16.** *(§7.9)* A gambler plays a biased game with $p = 0.6$, starting with 20 units, until reaching 40 or 0.

(a) Compute the probability of reaching 40.
(b) Compute the expected number of rounds.
(c) Compare with the fair game, and explain the direction of the difference.

**17.** *(§7.2, §7.11)* An Euler–Maruyama simulation of geometric Brownian motion (100, $\mu = 0.1$, $\sigma = 0.2$, $T = 1$) with monthly steps reports a mean terminal value of $110.4713$ with a Monte Carlo standard error of $0.005$. The exact mean is $110.5171$.

(a) State the two sources of discrepancy.
(b) Decide which one dominates, with a calculation.
(c) Say what you would change to remove the dominant one.

**18.** *(§7.12)* Three independent assets each lose 100 with probability $0.03$ and nothing otherwise.

(a) Compute $\operatorname{VaR}_{0.95}$ and $\operatorname{ES}_{0.95}$ for one asset.
(b) Compute both for the equally weighted portfolio of the three.
(c) Check subadditivity for VaR and for ES, and comment.

**19.** *(§7.2)* A probability $p = 0.02$ must be estimated with a 10 % relative standard error.

(a) Derive the required sample size.
(b) Compute it for $p = 0.02$ and for $p = 0.2$.
(c) Explain why the requirement is much harsher for the smaller probability.

**20.** *(§7.11)* For geometric Brownian motion with $S_0 = 100$, $\mu = 0.1$, $\sigma = 0.2$ and one Euler–Maruyama step to $T = 1$ with $Z_1 = 0$, compute the simulated terminal value, and the exact value for the same Brownian path. Comment.

**21.** *(§7.13)* A 95 % VaR model produced 15 exceedances in 250 days.

(a) Compute the Kupiec likelihood-ratio statistic and its p-value.
(b) State the conclusion at the 5 % level.
(c) Explain what the test does not detect.

**22.** *(§7.9)* A biased random walk has $p = 0.52$ and barriers at 0 and 40, starting from 20.

(a) Compute the exact probability of reaching 40 before 0.
(b) Compute the diffusion approximation with $\mu = 2p-1$ and $\sigma^2 = 4pq$.
(c) Comment on the quality of the approximation and on what it depends.

## Advanced

**23.** *(§8.1, §8.2)* Prove the weak law of large numbers for i.i.d. variables with finite variance, and explain what the central limit theorem adds. Then state precisely what the law does *not* say about a simulation whose model is wrong.

**24.** *(§8.3)* Prove the antithetic variance identity and the covariance inequality for monotone $f$, and deduce when antithetic sampling cannot help.

**25.** *(§8.5)* Prove the inverse transform theorem for the generalised inverse, including the case of a distribution with jumps. Use it to justify the discrete inverse transform of Exercise 2.

**26.** *(§8.6)* Prove that rejection sampling produces draws from the target density and that the acceptance probability is $1/M$. Then explain why the method degrades in high dimensions.

**27.** *(§8.12)* Using the Rockafellar–Uryasev representation, prove that expected shortfall is subadditive. Then prove that VaR is not subadditive by the three-asset construction of Exercise 18, computing the exact threshold on $p$ at which the violation appears.

**28.** *(§8.7)* Derive the stationary distribution of the M/M/1 queue from the balance equations, prove that it exists if and only if $\rho < 1$, and derive $L$, $L_q$, $W$ and $W_q$.

**29.** *(§7.8)* Prove Little's law for a single sample path, stating the hypotheses and showing where the boundary terms enter. Explain why the law fails during a transient.

**30.** *(§8.10)* Using Itô's lemma, solve $dS_t = \mu S_t\,dt + \sigma S_t\,dW_t$ and compute $\mathbb{E}[S_t]$ and $\operatorname{Var}(S_t)$. Explain why the median grows at rate $\mu - \sigma^2/2$ and the mean at rate $\mu$.

**31.** *(§8.12)* Prove the Rockafellar–Uryasev representation, that the minimiser is a VaR, and that $\operatorname{ES}_\alpha \ge \operatorname{VaR}_\alpha$. Verify both statements on the normal case of Exercise 9.

## Challenge

**32.** *(§7.3, §8.2)* Let $X_t$ be a stationary AR(1) process, $X_t = \rho X_{t-1} + \varepsilon_t$ with $|\rho| < 1$ and i.i.d. noise of variance $\sigma_\varepsilon^2$.

(a) Compute $\operatorname{Var}(X_t)$ and the autocorrelations $\rho_k$.
(b) Prove that $\operatorname{Var}(\bar X_n) \approx \frac{\sigma^2}{n}\cdot\frac{1+\rho}{1-\rho}$ for large $n$, where $\sigma^2 = \operatorname{Var}(X_t)$.
(c) Compute the inflation factor for $\rho = 0.9$ and say what it implies for a simulation whose output is autocorrelated.

**33.** *(§8.4)* Let $X \sim \mathrm{Exp}(1)$ and estimate $\theta = \mathbb{E}[1] = 1$ using the proposal $q(x) = 2e^{-2x}$.

(a) Show that the estimator is unbiased.
(b) Show that its variance is infinite.
(c) Explain why a pilot run would not reveal the problem, and what diagnostic would.

**34.** *(§7.3)* Let $X$ have a Pareto tail, $\Pr(X > x) = x^{-\alpha}$ for $x \ge 1$, with $1 < \alpha < 2$.

(a) Show that $\mathbb{E}[X] < \infty$ but $\operatorname{Var}(X) = \infty$.
(b) Explain why the central limit theorem does not apply to the sample mean.
(c) State the correct scaling of the sample mean, and compute it for $\alpha = 1.5$.
(d) Explain the practical consequence for estimating the mean of a heavy-tailed loss by simulation.

**35.** *(§7.2, §7.5)* You must estimate $p = \Pr(\text{loss} > 0) = 10^{-6}$ with a 10 % relative standard error, and one simulated path costs one unit of time.

(a) Compute the number of paths needed by brute force.
(b) Design an importance sampling scheme, state the achievable relative standard error per path, and compute the number of paths needed.
(c) Compare the two budgets, and list the assumptions that make your comparison optimistic.

**36.** *(§7.13)* A report states: "We simulated 1000 paths using seed 42. The mean cost was €4.2 m with a standard deviation of €1.1 m, so the expected cost is €4.2 m." Identify every error and omission, and rewrite the sentence as a correct report.

**37.** *(§7.13)* A colleague proposes to validate a queueing model by checking that the simulated average queue length equals the observed average to within 1 %. Explain, using the standard error and the notion of power, why this may be uninformative, and propose a better validation design.

**38.** *(§7.12)* A risk report quotes a 99 % VaR of €4.2 m estimated from 250 daily observations, with no other information. List the questions you would ask before using the number, and explain what each reveals.

**39.** *(§7.11, §7.13)* Design a convergence study for a simulation of a stochastic differential equation. Specify the grid sizes, the number of paths per grid, the quantities to compare, and the decision rule that distinguishes discretisation bias from Monte Carlo error.

**40.** *(§7.1, §7.13)* A deterministic model and a stochastic model of the same system disagree about the mean cost by 20 %. Give three possible reasons consistent with both models being correctly implemented, and say what data would distinguish them.
