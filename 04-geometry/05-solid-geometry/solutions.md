# Solid Geometry — Solutions

> [Tutorial](README.md) · [Exercises](exercises.md) · 36 worked solutions

Each solution states the strategy, carries out every significant step, and checks the result. Volumes
are in cubic units, areas in square units; the units are written out wherever a number could be
ambiguous.

## Beginner

### Solution 1

**Strategy.** All three questions follow directly from the box formulas $V=lwh$, $A=2(lw+lh+wh)$ and
$d=\sqrt{l^2+w^2+h^2}$.

**Volume.**
$$V=5\cdot4\cdot3=60\ \mathrm{cm^3}.$$

**Surface area.** The three pairs of faces have areas $5\cdot4=20$, $5\cdot3=15$ and $4\cdot3=12$:
$$A=2(20+15+12)=2\cdot47=94\ \mathrm{cm^2}.$$

**Space diagonal.**
$$d=\sqrt{5^2+4^2+3^2}=\sqrt{25+16+9}=\sqrt{50}=5\sqrt2\approx7.07\ \mathrm{cm}.$$

*Check.* The diagonal must exceed the longest edge $5$ and be less than the sum of the edges $12$:
$5<7.07<12$ ✓.

### Solution 2

**Edge.** A cube of edge $a$ has surface $6a^2$, so
$$6a^2=150 \;\Longrightarrow\; a^2=25 \;\Longrightarrow\; a=5\ \mathrm{cm}.$$

**Volume.** $V=a^3=125\ \mathrm{cm^3}$.

**Diagonal.** $d=a\sqrt3=5\sqrt3\approx8.66\ \mathrm{cm}$.

*Check.* $5\sqrt3\approx8.66$ lies between $a=5$ and $3a=15$ ✓, and $d^2=75=3a^2$ ✓.

### Solution 3

**Edge.** $a^3=343$, and since $7^3=343$, $a=7\ \mathrm{cm}$.

**Surface.** $A=6a^2=6\cdot49=294\ \mathrm{cm^2}$.

*Check.* $7^3=343$ and $6\cdot7^2=294$; the ratio $A/V=294/343=6/7$, which equals $6/a$ as it must ✓.

### Solution 4

**Base.** The base is a right triangle with legs $3$ and $4$, so its area is $\tfrac12\cdot3\cdot4=6\ \mathrm{cm^2}$
and its hypotenuse is $\sqrt{3^2+4^2}=5$, giving perimeter $P=3+4+5=12\ \mathrm{cm}$.

**Volume.** $V=Bh=6\cdot10=60\ \mathrm{cm^3}$.

**Surface.** The two triangular ends contribute $2\cdot6=12$; the three rectangular sides contribute
$Ph=12\cdot10=120$. Hence
$$A=12+120=132\ \mathrm{cm^2}.$$
Check each rectangle separately: $3\cdot10=30$, $4\cdot10=40$, $5\cdot10=50$, and $30+40+50=120$ ✓.

### Solution 5

**Volume.** $V=\pi r^2h=\pi\cdot25\cdot7=175\pi\approx549.78\ \mathrm{cm^3}$.

**Lateral area.** $S_{\text{lat}}=2\pi rh=2\pi\cdot5\cdot7=70\pi\approx219.91\ \mathrm{cm^2}$.

**Total.** The two ends contribute $2\pi r^2=50\pi$, so
$$S=70\pi+50\pi=120\pi\approx376.99\ \mathrm{cm^2}.$$

*Check.* $S=2\pi r(r+h)=2\pi\cdot5\cdot12=120\pi$ ✓.

### Solution 6

**Radius first.** The diameter is $10$, so $r=5\ \mathrm{cm}$. This conversion is the whole point of the
exercise: using $10$ as the radius would give four times the volume.

**Volume.** $V=\pi\cdot25\cdot12=300\pi\approx942.48\ \mathrm{cm^3}$.

**Surface.** $S=2\pi r^2+2\pi rh=50\pi+2\pi\cdot5\cdot12=50\pi+120\pi=170\pi\approx534.07\ \mathrm{cm^2}$.

*Check.* $2\pi r(r+h)=2\pi\cdot5\cdot17=170\pi$ ✓.

### Solution 7

**Slant height.** $l=\sqrt{r^2+h^2}=\sqrt{36+64}=10\ \mathrm{cm}$.

**Volume.** $V=\tfrac13\pi r^2h=\tfrac13\pi\cdot36\cdot8=96\pi\approx301.59\ \mathrm{cm^3}$.

**Lateral area.** $S_{\text{lat}}=\pi rl=\pi\cdot6\cdot10=60\pi\approx188.50\ \mathrm{cm^2}$.

**Total.** $S=60\pi+\pi\cdot36=96\pi\approx301.59\ \mathrm{cm^2}$.

*Remark.* The numerical equality of $V$ and $S$ here is accidental: $V=\tfrac13\pi r^2h$ and
$S=\pi r(r+l)$ coincide only because $36\cdot8/3=6\cdot16$.

### Solution 8

**Surface.** $A=4\pi R^2=4\pi\cdot49=196\pi\approx615.75\ \mathrm{cm^2}$.

**Volume.** $V=\tfrac43\pi R^3=\tfrac43\pi\cdot343=\dfrac{1372\pi}{3}\approx1436.76\ \mathrm{cm^3}$.

*Check.* $V/A=R/3=7/3$, so $V=196\pi\cdot7/3=1372\pi/3$ ✓.

### Solution 9

**Radius.** From $\tfrac43\pi R^3=288\pi$ divide by $\pi$ and multiply by $\tfrac34$:
$$R^3=288\cdot\tfrac34=216 \;\Longrightarrow\; R=6\ \mathrm{cm}.$$

**Surface.** $A=4\pi\cdot36=144\pi\approx452.39\ \mathrm{cm^2}$.

*Check.* $V/A=R/3=2$, so $A=3V/R=3\cdot288\pi/6=144\pi$ ✓.

### Solution 10

**Base.** A regular hexagon of side $2$ is six equilateral triangles of side $2$:
$$B=6\cdot\frac{\sqrt3}{4}\cdot4=6\sqrt3\approx10.39\ \mathrm{cm^2},$$
in agreement with $B=\tfrac{3\sqrt3}{2}s^2=\tfrac{3\sqrt3}{2}\cdot4=6\sqrt3$.

**Volume.** $V=Bh=6\sqrt3\cdot5=30\sqrt3\approx51.96\ \mathrm{cm^3}$.

**Surface.** The lateral surface is six rectangles $2\times5$: $S_{\text{lat}}=6\cdot10=60$. Hence
$$S=60+2\cdot6\sqrt3=60+12\sqrt3\approx80.78\ \mathrm{cm^2}.$$

*Check.* The lateral area equals $Ph=12\cdot5=60$ ✓.

### Solution 11

**Euler.** $V-E+F=2$ gives $8-E+6=2$, so $E=12$.

**Identification.** A convex polyhedron with $8$ vertices, $12$ edges and $6$ square faces is the
**cube**. Consistency: three squares per vertex give $qV=3\cdot8=24=2E$ ✓.

### Solution 12

**Euler.** $6-12+F=2$ gives $F=8$.

**Identification.** Eight triangular faces and six vertices: the **regular octahedron**. Consistency:
$3F=24=2E$ ✓ and $qV$ with $q=4$ gives $4\cdot6=24=2E$ ✓.

### Solution 13

**Count.** The base contributes its $4$ vertices and $4$ edges; the apex adds $1$ vertex; the four
lateral edges join the apex to the base. So
$$V=4+1=5,\qquad E=4+4=8,\qquad F=1+4=5 .$$

**Euler.** $5-8+5=2$ ✓.

*Remark.* The count "$E=8$" is easy to get wrong by counting the base edges twice or by forgetting the
lateral edges; the Euler check is a cheap way to detect such an error, because the answer must be $2$
for any polyhedron built this way.

## Intermediate

### Solution 14

**Height.** A regular square pyramid has the apex above the centre of the base; the apothem of the base
is half the side, $5$. The height, the apothem and the slant height form a right triangle with the slant
height as hypotenuse:
$$h=\sqrt{l^2-5^2}=\sqrt{169-25}=\sqrt{144}=12\ \mathrm{cm}.$$

**Volume.** $V=\tfrac13Bh=\tfrac13\cdot100\cdot12=400\ \mathrm{cm^3}$.

**Surface.** The base perimeter is $P=40$, so
$$S_{\text{lat}}=\tfrac12Pl=\tfrac12\cdot40\cdot13=260,\qquad S=260+100=360\ \mathrm{cm^2}.$$

*Check by faces:* each lateral face has area $\tfrac12\cdot10\cdot13=65$, and $4\cdot65=260$ ✓.

### Solution 15

**Height.** $h=\sqrt{l^2-r^2}=\sqrt{169-25}=12\ \mathrm{cm}$.

**Volume.** $V=\tfrac13\pi\cdot25\cdot12=100\pi\approx314.16\ \mathrm{cm^3}$.

**Surface.** $S_{\text{lat}}=\pi\cdot5\cdot13=65\pi$ and the base is $25\pi$, so
$$S=90\pi\approx282.74\ \mathrm{cm^2}.$$

*Check.* $S=\pi r(r+l)=\pi\cdot5\cdot18=90\pi$ ✓.

### Solution 16

**Sphere.** With $R=3$, $V_s=\tfrac43\pi\cdot27=36\pi\approx113.10\ \mathrm{cm^3}$.

**Cube.** $V_c=6^3=216\ \mathrm{cm^3}$.

**Fraction.**
$$\frac{V_s}{V_c}=\frac{36\pi}{216}=\frac{\pi}{6}\approx0.524 .$$
So the sphere fills just over half the cube.

*Why the answer is independent of the size.* Any sphere inscribed in a cube has $R=a/2$, so the ratio is
$\tfrac43\pi(a/2)^3/a^3=\pi/6$ for every cube. The cube leaves $1-\pi/6\approx47.6\%$ of its volume
empty.

### Solution 17

**Edge.** The space diagonal of the cube is a diameter of the sphere, so $a\sqrt3=2R=6\sqrt3$, giving
$a=6\ \mathrm{cm}$.

**Volumes.** $V_{\text{cube}}=216\ \mathrm{cm^3}$ and
$$V_{\text{sphere}}=\tfrac43\pi R^3=\tfrac43\pi\cdot(3\sqrt3)^3=\tfrac43\pi\cdot81\sqrt3=108\pi\sqrt3
\approx587.90\ \mathrm{cm^3}.$$
(The cube inside has the smaller volume, as it must.)

**Ratio.**
$$\frac{V_{\text{cube}}}{V_{\text{sphere}}}=\frac{216}{108\pi\sqrt3}=\frac{2}{\pi\sqrt3}
=\frac{2\sqrt3}{3\pi}\approx0.368 .$$

*Check.* $0.368<1$ ✓; the constant is again independent of scale, since both volumes scale like $a^3$.

### Solution 18

**Volume.** With $R=4$, $r=2$, $h=3$:
$$V=\tfrac13\pi h(R^2+Rr+r^2)=\tfrac13\pi\cdot3\cdot(16+8+4)=\pi\cdot28=28\pi\approx87.96\ \mathrm{cm^3}.$$

**Lateral area.** The slant height of the frustum is
$$l=\sqrt{h^2+(R-r)^2}=\sqrt{9+4}=\sqrt{13},$$
so
$$S_{\text{lat}}=\pi(R+r)l=6\pi\sqrt{13}\approx67.99\ \mathrm{cm^2}.$$

*Check.* By subtraction of cones: the full cone has height $H=\frac{Rh}{R-r}=\frac{4\cdot3}{2}=6$, so its
volume is $\tfrac13\pi\cdot16\cdot6=32\pi$ and the removed cone has height $6-3=3$ and volume
$\tfrac13\pi\cdot4\cdot3=4\pi$; $32\pi-4\pi=28\pi$ ✓.

### Solution 19

**Base radius.** The arc of the sector becomes the circumference of the base:
$$10\cdot\pi=10\pi=2\pi r \;\Longrightarrow\; r=5\ \mathrm{cm}.$$
(The semicircle has arc length $\pi l=10\pi$.)

**Height.** The slant height is the sector radius, $l=10$, so
$$h=\sqrt{l^2-r^2}=\sqrt{100-25}=\sqrt{75}=5\sqrt3\approx8.66\ \mathrm{cm}.$$

**Volume.**
$$V=\tfrac13\pi\cdot25\cdot5\sqrt3=\frac{125\pi\sqrt3}{3}\approx226.72\ \mathrm{cm^3}.$$

*Check.* The lateral area from the sector is $\tfrac12\cdot10\cdot10\pi=50\pi$, and $\pi rl=50\pi$ ✓.

### Solution 20

**Volume.** $V=\pi r^2h=\pi\cdot4\cdot3=12\pi\approx37.70\ \mathrm{m^3}$.

**Capacity.** $1\ \mathrm{m^3}=1000\ \mathrm{L}$, so the capacity is
$$12\pi\cdot1000=12\,000\pi\approx37\,699\ \mathrm{L}.$$
(Equivalently $37.7$ kilolitres, about $37.7$ tonnes of water.)

*Check.* $1\ \mathrm{m^3}=10^6\ \mathrm{cm^3}=10^6\ \mathrm{mL}=1000\ \mathrm{L}$ ✓.

### Solution 21

**From the faces.** Each edge belongs to two triangles, and each triangle has three edges, so
$$3F=2E \;\Longrightarrow\; 24=2E \;\Longrightarrow\; E=12 .$$

**From Euler.** $V-E+F=2$ gives $6-12+8=2$ ✓, so the two counts agree.

**Identification.** Six vertices, eight triangular faces and four faces at each vertex: the regular
**octahedron**.

*Remark.* If the two counts had disagreed, the data would have been inconsistent — a useful check in any
"count the edges" problem.

### Solution 22

**Edges.** $E=V+F-2=12+8-2=18$.

**Base.** A prism with an $n$-gon base has $2n$ vertices, $n+2$ faces and $3n$ edges. From $2n=12$ we get
$n=6$; then $F=6+2=8$ ✓ and $E=3\cdot6=18$ ✓. The prism is a **hexagonal prism**.

### Solution 23

**The argument.** Fold a row of squares along the edges between them. Each fold turns the next square
through $90^\circ$ about a cube edge, so consecutive squares in the row occupy consecutive faces around
one axis. After four squares the row has gone right round the cube and the fifth square would land on the
face occupied by the first; it would overlap it rather than cover a new face. A net must cover each of the
six faces exactly once, so a row can contain at most four squares.

*Consequence.* Every cube net therefore has a row of at most four squares, which is the starting point of
the classical enumeration: the $11$ nets fall into families with a row of four, of three, or of two.

### Solution 24

**Base radius.** The sector's arc becomes the base circumference:
$$\text{arc}=12\cdot\frac{2\pi}{3}=8\pi=2\pi r \;\Longrightarrow\; r=4\ \mathrm{cm}.$$

**Height.** The slant height is the sector radius, $l=12$, so
$$h=\sqrt{144-16}=\sqrt{128}=8\sqrt2\approx11.31\ \mathrm{cm}.$$

**Volume.**
$$V=\tfrac13\pi\cdot16\cdot8\sqrt2=\frac{128\pi\sqrt2}{3}\approx189.56\ \mathrm{cm^3}.$$

*Check.* $S_{\text{lat}}=\pi rl=48\pi$, and the sector area is $\tfrac12\cdot12\cdot8\pi=48\pi$ ✓.

### Solution 25

**Volumes.**
$$V_{\text{cyl}}=\pi\cdot9\cdot10=90\pi,\qquad
V_{\text{cone}}=\tfrac13\pi\cdot9\cdot4=12\pi,\qquad V=102\pi\approx320.44\ \mathrm{cm^3}.$$

**Surface.** Four parts are exposed:

* the lateral surface of the cylinder, $2\pi\cdot3\cdot10=60\pi$;
* the lateral surface of the cone, $\pi rl$ with $l=\sqrt{3^2+4^2}=5$, giving $15\pi$;
* the flat bottom, $\pi\cdot9=9\pi$;
* nothing else — the disc where the cone meets the cylinder is interior.

Hence
$$S=60\pi+15\pi+9\pi=84\pi\approx263.89\ \mathrm{cm^2}.$$

*Pitfall.* Adding the top disc of the cylinder ($9\pi$) would double count a face that is glued to the
cone's base.

## Advanced

### Solution 26

**The partition.** Let the prism have base triangle $ABC$ and top triangle $A'B'C'$, with lateral edges
$AA'$, $BB'$, $CC'$. Define
$$T_1=ABCA',\qquad T_2=A'B'BC,\qquad T_3=A'B'C'C .$$
Cutting the prism by the plane $A'BC$ leaves $T_1$ and a wedge; cutting that wedge by the plane $A'B'C$
leaves $T_2$ and $T_3$. So the three tetrahedra tile the prism and meet only along faces.

**Equal volumes.** Compare them two at a time.

* $T_1$ and $T_2$. View $T_1$ with base triangle $AA'B$ and apex $C$; view $T_2$ with base triangle
  $A'B'B$ and apex $C$. Both bases lie in the plane of the lateral face $ABB'A'$. In the parallelogram
  $ABB'A'$ the diagonal $A'B$ splits the figure into the two congruent triangles $AA'B$ and $A'B'B$. Equal
  bases in one plane with a common apex give equal volumes (same height).
* $T_2$ and $T_3$. View $T_2$ with base $B'BC$ and apex $A'$; view $T_3$ with base $B'C'C$ and apex
  $A'$. The diagonal $B'C$ splits the parallelogram $BCC'B'$ into two congruent triangles, so again the
  volumes are equal.

Therefore $V(T_1)=V(T_2)=V(T_3)=\tfrac13 V_{\text{prism}}=\tfrac13Bh$, where $B$ is the base area and $h$
the height. Since $T_1$ is a pyramid with base $ABC$ and height $h$, every triangular pyramid has volume
$\tfrac13Bh$.

**From triangles to general pyramids.** Triangulate the base polygon into triangles of areas
$B_1,\dots,B_k$, $\sum B_i=B$. Each triangle together with the apex is a tetrahedron whose height is the
distance $h$ from the apex to the base plane, the same for all. Adding,
$$V=\sum_{i=1}^{k}\tfrac13B_ih=\tfrac13h\sum_{i=1}^{k}B_i=\tfrac13Bh .$$
$\blacksquare$

### Solution 27

**Set-up.** Let the base be a disc of radius $r$ in the plane $z=0$ with centre $O$, and let the oblique
cylinder be generated by translating that disc along a vector $\mathbf{v}=(p,q,h)$ with $h>0$. Let the
right cylinder have the same base disc and height $h$, so its top disc is the translate by $(0,0,h)$.

**Cross-sections.** Cut both solids by the horizontal plane $z=y_0$ for $0\le y_0\le h$.

* In the oblique cylinder the section is the base disc translated by $\frac{y_0}{h}\mathbf{v}$; it is a
  disc of radius $r$.
* In the right cylinder the section is the base disc translated by $(0,0,y_0)$; also a disc of radius $r$.

The two sections are congruent, hence have equal area $\pi r^2$, for every height $y_0$; the sections at
heights outside $[0,h]$ are empty in both solids. By Cavalieri the volumes are equal:
$$V=\pi r^2h .$$
$\blacksquare$

### Solution 28

**Set-up.** The box has volume $x^2h=V$, so $h=\dfrac{V}{x^2}$. Its surface is
$$S=2x^2+4xh=2x^2+\frac{4V}{x}.$$

**AM–GM.** Write the last term as two equal pieces and apply $a+b+c\ge3\sqrt[3]{abc}$:
$$S=2x^2+\frac{2V}{x}+\frac{2V}{x}\ \ge\ 3\sqrt[3]{2x^2\cdot\frac{2V}{x}\cdot\frac{2V}{x}}
=3\sqrt[3]{8V^2}=6V^{2/3}.$$

**Equality.** Equality in AM–GM holds exactly when the three terms are equal:
$$2x^2=\frac{2V}{x} \;\Longrightarrow\; x^3=V \;\Longrightarrow\; x=\sqrt[3]{V},$$
and then $h=V/x^2=x$. So the box is a cube of edge $\sqrt[3]{V}$, and its surface is
$6V^{2/3}$, the minimum. $\blacksquare$

*Remark.* The same conclusion follows by differentiating $S$ with respect to $x$ and setting
$S'=4x-4V/x^2$ to zero, which again gives $x^3=V$.

### Solution 29

**The inequality.** From Lemma 7.3, a Platonic solid with regular $p$-gons and $q$ faces at each vertex
must satisfy
$$(p-2)(q-2)<4,\qquad p\ge3,\ q\ge3 .$$

**No hexagonal faces.** For $p=6$ the interior angle is $120^\circ$, so the angle condition reads
$q\cdot120^\circ<360^\circ$, i.e. $q<3$, which contradicts $q\ge3$. Equivalently
$(p-2)(q-2)=4(q-2)\ge4$, so the strict inequality fails.

**No faces with $p\ge7$.** For $p\ge7$ the interior angle is
$\frac{(p-2)180^\circ}{p}\ge\frac{5\cdot180^\circ}{7}\approx128.6^\circ>120^\circ$, so even the minimum
$q=3$ gives a sum above $360^\circ$. Equivalently $(p-2)(q-2)\ge5\cdot1=5>4$.

**Conclusion.** Only $p\in\{3,4,5\}$ is possible, and for each the inequality restricts $q$ to exactly the
values in Theorem 7.4. $\blacksquare$

### Solution 30

**Height.** Let the tetrahedron be $ABCD$ with all edges $a$, and let $M$ be the centroid of the base
$BCD$. In the equilateral base the distance from $M$ to a vertex is the circumradius
$$R_{\text{base}}=\frac{a}{\sqrt3},$$
as follows from $a=2R_{\text{base}}\sin60^\circ=R_{\text{base}}\sqrt3$. The segment $AM$ is perpendicular
to the base, so Pythagoras in the right triangle $AMB$ gives
$$h^2=a^2-R_{\text{base}}^2=a^2-\frac{a^2}{3}=\frac{2a^2}{3},\qquad h=a\sqrt{\frac23}.$$

**Volume.** The base area is $\frac{\sqrt3}{4}a^2$, so
$$V=\tfrac13\cdot\frac{\sqrt3}{4}a^2\cdot a\sqrt{\frac23}
=\frac{a^3}{12}\sqrt3\cdot\sqrt{\frac23}
=\frac{a^3}{12}\sqrt{2}=\frac{a^3}{6\sqrt2}.$$
(The last equality multiplies numerator and denominator by $\sqrt2$: $\frac{\sqrt2}{12}=\frac{1}{6\sqrt2}$.)

*Check.* For $a=2$: $h=2\sqrt{2/3}\approx1.633$ and $V=8/(6\sqrt2)=4/(3\sqrt2)\approx0.943$. Directly,
$\tfrac13\cdot\sqrt3\cdot1.633\approx0.943$ ✓. $\blacksquare$

### Solution 31

**The two pyramids.** Place the octahedron with vertices $(\pm c,0,0)$, $(0,\pm c,0)$, $(0,0,\pm c)$.
The distance between two adjacent vertices such as $(c,0,0)$ and $(0,c,0)$ is $c\sqrt2$, so $c=a/\sqrt2$.
The four vertices with $z=0$ form a square of side $c\sqrt2=a$, hence of area $a^2$. Together with the
vertex $(0,0,c)$ they form a square pyramid of height $c$; together with $(0,0,-c)$ they form a congruent
pyramid on the other side. The two pyramids share the square base and fill the octahedron.

**Volume.**
$$V=2\cdot\tfrac13\cdot a^2\cdot c=\tfrac23a^2\cdot\frac{a}{\sqrt2}=\frac{2a^3}{3\sqrt2}=\frac{\sqrt2}{3}a^3 .$$

*Check.* For $a=\sqrt2$ (the unit-coordinate octahedron), $V=\frac{\sqrt2}{3}\cdot2\sqrt2=\frac43$, and
directly $2\cdot\tfrac13\cdot2\cdot1=\frac43$ ✓. $\blacksquare$

### Solution 32

**At most six sides.** A segment of the section lies in a face of the cube. A plane that is not parallel
to a face meets each of the six faces in at most one segment (parallel planes meet in nothing or in a
whole line, the degenerate case), so at most six segments form the boundary. Hence the section has at
most six sides.

**No regular pentagon.** Suppose the section is a pentagon. Five sides lie in five distinct faces, so the
plane misses exactly one of the six faces. The six faces of a cube form three pairs of parallel faces, and
a plane cuts two parallel planes in parallel lines (if it cuts both). Missing one face means that one pair
contributes only one cut, while the other two pairs contribute two cuts each. Therefore the pentagon has
**two pairs of parallel sides**.

A regular pentagon has no pair of parallel sides: its sides turn by the exterior angle $72^\circ$, and two
sides are parallel exactly when the number of turns between them is a multiple of $180^\circ$, i.e. a
multiple of $180/72=2.5$ steps, impossible in whole steps. So a regular pentagon cannot occur.
$\blacksquare$

## Challenge

### Solution 33

**The two solids.** Let the hemisphere be
$$H=\{(x,y,z):x^2+y^2+z^2\le R^2,\ y\ge0\}$$
with its flat face on the plane $y=0$. Let the cylinder be $C=\{x^2+z^2\le R^2,\ 0\le y\le R\}$ and the
cone be $K=\{x^2+z^2\le y^2,\ 0\le y\le R\}$, whose apex is the origin (the centre of the cylinder's base)
and whose base circle at height $R$ has radius $R$. Both $H$ and $C\setminus K$ lie between the planes
$y=0$ and $y=R$.

**Section of the hemisphere at height $y$.** A point of $H$ with second coordinate $y$ satisfies
$x^2+z^2\le R^2-y^2$, so the section is a disc of area
$$A_H(y)=\pi(R^2-y^2).$$

**Section of the cylinder minus the cone at height $y$.** The cylinder contributes the disc
$x^2+z^2\le R^2$, of area $\pi R^2$. The cone at height $y$ satisfies $x^2+z^2\le y^2$, a disc of area
$\pi y^2$. Hence
$$A_{C\setminus K}(y)=\pi R^2-\pi y^2=\pi(R^2-y^2)=A_H(y).$$

**Cavalieri.** The sections have equal areas for every $y\in[0,R]$ and both solids are empty outside that
range, so $V(H)=V(C)-V(K)$. Now $V(C)=\pi R^3$ and, by the cone formula (or by the same slicing argument
applied to a pyramid), $V(K)=\tfrac13\pi R^3$. Therefore
$$V(H)=\pi R^3-\tfrac13\pi R^3=\tfrac23\pi R^3,\qquad
V_{\text{ball}}=2V(H)=\tfrac43\pi R^3 .$$
$\blacksquare$

*Remark.* The two solids are *not* congruent, and the hemisphere is not "the same shape" as
cylinder-minus-cone; only the family of cross-sectional areas agrees. That is exactly what Cavalieri's
principle licenses.

### Solution 34

**(a) The frame.** The counts are given: $V=16$, $E=32$, $F=16$. Hence
$$V-E+F=16-32+16=0 .$$

**(b) Two tetrahedra at a vertex.** The shared vertex is counted once, so $V=4+4-1=7$. No edge is shared,
so $E=6+6=12$, and no face is shared, so $F=4+4=8$. Hence
$$V-E+F=7-12+8=3 .$$

**(c) Which hypothesis fails.**

* For the frame, every face is a polygon, every edge belongs to exactly two faces, and the surface is
  connected — but the surface is **not simple**: it is a torus, with a tunnel through the middle. A closed
  loop drawn on the surface around the tunnel cannot be shrunk to a point, which is precisely what
  "homeomorphic to a sphere" forbids. The general formula is $V-E+F=2-2g$ with genus $g=1$ here.
* For the two tetrahedra, the surface is not even a surface at the shared vertex: a small sphere centred
  there meets the solid in two separate closed curves, not one, so a neighbourhood of that point is not a
  disc. Definition 5.4 fails, and Euler's theorem does not apply. The value $3=2+2-1$ reflects two
  sphere-like pieces sharing one point.

*Moral.* $V-E+F$ is not a property of "a solid" but of a *surface type*; the formula $2$ labels the sphere.

### Solution 35

**(a) Volumes.** The hemisphere has
$$V_{\text{hemi}}=\tfrac23\pi R^3 .$$
The cone has base radius $R$ and height $R$, so
$$V_{\text{cone}}=\tfrac13\pi R^2\cdot R=\tfrac13\pi R^3 .$$
The hemisphere is exactly **twice** the cone.

**(b) Equal-volume cone.** Solve
$$\tfrac13\pi R^2h=\tfrac23\pi R^3 \;\Longrightarrow\; h=2R .$$
So a cone of base radius $R$ needs height $2R$ to match the hemisphere.

**(c) Why.** In Section 7.5 the hemisphere was compared with the cylinder of radius $R$ and height $R$
*with the cone removed*: at every height $y$ both have cross-sectional area $\pi(R^2-y^2)$. Since the
cylinder has volume $\pi R^3$ and the removed cone $\tfrac13\pi R^3$, the hemisphere is $\tfrac23\pi R^3$
and therefore twice the cone that was removed. Part (b) says that doubling the cone's height doubles its
volume, since volume is linear in height for a fixed base.

*Check.* At height $y$ the cone alone has area $\pi y^2$ while the hemisphere has $\pi(R^2-y^2)$; these
agree only at $y=R/\sqrt2$, which is why the two solids are not comparable by a single slice — the
cylinder is what makes the comparison work.

### Solution 36

**Relate the variables.** Let the cylinder have radius $r$ and height $h$, with axis through the sphere's
centre. Half the height, the radius and the sphere's radius form a right triangle:
$$\left(\tfrac h2\right)^2+r^2=R^2 \;\Longrightarrow\; h=2\sqrt{R^2-r^2},\qquad 0\le r\le R .$$

**Volume.**
$$V(r)=\pi r^2h=2\pi r^2\sqrt{R^2-r^2},\qquad
V(r)^2=4\pi^2r^4(R^2-r^2).$$
Maximising $V$ is the same as maximising $r^4(R^2-r^2)$.

**AM–GM.** Put $u=r^2$ and apply AM–GM to $\tfrac u2,\tfrac u2,R^2-u$, whose sum is $R^2$:
$$\frac{u}{2}\cdot\frac{u}{2}\cdot(R^2-u)\le\left(\frac{R^2}{3}\right)^3=\frac{R^6}{27}
\;\Longrightarrow\; u^2(R^2-u)\le\frac{4R^6}{27},$$
with equality exactly when $\tfrac u2=R^2-u$, i.e. $u=\tfrac{2R^2}{3}$.

**Answer.**
$$r=\sqrt{\tfrac23}\,R,\qquad h=2\sqrt{R^2-\tfrac23R^2}=\frac{2R}{\sqrt3},\qquad
V_{\max}=2\pi\cdot\tfrac{2R^2}{3}\cdot\frac{R}{\sqrt3}=\frac{4\pi R^3}{3\sqrt3}.$$

**Comparison with the sphere.** Numerically $V_{\max}\approx2.418R^3$ against
$V_{\text{sphere}}=\tfrac43\pi R^3\approx4.189R^3$, a ratio of
$$\frac{V_{\max}}{V_{\text{sphere}}}
=\frac{4\pi R^3/(3\sqrt3)}{4\pi R^3/3}=\frac{1}{\sqrt3}\approx0.577 .$$
So the largest inscribed cylinder fills about $57.7\%$ of the sphere — comfortably less, as it must be.

*Check.* With $h=2R/\sqrt3$ the half-height is $R/\sqrt3$ and
$r^2+(R/\sqrt3)^2=\tfrac23R^2+\tfrac13R^2=R^2$ ✓, so the cylinder really is inscribed.