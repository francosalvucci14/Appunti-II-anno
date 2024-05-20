
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



#### Demultiplexing orientato alla connessione

## Trasporto senza connessione : UDP