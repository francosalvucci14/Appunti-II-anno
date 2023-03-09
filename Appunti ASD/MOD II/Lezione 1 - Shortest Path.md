
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

**Proof** : Easy consequence of the _**Principle of Sub-Optimal**_ of Shortest Paths in a graph with positive weights : 

>[!quote] Any sub-path of a shortest pats is a shortest path

![[appunti asd/mod ii/immagini/Pasted image 20230308101859.png|center|600]]


## Dijkstra's Algorithm

Dijkstra's Algorithm : 

- Maintain a set of _**explored nodes**_ S for which we have determined the shortest path distance $d(u)$ form "s" to "u"
- Initialize $S=\{s\},d(s)=0$
- Repeatedly choose unexplored node v which minimizes $$\pi(v)=min_{e=(u,v)t.c\ u\in S}\{d(u)+l_e\}(\star)$$ add v to S, set $d(v)=\pi(v)$ , and store the father of **v** (i.e u)

>$\star$ = shortest path to some "u" in explored part, followed by a signle edge (u,v)

![[appunti asd/mod ii/immagini/Pasted image 20230308103125.png|center|500]]


Dijkstra's Algorithm (Overall Scheme) : 

- Maintain a set of _**explored nodes**_ S for which we have determined the shortest path distance $d(u)$ form "s" to "u"
- Initialize $S=\{s\},d(s)=0$
- Repeatedly choose unexplored node v which minimizes $$\pi(v)=min_{e=(u,v)t.c\ u\in S}\{d(u)+l_e\}(\star\star)$$ add v to S, set $d(v)=\pi(v)$ , and store the father of **v** (i.e u)

>$\star\star$ = shortest path to some "u" in explored part, followed by a signle edge (u,v)
>**How to do it?**

![[appunti asd/mod ii/immagini/Pasted image 20230308103722.png|center|500]]


