
# Definizione di macchina di Turing

La macchina di Turing che abbiamo visto informalmente durante la scorsa lezione utilizza 3 nastri: sui primi due nastri, prima che la macchina inizi ad operare, vengono scritti (dall’utente) i due numeri da sommare, sul terzo, inizialmente vuoto, la macchina scrive il risultato nel corso della sua computazione

Dobbiamo, ora, formalizzare questi concetti e, allo scopo, cominciamo con il limitarci a considerare macchine di Turing che utilizzano un **solo nastro**

La definizione 1.3 a pag. 9 della dispensa 1 presenta una macchina di Turing ad un nastro come:

- una unità di controllo che, ad ogni istante, può trovarsi in uno stato interno appartenente ad un certo insieme Q che contiene, fra gli altri, lo stato particolare $q_0$ che fa partire la computazione e un sottoinsieme $Q_F$ di stati che fanno terminare la computazione
- un nastro suddiviso in un infinito numero di celle, ciascuna delle quali, ad ogni istante, può essere vuota o contenere un simbolo appartenente ad un alfabeto $\Sigma$, e sul quale nastro si muove una testina di lettura/scrittura
- ad ogni istante, dipendentemente dallo stato interno e da ciò che è letto dalla testina, viene eseguita una quintupla scelta in un insieme $P$ di quintuple

E come funziona una macchina di Turing? Facile: quando l’unità di controllo si trova nello stato $q_0$, la testina legge il simbolo contenuto nella cella che sta scandendo, cerca una quintupla i cui primi due elementi sono $q_0$ e il simbolo letto dalla testina (che può anche essere il simbolo blank $\square$) e, se trova una tale quintupla, la esegue

- se non la trova ... non compie alcuna azione (ci torneremo più avanti) e la computazione termina

Eseguire una quintupla significa eseguire le tre azioni in essa indicate:

- sovrascrivere il simbolo nella cella scandita dalla testina con il simbolo indicato nella quintupla
- cambiare (eventualmente) stato interno
	- eventualmente, ossia, a meno che nella quintupla non sia indicato di rimanere nel medesimo stato in cui ci si trovava prima della sua esecuzione
- muovere (eventualmente) la testina
	- eventualmente, ossia a meno che nella quintupla sia indicato “ferma”

Eseguita la prima quintupla, si cerca un’altra quintupla da eseguire (ossia, una quintupla i cui primi due elementi sono lo stato in cui si trova la machina e il simbolo letto dalla testina) e così via, fino a quando nessuna quintupla può essere eseguita

## Esempio di macchina di Turing

Consideriamo una macchina di Turing ad un nastro, $T_{parità}$ , definita sull’alfabeto $\Sigma=\langle 0,1,p,d\rangle$ e sull’insieme di stati $Q=\langle q_0,q_p,q_d,q_f\rangle$ con stato iniziale $q_0$ e stato finale $q_f$ il cui insieme delle quintuple è :
$$\begin{align}P=&\{\langle q_0,0,\square,q_p,dx\rangle,\langle q_0,1,\square,q_d,dx\rangle\\&\langle q_p,0,\square,q_p,dx\rangle,\langle q_d,0,\square,q_d,dx\rangle\\&\langle q_p,1,\square,q_d,dx\rangle,\langle q_d,1,\square,q_p,dx\rangle\\&\langle q_p,\square,p,q_f,stop\rangle,\langle q_d,\square,d,q_f,stop\rangle\}\end{align}$$
La macchina $T_{parità}$ scandisce la sequenza di caratteri scritta sul suo nastro, cancellandoli via via che vengono scanditi, e verificando se tale sequenza contiene un numero pari o un numero dispari di ‘1’: al termine della scansione, nel primo caso scrive ‘p’ e termina, nel secondo caso scrive ‘d’ e termina

Vediamo ora la macchina $T_{parità}$  in azione:

- poniamo la macchina nello stato q_0
- scriviamo una sequenza di caratteri sul nastro – che era precedentemente vuoto
- posizioniamo la testina sul carattere più a sinistra fra quelli scritti sul nastro
- ![[appunti fi/mod ii/immagini/Pasted image 20230308153924.png|center|500]]
- .. e vediamo cosa succede

Osserviamo che P contiene la quintupla $\langle q_0 , 1, \square, q_d , dx\rangle$ e che essa può essere eseguita

![[appunti fi/mod ii/immagini/Pasted image 20230308154102.png|center|500]]

eseguiamo, la quintupla, $\langle q_0 , 1, \square, q_d , dx\rangle$ : 

![[appunti fi/mod ii/immagini/Pasted image 20230308154155.png|center|500]]

E cosi via...

Naturalmente, sul nastro di $T_{parità}$ possiamo scrivere ciò che vogliamo:

- ad esempio, possiamo scrivere la sequenza di caratteri p010
- e vedere cosa succede facendo partire questa nuova computazione:
- ![[appunti fi/mod ii/immagini/Pasted image 20230308154333.png|center|500]]
.. Attenzione! P non contiene alcuna quintupla che inizia con la coppia $(q_0,p)$
- quindi, nessuna quintupla può essere eseguita

## Ritorniamo alla definizione di macchina di Turing (a singolo nastro)

Riassumiamo: una macchina di Turing ad un nastro è completamente caratterizzata dai cinque elementi:

- $\Sigma$, ossia, un insieme $\underline{finito}$ di caratteri che prende il nome di **alfabeto**
- $Q$, ossia, un insieme $\underline{finito}$ di **stati interni**
- uno stato interno particolare (generalmente indicato come $q_0$) chiamato **stato iniziale**
- un sottoinsieme $Q_F$ di $Q$ di stati finali
- un insieme $P\subseteq Q\times\Sigma\times\Sigma\times Q\times\{sx,stop,dx\}$ di quintuple
	- che, sappiamo, deve essere _non ambiguo_
	- ossia,  non contiene coppie di quintuple che hanno uguali i primi due elementi
	- ossia, in effetti, $P$ **è una funzione**: $P:Q\times\Sigma\to\Sigma\times Q\times\{sx,stop,dx\}$

Ossia, possiamo dire che:  **una macchina di Turing (ad un nastro) è una quintupla$\langle\Sigma,Q ,q_0, Q_F, P\rangle$**
e dare per assodata l’esistenza di unità di controllo e nastro

# Definizione di macchina di Turing (a nastro multiplo)

E che dire di una macchina di Turing a più nastri? È (quasi) la stessa cosa:
una macchina di Turing a k nastri è completamente caratterizzata da

- un **alfabeto** $\Sigma$, ossia, un insieme finito di caratteri
- un insieme finito $Q$ di **stati interni**
- uno stato interno **iniziale**
- un sottoinsieme $Q_F$ di $Q$ di stati finali
- un insieme $P$ di **quintuple**, ove in questo caso una quintupla ha la forma   $\langle q_1 , (a_1, a_2, ... , a_k), (b_1, b_2, ... , b_k),  q_2 , (m_1, m_2, ... , m_k)\rangle$
	- $(a_1, a_2, ... , a_k)$ sono i caratteri che devono essere letti sui k nastri
		- $a_1$ è il carattere che deve essere letto sul nastro 1, $a_2$ è il carattere che deve essere letto sul nastro 2, ...
	- $(b_1, b_2, ... , b_k)$ sono i caratteri che devono essere scritti sui k nastri (sovrascrivendo $(a_1, a_2, ... , a_k)$ )
		-  $b_1$ è il carattere che deve essere scritto sul nastro 1, ...
	-  $(m_1, m_2, ... , m_k)$, sono i movimenti che devono essere eseguiti dalle k testine
		-  $m_1$ è il movimento che deve essere compiuto dalla testina sul nastro 1, ...

>[!important]- Osservazione
>Il numero di nastri che si possono usare devono essere sempre un numero k **costante**, e quindi che non dipende dall'input.

**OSSERVAZIONE**
per capire quale sia il numero di nastri di una macchina di Turing $\langle\Sigma,Q, q_0, Q_F, P\rangle$ è sufficiente osservare le quintuple contenute in P:

- il numero di componenti del secondo elemento di una quintupla in P (che specifica ciò che deve essere letto sul/sui nastro/nastri per poter eseguire una quintupla) corrisponde al numero di nastri!
- ad esempio, se le quintuple di una macchina di Turing hanno la forma $\langle q_1 , a_1, ...\rangle$ allora si tratta di una macchina ad un nastro
- se le quintuple di una macchina di Turing hanno la forma $\langle q_1 , (a_1, a_2), ... \rangle$ allora si tratta di una macchina a due nastri
- e così via

# Definizione di Macchina di Turing

Dunque, possiamo dire che, in generale, una macchina di Turing è una quintupla$\langle\Sigma,Q, q_0, Q_F, P\rangle$

E, come dovremmo aver compreso, una macchina di Turing è la descrizione di un procedimento di calcolo

ossia, è un algoritmo descritto utilizzando le regole introdotte da Alan Turing

- in qualche modo, dunque, un programma scritto nel linguaggio progettato da Turing

Le regole introdotte da Turing per descrivere procedimenti di calcolo costituiscono un **modello di calcolo**

- tanto quanto ciascun linguaggio di programmazione, ad esempio, è un modello di calcolo
- o tanti altri modelli ai quali accenneremo

un modello di calcolo che prende il nome di **_Macchina di Turing_**  

Per esercizi vedi su Ipad, lezione 2

# macchine di Turing

Il modello di calcolo Macchina di Turing richiede che in ogni macchina l’insieme degli stati e l’alfabeto abbiano cardinalità **finita** – e lo stesso vale per il numero di nastri

è necessario che numero di stati, numero di simboli dell’alfabeto, numero di quintuple e numero di nastri siano **costanti**

- **ossia, indipendenti dall’input**

## Tante definizioni per la macchina di Turing

Nel paragrafo 2.1 della dispensa 2 vengono presentate alcune definizioni formali relative alle macchine di Turing:

- parole
- stati globali
- transizioni
- computazioni

Queste definizioni devono essere tenute sempre presenti!!!!

Osservate che viene utilizzata la parola _deterministica_: questo significa che P è una funzione (avremo tempo e modo di affrontarla bene e a lungo, questa questione)

Innanzi tutto: dato un alfabeto finito $\Sigma$, una _**parola**_ su $\Sigma$ è una sequenza finita di elementi di $\Sigma$

- ad esempio, aba è una parola sull’alfabeto $\Sigma$ = { a, b, c }

L’insieme della parole su un alfabeto $\Sigma$ si indica con $\Sigma^{\star}$ 

### Stati globali

Uno stato globale SG di una macchina di Turing è una “fotografia” della macchina ad un certo istante

Formalmente, uno **stato globale** di una macchina ad un nastro T ad un certo istante

- contiene una descrizione della porzione non blank del nastro di T, della posizione della testina (e, dunque, del carattere da essa letto) e dello stato interno  
- ed è rappresentato mediante la sequenza di caratteri (non blank) contenuti sul nastro in cui al carattere letto dalla testina è premesso lo stato interno

Naturalmente, possiamo definire anche lo stato globale di una macchina a k nastri (con k costante!)

![[appunti fi/mod ii/immagini/Pasted image 20230310124342.png|center|600]]


### Transizioni

Una transizione dallo stato globale $SG_1$ allo stato globale $SG_2$ avviene quando viene eseguita una quintupla che trasforma $SG_1$ in $SG_2$

Formalmente, se $T =\langle\Sigma, Q, q_0, Q_F, P\rangle$ è una macchina di Turing ad un nastro, esiste una **transizione** da $SG_1$ a $SG_2$ se esiste una quintupla $\langle q,x,x',q',m\rangle\in P$ tale che

- in $SG_1$ T si trova nello stato interno $q\in Q$
- in $SG_1$ la testina di T sta scandendo una cella che contiene il carattere $x\in\Sigma$
- in $SG_2$ la cella che in $SG_1$ conteneva il carattere x contiene il carattere $x'\in\Sigma$
- in $SG_2$ T si trova nello stato interno $q'\in Q$
- in $SG_2$ la testina di T sta scandendo la cella che si trova in posizione m rispetto a quella che stava scandendo in $SG_1$

il concetto può essere facilmente esteso a macchine a più nastri
- con qualche tecnicismo in più, che non affrontiamo

![[appunti fi/mod ii/immagini/Pasted image 20230310124748.png|center|600]]

### Computazione

Informalmente, una computazione di una macchina di Turing **deterministica** a un nastro $T =\langle\Sigma, Q, q_0, Q_F, P\rangle$ è l’esecuzione delle quintuple di T su una sequenza di caratteri scritti sul suo nastro
- e analogamente per le macchine a più nastri

Formalmente: una **computazione** di una macchina di Turing T è una sequenza $SG_0$, $SG_1$, $SG_2$, ... , $SG_h$, ... di stati globali di T tali che

- $SG_0$ è uno stato globale iniziale, ossia, uno stato globale nel quale lo stato interno è $q_0$ e la testina è posizionata sul carattere più a sinistra scritto sul nastro
- per ogni $0\leq i\leq h-1$, esiste una transizione da $SG_i$ a $SG_{i+1}$ oppure per ogni $h\geq i+1$ $SG_h$ non è definito

se esiste un indice h tale che $SG_h$ è uno stato globale dal quale non può avvenire alcuna transizione allora la computazione **termina**

- e questo accade quando lo stato interno nel quale T si trova in  $SG_h$ è uno stato finale oppure P non contiene una quintupla che possa essere eseguita in $SG_h$

![[appunti fi/mod ii/immagini/Pasted image 20230310125150.png|center|600]]

### Trasduttori e Riconoscitori

#### Trasduttori

Nel paragrafo 2.2 della dispensa 2 vengono definiti due tipi di macchine di Turing.

Le macchine di tipo **trasduttore** sanno calcolare il valore di una funzione qualsiasi

- ad esempio, un trasduttore sa calcolare la funzione f(a,b)=a+b.

Assumeremo sempre che le macchine di Turing di tipo trasduttore dispongano di un **nastro di output** sul quale scrivono il valore della funzione che hanno calcolato

Un trasduttore <u>ha un solo stato finale</u> con il quale terminare la computazione: lo stato $q_F$

#### Riconoscitori

Nel paragrafo 2.2 della dispensa 2 vengono definiti due tipi di macchine di Turing.

Le macchine di tipo **riconoscitore** sanno calcolare soltanto il valore di funzioni booleane

- ossia, funzioni il cui valore è 0 oppure 1

e non dispongono di un nastro di output.

**Il valore calcolato da un riconoscitore viene memorizzato nello stato interno con il quale la macchina termina la computazione**: $q_A$ se il valore della funzione è 1, $q_R$ se il valore della funzione è 0

- quindi, ogni riconoscitore ha due stati finali: $q_A,q_R$

Diciamo che un riconoscitore T **accetta** x se la computazione $T(x)$ termina in $q_A$ e che la macchina T **rigetta** x se la computazione $T(x)$ termina in $q_R$

### Esito di una computazione

Sempre nel paragrafo 2.2 della dispensa 2 viene introdotto il concetto di esito di una computazione

Data una macchina di Turing T ed un suo input x, l’esito della computazione $T(x)$ è indicato con $o_T(x)$ – informalmente è “il risultato” della computazione, la risposta che ci dà la macchina rispetto all’istanza x del problema che le abbiamo chiesto di risolvere

Se T è una macchina di tipo _trasduttore_, allora $o_T(x)$ è la parola scritta da T sul nastro di output al termine della computazione $T(x)$ (ossia, quando T ha raggiunto lo stato $q_F$): ad esempio, se T è il trasduttore che calcola la funzione $f(a,b)=a+b\implies o_T(15,6)= 21$

Se T è una macchina di tipo **riconoscitore**, allora $o_T(x)$ è lo stato interno con il quale la macchina termina la computazione $T(x)$: ad esempio, se T è la macchina che decide se una parola è palindroma, allora $o_T(abba) =q_A$ e $o_T(baaba) =q_R$

