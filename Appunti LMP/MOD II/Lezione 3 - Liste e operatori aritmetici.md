
Algoritmo di risoluzione dell'esercizio a [[Lezione 2 - Il primo passo]]

![[appunti lmp/mod ii/immagini/Pasted image 20230313110900.png|center|600]]

# Esecuzione programma

Analizza i fatti/regole dall'alto verso il basso (quindi è importante l'ordine con cui vengono scritti)

Utilizzo del **Backtracking** per tornare indietro a prima che una variabile fosse unificata o che una certa regola fosse esplorata

Utilizzo della **ricorsione** per chiamare le altre regole

Per avere altre risposte, e quindi forzare il backtracking anche se il programma ne ha già trovata una che funziona, basta premere ";"

# Lettura dei programmi Prolog

Il mondo dei **se** può essere letto in maniera:

- Dichiarativa : i problemi sono risolubili attraverso la scrittura di un insieme di regole
- Procedurale : i problemi sono risolubili attraverso la scrittura di sequenze di istruzioni

## Lettura dichiarativa

è la lettura classica (e più corretta) :

**Esempio**

Una clausola con variabili come :
```prolog
grandparent(X,Y):-
	parent(X,Z),
	parent(Z,Y).
```
viene letta come :
Per ogni X e Y e Z, 
```prolog
granparent(X,Y) è vero se
parent(X,Z) è vero e
parent(Z,Y) è vero
```

**Altro esempio**

Una query come :
```prolog
?- grandparent(X,mario).
```
viene letta come :
`Esiste un X tale che grandparent(X,mario) è vero?`

## Lettura procedurale

è una lettura necessaria

**Esempio**

Una clausola con variabili come :
```prolog
grandparent(X,Y):-
	parent(X,Z),
	parent(Z,Y).
```
può essere anche letta come :

Per qualsiasi valore delle variabili X e Y e Z,
per soddisfare il goal **grandparent(X,Y)** soddisfa prima il goal parent(X,Z) e poi il parent(Z,Y).

>[!warning]- Attenzione
>Le variabili NON variano valore durante il soddisfamento del goal

Una query come :
```prolog
?- grandparent(X,mario).
```
viene letta come :
Soddisfare il goal grandparent(X,mario) trovando il valore della variabile X?

## Osservazioni

Importanza dell'ordine delle clausole e nelle clausole

```prolog
path(X,Y):- path(X,Z),path(Z,Y).
path(X,Y):- edge(X,Y).
```

genera un loop infinito!!!

# Liste

In Prolog le liste sono molto utilizzate

>[!definition]- Definizione(Liste)
>Sequenza di vari elementi (anche ripetuti), che possono essere a loro volta delle liste

**Esempio**

```prolog
[primo,secondo,[primo2,secondo2]].
```

Lista composta da 3 elementi
Il terzo elemento è a sua volta una lista

La lista può essere vuota (caso molto importante e utilizzato)

Ogni lista è composta da due parti:
- **Head**: è il primo elemento
- **Tail**: è il resto della lista (a sua volta una lista)

Le liste possono essere rappresentatu in due modi:
- `[a,b,c,d]`
- `.(a,.(b,.(c,.(d,[]))))`

Per estrarre la Testa di una lista si usa la notazione:
- `[H|T]`, dove H è la testa e T è la coda (lista rimanente senza primo elemento)

Si possono estrarre più elementi contemporaneamente:

- `[H1,H2|T]`
- H1 e H2 sono il primo e secondo elemento 
- T è la lista rimanente senza i primi due elementi

## Operatori su liste

$member(?ELem,?List)$
- restituisce true se Elem si trova nella lista, può essere usato in vari modi:
	- $member(b,[a,b,c,d]).$->true
	- $member(e,[a,b,c,d]).$->false
	- $member(X,[a,b,c,d]).$->X=a,X=b,....
	- $member(c,[a,b,X,d]).$->X=c

Possibile implementazione : 
```prolog
member(X,[X,_]).
member(X,[_,T]):-
	member(X,T).
```

$append(?List1,?List2,?List1AndList2)$ 
- **List1AndList2** è la concatenazione di **List1** e **List2**. Vari utilizzi:
	- $append([a,b],[c,d],X).$->$X=[a,b,c,d]$
	- $append([a,b],X,[a,b,c,d]).$->$X=[c,d]$
	- ...

**Esercizio**

Scrivere una possibile implementazione della append.
Scrivere la regola per invertire tutti gli elementi di una lista, in modo da avere:
```prolog
?- reversed([a,b,c,d,e,f],X).
X=[f,e,d,c,b,a]
```


