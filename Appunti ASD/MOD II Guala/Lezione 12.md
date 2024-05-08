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

>[!definition]- Definizione
>Due percorsi sono **disgiunti** se non hanno archi in comune

>[!definition]- Problema dei percorsi disgiunti
>Dato un grafo diretto $G=(V,E)$ e due nodi $s,t$, trova il massimo numero di percorsi disgiunti $s\to t$


**Esempio** : Le reti di comunicazione

![[Pasted image 20240508103731.png|center|500]]

![[Pasted image 20240508103752.png|center|500]]

### Formulazione max-flow

**Formulazione max-flow** : Assegnare una capacità di $1$ ad ogni arco

>[!definition]- Teorema
>C'è una corrispondenza $1-1$ tra i $k$ percorsi disgiunti $s\to t$ in $G$ e il valore $k$ del flusso in $G'$


**Dimostrazione** $\implies$
- Siano $P_1,\dots,P_k$ i $k$ percorsi disgiunti $s\to t$ in $G$
- Sia $$f(e)=\begin{cases}1&\text{arco e "partecipa" in qualche percorso }P_j\\0&\text{altrimenti}\end{cases}$$
- Dato che i percorsi sono disgiunti, $f$ è un flusso di valore $k$

![[Pasted image 20240508104219.png|center|500]]

**Dimostrazione** $\impliedby$
- Sia $f$ un flusso in $G'$ di valore $k$
- Consideriamo l'arco $(s,u)$ con $f(s,u)=1$
	- Per la conservazione del flusso, esiste un arco $(u,v)$ con $f(u,v)=1$
	- Continua finchè non raggiungi $t$, scegliendo sempre un nuovo arco
- Produce $k$ percorsi disgiunti (non necessariamente semplice) (si possono eliminare i cicli per ottenere percorsi semplici in tempo $O(mn)$ se si desidera)

![[Pasted image 20240508104219.png|center|500]]

**Corollario** : Si può risolvere il problema dei percorsi disgiunti usando la formulazione max-flow

**Dim** :
- Teorema di integralità $\implies$ Esiste un max-flow $f^\star$ in $G'$ che è intero
- Corrispondenza $1-1\implies f^\star$ corrisponde al massimo numero di percorsi disgiunti $s\to t$ in $G$
#### Tempo di esecuzione

Il tempo di esecuzione dell'algoritmo è il seguente
- Usando Ford-Fulkerson si hanno $\leq n$ aumenti $\implies$ tempo $O(mn)$
### Percorsi disgiunti su grafi non diretti

Il problema è identico al problema precedente, solo che il grafo in questione non è diretto

![[Pasted image 20240508105314.png|center|500]]

![[Pasted image 20240508105328.png|center|500]]

![[Pasted image 20240508105343.png|center|500]]

## Segmentazione dell'immagine

**Segmentazione dell'immagine** :
- Dividere l'immagine in regioni coerenti
- Problema centrale nel processing dell'immagine

**Esempio** : Separare l'umano e il robot dalla scena in background

![[Pasted image 20240508112900.png|center|500]]

**Segmentazione foreground/background**
- Un Label che dice se l'immagine appartiene al background o no
- $V=$ insieme di pixel, $E=$ coppie di pixel vicine
- $a_i\geq0$ è la probabilità che il pixel $i$ sia in foreground
- $b_i\geq0$ è la probabilità che il pixel $i$ sia in background
- $p_{ij}\geq0$ è la penalità di separazione per aver etichettato uno tra $i$ e $j$ come freground, e l'altro come backround

![[Pasted image 20240508113255.png|center|200]]

**Goal** :
- **Accuratezza** : se $a_i\gt b_i$, preferiamo etichettare $i$ come foreground
- **Smoothness** : se molti vicini di $i$ sono etichettati in primo piano, dovremmo essere propensi a etichettare $i$ come foreground
- Trovare una partizione $(\underbracket{A}_{\text{foreground}},\underbracket{B}_{\text{background}})$ che massimizza : $$\sum_{i\in A}a_i+\sum_{j\in B}b_j-\sum\limits_{(i,j)\in E\atop\vert A\cap\{i,j\}\vert=1}p_{ij}$$
SI può formulare come un problema di min-cut

Facciamolo diventare un **problema di minimizzazione**  :
- Massimizzare $\sum\limits_{i\in A}a_i+\sum\limits_{j\in B}b_j-\sum\limits_{(i,j)\in E\atop\vert A\cap\{i,j\}\vert=1}p_{ij}$
- È equivalente a minimizzare $$\underbracket{(\sum\limits_{i\in V}a_i+\sum\limits_{j\in V}b_j)}_{\text{una costante}}-\sum_{i\in A}a_i-\sum_{j\in B}b_j+\sum\limits_{(i,j)\in E\atop\vert A\cap\{i,j\}\vert=1}p_{ij}$$
Quindi, formulato come un problema di min-cut abbiamo :
- $G'=(V',E')$
- Per ogni pixel si crea un nodo
- Usiamo due archi antiparalleli al posto di un arco non diretto
- Aggiungiamo la sorgete $s$ che corrisponde al foreground
- Aggiungiamo il pozzo $t$ che corrisponde al background

Il grafo $G'$ sarà cosi fatto

![[Pasted image 20240508115145.png|center|200]]

![[Pasted image 20240508115202.png|center|500]]

Per essere precisi

**Consideriamo il min-cut** $(A,B)\in G'$
- $A=$ foreground
	- $$cap(A,B)=\sum\limits_{j\in B}a_j+\sum\limits_{i\in A}b_i-\sum\limits_{(i,j)\in E\atop i\in A, j\in B}p_{ij}$$
- Precisamente la quantità che vogliamo minimizzare



## Baseball Elimination