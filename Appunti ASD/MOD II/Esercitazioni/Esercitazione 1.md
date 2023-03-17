# In Depth of Minimum Spanning Tree

## MST : Recap

Given a graph $G=(V,E)$ and non-negative weights $c:E\to\mathbb R^+$, a **minimum spanning tree (MST) T** of G iss a subset of edges $T\subseteq E$, s.t.
1. The graph $(V,T)$ is connected and acyclic
2. The cost of $$cost(T)=\sum_{e\in T}c(e)$$ is **minimized**

## Computing a spanning tree

1. Prim's Algorithm
2. Kruskal's Algorithm
3. Reverse-Delete Algorithm

All of them use **cut-property/cycle-property**

### Cut-property

Assume all edge costs are distinct. Consider a <u>non-empty</u> cut $S\cup(V\setminus S)$ of G

The minimum cost edge e crossing the cut is in **every** MST of G

![[Pasted image 20230317162757.png|center|200]]

### Cycle-property

Assume all edge costs are distinct. Let C be any cycle in G

The maximum cost edge e in C does not belogn to **any** MST of G

![[Pasted image 20230317162916.png|center|200]]

See animation on [VisualGo](https://visualgo.net/en6)

## SPT vs MST

**Question** : are MST and SPT the same thing? **...NO**

![[Pasted image 20230317163034.png|center|500]]

What about all different edge costs?

![[Pasted image 20230317163104.png|center|500]]

### Problem 1

**Input** :
- $G=(V,E)$
- $c:E\to\mathbb R^+$
- $e\in E$
**Output** : 
- _True_ if exists a MST T of G such that $e\in T$
- _False_ otherwise (if no MST of G contains $e$)
**Constraints** : $O(m+n)$ running time

#### Solution

1. **Remove** all edges $e'$ from $E$ s.t. $c(e')\gt c(e)$, and remove also $e$. Set $G'=(V,E')$ this new graph ![[Pasted image 20230317163510.png|center|500]]
2. Let u,v the two endpoints of $e$. **Start** from u a **BFS** (or **DFS**) search. ![[Pasted image 20230317163615.png|center|500]] Observed that $T_u$ is the connected component of $G'$ containing u
3. Check if u and v in the same connected component of $G'$
	1. If $v\in T_u\implies e$ is NOT in a MST of $G'$ (return **False**)
	2. IF $v\not\in T_u\implies e$ is in a MST of $G'$ (return **True**)

#### Complexity

1. **Build** $G'\to O(m)$
2. **Compute** $T_u\to\Theta(n+m)$
3. **Check the condition** $\to O(1)\implies$ running time $O(n+m)$

#### Analysis

##### Analysis : case 1

What means that $v\in T_u?$

**Obs 1** : Every edge in $T_u$ has cost $\leq c(e)$
**Obs 2** : Since $e\in T_u$ exists a path $P$ in $G'$ from u to v
**Obs 1+ Obs 2** $\implies$ exists a **cycle** $P+e$ in $G$ for which $e$ has the maximum cost.

**cycle-property** $\implies e$ does not belong to any MST of G!

![[Pasted image 20230317164323.png|center|300]]


##### Analysis : case 2

What means that $v\not\in T_u?$

**Obs 1** : u and v are disconnected in $G'$, so in a MST for $G$ there MUST be an edge crossing $T_u$
**Obs 2** : Every edge crossing $T_u$ has cost $\geq c(e)$
**Obs 3** : $e$ crosses $T_u$
**Obs1+Obs2+Obs3** $\implies e$ is the minimum cost edge crossing $T_u$

**cut-property** $\implies e$ belongs to a MST of G!

![[Pasted image 20230317164607.png|center|300]]

## Removing unique-cost assumption

Suppose a no unique-costs istance:
$$I=\langle G=(V,E),c:E\to\mathbb N\rangle$$
s.t. exists two edges $e\neq e'$ with the same costs $c(e)=c(e')$

Assume <u>for semplicity</u> that $c(e)\geq1$ (_it is sufficient to scale the cost of each edge by a constant factor_)

Let's create a new instance $\tilde{I}$, adding a little **perturbation** $b_e\leq\frac{1}{n^2}$ at all edge costs $c(e)$, s.t
$$\forall e\neq e',c(e)\gt c(e')\iff\tilde{c}(e)\gt\tilde{c}(e')$$
The new istance is $$\tilde{I}=\langle G=(V,E),\tilde{c}:e\to c(e)+b_e\rangle$$
### Proof

Assume by contradiction that exists a MST $T$ **better** than $\tilde{T}$ for the original instance $I$
$$cost(T,I)=\sum_{e\in T}c(e)\lt\sum_{e\in\tilde{T}}c(e)=cost(\tilde{T},I)$$
### Observation (I)

Since $forall e\in E$ we have $\tilde{c}(e)\leq c(e)+\frac{1}{n^2}$

$$\begin{align}cost(T,\tilde{I})&=\sum_{e\in T}\tilde{c}(e)\leq\sum_{e\in T}(c(e)+\frac{1}{n^2})\\&=\sum_{e\in T}c(e)+\underbrace{|T|}_{n-1}\cdot\frac{1}{n^2}\\&\lt cost(T,I)+\frac{1}{n}\\&cost(T,\tilde{I})\lt cost(T,I)+\frac{1}{n}\end{align}$$
### Observation (II)

By hypotesis of optimality of $T$, and because $c(e)\geq1$, we have 
$$cost(T,I)\leq cost(\tilde{T},I)-1$$
### Observation (III)

$$\begin{align}cost(\tilde{T},I)&=\sum_{e\in\tilde{T}}c(e)\lt\sum_{e\in\tilde{T}}\tilde{c}(e)\\&=cost(\tilde{T},\tilde{I})\lt cost(\tilde{T},\tilde{I})+\frac{1}{n}\\&cost(\tilde{T},I)\lt cost(\tilde{T},\tilde{I})+\frac{1}{n}\end{align}$$
### Observation (IV)

Combining **Obs (I)+Obs(II)**, we have
$$$$