# Experimental Design — Solutions

> [Experimental Design](README.md) · Solutions to all 36 problems · Exercises: [exercises.md](exercises.md)

Every solution states the strategy, then the steps. Numerical work is carried at full precision and rounded at
the end.

## Beginner

### 1. Classifying claims

*Strategy.* A causal claim asserts that an intervention would change the outcome; it needs either random
assignment or an explicit identification argument. A claim about a selected subgroup needs particular care.

(a) **Associational as stated.** It reports a comparison between children who do and do not eat breakfast.
A causal reading would need, at least, a randomised trial of breakfast provision (several exist) or an
argument that no confounder — household income, parental attention, overall diet — drives both.

(b) **Causal.** "Assigning" names an intervention. The evidence is the random assignment itself: with a
sufficiently large randomised trial, the difference in mean scores estimates the causal effect for the
participating classrooms.

(c) **Causal**, and correct, but no single experiment supports it: the evidence is the combination of
epidemiological cohort studies, dose–response gradients, temporal consistency, animal and cellular mechanisms,
and the decline in lung-cancer mortality after smoking falls. The claim is causal on the strength of that
whole body of evidence, not on one association.

(d) **Ambiguous, and probably an artefact of selection.** Restricting to patients already in intensive care
conditions on a consequence of both illness severity and treatment; the comparison can generate association
without any causal effect of blood pressure itself on mortality. This is collider bias (Exercise 26).

(e) **Associational.** Rainfall is not assigned; a causal reading would need an irrigation experiment, or a
design exploiting exogenous variation in rainfall.

### 2. Units, treatments, outcomes, factors

(a) **Units:** the $40$ plots. **Treatments:** the four fertiliser blends. **Outcome:** yield. **Factor:**
fertiliser, with four levels. Note that the unit of randomisation (plot) is the unit of analysis.

(b) **Units:** the patients. **Treatments:** new surgical technique, standard technique (two levels of one
factor). **Outcome:** complications within $30$ days — a binary outcome, so the estimand is a difference in
risks.

(c) **Units:** users (or sessions, depending on what is randomised). **Treatments:** three page layouts, i.e.
one factor with three levels. **Outcome:** subscription, binary.

### 3. Counting assignments

(a) Complete randomisation of $8$ units with $4$ treated gives $\binom{8}{4}=70$ distinct assignments.

(b) $\binom{6}{3}=20$.

(c) Pairing $10$ units into $5$ labelled pairs: order the units and pair them consecutively, which counts each
pairing $2^5\cdot5!$ times (order within pairs and order of pairs). So the number is

$$\frac{10!}{2^5\cdot5!}=\frac{3\,628\,800}{32\cdot120}=945 .$$

*Check.* Choosing the five pairs sequentially counts each pairing $5!$ times, giving
$\binom{10}{2}\binom{8}{2}\binom{6}{2}\binom{4}{2}\binom{2}{2}/5!=945$, as required.

### 4. A difference in means

(a) $6.2-2.1=4.1$ mmHg.

(b) "Among the patients eligible for this trial, assignment to the drug rather than control reduced mean
blood pressure by an estimated $4.1$ mmHg over the follow-up period."

(c) Anything two of: the follow-up period and the dose; whether the comparison is with placebo or usual care;
the population to which the estimate generalises; and the uncertainty (the standard error or interval is not
given, so $4.1$ could be $4.1\pm0.5$ or $4.1\pm9$).

### 5. Main effects and interaction

With cell means $\bar y_{00}=18$, $\bar y_{10}=22$, $\bar y_{01}=20$, $\bar y_{11}=28$:

$$\text{effect}_A=\tfrac12(22+28)-\tfrac12(18+20)=25-19=6,$$
$$\text{effect}_B=\tfrac12(20+28)-\tfrac12(18+22)=24-20=4,$$
$$\text{interaction}_{AB}=(28-20)-(22-18)=8-4=4 .$$

(d) The effect of raising temperature is $4$ units without catalyst and $8$ units with it: the catalyst
doubles the benefit of higher temperature. Because the interaction is present, quoting either main effect
alone describes no actual condition.

### 6. Confounders

(a) **Health consciousness** (and income, education, diet): people who take supplements differ in many ways
that affect mortality.

(b) **Case mix and size**: larger hospitals have more nurses *and* more complex patients; severity differs
systematically. Also wealth of the region.

(c) **Prior attainment and family background**: selection into selective schools is based on the very
variable being predicted.

(d) **National wealth**: richer countries consume more chocolate and produce more Nobel laureates; the
association is a textbook example of a third variable.

### 7. Blocking an animal experiment

(a) **Cage** is the natural block: animals in one cage share litter, position, microclimate and handling.
Blocking by cage makes each diet comparison a within-cage comparison, removing cage-to-cage variation from
the error.

(b) With $t=3$ treatments and $b=8$ blocks: treatments $3-1=2$ df, blocks $8-1=7$ df, error
$(3-1)(8-1)=14$ df, total $24-1=23$ df. (The design must have each diet appearing twice per cage or one diet
per cage with two animals: with $6$ animals per cage and $3$ diets, allocate $2$ animals to each diet.)

(c) Randomising *within* cages is what protects against systematic ordering effects — position in the rack,
order of handling, time of feeding. If diet were assigned to cages by position, a gradient in light or
temperature would be confounded with diet. Randomising within the cage also makes the residual variation
exchangeable across diets, which the analysis assumes.

### 8. Potential outcomes and selection bias

(a) $\tau_i=Y_i(1)-Y_i(0)=(8,5,2,3,1,2)$, so
$\text{SATE}=(8+5+2+3+1+2)/6=21/6=3.5$.

(b) $\bar Y_T=(12+9+7)/3=28/3=9.3333$ and $\bar Y_C=(2+3+1)/3=2$, so $\hat\tau=7.3333$.

(c) $\overline{Y(1)}=40/6=6.6667$ and $\overline{Y(0)}=19/6=3.1667$; hence
$b_T=9.3333-6.6667=2.6667$ and $b_C=2-3.1667=-1.1667$. Then

$$\text{SATE}+b_T-b_C=3.5+2.6667+1.1667=7.3334=\hat\tau . \checkmark$$

The treated units were the ones with the largest gains, so this realisation overstates the effect by
$3.83$; the procedure is unbiased, the realisation is not.

### 9. Blinding

(a) **Double blind**: the tablet and the placebo should be identical in appearance, taste and packaging, so
neither participants nor outcome assessors know the arm. A pharmacist holds the code.

(b) **Assessor blinding at least.** Participants cannot be blinded to whether they receive hands-on therapy,
but the person measuring the outcome can be, and the outcome should be something not self-reported where
possible. The report must say that participants were not blinded, because expectation may affect effort.

(c) **Assessor and analyst blinding**; blinding of patients is impossible for surgery versus medicine, and a
sham operation raises its own ethical problems. The analysis should pre-specify objective outcomes and the
report should discuss the likely direction of the resulting bias.

### 10. Sample size

(a) $z_{0.975}+z_{0.90}=1.960+1.2816=3.2416$, so

$$n=\frac{2(12^2)(3.2416)^2}{4^2}=\frac{288(10.508)}{16}=189.1\ \longrightarrow\ 190 \text{ per group}.$$

(b) $190/0.85=223.5$, so $224$ per group.

(c) $n\propto1/\Delta^2$, so halving $\Delta$ multiplies $n$ by $4$: $4(189.1)=756.5$, about $757$ per group
before allowing for dropout. This is the single most important fact in planning: small effects are expensive.

### 11. Simpson's paradox

(a) Marginal: A $=(9+40)/100=49\%$; B $=(80+20)/200=50\%$.

(b) Stratified: A $90\%$ and $44.4\%$; B $80\%$ and $20\%$. A is better in both strata.

(c) The marginal rate for each treatment is a weighted average of its stratum rates, with weights given by
that treatment's own distribution of patients across strata. A's patients were mostly high risk ($90$ of
$100$), where everyone does badly; B's were mostly low risk ($100$ of $200$), where everyone does well. The
aggregate therefore compares case mixes as much as treatments.

(d) Standardised to $110$ low risk and $190$ high risk:

$$\text{A}=\frac{0.90(110)+0.4444(190)}{300}=\frac{99+84.44}{300}=0.6115,\qquad
\text{B}=\frac{0.80(110)+0.20(190)}{300}=\frac{88+38}{300}=0.4200 .$$

A is better by $19.2$ percentage points once the case mix is held fixed — the opposite conclusion from (a).

### 12. Risk difference and relative risk

(a) Exposed: $45/150=0.3000$. Unexposed: $30/140=0.2143$.

(b) Risk difference $=0.3000-0.2143=0.0857$, i.e. $85.7$ extra cases per $1000$ exposed. Relative risk
$=0.3000/0.2143=1.400$.

(c) "Extra cases per $1000$" is the risk difference; "how many times more likely" is the relative risk. The
two answer different questions: the difference is what matters for planning services, the ratio for judging
strength of association.

## Intermediate

### 13. A randomisation test by enumeration

(a) $\bar Y_T=(5+7+9)/3=7$ and $\bar Y_C=(4+3+6)/3=13/3=4.3333$, so $\hat\tau=2.6667$.

(b) Enumerating the $20$ assignments gives the following distribution of $\hat\tau$ (values rounded):

| Value | $0$ | $0.667$ | $1.0$ | $1.667$ | $2.0$ | $2.667$ | $3.0$ | $3.667$ | $4.0$ | $4.667$ |
|---|---|---|---|---|---|---|---|---|---|---|
| Count | 1 | 1 | 2 | 2 | 4 | 4 | 2 | 2 | 1 | 1 |

The distribution has mean $2.3333$, which equals the SATE — the content of Exercise 14 — and standard
deviation $1.1450$.

(c) Ten of the twenty assignments give $\lvert\hat\tau\rvert\ge2.6667$, so $p=10/20=0.50$.

(d) The $p$-value is the probability, under the sharp null that $Y_i(1)=Y_i(0)$ for every unit, that a
randomly chosen assignment produces a difference at least as extreme as the observed one. The sharp null
says the treatment changed nothing for anyone — a stronger statement than "the average effect is zero". With
only $20$ assignments the smallest attainable two-sided $p$-value is $1/20=0.05$, and here it is $0.50$: the
data are entirely compatible with no effect.

### 14. Unbiasedness of the treated mean

(a) $\bar Y_T=\dfrac{1}{n_T}\sum_{i=1}^{n}T_iY_i(1)$, because $T_i=1$ selects the treated units and they
number $n_T$.

(b) Under complete randomisation each unit has $\Pr(T_i=1)=n_T/n$. Therefore, by linearity of expectation and
because the potential outcomes are fixed features of the units,

$$\mathbb{E}[\bar Y_T]=\frac{1}{n_T}\sum_iY_i(1)\Pr(T_i=1)=\frac{1}{n_T}\cdot\frac{n_T}{n}\sum_iY_i(1)=\frac1n\sum_iY_i(1)=\overline{Y(1)} .$$

(c) The same argument applied to $1-T_i$ gives $\mathbb{E}[\bar Y_C]=\overline{Y(0)}$, so
$\mathbb{E}[\hat\tau]=\overline{Y(1)}-\overline{Y(0)}=\text{SATE}$. SUTVA enters because it lets us write the
observed outcome as one of two fixed potential outcomes; with interference, $Y_i(1)$ would depend on the
assignments of other units and the argument would fail.

### 15. Power

(a) The standardised effect is
$\delta=\Delta/(\sigma\sqrt{2/n})=5/(10\sqrt{2/40})=5/2.2361=2.2361$. Power
$\approx\Phi(2.2361-1.960)=0.598$.

(b) $n=2(10^2)(1.960+1.2816)^2/25=200(10.5076)/25=84.06$, so $85$ per group. (The exact $t$ calculation at
$n=85$ gives $0.8999$, confirming the design.)

(c) The normal approximation treats $s$ as if it were $\sigma$; the $t$ statistic has heavier tails, so the
same critical value leaves a slightly smaller rejection region under the alternative. The discrepancy grows
as $n$ falls, which is why exact calculations are used for small trials.

### 16. Paired versus unpaired

(a) $\operatorname{Var}(\bar d)=2(144)(0.3)/20=4.32$, standard error $2.0785$.

(b) For $\rho=0.2$: $2(144)(0.8)/20=11.52$, standard error $3.3941$.

(c) The unpaired design on the same $40$ units has $2(144)/40=7.2$, standard error $2.6833$. So $\rho=0.7$
gives a $40\%$ reduction in variance relative to no pairing; $\rho=0.2$ gives a $60\%$ *increase*.

(d) Blocking on a variable that is negatively (or barely) correlated with the outcome wastes degrees of freedom
and can raise the variance. Blocks must be formed from variables known to be positively associated with the
outcome — in practice, variables that predict it.

### 17. A $2^2$ design from totals

(a) With $n=3$ replicates per cell, contrasts are sums over cell totals:

$$\text{contrast}_A=(72+90)-(60+66)=36,\qquad \text{contrast}_B=(66+90)-(60+72)=24,\qquad
\text{contrast}_{AB}=(90+60)-(72+66)=12 .$$

Hence $\mathrm{SS}_A=36^2/12=108$, $\mathrm{SS}_B=24^2/12=48$, $\mathrm{SS}_{AB}=12^2/12=12$.

(b) With $\mathrm{SSE}=8$ on $4(3-1)=8$ df, $\mathrm{MSE}=1$, so $F_A=108$, $F_B=48$, $F_{AB}=12$, each on
$(1,8)$ with $p=6.4\times10^{-6}$, $1.2\times10^{-4}$ and $0.0085$. The total sum of squares is
$108+48+12+8=176$ on $11$ df. Check: the cell means are $20,24,22,30$ with grand mean $24$, so
$\mathrm{SS}_{\text{cells}}=3(16+0+4+36)=168$ and $168+8=176$. ✓

(c) All three effects are material, and the interaction is significant at the $1\%$ level, so the main effects
must be qualified: report the two simple effects of $A$ (at each level of $B$) rather than the average $6$.

### 18. Propensity scores

(a) $\operatorname{logit}e(x)=-4+0.08x$:

| Age | logit | $e(x)$ |
|---|---|---|
| 40 | $-0.8$ | $0.3100$ |
| 60 | $0.8$ | $0.6900$ |
| 70 | $1.6$ | $0.8320$ |

(b) A treated $40$-year-old (score $0.31$) should be compared with controls of similar age, i.e. of similar
propensity score. Because age is the only covariate, matching on the score here is the same as matching on
age; with many covariates, matching on the score balances them all at once.

(c) A control aged $70$ has score $0.83$, and treated units with that score are rare or absent. Comparing that
control with a $40$-year-old treated patient would compare two different populations. When scores do not
overlap, the effect is not identified in that region (positivity fails), and the honest response is to report
the region of overlap and restrict the estimand to it.

### 19. Pooling three studies

(a) Weights $1/s_i^2$ are $25$, $100$, $400$, summing to $525$. Then

$$\hat\theta_{\text{FE}}=\frac{25(0.50)+100(0.30)+400(0.25)}{525}=\frac{12.5+30+100}{525}=0.2714 .$$

(b) $\operatorname{se}=1/\sqrt{525}=0.04364$, so the interval is
$0.2714\pm1.960(0.04364)=(0.1859,\,0.3570)$.

(c) $Q=25(0.2286)^2+100(0.0286)^2+400(-0.0214)^2=1.3061+0.0816+0.1837=1.5714$ on $2$ df, so $I^2=\max\{0,(1.5714-2)/1.5714\}=0$.
There is no evidence of heterogeneity: the studies are consistent with one common effect, and a fixed-effect
summary is reasonable.

### 20. Matching

(a) Treated mean $=(71+68+64)/3=203/3=67.6667$. Control mean $=(66+63+60+55+50)/5=294/5=58.8$. Crude
difference $=8.8667$.

(b) Nearest-age matches: $41\leftrightarrow39$ (outcome $66$), $47\leftrightarrow46$ ($63$), $55\leftrightarrow54$
($60$). Matched control mean $=(66+63+60)/3=63$, so the matched difference is $67.6667-63=4.6667$.

(c) The control group contains two older subjects (aged $60$ and $66$) with lower outcomes; the crude
comparison therefore mixes the treatment effect with the age difference. Because age is strongly related to
the outcome, matching removes most of that. Report the matched estimate ($4.67$) with its interval, and state
that two controls were outside the age range of the treated group, so the estimate applies to ages
$39$–$55$.

### 21. Standardised effect size

(a) $d=(12.4-10.1)/3.2=2.3/3.2=0.7188$.

(b) By the conventional (and arbitrary) benchmarks, $0.72$ is a *medium-to-large* effect: above Cohen's $0.5$
for medium, below $0.8$ for large.

(c) $n=2(1.960+0.8416)^2/0.7188^2=2(7.8490)/0.5166=15.698/0.5166=30.4$, so $31$ per group.

### 22. Neyman variance

(a) $\operatorname{Var}=\dfrac{16}{50}+\dfrac{9}{50}-\dfrac{4}{100}=0.32+0.18-0.04=0.46$, standard error
$0.6782$.

(b) $\sigma^2(1/50+1/50)=12.5(0.04)=0.50$, standard error $0.7071$.

(c) The usual estimator ignores the $-\,S_{TC}^2/N$ term, which is non-zero whenever effects vary across units.
Because that term is subtracted in the true variance, the usual estimator targets a larger quantity and so
over-states the variance on average — it is conservative, which is a safe direction for inference.

### 23. Intention to treat versus per protocol

(a) ITT: $(60+10)/100-40/100=0.70-0.40=0.30$.

(b) Per protocol: $60/70-40/100=0.8571-0.4000=0.4571$.

(c) ITT is the primary analysis: randomisation is preserved, so the comparison is unconfounded and estimates
the effect of *offering* the treatment, which is what a policy decision requires. The per-protocol subset is
self-selected — the patients who complied may be those with milder disease or greater motivation — so the
comparison is confounded and overstates the effect of actually receiving treatment. A valid estimate of the
latter needs an instrumental-variable or compliance-adjusted analysis, not a naive restriction.

### 24. Classifying variables

(a) **Confounder**: a common cause of $X$ and $Y$. Adjusting for it is necessary.

(b) **Mediator**: on the causal path. Adjusting for it removes part of the effect and answers "the part of the
effect not through $M$".

(c) **Collider**: a common effect. Adjusting for it induces association; leave it alone.

(d) $Y\to Z\to X$: $Z$ is a *descendant of the outcome* (part of the effect of $Y$), and adjusting for it
distorts the comparison. It is not a confounder merely because it is associated with $X$; the direction of
the arrows rules it out.

## Advanced

### 25. Why pairing reduces variance

(a) $\operatorname{Var}(Y_{i1}-Y_{i2})=\operatorname{Var}(Y_{i1})+\operatorname{Var}(Y_{i2})-2\operatorname{Cov}(Y_{i1},Y_{i2})=\sigma^2+\sigma^2-2\rho\sigma^2=2\sigma^2(1-\rho)$.

(b) The $n$ pair differences are independent, so
$\operatorname{Var}(\bar d)=\frac{1}{n^2}\sum_i2\sigma^2(1-\rho)=\frac{2\sigma^2(1-\rho)}{n}$.
The unpaired design on the same $2n$ units has $\frac{\sigma^2}{n}+\frac{\sigma^2}{n}=\frac{2\sigma^2}{n}$.

(c) The ratio is $1-\rho$, which is less than $1$ exactly when $\rho>0$, equal to $1$ when $\rho=0$, and
greater than $1$ when $\rho<0$. The cost is degrees of freedom: $n-1$ for the paired analysis against $2n-2$
for the unpaired, so with very few pairs the variance gain may be offset by a larger critical value.

### 26. Collider bias, numerically

(a) With $X,Y$ independent Bernoulli$(0.5)$, all four cells have probability $0.25$:

| | $Y=0$ | $Y=1$ |
|---|---|---|
| $X=0$ | $0.25$ | $0.25$ |
| $X=1$ | $0.25$ | $0.25$ |

(b) $C=1$ excludes only the cell $(0,0)$, leaving probability $0.75$. Within that region,
$\Pr(X=1\mid C=1)=0.50/0.75=2/3$, $\Pr(Y=1\mid C=1)=2/3$, and
$\Pr(X=1,Y=1\mid C=1)=0.25/0.75=1/3$.

(c) Independence would require $\Pr(X=1,Y=1\mid C=1)=\Pr(X=1\mid C=1)\Pr(Y=1\mid C=1)=4/9=0.4444$, but the
actual value is $0.3333$. The variables are negatively associated given $C=1$: if one is $1$, the other is
more likely to be $0$.

(d) Restricting a sample to a group defined by a common effect of two variables creates a spurious association
between them — the reason studies restricted to hospital patients, survivors or volunteers can report
correlations that do not exist in the population.

### 27. Backdoor adjustment

(a) The only path from $X$ to $Y$ beginning with an arrow into $X$ is $X\leftarrow Z\to Y$. Adjusting for $Z$
blocks it, and $Z$ is not a descendant of $X$, so $S=\{Z\}$ satisfies the backdoor criterion. The path
$X\to M\to Y$ is causal and must *not* be blocked.

(b) The adjustment formula gives

$$\Pr(Y=1\mid do(X=x))=\sum_z\Pr(Y=1\mid X=x,Z=z)\Pr(Z=z).$$

Using the numbers: the stratum-specific differences are $0.5-0.3=0.2$ at $Z=0$ and $0.8-0.7=0.1$ at $Z=1$, so

$$\text{ATE}=0.4(0.2)+0.6(0.1)=0.08+0.06=0.14 .$$

(c) $M$ lies on the causal path. Adjusting for it blocks $X\to M\to Y$ and leaves only any direct effect;
here, with no direct effect, adjusting for $M$ would return $0$ — the correct answer to "how much of the
effect does not go through $M$", and the wrong answer to "what is the effect of $X$".

### 28. Deriving the sample-size formula

(a) With equal allocation, $\operatorname{Var}(\hat\Delta)=2\sigma^2/n$. Under the alternative,
$Z=\hat\Delta/\sqrt{2\sigma^2/n}$ is approximately normal with mean
$\delta=\Delta/(\sigma\sqrt{2/n})$ and variance $1$.

(b) The two-sided level-$\alpha$ test rejects when $\lvert\hat\Delta\rvert>z_{1-\alpha/2}\sqrt{2\sigma^2/n}$,
i.e. when $\lvert Z\rvert>z_{1-\alpha/2}$.

(c) Power $=\Pr(\lvert Z\rvert>z_{1-\alpha/2})=\Phi(\delta-z_{1-\alpha/2})+\Phi(-\delta-z_{1-\alpha/2})$,
and the second term is negligible. Setting the first equal to $1-\beta$ gives
$\delta-z_{1-\alpha/2}=z_{1-\beta}$, hence

$$\frac{\Delta}{\sigma}\sqrt{\frac n2}=z_{1-\alpha/2}+z_{1-\beta}
\ \Longrightarrow\ n=\frac{2\sigma^2\bigl(z_{1-\alpha/2}+z_{1-\beta}\bigr)^2}{\Delta^2} . \checkmark$$

### 29. Why intention-to-treat is the right comparison

(a) Let $D_i\in\{0,1\}$ be the treatment actually received and $T_i$ the assignment. The observed outcome is
$Y_i=D_iY_i(1)+(1-D_i)Y_i(0)$.

(b) Under randomisation, $T_i$ is independent of every pre-treatment characteristic, including both potential
outcomes and the compliance behaviour $D_i(1),D_i(0)$. Hence

$$\mathbb{E}[Y_i\mid T_i=1]=\mathbb{E}\bigl[D_iY_i(1)+(1-D_i)Y_i(0)\mid T_i=1\bigr]
=\mathbb{E}\bigl[D_i(1)Y_i(1)+(1-D_i(1))Y_i(0)\bigr],$$

the average outcome when everyone is *assigned* to treatment, counting non-compliance. The same holds for
$T_i=0$, so the difference in means estimates the effect of assignment.

(c) Per-protocol conditions on $D_i=1$, which is a post-assignment event. Since compliance depends on the
patient and on the treatment, conditioning on it breaks the independence that made the comparison valid: the
compliers in the treated arm are a selected subgroup with no counterpart in the control arm.

### 30. Multiplicity

(a) If the five tests are independent and all nulls are true,
$\text{FWER}=1-0.95^5=1-0.7738=0.2262$: a $23\%$ chance of at least one false positive.

(b) Bonferroni: test each at $\alpha/5=0.01$. Then
$\text{FWER}\le\sum_{j=1}^{5}0.01=0.05$ by the union bound, with no independence assumption.

(c) Each test becomes harder to pass, so power falls — in this case substantially, since the critical $z$
moves from $1.96$ to $2.576$. The adjustment protects the family-wise error rate at the cost of sensitivity;
pre-specifying one primary outcome, or using a hierarchical testing procedure, recovers much of the loss.

### 31. Heterogeneous meta-analysis

(a) Weights $156.25$, $6.25$, $100$, $11.111$, $69.444$ (sum $343.06$). Then
$\hat\theta_{\text{FE}}=0.12632$ with $\operatorname{se}=1/\sqrt{343.06}=0.05399$ and interval
$(0.0205,\,0.2321)$.

(b) $Q=6.9638$ on $4$ df, so $I^2=(6.9638-4)/6.9638=0.4256$: about $43\%$ of the variation is attributable to
heterogeneity rather than chance. $\Pr(Q\ge6.96)=0.138$, so there is no formal rejection of homogeneity, but
$I^2$ and the visual spread both suggest the studies are not estimating one effect.

(c) $\sum_iw_i=343.06$ and $\sum_iw_i^2=39\,399.11$, so $\sum w_i^2/\sum w_i=114.85$ and

$$C=\sum_iw_i-\frac{\sum_iw_i^2}{\sum_iw_i}=343.06-114.85=228.21,\qquad
\tau^2=\max\{0,(6.9638-4)/228.21\}=0.012987 .$$

The random-effects weights are $1/(s_i^2+\tau^2)$: $51.58$, $5.78$, $43.50$, $9.71$, $36.51$ (sum $147.08$),
giving $\hat\theta_{\text{RE}}=0.16207$ with $\operatorname{se}=0.08245$ and interval
$(0.00046,\,0.3237)$.

(d) The random-effects estimate is pulled towards the large, imprecise study ($0.90$, weight $6.25$ under
fixed effects and $5.78$ under random effects, but now $3.9\%$ of a smaller total instead of $1.8\%$) and its
interval is $53\%$ wider. The interval almost touches zero. When heterogeneity is present, the narrower
fixed-effect interval is over-confident: it answers a question ("one common effect") the data do not support.

## Challenge

### 32. Constructing a Simpson's-paradox table

(a) Let stratum 1 be low risk and stratum 2 high risk. Treatment A is concentrated in the high-risk stratum,
where everyone does badly; B is concentrated in the low-risk stratum.

| Stratum | A successes / $n$ | A rate | B successes / $n$ | B rate |
|---|---|---|---|---|
| Low risk | $18/20$ | $90\%$ | $160/200$ | $80\%$ |
| High risk | $72/180$ | $40\%$ | $20/100$ | $20\%$ |
| **Total** | $90/200$ | $45\%$ | $180/300$ | $60\%$ |

(b) Within strata A wins: $90\%>80\%$ and $40\%>20\%$. Marginally B wins: $60\%>45\%$. Both computations are
correct; they answer different questions.

(c) Standardised to the pooled stratum sizes ($220$ low risk, $280$ high risk):

$$\text{A}=\frac{0.9(220)+0.4(280)}{500}=\frac{198+112}{500}=0.620,\qquad
\text{B}=\frac{0.8(220)+0.2(280)}{500}=\frac{176+56}{500}=0.464 .$$

On a common case mix A is better by $15.6$ percentage points, agreeing with the stratified comparison.

(d) The reversal requires the two groups' stratum distributions to differ enough to outweigh A's
within-stratum advantage. Here $90\%$ of A's patients are high risk against $33\%$ of B's, and the high-risk
stratum has a much lower baseline rate, so A's marginal rate is dragged down. With equal stratum sizes the
marginal rate is an average of the same two stratum rates with the same weights for both groups, so no
reversal is possible.

### 33. Over-controlling for a mediator

(a) $\mathbb{E}[Y\mid T=1]=0.7(12)+0.3(8)=8.4+2.4=10.8$ and
$\mathbb{E}[Y\mid T=0]=0.3(10)+0.7(6)=3.0+4.2=7.2$, so the total effect is $10.8-7.2=3.6$.

(b) Within $M=1$: $12-10=2$; within $M=0$: $8-6=2$. Any weighted average, and in particular the
$M$-adjusted effect, is therefore $2$.

(c) $M$ is a mediator: part of the effect of $T$ operates by raising $\Pr(M=1)$, and adjusting for $M$ blocks
that channel. The number $2$ is the direct effect of $T$ at a fixed level of $M$ — here the effect that does
not pass through $M$ — and it understates the total effect $3.6$. This is *over-control* (or
mediator adjustment), the mirror image of confounding: the same arithmetic that removes confounding removes
genuine effect when applied to a variable downstream of the treatment.

### 34. DerSimonian–Laird in detail

(a) Weights $100$, $25$, $44.444$, $69.444$ (sum $238.89$), so
$\hat\theta_{\text{FE}}=0.3872$, $\operatorname{se}=1/\sqrt{238.89}=0.06470$. $Q=3.4331$ on $3$ df
($p=0.330$), $I^2=(3.4331-3)/3.4331=0.1262$, i.e. about $13\%$.

(b) $\sum_iw_i=238.89$ and $\sum_iw_i^2=17\,422.84$, so $\sum_iw_i^2/\sum_iw_i=72.93$ and

$$C=238.89-72.93=165.96,\qquad \tau^2=\max\{0,(3.4331-3)/165.96\}=0.002610 .$$

Random-effects weights $1/(s_i^2+\tau^2)$ are $79.30$, $23.47$, $39.82$, $58.79$ (sum $201.39$).

(c) $\hat\theta_{\text{RE}}=0.38705$, $\operatorname{se}=1/\sqrt{201.39}=0.07047$, interval
$0.3871\pm1.960(0.07047)=(0.2489,\,0.5252)$.

(d) The two estimates are almost identical here because $\tau^2$ is small; the random-effects interval is
about $9\%$ wider, reflecting the small heterogeneity penalty. A large difference between the two estimates
would indicate that the fixed-effect weighting is being driven by the most precise study, whose effect may not
be representative.

*Arithmetic check.* $\sum w_i=100+25+44.444+69.444=238.888$; the weighted mean
$(100(0.40)+25(0.20)+44.444(0.60)+69.444(0.30))/238.888=(40+5+26.667+20.833)/238.888=92.5/238.888=0.3872$. ✓

### 35. Randomisation versus superpopulation inference

(a) From Exercise 13, the $20$ assignment-specific differences have mean $2.3333$ and standard deviation
$1.1450$. That is the spread *over assignments*, holding the units fixed.

(b) The observed treated values are $5,7,9$ ($s_T^2=4$) and the controls $4,3,6$ ($s_C^2=2.3333$), so

$$\sqrt{\frac{4}{3}+\frac{2.3333}{3}}=\sqrt{2.1111}=1.4530 .$$

(c) The randomisation standard deviation describes how the estimate would vary if the *same six units* were
re-assigned at random; it is the exact finite-population quantity. The two-sample standard error describes
how the estimate would vary if the units themselves were drawn from a population and then assigned — it has
to estimate $\sigma^2$ from three observations per group, and it targets a different variance. They need not
agree, and here they differ by about $27\%$.

(d) Randomisation inference needs no sampling model: the only randomness is the assignment, which the
experimenter controls. Any claim about a wider population requires an additional assumption that the units
are representative, which no randomisation can supply.

### 36. Unequal allocation

(a) With $n_C=kn_T$ and total $n=(1+k)n_T$,

$$\operatorname{Var}(\hat\Delta)=\sigma^2\Bigl(\frac1{n_T}+\frac1{kn_T}\Bigr)=\frac{\sigma^2}{n_T}\Bigl(1+\frac1k\Bigr),$$

so the standardised statistic has non-centrality
$\delta=\dfrac{\Delta}{\sigma}\sqrt{\dfrac{n_T}{1+1/k}}$. Setting $\delta=z_{1-\alpha/2}+z_{1-\beta}$ and
solving:

$$n_T=\frac{\bigl(1+\tfrac1k\bigr)\sigma^2\bigl(z_{1-\alpha/2}+z_{1-\beta}\bigr)^2}{\Delta^2}. \checkmark$$

(b) With $k=2$, $\sigma=10$, $\Delta=5$, $z_{0.975}+z_{0.80}=2.8016$:

$$n_T=\frac{1.5(100)(7.8490)}{25}=47.09\ \longrightarrow\ 48,\qquad n_C=96 .$$

(c) Total $144$ against $128$ for equal allocation ($64+64$) — about $12.5\%$ more units for the same power.
Unequal allocation is chosen when controls are cheap or plentiful (more controls per treated unit reduces
variance at a decreasing rate), and the formula quantifies the trade: the variance is
$\sigma^2(1/n_T+1/n_C)$, which for fixed total $n$ is minimised by $n_T=n_C$. Departing from equality is only
worthwhile if the extra controls cost less than the extra treated units.
