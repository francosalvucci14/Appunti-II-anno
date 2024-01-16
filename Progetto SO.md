# Analisi della realtà

La realtà è formata da 3 oggetti principali, che sono:
- Centro di Ricerca di Roma
- Clinica di Firenze
- Camper

Nel Centro di Ricerca ci sono due padiglioni, adibiti a convegni, ricerce in laboratorio e erogazione di prestazioni sanitarie.
Nella Clinica vengono effettuate visite mediche ed esami diagnostici.
Nel Camper vengono erogate visite gratuite di screening.

L'attività generale viene gestita tramite il sito web del Campus, dove :
- gli utenti possono prenotare le visite
- il personale medico accede al sito e controlla la lista dei pazienti,gestisce corsi,convegni e pagamento delle prestazioni mediche
- i medici prenotano gli esami per conto dei pazienti

I medici e il personale medico accedono al sito tramite username e password, in un area riservata.

## Analisi delle funzionalità del sistema

- **Gestione dei medici**:
	- Anagrafica, e-mail, cellulare, computer, telefono di reparto, switch
	- Acceedono al sito tramite user e password
	- Prenotano esami per i pazienti tramite Camper
- **Gestione dei pazienti**:
	- Anagrafica, anamnesi, e-mail,cellulare
	- Accesso al sito tramite registrazione
	- Prenotano le visite mediche
- **Gestione Prenotazioni**:
	- Codice, data e ora
- **Gestione Prestazioni**:
	- Codice, tipo (visita medica, analisi, etc..) costo
- **Gestione Corsi e Convegni**:
	- Codice, descrizione, data e ora di inizio e fine
- **Gestione Sito Web**:
	- Accesso, in una area riservata, per medici e personale medico
	- Accesso tramite username e password per l'area personale relativa al singolo utente
	- Accesso all'area medica
	- Accesso all'area per la gestione di convegni e corsi

## Ipotesi iniziali e aggiuntive

- Utilizzo di un database per la gestione e memorizzazione dei dati
- Utilizzo di protocolli di sicurezza web per il mantenimento dei dati
- Utilizzo di protocolli di sicurezza per la comunicazione tra le sedi e il camper

# Soluzioni proposte

1. Implementazione di una VPN crittografata:
	1. Scelta di una VPN sicura e affidabile
	2. Implementazione di tunnel VPN tra le sedi di Roma e Firenze, e supporto per il collegamento con il camper
	3. Implementazione di sistemi di autenticazione sicuri