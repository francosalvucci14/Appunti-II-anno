# Classi di complessità

## Alla ricerca della macchina più veloce

Ci siamo lasciati con la storia della correlazione polinomiale: 																									`Tutti i modelli (deterministici) sono correlati polinomialmente`

Tuttavia, 
- se ho una macchina di Turing $T$ che decide linguaggio $L\subseteq\Sigma^\star$ tale che, per ogni $x\in\Sigma^\star$, $dtime(T, x) \leq |x|^3$
- e un’altra macchina $T_4$ che decide lo stesso linguaggio L e tale che , per ogni $x\in\Sigma^\star$, $dtime(T_4, x)\leq\frac{|x|^3}{4}$
Beh, mi sa tanto che mi conviene scegliere T4, per decidere L!

Ma nella Teoria della Complessità Computazionale le cose non sono proprio così…

[^1]: Teorema 6.7

>[!definition]- Teorema 6.7 [Accellerazione lineare]
>Sia $L\subseteq\Sigma^\star$ un linguaggio deciso da una macchina di Turing deterministica ad un nastro T tale che, per ogni $x\in\Sigma^\star$, $dtime(T,x) = t(|x|)$ e sia k > 0 una costante. Allora:
>- esiste una macchina di Turing _ad un nastro_ $T_1$ tale che $T_1$ decide L e, per ogni $x\in\Sigma^\star$ $dtime(T_1, x)\leq\frac{t(|x|)}{k}+  O(|x|^2)$
>- esiste una macchina di Turing _a due nastri_ $T_2$ tale che $T_2$ decide L e, per ogni $x\in\Sigma^\star$ $dtime(T_2, x)\leq\frac{t(|x|)}{k}   +  O(|x|)$

^8409f2

Questo teorema ci dice che, dato un qualunque algoritmo, esiste sempre un algoritmo più veloce del primo di un fattore costante! 

Resta da capire: perché i due addendi $O(|x|^2)\space e\space O(|x|)?$
- essi derivano dal fatto che, per poter essere più veloci, le macchine $T_1$ e $T_2$ devono innanzi tutto codificare in forma compressa il proprio input (vedi prossimo teorema): se la codifica compressa viene scritta su un nastro apposito (come fa $T_2$ sul suo secondo nastro) sono sufficienti $O(|x|)$ passi, se si dispone di un solo nastro (il caso di $T_1$) occorrono $O(|x|^2)$ passi

>[!info]- Osservazione
>$\Sigma^{\star} = \{0,1\}^\star$

### Risparmiare memoria

Si può dimostrare qualcosa di analogo nel caso della funzione dspace

>[!definition]- Teorema 6.6 [Compressione lineare]
>Sia $L\subseteq\Sigma^\star$ un linguaggio deciso da una macchina di Turing deterministica ad un nastro T tale che, per ogni $x\in\Sigma^\star$, $dspace(T, x) = s(|x|)$ e sia k > 0 una costante. Allora:
>- esiste una macchina di Turing _ad un nastro_ $T_1$ tale che $T_1$ decide L e, per ogni $x\in\Sigma^\star$ $dspace(T_1, x)\leq\frac{s(|x|)}{k}   +  O(|x|)$

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

Le classi che misurano “_**efficienza temporale**_” nel caso deterministico si chiamano $DTIME$: data una _funzione totale e calcolabile f_, 
$$\begin{align}DTIME[f(n)] = &\{ L \subseteq\{0,1\}^\star| \exists T (\text{deterministica})\text{che DECIDE L e},\\& \forall x\in \{0,1\}^\star, dtime(T,x) \in O( f(|x|) ) \}\end{align}$$

>[!error]- Osservazione
>Nella Teoria della Complessità Computazionale si parla di classi invece che di insiemi
>**ATTENZIONE**: $dtime$ (minuscolo) è la misura di complessità, ossia, una funzione;                   $DTIME$ (maiuscolo) è una classe di complessità, ossia, un insieme!
>Si osservi che $DTIME[ f(n) ] = DTIME[ f(n)/2 ] = DTIME[2 f(n)+58 ] =\dots$
>come è giusto che sia a seguito del **Teorema di accelerazione lineare.** [^2]

Le classi che misurano “_**efficienza spaziale**_” nel caso deterministico si chiamano  DSPACE: data una _funzione totale e calcolabile f_, 																															$$\begin{align}DSPACE[f(n)] = &\{ L \subseteq\{0,1\}^\star | \exists T(\text{deterministica})\text{che DECIDE L e},\\& \forall x \in \{0,1\}^\star, dspace(T,x) \in O( f(|x|) ) \}\end{align}$$
## Classi di complessità non deterministiche

Le stesse considerazioni che ci hanno condotto a definire le classi di complessità deterministiche, possono essere ripetute anche nel caso non deterministico

Le classi che misurano “_**efficienza temporale**_” nel caso non deterministico si chiamano NTIME: data una funzione _totale e calcolabile f_, 																													$$\begin{align}NTIME[f(n)] = &\{ L \subseteq\{0,1\}^\star | \exists NT(\text{non deterministica})\text{ che ACCETTA L e},\\& \forall x \in L, ntime(NT,x) \in O( f(|x|) ) \}\end{align}$$
Ma perché una classe non deterministica è definita in base al tempo di accettazione, invece che del tempo di decisione? Ricordate quello che abbiamo detto la scorsa lezione: se sappiamo che un linguaggio è accettato entro un certo numero di istruzioni, sappiamo che quel linguaggio è decidibile, <u><i>ma non sappiamo quanto tempo occorre a rigettare le parole del suo complemento!</i></u>
E a noi interessa accettare le parole del linguaggio – non di rifiutare quelle del complemento!

Le classi che misurano “_**efficienza spaziale**_” nel caso non deterministico si chiamano  NSPACE: data una funzione _totale e calcolabile f_, 																															$$\begin{align}NSPACE[f(n)] = &\{ L \subseteq\{0,1\}^\star | \exists NT(\text{non deterministica})\text{ che ACCETTA L e},\\& \forall x \in L, nspace(NT,x) \in O( f(|x|) ) \}\end{align}$$
## Classi complemento

Sia f una funzione totale e calcolabile 
- La classe $coDTIME[f(n)]$ contiene i linguaggi il cui complemento è contenuto in $DTIME[(f(n)]$:																						$$coDTIME[f(n)] = \{L \subseteq\{0,1\}^\star | L^C \in DTIME[f(n)] \} $$
- La classe $coDSPACE[f(n)]$ contiene i linguaggi il cui complemento è contenuto in $DSPACE[(f(n)]$: 																							$$coDSPACE[f(n)] = \{L \subseteq\{0,1\}^\star | L^C \in DSPACE[f(n)] \} $$
- La classe $coNTIME[f(n)]$ contiene i linguaggi il cui complemento è contenuto in $NTIME[(f(n)]$: 																		$$conTIME[f(n)] = \{L \subseteq\{0,1\}^\star | L^C \in NTIME[f(n)] \} $$
- La classe $coNSPACE[f(n)]$ contiene i linguaggi il cui complemento è contenuto in $NSPACE[(f(n)]$: 																			$$coNTIME[f(n)] = \{L \subseteq\{0,1\}^\star | L^C \in NTIME[f(n)] \} $$

Le definizioni formali sono a pag. 10 della dispensa 6

### Piccole osservazioni

Innanzi tutto, perché ci limitiamo a considerare linguaggi definiti sull’alfabeto $\{0,1\}$?
- In realtà, lo facciamo perché è più comodo
- ma potremmo utilizzare un alfabeto qualsiasi (e, quando ci farà comodo, lo faremo)
- tanto, sappiamo che se un linguaggio è deciso da una macchina definita su un alfabeto qualsiasi, allora esiste anche una macchina definita su $\{0,1\}$ che lo decide 
- E le due macchine, sappiamo, sono pure polinomialmente correlate!

Poi, alla funzione f che che definisce una classe di complessità (ad esempio, $DTIME[f(n)]$ ) diamo il nome di _**funzione limite**_
Ma perché viene sempre richiesto che una funzione limite sia totale e calcolabile?
- Si ricordino gli assiomi di Blum?

## Relazioni fra classi di complessità

Siamo al paragrafo 6.4

>[!definition]- Teorema 6.8: 
>Per ogni funzione totale calcolabile $f:\mathbb N\to\mathbb N$,
>$$DTIME[ f (n)] \subseteq NTIME[ f (n)];DSPACE[ f (n)] \subseteq NSPACE[ f (n)]$$

Facile: una macchina di Turing deterministica è una particolare macchina di Turing non deterministica avente grado di non determinismo pari ad 1 e, inoltre, ogni parola decisa in un certo numero di passi è anche accettata in quel  un certo numero di passi, e una parola decisa utilizzando un certo numero di celle è anche accettata in quel  un certo numero di celle

>[!definition]- Teorema 6.9: 
>Per ogni funzione totale calcolabile $f:\mathbb N\to\mathbb N$,
>$$DTIME[ f (n)] \subseteq DSPACE[ f (n)]; NTIME[ f (n)] \subseteq NSPACE[ f (n)] $$

_dim_ :
- Segue direttamente dal Teorema 6.1 [^1] Sia $L \subseteq \{0,1\}^\star$ tale che $L \in DTIME[ f (n)]$: 
- allora, esiste una macchina di Turing deterministica T che decide L e tale che, 		         $$\forall x \in \{0,1\}^\star, dtime(T,x) \in O(f(|x|))$$
- poiché $dspace(T,x) \leq dtime(T,x)$, allora $dspace(T,x) \leq dtime(T,x)in O(f(|x|))$
- questo implica che $dspace(T,x) \in O(f(|x|))$ e che, dunque, $L \in DSPACE[f(n)].$
- Analogo il caso non deterministico

>[!definition]- Teorema 6.10: 
>Per ogni funzione totale calcolabile f :  → ,					
>$$DSPACE[ f (n)] \subseteq DTIME[2^{O(f(n))} ];NSPACE[ f (n)] \subseteq NTIME[2^{O(f(n))}].$$

_dim_
- Anche in questo caso, la prova segue direttamente dal Teorema 6.1. [^1]
- Sia $L \subseteq \{0,1\}^\star | L \in DSPACE[f(n)]$: allora, esiste una macchina di Turing deterministica T che decide L e tale che, per ogni $x \in \{0,1\}^\star$, $dspace(T,x) \in O(f(|x|))$. 
- Poiché $$\begin{align}dtime(T,x) &\leq dspace(T,x)|Q| (|\Sigma|+1)^{dspace(T,x)} = dspace(T,x)|Q| 3^{dspace(T,x)}\\& = 2^{\log{( dspace(T,x))}} |Q| [2^{\log{3}}]^{dspace(T,x)} \\&=|Q| 2^{\log dspace(T,x) + dspace(T,x) \log3}\leq|Q| 2^{[1+\log{3} ] dspace(T,x)}\end{align} $$
- allora $dtime(T,x) ∈ O(2^{O(f(|x|))} )$ 
- e, dunque, $L \in DTIME[ 2^{O(f(n))} ]$.

La dimostrazione per il caso non deterministico è analoga. 

[^1]: Vedi lezione 10 [[Appunti FI/MOD II/Lezione 10#^eaf160|Teorema 6.1]]

>[!definition]- Teorema 6.11: 
>Per ogni funzione totale calcolabile $f:\mathbb N\to\mathbb N$,
>$$DTIME[ f (n)] = coDTIME[f (n)]; DSPACE[ f (n)] = coDSPACE[f (n)].$$

_dim_
- Sia $L \subseteq \{0,1\}^\star | L \in DTIME[f(n)]$: allora, esiste una macchina di Turing deterministica T che decide L e tale che, per ogni $x \in \{0,1\}^\star$, $dtime(T,x) \in O(f(|x|)).$
- Poiché T decide L, allora $T(x)=q_A$ se $x \in L$, e $T(x)=q_R$ se $x \in \{0,1\}^\star-L = L^C$
- Costruiamo una macchina T’ identica a T tranne per il fatto che, rispetto a T, gli stati di accettazione e di rigetto di T’ sono invertiti, 
- allora, per ogni $x \in \{0,1\}^\star$, $dtime(T’,x) \in O(f(|x|)),$
- e, inoltre, $T’(x)=q_R$ se $x \in L$, e $T’(x)=q_A$ se $x \in \{0,1\}^\star-L = L^C.$
- Dunque, T’ decide $L^C$ e, per ogni $x \in \{0,1\}^\star$, $dtime(T’,x) \in O(f(|x|)).$
- Quindi, $L^C \in DTIME[f(n)].$
- Poiché L è un qualunque linguaggio in $DTIME[f(n)]$ e, quindi, $L^C$ è un qualunque linguaggio in $coDTIME[f(n)]$, questo significa che: 
	- per ogni linguaggio $L^C \in coDTIME[f(n)], L^C \in DTIME[f(n)]$
	- per ogni linguaggio $L \in DTIME[f(n)]$, poiché $L^C \in DTIME[f(n)]$, allora $L \in coDTIME[f(n)]$

La dimostrazione per DSPACE e coDSPACE è analoga. 

### Classi "poco precise"

Attenzione: l’utilizzo di $O$ nella definizione delle classi di complessità ha come conseguenza che esse non caratterizzino con precisione i linguaggi
- nel senso che, se dimostriamo che un certo linguaggio L è contenuto, ad esempio, in $DTIME[f(n)]$ (per qualche funzione totale e calcolabile f), allora… esiste una serie _infinita_ di classi DTIME nelle quali L è contenuto!

Andiamo a chiarire

Ricordiamo che, date $f : \mathbb N\to\mathbb N, g :\mathbb N\to\mathbb N$ due funzioni, $f(n) \in O(g(n))$ se
- esistono $n_0 \in\mathbb N$ e $c \in\mathbb N$ tali che, per ogni $n\geq n_0, f(n)\leq  c\cdot g(n)$
 - $\exists n_0\in\mathbb N,\exists c \in\mathbb N  :\forall  n\geq n0 [ f(n)\leq c\cdot g(n) ]$
Ossia, $O(f(n)) \subseteq O(g(n))$ e da questo segue il seguente teorema

>[!definition]- Teorema 6.12: 
>Per ogni coppia di funzioni totali calcolabili $f :\mathbb N\to\mathbb N, g:\mathbb N\to\mathbb N$  tali che $n_0 \in \mathbb N : \forall  n\geq n_0 [ f(n)  g(n) ]$ – ossia $f(n) \leq g(n)$ definitivamente
  $$\begin{align}&DTIME[ f (n)] \subseteq DTIME[g(n)]\\& 			NTIME[ f (n)] \subseteq NTIME[g(n)],\\& 					DSPACE[ f (n)] \subseteq DSPACE[g(n)]\\& 		NSPACE[ f (n)] \subseteq NSPACE[g(n)]. \end{align}$$ 
  Infatti, $O(f(n)) \subseteq O(g(n))$

Ok, allora il Teorema 6.12 ci dice che, se collochiamo un linguaggio L, ad esempio, in $DTIME[f(n)]$, allora L appartiene anche a tutte le classi $DTIME[g(n)]$ tali che, definitivamente, $f(n)\leq g(n)$

E questo, fate attenzione, significa che: se collochiamo un linguaggio L, ad esempio, in $DTIME[f(n)]$, questo non implica che L non possa appartenere anche a qualche classe $DTIME[r(n)]$ tali che, definitivamente, $r(n)\leq   f(n)!$

Che, detto altrimenti, significa che qualcuno potrebbe progettare per decidere L un algoritmo più efficiente del nostro!

Perciò, aver collocato un linguaggio L, ad esempio, in $DTIME[f(n)]$, è aver fatto solo metà del lavoro :
- l’altra metà sarebbe dimostrare che L non appartiene a $DTIME[r(n)]$ per alcuna funzione r(n) tale che, definitivamente, $r(n)\leq   f(n)$!
- e questo è un compito parecchio più complesso

Di contro, nella definizione di una teoria della complessità in grado di classificare significativamente i linguaggi in classi di complessità crescente, 
- perché, in definitiva, noi vorremmo poter dire; “questo problema **è più difficile** di quest’altro”
sarebbe auspicabile che $DTIME[f(n)]$ non fosse contenuto in $DTIME[g(n)]$ quando f(n) è molto più grande di g(n) – ad esempio, quando $f (n) = 2^{g(n)}$ !
Ma, invece:


>[!definition]- Teorema 6.13 (Gap Theorem): 
>Esiste una funzione totale calcolabile $f :\mathbb N  \to\mathbb N$ tale che	$$DTIME[ 2^{f(n)} ] \subseteq DTIME[f(n)]. $$
E allora?!
  
[^2]: Vedi lezione 11 [[Lezione 11#^8409f2|Teorema 6.7]]

