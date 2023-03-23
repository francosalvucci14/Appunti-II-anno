
# Union di costo lineare

**find e makeSet** richiedono solo tempo $O(1)$, ma particolari sequenze di union possono essere molto inefficienti

![[appunti asd/mod ii/immagini/Pasted image 20230323142952.png|center|350]]

Se eseguiamo n makeSet, n-1 union come sopra, e m find (in qualsiasi ordine), il **tempo** richiesto **dall'intera sequenza** di operazioni è $O(n+1+2+\dots+(n-1)+m)=O(m+n^2)$ 

# Migliorare la struttura QuickFind : euristiche di bilanciamento nell'operazione union

**Idea** : fare in modo che un nodo/elemento non cambi troppo spesso padre

## Bilanciamento in alberi QuickFind

Nell'unione degli insiemi A e B, attacchiamo gli elementi dell'insieme **di cardinalità minore a quello di cardinalità maggiore**, e se necessario modifichiamo la radice dell'albero ottenuto (cosidetta **union by size**)

**Esempio**

![[appunti asd/mod ii/immagini/Pasted image 20230322154057.png|center|500]]

Dopo l'esecuzione di union(2,3)

![[appunti asd/mod ii/immagini/Pasted image 20230322154144.png|center|500]]

![[appunti asd/mod ii/immagini/Pasted image 20230322154231.png|center|500]]

Esecuzione di union(4,2):

![[appunti asd/mod ii/immagini/Pasted image 20230323143648.png|center|500]]

![[appunti asd/mod ii/immagini/Pasted image 20230323143743.png|center|500]]

### Realizzazione (1/3)

![[Pasted image 20230323143901.png|center|500]]

### Realizzazione (2/3)

![[Pasted image 20230323143926.png|center|500]]

### Realizzazione (3/3)

![[appunti asd/mod ii/immagini/Pasted image 20230323143957.png|center|500]]

$T_{am}$ = tempo per operazione ammortizzato sull'intera sequenza di unioni (vedremo che una singola union può costare $\Theta(n)$, ma l'intersa sequenza di n-1 costa $O(nlog(n))$ )

## Complessità di un'operazione di Union

![[appunti asd/mod ii/immagini/Pasted image 20230323144810.png|center|550]]

### Analisi ammortizzata (1/2)

Vogliamo dimostrare che se eseguiamo m find, n makeSet, e al più n-1 union, il tempo richiesto dall'intera sequenza di operazioni è $O(m+n\cdot\log(n))$ 

Idea della dimostrazione:
- è facile vedere che find e makeSet richiedono tempo $\Theta(m+n)$
- Per analizzare le operazioni di union, ci concentriamo su un singolo nodo e dimostriamo che il tempo speso per tale nodo è $O(\log{n})$, allora in totale, il tempo speso è $O(n\cdot\log{n})$ 

### Analisi ammortizzata (2/2)

Quando eseguiamo una union, per ogni nodo che cambia padre pagheremo tempo costante

Osserviamo ora che ogni nodo può cambiare al più $O(\log{n})$ padri, poichè ogni volta che un nodo cambia padre la cardinalità dell'insieme al quale apparterrà è **almeno doppia** rispetto a quella dell'insieme a cui apparteneva
- all'inizio un nodo è in un insieme di dimensione1
- poi se cambia padre in un insieme di dimensione almeno 2,
- all'i-esimo cambio è in un insieme di dimensione almeno $2^i$
Il tempo speso per un singolo nodo sull'itenra sequenza di n union è $O(\log{n})$
L'intera sequenza di operazioni costa
$$O(m+n+n\cdot\log{n})=O(m+n\cdot\log{n})$$
