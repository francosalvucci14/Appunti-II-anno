
# Indice degli algoritmi

- Algoritmi basati su confronto:
	- [[Algoritmi#MergeSort|MergeSort]]
	- [[Algoritmi#BubbleSort|BubbleSort]]
	- [[Algoritmi#Insertion Sort|InsertionSort]]
	- [[Algoritmi#SelectionSort|SelectionSort]]
	- [[Algoritmi#QuickSort|QuickSort]]
	- [[Algoritmi#HeapSort|HeapSort]]

- Algoritmi non basati su confronto
	- [[Algoritmi#IntegerSort|IntegerSort]]
	- [[Algoritmi#BucketSort|BucketSort]]
	- [[Algoritmi#RadixSort|RadixSort]]

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
![[appunti asd/algoritmi/img/Pasted image 20221114151346.png|center|500]]

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
![[appunti asd/algoritmi/img/Pasted image 20221114152736.png|center|500]]

Pseudo-codice fixHeap(1,A)
![[appunti asd/algoritmi/img/Pasted image 20221114152647.png|center|500]]

Pseudo-codice heapify
![[appunti asd/algoritmi/img/Pasted image 20221114152850.png|center|500]]

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
![[appunti asd/algoritmi/img/Pasted image 20221114152131.png|center|500]]

Pseudo-codice MergeSort
![[appunti asd/algoritmi/img/Pasted image 20221114152039.png|center|500]]

### Complessità temporale

La complessità termporale del MergeSort è descritto dalla seguente relazione di ricorrenza:
$$T(n)=2T(n/2)+O(n)$$
Usando il Teorema Master abbiamo che:
$$T(n)=O(nlog(n))$$
 
## SelectionSort 

Spiegazione qui -> [[Lezione 5 - Capitolo 4#Selection Sort|SelectionSort]]
### Pseudo-codice
![[appunti asd/algoritmi/img/Pasted image 20221114151002.png|center|500]]

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
![[appunti asd/algoritmi/img/Pasted image 20221114152458.png|center|500]]

Pseudo-codice QuickSort
![[appunti asd/algoritmi/img/Pasted image 20221114152536.png|center|500]]

### Complessità temporale

Upper Bound:
$$T(n)=T(n-1)+T(0)+O(n)=T(n-1)+O(1)+O(n)=T(n-1)+O(n)\implies T(n)=O(n^2)$$
Lower Bound:
$$T(n)=\Omega(nlog(n))$$




# Algoritmi non basati su confronto

## IntegerSort

### Pseudo-codice
![[appunti asd/algoritmi/img/Pasted image 20221114151518.png|center|400]]

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




## BucketSort

Spiegazione qui -> [[Lezione 8 - Capitolo 4#BucketSort|BucketSort]]

### Pseudo-codice

Pseudo codice BucketSort
![[appunti asd/algoritmi/img/Pasted image 20221114151629.png|center|500]]

### Complessità temporale

Come l'IntegerSort, quindi $O(n+k)$

## RadixSort

Spiegazione qui -> [[Lezione 8 - Capitolo 4#RadixSort|RadixSort]]
### Pseudo-codice

Pseudo codice RadixSort
>RadixSort(A)

### Complessità
- $O(log_bk)$ passate di BucketSort
- Ciascuna passata richiede tempo $O(n+b)$
Quindi:
$$O((n+b)log_bk)$$
Se $b=\Theta(n)$, si ha $O(nlog_nk)=O[n\frac{log(k)}{log(n)}]$

Tempo lineare se $k=O(n^c)$, c costante

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
def SelectionSort(a):
    n=len(a)
    for k in range(n-2):
        m=k+1
        for j in range(k+2,n):
            if a[j]<a[m]:
                m=j
        a[m],a[k+1]=a[k+1],a[m]
    return a
a = [1,10,4,3,3,5,20]
print(SelectionSort(a))
```


## HeapSort
da completare
```python
import math
def HeapSort(a):
    heapify(a)
    heapsize = len(a)-1
    for i in range(heapsize,2,-1):
        a[1],a[i]=a[i],a[1]
        heapsize -=1
        fixHeap(1,a)
    return a

def fixHeap(i,a):
    heapsize = len(a)-1
    sx = 2*i
    dx = 2*i+1
    if sx<=heapsize and a[sx]>a[i]:
        max = sx
    else:
        max = i
    if dx<=heapsize and a[dx]>a[max]:
        max = dx
    if max != i:
        a[i],a[max] = a[max],a[i]
        fixHeap(max,a)

def heapify(a):
    heapsize = len(a)-1
    n=heapsize
    for i in range(math.floor(n/2),1):
        fixHeap(i,a)

a = [1,10,4,3,3,5,20]
print(HeapSort(a))
```


