# Non-Euclidean Geometry — Exercises

> [Tutorial](README.md) · 36 problems · Levels: Beginner, Intermediate, Advanced, Challenge

Work each problem completely: state the model and the curvature normalization, show the formula you use, and
check that the answer is plausible (sign of the defect or excess, triangle inequality, limiting cases). Full
solutions are in [solutions.md](solutions.md); do not open that file until you have attempted the problems.

## Beginner

**1.** State Euclid's fifth postulate and Playfair's axiom. Explain in one paragraph why they are equivalent
in neutral geometry.

**2.** On the unit sphere, a spherical triangle has angles $90^\circ$, $90^\circ$ and $60^\circ$. Find its
spherical excess and its area.

**3.** On the Earth, model the surface as a sphere of radius $R=6371$ km. A spherical triangle has angles
$90^\circ$, $60^\circ$ and $60^\circ$. Find its area in square kilometres.

**4.** On the unit sphere, find the area of a lune of angle $72^\circ$.

**5.** Find the great-circle distance from $(0^\circ,0^\circ)$ to $(60^\circ\text{N},30^\circ\text{E})$ on a
sphere of radius $6371$ km.

**6.** In the Poincaré disk, compute $d_{\mathbb{D}}(0,\tfrac13)$.

**7.** In the upper half-plane, compute $d_{\mathbb{H}}(i,4i)$.

**8.** A hyperbolic triangle has angles $50^\circ$, $60^\circ$ and $50^\circ$. Find its defect and its area
for curvature $K=-1$.

**9.** A sphere has radius $3$. State its Gaussian curvature and the sign of the angle sum of every
nondegenerate spherical triangle on it.

**10.** Compare the circumference of a circle of radius $1$ in the hyperbolic plane ($K=-1$), the Euclidean
plane, and the sphere of radius $1$.

**11.** In the Klein model, compute the distance from the centre to the point at Euclidean distance
$r=\tfrac12$ along a diameter.

**12.** For a point at distance $d=1$ from a line in the hyperbolic plane ($K=-1$), compute the angle of
parallelism $\Pi(1)$.

## Intermediate

**13.** Derive the spherical law of cosines for the unit sphere using vectors: place the vertices at
$(0,0,1)$, $(\sin b,0,\cos b)$ and $(\sin a\cos C,\sin a\sin C,\cos a)$, and compute the dot product.

**14.** On the unit sphere, let $a=60^\circ$, $b=45^\circ$ and $C=60^\circ$. Find $c$.

**15.** An equilateral spherical triangle on the unit sphere has all angles $72^\circ$. Find its area and
explain why twenty congruent copies tile the sphere.

**16.** In the Poincaré disk, find the complete geodesic through $\tfrac12$ and $\tfrac{i}{2}$. Give the
centre and radius of the Euclidean circle, and verify orthogonality to the boundary.

**17.** Show that the maps $z\mapsto -z$ and $z\mapsto\bar z$ are isometries of the Poincaré disk.

**18.** In the upper half-plane, verify that the semicircle $|z|=1$, $\operatorname{Im}z>0$, is a geodesic.
(Use the geodesic equations or the orthogonality criterion.)

**19.** Compare the areas of a hyperbolic disk of radius $2$ ($K=-1$), a Euclidean disk of radius $2$, and a
spherical disk of radius $1$ on a sphere of radius $2$.

**20.** Prove that the summit angles of a Saccheri quadrilateral are equal in neutral geometry.

**21.** In the hyperbolic plane with $K=-1$, a triangle has $a=b=1$ and $C=120^\circ$. Find $c$.

**22.** London is at $51.5^\circ\text{N}$, $0.1^\circ\text{W}$; New York is at $40.7^\circ\text{N}$,
$74^\circ\text{W}$. Use the spherical law of cosines to estimate the great-circle distance, taking
$R=6371$ km.

## Advanced

**23.** Prove Girard's theorem: for a spherical triangle on $S^2_R$ with angles $A,B,C$,
$\operatorname{area}(T)=R^2(A+B+C-\pi)$.

**24.** Prove the spherical sine law for the unit sphere using the vector identity
$(u\times v)\times(u\times w)=[u\cdot(v\times w)]u$.

**25.** Prove the hyperbolic law of cosines $\cosh c=\cosh a\cosh b-\sinh a\sinh b\cos C$ using the
hyperboloid model.

**26.** Prove that every nondegenerate hyperbolic triangle has angle sum strictly less than $\pi$, using the
Poincaré disk and a comparison with a Euclidean triangle.

**27.** Derive the angle-of-parallelism formula $\tan(\Pi(d)/2)=e^{-d}$ in the upper half-plane.

**28.** Show that the Cayley transform $z\mapsto i(1+z)/(1-z)$ is an isometry from the Poincaré disk with
metric $4|dz|^2/(1-|z|^2)^2$ to the upper half-plane with metric $|dz|^2/(\operatorname{Im}z)^2$.

**29.** Derive the formulas $C(r)=2\pi\sinh r$ and $A(r)=2\pi(\cosh r-1)$ for hyperbolic circles and disks
of radius $r$ in the unit-curvature plane.

**30.** Prove that two hyperbolic triangles with the same angles are congruent (AAA).

**31.** Prove that an ideal hyperbolic triangle has area $\pi$ (curvature $K=-1$).

## Challenge

**32.** A regular hyperbolic tiling $\{p,q\}$ consists of regular $p$-gons, $q$ meeting at each vertex. Show
that it exists exactly when $1/p+1/q<1/2$, and compute the area of one $p$-gon for $\{7,3\}$ and $\{8,3\}$.

**33.** Starting from Gauss–Bonnet for a geodesic triangle, derive the area formulas
$\operatorname{area}=R^2(A+B+C-\pi)$ for the sphere, $\operatorname{area}=0$ constraint for the plane, and
$\operatorname{area}=R^2(\pi-A-B-C)$ for the hyperbolic plane. Check the signs and the limits $R\to\infty$.

**34.** In the Klein model, let $\ell$ be a chord and $P$ an interior point not on $\ell$. Prove that there
are infinitely many chords through $P$ that do not meet $\ell$, and identify exactly two **limiting**
parallels.

**35.** A hyperbolic quadrilateral has interior angles $A,B,C,D$ (curvature $K=-1$). Prove
$A+B+C+D<2\pi$ and $\operatorname{area}=2\pi-(A+B+C+D)$.

**36.** Spherical geometry has no parallel lines, yet it cannot be used to prove that the parallel postulate
is independent of neutral geometry. Explain why by listing at least three axioms of neutral geometry that
spherical geometry fails, with proofs or counterexamples. Then state which model does prove independence and
why.
