# Classi di complessità

## Alla ricerca della macchina più veloce

Ci siamo lasciati con la storia della correlazione polinomiale: 																									`Tutti i modelli (deterministici) sono correlati polinomialmente`

Tuttavia, 
- se ho una macchina di Turing $T$ che decide linguaggio $L\subseteq\Sigma^\star$ tale che, per ogni $x\in\Sigma^\star$, $dtime(T, x) \leq |x|^3$
- e un’altra macchina $T_4$ che decide lo stesso linguaggio L e tale che , per ogni $x\in\Sigma^\star$, $dtime(T_4, x)\leq\frac{|x|^3}{4}$
Beh, mi sa tanto che mi conviene scegliere T4, per decidere L!

Ma nella Teoria della Complessità Computazionale le cose non sono proprio così…

>[!definition]- Teorema 6.7 [Accellerazione lineare]
>Sia $L\subseteq\Sigma^\star$ un linguaggio deciso da una macchina di Turing deterministica ad un nastro T tale che, per ogni $x\in\Sigma^\star$, $dtime(T,x) = t(|x|)$ e sia k > 0 una costante. Allora:
>- esiste una macchina di Turing _ad un nastro_ $T_1$ tale che $T_1$ decide L e, per ogni $x\in\Sigma^\star$, $dtime(T_1, x)\leq\frac{t(|x|)}{k}+  O(|x|^2)$
>- esiste una macchina di Turing _a due nastri_ $T_2$ tale che $T_2$ decide L e, per ogni $x\in\Sigma^\star$, $dtime(T_2, x)\leq\frac{t(|x|)}{k}   +  O(|x|)$

Questo teorema ci dice che, dato un qualunque algoritmo, esiste sempre un algoritmo più veloce del primo di un fattore costante! 

Resta da capire: perché i due addendi $O(|x|^2)\space e\space O(|x|)?$
- essi derivano dal fatto che, per poter essere più veloci, le macchine $T_1$ e $T_2$ devono innanzi tutto codificare in forma compressa il proprio input (vedi prossimo teorema): se la codifica compressa viene scritta su un nastro apposito (come fa $T_2$ sul suo secondo nastro) sono sufficienti $O(|x|)$ passi, se si dispone di un solo nastro (il caso di $T_1$) occorrono $O(|x|^2)$ passi

>[!info]- Osservazione
>$\Sigma^{\star} = \{0,1\}^\star$

### Risparmiare memoria

Si può dimostrare qualcosa di analogo nel caso della funzione dspace

>[!definition]- Teorema 6.6 [Compressione lineare]
>Sia $L\subseteq\Sigma^\star$ un linguaggio deciso da una macchina di Turing deterministica ad un nastro T tale che, per ogni $x\in\Sigma^\star$, $dspace(T, x) = s(|x|)$ e sia k > 0 una costante. Allora:
>- esiste una macchina di Turing _ad un nastro_ $T_1$ tale che $T_1$ decide L e, per ogni $x\in\Sigma^\star$, $dspace(T_1, x)\leq\frac{s(|x|)}{k}   +  O(|x|)$

Questo teorema ci dice che, dato un qualunque algoritmo, esiste sempre un algoritmo che usa una frazione costante della memoria del primo! 
Resta da capire: perché l’addendo $O(|x|)$?
- deriva dal fatto che l’input di $T_1$ è lo stesso di T. Pertanto $T_1$ deve innanzi tutto codificare in forma compressa il proprio input e poi lavorare sull’alfabeto compresso: osservate che l’alfabeto compresso è $\Sigma^k$ (ossia, un carattere dell’alfabeto compresso è una parola di k caratteri di $\Sigma$) e che l’alfabeto di $T_1$ è $\Sigma^k\cup\Sigma$

## Classi di complessità deterministiche

Siamo pronti a raggruppare i linguaggi in base all’efficienza delle macchine che li decidono - e siamo a pag. 9 della dispensa 6
- per esempio, potremmo considerare l’insieme dei linguaggi tali che _**la migliore macchina che li decide**_ ha una certa efficienza

E che vuol dire?
- un linguaggio L è un insieme di parole
- e una macchina che decide L, tipicamente, esegue un numero diverso di operazioni quando opera su input diversi – anche su input diversi che hanno la stessa lunghezza
- Si prenda, ad esempio, la macchina $T_{PPAL}$, che accettava parole palindrome di lunghezza pari sull’alfabeto $\{a,b\}$. Ebbene: $T_{PPAL}(abababab)$ rigetta dopo aver eseguito 10 quintuple, $T_{PPAL}(abbbbbba)$ accetta dopo aver eseguito all’incirca 45 quintuple (deve fare avanti e indietro un sacco di volte!)
 - e considerazioni analoghe possono essere fatte per la misura dspace)

Cosa significa dire che una macchina che decide un linguaggio ha una certa efficienza?
- che si comporta “bene” (con quella efficienza) almeno su qualche input?
- o che si comporta “bene” su ogni input?

La risposta corretta è la seconda: vogliamo che la macchina che decide un linguaggio $L\subseteq\Sigma^\star$ si comporti ”bene” su **ogni** parola $x\in\Sigma^\star$
Poi, non possiamo scegliere la “_migliore_” macchina che decide un linguaggio
- perché se un linguaggio è deciso da una macchina che ha una certa efficienza, quel linguaggio è deciso anche da una macchina che è efficiente il doppio. O il triplo. O il quadruplo…
E per risolvere questa questione ricorriamo alla notazione $O\space(\text{O grande})$: 
- diciamo che un linguaggio L appartiene all’insieme caratterizzato dalla “efficienza temporale” individuata dalla funzione totale e calcolabile f se esiste una macchina T che decide L e che, per ogni parola x sull’alfabeto di L, termina in $O( f(|x ) )$ istruzioni
E analogamente a proposito di “efficienza spaziale” 

>[!info]- Osservazione
>è sparita la richiesta di “migliore” macchina che decide L

Le classi che misurano “_**efficienza temporale**_” nel caso deterministico si chiamano $DTIME$: data una funzione totale e calcolabile f, 
$$\begin{align}DTIME[f(n)] = &\{ L \subseteq\{0,1\}^\star| \exists T (\text{deterministica})\text{che decide L e},\\& \forall x\in \{0,1\}^\star, dtime(T,x) \in O( f(|x|) ) \}\end{align}$$

Nella Teoria della Complessità Computazionale si parla di classi invece che di insiemi
**ATTENZIONE**: $dtime$ (minuscolo) è la misura di complessità, ossia, una funzione;                   $DTIME$ (maiuscolo) è una classe di complessità, ossia, un insieme!
Si osservi che $DTIME[ f(n) ] = DTIME[ f(n)/2 ] = DTIME[2 f(n)+58 ] =\dots$
come è giusto che sia a seguito del **Teorema di accelerazione lineare.** [^1]
