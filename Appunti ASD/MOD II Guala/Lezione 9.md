
```table-of-contents
title: 
style: nestedList # TOC style (nestedList|inlineFirstLevel)
minLevel: 0 # Include headings from the specified level
maxLevel: 0 # Include headings up to the specified level
includeLinks: true # Make headings clickable
debugInConsole: false # Print debug info in Obsidian console
```

# Algoritmo di Bellman-Ford-Moore

## Shortest path con pesi negativi

Ricordiamo la definizione del problema SP

>[!definition]- Problema SP
>Dato un grafo diretto $G=(V,E)$ con lunghezze degli archi arbitrarie $l_{vw}$, trovare lo SP da un nodo sorgente $s$ a un nodo destinazione $t$

**Esempio**

![[Pasted image 20240415112433.png|center|500]]

### Tentativi falliti

Vediamo come l'algoritmo di Dijkstra non funziona per istanze di grafi con pesi negativi

**Dijkstra** : Potrebbe non produrre lo SP quando le lunghezze degli archi sono negative

**Esempio**

![[Pasted image 20240415112712.png|center|200]]

Come si può vedere da questo esempio, l'algoritmo di Dijkstra va a prendere i nodi nell'ordine $s,t,w,v$, ma lo SP corretto sarebbe il percorso $s\to v\to w\to t$

### Cicli negativi

>[!definition]- Cicli negativi
>Un **ciclo negativo** è un ciclo diretto dove la somma dei pesi degli archi che lo compongono è negativo
>Quindi, un ciclo negativo $W$ è : $$l(W)=\sum\limits_{e\in W}l_e\lt0$$

![[Pasted image 20240415113125.png|center|300]]

### SP e Cicli negativi

**Lemma 1** : Se un certo percorso $v\to t$ contiene un ciclo negativo, allora non esiste uno shortes path da $v$ a $t$

**Dimostrazione** : Se esistesse un tale ciclo, chiamato $W$, allora si potrebbe costruire un percorso $v\to t$ di lunghezza arbitrariamente negativa girando intorno a $W$ quante volte lo si desidera.

![[Pasted image 20240415113524.png|center|300]]

**Lemma 2** : Se $G$ non ha cicli negativi, allroa esiste uno shortest path $v\to t$ che è semplice (ovvero che usa $\leq n-1$ archi)

**Dimostrazione**
- Di tutti gli SP $v\to t$, considera quello che usa meno archi
- Se tale percorso $P$ contiene un ciclo diretto $W$, possiamo rimuovere la porzione di $P$ che corrisponde a $W$ senza incrementarne la lunghezza

![[Pasted image 20240415113728.png|center|300]]

### Problemi SP e Cicli negativi

Diamo ora la definizione dei due problemi fondamentali di questo argomento, ovvero :
- **Single-destination shortest-path**
- **Negative-cycle**

>[!definition]- Single-destination shortest-path
>Dato un grafo diretto $G=(V,E)$ con pesi sugli arhci $l_{vw}$ (ma no cicli negativi) e un determinato nodo $t$, trovare lo SP $v\to t$ per ogni nodo $v$
>Equivalente al problema `single-source shortest-path (in quel caso gli archi vengono invertiti, e si cerca lo SP da v a t)`

>[!definition]- Negative-cycle
>Dato un grafo diretto $G=(V,E)$ con pesi sugli archi $l_{vw}$, trovare un ciclo negativo (se esiste)

![[Pasted image 20240415114239.png|center]]

### SP con pesi negativi : Programmazione dinamica

>[!definition]- Sottoproblemi
>$OPT(i,v)$ =  lunghezza dello SP $v\to t$ che usa $\leq i$ archi

**Goal** : $OPT(n-1,v)$ per ogni $v$

Ci sono due casistiche

**Caso 1** : Lo SP $v\to t$ usa $\leq i-1$ archi
- In questo caso $OPT(i,v)=OPT(i-1,v)$

**Caso 2** : Lo SP $v\to t$ usa esattamente $i$ archi
- Se l'arco $(v,w)$ è il primo arco nello SP $v\to t$, paghiamo il peso dell'arco, quindi $l_{vw}$
- Poi, selezioniamo il miglior percorso $w\to t$ che usa $\leq i-1$ archi

**L'equazione di Bellman sarà** :
$$OPT(i,v)=\begin{cases}0&i=0\land v=t\\\infty&i=0\land v\neq t\\\min\{OPT(i-1,v),\min_{(v,w)\in E}\{OPT(i-1,w)+l_{vw}\}\}&i\gt0\end{cases}$$

#### Implementazione

L'algoritmo sarà il seguente

![[Pasted image 20240415115016.png|center|500]]

>[!definition]- Teorema 1
>Dato un grafo diretto $G=(V,E)$ che non contiene cicli negativi, l'algoritmo di DP calcola la lunghezza dello SP $v\to t$,per ogni nodo $v$, in tempo $\Theta(mn)$ e spazio $\Theta(n^2)$

