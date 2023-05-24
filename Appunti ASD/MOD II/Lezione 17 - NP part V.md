# Sequencing Problems

## Hamiltonian Cycle

**HAM-CYCLE**: given an undirected graph $G = (V, E)$, does there exist a simple cycle G that contains every node in V.

![[appunti asd/mod ii/immagini/Pasted image 20230518143231.png|center|550]]

![[appunti asd/mod ii/immagini/Pasted image 20230518143408.png|center|550]]

>[!info]- Osservazione
>Il problema Hamiltonian Cycle è NP-Completo
>Questo perchè $$\text{HAMILTONIAN-CYCLE}\preceq_p\text{HAMILTONIAN PATH}\preceq_{p}\text{LONGHEST PATH}$$
>E Longhest PAth è NP-Completo

### Directed Ham-Cycle

**DIR-HAM-CYCLE**: given a _**digraph**_ $G = (V, E)$, does there exists a simple <u>directed</u> cycle $\Gamma$ that contains every node in V?

>[!definition]- THM 1. 
>**DIR-HAM-CYCLE** $\preceq_p$ **HAM-CYCLE.**

Pf. Given a <u>directed</u> graph $G = (V, E)$, construct an <u>undirected</u> graph $G'$ with $3n$ nodes.

![[appunti asd/mod ii/immagini/Pasted image 20230518143728.png|center|550]]

![[appunti asd/mod ii/immagini/Pasted image 20230518144000.png|center|700]]


## 3-SAT Reduces to Directed Hamiltonian Cycle

>[!definition]- THM 2. 
>**3-SAT** $\preceq_p$ **DIR-HAM-CYCLE.**

Proof. Given an instance $\Phi$ of 3-SAT, we construct an instance G(V,E) of DIR-HAM-CYCLE such that:
- G has a **Hamiltonian cycle** $\iff \Phi$ **is satisfiable.**

_Construction_. First, create graph that has $2^n$ Hamiltonian **cycles** which correspond in a natural way to $2^n$ possible truth assignments for $\Phi$

_Construction_. Given 3-SAT instance $\Phi$ with **n** variables $x_i$ and **k** clauses.
- Construct G to have $2^n$ Hamiltonian cycles.
- Intuition: traverse path i from left to right $\iff$ set variable $x_i = 1.$

![[appunti asd/mod ii/immagini/Pasted image 20230518145250.png|center|600]]

For each clause $C_j$: add a gadget with 1 grey node and 6 edges.

![[appunti asd/mod ii/immagini/Pasted image 20230518145636.png|center|600]]


>[!definition]- THM. 
>**HAMILTONIAN-CYCLE** $\preceq_p$ **HAMILTONIAN PATH**

**Proof (sketch).** $G(V,E)$ has a **Hamilton Cycle** $\iff$ f(G) has a _**Hamilton Path**_.
From $G=(V,E)$ , construct $G’(V’,E’) = f(G)$ as follows.
- Fix any $v\in V$ and add 3 **new** nodes: $v',s,t\in V.$
- $v'$ is a "copy" of v, and add a **source** s and a sink t, connected to v,v′, respectively. (See Figure)
- Add **edges** $\{(v',w)|(v,w) ∈ E\} \cup \{(s,v),(v',t),(v,v')\}.$

If G has a **Hamiltonian Cycle HC** then it can be transformed into a **Hamiltonian Path** for $G’= f(G)$ starting from s and ending to t and viceversa.

![[appunti asd/mod ii/immagini/Pasted image 20230518151141.png|center|600]]


## Longest Path

**SHORTEST-PATH**. Given a digraph $G = (V, E)$, does there exists a simple path of **length at most k edges**?

**LONGEST-PATH**. Given a digraph $G = (V, E)$, does there exists a simple path of **length at least k edges**?

>[!definition]- THM. 
>LONGEST-PATH is **NP-Complete**

Proof.
**LEMMA**: **HAM-PATH** $\preceq_p$ **LONGEST-PATH:**
PROOF (of Lemma): Trivial, take: $G(V,E) \to \langle G(V,E), k=n-1\rangle$ 

## Traveling Salesperson Problem

**TSP**. Given a set of n cities and a pairwise distance function $d(u, v)$, is there a tour of length $\leq D$?

![[appunti asd/mod ii/immagini/Pasted image 20230518153109.png|center|600]]

![[appunti asd/mod ii/immagini/Pasted image 20230518153156.png|center|600]]


![[appunti asd/mod ii/immagini/Pasted image 20230518153230.png|center|600]]

![[appunti asd/mod ii/immagini/Pasted image 20230518153257.png|center|600]]

**TSP**. Given a set of n cities and a pairwise distance function **d(u,v)**, is there a tour/cycle of length $\leq D$?

**HAM-CYCLE**: given a graph G = (V, E), does there exists a simple cycle that contains every node in V (i.e. a Hamiltonian Cycle)?

Claim. **HAM-CYCLE** $\preceq_p$ **TSP**.
Proof. Given instance $G = (V, E)$ of HAM-CYCLE with $|V| = n$:
- create n cities with distance function $$d(u,v)=\begin{cases}1&(u,v)\in E\\2&(u,v)\not\in E\end{cases}$$
- TSP instance has tour of length $\leq n \iff G$ is Hamiltonian.


