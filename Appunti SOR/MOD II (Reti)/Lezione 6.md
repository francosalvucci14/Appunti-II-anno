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

