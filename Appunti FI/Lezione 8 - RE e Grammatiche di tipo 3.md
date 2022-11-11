# Espressioni Regolari

>**Teorema**
>Tutti i linguaggi definiti da espressioni regolari sono regolari

>**Teorema**
>Data una grammatica $\mathcal G$ di tipo 3, esiste una espression regolare $r$ tale che $L(\mathcal G)=L(r)$, che descrive cioè il linguaggio generato da $\mathcal G$

Consideriamo una grammatica $\mathcal G$ di tipo 3 e il linguaggio $L$ da essa generato, che per semplicità assumiamo non contenga la stringa vuota $\varepsilon$

Se così non fosse, applichiamo le considerazioni seguenti al linguaggio $L-\lbrace\varepsilon\rbrace$, anch'esso regolare: una volta derivata un'espressione regolare $r$ che lo definisce, l'espressione regolare che definisce $L$ sarà chiaramente $r+\varepsilon$

Alla grammatica $\mathcal G$ possiamo far corrispondere un sistema di equazioni su espressioni regolari

Estensione del linguaggio delle espressioni regolari con variabili $A,...,Z$, associando una variabile ad ogni non terminale in $\mathcal G$

Tali variabili potranno assumere valori nell'insieme delle espressioni regolari

Raggruppamento di tutte le produzioni che presentano a sinistra lo stesso non terminale. Per ogni produzione del tipo $$A\to a_1B_1|a_2B_2|...|a_nB_n|b_1|b_2|...|b_m$$abbiamo un equazione del tipo:
$$A=a_1B_1+a_2B_2+...+a_nB_n+b_1+b_2+...+b_m$$

Da una grammatica regolare si ottiene un sistema di **equazioni lineari destre**, in cui ogni monomio contiene una variabile a destra di simboli terminali