# CNF (Chomsky Normal Form)

Una grammatica di tipo 2 si dice in **Forma Normale di Chomsky** se tutte le sue produzioni sono del tipo $A\to BC$ o del tipo $A\to a$, con $A,B,C\in V_N,a\in V_T$

>[!important]- Teorema
>Data un grammatica $\mathcal G$ non contestuale tale che $\varepsilon\not\in L(\mathcal G)$, esiste una grammatica equivalente in CNF

Come mostrato, è possibilederivare una grammatica $\mathcal G'$ in forma ridotta equivalente a $\mathcal G$: in particolare, $\mathcal G'$ non ha produzioni unitarie

Da $\mathcal G'$, è possibile derivare una grammatica $\mathcal G''$ in CNF, equivalente a essa

Sia $A\to\zeta_{i_1}...\zeta_{i_n}$  una produzione di $\mathcal G'$ non in CNF. Si possono verificare due casi:

- $n\geq3$ e $\zeta_{i_j}\in V_N,j=1,...,n$. In tal caso, introduciamo $n-2$ nuovi simboli non terminali $Z_1,...,Z_{n-2}$ e sostituiamo la produzione $A\to\zeta_{i_1}...\zeta_{i_n}$ con le produzioni $$\begin{align}A&\to\zeta_{i_1}Z_1\\Z_1&\to\zeta_{i_2}Z_2\\&...\\Z_{n-2}&\to\zeta_{i_{n-1}}\zeta_{i_n}\end{align}$$
	- **Esempio** $A\to BCBD$ diventa $A\to BZ_1,Z_1\to CZ_2,Z_2\to BD$ 
- $n\geq2$ e $\zeta_{i_j}\in V_N$ per qualche $j\in\lbrace 1,...,n\rbrace$. In tal caso per ciascun $\zeta_{i_j}\in V_T$ introduciamo un nuovo non terminale $\overline Z_{i_j}$, sostituiamo $\overline Z_{i_j}$ a $\zeta_{i_j}$ nella produzione considerata e aggiungiamo la produzione $\overline Z_{i_j}\to\zeta_{i_j}$. Così facendo o abbiamo messo in CNF la produzione considerata (se $n=2$) o ci siamo ricondotti al caso precedente (se $n\geq3$). 
	- **Esempio**: La grammatica $A\to ab$ diventa $A\to X_aX_b,X_a\to a,X_b\to b$

**Esempio**

Si consideri la grammatica di tipo 2 che genera il linguaggio $\lbrace a^nb^n|n\geq1\rbrace$ con le produzioni:
$$\begin{align}S&\to aSb\\S&\to ab\end{align}$$
La gramamtica è in forma ridotta

La grammatica equivalente in CNF avrà le seguenti produzioni: 
$$\begin{align}&S\to X_aSX_b\\&X_a\to a\\&X_b\to b\\&\text{oppure}\\&S\to X_aZ_1\\&Z_1\to SX_b\\&X_a\to a\\&X_b\to b\end{align}$$
>[!info]- Osservazione
>La produzione $S\to X_aSX_b$ può essere sostituita con le produzioni $S\to X_aZ_1,Z_1\to SX_b$


# GNF (Greibach Normal Form)
