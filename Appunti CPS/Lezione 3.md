# Indipendenza tra più eventi

_Def_
Sia {$A_i$}$_{i\ni I}$ una famiglia di eventi.
Allora si ha una famiglia di eventi indipendenti se:
- la famiglia è finita quindi $\forall$ sottoinsieme di alemeno due insiemi ($A_{i_1},...,A_{i_k}$)  con $k\geq2$ si ha$$P(A_{i_1}\cap...\cap A_{i_k}) = P(A_{i_1})\cdot...\cdot P(A_{i_k})$$
- se la famiglia è infinita, ogni sottoinsieme finito lo è in accordo con quanto detto sopra

**Esempio**
Consideriamo tre eventi {$A_1,A_2,A_3$}. Allora c'è indipendenza se:
$$\begin{cases}P(A_1\cap A_2)=P(A_1)P(A_2)\\
P(A_1\cap A_3)=P(A_1)P(A_3)\\
P(A_2\cap A_3)=P(A_2)P(A_3)\end{cases}\:\: e\: P(A_1\cap A_2\cap A_3) = P(A_1)P(A_2)P(A_3)$$

Consideriamo la seguente situazione : Un'urna ha 4 carte numerate come segue (1,2,3,123) e si estrae una carta a caso
Consideriamo l'evento $A_i$={la carta estratta ha il numero i} i=1,2,3

Allora
$P(A_1) = P(A_2) = P(A_3) = \frac {2}{4}=\frac {1}{2}$
$P(A_1\cap A_2) = P(A_1\cap A_3) = P(A_2\cap A_3) = \frac {1}{4}$
$P(A_1\cap A_2\cap A_3)=\frac {1}{4}$

