# Exponential and Logarithmic Models — Exercises

> [Tutorial](README.md) · 36 problems · Levels: Beginner, Intermediate, Advanced, Challenge

Work each problem completely, and check every numerical answer by a second method — a substitution, a
ratio, or an estimate by the rule of 72. Where a problem asks what a model *shows*, answer in terms of
the evidence actually available, not what the model would predict if it continued forever. Do not open
[solutions.md](solutions.md) until you have attempted the problems.

Throughout, $\log$ means $\log_{10}$ and $\ln$ means $\log_e$. Give numerical answers to three
significant figures unless the problem says otherwise.

## Beginner

**1.** A town has $12{,}000$ inhabitants and grows at $4\%$ per year. Taking $t=0$ in 2020, write
$P(t) = P_0b^{t}$ for the population, state the continuous rate $k = \ln b$, and predict the population
in 2030.

**2.** A quantity is multiplied by $1.035$ every year. State (a) the annual percentage growth rate,
(b) the continuous rate $k$, and (c) the growth factor per decade.

**3.** A quantity grows at $12\%$ per year. Find its doubling time exactly, and compare with the rule
of 72.

**4.** A radioactive substance has a half-life of $12$ years. What fraction remains after $30$ years?
How many half-lives is that?

**5.** $\$2{,}500$ is invested at a continuous rate of $3.6\%$ per year. Find the balance after $8$
years, and the effective annual rate.

**6.** A bank quotes $4\%$ nominal per year compounded quarterly. Find the effective annual rate, and
the factor by which the balance grows in $10$ years.

**7.** Rewrite $y = 5\cdot 3^{x}$ in the form $y = 5e^{kx}$, giving $k$ to four decimal places.

**8.** A solution has hydrogen-ion concentration $\left[\mathrm{H}^{+}\right] = 4.5\times10^{-6}$ mol/L.
Find its pH. Is it acidic or basic?

**9.** An amplifier's output power is $500$ times its input power. Express this gain in decibels.

**10.** One earthquake has magnitude $5.2$ and another $4.1$. Find the ratios of (a) their ground
amplitudes and (b) their released energies.

**11.** Two stars differ by $3$ magnitudes. Find the ratio of their fluxes, and say which star is
brighter and by how much.

**12.** A colony follows $N = 7\cdot 2^{x}$. For what $x$ is $N = 224$?

**13.** Two data tables are given. Decide which is exponential and which is a power law, and give both
models.

| Table A: $x$ | $0$ | $1$ | $2$ | $3$ |
|---|---|---|---|---|
| $y$ | $5$ | $15$ | $45$ | $135$ |

| Table B: $x$ | $1$ | $2$ | $4$ | $8$ |
|---|---|---|---|---|
| $y$ | $5$ | $15$ | $45$ | $135$ |

## Intermediate

**14.** A model $y = ab^{x}$ passes through $(0,3)$ and $(4,48)$. Find $a$ and $b$, predict $y$ at
$x=2$, and state precisely what the prediction at $x = 10$ is worth.

**15.** A bone sample contains $45\%$ of its original carbon-14. Using a half-life of $5730$ years,
estimate its age.

**16.** A bacterial culture grows from $500$ to $4000$ in $4.5$ hours. Find the hourly growth factor,
the continuous rate, and the doubling time.

**17.** A drug has a half-life of $6$ hours. A patient receives $400$ mg. (a) How much remains after
$9$ hours? (b) When does the amount fall below $25$ mg?

**18.** A power law $y = ax^{p}$ passes through $(2,12)$ and $(5,187.5)$. Find $a$ and $p$, and check
the model at $x = 3$.

**19.** A straight line on a semi-log plot (vertical axis $\log y$, horizontal axis $x$) rises $0.9$
units of $\log y$ over $3$ units of $x$. Find the growth factor $b$ per unit $x$, and the horizontal
distance required for $y$ to double.

**20.** Intel's 4004 processor (1971) had $2{,}300$ transistors; the 80486 (1989) had $1{,}180{,}000$.
Fit an exponential to these two points and find the doubling time. Then predict the transistor count
for 2000 and for 2010, and compare with the actual figures of about $42$ million and $1.17$ billion.

**21.** Investment A pays a continuous rate of $6.0\%$. Investment B pays $6.2\%$ compounded annually.
Which is better over $20$ years on $\$5{,}000$? Give the difference in dollars. What does this show
about "more frequent compounding is always better"?

**22.** A population follows a logistic model with $K = 2000$, $P_0 = 100$ and $r = 0.6$ per year.
Find $A$, $P(3)$, the time at which growth is fastest, and the maximum growth rate.

**23.** A data set is found to satisfy $\dfrac{1}{P} = 0.002 + 0.018e^{-0.4t}$. Identify $K$, $A$, $r$
and $P_0$, and compute $P(5)$.

**24.** An algorithm runs in $2^{n}$ microseconds. How long does it take at $n = 40$ and at $n = 50$?
Give the second answer in years.

**25.** Earthquake X has magnitude $7.0$ and earthquake Y has magnitude $5.0$. (a) By what factor do
their amplitudes differ, and their energies? (b) Earthquake Z releases $10^{4.5}$ times the energy of
earthquake Y; what is its magnitude?

## Advanced

**26.** (a) Derive $T_2 = \dfrac{\ln 2}{\ln b}$ from the definition of doubling time, and explain why
$Q_0$ does not appear. (b) For annual rates of $2\%$, $7\%$ and $20\%$, compare the exact doubling time
with the rule of 72, and compute the percentage error of the rule in each case.

**27.** (a) Derive $\displaystyle\lim_{n\to\infty}\left(1+\frac rn\right)^{nt} = e^{rt}$, stating which
standard limit you use. (b) For $r = 6\%$, tabulate the effective annual rate for $n = 1,\,2,\,4,\,12,\,365$
and for $n\to\infty$. What is the *largest possible* gain from compounding more often at a fixed
nominal rate?

**28.** (a) Prove that if $y = ab^{x}$ with $b>1$, then for any fixed step $h>0$ the ratio
$y(x+h)/y(x)$ is the same for every $x$. (b) Prove that on a semi-log plot with vertical axis
$\log y$, the slope of the line is $\log b$, and deduce that the horizontal distance needed to double
$y$ is $\dfrac{\log 2}{\log b}$.

**29.** (a) Show that changing the logarithm base from $10$ to $e$ leaves the slope of a log-log plot
equal to $p$ (provided both axes are converted) but multiplies the intercept by $\ln 10$. (b) Explain
what goes wrong if the vertical axis is $\ln y$ while the horizontal axis is $\log x$, and compute the
slope that a power law $y = 3x^{2}$ would show in that mixed plot.

**30.** For the logistic model $P(t) = \dfrac{K}{1+Ae^{-rt}}$ with $K>0$, $r>0$, $A>0$: (a) prove
$P(0) = \dfrac{K}{1+A}$; (b) prove $0<P(t)<K$ for all $t$; (c) prove that the rate
$rP\left(1-\dfrac PK\right)$ is maximised at $P = K/2$ with maximum value $rK/4$; (d) prove that the
time to reach $K/2$ is $\dfrac{\ln A}{r}$; (e) prove the symmetry $P(t_0+s)+P(t_0-s) = K$.

**31.** Using $2{,}300$ transistors in 1971 and $42$ million in 2000, and $42$ million in 2000 and
$1.17$ billion in 2010: (a) compute the doubling time for each period; (b) comment on whether the
near-agreement of the two numbers supports the claim that "transistor count doubles every two years
without exception". Mention at least one fact about processor performance that the transistor count
does not capture.

## Challenge

**32.** A yeast population in a $200$-mL flask is measured with the flask's capacity independently
estimated at $K = 200$ million cells.

| $t$ (hours) | $0$ | $2$ | $4$ | $6$ | $8$ |
|---|---|---|---|---|---|
| $P$ (millions) | $10.00$ | $25.03$ | $56.00$ | $102.78$ | $148.37$ |

(a) Fit $P = P_0b^{t}$ to the first two points and predict $t = 4, 6, 8$. (b) Fit the logistic model
with the given $K$ to the same two points and predict $t = 4,6,8$. (c) Which model do the data support,
and by what evidence? (d) Suppose the capacity had not been estimated independently. What could you
still conclude from these five points?

**33.** The period of a pendulum is $T = 2\pi\sqrt{L/g}$, which is a power law $T = aL^{1/2}$ with
$g = 9.81\ \mathrm{m\,s^{-2}}$.

| $L$ (m) | $0.25$ | $0.50$ | $1.00$ | $2.00$ |
|---|---|---|---|---|
| $T$ (s) | $1.003$ | $1.419$ | $2.006$ | $2.837$ |

(a) Estimate the exponent from the two extreme points using base-$e$ logarithms. (b) Repeat using
base-$10$ logarithms and confirm the exponent is unchanged. (c) Estimate the uncertainty in $p$ if each
period is uncertain by $1\%$. (d) Explain why an exponential model is impossible here on dimensional
grounds alone.

**34.** A culture's early measurements are $P(0) = 10$, $P(2) = 26.72$, $P(4) = 69.45$ (millions).
(a) Fit a logistic model with $K = 1000$ using the points at $t=0$ and $t=4$, and find $r$. Check the
fit at $t=2$. (b) Repeat with $K = 2000$. (c) Predict $P(10)$ from both fits and comment. (d) State
what this demonstrates about estimating a carrying capacity from data far below it.

**35.** (a) Prove that on a logarithmic scale, equal ratios are equally spaced: if $x_2/x_1 = x_3/x_2$
and all are positive, then $\log_b x_2 - \log_b x_1 = \log_b x_3 - \log_b x_2$ for any base $b>0$,
$b\ne1$. (b) Prove that a level difference is a ratio: if $L_i = c\log_{10}(Q_i/Q_0)$, then
$Q_1/Q_2 = 10^{(L_1-L_2)/c}$. (c) Using (a), explain why a slide rule adds lengths to multiply
numbers, and state the length of the interval from $1$ to $10$ on a slide rule whose total length
represents one decade.

**36.** A logistic process has carrying capacity $K$, intrinsic rate $r$ and initial value $P_0$, and
$A = (K-P_0)/P_0$. Define $u(t) = Ae^{-rt}$.

(a) Prove that $\dfrac{P_0e^{rt}}{P(t)} = \dfrac{A+e^{rt}}{1+A}$.
(b) Deduce that $1 \le \dfrac{P_0e^{rt}}{P(t)} \le 1 + \dfrac1{u(t)}$, so that while $u \ge 20$ the
logistic and exponential curves agree to within $5\%$.
(c) Hence explain why data satisfying $P \le K/21$ cannot distinguish a logistic model from its
exponential approximation, and what a modeller must do about it.

(d) Design a sampling plan for a process you believe is logistic: state *when* you would sample, what
you would plot, how you would validate the fit, and two ways the plan could still fail.
