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

