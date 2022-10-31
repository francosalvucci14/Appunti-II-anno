# Automi a Stati Finiti

## Automi a Stati Finiti Deterministici
_Def_
Un **automa a stati finiti deterministico** (ASFD) è una quintupla $\mathcal A=\langle\Sigma,Q,\delta,q_0,F\rangle$, dove:
- $\Sigma=\lbrace a_1,...,a_n\rbrace$ è l'**alfabeto** di input (corrisponde all'insieme dei simboli terminali nelle grammatiche)
- $Q=\lbrace q_0,...,q_m\rbrace$ è un insieme finito e non vuoto di **stati**
- $q_0\in Q$ è lo **stato iniziale**
- $F\subseteq Q$ è un insieme di **stati finali**
- $\delta:Q\times\Sigma\to Q$ è la **funzione (totale) di transizione** che ad ogni coppia $\langle\text{stato},\text{carattere in input}\rangle$ associa uno stato successivo.

>**Oss** Un ASFD è la specializzazione più semplice e di fatto è il modello più debole dal punto di vista espressivo e computazionale

![[appunti fi/immagini/Pasted image 20221031113627.png|center|600]]

Si assume che il nastro sia read-only, e può essere letto solo da sinistra verso destra

### Funzione di transizione

![[appunti fi/immagini/Pasted image 20221031113922.png|center|500]]

La funzione $\delta$ si rappresenta con una tabella, come in figura, dove i valori di $Q$ sono le righe, mentre i valori di $\Sigma$ sono le colonne.
Quindi questa tabella ci dice che
- $\delta(q_0,a)=q_0||\delta(q_0,b)=q_1$
- $\delta(q_1,a)=q_2$
- etc...
La tabella prende nome di **tabella di transizione**
Il grafo prende nome di **grafo di transizione**:
- i nodi sono gli stati
- nell'insieme dei nodi c'è un nodo particolare, che è il nodo iniziale (indicato con una freccia entrante etichettata con "start")
- ci sono poi nodi speciali che corrispondono agli stati finali, indicati con la notazione grafica doppia cornice intorno (es. $q_1$)

Esempio:
$\delta(q_i,a_j)=q_k$ viene rappresentato con 
![[appunti fi/immagini/Pasted image 20221031115625.png|center|400]]

### Configurazione di un ASF

Dato un automa a stati finiti $\mathcal A=\langle\Sigma,Q,\delta,q_0,F\rangle$, una configurazione di $\mathcal A$ è una coppia (q,x), con $q\in Q$ e $x\in\Sigma^\star$
Una configurazione $\langle q,x\rangle,q\in Q\:e\:x\in\Sigma^\star$, di $\mathcal A$, è detta:
- **iniziale** se $q=q_0$
- **finale** se $x=\epsilon$
- **accettante** se $x=\epsilon$ e $q\in F$

### Transizioni di un ASFD

Dato un ASFD $\mathcal A=\langle\Sigma,Q,\delta,q_0,F\rangle$ e due configurazioni $(q,x)$ e $(q',y)$ di $\mathcal A$, avremo che $(q,x)\vdash_{\mathcal A}(q',y)$ se e solo se valgono le due condizioni:

1. $x=ay$, per un qualche $a\in\Sigma$
2. $\delta(q,a)=q'$

### Accettazione da un ASFD

Dato un automa a stati finiti deterministico $\mathcal A=\langle\Sigma,Q,\delta,q_0,F\rangle$, una stringa $x\in\Sigma^\star$ è accettata da $\mathcal A$ se e solo se:
$$(q_o,x)\vdash_{\mathcal A}^\star (q,\epsilon)$$
con $q\in F$

Possiamo definire il linguaggio riconosciuto da $\mathcal A$ come
$$L(\mathcal A)=\lbrace x\in\Sigma^\star|(q_0,x)\vdash_{\mathcal A}^\star(q,\epsilon),q\in F\rbrace$$

**Esempio**

La stringa aab è accettata dall'automa a stati finiti deterministico
![[appunti fi/immagini/Pasted image 20221031130503.png|center|500]]

Infatti, a partire dalla configurazione iniziale $(q_0,aab)$ l'automa raggiunge la configurazione di accettazione $(q_1,\epsilon)$ per mezzo della computazione 
$$(q_0,aab)\vdash(1_0,ab)\vdash(q_0,b)\vdash(q_1,\epsilon)$$

### Funzione di transizione estesa
Dato un automa a stati finiti deterministico $\mathcal A=\langle\Sigma,Q,\delta,q_0,F\rangle$, la sua **funzione di transizione estesa**
$$\overline\delta:Q\times\Sigma^\star\to Q$$
è definita come la chiusura transitiva della $\delta$:
$$\overline\delta(q,\epsilon)=q$$
$$\overline\delta(q,xa)=\delta(\overline\delta(q,x),a)$$
dove $a\in\Sigma,x\in\Sigma^\star$
Una stringa $x\in\Sigma^\star$ è accettata da $\mathcal A=\langle\Sigma,Q,\delta,q_0,F\rangle$ se e solo se $\overline\delta(q_0,x)\in F$
