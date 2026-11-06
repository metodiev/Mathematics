# Triangle Trigonometry — Solutions

> [Tutorial](README.md) · [Exercises](exercises.md) · 37 worked solutions

Each solution names the case, carries out the computation, and checks the result. Angles are given to
two decimal places; sides are given to three decimal places. Intermediate values are carried at full
precision.

## Beginner

### 1.

**Case: AAS.** The third angle is

$$C=180^\circ-42^\circ-75^\circ=63^\circ.$$

The law of sines with the known pair $(a,A)=(10,42^\circ)$ gives

$$b=\frac{a\sin B}{\sin A}=\frac{10\sin75^\circ}{\sin42^\circ}
=\frac{10(0.965926)}{0.669131}=14.436.$$

**Answer.** $b\approx14.44$.

**Check.** $\dfrac{a}{\sin A}=\dfrac{10}{0.669131}=14.945$ and
$\dfrac{b}{\sin B}=\dfrac{14.436}{0.965926}=14.945$.

### 2.

**Case: AAS.** The third angle is $C=180^\circ-30^\circ-45^\circ=105^\circ$. The law of sines gives

$$b=\frac{a\sin B}{\sin A}=\frac{24\sin45^\circ}{\sin30^\circ}
=\frac{24(0.707107)}{0.5}=33.941.$$

**Answer.** $b\approx33.94$. The side $b$ is the largest because $B=45^\circ$ is the largest angle,
and indeed $33.94>24$.

### 3.

**Case: SAS.** Use the law of cosines with the included angle $A$:

$$\begin{aligned}
a^2&=b^2+c^2-2bc\cos A\\
&=81+196-2(9)(14)\cos48^\circ\\
&=277-252(0.669131)\\
&=277-168.621=108.379.
\end{aligned}$$

Therefore $a=\sqrt{108.379}=10.411$.

**Answer.** $a\approx10.41$.

**Check.** Since $A=48^\circ$ is acute, $a^2<b^2+c^2=277$; indeed $108.379<277$.

### 4.

**Case: SSS.** Use the angle form of the law of cosines:

$$\cos C=\frac{a^2+b^2-c^2}{2ab}=\frac{25+64-100}{2(5)(8)}=\frac{-11}{80}=-0.1375.$$

Therefore

$$C=\arccos(-0.1375)=97.90^\circ.$$

**Answer.** $C\approx97.90^\circ$, obtuse.

**Check.** $c^2=100>a^2+b^2=89$, so the angle opposite $c$ must be obtuse, as found.

### 5.

**Case: SAS, area.** By Proposition 7.8,

$$K=\tfrac12ab\sin C=\tfrac12(7)(10)\sin52^\circ=35(0.788011)=27.580.$$

**Answer.** $K\approx27.58$.

**Check.** The maximum possible area for sides $7$ and $10$ is $35$, attained at $C=90^\circ$; the
value $27.58$ is plausible for $C=52^\circ$.

### 6.

**Case: SSS, area.** An equilateral triangle of side $6$ has semiperimeter $s=9$, so Heron gives

$$K=\sqrt{9\cdot3\cdot3\cdot3}=\sqrt{243}=9\sqrt3=15.588.$$

**Answer.** $K=9\sqrt3\approx15.59$.

**Check.** The standard formula $K=\dfrac{\sqrt3}{4}a^2$ gives
$\dfrac{\sqrt3}{4}(36)=9\sqrt3$, agreeing.

### 7.

**Case: SSS, area.** The semiperimeter is $s=\dfrac{6+8+10}{2}=12$, so

$$K=\sqrt{12(12-6)(12-8)(12-10)}=\sqrt{12\cdot6\cdot4\cdot2}=\sqrt{576}=24.$$

**Answer.** $K=24$.

**Check.** The triangle is right-angled because $6^2+8^2=10^2$, and
$\tfrac12(6)(8)=24$.

### 8.

**Case: SSS, area.** The semiperimeter is $s=\dfrac{9+10+17}{2}=18$, so

$$K=\sqrt{18(18-9)(18-10)(18-17)}=\sqrt{18\cdot9\cdot8\cdot1}=\sqrt{1296}=36.$$

**Answer.** $K=36$.

**Check.** The area is small relative to the sides because the triangle is nearly degenerate:
$9+10=19$ is only just larger than $17$.

### 9.

**Case: AAS, circumradius.** By the extended law of sines,

$$R=\frac{a}{2\sin A}=\frac{13}{2\sin50^\circ}=\frac{13}{1.532089}=8.485.$$

**Answer.** $R\approx8.49$.

**Check.** $2R\sin50^\circ=16.970(0.766044)=13.000=a$.

### 10.

**Case: ASA.** The third angle is

$$C=180^\circ-80^\circ-40^\circ=60^\circ.$$

The largest angle is $A=80^\circ$, so the longest side is the side opposite $A$, namely $a$.

**Answer.** $C=60^\circ$; the longest side is $a$.

**Check.** The angles in increasing order are $B=40^\circ$, $C=60^\circ$, $A=80^\circ$, so the sides
in increasing order are $b<c<a$.

### 11.

**Case: SSA.** The law of sines gives

$$\sin B=\frac{b\sin A}{a}=\frac{9\sin60^\circ}{14}=\frac{9(0.866025)}{14}=0.556731.$$

The two candidates are $B_1=33.83^\circ$ and $B_2=180^\circ-33.83^\circ=146.17^\circ$. The second is
impossible because $A+B_2=60^\circ+146.17^\circ=206.17^\circ>180^\circ$. Hence $B=33.83^\circ$ and

$$C=180^\circ-60^\circ-33.83^\circ=86.17^\circ.$$

**Answer.** $B\approx33.83^\circ$ (one triangle).

**Check.** Here $a=14>b=9$, which is the one-solution row $a\ge b$ of the table in Section 7.4.

### 12.

**Case: SAS with a right angle.** The angle at $P$ between the two bearings is
$160^\circ-70^\circ=90^\circ$. Therefore triangle $PQR$ is right-angled at $P$, and

$$QR^2=PQ^2+PR^2=12^2+8^2=144+64=208,$$

so $QR=\sqrt{208}=4\sqrt{13}=14.422$ km.

**Answer.** $QR\approx14.42$ km.

**Check.** $4\sqrt{13}=14.4222$, and $14.4222^2=208.0$.

## Intermediate

### 13.

**Case: SSA, no solution.** The law of sines would require

$$\sin B=\frac{b\sin A}{a}=\frac{12\sin35^\circ}{6}=\frac{12(0.573576)}{6}=1.14715.$$

Since $\sin B$ cannot exceed $1$, no angle $B$ exists and therefore no triangle exists.

**Alternative view.** The perpendicular distance from $C$ to the line $AB$ is
$h=b\sin A=12(0.573576)=6.883$. The side $a=6$ is shorter than $h$, so the circle of radius $a$
about $C$ does not reach the line through $A$ at all.

### 14.

**Case: SAS.** First find $a$:

$$\begin{aligned}
a^2&=b^2+c^2-2bc\cos A\\
&=256+400-2(16)(20)\cos65^\circ\\
&=656-640(0.422618)\\
&=656-270.476=385.524,
\end{aligned}$$

so $a=19.635$.

For $B$, use the law of cosines so that no ambiguity is possible:

$$\cos B=\frac{a^2+c^2-b^2}{2ac}=\frac{385.524+400-256}{2(19.635)(20)}
=\frac{529.524}{785.400}=0.674210,$$

so $B=47.61^\circ$. Then

$$C=180^\circ-65^\circ-47.61^\circ=67.39^\circ.$$

**Answer.** $a\approx19.64$, $B\approx47.61^\circ$, $C\approx67.39^\circ$.

**Check.** $\dfrac{a}{\sin A}=\dfrac{19.635}{0.906308}=21.665$;
$\sin47.61^\circ=0.73853$, so $\dfrac{b}{\sin B}=\dfrac{16}{0.73853}=21.665$; and
$\dfrac{c}{\sin C}=\dfrac{20}{0.92317}=21.665$. All three ratios agree.

### 15.

**Case: SSS.** The largest side is $a=9$, so compute $A$ first with the law of cosines:

$$\cos A=\frac{b^2+c^2-a^2}{2bc}=\frac{49+25-81}{2(7)(5)}=\frac{-7}{70}=-0.1,$$

so $A=95.74^\circ$.

For $B$:

$$\cos B=\frac{a^2+c^2-b^2}{2ac}=\frac{81+25-49}{2(9)(5)}=\frac{57}{90}=0.633333,$$

so $B=50.70^\circ$. Then

$$C=180^\circ-95.74^\circ-50.70^\circ=33.56^\circ.$$

**Answer.** $A\approx95.74^\circ$, $B\approx50.70^\circ$, $C\approx33.56^\circ$.

**Check.** The angles sum to $180.00^\circ$, and the largest angle is opposite the largest side.

### 16.

**Case: ASA.** The third angle is $C=180^\circ-48^\circ-57^\circ=75^\circ$. The law of sines gives

$$a=\frac{c\sin A}{\sin C}=\frac{20\sin48^\circ}{\sin75^\circ}
=\frac{20(0.743145)}{0.965926}=15.387,$$

$$b=\frac{c\sin B}{\sin C}=\frac{20\sin57^\circ}{\sin75^\circ}
=\frac{20(0.838671)}{0.965926}=17.365.$$

**Answer.** $C=75^\circ$, $a\approx15.39$, $b\approx17.37$.

**Check.** The sides in increasing order are $a<b<c$, matching the angles
$A=48^\circ<B=57^\circ<C=75^\circ$.

### 17.

**Case: SSS, area.** The semiperimeter is $s=\dfrac{9+12+15}{2}=18$, so

$$K=\sqrt{18(18-9)(18-12)(18-15)}=\sqrt{18\cdot9\cdot6\cdot3}=\sqrt{2916}=54.$$

**Answer.** $K=54$.

**Check.** The triangle is right-angled ($9^2+12^2=15^2$), and $\tfrac12(9)(12)=54$.

### 18.

**Case: SSS, area.** The semiperimeter is $s=\dfrac{7+8+13}{2}=14$, so

$$K=\sqrt{14(14-7)(14-8)(14-13)}=\sqrt{14\cdot7\cdot6\cdot1}=\sqrt{588}=24.249.$$

**Answer.** $K\approx24.25$.

**Check.** Using the angle form, $\cos C=\dfrac{49+64-169}{2(7)(8)}=\dfrac{-56}{112}=-0.5$, so
$C=120^\circ$ and $K=\tfrac12(7)(8)\sin120^\circ=28(0.866025)=24.249$.

### 19.

**Case: SSS, area then circumradius.** The semiperimeter is $s=\dfrac{5+6+7}{2}=9$, so

$$K=\sqrt{9(9-5)(9-6)(9-7)}=\sqrt{9\cdot4\cdot3\cdot2}=\sqrt{216}=14.697.$$

Then

$$R=\frac{abc}{4K}=\frac{5\cdot6\cdot7}{4(14.697)}=\frac{210}{58.788}=3.572.$$

**Answer.** $R\approx3.57$.

**Check.** The extended law of sines gives
$\sin A=\dfrac{5}{2(3.572)}=0.6999$, so $A\approx44.4^\circ$; then
$\dfrac{6}{\sin B}=2R=7.144$ gives $\sin B=0.8399$ and $B\approx57.1^\circ$; then
$C\approx78.5^\circ$ and $\dfrac{7}{\sin78.5^\circ}=7.144$, consistent.

### 20.

**Case: SAS with a right angle.** At $Q$, the back bearing of $PQ$ is
$025^\circ+180^\circ=205^\circ$, and the forward bearing to $R$ is $115^\circ$. Hence

$$\angle PQR=205^\circ-115^\circ=90^\circ.$$

Therefore

$$PR^2=12^2+5^2=144+25=169,\qquad PR=13\ \text{km}.$$

For the bearing, use compass coordinates:

$$Q=(12\sin25^\circ,\ 12\cos25^\circ)=(5.0714,\ 10.8757),$$

$$R=Q+(5\sin115^\circ,\ 5\cos115^\circ)=(5.0714+4.5315,\ 10.8757-2.1131)=(9.6029,\ 8.7626).$$

The bearing of $R$ from $P$ is

$$\beta=\arctan\frac{\text{east}}{\text{north}}=\arctan\frac{9.6029}{8.7626}=47.62^\circ.$$

**Answer.** $PR=13$ km, bearing $047.6^\circ$.

**Check.** The angle at $P$ is $\arctan(5/12)=22.62^\circ$, and $25^\circ+22.62^\circ=47.62^\circ$.
Also $\sqrt{9.6029^2+8.7626^2}=\sqrt{92.22+76.78}=\sqrt{169}=13$.

### 21.

**Case: two forces.** By Proposition 7.13, with $\theta=120^\circ$,

$$\begin{aligned}
R^2&=50^2+80^2+2(50)(80)\cos120^\circ\\
&=2500+6400+8000(-0.5)\\
&=8900-4000=4900,
\end{aligned}$$

so $R=70$ N.

Let $\alpha$ be the angle between the resultant and the $80$ N force. By the law of sines in the
force triangle,

$$\sin\alpha=\frac{50\sin120^\circ}{70}=\frac{50(0.866025)}{70}=0.618589,$$

so $\alpha=38.21^\circ$.

**Answer.** $R=70$ N, at $38.21^\circ$ to the $80$ N force and $120^\circ-38.21^\circ=81.79^\circ$
to the $50$ N force.

**Check.** The force triangle has angles $60^\circ$ (supplement of $120^\circ$), $38.21^\circ$ and
$81.79^\circ$, summing to $180^\circ$.

### 22.

**Case: two forces.** With $\theta=50^\circ$,

$$\begin{aligned}
R^2&=20^2+30^2+2(20)(30)\cos50^\circ\\
&=400+900+1200(0.642788)\\
&=1300+771.345=2071.345,
\end{aligned}$$

so $R=45.512$ N.

The angle $\alpha$ with the $30$ N force satisfies

$$\sin\alpha=\frac{20\sin50^\circ}{45.512}=\frac{20(0.766044)}{45.512}=0.336617,$$

so $\alpha=19.67^\circ$.

**Answer.** $R\approx45.51$ N, at $19.67^\circ$ to the $30$ N force.

**Check.** The resultant is closer to the larger force, and $19.67^\circ<25^\circ$, the halfway
direction, as expected.

### 23.

**Case: SAS with a right angle.** The angle at $P$ is $145^\circ-55^\circ=90^\circ$, so

$$LS^2=18^2+24^2=324+576=900,\qquad LS=30\ \text{km}.$$

**Answer.** $LS=30$ km.

**Check.** The sides $18$, $24$, $30$ are $3$ times $6$, $8$, $10$, a right triangle.

### 24.

**Case: SSS, area.** The semiperimeter is $s=\dfrac{10+10+12}{2}=16$, so

$$K=\sqrt{16(16-10)(16-10)(16-12)}=\sqrt{16\cdot6\cdot6\cdot4}=\sqrt{2304}=48.$$

**Answer.** $K=48$.

**Check.** The altitude to the base of length $12$ has length $\sqrt{10^2-6^2}=8$, so
$K=\tfrac12(12)(8)=48$.

## Advanced

### 25.

**Claim.** In every triangle $ABC$,
$$\frac{a}{\sin A}=\frac{b}{\sin B}=\frac{c}{\sin C}.$$

**Proof.** Drop the perpendicular from $C$ to the line $AB$, and let $D$ be the foot; write
$h=\lvert CD\rvert$.

*Case 1: $D$ lies between $A$ and $B$.* Then the triangles $ACD$ and $BCD$ are right-angled at $D$,
with hypotenuse $AC=b$ and $BC=a$ respectively. The angle at $A$ in triangle $ACD$ is $A$, and the
angle at $B$ in triangle $BCD$ is $B$. Therefore

$$h=b\sin A,\qquad h=a\sin B.$$

Equating,

$$b\sin A=a\sin B\quad\Longrightarrow\quad \frac{a}{\sin A}=\frac{b}{\sin B},$$

because $\sin A$ and $\sin B$ are positive for angles of a triangle.

*Case 2: $A$ is obtuse.* Then $D$ lies on the extension of $AB$ beyond $A$. In the right triangle
$ACD$ the interior angle at $A$ is $\pi-A$, so

$$h=b\sin(\pi-A)=b\sin A$$

by the supplement identity. The right triangle $BCD$ is unchanged, with angle $B$ at $B$, so
$h=a\sin B$. Equating gives the same result. The case in which $B$ is obtuse is symmetric.

*Case 3: $A=\pi/2$.* Then the altitude from $C$ to $AB$ has length $b$ (since $AC\perp AB$), and
$h=b=b\sin A$; also $h=a\sin B$ because $BCD$ is right-angled at $B$ with hypotenuse $a$. The
conclusion is unchanged.

Repeating the whole argument with the altitude dropped from $A$ (to the line $BC$) gives
$\dfrac{b}{\sin B}=\dfrac{c}{\sin C}$. Hence all three ratios are equal. $\blacksquare$

**Remark.** The proof uses only right-triangle trigonometry and the supplement identity
$\sin(\pi-\theta)=\sin\theta$; no area formula and no law of cosines are needed.

### 26.

**Claim.** For a triangle $ABC$ with circumradius $R$,
$$\frac{a}{\sin A}=2R.$$

**Proof.** Let $O$ be the centre of the circumcircle and $M$ the midpoint of the chord $BC$. Since
$OB=OC=R$, the triangle $OBC$ is isosceles, and $OM$ is perpendicular to $BC$; therefore
$BM=MC=a/2$ and triangle $BOM$ is right-angled at $M$ with hypotenuse $OB=R$.

Let $\psi=\angle BOC$ be the central angle subtending the chord $BC$ on the side of $A$. By the
inscribed angle theorem, the inscribed angle $A$ is half of $\psi$ when $O$ and $A$ lie on the same
side of $BC$, that is $\psi=2A$ for $A$ acute. (The inscribed angle theorem follows from the
isosceles triangles formed by the radii: the two base angles are equal, and the exterior angle at $O$
is the sum of the two, which gives the factor of two.)

*If $A$ is acute,* then $\angle BOM=\psi/2=A$, and in the right triangle $BOM$,

$$\sin A=\frac{BM}{OB}=\frac{a/2}{R},$$

so $a=2R\sin A$.

*If $A$ is obtuse,* the inscribed angle subtends the major arc $BC$, and the central angle of the
minor arc is $\psi=2\pi-2A$. Then $\angle BOM=\pi-A$, and

$$\sin(\pi-A)=\frac{a/2}{R},$$

which again gives $a=2R\sin A$ because $\sin(\pi-A)=\sin A$.

*If $A=\pi/2$,* then $BC$ is a diameter, so $a=2R=2R\sin A$.

The same argument at $B$ and at $C$ gives $b=2R\sin B$ and $c=2R\sin C$; dividing by the sines
completes the proof. $\blacksquare$

### 27.

**Claim.** $a^2=b^2+c^2-2bc\cos A$.

**Proof.** Drop the altitude from $A$ to the line $BC$ and let $D$ be its foot. Write
$x=\lvert CD\rvert$ and $h=\lvert AD\rvert$.

In the right triangle $ACD$, the angle at $C$ is $C$, so

$$x=b\cos C,\qquad h=b\sin C.$$

In the right triangle $ABD$, the hypotenuse is $AB=c$ and the leg $AD=h$, so

$$c^2=h^2+\lvert BD\rvert^2.$$

The length $\lvert BD\rvert$ depends on the position of $D$:

* if $D$ lies between $B$ and $C$, then $\lvert BD\rvert=a-x=a-b\cos C$;
* if $C$ is obtuse, then $D$ lies beyond $C$ and $\lvert BD\rvert=a+x=a+b\lvert\cos C\rvert$; since
  $\cos C<0$, this is again $a-b\cos C$;
* if $B$ is obtuse, then $D$ lies beyond $B$, $x>a$, and $\lvert BD\rvert=x-a=-(a-b\cos C)$; the
  square removes the sign.

In every case,

$$\begin{aligned}
c^2&=h^2+(a-b\cos C)^2\\
&=b^2\sin^2C+a^2-2ab\cos C+b^2\cos^2C\\
&=a^2+b^2-2ab\cos C,
\end{aligned}$$

using $\sin^2C+\cos^2C=1$. Relabelling the vertices gives the other two forms. $\blacksquare$

### 28.

**Claim.** With $s=\tfrac12(a+b+c)$, the area satisfies
$$K=\sqrt{s(s-a)(s-b)(s-c)}.$$

**Derivation.** From $K=\tfrac12ab\sin C$,

$$16K^2=4a^2b^2\sin^2C=4a^2b^2(1-\cos^2C)=4a^2b^2-(2ab\cos C)^2.$$

The law of cosines gives $2ab\cos C=a^2+b^2-c^2$, so

$$16K^2=4a^2b^2-(a^2+b^2-c^2)^2.$$

Factor the difference of squares with $X=2ab$ and $Y=a^2+b^2-c^2$:

$$\begin{aligned}
16K^2&=(2ab-a^2-b^2+c^2)(2ab+a^2+b^2-c^2)\\
&=\bigl(c^2-(a-b)^2\bigr)\bigl((a+b)^2-c^2\bigr)\\
&=(c-a+b)(c+a-b)(a+b-c)(a+b+c).
\end{aligned}$$

Each factor is twice a semiperimeter difference:

$$c-a+b=2(s-a),\quad c+a-b=2(s-b),\quad a+b-c=2(s-c),\quad a+b+c=2s.$$

Therefore $16K^2=16s(s-a)(s-b)(s-c)$, and since $K>0$,

$$K=\sqrt{s(s-a)(s-b)(s-c)}. \qquad\blacksquare$$

**Remark.** The identity $16K^2=16s(s-a)(s-b)(s-c)$ is a polynomial identity in $a,b,c$; it can be
verified by expanding both sides, which is a useful independent check of the algebra.

### 29.

**Claim.** $K=\dfrac{abc}{4R}$.

**Proof.** The extended law of sines (Problem 26) gives $a=2R\sin A$, hence
$\sin A=\dfrac{a}{2R}$. The area formula with sides $b$ and $c$ and included angle $A$ gives

$$K=\tfrac12bc\sin A=\tfrac12bc\cdot\frac{a}{2R}=\frac{abc}{4R}. \qquad\blacksquare$$

**Check.** Problem 37 gives an instance: for sides $5$, $7$, $8$, $abc=280$, $R=\dfrac{7}{\sqrt3}$ and
$K=10\sqrt3$, so $4RK=4\cdot\dfrac{7}{\sqrt3}\cdot10\sqrt3=280=abc$.

### 30.

**Case: SSA.** Here $a=7$, $b=8$, $A=30^\circ$, so

$$\sin B=\frac{b\sin A}{a}=\frac{8\sin30^\circ}{7}=\frac{4}{7}=0.571429.$$

The two candidates are

$$B_1=\arcsin\left(\frac47\right)=34.85^\circ,\qquad B_2=180^\circ-34.85^\circ=145.15^\circ.$$

**Testing the candidates.**

* $A+B_1=64.85^\circ<180^\circ$: valid.
* $A+B_2=175.15^\circ<180^\circ$: also valid.

So there are **two** triangles. (Equivalently, $h=b\sin A=4$, and $4<7<8$, the two-solution row.)

**First triangle.** $B=34.85^\circ$, $C=180^\circ-30^\circ-34.85^\circ=115.15^\circ$, and

$$c=\frac{a\sin C}{\sin A}=\frac{7\sin115.15^\circ}{0.5}=14(0.90518)=12.673.$$

**Second triangle.** $B=145.15^\circ$, $C=180^\circ-30^\circ-145.15^\circ=4.85^\circ$, and

$$c=\frac{7\sin4.85^\circ}{0.5}=14(0.08455)=1.184.$$

**Answer.**

| Solution | $B$ | $C$ | $c$ |
|---|---|---|---|
| 1 | $34.85^\circ$ | $115.15^\circ$ | $12.673$ |
| 2 | $145.15^\circ$ | $4.85^\circ$ | $1.184$ |

**Check.** Both triangles have $a=7$, $b=8$ and $A=30^\circ$ by construction. The second is extremely
thin, with $C$ under $5^\circ$, which is why $c$ is barely more than $1$.

### 31.

**Case: vector addition (wind triangle).** The wind is *from* $160^\circ$, so it blows *toward*
$340^\circ$. Use compass coordinates with east as $x$ and north as $y$.

Aircraft air velocity:

$$(200\sin70^\circ,\ 200\cos70^\circ)=(187.939,\ 68.404).$$

Wind velocity:

$$(40\sin340^\circ,\ 40\cos340^\circ)=(-13.681,\ 37.588).$$

Ground velocity:

$$(187.939-13.681,\ 68.404+37.588)=(174.258,\ 105.992).$$

Ground speed:

$$\sqrt{174.258^2+105.992^2}=\sqrt{30365.8+11234.3}=\sqrt{41600.1}=203.961\ \text{km/h}.$$

Track:

$$\arctan\frac{174.258}{105.992}=58.69^\circ.$$

**Answer.** Ground speed $204.0$ km/h, track $058.7^\circ$.

**Check.** The heading $070^\circ$ and the wind direction $340^\circ$ differ by $90^\circ$, so the
wind triangle is right-angled and the ground speed is
$\sqrt{200^2+40^2}=\sqrt{41600}=203.96$, matching. The wind pushes the aircraft to the left of its
heading (from $070^\circ$ to $058.7^\circ$), which is consistent with a wind blowing toward
$340^\circ$.

### 32.

**Claim (projection formula).** In every triangle,
$$a=b\cos C+c\cos B.$$

**Proof.** Drop the altitude from $A$ to the line $BC$ and let $D$ be its foot. Work with **signed**
lengths along the line $BC$, positive in the direction from $B$ to $C$.

In the right triangle $ABD$, the projection of $AB$ onto the line $BC$ is
$BD=c\cos B$: if $B$ is acute, $D$ lies on the ray from $B$ toward $C$ and the projection is
positive; if $B$ is obtuse, $D$ lies on the opposite ray and the signed projection is
$c\cos(\pi-B)=-c\cos B=c\cos B$, because $\cos B<0$ in that case. Either way the signed formula
$BD=c\cos B$ holds.

Similarly, in the right triangle $ACD$, the signed distance from $D$ to $C$ is $b\cos C$.

Because $D$ lies on the line $BC$, the signed segments satisfy $BD+DC=BC$, that is

$$c\cos B+b\cos C=a. \qquad\blacksquare$$

**Check.** For an obtuse angle, take $A=120^\circ$, $b=5$, $c=6$; then
$a^2=25+36-60\cos120^\circ=61+30=91$, so $a=9.539$. The law of cosines gives
$\cos B=\dfrac{a^2+c^2-b^2}{2ac}=\dfrac{91+36-25}{2(9.539)(6)}=0.8910$ and
$\cos C=\dfrac{a^2+b^2-c^2}{2ab}=\dfrac{91+25-36}{2(9.539)(5)}=0.8387$, so
$b\cos C+c\cos B=5(0.8387)+6(0.8910)=4.1935+5.3460=9.5395=a$.

### 33.

**Claim.** $a^2+b^2+c^2=2(ab\cos C+bc\cos A+ca\cos B)$.

**Proof.** Write the law of cosines three times, once for each side:

$$a^2=b^2+c^2-2bc\cos A,$$
$$b^2=c^2+a^2-2ca\cos B,$$
$$c^2=a^2+b^2-2ab\cos C.$$

Adding the three equations, the left side is $a^2+b^2+c^2$ and the right side is

$$2(a^2+b^2+c^2)-2(bc\cos A+ca\cos B+ab\cos C).$$

Hence

$$a^2+b^2+c^2=2(a^2+b^2+c^2)-2(bc\cos A+ca\cos B+ab\cos C),$$

and subtracting $a^2+b^2+c^2$ from both sides gives

$$0=(a^2+b^2+c^2)-2(bc\cos A+ca\cos B+ab\cos C),$$

which is the claim. $\blacksquare$

**Check.** For the triangle $7,9,11$: the left side is $49+81+121=251$. The angles satisfy
$\cos A=\dfrac{81+121-49}{2(9)(11)}=0.77273$, $\cos B=\dfrac{49+121-81}{2(7)(11)}=0.57792$ and
$\cos C=\dfrac{49+81-121}{2(7)(9)}=0.07143$. Then
$2(7\cdot9(0.07143)+9\cdot11(0.77273)+11\cdot7(0.57792))=2(4.5+76.5+44.5)=251$.

## Challenge

### 34.

**Strategy.** The angle $C$ is included between the sides $a=2x$ and $b=x+1$, so the law of cosines
gives an equation for $x$ alone.

$$c^2=a^2+b^2-2ab\cos C.$$

Substituting $c=3$, $a=2x$, $b=x+1$ and $\cos60^\circ=\tfrac12$:

$$\begin{aligned}
9&=(2x)^2+(x+1)^2-2(2x)(x+1)\cdot\tfrac12\\
&=4x^2+x^2+2x+1-2x^2-2x\\
&=3x^2+1.
\end{aligned}$$

Therefore $3x^2=8$, so

$$x=\sqrt{\frac83}=\frac{2\sqrt6}{3}=1.633.$$

The negative root is rejected because a side length must be positive.

**Sides.** $a=2x=3.266$, $b=x+1=2.633$, $c=3$.

**Triangle inequality.** $a+b=5.899>3$; $a+c=6.266>2.633$; $b+c=5.633>3.266$. All three hold, so the
triangle exists.

**Check.** With these sides,
$\cos C=\dfrac{a^2+b^2-c^2}{2ab}=\dfrac{10.667+6.933-9}{2(3.266)(2.633)}=\dfrac{8.600}{17.199}=0.5$,
so $C=60^\circ$.

**Answer.** $x=\dfrac{2\sqrt6}{3}\approx1.633$.

### 35.

**Strategy.** Replace every side by $2R$ times the sine of the opposite angle, then use sum-to-product
and the triangle identity for half-angles.

$$\begin{aligned}
\frac{a+b}{c}
&=\frac{2R\sin A+2R\sin B}{2R\sin C}\\
&=\frac{\sin A+\sin B}{\sin C}\\
&=\frac{2\sin\dfrac{A+B}{2}\cos\dfrac{A-B}{2}}{2\sin\dfrac{C}{2}\cos\dfrac{C}{2}}.
\end{aligned}$$

Because $A+B=\pi-C$, we have $\dfrac{A+B}{2}=\dfrac{\pi}{2}-\dfrac{C}{2}$, so
$\sin\dfrac{A+B}{2}=\cos\dfrac{C}{2}$. Substituting,

$$\frac{a+b}{c}
=\frac{2\cos\dfrac{C}{2}\cos\dfrac{A-B}{2}}{2\sin\dfrac{C}{2}\cos\dfrac{C}{2}}
=\frac{\cos\dfrac{A-B}{2}}{\sin\dfrac{C}{2}}. \qquad\blacksquare$$

**Check.** For an equilateral triangle, $\dfrac{a+b}{c}=2$ and
$\dfrac{\cos0}{\sin30^\circ}=\dfrac{1}{0.5}=2$.

### 36.

**Strategy.** Express the ratio $a/b$ in two ways: by the law of sines (using $A=2B$) and by the law
of cosines for $b$. Eliminate $\cos B$.

By the law of sines,

$$\frac{a}{b}=\frac{\sin A}{\sin B}=\frac{\sin 2B}{\sin B}=\frac{2\sin B\cos B}{\sin B}=2\cos B,$$

so $\cos B=\dfrac{a}{2b}$.

By the law of cosines applied to the side $b$,

$$b^2=a^2+c^2-2ac\cos B.$$

Substituting $\cos B=\dfrac{a}{2b}$:

$$b^2=a^2+c^2-2ac\cdot\frac{a}{2b}=a^2+c^2-\frac{a^2c}{b}.$$

Multiply by $b$:

$$b^3=a^2b+c^2b-a^2c.$$

Rearrange to group the terms containing $a^2$:

$$a^2(c-b)=b(c^2-b^2)=b(c-b)(c+b).$$

Since $A=2B$ and $A+B<180^\circ$, we have $B<60^\circ$, so $A\ne B$ and therefore $c\ne b$. Dividing
by the nonzero factor $c-b$,

$$a^2=b(b+c). \qquad\blacksquare$$

**Check.** Take $B=40^\circ$, $A=80^\circ$, $C=60^\circ$. Then
$\dfrac{a}{b}=\dfrac{\sin80^\circ}{\sin40^\circ}=1.5321$, and
$\dfrac{b+c}{b}=1+\dfrac{\sin60^\circ}{\sin40^\circ}=1+1.3473=2.3473$; the product
$b(b+c)=2.3473b^2$ should equal $a^2=(1.5321b)^2=2.3473b^2$, which it does.

### 37.

**Area.** The semiperimeter is $s=\dfrac{5+7+8}{2}=10$, so

$$K=\sqrt{10(10-5)(10-7)(10-8)}=\sqrt{10\cdot5\cdot3\cdot2}=\sqrt{300}=10\sqrt3=17.321.$$

**Inradius.**

$$r=\frac{K}{s}=\frac{10\sqrt3}{10}=\sqrt3=1.732.$$

**Circumradius.**

$$R=\frac{abc}{4K}=\frac{5\cdot7\cdot8}{4\cdot10\sqrt3}=\frac{280}{40\sqrt3}=\frac{7}{\sqrt3}
=\frac{7\sqrt3}{3}=4.041.$$

**Verification of $K=rs$.**

$$rs=10\cdot\sqrt3=10\sqrt3=K.$$

**Verification of $abc=4RK$.**

$$4RK=4\cdot\frac{7}{\sqrt3}\cdot10\sqrt3=280=5\cdot7\cdot8=abc.$$

**Answer.** $K=10\sqrt3\approx17.32$, $r=\sqrt3\approx1.73$, $R=\dfrac{7}{\sqrt3}\approx4.04$.

**Check.** The largest angle is opposite the side $8$:
$\cos C=\dfrac{25+49-64}{2(5)(7)}=\dfrac{10}{70}=0.14286$, so $C=81.79^\circ$. Then
$\sin C=0.98974$ and $2R\sin C=8.082(0.98974)=8.000$, as required.
