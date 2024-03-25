# Programmazione Dinamica

Sommario :
- La tecnica della **programmazione dinamica** all'opera
- Un problema interessante : **insieme indipendente** di peso massimo (per un grafo a cammino)
	- Perchè le altre tecniche non funzionano
	- Ragionare sulla struttura/proprietà della soluzione
- Un algoritmo di programmazione dinamica con **complessità lineare**
- Principi generali della programmazione dinamica
	- sottoproblemi, relazioni fra sottoproblemi, tabelle

## Insieme indipendente di peso massimo (su grafi a cammino)

- Input : Un cammino $G$ di $n$ nodi. Ogni nodo $v_i$ ha peso $w_i$
- Goal : Trovare un insieme indipendente di peso massimo, ovvero un insieme $S$ di nodi tale che
	- $S$ è un $II$
	- $w(S)=\sum\limits_{v_{i}\in S}w_i$ è più grande possibile

![[Pasted image 20240325094757.png|center|500]]

>[!definition]- Insieme Indipendente
>Un insieme indipendente di $G$ è un sottoinsieme di nodi che contiene due nodi adiacenti, ovvero per ogni coppoia di nodi dell'insieme i due nodi non sono colelgati da un arco

**Vedi esempio** [Esempio](https://www.mat.uniroma2.it/~guala/04_DP_I_2023.pdf?5)
