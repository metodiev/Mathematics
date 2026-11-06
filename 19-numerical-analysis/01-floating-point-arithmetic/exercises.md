# Floating-Point Arithmetic — Exercises

> [Tutorial](README.md) · 36 problems · Levels: Beginner, Intermediate, Advanced, Challenge

Every problem asks for a number that can be checked or a statement that must be proved. Numbers are
required to the precision stated; "about" means three significant digits. You may use any result from
the [tutorial](README.md); theorem numbers refer to it. Full solutions are in [solutions.md](solutions.md).

## Beginner

**1.** Write $0.375$ in binary. Is it representable exactly in binary64? In binary32?

**2.** Write $1/3$ in binary to eight fractional bits, state the repeating period, and explain why
$1/3$ is in no binary format.

**3.** Normalise $45.5$ as $\pm m\cdot2^{e-p+1}$ with $p=8$. Is $45.5\in F(2,8,-3,5)$?

**4.** Decode the binary32 pattern `0x41200000` into a real number, showing the sign, exponent and
fraction fields.

**5.** Encode $-0.5$ in binary32 and give the result as eight hexadecimal digits.

**6.** For $F(2,4,-3,3)$ compute $\varepsilon_{\mathrm{mach}}$, $u$, the largest finite number, and the
number of positive normalised elements.

**7.** Compute $\operatorname{ulp}(x)$ for $x=1$, $x=1024$, $x=2^{20}$ and $x=10^{16}$ in binary64.

**8.** Round $2/3$ to four significant binary digits. Give the result, the absolute error and the
relative error.

**9.** In IEEE double precision, is `0.1 + 0.2 == 0.3` true? Answer with the stored values of the three
constants and the difference.

**10.** How many doubles lie in $[2,4)$? In $[1,4)$? In $[1,1024)$?

**11.** Give the largest finite double as $(2-2^{-52})2^{1023}$ and its decimal value, and the smallest
positive normal double as a power of two.

**12.** Convert $(1.101)_2\times2^{3}$ and $(0.00101)_2\times2^{-2}$ to decimal.

**13.** The approximation $\hat\pi=3.14$ is used for $\pi$. Compute the absolute error, the relative
error, and the number of correct significant digits by Definition 5.5.

## Intermediate

**14.** Prove that $\lvert\operatorname{fl}(x)-x\rvert\le u\lvert x\rvert$ for round-to-nearest, and show
that the constant cannot be improved: compute the exact relative error of $\operatorname{fl}(1+2^{-24})$
in binary32.

**15.** Derive the gap formula of Theorem 8.3(a). Use it to count the doubles in $[1,2)$ and in
$[1,2^{10})$.

**16.** Add ten copies of $\operatorname{fl}_{32}(0.1)$ in binary32 by hand (round at each step). Give
the final value, the absolute error and the relative error, and compare with the bound $\gamma_9$.

**17.** Solve $0.001x^2+1000x+1=0$ twice: once with $(-b\pm\sqrt{b^2-4ac})/(2a)$ and once with the
stable formula. Give both roots from both methods and the relative error of the small root in each case.

**18.** Evaluate $\sqrt{x+1}-\sqrt{x}$ at $x=10^{8}$ with the naive formula and with the rationalised
one. Give both values and the relative error of the naive value.

**19.** Evaluate $1-\cos x$ at $x=10^{-6}$ naively and as $2\sin^2(x/2)$. Compare the observed relative
error with the estimate $4u/x^{2}$ of Theorem 8.10.

**20.** Trace Kahan summation on the data $[1,\,10^{-16},\,10^{-16},\,10^{-16}]$, recording $s$ and $c$
after each step. Compare the final $s$ with the correctly rounded sum.

**21.** Apply the TwoSum algorithm to $a=10^{16}$, $b=1$: compute $s=a\oplus b$, $z=s\ominus a$ and
$e=(a\ominus(s\ominus z))\oplus(b\ominus z)$. Verify that $s+e=a+b$ exactly.

**22.** Compute the relative condition number of $f(x)=1/(x-1)$ at $x=1.001$ and of $f(x)=\cos x$ at
$x=1.5707963$. Which computation is hopeless in double precision?

**23.** For the four numbers $10^{8}+1,10^{8}+2,10^{8}+3,10^{8}+4$ compute the variance with
$\overline{x^{2}}-\bar x^{2}$ and with the two-pass formula, in double precision. Explain the
discrepancy.

**24.** Explain, using the gap at $10^{16}$, why $(10^{16}+1)-10^{16}=0$ but $(10^{16}+2)-10^{16}=2$.
What does this say about testing equality of computed reals?

## Advanced

**25.** Prove Theorem 8.5: if $nu<1$ then the left-to-right computed sum $s_n$ satisfies
$\lvert s_n-\sum x_i\rvert\le\gamma_{n-1}\sum\lvert x_i\rvert$ with $\gamma_k=ku/(1-ku)$.

**26.** Prove Kahan's compensation lemma (Theorem 8.7): for $s,y\in F$ with $\lvert s\rvert\ge\lvert y\rvert$,
$t=\operatorname{fl}(s+y)$ and $e=\operatorname{fl}((t-s)-y)$, we have $s+y=t+e$ exactly.

**27.** Let $ax^{2}+bx+c=0$ with $a\ne0$, $b\ne0$, $D=b^{2}-4ac>0$. Prove that the roots computed as
$q/a$ and $c/q$, with $q=-\tfrac12(b+\operatorname{sign}(b)\sqrt D)$, both have relative error $O(u)$
when $\sqrt D$ is computed to relative accuracy $u$ and $q$ almost cancels. State your assumptions.

**28.** Prove Theorem 8.6: pairwise summation satisfies
$\lvert s-\sum x_i\rvert\le\gamma_{\lceil\log_2 n\rceil}\sum\lvert x_i\rvert$.

**29.** Prove that $\lvert F(\beta,p,L,U)\rvert=2(\beta-1)\beta^{p-1}(U-L+1)+1$, and deduce that $1/3$
belongs to no binary format.

**30.** Derive the relative condition number of evaluating a polynomial $p$ at $x\ne0$ with $p(x)\ne0$.
Compute it for $p(x)=x^{2}+10^{8}x+1$ at $x=1$, and interpret the answer.

**31.** Show that the bound $u$ in Theorem 8.1 is sharp in the following sense: for each precision
$p\ge2$ there are reals $x$ with $\lvert\operatorname{fl}(x)-x\rvert/\lvert x\rvert=u/(1+u)$, so no
constant smaller than $u/(1+u)$ works for all $x$.

**32.** Prove that $\operatorname{fl}$ is monotone: $x\le y$ implies $\operatorname{fl}(x)\le\operatorname{fl}(y)$.
Deduce that $x\mapsto x\oplus y$ and $y\mapsto x\oplus y$ are monotone, and give an example showing that
$\oplus$ is nevertheless not associative.

## Challenge

**33.** Find data for which Kahan compensated summation returns a badly wrong sum while Neumaier's
variant returns the correctly rounded one. Verify your example numerically and explain why Kahan's lemma
does not apply.

**34.** Prove Sterbenz's lemma: if $x,y\in F$ and $y/2\le x\le2y$ then $x-y\in F$. Deduce that the
subtraction $x\ominus y$ is exact whenever $x$ and $y$ lie in the same binade, and explain why this does
not contradict the catastrophic cancellation of Section 7.5.

**35.** Show that the bound of Theorem 8.5 is attained up to a factor: for $x_1=1$ and
$x_2=\cdots=x_n=2^{-53}$ with $n=1000$, compute the naive sum and the exact sum, and compare the error
with $\gamma_{n-1}\sum\lvert x_i\rvert$.

**36.** Prove that no finite binary format contains every rational number, and compare three strategies
for exact arithmetic — integers, rationals, and arbitrary-precision floats — on the computation
$\frac13+\frac16$ and on $\sum_{k=1}^{10^{6}}10^{-6}$.
