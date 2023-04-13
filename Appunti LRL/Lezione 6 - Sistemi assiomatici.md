
# Sistemi assiomatici

Una sistema formale consiste in _schemi di assiomi e regole di inferenza_, oltre che dell’in-  
sieme dei simboli che vengono usati e delle definizioni che stabiliscono quali sequenze di  
simboli sono “formula”. 
Nel caso della logica proposizionale gli schemi di assiomi sono un insieme di formule ben formate e le regole di inferenza sono relazioni di formule di questo tipo: 
“Dalle formule $X_1, \dots , X_n$ segue la formula $Y$ ”. 
Vediamo subito un esempio.  
Consideriamo i due assiomi seguenti : 
$$\begin{align}&A_{1} : X\to(Y\to X)\\&A_{2}: (X\to(Y\to Z))\to((X\to Y)\to(X\to Z))\end{align}$$

La regola di inferenza che usiamo si chiama _Modus Ponens_: “Dalle formule $X$ e $X \to Y$ segue la formula Y ”. 
In simboli la scriviamo così  
![[appunti lrl/immagini/Pasted image 20230413114633.png|center|100]]

In questi episodio chiamerò $S_0$ il sistema assiomatico costituito dagli assiomi in $A_1$ e $A_2$ e dalla regola di inferenza Modus Ponens.

Diciamo che una formula $\mathcal F$ è un’istanza di un assioma, se si ottiene da uno schema di assioma, sostituendo ad ogni lettera dello schema una formula. 
Per esempio, la formula $(q \to r) \to (p \to (q \to r))$ è un’istanza dell’assioma $A_1$, perchè si ottiene da $A_1$ sostituendo$(q \to r)$ alla lettera $X$ e p alla lettera $Y$ .

## Teoremi e dimostrazioni

Abbiamo iniziato questo corso ponendoci la domanda “Cos'è una dimostrazione?”. 
Nell’ambito di un sistema assiomatico, possiamo darne una definizione precisa.  

>[!definition]- Definizione 2.1 (Dimostrazione)
>In un sistema assiomatico S, una dimostrazione è una sequenza di formule $F_1, \dots , F_n$ tale che ogni formula $F_i$:
>- O è un’istanza di un assioma;
>- Oppure si ottiene dalle formule precedenti della sequenza tramite una regola di  inferenza.

**Esempio.** Consideriamo il nostro sistema $S_0$. Nel seguito la indicheremo con _M.P._ la  
regola di inferenza Modus Ponens.

![[appunti lrl/immagini/Pasted image 20230413115413.png|center|600]]

La sequenza di formule (1), (2) e (3) qui sopra è una dimostrazione secondo la Definizione 2.1.
Infatti, le formule (1) e (2) sono istanze di assiomi, e la formula (3) si ottiene dalle due formule precedenti usando la regola di inferenza Modus Ponens, dove abbiamo posto $$X = (p \to (q \to p))$ e $Y = (p \to q) \to (p \to p)$$
A questo punto possiamo anche dire cos’è un teorema in un sistema assiomatico.

>[!definition]- Definizione 2.2 (Teorema)
>In un sistema assiomatico, un teorema è l’ultima formula di una dimostrazione.

## Derivazioni e Teorema di Deduzione

Un concetto che estende quello di dimostrazione è quello che chiamiamo _derivazione_.  
>[!definition]- Definizione 3.1 (Derivazione)
>Sia S un sistema assiomatico, sia $\mathcal F$ una formula e sia $\Gamma$ un insieme di formule. Diciamo che $\mathcal F$ deriva da $\Gamma$ nel sistema S se esiste una sequenza di formule $F_1, \dots , F_n$ tali che $F_n = \mathcal F$ e ognuna delle $F_i$, per i = 1, . . . n, :
>- O è un’istanza di un assioma;  
>- O si ottiene dalle formule precedenti della sequenza tramite una regola di inferenza;
>- Oppure è una delle formule dell’insieme $\Gamma$.  
>La sequenza $F_1, \dots , F_n$ si chiama **derivazione** di $\mathcal F$ da $\Gamma$. Le formule in $\Gamma$ sono le ipotesi della derivazione.  

Introduciamo anche un po’ di simboli. Quando una formula F deriva da un insieme $\Gamma$ in un sistema assiomatico S scriviamo $\Gamma\vdash_S F$. Quando il sistema S di cui stiamo parlando è chiaro dal contesto lo omettiamo e scriviamo semplicemente $\Gamma\vdash F$.

**Esempio**
Consideriamo sempre il nostro sistema $S_0$ e facciamo vedere che la formula $p \to r$ deriva dalle formule $p \to q$ e $q \to r$. In simboli
$$p\to q,q\to r\vdash p\to r$$
Chiamiamo $p \to q$ e $q \to r$ rispettivamente Ipotesi 1 e Ipotesi 2.

![[appunti lrl/immagini/Pasted image 20230413121349.png|center|500]]

La sequenza di formule (1), . . . , (7) qui sopra è una derivazione della formula $p \to r$ dall’insieme di formule $\{p \to q, q \to r\}$. Le formule (1) e (2) sono istanze di assiomi, (3)  
e (6) sono le ipotesi, (4), (5) e (7) seguono da formule precedenti tramite Modus Ponens.

Se confrontate le definizioni di dimostrazione e teorema con quella di derivazione,  
potete osservare che una dimostrazione di $\mathcal F$ è una derivazione di $\mathcal F$ con $\Gamma = \emptyset$. 

Per indicare che una formula $\mathcal F$ è un teorema nel sistema S perciò scriveremo $\vdash\mathcal F$

**Esercizio 8**. Siano $\mathcal F$ e $\mathcal G$ due formule. Dimostrare che se in $S_0$ si può derivare $\mathcal G$ da $\mathcal F$, allora $\mathcal F\to\mathcal G$ è un teorema. In simboli, se $\mathcal F\vdash\mathcal G$ allora $\vdash\mathcal F\to\mathcal G$

L’esercizio precedente si può generalizzare un po’, ottenendo quello che si chiama **Teorema di deduzione.**  

>[!definition]- Teorema 3.2 (Teorema di deduzione)
>Sia $\Gamma$ un insieme di formule e siano $\mathcal F$ e $\mathcal G$ due formule. Nel sistema $S_0$ se $\Gamma\cup\{\mathcal F\}\vdash\mathcal G$ allora $\Gamma\vdash\mathcal F\to\mathcal G$



