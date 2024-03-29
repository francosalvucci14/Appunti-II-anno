
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

>[!quote] Any sub-path of a shortest path is a shortest path

![[appunti asd/mod ii/immagini/Pasted image 20230308101859.png|center|600]]


## Dijkstra's Algorithm

Dijkstra's Algorithm : 

- Maintain a set of _**explored nodes**_ S for which we have determined the shortest path distance $d(u)$ form "s" to "u"
- Initialize $S=\{s\},d(s)=0$
- Repeatedly choose unexplored node v which minimizes $$\pi(v)=min_{e=(u,v)t.c\ u\in S}\{d(u)+l_e\}(\star)$$ add v to S, set $d(v)=\pi(v)$ , and store the father of **v** (i.e u)

>$\star$ = shortest path to some "u" in explored part, followed by a single edge (u,v)

![[appunti asd/mod ii/immagini/Pasted image 20230308103125.png|center|500]]


Dijkstra's Algorithm (Overall Scheme) : 

- Maintain a set of _**explored nodes**_ S for which we have determined the shortest path distance $d(u)$ form "s" to "u"
- Initialize $S=\{s\},d(s)=0$
- Repeatedly choose unexplored node v which minimizes $$\pi(v)=min_{e=(u,v)t.c\ u\in S}\{d(u)+l_e\}(\star\star)$$ add v to S, set $d(v)=\pi(v)$ , and store the father of **v** (i.e u)

>$\star\star$ = shortest path to some "u" in explored part, followed by a signle edge (u,v)
>**How to do it?**

![[appunti asd/mod ii/immagini/Pasted image 20230308103722.png|center|500]]


### Proof of Correctness

>[!important]- THM 1.
>For each node $u\in S,d(u)$ is the **lenght** of the **shortest** s-u path

**Dim** (by induction on $|S|$)

- Base case : $|S|=1$
- Inductive hypothesis: Assume true for $|S|=k\geq1$
	- Let v be next node added to S, and let u-v be the chosen edge
	- The shortest s-u path plus (u,v) is an s-v path of lenght $\pi(v)$
	- Consider any s-v path P. We'll see that it's no shorter than $\pi(v)$
	- Let x-y be the **first edge** in $P$ that leaves S, and let $P'$ be the subpath to x
	- $P$ is already too long as soon as it leaves S
	- $$l(P)\geq l(P')+l(x,y)\geq d(x)+l(x,y)\geq\pi(y)\geq\pi(v)$$

