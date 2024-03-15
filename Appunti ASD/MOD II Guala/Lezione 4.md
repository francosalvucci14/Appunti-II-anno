# Sempre su MST : Algoritmo di Prim

>[!definition]- Algoritmo di Prim
>Inizia prendendo un nodo sorgente $s$, e in modo greedy crea l'albero $T$. Ad ogni stepp aggiunge a $T$ l'arco $e$ di costo minimo, che ha esattamente un endpoint in $T$

**Correttezza** : Conseguenza diretta della cut property, usata esattamente n-1 volte

[Esempio Algoritmo di Prim](https://www.mat.uniroma2.it/~guala/03_mst_2023.pdf#35)

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

