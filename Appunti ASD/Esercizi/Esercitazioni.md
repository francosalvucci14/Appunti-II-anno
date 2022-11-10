
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

