
# Minimum Spanning Tree

>[!important]- Definition
>Given a connected graph $G=(V,E)$ with real-valued edge weights $c_e$, an MST is a subset of the edges $T\subseteq E$ such that $T$ is a spanning tree whose sum of edge weights is minimized

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



