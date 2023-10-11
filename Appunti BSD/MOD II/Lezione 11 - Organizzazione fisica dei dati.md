# Organizzazione fisica dei dati

L'organizzazione fisica dei dati di un database deve essere **efficiente**, ciò significa che il sistema di gestione di un database (DBMS) deve avere la capacità di rispondere alle richieste dell'utente il più velocemente possibile.

I DBMS offrono i loro servizi in modo "trasparente" e permettono di farci ignorare le proprie strutture fisiche 
- il DBMS utilizza in maniera efficiente le strutture
- Abbiamo considerato il DBMS come una "scatola nera"

## Gestore degli accessi e delle interrogazioni

![[appunti bsd/mod ii/immagini/Pasted image 20231011163121.png|center|300]]

### Caratteristiche memoria secondarie

- Si chiamano così perchè i dati, per essere letti o scritti, devono essere trasferiti nella memoria principale
- Sono organizzate in **blocchi**
- Permettono la scrittura/lettura sull'intero blocco
- Il costo delle operazioni in memoria principale è trascurabile rispetto a quello di accesso a un blocco di memoria secondaria

#### I Blocchi

- Un disco è partizionato in blocchi
- I blocchi hanno formato fisso (compreso tra i 512 e 4096 byte)
- Un blocco corrisponde in genere al settore di una traccia di disco
- Il tempo di risposta si valuta in numero di accessi al disco e dipende da :
	- tempo di **posizionamento della testina** (10-50ms)
	- tempo di **latenza** (5-10ms)
	- tempo di **trasferimento** (1-2ms)

#### Il Buffer

- è un'apposita zona di memoria centrale che, nei DBMS, agisce da interazione tra memoria secondaria e memoria principale
- è organizzato in pagine con un numero intero di blocchi
- con la riduzione dei costi si hanno buffer sempre più grandi
## Organizzazione delle tuple nelle pagine

![[appunti bsd/mod ii/immagini/Pasted image 20231011163818.png|center|550]]

## Gestore del buffer

- Si occupa del caricamento/scaricamento pagine, decidendo inoltre cosa farne
- Segue la legge del 'data location' (20/80)
- Una directory descrive il contenuto correte del buffer
- Ogni pagina ha delle variabili di stato (contatore, bit di stato)
- Il gestore del buffer segue un algoritmo preciso

## Organizzazione fisica dei file

I dati sono organizzati in **file**
- i file sono divisi in **record**
	- **record logici**, quelli visibili
	- **record fisici**, con informazioni del record e campi

**Informazioni** : 
- _Puntatore_ al record
- Tipo record
- Lunghezza record
- BIt di cancellazione
- Eventuali Offset dei campi
- Eventuale puntatore al prossimo record

Un _puntatore_ è una coppia (b,k)

**Campi** :
- Eventuale offset del campo
- Campo vero e proprio

**Esempio** 

Limitare la dimensione dei file separando gli attributi con accesso frequente da quelli con minor accesso semplifica la gestione del buffer :

- Si consideri R con $T=500.000$ tuple con attributi $K,A_1,A_2$ ognuno lungo $a=5$ byte
- Si consideri un sistema con blocchi di dimensione $B=1$ Kb
- Se le operazioni più frequenti chiedono la proiezione su uno solo dei due attributi R diventa $R_1(K,A_1),R_2(K,A_2)$
- Ognuna di $\frac{T}{\frac{B}{2a}}= 5000$ blocchi -> proiezione = 5000 accessi. Altrimenti sarebbero 7500 accessi

## Strutture primarie per l'organizzazione dei file e metodi di accesso

Criteri secondo i quali sono disposte le tuple nell'ambito del file -> TIpi di file

3 TIpi di file : 
- Sequenziali (**Heap**)
- Ad accesso calcolato (**Hash**)
- Ad albero (**Isam,Btree,B+tree**)

