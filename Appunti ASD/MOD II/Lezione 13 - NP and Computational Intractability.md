# Definition of NP

## Decision Problem

>[!definition]- Def. (Decision problem.)
>$\Sigma$ = Finite Alphabet ; $\Sigma^\star \equiv\{\text{all possible finite strings x of alphabet}\space \Sigma\}$
>**A Decision Problem** : $X = X \subseteq\Sigma^\star$
>Instance: any fixed string $s\in\Sigma^\star$
>Question: Does $s \in X ?$ (Note: $X \equiv \{\text{all YES Instances} \}$)

>[!definition]- Def. (Algorithm A)
>Solves/decides problem X **if**, for any instance $s\in\Sigma^\star$, $$A(s) = yes\iff s\in X$$

**Polynomial time**.
Algorithm A runs in **poly-time** if for every string s, $A(s)$ terminates in at most $p(|s|)$ "steps", where $p(\cdot)$ is some polynomial, where $$|s| \equiv\text{length of s}$$
**Ex**
PRIMES: $X = \{ 2, 3, 5, 7, 11, 13, 17, 23, 29, 31, 37, \dots\}$
Algorithm. `[Agrawal-Kayal-Saxena, 2002]`  $p(|s|) = |s|^8.$

## Definition of P

$P \equiv$ {X for which there is a **deterministic poly-time** algorithm}

![[appunti asd/mod ii/immagini/Pasted image 20230426100807.png|center|650]]


## The class NP

_**Certification algorithm**_: **Intuition.**
- _Certifier_ views things from "managerial" viewpoint.
- _Certifier_ doesn't determine whether $s \in X$ on its own; rather, it checks a proposed **proof** t that $s \in X$.

>[!definition]- Algorithm C(s, t)
>Is a _certifier_ for problem X if, for every string $s\in\Sigma^\star$, $s \in X$ **iff there exists a string t such that C(s, t) = yes**; t = "certificate" or "witness"

>[!definition]- Def. (NP) 
>NP $\equiv$ { X for which there exists a **poly-time _certifier_** }

>[!info]- Osservation
>C(s, t) is a poly-time algorithm and $|t| \leq p(|s|)$ for some polynomial $p(\cdot)$.

>[!warning]- Remark
>NP stands for **nondeterministic polynomial-time.**

### Certifiers and Certificates: Composite

**COMPOSITES**. Given an integer s, is s composite?

**Certificate**. Any nontrivial factor t of s. Note that such a certificate exists iff s is composite. Moreover $|t| \leq |s|$.

![[appunti asd/mod ii/immagini/Pasted image 20230505122653.png|center|500]]

EX. Instance. s = 437669.
Certificate. t = 541 or 809.

### Certifiers and Certificates: 3-Satisfability


**3-SAT.**
- _Instance_: CNF formula $\phi$ _**in the Boolean variable**_ $x_1 , x_2, \dots, x_n$,
- _Question_: is there a **satisfying** assignment $t \in \{0,1\}^n$ for $\phi(x_1 , x_2, \dots, x_n)$
- _Certificate_. An assignment $t \in \{0,1\}^n$

**Certifier**. Check that each clause in $\phi(x_1 , x_2, \dots, x_n)$ has at least one true literal.

![[appunti asd/mod ii/immagini/Pasted image 20230505123145.png|center|550]]

**THM**.
3-SAT is in NP.

### Certifiers and Certificates: Hamiltonian Cycle

**HAM-CYCLE**.
- _Instance_. an undirected graph $G = (V, E)$ where $V = \{1,2,\dots,n\}$
- _Question_. does there exist a <u>simple</u> cycle C that visits <u>every</u> node of V?
- _Certificate_: a **permutation** $\Pi$ of $V= \{1,2,\dots,n\}.$

**Certifier** $C(G(V,E), \Pi)$. Check that:
1. $\Pi$ is a permutation of V, i.e., it contains each $v \in V$ exactly once , and
2. there is edge $(v,w) \in E$ between each pair of adjacent nodes $<u,w> \in \Pi$ 

**Thm**. HAM-CYCLE is in NP.

![[appunti asd/mod ii/immagini/Pasted image 20230505123758.png|center|500]]

## P,EXP,NP

- **P**. Decision problems for which there is a _**poly-time algorithm**_.
- **EXP**. Decision problems for which there is an _**exponential-time algorithm**_.
- **NP**. Decision problems for which there is a _**poly-time certifier**_.

>[!definition]- Claim. $P \in NP$.

Pf. Consider any problem X in P.
- By hyp., there exists a poly-time algorithm A(s) that solves X.
- Certificate: $t = \varepsilon$, certifier C(s, t) = A(s).

>[!definition]- Claim. $NP \in EXP.$

Pf. Consider any problem X in NP.
- By definition, there exists a poly-time certifier C(s, t) for X.
- To solve input s, run C(s, t) on all proofs, i.e., strings t with $|t| \in p(|s|)$.
- How many strings t to check? if proof’s alphabet is binary, then number of t’s $= 2^{p(|s|)}$ which is ok since we are in EXP
- Return yes, if C(s, t) returns yes forany of these t’s .

