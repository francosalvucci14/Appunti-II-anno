
# Optimal Prefix Codes : Huffman Encoding

**Observation 1**. _**Lowest frequency items**_ should be at the _**lowest level**_ in tree of optimal prefix code.
**Observation 2**. For $n > 1$, the lowest level always contains _**at least two leaves**_ (optimal trees are full!).
**Observation 3**. **The order** in which items appear in a level <u>does not</u> matter.

>[!definition]- Claim 1
>There is an optimal prefix code with tree $T^\star$ where the two lowest-frequency letters are assigned to leaves that are brothers in $T^\star$.

## Huffman Codes

Greedy Template. `[Huffman, 1952]`

Create the tree **bottom-up**.

1) **_Make two leaves_** for two lowest-frequency letters **y** and **z**.
2) **Recursively** build tree for the rest: replacing y and z with a _meta-letter_ for yz. with frequency $f_{yz} = f_y + f_z$
3) **Consider** the new alphabet $S' = S - \{y,z\} + \{yz\}$

![[appunti asd/mod ii/immagini/Pasted image 20230412093916.png|center|500]]

Q. What is the time complexity?
A. $T(n) = T(n-1) + O(n)\to O(n^2)$

Q. How to implement finding _**lowest-frequency letters**_ efficiently?
A. Use priority queue for S: $T(n) = T(n-1) + O(\log{n})\to O(n logn)$

### Greedy Analysis

**Claim.** $ABL(T') = ABL(T) - f_{\omega}$

**Proof** 
![[appunti asd/mod ii/immagini/Pasted image 20230412100205.png|center|500]]

**Claim**. Huffman code for S achieves the minimum ABL of any prefix code.
**Pf**. (by induction)

_Base_: For $n=2$ there is no shorter code than root and two leaves.
_Ind. Hypothesis_: Huffman tree T’ for S’ with $\omega$ instead of y and z is **optimal** (S' ha dimensione n-1):
$$ABL( T' ) \leq ABL( Z' )$$for any feasible Z’ for S’

Step: (by contradiction)
- Suppose Huffman tree T for S is **not** optimal.
- So there is some tree $Z_1$ such that $ABL(Z_1) \lt ABL(T)$
- Then there is also a tree Z for which leaves y and z exist that are **brothers** and have the **lowest level** and $ABL(Z_1) \lt ABL(T)$ **(see Claim 1).**
- Let Z ' **obtained** from Z with and **z and y deleted**, and their **former parent** labeled $\omega$.
- Similar T’ is derived from S’ in our algorithm.
- We know that $ABL(Z')=ABL(Z)-f_{\omega}$, as well as $ABL(T')=ABL(T)-f_{\omega}$.
- But also $ABL(Z) \lt ABL(T) \to ABL(Z') \lt ABL(T')$.
