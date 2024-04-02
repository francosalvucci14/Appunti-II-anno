# Segmented Least Square & Knapsack

## Least Square

>[!definition]- Least Squares
>Problema fondamentale in statistica :
>- Dati $n$ punti nello spazio : $(x_1,y_1),\dots,(x_n,y_n)$
>- Trovare una retta $y=ax+b$ che minimizza la somma degli scarti quadratici (**squared error**), ovvero : $$SSE=\sum\limits_{i=1}^n(y_i-ax_i-b)^2$$

![[Pasted image 20240402095736.png|center|300]]

**Soluzione** Calcolo $\implies$ il minimo errore si ottiene quando
$$\begin{align}&a=\frac{n\sum\limits_ix_iy_i-(\sum\limits_ix_i)(\sum\limits_iy_i)}{n\sum\limits_ix_i^2-(\sum\limits_ix_i)^2}\\&b=\frac{\sum\limits_iy_i-a\sum\limits_ix_i}{n}\end{align}$$

## Segmented Least Square

>[!definition]- Segmented LS
>- I punti giacciono approssimativamente su una sequenza di segmenti
>- Dati $n$ punti nel piano : $(x_1,y_1),\dots,(x_n,y_n)$ con $x_1\lt x_2\lt\dots x_n$ trovare una sequenza di linee che minimizzano $f(x)$

**Q** : Qual'è una scelta ragionevole per $f(x)$ in modo da `bilanciare` $\underbrace{\text{accuratezza}}_{\text{bontà di adattamento}}$ e $\underbrace{\text{parsimonia}}_{\text{numero di linee}}$?

![[Pasted image 20240402100619.png|center|300]]

**Goal** : minimizzare $f(x)=E+cL$ per una qualche costante $c\gt0$, dove :
- $E$ = Somma delle somme degli scarti quadratici in ogni segmento
- $L$ = numero di linee

### Dynamic Programming : Scelte multiple

**Notazione** :
- $OPT(j)$ = minimo costo per i punti $p_1,p_2,\dots,p_j$
- $e_{ij}$ = $SSE$ per i punti $p_i,p_{i+1},\dots,p_j$

Per calcolare $OPT(j)$ :
- L'ultimo segmento usa i punti $p_i,p_{i+1},\dots,p_j$ per un qualche $i\leq j$
- Costo = $\underbrace{e_{ij}+c+OPT(i-1)}_{\text{proprietà ottimale della sottostruttura}}$

**Equazione di Bellman**
$$OPT(j)=\begin{cases}0&j=0\\\min_{1\leq i\leq j}\{e_{ij}+c+OPT(i-1)\}&j\gt0\end{cases}$$
### Algoritmo per SLS

![[Pasted image 20240402101239.png|center|500]]

#### Analisi dell'algoritmo

>[!definition]- Teorema `[Bellman 1961]`
>L'algoritmo di DP risolve il problema del SLS in tempo $O(n^3)$ e spazio $O(n^2)$

**Dimostrazione** :
- Bottleneck lo abbimao quando calcoliamo l'SSE $e_{ij}$ per ongi $i$ e $j$ $$\begin{align}&a_{ij}=\frac{n\sum\limits_kx_ky_k-(\sum\limits_kx_k)(\sum\limits_ky_k)}{n\sum\limits_kx_k^2-(\sum\limits_kx_k)^2}\\&b_{ij}=\frac{\sum\limits_ky_k-a\sum\limits_kx_k}{n}\end{align}$$
- Tempo $O(n)$ per calcolare $e_{ij}$

**Osservazione** : L'algoritmo può essere implementato in modo tale da avere tempo di esecuzione pari a $O(n^2)$
- $\forall i$ : pre-calcola le somme comulative $\sum\limits_{k=1}^ix_k,\sum\limits_{k=1}^iy_k,\sum\limits_{k=1}^ix_k^2,\sum\limits_{k=1}^ix_ky_k$
- Usando le somme comulative, si può calcolare $e_{ij}$ in tempo $O(1)$

----
# Knapsack

**Goal** : Preparare lo "zaino" in modo da massimizzare il valore totale degli oggetti presi
- Ci sono $n$ oggetti : l'oggetto $i$ ha un valore $v_i\gt0$ e peso $w_i\gt0$
- Valore di un sottoinsieme di oggetti = somma dei valori degli oggetti singoli
- Lo "zaino" (knapsack) ha un limite di peso pari a $W$

**Esempio** : Il sottoinsieme $\{1,2,5\}$ ha valore $35\$$ (e peso 10)
**Esempio** : Il sottoinsieme $\{3,4\}$ ha valore $40\$$ (e peso 11)

**Assunzione** : Tutti i valori e i pesi sono integrali

![[Pasted image 20240402102313.png|center|500]]

## Dynamic Programming : Falsa partenza

>[!definition]
>$OPT(i)$ = Valore ottimale per il problema del knapsack con gli elementi $1,\dots,i$

**Goal** : $OPT(n)$

Abbiamo 2 casi
1) $OPT(i)$ non seleziona l'elemento $i$
2) $OPT(i)$ seleziona l'elemento $i$

**Caso 1** : $OPT(i)$ non seleziona l'elemento $i$
- $OPT$ seleziona i migliori tra $\{1,2,\dots,i-1\}$

**Caso 2** : $OPT(i)$ seleziona l'elemento $i$
- Selezionare l'elemento $i$ non implica immediatamente che dobbiamo rigettare gli altri elementi
- Senza sapere quale altro elemento è stato selezionato prima di $i$, non possiamo sapere se abbiamo abbastanza spazio per $i$

**Conclusione** : Servono più sottoproblemi

## Dynamic Programming : Due variabili

>[!definition]
>$OPT(i)$ = Valore ottimale per il problema del knapsack con gli elementi $1,\dots,i$, soggetti al limite di peso $w$

**Goal** : $OTP(n,W)$

Anche qui abbiamo due casistiche

**Caso 1** : $OPT(i)$ non seleziona l'elemento $i$ (possibile perchè $w_i\gt w$)
- $OPT$ seleziona i migliori tra $\{1,2,\dots,i-1\}$ soggetti al peso limite $w$

**Caso 2** : $OPT(i)$ seleziona l'elemento $i$
- Salviamo il valore $v_i$
- Il nuovo peso limite sarà = $w-w_i$
- $OPT(i,w)$ seleziona i migliori tra $\{1,2,\dots,i-1\}$ soggetti al nuovo peso limite

**Equazione di Bellman**

$$OPT(i,w)=\begin{cases}0&i=0\\OPT(i-1,w)&w_i\gt w\\\max\{OPT(i-1,w),v_i+OPT(i-1,w-w_i)\}&\text{altrimenti}\end{cases}$$

### Algoritmo di DP per Knapsack (bottom-up)

![[Pasted image 20240402103330.png|center|500]]

**Esempio**

![[Pasted image 20240402103401.png|center|500]]

#### Tempo di esecuzione

>[!definition]- Teorema
>L'algoritmo di DP per il problema del Knapsack con $n$ elementi e peso massimo $W$, lo risolve in tempo $\Theta(nW)$ e spazio $\Theta(nW)$

**Dimostrazione** :
- Impiega tempo $O(1)$ per le entry della tabella
- CI sono $\Theta(nW)$ entry della tabella
- Dopo aver calcolato il valore della soluzione ottima, possiamo tornare indietro per trovare la soluzione : $$OPT(i,w)\text{ prende l'elemento}\space i\iff M[i,w]\gt M[i-1,w]$$
Ma la domanda fondamentale è la seguente

**Q** : Il tempo di esecuzione dell'algoritmo appena mostrato è polinomiale?

**A** : NO!!, perchè $\Theta(nW)$ non è una funzione polinomiale nella dimensione dell'input, ma si dice `pseudo-polinomiale`

>[!definition]- Algoritmo pseudo-polinomiale
>Un algoritmo il cui tempo di esecuzione risulta essere polinomiale nel valore dell'input (es: il più grande intero presente nell'input) :
>- Efficiente quando i numeri nell'input sono ragionevolmente piccoli
>- Non necessariamente polinomiale nella dimensione dell'input (numeor di bits richiesti per rappresentare l'input)

