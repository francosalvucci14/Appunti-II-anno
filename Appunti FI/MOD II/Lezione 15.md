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

>[!definition]- Teorema 6.24: 
>La classe coNP è **chiusa rispetto alla riducibilità polinomiale**. 

Come detto sulla dispensa, “La dimostrazione è analoga a quella del Teorema 6.21 ed è lasciata per esercizio. “

Come per tutte le classi di complessità, anche per la classe coNP possiamo definire linguaggi completi rispetto alla riducibilità polinomiale

>[!definition]- Definizione
>Un linguaggio L è coNP-completo se
>1) $L\in coNP$
>2) per ogni linguaggio $L’\in coNP$, si ha che $L’\preceq_p L$

Come abbiamo visto la scorsa lezione, i linguaggi NP-completi sono i possibili linguaggi separatori fra P e NP
- ossia, nell’ipotesi $P\neq NP$, un linguaggio NP-completo non può essere contenuto in P
- sono i linguaggi “più difficili” all’interno di NP

La stessa cosa ci proponiamo di fare nella classe coNP

Vogliamo mostrare che i linguaggi coNP-complet sono i candidati ad essere i linguaggi separatori fra NP e coNP 
- ossia che, nell’ipotesi $coNP\neq NP$ , un linguaggio coNP-completo non può essere contenuto in NP
- che i linguaggi coNP-completi sono i linguaggi “più difficili” all’interno di coNP

Questo è l’obiettivo dei prossimi due teoremi.

>[!definition]- Teorema 6.25: 
>Un linguaggio L è NP-completo se e soltanto se il suo complemento $L^c$ è coNP-completo

**Dim**
$\to$ Sia L un linguaggio NP-completo, mostriamo che $L^c$ è coNP-completo
1) $L\in  NP$ e, quindi, $L^c\in  coNP.$
2) Dobbiamo mostrare che, per ogni $L_1\in  coNP$, vale che $L_1\preceq_p L_c$
	- sia allora $L_1$ un _qualsiasi_ linguaggio in coNP (ossia, $\forall L_1\in  coNP$ ): allora, $L_1^c\in  NP$ 
	- poiché L è completo per la classe NP, allora per ogni $L_0\in  NP$, $L_0\preceq_p L$: allora, in particolare, poiché $L_1^c\in  NP$, vale che $L_1^c\preceq_p L$
	- Questo significa che esiste una funzione $f_1 : \{0,1\}^\star \to \{0,1\}^\star$ tale che $f_1\in FP$ e, per ogni $x\in \{0,1\}^\star, x\in L_1^c$ se e soltanto se $f_1(x)\in L.$
	- Ma questo è equivalente a dire che, per ogni $x\in \{0,1\}^\star, x\not\in  L_1^c$ se e soltanto se $f_1(x)\not\in  L$, 
	- quindi, per ogni $x\in \{0,1\}^\star, x\in L_1$ se e soltanto se $f_1(x)\in  L^c$
	- ossia, $L_1\preceq_p L^c$
	- **Poiché $L_1$ è un qualsiasi linguaggio in coNP**, questo dimostra che $L^c$ è completo per coNP. 

$\leftarrow$ Sia $L^c$ un linguaggio coNP-completo, mostriamo che L è NP-completo
1) $L^c\in  coNP$ e, quindi, $L\in  NP.$
2) Dobbiamo mostrare che, per ogni $L_1\in  NP$, vale che $L_1\preceq_p L$
	- sia allora $L_1$ un _qualsiasi_ linguaggio in NP (ossia, $\forall L_1\in  NP$ ): allora, $L_1^c\in  coNP$ 
	- poiché $L^c$ è completo per la classe coNP, allora per ogni $L_0\in  coNP$, $L_0\preceq_p L^c$: allora, in particolare, poiché $L_1^c\in  coNP$, vale che $L_1^c\preceq_p L^c$ 
	- Questo significa che esiste una funzione $f_1 : \{0,1\}^\star \to \{0,1\}^\star$ tale che $f_1\in FP$ e, per ogni $x\in \{0,1\}^\star, x\in L_1^c$ se e soltanto se $f_1(x)\in L^c.$
	- Ma questo è equivalente a dire che, per ogni $x\in \{0,1\}^\star, x\not\in  L_1^c$ se e soltanto se $f_1(x)\not\in  L^c$, ossia, per ogni $x\in \{0,1\}^\star, x\in L_1$ se e soltanto se $f_1(x)\in  L$ .
	- Poiché $L_1$ è un qualsiasi linguaggio in NP, questo dimostra che L è completo per NP. 

>[!definition]- Teorema 6.26: 
>Se esiste un linguaggio L NP-completo tale che $L \in coNP$, allora $NP = coNP$. 

Dimostriamo il teorema mostrando prima che
1) $coNP \subseteq NP$ e poi
2) $NP \subseteq coNP$

Sia L un qualunque linguaggio NP-completo tale che che $L\in  coNP$

(1) Poiché $L\in  NP\cap  coNP$, allora $L\in  coNP$, e, allora, $L^c\in  NP.$
- Poiché L è NP-completo allora, per il Teorema 6.25, $L^c$ è coNP-completo, 
	- quindi, per ogni $L’\in  coNP$, si ha che $L’\preceq_p L^c$. 
- Ma **NP è chiusa rispetto alla riducibilità polinomiale** (Teorema 6.22), allora, per ogni linguaggio $L’\in  coNP$, si ha che $L’\in  NP$. 
- E questo dimostra che $coNP \subseteq NP$. 

(2) Mostriamo ora l’inclusione opposta. 
- Poiché L è NP-completo allora, per ogni $L’’\in  NP$ si ha che $L’’\preceq_p  L$ 
- Poiché $L\in  NP\cap  coNP$, allora, in particolare, $L\in  coNP$. 
- Ma **coNP è chiusa rispetto alla riducibilità polinomiale** (Teorema 6.24), allora per ogni $L’’\in  NP$ si ha che $L’’\in  coNP$
- E questo dimostra che $NP \subseteq coNP$. 

Infine, le due inclusioni $coNP \subseteq NP, NP \subseteq coNP$ dimostrano il teorema. 


