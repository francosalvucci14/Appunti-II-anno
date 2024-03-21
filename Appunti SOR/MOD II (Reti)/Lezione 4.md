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
