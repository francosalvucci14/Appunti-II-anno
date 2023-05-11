
# co-NP and the Asymmetry of NP

## Np and co-NP

>[!definition]- DEF 1. (NP) 
>Decision problems for which there is a poly-time certifier: $X \in NP \iff \exists$ poly-time certifier C(s, t) s.t. for every string $s\in\Sigma^\star$,$s \in X$ (i.e. s is a yes Instance ) $\iff \exists$ a string t such that C(s, t) = yes. t = certificate or witness

Ex. SAT, HAM-CYCLE, COMPOSITES.

>[!definition]- Def. 
>Given a decision problem X, its _**complement**_ X is the same problem with the yes and no answers reverse.

Ex.
$X = \{ 0, 1, 4, 6, 8, 9, 10, 12, 14, 15, \dots \}$ = { yes Instances of COMPOSITES}
$co-X = \{ 2, 3, 5, 7, 11, 13, 17, 23, 29, \dots \}$
$co-NP$ = { **All Complements** of decision problems in NP}

Ex. Co-SAT (TAUTOLOGY), NO-HAM-CYCLE, PRIMES $\in co-NP$

### Asymmetry of NP

<u>Asymmetry of NP:</u>
- We only need to have **at least one** short proof (Certificate) of yes **instances**.
- While, for no **instances**, we require **no** (short) proof must exist.

**Ex 1**. SAT vs. Co-SAT (TAUTOLOGY).
- SAT: Can prove a **CNF formula** is satisfiable by giving good assignment (certificate).
- Co-SAT: How could we prove that a **CNF formula** is _not_ satisfiable via a short certificate?

**Ex 2**. HAM-CYCLE vs. Co-HAM-CYCLE.
- Can prove a graph is **Hamiltonian** by giving such a Hamiltonian cycle.
- How could we prove that a graph is **_not_ Hamiltonian** via a short certificate?

>[!warning]- Remark.
>SAT is NP-complete and $SAT\equiv_p Co-SAT$


But,how do we classify Co-SAT ? Is it in NP? can be in P?

> We don’t even know whether it is in NP !

### NP = co-NP?

**Fundamental question**. Does NP = co-NP?
- Do yes instances have succinct certificates iff no instances do?
- Consensus opinion: no!

>[!definition]- Theorem. 
>If $NP\neq co-NP$, then $P \neq NP.$

**Proof** (By Contradiction).
- P is closed under complementation (i.e. $P=Co-P$)
- If $P = NP$, then NP is also closed under complementation.
- In other words, $NP = co-NP.$
- Contradiction!

### Good characterizations

**Good characterization**. $[\text{Edmonds 1965}]$
What is $NP \cap co-NP$?
If problem X is in both NP and co-NP, then:
- for yes **instance**, there is a short certificate $t^{YES}$
- for no **instance**, there is a short disqualifier $t^{NO}$

Ex. Given a **bipartite graph G(V,E)**, is there a Perfect Matching.
- If yes, can exhibit a perfect matching.
- If no, can exhibit a set of nodes S such that $|N(S)| \lt |S|$.

**Decision Problem PM**: Given a bipartite graph $G(V_1,V_2; E)$, is there a _**Perfect Matching M**_?
- If yes, can exhibit a Perfect Matching $M \subseteq E$
- If no, can exhibit a set of nodes S such that $|N(S)| \lt |S|$.

![[appunti asd/mod ii/immagini/Pasted image 20230511150521.png|center|550]]


Observation. $P \subseteq NP \cap co-NP$.

Fundamental open question. Does $P = NP \cap co-NP$?
- Mixed opinions.
- Many examples where problem found to have a non-trivial good characterization, but only years later discovered to be in P.
	- linear programming $[\text{Khachiyan, 1979}]$
	- primality testing $[\text{Agrawal-Kayal-Saxena, 2002}]$

>[!definition]- THM. 
>Factoring is in $NP \cap co-NP$, but **not known** to be in P.

#### PRIMES is in $NP \cap co-NP$

PRIMES = Given an odd integer $s \gt 0$, s is PRIME ?

>[!definition]- THM A. 
>PRIMES is in $NP\cap co-NP.$

Proof.
We already know that PRIMES is in co-NP, so it suffices to prove that PRIMES is in NP.

>[!definition]- Pratt's Theorem.
>An odd integer s is **prime** $\iff$ _**there exists**_ an integer t s.t. $1 \lt t \lt s$ s.t. $$\begin{align}&t^{s-1}\equiv 1 (\text{mod s})(a)\\&t^{(s-1)/p}\neq 1(\text{mod s})(b)\end{align}$$ for all prime divisors p of s-1

![[appunti asd/mod ii/immagini/Pasted image 20230511154324.png|center|550]]

#### FACTOR is in $NP \cap co-NP$

**FACTORIZE (Search Problem).** Given an integer x, find its prime factorization.

**FACTOR (Decision Problem)**. Given two integers x and y, does x have a **nontrivial factor** less than y?

>[!definition]- Theorem. 
>$FACTOR\equiv_p FACTORIZE$

Proof: Omitted (Binary Search and More Number Theory)

>[!definition]- Theorem. 
>FACTOR is in $NP\cap co-NP.$

Proof.
- Certificate: a **factor p** of x that is less than y.
- Disqualifier: The prime factorization of x (where each prime factor is larger than y), along with a certificate that **each factor is prime** (apply Pratt’s Theorem and THM A in the previous slide).



