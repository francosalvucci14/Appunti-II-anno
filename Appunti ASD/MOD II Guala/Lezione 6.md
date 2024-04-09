
```table-of-contents
title: 
style: nestedList # TOC style (nestedList|inlineFirstLevel)
minLevel: 0 # Include headings from the specified level
maxLevel: 0 # Include headings up to the specified level
includeLinks: true # Make headings clickable
debugInConsole: false # Print debug info in Obsidian console
```

# Paradigmi Algoritmici

**Greedy** : Processare l'input in un certo ordine, prendendo decisioni irrevocabili

**Divide-et-Impera** : Dividere il problema in sottoproblemi `indipendenti`; risolvere ogni sottoproblema; combinare le soluzioni dei sottoproblemi per formare la soluzione del problema originale

**Dynamic Programming** : Dividere il problema in una serie di sottoproblemi `sovrapposti` ; combinare la soluzione in sottoproblemi più piccoli per formare la soluzione del sottoproblema più grande

----

# Weighted Interval Scheduling

- Job $j$ che inizia al tempo $s_j$, e finisce al tempo $f_j$, che ha un peso $w_j\gt0$
- Due job si dicono **compatibili** se sono si sovrappongono
- **Goal** : Trovare il sottoinsieme di peso massimo di job mutualmente compatibili

![[Pasted image 20240327095836.png|center|500]]

Dato che il problema è l'IS con pesi sui job, possiamo pensare di usare lo stesso algoritmo usato per l'IS, ovvero l'algoritmo `EFTF [Earliest-Finish-Time-First]`

## Algoritmo Greedy EFTF

**Recall** : L'algoritmo greedy è corretto se tutti i pesi sono a 1

**Osservazione** : L'algoritmo greedy fallisce miseramente per la versione con pesi $\neq1$

![[Pasted image 20240327100033.png|center|500]]

Come si può vedere dall'esempio, l'algoritmo EFTF va a scegliere i job a e h, andando a guadagnare 2, quando invece avrebbe dovuto scegliere il job b, andando cosi a guadagnare 999

Cerchiamo di migliorare la situazione

**Convenzione** : Job sono ordinati in ordine crescente di finish time $f_1\leq f_2\leq\dots f_n$

>[!definition]- $p(j)$
>$p(j)$ = più grande indice $i\lt j$ tale che il job $i$ è compatibile con $j$

**Esempio** : $p(8)=1,p(7)=3,p(2)=0$

![[Pasted image 20240327100516.png|center|500]]

## Dynamic Programming : Scelta binaria

>[!definition]- OPT(j)
>$OPT(j)$ = peso massimo di ogni sottoinsieme di job mutualmente compatibili per il sottoproblema che consiste nei soli job $1,2,\dots j$

**Goal** : $OPT(n)$ = peso massimo di ogni sottoinsieme di job mutualmente compatibili

Abbiamo due casistiche

**Caso 1** : $OPT(j)$ non sceglie il job $j$
- CI deve essere una soluzione ottima al problema che consiste nei rimanenti job $1,2,\dots j-1$

**Caso 2** : $OPT(j)$ sceglie il job $j$
- Prendiamo il profitto $w_j$
- Non possiamo usare job incompatibili ${p(j)+1,p(j)+2,\dots j-1}$
- Deve includere la soluzione ottimale al problema che consiste nel rimanenti job compatibili $1,2,\dots p(j)$

**Equazione di Bellman** : $$OPT(j)=\begin{cases}0&j=0\\\max\{OPT(j-1),w_j+OPT(j-2)\}&j\gt0\end{cases}$$
### Bottom-Up Dynamic Programming (Table-base)

![[Pasted image 20240327101301.png|center|500]]

**Tempo di esecuzione** : La versione Bottom-Up richiede tempo $O(n\log(n))$
- Ordinare tramite finish time : $O(n\log(n))$ usando il MergeSort
- Calcolare $p[j]$ per ogni $j$ : $O(n\log(n))$ usando il binary search
- Il ciclo for richiede tempo $O(n)$

### Ricorsione aka Brute Force

![[Pasted image 20240327101608.png|center|500]]

Il tempo di esecuzione dell'algoritmo è descritto dalla seguente equazione di ricorrenza

$$T(n)=\begin{cases}\Theta(1)&n=1\\2T(n-1)+\Theta(1)&n\gt1\end{cases}\implies T(n)=\Theta(2^n)$$
**Osservazione** : L'algoritmo ricorsivo è spettacolarmente lento a causa dei sottoproblemi che si sovrappongono $\implies$ algoritmo esponenziale

**Esempio** : Numero di chiamate ricorsive per una famiglia di istanze "stratificate" cresce come la sequenza di Fibonacci

![[Pasted image 20240327101948.png|center|500]]

### Top-down Dynamic Programming (Memoization)

**Memoization** :
- Salva il risultato del sottoproblema $j$ in $M[j]$
- Usa $M[j]$ per evitare di risolvere il sottoproblema $j$ più di una volta

![[Pasted image 20240327102354.png|center|500]]

**Claim** : La versione "Memoizzata" dell'algoritmo richiede tempo $O(n\log(n))$

**Pf.**
- Ordinare tramite finish time : $O(n\log(n))$ usando il MergeSort
- Calcolare $p[j]$ per ogni $j$ : $O(n\log(n))$ usando il binary search
- `M-ComputeOPT(j)` : Ogni invocazione richiede tempo $O(1)$ e inoltre :
	1) Ritorna un valore inizializzato $M[j]$
	2) Inizializza $M[j]$ ed esegue due chiamate ricorsive
- Misura di progresso $\phi$ = # voci inizializzate in $M[1\dots n]$
	- Inizialmente $\phi=0$; Totale $\phi\leq n$
	- Incrementa $\phi$ di 1 $\implies\leq 2n$ chiamate ricorsive
- Tempo totale di esecuzione di `M-Compute-OPT(n)` è $O(n)$

**Q** : L'algoritmo di DP calcola il valore della soluzione ottima. Come troviamo la soluzione ottima?
**A** : Eseguiamo una seconda passata chiamando l'algoritmo `Find-Solution(n)`

![[Pasted image 20240327103431.png|center|500]]

Numero di chiamate ricorsive $\leq n\implies O(n)$

## Memoization (top-down) vs Table-base (bottom-up)

| Memoization                                                           | Table-base                                                                 |
| --------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| ApproccioTop-Down                                                     | **Più difficile da "afferrare"**                                           |
| Più facile indicizzare i sottoproblemi da altri oggetti (es. insieme) | **Bisogna indicizzare i sottoproblemi con gli interi**                     |
| Calcola solo i sottoproblemi necessari                                | **Calcola sempre tutti i sottoproblemi**                                   |
| **Chiamate delle funzioni sopraelevate**                              | Nessuna ricorsione. Più efficiente                                         |
| **La complessità temporale è più difficile da analizzare**            | La complessità temporale è più facile da analizzare, codice corto e pulito |

----
# Longest Increasing Subsequence

Una piccola analogia

Robert vuole bere il più possibile

- Robert cammina lungo una via e incontra $n$ taverne $t_1,t_2,\dots t_n$ in ordine
- Quando Robert incontra una taverna $t_i$, lui si può fermare a bere o no
- Il vino servito nella taverna $t_i$ ha gradazione $s_i$
- La gradazione dei drinks di Robert deve incrementarsi ogni volta
- **Goal** : Calcola il massimo numero di fermate di Robert

**Esempio**

![[Pasted image 20240327112742.png|center|500]]
![[Pasted image 20240327112801.png|center|500]]

Soluzione ottima : 6

Questo problema è conosciuto col nome di **Longest Increasing Subsequence**

## Algoritmo DP : Prima prova

- **Definizioni dei sottoproblemi** : $OPT[i]$ : Lunghezza del LIS di $S[1],\dots S[i]$
- **Caso base** $$OPT[1]=1$$
- **Soluzione** $$OPT[n]$$
- Formula ricorsiva ???

## Algoritmo DP : Seconda prova

**Tip** : Molte volte aggiungere costanti al problema può aiutare!

$OPT[i]$ : Lunghezza del LIS di $S[1],\dots S[i]$ che finisce con $S[i]$

Vedi esempio qui -> [Esempio](https://www.mat.uniroma2.it/~guala/05_DP_II_2023.pdf#page=22)

- **Definizione di sottoproblemi** : $OPT[i]$ : Lunghezza del LIS di $S[1],\dots S[i]$ che finisce con $S[i]$
- **Caso base** : $$OPT[1]=1$$
- **Soluzione** : $$\max_{i=1,2,\dots,n}OPT[i]$$
- **Ordine dei sottoproblemi** $$OPT[1],OPT[2],\dots OPT[n]$$
- **Formula ricorsiva** $$OPT[i]=1+\max\{0,\max_{j=1,2,\dots,i-1}OPT[j]\}$$
Ora vediamo lo pseudocodice dell'algoritmo

![[Pasted image 20240327113940.png|center|500]]

**Tempo di esecuzione**
- Ogni $OPT[i]$ viene calcolare in tempo $O(i)=O(n)$
- tempo totale $O(n^2)$