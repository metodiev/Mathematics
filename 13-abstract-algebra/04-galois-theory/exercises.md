# Galois Theory — Exercises

> [Galois Theory](README.md) · 38 problems · Beginner → Challenge · Solutions: [solutions.md](solutions.md)

Attempt every problem in writing before looking at [solutions.md](solutions.md). Each problem names the section of the tutorial that supplies the technique, and *(proof)* marks a problem that requires a complete argument with every hypothesis stated. Section numbers refer to [README.md](README.md).

Notation: $F$ is a field and $E/F$ a field extension; $[E:F]$ is the degree; $m_\alpha$ is the minimal polynomial of $\alpha$ over the base field in question; $F(\alpha_1,\dots,\alpha_n)$ is the smallest subfield containing $F$ and the $\alpha_i$; $\zeta_n = e^{2\pi i/n}$; $\omega = \zeta_3$; $\Delta(f)$ is the discriminant; $\operatorname{Gal}(E/F)$ and $\operatorname{Gal}(f/F)$ are Galois groups; $S_n$, $A_n$, $C_n$, $V_4$, $D_4$ are as in [README §6](README.md#6-mathematical-notation); $(k\,l)$ denotes a transposition and $(1\,2\,\cdots\,n)$ an $n$-cycle.

## Beginner

**1.** *(§5.1, §7.1)* Compute each degree, justifying every step with the tower law and an irreducibility argument.
(a) $[\mathbb{Q}(\sqrt3,\sqrt5):\mathbb{Q}]$; (b) $[\mathbb{Q}(\sqrt[3]{3}):\mathbb{Q}]$; (c) $[\mathbb{Q}(\sqrt[4]{2}):\mathbb{Q}]$; (d) $[\mathbb{Q}(\zeta_6):\mathbb{Q}]$; (e) $[\mathbb{Q}(\sqrt2,i):\mathbb{Q}]$.

**2.** *(§5.2)* Find the minimal polynomial over $\mathbb{Q}$ of (a) $\sqrt5$; (b) $\sqrt[3]{3}+1$; (c) $\sqrt2+i$; (d) $\zeta_5+\zeta_5^{-1}$. In each case prove minimality.

**3.** *(§5.4)* Determine the splitting field and its degree over the stated field: (a) $x^4-1$ over $\mathbb{Q}$; (b) $x^3-1$ over $\mathbb{Q}$; (c) $x^2+1$ over $\mathbb{R}$; (d) $x^2+x+1$ over $\mathbb{F}_2$.

**4.** *(§5.7)* *(proof)* Show that $\mathbb{Q}(\sqrt5)/\mathbb{Q}$ is Galois by writing down all its automorphisms and computing the fixed field. Show that $\mathbb{Q}(\sqrt[3]{3})/\mathbb{Q}$ is not Galois, and that $\operatorname{Aut}(\mathbb{Q}(\sqrt[3]{3})/\mathbb{Q})$ is trivial.

**5.** *(§5.7, §7.9)* Let $E = \mathbb{Q}(\sqrt3,\sqrt5)$. List the four elements of $\operatorname{Gal}(E/\mathbb{Q})$, show that the group is $V_4$, and list all five subgroups together with their fixed fields.

**6.** *(§5.5)* Decide, with justification from $\gcd(f,f')$, whether each polynomial is separable over the stated field: (a) $x^2+1$ over $\mathbb{Q}$; (b) $x^2+1$ over $\mathbb{F}_2$; (c) $x^3-x$ over $\mathbb{F}_3$; (d) $x^2+x+1$ over $\mathbb{F}_2$; (e) $x^p-t$ over $\mathbb{F}_p(t)$; (f) $x^4+1$ over $\mathbb{Q}$.

**7.** *(§5.5, §7.12)* Factor $x^4+1$ into irreducibles over $\mathbb{Q}$, over $\mathbb{F}_2$ and over $\mathbb{F}_3$, and state which of the three factorisations shows inseparability.

**8.** *(§7.10)* Compute the discriminant of (a) $x^2-7$; (b) $x^2+x+1$; (c) $x^3-3x+1$; (d) $x^3-1$; (e) $x^3-7x+7$; (f) $x^4-2$. Which of these discriminants are squares in $\mathbb{Q}$, and what does Theorem 7.10.3 then say about the Galois group?

**9.** *(§7.8)* Determine the splitting field and the Galois group over $\mathbb{Q}$ of (a) $x^2-3$; (b) $x^2+3$; (c) $x^2-4x+1$; (d) $x^2-4x+4$.

**10.** *(§7.10)* *(proof)* Prove that $x^3-7x+7$ is irreducible over $\mathbb{Q}$, compute $\Delta = 49$, and deduce that its Galois group is $A_3$ and that its splitting field has degree $3$.

**11.** *(§7.13)* Compute $\varphi(n)$ for $n = 7, 9, 12, 15, 16, 17, 20, 24, 25, 30$, and decide for each whether the regular $n$-gon is constructible. Name the criterion you use at each step.

**12.** *(§5.6)* Decide whether each extension is normal over $\mathbb{Q}$, with proof or counterexample: $\mathbb{Q}(\zeta_5)$, $\mathbb{Q}(\sqrt[3]{2})$, $\mathbb{Q}(\sqrt2,\sqrt[3]{2})$, $\mathbb{Q}(\sqrt[4]{2})$, $\mathbb{Q}(\sqrt2,\sqrt3)$, $\mathbb{Q}(\omega,\sqrt[3]{2})$.

## Intermediate

**13.** *(§7.7)* *(proof)* Prove that if $[E:F] = 2$ and $\operatorname{char} F \ne 2$ then $E/F$ is Galois with group $C_2$. Then show that in characteristic $2$ the extension $\mathbb{F}_2(t^{1/2})/\mathbb{F}_2(t)$ has degree $2$ but is not Galois, and say exactly which of "normal" and "separable" fails.

**14.** *(§7.1)* *(proof)* Prove the tower law for finite extensions, including the spanning and independence steps. Deduce that if $[E:F] = p$ is prime there are no intermediate fields, and that if $[E:F] = 4$ and $E \ne F$ then either $E = F(\alpha)$ for some $\alpha$ with $m_\alpha$ of degree $4$, or $E$ contains an intermediate field of degree $2$ over $F$.

**15.** *(§7.6)* *(proof)* Let $E$ be a field and $H$ a subgroup of $\operatorname{Aut}(E)$. Prove that $E^H$ is a subfield of $E$. Then, assuming $H$ finite and $F = E^H$, prove that $E/F$ is Galois with $\operatorname{Gal}(E/F) = H$.

**16.** *(§7.8)* Let $f = x^4-4x^2+2 \in \mathbb{Q}[x]$. Show that $f$ is irreducible, that its splitting field is $E = \mathbb{Q}(\alpha)$ where $\alpha^2 = 2+\sqrt2$, and that $\operatorname{Gal}(f/\mathbb{Q}) \cong C_4$ by exhibiting an automorphism of order $4$.

**17.** *(§7.9)* *(proof)* Let $E/F$ be finite Galois with group $G$, and let $K$ be an intermediate field. Prove that every $F$-automorphism of $K$ extends to an element of $G$, and deduce that restriction gives a surjection $G \to \operatorname{Gal}(K/F)$ when $K/F$ is normal.

**18.** *(§7.9)* For $E = \mathbb{Q}(\zeta_9)$ list all subgroups of $G = \operatorname{Gal}(E/\mathbb{Q})$ by exhibiting $G$ as an explicit cyclic group, and for each subgroup give the fixed field and its degree over $\mathbb{Q}$. Identify the unique quadratic subfield.

**19.** *(§7.11)* For $f = x^4+4x^2+2$ compute the cubic resolvent, determine which case of Theorem 7.11.4 applies, and compute the Galois group and the degree of the splitting field.

**20.** *(§7.13)* *(proof)* Prove that $\cos 20^\circ$ has minimal polynomial $8x^3-6x-1$ over $\mathbb{Q}$, and deduce that a $60^\circ$ angle cannot be trisected with ruler and compass. State the theorem you use.

**21.** *(§7.12)* *(proof)* Prove that $\mathbb{Q}(\zeta_5)/\mathbb{Q}$ is Galois with group $C_4$, that it has exactly one proper nontrivial intermediate field, and that this field is $\mathbb{Q}(\sqrt5)$.

**22.** *(§7.15)* Compute the derived series of $S_4$ and of $A_4$; deduce that $S_4$ is solvable and that $A_4$ is solvable but not abelian. Explain why this does not contradict the non-solvability of $A_5$.

**23.** *(§7.9)* Using the subgroup table of Example 9.6 for $E = \mathbb{Q}(\sqrt[4]{2}, i)$, decide which of the ten intermediate fields are Galois over $\mathbb{Q}$, and prove each claim from the fundamental theorem.

## Advanced

**24.** *(§7.4)* *(proof)* Prove Theorem 7.4.3: for finite extensions $F \subseteq K \subseteq E$, $[E:F]_s = [E:K]_s[K:F]_s \le [E:F]$, with equality if and only if $E/F$ is separable.

**25.** *(§7.9)* *(proof)* Let $E/F$ be Galois with group $G$ and let $H \trianglelefteq G$. Prove that $E^H/F$ is Galois and that $\operatorname{Gal}(E^H/F) \cong G/H$, including a proof that every automorphism of $E^H$ over $F$ extends to one of $E$.

**26.** *(§7.9)* *(proof)* Let $E/F$ be finite Galois with group $G$, and $H \le G$. Prove that $\operatorname{Gal}(E/E^H) = H$ and that $[E:E^H] = |H|$, naming every theorem used.

**27.** *(§7.15)* *(proof)* Prove that the only normal subgroups of $S_5$ are $\{e\}$, $A_5$ and $S_5$, and deduce that $S_5$ is not solvable.

**28.** *(§7.8)* *(proof)* Prove that if $f \in \mathbb{Q}[x]$ is irreducible of prime degree $p$ and has exactly two non-real roots, then $\operatorname{Gal}(f) \cong S_p$. Apply the result to $x^3+x+1$.

**29.** *(§7.9)* *(proof)* Prove the lattice identity $E^{H_1\cap H_2} = E^{H_1}E^{H_2}$ for subgroups $H_1,H_2$ of a finite Galois group $G$, including the assertion that $E^{H_1}E^{H_2}$ is a field of degree $[G : H_1\cap H_2]$ over $F$.

**30.** *(§7.12)* *(proof)* For $n = 8$ exhibit $\operatorname{Gal}(\mathbb{Q}(\zeta_8)/\mathbb{Q}) \cong V_4$, list all five subgroups and their fixed fields, and verify the degree of each fixed field.

**31.** *(§7.14)* *(proof)* Prove that if $E/F$ is a Galois radical extension in characteristic $0$ with a tower of cyclic steps, then $\operatorname{Gal}(E/F)$ is solvable; then explain how this yields Theorem 7.14.6 for a general radical extension.

**32.** *(§7.14)* *(proof)* Prove that a finite group $G$ is solvable if and only if it has a chain $G = G_0 \trianglerighteq G_1 \trianglerighteq \cdots \trianglerighteq G_m = \{e\}$ whose successive quotients are cyclic of prime order.

**33.** *(§7.14)* *(proof)* Prove that every finite $p$-group is solvable, and compute the derived series of the group $C_p \rtimes C_{p-1}$ of affine maps $x \mapsto ax+b$ over $\mathbb{F}_p$. Deduce that $x^p-2$ is solvable by radicals over $\mathbb{Q}$.

## Challenge

**34.** *(§7.8, §7.15)* *(proof)* Prove that $x^5-x-1$ is irreducible over $\mathbb{Q}$ and that its Galois group is $S_5$. (Hint: reduce modulo $2$, and rule out a quadratic factor over $\mathbb{Z}$ by evaluating at $0,1,-1$.)

**35.** *(§7.8, §7.12)* *(proof)* For a prime $p$, prove that $\operatorname{Gal}(x^p-2/\mathbb{Q}) \cong C_p \rtimes (\mathbb{Z}/p)^\times$, and determine exactly when this group is contained in $A_p$. Check your answer for $p = 3, 5$.

**36.** *(§7.14)* *(proof)* Prove Theorem 7.14.8 in full: if $\operatorname{char} F = 0$, $F$ contains a primitive $p$-th root of unity for every prime $p$ dividing $|\operatorname{Gal}(f/F)|$, and $\operatorname{Gal}(f/F)$ is solvable, then $f$ is solvable by radicals. Include a complete proof of Kummer's lemma.

**37.** *(§7.15)* *(proof)* Prove that the fixed field of $S_n$ acting on $\mathbb{Q}(x_1,\dots,x_n)$ by permuting the variables is $\mathbb{Q}(e_1,\dots,e_n)$, the field of symmetric rational functions, and deduce that the general quintic has Galois group $S_5$.

**38.** *(§7.12)* *(proof)* For $n \ge 3$ let $E = \mathbb{Q}(\zeta_n)$ and $E^+ = \mathbb{Q}(\zeta_n+\zeta_n^{-1})$. Prove that $E^+$ is the fixed field of complex conjugation, that $[E:E^+] = 2$ and $[E^+:\mathbb{Q}] = \varphi(n)/2$, and that $E^+/\mathbb{Q}$ is Galois with group $(\mathbb{Z}/n)^\times/\{\pm1\}$. Compute $E^+$ explicitly for $n = 7, 8, 9$.