
# Minimum Spanning Tree

>[!important]- Definition
>Given a connected graph $G=(V,E)$ with real-valued edge weights $c_e$, an MST is a subset of the edges $T\subseteq E$ such that $T$ is a spanning tree whose sum of edge weights is minimized

![[appunti asd/mod ii/immagini/Pasted image 20230309163355.png|center|600]]

**Cayley's Theorem**:  There are $n^{n-2}$ spanning trees of $K_n$ (can't solve by brute force)

## The MST Problem : Formal Definition

**Input** : 
- Symmetric, connected weighted graph $G=(V,E,w)$, where:
	- $V$ = Set of nodes
	- $E$ = Set of edges
	- Edge cost function $c:E\to\mathbb R^+$
**Feasible Solution**:
- Any Spanning Tree of G : 
	- $F,F\subseteq E$
**Cost of feasible solution** :
- Cost (to minimize) $$c(T)=\sum_{e\in T}c(e)$$

## General Approach : Greedy Algorithms

- **Kruskal's algorithm** : Start with $T=\emptyset$. Consider edges in **ascending order** of cost. Insert edge e in T unless doing so would create a **cycle**
- Reverse-Delete algorithm : Start with $T=E$. Consider edges in **descendig order** of cost. Delete edge e from T unless doing so would **disconnect T**
- Prim's algorithm : Start with any root node s and greedily grow a tree T from s outward (visiting G). At each steps, add the **cheapest edge** e to T that has exactly one endpoint in T

>[!important]- Main Theorem
>All three algorithms produce an MST

### Greedy Algorithms : Analysis

PROOF of the MAIN THEOREM

We will use TOW GENERAL PROPRERTIES OF GRAPHS : 

![[appunti asd/mod ii/immagini/Pasted image 20230309163922.png|center|600]]

**Simplifying assumption** : All edge costs $c(e)$ are distinct

**Cut property** : Let S be any subset of nodes, and let "e" be the min cost edge with exactly one endpoint in S, Then the MST contains "e"

**Cycle property** : Let C be any cicle, and let "f" be the max cost edge belonging to C. Then the MST does not contain "f"