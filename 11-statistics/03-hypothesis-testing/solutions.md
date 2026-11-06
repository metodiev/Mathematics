# Hypothesis Testing — Solutions

> [Hypothesis Testing](README.md) · Solutions to the 36 problems in [exercises.md](exercises.md)

Each solution states the hypotheses, checks the assumptions, carries out the computation, reports the
decision, and interprets it without overstating the conclusion. Where a p-value is near a threshold,
the exact value is given and the fragility of the decision is noted.

## Beginner

**1.** *Strategy: identify the parameter first; the parameter determines the form of the hypotheses.*

(a) Let $\mu_T$ and $\mu_P$ be the mean blood pressures under treatment and placebo. The claim is
directional: $H_0:\mu_T\ge\mu_P$ against $H_1:\mu_T<\mu_P$. In the common simplified form,
$H_0:\mu_T=\mu_P$ against $H_1:\mu_T<\mu_P$. One-sided. The parameter is the difference
$\mu_T-\mu_P$.

(b) Let $\mu$ be the mean fill volume. Either direction is a defect, so $H_0:\mu=500$ against
$H_1:\mu\ne500$. Two-sided.

(c) Let $p=\Pr(\text{heads})$. Bias in either direction is of interest, so $H_0:p=0.5$ against
$H_1:p\ne0.5$. Two-sided.

(d) Let $a$ be the true accuracy. The claim is directional, so $H_0:a\le0.9$ against $H_1:a>0.9$, or
the simple-null version $H_0:a=0.9$ against $H_1:a>0.9$. One-sided.

*Pitfall.* A one-sided hypothesis must be justified by the scientific question before the data are
seen, not by the direction the data happen to show.

**2.** *Strategy: map the decision table onto the trial.*

A Type I error is rejecting a true null: convicting an innocent defendant. A Type II error is failing to
reject a false null: acquitting a guilty defendant. "Beyond reasonable doubt" corresponds to the
significance level $\alpha$: the tolerable probability of a wrongful conviction when the defendant is
innocent. Lowering $\alpha$ makes convictions harder and increases the probability of acquitting the
guilty, the same trade-off as lowering the Type I error rate.

"Not guilty" is a verdict about the evidence, not a finding of factual innocence: the prosecution did
not meet the threshold. Likewise, "not significant" means the data did not meet the pre-specified
threshold, not that $H_0$ is true. The correct statement is that the data are compatible with $H_0$ at
level $\alpha$, and a confidence interval is needed to say which other parameter values remain
compatible.

**3.** *Strategy: evaluate the binomial tail at the null and at the alternative.*

(a) Under $p=0.5$, $X\sim\operatorname{Bin}(10,0.5)$ and

$$\alpha=\Pr(X\ge8)=\frac{\binom{10}{8}+\binom{10}{9}+\binom{10}{10}}{2^{10}}
=\frac{45+10+1}{1024}=\frac{56}{1024}=0.0546875.$$

(b) Under $p=0.8$,

$$\Pr(X\ge8)=\binom{10}{8}(0.8)^8(0.2)^2+\binom{10}{9}(0.8)^9(0.2)+(0.8)^{10}
=0.301990+0.268435+0.107374=0.677799.$$

Hence $\beta=1-0.677799=0.322200$, and the power is $0.677799$.

(c) For the rule $X\ge9$:

$$\alpha=\frac{10+1}{1024}=0.010742,$$

and

$$\Pr(X\ge9\mid p=0.8)=10(0.8)^9(0.2)+(0.8)^{10}
=0.268435+0.107374=0.375809,$$

so $\beta=0.624190$ and the power is $0.375809$.

The stricter rule cuts $\alpha$ from $0.0547$ to $0.0107$ but also cuts power from $0.678$ to $0.376$.
This is the trade-off of §7.5: with fixed $n$, a smaller Type I error rate means a larger Type II error
rate.

**4.** *Strategy: one-sided p-values are tail areas; two-sided ones double the smaller tail.*

For $z_{\text{obs}}=2.00$:

- upper-tail: $p=\Pr(Z\ge2)=1-\Phi(2)=0.02275$;
- two-sided: $p=2(1-\Phi(2))=0.04550$.

At $\alpha=0.05$ both reject, since $0.02275<0.05$ and $0.04550<0.05$. At $\alpha=0.01$ neither
rejects. The two-sided p-value is exactly twice the one-sided value here because the standard normal is
symmetric and the observed statistic is in the upper tail.

*Pitfall.* Reporting the one-sided p-value after choosing the direction from the data halves the
p-value dishonestly. The one-sided test is valid only when the direction was fixed in advance.

**5.** *Strategy: use the $t$ tables and compare with the normal limit.*

With $t=1.80$ and $\mathrm{df}=15$:

- one-sided: $p=\Pr(t_{15}\ge1.80)=0.04600$;
- two-sided: $p=2(0.04600)=0.09200$.

With $\mathrm{df}=100$:

- one-sided: $p=0.03744$;
- two-sided: $p=0.07488$.

The two-sided p-value decreases because the $t$ distribution has heavier tails than the normal for
small degrees of freedom. As $\mathrm{df}\to\infty$, $t_{100}$ approaches $N(0,1)$, and the tail
probability approaches the normal value $1-\Phi(1.80)=0.03593$ (one-sided) and $0.07186$ (two-sided).
Using a normal approximation with a small sample would therefore understate the p-value.

**6.** *Strategy: use the binomial distribution of the number of false rejections.*

Under the global null and independence, the number of rejections is
$\operatorname{Bin}(1000,0.05)$. Its expectation is $1000(0.05)=50$. The probability of at least one
false rejection is

$$1-(1-0.05)^{1000}=1-0.95^{1000}\approx1-5.3\times10^{-23}\approx1.$$

For $20$ tests, $1-0.95^{20}=0.6415$. Even a modest battery of twenty tests has a nearly two-thirds
chance of producing at least one false positive. The expected number grows linearly in $m$, but the
probability of at least one grows much faster and saturates near $1$. This is why multiplicity
correction is not optional when many tests are performed.

**7.** *Strategy: compute the $t$ interval and compare each null value with it.*

The standard error is $2.0/\sqrt{25}=0.4$. The 95% interval is

$$10.9\pm t_{0.975,24}(0.4)=10.9\pm2.0639(0.4)=10.9\pm0.8256=(10.0744,11.7256).$$

For $H_0:\mu=10$:

$$t=\frac{10.9-10}{0.4}=2.25,\qquad \mathrm{df}=24,\qquad p=0.0339,$$

so reject at $\alpha=0.05$. The value $10$ lies outside the confidence interval.

For $H_0:\mu=11$:

$$t=\frac{10.9-11}{0.4}=-0.25,\qquad p=0.8047,$$

so do not reject. The value $11$ lies inside the interval. The two decisions agree with the interval
because of the duality of §5.10: the interval is exactly the set of null values not rejected by the
two-sided test.

*Pitfall.* Do not conclude from the non-rejection of $11$ that $\mu=11$; the interval also contains
$10.1$ and $11.7$.

**8.** *Strategy: apply the three tests and compare their behaviour near the boundary.*

(a) Without continuity correction,

$$z=\frac{0.60-0.50}{\sqrt{0.5\cdot0.5/100}}=\frac{0.10}{0.05}=2.00,
\qquad p=2(1-\Phi(2))=0.0455.$$

(b) With continuity correction,

$$z=\frac{0.10-0.005}{0.05}=1.90,\qquad p=2(1-\Phi(1.90))=0.0574.$$

(c) The exact two-sided binomial p-value is $0.0569$ (computed as the total probability of outcomes
with likelihood at most that of $60$ successes).

The uncorrected normal approximation rejects at $0.05$, while the corrected and exact tests do not. The
uncorrected approximation ignores the discreteness of the binomial and is anti-conservative near the
boundary. When a decision depends on the third decimal place, the exact test is the appropriate
choice, and the result should be reported as borderline rather than decisive.

**9.** *Strategy: count free cell probabilities, subtracting one per estimated parameter.*

(a) $5-1=4$. (b) $5-1-1=3$. (c) $(3-1)(4-1)=6$. (d) $(2-1)(2-1)=1$.
(e) $6-1-2=3$.

The rule for a goodness-of-fit test is $\mathrm{df}=k-1-s$, where $s$ is the number of parameters
estimated from the data. For an independence test the margins are fixed by the design, leaving
$(r-1)(c-1)$ free probabilities.

**10.** *Strategy: convert each effect size to a $t$ statistic and compare p-values with $d$.*

Study A: $t=d\sqrt n=0.5\cdot5=2.5$, $\mathrm{df}=24$, two-sided $p=0.0197$.
Study B: $t=0.1\cdot20=2.0$, $\mathrm{df}=399$, two-sided $p=0.0462$.

Both are significant at $\alpha=0.05$, but they describe very different effects. Study A's effect is
medium-sized by conventional standards; study B's is small. Study B achieves significance because its
sample is sixteen times larger, which shrinks the standard error enough to make a $0.1$-standard-
deviation effect detectable. This is the central lesson of §7.15: a p-value is a compound of effect
size and precision, and "significant" does not mean "large".

**11.** *Strategy: independent tests give a binomial count of false rejections.*

With ten independent tests, each rejecting a true null with probability $0.05$,

$$\Pr(\text{at least one})=\ 1-(1-0.05)^{10}=1-0.95^{10}=0.4013.$$

The expected number of false rejections is $10(0.05)=0.5$. The Bonferroni threshold is
$0.05/10=0.005$ per test. Note that the expected count is small while the probability of at least one
is large: expectation and probability answer different questions.

**12.** *Strategy: test each statement against the definition of a p-value.*

(a) False. The p-value is not $\Pr(H_0\mid\text{data})$; no prior is involved.
(b) True, with the qualification "assuming the model and $H_0$ are correct" and with the tail defined
by the test. This is the definition.
(c) False. Replication probability depends on power and the replication design; it is not $1-p$.
(d) False. The p-value says nothing about the magnitude of the effect; a large sample can make a tiny
effect significant.
(e) True at $\alpha=0.05$, since $0.03<0.05$. This is a decision, not a proof.
(f) False. "Due to chance" is not a well-defined alternative; the p-value conditions on $H_0$ and the
model.

*Pitfall.* Statements (a), (c) and (f) are the three most common misreadings; each smuggles in a
posterior probability or a replication probability that the p-value does not provide.

## Intermediate

**13.** *Strategy: one-sample $t$-test with $n-1$ degrees of freedom.*

The standard error is $\operatorname{SE}=6.1/\sqrt{16}=1.525$. The statistic is

$$t=\frac{52.3-50}{1.525}=1.5082,\qquad \mathrm{df}=15.$$

The two-sided p-value is $2\Pr(t_{15}\ge1.5082)=0.1523$. Since $0.1523>0.05$, do not reject $H_0$.

The 95% interval is

$$52.3\pm t_{0.975,15}(1.525)=52.3\pm2.1314(1.525)=52.3\pm3.2505=(49.0495,55.5505).$$

The data are compatible with a mean as low as $49.05$ and as high as $55.55$. The correct conclusion is
that the study did not detect a difference from $50$ at the 5% level, not that the mean is $50$.

**14.** *Strategy: known-$\sigma$ $z$-test, then compare one- and two-sided versions.*

The standard error is $12/\sqrt{36}=2$, so

$$z=\frac{104-100}{2}=2.00.$$

For $H_1:\mu>100$, $p=1-\Phi(2)=0.02275$, so reject at $\alpha=0.05$.
For $H_1:\mu\ne100$, $p=2(0.02275)=0.04550$, so also reject at $\alpha=0.05$, but only just.

The 95% confidence interval is $104\pm1.96(2)=(100.08,107.92)$, which excludes $100$ and is
consistent with both tests. The one-sided p-value is half the two-sided value because the normal model
is symmetric and the observed statistic is in the specified direction.

**15.** *Strategy: pooled two-sample $t$-test.*

The difference in means is $32.4-28.9=3.5$. The pooled variance is

$$s_p^2=\frac{(10-1)(4.0)^2+(12-1)(3.0)^2}{10+12-2}=\frac{144+99}{20}=12.15.$$

The standard error is

$$\operatorname{SE}=s_p\sqrt{\frac{1}{10}+\frac{1}{12}}=\sqrt{12.15(0.183333)}=1.4925.$$

Hence

$$t=\frac{3.5}{1.4925}=2.3451,\qquad \mathrm{df}=20,$$

and the two-sided p-value is $0.02945$. Reject $H_0$ at $\alpha=0.05$.

The 95% confidence interval for the difference is
$3.5\pm t_{0.975,20}(1.4925)=3.5\pm2.0860(1.4925)=(0.387,6.613)$. The interval excludes $0$ but
includes differences as small as $0.39$ and as large as $6.61$; the data are compatible with a modest
to substantial effect.

*Assumptions.* Independent samples, approximate normality within each group, and equal variances. The
last is questionable here: $s_1^2=16$ and $s_2^2=9$, a ratio of $1.78$. Exercise 16 checks the
Welch version.

**16.** *Strategy: Welch's test does not pool the variances.*

The standard error is

$$\operatorname{SE}=\sqrt{\frac{16}{10}+\frac{9}{12}}=\sqrt{1.6+0.75}=1.5330,$$

so

$$t=\frac{3.5}{1.5330}=2.2831.$$

The Welch–Satterthwaite degrees of freedom are

$$\nu=\frac{(1.6+0.75)^2}{\frac{1.6^2}{9}+\frac{0.75^2}{11}}
=\frac{5.5225}{0.28444+0.05114}=16.4565.$$

The two-sided p-value is $2\Pr(t_{16.46}\ge2.2831)=0.0360$. Reject at $\alpha=0.05$, but the evidence
is weaker than in the pooled test because the degrees of freedom are smaller.

*Which test?* Welch's test is preferable as a default: it does not assume equal variances and loses
little power when they are equal. The pooled test can have an inflated Type I error when variances
differ and sample sizes are unequal, which is exactly the situation in which the equal-variance
assumption is least plausible.

**17.** *Strategy: analyse the differences, then compare with the (wrong) unpaired analysis.*

The differences are $8,9,8,9,8,9$. Their mean is $8.5$; the deviations are
$-0.5,0.5,-0.5,0.5,-0.5,0.5$, whose squares sum to $1.5$, so $s_d^2=1.5/5=0.3$ and $s_d=0.5477$. The
standard error is $0.5477/\sqrt6=0.2236$, and

$$t=\frac{8.5}{0.2236}=38.013,\qquad \mathrm{df}=5,$$

with two-sided $p=2.37\times10^{-7}$.

For the unpaired analysis, the before mean is $187.5$ with $s_1^2=787.5$, the after mean is $179.0$
with $s_2^2=778.8$, and the pooled variance is $(787.5+778.8)/2=783.15$. The standard error is
$\sqrt{783.15(2/6)}=16.157$, giving

$$t=\frac{187.5-179.0}{16.157}=0.526,\qquad \mathrm{df}=10,\qquad p=0.610.$$

The paired analysis is decisive, the unpaired analysis is not. The reason is the between-subject
variability: subjects differ by $75$ units at baseline, which dominates the unpaired standard error.
Pairing compares each subject with themselves and removes that variability. Pairing must be part of the
design; choosing pairs after seeing the data would invalidate the test.

**18.** *Strategy: expected counts from the hypothesised proportions, then $\chi^2$ with $k-1$ df.*

The expected counts are $200(1/4)=50$, $200(1/2)=100$ and $200(1/4)=50$. The statistic is

$$\chi^2=\frac{(60-50)^2}{50}+\frac{(95-100)^2}{100}+\frac{(45-50)^2}{50}
=\frac{100}{50}+\frac{25}{100}+\frac{25}{50}=2+0.25+0.5=2.75.$$

With $k=3$ categories and no estimated parameters, $\mathrm{df}=2$. The p-value is
$\Pr(\chi^2_2\ge2.75)=0.2528$, so do not reject the hypothesised proportions. All expected counts are
at least $50$, so the chi-squared approximation is safe.

*Interpretation.* The data are compatible with the $1:2:1$ model; they do not prove it. A different
sample could still reveal a modest deviation.

**19.** *Strategy: compute expected counts from the margins, then sum the squared residuals.*

The row totals are $50,50,50$; the column totals are $90$ (first column: $30+20+40$) and $60$
(second column: $20+30+10$); the grand total is $150$. Under independence, every expected count is
$50\cdot90/150=30$ in the first column and $50\cdot60/150=20$ in the second. The statistic is

$$\chi^2=0+\left(\frac{(20-30)^2}{30}+\frac{(30-20)^2}{20}\right)
+\left(\frac{(40-30)^2}{30}+\frac{(10-20)^2}{20}\right).$$

The first row contributes $0$; the second and third each contribute
$100/30+100/20=3.3333+5=8.3333$. Hence $\chi^2=16.6667$. With
$\mathrm{df}=(3-1)(2-1)=2$, the p-value is $0.000240$, so there is strong evidence of association.

The test does **not** establish causation, and it does not say which rows differ. The residuals suggest
that the first row is as expected while the second and third deviate in opposite directions. All
expected counts are at least $20$, so the approximation is adequate.

**20.** *Strategy: pool the proportions under the null, then use the normal approximation.*

The sample proportions are $\hat p_1=120/300=0.4$ and $\hat p_2=90/300=0.3$. The pooled estimate is

$$\hat p=\frac{120+90}{600}=0.35.$$

The standard error is

$$\operatorname{SE}=\sqrt{0.35(0.65)\left(\frac{1}{300}+\frac{1}{300}\right)}
=\sqrt{0.2275\cdot0.0066667}=0.038944.$$

Thus

$$z=\frac{0.4-0.3}{0.038944}=2.5678,\qquad p=2(1-\Phi(2.5678))=0.0102,$$

so reject equality at $\alpha=0.05$.

The 95% confidence interval for $p_1-p_2$ uses the unpooled standard error:

$$\operatorname{SE}_{\text{unpooled}}=\sqrt{\frac{0.4(0.6)}{300}+\frac{0.3(0.7)}{300}}
=0.038729,$$

so the interval is $0.1\pm1.96(0.038729)=(0.0241,0.1759)$.

*Check.* For the $2\times2$ table with counts $120,180,90,210$, the chi-squared statistic is
$z^2=2.5678^2=6.5934$, matching the direct computation from the table.

**21.** *Strategy: invert the power formula for the two-sided $z$-test.*

For power $1-\beta=0.80$, $z_{1-\beta}=0.8416$, and

$$n=\frac{(z_{0.975}+z_{0.80})^2\sigma^2}{\delta^2}
=\frac{(1.960+0.8416)^2(225)}{25}
=\frac{(2.8016)^2(225)}{25}=70.64.$$

Round up to $n=71$.

For power $0.90$, $z_{0.90}=1.2816$, and

$$n=\frac{(1.960+1.2816)^2(225)}{25}=\frac{(3.2416)^2(225)}{25}=94.57,$$

so $n=95$.

The ratio $95/71=1.34$ is not dramatic, but the absolute increase matters in a costly trial. The
calculation assumes known $\sigma$; with estimated $\sigma$ and a $t$-test, the required $n$ is
slightly larger (Exercise 31).

**22.** *Strategy: apply each procedure to the sorted p-values.*

The sorted p-values are $0.01,0.02,0.03,0.04,0.05$.

**Bonferroni.** Threshold $0.05/5=0.01$. Only $0.01$ is rejected (the comparison is $\le$).

**Holm.** The thresholds are

$$\frac{0.05}{5}=0.01,\quad \frac{0.05}{4}=0.0125,\quad
\frac{0.05}{3}=0.01667,\quad \frac{0.05}{2}=0.025,\quad \frac{0.05}{1}=0.05.$$

Compare in order: $0.01\le0.01$ (reject), $0.02\le0.0125$ (fail). Holm stops at the first failure, so
only the first hypothesis is rejected.

The answers agree here. They need not in general: if the first two p-values were $0.001$ and
$0.012$, Holm would reject both ($0.012\le0.0125$) while Bonferroni would reject only the first.
Holm is uniformly more powerful because its later thresholds are larger than $\alpha/m$.

**23.** *Strategy: compute the rejection probability under the alternative for each $\alpha$.*

For $\alpha=0.05$, the critical values are $100\pm1.96(2)=100\pm3.92$. Under $\mu=105$,

$$\text{power}=\Pr(Z>(103.92-105)/2)+\Pr(Z<(96.08-105)/2)
=\Pr(Z>-0.54)+4\times10^{-6}=0.7054.$$

The Type II error rate is $1-0.7054=0.2946$.

For $\alpha=0.01$, the critical values are $100\pm2.5758(2)=100\pm5.1516$. Under $\mu=105$,

$$\text{power}=\Pr(Z>(105.1516-105)/2)=\Pr(Z>0.0758)=0.4698.$$

The Type II error rate is $0.5302$.

Lowering $\alpha$ from $0.05$ to $0.01$ raises the Type II error from $0.295$ to $0.530$: the test
becomes much less likely to detect the same effect. The only ways to recover power are a larger sample,
a smaller $\sigma$, or a larger effect.

## Advanced

**24.** *Strategy: compute the likelihood ratio and use its monotonicity.*

(a) The likelihoods under $\mu=0$ and $\mu=0.5$ are

$$f_0(x)=(2\pi)^{-8}\exp\left(-\frac12\sum x_i^2\right),\qquad
f_1(x)=(2\pi)^{-8}\exp\left(-\frac12\sum (x_i-0.5)^2\right).$$

Their ratio is

$$\Lambda(x)=\frac{f_1(x)}{f_0(x)}
=\exp\left(-\frac12\sum\left[(x_i-0.5)^2-x_i^2\right]\right)
=\exp\left(-\frac12\left[-\sum x_i+\frac{16}{4}\right]\right).$$

Since $\sum x_i=16\bar x$,

$$\Lambda(x)=\exp\left(8\bar x-2\right).$$

This is strictly increasing in $\bar x$, so rejecting for large $\Lambda$ is the same as rejecting for
large $\bar x$. By the Neyman–Pearson lemma, that test is most powerful at level $\alpha$.

(b) Under $H_0$, $\bar X\sim N(0,1/16)$, so $\operatorname{SE}=0.25$. The critical value is

$$c=z_{0.95}(0.25)=1.6449(0.25)=0.4112.$$

Reject $H_0$ when $\bar x>0.4112$.

(c) Under $\mu=0.5$, $\bar X\sim N(0.5,0.25^2)$, so

$$\text{power}=\Pr(\bar X>0.4112)=\Pr\left(Z>\frac{0.4112-0.5}{0.25}\right)
=\Pr(Z>-0.3552)=0.6388.$$

The test detects the half-unit effect about $64\%$ of the time. The calculation is exact under the
normal model; the only approximation is the normal table.

**25.** *Strategy: factor the likelihood ratio and use the binomial tail.*

(a) With $S=\sum_iX_i$,

$$\frac{f_1(x)}{f_0(x)}
=\prod_{i=1}^{10}\frac{0.4^{x_i}0.6^{1-x_i}}{0.2^{x_i}0.8^{1-x_i}}
=\left(\frac{0.4}{0.2}\right)^{S}\left(\frac{0.6}{0.8}\right)^{10-S}
=2^S(0.75)^{10-S}=0.75^{10}\left(\frac{8}{3}\right)^S.$$

Since $8/3>1$, the ratio is strictly increasing in $S$. The most powerful test rejects for large $S$.

(b) Compute the null tails:

$$\Pr(S\ge4\mid p=0.2)=1-\Pr(S\le3)=0.120874,$$
$$\Pr(S\ge5\mid p=0.2)=1-\Pr(S\le4)=0.032793.$$

A test rejecting for $S\ge4$ has level $0.1209>0.05$; the test rejecting for $S\ge5$ has level
$0.0328\le0.05$. Among the non-randomised monotone tests of level at most $0.05$, $S\ge5$ has the
largest power, because lowering the threshold would violate the level and raising it would reduce
power. So the chosen test is $S\ge5$.

(c) Its level is $0.032793$ and its power at $p=0.4$ is

$$\Pr(S\ge5\mid p=0.4)=1-\Pr(S\le4)=0.366897.$$

*Remark.* The test is conservative: its actual level is $0.0328$, not $0.05$. A randomised test could
achieve exactly $0.05$ by rejecting at $S=4$ with a suitable probability (Exercise 36). The discreteness
of the binomial is the reason.

**26.** *Strategy: transform the statistic by its CDF.*

(a) Let $F$ be the strictly increasing continuous CDF of $T$ under $H_0$. Then $U=F(T)$ is uniform on
$[0,1]$: for $0\le u\le1$,

$$\Pr(U\le u)=\Pr(T\le F^{-1}(u))=F(F^{-1}(u))=u.$$

The p-value is $p=1-F(T)=1-U$, which is also uniform on $[0,1]$.

(b) For $\alpha\in[0,1]$,

$$\Pr_{H_0}(p\le\alpha)=\Pr(1-U\le\alpha)=\Pr(U\ge1-\alpha)=\alpha.$$

(c) If $T$ is discrete, $F$ has jumps, and $p=1-F(T)$ takes only the values of the tail sums. The CDF
of $p$ is then a step function that lies above the uniform CDF: $\Pr(p\le\alpha)$ equals the largest
achievable tail probability not exceeding $\alpha$, which is at most $\alpha$. Hence the test is
conservative. Equality holds only at the achievable levels, not for every $\alpha$.

**27.** *Strategy: use the symmetry of the null distribution and the uniform transform.*

(a) Let $U=F(T)$. By Exercise 26, $U$ is uniform on $[0,1]$. The two-sided p-value is
$p=2\min(U,1-U)$. For $0<\alpha<1$,

$$\Pr(p\le\alpha)=\Pr\left(U\le\frac{\alpha}{2}\right)+\Pr\left(U\ge1-\frac{\alpha}{2}\right)
=\frac{\alpha}{2}+\frac{\alpha}{2}=\alpha.$$

Symmetry ensures that the lower tail $\{T\le t\}$ and the upper tail $\{T\ge -t\}$ have equal
probability, so doubling the smaller tail really is the probability of the two-sided extreme region.
For a symmetric unimodal distribution, the region $|T|\ge|t|$ is also the likelihood-ratio ordering.

(b) For an asymmetric statistic, the two tails at the observed value can have different probabilities.
Doubling the smaller tail can understate the p-value, and doubling the larger can exceed $1$. The
correct procedure is to define an ordering of the sample space by "at least as extreme" — usually via
the likelihood ratio or via a statistic whose large values are evidence against $H_0$ — and to sum the
probabilities of all outcomes at least as extreme. In practice, use a test statistic with a known
symmetric null distribution (such as $|Z|$ or $t$) or compute the p-value by simulation from the null.

**28.** *Strategy: expand $z^2$ and clear denominators.*

Let $n=a+b+c+d$, $\hat p_1=a/(a+b)$, $\hat p_2=c/(c+d)$ and $\hat p=(a+c)/n$. The pooled statistic is

$$z=\frac{\hat p_1-\hat p_2}{\sqrt{\hat p(1-\hat p)\left(\frac{1}{a+b}+\frac{1}{c+d}\right)}}.$$

First,

$$\hat p_1-\hat p_2=\frac{a(c+d)-c(a+b)}{(a+b)(c+d)}=\frac{ad-bc}{(a+b)(c+d)}.$$

Second,

$$\hat p(1-\hat p)=\frac{(a+c)(b+d)}{n^2},$$

and

$$\frac{1}{a+b}+\frac{1}{c+d}=\frac{a+b+c+d}{(a+b)(c+d)}=\frac{n}{(a+b)(c+d)}.$$

Therefore

$$\hat p(1-\hat p)\left(\frac{1}{a+b}+\frac{1}{c+d}\right)
=\frac{(a+c)(b+d)}{n(a+b)(c+d)}.$$

Squaring $z$,

$$z^2=\frac{(ad-bc)^2}{(a+b)^2(c+d)^2}\cdot\frac{n(a+b)(c+d)}{(a+c)(b+d)}
=\frac{n(ad-bc)^2}{(a+b)(c+d)(a+c)(b+d)}.$$

The right-hand side is exactly the chi-squared statistic of the $2\times2$ table. Hence $z^2=\chi^2$.
$\blacksquare$

**29.** *Strategy: union bound for Bonferroni; step-down argument for Holm.*

(a) Let $A_i$ be the event that $H_i$ is falsely rejected. The Bonferroni procedure rejects $H_i$ when
$p_i\le\alpha/m$, so $\Pr(A_i)\le\alpha/m$ for each $i$ (this is the validity of the individual test).
By the union bound,

$$\Pr\left(\bigcup_{i=1}^{m}A_i\right)\le\sum_{i=1}^{m}\Pr(A_i)\le m\cdot\frac{\alpha}{m}=\alpha.$$

No assumption about dependence is used. $\blacksquare$

(b) Without correction, the FWER under independence is
$1-(1-0.05)^{20}=0.6415$, far above $0.05$. Bonferroni guarantees at most $0.05$; after correction the
actual FWER under independence is $1-(1-0.0025)^{20}=0.0488$, just below the bound. Bonferroni is
therefore not very conservative in this independent case, though it can be conservative under positive
dependence.

(c) **Holm.** Sort the p-values $p_{(1)}\le\cdots\le p_{(m)}$ and let $H_{(i)}$ be the corresponding
hypotheses. Reject $H_{(1)},\dots,H_{(i)}$ for the largest $i$ such that
$p_{(j)}\le\alpha/(m-j+1)$ for all $j\le i$; stop at the first failure.

*Why it controls the FWER.* If the smallest true-null p-value is $p_{(k)}$, then the event that any
true null is rejected implies $p_{(k)}\le\alpha/(m-k+1)$ (the threshold at its position is at least this
large). The probability of that event is at most $\alpha$ by a Bonferroni-type argument over the at
most $m-k+1$ hypotheses with p-values at most $p_{(k)}$. The detailed proof is in Holm's original
paper and in Casella and Berger.

*Why it is more powerful.* The thresholds $\alpha/(m-j+1)$ are at least $\alpha/m$ for every $j$, so
Holm rejects every hypothesis Bonferroni rejects, and possibly more. It is uniformly at least as
powerful.

**30.** *Strategy: independent looks give a binomial event; alpha spending changes the per-look
thresholds.*

(a) If the five analyses are independent and $H_0$ is true, each rejects with probability $0.05$, so

$$\Pr(\text{at least one rejection})=1-(1-0.05)^5=1-0.95^5=0.2262.$$

(b) For ten looks, $1-0.95^{10}=0.4013$.

(c) A pre-specified alpha-spending function allocates a small amount of the total $\alpha$ to each
interim analysis, for example $\alpha_1=0.005$, $\alpha_2=0.01$, and so on, with the cumulative
spending never exceeding $\alpha$. The overall Type I error is then controlled at $\alpha$ even though
the data are examined repeatedly. The naive procedure — test at the full $\alpha$ at every look and
stop at the first significant result — is optional stopping: it inflates the Type I error to $0.2262$
for five looks because each look is a separate opportunity to reject. The nominal $0.05$ applies to a
single planned test, not to a data-dependent sequence.

**31.** *Strategy: evaluate the noncentral $t$ power numerically and compare with the normal formula.*

The normal approximation gives

$$n=\frac{(1.960+0.8416)^2(0.5)^{-2}}{1}
=\frac{7.849}{0.25}=31.40,$$

so $32$ observations. But the exact $t$ power, using the noncentral $t$ distribution, is

| $n$ | power |
|---|---|
| 32 | $0.7823$ |
| 33 | $0.7954$ |
| 34 | $0.8078$ |
| 35 | $0.8195$ |

The smallest $n$ reaching $0.80$ is $34$, not $32$. The difference arises because the $t$-test
estimates $\sigma$ and uses a heavier-tailed null distribution; both effects require a slightly larger
sample. The normal formula is a useful first approximation, but a final sample-size calculation for a
$t$-test should use the noncentral $t$ distribution.

## Challenge

**32.** *Strategy: use the two-proportion sample-size formula; then examine the effect of multiplicity
and peeking.*

(a) For $p_1=0.10$, $p_2=0.12$, $\alpha=0.05$ two-sided and power $0.80$,

$$n=\frac{(z_{0.975}+z_{0.80})^2\left[p_1(1-p_1)+p_2(1-p_2)\right]}{(p_2-p_1)^2}
=\frac{(2.8016)^2(0.09+0.1056)}{(0.02)^2}.$$

The numerator is $7.849(0.1956)=1.5353$, and dividing by $0.0004$ gives $3838.1$. Round up:
$3839$ per arm.

(b) With five metrics and Bonferroni, the primary test would use $\alpha=0.05/5=0.01$, so
$z_{0.995}=2.5758$:

$$n=\frac{(2.5758+0.8416)^2(0.1956)}{0.0004}
=\frac{(3.4174)^2(0.1956)}{0.0004}=\frac{2.2844}{0.0004}=5711.0,$$

so $5712$ per arm. The sample size rises by about $49\%$. If the four secondary metrics are explicitly
exploratory and not used for confirmatory claims, the primary metric can remain at $0.05$; the choice
must be pre-specified, not made after seeing which metric looks best.

(c) Checking daily and stopping at the first $p<0.05$ is optional stopping. Each look is another
chance to reject under $H_0$; with many looks the Type I error approaches $1$, so the nominal $0.05$ and
the power calculation no longer describe the procedure. Use a sequential design with a pre-specified
alpha-spending function, or fix the sample size and analyse once.

**33.** *Strategy: compute the interval, interpret non-significance, and state TOST.*

(a) The standard error is

$$\operatorname{SE}=\sqrt{\frac{s_1^2}{n_1}+\frac{s_2^2}{n_2}}
=\sqrt{\frac{1}{20}+\frac{1}{20}}=0.3162.$$

With $t_{0.975,38}=2.0244$, the margin is $2.0244(0.3162)=0.6402$, so the interval is
$(-0.640,0.640)$.

(b) The interval contains differences as large as $0.64$ standard deviations in either direction.
A non-significant test therefore does not establish that the difference is zero; it establishes only
that the data are compatible with a range of effects, including potentially important ones. To claim
equivalence, one must specify a margin $\Delta$ that is the largest difference considered practically
negligible, and show that the data exclude differences outside $(-\Delta,\Delta)$.

(c) **TOST.** Choose a margin $\Delta>0$. Perform two one-sided tests:

$$H_{0a}:\mu_1-\mu_2\le-\Delta \quad\text{against}\quad H_{1a}:\mu_1-\mu_2>-\Delta,$$
$$H_{0b}:\mu_1-\mu_2\ge\Delta \quad\text{against}\quad H_{1b}:\mu_1-\mu_2<\Delta.$$

If both null hypotheses are rejected at level $\alpha$, equivalence within $\Delta$ is established at
level $\alpha$. Equivalently, a $1-2\alpha$ confidence interval for the difference must lie entirely
inside $(-\Delta,\Delta)$. TOST is not the same as a non-significant two-sided test: it requires a
pre-specified margin and demonstrates that the data are inconsistent with effects outside it.

**34.** *Strategy: compute the normal tail and the truncated mean.*

(a) Significance requires $\hat\delta>1.96(0.1)=0.196$. Under $\hat\delta\sim N(0.2,0.1^2)$,

$$\text{power}=\Pr(\hat\delta>0.196)=\Pr\left(Z>\frac{0.196-0.2}{0.1}\right)
=\Pr(Z>-0.04)=0.5160.$$

So the study has only about $52\%$ power even though the true effect is twice the standard error.

(b) With $c=0.196$, $\mu=0.2$, $\sigma=0.1$,

$$\mathbb{E}[\hat\delta\mid\text{significant}]
=0.2+0.1\frac{\phi((0.196-0.2)/0.1)}{1-\Phi((0.196-0.2)/0.1)}
=0.2+0.1\frac{\phi(-0.04)}{0.5160}.$$

Using $\phi(-0.04)=0.3986$,

$$\mathbb{E}[\hat\delta\mid\text{significant}]=0.2+0.1(0.7725)=0.2773.$$

(c) The conditional estimate is $0.277$, about $39\%$ larger than the true $0.2$. This is the winner's
curse: when power is modest, the studies that reach significance are those whose random error happened
to be positive. The first published estimate is therefore biased upward, and a replication with the
same true effect will on average be smaller. The calculation also shows why effect sizes from small
significant studies should not be taken at face value, and why replication is essential.

**35.** *Strategy: estimate $\lambda$, compute expected counts, then apply chi-squared with the
degrees-of-freedom penalty.*

(a) The estimate is $\hat\lambda=1.65$. The Poisson probabilities are

| $k$ | $0$ | $1$ | $2$ | $3$ | $\ge4$ |
|---|---|---|---|---|---|
| $p_k$ | $0.19205$ | $0.31688$ | $0.26143$ | $0.14379$ | $0.08585$ |
| $E_k=200p_k$ | $38.410$ | $63.376$ | $52.286$ | $28.757$ | $17.171$ |

The last probability is $1-\sum_{k=0}^{3}p_k$.

(b) The statistic is

$$\chi^2=\frac{(40-38.410)^2}{38.410}+\frac{(60-63.376)^2}{63.376}
+\frac{(50-52.286)^2}{52.286}+\frac{(30-28.757)^2}{28.757}
+\frac{(20-17.171)^2}{17.171}=0.8655.$$

With $k=5$ cells, one estimated parameter and $\mathrm{df}=5-1-1=3$, the p-value is
$\Pr(\chi^2_3\ge0.8655)=0.8338$. There is no evidence of lack of fit.

(c) One degree of freedom is lost because $\lambda$ was estimated from the same data: the expected
counts are constrained to match the sample mean, reducing the effective number of free cell
comparisons. If $\lambda$ had been specified in advance, the degrees of freedom would be $5-1=4$. The
smallest expected count is $17.17\ge5$, so the chi-squared approximation is acceptable. The test has
limited power: with $200$ observations and five cells, moderate departures from Poisson could go
undetected, and the grouping of all values $\ge4$ discards information about the upper tail.

**36.** *Strategy: solve the level equation for the randomisation probability, then recompute the power.*

Under $H_0:p=0.2$, the relevant probabilities are

$$\Pr(S\ge5)=0.0327935,\qquad \Pr(S=4)=\binom{10}{4}(0.2)^4(0.8)^6=0.0880804.$$

(a) The level of the randomised test is

$$\alpha(\gamma)=0.0327935+\gamma(0.0880804).$$

Set this equal to $0.05$:

$$\gamma=\frac{0.05-0.0327935}{0.0880804}=0.19535.$$

So reject for $S\ge5$, reject for $S=4$ with probability $0.19535$, and never reject for $S\le3$.

(b) Under $p=0.4$,

$$\Pr(S\ge5\mid0.4)=0.3668967,\qquad
\Pr(S=4\mid0.4)=\binom{10}{4}(0.4)^4(0.6)^6=0.2508227.$$

The power is

$$0.3668967+0.19535(0.2508227)=0.3668967+0.0490=0.4159.$$

(c) A non-randomised test can only choose a rejection region, so its level is one of the binomial tail
probabilities. Near $0.05$ the available levels are $0.03279$ (reject for $S\ge5$) and $0.12087$
(reject for $S\ge4$); neither equals $0.05$. Randomisation at the boundary $S=4$ fills the gap by
rejecting with an auxiliary probability that is independent of the data. This achieves the exact level
but is rarely used in practice because it requires a random device and makes the decision depend on
something beyond the data. The Neyman–Pearson lemma is stated for randomised tests precisely so that
"most powerful at level $\alpha$" is attainable for discrete models.

