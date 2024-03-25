# Minimum Spanning Tree

**Minimum spanning tree**. Grafo connesso $G=(V,E)$ con gli archi pesati con valori reali, detti $c_e$, un MST è un sottoinsieme $T\subseteq E$ tale che $T$ è un albero ricoprente[^1] dove la somma dei pesi degli archi è minimizzata

**Esempio**

![[Pasted image 20240312150759.png|center|500]]

>[!definition]- Teorema di Cayley
>Esistono $n^{n-2}$ alberi ricoprenti di $K_n$ ($K_n$ = grafo completo)

## Definizione formale

- **Input**: Grafo pesato e connesso $G=(V,E)$ con pesi reali $c_e$
- **Soluzione ammissibile** : Un albero ricoprente $T$ di $G$
- **Misura (da minimizzare)** : Il costo di $T$, ovvero $c(T)=\sum_{e\in T}c_e$

## Unicità del MST

L'MST _non_ è unico in generale

![[Pasted image 20240312152443.png|center|500]]

**Proprietà** : Se $G$ ha pesi distinti allora l'MST è unico

## Cicli e Tagli

**Ciclo** : Insieme di archi della forma $a-b,b-c,c-d,\dots,y-z,z-a$

![[Pasted image 20240312152856.png|center|500]]

**Taglio** : Un taglio è un sottoinsieme di nodi, detto S

**CutSet** : Il corrispondente cutset $D$ di $S$ è un sottoinsieme di archi con esattamente un endpoint in $S$

![[Pasted image 20240312153013.png|center|500]]

### Intersezione Ciclo-Taglio

**Claim** : Un ciclo e un cutset si intersecano in un numero pari di archi

![[Pasted image 20240312153117.png|center|500]]

**Dim** Tramite foto

![[Pasted image 20240312153146.png|center|500]]

### Algoritmi Greedy

>[!definition]- Cut property
>Sia $S$ un qualunque sottoinsieme di nodi, e sia $e$ l'arco di costo minimo con esattamente un endpoint in $S$. Allora esiste un MST che contiene $e$

>[!definition]- Cycle property
>Sia $C$ un qualunque ciclo, e sia $f$ l'arco di costo massimo in $C$. Allora esiste un MST che non contiene $f$

![[Pasted image 20240315101942.png|center|500]]

**Dimostrazione cut property (cambio di argomento)**
- Supponiamo che $e$ non appartenga al MST $T^\star$
- Aggiungere $e$ a $T^\star$ crea un ciclo $C$ in $T^\star$
- L'arco $e$ sta sia in $C$ che nel cutset $D$ corrispondete a $S\implies$ esiste un'altro arco, chiamato $f$, che sta sia in $C$ che in $D$
- $T'=T^\star\cup\{e\}-\{f\}$ è ancora uno ST
- Dato che $c_e\leq c_f\implies cost(T')\leq cost(T^\star)$
- Quindi $T'$ è un MST che contiene $e$

![[Pasted image 20240315102402.png|center|500]]

**Dimostrazione cycle property (cambio di argomento)**
- Supponiamo che $f$  appartenga al MST $T^\star$
- Eliminare $f$ da $T^\star$ crea un taglio $S$ in $T^\star$
- L'arco $f$ sta sia in $C$ che nel cutset $D$ corrispondete a $S\implies$ esiste un'altro arco, chiamato $e$, che sta sia in $C$ che in $D$
- $T'=T^\star\cup\{e\}-\{f\}$ è ancora uno ST
- Dato che $c_e\leq c_f\implies cost(T')\leq cost(T^\star)$
- Quindi $T'$ è un MST che non contiene $f$

## Algoritmo di Kruskal

>[!definition]- Algoritmo di Kruskal
>Inizia con $T=\emptyset$. Considera gli archi ordinati in modo crescente di costo. Inserisce l'arco $e$ in $T$ fino a quando $e$ non crea un ciclo

Un'implementazione efficente dell'algoritmo di Kruskal prevede di usare la struttura dati Union-Find
- Per mantenere le componenti connesse della soluzione corrente
- Per controllare quando l'arco che stiamo inserendo va a creare un ciclo (con la soluzione corrente)

### Pseudocodice

Lo pseudocodice di Kruskal è il seguente

![[Pasted image 20240315103439.png|center|400]]

[Esempio Funzionamento Algoritmo di Kruskal](https://www.mat.uniroma2.it/~guala/03_mst_2023.pdf?16)

## Running Time

- Ordinare gli archi -> $O(m\log(m))=O(m\log(n))$
- Operazioni sulla UF
	- n makeSet
	- m find
	- n-1 union
Il costo totale dell'algoritmo è $$O(m\log(n))+UF(m,n)$$
Se usiamo la QuickFind con l'euristica union-by-size il costo diventa
$$O(m\log(n))+m+n\log(n)=O(m\log(n))$$
Stessa cosa se usiamo la QuickUnion, sempre con l'euristica union-by-size


[^1]: Albero Ricoprente = Albero che tocca tutti i nodi di un grafo