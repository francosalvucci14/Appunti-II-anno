
# Ambiguità

Una grammmatica CF $\mathcal G$ si dice **ambigua** se esiste una stringa $x\in L(\mathcal G)$ derivabile con due diversi alberi sintattici

L'albero sintattico di una stringa corrisponde in qualche modo al significato della stringa stessa, quindi l'univocità di questo albero è importante per comprendere senza ambiguità tale significato

**esempio**

Si consideri la grammatica 
$$E\to E+E|E-E|E*E|E/E|(E)|a$$
Essa genera tutte le espressioni aritmetiche sulla variabile a, ma come si vede facilmente la stessa espressione può essere derivata con alberi di derivazione differenti

Ad esempio la stringa $a+a*a$ può venire derivata mediante due diversi alberi 

![[appunti fi/mod i/immagini/Pasted image 20221209100138.png|center|600]]

Se si pone $a=3$, nel primo albero avremo che la stringa genererà il numero 12, mentre il secondo genererà il numero 18

## Eliminazione dell'ambiguità

- Introduzione di parentesi
- Precedenza tra operatori

### Parentesi
$$E\to (E+E)|(E-E)|(E*E)|(E/E)|(E)|a$$
I due diversi alberi di derivazione che davano origine alla stessa stringa, danno ora origine alle due stringhe
$$\begin{align}&(a+(a*a))\\&((a+a)*a)\end{align}$$


### Precedenza

$$\begin{align}&E\to E+T|E-T|T\\&T\to T*F|T/F|F\\&F\to (E)|a\end{align}$$
La grammatica rappresenta nella sua struttura le relazioni di precedenza definite tra gli operatori (nell'ordine non decrescente $+,-,*,/$) e in tal caso consente di utilizzare le parentesi soltanto quando strettamente necessario

## Riconoscimento

Data una grammatica $\mathcal G$ non contestuale, $\mathcal G$ è ambigua?

Il problema è **indicidibile** nel caso delle CFG: non esiste quindi nessun algoritmo di decisione che, data una CFG, restituisca T se la grammatica è ambigua e F altrimenti

### Riduzione

Indecibilità dimostrata mediante **riduzione** da un'altro problema di decisione $\mathcal P$, che si sa essere indecidibile

Schema generale di dimostrazione:

- Si vuole mostrare che il problema $\mathcal P_1$ è indecidibile
- Si individua un'altro problema $\mathcal P_0$ che si sa essere indecidibile
- Se definisce un algoritmo $\mathcal A$ che trasforma ogni istanza $\mathcal I_0$ di $\mathcal P_0$ in una istanza $\mathcal I_1=\mathcal A(\mathcal I_0)$ di $\mathcal P_0$
- Si mostra che l'istanza $\mathcal I_1$ è positiva per $\mathcal P_1$ se e solo se $\mathcal I_0$ è positiva per $\mathcal P_0$
- Si conclude che $\mathcal P_1$ è indecidibile: se così non fosse avremmo un algoritmo che decide $\mathcal P_0$, in quanto potremmo trasformare, per mezzo di $\mathcal A$, ogni sua istanza in una istanza corrispondente di $\mathcal P_1$, che potremmo, per ipotesi, risolvere

Nel nostro caso:

- $\mathcal P_1$ è il problema di determinare, data una grammatica CF (istanza del problema), se essa è ambigua
- $\mathcal P_0$ è **PCP** (Problema delle Corrispondenze di Post):
	- data una istanza del problema, composta da:
		- un alfabeto $\Sigma$
		- due sequenze di k parole $X=x_1,...,x_k$ e $Y=y_1,...,y_k$ costruite su $\Sigma$
	- ci si chiede se esiste una sequenza di $m\geq1$ interi $i_1,i_2,...,i_m$ in $[1,..,k]$ tale che risulti $$x_{i_1},...,x_{i_m}=y_{i_1},...,y_{i_m}$$

