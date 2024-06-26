
```table-of-contents
title: 
style: nestedList # TOC style (nestedList|inlineFirstLevel)
minLevel: 0 # Include headings from the specified level
maxLevel: 0 # Include headings up to the specified level
includeLinks: true # Make headings clickable
debugInConsole: false # Print debug info in Obsidian console
```

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

## Progettazione dell'algoritmo : che tecnica usare?

### Forza bruta : enumerazione

**Idea** : enumeriamo tutti i sottoinsiemi degli $n$ ndoi, per ognuno verifichiamo che è un insieme indipendente, ne calcoliamo il peso e teniamo quello di peso massimo

**Domanda** : quanti sottoinsiemi guardiamo?
**Risposta** : troppi, sono $2^n$

### Approccio greedy (goloso)

**idea** : Costruisco la soluzione in modo incrementale scegliendo ogni volta il nodo indipendente di valore massimo

**Domanda** : funziona?
**Risposta** : su questa istanza l'algoritmo se l'è cavata bene, ma in generale l'approccio greedy non funziona

Vediamo un controesempio

![[Pasted image 20240325095435.png|center|500]]

### Divide et impera

**idea** : divido il cammino a metà, calcolo ricorsivamente l'$II$ di peso massimo sulle due metà e poi ricombino le soluzioni

**domanda** : è corretto?
**domanda2** : posso risolvere (efficientemente) i conflitti che ho quando ricombino?

![[Pasted image 20240325095620.png|center|300]]

## Cosa non sta funzionando?

Non stiamo campendo davvero la **struttura del problema**

La comprensione della struttura del problema ci porterà a sviluppare un **nuovo approccio**

**Cerchiamo un nuovo approccio**

**Passaggio critico** : Ragionare sulla struttura/proprietà della soluzione (ottima) del problema
- In termini di soluzioni (ottime) di sottoproblemi più "piccoli"
- Non davvero diverso da come si ragiona implicitamente quando si usa la tecnica del divide-et-impera

**Obiettivo** : esprimere la **soluzione del problema** come combinazione di **soluzioni di (opportuni) sottoproblemi**. Se le combinazioni sono "poche" possiamo cercare la combinazione giusta per forza bruta

### Ragionando sulla struttura della soluzione

Sia $S^\star$ la soluzione ottima, ovvero l'$II$ di peso massimo di $G$. Consideriamo l'ultimo nodo $v_n$ di $G$

>[!info]- Osservazione
>Dell'ultimo nodo di $G$ possiamo dire due cose :
>- $v_n\not\in S^\star$
>- $v_n\in S^\star$

Vediamo il primo caso $v_n\not\in S^\star$

- Consideriamo $G'=G-\{v_n\}$
- Allora $S^\star$ è una soluzione ottima per $G'$
- Se esistesse una soluzione $S$ migliore per $G'$, $S$ sarebbe migliore anche per $G$ : assurdo!

![[Pasted image 20240325100502.png|center|500]]

Vediamo ora il caso 2 : $v_n\in S^\star$

- Consideriamo $G''=G-\{v_{n-1},v_n\}$
- Allora $\frac{S^\star}{v_n}$ è una soluzione ottima per $G''$
- Se esistesse una soluzione $S$ migliore per $G''$, $S\cup\{v_n\}$ sarebbe soluzione migliore di $S^\star$ per $G$ : assurdo!

![[Pasted image 20240325100739.png|center|500]]

### Verso l'algoritmo

**Proprietà** : L'$II$ di peso massimo per $G$ deve essere o :
- l'$II$ di peso massimo per $G'$
- $v_n$ unito all'$II$ di peso massimo per $G''$

**Idea (folle)** : Calcolare tutte e due le soluzioni e ritornare la migliore delle due

Qual'è il tempo dell'algoritmo se calcolo le due soluzioni **ricorsivamente**?

Il tempo speso dall'algoritmo è $$T(n)=T(n-1)+T(n-2)+O(1)\implies T(n)=\Theta(\phi^n)$$
Il tempo è quello di fibonacci2

Effettivamente era un'idea abbastanza folle, assomigliava molto alla brute force

**Domanda fondamentale** : quanti problemi distinti sono risolti dall'algoritmo ricorsivo? $\Theta(n)$

C'è un sottoproblema per ogni prefisso di $G$

**Idea** : procediamo iterativamente considerando prefissi di $G$ dai più piccoli verso i più grandi

## Algoritmo di Programmazione Dinamica

- $G_j$ : sottocammino composto dai primi $j$ vertici di $G$
- Sottoproblema $j$ : Calcolare il peso del miglior $II$ per $G_j$
- $OPT[j]$ : Valore della soluzione del sottoproblema $j$, ovvero peso dell'$II$ di peso massimo in $G_j$

$$\begin{align}&OPT[1]=w_1;OPT[2]=\max\{w_1,w_2\}\\&OPT[j]=\max\{OPT[j-1],w_i+OPT[j-2]\}\end{align}$$

![[Pasted image 20240325101518.png|center|500]]

L'algoritmo è il seguente

```pseudo
\begin{algorithm}
    \caption{Algoritmo Dynamic Programming}
    \begin{algorithmic}
      \Procedure{Algoritmo}{$OPT, w_1, w_2, n$}
        \State $OPT[1] \gets w_1$
        \State $OPT[2] \gets \max\{w_1,w_2\}$
        \For{$j \gets 3$ \To $n$}
          \State $OPT[j]=\max\{OPT[j-1],w_j+OPT[j-2]\}$
        \EndFor
	    \State return $OPT[n]$
      \EndProcedure
      \end{algorithmic}
    \end{algorithm}
```

Il tempo di esecuzione è $T(n) = \Theta(n)$

>[!info]- Osservazione
>L'algoritmo calcola il valore della soluzione ottima, ma non la soluzione effettiva del problema

### Ricostruzione della soluzione (in tempo lineare)

**Idea semplice** : Mentre calcoliamo i valori $OPT[j]$ possiamo mantenere esplicitamente anche la soluzione
- Corretta ma non ideale : spreco di tempo e spazio

**Idea migliore** : Ricostruire la soluzione solo alla fine sfruttando il vettore $OPT[]$

>[!warning]- Proprietà chiave
>$v_j\in II$ di peso massimo per $G_j\iff w_j+OPT[j-2]\geq OPT[j-1]$

L'algoritmo che ricostruisce la soluzione è il seguente

```pseudo
\begin{algorithm}
    \caption{Algoritmo di Ricostruzione}
    \begin{algorithmic}
      \Procedure{Ricostruzione}{$OPT, S^\star, n$}
        \State $S^\star \gets \emptyset$
        \State $j \gets n$
        \While{$j \geq 3$}
		    \If{$OPT[j-1]\geq w_j+OPT[j-2]$}
			    \State $j=j-1$
			    \Else
				    \State $S^\star=S^\star\cup\{v_j\}$
				    \State $j=j-2$
	        \EndIf
          \State $OPT[j]=\max\{OPT[j-1],w_j+OPT[j-2]\}$
        \EndWhile
	    \If{$j=2\land w_2\gt w_1$}
		    \State $S^\star=S^\star\cup\{v_2\}$
		    \Else
			    \State $S^\star=S^\star\cup\{v_1\}$
        \EndIf
	    \State return $S^\star$
      \EndProcedure
      \end{algorithmic}
    \end{algorithm}
```
La complessità temporale è $T(n)=\Theta(n)$

## Programmazione Dinamica : Principi generali

1) Identificare un numero piccolo di sottoproblemi
	1) **es : calcolare l'II di peso massimo per $G_j$**
2) Descrivere la soluzione di un generico sottoproblema in funzione delle soluzioni di sottoproblemi più "piccoli"
	1) **es** : $OPT[j]=\max\{OPT[j-1],w_i+OPT[j-2]\}$
3) Le soluzioni dei sottoproblemi sono memorizzate in una tabella
4) Avanzare opportunamente sulla tabella, calcolando la soluzione del sottoproblema corrente in funzione delle soluzioni di sottoproblemi già risolti

### Proprietà dei sottoproblemi

1) Essere pochi
2) Risolti tutti i sottoproblemi si può calcolare velocemente la soluzione al problema generale
	1) **Spesso la soluzione cercata è semplicemente quella del sottoproblema più grande**
3) Ci devono essere sottoproblemi "piccoli"
	1) **casi base**
4) Ci deve essere un ordine in cui risolvere i sottoproblemi
	1) **e quindi un modo di avanzare nella tabella e riempirla**

### Ruolo dei sottoproblemi

La chiave di tutto è la definizione dei "**giusti**" sottoproblemi

La definizione dei "**giusti**" sottoproblemi è un **punto di arrivo**

Solo una volta definiti i sottoproblemi si può verificare che l'algoritmo è **corretto**

Se la definizione dei sottoproblemi è un punto di arrivo, come ci arrivo?
- **Ragionando sulla struttura della soluzione (ottima) cercata**

La struttura della soluzione può suggerire i sottoproblemi e l'ordine in cui considerarli