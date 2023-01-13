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


