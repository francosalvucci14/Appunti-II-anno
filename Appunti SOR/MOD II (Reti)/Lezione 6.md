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

Un primo approccio è il file `hosts (/etc/hosts) in POSIX`, che associa un indirizzo IP a uno o più hostname

```
185.300.10.1 host1
185.300.10.2 host2 merlin
```

Il file è locale a un nodo, il suo contenuto non deve necessariamente coincidere con quelli di altri nodi

