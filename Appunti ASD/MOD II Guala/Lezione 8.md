
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

## Edit distance su grafi

>[!definition]- Edit distance su grafi
>Sia $f(i,j)$ la lunghezza dello shortest path da $(0,0)\to(i,j)$

**Lemma** : $f(i,j)=OPT(i,j)\space\forall i,j$

![[Pasted image 20240412113813.png|center|600]]


**Dimostrazione del Lemma** (tramite induzione forte su $i+j$)
- Caso base : $f(0,0)=OPT(0,0)=0$
- Ipotesti induttiva : Assumi che è vera $\forall(i',j')$ con $i'+j'\lt i+j$
- L'ultimo arco dello shortest path $\to(i,j)$ viene da $(i-1,j-1),(i-1,j)$ oppure $(i,j-1)$
- Quindi, abbiamo che $$\begin{align}f(i,j)&=\min\{\alpha_{x_iy_j}+f(i-1,j-1),\delta+f(i-1,j),\delta+f(i,j-1)\}\\&=\underbrace{\min\{\alpha_{x_iy_j}+OPT(i-1,j-1),\delta+OPT(i-1,j),\delta+OPT(i,j-1)\}}_{\text{Ipotesi induttica}}\\&=\underbrace{OPT(i,j)}_{\text{Equazione di Bellman}}\square\end{align}$$
![[Pasted image 20240412115337.png|center|100]]

Si può calcolare $f(\star,j)$ per ogni $j$ in tempo $O(mn)$ e spazio $O(m+n)$

![[Pasted image 20240412115607.png|center|500]]

Diamo la definizione di un'altra funzione simile a $f(i,j)$

>[!definition]- Edit distance su grafi (2)
>Sia $g(i,j)$ la lunghezza dello shortest path da $(i,j)\to(m,n)$

![[Pasted image 20240412115809.png|center|500]]

Si può calcolare $g(i,j)$ invertendo l'orientamento degli archi e invertendo i ruoli di $(0,0)$ e $(m,n)$

![[Pasted image 20240412115906.png|center|500]]

![[Pasted image 20240412115958.png|center|500]]

Ora un paio di osservazioni fondamentali

>[!info]- Osservazione 1
>La lunghezza dello SP che usa $(i,j)$ è $f(i,j)+g(i,j)$

**Dimostrazione per foto**

![[Pasted image 20240412120100.png|center|500]]

>[!info]- Osservazione 2
>Sia $q$ un indice che minimizza $f(q,\frac{n}{2})+g(q,\frac{n}{2})$
>Allora esiste uno SP da $(0,0)\to(m,n)$ che usa $(q,\frac{n}{2})$

**Dimostrazione per foto**

![[Pasted image 20240412120245.png|center|500]]

## Algoritmo di Hirschberg

**Divide** : Trova l'indice $q$ che minimizza $f(q,\frac{n}{2})+g(q,\frac{n}{2})$; salva il nodo $i-j$ come parte della soluzione

**Conquista** : Calcola ricorsivamente l'allineamento ottimo in ogni pezzo

![[Pasted image 20240412120408.png|center|500]]

### Analisi dello spazio

>[!definition]- Teorema di Hirschberg
>L'algoritmo di Hirschberg usa spazio $\Theta(m+n)$

**Dimostrazione**

- Ogni chiamata ricorsva usa spazio $\Theta(m)$ per calcolare $f(\star,\frac{n}{2})$ e $g(\star,\frac{n}{2})$
- Server solo $\Theta(1)$ di spazio per mantenere le chiamate ricorsive
- Il numero di chiamare ricorsive è $\leq n$

### Analisi del tempo di esecuzione

>[!definition]- Teorema
>Sia $T(m,n)$ il massimo tempo di esecuzione dell'algoritmo di Hirschberg su una strigna di lunghezza al più $m$ e $n$.
>Allora $T(m,n)=O(mn)$

**Dimostrazione** (induzione forte su $m+n$)
- $O(mn)$ tempo per calcolare $f(\star,\frac{n}{2})$ e $g(\star,\frac{n}{2})$ e trovare l'indice $q$
- $T(q,\frac{n}{2})+T(m-q,\frac{n}{2})$ tempo per le due chiamate ricorsive
- Scegli una costante $c$ tale che : $$\begin{align}&T(m,2)\leq cm\\&T(2,n)\leq cn\\&T(m,n)\leq cmn+T(q,n/2)+T(m-q,n/2)\end{align}$$
- Claim : $T(m,n)\leq2cmn$
- Dimostriamolo :
	- Caso base : $m=2\land n=2$
	- Ipotesi induttiva : $T(m',n')\leq2cm'n'$ per ogni $(m',n')$ con $m'+n'\lt m+n$
	- Quindi : $$\begin{align}T(m,n)&\leq T(q,n/2)+T(m-q,n/2)+cmn\\&\underbrace{\leq2cq*n/2+2c(m-q)n/2+cmn}_{\text{Ipotesi Induttiva}}\\&=cqn+cmn-cqn+cmn\\&=2cm\space\square\end{align}$$