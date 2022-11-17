
# Esercitazione 1

## Esercizio 1
>Dimostrare o confutare la seguente affermazione:
>Date $f(n)$ e $g(n)$, allora vale che:
>$f(n)=O(g(n))\implies 2^{f(n)}=O(2^{n/2})$

Soluzione:

prendiamo $f(n)=n\:e\:g(n)=n/2$
Così vale che $n=O(n/2)$, ma $2^n\neq O(2^{n/2})$

Infatti:
$lim_{n\to\infty}\frac{n}{n/2}=1/2\lt\infty$ e quindi $n=O(n/2)$

Ma:
$lim_{n\to\infty}\frac{2^n}{2^{n/2}}=2^{n/2}=\infty$ e quindi $2^n=\omega(2^{n/2})$

### Altri esempi per cui non vale l'implicazione
- $f(n)=2n\:e\:g(n)=n$
- $f(n)=n\:e\:g(n)=n^2$
- etc

## Esercizio 2

>Progettare un algoritmo (efficiente) che, dato un array ordinato $A[1:n]$ di n interi e un intero x, trova (se esistono) due indici i e j, $i\lt j$, tale che $A[i]+A[j]=x$

Soluzione banale:
Fisso "i", e per ogni "i" lo confronto con n-1 "j",se li trovo li ritorno, altrimenti ritorno -1
```python
def funzione(A,x):
    n=len(A)
    for i in range(n-1):
        for j in range(i+1,n):
            if A[i]+A[j]==x:
                return i,j
    return (-1,-1)
a = [2,5,9,14,20,21,25,40]
print(funzione(a,25))
```

Corretto? Sì
Complessità? $O(n^2)$

Soluzione non banale

Utilizzo il binarysearch per cercare l'indice j, e per ogni i confronto i con il j trovato dal binarysearch, se j non viene trovato mi ritorna -1
```python
def bin_search( a, k ):
    n = len(a)
    lx, rx = 0, n-1
    while lx <= rx: # fintanto che lo spazio di ricerca non è vuoto
        cx = (lx + rx)//2
        if k == a[cx]:
            return cx
        if k < a[cx]:
            rx = cx-1
        else: # k > a[cx]
            lx = cx+1
    return -1

def algoritmo(A,x):
    n=len(A)
    for i in range(n-1):
        j=bin_search(a,x-A[i])
        if (A[i]+A[j]==x):
            return i,j
    return (-1,-1)

a = [2,5,9,14,20,21,25,40]
print(funzione(a,26))
```

Corretto? Si
Complessità? $O(nlog(n))$

Soluzione meglio di nlog(n)

**Idea**: scansionare l'array "parallelamente" da sinistra e da destra
```python
def Lineare(A,x):
    n=len(A)
    i,j=0,n-1
    while i<j:
        if (A[i]+A[j]==x):
            return i,j
        if (A[i]+A[j]<x):
            i+=1
        else:
            j-=1
    return (-1,-1)

a = [2,5,9,14,20,21,25,40]
print(funzione(a,54))
```

Complessità? $O(n)$
Correttezza? Da vedere

**Oss**: Se non esistono due elementi di A che sommano a x l'algoritmo _Lineare_ risponde sicuramente bene, ovvero restituisce (-1,-1)

# Esercitazione 2

## Esercizio 1

### Risposta alla domanda a
Utilizzo un algoritmo che in tempo $O(log(n))$ mi trova l'indice del massimo. L'algoritmo si basa sul fatto che $a[m]>a[m-1]\:e\:a[m+1]$ 
Il codice è questo:
```python
#a = [2,4,20,13,9,6,5,2]
a = [2,4,20,30,31,6,5,2]
def funzione(a):
    n = len(a)
    lx,rx = 0,n-1
    while lx<=rx:
        cx = (rx+lx)//2
        if (a[cx-1]<a[cx] and a[cx+1]<a[cx]):
            return cx
        if a[cx-1]>a[cx]:
            rx=cx-1
        else:
            lx=cx+1
print(funzione(a))
```
### Risposta alla domanda b
Dato m trovato prima, sappiamo che le due "metà" $a[1:m]$ e $a[m+1,n]$ sono già ordinate
A questo punto utilizzo il Merge per fonderle velocemente
Codice:
```python
import math
a = [2,4,20,30,31,6,5,2]
def trovaMax(a):
    n = len(a)
    lx,rx = 0,n-1
    while lx<=rx:
        cx = (rx+lx)//2
        if (a[cx-1]<a[cx] and a[cx+1]<a[cx]):
            return cx
        if a[cx-1]>a[cx]:
            rx=cx-1
        else:
            lx=cx+1
def ordina(a,m):
    n=len(a)
    if m != n:
        Inverti(a,m)
        if m!=1:
            a = merge(a[:m],a[m:])
    return a
def Inverti(a,m):
    n=len(a)-1
    while m<n:
        tmp = a[m]
        a[m]=a[n]
        a[n]=tmp
        m+=1
        n-=1
    return a
def merge( a, b ):
    n_a, n_b = len(a), len(b)
    i, j = 0, 0 # indice in a ed in b rispettivamente
    c = [] # lista di output
    while i < n_a and j < n_b:
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    c += a[i:] + b[j:]
    return c
max = trovaMax(a)
print(ordina(a,max))
```
Con la funzione trovaMax trovo l'indice dell'elemento maggiore nell'array A, come nella risposta a
Poi partendo da m inverto la lista, quindi inverto da m a fine lista (tutta la parte sinistra partendo da m)
a questo punto in tempo lineare eseguo il merge delle due sottoliste e ottengo l'array ordinato in tempo $o(nlog(n))$

# Esercizio 2

## Esercizio 3 (opzionale)

Sia $V[1:n]$ un vettore di n caratteri, dove ogni posizione può contenere un carattere nell'insieme $\lbrace Y,E,S\rbrace$. il vettore è organizzato in modo che, se letto da sinistra verso destra, si ottiene pirma un seq. non nulla di Y, poi di E e poi si S
Progettare un algoritmo che in tempo $o(n)$ calcoli il numero di Y,E,S nel vettore.

Codice:
```python
a = ["Y","Y","E","E","E","E","S","S"]
def algoritmo(a):
    num_y = applicazionebinsearch(a,"Y",0)
    num_e = applicazionebinsearch(a,"E",1)-num_y
    num_s = applicazionebinsearch(a,"S",2)-(num_e+num_y)
    return(num_y,num_e,num_s)
def applicazionebinsearch(a,k,flag):
    """flag = 0 per Y, flag = 1 per E, flag = 2 per S"""
    n = len(a)
    lx, rx = 0, n-1
    while lx <= rx:
            cx = (lx + rx)//2
            if k == a[cx] and ( cx == n-1 or a[cx+1] != k ):
                return cx+1
            if flag == 0 or flag == 1:
                if k != a[cx+1]:
                    rx = cx-1
                else:
                    lx = cx+1
            else:
                if k != a[cx-1]:
                    lx = cx+1
                else:
                    rx = cx-1
    return -1
print(algoritmo(a))
```

Pseudocodice

Algoritmo
![[Pasted image 20221117115715.png|center|700]]

Applicazione BinSearch
![[Pasted image 20221117115744.png|center|700]]














