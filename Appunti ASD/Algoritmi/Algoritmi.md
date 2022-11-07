
# Indice degli algoritmi

- Algoritmi basati su confronto:
	- [[Algoritmi#MergeSort|MergeSort]]
	- [[Algoritmi#BubbleSort|BubbleSort]]
	- [[Algoritmi#Insertion Sort|InsertionSort]]
	- [[Lezione 5 - Capitolo 4#Selection Sort|SelectionSort]]
	- [[Lezione 5 - Capitolo 4#QuickSort|QuickSort]]
	- [[Algoritmi#HeapSort|HeapSort]]

- Algoritmi non basati su confronto
	- [[Algoritmi#IntegerSort|IntegerSort]]
	- BucketSort
	- RadixSort

Per una spiegazione più dettagliata di qeusti algoritmi si rimanda a questo link [Algoritmi](http://people.disim.univaq.it/guido.proietti/lezioni_algo2021.html)


# Algoritmi basati su confronto

## BubbleSort

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

## InsertionSort

Spiegazione dettagliata qui -> [Algoritmi,lezione 13/10/21](http://people.disim.univaq.it/guido.proietti/lezioni_algo2021.html)
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

Spiegazione qui -> [[Lezione 6 - HeapSort#HeapSort|HeapSort]]
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


## MergeSort

Spiegazione qui -> [[Lezione 5 - Capitolo 4#MergeSort|MergeSort]]
### Pseudo-codice

Pseudo-codice procedura Merge
>$Merge(A,i_1,f_1,f_2)$
>1. Sia X un array ausilirario di lunghezza $f_2-i_1+1$
>2. $i=1;k_1=i_1$
>3. $k_2=f_1+1$
>4. while($k_1\leq f_1\:e\:k_2\leq f_2$) do
>5.      if($A[k_1]\leq A[k_2]$)
>6. 	 then $X[i]=A[k_1]$
>7. 		 incrementa i e $k_1$
>8. 	 else $X[i]=A[k_2]$
>9. 		 incrementa i e $k_2$
>10. if($k_1\leq f_1$) then copia $A[k_1;f_1]$ alla fine di X
>11. else copia $A[k_2;f_2]$ alla fine di X
>12. copia X in $A[i_1;f_2]$


Pseudo-codice MergeSort
>MergeSort(A,i,f)
> 1. if(i<f) then
> 2. 	 m=$\lfloor(i+f)/2\rfloor$
> 3. 	 MergeSort(A,i,m)
> 4. 	 MergeSort(A,m+1,f)
> 5. 	 Merge(A,i,m,f) $\implies\:fonde\:A[i;m]\:e\:A[m+1;f]\:output\:A[i;f]$

### Complessità temporale

La complessità termporale del MergeSort è descritto dalla seguente relazione di ricorrenza:
$$T(n)=2T(n/2)+O(n)$$
Usando il Teorema Master abbiamo che:
$$T(n)=O(nlog(n))$$
 
## SelectionSort 

Spiegazione qui -> [[Lezione 5 - Capitolo 4#Selection Sort|SelectionSort]]
### Pseudo-codice

>SelectionSort(A)
>1. for k=0 to n-2 do
>2.     m=k+1
>3.     for j=k+2 to n do
>4.          if($A[j]\lt A[m]$) then m=j
>5.     scambia $A[m]\:con\:A[k+1]$
### Complessità temporale

Upper Bound:
$$T(n)\leq 5n^2O(1)=\Theta(n^2)\implies T(n)=O(n^2)$$
Lower Bound:
$$T(n)\geq\sum_{k=0}^{n-2}(n-k-1)=\sum_{k=1}^{n-1}(k)=n(n-1)/2=\Theta(n^2)\implies T(n)=\Omega(n^2)$$
Upper Bound $O(n^2)$ e Lower Bound $\Omega(n^2)$ allora $T(n)=\Theta(n^2)$

## QuickSort

Spiegazione qui -> [[Lezione 5 - Capitolo 4#QuickSort|QuickSort]]
### Pseudo-codice

Pseudo-codice Partition
>Partition(A,i,f)
>1. $x=A[i]$
>2. inf=i
>3. sup=f+1
>4. while(true) do
>5. 	 do (inf=inf+1) while ($inf\leq f\:e\:A[inf]\leq x$)
>6. 	 do (sup=sup-1) while ($A[sup]\gt x$)
>7. 	 if ($inf\lt sup$) then scambia $A[inf]\:e\:A[sup]$
>8. 	 else **break**
>9. scambia $A[i]\:e\:A[sup]$
>10. return sup

Pseudo-codice QuickSort
>QuickSort(A,i,f)
>1. if($i\lt f$) then
>2. 	 m=Partition(A,i,f)
>3. 	 QuickSort(A,i,m-1)
>4. 	 QuickSort(A,m+1,f)


### Complessità temporale

Upper Bound:
$$T(n)=T(n-1)+T(0)+O(n)=T(n-1)+O(1)+O(n)=T(n-1)+O(n)\implies T(n)=O(n^2)$$
Lower Bound:
$$T(n)=\Omega(nlog(n))$$




# Algoritmi non basati su confronto

## IntegerSort

### Pseudo-codice

Pseudo-codice:
>IntegerSort(A,k):
>1. Sia Y un array di dimensione k
>2. for i=1 to k do $Y[i]=0$
>3. for i=1 to n do incrementa $Y[x[i]]$
>4. j=1
>5. for i=1 to k do
>6. 	while($Y[i]\gt0$) do
>7. 	$X[j]=i$
>8. 	incrementa j
>9. 	decrementa $Y[i]$

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




# Codici degli algoritmi in python
## BubbleSort
```python
def bubble_sort( a ):
    '''
    pre: a è una lista di numeri
    ordina la lista dall'elemento più piccolo a quello più grande
    '''
    n = len(a)
    ordinata = False
    num_scansioni = 1
    while not ordinata:
        print(num_scansioni)
        num_scansioni += 1
        ordinata = True
        for i in range(n-1):
            # confrontiamo l'elemento in posizione i e i+1
            if a[i] > a[i+1]:
                # scambio gli elementi, non posso dire che la lista è ordinata
                a[i], a[i+1] = a[i+1], a[i]
                ordinata = False
b = [9,8,7,6,5,4,3,2,1]
bubble_sort(b)
print(b)
```

## MergeSort
```python
def merge( a, lx, cx, rx ):
    '''
    Precondizione: a lista e a[lx:cx] e a[cx:rx] ordinate in modo non decrescente
    Modifica a fondendo le due sottoliste in modo che a[lx:rx] risulti ordinata
    Sia n = len(a), e k = rx-lx
    '''
    i, j = lx, cx # indice in a[lx:cx] ed in a[cx:rx] rispettivamente
    c = [] # lista di output
    while i < cx and j < rx:
        if a[i] < a[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(a[j])
            j += 1
    c += a[i:cx] + a[j:rx]
    for i in range(len(c)):
        a[lx+i] = c[i]

def merge_sort(a, lx, rx):
    '''
    Precondizione: a una lista numerica
    Ordina a[lx:rx]
    '''
    if lx <= rx-2: # almeno due elementi in a[lx:rx]
        cx = (rx+lx)//2
        merge_sort(a, lx, cx)
        merge_sort(a, cx, rx)
        a = merge(a, lx, cx, rx)
a = [2,1,10,5,7,0,4,9,6,8,11,1,2]
n = len(a)
merge_sort(a, 0, n)
print(a)
```

## IntegerSort
```python
def IntegerSort(A,k):
    Y=[0]*k
    n=len(A)
    for i in range(n-1):
        Y[A[i]]+=1
    j=0
    for i in range(k):
        while(Y[i]>0):
            A[j]=i
            j+=1
            Y[i]-=1
    return A
a = [1,10,4,3,3,5,20]
print(IntegerSort(a,20))
```

## QuickSort
```python
def QuickSort(A,i,f):
    if(i<f):
        m=Partition(A,i,f)
        QuickSort(A,i,m-1)
        QuickSort(A,m+1,f)
    return A
    
def Partition(A,i,f):
    x=A[i]
    inf=i
    sup=f+1
    while True:
        inf=inf+1
        while inf<= f and A[inf]<= x:
            inf=inf+1
        sup=sup-1
        while A[sup]>x:
            sup=sup-1
        if inf< sup:
            A[inf],A[sup]=A[sup],A[inf]
        else:
            break
    A[i],A[sup]=A[sup],A[i]
    return sup

a = [1,10,4,3,3,5,20]
print(QuickSort(a,0,6))
```

## SelectionSort

```python

```
