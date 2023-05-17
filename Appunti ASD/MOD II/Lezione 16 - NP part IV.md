# Polynomial-Time Reductions

## Classify Problems According to Computational Requirements

Q. Which problems will we be able to solve in practice?
A working definition. `[von Neumann 1953, Godel 1956, Cobham 1964, Edmonds 1965, Rabin 1966]`
Those with **polynomial-time** algorithms.

![[appunti asd/mod ii/immagini/Pasted image 20230517092453.png|center|500]]

### Classify Problems

**Desiderata**. Classify problems according to those that can be solved in _**polynomial-time**_ and those that cannot.

**Provably requires exponential-time.**
- Given a **_Turing machine_**, does it halt in at most _**k**_ steps?
- Given a board position in an _**n-by-n**_ generalization of chess, can _**black**_ guarantee a win?

**Frustrating news**. Huge number of fundamental problems have defied classification for decades.

**This chapter**. Show that these fundamental problems are "_**computationally equivalent**_" and appear to be different manifestations of one really **hard problem**.

## Polynomial-Time Reduction

**Desiderata**. Suppose we could solve Y in _polynomial-time_. What else could we solve in polynomial time?

>[!definition]- Reduction. 
>Problem X _**polynomial reduces to problem**_ Y if arbitrary instances of problem X can be solved using:
>- _Polynomial_ number of standard computational steps, plus 
>- _Polynomial_ number of calls to oracle that solves problem Y.

Notation. $X\preceq_{p} Y.$

Remarks.
- We pay for time to **write down** instances sent to black box $\to$ instances of Y must be of _polynomial size **in the instance of X**._
- Note: Cook reducibility.

**Purpose**. Classify problems according to relative difficulty.

The use of poly-time reduction.

**Design algorithms**. If $X\preceq_p Y$ and Y can be solved in _polynomial-time_, then X can also be solved in _polynomial time._

**Establish intractability**. If $X\preceq_p Y$ and X _**cannot be solved**_ in polynomial time, then Y **cannot be solved** in polynomial time as well.

**Establish equivalence**. If $X\preceq_p Y$ and $Y\preceq_p X$, we use notation $X\equiv_p Y$.

### Reduction By Simple Equivalence

#### Independent Set

**INDEPENDENT SET**: Given a graph $G = (V, E)$ and an integer k, is there a subset of vertices $S \subseteq V$ such that $|S|\geq k$, and for each edge at most one of its endpoints is in S?

Ex. Is there an independent set of size $\geq$ 6? Yes.
Ex. Is there an independent set of size $\geq$ 7? No.

![[appunti asd/mod ii/immagini/Pasted image 20230517093719.png|center|500]]

#### Vertex Cover

**VERTEX COVER**: Given a graph $G = (V, E)$ and an integer k, is there a subset of vertices $S \subseteq V$ such that $|S| \leq k$, and for each edge, at least one of its endpoints is in S?

Ex. Is there a vertex cover of size $\leq$ 4? Yes.
Ex. Is there a vertex cover of size $\leq$ 3? No

![[appunti asd/mod ii/immagini/Pasted image 20230517093831.png|center|500]]


##### Hardness of Vertex Cover

**VERTEX COVER**: Given a graph $G = (V, E)$ and an integer k, is there a subset of vertices $S \subseteq V$ such that $|S| \leq k$, and for each edge, at least one of its endpoints is in S?

Excercise: Greedy does not work!
1) Select the node v with maximal degree (break ties arbitraly)
2) remove v and its edges
3) apply step 1 to the new graph until all edges are covered.

Show the algorithm does not find (always) the optimum.

#### Vertex Cover and Independent Set

Claim. **VERTEX-COVER** $\equiv_p$ **INDEPENDENT-SET**.
Pf. We show $S$ is an independent set **iff** $V - S$ is a vertex cover.

![[appunti asd/mod ii/immagini/Pasted image 20230517094122.png|center|500]]


**Claim 1**. S is an independent set $\iff$ V - S is a vertex cover
Pf.
$\to$
- Let S be any independent set.
- Consider an arbitrary edge (u, v).
- S independent $\to$ $u \not\in S$ or $v \not\in S$ $\to$ $u \in V - S$ or $v \in V - S.$
- Thus, $V - S$ **covers** (u, v).
$\leftarrow$
- Let V - S be any vertex cover.
- Consider two nodes $u\in S$ and $v\in S$.
- Observe that $(u, v)\in E$ since V - S is a vertex cover.
- Thus, no two nodes in S are joined by an edge $\to$ S independent set. $\square$

>[!definition]- THM
>**VERTEX-COVER** $\equiv_p$ **INDEPENDENT-SET**.


Pr.
- $VC \preceq_p P IS$; **Hypothesis: Poly-time Alg. A(--) for IS**
- Given instance $X = \langle G(V,E) ; k\gt0 \rangle$ of VC;
- Transform it into instance $Y=\langle G(V,E) , k’=n-k\rangle$;
- Apply **Algo A(Y)** (thanks to Claim 1)
- $IS\preceq_p VC$; Similar.

### Reduction from Special Case to General Case

#### Set Cover

**SET COVER**: Given a set of elements, a collection $S_1, S_2,\dots , S_m$ of subsets of U, and an integer k, does there exist a collection of $\leq$ k of these sets whose union is **equal** to U?

Sample application.
- m available pieces of software $W_1,\dots,W_m$.
- Set U of n capabilities that we would like our system to have.
- The ith piece of software provides the set $S_i \subseteq U$ of capabilities.
- Goal: achieve all n capabilities using fewest pieces of software.

![[appunti asd/mod ii/immagini/Pasted image 20230517095309.png|center|500]]


##### Vertex Cover Reduces to Set Cover

**Claim**. **VERTEX-COVER** $\preceq_p$ **SET-COVER.**
Pf. Given a VERTEX-COVER instance G = (V, E), k, we construct a set cover instance whose size equals the size of the vertex cover instance.

**Construction**.

- **GOAL of reductions:** _Programming with the language of the second problem_
- _VC **Language**_: 
	- Q. What means when we select a node v in V ? 
	- A. We cover all its edges
- _SC **Language**_: 1 edge $\to$ 1 element of the Universe U
	- 1 vertex v $\to$ 1 subset of U = edges covered by v
- Create SET-COVER instance: 
	- $k = k, U = E, \forall v \in V: S_v = \{e \in E :\text{ e incident to v} \}$
- Set Cover of size $\leq k \iff$ Vertex Cover of size $\leq k$.

![[appunti asd/mod ii/immagini/Pasted image 20230517100055.png|center|600]]


### Reductions via "Gadgets"

#### Satisfiability

**Literal**: A Boolean variable or its negation. $x_i$ or $\neg x_i$

**Clause**: A disjunction of literals. $C_j = x_1 \lor \neg x_2 \lor x_3$

**Conjunctive normal form**: A propositional formula $\Phi$ that is the conjunction of clauses.
$\Phi=C_1 \land C_2\land C_3\land C_4$

>[!definition]- Def. 
>The size $| \Phi |$ is the number of clauses.

**SAT**: Given CNF formula $\Phi$, does it have a satisfying truth assignment?
**3-SAT**: SAT where each clause contains exactly 3 literals.

![[appunti asd/mod ii/immagini/Pasted image 20230517101954.png|center|500]]

#### 3 Satisfiability Reduces to Independent Set

Claim. **3-SAT** $\preceq_p$ **INDEPENDENT-SET.**
Pf. Given an instance $\Phi$ of 3-SAT, we construct an instance (G, k) of INDEPENDENT-SET that has an independent set of size $k \iff \Phi$ is **satisfiable**.

Construction.
- G contains 3 vertices for each clause, one for each literal.
- Connect 3 literals in a clause in a triangle = _**GADGET**_
- Connect **positive** literal to each of its **negations**.
- set $k = | \Phi |$

![[appunti asd/mod ii/immagini/Pasted image 20230517102305.png|center|600]]


