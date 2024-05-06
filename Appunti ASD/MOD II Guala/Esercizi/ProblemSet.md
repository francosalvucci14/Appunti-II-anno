
```table-of-contents
title: 
style: nestedList # TOC style (nestedList|inlineFirstLevel)
minLevel: 0 # Include headings from the specified level
maxLevel: 0 # Include headings up to the specified level
includeLinks: true # Make headings clickable
debugInConsole: false # Print debug info in Obsidian console
```

# Esercizio 1

# Esercizio 2

## Struttura

## Esempio

## Pseudocodice

# Esercizio 3

## Struttura

### Definizione dei sottoproblemi

Prima di risolvere l'esercizio, definiamo prima i sottoproblemi, e dopo averli definiti, andiamo a dimostrarne la correttezza

I sottoproblemi sono i seguenti :

$\forall i,j$ abbiamo che :
$$OPT(i,j)=\text{Minimo costo dell'albero composto dalle foglie che vanno dalla posizione i a j}$$
- $i,j$ sono gli indici del vettore $c[i:j]$, dove $c$ è il vettore dei valori presi in input, con $i\leq j$

Adesso, per capire se i sottoproblemi vanno bene, dobbiamo rispondere alle seguenti domande

1) **I sottoproblemi sono pochi?** Dobbiamo calcolare l'ottimo per tutte le possibili coppie di elementi tali che $i\leq j$. In questo modo abbiamo che il numero di sottoproblemi è pari a $O(n^2/2)$ perchè una volta che abbiamo calcolato la coppia $(i,j)$, la coppia $(j,i)$ non verrà calcolata in quanto è equivalente alla sua controparte.
2) **È possibile definire la soluzione del sottoproblema generico in funzione dei sottoproblemi più piccoli?** Si, perchè il valore dell'$OPT(i,j)$ è dato dall'$OPT(i,k)+OPT(k+1,j)+$ prodotto tra massima foglia sx e massima foglia dx.
3) **In che ordine è possibile risolvere i sottoproblemi?** L'ordine di risoluzione è partire dal problema iniziale, e calcolare l'ottimo dei sottoproblemi più piccoli andando a "indovinare" l'indice $k$ che minimizza il costo dell'albero composto dalle foglie che vanno da $i\to j$, per poi ricombinare tutte le soluzioni dei sottoproblemi, in modo da ottenere il valore finale, ovvero $OPT(1,n)$
4) **Quali sono i casi base?** Abbiamo 2 casi base
	1) $i=j$, significa che stiamo vedendo una sola foglia, e di conseguenza non possiamo generare nessun nodo interno, quindi l'albero avrà costo $0$
	2) $j-i=1$, significa che abbiamo 2 foglie, di conseguenza il costo dell'albero sarà il prodotto tra $c(i)$ e $c(j)$

### Equazione di Bellman

A questo punto, possiamo definire la **formula di Bellman**, che sarà

$$OPT(i, j)=\begin{cases}0&\text{se i=j}\\c(i)*c(j)&\text{se |j-i|=1}\\\min_{k=i}^{j} \{ OPT(i, k) + OPT(k+1, j) + \text{max-leaf}(i, k) \times \text{max-leaf}(k+1, j)\}&\text{altrimenti}\end{cases}$$

Il valore che vogliamo ottenere è
 $$OPT[1,n]$$
 >[!info]- Osservazione
 >$\text{max-leaf(i,k)}$ prende il valore massimo che si trova nella porzione di array $c[i:k]$, $\forall k=i,\dots,j$
 >In modo analogo vale la stessa osservazione per $\text{max-leaf(k+1,j)}$
## Esempio di esecuzione

**Esempio** : $c=[5,7,6,8]$

Con l'input di esempio, vediamo che la matrice OPT sarà così generata

```python
1)
 [-1 -1 -1 -1]
 [-1 -1 -1 -1]
 [-1 -1 -1 -1]
 [-1 -1 -1 -1]
2)
 [ 0 -1 -1 -1]
 [-1  0 -1 -1]
 [-1 -1  0 -1]
 [-1 -1 -1  0]
3)
[[ 0 -1 -1 -1]
 [-1  0 -1 -1]
 [-1 -1  0 48]
 [-1 -1 -1  0]]
4)
 [ 0 -1 -1 -1]
 [-1  0 42 -1]
 [-1 -1  0 48]
 [-1 -1 -1  0]
5)
 [ 0 -1 -1 -1]
 [-1  0 42 98]
 [-1 -1  0 48]
 [-1 -1 -1  0]
6)
 [ 0 35 -1 -1]
 [-1  0 42 98]
 [-1 -1  0 48]
 [-1 -1 -1  0]
7)
 [ 0 35 77 -1]
 [-1  0 42 98]
 [-1 -1  0 48]
 [-1 -1 -1  0]
8)
 [  0  35  77 133]
 [ -1   0  42  98]
 [ -1  -1   0  48]
 [ -1  -1  -1   0]
```

Il costo totale dell'albero lo troviamo nella posizione $OPT[1,n]$.
L'albero che viene generato è il seguente :

![[AlberoEs3.png|center|350]]

E da qui vediamo che il costo dell'albero (la somma dei nodi in blu) è proprio $133$

## Pseudocodice

```pseudo
\begin{algorithm}
\caption{Algoritmo}
\begin{algorithmic}
\Procedure{Soluzione}{lista $c$,int $n$, int $i$, int $j$,list $OPT$}
	
    \If{$OPT(i,j)\neq -1$}
	    \State return $OPT(i,j)$
    \EndIf
    \If{$i==j$}
		\State $OPT(i,j)\gets 0$
	\Else
	 \State $min_{cost}\gets\infty$
		\For{$k=i$ to $j$}
			\State $\text{left-cost}\gets \text{Soluzione}(c,n,i,k,OPT)$
			\State $\text{right-cost}\gets \text{Soluzione}(c,n,k+1,j,OPT)$
			\State $\text{internal-cost}\gets \max\{c[i:k]\}*\max\{c[k+1:j]\}$
			\State $\text{total-cost}\gets \text{left-cost}+\text{right-cost}+\text{internal-cost}$
			\State $min_{cost}=\min\{min_{cost},\text{internal-cost}\}$
		\EndFor	
		\State $OPT(i,j)\gets min_{cost}$
    \EndIf
    \State return $OPT(i,j)$
\EndProcedure
\end{algorithmic}
\end{algorithm}
```
