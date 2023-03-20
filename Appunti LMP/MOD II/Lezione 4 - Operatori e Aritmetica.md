
# Operatori

In Prolog è possibile definire nuovi operatori, ma ne esistono già alcuni definiti (esempio gli operatori aritmetici)

$1*2+3*4$ ha i due operatori $*,+$

La scrittura in Prolog sarebbe
- $+(*(1,2),*(3,4))$

![[appunti lmp/mod ii/immagini/Pasted image 20230320111706.png|center|300]]

## Definire un operatore

Ogni operatore ha una sua priorità

$a + b*c$ come deve essere letto?

- $+(a, *(b,c)$ ?
- $*( +(a,b), c)$ ?

In matematica $*$ lega di più di $+$, e quindi $+$ ha priorità più alta di $*$

![[appunti lmp/mod ii/immagini/Pasted image 20230320111828.png|center|400]]


```prolog
:- op(Priorità, Tipo, Operatore).
```

Priorità è un numero tra 0 e 1200

Tipo:
- infisso : xfx, xfy, yfx
- prefisso: fx, fy
- postfisso: xf, fy

Operatore: il nome/simbolo dell’operatore

Il tipo serve ad indicare anche la precedenza degli operatori:
- x : la sua priorità deve essere minore di quella dell’operatore
- y: la sua priorità deve essere minore o uguale a quella dell’operatore

```prolog
:- op(700, yfx, somma).
```

Qual è l’albero risultante di
- 9 somma 5 somma 7  ?

# Aritmetica

Prolog può essere usato anche per fare dei calcoli, con alcune limitazioni

Come detto gli operatori aritmetici sono già definiti

$A = B + C$ assegna ad A _**non**_ il risultato della somma ma assegna proprio B + C

per eseguire l’operazione bisogna usare **is**

$A$ is $5 + 6$ fa sì che in A venga messo il valore 11

$B$ is $8 + 2 * 3$ mette in B 14 (rispetta la priorità)

A destra di **is** non possono esserci variabile non ancora istanziate

**Esempi**

```prolog
A = 3 , B is A + 4.
–A = 3 e B = 7

A = 3, B = A + C.
–A = 3 e B = 3+C

A = 3, B is A+C, C=4.

–ERROR: is/2: Arguments are not sufficiently instantiated
```

## Operatori per i calcoli

Gli operatori direttamente utilizzabili sono:

- +
- -
- $*$
- /
- $**$ (elevamento a potenza)
- $//$ (divisione intera)
- mod  (modulo, resto della divisione)
- `<, >, >=, =<, =, \=`  (sono confronti booleani utili come predicati, ma non utilizzabili a sinistra di is)
- number(X)  (vero se X è un numero, falso negli altri casi)

**Esempio**

```prolog
calcola(X + Y, Z):-
    Z is X+Y.

calcola(5+8,Y).
	Y = 13
calcola(5+8+2,X).
	X = 15
```

