# Porte Logiche
Quando si parla di circuiti si usa una notazione diversa per esprimere gli stessi concetti che abbiamo utilizzato nella logica proprosizionale: per esempio indichiamo con 0 e 1, False e True, rispettivamente.

![[appunti lrl/immagini/img31.png|center|400]]



Quando si parla di circuiti non si utilizza mai il simbolo $\implies$ ma possiamo esprimere p $\implies$q come $\bar{p}+q$ .
in logica generalmente non si usa un simbolo specifico per lo XOR, mentre quando si parla di circuiti si usa a tale scopo $p\oplus q$ .

Si hanno a disposizione delle porte logiche, che implementeranno le operazioni logiche elementari, AND, OR e NOT, senza preoccuparci della loro composizione elettrotecnica.

![[appunti lrl/immagini/img32.png|center|400]]

Data una formula $\mathcal F$ della logica proposizionale, possiamo sempre costruire un circuito che implementi  $\mathcal F$ usando porte logiche elementari. Per esempio, la formula $x_{0}\implies(x_{1}\land x_2)$ è equivalente alla formula $\bar x_{0}\lor(x_{1}\land x_2)$, quindi un circuito che la implementa è 

![[appunti lrl/immagini/img33.png|center|400]]

In aggiunta alle porte logiche elementari, possiamo assumere di avere porte logiche che implementano operazioni binarie più comuni, per esempio

![[appunti lrl/immagini/img34.png|center|400]]

# Operazioni Aritmetiche

Si possono utilizzare le porte logiche per creare circuiti che eseguono operazioni aritmetiche.
## Ex: 
Costruiamo un circuito con tre input a, b, c e due output s e $c_{out}$ con le seguenti tabelle di verità 

![[appunti lrl/immagini/img35.png|center|400]]

La tabella di s è uno XOR mentre quella di c è un AND, quindi possiamo disegnare il circuito così

![[appunti lrl/immagini/img36.png|center|400]]

In questo circuito l'output s è proprio la somma dei due bit di input, mentre l'output c'è il riporto. Un tale circuito si chiama Half Adder.
Ricordiamo come facciamo la somma di due numeri espressi in binario.

# Forme normali e circuiti

Una formula si dice in forma normale disgiuntiva (DNF) se è una disgiunzione di clausole  
congiuntive $C_1 \lor C_2 \lor \dots\lor C_n$ dove ogni clausola è una congiunzione di letterali $C_i = l_{i,1} \land l_{i,2} \land\dots\land l_{i,k_i}$ e ogni letterale è una variabile oppure una variabile negata. 
Per  esempio,  
$$(p ∧ q ∧ ¬r) ∨ (¬p ∧ q ∧ ¬r) ∨ (p ∧ q ∧ r) (1)  $$
è in forma normale disgiuntiva. Data una formula X esiste sempre una formula Y  
equivalente a X in forma normale disgiuntiva.  
Nel linguaggio che usiamo per i circuiti chiamiamo forma normale _**somma di prodotti**_ la forma normale disgiuntiva. Infatti osservate che se scriviamo la formula in (1) usando  
la simbologia che abbiamo introdotto per i circuiti otteniamo  
$$pq ̄r + ̄pq ̄r + pqr (2)  $$
Una formula si dice in forma normale congiuntiva (CNF) se è una congiunzione di  
clausole disgiuntive (dette anche semplicemente clausole) $D_1 \land D2_ \land\dots\land D_n$ dove ogni  
clausola è una disgiunzione di letterali $D_i = l_{i,1} \lor l_{i,2} \lor\dots\lor l_{i,k_i}$ e ogni letterale è una  
variabile oppure una variabile negata. Per esempio,  
$$(p ∨ q ∨ ¬r) ∧ (¬p ∨ q ∨ ¬r)  $$
è in forma normale congiuntiva. Data una formula X esiste sempre una formula Y  
equivalente a X in forma normale congiuntiva.  
Nel linguaggio che usiamo per i circuiti chiamiamo forma normale _**prodotto di somme**_ la forma normale congiuntiva

Se si ha una formula in forma normale è immediato ricavare un circuito e disegnarlo in un modo "standard" . Per esempio, data la seguente tabella di verità

![[appunti lrl/immagini/img37.png|center|400]]

si può scrivere una formula in forma normale somma di prodotti $$y = x_{0}\bar x_{1} \bar x_{2} +x_{0} x_{1} \bar x_{2} + x_{0} x_{1} x_{2}$$ 
e disegnare un circuito che la implementa

![[appunti lrl/immagini/img38.png|center|400]]