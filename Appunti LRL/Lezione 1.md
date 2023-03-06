
3 lezioni e 1 esercitazione (in modo ciclico) con i 2 tutor

Libri:
- Raymond M. Smullyan. A Beginner’s Guide to Mathematical Logic. Dover Publications, 2014. 
- Sarah L. Harris and David Money Harris. Sistemi digitali e architettura dei calcolatori. Zanichelli, 2017

# Programma generale

2 parti del corso:
1. Logica
	1. Riepilogo di matematica
	2. Logica proposizionale
	3. Logica del primo ordine
2. Reti logiche
	1. Reti combinatorie
	2. Reti sequenziali
	3. Codifiche

# Cos'è la logica?

> La logica è _ragionamento_ 

In modo meno formale, la logica è una strada che porta a una risposta

**Esempio**

Tutti gli uomini sono mortali $\to$ Io sono un uomo $\to$ Io sono mortale

**Esempio**

Tutte le mosche volano $\to$ Io sono una mosca $\to$ Io volo

Questi due sillogismi sono entrambi validi, perchè se sono vere le premesse, allora è vera anche la risposta

Per la struttura del ragionamento in se, i due sillogismi sono entrambi **_validi_**

**Esempio**

- Il cibo buono non è economico
- Il cibo economico non è buono

Le due frasi sono uguali?

Da un punto di vista prettamente logico si, vediamo perchè:

A = "il cibo è buono"
B = "il cibo è economico"

Possiamo vedere che $A\implies\overline B$ e $B\implies\overline A$

Le due relazioni sono equivalenti

## Come possiamo definire il concetto di "dimostrazione"?

Prendiamo alcuni esempi provenienti dalla teoria degli insiemi

Un'insieme è una collezione di oggetti

Le operazioni che si possono fare sugli insiemi sono:

- $A\cup B$ Unione
- $A\cap B$ Intersezione
- $A\setminus B$ Differenza
- $A\times B$ Prodotto cartesiano
- $\overline A$ Complementare di A
- $A\uplus B$ Unione disgiunta
- $(A\setminus B)\cup(B\setminus A)$ Differenza Simmetrica, si indica anche con il simbolo $\triangle$ $A\triangle B$

**Esempio**

$A\cup B=A\cap B$?

In genere no, ma se A e B sono uguali, la risposta diventa **SI**

Ma la relazione non è **valida** (valida = vera sempre)

**Esercizio**

$A\cap(B\triangle C)=(A\cap B)\triangle(A\cap C)$ 

Verificare che la relazione è valida

**Fine esercizio**

Data una sequenza 
$A_1,A_2,...,A_n$

La porzione $A_i$ sarà
$$A_i=\{\underline x=(x_1,...,x_n)\in\{0,1\}^\star:x_i=1\}$$
