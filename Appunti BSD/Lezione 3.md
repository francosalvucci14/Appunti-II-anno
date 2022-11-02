
- [[Appunti BSD/Lezione 3#Modello Relazionale|Modello Relazionale]]
- [[Appunti BSD/Lezione 3#Strutture Nidificate|Strutture Nidificate]]
- [[Appunti BSD/Lezione 3#Informazione incompleta|Informazione incompleta]]

# Modello Relazionale

Modello proposto da E. F. Codd nel 1970 per favorire **l'indipendenza dei dati**
Disponibile in **DBMS reali nel 1981**
Si basa sul concetto matematico di **relazione(con una variante)**. Le relazioni hanno naturale rappresentazione per mezzo di **tabelle**

## Relazione Matematica
- $D_1,..,D_n$: insieme anche non distinti detti **domini**
- il **prodotto cartesiano** $D_1\times...\times D_n$ è definito come: l'insieme di tutte le **n-uple($d_1,..,d_n$)** tali che $d_1\in D_1,...,d_n\in D_n$
- Una **relazione matematica** su $D_1,...,D_n$ è un sottoinsieme di $D_1\times...\times D_n$
- $D_1,...,D_n$ sono i **domini della relazione**

**Esempio**
![[appunti bsd/immagini/Pasted image 20221102200220.png|center|500]]

### Relazione Matematica: Proprietà

Una relazione matematica è un insieme di n-uple ordinate: $(d_1,...,d_n)|d_1\in D_1,...,d_n\in D_n$
Una relazione è un **insieme**, quindi:
- _non c'è ordinamento_ fra le n-uple;
- le n-uple sono _distinte_
- _ciascuna n-upla è ordinata_: l'i-esimo valore proveien dall'i-esimo dominio



# Strutture Nidificate
# Informazione incompleta

