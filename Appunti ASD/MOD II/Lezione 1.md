
# Shortest Path in a Graph

![[appunti asd/mod ii/immagini/Pasted image 20230308092458.png|center|500]]

## Shortest Path Problem

**Input** : Weighted connected graph $\langle G=(V,E),l:E\to \mathbb R^+\rangle$; **Source** s in V 
(Lenght $l_e$ = lenght of edge e)
**Feasible Solution** : Any set ($T\subseteq E$) of _simple_ paths from "s" to "t", $\forall t\in V : t\neq s$ 
**Goal** : for any t in V, **_minimize_ the cost** of the **s-t path**

> cost of path = sum of edge costs in path

![[appunti asd/mod ii/immagini/Pasted image 20230308092938.png|center]]

### Shortest Path Trees

>[!important]- Theorem (SPT)
>For any inputs $[\langle G=(V,E),l:E\to\mathbb R^+,s\in V\rangle]$, there always exists an **optimal** solution that forms a Spanning Tree for G

**Proof** : Esay consequence of the _**Principle of Sub-Optimal**_ of Shortest Paths in a graph with positive weights : 

>"Any sub-path of a shortest pats is a shortest path"

