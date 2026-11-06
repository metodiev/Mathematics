# Law of Large Numbers and the Central Limit Theorem — Exercises

> [Law of Large Numbers and the Central Limit Theorem](README.md) · 36 problems · Beginner → Challenge · Solutions: [solutions.md](solutions.md)

Work through the problems in order. Every problem is solvable with the definitions and theorems of the
tutorial, and the section reference tells you where to look. Do not consult [solutions.md](solutions.md)
until you have written an attempt.

**Conventions.** $X_1,X_2,\dots$ are random variables on one probability space unless stated otherwise;
$S_n=X_1+\cdots+X_n$ and $\bar X_n=S_n/n$. "i.i.d." means independent and identically distributed.
$\Phi$ is the standard normal CDF, $\phi$ its density, and $z_{0.975}=1.96$. Dice are fair and
independent. Numerical answers should be given to four significant figures.

## Beginner

**1.** *(§5.1–5.3)* For each statement, name the mode of convergence it expresses (in probability, almost
surely, or in distribution), and say whether the statement as written is correct.

(a) For every $\varepsilon>0$, $\Pr(\lvert X_n-X\rvert>\varepsilon)\to0$.
(b) $\Pr\bigl(\lim_{n\to\infty}X_n=X\bigr)=1$.
(c) $F_n(x)\to F(x)$ for every $x\in\mathbb{R}$.
(d) $\mathbb{E}[f(X_n)]\to\mathbb{E}[f(X)]$ for every bounded continuous $f$.

**2.** *(§7.2)* A fair die is rolled $n=2000$ times and $\bar X_n$ is the average.

(a) State $\mu$ and $\sigma^{2}$ for one roll.
(b) Use Chebyshev to bound $\Pr(\lvert\bar X_n-3.5\rvert\ge0.3)$.
(c) What does the bound become for $n=8000$?

**3.** *(§7.6)* Let $S\sim\operatorname{Bin}(64,\tfrac12)$. Compute $\Pr(S\le40)$

(a) with the continuity correction;
(b) without the continuity correction;
(c) exactly, and compare the two errors.

**4.** *(§7.6)* Let $S\sim\operatorname{Bin}(50,0.4)$. Compute $\Pr(S\ge25)$

(a) with the continuity correction;
(b) without it;
(c) exactly, and say which approximation is better and by what factor.

**5.** *(§7.6)* A fair coin is tossed $n$ times and $\hat p_n$ is the proportion of heads.

(a) State the De Moivre–Laplace theorem for $\hat p_n$.
(b) Find the smallest $n$ for which the $95\%$ margin of error is at most $0.01$.
(c) Repeat for a margin of $0.05$.

**6.** *(§5.4, §8.2)* A population has standard deviation $\sigma=5$. A sample of $n=400$ is averaged.

(a) Give the standard error of $\bar X_n$.
(b) Approximate $\Pr(\lvert\bar X_n-\mu\rvert\le0.5)$.
(c) How large must $n$ be to halve the standard error?

**7.** *(§7.8)* Which of the following satisfy the hypotheses of the central limit theorem (i.i.d. sums,
finite positive variance)? Justify each answer briefly.

(a) Bernoulli$(0.3)$; (b) $\operatorname{Pois}(4)$; (c) standard Cauchy; (d) Pareto with tail exponent
$\alpha=1.5$; (e) uniform on $[0,1]$; (f) $X_n$ taking the values $\pm2^{n}$ with probability $\tfrac12$
each.

**8.** *(§7.2, §7.6)* A fair die is rolled $n=100$ times.

(a) Bound $\Pr(\lvert\bar X_n-3.5\rvert\ge0.1)$ by Chebyshev, and comment on the answer.
(b) Estimate the same probability with the CLT.
(c) Explain in one sentence why the two differ so much.

**9.** *(§5.4, §7.9)* Let $X_i\sim\operatorname{Exp}(2)$ be i.i.d. and $n=25$.

(a) State the mean and variance of one $X_i$.
(b) Give the standard error of $\bar X_n$.
(c) Use the CLT to estimate $\Pr(\bar X_{25}\le0.6)$.

**10.** *(§7.1)* Let $X_n=1/n$ for every $\omega$ (a deterministic sequence).

(a) Show $X_n\to0$ in probability, almost surely and in distribution.
(b) What is the limiting distribution?
(c) Does the same hold for $X_n=n$? Explain.

**11.** *(§7.6)* Forty-eight dice are rolled and $S$ is the total. Use the CLT with the continuity
correction to estimate $\Pr(S\ge200)$.

## Intermediate

**12.** *(§7.6)* For $S\sim\operatorname{Bin}(100,\tfrac12)$, compute $\Pr(40\le S\le60)$ by the exact
binomial, with the continuity correction, and without it. Compare the two errors and explain why the
correction helps much less here than for the interval $[45,55]$ of Example 9.2.

**13.** *(§7.8)* Let $X_i\sim\operatorname{Exp}(1)$ be i.i.d.

(a) Estimate $\Pr(\bar X_{100}\le1.2)$ by the CLT, and compare with the exact value $0.97214$.
(b) Repeat for $n=400$, where the exact value is $0.999921$.
(c) By what factor does the CLT error decrease from $n=100$ to $n=400$, and does that match Berry–Esseen?

**14.** *(§7.1)* Let $X$ take the values $+1$ and $-1$ with probability $\tfrac12$ each, and set $X_n=-X$
for every $n$.

(a) Show $X_n\xrightarrow{d}X$.
(b) Show $X_n$ does not converge to $X$ in probability.
(c) To what does $X_n$ converge in probability?

**15.** *(§7.1, Theorem 7.5)* Prove that $X_n\xrightarrow{p}X$ if and only if every subsequence
$(X_{n_k})$ has a further subsequence converging almost surely to $X$.

**16.** *(§7.2, §7.8)* Let $X_i$ have the Pareto density $f(x)=\alpha x^{-\alpha-1}$ for $x\ge1$, with
$\alpha=\tfrac32$.

(a) Compute $\mathbb{E}[X_i]$ and show $\operatorname{Var}(X_i)=\infty$.
(b) Does the weak law of large numbers hold? Which theorem applies?
(c) Explain why the Chebyshev proof of §7.2 gives no information here.

**17.** *(§7.7)* Let $X_i\sim\text{Bernoulli}(0.1)$ and $n=100$. Compute the third absolute central
moment $\rho$, then the Berry–Esseen bound for the supremum error of $Z_n$.

**18.** *(§7.9)* A Monte Carlo estimator has $\sigma=2$ for a single sample.

(a) How many samples give a standard error of $0.05$?
(b) How many give a $95\%$ confidence interval of half-width $0.1$?
(c) If the cost of one sample doubles, how much larger must $n$ be for the same accuracy, and what does
that say about variance reduction?

**19.** *(§7.6)* For $S\sim\operatorname{Bin}(n,p)$ and a value $k<np$, the continuity correction replaces
$(k-np)/\sqrt{npq}$ by $(k+\tfrac12-np)/\sqrt{npq}$.

(a) Does this increase or decrease the approximated value of $\Pr(S\le k)$?
(b) Explain geometrically why, using the bar of width $1$ centred at $k$.
(c) For $k>np$, which direction does the correction go, and does that agree with (a)?

**20.** *(§7.8)* Let $X$ be uniform on $\{0,2\}$ and $S=\sum_{i\le10}X_i$.

(a) Compute $\Pr(S=10)$ exactly.
(b) Approximate it with the continuity correction of width $1$.
(c) Approximate it with the correct span $2$, i.e. report $\frac{2}{\sigma\sqrt n}\phi(z)$, and explain the
discrepancy.

**21.** *(§7.8)* Let $Y_1,Y_2,\dots$ have variance $\sigma^{2}=1$ and correlation $\rho=0.5$ between every
pair of distinct variables, so $\operatorname{Cov}(Y_i,Y_j)=\rho$ for $i\ne j$.

(a) Show $\operatorname{Var}(\bar Y_n)=\frac{1}{n}+\bigl(1-\frac1n\bigr)\rho$.
(b) Evaluate at $n=100$ and give the limit as $n\to\infty$.
(c) What does this say about the law of large numbers for such data?

**22.** *(§7.1)* Prove that the probability limit is unique: if $X_n\xrightarrow{p}X$ and
$X_n\xrightarrow{p}Y$ then $\Pr(X=Y)=1$.

**23.** *(§7.4)* Show that the Lindeberg condition holds automatically for i.i.d. variables with
$0<\sigma^{2}<\infty$.

## Advanced

**24.** *(§7.2)* Prove the weak law under the weaker hypothesis that the $X_i$ are pairwise uncorrelated
with $\mathbb{E}[X_i]=\mu$ and $\operatorname{Var}(X_i)\le\sigma^{2}$ for all $i$ (no identical
distribution assumed).

**25.** *(§7.3)* Prove the strong law of large numbers under the hypothesis $\mathbb{E}[X_1^{4}]<\infty$
and $\mathbb{E}[X_1]=\mu$, including the reduction to the centred case and the application of
Borel–Cantelli. (This is the finite fourth-moment case of Theorem 5.7.)

**26.** *(§7.4, Slutsky)* Let $X_n\xrightarrow{d}X$ and $Y_n\xrightarrow{p}c$ for a constant $c$. Prove
$X_n+Y_n\xrightarrow{d}X+c$. Where exactly does the hypothesis that the limit of $Y_n$ is a constant get
used?

**27.** *(§7.3, portmanteau)*

(a) Prove: if $X_n\xrightarrow{d}X$ then $\mathbb{E}[f(X_n)]\to\mathbb{E}[f(X)]$ for every bounded
uniformly continuous $f$.
(b) Show that boundedness cannot be dropped: find $X_n\xrightarrow{d}0$ and an unbounded continuous $f$
with $\mathbb{E}[f(X_n)]\not\to f(0)$. (Boundedness itself is not the issue — bounded continuous $f$ works
too, by the portmanteau theorem.)

**28.** *(§7.6, local limit)* Let $S_n\sim\operatorname{Bin}(n,p)$ and fix a value $z$ with
$k_n=np+z\sqrt{npq}$ an integer. Using Stirling's formula $m!\sim\sqrt{2\pi m}(m/e)^{m}$, prove

$$\Pr(S_n=k_n)\sim\frac{1}{\sqrt{2\pi npq}}e^{-z^{2}/2}.$$

**29.** *(§7.1, moments)* Let $X_n$ take the value $n$ with probability $1/n$ and $0$ otherwise.

(a) Show $X_n\xrightarrow{p}0$ and $X_n\xrightarrow{d}0$.
(b) Show $\mathbb{E}[X_n]=1$ for every $n$, so no moments converge.
(c) Which theorem would have to be added to the CLT framework to conclude $\mathbb{E}[X_n]\to0$, and why
does it fail here?

**30.** *(§7.4, delta method)* Let $\bar X_n$ be a sample mean with $\mathbb{E}[X_1]=\mu$,
$\operatorname{Var}(X_1)=\sigma^{2}$, and let $g$ be differentiable at $\mu$ with $g'(\mu)\ne0$. Prove

$$\sqrt n\bigl(g(\bar X_n)-g(\mu)\bigr)\xrightarrow{d}\mathcal{N}\bigl(0,\sigma^{2}g'(\mu)^{2}\bigr),$$

stating clearly where Taylor's theorem and Slutsky's theorem enter.

**31.** *(§7.4, §7.8)*

(a) Show that if the CLT holds for i.i.d. $X_i$ then the weak law holds.
(b) Give an example of i.i.d. variables for which the weak law holds but the CLT does not, with a proof.
(c) What does (b) show about the logical relation between the two theorems?

## Challenge

**32.** *(§7.7)* Let $X_i$ be Bernoulli$(\tfrac12)$ and $Z_n$ the standardised sum.

(a) For $n=2m$, show $F_{Z_n}(0)-\Phi(0)=\tfrac12\Pr(S_n=m)$.
(b) Using $\binom{2m}{m}4^{-m}\sim\frac{1}{\sqrt{\pi m}}$, show the supremum error is at least
$\frac{1}{2\sqrt{\pi m}}\sim\frac{0.3989}{\sqrt n}$.
(c) Conclude that the $1/\sqrt n$ rate in Berry–Esseen cannot be improved.

**33.** *(§7.8)* Let $X_i$ be i.i.d. standard Cauchy, with characteristic function
$\varphi(t)=\mathbb{E}[e^{itX}]=e^{-\lvert t\rvert}$.

(a) Show that $\bar X_n$ has characteristic function $e^{-\lvert t\rvert}$.
(b) Conclude that $\bar X_n$ is standard Cauchy for every $n$, so the weak law fails.
(c) Explain what the "limit" of the normalised sums $(S_n-n\mu)/(\sigma\sqrt n)$ would be if $\sigma$ were
finite, and why no such rescaling exists here.

**34.** *(§7.6, Poisson's law of rare events)* Let $S_n\sim\operatorname{Bin}(n,\lambda/n)$ with $\lambda>0$
fixed.

(a) Show $\Pr(S_n=k)\to e^{-\lambda}\lambda^{k}/k!$ for each fixed $k$.
(b) Show that $\Pr(S_n=0)\to e^{-\lambda}$, and reconcile this with the normal approximation, whose
standard deviation is $\sqrt{\lambda(1-\lambda/n)}\to\sqrt\lambda$, bounded.
(c) Explain why the CLT does not contradict the Poisson limit.

**35.** *(§7.2, §7.4, coupon collector)* Let $T_n$ be the time to collect all $n$ coupons, written as a
sum of independent geometric variables $G_j$ with success probability $j/n$, $j=1,\dots,n$.

(a) Show $\operatorname{Var}(T_n)=n^{2}\sum_{j=1}^{n}\frac{1}{j^{2}}-n\sum_{j=1}^{n}\frac1j$, and deduce
$\operatorname{Var}(T_n)\sim\frac{\pi^{2}}{6}n^{2}$.
(b) Show that the largest summand, $G_1$, has variance $n(n-1)$, comparable to the total, so the
Lindeberg condition fails.
(c) Explain why $(T_n-nH_n)/n$ has a non-normal limit, and why the CLT nevertheless gives a good
approximation when $n$ is small but not when $n$ is large.

**36.** *(§7.1)* A simulation estimates $p=\Pr(\lvert Z\rvert\le1)=0.6827$ for $Z\sim\mathcal{N}(0,1)$ by
simulating $N$ independent standardised sums $Z^{(1)},\dots,Z^{(N)}$ and recording the fraction inside
$[-1,1]$.

(a) Give the standard error of the estimated fraction as a function of $N$.
(b) Find the smallest $N$ that makes the standard error at most $0.005$.
(c) If the simulated $Z^{(i)}$ are only approximately normal, does the estimate of $p$ remain consistent
as $N\to\infty$? Explain which limit theorem is doing the work.
