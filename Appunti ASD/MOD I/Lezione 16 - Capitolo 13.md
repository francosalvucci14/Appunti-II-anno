
# Cammini minimi: Algoritmo di Dijkstra

## Cammini minimi in grafi: cammini a singola sorgente (senzi pesi negativi)

### Cammini minimi in grafi pesati

Sia G=(V,E,w) un grafo **orientato** o **non orientato** con pesi w **reali** sugli archi. Il **costo** o **lunghezza** di un cammino $\pi=<v_0,v_1,v_2,...,v_k>$ è:
$$w(\pi)=\sum_{i=1}^kw(v_{i-1},v_i)$$
Un **cammino minimo** tra una coppia di vertici x e y è un cammino avente **costo minore o uguale** a quello di ogni altro cammino tra gli stessi vertici

>[!info]- Nota
>Il cammino minimo non è necessariamente unico

Vedi esempio qua -> [Esempio1](http://www.mat.uniroma2.it/~guala/Dijkstra_2020.pdf#4)
Vedi esempio qua -> [Esempio2](http://www.mat.uniroma2.it/~guala/Dijkstra_2020.pdf#6)

![[appunti asd/mod i/immagini/Pasted image 20221222092644.png|center|600]]

$d_G(u,v)=17$

**Problema**: dati u e v, trovare un cammino minimo (e/o **distanza**) da u a v

**Problema**: trovare il cammino minimo fra due nodi
![[appunti asd/mod i/immagini/Pasted image 20221222092836.png|center|600]]

![[appunti asd/mod i/immagini/Pasted image 20221222092928.png|center|600]]


### Esiste sempre un cammino minimo fra due nodi?

**Risposta**: ...no!

- se non esiste nessun cammino da u a v:
	- $d(u,v)=\infty$
- se c'è un cammino che contiene un **ciclo** uil cui costo è negativo
	- $d(u,v)=-\infty$

![[appunti asd/mod i/immagini/Pasted image 20221222093143.png|center|400]]

>[!info]- Osservazione
>Se G non contiene cicli negativi, esistono cammini minimi che sono cammini **semplici**

#### Sottostruttura ottima

Ogni **sottocammino** di un cammino minimo è un cammino minimo

dim: tecinca **cut&paste**

![[appunti asd/mod i/immagini/Pasted image 20221222093353.png|center|550]]

#### Disuguaglianza triangolare

$\forall u,v,x\in V$, cale che:
$$d(u,v)\leq d(u,x)+d(x,v)$$

![[appunti asd/mod i/immagini/Pasted image 20221222093548.png|center|600]]

### Cammini minimi a singola sorgente

![[appunti asd/mod i/immagini/Pasted image 20221222093716.png|center|600]]

#### Problema del calcolo dei cammini minimi a singola sorgente

Due varianti:

- Dato $G=(V,E,w),s\in V$, calcola le distanze di tutti i nodi da s, ovvero, $d_G(s,v)$ per ogni $v\in V$
- Dato $G=(V,E,w),s\in V$, calcola l'**albero dei cammini minimi** di G radicato in s


##### Albero dei cammini minimi (Shortest Path Tree - SPT)

T è un albero dei cammini minimi con sorgente s di un grafo G=(V,E,w) se:
- T è un albero radicato in s
- per ogni $v\in V$, vale: $d_T(s,v)=d_G(s,v)$

![[appunti asd/mod i/immagini/Pasted image 20221222094108.png|center|200]]

Per grafi non pesati: SPT radicato in s = Albero BFS radicato in s

![[appunti asd/mod i/immagini/Pasted image 20221222094207.png|center|400]]
![[appunti asd/mod i/immagini/Pasted image 20221222094226.png|center|400]]

## Algoritmo di Dijkstra

>[!important]- Assunzione
>Tutti gli archi hanno peso non negativo, ovvero ogni arco (u,v) del grafo ha peso $w(u,v)\geq0$

### Idea intuitiva dell'algoritmo: pompare acqua nella sorgente

Archi come **tubi**
Peso degli archi come **lunghezza**
Acqua **scorre a velocità costante**

Vedi l'idea qua: [Alg.Dijkstra](http://www.mat.uniroma2.it/~guala/Dijkstra_2021.pdf#page=21) 

### Verso l'algoritmo: approccio greedy (goloso)

1. Mantiene per ogni nodo v una **stima** (per eccesso) $D_{sv}$ alla distanza $d(s,v)$. Inizialmente, unica stima finita $D_{ss}=0$
2. Mantiene un insieme X di nodi per cui le stime sono **esatte**; e anche un albero T dei cammini minimi verso nodi in X (albero nero). Inizialmente $X=\{s\}$, T non ha archi
3. Ad ogni passo aggiunge a X il nodo u in V-X la cui stima è minima; aggiung e a T uno specifico arco (arancione) entrante in u
4. Aggiorna le stime guardando i nodi adiacenti a u


![[appunti asd/mod i/immagini/Pasted image 20221222095537.png|center|400]]

I nodi da aggiungere progressivamente a X (e quindi a T) sono mantenuti in una **coda di priorità**, associati ad **un unico arco** (arco arancione) che li connette a T

La stima per un nodo $y\in V-X$ è: $D_{sy}=min\{D_{sx}+w(x,y):(x,y)\in E,x\in X\}$
L'arco che fornisce il minimo è l'arco arancione

Se y è in coda con arco (x,y) associato, e se dopo aver aggiunto u a T troviamo un arco (u,y) tale che $D_{su}+w(u,y)\lt D_{sx}+w(x,y)$, allora **rimpiazziamo** (x,y) con (u,y) ed aggiorniamo $D_{sv}$

![[appunti asd/mod i/immagini/Pasted image 20221222095955.png|center|400]]

### Pseudocodice

![[appunti asd/mod i/immagini/Pasted image 20221222100111.png|center|500]]

>[!info]- Nota
>$\hat T$ è un albero che contiene tutti i nodi in X **più** i nodi correntemente contenuti nella coda di priorità (nodi arancioni); è composto cioè dagli archi di T (albero dei cammini minimi ristretto ai nodi in X) più gli archi arancioni (potenziali archi da aggiungere a T)


