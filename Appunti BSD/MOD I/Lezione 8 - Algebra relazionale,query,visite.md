# Argomenti

- Linguaggi di interrogazione
- Algebra Relazionale
- Operatori insiemistici
- Ridenominazione
- Selezione
- Join
- Theta Join
- Query

# Linguaggi per base di dati

- Operazioni sullo schema
	- **DDL: Data Definition Language**
- Operazione sui dati:
	- **DML: Data Manipulation Language**
		- Interrogazione ("query")
		- Aggiornamento

## Linguaggi di interrogazione per basi di dati relazionali

- **Dichiarativi**: specificano le proprietà del risultato ("**che cosa**")
- **Procedurali**: specificano le modalità di generazione del risultato ("**come**")

## Linguaggi Relazionali

- **Algebra relazionale**: procedurale
	- Insieme di operatori
		- Su relazioni
		- Che producono relazioni
		- E possono essere composti
- **Calcolo Relazionale**: dichiarativo (teorico)
	- Basato sul calcolo dei predicati del primo ordine
	- Connettivi e clausole che consentono di descrivere la relazione del risultato
- **SQL (Structured Query Language)**: intermedio (reale)
- **QBE (Query by Example)**: dichiarativo (reale)

# Algebra Relazionale

Linguaggio procedurale, in cui le operazioni vengono descritte descrivendo la procedura per ottenere la soluzione.

**Operatori di base**: 
- **Unione,Differenza,Intersezione**: derivati dalla teoria degli insiemi
- **Ridenominazione,Selezione,Proiezione**: specifici dell'algebra relazionale
- **Join**: che può assumere diverse forme (naturale, theta-join,prodotto cartesiano)

# Operatori insiemistici

Le relazioni sono **insiemi** e quindi è naturale estendere ad esse le operazioni relative.

Tuttavia le relazioni sono insiemi di tuple **omogenee** e quindi ha senso definire ed applicare tali operatori solo a tuple **definite sugli stessi attributi**

Es. l'unione fra due relazioni su tuple non omogenee _non è_ una relazione

## Operatori derivati dagli insiemi

- **Unione**: L'unione fra due relazioni $r_1,r_2$ definite sullo stesso insieme di attributi X è indicata con $r_1\cup r_2$ ed è una relazione su X contenente le tuple che appartengono a $r_1$ o $r_2$ oppure entrambe
- **Intersezione**: L'intersezione fra due relazioni $r_1,r_2$ definite sullo stesso insieme di attributi X è indicata con $r_1\cap r_2$ ed è una relazione su X contenente le tuple che appartengono sia a $r_1$ che a $r_2$
- **Differenza**: La differenza fra due relazioni $r_1,r_2$ definite sullo stesso inisme edi attributi X è indicata con $r_1-r_2$ ed è una relazione su X contenente le tuple che appartengono a $r_1$ e non a $r_2$

Per esempio:

![[appunti bsd/mod i/immagini/Pasted image 20230113121721.png|center|600]]

# Ridenominazione

L'operazione di **ridenominazione** cambia il nome degli attributi allo scopo di facilitare operazioni insiemistiche

é un operatore che consente di modificare il nome di un attributo per poterlo associare ad un altro attributo in una operazione algebrica:
- operatore **monadico** (con argomento)
- "**modifica lo schema**" lasciando inalterata l'istanza dell'operando

SI indica con "$\rho$ nuovonome $\leftarrow$ vecchionome (Relazione)"

La ridenominazione $\rho_{B1,B2,...,Bk\leftarrow A1,A2,...,Ak}(R)$ contiene tuple $t'$ tali che $t'$ è una tupla e $t'[B_i]=t[A_i]$, cioè cambiano i nomi degli attributi ma i valori non cambiano

**Esempio**: Date le relazioni
- **Paternità** (Padre,Figlio)
- **Maternità** (Madre,Figlio)
è possibile ottenere : **$\rho$ Genitore $\leftarrow$ Padre (Paternità) $\cup$ $\rho$ Genitore $\leftarrow$ Madre (Maternità)**

**Esempio**

![[appunti bsd/mod i/immagini/Pasted image 20230113122711.png|center|500]]
![[appunti bsd/mod i/immagini/Pasted image 20230113122810.png|center|500]]

# Selezione e Proiezione

Le operazioni di **selezione** e di **proiezione** si applicano ad una relazione e ne restituiscono una porzione

Possono essere considerate ortogonali o complementari, in quanto una opera sulle **righe** el'altra sulle **colonne**

La **selezione** produce un insieme di tuple, su tutti gli attributi

La **produzione** produce un risultato definito su un inseme di attributi, cui contribuiscono tutte le tuple

![[appunti bsd/mod i/immagini/Pasted image 20230113123542.png|center|500]]

- Operatore **monadico**
- Produce un risultato che:
	- ha lo stesso schema dell'operando
	- contiene un sottoinsieme delle ennuple dell'operando che soddisfano una **specifica _condizione di selezione_**
- Si indica con $\sigma_F(r)$ o $SEL_F(r)$, dove:
	- F è una condizione da verificare
	- r è la relazione a cui la selezione è applicata definita su un insieme di attributi X

Quindi, $\sigma_F(r)$ produce una relazione sugli stessi attributi di r contenente le ennupla su cui F è vera (**semantica**)

## Selezione: Condizione di selezione

- F è una formula proposizionale su X, cioè una formula ottenuta combinando con i simboli $\land(and),\lor(or),\lnot(not)$ espressioni del tipo $A\theta B$ o $A\theta c$, dove:
	- $\theta$ è un operatore di confronto ($\leq,\lt,=,\gt,\geq$)
	- A e B sono attributi di X su cui il confronto abbia senso
	- c è una costante tale che il confronto con A sia definito
- è definito un valore di verità di F su una ennupla $t\in r$:
	- $A\theta B$ è vera se e solo se $t[A]\theta t[B]$ è vero
	- $A\theta c$ è vera se $t[A]\theta c$ è vera
	- $F_1\land F_2,F_1\lor F_2,\lnot F$ hanno l'usuale significato

**Esempio**

![[appunti bsd/mod i/immagini/Pasted image 20230113155508.png|center|500]]

![[appunti bsd/mod i/immagini/Pasted image 20230113155614.png|center|500]]

## Selezione con valori nulli

![[appunti bsd/mod i/immagini/Pasted image 20230113155721.png|center|500]]

- Perchè? Perchè le selezioni vengono valutate separatamente!
- Ma anche $$\sigma_{Età\gt30\lor Età\leq30}(Persone)\neq Persone$$
- Perchè? Perchè anche le condizioni atomiche vengono valutate separatamente!

Per riferisi ai valori nulli esistono forme apposite di condizioni:$$\begin{align}&\text{Is Null}\\&\text{Is Not Null}\end{align}$$
![[appunti bsd/mod i/immagini/Pasted image 20230113160103.png|center|500]]

# Proiezione

Dati una relazione $r(X)$ e un sottoinsieme Y di X, la proiezione di r su Y si indica con 
$$\Pi_Y(r),PROJ_Y(r)$$
l'insieme delle ennuple su Y ottenute dalle ennuple di r considerando solo i valori su Y

La proiezione $\Pi_Y(r)$ è l'insieme di tuple su un sottoinsieme Y di attributi X di R, ottenuta dalle tuple  di R considerando solo i valori su Y cioè:
$$\Pi_Y(r)=\{t[Y]:t\in r\}$$
Una proiezione ha un numero di tuple _minore o uguale_ rispetto alla relazione r cui è applicata. Il numero di tuple è uguale se e solo se **Y è superchiave per r**

**Esempio**:

Visualizzare matricola e cognome di tutti i cittadini

![[appunti bsd/mod i/immagini/Pasted image 20230113160642.png|center|500]]
 
# Join








