
# Riduzioni e introduzione alla Teoria della Complessità Computazionale

## Usare la tecnica della "scatola nera"

Torniamo alla dimostrazione dell’indecidibilità dell’Halting Problem

Siamo partiti supponendo di avere una macchina T in grado di decidere $L_H$, e poi: 
- senza sapere come era fatta T (senza “aprirla”)
- abbiamo costruito una serie di altre macchine – T, T’, T’’, T* - che ci hanno portato dove volevamo
La macchina T’ la abbiamo costruita senza sapere come era fatta T

Ora, quando T’ usava T, T passava (come “parametro”) a T’ il suo stesso input (i,x)
In generale, possiamo utilizzare una macchina $T_0$ all’interno di un’altra macchina $T_1$ in un modo un po’ più complesso
- in effetti, il linguaggio deciso/accettato da T0  potrebbe anche essere molto diverso da quello deciso/accettato da T1 
- allora, potrebbe essere necessario “modificare” l’input di $T_1$ prima di “darlo in pasto” a $T_0$ 

**Esempio** : voglio costruire una macchina che decida il linguaggio $L_{P12}$ che contiene tutte (e sole) le parole palindrome di lunghezza pari costituite dai caratteri ‘1’ e ‘2’
- Questo linguaggio però somiglia molto al linguaggio già visto in precedenza, ovvero $L_{PPAL}$
- Ma invece che mettersi a ri-progettare una macchina di Turing da capo, possiamo usare quella per $L_{PPAL}$, andando però a trasformare le parole di $L_{P12}$ in parole di $L_{PPAL}$

Come fare?
Prendo il mio $x\in\{1,2\}^\star$ e procedo così:  assumendo $x = x_1 x_2\dots x_n$, per ogni $h =1, 2, \dots , n$ :
- se $x_h$ = ’1’ allora poniamo $y_h$ = ‘a’
- se $x_h$ = ’2’ allora poniamo $y_h$ = ‘b’
infine, poniamo $y = y_1 y_2\dots y_n$ .

Quello che ho ottenuto è quindi una parola $y\in\{a,b\}^\star$ che ha le seguenti caratteristiche
- se $x\in L_{P12}$ allora $y\in L_{PPAL}$
- se $x\not\in L_{P12}$ allora $y\not\in L_{PPAL}$

### Riduzioni (many-to-one)

Quello che abbiamo fatto, in realtà, è qualcosa di più di una semplice trasformazione di una parola in un’altra parola
Abbiamo progettato una funzione $f : \{1,2\}^\star\to\{a,b\}^\star$ tale che
1) f è _totale e calcolabile_ – ossia, 
	1) è definita per ogni parola $x\in\{1,2\}^\star$ e, inoltre, 
	2) esiste una macchina di Turing di tipo trasduttore $T_f$ tale che, per ogni parola $x\in\{1,2\}^\star$, la computazione $T_f (x)$ termina con la parola $f(x)\in\{a,b\}^\star$ scritta sul nastro di output
2) per ogni $x\in\{1,2\}^\star$ vale che: $x\in L_{P12}$ se e solo se $f(x)\in  L_{PPAL}$ $$\forall x\in\{1,2\}^\star [ x\in L_{P12}\iff f(x)\in  L_{PPAL} ]$$

La funzione f si chiama _**riduzione**_ da $L_{P12}$ a $L_{PPAL}$

E si dice che $L_{P12}$ è _**riducibile**_ a $L_{PPAL}$ e si scrive $L_{P12}\preceq L_{PPAL}$

Quello che abbiamo detto sino ad ora può essere generalizzato
Dati due linguaggi, $L_1\subseteq\Sigma_1^\star$  e $L_2\subseteq\Sigma_2^\star$,  diciamo che $L_1$ è riducibile a $L_2$ e scriviamo $L_1\preceq L_2$  se $\exists$ una funzione $f:\Sigma_1^\star\to\Sigma_2^\star$ tale che :
1) f è totale e calcolabile
2) $$\forall x\in\Sigma_1^\star [ x\in L_1\iff f(x)\in  L_2$$

Siamo al paragrafo 5.5

#### Esempio

Vedi qua -> [Esempio](https://uniroma2.sharepoint.com/:p:/r/sites/DI_IANNI-8066834-FONDAMENTI_DI_INFORMATICA_1/Materiale%20del%20corso/Lezione09-riduzioni-IntroComplessita%CC%80.pptx?d=wce90e2d940284c36a2f47eb03310b906&csf=1&web=1&e=zFYX3C) da pagina 6 a pagina 14

## Decidibilità, accettabilità e riduzioni

**Teorema 1**
Il concetto di riduzione si rivela molto utile come strumento per dimostrare  che un linguaggio è decidibile/accettabile: dato un linguaggio $L_3$

Se dimostro che $L_3 \preceq L_4$ , per un qualche altro linguaggio $L_4$ , se io so che $L_4$ è **decidibile** allora, posso concludere che anche $L_3$ è **decidibile** 

_Dim_
Infatti, sia $L_3\in\Sigma_3^\star\space e\space L_4\in\Sigma_4^\star$
- L4 è _decidibile_ : allora esiste una macchina $T_4$ tale che, per ogni $x\in\Sigma_4^\star, T_4 (x)$ termina in $q_A$ se $x\in L_4$, $T_4 (x)$ termina in $q_R$ se $x\not\in L_4$
- $L_3\preceq  L_4$ : allora esiste una un trasduttore $T_f$ tale che, per ogni $x\in\Sigma_3^\star, T_f (x)$ termina con una parola $y\in\Sigma_4^\star$ scritta sul nastro di output tale che $y\in L_4$ se $x\in L_3$, e $y\not\in L_4$ se $x\not\in L_3$

Ora, costruiamo una macchina $T_3$ , a 2 nastri, che, con input $x\Sigma_3^\star$ :
- prima simula $T_f (x)$ scrivendo l’output y sul secondo nastro
- poi simula $T_4 (y)$: se $T_4 (y)$ accetta allora anche $T_3$ accetta, se $T_4 (y)$ rigetta allora anche $T_3$ rigetta

Poiché $y\in L_4$ se $x\in L_3$, e $y\not\in L_4$ se $x\not\in L_3$ : 
- se $x\in L_3$ allora $y\in L_4$  e, quindi, $T_4 (y)$ accetta; quindi, $T_3$ accetta le parole in $L_3$, 
- se $x\not\in  L_3$  allora $y\not\in  L_4$  e, quindi, $T_4 (y)$ rigetta; quindi $T_3$ rigetta le parole che non sono in $L_3$. 

In conclusione, $T_3$ decide $L_3$. Ossia, $L_3$ è **_decidibile_** $\square$
Con una dimostrazione simile si dimostra anche l'accettabilità (vedi pdf Lezione 9)

**Teorema 2**
Il concetto di riduzione si rivela molto utile come strumento per dimostrare che un linguaggio è non decidibile/non accettabile: dato un linguaggio $L_2$ :
- Se dimostro che $L_1\preceq  L_2$ , per un qualche altro linguaggio $L_1$ , se io so che $L_1$ è _**non decidibile**_ allora, posso concludere che anche $L_2$ è _**non decidibile**_

_Dim_
Infatti, sia $L_1\subseteq\Sigma_1^\star\space e\space L_2\subseteq\Sigma_2^\star$ :
- _se L2 fosse decidibile (per assurdo)_: allora, poiché $L_1\preceq  L_2$ , per quello che abbiamo appena dimostrato (vedi teorema 1) anche $L_1$ sarebbe decidibile, contraddicendo l’ipotesi che $L_1$ è non decidibile

Con una dimostrazione simile si dimostra la non accettabilità

In conclusione, il concetto di riduzione può essere utilizzato in due “direzioni”:

1) riducendo un linguaggio “**sconosciuto**” ad un linguaggio accettabile/decidibile dimostriamo che il linguaggio “**sconosciuto**” è anch’esso accettabile/decidibile 
	1) ad esempio, dimostrando che $L_{P12}\preceq  L_{PPAL}$ e sapendo che $L_{PPAL}$ è decidibile, abbiamo dimostrato che $L_{P12}$ è decidibile
	2) ad esempio, dimostrando che $L_{H0}\preceq  L_H$ e sapendo che $L_H$ è accettabile, abbiamo dimostrato che $L_{H0}$ è accettabile
2) riducendo un linguaggio non accettabile/non decidibile ad un linguaggio “**sconosciuto**” dimostriamo che il linguaggio “**sconosciuto**” è anch’esso non accettabile/non decidibile 
	1) ad esempio, dimostrando che $L_H\preceq  L_{H0}$ e sapendo che $L_H$ è non decidibile, abbiamo dimostrato che $L_{0}$ è non decidibile

---
# Calcolabilità

Abbiamo studiato cosa si intende per problema risolvibile
- o meglio, per linguaggio decidibile
- o linguaggio accettabile
- o funzione calcolabile

E abbiamo visto che esistono problemi non risolvibili.
Ma anche problemi risolvibili

Siamo davvero sicuri di poter risolvere i problemi risolvibili?

## Le Torri di Hanoi

![[appunti fi/mod ii/immagini/Pasted image 20230404145204.png|center|500]]

Prendiamo come esempio questa istanza del problema 

Per spostare una torre di n dischi è necessario:
- spostare la sotto-torre costituita dagli n-1 dischi più piccoli dall’asta di sinistra a quella centrale (configurazione 4) nella figura), 
- poi spostare il disco più grande sull’asta di destra (configurazione 5) nella figura),
- e, infine, spostare la sotto-torre costituita dagli n-1 dischi più piccoli dall’asta centrale a quella di destra (configurazione 7) nella figura).

Quindi, se indichiamo con $M(n)$ il numero di spostamenti di dischi singoli necessario a spostare una torre di n dischi, vale la seguente relazione di ricorrenza: 								$$M(n) = 2 M(n-1) +1 $$
Che ha come soluzione $M(n) = 2^n-1$
E non possiamo far di meglio

**E allora?**

Lo sappiamo risolvere o no il problema della torre di Hanoi?

Certo, che lo sappiamo risolvere!

Tuttavia, se il tempo necessario a calcolare la soluzione di (un’istanza di) un problema è troppo elevato, _saper calcolare quella soluzione è equivalente a non saperla calcolare_

## La Teoria della Complessità Computazionale

Studia la “**quantità di risorse**” necessarie a risolvere un problema
- meglio: a decidere un linguaggio
E suddivide i problemi in “trattabili” e “intrattabili”
- dipendentemente dal fatto che la “quantità di risorse” necessarie cresca come un polinomio o più di un polinomio

Ma perché la crescita polinomiale è discriminante fra trattabilità e intrattabilità?
- Beh, lo avete visto quanto è grande 264: un numero di 20 (venti!) cifre. Invece, 642 è il minuscolo 4096. Piccolo.

Una funzione più che polinomiale cresce infinitamente più velocemente di una funzione polinomiale! 
- e, se quella funzione rappresenta la “quantità di risorse” necessaria a risolvere un problema…
- Stiamo nella merda

Sì, ma qui stiamo parlando di funzioni che rappresentano la “quantità di risorse” necessaria a risolvere un problema
Ma qual è l’argomento di queste funzioni?
- Cioè: in funzione di cosa esprimiamo la complessità di un problema?
E, poi, quali sono le “risorse” che prendiamo in considerazione?

