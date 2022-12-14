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

![[appunti asd/mod i/immagini/Pasted image 20221214123400.png|center]]

![[appunti asd/mod i/immagini/Pasted image 20221214123443.png|center]]

