# Introduzione alla probabilità e statistica

## Il fenomeno aleatorio

_Def :_
Un fenomeno è detto aleatorio se il suo esito è incerto.
L'insieme dei possibili esiti (in genere "numerico", eventualmente multidimensionale) viene indicato con $\Omega$ (Omega)

Si divide in due gruppi:
- Discreto : se $\Omega$ è finito o numerabile
- Continuo : se $\Omega$ è più che numerabile

Esempi discreti:
1) $\Omega$ finito (Possibili risultati del lancio di un dato) $\Omega$ = {1,2,3,4,5,6}
2) $\Omega$ numerabile (Numero di telefonate ricevute da un centralino) $\Omega$ = {0,1,2,...}

Esempio continuo:
1) Tempo di funzionamento di una lampadina rispetto ad una certa unità di misura $\Omega$ = (0,$\infty$)

In generale si introduce una "Famiglia di eventi" A che viene individuata da una famiglia di sottoinsiemi di $\Omega$

Tornando agli esempi : 
- "esce un numero pari" $\iff$ $\{ 2,4,6 \}  \subset \{1,2,...,6\}$
- "Il centralino si spegne dopo il tempo t=5" $\iff (5,\infty) \subset (0,\infty)$

Allora viene naturale considerare la corrispondenza tra "<u>Operazioni logiche tra eventi</u>" e "<u>Operazioni insiemistiche</u>":

- Somma logica : $A \lor B \implies$ Unione: $A\cup B$ 
- Prodotto logico : $A \land B \implies$ Intersezione: $A \cap B$
- Negazione: $\overline{A} \implies$ Complementare: $A^c = \Omega * A$  

## Sigma-algebra($\sigma$-algebra)

Si vuole fare riferimento a "Famiglia di eventi con buone proprietà". Si intende che, facendo operazioni insiemistiche su elementi di A, si ottiene ancora un elemento di A

_Def : 

Sia $\Omega$ un insieme non vuoto e sia A $\subset \mathcal{P}(\Omega)$
Allora A è una $\sigma-algebra$ (di eventi) se:
1) $\Omega \ni A$
2) $\forall a \ni A \implies a^c \ni A$
3) $\forall\{A_n\}_{n\geq1} \subset A \implies \bigcup_{n\geq1} A_n \ni A$

OSS: si vede facilmente che anche $\emptyset \ni A$ e che $\bigcap_{n\geq1} A_n \ni A$ nella 3)

## Misure di probabilità

_Def : 

Sia $\Omega$ un insieme non vuoto e A una $\sigma-algebra$ di eventi
Allora la funzione ${P: A\implies [0,\infty)}$ è una <u>misura di probabilità</u> se:
1) $P{(\Omega)} = 1$
2) $\forall \{A_n\}_{n\geq1} \subset A$ t.c. $A_m \cap A_n = \emptyset$ per m $\neq$ n si ha:

P($\bigcup_{n\geq1} A_n$) = $\sum_{n\geq1}P{(A_n)}$

**Terminologia**: la terna ($\Omega$,A,P) è detta <u>spazio di probabilità</u>


