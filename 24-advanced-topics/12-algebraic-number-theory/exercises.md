# Algebraic Number Theory — Exercises

> [Algebraic Number Theory](README.md) · 36 problems · Beginner → Challenge · Solutions: [solutions.md](solutions.md)

Attempt every problem in writing before looking at the answers. Problems marked *(proof)* require a
complete argument with every hypothesis stated. Theorem numbers refer to [README.md](README.md).

**Notation.** $K$ is a number field, $\mathcal{O}_K$ its ring of integers, $n = [K:\mathbb{Q}]$,
$\Delta_K$ its discriminant, $N$ and $T$ the norm and trace, $\mathrm{Cl}_K$ the class group and $h_K$
its order. For a quadratic field $K = \mathbb{Q}(\sqrt d)$ we write $\alpha = \sqrt d$. Ideals are
written $\mathfrak{a}, \mathfrak{p}, \mathfrak{q}$; the norm of an ideal is $N(\mathfrak{a}) = \lvert\mathcal{O}_K/\mathfrak{a}\rvert$.
$\omega = (1+\sqrt{-3})/2$ denotes the primitive cube root of unity $(1+\sqrt{-3})/2$. "UFD" means
unique factorisation domain and "PID" means principal ideal domain.

## Beginner

**1.** Compute $\mathcal{O}_K$ and $\Delta_K$ for $K = \mathbb{Q}(\sqrt{-2})$, $\mathbb{Q}(\sqrt{-7})$,
$\mathbb{Q}(\sqrt3)$, $\mathbb{Q}(\sqrt{13})$ and $\mathbb{Q}(\sqrt{-11})$, using Theorem 7.1.

**2.** For each element compute the norm, the trace and the minimal polynomial: (a) $1+2\sqrt{-2}$ in
$\mathbb{Q}(\sqrt{-2})$; (b) $3-\sqrt5$ in $\mathbb{Q}(\sqrt5)$; (c) $2+\sqrt{-7}$ in $\mathbb{Q}(\sqrt{-7})$.

**3.** *(proof)* Show that $\frac{1+\sqrt{13}}{2}$ is an algebraic integer, and deduce that
$[\mathcal{O}_{\mathbb{Q}(\sqrt{13})} : \mathbb{Z}[\sqrt{13}]] = 2$.

**4.** *(proof)* Show that $\mathbb{Z}[\sqrt5]$ is not integrally closed in $\mathbb{Q}(\sqrt5)$, while
$\mathbb{Z}[\sqrt{-5}]$ is integrally closed in $\mathbb{Q}(\sqrt{-5})$.

**5.** *(proof)* Show that $\alpha = \sqrt2+\sqrt3$ is an algebraic integer by exhibiting a monic polynomial
over $\mathbb{Z}$ satisfied by $\alpha$. What is its degree over $\mathbb{Q}$?

**6.** Compute $\operatorname{disc}(x^3-x+1)$ and $\operatorname{disc}(x^3+x+1)$ using the formula
$\operatorname{disc}(x^3+px+q) = -4p^3-27q^2$.

**7.** Determine the unit groups of $\mathbb{Z}[i]$ and $\mathbb{Z}[\sqrt{-5}]$, proving that no other
elements are units.

**8.** Determine the splitting type and the explicit prime ideal factorisation of $3$ and $17$ in
$\mathbb{Q}(i)$.

**9.** Determine the splitting type and the explicit prime ideal factorisation of $11$ and $29$ in
$\mathbb{Q}(\sqrt{-5})$.

**10.** Compute the continued fraction of $\sqrt7$, the fundamental solution of $x^2-7y^2=1$, and the next
two positive solutions.

**11.** *(proof)* Show that $(1+i)$ is a prime ideal of $\mathbb{Z}[i]$, compute its norm, and exhibit $2$
as a unit times $(1+i)^2$.

**12.** Factor the principal ideal $(7)$ in $\mathbb{Z}[\sqrt2]$, exhibiting explicit generators of the
prime ideals.

## Intermediate

**13.** *(proof)* For $K = \mathbb{Q}(\sqrt d)$ and $\alpha = a+b\sqrt d \ne 0$, prove directly that
$[\mathcal{O}_K : \alpha\mathcal{O}_K] = \lvert a^2-db^2\rvert$ by computing the determinant of
multiplication by $\alpha$ in the basis $1,\sqrt d$.

**14.** Factor the principal ideal $(10)$ into prime ideals in $\mathbb{Z}[i]$ and in $\mathbb{Z}[\sqrt{-5}]$.

**15.** *(proof)* In $\mathbb{Z}[\sqrt{-5}]$ let $\mathfrak{q} = (3, 1+\alpha)$ with $\alpha = \sqrt{-5}$.
Prove that $\mathfrak{q}\bar{\mathfrak{q}} = (3)$, that $\mathfrak{q}$ is not principal, and that
$\mathfrak{q}^2 = (2-\alpha)$.

**16.** Compute the Minkowski bound for $K = \mathbb{Q}(\sqrt{-11})$, $\mathbb{Q}(\sqrt{17})$ and
$\mathbb{Q}(\sqrt{-3})$, and state what each bound proves about $h_K$.

**17.** *(proof)* Prove that $h_K = 1$ for $K = \mathbb{Q}(\sqrt{-2})$ and $K = \mathbb{Q}(\sqrt{-3})$ by
the Minkowski bound, checking all ideals of small norm.

**18.** *(proof)* Show that $3$ is irreducible but not prime in $\mathbb{Z}[\sqrt{-5}]$.

**19.** *(proof)* Prove that a rational prime $p \equiv 3 \pmod 4$ remains prime in $\mathbb{Z}[i]$.

**20.** *(proof)* Using the splitting law and the fact that $\mathbb{Z}[i]$ is a UFD, prove that every
prime $p \equiv 1 \pmod 4$ is a sum of two integer squares.

**21.** Compute the regulators of $\mathbb{Q}(\sqrt5)$ and $\mathbb{Q}(\sqrt2)$, and verify the analytic
class number formula (7.4) for each using the known residues.

**22.** *(proof)* Prove that $x^2-2y^2=-1$ has infinitely many solutions in positive integers, and give the
first three.

## Advanced

**23.** *(proof)* Prove Proposition 5.10 in the quadratic case: if $\alpha_1,\alpha_2 \in \mathcal{O}_K$ form
a $\mathbb{Q}$-basis and $M = \mathbb{Z}\alpha_1+\mathbb{Z}\alpha_2$, then
$\operatorname{disc}(\alpha_1,\alpha_2) = [\mathcal{O}_K:M]^2\Delta_K$.

**24.** *(proof)* Prove that for $\alpha \ne 0$, $N((\alpha)) = \lvert N_{K/\mathbb{Q}}(\alpha)\rvert$.

**25.** *(proof)* Prove that the ideal norm is multiplicative: $N(\mathfrak{a}\mathfrak{b}) = N(\mathfrak{a})N(\mathfrak{b})$
for nonzero integral ideals.

**26.** *(proof)* Prove Theorem 7.10 in both directions: $\mathcal{O}_K$ is a UFD if and only if $h_K = 1$.
State clearly where unique factorisation of ideals is used.

**27.** *(proof)* Prove that $\mathcal{O}_K$ is integrally closed in $K$, and that every nonzero prime ideal
is maximal.

**28.** *(proof)* For a quadratic field $K$ and a rational prime $p$, prove the fundamental identity
$\sum_{i=1}^{g}e_if_i = 2$ directly from the Chinese remainder theorem applied to
$\mathcal{O}_K/p\mathcal{O}_K$.

**29.** *(proof)* Compute the class group of $K = \mathbb{Q}(\sqrt{10})$, showing that every class contains an
ideal of norm at most $4$ and that $h_K = 2$.

**30.** *(proof)* Prove that $\mathbb{Z}[i]$ is Euclidean for the norm $N(a+bi) = a^2+b^2$, and deduce that
it is a UFD.

**31.** *(proof)* Prove the real quadratic case of Dirichlet's unit theorem: if $K = \mathbb{Q}(\sqrt d)$ with
$d>0$ squarefree, then $\mathcal{O}_K^\times \cong \{\pm1\}\times\mathbb{Z}$, by exhibiting a fundamental unit
and proving by descent that it generates.

## Challenge

**32.** *(proof)* Verify the analytic class number formula for $K = \mathbb{Q}(\sqrt{-6})$ by computing
$L(1,\chi_{-24})$ explicitly and checking that it equals the residue predicted by (7.4).

**33.** *(proof)* Prove that there are infinitely many primes $p \equiv 1 \pmod 4$, using unique factorisation
in $\mathbb{Z}[i]$.

**34.** *(proof)* Determine all squarefree $d$ with $\lvert d\rvert \le 10$ for which $h_{\mathbb{Q}(\sqrt d)} = 1$,
justifying each answer with the Minkowski bound and a principality test.

**35.** *(proof)* Prove that $\mathbb{Z}[\omega]$ with $\omega = (1+\sqrt{-3})/2$ is Euclidean for the norm
$N(a+b\omega) = a^2+ab+b^2$, and deduce that a prime $p \equiv 1 \pmod 3$ can be written $p = x^2+3y^2$.

**36.** *(proof)* Verify the analytic class number formula for $K = \mathbb{Q}(\sqrt5)$, using
$L(1,\chi_5) = \frac{2}{\sqrt5}\log\frac{1+\sqrt5}{2}$, and deduce a numerical value for $h_KR_K$.
