# Floating-Point Arithmetic — Solutions

> [Tutorial](README.md) · [Exercises](exercises.md) · Complete solutions to all 36 problems

Theorem and definition numbers refer to the [tutorial](README.md). Every numerical value quoted below
was computed in IEEE double precision (or in the format named), and every exact comparison uses
higher-precision arithmetic where a decimal expansion is given.

## Beginner

### Solution 1

**Answer.** $0.375=(0.011)_2=(1.1)_2\times2^{-2}$; representable exactly in both formats.

*Method.* Repeated doubling of the fractional part: $0.375\times2=0.75$ (bit $0$), $0.75\times2=1.5$
(bit $1$), $0.5\times2=1.0$ (bit $1$). The fraction terminates after three bits, so the expansion is
finite and the number is in every binary format whose exponent range contains $-2$ and whose precision
is at least $2$.

*Check via the definition.* $0.375=1.5\times2^{-2}$; with $p=2$, $m=3$ satisfies $2^{1}\le3\le2^{2}-1=3$,
so $0.375=m\cdot2^{e-p+1}=3\cdot2^{-2-2+1}=3\cdot2^{-3}=0.375$. Since $p=2\le24\le53$, the representation
is exact in both binary32 and binary64 — and in the toy system $F(2,3,-1,2)$, since $e=-2$ there is below
$L=-1$: in *that* format it underflows. The distinction matters: representability is relative to the
format's exponent range, not only to the number of digits.

### Solution 2

**Answer.** $1/3=(0.010101\ldots)_2$, period $2$ (the block $01$); not in any binary format.

*Method.* Doubling: $1/3\to2/3$ (bit $0$), $2/3\to4/3$ (bit $1$, remainder $1/3$). The remainder repeats
after two steps, so the bits repeat with period $2$: $1/3=0.0101\,0101\ldots_2=1.0101\ldots_2\times2^{-2}$.

*Why no binary format contains it.* Suppose $1/3=m\,2^{e-p+1}$ with integers $m,e,p$. Then
$$
1=3m\,2^{e-p+1}\quad\Longrightarrow\quad 2^{p-1-e}=3m .
$$
The left side is a power of $2$, the right side is divisible by $3$; a power of $2$ is never divisible by
$3$. Contradiction. The same argument (with $3$ replaced by any odd factor of the denominator) shows that
a rational is binary-representable exactly when its denominator, in lowest terms, is a power of $2$.

*Pitfall.* The decimal expansion $0.333\ldots$ is equally infinite, but "repeating" in base $10$ does not
imply "repeating" in base $2$; only denominators of the form $2^{a}5^{b}$ give terminating decimals, and
only $2^{a}$ gives terminating binaries.

### Solution 3

**Answer.** $45.5=(101101.1)_2=(1.011011)_2\times2^{5}$, so $e=5$ and $m=(1011011)_2=91$ with $p=8$; hence
$45.5\in F(2,8,-3,5)$, and it is *not* in $F(2,4,-3,3)$.

*Method.* $45=32+8+4+1=(101101)_2$ and $0.5=(0.1)_2$, so $45.5=(101101.1)_2$. Normalising shifts the
point five places: $1.011011_2\times2^{5}$. The significand has $7$ digits, and with $p=8$ one trailing
zero is appended: $m=(10110110)_2=182$, which satisfies $2^{7}=128\le182\le255$.

*Check.* $m\,2^{e-p+1}=182\cdot2^{5-8+1}=182\cdot2^{-2}=45.5$ ✓. The exponent $e=5$ is within $[-3,5]$ ✓.

*Why the toy system fails.* In $F(2,4,-3,3)$ the largest element is $(2-2^{-3})2^{3}=15$, so $45.5$ is out
of range; even with a wider range, $p=4$ would force rounding to $(1.011)_2\times2^{5}=44$.

### Solution 4

**Answer.** `0x41200000`${}=10$.

*Method.* Expand to bits: `0x41`$=0100\,0001$ and `0x200000`$=0010\,0000\,0000\,0000\,0000\,0000$, so the
pattern is `0 10000010 01000000000000000000000`.
- Sign $s=0$: positive.
- Exponent field $E=(10000010)_2=130$, so $e=130-127=3$.
- Fraction field $F=(010\cdots0)_2=2^{21}=2097152$, so $F/2^{23}=2^{-2}=0.25$.
- Value: $(1+0.25)\cdot2^{3}=1.25\cdot8=10$.

*Check.* $10=1.25\times2^{3}$ is exactly representable, so decoding returns $10$ with no error. The
hexadecimal grouping is what makes the exercise quick: the leading hex digit holds the sign and four
exponent bits, the second hex digit the rest of the exponent and three fraction bits.

### Solution 5

**Answer.** `0xBF000000`.

*Method.* $-0.5=-(1.0)_2\times2^{-1}$, so the sign bit is $1$, the fraction field is $0$, and the biased
exponent is $-1+127=126=(01111110)_2$. The pattern is `1 01111110 00000000000000000000000`, which groups
as `1011 1111 0000 0000 0000 0000 0000 0000` $=$ `0xBF000000`.

*Check.* $E=126\Rightarrow e=-1$; significand $1.0$; value $-1\cdot2^{-1}=-0.5$ ✓.

*Pitfall.* Writing `0x3F000000` gives $+0.5$; the difference between the two patterns is exactly the sign
bit, which is bit $31$, the most significant bit of the leading hex digit. Hence the leading hex digits
`3F` and `BF` for positive and negative numbers of this magnitude.

### Solution 6

**Answer.** $\varepsilon_{\mathrm{mach}}=2^{-3}=0.125$, $u=0.0625$, largest $=15$, $56$ positive
normalised elements (and $\lvert F\rvert=113$).

*Method.* Here $\beta=2$, $p=4$, $L=-3$, $U=3$.
- $\varepsilon_{\mathrm{mach}}=\beta^{1-p}=2^{-3}=0.125$; $u=\tfrac12\varepsilon_{\mathrm{mach}}=2^{-4}=0.0625$.
- Largest: $(2-2^{1-p})\beta^{U}=(2-2^{-3})\cdot2^{3}=1.875\cdot8=15$; in the form of Definition 5.1,
  $m=15\cdot2^{U-p+1}=15\cdot2^{0}=15$, so the largest significand $m=15$ times $2^{3-4+1}=1$.
- Positive count: $(\beta-1)\beta^{p-1}=1\cdot2^{3}=8$ per binade, and there are $U-L+1=7$ binades, so $56$.
- Total: $2\cdot56+1=113$ (Theorem 8.3(c)).

*Check.* The positive elements of the top binade are $8,9,\dots,15$ (step $1$), so the largest is $15$ ✓,
and the smallest positive element is $2^{L}=2^{-3}=0.125$, the leading significand $1.000$ of the bottom
binade.

### Solution 7

**Answer.** $\operatorname{ulp}(1)=2^{-52}\approx2.22\times10^{-16}$; $\operatorname{ulp}(1024)=2^{-42}\approx2.27\times10^{-13}$;
$\operatorname{ulp}(2^{20})=2^{-32}\approx2.33\times10^{-10}$; $\operatorname{ulp}(10^{16})=2$.

*Method.* By Theorem 8.3(a), $\operatorname{ulp}(x)=\beta^{e-p+1}=2^{e-52}$ on $[\beta^{e},\beta^{e+1})$.
- $1=2^{0}$, so $e=0$: $2^{-52}$.
- $1024=2^{10}$, so $e=10$: $2^{-42}$.
- $2^{20}$: $e=20$, so $2^{-32}$.
- $10^{16}$: since $2^{53}=9.007\times10^{15}\le10^{16}<2^{54}$, $e=53$, so $2^{53-52}=2$.

*Interpretation.* The gap is proportional to the magnitude: multiplying $x$ by $2^{10}$ multiplies its ulp
by $2^{10}$. The last entry shows that at magnitude $10^{16}$ the doubles are spaced $2$ apart, so an odd
integer there is not representable at all.

### Solution 8

**Answer.** $\operatorname{fl}(2/3)=(1.011)_2\times2^{-1}=0.6875$; absolute error $0.0208333\ldots$;
relative error $0.03125=2^{-5}$.

*Method.* Repeated doubling of $2/3$: $4/3$ (bit $1$, remainder $1/3$), $2/3$ (bit $0$, remainder $2/3$),
so $2/3=0.101010\ldots_2=1.0101\ldots_2\times2^{-1}$. With four significant bits we keep $1.010$ and look at
the next bit, which is $1$; rounding up gives $1.011_2=1.375$, hence $1.375\times2^{-1}=0.6875$.

*Errors.* $0.6875-2/3=\dfrac{11}{16}-\dfrac{2}{3}=\dfrac{33-32}{48}=\dfrac{1}{48}=0.0208333\ldots$, and
$$
\frac{1/48}{2/3}=\frac{1}{48}\cdot\frac{3}{2}=\frac{1}{32}=0.03125 .
$$
This is below $u=2^{-4}=0.0625$ ✓, and it is exactly half a gap in relative terms, as expected for a number
just above a tie.

### Solution 9

**Answer.** No: `0.1 + 0.2` is $0.30000000000000004440892098500626$, while the stored `0.3` is
$0.29999999999999998889776975374843$. The difference is $5.55\times10^{-17}$.

*Method.* All three decimals have infinite binary expansions (Solution 1 shows the argument for
$0.1=0.0\overline{0011}_2$; $0.2$ is the same pattern shifted, and $0.3=0.01\overline{0011}_2$). Each is
rounded to $53$ bits:
- $\operatorname{fl}(0.1)=0.1(1+5.551\times10^{-17})$,
- $\operatorname{fl}(0.2)=0.2(1+5.551\times10^{-17})$, since doubling is exact,
- $\operatorname{fl}(0.3)=0.3(1-1.850\times10^{-17})$.

Adding the first two exactly and rounding gives $0.3000000000000000444\ldots$, which is not the stored
$0.3$; the two values differ by $5.551\times10^{-17}$, exactly one ulp at $0.3$ (the gap on
$[2^{-2},2^{-1})$ is $2^{-54}=5.55\times10^{-17}$).

*Moral.* The three constants are each within $u$ of the decimals they represent, so each is "correct"; the
equality test compares bit patterns, and the bit patterns differ because the rounding errors do not cancel.
Comparing floating-point results for equality is a category error; compare with a tolerance or compare
exact rational values.

### Solution 10

**Answer.** $2^{52}$ doubles in $[2,4)$, $2^{53}$ in $[1,4)$, and $10\cdot2^{52}=4.5036\times10^{16}$ in
$[1,1024)$.

*Method.* By Theorem 8.3(b) each binade $[\beta^{e},\beta^{e+1})$ contains $(\beta-1)\beta^{p-1}=2^{52}$
doubles. The interval $[2,4)$ is one binade $[2^{1},2^{2})$, so $2^{52}$. The interval $[1,4)$ is the union
of $[1,2)$ and $[2,4)$, so $2\cdot2^{52}=2^{53}$. Finally $1024=2^{10}$, and $[1,1024)$ comprises the ten
binades $e=0,1,\dots,9$, hence $10\cdot2^{52}=4.5035996\times10^{16}$.

*Remark.* The count is the same in every binade, which is exactly the statement that the *relative* density
is constant: there are as many doubles between $1$ and $2$ as between $2^{500}$ and $2^{501}$.

### Solution 11

**Answer.** Largest finite: $(2-2^{-52})2^{1023}=1.7976931348623157\times10^{308}$; smallest normal:
$2^{-1022}=2.2250738585072014\times10^{-308}$.

*Method.* In Definition 5.1 take $m=2^{53}-1$ (the largest significand, all $53$ bits set) and $e=1023$:
$$
(2^{53}-1)2^{1023-53+1}=(2-2^{-52})2^{1023}.
$$
Evaluating in double gives $1.7976931348623157\times10^{308}$, the value reported by `DBL_MAX`. The smallest
normal is $m=2^{52}$, $e=-1022$: $2^{52}\cdot2^{-1022-53+1}=2^{-1022}$.

*Cross-check.* The binary32 analogues are $(2-2^{-23})2^{127}=3.4028235\times10^{38}$ and
$2^{-126}=1.1754944\times10^{-38}$. The ratio of the largest to the smallest normal is about $2^{2046}$ in
double precision, roughly $10^{616}$.

### Solution 12

**Answer.** $(1.101)_2\times2^{3}=13$ and $(0.00101)_2\times2^{-2}=0.0390625$.

*Method.* For the first, $(1.101)_2=1+1/2+1/8=1.625$, and $1.625\cdot8=13$. For the second,
$(0.00101)_2=2^{-3}+2^{-5}=0.125+0.03125=0.15625$, and $0.15625\cdot2^{-2}=0.0390625$.

*Remark.* The second number is $5\cdot2^{-7}$: five is the significand integer, and moving the point three
places left of $1.01$ gives $2^{-3}$ relative to $1.01$. Both values are exactly representable in binary64,
in binary32, and in any format with enough bits.

### Solution 13

**Answer.** Absolute error $0.0015927$, relative error $5.070\times10^{-4}$, three correct significant
digits.

*Method.* $\lvert3.14-\pi\rvert=0.001592653589793\ldots$. Since $10^{0}\le\pi<10^{1}$, the relative error is
$0.00159265/3.14159=5.0695\times10^{-4}$. Definition 5.5 asks for the largest $k$ with
$$
\lvert\hat x-x\rvert\le\tfrac12\cdot10^{m-k+1}=\tfrac12\cdot10^{1-k}.
$$
For $k=3$ the bound is $0.005$ ✓; for $k=4$ it is $0.0005$, which $0.00159$ exceeds. So $k=3$.

*Consistency check with the relative-error form.* $5.07\times10^{-4}\le5\cdot10^{-3}=5\cdot10^{-k}$ with
$k=3$ ✓, and exceeds $5\cdot10^{-4}$ for $k=4$ ✗ — the same answer.

## Intermediate

### Solution 14

*Strategy.* Rescale to the binade, where the gap is known, and then exhibit the worst case.

*Proof of the bound.* Let $x\in[\beta^{e},\beta^{e+1})$ with $L\le e\le U$. By Theorem 8.3(a) the machine
numbers there are spaced $h=\beta^{e-p+1}$ apart, so round-to-nearest returns the nearest one and
$\lvert\operatorname{fl}(x)-x\rvert\le h/2$. Since $\lvert x\rvert\ge\beta^{e}$,
$$
\lvert\operatorname{fl}(x)-x\rvert\le\frac{h}{2}=\frac{\beta^{e-p+1}}{2}\le\frac{\beta^{e-p+1}}{2}\cdot\frac{\lvert x\rvert}{\beta^{e}}=u\lvert x\rvert . \qquad\blacksquare
$$

*Sharpness in binary32.* Take $x=1+2^{-24}$. The neighbours are $1$ and $1+2^{-23}$, and $x$ is exactly
halfway, so the tie rule applies: $1$ has significand $1.000\ldots0$ (even last bit) and $1+2^{-23}$ has
last bit $1$, so $\operatorname{fl}(x)=1$. Hence
$$
\frac{\lvert\operatorname{fl}(x)-x\rvert}{\lvert x\rvert}=\frac{2^{-24}}{1+2^{-24}}=\frac{u}{1+u}=5.960464122\times10^{-8},
$$
with $u=2^{-24}=5.9604644775\times10^{-8}$. The relative error is smaller than $u$ but approaches it as
$p\to\infty$, so no constant below $u$ works.

*Pitfall.* For $x$ in the subnormal range the relative bound fails (only an absolute bound survives), which
is why Theorem 8.1 restricts $\lvert x\rvert\ge\beta^{L}$.

### Solution 15

*Derivation.* By Definition 5.1 the elements of $[\beta^{e},\beta^{e+1})$ are $m\beta^{e-p+1}$ with
$\beta^{p-1}\le m\le\beta^{p}-1$. Consecutive integers $m$ give consecutive elements, so the gap is the
coefficient $\beta^{e-p+1}$. At the top, $m=\beta^{p}-1$ gives $\beta^{e+1}-\beta^{e-p+1}$, whose successor
$m=\beta^{p-1}$ of the next binade is $\beta^{p-1}\beta^{e+1-p+1}=\beta^{e+1}$; the progression is continuous.

*Counts.* Number per binade: $\beta^{p}-1-\beta^{p-1}+1=(\beta-1)\beta^{p-1}=2^{52}$ for $\beta=2$, $p=53$.
In $[1,2)$: $2^{52}=4.5035996\times10^{15}$. In $[1,2^{10})$: ten binades, so $10\cdot2^{52}=4.5036\times10^{16}$.

*Check.* The gap on $[1,2)$ is $2^{0-52}=2^{-52}$, and the interval length is $1$, so a uniform grid would
need $2^{52}$ intervals and $2^{52}$ points ✓.

### Solution 16

*Strategy.* Add sequentially in binary32, keeping each partial sum to 24 bits.

$0.1$ rounds to $\operatorname{fl}_{32}(0.1)=0.100000001490116119384765625$. The computed partial sums
(exact decimal expansions of the float32 values) are

| $k$ | $s_k$ | error |
|---|---|---|
| 1 | $0.100000001490116$ | $1.49\times10^{-9}$ |
| 2 | $0.200000002980232$ | $2.98\times10^{-9}$ |
| 3 | $0.300000011920929$ | $1.19\times10^{-8}$ |
| 4 | $0.400000005960464$ | $5.96\times10^{-9}$ |
| 5 | $0.500000000000000$ | $0$ |
| 6 | $0.600000023841858$ | $2.38\times10^{-8}$ |
| 7 | $0.700000047683716$ | $4.77\times10^{-8}$ |
| 8 | $0.800000071525574$ | $7.15\times10^{-8}$ |
| 9 | $0.900000095367432$ | $9.54\times10^{-8}$ |
| 10 | $1.000000119209290$ | $1.19\times10^{-7}$ |

*Answer.* $1.00000011920928955078125$; absolute error $1.1920929\times10^{-7}$; relative error
$1.1920929\times10^{-7}=2\varepsilon_{\mathrm{mach}}=4u$.

*Bound check.* $\gamma_9=9u/(1-9u)=5.365\times10^{-7}\cdot\sum\lvert x_i\rvert$, so the observed error is
about $1/4.5$ of the worst case ✓.

*Remark.* In double precision the same ten additions give exactly $1.0$, because two of the roundings
cancel. The float32 result is *larger* than $1$ because the addend itself is larger than $0.1$ and the
accumulated rounding errors happen to be positive.

### Solution 17

*Strategy.* Compute the discriminant exactly enough to see the cancellation, then compare with the
stabilised pair.

Here $a=0.001$, $b=1000$, $c=1$, so $D=b^{2}-4ac=1\,000\,000-0.004=999999.996$.

*Textbook formula.* $\sqrt D=999.999998$. Then
$$
x_1=\frac{-1000+999.999998}{2\cdot0.001}=-0.0009999999974752427,\qquad x_2=\frac{-1000-999.999998}{0.002}=-999999.999 .
$$
The exact small root is $-0.001000000001$ (from $x=(-b+\sqrt{b^{2}-4ac})/(2a)$ in exact arithmetic,
or from the product identity), so the relative error is
$$
\frac{\lvert-0.0009999999974752427+0.001000000001\rvert}{0.001000000001}=3.52\times10^{-9}.
$$

*Stable formula.* $b>0$, so $q=-\tfrac12(1000+\sqrt D)=-999.999999$ and
$$
x_1=\frac{c}{q}=\frac{1}{-999.999999}=-0.001000000001,\qquad x_2=\frac{q}{a}=\frac{-999.999999}{0.001}=-999999.999 .
$$
The small root now has relative error $0$ to the digits displayed (below $10^{-16}$).

*Interpretation.* Here $b^{2}\gg\lvert4ac\rvert$ only moderately, so the loss is about $7$ digits rather
than $16$; the relative error $3.5\times10^{-9}$ is exactly the predicted amplification
$u\cdot(\lvert b\rvert+\sqrt D)/\lvert-b+\sqrt D\rvert\approx1.1\times10^{-16}\cdot2\times10^{6}$. The
large root is unaffected because its numerator adds.

### Solution 18

*Answer.* Naive $5.000000055588316\times10^{-5}$; stable $4.9999999874999996\times10^{-5}$; relative error
of the naive value $1.36\times10^{-8}$.

*Method.* At $x=10^{8}$, $\sqrt{x+1}=10000.00004999999\ldots$ and $\sqrt x=10000$, so the difference is
$5\times10^{-5}$ obtained by cancelling eight leading digits. The rationalised form
$$
\sqrt{x+1}-\sqrt{x}=\frac{1}{\sqrt{x+1}+\sqrt{x}}=\frac{1}{20000.00005}=4.9999999875\times10^{-5}
$$
never subtracts.

*Diagnosis.* $\lvert x\rvert+\lvert y\rvert\approx2\times10^{4}$ and $\lvert x-y\rvert\approx5\times10^{-5}$,
so the cancellation ratio is about $4\times10^{8}$; by Theorem 8.4 the relative error is at most
$u\cdot4\times10^{8}\approx4.4\times10^{-8}$, and the observed $1.36\times10^{-8}$ is within it.

### Solution 19

*Answer.* Naive $5.000444502911705\times10^{-13}$; stable $5.000000000000000\times10^{-13}$; relative error
$8.89\times10^{-5}$; the bound $4u/x^{2}=4.44\times10^{-4}$ is respected.

*Method.* $\cos(10^{-6})=0.9999999999995$ exactly to $16$ digits, so $1-\cos x$ is computed by cancelling
$1$ against a number that agrees with it in twelve digits. The stable value
$2\sin^{2}(5\times10^{-7})=5\times10^{-13}$ to machine precision.

*Check against Theorem 8.10.* The absolute error is $\lvert5.0004445-5.0\rvert\times10^{-13}=4.445\times10^{-17}$,
below $2u=2.22\times10^{-16}$ ✓. The relative error is $8.89\times10^{-5}$, below the predicted
$4u/x^{2}=4.44\times10^{-4}$ ✓ (the constant in the theorem is not optimal).

*Remark.* The relative error grows like $x^{-2}$: at $x=10^{-4}$ it would be $8.9\times10^{-9}$, and at
$x=10^{-8}$ the whole result is lost. The threshold $4u/x^{2}\approx1$ predicts catastrophe at
$x\approx\sqrt{4u}\approx2\times10^{-8}$, consistent with the table of Example 9.6.

### Solution 20

*Strategy.* Run the loop of Section 7.7 by hand, tracking $s$ and $c$.

Data: $1,\ 10^{-16},\ 10^{-16},\ 10^{-16}$.

| step | $x$ | $y=x-c$ | $t=s+y$ | $c=(t-s)-y$ | $s=t$ |
|---|---|---|---|---|---|
| 1 | $1$ | $1$ | $1$ | $0$ | $1$ |
| 2 | $10^{-16}$ | $10^{-16}$ | $1$ | $-10^{-16}$ | $1$ |
| 3 | $10^{-16}$ | $2\times10^{-16}$ | $1.0000000000000002$ | $2.204\times10^{-17}$ | $1.0000000000000002$ |
| 4 | $10^{-16}$ | $7.7955\times10^{-17}$ | $1.0000000000000002$ | $-7.7955\times10^{-17}$ | $1.0000000000000002$ |

*Answer.* Final $s=1.0000000000000002$, which equals the correctly rounded sum
(and `math.fsum`), namely $1+3\times10^{-16}$ rounded to the nearest double. The exact real sum is
$1+3\times10^{-16}$; the nearest double is $1+2^{-52}=1.0000000000000002$ because
$3\times10^{-16}=1.35$ ulps.

*Why it works.* At step 2 the true error $-10^{-16}$ is stored in $c$; at step 3 the addend is
compensated to $2\times10^{-16}$, which is large enough to move $s$ by one ulp. This is Kahan's lemma
(Theorem 8.7) in action: whenever $\lvert s\rvert\ge\lvert y\rvert$ no low-order bit is lost.

### Solution 21

*Strategy.* TwoSum of Dekker: sum, then recover the error with two subtractions and a correction.

$$
s=a\oplus b=10^{16},\qquad z=s\ominus a=0,\qquad e=(a\ominus(s\ominus z))\oplus(b\ominus z)=1\oplus0=1 .
$$

*Answer.* $s=10^{16}$, $e=1$, and $s+e=10^{16}+1=a+b$ exactly (the real sum is $10^{16}+1$, which is not
representable because the gap at $10^{16}$ is $2$).

*Explanation.* The exact sum lies between the two neighbouring doubles $10^{16}$ and $10^{16}+2$, and the
rounding chose $10^{16}$; the algorithm reconstructs the missing $1$ from the operands. This is why
TwoSum requires the branch-free Fast2Sum form only when $\lvert a\rvert\ge\lvert b\rvert$; the general
algorithm with the three subtractions works for any pair.

*Use.* A correctly rounded dot product sums the $(s_i,e_i)$ pairs in double-double arithmetic; the
recovered errors supply the low-order digits that plain summation loses.

### Solution 22

*Answer.* $\kappa\approx1001$ for $1/(x-1)$ at $1.001$, and $\kappa\approx5.86\times10^{7}$ for $\cos x$ at
$1.5707963$. The cosine is the hopeless one in double precision.

*Method.* By Theorem 8.8, $\kappa_{\mathrm{rel}}(x)=\lvert x f'(x)/f(x)\rvert$.
- $f(x)=1/(x-1)$: $f'(x)=-1/(x-1)^{2}$, so $\kappa=x/\lvert x-1\rvert=1.001/0.001=1001$. An input
  perturbation of $10^{-16}$ produces $10^{-13}$ in the output — three digits lost.
- $f(x)=\cos x$: $f'(x)=-\sin x$, so $\kappa=x\sin x/\cos x$. At $x=1.5707963$, $\cos x=2.679\times10^{-8}$
  and $\sin x\approx1$, giving $\kappa=1.5707963/2.679\times10^{-8}=5.86\times10^{7}$.

*Interpretation.* In double precision the attainable relative accuracy is about $\kappa u$: $1.1\times10^{-13}$
for the first and $6.5\times10^{-9}$ for the second. Both problems are ill conditioned, but only mildly so
for the first; the cosine loses seven digits even with a perfect algorithm, which is why
$\arccos$ near $1$ and $\sin$ near $\pi$ are computed by special formulas.

### Solution 23

*Answer.* One-pass $2.0$; two-pass $1.25$; the exact variance is $1.25$.

*Method.* With $x_i=10^{8}+i$ for $i=1,\dots,4$:
- $\bar x=10^{8}+2.5$ and $\overline{x^{2}}=10^{16}+5\times10^{8}+7.5$, so
  $\overline{x^{2}}-\bar x^{2}=1.25$ in exact arithmetic.
- In double precision $\overline{x^{2}}$ rounds to $1.0000000500000008\times10^{16}$ and
  $\bar x^{2}=1.0000000500000006\times10^{16}$; their difference is $2.0$ — but the two numbers agree in
  $16$ digits, so the difference is mostly noise.
- The two-pass formula computes $\bar x$ first and then $\frac14\sum(x_i-\bar x)^{2}
  =\frac14(2.25+0.25+0.25+2.25)=1.25$ without forming any large intermediate.

*Diagnosis.* The one-pass formula is unstable, not merely ill conditioned: $\kappa$ of the map
$(x_i)\mapsto\overline{x^{2}}-\bar x^{2}$ is about $\overline{x^{2}}/\operatorname{Var}\approx8\times10^{15}$,
which is the whole precision, and the naive evaluation adds its own rounding. Welford's recurrence avoids
both problems.

### Solution 24

*Answer.* The gap at $10^{16}$ is $2$, so $10^{16}+1$ is a tie rounded to the even significand
$10^{16}$, while $10^{16}+2$ is representable. Hence $(10^{16}+1)-10^{16}=0$ and
$(10^{16}+2)-10^{16}=2$.

*Method.* $2^{53}=9007199254740992\le10^{16}=10000000000000000<2^{54}$, so the binade is $[2^{53},2^{54})$
and by Theorem 8.3(a) the gap is $2^{53-52}=2$. The doubles there are the even integers. The real
$10^{16}+1$ lies exactly halfway between $10^{16}$ and $10^{16}+2$; ties-to-even picks $10^{16}$, whose
significand integer is even. The real $10^{16}+2$ is itself a double.

*Consequence for equality tests.* `x == y` tests bits, not mathematical equality, and two mathematically
distinct reals can share a double, while two mathematically equal expressions can differ by an ulp. Tests
must use a tolerance scaled to the problem, or exact arithmetic.

## Advanced

### Solution 25

*Strategy.* Induct on the number of terms, tracking the growth of the error factor.

Let $S_k=\sum_{i\le k}x_i$, $T_k=\sum_{i\le k}\lvert x_i\rvert$, and $\hat s_k$ be the computed partial
sum, so $\hat s_k=(\hat s_{k-1}+x_k)(1+\delta_k)$ with $\lvert\delta_k\rvert\le u$ (Theorem 8.2). Claim:
$\lvert\hat s_k-S_k\rvert\le\gamma_{k-1}T_k$.

*Base.* $k=1$: $\hat s_1=x_1$ exactly and $\gamma_0=0$ ✓.

*Step.* From the definition,
$$
\hat s_k-S_k=(\hat s_{k-1}+x_k-S_k)+(\hat s_{k-1}+x_k)\delta_k=(\hat s_{k-1}-S_{k-1})+(\hat s_{k-1}+x_k)\delta_k,
$$
so
$$
\lvert\hat s_k-S_k\rvert\le\lvert\hat s_{k-1}-S_{k-1}\rvert+u\lvert\hat s_{k-1}+x_k\rvert
\le\gamma_{k-2}T_{k-1}+u(1+\gamma_{k-2})T_{k-1}+u\lvert x_k\rvert,
$$
using $\lvert\hat s_{k-1}\rvert\le\lvert S_{k-1}\rvert+\gamma_{k-2}T_{k-1}$ and $\lvert S_{k-1}\rvert\le T_{k-1}$.

*The key identity.*
$$
\gamma_{k-2}+u(1+\gamma_{k-2})=\gamma_{k-2}(1+u)+u=\frac{(k-2)u(1+u)+u(1-(k-2)u)}{1-(k-2)u}=\frac{(k-1)u}{1-(k-2)u}\le\gamma_{k-1},
$$
because $1-(k-2)u\ge1-(k-1)u>0$. Also $u\le\gamma_{k-1}$ since $\gamma_{k-1}=(k-1)u/(1-(k-1)u)\ge u$.
Therefore
$$
\lvert\hat s_k-S_k\rvert\le\gamma_{k-1}T_{k-1}+\gamma_{k-1}\lvert x_k\rvert=\gamma_{k-1}T_k. \qquad\blacksquare
$$

*Sharpness.* Example 35 shows the bound is attained to leading order, so the linear growth in $n$ is real
and not an artefact of the proof.

### Solution 26

*Strategy.* Split into the exact case and the inexact case; in the inexact case use Sterbenz twice.

*Proof.* If $s+y$ is representable then $t=s+y$ and the computed $e=(t-s)-y$ is exact by Sterbenz
($t$ and $s$ are within a factor of two, and $(t-s)$ and $y$ likewise), giving $e=0$.

Otherwise $s+y$ is inexact. First, $\lvert s+y\rvert\ge\lvert s\rvert/2$: if instead
$\lvert s+y\rvert<\lvert s\rvert/2$, then $s$ and $-y$ satisfy $\lvert s\rvert/2\le\lvert y\rvert\le\lvert s\rvert$,
so $s+y=s-(-y)$ is a difference of two floats within a factor of two and Sterbenz (Theorem 8.12) makes it
exact — contradiction. Hence $\lvert t\rvert\ge\lvert s\rvert/2$ as well (since $t$ is within a half-gap of
$s+y$), so $t$ and $s$ lie within a factor of two and $u=t-s$ is exact.

Now $u-y=t-s-y=t-(s+y)=-\varepsilon$ where $\varepsilon$ is the rounding error of the addition. Since the
addition was inexact, $\varepsilon$ is a nonzero multiple of $\operatorname{ulp}(t)/2$ with
$\lvert\varepsilon\rvert\le\operatorname{ulp}(t)/2$, hence $\varepsilon$ is representable (its significand
needs at most one bit at the scale of $t$). Therefore the real number $u-y$ is a float equal to
$\operatorname{fl}(u-y)=e$, and $s+y=t-\varepsilon=t+e$. $\blacksquare$

*Remark.* This is Dekker's Fast2Sum, the only branch-free exact transformation that needs no assumptions
beyond $\lvert s\rvert\ge\lvert y\rvert$. Without that inequality — when a large term follows many small
ones — the lemma fails, which is Exercise 33.

### Solution 27

*Strategy.* Bound each of the four roundings and use $\lvert q\rvert\ge\lvert b\rvert/2$ to control the
divisions.

*Assumptions.* The operations are correctly rounded (Theorem 8.2), so $\operatorname{fl}(\sqrt D)=\sqrt D(1+\alpha)$
with $\lvert\alpha\rvert\le u$; $D>0$; $a\ne0$; no overflow or underflow.

*Step 1: $q$.* We have $q=-\tfrac12(b+\operatorname{sign}(b)\sqrt D)$. The two terms have the same sign, so
the addition cannot cancel: if $b>0$, then $\lvert b+\sqrt D\rvert\ge\lvert b\rvert$; the computed sum has
relative error at most $u$ for the square root, $u$ for the addition, and $u$ for the multiply by $\tfrac12$,
so $q=q_{\text{exact}}(1+\theta_1)$ with $\lvert\theta_1\rvert\le3u+O(u^{2})$. Moreover
$\lvert q\rvert\ge\tfrac12\lvert b\rvert$ and $\lvert q\rvert\ge\tfrac12\sqrt D$.

*Step 2: the root $q/a$.* Division by $a\ne0$ adds at most $u$, so $q/a$ has relative error at most
$4u+O(u^{2})$ — this root is obtained without cancellation, and $\lvert q/a\rvert\ge\lvert b/(2a)\rvert$.

*Step 3: the root $c/q$.* Similarly $c/q$ has relative error at most $4u+O(u^{2})$, and no cancellation
occurs in the division because division has none: for $q\ne0$,
$\operatorname{fl}(c/q)=(c/q)(1+\delta')$ with $\lvert\delta'\rvert\le u$ by Theorem 8.2, and the errors of
$c$ and $q$ enter additively. Hence both roots have relative error $O(u)$.

*Where the textbook formula fails.* There the small root is $(-b+\sqrt D)/(2a)$; when $b^{2}\gg\lvert4ac\rvert$
the two terms cancel, the absolute error $u\lvert b\rvert$ is inherited, and the relative error becomes
$u\lvert b\rvert/\lvert-b+\sqrt D\rvert=O(u\,b^{2}/\lvert4ac\rvert)$, unbounded as $c\to0$. The stable
formula replaces that subtraction by the division $c/q$, whose denominator is $\Theta(b)$.

### Solution 28

*Strategy.* Induct on the depth of the summation tree; each level costs one rounding.

*Claim.* For a subtree of depth $d$ containing terms indexed by $I$,
$\lvert\hat s-S\rvert\le\gamma_d\sum_{i\in I}\lvert x_i\rvert$.

*Base.* $d=0$: a single term, exact, $\gamma_0=0$ ✓.

*Step.* A subtree of depth $d$ combines two subtrees of depth $d-1$ by one rounded addition:
$\hat s=(\hat s_1+\hat s_2)(1+\delta)$, $\lvert\delta\rvert\le u$. Writing $\Sigma_j=\sum_{i\in I_j}\lvert x_i\rvert$,
$$
\lvert\hat s-S\rvert\le\lvert\hat s_1-S_1\rvert+\lvert\hat s_2-S_2\rvert+u\lvert\hat s_1+\hat s_2\rvert
\le\gamma_{d-1}(\Sigma_1+\Sigma_2)+u(1+\gamma_{d-1})(\Sigma_1+\Sigma_2),
$$
since $\lvert\hat s_j\rvert\le(1+\gamma_{d-1})\Sigma_j$. The identity proved in Solution 25 gives
$\gamma_{d-1}+u(1+\gamma_{d-1})\le\gamma_d$, so $\lvert\hat s-S\rvert\le\gamma_d(\Sigma_1+\Sigma_2)$ ✓.

*Conclusion.* A balanced tree over $n$ terms has depth $\lceil\log_2 n\rceil$, giving
$\lvert s-\sum x_i\rvert\le\gamma_{\lceil\log_2 n\rceil}\sum\lvert x_i\rvert$. For $n=10^{6}$ the depth is
$20$, so the factor is $1.2\times10^{-6}$ instead of $6.3\times10^{-2}$. $\blacksquare$

### Solution 29

*Strategy.* Count the significands and the binades; then use a parity argument for $1/3$.

*Count.* For each exponent $e\in[L,U]$, the significand integer $m$ runs over
$\beta^{p-1}\le m\le\beta^{p}-1$, which is $\beta^{p}-\beta^{p-1}=(\beta-1)\beta^{p-1}$ values. There are
$U-L+1$ exponents and two signs, and $0$ is neither positive nor negative, so
$$
\lvert F\rvert=2(\beta-1)\beta^{p-1}(U-L+1)+1 .
$$
For $F(2,3,-1,2)$: $2\cdot1\cdot4\cdot4+1=33$; for binary32 the count is $2\cdot1\cdot2^{23}\cdot254+1\approx2^{32}$,
close to the $2^{32}$ patterns (the difference is accounted for by the two zeros and by the reserved
patterns for subnormals, infinities and NaNs).

*$1/3$ is in no binary format.* Suppose $1/3=m2^{e-p+1}$ with integers. Then $2^{p-1-e}=3m$. The left side
is a power of two and the right side is divisible by three; contradiction. Hence $1/3\notin F(\beta,p,L,U)$
for every binary format. $\blacksquare$

*Remark.* Finiteness alone gives the result by countability (Theorem 8.11); the parity argument pinpoints
*which* rationals are representable: exactly those whose reduced denominator is a power of two.

### Solution 30

*Strategy.* Differentiate and apply Theorem 8.8.

*Derivation.* For $p(x)=\sum_{k=0}^{n}a_kx^{k}$ with $p(x)\ne0$ and $x\ne0$,
$$
\kappa_{\mathrm{rel}}(x)=\left\lvert\frac{x\,p'(x)}{p(x)}\right\rvert=\left\lvert\frac{\sum_{k} k\,a_kx^{k}}{\sum_k a_kx^{k}}\right\rvert .
$$
The numerator is a weighted average of the exponents $k$, with weights $a_kx^{k}$: $\kappa$ is the
"average degree" of the terms that dominate at $x$. For large $x$ it tends to $n$; for small $x$ it tends
to the lowest degree present.

*The example.* $p(x)=x^{2}+10^{8}x+1$ at $x=1$: $p(1)=10^{8}+2$ and $p'(1)=10^{8}+2$, so
$\kappa=1$.

*Interpretation.* Evaluating $p$ at $x=1$ is perfectly conditioned — a relative perturbation of $x$ changes
$p$ by the same relative amount. Yet Example 9.5 computes a root of the same polynomial with a $25\%$
error. The failure is therefore entirely *algorithmic*: the cancellation in $-b+\sqrt{b^{2}-4ac}$ is not
present in the data. This is the cleanest illustration in the chapter of the distinction between
conditioning and stability.

*Second reading.* Near a root $r$, $\kappa_{\mathrm{rel}}(x)=\lvert xp'(x)/p(x)\rvert\to\infty$ because
$p(r)=0$; that is the conditioning of the *inverse* problem (finding $r$ from $p$), not of the evaluation.

### Solution 31

*Strategy.* Use the tie point one gap above $1$.

*Construction.* For binary precision $p\ge2$ take $x=1+2^{-p}$. Then $x$ is exactly halfway between the
consecutive machine numbers $1$ and $1+2^{-p+1}=1+2u$, and the lower one has an even significand, so
ties-to-even gives $\operatorname{fl}(x)=1$ and
$$
\frac{\lvert\operatorname{fl}(x)-x\rvert}{\lvert x\rvert}=\frac{2^{-p}}{1+2^{-p}}=\frac{u}{1+u},
$$
with $u=2^{-p}$ (since $\beta=2$). For binary32 this is $5.960464122\times10^{-8}$, for binary64
$1.1102230246251563\times10^{-16}$.

*Sharpness.* Let $\varepsilon>0$. If $x$ is slightly *below* the tie point, rounding returns $1$ and the
relative error is $(2^{-p}-\varepsilon)/(1+2^{-p}-\varepsilon)$, which tends to $u/(1+u)$ from below as
$\varepsilon\to0$. Hence the supremum of the relative error over the normal range is exactly $u/(1+u)$, and
any constant valid for all $x$ must be at least that. Since $u/(1+u)<u$, Theorem 8.1's constant $u$ is
valid but not attained. $\blacksquare$

### Solution 32

*Strategy.* Monotonicity follows from the order-preserving property of "nearest"; associativity fails by
an explicit counterexample.

*Proof of monotonicity.* Let $x\le y$. If both lie in the same interval between consecutive machine numbers,
the nearest-point map is monotone there. If they lie in different intervals, let $a\le b$ be the
corresponding nearest machine numbers; if $a>b$ then $b$ is closer to $x$ than $a$ is, contradicting the
choice of $a$ (formally: the intervals are ordered, and the nearest point of a lower interval cannot exceed
the nearest point of a higher one). Hence $\operatorname{fl}(x)\le\operatorname{fl}(y)$. $\blacksquare$

*Consequence.* Since $x\mapsto x+y$ is monotone in $x$ and $\operatorname{fl}$ is monotone,
$x\mapsto x\oplus y=\operatorname{fl}(x+y)$ is monotone; similarly in $y$. So $\oplus$ is monotone in each
argument, and also commutative, but *not* associative:
$$
(1\oplus10^{-16})\oplus10^{-16}=1\oplus10^{-16}=1,\qquad 1\oplus(10^{-16}\oplus10^{-16})=1\oplus2\times10^{-16}=1.0000000000000002 .
$$
*Why.* $1+10^{-16}$ rounds to $1$ (the perturbation is below half an ulp), while
$2\times10^{-16}$ exceeds half an ulp and rounds up. Monotonicity does not imply associativity: the
rounding of the intermediate result depends on its magnitude, which the regrouping changes.

## Challenge

### Solution 33

*Data.* Take $x=[1,\,10^{100},\,1,\,-10^{100}]$. The exact sum is $2$.

*Kahan's result.* Running the loop:
- $x=1$: $s=1$, $c=0$.
- $x=10^{100}$: $y=10^{100}$, $t=10^{100}$, $c=(t-s)-y=(10^{100}-1)-10^{100}=0$, $s=10^{100}$.
- $x=1$: $y=1$, $t=10^{100}$, $c=(10^{100}-10^{100})-1=-1$, $s=10^{100}$.
- $x=-10^{100}$: $y=-10^{100}+1$, which rounds to $-10^{100}$; $t=0$; $c=(0-10^{100})-(-10^{100})=0$; $s=0$.

The computed sum is $0$, not $2$; Neumaier's variant returns $2$ (verified in double precision).

*Why Kahan's lemma does not apply.* At the third step $\lvert s\rvert=10^{100}\gg\lvert y\rvert=1$, so the
lemma does hold and $c=-1$ is exact. At the fourth step, however, $y=-10^{100}+1$ rounds to $-10^{100}$,
so the "addend" is no longer the quantity the compensation was designed for, and the sum $t=0$ cancels.
The lemma protects each addition, but the *accumulated* correction is not propagated when a large
cancelling term arrives: the exact information "$-1$" sits in $c$ and is discarded by the final rounding.
Neumaier stores $\pm((s-t)+x)$ and adds $c$ at the end, which recovers the $1$ from each cancellation.

*Lesson.* Compensated algorithms need a hypothesis on the *order* of the data, not merely on each
operation. Kahan is safe for data of slowly varying magnitude (the usual case in numerical integration);
Neumaier is safe for arbitrary order at the cost of one extra branch and one extra addition.

### Solution 34

*Proof of Sterbenz's lemma.* Let $0<y\le x\le2y$. Then $x$ and $y$ either lie in one binade $[2^{k},2^{k+1})$
or in two adjacent binades, and in both cases both are integer multiples of the gap
$h=2^{k-p+1}$ of the larger binade. Hence $x-y=jh$ with an integer $j$, and $0\le j\le2^{p}$ because
$0\le x-y\le y\le2^{k+1}=2^{p}h$. If $j=2^{p}$ then $x-y=2^{k+1}$, which is representable; if $j<2^{p}$
then $j$ fits in $p$ bits, so $jh$ is representable. $\blacksquare$

*Same binade.* If $x,y\in[2^{k},2^{k+1})$ with $x\ge y$, then $y\ge2^{k}>x/2$, so Sterbenz applies and
$x\ominus y=x-y$ exactly.

*Why this does not contradict Section 7.5.* Exactness of the subtraction means the *absolute* error is
unchanged; it says nothing about the relative error, which is
$(\text{error in }x)+(\text{error in }y)$ divided by $\lvert x-y\rvert$. When $x$ and $y$ agree to $k$
digits, $\lvert x-y\rvert$ is $10^{-k}$ times their size, so the relative error of the difference is $10^{k}$
times that of the operands. The information was lost when $x$ and $y$ were computed or stored, not when
they were subtracted. This is why reformulating the algebra (Section 7.6) is the only remedy: no amount of
care in the subtraction can recover digits that the operands never had.

### Solution 35

*Computation.* Take $x_1=1$ and $x_2=\cdots=x_{1000}=2^{-53}$, so $n=1000$ and $T_n=1+999\cdot2^{-53}$.

At every step the partial sum is $1$ (adding $2^{-53}$ to $1$ is exactly a tie between $1$ and
$1+2^{-52}$, and ties-to-even keeps $1$), so the computed sum is $s_n=1$. The exact sum is
$1+999\cdot2^{-53}=1.000000000000111$.

*Error versus the bound.* The error is
$$
999\cdot2^{-53}=1.1091128\times10^{-13},
$$
and the bound is
$$
\gamma_{999}T_n=\frac{999u}{1-999u}\left(1+999u\right)=1.1091128\times10^{-13}\quad (u=2^{-53}),
$$
to seven digits. The bound is therefore attained, not merely an overestimate.

*Generalisation.* For arbitrary $n<2^{52}$ the same data give error $(n-1)u$ and bound
$\gamma_{n-1}T_n=(n-1)u\,(1+O(nu))$, so the linear growth in $n$ is sharp. This is why summing $10^6$
terms in single precision can lose the equivalent of $\log_{2}(10^{6})\approx20$ bits — a quarter of the
significand when the terms also vary in size.

### Solution 36

*Part 1: no finite binary format contains every rational.* Suppose $\mathbb{Q}\subseteq F(\beta,p,L,U)$.
Then $\mathbb{Q}$ is a subset of a finite set, hence finite — but $\mathbb{Q}$ is infinite. Contradiction.
More concretely, Solution 29 shows that $1/3$ is in no binary format, and the argument extends to every
rational whose reduced denominator has an odd factor.

*Part 2: comparing three exact strategies.*

*Integers.* Scale so that all quantities are integers: $\frac13+\frac16$ becomes $\frac{2}{6}+\frac{1}{6}$
with numerator arithmetic $2+1=3$ over the common denominator $6$, and $\sum_{k=1}^{10^{6}}10^{-6}$ becomes
$\sum 1=10^{6}$ in units of $10^{-6}$. Integers are exact, fast, and closed under $+,-,\times$; division
requires a representation decision (rationals or a fixed scale).

*Rationals.* Represent a number as a pair $(p,q)$ with $q>0$ and $\gcd(p,q)=1$. Then
$\frac13+\frac16=\frac{2+1}{6}=\frac{3}{6}=\frac12$ exactly, with one gcd reduction. Rationals are closed
under all four operations (except division by zero), but numerator and denominator grow: summing $10^{6}$
terms of $1/k$ produces the denominator $\operatorname{lcm}(1,\dots,10^{6})$, which has about $434{,}000$
decimal digits, so the cost is superlinear and must be managed by reduction.

*Arbitrary-precision floats.* With a precision of, say, $100$ decimal digits, $\frac13+\frac16$ gives
$0.5$ followed by $99$ zeros — exact to the working precision but not *exactly* $\frac12$ unless the
representation is dyadic. Arbitrary precision removes the practical problem but not the principle: the
result is still a rounded value, and the error is bounded by $u$ times the magnitude, now with a much
smaller $u$.

*Numerical check in binary64.* $\frac13+\frac16$ evaluates to exactly $0.5$: the stored values are
$0.3333333333333333148\ldots$ and $0.1666666666666666574\ldots$, whose exact sum is
$0.4999999999999999722\ldots$, within half an ulp of $0.5$, so the final addition rounds to $0.5$. The
agreement is a coincidence of the rounding directions, not a guarantee. By contrast,
$\sum_{k=1}^{10^{6}}10^{-6}$ computed naively in double precision gives $1.000000000007918$, an error of
$7.9\times10^{-12}$, while the correctly rounded sum (and `math.fsum`) is $1.0$.

*Conclusion.* Exact arithmetic is a property of the *representation*, not of the precision: integers and
rationals are closed and exact, floating point of any fixed precision is not.
