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

asd

[^1]: Albero Ricoprente = Albero che tocca tutti i nodi di un grafo