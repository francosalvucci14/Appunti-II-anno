
# Macchine,linguaggi,funzioni

Siamo partiti cercando di capire come risolvere automaticamente i problemi

E abbiamo studiato la soluzione proposta da Alan Turing che, partendo dalla sua analisi del processo di soluzione, è arrivato a definire il passo elementare di calcolo: una operazione

Da questa idea di operazione elementare, Turing ha introdotto un modello di calcolo: la Macchina di Turing

Beh, a questo punto è ragionevole porsi un po’ di domande:
- utilizzando la Macchina di Turing, possiamo risolvere tutti i problemi? Oppure esiste qualche problema che non è risolubile con la Macchina di Turing?
- E, se esiste qualche qualche problema che non è risolubile con la Macchina di Turing, non sarà forse possibile risolvere quel problema con un altro modello di calcolo?

Siamo alla dispensa 3, paragrafo 3.1

Una macchina di Turing (di tipo riconoscitore) è un oggetto che, se gli diamo un certo input, quella ci risponde se quell’input soddisfa una certa proprietà

L’input di una macchina di Turing è una parola (scritta con i caratteri di un certo alfabeto).

Quindi: una macchina di Turing (di tipo riconoscitore) è un oggetto che, se gli scriviamo una certa parola sul nastro, quella ci risponde se quella parola soddisfa una certa proprietà

Allora, possiamo considerare l’insieme di tutte le parole che soddisfano quella certa proprietà e dire: “la nostra macchina di Turing sa riconoscere le parole che appartengono a tale insieme!”

Ma non è abbastanza formale: che vuol dire esattamente _**riconoscere**_?

## Decidere un linguaggio

Dato un alfabeto $\Sigma$, un **linguaggio** L è un insieme di parole costituite dai caratteri di $\Sigma$ ossia, $L\subseteq\Sigma^\star$

Un linguaggio L è _**deciso**_ da una macchina di Turing T se
- per ogni $x\in L$, la computazione T(x) termina in $q_A$
- per ogni $x\not\in L$, la computazione T(x) termina in $q_R$

Quindi, **le computazioni della macchina T che decide L terminano sempre**: sia che sul nastro di T venga scritto un input appartenente ad L, sia che sul nastro di T venga scritto un input non appartenente ad L, T giunge ad una conclusione

Ossia, T è sempre in grado di distinguere fra le parole di L e le parole che non sono in L. 

Qualunque sia x in $\Sigma^\star$, T ci dice se x è in L oppure no

**Esempio**

Prendiamo la macchina $T_{PAL}$, con le quintuple

- $\langle q_0,a,\square,q_a,D\rangle,\langle q_0,b,\square,q_b,D\rangle$
- $\langle q_a,a,a,q_a,D\rangle,\langle q_a,b,b,q_a,D\rangle,\langle q_b,a,a,q_b,D\rangle,\langle q_b,b,b,q_b,D\rangle$
- $\langle q_a,\square,\square,q_{a_1},S\rangle,\langle q_b,\square,\square,q_{b_1},S\rangle$
- $\langle q_{a_1},a,\square,q_2,S\rangle,\langle q_{a_1},b,b,q_R,F\rangle,\langle q_{b_1},a,a,q_R,F\rangle,\langle q_{b_1},b,\square,q_2,S\rangle$
- $\langle q_2,a,a,q_2,S\rangle,\langle q_2,b,b,q_2,S\rangle,\langle q_2,\square,\square,q_0,D\rangle$
- $\langle q_0,\square,\square,q_A,F\rangle$
- $\langle q_{a_1},\square,\square,q_R,F\rangle,\langle q_{b_1},\square,\square,q_R,F\rangle$ 

$T_{PAL}$ decide il linguaggio $L_{PPAL}$ (Pari e Palindrome) seguente : $$L_{PPAL}=\{x_1x_{2\dots}x_{2n}\in\{a,b\}^\star:n\in\mathbb N\land\forall i\in \{1,2,\dots n\}[x_i=x_{2n-i+1}]\}$$

## Accettare un linguaggio

Dato un alfabeto $\Sigma$, un **linguaggio** L è un insieme di parole costituite dai caratteri di $\Sigma$ ossia, $L\subseteq\Sigma^\star$

Un linguaggio L è _**accettato**_ da una macchina di Turing T se
- per ogni $x\in L$, la computazione T(x) termina in $q_A$
- per ogni $x\not\in L$, la computazione T(x) **non** termina in $q_A$

Quindi, se sul nastro di T viene scritto un input x appartenente ad L, siamo certi (a) che $T(x)$ termina e (b) che $T(x)$ termina in $q_A$

Se sul nastro di T viene scritto un input x non apaprtenente ad L, possiamo solo essere certi che $T(x)$ non termina in $a_A$

Quindi, T è solo in grado di dirci se una parola appartiene ad L

**Esempio**

Modifichiamo le utlime 2 quintuple della macchina $T_{PAL}$ per ottenere la macchina $T_{PAL1}$

- $\langle q_0,a,\square,q_a,D\rangle,\langle q_0,b,\square,q_b,D\rangle$
- $\langle q_a,a,a,q_a,D\rangle,\langle q_a,b,b,q_a,D\rangle,\langle q_b,a,a,q_b,D\rangle,\langle q_b,b,b,q_b,D\rangle$
- $\langle q_a,\square,\square,q_{a_1},S\rangle,\langle q_b,\square,\square,q_{b_1},S\rangle$
- $\langle q_{a_1},a,\square,q_2,S\rangle,\langle q_{a_1},b,b,q_R,F\rangle,\langle q_{b_1},a,a,q_R,F\rangle,\langle q_{b_1},b,\square,q_2,S\rangle$
- $\langle q_2,a,a,q_2,S\rangle,\langle q_2,b,b,q_2,S\rangle,\langle q_2,\square,\square,q_0,D\rangle$
- $\langle q_0,\square,\square,q_A,F\rangle$
- $\langle q_{a_1},\square,\square,q_{a_1},F\rangle,\langle q_{b_1},\square,\square,q_{b_1},F\rangle$

Ebbene, $T_{PAL1}$ accetta il linguaggio $L_{PPAL}$ ma non lo decide.
In particolare:
- accetta le parole palindrome di lunghezza pari
- rigetta le parole non palindrome
- rigetta le parole palindrome di lunghezza pari che hanno 'b' come carattere centrale
- non termina sulle parole palindrome di lunghezza dispari che hanno 'a' come carattere centrale

## Linguaggi decidibili/accettabili

Un linguaggio $L\subseteq\Sigma^\star$ è **decidibile** se esiste una macchina di Turing T che lo decide
- ossia, che, per ogni $x\Sigma^\star$ , T(x) termina:
	- se $x\in L$ allora T(x) termina in $q_A$, se $x\not\in L$ allora T(x) termina in $q_R$ 
Quando un linguaggio L è deciso da una macchina T scriviamo: L= L(T)

Un linguaggio $L\subseteq\Sigma^\star$ è **accettabile** se esiste una macchina di Turing T che lo accetta
- ossia, che, per ogni $x\in L$, T(x) termina in $q_A$ 
	- se $x\not\in L$ allora sappiamo solo che T(x) non termina in $q_A$ : potrebbe terminare in $q_R$ oppure non terminare 

Naturalmente, ogni linguaggio decidibile è anche accettabile – ma non viceversa!

### Linguaggio complemento

Dunque, mentre una macchina che decide un linguaggio su un alfabeto $\Sigma$ sa ben comportarsi con tutte le parole in $\Sigma^\star$, una macchina che accetta un linguaggio su un alfabeto $\Sigma$, invece, non sa sempre come comportarsi sulle parole in $\Sigma^\star$ che non sono in L

Sia $L\subseteq\Sigma^\star$; chiamiamo linguaggio complemento di L il linguaggio $L^C=\Sigma^\star-L$

Allora, possiamo dire che la differenza fra decisione e accettazione di un linguaggio è il comportamento della macchina sul linguaggio complemento

#### Teorema 3.1 (Molto importante)

>[!definition]- Teorema 3.1
>$L\subseteq\Sigma^\star$ è **decidibile** $\iff$ $L$ è accettabile e $L^C$ è accettabile

La dimostrazione si divide in due parti

**Parte I**

**_Se L è decidibile_** allora:
- Chiamiamo T la macchina che decide L
- Dobbiamo costruire una macchina $T_1$ che accetta $L$ e una macchina $T_2$ che accetta $L^C$
- La macchina $T_1$ è la stessa macchina T
	- infatti, $\forall x\in L,T(x)$ termina in $q_A$
- $T_2$ si ottiene invertendo gli stati di accettazione e rigetto di T
	- infatti, poichè T decide L
		- allora per ogni $x\not\in L(\text{equivalente a } x\in L^C),T(x)$ termina in $q_R$
		- e dunque, per ogni $x\in L^C,T_2(x)$ termina in $q_A$

_**Se L è accettabile e $L^C$ è accettabile**_ allora:
- Chiamiamo $T_1$ la macchina che accetta L e $T_2$ che accetta $L^C$
- Dobbiamo costruire una macchina T che decide L
- Dotiamo T di due nastri : il nastro 1 viene usato per simulare $T_1(x)$ e il nastro 2 viene usato per simulare $T_2(x)$
- **Input di T** : una parola x scritta sul nastro 1
- Inizializzazione: T copia l'input x sul nastro 2, e poi inizia la computazione vera e propria:
	1) T simula un passo di $T_1(x)$: se quel passo fa accettare $T_1$ allora accetta, 										altrimenti va a 2)
	2) T simula un passo di $T_2(x)$: se quel passo fa accettare $T_2$ allora rigetta, 										altrimenti va a 1)
poiché x  L oppure x L , allora, prima o poi T1 accetta o T2 accetta: allora, T decide L.

Ma perché simuliamo un passo alla volta di ciascuna macchina?

Vediamo

Prendiamo la macchina $T_{PAL2}$, avente le seguenti quintuple, che accetta $L_{PPAL}^C$

- $\langle q_0,a,\square,q_a,D\rangle,\langle q_0,b,\square,q_b,D\rangle$
- $\langle q_a,a,a,q_a,D\rangle,\langle q_a,b,b,q_a,D\rangle,\langle q_b,a,a,q_b,D\rangle,\langle q_b,b,b,q_b,D\rangle$
- $\langle q_a,\square,\square,q_{a_1},S\rangle,\langle q_b,\square,\square,q_{b_1},S\rangle$
- $\langle q_{a_1},a,\square,q_2,S\rangle,\langle q_{a_1},b,b,q_R,F\rangle,\langle q_{b_1},a,a,q_R,F\rangle,\langle q_{b_1},b,\square,q_2,S\rangle$
- $\langle q_2,a,a,q_2,S\rangle,\langle q_2,b,b,q_2,S\rangle,\langle q_2,\square,\square,q_0,D\rangle$
- $\langle q_0,\square,\square,q_0,F\rangle$
- $\langle q_{a_1},\square,\square,q_A,F\rangle,\langle q_{b_1},\square,\square,q_A,F\rangle$

Ora, costruiamo la macchina $T_{PAL}'$ che ha due  nastri: dopo aver copiato l’input x (che inizialmente è scritto sul nastro 1) sul nastro 2, T usa il nastro 1 per simulare $T_{PAL1}(x)$ e il nastro 2 per simulare $T_{PAL2}(x)$ 

Costruiamo la macchina $T_{PAL}'$ che opera in due fasi:
- durante la prima fase simula l’intera computazione $T_{PAL1}(aba)$
- durante la seconda fase simula l’intera computazione $T_{PAL2}(aba)$

Bene. Ora eseguiamo la computazione $T_{PAL}'(bab)$ 

Si osservi che $aba\in L_{PPAL}^C$ : quindi, $T_{PAL}'(aba)$ dovrebbe rigettare

Ma aba è una parola palindroma di lunghezza dispari con ‘a’ al centro

E quindi, poiché $T_{PAL}'$ simula prima l’intera computazione $T_{PAL1}(bab)$, $T_{PAL}'$ non termina!

Ecco perché “un passo alla volta”!

## Funzioni calcolabili

Torniamo ai trasduttori

Ma che vuol dire calcolare il valore di una funzione?

Ad esempio: 
- f(n) = $n^2$ nel punto n = 5, vale 25 – ossia, f(5) = 25
- f(n) = $2^n$ nel punto n = 9 vale 512 - ossia, f(9)=512
- f(n) =  $\frac{1}{n-4}$ nel punto n = 4 vale … 

Intanto ci limitiamo a considerare funzioni "discrete" - ossia, dati due alfabeti finiti $\Sigma_1,\Sigma_2$, noi consideriamo solo funzioni del tipo $$f:\Sigma_1^\star\to\Sigma_2^\star$$
Poi, calcoleremo le funzioni solo dove sono definite

E infatti, parliamo di **funzioni** in generale (che possono non essere definite in alcuni punti) e di **funzioni totali** ( che sono definite per ogni $x\in\Sigma_1^\star$)

>[!definition]- Definizione (funzione calcolabile)
>Una funzione $f:\Sigma_1^\star\to\Sigma_2^\star$ è **calcolabile** se esite una macchina di Turing di tipo trasduttore tale che, per ogni $x\in\Sigma_1^\star$ tale che f(x) è definita, $T(x)=f(x)$
>Oppure
>f è **calcolabile** se $$\exists T : \forall x\in\Sigma_1^\star[T(x)=f(x)\iff\text{f è definita}]$$

Si osservi che questa definizione nulla ci dice circa le computazioni T(x) tali che f(x) non è definita
- in questo caso, T(x) potrebbe non terminare
- oppure terminare con un valore scritto sul nastro di output che non corrisponde al valore f(x): infatti, f(x) non esiste!

Perciò, a pensarci bene, il concetto di calcolabilità di una funzione è molto simile al concetto di accettabilità di un linguaggio

### Funzioni e linguaggi

Pensandoci bene, ad ogni linguaggio $L\subseteq\Sigma^\star$ possiamo associare una funzione - quella che si chiama _funzione caratteristica_ di un insieme: una funzione $\chi_L :\Sigma^\star\to\{0,1\}$ tale che, per ogni $x\in\Sigma^\star$, 
- $\chi_L(x)=1$ se $x\in L$,
- $\chi_L(x)=0$ se $x\not\in L$
Si osservi che, qualunque sia L,$\chi_L$ è una funzione **totale**

>[!definition]- Teorema 3.2
>$\chi_L$ è calcolabile se e solo se L è decidibile

La dimostrazione si trova sulle dispense

Ri-pensandoci bene, anche ad ogni funzione $f :\Sigma_1^\star\to\Sigma_2^\star$ possiamo associare un linguaggio $L_f\subseteq\Sigma_1^\star\times\Sigma_2^\star: L_f=\{(x,y)\in\Sigma_1^\star\times\Sigma_{2^\star}: y=f(x)\}$

TEOREMA 3.3: Se f è calcolabile e totale allora Lf è decidibile

>[!definition]- Teorema 3.1
>Se f è calcolabile e totale allora $L_f$ è decidibile

Dimostrazione:
- Idea della dimostrazione: sia $T_f$ è il trasduttore che calcola f
- Costruiamo il riconoscitore T per decidere $L_f$ : T ha tre nastri – sul primo nastro è scritto l’input x, sul secondo nastro è scritto l’input y, il terzo nastro è un nastro di lavoro
- T opera in due fasi:
	- FASE 1: T simula $T_f(x)$ scrivendo il risultato f(x) = z sul terzo nastro
	- FASE 2: T confronta z con y, accettando se sono uguali rigettando se sono diverse
La dimostrazione che T effettivamente decide $L_f$ è sulla dispensa

>[!definition]- Teorema 3.4
>Se $L_f$ è decidibile allora f è calcolabile

Dimostrazione:
- Costruiamo una macchina $T_f$ , con 4 nastri ed un nastro di output, che opera come segue 
	- inizialmente, l’input x è scritto sul primo nastro, e $T_f$ scrive 0 sul secondo nastro
	- $T_f$ scrive sul terzo nastro tutte le parole di lunghezza 0: ossia, la parola vuota - $\square$
	- $T_f$ simula la computazione $T_L(x,\square)$: se $T_L$ accetta, allora $T_f$ scrive $\square$ sul nastro di output, altrimenti (e, in questo caso $T_L$ rigetta) passa al successivo passo 1)
	- **PASSO 1)** $T_f$ incrementa di 1 il valore scritto sul secondo nastro
	- **PASSO 2)** $T_f$  scrive sul terzo nastro tutte le parole in $\Sigma_2^\star$ la cui lunghezza è il valore scritto sul secondo nastro: ad esempio, se sul secondo nastro è scritto 2 e $\Sigma_2=\{a,b\}$, allora $T_f$ scrive sul terzo nastro le parole aa, ab, ba, bb
	- **PASSO 3)** per ogni parola y scritta sul terzo nastro, $T_f$ simula la computazione $T_L (x, y)$: se $T_L$ accetta, allora $T_f$ scrive sul y nastro di output e termina, altrimenti (e, in questo caso $T_L$ rigetta) 
		- se non ha ancora esaminato tutte le parole scritte sul terzo nastro, passa alla parola successiva 
		- altrimenti, se ha esaminato tutte le parole scritte sul secondo nastro e nessuna ha indotto $T_L$ ad accettare, torna al PASSO 1)  

Si osservino che i passi 1), 2) e 3) terminano sempre.

Perciò, se f è definita in $x_0$, allora, 
- detto $n_0$ il numero di caratteri di $f(x_0)$, 
- quando sul secondo nastro verrà scritto $n_0$, sul terzo nastro verranno scritte tutte le parole di $n_0$ caratteri e fra esse anche la parola $f(x_0)$ (chiamiamola $y_0$) 
- allora, poiché tutte le computazioni $T_L (x_0, y)$ terminano, prima o poi verrà anche eseguita la computazione $T_L (x_0, y_0)$ che terminerà in $q_A$: così, $y_0$ verrà scritto sul nastro di output di $T_f$ e la computazione $T_f (x_0)$ terminerà

Questo dimostra che “se f è definita in $x_0$, allora $T_f (x_0)$ calcola $f(x_0)$”

Quindi, f è calcolabile.

Ma, se f non è definita in $x_0$, allora **non verrà mai trovata una parola $y_0$ tale che $T_L (x_0, y_0)$ accetta** – perché $T_L$ decide $L_f=\{(x,y)\in\Sigma_1^\star\times\Sigma_{2^\star}: y=f(x)\}$

E quindi, anche se $L_f$ è decidibile, non è detto che f sia totale.