
# Riducibilità polinomiale

La maggior parte delle relazioni fra classi complessità che abbiamo visto, fino ad ora, sono **inclusioni improprie**.
A parte $P\subset  EXPTIME$  e $PSPACE = NPSPACE$

Ossia, a parte queste due ultime relazioni, per ciascuna delle rimanenti relazioni non siamo in grado di dimostrare né l’inclusione propria né la coincidenza delle due classi che la costituiscono. 

Ad esempio, sappiamo che 
- tutti i linguaggi che sono in PSPACE sono anche in EXPTIME $(PSPACE \subseteq EXPTIME)$
- tutti i linguaggi che sono in P sono anche in NP $(P\subseteq  NP)$
Ma non sappiamo rispondere alle seguenti domande
- non sarà forse che tutti i linguaggi in EXPTIME sono anche in PSPACE? Ossia, che 			$PSPACE = EXPTIME$?
- Oppure, esiste almeno un linguaggio in NP che _**non**_ può essere deciso in tempo deterministico polinomiale? Ossia: è $P \subset NP$ oppure $P = NP$

Le relazioni che conosciamo sono, in massima parte, relazioni **deboli**

E, inoltre, pur riuscendo a dimostrare che una certa classe di complessità $\mathcal C_1$ è contenuta propriamente in un’altra classe di complessità $\mathcal C_2$ (ossia,$\mathcal C_1\subset\mathcal C_2$)

Anche in questo caso, seppure dimostriamo che un certo linguaggio L appartiene a $\mathcal C_2$, 
come facciamo a sapere se quel linguaggio è anche in $\mathcal C_1$ oppure se, invece, è un _**linguaggio separatore**_ fra $\mathcal C_1$ e $\mathcal C_2$, ossia è contenuto in $\mathcal C_2-\mathcal C_1$?

## $=$ oppure $\neq$

Date due classi di complessità $\mathcal C_1$ e $\mathcal C_2$ tali che $\mathcal C_1\subseteq\mathcal C_2$, come fare per poter capire se $\mathcal C_1=\mathcal C_2$ oppure $\mathcal C_1\neq\mathcal C_2$?

Idea: se per caso trovassimo un linguaggio$L_0 \in \mathcal C_2$ tale che  
- supponendo di avere un algoritmo $\mathcal A$ che decide $L_0$ utilizzando una quantità di risorse pari a quella che definisce la classe $\mathcal C_1$
- per ogni altro linguaggio L in $\mathcal C_2$ riusciamo a costruire, simulando $\mathcal A$ , un algoritmo $\mathcal B_1$ che decide L e che utilizza una quantità di risorse pari a quella che definisce la classe $\mathcal C_1$

Allora, se riuscissimo davvero a progettare $\mathcal A$, sapremmo automaticamente che tutti i linguaggi in $\mathcal C_2$ sono anche in $\mathcal C_1$ 
E, d’altra parte, questo implicherebbe anche che
- se qualcuno riuscisse a dimostrare che $\mathcal C_1\neq\mathcal C_2$ allora sapremmo automaticamente che $L_0\not\in\mathcal C_1$ 
 
$L_0$ **sarebbe il padre di tutti i linguaggi in** $\mathcal C_2$

### Ritornando alle riduzioni

Dati due linguaggi, $L_1\subseteq\Sigma_1^\star$  e $L_2\subseteq\Sigma_2^\star$,  diciamo che $L_1$ è riducibile a $L_2$ e scriviamo $L_1\preceq  L_2$ se:
Esiste una funzione $f :\Sigma_1^\star\to\Sigma_2^\star$ tale che
1) f è totale e calcolabile, 
	1) è definita per ogni parola $x\in\Sigma_1^\star$ e, inoltre, 
	2) esiste una macchina di Turing di tipo trasduttore $T_f$ tale che, per ogni parola $x\in\Sigma_1^\star$, la computazione $T_f (x)$ termina con la parola $f(x)\in\Sigma_2^\star$ scritta sul nastro di output
2) per ogni $x\in\Sigma_1^\star$ vale che: $x \in L_1$ se e solo se $f(x)\in  L_2$ :
$$\forall x\in\Sigma_1^\star [ x \in L_1\iff   f(x)\in  L_2 ]$$

Ora, aggiungiamo una piccola richiesta alla funzione di riduzione f: richiediamo che
oltre ad essere totale e calcolabile
3) per ogni $x\in\Sigma_1^\star$, f(x) è calcolabile in tempo polinomiale in |x| – ossia, $f\in FP$

#### Un nuovo strumento

Dati due linguaggi, $L_1\subseteq\Sigma_1^\star$  e $L_2\subseteq\Sigma_2^\star$, diciamo che 
$L_1$ è _**polinomialmente**_ riducibile a $L_2$ e scriviamo $L_1 \preceq_p L_2$  se
Esiste una funzione $f :\Sigma_1^\star\to\Sigma_2^\star$ tale che
1) f è totale e calcolabile in tempo polinomiale (in breve, f  FP) – ossia, 
	1) è definita per ogni parola $x\in\Sigma_1^\star$ e, inoltre, 
	2) esiste una macchina di Turing di tipo trasduttore $T_f$ tale che, per ogni parola $x\in\Sigma_1^\star$ la computazione $T_f (x)$ termina con la parola $f(x)\in\Sigma_2^\star$ scritta sul nastro di output
	3) esiste una costante c tale che: per ogni $x\in\Sigma_1^\star$ , $dtime(T_f,x)\in  O(|x|^c )$
2) per ogni $x\in\Sigma_1^\star$ vale che: $x \in L_1$ se e solo se $f(x)\in  L_2$ :
$$\forall x\in\Sigma_1^\star [ x \in L_1\iff   f(x)\in  L_2 ]$$

E siamo al paragrafo 6.8

Abbiamo questi due linguaggi, e riusciamo a dimostrare che $L_1 \preceq_p L_2$ 
- cioè, dimostriamo che esistono un trasduttore $T_r$ e una costante c tali che, per ogni $x\in\Sigma_1^\star$ e, inoltre, per ogni $x\in\Sigma_1^\star$, $dtime(T_r,x)\in  O(|x|^c )$

Supponiamo di sapere che $L_2 \in DTIME[ f(n) ]$
- cioè, esiste un riconoscitore $T_2$ tale che, per ogni $y\in\Sigma_2^\star$, $T_2(y)$ accetta se e soltanto se $y \in L_2$  e, inoltre, per ogni $y\in\Sigma_2^\star$, $dtime(T_2, y) \in O( f (|y|) )$  

Allora, possiamo costruire la seguente macchina $T_1$ : con input $x\in\Sigma_1^\star$, $T_1$ opera in due fasi (ed utilizza due nastri)
- FASE 1: $T_1$ simula $T_r(x)$ scrivendo l’output y sul secondo nastro
- FASE 2: T1 simula $T_2(y)$ sul secondo nastro: se $T_2(y)$ accetta allora anche $T_1$ accetta, se $T_2(y)$ rigetta allora anche $T_1$ rigetta. 

$T_1$ **decide** $L_1$: 
- perché $T_2(y)$ accetta se e solo se $y\in  L_2$ , e $y\in  L_2$ se e solo se $x\in  L_1$ 

Ma quanto impiega $T_1$ a decidere $L_1$?

La FASE 1 termina in $O(|x|^c )$ passi
la FASE 2 termina in $O( f(|y|) )$ passi
Ma quanto è grande |y| in funzione di |x|?
- beh, poiché $T_r(x)$ impiega $O(|x|^c )$ passi per calcolare y
- e in questo numero di passi sono conteggiati anche i passi che occorrono a scrivere y sul nastro di output
- allora, $|y|\in  O(|x|^c )$
E, quindi, per ogni $x\in\Sigma_1^\star$, $T_1(x)$ termina in $O(|x|^c + f(|x|^c ))$ passi 

Ossia, $L_1\in  DTIME[ n^c + f( n^c ) ]$

Allora, se $L_2\in P$ allora $L_1\in  P$
- in questo caso, esiste una costante k tale che $L_2\in  DTIME[ n^k  ]$
- allora, $L_1\in  DTIME[ n^c + ( n^c )^k ]\subseteq P$

E quindi, se $L_2\in EXPTIME$ allora $L_1\in  EXPTIME$.

Ma si può dimostrare la stessa cosa con le classi non deterministiche:
E anche per le classi spaziali


