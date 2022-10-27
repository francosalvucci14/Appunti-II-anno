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
$P(\lbrace\omega\in\Omega:X(\omega)\in B\rbrace)$ useremo la notazione $P(\lbrace X\in B\rbrace)$, o anche $P(X\in B)$

## Distribuzione o Legge di una v.a reale
è la corrispondente tra "gli insiemi della retta B per cui $\lbrace X\in B\rbrace\in A$" e i valori $P(\lbrace X\in B\rbrace)$ relativi

## Funzione di distribuzione di una v.a reale
è la funzione $F_x:\mathbb R\to [0,1]$ così definita: $F_x(t)=P(X\leq t)$

### Commento
La conoscenza di $F_x$ consete di individuare la distribuzione di una v.a. X
Quindi, se uno conosce i valori di $P(X\in B)$ per $B=(-\infty,t]$ (al variare di tutti i valori $t\in\mathbb R$), è possibile conosceere tutti i valori di $P(X\in B)$ al variare di $B\subset\mathbb R$

## Proprietà della funzione di distribuzione $F_x$
1. $F_x$ non è decrescente, cioè $F_x(t_1)\leq F_x(t_2)$ $\forall t_1,t_2\in\mathbb R|t_1\leq t_2$. Questo si verifica facilemente osservando che $$t_1\leq t_2\implies (-\infty,t_1]\subset(-\infty,t_2]\implies P(X\leq t_1)\leq P(X\leq t_2)\implies F_x(t_1)\leq F_x(t_2)$$
2. $lim_{t\to-\infty} F_x(t)=0$ e $lim_{t\to\infty} F_x(t)=1$
3. $F_x$ è continua a destra, cioè $\forall t_0\in\mathbb R F_x(t)=F_x(t_0)$

![[appunti cps/immagini/Pasted image 20221027135649.png|center|600]]

## Variabili aleatorie discrete




 
