
# Lower Bound al probroblema di ordinamento e Algoritmi Lineari

## Sommario

- Delimitazioni inferiori e superiori (di algoritmi e problemi)
- Qunto velocemente si possono ordinare n elementi?
	- una soglia asintotica di velocità sotto la quale non si può scendere: un **lower bound**
		- per una classe di algoritmi ragionevoli - quelli basati su confronti
	- una tecnica elegante che usa gli **alberi di decisione**
- E se si esce da questa classe di algoritmi?
	- **integer sort** e **bucket sort** (per interi "piccoli")
	- **radix sort** (per interi più "grandi")

## Delimitazioni inferiori e superiori (di algoritmi e problemi)

### Delimitazioni superiori (_upper bound_)
_Def_
Un algoritmo A ha complessità (costo di esecuzione) $O(f(n))$ rispetto ad una certa risorsa di calcolo, se la quantità $r(n)$ di risorsa usata da A nel caso peggiore su istanze di dimensione n verifica la relazione $r(n)=O(f(n))$

_Def_
Un problema P ha una complessità $O(f(n))$ rispetto ad una risorsa di calcolo se **esiste** un algoritmo che risolve P il cui costo di esecuzione rispetto quella risorsa è $O(f(n))$

### Delimitazioni inferiori (_lower bound_)
_Def_
Un algoritmo A ha complessità (costo di esecuzione) $\Omega(f(n))$ rispetto ad una certa risorsa di calcolo, se la quantità $r(n)$ di risorsa usata da A nel caso peggiore su istanze di dimensione n verifica la relazione $r(n)=\Omega(f(n))$

_Def_
Un problema P ha una complessità $\Omega(f(n))$ rispetto ad una risorsa di calcolo se **ogni algoritmo** che risolve P ha costo di esecuzione nel caso peggiore $\Omega(f(n))$ rispetto quella risorsa

## Ottimalità di un algoritmo
_Def_
Dato un problema P con complessità $\Omega(f(n))$ rispetto ad una risorsa di calcolo, un algoritmo che risolve P è (asintoticamente) **ottimo** se ha costo di esecuzione $O(f(n))$ rispetto a quella risorsa

## Complessità temporale del problema di ordinamento

- **Upper Bound:**$O(n^2)$:
	- Insertion Sort,Selection Sort,Quick Sort, Bubble Sort
- **Un upper bound migliore**: $O(n log(n))$
	- Merge Sort,Heap Sort
- **Lower bound** $\Omega(n)$
	- banale: ogni algoritmo che ordina n elementi li deve almeno leggere tutti

Abbiamo quindi un **gap di log(n)** tra upper bound e lower bound

**Possiamo fare meglio?**

### Sui limiti della velocità: una delimitazione inferiori alla complessità del problema

>**Ordinamento per confronti**
>Dati due elementi $a_i,a_j$, per determinare l'ordinamento relativo effettuiamo una delle seguenti operazioni di confronto:
>$$a_i\lt a_j\:;\:a_i\leq a_j\:;\:a_i=a_j\:;\:a_i\geq a_j\:;\:a_i\gt a_j$$
>Non si possono esaminare i valori degli elementi o ottenere informazioni sul loro ordine in altro modo

**Notare**: Tutti gli algoritmi citati prima sono algoritmi di ordinamento per confronto

>**Teorema**:
>**Ogni** algoritmo basato su confronti che ordina n elementi deve fare nel caso peggiore $\Omega(nlog(n))$ confronti

**Oss**: il **num. di passi** che un algoritmo esegue è un lower bound al **num. di passi elementari** che esegue

>**Corollario**
>Il MergeSort e l'HeapSort sono algoritmi ottimi (almeno dentro la classe di algoritmi basati su confronti)

### Uno strumento utile: albero di decisione

Gli algoritmi di ordinamento per confronto possono essere descritti in modo astratto in termini di **alberi di decisione**

Un generico algoritmo di ordinamento per confronto lavora nel modo seguente:
- confronta due elementi $a_i,a_j$ (ad esempio effettua il test $a_i\leq a_j$);
- a seconda del risultato - riordina e/o decide il confronto successivo da eseguire.

_Def_
**Albero di decisione**: Descrive i confronti che l'algoritmo esegue quando opera su un input di una **determinata dimensione**. I movimenti dei dati e tutti gli altri aspetti dell'algoritmo vengono ignorati

## Albero di decisione

Descrive le diverse sequenze di confronti che A potrebbe fare su istanze di dimensione n
Nodo interno (non foglia): $i:j$
- modella il **confronto** tra $a_i\:e\:a_j$
Nodo foglia:
- modella una risposta (output) dell'algoritmo: **permutazione degli elementi**

![[appunti asd/immagini/Pasted image 20221103094813.png|center]]

**Osservazioni**
- L'albero di decisione **non è** associato ad un problema
- L'albero di decisione **non è** associato **solo** ad un algoritmo
- L'albero di decisione è associato ad un **algoritmo** e a una **dimensione dell'istanza**
- L'albero di decisione descrive le diverse sequenze di confronti che un certo algoritmo può eseguire su istanze di una **data dimensione**
- L'albero di decisione è una descrizione alternativa dell'algoritmo (customizzato per istanze di una certa dimensione)

**Esempio/Esercizio**
Fornire l'albero di decisione del seguente algoritmo per istanze di dimensione 3
PSEUDO CODICE INSERTIONSORT

**Proprietà**
- Per una particolare istanza, i confronti eseguiti dall'algoritmo su quella istanza rappresentano unn **cammino radice-foglia**
- L'algoritmo segue un cammino diverso a seconda delle caratteristiche dell'istanza:
	- **Caso peggiore**: cammino più lungo
- Il numero di confronti nel caso peggiore è pari **all'altezza dell'albero di decisione**
- Un albero di decisione di un algoritmo (corretto) che risolve il problema dell'ordinamento di n elementi deve avere necessariamente **almeno n! foglie**

>**Lemma**
>Un albero binario T con k foglie, ha altezza almeno $log_2k$

**dim** (per induzione su k)
**caso base**: k=1, altezza almeno $log_21=0$
**caso induttivo**: $k\gt 1$
Considera il nodo interno v più vicino alla radice che ha due figli (v potrebbe essere la radice). nota che v deve esistere perchè $k\gt1$

v ha almeno un figlio u che è radice di un (sotto)albero che ha almeno k/2 foglie e $\lt$ k foglie

T ha altezza almeno
$1+log_2k/2=1+log_2k-log_22=log_2k$

![[appunti asd/immagini/Pasted image 20221103100148.png|center|300]]

## Il Lower Bound $\Omega(nlog(n))$

Consideriamo l'albero di decisione di un qualsiasi algoritmo che risolve il problema dell'ordinamento di n elementi
L'altezza h dell'albero di decisione è almeno $log_2(n!)$
**Formula di Stirling**: $n!\approx (2\pi n)^{1/2}\cdot(n/e)^n$

![[appunti asd/immagini/Pasted image 20221103100605.png|center|500]]
$$\lceil a\rceil$$

