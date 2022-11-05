- [[Lezione 4 - Vincoli d'integrità#Vincoli di integrità|Vincoli di integrità]]
- [[Lezione 4 - Vincoli d'integrità#Vincoli di ennupla|Vincoli di ennupla]]
- [[Lezione 4 - Vincoli d'integrità#Chiavi e schemi di relazione|Chiavi e schemi di relazione]]
- [[Lezione 4 - Vincoli d'integrità#Chiavi e valori nulli|Chiavi e valori nulli]]
- [[Lezione 4 - Vincoli d'integrità#Vincoli di integrità referenziale|Vincoli di integrità referenziale]]

# Vincoli di integrità
Esistono istanze di basi di dati che, pur sintatticamente corrette, non rappresentano informazioni possibili per l'applicazione di interesse.

**Esempio**
![[appunti bsd/immagini/Pasted image 20221105112059.png|center|600]]

_Def_
Proprietà che deve essere soddisfatta dalle istanze che rappresentano informazioni corrette per l'applicazione
Un vincolo è una funzione booleana (un **predicato** basato sulla logica del prim'ordine) che associa ad ogni istanza il valore **vero** o **falso**
I vincoli di integrità consentono una descrizione più accurata della realtà e vengono usati dai DBMS nella esecuzione delle interrogazioni

## Tipi di vincoli
- vincoli **intrarelazionali**:
	- vincoli su valori (o di **dominio**)
	- vincoli su **ennupla**
- vincoli **interrelazionali**

# Vincoli di ennupla

Esprimono condizioni sui valori di ciascuna ennupla, indipendentemente dalle altre ennuple
Caso particolare:
- **vincoli di dominio**: coinvolgono un solo attributo
Una possibile sintassi:
- espressione booleana di atomi che confrontano valori di attributo o espressioni aritmetiche su di essi
![[appunti bsd/immagini/Pasted image 20221105112635.png|center|500]]

**Esempio**
![[appunti bsd/immagini/Pasted image 20221105112832.png|center|600]]


# Chiavi e schemi di relazione

## Identificatore delle ennuple

- Non ci sono due ennuple con lo stesso valore sull'attibuto **Matricola**
- Non ci sono due ennuple uguali su tutti e tre gli attibuti **Cognome,Nome,Data di Nascita**
![[appunti bsd/immagini/Pasted image 20221105113142.png|center|600]]



# Chiavi e valori nulli
# Vincoli di integrità referenziale

