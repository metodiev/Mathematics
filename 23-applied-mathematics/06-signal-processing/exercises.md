# Signal Processing — Exercises

> [Signal Processing](README.md) · 36 problems · Beginner → Challenge · Solutions: [solutions.md](solutions.md)

Work through the problems in order. Everything is solvable from the tutorial; the section reference in
italics says where to look. Attempt each problem in writing before opening [solutions.md](solutions.md).

**Conventions.** Frequencies are in hertz and angular frequencies in radians per second; the Fourier
transform is $\hat x(\omega) = \int x(t)e^{-i\omega t}dt$ with inverse carrying $1/(2\pi)$; the
normalised sinc is written $\operatorname{sinc} x = \sin x/x$ with $\operatorname{sinc}0 = 1$; the DFT is
$X_k = \sum_{n=0}^{N-1}x_ne^{-2\pi ikn/N}$; the $z$-transform is $X(z) = \sum_nx_nz^{-n}$ and its ROC is
always to be stated. Where a problem asks for an estimate, three significant figures suffice.

## Beginner

**1.** *(§7.2)* Decide whether each signal is periodic, and if so give the fundamental period.

(a) $x(t) = \cos\frac{2\pi t}{3} + \sin\frac{\pi t}{2}$
(b) $x_n = \cos\frac{2\pi n}{5} + \cos\frac{2\pi n}{3}$
(c) $x_n = \cos n$
(d) $x(t) = e^{i\sqrt{2}\,t}$

**2.** *(§7.2)* For each signal compute the energy and the power, and classify it as energy, power, or
neither.

(a) $x(t) = e^{-3t}u(t)$
(b) $x(t) = 3\cos(2\pi \cdot 50\,t)$
(c) $x(t) = \operatorname{rect}(t/4)$
(d) $x_n = (0.5)^n u_n$
(e) $x_n = (-1)^n$

**3.** *(§7.3)* Compute all Fourier coefficients of $x(t) = \cos^2(\omega_0 t)$ and write the series in
complex form. Check the result with Parseval's identity.

**4.** *(§7.3)* Let $x(t) = t$ for $-\pi < t < \pi$ and extend periodically with period $2\pi$.

(a) Compute the coefficients $c_n$ from the definition.
(b) Write the real Fourier series.
(c) Evaluate the series at $t = \pi$ and explain what happens.

**5.** *(§7.5)* Compute $\hat x$ for $x(t) = e^{-a\lvert t\rvert}$ with $a > 0$, and check the value at
$\omega = 0$ against $\int x\,dt$.

**6.** *(§7.6)* Using the properties in §7.6 (not the definition), find the Fourier transforms of

(a) $x(t) = \operatorname{rect}\!\left(\dfrac{t - 3}{4}\right)$
(b) $x(t) = e^{-(t-2)^2/2}$
(c) $x(t) = e^{i5t}e^{-t^2/2}$
(d) $x(t) = \dfrac{d}{dt}\left[e^{-t^2/2}\right]$

**7.** *(§7.6)* Let $f(t) = \operatorname{rect}(t)$ and $g(t) = \operatorname{rect}\!\left(\dfrac{t-1}{2}\right)$.
Compute $(f * g)(t)$ explicitly, sketch it, and check its area against $\hat f(0)\hat g(0)$.

**8.** *(§7.7)* A signal occupies the band $0 \le f \le 3.4$ kHz.

(a) What is its Nyquist rate?
(b) Why do telephone systems sample at 8 kHz rather than at exactly 6.8 kHz?
(c) What would happen to a 4 kHz tone present in the input, sampled at 8 kHz without an anti-aliasing
filter?

**9.** *(§7.7)* A tone at $f_0 = 1.2$ kHz is sampled at $f_s = 1$ kHz. What frequency is reconstructed?
Verify your answer by comparing samples directly.

**10.** *(§7.8)* Compute the DFT of $x = (1,1,1,1)$ and of $y = (1,-1,1,-1)$ for $N = 4$, and say what
each spectrum means in words.

**11.** *(§7.9)*

(a) Compute the $z$-transform of $x = (1, 2, 3)$ (with $x_n = 0$ outside $n = 0,1,2$) and state its ROC.
(b) Evaluate $X(1)$ and explain the result.
(c) Find the zeros of $X$.

**12.** *(§7.10)* For the system $h_n = (1/2)^n u_n$, compute $H(e^{i\omega})$, evaluate $\lvert H\rvert$
at $\omega = 0, \pi/2, \pi$, and classify the filter.

## Intermediate

**13.** *(§7.3, §7.4)* Find the Fourier series of $x(t) = \lvert\sin t\rvert$, and deduce
$\displaystyle\sum_{n=1}^{\infty}\frac{1}{4n^2-1} = \frac12$.

**14.** *(§7.4, §8)* Using the square-wave series of §7.3 and Parseval's identity, evaluate
$\displaystyle\sum_{k=0}^{\infty}\frac{1}{(2k+1)^2}$. Deduce $\sum_{n\ge1} n^{-2} = \pi^2/6$.

**15.** *(§7.4)* Prove that if $x$ is $T$-periodic and $k$ times continuously differentiable with
$x^{(k)}$ piecewise $C^1$, then $c_n = O(n^{-k-1})$. Apply the result to a triangle wave and explain why
its coefficients decay faster than those of a square wave.

**16.** *(§7.5, §7.6)* Using the duality property and the pair
$\operatorname{rect}(t/\tau) \leftrightarrow \tau\operatorname{sinc}(\omega\tau/2)$, find the Fourier
transform of $x(t) = \operatorname{sinc}(t)$ (in the general $L^2$ sense) and state in which sense the
formula holds.

**17.** *(§7.6)*

(a) Show that $\widehat{t\,e^{-t^2/2}}(\omega) = -i\omega\sqrt{2\pi}e^{-\omega^2/2}$ in two ways: by
differentiation of the known Gaussian pair, and by the differentiation property applied to $x'$.
(b) Compute the Fourier transform of the triangle $\Lambda(t) = (1-\lvert t\rvert)^+$ both directly and
via $f*f$ with $f = \operatorname{rect}(t)$.

**18.** *(§7.7)* The signal $x(t) = \cos(2\pi\cdot1000t) + \tfrac12\cos(2\pi\cdot3500t)$ is sampled at
$f_s = 4$ kHz and reconstructed ideally. Which frequencies are present in the output? Which of them were
not in the input, and why?

**19.** *(§7.7)*

(a) Prove that sampling $\cos(\omega t)$ at rate $\omega_s$ gives the same sequence as sampling
$\cos((\omega + k\omega_s)t)$ for every integer $k$.
(b) Deduce that for $0 \le f_0 < f_s$ the alias is $f_0$ if $f_0 \le f_s/2$ and $f_s - f_0$ if
$f_0 > f_s/2$.

**20.** *(§7.8)* Let $x = (1,0,-1,0)$ and $h = (0,1,1,0)$.

(a) Compute both DFTs for $N = 4$.
(b) Compute the circular convolution $h \circledast x$ directly and verify it against the product of the
DFTs.
(c) Verify Parseval for $x$.

**21.** *(§7.8)* Two sinusoids at 1000 Hz and 1001 Hz are to be separated by a DFT.

(a) How long must the observation window be, in principle, and what frequency spacing does that
correspond to?
(b) At $f_s = 8$ kHz, how many samples are needed?
(c) Does zero-padding to $10^5$ points help? Explain.

**22.** *(§7.9)* For $x_n = (1/3)^nu_n - 2^nu_{-n-1}$ find $X(z)$, its ROC, and decide whether the
corresponding LTI system is stable. Sketch the ROC and the pole-zero pattern.

**23.** *(§7.10)* Consider $y_n = (1-\alpha)y_{n-1} + \alpha x_n$ with $0 < \alpha < 2$.

(a) Find $H(z)$, its pole, and the range of $\alpha$ for stability.
(b) Find the DC gain and the gain at $\omega = \pi$.
(c) Find the half-power cutoff $\omega_c$ as a function of $\alpha$, and discuss the limits
$\alpha \to 0$ and $\alpha \to 1$.

**24.** *(§7.11)* For a length-$N$ window $w_n$, define the coherent gain
$\mathrm{CG} = \frac1N\sum_n w_n$ and the equivalent noise bandwidth
$\mathrm{ENBW} = N\frac{\sum_n w_n^2}{\left(\sum_n w_n\right)^2}$.

(a) Compute both for the rectangular window.
(b) Compute both for the Hann window $w_n = \tfrac12 - \tfrac12\cos\frac{2\pi n}{N-1}$, using
$\sum_n\cos\frac{2\pi n}{N-1} = 1$ and $\sum_n\cos^2\frac{2\pi n}{N-1} = \frac{N}{2}$ for $N \ge 3$.
(c) Which window would you choose to detect a weak tone next to a strong one, and what does it cost?

## Advanced

**25.** *(§7.3, §7.4)* Prove Bessel's inequality for a $T$-periodic $x \in L^2$, deduce
$c_n \to 0$, and prove that for piecewise $C^1$ $x$ the inequality is an equality (Parseval).

**26.** *(§7.6)* Let $f, g \in L^1(\mathbb{R})$.

(a) Prove $\widehat{f*g} = \hat f\hat g$, stating the theorem that justifies the interchange.
(b) Deduce $\lVert f*g\rVert_1 \le \lVert f\rVert_1\lVert g\rVert_1$.
(c) Assuming Plancherel, prove $\lVert f*g\rVert_\infty \le \lVert f\rVert_2\lVert g\rVert_2$ for
$f,g \in L^2$, and show by example that the analogous bound with $\lVert\,\cdot\,\rVert_2$ on the left
is false.

**27.** *(§7.7)* Prove the aliasing formula: if $x \in L^2$ and $x_s$ is obtained by sampling at rate
$\omega_s$ and ideal reconstruction, then $\hat x_s(\omega) = \sum_k\hat x(\omega + k\omega_s)$ for
$\lvert\omega\rvert \le \omega_s/2$. Explain why the copies overlap exactly when $x$ is not bandlimited
to $\omega_s/2$.

**28.** *(§7.7)*

(a) Prove that if two $L^2$ signals are bandlimited to $\Omega$ and agree at all points $nT_s$ with
$T_s \le \pi/\Omega$, then they are equal almost everywhere.
(b) Show that the hypothesis is sharp: for $T_s > \pi/\Omega$ exhibit a nonzero signal bandlimited to
$\Omega$ that vanishes at every $nT_s$.

**29.** *(§7.8)* Prove, for the DFT of length $N$: (a) the orthogonality relation, (b) the inversion
formula, (c) Parseval's identity, and (d) the circular convolution theorem.

**30.** *(§7.12)*

(a) Prove the general inequality $\sigma_A^2\sigma_B^2 \ge \frac14\bigl\lvert\langle[A,B]\rangle\bigr\rvert^2$
for self-adjoint operators $A,B$ on an inner product space, where
$[A,B] = AB - BA$ and the variances are those of the state $\psi$ with $\lVert\psi\rVert = 1$.
(b) Apply it with $A = $ multiplication by $t$ and $B = -i\frac{d}{dt}$ to recover
$\sigma_t\sigma_\omega \ge \tfrac12$, and check the commutator.

**31.** *(§7.10)*

(a) Show that the ideal discrete-time low-pass filter of Definition 5.11 has
$h_n \notin \ell^1(\mathbb{Z})$, hence is not BIBO stable.
(b) Show that it is not causal.
(c) Explain why (a) and (b) together make an exact ideal filter unrealisable, and what Paley–Wiener adds.

**32.** *(§7.10)* Let $h$ be a real FIR filter of length $N$ and $H(\omega) = \sum_{n=0}^{N-1}h_ne^{-i\omega n}$.

(a) Show that $H$ has linear phase, i.e. $H(\omega) = A(\omega)e^{-i\omega(N-1)/2}$ with $A$ real, if and
only if $h_n = h_{N-1-n}$ for all $n$.
(b) Deduce that a real, zero-phase FIR filter must be non-causal, and describe the usual remedy.

## Challenge

**33.** *(§7.4)* Derive the Gibbs overshoot. For the square wave of §7.3, write $S_N$ as an integral
against the Dirichlet kernel, show that at the first overshoot $t_N \to 0$ with $N t_N \to \pi$, and
conclude that the maximal value tends to
$\frac{2}{\pi}\int_0^{\pi}\frac{\sin u}{u}du - 1 \approx 0.0895$ above the jump.

**34.** *(§7.10, §7.11)* A low-pass FIR filter is required with passband edge 1 kHz, stopband edge 1.2 kHz,
stopband attenuation 60 dB, at $f_s = 8$ kHz. Using Kaiser's estimates — transition width
$\Delta f \approx (A - 8)f_s/(2.285\cdot 2\pi N)$ with $A$ in dB, and $\beta \approx 0.1102(A-8)$ for
$A > 50$ — estimate the required order, the delay, and the cost of computing one output sample by direct
convolution. Compare with the FFT-based cost for a block of $10^4$ samples.

**35.** *(§7.7)* Using the Poisson summation formula
$\sum_{n\in\mathbb{Z}}\phi(n) = \sum_{k\in\mathbb{Z}}\hat\phi(2\pi k)$, prove that sampling a signal at
interval $T_s$ periodises its spectrum with period $\omega_s = 2\pi/T_s$, in the sense that the sampled
distribution has Fourier transform $\frac{1}{T_s}\sum_k\hat x(\omega - k\omega_s)$. Deduce the sampling
theorem and identify exactly where the hypothesis of bandlimitation is used.

**36.** *(§7.12)*

(a) Prove that a nonzero $x \in L^2$ and its transform cannot both have compact support.
(b) Prove that equality in $\sigma_t\sigma_\omega \ge 1/2$ forces $x(t) = Ce^{-at^2}$ with $a>0$, and
that every such Gaussian indeed attains equality.
