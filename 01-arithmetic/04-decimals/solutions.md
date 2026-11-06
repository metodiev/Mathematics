# Decimals — Solutions

> [Decimals](README.md) · [Exercises](exercises.md) · Full worked solutions.

## Beginner

### **1.**

The place values to the right of the point are $10^{-1}=0.1$, $10^{-2}=0.01$, and
$10^{-3}=0.001$. Reading the digits of $47.382$:

$$
47.382=4\cdot10+7\cdot1+3\cdot0.1+8\cdot0.01+2\cdot0.001.
$$

There are three digits after the point, so the denominator is $10^{3}=1000$:

$$
47.382=\frac{47382}{1000}.
$$

The numerator and denominator are both even, so the fraction is **not** in lowest terms. Divide
by $2$:

$$
\frac{47382}{1000}=\frac{23691}{500}.
$$

The numerator $23691$ is odd and does not end in $0$ or $5$, so no further factor $2$ or $5$
cancels. The reduced denominator is $500=2^{2}\cdot5^{3}$, which is of the form $2^{a}5^{b}$, as
Theorem 7.1 requires for a terminating decimal.

### **2.**

There are three digits after the point, so

$$
0.625=\frac{625}{1000}.
$$

The greatest common divisor of $625$ and $1000$ is $125$:

$$
\frac{625}{1000}=\frac{625\div125}{1000\div125}=\frac{5}{8}.
$$

The denominator is $8=2^{3}$, a power of $2$, so the decimal terminates after three places.

### **3.**

Write the fraction with denominator $100$:

$$
\frac{11}{25}=\frac{11\cdot4}{25\cdot4}=\frac{44}{100}=0.44.
$$

Equivalently, the denominator $25=5^{2}$ has $\max(0,2)=2$ decimal places, and
$11\div25=0.44$.

### **4.**

Write both diameters with the same number of decimal places:

$$
0.07=0.07,\qquad 0.1=0.10.
$$

Compare place by place from the left. The tenths digits are $0$ and $1$. Since $0<1$, we have
$0.07<0.10$ and the answer is already decided; the hundredths digits never need to be compared.
Equivalently, $0.07$ is seven hundredths while $0.1$ is ten hundredths, and seven is less than
ten. The wire of diameter $0.1$ mm is thicker.

The common error is to see the digit $7$ in $0.07$ and conclude that it is larger. Place value
decides: the $7$ is in the hundredths place, not the tenths place.

### **5.**

**(a)** To two decimal places, the first discarded digit is the third decimal digit, $8$. Since
$8\ge5$, the second digit $1$ increases to $2$: $2.72$.

**(b)** To three decimal places, the first discarded digit is the fourth decimal digit, $2$. Since
$2<5$, the first three digits stay: $2.718$.

**(c)** To four decimal places, the first discarded digit is the fifth decimal digit, $8$. The
fourth digit $2$ increases to $3$: $2.7183$.

### **6.**

The number $0.0034789$ has leading zeros that are not significant. The first three significant
digits are $3,4,7$. The next digit is $8\ge5$, so the $7$ rounds up to $8$:

$$
0.0034789\approx0.00348.
$$

The result has three significant figures; its leading zeros only fix the position of the decimal
point.

### **7.**

Align the decimal points and pad with zeros:

$$
\begin{array}{r}
2.700\\
0.450\\
12.003\\
\hline
15.153
\end{array}
$$

The total distance is $15.153$ km.

### **8.**

Multiply the side lengths:

$$
0.6\times0.25=\frac{6}{10}\times\frac{25}{100}=\frac{150}{1000}=0.150=0.15.
$$

The area is $0.15$ square metres. The factor $0.6$ has one decimal place and $0.25$ has two, so
the product has $1+2=3$ decimal places before the trailing zero is dropped.

### **9.**

Division by $0.045$ is the same as multiplication by $1000$ in both numerator and denominator:

$$
5.4\div0.045=\frac{5.4}{0.045}=\frac{5400}{45}=120.
$$

Exactly $120$ full vials can be filled.

### **10.**

For $3.2\times10^{4}$, the exponent $4$ moves the decimal point four places right:

$$
3.2\times10^{4}=32{,}000.
$$

For $5.67\times10^{-3}$, the exponent $-3$ moves the point three places left:

$$
5.67\times10^{-3}=0.00567.
$$

### **11.**

Move the decimal point four places to the right to obtain a significand between $1$ and $10$:

$$
0.000407=4.07\times10^{-4}.
$$

The exponent is $-4$ because the point was moved four places right.

### **12.**

The denominator is $16=2^{4}$, so by Theorem 7.1 the decimal terminates. Concretely,

$$
\frac{9}{16}=\frac{9\cdot625}{16\cdot625}=\frac{5625}{10000}=0.5625.
$$

It terminates after $\max(4,0)=4$ decimal places.

## Intermediate

### **13.**

For $x=0.\overline{4}$, the repeating block has length $1$:

$$
10x=4.\overline{4}=4+x.
$$

Hence $9x=4$ and $x=\tfrac{4}{9}$.

For $y=0.\overline{27}$, the block has length $2$:

$$
100y=27.\overline{27}=27+y.
$$

Hence $99y=27$ and

$$
y=\frac{27}{99}=\frac{3}{11}.
$$

Both fractions are in lowest terms.

### **14.**

Let $x=0.1\overline{6}=0.16666\ldots$. Multiply by $10$ to move the non-repeating digit:

$$
10x=1.\overline{6}.
$$

Multiplying by $10$ again shifts one full repeating block:

$$
100x=16.\overline{6}.
$$

Subtract the first equation from the second:

$$
90x=15,\qquad x=\frac{15}{90}=\frac{1}{6}.
$$

As a check, $1\div6=0.16666\ldots$.

### **15.**

Let $x=0.\overline{142857}$. The block has length $6$, so

$$
10^{6}x=142857.\overline{142857}=142857+x.
$$

Thus

$$
(10^{6}-1)x=142857,\qquad x=\frac{142857}{999999}.
$$

Now $999999=7\cdot142857$ (check: $7\cdot142857=999999$), so

$$
x=\frac{142857}{7\cdot142857}=\frac{1}{7}.
$$

This confirms the familiar expansion $1/7=0.\overline{142857}$.

### **16.**

Apply Theorem 7.1 to each reduced denominator:

* $\tfrac{7}{12}$: $12=2^{2}\cdot3$, and the factor $3$ does not cancel with $7$, so the decimal
  repeats.
* $\tfrac{9}{40}$: $40=2^{3}\cdot5$, so it terminates. Multiplying by $25$:
  $\tfrac{9}{40}=\tfrac{225}{1000}=0.225$.
* $\tfrac{11}{250}$: $250=2\cdot5^{3}$, so it terminates. Multiplying by $4$:
  $\tfrac{11}{250}=\tfrac{44}{1000}=0.044$.
* $\tfrac{5}{6}$: $6=2\cdot3$, and the factor $3$ does not cancel with $5$, so the decimal repeats
  ($0.8\overline{3}$).

The terminating decimals are $0.225$ and $0.044$.

### **17.**

Compute the product first:

$$
0.125\times0.8=\frac{125}{1000}\times\frac{8}{10}
=\frac{1000}{10000}=0.1.
$$

Then divide by $0.04$:

$$
0.1\div0.04=\frac{0.1}{0.04}=\frac{10}{4}=2.5.
$$

The value is exactly $2.5$.

### **18.**

Subtract the debit:

$$
12.5-3.75=8.75.
$$

Add the credit:

$$
8.75+0.625=9.375.
$$

The final balance is $9.375$. In aligned form, $12.500-3.750=8.750$ and $8.750+0.625=9.375$;
the decimal points line up in every column.

### **19.**

Convert each fraction to a decimal:

$$
\frac{3}{8}=0.375,\qquad \frac{2}{5}=0.4=0.400.
$$

Now compare $0.375$, $0.380$, $0.385$, and $0.400$ place by place. The tenths digits are all $3$
or $4$; the smallest is $0.375$ (tenths $3$). Among the remaining three, $0.380<0.385<0.400$.
Hence

$$
\frac{3}{8}<0.38<0.385<\frac{2}{5}.
$$

### **20.**

To round $5.9995$ to three decimal places, look at the fourth decimal digit, which is $5$. Round
half up, so add $1$ to the third decimal place. Since that digit is $9$, the carry propagates
through every position:

$$
5.9995\longrightarrow 6.000.
$$

The result is $6.000$, not $5.999$ and not $6$. The trailing zeros are significant: $6.000$ has
four significant figures and records that the value is known to three decimal places. The original
$5.9995$ had five significant figures; rounding to three decimal places reduces the number of
significant figures because the carry absorbs the leading digit.

### **21.**

**(a)** $0.03050$: the leading zeros are not significant; the digits $3,0,5,0$ are. Four
significant figures.

**(b)** $10.0$: the trailing zero after the decimal point is significant. Three significant
figures.

**(c)** $4.500$: all four digits are significant, including the two trailing zeros. Four
significant figures.

**(d)** $1200$ written without a decimal point is ambiguous. The trailing zeros could be
placeholders (two significant figures, if the measurement is to the nearest hundred), or one or
both could be significant (three or four significant figures). Scientific notation removes the
ambiguity: $1.2\times10^{3}$ has two, $1.20\times10^{3}$ has three, and $1.200\times10^{3}$ has
four.

### **22.**

Divide the significands and subtract the exponents:

$$
\frac{4.8\times10^{6}}{2.4\times10^{-3}}
=\frac{4.8}{2.4}\times10^{6-(-3)}
=2.0\times10^{9}.
$$

The rate is $2.0\times10^{9}$ counts per second. The subtraction of a negative exponent is the
step most often missed: $6-(-3)=9$.

### **23.**

Round each significand to one digit:

$$
6.1\approx6,\qquad 1.9\approx2.
$$

Then

$$
(6\times10^{4})(2\times10^{-6})=12\times10^{-2}=1.2\times10^{-1}=0.12\ \text{m}.
$$

The exact product is

$$
(6.1\times10^{4})(1.9\times10^{-6})=(6.1\cdot1.9)\times10^{-2}=11.59\times10^{-2}=0.1159.
$$

The relative error of the estimate is

$$
\frac{|0.12-0.1159|}{0.1159}=\frac{0.0041}{0.1159}\approx0.0354=3.54\%,
$$

which is within $5\%$. The estimate has the correct order of magnitude, which is its main purpose.

### **24.**

Multiply the volume per stroke by the number of strokes:

$$
0.035\times12{,}500=437.5\ \text{litres}.
$$

To three significant figures, $437.5$ rounds to $438$ (the fourth significant digit is $5$, so the
third digit $7$ rounds up to $8$). In scientific notation, $4.38\times10^{2}$ litres.

## Advanced

### **25.**

Suppose $\tfrac{p}{q}$ has a terminating decimal expansion. Then for some integer $k\ge0$ and some
integer $N$,

$$
\frac{p}{q}=\frac{N}{10^{k}}.
$$

Cross-multiplying gives

$$
p\cdot10^{k}=qN.
$$

Thus $q$ divides $p\cdot10^{k}$. Because $\tfrac{p}{q}$ is in lowest terms, $\gcd(p,q)=1$. A
standard consequence of unique prime factorisation is Euclid's lemma: if $q$ divides a product
and is coprime to one factor, it divides the other. Hence

$$
q\mid10^{k}=2^{k}5^{k}.
$$

Therefore every prime factor of $q$ is either $2$ or $5$, so $q=2^{a}5^{b}$ for some integers
$a,b\ge0$. This includes the case $q=1$, where $a=b=0$.

### **26.**

**Algebraic proof.** Let $x=0.\overline{9}$. Multiplying by $10$ shifts the decimal point one
place:

$$
10x=9.\overline{9}=9+0.\overline{9}=9+x.
$$

Subtracting $x$ from both sides gives

$$
9x=9,\qquad x=1.
$$

**Truncation proof.** The $n$-th truncation is

$$
T_{n}=\frac{9}{10}+\frac{9}{10^{2}}+\cdots+\frac{9}{10^{n}}.
$$

Multiply by $1-\tfrac{1}{10}$; all intermediate terms cancel:

$$
\left(1-\frac{1}{10}\right)T_{n}
=\frac{9}{10}-\frac{9}{10^{n+1}}.
$$

Since the left factor is $\tfrac{9}{10}$,

$$
T_{n}=1-\frac{1}{10^{n}}.
$$

For every $\varepsilon>0$ choose $n$ with $10^{-n}<\varepsilon$. Then

$$
1-\varepsilon<T_{n}<1,
$$

so $|1-T_{n}|<\varepsilon$. The truncations approach $1$ arbitrarily closely, and by the
definition of an infinite decimal, $0.\overline{9}=1$.

The equality is exact because $0.\overline{9}$ denotes the limit of its truncations, not any one
truncation. The truncations $0.9,0.99,0.999,\ldots$ are all less than $1$, but their limit is $1$.
There is no positive real number between $0.\overline{9}$ and $1$.

### **27.**

Let $x=2.3\overline{81}=2.3818181\ldots$. The non-repeating part has one digit and the repeating
block has two digits. Multiply by $10$ and by $1000$:

$$
10x=23.\overline{81}=23.818181\ldots,
$$

$$
1000x=2381.\overline{81}=2381.818181\ldots.
$$

Subtract the first equation from the second:

$$
990x=2381.818181\ldots-23.818181\ldots=2358.
$$

Hence

$$
x=\frac{2358}{990}.
$$

Divide numerator and denominator by $18$:

$$
\frac{2358}{990}=\frac{131}{55}.
$$

As a check, $131\div55=2.381818\ldots=2.3\overline{81}$.

### **28.**

Let $a=\dfrac{A}{10^{m}}$ and $b=\dfrac{B}{10^{n}}$, where $A$ and $B$ are integers and $m,n\ge0$.
Then

$$
ab=\frac{A}{10^{m}}\cdot\frac{B}{10^{n}}
=\frac{AB}{10^{m}10^{n}}
=\frac{AB}{10^{m+n}},
$$

using $10^{m}10^{n}=10^{m+n}$. This is the decimal-place rule: multiply the integers $A$ and $B$,
then place the decimal point $m+n$ places from the right.

Trailing zeros arise when $AB$ has factors of $10$. For example,

$$
0.25\times0.4=\frac{25}{100}\times\frac{4}{10}=\frac{100}{1000}=0.100=0.1.
$$

The value $0.100$ and $0.1$ are the same real number, because $\tfrac{100}{1000}=\tfrac{1}{10}$.
The trailing zeros may therefore be dropped without changing the value. They should be retained
only when they carry information about significant figures.

### **29.**

**First procedure.** Round $2.45$ to one decimal place. The first discarded digit is $5$, so round
half up: $2.45\to2.5$. Then round $2.5$ to the nearest integer. The first discarded digit is $5$,
so round half up again: $2.5\to3$.

**Second procedure.** Round $2.45$ directly to the nearest integer. The first discarded digit is
$4<5$, so the integer part stays: $2.45\to2$.

The two procedures give $3$ and $2$. They differ because the first rounding moved the value to a
tie ($2.5$), and the second rounding then resolved that tie upward. This is the double-rounding
problem: rounding is not associative.

The direct procedure better preserves the original value. The number $2.45$ is at distance $0.45$
from $2$ and $0.55$ from $3$, so its nearest integer is $2$. Rounding twice produces $3$, which is
farther from the original value. In calculations, keep full precision and round once, at the end.

### **30.**

Three terminating decimals between $0.21$ and $0.22$ are

$$
0.211,\qquad 0.2149,\qquad 0.219.
$$

Each has a finite number of decimal places, so each terminates.

For the general proof, let $a<b$ be distinct terminating decimals. Write both with the same number
$k$ of decimal places:

$$
a=\frac{A}{10^{k}},\qquad b=\frac{B}{10^{k}},
$$

where $A$ and $B$ are integers with $A<B$. Define

$$
c=\frac{a+b}{2}=\frac{A+B}{2\cdot10^{k}}.
$$

The denominator is $2\cdot2^{k}5^{k}=2^{k+1}5^{k}$, which has only the prime factors $2$ and $5$.
Hence $c$ is a terminating decimal by Theorem 7.1. Since $a<b$,

$$
a=\frac{a+a}{2}<\frac{a+b}{2}<\frac{b+b}{2}=b,
$$

so $a<c<b$. Repeating the construction with $a,c$ or $c,b$ produces infinitely many terminating
decimals in the interval.

### **31.**

For $0.75$, write

$$
0.75=\frac{75}{100}=\frac{74}{100}+\frac{1}{100}.
$$

Now $\tfrac{1}{100}=0.00999\ldots=0.00\overline{9}$, so

$$
0.75=0.74+0.00\overline{9}=0.74\overline{9}.
$$

For $0.125$,

$$
0.125=\frac{125}{1000}=\frac{124}{1000}+\frac{1}{1000}.
$$

Since $\tfrac{1}{1000}=0.000999\ldots=0.000\overline{9}$,

$$
0.125=0.124+0.000\overline{9}=0.124\overline{9}.
$$

In general, if $x=\tfrac{N}{10^{k}}$ is a terminating decimal, then

$$
x=\frac{N-1}{10^{k}}+\frac{1}{10^{k}}.
$$

The first term is a terminating decimal with at most $k$ places; the second term is
$0.\underbrace{00\cdots0}_{k\text{ zeros}}999\ldots$, which equals $10^{-k}$. Hence $x$ has the
second expansion obtained by decreasing the last nonzero digit of the terminating expansion by $1$
(borrowing through any zeros) and appending infinitely many $9$s. For example,
$0.250=0.249\overline{9}$ and $1=0.\overline{9}$.

### **32.**

The fraction $0.2=\tfrac{1}{5}$ has reduced denominator $5$. A fraction has a terminating binary
expansion exactly when its reduced denominator is a power of $2$ (the binary analogue of Theorem
7.1). The factor $5$ prevents this, so the binary expansion of $0.2$ repeats forever:

$$
0.2_{10}=0.001100110011\ldots_{2}.
$$

A double stores the nearest representable number, which is exactly

$$
0.200000000000000011102230246251565404236316680908203125.
$$

To $20$ significant digits this is $0.20000000000000001110$. Adding the stored values of $0.2$ and
$0.4$ and rounding to the nearest double gives

$$
0.2+0.4=0.600000000000000088817841970012523233890533447265625,
$$

displayed by most languages as `0.6000000000000001`.

A loop that starts at $0$ and adds $0.2$ ten times accumulates ten rounded additions. In double
precision the result is $1.9999999999999998$, not $2.0$, so a direct comparison with `2.0` fails.
The remedy is to compare with a tolerance, or to use exact decimal arithmetic when exact decimal
values are required.

## Challenge

### **33.**

Let $a<b$ be real numbers. Choose a positive integer $k$ such that

$$
10^{-k}<b-a.
$$

Such a $k$ exists by the Archimedean property of the real numbers. Let $m$ be the smallest integer
strictly greater than $a\cdot10^{k}$; such an integer exists because the integers are unbounded
above. By minimality, $m-1\le a\cdot10^{k}$, so

$$
m\le a\cdot10^{k}+1.
$$

Dividing by $10^{k}$ gives

$$
a<\frac{m}{10^{k}}\le a+10^{-k}<a+(b-a)=b.
$$

Thus $\tfrac{m}{10^{k}}$ is a terminating decimal lying strictly between $a$ and $b$. (If
$a\cdot10^{k}$ is itself an integer, the strict inequality $m>a\cdot10^{k}$ ensures the decimal is
strictly greater than $a$; the upper bound is still strict because $10^{-k}<b-a$.)

This proves that the terminating decimals are dense in the real line.

### **34.**

**Rational $\Rightarrow$ eventually periodic.** Let $x=\tfrac{p}{q}$ with $q>0$. Perform long
division. Write

$$
p=q a_{0}+r_{0},\qquad 0\le r_{0}<q,
$$

and for $i\ge1$,

$$
10r_{i-1}=q d_{i}+r_{i},\qquad 0\le r_{i}<q.
$$

After $n$ steps,

$$
\frac{p}{q}
=a_{0}+\frac{d_{1}}{10}+\cdots+\frac{d_{n}}{10^{n}}
+\frac{r_{n}}{q\cdot10^{n}},
$$

and the final term tends to $0$ as $n\to\infty$, so the digits $d_{1}d_{2}\ldots$ form the decimal
expansion of $\tfrac{p}{q}$.

Each remainder $r_{i}$ lies in the finite set $\{0,1,\ldots,q-1\}$. If some $r_{i}=0$, the
expansion terminates. Otherwise all remainders lie in the $(q-1)$-element set
$\{1,\ldots,q-1\}$; among the $q+1$ remainders $r_{0},r_{1},\ldots,r_{q}$ two are equal by the
pigeonhole principle. Say $r_{i}=r_{j}$ with $0\le i<j\le q$. The long-division rule is
deterministic, so the block of digits $d_{i+1}\cdots d_{j}$ repeats forever. Hence the expansion is
eventually periodic.

**Eventually periodic $\Rightarrow$ rational.** First consider a pure repeating decimal

$$
x=0.\overline{b_{1}\cdots b_{k}}.
$$

Let $N$ be the integer formed by the block. Then

$$
10^{k}x=N+0.\overline{b_{1}\cdots b_{k}}=N+x,
$$

so $(10^{k}-1)x=N$ and $x=\dfrac{N}{10^{k}-1}$, a rational number.

For a mixed decimal $x=a_{1}\cdots a_{m}.\overline{b_{1}\cdots b_{k}}$, multiply by $10^{m}$ and by
$10^{m+k}$:

$$
10^{m}x=A.\overline{b_{1}\cdots b_{k}},\qquad
10^{m+k}x=B.\overline{b_{1}\cdots b_{k}},
$$

where $A$ is the integer formed by $a_{1}\cdots a_{m}$ and $B$ is the integer formed by
$a_{1}\cdots a_{m}b_{1}\cdots b_{k}$. Subtracting gives

$$
\left(10^{m+k}-10^{m}\right)x=B-A,
$$

hence

$$
x=\frac{B-A}{10^{m}\left(10^{k}-1\right)},
$$

a quotient of integers. A terminating decimal is already of the form $N/10^{k}$. Therefore every
eventually periodic decimal is rational.

Combining the two directions: a real number is rational if and only if its decimal expansion is
eventually periodic.

### **35.**

Write $n=2^{a}5^{b}m$ where $\gcd(m,10)=1$. Multiplying by $2^{a}5^{b}$ only shifts the decimal
point and adds a finite preperiod, so the eventual period of $1/n$ is the period of $1/m$. Thus we
may assume $\gcd(n,10)=1$.

The decimal expansion of $1/n$ has period exactly $3$ precisely when $10^{3}\equiv1\pmod n$ and
$10^{2}\not\equiv1\pmod n$ (the condition $10\not\equiv1$ is then automatic, since if $10\equiv1$
then $10^{2}\equiv1$). The first congruence says $n\mid10^{3}-1=999$.

Factor

$$
999=27\cdot37=3^{3}\cdot37.
$$

Its positive divisors are

$$
1,\ 3,\ 9,\ 27,\ 37,\ 111,\ 333,\ 999.
$$

A divisor $n$ of $999$ has period $1$ or $2$ exactly when $n\mid10^{2}-1=99$. Among the divisors of
$999$, the ones that divide $99$ are $1,3,9$ (indeed $11,33,99$ are not divisors of $999$). Every
other divisor of $999$ has period exactly $3$, because it divides $10^{3}-1$ but not $10^{2}-1$
and therefore cannot have period $1$ or $2$. The smallest is $n=27$.

Check directly:

$$
10^{1}=10\not\equiv1\pmod{27},\qquad
10^{2}=100\equiv19\not\equiv1\pmod{27},\qquad
10^{3}=1000\equiv1\pmod{27},
$$

since $1000-999=1$. Therefore the period of $1/27$ is exactly $3$:

$$
\frac{1}{27}=0.\overline{037}.
$$

No smaller $n$ works: any $n<27$ with period $3$ would have a divisor $m<27$ coprime to $10$ with
period $3$, forcing $m\mid999$ and $m\nmid99$; but the divisors of $999$ below $27$ are
$1,3,9$, all of which divide $99$ and have period $1$.

### **36.**

In double precision, the left-associated sum is

$$
(0.1+0.2)+0.3=0.6000000000000001,
$$

while the right-associated sum is

$$
0.1+(0.2+0.3)=0.6.
$$

The difference arises from rounding at each addition. The stored value of $0.1$ is slightly larger
than $0.1$, and the stored value of $0.2$ is slightly larger than $0.2$. Their sum rounds to
$0.30000000000000004$. Adding the stored value of $0.3$ (which is slightly smaller than $0.3$) and
rounding again gives $0.6000000000000001$. In the other order, $0.2+0.3$ happens to round exactly
to $0.5$, and then $0.1+0.5$ rounds to the double nearest $0.6$, displayed as `0.6`.

This does not contradict the associative law of addition. The associative law is a theorem about
exact real numbers: $(x+y)+z=x+(y+z)$ for all real $x,y,z$. Floating-point addition is a different
operation: each addition is followed by rounding to the nearest representable double. That rounded
operation is not associative. The two expressions agree in exact real arithmetic (both equal
$0.6$); they differ only because the computer rounds intermediate results.
