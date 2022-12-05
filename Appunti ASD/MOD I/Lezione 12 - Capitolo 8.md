# Il problema della Coda con priorità

## Tipo di dato

![[appunti asd/mod i/immagini/Pasted image 20221205161959.png|center]]

**Operazioni aggiuntive**
![[appunti asd/mod i/immagini/Pasted image 20221205162056.png|center]]

**Applicazioni**: gestione code in risorse condivise, gestione priorità in processi concorrenti, progettazione di algoritmi efficienti per diversi problemi fondamentali (es: calcolo cammini minimi in un grafo, minimo albero ricoprente,ordinamento,ecc...)

## Quattro implementazioni elementari

1. Array non ordinato
2. Array ordinato
3. Lista non ordinata
4. Lista ordinata

Ci focalizzeremo soltato sulle **operazioni di base**

### Array non ordinato

Lo dimensiono sufficientemente grande e tengo traccia del numero n di elementi nella coda in una variabile di appoggio

- **FindMin**: $\Theta(n)$ (devo guardare tutti gli elementi)
- **Insert**: $O(1)$ (inserisco in coda)
- **Delete**: $O(1)$ (poichè mi viene fornito il riferimento diretto all'elemento da cancellare, lo posso cancellare in $O(1)$ sovracopiando l'ultimo elemento)
- **DeleteMin**: $\Theta(n)$ (devo prima cercare il minimo in $\Theta(n)$, poi lo posso cancellare in $O(1)$)

### Array ordinato

Lo dimensiono sufficientemente grande, lo tengo **ordinato** in ordine **decrescente** e tengo traccia del numero n di elementi nella coda in una variabile di appoggio

- **FindMin**: $O(1)$
- **Insert**: $O(n)$ (trovo in $\Theta(log(n))$ la giusta posizione, ma poi devo fare $O(n)$ spostamenti)
- **Delete**: $O(n)$ (devo fare $O(n)$ spostamenti)
- **DeleteMin**: $O(1)$ (l'elemento minimo è in fondo all'array, non devo fare spostamenti)

### Lista non ordinata

La considero **bidirezionale**

![[appunti asd/mod i/immagini/Pasted image 20221205163205.png|center|400]]

- **FindMin**: $\Theta(n)$ (devo guardare tutti gli elementi)
- **Insert**: $O(1)$ (inserisco in coda o in testa)
- **Delete**: $O(1)$ (poichè mi viene fornito il riferimento diretto all'elemento da cancellare, lo posso cancellare in $O(1)$ agendo sui puntatori)
- **DeleteMin**: $\Theta(n)$ (devo prima cercare il minimo in $\Theta(n)$, poi lo posso cancellare in $O(1)$)

### Lista ordinata

Tengo la lista bidirezionale **ordinata** in ordine **crescente**

- **FindMin**: $O(1)$ (il minimo è in testa alla lista)
- **Insert**: $O(n)$ (trovo in $O(n)$ la giusta posizione, e poi faccio in $O(1)$ l'inserimento)
- **Delete**: $O(1)$ (agisco sui puntatori)
- **DeleteMin**: $O(1)$ (basta far puntare la testa della lista al secondo elemento della lista stessa)

### Riepilogo

![[appunti asd/mod i/immagini/Pasted image 20221205163929.png|center|600]]


## Tre implementazioni evolute

1. d-heap: generalizzazione degli heap binari visti per l'ordinamento
2. Heap binomiali
3. Heap di Fibonacci (cenni)

### d-heap

_Def_

Un d-heap è un albero radicato d-ario con le seguenti proprietà:
1. **Struttura**: è completo almeno fino al penultimo livello, e tutte le foglie sull'ultimo livello sono compattate verso sinistra
2. **Contenuto Informativo**: ogni nodo v contiene un elemento **elem(v)** ed una chiave **chiave(v)** presa da un dominio totalmente ordinato
3. **Ordinamento Parziale (inverso) dell'heap (min-heap)**: chiave(v)$\geq$chiave(parent(v)) per ogni nodo v diverso dalla radice

**Esempio**

Heap d-ario con 18 nodi e d=3
![[appunti asd/mod i/immagini/Pasted image 20221205164418.png|center|600]]


#### Proprietà

1. Un d-heap con n nodi ha altezza $\Theta(log_dn)$
2. La **radice** contiene l'**elemento con chiave minima** (per via della proprietà di ordimento a heap)
3. Può essere **rappresentato implicitamente** tramite vettore posizionale grazie alla proprietà di struttura

##### Procedure ausiliarie

Utili per ripristinare la prorpietà di ordinamento a heap su un nodo v che non la soddisfi
![[appunti asd/mod i/immagini/Pasted image 20221205165117.png|center]]

#### FindMin

![[appunti asd/mod i/immagini/Pasted image 20221205165304.png|center|500]]

$T(n)=O(1)$

#### Insert(elem e, chiave k)

Vedi esempio qua [Esempio Insert](https://www.mat.uniroma2.it/~guala/cap8_2021.pdf) da pagina 17 a 21

![[appunti asd/mod i/immagini/Pasted image 20221205165446.png|center]]

$T(n)=O(log_dn)$ per l'esecuzione di muoviAlto

#### delete(elem e) e deleteMin

Vedi esempio qua [Esempio delete](https://www.mat.uniroma2.it/~guala/cap8_2021.pdf) da pagina 23 a 30

![[appunti asd/mod i/immagini/Pasted image 20221205170319.png|center]]

$T(n)=O(log_dn)$ o $O(dlog_dn)$ per l'esecuzione di muoviAlto o muoviBasso

#### decreaseKey (elem e, chiave d)

Vedi esempio qua [Esempio delete](https://www.mat.uniroma2.it/~guala/cap8_2021.pdf) da pagina 32 a 36

![[appunti asd/mod i/immagini/Pasted image 20221205170802.png|center]]

$T(n)=O(log_dn)$ per l'esecuzione di muoviAlto

#### increaseKey (elem e,chiave d)

Vedi esempio qua [Esempio delete](https://www.mat.uniroma2.it/~guala/cap8_2021.pdf) da pagina 38 a 42

![[appunti asd/mod i/immagini/Pasted image 20221205170924.png|center]]

$T(n)=O(dlog_dn)$ per l'esecuzione di muoviBasso

#### merge (CodaPriorità $c_1$, CodaPriorità $c_2$)

Due modi:
1. **Costruire da zero**: si distruggono le due cose e se ne crea una nuova contenente l'unione degli elementi
2. **Inserimenti ripetuti**: si inseriscono ripetutamente gli elementi della cosa più piccola in quella più grande

##### Costruire da zero
