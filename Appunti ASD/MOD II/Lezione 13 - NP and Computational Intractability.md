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



