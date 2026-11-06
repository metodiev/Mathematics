# Limits — Solutions

> [Tutorial](README.md) · [Exercises](exercises.md) · 36 worked solutions

Each solution names the method and the theorem that justifies it, shows every algebraic step, and
flags the pitfall that the problem is designed to expose. In $\varepsilon$-$\delta$ problems the
choice of $\delta$ is derived, not guessed, and the implication is verified explicitly.

## Beginner

**1.**

*Method: substitution for a polynomial (Corollary 7.6).*

$$
\lim_{x\to3}\left(x^2-2x+5\right)=3^2-2\cdot3+5=9-6+5=8 .
$$

The function is a polynomial, so the limit is its value; no denominator vanishes.

**2.**

*Method: substitution.*

$$
\lim_{x\to-2}\left(x^3+4x-1\right)=(-2)^3+4(-2)-1=-8-8-1=-17 .
$$

*Pitfall:* $(-2)^3=-8$, not $+8$; a lost sign here is the usual error.

**3.**

*Method: factoring.* Substitution gives $0/0$, so factor the difference of squares:

$$
\frac{x^2-16}{x-4}=\frac{(x-4)(x+4)}{x-4}=x+4 \qquad (x\neq4).
$$

By Theorem 8.2 (locality), the limits agree, and by substitution

$$
\lim_{x\to4}\frac{x^2-16}{x-4}=\lim_{x\to4}(x+4)=8 .
$$

*Check:* at $x=4.001$ the quotient is $8.001$, and at $x=3.999$ it is $7.999$.

**4.**

*Method: factoring both quadratics.* Substitution gives $0/0$. Factor:

$$
x^2-x-2=(x-2)(x+1), \qquad x^2-4=(x-2)(x+2).
$$

For $x\neq2$,

$$
\frac{x^2-x-2}{x^2-4}=\frac{(x-2)(x+1)}{(x-2)(x+2)}=\frac{x+1}{x+2}\longrightarrow\frac{2+1}{2+2}=\frac34 .
$$

The cancelled factor $x-2$ is legitimate because $x\neq2$ in the limit (Theorem 8.2), and the final
substitution is valid because the new denominator equals $4\neq0$ at $x=2$.

**5.**

*Method: factor out $x$.* For $x\neq0$,

$$
\frac{3x^2+x}{x}=\frac{x(3x+1)}{x}=3x+1\longrightarrow1 .
$$

*Pitfall:* do not "cancel $x$ from $3x^2$" to get $3x$ and then forget the $+1$; the factor $x$ must be
cancelled from the whole numerator, which is $x(3x+1)$, not from one term.

**6.**

*Method: factoring the difference of squares.*

$$
\frac{x^2-1}{x+1}=\frac{(x-1)(x+1)}{x+1}=x-1 \qquad (x\neq-1),
$$

so the limit is $-1-1=-2$.

*Alternative:* the numerator vanishes at $x=-1$ because $(-1)^2-1=0$; the factor theorem guarantees
the factor $x+1$.

**7.**

*Method: one-sided limits.* On the left of $0$ the formula is $x+3$, so

$$
\lim_{x\to0^-}f(x)=\lim_{x\to0^-}(x+3)=3 .
$$

On the right the formula is $x^2+1$, so

$$
\lim_{x\to0^+}f(x)=\lim_{x\to0^+}(x^2+1)=1 .
$$

The one-sided limits exist but differ ($3\neq1$), so by Theorem 7.1 the two-sided limit does not
exist. The value $f(0)=1$ is irrelevant to the left-hand limit and does not repair the mismatch.

**8.**

*Method: one-sided limits.* For $x<2$ the formula is $x^2$:

$$
\lim_{x\to2^-}g(x)=2^2=4 .
$$

For $x>2$ the formula is $5-x$:

$$
\lim_{x\to2^+}g(x)=5-2=3 .
$$

Since $4\neq3$, the two-sided limit does not exist. The function is not even defined at $x=2$ by the
given formula, but that is irrelevant: the two sides already disagree.

**9.**

*Method: divide by the highest power.* For $x\neq0$,

$$
\frac{4x^2-3}{2x^2+x}=\frac{4-\dfrac{3}{x^2}}{2+\dfrac1x}\longrightarrow\frac{4-0}{2+0}=2 .
$$

Both $3/x^2\to0$ and $1/x\to0$; the denominator limit is $2\neq0$, so the quotient law applies. The
line $y=2$ is a horizontal asymptote.

**10.**

*Method: divide by the highest power.* For $x\neq0$,

$$
\frac{5x^3+x}{x^3-2}=\frac{5+\dfrac{1}{x^2}}{1-\dfrac{2}{x^3}}\longrightarrow\frac{5+0}{1-0}=5 .
$$

The sign of $x$ is irrelevant here because only even powers of $x$ occur in the correction terms.

**11.**

*Method: sum law and $1/x^k\to0$.* Both limits exist and are finite:

$$
\lim_{x\to\infty}\frac2x=0, \qquad \lim_{x\to\infty}\frac{3}{x^2}=0,
$$

so by the sum law the limit is $0+0=0$.

**12.**

*Method: standard limit (Theorem 7.8) after a change of scale.* Write

$$
\frac{\sin 5x}{x}=5\cdot\frac{\sin 5x}{5x}.
$$

As $x\to0$, also $u=5x\to0$, and $\sin u/u\to1$. By the constant-multiple law,

$$
\lim_{x\to0}\frac{\sin 5x}{x}=5\cdot1=5 .
$$

*Pitfall:* the factor is $5$, not $1/5$; the substitution $u=5x$ multiplies the denominator by $5$,
which is compensated by the factor $5$ in front.

**13.**

*Method: half-angle identity (Corollary 7.9).*

$$
\frac{1-\cos x}{x^2}=\frac{2\sin^2(x/2)}{x^2}=\frac12\left(\frac{\sin(x/2)}{x/2}\right)^2\longrightarrow\frac12\cdot1^2=\frac12 .
$$

The limit is $\frac12$, not $0$: the numerator is of order $x^2/2$, exactly like the denominator.

**14.**

*Method: standard limit and the cosine factor.*

$$
\frac{\tan 2x}{x}=\frac{\sin 2x}{x\cos 2x}=2\cdot\frac{\sin 2x}{2x}\cdot\frac{1}{\cos 2x}.
$$

As $x\to0$, $\sin(2x)/(2x)\to1$ and $\cos 2x\to1$, so by the product and quotient laws the limit is
$2\cdot1\cdot1=2$.

## Intermediate

**15.**

*Method: rationalise the numerator.* Multiply by the conjugate $\sqrt{x+9}+3$:

$$
\frac{\sqrt{x+9}-3}{x}
=\frac{(x+9)-9}{x\left(\sqrt{x+9}+3\right)}
=\frac{x}{x\left(\sqrt{x+9}+3\right)}
=\frac{1}{\sqrt{x+9}+3}.
$$

For $x$ near $0$ the denominator is near $6\neq0$, so substitution applies:

$$
\lim_{x\to0}\frac{1}{\sqrt{x+9}+3}=\frac{1}{3+3}=\frac16 .
$$

The root law (Lemma 7.5) justifies passing the limit inside the square root, since $x+9\to9>0$.

**16.**

*Method: rationalise the numerator.* Note that $\sqrt{2\cdot4+1}=\sqrt9=3$, so the numerator vanishes
at $x=4$ and substitution gives $0/0$.

$$
\frac{\sqrt{2x+1}-3}{x-4}
=\frac{(2x+1)-9}{(x-4)\left(\sqrt{2x+1}+3\right)}
=\frac{2(x-4)}{(x-4)\left(\sqrt{2x+1}+3\right)}
=\frac{2}{\sqrt{2x+1}+3}.
$$

For $x\neq4$ the cancellation is legitimate, and

$$
\lim_{x\to4}\frac{2}{\sqrt{2x+1}+3}=\frac{2}{3+3}=\frac13 .
$$

*Pitfall:* dropping the factor $2$ in $(2x+1)-9=2(x-4)$ gives the wrong value $\frac16$; the factor must be tracked through the cancellation.

**17.**

*Method: rationalise (an $\infty-\infty$ form).*

$$
\sqrt{4x^2+3x}-2x=\frac{(4x^2+3x)-4x^2}{\sqrt{4x^2+3x}+2x}=\frac{3x}{\sqrt{4x^2+3x}+2x}.
$$

For $x>0$, divide numerator and denominator by $x>0$ and use
$\sqrt{4x^2+3x}/x=\sqrt{4+3/x}$:

$$
\frac{3}{\sqrt{4+\dfrac3x}+2}\longrightarrow\frac{3}{\sqrt4+2}=\frac34 .
$$

**18.**

*Method: rationalise, then take care with the sign.* This is an $\infty-\infty$ form:

$$
\sqrt{x^2+2x}+x=\frac{(x^2+2x)-x^2}{\sqrt{x^2+2x}-x}=\frac{2x}{\sqrt{x^2+2x}-x}.
$$

For $x<0$, $\sqrt{x^2+2x}=\lvert x\rvert\sqrt{1+2/x}=-x\sqrt{1+2/x}$. Hence the denominator is

$$
-x\sqrt{1+\frac2x}-x=-x\left(\sqrt{1+\frac2x}+1\right),
$$

and

$$
\frac{2x}{-x\left(\sqrt{1+\dfrac2x}+1\right)}=-\frac{2}{\sqrt{1+\dfrac2x}+1}\longrightarrow-\frac{2}{1+1}=-1 .
$$

*Pitfall:* using $\sqrt{x^2}=x$ instead of $-x$ gives $+1$, the wrong horizontal asymptote. The
function $\sqrt{x^2+2x}+x$ has limit $+\infty$ at $+\infty$ but tends to $-1$ at $-\infty$, so its
graph has two different horizontal asymptotes.

**19.**

*Method: divide by $x^3$.*

$$
\frac{3x^3-2x+1}{x^3+x^2-5}=\frac{3-\dfrac{2}{x^2}+\dfrac{1}{x^3}}{1+\dfrac1x-\dfrac{5}{x^3}}\longrightarrow\frac{3-0+0}{1+0-0}=3 .
$$

The denominator limit is $1\neq0$, so the quotient law applies.

**20.**

*Method: combine two standard limits.*

$$
\frac{\sin 3x}{\sin 7x}=\frac{\dfrac{\sin 3x}{x}}{\dfrac{\sin 7x}{x}}=\frac{3\cdot\dfrac{\sin 3x}{3x}}{7\cdot\dfrac{\sin 7x}{7x}}.
$$

As $x\to0$ both fractions in the numerator and denominator tend to $1$, and the denominator limit is
$7\neq0$, so

$$
\lim_{x\to0}\frac{\sin 3x}{\sin 7x}=\frac{3\cdot1}{7\cdot1}=\frac37 .
$$

**21.**

*Method: half-angle identity.*

$$
1-\cos 3x=2\sin^2\frac{3x}{2},
$$

so

$$
\frac{1-\cos 3x}{x^2}=2\cdot\frac{\sin^2(3x/2)}{x^2}
=2\left(\frac32\right)^2\left(\frac{\sin(3x/2)}{3x/2}\right)^2
=\frac92\left(\frac{\sin(3x/2)}{3x/2}\right)^2\longrightarrow\frac92 .
$$

*Check:* with $x$ replaced by $3x$ in Solution 13, the answer scales by $3^2=9$, giving $9/2$, as it
must.

**22.**

*Method: standard exponential limit (Theorem 7.10).*

$$
\frac{e^{2x}-1}{x}=2\cdot\frac{e^{2x}-1}{2x}\longrightarrow2\cdot1=2,
$$

where $u=2x\to0$ is the variable of the standard limit.

**23.**

*Method: direct $\varepsilon$-$\delta$ estimate.*

Let $\varepsilon>0$. We need

$$
\lvert (4x-1)-3\rvert=\lvert 4x-4\rvert=4\lvert x-1\rvert<\varepsilon,
$$

which holds whenever $\lvert x-1\rvert<\varepsilon/4$. Choose $\delta=\varepsilon/4>0$. Then for every
$x$ with $0<\lvert x-1\rvert<\delta$,

$$
\lvert (4x-1)-3\rvert=4\lvert x-1\rvert<4\cdot\frac{\varepsilon}{4}=\varepsilon .
$$

This is exactly Definition 5.1 with $a=1$, $L=3$. The proof uses no property of $x$ beyond
$0<\lvert x-1\rvert<\delta$; in particular $\delta$ does not depend on $x$.

**24.**

*Method: $\varepsilon$-$\delta$ with a preliminary restriction.*

Let $\varepsilon>0$. Factor:

$$
\lvert x^2-4\rvert=\lvert x-2\rvert\,\lvert x+2\rvert .
$$

We need a bound on $\lvert x+2\rvert$ near $2$. If $\lvert x-2\rvert<1$, then
$\lvert x+2\rvert=\lvert (x-2)+4\rvert\le\lvert x-2\rvert+4<5$. Hence, under the restriction
$\lvert x-2\rvert<1$,

$$
\lvert x^2-4\rvert<5\lvert x-2\rvert .
$$

Choose

$$
\delta=\min\left(1,\frac{\varepsilon}{5}\right).
$$

For $0<\lvert x-2\rvert<\delta$ both constraints hold, and

$$
\lvert x^2-4\rvert=\lvert x-2\rvert\,\lvert x+2\rvert<5\cdot\frac{\varepsilon}{5}=\varepsilon .
$$

This proves $\lim_{x\to2}x^2=4$. *Pitfall:* choosing $\delta=\varepsilon/5$ alone is not enough,
because the bound $\lvert x+2\rvert<5$ needs $\lvert x-2\rvert<1$; the minimum handles both
requirements.

**25.**

*Method: rationalise and bound the denominator away from $0$.*

Let $\varepsilon>0$. For $x\ge0$,

$$
\lvert\sqrt x-2\rvert=\frac{\lvert x-4\rvert}{\sqrt x+2}\le\frac{\lvert x-4\rvert}{2},
$$

because $\sqrt x\ge0$ makes the denominator at least $2$. Choose $\delta=\min(4,2\varepsilon)$. If
$0<\lvert x-4\rvert<\delta$, then $x>0$ (because $\delta\le4$), so the computation above applies and

$$
\lvert\sqrt x-2\rvert\le\frac{\lvert x-4\rvert}{2}<\frac{2\varepsilon}{2}=\varepsilon .
$$

The domain restriction $x\ge0$ is part of the function; the limit is two-sided in the domain of
$\sqrt x$, which near $4$ is a full neighbourhood, since $4>0$.

## Advanced

**26.**

*Method: split the tolerance $\varepsilon$ into two halves.*

Let $a$ be a limit point of the common domain, and let $\varepsilon>0$. By the definition applied with
$\varepsilon/2$, there are $\delta_1>0$ and $\delta_2>0$ such that

$$
0<\lvert x-a\rvert<\delta_1\Rightarrow\lvert f(x)-L\rvert<\frac{\varepsilon}{2},
\qquad
0<\lvert x-a\rvert<\delta_2\Rightarrow\lvert g(x)-M\rvert<\frac{\varepsilon}{2}.
$$

Set $\delta=\min(\delta_1,\delta_2)>0$. For every $x$ in the domain with $0<\lvert x-a\rvert<\delta$,

$$
\lvert (f(x)+g(x))-(L+M)\rvert\le\lvert f(x)-L\rvert+\lvert g(x)-M\rvert<\frac{\varepsilon}{2}+\frac{\varepsilon}{2}=\varepsilon .
$$

Hence $\lim_{x\to a}(f+g)=L+M$. The only ingredients are the definition and the triangle inequality;
the choice $\varepsilon/2$ is forced by the need to add two errors.

**27.**

*Method: squeeze theorem.*

For $x\neq0$, $\lvert\sin(1/x)\rvert\le1$, so

$$
-\lvert x\rvert\le x\sin\frac1x\le\lvert x\rvert .
$$

Let $f(x)=-\lvert x\rvert$ and $h(x)=\lvert x\rvert$. Both tend to $0$ as $x\to0$: for $\varepsilon>0$,
take $\delta=\varepsilon$; then $0<\lvert x\rvert<\delta$ implies $\lvert\lvert x\rvert-0\rvert<\varepsilon$
and the same for $-\lvert x\rvert$. By the squeeze theorem (Theorem 7.7) with $L=0$,

$$
\lim_{x\to0}x\sin\frac1x=0 .
$$

*Why the argument fails for $\sin(1/x)$:* the squeeze requires the two bounding functions to have the
same limit. For $\sin(1/x)$ no such bound with limit $0$ exists, because $\lvert\sin(1/x)\rvert$ is
equal to $1$ at points arbitrarily close to $0$; the oscillation has amplitude $1$, not amplitude
$\lvert x\rvert$.

**28.**

*Method: two sequences and Theorem 7.21.* Take

$$
x_n=\frac{1}{\frac{\pi}{2}+2\pi n}, \qquad y_n=\frac{1}{2\pi n} \qquad (n\in\mathbb{N}).
$$

Then $x_n>0$, $y_n>0$, and both tend to $0$ because their denominators tend to $+\infty$. Moreover,

$$
\sin\frac{1}{x_n}=\sin\left(\frac{\pi}{2}+2\pi n\right)=1,
\qquad
\sin\frac{1}{y_n}=\sin(2\pi n)=0 .
$$

Thus $f(x_n)\to1$ and $f(y_n)\to0$. If a limit $L$ existed, every sequence $z_n\to0$ with $z_n\neq0$
would have $f(z_n)\to L$ (the sequential criterion, proved in Solution 35). Applying this to
$(x_n)$ and $(y_n)$ would give $L=1$ and $L=0$, a contradiction. Hence the limit does not exist.

*Remark:* the same two sequences show that the range of $\sin(1/x)$ accumulates on all of $[-1,1]$
near $0$, so no candidate $L$ can satisfy the definition with $\varepsilon=1/2$.

**29.**

*Method: L'Hôpital's rule, with hypotheses checked.*

Write $f(x)=x-\sin x$ and $g(x)=x^3$. Both are differentiable on $\mathbb{R}$, and $g'(x)=3x^2\neq0$
for $x\neq0$. Also $f(0)=0=g(0)$, so hypothesis (H1) of Theorem 7.13 holds. The derivative ratio is

$$
\frac{f'(x)}{g'(x)}=\frac{1-\cos x}{3x^2}=\frac13\cdot\frac{1-\cos x}{x^2}.
$$

By Corollary 7.9, $\frac{1-\cos x}{x^2}\to\frac12$, so by the constant-multiple law the derivative
ratio tends to $\frac13\cdot\frac12=\frac16$. Since this is a finite limit, Theorem 7.13 gives

$$
\lim_{x\to0}\frac{x-\sin x}{x^3}=\frac16 .
$$

*Why this is not circular:* the derivative $(\sin x)'=\cos x$ is a theorem already available; the
standard limit $\sin x/x\to1$ was used to prove it, but is not being re-proved here. L'Hôpital is
applied to a *new* quotient, not to the limit that founded the derivative. Only one application is
needed: after differentiating once, the quotient is a constant multiple of the known limit
$(1-\cos x)/x^2$.

**30.**

*Method: algebra and Definition 5.4.*

Write

$$
f(x)=\frac{x}{x-2}=1+\frac{2}{x-2}.
$$

*Right-hand limit.* Let $M\in\mathbb{R}$. If $M\le0$, any $\delta>0$ works, since $f(x)>1>M$ for
$x>2$. If $M>0$, choose $\delta=2/M>0$. For $0<x-2<\delta$ we have $x-2<2/M$, hence
$2/(x-2)>M$, and therefore

$$
f(x)=1+\frac{2}{x-2}>M .
$$

This is exactly Definition 5.4 for $x\to2^+$; hence $\lim_{x\to2^+}f(x)=+\infty$.

*Left-hand limit.* For $x<2$ we have $x-2<0$, so $2/(x-2)<0$ and $f(x)=1+2/(x-2)<1$. Given
$M\in\mathbb{R}$: if $M\ge1$, every $\delta>0$ satisfies $f(x)<1\le M$ for $x\in(2-\delta,2)$. If
$M<1$, choose $\delta=\dfrac{2}{1-M}>0$. For $x\in(2-\delta,2)$,

$$
x-2>-\delta=-\frac{2}{1-M}
\ \Longrightarrow\
\frac{1}{x-2}<-\frac{1-M}{2}
\ \Longrightarrow\
\frac{2}{x-2}<-(1-M)=M-1,
$$

where the second step uses that $x-2<0$ (dividing by a negative number reverses the inequality). Hence
$f(x)=1+\frac{2}{x-2}<1+(M-1)=M$. This is Definition 5.4 for $x\to2^-$, so
$\lim_{x\to2^-}f(x)=-\infty$.

The line $x=2$ is a vertical asymptote, with the graph rising on the right and falling on the left.

**31.**

**(a) Sign preservation.** Let $\varepsilon=L/2>0$. By the definition of the limit, there is $\delta>0$
such that $0<\lvert x-a\rvert<\delta$ implies $\lvert f(x)-L\rvert<L/2$. For such $x$,

$$
f(x)=L-(L-f(x))\ge L-\lvert f(x)-L\rvert>L-\frac L2=\frac L2>0 .
$$

**(b) Order comparison.** Let $\varepsilon=(M-L)/3>0$. Choose $\delta$ so that both
$\lvert f(x)-L\rvert<\varepsilon$ and $\lvert g(x)-M\rvert<\varepsilon$ on the punctured
$\delta$-neighbourhood. There,

$$
f(x)<L+\varepsilon=L+\frac{M-L}{3}=\frac{2L+M}{3},
\qquad
g(x)>M-\varepsilon=M-\frac{M-L}{3}=\frac{2M+L}{3}.
$$

Since $M>L$, we have $\frac{2L+M}{3}<\frac{2M+L}{3}$, so $f(x)<g(x)$ on that neighbourhood. *Pitfall:*
the conclusion is strict inequality on a neighbourhood, which is stronger than the order-preservation
theorem (Theorem 8.1) and requires the strict hypothesis $L<M$.

**32.**

**(a)** For every real $u,v$, the reverse triangle inequality gives

$$
\bigl\lvert\lvert u\rvert-\lvert v\rvert\bigr\rvert\le\lvert u-v\rvert .
$$

Let $\varepsilon>0$ and choose $\delta>0$ with $\lvert f(x)-L\rvert<\varepsilon$ for
$0<\lvert x-a\rvert<\delta$. Then

$$
\bigl\lvert\lvert f(x)\rvert-\lvert L\rvert\bigr\rvert\le\lvert f(x)-L\rvert<\varepsilon,
$$

so $\lvert f(x)\rvert\to\lvert L\rvert$.

**(b)** Let $f(x)=x/\lvert x\rvert$ for $x\neq0$, with any value at $0$. Then $\lvert f(x)\rvert=1$ for
all $x\neq0$, so $\lvert f(x)\rvert\to1$. But $f(x)=1$ for $x>0$ and $f(x)=-1$ for $x<0$, so the
one-sided limits at $0$ are $1$ and $-1$; by Theorem 7.1 the two-sided limit of $f$ does not exist.
Thus $\lvert f\rvert$ may converge while $f$ does not: taking absolute values destroys sign
information, and it cannot be recovered from the limit of $\lvert f\rvert$.

## Challenge

**33.**

*Proof of the squeeze theorem.* Let $\varepsilon>0$. By the definition of the limit for $f$, there is
$\delta_1>0$ with

$$
0<\lvert x-a\rvert<\delta_1\Rightarrow\lvert f(x)-L\rvert<\varepsilon,
$$

which in particular gives $f(x)>L-\varepsilon$. By the definition for $h$, there is $\delta_2>0$ with

$$
0<\lvert x-a\rvert<\delta_2\Rightarrow\lvert h(x)-L\rvert<\varepsilon,
$$

which gives $h(x)<L+\varepsilon$. Set $\delta=\min(\delta_0,\delta_1,\delta_2)>0$. For every $x$ in
the domain with $0<\lvert x-a\rvert<\delta$,

$$
L-\varepsilon<f(x)\le g(x)\le h(x)<L+\varepsilon .
$$

Hence $-\varepsilon<g(x)-L<\varepsilon$, that is, $\lvert g(x)-L\rvert<\varepsilon$. Therefore
$\lim_{x\to a}g(x)=L$.

*One-sided version.* Suppose $f(x)\le g(x)\le h(x)$ for $0<x-a<\delta_0$ and
$\lim_{x\to a^+}f(x)=\lim_{x\to a^+}h(x)=L$. Given $\varepsilon>0$, choose $\delta_1,\delta_2>0$ as
above but with the condition $0<x-a<\delta_i$; set $\delta=\min(\delta_0,\delta_1,\delta_2)$. For
$0<x-a<\delta$ the same chain of inequalities holds, so $\lvert g(x)-L\rvert<\varepsilon$. Hence
$\lim_{x\to a^+}g(x)=L$. The proof for $x\to a^-$ is identical with $0<a-x<\delta$. $\blacksquare$

**34.**

*Proof.* Suppose $\lvert f(x)\rvert\le B$ for $0<\lvert x-a\rvert<r$, with $B\ge0$. Let $\varepsilon>0$.

If $B=0$, then $f(x)=0$ on the punctured $r$-neighbourhood, so $f(x)g(x)=0$ there and the limit is
$0$.

If $B>0$, choose $\delta>0$ with $\delta\le r$ and $\lvert g(x)\rvert<\varepsilon/B$ for
$0<\lvert x-a\rvert<\delta$ (possible because $g\to0$). Then for $0<\lvert x-a\rvert<\delta$,

$$
\lvert f(x)g(x)\rvert=\lvert f(x)\rvert\,\lvert g(x)\rvert\le B\cdot\frac{\varepsilon}{B}=\varepsilon .
$$

Hence $fg\to0$. No limit of $f$ is required: only the bound. In particular $f$ may oscillate
violently, as long as it stays bounded.

*Application.* For $x\neq0$ and $n\ge1$, $\lvert\sin(1/x)\rvert\le1$, so

$$
\lvert x^n\sin(1/x)\rvert\le\lvert x\rvert^n\longrightarrow0 .
$$

Taking $f(x)=\sin(1/x)$ (bounded by $1$) and $g(x)=x^n$ (tending to $0$), the lemma gives
$x^n\sin(1/x)\to0$. The limit of $f$ itself does not exist when $n=0$; for $n\ge1$ the factor $x^n$
forces the product to $0$ even though $\sin(1/x)$ oscillates. $\blacksquare$

**35.**

**(a) Sequential criterion.**

*($\Rightarrow$)* Assume $\lim_{x\to a}f(x)=L$, and let $(x_n)$ be a sequence in the domain with
$x_n\neq a$ and $x_n\to a$. Given $\varepsilon>0$, choose $\delta>0$ as in Definition 5.1. Since
$x_n\to a$, there is $N$ such that $\lvert x_n-a\rvert<\delta$ for all $n\ge N$; since $x_n\neq a$,
this gives $0<\lvert x_n-a\rvert<\delta$, hence $\lvert f(x_n)-L\rvert<\varepsilon$ for all $n\ge N$.
Therefore $f(x_n)\to L$.

*($\Leftarrow$)* Assume the sequential property holds for $L$ and suppose, for contradiction, that
$\lim_{x\to a}f(x)\neq L$. Negating Definition 5.1 gives an $\varepsilon>0$ such that for every
$\delta>0$ there exists $x$ in the domain with $0<\lvert x-a\rvert<\delta$ and
$\lvert f(x)-L\rvert\ge\varepsilon$. Apply this with $\delta=1/n$ for each $n\in\mathbb{N}$ and call
the resulting point $x_n$. Then $x_n\neq a$, $\lvert x_n-a\rvert<1/n$, so $x_n\to a$, while
$\lvert f(x_n)-L\rvert\ge\varepsilon$ for every $n$. Hence $f(x_n)$ does not converge to $L$,
contradicting the sequential property. Therefore $\lim_{x\to a}f(x)=L$.

**(b)** Take

$$
x_n=\frac{1}{2\pi n}, \qquad y_n=\frac{1}{(2n+1)\pi} \qquad (n\in\mathbb{N}).
$$

Both tend to $0$, and both are nonzero. But

$$
\cos\frac{1}{x_n}=\cos(2\pi n)=1, \qquad \cos\frac{1}{y_n}=\cos((2n+1)\pi)=-1 .
$$

If $\lim_{x\to0}\cos(1/x)$ existed and equalled $L$, part (a) would force $L=1$ and $L=-1$,
a contradiction. Hence the limit does not exist.

**36.**

**(a)** Assume $\lim_{x\to\infty}f(x)=L$. Let $\varepsilon>0$. By Definition 5.3 there is $M\in\mathbb{R}$
such that $x>M$ implies $\lvert f(x)-L\rvert<\varepsilon$. Choose $N\in\mathbb{N}$ with $N>M$. For every
$n\ge N$ we have $n>M$, hence $\lvert a_n-L\rvert=\lvert f(n)-L\rvert<\varepsilon$. Therefore
$a_n\to L$.

**(b)** Let $f(x)=\sin(\pi x)$. For every integer $n\ge1$, $f(n)=\sin(\pi n)=0$, so the sequence
$a_n=f(n)$ converges to $0$. But $f$ has no limit as $x\to\infty$: the sequences $x_n=2n$ and
$y_n=2n+\frac12$ both tend to $+\infty$, while $f(x_n)=0$ and $f(y_n)=\sin(2\pi n+\pi/2)=1$. Two
sequences with different value-limits prove non-existence (the sequential criterion for limits at
infinity, the same argument as Theorem 7.21). The converse of (a) therefore fails: convergence along
the integers is weaker than convergence along the reals.

**(c)** For $x>0$, write

$$
x^{1/x}=e^{(\ln x)/x}.
$$

*Step 1: $\dfrac{\ln x}{x}\to0$.* This is an $\infty/\infty$ form. Take $f(x)=\ln x$ and $g(x)=x$ on
$(0,\infty)$. Both are differentiable, $g'(x)=1\neq0$, and $\lvert g(x)\rvert=x\to+\infty$, so (H2) of
Theorem 7.13 holds. The derivative ratio is

$$
\frac{f'(x)}{g'(x)}=\frac{1/x}{1}=\frac1x\longrightarrow0 .
$$

By L'Hôpital's rule, $\ln x/x\to0$.

*Step 2: $e^{y}\to e^{0}=1$ as $y\to0$.* From Theorem 7.10, $e^y-1=y\cdot\frac{e^y-1}{y}\to0$, so
$e^y\to1$; more generally, $e^y-e=e(e^{y-1}-1)\to0$, so $e^y\to e$.

Combining the two steps (composition of the limit with the continuous exponential, justified by
$e^y\to e$ as $y\to1$), we obtain

$$
\lim_{x\to\infty}x^{1/x}=e^{0}=1 .
$$

*Remark:* numerically, $1000^{1/1000}\approx1.0069$, consistent with a limit of $1$ from above.
