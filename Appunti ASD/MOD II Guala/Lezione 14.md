```table-of-contents
title: 
style: nestedList # TOC style (nestedList|inlineFirstLevel)
minLevel: 0 # Include headings from the specified level
maxLevel: 0 # Include headings up to the specified level
includeLinks: true # Make headings clickable
debugInConsole: false # Print debug info in Obsidian console
```
# Intrattabilità II

**Piccolo recap**

![[Pasted image 20240515111420.png|center|500]]

# P vs NP

## Classe P

**Problemi Decisionali**
- Problema $X$ è un insieme di stringhe
- Istanza $s$ è una stringa
- Algoritmo $A$ risolve $X$ $$A(s)=\begin{cases}\text{si}&s\in X\\\text{no}&s\not\in X\end{cases}$$
**Definizione** : L'algoritmo $A$ viene eseguito in **tempo polinomiale** se per ogni stringa $s,A(s)$ termina in $\leq p(\vert \underbracket{s}_{\text{lunghezza di s}}\vert)$ "passi", dove $p(.)$ è una qualche funzione polinomiale

>[!definition]- Classe $P$
>La classe $P=$ insieme dei problemi decisionali per i quali esiste un algoritmo polinomiale (**Su una macchina di Turin deterministica**)

**Esempio**

![[Pasted image 20240515112705.png|center|500]]

### Alcuni problemi in P

![[Pasted image 20240515112749.png|center|500]]

## La classe NP

>[!definition]- Certificato
>L'algoritmo $C(s,t)$ è un **certificato** per il problema $X\iff$ per ogni stringa $s:s\in X\iff$ esiste una stringa $t$ tale che $C(s,t)=si$

>[!definition]- Classe $NP$
>Classe $NP=$ insieme dei problemi decisionali per i quali esiste un certificatore polinomiale
>- $C(s,t)$ è un algoritmo polinomiale
>- Certificato $t$ di dimensione polinomiale : $\vert t\vert\leq p(\vert s \vert)$ per un quale polinomio $p(.)$

**Esempio**

![[Pasted image 20240515113613.png|center|500]]

### Certificati e Certificatori : Soddisfacibilità

**SAT** : Data una formula $\Phi$ in CNF, esiste un assegnamento di verità?
**3-SAT** : SAT con le clausole che hanno esattamente 3 letterali

**Certificato** : Un' assegnazione di verità alle variabili booleane

**Certificatore** : Controlla che ogni clausola in $\Phi$ ha almeno un letterale vero

![[Pasted image 20240515113932.png|center|500]]

In conclusione : $SAT\in NP$ , $3-SAT\in NP$

### Certificati e Certificatori : Percorso Hamiltoniano

>[!definition]- Percorso Hamiltoniamo
>Dato un grafo non diretto $G=(V,E)$, esiste un percorso semplice $P$ che visita tutti i nodi?

**Certificato** : Una permutazione $\pi$ degli $n$ nodi

**Certificatore** : Controlla che $\pi$ contiene ogni nodo di $V$ esattamente una volta, e che $G$ contiene un arco tra ogni coppia di nodi adiacenti

![[Pasted image 20240515114321.png|center|500]]

In conclusione : $HP\in NP$

### Alcuni problemi in NP

![[Pasted image 20240515114510.png|center|500]]

## P, NP e EXP

- $P=$ insieme dei problemi decisionali per i quali esiste un algoritmo **polinomiale**
- $NP=$ insieme dei problemi decisionali per i quali esiste un **certificatore polinomiale**
- $EXP=$ Insieme dei problemi decisionali per i quali esiste un algoritmo **esponenziale**

**Proposizione** : $P\subseteq NP$

**Dimostrazione** : Considera un qualunque problema $X\in P$
- Per definizione, esiste un algoritmo polinomiale $A(s)$ che risolve $X$
- Certificato $t=\epsilon$, certificatore $C(s,t)=A(s)$

**Proposizione** : $NP\subseteq EXP$

**Dimostrazione** : Considera un qualunque problema $X\in NP$
- Per definizione, esiste un certificatore polinomiale $C(s,t)$ per $X$, dove il certificato $t$ soddisfa $\vert t\vert\leq p(\vert s \vert)$ per un qualche polinomio $p(.)$
- Per risolvere l'istanza $s$, esegui $C(s,t)$ su tutte le stringhe $t$, con $\vert t\vert\leq p(\vert s \vert)$
- Ritorna `si` $\iff C(s,t)$ ritorna `si` per ognuno di questi potenziali certificati

**Fatto** : $P\neq EXP\implies$ o $P\neq NP$, o $NP\neq EXP$, o entrambi

# La questione principale : P vs NP

**D** : Come si risolve un'istanza di 3-SAT con $n$ variabili?
**R** : Ricerca esaustiva : provare tutti i $2^n$ assegnamenti di verità

**D** : Possiamo fare qualcosa di sostanzialmente più intelligente?

**Congettura** : Non esiste un **algoritmo polinomiale** per 3-SAT

![[Pasted image 20240515121725.png|center|300]]

Vale che $P=NP?$ `[Cook 1971, Edmonds, Levin, Yablonski, Godel]`
Il problema decisionale è facile quanto il problema della certificazione?

![[Pasted image 20240515121937.png|center|500]]

**Se la risposta è si...** Esiste un algoritmo efficiente per 3-SAT, TSP, VertexCover,$\dots$
**Se la risposta è no...** Non esitono algoritmi possibili per 3-SAT, TSP, VertexCover,$\dots$

# NP-Completezza

## Trasformazioni polinomiali

>[!definition]- Riduzioni di Cook
>Il problema $X$ si **riduce polinomialmente (Cook)** al problema $Y$ se arbitrarie istanze del problema $X$ possono essere risolte utilizzando:
>- Numero polinomiale di passi computazionali standard, più
>- Numero polinomiale di chiamate all'**oracolo** che risolve il problema $Y$.

>[!definition]- Riduzioni di Karp
>Il problema $X$ **si trasforma polinomialmente (Karp)** in un problema $Y$ se, data una qualsiasi istanza $x\in X$, si può costruire un'istanza $y\in Y$ tale che $x$ è un'istanza *si* di $X\iff y$ è un'istanza *si* di $Y$

**Nota** :
La trasformazione polinomiale è una riduzione polinomiale con una sola chiamata all'oracolo per Y, esattamente alla fine dell'algoritmo per X. Quasi tutte le riduzioni precedenti erano di questa forma

## NP-Completo

>[!definition]- NP-Completezza
>Un problema $Y\in NP$ si dice NP-Completo se per ogni altro problema $X\in NP$, si ha che $X\leq_pY$

**Proposizione** : Supponiamo che $Y\in NPC$. Allora $Y\in P\iff P=NP$

**Dim** $\impliedby$ Se $P=NP$, allora $Y\in P$ perchè $Y\in NP$
**Dim** $\implies$ Supponiamo $Y\in P$
- Considera ogni altro problema $X\in NP$ Dato che $X\leq_pY$, abbiamo che $X\in P$
- Questo implica che $NP\subseteq P$
- Ma noi già sappiamo che $P\subseteq NP$.
- Quindi $P=NP$

### Il "primo" problema NP-Completo

>[!definition]- Teorema di Cook-Levin
>SAT è NP-Completo

## Implicazioni di Karp

![[Pasted image 20240518151204.png|center|500]]

## Implicazioni di Cook-Levin

![[Pasted image 20240518151232.png|center|500]]

## Implicazioni di Karp+Cook-Levin

![[Pasted image 20240518151255.png|center|500]]

