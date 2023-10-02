# Argomenti

- Anomalie di uno schema
- Normalizzazione
- Dipendenze funzionali
- Forme Normali
	- Prima forma normale (**1NF**)
	- Seconda forma normale (**2NF**)
	- Terza forma normale (**3NF**)
	- Boyce Codd (**BCNF**)
	- Quarta e quinta forma normale
- Normalizzazione e decomposizione

# Anomalie di uno schema

## Semantica di un buon schema

**Linea guida 1** : Informalmente, ogni tupla in una relazione dovrebbe rappresentare un'entità o un'istanza di relazione (Si applica alle relazioni individuali e ai loro attributi)

Gli attributi di diverse entità (DIpendenti, dipartimenti, progetti) **non dovrebbero essere mescolati** nella stessa relazione

Per riferirsi ad altre entità dovrebbero essere usare solo le chiavi esterne

**Gli attributi di entità e di relazioni diverse** dovrebbero essere tenbuti il più possibile separati

Progettare uno schema che possa essere spiegato facilmente relazione per relazione. La semantica degli attributi dovrebbe essere facile da interpretare

## Ridondanze e anomalie di aggiornamento

Mischiare attributi di più entità può causare problemi

**Le informazioni vengono memorizzate in modo ridondante sprecando spazio di archiviazione**

Problemi con le anomalie di aggiornamento : 
- Anomalie di inserimento
- Anomalie di eliminazione
- Anomalie di modifica

### Esempio di anomalia di aggiornamento

Si consideri la relazione :
```EMP_PROJ(Emp#,Proj#,Ename,Pname,No_hours)```

**Anomalia dell'aggiornamento** : La modifica del nome del numero di progetto P1 da "Fatturazione" a "Customer-Accounting" può causare l'aggiornamento per tutti i 100 dipendenti che lavorano al progetto P1

**Anomalia d'inserimento** : Non è possibile inserire un progetto a meno che non abbia un dipendente assegnato - Al contrario, impossibile inserire un dipendente a meno che un lui/lei è assegnato a un progetto

**Anomalia di cancellazione** : Quando un progetto viene eliminato, ciò comporterà l'eliminazione di tutti i dipendenti che lavorano su quel progetto. In alternativa, se un dipendente è l'unico dipendente di un progetto, l'eliminazione di tale dipendente comporterebbe l'eliminazione del progetto corrispondente

![[appunti bsd/mod ii/immagini/Pasted image 20231002130435.png|center]]

![[appunti bsd/mod ii/immagini/Pasted image 20231002130548.png|center]]

## Anomalie e valori nulli

**Linea guida 2** : Progettare uno schema che non risenta dele anomalie di inserimento, cancellazione e aggiornamento. Se sono presentim annotarle in modo che le appliocazioni possano tenerne conto

**Linea guida 3** : Le relazioni dovrebbero essere progettate in modo tale che le loro tuple abbiano il minor numero possibile di **valori NULL**

Gli attributi che sono spesso NULL potrebbero essere collocati in relazioni separate (con la chiave primaria)

Motivi per i nulli : 
- **attributo non applicabile o non valido**
- **attributo valore sconosciuto (può esistere)**
- **valore noto per esisitere, ma non disponibile**

