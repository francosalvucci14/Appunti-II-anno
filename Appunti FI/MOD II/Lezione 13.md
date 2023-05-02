# Specifiche classi di complessità

Siamo al paragrafo 6.6, pronti a definire alcune fra le più rilevanti classi di complessità: 	

$P =\bigcup_{k\in\mathbb N}DTIME[n^k]$
- la classe dei linguaggi _**decidibili in tempo deterministico polinomiale;**_

$NP =\bigcup_{k\in\mathbb N}NTIME[n^k]$
- la classe dei linguaggi _**accettabili in tempo non deterministico polinomiale;**_
	- ma anche **decidibili** in tempo non deterministico polinomiale!

$PSPACE =\bigcup_{k\in\mathbb N}DSPACE[n^k]$
- la classe dei linguaggi **_decidibili in spazio deterministico polinomiale_**; 

$NPSPACE =\bigcup_{k\in\mathbb N}NSPACE[n^k]$
- la classe dei linguaggi **_accettabili in spazio non deterministico polinomiale;_** 
	- ma anche **decidibili** in spazio non deterministico polinomiale!

$EXPTIME =\bigcup_{k\in\mathbb N}DTIME[2^{p(n,k)}]$
- la classe dei linguaggi **_decidibili in tempo deterministico esponenziale_** ove l’esponente che descrive la funzione limite è un polinomio in n di grado k – indicato come p(n,k)

$NEXPTIME =\bigcup_{k\in\mathbb N}NTIME[2^{p(n,k)}]$
- la classe dei linguaggi **_accettabili in tempo non deterministico esponenziale_** (ove l’esponente che descrive la funzione limite è un polinomio in n di grado k); 
- ma anche decidibili in tempo non deterministico esponenziale!

Infine, una classe di complessità di funzioni: la classe delle funzioni (totali) calcolabili in tempo deterministico polinomiale: 																																$$FP=\bigcup_{k\in\mathbb N} \{ f :\Sigma_1^\star \to\Sigma_2^\star : \exists T  \text{ che calcola f e}, \forall x\in\Sigma_1^\star, dtime(T,x) \in O(|x|^k)\}$$
P ⊆ NP , PSPACE ⊆ NPSPACE e EXPTIME ⊆ NEXPTIME
conseguenza diretta del Teorema 6.8: una macchina deterministica è una macchina non deterministica con grado di non determinismo 1

## Proprietà - Corollario 6.2

$P \subseteq NP , PSPACE \subseteq NPSPACE , EXPTIME \subseteq NEXPTIME$
- conseguenza diretta del Teorema 6.8: una macchina deterministica è una macchina non deterministica con grado di non determinismo 1

$P \subseteq PSPACE , NP \subseteq NPSPACE$
- sono conseguenza diretta del Teorema 6.9: per ogni funzione totale e calcolabile f					$DTIME[f(n)] \subseteq DSPACE[f(n)]$ e $NTIME[f(n)] \subseteq NSPACE[f(n)]$

$PSPACE \subseteq EXPTIME , NPSPACE \subseteq NEXPTIME$
- sono conseguenza diretta del Teorema 6.10: per ogni funzione totale e calcolabile f			$DSPACE[f(n)] \subseteq DTIME[2^{O(f(n))}]$ e $NSPACE[f(n)] \subseteq NTIME[2^{ O(f(n))}]$

$NP \subseteq EXPTIME$
- conseguenza diretta del Teorema 6.17: per ogni funzione time-constructible f 								$NTIME[f(n)] \subseteq DTIME[2^{O(f(n))}]$
- e i polinomi sono funzioni time-constructible

## Relazioni interessanti

Tutte le relazioni fra classi complessità che abbiamo, fino ad ora, dimostrato sono inclusioni improprie.

Ossia, per ciascuna di quelle relazioni non siamo in grado di dimostrare né l’inclusione propria né la coincidenza delle due classi che la costituiscono. 

Ad esempio, sappiamo che 
- tutti i linguaggi che sono in PSPACE sono anche in EXPTIME
- tutti i linguaggi che sono in P sono anche in NP

Ma non sappiamo rispondere alle seguenti domande
- non sarà forse che tutti i linguaggi in EXPTIME sono anche in PSPACE? Ossia, che 			PSPACE = EXPTIME?
- Oppure, esiste almeno un linguaggio in EXPTIME che non può essere deciso in spazio polinomiale? Ossia, che PSPACE  EXPTIME

Si tratta di relazioni deboli
- e sarebbe tremendo se si dimostrasse che tutte quelle inclusioni improprie fossero, in effetti, delle uguaglianze!
- Non saremmo affatto in grado di classificare i problemi in “facili” e “difficili”

### L'unica relazione di contenimento stretto

In effetti, uno strumento che dimostra l’inclusione stretta fra classi di complessità ce l’abbiamo: il Teorema di gerarchia temporale:

Teorema 6.15 (Teorema di gerarchia temporale):
Siano $f :\mathbb N\to\mathbb N , g :\mathbb N\to\mathbb N$ due funzioni tali che f è time-constructible e $$\lim_{n\to\infty}\frac{g(n)\cdot\log(g(n))}{f(n)}=0$$
Allora, $DTIME[g(n)]\subset  DTIME[ f (n)]$ ossia, esiste un linguaggio L tale che $L\in   DTIME[ f(n)]$ e $L\not\in  DTIME[g(n)]$. 

Dimostriamo ora il seguente caso particolare del Teorema di gerarchia temporale: 																				           

>[!definition]- Teorema 6.18: 
>$P\subset EXPTIME$

La dimostrazione consiste nel costruire un particolare linguaggio $L \subseteq \{0,1\}^\star$ tale che : 
- L è deciso in tempo deterministico $t(n) = n2^{2n}$ – cioè $L \in DTIME[n2^{2n}]$
- e, contemporaneamente,$L \not\in DTIME[2^n]$ . 

Questo dimostrerà che $DTIME[2^n]\subset DTIME[n2^{2n}]$

Quindi, poiché: 
$P \subseteq DTIME[2^n]$ e $DTIME[n2^{2n}] \subseteq DTIME[2^{n}2^{2n}] \subseteq EXPTIME$
avremo: $P \subseteq DTIME[2^n]\subset   DTIME[n2^{2n}] \subseteq EXPTIME$

ossia,  avremo dimostrato che $P\subseteq  EXPTIME$

Definiamo, allora, il seguente linguaggio:
$$\begin{align}L = \{ &z  \in\{0,1\}^\star : z = 1^i0x \\&\land x \text{ è la codifica binaria di una parola } k \in\mathbb N \\&\text{ che è la codifica  di una macchina di Turing Tk definita sull’alfabeto \{0, 1\}}\\& \land T_k (z)\space \text{termina in }2^{2|z|}\text{ passi}\\& \land T_k(z)\text{ rigetta}\}\end{align}$$
Chiariamo:
- “$z = 1^i 0 x$ “ significa che z inizia con una sequenza di ‘1’ (lunga quanto gli pare)
- “e  x è la codifica binaria di una parola $k\in\mathbb N$ che è la codifica di una macchina di Turing deterministica ad un nastro di tipo riconoscitore $T_k$ definita sull’alfabeto $\{0, 1\}$” significa che la parola (binaria) che inizia a destra del primo ‘0’ di z è un intero k, che è la codifica di una macchina di Turing $T_k$
- “e $T_k (z)$ termina in $2^{2|z|}$ passi e $T_k(z)$ rigetta” significa che, se alla macchina $T_k$ si dà in input z (al cui interno è codificato, in binario, k), la computazione $T_k (z)$ termina in $2^{2|z|}$ passi , e termina nello stato di rigetto 

Non vi ricorda un po’ l’halting problem?


