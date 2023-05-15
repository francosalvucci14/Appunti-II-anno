
Codice Esercizio parser top down

```prolog
/*parser top down per grammatiche*/

/*Esempio
 * A --> B C
 * C --> D E
 * B --> a
 * C --> d
 * D --> d
 * E --> e*/

/*A -*-> ad*/
/*Esempi di derivazione : 
A-*-> BC -*-> aC -*->aDE-*-> NO
A-*-> BC -*-> aC -*->ad SI*/

/*La stringa da cercare la scriviamo come una lista di lettere,in questo caso [a,d]*/
/*Ogni regola ha il suo predicato*/

'A' --> 'B', 'C'.
/*'A'(SDR,R_SDR):- % SDR = Stringa da RIconoscere, R_SDR = Restante SDR
    'B'(SDR,R_SDR_B), % R_SDR_B = R_SDR da B
    'C'(R_SDR_B,R_SDR).*/

'A' --> 'B', 'C', 'D'. % Serve per scrive in maniera più compatta
/*Genera 'A'(A, B) :-
    'B'(A, C),
    'C'(C, D),
    'D'(D, B).*/

'C' --> 'D', 'E'.
/*'C'(SDR,R_SDR):-
    'D'(SDR,R_SDR_D),
    'E'(R_SDR_D,R_SDR).*/
'C' --> [d]. %Genera'C'([d|R],R).
'B' --> [a]. %Genera 'B'([a|R],R).
'D' --> [d]. %Genera'D'([d|R],R).
'E' --> [e]. %Genera'E'([e|R],R).
'E' --> [j]. %Genera 'E'([j|A], A).

mossa(-1) --> [down].
mossa(+1) --> [up].
seq(V) --> mossa(V).
seq(V) --> mossa(VM),seq(VS), {V is VM+VS}. /*tutto cio che sta in {} non entrerà nella regola*/

```