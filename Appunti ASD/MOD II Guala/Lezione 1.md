
```table-of-contents
title: 
style: nestedList # TOC style (nestedList|inlineFirstLevel)
minLevel: 0 # Include headings from the specified level
maxLevel: 0 # Include headings up to the specified level
includeLinks: true # Make headings clickable
debugInConsole: false # Print debug info in Obsidian console
```

# Interval Scheduling

Job $j$ inizia al tempo $s_j$ e finisce al tempo $f_j$
Due job si dicono **compatibili** se non si sovrappongono l'uno con l'altro
Goal : Trovare il massimo sottoinsieme (numero) di job mutualmente compatibili

![[Pasted image 20240306103318.png|center|500]]

>[!definition]-  Definizione formale
>**Input** :
>- Insieme di n intervalli $I_1,\dots,I_n$
>- L'intervallo $I_i$ inizia al tempo $s_i$ e finisce al tempo $f_i$
>
>**Soluzione ammissibile** :
>- Un sottoinsieme $S$ di intervalli che sono mutualmente compatibili, per esempio $$\forall I_i,I_j\in S,I_i\space\text{non si sovrappone a }I_j$$
>
>**Misura (da massimizzare)**
>- Numero di intervalli schedulati, ovvero la cardinalità di $S$

## Algoritmo Greedy per IS

**Template Greedy** : Considerare i job in un certo ordine naturale
Prendo ogni job che risulta essere compatibile con il job preso in precedenza

Ci sono 4 tipi di ordinamento naturale, e sono :

- **Earliest Start Time** : Consideriamo i job ordinati tramite $s_j$
- **Earliest Finish Time** : Consideriamo i job ordinati tramite $f_j$
- **Shortest Interval** : Consideriamo i job ordinati traAmite il valore $f_j-s_j$
- **Fewest Conflicts** : Per ogni job $j$, consideriamo il numero di job che vanno in conflitto con lui, detti $c_j$. Ordiamo i job in base al valore $c_j$

Possiamo dimostrare che il secondo metodo porta alla soluzione ottima, mentre gli altri 3 no

Lo dimostriamo tramite controesempi per i restanti 3 tipi

![[Pasted image 20240306104307.png|center|500]]

Ora mostriamo un'algoritmo per il secondo tipo di ordinamento

![[Pasted image 20240306104643.png|center|500]]

Per vedere la demo di come funziona l'algoritmo, si veda questa pagina
[Demo algoritmo per IS](https://www.mat.uniroma2.it/~guala/01_Interval_scheduling_2023.pdf#7)

### Analisi algoritmo greedy $[EFTF]$

Diamo prima di tutto una proposizione, che ci dice in quanto tempo viene eseguito questo algoritmo

>[!info]- **Proposizione**
>L'algoritmo EFTF può essere implementato in tempo $O(nlog(n))$

Come?

- L'ordinamento si fa tranquillamente in tempo $O(nlog(n))$ tramite MergeSort
- Teniamo traccia dell'ultimo job che p stato aggiunto all'insieme $S$, ovvero il job $j^\star$
- Il job $j$ è compatibile con $S\iff s_j\geq f_{j^\star}$

Diamo adesso un lemma, e poi lo dimostriamo

Prima di tutto :

- Siano $i_1,\dots,i_k$ un'insieme di job selezionati dall'algoritmo greedy `EFTF`
- Siano $j_1,\dots,j_m$ un'insieme di job nella soluzione ottimale

Denotiamo con $f(i_r)$ il finish time del job $i_r$

>[!warning]- Lemma (Greedy Stays Ahead)
>$\forall r=1,2,\dots,k$, si ha che $f(i_r)\leq f(j_r)$

**Dimostrazione per induzione**
- $r=1$ ovvio
- $r\gt1$ : ![[Pasted image 20240306105813.png|center|600]]
Il job $i_r$ deve finire necessariamente prima del job $j_r$ (quindi $j_r$ è disponibile per l'algoritmo greedy)

Adesso diamo l'enunciato di un teorema molto importante

>[!definition]- Teorema
>L'algoritmo greedy EFTF è ottimo

**Dimostrazione per assurdo**
- Siano $i_1,\dots,i_k$ un'insieme di job selezionati dall'algoritmo greedy `EFTF`
- Siano $j_1,\dots,j_m$ un'insieme di job nella soluzione ottimale
- Assumiamo che il greedy non sia ottimo
- Allora deve essere necessariamente $m\gt k$

![[Pasted image 20240306110149.png|center]]

Se $m\gt k$, allora deve esistere necessariamente un altro job, detto $j_{k+1}$, nella soluzione ottimale.
Tale job però risulta compatabile con tutti gli altri job della soluzione greedy, perchè si può notare che il finish time del job $j_{k+1}$ rispetta la seguente equazione : $f_{j_{k+1}}\geq f_{i_k}$ , e di conseguenza il job $j_{k+1}$ deve essere necessariamente prso dall'algoritmo greedy, il che è assurdo perchè abbiamo assunto che il numero di job scelti dal greedy sono $k$

---

# Interval Partitioning

Il problema è molto simile al problema dell'Interval Scheduling, l'unica differenza è che i job, qui chiamati `partizioni`, devono essere schedulati in delle classi, e dobbiamo trovare il minimo numero di classi necessarie per schedulare tutte le n partizioni

Vediamolo

La partizione $j$ inizia al tempo $s_j$ e finisce al tempo $f_j$
Goal : Trovare il minimo numero di classi che servono per schedulare tutte le partizioni in modo tale da avere che due partizioni non occorrono nella stessa classe contemporaneamente

**Esempio**

Questa schedule usa 4 classi per schedulare 10 partizioni

![[Pasted image 20240306111544.png|center|600]]

Vediamo un'altro esempio, questo usa 3 classi per schedulare 10 partizioni

![[Pasted image 20240306111647.png|center|600]]

è facile notare che questa soluzione è la soluzione ottima

Diamo ora la definizione formale di questo problema

>[!definition]- Definizione formale
>**Input** :
>- Insieme di n intervalli $I_1,\dots,I_n$
>- L'intervallo $I_i$ inizia al tempo $s_i$ e finisce al tempo $f_i$
>
>**Soluzione Ammissibile** :
>- Una partizione degli intervalli in sottoinsiemi, chiamati $C_1,\dots,C_d$ tale che ogni $C_i$ contiene intervalli mutualmente compatibili
>
>**Misura (da minimizzare)** :
>- Numero di classi usate, ovvero il numero $d$

## Algoritmo greedy per IP

**Template Greedy** Considerare gli intervalli in un certo ordine naturale. Assegnamo ognuno di loro ad una classe disponibile (quale?). Creaiamo una nuova classe se nessuna è disponibile

Anche qui ci sono 4 tipi di ordinamento naturale degli intervalli, che sono gli stessi del problema IS

- **Earliest Start Time** : Consideriamo i job ordinati tramite $s_j$
- **Earliest Finish Time** : Consideriamo i job ordinati tramite $f_j$
- **Shortest Interval** : Consideriamo i job ordinati tramite il valore $f_j-s_j$
- **Fewest Conflicts** : Per ogni job $j$, consideriamo il numero di job che vanno in conflitto con lui, detti $c_j$. Ordiamo i job in base al valore $c_j$

Possiamo dimostrare che il primo metodo genera la soluzione ottima, mentre gli altri 3 no

Diamo un controesempio per i 3 tipi di ordinamento che non portano alla soluzione ottima

![[Pasted image 20240306112603.png|center|400]]

Vediamo il codice dell'algoritmo che permette di risolvere il problema dell'Interval Partitioning

![[Pasted image 20240306112715.png|center|500]]

Per vedere la demo dell'algoritmo, rimando alla seguente pagina web
[Demo algoritmo ESTF](https://www.mat.uniroma2.it/~guala/01_Interval_scheduling_2023.pdf#36)

### Analisi algoritmo  greedy $[ESTF]$

>[!info]- Proposizione
>L'algoritmo greedy ESTF può essere implementato in tempo $O(nlog(n))$

**Dimostrazione**

- Ordinamento tramite starting time può essere fatto in tempo $O(nlog(n))$ tramite MergeSort
- Salviamo le classi in una **coda con priorità** (chiave = finish time dell'ultimo intervallo)
	- Per creare una nuova classe, eseguiamo l'operazione di Insert della coda
	- Per schedulare l'intervallo $j$ nella classe $k$, eseguiamo l'operazione di Increase-Key della classe $k$ in $f_j$
	- Per vedere se l'intervallo $j$ è compatibile con una qualunque classe, eseguiamo prima l'operazione Find-Min, poi confrontiamo il valore $s_j$ con il valore di Find-Min
- Il numero totale di operazioni è $O(n)$, ognuna di costo $O(log(n))$

#### Lower Bound della soluzione ottima

Diamo prima la definizione di **depth (profondità)**

>[!definition]- Depth (profondità)
>La **depth** di un insieme di intervalli aperti è il massimo numero di intervalli che contengono un determinato punto

**Osservazione Chiave** : Numero di classi necessarie $\geq$ depth

Q. Il numero minimo di classi necessarie equivale sempre alla profondità?
A. Sì! Inoltre, l'algoritmo ESTF trova una pianificazione il cui numero di classi è pari alla profondità.

**Esempio di depth**

![[Pasted image 20240306115451.png|center|600]]

### Ritornando all'analisi dell'algoritmo $[ESTF]$

**Osservazione** : L'algoritmo ESTF non schedula mai due intervalli incompatibili nella stessa classe

Diamo ora l'enunciato del teorema

>[!definition]- Teorema
>L'algoritmo ESTF è ottimo

**Dimostrazione**
- Sia $d$ il numero di classi che l'algoritmo alloca
- La classe $d$ è aperta perchè abbiamo bisogno di schedulare l'intervallo, detto $j$, che è incompatibile con gli altri intervalli nelle restanti $d-1$ classi
- Quindi, questi $d$ intervalli devono finire dopo $s_j$
- Dato che abbiamo ordinato tramite starting time, ognuno di questi intervalli incompatibili iniziano non più tardi di $s_j$
- Quindi, abbiamo $d$ intervalli che si sovrappongono al tempo $s_j+\epsilon$
- Dall'osservazione chiave $\to$ tutte le schedule usano $\geq d$ classi