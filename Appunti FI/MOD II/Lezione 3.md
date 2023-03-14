
# Tanti modelli di macchine di Turing

´Siamo al paragrafo 2.4 della dispensa 2 (pag. 6). In questo paragrafo vengono introdotti diversi modelli di macchine di Turinq

- ´Macchine con **tanti nastri** con **testine indipendenti** : quando viene eseguita una quintupla, la testina su un nastro si può muovere come gli pare, indipendentemente da come si muovono le testine sugli altri nastri)
- ´Macchine con **tanti nastri** con **testine solidali** : quando viene eseguita una quintupla, se la testina su un nastro si muove in una certa direzione, anche le testine sugli altri nastri si muovono nella stessa direzione
- ´Macchine che usano un **alfabeto con tanti simboli**
- ´Macchine che utilizzano un **alfabeto binario**, ossia, con due soli simboli (0 e 1)

´e si dimostra che “**tutto quello che riusciamo a fare con una macchina di uno qualsiasi di questi modelli, riusciamo a farlo anche con una macchina di uno qualsiasi degli altri modelli**”

## Testine indipendenti = Testine solidali

´Naturalmente, poiché una macchina a testine solidali è una particolare macchina a testine indipendenti nella quale, ogni volta che viene eseguita una quintupla, tutte le testine si muovono allo stesso modo, allora **tutto ciò che facciamo con il modello a testine indipendenti riusciamo a farlo anche con il modello a testine solidali**

´Mostriamo ora l’inverso, ossia, che _tutto ciò che facciamo con il modello a testine indipendenti riusciamo a farlo anche con il modello a testine solidali_

- ´lo facciamo in un caso particolare: quando la macchina a testine indipendenti ha 2 nastri
- ´Ma si generalizza a quanti nastri ci pare

´Sia T una macchina a 2 nastri con testine indipendenti: una sua quintupla è $\langle q_1 , (a,b), (c,d), q_2 , (m_1,m_2)\rangle$ dove $m_1$ è il movimento della testina sul primo nastro e $m_2$ è il movimento della testina sul secondo nastro

´Vediamo come trasformare quella quintupla in **_un insieme di quintuple_** di una macchina $T'$ a tre nastri a testine solidali che “si comporta come” la quintupla di $T$

### Il caso $m_1$ = destra, $m_2$ = sinistra

´Cominciamo con il vedere cosa accade in T quando esegue $\langle q_1 , (a,b), (c,d), q_2 , (dx,sx)\rangle$ 

![[appunti fi/mod ii/immagini/Pasted image 20230314153319.png|center|500]]

´Come facciamo ad ottenere lo stesso comportamento in T’?

´Pensate come sarebbe facile se, dopo aver scritto c sul primo nastro e d sul secondo nastro, potessimo tirare il primo nastro a sinistra e il secondo nastro a destra (tenendo ferme le testine), come indicato dalle frecce rosse nel disegno a sinistra, per ottenere lo stato globale nel disegno a destra:

![[appunti fi/mod ii/immagini/Pasted image 20230314153527.png|center|550]]

´Ma i nastri non si possono tirare da una parte o dall’altra…

´Allora, dobbiamo armarci di santa pazienza e

- ´ **ricordandoci la coppia di celle dalla quale partiamo**

´spostarci sul carattere più a destra del primo nastro,´leggere quel carrattere e **ricordandolo**, cancellarlo e copiarlo sulla cella a sinistra ricordando il carattere che vi era scritto in precedenza, e ripetere questo “shift” dei caratteri sul primo nastro, fino ad aver raggiunto il carattere più a destra

´“memorizzo $a_8$” = entro in uno stato che dipende da $a_8$, del tipo $q(a_8)$ 

![[appunti fi/mod ii/immagini/Pasted image 20230314153719.png|center|500]]

´... Terminato lo “shift” sul primo nastro, **sempre ricordandoci da quali celle eravamo partiti, dobbiamo**
- ´spostarci sul carattere più a sinistra del secondo nastro
- ´leggere quel carrattere e ricordandolo, cancellarlo e copiarlo sulla cella a destra ricordando il carattere che vi era scritto in precedenza, e ripetere questo “shift” dei caratteri sul secondo nastro, fino ad aver raggiunto il carattere più a destra

![[appunti fi/mod ii/immagini/Pasted image 20230314153945.png|center|500]]

´Ed ora, non ci resta che posizionarci sulla cella dalla quale eravamo partiti

´Ma come facciamo a ricordarci da dove eravamo partiti?!

´Abbiamo bisogno di un terzo nastro sul quale scrivere un carattere speciale, tipo "$\star$", che faccia da “**segnaposto**”

´E questo lo illustriamo nelle figure alle prossime pagine:

- T’ ha appena sostituto ‘a’ con ‘c’ sul primo nastro e ‘b’ con ‘d’ sul secondo nastro, e si prepara ad eseguire lo shift sul primo nastro (figura A)
- T’ ha appena finito lo shift sul primo nastro e si prepara ad eseguire lo shift sul secondo nastro (figura B)
- T’ ha appena finito lo shift sul secondo nastro e si prepara a posizionare le testine (figura C)
- T’ ha posizionato le testine nella posizione indicata da "$\star$": le testine sui primi due nastri leggono gli stessi caratteri letti dalle testine di T al termine dell’esecuzione della quintupla $\langle q_1 , (a,b), (c,d), q_2 , (dx,sx)\rangle$ (figura D)

´la simulazione della quintupla $\langle q_1 , (a,b), (c,d), q_2 , (dx,sx)\rangle$ di T è terminata!

**Figura A**:
![[appunti fi/mod ii/immagini/Pasted image 20230314154815.png|center|300]]

**Figura B:**
![[appunti fi/mod ii/immagini/Pasted image 20230314160211.png|center|300]]

**Figura C**:
![[appunti fi/mod ii/immagini/Pasted image 20230314160248.png|center|300]]

**Figura D**:
![[appunti fi/mod ii/immagini/Pasted image 20230314160326.png|center|300]]

´la simulazione della quintupla $\langle q_1 , (a,b), (c,d), q_2 , (dx,sx)\rangle$ di T è terminata!







