# Esercizio 1

- Input:
	- Grafo non diretto e pesato $G=(V,E,w)$
	- $e\in E$
- Goal: Capire se $e\in MST(G)$
- Tempo
	- Algoritmo Stupido
		- Calcolo $MST$
		- Vedo se $e\in MST$
	- Con Prim $\implies O(m+n\log(n))$
	- Con Kruskal $\implies O(m\log(n))$
- Tempo ottimo da trovare $O(m+n)$

**Grafo di esempio**

![[Pasted image 20240319144449.png|center|500]]

**Soluzione**

ALG(G,e):
- Costruisco $G'$ partendo da $G$, $G'$ usa solo archi il cui peso è $\leq w(e)$
- Eseguo una visita su $G'$ (DFS o BFS), per capire se $v$ è raggiungibile da $u$
	- Se si $\implies e\not\in MST$
	- Se no $\implies e\in MST$

Quanto costa questo algoritmo?

- Costruzione di $G'\implies O(m+n)$
- Visita $O(m+n)$
- Controllo sul peso $O(1)$

**Dimostrazione di correttezza**

_Proprietà_ : $e\not\in MST\iff v$ è raggiungibile da $u$ in $G'$
$(\leftarrow)$
- Prendiamo un cammino $P$ da $u$ a $v$ in $G'$
- Aggiungere $e$ in $P$, $P=P\cup\{e\}$, crea un ciclo in cui $e$ ha peso massimo
- Applico la cycle property $\implies e\not\in MST$

$(\rightarrow)$
- $S=\{w\in V|\text{w è raggiungibile da u in G'}\}$
- L'arco $e$ attraversa il taglio $S-\frac{V}{S}$
- Tutti gli archi che attraversano il taglio devono essere di peso $\gt w(e)$ (per costruzione di $G'$)
- Quindi $e\in MST$ per la cut property

---

# Esercizio 2

- Input : Albero binario completo e pesato $T$
- Soluzione Ammissibile : Nuova pesatura $w'$ di $T$ con $w'(e)\geq w(e)$ tale che tutte le foglie rispetto a $w'$ hanno la stessa distanza
- Misura (da minimizzare) : $$w'(T)=\sum\limits_{e}w'(e)$$
