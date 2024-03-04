Prof Manuel Fiorelli
# Introduzione

## Panoramica

- Cos'è Interne?
- Cos'è un protocollo?
- Host, reti di accesso, etc...
- Nucleo di rete: commutazione di un pacchetto e commutazione di circuito,struttura di internet
- Prestazioni : perdite, ritardi, throughput
- Sicurezza
- Livelli di protocollo

## Internet : descrizione degli "ingranaggi"

Miliardi di **dispositivi di calcolo** connessi :

- **host** = sistema periferico (_**end system**_)
- Eseguono le applicazioni di rete ai confini di Internet ("_edge_")

>[!definition]- Commutatori di pacchetto (packet switches)
>inoltrano i pacchetti (pezzi di dati), e possono essere:
>- router
>- switch

> [!definition]- Reti di collegamenti (communication link)
> - Fibra ottica, rame, radio, satellite
> - Tasso di trasmissione (*transmission rate*):
> 	- ampiezza di banda (*bandwidth*)

**Reti** :

- Collezione di dispositivi, router, collegamenti:
	- Gestiti da una singola organizzazione

![[Pasted image 20240304144639.png|center|500]]

![[Pasted image 20240304144706.png|center|400]]
### Dispositivi connessi a Internet

CI sono vari dispositivi che si connettono ad Internet, tra cui:

- Telecamere di sicurezza
- Frigoriferi smart
- Console di gioco
- Telefoni
- Etc...

>[!quote] Televendita di dispositivi by Giorgio Mastrota

### Sistemi periferici

Sistemi periferici in Internet :
- **PC desktop**
- **Server** (spesso raggruppati in cluster all'interno di data center)
- **Dispositivi mobile**
- altri tipi di "cose" (*things*) che in passato non erano connesse -> il termine "rete di calcolatori" sta diventando obsoleto

## Ritornando a : descrizione degli "ingranaggi"

**Internet = "Rete di Reti"**
- ISP interconnessi

> [!definition]- ISP
> ISP = Internet Service Provider, che possono essere :
> - aziendali
> - residenziali
> - pubblici
> - etc...

>[!info]- Protocolli
>I **Protocolli** sono ovunque:
>- Controllano l'invio e la ricezione dei messaggi
>- es. HTTP, Streaming Video, TCP/IP, WiFi, etc...

Gli **standard di Internet** sono :

- **RFC** : Request for Comments
- **IETF** : Internet Engineering Task Force

Altri enti di stardardizzazione sono :
- IEEE 802 LAN Standards Committee, per Ethernet e Wireless
- etc...

>[!definition]- Infrastruttura di rete
>Fornisce servizi alle applicazioni :
>- Web
>- Streaming
>- Email
>- Social Media
>- etc...
>
>Fornisce un'**interfaccia di programmazione** alle applicazioni distribuite
>- "*Hook*" che consentono alle applicazioni mittente/destinatario di "connettersi", usare il servizio di trasporto di Internet
>- Fornisce molte opzioni di servizio

## Cos'è un protocollo?

ES. Protocolli Umani :

- Che ore sono?
- Ho una domanda
- etc...

I **Protocolli sono regole** per :

- Specifici messaggi inviati
- Specifiche azioni da intraprendere alla ricezione di un messaggio o altri eventi

### Protocolli di Rete

I protocolli di rete sono simili ai protocolli umani, ad eccezzione del fatto che le entità che si scambiano i messaggi e che intraprendono azioni sono componenti hardware o software di qualche dispositivo (*Device*)

Quindi, possiamo dire che :

>[!definition]- Protocollo (definizione formale)
>Un **protocollo** definisce il **formato** e l'**ordine** dei messaggi scambiati tra due o più entità in comunicazione, così come le **azioni intraprese** in fase di trasmissione e/o ricezione di un messaggio o di un'altro evento

**Esempio di protocollo umano e di rete**

![[Pasted image 20240304144744.png|center|400]]

## Ai confini della rete

I dispositivi connessi a Internet sono detti **sistemi periferici** o **end system**, in quanto si trovano ai confini di Internet

I sistemi periferici vengono detti **host**, e si dividono in due categorie :
- **Client** : Host che richiedono servizi, quali PC, smartphone, laptop, etc..
- **Server** : Host che erogano servizi, e sono solitamente macchine più potenti dei normali PC, che sono collocati in grandi **data center**

### Reti di accesso e mezzi trasmissivi

>[!definition]- Reti di accesso (access network)
>Rete che **connette fisicamente** un sistema al suo **edge router**, che è il primo router sul percorso dal sistema d'origine a un qualsiasi altro sistema di destinazione collocato al di fuori della rete di accesso

Esistono vari tipi di reti di accesso, tra cui :

- Accesso residenziale :
	- DSL, Via Cavo, FTTH, Etc...
- Accesso aziendale :
	- Ethernet, WiFi, etc...
- Accessi wireless su scala geografica :
	- 3G, LTE 4G, 5G, etc...

#### Reti di accesso : DSL

**DSL = Digital Subscriber Line**
**DSLAM = Digital Subscriber Line Access Multiplex**

Utilizza la linea telefonica esistente verso il DSLAM nella centrale locale.

Il modem DSL converte i dati digitali in toni ad alta frequenza, per poterli trasmettere alla centrale locale sul cavo telefonico; tutti i segnali analogici in arrivo dalle abitazioni vengono riconvertiti in formato digitale nel DSLAM

Le linee telefoniche residenziali trasportano contemporaneamente dati e segnali telefonici tradizionali codificandoli in tre bande di frequenza non sovrapposte:

- Downstream (verso l'abitazione) ad alta velocità, nella banda tra 50 kHz e 1 MHz
- Upstream (verso il DSLAM) a velocità media, nella banda tra 4 e 50 kHz
- Canale telefonico ordinario a due vie, nella banda tra 0 e 4kHz

**Esempio di rete di accesso residenziale tramite DSL**

![[Pasted image 20240304145650.png|center|500]]

#### Reti di accesso : FFTTx

Si parla di Fibra Ottica

Abbiamo diversi tipi di collegamenti con fibra ottica, e sono :

- FTTH : Fiber-to-the-Home (1 Gbps in downlink)
- FTTB : Fiber-to-the-Basement
- FTTC : Fiber-to-the-Cabinet (100/200 Mbps in downlink)
- FTTN : Fiber-to-the-Node

La più usata è la FTTH, che però viene suddivisa da molte abitazioni.

Due architetture che usano questa suddivisione sono :
- **AON** (Active Optical Network) : Rete ottica attiva
- **PON** (Passive Optical Network) : Rete ottica passiva

**Esempio di FTTH tramite architettura PON**

![[Pasted image 20240304151225.png|center|500]]

**ONT = Optical Network Terminator**
**OLT = Optical Line Terminator**

Ogni casa ha un ONT, connesso a un separatore ottico (Splitter) di quartiere tramite fibra ottica dedicata
Lo splitter combina più abitazioni in una sola fibra ottica condivisa, che si connette al OLT
L'OLT, che fornisce la conversione tra segnali ottici e digitali, si connette ad Internet tramite un router 

