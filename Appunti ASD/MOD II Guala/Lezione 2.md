# Union-Find

## Il problema Union-Find

Mantenere una collezione di insiemi disgiunti contenenti elementi distinti, durante l'esecuzione di una sequenza di operazioni del tipo:
- `makeSet(x)` : crea il nuovo insieme $x=\{x\}$ di nome x
- `Union(A,B)` : unisce gli insiemi A e B in un unico insieme, di nome A, e distrugge i vecchi insiemi
- `Find(x)` : restituisce il nome dell'insieme che contiene l'elemento x

**Esempio**

![[Pasted image 20240312141349.png|center|400]]

D : se ho n elementi, quante union posso fare?
R : al più $n-1$

**Obiettivo** : Progettare una struttura dati che sia efficiente su una sequenza arbitraria di operazioni

**Idea Generale** : Rappresentare gli insiemi disgiunti con una foresta

Ogni insieme è un **albero radicato**

La **radice** contiene il nome dell'insieme

## Approcci Elementari

### QuickFind

Usiamo una **foresta di alberi di altezza 1** per rappresentare gli insiemi disgiunti.
In ogni albero :
- Radice = nome dell'insieme
- Foglie = Elementi (**incluso** l'elemento rappresentativo)

**Realizzazione**

![[Pasted image 20240312142125.png|center|500]]

![[Pasted image 20240312142145.png|center|500]]

**Esempio di operazioni sulla QuickFind**

![[Pasted image 20240312142209.png|center|500]]

**Esempio di una sequenza di operazioni** : [Esempio](https://www.mat.uniroma2.it/~guala/02_Union_find_2023.pdf?11)

Quanto costano le operazioni?
- makeSet(x) costa $O(1)$
- Find(x) costa $O(1)$
- Union(A,B) costa $O(n)$

#### Union di costo lineare

Find e makeSet richiedono tempo costante, ma particolari sequenze di union possono essere **molto inefficienti**

![[Pasted image 20240312142529.png|center|400]]

#### Migliorare la struttura QuickFind : euristica union-by-size

Idea di questa modifica è quella di fare in modo che un nodo/elemento non cambi padre troppo spesso

Nell’unione degli insiemi A e B, attacchiamo gli elementi dell’**insieme di cardinalità minore** a quello di **cardinalità maggiore**, e se necessario modifichiamo la radice dell’albero ottenuto (per aggiornare il nome)

Ogni insieme mantiene esplicitamente anche la propria size (numero di elementi)

![[Pasted image 20240312143151.png|center|400]]

**Vedi esempio :** [Esempio](https://www.mat.uniroma2.it/~guala/02_Union_find_2023.pdf?25)

**Realizzazione**

![[Pasted image 20240312143254.png|center|500]]

![[Pasted image 20240312143327.png|center|500]]

![[Pasted image 20240312143353.png|center|500]]

$T_{am}$ = tempo per operazione **ammortizzato** sull’intera sequenza di unioni

Ogni singola operazione costa :
- makeSet(x) costa $O(1)$
- Union(A,B) costa $O(n)$ caso peggiore, $O(\log(n))$ ammortizzato
- Find(x) costa $O(1)$

**Domanda** : quanto costa cambiare padre ad un nodo?
Risposta : tempo costante

**Domanda(Cruciale)** : quante volte un nodo cambia padre?
Risposta : al più $\log(n)$

![[Pasted image 20240312143902.png|center|500]]

##### Analisi Ammortizzata

Vogliamo dimostrare che se eseguiamo m find, n makeSet, e le al più n-1 union, il tempo richiesto dall’intera sequenza di operazioni è $O(m + n\log(n))$

Idea della dimostrazione :
- è facile vedere che find e makeSet richiedono tempo $\Theta(m+n)$
- Per analizzare le operazioni di **union**, ci concentriamo su un singolo nodo/elemento e dimostriamo che il tempo speso per tale nodo è $O(\log(n))\implies$ in totale, tempo speso è $O(n\log(n))$
- Quando eseguiamo una union, per ogni nodo che cambia padre pagheremo tempo costante
- Osserviamo ora che ogni nodo può **cambiare** al più $O(\log(n))$ **padri**, poiché ogni volta che un nodo cambia padre la cardinalità dell’insieme al quale apparterrà **è almeno doppia** rispetto a quella dell’insieme cui apparteneva!
	- all’inizio un nodo è in un insieme di dimensione 1
	- poi se cambia padre in un insieme di dimensione almeno 2
	- all’i-esimo cambio è in un insieme di dimensione almeno $2^i$

Il tempo speso per un singolo nodo sull’intera sequenza di n union è $O(\log(n))$
L’intera sequenza di operazioni costa
$$O(m+n+n\log(n))=O(m+n\log(n))$$

### QuickUnion

Usiamo una **foresta di alberi di altezza anche maggiore di 1** per rappresentare gli insiemi disgiunti.
In ogni albero:
- Radice = Elemento rappresentativo
- Nodi interni = Altri elementi (**escluso** l'elemento nella radice)

**Esempio di operazioni sulla QuickUnion**

![[Pasted image 20240312144528.png|center|500]]


**Esempio sequenza di operazioni** : [Esempio](https://www.mat.uniroma2.it/~guala/02_Union_find_2023.pdf?45)

Quanto costano le operazioni?
- makeSet(x) costa $O(1)$
- Union(A,B) costa $O(1)$
- Find(x) costa $O(n)$

#### Find di costo lineare

Particolari sequenze di union possono generare un albero di altezza lineare, e quindi la find è molto indefficiente (costo n-1 nel caso peggiore)

![[Pasted image 20240312144748.png|center|500]]

Se eseguiamo n makeSet, n-1 union come sopra, seguite da m find, il tempo richiesto dall’intera sequenza di operazioni è $O(n+n-1+mn)=O(mn)$

#### Migliorare la struttura QuickUnion : euristica union-by-size

L'idea è fare in modo che per ogni insieme l'albero corrispondente abbia altezza piccola

**Union by size**: nell’unione degli insiemi A e B, rendiamo la radice dell’albero con **meno nodi** figlia della radice dell’**albero con più nodi**

![[Pasted image 20240312145003.png|center|500]]

**Esempio sequenza di operazioni** : [Esempio](https://www.mat.uniroma2.it/~guala/02_Union_find_2023.pdf?56)

>[!definition]- Lemma
>Con la union by size, dato un albero QuickUnion con size (numero di nodi) s e altezza h vale che $s\geq2^h$

$$\begin{align}&\text{L’operazione find richiede tempo}\:O(\log(n))\\&\downarrow\\&\text{L’intera sequenza di operazioni costa}\:O(n+m\log(n))\end{align}$$

#### Ulteriore Euristica : compressione dei cammini

**Idea**: quando eseguo `find(x)` e attraverso il cammino da x alla radice, **comprimo il cammino**, ovvero rendo tutti i nodi del cammino figli della radice

**Intuizione**: find(x) ha un costo ancora lineare nella lunghezza del cammino attraversato, ma prossime find costeranno di meno

![[Pasted image 20240312145715.png|center|500]]

>[!definition]- Teorema $[\text{Tarjan,Van Leeuwen}]$
>Usando in **QuickUnion** le euristiche di union by rank (o by size) e compressione dei cammini, una qualsiasi sequenza di n makeSet, n-1 union e m find hanno un costo di $O(n+m*\alpha(n+m,n))$

$\alpha(x,y)$ è la funzione inversa di Ackermann

#### Funzione inversa di Ackermann $A(i,j)$ e la sua inversa $\alpha(m,n)$

Notazione: con $a^{b^c}$ intendiamo $a^{(b^c)}$, e non $(a^b)^c=a^{b*c}$
Per interi $i,j\geq1$, definiamo A(i,j) come
$$\begin{align}A(i,j)=\begin{cases}A(1,j) = 2^j&j\geq1\\A(i,1)= A(i-1,2)&i\geq2\\A(i,j)=A(i-1,A(i,j-1))&i,j\geq2\end{cases}\end{align}$$