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

## P vs NP

### Classe P

**Problemi Decisionali**
- Problema $X$ è un insieme di stringhe
- Istanza $s$ è una stringa
- Algoritmo $A$ risolve $X$ $$A(s)=\begin{cases}\text{si}&s\in X\\\text{no}&s\not\in X\end{cases}$$
**Definizione** : L'algoritmo $A$ viene eseguito in **tempo polinomiale** se per ogni stringa $s,A(s)$ termina in $\leq p(\vert \underbracket{s}_{\text{lunghezza di s}}\vert)$ "passi", dove $p(.)$ è una qualche funzione polinomiale

>[!definition]- Classe $P$
>La classe $P=$ insieme dei problemi decisionali per i quali esiste un algoritmo polinomiale (**Su una macchina di Turin deterministica**)

**Esempio**

![[Pasted image 20240515112705.png|center|500]]

#### Alcuni problemi in P

![[Pasted image 20240515112749.png|center|500]]

### La classe NP

>[!definition]- Certificato
>L'algoritmo $C(s,t)$ è un **certificato** per il problema $X\iff$ per ogni stringa $s:s\in X\iff$ esiste una stringa $t$ tale che $C(s,t)=si$

>[!definition]- Classe $NP$
>Classe $NP=$ insieme dei problemi decisionali per i quali esiste un certificatore polinomiale
>- $C(s,t)$ è un algoritmo polinomiale
>- Certificato $t$ di dimensione polinomiale : $\vert t\vert\leq p(\vert s \vert)$ per un quale polinomio $p(.)$

**Esempio**

![[Pasted image 20240515113613.png|center|500]]
