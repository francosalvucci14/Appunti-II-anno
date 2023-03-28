
# Modelli di calcolo

Siamo al paragrafo 3.3 della dispensa 3, dove vengono definiti un sacco di modelli di calcolo
che, guarda caso, sono tutti basati sullo stesso concetto di “operazione elementare” utilizzato da Turing

Ebbene: per tutti i modelli di calcolo definiti fino ad ora, è stato dimostrato che sanno “risolvere” tutti e soli i problemi che possono essere “risolti” mediante la Macchina di Turing

Ossia, tutti i modelli di calcolo introdotti sino ad ora sono **Turing-equivalenti**

# Tesi di Church-Turing

Questa tesi assume che non esista un modello di calcolo più potente della Macchina di Turing: dato un qualunque altro modello di calcolo **M** :
- se un linguaggio L è decidibile/accettabile nel modello M allora L è decidibile/accettabile nel modello Macchina di Turing
- se una funzione f è calcolabile nel modello M allora f è calcolabile nel modello Macchina di Turing
- e viceversa
Purché **M** sia un modello” ragionevole”
- ossia, sia basato sul concetto di operazione elementare del quale abbiamo parlato diffusamente

Dunque:

>[!quote]- Tesi
>è calcolabile tutto e solo ciò che può essere calcolato dalla Macchina di Turing

>[!warning]
>Questa è una tesi,non è un teorema, il che significa che non è stata ancora dimostrata
>
>E sembra difficile riuscire a dimostrarla: sembra difficile riuscire a prevedere i modelli di calcolo che potrebbero essere definiti nel futuro…
>Tuttavia, sembra poco probabile riuscire a progettare un modello di calcolo che non la soddisfi ,e non dimentichiamolo, tutti i modelli di calcolo esistenti la soddisfano
>infatti, **è generalmente accettata!**

# Il modello di calcolo PascalMinimo

È un linguaggio di programmazione – perché ogni linguaggio di programmazione è un modello di calcolo!
Dispone di tutte le istruzioni “tipiche” dei linguaggi di programmazione
- istruzione di assegnazione: $a\leftarrow b$ 
- istruzione condizionale **if … then ... else**
- istruzioni di loop **while ( … ) do e for (...)**
- funzioni
- istruzioni per l’I/O
- ecc. ecc.

E dispone di variabili semplici (intere, caratteri, ...) ma anche di variabili che corrispondono a collezioni di oggetti – insiemi e, soprattutto, **array**

E la descrizione di questo linguaggio si trova a pag. 7 della dispensa 3

Nella dispensa 3, a partire da pag. 7, si accenna alla dimostrazione che il modello di calcolo PascalMinimo è equivalente alla Macchina di Turing

- nel Teorema 3.5 si dà un’idea (grossolana) di come “trasformare” un programma in PascalMinimo in una macchina di Turing che “faccia le stesse cose”

- nel Teorema 3.6 si dà un’idea (abbastanza precisa) di come “trasformare” una macchina di Turing in un programma in PascalMinimo che “faccia le stesse cose”

>[!definition]- Teorema 3.5: 
>Per ogni programma scritto in accordo con il linguaggio di programmazione PascalMinimo, esiste una macchina di Turing T di tipo trasduttore che scrive sul nastro di output lo stesso valore fornito in output dal programma. 

Sulla dispensa viene descritta solo l’idea della dimostrazione
- in particolare, viene mostrato come “trasformare” un programma in PascalMinimo in una macchina di Turing di tipo trasduttore solo nel caso in cui il programma non utilizzi variabili strutturate come, ad esempio, gli array
	- se il programma utilizzasse qualche array, la “trasformazione” sarebbe enormemente più complicata!

>[!definition]- Teorema 3.6: 
>Per ogni macchina di Turing deterministica T di tipo riconoscitore ad un nastro esiste un programma $A_T$ scritto in accordo alle regole del linguaggio PascalMinimo tale che, per ogni parola x, se T (x) termina nello stato finale $q_F\in\{q_A,q_R\}$ allora $A_T$ con input x restituisce $q_F$ in output. 

Dimostriamo questo teorema progettando un programma U  che si comporta come la macchina Universale:
- utilizzando opportune strutture dati per rappresentare  le quintuple di una generica macchina di Turing , e il suo stato iniziale, e i suoi stati finali
- e altre opportune strutture dati per rappresentare un input di quella generica macchina,
- fornendo in input ad U le descrizioni di una data macchina T e di un suo dato input x (in accordo alle strutture dati utilizzate)
- l’esecuzione di U sul suo input restituisce un output che corrisponde allo stato in cui terminerebbe la computazione T(x)
	- o che non termina qualora T(x) non terminasse

Per memorizzare le quintuple della macchina T che si vuole simulare, utilizziamo i 5 array Q1, S1, S2, Q2, M:
- e usiamo i valori -1, 0, 1 per rappresentare i movimenti della testina ‘sinistra’, ‘ferma’, ‘destra’
Se la i-esima quintupla di T è $\langle q,a,b,q',m\rangle$ ,  allora avremo $$Q1[ i ] =q, S1[ i ] = a, S2[ i ] = b, Q2[ i ] = q’, M[ i ] = -1$$
- $Q1[i]$ memorizza lo stato in cui si deve trovare la macchina per eseguire la quintupla i, $Q2[i]$ memorizza lo stato in cui deve entrare la macchina dopo aver eseguito la quintupla i, e analogamente per $S1[i], S2[i]\space e\space M[i]$

Rappresentiamo il nastro di T mediante l’array N, che, per semplicità, ammettiamo possa avere anche indici negativi

## Un programma che simula U

![[appunti fi/mod ii/immagini/Pasted image 20230328164147.png|center|600]]

![[appunti fi/mod ii/immagini/Pasted image 20230328164835.png|center|600]]

![[appunti fi/mod ii/immagini/Pasted image 20230328164905.png|center|600]]

![[appunti fi/mod ii/immagini/Pasted image 20230328164932.png|center|600]]

### Macchina non deterministica in PascalMinimo

Guardiamo insieme ora l’algoritmo in PascalMinimo che simula una macchina di Turing non deterministica (che si trova al paragrafo 3.4)

L’algoritmo implementa in PascalMinimo la coda di rondine con ripetizioni che abbiamo descritto informalmente nel corso della Lezione 4, e che dimostra il Teorema 2.1 (Dispensa 2):
- inizializza un contatore i a 1
- simula tutte le computazioni deterministiche di i istruzioni
	- se una di esse accetta, allora accetta
	- altrimenti; se tutte rigettano, allora rigetta
se al passo precedente non hai terminato (ossia, nessuna computazione di i passi ha accettato e almeno una di esse non ha rigettato), allora incrementa il valore di i e ripeti il passo precedente

E tutto ciò si traduce nel seguente codice

![[appunti fi/mod ii/immagini/Pasted image 20230328165336.png|center|600]]

ove la simulazione di tutte le computazioni deterministiche è eseguita dall’invocazione della funzione ricorsiva simulaRicorsivo($q_0$ , 1, N , i) 
- i cui parametri sono: lo stato interno ($q_0$), la posizione della testina (1) e il contenuto del nastro (N) della macchina non deterministica quando ha inizio la simulazione, e la lunghezza (i) delle computazioni da simulare

Ecco lo schema della funzione ricorsiva

![[appunti fi/mod ii/immagini/Pasted image 20230328165502.png|center|600]]

![[appunti fi/mod ii/immagini/Pasted image 20230328165541.png|center|600]]







