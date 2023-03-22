
# Clustering

![[appunti asd/mod ii/immagini/Pasted image 20230322090332.png|center|500]]

>[!definition]- Definition (Clustering)
>Given a set U of n objects labeled $p_1,..,p_n$, classify into coherent groups

>[!definition]- Definition (Distance function)
>Numeric value specifying "closeness" of two objects : $$distance(p_i,p_j)$$

**Fundamental problem** : Divide into clusters so that points in different clusters **are far apart**
- Routing in mobile ad hoc networks
- Identify patterns in gene expression
- Document categorization for web search
- Similarity searching in medical image databases
- Skycat : cluster $10^9$ sky objects into stars,quasars,galaxies.

## Clustering of Maximum Spacing

**k-Clustering** : Divide objects into k non-empty groups

**Distance function**. Assume it satisfies several natural properties
- $d(p_i,p_j)=0\iff p_i=p_j$ (identity of indiscernibles)
- $d(p_i,p_j)\geq0$ (non negativity)
- $d(p_i,p_j)=d(p_j,p_i)$ (symmetry)

>[!definition]- Definition (Spacing)
>Min distance between any pair of points in different clusters

**Clustering of maximum spacing** : Given an integer k, find a k-Clustering of _**maximum spacing**_

![[appunti asd/mod ii/immagini/Pasted image 20230322091519.png|center|500]]


soluzione ammissibile  : dati i cluster definire una k partizione di questi punti (una qualunque k partizione dei cluster iniziali)

Input del problema : Grafo connesso $G=(V=\{p_1,..,p_n\},E=V\times V\text{non ordinati})$   

## Greedy Clustering Algorithm

**Single-link k-Clustering algorithm**
- Form a graph on the vertex set U, corresponding to n clusters
- Find the **closest** pair (edge) of objects $(p,p')$ such that $p\:\&\:p'$ <u>are not in the same cluster</u>, and add **an edge** between them: so merging 2 clusters
- Repeat **n-k** times until there are exactly k clusters

**Key Obs 1** : This procedure is precisely Kruskal's Algorithm (exceot we stop when there are k connceted components)

**Key Obs 2** : Equivalent to finding an MST T and deleting the k-1 most expensive edges from T (thus forming k connetcet components)

### Analysis

**Theorem** : Let $C^\star$ denote the clustering $C_1^\star,...,C_k^\star$ formed by deleting the k-1 most expensive edges of an MST. Then, $C^\star$  is a k-clustering of _**maximal spacing**_

**Pf** : Let **C** denote some other clustering $C_1,...,C_k$
- The spacing of $C^\star$ is the lenght $d^\star$ of the $(k-1)^{st}$ **most expensive edge**
- Let p,p' be in the same cluster in $C^\star$, say $C_r^\star$, but different clusters in **C**, say $C_s,C_t$
- Some edge $(q,q')$ on $p\to p'$ path in $C_r^\star$ spans **two diff** clusters in **C**
- **All** edges on $p\to p'$ path have lenght $\leq d^\star$ since Kruskal chooses them
- Spacing of **C** is $\leq d^\star$ since q and q' are in <u><b>different</b></u> clusters in **C**

![[appunti asd/mod ii/immagini/Pasted image 20230322095427.png|center|300]]

---
# Union-Find

## Il problema Union-Find

Mantenere una **_collezione di insiemi disgiunti_** contenenti elementi distinti di un insieme (universo) U permettendo sequenze di operazioni del seguente tipo : 
- **makeSet(x)** = crea il nuovo insieme $x=\{x\}$
- **union(A,B)** = unisce gli insiemi A e B in un univo insieme, di nome A, e distrugge i vecchi insiemi A e B (si suppone di accedere direttamente agli insiemi A,B)
- **find(x)** = restituisce il nome dell'insieme contenente l'elemento x (si suppone di accedere **direttamente** all'elemento x) 

**Esempio**

![[appunti asd/mod ii/immagini/Pasted image 20230322101856.png|center|500]]

n=6
L'elemento in **grassetto** da il nome all'insieme

D: Se ho n elementi, quante union posso fare al più?
R : n-1

**Idea generale** : Rappresentare gli insiemi disgiunti con una foresta

Ogni insieme è un **albero radicato**

La **radice** contiene il nome dell'**insieme** (elemento rappresentativo)

### Alberi QuickFind

Usiamo una foresta di alberi di altezza 1 per rappresentare gli insiemi disgiunti. In ogni albero : 
- Radice = nome dell'insieme
- Foglie = elementi (incluso l'elemento rappresentativo, il cui valore è nella radice e da il nome all'insieme)

#### Realizzazione (1/2)

![[appunti asd/mod ii/immagini/Pasted image 20230322103123.png|center|500]]

#### Realizzazione (2/2)

![[appunti asd/mod ii/immagini/Pasted image 20230322103203.png|center|500]]



