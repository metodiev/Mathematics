# Linear Regression — Solutions

> [Linear Regression](README.md) · Solutions to all 36 problems · Exercises: [exercises.md](exercises.md)

Every solution states the strategy first, then the steps. Numbers are carried at full precision and rounded
only at the end. Where a second method exists, it is given as a remark.

## Beginner

### 1. Reading a fitted line

*Strategy.* Use §7.5: a slope is a rate in the units of $y$ per unit of $x$; an intercept is a conditional
mean at $x=0$ and is only interpretable inside the data range.

(a) Each additional millimetre of rainfall is associated with $0.64$ kg more yield per plot, on average.

(b) $b_0=5.2$ kg is the predicted mean yield at $x=0$ mm of rainfall. Rainfall never drops below $40$ mm in
these data, and $0$ mm is physically far outside the observed range, so this is an extrapolation and should
not be reported as a finding. (Dropping the intercept is not the remedy: that would force the line through
the origin and change the slope.)

(c) $\hat y=5.2+0.64(80)=5.2+51.2=56.4$ kg per plot.

(d) Any two of: that rainfall *causes* higher yield (plots were not assigned rainfall at random); that the
relationship stays linear outside $40\le x\le120$; that $R^2$ is large or that the model is correct; that
individual plots will follow this line (it describes a conditional mean, not an individual).

### 2. Fitting from summary statistics

*Strategy.* Convert raw sums to centred sums first: that is where the rounding errors are avoided.

(a)

$$S_{xx}=\sum x_i^2-\frac{(\sum x_i)^2}{n}=310-\frac{50^2}{10}=310-250=60,$$
$$S_{xy}=\sum x_iy_i-\frac{(\sum x_i)(\sum y_i)}{n}=700-\frac{50\cdot120}{10}=700-600=100 .$$

(b) $b_1=S_{xy}/S_{xx}=100/60=1.6667$. With $\bar x=5$ and $\bar y=12$,
$b_0=\bar y-b_1\bar x=12-1.6667(5)=12-8.3333=3.6667$.

(c) $b_0+b_1\bar x=3.6667+1.6667(5)=3.6667+8.3333=12=\bar y$. ✓

(d) $\sum_ie_i=\sum y_i-nb_0-b_1\sum x_i=120-10(3.6667)-1.6667(50)=120-36.667-83.333=0$. ✓
This had to happen by (b): the residuals always sum to zero when the intercept solves the first normal
equation.

### 3. Residuals, $\mathrm{SSE}$ and $R^2$

*Strategy.* Compute fitted values first, then residuals, then the two sums of squares.

(a) Fitted values $1.5+1.6x$ are $3.1,\,4.7,\,6.3,\,7.9,\,9.5,\,11.1$. Hence

$$e=(-0.2,\,-0.1,\,-0.2,\,-0.2,\,-0.1,\,0.1).$$

(b) $\mathrm{SSE}=0.04+0.01+0.04+0.04+0.01+0.01=0.15$.

(c) $\bar y=41.9/6=6.9833$, and

$$S_{yy}=\sum(y_i-\bar y)^2=16.674+5.680+0.780+0.514+5.840+17.780=47.268 .$$

So $R^2=1-0.15/47.268=1-0.003174=0.9968$.

(d) The residuals are all negative except the last, and $\sum e_i=-0.7\ne0$. By §8.1 a genuine
least-squares line with an intercept has $\sum e_i=0$, so the stated line is *not* the least-squares fit
for these data: it lies slightly above the cloud on the left and to the right. The near-perfect $R^2$
therefore measures how close the supplied line happens to be, not the quality of a fit.

### 4. $\mathrm{SSE}$ and $R^2$

(a) $\mathrm{SSE}=\mathrm{SST}-\mathrm{SSR}=250-180=70$ and $R^2=180/250=0.72$.

(b) $72\%$ of the sample variation of $y$ about its mean is accounted for by the fitted values; equivalently,
the residuals are $28\%$ as variable, in squared-deviation terms, as $y$ is about its own mean.

(c) $R^2$ is a ratio of sums of squares, not a probability or a percentage of correct predictions. A model
can account for $72\%$ of the variance and still be wrong about the functional form, biased by an omitted
variable, or useless for prediction. It also says nothing about the size of the residual standard error in the
units of $y$.

### 5. Standard error of the slope

(a) $\operatorname{se}(b_1)=s/\sqrt{S_{xx}}=4/\sqrt{250}=4/15.8114=0.25298$.

(b) Replacing $x_i$ by $2x_i$ multiplies $S_{xx}$ by $4$, giving $1000$. Fitted values are unchanged and the
slope halves, so $s$ is unchanged and $\operatorname{se}(b_1)=4/\sqrt{1000}=0.12649$ — exactly half the
previous value. Precision *per unit of the new variable* is therefore unchanged; what changes is the size of
one unit relative to the spread of $x$.

(c) Not necessarily. $\operatorname{se}(b_1)=s/\sqrt{S_{xx}}$ and $s$ is an estimate of the same $\sigma$, so
doubling $n$ helps only through $S_{xx}$. If the new $x$-values are spread like the old ones, $S_{xx}$
roughly doubles and $\operatorname{se}(b_1)$ falls by a factor $\sqrt2$. If the new observations sit near
$\bar x$, $S_{xx}$ barely grows and the standard error barely falls. Precision comes from *spread* in $x$ as
much as from sample size.

### 6. Testing a slope

(a) $t=(1.8-0)/0.6=3.00$ on $n-2=18$ degrees of freedom. Since $t_{18,0.975}=2.101$ and $3.00>2.101$, reject
$H_0\colon\beta_1=0$ at the $5\%$ level.

(b) $1.8\pm2.101(0.6)=1.8\pm1.2606$, i.e. $(0.5394,\,3.0606)$.

(c) It means: if the study were repeated many times, about $95\%$ of intervals built this way would contain
the true $\beta_1$. It does not mean that $\beta_1$ lies in $(0.5394,3.0606)$ with probability $0.95$ — after
the data are in, the interval either contains the fixed $\beta_1$ or it does not.

*Remark.* Because the interval excludes $0$, the test in (a) and the interval in (b) agree, as they must:
the interval is the set of null values not rejected at the $5\%$ level.

### 7. Changing the units of the predictor

(a) A $1\,^{\circ}\mathrm{C}$ higher temperature is associated with $0.05$ litres per $100$ km *less* fuel
use, on average.

(b) From $t_{\mathrm C}=(t_{\mathrm F}-32)/1.8$,

$$\hat y=9.4-0.05\cdot\frac{t_{\mathrm F}-32}{1.8}=9.4-0.027778(t_{\mathrm F}-32)=10.2889-0.027778\,t_{\mathrm F}.$$

(c) The slope is smaller in magnitude because one degree Fahrenheit is only $5/9$ of a degree Celsius:
$0.05\times\frac{5}{9}=0.027778$. Both models give identical fitted values — the $R^2$, $t$ statistic and
residuals are unchanged — so the choice is purely a matter of the reader's units. A US audience expects
$^{\circ}\mathrm{F}$, and quoting a per-$^{\circ}\mathrm{C}$ slope to them invites misreading.

### 8. Two intervals at one point

Use $t_{18,0.975}=2.101$ and $s=4$.

(a) $\operatorname{se}(\hat y_0)=4\sqrt{0.1+0.05}=4(0.387298)=1.54919$, so
$50\pm2.101(1.54919)=50\pm3.2548=(46.75,\,53.25)$.

(b) $\operatorname{se}(y_0-\hat y_0)=4\sqrt{1.15}=4(1.072381)=4.28952$, so
$50\pm2.101(4.28952)=50\pm9.0117=(40.99,\,59.01)$.

(c) The ratio is $\sqrt{1.15/0.15}=\sqrt{7.667}=2.769$. The prediction interval carries the additional
$\sigma^2$ of the new observation's own error, which no amount of fitting can remove; the confidence interval
carries only the uncertainty in the estimated mean.

### 9. Diagnosing residual plots

(a) **A1 linearity.** A U shape means the mean of $y$ bends while the fit is straight.

(b) **A3 homoscedasticity.** Spread proportional to the mean is the classic funnel.

(c) **A4 normality.** An S-shaped Q–Q plot means tails heavier or lighter than normal, not a wrong mean
structure.

(d) **A2 independence.** A trend in collection order means consecutive errors are correlated — a time effect,
not a curvature in $x$.

### 10. The normal equations by hand

*Strategy.* $X^{\mathsf{T}}X$ collects $n$, $\sum x$, $\sum x^2$; $X^{\mathsf{T}}\mathbf{y}$ collects $\sum y$,
$\sum xy$.

(a) $n=4$, $\sum x_i=10$, $\sum x_i^2=30$, $\sum y_i=19$, $\sum x_iy_i=2+8+15+32=57$. So

$$X^{\mathsf{T}}X=\begin{pmatrix}4&10\\10&30\end{pmatrix},\qquad
X^{\mathsf{T}}\mathbf{y}=\begin{pmatrix}19\\57\end{pmatrix}.$$

(b) The equations are $4b_0+10b_1=19$ and $10b_0+30b_1=57$. From the first,
$b_0=(19-10b_1)/4$. Substituting:

$$\frac{10(19-10b_1)}{4}+30b_1=57\ \Longrightarrow\ 47.5-25b_1+30b_1=57\ \Longrightarrow\ 5b_1=9.5\ \Longrightarrow\ b_1=1.9,$$

and then $b_0=(19-19)/4=0$. The fitted line is $\hat y=1.9x$.

(c) Fitted values $1.9,\,3.8,\,5.7,\,7.6$, so $\mathbf{e}=(0.1,\,0.2,\,-0.7,\,0.4)$.
$\mathbf{e}\cdot\mathbf{1}=0.1+0.2-0.7+0.4=0$ ✓ and
$\mathbf{e}\cdot\mathbf{x}=0.1+0.4-2.1+1.6=0$ ✓.

*Remark.* $\det(X^{\mathsf{T}}X)=4(30)-100=20>0$, so the system has a unique solution. In general
$\det(X^{\mathsf{T}}X)=nS_{xx}$; here $S_{xx}=30-100/4=5$ and $4(5)=20$. ✓

### 11. From $R^2$ to $r$

(a) $r=\pm\sqrt{0.64}=\pm0.8$; the slope is negative and $r$ has the sign of $b_1$ (both equal
$S_{xy}$ divided by positive quantities), so $r=-0.8$.

(b) $r=+\sqrt{0.09}=+0.3$.

(c) $R^2=r^2$ discards the sign, and it is also invariant to swapping $x$ and $y$ and to rescaling either
variable. Two data sets with identical $R^2$ can have opposite directions of association.

### 12. Leverage

(a) $h=1/21+(15-5)^2/400=0.047619+0.25=0.29762$.

(b) $h=1/21+0=0.047619$.

(c) The average leverage is $p/n=2/21=0.095238$, and the $2p/n$ rule gives a threshold of $0.19048$. Since
$0.29762>0.19048$, the observation at $x=15$ is high-leverage: it lies $10$ units from $\bar x$ against a
standard deviation of $x$ of about $\sqrt{S_{xx}/(n-1)}=\sqrt{20}=4.47$.

## Intermediate

### 13. Deriving the least-squares slope

(a) The first normal equation is $\sum_i(y_i-b_0-b_1x_i)=0$, i.e. $n\bar y-nb_0-nb_1\bar x=0$, so
$b_0=\bar y-b_1\bar x$.

(b) The second normal equation is $\sum_ix_iy_i-b_0\sum_ix_i-b_1\sum_ix_i^2=0$. Substitute $b_0$:

$$\sum_ix_iy_i-(\bar y-b_1\bar x)n\bar x-b_1\sum_ix_i^2=0 .$$

Using $n\bar x\bar y=\sum_ix_i\bar y$, this is
$\sum_ix_i(y_i-\bar y)-b_1\bigl(\sum_ix_i^2-n\bar x^2\bigr)=0$, that is $S_{xy}-b_1S_{xx}=0$, so
$b_1=S_{xy}/S_{xx}$.

(c) The Hessian of $Q$ is $\begin{pmatrix}2n&2\sum x_i\\2\sum x_i&2\sum x_i^2\end{pmatrix}$, with determinant
$4nS_{xx}>0$ and positive leading entry $2n$; the quadratic is therefore strictly convex and its unique
stationary point is the global minimum.

### 14. Why the residuals sum to zero — and when they do not

(a) $\sum_ie_i=\sum_i(y_i-b_0-b_1x_i)=n\bar y-nb_0-nb_1\bar x=n(\bar y-b_0-b_1\bar x)=0$, using
$b_0=\bar y-b_1\bar x$ from the first normal equation.

(b) By the second normal equation, $\sum_ix_ie_i=\sum_ix_i(y_i-b_0-b_1x_i)=0$ directly.

(c) Without an intercept, the objective is $\sum_i(y_i-b_1x_i)^2$, whose derivative $-2\sum_ix_i(y_i-b_1x_i)$
gives $b_1=\sum_ix_iy_i/\sum_ix_i^2$. Take $x=(1,2)$ and $y=(1,0)$: $b_1=1/5=0.2$, residuals are
$1-0.2=0.8$ and $0-0.4=-0.4$, and $\sum_ie_i=0.4\ne0$. The constraint $\sum_ie_i=0$ came from differentiating
with respect to the intercept; with no intercept there is no such equation.

### 15. $R^2=r^2$

(a) $\mathrm{SSR}=\sum_i(\hat y_i-\bar y)^2$. Since $\hat y_i-\bar y=b_1(x_i-\bar x)$, this is
$b_1^2\sum_i(x_i-\bar x)^2=b_1^2S_{xx}$.

(b) $b_1=S_{xy}/S_{xx}$ gives $b_1^2S_{xx}=S_{xy}^2/S_{xx}$.

(c) Hence $R^2=\mathrm{SSR}/\mathrm{SST}=\dfrac{S_{xy}^2}{S_{xx}S_{yy}}=\left(\dfrac{S_{xy}}{\sqrt{S_{xx}S_{yy}}}\right)^2=r^2$.
The step $\hat y_i-\bar y=b_1(x_i-\bar x)$ uses $b_0=\bar y-b_1\bar x$, which is exactly where the intercept
assumption enters; without it, $\hat y_i-\bar y=-\bar y+b_1x_i$, the expansion no longer collapses, and $R^2$
can even be negative.

### 16. A full inference table from two numbers

(a) $t=0.85/0.21=4.0476$ on $n-2=23$ degrees of freedom. Compare with $t_{23,0.975}=2.069$: since
$4.05>2.07$, reject $H_0\colon\beta_1=0$ at $\alpha=0.05$.

(b) $0.85\pm2.069(0.21)=0.85\pm0.43449=(0.4155,\,1.2845)$.

(c) $t=4.05$ lies between the $0.999$ and $0.9995$ quantiles of $t_{23}$, so the two-sided $p$-value is about
$0.0005$. Without software: the tail probability is roughly $2\Phi(-4.05)\approx2(0.00003)=0.00006$ in the
normal approximation, and the $t_{23}$ tail is heavier, so the true value is larger — a factor of about ten
here. Reading an approximate $p$ from a table of critical values and rounding is honest; quoting six decimals
from memory is not.

### 17. Confidence or prediction interval?

With $n=25$, $t_{23,0.975}=2.069$; $1/n=0.04$ and $(14-10)^2/500=0.032$.

(a) $\hat y_0=5+2(14)=33$.

(b) $\operatorname{se}=\ 3\sqrt{0.04+0.032}=3\sqrt{0.072}=3(0.268328)=0.80498$, so
$33\pm2.069(0.80498)=33\pm1.6655=(31.33,\,34.67)$.

(c) $\operatorname{se}=3\sqrt{1.072}=3(1.035374)=3.10612$, so
$33\pm2.069(3.10612)=33\pm6.4266=(26.57,\,39.43)$.

(d) Quote the **prediction interval**. The farmer is deciding about one future plot, not about the average of
all plots at $x_0$; a $95\%$ prediction interval has $95\%$ coverage for that single outcome, while the
confidence interval is $95\%$ only for the mean and would be badly too narrow for a single plot.

### 18. Arithmetic of a multiple regression

(a)

$$\mathbf{b}=\begin{pmatrix}0.4&-0.1&-0.05\\-0.1&0.05&0.01\\-0.05&0.01&0.02\end{pmatrix}
\begin{pmatrix}40\\60\\30\end{pmatrix}
=\begin{pmatrix}16-6-1.5\\-4+3+0.3\\-2+0.6+0.6\end{pmatrix}
=\begin{pmatrix}8.5\\-0.7\\-0.8\end{pmatrix}.$$

(b) The squared standard errors are $s^2$ times the diagonal entries:

$$\operatorname{se}(b_0)=\sqrt{4(0.4)}=1.2649,\qquad \operatorname{se}(b_1)=\sqrt{4(0.05)}=0.44721,\qquad
\operatorname{se}(b_2)=\sqrt{4(0.02)}=0.28284 .$$

(c) $t=-0.8/0.28284=-2.8284$ on $n-p=20-3=17$ degrees of freedom. With $t_{17,0.975}=2.110$,
$\lvert t\rvert=2.83>2.11$, so $b_2$ is significant at the $5\%$ level; the two-sided $p$-value is about
$0.0116$. Note the degrees of freedom: using $n-2$ or $n-1$ here would be wrong, because three parameters
were estimated.

### 19. Variance inflation

(a) $\operatorname{VIF}_1=1/(1-0.81)=1/0.19=5.2632$, and
$\sqrt{5.2632}=2.2942$: the standard error is $2.29$ times what it would be if $x_1$ were uncorrelated with
the other three.

(b) There are $4$ variance inflation factors, one per predictor, each from regressing that predictor on *all*
the others. A naive analyst regressing each predictor on one other predictor would compute $6$ pairwise
correlations, which measure pairwise collinearity only: a predictor can be almost perfectly predictable from
a *combination* of others while correlating modestly with each one individually. This is why VIFs are the
standard diagnostic.

(c) High VIFs do not damage predictions or fitted values (the model is only reparameterised), but they do
destroy the precision of individual coefficients and make their signs unstable.

### 20. Log–log model

(a) The elasticity is $b_1=0.62$: a $1\%$ increase in $x$ is associated with about a $0.62\%$ increase in $y$.

(b) $\ln y=2.30+0.62\ln 100=2.30+0.62(4.605170)=2.30+2.855205=5.155205$, so
$y=e^{5.155205}=173.33$.

(c) A $10\%$ increase in $x$ multiplies $y$ by $1.1^{0.62}=e^{0.62\ln1.1}=e^{0.059092}=1.06087$, i.e. about
$+6.09\%$.

(d) Because the model is linear in $\ln x$: the change in $\ln y$ for a given *proportional* change in $x$ is
the same at every level of $x$. That is what "constant elasticity" means, and it is the reason log–log models
are the default for multiplicative processes.

*Caution.* $173.33$ estimates the conditional median (under log-normal errors), not the mean.

### 21. Log–linear growth model

(a) Each additional hour multiplies the expected count by $e^{0.08}$: $b_1$ is a growth rate on the log scale.

(b) $e^{0.08}=1.08329$, so the count increases by about $8.33\%$ per hour.

(c) Doubling requires $e^{0.08T}=2$, i.e. $T=\ln2/0.08=0.693147/0.08=8.664$ hours.

(d) A linear model $y=b_0+b_1t$ asserts a constant *absolute* increase per hour; bacterial growth is
multiplicative, so the absolute increase accelerates. Fitting a line to exponentially growing counts
produces residuals that fan out and predicts absurd values in either direction. The log transform makes both
the mean structure and the variance structure approximately correct.

### 22. A quadratic fit

(a) $\mathrm{d}\hat y/\mathrm{d}x=4-x$, which vanishes at $x=4$; there
$\hat y=10+16-0.5(16)=10+16-8=18$. Since $\mathrm{d}^2\hat y/\mathrm{d}x^2=-1<0$, this is a maximum.

(b) At $x=2$: $4-2=2$. At $x=6$: $4-6=-2$.

(c) The marginal effect changes with $x$, so the curve rises, turns at $x=4$ and then falls. The coefficient
$4$ is the slope only at $x=0$; calling it "the effect of $x$" is wrong everywhere else. For a quadratic,
report the turning point and the marginal effect at the values of $x$ that matter.

### 23. Standardised residual and Cook's distance

(a) $r=\dfrac{5}{2.1\sqrt{1-0.4}}=\dfrac{5}{2.1(0.774597)}=\dfrac{5}{1.626653}=3.0738$. This exceeds $3$, a
strong indication that the point is unusual in $y$.

(b)

$$D=\frac{e^2}{ps^2}\cdot\frac{h}{(1-h)^2}=\frac{25}{2(4.41)}\cdot\frac{0.4}{0.36}=2.8345(1.1111)=3.1494 .$$

(c) Both. The standardised residual identifies it as an outlier in $y$, and $D=3.15>1$ identifies it as
influential: removing it would move the fitted surface substantially. High $h$ alone would not have been
enough — leverage without a large residual does not change the fit much — and a large residual at low
leverage *is* worth attention but moves the line less.

### 24. Adjusted $R^2$

(a) With $n=50$:

$$R^2_{\text{adj},1}=1-\frac{(1-0.72)(49)}{48}=1-0.285833=0.71417,$$
$$R^2_{\text{adj},2}=1-\frac{(1-0.75)(49)}{45}=1-0.272222=0.72778 .$$

(b) Model 2 is slightly better on adjusted $R^2$ ($0.728$ against $0.714$). That is weak evidence: we would
also want to know whether the three extra predictors are individually or jointly significant, whether they
were chosen before seeing the data, how the models perform out of sample, and whether the residual
diagnostics of model 2 are sound.

(c) Adding a predictor increases $R^2$ but also increases $p$, hence the penalty $(n-1)/(n-p)$. The gain in
$R^2$ is small for a useless predictor — on average it is $1/(n-1)$ per predictor under independence — while
the penalty is fixed at $(n-1)/(n-p)$, so $R^2_{\text{adj}}$ falls unless the new predictor earns its place.

## Advanced

### 25. The variance of the slope

(a) From §8.2, $b_1=\beta_1+\sum_ic_i\varepsilon_i$ with $c_i=(x_i-\bar x)/S_{xx}$.

(b) $\sum_ic_i=\frac{1}{S_{xx}}\sum_i(x_i-\bar x)=0$;
$\sum_ic_ix_i=\frac{1}{S_{xx}}\sum_i(x_i-\bar x)x_i=\frac{S_{xx}}{S_{xx}}=1$;
$\sum_ic_i^2=\frac{1}{S_{xx}^2}\sum_i(x_i-\bar x)^2=\frac{S_{xx}}{S_{xx}^2}=\frac{1}{S_{xx}}$.

(c) $\operatorname{Var}(b_1)=\operatorname{Var}\bigl(\sum_ic_i\varepsilon_i\bigr)=\sum_i\sum_jc_ic_j\operatorname{Cov}(\varepsilon_i,\varepsilon_j)$.
A2 makes the off-diagonal covariances zero, and A3 sets the diagonal ones to $\sigma^2$:

$$\operatorname{Var}(b_1)=\sigma^2\sum_ic_i^2=\frac{\sigma^2}{S_{xx}} .$$

Replacing $\sigma^2$ by its unbiased estimate $s^2$ gives $\operatorname{se}(b_1)=s/\sqrt{S_{xx}}$. A1 is
needed too, but only to make $\mathbb{E}[b_1]=\beta_1$; the variance calculation needs A2 and A3.

### 26. The analysis-of-variance identity

(a) With $d_i=\hat y_i-\bar y$ and $e_i=y_i-\hat y_i$, we have $y_i-\bar y=d_i+e_i$, hence

$$\sum_i(y_i-\bar y)^2=\sum_id_i^2+2\sum_id_ie_i+\sum_ie_i^2 .$$

(b) By §8.1, $d_i=b_1(x_i-\bar x)$ and both $\sum_ie_i=0$ and $\sum_ix_ie_i=0$, so

$$\sum_id_ie_i=b_1\sum_i(x_i-\bar x)e_i=b_1\Bigl(\sum_ix_ie_i-\bar x\sum_ie_i\Bigr)=b_1(0-0)=0 .$$

Therefore $\mathrm{SST}=\mathrm{SSR}+\mathrm{SSE}$.

(c) Take $x=(1,2)$, $y=(1,0)$ with no intercept. The optimum is $b_1=\sum x_iy_i/\sum x_i^2=1/5=0.2$, giving
$\hat y=(0.2,0.4)$, $\bar y=0.5$. Then $\mathrm{SST}=(-0.5)^2+(0.5)^2=0.5$,
$\mathrm{SSR}=(0.2-0.5)^2+(0.4-0.5)^2=0.09+0.01=0.10$, $\mathrm{SSE}=(0.8)^2+(-0.4)^2=0.64+0.16=0.80$.
Since $0.10+0.80=0.90\ne0.5$, the identity fails. (Here $R^2=\mathrm{SSR}/\mathrm{SST}=0.2$ is still between
$0$ and $1$, but with a different definition of $\mathrm{SST}$; some software uses
$1-\mathrm{SSE}/\sum y_i^2$ instead.)

### 27. Pythagoras for the projection

(a) $\hat{\mathbf{y}}\cdot\mathbf{e}=(H\mathbf{y})^{\mathsf{T}}(I-H)\mathbf{y}=\mathbf{y}^{\mathsf{T}}H^{\mathsf{T}}(I-H)\mathbf{y}$.
Since $H^{\mathsf{T}}=H$ and $H^2=H$, $H(I-H)=H-H^2=0$, so the inner product is $0$.

(b) Expanding the squared norm and using $\hat{\mathbf{y}}\cdot\mathbf{e}=0$,

$$\lVert\mathbf{y}\rVert^2=(\hat{\mathbf{y}}+\mathbf{e})\cdot(\hat{\mathbf{y}}+\mathbf{e})
=\lVert\hat{\mathbf{y}}\rVert^2+2\hat{\mathbf{y}}\cdot\mathbf{e}+\lVert\mathbf{e}\rVert^2
=\lVert\hat{\mathbf{y}}\rVert^2+\lVert\mathbf{e}\rVert^2 .$$

(c) The projection of $\mathbf{y}$ onto $\mathcal{M}$ is closer to $\mathbf{y}$ than any other point of
$\mathcal{M}$, and $\bar y\mathbf{1}\in\mathcal{M}$, so
$\lVert\hat{\mathbf{y}}\rVert^2\ge\lVert\bar y\mathbf{1}\rVert^2=n\bar y^2$ with equality only when the
predictor contributes nothing. Subtracting $n\bar y^2$ from the identity in (b) gives

$$\underbrace{\lVert\mathbf{y}\rVert^2-n\bar y^2}_{\mathrm{SST}}
=\underbrace{\bigl(\lVert\hat{\mathbf{y}}\rVert^2-n\bar y^2\bigr)}_{\mathrm{SSR}}+\underbrace{\lVert\mathbf{e}\rVert^2}_{\mathrm{SSE}},$$

which is $\mathrm{SST}=\mathrm{SSR}+\mathrm{SSE}$ because
$\lVert\hat{\mathbf{y}}\rVert^2-n\bar y^2=\lVert\hat{\mathbf{y}}-\bar y\mathbf{1}\rVert^2$ (the cross term
$\bar y\mathbf{1}\cdot(\hat{\mathbf{y}}-\bar y\mathbf{1})=0$ since $\mathbf{1}^{\mathsf{T}}\hat{\mathbf{y}}=n\bar y$).

### 28. Properties of the hat matrix

(a) $H^{\mathsf{T}}=[X(X^{\mathsf{T}}X)^{-1}X^{\mathsf{T}}]^{\mathsf{T}}=X[(X^{\mathsf{T}}X)^{-1}]^{\mathsf{T}}X^{\mathsf{T}}=H$
because $X^{\mathsf{T}}X$ is symmetric so its inverse is too. And
$H^2=X(X^{\mathsf{T}}X)^{-1}X^{\mathsf{T}}X(X^{\mathsf{T}}X)^{-1}X^{\mathsf{T}}=X(X^{\mathsf{T}}X)^{-1}X^{\mathsf{T}}=H$.

(b) Using the cyclic property $\operatorname{tr}(AB)=\operatorname{tr}(BA)$,

$$\operatorname{tr}H=\operatorname{tr}\bigl(X(X^{\mathsf{T}}X)^{-1}X^{\mathsf{T}}\bigr)
=\operatorname{tr}\bigl((X^{\mathsf{T}}X)^{-1}X^{\mathsf{T}}X\bigr)=\operatorname{tr}(I_p)=p .$$

(c) $h_{ii}$ is the $i$-th diagonal entry of $H$, so $\sum_ih_{ii}=\operatorname{tr}H=p$. For the bounds:
$H$ is a projection, so $\hat{\mathbf{y}}=H\mathbf{y}$ has $\lVert\hat{\mathbf{y}}\rVert\le\lVert\mathbf{y}\rVert$
for every $\mathbf{y}$; taking $\mathbf{y}$ to be the $i$-th standard basis vector gives
$h_{ii}=\lVert H\mathbf{e}_i\rVert^2\le1$, and $h_{ii}=\mathbf{e}_i^{\mathsf{T}}H^{\mathsf{T}}H\mathbf{e}_i=\lVert H\mathbf{e}_i\rVert^2\ge0$.

(d) For $X=[\mathbf{1}\ \ \mathbf{x}]$, the leverage of row $i$ is
$h_{ii}=\mathbf{x}_i^{\mathsf{T}}(X^{\mathsf{T}}X)^{-1}\mathbf{x}_i$ with $\mathbf{x}_i=(1,x_i)^{\mathsf{T}}$. In
centred coordinates, $(X^{\mathsf{T}}X)^{-1}=\operatorname{diag}(1/n,\,1/S_{xx})$, so
$h_{ii}=\frac{1}{n}+\frac{(x_i-\bar x)^2}{S_{xx}}$.

### 29. The prediction interval

(a) Since $b_0=\bar y-b_1\bar x$, $\hat y_0=b_0+b_1x_0=\bar y+b_1(x_0-\bar x)$. Also
$\operatorname{Cov}(\bar y,b_1)=0$ (§8.5), so

$$\operatorname{Var}(\hat y_0)=\operatorname{Var}(\bar y)+(x_0-\bar x)^2\operatorname{Var}(b_1)
=\frac{\sigma^2}{n}+\frac{(x_0-\bar x)^2\sigma^2}{S_{xx}} .$$

(b) $y_0-\hat y_0=\varepsilon_0-(\hat y_0-\beta_0-\beta_1x_0)$. The new error $\varepsilon_0$ is independent of
the sample, hence independent of $\hat y_0$ and of the estimation error; therefore the variance of the
difference is the sum:

$$\operatorname{Var}(y_0-\hat y_0)=\sigma^2+\sigma^2\Bigl(\frac1n+\frac{(x_0-\bar x)^2}{S_{xx}}\Bigr)
=\sigma^2\Bigl(1+\frac1n+\frac{(x_0-\bar x)^2}{S_{xx}}\Bigr).$$

(c) As $n\to\infty$ with the $x$-distribution fixed, $S_{xx}\to\infty$ and $\operatorname{Var}(\hat y_0)\to0$,
but $\operatorname{Var}(y_0-\hat y_0)\to\sigma^2$. The interval width therefore tends to
$2(1.96)\sigma$: the irreducible variability of a single observation. Estimating the mean perfectly does not
tell you what one individual will do.

### 30. Weighted least squares

(a) The objective is $(\mathbf{y}-X\boldsymbol\beta)^{\mathsf{T}}W(\mathbf{y}-X\boldsymbol\beta)$; its
gradient is $-2X^{\mathsf{T}}W(\mathbf{y}-X\boldsymbol\beta)$, which vanishes when
$X^{\mathsf{T}}WX\boldsymbol\beta=X^{\mathsf{T}}W\mathbf{y}$. With $W$ positive definite and $X$ of full
column rank, $X^{\mathsf{T}}WX$ is positive definite and invertible, so
$\mathbf{b}_W=(X^{\mathsf{T}}WX)^{-1}X^{\mathsf{T}}W\mathbf{y}$ is the unique minimiser.

(b) $\mathbf{b}_W=\boldsymbol\beta+(X^{\mathsf{T}}WX)^{-1}X^{\mathsf{T}}W\boldsymbol\varepsilon$, so

$$\operatorname{Var}(\mathbf{b}_W)=(X^{\mathsf{T}}WX)^{-1}X^{\mathsf{T}}W\operatorname{Var}(\boldsymbol\varepsilon)WX(X^{\mathsf{T}}WX)^{-1}
=\sigma^2(X^{\mathsf{T}}WX)^{-1},$$

because $\operatorname{Var}(\boldsymbol\varepsilon)=\sigma^2W^{-1}$.

(c) With one predictor and an intercept, the first normal equation gives
$b_{0,W}=\bar y_w-b_{1,W}\bar x_w$ where $\bar x_w=\sum w_ix_i/\sum w_i$ and likewise for $y$. Substituting
into the second gives

$$b_{1,W}=\frac{\sum_iw_i(x_i-\bar x_w)(y_i-\bar y_w)}{\sum_iw_i(x_i-\bar x_w)^2} .$$

If $\operatorname{sd}(\varepsilon_i)=\sigma x_i$, then $w_i=1/x_i^2$ and each observation is weighted by the
inverse of its own error variance — the observations that are noisiest in absolute terms count least. This is
exactly the generalised-least-squares principle: divide through the model by $x_i$ and the errors become
homoscedastic.

### 31. Variance inflation via Frisch–Waugh–Lovell

(a) Regress $\mathbf{x}_2$ on $\mathbf{x}_1$ (with intercept) and let $\tilde{\mathbf{x}}_2$ be the residual
vector; regress $\mathbf{y}$ likewise and let $\tilde{\mathbf{y}}$ be its residual. By §8.9,

$$b_2=\frac{\tilde{\mathbf{x}}_2^{\mathsf{T}}\tilde{\mathbf{y}}}{\tilde{\mathbf{x}}_2^{\mathsf{T}}\tilde{\mathbf{x}}_2}
=\frac{\tilde{\mathbf{x}}_2^{\mathsf{T}}\tilde{\mathbf{y}}}{\lVert\tilde{\mathbf{x}}_2\rVert^2}.$$

(b) $\lVert\tilde{\mathbf{x}}_2\rVert^2$ is the residual sum of squares from regressing $x_2$ on $x_1$,
which equals the total $S_{22}$ minus the part explained: $S_{22}(1-R^2)$ with $R^2=r_{12}^2$. Hence
$\lVert\tilde{\mathbf{x}}_2\rVert^2=S_{22}(1-r_{12}^2)$.

(c) Since $b_2$ is a fixed linear combination of the responses with coefficient vector
$\tilde{\mathbf{x}}_2/\lVert\tilde{\mathbf{x}}_2\rVert^2$,

$$\operatorname{Var}(b_2)=\sigma^2\frac{\lVert\tilde{\mathbf{x}}_2\rVert^2}{\lVert\tilde{\mathbf{x}}_2\rVert^4}
=\frac{\sigma^2}{\lVert\tilde{\mathbf{x}}_2\rVert^2}
=\frac{\sigma^2}{S_{22}(1-r_{12}^2)}=\operatorname{VIF}_2\cdot\frac{\sigma^2}{S_{22}} .$$

When $r_{12}=0.95$, $\operatorname{VIF}_2=1/(1-0.9025)=10.26$: the variance is ten times larger and the
standard error $3.20$ times larger than in an orthogonal design.

## Challenge

### 32. Omitted-variable bias

(a) The simple-regression slope computed on a sample satisfies
$b_1=\dfrac{\operatorname{Cov}_n(x_1,y)}{\operatorname{Var}_n(x_1)}$ in sample moments. Substituting the
true model $y=\beta_0+\beta_1x_1+\beta_2x_2+\varepsilon$:

$$\operatorname{Cov}_n(x_1,y)=\beta_1\operatorname{Var}_n(x_1)+\beta_2\operatorname{Cov}_n(x_1,x_2)+\operatorname{Cov}_n(x_1,\varepsilon).$$

Dividing by $\operatorname{Var}_n(x_1)$ gives
$b_1=\beta_1+\beta_2\frac{\operatorname{Cov}_n(x_1,x_2)}{\operatorname{Var}_n(x_1)}+\frac{\operatorname{Cov}_n(x_1,\varepsilon)}{\operatorname{Var}_n(x_1)}$.
As $n\to\infty$ the sample moments converge to their population counterparts and the last term vanishes under
A1, so $\operatorname{plim}b_1=\beta_1+\beta_2\delta$ with
$\delta=\operatorname{Cov}(x_1,x_2)/\operatorname{Var}(x_1)$, which is exactly the population slope of $x_2$
on $x_1$.

(b) No bias requires $\beta_2=0$ (the omitted variable does not matter) or $\delta=0$ (it is uncorrelated with
the included predictor). Neither is checkable from the sample: $\beta_2$ belongs to a model that was not
fitted, and $\delta=0$ in the sample does not prove $\delta=0$ in the population — and the sample correlation
is not evidence about the effect of a variable never recorded. This is why the argument for a regression must
come from design or theory, not from the fit.

(c) $\beta_1+\beta_2\delta=0.5+2(0.3)=1.1$: the estimate is biased upwards by $0.6$, more than doubling the
true slope. With $\delta=-0.5$ the bias is $2(-0.5)=-1.0$, so the estimate converges to $-0.5$ — the opposite
sign to the truth. A sign reversal is entirely possible with omitted-variable bias, which is why "the
coefficient has the wrong sign" is not a proof that a variable should be dropped.

### 33. Adding an irrelevant but correlated predictor

(a) Write the two-predictor model as $y=\beta_0+\beta_1x_1+\beta_2x_2+\varepsilon$ with $\beta_2=0$. By §8.8,
$\mathbb{E}[\mathbf{b}]=\boldsymbol\beta=(\beta_0,\beta_1,0)^{\mathsf{T}}$, so $b_1$ remains unbiased for
$\beta_1$ whatever the correlation between the predictors. Unbiasedness never depended on the extra variable.

(b) By §8.9 and §31, $\operatorname{Var}(b_1)=\sigma^2/(S_{11}(1-r^2))$ rather than $\sigma^2/S_{11}$; the
factor is $1/(1-r^2)=1/(1-0.49)=1.9608$. The standard error is inflated by $\sqrt{1.9608}=1.4003$.

(c) The extra predictor costs $40\%$ more variance in the coefficient of interest and one degree of freedom,
and buys nothing in bias — so on this analysis it is a pure loss. But the phrase "irrelevant" is a claim about
the population, which the analyst does not know. If $x_2$ is plausibly related to $y$ *and* is predictive of
$y$, including it reduces the residual variance $\sigma^2$ and can lower
$\operatorname{Var}(b_1)$ despite the inflation factor: the two effects compete. The practical rule is to
decide from subject-matter knowledge and from out-of-sample or adjusted criteria, not from the $t$-statistic
of the nuisance coefficient.

### 34. Cook's distance

(a) $e_i^2$ measures how far point $i$ lies from the fitted surface; $s^2$ scales it by the typical residual
size, so the first factor is a squared standardised residual (up to the $1-h_{ii}$ correction). The factor
$h_{ii}/(1-h_{ii})^2$ measures how much the fit at point $i$ depends on $y_i$: as $h_{ii}\to1$ the fitted value
reproduces $y_i$ almost exactly and the remaining data cannot discipline it, so a residual there implies a
large displacement.

(b) $\dfrac{16}{2(4)}\cdot\dfrac{0.5}{0.25}=2(2)=4$, well above the conventional threshold $1$: the point is
influential.

(c) The standardised residual is $r_i=e_i/(s\sqrt{1-h_{ii}})$, so $e_i^2=r_i^2s^2(1-h_{ii})$. Substituting:

$$D_i=\frac{r_i^2s^2(1-h_{ii})}{ps^2}\cdot\frac{h_{ii}}{(1-h_{ii})^2}=\frac{r_i^2}{p}\cdot\frac{h_{ii}}{1-h_{ii}} .$$

(d) For fixed $r_i$, $h/(1-h)$ increases in $h$ and tends to infinity as $h\to1$. So influence is largest at
high leverage, and in a small sample the largest leverage is automatically large ($h\ge p/n$, so with $n=10$
and $p=2$ the maximum leverage is at least $0.2$). A single unusual observation in a small study can
therefore determine the conclusion.

### 35. Measurement error in the predictor

(a) Write $y=\beta_0+\beta_1w+\bigl(\varepsilon-\beta_1u\bigr)$; the composite error is correlated with the
regressor $w$, because $\operatorname{Cov}(w,\varepsilon-\beta_1u)=-\beta_1\sigma_u^2\ne0$. Hence the
zero-correlation assumption fails and

$$\operatorname{plim}b_1=\frac{\operatorname{Cov}(w,y)}{\operatorname{Var}(w)}
=\frac{\beta_1\sigma_x^2}{\sigma_x^2+\sigma_u^2}=\beta_1\lambda,$$

using $\operatorname{Cov}(w,y)=\beta_1\operatorname{Var}(x)=\beta_1\sigma_x^2$ and
$\operatorname{Var}(w)=\sigma_x^2+\sigma_u^2$. The factor $\lambda\in(0,1]$ is the *reliability ratio*.

(b) $\operatorname{plim}b_1=2(0.8)=1.6$: the slope is attenuated by $20\%$ toward zero, and the distortion
does not vanish with more data.

(c) Error in $y$ inflates the residual variance but is uncorrelated with $x$, so the slope stays unbiased; only
the standard errors, $R^2$ and efficiency suffer. Asymmetry of the two cases is the reason a mismeasured
predictor is a serious problem and a mismeasured response is a mild one.

*Remark.* The bias is multiplicative, so it can never change the sign of a coefficient; it shrinks it.

### 36. $R^2$ when nothing is related

(a) Under bivariate normality with $\rho=0$, $R^2=r^2$ satisfies
$R^2\sim\operatorname{Beta}\!\left(\tfrac12,\tfrac{n-2}{2}\right)$. For a beta variable with parameters
$a,b$, the mean is $a/(a+b)$, so

$$\mathbb{E}[R^2]=\frac{\tfrac12}{\tfrac12+\tfrac{n-2}{2}}=\frac{1}{n-1} .$$

(b) For $n=20$: $1/19=0.0526$. For $n=200$: $1/199=0.00503$. A "respectable" $R^2$ of $0.05$ is exactly what
pure noise produces with twenty observations. Comparisons of $R^2$ across sample sizes are therefore
misleading unless the expected value under the null is taken into account.

(c) With $p-1$ independent predictors, $\mathbb{E}[R^2]=(p-1)/(n-1)$ under the null. That is precisely the
quantity $R^2_{\text{adj}}$ removes: since
$\mathbb{E}[1-R^2_{\text{adj}}]=\mathbb{E}[1-R^2]\frac{n-1}{n-p}=\frac{n-p}{n-1}\cdot\frac{n-1}{n-p}=1$,
the adjusted measure has expectation approximately $0$ when the predictors are useless, so it does not reward
adding columns.

*Simulation check.* Drawing $x$ and $y$ independently with $n=20$ and averaging $R^2$ over $20{,}000$ samples
gave $0.0528$, against the predicted $1/19=0.0526$. ✓
