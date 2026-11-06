# Applications of Integration — Solutions

> [Applications of Integration](README.md) · Solutions to the 36 problems in [exercises.md](exercises.md)

Each solution states the set-up — variable, element, limits — before integrating, and checks the answer
by differentiating, by an independent method, or by a special case. Pitfalls are flagged where the problem
is designed to expose them.

## Beginner

### Solution 1

*Set-up.* Solve $x^2=2x$: $x(x-2)=0$, so $x=0$ and $x=2$. On $(0,2)$, $2x-x^2=x(2-x)>0$, so the line is
the top curve. With vertical strips,

$$A=\int_0^2(2x-x^2)\,dx=\left[x^2-\frac{x^3}{3}\right]_0^2=4-\frac83=\frac43 .$$

*Check.* The area under $y=2x$ is a triangle of base $2$ and height $4$, area $4$; the area under
$y=x^2$ is $\int_0^2x^2dx=8/3$. Their difference is $4-8/3=4/3$, in agreement.

### Solution 2

*Set-up.* The curves $y=e^x$ and $y=1$ meet at $x=0$. On $[0,\ln3]$, $e^x\ge1$. Hence

$$A=\int_0^{\ln3}(e^x-1)\,dx=\left[e^x-x\right]_0^{\ln3}=(3-\ln3)-(1-0)=2-\ln3 .$$

*Check.* Since $\ln3\approx1.0986$, $A\approx0.9014$, positive and less than the rectangle
$(\ln3)(3-1)\approx2.197$ that contains it.

### Solution 3

*Set-up.* A vertical slice at $x$ is a disk of radius $2x$, so $A(x)=\pi(2x)^2=4\pi x^2$ and

$$V=\int_0^3 4\pi x^2\,dx=4\pi\left[\frac{x^3}{3}\right]_0^3=36\pi .$$

*Check.* The solid is a cone of radius $6$ and height $3$:
$V=\frac13\pi(6)^2(3)=36\pi$, in agreement.

### Solution 4

*Set-up (shells).* The region is $0\le y\le x$, $0\le x\le2$. The shell at $x$ has radius $x$ and height
$x$, so

$$V=2\pi\int_0^2 x\cdot x\,dx=2\pi\left[\frac{x^3}{3}\right]_0^2=\frac{16\pi}{3}.$$

*Check (washers).* Describe the region as $y\le x\le2$, $0\le y\le2$. The washer at height $y$ has outer
radius $2$ and inner radius $y$:

$$V=\pi\int_0^2(4-y^2)\,dy=\pi\left[4y-\frac{y^3}{3}\right]_0^2
=\pi\left(8-\frac83\right)=\frac{16\pi}{3},$$

in agreement.

### Solution 5

*Set-up.* The average is

$$\bar f=\frac{1}{3-0}\int_0^3x^2\,dx=\frac13\cdot\frac{27}{3}=3 .$$

Solve $f(c)=\bar f$: $c^2=3$, so $c=\sqrt3$ or $c=-\sqrt3$. Only $c=\sqrt3\in[0,3]$ is admissible.

*Check.* $\sqrt3\approx1.732$ lies in the interval, and the Mean Value Theorem for integrals guarantees at
least one such $c$ because $f$ is continuous.

### Solution 6

*Set-up.* Write $f(x)=\frac12(e^x+e^{-x})=\cosh x$. Then $f'(x)=\sinh x$ and
$1+f'(x)^2=1+\sinh^2x=\cosh^2x$. Since $\cosh x>0$, $\sqrt{1+f'^2}=\cosh x$, so

$$L=\int_0^1\cosh x\,dx=\sinh 1=\frac{e-e^{-1}}{2}\approx1.1752 .$$

*Check.* The chord from $(0,1)$ to $(1,\cosh1)$ has length
$\sqrt{1+(\cosh1-1)^2}$. Since $\cosh1\approx1.5431$, the chord is
$\sqrt{1+0.5431^2}\approx1.138$, which is less than the arc length $1.175$, as it must be. ✓

### Solution 7

*Set-up.* Hooke's law gives $F(x)=50x$, so

$$W=\int_0^{0.2}50x\,dx=25x^2\Big|_0^{0.2}=25(0.04)=1\ \mathrm{J}.$$

*Check.* Doubling the stretch to $0.4$ m would cost $25(0.16)=4$ J, four times as much, as the quadratic
formula predicts.

### Solution 8

*Set-up.* Measure depth $h$ from the surface, $0\le h\le3$. The width is constant, $w(h)=2$, so

$$F=\rho g\int_0^32h\,dh=\rho g\left[h^2\right]_0^3=9\rho g=9(9800)=88{,}200\ \mathrm{N}.$$

*Check by the centroid shortcut.* The area is $6\ \mathrm{m^2}$ and the centroid is at depth $1.5$ m, so
$F=\rho g(6)(1.5)=9\rho g$, in agreement.

### Solution 9

*Set-up.* Here $f(x)=b$ and $g(x)=0$ on $[0,a]$, so $A=ab$. Then

$$\bar x=\frac1{ab}\int_0^a xb\,dx=\frac{1}{ab}\cdot\frac{a^2b}{2}=\frac a2,$$

$$\bar y=\frac{1}{2ab}\int_0^a b^2\,dx=\frac{1}{2ab}\cdot ab^2=\frac b2.$$

*Check.* The centroid of a rectangle is at the intersection of its diagonals, $(\frac a2,\frac b2)$, as
expected.

### Solution 10

*Normalization.* $\displaystyle\int_0^13x^2dx=\left[x^3\right]_0^1=1$, so $f$ is a density.

*Probability.* $\displaystyle\Pr\left(X\le\frac12\right)=\int_0^{1/2}3x^2dx =\left[x^3\right]_0^{1/2}=\frac18 .$

*Mean.* $\displaystyle\mathbb{E}[X]=\int_0^13x^3dx=\left[\frac{3x^4}{4}\right]_0^1=\frac34 .$

*Check.* Since $f$ increases with $x$, the mean should exceed the midpoint $1/2$; $\frac34>\frac12$. ✓

### Solution 11

*Set-up.* The consumer surplus is the area between the demand curve and the price line:

$$CS=\int_0^{10}(50-2q)\,dq-10\cdot30
=\left[50q-q^2\right]_0^{10}-300=500-100-300=100 .$$

*Check.* The demand curve is a straight line from $(0,50)$ to $(10,30)$; the surplus is a triangle of base
$10$ and height $20$, area $100$, in agreement.

### Solution 12

*Set-up.* Here $f(x)=R$ is constant, so $f'(x)=0$ and $ds=dx$. The surface is a cylinder of radius $R$,
and

$$S=2\pi\int_0^hR\,dx=2\pi Rh .$$

*Check.* Unrolling the cylinder gives a rectangle of width $2\pi R$ and height $h$, area $2\pi Rh$, in
agreement.

## Intermediate

### Solution 13

*Set-up.* The curves meet where $x^3=x$, that is $x(x-1)(x+1)=0$, so at $x=-1,0,1$. On $(-1,0)$, $x^3>x$;
on $(0,1)$, $x>x^3$. Geometric area:

$$A=\int_{-1}^0(x^3-x)\,dx+\int_0^1(x-x^3)\,dx .$$

Compute

$$\int_{-1}^0(x^3-x)\,dx=\left[\frac{x^4}{4}-\frac{x^2}{2}\right]_{-1}^0
=0-\left(\frac14-\frac12\right)=\frac14,$$

and similarly $\int_0^1(x-x^3)dx=\frac12-\frac14=\frac14$. Hence $A=\frac12$.

*Why not one integral?* The integrand $x-x^3$ changes sign at $0$. Its integral over $[-1,1]$ is $0$ by odd
symmetry, which is the **net signed area**, not the geometric area. Splitting at the crossing is
mandatory.

### Solution 14

*Set-up.* At position $x\in[-2,2]$, the base has $y=\pm\sqrt{4-x^2}$, so the side of the square is
$s(x)=2\sqrt{4-x^2}$. Its area is $A(x)=s(x)^2=4(4-x^2)$. Therefore

$$V=\int_{-2}^2 4(4-x^2)\,dx=4\left[4x-\frac{x^3}{3}\right]_{-2}^2
=4\left[\left(8-\frac83\right)-\left(-8+\frac83\right)\right]=4\cdot\frac{32}{3}=\frac{128}{3}.$$

*Check.* The solid lies inside the cylinder over the disk of radius $2$ and height $4$, whose volume is
$16\pi\approx50.27$, and it contains the square prism over the square inscribed in the disk (side
$2\sqrt2$) with height $4$, volume $(2\sqrt2)^2\cdot4=32$. The value $128/3\approx42.67$ lies between $32$
and $50.27$, as it must. ✓

### Solution 15

*Set-up.* The curves meet where $\sqrt x=x$, that is $x=x^2$, so $x=0$ or $x=1$. On $(0,1)$,
$\sqrt x\ge x$. The washer at $x$ has outer radius $\sqrt x$ and inner radius $x$:

$$V=\pi\int_0^1\left(x-x^2\right)dx
=\pi\left(\frac12-\frac13\right)=\frac{\pi}{6}.$$

*Check by shells.* For $0\le y\le1$, the region is $y^2\le x\le y$ (since $y=\sqrt x$ gives $x=y^2$ and
$y=x$ gives $x=y$). The shell at height $y$ has radius $y$ and height $y-y^2$:

$$V=2\pi\int_0^1y\left(y-y^2\right)dy
=2\pi\left(\frac13-\frac14\right)=\frac{\pi}{6},$$

in agreement. ✓

### Solution 16

*Set-up.* The shell at $x\in[0,1]$ has radius $x$ and height $x^2$, so

$$V=2\pi\int_0^1x\cdot x^2\,dx=2\pi\left[\frac{x^4}{4}\right]_0^1=\frac{\pi}{2}.$$

*Check by washers.* For $0\le y\le1$, the region is $\sqrt y\le x\le1$; the washer at height $y$ has outer
radius $1$ and inner radius $\sqrt y$:

$$V=\pi\int_0^1(1-y)\,dy=\pi\left[y-\frac{y^2}{2}\right]_0^1=\frac{\pi}{2},$$

in agreement.

### Solution 17

*Set-up.* Differentiate $y=\ln(\sec x)$:
$y'=\frac{1}{\sec x}\cdot\sec x\tan x=\tan x$. Then
$1+y'^2=1+\tan^2x=\sec^2x$, and $\sec x>0$ on $[0,\pi/4]$, so $ds=\sec x\,dx$. Hence

$$L=\int_0^{\pi/4}\sec x\,dx
=\left[\ln\lvert\sec x+\tan x\rvert\right]_0^{\pi/4}
=\ln\left(\sqrt2+1\right)-\ln1=\ln\left(1+\sqrt2\right).$$

*Check.* $\ln(1+\sqrt2)\approx0.8814$, slightly more than the chord from $(0,0)$ to
$(\pi/4,\ln\sqrt2)\approx(0.7854,0.3466)$, whose length is
$\sqrt{0.6169+0.1201}\approx0.8579$. ✓

### Solution 18

*Set-up.* $f(x)=\sqrt x$, so $f'(x)=\frac{1}{2\sqrt x}$ and

$$1+f'(x)^2=1+\frac{1}{4x}=\frac{4x+1}{4x}.$$

Hence $ds=\frac{\sqrt{4x+1}}{2\sqrt x}\,dx$ and $2\pi f\,ds =2\pi\sqrt x\cdot\frac{\sqrt{4x+1}}{2\sqrt x}\,dx=\pi\sqrt{4x+1}\,dx$. Therefore

$$S=\pi\int_0^4\sqrt{4x+1}\,dx
=\pi\cdot\frac14\cdot\frac23\left[(4x+1)^{3/2}\right]_0^4
=\frac{\pi}{6}\left(17^{3/2}-1\right)=\frac{\pi}{6}\left(17\sqrt{17}-1\right).$$

*Check by differentiation.*
$\frac{d}{dx}\frac{\pi}{6}(4x+1)^{3/2} =\frac{\pi}{6}\cdot\frac32(4x+1)^{1/2}\cdot4=\pi\sqrt{4x+1}$, which is the integrand. ✓

### Solution 19

*Set-up.* Measure height $y$ from the bottom. The horizontal cross-section has area $2\cdot3=6\ \mathrm{m^2}$,
constant. The slice at height $y$ has volume $6\,dy$, weight $6\gamma\,dy$, and is lifted $4-y$ metres.
Thus

$$W=\gamma\int_0^46(4-y)\,dy
=6\gamma\left[4y-\frac{y^2}{2}\right]_0^4
=6\gamma(16-8)=48\gamma .$$

With $\gamma=9800$, $W=470{,}400$ J.

*Check by centre of mass.* The volume is $24\ \mathrm{m^3}$, the mass is $24{,}000$ kg, and the centroid
is at height $2$ m; the average lift is $4-2=2$ m. Hence
$W=24{,}000(9.8)(2)=470{,}400$ J, in agreement. ✓

### Solution 20

*Set-up.* The area is

$$A=\int_0^4\sqrt x\,dx=\left[\frac23x^{3/2}\right]_0^4=\frac{16}{3}.$$

The moments are

$$M_y=\int_0^4x\sqrt x\,dx=\int_0^4x^{3/2}dx
=\left[\frac25x^{5/2}\right]_0^4=\frac{64}{5},$$

$$M_x=\frac12\int_0^4(\sqrt x)^2dx=\frac12\int_0^4x\,dx=4 .$$

Therefore

$$\bar x=\frac{M_y}{A}=\frac{64/5}{16/3}=\frac{12}{5},\qquad
\bar y=\frac{M_x}{A}=\frac{4}{16/3}=\frac34 .$$

*Check.* $\bar x=2.4$ is left of the midpoint $2$ of $[0,4]$? No: $2.4>2$, and the region is thicker at
larger $x$ because $\sqrt x$ increases, so the centroid should be to the right of $2$. ✓ Also
$\bar y=0.75$ is below half the maximum height $2$, as expected.

### Solution 21

*Set-up.* Measure depth $h$ from the surface. The top of the plate is at $h=2$ and the bottom at $h=5$.
The width is $w(h)=4$, so

$$F=\rho g\int_2^54h\,dh
=4\rho g\left[\frac{h^2}{2}\right]_2^5
=2\rho g(25-4)=42\rho g=42(9800)=411{,}600\ \mathrm{N}.$$

*Check by the centroid shortcut.* The area is $12\ \mathrm{m^2}$ and the centroid is at depth $3.5$ m, so
$F=\rho g(12)(3.5)=42\rho g$, in agreement.

### Solution 22

*Equilibrium.* Set $30-q^2=6+\frac12q^2$: $24=\frac32q^2$, so $q^2=16$, $q^*=4$, and
$p^*=30-16=14$ (also $S(4)=6+8=14$).

*Consumer surplus.*

$$CS=\int_0^4(30-q^2)\,dq-4\cdot14
=\left[30q-\frac{q^3}{3}\right]_0^4-56
=120-\frac{64}{3}-56=64-\frac{64}{3}=\frac{128}{3}.$$

*Producer surplus.*

$$PS=4\cdot14-\int_0^4\left(6+\frac{q^2}{2}\right)dq
=56-\left[6q+\frac{q^3}{6}\right]_0^4
=56-\left(24+\frac{64}{6}\right)=32-\frac{32}{3}=\frac{64}{3}.$$

*Check.* The total surplus is
$\int_0^4\left[(30-q^2)-\left(6+\frac{q^2}{2}\right)\right]dq =\int_0^4\left(24-\frac32q^2\right)dq =96-32=64$, and $CS+PS=\frac{128}{3}+\frac{64}{3}=64$. ✓

## Advanced

### Solution 23

**(a)** For $f(x)=x$ on $[0,1]$,

$$f_{\mathrm{rms}}^2=\frac{1}{1-0}\int_0^1x^2dx=\frac13,
\qquad f_{\mathrm{rms}}=\frac{1}{\sqrt3}=\frac{\sqrt3}{3}.$$

**(b)** For $f(x)=\sin x$ on $[0,\pi]$, use $\sin^2x=\frac{1-\cos2x}{2}$:

$$f_{\mathrm{rms}}^2=\frac1\pi\int_0^\pi\sin^2x\,dx
=\frac1\pi\left[\frac x2-\frac{\sin2x}{4}\right]_0^\pi
=\frac1\pi\cdot\frac\pi2=\frac12,$$

so $f_{\mathrm{rms}}=\frac{1}{\sqrt2}=\frac{\sqrt2}{2}$.

*Check.* The RMS of $\sin$ over a full period is $1/\sqrt2\approx0.707$, the standard result for a
sinusoid. For $x$ on $[0,1]$, the RMS is $\sqrt3/3\approx0.577$ and the mean is $0.5$; the RMS must be at
least the mean, by Cauchy–Schwarz, and indeed it is. ✓

### Solution 24

*Set-up.* The lamina is $0\le y\le x^2$, $0\le x\le1$, with density $1$.

*About the $y$-axis.* The strip at $x$ is at distance $x$:

$$I_y=\int_0^1x^2\left(x^2-0\right)dx=\int_0^1x^4dx=\frac15 .$$

*About the $x$-axis.* Use $dI_x=\frac13(f^3-g^3)dx$ with $f=x^2$, $g=0$:

$$I_x=\frac13\int_0^1x^6dx=\frac13\cdot\frac17=\frac{1}{21}.$$

*Check.* Both are positive and less than the corresponding values for the unit square, $1/3$ and $1/3$;
the region is thinner than the square, so smaller moments are expected. The units are mass $\times$
length$^2$; with density $1$ the numerical values are in those units.

### Solution 25

*Set-up.* The cone is $0\le y\le\frac rhx$, $0\le x\le h$. At position $x$ the disk has radius
$f(x)=\frac rhx$. By the moment-of-inertia formula for a solid of revolution,

$$I=\frac{\pi\rho}{2}\int_0^h\left(\frac rhx\right)^4dx
=\frac{\pi\rho}{2}\cdot\frac{r^4}{h^4}\cdot\frac{h^5}{5}
=\frac{\pi\rho r^4h}{10}.$$

The mass is the volume times the density:

$$M=\rho\cdot\frac13\pi r^2h=\frac{\pi\rho r^2h}{3}.$$

Therefore

$$\frac{I}{M}=\frac{\pi\rho r^4h/10}{\pi\rho r^2h/3}
=\frac{3r^2}{10},\qquad I=\frac{3}{10}Mr^2.$$

*Check.* For a uniform disk of radius $r$, $I=\frac12Mr^2$; the cone's mass is spread closer to the axis
on average, so its coefficient should be smaller than $\frac12$; $\frac{3}{10}<\frac12$. ✓

### Solution 26

*Set-up.* Measure depth $h$ from the surface, $0\le h\le3$. By similar triangles, the width at depth $h$
is $w(h)=4\left(1-\frac h3\right)=4-\frac{4h}{3}$. Hence

$$F=\rho g\int_0^3h\left(4-\frac{4h}{3}\right)dh
=4\rho g\int_0^3\left(h-\frac{h^2}{3}\right)dh
=4\rho g\left[\frac{h^2}{2}-\frac{h^3}{9}\right]_0^3
=4\rho g\left(\frac92-3\right)=6\rho g .$$

With $\rho g=9800$, $F=58{,}800$ N.

*Check by the centroid shortcut.* The plate is a triangle of base $4$ and height $3$, so
$A=\frac12(4)(3)=6\ \mathrm{m^2}$. Its centroid is one third of the height above the base, i.e. at depth
$\bar h=1$ m. Then $F=\rho gA\bar h=6\rho g$, in agreement.

### Solution 27

*Normalization.*

$$\int_{-1}^1\frac34(1-x^2)\,dx
=\frac34\left[x-\frac{x^3}{3}\right]_{-1}^1
=\frac34\left[\left(1-\frac13\right)-\left(-1+\frac13\right)\right]
=\frac34\cdot\frac43=1 .$$

*Mean.* The integrand $x\cdot\frac34(1-x^2)$ is odd on the symmetric interval $[-1,1]$, so
$\mathbb{E}[X]=0$.

*Variance.* Since the mean is $0$, $\operatorname{Var}(X)=\mathbb{E}[X^2]$:

$$\mathbb{E}[X^2]=\frac34\int_{-1}^1x^2(1-x^2)\,dx
=\frac34\cdot2\left(\frac13-\frac15\right)
=\frac34\cdot\frac{4}{15}=\frac15 .$$

*Probability.*

$$\Pr\left(\lvert X\rvert\le\frac12\right)
=\frac34\int_{-1/2}^{1/2}(1-x^2)\,dx
=\frac34\cdot2\left(\frac12-\frac{1}{24}\right)
=\frac34\cdot\frac{11}{12}=\frac{11}{16}.$$

*Check.* $\frac{11}{16}=0.6875$, and the density is concentrated near $0$, so a probability above $1/2$ for
the central half of the interval is plausible. ✓

### Solution 28

*Set-up.* The cap is revolved about the $x$-axis, so the disk at $x\in[a,R]$ has radius
$\sqrt{R^2-x^2}$:

$$V=\pi\int_a^R(R^2-x^2)\,dx
=\pi\left[R^2x-\frac{x^3}{3}\right]_a^R
=\pi\left[\left(R^3-\frac{R^3}{3}\right)-\left(R^2a-\frac{a^3}{3}\right)\right].$$

Simplify:

$$V=\pi\left(\frac{2R^3}{3}-R^2a+\frac{a^3}{3}\right)
=\frac{\pi}{3}\left(2R^3-3R^2a+a^3\right).$$

Factor $2R^3-3R^2a+a^3=(R-a)^2(2R+a)$: expanding the right side gives
$2R^3+R^2a-4R^2a-2Ra^2+2Ra^2+a^3=2R^3-3R^2a+a^3$. Hence

$$V=\frac{\pi}{3}(R-a)^2(2R+a).$$

*Checks.* At $a=0$ this is $\frac{2\pi R^3}{3}$, the volume of a hemisphere; at $a=R$ it is $0$. Both
agree with the geometry.

### Solution 29

*Set-up.* Measure height $y$ from the vertex, so $0\le y\le4$. By similar triangles, the radius at height
$y$ satisfies $\frac{r(y)}{2}=\frac y4$, so $r(y)=\frac y2$ and $A(y)=\frac{\pi y^2}{4}$. The slice at
height $y$ is lifted $4-y$ metres, so

$$W=\gamma\int_0^4\frac{\pi y^2}{4}(4-y)\,dy
=\frac{\pi\gamma}{4}\left[\frac{4y^3}{3}-\frac{y^4}{4}\right]_0^4
=\frac{\pi\gamma}{4}\left(\frac{256}{3}-64\right).$$

Since $\frac{256}{3}-64=\frac{256-192}{3}=\frac{64}{3}$,

$$W=\frac{\pi\gamma}{4}\cdot\frac{64}{3}=\frac{16\pi\gamma}{3}.$$

With $\gamma=9800$, $W=\frac{156{,}800\pi}{3}\approx164{,}201$ J.

*Check by centre of mass.* The volume is $\frac13\pi(2)^2(4)=\frac{16\pi}{3}$, so the mass is
$\frac{16\pi\rho}{3}$. The centroid of a cone is one quarter of the height from the base, i.e. at
$y=3$, so the average lift is $4-3=1$ m. Hence
$W=Mg(1)=\frac{16\pi\rho g}{3}=\frac{16\pi\gamma}{3}$, in agreement.

### Solution 30

*Set-up.* The area is

$$A=\int_0^\pi\sin x\,dx=\left[-\cos x\right]_0^\pi=2 .$$

By symmetry about $x=\pi/2$, $\bar x=\pi/2$. For $\bar y$, the strip at $x$ has centroid height
$\frac12\sin x$ and width $\sin x\,dx$, so

$$M_x=\frac12\int_0^\pi\sin^2x\,dx
=\frac12\left[\frac x2-\frac{\sin2x}{4}\right]_0^\pi
=\frac12\cdot\frac\pi2=\frac{\pi}{4}.$$

Therefore

$$\bar y=\frac{M_x}{A}=\frac{\pi/4}{2}=\frac{\pi}{8}.$$

*Check.* The centroid lies on the axis of symmetry $x=\pi/2$ and at height $\pi/8\approx0.393$, which is
below the midpoint of the maximum height $1/2$; the sine arch is thinner near its top, so this is
plausible. ✓

### Solution 31

*Set-up.* Use shells about the $y$-axis. The shell at $x\in[0,\pi]$ has radius $x$ and height
$\sin x$ (non-negative on the interval), so

$$V=2\pi\int_0^\pi x\sin x\,dx .$$

Integrate by parts with $u=x$, $dv=\sin x\,dx$: $du=dx$, $v=-\cos x$,

$$\int_0^\pi x\sin x\,dx
=\left[-x\cos x\right]_0^\pi+\int_0^\pi\cos x\,dx
=\pi+\left[\sin x\right]_0^\pi=\pi .$$

Hence $V=2\pi\cdot\pi=2\pi^2$.

*Check.* Pappus's theorem gives $V=2\pi\bar xA=2\pi(\pi/2)(2)=2\pi^2$, because the centroid of the sine
arch has $\bar x=\pi/2$ and the area is $2$ (Solution 30). The dimension is a length cubed, and the value
$2\pi^2\approx19.74$ is positive. ✓

## Challenge

### Solution 32

**Theorem.** Let a plane region of area $A$ lie entirely above the horizontal line $y=k$, and let its
centroid be at distance $d=\bar y-k$ from that line. If the region is revolved about $y=k$, the volume is
$V=2\pi dA$.

*Proof.* Describe the region by horizontal strips: for $c\le y\le d_1$, the region is
$L(y)\le x\le R(y)$, with $L,R$ continuous and $c>k$. The horizontal strip at height $y$ has length
$R(y)-L(y)$ and thickness $dy$; when revolved about $y=k$ it sweeps a cylindrical shell of radius $y-k$
and height $R(y)-L(y)$. By the shell formula for a horizontal axis, the volume element is
$2\pi(y-k)(R-L)\,dy$, so

$$V=2\pi\int_c^{d_1}(y-k)\bigl(R(y)-L(y)\bigr)dy
=2\pi\left[\int_c^{d_1}y(R-L)\,dy-k\int_c^{d_1}(R-L)\,dy\right].$$

By the centroid formula for horizontal strips, $\int_c^{d_1}y(R-L)\,dy=A\bar y$ and
$\int_c^{d_1}(R-L)\,dy=A$. Hence

$$V=2\pi(A\bar y-kA)=2\pi A(\bar y-k)=2\pi dA . \qquad\blacksquare$$

*Hypotheses used.* $L,R$ continuous so that the integrals exist; the region lies on one side of the axis
so that $y-k$ has constant sign and the shell radius is $y-k$; the centroid exists, which follows from
the continuity and finite area. If the axis crosses the region, the formula counts the parts on the two
sides with opposite orientation and must be replaced by a split calculation.

### Solution 33

**By washers.** For $-r\le y\le r$, the disk $(x-R)^2+y^2\le r^2$ is described by
$R-\sqrt{r^2-y^2}\le x\le R+\sqrt{r^2-y^2}$. Revolve about the $y$-axis: the washer at height $y$ has
outer radius $R+\sqrt{r^2-y^2}$ and inner radius $R-\sqrt{r^2-y^2}$ (positive because $R>r$). Its area is

$$\pi\left[\left(R+s\right)^2-\left(R-s\right)^2\right]=4\pi Rs,
\qquad s=\sqrt{r^2-y^2}.$$

Therefore

$$V=4\pi R\int_{-r}^{r}\sqrt{r^2-y^2}\,dy .$$

The integral is the area of the semicircle of radius $r$, namely $\frac12\pi r^2$, so

$$V=4\pi R\cdot\frac{\pi r^2}{2}=2\pi^2Rr^2 .$$

**By Pappus.** The disk has area $A=\pi r^2$ and centroid at $(R,0)$. The axis $x=0$ does not meet the
disk because $R>r$, so the distance from the centroid to the axis is $d=R$. Pappus gives
$V=2\pi dA=2\pi R\cdot\pi r^2=2\pi^2Rr^2$, in agreement.

*Check.* The torus is contained in the cylinder of radius $R+r$ and height $2r$, whose volume is
$2\pi(R+r)^2r$; since $R>r$, $2\pi^2Rr^2<2\pi(R+r)^2r$? Numerically with $R=3$, $r=1$: torus
$2\pi^2(3)=6\pi^2\approx59.2$; cylinder $2\pi(16)=32\pi\approx100.5$. ✓

### Solution 34

*Mass.* The horizontal strip at height $y\in[0,R]$ has length $2\sqrt{R^2-y^2}$, thickness $dy$, and
density $ky$, so

$$M=\int_0^R ky\cdot2\sqrt{R^2-y^2}\,dy
=2k\int_0^Ry\sqrt{R^2-y^2}\,dy .$$

Substitute $u=R^2-y^2$, $du=-2y\,dy$:

$$M=2k\cdot\frac12\int_0^{R^2}u^{1/2}du
=k\left[\frac23u^{3/2}\right]_0^{R^2}
=\frac{2kR^3}{3}.$$

*Moment about the $x$-axis.* Each element of the strip is at distance $y$, so the moment element is
$y\,dm=ky^2\cdot2\sqrt{R^2-y^2}\,dy$, and

$$M_x=2k\int_0^Ry^2\sqrt{R^2-y^2}\,dy .$$

Put $y=R\sin\theta$, $dy=R\cos\theta\,d\theta$, with $\theta$ from $0$ to $\pi/2$; then
$\sqrt{R^2-y^2}=R\cos\theta$ and

$$M_x=2kR^4\int_0^{\pi/2}\sin^2\theta\cos^2\theta\,d\theta .$$

Since $\sin^2\theta\cos^2\theta=\frac14\sin^2 2\theta$ and
$\int_0^{\pi/2}\sin^2 2\theta\,d\theta=\frac{\pi}{4}$,

$$\int_0^{\pi/2}\sin^2\theta\cos^2\theta\,d\theta=\frac14\cdot\frac{\pi}{4}=\frac{\pi}{16},$$

so $M_x=2kR^4\cdot\frac{\pi}{16}=\frac{k\pi R^4}{8}$.

*Centroid.* By symmetry about the $y$-axis, $\bar x=0$, and

$$\bar y=\frac{M_x}{M}
=\frac{k\pi R^4/8}{2kR^3/3}
=\frac{3\pi R}{16}.$$

*Why $\bar y>\frac{4R}{3\pi}$.* The uniform semicircle has $\bar y=\frac{4R}{3\pi}\approx0.424R$; the
density $ky$ increases with height, so the mass is shifted upward, and
$\frac{3\pi}{16}\approx0.589>\frac{4}{3\pi}\approx0.424$. The calculation confirms the intuition.

### Solution 35

*Set-up.* The Gini coefficient is

$$G=1-2\int_0^1x^n\,dx
=1-\frac{2}{n+1}
=\frac{n+1-2}{n+1}
=\frac{n-1}{n+1}.$$

For $n=2$: $G=\frac{2-1}{2+1}=\frac13$. For $n=3$: $G=\frac{3-1}{3+1}=\frac12$.

*Checks and interpretation.* For $n=1$, $L(x)=x$, everyone receives the same fraction as their population
share, and $G=0$: perfect equality. As $n\to\infty$, $G\to1$: the Lorenz curve hugs the horizontal axis and
income is concentrated in an arbitrarily small top fraction. Since $x^n\le x$ for $n\ge1$ and
$0\le x\le1$, the Lorenz curve lies below the diagonal, as it must, and $G\ge0$. The area between the
Lorenz curve and the diagonal is $\int_0^1(x-x^n)dx=\frac12-\frac{1}{n+1}=\frac{G}{2}$, which is the
geometric meaning of $G$ as twice that area. ✓

### Solution 36

**Derivation.** Let $f\in C^1[a,b]$ with $f\ge0$ and $a\ge0$, and revolve the graph $y=f(x)$ about the
$y$-axis. Partition $[a,b]$ at $a=x_0<\cdots<x_n=b$ and consider the band over $[x_{k-1},x_k]$. The surface
is approximated by the frustum of a cone whose two radii are $x_{k-1}$ and $x_k$ — the **distances of the
endpoints from the axis of revolution**, not the heights $f(x_{k-1})$, $f(x_k)$ — and whose slant height is

$$\ell_k=\sqrt{(\Delta x_k)^2+(\Delta y_k)^2}.$$

By the Mean Value Theorem, there is $\xi_k\in(x_{k-1},x_k)$ with
$\Delta y_k=f'(\xi_k)\Delta x_k$, so
$\ell_k=\sqrt{1+f'(\xi_k)^2}\,\Delta x_k$. The lateral area of the frustum is
$\pi(r_1+r_2)\ell=\pi(x_{k-1}+x_k)\ell_k$ by Lemma 5 of §8.5. Therefore the total frustum area is

$$S_n=\sum_{k=1}^n\pi(x_{k-1}+x_k)\sqrt{1+f'(\xi_k)^2}\,\Delta x_k .$$

Let $M=\max_{[a,b]}\sqrt{1+f'(x)^2}$, which is finite because $f'$ is continuous. Compare $S_n$ with the
Riemann sum at the same points $\xi_k$:

$$\left\lvert S_n-2\pi\sum_{k=1}^n\xi_k\sqrt{1+f'(\xi_k)^2}\,\Delta x_k\right\rvert
\le\pi\sum_{k=1}^n\lvert x_{k-1}+x_k-2\xi_k\rvert\sqrt{1+f'(\xi_k)^2}\,\Delta x_k .$$

Since $x_{k-1}\le\xi_k\le x_k$, we have $\lvert x_{k-1}+x_k-2\xi_k\rvert\le2\Delta x_k$, so the right side
is at most

$$2\pi M\sum_{k=1}^n(\Delta x_k)^2\le2\pi M(b-a)\max_k\Delta x_k\longrightarrow0 .$$

The sum $2\pi\sum_k\xi_k\sqrt{1+f'(\xi_k)^2}\Delta x_k$ is a Riemann sum for the continuous function
$2\pi x\sqrt{1+f'(x)^2}$, hence converges to $2\pi\int_a^bx\sqrt{1+f'(x)^2}\,dx$. Therefore the frustum
areas tend to the integral,

$$S=2\pi\int_a^bx\sqrt{1+f'(x)^2}\,dx .$$

**Why the radius is $x$.** In a surface of revolution about the $y$-axis, the circle traced by a point
$(x,f(x))$ has radius equal to its horizontal distance from the axis, which is $x$. The height $f(x)$ is
measured along the axis and plays the role of the frustum's *length*, not its radius. Confusing the two
produces the wrong formula $2\pi\int f\sqrt{1+f'^2}\,dx$, which is the formula for revolution about the
$x$-axis, not the $y$-axis.

**Why the limit is the integral.** The frustum area is a Riemann sum of a continuous function once the
second-order term is removed. The removal is legitimate because each error is $O((\Delta x_k)^2)$ and the
sum of $n$ such terms is $O(\max\Delta x)$; this is the same argument that justifies the shell formula.
Continuity of $f'$ is what makes $\sqrt{1+f'^2}$ continuous and the Riemann sums converge; for a merely
continuous $f$ the surface area may be infinite. $\blacksquare$
