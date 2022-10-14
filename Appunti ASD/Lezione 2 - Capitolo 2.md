# Complessità computazionale e notazioni asintotiche

## Un modello di calcolo storico: la macchina di Turing

![[appunti asd/immagini/Pasted image 20221014151459.png]]

- Troppo di basso livello: somiglia troppo poco ai calcolatori reali su cui girano i programmi
- Utile per parlare di calcolabilità ma meno utile per parlare di efficenza

Un modello più realistico...
- Macchina a registri (**RAM**: random access machine)
	- un programma finito
	- un nastro in ingresso e uno di uscita
	- una memoria strutturata come un array
		- ogni cella può contenere un qualunque valore reale/intero
	- due registri speciali: PC e ACC
- la RAM è unìastrazione dell'architettura di von Neumann

![[appunti asd/immagini/Pasted image 20221014152028.png]]

## Modello di calcolo: cosa posso fare
- L'analisi della complessità di un algoritmo è basata sul concetto di **passo elementare**
- passi elementari su una RAM:
	- istruzioni ingresso/uscita
	- operazione aritmetico/logica
	- accesso/modifica del contenuto della memoria
## Criterio di costo: quanto mi costa
### Criterio di costo uniforme:
- tutte le operazioni hanno lo stesso costo 
- complessità temporale misurata come **numero di passi elementari eseguiti**
### Criterio di costo logaritmico
- Il costo di una operazione dipende dalla dimensione degli operandi dell'istruzione
- Un'operazione su un operando di valore x ha costo log(x)
- è un criterio di costo che modella meglio la complessità di **algoritmi "numerici"**

**Oss** il criterio di costo generalmente usato è quello UNIFORME

## Caso peggiore e caso medio

Misureremo il tempo di esecuzione di un algoritmo in funzione della dimensione n delle istanze
Istanze diverse, a **parità di dimensione**, potrebbero però richiedere **tempo diverso**
Distinguiamo quindi ulteriormente tra analisi nel caso **peggiore** e **medio**

### Caso peggiore
Sia **tempo(I)** il tempo di esecuzione di un algoritmo sull'istanza I
$$T_{worst}(n)=max_{\text{istanze I di dimensione n}}(tempo(I))$$
Intuitivamente, $T_{worst}(n)$ è il tempo di esecuzione sulle istanze di ingresso che comportano più lavoro sull'algoritmo
Rappresenta una garanzia sul tempo di esecuzione di ogni istanza
### Caso medio
Sia P(I) la probabilità di occorrenza dell'istanza I
$$T_{avg}(n)=\sum_{\text{istanze I di dimensione n}}(P(I)\cdot tempo(I))$$
Intuitivamente, $T_{avg}(n)$ è il tempo di esecuzione nel caso medio, ovvero sulle istanze di ingresso "tipiche" per il problema
Come faccio a conoscere la distribuizione di probabilità sulle istanze?
- Semplice:(di solito) non posso conoscerla
	- faccio un'assunzione
	- spesso è difficile fare assunzioni realistiche

## Notazione asintotica: intuizioni

La complessità computazionale di un algoritmo viene espressa con una funzione T(n)

_Def_
T(n):# passi elementari eseguiti su una RAM nel caso peggiore di un'istanza di dimensione n

**Idea**: descrivere T(n) in modo **qualitativo**. Ovvero: perdere un pò in **precisione** (senza perdere l'essenziale) e guadagnare in **semplicità**

**Esempio**
$$T(n)=\begin{cases}71n^2+100(n/4)+7 & n\:è\:pari\\
70n^2+150(n+1)/4+5 & n\:è\:dispari\end{cases}$$
Scriveremo $T(n)=\Theta(n^2)$
intuitivamente vuol dire: T(n) è proporzionale a $n^2$
cioè ignoro:
- costanti moltiplicative
- termini di ordine inferiore

### Notazione asintotica O
$f(n)=\mathcal{O}g(n)$se$\exists$ c>0, $n_0\geq0$ tali che $0\leq f(n)\leq c\cdot g(n)\:\:\forall\: n\geq n_0$    

![[appunti asd/immagini/Pasted image 20221014155959.png|center]]
**Esempi**

Sia $f(n)=2n^2+3n$, allora:
- $f(n)=O(n^3)$
- $f(n)=O(n^2)$
- $f(n)\neq O(n)$

In generale
$$f(n)=O(g(n))\implies lim_{n\to\infty}{\frac{f(n)}{g(n)}}\lt\infty$$
### Notazione asintotica $\Omega$

$f(n)=\Omega(g(n))$ se $\exists\:c\gt0, n_0\geq0|f(n)\geq c\cdot g(n)\geq0$ 

![[appunti asd/immagini/Pasted image 20221014160550.png]]

**Esempi**

Sia $f(n)=2n^2-3n$ allora:
- $f(n)=\Omega(n)$
- $f(n)=\Omega(n^2)$
- $f(n)\neq\Omega(n^3)$

In generale
$$f(n)=\Omega(g(n))\implies lim_{n\to\infty}\frac{f(n)}{g(n)}\gt0$$
