
```table-of-contents
title: 
style: nestedList # TOC style (nestedList|inlineFirstLevel)
minLevel: 0 # Include headings from the specified level
maxLevel: 0 # Include headings up to the specified level
includeLinks: true # Make headings clickable
debugInConsole: false # Print debug info in Obsidian console
```

# Es1
# Es2
# Es3

**Definizione dei sottoproblemi**

$\forall i,j$ abbiamo che :
$$OPT(i,j)=\text{Minimo costo dell'albero composto dalle foglie che vanno dalla posizione i a j}$$
- $i,j$ sono gli indici del vettore $c[i:j]$, dove $c$ è il vettore dei valori presi in input, con $i\leq j$

Adesso, per capire se i sottoproblemi vanno bene, dobbiamo rispondere alle seguenti domande

1) I sottoproblemi sono pochi? Dobbiamo calcolare l'ottimo per tutte le possibili coppie di elementi tali che $i\leq j$. In questo modo abbiamo che il numero di sottoproblemi è pari a $O(n^2/2)$ perchè una volta che abbiamo calcolato la coppia $(i,j)$, la coppia $(j,i)$ non verrà calcolata in quanto è equivalente alla sua controparte.
2) È possibile definire la soluzione del sottoproblema generico in funzione dei sottoproblemi più piccoli? Si, perchè il valore dell'$OPT(i,j)$ è dato dall'$OPT(i,k)+OPT(k+1,j)+$ prodotto tra massima foglia sx e massima foglia dx.
3) In che ordine è possibile risolvere i sottoproblemi? L'ordine di risoluzione è partire dal problema iniziale, e calcolare l'ottimo dei sottoproblemi più piccoli andando a "indovinare" l'indice $k$ che minimizza il costo dell'albero composto dalle foglie che vanno da $i\to j$, per poi ricombinare tutte le soluzioni dei sottoproblemi, in modo da ottenere il valore finale, ovvero $OPT(1,n)$
4) Quali sono i casi base? Abbiamo 2 casi base
	1) $i=j$, significa che stiamo vedendo una sola foglia, e di conseguenza non possiamo generare nessun nodo interno, quindi l'albero avrà costo $0$
	2) $j-i=1$, significa che abbimao 2 foglie, di conseguenza il costo dell'albero sarà il prodotto tra $c(i)$ e $c(j)$

A questo punto, possiamo definire la **formula di Bellman**, che sarà

$$OPT(i, j)=\begin{cases}0&\text{se i=j}\\c(i)*c(j)&\text{se |j-i|=1}\\\min_{k=i}^{j} \{ OPT(i, k) + OPT(k+1, j) + \text{max-leaf}(i, k) \times \text{max-leaf}(k+1, j)\}&\text{altrimenti}\end{cases}$$

Il valore che vogliamo ottenere è
 $$OPT[1,n]$$



**Esempio** : $c=[5,7,6,8]$

L'algoritmo parte con $i=1\land j=n$, e va a "indovinare" l'indice $k$, ricorsivamente, che minimizza il costo dell'albero completo