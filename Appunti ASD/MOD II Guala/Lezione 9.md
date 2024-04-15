
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

**Lemma 2** : Se $G$ non ha cicli negativi, allroa esiste uno shortest path $v\to t$ che è semplice (ovvero che usa $\leq n-1$ archi) ^ddb5fe

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

**Dimostrazione**
- La tabella $M$ richiede spazio $\Theta(n^2)$
- Ogni iterazione $i$ impiega tempo $\Theta(m)$ dato che dobbiamo esaminare ogni arco una volta

**Trovare lo SP**:
- Approccio 1 : Mantenere una variabile $successor[i,v]$, che punta al prossimo nodo nello SP $v\to t$ che usa $\leq i$ archi
- Approccio 2 : Calcoliamo la lunghezza ottimale $M[i,v]$ e consideriamo solo gli archi con $M[i,v]=M[i-1,v]+l_{vw}$. Ogni percorso diretto in questo sottografo è uno SP

#### Miglioramenti pratici

Possiamo ottimizzare lo spazio

**Ottimizzazione dello spazio** : Manteniamo due array `unidimensionali` (al posto di un solo array bidimensionale)
- $d[v]$ = lunghezza dello SP $v\to t$ che abbiamo trovato prima
- $successor[v]$ = prossimo nodo del percorso $v\to t$

**Ottimizzazione delle permormance** : Se $d[v]$ non è stato aggiornato nell'iterazione $i-1$, allora non ce motivo di considerare gli archi entranti in $w$ nell'iterazione $i$

Diamo ora l'algoritmo ottimizzato, che saraà quello di Bellman-Ford-Moore
## Algoritmo di Bellman-Ford-Moore : Implementazione efficiente

![[Pasted image 20240415131338.png|center|500]]

### Analisi dell'algoritmo

**Lemma 3** : Per ogni nodo $v:d[v]$ è lunghezza di un qualche percorso $v\to t$
**Lemma 4** : Per ogni nodo $v:d[v]$ è monotona non crescente

**Lemma 5** : Dopo l'i-esima passata, $d[v]\leq$ lunghezza dello SP $v\to t$ che usa $\leq i$ archi ^8f65ab

**Dimostrazione lemma 5** (induzione su i)
- Caso base $i=0$
- Assumi vero dopo l'i-esima passata
- Sia $P$ un qualunque percorso $v\to t$ con $\leq i+1$ archi
- Sia $(v,w)$ il primo arco in $P$ e sia $P'$ un sottopercorso $w\to t$
- Per ipotesi induttiva, alla fine dell'i-esima passata, $d[w]\leq l(P')$ (e per il Lemma4 $d[w]$ non aumenta) perchè $P'$ è il percorso $w\to t$ con $\leq i$ archi
- Dopo aver considerato l'arco $(v,w)$ nella passata $i+1$ : $$\begin{align}\overbrace{d[v]}^{\text{Per il lemma 4, d[v] non aumenta}}&\leq l_{vw}+d[w]\\&\leq l_{vw}+l(P')\\&=l(P)\end{align}$$

>[!definition]- Teorema 2
>Assumi che non ci siano cicli negativi, l'algoritmo BFM calcola la lunghezza dello SP $v\to t$ in tempo $O(mn)$ e spazio $\Theta(n)$

**Dimostrazione** : Usando il [[Appunti ASD/MOD II Guala/Lezione 9#^ddb5fe|lemma 2]] + il [[Appunti ASD/MOD II Guala/Lezione 9#^8f65ab|lemma 5]]

>[!info]- Remark
>BFM è tipicamente veloce nella pratica
>- Arco $(v,w)$ viene considerato nel passaggio $i+1\iff d[w]$ viene aggiornata nel passaggio $i$
>- Se lo SP ha $k$ archi, allora l'algoritmo lo trova dopo $\leq k$ passate

Cosa possiamo dire sugli SPS

**Claim** : In tutto BFM, seguire i puntatori $successor[v]$ genera un percorso diretto da $v$ a $t$ di lunghezza $d[v]$

**Controesempio** : Il claim è falso
- La lunghezza del successore nel percorso $v\to t$ potrebbe essere strettamente più corto di $d[v]$

![[Pasted image 20240415133858.png|center|500]]
![[Pasted image 20240415133915.png|center|500]]

- Se il ciclo è negativo, il grafo dei successori potrebbe avere cicli diretti

![[Pasted image 20240415134055.png|center|500]]
![[Pasted image 20240415134121.png|center|500]]

### Trovare lo SP

**Lemma 6** : Ogni ciclo diretto $W$ nel grafo dei successori è un ciclo negativo ^a0a77b

**Dimostrazione** :
- Se la variabile $successor[v]=w$, dobbiamo avere che $d[v]\geq d[w]+l_{vw}$ (la parte sinistra e destra dell'equazione sono uguali quando $successor[v]$ viene impostato; $d[w]$ può solo decrementare; $d[v]$ decrementa solo quando $successor[v]$ viene resettatto)
- Sia $v_1\to v_2\to\dots v_k\to v_1$ una sequenza di nodi in un ciclo diretto $W$
- Assumi che $(v_k,v_1)$ sia l'ultimo arco in $W$ aggiunto al grafo dei successori
- Poco prima : $$\begin{align}&d[v_1]\geq d[v_2]+l(v_1,v_2)\\&d[v_2]\geq d[v_3]+l(v_2,v_3)\\&\vdots\\&d[v_{k-1}]\geq d[v_k]+l(v_{k-1},v_k)\\&d[v_k]\gt d[v_1]+l(v_k,v_1)\end{align}$$
- L'aggiunta di disuguaglianze produce $\underbrace{l(v_1,v_2)+l(v_2,v_3)+\dots+l(v_{k-1},v_k)+l(v_k,v_1)\lt0}_{\text{W è un ciclo negativo}}$

>[!definition]- Teorema 3
>Assumiamo che non ci siano cicli negativi, allora BFM trova lo Sp $v\to t,\forall v$ in tempo $O(mn)$ e spazio $\Theta(n)$

**Dimostrazione** :
- Il grafo dei successori non può avere cicli diretti, per il [[Appunti ASD/MOD II Guala/Lezione 9#^a0a77b|lemma 6]]
- Quindi, seguendo i puntatori successivi da $v$, si ottiene un percorso diretto fino a $t$
- Siano $v=v_1\to v_2\to\dots v_k=t$ i nodi in questo percorso $P$
- Alla fine, se $successor[v]=w$, dobbiamo avere che $d[v]=d[w]+l_{vw}$ (la parte sinistra e destra dell'equazione risulta essere uguale quando $successor[v]$ viene impostato; $d[.]$ non cambia `(dato che l'algoritmo è terminato)`)
- Quindi : $$\begin{align}&d[v_1]= d[v_2]+l(v_1,v_2)\\&d[v_2]= d[v_3]+l(v_2,v_3)\\&\vdots\\&d[v_{k-1}]= d[v_k]+l(v_{k-1},v_k)\end{align}$$
- L'aggiunta di queste equazioni produce $\underbrace{d[v]}_{\text{lunghezza minima del percorso da v a t, per il teorema 2}}=\underbrace{d[t]}_{0}+\underbrace{l(v_1,v_2)+l(v_2,v_3)+\dots+l(v_{k-1}),v_k}_{\text{lunghezza del percorso P}}$

L'algoritmo di BFM modificato, per vedere se esiste un ciclo negativo sarà il seguente

![[Pasted image 20240415140108.png|center|500]]

**Lemma 6.1** : Se esiste un ciclo negativo (che può essere raggiunto), allora l'algoritmo (modificato) lo notifica

**Dimostrazione**
- Se non esistono cicli negativi, la passata n-esima non fa nulla
- Sia $v_1\to v_2\to\dots v_k\to v_1$ un ciclo negativo diretto chiamato $W$
- Assumiamo per contraddizione che l'algoritmo non lo notifica
- Allora : La condizione dell'ultimo `IF` sarà sempre false
- Allora : $$\begin{align}&d[v_1]\leq d[v_2]+l(v_1,v_2)\\&d[v_2]\leq d[v_3]+l(v_2,v_3)\\&\vdots\\&d[v_{k-1}]\leq d[v_k]+l(v_{k-1},v_k)\\&d[v_k]\leq d[v_1]+l(v_k,v_1)\end{align}$$
- L'aggiunta di queste equazioni produce $\underbrace{l(v_1,v_2)+l(v_2,v_3)+\dots+l(v_{k-1},v_k)+l(v_k,v_1)\geq0}_{\text{W non può essere un ciclo negativo : contraddizione}}$