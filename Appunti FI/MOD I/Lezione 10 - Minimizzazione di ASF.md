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

Ipotesi:

Tutti gli stati di $\mathcal A$ sono raggiungibili dallo stato iniziale, altrimenti è necessario un passo preliminare di eliminazione degli stati irraggiungibili

- Per marcare le coppire di stati distinguibili si utilizza una tabella contenente una casella per ciascuna coppia (non ordinata) di stati di $Q$
- Le caselle vengono usate per marcare le coppie di stati distinguibili e per elencare, in una lista associata, tutte le coppie che dovranno essere marcate qualora la coppia a cui è associata la casella venga marcata

La procedura inizia con la marcatura delle coppie distinguibili tramite la stringa $\varepsilon$ (tutte e sole le coppie costituite da uno stato finale e da uno non finale)
Per ogni coppia $(p,q)$ non ancora marcata, si considerano, per ogni $q\in\Sigma$, tutte le coppie $(r,s)$, con $r=\delta(p,)\:e\:s=\delta(q,a)$
- Se nessuna delle coppie $(r,s)$ è marcata come distinguibile allora si inserisce $(p,q)$ nella lista associata ad ognuna di esse
- Altrimenti p e q veongono riconosciuti distinguibili e la corrispondente casella viene marcata; qualora questa contenga una lista di coppie si procede (ricorsivamente) con la marcatura delle relative caselle

![[appunti fi/mod i/immagini/Pasted image 20221117125800.png|center|600]]

Una volta identificate le coppie di stati indistinguibili, ricordando che la relazione di indistinguibilità è una relazione di equivalenza, l'automa equivalente con il minimo numero di stati è dato evidentemente da $\mathcal A'=\langle\Sigma,Q',\delta',q_0',F'\rangle$, in cui:

1. $Q'$ è costruito selezionando, per ogni insieme di stati indistinguibili, uno ed un solo stato $Q$ (rappresentante)
2. $F'$ è costruito da tutti i rappresentanti appartenenti a $F$
3. $\delta'$ è ottenuta da $\delta$ mediante restrizione al dominio $Q'\times\Sigma$ ed inoltre, per ogni $\delta(q_i,a)=q_j$, con $q_i\in Q'\:e\:q_j\in Q$, poniamo $\delta'(q_i,a)=q_k$, dove $q_k\in Q'$ è il rappresentante dell'insieme di stati indistinguibili che include $q_j$ (chiaramente, se $q_j\in Q'$ allora è esso stesso un rappresentante e dunque $q_k=q_j$)

**Esempio**

![[appunti fi/mod i/immagini/Pasted image 20221117131616.png|center|600]]

**Passo inziale**: $q_0,q_1$, finali, distinguibili da tutti gli altri

Tutte le coppie in cui uno dei stati è $q_o\:o\:q_1$ e l'altro non è $q_o\:o\:q_1$ sono marcate 

![[appunti fi/mod i/immagini/Pasted image 20221117131847.png|center|600]]

