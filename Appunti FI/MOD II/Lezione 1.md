
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

