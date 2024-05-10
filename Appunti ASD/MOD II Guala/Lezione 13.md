```table-of-contents
title: 
style: nestedList # TOC style (nestedList|inlineFirstLevel)
minLevel: 0 # Include headings from the specified level
maxLevel: 0 # Include headings up to the specified level
includeLinks: true # Make headings clickable
debugInConsole: false # Print debug info in Obsidian console
```
# Intrattabilità I
## Pattern e Antipattern nella progettazione di Algoritmi

Alcuni pattern di progettazione sono :
- Greedy
- Divide et impera
- Programmazione dinamica
- Dualità
- **Riduzioni**
- etc...

Mentre gli anti-pattern sono :
- **NP-Completezza** : Algoritmi con tempo $O(n^k)$ sono altamente improbabili
- PSPACE-Completezza : Algoritmo per la certificazione della soluzione in tempo $O(n^k)$ altamente improbabile
- Indecibilità : Nessun algoritmo possibile

## Classificare i problemi in base ai requisiti computazionali

**D** : Quali problemi siamo in grado di risolvere?

**R** : Quelli che hanno un'algoritmo polinomiale

**Teoria** : La definizione è ampia e solida
**Pratica** : Gli algoritmo polinomiali sono adatti a problemi enormi

![[Pasted image 20240510110811.png|center|500]]
### Classificare i problemi

**Desiderata**. Classificare i problemi in base a quelli che possono essere risolti in tempo polinomiale e a quelli che non possono essere risolti.

Esempi che richiedono tempo esponenziale.
- Dato un programma di dimensione costante, si arresta al massimo in k passi?
- Data una posizione di tavola in una generalizzazione n per n della dama, il nero può garantire una vittoria?

## Riduzioni polinomiali

**Osservazione** : Supponiamo di poter risolvere il problema $Y$ in tempo polinomiale. Che altro possiamo risolvere in tempo polinomiale?

>[!definition]- Riduzioni
>Un problema $X$ si **riduce polinomialmente (Cook)** ad un problema $Y$ se istanze arbitrarie di $X$ possono essere risolte usando :
>- Un numero polinomiale di passaggi computazionali standard, più
>- Un numero polinomiale di chiamate all'**Oracolo** che risolve il problema $Y$

>[!info]- Osservazione
>L'oracolo è un **modello computazionale** creato con speciali pezzi hardware che risolve le istanze di $Y$ in tempo costante (Prettamente teorico)

![[Pasted image 20240510111523.png|center|500]]

Per le riduzioni polinomiali si usa la **notazione** $$X\leq_pY$$
Occhio a non fare l'errore di confondere $X\leq_pY$ con $Y\leq_pX$

- **Progettazione di algoritmi** : Se $X\leq_pY$ e $Y$ si può risolvere in tempo polinomiale, allora anche $X$ si può risolvere in tempo polinomiale
- **Stabilire l'intrattabilità** : Se $X\leq_pY$ e $X$ non può essere risolto in tempo polinomiale, allora neanche $Y$ si potrà risolvere in tempo polinomiale
- **Stabilire l'equivalenza** : Se sia $X\leq_p Y$ che $Y\leq_p X$, si usa la notazione $X\equiv_p Y$. In questo caso, $X$ può essere risolto in tempo polinomiale $\iff$ $Y$ può esserlo

## Problemi di covering e packing

Diamo ora la definizione di un paio di problemi fondamentali nella teoria della complessità.

Dimostreremo anche che questi problemi sono **NP-Completi** mediante riduzione dal problema **SAT**

### Indipendent Set

>[!definition]- Definizione
>Dato un grafo $G=(V,E)$ e un itero $k$, esiste un sottoinsieme di $k$ (o più) vertici tale che due vertici non sono adiacenti?

**Esempio** : Esiste un'indipendet set di dimensione $\geq6$?
**Esempio** : Esiste un'indipendet set di dimensione $\geq7$?

![[Pasted image 20240510151046.png|center|500]]

### Vertex Cover

>[!definition]- Definizione
>Dato un grafo $G=(V,E)$ e un itero $k$, esiste un sottoinsieme di $k$ (o meno) vertici tale che ogni arco è incidente ad almeno un vertice nel sottoinsieme?

**Esempio** : Esiste un vertex cover di dimensione $\leq4$?
**Esempio** : Esiste un vertex cover di dimensione $\leq3$?

![[Pasted image 20240510151242.png|center|500]]

### Vertex Cover e Indipendent Set si riducono l'uno all'altro

>[!definition]- Teorema
>Indipendent Set $\equiv_p$ Vertex Cover

**Dimostrazione** : Dimostriamo che $S$ è un Indipendent Set di dimensione $k\iff V-S$ è un Vertex Cover di dimensione $n-k$

