# Hypothesis Testing — Exercises

> [Hypothesis Testing](README.md) · 36 problems · Beginner → Challenge · Solutions: [solutions.md](solutions.md)

Attempt every problem in writing before looking at [solutions.md](solutions.md). Each problem names
the section of the tutorial that supplies the method. Use a calculator or statistical tables for the
normal, $t$ and chi-squared distributions; four significant figures are enough unless the problem says
otherwise. State the assumptions of every test you use, and distinguish clearly between a p-value, a
significance level and an effect size.

Notation: $\Phi$ is the standard normal CDF, $z_{1-\alpha}$ the $1-\alpha$ quantile of $N(0,1)$,
$t_{\nu}$ the $t$ distribution with $\nu$ degrees of freedom, and $\chi^2_\nu$ the chi-squared
distribution with $\nu$ degrees of freedom. "Two-sided" means $H_1:\theta\ne\theta_0$; "one-sided"
means the direction is stated in the problem.

## Beginner

**1.** *(§7.1, §7.2)* For each scenario, state $H_0$ and $H_1$ in terms of a parameter, say whether the
test should be one- or two-sided, and identify the parameter.
(a) A new drug is intended to lower mean blood pressure relative to a placebo.
(b) A filling machine is supposed to put $500$ ml in each bottle; either overfilling or underfilling is
a problem.
(c) A coin is suspected of being biased.
(d) A classifier is claimed to have accuracy above $0.9$.

**2.** *(§4, §7.5)* In the courtroom analogy, identify which error corresponds to a Type I error and
which to a Type II error. What does "beyond reasonable doubt" correspond to statistically? Explain why
"not guilty" is not the same as "innocent", and connect this to "not significant".

**3.** *(§7.5, §7.13)* Let $X\sim\operatorname{Bin}(10,p)$. Test $H_0:p=0.5$ against $H_1:p=0.8$,
rejecting when $X\ge8$.
(a) Compute the Type I error probability $\alpha$.
(b) Compute the Type II error probability $\beta$ and the power at $p=0.8$.
(c) Repeat for the rejection rule $X\ge9$ and compare the two rules.

**4.** *(§7.4, §9.3)* A test statistic has $z_{\text{obs}}=2.00$. Compute the one-sided p-value for
$H_1:\mu>\mu_0$ and the two-sided p-value. State the decisions at $\alpha=0.05$ and at $\alpha=0.01$
for both.

**5.** *(§7.8)* A $t$-statistic equals $1.80$ with $15$ degrees of freedom. Compute the one-sided and
two-sided p-values. Repeat with $100$ degrees of freedom and explain why the two-sided p-value
decreases.

**6.** *(§7.4, §7.14)* Suppose $1000$ independent hypotheses are tested at $\alpha=0.05$ and all nulls
are true. What is the expected number of false rejections? What is the probability of at least one false
rejection? Repeat the probability calculation for $20$ tests and comment on the difference.

**7.** *(§7.4, §8.5, §5.10)* A sample of $n=25$ gives $\bar x=10.9$ and $s=2.0$. Construct the 95%
$t$-confidence interval for $\mu$. Test $H_0:\mu=10$ and $H_0:\mu=11$ at $\alpha=0.05$ (two-sided), and
verify that each decision agrees with whether the corresponding null value lies in the interval.

**8.** *(§7.9)* In $100$ trials there are $60$ successes. Test $H_0:p=0.5$ against $H_1:p\ne0.5$ using
(a) the normal approximation without continuity correction, (b) the normal approximation with
continuity correction, and (c) the exact binomial test. Report the three p-values and discuss why they
differ near $\alpha=0.05$.

**9.** *(§7.11, §7.12)* Give the degrees of freedom for each test.
(a) Goodness of fit with $5$ categories, no estimated parameters.
(b) Goodness of fit with $5$ categories, one parameter estimated from the data.
(c) Independence in a $3\times4$ table.
(d) Independence in a $2\times2$ table.
(e) Goodness of fit with $6$ categories, two parameters estimated.

**10.** *(§7.15)* Two one-sample studies test the same null hypothesis. Study A has $n=25$ and Cohen's
$d=0.5$; study B has $n=400$ and $d=0.1$. Using $t=d\sqrt n$ as the test statistic, compute the
two-sided p-values and compare the statistical significance with the substantive effect sizes.

**11.** *(§7.14)* Ten independent hypotheses are tested at $\alpha=0.05$ under a global null.
Compute the probability of at least one false rejection and the expected number of false rejections.
What is the Bonferroni threshold for each test?

**12.** *(§7.4)* A study reports $p=0.03$. Which of the following statements are correct?
(a) There is a $3\%$ chance that $H_0$ is true.
(b) If $H_0$ is true, about $3\%$ of studies like this would produce a result at least as extreme.
(c) There is a $97\%$ chance that the result will replicate.
(d) The effect is large.
(e) At $\alpha=0.05$ the test rejects $H_0$.
(f) There is a $3\%$ chance that the result is due to chance.

## Intermediate

**13.** *(§7.8)* A sample of $n=16$ has $\bar x=52.3$ and $s=6.1$. Test $H_0:\mu=50$ against
$H_1:\mu\ne50$ at $\alpha=0.05$. Report the standard error, the $t$-statistic, the degrees of freedom,
the p-value and the 95% confidence interval. State the conclusion in a sentence that does not use the
word "prove".

**14.** *(§7.7)* A sample of $n=36$ from a normal population with known $\sigma=12$ has $\bar x=104$.
Test $H_0:\mu=100$ against $H_1:\mu>100$ at $\alpha=0.05$, then against $H_1:\mu\ne100$. Report both
p-values and both decisions, and construct the 95% confidence interval.

**15.** *(§7.10)* Two independent samples give: $n_1=10$, $\bar x_1=32.4$, $s_1=4.0$; and $n_2=12$,
$\bar x_2=28.9$, $s_2=3.0$. Assuming equal variances, compute the pooled variance, the standard error
of the difference, the $t$-statistic, the degrees of freedom and the two-sided p-value. State the
conclusion at $\alpha=0.05$.

**16.** *(§7.10)* Repeat Exercise 15 using Welch's test. Report the standard error, the $t$-statistic,
the Welch–Satterthwaite degrees of freedom and the p-value. Compare the conclusion with the pooled test
and explain which test you would prefer if the variances were genuinely uncertain.

**17.** *(§7.10)* Six subjects are measured before and after a treatment:

| Subject | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| Before | 150 | 165 | 180 | 195 | 210 | 225 |
| After | 142 | 156 | 172 | 186 | 202 | 216 |

Analyse the data as a paired design, reporting the mean and standard deviation of the differences, the
$t$-statistic, the degrees of freedom and the p-value. Then analyse the same numbers as two independent
samples (pooled $t$-test) and explain why the conclusions differ.

**18.** *(§7.11)* A categorical variable has three categories with hypothesised proportions
$1/4,1/2,1/4$. The observed counts out of $200$ are $60,95,45$. Compute the expected counts, the
chi-squared statistic, the degrees of freedom and the p-value. State the conclusion.

**19.** *(§7.12)* A $3\times2$ contingency table has rows with counts $(30,20)$, $(20,30)$ and
$(40,10)$. Compute the row and column totals, the expected counts, the chi-squared statistic, the
degrees of freedom and the p-value. State the conclusion and one thing the test does **not** establish.

**20.** *(§7.9)* Two independent samples give $120$ successes in $300$ trials and $90$ successes in
$300$ trials. Test $H_0:p_1=p_2$ against $H_1:p_1\ne p_2$ using the pooled two-proportion $z$-test.
Report the pooled estimate, the standard error, $z$, the p-value, and the 95% confidence interval for
$p_1-p_2$. Verify that $z^2$ equals the chi-squared statistic for the corresponding $2\times2$ table.

**21.** *(§8.5)* A two-sided $z$-test at $\alpha=0.05$ has $\sigma=15$ and should detect a true mean
difference of $\delta=5$ with power $0.90$. Compute the required sample size. Repeat for power $0.80$
and compare the two sample sizes.

**22.** *(§7.14)* Five hypotheses have p-values $0.01,0.02,0.03,0.04,0.05$. At family-wise
$\alpha=0.05$, apply (a) the Bonferroni procedure and (b) Holm's step-down procedure. State which
hypotheses are rejected in each case and explain why the answers differ or agree.

**23.** *(§7.5, §8.5)* A two-sided $z$-test has $\sigma=10$, $n=25$, $\mu_0=100$ and a true mean
$\mu_1=105$. Compute the power at $\alpha=0.05$ and at $\alpha=0.01$. Report the Type II error rates
and explain the trade-off.

## Advanced

**24.** *(§7.13)* Let $X_1,\dots,X_{16}$ be independent $N(\mu,1)$. Test $H_0:\mu=0$ against
$H_1:\mu=0.5$ at $\alpha=0.05$.
(a) Derive the likelihood ratio and show that the most powerful test rejects for large $\bar x$.
(b) Find the critical value and the rejection region.
(c) Compute the power at $\mu=0.5$.

**25.** *(§7.13)* Let $X_1,\dots,X_{10}$ be independent Bernoulli$(p)$. Test $H_0:p=0.2$ against
$H_1:p=0.4$.
(a) Show that the likelihood ratio is an increasing function of $S=\sum_iX_i$.
(b) Find the non-randomised test of level at most $0.05$ with the largest power among tests of the form
"reject when $S\ge c$".
(c) Report its exact level and power.

**26.** *(§7.4, §8.4)* Let $T$ be a continuous test statistic with strictly increasing CDF $F$ under
$H_0$, and suppose the test rejects for large $T$.
(a) Show that $p=1-F(T)$ is uniformly distributed on $[0,1]$ under $H_0$.
(b) Deduce that $\Pr_{H_0}(p\le\alpha)=\alpha$ for every $\alpha$.
(c) Explain why a discrete test statistic produces a p-value that is stochastically larger than
uniform, and why the test is then conservative.

**27.** *(§7.6)* Let $T$ have a continuous distribution symmetric about $0$ under $H_0$.
(a) Show that the two-sided p-value $p=2\min(F(T),1-F(T))$ satisfies
$\Pr_{H_0}(p\le\alpha)=\alpha$ for $\alpha\in(0,1)$.
(b) Explain why naive doubling is not valid for an asymmetric statistic, and how the extremeness
ordering should be defined instead.

**28.** *(§8.3)* For a $2\times2$ table with counts $a,b,c,d$ and total $n=a+b+c+d$, prove that the
chi-squared statistic without continuity correction equals the square of the pooled two-proportion
$z$-statistic. You may use the identity
$n(ad-bc)^2=(a+b)(c+d)(a+c)(b+d)\,z^2$ and should derive it or verify it algebraically.

**29.** *(§7.14)*
(a) Prove that the Bonferroni procedure controls the family-wise error rate at $\alpha$ for any
dependence structure.
(b) For $m=20$ and $\alpha=0.05$, compare the Bonferroni bound with the exact FWER under independence,
$1-(1-\alpha)^{20}$.
(c) State Holm's procedure and explain why it is uniformly more powerful than Bonferroni.

**30.** *(§7.16)* A researcher performs five independent interim analyses of the same null hypothesis
and stops as soon as any analysis gives $p<0.05$.
(a) Compute the probability of at least one false rejection under $H_0$.
(b) Repeat for ten interim analyses.
(c) Explain how a pre-specified alpha-spending function would change the calculation, and why the
naive procedure is a form of optional stopping.

**31.** *(§7.5, §8.5)* A one-sample $t$-test with $n$ observations, two-sided $\alpha=0.05$, is
required to have power $0.80$ when $\delta/\sigma=0.5$. The power is
$\Pr(T'_{n-1,\delta\sqrt n}>t_{0.975,n-1})$, where $T'_{\nu,\eta}$ denotes a noncentral $t$ variable
with noncentrality $\eta$ (a standard numerical distribution; use software or tables). Find the
smallest $n$ by evaluating the power for $n=32,33,34,35$. Compare with the sample size given by the
normal approximation.

## Challenge

**32.** *(§8.5, §7.14)* An A/B test compares two conversion rates. The baseline rate is $10\%$, and the
team wants to detect an increase to $12\%$ with power $0.80$ at two-sided $\alpha=0.05$.
(a) Compute the required sample size per arm using the two-proportion sample-size formula with
$p_1=0.10$ and $p_2=0.12$.
(b) Suppose the team also plans to test four secondary metrics. Explain how Bonferroni would change the
threshold and what that does to the required sample size for the primary metric.
(c) Explain why checking the results daily and stopping at the first significant result invalidates the
calculation.

**33.** *(§7.2, §7.4)* An experiment with $20$ subjects per group finds an observed difference of $0$
with sample standard deviation $1$ in each group. The two-sided 95% confidence interval for the
difference is therefore approximately $0\pm0.64$ (using $t_{0.975,38}=2.024$).
(a) Verify the standard error and the interval.
(b) Explain why the result does **not** establish that the true difference is $0$, and state what range
of effects remains compatible with the data.
(c) Describe the two one-sided tests (TOST) procedure for establishing equivalence within a margin
$\Delta$, and state the null and alternative hypotheses it uses.

**34.** *(§7.15, §7.16)* A study has a true standardised effect $\delta=0.2$ and standard error
$\sigma=0.1$ (so the observed estimate is $N(0.2,0.1^2)$). Significance requires
$\hat\delta>1.96\sigma$.
(a) Compute the probability that the study is significant (the power).
(b) Compute $\mathbb{E}[\hat\delta\mid\text{significant}]$ using the truncated-normal formula
$\mathbb{E}[X\mid X>c]=\mu+\sigma\frac{\phi((c-\mu)/\sigma)}{1-\Phi((c-\mu)/\sigma)}$.
(c) Explain the winner's curse and what the calculation predicts for the first published estimate.

**35.** *(§7.11)* A Poisson model is fitted to $200$ counts. The observed frequencies for the values
$0,1,2,3,\ge4$ are $40,60,50,30,20$, and the sample mean of the raw counts is $1.65$. Test the
goodness of fit of a Poisson model.
(a) Compute the estimated probabilities and expected counts.
(b) Compute the chi-squared statistic, the degrees of freedom and the p-value.
(c) Explain why the degrees of freedom are $5-1-1=3$ rather than $5-1=4$, and check the expected-count
condition.

**36.** *(§5.8, §7.13)* Ten independent Bernoulli trials are used to test $H_0:p=0.2$ against
$H_1:p=0.4$. A randomised test rejects for $S\ge5$ with probability $1$, for $S=4$ with probability
$\gamma$, and for $S\le3$ with probability $0$.
(a) Find $\gamma$ so that the test has level exactly $0.05$.
(b) Compute the power of this randomised test at $p=0.4$.
(c) Explain why no non-randomised test of this form has level exactly $0.05$.
