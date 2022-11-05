
# Indice degli algoritmi

- Algoritmi basati su confronto:
	- MergeSort
	- [[Algoritmi#BubbleSort|BubbleSort]]
	- [[Algoritmi#Insertion Sort|InsertionSort]]
	- SelectionSort
	- QuickSort
	- [[Algoritmi#HeapSort|HeapSort]]

- Algoritmi non basati su confronto
	- [[Algoritmi#IntegerSort|IntegerSort]]
	- BucketSort
	- RadixSort

# Algoritmi basati su confronto

## BubbleSort
Algoritmo 1 (BubbleSort)

### Pseudo-codice
Pseudo-codice:

>BubbleSort(A):
>1. scambio = true
>2. while scambio do
>3. 	scambio = false
>4. 	for i =0 to n-2 do
>5. 		if $A[i]\gt A[i+1]$ then
>6. 		swap($A[i],A[i+1]$)
>7. 		scambio=true

n è la lunghezza dell'array

### Complessità temporale

l'Upper bound dell'algoritmo è:

T(n)=#passi elementari eseguiti su una RAM
$c_j$= costo della j-esima riga
- linee 1,3,5,6,7 hanno costo costante
- linea 2 eseguita al più n volte
- linea 4 eseguita al più n-2 volte per ogni ciclo esterno

$$T(n)\leq c_1+nc_2+n(n-2)(c_3+c_4+c_5)\implies T(n)=O(n^2)\implies T(n)=\Theta(n^2)$$

## Insertion Sort

### Pseudo-codice

>InsertionSort(A)
>1. for j=2 to n
>2.	do key=$A[j]$
>3.		//inserisce $A[j]$ nella sequenza ordinata $A[1...j-1]$
>4.		i=j-1
>5.		while $i\gt0\:and\:A[i]\gt key$
>6.			do $A[i+1]=A[i]$
>7.				i=i-1
>8.		$A[i+1]=key$

### Complessità temporale

- linea 1 eseguita n-2 volte
- linea 2,3 costo costante,eseguite al più n volte
- linea 4 eseguita al più n-2 volte (In realtà sarebbe $\sum_{j=2}^n t_j$) per ciclo esterno
- linee 5,6 costo costante, eseguite al più n-2 volte (In realtà sarebbe $\sum_{j=2}^n t_j$)
- linea 7 costo costante
$t_j$ è il numero di volte che la linea 4 viene eseguita

$T(n)\leq n((c_2+c_3+c_7+c_6+c_5)+(n-2))=nc+n^2\implies$
$T(n)=O(n^2)\implies T(n)=\Theta(n^2)$

## HeapSort

#### Pseudo-codice

Pseudo-codice HeapSort:

>HeapSort(A)
>1. Heapify(A)
>2. $Heapsize[A]=n$
>3. for i = n down to 2 do
>4.	   scambia $A[i]$ e $A[j]$
>5.    $Heapsize[A]=Heapsize[A]-1$
>6.    fixHeap(1,A)

Pseudo-codice fixHeap(1,A)

>fixHeap(i,A)
>1. s=sin(i)
>2. d=des(i)
>3. if($s\leq Heapsize[A]$ e $A[s]\gt A[i]$ )
>4.       then massimo = s
>5.       else massimo = i
>6. if($d\leq Heapsize[A]$ e $A[d]\gt A[massimo]$ )
>7.       then massimo = d
>8. if (massimo$\neq$ i) then
>9.      scambia $A[i]$ e $A[massimo]$
>10.	     fixHeap(massimo,A)

Pseudo-codice heapify

>**heapify**(A)
>1. $Heapsize[A]=n$
>2. for i = $\lfloor n/2\rfloor$  down to 1 do
>3.       fixHeap(i,A)

### Complessità temporale

Per complessità temporale di heapify si rimanda alla lezione [[Lezione 6 - HeapSort#Complessità heapify|Lezione 6 - Complessità heapify]]

Complessità HeapSort:
- linea 1 costo $O(n)$ (costruzione dell'heap)
- linea 3-6 esegue n-1 estrazioni di costo $O(log(n))$

Quindi $$T(n)\leq(n-1)log(n)\implies O(nlog(n))$$


# Algoritmi non basati su confronto

## IntegerSort

### Pseudo-codice

Pseudo-codice:
>IntegerSort(A,k):
>1. Sia Y un array di dimensione k
>2. for i=1 to k do $Y[i]=0$
>3. for i=1 to n do incrementa $Y[x[i]]$
>4. j=i
>5. for i=1 to k do
>6. 	while($Y[i]\gt0$) do
>7. 	$X[j]=i$
>8. 	incrementa i
>9. 	decrementa j

### Complessità temporale

- linea 1 costo $O(1)$
- linea 2 costo $O(k)$
- linea 3 costo $O(n)$
- linea 4 costo $O(1)$
- linea 5 costo $O(k)$
- linee 6-9, per i fissato il num. di volte eseguite è al più $1+Y[i]\implies O(k+n)$

Quindi:
$$T(n)\leq\sum_{i=1}^k(1+Y[i])=\sum_{i=1}^k1+\sum_{i=1}^k(Y[i])=k+n\implies O(n+k)$$
#### Analisi
- Tempo $O(1)+O(k)=O(k)$ per inizializzare Y a 0
- Tempo $O(1)+O(n)=O(n)$ per calcolare i valori dei contatori
- Tempo $O(n+k)$ per ricostruire X
$O(n+k)$
Tempo linearea se $k=O(n)$
