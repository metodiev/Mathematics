# Geometric Transformations — Exercises

> [Tutorial](README.md) · 35 problems · Levels: Beginner, Intermediate, Advanced, Challenge

Draw each figure on squared paper before computing, and check every image by comparing lengths and, where
relevant, orientation. For composition problems, write the order explicitly — rightmost transformation
first. Full solutions are in [solutions.md](solutions.md); do not open that file until you have attempted
the problems.

## Beginner

**1.** Translate the point $(-4,5)$ by the vector $(6,-3)$.

**2.** Rotate $(-2,5)$ through $90^\circ$ anticlockwise about the origin.

**3.** Rotate $(-3,4)$ through $180^\circ$ about the origin.

**4.** Reflect $(5,-3)$ in (a) the $x$-axis and (b) the $y$-axis.

**5.** Reflect $(2,7)$ in the line $y=x$.

**6.** Dilate $(6,-9)$ with centre the origin and factor $\tfrac13$.

**7.** Write down the $2\times2$ matrix of the rotation through $90^\circ$ about the origin, and use it to
find the image of $(1,0)$.

**8.** Identify the transformation $(x,y)\mapsto(x+4,\ y-1)$.

**9.** Identify the transformation $(x,y)\mapsto(-x,\ y)$.

**10.** Identify the transformation $(x,y)\mapsto(2x,\ 2y)$.

**11.** Identify the transformation $(x,y)\mapsto(y,\ x)$.

**12.** For each of a regular decagon, a non-square rhombus, an isosceles triangle that is not equilateral,
and a scalene triangle, state the number of lines of symmetry and the order of rotational symmetry.

## Intermediate

**13.** Rotate $(3,4)$ through $60^\circ$ anticlockwise about the origin, giving exact values.

**14.** Let $T$ be the translation by $(2,1)$ and $R$ the rotation through $90^\circ$ about the origin.
Compute $(R\circ T)(1,1)$ and $(T\circ R)(1,1)$, and comment.

**15.** Find the image of the line $y=-3x+2$ under reflection in the $y$-axis.

**16.** Find the image of the line $y=2x+3$ under the rotation through $90^\circ$ about the origin.

**17.** Let $g(x,y)=(x-4,\ -y)$. Find its fixed points, compute $g\circ g$, and find $g^{-1}$.

**18.** Rotate $(5,2)$ through $90^\circ$ about the point $(2,1)$.

**19.** Dilate $(5,1)$ with centre $(2,3)$ and factor $2$.

**20.** Describe the symmetry group of a regular pentagon: how many elements, how many rotations, how many
reflections?

**21.** Describe the composition of the reflections in the lines $x=1$ and $x=4$, in both orders. What is
the resulting transformation in each case?

**22.** A triangle with vertices $A(1,1)$, $B(3,1)$, $C(1,2)$ is mapped to $(3,3)$, $(7,3)$, $(3,5)$.
Identify the transformation, including its centre and factor.

**23.** Show that a rotation by $30^\circ$ about the origin followed by a rotation by $60^\circ$ about the
origin is a rotation by $90^\circ$, and verify this on the point $(2,0)$.

**24.** Verify that the matrix $\begin{pmatrix}0&1\\1&0\end{pmatrix}$ is orthogonal and has determinant
$-1$. Which transformation does it represent?

## Advanced

**25.** Prove from the coordinate formula that a rotation about the origin preserves distance. (Use the
trigonometric identity $\cos^2\theta+\sin^2\theta=1$.)

**26.** Prove that the composition of the reflections in two lines through the origin, at angles $\alpha$
and $\beta$, is a rotation about the origin through $2(\beta-\alpha)$.

**27.** Let $T$ be an isometry with $T(0,0)=(0,0)$. Prove that $T$ is linear, i.e. $T(u+v)=T(u)+T(v)$ and
$T(\lambda u)=\lambda T(u)$, and that its matrix $A$ satisfies $A^{\mathsf T}A=I$. (This is the fact used
in the classification of isometries.)

**28.** Classify the $2\times2$ orthogonal matrices by determinant: prove that those with determinant $+1$
are rotation matrices and those with determinant $-1$ are reflection matrices.

**29.** Prove that the only regular polygons that tile the plane are the equilateral triangle, the square
and the regular hexagon.

**30.** Prove that a regular pentagon cannot tile the plane by the angle argument. (You may remark on the
fact that irregular pentagons can.)

**31.** For a glide reflection $g=T_v\circ r_\ell$ with $v\parallel\ell$ and $v\ne0$, prove that $g^{-1}$
is also a glide reflection with the same axis, and identify its glide vector.

## Challenge

**32.** Prove the crystallographic restriction: if a rotation by angle $\theta$ is a symmetry of a
two-dimensional lattice, then $\theta$ is a multiple of $90^\circ$, $60^\circ$, $120^\circ$ or $180^\circ$.
Deduce that only rotational orders $1,2,3,4,6$ occur.

**33.** Prove that the symmetry group of a non-square rectangle has exactly four elements, and show that
every pair of elements commutes. (This group is the Klein four-group.)

**34.** Suppose a figure $F$ has two lines of symmetry $\ell_1$ and $\ell_2$ meeting at a point $O$ at
angle $\theta$. Prove that $F$ has a rotational symmetry about $O$ through $2\theta$. Deduce that a figure
with two perpendicular axes of symmetry has half-turn symmetry.

**35.** Prove that a glide reflection has no fixed points. Conversely, prove that an
orientation-reversing isometry with no fixed points is a glide reflection. (Hint: reduce the matrix part
to $\begin{pmatrix}1&0\\0&-1\end{pmatrix}$ by a rotation of coordinates, then read off the fixed set.)
