# Linear Regression — Exercises

> [Linear Regression](README.md) · 36 problems · Beginner → Challenge · Solutions: [solutions.md](solutions.md)

Attempt each problem in writing before consulting [solutions.md](solutions.md). The problems are grouped by
level but numbered continuously; the section of the tutorial tested is given in italics.

**Conventions.** Unless stated otherwise the model has an intercept, $x$-values are treated as fixed, and
variances use divisor $n-1$ or $n-p$ as appropriate. Critical values: $t_{6}=2.447$, $t_{8}=2.306$,
$t_{9}=2.262$, $t_{18}=2.101$, $t_{20}=2.086$, $t_{23}=2.069$, $t_{25}=2.060$; $z_{0.975}=1.960$,
$z_{0.80}=0.8416$. Keep full precision during calculations and round final answers to four significant
figures; $\bar x$ and $\bar y$ are exact in these data.

## Beginner

**1.** *(§7.5)* A fitted model for wheat yield $y$ (kg per plot) against rainfall $x$ (mm) is
$\hat y=5.2+0.64x$, estimated from plots with $40\le x\le120$.

(a) Interpret $b_1$ in one sentence, including units.
(b) Interpret $b_0$, and say whether it should be reported as a finding.
(c) Predict the yield at $x=80$ mm.
(d) State two things this fit does not establish.

**2.** *(§7.3, §8.11)* A sample of $n=10$ gives $\sum x_i=50$, $\sum y_i=120$, $\sum x_i^2=310$ and
$\sum x_iy_i=700$.

(a) Compute $S_{xx}$ and $S_{xy}$.
(b) Compute $b_1$ and $b_0$.
(c) Verify that the fitted line passes through $(\bar x,\bar y)$.
(d) Verify $\sum_i e_i=0$ using only the fitted equation and the summary statistics.

**3.** *(§5.3, §7.2)* A line $\hat y=1.5+1.6x$ is fitted to the data below.

| $x$ | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| $y$ | 2.9 | 4.6 | 6.1 | 7.7 | 9.4 | 11.2 |

(a) Compute all six residuals.
(b) Compute $\mathrm{SSE}$.
(c) Compute $S_{yy}$ and hence $R^2$.
(d) Do the residuals suggest any systematic problem? Justify in one sentence.

**4.** *(§7.6)* A regression of $y$ on one predictor gives $\mathrm{SSR}=180$ and $\mathrm{SST}=250$.

(a) Compute $\mathrm{SSE}$ and $R^2$.
(b) Interpret $R^2$ in words, without using the word "explain".
(c) A colleague says "$R^2=0.72$, so the model is $72\%$ correct". Identify the error.

**5.** *(§7.8, §8.5)* A simple regression has $S_{xx}=250$ and residual standard error $s=4$.

(a) Compute $\operatorname{se}(b_1)$.
(b) Doubling every $x_i$ leaves the residuals unchanged. What happens to $S_{xx}$ and to
$\operatorname{se}(b_1)$, and by what factor?
(c) A second data set has the same $S_{xx}$ but twice as many observations, with the same accuracy per
observation. Without computing, say whether $\operatorname{se}(b_1)$ must fall. Explain.

**6.** *(§7.8)* For a regression with $n=20$ observations the estimate is $b_1=1.8$ with
$\operatorname{se}(b_1)=0.6$.

(a) Test $H_0\colon\beta_1=0$ against a two-sided alternative at $\alpha=0.05$.
(b) Give a $95\%$ confidence interval for $\beta_1$.
(c) State in one sentence what the interval means and, separately, what it does not mean.

**7.** *(§7.5)* A model for fuel use $y$ (litres per $100$ km) against temperature $x$ (°C) is
$\hat y=9.4-0.05x$.

(a) Interpret the slope with units.
(b) Rewrite the model with temperature measured in degrees Fahrenheit, using $t_{\mathrm{F}}=1.8t_{\mathrm{C}}+32$.
(c) Comment on how the interpretation of the new slope differs, and on which version a reader in the United
States would find easier to use.

**8.** *(§7.9)* A regression with $n=20$ has $s=4$, $\hat y_0=50$ and $(x_0-\bar x)^2/S_{xx}=0.05$ at a chosen
$x_0$.

(a) Compute a $95\%$ confidence interval for the mean response at $x_0$.
(b) Compute a $95\%$ prediction interval for a new observation at $x_0$.
(c) Explain the ratio of their widths.

**9.** *(§7.7)* Match each residual plot description to the assumption it most directly violates, choosing from
A1 linearity, A2 independence, A3 homoscedasticity and A4 normality.

(a) Residuals form a clean U shape when plotted against $\hat y$.
(b) The spread of residuals triples as $\hat y$ grows from $20$ to $80$.
(c) The Q–Q plot is an S shape: the middle is straight, both tails bend away.
(d) Residuals plotted against the order of collection drift upwards for the first half and downwards for the
second half.

**10.** *(§7.4, §8.8)* The design matrix is $X=\begin{pmatrix}1&1\\1&2\\1&3\\1&4\end{pmatrix}$ and
$\mathbf{y}=(2,4,5,8)^{\mathsf{T}}$.

(a) Compute $X^{\mathsf{T}}X$ and $X^{\mathsf{T}}\mathbf{y}$.
(b) Solve $X^{\mathsf{T}}X\mathbf{b}=X^{\mathsf{T}}\mathbf{y}$.
(c) Verify $\mathbf{e}\cdot\mathbf{1}=0$ and $\mathbf{e}\cdot\mathbf{x}=0$.

**11.** *(§7.6, §8.4)* For a simple regression, $R^2=0.64$ and the estimated slope is negative.

(a) Find the sample correlation $r$.
(b) Find $r$ if instead $R^2=0.09$ and the slope is positive.
(c) Explain why $R^2$ alone cannot tell you the sign of the relationship.

**12.** *(§7.13)* A simple regression has $n=21$, $\bar x=5$ and $S_{xx}=400$.

(a) Compute the leverage of the observation with $x=15$.
(b) Compute the leverage of the observation with $x=5$.
(c) Compute the average leverage and say, with a reason, whether the point $x=15$ is high-leverage by the
$2p/n$ rule.

## Intermediate

**13.** *(§7.3)* Derive $b_1=S_{xy}/S_{xx}$ starting from the two normal equations.

(a) Solve the first normal equation for $b_0$ in terms of $b_1$, $\bar x$ and $\bar y$.
(b) Substitute into the second and show that $b_1S_{xx}=S_{xy}$.
(c) Explain why the solution is a minimum and not a maximum or saddle point.

**14.** *(§8.1)* Let $b_0,b_1$ minimise $\sum_i(y_i-b_0-b_1x_i)^2$ with $S_{xx}>0$.

(a) Prove $\sum_i e_i=0$.
(b) Prove $\sum_i x_ie_i=0$.
(c) Show that (a) fails for the model with no intercept, by exhibiting a small data set where
$\sum_i(y_i-b_1x_i)\ne0$ at the no-intercept optimum.

**15.** *(§8.4)* Prove that for simple linear regression with an intercept, $R^2=r^2$.

(a) Express $\mathrm{SSR}$ in terms of $b_1$ and $S_{xx}$.
(b) Substitute $b_1=S_{xy}/S_{xx}$ and simplify.
(c) Deduce the result and state where the intercept assumption was used.

**16.** *(§7.8)* A regression with $n=25$ gives $b_1=0.85$ and $\operatorname{se}(b_1)=0.21$.

(a) Compute the $t$ statistic and compare it with the correct critical value.
(b) Compute a $95\%$ confidence interval.
(c) Give a rough two-sided $p$-value and explain how you obtained it without software.

**17.** *(§7.9)* A simple regression uses $n=25$ observations with $\bar x=10$, $S_{xx}=500$, $s=3$,
$b_0=5$ and $b_1=2$. Interest centres on $x_0=14$.

(a) Compute $\hat y_0$.
(b) Compute a $95\%$ confidence interval for the mean response at $x_0$.
(c) Compute a $95\%$ prediction interval for a new observation at $x_0$.
(d) Which interval would you quote to a farmer deciding whether to apply the treatment at $x_0$, and why?

**18.** *(§7.10, §8.8)* A multiple regression has
$(X^{\mathsf{T}}X)^{-1}=\begin{pmatrix}0.4&-0.1&-0.05\\-0.1&0.05&0.01\\-0.05&0.01&0.02\end{pmatrix}$,
$X^{\mathsf{T}}\mathbf{y}=(40,60,30)^{\mathsf{T}}$ and $s^2=4$.

(a) Compute $\mathbf{b}$.
(b) Compute the three standard errors.
(c) Compute the $t$ statistic for $b_2=-0.8$ and comment, given that there are $n=20$ observations and
$p=3$ parameters.

**19.** *(§7.11)* A multiple regression has four predictors besides the intercept.

(a) Regressing $x_1$ on the other three predictors gives $R_1^2=0.81$. Compute $\operatorname{VIF}_1$ and the
factor by which $\operatorname{se}(b_1)$ is inflated.
(b) How many variance inflation factors are there in this model, and how many would a naive analyst compute
by regressing each predictor on only one other predictor?
(c) Name one consequence of high VIFs that affects predictions and one that does not.

**20.** *(§7.12)* A fitted model is $\ln y=2.30+0.62\ln x$.

(a) State the elasticity and interpret it.
(b) Predict $y$ at $x=100$.
(c) By what percentage does the model predict $y$ changes when $x$ increases by $10\%$?
(d) Explain why the answer to (c) does not depend on the level of $x$.

**21.** *(§7.12)* A fitted model for bacterial count is $\ln y=4.1+0.08t$, with $t$ in hours.

(a) Interpret $0.08$.
(b) Compute the multiplicative change per hour.
(c) Compute the doubling time.
(d) Explain why a linear model for $y$ would have been inappropriate here.

**22.** *(§7.12)* A quadratic fit is $\hat y=10+4x-0.5x^2$.

(a) Find the value of $x$ at which $\hat y$ is largest, and the corresponding $\hat y$.
(b) Compute the marginal effect $\mathrm{d}\hat y/\mathrm{d}x$ at $x=2$ and at $x=6$.
(c) Explain what the change of sign means and why it makes the linear coefficient alone uninterpretable.

**23.** *(§7.13)* For one observation $e=5$, $s=2.1$ and $h=0.4$; the model has $p=2$ parameters.

(a) Compute the standardised residual.
(b) Compute Cook's distance.
(c) Would you describe the point as an outlier, an influential point, both or neither? Justify.

**24.** *(§7.6)* Two models are fitted to the same $n=50$ observations. Model 1 has one predictor and
$R^2=0.72$; model 2 has four predictors and $R^2=0.75$.

(a) Compute $R^2_{\text{adj}}$ for both.
(b) Which model do you prefer on this evidence, and what else would you want to know?
(c) Explain why $R^2_{\text{adj}}$ can decrease when a predictor is added even though $R^2$ cannot.

## Advanced

**25.** *(§8.5)* Prove that $\operatorname{Var}(b_1)=\sigma^2/S_{xx}$ under A1–A3, and deduce
$\operatorname{se}(b_1)$.

(a) Write $b_1=\sum_i c_iy_i$ and identify $c_i$.
(b) Verify $\sum_ic_i=0$, $\sum_ic_ix_i=1$ and $\sum_ic_i^2=1/S_{xx}$.
(c) Compute the variance and explain where A2 and A3 enter.

**26.** *(§8.3)* Prove $\mathrm{SST}=\mathrm{SSR}+\mathrm{SSE}$ for a model with an intercept.

(a) Expand $\sum_i(y_i-\bar y)^2$ with $y_i-\bar y=(\hat y_i-\bar y)+(y_i-\hat y_i)$.
(b) Show the cross term vanishes, quoting the results you need from §8.1.
(c) Show by explicit counterexample that the identity can fail without an intercept.

**27.** *(§7.4)* Let $\hat{\mathbf{y}}=H\mathbf{y}$ be the least-squares projection and
$\mathbf{e}=(I-H)\mathbf{y}$.

(a) Show $\hat{\mathbf{y}}\cdot\mathbf{e}=0$.
(b) Deduce $\lVert\mathbf{y}\rVert^2=\lVert\hat{\mathbf{y}}\rVert^2+\lVert\mathbf{e}\rVert^2$.
(c) Explain why $\lVert\hat{\mathbf{y}}\rVert^2\ge n\bar y^2$ and how this yields the analysis-of-variance
identity.

**28.** *(§7.13)* For the hat matrix $H=X(X^{\mathsf{T}}X)^{-1}X^{\mathsf{T}}$ of a model with $p$
parameters and full column rank:

(a) prove $H^{\mathsf{T}}=H$ and $H^2=H$;
(b) prove $\operatorname{tr}H=p$;
(c) deduce $\sum_ih_{ii}=p$ and explain why $0\le h_{ii}\le1$;
(d) show that in simple regression $h_{ii}=\frac1n+\frac{(x_i-\bar x)^2}{S_{xx}}$.

**29.** *(§8.7)* Derive the prediction-interval variance and explain its limit.

(a) Show $\hat y_0=\bar y+b_1(x_0-\bar x)$ and hence
$\operatorname{Var}(\hat y_0)=\sigma^2\left(\frac1n+\frac{(x_0-\bar x)^2}{S_{xx}}\right)$, quoting the
covariance you need.
(b) Argue that $\operatorname{Var}(y_0-\hat y_0)=\sigma^2+\operatorname{Var}(\hat y_0)$, stating the
independence assumption used.
(c) Explain why the prediction interval does not shrink to zero as $n\to\infty$.

**30.** *(§7.10)* Weighted least squares fits $\boldsymbol\beta$ by minimising
$\sum_i w_i(y_i-\mathbf{x}_i^{\mathsf{T}}\boldsymbol\beta)^2$ with known weights $w_i>0$.

(a) Show the minimiser is $\mathbf{b}_W=(X^{\mathsf{T}}WX)^{-1}X^{\mathsf{T}}W\mathbf{y}$ with
$W=\operatorname{diag}(w_1,\dots,w_n)$.
(b) Show $\operatorname{Var}(\mathbf{b}_W)=\sigma^2(X^{\mathsf{T}}WX)^{-1}$ when
$\operatorname{Var}(\varepsilon_i)=\sigma^2/w_i$.
(c) In simple regression, deduce $b_{1,W}=\sum_iw_i(x_i-\bar x_w)(y_i-\bar y_w)/\sum_iw_i(x_i-\bar x_w)^2$
with weighted means, and explain why weighting by $1/x_i^2$ is natural when the error standard deviation is
proportional to $x_i$.

**31.** *(§8.9)* Use the Frisch–Waugh–Lovell theorem to derive $\operatorname{Var}(b_j)$ in a multiple
regression with two predictors $x_1,x_2$.

(a) Apply the theorem to $x_2$, writing $b_2$ as a ratio of residual sums of squares.
(b) Show that the residual sum of squares of $x_2$ after regressing on $x_1$ equals
$S_{22}(1-r_{12}^2)$.
(c) Deduce $\operatorname{VIF}_2=1/(1-r_{12}^2)$ and interpret the case $r_{12}=0.95$.

## Challenge

**32.** *(§7.14)* The true model is $y=\beta_0+\beta_1x_1+\beta_2x_2+\varepsilon$ but an analyst regresses
$y$ on $x_1$ alone.

(a) Show that $\operatorname{plim}b_1=\beta_1+\beta_2\delta$ where $\delta$ is the slope of the population
regression of $x_2$ on $x_1$, namely $\delta=\operatorname{Cov}(x_1,x_2)/\operatorname{Var}(x_1)$.
(b) State the two conditions under which the simple-regression slope is unbiased for $\beta_1$, and explain
why neither can be checked from the sample alone.
(c) Evaluate the bias when $\beta_1=0.5$, $\beta_2=2$ and $\delta=0.3$, and say what happens to the sign of
the estimate if $\delta=-0.5$.

**33.** *(§7.10, §7.11)* An analyst adds to a regression a predictor that is, in the population, unrelated to
$y$ but correlated with the existing predictor at $r=0.70$.

(a) Show that the estimator remains unbiased.
(b) Show that the variance of the original coefficient is inflated by the factor $1/(1-r^2)$, and evaluate it.
(c) Explain the practical advice that follows, and connect it to the idea of an "irrelevant variable" that is
nevertheless worth controlling for when it reduces error variance.

**34.** *(§7.13)* Cook's distance for observation $i$ is
$D_i=\frac{e_i^2}{ps^2}\cdot\frac{h_{ii}}{(1-h_{ii})^2}$.

(a) Explain each factor and why the second one measures leverage.
(b) Compute $D_i$ for $e=4$, $h=0.5$, $s=2$, $p=2$.
(c) Show that $D_i$ can be written in terms of the standardised residual
$r_i=e_i/(s\sqrt{1-h_{ii}})$ as $D_i=\frac{r_i^2}{p}\cdot\frac{h_{ii}}{1-h_{ii}}$.
(d) For which $h_{ii}$ is $D_i$ largest, given a fixed standardised residual, and what does this say about
small data sets?

**35.** *(§7.14)* Suppose the predictor is measured with error: we observe $w_i=x_i+u_i$ with
$u_i\perp\!\!\!\perp x_i$, $\mathbb{E}[u_i]=0$, $\operatorname{Var}(u_i)=\sigma_u^2$, while the model is
$y_i=\beta_0+\beta_1x_i+\varepsilon_i$.

(a) Argue that regressing $y$ on $w$ estimates $\beta_1\frac{\sigma_x^2}{\sigma_x^2+\sigma_u^2}$.
(b) Evaluate this when $\beta_1=2$ and the reliability ratio is $0.8$.
(c) Explain why measurement error in $y$ does not bias the slope in the same way, and what it does do.

**36.** *(§7.6, §8.4)* Under independence of $x$ and $y$, $R^2$ is not zero in a sample: it has a
distribution.

(a) State the distribution of $R^2$ in simple regression under bivariate normality and independence, and
derive $\mathbb{E}[R^2]$.
(b) Evaluate $\mathbb{E}[R^2]$ for $n=20$ and for $n=200$, and comment on what this implies for comparing
$R^2$ across sample sizes.
(c) Explain the corresponding result for a regression with $p-1$ independent predictors, and why it motivates
$R^2_{\text{adj}}$.
