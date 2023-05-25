
# Part I

## Approximation Algorithms

### Review: Decision Problems vs Optimization Problems in NP

Given any **Opt** Problem $Min-P = (X, Y (x),m(x,Y (x)),MIN/MAX)$ we can always define the corresponding **decision Problem** $k-P = (X, Y (x),m(x,Y (x)), \leq k (\geq k) )$

>[!definition]- FACT (Definition).
>The corresponding Opt problem Min-P is **NP-hard** $\iff$ the decision problem k-P is **NP-Hard**

>[!definition]- COR. 
>If $P \neq NP$ and Min-P is **NP-hard**, THEN there is no poly-time deterministic algorithm for it.

**Proof**. By contradiction
If Min-P would have a poly-time algo A( x ) then it can be used to decide k-P , for any k on the same instance x !

### Approximation Ratio (Error)

**Optimization Problem**
Given an optimization problem $P = (X, Y (x), m(x, Y (x)), MIN/MAX )$, we say A is an **r -approximation algorithm** for P if, for any instance $x \in X$ , the computation $A(x )$ returns a <u>feasible</u> solution $y^A$ such that:
$$\frac{m(x,y^A)}{opt(x)}\leq r\geq1\space(\text{in the case of MIN})$$

### Min-Vertex Cover

**k-VC**: Given a graph $G = (V, E)$ and an integer k, is there a k-size VC, i.e., a subset of
vertices $S \subseteq V$ such that $|S| \leq k$, and for each edge, at least one of its endpoints is in S?

**Min-VC**: Given a graph $G = (V, E)$, find a VC $S^\star$ for G of minimum size

Ex. there min-VC for the graph below has size 4.

![[appunti asd/mod ii/immagini/Pasted image 20230525144017.png|center|300]]

![[appunti asd/mod ii/immagini/Pasted image 20230525144043.png]] Vertex Cover

#### A lower bound for optimal VC via Maximal Matchings

>[!definition]- DEF. [Maximal Matching]
>Given $G (V , E )$, a **Maximal Matching** $M \subseteq E$ is a maximal subset of edges that share no vertex of V.

**FACT 1**: Given any graph $G (V , E )$, consider any Maximal Matching $M \subseteq E$ . Then, any VC for G must contain at least 1 vertex for every edge in M.

Proof.
immediate consequence of def.s of Matching and VC.

**FACT 2** (Lower Bound for the Optimum): $opt(G ) \geq |M|$

#### An apx algorithm for Min VC

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

---
# Part II

## Load Balancing

**Input**. _m_ identical machines; _n_ jobs, job _j_ has processing time $t_j$.
- Job j must run contiguously **on one** machine.
- A machine can process **at most one job** at a time.

>[!definition]- Def (Feasible Solutions). 
>Let $J(i)$ be the subset of jobs assigned to machine i. The load of machine i is $$L_i=\sum\limits_{j\in J(i)}t_j$$

>[!definition]- Def(Cost of a Solution). 
>The **makespan** is the maximum load on any machine $L = max \{ L_i : i = 1,\dots, m \}$

The Load Balancing Problem (It is **NP-HARD**):
Assign each job j to a machine i to _minimize **makespan**_.

### Greedy Approach

**List-Scheduling (LS) algorithm.**
- Consider n jobs in any fixed order.
- Assign job j to a machine whose load is the smallest one <u>so far</u>

![[appunti asd/mod ii/immagini/Pasted image 20230525152135.png|center|500]]

**Implementation**. $O(n\log(m))$ using a **priority queue.**

### List Scheduling Analysis

>[!definition]- Theorem. [Graham, 1966] 
>LS algorithm is 2-approximation.

- First **worst-case analysis** of an approximation algorithm.
- Need to compare LS solution with **optimal** makespan $L^\star$.

**Lemma 1**. The optimal **makespan** $L^\star\geq max_j{t_j}.$ 
Pf. Some machine must process the most time-consuming job.

**Lemma 2**. The optimal makespan $L^\star \geq \frac{1}{m} \sum\limits_{j} t_j$
Pf.
- The total processing time (i.e. total work) is $\sum\limits_{j} t_j$ .
- One of the m machines <u>must</u> do at least a $\frac{1}{m}$ fraction of total **work**. 

Pf of Theorem. 
Consider load $L_i$ of bottleneck machine i.
- Let j be <u>last</u> job scheduled on machine i.
- When job j assigned to machine i, i had **smallest load**. Its load <u>before</u> assignment is $$L_i - t_j \to L_i - t_j \leq L_k\space\space \forall 1 \leq k \leq m$$
![[appunti asd/mod ii/immagini/Pasted image 20230525153132.png|center|700]]

- Sum inequalities over all k and **divide** by m:
$$\begin{align}m (L_i - t_j ) &\leq\sum\limits L_k\\L_i-t_j&\leq\frac{1}{m} \sum\limits_{k} L_k\\&=\frac{1}{m} \sum\limits_{k} t_k\\Lem.1\to&\leq L^\star\end{align}$$
- **Now** $$L_i = \underbrace{(L_i - t_j )}_{\leq L^\star} + \underbrace{t_j}_{\leq L^{\star}(\text{Lemma 2})} \leq 2L^\star$$
Q. Is our analysis tight?
A. **Essentially yes**.

Ex: m machines, n= m(m-1) jobs: length 1 jobs, one job of length m
LS SOLUTION:

![[appunti asd/mod ii/immagini/Pasted image 20230525154456.png|center|600]]

OPTIMAL SOLUTION:

![[appunti asd/mod ii/immagini/Pasted image 20230525154526.png|center|600]]










