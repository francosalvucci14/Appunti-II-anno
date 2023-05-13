# Classi complemento

## Classi di complessità complemento

Torniamo un attimo al paragrafo 6.6: accanto alle classi introdotte all’inizio di questo paragrafo, possiamo considerare i corrispondenti complementi:
- $coP = \{L \subseteq \{0,1\}^\star : L^ \in P \},$
- $coNP = \{L \subseteq \{0,1\}^\star : L^c \in NP \},$ 
E, allo stesso modo, le classi
- coEXPTIME, coNEXPTIME, coPSPACE
E, in generale: 	
$$\begin{align}&coDTIME[f(n)] = \{L \subseteq \{0,1\}^\star : L^c \in DTIME[f(n)] \},\\& 		  							   	coDSPACE[f(n)] = \{L \subseteq \{0,1\}^\star : L^c \in DSPACE[f(n)] \}, 	\\&							coNTIME[f(n)] = \{L \subseteq \{0,1\}^\star : L^c \in NTIME[f(n)] \}, \\&										coNSPACE[f(n)] = \{L \subseteq \{0,1\}^\star : L^c \in NSPACE[f(n)] \}, 
\end{align}$$

Osserviamo che nella definizione delle classi di complessità complemento non viene specificato come vengono decisi (o accettati) i linguaggi che vi appartengono ma, invece, **viene specificato come vengono decisi (o accettati) i _complementi_ dei linguaggi che vi appartengono**
Tuttavia, questa differenza è irrilevante quando si parla di classi deterministiche

**Corollario 6.3**: $P = coP$ (Ma anche che $coPSPACE = PSPACE$)

Possiamo arrivare alla stessa conclusione per le classi non deterministiche?
- Cioè: possiamo utilizzare la stessa tecnica utilizzata nella dimostrazione del Teorema 6.11 nel caso non deterministico?
- Possiamo complementare gli stati di accettazione e di rigetto di una macchina NT che accetta un linguaggio L al fine di accettare il complemento di L?

Allora: è vero, anche se NP è definita come la classe dei linguaggi _accettati_ in tempo non deterministico polinomiale, i linguaggi in NP sono, in effetti, linguaggi _decisi_ da macchine non deterministiche in tempo polinomiale

Tuttavia, ricordiamo che una macchina di Turing non deterministica NT
- **accetta** un input x se **_esiste_ una computazione deterministica in NT(x) che termina in $q_A$**
- **rigetta** un input x se **_ogni_ computazione deterministica in NT(x) termina in $q_R$**

Il problema è proprio in questa asimmetria nelle definizioni di accettazione e di rigetto

## Facciamo un "gioco"

Proviamo ad applicare la stessa tecnica usata nel teorema 6.11 ad un macchina non deterministica NT
- costruiamo una nuova macchina NT’ invertendo gli stati di accettazione e di rigetto di NT
- e vediamo se NT’ accetta (oppure no) il complemento del linguaggio accettato da NT

Cominciamo scegliendo un linguaggio $L \subseteq \{0,1\}^\star$ accettato da una macchina di Turing non deterministica NT

E ricordiamo che il linguaggio complemento di L è $L^c = \{0,1\}^\star-L$
- ossia, per ogni $x\in  \{0,1\}^\star$
	- se $x\in  L$ allora $x\not\in L^c$
	- se $x\not\in L$ allora $x\in  L^c$

Allora, una macchina non deterministica $NT^c$ accetta $L^c$ se, per ogni $x\in  \{0,1\}^\star,$
- se $x\in  L$ allora $NT^c(x)$ non accetta
- se $x\not\in L$ allora $NT^c(x)$ accetta
e, quindi,
- se $x\in  L$ allora **_ogni_ computazione deterministica in $NT^c(x)$ <u>non</u> termina in $q_A$**
- se x L allora **_esiste_ una computazione deterministica in $NT^c(x)$ che termina in $q_A$**

Prima di invertire gli stati di accettazione e di rigetto di NT, costruiamo una nuova macchina $NT_1$ che, ancora, accetta L

Prendiamo NT ed aggiungiamo all’insieme delle sue quintuple le quintuple 
$$\langle q_0,s,s,q_R,F\rangle,\forall s\in\{0,1,\square\}$$
![[appunti fi/mod ii/immagini/Pasted image 20230513110917.png|center]]

$NT_1$ accetta L 
- infatti: per ogni $x\in  L$ 
	- poiché NT accetta L, allora $NT(x)$ accetta 
	- allora, esiste una computazione deterministica di NT(x) che termina in $q_A$, ma quella stessa computazione deterministica compare anche in $NT_1(x)$ 
	- e, quindi, $NT_1(x)$ accetta

![[appunti fi/mod ii/immagini/Pasted image 20230513111154.png|center]]

- e d’altra parte: per ogni $x\not\in L$ 
	- poiché NT accetta L, allora $NT(x)$ non accetta (ossia, rigetta oppure non termina)
	- allora, non esiste alcuna computazione deterministica di $NT(x)$ che termina in $q_A$, e allo stesso modo non esiste in $NT_1(x)$ una computazione deterministica che accetta
	- e, quindi, $NT_1(x)$ non accetta.

![[appunti fi/mod ii/immagini/Pasted image 20230513111404.png|center]]

Dunque, abbiamo un linguaggio $L \subseteq \{0,1\}^\star$ accettato dalla macchina non deterministica $NT_1$
- e adesso applichiamo a $NT_1$ la stessa tecnica usata nel teorema : costruiamo una nuova macchina $NT^c_1$  invertendo gli stati di accettazione e di rigetto di $NT_1$

Ci aspetteremmo che $NT^c_1$ accetti $L^c$
Vediamo: scegliamo $x\in  \{0,1\}^\star$ e poniamo $x = x_1x_2\dots x_n$

se $x\in  L^c$:
- in $NT_1(x)$ esiste la computazione deterministica $\langle q_0, x_1, x_1, q_R , F\rangle$ che termina in $q_R$
- e quella stessa computazione deterministica compare anche in $NT^c_1(x)$ che, però, in $NT^c_1$ termina in $q_A$
- allora $NT^c_1(x)$ **accetta** – Bene!

se $x\not\in L^c$ :
- se fosse vero che $NT^c_1$ decide $L^c$ allora $NT^c_1(x)$ _**non**_ dovrebbe accettare 
- ma in $NT_1(x)$ esiste la computazione deterministica $\langle q_0, x_1, x_1, q_R , F\rangle$ che termina in $q_R$
- e quella stessa computazione deterministica compare anche in $NT^c_1(x)$ che, però, in $NT^c_1$ termina in $q_A$
- allora $NT^c_1(x)$ **accetta** – $NT^c_1(x)$ _**non**_ dovrebbe accettare se $x\not\in L^c$!

Invece, $NT^c_1(x)$ **accetta qualunque sia x**!

E quindi $NT^c_1$ non accetta $L^c$.

Allora: anche se i linguaggi in NP sono, in effetti, linguaggi _decisi_ da macchine non deterministiche in tempo polinomiale, il fatto che una macchina di Turing non deterministica NT
- **accetta** un input x se **_esiste_ una computazione deterministica in NT(x) che termina in $q_A$**
- **rigetta** un input x se **_ogni_ computazione deterministica in NT(x) termina in $q_R$**

cioè, questa asimmetria nelle definizioni di accettazione e di rigetto non permette di derivare una macchina che decide $L^c$ invertendo gli stati di accettazione e di rigetto di una macchina non deterministica che decide L

E questo significa che **non possiamo affermare che $coNP = NP$**

Ma, tutto questo ragionamento, ci permette forse di affermare che $coNP\neq NP$?
Assolutamente no!

E quindi?

## Questioni di congetture

Abbiamo detto più volte che la maggior parte delle inclusioni fra classi di complessità sono inclusioni deboli
- nelle quali non si riesce a dimostrare che le due classi sono diverse
- ma non si riesce nemmeno a dimostrare che le due classi sono uguali!

Il caso più famoso è quello che riguarda le classi P e NP
- sappiamo che $P \subseteq NP$ – e, quindi, che ogni problema in P è contenuto anche in NP
- ma non sappiamo se $P = NP$ – ossia, se ogni problema in NP è contenuto, in effetti, in P
- né sappiamo se $P\neq NP$ – ossia, se esiste un problema in NP che non è contenuto in P

La **prima congettura fondamentale della teoria della complessità computazionale** ipotizza che $$P\neq NP$$
Ed ora abbiamo appena scoperto una nuova congettura:
La **seconda congettura della teoria della complessità computazionale** ipotizza che $$coNP\neq NP$$
### Relazioni fra le due congetture

In effetti, comunque, le due congetture non sono del tutto indipendenti, come descritto nel prossimo teorema

>[!definition]- Teorema 6.23: 
>Se $P = NP$ allora $NP = coNP$. 

**Dimostrazione**: 
- per il Corollario 6.3, P = coP
- per ipotesi: P = NP e quindi coP = coNP
- allora: NP = P = coP = coNP															

Il teorema afferma che: se è **_falsa_ la Prima Congettura Fondamentale della Teoria della Complessità Computazionale allora è falsa anche la Seconda Congettura della Teoria della Complessità Computazionale**

Questo teorema può anche essere letto come: se $NP\neq  coNP$ allora $P\neq  NP$
- ossia: se è **_vera_ la Seconda Congettura della Teoria della Complessità Computazionale allora è vera anche la Congettura Fondamentale della Teoria della Complessità Computazionale** 

L’affermazione inversa “se NP = coNP allora P = NP” non è invece stata dimostrata
Per questo le due congetture sono, fino ad ora, due <u>congetture distinte</u>

## Struttura della classe coNP

