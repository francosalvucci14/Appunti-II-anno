
# Equivalenza tra ASFD e ASFND

Dato un ASFD che riconosce un linguaggio $L$, esiste corrispondentemente un ASFND che rinconosce lo stesso linguaggio $L$; viceversa, dato un ASFND che riconosce un linguaggio $L'$, esiste un ASFD che riconosce lo stesso linguaggio $L'$ 

Dato un ASFND $\mathcal A_n=\langle\Sigma,Q,\delta,q_0,F\rangle$, un ASFD equivalente $\mathcal A'=\langle\Sigma,Q',\delta',q_0',F'\rangle$ è derivabile nel modo seguente:

L'insieme $Q'$ è in corrispondenza biunivoca con $\mathcal P(Q)$ (quindi $|Q'|=2^{|Q|}$).

Indichiamo come $[q_{i_1},...,q_{i_k}]\in Q'$ lo stato corrispondente all'insieme $\lbrace q_{i_1},...,q_{i_k}\rbrace\subseteq Q$: i nomi degli stati di $Q$ sono ordinati lessicograficamente.

Quindi $Q'$ risulta definito come:
$$Q'=\lbrace[q_{i_1},...,q_{i_k}]:\lbrace q_{i_1},...,q_{i_k}\rbrace\in\mathcal P(Q)\rbrace$$

Lo stato iniziale è $q_0'=[q_0]$

Gli stati finali di $F'$ corrispondono ai sottoinsiemi di Q che contengono almeno un elemento di $F$:
$$F'=\lbrace[q_{i_1},...,q_{i_k}]:\lbrace q_{i_1},...,q_{i_k}\rbrace\in\mathcal P(Q)\land\lbrace q_{i_1},...,q_{i_k}\rbrace\cap F\neq\emptyset\rbrace$$

$\delta^{'}$ è definita nel seguente modo:
$$\forall q_{i_1},...,q_{i_k}\in Q,\forall a\in\Sigma,\delta'([q_{i_1},...,q_{i_k}],a)=[q_{j_1},...,q_{j_h}]$$
se e solo se
$$\delta_N(q_{i_1},a)\cup...\cup\delta_N(q_{i_k},a)=\lbrace q_{j_1},...,q_{j_h}\rbrace$$
con $k\gt0,h\geq0$

Inoltre, si assume che per ogni $a\in\Sigma$ sia $\delta'([],a)=[]$

**Esempio di transizione da ASFND a ASFD**

![[appunti fi/immagini/Pasted image 20221107150359.png|center|600]]

Come mostrare che $\mathcal A_N$ e $\mathcal A$ sono equivalenti?

è necessario mostrare che, per ogni $x\in\Sigma^\star$, se $x$ è accettata da $\mathcal A_N$ allora viene accettata anche da $\mathcal A$. Vale anche il viceversa

Dimostrazione "più forte", che ad ogni computazione effettuata dall'automa $\mathcal A$ ne corrisponde una equivalente dell'automa $\mathcal A_N$ e viceversa. Cioè
$$\overline\delta'([q_0],x)=[q_{j_1},...,q_{j_h}]\iff\overline\delta_N(q_0,x)=\lbrace q_{j_1},...,q_{j_h}\rbrace$$

Se è vero questo, significa che o ogni stringa $x$ è accettata sia da $\mathcal A$ e da $\mathcal A_N$, o non è accettata da nessuno dei due

