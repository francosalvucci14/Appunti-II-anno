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

