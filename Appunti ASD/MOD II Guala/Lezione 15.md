```table-of-contents
title: 
style: nestedList # TOC style (nestedList|inlineFirstLevel)
minLevel: 0 # Include headings from the specified level
maxLevel: 0 # Include headings up to the specified level
includeLinks: true # Make headings clickable
debugInConsole: false # Print debug info in Obsidian console
```
# Algoritmi di Approssimazione

## Affrontare la NP-Completezza

**D** : Supponiamo di dover risolvere un problema di ottimizzazione $NPC$. Cosa dovrei fare?

**R** : Sacrificare una di queste funzioni desiderate
- Viene eseguito in tempo polinomiale
- Risolvere istanze arbitrarie del problema
- Trovare una soluzione ottimale al problema (**Sacrifichiamo questo**)

Algoritmo $\rho-$approssimante :
- Eseguito in tempo polinomiale
- Risolvere istanze arbitrarie del problema
- Trovare una soluzione che si trova entro il rapporto $\rho$ dell'ottimo

**Challenge** :
Abbiamo la necessità di dimostrare che il valore di una soluzione è vicino all'ottimo, senza sapere quale sia il valore ottimale

>[!definition]- Algoritmo $\alpha-$approsimante
>Un algoritmo $\alpha-$approssimante per un problema di ottimizzazione è un algoritmo polinomiale che per tutte le istanze del problema, produce una soluzione il cui valore entra nel rapporto $\alpha$ del valore della soluzione ottima

$\alpha$ : Viene chiamato **rapporto di approssimazione** o **fattore di approssimazione**

**Problema di minimizzazione** :
- $\alpha\geq1$
- Per ogni soluzione $x,cost(x)\leq\alpha OPT(x)$

**Problema di massimizzazione** :
- $\alpha\leq1$
- Per ogni soluzione $x,valore(x)\geq\alpha OPT(x)$

## Problema del Load Balancing

**Input** : $m$ macchine identiche; $n\geq m$ jobs; il job $j$ ha tempo di processamento pari a $t_j$
- Il job $j$ deve essere eseguito in modo continuo su una macchina
- Una macchina può processare al più un job alla volta

>[!definition]- Carico della macchina
>Sia $S[i]$ un sottoinsieme dei job assegnati alla macchina $i$.
>Il **carico** della macchina $i$ è $L[i]=\sum\limits_{j\in S[i]}t_j$

>[!definition]- Makespan
>Il **makespan** è il massimo carico di ogni macchina $L=\max_i\{L[i]\}$

Quindi, il problema del **Load Balancing** è quello di assegnare ogni job a una macchina per minimizzare il makespan

![[Pasted image 20240523113718.png|center|500]]

### Load Balancing su due macchine è NP-Hard

**Claim** : Load Balancing è hard anche se abbiamo $m=2$ macchine
**Dim** : $PARTITION\leq_pLOAD-BALANCE$

![[Pasted image 20240523113839.png|center|500]]

### Load Balancing : List Scheduling

**Algoritmo list-scheduling**
- Consideriamo $n$ job in un qualche ordine
- Assegnamo il job $j$ alla macchina $i$ il cui carico è finora il più basso

![[Pasted image 20240523114011.png|center|500]]

**Implementazione** : Tempo $O(n\log(n))$ usando una coda con priorità per i carichi $L[k]$

Vedi esempio qui -> [Esempio](https://www.mat.uniroma2.it/~guala/09_Apx_Algorithms_I_2023.pdf#page=9)

#### Load Balancing : Analisi del List Scheduling

>[!definition]- Teorema `[Graham 1966]`
>L'algoritmo greedy è 2-approssimante
>- Prima analisi del caso peggiore di un algoritmo di approssimazione.
>- È necessario confrontare la soluzione risultante con il makespan ottimale $L^\star$

**Lemma 1** : Per ogni $k$ : il makespan ottimo è $L^\star\geq t_k$
**Dim** : Una qualche macchina deve elaborare il lavoro più dispendioso in termini di tempo

**Lemma 2** : Il makespan ottimo è $L^\star\geq\frac{1}{m}\sum\limits_kt_k$
**Dim**
- Il tempo totale di processamento è $\sum\limits_kt_k$
- Una delle $m$ macchine deve fare almeno una frazione $\frac{1}{m}$ del lavoro totale

