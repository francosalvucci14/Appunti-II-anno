```table-of-contents
title: 
style: nestedList # TOC style (nestedList|inlineFirstLevel)
minLevel: 0 # Include headings from the specified level
maxLevel: 0 # Include headings up to the specified level
includeLinks: true # Make headings clickable
debugInConsole: false # Print debug info in Obsidian console
```
# Algoritmi di Approssimazione I

## Affrontare la NP-Completezza

**D** : Supponiamo di dover risolvere un problema di ottimizzazione $NPC$. Cosa dovrei fare?

**R** : Sacrificare una di queste funzioni desiderate
- Viene eseguito in tempo polinomiale
- Risolvere istanze arbitrarie del problema
- Trovare una soluzione ottimale al problema (**Sacrifichiamo questo**)

Algoritmo $\rho-$approssimante :
- Eseguito in tempo polinomiale
- Risolvere istanze arbitrarie del problema
- Trovare una soluzione che si trova entro il rapporto $\rho$ dell'ottimo

**Challenge** :
Abbiamo la necessità di dimostrare che il valore di una soluzione è vicino all'ottimo, senza sapere quale sia il valore ottimale

>[!definition]- Algoritmo $\alpha-$approsimante
>Un algoritmo $\alpha-$approssimante per un problema di ottimizzazione è un algoritmo polinomiale che per tutte le istanze del problema, produce una soluzione il cui valore entra nel rapporto $\alpha$ del valore della soluzione ottima

$\alpha$ : Viene chiamato **rapporto di approssimazione** o **fattore di approssimazione**

**Problema di minimizzazione** :
- $\alpha\geq1$
- Per ogni soluzione $x,cost(x)\leq\alpha OPT(x)$

**Problema di massimizzazione** :
- $\alpha\leq1$
- Per ogni soluzione $x,valore(x)\geq\alpha OPT(x)$

## Problema del Load Balancing

**Input** : $m$ macchine identiche; $n\geq m$ jobs; il job $j$ ha tempo di processamento pari a $t_j$
- Il job $j$ deve essere eseguito in modo continuo su una macchina
- Una macchina può processare al più un job alla volta

>[!definition]- Carico della macchina
>Sia $S[i]$ un sottoinsieme dei job assegnati alla macchina $i$.
>Il **carico** della macchina $i$ è $L[i]=\sum\limits_{j\in S[i]}t_j$

>[!definition]- Makespan
>Il **makespan** è il massimo carico di ogni macchina $L=\max_i\{L[i]\}$

Quindi, il problema del **Load Balancing** è quello di assegnare ogni job a una macchina per minimizzare il makespan

![[Pasted image 20240523113718.png|center|500]]

### Load Balancing su due macchine è NP-Hard

**Claim** : Load Balancing è hard anche se abbiamo $m=2$ macchine
**Dim** : $PARTITION\leq_pLOAD-BALANCE$

![[Pasted image 20240523113839.png|center|500]]

### Load Balancing : List Scheduling

**Algoritmo list-scheduling**
- Consideriamo $n$ job in un qualche ordine
- Assegnamo il job $j$ alla macchina $i$ il cui carico è finora il più basso

![[Pasted image 20240523114011.png|center|500]]

**Implementazione** : Tempo $O(n\log(n))$ usando una coda con priorità per i carichi $L[k]$

Vedi esempio qui -> [Esempio](https://www.mat.uniroma2.it/~guala/09_Apx_Algorithms_I_2023.pdf#page=9)

#### Load Balancing : Analisi del List Scheduling

>[!definition]- Teorema `[Graham 1966]`
>L'algoritmo greedy è 2-approssimante
>- Prima analisi del caso peggiore di un algoritmo di approssimazione.
>- È necessario confrontare la soluzione risultante con il makespan ottimale $L^\star$

**Lemma 1** : Per ogni $k$ : il makespan ottimo è $L^\star\geq t_k$
**Dim** : Una qualche macchina deve elaborare il lavoro più dispendioso in termini di tempo

**Lemma 2** : Il makespan ottimo è $L^\star\geq\frac{1}{m}\sum\limits_kt_k$
**Dim**
- Il tempo totale di processamento è $\sum\limits_kt_k$
- Una delle $m$ macchine deve fare almeno una frazione $\frac{1}{m}$ del lavoro totale

**Dimostrazione del teorema** : Consideriamo il carico $L[i]$ della macchina bottleneck $i$ (macchina che finisce con il carico più grande)
- Sia $j$ l'ultimo job schedulato per la macchina $i$
- Quando assegnamo il job $j$ alla macchina $i$, $i$ ha il carico più piccolo. Il suo carico prima dell'assegnamento è $L[i]-t_j$, quindi $L[i]-t_j\leq L[k],\forall 1\leq k\leq m$ ![[Pasted image 20240523114956.png|center|500]]
- Sommiamo le disuguaglianze su tutti i $k$ e divido per $m$ : $$\begin{align}L[i]-t_j&\leq\frac{1}{m}\sum\limits_kL[k]\\&=\frac{1}{m}\sum\limits_ktk\\&\underbracket{\leq}_{\text{Lemma 2}} L^\star\end{align}$$
- Ora, $L=L[i]=\underbrace{(L[i]-t_j)}_{\leq L^\star}+\underbrace{t_j}_{\leq L^\star}\leq 2L^\star$

> Quindi l'algoritmo ritorna circa **due volte il valore ottimo**

**D** : La nostra analisi è giusta?

**R** : Essenzialmente si

**Esempio** : $m$ macchine, i primi $m(m-1)$ job hanno lunghezza $1$, l'ultimo job ha lunghezza $m$

![[Pasted image 20240523115533.png|center|500]]

![[Pasted image 20240523115553.png|center|500]]

### Load Balancing : Regola LPT

**Longest Processing Time (LPT)** : Ordiniamo $n$ job in ordine decrescente in base al tempo di processamento; poi lanciamo l'algoritmo list-scheduling

![[Pasted image 20240523115753.png|center|500]]

#### Load Balancing : Analisi della Regola LPT

**Osservazione** : Se la macchina bottleneck $i$ ha un solo job, allora LPT è ottimale
**Dim** : Ogni soluzione deve schedulare quel job

**Lemma 3** : Se ci sono più di $m$ job, $L^\star\geq2t_{m+1}$
**Dim** :
- Consideriamo i tempi di processamento dei primi $m+1$ jobs $t_1\geq t_2\geq\dots\geq t_{m+1}$
- Ognuno richiede tempo almeno $t_{m+1}$
- Ci sono $m+1$ job e $m$ macchine, per il principio della piccionaia. almeno una macchina deve ottenere due job

>[!definition]- Teorema
>La regola LPT è un algoritmo $\frac{3}{2}-$approssimante

**Dimostrazione (simile al list-scheduling)**
- Consideriamo il carico $L[i]$ della macchina bottleneck $i$
- Sia $j$ l'ultimo job schedulato sulla macchina $i$ (assumendo che la macchina $i$ ha almeno 2 job, abbiamo che $j\geq m+1$) $$L=L[i]=\underbrace{(L[i]-t_j)}_{\leq L^\star}+\underbrace{t_j}_{\leq \frac{1}{2}L^\star}\leq \frac{3}{2}L^\star$$
**D** : La nostra analisi è corretta?
**R** : No

>[!definition]- Teorema `[Graham 1969]`
>La regola LPT è $\frac{4}{3}-$approssimante

**Dim** Analisi più sofisticata dello stesso algoritmo

---

# Algoritmi di Approssimazione II

## Problema k-Center

**Input** : Insieme di $n$ siti $s_1,\dots,s_n$ e un intero $k\gt0$

**Problema Center Selection** : Selezionare $k$ centri $C$ tale che la distanza massima da un sito al centro più vicino è minimizzata

![[Pasted image 20240523121858.png|center|500]]

![[Pasted image 20240523121919.png|center|500]]

**Variante del problema** : I centri devono essere in uno dei siti

![[Pasted image 20240523122131.png|center|500]]

**Notazione** :
- $dist(x,y)$ = distanza tra $x$ e $y$
- $dist(s_i,C)=\min_{c\in C}dist(s_i,c)$ = distanza da $s_i$ al centro più vicino
- $r(C)=\max_idist(s_i,C)$ = raggio di copertura minimo

**Goal** : Trovare un insieme di centri $C$ che minimizza $r(C)$, soggetto a $\vert C\vert=k$

**Proprietà della funzione distanza**
- $dist(x,x)=0$ `(identità)`
- $dist(x,y)=dist(y,x)$ `(simmetria)`
- $dist(x,y)\leq dist(x,z)+dist(z,y)$ `(disuguaglianza triangolare)`

**Esempio** : Ogni sito è un vertice in un grafo pesato non diretto, un sito può essere un nodo, $dist(x,y)$ = distanza (pesata) in $G$ tra $x$ e $y$

![[Pasted image 20240523122651.png|center|500]]

### Algoritmo Greedy

**Algoritmo** : Scegliere ripetutamente il centro successivo come sito **più lontano** da qualsiasi centro esistente

![[Pasted image 20240523122759.png|center|500]]

**Osservazione** : Al termine, tutti i centri in $C$ sono a coppie almeno $r(C)$ distanti tra loro.

Vedi esempio qui -> [Esempio](https://www.mat.uniroma2.it/~guala/09_Apx_Algorithms_II_2023.pdf#page=20)

#### Analisi dell'algoritmo greedy

>[!definition]- Teorema
>Sia $C^\star$ un insieme ottimale di centri.
>Allora $r(C)\leq2r(C^\star)$

**Dimostrazione (per assurdo)** Assumiamo che $r(C^\star)\lt\frac{1}{2}r(C)$
- Per ogni sito $c_i\in C$, consideriamo una sfera di raggio $\frac{1}{2}r(C)$
- Esattamente un $c_i^\star$ in ogni sfera
	- Ogni sfera con centro $c_i\in C$ deve contenere un centro in $C^\star$
	- Le sfere sono disgiunte e $\vert C\vert=\vert C^\star\vert$ ![[Pasted image 20240523123538.png|center|500]]
	- Sia $c_i$ il sito abbinato con $c_i^\star$
- Consideriamo un qualunque sito $s$ e il cuo centro più vicino $c_i^\star\in C^\star$
- $$dist(s,C)\leq dist(s,c_i)\underbrace{\leq}_{\Delta-\text{disuguaglianza}}\underbrace{dist(s,c_i^\star)+dist(c_i^\star,c_i)}_{\leq r(C^\star)\text{ dato che il centro più vicino è }c_i^\star}\leq2r(C^\star)$$
- Quindi $r(C)\leq2r(C^\star)$

>[!definition]- Teorema
>L'algoritmo greedy è $2-$approssimante per questo problema

**Remark** : L'algoritmo greedy posizione sempre i centri nei siti, ma lo fa con un fattore di $2$ rispetto alla soluzione ottima, che permette di posizionare i centri ovunque

**D** : C'è speranza di ottenere una approssimazione migliore? ..Molto improbabile

>[!definition]- Teorema
>A meno che $P=NP$, non esiste un algoritmo $\rho-$approssimante per questo problema per ogni $\rho\lt2$

