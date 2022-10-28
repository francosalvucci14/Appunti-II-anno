# Progettare algoritmi veolic usando strutture dati efficienti

## HeapSort
Stesso approccio incrementale del SelectionSort
- selezione gli elementi dal più grande al più piccolo
- usa una **struttura dati efficente**
	- estrazione in tempo $O(log(n))$ del massimo

>**Tipo di dato** Specifica una collezione di oggetti e delle operazioni di interesse su tale colelzione (es. Dizionario: mantiene un insieme di elementi con chiavi soggetto a operazioni di inserimento, cancellazione,ricerca)

>**Struttura dati** Organizzazione dei dati che permette di memorizzare la collezione e supportare le operazioni di un tipo di dato usando meno risorse di calcolo possibile

**Cruciale**: progettare una struttura dati H su cui eseguire efficientemente le operazioni:
- dato un array A, generare velocemente H
- trovare il più grande oggetto in H
- cancellare il più grande oggetto da H

**Tipo di dato associato**: coda con priorità

### Alberi: qualche altra definizione

![[appunti asd/immagini/Pasted image 20221028093543.png|center|700]]

**albero d-ario**: albero in cui tutti i nodi interni hanno (al più) d figli
$d=2\implies$**albero binario**
Un albero d-ario è **completo**: se tutti nodi interni hanno esattamente d figli e le foglie sono tutte allo steso livello

![[appunti asd/immagini/Pasted image 20221028093928.png|center|600]]


## Struttura dati Heap
Associati ad un insieme S=albero binario radicato con le seguenti proprietà:
1. completo fino al penultimo livello (struttura rafforzata: foglie sull'ultimo livello tutte compattate a sinistra)
2. gli elementi di S sono memorizzati nei nodi dell'albero (ogni nodo v memorizza uno e un solo elemento, denotato con chiave(v))
3. $chiave(padre(v))\geq chiave(v)$ per ogni nodo v diverso dalla radice


![[appunti asd/immagini/Pasted image 20221028094332.png|center|600]]

### Proprietà salienti degli Heap
1. Il **massimo** è contenuto **nella radice**
2. L'albero con n nodi ha **altezza O(log(n))**
3. Gli heap con struttura rafforzara possono essere rappresentati in un **array di dimensione pari a n**
#### Altezza di un heap : prop2
Sia H un heap di n nodi e altezza h
![[appunti asd/immagini/Pasted image 20221028094753.png|center|600]]

$$n\geq 1+\sum_{i=0}^{h-1}2^i=1+2^h-1=2^h\implies h\leq log_2n$$
#### Rappresentazione tramite vettore posizionale : prop3

![[appunti asd/immagini/Pasted image 20221028095850.png|center|600]]

...ancora un esempio
![[appunti asd/immagini/Pasted image 20221028095939.png|center|700]]

## La procedura fixHeap

Sia v la radice di H. Assume che i sottoalberi radicati nel figlio sinistro e destro di v sono heap,ma la proprietà di ordinamento delle chiavi non vale per v. Posso ripristinarla così:

> **fixHeap**(nodo v,heap H)
> if (v non è una foglia) then
> 	sia u il figlio di v con chiave massima
> 	if (chiave(v)$\lt$chiave(u)) then
> 		scambia chiave(v) e chiave(u)
> 		**fixHeap**(u,H)

Tempo di esecuzione: $O(log(n))$

**Esempio**
![[appunti asd/immagini/Pasted image 20221028101608.png|center|500]]
Scambio 4 con 16 (quindi chiave(i=1)<chiave(i=2))


