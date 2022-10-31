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

#### Accettazione da un ASFD

Dato un automa a stati finiti deterministico $\mathcal A=\langle\Sigma,Q,\delta,q_0,F\rangle$, una stringa $x\in\Sigma^\star$ è accettata da $\mathcal A$ se e solo se:
$$(q_o,x)\vdash_{\mathcal A}^\star (q,\epsilon)$$
con $q\in F$

Possiamo definire il linguaggio riconosciuto da $\mathcal A$ come
$$L(\mathcal A)=\lbrace x\in\Sigma^\star|(q_0,x)\vdash_{\mathcal A}^\star(q,\epsilon),q\in F\rbrace$$

**Esempio**

La stringa aab è accettata dall'automa a stati finiti deterministico
![[appunti fi/immagini/Pasted image 20221031130503.png|center|500]]

Infatti, a partire dalla configurazione iniziale $(q_0,aab)$ l'automa raggiunge la configurazione di accettazione $(q_1,\epsilon)$ per mezzo della computazione 
$$(q_0,aab)\vdash(q_0,ab)\vdash(q_0,b)\vdash(q_1,\epsilon)$$

#### Funzione di transizione estesa
Dato un automa a stati finiti deterministico $\mathcal A=\langle\Sigma,Q,\delta,q_0,F\rangle$, la sua **funzione di transizione estesa**
$$\overline\delta:Q\times\Sigma^\star\to Q$$
è definita come la chiusura transitiva della $\delta$:
$$\overline\delta(q,\epsilon)=q$$
$$\overline\delta(q,xa)=\delta(\overline\delta(q,x),a)$$
dove $a\in\Sigma,x\in\Sigma^\star$
Una stringa $x\in\Sigma^\star$ è accettata da $\mathcal A=\langle\Sigma,Q,\delta,q_0,F\rangle$ se e solo se $\overline\delta(q_0,x)\in F$

**esempio**
$\delta(q,a)$
$\overline\delta(q,aab)$

### Linguaggio riconosciuto da un ASFD

Il **linguaggio riconosciuto** da un automa a stati finiti deterministico $\mathcal A$ è l'insieme
$$L(\mathcal A)=\lbrace x\in\Sigma^\star|\delta(q_0,x)\in F\rbrace$$
**esempio 1**
vedi file su notability.

### Funzione di transizione parziale

La funzione di transizione $\delta$ è stata definita come totale
Ogni ASFD $\mathcal A=\langle\Sigma,Q,\delta,q_0,F\rangle$ con funzione di transizione $\delta$ non totale può essere trasformato in un ASFD $\mathcal A'=\langle\Sigma,Q',\delta',q_0,F\rangle$ con funzione di transizione totale ed equivalente, ponendo $Q'=Q\cup\lbrace \overline q\rbrace$ e $\overline\delta$ tale che:

1. Se $\delta(q,a),q\in Q$ è definito allora $\delta'(q,a)=\delta(q,a)$
2. Se $\delta(q,a),\in Q$ non è definito allora $\delta'(q,a)=\overline q$
3. $\delta'(\overline q,a)=\overline q$ per ogni $a\in\Sigma$

### Linguaggi decisi da un ASFD

Insieme $\mathcal R$ dei linguaggi decisi da automi a stati finiti deterministici:
$$\mathcal R=\lbrace L\subseteq\Sigma^\star|\exists\:ASFD\:\mathcal A\:tale\:che\:L=L(\mathcal A)\rbrace$$
Questa classe di linguaggi coincide con quella dei linguaggi generati dalle grammatiche di tipo 3 e con quella dei linguaggi definiti da espressione regolari.

## Automi a Stati Finiti Non Deterministici

_Def_
Un **automa a stati non deterministico** è una quintupla $\mathcal A_N=\langle\Sigma,Q,\delta_N,q_0,F\rangle$, in cui:
- $\Sigma=\lbrace a_1,...,a_n\rbrace$ è l'**alfabeto** di input (corrisponde all'insieme dei simboli terminali nelle grammatiche)
- $Q=\lbrace q_0,...,q_m\rbrace$ è un insieme finito e non vuoto di **stati**
- $q_0\in Q$ è lo **stato iniziale**
- $F\subseteq Q$ è un insieme di **stati finali**
- $\delta_N:Q\times\Sigma\to\mathcal P(Q)$ è una funzione (parziale), detta **funzione di transizione**, che ad ogni coppia $\langle stato,carattere\rangle$ su cui è definita associa un sottoinsieme di $Q$ (eventualmente vuoto)

**Esempio funzione di transizione ASFND**

![[appunti fi/immagini/Pasted image 20221031172410.png|center|400]]

**Esempio**

Un ASFND può essere descritto, così come un ASFD, tramite un grafo di transizione

![[appunti fi/immagini/Pasted image 20221031172800.png|center|500]]

### Computazioni di un ASFND

Un automa a stati finiti non deterministico definisce, data una stringa in input, un insieme di computazioni

Alternativamente, possiamo considerare che l'automa esegue una sola **computazione non deterministica** nel corso della quale, per ogni carattere letto, assume non uno solo, ma un insieme di stati attuali e transita, ad ogni nuovo carattere, non da stato a stato ma da un insieme di stati ad un insieme di stati

**Esempio**
Usando la stringa bbab e il grafo dell'esempio precedente abbiamo che
$$\lbrace q_0\rbrace\underbrace{\to}_{\text{leggiamo una b}}\lbrace q_0,q_1\rbrace\underbrace{\to}_{\text{leggiamo un'altra b}}\lbrace q_0,q_1,q_3\rbrace$$
che corrisponde alla tabella di prima
In questo caso la stringa bbab non viene accettata dall'ASFND perchè l'insieme di stati $\lbrace q_0,q_1\rbrace$ non comprende stati finali
**fine esempio**

**Esempio**
L'automa precedente definisce, in corrispondenza alla stringa in input bba, le tre computazioni:
- $(q_0,bba)\vdash(q_0,ba)\vdash(q_0,a)\vdash(q_0,\epsilon)$
- $(q_0,bba)\vdash(q_0,ba)\vdash(q_1,a)\vdash(q_2,\epsilon)$
- $(q_0,bba)\vdash(q_0,ba)\vdash(q_1,a)\vdash(q_3,\epsilon)$

Il prefisso bb della stringa di input da luogo anche alla computazione:
- $(q_0,bb)\vdash(q_1,b)\vdash(q_3,\epsilon)$
la quale però non presenta continuazioni possibili

Albero delle computazioni corrispondente
![[appunti fi/immagini/Pasted image 20221031174530.png|center|500]]

Alternativamente, possiamo considerare che l'automa definisca la computazione non deterministica:
$$(\lbrace q_0\rbrace,bba)\vdash(\lbrace q_0,q_1\rbrace,ba)\vdash(\lbrace q_0,q_1,q_3\rbrace,a)\vdash(\lbrace q_0,q_1,q_3\rbrace,\epsilon)$$

### Accettazione ad ASFND

Una stringa x viene accettata da un automa a stati finiti non deterministico se almeno una delle computazioni definite per la stringa stessa è di accettazione, quindi se:
$$(\lbrace q_0\rbrace,x)\vdash^\star(\mathcal Q,\epsilon)$$
con $\mathcal Q\subseteq Q$ e $$\mathcal Q\cap F \neq\emptyset$$
### Funzione di transizione estesa di un ASFND
Dato un ASFND, la **funzione di transizione estesa** è la funzione $\overline\delta_N:Q\times\Sigma^\star\to\mathcal P(Q)$, definita nel seguente modo
$$\overline\delta_N(q,\epsilon)=\lbrace q\rbrace$$
$$\overline\delta_N(q,xa)=\bigcup_{p\in\overline\delta_N(q,x)}\delta_N(p,a)$$
dove $a\in\Sigma,x\in\Sigma^\star,p\in Q$

Dato uno stato q ed una striga x in input, $q'\in\overline\delta_N(q,x)$ se e solo se esiste una computazione dell'automa la quale, a partire da q ed in conseguenza della lettura della stringa x, conduce allo stato $q'$

### Linguaggio accettato da un ASFND

Il linguaggio $L(\mathcal A)$ accettato da un ASFND $\mathcal A$ è definito come:
$$L(\mathcal A)=\lbrace x\in\Sigma^\star|(\lbrace q_0,x\rbrace)\vdash^\star(Q,\epsilon),Q\cap F\neq\emptyset\rbrace$$
o anche come:
$$L(\mathcal A_N)=\lbrace x\in\Sigma^\star|\overline\delta_N(q_0,x)\cap F\neq\emptyset\rbrace$$


