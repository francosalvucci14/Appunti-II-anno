
# Teorema di Cantor

>$\not\exists$ una funzione biunivoca tra $\mathbb N$ e $\mathcal P(\mathbb N)$

**Dimostrazione**

Supponiamo per assurdo che $\exists f:\mathbb N\to\mathcal P(\mathbb N)$ biunivoca
Definiamo un insieme $C$ in questo modo:
$$C\coloneqq\{i\in\mathbb N:i\not\in A_i\}\subseteq\mathbb N$$
Deve valere $C=A_k,\forall k\in \mathbb N$

A questo punto abbiamo 2 opzioni:

1. se $k\in C\implies k\in A_k\implies k\not\in C$ (assurdo)
2. se $k\not\in C\implies k\not\in A_k\implies k\in C$ (assurdo)

**Contraddizione**

Abbiamo trovato un'affermazione $P=k\in C$ tale che : 
ne "P" è vera, ne $\overline{P}$ è vera

Questo si chiama _**Principio del terzo escluso**_ oppure _**Principio di non contraddizione**_

**Esempio (Principio di non contraddizione)** "Io sto mentendo", la frase non è ne vera ne falsa

# Paradosso di Russell

Chiamiamo "ordinario" un insieme $S$ tale che $S\not\in S$
Chiamiamo "straordinario" un insieme $S$ tale che $S\in S$
Prendiamo $C\coloneqq\{\text{insiemi "ordinari"}\}$ 

$C$ è "ordinario" o "straordinario"?

Vediamo:

1. Se $C$ è "ordinario" $\implies C\in C\implies$ $C$ è "straordinario" 
2. Se $C$ è "straordinario" $\implies C\not\in C\implies$ $C$ è "ordinario"
(paradosso)

# Assioma di astrazione (o Principio di astrazione)

Data una proprietà $P$ esiste l'insieme di tutti gli elementi che hanno la proprietà $P$
$S=\{x.P(x)\}$

# Principio di astrazione limitato

Data una proprietà $P$ e un insieme $S$, allora esiste un'insieme di tutti gli elementi di $S$ che hanno la proprietà $P$

# Dimostrazioni per induzione

$9^n+3$ è divisibile per 4, $\forall n\in\mathbb N$?

Chiamiamo con $P(n)$ l'affermazione $P(n)=9^n+3\text{ è divisibile per 4}$

1. Dobbiamo verificare che $P(0)$ sia vera
2. Dimostrare che , dato $k\in\mathbb N$ qualsiasi, se è vero $P(k)\implies$ sarà vero $P(k+1)$ (passo induttivo)

**Base** : $(n=0)\implies 9^0+3=1+3=4$ OK
**Induttivo** $(n\geq1):\exists k\in\mathbb N,k\geq1 : P(k)=9^k+3\text{ è div. per 4},P(k+1)=9^{k+1}+3\text{ è div. per 4}$

Quindi :
$$9^{k+1}+3=9\cdot 9^k+3=(8+1)9^k+3=\underbrace{8\cdot 9^k}_{\text{div. per 4 perchè 8 è div. è per 4}}+\underbrace{9^k+3}_{\text{ipotesi induttiva}}$$
La somma di due numeri divisibili per 4 è ancora divisibile per 4






