
# Funzioni time/space - constructible

>[!definition]- Definizione 6.1: 
>Una funzione totale e calcolabile $f :\mathbb N  \to\mathbb N$ è **time-constructible** se esiste una macchina di Turing T di tipo trasduttore che, preso in input un intero n espresso in notazione unaria (ossia, come sequenza di n ‘1’), scrive sul nastro output il valore f(n) in unario e $dtime(T,n) \in O(f(n))$ . 

>[!definition]- Definizione 6.2: 
>Una funzione totale calcolabile $f :\mathbb N  \to\mathbb N$ è **space-constructible** se esiste una macchina di Turing T di tipo trasduttore che,preso in input il valore n espresso in notazione unaria, scrive sul nastro output il valore f (n) in unario e $dspace(T,n) \in O(f(n))$. 


D’ora in poi scriveremo $1^n$ per intendere una sequenza di n ’1’ – ossia, “n espresso in notazione unaria”

>[!error]- Attenzione: 
>L’input n di una macchina che testimonia la time-contructibility (o la space-constructibility) di una funzione f deve essere in _notazione unaria_
>- ad esempio, 5 è espresso come $1^5 = 11111$
>- questo significa che la lunghezza dell’input è uguale al valore dell’input: $|n| = n$
>- e quella macchina scrive sul nastro di output il valore f(n) in notazione unaria

Una funzione time-constructible è molto più che una funzione totale e calcolabile, **è una funzione che può essere calcolata in tempo proporzionale al suo valore**
- in parole povere, scrivere un ‘1’ sul nastro di output richiede alla macchina che la calcola di eseguire un numero costante di istruzioni (in media)

E analogamente per le funzioni space-constructible

Tutte le funzioni “regolari” con le quali abbiamo normalmente a che fare sono sia time- constructible che space-constructible:
- tutti i polinomi – ossia, $f(n) = n^k$, con k costante
- le funzioni esponenziali – ossia, $f(n) = 2^n$, o anche $f(n) = n^n$ , 
- e tantissime altre
- grosso modo, le funzioni “regolari” sono time/space-constructible


## Addio Gap Theorem

La funzione totale calcolabile $f :\mathbb N\to\mathbb N$ definita nel gap theorem **non** è time-constructible!
E, infatti valgono i seguenti teoremi

>[!definition]- Teorema 6.14 (Teorema di gerarchia spaziale):
> Siano $f :\mathbb N\to\mathbb N , g :\mathbb N\to\mathbb N$ due funzioni tali che f è space-constructible  e $$\lim_{n\to\infty}\frac{g(n)}{f(n)}=0$$
> Allora, $DSPACE[g(n)]\subset  DSPACE[ f (n)]$, ossia, esiste un linguaggio L tale che 	$L\in   DSPACE[ f(n)]$ e $L \not\in DSPACE[ g(n)].$

>[!definition]- Teorema 6.15 (Teorema di gerarchia temporale):
> Siano $f :\mathbb N\to\mathbb N , g :\mathbb N\to\mathbb N$ due funzioni tali che f è time-constructible e $$\lim_{n\to\infty}\frac{g(n)\cdot\log(g(n))}{f(n)}=0$$
>Allora, $DTIME[g(n)]\subset  DTIME[ f (n)]$ ossia, esiste un linguaggio L tale che $L\in   DTIME[ f(n)]$ e $L\not\in  DTIME[g(n)]$. 

Ma qual è il significato dei teoremi di gerarchia spaziale e temporale?
Se $\lim_{n\to\infty}\frac{g(n)}{f(n)}=0$ , allora f(n) cresce “asintoticamente più velocemente” di g(n)
- ossia, man mano che n cresce, la distanza fra g(n) e f(n) aumenta sempre di più
- o, se preferite, f(n) diventa enormemente grande per valori di n molto più piccoli di quelli che occorrono a g(n) per diventare altrettanto grande	   
E un discorso analogo vale (a maggior ragione!) se $$\lim_{n\to\infty}\frac{g(n)\cdot\log(g(n))}{f(n)}=0$$
Quindi, il teorema di gerarchia temporale ci dice che 
- quando f **è time-constructible **
- $DTIME[f(n)]$ non è contenuto in $DTIME[g(n)]$ quando f(n) **è molto più grande** di g(n)

E analogamente per quanto afferma il teorema di gerarchia spaziale relativamente alle classi DSPACE quando f è space-constructible 

## Alcune questioni aperte

C’erano poi, un paio di cose che erano rimaste un po’ in sospeso
Diciamo, non del tutto chiuse

Innanzi tutto, c’era la questione della definizione delle classi di complessità non deterministiche – dove viene richiesta la accettabilità di un linguaggio
- pur sapendo che, ogni volta che fissiamo la quantità massima di risorse (spazio o tempo) utilizzabile, un linguaggio accettabile è anche decidibile
- non conosciamo la quantità di risorse che occorrono per rigettare le parole che non vi appartengono

Poi, sappiamo che tutto ciò che è deciso da una macchina non deterministica può essere deciso anche da una macchina deterministica
- Tuttavia, un linguaggio che sappiamo appartenere a $NTIME[f(n)]$ non sappiamo ancora in quale classe di complessità temporale deterministica collocarlo 
- né sappiamo se il fatto di sapere che appartiene a $NTIME[f(n)]$ ci fornisca strumenti in grado di affermare “ok, allora sta pure in $DTIME[\text{qualche altra funzione}]$”

### La prima questione aperta

Innanzi tutto, non è proprio piacevole dover ammettere che se un certo linguaggio L è in $NTIME[f(n)]$
- ossia, sappiamo che esiste una macchina NT che accetta le sue parole x (ossia, le parole $x\in L$) eseguendo $O( f(|x|))$ istruzioni
non sappiamo quanto tempo occorre per capire che una parola non appartiene a quel linguaggio 
- ossia, quando $x\not\in  L$ non sappiamo quante istruzioni sono eseguite da ciascuna computazione deterministica di NT(x) – che, sappiamo, rigetta

Ebbene, il prossimo teorema afferma che:
- se f è time-constructible e L è in $NTIME[f(n)]$, allora la macchina NT che accetta le parole x di L eseguendo $O(f(|x|))$ istruzioni **è anche capace di _rigettare_ le parole non in L _eseguendo $O(f(|x|))$ istruzioni_;**
- se f è space-constructible e L è in $NSPACE[f(n)]$, allora la macchina NT che accetta le parole di L utilizzando $O(f(|x|))$ celle del nastro è anche capace di rigettare le parole di L utilizzando $O(f(|x|))$ celle del nastro;

>[!definition]- Teorema 6.16: 
>Sia $f : \mathbb N\to\mathbb N$ una funzione time-constructible. Allora, per ogni $L\in  NTIME[ f (n)]$, si ha che L è decidibile in tempo non deterministico in $O( f (n))$. 
>Sia $f : \mathbb N\to\mathbb N$ una funzione space-constructible. Allora, per ogni $L\in  NSPACE[ f (n)]$, si ha che L è decidibile in spazio non deterministico in $O( f (n))$ 

Dimostriamo soltanto il caso in cui f è time-constructible
La dimostrazione del caso in cui f è space-constructible è analoga 
Riutilizziamo, aggiustandola opportunamente, la dimostrazione del Teorema 6.2

>[!definition]- Teorema 6.2 (tempo)
>Sia $f : \mathbb N\to\mathbb N$ una funzione totale calcolabile.
>Se $L\subseteq\Sigma^\star$  è accettato da una macchina di Turing non deterministica NT tale che, per ogni $x \in L, ntime(NT,x) \leq f (|x|)$ allora L è decidibile.

Lo vedete quanto si assomigliano i due teoremi?

_**Dim**_

$L\in  NTIME[ f (n)]$: sia NT la macchina che accetta L, e assumiamo che, per $x \in L,ntime(NT,x) \leq c f(|x|)$, per qualche costante $c > 0$

Poiché f è time-constructible, anche $c f$ è time-constructible: allora, esiste una macchina $T_f$ di tipo trasduttore tale che, per ogni $n\in\mathbb N$, $T_f (1^n)$ termina :
- con il valore $c f(n)$ scritto sul nastro di output in unario
- dopo aver eseguito $O(c f(n))$ istruzioni
Costruiamo una nuova macchina non deterministica NT’, a tre nastri, che decide L: per ogni $x\in\Sigma^\star$ :
- NT’(x) scrive |x| in unario sul secondo nastro e invoca $T_f(|x|)$: al termine della computazione sul terzo nastro si troverà scritto $c f(|x|)$ in unario
- NT’(x) invoca NT(x) e, per ogni quintupla eseguita "_non deterministicamente_" da NT(x):
	- NT’ “cancella” un ‘1’ dal terzo nastro e, inoltre,
	- se NT(x) accetta allora anche NT’(x) accetta, se NT(x) rigetta allora anche NT’(x) rigetta;
- Se quando il terzo nastro di NT’ è vuoto NT(x) non ha ancora terminato, allora NT’(x) rigetta

Osserviamo, intanto, che le computazioni di NT’ terminano sempre
- se la simulazione di una computazione di NT(x) dura più di $c f(|x|)$ passi, la interrompiamo! 

Poi, NT’ decide L, infatti:
- se $x\in L$, allora NT(x) accetta in al più $c f(|x|)$ passi: e, quindi, NT’(x) accetta
- se $x\not\in  L$, allora o NT(x) rigetta in al più $c f(|x|)$ passi e, quindi, NT’(x) rigetta, oppure NT(x) non termina entro $c f(|x|)$ passi e, quindi, NT’(x), ugualmente, rigetta

Ma quanto impiega NT’ a decidere se $x\in L$ oppure no?
- $O(c f(|x|)$ per calcolare $c f(|x|)$ – perché $c f$ è time-constructible!
- e altri $c f(|x|)$ passi per simulare $c f(|x|)$ passi di NT(x), ossia, $O(f(|x|))$ passi
**Per questo possiamo concludere che L è decidibile, in tempo non deterministico** $O(f(n))$

### La seconda questione aperta

Le uniche relazioni che conosciamo (fino ad ora) fra classi deterministiche e classi non deterministiche sono quelle banali: 	$$DTIME[f(n)] \subseteq NTIME[f(n)],   DSPACE[ f (n)] \subseteq NSPACE[ f (n)].$$ 
basate sull’osservazione che una macchina deterministica è una particolare macchina non deterministica

A parte ciò, sappiamo che tutto ciò che è deciso da una macchina non deterministica può essere deciso anche da una macchina deterministica. 

Tuttavia, un linguaggio che sappiamo appartenere a $NTIME[f(n)]$ non sappiamo in quale classe di complessità temporale deterministica collocarlo 
- non sappiamo se esiste un funzione g(n) che magari cresce molto più velocemente di f(n) tale che possiamo affermare “se L appartiene a $NTIME[f(n)]$ allora L appartiene a $DTIME[g(n)]$”
a meno che la funzione limite f della classe non sia una funzione time-constructible…

>[!definition]- Teorema 6.17:
> Per ogni funzione time-constructible $f :\mathbb N\to\mathbb N$,$$NTIME[ f (n)] \subseteq DTIME[ 2^{O( f (n))} ]$$

_**Dim**_

Sia $L \subseteq \{0,1\}^\star$ tale che $L \in NTIME[ f (n) ]$; allora esistono 
- una macchina di Turing non deterministica NT che accetta L 
- una costante h 
tali che, per ogni $x \in L$, $ntime(NT,x) \leq hf(|x|)$.

Poichè $h f$ è time-constructible, esiste $T_f$ che, con input $1^n$, calcola $1^{hf(n)}$ in tempo $O( f(n))$. 

Indichiamo con k il grado di non determinismo di NT, e utilizziamo di nuovo la tecnica della simulazione per definire una macchina di Turing deterministica T, dotata di 3 nastri, che simuli il comportamento di NT: 
- su input x, T simula in successione, una dopo l’altra, tutte le computazioni deterministiche di NT (x) di lunghezza $h f (|x|).$

La macchina T con input x opera in due fasi, come di seguito descritto: 
1) Simula la computazione $T_f(|x|)$: 
	- per ogni carattere di x, scrive sul secondo nastro un carattere ‘1’
	- in seguito, calcola $1^{f(|x|)}$ scrivendolo sul terzo nastro 
	- infine, concatena h volte il contenuto del terzo nastro ottenendo il valore $1^{ h f (|x|)}$
		- (stiamo dimostrando che: se f è time-constructible allora anche $h f$ è time constructible, cosa che nel teorema precedente avevamo solo enunciato). 
2) Simula, una alla volta, tutte le computazioni deterministiche di NT(x) di lunghezza $h f(|x|)$ utilizzando, per ciascuna computazione, la posizione della testina sul terzo nastro come contatore:
	- simula al più $h f(|x|)$ passi della computazione _**più a sinistra**_ di tutte nell’albero NT(x): se tale computazione accetta entro $h f(|x|)$ passi allora T termina in $q_A$, altrimenti
	- simula al più $h f(|x|)$ passi della computazione _**immediatamente più a destra**_ di quella appena simulata: se tale computazione accetta entro $h f(|x|)$ passi allora T termina in $q_A$, altrimenti
	- …
	- simula al più $h f(|x|)$ passi della computazione _**più a destra di tutte**_ nell’albero NT(x): se tale computazione accetta entro $h f(|x|)$ passi allora T termina in $q_A$, altrimenti T termina in $q_R$

T decide L: infatti, poiché in al più $h f(|x|)$ passi NT accetta le parole $x\in  L$, allora 
- se $x\in L$, in $hf(|x|)$ passi una delle computazioni deterministiche di NT(x) termina nello stato di accettazione 
	- durante la FASE 2), poiché T simula i primi $h f(|x|)$ passi di tutte le computazioni deterministiche di NT(x) fino a quando una di esse accetta oppure non le ha esaminate tutte, prima o poi T simulerà anche quella accettante: e questo porterà T nello stato $q_A$
- se $x\not\in L$, in $hf(|x|)$ passi nessuna delle computazioni deterministiche di NT(x) termina nello stato di accettazione 
	- durante la FASE 2), T dovrà simulare i primi $h f(|x|)$ passi di tutte le computazioni deterministiche di NT(x) (da quella più a sinistra nell’albero a quella più a destra, nessuna esclusa), perché nessuna di esse accetta: e questo porterà T nello stato $q_R$
Questo prova che T decide L. 

Ma quanto tempo impiega T a decidere L? 
- Intanto, la FASE 1) richiede $O( h f(|x|)$ passi – perché f è time-constructible
- Poi, riguardo la FASE 2):
	- sia k il grado di non determinismo di NT,  k è costante!
	- allora, il numero di computazioni deterministiche di NT(x) di lunghezza $h f(|x|)$ è  $k^{ h f(|x|)}$ 
	- ciascuna di queste computazioni viene simulata da T in $O( h f(|x|))$ passi. 
Allora, $$dtime(T,x)\in  O( h f(|x|) + h f(|x|) k^{h f(|x|)} ) = O( h f(|x|) k^{h f(|x|)} ) \subseteq O(2^{O(f(|x|)} ).$$
Infine, in virtù del Teorema 6.3, esiste una macchina $T_1$ ad un nastro tale che 
- per ogni input x, l’esito della computazione $T_1(x)$ coincide con l’esito della computazione T(x) 
- ed esiste una costante c tale che $dtime(T:1, x)\leq dtime(T, x)^c \in O(2^{O( f(|x|) )} ).$
Questo conclude la dimostrazione che $L\in  DTIME[2^{O( f (|x|))} ].$ $\square$

