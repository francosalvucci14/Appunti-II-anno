Ritornando a [[Lezione 11 - Pumping Lemma,Linguaggi CF#Forme ridotte e forme normali|Forme ridotte e forme normali]]

# Forme ridotte e normali 

Trasformazione di una grammatica $\mathcal G=\langle V_T,V_N,P,S\rangle$ di tipo 2 in una grammatica equivalente in forma ridotta mediante una sequenza di passi

1. A partire da $\mathcal G$, derivazione di $\mathcal G_1$ di tipo 2 senza $\varepsilon$-produzioni tale che $L(\mathcal G_1)=L(\mathcal G)-\lbrace\varepsilon\rbrace$
2. A partire da $\mathcal G_1$, derivazione di $\mathcal G_2$ di tipo 2 senza $\varepsilon$-produzioni e senza produzioni unitarie tale che $L(\mathcal G_2)=L(\mathcal G_1)$
3. A partire da $\mathcal G_2$, derivazione di $\mathcal G_3$ di tipo 2 senza $\varepsilon$-produzioni, senza produzioni unitarie e senza simboli inutili tale che $L(\mathcal G_3)=L(\mathcal G_2)$
4. La grammatica $\mathcal G_4$ di tipo 2, equivalente a $\mathcal G$ coincide con $\mathcal G_3$ se $\varepsilon\not\in L(\mathcal G)$; altrimenti, $\mathcal G_4$ è ottenuta da $\mathcal G_3$ introducendo un nuovo assioma ed un opportuno insieme di produzioni su tale simbolo


## Passo 1

>[!important]- Teorema
>Data una grammatica $\mathcal G=\langle V_T,V_N,P,S\rangle$ il cui insieme di produzioni P comprende soltanto produzioni di tipo non contestuale e produzioni vuote, esiste una grammatica non contestuale $\mathcal G'$ tale che $L(\mathcal G')=L(\mathcal G)-\lbrace\varepsilon\rbrace$

Determinazione dell'insieme $N\subseteq V_N$ dei simboli che si annullano, cioè i non terminali da cui è possibile derivare $\varepsilon$ in $\mathcal G$

Costruzione di una sequenza $N_0,N_1,...,N_k=N$ di sottoinsiemi di $V_N$, con $N_0=\lbrace A\in V_N|A\to\varepsilon\in P\rbrace$ e $N_{i+1}$ derivato da $N_i$ :$$N_{i+1}=N_i\cup\lbrace B\in V_N|(B\to\beta\in P)\land(\beta\in N_i^+)\rbrace$$
La costruzione termina quando $N_{k+1}=N_k, k\geq0$

$\varepsilon\in L(\mathcal G)\iff S\in N$

![[appunti fi/mod i/immagini/Pasted image 20221122112802.png|center|500]]

**Esempio**
Consideriamo la grammatica $\mathcal G=\langle\{a,b\},\{S,A,B\},P,S\rangle$, le cui produzioni sono:
$$\begin{align}S&\to A|SSa\\A&\to B|Ab|\varepsilon\\B&\to S|ab|aA\end{align}$$
Quindi:
$$\begin{align}N_0 &= \{A\}\\N_1 &= \{A,S\}\\N_2&=\{A,S,B\}\\N_3&=\{A,S,B\}=N_2=N\end{align}$$
Costruzione delle produzioni $P'$ di $\mathcal G'$:
- Si esamina ciascuna produzione $A\to\alpha$ di $P$, con l'esclusione delle $\varepsilon$-produzioni:
	- Se nessun simbolo di $\alpha$ è annullabile: $A\to\alpha$ è inserita in $P'$
	- Altrimenti $\alpha$ contiene $k\gt0$ simboli che si annullano: sono inserite in $P'$ tutte le possibili produzioni ottenute da $A\to\alpha$ eliminando da $\alpha$ uno dei sottoinsiemi di simboli che si annullano

Ritornando all'esempio:

Le produzioni $P'$ sono quindi:
$$\begin{align}S&\to A|SSa|Sa|a|\varepsilon\\A&\to B|Ab|b\\B&\to S|ab|aA|a\end{align}$$

## Passo 2

>[!important]- Teorema
>Per ogni grammatica $\mathcal G$ di tipo 2 senza $\varepsilon$-produzioni, esiste sempre una grammatica $\mathcal G'$ di tipo 2 senza $\varepsilon$-produzioni,priva di produzioni unitarie ed equivalente a $\mathcal G$

Sia, per ogni $A\in V_N,U(A)$ il sottoinsieme di $V_N-\lbrace A\rbrace$ comprendente tutti i non terminali derivabii da $A$ applicando una sequenza di produzioni unitarie:
$$U(A)=\lbrace B\in V_N-\lbrace A\rbrace|A\xRightarrow[]{\star}B\rbrace$$
Data la grammatica $\mathcal G=\langle V_T,V_N,P,S\rangle$, $P'$ è costruito:

- Inserendo dapprima in $P'$ tutte le produzioni non unitarie di $P$
- Inserendo in $P'$, per ogni non terminale $A$ e per ogni $B\in U(A)$, la produzione $A\to\beta$ se e solo se in $P$ esiste una produzione non unitaria $B\to\beta$

**Esercizio/Esempio**
Costruire un algoritmo che, data una grammatica $\mathcal G$ di tipo 2 senza $\varepsilon$-produzioni e dato un non terminale $A$ della grammatica, determini l’insieme $U(A)$

Soluzione:
- Passo iniziale: Inserisci in $U(A)$ tutti i simboli $B$ tali che $A\to B$
- Passo iterativo: per ogni simbolo $B\in U(A)$, inserisci in $U(A)$ tutti i simboli $C$ tali che $B\to C$; termina se nessun nuovo simbolo è stato inserito in $U(A)$


## Passo 3

