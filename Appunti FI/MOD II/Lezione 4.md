
# macchine non deterministiche

Siamo al paragrafo 2.3 della dispensa 2 (pag. 4).

Prendiamo una macchina di Turing:
- cioè, un alfabeto $\Sigma$ e un insieme degli stati $Q$
- e, soprattutto, l’insieme delle sue quintuple $P$
- è sufficiente avere l’insieme $P$ per sapere tutto di $T$: da $P$ possiamo ricavare sia $\Sigma$ che $Q$
- in realtà $P$ non ci dice proprio tutto tutto: per sapere tutto di $T$, oltre che $P$, dobbiamo conoscere anche quale sia lo stato iniziale e quali siano gli stati finali

Bene. Quindi, $P$ è il “cuore” di $T$. Ora, andiamo a studiare la struttura di $P$

Intanto, ricordiamo che possiamo vedere $P$ come una funzione che associa ad una coppia (stato, simbolo) una tripla (stato, simbolo ,movimento) , ossia : 
$$P:Q\times\Sigma\to\Sigma\times Q\times\{S,D,F\}$$

## P è una funzione totale?

Una quintupla $\langle q_1 , a, b, q_2 , m\rangle$ ci dice che: se siamo nello stato $q_1$ e leggiamo il carattere a allora dobbiamo comportarci in un certo modo

Ma cosa succede se, trovandoci in uno stato q e leggendo un carattere s non troviamo in $P$ alcuna quintupla i cui primi due simboli sono q e s?

Non viene indicata alcuna azione da compiere. E, allora, T non può far altro che non compiere alcuna azione.

Cioè, T interrompe la sua computazione - è come se avesse raggiunto uno stato finale

Però, uno stato finale non lo ha raggiunto

Per capire, dobbiamo chiarire che cosa significa che ad una coppia (q,s) non è associata alcuna quintupla in  $P$ – e lo facciamo separatamente per i trasduttori e per i riconoscitori

### Trasduttori

Se T è un trasduttore, che cosa significa che ad una coppia (q,s) non è associata alcuna quintupla in $P$?

Facciamo un esempio: consideriamo una macchina $T$ a 3 nastri che calcola il risultato dell’addizione in colonna di due interi **nel caso in cui il secondo addendo è costituito di sole cifre pari**
- non esistono quintuple di T del tipo $\langle q , (x,y,\square), (x,y,z), q_1 , sx\rangle$, dove y è una cifra dispari

Se assumiamo che il secondo addendo (scritto sul secondo nastro) sia costituito di sole cifre pari, allora

- eseguendo tutte le quintuple che abbiamo visto nelle lezioni precedenti, T scrive una alla volta le cifre del risultato sul nastro di output
- ossia, man mano che la computazione prosegue, le cifre del risultato compaiono sul nastro di output

Cosa succede, però, se un utente ha scritto 1234 sul primo nastro e 2560 sul secondo nastro?

- T scrive 4 sul nastro di output
- poi, scrive 9 sul nastro di output
- poi... Errore! Non trova più alcuna quintupla da eseguire

ma il nastro di output non è vuoto...

Se, trovandoci in uno stato q e leggendo un carattere s non troviamo in $P$ alcuna quintupla i cui primi due simboli sono q e s, poiché non viene indicata alcuna azione da compiere, $T$ non può far altro che non compiere alcuna azione!

Quindi potremmo pensare che: ogni qualvolta ad una coppia (q,s) non è associata alcuna quintupla in P, è possibile aggiungere a P la quintupla $\langle q , s, s, q_F , F\rangle$

Tuttavia : 
- mentre un trasduttore lavora, man mano che esegue le sue quintuple, è possibile che scriva qualcosa sul nastro di output – la prima parte del risultato
- però se la computazione di T è terminata, non perché T è entrata in uno stato finale ma perché non ha trovato quintuple da eseguire, allora _**quel che è scritto sul nastro di output non è il risultato cercato!**_
- E l’utente come fa a capirlo????

Abbiamo due possibilità a disposizione:

1. Chi ha progettato T ha considerato tutte le possibilità (stato,simbolo), anche quelle “**impossibili**” (che si incontrano quando l’utilizzatore non legge il libretto di istruzioni di T e scrive sul nastro un input non conforme alle specifiche): per ciascuna di queste coppie impossibili ha scritto una serie di quintuple che prima cancellano il contenuto del nastro di output e poi portano $T$ in $q_F$, progettando quindi una **_funzione $P$ totale_**
	1. o, equivalentemente, per ciascuna di queste coppie, viene scritto un messaggio di errore sul nastro di output prima di raggiungere lo stato $q_F$
2. Chi ha progettato $T$ ha deciso che se un utilizzatore è stato poco accorto e non ha rispettato le specifiche… peggio per lui! E, semplicemente, chi ha progettato $T$ ha scritto solo le quintuple per le coppie (stato,simbolo) significative. E, così, ha progettato una _**funzione $P$ non totale**_

### Riconoscitori

Per capire cosa accade quando $T$ è un riconoscitore dobbiamo prima chiarire cosa significa, nel caso in cui $T$ è un riconoscitore, che ad una coppia (q,s) non è associata alcuna quintupla in $P$

Facciamo un esempio: consideriamo una macchina $T$ che decide se il risultato dell’addizione di due interi sarà un numero pari
- non deve calcolare il risultato: deve solo terminare in $q_A$ qualora il risultato sia pari, in $q_R$ qualora il risultato sia dispari

Quindi, se assumiamo che l’input sia scritto sul nastro di T nella forma “primo addendo + secondo addendo” (dove ciascun addendo è una sequenza di cifre), allora
- T deve spostare la testina sulla cifra meno significativa del primo addendo (quella a sinistra del ‘+’) e ricordarsi se è pari o dispari
- poi deve spostare la testina sulla cifra meno significativa del secondo addendo (ossia seve superare la sequenza di cifre che compongono il secondo addendo e posizionarsi sulla cifra a sinistra del $\square$) e, dipendentemente da quello che si ricordava e dal fatto che tale cifra sia pari o dispari, terminare in $q_A$ o in $q_R$.

Ma che succede se, invece, un utilizzatore poco accorto scrive sul nastro di $T$ la parola “$576+48+$”? Come si comporta $T$?
- non sappiamo come si comporta, ma certamente ci aspettiamo che essa non termini in $q_A$
- perché T deve terminare in qA solo se la somma di due numeri è pari
- e qui, invece, le viene proposta la somma di quasi tre numeri (ossia, due numeri e un +)

Allora, ci sono due possibilità:

- Chi ha progettato $T$ ha considerato tutte le possibilità (stato,simbolo), anche quelle “**impossibili**” (quando l’utilizzatore non legge il libretto di istruzioni di T e scrive sul nastro un input non conforme alle specifiche): per ciascuna di queste coppie impossibili ha scritto una quintupla che porta $T$ in $q_R$, progettando una **funzione $P$ totale**
- Chi ha progettato $T$ ha deciso che se un utilizzatore è stato poco accorto e non ha rispettato le specifiche… peggio per lui! E, semplicemente, chi ha progettato T ha scritto solo le quintuple per le coppie (stato,simbolo) significative. E, così, ha progettato una **funzione $P$ non totale**

Possiamo ora rispondere alla domanda “ma se T è un riconoscitore e ad una coppia (q,s) non è associata alcuna quintupla in P?: in questo caso, possiamo assumere che, in tal caso, $T$ rigetti
- è come se, implicitamente, aggiungessimo a P la quintupla $\langle q , s, s, q_R , F\rangle$ 

## E se P non fosse una funzione?

E che vuol dire “e se $P$ non fosse una funzione?”?!

Ma, prima ancora, cosa vuol dire che $P$ è una funzione?

Beh, questo è facile: se $P$ è una funzione, allora, per ogni stato q e per ogni carattere a, non possono esistere due quintuple che iniziano con la coppia (q,a)

In effetti, una quintupla $\langle q_1 , a, b, q_2 , m\rangle$, per come la abbiamo definita, ci dice che: se siamo nello stato q1 e leggiamo il carattere a allora dobbiamo comportarci in un certo modo – e non abbiamo scelta: trovandoci nello stato $q_1$ e leggendo il carattere a non possiamo far altro che scrivere b, entrare nello stato $q_2$ e muovere come specificato da m la testina.

Quindi, una quintupla è un ordine

E, quindi, da quello che abbiamo detto fino ad ora, non avrebbe senso avere due quintuple $\langle q_1 , a, b, q_2 , m\rangle$ e $\langle q_1 , a, b', q_2' , m\rangle$ : come dovremmo mai comportarci trovandoci nello stato $q_1$ e leggendo il carattere a?!

Possiamo anche vedere una quintupla come una indicazione precisa e non ambigua circa quale operazione eseguire per giungere alla soluzione

Una indicazione che viene fornita da chi ha progettato la macchina di Turing

E se costui, il progettista, arrivato ad un certo punto non sapesse bene come continuare?

Potrebbe dirci “se sei nello stato q e leggi il simbolo a, non so bene quale è la cosa giusta da fare ma, di certo, devi fare una di queste cose: {elenco di cose da fare fra cui scegliere}. Decidi un po’ tu…”

E come farebbe costui a comunicarci questa cosa? Ma con tante quintuple che iniziano con la stessa coppia stato interno – simbolo letto!

**Esempio** : $\langle q , a, b_1, q_1 , m_1\rangle,\dots,\langle q , a, b_k, q_k , m_k\rangle$ 

Cosa accade quando l’insieme delle quintuple di una macchina $T$ ha la multi-quintupla sopra e, durante una computazione $T(x)$, si trova nello stato interno q e legge il carattere a?

Possiamo descrivere il comportamento di $T$ in due modi diversi:

- $T$ diventa una macchina parallela
- $T$ chiede l’intervento di un "genio"

i due modi diversi sono **equivalenti**

### Una macchina parallela

In questo caso, quando $T$ si trova nello stato q e legge il simbolo a, le k quintuple $\langle q , a, b_1, q_1 , m_1\rangle,\dots,\langle q , a, b_k, q_k , m_k\rangle$, $T$ le esegue tutte,in parallelo!

Avviene la transizione dallo stato globale di partenza a k stati globali differenti
- che proseguono la computazione, ognuno per conto suo

E se, successivamente, da uno di questi stati globali ci si troverà a dover eseguire un’altra multi-quintupla, il processo di moltiplicazione si ripeterà
- diventerà una specie di albero

![[appunti asd/mod ii/immagini/Pasted image 20230316121345.png|center|500]]

Già, ma, allora, quale è l’esito di una computazione di una macchina capace di auto-replicarsi in innumerevoli copie parallele?

Come facciamo a dire quando una computazione di tale macchina accetta e quando rigetta? Come facciamo a sapere se la soluzione all’istanza x del nostro problema è 0 oppure 1? A quale delle copie parallele dobbiamo dar credito?

Per rispondere, dobbiamo prima chiarire una questione: anche se stiamo parlando di funzioni a valori in {0,1}, c’è, in realtà, una certa asimmetria fra i due valori. O meglio, c’è una asimmetria fra gli stati $q_A$ e $q_R$
- ad un riconoscitore è richiesto di _riconoscere_ le parole che **soddisfano** una certa proprietà - ad esempio, deve riconoscere le parole palindrome
- non di riconoscere le parole che _**non**_ soddisfano quella proprietà – per questo insieme di parole, se ci interessa individuarle, potremmo progettare un altro riconoscitore!

Quindi, in effetti, quel che ci interessa “di più” è lo stato $q_A$ – possiamo dire che arriviamo alla soluzione quando la macchina raggiunge lo stato $q_A$

Ragioniamo: l’idea delle multi-quintuple è che ci vengono mostrate tante strade possibili che potrebbero “portarci a destinazione” – ossia, allo stato qA

Naturalmente, non tutte le strade portano alla soluzione.

**Ma basta che ce ne sia una, di strada che porta a destinazione!**

Quindi, diciamo che: la computazione di una macchina parallela:
- **accetta** se esiste almeno un percorso nell’albero che porta la macchina nello stato $q_A$
- **rigetta** se tutti i percorsi nell’albero portano nello stato $q_R$– ossia se il percorso che porta a destinazione proprio non esiste!

### "Genio"

In questo caso, quando $T$ si trova nello stato q e legge il simbolo a, e $P$ contiene le k quintuple $\langle q , a, b_1, q_1 , m_1\rangle,\dots,\langle q , a, b_k, q_k , m_k\rangle$, $T$ chiama un "**genio**" e quello _**sceglie**_ quale di queste quintuple eseguire!

Così, la computazione diventa una sequenza di scelte del genio

Per questo la computazione di $T$ prende il nome di _**non deterministica**_
- perché il suo esito non è completamente determinato dal suo input

Cioè: se una macchina di Turing non ha multi-quintuple, allora, per ogni input x, la computazione $T(x)$ avrà sempre lo stesso esito

- se eseguiamo $T(x)$ ed essa termina in $q_A$, e poi ripetiamo $T(x)$ un milione di volte, ogni ripetizione terminerà in $q_A$
- e lo stesso vale se la prima esecuzione di $T(x)$ termina in $q_R$
- per questo una macchina che **non** ha multi-quintuple è **_deterministica_**

Se, invece, $T$ contiene multi-quintuple, $T$ è non deterministica, allora esecuzioni diverse di $T(x)$ possono avere esiti diversi!

Già, ma, allora, quale è l’esito di una computazione di una macchina non deterministica $T$ nel modello in cui interviene il genio?
- Anzi, visto che la macchina è non deterministica, chiamiamola NT

Come facciamo a dire quando $NT(x)$ accetta e quando rigetta? Come facciamo a sapere se la soluzione all’istanza x del nostro problema è 0 oppure 1?

La risposta è analoga al modello parallelo e, come in quel caso, è asimmetrica:

- $NT(x)$ **accetta** se esiste almeno una scelta di multi-quintuple che porta la macchina nello stato $q_A$
- $NT(x)$ **rigetta** se qualunque scelta di multi-quintuple porta la macchina nello stato $q_R$

## Equivalenza tra i modelli

In definitiva

- una macchina parallela accetta se esiste un percorso nell’albero che la fa entrare nello stato $q_A$ e rigetta se tutti i percorsi la fanno entrare nello stato $q_R$
- una macchina genio-dotata accetta se esiste una scelta di quintuple che la fa entrare nello stato $q_A$ e rigetta se tutte le scelte di quintuple la fanno entrare nello stato $q_R$

I due modelli sono **equivalenti**!

Sono due modelli, due modi, in cui possiamo descrivere una macchina di Turing non deterministica

# Determinismo e non determinismo

Ricapitolando:

- una macchina di Turing $T$ è deterministica se, per ogni stato q e per ogni carattere a, l’insieme P delle sue quintuple non contiene più di una quintupla che inizia con (q,a)
- una macchina di Turing $NT$ è non deterministica se esistono uno stato q e un carattere a tali che l’insieme P delle sue quintuple contiene due o più quintuple che iniziano con (q,a)
- consideriamo solo macchine non deterministiche di tipo riconoscitore

Una computazione non deterministica contiene tante computazioni deterministiche – una per ciascun ramo dell’albero

>[!definition]- Grado di non determinismo
>Il **grado di non determinismo** di una macchina non deterministica $NT$ è il massimo numero di quintuple che iniziano con la stessa coppia stato-carattere, ossia, $$max_{q,a}|\{\langle q,a,b,q_1,m\rangle\in P\}|$$

Naturalmente, il grado di non determinismo di una macchina definita sull’alfabeto $\Sigma$  e sull’insieme degli stati Q può essere al massimo : 
$$|\Sigma|\times|Q|\times 3$$
ed è, quindi, **costante**