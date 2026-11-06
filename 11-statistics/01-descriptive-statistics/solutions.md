# Descriptive Statistics — Solutions

> [Descriptive Statistics](README.md) · Solutions to the 36 problems in [exercises.md](exercises.md)

Each solution states the strategy, carries out every significant step, and ends with a check where one
exists. Pitfalls are flagged where a problem is designed to expose one.

## Beginner

**1.** *(Strategy: order the data first; every summary except the mean reads off the ordered list.)*

The sum is $15+12+17+12+20+14+12+19=121$, so $\bar{x}=121/8=15.125$.

In order: $12,12,12,14,15,17,19,20$. With $n=8$ the median is the average of the fourth and fifth
values, $(14+15)/2=14.5$. The mode is $12$, which occurs three times; every other value occurs once.
The range is $20-12=8$.

The deviations from $15.125$ are $-0.125$ (for $15$), $-3.125$ three times (for $12$), $1.875$ (for
$17$), $4.875$ (for $20$), $-1.125$ (for $14$) and $3.875$ (for $19$). Their squares are $0.015625$,
$9.765625$ three times, $3.515625$, $23.765625$, $1.265625$ and $15.015625$, whose sum is

$$0.015625+3(9.765625)+3.515625+23.765625+1.265625+15.015625=72.875.$$

Hence

$$s^2=\frac{72.875}{7}=10.4107,\qquad s=\sqrt{10.4107}=3.227.$$

*Choice.* The mean ($15.125$) and median ($14.5$) are close and the data are roughly symmetric with no
extreme value, so the mean with the standard deviation is a reasonable summary. If robustness were the
priority, report the median $14.5$ with the IQR: $Q_1=12$ and $Q_3=17.5$ under the linear rule, so
$\operatorname{IQR}=5.5$.

*Check.* The deviations sum to $-0.125-9.375+1.875+4.875-1.125+3.875=0$. $\checkmark$

**2.** *(Strategy: ask what operations are meaningful, not what the numerals look like.)*

(a) **Nominal, discrete.** Blood groups are labels; only equality and counting are meaningful.
(b) **Ordinal, discrete.** The categories are ordered but the distances between "mild", "moderate" and
"severe" are not defined.
(c) **Interval, continuous.** Differences of temperature are meaningful, but $0^\circ$C is an arbitrary
point and $20^\circ$C is not "twice as warm" as $10^\circ$C.
(d) **Ratio, continuous.** Mass has a true zero and ratios are meaningful; a $2$ kg object is twice as
massive as a $1$ kg object. Recorded to finite precision, but modelled as continuous.
(e) **Ratio, discrete.** A count with a true zero; $4$ siblings is twice $2$.
(f) **Interval, discrete.** Differences between years are meaningful, but year $0$ is a convention and a
ratio of years is meaningless.
(g) **Nominal, discrete.** A postcode is a label, even though it is written with digits; arithmetic on it
is meaningless.
(h) **Ratio, continuous.** Waiting time has a true zero and ratios are meaningful.

*Pitfall.* Coding is not measurement. Turning (a) or (g) into numbers does not make their means
meaningful.

**3.** *(Strategy: compare a non-robust summary with a robust one and quantify the influence of the
extreme value.)*

The sum is $32+35+38+40+42+250=437$, so the mean is

$$\bar{x}=\frac{437}{6}=72.83\ \text{thousand}.$$

In order, the sixth value is $250$ and the two middle values are $38$ and $40$, so the median is
$(38+40)/2=39$ thousand. The median is far more representative: five of the six salaries are between
$32$ and $42$, and the mean lies above all of them except $250$.

Without $250$ the remaining sum is $187$ over five observations, so the mean is
$187/5=37.4$ thousand. Equivalently, with all six observations,
$\bar{x}=(5\cdot37.4+250)/6=72.83$: the single value $250$ pulls the mean up by $72.83-37.4=35.43$
thousand. The median changes only from $39$ to $38$. This is the breakdown-point difference in action.

*Check.* $5(37.4)+250=187+250=437$. $\checkmark$

**4.** *(Strategy: the mean determines the total; recover the missing total by subtraction.)*

The seven known numbers sum to

$$18+22+27+30+21+25+29=172.$$

The mean of eight numbers is $25$, so their total is $8\cdot25=200$. Hence the eighth number is
$200-172=28$.

If the eighth number were $68$, the total would be $172+68=240$ and the mean would be
$240/8=30$.

*Check.* $(172+28)/8=200/8=25$. $\checkmark$

**5.** *(Strategy: a weighted mean divides by the total weight, not by the number of components.)*

The weighted sum is

$$85\cdot2+70\cdot3+90\cdot1+60\cdot4=170+210+90+240=710,$$

and the total weight is $2+3+1+4=10$. Hence

$$\bar{x}_w=\frac{710}{10}=71.$$

*Pitfall.* The unweighted mean of the four scores is $(85+70+90+60)/4=76.25$, which is wrong because the
final examination carries four times the weight of the presentation.

**6.** *(Strategy: compute the deviations once and use them for both variances.)*

The sum is $5+7+7+8+13=40$, so $\bar{x}=40/5=8$. The deviations are

$$5-8=-3,\quad 7-8=-1,\quad 7-8=-1,\quad 8-8=0,\quad 13-8=5,$$

which sum to $-3-1-1+0+5=0$, as Proposition 8.1 requires. The sum of squared deviations is

$$(-3)^2+(-1)^2+(-1)^2+0^2+5^2=9+1+1+0+25=36.$$

With divisor $n=5$,

$$\sigma^2=\frac{36}{5}=7.2,\qquad \sigma=\sqrt{7.2}=2.683;$$

with divisor $n-1=4$,

$$s^2=\frac{36}{4}=9,\qquad s=3.$$

For a sample, report $s^2=9$ and $s=3$: the population formula assumes the mean is known independently,
whereas here $\bar{x}$ was estimated from the same five observations. If the five values were the whole
population, $7.2$ and $2.683$ would be correct.

*Check.* $7.2/9=0.8=4/5=(n-1)/n$. $\checkmark$

**7.** *(Strategy: apply the linear quartile rule, then the fences, then read the whiskers off the
ordered data.)*

The ordered data are $2,4,5,7,8,9,10,12,30$ with $n=9$; the median is $x_{(5)}=8$.

For $Q_1$, $h=1+8(0.25)=3$, so $Q_1=x_{(3)}=5$. For $Q_3$, $h=1+8(0.75)=7$, so $Q_3=x_{(7)}=10$.
Therefore

$$\operatorname{IQR}=10-5=5,$$

and the fences are

$$Q_1-1.5\operatorname{IQR}=5-7.5=-2.5,\qquad Q_3+1.5\operatorname{IQR}=10+7.5=17.5.$$

The value $30>17.5$ is flagged; $12$ is not. The five-number summary is $(2,5,8,10,30)$. A schematic
boxplot has a box from $5$ to $10$ with a line at $8$, a lower whisker ending at the smallest non-flagged
value $2$, an upper whisker ending at the largest non-flagged value $12$, and a separate point at $30$.

*Pitfall.* The upper whisker does not reach $30$: it stops at the largest observation inside the fence.
Drawing the whisker to the maximum hides the outlier.

**8.** *(Strategy: compute the same five summaries for both and compare, rather than intuiting
robustness.)*

For A ($10,12,13,15,16$): the sum is $66$, so the mean is $13.2$; the median is $13$; the range is
$16-10=6$. With $h=1+4(0.25)=2$, $Q_1=12$, and with $h=1+4(0.75)=4$, $Q_3=15$, so
$\operatorname{IQR}=3$. The deviations from $13.2$ are $-3.2,-1.2,-0.2,1.8,2.8$, whose squares sum to
$10.24+1.44+0.04+3.24+7.84=22.8$; hence $s^2=22.8/4=5.7$ and $s=2.387$.

For B ($10,12,13,15,60$): the sum is $110$, so the mean is $22$; the median is still $13$; the range is
$50$; the quartiles are again $12$ and $15$, so the IQR is $3$. The deviations from $22$ are
$-12,-10,-9,-7,38$, whose squares sum to $144+100+81+49+1444=1818$; hence $s^2=1818/4=454.5$ and
$s=21.32$.

Changing $16$ to $60$ leaves the median and IQR exactly unchanged, while the mean rises by $8.8$, the
range by $44$ and the standard deviation by a factor of $8.93$. The median and IQR are robust to a single
extreme observation; the mean, range and standard deviation are not. This is why skewed or outlier-heavy
data are summarised by the median and IQR.

*Check.* For A, $\sum x_i=66$ and $\sum x_i^2=100+144+169+225+256=894$, so
$\sum(x_i-\bar x)^2=894-66^2/5=894-871.2=22.8$. $\checkmark$ For B, $\sum x_i=110$ and
$\sum x_i^2=894-256+3600=4238$, so $\sum(x_i-\bar x)^2=4238-110^2/5=4238-2420=1818$. $\checkmark$

**9.** *(Strategy: standardise by subtracting the mean and dividing by the standard deviation.)*

For $\mu=70$ and $\sigma=10$,

$$z=\frac{x-70}{10}.$$

The four values give

| $x$ | $55$ | $70$ | $85$ | $100$ |
|---|---|---|---|---|
| $z$ | $-1.5$ | $0$ | $1.5$ | $3$ |

Interpretation: $55$ is $1.5$ standard deviations below the mean; $70$ is at the mean; $85$ is $1.5$
standard deviations above; $100$ is $3$ standard deviations above. Under the rule $\lvert z\rvert>2$, only
$100$ is unusual. If the marks are approximately normal, $z=3$ lies above the $99.8$th percentile, while
$z=1.5$ is about the $93$rd — but that percentile statement requires the normality assumption, whereas
the $z$-scores themselves do not.

**10.** *(Strategy: invert $z=(x-\mu)/\sigma$ to $x=\mu+z\sigma$.)*

With $\mu=500$ and $\sigma=100$:

$$x=500+100z.$$

Hence $z=-0.5$ gives $x=500-50=450$; $z=1.25$ gives $x=500+125=625$; $z=0$ gives $500$; and $z=2.5$
gives $x=500+250=750$.

For $x=620$,

$$z=\frac{620-500}{100}=\frac{120}{100}=1.2,$$

so the score is $1.2$ standard deviations above the mean.

*Check.* $500+100(1.2)=620$. $\checkmark$

**11.** *(Strategy: name the shape, then use the direction of the tail to predict the mean–median
ordering; treat the prediction as a tendency.)*

(a) **Uniform** on $[20,40]$. The distribution is symmetric, so the mean and median both equal $30$.
Mean and standard deviation are adequate summaries, but the range ($20$) is more informative and the
standard deviation of a uniform distribution on an interval of width $20$ is $20/\sqrt{12}=5.774$.

(b) **Right-skewed.** The long tail of large values pulls the mean above the median. The mean and standard
deviation are poor summaries alone because they are dominated by the tail; report the median and IQR, and
consider a log transformation.

(c) **Left-skewed.** The long tail of small values pulls the mean below the median. Again report the
median and IQR.

(d) **Bimodal.** The mean and median may fall near $50$, in the trough between the peaks, where no
observation lies. Report the two modes and summarise each cluster separately; the overall mean is not a
typical value.

*Caveat.* The mean–median ordering in (b) and (c) is a rule of thumb, not a theorem; it can fail for
mixtures and for unusual tail shapes.

**12.** *(Strategy: use the frequency-table formulas; remember that the mean and variance are weighted by
the frequencies.)*

The total frequency is $n=5+8+5+2=20$. The sum is

$$\sum f x=5(0)+8(1)+5(2)+2(3)=0+8+10+6=24,$$

so $\bar{x}=24/20=1.2$. The sum of squares is

$$\sum f x^2=5(0)+8(1)+5(4)+2(9)=0+8+20+18=46,$$

so the population variance is

$$\sigma^2=\frac{46}{20}-1.2^2=2.3-1.44=0.86,\qquad \sigma=\sqrt{0.86}=0.9274.$$

For the median, the cumulative frequencies are $5$ (value $0$) and $13$ (value $1$). With $n=20$, the
median is the average of the $10$th and $11$th ordered values, and both lie in the value-$1$ group, so
the median is $1$. The mode is also $1$, the value of greatest frequency.

*Check.* If the same data were treated as a sample, the variance would be
$(46-24^2/20)/19=(46-28.8)/19=17.2/19=0.9053$, slightly larger than $0.86$, as expected.

## Intermediate

**13.** *(Strategy: replace each class by its midpoint, then apply the weighted formulas; acknowledge that
the result is an approximation.)*

The midpoints of the classes are $5,15,25,35,45$ and $n=40$. The grouped sum is

$$\sum f m=4(5)+9(15)+15(25)+7(35)+5(45)=20+135+375+245+225=1000,$$

so the grouped mean is $1000/40=25$.

The deviations of the midpoints from $25$ are $-20,-10,0,10,20$, so

$$\sum f(m-\bar{x})^2=4(400)+9(100)+15(0)+7(100)+5(400)=1600+900+700+2000=5200.$$

Hence the sample variance is

$$s^2=\frac{5200}{39}=133.33,\qquad s=11.55,$$

and the population variance would be $5200/40=130$ with $\sigma=11.40$.

The modal class is $[20,30)$ with frequency $15$. With $L=20$, $h=10$, $f_1=15$, $f_0=9$ and $f_2=7$,

$$\hat M=20+\frac{15-9}{2(15)-9-7}(10)=20+\frac{6}{14}(10)=20+4.286=24.29.$$

All three numbers are estimates because the calculation assumes every observation in a class equals its
midpoint. Grouping discards the variation *within* classes, so the grouped variance typically
underestimates the variance of the original observations: by the decomposition of Proposition 8.8, the
true total variation is the within-class variation plus the between-class variation, and only the second
survives grouping. The mean is exact only if each class's mean equals its midpoint.

*Check.* The frequencies sum to $40$ and the weighted midpoints lie between $5$ and $45$, so a mean of
$25$ is plausible. $\checkmark$

**14.** *(Strategy: compute both sets of quartiles from the same ordered data and compare the fences.)*

The data are already ordered: $x_{(1)}=2,\dots,x_{(11)}=30$, with $n=11$ and median $x_{(6)}=10$.

**(a) Linear rule $h=1+(n-1)p$.** For $Q_1$, $h=1+10(0.25)=3.5$, so

$$Q_1=x_{(3)}+0.5(x_{(4)}-x_{(3)})=5+0.5(7-5)=6.$$

For $Q_3$, $h=1+10(0.75)=8.5$, so

$$Q_3=14+0.5(17-14)=15.5.$$

Hence $\operatorname{IQR}=15.5-6=9.5$ and the fences are

$$6-1.5(9.5)=-8.25,\qquad 15.5+1.5(9.5)=29.75.$$

Since $30>29.75$, $30$ is flagged as an outlier.

**(b) Exclusive rule $h=(n+1)p$.** For $Q_1$, $h=12(0.25)=3$, so $Q_1=x_{(3)}=5$. For $Q_3$,
$h=12(0.75)=9$, so $Q_3=x_{(9)}=17$. Hence $\operatorname{IQR}=12$ and the fences are

$$5-1.5(12)=-13,\qquad 17+1.5(12)=35.$$

Since $30<35$, $30$ is not flagged.

The conclusion therefore *does* depend on the convention. Neither rule is wrong; they answer slightly
different interpolation questions. The honest report states the rule and, when a decision depends on it,
reports both. The linear rule is the default in this tutorial and in R; the exclusive rule is Excel's
`QUARTILE.EXC` and is closer to the "median of the upper half" idea for this dataset.

*Check.* In both cases the lower fence is below the minimum, so no lower outliers are flagged; only the
upper tail is at issue. $\checkmark$

**15.** *(Strategy: density is count divided by total count times width; area is the proportion.)*

(a) The densities are

$$\hat f_1=\frac{20}{50\cdot5}=0.080,\qquad \hat f_2=\frac{25}{50\cdot10}=0.050,\qquad
\hat f_3=\frac{5}{50\cdot15}=0.006667.$$

The areas are $h_j\hat f_j=f_j/n$: $5(0.080)=0.40$, $10(0.050)=0.50$ and $15(0.006667)=0.10$. They sum
to $0.40+0.50+0.10=1$.

(b) A count histogram draws heights $20,25,5$. The second bar is $25\%$ taller than the first, which
suggests that the middle bin has the highest concentration, but the middle bin is twice as wide and the
third three times as wide. Per unit of measurement, the first bin has the highest density ($0.080$
against $0.050$ and $0.0067$). Counts confound frequency with width; only the density is comparable
across bins.

(c) The midpoints are $2.5$, $10$ and $22.5$, so the grouped mean is

$$\frac{20(2.5)+25(10)+5(22.5)}{50}=\frac{50+250+112.5}{50}=\frac{412.5}{50}=8.25.$$

This is an estimate: it assumes the observations within each bin are centred at the midpoint. It also
depends on the bin boundaries.

**16.** *(Strategy: the overall mean is weighted by group sizes; the overall variance uses sums of
squares, not an average of variances.)*

The overall mean is

$$\bar{x}=\frac{40(70)+60(80)}{100}=\frac{2800+4800}{100}=76.$$

The within-group sum of squares is

$$\text{SSW}=(n_A-1)s_A^2+(n_B-1)s_B^2=39(100)+59(144)=3900+8496=12396.$$

The between-group sum of squares is

$$\text{SSB}=n_A(\bar{x}_A-\bar{x})^2+n_B(\bar{x}_B-\bar{x})^2=40(70-76)^2+60(80-76)^2=40(36)+60(16)=1440+960=2400.$$

Hence

$$\text{SST}=12396+2400=14796,\qquad s^2=\frac{14796}{99}=149.45,\qquad s=12.225.$$

The weighted average of the two standard deviations is $(40\cdot10+60\cdot12)/100=11.2$, and the weighted
average of the two variances is $(40\cdot100+60\cdot144)/100=126.4$. Both are smaller than $149.45$,
because they ignore the variation of the group means about the overall mean ($\text{SSB}=2400$). The
combined standard deviation is not an average of the group standard deviations; it is the square root of
(total sum of squares)/(total degrees of freedom).

*Check.* $12396/99=125.21$ is the average within-group variance contribution, and $2400/99=24.24$ is the
between-group contribution; their sum is $149.45$. $\checkmark$

**17.** *(Strategy: compute stratum-specific and overall rates, then express the overall as a weighted
average to expose the weights.)*

(a) For A: mild $9/10=0.900$; severe $40/90=0.4444$; overall $49/100=0.490$. For B: mild
$8/10=0.800$; severe $4/10=0.400$; overall $12/20=0.600$.

(b) A's rate exceeds B's in the mild stratum ($0.900>0.800$) and in the severe stratum
($0.4444>0.400$), but A's overall rate is lower ($0.490<0.600$). This is Simpson's paradox.

(c) A's overall rate is the weighted average of its stratum rates with weights equal to its stratum
shares:

$$0.490=\frac{10}{100}(0.900)+\frac{90}{100}(0.4444)=0.090+0.400.$$

B's weights are equal:

$$0.600=\frac{10}{20}(0.800)+\frac{10}{20}(0.400)=0.400+0.200.$$

Standardising both to a common $50/50$ mixture gives

$$\text{A: }0.5(0.900)+0.5(0.4444)=0.6722,\qquad
\text{B: }0.5(0.800)+0.5(0.400)=0.6000.$$

On the common mixture, A is better.

(d) "Which treatment is better for a patient?" requires the stratified or standardised comparison, which
controls the case mix; the answer is A on a common mixture. "What happened at this clinic?" is answered
by the observed overall rates, which reflect both the treatments and the clinic's case mix. Reporting
only one of the two answers is misleading.

**18.** *(Strategy: two points determine a perfect line, so the within-group correlations are $\pm1$;
compute the overall correlation from the pooled deviations.)*

(a) Group 1: mean $x=(0+10)/2=5$, mean $y=(10+0)/2=5$, so $(5,5)$. Group 2: mean
$x=(5+15)/2=10$, mean $y=(11+1)/2=6$, so $(10,6)$.

(b) In group 1, $y=10-x$, a decreasing line, so the two points are perfectly negatively associated:
$r=-1$. In group 2, the line through $(5,11)$ and $(15,1)$ has slope $(1-11)/(15-5)=-10/10=-1$ and
intercept $16$, so $y=16-x$; it is also decreasing, so $r=-1$.

(c) The four points are $(0,10),(10,0),(5,11),(15,1)$. Their means are
$\bar{x}=30/4=7.5$ and $\bar{y}=22/4=5.5$. The deviations are

| Point | $x-7.5$ | $y-5.5$ | product |
|---|---|---|---|
| $(0,10)$ | $-7.5$ | $4.5$ | $-33.75$ |
| $(10,0)$ | $2.5$ | $-5.5$ | $-13.75$ |
| $(5,11)$ | $-2.5$ | $5.5$ | $-13.75$ |
| $(15,1)$ | $7.5$ | $-4.5$ | $-33.75$ |

The products sum to $-95$, so the covariance is $-95/4=-23.75$. Also
$\operatorname{Var}(x)=(56.25+6.25+6.25+56.25)/4=31.25$ and
$\operatorname{Var}(y)=(20.25+30.25+30.25+20.25)/4=25.25$. Hence

$$r=\frac{-23.75}{\sqrt{31.25\cdot25.25}}=\frac{-23.75}{28.09}=-0.8455.$$

(d) The group means are $(5,5)$ and $(10,6)$: as the group mean of $x$ rises from $5$ to $10$, the group
mean of $y$ rises from $5$ to $6$. An analyst seeing only those two points would infer a positive
relationship. The individual data show a negative relationship. The error is the **ecological fallacy**:
a relationship between group averages does not determine the relationship between individuals. Neither
correlation is wrong; the inference from the aggregate to the individual is.

**19.** *(Strategy: standardise each score in its own class; compare; then use the normal table and
Chebyshev's bound separately.)*

(a) $z_A=(86-68)/12=18/12=1.5$ and $z_B=(80-74)/6=6/6=1.0$. Student A is $1.5$ standard deviations above
the class mean, student B only $1.0$, so A is further above their class.

(b) Assuming normality, $\Phi(1.5)=0.9332$ and $\Phi(1.0)=0.8413$: A is roughly at the $93$rd percentile
and B at the $84$th.

(c) Chebyshev's inequality gives at least $1-1/2^2=0.75$, i.e. $75\%$, within two standard deviations of
the mean, for any distribution with finite variance. For a normal distribution the exact figure is
$95.4\%$. The Chebyshev bound is much weaker but requires no distributional assumption; the normal value
is sharper but conditional on normality.

**20.** *(Strategy: apply the affine transformation to each value and to each summary, then verify the
equivariance rules of Proposition 8.4.)*

(a) Using $F=1.8C+32$:

| $C$ | $12$ | $15$ | $18$ | $21$ | $24$ |
|---|---|---|---|---|---|
| $F$ | $53.6$ | $59.0$ | $64.4$ | $69.8$ | $75.2$ |

(b) In °C: mean $18$, median $18$, deviations $-6,-3,0,3,6$, sum of squares $90$, so
$s^2=90/4=22.5$ and $s=4.743$. With $n=5$, $Q_1=x_{(2)}=15$ and $Q_3=x_{(4)}=21$, so
$\operatorname{IQR}=6$.

In °F: mean $64.4$, median $64.4$, deviations from $64.4$ are $-10.8,-5.4,0,5.4,10.8$, whose squares sum
to $291.6$, so $s^2=291.6/4=72.9$ and $s=8.538$. The quartiles are $59.0$ and $69.8$, so the IQR is
$10.8$.

(c) $\bar F=1.8(18)+32=32.4+32=64.4$. Also $1.8s_C=1.8(4.743)=8.538=s_F$ and
$1.8\operatorname{IQR}_C=1.8(6)=10.8=\operatorname{IQR}_F$, in agreement with Proposition 8.4.

(d) The median transforms in the same way because $C\mapsto1.8C+32$ is strictly increasing and therefore
preserves order: the middle Celsius observation corresponds to the middle Fahrenheit observation. It
also holds for a decreasing affine map, because the median is the $0.5$-quantile and the two tails swap
but the middle does not. It fails for a non-monotone transformation: for the data $-2,-1,0,1,2$, the
median is $0$, but under $y=x^2$ the transformed data $4,1,0,1,4$ have median $1$, not $0^2=0$.

**21.** *(Strategy: recompute the standard deviation without the suspect value to expose masking.)*

(a) With all eleven values, the sum is $170$, so $\bar{x}=170/11=15.4545$. The sum of squared deviations
is $1772.727$, so $s=\sqrt{1772.727/10}=\sqrt{177.273}=13.3144$. Hence

$$z_{52}=\frac{52-15.4545}{13.3144}=\frac{36.5455}{13.3144}=2.745.$$

(b) Without $52$, the remaining ten values are $4,6,7,9,10,12,13,16,19,22$; their sum is $118$ and their
mean $11.8$. The deviations are $-7.8,-5.8,-4.8,-2.8,-1.8,0.2,1.2,4.2,7.2,10.2$, whose squares sum to

$$60.84+33.64+23.04+7.84+3.24+0.04+1.44+17.64+51.84+104.04=303.60.$$

Hence $s=\sqrt{303.60/9}=\sqrt{33.733}=5.808$ and

$$z_{52}=\frac{52-11.8}{5.808}=6.921.$$

(c) With all eleven values, $Q_1=8$, $Q_3=17.5$, $\operatorname{IQR}=9.5$ and the upper fence is
$17.5+14.25=31.75$; $52>31.75$, so it is flagged.

(d) The discrepancy between $z=2.74$ (all data) and $z=6.92$ (data without $52$) is **masking**. The
outlier inflates both the mean and, much more strongly, the standard deviation in its own denominator, so
its $z$-score is pulled below the threshold of $3$. Excluding it gives a scale that reflects the bulk.
The IQR rule is not fooled, because $Q_1$ and $Q_3$ are unaffected by $52$.

*Check.* $303.60/9=33.733$ and $\sqrt{33.733}=5.808$; the sum of the ten deviations is
$-7.8-5.8-4.8-2.8-1.8+0.2+1.2+4.2+7.2+10.2=0$. $\checkmark$

**22.** *(Strategy: compute each summary from its definition and compare the influence of $100$.)*

The mean is $(1+2+4+8+50)/5=65/5=13$; the median is the third ordered value, $4$.

The deviations from the mean are $-12,-11,-9,-5,37$, whose absolute values sum to
$12+11+9+5+37=74$. Hence $\operatorname{MeanAD}=74/5=14.8$.

The absolute deviations from the median are $3,2,0,4,46$; in order they are $0,2,3,4,46$, whose median
is $3$. Hence $\operatorname{MedAD}=3$.

The squared deviations sum to $144+121+81+25+1369=1740$, so $s^2=1740/4=435$ and $s=20.86$.

The median $4$ and the MedAD $3$ describe the bulk: four of the five values lie within $4$ of $4$. The
mean $13$ and the standard deviation $20.86$ are dominated by $50$; the interval $\bar{x}\pm2s$ is
$[-28.7,54.7]$, which is technically correct and practically useless. The mean absolute deviation
$14.8$ is intermediate: it is less affected than the standard deviation because it does not square the
outlier, but it is still unbounded under a single extreme value.

## Advanced

**23.** *(Strategy: expand around the mean; every statement reduces to the vanishing sum of deviations.)*

(a) By definition $n\bar{x}=\sum_i x_i$, so

$$\sum_{i=1}^{n}(x_i-\bar{x})=\sum_{i=1}^{n}x_i-\sum_{i=1}^{n}\bar{x}=n\bar{x}-n\bar{x}=0.$$

(b) **Calculus.** Expanding,

$$Q(c)=\sum_i(x_i-c)^2=\sum_i x_i^2-2c\sum_i x_i+nc^2 .$$

Differentiating with respect to $c$,

$$Q'(c)=-2\sum_i x_i+2nc=2n(c-\bar{x}).$$

Hence $Q'(c)=0$ exactly at $c=\bar{x}$. Since $Q''(c)=2n>0$, $Q$ is strictly convex and this stationary
point is the unique global minimum.

**Completing the square.** For any $c$,

$$Q(c)=\sum_i\bigl[(x_i-\bar{x})+(\bar{x}-c)\bigr]^2
=\sum_i(x_i-\bar{x})^2+2(\bar{x}-c)\sum_i(x_i-\bar{x})+n(\bar{x}-c)^2 .$$

The middle term vanishes by part (a), leaving

$$Q(c)=\sum_i(x_i-\bar{x})^2+n(\bar{x}-c)^2\ge\sum_i(x_i-\bar{x})^2,$$

with equality exactly when $(\bar{x}-c)^2=0$, i.e. $c=\bar{x}$. Uniqueness follows.

(c) The minimum value is $Q(\bar{x})=\sum_i(x_i-\bar{x})^2$. $\blacksquare$

**24.** *(Strategy: expand the square for (a); for (b) use the identity that separates the sample mean
from the true mean.)*

(a)

$$\sum_i(x_i-\bar{x})^2=\sum_i x_i^2-2\bar{x}\sum_i x_i+n\bar{x}^2
=\sum_i x_i^2-2n\bar{x}^2+n\bar{x}^2=\sum_i x_i^2-n\bar{x}^2 .$$

Since $\bar{x}=(\sum_i x_i)/n$, we have $n\bar{x}^2=(\sum_i x_i)^2/n$, which gives the stated form.

(b) Since $\sum_i(X_i-\mu)=n(\bar{X}-\mu)$,

$$\sum_i(X_i-\bar{X})^2=\sum_i\bigl[(X_i-\mu)-(\bar{X}-\mu)\bigr]^2
=\sum_i(X_i-\mu)^2-2(\bar{X}-\mu)\sum_i(X_i-\mu)+n(\bar{X}-\mu)^2$$
$$=\sum_i(X_i-\mu)^2-2n(\bar{X}-\mu)^2+n(\bar{X}-\mu)^2
=\sum_i(X_i-\mu)^2-n(\bar{X}-\mu)^2 .$$

Taking expectations,

$$\mathbb{E}\left[\sum_i(X_i-\bar{X})^2\right]=\sum_i\mathbb{E}[(X_i-\mu)^2]-n\mathbb{E}[(\bar{X}-\mu)^2]
=n\sigma^2-n\operatorname{Var}(\bar{X}).$$

Independence is used here, and only here, to write $\operatorname{Var}(\bar{X})=\sigma^2/n$ (uncorrelated
observations would suffice). Substituting,

$$\mathbb{E}\left[\sum_i(X_i-\bar{X})^2\right]=n\sigma^2-n\frac{\sigma^2}{n}=(n-1)\sigma^2,$$

so

$$\mathbb{E}[s^2]=\frac{1}{n-1}\mathbb{E}\left[\sum_i(X_i-\bar{X})^2\right]=\sigma^2 .$$

(c) With divisor $n$,

$$\mathbb{E}\left[\frac1n\sum_i(X_i-\bar{X})^2\right]=\frac{n-1}{n}\sigma^2,$$

so the bias is $\frac{n-1}{n}\sigma^2-\sigma^2=-\sigma^2/n$, a downward bias that vanishes as
$n\to\infty$.

**25.** *(Strategy: use convexity and count the observations on each side of $c$.)*

(a) $A(c)=\sum_i\lvert x_i-c\rvert$ is a sum of convex functions, hence convex. On an interval
containing no data point it is differentiable, and

$$A'(c)=\#\{i:x_i<c\}-\#\{i:x_i>c\}=2j(c)+e(c)-n,$$

where $j(c)=\#\{i:x_i<c\}$ and $e(c)=\#\{i:x_i=c\}$.

If $n=2k+1$, then just below $x_{(k+1)}$ we have $j\le k$ and $e=0$, so $A'\le2k-n=-1<0$; just above,
$j\ge k+1$ and $e=0$, so $A'\ge2(k+1)-n=1>0$. Convexity then gives a minimum at $x_{(k+1)}$.

If $n=2k$, then between $x_{(k)}$ and $x_{(k+1)}$, $j=k$ and $e=0$, so $A'=2k-n=0$; to the left of
$x_{(k)}$ the derivative is negative and to the right of $x_{(k+1)}$ it is positive. Hence every point of
$[x_{(k)},x_{(k+1)}]$ is a minimiser. The minimiser is unique exactly when $x_{(k)}=x_{(k+1)}$, that is,
when the data have a unique median; otherwise the minimising set is the whole interval between the two
middle order statistics. If data values are tied, the same counting argument applies with $e(c)>0$ and
gives the same conclusion.

(b) For $1,2,3,10$, $n=4$, so every $c\in[2,3]$ is a median and a minimiser. Check:
$A(c)=(c-1)+(c-2)+(3-c)+(10-c)=10$ for $c\in[2,3]$. At $c=1$, $A=0+1+2+9=12$; at $c=4$,
$A=3+2+1+6=12$. The minimum value is $10$ and it is attained on the whole interval $[2,3]$. $\blacksquare$

**26.** *(Strategy: add and subtract the group means, then use the vanishing of within-group deviations.)*

(a) Write $n=\sum_g n_g$ and let $\bar{x}$ be the overall mean. Then
$\bar{x}=\sum_g(n_g/n)\bar{x}_g$ because both sides equal $(\sum_g\sum_i x_{gi})/n$. For each observation,

$$x_{gi}-\bar{x}=(x_{gi}-\bar{x}_g)+(\bar{x}_g-\bar{x}).$$

Squaring and summing over $i$ and $g$,

$$\text{SST}=\sum_g\sum_i(x_{gi}-\bar{x}_g)^2
+2\sum_g(\bar{x}_g-\bar{x})\sum_i(x_{gi}-\bar{x}_g)
+\sum_g n_g(\bar{x}_g-\bar{x})^2 .$$

For each $g$, $\sum_i(x_{gi}-\bar{x}_g)=0$ by Proposition 8.1, so the cross term vanishes. The first term
is $\sum_g(n_g-1)s_g^2=\text{SSW}$, and the third is $\sum_g n_g(\bar{x}_g-\bar{x})^2=\text{SSB}$.

(b) With $n_A=40$, $\bar{x}_A=70$, $s_A=10$ and $n_B=60$, $\bar{x}_B=80$, $s_B=12$, the overall mean is
$76$. Then

$$\text{SSW}=39(100)+59(144)=3900+8496=12396,$$
$$\text{SSB}=40(70-76)^2+60(80-76)^2=40(36)+60(16)=1440+960=2400,$$
$$\text{SST}=12396+2400=14796.$$

These agree with the direct sum of squares used in Exercise 16, and $s^2=14796/99=149.45$. $\blacksquare$

**27.** *(Strategy: for the median, count how many original values must survive; for the mean, exhibit one
contaminated value.)*

(a) Replace $x_1$ by $x_1+M$. The new mean is

$$\bar{x}'=\frac{1}{n}\left(\sum_{i=1}^{n}x_i+M\right)=\bar{x}+\frac{M}{n},$$

which can be made arbitrarily large by choosing $M$. The median, by contrast, is unchanged if $n\ge3$
and the other values straddle it, because one observation cannot change which value is in the middle.

(b) Let $n=2k+1$ and suppose at most $k$ observations are replaced. At least $n-k=k+1$ original
observations remain, and all of them lie in $[x_{(1)},x_{(n)}]$. Hence at least $k+1$ of the new values
are at most $x_{(n)}$, so the $(k+1)$-th smallest new value — the new median — is at most $x_{(n)}$.
Similarly, at least $k+1$ new values are at least $x_{(1)}$, so the new median is at least $x_{(1)}$.
Therefore the new median lies in $[x_{(1)},x_{(n)}]$ and cannot be driven to infinity.

(c) Now allow $k+1$ replacements. Keep only $k$ original observations and set the other $k+1$ values to a
large number $M$. Then exactly $k$ values are below $M$ and $k+1$ are equal to $M$, so the $(k+1)$-th
smallest value is $M$. Letting $M\to\infty$ makes the median arbitrarily large.

The *breakdown point* is the smallest fraction $m/n$ of replacements that can make the estimator
arbitrarily far from its clean value. For the mean it is $1/n\to0$; for the median it is
$(k+1)/n=(n+1)/(2n)\to1/2$ for odd $n$, and $1/2$ for even $n$. Hence "the median has breakdown point
about $50\%$" and "the mean has breakdown point $0$". $\blacksquare$

**28.** *(Strategy: convert quartiles to $z$-values with the normal table, then integrate the tails.)*

(a) For $X\sim\mathcal N(\mu,\sigma^2)$, $Z=(X-\mu)/\sigma\sim\mathcal N(0,1)$. Since
$\Phi(0.67449)=0.75$, the $75$th percentile of $X$ is $\mu+0.67449\sigma$. By symmetry the $25$th
percentile is $\mu-0.67449\sigma$. Hence

$$Q_1=\mu-0.6745\sigma,\qquad Q_3=\mu+0.6745\sigma.$$

(b) Subtracting,

$$\operatorname{IQR}=Q_3-Q_1=2(0.67449)\sigma=1.34898\sigma.$$

The fences are

$$Q_1-1.5\operatorname{IQR}=\mu-\sigma(0.67449+1.5\cdot1.34898)=\mu-2.69796\sigma,$$
$$Q_3+1.5\operatorname{IQR}=\mu+2.69796\sigma.$$

(c) The probability outside is

$$2\Pr(Z>2.69796)=2\bigl(1-\Phi(2.69796)\bigr)=2(0.003488)=0.006976\approx0.0070,$$

about $0.35\%$ in each tail. The rule is a display convention calibrated for normal data: in heavy-tailed
data it flags far more than $0.7\%$, and in bounded or discrete data it may flag none. A flagged value is
a candidate for investigation, not evidence against normality, and the procedure has no null hypothesis
and no error rate in the testing sense.

**29.** *(Strategy: use $m_k(a+bx)=b^km_k(x)$, which follows from $y_i-\bar{y}=b(x_i-\bar{x})$.)*

(a) With $y_i=a+bx_i$, $\bar{y}=a+b\bar{x}$, so $y_i-\bar{y}=b(x_i-\bar{x})$. Hence
$m_k(y)=b^km_k(x)$ for every $k\ge1$, and

$$g_1(y)=\frac{m_3(y)}{m_2(y)^{3/2}}=\frac{b^3m_3(x)}{\lvert b\rvert^3m_2(x)^{3/2}}
=\frac{b^3}{\lvert b\rvert^3}g_1(x)=\operatorname{sign}(b)g_1(x).$$

(b) For $1,1,2,2,2,4,12$: $n=7$ and the mean is $24/7=3.428571$. The deviations are
$-2.428571,-2.428571,-1.428571,-1.428571,-1.428571,0.571429,8.571429$.

$$m_2=\frac{5.897959(2)+2.040816(3)+0.326531+73.469388}{7}
=\frac{91.714286}{7}=13.102041,$$
$$m_3=\frac{-14.323615(2)-2.915452(3)+0.186588+629.737609}{7}
=\frac{592.530612}{7}=84.647230,$$
$$g_1=\frac{84.647230}{(13.102041)^{3/2}}=\frac{84.647230}{47.425118}=1.7849.$$

(c) Multiplying every value by $-1$ gives $-1,-1,-2,-2,-2,-4,-12$. Here $b=-1$, so
$g_1$ must equal $-g_1(x)=-1.7849$. Directly, the mean is $-24/7$, each deviation is the negative of the
corresponding positive-data deviation, $m_2$ is unchanged and $m_3$ changes sign, so $g_1=-1.7849$.
$\checkmark$

**30.** *(Strategy: write the transformed deviations explicitly and use the definitions.)*

(a) Let $y_i=a+bx_i$. Then $\bar{y}=a+b\bar{x}$ and $y_i-\bar{y}=b(x_i-\bar{x})$, so

$$s_y^2=\frac{1}{n-1}\sum_i b^2(x_i-\bar{x})^2=b^2s_x^2 .$$

Adding $a$ ($b=1$) leaves the variance unchanged; multiplying by $b$ multiplies the variance by $b^2$.

(b) Let $z_i=(x_i-\bar{x})/s_x$. The mean of the $z$-scores is

$$\bar{z}=\frac1n\sum_i\frac{x_i-\bar{x}}{s_x}=\frac{1}{n s_x}\sum_i(x_i-\bar{x})=0,$$

using Proposition 8.1. The sample variance is

$$s_z^2=\frac{1}{n-1}\sum_i z_i^2=\frac{1}{(n-1)s_x^2}\sum_i(x_i-\bar{x})^2
=\frac{(n-1)s_x^2}{(n-1)s_x^2}=1.$$

(c) Standardisation is an affine transformation: it subtracts a constant and divides by a constant. By
Proposition 8.10, affine transformations cannot change skewness in magnitude, only its sign; they cannot
create tails, bimodality or normality. The $z$-scores of a skewed dataset are still skewed, and their
histogram is a rescaled and shifted copy of the original. The result "mean $0$, variance $1$" describes
only the first two moments.

## Challenge

**31.** *(Strategy: make the two groups' stratum sizes very different while keeping the totals equal.)*

(a) One construction, with $30$ patients per treatment:

| Stratum | A successes / patients | A rate | B successes / patients | B rate |
|---|---|---|---|---|
| Mild | $5/5$ | $1.00$ | $20/25$ | $0.80$ |
| Severe | $10/25$ | $0.40$ | $1/5$ | $0.20$ |
| Total | $15/30$ | $0.50$ | $21/30$ | $0.70$ |

A wins both strata ($1.00>0.80$ and $0.40>0.20$) and loses overall ($0.50<0.70$). The totals are equal
at $30$ each, so the reversal is not an artefact of unequal total sizes; it comes from unequal *stratum*
sizes. A treats $25/30=83.3\%$ severe patients, B only $5/30=16.7\%$.

(b) If the two treatments have the same number $n_h$ of patients in every stratum $h$, then both overall
rates use the same weights $w_h=n_h/n>0$:

$$\bar{p}_A=\sum_h w_hp_{hA},\qquad \bar{p}_B=\sum_h w_hp_{hB}.$$

Subtracting,

$$\bar{p}_A-\bar{p}_B=\sum_h w_h(p_{hA}-p_{hB}),$$

a sum of strictly positive terms; hence $\bar{p}_A>\bar{p}_B$. Therefore a reversal with equal stratum
sizes is impossible: unequal stratum sizes (or, equivalently, different distributions of the groups
across strata) are essential. $\blacksquare$

**32.** *(Strategy: compare the sum of squares with the contribution of the observations outside the
interval.)*

Let $S=\{i:\lvert x_i-\bar{x}\rvert\ge k\sigma\}$ and let $m=\lvert S\rvert$. Then

$$n\sigma^2=\sum_{i=1}^{n}(x_i-\bar{x})^2\ge\sum_{i\in S}(x_i-\bar{x})^2\ge\sum_{i\in S}k^2\sigma^2=mk^2\sigma^2 .$$

Since $\sigma^2>0$, dividing by $nk^2\sigma^2$ gives $m/n\le1/k^2$, which is the empirical Chebyshev
inequality.

For the data $2,4,4,5,5,5,7,9,9,15$: $n=10$, the sum is $65$, so $\bar{x}=6.5$. The squared deviations are
$20.25,6.25,6.25,2.25,2.25,2.25,0.25,6.25,6.25,72.25$, whose sum is $124.5$. Hence
$\sigma^2=124.5/10=12.45$ and $\sigma=\sqrt{12.45}=3.5285$. The interval is

$$\bar{x}\pm2\sigma=6.5\pm7.057=[-0.557,\ 13.557].$$

Only $15$ lies outside, so the actual fraction is $1/10=0.10$, which is below the bound $1/2^2=0.25$.

The bound is not attained here because equality in the proof requires every observation in $S$ to be
exactly $k\sigma$ from the mean and every observation outside $S$ to equal the mean. Here $15$ is at
distance $8.5>7.057$, and the other values are spread across the interval rather than concentrated at
$6.5$, so both inequalities in the chain are strict.

**33.** *(Strategy: compute the visual ratios, then compare them with the true ratio.)*

(a) On the axis $0$–$110$, the bar lengths are proportional to $100$ and $105$, so the apparent ratio is
$105/100=1.05$ and the apparent difference is $5\%$. On the axis $95$–$110$, the lengths are
$100-95=5$ and $105-95=10$, so the apparent ratio is $10/5=2$ and the apparent difference is
$(10-5)/5=100\%$.

The ratio of the apparent ratios is $2/1.05=1.905$, so the truncated axis exaggerates the ratio by about
$90.5\%$. Measured as a relative difference, the visual suggests $100\%$ instead of $5\%$ — a twentyfold
exaggeration.

(b) Doubling both height and width multiplies the area by $2\cdot2=4$. The value doubled (factor $2$), so
the area exaggerates the change by a factor $4/2=2$: the picture suggests a $300\%$ increase
(area ratio $4$) when the value increased by $100\%$ (ratio $2$).

(c) Two further distortions, with remedies:

* *Dual axes.* Plotting two series against independently chosen vertical scales can make them look
  correlated when they are not. Remedy: use one axis, or index both series to a common base $=100$ and say
  so.
* *Cherry-picked time window or bin width.* Starting a trend at a favourable trough, or choosing a bin
  width that creates a peak, can reverse the impression. Remedy: show the full series, state the window,
  and check that the conclusion survives several reasonable bin widths.
* *Cumulative rather than period data.* A cumulative curve always rises, which can obscure a decline in
  the underlying rate. Remedy: plot the period increments alongside the cumulative totals.
* *3-D pie charts.* Perspective makes the far slices look smaller. Remedy: use a bar chart or a
  two-dimensional pie with labels.

**34.** *(Strategy: the median of $\lvert X-\mu\rvert$ is the value that leaves half the probability on
each side.)*

(a) For $X\sim\mathcal N(\mu,\sigma^2)$ and $Z=(X-\mu)/\sigma$,

$$\Pr(\lvert X-\mu\rvert\le0.6745\sigma)=\Pr(-0.6745\le Z\le0.6745)
=\Phi(0.6745)-\Phi(-0.6745)=0.75-0.25=0.5 .$$

Hence $0.6745\sigma$ is the median of the distribution of $\lvert X-\mu\rvert$, which is exactly the
definition of $\operatorname{MedAD}$ for a normal distribution (the sample version estimates it).

(b) Rearranging, $\sigma=\operatorname{MedAD}/0.6745=1.4826\operatorname{MedAD}$.

(c) The ordered data are $9.8,9.9,10.0,10.1,10.2,10.3,10.4,10.5$. The median is
$(10.1+10.2)/2=10.15$. The absolute deviations are $0.05,0.35,0.35,0.05,0.25,0.15,0.15,0.25$; in order,
$0.05,0.05,0.15,0.15,0.25,0.25,0.35,0.35$, whose median is $(0.15+0.25)/2=0.20$. Hence

$$1.4826\operatorname{MedAD}=1.4826(0.20)=0.29652 .$$

For the same eight values the mean is $10.15$, the squared deviations sum to $0.42$, so
$s^2=0.42/7=0.06$ and $s=0.24495$. The robust estimate $0.2965$ is about $21\%$ larger than $s$, which is
reasonable agreement for eight observations.

(d) The MedAD is based on the median and on the median of absolute deviations. By Exercise 27, neither
can be driven arbitrarily far by fewer than half the observations; hence the MedAD has breakdown point
about $50\%$. The standard deviation is a sum of squares, so one observation moved far enough makes it
arbitrarily large: breakdown point $0$. The MedAD therefore describes the bulk even when the tails are
contaminated, at the cost of ignoring the exact magnitudes of the largest deviations.

**35.** *(Strategy: substitute the affine transformation into the definition of $z$ and track the sign of
$b$.)*

(a) If $y_i=a+bx_i$ with $b>0$, then $\bar{y}=a+b\bar{x}$ and $s_y=\lvert b\rvert s_x=bs_x$. Hence

$$z_{y_i}=\frac{y_i-\bar{y}}{s_y}=\frac{a+bx_i-a-b\bar{x}}{bs_x}
=\frac{b(x_i-\bar{x})}{bs_x}=\frac{x_i-\bar{x}}{s_x}=z_{x_i}.$$

(b) If $b<0$, then $s_y=\lvert b\rvert s_x=-bs_x$, so

$$z_{y_i}=\frac{b(x_i-\bar{x})}{-bs_x}=-z_{x_i}.$$

The $z$-scores reverse sign but keep their magnitudes: a change of units that reverses the direction of
the scale (for example, measuring a score as "errors" rather than "correct answers") reflects the
standardised values.

(c) The invariance means that a $z$-score is unit-free: metres or centimetres, °C or °F, dollars or
thousands of dollars all give the same standardised value. This is essential when measurements on
different scales must be combined or compared, as in standardised test batteries, multi-feature
clustering, principal components and regression with predictors on different units. It is not appropriate
when the scale itself carries meaning and should not be erased — for example, compositional data where
only ratios are meaningful, or any analysis in which the absolute magnitude is the subject. It is also
not a substitute for examining the distribution: standardisation preserves skewness and outliers, and
can make a badly behaved variable look deceptively "standard".

**36.** *(Strategy: compute the within-group correlations from the exact linear relations, then the
pooled correlation from the pooled deviations.)*

(a) Group 1: $(1,1),(2,2),(3,3)$ lie on $y=x$, so $r_1=1$. Group 2: $(7,-1),(8,0),(9,1)$ lie on
$y=x-8$, so $r_2=1$. Both groups show a perfect positive linear relationship.

(b) Across all six points, $\bar{x}=(1+2+3+7+8+9)/6=30/6=5$ and
$\bar{y}=(1+2+3-1+0+1)/6=6/6=1$. The deviations are

| Point | $x-5$ | $y-1$ | product |
|---|---|---|---|
| $(1,1)$ | $-4$ | $0$ | $0$ |
| $(2,2)$ | $-3$ | $1$ | $-3$ |
| $(3,3)$ | $-2$ | $2$ | $-4$ |
| $(7,-1)$ | $2$ | $-2$ | $-4$ |
| $(8,0)$ | $3$ | $-1$ | $-3$ |
| $(9,1)$ | $4$ | $0$ | $0$ |

The products sum to $-14$, so the covariance is $-14/6=-2.3333$. Also
$\operatorname{Var}(x)=(16+9+4+4+9+16)/6=58/6=9.6667$ and
$\operatorname{Var}(y)=(0+1+4+4+1+0)/6=10/6=1.6667$. Therefore

$$r=\frac{-2.3333}{\sqrt{(9.6667)(1.6667)}}=\frac{-2.3333}{4.0139}=-0.5813 .$$

(c) Within each group the relationship is positive and perfect; the group means are $(2,2)$ and $(8,0)$,
so the *between-group* relationship is negative (the group with the larger mean $x$ has the smaller mean
$y$). The pooled correlation mixes within-group and between-group variation. Here the between-group
component dominates the covariance, so the pooled correlation is negative even though every group is
perfectly positive. This is Simpson's paradox in its correlation form, also called an aggregation
reversal.

(d) Pooling data from several groups can produce a correlation whose sign contradicts the correlation in
every group. Anyone who pools must plot the groups separately, compute the correlation within each, and
consider a model with group effects (fixed or random) rather than a single pooled coefficient. The pooled
coefficient describes the mixture, not the individuals.

