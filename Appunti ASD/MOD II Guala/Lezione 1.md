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

## Algoritmi Greedy per IS

**Template Greedy** : Considerare i job in un certo ordine naturale
Prendo ogni job che risulta essere compatibile con il job preso in precedenza

Ci sono 4 tipi di ordinamento naturale, e sono :

- **Earliest Start Time** : Consideriamo i job ordinati tramite $s_j$
- **Earliest Finish Time** : Consideriamo i job ordinati tramite $f_j$
- **Shortest Interval** : Consideriamo i job ordinati tramite il valore $f_j-s_j$
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

**Proposizione** : L'algoritmo EFTF viene eseguito in tempo $O(nlog(n))$

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

