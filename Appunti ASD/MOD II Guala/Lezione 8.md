
```table-of-contents
title: 
style: nestedList # TOC style (nestedList|inlineFirstLevel)
minLevel: 0 # Include headings from the specified level
maxLevel: 0 # Include headings up to the specified level
includeLinks: true # Make headings clickable
debugInConsole: false # Print debug info in Obsidian console
```

# Sequence Alignment

Prima di parlare del problema del Sequence Alignment, diamo la definizione di due 'sottoproblemi' che ci serviranno più avanti
## String similarity

Il problema della string similarity si occupa di rispondere a domande del tipo :

**D** : Quanto sono simili due stringhe?

Prendiamo in esempio le stringhe `ocurrance` e `occurrence`

![[Pasted image 20240411143810.png|center|500]]

## Edit distance

>[!definition]- Edit distance
>Penalità del gap $\delta$ (gap penalty)
>Penalità del mismatch $\alpha_{p,q}$ (mismatch penalty)
>Il costo totale è la somma delle penalità dei gap e dei mismatch

![[Pasted image 20240411144003.png|center|500]]

Prendiamo un'altro esempio

Qual'è l'edit distance tra queste due stringhe?

`PALETTE` e `PALATE`

Se assumiamo che $\delta=2$ e $\alpha=1$

![[Pasted image 20240411144223.png|center|200]]

Torniamo adesso al problema del Sequence Alignment

**Goal** : Date due stringhe $x_1,x_2,\dots,x_m$ e $y_1,y_2,\dots,y_n$, trovare l'`allineamento` di costo minimo

>[!definition]- Allineamento
>Un allineamento $M$ è un insieme di coppie ordinate $x_i-y_i$ tale che ogni carattere appare al più in una coppia e non si intersecano $$x_i-y_i\land x'_i-y'_i\text{ cross}\iff i\lt i',\text{but }j\gt j'$$

>[!definition]- Costo dell'allineamento
>Il costo dell'allineamento $M$ è $$cost(M)=\underbrace{\sum\limits_{(x_i,y_i)\in M}\alpha_{x_iy_i}}_{\text{mismatch}}+\underbrace{\sum\limits_{i:x_i\text{ unmatched}}\delta+\sum\limits_{j:y_j\text{ unmatched}}\delta}_{\text{gap}}$$

![[Pasted image 20240411145156.png|center|200]]

Un'allineamento di CTACCG e TACATG è
$$M=\{x_2-y_1,x_3-y_2,x_4-y_3,x_5-y_4,x_6-y_6\}$$
## Struttura del problema

>[!definition]- OPT(i,j)
>$OPT(i,j)$= costo minimo per allineare le stringhe prefisso $x_1,x_2,\dots,x_i$ e $y_1,y_2,\dots,y_j$

**Goal** : $OPT(m,n)$

Abbiamo due casistiche

1) Caso 1: $OPT(i,j)$ prende la coppia $x_i-y_j$
	1) Pago il costo del mismatch per la coppia $x_i-y_j$ + il costo minimo per allineare le stringhe $x_1,x_2,\dots,x_{i-1}$ e $y_1,y_2,\dots,y_{j-1}$
2) Caso 2a : $OPT(i,j)$ non prende il carattere $x_i$
	1) Pago il costo del gap per $x_i$ + il costo minimo per allineare le stringhe $x_1,x_2,\dots,x_{i-1}$ e $y_1,y_2,\dots,y_j$
3) Caso 2b : $OPT(i,j)$ non prende il carattere $y_j$
	1) Pago il costo del gap per $y_j$ + il costo minimo per allineare le stringhe $x_1,x_2,\dots,x_i$ e $y_1,y_2,\dots,y_{j-1}$

L'equazione di Bellman è la seguente

**Equazione di Bellman**

$$OPT(i,j)=\begin{cases}j*\delta&i=0\\i*\delta&j=0\\\min\begin{cases}\alpha_{x_iy_j}+OPT(i-1,j-1)\\\delta+OPT(i-1,j)\\\delta+OPT(i,j-1)\end{cases}&\text{altrimenti}\end{cases}$$

### Algoritmo Bottom-Up

L'algoritmo di tipo bottom-up per questo problema è il seguente

![[Pasted image 20240411150753.png|center|500]]

#### Traceback

![[Pasted image 20240411150830.png|center|500]]

#### Analisi dell'algoritmo

>[!definition]- Teorema
>L'algoritmo DP calcola l'edit distance (e l'allineamento ottimale) di due stringhe di lunghezza $m$ e $n$ in tempo e spazio $\Theta(mn)$

**Dimostrazione**

- L'algoritmo calcola l'edit distance
- Può tornare indietro per estrarre l'allineamento ottimale

Possiamo migliorare lo spazio usato dall'algoritmo usando l'algoritmo di Hirschberg, che adesso vedremo

----

# Algoritmo di Hirschberg

## Sequence Alignment in spazio lineare

>[!definition]- Teorema di Hirschberg
>Esiste un'algoritmo che trova l'allineamento ottimale i tempo $O(mn)$ e spazio $O(m+n)$
>- Combinazione del divide-et-impera e programmazione dinamica

### Migliorare lo spazio : primo approccio

![[Pasted image 20240411151552.png|center|400]]

Per calcolare la prossiamo colonna/riga della matrice abbiamo bisogno soltanto della colonna/riga precedente $\implies$ Manteniamo solo 2 colonne/righe a volta $\implies$ spazio usato $O(m+n)$

>[!info]- Osservazione
>Questo permette di calcolare l'edit distance ma non l'allineamento

