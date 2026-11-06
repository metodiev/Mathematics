# Non-Euclidean Geometry — Solutions

> [Tutorial](README.md) · [Exercises](exercises.md) · 36 worked solutions

Each solution states the strategy, carries out every significant step, and checks the result against the
definition or a limiting case. Curvature is $K=-1$ unless a radius $R$ is explicitly introduced.

## Beginner

### Solution 1

Euclid V: if a transversal meets two lines and the interior angles on one side sum to less than two right
angles, the lines meet on that side. Playfair: through a point not on a line there is at most one parallel.

*Existence.* In neutral geometry at least one parallel exists: drop the perpendicular $PQ$ to $\ell$ and erect
the perpendicular to $PQ$ at $P$; the alternate interior angles are right angles, so the new line is parallel
to $\ell$.

*Euclid V implies Playfair.* Suppose $m,m'$ through $P$ are both parallel to $\ell$. Let a transversal through
$P$ meet $\ell$ at $Q$. On one side of the transversal, the same-side interior angles with each parallel are
supplementary to the angle at $Q$, so both $m$ and $m'$ make the same angle with the transversal; hence they
coincide. So there is at most one.

*Playfair implies Euclid V.* Suppose the angles $\alpha$ at $Q$ and $\beta$ at $P$ on one side satisfy
$\alpha+\beta<\pi$. Construct through $P$ the line $m'$ with angle $\beta'=\pi-\alpha$ on that side. Then the
alternate interior angles are equal, so $m'\parallel\ell$. Since $\beta<\beta'$, $m\ne m'$; by Playfair, $m$
meets $\ell$. The meeting is on the side where the sum is less than $\pi$, because on the other side the
same-side angles sum to $2\pi-(\alpha+\beta)>\pi$, and two lines meeting on a side form a triangle whose two
interior angles have sum less than $\pi$. Hence Euclid V. ∎

### Solution 2

The excess is $90^\circ+90^\circ+60^\circ-180^\circ=60^\circ=\pi/3$. For the unit sphere,
$$\operatorname{area}=R^2(A+B+C-\pi)=1\cdot\frac{\pi}{3}=\frac{\pi}{3}\approx1.047.$$
*Check.* The triangle is one sixth of a hemisphere? Its area is less than the octant area $\pi/2\approx1.571$,
as it must be. ✓

### Solution 3

In radians the angles are $\pi/2,\pi/3,\pi/3$, whose sum is $7\pi/6$. The excess is
$$7\pi/6-\pi=\pi/6.$$
Thus
$$\operatorname{area}=R^2\cdot\frac{\pi}{6}=6371^2\cdot\frac{\pi}{6}\approx4.0590\times10^7\cdot0.5236
\approx2.125\times10^7\ \mathrm{km}^2.$$
*Check.* This is about $4.2\%$ of the Earth's surface $4\pi R^2\approx5.10\times10^8\ \mathrm{km}^2$, which is
plausible for a triangle with three moderate angles. ✓

### Solution 4

$72^\circ=2\pi/5$. A lune of angle $\theta$ has area $2R^2\theta$, so
$$\operatorname{area}=2\cdot1^2\cdot\frac{2\pi}{5}=\frac{4\pi}{5}\approx2.513.$$
*Check.* A lune of angle $180^\circ=\pi$ is a hemisphere of area $2\pi$; the formula gives $2\pi$ ✓.

### Solution 5

Use $\cos c=\sin\varphi_1\sin\varphi_2+\cos\varphi_1\cos\varphi_2\cos(\lambda_1-\lambda_2)$ with
$\varphi_1=0$, $\lambda_1=0$, $\varphi_2=60^\circ$, $\lambda_2=30^\circ$:
$$\cos c=0+\cos0^\circ\cos60^\circ\cos30^\circ=\frac12\cdot\frac{\sqrt3}{2}=\frac{\sqrt3}{4}\approx0.4330.$$
Hence $c=\arccos(0.4330)\approx64.34^\circ=1.123$ rad, and the distance is
$$Rc\approx6371\times1.123\approx7154\ \mathrm{km}.$$
*Check.* The point is at latitude $60^\circ$, so its distance from the equator is at most $90^\circ$ and at
least $60^\circ$; $64.34^\circ$ lies between ✓.

### Solution 6

For $z=0$ and $w=\tfrac13$,
$$d_{\mathbb D}(0,\tfrac13)=2\operatorname{artanh}\frac13
=\ln\frac{1+\frac13}{1-\frac13}=\ln2\approx0.6931.$$
*Check.* The Euclidean distance is $1/3$, but the hyperbolic distance is larger, as it must be because the
metric blows up near the boundary. ✓

### Solution 7

Use $d_{\mathbb H}(z,w)=\operatorname{arcosh}\left(1+\frac{|z-w|^2}{2\operatorname{Im}z\operatorname{Im}w}\right)$
with $z=i$, $w=4i$:
$$d=\operatorname{arcosh}\left(1+\frac{(4-1)^2}{2\cdot1\cdot4}\right)
=\operatorname{arcosh}\left(1+\frac98\right)=\operatorname{arcosh}\frac{17}{8}.$$
Since $\cosh\ln4=(4+1/4)/2=17/8$, we get $d=\ln4\approx1.3863$.
*Check.* Integrate the metric along the vertical geodesic: $\int_1^4 dy/y=\ln4$ ✓.

### Solution 8

The defect is
$$\delta=\pi-(A+B+C)=180^\circ-160^\circ=20^\circ=\frac{\pi}{9}.$$
For $K=-1$, area equals the defect, so
$$\operatorname{area}=\frac{\pi}{9}\approx0.3491.$$
*Check.* The area is less than the ideal-triangle bound $\pi\approx3.142$ ✓.

### Solution 9

The Gaussian curvature is $K=1/R^2=1/9$. Every nondegenerate spherical triangle has positive excess
$A+B+C-\pi=\operatorname{area}/R^2>0$, so its angle sum is greater than $\pi$. ∎

### Solution 10

Hyperbolic ($K=-1$): $C=2\pi\sinh1\approx2\pi(1.1752)\approx7.384$. Euclidean: $C=2\pi\approx6.283$.
Spherical ($R=1$): $C=2\pi\sin1\approx2\pi(0.8415)\approx5.288$. Thus
$$C_{\text{spherical}}<C_{\text{Euclidean}}<C_{\text{hyperbolic}}.$$
This is consistent with the sign of curvature: positive curvature closes circles up, negative curvature opens
them out. ✓

### Solution 11

For a point at Euclidean radius $r$ on a diameter, the ideal endpoints are at parameters $p=-1$ and $q=1$,
and the centre has parameter $a=0$. Thus
$$d_K(0,r)=\frac12\ln\frac{(p-a)(q-b)}{(p-b)(q-a)}
=\frac12\ln\frac{(-1)(1-r)}{(-1-r)(1)}
=\frac12\ln\frac{1+r}{1-r}.$$
At $r=\tfrac12$,
$$d_K=\frac12\ln\frac{3/2}{1/2}=\frac12\ln3\approx0.5493.$$
*Check.* This is exactly $\operatorname{artanh}(1/2)$ ✓.

### Solution 12

$$\tan\frac{\Pi(1)}{2}=e^{-1}\quad\Longrightarrow\quad
\Pi(1)=2\arctan(e^{-1})\approx2(0.3525)=0.7050\ \mathrm{rad}\approx40.40^\circ.$$
*Check.* As $d\to0$, $\Pi\to90^\circ$; $40.4^\circ<90^\circ$ and positive ✓.

## Intermediate

### Solution 13

Let the vertices be unit vectors $w=(0,0,1)$, $u=(\sin b,0,\cos b)$ and
$v=(\sin a\cos C,\sin a\sin C,\cos a)$. The coordinates encode: the angle between $u$ and $w$ is $b$ (so
$u\cdot w=\cos b$); the angle between $v$ and $w$ is $a$ (so $v\cdot w=\cos a$); and the dihedral angle at
$w$ is $C$, because the projection of $v$ onto the $xy$-plane makes angle $C$ with the projection of $u$,
which is the positive $x$-axis. Then
$$u\cdot v=\sin b\,\sin a\cos C+0\cdot\sin a\sin C+\cos b\cos a
=\cos a\cos b+\sin a\sin b\cos C.$$
But $u\cdot v=\cos c$, where $c$ is the angle between $u$ and $v$, i.e. the side opposite $C$. Hence
$$\cos c=\cos a\cos b+\sin a\sin b\cos C. \qquad\square$$

### Solution 14

$$\cos c=\cos60^\circ\cos45^\circ+\sin60^\circ\sin45^\circ\cos60^\circ
=\frac12\cdot\frac{\sqrt2}{2}+\frac{\sqrt3}{2}\cdot\frac{\sqrt2}{2}\cdot\frac12
=\frac{\sqrt2}{4}+\frac{\sqrt6}{8}.$$
Numerically $\sqrt2/4\approx0.353553$ and $\sqrt6/8\approx0.306186$, so $\cos c\approx0.659739$ and
$$c\approx48.72^\circ.$$
*Check.* The triangle inequality on a sphere requires $|a-b|<c<a+b$ (for sides less than $\pi$); here
$15^\circ<48.72^\circ<105^\circ$ ✓.

### Solution 15

The excess is $3(72^\circ)-180^\circ=36^\circ=\pi/5$, so for the unit sphere the area is $\pi/5$. Twenty
congruent copies have total area $20\pi/5=4\pi$, the area of the whole unit sphere. The icosahedral
tessellation has 20 equilateral triangular faces and 5 triangles at each vertex; at each vertex the five
angles $72^\circ$ sum to $360^\circ$, so the triangles fit without overlap. Hence the copies tile the sphere.
$\square$

### Solution 16

By symmetry the centre lies on the line $x=y$, say $P=(a,a)$, and the circle is orthogonal to the unit circle,
so its radius $\rho$ satisfies $|P|^2=\rho^2+1$, i.e. $2a^2=\rho^2+1$. The point $\tfrac12$ lies on it:
$$\rho^2=\left(a-\tfrac12\right)^2+a^2=2a^2-a+\tfrac14.$$
Equating with $\rho^2=2a^2-1$ gives $2a^2-a+\tfrac14=2a^2-1$, hence $a=\tfrac54$. Therefore
$$\rho^2=2\cdot\frac{25}{16}-1=\frac{25}{8}-1=\frac{17}{8},\qquad
\rho=\sqrt{\frac{17}{8}}\approx1.458.$$
The geodesic is the arc inside the disk of the circle
$$\left(x-\tfrac54\right)^2+\left(y-\tfrac54\right)^2=\tfrac{17}{8}.$$
*Check.* The point $\tfrac{i}{2}=(0,\tfrac12)$ also satisfies
$(-\tfrac54)^2+(-\tfrac34)^2=\tfrac{25}{16}+\tfrac{9}{16}=\tfrac{34}{16}=\tfrac{17}{8}$ ✓, and orthogonality
holds because $|P|^2=25/8=\rho^2+1$ ✓.

### Solution 17

For $f(z)=-z$,
$$|f(z)-f(w)|=|z-w|,\qquad |1-\overline{f(z)}f(w)|=|1-\bar z w|,$$
so the quotient in the distance formula is unchanged.

For $g(z)=\bar z$,
$$|g(z)-g(w)|=|\bar z-\bar w|=|z-w|,$$
and $1-\overline{g(z)}g(w)=1-zw$. Its modulus is $|1-zw|=|\overline{1-\bar z w}|=|1-\bar z w|$. Hence the
quotient is again unchanged. Both maps preserve the disk and the distance, so both are isometries. ∎

### Solution 18

Parametrise the semicircle by $(x,y)=(\cos\theta,\sin\theta)$, $0<\theta<\pi$. Take $\theta'=\sin\theta$,
so the speed is
$$\frac{\sqrt{(x')^2+(y')^2}}{y}
=\frac{\sqrt{\sin^4\theta+\sin^2\theta\cos^2\theta}}{\sin\theta}=1.$$
Then $x'=-\sin^2\theta$, $y'=\sin\theta\cos\theta$, and
$$x''=-2\sin^2\theta\cos\theta,\qquad
\frac{2}{y}x'y'=\frac{2}{\sin\theta}(-\sin^2\theta)(\sin\theta\cos\theta)
=-2\sin^2\theta\cos\theta,$$
so the first geodesic equation holds. Also
$$y''=\sin\theta(\cos^2\theta-\sin^2\theta),\qquad
\frac{1}{y}\bigl((x')^2-(y')^2\bigr)
=\frac{1}{\sin\theta}\bigl(\sin^4\theta-\sin^2\theta\cos^2\theta\bigr)
=\sin\theta(\sin^2\theta-\cos^2\theta),$$
so $y''+\frac1y((x')^2-(y')^2)=0$. Both geodesic equations hold. ∎

### Solution 19

Hyperbolic: $A=2\pi(\cosh2-1)=2\pi(3.7622-1)\approx17.355$.
Euclidean: $A=\pi\cdot2^2=4\pi\approx12.566$.
Spherical with $R=2$, $r=1$: $A=2\pi R^2(1-\cos(r/R))=8\pi(1-\cos0.5)\approx3.077$.
Hence
$$A_{\text{spherical}}<A_{\text{Euclidean}}<A_{\text{hyperbolic}}.$$
*Check.* The hyperbolic disk has more area than the Euclidean one of the same radius because circles grow like
$\sinh r$, and the spherical disk has less because circles shrink like $\sin(r/R)$ ✓.

### Solution 20

Let $ABCD$ have base $AB$, right angles at $A$ and $B$, and $AD=BC$. In triangles $ABD$ and $BAC$:
$AD=BC$, $AB=BA$, and $\angle DAB=\angle CBA=90^\circ$. By SAS, $BD=AC$. In triangles $ADC$ and $BCD$:
$AD=BC$, $AC=BD$, and $DC=CD$. By SSS, they are congruent, so $\angle ADC=\angle BCD$. These are the summit
angles. ∎

### Solution 21

$$\cosh c=\cosh1\cosh1-\sinh1\sinh1\cos120^\circ
=\cosh^2 1+\frac12\sinh^2 1.$$
Using $\cosh1\approx1.54308$ and $\sinh1\approx1.17520$,
$$\cosh c\approx2.38110+0.5(1.38110)=3.07165.$$
Thus
$$c=\operatorname{arcosh}(3.07165)=\ln\left(3.07165+\sqrt{3.07165^2-1}\right)
=\ln(3.07165+2.90257)\approx\ln5.97422\approx1.7877.$$
*Check.* The hyperbolic triangle inequality gives $c<a+b=2$; $1.7877<2$ ✓, and $c>|a-b|=0$ ✓.

### Solution 22

Convert to radians and use
$$\cos c=\sin\varphi_1\sin\varphi_2+\cos\varphi_1\cos\varphi_2\cos(\lambda_1-\lambda_2).$$
Here $\varphi_1=51.5^\circ$, $\varphi_2=40.7^\circ$, $\lambda_1-\lambda_2=73.9^\circ$. Then
$$\cos c=(0.7826)(0.6521)+(0.6225)(0.7581)(0.2773)
\approx0.5103+0.1309=0.6412,$$
so $c\approx50.11^\circ=0.8746$ rad and
$$d=6371\cdot0.8746\approx5572\ \mathrm{km}.$$
*Check.* The quoted great-circle distance between London and New York is about $5570$ km ✓.

## Advanced

### Solution 23

Let the three great circles containing the sides divide the sphere into eight spherical triangles: $T$, its
antipodal image $T'$, and six others forming three antipodal pairs $U,U'$, $V,V'$, $W,W'$, where $U$ is
adjacent to $T$ across the side opposite $A$, $V$ across the side opposite $B$, and $W$ across the side
opposite $C$.

*Lune at $A$.* The two great circles through $A$ bound a lune of angle $A$. The great circle through the
opposite side cuts this lune into $T$ and $U$. By §8.3, the lune has area $2R^2A$. Hence
$$\operatorname{area}(T)+\operatorname{area}(U)=2R^2A.$$
Similarly
$$\operatorname{area}(T)+\operatorname{area}(V)=2R^2B,\qquad
\operatorname{area}(T)+\operatorname{area}(W)=2R^2C.$$
Adding,
$$2R^2(A+B+C)=3\operatorname{area}(T)+\operatorname{area}(U)+\operatorname{area}(V)+\operatorname{area}(W).$$

*Partition of the sphere.* The eight triangles have disjoint interiors and cover the sphere. The antipodal map
is an isometry, so $\operatorname{area}(T')=\operatorname{area}(T)$,
$\operatorname{area}(U')=\operatorname{area}(U)$, and similarly. Therefore
$$4\pi R^2=2\operatorname{area}(T)+2\bigl(\operatorname{area}(U)+\operatorname{area}(V)+\operatorname{area}(W)\bigr),$$
which gives
$$\operatorname{area}(U)+\operatorname{area}(V)+\operatorname{area}(W)=2\pi R^2-\operatorname{area}(T).$$
Substituting,
$$2R^2(A+B+C)=3\operatorname{area}(T)+2\pi R^2-\operatorname{area}(T)
=2\operatorname{area}(T)+2\pi R^2,$$
so
$$\operatorname{area}(T)=R^2(A+B+C-\pi). \qquad\blacksquare$$

### Solution 24

For unit vectors $u,v,w$, the identity
$$(u\times v)\times(u\times w)=[u\cdot(v\times w)]\,u$$
follows from the vector triple product. Taking magnitudes,
$$|(u\times v)\times(u\times w)|=|u\cdot(v\times w)|.$$
The left side is
$$|u\times v|\,|u\times w|\sin A=\sin c\,\sin b\,\sin A,$$
because $|u\times v|=\sin c$, $|u\times w|=\sin b$, and the angle between the normals $u\times v$ and $u\times w$
is the dihedral angle $A$ (or $\pi-A$, whose sine is the same). The right side is the absolute value of the
scalar triple product, which by symmetry equals $\sin a\,\sin b\,\sin C$. Hence
$$\sin c\,\sin b\,\sin A=\sin a\,\sin b\,\sin C.$$
Cancelling $\sin b>0$,
$$\frac{\sin A}{\sin a}=\frac{\sin C}{\sin c}.$$
The same argument with the roles of the vertices permuted gives the full sine law. ∎

### Solution 25

In the hyperboloid model,
$$\mathbb{H}^2=\{x=(x_0,x_1,x_2):\langle x,x\rangle_{2,1}=-1,\ x_0>0\},\qquad
\langle x,y\rangle_{2,1}=x_1y_1+x_2y_2-x_0y_0,$$
and $\cosh d(x,y)=-\langle x,y\rangle_{2,1}$.

Place $C=(1,0,0)$, $A=(\cosh b,\sinh b,0)$ and $B=(\cosh a,\sinh a\cos C,\sinh a\sin C)$. Then
$$\langle A,A\rangle_{2,1}=\sinh^2 b-\cosh^2 b=-1,\qquad
\langle B,B\rangle_{2,1}=\sinh^2 a-\cosh^2 a=-1,$$
so both are on $\mathbb{H}^2$. Moreover $d(A,C)=b$ and $d(B,C)=a$ because
$$-\langle A,C\rangle_{2,1}=\cosh b,\qquad -\langle B,C\rangle_{2,1}=\cosh a.$$
The angle at $C$ between the two geodesics is $C$ by construction (the second coordinate of $B$ is
$\sinh a\cos C$). Finally,
$$-\langle A,B\rangle_{2,1}
=-\bigl(\sinh b\,\sinh a\cos C-\cosh b\cosh a\bigr)
=\cosh a\cosh b-\sinh a\sinh b\cos C.$$
Since $d(A,B)=c$, the left side is $\cosh c$, so
$$\cosh c=\cosh a\cosh b-\sinh a\sinh b\cos C. \qquad\blacksquare$$

### Solution 26

Work in the Poincaré disk and use an isometry to send a vertex $A$ to the centre $O$. Isometries preserve
angles and geodesics, so it suffices to compare the triangle $OBC$ with the Euclidean triangle with the same
vertices. The sides $OB$ and $OC$ are Euclidean radii.

*The arc $BC$ lies inside the Euclidean triangle $OBC$.* The side $BC$ is an arc of a circle $\gamma$ orthogonal
to $\partial\mathbb{D}$. Let $P$ be the centre of $\gamma$ and $\rho$ its radius. Orthogonality gives
$|P|^2=\rho^2+1$, so $|P|>1$. Every ray from $O$ meets $\gamma$ in at most one point of $\mathbb{D}$: for a
unit vector $X$, the points $tX$ on $\gamma$ satisfy
$$|tX-P|^2=\rho^2\iff t^2-2t(X\cdot P)+1=0,$$
whose roots have product $1$; so an interior intersection ($0<t<1$) excludes a second one. Hence the arc,
being connected and joining $B$ to $C$, stays inside the cone spanned by $OB$ and $OC$. The point of $\gamma$
farthest from $O$ is $P(1+\rho/|P|)$, which lies outside $\mathbb{D}$; the arc inside $\mathbb{D}$ is the
other arc between $B$ and $C$, so it lies on the side of the chord $BC$ opposite that point. Since the chord
lies in $\mathbb{D}$ and $|P|>1$, the centre $P$ and that farthest point are on the same side of the chord;
hence the inside arc is on the $O$ side of $BC$. A connected arc in the cone and on the $O$ side of $BC$ is
contained in the triangle $OBC$.

Therefore the tangent to the arc at $B$ points into the Euclidean angle $\angle OBC$, so the hyperbolic angle
at $B$ is strictly smaller than the Euclidean angle. Similarly at $C$. The angle at $O$ is unchanged. Hence
$$A+B+C<\angle OBC+\angle OCB+\angle BOC=\pi. \qquad\blacksquare$$

### Solution 27

Put the line $\ell$ on the imaginary axis of $\mathbb{H}$ and let $P=(x_0,y_0)$ with $x_0>0$. Set
$r=\sqrt{x_0^2+y_0^2}$. The geodesic through $P$ perpendicular to $\ell$ is the circle centred at $0$ of radius
$r$; it meets $\ell$ at $(0,r)$. The distance formula gives
$$\cosh d=\frac{r}{y_0},\qquad \sinh d=\frac{x_0}{y_0},\qquad \tanh d=\frac{x_0}{r}.$$
The limiting parallel through $P$ asymptotic to $\ell$ at infinity is the vertical line $x=x_0$. The tangent
to the perpendicular at $P$ has direction $(-y_0,x_0)$, and the vertical direction is $(0,1)$. If
$\Pi=\Pi(d)$ is the angle between them, then
$$\cos\Pi=\frac{x_0}{r}=\tanh d,\qquad \sin\Pi=\frac{y_0}{r}=\operatorname{sech}d.$$
Therefore
$$\tan\frac{\Pi}{2}=\frac{\sin\Pi}{1+\cos\Pi}
=\frac{\operatorname{sech}d}{1+\tanh d}
=\frac{1}{\cosh d+\sinh d}=e^{-d}. \qquad\blacksquare$$

### Solution 28

Let $w=i(1+z)/(1-z)$. First compute the imaginary part:
$$\frac{1+z}{1-z}=\frac{(1+z)(1-\bar z)}{|1-z|^2}
=\frac{1-|z|^2+z-\bar z}{|1-z|^2}
=\frac{1-|z|^2+2i\operatorname{Im}z}{|1-z|^2}.$$
Multiplying by $i$,
$$w=i\frac{1-|z|^2}{|1-z|^2}-\frac{2\operatorname{Im}z}{|1-z|^2},$$
so
$$\operatorname{Im}w=\frac{1-|z|^2}{|1-z|^2}.$$
Next,
$$\frac{dw}{dz}=i\frac{(1-z)+(1+z)}{(1-z)^2}=\frac{2i}{(1-z)^2}.$$
Hence
$$\frac{|dw|^2}{(\operatorname{Im}w)^2}
=\frac{4|dz|^2}{|1-z|^4}\cdot\frac{|1-z|^4}{(1-|z|^2)^2}
=\frac{4|dz|^2}{(1-|z|^2)^2}.$$
This is exactly the Poincaré disk metric, so the Cayley transform is an isometry. ∎

### Solution 29

In the disk, let $r=d_{\mathbb{D}}(0,z)$ and $\rho=|z|$. Since $r=2\operatorname{artanh}\rho$, we have
$\rho=\tanh(r/2)$. The hyperbolic area element is
$$dA=\frac{4\rho}{(1-\rho^2)^2}\,d\rho\,d\theta.$$
Now
$$\frac{d\rho}{dr}=\frac12\operatorname{sech}^2\frac r2,\qquad
1-\rho^2=1-\tanh^2\frac r2=\operatorname{sech}^2\frac r2.$$
Therefore
$$\frac{4\rho}{(1-\rho^2)^2}\,d\rho
=4\tanh\frac r2\cosh^4\frac r2\cdot\frac12\operatorname{sech}^2\frac r2\,dr
=2\tanh\frac r2\cosh^2\frac r2\,dr
=2\sinh\frac r2\cosh\frac r2\,dr
=\sinh r\,dr.$$
Thus $dA=\sinh r\,dr\,d\theta$ in geodesic polar coordinates. Integrating,
$$C(r)=\int_0^{2\pi}\sinh r\,d\theta=2\pi\sinh r,$$
and
$$A(r)=\int_0^r\int_0^{2\pi}\sinh s\,d\theta\,ds
=2\pi\int_0^r\sinh s\,ds=2\pi(\cosh r-1). \qquad\blacksquare$$

### Solution 30

The **dual law of cosines** for a hyperbolic triangle (obtained from the side law by algebraic elimination,
using $\sinh^2=\cosh^2-1$) is
$$\cos C=-\cos A\cos B+\sin A\sin B\cosh c,$$
with cyclic permutations. (Substituting
$\cos A=(\cosh b\cosh c-\cosh a)/(\sinh b\sinh c)$ and
$\cos B=(\cosh a\cosh c-\cosh b)/(\sinh a\sinh c)$ into the right side, and using
$\sinh^2=\cosh^2-1$, simplifies it to $(\cosh a\cosh b-\cosh c)/(\sinh a\sinh b)=\cos C$.) Given the angles
$A,B,C$ with $A+B+C<\pi$, this determines
$$\cosh c=\frac{\cos C+\cos A\cos B}{\sin A\sin B},$$
because $\sin A,\sin B>0$. Similarly it determines $\cosh a$ and $\cosh b$. Since $\cosh$ is injective on
$[0,\infty)$, the three side lengths are determined. Two hyperbolic triangles with the same angles therefore
have the same side lengths, hence are congruent by SSS. ∎

### Solution 31

Every ideal triangle is isometric to the one in the upper half-plane with ideal vertices $-1,1,\infty$: the
group of hyperbolic isometries acts triply transitively on the boundary real line, so it can send any three
distinct ideal points to $-1,1,\infty$.

That triangle is bounded by the semicircle $|z|=1$ (the geodesic from $-1$ to $1$) and the vertical lines
$x=-1$ and $x=1$ (the geodesics from $-1$ and $1$ to $\infty$). Its interior is
$$\{(x,y):-1<x<1,\ y>\sqrt{1-x^2}\}.$$
With $dA=dx\,dy/y^2$,
$$\operatorname{area}=\int_{-1}^{1}\int_{\sqrt{1-x^2}}^{\infty}\frac{dy}{y^2}\,dx
=\int_{-1}^{1}\frac{dx}{\sqrt{1-x^2}}
=\bigl[\arcsin x\bigr]_{-1}^{1}=\frac{\pi}{2}-\left(-\frac{\pi}{2}\right)=\pi. \qquad\blacksquare$$

## Challenge

### Solution 32

At each vertex, $q$ copies of the interior angle $2\pi/q$ fill the full angle $2\pi$. A regular hyperbolic
$p$-gon exists with interior angle $\theta$ for every $0<\theta<(p-2)\pi/p$: as the polygon shrinks to a point,
$\theta$ tends to the Euclidean value $(p-2)\pi/p$, and as its vertices go to infinity, $\theta$ tends to $0$.
Hence a $\{p,q\}$ tiling exists exactly when
$$\frac{2\pi}{q}<\frac{(p-2)\pi}{p}
\iff \frac{2}{q}<\frac{p-2}{p}
\iff 2p<q(p-2)
\iff \frac1p+\frac1q<\frac12.$$
The area of one $p$-gon is
$$\operatorname{area}=(p-2)\pi-p\cdot\frac{2\pi}{q}
=\pi\left(p-2-\frac{2p}{q}\right).$$
For $\{7,3\}$: $1/7+1/3=10/21<1/2$, and
$$\operatorname{area}=\pi\left(5-\frac{14}{3}\right)=\frac{\pi}{3}.$$
For $\{8,3\}$: $1/8+1/3=11/24<1/2$, and
$$\operatorname{area}=\pi\left(6-\frac{16}{3}\right)=\frac{2\pi}{3}.$$
*Check.* Both areas are positive, as they must be for a hyperbolic tiling; the Euclidean case
$1/p+1/q=1/2$ would give area $0$, and the spherical case gives a negative "area" in this formula. ✓

### Solution 33

Gauss–Bonnet for a geodesic triangle states
$$A+B+C-\pi=\iint_T K\,dA.$$
For constant curvature $K$ this is $A+B+C-\pi=K\operatorname{area}(T)$.

*Sphere* ($K=1/R^2$): $\operatorname{area}=R^2(A+B+C-\pi)$. The excess is positive, so the area is positive.
For the octant, excess $\pi/2$, area $\pi R^2/2$.

*Plane* ($K=0$): $A+B+C-\pi=0$ for every triangle, so the angle sum is always $\pi$ and the area is not
determined by the angles. There is no positive area formula of the same kind.

*Hyperbolic plane* ($K=-1/R^2$): $A+B+C-\pi=-\operatorname{area}/R^2$, so
$\operatorname{area}=R^2(\pi-A-B-C)$. The defect is positive, so the area is positive.

*Limit $R\to\infty$.* For a fixed area, $K\cdot\operatorname{area}\to0$, so the excess or defect tends to $0$
and the angle sum tends to $\pi$, recovering the Euclidean case on scales small compared with $R$. This is the
local flatness of a very large sphere or a very large hyperbolic plane. ✓

### Solution 34

Let $\ell$ be a chord with ideal endpoints $u,v$. A chord through $P$ is determined by its second ideal
endpoint $t$ on the boundary circle. The chords through $P$ that meet $\ell$ are exactly those whose
directions lie in the closed angular interval between the lines $Pu$ and $Pv$; this interval is the projection
of the segment $\ell$ from $P$. Its complement is a nonempty open interval of directions, containing infinitely
many lines through $P$, and each of them gives a chord that misses $\ell$. Hence there are infinitely many
parallels through $P$.

The two limiting cases are the chords $Pu$ and $Pv$: they meet $\ell$ only at the ideal endpoints $u$ and $v$,
so they approach $\ell$ asymptotically and are the two limiting parallels. Every other chord in the
complementary interval misses $\ell$ by a positive distance and is ultraparallel. ∎

### Solution 35

Draw a diagonal of the quadrilateral, splitting it into two triangles. Let the angles of the first triangle be
$A,B_1,D_1$ and those of the second be $B_2,C,D_2$, where $B=B_1+B_2$ and $D=D_1+D_2$. By the hyperbolic
defect formula,
$$\operatorname{area}=\bigl(\pi-A-B_1-D_1\bigr)+\bigl(\pi-B_2-C-D_2\bigr)
=2\pi-(A+B+C+D).$$
Since the quadrilateral is nondegenerate, both triangles have positive area, so
$A+B+C+D<2\pi$. This also shows the area is positive. ∎

### Solution 36

Spherical geometry fails several axioms of neutral geometry:

1. **Two points determine a line.** Two antipodal points lie on infinitely many great circles: every plane
   through the origin containing their diameter cuts the sphere in a great circle through both.
2. **A segment can be extended indefinitely.** A great circle is closed and has length $2\pi R$; walking along
   it returns to the starting point and produces no new points beyond it.
3. **Order axioms.** A great circle is a circle, not a line with two ends; the usual betweenness relation on a
   line fails globally (there is no linear order of all points of a great circle compatible with the incidence
   structure).
4. **Existence of a parallel.** Neutral geometry proves that through a point not on a line there is at least
   one parallel; on the sphere there are none, because any two great circles meet.

A model of neutral geometry plus $\neg$Playfair must satisfy *all* of neutral geometry, not just the negation
of the parallel postulate. The sphere fails the axioms above, so it is not such a model and cannot prove
independence. The Poincaré disk (equivalently the Klein model) does satisfy neutral geometry and the negation
of Playfair: its lines are circular arcs orthogonal to the boundary, through an exterior point there are
infinitely many disjoint ones, and every neutral axiom is a theorem about the disk. Hence, relative to the
consistency of Euclidean geometry, the parallel postulate is independent. ∎
