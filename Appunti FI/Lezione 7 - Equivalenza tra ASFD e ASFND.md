
# Equivalenza tra ASFD e ASFND

Dato un ASFD che riconosce un linguaggio $L$, esiste corrispondentemente un ASFND che rinconosce lo stesso linguaggio $L$; viceversa, dato un ASFND che riconosce un linguaggio $L'$, esiste un ASFD che riconosce lo stesso linguaggio $L'$ 

Dato un ASFND $\mathcal A_n=\langle\Sigma,Q,\delta,q_0,F\rangle$, un ASFD equivalente $\mathcal A'=\langle\Sigma,Q',\delta',q_0',F'\rangle$ è derivabile nel modo seguente:

L'insieme $Q'$ è in corrispondenza biunivoca con $\mathcal P(Q)$ (quindi $|Q'|=2^{|Q|}$).

Indichiamo come $[q_{i_1},...,q_{i_k}]\in Q'$ lo stato corrispondente all'insieme $\lbrace q_{i_1},...,q_{i_k}\rbrace\subseteq Q$: i nomi degli stati di Q sono ordinati lessicograficamente.

Quindi $Q'$ risulta definito come:
$$Q'=\lbrace[q_{i_1},...,q_{i_k}]|\lbrace q_{i_1},...,q_{i_k}\rbrace\in\mathcal P(Q)\rbrace$$

Lo stato iniziale è $q_0'=[q_0]$
Gli stati finali di $F'$ corrispondono ai sottoinsiemi di Q che contengono almeno un elemento di $F$:
$$F'=\lbrace[q_{i_1},...,q_{i_k}]|\lbrace q_{i_1},...,q_{i_k}\rbrace\in\mathcal P(Q)\land\lbrace q_{i_1},...,q_{i_k}\rbrace\cap F\neq0\rbrace$$

$\delta'$ è definita nel seguente modo:
$$\forall q_{i_1},...,q_{i_k}\in Q,\forall a\in\Sigma,\delta'([q_{i_1},...,q_{i_k}],a)=[q_{j_1},...,q_{j_h}]$$
se e solo se
$$\delta_N(q_{i_1},a)\cup...\cup\delta_N(q_{i_k},a)=\lbrace q_{j_1},...,q_{j_h}\rbrace$$
con $k\gt0,h\geq0$

Inoltre, si assume che per ogni $a\in\Sigma$ sia $\delta'([],a)=[]$

Come mostrare che $\mathcal A_N$ e $\mathcal A$ sono equivalenti?