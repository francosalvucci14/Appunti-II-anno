# La macchina di Turing Universale

## Cosa è una macchina di Turing?

Una macchina di Turing è la descrizione di un procedimento per risolvere un problema

- decritto nel linguaggio delle quintuple
- ossia, è un procedimento per il modello di calcolo Macchina di Turing

Quindi, una macchina di Turing è un algoritmo

- e, se la facciamo lavorare su qualche input, quella, in qualche modo, ci calcola la soluzione per l’istanza del problema che gli abbiamo dato in input

e il dato in input, per una macchina di Turing, è una parola, costituita da caratteri di un certo alfabeto

- l’input è una **parola** – che viene scritta sul nastro della macchina

### Macchine e parole

Prendiamo una macchina di Turing definita cosi 
$$\langle\Sigma,Q,q_0,Q_F,P\rangle$$
Se decidiamo di costruire una parola secondo el regole seguenti : 
- il primo carattere della parola è $q_0$, che è seguito da un carattere non in $\Sigma$, diciamo $-$
- che è seguito da $q_A$, poi da $-$, poi da $q_R$,
- e poi, seguono, una di seguito all’altra, tutte le quintuple

la parola che abbiamo appena costrutiro definisce completamente T

Vediamo un esempio:

Prendiamo una macchina $T_{PAL}$ che termina in $q_A$ se la parola scritta (composta dai caratteri a e b) sul suo nastro ha lunghezza pari ed è palindroma

Il suo stato iniziale è $q_0$, il suo stato di accettazione è $q_A$, il suo stato di rigetto è $q_R$ e le sue quintuple sono:
- $\langle q_0,a,\square,q_a,D\rangle,\langle q_0,b,\square,q_b,D\rangle$
- $\langle q_a,a,a,q_a,D\rangle,\langle q_a,b,b,q_a,D\rangle,\langle q_b,a,a,q_b,D\rangle,\langle q_b,b,b,q_b,D\rangle$
- $\langle q_a,\square,\square,q_{a_1},S\rangle,\langle q_b,\square,\square,q_{b_1},S\rangle$
- $\langle q_{a_1},a,\square,q_2,S\rangle,\langle q_{a_1},b,b,q_R,F\rangle,\langle q_{b_1},a,a,q_R,F\rangle,\langle q_{b_1},b,\square,q_2,S\rangle$
- $\langle q_2,a,a,q_2,S\rangle,\langle q_2,b,b,q_2,S\rangle,\langle q_2,\square,\square,q_0,D\rangle$
- $\langle q_0,\square,\square,q_A,F\rangle$

A questo punto, $T_{PAL}$ è completamente descritta dalla parola seguente:
- $$\begin{align}&q_0-q_A-q_R\langle q_0,a,\square,q_a,D\rangle,\langle q_0,b,\square,q_b,D\rangle\\&\langle q_a,a,a,q_a,D\rangle,\langle q_a,b,b,q_a,D\rangle,\langle q_b,a,a,q_b,D\rangle,\langle q_b,b,b,q_b,D\rangle\\&\langle q_a,\square,\square,q_{a_1},S\rangle,\langle q_b,\square,\square,q_{b_1},S\rangle\\&\langle q_{a_1},a,\square,q_2,S\rangle,\langle q_{a_1},b,b,q_R,F\rangle,\langle q_{b_1},a,a,q_R,F\rangle,\langle q_{b_1},b,\square,q_2,S\rangle\\&\langle q_2,a,a,q_2,S\rangle,\langle q_2,b,b,q_2,S\rangle,\langle q_2,\square,\square,q_0,D\rangle\\&\langle q_0,\square,\square,q_A,F\rangle\end{align}$$
In definitiva, una macchina di Turing è una parola (costituita da caratteri dell'alfabeto $Q\cup\Sigma\cup\{-,\langle,\rangle,\square\}$)

Ma se è una parola, allora possiamo scriverla sul nastro di un'altra macchina di Turing (chiamiamola A) così che A lavori sulla nostra macchina come input

Ma perchè dovremmo?
- Per esempio, se sul nastro di A ci scriviamo, oltre alla parola che descrive la nostra macchina di Turing di partenza (chiamiamola T), anche un input x di T, allora A potrebbe simulare la computazione $T(x)$
- e dunque, se chiamiamo $p_T$ la parola che descrive T, l’esito della computazione $A(p_T, x)$ sarebbe uguale all’esito della computazione $T(x)$

### Oltre la macchina

Pensate se, per caso, riuscissimo a progettare una macchina di Turing U che prende in input due parole
- una parola $p_T$ che descrive una qualsiasi macchina di Turing T
- una parola x, input di T

e che riesce a simulare la computazione $T(x)$ – qualunque sia T

U sarebbe una macchina di Turing alla quale posso comunicare un algoritmo qualsiasi e un input per quell'algoritmo, e U esegue l'algoritmo su quell'input

U sarebbe l'algoritmo che descrive il comportamento di un calcolatore

Questa macchina prende il nome di _**macchina di Turing Universale**_

>[!info]
>La macchina viene descritta a fondo nel paragrafo 2.6 della dispensa 2 (da vedere)


## La macchina di Turing Universale

Intanto, progettiamo U in modo tale che sappia simulare soltanto macchine ad un nastro

Poi, dotiamo U di 4 nastri e testine indipendenti
- sul primo nastro viene inizialmente scritta la parola $p_T$ che descrive la macchina T la cui computazione deve essere simulata – e il contenuto di questo nastro non sarà mai modificato durante la computazione $U(T, x)$
- sul secondo nastro viene scritto l’input x della macchina T – e questo sarà il nastro sul quale avverrà la simulazione vera e propria della computazione $T(x)$
- sul terzo nastro, all’inizio della computazione, U copia lo stato iniziale di T – che, ricordiamo, è il primo simbolo di $p_T$
- sul quarto nastro, all’inizio della computazione, U copia lo stato di accettazione di T – che, ricordiamo, è il simbolo di $p_T$ a destra del primo $-$

**Esempio**

U prima che la computazione $U(p_{T_{PAL}},ababbbabaa)$ abbia inizio

![[appunti fi/mod ii/immagini/Pasted image 20230321134008.png|center|500]]

La computazione $U(p_{T_{PAL}},ababbbabaa)$ procede: U ha copiato lo stato iniziale di $T_{PAL}$ su $N_3$, lo stato di accettazione $T_{PAL}$ su $N_4$, e si prepara a simulare $T_{PAL}(x)$

![[appunti fi/mod ii/immagini/Pasted image 20230321134121.png|center|500]]

A questo punto, U ha copiato lo stato iniziale di T sul terzo nastro e lo stato di accettazione di T su quarto nastro. Per tutta la durata della simulazione che U sta per iniziare:

- il contenuto di $N_4$ non verrà mai modificato
- **$N_3$ conterrà sempre lo stato in cui si troverebbe T a quel punto della simulazione**

U inizia la simulazione di $T(x)$ vera e propria: che è una ripetizione dei passi seguenti

1. U cerca la quintupla di T da eseguire
2. se ha trovato la quintupla da eseguire, allora la esegue e torna al punto 1)
3. se non ha trovato la quintupla da eseguire, allora confronta il carattere letto sul terzo nastro (lo stato in cui si troverebbe T a questo punto della computazione) con il carattere letto sul quarto nastro (lo stato di accettazione di T)
	1. se sono uguali, allora accetta
	2. se sono diversi, rigetta

Vediamo i punti 1) e 2) in dettaglio

1. U cerca la quintupla di T da eseguire: la testina su $N_1$ è posizionata sul primo carattere $\langle$ ; U esegue i passi seguenti
	1. muove a destra di una posizione la testina su $N_1$
	2. se legge lo stesso carattere su $N_1$ e su $N_3$, allora U sta scandendo una quintupla di T che inizia con lo stato in cui si troverebbe T a questo punto della computazione; in questo caso muove a destra la testina su $N_1$ per posizionarla sul carattere a destra di ‘,’
		1. se legge lo stesso carattere su $N_2$ e $N_1$, allora ha trovato la quintupla da eseguire e passa al punto 2)
		2. se non legge lo stesso carattere su $N_2$ e $N_1$, allora non ha trovato la quintupla da eseguire: in questo caso, muove a destra la testina su $N_1$ alla ricerca del prossimo carattere $\langle$ : se lo trova allora torna al punto 1.1), se non lo trova allora ha scandito tutte le quintuple di T senza trovare quella da eseguire e passa al punto 3)
	3. se non legge lo stesso carattere su $N_1$ e su $N_3$, allora sta scandendo una quintupla di T che non inizia con lo stato in cui si troverebbe T a questo punto della computazione; in questo caso muove a destra la testina su $N_1$ alla ricerca del prossimo carattere $\langle$ : se lo trova allora torna al punto 1.1), se non lo trova allora ha scandito tutte le quintuple di T senza trovare quella da eseguire e passa al punto 3)

2. se U ha trovato la quintupla da eseguire, allora la esegue e torna al punto 1); la testina su $N_1$ è posizionata sul carattere uguale a quello letto dalla testina su $N_2$:
	1. muove a destra di due posizioni la testina su $N_1$: ora è posizionata sul carattere che deve essere scritto
	2. copia su $N_2$ il carattere che legge su $N_1$
	3. muove a destra di due posizioni la testina su $N_1$: ora è posizionata sul carattere che corrisponde allo stato in cui T deve entrare
	4. copia su $N_3$ il carattere che legge su $N_1$
	5. muove a destra di due posizioni la testina su $N_1$ : ora è posizionata sul carattere che descrive il movimento della testina
	6. se su $N_1$ legge ‘S’ allora sposta a sinistra la testina su $N_2$, se su $N_1$ legge ‘D’ allora sposta a destra la testina su $N_2$, se su $N_1$ legge ‘F’ allora non compie alcuna azione

Riferirsi alla figura relativa alla computazione $U(p_{T_{PAL}},ababbbabaa)$

Abbiamo tralasciato qualche dettaglio importante circa il funzionamento di U

Intanto, si osservi che le testine sui nastri 3 e 4 non si muovono mai
- inoltre, dopo che nella prima cella di $N_4$ è stato scritto lo stato di accettazione della macchina “scritta” su $N_1$, il contenuto di $N_4$ non verrà mai più modificato

Qual'è l'alfabeto di U? 

Finora abbiamo usato l'insieme $Q\cup\Sigma\cup\{-,\langle,\rangle,\square\}$ come alfabeto

Ma ogni macchina T ha un suo insieme degli stati $Q$ e un suo alfabeto $\Sigma$ e noi vogliamo che U sappia simulare qualunque macchina di Turing T.

Allora,dato che l'alfabeto di U non può essere infinito, codifichiamo tutto in binario (usando la codifica vista in precedenza (sta sulla dispensa))

Per il procedimento vedi pagina 11 della dispensa 2

A questo punto, quello che cambia rispetto alla descrizione di U è la gestione del passo 1.2):
- se legge lo stesso carattere su $N_1$ e su $N_3$, allora U sta scandendo una quintupla di T che inizia con lo stato in cui si troverebbe T a questo punto della computazione; in questo caso muove a destra la testina su $N_1$ per posizionarla sul carattere a destra di ‘,’
Adesso, su $N_3$ non è scritto un singolo carattere, ma una parola di k bit

Perciò, “se legge lo stesso carattere su $N_1$ e su $N_3$” diventa ora “se la sequenza di k bit sul nastro $N_1$ che inizia dal punto in cui è posizionata la testina coincide con la sequenza di k bit sul nastro $N_3$”
- quella che prima era una quintupla, deve essere ora trasformata in un insieme di quintuple che permettono di eseguire k confronti

La descrizione completa della macchina U che lavora con questa codifica binaria (che è un lavoraccio tecnico) si trova nel paragrafo 2.6. 

Un’ultima questione: e se, putacaso, la parola scritta sul primo nastro di U non corrisponde alla descrizione di una macchina di Turing?

Abbiamo due possibilità per gestire questa questione

- prima di iniziare a copiare lo stato iniziale di T sul terzo nastro e lo stato di accettazione di T sul quarto nastro, U controlla che la parola scritta sul primo nastro sia effettivamente la descrizione di una macchina di Turing (ossia, soddisfi le specifiche descritte a pag. 11 della dispensa 2: se non è così, U termina nello stato di rigetto
- oppure, utilizziamo la regola che abbiamo illustrato nel paragrafo 2.3: se l’input non rispetta le specifiche… amen.


