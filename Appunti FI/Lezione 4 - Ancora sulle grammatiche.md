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
- Dimostrare che ogni $z\in V_t^\star=\lbrace a^nb^nc^n\rbrace^\star$ derivabile in $\mathcal G$ ha la forma $a^nb^nc^n$

**Esempio/Esercizio**

La grammatica $\mathcal G=\langle\lbrace a,b\rbrace,\lbrace S,A\rbrace,P,S\rangle$ con pruduzioni $P$

1. $S\to Ab$
2. $A\to Sa$

genera il linguaggio vuoto $\Lambda$  

**Esempio**

Dimostriamo che la grammatica $\mathcal G=\langle\lbrace a,b,c\rbrace,\lbrace S,A\rbrace,P,S\rangle$ con produzioni $P$