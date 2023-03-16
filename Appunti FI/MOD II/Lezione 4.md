
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

