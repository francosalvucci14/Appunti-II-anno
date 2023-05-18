# Sequencing Problems

## Hamiltonian Cycle

**HAM-CYCLE**: given an undirected graph $G = (V, E)$, does there exist a simple cycle G that contains every node in V.

![[appunti asd/mod ii/immagini/Pasted image 20230518143231.png|center|550]]

![[appunti asd/mod ii/immagini/Pasted image 20230518143408.png|center|550]]

### Directed Ham-Cycle

**DIR-HAM-CYCLE**: given a _**digraph**_ $G = (V, E)$, does there exists a simple <u>directed</u> cycle $\Gamma$ that contains every node in V?

>[!definition]- THM 1. 
>**DIR-HAM-CYCLE** $\preceq_p$ **HAM-CYCLE.**

Pf. Given a directed graph $G = (V, E)$, construct an undirected graph $G'$ with $3n$ nodes.

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



