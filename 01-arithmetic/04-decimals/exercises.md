# Decimals — Exercises

> [Decimals](README.md) · 36 problems · Attempt all problems before reading [solutions.md](solutions.md).

Work with exact decimal values unless a problem explicitly asks for a rounded answer. For problems
about floating point, assume IEEE 754 double precision (53 bits of significand).

## Beginner

**1.** A laboratory sample has mass $47.382$ grams. Write this number in expanded place-value form
and as a fraction whose denominator is a power of ten. Is the fraction in lowest terms?

**2.** A wrench is marked $0.625$ inch. Write this measurement as a fraction in lowest terms and
identify the denominator's prime factorisation.

**3.** A carpenter cuts a strip of wood $\tfrac{11}{25}$ metre long. Write this length as a decimal.

**4.** Two wires have diameters $0.07$ mm and $0.1$ mm. Which wire is thicker? Justify your answer
by comparing place values, not by counting digits.

**5.** A calculator displays $2.71828$. Round this number to (a) two decimal places, (b) three
decimal places, and (c) four decimal places.

**6.** A chemical analysis reports a concentration of $0.0034789$ grams per litre. Round this value
to three significant figures.

**7.** A cyclist rides $2.7$ km, then $0.45$ km, then $12.003$ km. What is the total distance?

**8.** A rectangular tile measures $0.6$ m by $0.25$ m. What is its area in square metres?

**9.** A $5.4$-litre bottle of solvent is decanted into vials of capacity $0.045$ litre. How many
full vials can be filled?

**10.** A computer's memory is quoted as $3.2\times10^{4}$ bytes, and a timing interval is
$5.67\times10^{-3}$ seconds. Write both numbers in ordinary decimal notation.

**11.** The diameter of a fine wire is $0.000407$ metres. Write this diameter in scientific
notation.

**12.** A bolt has diameter $\tfrac{9}{16}$ inch. Does its decimal expansion terminate? Use the
denominator criterion to justify your answer, and give the decimal.

## Intermediate

**13.** Convert the repeating decimals $0.\overline{4}$ and $0.\overline{27}$ to fractions in lowest
terms. (They arise as two measured ratios in a workshop.)

**14.** A pipe diameter is $0.1\overline{6}$ inch. Convert this repeating decimal to a fraction in
lowest terms.

**15.** A gear turns through a cycle of $0.\overline{142857}$ of a revolution. Convert this value to
a fraction in lowest terms.

**16.** A mechanic compares four gear ratios: $\tfrac{7}{12}$, $\tfrac{9}{40}$, $\tfrac{11}{250}$,
and $\tfrac{5}{6}$. Which of these have terminating decimal expansions? Give the terminating
decimals.

**17.** A laboratory formula is $0.125\times0.8\div0.04$. Evaluate it exactly.

**18.** A ledger records a balance of $12.5$, then a debit of $3.75$, then a credit of $0.625$. What
is the final balance?

**19.** Four sheet-metal thicknesses are given as $\tfrac{3}{8}$ mm, $0.38$ mm, $0.385$ mm, and
$\tfrac{2}{5}$ mm. Arrange them in increasing order.

**20.** A digital balance displays $5.9995$ grams. Round the reading to three decimal places.
Explain why every digit changes, and state the result with the correct number of significant
figures.

**21.** State the number of significant figures in each measurement: (a) $0.03050$ g, (b) $10.0$
mL, (c) $4.500$ kg, (d) $1200$ m written without a decimal point. Explain the ambiguity in part
(d).

**22.** A sensor records $4.8\times10^{6}$ counts in $2.4\times10^{-3}$ seconds. Compute the rate in
counts per second and write the answer in scientific notation.

**23.** A cable contains $6.1\times10^{4}$ strands, each of thickness $1.9\times10^{-6}$ m. Estimate
the total thickness to one significant figure, then compute the exact product and state whether the
estimate is within $5\%$ of it.

**24.** A pump delivers $0.035$ litre per stroke. How many litres are delivered in $12{,}500$
strokes? Report the result to three significant figures.

## Advanced

**25.** Let $\tfrac{p}{q}$ be a fraction in lowest terms with $q>0$. Prove that if $\tfrac{p}{q}$
has a terminating decimal expansion, then $q=2^{a}5^{b}$ for some integers $a,b\ge 0$.

**26.** Prove that $0.\overline{9}=1$ in two different ways: one algebraic and one using truncations
or a contradiction argument. Explain why the equality is exact rather than approximate.

**27.** A machinist records a measurement of $2.3\overline{81}$ inches. Convert this repeating
decimal to a fraction in lowest terms.

**28.** Prove the decimal-place rule for multiplication: if $a=\tfrac{A}{10^{m}}$ and
$b=\tfrac{B}{10^{n}}$ with $A,B$ integers, then $ab=\tfrac{AB}{10^{m+n}}$. Explain what happens to
trailing zeros and why they may be dropped.

**29.** A spreadsheet first rounds $2.45$ to one decimal place and then rounds the result to the
nearest integer. A second cell rounds $2.45$ directly to the nearest integer. Compute both results
and explain why they differ. Which procedure better preserves the original value?

**30.** Find three terminating decimals between $0.21$ and $0.22$. Then prove that between any two
distinct terminating decimals there is another terminating decimal.

**31.** Show that $0.75=0.74\overline{9}$ and $0.125=0.124\overline{9}$. State and justify the general
rule that produces the second expansion of a terminating decimal.

**32.** A programmer writes a loop that adds $0.2$ five times and compares the result with $1.0$.
Explain why the comparison may fail in double precision. Give the exact stored value of $0.2$ to
$20$ significant digits and the computed value of $0.2+0.4$ as usually displayed.

## Challenge

**33.** Prove that between any two distinct real numbers $a<b$ there is a terminating decimal. (You
may use the fact that for every positive real number $x$ there is an integer $k$ with
$10^{-k}<x$.)

**34.** Prove the classification theorem: a real number is rational if and only if its decimal
expansion is eventually periodic. Give both directions, including the pigeonhole argument for
rationals and the conversion formula for eventually periodic decimals.

**35.** Find the smallest positive integer $n$ such that the decimal expansion of $\tfrac{1}{n}$ has
period exactly $3$. Justify both that your $n$ works and that no smaller $n$ works.

**36.** In double precision, compute $(0.1+0.2)+0.3$ and $0.1+(0.2+0.3)$. Explain why the two
results can differ, even though exact real arithmetic gives the same value. Does this contradict
the associative law of addition?
