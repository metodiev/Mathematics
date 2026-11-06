# Random Variables — Exercises

> [Random Variables](README.md) · 36 problems · Beginner → Challenge · Solutions: [solutions.md](solutions.md)

Work through the problems in order. Every problem is solvable from the tutorial; the section reference tells you
where to look. Do not consult [solutions.md](solutions.md) until you have written an attempt.

**Conventions.** $U\sim\text{Uniform}(a,b)$ means the uniform law on $(a,b)$. Densities are zero outside the
stated support. $\Phi$ and $\varphi$ are the standard normal CDF and density, and $\Gamma$ is the gamma
function. "Verify" means check the defining property by computation, not by assertion.

## Beginner

**1.** *(§7.2)* A discrete random variable has $p_X(0)=0.2$, $p_X(1)=0.5$, $p_X(2)=0.3$ and $p_X=0$ elsewhere.

(a) Verify that this is a mass function.
(b) Compute $\Pr(X\le1)$, $\Pr(X\ge1)$, $\Pr(0<X<2)$ and $\Pr(X=2)$.
(c) Compute $F_X(1.5)$ and $F_X(2)$.
(d) Sketch (in words) the shape of $F_X$ and state where it jumps.

**2.** *(§7.3)* Let $f(x)=cx^2$ for $0<x<1$ and $f(x)=0$ otherwise.

(a) Find $c$.
(b) Find the CDF $F$.
(c) Compute $\Pr(X>1/2)$.
(d) Find the median $Q(1/2)$ exactly, and approximate it.

**3.** *(§7.3)* Let $X\sim\text{Uniform}(2,6)$.

(a) Write down the density and the CDF.
(b) Compute $\Pr(2.5<X<4)$.
(c) Find the median.
(d) Compute $\Pr(X=3)$ and explain the answer.

**4.** *(§7.3, §9.6)* Let $X\sim\text{Exponential}(2)$, so $f(x)=2e^{-2x}$ for $x>0$.

(a) Verify that $f$ is a density.
(b) Compute $\Pr(X>1)$ and $\Pr(X\le0.5)$.
(c) Find the median, exactly and approximately.
(d) Compute $\Pr(X=1)$.

**5.** *(§7.4)* A random variable has

$$
F(x)=\begin{cases}0,&x<0,\\ 0.2,&0\le x<1,\\ 0.7,&1\le x<3,\\ 1,&x\ge3.\end{cases}
$$

(a) Verify that $F$ is a CDF, checking right-continuity at $x=0,1,3$.
(b) Find the mass function.
(c) Compute $\Pr(0.5<X\le2.5)$ and $\Pr(X=1.5)$.
(d) Find the median and the $0.8$-quantile.

**6.** *(§7.3)* A random variable has $F(x)=0$ for $x<0$, $F(x)=x^3$ for $0\le x<1$, and $F(x)=1$ for $x\ge1$.

(a) Verify that $F$ is a CDF.
(b) Find the density.
(c) Compute $\Pr(X\le0.5)$ and $\Pr(0.5<X<1)$.
(d) Find the median exactly.

**7.** *(§7.3, §7.10)* Let $f(x)=2x$ for $0<x<1$ and $0$ otherwise.

(a) Verify that $f$ is a density.
(b) Find $F$ and compute $\Pr(0.2<X<0.6)$.
(c) Find the largest value taken by $f$. Is the density allowed to exceed $1$?
(d) Compute $\Pr(X=0.5)$.

**8.** *(§7.10)* Let $f(x)=2$ for $0<x<1/2$ and $f(x)=0$ otherwise.

(a) Verify that $f$ is a density, and explain why a density of $2$ is not a probability of $2$.
(b) Find the CDF.
(c) Compute $\Pr(X=0.25)$, $\Pr(0.25<X<0.5)$ and $\Pr(0.24<X<0.26)$.
(d) A student says "the density at $0.25$ is $2$, so $X$ is more than twice as likely to be near $0.25$ as a
uniform variable would be". Is the statement meaningful, and is the comparison correct?

**9.** *(§7.6)* Let $X\sim\text{Uniform}(0,1)$ and $Y=3X+1$.

(a) Find the density and the CDF of $Y$ without using the general formula, by working from events in $X$.
(b) Check the result with the formula for an affine map.
(c) Find $Q_Y(p)$ and verify that $Q_Y(p)=3Q_X(p)+1$.

**10.** *(§7.6)* Let $X\sim\text{Uniform}(0,1)$ and $Y=X^2$.

(a) Find the density of $Y$ by summing over preimages.
(b) Find the CDF of $Y$ directly and differentiate it.
(c) Is $Y$ uniform on $(0,1)$? Explain.

**11.** *(§7.8, §7.9)* The joint mass function of $(X,Y)$, with $X,Y\in\{0,1\}$, is $p(0,0)=0.1$, $p(0,1)=0.2$,
$p(1,0)=0.3$, $p(1,1)=0.4$.

(a) Find the marginal mass functions.
(b) Compute $\Pr(Y=1\mid X=0)$.
(c) Are $X$ and $Y$ independent? Justify by a computation.
(d) Compute $\Pr(X=Y)$.

**12.** *(§7.8, §7.9)* Let $f_{X,Y}(x,y)=4xy$ on $[0,1]^2$.

(a) Verify that $f_{X,Y}$ is a joint density.
(b) Find the marginals $f_X$ and $f_Y$.
(c) Show that $X$ and $Y$ are independent.
(d) Compute $\Pr(X<Y)$.

## Intermediate

**13.** *(§7.4)* A random variable has

$$
F(x)=\begin{cases}0,&x<0,\\ \dfrac{x^2}{2},&0\le x<1,\\ 1,&x\ge1.\end{cases}
$$

(a) Verify that $F$ is a CDF.
(b) Find all atoms and the density part, and check that the masses sum to $1$.
(c) Compute $\Pr(0.5<X<1)$ and $\Pr(X=1)$.
(d) Find the median.

**14.** *(§7.5)* Let $X\sim\text{Exponential}(1)$.

(a) Find $Q(u)$.
(b) Compute $Q(1/4)$, $Q(1/2)$, $Q(3/4)$ and the interquartile range, exactly and numerically.
(c) Verify that $\Pr\bigl(X\le Q(1/4)\bigr)=1/4$.
(d) Find the value $x$ with $\Pr(X>x)=0.1$.

**15.** *(§7.6)* Let $X\sim\text{Uniform}(-2,2)$ and $Y=X^2$.

(a) Find the density of $Y$, stating the domain.
(b) Verify that it integrates to $1$.
(c) Compute $\Pr(Y\le1)$ in two ways.

**16.** *(§7.6)* Let $X\sim\text{Exponential}(1)$ and $Y=e^{-X}$.

(a) Find the CDF of $Y$ from the event $\{e^{-X}\le y\}$.
(b) Find the density of $Y$ and identify the distribution.
(c) Repeat (b) with the change-of-variable formula and check that the two agree.

**17.** *(§7.7)* Let $X$ be uniform on $(0,1)$ with probability $\tfrac12$ and uniform on $(2,3)$ with
probability $\tfrac12$.

(a) Write the density and sketch its shape.
(b) Compute $\mathbb{E}[X]$ and $\operatorname{Var}(X)$ using the mixture formulas.
(c) Compute $\mathbb{E}[X]$ and $\operatorname{Var}(X)$ from the density directly, and compare.
(d) Is the density bimodal? Explain.

**18.** *(§7.8)* Let $f_{X,Y}(x,y)=24xy$ for $x\ge0$, $y\ge0$, $x+y\le1$, and $0$ otherwise.

(a) Verify that $f_{X,Y}$ is a joint density.
(b) Find $f_X$ and $f_Y$.
(c) Find $f_{Y\mid X}(y\mid x)$ and identify the conditional law.
(d) Compute $\Pr\bigl(Y\le\tfrac14\mid X=\tfrac12\bigr)$.
(e) Are $X$ and $Y$ independent?

**19.** *(§7.8, §7.9)* Let $f_{X,Y}(x,y)=6xy^2$ on $[0,1]^2$.

(a) Verify normalisation and find the marginals.
(b) Show that $X$ and $Y$ are independent.
(c) Compute $\Pr(X<Y)$.
(d) Find $f_{X\mid Y}(x\mid y)$ and check that it integrates to $1$ for each $y$.

**20.** *(§7.5, §7.6)* Let $X$ have $F(x)=x^2$ for $0\le x\le1$ (and $0$, $1$ outside).

(a) Show directly that $F(X)\sim\text{Uniform}(0,1)$.
(b) Deduce the distribution of $X^2$ and reconcile it with (a).
(c) Find the density of $-\ln X$.
(d) Find the density of $X^2$ by the change-of-variable formula and compare with (b).

**21.** *(§7.6)* Let $X\sim\mathcal{N}(0,1)$ and $Y=e^{X}$ (the lognormal law).

(a) Derive the density of $Y$.
(b) Verify that it integrates to $1$ by the substitution $y=e^{x}$.
(c) Compute $\Pr(Y\le1)$ and $\Pr(1<Y<e)$ in terms of $\Phi$.
(d) Explain why $Y$ is not symmetric, although $X$ is.

**22.** *(§7.8)* Let $X,Y$ be independent uniform on $(0,1)$ and $Z=\max(X,Y)$.

(a) Compute $F_Z(z)$ for $0\le z\le1$ and hence the density.
(b) Compute $\Pr(Z>0.5)$.
(c) Find the median of $Z$.
(d) Find $\Pr\bigl(X\le z/2\mid Z=z\bigr)$ informally, and explain why conditioning on $Z=z$ is delicate.

## Advanced

**23.** *(§7.5)* Let $F$ be a CDF with quantile function $Q$.

(a) Prove that $Q(p)<x$ if and only if there exists $t<x$ with $F(t)\ge p$.
(b) Deduce that $Q(p)$ is the *smallest* $x$ with $F(x)\ge p$, so that the infimum in the definition is attained.
(c) Suppose $F$ is continuous and strictly increasing on an interval carrying all the mass. Show that
$Q(p)<x\iff p<F(x)$, and identify where the strict inequality comes from.
(d) Explain, with two different examples, why the plausible-looking identity $Q(p)<x\iff p\le F(x^{-})$ is false in
general: one example where $Q(p)<x$ holds although $p=F(x^{-})$, and one where $p=F(x^{-})$ holds although
$Q(p)=x$.

**24.** *(§7.3, §8.4)* Let $X\sim\text{Uniform}(0,1)$ with density $f\equiv1$ on $(0,1)$.

(a) Define $g(x)=f(x)+\mathbf{1}_{\mathbb{Q}}(x)$. Show that $g\ge0$ and that $\int_{\mathbb{R}}g=1$, so $g$ is
also a density of $X$.
(b) Show that $g$ is discontinuous at every point of $(0,1)$, that $g\ne f$ on a countable dense set, and that
$g$ takes only the values $1$ and $2$ there.
(c) Conclude that a density is determined only up to equality almost everywhere, and explain why the CDF is
nevertheless uniquely determined.
(d) Can two different *continuous* densities define the same distribution? Justify your answer.

**25.** *(§7.6, §8.5)* Let $X$ have density $f_X$ and let $Y=X^2$.

(a) Derive $f_Y(y)=\bigl[f_X(\sqrt y)+f_X(-\sqrt y)\bigr]/(2\sqrt y)$ for $y>0$ from the CDF, treating the cases
$y>0$ and $y\le0$ separately.
(b) Apply the formula to $X\sim\mathcal{N}(0,1)$ and obtain $f_Y(y)=e^{-y/2}/\sqrt{2\pi y}$ on $y>0$.
(c) Verify that this is a density using $\Gamma(\tfrac12)=\sqrt\pi$ and the substitution $y=2u$.
(d) Explain what goes wrong if one writes $f_Y(y)=f_X(\sqrt y)/(2\sqrt y)$.

**26.** *(§7.4, §8.3)* Let $F$ be a CDF with atom set $A=\{x:\Pr(X=x)>0\}$.

(a) Prove that $F$ is continuous at $x$ if and only if $x\notin A$.
(b) Prove that the jump function $F_d(x)=\sum_{a\in A,\,a\le x}\Pr(X=a)$ is nondecreasing and right-continuous,
that it is a step function with total mass $\Pr(X\in A)$, and that $A$ is countable.
(c) For the CDF of Exercise 13, compute $F_d$ and exhibit the decomposition of $F$ explicitly.
(d) Explain why a CDF can have infinitely many atoms but only countably many.

**27.** *(§7.9)* Let $X\perp\!\!\!\perp Y$ and let $g,h$ be Borel.

(a) Prove that $g(X)\perp\!\!\!\perp h(Y)$ from the definition of independence.
(b) Show that the converse fails: exhibit dependent $X,Y$ and Borel $g,h$ such that $g(X)\perp\!\!\!\perp h(Y)$.
(c) Show in your example that $g(X)$ and $h(Y)$ are degenerate, and explain why degenerate variables are
independent of everything.

**28.** *(§7.9)* Let $X$ be uniform on $\{0,1\}$ and, conditionally on $X$,
$$
Y=\begin{cases}+1\text{ or }-1\text{ with probability }\tfrac12\text{ each},&X=0,\\
+2\text{ or }-2\text{ with probability }\tfrac12\text{ each},&X=1.\end{cases}
$$

(a) Compute $\mathbb{E}[Y\mid X=0]$, $\mathbb{E}[Y\mid X=1]$ and $\mathbb{E}[Y]$.
(b) Compute $\operatorname{Cov}(X,Y)$ and conclude that $X$ and $Y$ are uncorrelated.
(c) Show that $X$ and $Y$ are not independent by comparing $\Pr(Y=1\mid X=0)$ with $\Pr(Y=1)$.
(d) Explain why this example cannot be replaced by one in which $Y$ takes only two values as well.

**29.** *(§7.8)* Let $f_{X,Y}$ be a joint density with $f_X(x)>0$ and $f_Y(y)>0$.

(a) Prove the continuous Bayes identity $f_{X\mid Y}(x\mid y)f_Y(y)=f_{Y\mid X}(y\mid x)f_X(x)$.
(b) For the density $f_{X,Y}=2$ on $0\le y\le x\le1$, compute $f_{X\mid Y}(x\mid y)$ and verify that it is a
density in $x$ for each $y\in(0,1)$.
(c) Compute $\Pr\bigl(X\le\tfrac34\mid Y=\tfrac12\bigr)$.
(d) Explain why the answer to (c) must exceed $\Pr\bigl(X\le\tfrac34\bigr)=\tfrac{9}{16}$.

**30.** *(§7.5, §8.7)* Let $X$ have CDF $F$.

(a) Prove that if $F$ has an atom at $x$, then $F(X)$ has an atom at $F(x)$, of mass at least $\Pr(X=x)$.
(b) Deduce that if $F(X)\sim\text{Uniform}(0,1)$ then $F$ is continuous.
(c) Prove the converse: if $F$ is continuous then $F(X)\sim\text{Uniform}(0,1)$. (Hint:
$\{F(X)\le u\}=\{X\le Q(u)\}$ and $F(Q(u))=u$.)
(d) Compute the law of $F(X)$ when $\Pr(X=0)=\Pr(X=1)=\tfrac12$ and confirm that it is not uniform.
(e) Give a continuous $F$, other than the identity CDF, for which $F(X)$ is uniform, and verify it.

## Challenge

**31.** *(§7.4)* The *Cantor distribution* is defined by the Cantor function $F$: on the middle third
$(\tfrac13,\tfrac23)$, $F=\tfrac12$; on the middle thirds of the two remaining intervals, $F=\tfrac14$ and
$\tfrac34$ respectively; continuing indefinitely and extending continuously gives a nondecreasing $F$ with
$F(0)=0$, $F(1)=1$.

(a) Show that $F$ is continuous and constant on each interval removed in the construction.
(b) Show that $F'=0$ at every point of the complement of the Cantor set, and hence almost everywhere.
(c) Show that $\Pr(X=x)=0$ for every $x$, so $F$ has no atoms.
(d) Show that $X$ has no density.
(e) Compute $\Pr\bigl(X\in[0,\tfrac13]\bigr)$, $\Pr\bigl(X\in[\tfrac13,\tfrac23]\bigr)$ and
$\Pr(X\in C)$ where $C$ is the Cantor set. Comment on the last value given that $C$ has length zero.

**32.** *(§7.7)* Let $f$ be the mixture of $\mathcal{N}(\mu_1,\sigma^2)$ and $\mathcal{N}(\mu_2,\sigma^2)$ with
weights $w_1,w_2>0$, $w_1+w_2=1$, and put $\Delta=\mu_2-\mu_1>0$ and $m=(\mu_1+\mu_2)/2$.

(a) Show that $f'(m)=\dfrac{w_2-w_1}{\sigma^{2}}\cdot\dfrac{\Delta}{2\sigma}\varphi\!\left(\dfrac{\Delta}{2\sigma}\right)$,
and deduce that $f'(m)=0$ when $w_1=w_2$.
(b) For $w_1=w_2=\tfrac12$, show that
$f''(m)=\dfrac{1}{\sigma^{3}}\left(\dfrac{\Delta^{2}}{4\sigma^{2}}-1\right)\varphi\!\left(\dfrac{\Delta}{2\sigma}\right)$.
(c) Deduce that $\Delta>2\sigma$ implies that $m$ is a strict local minimum of $f$.
(d) Show that $f'(\mu_1)>0$ and $f'(\mu_2)<0$, and conclude that $f$ has a local maximum in $(\mu_1,m)$ and
another in $(m,\mu_2)$: the mixture is bimodal.
(e) The converse is also true: for $\Delta\le2\sigma$ and equal weights the mixture is unimodal. Explain why this
direction is harder, and verify the threshold numerically for $\sigma=1$, $\Delta=2$ by evaluating $f''(m)$.

**33.** *(§9.9)* Let $X_1,X_2,X_3$ be independent uniform on $(0,1)$ and $Z=X_1+X_2+X_3$.

(a) Derive the density of $Z$ on each of the intervals $(0,1)$, $(1,2)$, $(2,3)$ by conditioning on $X_3$ and
using the triangular density of the sum of two uniforms.
(b) Verify that the three pieces agree at $z=1$ and $z=2$.
(c) Verify that the density integrates to $1$.
(d) Verify the symmetry $f_Z(z)=f_Z(3-z)$ and explain its origin.
(e) Compute $\Pr(Z\le1.5)$ without further integration, using symmetry.

**34.** *(§7.10)*

(a) Prove that if a density satisfies $f(x)\ge c>0$ for all $x$ in an interval of length $L$, then $cL\le1$.
(b) Deduce that a density cannot satisfy $f(x)\ge1$ on an interval of length greater than $1$.
(c) Give a density that is strictly greater than $1$ at every point of its support, and verify the bound in (a)
with equality.
(d) Give a density with $f(x)\le1$ everywhere that is not the uniform density, and one that is unbounded yet a
density.
(e) A student claims that $f(x)\le1$ for every density because "probabilities are at most $1$". Identify the two
errors.

**35.** *(§7.5, §8.7)* Let $F$ be a CDF with quantile function $Q=Q_F$, and let $U\sim\text{Uniform}(0,1)$.

(a) Prove that $\{Q(U)\le x\}=\{U\le F(x)\}$ for every $x$, taking care with the case $F(x)=0$ and $F(x)=1$.
(b) Deduce that $Q(U)$ has CDF $F$ even when $F$ has jumps.
(c) For $p_X(0)=0.2$, $p_X(1)=0.5$, $p_X(2)=0.3$, write $Q$ explicitly as a step function on $(0,1)$.
(d) For that $Q$, compute $\Pr\bigl(Q(U)=0\bigr)$, $\Pr\bigl(Q(U)=1\bigr)$ and $\Pr\bigl(Q(U)=2\bigr)$, and
compare with the masses.
(e) Explain why inverse transform sampling is exact, not approximate, for discrete laws.

**36.** *(§7.5)* For CDFs $F$ and $G$ with quantile functions $Q_F,Q_G$, write $F\succeq G$ when $F(x)\ge G(x)$ for
all $x$ (equivalently, $X$ is stochastically smaller than $Y$ when $X\sim F$, $Y\sim G$).

(a) Prove that $F\succeq G$ implies $Q_F(p)\le Q_G(p)$ for all $p\in(0,1)$.
(b) Prove the converse.
(c) Conclude that $F\succeq G$ if and only if $Q_F\le Q_G$ pointwise.
(d) Check the criterion on the exponential laws with rates $\lambda_1<\lambda_2$: which is stochastically smaller,
and does the quantile inequality hold?
