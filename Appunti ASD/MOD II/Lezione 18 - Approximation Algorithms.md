
# Approximation Algorithms

## Review: Decision Problems vs Optimization Problems in NP

Given any **Opt** Problem $Min-P = (X, Y (x),m(x,Y (x)),MIN/MAX)$ we can always define the corresponding **decision Problem** $k-P = (X, Y (x),m(x,Y (x)), \leq k (\geq k) )$

>[!definition]- FACT (Definition).
>The corresponding Opt problem Min-P is **NP-hard** $\iff$ the decision problem k-P is **NP-Hard**

>[!definition]- COR. 
>If $P \neq NP$ and Min-P is **NP-hard**, THEN there is no poly-time deterministic algorithm for it.

**Proof**. By contradiction
If Min-P would have a poly-time algo A( x ) then it can be used to decide k-P , for any k on the same instance x !

## Approximation Ratio (Error)

**Optimization Problem**
Given an optimization problem $P = (X, Y (x), m(x, Y (x)), MIN/MAX )$, we say A is an **r -approximation algorithm** for P if, for any instance $x \in X$ , the computation $A(x )$ returns a <u>feasible</u> solution $y^A$ such that:
$$\frac{m(x,y^A)}{opt(x)}\leq r\geq1\space(\text{in the case of MIN})$$

## Min-Vertex Cover

**k-VC**: Given a graph $G = (V, E)$ and an integer k, is there a k-size VC, i.e., a subset of
vertices $S \subseteq V$ such that $|S| \leq k$, and for each edge, at least one of its endpoints is in S?

**Min-VC**: Given a graph $G = (V, E)$, find a VC $S^\star$ for G of minimum size

Ex. there min-VC for the graph below has size 4.

![[appunti asd/mod ii/immagini/Pasted image 20230525144017.png|center|300]]

![[appunti asd/mod ii/immagini/Pasted image 20230525144043.png]] Vertex Cover

### A lower bound for optimal VC via Maximal Matchings

>[!definition]- DEF. [Maximal Matching]
>Given $G (V , E )$, a **Maximal Matching** $M \subseteq E$ is a maximal subset of edges that share no vertex of V.

**FACT 1**: Given any graph $G (V , E )$, consider any Maximal Matching $M \subseteq E$ . Then, any VC for G must contain at least 1 vertex for every edge in M.

Proof.
immediate consequence of def.s of Matching and VC.

**FACT 2** (Lower Bound for the Optimum): $opt(G ) \geq |M|$

### An apx algorithm for Min VC

Matching Algorithm M−ALG
- Input: $G (V , E)$;
- Find (any) Maximal Matching M;
- Return **C** = {all nodes touched by M};

>[!definition]- THM 3.
>M-ALG is a **2-apx algorithm** for Min-VC.

Proof of THM 3.
**FACT 4**. The returned solution C is:
1) always a VC for G 
2) $|C | = 2|M|$.

Proof. 
1) Immediate consequence of the fact that M is Maximal.
2) is trivial.

Recall FACT 2: $opt (G ) \geq |M| \space(3)$
From (2) and (3), it follows that:
$$\frac{|C |}{opt (G )}  \leq \frac{2|M|}{|M|}= 2$$
