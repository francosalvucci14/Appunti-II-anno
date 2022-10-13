# Introduzione

## Induzione matematica semplice

Data una proposizione $P(n)$ definita per un generico numero naturale n, si a che essa è vera per tutti i num naturali se:
- P(0) è vera (**passo base** dell'induzione)
- $\forall$ naturale k, $P(k)$ vera (ipotesi induttiva) implica $P(k+1)$ vera (**passo induttivo**) 

$$(P(0)\wedge\forall k' (P(k')\implies P(k'+1)))\implies \forall\: nP(n)$$
**Esempio**
dimostrare che $\sum_{i=0}^n i=\frac{n(n+1)}{2}$ (questa è $P(n)$)
- Passo base : $\sum_{i=0}^0 i = \frac{0(0+1)}{2} = 0$ 
- Passo induttivo:$$\sum_{i=0}^{k+1}i=\sum_{i=0}^k i+(k+1)=\frac{k(k+1)}{2}+(k+1)=\frac{k^2+3k+2}{2}=\frac{(k+1)(k+2)}{2}$$
> Sostanzialmente dobbiamo verificare che se vale $\sum_{i=0}^k i= \frac{k(k+1)}{2} \implies$ vale $\sum_{i=0}^{k+1} i = \frac{(k+1)(k+2)}{2}$ 

Chiaramente questo è verificato e vale $\forall k$ 

**Esempio**

Dimostrare che $\sum_{i=0}^{n-1}2^i=2^n-1\: per\: n\geq1$
- Passo base(n=1): $\sum_{i=0}^02^i=2^0-1=0$
- Passo Induttivo:$$\sum_{i=0}^{k-1}2^i=2^k-1\implies \sum_{i=0}^{k}2^i=2^{k+1}-1$$
$$\sum_{i=0}^k 2^i=\sum_{i=0}^{k-1}2^i+2^k=2^k-1+2^k=2\cdot2^k-1=2^{k+1}-1$$


## Induzione completa
data una proposizione $P(n)$ definita per un generico numero naturale $n\geq n_0$ si ha che essa è vera per tutti gli $n\geq n_0$ se:
- $P(n_0)$ è vera (passo base dell'induzione)
- per ogni naturale $k\geq n_0,P(i)$ è vera per ogni $i,n_0\leq i\leq k$ (ipotesi induttiva) implica $P(k+1)$ vera (passo induttivo)
$$(P(0)\wedge \forall k'(P(0)\wedge...\wedge P(k')\implies P(k'+1)))\implies \forall\:nP(n)$$
## Insiemi Infiniti

Due insiemi A e B si dicono **equinumerosi** se esiste una biezione tra di essi
Dato un insieme finito A, la sua cardinalità |A| è definita come :
$$|A|=\begin{cases}0 & se\: A=\emptyset\\
n & se\: è\: equinumeroso\:a\: (0,1,...,n-1),con\: n\geq1\end{cases}$$
- Un insieme di dice numerabile se esso è **equinumeroso** a $\mathbb N$ 
- Un insieme si dice **contabile** se esso è finito o numerabile
- Per indicare la cardinalità degli insiemi infiniti equinumerosi ad $\mathbb N$ si utilizza il simbolo $\aleph_0$ 
- Se un insieme A è equinumeroso a un insieme B, con $B \subseteq C$, dove C è un insieme contabile, allora anche A è contabile