```table-of-contents
title: 
style: nestedList # TOC style (nestedList|inlineFirstLevel)
minLevel: 0 # Include headings from the specified level
maxLevel: 0 # Include headings up to the specified level
includeLinks: true # Make headings clickable
debugInConsole: false # Print debug info in Obsidian console
```
# Network Flow 2

**Applicazioni del max-flow e min-cut**

I problemi max-flow e min-cut sono applicabili in vari ambiti, tra cui :
- Data mining
- Open-pit mining
- Matching Bipartito
- Network connectivity
- Distribuited computing
- etc...

In questa lezione ne vedremo 4
## Matching Bipartito

Diamo la definizione di matching

>[!definition]- Matching
>Dato un grafo non diretto $G=(V,E)$, un **sottoinsieme** di archi $M\subseteq E$ è un **matching** se ogni nodo appare in al più un arco in $M$

**Max Matching** : Dato un grafo $G$, trovare il matching di cardinalità massima

![[Pasted image 20240430115001.png|center|500]]

Dopo aver dato la definizione di Matching, diamo ora la definizione di **Matching Bipartito**

>[!definition]- Grafo bipartito
>Un grafo $G$ si dice **bipartito** se i nodi possono essere partizionati in due sottoinsieme $L$ e $R$ tale che ogni arco connette un nodo di $L$ con uno di $R$

>[!definition]- Matching bipartito
>Dato un grafo bipartito $G=(L\cup R,E)$, trovare il matching di cardinalità massima

![[Pasted image 20240430115219.png|center|300]]

### Matching perfetto (in grafi bipartiti)

>[!definition]- Matching perfetto
>Dato un grafo $G=(V,E)$, un sottoinsieme di archi $M\subseteq E$ si dice **matching perfetto** se ogni nodo appare esattamente in un arco di $M$

Detto questo, il problema del Matching Perfetto è il seguente

**Problema del matching perfetto** : Dato un grafo bipartito $G=(L\cup R,E)$, trovare il matching perfetto, o se non esiste riportarlo correttamente

![[Pasted image 20240430115705.png|center|500]]

### Matching Bipartito : Formulazione max-flow

**Formulazione**
- Creare un grafo diretto (**ausilario**) $G'=(L\cup R\cup \{s,t\},E')$
- A tutti gli archi che vanno da $L$ a $R$ assegniamo capacità *infinito*
- A tutti gli archi da $s$ a $L$ assegniamo capacità $1$
- Stessa cosa per gli archi da $R$ a $t$

![[Pasted image 20240430120150.png|center|500]]

#### Dimostrazione di correttezza

>[!definition]- Teorema
>Esiste una corrispondenza $1-1$ tra i matching di cardinalità $k$ in $G$ e i flussi interi ($\forall e:f(e)\in\{0,1\}$) di valore $k$ in $G'$

**Dim** $\implies$
- Sia $M$ un matching in $G$ di cardinalità $k$
- Considera un flusso $f$ che manda $1$ unità ad ognuno dei $k$ percorsi corrispondenti
- $f$ è un flusso di valore $k$

![[Pasted image 20240430120603.png|center|500]]

**Dim** $\impliedby$
- Sia $f$ un flusso integrale in $G'$ di valore $k$
- Considera $M=$ insieme di archi da $L$ a $R$ con $f(e)=1$
	- Ogni nodo in $L$ e $R$ partecipa in appare in al più un arco in $M$
	- $|M|=k$ : Applichiamo il lemma sul valore del flusso, al taglio $(L\cup\{s\},R\cup\{t\})$

![[Pasted image 20240430120955.png|center|500]]

**Corollario** : SI può risolvere il problema del matching bipartito tramite la formulazione max-flow

**Dim**
- Dal teorema di integralità $\implies$ Esiste un max flow $f^\star$ in $G'$ che è intero
- Corrispondenza $1-1\implies f^\star$ corrispoinde al matching di cardinalità massima

![[Pasted image 20240430120955.png|center|500]]

#### Tempo di esecuzione

Se usiamo Ford-Fulkerson, abbiamo $\leq n$ aumenti $\implies$Tempo $O(mn)$
## Percorsi Disgiunti



## Segmentazione dell'immagine

## Baseball Elimination

