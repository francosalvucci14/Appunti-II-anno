
# Problemi e codifiche

## Dai linguaggi ai problemi

Le teorie della calcolabiltà e della complessità sono fondate sul concetto di appartenenza di una parola ad un insieme di parole: un concetto
- semplice
- elegante
- formale
- rigoroso

Tuttavia, nella vita reale, non ti capita spesso di domandarti “ma questa parola apparterrà forse a questo insieme?”

Nella vita reale, piuttosto, ti capita di dover trovare le soluzioni ad istanze di problemi

E, allora, queste teorie sarebbe bello trasferirle nel mondo dei problemi
Ma il concetto “**trovare la soluzione ad una istanza di un problema**” è, senza dubbio, più arbitrario
- se vogliamo, più evanescente
meno rigoroso di quello di appartenenza di una parola ad un insieme di parole

### Formalizzare i problemi

**ESEMPIO: dato un numero intero… (segue richesta relativa ai divisori del numero)**

Di qualunque problema stiamo parlando, la struttura di un problema è sostanzialmente la seguente
- **dati un insieme di oggetti conosciuti** – l’insieme dei dati che costituisce una istanza      del problema
- **all’interno di un secondo insieme di oggetti** – l’insieme delle soluzioni possibili
- **cercare gli oggetti che soddisfino certi vincoli**  e, **sulla base degli oggetti trovati, fornire un qualche tipo di risposta**

**Dati un insieme di oggetti conosciuti**: dobbiamo descrivere le istanze del problema, ossia in cosa consiste ciascuna istanza del problema

Descriviamo le istanze del problema definendo un insieme $\mathcal I$ - l’**insieme delle istanze**
- un elemento di $\mathcal I$ corrisponde ad una istanza del problema
- nell’ESEMPIO: $\mathcal I =\mathbb N$

**All’interno di un secondo insieme di oggetti** – l’insieme delle soluzioni possibili: dobbiamo descrivere cosa ci viene richiesto di cercare

Descriviamo le soluzioni possibili per una istanza x del problema definendo un insieme S(x)
$S(x)$
- $S(x)$ descrive tutti gli oggetti che dobbiamo testare per verificare se soddisfano i vincoli del problema
- nell’ESEMPIO: $S(x) =  \{y\in\mathbb N  : y\leq  x \}$

**Cercare gli oggetti che soddisfino certi “vincoli”**: dobbiamo descrivere quali oggetti, all’interno delle soluzioni possibili, soddisfano la richiesta del problema 

Descriviamo le soluzioni possibili associate ad una istanza x che soddisfano i vincoli del problema definendo un insieme $\eta(S(x))$ di soluzioni effettive per l’istanza x
- $\eta(S(x))$ è l’insieme che contiene tutti gli oggetti che sono soluzioni possibili per x e che soddisfano i vincoli del problema
- nell’ESEMPIO: poiché il problema si pone qualche domanda circa i divisori di un dato numero x,$\eta(S(x)) = \{ y\in  S(x): \text{y è un divisore di x} \}$

**Sulla base degli oggetti trovati, fornire un qualche tipo di risposta** : dipendentemente dalla domanda posta dal problema, dobbiamo rispondere fornendo quanto ci viene richiesto

Descriviamo la risposta al problema definendo una funzione $\rho$ che associa all’insieme delle soluzioni effettive per l’istanza x una risposta scelta nell’insieme _R_ delle risposte

E, per chiarire questa questione, dobbiamo entrare nel dettaglio di (segue richiesta relativa ai divisori del numero)

In questo caso, $R = 2^{\mathbb N}$ 
- ossia, la risposta ad una istanza del problema è un sottoinsieme di 
e, per ogni istanza n del problema, $\rho(\eta(S(n))) = \eta(S(n))$

Ci sono altri esempi, ovvero Esempio 2,3,4
Vedi sulla dispensa (non ho voglia di scriverli 😄 )

#### Tipi di problemi

ESEMPIO 4: dato un numero intero n, calcolare il più grande divisore non banale d di n  (ossia, $d \gt 1$  e $d \lt n$)
- è un _**problema di ottimizzazione**_, in quanto alle soluzioni effettive è associata una misura e viene richiesto di trovare una soluzione effettiva di misura massima (come in questo caso), oppure minima 
ESEMPIO 3: dato un numero intero n, calcolare un divisore non banale d di n  (ossia, $d \gt 1$  e $d \lt n$)
- è un _**problema di ricerca**_, in quanto viene richiesto di trovare (e mostrare) una qualunque soluzione effettiva
- sono i problemi con i quali abbiamo maggiore confidenza
ESEMPIO 1: dato un numero intero n, elencare tutti i divisori di n 
- è un _**problema di enumerazione**_, in quanto ci viene richiesto di elencare tutte le soluzioni effettive
ESEMPIO 2: dato un numero intero n, verificare se n è primo
- è un _**problema di decisione (o decisionale)**_, in quanto ci viene richiesto di decidere se l’istanza possiede una certa proprietà

Naturalmente, i due diversi tipi di macchine di Turing risolvono diversi tipi di problemi
- Trasduttori per i problemi di ricerca, di enumerazione, e di ottimizzazione 
- Riconoscitori per i problemi di decisione
La Teoria della Complessità si occupa, per lo più, di decidere dell’appartenenza di parole ad insiemi di parole utilizzando riconoscitori

Sembra naturale estendere quanto studiato nella dispensa 6 ai problemi decisionali

### Problemi decisionali

Abbiamo visto che un problema, in generale, può essere descritto da una quintupla $\langle \mathcal I, S,\eta ,\rho , R \rangle$ , dove
 - $\eta$ è il sottoinsieme di S che specifica quali, fra le soluzioni possibili, sono le soluzioni effettive per una data istanza $x\in\mathcal I$
- $\rho$ è la funzione che associa all’insieme delle soluzioni effettive $\eta(S(x))$ una risposta (elemento di R) all’istanza x del problema

Nel caso di problemi decisionali, sappiamo che $R = \{ vero, falso\}$
Questo significa che, in effetti, $\rho$ **è un predicato**
- ossia, una funzione booleana
- o, per dirla semplice, una proposizione logica il cui valore di verità dipende da qualche incognita

Allora, possiamo riassumere $\eta,\rho , R$ in un unico predicato $\pi: \pi(x,S(x))$=**vero se e soltanto se l’insieme delle soluzioni possibili per x soddisfa i vincoli del problema**

E, quindi, un problema decisionale è descritto da una tripla $\langle \mathcal I, S,\pi \rangle$

#### Esempi

Un problema decisionale è descritto da una tripla $\langle \mathcal I, S,\pi \rangle$ 

**Esempio 1**: dati un grafo non orientato G, una coppia di nodi s e t, e un intero k, decidere se esiste in G un percorso da s a t di lunghezza  k

- $\mathcal I= \{\langle G, s, t, k \rangle : \text{G è un grafo non orientato}\land\text{s,t sono due nodi di G}\land  k\in\mathbb N   \}$
- $S(G, s, t, k) = \{ \langle u_0, u_1, \dots , u_k \rangle : \forall i=0,\dots ,k, u_i\text{ è un nodo del grafo} \}$
- $\begin{align}&\pi(G, s, t, k, S(G, s, t, k) )=  \exists \langle u_0, u_1, \dots , u_k \rangle\in  S(G, s, t, k) : s=u_0, t=u_{k}\\&\land \forall i=0, \dots ,k-1, [ (u_i , u_{i+1})\text{ è un arco del grafo} ]\end{align}$

Esempio 2: dato un insieme X di variabili booleane ed un predicato f, definito sulle variabili in X e contenente i soli operatori $\land,\lor, \lnot$, decidere se esiste una assegnazione a di valori in {vero, falso} alle variabili in X tali che $f(a(X))$=vero

- $\mathcal I= \{ \langle X,f \rangle : \text{X è un insieme di variabili booleane}\land \text{ f e un predicato su X}\}$
- $S(X,f) = \{ a: X\to  \{vero, falso\} \}$ (S è l’insieme delle assegnazioni di verità alle variabili in X)
- $\pi(X,f, S(X,f) )= \exists a\in S(X,f) : f(a(X)) = vero$

**Nota bene**: ciascun problema decisionale può essere descritto da diverse triple $\langle \mathcal I, S,\pi \rangle$

## Da problema a linguaggio

A questo punto, formalizzato il concetto di problema decisionale.

Siamo quasi pronti ad estendere quanto abbiamo studiato sulla complessità dei linguaggi alla complessità dei problemi decisionali

E, visto che la complessità dei linguaggi è studiata utilizzando la Macchina di Turing, utilizzeremo la Macchina di Turing anche per studiare la complessità dei problemi decisionali

Ma per utilizzare una macchina di Turing per risolvere un problema decisionale abbiamo bisogno di trasformare le **istanze** di quel problema in **parole**

Ossia, occorre _**codificare**_ opportunamente le istanze di un problema decisionale

### Codifica

Nel paragrafo 7.4 viene introdotta la questione delle codifiche attraverso un esempio: l’ Esempio 2 che abbiamo visto poc’anzi

Di questo problema viene considerato un caso particolare: 3SAT
- la funzione f è in una forma particolare: $f = c_1\land c_2 \land\dots\land cm$
- e ciascuna $c_j$ prende il nome di clausola ed è l’or ( $\lor$ ) di tre letterali
- dove un letterale è una variabile o una variabile negata – tipo $x_1\lor\neg  x_2\lor x_3$

Come codificare gli elementi di $\mathcal I$?
Abbiamo due possibilità:
1) codifichiamo la struttura di f
2) codifichiamo “il significato” di f

**CODIFICA** $\chi_1$ : codifichiamo la struttura di f
- rappresentiamo ciascun elemento di $X = \{x_1 , x_2,\dots , x_n\}$ con $n=|X|$ bit: $x_i$ ha l’i-esimo bit 1 e tutti gli altri bit 0
- rappresentiamo un letterale in una clausola mediante la rappresentazione della variabile corrispondente al letterale preceduta da 0 se il letterale è la variabile non negata, preceduta da 1 se se il letterale è la variabile negata
- gli $\lor$ in una clausola sono rappresentati da ’2’
- gli $\land$ fra due clausole sono rappresentati da ‘3’
- premettiamo alla codifica di f tanti ‘4’ quanti gli elementi di X – ossia, $|X| = ’4’$

Ad esempio, se $X = \{x_1, x_2, x_3\}$ e $f = c_1\land c_2$ con $c_1= x_1\lor  x_2\lor  x_3$ e $c_2 = x_1\lor\neg  x_2\lor\neg  x_3$ rappresentiamo $\langle X,f \rangle$  come :
444 0 100 2 0 010 2 0 001 3 0 100 2 1 010 2 1 001

**CODIFICA** $\chi_2$ : codifichiamo “il significato” di f – codifichiamo f in **forma esplicita**
- qualunque funzione è completamente descritta descrivendo i valori che essa assume in **tutti** i punti del suo insieme di esistenza
- naturalmente, se una funzione è definita su non possiamo descrivere il valore che essa assume per ogni $n\in\mathbb N$ : in numeri naturali sono infiniti!
- invece, la f della nostra istanza $\langle X,f \rangle$ di 3SAT è definita su $\{vero, falso\}^{|X|}$ 
- quindi, poiché X è un insieme finito, l’insieme di esistenza di f è finito
- allora, possiamo codificare f in forma esplicita mediante la sua **tavola di verità**

esempio: se $X = \{x_1, x_2, x_3\}$ e $f = c_1\land c_2$ con $c_1= x_1\lor  x_2\lor  x_3$ e $c_2 = x_1\lor\neg  x_2\lor\neg  x_3$

![[appunti fi/mod ii/immagini/Pasted image 20230524145558.png|center|300]]

Codificando: vero con ‘1’ e falso con ‘0’, e scrivendo le righe della tavola una di seguito all’altra, separate da ‘2’, otteniamo: 1111 2 1101 2 1011 2 1001 2 0110 2 0101 2 0011 2 0000 2

### Codifica e soluzione

SOLUZIONE: data $\langle X,f \rangle$ istanza di 3SAT, per decidere se f è **soddisfacibile**, consideriamo il seguente algoritmo: 
1) calcola $n = |X|$; 
2) per ogni assegnazione di verità a all’insieme delle n variabili in X : verifica se   		      $f (a(X )) =$ vero e, in tal caso termina nello stato di accettazione $q_A$; 
3) se non ha mai terminato in $q_A$ al passo 2, termina nello stato di rigetto $q_R$. 

Vediamo ora il precedente algoritmo implementato utilizzando entrambe le codifiche. 

Se $\langle X,f \rangle$ è codificata secondo la CODIFICA $\chi_1$ : 

- Utilizziamo una macchina di Turing $T_1$ a due nastri e che opera in due fasi:
- All’inizio della computazione, $\chi_1(X,f)$ è scritta sul primo nastro, il secondo nastro è vuoto
	- Fase 1: utilizzando i ‘4’ iniziali della codifica di $\langle X,f \rangle$, scrive sul secondo nastro tutte le parole binarie di lunghezza |X|, separate le une dalle altre da un ‘5’: ciascuna parola binaria corrisponde ad una assegnazione di verità agli elementi di X
	- Fase 2: per ogni assegnazione di verità a scritta sul secondo nastro, utilizzando la codifica di f scritta sul primo nastro, verifica se a soddisfa f: se ciò accade, accetta e termina
- se ha terminato la fase 2 senza accettare, rigetta

Bene, ma quanto è $dtime (T_1, \chi_1(X,f))$?
- Fase 1: se $n = |X|$ , la fase 1 richiede almeno $2^n$ passi, tante sono le assegnazioni possibili
- $|\chi_1(X,f)| \lt n + [3(n+1) +3] (2n)^3  \lt  n^4 +7n (8n^3)  \lt    57  n^4$

E, quindi, $dtime (T_1, \chi_1(X,f)) \gt 2^n \gt 2^{\frac{\sqrt[4]{|\chi_1(X,f)|}}{57}}$

Se $\langle X,f \rangle$ è codificata secondo la CODIFICA $\chi_2$ : 

- esempio: 1111 2 1101 2 1011 2 1001 2 0110 2 0101 2 0011 2 0000 2
- Utilizziamo una macchina di Turing $T_2$ ad un solo nastro:
- all’inizio della computazione, $\chi_2 (X,f)$ è scritta sul nastro
	- $T_2$ scandisce l’input: poiché il carattere (‘0’ o ‘1’) a sinistra di un ‘2’ è il valore assunto da f quando alle sue variabili sono assegnati i valori a sinistra di quel carattere, se trova un ‘1’ a sinistra di un ‘2’ allora accetta e termina
	- poiché $\chi_2 (X,f)$ contiene in sé tutte le possibili assegnazioni di verità alle variabili in f, se $T_2$ ha terminato scansione dell’input senza accettare, rigetta

Bene, ma quanto è $dtime (T_2, \chi_2 (X,f))$?
Questa volta è facilissimo: $T_2$ deve solo scandire una volta l’input
E, quindi, $dtime (T_2, \chi_2 (X,f)) = |\chi_2 (X,f)|$

