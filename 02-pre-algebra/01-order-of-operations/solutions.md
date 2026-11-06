# Order of Operations — Solutions

> [Tutorial](README.md) · [Exercises](exercises.md)

Each solution shows the intermediate line after every precedence level. If your answer differs, compare the intermediate lines before assuming the final arithmetic is wrong: precedence errors usually appear one line before the final answer.

## Beginner

**1.** Multiplication before addition:
$$8 + 4 \times 3 = 8 + 12 = 20.$$

**2.** Division before subtraction:
$$25 - 6 \div 2 = 25 - 3 = 22.$$

**3.** Exponents first, then add:
$$3^2 + 4^2 = 9 + 16 = 25.$$

**4.** Exponentiation, then multiplication, then addition:
$$2 + 3^2 \times 2 = 2 + 9 \times 2 = 2 + 18 = 20.$$
The common wrong answer $50$ comes from $(2+3)^2\times2$, which is a different expression.

**5.** Multiplication and division share one level and are read left to right:
$$18 \div 3 \times 2 = (18 \div 3) \times 2 = 6 \times 2 = 12.$$

**6.** The parentheses force the multiplication first:
$$18 \div (3 \times 2) = 18 \div 6 = 3.$$
Comparing with Problem 5 shows that the parentheses change the value from $12$ to $3$.

**7.** Exponentiation binds more tightly than the minus sign:
$$-4^2 = -(4^2) = -16.$$
Read it as "the negative of four squared", not "negative four, squared".

**8.** Here the parentheses include the minus sign in the base:
$$(-4)^2 = (-4)(-4) = 16.$$

**9.** Both roots are exact:
$$\sqrt{64} - \sqrt{9} = 8 - 3 = 5.$$

**10.** Parentheses first, then the cube:
$$(5-2)^3 = 3^3 = 27.$$

**11.** Grouping symbol, then multiplication and division left to right:
$$4(6+2) \div 8 = 4 \times 8 \div 8 = 32 \div 8 = 4.$$

## Intermediate

**12.** Parentheses, then multiplication and division left to right, then addition:
$$7 + 2(9-4) \div 5 = 7 + 2 \times 5 \div 5 = 7 + 10 \div 5 = 7 + 2 = 9.$$

**13.** The fraction bar groups the whole numerator and denominator. Numerator: $3\times4=12$, then $15-12=3$. Denominator: $2+1=3$. Hence
$$\dfrac{15-3\times4}{2+1} = \dfrac{3}{3} = 1.$$

**14.** Work from the innermost parentheses outward:
$$4-6=-2,$$
$$3-(-2)=3+2=5,$$
$$2\times5=10,$$
$$5-10=-5.$$
So the value is $-5$. The sign change at the second line is the step most often missed.

**15.** The radical groups the subtraction:
$$100-64=36,\qquad \sqrt{36}=6,\qquad 6\times3=18.$$
Do not split the root: $\sqrt{100}-\sqrt{64}=10-8=2$ would be a different expression.

**16.** Multiplication before addition. First
$$\dfrac{1}{6}\times\dfrac{3}{4}=\dfrac{3}{24}=\dfrac{1}{8}.$$
Then
$$\dfrac{2}{3}+\dfrac{1}{8}=\dfrac{16}{24}+\dfrac{3}{24}=\dfrac{19}{24}.$$
The fraction is already in lowest terms because $19$ is prime and does not divide $24$.

**17.** Substitute with parentheses:
$$2(-2)^2 - 3(-2) + 1 = 2\cdot4 + 6 + 1 = 8+6+1=15.$$
The term $-3(-2)$ is $+6$; losing that sign gives the wrong answer $3$.

**18.** Substitute:
$$\dfrac{a+b}{a-b}=\dfrac{5+(-3)}{5-(-3)}=\dfrac{2}{8}=\dfrac{1}{4}.$$
The denominator is $5+3=8$, not $5-3=2$.

**19.** Parentheses, then exponent, then multiplication, then addition:
$$2^3 + 3(4-1)^2 = 8 + 3(3)^2 = 8 + 3\cdot9 = 8+27 = 35.$$
Note that $(4-1)^2=9$, not $16-1=15$.

**20.** We need the sum $2+3$ to be multiplied by $4$, and then $1$ subtracted:
$$(2+3)\times4 - 1 = 5\times4-1=20-1=19.$$
The unparenthesized expression equals $2+12-1=13$.

**21.** Compute both sides.
$$\text{Left: }(10-4)-3=6-3=3.$$
$$\text{Right: }10-(4-3)=10-1=9.$$
The statement is **false**: subtraction is not associative. In general $a-(b-c)=a-b+c$, whereas $(a-b)-c=a-b-c$; the two differ by $2c$.

## Advanced

**22.** Innermost first:
$$3-1=2,$$
$$2(2)=4 \quad\text{(inside the brackets)},$$
$$5-4=1,$$
$$4[1]=4,$$
$$2+4=6,$$
$$3\{6\}=18,$$
$$18\div6=3.$$
The value is $3$.

**23.** Direct evaluation:
$$\dfrac{x^2-y^2}{x-y}=\dfrac{5^2-(-3)^2}{5-(-3)}=\dfrac{25-9}{8}=\dfrac{16}{8}=2.$$
Factoring gives $x^2-y^2=(x-y)(x+y)$, so
$$\dfrac{(x-y)(x+y)}{x-y}=x+y=5+(-3)=2,$$
provided $x-y\neq0$. The two answers must agree because cancelling the factor $x-y$ is valid exactly when $x\neq y$; here $5-(-3)=8\neq0$. If $x=y$ the original expression is $0/0$, which is undefined, while $x+y=2x$ is perfectly well defined — a reminder that cancellation carries a hypothesis.

**24.** By the right-to-left convention for power towers,
$$2^{3^2}=2^{(3^2)}=2^9=512.$$
With explicit parentheses,
$$(2^3)^2=8^2=64.$$
They are **not** equal. The notation $2^{3^2}$ means the first; the second would usually be simplified using $(a^m)^n=a^{mn}$ to $2^6=64$. The right-associative convention is what makes the tower notation express something that cannot be written as a single product of exponents.

**25.** (a) With equal precedence read left to right:
$$6\div2(1+2)=6\div2\times3=(6\div2)\times3=3\times3=9.$$
(b) If juxtaposition binds more tightly than $\div$:
$$6\div\bigl(2(1+2)\bigr)=6\div(2\times3)=6\div6=1.$$
Unambiguous rewrites: for $9$,
$$(6\div2)(1+2)\quad\text{or}\quad \dfrac{6}{2}(1+2),$$
and for $1$,
$$\dfrac{6}{2(1+2)}.$$
The original string is genuinely ambiguous; choosing a convention resolves it, but writing the parentheses avoids the argument entirely.

**26.** Take $a=10$, $b=4$, $c=3$:
$$(a-b)-c=(10-4)-3=6-3=3,$$
$$a-(b-c)=10-(4-3)=10-1=9.$$
Both readings are legal; the standard left-to-right convention selects the first. In general,
$$(a-b)-c=a-b-c,\qquad a-(b-c)=a-b+c,$$
so the results differ by $2c$ and coincide only when $c=0$. (Any example with $c\neq0$ works, e.g. $a=5,b=1,c=2$ gives $2$ versus $6$.)

**27.** Absolute value first, then exponent, then multiplication, then subtraction:
$$\lvert -8\rvert - 2^2\times(-3) = 8 - 4\times(-3) = 8 - (-12) = 8+12 = 20.$$
Two sign traps: $-2^2=-4$, and subtracting a negative product adds.

**28.** Numerator:
$$(2+3)^2-(2^2+3^2)=5^2-(4+9)=25-13=12.$$
Denominator: $2\times3=6$. Hence the value is $12/6=2$.

The numerator is $2\cdot2\cdot3$ because expanding the square gives
$$(2+3)^2=2^2+2\cdot2\cdot3+3^2.$$
Subtracting $2^2+3^2$ leaves the cross term $2\cdot2\cdot3=12$. This is a special case of $(a+b)^2-(a^2+b^2)=2ab$.

## Challenge

**29.** One solution is
$$8\div\left(3-\dfrac{8}{3}\right).$$
Check the parentheses first:
$$3-\dfrac{8}{3}=\dfrac{9}{3}-\dfrac{8}{3}=\dfrac{1}{3},$$
so
$$8\div\dfrac{1}{3}=8\times3=24.$$
The expression uses $8$, $3$, $8$, $3$ exactly once. (Other solutions exist, for example $8\div(3-8\div3)$ is the same expression written with $\div$ instead of a fraction bar.)

**30.** One construction for each value, each using exactly four $4$s:
$$1=\dfrac{44}{44},\qquad 2=\dfrac{4}{4}+\dfrac{4}{4},\qquad 3=\dfrac{4+4+4}{4},$$
$$4=4+(4-4)\times4,\qquad 5=\dfrac{4\times4+4}{4}.$$
Checks: $44/44=1$; $1+1=2$; $12/4=3$; $4+0\cdot4=4$; $(16+4)/4=5$. Many other answers are possible — for instance $4=(4-4)\times4+4$ and $5=4+(4+4)\div4$ — so the answer is not unique.

**31.** The student computed
$$(2+3)\times4=5\times4=20.$$
That is, they multiplied $4$ by the *sum* $2+3$. In the written expression $2+3\times4$ there are no parentheses, so multiplication is applied to $3$ and $4$ only: $3\times4=12$, and then $2+12=14$. The student silently supplied parentheses that were not written.

**32.** Treat numerator and denominator as separate grouped expressions.

Numerator:
$$(-2)^3=(-2)(-2)(-2)=-8,$$
$$-(-2)^3=-(-8)=8,$$
$$(-3)^2=9,$$
$$8+9=17.$$

Denominator: the exponent applies to $2$ only, because $-2^2=-(2^2)$:
$$-2^2+1=-4+1=-3.$$

Therefore
$$\dfrac{-(-2)^3+(-3)^2}{-2^2+1}=\dfrac{17}{-3}=-\dfrac{17}{3}.$$
If the denominator had been read as $(-2)^2+1=5$, the answer would be $17/5$ — a sign-and-grouping error, not an arithmetic slip.
