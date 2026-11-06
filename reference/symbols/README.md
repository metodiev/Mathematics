# Symbol Reference

This page answers one question: *what does that symbol mean?* It is arranged for lookup, not for
teaching — the rows are ordered by symbol (punctuation and operators first, then Latin letters, then
Greek letters), so a symbol met in a text can be found by scanning the left-hand column. Every row
carries a true example, because a definition you cannot instantiate is a definition you do not yet
own.

The full conventions — how symbols are typeset, how they are read aloud, which bracket means what —
live in [MATHEMATICAL_NOTATION.md](../../MATHEMATICAL_NOTATION.md). This page is deliberately narrower:
one row per symbol, no paragraphs of explanation, and a separate section for symbols that carry more
than one meaning.

## 1. How to Read These Tables

* **Symbol** is written in LaTeX, exactly as it is rendered in this repository.
* **Name** is the standard spoken name; where a symbol has several names, the commonest comes first.
* **Meaning** is the definition in one line. A condition written here is part of the meaning.
* **Example** is a true instance. An example of the form $x=2$ means "specialise the symbols this
  way and the statement is correct".

Rows are sorted by the symbol itself within each table. The division is by role rather than by
alphabet: $d$ as a differential and $\Delta$ as a change are listed with the operators because that is
how they are most often met, and section 5 resolves the remaining collisions.

## 2. Symbols That Are Not Letters

| Symbol | Name | Meaning | Example |
|---|---|---|---|
| $+$ | plus | addition | $3+4=7$ |
| $-$ | minus | subtraction, or negation of a single quantity | $7-4=3$; $-x$ is the additive inverse of $x$ |
| $\pm$ | plus-minus | two values differing in one sign, taken consistently | $x^2=9 \iff x=\pm3$ |
| $\mp$ | minus-plus | the opposite sign to a preceding $\pm$ | $\cos(A\pm B)=\cos A\cos B\mp\sin A\sin B$ |
| $\times$ | times | multiplication of numbers; Cartesian product of sets | $4\times5=20$; $A\times B=\{(a,b):a\in A,\ b\in B\}$ |
| $\cdot$ | dot | multiplication; dot product of vectors | $3\cdot4=12$; $\mathbf{u}\cdot\mathbf{v}=u_1v_1+u_2v_2+u_3v_3$ |
| $\div$ | divided by | division | $12\div4=3$ |
| $/$ | slash | quotient | $3/4=\dfrac{3}{4}$ |
| $=$ | equals | the two sides have the same value (a claim, not a command) | $2+2=4$ |
| $\ne$ | not equal | the two sides differ | $\pi\ne3.14$ |
| $\approx$ | approximately equal | equal to within the stated precision | $\pi\approx3.14159$ |
| $<$ | less than | strict order | $2<3$ |
| $\le$ | at most | $x\le y$ means $x<y$ or $x=y$ | $x^2\ge0$ for all real $x$ |
| $\ll$ | much less than | informal order-of-magnitude comparison, not a defined relation | $10^{-9}\ll1$ |
| $\propto$ | proportional to | $x=ky$ for some constant $k\ne0$ | the area of a circle is $\propto r^2$ |
| $\equiv$ | identically equal; congruent | an identity, or congruence modulo $n$ | $\sin^2x+\cos^2x\equiv1$; $7\equiv2\pmod5$ |
| $:=$ | defined as | introduces a definition and nothing else | $e:=\lim_{n\to\infty}\left(1+\frac1n\right)^n$ |
| $\infty$ | infinity | a limit symbol or a statement about size; not a real number | $\lim_{x\to\infty}\frac1x=0$ |
| $\%$ | percent | per hundred | $7\%=\dfrac{7}{100}=0.07$ |
| $^\circ$ | degree | angle unit with $1^\circ=\pi/180$ rad | $90^\circ=\pi/2$ |
| $'$ | prime | derivative, or a distinguished second object | $f'(x)=2x$ for $f(x)=x^2$; $A'$ a reflected point |
| $\sqrt{\ }$ | square root | the non-negative root | $\sqrt9=3$ |
| $\sqrt[n]{\ }$ | $n$-th root | the real root for odd $n$; the non-negative root for even $n$ | $\sqrt[3]{-8}=-2$; $\sqrt[4]{16}=2$ |
| $\lvert x\rvert$ | absolute value | distance from $x$ to $0$ | $\lvert-3\rvert=3$ |
| $\lfloor x\rfloor$ | floor | greatest integer $\le x$ | $\lfloor2.7\rfloor=2$; $\lfloor-2.3\rfloor=-3$ |
| $\lceil x\rceil$ | ceiling | least integer $\ge x$ | $\lceil2.1\rceil=3$; $\lceil-2.1\rceil=-2$ |
| $!$ | factorial | $n!=1\cdot2\cdots n$ with $0!=1$ | $5!=120$ |
| $\binom{n}{k}$ | binomial coefficient | $\dfrac{n!}{k!\,(n-k)!}$ for $0\le k\le n$ | $\binom52=10$ |
| $\sum$ | sum | indexed addition | $\sum_{k=1}^{4}k=10$ |
| $\prod$ | product | indexed multiplication | $\prod_{k=1}^{4}k=24$ |
| $\int$ | integral | antiderivative, or signed area | $\int_0^1x\,dx=\dfrac12$ |
| $\oint$ | contour integral | integral around a closed curve | $\oint_{\lvert z\rvert=1}\dfrac{dz}{z}=2\pi i$ |
| $\partial$ | partial | partial derivative | $\dfrac{\partial}{\partial x}(x^2y)=2xy$ |
| $\partial A$ | boundary of $A$ | points every neighbourhood of which meets both $A$ and its complement | $\partial[0,1]=\{0,1\}$ |
| $\nabla$ | nabla, del | gradient operator | $\nabla f=(f_x,f_y)$ |
| $\Delta$ | delta | change in a quantity; also the Laplacian | $\Delta x=x_2-x_1$; $\Delta f=\nabla\cdot\nabla f$ |
| $d$ | dee | differential, or the differential of a function | $df=f'(x)\,dx$ |
| $\neg$ | not | negation | $\neg(P\land Q)$ |
| $\land$ | and | conjunction | $P\land Q$ is true only when both are true |
| $\lor$ | or | disjunction, inclusive unless stated | $P\lor Q$ |
| $\oplus$ | xor; direct sum | exactly one of the two; or a direct sum of spaces | $P\oplus Q$; $V\oplus W$ |
| $\Rightarrow$ | implies | if the left is true then the right is true | $x=2\Rightarrow x^2=4$ |
| $\Leftrightarrow$ | if and only if | the two statements have the same truth value | $x^2=4\Leftrightarrow x=\pm2$ over $\mathbb{R}$ |
| $\forall$ | for all | universal quantifier | $\forall x\in\mathbb{R},\ x^2\ge0$ |
| $\exists$ | there exists | existential quantifier | $\exists x\in\mathbb{R},\ x^2=2$ |
| $\exists!$ | there exists uniquely | existence together with uniqueness | $\exists!x\in\mathbb{R},\ x+3=5$ |
| $\vdash$ | turnstile | is provable from | $\{\varphi,\ \varphi\to\psi\}\vdash\psi$ |
| $\models$ | models, entails | is true in every model of | $\{\varphi,\ \varphi\to\psi\}\models\psi$ |
| $\therefore$ | therefore | introduces a conclusion | $x=2\therefore x^2=4$ |
| $\because$ | because | introduces a reason | $2\mid n$, because $n=2k$ |
| $\blacksquare$ | end of proof | marks a completed proof | — |
| $\in$ | is an element of | membership | $3\in\mathbb{N}$ |
| $\notin$ | is not an element of | non-membership | $\tfrac12\notin\mathbb{Z}$ |
| $\subseteq$ | subset | every element of the left is in the right | $\mathbb{N}\subseteq\mathbb{Z}$ |
| $\subsetneq$ | proper subset | subset and not equal | $\mathbb{N}\subsetneq\mathbb{Z}$ |
| $\cup$ | union | elements in either set | $\{1,2\}\cup\{2,3\}=\{1,2,3\}$ |
| $\cap$ | intersection | elements in both sets | $\{1,2\}\cap\{2,3\}=\{2\}$ |
| $\setminus$ | set difference | elements of the left not in the right | $\{1,2,3\}\setminus\{2\}=\{1,3\}$ |
| $\triangle$ | symmetric difference | elements in exactly one of the two | $\{1,2\}\triangle\{2,3\}=\{1,3\}$ |
| $\varnothing$ | empty set | the set with no elements | $\{x\in\mathbb{R}:x^2<0\}=\varnothing$ |
| $\mathcal{P}(A)$ | power set | the set of all subsets of $A$ | $\lvert\mathcal{P}(\{1,2\})\rvert=4$ |
| $\lvert A\rvert$ | cardinality | number of elements of a finite set | $\lvert\{2,4,6\}\rvert=3$ |
| $\bigcup_{i\in I}A_i$ | indexed union | elements in at least one $A_i$ | $\bigcup_{n\ge1}[-n,n]=\mathbb{R}$ |
| $\bigcap_{i\in I}A_i$ | indexed intersection | elements in every $A_i$ | $\bigcap_{n\ge1}\left(0,\tfrac1n\right)=\varnothing$ |
| $\sqcup$ | disjoint union | union of sets declared pairwise disjoint | $\{1,2\}\sqcup\{3\}$ |
| $A^{\complement}$ | complement | elements of a fixed universe not in $A$ | $A^{\complement}=\{x\in U:x\notin A\}$ |
| $\perp$ | perpendicular; independent | geometric orthogonality; statistical independence | $u\perp v$; $X\perp\!\!\!\perp Y$ |
| $\parallel$ | parallel | same direction | $l_1\parallel l_2$ |
| $\circ$ | small circle | composition of functions | with $f(x)=x^2$, $g(x)=x+1$: $(f\circ g)(x)=(x+1)^2$ |
| $\mapsto$ | maps to | the rule sending an element to its value | $x\mapsto x^2$ |
| $\to$ | tends to; maps to | a limit arrow, or a function arrow | $x\to0^+$; $f:A\to B$ |
| $\sim$ | distributed as; equivalent; asymptotically like | context decides | $X\sim\mathcal{N}(0,1)$; $\sin x\sim x$ as $x\to0$ |
| $\cong$ | isomorphic; congruent | same structure; same shape and size | $V\cong W$; $\triangle ABC\cong\triangle DEF$ |
| $\langle u,v\rangle$ | inner product | generalised dot product | $\langle(1,0),(0,1)\rangle=0$ |
| $\lVert x\rVert$ | norm | length | $\lVert(3,4)\rVert=5$ |
| $A^{*}$ | star | conjugate transpose of a matrix; convolution of functions | $A^{*}=\overline{A}^{\mathsf{T}}$; $(f*g)(t)=\displaystyle\int f(\tau)g(t-\tau)\,d\tau$ |

## 3. Latin Letters and Letter Combinations

| Symbol | Name | Meaning | Example |
|---|---|---|---|
| $a\mid b$ | divides | $b=ak$ for some $k\in\mathbb{Z}$ | $3\mid12$; $4\nmid10$ |
| $A$ | matrix; area; a set | context decides | $A=(a_{ij})$; $A=\pi r^2$ |
| $A^{\mathsf{T}}$ | transpose | rows and columns exchanged | $(A^{\mathsf{T}})_{ij}=a_{ji}$ |
| $A^{-1}$ | inverse | the matrix with $AA^{-1}=I$; exists iff $\det A\ne0$ | $\begin{pmatrix}2&0\\0&4\end{pmatrix}^{-1}=\begin{pmatrix}1/2&0\\0&1/4\end{pmatrix}$ |
| $B_r(x)$ | open ball | $\{y:d(x,y)<r\}$ | in $\mathbb{R}$, $B_1(0)=(-1,1)$ |
| $C$ | constant of integration | an arbitrary additive constant | $\int2x\,dx=x^2+C$ |
| $\mathbb{C}$ | complex numbers | $\{a+bi: a,b\in\mathbb{R}\}$ with $i^2=-1$ | $3+4i\in\mathbb{C}$ |
| $d(x,y)$ | distance, metric | the distance between two points | $d(x,y)=\lvert x-y\rvert$ on $\mathbb{R}$ |
| $\dim V$ | dimension | size of any basis of $V$ | $\dim\mathbb{R}^3=3$ |
| $e$ | Euler's number | $\lim_{n\to\infty}(1+1/n)^n=2.71828\ldots$ | $e^{i\pi}=-1$ |
| $\mathbb{E}[X]$ | expectation | probability-weighted mean | $\mathbb{E}[X]=\sum_x x\Pr(X=x)$ |
| $f:A\to B$ | function | domain $A$, codomain $B$ | $f:\mathbb{R}\to\mathbb{R}$, $f(x)=x^2$ |
| $f^{-1}$ | inverse function | exists only when $f$ is a bijection | $f(x)=2x+1\Rightarrow f^{-1}(y)=(y-1)/2$ |
| $f'(x)$ | derivative | instantaneous rate of change | $(x^3)'=3x^2$ |
| $i$ | imaginary unit | $i^2=-1$ | $\sqrt{-4}=2i$ |
| $I$ | identity matrix | $1$ on the diagonal, $0$ elsewhere | $I_2=\begin{pmatrix}1&0\\0&1\end{pmatrix}$ |
| $n!$ | factorial | $1\cdot2\cdots n$, with $0!=1$ | $4!=24$ |
| $\mathbb{N}$ | natural numbers | $\{1,2,3,\dots\}$; $\mathbb{N}_0=\{0,1,2,\dots\}$ is written when $0$ is included | $7\in\mathbb{N}$, $0\notin\mathbb{N}$ |
| $O(g)$ | big-O | $\lvert f\rvert\le C\lvert g\rvert$ eventually | $3x^2+1=O(x^2)$ as $x\to\infty$ |
| $o(g)$ | little-o | $f/g\to0$ | $x^2=o(x)$ as $x\to0$ |
| $\Theta(g)$ | big-Theta | bounded above and below by multiples of $g$ | $2x^2+x=\Theta(x^2)$ as $x\to\infty$ |
| $\Omega(g)$ | big-Omega | $\lvert f\rvert\ge c\lvert g\rvert$ eventually | $x^3=\Omega(x^2)$ as $x\to\infty$ |
| $P(A)$, $\Pr(A)$ | probability | a number in $[0,1]$ | $P(A^{\complement})=1-P(A)$ |
| $p$ | prime; probability of success | context decides | $p=7$ is prime; $X\sim\operatorname{Bin}(n,p)$ |
| $\mathbb{Q}$ | rational numbers | quotients $p/q$ with $p,q\in\mathbb{Z}$, $q\ne0$ | $\tfrac23\in\mathbb{Q}$; $\sqrt2\notin\mathbb{Q}$ |
| $s^2$ | sample variance | $\dfrac{1}{n-1}\sum_{i=1}^n(x_i-\bar{x})^2$ | $s^2$ estimates $\sigma^2$ |
| $\operatorname{tr}A$ | trace | sum of the diagonal entries | $\operatorname{tr}\begin{pmatrix}1&2\\3&4\end{pmatrix}=5$ |
| $\operatorname{Var}(X)$ | variance | $\mathbb{E}[(X-\mu)^2]$ | $\operatorname{Var}(X)=\mathbb{E}[X^2]-\mu^2$ |
| $\operatorname{Cov}(X,Y)$ | covariance | $\mathbb{E}[(X-\mu_X)(Y-\mu_Y)]$ | $\operatorname{Cov}(X,X)=\operatorname{Var}(X)$ |
| $\operatorname{Re}z$, $\operatorname{Im}z$ | real and imaginary parts | $z=\operatorname{Re}z+i\operatorname{Im}z$ | $\operatorname{Re}(3+4i)=3$ |
| $\arg z$ | argument | angle in polar form | $z=r e^{i\arg z}$ |
| $\lvert z\rvert$ | modulus | distance from $z$ to $0$ in the plane | $\lvert3+4i\rvert=5$ |
| $\det A$ | determinant | signed volume scaling factor | $\det\begin{pmatrix}1&2\\3&4\end{pmatrix}=-2$ |
| $\operatorname{rank}A$ | rank | dimension of the column space | $\operatorname{rank}\begin{pmatrix}1&0\\0&0\end{pmatrix}=1$ |
| $\mathbb{R}$ | real numbers | the complete ordered field | $\pi\in\mathbb{R}$; $\sqrt2\in\mathbb{R}$ |
| $\ker T$ | kernel | $\{v:Tv=0\}$ | $\ker(x\mapsto2x)=\{0\}$ |
| $\operatorname{im}T$ | image | $\{Tv:v\in V\}$ | $\operatorname{im}(x\mapsto2x)=\mathbb{R}$ |
| $\operatorname{span}S$ | span | all finite linear combinations of $S$ | $\operatorname{span}\{(1,0),(0,1)\}=\mathbb{R}^2$ |
| $\sup S$, $\inf S$ | supremum, infimum | least upper bound, greatest lower bound | $\sup(0,1)=1$; $\inf(0,1)=0$ |
| $\max S$, $\min S$ | maximum, minimum | largest or smallest element, when attained | $\max[0,1]=1$; $(0,1)$ has no maximum |
| $\delta_{ij}$ | Kronecker delta | $1$ if $i=j$, else $0$ | $\delta_{12}=0$ |
| $\mathbb{Z}$ | integers | $\{\dots,-2,-1,0,1,2,\dots\}$ | $-3\in\mathbb{Z}$; $\tfrac12\notin\mathbb{Z}$ |
| $X$ | random variable | a measurable function on a sample space | $X\sim\mathcal{N}(0,1)$ |
| $z$ | complex number; standard score | context decides | $z=a+bi$; $z=(x-\mu)/\sigma$ |
| $Z$ | standard normal variable | $Z\sim\mathcal{N}(0,1)$ | $\Pr(Z\le1.96)\approx0.975$ |

## 4. Greek Letters

| Symbol | Name | Meaning | Example |
|---|---|---|---|
| $\alpha$ | alpha | significance level; an angle | reject $H_0$ when $p<\alpha$; $\alpha=30^\circ$ |
| $\beta$ | beta | regression coefficient; Type II error rate | $y=\beta_0+\beta_1x$ |
| $\gamma$ | gamma | an angle; a parametrised curve | $\gamma(t)=(t,t^2)$ |
| $\Gamma$ | Gamma | the Gamma function, $\Gamma(n)=(n-1)!$ for $n\in\mathbb{N}$ | $\Gamma(5)=24$ |
| $\Delta$ | Delta | change; discriminant; Laplacian | $\Delta=b^2-4ac$ |
| $\delta$ | delta | a small positive increment | $\lvert x-a\rvert<\delta$ |
| $\varepsilon$, $\epsilon$ | epsilon | an arbitrarily small positive number | $\forall\varepsilon>0\ \exists\delta>0$ |
| $\zeta$ | zeta | the Riemann zeta function | $\zeta(2)=\pi^2/6$ |
| $\theta$ | theta | an angle; a parameter | $\sin\theta$; $\theta\in\Theta$ |
| $\kappa$ | kappa | curvature; condition number | $\kappa=\dfrac{\lvert f''\rvert}{(1+f'^2)^{3/2}}$ for a plane curve |
| $\lambda$ | lambda | eigenvalue; rate parameter | $Av=\lambda v$; $X\sim\operatorname{Pois}(\lambda)$ |
| $\Lambda$ | Lambda | diagonal matrix of eigenvalues | $A=Q\Lambda Q^{\mathsf{T}}$ |
| $\mu$ | mu | mean; a measure | $\mu=\mathbb{E}[X]$; $\mu(A)$ |
| $\nu$ | nu | degrees of freedom | $t_\nu$ |
| $\pi$ | pi | $3.14159\ldots$; also a projection map | $2\pi r$; $\pi^2=\pi$ |
| $\rho$ | rho | correlation; density | $\rho=\dfrac{\operatorname{Cov}(X,Y)}{\sigma_X\sigma_Y}$ |
| $\sigma$ | sigma | standard deviation; a permutation; a sigma-algebra | $\sigma=\sqrt{\operatorname{Var}X}$; $\sigma\in S_n$ |
| $\tau$ | tau | a topology; a stopping time | $\tau$ is a family of open sets closed under unions |
| $\phi$, $\varphi$ | phi | an angle; Euler's totient; the golden ratio | $\varphi(10)=4$; $\varphi=\dfrac{1+\sqrt5}{2}$ |
| $\Phi$ | Phi | standard normal cumulative distribution | $\Phi(0)=0.5$ |
| $\chi$ | chi | Euler characteristic; chi-squared statistic | $V-E+F=2$; $\chi^2=\sum\dfrac{(O-E)^2}{E}$ |
| $\psi$ | psi | a wave function; a generic function | $\psi(x,t)$ |
| $\Omega$ | Omega | sample space; asymptotic lower bound | $\Omega=\{H,T\}$; $n^2=\Omega(n)$ |
| $\omega$ | omega | angular frequency; a complex cube root of unity | $\omega=2\pi f$; $\omega^3=1$ |

## 5. One Symbol, Several Meanings

Ambiguity is resolved by the type of the object, never by guessing. The table lists every collision a
reader of this repository is likely to meet.

| Symbol | Readings | How to tell |
|---|---|---|
| $\lvert\cdot\rvert$ | absolute value; cardinality; determinant; complex modulus | the argument is a number, a set, a matrix or a complex number |
| $\log$ | base $10$ in elementary chapters; natural log in analysis | this repository writes the base explicitly, or uses $\ln$ for base $e$ |
| $\sin^{-1}x$ | $\arcsin x$ only | a power of a trigonometric function is written $(\sin x)^2$, never $\sin^{-1}x$ |
| $f^{-1}$ | the inverse function | $1/f(x)$ is written $f(x)^{-1}$ |
| $\subset$ | subset; sometimes proper subset | this repository uses $\subseteq$ and $\subsetneq$ to remove the doubt |
| $\pi$ | the constant; a projection map | a number cannot be composed with a vector |
| $\sigma$ | standard deviation; a permutation; a sigma-algebra | the surrounding algebra decides |
| $\Delta$ | a change; the Laplacian; a discriminant | $\Delta x$ is a change, $\Delta f$ is a Laplacian, $\Delta=b^2-4ac$ is a discriminant |
| $\mathbb{E}$ | expectation | an event is written $E$ in upright type or $\mathcal{E}$ |
| $P$ | probability; power set; projection | $\mathcal{P}(A)$ is the power set here |
| $\sim$ | equivalence relation; "is distributed as"; asymptotic equivalence | a relation between sets, between random variables, or between functions |
| $\bar{z}$ | complex conjugate | a bar over a *set* means closure, $\overline{S}$ |
| $A^{\complement}$ | complement in a fixed universe | some texts write $A^{c}$; this repository always uses $\complement$ |
| $d$ | differential; a metric | $df$ acts on increments; $d(x,y)$ is a number |
| $R$ | radius; circumradius; a ring | context; correlation is always $\rho$ here |
| $\Omega$ | sample space; asymptotic lower bound | $\Omega(n)$ takes an argument |
| $\omega$ | angular frequency; a root of unity | context |

## 6. Where Each Group Is Taught

| Area | Symbols introduced there | Discipline |
|---|---|---|
| Logic and proof | $\neg$, $\land$, $\lor$, $\Rightarrow$, $\Leftrightarrow$, $\forall$, $\exists$, $\vdash$, $\models$ | [Foundations](../../00-foundations/README.md) |
| Sets and functions | $\in$, $\subseteq$, $\cup$, $\cap$, $\setminus$, $\varnothing$, $\mathcal{P}$, $f:A\to B$, $f\circ g$ | [Foundations](../../00-foundations/README.md) |
| Number systems and arithmetic | $\mathbb{N}$, $\mathbb{Z}$, $\mathbb{Q}$, $\mathbb{R}$, $\mathbb{C}$, $\lvert x\rvert$, $\sqrt{\ }$, $\%$ | [Arithmetic](../../01-arithmetic/README.md) |
| Elementary algebra | $a^n$, $\log_a$, $\sum$, $\prod$, $\binom{n}{k}$ | [Algebra](../../03-algebra/README.md) |
| Geometry and trigonometry | $\pi$, $^\circ$, $\sin$, $\cos$, $\tan$, $\angle$ | [Geometry](../../04-geometry/README.md), [Trigonometry](../../05-trigonometry/README.md) |
| Calculus and analysis | $\lim$, $f'$, $\dfrac{df}{dx}$, $\int$, $\partial$, $\nabla$, $O$, $o$, $\sim$ | [Calculus](../../07-calculus/README.md) |
| Linear algebra | $A^{\mathsf{T}}$, $A^{-1}$, $\det$, $\operatorname{tr}$, $\operatorname{rank}$, $\lambda$, $\langle\cdot,\cdot\rangle$, $\lVert\cdot\rVert$ | [Linear Algebra](../../08-linear-algebra/README.md) |
| Probability and statistics | $\Pr$, $\mathbb{E}$, $\operatorname{Var}$, $\operatorname{Cov}$, $\rho$, $\Phi$, $\bar{x}$, $s^2$ | [Probability](../../10-probability/README.md), [Statistics](../../11-statistics/README.md) |
| Topology | $\tau$, $\partial A$, $\overline{S}$, $B_r(x)$, $\cong$ | [Topology](../../17-topology/README.md) |

---

*Part of the [Reference Library](../README.md). Notation follows
[MATHEMATICAL_NOTATION.md](../../MATHEMATICAL_NOTATION.md); terms are defined in
[GLOSSARY.md](../../GLOSSARY.md); the curriculum itself begins at [README.md](../../README.md).*
