
# Optimal Prefix Codes : Huffman Encoding

**Observation 1**. _**Lowest frequency items**_ should be at the _**lowest level**_ in tree of optimal prefix code.
**Observation 2**. For $n > 1$, the lowest level always contains _**at least two leaves**_ (optimal trees are full!).
**Observation 3**. **The order** in which items appear in a level <u>does not</u> matter.

>[!definition]- Claim 1
>There is an optimal prefix code with tree $T^\star$ where the two lowest-frequency letters are assigned to leaves that are brothers in $T^\star$.

## Huffman Codes

