# Exponential and Logarithmic Models — Solutions

> [Tutorial](README.md) · [Exercises](exercises.md) · 36 worked solutions

Each solution states the strategy, carries out every step, and ends with an answer and a check. Where a
result is a model prediction, the final remark says exactly what the number does and does not show. All
figures below were recomputed to three significant figures; a check that is marked ✓ reproduces the
answer by an independent route.

## Beginner

**1.**

**Strategy.** Two parameters: the value at $t=0$ and the annual factor. Read both from the sentence.

$P_0 = 12{,}000$ and a $4\%$ annual increase multiplies by $b = 1.04$, so

$$P(t) = 12{,}000\,(1.04)^{t}, \qquad t \text{ in years since 2020}.$$

The continuous rate is $k = \ln 1.04 = 0.03922$ per year, so $P(t) = 12{,}000\,e^{0.03922t}$.

2030 corresponds to $t = 10$:

$$P(10) = 12{,}000\,(1.04)^{10} = 12{,}000(1.480244) = 17{,}762.9.$$

**Answer.** $P(t) = 12{,}000(1.04)^{t}$, $k = 0.0392$, and about $17{,}760$ people in 2030.

**Check.** Rule of 72: doubling in $72/4 = 18$ years, so $10$ years is $10/18 = 0.56$ doublings, and $2^{0.56} = 1.47$ — consistent with $1.480$. ✓

**2.**

**Strategy.** A multiplier per year is exactly $b$; convert it to a rate and to a decade factor by powers.

(a) $b = 1.035$ means a $3.5\%$ annual growth rate.

(b) $k = \ln 1.035 = 0.03440$ per year.

(c) Ten years is ten factors: $1.035^{10} = e^{10(0.03440)} = e^{0.34401} = 1.4106$.

**Answer.** $3.5\%$ per year; $k = 0.0344$; the decade factor is $1.411$, i.e. a $41.1\%$ increase per decade.

**Check.** $3.5\%$ per year for ten years is *not* $35\%$: compounding adds about $0.5$ percentage point per decade at this rate, and $41.1\% - 35\% = 6.1$, which is of the expected order for the cross terms. ✓

**3.**

**Strategy.** Doubling time solves $b^{T} = 2$; take logarithms.

$$1.12^{T} = 2 \;\Longrightarrow\; T = \frac{\ln 2}{\ln 1.12} = \frac{0.693147}{0.113329} = 6.116 \text{ years}.$$

The rule of 72 predicts $72/12 = 6$ years.

**Answer.** $T = 6.12$ years; the rule is $1.9\%$ low.

**Check.** $1.12^{6.116} = e^{6.116 \times 0.113329} = e^{0.69315} = 2.000$ ✓. The rule's error is largest for large rates; at $12\%$ it is already noticeable but still small enough for mental arithmetic.

**4.**

**Strategy.** Convert years to half-lives, then use $2^{-n}$.

$$n = \frac{30}{12} = 2.5, \qquad \frac{N}{N_0} = 2^{-2.5} = \frac{1}{2^{2}\sqrt{2}} = \frac{1}{4(1.41421)} = 0.17678.$$

**Answer.** $17.7\%$ remains, after $2.5$ half-lives.

**Check.** After $2$ half-lives, $25\%$; after $3$, $12.5\%$. $17.7\%$ lies between them, at $2.5$ half-lives as expected. ✓

**5.**

**Strategy.** Continuous compounding is $A = Pe^{rt}$; the effective annual rate is $e^{r}-1$.

$$A = 2500\,e^{0.036 \times 8} = 2500\,e^{0.288} = 2500(1.333757) = 3334.39,$$
$$r_{\text{eff}} = e^{0.036}-1 = 1.036656-1 = 0.036656.$$

**Answer.** $\$3{,}334.39$; effective annual rate $3.666\%$.

**Check.** Simple interest for $8$ years at $3.6\%$ gives $2500(1.288) = \$3{,}220$; compounding adds about $\$114$, which is $3.5\%$ of the principal over eight years — plausible for a $3.6\%$ rate. ✓

**6.**

**Strategy.** Quarterly compounding multiplies by $1 + 0.04/4 = 1.01$ each quarter.

$$r_{\text{eff}} = (1.01)^{4}-1 = 1.040604-1 = 0.040604.$$

Over ten years there are $40$ quarters:

$$1.01^{40} = e^{40\ln 1.01} = e^{0.398004} = 1.488864.$$

**Answer.** Effective rate $4.0604\%$; the balance grows by a factor $1.489$ in ten years.

**Check.** Continuous compounding at $4\%$ would give $e^{0.4} = 1.49182$, slightly more than $1.48886$, as it must be since quarterly compounding is less frequent. ✓

**7.**

**Strategy.** Use $3 = e^{\ln 3}$.

$$5\cdot3^{x} = 5\left(e^{\ln 3}\right)^{x} = 5e^{(\ln 3)x} = 5e^{1.0986x}.$$

**Answer.** $k = \ln 3 = 1.0986$.

**Check.** At $x=2$: original $5\cdot9 = 45$; new form $5e^{2.1972} = 5(9.0000) = 45$ ✓.

**8.**

**Strategy.** Apply the definition with the minus sign.

$$\mathrm{pH} = -\log_{10}\left(4.5\times10^{-6}\right) = 6 - \log_{10}4.5 = 6 - 0.65321 = 5.3468.$$

**Answer.** pH $= 5.35$, which is below $7$, so the solution is acidic.

**Check.** $10^{-5.3468} = 10^{-6}\cdot10^{0.6532} = 10^{-6}(4.50)$ ✓.

**9.**

**Strategy.** Decibels of *power* use the coefficient $10$.

$$L = 10\log_{10}(500) = 10(2.69897) = 26.99\ \text{dB}.$$

**Answer.** About $27.0$ dB.

**Check.** $500 = 100 \times 5$, so the gain is $20$ dB (for the factor $100$) plus $10\log_{10}5 = 6.99$ dB — total $26.99$ dB ✓. Note that if $500$ were an *amplitude* ratio, the answer would be $54.0$ dB; the physical quantity decides the coefficient.

**10.**

**Strategy.** Level differences are ratios (Property 8.9): for amplitude $c = 1$, for energy $c = 1.5$ in magnitude units.

The magnitude difference is $5.2 - 4.1 = 1.1$.

(a) Amplitude: $10^{1.1} = 12.589$.

(b) Energy: $10^{1.5 \times 1.1} = 10^{1.65} = 44.668$.

**Answer.** Amplitudes differ by a factor $12.6$; energies by a factor $44.7$.

**Check.** Energy scales as amplitude$^{3/2}$: $12.589^{1.5} = e^{1.5\ln 12.589} = e^{1.5(2.533)} = e^{3.799} = 44.6$ ✓.

**11.**

**Strategy.** Magnitude is $-2.5\log_{10}(F_1/F_2)$, so a difference of $3$ magnitudes gives $10^{3/2.5} = 10^{1.2}$.

$$10^{1.2} = 15.849.$$

**Answer.** The flux ratio is $15.8$. The *smaller* magnitude is the brighter star, so the star with the smaller number is $15.8$ times brighter.

**Check.** $5$ magnitudes is a factor $100$; $3$ magnitudes is $3/5$ of that, and $100^{3/5} = 10^{1.2}$ ✓.

**12.**

**Strategy.** Isolate the exponential and take logarithms.

$$7\cdot2^{x} = 224 \;\Longrightarrow\; 2^{x} = 32 \;\Longrightarrow\; x = \frac{\ln 32}{\ln 2} = 5.$$

**Answer.** $x = 5$.

**Check.** $7\cdot2^{5} = 7(32) = 224$ ✓.

**13.**

**Strategy.** Test the two signatures: constant *difference*, constant *ratio at equal $x$-steps*, or constant ratio *when $x$ is multiplied*.

**Table A.** The $x$-values are equally spaced and $y$ is multiplied by $3$ each step ($5, 15, 45, 135$). A constant ratio per unit step is exponential:

$$y = 5\cdot3^{x}.$$

**Table B.** Each $x$ is doubled and each $y$ is multiplied by $3$. A constant ratio of outputs for a constant ratio of inputs is a power law. With $y = ax^{p}$ and $x$ doubled, $2^{p} = 3$, so $p = \log_2 3 = 1.5850$ and $a = 5$:

$$y = 5x^{1.585}.$$

**Answer.** A is $y = 5\cdot3^{x}$; B is $y = 5x^{1.585}$.

**Check.** Table B at $x=4$: $5\cdot4^{1.585} = 5e^{1.585(1.3863)} = 5e^{2.1974} = 5(9.000) = 45$ ✓; at $x=8$: $5\cdot8^{1.585} = 5e^{3.2961} = 5(27.0) = 135$ ✓.

**Remark.** The two tables contain the same $y$-values; only the spacing of the inputs differs. This is the cleanest demonstration that "the numbers look exponential" is not a property of the numbers.

## Intermediate

**14.**

**Strategy.** Two points, two parameters; then hold the model fixed and test it elsewhere.

From $(0,3)$: $3 = ab^{0} = a$, so $a = 3$. From $(4,48)$:

$$48 = 3b^{4} \;\Longrightarrow\; b^{4} = 16 \;\Longrightarrow\; b = 2.$$

So $y = 3\cdot2^{x}$.

At $x=2$: $y = 3\cdot2^{2} = 12$.

**Answer.** $a = 3$, $b = 2$, $y(2) = 12$.

**What the prediction at $x=10$ is worth.** $y(10) = 3\cdot2^{10} = 3072$, but this is a pure extrapolation from two points with no degrees of freedom left. It is a restatement of "doubling every unit of $x$", not evidence that the quantity doubles; the data cannot contradict it, because the data were used up in the fit.

**Check.** $y(2)=12$ lies exactly halfway (in the multiplicative sense) between $3$ and $48$: $3\to12\to48$ doubles each time ✓.

**15.**

**Strategy.** Solve $\left(\tfrac12\right)^{t/5730} = 0.45$.

Taking natural logarithms,

$$\frac{t}{5730}\ln\tfrac12 = \ln 0.45 \;\Longrightarrow\; t = 5730\cdot\frac{\ln(1/0.45)}{\ln 2} = 5730\cdot\frac{0.798508}{0.693147} = 5730(1.15200) = 6601.$$

**Answer.** About $6{,}600$ years.

**Check.** $6601/5730 = 1.152$ half-lives, and $2^{-1.152} = 0.4499$ ✓.

**Remark.** The half-life of carbon-14 is now measured as $5700 \pm 30$ years; using $5700$ would give $6566$ years, a $0.5\%$ change. Quoting an age to four digits would overstate the accuracy of the method, whose real uncertainties (calibration, contamination, reservoir effects) are far larger than the arithmetic suggests.

**16.**

**Strategy.** The growth factor over $4.5$ hours is the ratio; the factor per hour is its $1/4.5$ power.

$$b_{4.5} = \frac{4000}{500} = 8, \qquad b_{1} = 8^{1/4.5} = e^{\ln 8/4.5} = e^{0.46210} = 1.5874.$$

Continuous rate: $k = \ln 1.5874 = 0.4621$ per hour. Doubling time:

$$T_2 = \frac{\ln 2}{0.4621} = 1.500 \text{ h}.$$

**Answer.** Hourly factor $1.587$ ($58.7\%$ per hour), $k = 0.462\ \mathrm{h^{-1}}$, doubling time $1.50$ h.

**Check.** In $4.5$ hours there are $4.5/1.5 = 3$ doublings, and $500\cdot2^{3} = 4000$ ✓. Direct: $1.5874^{4.5} = e^{4.5(0.4621)} = e^{2.0794} = 8$ ✓.

**17.**

**Strategy.** Convert to half-lives: $2^{-t/6}$ is the remaining fraction.

(a) $t = 9$ is $1.5$ half-lives:

$$m(9) = 400\cdot2^{-1.5} = 400(0.353553) = 141.4\ \text{mg}.$$

(b) Solve $400\cdot2^{-t/6} = 25$:

$$2^{-t/6} = \frac{25}{400} = \frac{1}{16} = 2^{-4} \;\Longrightarrow\; \frac{t}{6} = 4 \;\Longrightarrow\; t = 24 \text{ h}.$$

**Answer.** (a) $141$ mg remains; (b) the amount falls below $25$ mg after $24$ hours, i.e. after exactly four half-lives.

**Check.** $400 \to 200 \to 100 \to 50 \to 25$: four halvings, so $24$ hours ✓.

**Remark.** The model never reaches zero, so "below $25$ mg" is a threshold, not exhaustion — and in a real patient, absorption, metabolism and the dosing schedule matter more than the idealised half-life.

**18.**

**Strategy.** Divide the two equations to eliminate $a$, then use logarithms.

$$\frac{187.5}{12} = \frac{a\,5^{p}}{a\,2^{p}} = \left(\frac52\right)^{p} = 2.5^{p}.$$

So

$$p = \frac{\ln 15.625}{\ln 2.5} = \frac{2.748872}{0.916291} = 3.0000.$$

Then $a = \dfrac{12}{2^{3}} = 1.5$.

So $y = 1.5x^{3}$.

**Check at $x=3$:** $1.5(27) = 40.5$. There is no independent data point at $x=3$, so this is a prediction of the fitted model, not a test of it — the model used both data points and has nothing left over.

**Answer.** $a = 1.5$, $p = 3$, and $y(3) = 40.5$.

**Remark.** The exponent came out *exactly* $3$, which means the two given values were probably generated from a cube. Real measurements never give such a clean result.

**19.**

**Strategy.** On a semi-log plot the slope is $\log b$; here the slope is $\log y$ change per unit $x$.

$$\text{slope} = \frac{0.9}{3} = 0.3 \ \text{per unit } x.$$

$$\log b = 0.3 \;\Longrightarrow\; b = 10^{0.3} = 1.9953.$$

Doubling distance: the horizontal change $\Delta x$ with $\log y$ increasing by $\log 2$ is

$$\Delta x = \frac{\log 2}{\text{slope}} = \frac{0.30103}{0.3} = 1.0034.$$

**Answer.** $b = 1.995 \approx 2.0$ per unit $x$; a doubling about every $1.00$ units of $x$.

**Check.** $1.9953^{1.0034} = e^{1.0034\ln 1.9953} = e^{1.0034(0.69099)} = e^{0.69333} = 2.000$ ✓.

**Remark.** This is the normal use of a semi-log plot: a slope of $0.3$ per unit in base $10$ *is* a doubling per unit, because $\log_{10}2 = 0.30103$. Reading slopes in base $10$ is therefore very convenient — $0.3$ means "doubles".

**20.**

**Strategy.** Two points fix the model; compute the annual factor as a $1/18$ power.

$$\frac{y_2}{y_1} = \frac{1{,}180{,}000}{2{,}300} = 513.043, \qquad r = 513.043^{1/18} = e^{6.24038/18} = e^{0.346688} = 1.41437.$$

Doubling time:

$$T_2 = \frac{\ln 2}{\ln 1.41437} = \frac{0.693147}{0.346688} = 1.9993 \text{ years}.$$

Predictions from $2300\cdot1.41437^{\,t-1971}$:

* 2000 ($t=29$): $2300(1.41437)^{29} = 2300(23{,}247) = 53{,}467{,}000$.
* 2010 ($t=39$): $2300(1.41437)^{39} = 2300(744{,}733) = 1.713\times10^{9}$.

**Answer.** Doubling time $2.00$ years; predictions $53.5$ million for 2000 and $1.71$ billion for 2010, against actual values of $42$ million and $1.17$ billion.

**Errors.** 2000: $(53.47/42)-1 = +27\%$. 2010: $(1.713/1.17)-1 = +46\%$.

**What this shows.** A model that is *excellent* over the 18 years used for the fit ($2.00$ years is almost exactly the folklore value) drifts by $27\%$ one decade later and $46\%$ two decades later. Fitting quality on the calibration range says nothing about extrapolation quality.

**Check.** $1.41437^{18} = e^{18(0.346688)} = e^{6.24038} = 513.0$ ✓, recovering the input ratio.

**21.**

**Strategy.** Compare *effective* annual rates. Continuous at $6\%$: $e^{0.06}-1$. Annual at $6.2\%$: $6.2\%$ exactly.

$$e^{0.06}-1 = 1.0618365-1 = 0.0618365, \qquad \text{so } 6.1837\%.$$

Since $6.2\% > 6.1837\%$, B is better. Over $20$ years on $\$5{,}000$:

$$A:\ 5000\,e^{1.2} = 5000(3.320117) = 16{,}600.58,$$
$$B:\ 5000(1.062)^{20} = 5000(3.330354) = 16{,}651.77.$$

**Answer.** Investment B is better by $\$51.18$ on $\$5{,}000$ over $20$ years (about $0.31\%$).

**What this shows.** "More frequent compounding" is *not* automatically better: the nominal rate matters more. At a fixed nominal rate the most that extra compounding can add is $e^{r}-1-r$ — here $0.1837$ percentage points — which is smaller than the $0.2$ percentage-point advantage B gets from its higher nominal rate.

**Check.** $1.062^{20} = e^{20\ln 1.062} = e^{20(0.060155)} = e^{1.20310} = 3.33035$ ✓.

**22.**

**Strategy.** Use $A = (K-P_0)/P_0$, then evaluate; for the peak, use $P = K/2$.

$$A = \frac{2000-100}{100} = 19, \qquad P(t) = \frac{2000}{1+19e^{-0.6t}}.$$

At $t=3$: $e^{-1.8} = 0.165299$, $19(0.165299) = 3.14068$, so

$$P(3) = \frac{2000}{4.14068} = 483.0.$$

Fastest growth is at $P = K/2 = 1000$:

$$19e^{-0.6t} = 1 \;\Longrightarrow\; t = \frac{\ln 19}{0.6} = \frac{2.94444}{0.6} = 4.907 \text{ years}.$$

Maximum rate: $\dfrac{rK}{4} = \dfrac{0.6(2000)}{4} = 300$ per year.

**Answer.** $A = 19$; $P(3) = 483$; fastest growth at $t = 4.91$ years; maximum rate $300$ per year.

**Check.** $P(0) = 2000/20 = 100$ ✓. A growth rate of $300$ per year against a population of $1000$ is $30\%$ per year, which is $r/2 = 0.3$ — exactly what the formula $rP(1-P/K)$ gives at $P = K/2$ ✓.

**23.**

**Strategy.** Match the given expression to Properties 8.10 and 8.11.

$$\frac1P = \frac1K + \frac{A}{K}e^{-rt}.$$

Comparing: $\dfrac1K = 0.002$, so $K = 500$; $\dfrac AK = 0.018$, so $A = 0.018(500) = 9$; and $r = 0.4$.

Then $P_0 = \dfrac{K}{1+A} = \dfrac{500}{10} = 50$.

At $t=5$: $e^{-2} = 0.135335$, $9(0.135335) = 1.21802$, so

$$P(5) = \frac{500}{2.21802} = 225.4.$$

**Answer.** $K = 500$, $A = 9$, $r = 0.4$, $P_0 = 50$, $P(5) = 225$.

**Check.** $P(0) = 500/(1+9) = 50$ ✓, and the reciprocal at $t=0$ is $0.002+0.018 = 0.020 = 1/50$ ✓.

**24.**

**Strategy.** Convert microseconds to convenient units. One second is $10^{6}$ µs; one year is $3.15576\times10^{7}$ s.

* $n=40$: $2^{40} = 1.099512\times10^{12}\ \mu\text{s} = 1.099512\times10^{6}\ \text{s} = 12.73$ days.
* $n=50$: $2^{50} = 1.125900\times10^{15}\ \mu\text{s} = 1.125900\times10^{9}\ \text{s} = 35.68$ years.

**Answer.** About $12.7$ days at $n=40$ and about $35.7$ years at $n=50$.

**Check.** Ten extra units of $n$ multiply the time by $2^{10} = 1024$: $12.73 \text{ days} \times 1024 = 13{,}035$ days $= 35.7$ years ✓.

**Remark.** Going from $n=50$ to $n=60$ multiplies by another $1024$, giving about $36{,}500$ years — three times longer than recorded history. This is why "exponential time" and "slow" are different statements: the algorithm is exact, and exactness is what costs.

**25.**

**Strategy.** Amplitude one unit per magnitude; energy $1.5$ units per magnitude.

(a) $\Delta M = 7.0-5.0 = 2.0$: amplitude ratio $10^{2} = 100$; energy ratio $10^{1.5(2)} = 10^{3} = 1000$.

(b) Solve $10^{1.5\Delta M} = 10^{4.5}$, so $1.5\Delta M = 4.5$ and $\Delta M = 3$. Then

$$M_Z = M_Y + 3 = 5.0+3.0 = 8.0.$$

**Answer.** (a) $100$ times the amplitude and $1000$ times the energy; (b) magnitude $8.0$.

**Check.** $10^{1.5(3)} = 10^{4.5} = 31{,}623$ ✓, and $1000 = 10^{3}$ ✓.

**Remark.** An $M=8.0$ earthquake is not "three times" an $M=5.0$; it shakes the ground $1000$ times as much and releases a billion times the energy of one magnitude unit less. Words like "three times bigger" are simply wrong on a logarithmic scale.

## Advanced

**26.**

**Strategy.** Doubling time is defined by an identity in $t$; set it up, cancel, and solve.

(a) The definition is $Q(t+T_2) = 2Q(t)$ for all $t$. Write $Q(t) = Q_0b^{t}$:

$$Q_0b^{\,t+T_2} = 2Q_0b^{t} \;\Longrightarrow\; b^{\,t+T_2} = 2b^{t} \;\Longrightarrow\; b^{t}b^{T_2} = 2b^{t} \;\Longrightarrow\; b^{T_2} = 2.$$

The factor $b^{t}$ cancels because $b^{t}>0$; this is exactly where $Q_0$ disappears, and why the doubling time is a property of the *rate* alone. Taking logarithms,

$$T_2 = \frac{\ln 2}{\ln b}.$$

(b) Exact versus rule, with percentage error $(72/R - T_2)/T_2$:

| $R$ | $T_2 = \ln2/\ln(1+R/100)$ | $72/R$ | error of rule |
|---|---|---|---|
| $2\%$ | $35.003$ | $36.0$ | $+2.85\%$ |
| $7\%$ | $10.2448$ | $10.2857$ | $+0.40\%$ |
| $20\%$ | $3.8018$ | $3.60$ | $-5.31\%$ |

**Answer.** $T_2 = \ln 2/\ln b$, independent of $Q_0$. The rule of 72 is best near $7$–$8\%$ and gets steadily worse as the rate rises; it is also systematically too large at small rates.

**Why the error changes sign.** The rule approximates $\ln(1+x)$ by $x$ in the denominator and $\ln 2 \approx 0.693$ by $0.72$ in the numerator. At small $x$ the numerator error (about $+3.9\%$) dominates; at large $x$ the denominator error ($\ln(1+x)$ much less than $x$) dominates and reverses the sign. The two errors cancel near $R \approx 7.8\%$, which is why the rule is remembered with $72$ rather than $69.3$.

**27.**

**Strategy.** Recognise the standard limit $(1+1/m)^{m}\to e$ and substitute $m = n/r$.

(a) Write

$$\left(1+\frac rn\right)^{nt} = \left[\left(1+\frac rn\right)^{n/r}\right]^{rt}.$$

Let $m = n/r$; as $n\to\infty$, $m\to\infty$ and $\left(1+\frac1m\right)^{m}\to e$. The outer power is continuous, so the limit passes inside:

$$\lim_{n\to\infty}\left(1+\frac rn\right)^{nt} = e^{rt}.$$

The standard limit used is $\lim_{m\to\infty}\left(1+\frac1m\right)^{m} = e$, established in Section 7.3 of the tutorial by the monotone convergence of the sequence.

(b) With $r = 0.06$, $r_{\text{eff}} = (1+0.06/n)^{n}-1$:

| $n$ | $1$ | $2$ | $4$ | $12$ | $365$ | $\infty$ |
|---|---|---|---|---|---|---|
| $r_{\text{eff}}$ | $6.0000\%$ | $6.0900\%$ | $6.1364\%$ | $6.1678\%$ | $6.1831\%$ | $6.1837\%$ |

The sequence increases with $n$ towards $e^{0.06}-1 = 6.18365\%$.

**Answer.** The largest possible gain is the gap between annual and continuous compounding at the same nominal rate: $6.1837\% - 6.0000\% = 0.1837$ percentage points, i.e. about $3\%$ more interest per year than the nominal figure suggests.

**Check.** $1.06^{1} = 1.06$; $1.03^{2} = 1.0609$; $1.015^{4} = 1.061364$; $1.005^{12} = 1.061678$ ✓. Each $n$ is a finer subdivision of the same nominal rate, and the gains shrink quickly — most of the benefit is already present at monthly compounding.

**Remark.** The limit is approached from below and the table *suggests* monotonicity; a proof that $(1+r/n)^{n}$ increases with $n$ is a standard exercise in calculus and is not assumed here.

**28.**

**Strategy.** Compute the ratio and the transformed slope directly.

(a) For $y = ab^{x}$ with $a>0$, $b>1$:

$$\frac{y(x+h)}{y(x)} = \frac{ab^{x+h}}{ab^{x}} = b^{h},$$

which depends on $h$ but not on $x$. So equal $x$-steps always multiply $y$ by the same factor $b^{h}$; in particular with $h=1$ the successive ratios of the table are all $b$.

(b) $\log y = \log a + x\log b$, a line in $x$ with slope $\log b$. To double, $\log y$ must increase by $\log 2$, so

$$\Delta x = \frac{\log 2}{\log b}.$$

**Answer.** Both statements proved; the doubling distance is $\log2/\log b$, the same number as $T_2$ when $x$ is time.

**Remark.** Part (a) is the *test* for exponential behaviour in a table with equal spacing; part (b) is the *measurement* of the same parameter from a graph. They are the same number $b$ seen two ways, which is why a semi-log plot is a valid way to read a doubling time.

**29.**

**Strategy.** Convert between bases with $\ln X = (\ln 10)(\log X)$.

(a) With base $10$: $\log y = \log a + p\log x$ — slope $p$, intercept $\log a$.
With base $e$: $\ln y = \ln a + p\ln x$ — slope $p$, intercept $\ln a$.
Since $\ln a = (\ln 10)\log a$, the slope is unchanged and the intercept is multiplied by $\ln 10 = 2.302585$.

(b) If the vertical axis is $\ln y$ but the horizontal is $\log x$, then

$$\ln y = \ln a + p\ln x = \ln a + p(\ln 10)\log x,$$

so the plotted slope is $p\ln 10$, not $p$. For $y = 3x^{2}$ the apparent slope would be

$$2(2.302585) = 4.60517.$$

**Answer.** (a) slope unchanged, intercept scaled by $\ln 10$; (b) the mixed plot shows slope $4.605$, which is $p\ln 10$ — reading it as the exponent gives an answer $2.3$ times too large.

**Remark.** The safe rule is: plot both axes in the same base. If software insists on automatic axes, check the tick labels — "10, 100, 1000" is base $10$; "$e$, $e^{2}$, $e^{3}$" is base $e$.

**30.**

**Strategy.** Each part is a short algebraic identity; do them in the order that builds up.

(a) Set $t=0$: $e^{0} = 1$, so $P(0) = \dfrac{K}{1+A} = \dfrac{K}{1+(K-P_0)/P_0} = \dfrac{K}{(P_0+K-P_0)/P_0} = \dfrac{KP_0}{K} = P_0$.

(b) Since $K>0$, $A>0$ and $e^{-rt}>0$, the denominator $1+Ae^{-rt}>1$, hence

$$0 < P(t) = \frac{K}{1+Ae^{-rt}} < K.$$

(c) Complete the square in $P$:

$$P\left(1-\frac PK\right) = P - \frac{P^{2}}{K} = -\frac1K\left(P^{2}-KP\right) = -\frac1K\left[\left(P-\frac K2\right)^{2} - \frac{K^{2}}{4}\right] = \frac{K}{4} - \frac1K\left(P-\frac K2\right)^{2}.$$

So $rP(1-P/K) = \dfrac{rK}{4} - \dfrac{r}{K}\left(P-\dfrac K2\right)^{2} \le \dfrac{rK}{4}$, with equality exactly when $P = K/2$. Since the logistic $P(t)$ increases continuously through all values between $P_0$ and $K$ (it is strictly increasing, as $e^{-rt}$ is strictly decreasing), the value $P = K/2$ is attained, so the maximum rate is $rK/4$.

(d) $P = K/2$ means $\dfrac{K}{1+Ae^{-rt}} = \dfrac K2$, i.e. $1+Ae^{-rt} = 2$, i.e. $Ae^{-rt} = 1$. Taking logarithms, $\ln A - rt = 0$, so $t_0 = \dfrac{\ln A}{r}$.

(e) With $Ae^{-rt_0} = 1$:

$$P(t_0+s) = \frac{K}{1+e^{-rs}}, \qquad P(t_0-s) = \frac{K}{1+e^{rs}}.$$

Then

$$\frac{1}{1+e^{rs}} = \frac{e^{-rs}}{e^{-rs}+1}, \qquad \text{so} \qquad P(t_0-s) = \frac{Ke^{-rs}}{1+e^{-rs}}.$$

Adding,

$$P(t_0+s)+P(t_0-s) = \frac{K(1+e^{-rs})}{1+e^{-rs}} = K. \qquad \blacksquare$$

**Answer.** All five statements proved.

**Check.** With $K=1000$, $r=0.5$, $P_0=50$: $A=19$, $t_0 = \ln 19/0.5 = 5.889$, and at $s=0$ the identity gives $P(t_0) = 500 = K/2$ ✓. At $s=1$: $P(6.889) = 1000/(1+e^{-0.5}) = 622.5$ and $P(4.889) = 1000/(1+e^{0.5}) = 377.5$, and $622.5+377.5 = 1000.0$ ✓.

**31.**

**Strategy.** Compute each interval's own geometric mean rate; then compare the *meaning* of the two numbers.

(a) 1971–2000: $\dfrac{42\times10^{6}}{2300} = 18{,}260.9$ over $29$ years, so $r = 18{,}260.9^{1/29} = 1.40265$ and

$$T_2 = \frac{\ln 2}{\ln 1.40265} = 2.0485 \text{ years}.$$

2000–2010: $\dfrac{1.17\times10^{9}}{42\times10^{6}} = 27.857$ over $10$ years, so $r = 27.857^{1/10} = 1.39474$ and

$$T_2 = \frac{\ln 2}{0.332716} = 2.0833 \text{ years}.$$

(b) The two estimates agree to about $1.7\%$ — impressive, and enough to support "transistor count per chip has doubled roughly every two years over four decades". It does **not** support "without exception", for three reasons.

* Two intervals, each summarised by two endpoints, cannot establish an exceptionless law; a single year's product does not define the trend, and the choice of "transistor count" (logic only? cache included? per die or per package?) changes the numbers.
* The claim is about a *rate* estimated from two points per interval, so each estimate has no error bar at all. Agreement of two such estimates is weaker evidence than it looks.
* Moore's observation was a *forecast and an industry target*, not a law of nature; it held because the industry organised itself around it.

The transistor count is also not performance. Clock frequency stopped rising at about $4$ GHz around $2005$ because of power and heat limits, so single-thread performance stopped doubling every two years even while transistor counts continued to grow — the extra transistors went into parallelism and cache. Quoting transistor doubling as a performance law overstates what the data show.

**Answer.** $2.05$ years and $2.08$ years; the agreement supports a trend, not a law.

**Check.** $2^{10/2.0833} = 2^{4.80} = 27.86$ ✓, recovering the ten-year factor.

## Challenge

**32.**

**Strategy.** Compare a two-parameter exponential *fitted* to two points with a logistic whose $K$ is fixed independently and whose $r$ is fitted to the same two points. Then look at the held-back points.

(a) Exponential through $(0,10)$ and $(2,25.0322)$: $a = 10$ and

$$b = \left(\frac{25.0322}{10}\right)^{1/2} = \sqrt{2.50322} = 1.58216.$$

Predictions $10(1.58216)^{t}$:

| $t$ | $4$ | $6$ | $8$ |
|---|---|---|---|
| prediction | $62.66$ | $156.85$ | $392.64$ |
| measured | $56.00$ | $102.78$ | $148.37$ |
| error | $+11.9\%$ | $+52.6\%$ | $+164.6\%$ |

(b) Logistic with $K = 200$: $A = (200-10)/10 = 19$, and $P(2) = 25.0322$ gives

$$1+19e^{-2r} = \frac{200}{25.0322} = 7.98971 \;\Longrightarrow\; e^{-2r} = \frac{6.98971}{19} = 0.367879.$$

Since $0.367879 = e^{-1}$, we get $-2r = -1$ and $r = 0.5$. Then

$$P(t) = \frac{200}{1+19e^{-0.5t}},$$

whose values are $56.00$, $102.78$, $148.37$ at $t = 4, 6, 8$ — the measured values exactly.

(c) The logistic reproduces all five points exactly; the exponential misses the last by a factor $2.6$. The evidence is therefore decisive *given* the independent estimate $K = 200$: the growth is decelerating in exactly the way a logistic with that capacity predicts. Note also the internal signal: the successive ratios $2.503, 2.237, 1.835, 1.444$ are *decreasing*, whereas a true exponential with equal time steps must have constant ratios (Exercise 28). So the data themselves already refute the exponential, without any assumption about $K$.

(d) Without the independent estimate, the five points are consistent with a whole family of logistics. For instance, $K = 250$ with a suitably reduced $r$ would also pass close to all five, and would predict a $30\%$ higher final population. What the five points *do* support is: (i) the exponential family is refuted, because the ratios fall steadily; (ii) the growth is concavely decelerating, consistent with saturation; (iii) the value of $K$ remains uncertain — and that is the quantity everyone actually wants to know.

**Answer.** Exponential predicts $62.7, 156.9, 392.6$; logistic predicts $56.0, 102.8, 148.4$; the logistic is supported, but $K$ was supplied, not derived.

**Check.** $P(4) = 200/(1+19e^{-2}) = 200/3.57137 = 56.00$ ✓. Extrapolating the logistic to $t=10$ gives $177.3$, still $11\%$ below $K$ — saturation is slow.

**33.**

**Strategy.** A power law becomes a straight line on log-log axes; the exponent is the ratio of the log differences.

(a) Using base $e$:

$$p = \frac{\ln(2.837) - \ln(1.003)}{\ln(2.00) - \ln(0.25)} = \frac{1.04275 - 0.00300}{0.69315 - (-1.38629)} = \frac{1.03975}{2.07944} = 0.49999.$$

(b) Using base $10$:

$$p = \frac{\log(2.837) - \log(1.003)}{\log(2.00) - \log(0.25)} = \frac{0.45286 - 0.00130}{0.30103 - (-0.60206)} = \frac{0.45156}{0.90309} = 0.49999.$$

The same exponent, as Property 8.7 requires.

(c) Each logarithm carries an uncertainty of about $1\%$ (i.e. $\pm0.01$ in $\ln$), so the numerator is uncertain by about $\sqrt{0.01^{2}+0.01^{2}} = 0.0141$. Then

$$\Delta p \approx \frac{0.0141}{2.079} = 0.0068,$$

so $p = 0.500 \pm 0.007$. The measurement supports $p = 1/2$ but would also be consistent with $0.507$ or $0.493$.

(d) The parameter inside an exponential must be dimensionless: $e^{L}$ with $L$ in metres is meaningless, and changing units from metres to centimetres would change every prediction. A power law has no such problem, since $(100L)^{p} = 100^{p}L^{p}$ merely rescales $a$. So *dimensional analysis alone* rules out $T = ae^{bL}$; any dimensionally consistent model here must be a power law (or a function of a dimensionless group such as $L/g t^{2}$).

**Answer.** $p = 0.500$, the same in either base, with an uncertainty of about $\pm0.007$; an exponential is impossible on dimensional grounds.

**Check.** $a = T/L^{1/2} = 1.003/0.5 = 2.006$, and $2\pi/\sqrt{9.81} = 6.28319/3.13209 = 2.00607$ ✓ — the fitted constant reproduces the theoretical one to four digits, which is a check on the whole table, not on the model.

**34.**

**Strategy.** Fix $K$ and $P_0$, fit $r$ to the last point, and *then* look at the middle point — the standard hold-out test.

(a) $K = 1000$: $A = (1000-10)/10 = 99$. From $P(4) = 69.453$:

$$1+99e^{-4r} = \frac{1000}{69.453} = 14.3983 \;\Longrightarrow\; e^{-4r} = \frac{13.3983}{99} = 0.135336.$$

Since $\ln 0.135336 = -2.00000$, we get $r = 0.5000$. Check at $t=2$:

$$P(2) = \frac{1000}{1+99e^{-1}} = \frac{1000}{1+36.4205} = 26.724,$$

against the measured $26.72$ — a relative error of $0.015\%$, i.e. within the rounding of the data.

(b) $K = 2000$: $A = 199$. From $P(4) = 69.453$:

$$1+199e^{-4r} = \frac{2000}{69.453} = 28.7966 \;\Longrightarrow\; e^{-4r} = \frac{27.7966}{199} = 0.139682,$$
$$-4r = \ln 0.139682 = -1.96840 \;\Longrightarrow\; r = 0.49210.$$

Check at $t=2$:

$$P(2) = \frac{2000}{1+199e^{-0.98420}} = 26.534,$$

against $26.72$ — a relative error of $0.7\%$, still inside typical measurement noise.

(c) At $t=10$:

* $K=1000$ model: $P(10) = \dfrac{1000}{1+99e^{-5}} = \dfrac{1000}{1.66705} = 599.9$.
* $K=2000$ model: $P(10) = \dfrac{2000}{1+199e^{-4.9210}} = \dfrac{2000}{2.45108} = 816.0$.

The two differ by $36\%$, although both reproduce the data — one to $0.015\%$, the other to $0.7\%$.

(d) This is **identifiability**: while the population is far below the capacity, every large enough $K$ can be compensated by a smaller $r$ to give almost the same curve. Doubling the assumed capacity changed the fit on the observed range by less than $1\%$ and the prediction a few years out by more than a third. A carrying capacity estimated from data far below it is therefore a *guess dressed as a parameter*; it needs independent support (a physical constraint, a nutrient budget, or observations near saturation) before any extrapolation can be believed.

**Answer.** $r = 0.5000$ (error $0.015\%$) for $K=1000$; $r = 0.4921$ (error $0.7\%$) for $K=2000$; predictions $600$ versus $816$ at $t=10$.

**Check.** $P(2)$ for the first model: $e^{-1} = 0.367879$, $99(0.367879) = 36.420$, $1000/37.420 = 26.72$ ✓. Also $\ln 0.135336 = -2$ exactly, which is why the "fit" is exact — the data were constructed from $K=1000$, $P_0=10$, $r=0.5$.

**35.**

**Strategy.** Use the two logarithm laws; nothing else is needed.

(a) For $b>0$, $b\ne1$ and positive $x_i$:
$$\log_b x_2 - \log_b x_1 = \log_b\!\left(\frac{x_2}{x_1}\right), \qquad \log_b x_3 - \log_b x_2 = \log_b\!\left(\frac{x_3}{x_2}\right).$$
If $x_2/x_1 = x_3/x_2 = r$, both differences equal $\log_b r$. So equal ratios are equally spaced, and the spacing is $\log_b r$.

(b) $L_1 - L_2 = c\log_{10}(Q_1/Q_0) - c\log_{10}(Q_2/Q_0) = c\log_{10}\!\left(\frac{Q_1/Q_0}{Q_2/Q_0}\right) = c\log_{10}\!\left(\frac{Q_1}{Q_2}\right)$.
Dividing by $c$ and exponentiating: $\dfrac{Q_1}{Q_2} = 10^{(L_1-L_2)/c}$. $\blacksquare$

(c) On a slide rule, lengths are proportional to logarithms, so placing two lengths end to end *adds* logarithms:

$$\log x + \log y = \log(xy).$$

Adding lengths therefore multiplies the numbers, and no multiplication table is needed. A scale covering one decade from $1$ to $10$ has, by part (a), a single spacing $\log_{10}10 = 1$, so its full length $L$ represents exactly one decade; the interval from $1$ to $10$ is the whole scale, of length $L$. Likewise $1$ to $2$ occupies $0.301L$ — the same $30.1\%$ of the scale as $\log_{10}2$.

**Answer.** All three proved; the $1$–$10$ interval is the whole decade, length $L$.

**Remark.** Part (a) is the reason a log axis can be printed at all: the position of $2$ inside any decade is always $30.1\%$ of the way along, so one template serves every decade. Part (b) is the reason every scale in Section 7.7 reduces to "a difference of readings is a ratio".

**36.**

**Strategy.** Part (a) is a ratio of two explicit expressions; part (b) is an inequality obtained by bounding a fraction; parts (c)–(d) are interpretation.

(a) With $P_0 = \dfrac{K}{1+A}$,

$$P_0e^{rt} = \frac{Ke^{rt}}{1+A}, \qquad P(t) = \frac{K}{1+Ae^{-rt}} = \frac{Ke^{rt}}{e^{rt}+A},$$

so

$$\frac{P_0e^{rt}}{P(t)} = \frac{Ke^{rt}}{1+A}\cdot\frac{e^{rt}+A}{Ke^{rt}} = \frac{e^{rt}+A}{1+A},$$

which is the stated identity.

(b) Since $u = Ae^{-rt}$ gives $e^{rt} = A/u$,

$$\frac{P_0e^{rt}}{P(t)} = \frac{A + A/u}{1+A} = \frac{A}{1+A}\left(1+\frac1u\right) \le 1+\frac1u,$$

because $\dfrac{A}{1+A}<1$ and $1+\dfrac1u>1$. The ratio is also at least $1$ for $t \ge 0$, since $e^{rt}\ge1$ makes the numerator at least $1+A$. Therefore

$$1 \le \frac{P_0e^{rt}}{P(t)} \le 1+\frac1u,$$

i.e. the logistic never falls below the exponential by more than the fraction $\dfrac{1/u}{1+1/u} < \dfrac1u$. When $u \ge 20$ this is at most $5\%$ (indeed at most $4.76\%$).

(c) If $P(t) \le K/21$ then, since $P = K/(1+u)$, we have $1+u \ge 21$, i.e. $u \ge 20$. By (b) the logistic curve and the exponential $P_0e^{rt}$ agree to within $5\%$ everywhere in that range — and a real measurement of a population has noise of at least that order. Hence such data cannot distinguish the two families, *regardless of how many points are taken*, because the discrepancy is below the noise floor for the whole range. The modeller must (i) obtain a measurement near or beyond $K/2$, (ii) fix $K$ independently from the physics or biology of the system, or (iii) report the prediction as conditional on an assumed $K$ rather than as a prediction.

(d) A reasonable plan: sample densely in *log time* while the population is small (to pin down $r$), then continue with roughly equal spacing through and past the inflection, where the curvature is largest and $K$ becomes identifiable; if a saturation plateau is reached, keep sampling there to bound $K$ from below. Plot $\ln P$ against $t$ first (to see whether the early phase is exponential and to estimate $r$), then $1/P$ against $e^{-rt}$ (or the logit $\ln((K-P)/P)$ against $t$) to check the logistic form. Validate on held-back points at the *highest* populations, not by $R^2$ over the whole set.

Two ways it can still fail: (i) the environment changes during the experiment — nutrients deplete, a predator arrives, the temperature shifts — so that a constant $K$ is the wrong assumption and the "carrying capacity" is really a moving target; (ii) the measurement itself saturates (a plate reader or a counter that stops responding at high concentrations), producing an apparent plateau that is instrumental rather than biological. A third, commoner than either: the process is not logistic at all — an Allee effect, seasonality, or oscillations can all produce an S-shaped stretch that extrapolates badly.

**Answer.** (a) and (b) proved; (c) the discrepancy is bounded by $1/u \le 5\%$ while $P \le K/21$, so $K$ is not identifiable from such data; (d) a plan as described, with the stated failure modes.

**Remark.** Part (b) is the quantitative form of the warning in Section 7.8: "identifiability is a property of the data, not of the software". A fitting routine will always return a number for $K$; whether that number means anything is a question about the range you measured.
