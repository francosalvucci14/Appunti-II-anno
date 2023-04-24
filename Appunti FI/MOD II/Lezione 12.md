
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

