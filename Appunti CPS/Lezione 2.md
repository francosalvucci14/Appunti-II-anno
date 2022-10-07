# Formule legate alla probabilità condizionata

- [[#Regola del prodotto o formula inversa]]
- [[#Formula delle probabilità totali]]
- [[#Formula di Bayes]]


## Regola del prodotto (o formula inversa)

A partire da $P(A|B)=P(A\cap B)/P(B)$ si ottiene $P(A\cap B)=P(A|B)\cdot P(B)$

>Questa formula è utile quando la probabilità condizionata segue dal test dell'esercizio e la probabilità dell'intersezione è la grandezza da calcolare

Questa formula può essere usata anche per l'intersezione di più di due eventi. Ad esempio, nel caso di 3 event. si ha $P(A\cap B\cap C)=P(A|B\cap C)\cdot P(B\cap C)$ e quindi: 

>$P(A\cap B\cap C) = P(A|B\cap C)\cdot P(B|C)\cdot P(C)$


**Esempi**

Un'urna contiene 2 palline bianche, 3 rosse e 4 nere
Si estraggono 3 palline a caso, una alla volta <u>senza</u> reinserimento

1) calcolare la probabilità di ottenere la sequenza(rosso, non rosso) nelle prime due estrazioni
2) calcolare la probabilità di ottenere la sequenza(rosso, bianco,rosso)

**Risposte**
In questi casi si deve scegliere bene quali sono gli eventi per applicare le formule;infattti, se si scelgono male, otteniamo uguaglienze non utili per ottenere i valori numerici che cerchiamo.
TIpicamente di fa riferimento al "condizionamento rispetto alle estraziopni precedenti"

1) $P(R_1\cap R_2^{c})=P(R_2^{c}|R_1)\cdot P(R_1)=6/8\cdot 3/9 = 1/4$ 
2) $P(R_1\cap B_2\cap R_3)=P(R_3|R_1\cap B_2)\cdot P(B_2|R_1)\cdot P(R_1) = 2/7\cdot 2/8\cdot 3/9=1/42$

**Osservarzioni**
1) Supponiamo di "scegliere male" gli eventi. Ad esempio possiamo scrivere $P(R_1\cap B_2\cap R_3) = P(R_3|B_2\cap R_1)\cdot P(R_1|B_2)\cdot P(B_2)$
Questa uguaglianza è vera ma non è direttamente utilizzabile perchè non sappiamo dove un valore numerico per $P(R_1|B_2)$ e per $P(B_2)$ in maniera diretta
2) Le probabilità di certe sequenza di risultati non cambiano se consideriamo un ordine diverso dei risultati stessi
	Ad esempiocalcoliamo le probabilità di ottenere le sequenze di colori (bianco, rosso, nero) e (nero,rosso,bianco)
	$P(B_1\cap R_2\cap N_3) = P(N_3|B_1\cap R_2) P(R_2|B_1)P(B_1)=4/7\cdot 3/8\cdot 2/9 = 1/21$
	$P(N_1\cap B_2\cap R_3) = P(R_3|N_1\cap B_2) P(B_2|N_1)P(N_1)=3/7\cdot 2/8\cdot 4/9 = 1/21$
	
## Formula delle probabilità totali

Supponiamo di avere una <u>partizione di eventi</u> finito o numerabile
$(E_i:i\ni I)$ $I=(1,...,n)$ oppure $I=(1,2,3,...)$

Questo significa che $\bigcup_{i\ni I}E_i=\Omega$ e che $E_i\cap E_j=\emptyset$ per $i\neq j$
Inoltre sia A un altro evento.

>Si usa questa formula per calcolare P(A) quando si conoscono $P(E_i)_{i\ni I}$ e $P(A|E_i)_{i\ni I}$ per i valori per cui $P(E_i)\neq0$

Allora:
$P(A) = P(A\cap \Omega) = P(A\cap (\bigcup_{i\ni I}E_i)) = P(\bigcup_{i\ni I}(A\cap E_i))=\sum_{i\ni I}P(A\cap E_i)$
Ora per ciascun addendo per cui $P(E_i)\neq0$ si ha $P(A\cap E_i)=P(A|E_i)\cdot P(E_i)$
**Oss** In ogni caso, se fosse $P(E_i)=0$, si avrebbe $P(A\cap E_i)=0$ e vale l'uguaglianza anche se $P(A|E_i)$ non è ben definita

>In conclusione $P(A)=\sum_{i\ni I}P(A|E_i)\cdot P(E_i)$

Un caso particolare è quello in cui la partizione è costituita da due eventi:
$$\begin{cases}
E_1=E\\
E_2=E^c
\end{cases}$$
Allora:
$P(A)=P(A|E)\cdot P(E)+P(A|E^c)\cdot P(E^c)$

## Diagramma ad albero associato alla formula delle prob. totali
Si può costruire un diagramma ad albero associato dove ogni diramazione fa riferimento ad una partizione(ogni diramazione considera tutti i casi possibili.) Ad ogni arco si associa uno probabilità. Per fissare le idee consideriamo $I=(1,2,3)$

## Formula di Bayes
