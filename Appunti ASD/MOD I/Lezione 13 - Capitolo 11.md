# Grafi e visite di grafi

## Teoria dei grafi, problemi su grafi

### Origini storiche

Nel 1736, il matematico Eulero, affrontò l'annoso problema dei 7 ponti di Königsberg (Prussia)
![[appunti asd/mod i/immagini/Pasted image 20221214122043.png|center|400]]

è possibile o meno fare una passeggiata che parta da un **qualsiasi** punto della città e percorra **una ed una** sola volta ciascuno dei 7 ponti?

Eulero affrontò il problema schematizzando **topologicamente** la pianta della città, epurando così l'istanza da insignificanti dettagli **topografici**:
![[appunti asd/mod i/immagini/Pasted image 20221214122334.png|center]]

... e così Königsberg venne rappresentata con un insieme di **4 punti** (uno per ciascuna zona della città), opportunamente uniti da **7 linee** (una per ciascun ponte)

### Definizione di grafo (non orientato)

Un **grafo G=(V,E)** consiste in:
- Un insieme **V** di **vertici** (o nodi)
- Un insieme **E** di coppie (non ordinate) di vertici, detti **archi**

**Esempio**

Grafo di Eulero associato alla città di Königsberg:
- $V=\{A,B,C,D\}$
- $E=\{(A,B),(A,B),(A,D),(B,C),(B,C),(B,D),(B,D),(C,D)\}$

![[appunti asd/mod i/immagini/Pasted image 20221214123110.png|center]]

**Nota**: è più propriamente detto **multigrafo**, in quanto contiene **archi paralleli**

![[appunti asd/mod i/immagini/Pasted image 20221214123400.png|center|600]]

![[appunti asd/mod i/immagini/Pasted image 20221214123443.png|center|600]]

### Definizione di grafo diretto

Un **grafo diretto D=(V,A)** consiste in:
- Un insieme **V** di **vertici** (o **nodi**)
- Un insieme **A** di coppie **ordinate** di vertici, detti **archi diretti**

![[appunti asd/mod i/immagini/Pasted image 20221214123706.png|center|600]]

![[appunti asd/mod i/immagini/Pasted image 20221214123758.png|center|600]]

### Terminologia

- **G=(V,E)** grafo non diretto
- **n** = |V| numero di vertici
- **m** = |E| numero di archi
- **u** ed **v** sono **adiacenti**
- **(u,v)** è **incidente** a **u** e a **v** (detti **estremi**)
- $\delta(u)$: **grado** di **u**: numero archi incidenti a **u**
- **grado** di **G** = $max_{v\in V}\{\delta(v)\}$

![[appunti asd/mod i/immagini/Pasted image 20221214124123.png|center]]

### Che relazione c'è fra grado dei nodi e numero di archi?

#### Una semplice proprietà (grafi non diretti)

Cosa ottengo se sommo i gradi di ogni nodo?

![[appunti asd/mod i/immagini/Pasted image 20221214124257.png|center|400]]

>[!important]- Formula
>$$\sum_{v\in V}\delta(v)=2m$$

In ogni grafo il numero di nodi di grado dispari è pari

#### Una semplice proprietà (grafi diretti)

**Domanda (sui grafi diretti)**
Cosa ottengo se sommo il grado **uscente/entrante** di tutti i nodi?

![[appunti asd/mod i/immagini/Pasted image 20221214124551.png|center|400]]

>[!important]- Formula
>$$\sum_{v\in V}\delta_{out}(v)=\sum_{v\in V}\delta_{in}(v)=m$$


### Altra Terminologia

- **_cammino_**: sequenza di nodi connessi da archi
- **_lunghezza_** di un cammino: numero di archi del cammino
- **_distanza_**: la lunghezza del più corto cammino tra due vertici si dice **_distanza_** tra due vertici

![[appunti asd/mod i/immagini/Pasted image 20221214124943.png|center]]

**Esempio**:
distanza fra L e A: 4 (il cammino in questione è L-I-E-B-A)

In un grafo **orientato**, il cammino deve rispettare il verso di orientamento degli archi

- G è **connesso** se esiste un cammino per ogni coppia di vertici
- **ciclo**: un cammino chiuso, ovvero un cammino da un vertice a se stesso
- **diametro**: massima distanza fra due nodi_
	- $max_{u.v\in V}dist(u,v)$
	- il diametro di un grafo non connesso è $\infty$

![[appunti asd/mod i/immagini/Pasted image 20221214125445.png|center]]

![[appunti asd/mod i/immagini/Pasted image 20221214125541.png|center|600]]

