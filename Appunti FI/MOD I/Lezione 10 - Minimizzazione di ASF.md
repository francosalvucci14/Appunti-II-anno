# Minimizzazione

L'ASFD con minimo numero di stati che riconosce un dato linguaggio $L$ può essere derivato partizionando l'insieme $Q$ degli stati in un automa che riconosce $L$ in classi di equivalenza rispetto alla relazione
$$q_i\equiv q_j\iff(\forall x\in\Sigma^\star,\overline\delta(q_i,x)\in F\iff\overline\delta(q_j,x)\in F)$$
Quindi, $q_i\equiv q_j$ se e solo se ogni stringa che porta da $q_i$ ad uno stato finale porta anche da $q_j$ ad uno stato finale (e vice versa)


>[!Info]
>$\equiv$ è una relazione di equivalenza

Se $q_i\equiv q_j$ i due stati sono detti **indistinguibili**

Se esiste una stringa $x\in\Sigma^\star$ per cui $\overline\delta(q_i,x)\in F\:e\:\overline\delta(q_j,x)\in Q-F$ (o viceversa) diremo che $q_i,q_j$ sono **distinguibili** tramite x

La costruzione è basata sul teorema di Myhill-Nerode

>[!important]- Teorema Myhill-Nerode
>Dato un linguaggio $L$ definiamo la relazione di equivalenza $R_L$ su $\Sigma^\star$ come:$$xR_Ly\iff(\forall z\in\Sigma^\star,xz\in L\iff yz\in L)$$
>Un linguaggio $L\subseteq\Sigma^\star$ è regolare se e solo se $R_L$ partiziona $\Sigma^\star$ in un numero finito di classi di equivalenza

Dato un linguaggio regolare $L$ definiamo un ASF $\mathcal A'=\langle\Sigma,Q',\delta',q_0',F'\rangle$, dove:

1. $Q'$ associa a ogni classe di equivalenza $[x]$ di $\Sigma^\star$ uno stato $q_{[x]}$
2. $q_0'=q_{[\varepsilon]}$
3. $F'=\lbrace q_{[x]}|x\in L\rbrace$
4. $\delta'(q_{[x]},a)=q_{[xa]}\:\forall a \in\Sigma$

Si può notare che $\forall z\in[x]:\overline\delta'(q_0',z)=q_{[x]}$. Quindi:

- l'insieme delle stringhe che portano l'automa dallo stato iniziale allo stato finale $q_{[x]}$ corrisponde all'insieme delle stringhe (equivalenti secondo $R_L$) in $[x]$. Dalla definizione di $F'$ ne consegue immediatamente che $\mathcal A'$ riconosce $L$
- $Q'$, pari al numero di classi di equivalenza di $R_L$ è il minimo numero di classi in cui è possibile partizionare $\Sigma^\star$ in modo tale che valga la proprietà $\forall z\in\Sigma^\star,xz\in L\iff yz\in L$ se $xR_Ly$

>$Q'$ è minimo

_Dim_
Se così non fosse, esisterebbero due stringhe x,y non equivalenti rispetto a $R_L$, per cui $\overline\delta'(q_0',x)=\overline\delta'(q_0',y)=q$. Ma allora ne seguirebbe che $\forall z\in\Sigma:\overline\delta'(q_0',xz)=\overline\delta'(q_0',yz)$, il che comporterebbe allora che $xR_Ly$, contrariamente all'ipotesi
$\square$

Minimizzazione di un ASFD

- Individuazione di tutte le coppie di stati indistinguibili (mediante un algoritmo di marcatura delle coppie distinguibili)
- Unificazione degli stati equivalenti, eliminando quelli non raggiungibili e modificando opportunamente la funzione di transizione
