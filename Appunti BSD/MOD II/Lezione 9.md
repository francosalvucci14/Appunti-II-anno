
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

