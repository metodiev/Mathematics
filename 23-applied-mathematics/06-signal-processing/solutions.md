# Signal Processing — Solutions

> [Signal Processing](README.md) · Solutions to the 36 problems in [exercises.md](exercises.md)

Each solution states the strategy, carries out every significant step, and ends with a check where a
check is possible. Conventions are those of the tutorial: $\hat x(\omega) = \int x(t)e^{-i\omega t}dt$,
inverse with $1/(2\pi)$, $\operatorname{sinc}x = \sin x/x$.

## Beginner

**1.** *(Strategy: reduce every term to its period and take the least common multiple; in discrete time
first test whether $\omega/(2\pi)$ is rational.)*

(a) Periods $3$ and $2\pi/(\pi/2) = 4$; the ratio $3/4$ is rational, so the sum is periodic with period
$\operatorname{lcm}$ in the sense of the smallest $T$ with $T/3, T/4 \in \mathbb{Z}$, namely $T = 12$.

(b) Periods $5$ and $3$: LCM $15$.

(c) $\omega = 1$ and $\omega/(2\pi) = 1/(2\pi) \notin \mathbb{Q}$: not periodic.

(d) $\omega = \sqrt2$, period $T = 2\pi/\sqrt2 = \pi\sqrt2$: periodic. Irrationality of the period is
irrelevant in continuous time; only in discrete time must the period be an integer.

**2.** *(Strategy: integrate or sum $\lvert x\rvert^2$; a periodic bounded signal has infinite energy.)*

(a) $E = \int_0^\infty e^{-6t}dt = \frac16$, $P = 0$: energy signal.

(b) $E = \infty$; $P = \frac{A^2}{2} = \frac92$: power signal (amplitude $A = 3$).

(c) $E = \int_{-2}^{2}1\,dt = 4$, $P = 0$: energy signal.

(d) $E = \sum_{n\ge0}(1/4)^n = \frac{1}{1-1/4} = \frac43$, $P = 0$: energy signal.

(e) $E = \infty$ and $P = \lim_{N\to\infty}\frac{1}{2N+1}\sum_{n=-N}^{N}1 = 1$: power signal.

**3.** *(Strategy: use a double-angle identity so that the signal is already a finite Fourier series.)*

$\cos^2\omega_0t = \frac12 + \frac12\cos2\omega_0t = \frac12 + \frac14e^{2i\omega_0t} + \frac14e^{-2i\omega_0t}$,
so $c_0 = \frac12$, $c_{\pm2} = \frac14$, all other $c_n = 0$. Parseval: the left side is
$\frac{1}{T}\int\cos^4\omega_0t\,dt = \frac38$ (using $\cos^4 = \frac38 + \frac12\cos2\theta + \frac18\cos4\theta$,
whose average is $\frac38$), and the right side is $\frac14 + 2\cdot\frac1{16} = \frac38$. ✓

**4.** *(Strategy: integrate by parts once; the boundary terms carry all the information.)*

(a) With $T = 2\pi$ and $\omega_0 = 1$, for $n \ne 0$,
$\int te^{-int}dt = \frac{te^{-int}}{-in} + \frac{e^{-int}}{n^2}$, so evaluating between $-\pi$ and $\pi$
and using $e^{\pm in\pi} = (-1)^n$, the $\frac{1}{n^2}$ terms cancel and

$$c_n = \frac{1}{2\pi}\cdot\frac{-2\pi(-1)^n}{in} = \frac{i(-1)^n}{n}, \qquad n \ne 0, \qquad c_0 = \frac{1}{2\pi}\int_{-\pi}^{\pi}t\,dt = 0.$$

(b) Since $c_{-n} = -c_n$, pairing gives $c_ne^{int} + c_{-n}e^{-int} = 2ic_n\sin nt = -\frac{2(-1)^n}{n}\sin nt$,
so

$$x(t) = 2\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{n}\sin nt .$$

(c) At $t = \pi$ every sine vanishes, so the series gives $0$; the function jumps from $\pi$ (as
$t \to \pi^-$) to $-\pi$ (as $t \to -\pi^+$), and $\frac12(\pi + (-\pi)) = 0$. This is exactly Dirichlet's
rule of Theorem 7.2, and it is a useful check that the coefficients are right.

**5.** *(Strategy: split at $0$ so that the absolute value becomes two ordinary exponentials.)*

$$\hat x(\omega) = \int_{-\infty}^{0}e^{at}e^{-i\omega t}dt + \int_0^{\infty}e^{-at}e^{-i\omega t}dt
= \frac{1}{a - i\omega} + \frac{1}{a + i\omega} = \frac{2a}{a^2+\omega^2}.$$

At $\omega = 0$ this is $2/a$, and directly $\int e^{-a\lvert t\rvert}dt = 2\int_0^\infty e^{-at}dt = 2/a$. ✓
The transform is real and positive: $x$ is real and even, so by conjugate symmetry $\hat x$ is real and even.

**6.** *(Strategy: identify each signal as a shifted, scaled or modulated version of a table entry.)*

(a) $\operatorname{rect}(t/4)$ has transform $4\operatorname{sinc}(2\omega)$; the shift by $3$ multiplies
by $e^{-3i\omega}$: $\hat x = 4\operatorname{sinc}(2\omega)e^{-3i\omega}$.

(b) $e^{-t^2/2}$ has transform $\sqrt{2\pi}e^{-\omega^2/2}$; shifting by $2$ multiplies by $e^{-2i\omega}$:
$\hat x = \sqrt{2\pi}e^{-\omega^2/2}e^{-2i\omega}$.

(c) $e^{i5t}$ is modulation to $+5$: $\hat x = \sqrt{2\pi}e^{-(\omega-5)^2/2}$.

(d) The derivative property gives $\hat x = i\omega\sqrt{2\pi}e^{-\omega^2/2}$. As a check, the derivative
is $-te^{-t^2/2}$ and the transform of $te^{-t^2/2}$ (Exercise 17) is $-i\omega\sqrt{2\pi}e^{-\omega^2/2}$;
negating gives the same answer. ✓

**7.** *(Strategy: the convolution of two rectangles is the overlap length of two intervals.)*

$f$ is $1$ on $[-\tfrac12,\tfrac12]$ and $g$ is $1$ on $[0,2]$, so $(f*g)(t)$ is the length of
$[-\tfrac12,\tfrac12]\cap[t-2,t]$. That length is $0$ for $t \le -\tfrac12$; $t + \tfrac12$ for
$-\tfrac12 \le t \le \tfrac12$; $1$ for $\tfrac12 \le t \le \tfrac32$; $\tfrac52 - t$ for
$\tfrac32 \le t \le \tfrac52$; and $0$ afterwards. This is a trapezoid of height $1$, plateau length $1$
and base $3$, hence area $1\cdot1 + 2\cdot\frac12 = 2$. Check: $\hat f(0)\hat g(0) = 1 \cdot 2 = 2$. ✓

**8.** *(Strategy: Nyquist rate $= 2f_{\max}$; the margin question is about the transition band of the
analogue filter.)*

(a) $2 \times 3400 = 6800$ Hz.

(b) A real anti-aliasing filter has a transition band of finite width; sampling at exactly $6.8$ kHz would
require infinite attenuation immediately above $3.4$ kHz. Sampling at $8$ kHz gives a guard band and
matches the international telephony standard; slightly oversampling is almost always cheaper than
designing a brick-wall analogue filter.

(c) With $f_s = 8$ kHz, a $4$ kHz tone lies exactly at $f_s/2$. Its samples are
$\cos(2\pi\cdot4000\,n/8000) = \cos(\pi n) = (-1)^n$: a maximal alternating sequence. It cannot be
distinguished from other signals that produce the same samples, and both its amplitude and its phase are
lost. This is the degenerate case of the sampling theorem at equality, and the reason practical designs
keep $f_{\max}$ strictly below $f_s/2$.

**9.** *(Strategy: subtract multiples of $f_s$ until the frequency lies in $\lvert f\rvert \le f_s/2$.)*

$1200 - 1000 = 200$ Hz. Check: $\cos(2\pi\cdot1200\,n/1000) = \cos(2\pi\cdot1.2n)$ and
$\cos(2\pi\cdot0.2n)$ differ by $\cos$ of an added multiple of $2\pi n$. ✓ The reconstructed tone is
$200$ Hz, which is *not* in the input.

**10.** *(Strategy: compute with $\omega_4 = -i$ and interpret which bin carries the energy.)*

For $x = (1,1,1,1)$: $X_0 = 4$ and $X_k = \sum_n(-i)^{kn} = 0$ for $k = 1,2,3$ because the four roots of
unity sum to zero. A constant sequence has all its energy in the DC bin.

For $y = (1,-1,1,-1)$: $Y_k = \sum_n(-1)^n(-i)^{kn}$. Then $Y_0 = 1-1+1-1 = 0$; $Y_1 = 1+i-1-i = 0$;
$Y_2 = 1+1+1+1 = 4$; $Y_3 = 1-i-1+i = 0$. A sequence alternating at every sample has all its energy in
bin $N/2$, the Nyquist bin. Together the two examples say: bin $k$ measures the component at frequency
$2\pi k/N$.

**11.** *(Strategy: a finite sequence has a polynomial $z$-transform; factor it.)*

(a) $X(z) = 1 + 2z^{-1} + 3z^{-2} = \dfrac{z^2+2z+3}{z^2}$, convergent for every $z \ne 0$ (a finite sum
of powers of $z^{-1}$ converges absolutely for all $z\neq0$).

(b) $X(1) = 1+2+3 = 6 = \sum_n x_n$: the $z$-transform at $z=1$ is the DC gain, i.e. the sum of the
sequence.

(c) $z^2 + 2z + 3 = 0$ gives $z = -1 \pm i\sqrt2$, both of modulus $\sqrt3 \approx 1.732$: the two zeros
sit outside the unit circle.

**12.** *(Strategy: sum the geometric series and evaluate the modulus.)*

$$H(e^{i\omega}) = \sum_{n\ge0}\left(\tfrac12\right)^ne^{-i\omega n} = \frac{1}{1-\tfrac12e^{-i\omega}},
\qquad \lvert H\rvert = \frac{1}{\sqrt{1.25-\cos\omega}}.$$

At $\omega = 0$: $\lvert H\rvert = 1/\sqrt{0.25} = 2$, which equals $\sum_n h_n$. At $\omega = \pi/2$:
$1/\sqrt{1.25} = 0.894$. At $\omega = \pi$: $1/\sqrt{2.25} = 0.667$. Gain decreases with frequency, so the
filter is low-pass.

## Intermediate

**13.** *(Strategy: the period is $\pi$, not $2\pi$, so the fundamental frequency is $2$; integrate
$\sin t$ over one period where it is positive.)*

With $T = \pi$ and $\omega_0 = 2$, and $x(t) = \sin t$ on $[0,\pi]$,

$$c_n = \frac{1}{\pi}\int_0^{\pi}\sin t\,e^{-2int}dt .$$

Writing $\sin t = (e^{it}-e^{-it})/(2i)$ and using $e^{\pm i(1\mp 2n)\pi} = -1$,

$$c_n = \frac{1}{\pi}\cdot\frac{1}{2i}\left[\frac{2i}{1-2n} + \frac{2i}{1+2n}\right]
= \frac{2}{\pi(1-4n^2)} = -\frac{2}{\pi(4n^2-1)}, \qquad n \ne 0,$$

and $c_0 = \frac1\pi\int_0^\pi\sin t\,dt = \frac{2}{\pi}$. Pairing conjugates (each $c_n$ is real) gives

$$\lvert\sin t\rvert = \frac{2}{\pi} - \frac{4}{\pi}\sum_{n=1}^{\infty}\frac{\cos 2nt}{4n^2-1}.$$

At $t = 0$ the left side is $0$, so $\frac{2}{\pi} = \frac{4}{\pi}\sum_{n\ge1}\frac{1}{4n^2-1}$, i.e.
$\sum_{n\ge1}\frac{1}{4n^2-1} = \frac12$. ✓ (This is a telescoping series in disguise:
$\frac{1}{4n^2-1} = \frac12\left(\frac{1}{2n-1} - \frac{1}{2n+1}\right)$.)

**14.** *(Strategy: apply Parseval to the square wave, then peel off the even terms.)*

For $x = \pm1$ square wave, $\frac1T\int x^2 = 1$ and $\sum_n\lvert c_n\rvert^2 = 1$. Odd $n$ contribute
$\lvert c_n\rvert^2 = \frac{4}{\pi^2n^2}$ for both signs of $n$, so
$1 = \frac{8}{\pi^2}\sum_{k\ge0}\frac{1}{(2k+1)^2}$, hence $\sum_{k\ge0}(2k+1)^{-2} = \pi^2/8$.
Splitting $\sum_{n\ge1}n^{-2}$ into odd and even parts: $S = \frac{\pi^2}{8} + \frac14S$, so
$\frac34S = \frac{\pi^2}{8}$ and $S = \pi^2/6$. ✓

**15.** *(Strategy: integrate by parts $k+1$ times; each integration divides by $n\omega_0$ and every
boundary term dies because $x$ and its derivatives are continuous and periodic.)*

On each $C^1$ piece, $\int x^{(j)}e^{-in\omega_0t}dt = \frac{1}{in\omega_0}\int x^{(j+1)}e^{-in\omega_0t}dt$
plus boundary terms. The boundary terms at the ends of a piece combine across pieces; since $x^{(j)}$ is
continuous and $T$-periodic for $j \le k$, all of them cancel. After $k+1$ integrations,

$$c_n = \frac{1}{(in\omega_0)^{k+1}}\cdot\frac{1}{T}\int_{-T/2}^{T/2}x^{(k+1)}(t)e^{-in\omega_0t}dt = \frac{d_n}{(in\omega_0)^{k+1}},$$

with $d_n$ the coefficients of the piecewise-$L^2$ function $x^{(k+1)}$. Bessel's inequality for
$x^{(k+1)}$ gives $d_n \to 0$, hence $c_n = o(n^{-k-1})$, in particular $O(n^{-k-1})$.

A triangle wave has a continuous first derivative but a discontinuous second derivative, so a jump appears
first at the level of $x''$: $c_n = O(n^{-2})$, one power faster than the square wave's $O(n^{-1})$. The
lesson is that the *lowest* order at which a derivative jumps fixes the decay rate.

**16.** *(Strategy: use duality to exchange the roles of the two variables.)*

Duality states $\mathcal{F}(\hat f)(t) = 2\pi f(-t)$. Take $f(t) = \operatorname{rect}(t/\tau)$, so
$\hat f(\omega) = \tau\operatorname{sinc}(\omega\tau/2)$. Then

$$\mathcal{F}\bigl\{\tau\operatorname{sinc}(\tau t/2)\bigr\}(\omega) = 2\pi\operatorname{rect}(-\omega/\tau) = 2\pi\operatorname{rect}(\omega/\tau).$$

Setting $\tau = 2$ gives $\mathcal{F}{\operatorname{sinc} t}(\omega) = \pi\operatorname{rect}(\omega/2)$,
that is, $\pi$ for $\lvert\omega\rvert<1$ and $0$ for $\lvert\omega\rvert>1$. Since
$\operatorname{sinc}\notin L^1$, the equality is an $L^2$ identity (and holds pointwise almost
everywhere), not an absolutely convergent integral; the value at $\omega = \pm1$ is irrelevant.

**17.** *(Strategy: differentiate a known pair, then confirm with the differentiation theorem.)*

(a) Start from $\mathcal{F}{e^{-t^2/2}} = \sqrt{2\pi}e^{-\omega^2/2}$ and differentiate in $\omega$:
the left side becomes $\mathcal{F}{-it\,e^{-t^2/2}}$, the right side $-\omega\sqrt{2\pi}e^{-\omega^2/2}$.
Dividing by $-i$ gives $\mathcal{F}{te^{-t^2/2}} = -i\omega\sqrt{2\pi}e^{-\omega^2/2}$.

Second route: $x' = -te^{-t^2/2}$, so $\mathcal{F}{x'} = i\omega\hat x = i\omega\sqrt{2\pi}e^{-\omega^2/2}$,
and $\mathcal{F}{te^{-t^2/2}} = -\mathcal{F}{x'}$, the same result.

(b) $\Lambda = f*f$ with $f = \operatorname{rect}(t)$, hence $\hat\Lambda = \operatorname{sinc}^2(\omega/2)$
by the convolution theorem. Directly,

$$\hat\Lambda(\omega) = 2\int_0^{1}(1-t)\cos\omega t\,dt
= 2\left[\frac{(1-t)\sin\omega t}{\omega}\Big|_0^1 + \frac{1}{\omega}\int_0^1\sin\omega t\,dt\right]
= \frac{2(1-\cos\omega)}{\omega^2} = \frac{4\sin^2(\omega/2)}{\omega^2},$$

which is $\operatorname{sinc}^2(\omega/2)$. ✓ (Using $\lvert t\rvert$ symmetry before integrating is what
makes the boundary term at $t=1$ vanish.)

**18.** *(Strategy: fold each input frequency into $\lvert f\rvert \le f_s/2 = 2$ kHz.)*

$1000$ Hz is inside the band and survives. For $3500$ Hz: $(3500+2000)\bmod4000 = 1500$ and
$\lvert1500-2000\rvert = 500$ Hz. Check: $\cos(2\pi\cdot3500\,n/4000) = \cos(2\pi\cdot0.875n)$ and
$\cos(2\pi\cdot0.125n)$ differ by a multiple of $2\pi n$, so the samples agree. ✓

The output contains $1000$ Hz and $500$ Hz; the $500$ Hz component is an artefact of sampling, not a
component of the input. It is the standard example of a *false low frequency* created by aliasing: the
undersampled high tone appears as a low hum.

**19.** *(Strategy: everything follows from $\omega T_s = 2\pi f/f_s$ and the periodicity of $\cos$.)*

(a) At $t = nT_s$, using $\omega_sT_s = 2\pi$,

$$\cos\bigl((\omega + k\omega_s)nT_s\bigr) = \cos\bigl(\omega nT_s + 2\pi kn\bigr) = \cos(\omega nT_s).$$

(b) For $0 \le f_0 < f_s$ choose $k\in\{0,-1\}$ so that $f_0 + kf_s \in (-f_s/2, f_s/2]$. If
$f_0 \le f_s/2$ take $k = 0$ and the alias is $f_0$. If $f_0 > f_s/2$ take $k = -1$ and the alias is
$f_0 - f_s$, whose modulus is $f_s - f_0$. Since $\cos$ is even, only the modulus matters. ✓

**20.** *(Strategy: direct sums for the DFTs, index arithmetic modulo $4$ for the convolution.)*

(a) $X_k = 1 + 0 - (-i)^{2k} + 0 = 1 - (-1)^k$, so $X = (0,2,0,2)$. For $h$:
$H_k = (-i)^k + (-i)^{2k} = (-i)^k + (-1)^k$, so $H = (2,\,-1-i,\,0,\,-1+i)$.

(b) $y_n = x_{(n-1)\bmod4} + x_{(n-2)\bmod4}$, giving
$y_0 = x_3 + x_2 = -1$, $y_1 = x_0 + x_3 = 1$, $y_2 = x_1 + x_0 = 1$, $y_3 = x_2 + x_1 = -1$, i.e.
$y = (-1,1,1,-1)$.

Multiplication of spectra: $Y_0 = 0$, $Y_1 = (-1-i)(2) = -2-2i$, $Y_2 = 0$, $Y_3 = -2+2i$. Direct DFT of
$y$: $Y_0 = -1+1+1-1 = 0$ ✓ and $Y_1 = -1 - i - 1 - i = -2-2i$ ✓.

(c) $\sum_n\lvert x_n\rvert^2 = 1+0+1+0 = 2$ and $\frac14\sum_k\lvert X_k\rvert^2 = \frac14(0+4+0+4) = 2$. ✓

**21.** *(Strategy: the Rayleigh resolution limit is one bin, and the bin width is $1/T_{\text{obs}}$.)*

(a) Two tones separated by $\Delta f = 1$ Hz need $T_{\text{obs}} \ge 1/\Delta f = 1$ s, corresponding to a
bin spacing of $1$ Hz.

(b) $N = f_sT_{\text{obs}} = 8000$ samples.

(c) No. Zero-padding refines the *grid* on which the (already determined) spectrum is evaluated; it
interpolates. The two tones remain indistinguishable because the information separating them was never
recorded. Resolution is set by $T_{\text{obs}}$, not by the number of points.

**22.** *(Strategy: use the geometric sums for a right-sided and a left-sided exponential, then intersect
the two ROCs.)*

The right-sided part gives $\frac{1}{1-\frac13z^{-1}}$ for $\lvert z\rvert > \frac13$; the left-sided part
(see §7.9) gives $\frac{1}{1-2z^{-1}}$ for $\lvert z\rvert < 2$. Both converge on the annulus
$\frac13 < \lvert z\rvert < 2$, so

$$X(z) = \frac{1}{1-\frac13z^{-1}} + \frac{1}{1-2z^{-1}} = \frac{2 - \frac73z^{-1}}{1 - \frac73z^{-1} + \frac23z^{-2}},
\qquad \operatorname{ROC}: \tfrac13 < \lvert z\rvert < 2.$$

Poles at $z = \frac13$ and $z = 2$; the zero solves $2 - \frac73z^{-1} = 0$, i.e. $z = \frac76$. The ROC
contains the unit circle, so this (two-sided!) system is BIBO stable — even though one pole lies outside
the unit circle, because the causal-stability criterion applies only to causal systems.

**23.** *(Strategy: one-pole low-pass; everything follows from the pole location.)*

(a) $H(z) = \dfrac{\alpha}{1-(1-\alpha)z^{-1}}$, a single pole at $z = 1-\alpha$. Stability requires
$\lvert1-\alpha\rvert < 1$, i.e. $0 < \alpha < 2$. For $\alpha \ge 2$ the pole leaves the unit disc and
the recursion diverges.

(b) DC gain $H(1) = \frac{\alpha}{1-(1-\alpha)} = 1$: constants pass unchanged. At Nyquist,
$H(-1) = \frac{\alpha}{1+(1-\alpha)} = \frac{\alpha}{2-\alpha}$, which is $\ll1$ for small $\alpha$.

(c) $\lvert H(e^{i\omega})\rvert^2 = \dfrac{\alpha^2}{1+(1-\alpha)^2-2(1-\alpha)\cos\omega}$. Setting this
to $\frac12$ and solving,

$$\cos\omega_c = \frac{2-2\alpha-\alpha^2}{2(1-\alpha)}.$$

For $\alpha = 0.1$ this gives $0.99444$, i.e. $\omega_c \approx 0.105$ rad, matching Example 6. As
$\alpha\to0^+$ the right side tends to $1$, so $\omega_c\to0$: heavy smoothing, narrow band. As
$\alpha\to1^-$ the right side tends to $-\infty$, so the equation has no solution and $\omega_c = \pi$:
no filtering at all.

**24.** *(Strategy: evaluate the two sums with the given identities, then compare the trade-off.)*

(a) Rectangular: $\sum w_n = N$, $\sum w_n^2 = N$, so $\mathrm{CG} = 1$ and
$\mathrm{ENBW} = N\cdot N/N^2 = 1$.

(b) Hann: $\sum_n w_n = \frac N2 - \frac12\sum_n\cos\frac{2\pi n}{N-1} = \frac N2 - \frac12 = \frac{N-1}{2}$,
so $\mathrm{CG} = \frac{N-1}{2N}\to\frac12$. Also
$\sum_n w_n^2 = \sum_n\left(\frac14 - \frac12\cos\frac{2\pi n}{N-1} + \frac14\cos^2\frac{2\pi n}{N-1}\right)
= \frac N4 - \frac12 + \frac N8 = \frac{3N}{8} - \frac12$, hence

$$\mathrm{ENBW} = N\,\frac{3N/8 - 1/2}{(N-1)^2/4} = \frac{4N(3N/8-1/2)}{(N-1)^2} \xrightarrow[N\to\infty]{} \frac32 .$$

(c) To detect a weak tone beside a strong one, choose Hann (or Hamming): its first sidelobe is $-31$ dB
against the rectangular $-13$ dB, so the strong tone leaks far less onto its neighbours. The cost is
resolution (main lobe twice as wide) and effective noise bandwidth ($1.5$ instead of $1$ bin), plus the
need to divide measured amplitudes by $\mathrm{CG} = 0.5$.

## Advanced

**25.** *(Strategy: expand the squared norm of $x - p_N$ and drop a non-negative term.)*

For $p_N = \sum_{\lvert n\rvert\le N}a_ne_n$ with $\langle e_n,e_m\rangle = \delta_{nm}$,

$$\lVert x - p_N\rVert^2 = \lVert x\rVert^2 - \sum_{\lvert n\rvert\le N}\left(\bar a_n\langle x,e_n\rangle + a_n\overline{\langle x,e_n\rangle}\right) + \sum_{\lvert n\rvert\le N}\lvert a_n\rvert^2
= \lVert x\rVert^2 - \sum_{\lvert n\rvert\le N}\lvert c_n\rvert^2 + \sum_{\lvert n\rvert\le N}\lvert a_n - c_n\rvert^2 .$$

Choosing $a_n = c_n$ leaves $\lVert x\rVert^2 - \sum\lvert c_n\rvert^2 \ge 0$, which is Bessel. The partial
sums $\sum_{\lvert n\rvert\le N}\lvert c_n\rvert^2$ increase and are bounded, so they converge; hence
$c_n \to 0$.

For Parseval, if $x$ is piecewise $C^1$ then Theorem 7.1 gives absolute and uniform convergence of
$\sum c_ne_n$ to $x$. Multiplying by $\bar x$ and integrating term by term is then legitimate, and

$$\frac1T\int\lvert x\rvert^2 = \sum_n c_n\overline{\frac1T\int x e^{-in\omega_0t}dt} \cdot \frac{T}{T}
= \sum_n c_n\bar c_n,$$

because every cross term $\frac1T\int e^{i(n-m)\omega_0t}dt$ vanishes for $n \ne m$. The general $L^2$
case follows by density (Riesz–Fischer), which is the completeness statement cited in §7.4.

**26.** *(Strategy: Fubini for (a), then substitute and apply the triangle inequality.)*

(a) Since $\int\int\lvert f(\tau)g(t-\tau)\rvert d\tau dt = \lVert f\rVert_1\lVert g\rVert_1 < \infty$,
Tonelli gives integrability of the double integral and Fubini allows the interchange:

$$\widehat{f*g}(\omega) = \int f(\tau)\left(\int g(t-\tau)e^{-i\omega t}dt\right)d\tau
= \hat g(\omega)\int f(\tau)e^{-i\omega\tau}d\tau = \hat f(\omega)\hat g(\omega).$$

(b) $\lVert f*g\rVert_1 \le \int\int\lvert f(\tau)\rvert\lvert g(t-\tau)\rvert d\tau dt = \lVert f\rVert_1\lVert g\rVert_1$,
which also shows $f*g \in L^1$.

(c) For each $t$, Cauchy–Schwarz gives
$\lvert(f*g)(t)\rvert \le \lVert f\rVert_2\lVert g(t-\cdot)\rVert_2 = \lVert f\rVert_2\lVert g\rVert_2$, hence
$\lVert f*g\rVert_\infty \le \lVert f\rVert_2\lVert g\rVert_2$.

The analogous bound in $\lVert\cdot\rVert_2$ is false. Take $f = g = \mathbf{1}_{[0,L]}$: then
$\lVert f\rVert_2\lVert g\rVert_2 = L$, while $f*g$ is the triangle of height $L$ and base $2L$, so
$\lVert f*g\rVert_2^2 = 2\int_0^L (L-t)^2dt = \frac{2L^3}{3}$ and
$\lVert f*g\rVert_2 = L^{3/2}\sqrt{2/3} > L$ for $L > 3/2$. The correct general statement is Young's
inequality $\lVert f*g\rVert_r \le \lVert f\rVert_p\lVert g\rVert_q$ with $1/r = 1/p + 1/q - 1$; here
$p = q = 2$ forces $r = \infty$.

**27.** *(Strategy: write sampling as multiplication by a comb and use the convolution theorem.)*

The sampled signal is $x_s = x\cdot c$ with $c(t) = \sum_n\delta(t-nT_s)$. The comb is $T_s$-periodic, so
its Fourier series is $c = \frac{1}{T_s}\sum_k e^{ik\omega_st}$ (all coefficients equal $1/T_s$ by the
sifting property), and term-by-term transformation gives
$\hat c(\omega) = \frac{2\pi}{T_s}\sum_k\delta(\omega - k\omega_s) = \omega_s\sum_k\delta(\omega-k\omega_s)$.
By the multiplication–convolution identity of §7.6,

$$\hat x_s(\omega) = \frac{1}{2\pi}(\hat x * \hat c)(\omega) = \frac{1}{T_s}\sum_k\hat x(\omega - k\omega_s).$$

Restricting to $\lvert\omega\rvert\le\omega_s/2$ displays one copy per period. The copies are disjoint
exactly when the support of $\hat x$ has length at most $\omega_s$, i.e. when $x$ is bandlimited to
$\omega_s/2$; otherwise adjacent copies add, and the sum in the band is not $\hat x$ but a superposition —
the aliasing error.

**28.** *(Strategy: use the sampling theorem on the difference; then look for the slowest oscillation that
still vanishes at the sample points.)*

(a) Let $d$ be the difference. It is bandlimited to $\Omega$ and $d(nT_s) = 0$ for all $n$. By Theorem 7.4
(with $T_s \le \pi/\Omega$), $d$ equals its sinc interpolation of the samples, which is identically zero;
hence $d = 0$ almost everywhere.

(b) Let $T_s > \pi/\Omega$ and take $d(t) = \sin(\pi t/T_s)$. Its transform is supported in
$\lvert\omega\rvert \le \pi/T_s < \Omega$, so $d$ is bandlimited to $\Omega$; and $d(nT_s) = \sin(\pi n) = 0$
for every integer $n$, yet $d \not\equiv 0$. So the samples no longer determine the signal. The critical
rate $T_s = \pi/\Omega$ is exactly where the two statements meet.

**29.** *(Strategy: every part is the same geometric sum in disguise.)*

(a) For integers $k$: if $N\mid k$ then $\omega_N^{kn} = 1$ and the sum is $N$; otherwise
$\sum_{n=0}^{N-1}\omega_N^{kn} = \frac{1-\omega_N^{kN}}{1-\omega_N^k} = 0$ because $\omega_N^{kN} = 1$ and
$\omega_N^k\ne1$. Hence $\frac1N\sum_n e^{2\pi i(j-k)n/N} = \delta_{jk}$.

(b) Multiply $X_k$ by $e^{2\pi ijn/N}$, sum over $k$, and use (a):
$\frac1N\sum_kX_ke^{2\pi ijn/N} = \frac1N\sum_nx_n\sum_k e^{2\pi i(j-n)k/N} = x_j$.

(c) Substitute the inverse formula for $\overline{x_n} = \frac1N\sum_m\overline{X_m}e^{-2\pi imn/N}$ and use
(a):

$$\sum_n\lvert x_n\rvert^2 = \sum_n x_n\overline{x_n}
= \frac1N\sum_m\overline{X_m}\sum_n x_ne^{-2\pi imn/N}
= \frac1N\sum_m\overline{X_m}X_m = \frac1N\sum_k\lvert X_k\rvert^2,$$

because the inner sum is exactly $X_m$.

(d) With $y_n = \sum_m h_mx_{(n-m)\bmod N}$, substitute $j = (n-m)\bmod N$ and use the periodicity of
$e^{-2\pi ikn/N}$ to obtain $Y_k = H_kX_k$.

**30.** *(Strategy: Cauchy–Schwarz on the centred operators, then take imaginary parts.)*

(a) Let $\tilde A = A - \langle A\rangle I$ and $\tilde B = B - \langle B\rangle I$ (the means are real
because $A,B$ are self-adjoint). Then
$\sigma_A^2\sigma_B^2 = \langle\tilde A^2\rangle\langle\tilde B^2\rangle =
\lVert\tilde A\psi\rVert^2\lVert\tilde B\psi\rVert^2 \ge \lvert\langle\tilde A\psi,\tilde B\psi\rangle\rvert^2
= \lvert\langle\tilde A\tilde B\rangle\rvert^2 \ge \bigl(\operatorname{Im}\langle\tilde A\tilde B\rangle\bigr)^2$.
Now $\tilde A\tilde B - \tilde B\tilde A = [A,B]$, so
$\operatorname{Im}\langle\tilde A\tilde B\rangle = \frac{1}{2i}\langle[A,B]\rangle$, giving
$\sigma_A^2\sigma_B^2 \ge \frac14\lvert\langle[A,B]\rangle\rvert^2$.

(b) With $A = t$ and $B = -i\frac{d}{dt}$ acting on $\psi$,

$$[A,B]\psi = t\left(-i\psi'\right) - (-i)\frac{d}{dt}(t\psi) = -it\psi' + i\psi + it\psi' = i\psi,$$

so $[A,B] = iI$ and $\lvert\langle iI\rangle\rvert = 1$. Also $\sigma_B^2 = \int\lvert\psi'\rvert^2dt =
\frac{1}{2\pi}\int\omega^2\lvert\hat\psi\rvert^2d\omega = \sigma_\omega^2$ by Plancherel, provided the mean
frequency is zero (otherwise apply the same argument to $e^{i\omega_0t}\psi$). Hence
$\sigma_t^2\sigma_\omega^2 \ge \frac14$. Equality requires $\tilde B\psi = \lambda\tilde A\psi$ with
$\lambda$ purely imaginary, i.e. $\psi' = \lambda t\psi$: again the Gaussian.

**31.** *(Strategy: test the definition of BIBO stability on the impulse response itself.)*

(a) $h_n = \sin(\omega_cn)/(\pi n)$ for $n\ne0$. Then
$\sum_{n\ne0}\lvert h_n\rvert = \frac{1}{\pi}\sum_{n\ne0}\frac{\lvert\sin(\omega_cn)\rvert}{n}$, and since
$\lvert\sin(\omega_cn)\rvert$ has a positive average over each period of the sequence, the sum diverges
like $\frac{2}{\pi^2}\log N$: $h\notin\ell^1$.

BIBO stability fails explicitly: take the bounded input $x_n = \operatorname{sgn}(h_{-n})$. Then
$y_0 = \sum_k h_kx_{-k} = \sum_k\lvert h_k\rvert = \infty$.

(b) $h_n \ne 0$ for infinitely many $n < 0$ (all $n$ with $\omega_cn$ not a multiple of $\pi$), while an
ideal filter must respond before it is fed anything: the output at time $0$ depends on future inputs. So
the filter is non-causal.

(c) A realisable filter must be causal and stable; (a) and (b) exclude the ideal response on both counts.
They do not by themselves exclude *some* unrealisable-but-harmless responses; Paley–Wiener adds the sharp
statement: a causal, finite-energy filter has $\int\lvert\ln\lvert H\rvert\rvert < \infty$, so $H$ cannot
vanish on an interval. An exact stopband is therefore impossible for any causal filter, not merely
inconvenient for the sinc design.

**32.** *(Strategy: factor out the linear phase and test when the remainder is real.)*

(a) Write

$$H(\omega)e^{i\omega(N-1)/2} = \sum_{n=0}^{N-1}h_ne^{-i\omega\left(n-\frac{N-1}{2}\right)}
= \sum_{n}h_n\cos\omega\left(n-\tfrac{N-1}{2}\right) - i\sum_n h_n\sin\omega\left(n-\tfrac{N-1}{2}\right).$$

This is real for every $\omega$ iff $\sum_n h_n\sin(\omega(n-\frac{N-1}{2})) = 0$ for every $\omega$. The
functions $\sin(\omega m)$ for distinct integers $m$ are linearly independent (differentiate repeatedly at
$\omega=0$, or use orthogonality on $[-\pi,\pi]$), so the coefficient of each $m$ must vanish: for
$m = n - \frac{N-1}{2}$ and its mirror $-m = (N-1-n) - \frac{N-1}{2}$, the two coefficients $h_n$ and
$h_{N-1-n}$ must be equal. Hence $h_n = h_{N-1-n}$.

(b) If in addition $A$ is to be real and *even* — the definition of zero phase — then
$h_ne^{-i\omega n}$ must combine with $h_{-n}e^{i\omega n}$, which requires a symmetric, two-sided impulse
response with $h_{-n} = h_n$ and $n$ ranging over negative indices: the filter must be non-causal. The
standard remedies are (i) accept the linear phase $-\omega(N-1)/2$, i.e. a delay of $(N-1)/2$ samples,
which is what every real-time linear-phase FIR does; or (ii) filter offline, running the signal forwards
and then backwards through the same filter, which squares the magnitude response but cancels the phase.

## Challenge

**33.** *(Strategy: differentiate the partial sum, locate the first maximum, and let $N\to\infty$ inside
the integral.)*

For the $\pm1$ square wave with $T = 2\pi$, $S_N(t) = \frac{4}{\pi}\sum_{k=0}^{N-1}\frac{\sin((2k+1)t)}{2k+1}$,
so differentiating term by term gives

$$S_N'(t) = \frac{4}{\pi}\sum_{k=0}^{N-1}\cos((2k+1)t) = \frac{4}{\pi}\cdot\frac{\sin(2Nt)}{2\sin t}
= \frac{2\sin(2Nt)}{\pi\sin t},$$

using $\sum_{k=0}^{N-1}\cos((2k+1)t) = \frac{\sin(2Nt)}{2\sin t}$ (sum a geometric series of exponentials).
Hence $S_N'$ vanishes at $t_N = \pi/(2N)$ (and at multiples), and this is the first maximum because $S_N'$
changes sign from $+$ to $-$ there. Therefore

$$S_N(t_N) = \frac{2}{\pi}\int_0^{\pi/(2N)}\frac{\sin(2Ns)}{\sin s}\,ds
= \frac{2}{\pi}\int_0^{\pi}\frac{\sin u}{2N\sin\left(\frac{u}{2N}\right)}\,du
\;\xrightarrow[N\to\infty]{}\; \frac{2}{\pi}\int_0^{\pi}\frac{\sin u}{u}\,du,$$

where the substitution $u = 2Ns$ was used and the limit is justified by dominated convergence together
with $\sin(x)/x \to 1$. Numerically $\int_0^\pi \frac{\sin u}{u}du = 1.85194$, so the limiting peak is
$1.17898$: an overshoot of $0.17898$ above the value $1$, that is $8.95\%$ of the jump of size $2$. The
overshoot does not shrink with $N$; the region in which it occurs shrinks.

**34.** *(Strategy: solve Kaiser's relation for $N$, then compare direct and FFT costs.)*

With $A = 60$ dB and $\Delta f = 1200 - 1000 = 200$ Hz,

$$N \approx \frac{(A-8)f_s}{2.285\cdot 2\pi\,\Delta f}
= \frac{52\cdot 8000}{2.285\cdot 6.2832\cdot 200} \approx 145 .$$

So $N = 145$ taps (round up to an odd number so the delay is an integer), delay $(N-1)/2 = 72$ samples,
i.e. $72/8000 = 9$ ms — audible in a live monitoring chain but irrelevant for recorded signals.
$\beta \approx 0.1102(60-8) = 5.73$.

Direct convolution costs $N$ multiply–adds per output sample, about $1.2\times10^8$ per second at 8 kHz.

For a block of $10^4$ samples with FFT size $512$ (the smallest power of two above $N + \text{block}$ in
overlap-save), one block of 512 outputs costs about three FFTs of length 512, each $\approx 512\log_2 512 =
4608$ butterfly operations, so $\approx 1.4\times10^4$ operations for 512 outputs — about
$27$ operations per output instead of $145$. The saving grows with $N$: direct cost is $O(N)$ per sample,
FFT cost $O(\log N)$ per sample.

**35.** *(Strategy: Poisson summation is the statement that the Fourier transform of a comb is a comb;
apply it to $x$ times a comb and identify the result with the inverse transform of a periodised spectrum.)*

Let $T_s > 0$, $\omega_s = 2\pi/T_s$, and define the sampled distribution $x_s = x\sum_n\delta(\cdot - nT_s)$.
For a test function $\phi$, $\langle x_s,\phi\rangle = \sum_n x(nT_s)\phi(nT_s)$ (assuming $x$ continuous, so
that sampling is well defined). Poisson summation applied to $\phi(t)x(t)$ on the lattice $T_s\mathbb{Z}$
— that is, $\sum_n\psi(nT_s) = \frac{1}{T_s}\sum_k\hat\psi\!\left(\frac{2\pi k}{T_s}\right)$ — gives

$$\hat x_s(\omega) = \sum_n x(nT_s)e^{-i\omega nT_s} = \frac{1}{T_s}\sum_k\hat x(\omega - k\omega_s).$$

Comparing with the definition of the Fourier transform of the measure $x_s$ proves the periodisation
identity. Equivalently, the comb has $\hat c = \omega_s\sum_k\delta(\omega - k\omega_s)$ and the convolution
theorem gives the same sum.

Now suppose $\hat x$ is supported in $\lvert\omega\rvert\le\Omega$ with $\Omega \le \omega_s/2$. Then the
supports $[\omega_s k - \Omega, \omega_s k + \Omega]$ are disjoint, and multiplying $\hat x_s$ by
$T_s\operatorname{rect}(\omega/\omega_s)$ isolates the $k=0$ term, i.e. $\hat x$. Inverting gives the sinc
interpolation formula. The bandlimitation hypothesis is used at exactly one point: to assert that the
copies $\hat x(\omega - k\omega_s)$ do not overlap, so that the sum on $\lvert\omega\rvert\le\omega_s/2$
equals the single term $\hat x(\omega)/T_s$. Without it, the extracted spectrum is a superposition and
reconstruction returns an aliased signal.

**36.** *(Strategy: (a) compact support makes the transform entire, then use the identity theorem; (b)
read off the equality case in Cauchy–Schwarz.)*

(a) Suppose $x$ vanishes outside $[-M,M]$. Then
$\hat x(\omega) = \int_{-M}^{M}x(t)e^{-i\omega t}dt$; differentiating under the integral sign any number of
times (legitimate because the integrand is continuous on a compact set) shows that $\hat x$ extends to an
entire function of the complex variable $\omega$. If in addition $\hat x$ vanishes outside a compact set,
then it vanishes on the nonempty open set complementary to that support, so by the identity theorem for
holomorphic functions $\hat x \equiv 0$. Inverting, $x = 0$ almost everywhere. Hence a nonzero signal and
its transform cannot both be compactly supported — a signal cannot be simultaneously time-limited and
band-limited.

(b) Equality in $\sigma_t\sigma_\omega \ge \frac12$ requires equality in both steps of the proof of
Theorem 7.7. Equality in Cauchy–Schwarz forces $x' = c\,t\,x$ with $c$ real, whose solutions are
$x(t) = Ce^{ct^2/2}$; square-integrability forces $c < 0$, so $x(t) = Ce^{-at^2}$ with $a = -c/2 > 0$.
Conversely, for $x = e^{-t^2/(2\sigma^2)}$ one computes $\sigma_t = \sigma/\sqrt2$ and
$\sigma_\omega = 1/(\sigma\sqrt2)$ (Example 7), whose product is $\frac12$; multiplying by $C$, shifting in
time and modulating in frequency do not change the product, so every Gaussian is an equality case.
