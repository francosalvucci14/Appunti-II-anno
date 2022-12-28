# Automi a pila non deterministici

Un **automa a pila non deterministico** è definito come una settupla $\mathcal M=\langle\Sigma,\Gamma,Z_0,Q,q_0,F,\delta\rangle$ dove $\Sigma$ è l'**alfabeto in input**, $\Gamma$ è l'**alfabeto dei simboli della pila**, $Z_0\in\Gamma$ è il **simbolo iniziale di pila**, Q è un insieme finito e non vuoto di **stati**, $q_0\in Q$ è lo **stato iniziale**, $F\subseteq Q$ è l'**insieme degli stati finali**, $\delta:Q\times(\Sigma\cup\{\varepsilon\})\times\Gamma\to\mathcal P(Q\times\Gamma^\star)$ è la **funzione (parziale) di transizione**

**Oss**
$\mathcal P(Q\times\Gamma^\star)$ è l'insieme potenza di $Q\times\Gamma^\star$

Nel caso degli automi a pila la presenza del non determinismo comporta un aumento del potere computazionale

Mentre gli automi a pila non deterministici riconoscono la classe dei linguaggi non contestuali, gli automi a pila deterministici riconoscono un sottoinsieme proprio di tali linguaggi, la classe dei linguaggi non contestuali deterministici

**Esempio**: accettazione del linguaggio non contestuale $\{w\hat w|w\in\{s,b\}^+\}$, dove $\hat w$ indica la stringa riflessa di $w$  

**Esempio di accettazione per pila vuota**

Tabella di transizione dell’automa a pila che accetta per pila vuota il linguaggio $\{w\hat w|w\in\{s,b\}^+\}$

![[appunti fi/mod i/immagini/Pasted image 20221217162459.png|center|550]]

**Esempio di accettazione per stato finale**

Tabella di transizione dell’automa a pila che accetta per stato finale il linguaggio $\{w\hat w|w\in\{s,b\}^+\}$ con $q_f=q_2$

![[appunti fi/mod i/immagini/Pasted image 20221217162904.png|center|550]]

## Equivalenza tra condizioni di accettazione

>[!important]- Teorema
>Dato un automa a pila non deterministico $\mathcal M=\langle\Sigma,\Gamma,Z_0,Q,q_0,F,\delta\rangle$ che accetta un linguaggio per stato finale,esiste un automa a pila non deterministico $\mathcal M'=\langle\Sigma',\Gamma',Z_0',Q',q_0',\emptyset,\delta'\rangle$ che accetta lo stesso linguaggio per pila vuota, vale a dire tale che $L(\mathcal M)=N(\mathcal M')$

$\mathcal M'$ opera in modo simile a $\mathcal M$ , secondo lo schema seguente:

1. All’inizio $\mathcal M'$ ha nella pila un simbolo speciale $X$ non appartenente a $\Gamma$ ed inserisce al di sopra di $X$ il simbolo $Z_0$
2. Quindi,$\mathcal M'$ esegue gli stessi passi di $\mathcal M$. Si noti che nel corso di tale fase la pila di $\mathcal M'$ non sarà mai vuota
3. Se, alla fine della stringa di input,$\mathcal M$ raggiunge un suo stato finale (che quindi è raggiuntoanche da $\mathcal M'$),$\mathcal M'$ provvede ad eliminare tutti i simboli presenti in pila, incluso $X$


$\mathcal M'$ è allora definito come $\Sigma'=\Sigma,\Gamma'=\Gamma\cup\{X\}(X\not\in\Gamma),Z_0'=X,Q'=Q\cup\{q_0',q_f\}(q_0',q_f\not\in\Gamma)$ e, per quanto riguarda la funzione di transizione $\delta'$:

1. $\delta'(q,a,Z)=\delta(q,a,Z)$ per ogni $q\in Q,a\in\Sigma,Z\in\Gamma$
2. $\delta'(q,\varepsilon,Z)=\delta(q,\varepsilon,Z)$ per ogni $q\in Q-F,Z\in\Gamma$
3. $\delta'(q,\varepsilon,Z)=\delta(q,\varepsilon,Z)\cup\{(q_f,\varepsilon)\}$ per ogni $q\in F,Z\in\Gamma$
4. $\delta'(q_0',\varepsilon,X)=\{(q_0,Z_0X)\}$
5. $\delta'(q_f,\varepsilon,Z)=\{(q_f,\varepsilon)\}$ per ogni $Z\in\Gamma'$

A questo punto si avrà che:

- Per l'effetto di 1 e 2 $\mathcal M'$ simula perfettamente $\mathcal M$ se questo non si trova in uno stato finale
- Per l'effetto di 1 e 3 $\mathcal M'$ in uno stato finale può eseguire tutte le transizioni definite per $\mathcal M$ con l'ulteriore possibilità di effettuare una $\varepsilon$-transizione verso il suo stato $q_f$ lasciando la pila immutata
- La condizione 4 fa si che il simbolo $X$ rimanga in fondo alla pile mentre l'automa $\mathcal M'$ effettua la simulazione di $\mathcal M$
- La condizione 5 assicura lo svuotamento della pila di $\mathcal M'$ nel caso in cui $\mathcal M$ raggiunga uno stato finale

>[!important]- Teorema
>Dato un automa a pila non deterministico $\mathcal M=\langle\Sigma,\Gamma,Z_0,Q,q_0,F,\delta\rangle$ che accetta un linguaggio per pila vuota,esiste un automa a pila non deterministico $\mathcal M'=\langle\Sigma',\Gamma',Z_0',Q',q_0',\emptyset,\delta'\rangle$ che accetta lo stesso linguaggio per stato finale, vale a dire tale che $N(\mathcal M)=L(\mathcal M')$

$\mathcal M'$ opera in modo simile a $\mathcal M$ , secondo lo schema seguente:

1. All’inizio $\mathcal M'$ ha nella pila un simbolo speciale $X$ non appartenente a $\Gamma$ ed inserisce al di sopra di $X$ il simbolo $Z_0$
2. Quindi,$\mathcal M'$ esegue gli stessi passi di $\mathcal M$. Si noti che nel corso di tale fase la pila di $\mathcal M'$ non sarà mai vuota
3. Se, alla fine della stringa di input, $\mathcal M$ raggiunge la condizione di pila vuota, $\mathcal M'$ entra nello stato finale $q_f$

$\mathcal M'$ è allora definito come $\Sigma'=\Sigma,\Gamma'=\Gamma\cup\{X\}(X\not\in\Gamma),Z_0'=X,Q'=Q\cup\{q_0',q_f\}(q_0',q_f\not\in\Gamma)$ e, per quanto riguarda la funzione di transizione $\delta'$:

1. $\delta'(q,a,Z)=\delta(q,a,Z)$ per ogni $q\in Q,a\in\Sigma\cup\{\varepsilon\},Z\in\Gamma$
2. $\delta'(q,\varepsilon,Z)=\{(q_f,X)\}$ per ogni $q\in Q$
3. $\delta'(q_0',\varepsilon,X)=\{(q_0,Z_0X)\}$

A questo punto si avrà che: 

- Per effetto di 1, $\mathcal M'$ simula perfettamente $\mathcal M$ se la pila di questo non è vuota
- Per effetto di 2 $\mathcal M'$, se la pila di $\mathcal M$ è vuota (e quindi la propria contiene solo $X$), può effettuare una $\varepsilon$-transizione verso il suo stato finale $q_f$ lasciando la pila immutata
- La 3 fa si ch il simbolo $X$ rimanga in fondo alla pila mentre l'automa $\mathcal M'$ effettua la simulazione di $\mathcal M$

## Equivalenza CFG-NPDA

Se un linguaggio è generato da una grammatica $\mathcal G$ non contestuale, esiste un automa a pila non deterministico $\mathcal M$ tale che $L(\mathcal G)=N(\mathcal M)$

La dimostrazione è costruttiva: a partire da $\mathcal G$ deriviamo $\mathcal M$ e poi mostriamo l'equivalenza

### $\varepsilon\not\in L(\mathcal G)$

Consideriamo dapprima il caso in cui $\varepsilon\not\in L(\mathcal G)$. A partire da $\mathcal G$, costruiamo una grammatica $\mathcal G'=\langle\Sigma,V_N',P',S'\rangle$ equivalente a $\mathcal G$, ma in Forma Normale di Greibach

Per l'automa, poniamo $\Gamma=V_N',Q=\{q_0\},Z_0=S'$

Funzione di transizione: per ogni produzione $A\to a\gamma,\gamma\in(V_N')^\star$ introduciamo la regola $\delta(q_0,a,A)=(q_0,\gamma)$ (più precisamente si ha che $(q_0,\gamma)\in\delta(q_0,a,A)$)

L'equivalenza deriva dalla dimostrazione che 
$$(q,x,S')\vdash^\star(q,\varepsilon,\alpha)$$
se e solo se $S'\xRightarrow[]{\star}x\alpha$, dove $q\in Q,x\in\Sigma^\star,\alpha\in(V_N')$

**Dimostrazione**

In due passi:

1. Dimostrazione, per induzione su i (numero di passi della computazione), che se $$(q,x,S')\vdash^i(q,\varepsilon,\alpha)\implies S'\xRightarrow[]{\star}x\alpha$$
2. Dimostrazione, per induzione su i (numero di passi della derivazione), che se $$S'\xRightarrow[]{\star}x\alpha\implies (q,x,S')\vdash^\star(q,\varepsilon,\alpha)$$
$\square$


### $\varepsilon\in L(\mathcal G)$

Se $\varepsilon\in L(\mathcal G)$ possiamo costruire una grammatica $\mathcal G'$ in GNF che genera il linguaggio $L(\mathcal G')=L(\mathcal G)-\{\varepsilon\}$ e quindi applicare la procedura descritta per ottenere un automa a pila $\langle\Sigma,\Gamma,Z_0,\delta,\{q_0\},\emptyset\rangle$ che riconosce $L(\mathcal G')$

Un automa che riconosce $L(\mathcal G)$ può essere ottenuto aggiungendo un nuovo stato iniziale $q_0'$ e la transizione $\delta(q_0',\varepsilon,Z_0)=\{(q_0',\varepsilon),(q_0,Z_0)\}$




