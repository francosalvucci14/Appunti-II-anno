# Sempre su MST : Algoritmo di Prim

>[!definition]- Algoritmo di Prim
>Inizia prendendo un nodo sorgente $s$, e in modo greedy crea l'albero $T$. Ad ogni stepp aggiunge a $T$ l'arco $e$ di costo minimo, che ha esattamente un endpoint in $T$

**Correttezza** : Conseguenza diretta della cut property, usata esattamente n-1 volte

[Esempio Algoritmo di Prim](https://www.mat.uniroma2.it/~guala/03_mst_2023.pdf?35)

## Running Time

**Una possibile implementazione (la più semplice e inefficiente)**:
- Per n-1 volte, trovo l'arco di costo minimo che attraversa il taglio indotto dall'albero parziale, in tempo $O(m)$
- Costo totale $O(nm)$

**Implementazione più rapida e efficiente**:
- Mantiene un'insieme di nodi non esplorati, detto $S$
- Usa una coda con priorità per mantenere i nodi inesplorati
- Per ogni nodo non esplorato, la priorità di quel nodo è il costo di attachment, ovvero $a[v]$ = costo dell'arco di costo minimo incidente a v, che ha altri endpoint in $S$

## Pseudocodice

Lo pseudocodice dell'algoritmo di Prim è il seguente

![[Pasted image 20240315104733.png|center|500]]

**Tempo di esecuzione**

- $O(m+n)$ più il costo delle operazioni sulla coda
	- n inserimenti, n cancellazioni del minimo, m decrease key
- $O(n^2)$ con array, $O(m\log(n))$ con un heap binario
- $O(m+n\log(n))$ con gli heap di Fibonacci

Quindi, il tempo di esecuzione dell'algoritmo di Prim è
$$O(m+n\log(n))$$

----

# Clustering

>[!definition]- Clustering
>Insieme $U$ di n oggetti (che possono essere foto, documenti, micro-organismi,etc...) chiamati $p_1,\dots,p_n$, classificati in gruppi coerenti (**Cluster**)

>[!definition]- Funzione distanza
>Valore numerico che indica la "vicinanza" di due oggetti

**Problema fondamentale** : Dividere gli oggetti in cluster in modo tale che due punti in cluster diversi sono molto distanti

## Clustering di Spacing Massimo

**k-Clustering** : Dividere gli oggetti in $k$ gruppi non vuoti

**Funzione distanza** : Assumiamo che rispetti alcune proprietà naturali
- $d(p_i,p_j)=0\iff p_i=p_j$ **(identità)**
- $d(p_i,p_j)\geq0$ **(non negatività)**
- $d(p_i,p_j)=d(p_j,p_i)$ **(simmetria)**

**Spacing** : Distanza minima tra due coppie di punti in cluster diversi

>[!definition]- Clustering di Spacing Massimo
>Dato un intero $k$, trovare il k-clustering di spacing massimo

![[Pasted image 20240315105733.png|center|500]]

## Algoritmo Greedy Per Clustering

**Algoritmo Single-Linkage k-Clustering**:
- Crea un grafo sull'insieme dei vertici $U$, corrispondente a n cluster
- Trova la coppia di oggetti più vicini tale che i due oggetti si trovano in cluster diversi, e poi aggiungi un'arco tra i due
- Ripeti il procedimento $n-k$ volte, fino a quando non ci sono esattamente $k$ cluster

**Osservazione chiave** : Questo procedimento è esattamente l'algoritmo di Kruskal (solo che qui ci fermiamo quando abbiamo $k$ componenti connesse)

**Osservazione** : Questo è equivalente a trovare un MST e cancellare i $k-1$ archi di costo massimo

>[!definition]- Clustering Gerarchico
>Eseguire l'algoritmo di Kruskal fino alla fine genera, in modo implicito, un clustering gerarchico, ovvero un k-clustering per ogni valore di $k=n,n-1,\dots,1$

### Analisi dell'algoritmo

>[!definition]- Teorema
>Sia $C^\star$ un qualunque clustering, composoto dai cluster $C^\star_1,\dots,C^\star_k$, formato cancellando i $k-1$ archi più costosi del MST. Allora $C^\star$ è un k-clustering di spacing massimo

**Dimostrazione**

Sia $C$ un'altro clustering, formato dai cluster $C_1,\dots,C_k$
- Lo spacing di $C^\star$ è la lunghezza $d^\star$ del $(k-1)$-esimo arco più pesante del MST
- Siano $p_i,p_j$ due punti che stanno in un cluster di $C^\star$, detto $C^\star_r$, ma in due cluster diversi di $C$, detti $C_s,C_t$
- Un qualche arco $(p,q)$ sul percorso $p_i-p_j$ in $C^\star_r$ spazia due diversi cluster di $C$
- Tutti gli archi sul percorso $p_i-p_j$ hanno lunghezza $\leq d^\star$, dato che Kruskal li ha scelti nella sua soluzione
- Lo spacing di $C$, di conseguenza, è $\leq d^\star$ dato che $p$ e $q$ sono in due cluster diversi
- Quindi, $C^\star$ è un k-clustering di spacing massimo $\square$

![[Pasted image 20240315110930.png|center|400]]