# Descriptive Statistics — Exercises

> [Descriptive Statistics](README.md) · 36 problems · Beginner → Challenge · Solutions: [solutions.md](solutions.md)

Work through the problems in order; each states the section of the tutorial it tests. Attempt a written
solution before consulting [solutions.md](solutions.md). The attempt is where the learning happens.

**Conventions.** Sample variances and standard deviations use divisor $n-1$; population variances use
divisor $N$. Quartiles use the linear interpolation rule $h=1+(n-1)p$ unless a problem says otherwise.
Percentiles and probabilities that refer to the normal distribution may be obtained from a table; the
values $\Phi(1)=0.8413$, $\Phi(1.5)=0.9332$, $\Phi(1.75)=0.9599$, $\Phi(2)=0.9772$, $\Phi(2.2)=0.9861$
and $\Phi(2.5)=0.9938$ are supplied. Round final answers to four significant figures unless an exact value
is requested, but keep full precision during the calculation.

## Beginner

**1.** *(§7.3, §7.4)* The daily numbers of minutes spent commuting by eight employees were
$$15,\ 12,\ 17,\ 12,\ 20,\ 14,\ 12,\ 19.$$
Compute the mean, median, mode, range and sample standard deviation. State which measure of centre you
would report and why.

**2.** *(§7.2)* Classify each variable by scale (nominal, ordinal, interval or ratio) and as discrete or
continuous. Give a one-sentence reason for each.

(a) blood group; (b) a pain rating of mild, moderate or severe; (c) outdoor temperature in °C;
(d) body mass in kilograms; (e) number of siblings; (f) year of birth; (g) postcode; (h) waiting time in
minutes.

**3.** *(§7.3)* Six salaries, in thousands, are
$$32,\ 35,\ 38,\ 40,\ 42,\ 250.$$
Compute the mean and the median. Which is more representative of a typical salary? Recompute the mean
after removing $250$ and explain the size of the change.

**4.** *(§7.3)* The mean of eight numbers is $25$. Seven of them are
$$18,\ 22,\ 27,\ 30,\ 21,\ 25,\ 29.$$
Find the eighth number. If the eighth number were $68$ instead, what would the mean of the eight numbers
be?

**5.** *(§7.3)* A course grade is a weighted mean of four components: a project scored $85$ with weight
$2$, a midterm scored $70$ with weight $3$, a presentation scored $90$ with weight $1$, and a final
examination scored $60$ with weight $4$. Compute the course grade.

**6.** *(§7.4, §7.5)* For the five observations
$$5,\ 7,\ 7,\ 8,\ 13,$$
write down the deviations from the mean, verify that they sum to zero, and compute the sum of squared
deviations. Hence compute the population variance and standard deviation, and the sample variance and
standard deviation. Which pair would you report for a sample, and why?

**7.** *(§7.6, §7.7)* For the nine observations
$$2,\ 4,\ 5,\ 7,\ 8,\ 9,\ 10,\ 12,\ 30,$$
compute the five-number summary, the IQR and the fences. Identify any flagged values and state where the
whiskers of a schematic boxplot would end.

**8.** *(§7.4)* Two datasets are

* A: $10,\ 12,\ 13,\ 15,\ 16$;
* B: $10,\ 12,\ 13,\ 15,\ 60$.

For each, compute the mean, median, range, IQR and sample standard deviation. Which summaries are
affected by the change from $16$ to $60$, and which are not? What does this show about robustness?

**9.** *(§7.10)* A test has mean $70$ and standard deviation $10$. Compute the $z$-score of each of the
scores $55$, $70$, $85$ and $100$. Interpret each $z$-score in words, and say which scores would be
called unusual under the rule $\lvert z\rvert>2$.

**10.** *(§7.10)* A measurement has mean $\mu=500$ and standard deviation $\sigma=100$. Find the raw value
corresponding to each $z$-score: $z=-0.5$, $z=1.25$, $z=0$, $z=2.5$. Express a raw score of $620$ as a
$z$-score.

**11.** *(§7.8)* For each description, name the shape, state whether the mean is likely to be above,
below or equal to the median, and say whether the mean and standard deviation are good summaries.

(a) A histogram is flat between $20$ and $40$ and zero elsewhere.
(b) A histogram has a single peak near $30$ and a long tail of values up to $200$.
(c) A histogram has a single peak near $120$ and a long tail of values down to $10$.
(d) A histogram has peaks near $25$ and $75$ with a trough at $50$.

**12.** *(§7.3, §7.4)* A small survey records a discrete variable with frequencies

| Value | $0$ | $1$ | $2$ | $3$ |
|---|---|---|---|---|
| Frequency | $5$ | $8$ | $5$ | $2$ |

Compute the mean, the population variance and standard deviation, the median and the mode.

## Intermediate

**13.** *(§7.3, §7.4)* A grouped sample of $n=40$ observations is

| Class | $[0,10)$ | $[10,20)$ | $[20,30)$ | $[30,40)$ | $[40,50)$ |
|---|---|---|---|---|---|
| Frequency | $4$ | $9$ | $15$ | $7$ | $5$ |

Estimate the mean, the sample variance and the sample standard deviation using class midpoints. Find the
modal class and the grouped-mode estimate. Explain why these are estimates rather than exact values.

**14.** *(§7.6)* For the eleven values
$$3,\ 5,\ 6,\ 8,\ 9,\ 11,\ 12,\ 15,\ 18,\ 21,\ 33,$$
compute $Q_1$, $Q_3$, the IQR and the fences under (a) the linear rule $h=1+(n-1)p$ and (b) the exclusive
rule $h=(n+1)p$. Does the conclusion about whether $33$ is an outlier depend on the convention? Explain.

**15.** *(§7.9)* A sample of $n=50$ waiting times is grouped into the bins $[0,5)$, $[5,15)$ and
$[15,30)$ with counts $20$, $25$ and $5$.

(a) Compute the density of each bin and verify that the areas sum to $1$.
(b) Explain why a histogram of the raw counts gives a misleading impression of concentration.
(c) Assuming the observations are uniformly spread within each bin, estimate the mean using midpoints.

**16.** *(§7.4, §8.8)* Group A has $n_A=40$ employees with mean salary $70$ and sample standard deviation
$10$ (thousands). Group B has $n_B=60$ employees with mean $80$ and sample standard deviation $12$.
Compute the overall mean. Compute the within-group sum of squares, the between-group sum of squares and
the overall sample variance. Compare the overall standard deviation with the weighted average of the two
group standard deviations and explain the difference.

**17.** *(§7.11)* A clinic reports the following success counts.

| Stratum | Treatment A | Treatment B |
|---|---|---|
| Mild | $9$ of $10$ | $8$ of $10$ |
| Severe | $40$ of $90$ | $4$ of $10$ |

(a) Compute the success rate of each treatment in each stratum and overall.
(b) Verify that A has the higher rate in both strata but the lower rate overall.
(c) Show how the overall rates arise as weighted averages, and compute the rates standardised to a common
$50/50$ mixture of strata.
(d) Which comparison answers "which treatment is better for a patient?" and which answers "what happened
at this clinic?".

**18.** *(§7.11)* Two groups of two points are observed: group 1 consists of $(0,10)$ and $(10,0)$;
group 2 consists of $(5,11)$ and $(15,1)$.

(a) Compute the mean of each group.
(b) Show that within each group the correlation is $r=-1$.
(c) Compute the correlation across all four points and show that it is negative.
(d) Explain why an analyst who saw only the two group means would reach the opposite conclusion, and name
the fallacy.

**19.** *(§7.10)* In class A the mean mark is $68$ with standard deviation $12$; in class B the mean is
$74$ with standard deviation $6$. A student scores $86$ in class A and another scores $80$ in class B.

(a) Compute both $z$-scores and say which student is further above their class.
(b) Assuming normality, estimate both percentile ranks.
(c) State the Chebyshev lower bound for the proportion of each class within two standard deviations of
its mean, and compare it with the normal value $95.4\%$.

**20.** *(§7.4, §8.4)* Temperatures in °C are $12,15,18,21,24$.

(a) Convert each value to °F using $F=1.8C+32$.
(b) Compute the mean, median, sample standard deviation and IQR in °C and in °F.
(c) Verify that the mean transforms as $\bar F=1.8\bar C+32$ and the standard deviation and IQR as
$1.8$ times their Celsius values.
(d) Explain why the median transforms in the same way as the mean here, and give an example of a
transformation for which the median of the transformed data is not the transformed median.

**21.** *(§7.7)* The eleven values $3,5,6,8,9,11,12,15,18,21,47$ contain one large observation.

(a) Compute the $z$-score of $47$ using the mean and standard deviation of all eleven values.
(b) Recompute the $z$-score of $47$ using the mean and standard deviation of the other ten values.
(c) Apply the $1.5\times\operatorname{IQR}$ rule to the full dataset.
(d) Explain the discrepancy between (a) and (b) and name the phenomenon.

**22.** *(§7.4)* For the five observations $1,2,3,4,100$, compute the mean, the median, the mean absolute
deviation about the mean, the median absolute deviation about the median, and the sample standard
deviation. Which summaries describe the bulk of the data, and which are dominated by the extreme value?
Explain.

## Advanced

**23.** *(§8.1, §8.2)* (a) Prove that for any real numbers $x_1,\dots,x_n$ with mean $\bar{x}$,
$\sum_i(x_i-\bar{x})=0$. (b) Prove that $Q(c)=\sum_i(x_i-c)^2$ is uniquely minimised at $c=\bar{x}$, both
by calculus and by completing the square. (c) State the minimum value.

**24.** *(§8.3, §8.5)* (a) Prove the computational formula
$$\sum_{i=1}^{n}(x_i-\bar{x})^2=\sum_{i=1}^{n}x_i^2-\frac{1}{n}\left(\sum_{i=1}^{n}x_i\right)^2.$$
(b) Let $X_1,\dots,X_n$ be independent with mean $\mu$ and variance $\sigma^2$. Prove that
$\mathbb{E}[s^2]=\sigma^2$, stating exactly where independence is used. (c) Deduce the bias of the
estimator with divisor $n$.

**25.** *(§8.6)* (a) Prove that every median of $x_1,\dots,x_n$ minimises
$A(c)=\sum_i\lvert x_i-c\rvert$. Treat the cases $n$ odd and $n$ even, and say precisely when the
minimiser is not unique. (b) Illustrate the non-uniqueness with the four values $1,2,3,10$.

**26.** *(§8.8)* (a) Prove that for data divided into $G$ groups,
$$\text{SST}=\text{SSW}+\text{SSB},$$
defining each term. (b) Apply the identity to the two groups of Exercise 16 and verify the numerical
values.

**27.** *(§7.3, §7.7)* (a) Show that a single observation can change the sample mean by an arbitrary
amount. (b) Let $n=2k+1$ and suppose that at most $k$ observations are replaced by arbitrary values.
Prove that the new median still lies between $x_{(1)}$ and $x_{(n)}$ of the original ordered data.
(c) Show that if $k+1$ observations may be replaced, the median can be made arbitrarily large. Deduce
that the median's breakdown point is about $1/2$, while the mean's is $1/n$ and tends to $0$.

**28.** *(§7.7, §8.7)* Suppose $X\sim\mathcal N(\mu,\sigma^2)$.

(a) Show that $Q_1=\mu-0.6745\sigma$ and $Q_3=\mu+0.6745\sigma$, given
$\Phi^{-1}(0.75)=0.67449$.
(b) Compute the IQR in units of $\sigma$ and the two fences.
(c) Compute the two-tail probability outside the fences and comment on why the rule is not a test of
normality.

**29.** *(§8.10)* Let $g_1$ be the moment coefficient of skewness.

(a) Prove that $g_1(a+bx)=\operatorname{sign}(b)g_1(x)$ for $b\ne0$.
(b) Compute $g_1$ for $1,1,2,2,2,3,10$.
(c) Compute $g_1$ for $-1,-1,-2,-2,-2,-3,-10$ and check the sign rule.

**30.** *(§8.4, §8.9)* (a) Prove that adding a constant to every observation leaves the sample variance
unchanged and that multiplying by $b$ multiplies the sample variance by $b^2$. (b) Use these facts to
prove that the $z$-scores of a dataset have mean $0$ and sample variance $1$. (c) Explain why the result
does not imply that the $z$-scores are normally distributed.

## Challenge

**31.** *(§7.11)* (a) Construct a $2\times2\times2$ table (two treatments, two strata, $30$ patients per
treatment) in which treatment A has a higher success rate in each stratum but a lower overall rate.
Verify all six rates. (b) Prove the following: if the two treatments have the same number of patients in
every stratum, and A has a strictly higher rate in every stratum, then A has a strictly higher overall
rate. Explain why unequal stratum sizes are therefore essential to a reversal.

**32.** *(§8)* Let $x_1,\dots,x_n$ have mean $\bar{x}$ and population variance
$\sigma^2=\frac1n\sum_i(x_i-\bar{x})^2>0$. Prove the empirical Chebyshev inequality: for $k>0$, the
fraction of observations satisfying $\lvert x_i-\bar{x}\rvert\ge k\sigma$ is at most $1/k^2$. Apply it to
$$2,\ 4,\ 4,\ 5,\ 5,\ 5,\ 7,\ 9,\ 9,\ 15,$$
computing the mean and $\sigma$, the interval $\bar{x}\pm2\sigma$, the actual fraction outside, and the
bound. Explain why the bound is not attained here.

**33.** *(§7.11)* A report compares two values, $100$ and $105$.

(a) Compute the apparent ratio of the bar lengths when the vertical axis runs from $0$ to $110$ and when
it runs from $95$ to $110$. Express the second as a percentage exaggeration relative to the first.
(b) A pictogram doubles both the height and the width of a symbol to represent a doubled value. Compute
the ratio of the areas and the exaggeration.
(c) Describe two other graphical choices that can distort a comparison and state the honest alternative
for each.

**34.** *(§7.4, §8.7)* For a normal distribution, let $\operatorname{MedAD}$ be the median absolute
deviation from the median.

(a) Using $Q_1=\mu-0.6745\sigma$, show that $\operatorname{MedAD}=0.6745\sigma$ for a normal distribution.
(b) Deduce that $\sigma\approx1.4826\operatorname{MedAD}$.
(c) For the eight observations $12.1,11.4,12.8,13.0,11.9,12.5,12.2,11.7$, compute the median, the MedAD,
the estimate $1.4826\operatorname{MedAD}$, and the sample standard deviation. Compare them and comment.
(d) Explain why the MedAD is more robust than the standard deviation, using the breakdown-point idea.

**35.** *(§7.10, §8.4)* (a) Prove that if $y_i=a+bx_i$ with $b>0$, then the $z$-score of $y_i$ equals the
$z$-score of $x_i$. (b) Show what happens when $b<0$. (c) Explain why this invariance matters when
measurements on different scales are compared, and give one situation in which it is essential and one in
which it is not appropriate.

**36.** *(§7.11)* Two groups of three points are observed: group 1 is
$(1,1),(2,2),(3,3)$ and group 2 is $(7,-1),(8,0),(9,1)$.

(a) Compute the correlation within each group.
(b) Compute the correlation across all six points.
(c) Explain how the within-group and overall correlations can have opposite signs, and name the
phenomenon.
(d) State one practical consequence for anyone who pools data from several groups without checking the
group structure.
