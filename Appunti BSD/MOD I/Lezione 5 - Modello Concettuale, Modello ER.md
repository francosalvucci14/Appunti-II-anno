# Modello dei Dati

Insieme di costrutti utilizzati per organizzare i dati di interesse e descriverne la dinamica

Componente fondamentale: **meccanismi di strutturazione** (o **costrutti di tipo**)

Come nei linguaggi di programmazione esistono meccanismi che permettono di definire tipi di dati, così ogni modello dei dati prevede alcuni costruttori
Ad esempio, il **modello relazionale** prevede il costruttore **relazione**, che permette di definire insiemi di record omogenei

- **Modelli logici**: utilizzati nei DBMS esistenti per l'organizzazione dei dati:
	- utilizzati dai programmi
	- indipendenti dalle strutture fisiche
	- esempi: **relazionale**,reticolare,gerarchico, a oggetti
- **Modelli concettuali**: permettono di rappresentare i dati in modo indipendente da ogni sistema e dal modello logico su cui è basato
	- cercano di descrivere i concetti del mondo reale
	- sibi utilizzati nelle fasi preliminari di progettazione
	- Il più noto è il modello **_Entità-Relazione_**
- Sono stati sviluppati modelli più moderni:
	- **Modello Entità-Relazione Esteso - EER** (consente l'utilizzo di costrutti più potenti e.g ereditarietà)
	- **UML**: linguaggio unificato per la progettazione dei dati e delle funzioni

## Progettazione di Basi di Dati

Progettare una base di dati significa definirne **struttura,caratteristiche e contenuto**
Prevede l'uso di opportune **metodologie**. In base al grado di **astrazione**, nella progettazione abbiamo:
- _Modello concettuale_: rappresenta la realtà dei dati e le relazioni tra essi attraverso uno schema
- _Modello logico_: descrive il modo attraverso il quale i dati sono organizzati negli archivi del calcolatore
- _Modello fisico_: descrive come i dati sono registrati nelle memorie di massa

**Rappresentazione**
![[appunti bsd/mod i/immagini/Pasted image 20221122141408.png|center|500]]

### Modello Concettuale

Rappresentazione **astratta** della realtà:
- Definire un insieme di dati presenti in natura e che rappresentano la natura stessa delle informazioni che si vogliono archiviare
- **Non esistono regole** prefissate per l'individuazione dei dati e per la loro selezione

Progettazione della base di dati:

1. Cosa c'è? (Oggetti)
2. Come si collegano o si parlano?
3. Quanti tra loro?
4. Cosa identifica gli "oggetti"?
5. Quali informazioni utili non principali?

### Modello Entità Relazioni ER

Il **modello entità relazione** è uno strumento per analizzare le caratteristiche di una realtà in modo indipendente dagli eventi che in essa accadono, cioè per costruire un modello concettuale dei dati indipendente dalle applicazioni

In particolare:
![[appunti bsd/mod i/immagini/Pasted image 20221122142017.png|center|600]]
![[appunti bsd/mod i/immagini/Pasted image 20221122142117.png|center|600]]

#### Modello ER - Entità

_Def_

Un'**entità** è un oggetto, concreto o astratto, che ha un significato anche quando viene considerato in modo isolato ed è di interesse per la realtà che si vuole modellare

**Esempio**
- le persone, un modello di automobile,i movimenti contabili, le prove sostenute da uno studente
- gli studenti sono classificabili nel tipo entità Studente (il singolo studente rappresenta unìistanza del tipo entità Studente)
- i diversi modelli di automobile sono classificabili nel tipo entità Automobile

Infatti:
![[appunti bsd/mod i/immagini/Pasted image 20221122142403.png|center|600]]

#### Modello ER - Relazione

_Def_
La **relazione(relationship)** è un legame che stabilisce unìinterazione tra le entità

**Esempio**
Tra l'entità Persona e Automobile esiste l'associazione **Possedere** (tra Automobile e Persona esiste l'associazione **Essere Posseduta** che è l'inverso) che può essere descritta nel linguaggio naturale secondo due versi:
- una persona può possedere una o più automobili
- un'automobile deve essere posseduta da una persona

Si rappresenta solo un verso della relazione
![[appunti bsd/mod i/immagini/Pasted image 20221122143122.png|center|600]]

##### Relazioni ricorsive o isA
_Def_
Le relazioni tra un'entità e se stessa si dicono **ricorsive o isA**

**Esempio**
Esempio di relazione ricorsiva sull'entità Persona è l'associazione Essere genitore nella quale Persona partecipa con il ruolo di **Genitore** e di **Figlio**
![[appunti bsd/mod i/immagini/Pasted image 20221122143627.png|center|600]]

##### Relazioni ternarie
_Def_
Le relazioni tra tre entità si dicono **ternarie**

**Esempio**
Una relazione ternaria si compone di diverse relazioni binarie
![[appunti bsd/mod i/immagini/Pasted image 20221122144046.png|center|600]]

#### Modello ER - Attributi e Chiavi

_Def (Attributi)_
Le proprietà delle entità e delle relazioni sono descritte tramite gli **attributi**. Alcune caratteristiche che descrivono il **Dominio**:
- **Formato:** Tipi di valore che assume (carattere,numerico,data/ora,etc...)
- **Dimensione:** Quantità max di caratteri o cifre inseribili
- **Opzionalità:** Possibilità di non essere sempre valorizzato

**Esempio**
Automobile ($\underline{NumeroTelaio}$,modello,produttore,cilindrata,prezzo)
![[appunti bsd/mod i/immagini/Pasted image 20221122144837.png|center|300]]

_Def_
La **chiave primaria** è un attributo o un insieme di attributi che identificano univocamente un'istanza dell'entità

**Esempio**
(chiave primaria identificata con la sottolineatura)
- Automobile ($\underline{NumeroTelaio}$,modello,produttore,cilindrata,prezzo)
- Studente ($\underline {cognome,nome}$,data nascita)

![[appunti bsd/mod i/immagini/Pasted image 20221122145253.png|center|300]]

Anche le relazioni possono avere attributi, infatti:

![[appunti bsd/mod i/immagini/Pasted image 20221122145416.png|center|600]]

Spesso, anche in presenza di chiavi palesi, si utilizza un numero progressivo come chiave primaria ovvero una chiave artificiale
Infatti:
![[appunti bsd/mod i/immagini/Pasted image 20221122145517.png|center|600]]
_Def_
Una **chiave artificiale** è formata da un attributo privo di significato proprio. Di solito consiste in un contatore che si autoincrementa ad ogni istanza che si aggiunge

**Esempio**
![[appunti bsd/mod i/immagini/Pasted image 20221122145652.png|center|600]]

#### Modello ER - Proprietà

- Ogni entità deve avere una **chiave primaria**
- L'attributo chiave primaria **non può essere opzionale**
- La chiave primaria **non può avere valori ripetuti**

Proprietà per il Dominio:
- **Tipo di dato**: intero,decimale,carattere,data,...
- **Lunghezza**: numero di cifre o caratteri per rappresentare il valore del'attributi
- **Intervallo**: Limite superiore e inferiore dei valori
- **Vincoli**: Restrizioni sui valori ammessi
- **Supporto del valore NULL**: quando non è assegnato nessun valore
- Valore di **default**
Per le chiavi primarie:
- Il valore deve essere unico e i NULL non sono ammessi
Per le chiavi esterne:
- Il tipo di dato, la lunghezza e il formato della chiave esterna devono essere uguali a quelli della corrispondente chiave primaria

##### Ritornando a [[Lezione 5 - Modello Concettuale, Modello ER#Modello ER - Entità|Modello ER - Entità]]

Esistono vari tipi di entità, alcune **forti** e altre **deboli**
_Def_
Le entità **deboli** sono le entità che non hanno una chiave primaria e devono essere associate ad un'altra entità per essere completamente significative
![[appunti bsd/mod i/immagini/Pasted image 20221122150709.png|center|600]]

- Movimento ha senso solo in relazione a Conto
- Movimento è un entità debole
- Cliente e Conto sono entità forti
- Per evitare entità deboli, si aggiunge un numero progressivo come attributo

![[appunti bsd/mod i/immagini/Pasted image 20221122150955.png|center|600]]

#### Modello ER - Molteplicità

La **molteplicità** di una relazione è il numero di possibili istanze di un'entità che sono messe in corrispondenza con un'istanza dell'altra entità:

- I valori **min** e **max** assunti dalla molteplicità sono rappresentati con : **(1,1),(1,N),(0,1),(0,N)**
- Al valore min è associato il concetto di partecipazione facoltativa **(0)** o obbligatoria **(1)**
- Il valore massimo definisce la cardinalità della partecipazione all'associazione e assume due valori  1 e N
- In relazione alla cardinalità si parla di **associazioni**:
	- **Uno a uno 1:1**
	- **Uno a molti 1:N**
	- **Molti a molti N:N**

#### Modello ER - Associazione 1:1
Un'associazione tra E1 e E2 si dice _uno a uno (1:1)_ quando a ogni istanza di E1 corrisponde una sola istanza di E2 e a ogni istanza di E2 corrisponde una sola istanza di E1
![[appunti bsd/mod i/immagini/Pasted image 20221122152709.png|center|600]]

**Esempio**
![[appunti bsd/mod i/immagini/Pasted image 20221122152854.png|center|600]]

#### Modello ER - Associazione 1:N
Un'associazione tra E1 e E2 si dice uno a molti (1:N) quando a ogni istanza di E1 corrispondono una o più istanze di E2 e a ogni istanza di E2 corrisponde una sola istanza di E1
![[appunti bsd/mod i/immagini/Pasted image 20221122153254.png|center|600]]

**Esempio**
![[appunti bsd/mod i/immagini/Pasted image 20221122153325.png|center|600]]


#### Modello ER - Associazione N:N
Un'associazione tra E1 e E2 si dice uno a molti (1:N) quando a ogni istanza di E1 corrispondono una o più istanze di E2 e a ogni istanza di E2 corrispondono una o più istanze di E1
![[appunti bsd/mod i/immagini/Pasted image 20221122153612.png|center|600]]

**Esempio**
![[appunti bsd/mod i/immagini/Pasted image 20221122153728.png|center|600]]

Manca parte IsA - Generalizzazione - Ereditarietà - UML

