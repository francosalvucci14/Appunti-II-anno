
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

Ma si può dimostrare la stessa cosa con le classi non deterministiche

E anche per le classi spaziali

Il **Teorema 6.21** della dispensa 6 dimostra il solo caso “Se $L_1\preceq_p  L_2$ e $L_2\in P$ allora $L_1\in  P$”

## Chiusura di una classe rispetto a $\preceq_{\pi}$

>[!definition]- Definizione 6.4: 
>Una classe di complessità **C è chiusa rispetto ad una generica** $\pi$-riduzione se, per ogni coppia di linguaggi $L_1$ ed $L_2$ tali che $L_1\preceq_{\pi}  L_2$ e $L_2\in  C$, si ha che $L_1\in  C$. 

La chiusura di una classe C rispetto ad una $\pi$-riduzione può essere utilizzata per dimostrare l’appartenenza di un linguaggio L a C: 
- segue direttamente dalla definizione che, se sappiamo che una classe di complessità C è chiusa rispetto ad una $\pi$-riduzione e che un certo linguaggio $L_0$ appartiene a C, allora, se dimostriamo che $L\preceq_{\pi}  L_0$, possiamo dedurre che anche L appartiene a C. 

In questa lezione lo abbiamo dimostrato nel caso delle riduzioni polinomiali quando C = P
- e abbiamo detto che quella dimostrazione valeva anche per NP, EXPTIME, NEXPTIME, PSPACE

## Completezza di un linguaggio per una classe rispetto a $\preceq_{\pi}$

>[!definition]- Definizione 6.3: 
>Sia C una classe di complessità di linguaggi e sia $\preceq_{\pi}$ una generica $\pi$-riduzione. 																					  																	       Un linguaggio $L\subseteq\Sigma^\star$ è **C-completo rispetto alla** $\pi$-riducibilità se: 
>1) $L\in C$ 
>2) per ogni altro $L_0\in  C$, vale che $L_0\preceq_{\pi}  L$. 

Le nozioni di 
- completezza di un linguaggio per una classe rispetto ad una $\pi$-riduzione 
- chiusura di una classe rispetto alla $\pi$-riduzione 
sono gli strumenti che ci permettono di arrivare al concetto di “padre di tutti i linguaggi” per una classe

## Il padre di tutti i linguaggi di una classe

Abbiamo due classi di complessità $C_1$ e $C_2$ tali che $C_1\subseteq C_2$, e sappiamo che $C_1$ è chiusa rispetto ad una qualche $\pi$-riduzione:
- allora, per ogni coppia di linguaggi $L_1$ ed $L_2$ tali che $L_1\preceq_{\pi}  L_2$ e $L_2\in  C_1$,  si ha che $L_1\in  C_1$. 

Se per caso troviamo un linguaggio L $C_2$**–completo** rispetto a $\preceq_{\pi}$ 
- ossia, $L\in  C_2$ e per ogni altro $L_0\in  C_2$, vale che $L_0\preceq_{\pi}  L$
e se dimostriamo che $L\in  C_1$ , abbiamo che:
- per ogni altro $L_0\in  C_2$, vale che $L_0\preceq_{\pi}  L$ e inoltre $L\in  C_1$

Allora, in virtù della chiusura di $C_1$ rispetto alla $\pi$-riduzione, per ogni altro $L_0\in  C_2$, vale che $L_0\in  C_1$

Ma possiamo vederla anche in un altro modo: se $C_1\subseteq C_2$ e L è $C_2$–completo e se qualcuno riuscisse a dimostrare che $C_1\neq  C_2$ , allora sapremmo automaticamente che $L\not\in  C_1$

L sarebbe il padre di tutti i linguaggi in $C_2$: 
- il linguaggio più difficile fra tutti i linguaggi che stanno in $C_2$

E da questo otteniamo

>[!definition]- Teorema 6.20: 
>Siano C e $C_0$ due classi di complessità tali che $C_0\subseteq C$. Se $C_0$ è chiusa rispetto ad una $\pi$-riduzione allora, per ogni linguaggio L che sia C-completo rispetto a $\preceq_{\pi}$, $L\in  C_0$ se e solo se $C = C_0.$

**Dim**
- Se $C = C_0$ , poiché L è C-completo e, dunque $L\in C$, allora $L\in  C_0$.
- Viceversa, supponiamo che $L\in  C_0$. Poiché L è C-completo rispetto a $\preceq_{\pi}$ , allora, per ogni $L’\in  C, L’\preceq_{\pi}   L$. Poiché $C_0$ è chiusa rispetto a $\preceq_{\pi}$ , questo implica che, per ogni $L’\in  C, L’\in  C_0$: quindi, $C = C_0.$

## I linguaggi NP-Completi

A questo punto, abbandoniamo le generiche $\pi$-riduzioni e torniamo definitivamente alle riduzioni polinomiali

>[!definition]- Linguaggio NP-Completo
>Un linguaggio $L\subseteq\Sigma^\star$ è **NP-completo (rispetto alla riducibilità polinomiale)** se
>1) $L\in  NP$
>2) per ogni altro $L_0 \in NP$, vale che $L_0\preceq_p  L$. 

I linguaggi NP-completi sono particolarmente importanti per il loro ruolo di possibili linguaggi separatori fra le classi P e NP:

**Corollario 6.4**: Se $P\neq  NP$ allora, per ogni linguaggio NP-completo L, $L\in  P$. 

**Dim**
- Supponiamo che L sia un linguaggio NP-completo e che $L\in  P$. 
- Poiché L è NP-completo allora, per ogni linguaggio $L_0\in  NP$, $L_0\preceq_p L$; 
- ma, se $L\in  P$, poiché P è chiusa rispetto a $\preceq_p$ , questo implica che, per ogni $L_0\in NP, L_0\in  P$. 
- Ossia, $P = NP$, contraddicendo l’ipotesi. 

Ma quale è il senso del Corollario 6.4?
Intanto che **_è molto improbabile che un linguaggio NP-completo appartenga a P_**
- Ebbene, si sospetta che sia $P\neq  NP$ – ma nessuno è mai riuscito a dimostrarlo, per questo è una congettura

Quindi: se vogliamo dimostrare che, probabilmente, non esiste un algoritmo deterministico che decide in tempo polinomiale un linguaggio che è in NP, quel che dobbiamo fare è dimostrare che quel linguaggio è NP-completo