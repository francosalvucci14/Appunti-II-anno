
# Calcolo Relazionale

Notazione algebrica $\implies$ Algebra relazionale $\implies$ Linguaggio procedurale $\implies$ interrogazioni espresse applicando operatori alle relazioni 

Notazione logica $\implies$ Calcolo relazionale $\implies$ Linguaggio dichiarativo $\implies$ interrogazioni espresse tramite formule logiche le cui risposte devono essere rese vere dalle tuple

Basato sulla logica del prim’ordine
- Linguaggio formale per la rappresentazione della conoscenza 
	- Semantica non ambigua
	- Sistema formale di inferenza
Calcolo relazionale è alla base di quasi tutti i linguaggi di interrogazione esistenti e basati sul modello relazionale.

Esistono diverse versioni del calcolo relazionale, ne vedremo solo due :
- **Calcolo relazionale sui domini** (più vicino al calcolo dei predicati)
- **Calcolo relazionale sulle tuple con dichiarazioni di range** 
	- Variazione del precedente 
	- Base di molti costrutti degli attuali linguaggi

Il calcolo dei domini è una 6-pla $\{A,D,dom,s,O,F\}$
- A : Insieme degli attributi
- D : Insieme dei domini
- $Dom:A\to D$
- s : Schema di base di dati
- O : Insieme degli **operatori di confronto** $(\gt,\geq,\lt,\leq,\neq,=)$ e **logici** $(\land,\lor,\neg)$ e i quantificatori esistenziali $\exists$ e $\forall$ 
- F : Insieme delle formule corrette

## Formule corrette

>[!definition]- Definizione (Formula corretta)
>Una formula corretta è definita ricorsivamente a partire dagli atomi che sono formule corrette

**Atomi** : 
- $R(x)$ dove $R$ appartenente a s è uno shcema di relazione e x è una variabile di ennupla **(Calcolo delle Ennuple)**
- oppure
- $R(A_1:x_1,\dots,A_p:x_p)$ dove $R(A_1,\dots ,A_p)$ è uno schema di relazione appartenente a s e $x_1\dots,x_p$ sono variabili di dominio **(Calcolo dei domini)**
- $x\theta y$ o $x\theta c$, con x e y variabili di ennupla (risp. variabili di dominio), "c" è una costante e $\theta$ operatore di confronto

Se $f_1,f_2$ sono formule corrette, allora $f_1\land f_2,f_1\lor f_2,\neg f_1,(f_1)$ sono formule corrette (le parentesi sono utilizzate per alterare il normale ordine di precedenza nelle espressioni $(\neg,\land\,\lor)$ ).

Se $f$ è una formula corretta e x è una variabile di ennupla (risp. di dominio), allora $\exists x(f)$ e $\forall x(f)$ sono formule corrette

### Espressioni nel calcolo relazionale

**Un'espressione nel calcolo relazionale (query) ha la seguente forma :**
- **Calcolo dei domini** : $\{A_1:x_1,\dots,A_p:x_p|f\}$
	- $A_1:x_1,\dots,A_p:x_p$ è la **_target list_**
	- $A_1,\dots,A_p$ sono attributi distinti
	- $x_1,\dots,x_p$ sono variabili di dominio che rendono vera la formula corretta f
- **Calcolo delle ennuple** : $\{x|f\}$
	- Dove x è una variaible di ennupla che rende vera la formula corretta f

### Verità delle formule

Una formula atomica :
- $R(x)$ è **vera** sui valori di x che rappresentano ennuple di $R$ **(Calcolo delle Ennuple)**
- $R(A_1:x_1,\dots,A_p:x_p)$ è **vera** sui valori $x_1,\dots,x_p$ che formano una ennupla di $R$ **(Calcolo dei domini)**
- $x\theta y$ o  $x\theta c$ è **vera** sui valori $a_1,a_2$ tale che $a_1\theta a_2,a_1\theta c$ sono soddisfatte

La verità delle formule costruite per congiunzione, disgiunzione e negazione segue dalle regole usuali

Le fomule con i quantificatori sono vere secondo le seguenti regole : 
- $\exists x(f)$ è vera se essite **almeno** un valore a per la variabile x che rende vera la formula f
- $\forall x(f)$ è vera se per **ogni** possibile valore a per la variabile x, la formula f risulta vera

## Interrogazioni

**Esempi Vari**

![[Pasted image 20230317151410.png|center|500]]

![[Pasted image 20230317151536.png|center|600]]

## Problemi con il calcolo relazionale : Assunzione di mondo chiuso

Il calcolo relazionale ammette espressioni senza senso (sintatticamente corrette e semanticamente non valide)
- $\{A_1:x_1,A_2:x_2|R(A_1:x_1)\land(x_2=x_2)\}$
- $\{A_1:x_1|\neg(R(A_1:x_1))\}$
- Il risultato cambia al cambiare del dominio e può essere infinito se il dominio è infinito
Un linguaggio di interrogazione è **indipendente dal dominio** se il suo risultatom su ciascuna istanza di base di dati, non varia al variare del dominio rispetto al quale l'espressione è valutata

Si assume l'ipotesi di **mondo chiuso** in cui i domini sono ristretti ai valori presenti nell'istanza dello schema relazionale e alle costanti presenti nelle espressioni

Sotto questa ipotesi il calcolo relazionale è un linguaggio indipendente dal dominio

# Ritornando a calcolo relazionale

**Considerazioni :**
- un'espressione di un linguaggio di interrogazione sarebbe utile che fosse indipendente dal dominio
- Abbiamo bisogno di un'altra versione del calcolo relazionale, in cui le variabili, anzichè denotare singoli valori, denotino tuple

**Calcolo relazionale sui Domini ha dei difetti** : 
- Agisce sui domini invece che sui valori
- Per il motivo precedente diventa "verboso" (ha bisogno di tante variabili)
- Può portare a espressioni che non hanno senso
- Occorre un linguaggio che "focalizzi" le tuple di interesse

## Calcolo relazionale su tuple

**Calcolo relazioni su tuple** : 
$$\text{Espressione}:\{\text{Target List}|\text{Range List}|\text{Range List}\}$$
- **Target List** : lista degli obiettivi con elementi $Y:x.Z$ o $x.Z$ se $Z:x.Z$ o $x^\star$
- **Range List**: elenco delle variabili libere della formula con i relativi campi di variabilità
- **Formula del tipo:**
	- $x.A\theta c$ o $x.A\theta y.B$
	- connettivi di formule
	- $\exists x(R)(f)$ o $\forall x(R)(f)$

**Considerazioni**:
- Il calcolo su tupleperò non permette di esprimere tutte le interrogazioni che possono essere formulate in Algebra relazionale.
- **Esempio**: non c’è l' unione, per questo nei linguaggi interrogativi viene aggiunto esplicitamente un costrutto di unione.

### Interrogazioni

![[Pasted image 20230317152802.png|center|500]]

![[Pasted image 20230317152832.png|center|500]]

![[Pasted image 20230317152850.png|center|500]]

# Equivalenza fra i linguaggi

è possibile dimostrare che:
- Per ogni espressione del calcolo relazionale che sia indipendente dal dominio esiste un'espressione dell'algebra relazionale equivalente ad essa;
- Per ogni espressione dell'algebra relazionale esiste un'espressione del calcolo relazionale equivalente ad essa.

Dim: In modo ricorsivo a partire dagli operatori di base
