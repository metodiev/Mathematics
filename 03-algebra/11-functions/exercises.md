# Functions — Exercises

> [Tutorial](README.md) · 37 problems · Levels: Beginner, Intermediate, Advanced, Challenge

Work each problem completely: show the substitution or algebraic step, state domains and ranges in
interval notation, and justify every "one-to-one" or "therefore" with an argument rather than an
example. Proof problems require a general argument; a single example never proves a statement, though
it can disprove one. Full solutions are in [solutions.md](solutions.md); do not open that file until
you have attempted the problems.

## Beginner

**1.** For $f(x)=3x^2-2x+1$, compute $f(0)$, $f(-1)$, $f(2)$ and $f(a)$.

**2.** For $g(x)=\dfrac{x+1}{x-4}$, compute $g(0)$, $g(5)$ and $g(-1)$, and state the value of $x$ at
which $g$ is undefined.

**3.** Find the natural domain of $f(x)=\sqrt{x-5}$.

**4.** Find the natural domain of $h(x)=\dfrac{2x}{x^2-9}$.

**5.** Find the domain and the range of $f(x)=x^2-4$.

**6.** Does the equation $y^2=x$ define $y$ as a function of $x$? Justify your answer with the vertical
line test.

**7.** Is $f(x)=x^3$ one-to-one on $\mathbb{R}$? Justify your answer.

**8.** Decide whether $f(x)=x^4-3x^2$ is even, odd or neither.

**9.** Decide whether $f(x)=x^3+x$ is even, odd or neither.

**10.** Let $f(x)=2x-5$ and $g(x)=x^2$. Find $(f\circ g)(x)$ and $(g\circ f)(x)$.

**11.** Find the inverse of $f(x)=4x-7$, and verify that $f\big(f^{-1}(x)\big)=x$.

**12.** The Celsius temperature $C$ corresponding to a Fahrenheit temperature $F$ is
$C(F)=\tfrac59(F-32)$. Compute $C(32)$ and $C(212)$, find the inverse function $C^{-1}$, and use it to
convert $37\,^\circ\text{C}$ to Fahrenheit.

## Intermediate

**13.** Find the domain and the range of $g(x)=\sqrt{16-x^2}$.

**14.** Find the natural domain of $f(x)=\dfrac{\sqrt{x+3}}{x-2}$.

**15.** For $f(x)=x^2+5x$, form and simplify the difference quotient
$\dfrac{f(x+h)-f(x)}{h}$.

**16.** Compute the average rate of change of $f(x)=x^3$ on $[1,3]$.

**17.** Starting from the graph of $y=x^2$, describe the transformations that produce
$y=-2(x-3)^2+1$. State the vertex, the axis of symmetry, the domain and the range.

**18.** Write $y=\tfrac12\sqrt{4-x}$ as a sequence of transformations of $y=\sqrt{x}$, and state its
domain and range.

**19.** Let $f(x)=\sqrt{x}$ and $g(x)=x+2$. Find $(f\circ g)(x)$ and $(g\circ f)(x)$, together with the
domain of each.

**20.** Let $f(x)=\dfrac{1}{x-2}$ and $g(x)=x^2-4$. Find $(f\circ g)(x)$ and $(g\circ f)(x)$, together
with the domain of each.

**21.** Find the inverse of $f(x)=\dfrac{3x-1}{x+2}$, and state the domain and range of $f$ and of
$f^{-1}$.

**22.** For
$$f(x)=\begin{cases}x+2, & x<0,\\ x^2, & 0\le x\le 2,\\ 5, & x>2,\end{cases}$$
compute $f(-3)$, $f(0)$, $f(2)$, $f(4)$, and find the range of $f$.

**23.** Write $f(x)=x^3-2x^2+x-5$ as the sum of an even function and an odd function.

**24.** Write $h(x)=\lvert x-2\rvert+\lvert x+2\rvert$ as a piecewise function without absolute values,
sketch its graph, and find its minimum value and range.

## Advanced

**25.** Prove that $f(x)=x^3+x$ is one-to-one on $\mathbb{R}$, and hence find $f^{-1}(10)$.

**26.** Let $f$ and $g$ have domains symmetric about $0$. Prove each of the following, or give a
counterexample: (a) odd $\circ$ odd is odd; (b) even $\circ$ odd is even; (c) odd $\circ$ even is even;
(d) even $\circ$ even is even.

**27.** (a) Prove that if $f$ and $g$ are both one-to-one, then $f\circ g$ is one-to-one. (b) Give
explicit functions for which $f\circ g$ is one-to-one but $f$ is not.

**28.** Let $f(x)=x^2-6x+5$ with domain $[3,\infty)$. Show that $f$ is one-to-one on this domain, find
$f^{-1}$, and state the domain and range of both functions.

**29.** Let $f$ be a function with $\operatorname{dom} f=[-1,5]$. Describe how the graph of
$y=f(2x-6)$ is obtained from the graph of $y=f(x)$, distinguishing it from $y=f(2x)$ and from
$y=f(x-6)$, and find the domain of $y=f(2x-6)$.

**30.** Compute the average rate of change of $f(x)=\dfrac1x$ on the interval $[1,1+h]$ with $h>0$,
simplify the result, and explain what happens as $h$ becomes small.

**31.** Prove that a strictly increasing function on an interval is one-to-one there. Then use
$a^3-b^3=(a-b)(a^2+ab+b^2)$ to prove that $x\mapsto x^3$ is strictly increasing on $\mathbb{R}$.

**32.** Let $f(x)=\sqrt{x-1}$ and let $g(x)=x^2+2$ with domain $[0,\infty)$. Show that $g$ is
one-to-one, find $g^{-1}$, compute $f\circ g$, and find $(f\circ g)^{-1}$ twice — once directly and
once using $(f\circ g)^{-1}=g^{-1}\circ f^{-1}$ — confirming that the two answers agree.

**33.** A rectangular pen is built against a straight wall using $40$ m of fencing for the three
remaining sides. If $x$ is the length of each of the two sides perpendicular to the wall, the enclosed
area is $A(x)=x(20-x)$. State the domain forced by the geometry, find the range of $A$, and compute the
average rate of change of $A$ on $[2,6]$, interpreting the sign.

## Challenge

**34.** Let $f(x)=\dfrac{ax+b}{cx+d}$ with $ad-bc\ne 0$. (a) Determine the natural domain of $f$.
(b) Prove that $f$ is one-to-one on its domain. (c) Find $f^{-1}$ and show it has the same form, with
the roles of the coefficients exchanged. (d) Explain what happens when $c=0$.

**35.** Let $g:A\to B$ and $f:B\to C$. (a) Prove that if $f\circ g$ is one-to-one then $g$ is
one-to-one. (b) Prove that if $f\circ g$ is onto $C$ then $f$ is onto $C$. (c) Show by example that
neither converse holds. (d) Prove that $(f^{-1})^{-1}=f$ when $f:A\to B$ is a bijection.

**36.** For a function $f$, the graphs of $y=\lvert f(x)\rvert$ and $y=f(\lvert x\rvert)$ are built in
different ways. (a) Describe the geometric effect of each transformation and prove your description
from the definitions. (b) Prove that $x\mapsto f(\lvert x\rvert)$ is always even. (c) Apply both to
$f(x)=x^2-2x$: give the zeros, the vertex and the range of each resulting function.

**37.** Prove that $f(x)=\dfrac{x}{1-x}$ is a bijection from $(0,1)$ onto $(0,\infty)$; find its
inverse; and explain why this shows that an interval of finite length and an infinite interval can be
put into one-to-one correspondence.
