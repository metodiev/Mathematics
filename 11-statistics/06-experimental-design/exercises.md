# Experimental Design — Exercises

> [Experimental Design](README.md) · 36 problems · Beginner → Challenge · Solutions: [solutions.md](solutions.md)

Attempt each problem in writing before consulting [solutions.md](solutions.md). The problems are grouped by
level but numbered continuously; the section of the tutorial tested is given in italics.

**Conventions.** $T_i=1$ means unit $i$ was assigned to treatment. Outcomes are coded so that larger is better
unless stated. Critical values: $z_{0.975}=1.960$, $z_{0.95}=1.645$, $z_{0.90}=1.2816$, $z_{0.80}=0.8416$;
$t_{8}=2.306$, $t_{17}=2.110$; $\chi^2_{2,0.95}=5.991$, $\chi^2_{3,0.95}=7.815$. Keep full precision and
round final answers to four significant figures.

## Beginner

**1.** *(§7.1)* Classify each statement as (i) purely associational, (ii) causal, or (iii) ambiguous, and for
each causal claim name what evidence would be needed to support it.

(a) "Children who eat breakfast score higher on tests."
(b) "Assigning classrooms to a smaller class size raises test scores."
(c) "Smoking causes lung cancer."
(d) "Among patients admitted to intensive care, those with lower blood pressure die more often."
(e) "Rainfall is associated with higher crop yields."

**2.** *(§5.1)* For each study identify the units, the treatments, the outcome, and any factor with its
levels.

(a) A agronomist divides a field into $40$ plots, applies one of four fertiliser blends at random to each,
and records yield.
(b) A hospital randomly assigns patients to a new surgical technique or the standard one, and records
complications within $30$ days.
(c) A software firm randomly shows users one of three page layouts and records whether they subscribe.

**3.** *(§5.5)* Count the assignments.

(a) Eight units, four assigned to treatment, complete randomisation. How many distinct assignments exist?
(b) Six units, three treated. How many?
(c) Ten units paired into five pairs. In how many ways can the pairs be formed?

**4.** *(§7.2)* A trial reports blood-pressure reduction of $6.2$ mmHg in the treated group ($n=120$) and
$2.1$ mmHg in the control group ($n=118$).

(a) Compute the difference in means.
(b) Write the result as a complete sentence naming the estimand.
(c) Name two things the sentence leaves unspecified.

**5.** *(§7.7)* A $2^2$ factorial (temperature low/high; catalyst absent/present) gives cell means
$18$, $22$, $20$, $28$ in the order $(00),(10),(01),(11)$.

(a) Compute the main effect of temperature.
(b) Compute the main effect of catalyst.
(c) Compute the interaction.
(d) Interpret the interaction in one sentence.

**6.** *(§7.4)* Name a plausible confounder for each comparison.

(a) People who take vitamin supplements versus those who do not, comparing mortality.
(b) Hospitals with more nurses versus hospitals with fewer, comparing patient survival.
(c) Students at selective schools versus comprehensive schools, comparing examination results.
(d) Countries with higher chocolate consumption versus lower, comparing Nobel prizes per capita.

**7.** *(§7.6)* An experiment compares three diets using $48$ animals housed in $8$ cages of $6$ animals each.

(a) Suggest a blocking variable and explain why it helps.
(b) If the design is a randomised block design with $8$ blocks, state the degrees of freedom for treatments,
blocks and error.
(c) Explain why randomising *within* cages matters even if all animals in a cage get the same diet.

**8.** *(§7.2)* For six units, $Y(1)=(12,9,7,5,4,3)$ and $Y(0)=(4,4,5,2,3,1)$.

(a) Compute the individual effects and the SATE.
(b) Suppose units $1,2,3$ were treated. Compute $\bar Y_T$, $\bar Y_C$ and the naive estimate.
(c) Compute the selection-bias terms $b_T$ and $b_C$ and verify that the naive estimate equals
$\text{SATE}+b_T-b_C$.

**9.** *(§7.9)* For each study say what should be blinded and how, or explain why blinding is impossible.

(a) A trial of a new tablet against placebo.
(b) A trial of physiotherapy versus advice.
(c) A trial of surgery versus medical management.

**10.** *(§7.8)* A trial is planned with $\sigma=12$, a difference worth detecting of $\Delta=4$, $\alpha=0.05$
two-sided and power $0.90$.

(a) Compute the number needed per group using the normal approximation.
(b) Recompute if $15\%$ of participants are expected to drop out.
(c) By what factor does $n$ change if $\Delta$ is halved to $2$?

**11.** *(§7.11)* A study reports:

| Stratum | Treatment A | Treatment B |
|---|---|---|
| Low risk | $9/10=90\%$ | $80/100=80\%$ |
| High risk | $40/90=44.4\%$ | $20/100=20\%$ |

(a) Compute the marginal success rate for each treatment.
(b) Compute each treatment's rate in each stratum.
(c) Explain how the marginal comparison and the stratified comparisons can disagree.
(d) Standardise both treatments to the pooled stratum sizes ($110$ low risk, $190$ high risk).

**12.** *(§8.8)* In a cohort, $45$ of $150$ exposed and $30$ of $140$ unexposed subjects develop the outcome.

(a) Compute the risk in each group.
(b) Compute the risk difference and the relative risk.
(c) State which measure answers "how many extra cases per $1000$ exposed" and which answers "how many times
more likely".

## Intermediate

**13.** *(§8.2)* Six units with potential outcomes $Y(1)=(5,7,4,9,6,8)$ and $Y(0)=(3,4,4,5,3,6)$, of which
units $1,2,4$ were treated.

(a) Compute the observed difference in means.
(b) Enumerate all $\binom{6}{3}=20$ assignments and compute the difference for each.
(c) Compute the two-sided randomisation $p$-value.
(d) State what this $p$-value means and what the sharp null hypothesis is.

**14.** *(§7.3)* Prove that under complete randomisation with $n_T$ treated units out of $n$,
$\mathbb{E}[\bar Y_T]=\overline{Y(1)}$.

(a) Write $\bar Y_T$ as a sum over units involving $T_i$.
(b) Compute $\Pr(T_i=1)$ and take expectations.
(c) Deduce $\mathbb{E}[\hat\tau]=\text{SATE}$ and state where SUTVA is used.

**15.** *(§7.8)* A two-group trial has $\sigma=10$, $\Delta=5$, $\alpha=0.05$ two-sided.

(a) Compute the power at $n=40$ per group using the normal approximation.
(b) Compute the $n$ needed for power $0.90$.
(c) Explain why the exact $t$ calculation gives a slightly lower power than the normal approximation.

**16.** *(§7.6)* Twenty pairs, within-pair correlation $\rho$, outcome standard deviation $\sigma=12$.

(a) Compute $\operatorname{Var}(\bar d)$ and its standard error for $\rho=0.7$.
(b) Repeat for $\rho=0.2$.
(c) Compare both with the unpaired design using the same $40$ units.
(d) What does the comparison for $\rho=0.2$ imply about careless blocking?

**17.** *(§7.7)* A $2^2$ design has three replicates per cell with totals $T_{00}=60$, $T_{10}=72$,
$T_{01}=66$, $T_{11}=90$, and within-cell sum of squares $\mathrm{SSE}=8$.

(a) Compute the three contrast sums and their sums of squares.
(b) Compute the $F$ statistics and the total sum of squares.
(c) State which effects are material and how they should be reported.

**18.** *(§7.10)* A propensity model is $\operatorname{logit}\Pr(T=1\mid\text{age})=-4+0.08\,\text{age}$.

(a) Compute the propensity score at ages $40$, $60$ and $70$.
(b) Explain what a treated $40$-year-old should be compared with.
(c) Explain why a control aged $70$ has no good match among younger treated units, and what that means for
positivity.

**19.** *(§8.9)* Three studies report $0.50$ (SE $0.20$), $0.30$ (SE $0.10$) and $0.25$ (SE $0.05$).

(a) Compute the inverse-variance weights and the fixed-effect pooled estimate.
(b) Compute its standard error and a $95\%$ interval.
(c) Compute $Q$ and $I^2$ and comment on heterogeneity.

**20.** *(§7.10)* A treated group of three and a control group of five have ages and outcomes:

| Group | ages | outcomes |
|---|---|---|
| Treated | 41, 47, 55 | 71, 68, 64 |
| Control | 39, 46, 54, 60, 66 | 66, 63, 60, 55, 50 |

(a) Compute the crude difference in means.
(b) Match each treated unit to the nearest-age control and compute the matched difference.
(c) Explain why the two answers differ, and which you would report.

**21.** *(§7.8)* A trial finds means $12.4$ and $10.1$ with a pooled standard deviation of $3.2$.

(a) Compute Cohen's $d$.
(b) Classify the size using the conventional small/medium/large labels.
(c) Compute the $n$ per group needed for $80\%$ power at this effect size.

**22.** *(§8.3)* A randomised experiment has $n_T=n_C=50$, $N=100$, with $S_T^2=16$, $S_C^2=9$ and
$S_{TC}^2=4$.

(a) Compute the Neyman variance of $\bar Y_T-\bar Y_C$.
(b) Compute the variance that the usual estimator targets, $\sigma^2(1/n_T+1/n_C)$ with
$\sigma^2=12.5$.
(c) Explain why the usual estimator is conservative here.

**23.** *(§7.2, §11)* A trial randomises $200$ patients, $100$ per arm. In the treated arm, $70$ comply and $30$
do not; $60$ of the $70$ compliers and $10$ of the $30$ non-compliers improve. In the control arm, $40$ of
$100$ improve.

(a) Compute the intention-to-treat difference.
(b) Compute the per-protocol difference using compliers only.
(c) Explain which is the correct primary analysis and why the other is biased.

**24.** *(§7.12)* Classify each variable as confounder, mediator or collider for the effect of $X$ on $Y$.

(a) $Z$ causes both $X$ and $Y$.
(b) $X$ causes $M$ and $M$ causes $Y$.
(c) $X$ and $Y$ both cause $C$.
(d) $Z$ causes $X$, and $Y$ causes $Z$.

## Advanced

**25.** *(§8.4)* Prove that pairing reduces the variance of a difference in means.

(a) Show $\operatorname{Var}(Y_{i1}-Y_{i2})=2\sigma^2(1-\rho)$.
(b) Deduce $\operatorname{Var}(\bar d)=2\sigma^2(1-\rho)/n$ and compare with $2\sigma^2/n$ unpaired.
(c) Show that pairing is beneficial exactly when $\rho>0$, and explain what happens to the degrees of freedom.

**26.** *(§7.12)* Let $X$ and $Y$ be independent Bernoulli$(0.5)$ variables, and let $C=1$ if at least one of
$X,Y$ equals $1$ (a common effect).

(a) Tabulate the joint distribution of $(X,Y)$.
(b) Compute $\Pr(X=1\mid C=1)$, $\Pr(Y=1\mid C=1)$ and $\Pr(X=1,Y=1\mid C=1)$.
(c) Show that $X$ and $Y$ are negatively associated given $C=1$ although they are independent marginally.
(d) Explain the practical warning in one sentence.

**27.** *(§7.12)* Consider the graph $Z\to X$, $Z\to Y$, $X\to M\to Y$.

(a) Apply the backdoor criterion to identify the effect of $X$ on $Y$.
(b) State the adjustment formula and compute it for a two-level $Z$ with the following stratum results:
$Z=0$: $\Pr(Y=1\mid X=1)=0.5$, $\Pr(Y=1\mid X=0)=0.3$, $\Pr(Z=0)=0.4$;
$Z=1$: $\Pr(Y=1\mid X=1)=0.8$, $\Pr(Y=1\mid X=0)=0.7$, $\Pr(Z=1)=0.6$.
(c) Explain why adjusting for $M$ instead would answer a different question.

**28.** *(§8.6)* Derive the sample-size formula for a two-group comparison.

(a) Standardise $\hat\Delta$ and state its distribution under the alternative.
(b) Express the rejection rule at level $\alpha$ in terms of the standardised statistic.
(c) Solve for $n$ with power $1-\beta$ and state the result.

**29.** *(§7.2, §11)* Explain and prove why intention-to-treat estimates the effect of assignment rather than the
effect of treatment.

(a) Write the observed outcome in terms of assignment $T$, actual treatment received $D$, and potential
outcomes.
(b) Show that $\mathbb{E}[\bar Y_T-\bar Y_C]$ equals the average effect of assignment under randomisation.
(c) Explain why per-protocol analysis breaks this argument.

**30.** *(§7.14, §11)* A trial will test five independent outcomes at $\alpha=0.05$ each.

(a) Compute the family-wise error rate if all five null hypotheses are true.
(b) Compute the Bonferroni-adjusted per-test level and the resulting bound on the family-wise error rate.
(c) Explain the loss incurred by the adjustment.

**31.** *(§7.15)* Five studies report effects and standard errors
$(0.10,0.08)$, $(0.90,0.40)$, $(0.05,0.10)$, $(0.60,0.30)$, $(0.15,0.12)$.

(a) Compute the fixed-effect pooled estimate and its standard error.
(b) Compute $Q$ and $I^2$.
(c) Compute $\tau^2$ by DerSimonian–Laird and the random-effects estimate.
(d) Compare the two intervals and explain the difference.

## Challenge

**32.** *(§7.11)* Construct a $2\times2\times2$ table (treatment $\times$ stratum) in which treatment A is
better than B within each of two strata, yet B is better marginally.

(a) Give cell counts and rates satisfying this.
(b) Verify both the stratified and the marginal comparisons numerically.
(c) Standardise to the pooled stratum sizes and comment.
(d) State the condition on the stratum sizes that makes the reversal possible.

**33.** *(§7.12)* A treatment $T$ raises the probability of an intermediate response $M$, which in turn raises
$Y$: $T\to M\to Y$, with no direct effect.

| Group | $\Pr(M=1)$ | $\mathbb{E}[Y\mid M=1]$ | $\mathbb{E}[Y\mid M=0]$ |
|---|---|---|---|
| $T=1$ | $0.7$ | $12$ | $8$ |
| $T=0$ | $0.3$ | $10$ | $6$ |

(a) Compute the average outcome under each treatment and the total effect.
(b) Compute the effect of $T$ within each level of $M$ and the $M$-adjusted effect.
(c) Explain why the adjusted number is not the causal effect of $T$, and name the error.

**34.** *(§7.15)* Four studies report $(0.40,0.10)$, $(0.20,0.20)$, $(0.60,0.15)$ and $(0.30,0.12)$ as
(estimate, standard error).

(a) Compute the fixed-effect estimate, $Q$ and $I^2$.
(b) Compute $\tau^2$ by DerSimonian–Laird and the random-effects weights.
(c) Compute the random-effects estimate and its interval.
(d) Discuss what the difference between the two pooled estimates tells you.

**35.** *(§8.2, §8.3)* Distinguish randomisation inference from superpopulation inference.

(a) For the data of Exercise 13, compute the standard deviation of the randomisation distribution.
(b) Compute the usual two-sample standard error $\sqrt{s_T^2/n_T+s_C^2/n_C}$ using the observed groups.
(c) Explain what each quantity describes, and why they need not agree.
(d) State which inference is available without any model of sampling from a population.

**36.** *(§7.8)* A trial allocates twice as many controls as treated.

(a) Derive $n_T=(1+1/k)\sigma^2(z_{1-\alpha/2}+z_{1-\beta})^2/\Delta^2$ for $n_C=kn_T$.
(b) Compute $n_T$ and $n_C$ for $\Delta=5$, $\sigma=10$, $\alpha=0.05$, power $0.80$ and $k=2$.
(c) Compare the total sample with the equal-allocation design and comment.
