```table-of-contents
title: 
style: nestedList # TOC style (nestedList|inlineFirstLevel)
minLevel: 0 # Include headings from the specified level
maxLevel: 0 # Include headings up to the specified level
includeLinks: true # Make headings clickable
debugInConsole: false # Print debug info in Obsidian console
```
# Intrattabilità I
## Pattern e Antipattern nella progettazione di Algoritmi

Alcuni pattern di progettazione sono :
- Greedy
- Divide et impera
- Programmazione dinamica
- Dualità
- **Riduzioni**
- etc...

Mentre gli anti-pattern sono :
- **NP-Completezza** : Algoritmi con tempo $O(n^k)$ sono altamente improbabili
- PSPACE-Completezza : Algoritmo per la certificazione della soluzione in tempo $O(n^k)$ altamente improbabile
- Indecibilità : Nessun algoritmo possibile

## Classificare i problemi in base ai requisiti computazionali

**D** : Quali problemi siamo in grado di risolvere?

**R** : Quelli che hanno un'algoritmo polinomiale

**Teoria** : La definizione è ampia e solida
**Pratica** : Gli algoritmo polinomiali sono adatti a problemi enormi

![[Pasted image 20240510110811.png|center|500]]
### Classificare i problemi

**Desiderata**. Classificare i problemi in base a quelli che possono essere risolti in tempo polinomiale e a quelli che non possono essere risolti.

Esempi che richiedono tempo esponenziale.
- Dato un programma di dimensione costante, si arresta al massimo in k passi?
- Data una posizione di tavola in una generalizzazione n per n della dama, il nero può garantire una vittoria?

## Riduzioni polinomiali

**Osservazione** : Supponiamo di poter risolvere il problema $Y$ in tempo polinomiale. Che altro possiamo risolvere in tempo polinomiale?

>[!definition]- Riduzioni
>Un problema $X$ si **riduce polinomialmente (Cook)** ad un problema $Y$ se istanze arbitrarie di $X$ possono essere risolte usando :
>- Un numero polinomiale di passaggi computazionali standard, più
>- Un numero polinomiale di chiamate all'**Oracolo** che risolve il problema $Y$

>[!info]- Osservazione
>L'oracolo è un **modello computazionale** creato con speciali pezzi hardware che risolve le istanze di $Y$ in tempo costante (Prettamente teorico)

![[Pasted image 20240510111523.png|center|500]]

Per le riduzioni polinomiali si usa la **notazione** $$X\leq_pY$$
Occhio a non fare l'errore di confondere $X\leq_pY$ con $Y\leq_pX$

- **Progettazione di algoritmi** : Se $X\leq_pY$ e $Y$ si può risolvere in tempo polinomiale, allora anche $X$ si può risolvere in tempo polinomiale
- **Stabilire l'intrattabilità** : Se $X\leq_pY$ e $X$ non può essere risolto in tempo polinomiale, allora neanche $Y$ si potrà risolvere in tempo polinomiale
- **Stabilire l'equivalenza** : Se sia $X\leq_p Y$ che $Y\leq_p X$, si usa la notazione $X\equiv_p Y$. In questo caso, $X$ può essere risolto in tempo polinomiale $\iff$ $Y$ può esserlo

## Problemi di covering e packing

Diamo ora la definizione di un paio di problemi fondamentali nella teoria della complessità.

Dimostreremo anche che questi problemi sono **NP-Completi** mediante riduzione dal problema **SAT**

### Indipendent Set

>[!definition]- Definizione
>Dato un grafo $G=(V,E)$ e un itero $k$, esiste un sottoinsieme di $k$ (o più) vertici tale che due vertici non sono adiacenti?

**Esempio** : Esiste un'indipendet set di dimensione $\geq6$?
**Esempio** : Esiste un'indipendet set di dimensione $\geq7$?

![[Pasted image 20240510151046.png|center|500]]

### Vertex Cover

>[!definition]- Definizione
>Dato un grafo $G=(V,E)$ e un itero $k$, esiste un sottoinsieme di $k$ (o meno) vertici tale che ogni arco è incidente ad almeno un vertice nel sottoinsieme?

**Esempio** : Esiste un vertex cover di dimensione $\leq4$?
**Esempio** : Esiste un vertex cover di dimensione $\leq3$?

![[Pasted image 20240510151242.png|center|500]]

#### Vertex Cover e Indipendent Set si riducono l'uno all'altro

>[!definition]- Teorema
>Indipendent Set $\equiv_p$ Vertex Cover

**Dimostrazione** : Dimostriamo che $S$ è un Indipendent Set di dimensione $k\iff V-S$ è un Vertex Cover di dimensione $n-k$

![[Pasted image 20240510151242.png|center|500]]

$\implies$
- Sia $S$ un IS di dimensione $k$
- $V-S$ ha dimensione $n-k$
- Consideriamo un arco arbitrario $(u,v)\in E$
- $S$ indipendente significa $\implies$
	- o $u\not\in S,v\not\in S$, o entrambi
	- o $u\in V-S,v\in V-S$, o entrambi
- Quindi, $V-S$ copre $(u,v)$

$\impliedby$

- Sia $V-S$ un qualunque Vertex Cover di dimensione $n-k$
- $S$ ha dimensione $k$
- Consideriamo un arco arbitrario $(u,v)\in E$
- $V-S$ vertex cover significa $\implies$
	- $u\in V-S$, o $v\in V-S$, o entrambi
	- $u \not\in S$, o $v\not\in S$, o entrambi
- Quindi, $S$ è un insieme indipendente
### Set Cover

>[!definition]- Set Cover
>Dato un insieme $U$ di elementi, una collezzione $S$ di sottoinsiemi di $U$, e un intero $k$, esistono $\leq k$ di questi sottoinsiemi la cui unione è uguale a $U$?

**Esempio**
- $m$ pezzi di software disponibili
- Insieme $U$ di $n$ servizi che vorremmo nel nostro sistema
- L'i-esimo pezzo di software fornisce l'insieme $S_i\subseteq U$ di servizi
- Goal : ottenere tutte le $n$ funzionalità utilizzando il minor numero di pezzi di software.

![[Pasted image 20240513115626.png|center|400]]

#### Vertex Cover si riduce a Set Cover

>[!definition]- Teorema
>Vertex Cover $\leq_p$ Set Cover

**Dimostrazione** : Data un'istanza di Vertex Cover $G=(V,E)$ e $k$, costruiamo un'istanza di Set Cover $(U,S,k)$ che ha un set cover di dimensione $k\iff G$ ha un vertex cover di dimensione $k$

**Costruzione**
- Universo $U=E$
- Includiamo un sottoinsieme per ogni nodo $$v\in V:S_v=\{e\in E:\text{e incidente a v}\}$$
![[Pasted image 20240513120032.png|center|500]]

>[!definition]- Lemma
>$G=(V,E)$ contiene un vertex cover di dimensione $k\iff(U,S,k)$ contiene un set cover di dimensione $k$


**Dimostrazione** $\implies$
- Sia $X\subseteq V$ un vertex cover di dimensione $k$ in $G$
	- Allora $Y=\{S_v:v\in X\}$ è un vertex cover di dimensione $k$

![[Pasted image 20240513120341.png|center|500]]

*L'istanza "si" di Vertex Cover è stata risolta correttamente*

$\impliedby$
- Sia $Y\subseteq S$ un set cover di dimensione $k$ in $(U,S,k)$
	- Allora $X=\{v:S_v\in Y\}$ è un vertex cover di dimensione $k$

![[Pasted image 20240513120341.png|center|500]]

*L'istanza "no" di Vertex Cover è stata risolta correttamente*

## Problemi di soddisfazione dei vincoli

### Soddisfabilità

Prima di parlare del problema **SAT**, diamo la definizione di **Letterale, Clausola e Forma Normale Congiuntiva**

>[!definition]- Letterale
>Una variaible booleana o la sua negazione $$x_i\lor\lnot x_i$$

>[!definition]- Clausola
>Una disgiunzione di clausole $$C_j=x_1\lor\lnot x_2\lor x_3$$

>[!definition]- Forma Normale Congiuntiva (CNF)
>Una formula proposizionale $\Phi$ che è una congiunzione di clausole $$\Phi=C_1\land C_2\land C_3\land\dots$$

Possiamo ora parlare del problema **SAT**

>[!definition]- SAT
>Data una formula $\Phi$ in CNF, essa ha un assegnamento di verità?
>Ovvero, esiste un modo di assegnare le variabili in modo tale da avere che la formula $\Phi$ risulti vera?

>[!definition]- 3-SAT
>Generalizzazione del problema SET, dove ogni clausola ha esattamente 3 letterali
>Per esempio $$\Phi=(\lnot x_1\lor x_2\lor x_3)\land(x_1\lor\lnot x_2\lor x_3)\land(\lnot x_1\lor x_2\lor x_4)$$

L'istanza "si" per l'esempio sopra è
- $x_1=x_2=true$
- $x_3=x_4=false$

#### Il problema SAT è NP-Hard

**Ipotesi scientifica** : Non esiste un algoritmo polinomiale per 3-SAT

>[!error]- $P$ vs $NP$
>Questa ipotesi è equivalente alla congettura $P\neq NP$

### 3-SAT si riduce a Indipendent Set

>[!definition]- Teorema
>3-SAT $\leq_p$ Indipendent Set

**Dim**
Data un'istanza $\Phi$ di 3-SAT, costruiamo un istanza $(G,k)$ di Indipendet Set che ha un indipendent set di dimensione $k=\vert\Phi\vert\iff\Phi$ è ***soddisfacibile***

**Costruzione**
- $G$ contiene 3 nodi per ogni clausola, uno per ogni letterale
- Connetti i 3 letterali nella clausola in un triangolo
- Connetti ogni letterale con la sua negazione

![[Pasted image 20240513141352.png|center|500]]

**Lemma** : $\Phi$ è soddisfacibile $\iff G$ contiene un insieme indipendente di dimensione $k=\vert\Phi\vert$

**Dimostrazione** $\implies$
- Consideriamo ogni assegnamento soddisfacente per $\Phi$
- Selezionamo un letterale vero da ogni clausola/triangolo
- Questo è un indipendent set di dimensione $k=\vert\Phi\vert$

*L'istanza "si" di 3-SAT è stata risolta correttamente*

$\impliedby$
- Sia $S$ un indipendent set di dimensione $k$
- $S$ deve contenere esattamente un nodo da ogni triangolo
- Impostiamo questi letterali a `true`
- Tutte le clausole in $\Phi$ sono soddisfatte

*L'istanza "no" di 3-SAT è stata risolta correttamente*

# Riduzioni Polinomiali

![[Pasted image 20240513143549.png|center|500]]