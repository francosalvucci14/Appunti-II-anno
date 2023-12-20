
# Indice degli argomenti

- Componenti
- Motivazioni
- Obiettivi
- Raccolta dei dati
- Schemi

# Progetto VRoomA
## Componenti del gruppo

| Nome | Cognome | Matricola | Mail |
| -------- | -------- | --------- | ------------------------------------- |
| Leonardo | Ascenzi | 0310858 | leonardo.ascenzi@students.uniroma2.eu |
| Franco | Salvucci | 0306604 | franco.salvucci@students.uniroma2.eu |
| Nicolò | Spadoni | 0311175 | nicolo.spadoni@students.uniroma2.eu | | | | |
## Motivazioni

Il database che stiamo realizzando è incentrato all'implementazione di un software dedicato all'organizzazione di viaggi tramite taxi.
## Obiettivi

L'obiettivo principale di questo sistema è permettere agli utenti di organizzare gli spostamenti tramite taxi a seconda delle proprie esigenze, del tipo di veicolo scelto e del costo della tratta scelta.

Da un punto di vista societario, gli obiettivi sono quelli di valutare la qualità del lavoro degli autisti tramite i feedback forniti dai clienti e migliorare dove possibile il servizio.

## Raccolta dei dati

### Analisi dei requisiti

I **ruoli aziendali** sono i seguenti:
- Addetti Marketing
- Autisti
- Manutentori

Gli **addetti al marketing** possono inserire, previa autorizzazione da parte degli amministratori della società, delle **promo** che prevedono sconti sulle corse per gli utenti del sistema.

Gli **autisti** potranno scegliere se accettare o rifiutare la corsa, specificando in questo caso la motivazione del rifiuto.
Inoltre potranno lasciare un **feedback** all'utente riguardo il comportamento prima e durante la corsa.
Ogni **autista** ha la propria macchina privata, e può contattare i manutentori aziendali in caso di guasto del veicolo.
Ad ogni **autista** sono assegnati uno o più **turni** di lavoro, con il vincolo che il singolo autista non può essere assegnato a due turni lavorativi che hanno orario inizio e orario fine uguali.

I **manutentori** possono ricevere richieste di assistenza da parte degli autisti e contattare le officine convenzionate per effettuare il lavoro di assistenza.
Le **officine** non fanno parte della società.

Le tipologie di **veicolo** disponibili sono le seguenti:
- Base: 4 posti disponibili
- Plus: 7 posti disponibili, adibito a trasporto di carrozzine per disabili
- Premium: 12 posti disponibili, adibito a trasporto di carrozzine per disabili

Ogni **veicolo**, identificato in modo univoco dalla targa, per poter circolare, deve essere assicurato.

Quando si prenota una **corsa** (**tratta**) si possono scegliere due punti:
- Punto di Partenza, identificato come Punto di raccolta
- Punto di Arrivo, identificato come Punto di rilascio

Ogni **prenotazione** può essere accettata o rifiutata in base a determinate esigenze dell'**utente** (Es: prenotazione effettuata per errore) e dell'**autista** (Es: indisponibilità al servizio).
Ad ogni tratta completata è associato un feedback che può essere lasciato sia dall'**utente** che dall'**autista**.

Ogni **utente** ha diritto a ricevere **offerte** da poter usare al momento della prenotazione.
Può effettuare illimitate richieste di **prenotazione**, in base alle necessità personali (numero di passeggeri, persone con disabilità, punto di ritiro, punto di rilascio), con il vincolo di una corsa per volta.
A corsa completata l'**utente** può lasciare un **feedback** con un numero di stelle (da 1 a 5) e un commento.
Ogni **utente** deve aggiungere una **carta** con cui effettuare il pagamento relativo alla tratta effettuata, in un secondo momento potrà aggiungere altri metodi di pagamento secondo le proprie esigenze.
Ogni **utente** può aggiungere alla lista dei preferiti ua qualunque delle tratte effettuate da lui, scegliendo se aggiungere solo la tratta o anche l'autista.
Ogni **utente** può accedere alla cronologia delle prenotazioni effettuate.

### Glossario delle entità


| Entità | Descrizione | Attributi | Relazioni Coinvolte |
| ---------------------- | ----------------------------------------------------------------- | ------------------------- | --------------------------------------------------------------------------------- |
| Personale | Membri totali della società | **ID**, Nome, Cognome, DDN, Numero di Telefono, Email | Addetti Marketing, Manutentori, Autisti |
| Patente | Descrive tutte le info riguardanti la patente degli autisti | **Numero Patente**, DDS, Categoria | Autisti |
| Offerte | Serie di offerte che vengono proposte al singolo utente | **ID**, Promo Code, Info Offerta, | Utenti, Addetti Marketing |
| Manutentori | Addetti alla manutenzione delle auto degli autisti | **ID**, Qualifica | Personale, Autisti |
| Autisti | Personale che svolge il ruolo di autista delle auto nella società | **ID**, Stipendio | Patente, Manutentori, Veicoli, Turni, Richiesta Prenotazione, Personale, Feedback |
| Veicoli | Auto utilizzate per il servizio di taxi | **Targa**, Marca, Modello, Posti disponibili | Autisti, Assicurazione |
| Turni | Turni lavorativi che riguardano gli autisti | **ID**, Orario inizio, Orario fine | Autisti |
| Richiesta Prenotazione | Richieste di prenotazioni effettuate da parte dall'utente | **ID**, Punto di raccolta, Punto di rilascio, Orario richiesta, Numero Passeggeri | Autisti, Utenti, Tratte Complete, Tratte Rifiutate |
| Utenti | Utenti utilizzatori del servizio taxi | **ID**, Nome, Cognome, Email, Password, Abbonamento | Carta, Richiesta Prenotazione, Offerte, Feedback, Tratte completate |
| Feedback | Recensioni lasciate dall'utente e dagli autisti | **ID**, Stelle, Commento, Data | Tratte Completate, Utenti, Autisti |
| Tratte Completate | Corse effettuate portate a termine con successo | **ID**, Costo | Richiesta Prenotazione, Feedback, Carta, Utenti |
| Tratte Rifiutate | Corse rifiutate da parte dell'autista per determinati motivi | **ID**, Motivazione | Richiesta Prenotazione |
| Carta | Carta di credito personale dell'utente | **Numero Carta**, Data di Scadenza, CVV | Utenti, Tratte completate |
| Assicurazione | Dati dell'assicurazione associata al singolo veicolo | **ID**, Data di scandenza, Tipo | Veicoli |
| Addetti Marketing | Personale addetto al reparto marketing della società | **ID**, Ruolo | Offerte, Personale |

### Glossario dei termini

| Entità | Descrizione | Sinonimi |
| ---------------------- | ----------------------------------------------------------------- | ------------------------- |
| Personale | Membri totali della società | Organigramma |
| Patente | Descrive tutte le info riguardanti la patente degli autisti | Licenza di Guida |  |
| Offerte | Serie di offerte che vengono proposte al singolo utente | Promozioni |  |
| Manutentori | Addetti alla manutenzione delle auto degli autisti | Meccanici, Operai |  |
| Autisti | Personale che svolge il ruolo di autista delle auto nella società | Driver |   |
| Veicoli | Auto utilizzate per il servizio di taxi | Automobili |  |
| Turni | Turni lavorativi che riguardano gli autisti | Orario Lavorativo |  |
| Richiesta Prenotazione | Richieste di prenotazioni effettuate da parte dall'utente | Prenotazioni |  |
| Utenti | Utenti utilizzatori del servizio taxi | Persone |  |
| Feedback | Recensioni lasciate dall'utente e dagli autisti | Recensioni |  |
| Tratte Completate | Corse effettuate portate a termine con successo | Corse |  |
| Tratte Rifiutate | Corse rifiutate da parte dell'autista per determinati motivi | Corse Annullate |  |
| Carta | Carta di credito personale dell'utente | Metodo di pagamento |  |
| Assicurazione | Dati dell'assicurazione associata al singolo veicolo | RCA, Polizza assicurativa |  |
| Addetti Marketing | Personale addetto al reparto marketing della società | Advertiser |  |

### Glossario delle relazioni

| Relazione                    | Descrizione                                                                                                                                     | Entità                                      |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------- |
| VeicoloPossiedeAssicurazione | Relazione che dice che ogni veicolo ha una propria assicurazione                                                                                | Veicoli (1,1), Assicurazione (1,1)          |
| AutistaGuidaVeicolo          | Relazione che dice che ogni autista guida la propria autovettura                                                                                | Autisti (1,1), Veicoli (1,1)                |
| AutistaPossiedePatente       | Relazione che dice che ogni autista, per poter guidare, necessita di una patente                                                                | Autisti (1,1), Patente (1,1)                |
| ContattaPerGuasto            | Relazione che dice che ogni autista può (non necessariamente) contattare un manutentore per un guasto al veicolo                                | Autisti (0,N), Manutentori (0,N)            |
| AutistaLasciaFeedback        | Relazione che dice che ogni autista può lasciare uno o più feedback relativio a tutti gli aspetti della corsa effettuata                        | Autisti (1,N), Feedback (1,1)               |
| AssegantoA                   | Relazione che dice che ogni autista viene assegnato ad una richiesta di prenotazione, in base a determinate circostanze                         | Autisti (1,1), Richiesta Prenotazione (1,1) |
| AggiungeOfferta              | Relazione che dice che un addetto marketing può aggiungere una o più offerte per gli utenti                                                     | Addetti Marketing (1,N), Offerte (1,1)      |
| UtenteHaOfferta              | Relazione che dice che ogni utente può avere (non necessariamente) una o più offerte attive                                                     | Utenti (1,1), Offerte (1,N)                 |
| UtentePossiedeCarta          | Relazione che dice che ogni utente deve possedere almeno una carta con cui effettuare i pagamenti                                               | Utenti (1,N), Carta (1,1)                   |
| EffettuaPrenotazione         | Relazione che dice che ogni utente effettua una o più prenotazioni                                                                              | Utenti (1,N), Richiesta Prenotazioni (1,1)  |
| UtenteLasciaFeedback         | Relazione che dice che ogni utente può lasciare uno o più feedback relativi alle corse da lui effettuate                                        | Utenti (1,N), Feedback (1,1)                |
| CartaPagaTratta              | Relazione che dice che ogni utente, tramite la propria carta, deve pagare le tratte da lui effettuate                                           | Carta (1,N), Tratte Completate (1,1)        |
| TrattaAvereFeedback          | Relazione che dice che ogni tratta completata può avere (non necessariamente) un solo feedback, che viene lasciato dagli utenti e dagli autisti | Tratte Completate (0,1), Feedback (1,1)     |
|  AutistaAvereTurni | Ogni autista ha un proprio turno lavorativo, ad ogni turno lavorativo vengono assegnati uno o più autisti | Autisti (1,1), Turni (1,N) |                                                                                                                                                                              |                                             |

## Schemi

### Schemi di relazione

Le chiave primarie sono identificate in **grassetto**, mentre le chiavi secondarie (o esterne) sono scritte in stile _Italic_

- Personale (**ID_Personale**, Nome, Cognome, NumeroTelefono, Email)
- Autisti (**ID_Autista**, Stipendio, _NumeroPatente_, _Targa_, _ID_Turno)
- Manutentori (**ID_Manutentore**, Qualifica)
- Addetti Marketing (**ID_Addetto**, Ruolo)
- ContattaPerGuasto (_ID_Manutentore_, _ID_Autista_)
- Patente (**NumeroPatente**, DDS, Categoria)
- Turni (**ID_Turno**, OrarioInizio, OrarioFine)
- Veicoli (**Targa**, Marca, Modello, PostiDisponibili, _ID_Assicurazione_)
- Assicurazione (**ID_Assicurazione**, DataDiScadenza, Tipo)
- Offerte (**ID_Offerta**, PromoCode, InfoOfferta, _ID_Addetto_)
- Utenti (**ID_Utente**, Nome, Cognome, Email, Abbonamento, PSW, _ID_Offerta_)
- Carta (**NumeroCarta**, DataScadenza, CVV, _ID_Utente_)
- Richiesta Prenotazione (**ID_Richiesta**, OrarioRichiesta, NumeroPasseggeri, PuntoRaccolta, PuntoRilascio, _ID_Utente_, _ID_Autista_)
- Tratte Complete (**ID_Tratta**, Costo, _NumeroCarta_)
- Tratte Rifiutate (**ID_Tratta**, Motivazione)
- Feedback (**ID_Feedback**, Stelle, Commento, Data, _ID_Tratta_)
### Schema Logico

![[Schema-Logico.jpg|center]]

#### Normalizzazione

Di seguito si discutono le forme normali dello schema logico:

- **1NF**: tutti gli schemi di relazione nello schema logico sopra riportato sono in **1NF**, poiché tutti gli attributi sono semplici, ovvero contengono soltanto valori atomici indivisibili.
- **2NF**: tutti gli schemi di relazione dello schema logico sono anche già in **2NF**, poiché sono già in **1NF** e nessun attributo presenta alcuna dipendenza parziale. Tutti gli attributi dipendono funzionalmente solo dalla chiave primaria della stessa tabella.
- **3NF**: tutti gli schemi di relazione sono anche in **3NF** perché già in **2NF**, ed inoltre, tutti gli attributi delle tabelle dipendono funzionalmente e direttamente dalla chiave primaria, senza transitività.
### Schema Fisico

Abbiamo distinto le frecce che vanno dalle entità figlie a quelle padre mettendole in blu.

Nelle entità, le chiavi secondarie sono indentificate con il pallino grigio, mentre quelle primarie sono identificate con il pallino nero.

![[Schema-Fisico.jpg|center]]

#### Generalizzazione

Una generalizzazione rappresenta un legame logico tra un’entità genitore e una o più entità figlie, in questo caso le entità genitore sono “Personale” e "Richiesta Prenotazione", ognuna con le rispettive entità figlie, che sono:

1) **Personale**
	1) Autisti
	2) Addetti Marketing
	3) Manutentori
2) **Richiesta prenotazione**
	1) Tratte completate
	2) Tratte rifiutate


Abbiamo tre metodi per rappresentare una generalizzazione a livello fisico:

- Accorpamento del padre nelle entità figlie
- Accorpamento delle entità figlie nel padre
- Sostituzione della generalizzazione con relazioni

Tra questi metodi abbiamo scelto il terzo in quanto da noi considerato il più adeguato. Infatti, il primo metodo avrebbe portato ad una ridondanza di relazioni.

Il secondo metodo necessita dell’aggiunta di un attributo nelle entità "Personale" e "Richiesta Prenotazioni", con il compito di specificare il ruolo del lavoratore (Es. Autisti = 1, Manutentori = 2, etc..), e il tipo di prenotazione (Es. Completata = 1 e Rifiutata = 2), in più si sarebbe dovuto scegliere se perdere informazioni (attributi) dei figli o inserire le informazioni nel padre, quindi aggiungere attributi dei figli al padre. La seconda scelta avrebbe portato ad una quantità non indifferente di valori NULL.

### Implementazione Database - MySQL
#### Creazione delle tabelle

```SQL
CREATE TABLE Personale(
	ID int not null ,
	Nome varchar(50) not null,
	Cognome varchar(50) not null,
	DDN date not null,
	NumeroDiTelefono int not null,
	Email varchar(255),
	PRIMARY KEY (ID)
);

CREATE TABLE AddettiMarketing (
	ID_Addetto int not null,
	Ruolo varchar(50),
	PRIMARY KEY (ID_Addetto),
	FOREIGN KEY (ID_Addetto) REFERENCES Personale(ID)
);

CREATE TABLE Patente (
	NumeroPatente varchar(255) not null,
	DDS date not null,
	Categoria varchar(50),
	PRIMARY KEY (NumeroPatente)
);

CREATE TABLE Offerte (
	ID_Offerta int not null ,
	PromoCode int not null,
	InfoOfferta varchar(50) not null,
	ID_Addetto int not null,
	PRIMARY KEY (ID_Offerta),
	FOREIGN KEY (ID_Addetto) REFERENCES AddettiMarketing(ID_Addetto)
);

CREATE TABLE Manutentori (
	ID_Manutentore int not null ,
	Qualifica varchar(50) not null,
	PRIMARY KEY (ID_Manutentore),
	FOREIGN KEY (ID_Manutentore) REFERENCES Personale (ID)
);

CREATE TABLE Assicurazione (
	ID_Assicurazione int not null,
	DataScadenza date not null,
	Tipo varchar(50) not null,
	PRIMARY KEY (ID_Assicurazione)
);

CREATE TABLE Veicoli (
	Targa varchar(50) not null,
	Marca varchar(50) not null,
	Modello varchar(50) not null,
	PostiDisponibili int not null,
	Assicurazione int not null,
	PRIMARY KEY (Targa),
	FOREIGN KEY (Assicurazione) REFERENCES Assicurazione(ID_Assicurazione)
);

CREATE TABLE Turni (
	ID_Turno int not null ,
	OrarioInizio int not null,
	OrarioFine int not null,
	PRIMARY KEY (ID_Turno)
);

CREATE TABLE Autisti (
	ID_Autista int not null ,
	NumeroPatente varchar(255) not null,
	Turno int not null,
	Targa varchar(50) not null,
	Stipendio int not null,
	PRIMARY KEY (ID_Autista),
	FOREIGN KEY (ID_Autista) REFERENCES Personale (ID),
	FOREIGN KEY (NumeroPatente) REFERENCES Patente(NumeroPatente),
	FOREIGN KEY (Turno) REFERENCES Turni(ID_Turno),
	FOREIGN KEY (Targa) REFERENCES Veicoli(Targa)
);

CREATE TABLE Utenti (
	ID_Utente int not null ,
	Nome varchar(50) not null,
	Cognome varchar(50) not null,
	Email varchar(255) not null,
	Password varchar(255) not null,
	ID_Offerta int not null,
	Abbonamento varchar(50) not null,
	PRIMARY KEY (ID_Utente),
	FOREIGN KEY (ID_Offerta) REFERENCES Offerte (ID_Offerta)
);

CREATE TABLE RichiestePrenotazioni (
	ID_Richiesta int not null ,
	PuntoDiRaccolta varchar(50) not null,
	PuntoDiRilascio varchar(50) not null,
	DataRichiesta date not null,
	OrarioRichiesta varchar(50) not null,
	NumeroPasseggeri int not null,
	ID_Utente int not null,
	ID_Autista int not null,
	PRIMARY KEY (ID_Richiesta),
	FOREIGN KEY (ID_Utente) REFERENCES Utenti(ID_Utente),
	FOREIGN KEY (ID_Autista) REFERENCES Autisti(ID_Autista)
);

CREATE TABLE Carta (
	NumeroCarta varchar(50) not null,
	DataScadenza date not null,
	CVV int not null,
	ID_Utente int not null,
	PRIMARY KEY (NumeroCarta),
	FOREIGN KEY (ID_Utente) REFERENCES Utenti(ID_Utente)
);

CREATE TABLE TratteCompletate (
	ID_TrattaC int not null ,
	Costo int not null,
	NumeroCarta varchar(50) not null,
	PRIMARY KEY (ID_TrattaC),
	FOREIGN KEY (ID_TrattaC) REFERENCES RichiestePrenotazioni (ID_Richiesta),
	FOREIGN KEY (NumeroCarta) REFERENCES Carta (NumeroCarta)
);

CREATE TABLE Feedback (
	ID_Feedback int not null ,
	StelleUtente int not null,
	CommentoUtente varchar(255) not null,
	StelleAutista int not null,
	CommentoAutista varchar(255) not null,
	Data date not null,
	ID_TrattaCompletata int not null,
	PRIMARY KEY (ID_Feedback),
	FOREIGN KEY (ID_TrattaCompletata) REFERENCES TratteCompletate (ID_TrattaC)
);

CREATE TABLE TratteRifiutate (
	ID_TrattaR int not null ,
	Motivazione varchar(255) not null,
	PRIMARY KEY (ID_TrattaR),
	FOREIGN KEY (ID_TrattaR) REFERENCES RichiestePrenotazioni (ID_Richiesta)
);

CREATE TABLE ContattaPerGuasto (
	ID_Manutentore int not null,
	ID_Autista int not null,
	Motivo varchar(255) not null,
	FOREIGN KEY (ID_Manutentore) REFERENCES Manutentori (ID_Manutentore),
	FOREIGN KEY (ID_Autista) REFERENCES Autisti (ID_Autista)
);
```

#### Triggers

Abbiamo implementato dei triggers nel nostro sistema, per far rispettare i vincoli scritti sopra
(i.e. Un utente **NON** può prenotare più di una corsa nello stesso momento,etc...)

I triggers sono i seguenti

```SQL
CREATE TRIGGER `ControllaOrarioRichiesta` BEFORE INSERT ON `RichiestePrenotazioni` FOR EACH ROW BEGIN

-- Controlla se l'orario richiesto esiste già nella tabella
	IF EXISTS (
		SELECT 1
		FROM RichiestePrenotazioni
		WHERE OrarioRichiesta = NEW.OrarioRichiesta AND ID_Utente = NEW.ID_Utente
	) THEN
	
	-- Se l'orario esiste già, interrompi l'inserimento
		SIGNAL SQLSTATE '45000'
		SET MESSAGE_TEXT = '[ERRORE],OGNI UTENTE NON PUÒ PRENOTARE PIÙ DI UNA CORSA NELLO STESSO ORARIO';
	END IF;

END
```
#### Inserimenti Manuali

```SQL
INSERT INTO Personale (ID,Nome,Cognome,DDN,NumeroTelefono,Email) VALUES ();
```

### Script di creazione automatica di query

Per rendere paragonabili i tempi di esecuzione delle query non ottimizzate con quelle ottimizzate, è stato necessario introdurre, nel database, un gran numero di record.
Per velocizzare questo processo, è stato scritto uno script in Python che scrive tutti gli inserimenti generati casualmente, in un semplice file di testo.

Il file è il seguente

```Python
import random
from faker import Faker
import string
import decimal
import datetime

fake = Faker("it_IT")


def genRandomDate():
    start_date = datetime.date(1975, 1, 1)
    end_date = datetime.date(2001, 12, 30)
    num_days = (end_date - start_date).days
    rand_days = random.randint(1, num_days)
    random_date = start_date + datetime.timedelta(days=rand_days)
    return random_date

def genRandomCardDate():
    start_date = datetime.date(2027, 1, 1)
    end_date = datetime.date(2034, 12, 30)
    num_days = (end_date - start_date).days
    rand_days = random.randint(1, num_days)
    random_date = start_date + datetime.timedelta(days=rand_days)

    return random_date

def genRandomLicenceDate():
    start_date = datetime.date(2025, 1, 1)
    end_date = datetime.date(2035, 12, 30)
    num_days = (end_date - start_date).days
    rand_days = random.randint(1, num_days)
    random_date = start_date + datetime.timedelta(days=rand_days)

    return random_date

def genRandomRequestDate():
    start_date = datetime.date(2022, 1, 1)
    end_date = datetime.date(2023, 12, 30)
    num_days = (end_date - start_date).days
    rand_days = random.randint(1, num_days)
    random_date = start_date + datetime.timedelta(days=rand_days)

    return random_date

def generateEmail(name, surname):
    domain = fake.domain_name()
    return f"{name}.{surname}@{domain}"

def generateTarga():
    SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    NUMBERS = "0123456789"
    start = "".join(random.choice(SYMBOLS) for i in range(2))
    mezzo = "".join(random.choice(NUMBERS) for i in range(3))
    fine = "".join(random.choice(SYMBOLS) for i in range(2))

    return start+mezzo+fine

def generatePsw():
    ALL = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    psw = "".join(random.choice(ALL) for i in range(9))
    return psw

def generateCardNumber():
    NUMBERS = "0123456789"
    number = "".join(random.choice(NUMBERS) for i in range(16))
    return number

def checkStelleUtenti(stelle):
    if stelle == 1:
        return 1
    elif stelle == 2:
        return 2
    elif stelle == 3:
        return 3
    elif stelle == 4:
        return 4
    elif stelle == 5:
        return 5

print("Inizio esecuzione...")

print("L'ORDINE DI ESECUZIONE DEI FILE È 1.txt,2.txt,etc...")

print("Inizio Creazione 1.txt")

SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBERS = "0123456789"
ALL_SYMBOLS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# random_name = ""
f = open("1.txt", "w+")
f.write("---------------Inizio Inserimento Personale---------------\n")
random_id = ""
unique_Personale = ["''"]

values = []
for i in range(6000):
    data = genRandomDate()
    surname = fake.last_name()
    name = fake.first_name()
    email = str(generateEmail(name, surname))
    #random_id = "".join(random.choice(NUMBERS) for i in range(3))
    random_id = str(i)
    unique_Personale.append(random_id)
    
    query = "('" + random_id + "','"+ name+ "','"+ surname+ "','"+ str(data)+ "','"+ fake.phone_number()+ "','"+ email+ "')"
    values.append(query)
f.write(
    "INSERT INTO Personale (ID,Nome,Cognome,DDN,NumeroDiTelefono,Email) VALUES" + ",\n".join(values) + ";"
)    
f.write("\n")
f.write("---------------Fine Inserimento Personale---------------\n")
f.close()

print("1.txt Done")

print("Inizio Creazione 2.txt")

f = open("2.txt","w+")

f.write("---------------Inizio Inserimento Addetti Marketing---------------\n")
# parte addetti marketing
unique_AddMark = ["''"]

ruoli = ["Responsabile", "Analista", "Coordinatore"]
values_marketing = []
for i in range(3000):
    # random_name = "".join(random.choice(NUMBERS) for i in range(3))
    random_ruolo = random.choice(ruoli)
    random_id = unique_Personale[i]
    # print(random_name, end="\n")
    query = "('"+ random_id+ "','"+ random_ruolo+ "')"
    unique_AddMark.append(random_id)
    values_marketing.append(query)
f.write(
    "INSERT INTO AddettiMarketing (ID_Addetto,Ruolo) VALUES"+",\n".join(values_marketing)+";"
)
f.write("\n")
# fine parte addetti marketing
f.write("---------------Fine Inserimento Addetti Marketing---------------\n")
f.write("\n")
f.write("---------------Inizio Inserimento Patente---------------\n")

patenti = ["B","BE","B96"]
unique_Patente = ["''"]
values_patenti = []
for i in range(2900):
    data = genRandomLicenceDate()
    random_numpatente = "".join(random.choice(ALL_SYMBOLS) for i in range(9))
    categoria = "".join(random.choice(patenti) for i in range(1))
    unique_Patente.append(random_numpatente)
    
    query = "('"+ random_numpatente+ "','"+ str(data)+ "','"+ categoria+ "')"
    
    values_patenti.append(query)
f.write(
    "INSERT INTO Patente (NumeroPatente,DDS,Categoria) VALUES "+",\n".join(values_patenti)+";"
)
f.write("\n")
f.write("---------------Fine Inserimento Patente---------------\n")
f.write("\n")
f.write("---------------Inizio Inserimento Turni---------------\n")

unique_Turno = ["''"]
ora_inizio = ['9','10','11','14','15','16']
ora_fine = ['14','15','16','20','21','22']
values_turni = []
for i in range(5):
    
    random_turno = "".join(random.choice(NUMBERS) for i in range(1))
    inizio = "".join(random.choice(ora_inizio))
    fine = "".join(random.choice(ora_fine))
    unique_Turno.append(random_turno)
    query = "('"+ random_turno+ "','"+ inizio+ "','"+ fine+ "')"
    
    values_turni.append(query)
f.write(
    "INSERT INTO Turni (ID_Turno,OrarioInizio,OrarioFine) VALUES "+",\n".join(values_turni)+";"
)
f.write("\n")
f.write("---------------Fine Inserimento Turni---------------\n")
f.write("\n")
f.write("---------------Inizio Inserimento Assicurazione---------------\n")

unique_Assicurazione = ["''"]
values_assicurazione = []
tipo_assicurazione=["Kasko","Furto","Incendio","Base"]
for i in range(2901):
    random_id = str(i)
    data = genRandomDate()
    tipo = random.choice(tipo_assicurazione)
    query = "('"+ str(random_id)+ "','"+ str(data)+ "','"+ str(tipo)+ "')"
    unique_Assicurazione.append(random_id)
    values_assicurazione.append(query)
f.write(
    "INSERT INTO Assicurazione (ID_Assicurazione,DataScadenza,Tipo) VALUES "+",\n".join(values_assicurazione)+";"
)
f.write("\n")
f.write("---------------Fine Inserimento Assicurazione---------------\n")
f.write("\n")
f.write("---------------Inizio Inserimento Veicoli---------------\n")
unique_Veicolo = ["''"]
values_veicolo = []
l_marca = ["Fiat","BMW","Audi","Range Rover","Seat"]
l_modello = ["Punto","Panda","Q8","RS7"]
for i in range(2901):
    random_targa = generateTarga()
    random_assicurazione = unique_Assicurazione[i]
    query = "('"+ str(random_targa)+ "','"+ str(random.choice(l_marca))+ "','"+ str(random.choice(l_modello))+ "','"+str(random.randint(1,12))+"','"+str(random_assicurazione)+"')"
    unique_Veicolo.append(random_targa)
    values_veicolo.append(query)

f.write(
    "INSERT INTO Veicolo (Targa,Marca,Modello,PostiDisponibili,Assicurazione) VALUES "+",\n".join(values_veicolo)+";"
)
f.write("\n")
f.write("---------------Fine Inserimento Veicoli---------------\n")
f.write("\n")
f.write("---------------Inizio Inserimento Autisti---------------\n")

unique_Autisti = ["''"]
values_autisti = []
stipendio = ["1200","1500","1350"]
for i in range(2901):
    random_id = unique_Personale[3000+i]
    random_patente = unique_Patente[i]
    random_Turno = random.choice(unique_Turno[1:])
    random_targa = random.choice(unique_Veicolo)
    query = "('"+ random_id+ "','"+ random_patente+ "','"+ random_Turno+ "','"+random_targa+"','"+random.choice(stipendio)+"')"
    unique_Autisti.append(random_id)
    values_autisti.append(query)
f.write(
    "INSERT INTO Autisti (ID_Autista,NumeroPatente,Turno,Targa,Stipendio) VALUES "+",\n".join(values_autisti)+";"
)
f.write("\n")
f.write("---------------Fine Inserimento Autisti---------------\n")
f.write("\n")
f.write("---------------Inizio Inserimento Manutentori---------------\n")

unique_Manutentori = ["''"]
values_manutentori = []
qualifica = ["Gommista","Elettrauto","Meccanico","Carrozziere"]
for i in range(100):
    random_id = unique_Personale[5900+i]
    
    query = "('"+ random_id+ "','"+ random.choice(qualifica)+ "')"
    unique_Manutentori.append(random_id)
    values_manutentori.append(query)
f.write(
    "INSERT INTO Manutentori (ID_Manutentore,Qualifica) VALUES "+",\n".join(values_manutentori)+";"
)
f.write("\n")
f.write("---------------Fine Inserimento Manutentori---------------\n")
f.write("\n")
f.write("---------------Inizio Inserimento ContattaPerGuasto---------------\n")

unique_Contatto = ["''"]
values_contatto = []
motivi = ["Gomma Bucata","Spia dell motore accesa","Radiatore bucato","Batteria scarica"]
for i in range(100):
    random_manutentore = random.choice(unique_Manutentori)
    random_autista = random.choice(unique_Autisti)

    query = "('"+ random_manutentore+ "','"+ random_autista+ "','"+random.choice(motivi)+"')"
    unique_Contatto.append((random_manutentore,random_autista))
    values_contatto.append(query)
f.write(
    "INSERT INTO ContattaPerGuasto (ID_Manutentore,ID_Autista,Motivo) VALUES "+",\n".join(values_contatto)+";"
)
f.write("\n")
f.write("---------------Fine Inserimento ContattaPerGuasto---------------\n")

print("2.txt Done")
f.close()

print("Inizio Creazione 3.txt")
f = open("3.txt","w+")

f.write("---------------Inizio Inserimento Offerte---------------\n")
unique_Offerta = ["''"]
offerta = ["Sconto 10%","Sconto 15%","Sconto 20%","Credito 5€","Credito 10€"]
values_offerta = []
for i in range(15):
    random_id = str(i)
    promo = "".join(str(random.randint(1,9)) for i in range(6))
    random_addetto = random.choice(unique_AddMark)
    query = "('"+ random_id+ "','"+ promo+ "','"+ random.choice(offerta)+ "','"+random_addetto+"')"
    unique_Offerta.append(random_id)
    values_offerta.append(query)
f.write(
    "INSERT INTO Offerta (ID_Offerta,PromoCode,InfoOfferta,ID_Addetto) VALUES "+",\n".join(values_offerta)+";"
)
f.write("\n")
f.write("---------------Fine Inserimento Offerte---------------\n")
f.write("\n")
f.write("---------------Inizio Inserimento Utenti---------------\n")

unique_Utenti = ["''"]
values_utenti = []
abbonamento = ["Trimestrale","Semestrale","Annuale"]
for i in range(10000):
    random_id = str(i)
    surname = fake.last_name()
    name = fake.first_name()
    email = str(generateEmail(name, surname))
    psw = generatePsw()
    id_off = random.choice(unique_Offerta)
    query = "('"+ random_id+ "','"+ name+ "','"+ surname+ "','"+email+"','"+psw+"','"+id_off+"','"+random.choice(abbonamento)+"')"
    unique_Utenti.append(random_id)
    values_utenti.append(query)
f.write(
    "INSERT INTO Utenti (ID_Utente,Nome,Cognome,Email,Password,ID_Offerta,Abbonamento) VALUES "+",\n".join(values_utenti)+";"
)
f.write("\n")
f.write("---------------Fine Inserimento Utenti---------------\n")
f.write("\n")
f.write("---------------Inizio Inserimento Carte---------------\n")

unique_Carta = ["''"]
values_carta = []

for i in range(10000):
    random_id = str(i)
    data_scadenza = genRandomCardDate()
    cvv = "".join(str(random.randint(0,9)) for i in range(3))
    utente = unique_Utenti[i]
    query = "('"+ random_id+ "','"+ str(data_scadenza)+ "','"+ cvv+ "','"+utente+"')"
    unique_Carta.append(random_id)
    values_carta.append(query)
f.write(
    "INSERT INTO Carta (NumeroCarta,DataScandenza,CVV,ID_Utente) VALUES "+",\n".join(values_carta)+";"
)
f.write("---------------Fine Inserimento Carte---------------\n")
print("3.txt Done")
f.close()
print("Inizio creazione 4.txt")
f = open("4.txt","w+")

f.write("---------------Inizio Inserimento RichiestaPrenotazioni---------------\n")

unique_RichPren = ["''"]
values_ricpren = []
raccolta = ["Anagnina","Termini","Centocelle","Eur","Tor Vergata","Colosseo"]
rilascio = ["Finocchio","Garbatella","Ostia","San Lorenzo","Primavalle","San Basilio"]
data = []
ora = ['9','10','11','14','15','16','20','21','22']

for i in range(10000):
    random_id = str(i)
    passeggeri = str(random.randint(1,12))
    utente = random.choice(unique_Utenti)
    autista = random.choice(unique_Autisti)
    data = genRandomRequestDate()
    orario = random.choice(ora)
    query = "('"+ random_id+ "','"+ str(random.choice(raccolta))+ "','"+ str(random.choice(rilascio))+ "','"+str(data)+"','"+str(orario)+"','"+str(passeggeri)+"','"+str(utente)+"','"+str(autista)+"')"
    unique_RichPren.append(random_id)
    values_ricpren.append(query)
    data.append(orario)
f.write(
    "INSERT INTO RichiestePrenotazioni (ID_Richiesta,PuntoDiRaccolta,PuntoDiRilascio,DataRichiesta,OrarioRichiesta,NumeroPasseggeri,ID_Utente,ID_Autista) VALUES "+",\n".join(values_ricpren)+";"
)
f.write("\n")
f.write("---------------Fine Inserimento RichiestaPrenotazioni---------------\n")
f.write("\n")
f.write("---------------Inizio Inserimento TratteCompletate---------------\n")

unique_TrattaC = ["''"]
values_trattac = []
costo = ["25€","65€","115€","35€","50€"]
for i in range(7000):
    random_id = unique_RichPren[i]
    costi = random.choice(costo)
    numcarta = random.choice(unique_Carta)
    query = "('"+ random_id+ "','"+ str(costi)+ "','"+ str(numcarta)+ "')"
    unique_TrattaC.append(random_id)
    values_trattac.append(query)
f.write(
    "INSERT INTO TratteCompletate (ID_TrattaC,Costo,NumeroCarta) VALUES "+",\n".join(values_trattac)+";"
)
f.write("\n")
f.write("---------------Fine Inserimento TratteCompletate---------------\n")
f.write("\n")
f.write("---------------Inizio Inserimento Feedback---------------\n")

unique_Feed = ["''"]
values_feed = []
feedback_utente = {
                    1: "Non lo prenderò mai più!",
                    2: "Non mi è piaciuto lo stile di guida",
                    3: "Nulla di particolare",
                    4: "Veicolo molto pulito e comodo.",
                    5: "Autista veramente cordiale",
                   }

feedback_autisti = {
                    1: "Utente scortese!",
                    2: "Utente ritardatario",
                    3: "Nulla di particolare",
                    4: "Utente rispettoso.",
                    5: "Utente veramente genuino",
                   }

for i in range(7000):
    random_id = str(i)
    # Ottieni una chiave casuale
    stelle_random_ut = random.choice(list(feedback_utente.keys()))
    # Ottieni il valore corrispondente alla chiave casuale
    commento_ut = str(feedback_utente[stelle_random_ut])

    #stelle_random_aut = random.choice(list(feedback_autisti.keys()))
    stelle_random_aut = checkStelleUtenti(stelle_random_ut)
    # Ottieni il valore corrispondente alla chiave casuale
    commento_aut = str(feedback_autisti[stelle_random_aut])
    random_trattac = random.choice(unique_TrattaC)
    query = "('"+ random_id+ "','"+ str(stelle_random_ut)+ "','"+ str(commento_ut)+ "','"+str(stelle_random_aut)+"','"+str(commento_aut)+"','"+str(data[i])+"','"+str(random_trattac)+"')"

    unique_Feed.append(random_id)
    values_feed.append(query)

f.write(
    "INSERT INTO Feedback (ID_Feedback,StelleUtente,CommentoUtente,StelleAutista,CommentoAutista,Data,ID_TrattaCompletata) VALUES "+",\n".join(values_feed)+";"
)
f.write("\n")
f.write("---------------Fine Inserimento Feedback---------------\n")
f.write("\n")
f.write("---------------Inizio Inserimento TratteRifiutate---------------\n")

unique_TrattaR = ["''"]
values_trattar = []
motivi = ["Problema generale","Indisponibilità al servizio","Troppo lontano"]
for i in range(3000):
    random_id = unique_RichPren[7000+i]
    motivo = random.choice(motivi)
    query = "('"+ random_id+ "','"+ str(motivo)+ "')"
    unique_TrattaR.append(random_id)
    values_trattar.append(query)
f.write(
    "INSERT INTO TratteRifiutate (ID_TrattaR,Motivazione) VALUES "+",\n".join(values_trattar)+";"
)
f.write("\n")
f.write("---------------Fine Inserimento TratteRifiutate---------------\n")
print("4.txt Done")
f.close()
```