# Homological Algebra — Exercises

> [Homological Algebra](README.md) · 36 problems · Beginner → Challenge · Solutions: [solutions.md](solutions.md)

Attempt every problem in writing before consulting [solutions.md](solutions.md). Problems marked
*(proof)* require a complete argument with all hypotheses stated. Section references point into
[README.md](README.md).

**Notation.** $R$ is a ring with $1$ and $R\text{-}\mathbf{Mod}$ is the category of left $R$-modules.
$\operatorname{Ext}^n_R$ and $\operatorname{Tor}_n^R$ are the derived functors of Hom and tensor.
$\mathbb{Z}G$ is the group ring, $M^G$ the invariants and $M_G$ the coinvariants of a $G$-module $M$.
$\operatorname{Der}(G,M)$ is the group of derivations and $\operatorname{Inn}(G,M)$ the subgroup of
principal derivations. All complexes are concentrated in nonnegative degrees unless stated otherwise.

## Beginner

**1.** Compute the homology of the chain complex
$$0 \to \mathbb{Z} \xrightarrow{\ \times 3\ } \mathbb{Z} \xrightarrow{\ 0\ } \mathbb{Z} \to 0.$$

**2.** Determine whether each of the following sequences is exact. Justify each answer.
(a) $0 \to \mathbb{Z} \xrightarrow{2} \mathbb{Z} \to \mathbb{Z}/2 \to 0$;
(b) $0 \to \mathbb{Z}/2 \xrightarrow{2} \mathbb{Z}/4 \to \mathbb{Z}/2 \to 0$;
(c) $0 \to \mathbb{Z} \xrightarrow{2} \mathbb{Z} \to \mathbb{Z}/4 \to 0$.

**3.** *(proof)* Prove that every free $R$-module is projective, and prove that $\mathbb{Z}/2$ is not a
projective $\mathbb{Z}$-module.

**4.** *(proof)* Prove that $\mathbb{Q}$ is an injective $\mathbb{Z}$-module and that $\mathbb{Z}$ is
not injective.

**5.** Compute $\operatorname{Hom}_{\mathbb{Z}}(\mathbb{Z}/n,\mathbb{Z})$ and
$\operatorname{Hom}_{\mathbb{Z}}(\mathbb{Z}/n,\mathbb{Z}/m)$ for $n,m \ge 1$.

**6.** *(proof)* Prove that $\operatorname{Hom}_{\mathbb{Z}}(-,\mathbb{Z})$ is left exact but not exact,
using the short exact sequence $0 \to \mathbb{Z} \xrightarrow{2} \mathbb{Z} \to \mathbb{Z}/2 \to 0$.

**7.** *(proof)* Prove that $-\otimes_{\mathbb{Z}} \mathbb{Z}/2$ is right exact but not exact, using the
same short exact sequence.

**8.** Write down a projective resolution of $\mathbb{Z}/6$ over $\mathbb{Z}$ and a projective
resolution of $\mathbb{Z}/2$ over $\mathbb{Z}$. Verify exactness.

**9.** Write down an injective resolution of $\mathbb{Z}$ over $\mathbb{Z}$ and an injective resolution
of $\mathbb{Z}/3$ over $\mathbb{Z}$. Verify exactness.

**10.** *(proof)* Let $0 \to A \to B \to C \to 0$ be a short exact sequence of $R$-modules. Prove that
the sequence splits if $C$ is projective. State and prove the dual statement for $A$ injective.

**11.** Compute $\operatorname{Ext}^0_{\mathbb{Z}}(\mathbb{Z}/12,\mathbb{Z}/18)$ and
$\operatorname{Tor}_0^{\mathbb{Z}}(\mathbb{Z}/12,\mathbb{Z}/18)$.

**12.** *(proof)* Let $0 \to A \to B \to C \to 0$ be exact with $C$ free. Prove that
$B \cong A \oplus C$. Does the conclusion hold if $C$ is only projective?

## Intermediate

**13.** Compute $\operatorname{Ext}^n_{\mathbb{Z}}(\mathbb{Z}/12,\mathbb{Z}/18)$ for all $n \ge 0$.
Show every step.

**14.** Compute $\operatorname{Tor}_n^{\mathbb{Z}}(\mathbb{Z}/12,\mathbb{Z}/18)$ for all $n \ge 0$.
Compare with Exercise 13 and explain the agreement.

**15.** Compute $\operatorname{Ext}^1_{k[x]}(k,k)$ and $\operatorname{Tor}_1^{k[x]}(k,k)$, where
$k$ is a field and $x$ acts on $k$ by zero.

**16.** Compute $\operatorname{Ext}^1_{k[x]}(k[x]/(x^2),k)$ and
$\operatorname{Tor}_1^{k[x]}(k[x]/(x^2),k)$.

**17.** *(proof)* Construct the map from equivalence classes of extensions of $M$ by $N$ to
$\operatorname{Ext}^1_R(M,N)$ and prove that it is well defined. Show that the class of a split
extension is zero.

**18.** Compute $H^n(C_3,\mathbb{Z})$ for all $n \ge 0$, where $C_3$ acts trivially on $\mathbb{Z}$.

**19.** *(proof)* Prove that $H^1(G,M) \cong \operatorname{Der}(G,M)/\operatorname{Inn}(G,M)$ and that
$H_1(G,\mathbb{Z}) \cong G^{\mathrm{ab}}$.

**20.** *(proof)* Prove the five lemma for modules.

**21.** *(proof)* Prove the horseshoe lemma: given $0 \to A \to B \to C \to 0$ and projective
resolutions of $A$ and $C$, construct a projective resolution of $B$ fitting into a short exact
sequence of complexes.

**22.** *(proof)* Prove dimension shifting for Ext: if $0 \to K \to P \to M \to 0$ is exact with $P$
projective, then $\operatorname{Ext}^{n+1}_R(M,N) \cong \operatorname{Ext}^n_R(K,N)$ for all $n \ge 0$.

**23.** Let $R = k[x,y]$ and let $k$ be the module with $x = y = 0$. Using the Koszul resolution,
compute $\operatorname{Tor}_i^R(k,k)$ for all $i$.

**24.** *(proof)* Let $0 \to A \to B \to C \to 0$ be exact. Prove that if $A$ and $C$ are flat, then
$B$ is flat.

## Advanced

**25.** *(proof)* Prove that the long exact sequence in homology is natural: a commutative diagram of
short exact sequences of chain complexes induces a commutative ladder of long exact sequences.

**26.** *(proof)* Prove the comparison theorem for projective resolutions: existence of a chain map
lifting a given module map, and uniqueness up to chain homotopy.

**27.** *(proof)* Prove that $\operatorname{Ext}^n_R(M,N) = 0$ for $n > 0$ whenever $M$ is projective
or $N$ is injective. Then prove that $\operatorname{Tor}_n^R(M,N) = 0$ for $n > 0$ whenever $M$ is
flat.

**28.** *(proof)* Use dimension shifting to prove that for $m \ge 1$ and any abelian group $N$,
$$\operatorname{Ext}^n_{\mathbb{Z}}(\mathbb{Z}/m,N) \cong \begin{cases} N/mN, & n = 1,\\ 0, & n \ge 2.\end{cases}$$

**29.** *(proof)* Starting from the bar resolution, derive the standard cochain formula for
$H^n(G,M)$ and identify $H^0$ and $H^1$ explicitly.

**30.** *(proof)* Let $G$ be a finite group and $M$ a $G$-module. Prove that $|G|$ annihilates
$H^n(G,M)$ for every $n \ge 1$.

**31.** *(proof)* State and prove the five-term exact sequence associated with a first-quadrant
cohomological spectral sequence converging to $H^*$:
$$0 \to E_2^{1,0} \to H^1 \to E_2^{0,1} \xrightarrow{d_2} E_2^{2,0} \to H^2.$$

**32.** *(proof)* Prove that the category $\mathbf{Ch}(R)$ of chain complexes of $R$-modules is
abelian, describing kernels, cokernels, monomorphisms, epimorphisms and exact sequences degreewise.

## Challenge

**33.** *(proof)* Use the Freyd–Mitchell embedding theorem to prove that the five lemma holds in every
abelian category. Explain carefully why the embedding can be chosen to preserve the finite diagram
appearing in the statement.

**34.** *(proof)* Let $1 \to N \to G \to Q \to 1$ be a group extension and let $M$ be a $G$-module.
Construct the Lyndon–Hochschild–Serre spectral sequence
$$E_2^{p,q} = H^p\bigl(Q, H^q(N,M)\bigr) \Longrightarrow H^{p+q}(G,M),$$
and derive from it the five-term inflation-restriction sequence.

**35.** *(proof)* Use the Serre spectral sequence of the path–loop fibration
$\Omega S^n \to P S^n \to S^n$, whose total space is contractible, to compute
$H_*(\Omega S^2;\mathbb{Q})$ and $H_*(\Omega S^3;\mathbb{Q})$. Explain how the differentials are forced.

**36.** *(proof)* Prove that $\operatorname{Tor}_1^R(M,-)$ commutes with filtered colimits. Deduce
that every module is a filtered colimit of finitely presented modules, and use this to show that
flatness of $M$ can be tested on finitely generated ideals: $M$ is flat iff
$\operatorname{Tor}_1^R(M,R/I) = 0$ for every finitely generated left ideal $I$.
