
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

