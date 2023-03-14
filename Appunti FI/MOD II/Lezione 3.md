
# Tanti modelli di macchine di Turing

Siamo al paragrafo 2.4 della dispensa 2 (pag. 6). In questo paragrafo vengono introdotti diversi modelli di macchine di Turinq

- Macchine con **tanti nastri** con **testine indipendenti** : quando viene eseguita una quintupla, la testina su un nastro si può muovere come gli pare, indipendentemente da come si muovono le testine sugli altri nastri)
- Macchine con **tanti nastri** con **testine solidali** : quando viene eseguita una quintupla, se la testina su un nastro si muove in una certa direzione, anche le testine sugli altri nastri si muovono nella stessa direzione
- Macchine che usano un **alfabeto con tanti simboli**
- Macchine che utilizzano un **alfabeto binario**, ossia, con due soli simboli (0 e 1)

e si dimostra che “**tutto quello che riusciamo a fare con una macchina di uno qualsiasi di questi modelli, riusciamo a farlo anche con una macchina di uno qualsiasi degli altri modelli**”

## Testine indipendenti = Testine solidali

Naturalmente, poiché una macchina a testine solidali è una particolare macchina a testine indipendenti nella quale, ogni volta che viene eseguita una quintupla, tutte le testine si muovono allo stesso modo, allora **tutto ciò che facciamo con il modello a testine indipendenti riusciamo a farlo anche con il modello a testine solidali**

Mostriamo ora l’inverso, ossia, che _tutto ciò che facciamo con il modello a testine indipendenti riusciamo a farlo anche con il modello a testine solidali_

- lo facciamo in un caso particolare: quando la macchina a testine indipendenti ha 2 nastri
- Ma si generalizza a quanti nastri ci pare

Sia T una macchina a 2 nastri con testine indipendenti: una sua quintupla è $\langle q_1 , (a,b), (c,d), q_2 , (m_1,m_2)\rangle$ dove $m_1$ è il movimento della testina sul primo nastro e $m_2$ è il movimento della testina sul secondo nastro

Vediamo come trasformare quella quintupla in **_un insieme di quintuple_** di una macchina $T'$ a tre nastri a testine solidali che “si comporta come” la quintupla di $T$

### Il caso $m_1$ = destra, $m_2$ = sinistra

Cominciamo con il vedere cosa accade in T quando esegue $\langle q_1 , (a,b), (c,d), q_2 , (dx,sx)\rangle$ 

![[appunti fi/mod ii/immagini/Pasted image 20230314153319.png|center|500]]

Come facciamo ad ottenere lo stesso comportamento in T’?

Pensate come sarebbe facile se, dopo aver scritto c sul primo nastro e d sul secondo nastro, potessimo tirare il primo nastro a sinistra e il secondo nastro a destra (tenendo ferme le testine), come indicato dalle frecce rosse nel disegno a sinistra, per ottenere lo stato globale nel disegno a destra:

![[appunti fi/mod ii/immagini/Pasted image 20230314153527.png|center|550]]

Ma i nastri non si possono tirare da una parte o dall’altra…

Allora, dobbiamo armarci di santa pazienza e

-  **ricordandoci la coppia di celle dalla quale partiamo**

spostarci sul carattere più a destra del primo nastro,leggere quel carrattere e **ricordandolo**, cancellarlo e copiarlo sulla cella a sinistra ricordando il carattere che vi era scritto in precedenza, e ripetere questo “shift” dei caratteri sul primo nastro, fino ad aver raggiunto il carattere più a destra

“memorizzo $a_8$” = entro in uno stato che dipende da $a_8$, del tipo $q(a_8)$ 

![[appunti fi/mod ii/immagini/Pasted image 20230314153719.png|center|500]]

... Terminato lo “shift” sul primo nastro, **sempre ricordandoci da quali celle eravamo partiti, dobbiamo**
- spostarci sul carattere più a sinistra del secondo nastro
- leggere quel carrattere e ricordandolo, cancellarlo e copiarlo sulla cella a destra ricordando il carattere che vi era scritto in precedenza, e ripetere questo “shift” dei caratteri sul secondo nastro, fino ad aver raggiunto il carattere più a destra

![[appunti fi/mod ii/immagini/Pasted image 20230314153945.png|center|500]]

Ed ora, non ci resta che posizionarci sulla cella dalla quale eravamo partiti

Ma come facciamo a ricordarci da dove eravamo partiti?!

Abbiamo bisogno di un terzo nastro sul quale scrivere un carattere speciale, tipo "$\star$", che faccia da “**segnaposto**”

E questo lo illustriamo nelle figure alle prossime pagine:

- T’ ha appena sostituto ‘a’ con ‘c’ sul primo nastro e ‘b’ con ‘d’ sul secondo nastro, e si prepara ad eseguire lo shift sul primo nastro (figura A)
- T’ ha appena finito lo shift sul primo nastro e si prepara ad eseguire lo shift sul secondo nastro (figura B)
- T’ ha appena finito lo shift sul secondo nastro e si prepara a posizionare le testine (figura C)
- T’ ha posizionato le testine nella posizione indicata da "$\star$": le testine sui primi due nastri leggono gli stessi caratteri letti dalle testine di T al termine dell’esecuzione della quintupla $\langle q_1 , (a,b), (c,d), q_2 , (dx,sx)\rangle$ (figura D)

la simulazione della quintupla $\langle q_1 , (a,b), (c,d), q_2 , (dx,sx)\rangle$ di T è terminata!

**Figura A**:
![[appunti fi/mod ii/immagini/Pasted image 20230314154815.png|center|300]]

**Figura B:**
![[appunti fi/mod ii/immagini/Pasted image 20230314160211.png|center|300]]

**Figura C**:
![[appunti fi/mod ii/immagini/Pasted image 20230314160248.png|center|300]]

**Figura D**:
![[appunti fi/mod ii/immagini/Pasted image 20230314160326.png|center|300]]

la simulazione della quintupla $\langle q_1 , (a,b), (c,d), q_2 , (dx,sx)\rangle$ di T è terminata!

Riassumendo: una computazione di T’ _simula_ una computazione di T – ossia, impiegando un (bel) po’ di tempo in più, <u>fa passo passo le stesse cose che fa T</u>

Più in particolare, per ogni quintupla p in T, in T’ è definito un insieme p’ di quintuple tali che: quando

- i contenuti dei nastri di T e dei primi due nastri di T’ sono uguali e
- le testine di T e le prime due testine di T’ leggono gli stessi caratteri e
- la quintupla p può essere eseguita da T

allora le quintuple nell’insieme p’ possono essere eseguite da T’ e, inoltre,al termine dell’esecuzione di p da parte di T e dell’insieme p’ da parte di T’

- i contenuti dei primi due nastri di T’ e dei nastri di T sono uguali e
- le testine di T e le prime due testine di T’ leggono gli stessi caratteri

Infatti:

- T dopo aver eseguito la quintupla $\langle q_1 , (a,b), (c,d), q_2 , (dx,sx)\rangle$, figura A
- T’ dopo aver eseguito l’insieme di quintuple che corrispondono a $\langle q_1 , (a,b), (c,d), q_2 , (dx,sx)\rangle$ (subito dopo, T’ entra nello stato $q_2$) , figura B

**Figura A**
![[appunti fi/mod ii/immagini/Pasted image 20230314162711.png|center|300]]

**Figura B**
![[appunti fi/mod ii/immagini/Pasted image 20230314162808.png|center|300]]


E la codifica (o meglio, la _formalizzazione_) di questo procedimento si trova a pag.  6-8 della dispensa 2

Naturalmente per le altre coppie di spostamenti (m1=fermo e m2=sinistra, m1=fermo e m2=destra, m1=sinistra e m2=fermo, m1=destra e m2= fermo, m1=sinistra e m2=destra) si procede in modo analogo

In definitiva, abbiamo _**simulato**_ il comportamento di una macchina con k nastri e testine indipendenti mediante una macchina a k+1 nastri e testine solidali

Abbiamo, dunque, introdotto la tecnica della **simulazione**

- che consiste nel progettare una macchina T’ con certe caratteristiche che “fa la stessa cosa” di un’altra macchina T che ha altre caratteristiche

### Da tanti nastri a un solo nastro

Siamo al sotto-paragrafo 2.4.2 (pag. 9) della dispensa 2

Vogliamo far vedere che tutto quello che possiamo fare con macchine “ricche” (che hanno tanti nastri) possiamo farlo anche con macchine “povere” (che hanno un nastro solo, meschine)

Abbiamo una macchina $T_k$ che ha k nastri

Vogliamo far vedere che esiste una macchina $T$ con un nastro solo che fa le stesse cose che fa $T_k$

E come facciamo a far vedere che esiste una macchina T con un nastro solo che fa le stesse cose che fa $T_k$ ?

- Ancora con la tecnica della simulazione!

Costruiamo la macchina T a partire da $T_k$ : e facciamo l’esempio con k=3

- grazie al teorema precedente, **possiamo supporre che $T_3$ sia a testine solidali**

Per prima cosa, scriviamo l’input di $T_3$ sull’unico nastro di T

- assegniamo “indirizzi” alle celle dei nastri di $T_3$ in modo tale che le testine solidali di $T_3$ siano sempre posizionate su celle che hanno lo stesso indirizzo
	- praticamente, le celle che hanno lo stesso “indirizzo” sono una ”colonna di celle”
- se $(x_{1_1}, x_{1_2}, x_{1_3})$ sono i tre caratteri scritti sulle celle “di indirizzo 1” dei 3 nastri di $T_3$, noi scriviamo $x_{1_1}$ sulla cella 1, $x_{1_2}$ sulla cella 2 e $x_{1_3}$ sulla cella 3 di T

e proseguiamo così per tutto l’input di $T_3$ (osservate che la tripla di caratteri che occupa le celle di indirizzo h in $T_3$ viene scritto nelle celle 3h-2, 3h-1, 3h di T )

![[appunti fi/mod ii/immagini/Pasted image 20230314163848.png|center|500]]

A questo punto, sia $\langle q_1, (x_{1_1}, x_{1_2}, x_{1_3}), (y_{1_1}, y_{1_2}, y_{1_3}), q_2 , m\rangle$ una quintupla di T3

Naturalmente T non riesce a vedere contemporaneamente $x_{1_1}, x_{1_2}, x_{1_3}$

Perciò anche se si trova nello stato $q_1$ e legge $x_{1_1}$, la quintupla $\langle q_1, (x_{1_1}, x_{1_2}, x_{1_3}), (y_{1_1}, y_{1_2}, y_{1_3}), q_2 , m\rangle$ T non può eseguirla!

![[appunti fi/mod ii/immagini/Pasted image 20230314164600.png|center|300]]

per poter capire se può eseguire oppure no la quintupla $\langle q_1, (x_{1_1}, x_{1_2}, x_{1_3}), (y_{1_1}, y_{1_2}, y_{1_3}), q_2 , m\rangle$, T deve leggere 3 caratteri consecutivi e memorizzarli (nello stato interno)

![[appunti fi/mod ii/immagini/Pasted image 20230314164912.png|center|500]]

Una volta letti i 3 caratteri $x_{1_1}, x_{1_2}, x_{1_3}$ ed averli memorizzati nel suo stato (insieme con lo stato interno di partenza $q_1$), deve tornare indietro di 3 posizioni per predisporsi a scrivere $y_{1_1}, y_{1_2}, y_{1_3}$

Finalmente, può scrivere (in 3 passi) $y_{1_1}$, poi $y_{1_2}$ , poi $y_{1_3}$ 

![[appunti fi/mod ii/immagini/Pasted image 20230314165219.png|center|500]]

E, infine, T può simulare il movimento delle testine di $T_3$

Si consiglia un'approfondimento sulle dispense

### Da un alfabeto ricco a uno binario

Siamo al paragrafo 2.5, a pag. 10 della dispensa 2

Partiamo da una macchina T che è costruita su un alfabeto $\Sigma$ con tanti caratteri – un alfabeto ricco!

Si vuole mostrare che esiste una macchina $T_{01}$, costruita sull’alfabeto $\{0,1\}$, che fa le stesse cose di T

Visto che sappiamo che una macchina ad un nastro sa fare le stesse cose che sa fare una macchina a k nastri e viceversa, per semplificarci la vita prendiamo una macchina T con un nastro solo

- Che, detto meglio, diventa “**senza perdita di generalità, possiamo assumere che T abbia un solo nastro**”

Ancora una volta, utilizziamo la tecnica della simulazione: costruiamo una macchina $T_{01}$ che, passo passo, “simula” l’esecuzione delle quintuple di T

- e, per semplificarci la vita, dotiamo di tanti nastri la macchina T01

Partiamo dalla stessa codifica binaria b degli elementi di $\Sigma$ mostrata nel paragrafo 2.5: per ogni elemento $s\in\Sigma,b(s)$ è una parola costituita da $k=\lceil\log_2|\Sigma|\rceil$ caratteri "0" o "1"

Poi, per ogni elemento s di Σ e per ogni h compreso fra 1 e $k=\lceil\log_2|\Sigma|\rceil$, indichiamo con $b_h(s)$ l’h-esimo bit di b(s): ossia, $b(s) = b_1(s) b_2(s)... b_k(s)$

A questo punto, costruiamo $T_{01}$ come una macchina con k nastri e…

- osservazione: poiché $|\Sigma|$ è costante, allora anche k è costante!

Cominciamo con lo scrivere sui k nastri di $T_{01}$ la codifica binaria dell’input scritto sull’unico nastro di T

- Sia $x_1x_2 ... x_h$ l’input di T
- Nelle celle di indirizzo 1 dei nastri di $T_{01}$ scriviamo i simboli binari della codifica di $x_1$: se $b(x_1)=b_1(x_1) b_2(x_1)... b_k(x_1)$, allora scriviamo $b_1(x_1)$ nella cella 1 del primo nastro, $b_2(x_1)$ nella cella 1 del secondo nastro, e così via
- Nelle celle di indirizzo 1 dei nastri di $T_{01}$ scriviamo i simboli binari della codifica di $x_2$, ... e nelle celle di indirizzo k scriviamo i simboli binari della codifica di $x_k$.

**Esempio**

![[appunti fi/mod ii/immagini/Pasted image 20230314170549.png|center|500]]

A questo punto, una quintupla $\langle q_1 , a, c, q_2 , m\rangle$ di T diventa la quintupla$\langle q_1 , (b_1(a), b_2(a), ... b_k(a)), (b_1(c), b_2(c), ... b_k(c)), q_2 , m \rangle$ di $T_{01}$

Abbiamo visto come si fa a costruire una macchina che “fa le stesse cose” di un’altra macchina

Ma che vuol dire “fare le stesse cose”?

Beh, intanto, formalmente, “una macchina fa le stesse cose di un’altra macchina” si dice “**l’esito della computazione di una macchina su un input coincide con l’esito della computazione dell’altra macchina sullo stesso input (eventualmente codificato)**”

