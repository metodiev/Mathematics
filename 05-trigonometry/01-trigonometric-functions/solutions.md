# Trigonometric Functions — Solutions

> [Tutorial](README.md) · [Exercises](exercises.md)

Each solution states the strategy first, then every significant step. Exact answers are given in closed form; decimals appear only where the problem asks for them, and then they are marked with $\approx$. If your answer differs, compare the intermediate lines before assuming the arithmetic is wrong — in this topic the error is usually a swapped opposite/adjacent or a misremembered special value.

## Beginner

**1.** Strategy: the hypotenuse is missing, so compute it with Pythagoras before forming any ratio.

$$h = \sqrt{6^2 + 8^2} = \sqrt{36 + 64} = \sqrt{100} = 10.$$

Relative to the angle opposite the side of length $6$: opposite $= 6$, adjacent $= 8$, hypotenuse $= 10$. Hence

$$\sin\theta = \frac{6}{10} = \frac{3}{5}, \qquad \cos\theta = \frac{8}{10} = \frac{4}{5}, \qquad \tan\theta = \frac{6}{8} = \frac{3}{4}.$$

*Check:* $\sin^2\theta + \cos^2\theta = \frac{9}{25} + \frac{16}{25} = 1$, and $\tan\theta = \frac{3/5}{4/5} = \frac34$. This is the $3$–$4$–$5$ triangle scaled by $2$, so the ratios must match those of Section 7.1 — they do.

**2.** Strategy: Pythagoras gives the missing leg; the ratios then follow directly.

$$a = \sqrt{41^2 - 9^2} = \sqrt{1681 - 81} = \sqrt{1600} = 40.$$

Therefore

$$\sin\theta = \frac{9}{41}, \qquad \cos\theta = \frac{40}{41}, \qquad \tan\theta = \frac{9}{40}.$$

*Check:* $9^2 + 40^2 = 81 + 1600 = 1681 = 41^2$, and $\frac{9/41}{40/41} = \frac{9}{40}$.

**3.** Both values come from the half-equilateral triangle:

$$\sin 30^\circ + \cos 60^\circ = \frac{1}{2} + \frac{1}{2} = 1.$$

The coincidence is the cofunction identity in action: $\cos 60^\circ = \sin(90^\circ - 60^\circ) = \sin 30^\circ$, so the sum is $2\sin 30^\circ = 1$.

**4.** $\tan 45^\circ = 1$ (the two legs of the isosceles right triangle are equal) and $\sin 30^\circ = \tfrac12$:

$$\tan 45^\circ + \sin 30^\circ = 1 + \frac{1}{2} = \frac{3}{2}.$$

**5.** From the half-equilateral triangle, $\sin 60^\circ = \frac{\sqrt3}{2}$ and $\cos 30^\circ = \frac{\sqrt3}{2}$:

$$\sin 60^\circ \cos 30^\circ = \frac{\sqrt{3}}{2}\cdot\frac{\sqrt{3}}{2} = \frac{3}{4}.$$

Note $\cos 30^\circ = \sin 60^\circ$ by the cofunction identity, so the product is $\sin^2 60^\circ = \frac34$.

**6.** Compute each factor separately: $\sin 45^\circ = \cos 45^\circ = \frac{\sqrt2}{2}$ and $\sin 30^\circ = \frac12$. Then

$$\frac{\sqrt{2}}{2}\cdot\frac{\sqrt{2}}{2} + \left(\frac{1}{2}\right)^2 = \frac{2}{4} + \frac{1}{4} = \frac{1}{2} + \frac{1}{4} = \frac{3}{4}.$$

**7.** Substitute the table values and simplify the compound fraction:

$$\frac{\tan 60^\circ}{\tan 30^\circ} = \frac{\sqrt{3}}{\frac{\sqrt{3}}{3}} = \sqrt{3}\cdot\frac{3}{\sqrt{3}} = 3.$$

Division by $\frac{\sqrt3}{3}$ is multiplication by $\frac{3}{\sqrt3}$, and $\sqrt3/\sqrt3 = 1$.

**8.** In a $30$–$60$–$90$ triangle the sides are in the ratio $1 : \sqrt3 : 2$, with the shortest side opposite the $30^\circ$ angle and the middle side opposite the $60^\circ$ angle. The hypotenuse is $14$, so the scale factor from $(1,\sqrt3,2)$ is $7$:

$$\text{leg opposite } 30^\circ = 7, \qquad \text{leg opposite } 60^\circ = 7\sqrt{3} \approx 12.12.$$

*Check:* $7^2 + (7\sqrt3)^2 = 49 + 147 = 196 = 14^2$.

**9.** An isosceles right triangle has legs $x, x$ and hypotenuse $x\sqrt2$:

$$x\sqrt{2} = 8 \quad\Longrightarrow\quad x = \frac{8}{\sqrt{2}} = 4\sqrt{2} \approx 5.66.$$

The rationalisation is $\frac{8}{\sqrt2}\cdot\frac{\sqrt2}{\sqrt2} = \frac{8\sqrt2}{2} = 4\sqrt2$.

**10.** Strategy: build the triangle from the ratio. If $\sin\theta = \frac{5}{13}$ then opposite $= 5k$ and hypotenuse $= 13k$ for some $k>0$. The adjacent side is

$$a = \sqrt{(13k)^2 - (5k)^2} = k\sqrt{169-25} = k\sqrt{144} = 12k.$$

Hence

$$\cos\theta = \frac{12k}{13k} = \frac{12}{13}, \qquad \tan\theta = \frac{5k}{12k} = \frac{5}{12}.$$

The unknown scale $k$ cancels, which is Theorem 5.4 again.

**11.** Use the reciprocal definitions and the exact-value table:

$$\sec 45^\circ = \frac{1}{\cos 45^\circ} = \frac{1}{\sqrt2/2} = \frac{2}{\sqrt2} = \sqrt{2},$$
$$\csc 30^\circ = \frac{1}{\sin 30^\circ} = \frac{1}{1/2} = 2,$$
$$\cot 60^\circ = \frac{1}{\tan 60^\circ} = \frac{1}{\sqrt3} = \frac{\sqrt{3}}{3}.$$

**12.** The tangent compares rise to run:

$$\tan\theta = \frac{4}{100} = \frac{1}{25} = 0.04.$$

The angle is the inverse tangent: $\theta = \arctan(0.04) \approx 2.2906^\circ$, so $\theta \approx 2.29^\circ$. Both lengths are in metres, so the ratio is dimensionless — mixing centimetres and metres here would give $0.004$ and the wrong angle.

**13.** The wire is the hypotenuse. The height on the pole is opposite the angle at the ground; the anchor distance is adjacent:

$$\text{height} = 6\sin 55^\circ \approx 6 \times 0.8191520 = 4.9149 \approx 4.91\ \mathrm{m},$$
$$\text{distance} = 6\cos 55^\circ \approx 6 \times 0.5735764 = 3.4415 \approx 3.44\ \mathrm{m}.$$

*Check:* $4.91^2 + 3.44^2 = 24.1081 + 11.8336 = 35.9417 \approx 36 = 6^2$; the difference is rounding.

**14.** The shadow is the adjacent side, the tree the opposite side:

$$h = 18\tan 50^\circ \approx 18 \times 1.1917536 = 21.4516 \approx 21.45\ \mathrm{m}.$$

A quick sanity check on which function to use: at $45^\circ$ the shadow equals the height, and at $50^\circ$ the sun is steeper, so the shadow should be shorter than the tree — indeed $18 < 21.45$.

## Intermediate

**15.** From $\cos\theta = \frac{15}{17}$ take adjacent $= 15k$, hypotenuse $= 17k$. Then

$$o = \sqrt{(17k)^2 - (15k)^2} = k\sqrt{289 - 225} = k\sqrt{64} = 8k.$$

So

$$\sin\theta = \frac{8}{17}, \qquad \tan\theta = \frac{8}{15}, \qquad \csc\theta = \frac{17}{8}, \qquad \cot\theta = \frac{15}{8}.$$

**16.** Strategy: replace the tangent by its quotient form (Property 8.2) and cancel.

$$\tan\theta\cos\theta = \frac{\sin\theta}{\cos\theta}\cdot\cos\theta = \sin\theta.$$

The cancellation is legitimate because $\theta$ is acute, hence $\cos\theta \ne 0$. Reading the identity in reverse gives a useful formula: the opposite side equals the hypotenuse times $\sin$, which is the same as "adjacent times $\tan$".

**17.** With $\tan\theta = \frac{7}{24}$, take opposite $= 7k$ and adjacent $= 24k$. The hypotenuse is

$$h = k\sqrt{7^2 + 24^2} = k\sqrt{49 + 576} = k\sqrt{625} = 25k.$$

Therefore

$$\sin\theta = \frac{7}{25}, \qquad \cos\theta = \frac{24}{25}, \qquad \sec\theta = \frac{25}{24}.$$

*Check:* $\frac{7/25}{24/25} = \frac{7}{24}$, as required.

**18.** The cliff top is opposite the elevation angle and the $60\ \mathrm{m}$ is adjacent:

$$h = 60\tan 32^\circ \approx 60 \times 0.6248694 = 37.4922 \approx 37.49\ \mathrm{m}.$$

**19.** The string is the hypotenuse. The height is opposite and the horizontal distance is adjacent:

$$\text{height} = 45\sin 38^\circ \approx 45 \times 0.6156615 = 27.7048 \approx 27.70\ \mathrm{m},$$
$$\text{distance} = 45\cos 38^\circ \approx 45 \times 0.7880108 = 35.4605 \approx 35.46\ \mathrm{m}.$$

*Check:* $27.70^2 + 35.46^2 = 767.29 + 1257.41 = 2024.70 \approx 2025 = 45^2$.

**20.** Bearing is measured clockwise from north, so the northward displacement is the adjacent side and the eastward displacement the opposite side of a right triangle with hypotenuse $20$:

$$\text{north} = 20\cos 40^\circ \approx 15.32\ \mathrm{km}, \qquad \text{east} = 20\sin 40^\circ \approx 12.86\ \mathrm{km}.$$

Exact forms are $20\cos 40^\circ$ and $20\sin 40^\circ$; unlike the special angles, $40^\circ$ has no closed form in square roots. A common error is to swap them, putting $20\sin 40^\circ$ north; the check is that at a bearing of $0^\circ$ (due north) the whole displacement must be northward, and $\cos 0^\circ = 1$ while $\sin 0^\circ = 0$ gives exactly that.

**21.** Strategy: two right triangles share the vertical side $h$; write $h$ twice and eliminate the unknown horizontal distance.

Let $d$ be the horizontal distance from $A$ to the foot of the tower. From $A$:

$$\tan 45^\circ = \frac{h}{d} = 1 \quad\Longrightarrow\quad h = d.$$

From $B$, which is $d + 20$ from the foot:

$$\tan 30^\circ = \frac{h}{d+20} = \frac{1}{\sqrt3} \quad\Longrightarrow\quad h = \frac{d+20}{\sqrt3}.$$

Equate the two expressions for $h$:

$$d = \frac{d+20}{\sqrt{3}} \quad\Longrightarrow\quad d\sqrt{3} = d + 20 \quad\Longrightarrow\quad d(\sqrt3 - 1) = 20.$$

Hence

$$d = \frac{20}{\sqrt3 - 1} = \frac{20(\sqrt3+1)}{(\sqrt3-1)(\sqrt3+1)} = \frac{20(\sqrt3+1)}{2} = 10(\sqrt3+1),$$

using $( \sqrt3 - 1)(\sqrt3+1) = 3 - 1 = 2$. Since $h = d$,

$$h = 10(\sqrt{3}+1) \approx 10 \times 2.7320508 = 27.3205 \approx 27.32\ \mathrm{m}.$$

*Check:* from $B$ the distance is $d + 20 \approx 47.32$, and $47.32\tan 30^\circ = 47.32 \times 0.57735 = 27.32$. Consistent.

**22.** Let $ABC$ be right-angled at $C$, with $\angle A = \theta$. Then $\angle B = 90^\circ - \theta$ because the acute angles of a right triangle are complementary. The side opposite $A$ is $BC$, and the same side $BC$ is adjacent to $B$. Therefore

$$\sin\theta = \frac{BC}{AB} = \cos(90^\circ - \theta).$$

The point is that the *same* side plays the role "opposite" for one acute angle and "adjacent" for the other, so the two ratios are equal by definition. Applying this with $\theta = 65^\circ$:

$$\sin 25^\circ = \cos(90^\circ - 25^\circ) = \cos 65^\circ.$$

**23.** A slope of $1{:}12$ means rise $:$ run $= 1 : 12$, so

$$\text{run} = 12 \times 0.60 = 7.20\ \mathrm{m}.$$

The ramp length is the hypotenuse:

$$L = \sqrt{7.20^2 + 0.60^2} = \sqrt{51.84 + 0.36} = \sqrt{52.20} \approx 7.2250 \approx 7.23\ \mathrm{m}.$$

The angle satisfies $\tan\theta = \frac{1}{12}$, so

$$\theta = \arctan\!\left(\frac{1}{12}\right) \approx 4.7636^\circ \approx 4.76^\circ.$$

*Check:* $7.20\cos 4.76^\circ \approx 7.20 \times 0.99655 = 7.175$ and $7.23 \sin 4.76^\circ \approx 7.23 \times 0.08300 = 0.600$; both agree with the data to the stated precision.

**24.** The horizontal component is adjacent to the $35^\circ$ angle, the vertical component opposite:

$$F_h = 300\cos 35^\circ \approx 300 \times 0.8191520 = 245.7456 \approx 245.75\ \mathrm{N},$$
$$F_v = 300\sin 35^\circ \approx 300 \times 0.5735764 = 172.0729 \approx 172.07\ \mathrm{N}.$$

*Check:* $245.75^2 + 172.07^2 = 60393.06 + 29608.08 = 90001.14$, and $300^2 = 90000$; the excess is rounding of the components upward.

**25.** Split each leg of the flight into north and east components. For a bearing $\phi$, north $= d\cos\phi$ and east $= d\sin\phi$.

First leg, $\phi = 30^\circ$:

$$\text{north}_1 = 150\cos 30^\circ = 150\cdot\frac{\sqrt3}{2} = 75\sqrt3, \qquad \text{east}_1 = 150\sin 30^\circ = 75.$$

Second leg, bearing $120^\circ$: this direction is $30^\circ$ south of east, so its eastward component uses $\cos 30^\circ$ of the $100\ \mathrm{km}$ and its northward component is negative, $-100\sin 30^\circ$:

$$\text{east}_2 = 100\cos 30^\circ = 50\sqrt3, \qquad \text{north}_2 = -100\sin 30^\circ = -50.$$

Adding:

$$\text{north} = 75\sqrt3 - 50 \approx 129.9038 - 50 = 79.9038 \approx 79.90\ \mathrm{km},$$
$$\text{east} = 75 + 50\sqrt3 \approx 75 + 86.6025 = 161.6025 \approx 161.60\ \mathrm{km}.$$

The sign bookkeeping — "south of east" turns a north component negative while leaving the acute-angle trigonometry untouched — is the standard way to handle bearings beyond $90^\circ$ before angles are extended formally.

## Advanced

**26.** **(a) Algebraic route.** Start from Property 8.3 and divide by $\cos^2\theta$, which is nonzero for acute $\theta$:

$$\frac{\sin^2\theta}{\cos^2\theta} + \frac{\cos^2\theta}{\cos^2\theta} = \frac{1}{\cos^2\theta}.$$

Now $\frac{\sin^2\theta}{\cos^2\theta} = \left(\frac{\sin\theta}{\cos\theta}\right)^2 = \tan^2\theta$ and $\frac{1}{\cos^2\theta} = \sec^2\theta$, so

$$\tan^2\theta + 1 = \sec^2\theta.$$

**(b) Direct route.** In the right triangle, $o^2 + a^2 = h^2$. Divide by $a^2 > 0$:

$$\frac{o^2}{a^2} + \frac{a^2}{a^2} = \frac{h^2}{a^2}, \qquad\text{that is,}\qquad \tan^2\theta + 1 = \sec^2\theta.$$

Both routes prove the same statement; the second shows that the identity is Pythagoras in disguise, the first shows that it is a consequence of the sine/cosine identity. Since both reduce to $o^2 + a^2 = h^2$, they cannot disagree.

**27.** **First proof (triangle inequality).** Write the legs as $o, a$ and the hypotenuse as $h$. In any nondegenerate triangle, the sum of two sides exceeds the third:

$$o + a > h.$$

Dividing by $h > 0$,

$$\frac{o}{h} + \frac{a}{h} > 1, \qquad\text{that is,}\qquad \sin\theta + \cos\theta > 1.$$

**Second proof (algebra).** Square the sum:

$$(\sin\theta + \cos\theta)^2 = \sin^2\theta + 2\sin\theta\cos\theta + \cos^2\theta = 1 + 2\sin\theta\cos\theta.$$

For an acute angle, $\sin\theta > 0$ and $\cos\theta > 0$, so $2\sin\theta\cos\theta > 0$ and therefore $(\sin\theta+\cos\theta)^2 > 1$. Since $\sin\theta + \cos\theta > 0$, taking positive square roots gives $\sin\theta + \cos\theta > 1$.

**Why equality is impossible.** Equality in the triangle inequality occurs only for a degenerate triangle — one whose three vertices are collinear. A right triangle with a nonzero acute angle is nondegenerate, so the inequality is strict. In the algebraic proof, equality would require $\sin\theta\cos\theta = 0$, which happens only at $\theta = 0^\circ$ or $90^\circ$; neither is an acute angle of a right triangle.

**28.** Strategy: solve for the horizontal distance with the lower angle, then use it for the taller sight line.

Let $d$ be the horizontal distance from the observer to the wall under the pole. The building's top is at $45^\circ$:

$$\tan 45^\circ = \frac{20}{d} = 1 \quad\Longrightarrow\quad d = 20\ \mathrm{m}.$$

The pole's top is at $60^\circ$ from the same point, so its height above the ground is

$$H = d\tan 60^\circ = 20\sqrt{3} \approx 34.6410\ \mathrm{m}.$$

The pole stands on the roof, so its own height is

$$H - 20 = 20\sqrt3 - 20 = 20(\sqrt3 - 1) \approx 20 \times 0.7320508 = 14.6410 \approx 14.64\ \mathrm{m}.$$

*Check:* the elevation of the pole's top from the observer is $\arctan(34.6410/20) = \arctan(1.73205) = 60^\circ$, as given.

**29.** Strategy: two right triangles on opposite sides share the height; the two horizontal distances add to $100$.

Let $h$ be the height and let $x$ be the horizontal distance from the $30^\circ$ observer to the foot of the tower, $y$ the distance from the $45^\circ$ observer. Then

$$x + y = 100, \qquad \tan 30^\circ = \frac{h}{x}, \qquad \tan 45^\circ = \frac{h}{y}.$$

From the second and third,

$$x = \frac{h}{\tan 30^\circ} = h\sqrt3, \qquad y = \frac{h}{\tan 45^\circ} = h.$$

Substituting into $x + y = 100$:

$$h\sqrt3 + h = 100 \quad\Longrightarrow\quad h(\sqrt3 + 1) = 100 \quad\Longrightarrow\quad h = \frac{100}{\sqrt3+1}.$$

Rationalise with $\sqrt3 - 1$:

$$h = \frac{100(\sqrt3 - 1)}{(\sqrt3+1)(\sqrt3-1)} = \frac{100(\sqrt3-1)}{2} = 50(\sqrt3 - 1) \approx 50 \times 0.7320508 = 36.6025 \approx 36.60\ \mathrm{m}.$$

*Check:* $x = h\sqrt3 \approx 63.40$ and $y = h \approx 36.60$; their sum is $100.00$. Also $36.60/63.40 = 0.5773 = \tan 30^\circ$.

**30.** Convert both functions to sine and cosine:

$$\tan\theta + \cot\theta = \frac{\sin\theta}{\cos\theta} + \frac{\cos\theta}{\sin\theta} = \frac{\sin^2\theta + \cos^2\theta}{\sin\theta\cos\theta} = \frac{1}{\sin\theta\cos\theta},$$

where the common denominator is $\sin\theta\cos\theta$ and the numerator collapsed by Property 8.3. This proves the identity.

For the inequality, start from the square of a real number:

$$(\sin\theta - \cos\theta)^2 \ge 0.$$

Expanding and using $\sin^2\theta + \cos^2\theta = 1$:

$$1 - 2\sin\theta\cos\theta \ge 0 \quad\Longrightarrow\quad 2\sin\theta\cos\theta \le 1 \quad\Longrightarrow\quad \sin\theta\cos\theta \le \frac{1}{2}.$$

Since $\sin\theta\cos\theta > 0$ for acute $\theta$, inverting reverses the inequality:

$$\frac{1}{\sin\theta\cos\theta} \ge 2.$$

Therefore $\tan\theta + \cot\theta \ge 2$. Equality holds exactly when $\sin\theta = \cos\theta$, i.e. when the two legs are equal, which is $\theta = 45^\circ$. Indeed $\tan 45^\circ + \cot 45^\circ = 1 + 1 = 2$.

**31.** Strategy: multiply numerator and denominator by $1 - \sin\theta$, the conjugate of the numerator.

$$\frac{1+\sin\theta}{\cos\theta} = \frac{(1+\sin\theta)(1-\sin\theta)}{\cos\theta\,(1-\sin\theta)} = \frac{1 - \sin^2\theta}{\cos\theta\,(1-\sin\theta)} = \frac{\cos^2\theta}{\cos\theta\,(1-\sin\theta)} = \frac{\cos\theta}{1-\sin\theta}.$$

Three facts are used: the difference of squares $(1+\sin\theta)(1-\sin\theta) = 1-\sin^2\theta$; Property 8.3 in the form $1 - \sin^2\theta = \cos^2\theta$; and the cancellation of one factor $\cos\theta$, legitimate because $\cos\theta \ne 0$ for acute $\theta$. The final division by $1-\sin\theta$ is also safe since $\sin\theta < 1$.

At $\theta = 60^\circ$, with $\sin 60^\circ = \frac{\sqrt3}{2}$ and $\cos 60^\circ = \frac12$:

$$\text{left} = \frac{1 + \frac{\sqrt3}{2}}{\frac12} = 2\left(1 + \frac{\sqrt3}{2}\right) = 2 + \sqrt3,$$
$$\text{right} = \frac{\frac12}{1 - \frac{\sqrt3}{2}} = \frac{\frac12}{\frac{2-\sqrt3}{2}} = \frac{1}{2-\sqrt3} = \frac{2+\sqrt3}{(2-\sqrt3)(2+\sqrt3)} = 2+\sqrt3.$$

Both sides equal $2 + \sqrt3 \approx 3.732$, as the identity requires.

**32.** Strategy: both angles are measured from the horizontal through the observer's eye, so compute the two heights *above eye level* and subtract. The eye height cancels.

Height above eye level of the bottom of the window:

$$h_1 = 30\tan 25^\circ \approx 30 \times 0.4663077 = 13.9892\ \mathrm{m}.$$

Height above eye level of the top of the window:

$$h_2 = 30\tan 40^\circ \approx 30 \times 0.8390996 = 25.1730\ \mathrm{m}.$$

The window's height is the difference:

$$h_2 - h_1 \approx 25.1730 - 13.9892 = 11.1838 \approx 11.18\ \mathrm{m}.$$

**Why the eye height cancels.** Both sightings start from the same point, so both right triangles have their horizontal leg at eye level. Adding the eye height $1.8\ \mathrm{m}$ to each of $h_1, h_2$ converts them to heights above the ground, and the difference $(h_2 + 1.8) - (h_1 + 1.8)$ is unchanged. The eye height would matter if one angle had been measured from the ground and the other from eye level — a genuine hazard in field work.

*Sanity check:* at $45^\circ$ the height above eye level would equal the $30\ \mathrm{m}$ distance, and $40^\circ < 45^\circ$ gives $25.17 < 30$, which is consistent.

## Challenge

**33.** **Claim.** If $0^\circ < \alpha < \beta < 90^\circ$ then $\sin\alpha < \sin\beta$.

*Proof.* Fix a length $h$ and consider the circle with diameter $AB = h$, whose centre is $M$ and whose radius is $R = h/2$. Let $C$ be a point on the circle. By Thales' theorem, $\angle ACB = 90^\circ$, so $ABC$ is a right triangle with hypotenuse $h$ and $\angle BAC = \alpha$. Hence

$$\sin\alpha = \frac{BC}{AB} = \frac{BC}{h}.$$

By the inscribed-angle theorem, the angle $\angle BAC$ subtends the arc $BC$, so the central angle $\angle BMC$ equals $2\alpha$. Now $BC$ is the base of the isosceles triangle $BMC$ with equal sides $R$ and apex angle $2\alpha$.

It remains to know that the base of an isosceles triangle with fixed legs grows strictly with the apex angle. That is the **hinge theorem** (Euclid, *Elements* I.24): if two triangles have two sides respectively equal, and the angle included by those sides is larger in one triangle, then the third side is larger in that triangle. Applying it to the pairs of rays at angles $2\alpha < 2\beta$, the chord subtending $2\alpha$ is strictly shorter than the chord subtending $2\beta$, so $BC(\alpha) < BC(\beta)$, and dividing by $h$,

$$\sin\alpha < \sin\beta. \qquad \blacksquare$$

**Why this matters for $\arcsin$.** A function must return exactly one value for each input. The numbers $\sin\alpha$ and $\sin\beta$ being distinct whenever $\alpha \ne \beta$ means that a value $y \in (0,1)$ cannot come from two different acute angles — so "the acute angle whose sine is $y$" is unambiguous. Combined with the fact that $\sin\theta$ runs continuously from $0$ (at $0^\circ$) to $1$ (at $90^\circ$), every $y \in (0,1)$ is attained exactly once, which is precisely the statement that $\arcsin$ is a well-defined function on $(0,1)$. Without strict monotonicity the expression $\arcsin y$ would be ambiguous.

**34.** **Construction.** Let $ABC$ be right-angled at $C$ with $\angle A = 30^\circ$ and hypotenuse $AB = 2$. Then $BC = 1$ (opposite the $30^\circ$ angle) and $AC = \sqrt3$ (opposite the $60^\circ$ angle), from Section 7.4.

Extend the segment $CA$ beyond $A$ to a point $D$ with $AD = AB = 2$. Then

$$DC = DA + AC = 2 + \sqrt3.$$

**Angles.** Since $B$, $A$, $D$ are collinear with $A$ between $C$ and $D$, the angle $\angle BAD$ is supplementary to $\angle BAC$:

$$\angle BAD = 180^\circ - 30^\circ = 150^\circ.$$

Triangle $ABD$ is isosceles with $AB = AD = 2$, so its base angles are equal, and

$$\angle ABD = \angle BDA = \frac{180^\circ - 150^\circ}{2} = 15^\circ.$$

**Tangent.** Triangle $DCB$ is right-angled at $C$ (the same right angle as in $ABC$), with angle $15^\circ$ at $D$, opposite side $BC = 1$ and adjacent side $DC = 2 + \sqrt3$. Therefore

$$\tan 15^\circ = \frac{1}{2+\sqrt3} = \frac{2-\sqrt3}{(2+\sqrt3)(2-\sqrt3)} = \frac{2-\sqrt3}{4-3} = 2 - \sqrt{3}.$$

Numerically $2 - \sqrt3 \approx 0.267949$, consistent with the known $\tan 15^\circ \approx 0.2679$.

**Sine and cosine.** In the same triangle the hypotenuse is $DB$:

$$DB = \sqrt{DC^2 + BC^2} = \sqrt{(2+\sqrt3)^2 + 1} = \sqrt{7 + 4\sqrt3 + 1} = \sqrt{8 + 4\sqrt3}.$$

Now $(\sqrt6 + \sqrt2)^2 = 6 + 2\sqrt{12} + 2 = 8 + 4\sqrt3$, so $DB = \sqrt6 + \sqrt2$. Hence

$$\sin 15^\circ = \frac{BC}{DB} = \frac{1}{\sqrt6+\sqrt2} = \frac{\sqrt6-\sqrt2}{(\sqrt6+\sqrt2)(\sqrt6-\sqrt2)} = \frac{\sqrt6-\sqrt2}{6-2} = \frac{\sqrt6-\sqrt2}{4},$$
$$\cos 15^\circ = \frac{DC}{DB} = \frac{2+\sqrt3}{\sqrt6+\sqrt2} = \frac{(2+\sqrt3)(\sqrt6-\sqrt2)}{4} = \frac{2\sqrt6 - 2\sqrt2 + \sqrt{18} - \sqrt6}{4} = \frac{\sqrt6+\sqrt2}{4},$$

where $\sqrt{18} = 3\sqrt2$ was used in the last line. Numerically $\sin 15^\circ \approx 0.258819$ and $\cos 15^\circ \approx 0.965926$, and indeed $0.258819^2 + 0.965926^2 = 0.066987 + 0.933013 = 1$.

**35.** *Proof of the formula.* The hypothesis $\tan\theta = \frac{p}{q}$ says that the ratio opposite : adjacent equals $p : q$. Therefore for some $k > 0$ the opposite side is $pk$ and the adjacent side is $qk$. By Pythagoras the hypotenuse is

$$h = \sqrt{(pk)^2 + (qk)^2} = k\sqrt{p^2+q^2}.$$

Then

$$\sin\theta = \frac{pk}{k\sqrt{p^2+q^2}} = \frac{p}{\sqrt{p^2+q^2}}, \qquad \cos\theta = \frac{qk}{k\sqrt{p^2+q^2}} = \frac{q}{\sqrt{p^2+q^2}},$$

and the unknown scale $k$ cancels — which is the content of Theorem 5.4 once more.

*Rationality.* Squaring removes the square root:

$$\sin^2\theta = \frac{p^2}{p^2+q^2}, \qquad \cos^2\theta = \frac{q^2}{p^2+q^2},$$

which are quotients of integers, hence rational, for every pair of positive integers $p,q$. The value $\sin\theta$ itself is rational exactly when $\sqrt{p^2+q^2}$ is an integer, because $\frac{p}{\sqrt{p^2+q^2}}\cdot\frac{\sqrt{p^2+q^2}}{\sqrt{p^2+q^2}} = \frac{p\sqrt{p^2+q^2}}{p^2+q^2}$ is rational precisely when the surd $\sqrt{p^2+q^2}$ is an integer. That condition is exactly the definition of a Pythagorean triple $(p, q, \sqrt{p^2+q^2})$.

*Example.* For the $20$–$21$–$29$ triangle, $20^2 + 21^2 = 400 + 441 = 841 = 29^2$, so with $p = 20$ and $q = 21$,

$$\sin\theta = \frac{20}{29} \approx 0.6897, \qquad \cos\theta = \frac{21}{29} \approx 0.7241.$$

These are rational, as expected for a triple; the $1$–$1$–$\sqrt2$ triangle, by contrast, gives $\sin 45^\circ = \frac{\sqrt2}{2}$, irrational, because $\sqrt{1^2+1^2} = \sqrt2$ is not an integer.

**36.** **(a) Procedure and formula.** Choose a point $A$ on level ground with a clear view of the tower, and a straight line from $A$ that passes through the point directly beneath the top of the tower (sight on the tower and keep the base of the tower on that sight line as you move). Measure the angle of elevation $\alpha$ at $A$. Walk a measured distance $L$ directly away from the tower, staying on the same line, to a point $B$, and measure the angle of elevation $\beta$ there; necessarily $\beta < \alpha$.

Let $d$ be the horizontal distance from $A$ to the foot of the tower and $h$ the height. The two right triangles give

$$h = d\tan\alpha, \qquad h = (d + L)\tan\beta.$$

Equating:

$$d\tan\alpha = d\tan\beta + L\tan\beta \quad\Longrightarrow\quad d(\tan\alpha - \tan\beta) = L\tan\beta,$$

so

$$d = \frac{L\tan\beta}{\tan\alpha - \tan\beta}, \qquad h = d\tan\alpha = \frac{L\tan\alpha\tan\beta}{\tan\alpha - \tan\beta}.$$

The instrument's height $e$ above the ground does not cancel here the way it did in Problem 32, because both sightings are made from the same height: the computed $h$ is the height of the top *above the instrument*, so the true height is $h + e$. Measuring both angles from the same instrument height and adding $e$ at the end is the correct bookkeeping.

**(b) Numerical answer.** With $\alpha = 35^\circ$, $\beta = 22^\circ$ and $L = 40\ \mathrm{m}$:

$$\tan 35^\circ \approx 0.7002075, \qquad \tan 22^\circ \approx 0.4040262,$$
$$d = \frac{40 \times 0.4040262}{0.7002075 - 0.4040262} = \frac{16.16105}{0.2961813} \approx 54.5645\ \mathrm{m},$$
$$h = 54.5645 \times 0.7002075 \approx 38.2069\ \mathrm{m}.$$

So the top of the tower is about $38.21\ \mathrm{m}$ above the instrument; add the instrument height for the height above the ground.

*Check:* from $B$ the distance is $54.5645 + 40 = 94.5645$, and $94.5645 \times \tan 22^\circ = 94.5645 \times 0.4040262 = 38.2069$. Both triangles agree.

**(c) Sources of error.**

1. **Angle measurement, amplified by the small denominator.** The formula divides by $\tan\alpha - \tan\beta$, a difference of two similar numbers. For the data above, changing $\alpha$ from $35^\circ$ to $35.5^\circ$ gives $\tan 35.5^\circ \approx 0.7133$, hence $d = 16.16105/(0.7133-0.40403) \approx 52.25$ and $h \approx 37.27$ — an error of about $1\ \mathrm{m}$, or $2.5\%$, from a half-degree misreading. Angles should be measured with the best instrument available and repeated.
2. **Failure to stay on the line through the base.** If the walk from $A$ to $B$ is not along the line joining the observer to the foot of the tower, the horizontal distances no longer differ by exactly $L$ and the formula is invalid. A related hazard is sloping ground: the formula uses *horizontal* distance, so a slope changes the effective $L$ by a factor $\cos(\text{slope})$.

A third, smaller effect at long range is atmospheric refraction and the curvature of the Earth, which make the apparent elevation slightly too large; it is negligible for towers and relevant only for kilometres.

**Method note.** The same two-angle trick underlies the parallax method for the distance to nearby stars and the base-line method of terrestrial surveying: measure a known baseline, observe the same object from both ends, and let geometry supply what cannot be measured directly.
