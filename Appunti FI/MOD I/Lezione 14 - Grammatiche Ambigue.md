
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

