# Ancora sulle grammatiche

**Esempio**

Il linguaggio $L=\lbrace a^nb^nc^n|n\geq1\rbrace$ può essere generato dalla grammatica $\mathcal G$ in cui $V_T=\lbrace a,b,c\rbrace\:e\:V_n=\lbrace S,B,C,F,G\rbrace$ e le regole $P$ sono:

1. $S\to aSBC$
2. $CB\to BC$
3. $SB\to bF$
4. $FB\to bF$
5. $FC\to cG$
6. $GC\to cG$
7. $G\to\epsilon$

Vedi soluzione sotto l'esempio di [[Lezione 3 - Espressioni regolari,Grammatiche#Forme di frase|Lezione 3 (Forma di Frase)]]

**Esempio/Esercizio**
Come dimostrare che $L(G)=\lbrace a^nb^nc^n|n\geq1\rbrace$?

- Dimostrare che ogni x del tipo $a^nb^nc^n$ è derivabile in $\mathcal G$ 
- Dimostrare che ogni $z\in V_T^\star=\lbrace a^nb^nc^n\rbrace^\star$ derivabile in $\mathcal G$ ha la forma $a^nb^nc^n$

**Esempio/Esercizio**

La grammatica $\mathcal G=\langle\lbrace a,b\rbrace,\lbrace S,A\rbrace,P,S\rangle$ con pruduzioni $P$

1. $S\to Ab$
2. $A\to Sa$

genera il linguaggio vuoto $\Lambda$ (Perchè genero un ciclo infinito di stringhe che contengono un carattere Non terminale)

**Esempio**

Dimostriamo che la grammatica $\mathcal G=\langle\lbrace a,b,c\rbrace,\lbrace S,A\rbrace,P,S\rangle$ con produzioni $P$

1. $S\to aSc|A$
2. $A\to bAc|\epsilon$
genera il linguaggio
$$L=\lbrace a^nb^mc^{n+m}|n,m\geq0\rbrace$$
no dim.

**Esempio**
Data la grammatica $\mathcal G=\langle\lbrace a\rbrace,\lbrace S,I,F,M\rbrace,P,S\rangle$ con produzioni P

1. $S\to a|aa|IaF$
2. $aF\to Maa|MaaF$
3. $aM\to Maa$
4. $IM\to Ia|aa$

dimostrare che genera il linguaggio $\lbrace a^{2^n}|n\geq0\rbrace$
Per esempio, possiamo vedere che:

1. $S = a\to n=0$
2. $S=aa\to n=1$
3. $S=IaF=IMaa=aaaa\to n=2$
4. $S=IaF=IMaaF=IaaaF=IaaMaa=IaMaaaa=IMaaaaaa=aaaaaaaa\to n=3$

**Esercizio**
Definire la grammatica che genera il linguaggio $L=\lbrace a^nb^mc^p|n,p\geq0,m\geq1;n=m\lor m=p\rbrace$ 
e dimostrare la sua correttezza
(Il numero di b sarà uguale o al numeor di a, o al numeor di c; ES. la stringa abbcc è okay)

# Equivalenza tra grammatiche

Due grammatiche $\mathcal G_1\:e\:\mathcal G_2$ si dicono **equivalenti** se generano lo stesso linguaggio, vale a dire se $L(\mathcal G_1)=L(\mathcal G_2)$

**esempio/esercizio**

dimostrare che la grammatica con produzioni $S\to aS|b$ e la grammatica con produzioni $S\to b|Ab\:\:A\to Aa|a$ sono equivalenti

# Tipologia di grammatiche
## Grammatiche di tipo 0
_Def_
Le grammatiche di tipo 0, dette anche **non limitate**, definiscono la classe dei linguaggi più ampia possibile.
In esse le produzioni sono del tipo generale 
$$\alpha\to\beta,\alpha\in V^\star\circ V_N\circ V^\star,\beta\in V^\star$$

Queste grammatiche ammettono anche derivazioni che "accorciano" le forme di frase, come ad esempio quelle che si ottengono applicando le $\epsilon$-produzioni

I linguaggi generabili da grammatiche di tipo 0 si dicono **linguaggi di tipo 0**

**Esempio**
La gramamtica $$\mathcal G=\langle\lbrace a,b\rbrace,\lbrace S,A\rbrace,P,S\rangle$$
in cui P è 
1. $S\to aAb$
2. $aA\to aaAb$
3. $A\to\epsilon$

è di tipo 0 e genera il linguaggio $L=\lbrace a^nb^n|n\geq1\rbrace$
Infatti, per esempio una derivazione è:
$$S=aAb=aaAbb=aabb\to(a^2b^2)$$

## Grammatiche di tipo 1
_Def_
Dette anche **contestuali** o **context sensitive** (CS), ammettono qualunque regola di produzione che non riduca la lunghezza delle stringhe, cioè tutte le produzioni del tipo:
$$\alpha\to\gamma,\alpha\in V^\star\circ V_N\circ V^\star,\gamma\in V^+,|\alpha|\leq|\gamma|$$
I linguaggi generabili da grammativche di tipo 1 si dicono **linguaggi di tipo1, contestuali, o context sensitive**

**Oss** Nell'esempio di prima, la grammatica è di tipo 0 ma non di tipo 1 perchè la produzione $A\to\epsilon$ accorcia(infatti |A|=1 mentre |$\epsilon$|=0), e quindi non vale la regola per le grammatiche di tipo 1
**Oss** un linguaggio generato da una grammatica di tipo 1 è generato anche da una grammatica di tipo 0 (grammatica di tipo 1 $\subset$ grammatica di tipo 0)

**Esempio**

le produzioni 
1. $S\to aSa|aAb|aAa$
2. $aA\to aa$
3. $Ab\to aab$

appartengono ad una grammatica di tipo 1 (perchè nessuna delle produzioni accorcia, al più mantengono tutte la stessa lunghezza)

**Esempio**
Il linguaggio $L=\lbrace a^nb^n|n\geq1\rbrace$ visto prima, può essere generato da una gramamtica di tipo 1 avente le seguenti produzioni:
1. $S\to aBS|ab$
2. $Ba\to aB$
3. $Bb\to bb$

dunque il linguaggio è contestuale

### Definizione alternativa

Il termine "linguaggio contestuale" deriva dal fatto che sono generabili da gramamtiche aventi produzioni "contestuali" del tipo $$\beta_1A\beta_2\to \beta_1\gamma\beta_2,A\in V_N,\beta_1\beta_2\in V^\star,\gamma\in V^+$$
in cui si esprime il fatto che A può essere sostituito da $\gamma$ in una forma di frase solo se si trova nel contesto $\langle beta_1,\beta_2\rangle$ 

## Grammatiche di tipo 2
_Def_

Dette anche **non contestuali** o **contex free** (CF), ammettono solo produzioni del tipo:
$$A\to\beta,A\in V_N,\beta\in V^+$$
cioè produzioni in cui ogni non terminale A piò essere riscritto in una stringa $\beta$ indipendentemente dal contesto in cui esso si trova

**Esempio**
Grammatica che genera espressioni aritmetiche di somme e moltiplicazioni in una variabile i:

1. $E\to E+T|T$
2. $T\to T\cdot F|F$
3. $F\to i|(E)$

Generare la stringa $(i+i)\cdot i$ utilizando la gramamtica dell'esempio precedente

**Oss** il linguaggio visto prima $L=\lbrace a^nb^n|n\geq1\rbrace$ può essere generato dalla grammatica di tipo 2 con produzioni 

1. $S\to aSb|ab$

Dunque il linguaggio in questione è context free

## Grammatiche di tipo 3

Dette anche **lineari destre o regolari**, ammettono solo produzioni del tipo:
$$A\to\delta,A\in V_N,\delta\in (V_T\circ V_N)\cup V_T$$
il termine "regolare" deriva dal fatto che i corrispondendi linguaggi sono rappresentabili per mezzo di espressioni regolari

I linguaggi generabili da queste gramamtiche vengono detti **linguaggi di tipo 3 o regolari**

**Esempio**
la grammatica $\mathcal G=\langle\lbrace a,b\rbrace,\lbrace S\rbrace,P,S\rangle$
in cui P contiene le produzioni 
1. $S\to aS|b$
è una grammatica di tipo 3 e genera il linguaggio regolare $L=\lbrace a^nb|n\geq0\rbrace$

**Esercizio**
Definire una grammatica regolare per il linguaggio delle stringhe sull'alfabeto $\lbrace a,b\rbrace$ che contengono un numero dispari di a

#### Grammatiche lineari sinistre

Sono caratterizzate da regole del tipo:
$$A\to\delta,A\in V_N,\delta\in (V_N\circ V_T)\cup V_T$$
le grammatiche sinistre differiscono dalle grammatiche destre lineari destre in quanto l'unico simbolo non terminale che può comparire nella parte destra $\delta$ della produzione appare come primo simbolo

# Gerarchia di Chomsky

Per ogni $0\leq n\leq 2$, ogni grammatica di tipo n+1 è anche di tipo n: pertanto l'insieme dei linguaggi di tipo n contiene tutti i linguaggi di tipo n+1, formando quindi una gerarchai, detta **Gerarchia di Chomsky**

![[appunti fi/immagini/Pasted image 20221024124024.png|center|500]]
