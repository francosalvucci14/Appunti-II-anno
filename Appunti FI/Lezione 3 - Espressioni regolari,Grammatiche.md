# Ancora sulle espressioni regolari
Due epressioni regolari r,s sono **equivalenti** ($r\equiv s$) se $L(r)=L(s)$
ad esempio:
- $a+b\equiv b+a$
- $a+a\equiv a$
- $aa^\star\equiv a^\star a$
- $ab\not\equiv ba$ 

La differenza tra 1 e 4 è che il "+" è un operatore commutativo

## Algebra delle espressioni regolari
Assumiamo che $\cdot$ abbia precedenza su +. Quindi $a+b\cdot c\equiv a+(b\cdot c)$
Inoltre, rappresentiamo l'operatore $\cdot$ con la concatenazione degli operandi: $ab\equiv a\cdot b$

**Proprietà**
1. + è commutativa ($r+s\equiv s+r$), associativa ($r+(s+t)\equiv (r+s)+t$), con elemento neutro $\emptyset(r+\emptyset\equiv r)$,idempodente ($r+r\equiv r$)
2. $\cdot$ è associativa ($r(st)\equiv (rs)t$), con elemento neutro $\epsilon(r\epsilon\equiv r)$ e elemento nullo $\emptyset(r\emptyset\equiv\emptyset)$
3. $\cdot$ si distribuisce su + ($r(s+t)\equiv (rs+rt)$)
4. + _non_ si distribuisce su $\cdot$ ($r+st\not\equiv (r+s)(r+t)$)

**Proprietà derivate**
1. $\emptyset^\star\equiv\epsilon^\star\equiv\epsilon$
2. $r^\star\equiv r^\star r^\star\equiv (r^\star)^\star\equiv r+r^\star$
3. $r^\star\equiv\epsilon+r^\star\equiv\epsilon+rr^\star\equiv (\epsilon+r)^\star\equiv (\epsilon+r)r^\star$
4. $r^\star\equiv (r+r^2+...+r^k)^\star\equiv\epsilon+r+r^2+...+r^{k-1}+r^kr^\star\:\forall k\geq1$
5. $r^\star r\equiv rr^\star$
6. $(r+s)^\star\equiv (r^\star+s^\star)^\star\equiv (r^\star s^\star)^\star\equiv (r^\star s)^\star r^\star\equiv r^\star(sr^\star)^\star$
7. $r(sr)^\star\equiv (rs)^\star r$
8. $(r^\star s)^\star\equiv\epsilon+(r+s)^\star s$
9. $(rs^\star)\equiv\epsilon+r(r+s)^\star$

**Esempio**

Dimostrare che $(a+aa)(a+b)^\star\equiv a(a+b)^\star$

$(a+aa)(a+b)^\star\equiv (a+aa)a^\star(ba^\star)^\star$ in quanto $(r+s)^\star\equiv r^\star(sr^\star)^\star(\text{proprietà 6})$ 
$(a+aa)(a+b)^\star\equiv a(\epsilon+a)a^\star(ba^\star)^\star$ in quanto $r\equiv r\epsilon$ (proprietà 2 di $"\cdot"$)
$(a+aa)(a+b)^\star\equiv aa^\star(ba^\star)^\star$ in quanto $(\epsilon+r)r^\star\equiv r^\star$
$(a+aa)(a+b)^\star\equiv a(a+b)^\star$ in quanto $(r+s)^\star\equiv r^\star(sr^\star)^\star$

**Esempio**

Dimostrare che $a^\star(b+ab^\star)\equiv b+aa^\star b^\star$

$a^\star(b+ab^\star)\equiv (\epsilon+aa^\star)(b+ab^\star)$ in quanto $r^\star\equiv\epsilon+rr^\star$
$a^\star(b+ab^\star)\equiv b+ab^\star+aa^\star b+aa^\star ab^\star$ per distributiva
$a^\star(b+ab^\star)\equiv b+(ab^\star + aa^\star ab^\star)+aa^\star b$ per associativa e commutativa di +
$a^\star(b+ab^\star)\equiv b+(\epsilon+aa^\star)ab^\star + aa^\star b$ in quanto $r\equiv r\epsilon$
$a^\star(b+ab^\star)\equiv b+a^\star ab^\star + aa^\star b$ in quanto $r^\star\equiv\epsilon+rr^\star$
$a^\star(b+ab^\star)\equiv b+aa^\star b^\star+aa^\star b$ in quanto $r^\star r\equiv rr^\star$
$a^\star(b+ab^\star)\equiv b+aa^\star(b^\star+b)$ per distributiva
$a^\star(b+ab^\star)\equiv b+aa^\star b^\star$ in quanto $r^\star\equiv r^\star+r$

**Esempio**
Dimostrare che $(a+b)^\star\not\equiv a^\star+b^\star$
Basta osservare che $ab\in L((a+b)^\star) - L(a^\star+b^\star)$

**Semplificare l'espressione regolare** $aa(b^\star+a)+a(ab^\star+aa)$

$aa(b^\star+a)+a(ab^\star+aa)\equiv aa(b^\star+a)+aa(b^\star+a)$ distributiva
$aa(b^\star+a)+a(ab^\star+aa)\equiv aa(b^star+a)$ in quanto $r+r\equiv r$


# Grammatiche

Una **grammatica formale** $\mathcal G$ è una quadrupla $\mathcal G=\langle V_t,V_n,P,S\rangle$ in cui:

1. $V_t$ è un insieme finito e non vuoto di simboli **terminali**
2. $V_n$ è un insieme finito e non vuoto di simboli **non terminali**
3. $P$ è una relazione binaria di cardinalità finita su $$(V_t\cup V_n)^\star\circ V_n\circ (V_t\cup V_n)^\star\times(V_t\cup V_n)^\star$$ $P$ è detta insieme delle **produzioni**. Una coppia $\langle\alpha,\beta\rangle\in P$, si indica generalemtne con la notazione $\alpha\rightarrow\beta$;
4. $S\in V_n$ è detto **assioma**

La prima componete di una produzione $P$ (ovvero $\alpha$) è una qualunque stringa di caratteri **terminali** e **non terminali** mescolati, in cui deve esserci almeno un simbolo non terminale
La seconda componente (ovvero $\beta$) è una sequenza (pot. nulla) di simboli terminali e non 

**Esempio**
Si consideri la grammatica $G=\langle\lbrace a,b\rbrace,\lbrace S,B,C\rbrace,P,S\rbrace$, avente le seguenti regole di produzione:

1. $S\rightarrow aS$
2. $S\rightarrow B$
3. $B\rightarrow bB$
4. $B\rightarrow bC$
5. $C\rightarrow cC$
6. $C\rightarrow c$

Con questa grammatica si possono generalizzare le stringhe del linguaggio $$L(\mathcal G)=\lbrace a^nb^mc^h|n\geq0,m,h\geq1\rbrace$$
**Notazione**
Un insieme di produzioni aventi stessa parte sinistra

$\alpha\to\beta_1$
$\alpha\to\beta_2$
...
$\alpha\to\beta_n$
viene convenzionalmente indicato come: $$\alpha\to\beta_1|\beta_2|...|\beta_n$$
Inoltre, l'unione $V_t\cup V_n$ viene indicata con V

## $\epsilon-produzioni$
Una regola del tipo $\alpha\to\epsilon$, dove $\alpha\in V^\star\circ V_n\circ V^\star$, prende il nome di $\epsilon-produzione$ o $\epsilon-regola$

**esempio**
regola di produzione: $aBC\to\epsilon$
stringa: $BBaBCaC$ diventa $BBaC$

## Derivazioni dirette

Data una grammatica $\mathcal G=\langle V_t,V_n,P,S\rangle$, la **derivazione diretta** è una relazione su $(V^\star\circ V_n\circ V^\star)\times V^\star$ così definita:

La coppia $\langle\phi,\psi\rangle$ appartiene alla relazione se e solo se esistono $\alpha\in V^\star\circ V_n\circ V^\star\:e\:\beta,\gamma,\delta\in V^\star$ tali che :
$$\begin{cases}\phi=\gamma\alpha\delta\\\psi=\gamma\beta\delta\\\alpha\to\beta\in P\end{cases}$$
In questo caso, scriviamo $\phi\xRightarrow[\mathcal G]{}\psi$ 