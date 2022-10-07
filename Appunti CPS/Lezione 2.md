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
1) SUpponiamo di "scegliere male" gli eventi. Ad esempio possiamo scrivere $P(R_1\cap B_2\cap R_3) = P(R_3|B_2\cap R_1)\cdot P(R_1|B_2)\cdot P(B_2)$
Questa uguaglianza è vera ma non è direttamente utilizzabile perchè non sappiamo dove un valore numerico per $P(R_1|B_2)$ e per $P(B_2)$ in maniera diretta
2) Le probabilità di certe sequenza di risultati non cambiano se consideriamo un ordine diverso dei risultati stessi
	Ad esempiocalcoliamo le probabilità di ottenere le sequenze di colori (bianco, rosso, nero) e (nero,rosso,bianco)
	$P(B_1\cap R_2\cap N_3) = P(N_3|B_1\cap R_2) P(R_2|B_1)P(B_1)=4/7\cdot 3/8\cdot 2/9 = 1/21$
	$P(N_1\cap B_2\cap R_3) = P(R_3|N_1\cap B_2) P(B_2|N_1)P(N_1)=3/7\cdot 2/8\cdot 4/9 = 1/21$





## Formula delle probabilità totali
## Formula di Bayes
