```table-of-contents
title: 
style: nestedList # TOC style (nestedList|inlineFirstLevel)
minLevel: 0 # Include headings from the specified level
maxLevel: 0 # Include headings up to the specified level
includeLinks: true # Make headings clickable
debugInConsole: false # Print debug info in Obsidian console
```
# Livello di applicazione

## Creare un'applicazione di rete

Creare un'applicazione di rete significa **scrivere programmi che** :
- GIrano su sistemi terminali diversi
- Comunicano attraverso la rete
- Ad esempio, il software di un server Web comunica con il software di un browser

**Non è necessario scrivere programmi per il nucleo della rete** :
- I dispositivi del nucleo di rete non eseguono applicazioni utente
- Il confinamento delle applicazioni nei sistemi periferici ha facilitato il rapido sviluppo e la diffusione di una vasta gamma di applicazioni per Internet

![[Pasted image 20240321101420.png|center|300]]

### Paradigma Client-Server

L'architettura client-server è un'architettura estremamente diffusa

Essa conta di due componenti principali :
- **Server**
	- Host sempre attivo
	- Indirizzo IP fisso
	- Spesso posizionato in un datacenter, per la scalabilità
- **Client**
	- Host che contatta/comunica con il server
	- Può contattare il server in qualunque momento
	- Può avere indirizzi IP dinamici
	- *non* comunica con gli altri client

![[Pasted image 20240321101658.png|center|300]]

### Architettura peer-to-peer

A differenza dell'architettura client-server, qui non abbiamo un server che è sempre attivo, ma abbiamo coppie aribitrarie di host (**peer**), che comunicano direttamente l'uno con l'altro

I peer richiedono un servizio ad altri peer e forniscono un servizio in cambio ad altri peer
- Abbiamo il concetto di **scalabilità intrinseca** : nuovi peer aggiungono capacità al servizio generale, anche se aumentano il carico di lavoro

I peer non devono necessariamente essere sempre attivi e cambiano indirizzo IP (molto difficile da gestire)

## Processi comunicanti

>[!definition]- Processo
>Programma in esecuzione su un host

All'interno dello stesso host, due processi comunicano usando un approccio interprocesso (**inter-process communication**)

Processi su due host diversi comunicano attraverso lo scambio di messaggi

> **Processo client** : processo che da inizio alla comunicazione
> **Processo server** : processo che attende di essere contattato


>[!info]- Nota
>Nelle applicazioni P2P, un processo può essere sia client che server

### Socket

Un processo invia/riceve messaggi a/da la sua **socket**

Un socket è analogo a una porta
- Il processo mittente fa uscire il messaggio fuori dalla propria "porta" (socket)
- Il processo mittente presuppone l'esistenza di un'infrastruttura esterna che trasporterà il messaggio attraverso la rete fino alla (socket) del processo di destinazione

![[Pasted image 20240321102606.png|center|500]]

### Indirizzamento

Per ricevere messaggi, un processo deve avere un **identificatore**

Un host ha un indirizzo IP univoco a 32 bit

**D**: è sufficiente conoscere l'indirizzo IP dell'host su cui è in esecuzione un processo per identificare il processo stesso?

**R**: no, perchè sullo stesso host possono essere in esecuzione molti processi

L'identificatore comprende sia **l'indirizzo IP che i numeri di porta** associati al processo in esecuzione sull'host

Alcuni numeri di porta noti sono :
- 80 : HTTP
- 443 : HTTPS
- 22 : SSH
- 23 : FTP
- etc...

## Protocollo a livello applicativo

Un protocollo a livello applicativo definisce :

- **Tipi di messaggi scambiati** : rispsota, richiesta
- **Sintassi dei messaggi** : quali sono i campi nel messaggio e come sono descritti
- **Semantica dei messaggi** : Significato delle informazioni nei campi
- **Regole** per determinare quando e come un processo invia e risponde ai messaggi

## Quale servizio di trasporto richiede un'applicazione

- **Perdita dei dati**
	- Alcune applicazioni richiedono un trasferimento $100\%$ affidabile (es. trasferimento file, transazioni web,etc..)
	- Altre invece possono tollerare qualche perdita
- **Sensibilità al fattore tempo**
	- Alcune applicazioni richiedono che i ritardi siano bassi per essere "efficaci" (es . giochi interattivi, telefonia,etc..)
- **Throughput**
	- Alcune applicazioni (dette "sensibili alla bamnda"), ad esempio, quelle multimediali, per essere efficaci richiedono un'ampiezza di banda minima
	- Altre applicazioni utilizzano l'ampiezza di banda che si rende disponibile
- **Sicurezza**
	- Cifratura, integrità dei dati,etc..

**Recap dei requisiti**

![[Pasted image 20240321103737.png|center|500]]

## Servizi dei protocolli di trasporto di Internet

*Servizio TCP* :
- **Trasporto affidabile** fra i processi di invio e ricezione : dati consegnati senza errori, perdite e nell'ordine di invio
- **Controllo di flusso** : il mittente non vuole sovraccaricare il destinatario
- **Controllo della congestione** : "strozza" il processo d'invio quando la rete è sovraccarica
- **Orientato alla connessione** : è richiesto un setup fra i processi client e server
- **Non offre** : temporizzazione, garanzie su un'ampiezza di banda minima, sicurezza

*Servizio UDP* :
- **Trasferimento dati inaffidabile** fra i processi di invio e ricezione
- **Non offre** : affidabilità, controllo di flusso, controllo della congestione, temporizzazione, ampiezza di banda minima, sicurezza, setup alla connessione

### Rendere sicuro TCP

**Socket TCP e UDP**
- Nessuna cifratura
- Password inviate in chiaro, cioè senza cifratura, attraverso socket

**Transport Layer Security (TLS)**
- Offre connessioni TCP cifrate
- Controllo di integrità dei dati
- Autenticazione end-to-end

**TLS implementato a livello applicazione**
- Le applicazioni usato librerie TLS, cje usano a propria volta TCP
- Testo in chiaro (cleartext) inviato nella "socket"

## Web e HTTP

Una pagina web è costituita de *oggetti*, ciascuno dei quali può essere memorizzato su un server Web differente
Un oggetto può essere un file HTML, un'immagine, uno script JavaScript e cosi via
Una pagina web è formata da un **file HTML di base** che include *diversi oggetti referenziati*, ciascuno referenziato da un URL, ad esempio,
$$\underbrace{\text{www.someschool.edu}}_{\text{nome dell'host (hostname)}}/\underbrace{\text{someDept/pic.gif}}_{\text{percorso (path name)}}$$
### Panoramica su HTTP

HTTP : HyperText Transfer Protocol
- Protocollo a livello applicazione del Web
- Modello client/server:
	- **Client** : Browser che richiede, riceve (usando il protocollo HTTP) e "visualizza" gli oggetti del Web
	- **Server** : Il server Web che invia (usando il protocollo HTTP) oggetti in risposta alle richieste dei client

![[Pasted image 20240403114505.png|center|250]]

**HTTP usa TCP** :
- Il client inizializza la connessione TCP (crea una socket) con il server sulla porta 80
- Il server accetta la connessione TCP del client
- messaggi HTTP (messaggi di un protocollo di applicazione) scambiati tra browser (client HTTP) e server Web (server HTTP)
- Connessione chiusa TCP

**HTTP è un protocollo "senza stato" (stateless)**
- Il server non mantiene informazioni sulle richieste fatte dal client

#### Connessioni HTTP : Due tipi

| **Connessioni non persistenti**                          | **Connessioni persistenti**                                                             |
| -------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| Connessione TCP aperta                                   | Connessione TCP al server aperta                                                        |
| Almeno un oggetto viene trasmesso su una connessione TCP | Più oggetti possono essere trasmessi su una singola connessione TCP tra client e server |

##### Connessioni non persistenti

L'utente immette l'URL : http://www.someSchool.edu/someDepartment/home.html

![[Pasted image 20240403115850.png|center|600]]
![[Pasted image 20240403115924.png|center|600]]

**Tempo di risposta**

>[!definition]- RTT
>Tempo impiegato da un piccolo pacchetto per andare dal client al server e ritornare al client (include ritardi di elaborazione,accodamento,propagazione)

**Tempo di risposta (per oggetto)**
- un RTT per inizializzare la connessione TCP
- un RTT perchè ritornino la richiesta HTTP e i primi byte della risposta HTTP
- tempo di trasmissione del file/oggetto

Tempo di risposta con connessioni non persistenti = $2RTT$+tempo di trasmissione del file

![[Pasted image 20240403120220.png|center|500]]

##### Connessioni persistenti (HTTP 1.1)

**Svantaggi delle connessioni non persistenti** :
- Richiedono 2RTT per oggetto
- Overhead del sistema operativo per *ogni* connessione TCP
- I browser spesso aprono connessioni TCP parallele per caricare gli oggetti referenziati

**Connessioni persistenti (HTTP 1.1)**
- Il server lascia la connessione TCP aperta dopo l'invio di una risposta
- I successivi messaggi tra gli stessi client/server vengono trasmessi sulla connessione aperta
- Il client invia le richieste non appena incontra un oggetto referenziato
- un solo RTT per tutti gli oggetti referenziati

### Messaggio di richiesta HTTP

Due tipi di messaggi HTTP : **richiesta**, **risposta**

**Messaggio di richiesta HTTP** :
- ASCII (formato leggibile dall'utente)

![[Pasted image 20240403121254.png|center|600]]

Alcuni campi di intestazione nei messaggi di richiesta

**Host**
- Hostname o numero di porta (se assente, si assume 80 per HTTP e 443 per HTTPS) del server al quale sarà inviata la richiesta. Obbligatorio in HTTP/1.1; se assente, il server può rispondere con un 400 Bad Request (vedi codici qui -> [[#^7ce98c|Codici]])
**User-Agent**
- Identifica l'applicazione, il sistema operativo, il vendor e/o la versione dello user agent che sta effettuando la richiesta
**Accept**
- Tipi di contento, espressi come media type, compresi dal client
**Accept-Language**
- Linguaggi naturali o *locali* preferiti dal client
**Accept-Encoing**
- Algoritmi di codifica compresi dal client
**Connection**
- Controlla se la connessione rimarrà aperta al termine dello scambio richiesta/risposta. Il valore *close* indica che la connessione sarà chiusa (default in HTTP/1.0); altrimenti, una lista non vuota di nomi di header (in genere solo keep-alive), che saranno rimossi dal primo proxy non trasparente o cache, indica che la connessione rimarrà aperta (default in HTTP/1.1)
#### Formato generale

![[Pasted image 20240403141050.png|center|500]]

#### Altri messaggi di richiesta HTTP

**Metodo POST**
- La pagina web spesso include un form per l'input dell'utente
- L'input dell'utente viene inviato dal client al server nel corpo dell'entità di un messaggio di richiesta HTTP POST

**Metodo GET** (per inviare dati al server)
- L'input arriva al server nel campo URL della riga di richiesta (dopo un `?`)

**Metodo HEAD**
- Richiede le intestazioni (solo) che verebbero restituiste se l'URL specificato fosse richiesto con il metodo HTTP GET

**Metodo PUT**
- Carica un nuovo file (oggetto) sul server
- Sosituisce completamente il file esistente all'URL specificato con il contenuto del corpo dell'entità del messaggio di richiesta HTTP PUT

![[Pasted image 20240403141447.png|center|600]]

Altri campi di intestazione nei messaggi di richiesta

**Date**
- Data e ora in cui il messaggio è stato originato
**Server**
- Descrive il software usato dal server di origine per gestire la richiesta
**Last modified**
- Data e ora in cui il server di origine crede che l'oggetto sia stato modificato per l'ultima volta
**Accept-Ranges**
- Indica il supporto del server ai download parziali : il valore, se diverso da `none`, indica l'unità che si può usare per esprimere l'intervallo richiesto
**Content-Lenght**
- Lunghezza in byte del corpo dell'entità inviato al ricevente (o che sarebbe stato inviato nel caso di una richiesta HEAD)
**Content-Type**
- *Media type* (che indica un formato) del corpo dell'entità inviato al ricevente (o che sarebbe stato inviato nel caso di una richiesta HEAD)

### Codici di stato della risposta HTTP

^7ce98c

Si trovano nella prima riga nel messaggio di risposta dal server al client
Definiti da RFC 9110
Sono raggruppati in cinque categorie, discriminate dalla prima cifra

**1xx Informational**
- Una risposta intermedia per comunicare lo stato di connessione o l'avanzamento della richiesta prima di completare l'azione richeista e inviare una risposta finale
**2xx Successful**
- La richiesta è stata ricevuta con successo, compresa e accettata
**3xx Redirect**
- Il client deve eseguire ulteriori azioni per soddisfare la richiesta
**4xx Client Error**
- La richiesta è sintatticamente scorretta o non può essere soddisfatta (es. 404 Not Found)
**5xx Server Error**
- Il server ha fallito nel soddisfare una richiesta apparentemente valida

Vediamo quelli più noti

**200 OK**
- la richiesta ha avuto successo; l'oggetto richiesto viene inviato nella risposta
**301 Moved Permanetly**
- L'oggetto richiesto è stato trasferito; la nuova posizione è specificata nell'intesatzione `Location` della risposta
**400 Bad Request**
- Il messaggio di richiesta non è stato compreso dal server
**404 Not Found**
- Il documento richiesto non si trova sul server
**406 Not Acceptable**
- L'oggetto richiesto non esiste in una forma che soddisfa i vari `Accept-*`
**505 HTTP Version Not Supported**
- Il server non ha la versione di protocollo HTTP