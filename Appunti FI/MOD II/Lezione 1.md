Email prof : miriam.di.ianni@gmail.com
# Contenuti del corso

2 parti:

1. Calcolabilità
	1. Capire quali problemi possono essere risolti automaticamente
		1. più avanti vedremo che alcuni problemi che non possono essere risolti
	2. E per farlo, dovremmo capire cosa significa _risolvere **automaticamente** un problema_
		1. e, a dirla tutta, cosa significa, in assoluto, _**risolvere** un problema_
		2. e, persino, _cos'è un **problema**_
2. Complessità
	1. Capire quali dei problemi che possono essere risoltim possono essere proprio risolti **per davvero**
	2. Lo vedremo più avanti

# Problemi e istanze

Cos'è un problema? Facile

- "Quanto fa 5+2?", "Quanto misura l'area di un rettangolo la cui base è 5 e l'altezza è 3?" Ecco due esempi di problema

Sbagliato! Nell'esempio, sono illustrate due _**istanze**_ di due problemi diversi

I problemi a cui corrispondono quelle istanze sono:

1. Problemma Somma: dati due numeri reali n e k, calcolare il valore di n+k
2. Problema Area: dato un rettangolo, con base b e altezza h, calcolare l'area

>[!important]- Definizione (Problema)
>Un **problema** è la descrizione di un insieme di parametri, che chiameremo _**dati**_, colelgati da un certo insieme di relazioni,associata alla richiesta di derivare da essi un'altro insieme di parametri,che costituiscono la soluzione

Un'istanza di un problema è un particolare insieme di valori associati ai dati (lo vedremo più avanti)

## Risolvere un problema

Risolvere un problema significa individuare _un metodo_ che **sappia trovare la soluzione di qualunque istanza positiva del problema**
( e in più che sappia riconoscere se un'istanza è negativa)

Ossia, significa trovare un procedimento che, data una qualunque istanza del problema, indichi la sequenza di azioni che devono essere eseguite per trovare la soluzione a quell'istanza

E qui sorgono un bel pò di questioni:

- innanzi tutto, cos'è un procedimento?
- Cos'è un'azione?
- Chi è supposto devva eseguire le azioni indicate?

Queste questioni, come vedremo, sono fra loro interconnesse

Cos'è un procedimento?

>[!important]- Definizione (procedimento)
>Un procedimento è la descrizione di un insieme di azioni unita alla specifica dell'ordine con il quale le azioni devono essere eseguite

Che cos'è una azione?

- Qualcosa che deve essere fatto, ovvio! Tuttavia...
- Anche "_data un'istanza del problema, trova la soluzione di quell'istanza_" è una azione
- Allora, dobbiamo dire che **le azioni indicate in un procedimento, devono essere azioni semplici, cioè che possono essere eseguite con facilità**

## L'istruzione elementare

Se vogliamo svincolare la definizione di procedimento risolutivo di un problema da quello di esecutore delle azioni in esso indicate, è necessario, prima di tutto, chiarire formalmente cosa si intende con **istruzione elementare**

Vediamo la soluzione individuata da Alan Turing

Turing osservò che, indipendentemente dall'esecutore, qualunque istruzione, per poter essere definita _elementare_, deve avere le seguenti caratteristiche:

- deve essere scelta in un insieme di "poche" istruzioni possibili
- deve scegliere l'azione da eseguire all'interno di un insieme di "poche" azioni possibili
- deve poter essere eseguita ricordando una quantità limitata di dati, ossia, in termini più tecnici, utilizzando una quantità limitata di memoria

Osserviamo che le caratteristiche individuate da Turing indicano come istruzione elementare una operazione che possa essere eseguita a mente

**Esempio**

Consideriamo il PROBLEMA SOMMA: dati due interi n e k, ci viene richiesto di calcolare il numero n + k
Vogliamo progettare un procedimento che risolva questo problema
Ebbene: calcolare la somma di due interi è certamente facile  abbiamo imparato a calcolarla in prima elementare! 
- allora, potremmo pensare che l’istruzione “calcola n + k” sia un’istruzione elementare
ATTENZIONE: stiamo cercando un procedimento che risolva un problema (il PROBLEMA SOMMA), quindi “calcola n + k” deve essere un’istruzione elementare _**qualunque**_ valore venga assegnato a n e k 
Però, se n = 37895 e k = 441238 ... 
A nessuno di noi, soltanto guardando i due addendi, salta in mente il risultato (anche se le addizioni le sappiamo fare benissimo!)

Se n = 37895 e k = 441238, a nessuno di noi, guardando i due addendi, salta in mente quanto fa n + k 
Questo perché la nostra memoria è limitata 
Chiariamo: 
- In qualche modo, quando abbiamo imparato a fare le addizioni, abbiamo _**memorizzato**_ la tabella che ci permette di calcolare a mente la somma di qualunque coppia di numeri di una cifra ciascuno![[appunti fi/mod ii/immagini/Pasted image 20230307115244.png]]

Ma se disponessimo di una tabella sufficientemente grande che indica le somme di tutti i numeri naturali compresi fra 0 e 1000000 (ad esempio), ci basterebbe guardare nella cella opportuna e avremmo la somma cercata: al volo, ad occhio...

Ossia, disporre di questa nuova tabella ci permetterebbe di considerare istruzione elementare la somma di qualunque coppia di numeri naturali compresi fra 0 e 1000000
Allora, è fatta! Basta predisporre una tabella _sufficientemente grande_ e qualunque somma diventa un’istruzione elementare!
Ma **NO, NON FUNZIONA IN QUESTO MODO!!!!**
Il problema è che, per risolvere il PROBLEMA SOMMA, occorre indicare un procedimento che sappia addizionare _qualunque_ coppia di numeri naturali 
- per quanto grandi essi siano 
e, quindi, se volessimo considerare istruzione elementare la somma di qualunque coppia di numeri, **dovremmo costruire una tabella infinita!**

Ecco perché la somma di qualunque coppia di numeri naturali non può essere considerata un’operazione elementare: perché avremmo bisogno di memorizzare una tabella di dimensioni illimitate 
Mentre, invece, la nostra memoria è limitata! 
Per questa ragione, per eseguire la somma di qualunque coppia di numeri naturali, utilizziamo un _**procedimento**_ che
- utilizza un numero limitato di operazioni elementari (le somme di coppie di numeri di una sola cifra) 
- e in cui ogni operazione elementare utilizza una quantità limitata di dati (due cifre e l’eventuale riporto) 
In accordo alle caratteristiche enunciate da Turing
E adesso andiamo a ripassare questo procedimento ...

### La somma di due numeri naturali

- Per calcolare il valore della somma 37895 + 441238, innanzi tutto scriviamo l’operazione in colonna:$$\begin{align}&3 7 8 9 5 +\\&4 4 1 2 3 8=\end{align}$$
- poi, osserviamo le due cifre più a destra, e calcoliamo la loro somma e l’eventuale riporto $$\begin{align}&3 7 8 9 5 +\\& 4 4 1 2 3 8\end{align}$$ =  3 con riporto di 1
- poi, osserviamo le due cifre più a destra non ancora considerate, e calcoliamo la loro somma più l’eventuale riporto, e il nuovo eventuale riporto $$\begin{align}&3 7 8 9 5 +\\& 4 4 1 2 3 8\end{align}$$ = 3 3 con riporto di 1 
- ... e così via ...

Pensandoci bene, potremmo descrivere il procedimento per calcolare la “somma in colonna” di due numeri naturali nel modo seguente
1) posizionati sulla coppia di cifre più a destra, e poni r = 0 
2) fino a quando leggi una coppia di cifre, esegui la somma della coppia di cifre sulle quali sei posizionato, aggiungi r a tale valore e scrivi una cifra del risultato calcolando anche il nuovo valore di r, e poi spostati a sinistra
3) fino a quando leggi una sola cifra (ossia, le cifre di uno dei due numeri sono terminate) aggiungi r ad essa e scrivi una cifra del risultato calcolando anche il nuovo valore di r, e poi spostati a sinistra
4) se le cifre di entrambi i numeri sono terminate, allora calcola l’eventuale ultima cifra del risultato e termina

Ossia, il procedimento per calcolare la “somma in colonna” di due numeri naturali è una sequenza di “se sono vere _certe condizioni_ allora esegui **queste azioni**” 
- ad ogni coppia (_certe condizioni_, **queste azioni**) corrisponde un’istruzione 
- dove _certe condizioni_ è ciò che viene letto (la coppia di cifre dei due numeri, eventualmente assenti) e il valore del riporto 
- e **queste azioni** è ciò che viene scritto, la modifica del valore del riporto, e lo spostamento
	- o, in alcuni casi, **queste azioni** è l’indicazione che la somma è stata completata (termina)
- Pensandoci bene, questo procedimento potrebbe eseguirlo chiunque sappia leggere e scrivere e distinguere fra destra e sinistra 
	- che sono nozioni davvero **elementari!** 
	- Su questo non c’è davvero dubbio! 
- Ma, pur essendo istruzioni elementari da un punto di vista intuitivo, sono quelle appena individuate **istruzioni elementari nel senso indicato da Turing?**

Ricordiamo che, nell’accezione di Turing, un’istruzione, per potere essere definita elementare, deve avere le seguenti caratteristiche: 

- deve essere scelta in un insieme di “poche” istruzioni disponibili
- deve scegliere l’azione da eseguire all’interno di un insieme di “poche” azioni possibili
- deve poter essere eseguita ricordando una quantità limitata di dati, ossia, in termini più tecnici, utilizzando una quantità limitata di memoria. 

Ora, abbiamo già visto che nel procedimento che esegue la somma le azioni che vengono eseguite sono due: scrittura di una cifra e spostamento 

- e possiamo ben affermare che esse sono davvero “poche”! 

Ma è vero che Il procedimento che esegue la somma ha un insieme di “poche” istruzioni disponibili ciascuna delle quali utilizza una quantità limitata di memoria? 

- Che poi: ma cosa si intende con “poche” e con quantità limitata?

Ma è vero che Il procedimento che esegue la somma ha un insieme di “poche” istruzioni disponibili ciascuna delle quali utilizza una quantità limitata di memoria?

Riflettiamo:

- il numero di istruzioni disponibili è pari al numero di coppie di cifre moltiplicato per il numero di possibili valori per il riporto, ossia, 10 × 10 × 2 = 200
- per sapere quale istruzione dobbiamo eseguire abbiamo bisogno di conoscere le due cifre da sommare e il valore del riporto, ossia, 3 numeri di una cifra

Ricapitolando: per sommare qualunque coppia di interi (**grandi quanto ci pare**) abbiamo a **disposizione 222 istruzioni** (che eseguono 2 azioni) fra le quali scegliere quella da eseguire utilizzando una memoria di 3 cifre

Indipendentemente da quanto sono grandi i due numeri che vogliamo sommare, sempre 222 istruzioni (che eseguono 2 azioni) disponibili che utilizzano una memoria di 3 cifre sono!

**Ossia, il numero di istruzioni, azioni e la quantità di memoria necessaria sono _costanti_: non dipendono da quello che chiameremo input**
- chiaro ora cosa si intende con “poche” e con quantità limitata?
- Chiara, ora, la scelta di Turing delle sue tre caratteristiche!

Ossia, il procedimento per calcolare la “somma in colonna” di due numeri naturali è una sequenza di “se sono vere _certe condizioni_ allora esegui **queste azioni**” 
- ad ogni coppia (_certe condizioni_, **queste azioni**) corrisponde un’istruzione 
- dove _certe condizioni_ è ciò che viene letto (la coppia di cifre dei due numeri, eventualmente assenti) e il valore del riporto 
- e **queste azioni** è ciò che viene scritto, la modifica del valore del riporto, e lo spostamento
	- o, in alcuni casi, **queste azioni** è l’indicazione che la somma è stata completata (termina)
- Pensandoci bene, questo procedimento potrebbe eseguirlo chiunque sappia leggere e scrivere e distinguere fra destra e sinistra 
- Pensandoci bene, per eseguire questo procedimento non è necessario nemmeno sapere cosa significa “sommare due numeri naturali”
- esegui le istruzioni del procedimento e, come per magia, alla fine ti ritrovi con il risultato in mano
- Perché, naturalmente, le istruzioni ti dicono, **per ogni condizione possibile, esattamente quali azioni devi eseguire in quelle condizioni**
- questo significa che l’insieme di istruzioni è _non ambiguo_: non può contenere due (o più) istruzioni che, a partire dalle stesse condizioni , ti indica  diverse azioni da eseguire
	- non può succedere, ad esempio, che un’istruzione affermi “se è vero a allora scrivi 5” e un’altra istruzione affermi “se è vero a allora scrivi 6”
	- altrimenti, quando è vero a come devi comportarti tu che vuoi eseguire le istruzioni?
- E, dunque, **l’ordine in cui eseguire le istruzioni è indicato implicitamente nel meccanismo stesso de “se ... allora ...”**
	- in ogni istante devi eseguire l’unica istruzione che è possibile eseguire, fino a quando non incontri un’istruzione che ti dice di terminare
	- non puoi fare altro!
- Attenzione, però: per ottenere il risultato **devi** eseguire le istruzioni
	- ossia, ogni volta che si verificano quelle condizioni tu quelle azioni devi eseguirle
	- senza se e senza ma, le esegui e basta!
- Cioè, le istruzioni sono una sorta di ordini
	- loro ti dicono di fare qualcosa e tu lo fai!
- Questa idea di istruzione, nata dall’analisi di Turing, è alla base di molti linguaggi di programmazione che, proprio per questo, vengono detti imperativi
	- il C, il Fortran, ma anche Java o Python

## Risolvere automaticamente un problema

Eccoci al nocciolo della questione:

- informalmente, risolvere automaticamente un problema significa progettare un procedimento che risolve tutte le istanze di quel problema e che può essere eseguito da un automa
	- ossia, da un esecutore che può non avere alcuna idea del problema né del significato delle istruzioni contenute nel procedimento

Il resto della prima parte di questo modulo è dedicato a formalizzare questo concetto informale

## Un nuovo linguaggio...

Ripensiamo alla somma di due numeri naturali:

1) il procedimento che abbiamo visto è costituito di sole istruzioni      “se sono vere certe condizioni allora esegui queste azioni”
	1) ripetute fino a quando non si incontra il comando “termina”
2) in ciascuna istruzione le azioni da eseguire sono le 3 azioni seguenti
	1) la scrittura di una cifra, la (eventuale) modifica del riporto, il movimento a sinistra per considerare le successive due cifre da sommare
3) infine, le condizioni di ognuna delle istruzioni dipendono da due tipi di parametri
	1) il valore del riporto
	2) le due cifre da sommare

NOTA: mentre le due cifre da sommare le troviamo scritte sul foglio sul quale abbiamo indicato (in colonna) i due numeri che vogliamo sommare

Il valore del riporto lo teniamo a mente ad ogni coppia di cifre sommate

- è, cioè, qualcosa che caratterizza il nostro “stato interiore

In virtù delle osservazioni 1), 2) e 3), possiamo scrivere il nostro procedimento in forma più compatta

- poiché utilizziamo sole istruzioni “se condizione allora azione”  possiamo anche evitare di scrivere “se ... allora ...” ogni santa volta
- e scrivere, di seguito, le due condizioni seguite dalle tre azioni

così, ad esempio, l’istruzione

- se r = 0 e le due cifre sono 4 e 6, allora scrivi 0, poni r = 1, e spostati di una posizione a sinistra

diventa

-  $\langle q_0,(4,6),0,q_1,sx\rangle$

dove $q_0$ e $q_1$ sono due simboli che indicano, rispettivamente, r = 0 e r = 1
OSSERVAZIONE: in questo esempio sembrerebbe che anche “sinistra” possa essere omesso; vedremo che questa specifica, invece, occorre tenerla

e l’istruzione 
- se r = 1 e l’unica cifra è 5, allora scrivi 6, poni r = 0, e spostati di una posizione a sinistra
nella quale le cifre di uno degli operandi sono terminate, diventa la coppia di istruzioni
- $\langle q_1,(5,\square),6,q_0,sx\rangle$ 
- $\langle q_1,(\square,5),6,q_0,sx\rangle$ 
dove il simbolo $\square$ indica che non viene letto alcunché o che non deve essere scritto alcunché 
e abbiamo due diverse istruzioni perché l’operando le cui cifre sono terminate può essere il primo o il secondo

e, infine, le istruzioni 
- se r = 1 e le cifre di entrambi i numeri sono terminate, allora scrivi 1 e termina 
- se r = 0 e le cifre di entrambi i numeri sono terminate, allora termina 
diventano, rispettivamente 
- $\langle q_1,(\square,\square),1,q_f,fermo\rangle$
- $\langle q_0,(\square,\square),\square,q_f,fermo\rangle$
dove $q_f$ è lo “_**stato interiore**_” che permette all’esecutore di comprendere che non deve più eseguire alcuna azione 
- ossia, non si deve “tornare al punto 2)” 
e qui l’utilizzo di “fermo” mostra anche perché è necessario specificare come ci si deve muovere

## ... e una macchina che lo comprende

- Possiamo, a questo punto, rappresentare graficamente l’esecuzione del procedimento che calcola la somma di due numeri qualsiasi 
	- ad esempio, i numeri 53 e 28 
- per farlo, immaginiamo di disporre di una sorta di automa 
	- che rappresentiamo come una specie di “testa robotizzata” 
	- e che può trovarsi in uno di tre possibili “stati interiori”: $q_0$ , $q_1$ e $q_f$ 
- che utilizza, per leggere e scrivere , tre nastri 
	- suddivisi ciascuno in un numero infinito di celle 
	- tali che ciascuna cella, in ogni istante, può contenere o una cifra (un numero compreso fra 0 e 9) oppure può essere vuota (e indichiamo con $\square$ il simbolo di cella vuota) 
- e tre testine di lettura/scrittura 
- Non appena viene scritto qualcosa sui nastri, dipendentemente dallo “stato interiore” dell’automa e da quello che viene letto, l’automa inizia a **computare** – ossia a eseguire le quintuple del procedimento

![[appunti fi/mod ii/immagini/Pasted image 20230307151710.png|center|500]]

## Quasi una macchina di Turing

Quella che abbiamo visto è quasi una descrizione informale di una maccina di Turing 

_Quasi_, perché abbiamo utilizzato tre nastri e in una macchina di Turing occorre descrivere cosa viene letto (nelle condizioni) e cosa viene scritto (nelle azioni) su ogni nastro

Così che l’istruzione 

- se r = 0 e le due cifre sono 4 e 6, allora scrivi 0, poni r = 1, spostati di una posizione a sinistra e torna al punto 2) 

Diventa $\langle q_0,(4,6,\square),(4,6,0),q_1,sx\rangle$ 

- che specifica cosa deve essere scritto sui 3 nastri (4, 6, $\square$) e con cosa questi tre elementi devono essere sovrascritti (4, 6, 0)

Poiché specifica 2 condizioni e 3 azioni, essa prende il nome di **quintupla** 

E, quelli che abbiamo chiamato sino ad ora “stati interiori”, si chiamano propriamente **stati interni** 

E l’esecuzione delle quintuple su un insieme fissato di dati (come nella figura) si chiama **_computazione_**

# Calcolabilità

Quella che abbiamo visto è, dunque, una descrizione informale di una macchina di Turing

- con la ‘m’ minuscola

Che è la descrizione di un procedimento di risoluzione di un problema espresso nel linguaggio definito da Alan Turing

Linguaggio che costituisce un modello di calcolo: il modello Macchina di Turing 

- con la ’M’ maiuscola 

E tutto ciò, che è necessario per parlare di Calcolabilità


