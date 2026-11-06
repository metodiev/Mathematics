# Epidemic Models — Exercises

> [Epidemic Models](README.md) · 36 problems · Beginner → Challenge · Solutions: [solutions.md](solutions.md)

Work through the problems in order. Every problem is solvable with the definitions and theorems of the
tutorial, and the section reference tells you where to look. Attempt each problem in writing before
consulting [solutions.md](solutions.md).

**Conventions.** Time is measured in days unless a problem says otherwise. $R_0$ is the basic
reproduction number, $r$ the intrinsic growth rate of the early exponential phase, $T_d = \ln 2/r$ the
doubling time, and $z$ the final size. Populations are closed and homogeneously mixed unless stated.
Give numerical answers to four decimal places unless an exact value is requested.

## Beginner

**1.** *(§7.3, §7.8)* An infection has transmission rate $\beta = 0.8$ per day and removal rate
$\gamma = 0.25$ per day.

(a) Compute $R_0$ and the mean infectious period.
(b) Compute the early growth rate $r$ and the doubling time.
(c) If an infectious person has $10$ close contacts per day, what is the transmission probability per
    contact?

**2.** *(§7.3)* An infection has $R_0 = 4$ and a mean infectious period of $7$ days.

(a) Compute $\beta$.
(b) If contacts occur at rate $c = 10$ per day, compute the per-contact transmission probability.
(c) What happens to $R_0$ if the infectious period is halved and $\beta$ is unchanged?

**3.** *(§7.2)* For the SIR model of Definition 5.1:

(a) Show that $S+I+R$ is constant.
(b) Show that the faces $S=0$, $I=0$ and $R=0$ of the simplex are invariant, and explain why this makes
    the simplex positively invariant.
(c) Explain why the right-hand side is smooth enough for the existence–uniqueness theorem to apply.

**4.** *(§7.5)* Compute the herd immunity threshold $1-1/R_0$ for $R_0 = 2$, $4$, $8$ and $16$. Describe
the pattern and explain why the thresholds approach $1$.

**5.** *(§7.4)* Solve the final-size equation $1-z = e^{-R_0z}$ by bisection for

(a) $R_0 = 1.5$; (b) $R_0 = 4$.

In each case show at least two function evaluations that bracket the root, and interpret the answer.

**6.** *(§7.4)* Compute the peak height $I_{\text{peak}}/N = 1-(1+\ln R_0)/R_0$ for $R_0 = 2$ and
$R_0 = 4$, and compare with the herd immunity thresholds for the same values.

**7.** *(§7.7, §7.6)* For each scenario, state which of SIR, SEIR or SIS is the most appropriate first
model, and why.

(a) An infection with lifelong immunity and a two-day latent period.
(b) An infection with no immunity after recovery and no latent period.
(c) An infection with lifelong immunity and no latent period.
(d) An infection that confers immunity for about six months.

**8.** *(§7.2)* In the SIR model with $R_0 = 2$, $S_0 = N$ and $I_0\to0$, use the first integral

$$I + S - \frac{N}{R_0}\ln S = \text{constant}$$
to compute $I/N$ when $S = 0.8N$. Is the epidemic still growing at that moment?

**9.** *(§7.3)* An infection has $R_0 = 3$. Compute the effective reproduction number when the
susceptible fraction is $0.4$ and when it is $0.3$. In which case is the epidemic growing?

**10.** *(§7.5)* An infection has $R_0 = 2.5$.

(a) Compute the herd immunity threshold.
(b) Compute the coverage needed with a vaccine of efficacy $0.8$.
(c) Compute the minimum efficacy needed for elimination with full coverage.

**11.** *(§7.10)* For a branching process with Poisson offspring of mean $R_0$, the extinction
probability $q$ satisfies $q = e^{-R_0(1-q)}$. Compute $q$ for $R_0 = 1.5$ and for $R_0 = 2.5$, and
interpret both numbers.

**12.** *(§7.1–7.4)* Decide whether each statement is true or false, and correct the false ones.

(a) $R_0$ is a property of the pathogen.
(b) A disease with $R_0 = 2$ infects exactly half the population.
(c) If $R_0 < 1$ an introduced case cannot cause any secondary infections.
(d) The herd immunity threshold is the fraction ever infected.
(e) The epidemic ends when the susceptible pool is depleted below $N/R_0$.
(f) $R_0$ and the growth rate $r$ carry the same information.

## Intermediate

**13.** *(§7.4)* Derive the final-size equation from the SIR equations. Start from
$\dfrac{dI}{dS} = -1 + \dfrac{N}{R_0S}$, integrate from $t=0$ to $t=\infty$, and state every
assumption used (including what happens to $I(\infty)$).

**14.** *(§7.4)* Derive the peak-height formula

$$\frac{I_{\text{peak}}}{N} = 1 - \frac{1+\ln R_0}{R_0}$$
from the first integral, stating clearly why the maximum occurs at $S = N/R_0$.

**15.** *(§7.6)* An SEIR model has $\beta = 0.5$ per day, $\sigma = 0.25$ per day and $\gamma = 0.1$ per
day.

(a) Compute $R_0$ by the next-generation matrix.
(b) Solve the characteristic equation $(r+\sigma)(r+\gamma) = \sigma\beta$ for the growth rate $r$, and
    identify the positive root.
(c) Interpret the negative root.

**16.** *(§7.8)* An outbreak doubles every three days. The mean latent period is two days and the mean
infectious period is five days.

(a) Compute $r$.
(b) Compute $R_0$ under the SEIR model.
(c) Compute the $R_0$ that an SIR fit to the same data would produce, and the size of the error.

**17.** *(§7.7)* An SIS infection has $R_0 = 4$, $\gamma = 0.1$ per day and $\mu = 1/3650$ per day.

(a) Compute $\beta$.
(b) Compute the endemic equilibrium $S^{*}/N$ and $I^{*}/N$.
(c) Comment on whether the demographic term matters numerically here.

**18.** *(§7.7)* In the SIS model without demography the prevalence obeys the logistic equation

$$I' = \gamma(R_0-1)\,I\left(1-\frac{I}{I^{*}}\right), \qquad I^{*} = N\left(1-\frac{1}{R_0}\right).$$
Take $R_0 = 2$, $\gamma = 0.1$ per day, $I(0) = 0.01N$ and compute the time at which the prevalence
reaches $0.25N$.

**19.** *(§7.5)* An infection has $R_0 = 5$ and the vaccine has efficacy $0.85$.

(a) Compute the critical coverage.
(b) Compute the coverage needed if the vaccine were perfect.
(c) Explain why the imperfect vaccine makes elimination much harder but not impossible.

**20.** *(§7.10)* A country receives $20$ independent introductions of an infection with $R_0 = 3$ and
Poisson offspring. Using $q = 0.0595$, compute the probability of at least one major outbreak, and
comment on the result.

**21.** *(§7.8)* Reported cases at five-day intervals are $100$, $150$, $225$ and $337.5$.

(a) Verify that the growth is exponential and compute $r$.
(b) Convert to $R_0$ assuming an infectious period of $5$ days.
(c) Convert again assuming $8$ days, and comment on the difference.

**22.** *(§7.4)* A population has $50\%$ pre-existing immunity ($s_0 = 0.5$) and the infection has
$R_0 = 4$. Solve $s_\infty = s_0e^{-R_0(s_0-s_\infty)}$ by bisection and compute the final size $z$.
Compare with the fully susceptible case.

## Advanced

**23.** *(§7.6)* Derive the next-generation matrix for the SEIR model in full: write $\mathcal{F}$ and
$\mathcal{V}$, compute $FV^{-1}$, find its eigenvalues, and conclude $R_0 = \beta/\gamma$. Explain why
$\sigma$ does not appear in the answer.

**24.** *(§7.4)* Prove Theorem 7.2: the equation $1-z-e^{-R_0z}=0$ has a root in $(0,1)$ if and only if
$R_0>1$, and that root is unique. Your proof must use concavity and must explain why the trivial root
$z=0$ does not count.

**25.** *(§7.2)* Prove that in the SIR model $S(t)$ is non-increasing, that $I(t)$ has at most one
interior maximum, and that $I(t)\to0$ as $t\to\infty$. State the monotone convergence theorem you use.

**26.** *(§7.4)* Prove that $S_\infty > 0$ for every finite $R_0$, and that $S_\infty$ is a strictly
decreasing function of $R_0$. (You may use the final-size equation and the implicit function theorem.)

**27.** *(§7.7)* Analyse the SIS model without demography completely: find all equilibria, prove the
global stability of $I=0$ when $R_0\le1$, prove the global stability of $I^{*}>0$ when $R_0>1$, and
describe the bifurcation at $R_0=1$.

**28.** *(§7.8)* Derive the Euler–Lotka relation

$$1 = R_0\int_0^\infty e^{-r\tau}w(\tau)\,d\tau$$
for a general generation-time density $w$, by summing the expected infections over generations. Verify it
for the SIR model with $w(\tau) = \gamma e^{-\gamma\tau}$.

**29.** *(§7.6)* Show that the SEIR model has exactly the same final-size equation as the SIR model with
the same $R_0$ and $\gamma$. Explain which structural feature of both models the argument uses, and give
an example of a modification that would break the equality.

**30.** *(§7.3)* State and prove the threshold theorem for the SIR model directly, without quoting the
next-generation theorem: show that the disease-free equilibrium is locally asymptotically stable if and
only if $R_0<1$, by linearising the two-dimensional system at $(N,0)$ and computing the eigenvalues.

## Challenge

**31.** *(§7.10)* Derive the extinction probability of a branching process: let $G$ be the probability
generating function of the offspring distribution with mean $R_0$. Prove that the extinction probability
$q$ is the smallest fixed point of $G$ in $[0,1]$, and that $q<1$ if and only if $R_0>1$ and
$\Pr(X\ge2)>0$.

**32.** *(§7.10)* Compute the extinction probability for a geometric offspring distribution with mean
$R_0$, and compare with the Poisson case at $R_0 = 2$. Explain why the two differ even though the means
agree, and state which modelling assumption is doing the work.

**33.** *(§7.12)* A newspaper reports: "Scientists' model predicts 500,000 deaths by December unless
nothing changes." The model's report says: "In the absence of additional interventions, and assuming
constant contact rates, cumulative deaths reach 500,000 (95% interval 200,000–900,000) by December."

(a) Identify at least four errors or elisions in the newspaper sentence.
(b) Rewrite the sentence correctly in one sentence.
(c) Explain why the interval is not a prediction interval for the actual outcome.

**34.** *(§7.5)* A fraction $p$ of the population is vaccinated before an epidemic starts, with an
all-or-nothing vaccine of efficacy $\varepsilon$. Derive the final-size equation in the form

$$s_\infty = (1-\varepsilon p)\,e^{-R_0(s_0-s_\infty)}, \qquad s_0 = 1-\varepsilon p,$$
and determine the smallest $p$ that prevents any epidemic at all (that is, makes $z=0$ the only
solution). Compare with the formula $p_c = (1-1/R_0)/\varepsilon$.

**35.** *(§7.3, §7.9)* Consider a population split into two groups with next-generation matrix

$$K = \begin{pmatrix} 2 & 1 \\ 1 & 0.5 \end{pmatrix}.$$

(a) Compute $R_0 = \rho(K)$.
(b) Compute the eigenvector for the dominant eigenvalue and interpret it.
(c) Explain why the group with the higher internal transmission dominates the value of $R_0$, and what
    this implies for targeting interventions.

**36.** *(§7.2, §7.12)* The SIR model is often criticised for predicting that an epidemic ends with a
positive fraction of susceptibles. Using the final-size equation and the orbit relation, explain why
this is a *consequence of the model's assumptions* rather than a defect, and explain what modification
would allow an epidemic to infect the entire population.
