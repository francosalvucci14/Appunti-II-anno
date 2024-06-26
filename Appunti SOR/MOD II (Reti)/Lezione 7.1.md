
```table-of-contents
title: 
style: nestedList # TOC style (nestedList|inlineFirstLevel)
minLevel: 0 # Include headings from the specified level
maxLevel: 0 # Include headings up to the specified level
includeLinks: true # Make headings clickable
debugInConsole: false # Print debug info in Obsidian console
```
# Livello di trasporto

**Obiettivi**
- Capire i principi che sono alla base dei servizi del livello di trasporto:
	- multiplexing/demultiplexing
	- trasferimento dati affidabile
	- controllo di flusso
	- controllo della congestione

Conoscere i protocolli del livello di trasporto di Internet
- UDP: trasporto senza connessione
- TCP: trasporto orientato alla connessione
- controllo della congestione TCP

## Servizi e protocolli di trasporto

Forniscono la **comunicazione logica** tra processi applicativi di host differenti

I protocolli di trasporto vengono eseguiti nei sistemi periferici:
- Lato invio : scinde (se necessario) i messaggi dell'applicazione, combinando ciascuna parte con un'intestazione per creare un **segmento** e lo passa a livello di rete
- Lato ricezione: riassembla i segmenti in messaggi e li passa al livello applicazione

I router nel cammino da un host all'altro operano solo sull'intestazione del datagramma, ignorando il segmento incapsulato al suo interno

Più protocolli di trasporto sono a disposizione delle applicazioni
- TCP,UDP

![[Pasted image 20240520121138.png|center|400]]

### Relazione tra livello di trasporto e livello di rete

- **Livello di trasporto** : Comunicazione logica tra ***processi***
	- Si basa sui servizi del livello di rete e li potenzia

- **Livello di rete** : Comunicazione logica tra ***host***

### Protocolli del livello di trasporto in Internet

- **UDP** : User Datagram Protocol
	- Inaffidabile, consegne senz'ordine
	- Estensione "senza fronzoli" di IP: solo comunicazione tra processi e controllo degli errori
- **TCP** : Transmission Control Protocol
	- Comunicazione tra processi affidabile, consegne nell'ordine originario
	- Controllo di flusso
	- Controllo della congestione
	- Instaurazione della connessione

Servizi *non* disponibili:
- Garanzie sui ritardi
- Garanzie su ampiezza di banda

## Multiplexing/Demultiplexing

![[Pasted image 20240520121653.png|center|500]]

**Esempio di demultiplexing**

![[Pasted image 20240520121727.png|center|150]]

![[Pasted image 20240520121748.png|center|300]]

**Esempio di multiplexing**

![[Pasted image 20240520121827.png|center|150]]

![[Pasted image 20240520121854.png|center|300]]

### Come funziona il demultiplexing

L'host riceve i datagrammi IP
- Ogni datagramma ha un indirizzo IP di origine e un indirizzo IP di destinazione
- Ogni datagramma trasporta 1 segmento a livello di trasporto
- Ogni segmento ha un numero di porta di origine e un numero di porta di destinazione

L'host usa gli **indirizzi IP e i numeri porta** per inviare il segmento alla socket appropriata

![[Pasted image 20240520122406.png|center|300]]

#### Demultiplexing senza connessione

Quando si crea una socket, si deve specificare il numero di porta:
```C
mySocket=socket(AF_INET,SOCK_DGRAM)
mySocket.bind(('',9157))
```

Quando si crea il datagramma da inviare al socket UDP, si deve specificare :
- Indirizzo IP di destinazione
- Numero di paoorta di destinazione

Il segmento viene passato al livello di rete

Quando l'host riceve il segmento UDP:
- Controlla il numero della porta di destinazione nel segmento
- Invia il segmento UDP alla socket con quel numero di porta

Datagrammi IP/UDP con lo ***stesso indirizzo IP e numero di porta di destinazione***, ma indirizzi IP e/o numeri di porta di origine differenti vengono inviati alla ***stessa socket*** sull'host ricevente

![[Pasted image 20240520134414.png|center|500]]
#### Demultiplexing orientato alla connessione

La socket TCP è identificata da **quattro parametri** :
- Indirizzo IP di origine
- Numero di porta di origine
- Indirizzo IP di destinazione
- Numero di porta di destinazione

**Demux** : Il lato ricevente usa i ***quattro valori*** (quadrupla) per inviare il segmento alla socket appropriata

Un host serverr crea una socket passiva specificando un numero di porta

La *socket passiva* viene usata per accettare le richieste di connessione, per ciascuna delle quali verrà creata una nuova *socket connessa* (con la medesima porta e indirizzo IP locale, ma diversa porta e indirizzo remoto, discriminando pertanto le socket connese di client diversi)

![[Pasted image 20240520134752.png|center|500]]

## Trasporto senza connessione : UDP

UDP = Protocollo di trasporto di Internet "senza fronzoli"

Servizio di consegna "best effort" (massimo sforzo), i segmenti UDP possono essere :
- Perduti
- Consegnati fuori sequenza all'applicazione

**Senza connessione** :
- No handshaking tra mittente e destinatario UDP
- Ogni segmento UDP è gestito indipendentemente

>[!error]- Perchè esisite UDP?
>- Nessuna connessione stabilita (che potrebbe aggiungere ritardo)
>- Semplice : nessuno stato di connessione nel mittente e nel destinatario (perciò un server può gestire più client)
>- Intestazioni di segmento corte
>- Senza controllo della congestione
>	- UDP può sparare dati a raffica
>- Controllo più preciso a livello di applicazione su quali dati sono inviati e quando

Utilizzo di UDP:
- Applicazioni per lo streaming multimediale (tolleranti alle perdite, sensibili alla frequenza)
- DNS
- SNMP
- HTTP/3

Trasferimento affidabile con UDP (ad esempio, HTTP/3):
- Aggiungere affidabilità a livello di applicazione
- Aggiungere controllo della congestione a livello di applicazione

### UDP: azioni del livello di trasporto

![[Pasted image 20240520141900.png|center|500]]

![[Pasted image 20240520141923.png|center|500]]

![[Pasted image 20240520141942.png|center|500]]

### Struttura dei segmenti UDP

![[Pasted image 20240520142003.png|center|500]]

#### Checksum UDP

**Obiettivo** : Rilevare gli "errori" (bit alternati) nel segmento trasmesso

![[Pasted image 20240520142052.png|center|500]]
#### Checksum Internet

**Obiettivo** : Rilevare gli "errori" (bit alternati) nel segmento trasmesso

**Mittente** :
- Tratta il contenuto del segmento come una sequenza di interi da 16 bit
- *checksum* : complemento a 1 della somma della sequenza di interi a 16 bit
- pone il valore della cheksum nel campo checksum del segmento UDP

**Ricevente** :
- Calcola la cheksum allo stesso modo del mittente
- Il risultato è costituito da tutti bit 1
- Altre implementazioni verificano la checksum calcolandola e confrontandola col valore restituito