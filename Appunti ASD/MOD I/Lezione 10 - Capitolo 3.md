
# Strutture dati elementari

## Gestione di collezioni di oggetti

**Tipo di dato**:
- Specifica una collezione di oggetti e delle operazioni di interesse su tale collezione (es. inserisci,cancella,cerca)

**Struttura dati**:
- Organizzazione dei dati che permette di memorizzare la collezione e supportare le operazioni di un tipo di dato usando meno risorse di calcolo possibile

### Il tipo di dato Dizionario

![[appunti asd/mod i/immagini/Pasted image 20221117092001.png|center|600]]

### Il tipo di dato Pila

![[appunti asd/mod i/immagini/Pasted image 20221117092056.png|center|600]]

### Il tipo di dato Coda

![[appunti asd/mod i/immagini/Pasted image 20221117092140.png|center|600]]

## Tecniche di rappresentazione dei dati

**Rappresentazione indicizzate**:
- I dati sono contenuti (principalmente) in array

**Rappresentazioni collegate**:
- I dati sono contenuti in record collegati fra loro mediante puntatori

### Proprietà

**Rappresentazioni indicizzate**:
- Array: collezione di celle numerate che contengono elementi di un tipo prestabilito

>[!important]- Proprietà
>**(forte)**: gli indici delle celle di un array sono numeri consecutivi
>**(debole)**: non è possibile aggiungere nuove celle ad un array

**Rappresentazioni collegate**:
- i constituenti di base sono i _record_
- i record sono numerati tipicamente con il loro _indirizzo di memoria_
- record creati e distrutti individualmente e dinamicamente
- il collegamento tra un record A e un record B è realizzato tramite un puntatore

>[!important]- Proprietà
>**(forte)**: è possibile aggiungere o togliere record a una struttura collegata
>**(debole)**: gli indirizzi dei record di una struttura collegata non sono necessariamente consecutivi

**Esempi di strutture collegate**
![[appunti asd/mod i/immagini/Pasted image 20221117093120.png|center|600]]

### Pro e contro

**Rappresentazioni indicizzate**:
- **Pro**: accesso diretto ai dati mediante indici
- **Contro**: dimensione fissa (riallocazione array richiede tempo lineare)

**Rappresentazioni collegate**:
- **Pro**: dimensione variabile (aggiunta e rimozione record in tempo costante)
- **Contro**: accesso sequenziale ai dati

**Realizzazione di un dizionario**

Metodo più semplice: **array non ordinato** (sovradimensionamento)

- **Insert**: costa $O(1)$ - inserisco dopo l'ultimo elemento
- **Search**: costa $O(n)$ - devo scorrere l'array
- **Delete**: costa $O(n)$ - delete = search+cancellazione

**Array ordinato**:

- **Search**: $O(log(n))$ - ricerca binaria
- **Insert**: $O(n)$ - Ho bisogno di $O(log(n))$ confronti per trovare la giusta posizione in cui inserire, $O(n)$ trasferimento per mantenere l'array ordinato
- **Delete**: $O(n)$

...e con le liste?

**Lista non ordinata**:

- **Insert**: costa $O(1)$
- **Search**: costa $O(n)$
- **Delete**: costa $O(n)$

**Lista ordinata**:

- **Insert**: costa $O(n)$ - devo manterene ordinata la lista
- **Search**: costa $O(n)$ - non posso usare la ricerca binaria
- **Delete**: costa $O(n)$

## Alberi

### Organizzazione gerarchica dei dati

![[appunti asd/mod i/immagini/Pasted image 20221117095717.png|center|600]]

Dati contenuti nei **nodi**, relazioni gerarchiche definite dagli **archi** che li collegano

![[appunti asd/mod i/immagini/Pasted image 20221117095848.png|center|700]]

- **grado di un nodo**: numero dei suoi figli
- **albero d-ario,albero d-ario completo**

_Def_
u si dice **antenato** di v se u è raggiungibile da v risalendo di padre in padre
v si dice **discendente** di u se u è un antenato di v


