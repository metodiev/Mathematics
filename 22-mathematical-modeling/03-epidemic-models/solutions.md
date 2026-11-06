# Epidemic Models — Solutions

> [Epidemic Models](README.md) · Solutions to the 36 problems in [exercises.md](exercises.md)

Each solution states the strategy, carries out every significant step and ends with a check where one is
available. Section references point into the [tutorial](README.md).

## Beginner

**1.** *(Strategy: the two formulas $R_0=\beta/\gamma$ and $r=\beta-\gamma$, then the decomposition
$\beta = cp$.)*

(a) $R_0 = \beta/\gamma = 0.8/0.25 = 3.2$. The mean infectious period is $1/\gamma = 4$ days.

(b) $r = \beta-\gamma = 0.8-0.25 = 0.55$ per day, so

$$T_d = \frac{\ln 2}{r} = \frac{0.69315}{0.55} = 1.2603\ \text{days}.$$

(c) $\beta = cp$, so $p = \beta/c = 0.8/10 = 0.08$: each close contact transmits with probability
$8\%$.

*Check:* $R_0 = 1 + r/\gamma = 1 + 0.55/0.25 = 3.2$, consistent with (a). ✓

**2.** *(Strategy: invert $R_0=\beta/\gamma$; then use the contact decomposition.)*

(a) $\beta = R_0\gamma = 4 \times \frac17 = 0.57143$ per day.

(b) $p = \beta/c = 0.57143/10 = 0.057143$.

(c) Halving the infectious period doubles $\gamma$ to $2/7 = 0.28571$ per day; with $\beta$ unchanged,

$$R_0^{\text{new}} = \frac{0.57143}{0.28571} = 2 .$$

So $R_0$ halves. This is the arithmetic of isolation: shortening the infectious period is as effective
as reducing transmission per contact.

*Check:* $R_0^{\text{new}} = R_0/2 = 2$, and $R_0 = \beta \times T_{\text{inf}}$ shows the dependence
directly. ✓

**3.** *(Strategy: add the equations; check each face; quote smoothness.)*

(a) Differentiating the sum and substituting,

$$(S+I+R)' = -\frac{\beta SI}{N} + \left(\frac{\beta SI}{N}-\gamma I\right) + \gamma I = 0 .$$

Hence $S+I+R$ is constant, and it equals $N$ for all $t$ by the initial condition.

(b) On the face $S=0$: $S' = -\beta\cdot0\cdot I/N = 0$, so a solution with $S=0$ stays on the face. On
$I=0$: $I' = 0 - \gamma\cdot0 = 0$. On $R=0$: $R' = \gamma I \ge 0$, so the flow points into the
simplex. Since the boundary consists of these three faces and the vector field is tangent or inward on
each, a trajectory starting in the interior cannot cross the boundary (by uniqueness it cannot touch and
leave). Hence the simplex is positively invariant.

(c) The right-hand side is a polynomial in $(S,I,R)$, hence continuously differentiable with locally
bounded derivatives, so the existence–uniqueness theorem applies and gives a unique local solution;
boundedness of the vector field on the compact simplex extends it to all $t\ge0$.

*Check:* the invariant region and the conservation law are the two facts that make the planar reduction
valid. ✓

**4.** *(Strategy: evaluate $1-1/R_0$.)*

| $R_0$ | $2$ | $4$ | $8$ | $16$ |
|---|---|---|---|---|
| $p_c$ | $0.5$ | $0.75$ | $0.875$ | $0.9375$ |

Each doubling of $R_0$ halves the *remaining* gap $1-p_c = 1/R_0$: $0.5, 0.25, 0.125, 0.0625$. As
$R_0\to\infty$, $1/R_0\to0$ and $p_c\to1$: a sufficiently transmissible infection requires essentially
universal immunity.

*Check:* $p_c$ is increasing in $R_0$ and $p_c<1$ for every finite $R_0$. ✓

**5.** *(Strategy: bisection on $g(z)=1-z-e^{-R_0z}$, using the sign change from Theorem 7.2.)*

(a) $R_0 = 1.5$: $g(0.5) = 0.5-e^{-0.75} = 0.5-0.47237 = 0.02763 > 0$;
$g(0.6) = 0.4-e^{-0.9} = 0.4-0.40657 = -0.00657 < 0$. Root in $(0.5,0.6)$. Refining,

$$z = 0.58281 .$$

So $58.3\%$ are infected and $41.7\%$ escape.

(b) $R_0 = 4$: $g(0.97) = 0.03-e^{-3.88} = 0.03-0.02066 = 0.00934 > 0$;
$g(0.985) = 0.015-e^{-3.94} = 0.015-0.01946 = -0.00446 < 0$. Root in $(0.97,0.985)$. Refining,

$$z = 0.98017 .$$

So $98.0\%$ are infected and only $2.0\%$ escape.

*Interpretation.* A fourfold increase in $R_0$ raises the final size from $58\%$ to $98\%$; the
herd-immunity thresholds for the same values are $33.3\%$ and $75.0\%$, so both epidemics overshoot
substantially.

*Check:* both roots satisfy $1-z = e^{-R_0z}$ to the accuracy stated, and both lie below $1$. ✓

**6.** *(Strategy: substitute into the peak-height formula; compare with $1-1/R_0$.)*

$$R_0 = 2: \quad \frac{I_{\text{peak}}}{N} = 1-\frac{1+\ln2}{2} = 1-\frac{1.69315}{2} = 0.15343 .$$
$$R_0 = 4: \quad \frac{I_{\text{peak}}}{N} = 1-\frac{1+\ln4}{4} = 1-\frac{2.38629}{4} = 0.40343 .$$

The herd immunity thresholds are $0.5$ and $0.75$, both larger than the peak heights. The peak is the
maximum *prevalence*; the threshold is a *cumulative* fraction immune. They are different quantities and
there is no reason for one to be below the other in general — in these examples the peak prevalence
happens to be below the threshold because the epidemic is spread out in time.

*Check:* both peaks are in $(0,1)$ and increase with $R_0$. ✓

**7.** *(Strategy: match the biology to the compartments.)*

(a) **SEIR.** Lifelong immunity rules out SIS; the two-day latent period is exactly the $E$ compartment.

(b) **SIS.** No immunity after recovery means recovered individuals return to $S$; no latent period means
no $E$.

(c) **SIR.** Lifelong immunity, no latent period: the minimal model.

(d) **None of the three; an SIRS model is needed.** Immunity lasting about six months means recovered
individuals return to $S$ at rate $\omega = 1/(180\ \text{days})$, so the model needs an $S\to I\to R\to S$
loop. If forced to choose among the three, SIS is closer than SIR, because it at least allows
reinfection, but it wrongly sets the immune period to zero.

*Check:* the compartment diagram of §10.3 encodes exactly these decisions. ✓

**8.** *(Strategy: evaluate the constant at $t=0$ and solve for $I$.)*

At $t=0$, $S=N$ and $I=0$, so the constant is

$$0 + N - \frac{N}{2}\ln N = N\left(1-\frac{\ln N}{2}\right).$$

At a general $S$,

$$I = -S + \frac{N}{2}\ln S + N\left(1-\frac{\ln N}{2}\right),$$

so, dividing by $N$ and writing $s = S/N$,

$$\frac{I}{N} = 1 - s + \frac{1}{2}\ln s .$$

At $s = 0.8$: $\ln 0.8 = -0.22314$, so

$$\frac{I}{N} = 1-0.8+\frac{1}{2}(-0.22314) = 0.2-0.11157 = 0.08843 .$$

*Growth?* $I' = I(\beta S/N-\gamma) = \gamma I(R_0 s - 1) = \gamma I(2(0.8)-1) = 0.6\gamma I > 0$. The
epidemic is still growing; the peak occurs at $s = 1/R_0 = 0.5$.

*Check:* the formula gives $I/N = 0$ at $s=1$, and the value at $s=0.8$ is positive and below the peak
value $0.15343$. ✓

**9.** *(Strategy: $R_{\text{eff}} = R_0S/N$; compare with $1$.)*

At $S/N = 0.4$: $R_{\text{eff}} = 3(0.4) = 1.2 > 1$, so the epidemic is growing.
At $S/N = 0.3$: $R_{\text{eff}} = 3(0.3) = 0.9 < 1$, so the epidemic is declining.

The crossover is at $S/N = 1/3$, which is the peak: $S = N/R_0$.

*Check:* the two values straddle $1$ and the threshold $1/3$ lies between $0.3$ and $0.4$. ✓

**10.** *(Strategy: $p_c = 1-1/R_0$ and $p_c = (1-1/R_0)/\varepsilon$.)*

(a) $p_c = 1-1/2.5 = 0.6$, i.e. $60\%$.

(b) With $\varepsilon = 0.8$: $p_c = 0.6/0.8 = 0.75$, i.e. $75\%$ coverage.

(c) The minimum efficacy for elimination at $100\%$ coverage is
$\varepsilon_{\min} = 1-1/R_0 = 0.6$.

*Check:* $p_c$ rises as $\varepsilon$ falls, and $p_c\le1$ exactly when $\varepsilon\ge0.6$. ✓

**11.** *(Strategy: solve $q=e^{-R_0(1-q)}$ by iteration or bisection, taking the smallest root in
$[0,1)$.)*

$R_0 = 1.5$: $q = e^{-1.5(1-q)}$. Iterating from $q_0 = 0.5$:
$q_1 = e^{-0.75} = 0.47237$, $q_2 = e^{-1.5(0.52763)} = e^{-0.79145} = 0.45320$,
$q_3 = e^{-1.5(0.54680)} = e^{-0.82020} = 0.44041$, continuing to convergence gives $q = 0.41719$.
So a single introduction starts a major outbreak with probability $1-q = 0.58281$.

$R_0 = 2.5$: $q = e^{-2.5(1-q)}$ gives $q = 0.10736$, so a major outbreak occurs with probability
$0.89264$.

*Interpretation.* The higher the reproduction number, the less likely a single case is to fizzle, but
even at $R_0 = 2.5$ about one introduction in nine fails.

*Check:* both $q$ values lie in $(0,1)$, both decrease as $R_0$ increases, and $q\to1$ as
$R_0\downarrow1$. ✓

**12.** *(Strategy: match each statement to the definitions.)*

(a) **False.** $R_0$ depends on contact rates and on the duration of infectiousness, which are properties
of the population and of behaviour; two settings can have different $R_0$ for the same pathogen.

(b) **False.** $R_0 = 2$ gives a herd immunity threshold of $50\%$, but the final size is $79.7\%$
(§7.4). The two numbers answer different questions.

(c) **False.** $R_0<1$ is a statement about the *average* number of secondary cases. A case can still
infect several people; it is the average that is below $1$, so chains die out eventually but not
immediately.

(d) **False.** The threshold is the fraction immune at which transmission stops growing; the final size
(the fraction ever infected) is larger because of overshoot.

(e) **True.** The epidemic turns when $S$ falls below $N/R_0$; that is the content of §7.2 and §7.4.

(f) **False.** $R_0$ and $r$ are related by $r = \gamma(R_0-1)$ in the SIR model and by
$(r+\sigma)(r+\gamma)=\sigma\beta$ in SEIR; converting one to the other needs the generation time.

## Intermediate

**13.** *(Strategy: eliminate time by dividing the two equations, then integrate over the whole epidemic.)*

*Step 1: the quotient.* For $I>0$ and $S>0$,

$$\frac{dI}{dS} = \frac{I'}{S'} = \frac{\beta SI/N - \gamma I}{-\beta SI/N} = -1 + \frac{\gamma N}{\beta S} = -1 + \frac{N}{R_0S},$$

using $R_0 = \beta/\gamma$. This is a separable first-order equation for $I$ as a function of $S$; note
that it is valid along any orbit on which $S$ and $I$ are positive.

*Step 2: integrate.* Integrating with respect to $S$,

$$I(S) = -S + \frac{N}{R_0}\ln S + C .$$

*Step 3: fix the constant.* At $t=0$, $S=S_0$ and $I=I_0$, so
$C = I_0 + S_0 - (N/R_0)\ln S_0$. Hence

$$I(S) = I_0 + (S_0-S) + \frac{N}{R_0}\ln\frac{S}{S_0}.$$

*Step 4: take the limit.* As $t\to\infty$, $S\to S_\infty$ and $I\to0$ (§7.2). Substituting,

$$0 = I_0 + (S_0-S_\infty) + \frac{N}{R_0}\ln\frac{S_\infty}{S_0}.$$

*Step 5: divide by $N$ and let the initial seed vanish.* With $s_0 = S_0/N$, $i_0 = I_0/N$ and
$s_\infty = S_\infty/N$,

$$0 = i_0 + s_0 - s_\infty + \frac{1}{R_0}\ln\frac{s_\infty}{s_0}.$$

For $s_0 = 1$ and $i_0\to0$ this is $0 = 1 - s_\infty + \frac{1}{R_0}\ln s_\infty$, i.e.

$$1-s_\infty = -\frac{1}{R_0}\ln s_\infty = \frac{1}{R_0}\ln\frac{1}{s_\infty},$$

and exponentiating gives $s_\infty = e^{-R_0(1-s_\infty)}$, which is $1-z = e^{-R_0z}$ with
$z = 1-s_\infty$.

*Assumptions used.* (i) The population is closed and homogeneously mixed, so the equations are the SIR
equations; (ii) $I(t)\to0$ and $S(t)\to S_\infty>0$, which was proved in §7.2; (iii) $S$ is strictly
decreasing while $I>0$, so $S$ can be used as a parameter along the orbit; (iv) the initial infectious
fraction is negligible, which is what allows $i_0\to0$. If $i_0$ is not negligible, the exact relation
retains the $i_0$ term and $z$ is slightly larger.

*Check:* putting $s_\infty = 1-z$ into the equation reproduces $1-z = e^{-R_0z}$; for $R_0=2$ the
numeric solution $z = 0.7968$ satisfies $e^{-2(0.7968)} = e^{-1.5936} = 0.2032 = 1-z$. ✓

**14.** *(Strategy: maximise $I$ as a function of $S$, using the first integral; then justify that this
gives the maximum in time.)*

*Stationary point.* From $I(S) = -S + (N/R_0)\ln S + C$,

$$\frac{dI}{dS} = -1 + \frac{N}{R_0S}, \qquad \frac{d^2I}{dS^2} = -\frac{N}{R_0S^2} < 0 .$$

The second derivative is negative everywhere, so $I$ is a strictly concave function of $S$, and its
unique maximum on $(0,N]$ is where $dI/dS = 0$:

$$-1 + \frac{N}{R_0S} = 0 \quad\Longrightarrow\quad S = \frac{N}{R_0}.$$

*Value.* With initial data $(S,I) = (N,0)$ the constant is $C = N - (N/R_0)\ln N$, so

$$I_{\text{peak}} = -\frac{N}{R_0} + \frac{N}{R_0}\ln\frac{N}{R_0} + N - \frac{N}{R_0}\ln N = N - \frac{N}{R_0} - \frac{N}{R_0}\ln R_0 .$$

Dividing by $N$,

$$\frac{I_{\text{peak}}}{N} = 1 - \frac{1}{R_0} - \frac{\ln R_0}{R_0} = 1 - \frac{1+\ln R_0}{R_0}.$$

*Why this is a maximum in time.* $S(t)$ is strictly decreasing while $I>0$ (because $S' = -\beta SI/N<0$),
so the map $t\mapsto S(t)$ is a bijection from the growth phase onto an interval of $S$ values. Since $I$
as a function of $S$ has a single interior maximum, $I$ as a function of time does too, and it occurs at
the same state $S = N/R_0$. Equivalently, $I' = I(\beta S/N - \gamma) = \gamma I(R_0S/N-1)$ changes sign
from $+$ to $-$ exactly when $S$ crosses $N/R_0$ from above.

*Check:* at $R_0 = 2$ the formula gives $1-(1+0.69315)/2 = 0.15343$, positive and less than $1$; as
$R_0\downarrow1$ it tends to $0$, and as $R_0\to\infty$ it tends to $1$. ✓

**15.** *(Strategy: the next-generation matrix for the infected pair; then the characteristic quadratic.)*

(a) The infected compartments are $(E,I)$ and

$$F = \begin{pmatrix} 0 & \beta \\ 0 & 0\end{pmatrix}, \qquad V = \begin{pmatrix} \sigma & 0 \\ -\sigma & \gamma\end{pmatrix}, \qquad V^{-1} = \begin{pmatrix} 1/\sigma & 0 \\ 1/\gamma & 1/\gamma\end{pmatrix},$$

$$K = FV^{-1} = \begin{pmatrix} \beta/\gamma & \beta/\gamma \\ 0 & 0\end{pmatrix}, \qquad R_0 = \rho(K) = \frac{\beta}{\gamma} = \frac{0.5}{0.1} = 5 .$$

(b) The characteristic equation is $(r+\sigma)(r+\gamma) = \sigma\beta$:

$$(r+0.25)(r+0.1) = 0.25(0.5) = 0.125 \quad\Longrightarrow\quad r^2 + 0.35r + 0.025 - 0.125 = 0,$$

$$r^2+0.35r-0.1 = 0 \quad\Longrightarrow\quad r = \frac{-0.35\pm\sqrt{0.1225+0.4}}{2} = \frac{-0.35\pm0.72284}{2}.$$

The positive root is $r = 0.18642$ per day; the doubling time is $\ln2/0.18642 = 3.7184$ days.

(c) The negative root is $r_- = -0.53642$. It is the second eigenvalue of the $2\times2$ linearisation:
the general solution near the disease-free state is a combination $c_+e^{r_+t}\mathbf{v}_+ +
c_-e^{r_-t}\mathbf{v}_-$, and the negative mode decays. It does not describe the epidemic's growth; it
describes the rapid transient in which the exposed and infectious classes adjust to their ratio
$E/I = \gamma/\sigma$.

*Check:* $R_0 = 5>1$ and the positive root is positive; the product of the roots is $-0.1$, the
determinant, and their sum is $-0.35$, the negative of the coefficient of $r$. ✓

**16.** *(Strategy: $r$ from the doubling time, then the SEIR and SIR conversions.)*

(a) $r = \ln2/3 = 0.231049$ per day.

(b) With $\sigma = 1/2 = 0.5$ and $\gamma = 1/5 = 0.2$:

$$R_0^{\text{(SEIR)}} = \left(1+\frac{r}{\sigma}\right)\left(1+\frac{r}{\gamma}\right) = (1+0.462098)(1+1.155245) = 1.462098 \times 2.155245 = 3.15118 .$$

(c) The SIR fit uses only $\gamma$:

$$R_0^{\text{(SIR)}} = 1+\frac{r}{\gamma} = 1+1.155245 = 2.15525 .$$

The error is $(3.15118-2.15525)/3.15118 = 0.316$: the SIR estimate is $31.6\%$ too small. The bias is
systematic, not random, and grows with $r/\sigma$.

*Check:* $R_0>1$ in both cases, and the SEIR value exceeds the SIR value because the latent period makes
the same growth rate compatible with more transmission. ✓

**17.** *(Strategy: invert $R_0=\beta/(\gamma+\mu)$, then use $I^{*}/N = 1-1/R_0$.)*

(a) $\beta = R_0(\gamma+\mu) = 4\left(0.1+\frac{1}{3650}\right) = 4(0.100274) = 0.401096$ per day.

(b) $S^{*}/N = 1/R_0 = 0.25$ and $I^{*}/N = 1-1/R_0 = 0.75$.

(c) The demographic term changes $\gamma+\mu$ from $0.1$ to $0.100274$, a relative change of $0.27\%$.
It is negligible for this infection, because the mean infectious period (ten days) is far shorter than
the mean lifetime (ten years). Demography matters when the two time scales are comparable, as they are
for chronic infections with long durations.

*Check:* $S^{*}+I^{*} = N$, and $S^{*}/N = 1/R_0$ is the condition $R_{\text{eff}} = 1$. ✓

**18.** *(Strategy: solve the logistic equation by separation.)*

The equation separates:

$$\frac{dI}{I\left(1-\frac{I}{I^{*}}\right)} = \gamma(R_0-1)\,dt .$$

Using partial fractions $\dfrac{1}{I(1-I/I^{*})} = \dfrac{1}{I} + \dfrac{1/I^{*}}{1-I/I^{*}}$, integrating
and solving for $I$ gives

$$I(t) = \frac{I^{*}}{1+\left(\dfrac{I^{*}-I_0}{I_0}\right)e^{-\gamma(R_0-1)t}} .$$

Setting $I(t) = I_1$ and solving for $t$:

$$t = \frac{1}{\gamma(R_0-1)}\ln\frac{I_1\,(I^{*}-I_0)}{I_0\,(I^{*}-I_1)} .$$

With $I^{*} = 0.5N$, $I_0 = 0.01N$, $I_1 = 0.25N$:

$$\frac{I_1(I^{*}-I_0)}{I_0(I^{*}-I_1)} = \frac{0.25(0.49)}{0.01(0.25)} = \frac{0.1225}{0.0025} = 49, \qquad t = \frac{\ln 49}{0.1} = 38.92\ \text{days}.$$

*Interpretation.* Even at $R_0 = 2$ the SIS prevalence takes almost six weeks to rise from $1\%$ to
$25\%$ of its eventual $50\%$ level; the logistic approach to the endemic equilibrium slows down as the
gap closes.

*Check:* $I(0) = I^{*}/(1+(0.49/0.01)) = 0.5/(1+49) = 0.01$ ✓, and $t$ is positive. ✓

**19.** *(Strategy: $p_c = (1-1/R_0)/\varepsilon$.)*

(a) $p_c = (1-1/5)/0.85 = 0.8/0.85 = 0.94118$: $94.1\%$ coverage.

(b) With $\varepsilon = 1$: $p_c = 0.8$, i.e. $80\%$.

(c) The imperfect vaccine adds $14.1$ percentage points of required coverage, but $p_c$ remains below
$1$, so elimination is still possible if coverage reaches $94.1\%$. The criterion is
$\varepsilon\ge1-1/R_0 = 0.8$, and $0.85>0.8$, so the threshold is attainable. A vaccine below $0.8$
efficacy would make elimination by vaccination alone impossible at any coverage, though it would still
reduce the burden.

*Check:* $p_c\le1$ exactly when $\varepsilon\ge1-1/R_0 = 0.8$; since $0.85>0.8$, the criterion is met. ✓

**20.** *(Strategy: independent introductions multiply the extinction probabilities.)*

$$\Pr(\text{no major outbreak}) = q^{20} = 0.0595^{20} = 3.11\times10^{-25},$$
$$\Pr(\text{at least one major outbreak}) = 1-3.11\times10^{-25} \approx 1 .$$

*Comment.* Even though a single introduction of a $R_0=3$ infection fails about $6\%$ of the time,
twenty independent introductions are essentially certain to produce an outbreak. This is why repeated
introductions defeat border measures that are individually effective, and why the number of introductions
— not only $R_0$ — determines whether an elimination programme can succeed.

*Check:* $q^{20}<1$ and the probability is at most $1$. ✓

**21.** *(Strategy: check constant ratios, then regress $\log$ incidence on time.)*

(a) The ratios are $150/100 = 1.5$, $225/150 = 1.5$, $337.5/225 = 1.5$. A constant ratio over equal time
intervals is exponential growth: $y(t) = y_0e^{rt}$ with $e^{5r} = 1.5$, so

$$r = \frac{\ln 1.5}{5} = \frac{0.405465}{5} = 0.081093\ \text{per day}.$$

Equivalently, the doubling time is $\ln2/0.081093 = 8.548$ days.

(b) With $T_{\text{inf}} = 5$ days: $R_0 = 1+rT_{\text{inf}} = 1+0.405465 = 1.40547$.

(c) With $T_{\text{inf}} = 8$ days: $R_0 = 1+8(0.081093) = 1.64874$.

The two estimates differ by $(1.64874-1.40547)/1.64874 = 14.8\%$. The data determine $r$ precisely and
$R_0$ only up to the assumed infectious period; this is the identifiability problem of §7.8 in its
simplest form.

*Check:* both $R_0$ values exceed $1$, consistent with growth, and both increase with $T_{\text{inf}}$. ✓

**22.** *(Strategy: bisection on $h(s) = s - s_0e^{-R_0(s_0-s)}$, then report $z = s_0-s_\infty$.)*

With $s_0 = 0.5$ and $R_0 = 4$, $h(s) = s-0.5e^{-4(0.5-s)}$.

$$h(0.05) = 0.05-0.5e^{-1.8} = 0.05-0.08264 = -0.03264 < 0,$$
$$h(0.10) = 0.10-0.5e^{-1.6} = 0.10-0.10095 = -0.00095 < 0,$$
$$h(0.12) = 0.12-0.5e^{-1.52} = 0.12-0.10936 = 0.01064 > 0 .$$

So the root lies in $(0.10,0.12)$; refining,

$$s_\infty = 0.10159, \qquad z = s_0-s_\infty = 0.5-0.10159 = 0.39841 .$$

So $39.8\%$ of the population is infected, against $98.0\%$ with no pre-existing immunity (Exercise 5(b)).
The reduction is $(0.98-0.398)/0.98 = 59.4\%$ — far more than the $50\%$ immune fraction, because the
immunity both reduces the susceptible pool and pushes the epidemic below its exponential regime earlier.

*Check:* $s_\infty<s_0$, $z\in(0,1)$, and $s_0\to1$ recovers the earlier case. ✓

## Advanced

**23.** *(Strategy: write the infected subsystem in the form $\mathcal{F}-\mathcal{V}$, evaluate the
Jacobians at the disease-free equilibrium, and compute the spectral radius.)*

*The splitting.* The infected compartments are $E$ and $I$:

$$\mathcal{F} = \begin{pmatrix} \beta SI/N \\ 0\end{pmatrix}, \qquad \mathcal{V} = \begin{pmatrix} \sigma E \\ \gamma I - \sigma E \end{pmatrix}.$$

Here $\mathcal{F}$ collects the terms that create new infected individuals (only the $S\to E$ flow), and
$\mathcal{V}$ collects everything that moves individuals between or out of infected compartments
($E\to I$ progression and $I\to R$ removal).

*The Jacobians at $S=N$.* Since $\mathcal{F}$ does not depend on $E$ or $I$ except through the product
$SI$, at $I=0$ we have $\partial\mathcal{F}_1/\partial I = \beta S/N = \beta$ and
$\partial\mathcal{F}_1/\partial E = 0$. Hence

$$F = \begin{pmatrix} 0 & \beta \\ 0 & 0\end{pmatrix}, \qquad V = \begin{pmatrix} \sigma & 0 \\ -\sigma & \gamma\end{pmatrix}.$$

*Inversion.* $\det V = \sigma\gamma \ne 0$ and

$$V^{-1} = \frac{1}{\sigma\gamma}\begin{pmatrix} \gamma & 0 \\ \sigma & \sigma\end{pmatrix} = \begin{pmatrix} 1/\sigma & 0 \\ 1/\gamma & 1/\gamma\end{pmatrix}.$$

*The next-generation matrix.*

$$K = FV^{-1} = \begin{pmatrix} 0 & \beta \\ 0 & 0\end{pmatrix}\begin{pmatrix} 1/\sigma & 0 \\ 1/\gamma & 1/\gamma\end{pmatrix} = \begin{pmatrix} \beta/\gamma & \beta/\gamma \\ 0 & 0\end{pmatrix}.$$

*Eigenvalues.* $\det(K-\lambda I) = (\beta/\gamma-\lambda)(-\lambda) - 0 = \lambda(\lambda-\beta/\gamma)$,
so the eigenvalues are $0$ and $\beta/\gamma$, and

$$R_0 = \rho(K) = \frac{\beta}{\gamma} = 5\ \text{(for the parameters of Exercise 15)} .$$

*Why $\sigma$ disappears.* The entry $(K)_{11}$ is the expected number of infections produced in $E$ by
an individual introduced into $E$: that individual spends a mean $1/\sigma$ in $E$, transmitting nothing,
then a mean $1/\gamma$ in $I$, transmitting at rate $\beta$, so the expected count is
$\beta\times(1/\gamma)$. The $(K)_{12}$ entry is the same count for an individual introduced directly
into $I$: again $\beta/\gamma$. The latent period delays the arrival of those infections but does not
change how many there are, so $\sigma$ cancels. What $\sigma$ does change is the *timing*, and hence the
growth rate and the peak — the content of §7.6.

*Check:* the columns of $K$ are proportional, so the rank is $1$ and the non-zero eigenvalue is the trace
$\beta/\gamma$. ✓

**24.** *(Strategy: sign of $g$ at the endpoints, concavity, and the derivative at $0$.)*

Let $g(z) = 1-z-e^{-R_0z}$ for $z\in[0,1]$, with $R_0>0$.

*Endpoints.* $g(0) = 1-0-1 = 0$, so $z=0$ is always a root — it corresponds to "no epidemic". And
$g(1) = -e^{-R_0}<0$.

*Derivatives.* $g'(z) = -1+R_0e^{-R_0z}$ and $g''(z) = -R_0^2e^{-R_0z}<0$. So $g$ is strictly concave
on $[0,1]$.

*Case $R_0\le1$.* For every $z\ge0$, $e^{-R_0z}\le1$, so
$g'(z) = -1+R_0e^{-R_0z}\le-1+R_0\le0$. Thus $g$ is non-increasing on $[0,1]$; since $g(0)=0$, we have
$g(z)<0$ for $z\in(0,1]$. The only root in $[0,1]$ is $z=0$.

*Case $R_0>1$.* Now $g'(0) = R_0-1>0$, so $g$ is positive just to the right of $0$. Since $g(1)<0$, the
intermediate value theorem gives a root in $(0,1)$.

*Uniqueness.* Suppose $0<z_1<z_2<1$ are both roots. By strict concavity, the graph on $[z_1,z_2]$ lies
strictly above the chord joining $(z_1,g(z_1))$ and $(z_2,g(z_2))$, which is the zero line; hence
$g(z)>0$ for $z\in(z_1,z_2)$. But strict concavity also implies that the chord from $(0,0)$ to
$(z_2,0)$ lies strictly above the graph on $(0,z_2)$, so $g(z)<0$ there — a contradiction, since
$z_1\in(0,z_2)$. Hence at most one root in $(0,1)$.

*Why $z=0$ does not count.* $z=0$ is the "no epidemic" solution: it satisfies the algebraic equation but
corresponds to the initial state $S=S_0=N$ with $I=0$. The equation was derived by letting $I_0\to0$ and
then asking where $S$ ends up; the branch starting at $z=0$ is the degenerate one in which no infection
ever occurs. The epidemiologically meaningful solution is the positive root, which exists exactly when
$R_0>1$ and is the final size of a real epidemic. $\blacksquare$

**25.** *(Strategy: sign of $S'$; then the one-dimensional structure of $I'$ as a function of $S$; then
integrability of $I$.)*

*$S$ is non-increasing.* $S' = -\beta SI/N\le0$, since all the factors are non-negative. Hence $S(t)$
decreases and, being bounded below by $0$, converges to some $S_\infty\ge0$ by the monotone convergence
theorem for bounded monotone sequences.

*At most one interior maximum of $I$.* $I' = I\left(\beta S/N-\gamma\right) = \gamma I\left(R_0S/N-1\right)$.
The sign of $I'$ is the sign of $R_0S/N-1$, and $S$ is non-increasing. Therefore $I'$ can change sign at
most once, and only from $+$ to $-$, at the instant when $S = N/R_0$. (If $S_0\le N/R_0$ there is no
growth phase at all; if $S_0>N/R_0$ there is exactly one maximum.) The function $I$ is therefore
unimodal.

*$I\to0$.* $R' = \gamma I$, so $R$ is increasing and bounded above by $N$, hence converges; therefore

$$\int_0^\infty I(t)\,dt = \frac{R_\infty-R(0)}{\gamma}<\infty .$$

After the peak, $I$ is non-increasing and bounded below, so $I(t)\to L\ge0$. If $L>0$ then $I(t)\ge L/2$
for all large $t$, and the integral of $I$ would diverge, contradicting the finiteness above. Hence
$L=0$. (Before the peak $I$ is increasing; the argument needs only the behaviour for large $t$, where $I$
is non-increasing by the unimodality just proved.) $\blacksquare$

*Remarks.* The proof uses only that the total population is finite and conserved, so the same argument
works for SEIR. It also shows that convergence is not exponential in the tail: near the end $I$ decays
roughly like $e^{-\gamma t}$ once $S\approx S_\infty$, but the epidemic can take arbitrarily long to reach
that regime.

**26.** *(Strategy: read $S_\infty>0$ off the final-size equation; differentiate implicitly for the
monotonicity.)*

*Positivity.* At the positive root, $s_\infty = e^{-R_0(1-s_\infty)}$, and the right-hand side is
strictly positive for every finite $R_0$ and every $s_\infty\in[0,1]$. Hence $s_\infty>0$ and
$S_\infty = Ns_\infty>0$; the epidemic always leaves some susceptibles. The reason is that the force of
infection vanishes as $I\to0$, so the last susceptibles are never reached at a positive rate.

*Monotonicity.* Let $F(s,R_0) = s - e^{-R_0(1-s)}$ and let $s_\infty(R_0)$ be the positive root for
$R_0>1$. Then

$$\frac{\partial F}{\partial R_0} = (1-s)e^{-R_0(1-s)}, \qquad \frac{\partial F}{\partial s} = 1 - R_0e^{-R_0(1-s)} = 1-R_0s_\infty .$$

At the positive root, $s_\infty<1/R_0$ (because $z>0$), so $1-R_0s_\infty>0$: the implicit function
theorem applies and

$$\frac{ds_\infty}{dR_0} = -\frac{\partial F/\partial R_0}{\partial F/\partial s} = -\frac{(1-s_\infty)e^{-R_0(1-s_\infty)}}{1-R_0s_\infty} < 0 .$$

Hence $S_\infty$ is strictly decreasing in $R_0$ on $(1,\infty)$, so $z = 1-s_\infty$ is strictly
increasing. For $R_0\le1$ the only root is $s_\infty=1$. $\blacksquare$

*Check:* at $R_0 = 1.5$, $s_\infty = 0.41719$; at $R_0 = 2$, $0.20319$; at $R_0 = 3$, $0.05952$ —
decreasing, as proved. ✓

**27.** *(Strategy: one-dimensional sign analysis of the logistic-type equation.)*

Without demography, $S = N-I$ and

$$I' = f(I) := I\left[\beta\left(1-\frac{I}{N}\right)-\gamma\right] = \gamma I\left[R_0\left(1-\frac{I}{N}\right)-1\right].$$

*Equilibria.* $f(I)=0$ gives $I=0$ or $1-I/N = 1/R_0$, i.e.

$$I^{*} = N\left(1-\frac{1}{R_0}\right),$$

which is in $(0,N)$ exactly when $R_0>1$.

*Case $R_0\le1$.* For $I\in[0,N]$, $1-I/N\le1$, so $R_0(1-I/N)-1\le R_0-1\le0$, and the inequality is
strict unless $R_0=1$ and $I=0$. Hence $f(I)\le0$ on $[0,N]$, with $f(I)<0$ for $I>0$. Therefore $I$ is
non-increasing and $I(t)\to0$ (it is bounded below); $I=0$ is globally asymptotically stable on $[0,N]$.

*Case $R_0>1$.* Then $f(I)>0$ for $0<I<I^{*}$ (because $R_0(1-I/N)>1$) and $f(I)<0$ for $I^{*}<I\le N$.
So $I$ increases when below $I^{*}$ and decreases when above it. Since $f$ is a downward parabola, $I^{*}$
is globally asymptotically stable on $(0,N]$: from below, $I$ increases and is bounded by $I^{*}$; from
above, $I$ decreases and is bounded below by $I^{*}$; in either case the limit exists and must be an
equilibrium, hence $I^{*}$.

*Bifurcation at $R_0=1$.* At $R_0=1$ the two equilibria coincide, $I^{*}=0$. For $R_0$ slightly above
$1$, $I^{*}\approx N(R_0-1)$ is small; for $R_0$ below $1$ there is no positive equilibrium. The
equilibria exchange stability at $R_0=1$: this is a **transcritical bifurcation**, the standard mechanism
by which an endemic state appears as a parameter crosses a threshold. $\blacksquare$

*Remark.* The SIR model has no analogous branch: its only relevant equilibrium is $I=0$, because $R$ is
absorbing. Endemicity in the SIS model is a consequence of the return path $I\to S$.

**28.** *(Strategy: sum the expected infections in each generation, with the generation-time density
$w$.)*

Let one case be introduced at time $0$ in a fully susceptible population. The expected number of
secondary infections generated in the time interval $[\tau,\tau+d\tau)$ is $R_0w(\tau)\,d\tau$, by the
definition of $w$ as the generation-time density; the total over all $\tau$ is $R_0$.

If the epidemic grows as $I(t) = I_0e^{rt}$, the infections generated at time $t$ by all previous cases
are

$$I(t) = \int_0^\infty R_0w(\tau)\,I(t-\tau)\,d\tau .$$

This is the **renewal equation**: the incidence now is the reproduction number times the weighted past
incidence, with the weights given by the generation time. Substituting the exponential ansatz,

$$I_0e^{rt} = \int_0^\infty R_0w(\tau)\,I_0e^{r(t-\tau)}\,d\tau = I_0e^{rt}R_0\int_0^\infty e^{-r\tau}w(\tau)\,d\tau .$$

Cancelling $I_0e^{rt}>0$ gives the **Euler–Lotka equation**

$$1 = R_0\int_0^\infty e^{-r\tau}w(\tau)\,d\tau .$$

*Check for the SIR model.* With $w(\tau) = \gamma e^{-\gamma\tau}$ (exponential infectious period),

$$\int_0^\infty e^{-r\tau}\gamma e^{-\gamma\tau}\,d\tau = \frac{\gamma}{r+\gamma},$$

so $1 = R_0\gamma/(r+\gamma)$, i.e. $r = \gamma(R_0-1)$, exactly the linearisation of §7.3. ✓

*Check for SEIR.* The generation time is the sum of an exponential latent period with rate $\sigma$ and an
exponential infectious period with rate $\gamma$, so its Laplace transform is the product
$\frac{\sigma}{r+\sigma}\cdot\frac{\gamma}{r+\gamma}$; the equation becomes
$(r+\sigma)(r+\gamma) = \sigma\beta$, which is the characteristic equation of §7.6. ✓

*Interpretation.* The equation is the continuous-time analogue of "each generation is $R_0$ times the
previous one", corrected for the fact that generations overlap. It is the reason $R_0$ cannot be read off
a growth rate without knowing $w$.

**29.** *(Strategy: compute $dR/dS$ in both models and compare.)*

In the SIR model,

$$\frac{dR}{dS} = \frac{\gamma I}{-\beta SI/N} = -\frac{\gamma N}{\beta S} = -\frac{N}{R_0S}.$$

In the SEIR model, $R' = \gamma I$ and $S' = -\beta SI/N$ are *the same equations* as in SIR, while $E$
does not appear in either. Hence

$$\frac{dR}{dS} = -\frac{N}{R_0S}$$

as well, and integrating from $(S_0,R(0))$ to $(S_\infty,R_\infty)$ gives

$$R_\infty - R(0) = -\frac{N}{R_0}\ln\frac{S_\infty}{S_0},$$

which, with $R(0)=0$ and $R_\infty = N - S_\infty$ (since $E,I\to0$), is exactly the final-size equation.

*The structural feature.* The identity uses only that (i) the only route out of the susceptible class is
infection, with rate $\beta SI/N$, and (ii) the only route into $R$ is recovery from $I$ at rate $\gamma I$.
The exposed compartment is a detour that affects neither relation; it changes the *route* from $S$ to $R$
but not the *rate at which $R$ grows per unit of $S$ lost*.

*Modifications that break the equality.* Disease-induced mortality (then the population is not conserved
and $R_\infty = N - S_\infty$ fails); a vaccinated class with different susceptibility (the $S$ equation
splits); waning immunity (recovered individuals re-enter $S$, so $R$ is not absorbing); heterogeneity in
susceptibility (the $S$ equation is no longer one scalar). In each case the final size changes, and the
SIR formula becomes an approximation. $\blacksquare$

**30.** *(Strategy: write the $2\times2$ Jacobian at the disease-free state and compute its
eigenvalues.)*

The system in $(S,I)$ is

$$S' = -\frac{\beta SI}{N}, \qquad I' = \frac{\beta SI}{N}-\gamma I .$$

The Jacobian is

$$J(S,I) = \begin{pmatrix} -\beta I/N & -\beta S/N \\ \beta I/N & \beta S/N-\gamma\end{pmatrix}.$$

At the disease-free state $(S,I) = (N,0)$:

$$J(N,0) = \begin{pmatrix} 0 & -\beta \\ 0 & \beta-\gamma\end{pmatrix}.$$

*Eigenvalues.* The matrix is upper triangular, so the eigenvalues are the diagonal entries: $\lambda_1 = 0$
and $\lambda_2 = \beta-\gamma = \gamma(R_0-1)$.

*Interpretation.* $\lambda_2$ governs the growth of a small infection: $I$ grows if $\lambda_2>0$ and
decays if $\lambda_2<0$. $\lambda_1 = 0$ is the neutral direction along which $S$ can be changed without
leaving the disease-free set $\{(S,0) : 0\le S\le N\}$, which is a line of equilibria rather than an
isolated point. The correct statement is therefore about the disease-free *set*: it is stable, and small
infections die out, if and only if $\lambda_2\le0$, i.e. $\beta\le\gamma$, i.e. $R_0\le1$. If $R_0>1$
then $\lambda_2>0$ and the disease-free set is unstable.

*Why this is the threshold theorem.* The eigenvalue $\lambda_2$ is $F-V$ in the notation of §7.3, and
$R_0 = F/V = \beta/\gamma$; the sign of $F-V$ is the sign of $R_0-1$. The next-generation theorem is the
multidimensional generalisation of this one-line computation: for $m$ infected compartments, the
eigenvalues of $F-V$ all have negative real part exactly when $\rho(FV^{-1})<1$. $\blacksquare$

## Challenge

**31.** *(Strategy: first-generation decomposition; then monotonicity and convexity of the generating
function.)*

Let $X$ be the number of secondary cases of one individual, with $\Pr(X\ge0)=1$, mean
$\mathbb{E}[X] = R_0$, and probability generating function $G(s) = \mathbb{E}[s^{X}] = \sum_{k\ge0}p_ks^{k}$,
defined for $s\in[0,1]$. Let $q$ be the probability that the chain starting from one individual eventually
dies out.

*The fixed-point equation.* Condition on $X = k$. The $k$ descendant chains are independent copies of the
original process, so the probability that all of them die out is $q^{k}$. Hence

$$q = \sum_{k\ge0}p_kq^{k} = G(q).$$

*$q$ is the smallest fixed point.* Define $q_n$ as the probability that the chain is extinct by
generation $n$. Then $q_0 = \Pr(X=0) = G(0)$, and conditioning on the first generation as above gives
$q_{n+1} = G(q_n)$. Since $G$ is increasing and $q_0 = G(0)\ge0$, we get
$q_1 = G(q_0)\ge G(0) = q_0$, and inductively $q_{n+1}\ge q_n$. So $(q_n)$ is non-decreasing and bounded
above by $1$; it converges to some $q^{*}$, which satisfies $q^{*} = G(q^{*})$ by continuity. Since
extinction by generation $n$ increases to eventual extinction, $q_n\to q$ and $q = q^{*}$. If $r$ is any
fixed point in $[0,1]$, then $q_0 = G(0)\le G(r) = r$ (because $0\le r$ and $G$ is increasing) and
inductively $q_n\le r$; hence $q\le r$. So $q$ is the smallest fixed point.

*When is $q<1$?* $G$ is convex on $[0,1]$ (all coefficients non-negative), $G(1)=1$ and $G'(1^-) = R_0$
(the mean, for the left derivative). Let $h(s) = G(s)-s$. Then $h(1)=0$ and $h'(1^-) = R_0-1$.

If $R_0\le1$: by convexity, $G(s)\ge G(1)+G'(1)(s-1) = 1-R_0(1-s)\ge s$ for all $s\in[0,1]$, with
equality only in degenerate cases. So $h(s)\ge0$ on $[0,1]$ and the only fixed point is $1$: $q=1$, the
chain dies out almost surely.

If $R_0>1$: then $h'(1^-)>0$, so for $s$ just below $1$, $h(s)<0$; and $h(0) = p_0\ge0$. By the
intermediate value theorem there is a root in $[0,1)$, so the smallest fixed point is $<1$ and $q<1$.
(The condition $\Pr(X\ge2)>0$ ensures $G$ is not affine, so the root is genuinely below $1$ rather than a
tangency.)

*Conclusion.* $q=1$ iff $R_0\le1$ (with degenerate exceptions), and $q<1$ iff $R_0>1$; the probability of
a major outbreak from a single case is $1-q$. $\blacksquare$

*Check.* For Poisson offspring, $G(s) = e^{-R_0(1-s)}$ and the equation is $q=e^{-R_0(1-q)}$; at $R_0=1$
it becomes $q=e^{-(1-q)}$, whose only root in $[0,1]$ is $q=1$ (the function $e^{-(1-q)}-q$ is negative for
$q<1$). ✓

**32.** *(Strategy: compute the generating function of the geometric law, solve the quadratic, and compare
variances.)*

*Geometric offspring.* Let $X$ have the geometric distribution on $\{0,1,2,\dots\}$ with parameter
$q_0 = 1/(1+R_0)$, so that $\Pr(X=k) = q_0(1-q_0)^{k}$ and $\mathbb{E}[X] = (1-q_0)/q_0 = R_0$. The
generating function is

$$G(s) = \sum_{k\ge0}q_0(1-q_0)^{k}s^{k} = \frac{q_0}{1-(1-q_0)s} = \frac{1}{1+R_0(1-s)} .$$

Solving $q = G(q)$:

$$q\big(1+R_0(1-q)\big) = 1 \quad\Longrightarrow\quad R_0q^2-(1+R_0)q+1 = 0,$$

$$q = \frac{(1+R_0)\pm\sqrt{(1+R_0)^2-4R_0}}{2R_0} = \frac{(1+R_0)\pm(R_0-1)}{2R_0},$$

so the roots are $q=1$ and $q = 1/R_0$. The smallest is $q = 1/R_0$ (for $R_0>1$).

*Comparison at $R_0 = 2$.* Geometric: $q = 0.5$. Poisson: $q = 0.20319$. The Poisson chain is much more
likely to establish itself.

*Why they differ.* The two distributions have the same mean but different variances:
$\operatorname{Var}(X) = R_0$ for the Poisson and $\operatorname{Var}(X) = R_0(1+R_0)$ for the geometric
on $\{0,1,\dots\}$ (variance $R_0(1+R_0)$ indeed, since the geometric with success probability $q_0$ has
variance $(1-q_0)/q_0^2 = R_0(1+R_0)$). The geometric law puts more mass on $X=0$ (probability
$1/(1+R_0) = 1/3$ at $R_0=2$, against $e^{-2} = 0.135$ for the Poisson) and correspondingly more mass on
large values. The extra mass at zero makes early extinction more likely; the extra mass in the tail does
not compensate, because a chain that dies at the first generation is gone for ever.

*Which assumption is doing the work.* The offspring distribution encodes heterogeneity in transmission.
A Poisson law is the homogeneous-mixing, equal-opportunity assumption; a geometric law is the
maximally-overdispersed alternative with the same mean, and it is the natural description of
superspreading when transmission is dominated by a few individuals. Thus *overdispersion raises the
probability of stochastic extinction for a given $R_0$*, and estimates of outbreak risk from $R_0$ alone
are only as good as the assumed offspring distribution.

*Check.* $q = 1/R_0$ is in $(0,1)$ for $R_0>1$ and satisfies the fixed-point equation:
$1/(1+R_0(1-1/R_0)) = 1/(1+R_0-1) = 1/R_0$. ✓

**33.** *(Strategy: separate what the model says from what the sentence claims; then assess what the
interval covers.)*

(a) The errors and elisions are:

1. **"Scientists' model predicts"** — the model does not predict; it computes a scenario conditional on
   stated assumptions. The word "predicts" converts a conditional statement into a forecast.
2. **"unless nothing changes"** — a garbled double negative. The report's condition is "in the absence of
   additional interventions", which is the opposite of "nothing changes" in the sense intended: it means
   *no new measures*, not *no change in behaviour*.
3. **The interval is dropped.** The report gives $200{,}000$–$900{,}000$; the sentence quotes only the
   central figure, which invites the reader to treat it as the answer.
4. **"assuming constant contact rates" is omitted.** This is the assumption that does most of the work:
   if contacts fall, the projection fails; if they rise, it is too low.
5. **"by December" without a setting.** The sentence does not say which population, which reporting
   regime, or which definition of "death" (confirmed COVID-19 deaths? excess deaths?).
6. **"500,000 deaths" as a number of deaths** hides that the model's output is a projection of a
   stochastic process with a distribution; a single number is a summary, not the thing.

(b) *A correct one-sentence rewrite:* "One model projects that, if contact rates stay at their current
level and no further interventions are introduced, cumulative deaths in [population] will reach about
500,000 by December (95% interval 200,000–900,000); the projection would change if behaviour or policy
changed."

(c) *Why the interval is not a prediction interval.* The interval reflects uncertainty *within the
model* — parameter uncertainty and, in a stochastic model, demographic noise. It does not include
structural uncertainty (the model may be the wrong model), uncertainty about the assumptions themselves
(whether contacts will stay constant), uncertainty about future policy, or uncertainty about data
quality. A calibrated forecast interval would need to be wider, usually much wider, and its coverage
would have to be checked against outcomes — which is precisely what the report's interval does not
claim. Presenting the model interval as if it bounded the actual outcome is the error.

**34.** *(Strategy: repeat the derivation of §7.4 with a reduced initial susceptible fraction.)*

Let a fraction $p$ of the population be vaccinated before the epidemic, with an all-or-nothing vaccine of
efficacy $\varepsilon$. Then a fraction $\varepsilon p$ is immune and $s_0 = 1-\varepsilon p$ is
susceptible. Vaccinated-but-unprotected individuals are susceptible and behave like everyone else, so the
model is the SIR model restricted to a population with initial susceptible fraction $s_0$.

*The final-size equation.* Dividing the equations as in §7.2 gives
$dI/dS = -1 + N/(R_0S)$ independent of $s_0$; integrating from $(s_0N, I_0)$ to $(s_\infty N, 0)$ and
letting $I_0\to0$,

$$s_\infty = s_0\,e^{-R_0(s_0-s_\infty)}, \qquad z = s_0-s_\infty .$$

Substituting $s_0 = 1-\varepsilon p$ gives the stated form
$s_\infty = (1-\varepsilon p)e^{-R_0(s_0-s_\infty)}$.

*When is $z=0$ the only solution?* The equation always has the solution $s_\infty = s_0$ (i.e. $z=0$: no
epidemic). A positive solution exists exactly when the epidemic can grow from the initial state, which by
§7.3 requires $R_0s_0>1$. Hence $z=0$ is the only solution precisely when

$$R_0(1-\varepsilon p)\le1 \quad\Longleftrightarrow\quad p\ge\frac{1-1/R_0}{\varepsilon},$$

which is exactly $p_c$ of §7.5. So the two derivations agree: the herd-immunity threshold is the coverage
at which the final size collapses to zero.

*Interpretation.* The condition is about the *effective* reproduction number at the start, not about the
final size. At $p = p_c$ the epidemic is neutered at birth; above it, the same holds; below it, an
epidemic occurs whose size is given by the transcendental equation and which is smaller than in an
unvaccinated population. $\blacksquare$

**35.** *(Strategy: eigenvalues of a $2\times2$ matrix; then read the eigenvector as a composition.)*

(a) The characteristic polynomial is
$\det(K-\lambda I) = (2-\lambda)(0.5-\lambda)-1 = \lambda^2-2.5\lambda+1-1 = \lambda(\lambda-2.5)$, so the
eigenvalues are $0$ and $2.5$, and

$$R_0 = \rho(K) = 2.5 .$$

(b) For $\lambda = 2.5$, solve $(K-2.5I)v = 0$:

$$\begin{pmatrix}-0.5 & 1 \\ 1 & -2\end{pmatrix}\begin{pmatrix}v_1\\v_2\end{pmatrix} = 0 \quad\Longrightarrow\quad v_2 = 0.5\,v_1,$$

so a dominant eigenvector is $(2,1)$, normalised $(2,1)/\sqrt5 \approx (0.894,0.447)$. In the growing
phase, the ratio of new infections in group $1$ to those in group $2$ tends to $2:1$: the epidemic
concentrates in group $1$.

(c) Group $1$ has the larger within-group transmission ($2$ against $0.5$) and the larger cross-term
($1$ in each direction), so it contributes more to every generation and its eigenvector weight is
correspondingly larger. An intervention that halves transmission within group $1$ reduces $R_0$
substantially more than the same proportional reduction in group $2$; the eigenvector says where the
epidemic actually is. This is the quantitative version of "target the core groups", and it is why
homogeneous models can mislead about the effect of targeted measures.

*Check:* the columns of $K$ are not proportional (the matrix has rank $2$), so there are two eigenvalues,
$2.5$ and $0$; the sum equals the trace $2.5$ and the product equals the determinant $0$. ✓

**36.** *(Strategy: read the conclusion off the final-size equation, then explain physically which
assumption produces it.)*

*The mathematics.* The final-size equation is $1-z = e^{-R_0z}$. Its right-hand side is strictly
positive for every finite $R_0$ and every $z\in[0,1]$, so $1-z>0$ and $z<1$: the fraction ever infected
never reaches $1$. Equivalently, $s_\infty = e^{-R_0(1-s_\infty)}>0$. The same conclusion follows from
the orbit relation: $I = 0$ is reached at a positive value of $S$, because $I$ decreases towards zero
while $S$ is still positive.

*Why it is structural, not a defect.* In the SIR model the force of infection on a susceptible is
$\beta I/N$. As the epidemic proceeds, $I$ falls towards zero, so the force of infection falls to zero
faster than the last susceptibles can be found. Each remaining infectious person infects fewer than one
new person once $S<N/R_0$, and the process dies out with susceptibles left over. The same phenomenon
appears in any model in which transmission is proportional to the density of infectious individuals:
a vanishingly small $I$ cannot reach the remaining susceptibles. This is a *correct* feature of the
model in its domain, not an error; the error would be to interpret $S_\infty>0$ as a prediction about a
real population without checking whether the mechanism (homogeneous mixing with density-dependent
transmission) applies.

*What would allow everyone to be infected?* Any mechanism that keeps the force of infection positive
after the susceptible pool is small: ongoing importation from outside (a term $+\iota$ in $I'$), a
reservoir or vector that maintains transmission, a model with a constant external hazard
($S' = -\lambda S$), or $R_0 = \infty$ (a measure-zero limiting case). In real populations, repeated
epidemics, waning immunity and antigenic drift achieve the same effect over time: the *first* wave leaves
susceptibles, and later waves infect more of them. The single-wave SIR model is a statement about one
epidemic in a closed population, and within that scope the leftover susceptibles are real. $\blacksquare$
