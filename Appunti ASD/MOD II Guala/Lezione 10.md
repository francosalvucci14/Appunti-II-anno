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

## Minimum-Cut Problem

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

## Maximum-Flow Problem

>[!definition]- st-flow (flow)
>Un $st-$flow $f$ è una funzione che soddisfa le seguenti condizioni:
>- $\forall e\in E : 0\leq f(e)\leq c(e)$ (capacità)
>- $\forall v\in V-\{s,t\}: \sum\limits_{\text{archi e entranti in v}}f(e)=\sum\limits_{\text{archi e uscenti da v}}f(e)$ (conservazione del flusso)

![[Pasted image 20240422105646.png|center|500]]

>[!definition]- Valore del flusso
>Il **valore** del flusso $f$ è $$val(f)=\sum\limits_{\text{archi e uscenti da s}}f(e)-\sum\limits_{\text{archi e entranti in s}}f(e)$$

![[Pasted image 20240422105827.png|center|500]]
