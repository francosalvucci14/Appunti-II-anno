
# Union di costo lineare

**find e makeSet** richiedono solo tempo $O(1)$, ma particolari sequenze di union possono essere molto inefficienti

![[appunti asd/mod ii/immagini/Pasted image 20230323142952.png|center|350]]

Se eseguiamo n makeSet, n-1 union come sopra, e m find (in qualsiasi ordine), il **tempo** richiesto **dall'intera sequenza** di operazioni è $O(n+1+2+\dots+(n-1)+m)=O(m+n^2)$ 

# Migliorare la struttura QuickFind : euristiche di bilanciamento nell'operazione union

**Idea** : fare in modo che un nodo/elemento non cambi troppo spesso padre

## Bilanciamento in alberi QuickFind

Nell'unione degli insiemi A e B, attacchiamo gli elementi dell'insieme **di cardinalità minore a quello di cardinalità maggiore**, e se necessario modifichiamo la radice dell'albero ottenuto (cosidetta **union by size**)

**Esempio**

![[appunti asd/mod ii/immagini/Pasted image 20230322154057.png|center|500]]

Dopo l'esecuzione di union(2,3)

![[appunti asd/mod ii/immagini/Pasted image 20230322154144.png|center|500]]

![[appunti asd/mod ii/immagini/Pasted image 20230322154231.png|center|500]]

Esecuzione di union(4,2):

![[appunti asd/mod ii/immagini/Pasted image 20230323143648.png|center|500]]

![[appunti asd/mod ii/immagini/Pasted image 20230323143743.png|center|500]]

### Realizzazione (1/3)

![[Pasted image 20230323143901.png|center|500]]

### Realizzazione (2/3)

![[Pasted image 20230323143926.png|center|500]]

### Realizzazione (3/3)

![[appunti asd/mod ii/immagini/Pasted image 20230323143957.png|center|500]]

$T_{am}$ = tempo per operazione ammortizzato sull'intera sequenza di unioni (vedremo che una singola union può costare $\Theta(n)$, ma l'intersa sequenza di n-1 costa $O(nlog(n))$ )

## Complessità di un'operazione di Union

![[appunti asd/mod ii/immagini/Pasted image 20230323144810.png|center|550]]

### Analisi ammortizzata (1/2)

Vogliamo dimostrare che se eseguiamo m find, n makeSet, e al più n-1 union, il tempo richiesto dall'intera sequenza di operazioni è $O(m+n\cdot\log(n))$ 

Idea della dimostrazione:
- è facile vedere che find e makeSet richiedono tempo $\Theta(m+n)$
- Per analizzare le operazioni di union, ci concentriamo su un singolo nodo e dimostriamo che il tempo speso per tale nodo è $O(\log{n})$, allora in totale, il tempo speso è $O(n\cdot\log{n})$ 

### Analisi ammortizzata (2/2)

Quando eseguiamo una union, per ogni nodo che cambia padre pagheremo tempo costante

Osserviamo ora che ogni nodo può cambiare al più $O(\log{n})$ padri, poichè ogni volta che un nodo cambia padre la cardinalità dell'insieme al quale apparterrà è **almeno doppia** rispetto a quella dell'insieme a cui apparteneva

- all'inizio un nodo è in un insieme di dimensione1
- poi se cambia padre in un insieme di dimensione almeno 2,
- all'i-esimo cambio è in un insieme di dimensione almeno $2^i$

Il tempo speso per un singolo nodo sull'intera sequenza di n union è $O(\log{n})$
L'intera sequenza di operazioni costa
$$O(m+n+n\cdot\log{n})=O(m+n\cdot\log{n})$$
---

# Interval Scheduling

**Interval Scheduling**. Istance $I=\{I_1,\dots I_n\}$
- Job starts at time $s_j$ and finishes at time $f_j\implies I_j=(s_j,f_j)$
- Two jobs are **compatible** if they don't _**overlap**_
- **Goal** : find _**maximum**_ subset A of mutually compatible jobs

![[appunti asd/mod ii/immagini/Pasted image 20230323151649.png|center|500]]

>[!definition]- In modo formale
>- Istanza : $I=\{(s_1,f_1),\dots(s_i,f_i)\}\space s_i,f_i\in\mathbb N$
>- Soluzione ammissibile : un qualunque sottoinsieme $J\subseteq I$
>- Soluzione ottima : $J:\forall i\neq j\in J\implies (s_i,f_i)\space compatibile\space con (s_j,f_j)$
>$(s_i,f_i)-(s_j,f_j)$ sono compatibili se $(s_i,f_i)\cap(s_j,f_j)=\emptyset$

## Interval Scheduling : Greedy Algorithms

**Greedy template**
1. Consider all jobs in some fixed _order_ : Set A $\coloneqq\emptyset$ 
2. For each $j=1,\dots,n$, if $I_j$ is **compatible** with all jobs in A **THEN include** $I_j$ in A

**Possible Ordering Criteria**

- $[\text{Earliest start time}]$ Consider jobs in ascending order of $s_j$
- $[\text{Earliest finish time}]$ Consider jobs in ascending order of $f_j$
- $[\text{Shortest interval}]$ Consider jobs in ascending order of $f_j-s_j$
- $[\text{Fewest conflicts}]$ For each job j, count the **number of conflicting jobs** $c_j$. Schedule in ascending order of $c_j$

**Greedy template**: Consider jobs in some natural order. Take each job provided it's compatible with the ones already taken.

Greedy 1: Earliest Start Time
Does it work ?

1st Step of Problem Solvers: Find bad situations for the Algorithm.

![[appunti asd/mod ii/immagini/Pasted image 20230329090642.png|center]]

Greedy 2: Shortest Interval
Bad Situations ???

![[appunti asd/mod ii/immagini/Pasted image 20230329090727.png|center]]

Greedy 3: FEWEST CONFLICTS
**IDEA**: Use GRAPH MODELLING;

Which is the problem in terms of GRAPHS?

![[appunti asd/mod ii/immagini/Pasted image 20230329090809.png|center]]

**Greedy 4.** Consider jobs in increasing order of finish time. Take each job provided it's compatible with the ones already taken.

![[appunti asd/mod ii/immagini/Pasted image 20230329090857.png|center|550]]

**Implementation**. 
- TIME= $O(n\log n)$.
- Remember job $j^\star$ that was added last to A.
- Job j is compatible with A $\iff$ $s_j\geq f_{j^\star}$.

Let $i_1, i_2,\dots i_k$denote set A of jobs selected by _Greedy_.
Let $j_1, j_2, \dots j_m$ denote set of jobs in **any** solution (ordered w.r.t. finish time).

>[!definition]- Lemma 1 (Greedy Stays Ahead)
>For any $r = 1,\dots, k$ it holds
>$$f(i_r)\leq f(j_r)$$
>Proof. By induction on r. r =1 is trivial.

