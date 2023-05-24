
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

## Formalizzare i problemi

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

### Tipi di problemi

ESEMPIO 4: dato un numero intero n, calcolare il più grande divisore non banale d di n  (ossia, $d \gt 1$  e $d \lt n$)
- è un _**problema di ottimizzazione**_, in quanto alle soluzioni effettive è associata una misura e viene richiesto di trovare una soluzione effettiva di misura massima (come in questo caso), oppure minima 
ESEMPIO 3: dato un numero intero n, calcolare un divisore non banale d di n  (ossia, $d \gt 1$  e $d \lt n$)
- è un _**problema di ricerca**_, in quanto viene richiesto di trovare (e mostrare) una qualunque soluzione effettiva
- sono i problemi con i quali abbiamo maggiore confidenza
ESEMPIO 1: dato un numero intero n, elencare tutti i divisori di n 
- è un _**problema di enumerazione**_, in quanto ci viene richiesto di elencare tutte le soluzioni effettive
ESEMPIO 2: dato un numero intero n, verificare se n è primo
- è un _**problema di decisione (o decisionale)**_, in quanto ci viene richiesto di decidere se l’istanza possiede una certa proprietà


