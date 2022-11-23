# Da ER a Modello Relazionale

- Ogni **entità** diventa una relazione (o tabella)
- Ogni **attributo di entità** diventa un attributo di relazione,ossia una **colonna di tabella** ereditando le caratteristiche dell'attributo da cui deriva
- L'**identificatore univoco di una entità** diventa la **chiave primaria (PK)** della relazione

La rappresentazione di una tabella avviene tramite il suo schema: 
_nomerelazione(nome_attributo,nome_attributo,...)_
![[appunti bsd/mod i/immagini/Pasted image 20221123150119.png|center|600]]

## ER->Modello Relazionale (1:1)

La relazione 1:1 diventa un'unica relazione che contiene gli attributi della prima e della seconda entità

**Esempio con partecipazione obbligatoria**.
![[appunti bsd/mod i/immagini/Pasted image 20221123150316.png|center|600]]


![[appunti bsd/mod i/immagini/Pasted image 20221123150444.png|center|700]]
![[appunti bsd/mod i/immagini/Pasted image 20221123150728.png|center|700]]

La relazione 1:1 con una entità con _partecipazione opzionale_ viene trattata come una _associazione uno a molti_ scegliendo l'entità con _partecipazione opzionale come se fosse a molti_

Se _entrambe_ le entità partecipano in modo opzionale si tratta come una _associazione molti a molti_

**Esempio con partecipazione opzionale da un lato**
![[appunti bsd/mod i/immagini/Pasted image 20221123151117.png|center|700]]

**Esempio**
![[appunti bsd/mod i/immagini/Pasted image 20221123151207.png|center|700]]

**Esempio con partecipazione opzionale da entrambi i lati**
![[appunti bsd/mod i/immagini/Pasted image 20221123151553.png|center|700]]

**Esempio**
![[appunti bsd/mod i/immagini/Pasted image 20221123151731.png|center|700]]











