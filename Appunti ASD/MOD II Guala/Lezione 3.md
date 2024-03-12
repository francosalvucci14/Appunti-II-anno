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




[^1]: Albero Ricoprente = Albero che tocca tutti i nodi di un grafo