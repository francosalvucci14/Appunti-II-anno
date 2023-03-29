
# Esercizio 1

Vogliamo eliminare i duplicati da una lista. Prendiamo ad esempio la seguente lista:

`[3,6,2,3,5,1,2,3,6]`

La lista risultante dovrebbe essere la seguente:

`[1,2,3,5,6]`

Codice 
```prolog
list2set([],[]).
list2set([H|T],X):-
    appartiene(H,T),
    list2set(T,X),!.
list2set([H|T],[H|X]):-
    list2set(T,X).

/*Stessa cosa di sopra ma con il sort*/
% Una lista vuota è un set vuoto
list2set_sort([],[]).
% Caso in cui H è già presente nel set
list2set_sort([H|T], SortedSet):-
    list2set_sort(T,S),
    member(H,S),
    sort(S,SortedSet),!.
% Caso in cui H non è presente nel set
list2set_sort([H|T], SortedSet):-
    list2set_sort(T,T_S),
    sort([H|T_S], SortedSet).
```

# Esercizio 2

Date due liste:

`[1,2,3,5,6]`
`[2,5,7]`

Vorremmo avere una lista che è l'intersezione delle due, in questo caso: `[2,5]`

Codice

```prolog
% Casi base, l'intersezione con l'insieme vuoto, è l'insieme vuoto
set_intersect(_,[],[]).
set_intersect([],_,[]).
% Caso in cui entrambi i set condividono H
set_intersect([H|T1], [H|T2], [H|T]):-
    set_intersect(T1,T2,T).
% Caso in cui H del primo set è minore di H del secondo set, scorri il primo
set_intersect([H1|T1], [H2|T2], IntersectedSet):-
    H1 < H2,
    set_intersect(T1, [H2|T2], IntersectedSet),!.
% Caso in cui H del secondo set è minore di H del primo set, scorri il secondo
set_intersect([H1|T1], [H2|T2], IntersectedSet):-
    H2 < H1,
    set_intersect([H1|T1], T2, IntersectedSet).

% Define intersect(L1, L2, IntersectedList) predicate here.

% Definisci due set dalle liste di partenza e fai l'intersect insiemistico
intersect(L1, L2, ListIntersected):-
    list2set(L1,S1),
    list2set(L2,S2),
    set_intersect(S1,S2, ListIntersected),!.
```

# Esercizio 3

Prendiamo ad esempio le due liste di prima:

1.  `[1,2,3,5,6]`
2.  `[2,5,7]`

L'unione delle due liste dovrebbe essere la seguente:  
`[1,2,3,5,6,7]`.

Codice
```prolog
% Define set_union(S1, S2, UnitedSet) predicate here

% Casi base: l'unione tra un insieme vuoto ed un altro insieme, è "l'altro insieme"
set_union([], S, S).
set_union(S, [], S).
% Caso in cui i due set condividono H
set_union([H|T1], [H|T2], [H|T]):-
    set_union(T1,T2,T).
% Caso in cui H1 del primo set è minore di H2 del secondo set, aggiungi H1 alla soluzione
set_union([H1|T1], [H2|T2], [H1|T]):-
    H1 < H2,
    set_union(T1, [H2|T2], T).
% Caso in cui H2 del secondo set è minore di H1 del primo set, aggiungi H2 alla soluzione
set_union([H1|T1], [H2|T2], [H2|T]):-
    H2 < H1,
    set_union([H1|T1], T2, T).
% Definisci due set dalle liste di partenza e fai l'unione insiemistica
union(L1, L2, UnitedList):-
    list2set(L1, S1),
    list2set(L2, S2),
    set_union(S1, S2, UnitedList), !.
```

