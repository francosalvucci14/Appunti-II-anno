# Capitolo 3 - Modeli discreti
## Modelli Discreti
In questo capitolo tratteremo essenzialmente **VARIABILI ALEATORIE DISCRETE**(spesso definite su spazi di prob. $(\Omega,\mathcal A,\mathcal P)$ con $\Omega$ discreto)

_Def_
In generale una variabile aleatoria è una funzione del tipo $$X:\Omega\rightarrow\mathcal X$$
Dove $\mathcal X$ è un qualunque insieme, con certe proprietà
In questo corso tratteremo il caso in cui $\mathcal X=\mathbb R$(o un suo sottinsieme)
Il concetto di v.a è utile perchè spesso gli eventi di interesse negli esercizi sono esprimibili tramite v.a
**Esempio**
Si lanciano due dadi e consideriamo l'evento "la somma dei due numeri ottenuti è uguale a 5"
Allora è utile fare riferimento alla seguente scelta dell'insieme $\Omega$:
>$\Omega=\lbrace 1,...,6\rbrace x\lbrace 1,...,6\rbrace=\lbrace w=(w_1,w_2):w_1,w_2\in\lbrace 1,...,6\rbrace\rbrace$

Essendo $\Omega$ un insieme finito, non ci sono problemi nello scegliere $\mathcal A=\mathcal P(\Omega)$ 
Inoltre è opportuno considerare la seguente funzione $X:\Omega\rightarrow\mathbb R$
definita come segue:
$$X(w)=X(w_1,w_2)=w_1+w_2 \:\forall w=(w_1,w_2)\in\Omega$$
Allora l'evento di interesse è:
>$w=(w_1,w_2)\in\Omega:X(w)=5$

_Def_
Sia ($\Omega,\mathcal A,\mathcal P$) uno spazio di prob. Inoltre sia $X:\Omega\rightarrow\mathbb R$ una funzione.
Allora la funzione X è una v.a (_reale_) se vale la seguente condizione
$$\forall t\in\mathbb R\:\:\lbrace w\in\Omega:X(w)\leq t\rbrace\in \mathcal A$$
In altri termini si richiede che le controimmagini delle semirette del tipo $(-\infty,t]$, che sono sottoinsiemi di $\Omega$, sono elementi della $\sigma-algebra\:\mathcal A$ 
Questo consente di dire che, per queste controimmagini, è possibile definire la prob.
Quindi possiamo dire che, per ogni $t\in\mathbb R$, $P(\lbrace w\in\Omega:X(w)\leq t\rbrace)$ è un numero ben definito
Quindi si richiede che, se $B=(-\infty,t]$ per qualsiasi scelta di $t\in\mathbb R$,
$\lbrace w\in\Omega:X(w)\in B\rbrace\in\mathcal A\:\:(\star)$

A partire da questa richiesta, la condizione $(\star)$ vale anche per le altre scelte di B "naturali" da considerare:
$$\begin{cases}B=[t,\infty)\\B=(t,\infty) & \forall t\in\mathbb R\\B=(-\infty,t)\end{cases}$$
B unione finita o numeraabile di insiemi dei tipi indicati sopra
(Es: $B=(0,1)\cup \lbrace 2\rbrace\cup [4,5)\cup [6,\infty)$)

## Notazioni che useremo
$\lbrace w\in\Omega:X(w)\in B\rbrace\text{useremo la notazione}\implies \lbrace X\in B\rbrace$ 
$$

