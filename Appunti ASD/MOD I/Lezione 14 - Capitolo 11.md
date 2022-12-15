
# Strutture dati per rappresentare grafi

## Grafi non diretti

Quanto spazio?
![[appunti asd/mod i/immagini/Pasted image 20221215111018.png|center]]

**Matrice di adiacenza**: $O(n^2)$
![[appunti asd/mod i/immagini/Pasted image 20221215111110.png|center|300]]

**Liste di adiacenza**: $O(m+n)$
![[appunti asd/mod i/immagini/Pasted image 20221215111147.png|center|300]]

| **Operazione**              | Matrice di a. | Liste di a.                     |
| --------------------------- | ------------- | ------------------------------- |
| elenco archi incidenti in v | $O(n)$        | $O(\delta(v))$                  |
| c'è un arco (u,v)?          | $O(1)$        | $O(min\{\delta(u),\delta(v)\})$ |


## Grafi diretti

Quanto spazio?

![[appunti asd/mod i/immagini/Pasted image 20221215111613.png|center]]

**Matrice di adiacenza**: $O(n^2)$
![[appunti asd/mod i/immagini/Pasted image 20221215111658.png|center|300]]

**Liste di adiacenza**: $O(m+n)$
![[appunti asd/mod i/immagini/Pasted image 20221215111753.png|center|300]]


| **Operazione**            | Matrice di a. | Liste di a.    |
| ------------------------- | ------------- | -------------- |
| elenco archi uscenti da v | $O(n)$        | $O(\delta(v))$ |
| c'è arco (u,v)?           | $O(1)$        | $O(\delta(u))$ |

## Quali parti del grafo sono raggiungibili da un certo nodo?

... eseguo una **visita** del grafo

### Scopo e tipi di visita

Una visita di un grafo G permette di esaminare i nodi e gli archi di G **in modo sistematico** (se G è connesso)
Genera un **albero** di visita
Problema di base di molte applicazioni
Esistono vari tipi di visite con diverse proprietà:

- **visita in ampiezza (BFS=breadth first search)**
- **visita in profondità (DFS=depth first search)**

#### Visita in ampiezza

Dato un grafo G (non pesato) e un nodo s, trova tutte le **distanze/cammini minimi** da s verso ogni altro nodo v

**Applicazioni**:
- **web crawling**
	- come google trova nuove pagine da indicizzare
- **social networking**
	- trovare gli amici che potresti conoscere
- **network broadcast**
	- un nodo manda un messaggio a tutti gli altri nodi della rete
- **garbage collection**
	- come scoprire memoria non puù raggiungibile che si può liberare
- **model checking**
	- verificare una proprietà di un sistema
- **risolvere puzzle**
	- risolvere il Cubo di Rubick con un numero minimo di mosse

**Esempio**

Cubo di Rubick 2x2x2

- grafo delle configurazioni:
	- un vertice per ogni possibile stato del cubo
	- un arco fra due configurazioni se l'una è ottenibile dall'altra tramite una mossa

![[appunti asd/mod i/immagini/Pasted image 20221215112709.png|center|400]]





