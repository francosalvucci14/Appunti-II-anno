# Progettazione di una base di dati

Progettare una base di dati significa definirne struttura, caratteristiche e contenuto. E quindi prevede l'uso di opportune metodologie. In base al grado di astrazione, la progettazione prevede:

- **Modello concettuale**: rappresenta la realtà dei dati e le relazioni tra essi attraverso uno schema
- **Modello logico**: descrive il modo attraverso il quale i dati sono oragnizzati negli archivi del calcolatore
- **Modello fisico**: descrive come i dati sono registrati nelle memorie di massa

## Modello logico

Obiettivo della fase di progettazione logica è pervenire, **a partire dallo schema concettuale**, a uno schema logico che lo rappresenti in modo fedele, "efficiente" e indipendente dal particolare DBMS adottato. A tal fine questa fase di progettazione può essere suddivisa in 2 passi:
1. **Ristrutturazione dello schema Entità-Relazione**: è una fase indipendente dal modello logico e si basa su criteri di ottimizzazione dello schema
2. **Traduzione verso il modello logico**: fa riferimento ad uno specifico modello logico (**modello relazionale**)

## Ciclo di vita di un sistema informativo

1. **Studio di fattibilità**: definisce le varie alternative possibili,i relativi costi e le priorità di realizzazione
2. **Raccolta e analisi dei requisiti**: individua proprietà e funzionalità del sistema tramite interazione con gli utenti e definizione informale dei dati e delle operazioni
3. **Progettazione**: divisa in progettazione dei dati e progettazione delle applicazioni. Individua struttura e organizzazione dei dati e caratteristiche degli applicativi che vi dovranno accedere
4. **Implementazione**: realizza la base di dati e il codice dei programmi conformemente alle specifiche
5. **Validazione e collaudo**: verifica il corretto funzionamento del sistemas informativo
6. **Funzionamento**: il sistema informativo diviene operativo

![[appunti bsd/mod i/immagini/Pasted image 20221221145532.png|center|600]]


## Fasi della progettazione

- **Progettazione concettuale**: rappresenta le specifiche informali in modo formale e completo, ma indipendente dalla rappresentazione usata nei DBMS. Produce lo schma concettuale e fa riferimento ad un modello concettuale dei dati. Rappresenta il contenuto informativo e non la codifica
- **Progettazione logica**: traduce lo schema concettuale nello schema logico basato su un modello logico (es. relazionale) ancora indipendente dalla realizzazione fisica della base di dati
- **Progettazione fisica**: completa lo schema logico con la specifica dei parametri fisici di memorizzazione dei dati. Produce uno schema fisico e fa riferimento ad un modello fisico dei dati,dipendente dal DBMS

![[appunti bsd/mod i/immagini/Pasted image 20221221145847.png|center|600]]

## Specifiche

Si distinguono le **specifiche dei dati** e le **specifiche sulle operazioni**

- **Progettazione concettuale**: si usano le specifiche sui dati; quelle sulle operazioni servono a verificare che lo schema concettuale contenga tutte le informazioni necessarie alla loro esecuzione
- **Progettazione logica**: lo schema concettuale riassume le specifiche sui dati, le specifiche sulle operazioni si usano per ottenere uno schema logico che permetta di eseguirle in modo efficiente. Bisogna conoscere il modello ma non il DBMS adottato
- **Progettazione fisica**: si usano lo schema logico e le specifiche sulle operazioni per implementare il sistema in modo efficiente

## Progettazione concettuale

Il prodotto è uno schema E-R che descrive le specifiche sui dati relative ad una applicazione.

Si può suddividere in due fasi:

- **Raccolta e analisi dei requisiti**
	- Individuazione dei problemi da risolvere
	- Chiarimento ed organizzazione delle specifiche
- **Definizione dello schema E-R**

### Raccolta e analisi dei requisiti

I **requisiti** definiscono le caratteristiche dell'applicazione da realizzare (dati, operazioni)
I requisiti spesso sono espressi con frasi in linguaggio naturale spesso ambigue e disorganizzate
L'analisi consiste nel chiarimento e nell'organizzazione delle specifiche

- Il reperimento dei requisiti è un'attività difficile e non standardizzabile
- L'attività di analisi inizia con i primi requisiti raccolti spesso indirizza verso altre acquisizioni

Realizzazione di una descrizione del problema in linguaggio naturale che rispetti criteri di comletezza e non ambiguità

- corretto livello di astrazione
- frasi standardizzate
- semplicità dele specifiche (evitare frasi contorte)
- eliminazione di sinonimi o omonimi
- esplicitazione dei riferimenti fra termini
- glossario dei termini

Per i **dati**, specificare in numero delle **occorrenze** previste
Per le **operazioni**, specificare il **numero di volte** che si prevede che debbano essere eseguite in un certo arco di tempo

#### Fonti dei requisiti

- **Utenti** (interviste,documentazione scritta)
- **Documentazione esistente** (normative, leggi e regolamenti del settore, regolamenti interni, procedure aziendali, moduli)
- **Realizzazioni preesistenti** (applicativi da rimpiazzare, applicazioni che dovranno interagire col sistema da realizzare)

#### Interazione con gli utenti

- Utenti diversi possono fornire informazioni diverse
- Utenti a livello più alto hanno spesso una visione più ampia ma meno dettagliata
- Le interviste portano spesso ad una acquisizione dei requisiti "per raffinamenti successivi"
	- effettuare spesso verifiche di comprensione e coerenza
	- verificare anche per mezzo di esempi (generali e relativi a casi limite)
	- richiedere definizioni e classificazioni
	- far evidenziare gli aspetti essenziali rispetto a quelli marginali

Vedi esempio1 -> [Esempio 1](http://www.informatica.uniroma2.it/upload/2022/BDC/08-Progettazione.pdf#page=15)

Vedi esempio2 -> [Esempio 2-Più articolato](http://www.informatica.uniroma2.it/upload/2022/BDC/08-Progettazione.pdf#page18)

### Criteri di rappresentazione

- Rappresentare mediante **entità** classi di oggetti con esistenza autonoma e caratterizzati da proprietà significative
- Rappresentare mediante **attributi** gli oggetti con struttura semplice e che non rappresentino proprietà rilevanti
- Rappresentazione mediante **relazioni** concetti che associano più entità precedentemente identificate
- Rappresentazione mediante **generalizzazioni** concetti che risultino essere casi particolari di altri

## Strategie di progetto

Si possono utilizzare le strategie tipiche dello sviluppo di un processo di ingegnerizzazione (es. ingegneria del software)

- Strategie top-down
- Strategie bottom-up
- Strategie inside-out
- Approcci misti

### Strategia top-down

A partire da uno schema che descrive le specifiche mediante pochi concetti molto astratti, si produce uno schema concettuale mediante raffinamenti successivi che aggiungono via via più dettagli.

I raffinamenti successivi, come accade anche per altre strategie, vengono realizzati mediante trasformazioni elementari, denominate _primitive di trasformazione top-down_ che trasformano un concetto di uno schema in una struttura più complessa che descrive la realtà in maggiore dettaglio

![[appunti bsd/mod i/immagini/Pasted image 20221221152107.png|center|500]]

#### Primitive di trasformazione top-down

- **T1, _da entità a relazione fra entità_**: si applica quando si verifica che una entità descrive due concetti diversi legati logicamente fra loro
- **T2, _da entità a generalizzazione_**: si applica quando una entità è composta da sotto-entità distinte o,più in generale, che uno stesso concetto può in realtà comprendere più concetti
- **T3, _da relazione a insieme di relazioni_**: si applica quando una relazione descrive in realtà due o pià relazioni fra le medesime entità; tipicamente le due relazioni sono due specializzazioni di una relazione più generale
- **T4, _da relazione ad entità con relazioni_**: si applica quando una realzione descrive un concetto con esistenza autonoma ai fini dell'applicazione o concetti di cui si possono avere più occorrenze
- **T5, _introduzione di attributi in una entità_**: si applica per introdurre nuovi attributi ad una entità, che aiutino a descriverla in modo più completo
- **T6,_introduzione di attributi su relazioni_**: si applica per aggiungere proprietà a relazioni

![[appunti bsd/mod i/immagini/Pasted image 20221221152609.png|center|400]]

### Strategia bottom-up





