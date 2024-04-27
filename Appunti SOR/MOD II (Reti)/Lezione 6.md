```table-of-contents
title: 
style: nestedList # TOC style (nestedList|inlineFirstLevel)
minLevel: 0 # Include headings from the specified level
maxLevel: 0 # Include headings up to the specified level
includeLinks: true # Make headings clickable
debugInConsole: false # Print debug info in Obsidian console
```
# Problema : Risoluzione dei nomi

Le **persone** hanno molti identificatori :
- Nome
- Codice fiscale
- Numero della carta di intentità
- etc...

**Host e router** :
- Indirizzo IP (32 bit) - usato per indirizzare i datagrammi
- "nome" ad esempio `cs.umass.edu`

**Domanda** : Come possiamo mappare indirizzi Ip e nomi?

Un primo approccio è il file **hosts (/etc/hosts) in POSIX**, che associa un indirizzo IP a uno o più hostname

```
185.300.10.1 host1
185.300.10.2 host2 merlin
```

Il file è locale a un nodo, il suo contenuto non deve necessariamente coincidere con quelli di altri nodi

La soluzione è quella di usare un DNS (Domain Name Server)

# DNS

>[!definition]- Domain Name Server (DNS)
>- Il DNS è un **database distribuito** implementato in una gerarchia di **name server**
>- E' un protocollo a livello di applicazione che consente agli host, ai router e ai server DNS di comunicare per _**risolvere**_ i nomi (traduzione nome/indirizzo)

>[!warning]- Osservazione
>Le funzioni critiche di Internet vengono **implementate come protocolli a livello di applicazione**

## Servizi e struttura

I servizi che offre un DNS sono molteplici, infati abbiamo :
- Traduzione deglo hostname in indirizzi IP (più comune)
- Host aliasing
	- Nome canonico e alias
- Mail server aliasing
- Load distribution (distribuzione del carico di rete)
	- Server WEB replicati : più indirizzi IP corrispondono a un solo nome

**Q** : Perchè non centralizzare il DNS?
- Un *single point of failure*
- Volume di traffico
- Database centralizzato distante
- Manutenzione
**R** : Il DNS non scala!

Possiamo pensare al DNS come

- Un enorme database distribuito
	- Con $\sim$ miliardi di record, ciascuno di essi semplice
- Che gestisce molti *trilioni* di interrogazioni al giorno
	- *molte* più letture che scritture
	- *è importante* che quasi tutte le transizioni Internet interagiscono con il DNS
- è organizzativamente e fisicamente decentralizzato
	- milioni di organizzazioni diverse sono responsabili dei loro record

![[Pasted image 20240416150218.png|center|600]]

**Esempio**

Il client vuole l'indirizzo IP di `www.amazon.com`
- Il client interroga il root server per trovare il TLD server per .com
- Il client interroga il TLD server .com per ottenere il server autoritativo per `amazon.com`
- Il client interroga il server autoritativo per `amazon.com` per ottenere l'indirizzo IP di `www.amazon.com`

## Root name server

![[Pasted image 20240416152900.png|center|500]]

Ufficiale, contatto di ultima istanza da parte dei name server che non sono in grando di risolvere il nome
- Fornisce gli indirizzi IP dei TLD server

Questa è una funzione incredibilmente importante di Internet
- Internet non potrebbe funzionare senza
- DNSSRC - offre sicurezza (autenticazione, integrità dei messaggi)

l'ICANN (Internet Corporation for Assigned Names and Numbers) gestisce il root DNS domain

## TLD e Server Autoritativi

>[!definition]- Top-Level Domain (TLD) server
>- Si occupano dei domini .com, .org, .net, .edu, .aero, .jobs, etc..., e di tutti i domain locali di alto livello
>- Network Solutions : gestisce i server TLD per i domini .com e .net
>- Educause : Gestisce quelli per .edu

>[!definition]- DNS server autoritativo
>- Sono server DNS propri di ciascuna organizzazione, che forniscono i mapping ufficiali da hostname a IP per gli host dell'organizzazione
>- Possono essere mantenuti dall'organizzazione o dal service provider

## DNS locali

Quando l'host effettua una richiesta DNS, la query viene inviata al suo server DNS *locale* (con funzione di default name server)

Il sever DNS locale restituisce una risposta, rispondendo :
- Dalla sua cache locale di coppie nome->indirizzo (possibilmente non aggiornate)
- Inoltrando la richiesta alla gerarchia DNS per la risoluzione
Ciascun ISP ha un proprio server DNS locale, per trovare il vostro lanciare il comando :
- `ipconfig /all`

Il server DNS locale non appartiene strettamente alla gerarchia dei server

## DNS : Interrogazioni
### DNS : Interrogazione Iterativa

**Esempio** : l'host `engineering.nyu,edu` vuole l'indirizzo IP di `gaia.cs.umass.edu`

**Query iterativa**
- Il server contattato risponde con il nome del server da contattare

![[Pasted image 20240416154948.png|center|500]]

Il TLD DNS potrebbe conoscere in realtà un DNS server itermedio, ad esempio nel caso di domini di terzo livello, aventi ciascuno il proprio DNS server autoritativo

### DNS : Interrogazione Ricorsiva

**Esempio** : l'host `engineering.nyu,edu` vuole l'indirizzo IP di `gaia.cs.umass.edu`

**Interrogazione ricorsiva**
- Affida il compito di tradurre il nome al server contattato
- C'è un carico pesante ai livelli superiori di gerarchia?

![[Pasted image 20240416160225.png|center|500]]

## DNS : caching e aggiornamento dei record

Una volta che un (qualsiasi) name server impara la mappatura, la mette nella *cache*, e restituisce *immediatamente* il mapping nella cache di risposta a una query:
- Il caching migliora i tempi di risposta
- Le voci della cache vanno in timeout (scompaiono) dopo un certo tempo (**TTL**)
- I server TLD sono in genere memorizzati nella cache dei server dei nomi locali

Le voci nella cache potrebbero essere *obsolete*
- Se l'host con nome cambia il suo indirizzo IP, potrebbe non essere conosciuto su internet fino alla scadenza di tutti i TTL

## Record, Messaggi e Sicurezza DNS
### Record DNS

>[!definition]- Record RR
>DNS : database distribuito che memorizza 7 record di risorsa (**RR**)
>Formato RR : `(name, value, type, ttl)`

Ci sono 4 tipi per i RR

- `Type=A`
	- name è l'hostname
	- value è l'indirizzo IP
- `Type=CNAME`
	- name è il nome alias di qualche nome "canonico" (esempio `www.ibm.com`, in realtà diventa `servereast.backup2.ibm.com`)
	- value è il nome canonico
- `Type=NS`
	- name è il dominio
	- value è l'hostname dell'authoritative name server per questo dominio
- `Type=MX`
	- value è il nome del server di posta associato a name

### Messaggi DNS

**Domande** (query) e messaggi di **risposta** (reply), entrambi con lo stesso formato

Intestazione del messaggio :
- **Identificazione** : Numero di 16 bit per la domanda; la risposta alla domanda usa lo stesso numero
- **Flag** :
	- domanda o risposta
	- richiesta di ricorsione
	- ricorsione disponibile
	- DNS server autoritativo

![[Pasted image 20240427104526.png|center|400]]

- Sezione delle domande : campi per il nome richiesto e il tipo di domanda
- Sezione delle risposte : RR nella risposta alla domanda
- Sezione autoritativa : Record per server autoritativi
- Sezione aggiuntiva : Informazioni extra che possono esse usate

### Sicurezza del DNS

Vediamo 2 attacchi molto famosi e diffusi

**Attacchi DDoS (Distribuited Denial of Service)**
- Bombardare di traffico il root server
	- Finora senza successo
	- FIltraggio del traffico
	- I server DNS locali mantengono in cache gli indirizzi IP dei server TLD. consentendo di aggirare i roiot server
- Bombdardare i server TLD
	- Potenzialmente più pericoloso

**Attacchi di spoofing**
- Intercettare le query DNS, restituendo risposte fasulle
	- DNS cache poisoning

----
# Architettura Peer-to-Peer (P2P)

Descriviamo sinteticamente la struttura dell'architettura P2P

Struttura :
- Nessun server è sempre attivo
- Sistemi periferici arbitrari comunicano direttamente
- I peer richiedono un servizio ad altri peer e forniscono un servizio in cambio di altri peer
	- **scalabilità intrinseca** - Nuovi peer portano nuove capacità di servizio e nuove richieste di servizio
- I peer sono connessi a intermittenza e cambiano indirizzo IP
	- Gestione complessa

![[Pasted image 20240427105325.png|center|350]]

## Distribuzione di file : Client-Server vs P2P

**D** : Quanto tempo ci vuole per distribuire un file (di dimensione $F$) da un server a $N$ peer?
- La capacità di upload/download dei peer è una risorsa illimitata

![[Pasted image 20240427105551.png|center|500]]

### File distribution time : client-server

- **Trasmissione via server** : Deve inviare (caricare) in sequenza $N$ copie di file :
	- Tempo per inviare una copia $\frac{F}{u_s}$
	- Tempo per inviare $N$ copie : $N\frac{F}{u_s}$
- **Client** : ogni client deve scaricare una copia del file
	- $d_{\text{min}}$ = banda di download più bassa
	- Tempo di download per il client con banda minima è almeno $\frac{F}{d_{\text{min}}}$

Quindi, il tempo necessario per distribuire $F$ a $N$ client usando l'approccio client-server è $$D_{\text{c-s}}\geq\max\{\underbrace{N\frac{F}{u_s}}_{\text{Aumenta lineramente in N}},\frac{F}{u_s}\}$$
### File distribution time : P2P

- **Trasmissione via server** : Deve trasmettere almeno una copia del file :
	- Tempo per inviare una copia $\frac{F}{u_s}$
- **Client** : ogni client deve scaricare una copia del file
	- $d_{\text{min}}$ = banda di download più bassa
	- Tempo di download per il client con banda minima è almeno $\frac{F}{d_{\text{min}}}$

I client devono scaricare $NF$ bit
- Capacità totale di upload (che limita la massima velocità di download) è $u_s+\sum\limits u_i$

Quindi, il tempo necessario per distribuire $F$ a $N$ client usando l'approccio P2P è $$D_{\text{P2P}}\geq\max\{\frac{F}{u_s},\frac{F}{d_{\text{min}}},\frac{\overbrace{NF}^{\text{Aumenta lineramente in N}}}{\underbrace{u_s+\sum\limits u_i}_{\text{Ma anche questo, dato che ogni peer porta con sè la capacità di servizio}}}\}$$
### Client-Server vs P2P : Esempio

Banda di upload del client = $u,\frac{F}{u}$ = 1 ora, $u_s=10u,d_{\text{min}}\geq u_s$

![[Pasted image 20240427110848.png|center|500]]

