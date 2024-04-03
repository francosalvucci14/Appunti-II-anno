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

![[Pasted image 20240403114505.png|center|500]]

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

