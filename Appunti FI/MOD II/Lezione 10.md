
# Misure di complessità

Siamo alla dispensa 6, paragrafo 6.1
Una misura di complessità è una **funzione c** che associa un valore numerico ad una macchina di Turing T e ad un suo input x 
- $c(T,x)$ intende rappresentare il “costo” della computazione T(x)
- 
Affinché c possa essere considerata una misura di complessità, essa deve soddisfare le due seguenti proprietà, note come _**assiomi di Blum**_: 
1) <u>c è definita per tutte e sole le computazioni che terminano </u>
	2) se una computazione T(x) non termina, non ha senso considerare che tale computazione abbia come costo un valore finito; 
2) <u>c deve essere una funzione calcolabile:</u>
	1) deve esistere una macchina di Turing M che, ricevendo in input una macchina di Turing T ed un suo input x, calcola c(T,x) ogniqualvolta c(T,x) è definita (cioè, ogniqualvolta T (x) termina) 
	2) intuitivamente, questo significa che, il costo di una computazione  T(x) (che termina) dobbiamo poterlo calcolare effettivamente. 

## Misure deterministiche 

Iniziamo con le misure di complessità che si riferiscono a computazioni deterministiche.
- per ogni macchina di Turing deterministica T (riconoscitore o trasduttore), definita su un alfabeto $\Sigma$, 
- e per ogni $x\in\Sigma^\star$ 

definiamo le due **funzioni** seguenti associate alla computazione T(x): 
$$\begin{align}&dtime(T,x)=\begin{cases}\text{Numero di istruzioni eseguite da T(x)}&\text{se T(x) termina}\\\text{non definita}&\text{se T(x) non termina}\end{cases}\\&dspace(T,x)=\begin{cases}\text{Numero di celle di memoria utilizzate da T(x)}&\text{se T(x) termina}\\\text{non definita}&\text{se T(x) non termina}\end{cases}\end{align}$$

Osserviamo che **dtime** e **dspace** sono due funzioni **parziali**: non sono definite se T(x) non termina

Dimostriamo ora che le funzioni **dtime** e *dspace* soddisfano i due assiomi di Blum. 
1)  Facile: lo abbiamo già osservato! 
	1) Per ogni macchina di Turing deterministica T e per ogni $x\in\Sigma^\star$ , $dtime(T,x)$ e $dspace(T,x)$ sono definite se e solo se $T (x)$ termina. 
2)  Dobbiamo mostrare che dtime e dspace sono calcolabili. Iniziamo da dtime:
	1) Consideriamo una modifica $U_{dtime}$ della macchina di Turing universale U:
	2) aggiungiamo ad U il nastro $N_5$ che fungerà da contatore del numero di istruzioni della computazione $T(x)$
	3) $U_{dtime}(T,x)$ si comporta come $U(T,x)$ con l’unica differenza che, dopo avere eseguito una quintupla della macchina T su input x ed essersi preparata ad eseguire la quintupla successiva, scrive un 1 sul nastro $N_5$ e muove a destra la testina su tale nastro. 
	4) Al termine della computazione $U_{dtime}(T,x)$ (se essa termina) il nastro $N_5$ conterrà, codificato in unario, il numero di passi eseguiti dalla computazione $T(x)$
	5) dunque, **dtime** è una funzione calcolabile. 

La dimostrazione che dspace è una funzione calcolabile è simile

## Misure non deterministiche

Passiamo ora a definire le misure di complessità che si riferiscono a computazioni non deterministiche.
- per ogni macchina di Turing non deterministica NT (di tipo riconoscitore), definita su un alfabeto $\Sigma,$ 
- e per ogni $x\in\Sigma^\star$ 
- tali che **NT(x) ACCETTA**, 

definiamo le due funzioni seguenti: 
- $ntime(NT,x)$ = <u>minimo</u> numero di istruzioni eseguite da una computazione deterministica accettante di NT(x) 
- $nspace(NT,x)$ = <u>minimo</u> numero di celle utilizzate da una computazione deterministica accettante di NT(x).

Osservate che ntime e nspace sono due _funzioni parziali_, avendole definite solo per computazioni accettanti!

Potremmo aggiungere: 
- **se NT(x) non accetta**, anche quando NT(x) termina, allora
	- $ntime(NT,x)$ non è definita
	- $nspace(NT,x)$ non è definita

Ma perché, nella definizione di ntime e nspace, si parla di computazioni che “accettano” invece che di computazioni che “terminano”?

Ricordiamo che : 
- NT(x) accetta se _**esiste**_ una sua computazione deterministica che accetta
- NT(x) rigetta se _**tutte**_ le sue computazioni deterministiche rigettano

Perciò, se vogliamo estendere le definizioni di ntime e nspace a tutte le computazioni che terminano, dobbiamo dire che: per ogni macchina di Turing non deterministica NT, definita su un alfabeto $\Sigma$, e per ogni $x\in\Sigma^\star$ tali che NT(x) RIGETTA :
- $ntime(NT,x)$ = **massimo** numero di istruzioni eseguite da una computazione deterministica rigettante di  NT(x) 
- $nspace(NT,x)$ = **massimo** numero di celle utilizzate da una computazione deterministica rigettante di NT(x).

Anche con questa estensione, le funzioni ntime e nspace restano funzioni parziali

## Relazioni fra spazio e tempo

>[!definition]- Teorema 6.1 (caso deterministico)
>Sia T una macchina di Turing deterministica, definita su un alfabeto $\Sigma$ (non contenente il simbolo $\square$ ) e un insieme degli stati $Q$, e sia $x\in\Sigma^\star$ tale che $T(x)$ termina. Allora $$dspace(T,x)\leq dtime(T,x)\leq dspace(T,x)\cdot|Q|\cdot(|\Sigma|+1)^{dspace(T,x)}$$

1) $dspace(T,x) ≤ dtime(T,x)$ 
	1) Facile: se $T(x)$ utilizza $dspace(T,x)$ celle di memoria, quelle celle deve almeno leggerle
	2) e, per leggere ciascuna cella impiega un’istruzione (ossia, esegue una quintupla)
	3) In realtà esistono dei casi chiamati "casi anomali", per questo la definizione di dspace è un po’ diversa da quella che abbiamo visto
	7) ma noi ci teniamo quella e non consideriamo questi casi “anomali”

2) $dtime(T,x)\leq dspace(T,x)\cdot|Q|\cdot(|\Sigma|+1)^{dspace(T,x)}$
	1) Osserviamo che $dspace(T,x)\cdot|Q|\cdot(|\Sigma|+1)^{dspace(T,x)}$ è il numero di stati globali possibili di T nel caso in cui non più di $dspace(T,x$) celle del nastro vengano utilizzate dalla computazione T(x)
	2) Infatti: 
		1) poiché ogni cella del nastro può contenere un simbolo di $\Sigma$ oppure il blank, il numero di possibili configurazioni di $dspace(T,x)$ celle del nastro è     
		2) poi, per ognuna di queste configurazioni
			1) la testina può trovarsi su una qualsiasi delle $dspace(T,x)$ celle
			2) e la macchina può essere in uno qualsiasi dei $|Q|$ stati interni
	3) e questo è ben spiegato nella dispensa.
	4) Chiamiamo $k(T,x)$ questo valore: $k(T,x) = dspace(T,x)\cdot|Q|\cdot(|\Sigma|+1)^{dspace(T,x)}$
	5) Dunque: $k(T,x) = dspace(T,x)\cdot|Q|\cdot(|\Sigma|+1)^{dspace(T,x)}$ è il numero di stati globali possibili di T nel caso in cui non più di $dspace(T,x)$ celle del nastro vengano utilizzate dalla computazione $T(x)$
	6) Ora, ricordiamo che una computazione (deterministica) è una successione di stati globali tali che si passa da uno stato globale al successivo eseguendo una quintupla
	7) se $T(x)$ durasse più di $k(T,x)$ passi (senza uscire mai dalle $dspace(T,x)$ celle), allora sarebbe una successioni di stati globali contenente almeno due volte uno stesso stato globale – chiamiamolo $SG_H$ : ![[appunti fi/mod ii/immagini/Pasted image 20230407103213.png|center|350]]
	8) ma T è deterministica; allora, a partire da  è possibile eseguire un’unica quintupla (quella che porta nello stato globale $SG_{h+1}$) ed essa viene eseguita tutte le volte in cui T(x) si trova in $SG_h$
	9) quindi, entrambe le volte, avviene una transizione verso lo stesso stato globale $SG_{h+1}$
	10) e così via, e così via: T(x) sarebbe in loop (contro l’ipotesi che termina)
		1) studiatelo sulla dispensa (dove è descritto meglio!)

>[!definition]- Teorema 6.1 (caso non deterministico)
>Sia NT una macchina di Turing non deterministica, definita su un alfabeto $\Sigma$ (non contenente il simbolo $\square$ ) e un insieme degli stati $Q$, e sia $x\in\Sigma^\star$ tale che NT(x) accetta/termina. Allora $$nspace(NT,x)\leq ntime(NT,x)\leq nspace(NT,x)|Q|(|\Sigma|+1)^{nspace(NT,x)}$$

Questa dimostrazione è sensibilmente più complessa di quella del caso deterministico, e non verrà studiata
Ma si consiglia la visione

### Verso le classi di complessità

Sia $f : \mathbb N\to\mathbb N$  una funzione totale calcolabile.
Sia $\Sigma$ un alfabeto finito e sia $x\in\Sigma^\star$: indichiamo con $|x|$ il numero di caratteri di x

Un linguaggio $L\subseteq\Sigma^\star$ è **_deciso** in tempo (spazio) deterministico_ $f(n)$ se 
- esiste una macchina di Turing deterministica T che decide L e tale che, 
- per ogni $x\in\Sigma^\star$, $dtime(T,x)\leq f(|x|)\space\space	( dspace(T,x) = f(|x|) )$.

Un linguaggio $L\subseteq\Sigma^\star$  è **_accettato** in tempo (spazio) non deterministico_ $f(n)$ se
- esiste una macchina di Turing non deterministica NT che accetta L e tale che, 
- per ogni $x\in L$, $ntime(NT,x)\leq f(|x|)$ 	$( nspace(NT,x) \leq f(|x|) )$

Un linguaggio $L\subseteq\Sigma^\star$  è **_deciso** in tempo (spazio) non deterministico_ $f(n)$ se
- esiste una macchina di Turing non deterministica NT che decide L e tale che 
- per ogni $x\in\Sigma^\star$, $ntime(NT,x) \leq f(|x|)$		$(nspace(NT,x)\leq f (|x|))$. 

### Dall'accettazione alla decisione

Si osservi che 
- nel caso deterministico definiamo soltanto i linguaggi decisi in un certo tempo o spazio 
- nel caso non deterministico distinguiamo in linguaggi accettati in un certo tempo o spazio da quelli decisi nello stesso tempo o spazio

Ma perché?

Si potrebbe pensare che esistono linguaggi che sono accettabili in un certo tempo o spazio, ma che non sono decidibili – ossia, il loro complemento non è accettabile
- ma, allora, verrebbe da chiedersi, perché questa cosa esce fuori solamente quando si utilizza una macchina non deterministica?!

In effetti, non è così: il prossimo teorema mostra che, ogni qualvolta una funzione totale e calcolabile limita la quantità di risorse disponibili al fine di accettare le parole di un linguaggio, i concetti di accettabilità e di decidibilità coincidono. 

>[!definition]- Teorema 6.2 (tempo)
>Sia $f : \mathbb N\to\mathbb N$ una funzione totale calcolabile.
>Se $L\subseteq\Sigma^\star$  è accettato da una macchina di Turing non deterministica NT tale che, per ogni $x \in L, ntime(NT,x) \leq f (|x|)]$ allora L è decidibile.

**Dim**

Poiché f è totale calcolabile, esiste una macchina $T_f$ di tipo trasduttore tale che, per ogni $n\in\mathbb N$, $T_f (n$) termina con il valore $f(n)$scritto sul nastro di output

Costruiamo una nuova macchina non deterministica NT’, a tre nastri, che decide L: per ogni $x\in\Sigma^\star$ : 
- FASE 1) NT’(x) scrive |x| sul secondo nastro e invoca $T_f(|x|)$: al termine della computazione sul terzo nastro si troverà scritto $f(|x|)$ in unario
- FASE 2) NT’(x) _simula_ NT(x) e, per ogni quintupla eseguita da NT(x):
	- NT’ “cancella” un ‘1’ dal terzo nastro e, inoltre,
	- se NT(x) accetta allora anche NT’(x) accetta, se NT(x) rigetta allora anche NT’(x) rigetta;
- se quando il terzo nastro di NT’ è vuoto NT(x) non ha ancora terminato, allora NT’(x) rigetta

Si osservi che le computazioni di NT’ terminano sempre
- se una computazione NT’(x) dura più di f(|x|) passi, la interrompiamo!

Poi, NT’ decide L, infatti:
- se $x \in L$, allora NT(x) accetta in al più $f(|x|)$ passi: e, quindi, NT’(x) accetta
- se $x \not\in L$, allora o NT(x) rigetta in al più $f(|x|)$ passi e, quindi, NT’(x) rigetta, oppure NT(x) non termina entro $f(|x|)$ passi e, quindi, NT’(x), ugualmente, rigetta
Ma quanto impiega NT’ a rigettare x  L?
- Non possiamo sapere quanto tempo impiega $T_f$ a calcolare $f(|x|)$?
- Sappiamo solo che $T_f (|x|)$ termina, ma non in quanto tempo!

_Per questo possiamo concludere che L è decidibile, ma non possiamo concludere che è deciso in tempo non deterministico f(n)_

>[!definition]- Teorema 6.2 (spazio)
>Sia $f : \mathbb N\to\mathbb N$  una funzione totale calcolabile.
>Se $L\subseteq\Sigma^\star$ è accettato da una macchina di di Turing non deterministica NT tale che, per ogni $x \in L$, $nspace(NT,x) \leq f (|x|)]$ allora L è decidibile. 

La dimostrazione è analoga al caso di ntime

## Complessità e modelli di calcolo

Siamo al paragrafo 6.2 della dispensa 6
Qui si dimostra che che tutti i modelli di calcolo deterministici sono fra loro _**polinomialmente correlati**_
- Macchine di Turing ad un nastro
- Macchine di Turing a quanti nastri ci pare
- Macchine di Turing su alfabeto binario
- Macchine di Turing su alfabeti grandi quanto ci pare

Ma che vuol dire che questi modelli sono fra loro polinomialmente correlati?
- che per ogni macchina di Turing T di uno di questi tipi esistono una macchina di Turing T’ di uno qualunque degli altri tipi ed un polinomio p tali che T’ risolve lo stesso problema risolto da T e, per ogni x, $dtime(T’,x) \leq p( dtime(T,x) )$ e $dspace(T’,x) \leq p( dspace(T,x) )$ 

E anche che il modello Macchina di Turing è polinomialmente correlato con il PascalMinimo

Ok, ma cosa significa tutto ciò?
Che possiamo risolvere un problema utilizzando il modello che più ci aggrada
- ad esempio, per risolvere un certo problema possiamo scrivere un algoritmo A in PascalMinimo (invece che stare lì a progettare quintuple di una macchina di Turing)
- e se A trova la soluzione di una istanza x del problema eseguendo f(|x|) istruzioni allora esiste una macchina di Turing T ad un nastro che risolve lo stesso problema, ed esiste un polinomio p tale che $dtime(T,x) \leq  p( f(|x|)$

Ma perché è così importante sapere che sono polinomialmente correlati?
- Beh, perché se abbiamo un algoritmo in PascalMinimo che impiega un numero di istruzioni polinomiale nella lunghezza dell’input per risolvere il problema
- sappiamo anche che esiste una macchina di Turing che risolve lo stesso problema eseguendo, anch’essa, un numero di istruzioni polinomiale nella lunghezza dell’input

_**E un problema è trattabile se il tempo necessario a risolverlo è polinomiale (nella dimensione dell’input)**_
- perciò, se un problema è trattabile rispetto ad un modello, è trattabile anche rispetto a tutti gli altri!

