# Inverse Trigonometric Functions

> [Mathematics](../../README.md) › [Trigonometry](../README.md) · Level: Advanced · Prerequisites: [Trigonometric Functions](../01-trigonometric-functions/README.md), [The Unit Circle and Radian Measure](../02-unit-circle/README.md), [Trigonometric Identities](../03-trigonometric-identities/README.md), [Intermediate Algebra](../../03-algebra/04-intermediate-algebra/README.md) · Estimated time: 420 min

## 1. Introduction

Every operation in elementary arithmetic has an undo button: addition is undone by subtraction,
squaring by the square root. Trigonometry has none. The question "for which $\theta$ is
$\sin\theta=0.6$?" has infinitely many answers — an acute angle near $36.87^\circ$, its supplement
near $143.13^\circ$, and both of those plus or minus any number of full turns. That is not a defect
of the question; it is periodicity, and it is exactly what makes trigonometry the language of waves,
tides and alternating currents.

Undoing the sine is nevertheless possible if we agree to forget all but one answer. The **inverse
trigonometric functions** are that agreement made precise. Each one restricts the original function
to an interval of strict monotonicity and reads the restriction backwards. The resulting function has
a domain, a range, a graph and a derivative, and it returns a single angle for every admissible
value.

The chosen interval is called the **principal branch**, and the word matters. Sine is also strictly
increasing on $[3\pi/2,5\pi/2]$, so a consistent theory could be built there instead. The standard
choice is canonical because it is convenient: it contains $0$, it is symmetric about $0$, it makes
the arcsine odd, and it gives $\arcsin0=0$. The price is that the arcsine reports angles on the right
half of the circle, which is not always the angle a triangle problem needs.

Inverse trigonometric functions appear wherever an angle must be recovered from a ratio. A surveyor
turns two measured sides into an angle with an arctangent; a physicist adding a sine and a cosine of
the same frequency obtains a phase angle; a programmer drawing a vector uses `atan2(y,x)`; a
statistician's heavy-tailed Cauchy distribution has an arctangent as its cumulative function; and
every calculus student who writes $\int dx/(1+x^2)=\arctan x+C$ is integrating one. The arcsine
similarly undoes the substitution $x=\sin u$ in integrals containing $\sqrt{1-x^2}$.

The chapter rests on one idea: **cut the circle into a piece on which the height, width or slope
changes monotonically, and read the angle off it.** Section 5 makes the cut precise, Section 7
develops the consequences, and Sections 9 and 12 apply them. The companion topic
[Trigonometric Equations](../06-trigonometric-equations/README.md) adds the periods back.

## 2. Prerequisites

* **The six trigonometric functions**, their exact values at the special angles, and their signs by
  quadrant — [Trigonometric Functions](../01-trigonometric-functions/README.md).
* **The unit circle and radians**, including $\sin(\theta+2\pi)=\sin\theta$,
  $\cos(\theta+2\pi)=\cos\theta$ and $\tan(\theta+\pi)=\tan\theta$ —
  [The Unit Circle and Radian Measure](../02-unit-circle/README.md).
* **The elementary identities**: $\sin^2\theta+\cos^2\theta=1$, $1+\tan^2\theta=\sec^2\theta$, the
  sum formulas and the double-angle formulas —
  [Trigonometric Identities](../03-trigonometric-identities/README.md).
* **Injective functions and inverse functions**, including the horizontal-line test —
  [Functions](../../03-algebra/11-functions/README.md).
* **Interval notation** and the difference between open and closed endpoints —
  [Mathematical Notation](../../MATHEMATICAL_NOTATION.md).
* **Elementary algebra**, especially solving quadratics and using $\sqrt{t^2}=\lvert t\rvert$ —
  [Intermediate Algebra](../../03-algebra/04-intermediate-algebra/README.md).

Derivatives are quoted in Section 7.10 and used in Section 12.3, marked and proved in
[Calculus](../../07-calculus/README.md); the rest needs no calculus.

## 3. Learning Objectives

After working through this tutorial you will be able to:

1. Explain why $\sin$, $\cos$ and $\tan$ have no inverse on their natural domains, using periodicity
   and the horizontal-line test.
2. State the definitions of $\arcsin$, $\arccos$ and $\arctan$ with their principal ranges, and
   explain why each range is the conventional choice.
3. State each domain and range and sketch each graph, including the vertical tangents of the arcsine
   and arccosine and the horizontal asymptotes of the arctangent.
4. Evaluate the inverse functions exactly at the standard values.
5. Evaluate compositions such as $\sin(\arccos x)$ and $\tan(\arcsin x)$, with the correct sign and
   domain.
6. Decide when $\arcsin(\sin x)=x$, $\arccos(\cos x)=x$ or $\arctan(\tan x)=x$, and correct the value
   when it fails.
7. Quote the three derivatives with their domains and use them in differentiation and integration.
8. Prove and apply the arctangent addition formula, including the correction when $xy>1$.
9. Rewrite $a\sin\theta+b\cos\theta$ as a single sinusoid and interpret its phase angle.
10. Avoid the standard errors: $\sin^{-1}x$ as a reciprocal, forgotten principal ranges, and the
    addition formula used outside its hypotheses.

## 4. Intuition

**A staircase with repeating flights.** In a spiral staircase with a landing every turn, your height
repeats. If a friend says "you are three metres up", you cannot say where you are: there is such a
step on every flight. Choosing a principal branch is the instruction "on the second flight". It does
not change the staircase; it selects one flight as official.

**The horizontal-line test on the circle.** The line $y=0.6$ cuts the unit circle twice: once on the
right, at an angle near $36.87^\circ$, and once on the left, at the supplementary angle near
$143.13^\circ$. Allowing more turns cuts it again and again. The arcsine chooses the cut on the right
half, where the angle is between $-\pi/2$ and $\pi/2$. That is why $\arcsin0.6$ is acute and
$\arcsin(-0.6)$ is a negative fourth-quadrant angle.

**The arccosine is read from the top.** The line $x=0.6$ cuts the circle twice, and the conventional
branch keeps the upper cut, where the angle is in $[0,\pi]$. So $\arccos$ runs from $0$ at $x=1$
through $\pi/2$ at $x=0$ to $\pi$ at $x=-1$, decreasing as $x$ decreases.

**The arctangent is a slope meter.** A road rising $1$ metre per metre has slope $1$ and angle
$45^\circ$. A huge slope is nearly vertical. So $\arctan$ converts slope to angle, and its range
$(-\pi/2,\pi/2)$ is the set of directions a road can have without pointing backwards. A vertical wall
has no finite slope, which is why the endpoints are excluded.

**Why a convention is harmless.** "The" angle whose sine is $0.6$ is ambiguous, just as "the" square
root of $4$ is ambiguous until we agree that $\sqrt4=2$. In both cases the convention makes the
inverse continuous, matches the familiar positive answer, and is easy to remember. The standard
branch minimises correction terms: it makes $\arcsin$ and $\arctan$ odd and
$\arcsin x+\arccos x=\pi/2$ an identity rather than a case analysis.

**The name "arc".** On the unit circle the angle in radians equals the arc it cuts off, so "the angle
whose sine is $x$" is also "the arc whose sine is $x$" — hence $\arcsin$. The older notation
$\sin^{-1}$ says the same thing but collides with $\sin^2$ and with $1/\sin$; this repository writes
$\arcsin$ for the inverse.

## 5. Formal Definition

Angles are real numbers in radians. A function $f$ is **injective** (one-to-one) on $A$ when
$f(x_1)=f(x_2)$ with $x_1,x_2\in A$ forces $x_1=x_2$; only injective functions can be inverted.

**Definition 5.1 (Inverse function).** Let $f:A\to B$ be injective with image $f[A]$. The **inverse**
$f^{-1}:f[A]\to A$ is defined by

$$f^{-1}(y)=x \quad\Longleftrightarrow\quad f(x)=y.$$

Two cancellation laws follow: $f\bigl(f^{-1}(y)\bigr)=y$ for $y\in f[A]$, and
$f^{-1}\bigl(f(x)\bigr)=x$ for $x\in A$. The second holds *only* for $x$ in the restricted domain;
this asymmetry is the source of most errors in the subject.

**Definition 5.2 (Arcsine).** $\arcsin:[-1,1]\to[-\pi/2,\pi/2]$ is defined by

$$y=\arcsin x \quad\Longleftrightarrow\quad \sin y=x \ \text{ and }\ -\frac{\pi}{2}\le y\le\frac{\pi}{2}.$$

**Definition 5.3 (Arccosine).** $\arccos:[-1,1]\to[0,\pi]$ is defined by

$$y=\arccos x \quad\Longleftrightarrow\quad \cos y=x \ \text{ and }\ 0\le y\le\pi.$$

**Definition 5.4 (Arctangent).** $\arctan:\mathbb{R}\to(-\pi/2,\pi/2)$ is defined by

$$y=\arctan x \quad\Longleftrightarrow\quad \tan y=x \ \text{ and }\ -\frac{\pi}{2}<y<\frac{\pi}{2}.$$

These intervals are the **principal ranges**, and the inverse functions are the **principal
branches**.

**Proposition 5.5.** Each restricted function is a bijection onto its stated range: sine on
$[-\pi/2,\pi/2]$, cosine on $[0,\pi]$ and tangent on $(-\pi/2,\pi/2)$ are continuous and strictly
monotone, with images $[-1,1]$, $[-1,1]$ and $\mathbb{R}$ respectively.

*Proof.* For $-\pi/2\le\alpha<\beta\le\pi/2$, the sum-to-product identity gives
$\sin\beta-\sin\alpha=2\cos\frac{\alpha+\beta}{2}\sin\frac{\beta-\alpha}{2}>0$, since
$(\alpha+\beta)/2\in[0,\pi/2)$ and $(\beta-\alpha)/2\in(0,\pi/2]$. So sine is strictly increasing and
injective; being continuous with $\sin(\pm\pi/2)=\pm1$, it is surjective onto $[-1,1]$ by the
intermediate value theorem. For $0\le\alpha<\beta\le\pi$,
$\cos\alpha-\cos\beta=2\sin\frac{\alpha+\beta}{2}\sin\frac{\beta-\alpha}{2}>0$, so cosine is strictly
decreasing with image $[-1,1]$. Finally, on $(-\pi/2,\pi/2)$,

$$\tan\beta-\tan\alpha=\frac{\sin(\beta-\alpha)}{\cos\alpha\cos\beta}>0,$$

so tangent is strictly increasing; it is continuous and unbounded above and below as
$\theta\to\pm\pi/2$, hence surjective onto $\mathbb{R}$. $\blacksquare$

**Proposition 5.6 (Cancellation laws).**

$$\sin(\arcsin x)=x\ (x\in[-1,1]),\qquad \cos(\arccos x)=x\ (x\in[-1,1]),\qquad
\tan(\arctan x)=x\ (x\in\mathbb{R}),$$

and inversely,

$$\arcsin(\sin x)=x\ \left(x\in\left[-\frac{\pi}{2},\frac{\pi}{2}\right]\right),\quad
\arccos(\cos x)=x\ (x\in[0,\pi]),\quad
\arctan(\tan x)=x\ \left(x\in\left(-\frac{\pi}{2},\frac{\pi}{2}\right)\right).$$

*Proof.* Each is the equivalence of Definitions 5.2–5.4 read in one direction or the other, plus the
observation that the displayed interval is exactly the principal range. Outside it the inverse
returns a different angle with the same sine, cosine or tangent; Section 7.9 computes that angle.
$\blacksquare$

**Remark 5.7 (Why these intervals?).** Each range is a maximal interval of monotonicity, chosen so
that the inverse is as simple as possible.

* $[-\pi/2,\pi/2]$ is the longest interval containing $0$ on which sine is monotone, which makes
  $\arcsin$ odd and gives $\arcsin0=0$. A choice such as $[\pi/2,3\pi/2]$ would give $\arcsin0=\pi$.
* $[0,\pi]$ is the longest interval on which cosine is monotone, and it matches the possible range of
  a triangle angle — which is why $\arccos$ arises naturally in the cosine rule.
* $(-\pi/2,\pi/2)$ is the longest interval of monotonicity for tangent; the endpoints are excluded
  because tangent is undefined there.

No interval can be extended: sine repeats every $2\pi$ and satisfies
$\sin(\pi-\theta)=\sin\theta$, so it is not injective on any interval longer than $\pi$. $\blacksquare$

## 6. Mathematical Notation

| Symbol | Read as | Meaning |
|---|---|---|
| $\arcsin x$ | arcsine of $x$ | the unique $y\in[-\pi/2,\pi/2]$ with $\sin y=x$ |
| $\arccos x$ | arccosine of $x$ | the unique $y\in[0,\pi]$ with $\cos y=x$ |
| $\arctan x$ | arctangent of $x$ | the unique $y\in(-\pi/2,\pi/2)$ with $\tan y=x$ |
| $\sin^{-1}x$ | inverse sine of $x$ | the same function as $\arcsin x$; never $1/\sin x$ |
| $\arcsin(\sin x)$ | arcsine of sine of $x$ | the composite; equals $x$ only on the principal range |
| $f^{-1}$ | inverse of $f$ | the function of Definition 5.1, not the reciprocal |
| $[-1,1]$ | closed interval | both endpoints included: $-1\le x\le1$ |
| $(-\pi/2,\pi/2)$ | open interval | endpoints excluded |
| $\mathbb{R}$ | the real numbers | the domain of $\arctan$ |
| $n\in\mathbb{Z}$ | $n$ is an integer | used when adding periods |
| $\operatorname{atan2}(y,x)$ | two-argument arctangent | the angle of the point $(x,y)$, in $(-\pi,\pi]$ |

An inverse trigonometric function always outputs an **angle**, in radians unless a degree sign is
written. A calculator in degree mode returns $30$ where the mathematics expects $\pi/6$; the two
denote the same angle but cannot be mixed in one expression. Also, $\arcsin$ is a function, so it
cannot be distributed over sums: $\arcsin(a+b)\neq\arcsin a+\arcsin b$ in general.

## 7. Core Concepts

### 7.1 Why the Trigonometric Functions Have No Inverse

A function is invertible exactly when it never repeats a value. All three circular functions repeat
systematically:

$$\sin(\theta+2\pi)=\sin\theta,\quad \sin(\pi-\theta)=\sin\theta,\qquad
\cos(\theta+2\pi)=\cos\theta,\quad \cos(-\theta)=\cos\theta,\qquad
\tan(\theta+\pi)=\tan\theta.$$

So $\sin(\pi/6)=\sin(5\pi/6)=\tfrac12$ and $\tan(\pi/4)=\tan(5\pi/4)=1$: one output, infinitely many
inputs. Geometrically, every horizontal line $y=k$ with $-1\le k\le1$ cuts the sine curve infinitely
often, so the graph fails the horizontal-line test.

The failure cannot be repaired by notation. The relation "$\sin y=x$" is not a function: its graph is
the whole sine curve turned sideways. To obtain a function we must discard all but one solution for
each $x$, and the discard must be done by restricting the domain to a piece on which the function is
strictly monotone, otherwise the choice is still ambiguous.

### 7.2 Restricting the Domain: How a Branch Is Built

The recipe is the same in all three cases: choose an interval $I$ on which the function is strictly
monotone, keep only the part with domain $I$, and read that restriction backwards. Different
intervals give different **branches**: $[-\pi/2,\pi/2]$ gives the principal arcsine with
$\arcsin0=0$; $[\pi/2,3\pi/2]$ would give a branch with value $\pi$ at $0$. All are inverse functions
of suitable restrictions of sine, and all satisfy $\sin(\arcsin x)=x$; they differ only in which
angle they report. Only the first is called $\arcsin$.

Two facts make the principal choice work. The interval is **maximal**: any longer interval contains a
pair of points symmetric about $\pi/2$ (or separated by $\pi$) where sine repeats. And the inverse
**inherits geometry**: because $[-\pi/2,\pi/2]$ is symmetric and sine is odd, the arcsine is odd;
because $[0,\pi]$ is the range of a triangle angle, the arccosine is directly usable in the cosine
rule. The cost is that the inverse knows nothing about the discarded branches — Section 7.9 shows
the correction needed when an angle lies elsewhere.

### 7.3 The Arcsine

$\arcsin x$ is the angle in $[-\pi/2,\pi/2]$ whose sine is $x$.

* **Domain $[-1,1]$, range $[-\pi/2,\pi/2]$**, with $\arcsin1=\pi/2$ and $\arcsin(-1)=-\pi/2$.
* **Odd:** $\sin(\arcsin(-x))=-x=-\sin(\arcsin x)=\sin(-\arcsin x)$, and both angles lie in the
  principal range, where sine is injective. Hence $\arcsin(-x)=-\arcsin x$.
* **Increasing:** if $a<b$ then $\sin(\arcsin a)=a<b=\sin(\arcsin b)$, and sine is increasing on the
  principal interval, so $\arcsin a<\arcsin b$.

The graph runs from $(-1,-\pi/2)$ to $(1,\pi/2)$, with an inflection at the origin, concave down for
$x<0$ and concave up for $x>0$. It becomes vertical at $x=\pm1$: near the top or bottom of the
circle a tiny change in height produces a large change in angle.

### 7.4 The Arccosine

$\arccos x$ is the angle in $[0,\pi]$ whose cosine is $x$. Since cosine decreases from $1$ to $-1$
across that interval, the arccosine decreases from $\pi$ to $0$.

* **Domain $[-1,1]$, range $[0,\pi]$**, with $\arccos1=0$, $\arccos0=\pi/2$, $\arccos(-1)=\pi$.
* **Reflection law:** $\arccos(-x)=\pi-\arccos x$. *Proof:* if $y=\arccos x\in[0,\pi]$, then
  $\cos(\pi-y)=-x$ and $\pi-y\in[0,\pi]$, so uniqueness gives $\arccos(-x)=\pi-y$. $\blacksquare$
* **Complement law:** $\arcsin x+\arccos x=\pi/2$. *Proof:* with $y=\arcsin x\in[-\pi/2,\pi/2]$,
  $\cos(\pi/2-y)=\sin y=x$ and $\pi/2-y\in[0,\pi]$, so $\arccos x=\pi/2-y$. $\blacksquare$

The arccosine is neither odd nor even; its graph has a half-turn symmetry about $(0,\pi/2)$ and
vertical tangents at both endpoints.

### 7.5 The Arctangent

$\arctan x$ is the angle in $(-\pi/2,\pi/2)$ whose tangent is $x$; it converts slope into angle.

* **Domain $\mathbb{R}$, range $(-\pi/2,\pi/2)$.** The endpoints are excluded because tangent is
  undefined there.
* **Odd:** $\tan(-\arctan x)=-x$ with $-\arctan x$ in the principal range, so
  $\arctan(-x)=-\arctan x$.
* **Increasing**, with $\arctan0=0$, $\arctan1=\pi/4$, $\arctan(-1)=-\pi/4$.
* **Horizontal asymptotes** $y=\pm\pi/2$: approached, never attained.
* **Reciprocal law:** for $x>0$, $\arctan x+\arctan\frac1x=\frac{\pi}{2}$; for $x<0$ the sum is
  $-\frac{\pi}{2}$. *Proof:* for $x>0$ both angles lie in $(0,\pi/2)$, so the sum lies in $(0,\pi)$,
  and the tangent addition formula has denominator $1-x\cdot\frac1x=0$; the sum is therefore
  $\pi/2$. Oddness gives the negative case. $\blacksquare$

The graph passes through the origin with slope $1$, is concave down on $(0,\infty)$ and concave up on
$(-\infty,0)$, and flattens towards its asymptotes.

### 7.6 Graphs, Domains and Ranges

| Function | Domain | Range | Monotonicity | Symmetry | Behaviour at the ends |
|---|---|---|---|---|---|
| $\arcsin$ | $[-1,1]$ | $[-\pi/2,\pi/2]$ | strictly increasing | odd | vertical tangents at $x=\pm1$ |
| $\arccos$ | $[-1,1]$ | $[0,\pi]$ | strictly decreasing | $\arccos(-x)=\pi-\arccos x$ | vertical tangents at $x=\pm1$ |
| $\arctan$ | $\mathbb{R}$ | $(-\pi/2,\pi/2)$ | strictly increasing | odd | horizontal asymptotes $y=\pm\pi/2$ |

The shapes are fixed by three points and one bend: $\arcsin$ goes $(-1,-\pi/2)\to(0,0)\to(1,\pi/2)$
with an inflection at $0$; $\arccos$ goes $(-1,\pi)\to(0,\pi/2)\to(1,0)$ with an inflection at
$(0,\pi/2)$; $\arctan$ goes $(-\infty,-\pi/2)\to(0,0)\to(+\infty,\pi/2)$. Each graph is a different
arc of the unit circle read as a function of a coordinate — the arcsine reads the height on the right
semicircle, the arccosine reads the width on the upper semicircle, the arctangent reads the slope of
the radius. Section 10 tabulates the correspondence.

### 7.7 Exact Values

Ask "which angle in the principal range has this value?" rather than memorising.

| $x$ | $-1$ | $-\dfrac{\sqrt3}{2}$ | $-\dfrac{\sqrt2}{2}$ | $-\dfrac12$ | $0$ | $\dfrac12$ | $\dfrac{\sqrt2}{2}$ | $\dfrac{\sqrt3}{2}$ | $1$ |
|---|---|---|---|---|---|---|---|---|---|
| $\arcsin x$ | $-\dfrac{\pi}{2}$ | $-\dfrac{\pi}{3}$ | $-\dfrac{\pi}{4}$ | $-\dfrac{\pi}{6}$ | $0$ | $\dfrac{\pi}{6}$ | $\dfrac{\pi}{4}$ | $\dfrac{\pi}{3}$ | $\dfrac{\pi}{2}$ |
| $\arccos x$ | $\pi$ | $\dfrac{5\pi}{6}$ | $\dfrac{3\pi}{4}$ | $\dfrac{2\pi}{3}$ | $\dfrac{\pi}{2}$ | $\dfrac{\pi}{3}$ | $\dfrac{\pi}{4}$ | $\dfrac{\pi}{6}$ | $0$ |

| $x$ | $-\sqrt3$ | $-1$ | $-\dfrac{1}{\sqrt3}$ | $0$ | $\dfrac{1}{\sqrt3}$ | $1$ | $\sqrt3$ |
|---|---|---|---|---|---|---|---|
| $\arctan x$ | $-\dfrac{\pi}{3}$ | $-\dfrac{\pi}{4}$ | $-\dfrac{\pi}{6}$ | $0$ | $\dfrac{\pi}{6}$ | $\dfrac{\pi}{4}$ | $\dfrac{\pi}{3}$ |

Two checks catch most errors: the sign (an arccosine of a negative number is obtuse, while arcsine
and arctangent of a negative number are negative) and the range ($\lvert\arcsin x\rvert\le\pi/2$ and
$\arccos x\in[0,\pi]$).

### 7.8 Compositions of the Form $f\bigl(f^{-1}(x)\bigr)$

Here the inverse is applied first, so its output always lies in the principal range. The only care is
the sign of the square root.

Let $\theta=\arccos x\in[0,\pi]$, so $\cos\theta=x$. Then $\sin^2\theta=1-x^2$ and $\sin\theta\ge0$
on $[0,\pi]$, hence

$$\sin(\arccos x)=+\sqrt{1-x^2}\qquad(\lvert x\rvert\le1).$$

The plus sign is forced by the range of $\arccos$, not chosen for convenience. In the same way
$\cos(\arcsin x)=+\sqrt{1-x^2}$, because sine's principal range lies where cosine is non-negative.
Dividing gives

$$\tan(\arcsin x)=\frac{x}{\sqrt{1-x^2}}\ (\lvert x\rvert<1),\qquad
\tan(\arccos x)=\frac{\sqrt{1-x^2}}{x}\ (0<\lvert x\rvert\le1).$$

For the arctangent, $\tan\theta=x$ and $\cos\theta>0$ give
$\cos\theta=1/\sqrt{1+x^2}$, so

$$\sin(\arctan x)=\frac{x}{\sqrt{1+x^2}},\qquad
\cos(\arctan x)=\frac{1}{\sqrt{1+x^2}},\qquad
\sec(\arctan x)=\sqrt{1+x^2}.$$

**Right-triangle method.** For $0<x<1$, draw a right triangle with adjacent side $x$ and hypotenuse
$1$; the opposite side is $\sqrt{1-x^2}$ and every ratio can be read off. It is fast but assumes the
first quadrant, so when signs are in doubt use the algebraic derivation above.

### 7.9 Compositions of the Form $f^{-1}\bigl(f(x)\bigr)$

This direction is where errors live, because the inverse can only report a value in its principal
range. In the easy direction no correction is ever needed:

$$\sin(\arcsin x)=x\ (x\in[-1,1]),\qquad \cos(\arccos x)=x\ (x\in[-1,1]),\qquad
\tan(\arctan x)=x\ (x\in\mathbb{R}).$$

In the reverse direction, $\arcsin(\sin x)=x$ only when $x$ already lies in the principal range.
Otherwise the inverse returns the reflection of $x$ into that range:

$$\arcsin(\sin x)=
\begin{cases}
x, & -\dfrac{\pi}{2}\le x\le\dfrac{\pi}{2},\\[2mm]
\pi-x, & \dfrac{\pi}{2}\le x\le\dfrac{3\pi}{2},
\end{cases}$$

extended with period $2\pi$. The second line holds because $\pi-x\in[-\pi/2,\pi/2]$ and
$\sin(\pi-x)=\sin x$. Similarly

$$\arccos(\cos x)=
\begin{cases}
x, & 0\le x\le\pi,\\[2mm]
2\pi-x, & \pi\le x\le2\pi,
\end{cases}$$

extended with period $2\pi$; in particular $\arccos(\cos x)=\lvert x\rvert$ for
$\lvert x\rvert\le\pi$. Last, $\arctan(\tan x)=x$ only on $(-\pi/2,\pi/2)$; elsewhere it equals
$x-n\pi$, where $n$ brings the value into that interval. The arctangent version has period $\pi$, not
$2\pi$.

Three checks show the mechanism:

$$\arcsin\left(\sin\frac{5\pi}{6}\right)=\arcsin\frac12=\frac{\pi}{6},\qquad
\arccos\left(\cos\frac{7\pi}{5}\right)=2\pi-\frac{7\pi}{5}=\frac{3\pi}{5},\qquad
\arctan\left(\tan\frac{3\pi}{4}\right)=\frac{3\pi}{4}-\pi=-\frac{\pi}{4}.$$

On the circle, the point at angle $5\pi/6$ is the mirror image of the point at $\pi/6$ across the
$y$-axis, so both have the same height and the arcsine reports the representative on the right half.

The graphs are worth naming: $y=\arcsin(\sin x)$ is a **triangular wave** of period $2\pi$;
$y=\arccos(\cos x)$ is a shifted triangular wave; $y=\arctan(\tan x)$ is a **sawtooth** of period
$\pi$ with jumps at the odd multiples of $\pi/2$.

### 7.10 Derivatives

$$\frac{d}{dx}\arcsin x=\frac{1}{\sqrt{1-x^2}}\ (\lvert x\rvert<1),\qquad
\frac{d}{dx}\arccos x=-\frac{1}{\sqrt{1-x^2}}\ (\lvert x\rvert<1),\qquad
\frac{d}{dx}\arctan x=\frac{1}{1+x^2}\ (x\in\mathbb{R}).$$

These are proved in [Calculus](../../07-calculus/README.md); the derivations show where the domains
come from.

* *Arcsine:* with $y=\arcsin x$ and $\sin y=x$, implicit differentiation gives $\cos y\cdot y'=1$. On
  the principal interval $\cos y>0$, so $\cos y=\sqrt{1-x^2}$ and $y'=1/\sqrt{1-x^2}$.
* *Arctangent:* with $\tan y=x$, $\sec^2y\cdot y'=1$, and $\sec^2y=1+\tan^2y=1+x^2$, so
  $y'=1/(1+x^2)$.
* *Arccosine:* $\arccos x=\pi/2-\arcsin x$, so the derivative is $-1/\sqrt{1-x^2}$.

The domains are open because arcsine and arccosine have vertical tangents at $x=\pm1$; the
arctangent's derivative is defined everywhere and tends to $0$ at infinity.

Read backwards, the same statements are antiderivatives:

$$\int\frac{dx}{\sqrt{1-x^2}}=\arcsin x+C\ (\lvert x\rvert<1),\qquad
\int\frac{dx}{1+x^2}=\arctan x+C\ (x\in\mathbb{R}).$$

The first underlies the substitution $x=\sin\theta$, which turns $\sqrt{1-x^2}$ into $\cos\theta$; the
second underlies $x=\tan\theta$, which turns $1+x^2$ into $\sec^2\theta$.

### 7.11 The Arctangent Addition Formula

The tangent addition formula gives
$\tan(\alpha+\beta)=\dfrac{\tan\alpha+\tan\beta}{1-\tan\alpha\tan\beta}$, but applying $\arctan$ to
both sides is not automatic, because $\alpha+\beta$ may lie outside the principal range.

**Theorem 7.1.** Let $x,y\in\mathbb{R}$.

1. If $xy<1$, then $\arctan x+\arctan y=\arctan\dfrac{x+y}{1-xy}$.
2. If $xy=1$, then the sum is $\dfrac{\pi}{2}$ when $x>0$ and $-\dfrac{\pi}{2}$ when $x<0$.
3. If $xy>1$, then $x$ and $y$ have the same sign and
   $$\arctan x+\arctan y=\arctan\frac{x+y}{1-xy}+\begin{cases}\pi,&x>0,\\-\pi,&x<0.\end{cases}$$

*Proof.* Put $\alpha=\arctan x$ and $\beta=\arctan y$, so $\alpha+\beta\in(-\pi,\pi)$ and, when
$xy\ne1$, $\tan(\alpha+\beta)=\frac{x+y}{1-xy}$.

(1) If $x,y\ge0$, not both zero, then $\alpha+\beta\in[0,\pi)$ and
$\tan(\alpha+\beta)>0$ because numerator and denominator are positive; a positive tangent on
$[0,\pi)$ forces $\alpha+\beta\in[0,\pi/2)$. If $x,y\le0$, apply this to $-x,-y$ and use oddness. If
the signs differ, $\alpha$ and $\beta$ do too, so $\alpha+\beta\in(-\pi/2,\pi/2)$ at once. In every
case $\alpha+\beta$ lies in the principal range and equals the arctangent of its own tangent.

(2) Here $y=1/x$, and the reciprocal law of Section 7.5 applies; the fraction in case 1 has
denominator zero, so the case is genuinely separate.

(3) If $x,y>0$ and $xy>1$ then $\alpha+\beta>\pi/2$, so $\alpha+\beta-\pi\in(-\pi/2,0)$ and has the
same tangent; hence the sum equals the arctangent plus $\pi$. If $x,y<0$, apply the positive case to
$-x,-y$ and use oddness. $\blacksquare$

The formula improves on the tangent addition formula because it produces an angle, and because it
identifies exactly when the naive arctangent answer needs a full-turn correction. Examples 9.4 and
9.5 use both regimes.

### 7.12 The Other Three Inverse Functions

Secant, cosecant and cotangent have principal inverses with conventions that vary between texts:
$\operatorname{arccot}x=\frac{\pi}{2}-\arctan x$ with range $(0,\pi)$;
$\operatorname{arcsec}x=\arccos(1/x)$ with range $[0,\pi]\setminus\{\pi/2\}$ for $\lvert x\rvert\ge1$;
$\operatorname{arccsc}x=\arcsin(1/x)$ with range $[-\pi/2,\pi/2]\setminus\{0\}$. The arccotangent is
the dangerous one: some texts use $(-\pi/2,\pi/2]$, which changes it by $\pi$ on the negative axis.

## 8. Formulas and Properties

Every statement carries its hypotheses; a formula quoted without its domain is a wrong answer waiting
to happen.

### 8.1 Definitions and Principal Ranges

| Function | Domain | Range | Defining equivalence |
|---|---|---|---|
| $\arcsin x$ | $[-1,1]$ | $\left[-\dfrac{\pi}{2},\dfrac{\pi}{2}\right]$ | $\sin y=x$, $y$ in the range |
| $\arccos x$ | $[-1,1]$ | $[0,\pi]$ | $\cos y=x$, $y$ in the range |
| $\arctan x$ | $\mathbb{R}$ | $\left(-\dfrac{\pi}{2},\dfrac{\pi}{2}\right)$ | $\tan y=x$, $y$ in the range |

### 8.2 Symmetries and Complementarity

For all $x$ in the stated domains,

$$\arcsin(-x)=-\arcsin x\ (\lvert x\rvert\le1),\quad
\arccos(-x)=\pi-\arccos x\ (\lvert x\rvert\le1),\quad
\arctan(-x)=-\arctan x\ (x\in\mathbb{R}),$$

$$\arcsin x+\arccos x=\frac{\pi}{2},\qquad \arccos x=\frac{\pi}{2}-\arcsin x
\qquad(\lvert x\rvert\le1),$$

$$\arctan x+\arctan\frac1x=
\begin{cases}
\dfrac{\pi}{2}, & x>0,\\[2mm]
-\dfrac{\pi}{2}, & x<0.
\end{cases}$$

The reciprocal law excludes $x=0$, where $1/x$ is undefined, although $\arctan0$ itself is defined.

### 8.3 Compositions

All identities hold for every $x$ for which both sides are defined, with the non-negative square
root:

$$\sin(\arccos x)=\sqrt{1-x^2},\qquad \cos(\arcsin x)=\sqrt{1-x^2},\qquad
\tan(\arcsin x)=\frac{x}{\sqrt{1-x^2}}\ (\lvert x\rvert<1),$$

$$\tan(\arccos x)=\frac{\sqrt{1-x^2}}{x}\ (x\neq0),\qquad
\sin(\arctan x)=\frac{x}{\sqrt{1+x^2}},\qquad
\cos(\arctan x)=\frac{1}{\sqrt{1+x^2}},$$

$$\sin(2\arctan x)=\frac{2x}{1+x^2},\qquad \cos(2\arctan x)=\frac{1-x^2}{1+x^2},\qquad
\sin(2\arcsin x)=2x\sqrt{1-x^2}.$$

The signs are forced by the principal ranges (Section 7.8).

### 8.4 Calculus

For differentiable $u=u(x)$,

$$\frac{d}{dx}\arcsin u=\frac{u'}{\sqrt{1-u^2}},\qquad
\frac{d}{dx}\arccos u=-\frac{u'}{\sqrt{1-u^2}},\qquad
\frac{d}{dx}\arctan u=\frac{u'}{1+u^2}.$$

The first two require $\lvert u\rvert<1$; the third has no restriction beyond differentiability of
$u$. For $a>0$,

$$\int\frac{dx}{\sqrt{a^2-x^2}}=\arcsin\frac{x}{a}+C\ (\lvert x\rvert<a),\qquad
\int\frac{dx}{a^2+x^2}=\frac1a\arctan\frac{x}{a}+C\ (x\in\mathbb{R}).$$

### 8.5 The Arctangent Addition Formula

For $x,y\in\mathbb{R}$,

$$\arctan x+\arctan y=
\begin{cases}
\arctan\dfrac{x+y}{1-xy}, & xy<1,\\[3mm]
\dfrac{\pi}{2}\operatorname{sgn}(x), & xy=1,\\[3mm]
\arctan\dfrac{x+y}{1-xy}+\pi\operatorname{sgn}(x), & xy>1,
\end{cases}$$

with $\operatorname{sgn}(x)=1$ for $x>0$ and $-1$ for $x<0$. When $xy=1$, $x$ and $y$ have the same
sign. Two forms valid for *all* $x,y$ avoid the cases:

$$\sin(\arctan x+\arctan y)=\frac{x+y}{\sqrt{(1+x^2)(1+y^2)}},\qquad
\cos(\arctan x+\arctan y)=\frac{1-xy}{\sqrt{(1+x^2)(1+y^2)}}.$$

Both follow by expanding $\sin(\alpha+\beta)$ and $\cos(\alpha+\beta)$ with
$\sin\alpha=x/\sqrt{1+x^2}$ and $\cos\alpha=1/\sqrt{1+x^2}$.

## 9. Step-by-Step Examples

### Example 9.1: Reading the Principal Ranges

Evaluate (a) $\arcsin\left(-\dfrac{\sqrt3}{2}\right)$, (b) $\arccos\dfrac{\sqrt2}{2}$, and
(c) $\arctan(-\sqrt3)$.

**Strategy.** In each case, find the angle in the stated range with the given value. The sign gives
the quadrant; the range selects the representative.

(a) The reference angle for $\sqrt3/2$ is $\pi/3$, and sine is negative in the fourth quadrant of the
principal interval, so $\arcsin(-\sqrt3/2)=-\pi/3$.

(b) $\cos(\pi/4)=\sqrt2/2$ and $\pi/4\in[0,\pi]$, so $\arccos(\sqrt2/2)=\pi/4$.

(c) $\tan(\pi/3)=\sqrt3$ and $\tan(-\theta)=-\tan\theta$, so $\arctan(-\sqrt3)=-\pi/3$, which lies in
$(-\pi/2,\pi/2)$.

**Answer.** $-\dfrac{\pi}{3}$, $\dfrac{\pi}{4}$, $-\dfrac{\pi}{3}$.

**Check.** $\sin(-\pi/3)=-\sqrt3/2\approx-0.8660$, $\cos(\pi/4)\approx0.7071$,
$\tan(-\pi/3)\approx-1.7321$; each angle lies in its principal range.

### Example 9.2: A Composition with a Negative Cosine

Evaluate $\sin\left(\arccos\left(-\dfrac35\right)\right)$ and
$\tan\left(\arccos\left(-\dfrac35\right)\right)$.

**Strategy.** Name the angle, locate it from the range of the arccosine, then use the Pythagorean
identity with the sign fixed by that range.

Let $\theta=\arccos(-3/5)\in[0,\pi]$. Since $\cos\theta<0$, $\theta$ is in the second quadrant and
$\sin\theta>0$. Then

$$\sin^2\theta=1-\frac{9}{25}=\frac{16}{25}\ \Longrightarrow\ \sin\theta=\frac45,
\qquad \tan\theta=\frac{\sin\theta}{\cos\theta}=\frac{4/5}{-3/5}=-\frac43.$$

**Answer.** $\dfrac45$ and $-\dfrac43$.

**Check.** $\arccos(-0.6)\approx2.2143\in(\pi/2,\pi)$, and $\sin(2.2143)\approx0.8$,
$\tan(2.2143)\approx-1.3333$.

### Example 9.3: Simplifying a Double-Angle Composition

Simplify $\sin(2\arctan x)$ and evaluate it exactly at $x=3$.

**Strategy.** Put $\theta=\arctan x$, use the double-angle formula, and substitute the sine and cosine
found in Section 7.8.

With $\theta\in(-\pi/2,\pi/2)$, $\sin\theta=\dfrac{x}{\sqrt{1+x^2}}$ and
$\cos\theta=\dfrac{1}{\sqrt{1+x^2}}$. Hence

$$\sin2\theta=2\sin\theta\cos\theta
=\frac{2x}{1+x^2}.$$

At $x=3$ this is $\dfrac{6}{10}=\dfrac35$.

**Answer.** $\sin(2\arctan x)=\dfrac{2x}{1+x^2}$ for all $x$; at $x=3$, $\dfrac35$.

**Check.** $2\arctan3\approx2.4981$ lies in the second quadrant and $\sin(2.4981)\approx0.6$, as
predicted; the formula gives a positive value there.

### Example 9.4: Sum of Two Arctangents

Show that $\arctan\dfrac12+\arctan\dfrac13=\dfrac{\pi}{4}$.

**Strategy.** Compute the tangent of the sum and check that the sum lies where arctangent inverts
tangent.

Let $\alpha=\arctan\tfrac12$ and $\beta=\arctan\tfrac13$, both in $(0,\pi/2)$, so
$\alpha+\beta\in(0,\pi)$. Then

$$\tan(\alpha+\beta)=\frac{\tfrac12+\tfrac13}{1-\tfrac12\cdot\tfrac13}
=\frac{\tfrac56}{\tfrac56}=1.$$

A sum in $(0,\pi)$ with tangent $1$ must be $\pi/4$, since $5\pi/4$ is outside the interval.

**Answer.** The sum is $\dfrac{\pi}{4}$. Numerically, $0.4636+0.3218=0.7854=\pi/4$.

### Example 9.5: Solving an Arctangent Equation

Solve $\arctan(2x)+\arctan(3x)=\dfrac{\pi}{4}$ for real $x$.

**Strategy.** Apply the tangent to both sides, then check every candidate against the original
equation, because the tangent addition formula is not valid when $uv>1$.

Let $\alpha=\arctan(2x)$ and $\beta=\arctan(3x)$. Since tangent is injective on the principal range
and $\alpha+\beta=\pi/4$, the tangent addition formula with $u=2x$, $v=3x$ gives, when
$1-6x^2\neq0$,

$$\frac{5x}{1-6x^2}=1\quad\Longrightarrow\quad 6x^2+5x-1=0
\quad\Longrightarrow\quad(6x-1)(x+1)=0.$$

So $x=\tfrac16$ or $x=-1$.

* $x=\tfrac16$: $\arctan\tfrac13+\arctan\tfrac12=\pi/4$ by Example 9.4. Valid.
* $x=-1$: both arguments are negative and $uv=6>1$, so by Theorem 7.1 the sum is
  $\arctan\frac{-5}{-5}-\pi=\frac{\pi}{4}-\pi=-\frac{3\pi}{4}\neq\frac{\pi}{4}$. Rejected.

**Answer.** $x=\dfrac16$.

**Check.** $\arctan(1/3)+\arctan(1/2)\approx0.7854=\pi/4$; at $x=-1$ the sum is
$\approx-2.3562=-3\pi/4$.

### Example 9.6: Combining a Sine and a Cosine

Write $5\sin\theta-12\cos\theta$ as $R\sin(\theta+\varphi)$ with $R>0$, and state its maximum and
minimum.

**Strategy.** Expand $R\sin(\theta+\varphi)$ and match coefficients; the amplitude follows from
Pythagoras and the phase from an arctangent.

Since

$$R\sin(\theta+\varphi)=R\cos\varphi\,\sin\theta+R\sin\varphi\,\cos\theta,$$

matching requires $R\cos\varphi=5$ and $R\sin\varphi=-12$. Squaring and adding gives
$R^2=25+144=169$, so $R=13$. Then $\cos\varphi=\tfrac{5}{13}>0$ and
$\sin\varphi=-\tfrac{12}{13}<0$, so $\varphi$ is in the fourth quadrant:

$$\varphi=-\arctan\frac{12}{5}\approx-1.1760.$$

**Answer.** $5\sin\theta-12\cos\theta=13\sin\left(\theta-\arctan\dfrac{12}{5}\right)$, with maximum
$13$ and minimum $-13$.

**Check.** At $\theta=0$ the left side is $-12$ and the right side is
$13\sin(-1.1760)\approx-12.000$; at $\theta=\pi/2$ both equal $5$.

### Example 9.7: Calculus with Inverse Functions

Differentiate $f(x)=\arcsin(x^2)$ and evaluate $\displaystyle\int_0^2\frac{dx}{4+x^2}$.

**Strategy.** Chain rule with $u=x^2$ for the derivative; the arctangent antiderivative with $a=2$ for
the integral.

With $u=x^2$, $u'=2x$,

$$f'(x)=\frac{2x}{\sqrt{1-x^4}}\qquad(\lvert x\rvert<1).$$

For the integral, substitute $u=x/2$, $dx=2\,du$:

$$\int\frac{dx}{4+x^2}=\frac12\arctan\frac{x}{2}+C,$$

hence

$$\int_0^2\frac{dx}{4+x^2}=\frac12\left[\arctan\frac{x}{2}\right]_0^2
=\frac12\left(\frac{\pi}{4}-0\right)=\frac{\pi}{8}.$$

**Answer.** $f'(x)=\dfrac{2x}{\sqrt{1-x^4}}$ for $\lvert x\rvert<1$; the integral is
$\dfrac{\pi}{8}\approx0.3927$.

**Check.** The integrand lies between $1/8$ and $1/4$ on $[0,2]$, so the integral lies between $0.25$
and $0.5$; $\pi/8\approx0.3927$ does.

### Example 9.8: When the Inverse Does Not Return the Original Angle

Compute $\arccos\left(\cos\dfrac{7\pi}{5}\right)$ and
$\arctan\left(\tan\dfrac{5\pi}{6}\right)$, explaining each on the circle.

**Strategy.** Reflect the angle into the principal range, then read the inverse.

The angle $7\pi/5$ lies in the fourth quadrant, outside $[0,\pi]$. Reflection across the $x$-axis
gives $2\pi-7\pi/5=3\pi/5$, which has the same cosine and lies in $[0,\pi]$; so the first value is
$3\pi/5$.

The angle $5\pi/6$ lies in the second quadrant, outside $(-\pi/2,\pi/2)$. Tangent has period $\pi$,
and $5\pi/6-\pi=-\pi/6$ lies in the principal range with the same tangent; so the second value is
$-\pi/6$.

**Answer.** $\dfrac{3\pi}{5}$ and $-\dfrac{\pi}{6}$.

**Check.** $\cos(7\pi/5)=\cos(3\pi/5)\approx-0.3090$ and
$\tan(5\pi/6)=\tan(-\pi/6)\approx-0.5774$.

## 10. Visual Explanations

### 10.1 Choosing the Right Inverse

The decision is mechanical: a known sine calls for $\arcsin$ and an answer in $[-\pi/2,\pi/2]$; a
known cosine calls for $\arccos$ and an answer in $[0,\pi]$; a known tangent or slope calls for
$\arctan$ and an answer in $(-\pi/2,\pi/2)$; anything else is first converted to one of those three
by an identity. The resulting principal angle must then be checked against the geometry: a triangle,
a bearing or a phase may require the supplementary or opposite angle, which the inverse never knows.

### 10.2 Principal Representatives by Quadrant

Let $\alpha\in[0,\pi/2]$ be the reference angle of $\theta$. The table gives the value each inverse
reports for each quadrant, which is the content of Section 7.9 in tabular form.

| Location of $\theta$ | $\theta$ | $\arcsin(\sin\theta)$ | $\arccos(\cos\theta)$ | $\arctan(\tan\theta)$ |
|---|---|---|---|---|
| First quadrant | $\alpha$ | $\alpha$ | $\alpha$ | $\alpha$ |
| Second quadrant | $\pi-\alpha$ | $\alpha$ | $\pi-\alpha$ | $-\alpha$ |
| Third quadrant | $\pi+\alpha$ | $-\alpha$ | $\pi-\alpha$ | $\alpha$ |
| Fourth quadrant | $2\pi-\alpha$ | $-\alpha$ | $\alpha$ | $-\alpha$ |

Each column is the reflection of $\theta$ into the corresponding principal range. The first three
columns produce triangular waves; the last produces a sawtooth.

A sketch should show endpoint or limit values, monotonicity, concavity change and boundary behaviour;
Section 7.6 lists all four for each function.

## 11. Common Mistakes

**Mistake 1: reading $\sin^{-1}x$ as $1/\sin x$.** The superscript $-1$ on a function name means the
inverse; on a value it means a reciprocal. $\sin^{-1}(0.5)=\pi/6$, while
$(\sin0.5)^{-1}\approx2.086$.

**Mistake 2: assuming $\arcsin(\sin x)=x$ for all $x$.** At $x=5\pi/6$,
$\arcsin(\sin5\pi/6)=\arcsin(1/2)=\pi/6$. The identity holds exactly on $[-\pi/2,\pi/2]$. The
converse $\sin(\arcsin x)=x$ has no angle restriction but requires $x\in[-1,1]$.

**Mistake 3: writing $\arccos(-x)=-\arccos x$.** The arccosine is not odd. The correct law is
$\arccos(-x)=\pi-\arccos x$; at $x=1$, $\arccos(-1)=\pi$ while $-\arccos1=0$.

**Mistake 4: taking a negative square root in a composition.** Since $\arccos x\in[0,\pi]$, its sine
is non-negative, so $\sin(\arccos x)=+\sqrt{1-x^2}$ with no $\pm$.

**Mistake 5: applying $\arcsin x+\arccos y=\pi/2$ to different arguments.** The identity needs the
same $x$ in both places. With $x=0$, $y=1$ the sum is $0$, not $\pi/2$.

**Mistake 6: using the arctangent addition formula without its hypothesis.** Writing
$\arctan2+\arctan3=\arctan\frac{5}{-5}=-\pi/4$ is wrong; $xy=6>1$ and the correct value is
$3\pi/4$.

**Mistake 7: forgetting the $+n\pi$ when solving $\tan\theta=k$.** The arctangent gives one angle;
tangent repeats every $\pi$, so all solutions are $\arctan k+n\pi$.

**Mistake 8: mixing degrees and radians.** An inverse function returns an angle that may be written
$\pi/6$ or $30^\circ$, but adding a radian value to a degree value is meaningless. Convert first.

**Mistake 9: assuming $2\arctan x=\arctan2x$.** The correct doubling formula is
$2\arctan x=\arctan\dfrac{2x}{1-x^2}$ when $\lvert x\rvert<1$, with a $\pm\pi$ correction outside.
At $x=1$ the left side is $\pi/2$ but $\arctan2\approx1.107$.

**Mistake 10: omitting the chain rule or the domain in a derivative.** The derivative of
$\arcsin(x^2)$ is $\dfrac{2x}{\sqrt{1-x^4}}$ on $\lvert x\rvert<1$, not
$\dfrac{1}{\sqrt{1-x^4}}$ on all $x$.

**Mistake 11: quoting a derivative or a value outside its range.**
$\frac{d}{dx}\arcsin x=1/\sqrt{1-x^2}$ requires $\lvert x\rvert<1$, and $\arctan x=\pi/2$ has no real
solution: the finite-looking symbol $x=\tan(\pi/2)$ hides an infinite quantity.

## 12. Applications

### 12.1 Phase Angles and Combining Sinusoids

Any sum of a sine and a cosine of the same frequency is a single sinusoid:

$$a\sin\theta+b\cos\theta=R\sin(\theta+\varphi),\qquad R=\sqrt{a^2+b^2},\qquad
\varphi=\operatorname{atan2}(b,a).$$

The amplitude is $R$ and the phase is $\varphi$. This amplitude–phase form is the standard language of
alternating-current circuits, where out-of-phase voltages combine by phasor addition, and of forced
oscillations, where the response is a sinusoid of computable amplitude and phase.

### 12.2 Solving Triangles and Surveying

In a right triangle with legs $a$ and $b$, the angle opposite $a$ is $\arctan(a/b)$. This is the
oldest use of an inverse trigonometric function: a surveyor measures two sides and reads an angle
from a table of arctangents. In a general triangle the cosine rule gives

$$A=\arccos\frac{b^2+c^2-a^2}{2bc},$$

and here the range $[0,\pi]$ of the arccosine is exactly right, because a triangle angle may be
obtuse. The sine rule instead produces $\arcsin$, whose range $[-\pi/2,\pi/2]$ cannot describe an
obtuse angle; the missing possibility $A\leftrightarrow\pi-A$ is the **ambiguous case** treated in
[Triangle Trigonometry](../05-triangle-trigonometry/README.md).

### 12.3 Calculus: Substitution and Antiderivatives

The inverse functions are antiderivatives of algebraic expressions, which is how they enter
integration:

$$\int\frac{dx}{\sqrt{1-x^2}}=\arcsin x+C,\qquad
\int\frac{dx}{1+x^2}=\arctan x+C,\qquad
\int\frac{dx}{x\sqrt{x^2-1}}=\operatorname{arcsec}\lvert x\rvert+C.$$

They also drive the standard substitutions. For $\sqrt{a^2-x^2}$ put $x=a\sin\theta$; the radical
becomes $a\cos\theta$ because $\theta=\arcsin(x/a)\in[-\pi/2,\pi/2]$, where cosine is non-negative.
For $a^2+x^2$ put $x=a\tan\theta$; then $a^2+x^2=a^2\sec^2\theta$. The inverse function converts the
answer back from $\theta$ to $x$. See
[Techniques of Integration](../../07-calculus/08-techniques-of-integration/README.md).

### 12.4 Computer Graphics, Robotics and `atan2`

A program needing the direction of $(x,y)$ cannot use $\arctan(y/x)$ alone, because the quotient
loses the signs and $(1,1)$ and $(-1,-1)$ would share an angle. The two-argument
$\operatorname{atan2}(y,x)$ inspects the signs and returns an angle in $(-\pi,\pi]$. For example
$\operatorname{atan2}(-1,-1)=-3\pi/4$, while $\arctan\bigl((-1)/(-1)\bigr)=\pi/4$. Robot arms and
three-dimensional rotation code use the same idea.

## 13. Exercises

The problem set is in [exercises.md](exercises.md): 36 problems, graded from direct evaluation
through composition and simplification to proofs of addition formulas and classical identities. Every
problem is solvable from this tutorial; challenge problems are marked.

Attempt the problems before opening [solutions.md](solutions.md). Reading a solution is not the same
as being able to produce one.

## 14. Solutions

Full worked solutions, including strategy and every algebraic step, are in
[solutions.md](solutions.md). Each states the relevant domain, checks the answer on the unit circle,
and gives a decimal approximation as an independent check.

## 15. Summary

* The trigonometric functions are periodic and therefore not injective; restricting to an interval of
  strict monotonicity produces a **branch**.
* **Principal branches:**
  $$y=\arcsin x\iff \sin y=x,\ y\in\left[-\frac{\pi}{2},\frac{\pi}{2}\right];\quad
  y=\arccos x\iff \cos y=x,\ y\in[0,\pi];\quad
  y=\arctan x\iff \tan y=x,\ y\in\left(-\frac{\pi}{2},\frac{\pi}{2}\right).$$
* **Domains and ranges:** $\arcsin$ and $\arccos$ have domain $[-1,1]$ and ranges
  $[-\pi/2,\pi/2]$ and $[0,\pi]$; $\arctan$ has domain $\mathbb{R}$ and range $(-\pi/2,\pi/2)$.
* **Symmetries and compositions:** $\arcsin$ and $\arctan$ are odd, $\arccos(-x)=\pi-\arccos x$,
  $\arcsin x+\arccos x=\pi/2$, $\sin(\arccos x)=\sqrt{1-x^2}$, $\cos(\arcsin x)=\sqrt{1-x^2}$,
  $\sin(\arctan x)=x/\sqrt{1+x^2}$ and $\cos(\arctan x)=1/\sqrt{1+x^2}$.
* **Conditional identities:** $\arcsin(\sin x)=x$ only on $[-\pi/2,\pi/2]$;
  $\arccos(\cos x)=x$ only on $[0,\pi]$ (and $\arccos(\cos x)=\lvert x\rvert$ for
  $\lvert x\rvert\le\pi$); $\arctan(\tan x)=x$ only on $(-\pi/2,\pi/2)$.
* **Calculus:** $(\arcsin x)'=1/\sqrt{1-x^2}$, $(\arccos x)'=-1/\sqrt{1-x^2}$ and
  $(\arctan x)'=1/(1+x^2)$, with the stated domains.
* **Addition and phase form:** $\arctan x+\arctan y=\arctan\frac{x+y}{1-xy}$ when $xy<1$, with a
  correction by $\pm\pi$ when $xy>1$; $a\sin\theta+b\cos\theta=\sqrt{a^2+b^2}\,\sin(\theta+\varphi)$
  with $\varphi=\operatorname{atan2}(b,a)$.
* Every error in the subject comes from forgetting **which angle** the inverse was defined to return.

## 16. Further Learning

* [Trigonometric Functions](../01-trigonometric-functions/README.md) — the ratios and special values
  behind Section 7.7.
* [The Unit Circle and Radian Measure](../02-unit-circle/README.md) — periodicity and graphs.
* [Trigonometric Identities](../03-trigonometric-identities/README.md) — the formulas used in every
  derivation here.
* [Trigonometric Equations](../06-trigonometric-equations/README.md) — recovering all angles from one
  principal value.
* [Triangle Trigonometry](../05-triangle-trigonometry/README.md) — the sine and cosine rules in
  practice.
* [Functions](../../03-algebra/11-functions/README.md) — injectivity and inverse functions.
* [Calculus](../../07-calculus/README.md) — derivatives and integrals of the inverse functions.
* [Complex Analysis](../../15-complex-analysis/README.md) — multi-valued complex inverses and branch
  cuts.
* [Trigonometry](../README.md) — the discipline index and study order.

Standard references at this level are I. M. Gelfand and M. Saul, *Trigonometry*, Chapters 5–6;
S. L. Loney, *Plane Trigonometry*, Part I; and J. Stewart, L. Redlin and S. Watson, *Precalculus*.
For the two-argument arctangent and its numerical behaviour, any text on computer graphics or robotics
will do.
