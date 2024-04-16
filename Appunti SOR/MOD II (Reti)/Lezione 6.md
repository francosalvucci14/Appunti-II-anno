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

