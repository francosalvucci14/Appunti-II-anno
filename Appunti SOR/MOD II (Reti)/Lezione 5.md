
```table-of-contents
title: 
style: nestedList # TOC style (nestedList|inlineFirstLevel)
minLevel: 0 # Include headings from the specified level
maxLevel: 0 # Include headings up to the specified level
includeLinks: true # Make headings clickable
debugInConsole: false # Print debug info in Obsidian console
```

# Mantenere lo stato utente/server : i cookie

Ricorda : l'interazione HTTP GET/risposta è **senza stato (stateless)**

Nessuna nozione di scambio di messaggi HTTP in più fasi per completare una "transazione" Web
- Non è necessario che il client o il server tengano traccia dello "stato" dello scambio in più fasi
- Tutte le richieste HTTP sono indipendenti l'una dall'altra
- Non è necessario che il client nè il server siano in grado di "recuperare" da una transazione quasi completa ma mia completata

![[Pasted image 20240405103141.png|center|300]]

I siti web e il browser client usano i **cookie** per mantenere lo stato tra le transizioni

Ci sono 4 componenti:
1) Una riga di intestazione nel messaggio di _risposta_ HTTP
2) Una riga di intestazione nel messaggio di _richiesta_ HTTP
3) Un file cookie mantenuto sul sistema terminale dell'utente gestito dal browser dell'utente
4) Un database sul sito

**Esempio**
- Susan usa il browser dal portatile, visita uno specifico sito di e-commerce per la prima volta
- Quando arriva la richiesta HTTP iniziale al sito, il sito crea :
	- **Un  identificativo univoco**
	- **Una voce nel proprio database**, indicizzata dal numero identificativo
- Il server ritorna una risposta che include l'intestazione **Set-Cookie**, che contiene l'identificativo unico e che sarà aggiunto al file dei cookie
- Le successive richieste del browser di Susan per questo sito conterranno l'identificativo in una intestazione cookie

![[Pasted image 20240405104159.png|center|450]]

## Cookie

I cookie possono essere usati per :
- Autorizzazione
- Carrello degli acquisti
- Raccomandazioni
- Stato della sessione dell'utente

>[!info]- Nota
>Cookie e privacy :
>- I cookie consentono ai siti di _imparare_ molto da voi
>- Cookie persistenti di terze parti (tracking cookies) consentono il tracciamento di una identità comune attraverso siti web multipli

**Sfida: Come mantenere lo stato?**
- Presso gli endpoint del protocollo:
	- Mantenere lo stato presso il trasmettitore e il ricevitore attraverso multiple transazioni
- Nei messaggi:
	- I cookie trasportano lo stato nei messaggi HTTP

**Esempio**

![[Pasted image 20240405111842.png|center|500]]

### Tracciare il comportamento di navigazione di un utente

I cookie possono essere usati per:
- Tracciare (track) il comportamento degli utenti su un dato sito (**cookie di prima parte**)
- Tracciare il comportamento degli utenti su più siti (**cookie di terze parti**) senza neppure che l'utente abbia mai scelto di visitare il sito del tracekr (!)
- Il tracciamento può essere _invisibile_ all'utente
- Tracciamento di terze parti tramite cookie:
	- Disabilitato per impostazione predefinita nei browser Firefox e Safari
	- Eliminazione graduale dei cookie di terze parti nel brwoser Chrome, inizialmente bloccati per l'1% degli utenti a partire da Gennaio 2024, con l'obiettivo di estendere il blocco a tutti nel terzo trimestre del 2025

# Web cache

**Obiettivo** : soddisfare la richiesta del client senza coinvolgere il server d'origine (**origin server**)

L'utente configura il browser per usare una **Web Cache**

Il browser trasmette tutte le richieste HTTP alla cache
- **Se** l'oggetto è nella cache: la cache fornisce l'oggetto al client
- **Altrimenti** la cache richiede l'oggetto al server d'origine, memorizza l'oggetto ricevuto, e infine lo restituisce al client

![[Pasted image 20240405112941.png|center|400]]
## Web cache (server proxy)

La cache opera come client (per il server d'origine) e come server (per il client originale)

Il server comunica al client la cache consentita dell'oggetto nell'intestazione della risposta
- `Cache-Control: max-age=<seconds>`
- `Cache-Control: no-cache`

**Perchè** il web caching?
- Riduce i tempi di risposta alle richieste dei client
	- La cache è più vicina ai client
- Riduce il traffico sul collegamento di accesso a Internet istituzionale
- Internet è ricca di cache
	- Consente ai provider "scadenti" di fornire dati con efficacia

### Esempio di Caching

**Scenario** :
- Velocità collegamento d'accesso : $1.54$ Mbps
- RTT dal router istituzionale al server : $2$ s
- Dimensione di un oggetto : $100K$ bits
- Frequenza media di richieste dai browser istituzionali al server d'origine $15/s$
	- Velocità media di trasmissione dei dati ai browser $1.50$ Mbps

**Prestazioni** :
- Utilizzazione del collegamento d'accesso : $.97$ (problema : ritardo d'accodamento elevato con elevata utilizzazione)
- Utilizzazione della LAN : $.0015$
- end-to-end delay = Ritardo di Internet + Ritardo di collegamento d'accesso + Ritardo della LAN = $2$ s + minuti + microsecondi

![[Pasted image 20240405114205.png|center|300]]

#### Opzione 1 : collegamento d'accesso più veloce

**Scenario** :
- Velocità collegamento d'accesso : $154$ Mbps
- RTT dal router istituzionale al server : $2$ s
- Dimensione di un oggetto : $100K$ bits
- Frequenza media di richieste dai browser istituzionali al server d'origine $15/s$
	- Velocità media di trasmissione dei dati ai browser $1.50$ Mbps

**Prestazioni** :
- Utilizzazione del collegamento d'accesso : $.0097$
- Utilizzazione della LAN : $.0015$
- end-to-end delay = Ritardo di Internet + Ritardo di collegamento d'accesso + Ritardo della LAN = $2$ s + msecs + microsecondi

**Costo** : collegamento d'accesso più veloce (costoso!)

![[Pasted image 20240405114256.png|center|300]]

#### Opzione 2 : Installare una web cache

**Scenario** :
- Velocità collegamento d'accesso : $1.54$ Mbps
- RTT dal router istituzionale al server : $2$ s
- Dimensione di un oggetto : $100K$ bits
- Frequenza media di richieste dai browser istituzionali al server d'origine $15/s$
	- Velocità media di trasmissione dei dati ai browser $1.50$ Mbps

**Prestazioni** :
- Utilizzazione del collegamento d'accesso : ?
- Utilizzazione della LAN : ?
- end-to-end delay = ?

![[Pasted image 20240405114445.png|center|300]]

Come calcolare le prestazioni?

##### Calcolo dell'utilizzo del collegamento di accesso e del ritardo end-end con la cache

Supponiamo una percentuale di successo (hit rate) pari a $0.4$ :
- Il $40\%$ delle richieste sarà soddisfatto dalla cache, con ritardo basso (msec)
- Il $60\%$ delle richieste sarà soddisfatto del server d'origine
	- Tasso di trasmissione sul collegamento d'accesso $$0.6*1.50\text{ Mbps}=.9\text{ Mbps}$$
	- Utilizzazione collegamento d'accesso $\frac{0.9}{1.54}=.58$ significa basso (msec) ritardo di accodamento al collegamento d'accesso
- Ritardo end-to-end medio : $$\begin{align}0.6*\text{(ritardo dai server d'origine)}+&0.4*\text{(ritardo quando la richiesta è soddisfatta dalla cache)}\\&=\\0.6*(2.01)+&0.4*(\sim\text{msecs})\simeq1.2\text{ secs}\end{align}$$
**Ritardo medio end-end inferiore che con un collegamento a 154 Mbps**

### GET condizionale

^db726c

**Obiettivo** : Non inviare un oggetto se la cache ha una copia aggiornata dell'oggetto
- Nessun ritardo di trasmissione dell'oggetto( o suo delle risorse di rete )

***Client*** : Specifica la data della copia dell'oggetto nella richiesta HTTP
`if-modified-since: <data>`

***Server***: La risposta non contiene l'oggetto se la copia nella cache è aggiornata
`HTTP/1.0 304 Not Modified`

![[Pasted image 20240405115437.png|center|300]]

## Nota sul caching

Il caching può essere effettuato da:
- Una erb cache, ossia uno speciale tipo di proxy, cui il browser invia le richieste invece che indirizzarle all'origin server
- Oppure, dal browser stesso, che conserva una copia degli oggetti richiesti in precedenza

In entrambi i casi, occorre prestare attenzione al problema dell'aggiornamento delgi oggetti: vedi riga di intestazione [[Appunti SOR/MOD II (Reti)/Lezione 5#Web cache (server proxy)|Cache-Control]] e [[Appunti SOR/MOD II (Reti)/Lezione 5#^db726c|GET condizionale]]

# HTTP/2