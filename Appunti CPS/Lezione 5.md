# Richiami sulla parte finale dell'ultima lezione

$\Omega=\lbrace 0,1\rbrace\times...\times \lbrace 0,1\rbrace=\lbrace\omega=(\omega_1,...,1omega_n):\omega_1,...,\omega_n\in \lbrace 0,1\rbrace\rbrace$
$\mathcal A=\mathcal P(\Omega)$
P da definire (a partire dagli insiemi del tipo $\lbrace\omega\rbrace$ con $\omega\in\Omega$) per due casi:

1. n prove indipendenti con probabilità di successo p in ogni prova
2. n estrazioni casuali di un oggetto alla volta, senza reinserimento, da un insieme di $n_1$ oggetti di tipo 1, $n_2$ oggetti di tipo 2 (con $n_1+n_2\gt n$) (tipo 1 successo, tipo 2 fallimento)

Siamo interessati alla v.a X che conta il numero di successi, così definita:
$$X(\omega)=X(\omega_1,...,\omega_n)=\omega_1+...+\omega_n$$
Vogliamo trovare la densità discreta di X e si ha:
$$\forall k\in S_x=\lbrace 0,1,...,n\rbrace\:\:\:p_x(k)=\sum_{\omega:X(\omega)=k}P(\lbrace\omega\rbrace)$$

---

Nei casi 1 e 2 avremo che:
>$X(\omega)=X(\omega')\implies P(\lbrace\omega\rbrace)=P(\lbrace\omega'\rbrace)$
>Cioè, date due sequenze qualsiasi $\omega\:e\:\omega'$ con lo stesso numero di successi, le rispettive probabilità coincidono

Allora sarà conveniente dire che

$$\forall k\in S_x=\lbrace 0,1,...,n\rbrace,\exists q_k:X(\omega)=k\implies P(\lbrace\omega\rbrace)=q_k$$
**Esempio**
con n=3, esisteranno $q_0,q_1,q_2,q_3\geq0$ tali che:
$$\begin{cases}P(\lbrace 0,0,0\rbrace)=q_0\\P(\lbrace1,0,0\rbrace)=P(\lbrace0,1,0\rbrace)=P(\lbrace0,0,1\rbrace)=q_1\\P(\lbrace1,1,0\rbrace)=P(\lbrace1,0,1\rbrace)=P(\lbrace0,1,1\rbrace)=q_2\\P(\lbrace1,1,1\rbrace)=q_3\end{cases}$$
Ovviamente si dorvà avere che $q_0+3q_1+3q_2+q_3=1$

In corrispondenza, se possiamo (nuova notazione):
$$r_{n,k}=|\lbrace\omega:X(\omega)=k\rbrace|$$
per ogni $k\in S_x=\lbrace0,1,...,n\rbrace$ si ha:
$$p_x(k)=\sum_{\omega:X(\omega)=k}P(\lbrace\omega\rbrace)=\sum_{\omega:X(\omega)=k}q_k=\underbrace{q_k+...+q_k}_{r_{n,k}volte}=r_{n,k}\cdot q_k$$
Il valore di $q_k$ verrà determinato dalle ipotesi dei casi 1 e 2
Il valore di $r_{n,k}$ possiamo calcolarlo facilmente e si ha che $r_{n,k}=\binom{n}{k}$
Quindi nei casi 1 e 2 avremo $p_x(k)=\binom{n}{k}q_k\:per\:k\in\lbrace0,1,...,n\rbrace$

**Proposizione:** si ha che $r_{n,k}=\binom{n}{k}$
Dimostrazione:
Ad ogni sequenza di lunghezza n e con esattamente k volte "1" possiamo abbianre il sottoinsieme di $\{1,...,n\}$ delle posizioni degli "1":

$\underbrace{\omega=\{\omega_1,...,\omega_n\}}_{\text{tipo A}}\iff\underbrace{\{i_1,...,i_k\}\subset\{1,...,n\}}_{\text{tipo B}}$
Il numero di stringhe di tipo A è proprio : $r_{n,k}=|\lbrace\omega:X(\omega)=k\rbrace|$
I sottoinsiemi del tipo B sono in tutto $n\choose k$

Si ha cuna **corrispondenza biunivoca** tra l'insieme di sequenze e l'insieme di sottoinsiemi. Essendo una corrispondenza biunivoca tra due insiemi finiti, hanno lo stesso numero di elementi $\square$ 

**Esempio specifico della corrispondenza biunivoca**

n=4,k=2
$$\begin{align}(1,1,0,0)\to \{1,2\}\\(1,0,1,0)\to\{1,3\}\\(1,0,0,1)\to \{1,4\}\\(0,1,1,0)\to\{2,3\}\\(0,1,0,1)\to\{2,4\}\\(0,0,1,1)\to\{3,4\}\end{align}$$
A sinistra le sequenze, a destra i sottoinsiemi

Questo spiega che abbiamo $r_{4,2}=6$ sequenze binarie di lunghezza 4 e con esattamente 2 volte "q"

# Il caso 1: Distribuzione Binomiale

Si usa per la v.a che conta il numero di successi su n prove indipendenti, con probabilità di successo p in ogni prova (quindi in ogni prova c'è una probabilità di fallimento 1-p)











# Il caso 2: Distribuzione Ipergeometrica
