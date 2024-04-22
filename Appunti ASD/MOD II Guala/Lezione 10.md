```table-of-contents
title: 
style: nestedList # TOC style (nestedList|inlineFirstLevel)
minLevel: 0 # Include headings from the specified level
maxLevel: 0 # Include headings up to the specified level
includeLinks: true # Make headings clickable
debugInConsole: false # Print debug info in Obsidian console
```
# Network Flow Parte 1

## Flow Network

>[!definition]- Flow Network
>Un **Flow Network** è una tupla $G=(V,E,s,t,c)$
>- Grafo diretto $(V,E)$ con sorgente $s\in V$ e pozzo $t\in V$
>- Capacità $c(e)\geq0,\forall e\in E$

**Intuizione** Il materiale "scorre" in un network di trasporto; il materiale è originato dalla sorgente e viene spedito al pozzo

![[Pasted image 20240422102222.png|center|500]]

### Minimum-Cut Problem

Diamo alcune definizioni prima di parlare del problema del `Taglio Minimo`

>[!definition]- st-cut
>Un $st-$cut è una partizione $(A,B)$ dei nodi con $s\in A$ e $t\in B$

>[!definition]- Capacità
>La **capacità** è la somma delle capacità degli archi da $A\to B$
>Quindi, $$cap(A,B)=\sum\limits_{\text{archi e uscenti da A}}c(e)$$

>[!warning]- Osservazione
>Numero di stcut $\leq2^{n-2}$ (forza bruta)

Alcuni esempi

![[Pasted image 20240422102556.png|center|500]]

![[Pasted image 20240422102614.png|center|500]]

A questo punto, possiamo parlare del problema del `Taglio Minimo`

**Min-Cut problem** : Trovare un taglio di capacità `minima`

![[Pasted image 20240422105303.png|center|500]]

Diamo ora la definizione del problema Maximum-Flow

### Maximum-Flow Problem

>[!definition]- st-flow (flow)
>Un $st-$flow $f$ è una funzione che soddisfa le seguenti condizioni:
>- $\forall e\in E : 0\leq f(e)\leq c(e)$ (capacità)
>- $\forall v\in V-\{s,t\}: \sum\limits_{\text{archi e entranti in v}}f(e)=\sum\limits_{\text{archi e uscenti da v}}f(e)$ (conservazione del flusso)

![[Pasted image 20240422105646.png|center|500]]

>[!definition]- Valore del flusso
>Il **valore** del flusso $f$ è $$val(f)=\sum\limits_{\text{archi e uscenti da s}}f(e)-\sum\limits_{\text{archi e entranti in s}}f(e)$$

![[Pasted image 20240422105827.png|center|500]]

Il problema del Max-Flow è quindi il seguente

**Max-Flow Problem** : Trovare un flusso di valore `massimo`

![[Pasted image 20240422105921.png|center|500]]

## Algoritmo di Ford-Fulkerson

### Verso l'algoritmo per il max-flow

Prima di definire l'algoritmo di FF, vediamo prima l'approccio greedy (dimostreremo che il greedy non va bene)

**Algoritmo greedy** :
- Inizia con $f(e)=0,\forall e\in E$ ![[Pasted image 20240422110228.png|center|500]]
- Trova un percorso $s\to t$, chiamato $P$, dove per ogni arco vale $f(e)\lt c(e)$ ![[Pasted image 20240422110322.png|center|500]]
- Aumenta il flusso lungo il percorso $P$ ![[Pasted image 20240422110424.png|center|500]]
- Ripeti finchè non ti blocchi ![[Pasted image 20240422110510.png|center|500]] ![[Pasted image 20240422110529.png|center|500]] ![[Pasted image 20240422110546.png|center|500]]
Come possiamo vedere dagli esempi, l'algoritmo greedy dice che il valore finale del flusso è 16, ma il valore del flusso massimo è 19

#### Perchè il greedy fallisce?

**D** : Perchè l'algoritmo greedy fallisce?
**R** : Una volta che il greedy incrementa il valore del flusso su un'arco, non lo decrementa mai

**Esempio** : Consideriamo il network flow $G$
- L'unico max flow $f^\star$ ha $f^\star(v,w)=0$
- L'algoritmo greedy sceglie il percorso $s\to v\to w\to t$ come primo percorso

![[Pasted image 20240422110900.png|center|300]]

**Linea di fondo** : Abbiamo bisogno di un meccanismo per "disfare" le decisioni sbagliate

#### Residual network

**Arco originale** : $e=(u,v)\in E$

![[Pasted image 20240422111326.png|center|300]]

