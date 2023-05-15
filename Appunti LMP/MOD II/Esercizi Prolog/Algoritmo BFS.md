Codide Algoritmo BFS
```prolog
% Algoritmo BFS

/*edge(x,y)*/
/*prossima_frontiera(F,NF) vero se F è frontiera e NF è nuova frontiera*/

/*prossima_fromtiera_da_nodo(N,LN):-
 * setof(NN,edge(N,NN),LN).*/

edge(a,b).
edge(a,c).
edge(c,d).
edge(c,k).
edge(b,k).
edge(k,d).
edge(k,n).

prossimaFrontieraDaNodo(N,Path,NF):-
  edge(N,_),
  setof([NN|Path],edge(N,NN),NF).

prossimaFrontieraDaNodo(N,[]):-
  \+edge(N,_). /*\+ è il not*/
/*si può fare anche cosi edge(N,_),!, e al predicato sotto ci togli\+edge(N,_)*/

/*Cosi
prossimaFrontieraDaNodo(N,NF):-
  edge(N,_),!,
  setof(NN,edge(N,NN),NF).

prossimaFrontieraDaNodo(N,[]).*/

prossimaFrontiera([],[]).
prossimaFrontiera([Node|RestoFrontiera],NuovaFrontiera):-
    prossimaFrontieraDaNodo(Node,Node_NF),/*Node_NF = rontiera raggiungibile dal nodo*/
    prossimaFrontiera(RestoFrontiera,NF_RestoFrontiera),/*NF_RestoFrontiera lista contenente la frontiera raggingibile dai restanti nodi F*/
    union(Node_NF,NF_RestoFrontiera,NuovaFrontiera). /*fa il merge tra la lista Node_NF e NF_RestoFrontiera*/


/*esiste un path(A,B)?*/

path(A,B):-
	futuraFrontiera([A],_,B).
/*FFI = Futura Frontiera Intermedia*/
futuraFrontiera(F,FF,G):-
    prossimaFrontiera(F,FF),
    %write(FF),nl,
    member(G,FF).

futuraFrontiera(F,FF,G):-
    %write('in>'),write(F),nl,
    prossimaFrontiera(F,FFI),
    \+ FFI = [],/*Evita la ricorsione infinit acon liste vuote*/
    %write(FFI),nl,
    futuraFrontiera(FFI,FF,G).

```






