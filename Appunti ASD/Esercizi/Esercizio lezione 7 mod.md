Dato un vettore X di n reali in $[1,k]$, costruire in tempo $o(n^2)$ una struttura dati (**oracolo**) che sappia rispondere a domande (**query**) in tempo $O(log(n))$ del tipo : "quanti interi in X cadono nell'intervallo $[a,b]$?", per ogni a e b

per la risposta alla query usiamo il binarysearch

Soluzione:

- Passo 1: dato il vettore X in input, lo ordino in tempo $O(nlog(n))$ tramite il MergeSort, in questo modo il mio Oracolo sarà il vettore X ordinato
- Passo 2: Per rispondere alle query in tempo $O(log(n))$ utilizzo il binarysearch e mi trovo tutti gli elementi <= di b e < di a
- Passo 3: dopo aver ottenuto il numero di elementi <= b e < a eseguo la sottrazione, e quello sarà proprio il numero di elementi compresi fra a e b

Codice
```python
def CreaOracolo(x,a,b):

    n = len(x)

    merge_sort(x,0,n)

    print(x)

    if b>x[n-1]:

        return (n-binSearchLT(x,a))

    if a<x[0]:

        return binSearchGEQ(x,b)

    if b<a:

        return -1

    m_b = binSearchGEQ(x,b)

    m_a = binSearchLT(x,a)

    #print(f"elementi <= di b = {b}:{m_b}, elementi < di a = {a}:{m_a}")

    tot = m_b-m_a

    #print(f"elementi compresi tra a e b {tot}")

    return tot

  

def binSearchLT(a, key):

    n = len(a)

    left = 0

    right = n - 1

    count = 0

    while (left <= right):

        cx = int((right + left) / 2)

        # Check if cxdle element is

        # less than or equal to key

        if (a[cx] < key):

            # At least (cx + 1) elements are there

            # whose values are less than

            # or equal to key

            count = cx + 1

            left = cx + 1

        # If key is smaller, ignore right half

        else:

            right = cx - 1

    return count

  

def binSearchGEQ( a, k ):

    n = len(a)

    lx, rx = 0, n-1

    while lx <= rx: # fintanto che lo spazio di ricerca non è vuoto

        cx = (lx + rx)//2

        if k >= a[cx] and ( cx == n-1 or a[cx+1] > k ):

            return cx+1

        if k < a[cx]:

            rx = cx-1

        else: # k > a[cx]

            lx = cx+1

    return 0

def merge( a, lx, cx, rx ):

    '''

    Precondizione: a lista e a[lx:cx] e a[cx:rx] ordinate in modo non decrescente

    Modifica a fondendo le due sottoliste in modo che a[lx:rx] risulti ordinata

    Sia n = len(a), e k = rx-lx

    Costo: lineare in k

    '''

    i, j = lx, cx # indice in a[lx:cx] ed in a[cx:rx] rispettivamente

    c = [] # lista di output

    # Costo O(k)

    while i < cx and j < rx:

        if a[i] < a[j]:

            c.append(a[i])

            i += 1

        else:

            c.append(a[j])

            j += 1

    # Costo O(k)

    c += a[i:cx] + a[j:rx]

    #a = a[:lx] + c + a[rx:] Costo lx + (rx-lx) + (n-rx) = O(n)

  

    # Costo O(k)

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

#a = [2,1,10,5,7,0,4,9,6,8,11,1,2]

x = [1,-10,4.3,3.35,3,-5,20,-5,-5]

n = len(x)

#caso [a,b]

a = -5

b = -4.9

#caso (a,b]

'''a = -n**100

b = 15'''

#caso [a,b)

'''a = -5

b = n**100'''

print(CreaOracolo(x,a,b))
```
