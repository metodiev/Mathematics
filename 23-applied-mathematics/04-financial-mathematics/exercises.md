# Financial Mathematics — Exercises

> [Financial Mathematics](README.md) · 36 problems · Beginner → Challenge · Solutions: [solutions.md](solutions.md)

Work through the problems in order. Every problem is solvable with the definitions and derivations of
the tutorial, and the section reference says where to look. Attempt each problem in writing before
opening [solutions.md](solutions.md).

**Conventions.** Unless a problem says otherwise, rates are **per period** and cash flows occur at the
**end** of the period. "Nominal annual rate $r$ compounded $m$ times per year" means the per-period rate
is $r/m$. "Continuous" means continuously compounded. All option prices are European unless stated.
Currencies are written in euros; percentages are annual only when stated. Always state the convention
you use in your answer.

## Beginner

**1.** *(§5.1, §7.1)* €5,000 is invested for 8 years at a quoted annual rate of 4%.

(a) Compute the accumulated value under simple interest.
(b) Compute it under annual compounding.
(c) Compute it under continuous compounding.
(d) Rank the three results and explain the differences.

**2.** *(§7.1)* A bank quotes a nominal annual rate of 6% with different compounding frequencies.

(a) Compute the effective annual rate for quarterly, monthly and continuous compounding.
(b) Which is highest? Does the ordering agree with the limit $m\to\infty$?
(c) What nominal annual rate compounded monthly gives an effective annual rate of exactly 6%?

**3.** *(§5.2)* A payment of €20,000 is due in 7 years.

(a) Compute its present value at a 5% annual effective discount rate.
(b) Compute it at 6%.
(c) Explain why the present value falls when the rate rises, and by what percentage it falls between
(a) and (b).

**4.** *(§5.3)* €3,000 is deposited at the end of each year for 10 years at 6% annual effective.

(a) Compute the future value at the end of year 10.
(b) Compute the present value at time 0.
(c) Repeat (a) if the deposits are at the beginning of each year (annuity due).

**5.** *(§5.3)* A perpetuity pays €500 at the end of each year.

(a) Compute its present value at a 4.5% annual effective rate.
(b) Compute its present value if the payment grows at 1.5% per year and the first payment is €500 next
year.
(c) What happens to (b) if the growth rate equals the discount rate?

**6.** *(§5.3, §7.4)* A mortgage of €180,000 has a nominal annual rate of 3.6% compounded monthly and a
term of 25 years.

(a) Compute the monthly payment.
(b) Compute total payments and total interest.
(c) Compute the effective annual rate.
(d) Explain why the effective rate exceeds the nominal rate.

**7.** *(§7.1)* An investment earns a nominal annual return of 7%, and inflation is 2.5%.

(a) Compute the exact real return.
(b) Compute the approximation $i-\pi$.
(c) Explain which is appropriate for comparing purchasing power over a long horizon.

**8.** *(§5.6)* A bond has face value €1,000, a 4% annual coupon, three years to maturity and a yield to
maturity of 5% compounded annually.

(a) Compute its price.
(b) Is it at a premium, par or discount? Why?
(c) Compute the current yield (annual coupon divided by price).

**9.** *(§5.7)* A stock has price $S_T$ at option maturity. A call and a put both have strike €50.

(a) Tabulate the payoffs of the call and the put for $S_T=40,50,60$.
(b) Sketch (in words or a table) the payoff of a straddle: one call plus one put.
(c) For which $S_T$ does the straddle break even before the premium is considered?

**10.** *(§5.7, §7.11)* A non-dividend-paying stock trades at €80. A European call with strike €85 and
six months to maturity costs €4.50. The continuously compounded risk-free rate is 4%.

(a) Use put–call parity to compute the arbitrage-free price of the European put.
(b) Verify the parity identity numerically.
(c) If the put trades at €7.00, is it over- or underpriced? Describe the arbitrage.

**11.** *(§5.5)* A portfolio invests 70% in asset A and 30% in asset B. Asset A has expected return 12%
and volatility 18%; asset B has expected return 5% and volatility 8%; the correlation is 0.3.

(a) Compute the portfolio's expected return.
(b) Compute its variance and standard deviation.
(c) Compare the portfolio volatility with the weighted average of the two volatilities.

**12.** *(§5.4, §7.7)* An investor has utility $u(w)=\sqrt w$ and wealth €40,000. She faces a 50/50
gamble of $\pm$€4,000.

(a) Compute expected utility.
(b) Compute the certainty equivalent and the risk premium.
(c) Is the investor risk averse? Justify with the concavity of $u$.

## Intermediate

**13.** *(§7.4)* Use the mortgage of Exercise 6.

(a) Compute the outstanding balance after 5 years (60 payments).
(b) Compute the principal repaid and the interest paid over those 5 years.
(c) Explain why the interest share of the payment falls over time.

**14.** *(§5.2, §7.2)* A project costs €50,000 today and returns €15,000 at the end of each of the next
four years.

(a) Compute the NPV at a 10% annual effective discount rate.
(b) Compute the IRR.
(c) Should the project be accepted at 10%? What if the opportunity cost is 6%?
(d) Explain why the IRR alone can rank projects incorrectly.

**15.** *(§7.5)* The force of interest is $\delta(t)=0.03+0.0005t$ per year.

(a) Accumulate €2,000 from $t=0$ to $t=8$.
(b) Find the equivalent constant force of interest over the 8 years.
(c) Find the equivalent annual effective rate.

**16.** *(§5.3, §7.3)* €2,000 is paid annually for 12 years at a 5% annual effective rate.

(a) Compute the present value as an ordinary annuity.
(b) Compute it as an annuity due.
(c) Compute the difference and express it as a percentage of the ordinary annuity.

**17.** *(§7.3)* A growing perpetuity pays €800 next year.

(a) Compute its present value at a 6% annual effective rate with growth 2.5%.
(b) Compute it with growth 4%.
(c) What happens as the growth rate approaches the discount rate? What if it exceeds it?

**18.** *(§5.5, §7.8)* Asset 1 has $\mu_1=14\%$, $\sigma_1=25\%$; asset 2 has $\mu_2=4\%$,
$\sigma_2=8\%$; the correlation is $\rho=-0.2$.

(a) Compute the expected return and variance of the 50/50 portfolio.
(b) Compute the minimum-variance weight and the resulting expected return and volatility.
(c) Is the minimum-variance volatility below both individual volatilities? Explain.

**19.** *(§7.9)* An asset has beta 0.8. The risk-free rate is 2.5% and the expected market risk premium
is 6%.

(a) Compute the CAPM required return.
(b) An analyst forecasts an 8.5% return. Compute alpha.
(c) Interpret the sign of alpha and explain why it is not a riskless profit.

**20.** *(§5.6, §7.10)* A bond has face value €1,000, a 6% annual coupon, four years to maturity and a
yield to maturity of 5% compounded annually.

(a) Compute its price.
(b) Compute the Macaulay and modified duration.
(c) Estimate the price at a yield of 5.5% using modified duration, and compare with the exact price.
(d) Compute the convexity and the second-order approximation; compare again.

**21.** *(§5.8, §7.12)* A stock trades at €50. Over one period it moves to €62.50 or €40. The risk-free
rate is 4% per period. A European call has strike €50.

(a) Compute the terminal payoffs.
(b) Compute the risk-neutral probability.
(c) Compute the call price by risk-neutral pricing.
(d) Compute the replicating portfolio $(\Delta,B)$ and verify the cost.

**22.** *(§5.8, §7.13)* A non-dividend-paying stock trades at €50. A European call has strike €55,
maturity 0.75 years, volatility 25% and the continuously compounded risk-free rate is 4%.

(a) Compute $d_1$ and $d_2$.
(b) Compute $\Phi(d_1)$ and $\Phi(d_2)$ and the call price.
(c) Compute the put price by parity.
(d) State two assumptions of the model that are questionable for this stock.

**23.** *(§7.11)* A stock trades at €100; a European call and put both have strike €100 and one year to
maturity; the continuously compounded rate is 5%. The call costs €9 and the put costs €3.

(a) Compute the arbitrage-free put price from parity.
(b) Show that the quoted prices violate parity.
(c) Construct an arbitrage strategy and compute its profit at maturity.
(d) Explain which trades would restore parity.

**24.** *(§5.6)* A bond has face value €1,000, a 6% annual coupon paid semiannually, five years to
maturity and a yield to maturity of 5% nominal annual compounded semiannually.

(a) Compute the price.
(b) Compute the current yield.
(c) Compute total coupons received over the life of the bond.
(d) Explain why the price is above par.

## Advanced

**25.** *(§7.3)* Derive the present-value and future-value formulas for an ordinary annuity by summing a
geometric series. Derive the continuous-annuity formula by integration, and compare the two for
$C=1$, $r=5\%$, $T=20$.

**26.** *(§7.7)* An investor has CRRA utility $u(w)=w^{1-\gamma}/(1-\gamma)$ with $\gamma=2$, wealth
€100 and a 50/50 gamble of $\pm$€20.

(a) Compute expected utility, the certainty equivalent and the risk premium exactly.
(b) Compute the Arrow–Pratt measure at $w=100$ and the small-gamble approximation.
(c) Compare exact and approximate risk premia. Why are they equal here?

**27.** *(§7.8)* For two risky assets with weights $w$ and $1-w$:

(a) Derive the minimum-variance weight.
(b) Derive the expected return and variance along the efficient frontier.
(c) State and explain two-fund separation when a risk-free asset exists.
(d) For the assets of Exercise 18 and $r_f=2\%$, compute the tangency weight, expected return,
volatility and Sharpe ratio.

**28.** *(§7.9)* Derive the CAPM security market line from the condition that the market portfolio is
tangent to the efficient frontier.

(a) State the assumptions.
(b) Carry out the differentiation with respect to the weight in asset $i$.
(c) Interpret beta and alpha.
(d) Explain one empirical criticism of the model.

**29.** *(§7.10)* Derive the modified-duration approximation and the convexity correction from a
Taylor expansion of the bond price in the yield.

(a) Show that $dP/dy=-D^*P$.
(b) Derive the convexity term.
(c) For the bond of Exercise 20, compute the exact price and the second-order approximation at a yield
of 6%, and compare.

**30.** *(§5.8, §7.12)* A two-period binomial model has $S=100$, $u=1.2$, $d=0.8$, $R=1.05$ per period
and $K=100$.

(a) Compute the risk-neutral probability.
(b) Compute the terminal payoffs and work backwards to the call price.
(c) Compute the delta of the call at the initial node and at the up node.
(d) Verify the initial price by computing the replicating portfolio at the initial node.

**31.** *(§7.11)* A stock pays a continuous dividend yield $q=3\%$. Its price is €100; a European call
with strike €100 and one year to maturity costs €8; the continuously compounded risk-free rate is 5%.

(a) State and prove put–call parity with a continuous dividend yield.
(b) Compute the arbitrage-free put price.
(c) Explain how the dividend changes the parity relative to the no-dividend case.

## Challenge

**32.** *(§7.11)* Prove that an American call on a non-dividend-paying stock has the same value as the
European call, and prove the lower bound $C\ge\max(S_0-Ke^{-rT},0)$ for a European call.

**33.** *(§7.13)* Derive the Black–Scholes call formula by evaluating
$C=e^{-rT}\mathbb{E}^{\mathbb{Q}}[(S_T-K)^+]$ under the risk-neutral lognormal distribution.

(a) Write $S_T$ in terms of a standard normal variable.
(b) Determine the threshold $Z>-d_2$ for the option to finish in the money.
(c) Evaluate the two integrals and show that the result is $S_0\Phi(d_1)-Ke^{-rT}\Phi(d_2)$.

**34.** *(§7.12, §7.13)* Consider the Cox–Ross–Rubinstein binomial model with
$u=e^{\sigma\sqrt{\Delta t}}$, $d=1/u$ and $q=(e^{r\Delta t}-d)/(u-d)$, for $S=100$, $K=100$, $r=5\%$,
$\sigma=20\%$, $T=1$.

(a) Compute the binomial price for $n=1,2,5,10,100$ periods.
(b) Compare with the Black–Scholes price.
(c) Explain why the binomial price converges to Black–Scholes as $n\to\infty$.
(d) Explain why convergence is not monotone.

**35.** *(§7.15)* A trader sells a one-year at-the-money call on a non-dividend stock with
$S=100$, $K=100$, $r=5\%$, implied volatility $20\%$, and delta-hedges it continuously in theory but in
practice only at discrete intervals. The realised volatility turns out to be 30%.

(a) Compute the Black–Scholes price and gamma at inception.
(b) Using the approximation $\text{P\&L}\approx\tfrac12\Gamma S^2(\sigma_{\mathrm{real}}^2-\sigma_{\mathrm{imp}}^2)T$,
compute the expected delta-hedged profit or loss per share.
(c) Explain why the result is positive for the option seller or buyer, and identify the risk that the
approximation ignores.
(d) Give two reasons why the model's assumptions may fail in a crisis.

**36.** *(§7.10)* An insurer has a liability of €1,000,000 due in 5 years. The flat yield curve is 4%
(annual effective). Two zero-coupon bonds are available: one maturing in 2 years and one in 10 years.

(a) Compute the present value of the liability.
(b) Find the weights in the two zeros that match the liability's duration.
(c) Compute the invested amounts and the face values.
(d) Suppose the yield jumps immediately to 5%. Compute the new liability value and the new portfolio
value. Is the position immunised?
(e) Explain the role of convexity in the residual surplus.
