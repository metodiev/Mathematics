# Financial Mathematics

> [Applied Mathematics](../README.md) · Level: Advanced · Prerequisites: [Exponential and Logarithmic Functions](../../03-algebra/12-exponential-and-logarithmic-functions/README.md), [Sequences and Series in Calculus](../../07-calculus/11-sequences-and-series-in-calculus/README.md), [Applications of Derivatives](../../07-calculus/05-applications-of-derivatives/README.md), [Expectation and Variance](../../10-probability/05-expectation-and-variance/README.md), [Matrices](../../08-linear-algebra/02-matrices/README.md), [Optimization](../../18-optimization/README.md), [Linear Regression](../../11-statistics/04-linear-regression/README.md) · Estimated time: 540 min

## 1. Introduction

Finance is the mathematics of exchanging money across time and across states of the world. A euro
today is not the same object as a euro tomorrow: it can be invested, so a claim to a future euro is
worth less than a euro in hand. A euro in a boom is not the same as a euro in a recession: the former is
abundant when it is least needed. **Financial mathematics** turns those two observations into
quantitative statements about prices, returns and risk.

The subject rests on two principles. The **time value of money** says that cash flows at different dates
must be compared through discounting. The **no-arbitrage principle** says that two portfolios with
identical future payoffs must have the same price today; otherwise a riskless profit is available. The
first principle gives present value, annuities, mortgages and bond pricing. The second gives option
pricing, the binomial model and the Black–Scholes formula.

The historical development is short but intense. Louis Bachelier modelled stock prices with Brownian
motion in 1900, five years before Einstein's work on Brownian motion. Irving Fisher formalised present
value and the real rate of interest. Harry Markowitz introduced mean–variance portfolio theory in 1952.
Sharpe, Lintner and Mossin developed the capital asset pricing model in the 1960s. Fischer Black, Myron
Scholes and Robert Merton produced the option-pricing formula in 1973, the same year the Chicago Board
Options Exchange opened. The formula turned derivatives from gambling into engineering, and it also
demonstrated how quickly a beautiful model can be mistaken for a guarantee.

This tutorial develops the standard toolkit with derivations: interest conventions, present and future
value, annuities and mortgages, risk and expected utility, portfolio theory and the CAPM, bond pricing
and duration, put–call parity, the binomial model and Black–Scholes. Every numerical example states its
compounding convention. The final sections are deliberately critical: a model is a description, not a
promise, and the assumptions that make Black–Scholes tractable are exactly the assumptions that fail in
a crisis.

## 2. Prerequisites

* **Exponentials and logarithms** — compounding, continuous growth and the natural log:
  [Exponential and Logarithmic Functions](../../03-algebra/12-exponential-and-logarithmic-functions/README.md).
* **Sequences and series** — geometric series and present-value sums:
  [Sequences and Series in Calculus](../../07-calculus/11-sequences-and-series-in-calculus/README.md).
* **Derivatives and optimisation** — first-order conditions, concavity, constrained optimisation:
  [Applications of Derivatives](../../07-calculus/05-applications-of-derivatives/README.md),
  [Optimization](../../18-optimization/README.md).
* **Probability and expectation** — random variables, expectation, variance, covariance:
  [Expectation and Variance](../../10-probability/05-expectation-and-variance/README.md).
* **Matrices** — covariance matrices, quadratic forms and systems:
  [Matrices](../../08-linear-algebra/02-matrices/README.md).
* **Linear regression** — the CAPM is a regression of excess returns on the market:
  [Linear Regression](../../11-statistics/04-linear-regression/README.md).

No stochastic calculus is assumed. The Black–Scholes formula is stated and derived by the risk-neutral
expectation method, with the normality of log returns proved from the model; the corresponding partial
differential equation is stated and interpreted. Readers who want the full continuous-time theory should
continue with stochastic calculus after this topic.

## 3. Learning Objectives

After working through this tutorial you will be able to:

1. Convert between simple, discrete-compound, nominal, effective and continuous interest rates.
2. Compute present and future values of cash-flow streams and explain why the discount rate matters.
3. Derive the annuity, perpetuity and mortgage formulas from geometric series.
4. Construct an amortisation schedule and compute an outstanding mortgage balance.
5. Define holding-period returns, arithmetic and geometric means, volatility and the Sharpe ratio.
6. Explain expected utility, risk aversion, certainty equivalence and the Arrow–Pratt measure.
7. Compute the expected return and variance of a portfolio and derive the minimum-variance portfolio.
8. Describe the efficient frontier, diversification and two-fund separation.
9. Derive the CAPM from the tangency condition and interpret beta and alpha.
10. Price a coupon bond, compute Macaulay and modified duration, and approximate price changes with
    duration and convexity.
11. State and prove put–call parity, and derive the one-period binomial price by replication.
12. State the Black–Scholes formula and its assumptions, and explain why no-arbitrage forces prices.
13. Articulate the limitations of these models and avoid presenting them as guarantees.

## 4. Intuition

**Time value.** If you lend €100 for a year at 5%, you receive €105. The €100 today and the €105 in a
year are equivalent *at that rate*. Discounting reverses the comparison: €105 in a year is worth €100
today. The interest rate is an exchange rate between dates.

**Compounding.** Interest earns interest. At 5% annually, €100 grows to €105 after one year, then to
€110.25 after two: the second year's interest is earned on the first year's interest as well. The
frequency of compounding determines how often that reinvestment happens. Continuous compounding is the
limit of infinitely frequent compounding and gives the cleanest formulas.

**Present value.** A project is worth the sum of its future cash flows, each discounted at the
opportunity cost of capital. If that sum exceeds the cost, the project creates value. The internal rate
of return is the discount rate at which the sum equals the cost; it is a summary of the project, not a
measure of its size.

**Risk.** A return is a random variable. Its mean measures reward, its variance or standard deviation
measures dispersion. Most people dislike dispersion, so a risky asset must offer a higher expected
return than a safe one to be held. Expected utility makes that trade-off precise: a concave utility
function makes the certain equivalent of a gamble less than its expected value.

**Diversification.** Combining assets whose returns are imperfectly correlated reduces portfolio
variance without reducing expected return proportionally. The limit of diversification is the average
covariance, not zero: systematic risk remains. The efficient frontier is the set of portfolios that offer
the highest expected return for each level of variance.

**CAPM.** If all investors hold the same efficient portfolio, the market portfolio is that portfolio.
Then the only risk that commands a premium is covariance with the market. The CAPM summarises this in a
single number, beta, and a linear relation between expected excess return and beta.

**Bonds.** A bond is a loan with scheduled coupons and principal. Its price is the present value of those
cash flows at the market yield. Duration is the present-value-weighted average time to the cash flows, a
measure of sensitivity to yield changes; convexity corrects the approximation for larger moves.

**Options.** An option is a right, not an obligation. A call pays off when the underlying rises, a put
when it falls. The payoff is asymmetric, so its price is not the discounted expected payoff under the
real-world distribution alone; replication and risk-neutral pricing pin it down. No-arbitrage is the
engine: if a portfolio of stock and bond replicates the option, the option must cost the same as that
portfolio.

**A warning.** Every result below is conditional on assumptions. Models are disciplined estimates, not
guarantees; the 1998 failure of Long-Term Capital Management and the 2008 financial crisis are reminders
that model risk is real.

## 5. Formal Definition

### 5.1 Cash flows and interest

**Definition 5.1 (Cash-flow stream).** A cash-flow stream is a finite or infinite sequence
$(C_0,C_1,\dots,C_T)$ where $C_t$ is the cash amount received at date $t$, measured in a common
currency. Outflows are negative, inflows positive.

**Definition 5.2 (Simple interest).** At a constant simple rate $r$ per period, a principal $P$ grows to
$$A(t)=P(1+rt).$$
Interest is paid only on the original principal.

**Definition 5.3 (Compound interest).** At a nominal annual rate $r$ compounded $m$ times per year, a
principal $P$ grows after $t$ years to
$$A(t)=P\Bigl(1+\frac{r}{m}\Bigr)^{mt}.$$
The **effective annual rate** is $r_{\mathrm{eff}}=(1+r/m)^m-1$.

**Definition 5.4 (Continuous compounding).** At a continuously compounded annual rate $r$,
$$A(t)=Pe^{rt}.$$
The **force of interest** is $\delta=r$, and more generally
$\delta(t)=\dfrac{d}{dt}\ln A(t)$.

### 5.2 Present and future value

**Definition 5.5 (Discount factor and present value).** At a per-period rate $r$, the discount factor for
$t$ periods is $v^t=(1+r)^{-t}$. The present value of a cash-flow stream is
$$\mathrm{PV}=\sum_{t=0}^{T}\frac{C_t}{(1+r)^t}.$$
The future value at $T$ is $\mathrm{FV}=\mathrm{PV}\,(1+r)^T$.

**Definition 5.6 (Net present value and internal rate of return).** For an investment with initial
outlay $C_0<0$ and subsequent cash flows $C_1,\dots,C_T$,
$$\mathrm{NPV}(r)=C_0+\sum_{t=1}^{T}\frac{C_t}{(1+r)^t}.$$
The **internal rate of return** (IRR) is a rate $\rho$ with $\mathrm{NPV}(\rho)=0$. The NPV rule accepts
a project when $\mathrm{NPV}(r)>0$ at the opportunity cost $r$.

### 5.3 Annuities and mortgages

**Definition 5.7 (Annuity).** An **ordinary annuity** pays a constant amount $C$ at the end of each of
$n$ periods. Its present value at rate $r$ is
$$\mathrm{PV}=C\frac{1-(1+r)^{-n}}{r},$$
and its future value at the end of period $n$ is
$$\mathrm{FV}=C\frac{(1+r)^n-1}{r}.$$
An **annuity due** pays at the beginning of each period, so its value is $(1+r)$ times the ordinary
annuity. A **perpetuity** pays $C$ forever and has value $C/r$ when $r>0$; a growing perpetuity with
growth $g<r$ has value $C_1/(r-g)$, where $C_1$ is next period's payment.

**Definition 5.8 (Mortgage).** A mortgage of principal $L$ at per-period rate $r$ repaid in $n$ equal
installments $M$ has
$$M=\frac{Lr}{1-(1+r)^{-n}}.$$
The balance after $k$ payments is
$$B_k=L(1+r)^k-M\frac{(1+r)^k-1}{r}.$$

### 5.4 Returns and expected utility

**Definition 5.9 (Holding-period return).** For an asset with price $P_{t-1}$ and dividend $D_t$, the
holding-period return over period $t$ is
$$R_t=\frac{P_t+D_t-P_{t-1}}{P_{t-1}}.$$
The **geometric mean return** over $T$ periods is
$\bigl(\prod_{t=1}^{T}(1+R_t)\bigr)^{1/T}-1$; the **arithmetic mean** is $\frac1T\sum_tR_t$.

**Definition 5.10 (Expected utility and risk aversion).** A von Neumann–Morgenstern utility function
$u$ assigns utility to wealth. A decision maker is **risk averse** if $u$ is concave, **risk neutral** if
$u$ is linear, and **risk seeking** if $u$ is convex. The **certainty equivalent** $CE$ of a random
wealth $\tilde W$ satisfies
$$u(CE)=\mathbb{E}[u(\tilde W)],$$
and the **risk premium** is $\pi=\mathbb{E}[\tilde W]-CE$. The **Arrow–Pratt absolute risk aversion** is
$$A(w)=-\frac{u''(w)}{u'(w)}.$$

### 5.5 Portfolios

**Definition 5.11 (Portfolio return and variance).** A portfolio with weights $w_i$ summing to $1$ has
expected return
$$\mu_p=\sum_iw_i\mu_i$$
and variance
$$\sigma_p^2=\sum_i\sum_jw_iw_j\sigma_{ij},$$
where $\sigma_{ij}=\operatorname{Cov}(R_i,R_j)$ and $\sigma_{ii}=\sigma_i^2$. For two assets,
$$\sigma_p^2=w^2\sigma_1^2+(1-w)^2\sigma_2^2+2w(1-w)\rho\sigma_1\sigma_2,$$
with $\rho=\sigma_{12}/(\sigma_1\sigma_2)$.

**Definition 5.12 (Efficient frontier).** A portfolio is **mean–variance efficient** if no other
portfolio has a higher expected return with the same or lower variance. The set of such portfolios is the
**efficient frontier**. With a risk-free asset, the frontier becomes a straight line through the
risk-free rate, tangent to the risky frontier.

### 5.6 Bonds

**Definition 5.13 (Coupon bond).** A bond with face value $F$, annual coupon $c$, maturity $n$ and
yield to maturity $y$ has price
$$P=\sum_{t=1}^{n}\frac{cF}{(1+y)^t}+\frac{F}{(1+y)^n}.$$
If coupons are paid $m$ times per year, use the per-period yield $y/m$, $mn$ periods and coupon $cF/m$.

**Definition 5.14 (Duration and convexity).** The **Macaulay duration** is
$$D=\sum_{t=1}^{n}t\,\frac{\mathrm{PV}(CF_t)}{P},$$
the present-value-weighted average time to the cash flows. The **modified duration** is
$D^*=D/(1+y)$ for annual compounding. For a small yield change $\Delta y$,
$$\frac{\Delta P}{P}\approx-D^*\Delta y+\frac12C_{\mathrm{conv}}(\Delta y)^2,$$
where $C_{\mathrm{conv}}$ is the convexity.

### 5.7 Options and no-arbitrage

**Definition 5.15 (European option).** A European call on a stock with price $S_t$ gives the right to buy
at strike $K$ at maturity $T$; its payoff is $(S_T-K)^+=\max(S_T-K,0)$. A European put gives the right to
sell; its payoff is $(K-S_T)^+$. An American option may be exercised at any time up to $T$.

**Definition 5.16 (Arbitrage).** An arbitrage is a trading strategy with zero initial cost, non-negative
payoff in every state, and a strictly positive payoff in at least one state. A market is **arbitrage
free** if no such strategy exists.

**Definition 5.17 (Replicating portfolio and risk-neutral pricing).** A portfolio replicates a claim if
its payoff equals the claim's payoff in every state. In a complete arbitrage-free market the claim's
price equals the cost of any replicating portfolio. Equivalently, there is a **risk-neutral probability
measure** $\mathbb{Q}$ under which
$$\text{price}_0=e^{-rT}\mathbb{E}^{\mathbb{Q}}[\text{payoff}_T].$$

### 5.8 The binomial and Black–Scholes models

**Definition 5.18 (One-period binomial model).** A stock price $S$ moves to $Su$ or $Sd$ with $u>1>d$
over one period, while a risk-free bond grows by $R=1+r$. A claim with payoffs $C_u,C_d$ has the
replicating price
$$C=\frac{1}{R}\bigl[qC_u+(1-q)C_d\bigr],\qquad q=\frac{R-d}{u-d},$$
provided $d<R<u$.

**Definition 5.19 (Black–Scholes model).** Under the Black–Scholes assumptions, the price of a European
call is
$$C=S_0\Phi(d_1)-Ke^{-rT}\Phi(d_2),$$
and the price of a European put is
$$P=Ke^{-rT}\Phi(-d_2)-S_0\Phi(-d_1),$$
where
$$d_1=\frac{\ln(S_0/K)+(r+\sigma^2/2)T}{\sigma\sqrt T},\qquad d_2=d_1-\sigma\sqrt T,$$
and $\Phi$ is the standard normal cumulative distribution function.

## 6. Mathematical Notation

| Symbol | Read as | Meaning |
|---|---|---|
| $P$, $A(t)$ | principal, accumulated value | amount at time $t$ |
| $r$ | interest rate | per period unless stated |
| $m$ | compounding frequency | periods per year |
| $\delta$ | force of interest | continuous rate, $\delta=\ln(1+r)$ |
| $v^t$ | discount factor | $(1+r)^{-t}$ |
| $C_t$ | cash flow at $t$ | positive inflow or negative outflow |
| $\mathrm{NPV}$, $\mathrm{IRR}$ | net present value, internal rate of return | project criteria |
| $C$, $M$ | annuity payment, mortgage installment | constant periodic payment |
| $L$, $B_k$ | loan principal, balance after $k$ | mortgage variables |
| $R_t$ | holding-period return | $(P_t+D_t-P_{t-1})/P_{t-1}$ |
| $\mu$, $\sigma$ | mean, standard deviation | expected return, volatility |
| $\rho$ | correlation | $\sigma_{12}/(\sigma_1\sigma_2)$ |
| $u$, $CE$, $\pi$ | utility, certainty equivalent, risk premium | expected utility |
| $A(w)$ | absolute risk aversion | $-u''(w)/u'(w)$ |
| $w_i$ | portfolio weight | fraction invested in asset $i$ |
| $\beta_i$ | beta | $\sigma_{iM}/\sigma_M^2$ |
| $F$, $c$, $y$ | face value, coupon rate, yield | bond variables |
| $D$, $D^*$ | Macaulay, modified duration | interest-rate sensitivity |
| $S_t$, $K$, $T$ | stock price, strike, maturity | option variables |
| $\sigma$ | volatility | standard deviation of log returns |
| $\Phi$, $\phi$ | standard normal CDF, PDF | Black–Scholes |
| $\Delta$, $\Gamma$ | delta, gamma | option Greeks |

## 7. Core Concepts

### 7.1 Compounding conventions

The same quoted rate means different things under different conventions. For a principal of €1 held for
one year:

| Convention | Accumulated value | Effective annual rate |
|---|---|---|
| Simple, annual rate $r$ | $1+r$ | $r$ |
| Annual compounding | $1+r$ | $r$ |
| $m$ times per year | $(1+r/m)^m$ | $(1+r/m)^m-1$ |
| Continuous | $e^r$ | $e^r-1$ |

The effective annual rate is the annually compounded rate that produces the same accumulation:
$$1+r_{\mathrm{eff}}=\Bigl(1+\frac{r}{m}\Bigr)^m.$$
As $m\to\infty$, $\bigl(1+r/m\bigr)^m\to e^r$, so continuous compounding is the limit of ever more
frequent compounding. The continuous rate equivalent to an effective annual rate $r_{\mathrm{eff}}$ is
$\delta=\ln(1+r_{\mathrm{eff}})$.

**Always state the convention.** "6%" is ambiguous: 6% simple, 6% nominal compounded monthly, and 6%
continuously compounded give different effective rates (6%, 6.168%, and 6.184% respectively). A nominal
rate without a compounding frequency is not a well-defined price of money. The same care applies to
APR/APY, day-count conventions (actual/365, 30/360), and the difference between nominal and real rates:
$$1+i_{\mathrm{nominal}}=(1+i_{\mathrm{real}})(1+\pi),$$
so $i_{\mathrm{real}}\approx i_{\mathrm{nominal}}-\pi$ for small inflation $\pi$.

### 7.2 Present value, NPV and IRR

A cash flow $C_t$ at date $t$ has present value $C_t(1+r)^{-t}$ at the per-period discount rate $r$. The
present value of a stream is the sum; the future value at $T$ is the present value multiplied by
$(1+r)^T$. Discounting is linear, so present values of separate projects add.

**NPV and IRR.** The NPV rule accepts a project when
$$\mathrm{NPV}(r)=C_0+\sum_{t=1}^{T}\frac{C_t}{(1+r)^t}>0.$$
The IRR is a root of $\mathrm{NPV}(\rho)=0$. For a conventional project (one sign change in the cash
flows), there is at most one positive IRR and, when it exists, the rule "accept if IRR $>r$" agrees with
the NPV rule. For non-conventional cash flows there may be several IRRs or none, and the IRR can rank
projects incorrectly when their scales or durations differ. NPV is the primary criterion; IRR is a
summary.

**Real versus nominal.** Discount nominal cash flows at a nominal rate and real cash flows at a real
rate. Mixing them is a common and expensive error. If cash flows grow with inflation, the real rate
$i_{\mathrm{real}}=(1+i_{\mathrm{nominal}})/(1+\pi)-1$ is the correct discount rate for real cash flows.

### 7.3 Annuities and perpetuities

For an ordinary annuity of $C$ per period for $n$ periods, with $v=(1+r)^{-1}$,
$$\mathrm{PV}=C(v+v^2+\cdots+v^n)=Cv\frac{1-v^n}{1-v}
=C\frac{1-(1+r)^{-n}}{r}.$$
The future value at the end of period $n$ is $\mathrm{PV}(1+r)^n=C\bigl((1+r)^n-1\bigr)/r$. An annuity
due multiplies both by $1+r$ because every payment is one period earlier.

Letting $n\to\infty$ in the present-value formula gives the perpetuity value $C/r$ when $r>0$. A growing
perpetuity with next payment $C_1$ and growth $g<r$ has value $C_1/(r-g)$; a growing annuity with $n$
payments has value
$$C_1\frac{1-\bigl(\frac{1+g}{1+r}\bigr)^n}{r-g}.$$
With continuous compounding, a continuous payment stream at rate $C$ per year for $T$ years has present
value
$$\int_0^T Ce^{-rt}\,dt=C\frac{1-e^{-rT}}{r}.$$
Both formulas tend to $CT$ as $r\to0$; for positive $r$ they differ because of the timing of payments
within the year.

### 7.4 Mortgages and amortisation

A mortgage is an annuity from the lender's point of view: the lender pays $L$ today and receives $M$ at
the end of each of $n$ periods. Setting the present value of the payments equal to the loan gives
$$L=M\frac{1-(1+r)^{-n}}{r}
\quad\Longrightarrow\quad
M=\frac{Lr}{1-(1+r)^{-n}}.$$
Here $r$ is the **per-period** rate. A nominal annual rate of 4.5% compounded monthly means
$r=0.045/12=0.00375$ and $n=12\times30=360$ for a 30-year mortgage.

The amortisation recursion is
$$B_k=B_{k-1}(1+r)-M,\qquad B_0=L.$$
Interest in period $k$ is $rB_{k-1}$, principal repayment is $M-rB_{k-1}$, and the balance falls slowly
at first because most of the early payment is interest. Solving the recursion gives
$$B_k=L(1+r)^k-M\frac{(1+r)^k-1}{r}.$$
The total interest paid is $nM-L$. Fees, insurance and taxes are not in $M$; the **APR** includes them
and is therefore higher than the nominal mortgage rate.

### 7.5 Continuous compounding and the force of interest

If the accumulation function is $A(t)$, the force of interest is
$$\delta(t)=\frac{d}{dt}\ln A(t)=\frac{A'(t)}{A(t)}.$$
For a constant $\delta$, $A(t)=A(0)e^{\delta t}$; for a time-varying force,
$$A(T)=A(0)\exp\Bigl(\int_0^T\delta(t)\,dt\Bigr).$$
The continuously compounded rate equivalent to an effective annual rate $i$ is $\delta=\ln(1+i)$.
Continuous discounting uses $e^{-\delta T}$, and a continuous annuity has present value
$C(1-e^{-\delta T})/\delta$. Continuous compounding is convenient for derivatives because it makes
discounting and growth symmetric in the exponent.

### 7.6 Risk and return

For an asset with price $P_{t-1}$ and dividend $D_t$, the holding-period return is
$R_t=(P_t+D_t-P_{t-1})/P_{t-1}$. Over $T$ periods, the geometric mean return is
$$\bar R_{\mathrm{geo}}=\Bigl(\prod_{t=1}^{T}(1+R_t)\Bigr)^{1/T}-1,$$
while the arithmetic mean is $\bar R_{\mathrm{arith}}=\frac1T\sum_tR_t$. The geometric mean is the
constant per-period return that compounds to the same terminal wealth; it is the correct measure of
realised performance. The arithmetic mean is always at least the geometric mean, with equality only when
all returns are equal. For small returns and volatility $\sigma$, the gap is approximately
$\sigma^2/2$ — the **volatility drag**.

The sample variance of returns is $s^2=\frac{1}{T-1}\sum_t(R_t-\bar R)^2$, and the sample standard
deviation $s$ is the **volatility**. The **Sharpe ratio** of a portfolio with expected return $\mu_p$ and
volatility $\sigma_p$ is
$$\mathrm{SR}=\frac{\mu_p-r_f}{\sigma_p},$$
the excess expected return per unit of volatility. It is a slope, not a probability, and it is meaningful
only when the risk-free rate and the horizon are specified.

### 7.7 Expected utility and risk aversion

A von Neumann–Morgenstern utility $u$ ranks lotteries by expected utility. If $u$ is concave, Jensen's
inequality gives
$$\mathbb{E}[u(\tilde W)]\le u(\mathbb{E}[\tilde W]),$$
so the certain equivalent $CE$ defined by $u(CE)=\mathbb{E}[u(\tilde W)]$ satisfies
$CE\le\mathbb{E}[\tilde W]$. The risk premium is $\pi=\mathbb{E}[\tilde W]-CE\ge0$. A risk-neutral
decision maker has linear $u$ and $\pi=0$; a risk-seeking one has convex $u$ and $\pi<0$.

The **Arrow–Pratt** measure $A(w)=-u''(w)/u'(w)$ quantifies local risk aversion. For a small zero-mean
gamble with variance $\sigma^2$, a second-order Taylor expansion gives
$$\pi\approx\frac12A(w)\sigma^2.$$
Two standard families are **CRRA** utility $u(w)=w^{1-\gamma}/(1-\gamma)$ for $\gamma\ne1$ (with
$u(w)=\ln w$ at $\gamma=1$), for which $A(w)=\gamma/w$, and **CARA** utility
$u(w)=-e^{-\alpha w}$, for which $A(w)=\alpha$. CRRA implies that the share of wealth invested in a
risky asset is independent of wealth; CARA implies that the euro amount is independent of wealth. Neither
is literally true, which is why the choice of utility function is a modelling decision, not a fact.

### 7.8 Portfolio theory

For two assets with weights $w$ and $1-w$,
$$\mu_p=w\mu_1+(1-w)\mu_2,\qquad
\sigma_p^2=w^2\sigma_1^2+(1-w)^2\sigma_2^2+2w(1-w)\rho\sigma_1\sigma_2.$$
Differentiating the variance and setting the derivative to zero gives the **minimum-variance weight**
$$w^*=\frac{\sigma_2^2-\rho\sigma_1\sigma_2}{\sigma_1^2+\sigma_2^2-2\rho\sigma_1\sigma_2}.$$
When $\rho<1$, the minimum variance is below the weighted average of the individual variances: this is
**diversification**. When $\rho=-1$, a zero-variance portfolio exists at
$w=\sigma_2/(\sigma_1+\sigma_2)$; when $\rho=1$, the variance is a perfect square and no diversification
benefit remains.

Plotting $(\sigma_p,\mu_p)$ as $w$ varies traces a hyperbola in the $\sigma$–$\mu$ plane. The upper branch
is the **efficient frontier** of risky assets. With a risk-free asset at rate $r_f$, the efficient
frontier becomes the straight line through $(0,r_f)$ tangent to the risky frontier; the tangency
portfolio maximises the Sharpe ratio. Every efficient portfolio is a combination of the risk-free asset
and the tangency portfolio — **two-fund separation**.

With $N$ assets, $\mu_p=w^{\mathsf T}\mu$ and $\sigma_p^2=w^{\mathsf T}\Sigma w$, where $\Sigma$ is the
covariance matrix. The efficient frontier minimises $w^{\mathsf T}\Sigma w$ subject to
$w^{\mathsf T}\mu=\bar\mu$ and $w^{\mathsf T}\mathbf 1=1$. If all assets have equal variance $\sigma^2$
and pairwise correlation $\rho$, an equally weighted portfolio has
$\sigma_p^2=\sigma^2/N+(1-1/N)\rho\sigma^2\to\rho\sigma^2$: diversification removes idiosyncratic risk
but not the common component.

### 7.9 The capital asset pricing model

The CAPM assumes that investors have mean–variance preferences, share the same beliefs about means and
covariances, can borrow and lend at the risk-free rate, and face no taxes or transaction costs. Under
these assumptions every investor holds the same tangency portfolio; in equilibrium that portfolio is the
**market portfolio**.

**Derivation outline.** Consider a portfolio with weight $w$ in asset $i$ and $1-w$ in the market. Its
mean and standard deviation satisfy
$$\mu_p=w\mu_i+(1-w)\mu_M,\qquad
\sigma_p^2=w^2\sigma_i^2+(1-w)^2\sigma_M^2+2w(1-w)\sigma_{iM}.$$
At $w=0$,
$$\frac{d\mu_p}{dw}=\mu_i-\mu_M,\qquad
\frac{d\sigma_p}{dw}=\frac{\sigma_{iM}-\sigma_M^2}{\sigma_M}.$$
The market portfolio is on the efficient frontier, so the marginal trade-off between risk and return at
$w=0$ equals the slope of the capital market line:
$$\frac{\mu_i-\mu_M}{(\sigma_{iM}-\sigma_M^2)/\sigma_M}
=\frac{\mu_M-r_f}{\sigma_M}.$$
Rearranging gives the **security market line**
$$\mu_i-r_f=\beta_i(\mu_M-r_f),\qquad
\beta_i=\frac{\sigma_{iM}}{\sigma_M^2}.$$
The intercept $\alpha_i=\mu_i-[r_f+\beta_i(\mu_M-r_f)]$ measures the excess return not explained by
market exposure; in the CAPM, $\alpha_i=0$ for every asset.

Beta measures **systematic risk**, the part of an asset's variability that moves with the market.
Idiosyncratic risk can be diversified away and commands no premium. The CAPM is a regression of excess
returns on the market excess return, which is why [Linear Regression](../../11-statistics/04-linear-regression/README.md)
is a prerequisite. Empirically, the relation is noisy, betas are unstable, and the model is rejected in
many samples; the Fama–French factors and Roll's critique are standard references. The CAPM remains a
useful benchmark, not a complete description of asset prices.

### 7.10 Bond pricing and duration

A coupon bond's price is the present value of its coupons and face value at the yield to maturity. If
the coupon rate equals the yield, the bond trades at par; if the coupon is above the yield, it trades at
a premium; if below, at a discount. For a zero-coupon bond, $P=F(1+y)^{-n}$.

**Duration.** Differentiating the price with respect to $y$,
$$\frac{dP}{dy}=-\sum_{t=1}^{n}t\,\frac{CF_t}{(1+y)^{t+1}}
=-\frac{D}{1+y}P,$$
so the **modified duration** $D^*=D/(1+y)$ satisfies
$$\frac{dP}{P}\approx-D^*\,dy.$$
Macaulay duration is a weighted average of the times at which cash flows arrive, with weights equal to
their shares of present value. A zero-coupon bond has $D=n$; a level perpetuity has $D=(1+y)/y$. Higher
coupons and shorter maturities reduce duration.

**Convexity.** The second-order term is
$$C_{\mathrm{conv}}=\frac{1}{P}\sum_{t=1}^{n}\frac{t(t+1)CF_t}{(1+y)^{t+2}},$$
and
$$\frac{\Delta P}{P}\approx-D^*\Delta y+\frac12C_{\mathrm{conv}}(\Delta y)^2.$$
Convexity is positive for ordinary bonds, so the price gain from a yield fall exceeds the loss from an
equal rise. **Immunisation** matches the duration of assets and liabilities; matching both duration and
convexity reduces residual interest-rate risk further. Credit risk, liquidity and the term structure of
interest rates are separate matters; a single yield to maturity is itself a simplification.

### 7.11 Options and put–call parity

A European call pays $(S_T-K)^+$ at maturity; a European put pays $(K-S_T)^+$. The call's payoff is
unbounded above, the put's is bounded above by $K$, and both are convex functions of $S_T$.

**Theorem 7.1 (Put–call parity).** For European options on a non-dividend-paying stock,
$$C-P=S_0-Ke^{-rT}.$$

*Proof.* Compare two portfolios:

* Portfolio A: one European call plus cash $Ke^{-rT}$.
* Portfolio B: one European put plus one share.

At maturity $T$, Portfolio A is worth $(S_T-K)^++K=\max(S_T,K)$. Portfolio B is worth
$(K-S_T)^++S_T=\max(K,S_T)$. The payoffs are identical in every state, so no-arbitrage forces the
initial values to be equal:
$$C+Ke^{-rT}=P+S_0,$$
which rearranges to the identity. $\blacksquare$

The parity is a *static replication* statement: the two portfolios have the same payoff, so they must
have the same price. It holds for European options; for American options the corresponding inequality is
$S_0-K\le C-P\le S_0-Ke^{-rT}$. With a continuous dividend yield $q$, the parity becomes
$$C-P=S_0e^{-qT}-Ke^{-rT}.$$

**Bounds.** From parity and the non-negativity of option prices,
$$\max(S_0-Ke^{-rT},0)\le C\le S_0,\qquad
\max(Ke^{-rT}-S_0,0)\le P\le Ke^{-rT}.$$
An American call on a non-dividend-paying stock is never exercised early: exercising gives $S_0-K$, while
selling the call gives at least $S_0-Ke^{-rT}>S_0-K$ when $r>0$ and $T>0$. Hence the American call has
the same value as the European call. Early exercise of an American put can be optimal because the
strike received on exercise earns interest.

### 7.12 The binomial model

**One period.** A stock $S$ moves to $Su$ or $Sd$ with $u>1>d$; a bond grows by $R=1+r$. To replicate a
claim with payoffs $C_u,C_d$, hold $\Delta$ shares and $B$ in the bond:
$$\Delta Su+BR=C_u,\qquad \Delta Sd+BR=C_d.$$
Subtracting gives
$$\Delta=\frac{C_u-C_d}{S(u-d)},$$
and substituting back gives
$$B=\frac{uC_d-dC_u}{(u-d)R}.$$
The no-arbitrage price is the cost of the replicating portfolio:
$$C=\Delta S+B=\frac1R\Bigl[qC_u+(1-q)C_d\Bigr],\qquad
q=\frac{R-d}{u-d}.$$
The number $q$ is the **risk-neutral probability**; it makes the expected stock return under $\mathbb{Q}$
equal to the risk-free rate:
$qSu+(1-q)Sd=RS$. It is a pricing device, not a forecast.

**Multiple periods.** Repeat the one-period calculation backwards through the tree. With $n$ periods,
$\Delta t=T/n$, the Cox–Ross–Rubinstein choice
$$u=e^{\sigma\sqrt{\Delta t}},\qquad d=e^{-\sigma\sqrt{\Delta t}},\qquad
q=\frac{e^{r\Delta t}-d}{u-d}$$
matches the variance of log returns to first order in $\Delta t$. As $n\to\infty$ with $\Delta t=T/n$,
the binomial price converges to the Black–Scholes price (Exercise 34). The binomial model is also the
simplest setting in which to see the replication argument: the option is redundant because stock and
bond can reproduce it.

### 7.13 The Black–Scholes formula

Assume the stock follows the geometric Brownian motion
$$dS_t=\mu S_t\,dt+\sigma S_t\,dW_t,$$
the risk-free rate $r$ and volatility $\sigma$ are constant, there are no dividends, taxes or transaction
costs, trading is continuous, and short selling and borrowing are unrestricted. Then the price of a
European call is
$$C=S_0\Phi(d_1)-Ke^{-rT}\Phi(d_2),$$
with
$$d_1=\frac{\ln(S_0/K)+(r+\sigma^2/2)T}{\sigma\sqrt T},\qquad
d_2=d_1-\sigma\sqrt T.$$
The put price follows from put–call parity. The formula can be read as the cost of a replicating
portfolio: $\Phi(d_1)$ shares financed by borrowing $Ke^{-rT}\Phi(d_2)$. It is also the discounted
risk-neutral expectation of the payoff, because under $\mathbb{Q}$,
$$S_T=S_0\exp\bigl((r-\sigma^2/2)T+\sigma\sqrt T\,Z\bigr),\qquad Z\sim\mathcal N(0,1).$$

**The PDE.** A no-arbitrage argument on a delta-hedged portfolio gives the Black–Scholes partial
differential equation
$$\frac{\partial V}{\partial t}+\frac12\sigma^2S^2\frac{\partial^2V}{\partial S^2}
+rS\frac{\partial V}{\partial S}-rV=0,$$
with the terminal condition $V(S,T)=(S-K)^+$ for a call. The drift $\mu$ does not appear: two assets with
different expected returns but the same volatility have the same option price, because the option can be
hedged. This is the clearest expression of the no-arbitrage principle in continuous time.

**Greeks.** Delta $\partial V/\partial S=\Phi(d_1)$ for a call; gamma
$\partial^2V/\partial S^2=\phi(d_1)/(S\sigma\sqrt T)$; vega
$\partial V/\partial\sigma=S\phi(d_1)\sqrt T$; theta is the time decay; rho is sensitivity to $r$.
Delta-hedging means holding $\Phi(d_1)$ shares against a short call; in continuous time the hedge is
perfect, and in discrete time it leaves hedging error proportional to gamma and the square of the price
move.

**Implied volatility.** Inverting the formula for $\sigma$ given a market price gives the implied
volatility. If the model were exactly true, implied volatility would be constant across strikes and
maturities. In practice it varies, producing the **volatility smile** or **skew**: the market prices
tail risk differently from the lognormal model.

### 7.14 Why no-arbitrage forces prices

The **law of one price** says that two assets or portfolios with identical payoffs in every state must
have the same price. If they did not, buy the cheaper and sell the dearer: the initial cash flow is
positive and the future payoff is zero in every state, an arbitrage.

In a finite-state market, the **fundamental theorem of asset pricing** states that the market is
arbitrage free if and only if there exists a strictly positive probability measure $\mathbb{Q}$ under
which every traded asset's discounted price is a martingale. Prices are then discounted risk-neutral
expectations. The measure need not be unique; uniqueness corresponds to **completeness**, the property
that every claim can be replicated. The binomial model is complete; Black–Scholes is the continuous-time
limit of a complete market.

No-arbitrage does not say that the price is the "true" value or that the expected return under the
real-world measure is zero. It says that any two ways of producing the same payoff must cost the same.
That is enough to pin down derivative prices relative to the underlying and the bond, and it is why the
real-world drift cancels.

### 7.15 Model limitations

**Assumptions are false.** Constant volatility, lognormal returns, continuous trading, no transaction
costs, unlimited borrowing and short selling, and a constant risk-free rate are all approximations.
Returns have fat tails, skewness and volatility clustering; jumps occur; liquidity disappears in
stress.

**Volatility is not constant.** The volatility smile shows that a single $\sigma$ cannot fit all
strikes. Stochastic volatility, local volatility and jump models extend Black–Scholes, but each adds
parameters that are hard to estimate and unstable.

**Hedging is discrete.** Delta hedging rebalances at discrete intervals; the residual error depends on
gamma and the path. In a gap or a crash, the hedge cannot be adjusted at the assumed price. This is
**gap risk**.

**Parameters and markets.** $\mu$ and $\sigma$ are unknown and time-varying; a small error in
volatility changes the price materially, and expected returns are notoriously hard to estimate. Taxes,
transaction costs, bid–ask spreads, short-sale constraints, funding costs and counterparty credit risk
all matter, and correlations rise in crises. Diversification is not independence. **Gap risk** — the
inability to rebalance at the assumed price — is real.

**The CAPM is not the world.** Beta is estimated with error, the market portfolio is unobservable (Roll's
critique), and the cross-section of expected returns is influenced by size, value, momentum and
profitability. The CAPM is a benchmark, not a guarantee.

**The lesson.** A model is a disciplined way to organise assumptions and compute implications. It is not
a promise. Use models with explicit assumptions, stress-test them, report ranges rather than point
estimates, and never present a model output as a guaranteed outcome.

## 8. Formulas and Properties

| Quantity | Formula | Convention |
|---|---|---|
| Simple accumulation | $P(1+rt)$ | simple, per period |
| Compound accumulation | $P(1+r/m)^{mt}$ | nominal $r$, $m$ times/year |
| Continuous accumulation | $Pe^{rt}$ | continuous |
| Effective annual rate | $(1+r/m)^m-1$ | from nominal $r$ |
| Present value | $\sum_t C_t(1+r)^{-t}$ | per-period $r$ |
| Annuity PV | $C\dfrac{1-(1+r)^{-n}}{r}$ | ordinary, end-of-period |
| Annuity FV | $C\dfrac{(1+r)^n-1}{r}$ | ordinary |
| Perpetuity | $C/r$ | $r>0$ |
| Growing perpetuity | $C_1/(r-g)$ | $g<r$ |
| Mortgage payment | $\dfrac{Lr}{1-(1+r)^{-n}}$ | per-period $r$ |
| Portfolio variance | $w^{\mathsf T}\Sigma w$ | weights sum to 1 |
| Minimum-variance weight | $\dfrac{\sigma_2^2-\rho\sigma_1\sigma_2}{\sigma_1^2+\sigma_2^2-2\rho\sigma_1\sigma_2}$ | two assets |
| CAPM | $\mu_i=r_f+\beta_i(\mu_M-r_f)$ | one-factor |
| Bond price | $\sum_t cF(1+y)^{-t}+F(1+y)^{-n}$ | annual coupons |
| Modified duration | $D/(1+y)$ | annual yield |
| Price change | $\Delta P/P\approx-D^*\Delta y+\tfrac12C_{\mathrm{conv}}(\Delta y)^2$ | small yield change |
| Put–call parity | $C-P=S_0-Ke^{-rT}$ | European, no dividends |
| Binomial price | $\frac1R[qC_u+(1-q)C_d]$ | $q=(R-d)/(u-d)$ |
| Black–Scholes call | $S_0\Phi(d_1)-Ke^{-rT}\Phi(d_2)$ | European, no dividends |
| Black–Scholes put | $Ke^{-rT}\Phi(-d_2)-S_0\Phi(-d_1)$ | European, no dividends |

## 9. Step-by-Step Examples

### 9.1 Compounding conventions compared

Invest €10,000 for 10 years at a quoted annual rate of 6%, with the convention stated in each row:

| Convention | Calculation | Accumulated value |
|---|---|---|
| Simple interest | $10{,}000(1+0.06\cdot10)$ | €16,000.00 |
| Annual compounding | $10{,}000(1.06)^{10}$ | €17,908.48 |
| Semiannual, nominal 6% | $10{,}000(1.03)^{20}$ | €18,061.11 |
| Monthly, nominal 6% | $10{,}000(1.005)^{120}$ | €18,193.97 |
| Continuous, 6% | $10{,}000e^{0.60}$ | €18,221.19 |

The monthly convention has effective annual rate $(1.005)^{12}-1=6.1678\%$; the continuous equivalent
is $e^{0.06}-1=6.1837\%$. Simple interest is €2,221.19 below continuous compounding. Each entry
discounts back to €10,000 under its own convention, so the differences are genuine prices of time, not
arithmetic errors. ✓

### 9.2 A 30-year mortgage

A mortgage of €250,000 charges a nominal annual rate of 4.5% compounded monthly over 30 years, so
$r=0.00375$ per month and $n=360$.

**Payment.** By the annuity formula,
$$M=\frac{250{,}000\cdot0.00375}{1-(1.00375)^{-360}}=\text{€}1{,}266.71.$$
Total payments are $360(1{,}266.71)=\text{€}456{,}016.78$; total interest is €206,016.78. In month 1 interest is
$250{,}000(0.00375)=\text{€}937.50$, principal is €329.21, and the balance is €249,670.79: early payments are
mostly interest. After $k=120$,
$$B_{120}=250{,}000(1.00375)^{120}-1{,}266.71\frac{(1.00375)^{120}-1}{0.00375}
=\text{€}200{,}223.59,$$
so only about €49,776 of principal has been repaid after one third of the term. The effective annual rate
is $(1.00375)^{12}-1=4.594\%$; fees would raise the APR further. ✓

### 9.3 Expected utility and the risk premium

An investor has wealth €100,000 and utility $u(w)=\ln w$; she faces a 50/50 gamble of $\pm$€10,000.
Then
$$\mathbb{E}[u(\tilde W)]=\tfrac12\ln(90{,}000)+\tfrac12\ln(110{,}000)
=\ln\sqrt{90{,}000\cdot110{,}000}=\ln(99{,}498.74),$$
so the certainty equivalent is €99,498.74 and the risk premium is €501.26. Since $u'(w)=1/w$ and
$u''(w)=-1/w^2$, the Arrow–Pratt measure is $A(w)=1/w=10^{-5}$. The small-gamble approximation gives
$\pi\approx\tfrac12A(w)\sigma^2=\tfrac12(10^{-5})(10^8)=\text{€}500$, close to the exact €501.26. The investor
would pay about €501 to avoid the gamble. ✓

### 9.4 A two-asset portfolio and the efficient frontier

Asset 1 has $\mu_1=10\%$, $\sigma_1=20\%$; asset 2 has $\mu_2=6\%$, $\sigma_2=10\%$; correlation
$\rho=0.2$.

**A 60/40 portfolio.** $\mu_p=0.6(10)+0.4(6)=8.4\%$, and
$\sigma_p^2=0.36(0.04)+0.16(0.01)+2(0.6)(0.4)(0.2)(0.2)(0.1)=0.01792$, so $\sigma_p=13.39\%$.

**Minimum variance.** By the formula,
$$w^*=\frac{0.01-0.2(0.2)(0.1)}{0.04+0.01-2(0.2)(0.2)(0.1)}
=\frac{0.006}{0.042}=\frac17.$$
At $w=1/7$, $\mu_p=6.571\%$ and $\sigma_p=9.562\%$, below the volatility of either asset: this is
diversification. As $w$ ranges over $[0,1]$, the $(\sigma,\mu)$ points trace a hyperbola; its upper branch
is the efficient frontier.

**Risk-free asset.** With $r_f=3\%$, maximising the Sharpe ratio gives $w\approx0.3867$,
$\mu_p=7.547\%$, $\sigma_p=10.789\%$ and $\mathrm{SR}=0.4214$. Every efficient portfolio combines the
risk-free asset with this tangency portfolio (two-fund separation). ✓

### 9.5 The CAPM in one numerical example

Suppose $\operatorname{Cov}(R_i,R_M)=0.0216$, $\operatorname{Var}(R_M)=0.0144$, $r_f=2\%$ and
$\mathbb{E}[R_M]=9\%$. Then $\beta_i=0.0216/0.0144=1.5$, and the security market line gives
$$\mathbb{E}[R_i]=2\%+1.5(9\%-2\%)=12.5\%.$$
If an analyst forecasts $14\%$, the alpha is $14\%-12.5\%=1.5\%$: the forecast exceeds the return
required for the asset's systematic risk. A beta of 1.5 means the asset's covariance with the market is
1.5 times the market variance; idiosyncratic risk does not enter the required return because it can be
diversified away. ✓

### 9.6 Bond price, duration and convexity

A bond has face value €1,000, a 5% annual coupon (€50), five years to maturity and a yield to maturity
of 6% compounded annually.

**Price.**
$$P=50\frac{1-(1.06)^{-5}}{0.06}+1000(1.06)^{-5}
=50(4.212364)+1000(0.747258)=\text{€}957.88.$$
The bond trades at a discount because the coupon is below the yield.

**Duration.** Weighting each cash flow's present value by its time gives
$$D=\frac{1(47.17)+2(44.50)+3(41.98)+4(39.60)+5(784.62)}{957.88}=4.5347\text{ years},$$
so the modified duration is $D^*=4.5347/1.06=4.2780$.

**Price change for $\Delta y=+1\%$.** Duration gives
$\Delta P/P\approx-4.2780(0.01)=-4.278\%$, so $P\approx\text{€}916.90$. The exact price at 7% is €917.996.
With convexity $23.41$,
$$\frac{\Delta P}{P}\approx-0.042780+\tfrac12(23.41)(0.0001)=-0.041610,$$
giving $P\approx\text{€}918.02$, much closer to the exact value. ✓

### 9.7 Put–call parity and an arbitrage

A non-dividend-paying stock trades at €100; a European call with strike €100 and one year to maturity
costs €10; the continuously compounded risk-free rate is 5%.

By parity, the put should cost
$$P=C-S_0+Ke^{-rT}=10-100+100e^{-0.05}=\text{€}5.1229.$$
Suppose the put trades at €4. Buy the put, buy the stock and sell the call: the initial cash flow is
$-4-100+10=-\text{€}94$, financed by borrowing €94 at 5%. At maturity the portfolio pays
$$(K-S_T)^++S_T-(S_T-K)^+=K=\text{€}100$$
in every state. Repaying the loan costs $94e^{0.05}=\text{€}98.8195$, so the arbitrage profit is €1.1805 with
zero initial capital and no risk. Demand for the underpriced put and sales of the call would push prices
back to parity. ✓

### 9.8 The one-period binomial model by replication

A stock trades at €100 and moves to €120 or €80; the risk-free rate is 5% per period. A European call
has strike €100, so $C_u=20$ and $C_d=0$.

Hold $\Delta$ shares and $B$ in the bond:
$$\Delta(120)+1.05B=20,\qquad \Delta(80)+1.05B=0.$$
Subtracting gives $40\Delta=20$, so $\Delta=0.5$; then $1.05B=-40$, so $B=-38.0952$. The replicating
portfolio costs $0.5(100)-38.0952=\text{€}11.9048$.

The risk-neutral probability is $q=(1.05-0.8)/(1.2-0.8)=0.625$, and
$$C=\frac{0.625(20)+0.375(0)}{1.05}=\text{€}11.9048,$$
the same price. The risk-neutral expected stock price is $0.625(120)+0.375(80)=105=1.05(100)$. The
option is redundant, and $q$ is a pricing weight, not a forecast of the real probability of an up
move. ✓

### 9.9 Black–Scholes with numbers

A non-dividend-paying stock trades at €100; strike €100; continuously compounded risk-free rate 5%;
volatility 20%; maturity one year. Then
$$d_1=\frac{0+(0.05+0.02)(1)}{0.2}=0.35,\qquad d_2=0.35-0.2=0.15,$$
with $\Phi(0.35)=0.636831$ and $\Phi(0.15)=0.559618$. The call is
$$C=100(0.636831)-100e^{-0.05}(0.559618)
=63.6831-95.1229(0.559618)=\text{€}10.4506.$$
By parity, $P=10.4506-100+95.1229=\text{€}5.5735$. Delta is $\Phi(d_1)=0.6368$, gamma is
$\phi(0.35)/(100\cdot0.2)=0.01876$, and vega is $100\phi(0.35)=37.52$; a rise in volatility from 20% to
21% raises the call by about €0.375.

The formula assumes constant volatility, lognormal returns, no dividends, continuous trading, no
frictions and constant $r$. Change any of these and it is only an approximation; it is not a guarantee
that the option will earn the risk-free rate or that the hedge will be riskless in practice. ✓

## 10. Visual Explanations

Option payoffs at maturity for strike $K=100$:

| $S_T$ | 80 | 100 | 120 |
|---|---|---|---|
| Call payoff $(S_T-K)^+$ | 0 | 0 | 20 |
| Put payoff $(K-S_T)^+$ | 20 | 0 | 0 |

The call payoff is flat at zero below the strike and rises one-for-one above it; the put is the mirror
image. Both are convex in $S_T$, which is why gamma is positive and why a delta-hedged option position
benefits from large moves.

A second useful picture is the **time line of a cash-flow stream**: place each $C_t$ at its date, multiply
by the discount factor $(1+r)^{-t}$, and add. Every valuation formula in this topic — annuity, mortgage,
bond, option — is a special case of that sum.

## 11. Common Mistakes

**Mixing compounding frequencies.** A nominal rate quoted with monthly compounding is not an annual
discount rate. Convert to the per-period rate $r/m$ and the number of periods $mt$ before computing.

**Using the nominal rate as the effective rate.** The EAR is $(1+r/m)^m-1$, not $r$. For a mortgage, the
difference is small per year but large over 30 years; for high-frequency compounding it is larger.

**Discounting nominal cash flows at a real rate.** Match the cash flow to the rate: nominal with nominal,
real with real. The Fisher relation is $(1+i)=(1+r)(1+\pi)$.

**Reporting the arithmetic mean as performance.** The geometric mean is the realised compound return.
The arithmetic mean overstates long-run growth by roughly $\sigma^2/2$.

**Using variance in the Sharpe ratio.** The Sharpe ratio uses standard deviation, not variance. The units
matter.

**Omitting covariances.** Portfolio variance includes covariance terms; it equals the weighted average
of the individual variances only when all covariances are zero. The covariance terms are the source of
diversification.

**Believing diversification removes all risk.** It removes idiosyncratic risk; systematic risk remains
as the average covariance.

**Treating beta as total risk.** Beta measures covariance with the market. A high-volatility asset with
low correlation can have a low beta.

**Confusing duration with maturity.** Duration is a present-value-weighted average time and a sensitivity
measure. A coupon bond's duration is shorter than its maturity; a perpetuity has a finite duration.

**Using duration alone for large yield moves.** Duration is a first-order approximation. Add convexity,
and for very large moves reprice the bond.

**Forgetting dividends.** Put–call parity and Black–Scholes change when the stock pays dividends. Use
$S_0e^{-qT}$ for a continuous yield, or subtract the present value of discrete dividends.

**Assuming American puts equal European puts.** Early exercise of an American put can be optimal because
the strike received earns interest. The equality holds for American calls on non-dividend stocks, not for
puts in general.

**Treating risk-neutral probabilities as forecasts.** $q$ is a pricing weight that makes the discounted
stock price a martingale. It is not the real probability of an up move.

**Presenting a model as a guarantee.** Black–Scholes, the CAPM and duration are approximations with
hypotheses. Report assumptions and ranges; stress-test; do not promise outcomes.

## 12. Applications

**Personal finance.** Mortgages, student loans, retirement annuities and savings plans are present-value
calculations. The mortgage formula explains why early payments are mostly interest and why a shorter term
or a lower rate saves so much.

**Corporate finance.** Capital budgeting uses NPV; the discount rate is the opportunity cost of capital.
The CAPM supplies the cost of equity in the weighted average cost of capital. Bond duration informs
debt maturity choices.

**Asset management.** Mean–variance optimisation, the efficient frontier and the CAPM are the classical
tools of portfolio construction. Factor models extend them to size, value, momentum and profitability.

**Banking and risk management.** Duration gaps measure interest-rate risk; VaR and stress tests measure
loss risk; option Greeks measure derivative exposure. The 2008 crisis showed the limits of Gaussian
copulas and of models that assumed stable correlations.

**Insurance and actuarial science.** Annuities, life insurance and pensions are present-value
calculations with mortality and longevity risk. The same discounting logic applies, with survival
probabilities multiplying the cash-flow probabilities.

**Derivatives and hedging.** The binomial model and Black–Scholes are the basis of delta hedging,
structured products and volatility trading. Implied volatility is itself a traded quantity.

**Public policy.** Pension sustainability, government debt and infrastructure appraisal use discounting.
The choice of discount rate is an ethical as well as an economic decision, especially over long horizons.

## 13. Exercises

The problem set contains **36 problems** grouped as Beginner, Intermediate, Advanced and Challenge, with
full solutions. Every numerical answer states its compounding convention.

→ [Financial Mathematics — Exercises](exercises.md)

## 14. Solutions

Complete worked solutions, with derivations and numerical checks, are in

→ [Financial Mathematics — Solutions](solutions.md)

## 15. Summary

* Compare cash flows by discounting; the convention (simple, $m$-times compounded, continuous) must
  always be stated.
* The effective annual rate is $(1+r/m)^m-1$; the continuous equivalent is $e^r-1$.
* Annuity, perpetuity and mortgage formulas follow from geometric series.
* A mortgage payment is $Lr/(1-(1+r)^{-n})$ with $r$ and $n$ in the same period; early payments are
  mostly interest.
* Expected utility and concavity formalise risk aversion; the risk premium is approximately
  $\tfrac12A(w)\sigma^2$ for small gambles.
* Portfolio variance depends on covariances; diversification reduces but does not eliminate risk.
* The efficient frontier is the set of mean–variance efficient portfolios; with a risk-free asset it is
  a straight line and two-fund separation holds.
* The CAPM prices only systematic risk: $\mu_i-r_f=\beta_i(\mu_M-r_f)$.
* Bond prices fall when yields rise; modified duration approximates the sensitivity and convexity
  corrects it.
* Put–call parity is a static replication result: $C-P=S_0-Ke^{-rT}$ for European options on a
  non-dividend stock.
* The binomial price is the cost of a replicating portfolio; the risk-neutral probability is a pricing
  device.
* Black–Scholes follows from no-arbitrage and the lognormal model; its assumptions are approximations,
  not guarantees.

## 16. Further Learning

**Within this repository.**

* [Expectation and Variance](../../10-probability/05-expectation-and-variance/README.md) — the
  probabilistic foundation of risk and expected utility.
* [Sequences and Series in Calculus](../../07-calculus/11-sequences-and-series-in-calculus/README.md) —
  geometric series behind annuities and perpetuities.
* [Optimization](../../18-optimization/README.md) — constrained optimisation and the efficient frontier.
* [Linear Regression](../../11-statistics/04-linear-regression/README.md) — estimating beta and testing
  the CAPM.
* [Mathematical Modeling](../../22-mathematical-modeling/README.md) — assumptions, validation and model
  risk.
* [Applied Mathematics](../README.md) — the discipline index.

**Standard texts.**

* J. C. Hull, *Options, Futures, and Other Derivatives*, Pearson — the standard derivatives reference.
* J. Y. Campbell, A. W. Lo and A. C. MacKinlay, *The Econometrics of Financial Markets*, Princeton
  University Press — empirical asset pricing.
* D. G. Luenberger, *Investment Science*, Oxford University Press — an accessible mathematical treatment.
* S. E. Shreve, *Stochastic Calculus for Finance I–II*, Springer — the rigorous continuous-time theory.
* J. C. Cox and M. Rubinstein, *Options Markets*, Prentice-Hall — the binomial approach in detail.



