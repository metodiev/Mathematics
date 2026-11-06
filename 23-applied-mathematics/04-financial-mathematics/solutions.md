# Financial Mathematics — Solutions

> [Financial Mathematics](README.md) · Solutions to the 36 problems in [exercises.md](exercises.md)

Each solution states the convention, carries out every significant step, and ends with a check. All
percentages are annual only when stated; per-period rates are marked.

## Beginner

**1.** *(Strategy: apply each convention to the same principal and time.)*

(a) Simple interest: $5{,}000(1+0.04\cdot8)=5{,}000(1.32)=\text{€}6{,}600$.

(b) Annual compounding: $5{,}000(1.04)^8$. Since $1.04^8=1.36856905$,
$A=\text{€}6{,}842.85$.

(c) Continuous compounding: $5{,}000e^{0.04\cdot8}=5{,}000e^{0.32}$. Since $e^{0.32}=1.37712776$,
$A=\text{€}6{,}885.64$.

(d) Simple $<$ annual $<$ continuous. Simple interest never earns interest on interest; annual
compounding does so once a year; continuous compounding does so at every instant, which is the limiting
case of ever more frequent compounding.

*Check.* The continuous value exceeds the annual value by
$6{,}885.64-6{,}842.85=\text{€}42.79$, about the interest on the first year's interest. ✓

**2.** *(Strategy: convert each nominal rate to an effective annual rate.)*

(a) Quarterly: $(1+0.06/4)^4-1=(1.015)^4-1=0.06136355=6.1364\%$.
Monthly: $(1+0.005)^{12}-1=0.06167781=6.1678\%$.
Continuous: $e^{0.06}-1=0.06183655=6.1837\%$.

(b) Continuous is highest, then monthly, then quarterly. This agrees with the limit: as $m$ increases,
$(1+r/m)^m$ increases to $e^r$.

(c) Solve $(1+r/12)^{12}=1.06$. Then
$1+r/12=1.06^{1/12}$, so
$$r=12\bigl(1.06^{1/12}-1\bigr)=0.0584106=5.8411\%.$$
A nominal 5.8411% compounded monthly is equivalent to 6% effective annual.

*Check.* $(1+0.0584106/12)^{12}=1.06$. ✓

**3.** *(Strategy: discount a single cash flow.)*

(a) $PV=20{,}000(1.05)^{-7}=20{,}000/1.407100=\text{€}14{,}213.63$.

(b) $PV=20{,}000(1.06)^{-7}=20{,}000/1.503630=\text{€}13{,}301.14$.

(c) A higher discount rate means future cash is discounted more heavily, so present value falls. The
percentage fall is
$$\frac{14{,}213.63-13{,}301.14}{14{,}213.63}=6.4198\%.$$
Because the horizon is long, a one-percentage-point change in the rate changes the present value by more
than 6%.

*Check.* $14{,}213.63(1.05)^7=20{,}000$ and $13{,}301.14(1.06)^7=20{,}000$. ✓

**4.** *(Strategy: ordinary annuity formulas, then the annuity-due adjustment.)*

(a) $FV=3{,}000\dfrac{(1.06)^{10}-1}{0.06}$. Since $1.06^{10}=1.79084770$,
$FV=3{,}000(13.180795)=\text{€}39{,}542.38$.

(b) $PV=3{,}000\dfrac{1-(1.06)^{-10}}{0.06}=3{,}000(7.360087)=\text{€}22{,}080.26$.

(c) Annuity due: each deposit is one year earlier, so multiply by $1.06$:
$FV=39{,}542.38(1.06)=\text{€}41{,}914.93$. Equivalently, the 10 deposits earn one extra year of interest.

*Check.* $22{,}080.26(1.06)^{10}=39{,}542.38$. ✓

**5.** *(Strategy: perpetuity and growing-perpetuity formulas.)*

(a) $PV=500/0.045=\text{€}11{,}111.11$.

(b) With growth $g=0.015$, $PV=500/(0.045-0.015)=500/0.03=\text{€}16{,}666.67$.

(c) If $g=r$, the denominator is zero and the sum diverges: each term is $500$ in present value, so the
series has infinitely many equal positive terms. If $g>r$, the terms grow in present value and the sum
also diverges. The formula requires $g<r$.

*Check.* At $g=1.5\%$, the first payment is €500 and the growth-adjusted discount rate is 3%; €500/0.03
is €16,666.67. ✓

**6.** *(Strategy: convert the nominal annual rate to a monthly rate, then apply the mortgage formula.)*

(a) The per-period rate is $r=0.036/12=0.003$ per month and $n=25\cdot12=300$ months. Then
$$M=\frac{180{,}000(0.003)}{1-(1.003)^{-300}}=\text{€}910.80.$$

(b) Total payments are $300(910.80)=\text{€}273{,}241.46$; total interest is
$273{,}241.46-180{,}000=\text{€}93{,}241.46$.

(c) The effective annual rate is $(1.003)^{12}-1=0.03659998=3.6600\%$.

(d) Monthly compounding earns interest on interest twelve times a year, so the effective rate exceeds the
nominal 3.6%. The difference is small at this rate but grows with the rate and the frequency.

*Check.* The payment is about €911 per €180,000, or about €5.06 per €1,000 of loan, which is plausible
for a 25-year loan at 3.6%. ✓

**7.** *(Strategy: use the Fisher relation, then compare with the linear approximation.)*

(a) $1+i_{\mathrm{real}}=(1.07)/(1.025)=1.0439024$, so $i_{\mathrm{real}}=4.3902\%$.

(b) $i-\pi=7\%-2.5\%=4.5\%$.

(c) The exact real return is the correct compounding adjustment. The approximation overstates the real
return by about $0.1098$ percentage points; over long horizons the error compounds, so use the exact
Fisher relation when precision matters.

*Check.* $1.0439024(1.025)=1.07$. ✓

**8.** *(Strategy: discount the three cash flows at the yield.)*

(a)
$$P=\frac{40}{1.05}+\frac{40}{(1.05)^2}+\frac{1040}{(1.05)^3}
=38.0952+36.2812+898.3911=\text{€}972.77.$$

(b) The coupon rate is 4%, below the yield of 5%, so the bond trades at a discount. Investors demand 5%
but receive only 4% in coupons; the price must fall so that the total return (coupons plus capital gain)
is 5%.

(c) Current yield $=40/972.77=4.112\%$. It is above the coupon rate because the price is below par, but
below the yield to maturity because it ignores the capital gain to par.

*Check.* At a 5% yield the price is below the €1,000 face value, as required for a discount bond. ✓

**9.** *(Strategy: apply the payoff definitions.)*

(a)

| $S_T$ | 40 | 50 | 60 |
|---|---|---|---|
| Call $(S_T-50)^+$ | 0 | 0 | 10 |
| Put $(50-S_T)^+$ | 10 | 0 | 0 |

(b) A straddle (one call plus one put) pays $|S_T-50|$: 10 at $S_T=40$, 0 at $S_T=50$, 10 at $S_T=60$.

(c) Before the premium, the straddle breaks even at $S_T=50$, where both options expire worthless. With a
total premium $\pi$, the break-even points are $S_T=50\pm\pi$.

*Check.* The straddle payoff is non-negative for every $S_T$ and is zero only at the strike. ✓

**10.** *(Strategy: put–call parity, then compare the market put with the parity value.)*

(a) $P=C-S_0+Ke^{-rT}=4.50-80+85e^{-0.04(0.5)}$.
Since $e^{-0.02}=0.9801987$, $85e^{-0.02}=83.3169$. Thus
$P=4.50-80+83.3169=\text{€}7.8169$.

(b) $C-P=4.50-7.8169=-3.3169$; $S_0-Ke^{-rT}=80-83.3169=-3.3169$. The identity holds.

(c) The market put at €7.00 is underpriced relative to €7.8169. Buy the put, buy the stock and sell the
call. The initial cost is $80+7.00-4.50=\text{€}82.50$, financed by borrowing. At maturity the portfolio pays
$\max(S_T,85)=85$ in every state. Repaying the loan costs $82.50e^{0.02}=\text{€}84.1666$, so the arbitrage
profit is $85-84.1666=\text{€}0.8334$. Buying the put and selling the call would push the put price up and the
call price down until parity is restored.

*Check.* The profit is positive and riskless; the initial net investment is financed entirely by
borrowing. ✓

**11.** *(Strategy: weighted mean for return; covariance formula for variance.)*

(a) $\mu_p=0.7(12\%)+0.3(5\%)=8.4\%+1.5\%=9.9\%$.

(b)
$$\sigma_p^2=(0.7)^2(0.18)^2+(0.3)^2(0.08)^2+2(0.7)(0.3)(0.3)(0.18)(0.08).$$
The three terms are $0.015876$, $0.000576$ and $0.0018144$, so
$\sigma_p^2=0.0182664$ and $\sigma_p=0.135153=13.5153\%$.

(c) The weighted average of volatilities is $0.7(18\%)+0.3(8\%)=15\%$. The portfolio volatility is
13.52%, below 15%, because the correlation is only 0.3: some of the individual fluctuations offset.

*Check.* If $\rho=1$, the portfolio variance would be
$(0.7\cdot0.18+0.3\cdot0.08)^2=(0.15)^2=0.0225$, so the diversification benefit is
$0.0225-0.0182664=0.0042336$. ✓

**12.** *(Strategy: expected utility, then invert $u$ to get the certainty equivalent.)*

(a) $\mathbb{E}[u]=\tfrac12\sqrt{36{,}000}+\tfrac12\sqrt{44{,}000}$.
Since $\sqrt{36{,}000}=189.7367$ and $\sqrt{44{,}000}=209.7618$,
$\mathbb{E}[u]=(189.7367+209.7618)/2=199.7492$.

(b) $CE=(199.7492)^2=\text{€}39{,}899.75$. The risk premium is
$40{,}000-39{,}899.75=\text{€}100.25$.

(c) $u'(w)=\tfrac12w^{-1/2}>0$ and $u''(w)=-\tfrac14w^{-3/2}<0$, so $u$ is increasing and concave. A
concave utility function implies risk aversion: the certainty equivalent is below the expected wealth,
and the risk premium is positive.

*Check.* $\sqrt{39{,}899.75}=199.7492$, matching the expected utility. ✓

## Intermediate

**13.** *(Strategy: use the balance recursion or the closed-form balance.)*

The payment is $M=\text{€}910.8049$ per month and $r=0.003$.

(a) After 60 payments,
$$B_{60}=180{,}000(1.003)^{60}-910.8049\frac{(1.003)^{60}-1}{0.003}.$$
Since $(1.003)^{60}=1.1968948$, the first term is $215{,}441.06$ and the second is $59{,}777.58$;
hence $B_{60}=\text{€}155{,}663.48$.

(b) Principal repaid is $180{,}000-155{,}663.48=\text{€}24{,}336.52$. Total paid is $60(910.8049)=\text{€}54{,}648.29$.
Interest paid is $54{,}648.29-24{,}336.52=\text{€}30{,}311.77$.

(c) Interest each month is $rB_{k-1}$, which falls as the balance falls. The payment is constant, so the
principal component $M-rB_{k-1}$ rises. Early payments are mostly interest; later payments are mostly
principal.

*Check.* The interest plus principal over 60 months equals the total paid:
$30{,}311.77+24{,}336.52=54{,}648.29$. ✓

**14.** *(Strategy: discount each cash flow; solve the IRR numerically or by interpolation.)*

(a) The annuity factor at 10% for four years is
$\frac{1-(1.10)^{-4}}{0.10}=3.169865$. Thus
$PV=15{,}000(3.169865)=\text{€}47{,}547.98$, and
$NPV=47{,}547.98-50{,}000=-\text{€}2{,}452.02$.

(b) The IRR solves $50{,}000=15{,}000\,a_{\overline{4}|\rho}$, so
$a_{\overline{4}|\rho}=3.333333$. Solving numerically gives $\rho=7.7138\%$.

(c) At 10%, NPV is negative, so reject. At 6%, the annuity factor is
$\frac{1-(1.06)^{-4}}{0.06}=3.465106$, so
$PV=\text{€}51{,}976.59$ and $NPV=\text{€}1{,}976.59>0$; accept.

(d) IRR ignores the scale of the investment and assumes reinvestment at the IRR. A small project with a
high IRR can add less value than a large project with a lower IRR, and non-conventional cash flows can
produce multiple IRRs. NPV uses the actual opportunity cost and is additive.

*Check.* At the IRR, $15{,}000(3.333333)=50{,}000$. ✓

**15.** *(Strategy: integrate the force of interest.)*

(a)
$$\int_0^8(0.03+0.0005t)\,dt=0.03(8)+0.0005\frac{8^2}{2}=0.24+0.016=0.256.$$
Accumulated value: $2{,}000e^{0.256}=2{,}000(1.29175)=\text{€}2{,}583.51$.

(b) The equivalent constant force is the average:
$\bar\delta=0.256/8=0.032$ per year.

(c) The equivalent annual effective rate is $e^{0.032}-1=0.032518=3.2518\%$.

*Check.* $2{,}000(1.032518)^8=2{,}583.51$. ✓

**16.** *(Strategy: ordinary annuity, then multiply by $1+r$ for the due case.)*

(a) $PV=2{,}000\dfrac{1-(1.05)^{-12}}{0.05}$. Since $1.05^{12}=1.795856$,
$(1.05)^{-12}=0.556837$, so the factor is $(1-0.556837)/0.05=8.86326$ and
$PV=\text{€}17{,}726.50$.

(b) Annuity due: $PV=17{,}726.50(1.05)=\text{€}18{,}612.83$.

(c) Difference $=\text{€}886.33$, which is exactly $5\%$ of the ordinary annuity. Every payment is one period
earlier, so each is worth $5\%$ more.

*Check.* $17{,}726.50(1.05)=18{,}612.83$. ✓

**17.** *(Strategy: growing-perpetuity formula.)*

(a) $PV=\dfrac{800}{0.06-0.025}=\dfrac{800}{0.035}=\text{€}22{,}857.14$.

(b) $PV=\dfrac{800}{0.06-0.04}=\dfrac{800}{0.02}=\text{€}40{,}000$.

(c) As $g\to0.06$, the denominator tends to zero and the present value diverges. If $g\ge0.06$ the series
does not converge; the formula is invalid, and the economic interpretation is that the cash-flow stream
grows at least as fast as the discount rate forever.

*Check.* At $g=2.5\%$, the first payment is €800 and the effective discount rate is 3.5%;
$800/0.035=22{,}857.14$. ✓

**18.** *(Strategy: portfolio formulas and the minimum-variance weight.)*

(a) $\mu_p=0.5(14\%)+0.5(4\%)=9\%$.
$$\sigma_p^2=(0.5)^2(0.25)^2+(0.5)^2(0.08)^2+2(0.5)(0.5)(-0.2)(0.25)(0.08).$$
The terms are $0.015625$, $0.0016$ and $-0.002$, so $\sigma_p^2=0.015225$ and $\sigma_p=12.339\%$.

(b) With $\rho=-0.2$,
$$w^*=\frac{0.0064-(-0.2)(0.25)(0.08)}{0.0625+0.0064-2(-0.2)(0.25)(0.08)}
=\frac{0.0064+0.004}{0.0689+0.008}=\frac{0.0104}{0.0769}=0.135241.$$
The minimum-variance portfolio has
$\mu_p=0.135241(14\%)+0.864759(4\%)=5.3524\%$ and $\sigma_p=7.0665\%$.

(c) Yes: $7.0665\%<8\%<25\%$. Negative correlation allows a portfolio whose volatility is below that of
either asset; the two assets' fluctuations partly cancel.

*Check.* The minimum-variance weight uses about 13.5% in the high-return asset and 86.5% in the
low-volatility asset, which is plausible when the correlation is negative. ✓

**19.** *(Strategy: security market line and alpha.)*

(a) $\mathbb{E}[R_i]=r_f+\beta_i(\mathbb{E}[R_M]-r_f)=2.5\%+0.8(6\%)=7.3\%$.

(b) $\alpha=8.5\%-7.3\%=1.2\%$.

(c) Positive alpha means the forecast return exceeds the return required for the asset's systematic risk.
It is not a riskless profit: the forecast may be wrong, beta is estimated with error, and the asset still
carries idiosyncratic risk that is not priced by the CAPM.

*Check.* A beta below 1 means the required return is below the market premium; 7.3% is $2.5\%+4.8\%$. ✓

**20.** *(Strategy: price from the cash flows; duration from present-value weights; convexity from the
second derivative.)*

(a) The annuity factor at 5% for four years is
$\frac{1-(1.05)^{-4}}{0.05}=3.545951$. Thus
$P=60(3.545951)+1000(1.05)^{-4}=212.757+822.702=\text{€}1{,}035.46$.

(b) The present-value weights and times give
$$D=\frac{1(57.14)+2(54.42)+3(51.83)+4(872.06)}{1035.46}=3.6793\text{ years}.$$
The modified duration is $D^*=3.6793/1.05=3.5041$.

(c) At 5.5%, the exact price is
$P=60\frac{1-(1.055)^{-4}}{0.055}+1000(1.055)^{-4}=\text{€}1{,}017.53$.
The duration approximation is
$P\approx1035.46[1-3.5041(0.005)]=\text{€}1{,}017.32$. The error is about €0.21 because duration ignores
convexity.

(d) The convexity is $16.2090$. The second-order approximation is
$$P\approx1035.46\left[1-3.5041(0.005)+\tfrac12(16.2090)(0.005)^2\right]
=\text{€}1{,}017.53,$$
which matches the exact price to the cent. Convexity matters at a 50-basis-point move.

*Check.* At a 6% yield the bond would be at par ($\text{€}1,000$), so a 5.5% price above par is consistent. ✓

**21.** *(Strategy: risk-neutral probability, then replication.)*

(a) $C_u=\max(62.50-50,0)=\text{€}12.50$ and $C_d=\max(40-50,0)=0$.

(b) $q=\dfrac{R-d}{u-d}=\dfrac{1.04-0.80}{1.25-0.80}=\dfrac{0.24}{0.45}=0.533333$.

(c) $C=\dfrac{qC_u+(1-q)C_d}{R}=\dfrac{0.533333(12.50)}{1.04}=\text{€}6.4103$.

(d) $\Delta=\dfrac{C_u-C_d}{S(u-d)}=\dfrac{12.50}{50(0.45)}=0.555556$.
$B=\dfrac{uC_d-dC_u}{(u-d)R}=\dfrac{-0.80(12.50)}{0.45(1.04)}=-21.3675$.
Cost: $0.555556(50)-21.3675=27.7778-21.3675=\text{€}6.4103$, matching (c).

*Check.* At the up node the portfolio is $0.555556(62.50)-21.3675(1.04)=34.722-22.222=12.50$; at the
down node it is $22.222-22.222=0$. ✓

**22.** *(Strategy: Black–Scholes with the stated continuous rate and volatility.)*

(a)
$$d_1=\frac{\ln(50/55)+(0.04+0.25^2/2)(0.75)}{0.25\sqrt{0.75}}
=\frac{-0.095310+0.053438}{0.216506}=-0.1934,$$
and $d_2=-0.1934-0.216506=-0.4099$.

(b) $\Phi(d_1)=0.423322$ and $\Phi(d_2)=0.340937$. Thus
$$C=50(0.423322)-55e^{-0.03}(0.340937)
=21.1661-18.1973=\text{€}2.9688.$$

(c) $P=Ke^{-rT}\Phi(-d_2)-S_0\Phi(-d_1)=55e^{-0.03}(0.659063)-50(0.576678)=\text{€}6.3433$.
Parity check: $C-P=2.9688-6.3433=-3.3745$ and
$S_0-Ke^{-rT}=50-55e^{-0.03}=-3.3745$. ✓

(d) Two questionable assumptions: constant volatility (real volatility changes, and the smile shows
different implied volatilities at different strikes) and lognormal returns with no jumps (real returns
have fat tails). Other acceptable answers: no dividends, continuous trading, no transaction costs,
constant risk-free rate.

**23.** *(Strategy: parity value versus market price; then construct the replicating arbitrage.)*

(a) $P=C-S_0+Ke^{-rT}=9-100+100e^{-0.05}=9-100+95.1229=\text{€}4.1229$.

(b) The quoted put is €3.00, below €4.1229. Equivalently,
$C-P=9-3=6.00$, while $S_0-Ke^{-rT}=100-95.1229=4.8771$. Parity is violated.

(c) Buy the put, buy the stock and sell the call. Initial cash flow:
$-3-100+9=-\text{€}94$; borrow €94. At maturity the payoff is
$(100-S_T)^++S_T-(S_T-100)^+=100$ in every state. Repay $94e^{0.05}=\text{€}98.8195$; the arbitrage profit is
$100-98.8195=\text{€}1.1805$.

(d) Buying the underpriced put and selling the overpriced call (and buying stock to hedge) raises the put
price and lowers the call price until parity holds.

*Check.* The payoff is state-independent, so the strategy is riskless. ✓

**24.** *(Strategy: semiannual coupon, semiannual yield, ten periods.)*

(a) The per-period yield is $0.05/2=0.025$, the coupon is $0.06(1000)/2=\text{€}30$, and there are 10 periods:
$$P=30\frac{1-(1.025)^{-10}}{0.025}+1000(1.025)^{-10}
=30(8.75206)+781.198=\text{€}1{,}043.76.$$

(b) Current yield $=60/1043.76=5.748\%$.

(c) Total coupons $=10(30)=\text{€}300$.

(d) The coupon rate (6%) exceeds the yield (5%), so the bond must trade above par; the premium is the
present value of the excess coupons. At maturity the price converges to par, producing a capital loss
that offsets the excess coupon.

*Check.* The price is above €1,000, consistent with a premium bond. ✓

## Advanced

**25.** *(Strategy: sum a geometric series; integrate the continuous analogue.)*

Let $v=(1+r)^{-1}$. The present value of an ordinary annuity is
$$\mathrm{PV}=C(v+v^2+\cdots+v^n)=Cv\frac{1-v^n}{1-v}.$$
Since $1-v=1-\frac1{1+r}=\frac{r}{1+r}$ and $v=\frac1{1+r}$,
$$\frac{v}{1-v}=\frac{1/(1+r)}{r/(1+r)}=\frac1r,$$
so
$$\mathrm{PV}=C\frac{1-(1+r)^{-n}}{r}.$$
The future value at the end of period $n$ is
$$\mathrm{FV}=\mathrm{PV}(1+r)^n=C\frac{(1+r)^n-1}{r}.$$
For a continuous payment stream at rate $C$ per year,
$$\mathrm{PV}=\int_0^TCe^{-rt}\,dt=C\left[-\frac{e^{-rt}}{r}\right]_0^T
=C\frac{1-e^{-rT}}{r}.$$

**Comparison.** With $C=1$, $r=0.05$, $T=20$:
$$\mathrm{PV}_{\mathrm{annual}}=\frac{1-(1.05)^{-20}}{0.05}=12.46221,\qquad
\mathrm{PV}_{\mathrm{continuous}}=\frac{1-e^{-1}}{0.05}=12.64241.$$
The continuous stream is worth $0.18020$ more because payments arrive throughout each year rather than
only at year-end; on average they are earlier, so they are discounted less.

*Check.* As $r\to0$, both formulas tend to $n$ (discrete) and $T$ (continuous), and here $n=T=20$. ✓

**26.** *(Strategy: invert the utility; then compare the exact premium with Arrow–Pratt.)*

(a) With $\gamma=2$, $u(w)=w^{-1}/(-1)=-1/w$. The gamble pays $w-h=80$ or $w+h=120$ with probability
$\tfrac12$, so
$$\mathbb{E}[u]=\tfrac12\left(-\frac1{80}\right)+\tfrac12\left(-\frac1{120}\right)
=-\frac1{160}-\frac1{240}=-\frac{5}{480}=-\frac1{96}.$$
Since $u(CE)=-1/CE$, we get $CE=96$. The risk premium is $100-96=4$.

(b) $u'(w)=1/w^2$ and $u''(w)=-2/w^3$, so
$$A(w)=-\frac{u''(w)}{u'(w)}=\frac{2}{w}=\frac{2}{100}=0.02.$$
The small-gamble approximation is
$$\pi\approx\tfrac12A(w)\sigma^2=\tfrac12(0.02)(400)=4.$$

(c) The exact and approximate premia are equal. For $u(w)=-1/w$, the certainty equivalent of a symmetric
$\pm h$ gamble is exactly $w-h^2/w$: the expected utility is
$-\tfrac12[1/(w-h)+1/(w+h)]=-w/(w^2-h^2)$, so $CE=(w^2-h^2)/w=w-h^2/w$ and $\pi=h^2/w$. The
Arrow–Pratt formula gives the same $h^2/w$ because the second-order Taylor expansion is exact for this
utility. For other utilities the two differ by higher-order terms.

*Check.* $u(96)=-1/96=\mathbb{E}[u]$. ✓

**27.** *(Strategy: differentiate the variance; then impose the tangency condition.)*

(a) With $w$ in asset 1 and $1-w$ in asset 2,
$$\sigma_p^2=w^2\sigma_1^2+(1-w)^2\sigma_2^2+2w(1-w)\rho\sigma_1\sigma_2.$$
Differentiating,
$$\frac{d\sigma_p^2}{dw}=2w\sigma_1^2-2(1-w)\sigma_2^2+2(1-2w)\rho\sigma_1\sigma_2.$$
Set this to zero:
$$w(\sigma_1^2+\sigma_2^2-2\rho\sigma_1\sigma_2)=\sigma_2^2-\rho\sigma_1\sigma_2,$$
so
$$w^*=\frac{\sigma_2^2-\rho\sigma_1\sigma_2}{\sigma_1^2+\sigma_2^2-2\rho\sigma_1\sigma_2}.$$
The second derivative is $2(\sigma_1^2+\sigma_2^2-2\rho\sigma_1\sigma_2)>0$ unless the assets are
perfectly correlated, so this is a minimum.

(b) Along the frontier,
$\mu_p=w\mu_1+(1-w)\mu_2$ and $\sigma_p^2$ is the quadratic above. Eliminating
$w=(\mu_p-\mu_2)/(\mu_1-\mu_2)$ gives a quadratic relation between $\mu_p$ and $\sigma_p^2$: a hyperbola
in the $(\sigma_p,\mu_p)$ plane. The upper branch is the efficient frontier.

(c) With a risk-free asset, every efficient portfolio is a combination of the risk-free asset and the
tangency portfolio: **two-fund separation**. The tangency weight solves
$$\max_w\frac{w\mu_1+(1-w)\mu_2-r_f}{\sqrt{w^2\sigma_1^2+(1-w)^2\sigma_2^2+2w(1-w)\rho\sigma_1\sigma_2}}.$$
Its first-order condition gives
$$w_T=\frac{(\mu_1-r_f)\sigma_2^2-(\mu_2-r_f)\rho\sigma_1\sigma_2}
{(\mu_1-r_f)\sigma_2^2+(\mu_2-r_f)\sigma_1^2-(\mu_1+\mu_2-2r_f)\rho\sigma_1\sigma_2}.$$

(d) For Exercise 18, $\mu_1=14\%$, $\sigma_1=25\%$, $\mu_2=4\%$, $\sigma_2=8\%$, $\rho=-0.2$,
$r_f=2\%$:
$$w_T=\frac{(0.12)(0.0064)-(0.02)(-0.2)(0.02)}
{(0.12)(0.0064)+(0.02)(0.0625)-(0.14)(-0.2)(0.02)}
=\frac{0.000848}{0.002578}=0.328937.$$
Then $\mu_p=0.328937(14\%)+0.671063(4\%)=7.2894\%$,
$\sigma_p^2=0.0078785$ so $\sigma_p=8.8762\%$, and
$\mathrm{SR}=(7.2894-2)/8.8762=0.5959$.

*Check.* The tangency portfolio has a higher Sharpe ratio than the 50/50 portfolio:
$(9-2)/12.339=0.5673<0.5959$. ✓

**28.** *(Strategy: differentiate the mean and standard deviation of a portfolio that is almost entirely
the market.)*

(a) Assumptions: mean–variance investors; homogeneous beliefs about means, variances and covariances;
a risk-free asset with unlimited borrowing and lending; no taxes, transaction costs or short-sale
constraints; all investors hold the same tangency portfolio; markets clear, so that portfolio is the
market portfolio.

(b) Consider a portfolio with weight $w$ in asset $i$ and $1-w$ in the market. Then
$$\mu_p=w\mu_i+(1-w)\mu_M,\qquad
\sigma_p^2=w^2\sigma_i^2+(1-w)^2\sigma_M^2+2w(1-w)\sigma_{iM}.$$
At $w=0$,
$$\frac{d\mu_p}{dw}=\mu_i-\mu_M,\qquad
\frac{d\sigma_p}{dw}=\frac{\sigma_{iM}-\sigma_M^2}{\sigma_M}.$$
Because the market portfolio is on the efficient frontier, the slope of this trade-off at $w=0$ must
equal the slope of the capital market line:
$$\frac{\mu_i-\mu_M}{(\sigma_{iM}-\sigma_M^2)/\sigma_M}
=\frac{\mu_M-r_f}{\sigma_M}.$$
Multiplying by $\sigma_M$ and rearranging,
$$\mu_i-\mu_M=\frac{\sigma_{iM}-\sigma_M^2}{\sigma_M^2}(\mu_M-r_f)
=(\beta_i-1)(\mu_M-r_f),$$
so
$$\mu_i=r_f+\beta_i(\mu_M-r_f),\qquad \beta_i=\frac{\sigma_{iM}}{\sigma_M^2}.$$

(c) Beta measures systematic risk: the covariance of the asset with the market divided by the market
variance. Alpha is
$\alpha_i=\mu_i-[r_f+\beta_i(\mu_M-r_f)]$; in the CAPM every alpha is zero. A positive alpha is a
forecast of excess risk-adjusted return, not a free lunch.

(d) **Roll's critique:** the market portfolio is unobservable and includes all wealth, so the CAPM is
hard to test. Empirically, the security market line is flatter than predicted, and size, value and
momentum explain part of the cross-section. The model is a benchmark, not a complete description.

*Check.* If $\beta_i=1$, the formula gives $\mu_i=\mu_M$; if $\beta_i=0$, it gives $\mu_i=r_f$. ✓

**29.** *(Strategy: differentiate the price twice with respect to the yield.)*

(a) With $P=\sum_tCF_t(1+y)^{-t}$,
$$\frac{dP}{dy}=-\sum_t t\,CF_t(1+y)^{-(t+1)}
=-\frac{1}{1+y}\sum_t t\,\frac{CF_t}{(1+y)^t}
=-\frac{D}{1+y}P=-D^*P.$$
Hence $\Delta P/P\approx-D^*\Delta y$ to first order.

(b) Differentiating again,
$$\frac{d^2P}{dy^2}=\sum_t t(t+1)CF_t(1+y)^{-(t+2)}=P\,C_{\mathrm{conv}},$$
where
$$C_{\mathrm{conv}}=\frac1P\sum_t\frac{t(t+1)CF_t}{(1+y)^{t+2}}.$$
The second-order Taylor expansion is
$$\Delta P\approx P'\,\Delta y+\tfrac12P''(\Delta y)^2
=P\left(-D^*\Delta y+\tfrac12C_{\mathrm{conv}}(\Delta y)^2\right).$$

(c) For the bond of Exercise 20, $P=\text{€}1{,}035.46$, $D^*=3.50407$, $C_{\mathrm{conv}}=16.2090$.
At $y=6\%$, $\Delta y=0.01$. The exact price is €1,000. The first-order approximation is
$$1{,}035.46(1-3.50407(0.01))=\text{€}999.18.$$
The second-order approximation is
$$1{,}035.46\left(1-0.0350407+\tfrac12(16.2090)(0.0001)\right)=\text{€}1{,}000.02,$$
much closer. The residual €0.02 is the third-order term.

*Check.* At a 1% yield rise the bond loses about 3.42% of value; the modified duration predicts 3.50%,
and convexity reduces the predicted loss. ✓

**30.** *(Strategy: backward induction on the tree.)*

(a) $q=\dfrac{1.05-0.8}{1.2-0.8}=\dfrac{0.25}{0.4}=0.625$.

(b) Terminal prices: $144$, $96$, $64$; call payoffs: $44$, $0$, $0$. At the up node,
$$C_u=\frac{0.625(44)+0.375(0)}{1.05}=26.1905;$$
at the down node, $C_d=0$. At the root,
$$C_0=\frac{0.625(26.1905)+0.375(0)}{1.05}=15.5896.$$

(c) At the root,
$\Delta_0=(C_u-C_d)/(120-80)=26.1905/40=0.654762$.
At the up node, $\Delta_u=(44-0)/(144-96)=44/48=0.916667$.

(d) At the root, $B_0=C_0-\Delta_0S_0=15.5896-65.4762=-49.8866$. At the up node the portfolio is
$0.654762(120)+1.05(-49.8866)=78.5714-52.3809=26.1905=C_u$; at the down node it is
$52.3810-52.3809=0=C_d$. Replication works.

*Check.* The risk-neutral expected terminal price is
$0.625^2(144)+2(0.625)(0.375)(96)+0.375^2(64)=110.25$, and $1.05^2(100)=110.25$. ✓

**31.** *(Strategy: replicate with a dividend-reinvested share.)*

(a) **Parity with dividend yield.** Portfolio A: one call plus cash $Ke^{-rT}$. Portfolio B: one put plus
$e^{-qT}$ shares. With dividends reinvested at the yield $q$, $e^{-qT}$ shares grow to one share at $T$,
worth $S_T$. At maturity both portfolios are worth $\max(S_T,K)$. Therefore
$$C+Ke^{-rT}=P+S_0e^{-qT}
\quad\Longrightarrow\quad
C-P=S_0e^{-qT}-Ke^{-rT}.$$
The no-dividend case is $q=0$.

(b)
$$P=C-S_0e^{-qT}+Ke^{-rT}
=8-100e^{-0.03}+100e^{-0.05}
=8-97.0446+95.1229=\text{€}6.0784.$$

(c) The dividend reduces the effective value of the stock term from $S_0$ to $S_0e^{-qT}$, so for fixed
$C$ the put must be higher than in the no-dividend case. Intuitively, a call holder does not receive the
dividends, so the call is less valuable and the put more valuable relative to the no-dividend parity.

*Check.* $C-P=8-6.0784=1.9216$ and
$S_0e^{-qT}-Ke^{-rT}=97.0446-95.1229=1.9217$. ✓

## Challenge

**32.** *(Strategy: first prove the lower bound, then compare exercising with holding.)*

**Lower bound.** Consider a portfolio long one European call and long cash $Ke^{-rT}$, and a portfolio
long one share. At maturity the first is worth $(S_T-K)^++K=\max(S_T,K)\ge S_T$, so its initial value
must be at least $S_0$; otherwise buy the first, short the share, and pocket a riskless profit. Hence
$$C+Ke^{-rT}\ge S_0\quad\Longrightarrow\quad C\ge S_0-Ke^{-rT}.$$
Since $C\ge0$, $C\ge\max(S_0-Ke^{-rT},0)$.

**American call.** Let $C^{\mathrm{A}}_t$ be the value of an American call at time $t$ with remaining
maturity $T-t$. Clearly $C^{\mathrm{A}}\ge C^{\mathrm{E}}$. If the holder exercises at $t$, she receives
$S_t-K$. If she instead holds the option, the lower bound at $t$ is
$$C^{\mathrm{E}}_t\ge S_t-Ke^{-r(T-t)}>S_t-K$$
when $r>0$ and $T>t$. Holding is strictly better than exercising, and selling the option is at least as
good as holding. Therefore early exercise is never optimal, and $C^{\mathrm{A}}=C^{\mathrm{E}}$.

The argument uses the absence of dividends. With dividends, exercising early can capture the dividend
and the equality fails.

*Check.* At $t=T$, both values equal $(S_T-K)^+$; for $t<T$, the strict inequality follows from
$e^{-r(T-t)}<1$. ✓

**33.** *(Strategy: integrate the payoff against the lognormal density.)*

(a) Under the risk-neutral measure, the stock price at $T$ is
$$S_T=S_0\exp\left(\left(r-\frac{\sigma^2}{2}\right)T+\sigma\sqrt T\,Z\right),\qquad Z\sim\mathcal N(0,1).$$

(b) The call finishes in the money when $S_T>K$, i.e.
$$\left(r-\frac{\sigma^2}{2}\right)T+\sigma\sqrt T\,Z>\ln\frac{K}{S_0}.$$
Rearranging,
$$Z>-\frac{\ln(S_0/K)+(r-\sigma^2/2)T}{\sigma\sqrt T}=-d_2.$$

(c) Therefore
$$C=e^{-rT}\int_{-d_2}^{\infty}\left[S_0e^{(r-\sigma^2/2)T+\sigma\sqrt T z}-K\right]\phi(z)\,dz.$$
The second term is
$$-Ke^{-rT}\int_{-d_2}^{\infty}\phi(z)\,dz=-Ke^{-rT}\Phi(d_2).$$
For the first term, use $e^{az}\phi(z)=e^{a^2/2}\phi(z-a)$ with $a=\sigma\sqrt T$:
$$S_0e^{-rT}e^{(r-\sigma^2/2)T}\int_{-d_2}^{\infty}e^{\sigma\sqrt T z}\phi(z)\,dz
=S_0e^{-\sigma^2T/2}e^{\sigma^2T/2}\int_{-d_2}^{\infty}\phi(z-\sigma\sqrt T)\,dz.$$
The powers of $e$ cancel, and the substitution $u=z-\sigma\sqrt T$ gives
$$S_0\int_{-d_2-\sigma\sqrt T}^{\infty}\phi(u)\,du=S_0\Phi(d_2+\sigma\sqrt T)=S_0\Phi(d_1).$$
Combining,
$$C=S_0\Phi(d_1)-Ke^{-rT}\Phi(d_2).$$

*Check.* As $S_0\to\infty$, $d_1,d_2\to\infty$, so $C\to S_0-Ke^{-rT}$; as $S_0\to0$, both $\Phi$ terms
tend to $0$. ✓

**34.** *(Strategy: compute the CRR tree for several $n$; then invoke the central limit theorem.)*

(a) Using $u=e^{\sigma\sqrt{T/n}}$, $d=1/u$, $q=(e^{rT/n}-d)/(u-d)$ and backward induction:

| $n$ | Binomial price |
|---|---|
| 1 | 12.1623 |
| 2 | 9.5405 |
| 5 | 10.8059 |
| 10 | 10.2534 |
| 100 | 10.4306 |

(b) The Black–Scholes price is €10.4506. The binomial price approaches it as $n$ grows.

(c) Under the risk-neutral measure, each step's log return is $\ln u$ or $\ln d$, with probabilities $q$
and $1-q$. The total log return is a sum of $n$ independent terms. The parameters are chosen so that
the mean and variance of the sum converge to $(r-\sigma^2/2)T$ and $\sigma^2T$, respectively. By the
central limit theorem the sum converges in distribution to a normal with those parameters, so $S_T$
converges to the lognormal Black–Scholes stock price. The option payoff is continuous and grows at most
linearly in $S_T$, so its expectation converges to the Black–Scholes expectation.

(d) Convergence is not monotone because the strike may fall between adjacent nodes. When it does, the
terminal payoff is approximated with a saw-tooth error that oscillates as $n$ changes; the oscillation
shrinks as the node spacing shrinks, but it need not decrease at every step.

*Check.* For $n=1$, the tree is coarse and the price differs by €1.71; for $n=100$ the difference is
about €0.02. ✓

**35.** *(Strategy: use the gamma P\&L approximation and keep the sign straight.)*

(a) The Black–Scholes call price is €10.4506. Gamma is
$$\Gamma=\frac{\phi(d_1)}{S\sigma\sqrt T}
=\frac{\phi(0.35)}{100(0.2)}=\frac{0.375240}{20}=0.018762.$$

(b) If the trader is **long** the option and delta-hedges, the expected profit from volatility exposure is
$$\text{P\&L}\approx\tfrac12\Gamma S^2(\sigma_{\mathrm{real}}^2-\sigma_{\mathrm{imp}}^2)T
=\tfrac12(0.018762)(10{,}000)(0.09-0.04)(1)=\text{€}4.6905$$
per share. The trader in the question is **short** the call, so the sign reverses: the expected
delta-hedged result is a **loss** of about €4.69 per share, or €469 on 100 shares.

(c) The buyer of the option is long gamma: when realised volatility exceeds implied volatility, the
convexity of the payoff more than compensates for the premium paid. The seller is short gamma and loses.
The approximation ignores jump and gap risk, discrete hedging error, transaction costs, changes in the
volatility surface, and the possibility of a large move before the hedge can be adjusted; these can
dominate the estimate.

(d) Two reasons: (i) volatility is not constant and can jump, especially in a crisis, so the lognormal
model underestimates tail moves; (ii) liquidity and funding can disappear, so continuous hedging at the
assumed prices is impossible, and correlations rise when diversification is most needed.

*Check.* The sign is the one that matters: long gamma profits from realised volatility above implied;
short gamma loses. ✓

**36.** *(Strategy: duration-match the assets to the liability, then revalue after the yield shock.)*

(a) The present value of the liability at 4% is
$$L_0=\frac{1{,}000{,}000}{(1.04)^5}=\text{€}821{,}927.11.$$

(b) A zero-coupon bond maturing in $t$ years has duration $t$. Let $w$ be the weight in the 2-year zero
and $1-w$ the weight in the 10-year zero. Duration matching requires
$$2w+10(1-w)=5\quad\Longrightarrow\quad 10-8w=5\quad\Longrightarrow\quad w=0.625.$$
So 62.5% in the 2-year zero and 37.5% in the 10-year zero.

(c) Invest $0.625(821{,}927.11)=\text{€}513{,}704.44$ in the 2-year zero and
$0.375(821{,}927.11)=\text{€}308{,}222.67$ in the 10-year zero. The face values are
$$F_2=513{,}704.44(1.04)^2=\text{€}555{,}622.72,\qquad
F_{10}=308{,}222.67(1.04)^{10}=\text{€}456{,}244.84.$$

(d) At a 5% yield the liability becomes
$$L_1=\frac{1{,}000{,}000}{(1.05)^5}=\text{€}783{,}526.17.$$
The bond values become
$$V_2=\frac{555{,}622.72}{(1.05)^2}=\text{€}503{,}966.19,\qquad
V_{10}=\frac{456{,}244.84}{(1.05)^{10}}=\text{€}280{,}094.75.$$
Total assets are €784,060.94, so the surplus is
$784{,}060.94-783{,}526.17=\text{€}534.78$. The position is immunised to first order: the small positive surplus
comes from convexity.

(e) Duration matching equalises first-order interest-rate sensitivity. The asset portfolio has higher
convexity than the single liability cash flow, so for both a rise and a fall in yields the assets gain
relative to the liability. At 3% the surplus is about €607.93; at 5% it is about €534.78. Convexity is
therefore a second-order source of surplus, not a guarantee: it depends on the yield shift being
parallel and immediate, and on the bonds being held to their stated maturities.

*Check.* At 4% the portfolio value equals the liability exactly by construction; at 5% the surplus is
positive but small relative to €784,000. ✓

