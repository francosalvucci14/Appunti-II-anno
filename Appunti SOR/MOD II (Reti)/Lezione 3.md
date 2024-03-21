# Sicurezza di rete

Internet non è stata progettata pensando molto alla sicurezza

Ora bisogna pensare a :
- Come i malintenzionati possono attaccare le reti informatiche
- Come possiamo difendere le reti dagli attacchi
- Come progettare architetture immuni agli attacchi

## Malintenzionati : Intercettazione dei pacchetti

**Analisi dei pacchetti (packet sniffing)**
- media broadcast (Ethernet condivisa,wireless)
- un'interfaccia di rete promiscua legge/registra tutti i pacchetti che l'attraversa

![[Pasted image 20240320143040.png|center|500]]

Uno dei software più diffusi e usati è WireShark

## Malintenzionati : Identità falsa

**IP spoofing** : Iniezione di pacchetti con indirizzo sorgente falso

![[Pasted image 20240320143305.png|center|500]]

Usi :
- Ostacolare indentificazione/blocco di una soregente di attacco (vedi DoS dopo)
- Sfruttare relazione di fiducia tra gli host
- Indirizzare messaggi di risposta verso B, montando un'attacco di negazione di servizio contro B (vedi DoS) basato sull'amplificazione del traffico generato da C

## Malintenzionati : Negazione di servizio (Denial-of-Service, DoS)

**Negazione del servizio (DoS)** : Gli aggressori rendono una rete, un hosto o altro elemento infrastrutturale non disponibili per gli utenti leggittimi

Esistono 3 categorie di attacchi DoS :
- _Attacchi alla vulnerabilità dei sistemi_ : invio di (pochi) pacchetti costruiti ad arte per causare il blocco di un servizio o lo spegnimento di un host, sfruttando vulnerabilità delle applicazioni o dei sistemi operativi
- _Bandwidth flooding_ (inondazione di banda) : Invio massimo di pacchetti all'host obiettivo impedendo al traffico leggittimo di raggiungerlo
- _Connection flooding_ (inondazione di connessioni) : Stabilire un gran numero di connessioni TCP con l'host obietivo, impedendogli di accettare le connessioni legittime.

**Bandwidth flooding**

L'attaccante invia traffico a una velocitò prossima a $R_s$

![[Pasted image 20240320144023.png|center|500]]

Una singola sorgente di attacco potrebbe avere una velocità di accesso insufficiente (tipicamente $R_c\lt\lt R_s$) e sarebbe comunque facile da indentificare e bloccare

**Distribuited Denial of Service (DDoS)**

1. Selezionare l'obiettivo
2. Irrompere negli host attraverso la rete (vedi botnet)
3. Inviare pacchetti verso l'obiettivo da host compromessi (bot)

![[Pasted image 20240320144148.png|center|300]]

## Linee di difesa

- **Autenticazione** : dimostrare che siete chi dite di essere
- **Riservatezza** : Attraverso la cifratura
- **Integrità** : Le firme digitali prevengono/rilevano le manomissioni
- **Restrizioni di accesso** : VPN protette da password
- **Firewalls** : "Middlebox" specializzate nelle reti di accesso e di base
	- off-by-default : filtrare i pacchetti in entrata per limitare i mittenti, i destinatari e le applicazioni
	- rilevare/reagire agli attacchi DoS

---
# Livelli di protocollo e modelli di riferimento

Le reti sono complesse, con molti "pezzi"
- host
- router
- mezzi trasmissivi
- applicazioni
- protocolli
- hardware,software

C'è una qualche speranza di organizzare l'architettura delle reti

## Stratificazione

Approccio alla progettazione/discussione di sistemi complessi

- Una struttura esplicita consente l'identificazione dei vari componenti dei vari componenti di un sistema
	- Analisi del **modello di riferimento a strati**
- La modularizzazione facilita la manutenzione e l'aggiornamento di un sistema
	- Modifica dell'implementazione del servizio del livello : trasparente al resto del sistema
	- Es. le modifiche alla procedura di gate non influiscono sul resto del sistema

### Potenziali svantaggi

Un livello può duplicare funzionalità del livello inferiore

Necessità di violare la separazione tra livelli, perchè un livello ha bisogno di una informazione disponibile solo all'interno del livello inferiore

## Pila di protocolli (protocol stack) di Internet

- **Applicazione (application layer)** : Supporto alle applicazioni di rete
	- HTTP,IMAP,SMTP,DNS
- **Trasporto (transport layer)** : Trasferimento di dati tra processi (in esecuzione su host differenti)
	- TCP,UDP
- **Rete (network layer)** : Trasferimento di paccheti di rete, deti datagrammi, da un host all'altro
	- IP, Protocolli di instradamento
- **Collegamento (link layer)** : Trasferimento di dati tra elementi di rete vicini
	- Ethernet, 802.11 (WiFi), PPP
- **Fisico (physical layer)** : Bit "sul filo"

![[Pasted image 20240321095113.png|center|150]]

### Servizi, Stratificazione e Incapsulamento

![[Pasted image 20240321095231.png|center|600]]

![[Pasted image 20240321095251.png|center|600]]

![[Pasted image 20240321095314.png|center|600]]

![[Pasted image 20240321095331.png|center|600]]

### Modello di servizio (service model)

Insieme di servizi offerti da un livello a quello superiore

I diversi servizi possono essere implementati da protocolli diversi

Il livello di collegamento può offire servizi diversi in base al protocollo impiegato sul link

Inoltre, un protocollo a livello di collegamento può prevedere protocolli diversi, a livello fisico, dipendentemente dalla tecnologia di trasmissione e dal mezzo trasmissivo del link. Ethernet, ad esempio, ha molti protocolli dello strato fisico : es. uno per il doppino intrecciato, uno per la fibra, etc...

### Incapsulamento

L'idea è quella di usare l'effetto matrioska

![[Pasted image 20240321095758.png|center|500]]

![[Pasted image 20240321095824.png|center|500]]

![[Pasted image 20240321100011.png|center|500]]

### n-PDU : implementazione dei livelli

>[!definition]- n-PDU (Protocol Data Unit)
>è la singola unità di informazione scambiata tra pari attraverso un protocollo di livello n
>- Specifiche informazioni di controllo per il protocollo
>- Carico Utile (payload) . in genere una (n+1)-PDU


![[Pasted image 20240321100123.png|center|300]]

## Modello di riferimento ISO/OSI

Nel modello ISO/OSI ci sono due strati che nella pila di protocolli non esistono, essi sono:
- **Presentazione** : Consente alle applicazioni di interpretare il significato dei dati, ad esempio crittografia, compressione, convenzioni specifiche della macchina, etc...
- **Sessione** : Sincronizzazione, checkpointing, ripristino dello scambio dati

Dato che nella pila di protocolli questi due strati mancano, *se necessari* devono essere implementati nelle applicazioni

![[Pasted image 20240321100723.png|center|200]]

