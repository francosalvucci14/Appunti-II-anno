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

### Tuple spurie

Un progetto non corretto per un database relazionale può causare risultati errati per alcune operazioni JOIN

La **proprietà "lossless join"** viene utilizzata per garantire risultati significativi per le operazioni di join

**Linea guida 4** : Le relazioni dovrebbero essere progettate per soddisfare la condizione di lossless join. Non si dovrebbero creare tuple spurie facendo un natural-join di tutte le relazioni

# Normalizzazione

La **normalizzazione** è una formalizzazione teorica di alcuni problemi che possono emergere durante l'utilizzo, l'interrogazione e la gestione dei dati in un database e che possono impedire o rendere complicato l'uso delle informazioni. _Non sempre è applicabile_

Permette di costruire un DB corretto e ben definito

La normalizzazione è quindi un procedimento utile per **l'eliminazione della ridondanza** delle informazioni e per ridurre il rischio di incosistenza della base dati
Di fatto riduce la dimensione delle relazioni a partire da relazioni con concetti tra loro indipendenti

La normalizzazione dei dati può essere considerata come un processo di analisi degli schemi forniti, basato sulle loro dipendenze funzionali e chiavi primarie, per raggiungere le proprietà desiderate di :
- **Minimizzazzione della ridondanza**
- **Minimizzazione delle anomalie di inserimento, cancellazione, modifica**

# Dipendenze funzionali

Le **dipendenze funzionali** (FD) sono usate per specificare misure formali della "bontà" dei progetti relazionali

Le FD e le chiavi sono usati per definire le _**forme normali**_ per le relazioni

Le FD sono vincoli che derivano dal significato e dalle interrelazioni degli attributi dei dati

Un insieme di attributi X **determina funzionalmente** un insieme di attributi Y se il valore di **X determina un valore univoco per Y**

Si ha **dipendenza funzionale** tra attributi quando il valore di un insieme di attributi A determina un singolo valore dell’attributo B e si indica con $A\to B$. Si dice anche che B dipende da A o che A è un determinante per B

Se un attributo è chiave candidata di una relazione allora è un determinante di ogni attributo della relazione e viceversa, **un attributo che determina tutti gli altri attributi è chiave candidata.**

Si ha **dipendenza transitiva** quando A determina B e B determina C. Si dice allora che C dipende transitivamente da A

## Esempio

- Schema con anomalie

![[appunti bsd/mod ii/immagini/Pasted image 20231002142331.png|center|500]]

- Proprietà : 
	- Ogni impiegato ha un solo stipendio (anche se partecipa a più progetti)
	- Ogni progetto ha un bilancio
	- Ogni impiegato in ciascun progetto ha una sola funzione (anche se può avere funzioni diverse in progetti diversi
$$\begin{align}Impiegato&\to Stipendio\\Progetto&\to Bilancio\\Impiegato_{}Progetto&\to Funzione \end{align}$$
## Altre FD particolari

$Impiegato_{}Progetto \to Progetto$

Si tratta però di una FD “**banale**” (sempre soddisfatta)
- $Y \to A$ è _non banale_ se A non appartiene a Y
- $Y \to Z$ è _non banale_ se nessun attributo in Z appartiene a Y

Le anomalie sono legate ad alcune FD
- gli impiegati hanno un unico stipendio
$$Impiegato\to  Stipendio$$
- i progetti hanno un unico bilancio
$$Progetto \to Bilancio$$
Non tutte le FD causano anomalie
- In ciascun progetto, un impiegato svolge una sola funzione
$$Impiegato Progetto\to  Funzione$$
Il soddisfacimento è più “**semplice**”, perché Impiegato Progetto è chiave

## FD e anomalie

La terza FD corrisponde ad una **chiave** e non causa anomalie
**Le prime due FD non corrispondono a chiavi e causano anomalie**

La relazione contiene alcune informazioni legate alla chiave e altre ad attributi che non formano una chiave

Le anomalie sono causate dalla presenza di concetti eterogenei:
- proprietà degli impiegati (lo stipendio)
- proprietà di progetti (il bilancio)
- proprietà della chiave Impiegato Progetto

Un FD è una proprietà degli attributi nello schema R

Il vincolo deve valere su ogni istanza della relazione r(R)

Se K è una chiave di R, allora K determina funzionalmente tutti gli attributi in R (poiché non abbiamo mai due tuple distinte con $t_1[K]=t_2[K]$)

# Forme Normali

## Prima Forma Normale (1NF)

Uno schema di relazione R(X) con X insieme di attributi, è in 1NF **se ogni attributo appartenente ad X è un attributo semplice**.

Un attributo è un _attributo semplice_ se il suo valore è unico e indivisibile in una ennupla

- Esempio
Tabella non in 1NF: l’attributo Figli a carico contiene più valori

![[appunti bsd/mod ii/immagini/Pasted image 20231002145154.png|center]]

- Decomposizione
Tabella in 1NF: scomposizione in due tabelle

![[appunti bsd/mod ii/immagini/Pasted image 20231002145250.png|center]]


## Seconda Forma Normale (2NF)

Uno **schema di relazione R(X) è in 2NF** se è in 1NF e se ogni _**attributo non primo (non facente parte della chiave) di R(X)**_ dipende funzionalmente e completamente da ogni chiave di R(X)

- Esempio

Tabella non in 2NF: tutte le colonne corrispondenti agli attributi no chiave non dipendono dall’intera chiave primaria

![[appunti bsd/mod ii/immagini/Pasted image 20231002154817.png|center]]

Tabella in 2NF

![[appunti bsd/mod ii/immagini/Pasted image 20231002154837.png|center]]

## Terza Forma Normale (3NF) 

Uno **schema di relazione R(X) è in 3NF** se è in 1NF e se ogni attributo _**non primo**_ (non facente parte della chiave) di R(X) è dipendente in modo non transitivo da ogni chiave di R(X).

- Esempio
Tabella non in 3NF:
- telefono del Reparto ripetuto per ogni Impiegato di quel Reparto (ridondanza)
- se il telefono cambia, occorre modificare molte righe
- con errori di aggiornamento, si avrebbero telefoni differenti
- se un Reparto non ha impiegati, non si può conoscere il suo telefono

![[appunti bsd/mod ii/immagini/Pasted image 20231002155050.png|center]]

Tabella non in 3NF, dipendenze funzionali:
- CodImpiegato $\to$ Reparto
- Reparto $\to$ TelefonoReparto

![[appunti bsd/mod ii/immagini/Pasted image 20231002155115.png|center]]

Tabella in 3NF

![[appunti bsd/mod ii/immagini/Pasted image 20231002155418.png|center]]

## Forma Normale di Boyce-Codd

Una **relazione è in forma normale di Boyce-Codd (BNCF)** se è in 1NF se ogni volta che vale FD $X\to A$ in R, allora X è una superchiave di R

Ogni forma normale è strettamente più forte della precedente:
- Ogni relazione 2NF è in 1NF
- Ogni relazione 3NF è in 2NF
- Ogni relazione BCNF è in 3NF

Esistono relazioni che sono in 3NF ma non in BNCF

L'obiettivo è avere ogni relazione in BNCF (o 3NF)

![[appunti bsd/mod ii/immagini/Pasted image 20231004135041.png|center]]

## Quarta e Quinta forma normale

La quarta e quinta forma normale risolvono i problemi che si possono creare quando nella relazione sono presenti attributi multivalore, cioè attributi che possono assumere più valori in corrispondenza dello stesso valore di un altro attributo

## Quale forma normale?

è sufficiente rappresentare le relazioni in 3NF che, come si può dimostrare, ha il pregio di essere sempre ottenibile senza **perdita di informazioni** e senza perdita di **dipendenze funzionali**

Non è così invece per la forma normale di Boyce-Codd: ci sono relazioni che non possono essere normalizzate nella forma di Boyce-Codd senza perdita di dipendenze funzionali

Relazione in 3NF ma non in BNCF

![[appunti bsd/mod ii/immagini/Pasted image 20231004135516.png|center]]

# Normalizzazione e decomposizione

Che facciamo se una relazione non soddisfa la BNCF?
- La rimpiazziamo con altre relazioni che soddisfano la BNCF

Come?
- Decomponendo sulla base delle dipendenze funzionali, al fine di separare i concetti

Esempio di decomposizione

![[appunti bsd/mod ii/immagini/Pasted image 20231004144917.png|center]]

## Procedura intuitiva di normalizzazione

Non è valida in generale, ma solo nei casi "semplici"

Per ogni dipendenza $X\to Y$ che viola la BNCF, definire una relazione su XY ed eliminare Y dalla relazione originaria

Vediamo un esempio

![[appunti bsd/mod ii/immagini/Pasted image 20231004145456.png|center|400]]

Decomponiamo sulla base delle dipendenze

![[appunti bsd/mod ii/immagini/Pasted image 20231004145604.png|center|500]]

Proviamo a ricostruire

![[appunti bsd/mod ii/immagini/Pasted image 20231004145713.png|center|400]]

## Decomposizione senza perdita

Una relazione r si **decompone senza perdita** su $X_1,X_2$ se il join delle proiezioni di r su $X_1$ e $X_2$ è uguale a r stessa (cioè non contiene ennuple spurie)

La decomposizione senza perdita è garantite se gli attributi comuni contengono una **chiave** per almeno una delle relazioni decomposte

Proviamo a decomporre senza perdita

![[appunti bsd/mod ii/immagini/Pasted image 20231004150009.png|center|400]]

![[appunti bsd/mod ii/immagini/Pasted image 20231004150038.png|center|300]]

Un altro problema 
Supponiamo di voler inserire una nuova ennupla che specifica la partecipazione dell'impiegato Neri, che opera a Milano, al progetto Marte

![[appunti bsd/mod ii/immagini/Pasted image 20231004150224.png|center|500]]

![[appunti bsd/mod ii/immagini/Pasted image 20231004150253.png|center|500]]


## Composizione delle dipendenze

Una **decomposizione conserva le dipendenze** se ciascuna delle dipendenze funzionali dello schema origianrio coinvolge attributi che compaiono tutti insieme in uno degli schema decomposti

Progetto $\to$ Sede non è conservata

## Qualità delle decomposizioni

Una decomposizione dovrebbe sempre soddisfare:
- la decomposizione senza perdità, **che garantisce la ricostruzione delle informazioni originarie**
- la conservazione delle dipendenze, **che garantisce il mantenimento dei vincoli di integrità**

Esempio di relazione non normalizzata

![[appunti bsd/mod ii/immagini/Pasted image 20231004152833.png|center|500]]

In questo caso la decomposizione è problematica

Progetto Sede $\to$ Dirigente coinvolge tutti gli attributi e quindi nessuna decomposizione può preservare tale dipendenza

Quindi in alcuni casi la BCNF "non è raggiungibile"

## BCNF e Terza Forma Normale (3NF)

Una relazione r è in terza forma normale se, per ogni FD (non banale) $X\to Y$ definita su r, è verificata almeno una delle seguenti condizioni:
- X contiene una chaive K di r
- ogni attributo in Y è contenuto in almeno una chiave di r

La 3NF è meno restrittiva della forma normale di Boyce-Codd ( e ammette relazioni con alcune anomalie)

Ha il vantaggio di essere sempre "raggiungibile"

Se una relazione ha una sola chiave, allora essa è in BCNF se e solo se è in 3NF

### Decomposizione in terza forma normale

Si crea una relazione per ogni gruppo di attributi coinvolti in una dipendenza funzionale

SI verifica che alla fine una relazione contengauna chiave della relazione originaria

**Dipende dalle dipendenze individuate**

Una possibile strategia è :
- se la relazione non è normalizzata si decompone in terza forma normale
- alla fine si verifica se lo schema ottenuto è anche in BCNF

Esempio di schema non decomponibile in BCNF

![[appunti bsd/mod ii/immagini/Pasted image 20231004153729.png|center|400]]

una possibile riorganizzazione è 

![[appunti bsd/mod ii/immagini/Pasted image 20231004153820.png|center|400]]

La decomposizione in BCNF è

![[appunti bsd/mod ii/immagini/Pasted image 20231004153903.png|center|500]]

## Teoria della normalizzazione

I concetti visti possono essere formalizzati in maniera precisa
**Problema**: data una relazione r e un insieme di dipendenze funzionali definite su r, generare una decomposizione di r che:
- **Sia senza perdita e conservi le dipendenze**
- **Contenga solo relazioni normalizzate**

Faremo riferimento alla 3NF


### Implicazione dipendenze funzionali

Un insieme F di FD **implica** un'altra FD f se ogni relazione che soddisfa tutte le FD in F soddisfa anche f

Esempio : 
- R(Impiegato,Categoria,Stipendio)
- Le FD Impiegato $\to$ Categoria e Categoria $\to$ Stipendio implicano la FD Impiegato $\to$ Stipendio

### Chiusura di un insieme di attributi

Dati uno schema di relazione R(U), un insieme F di FD definite su U e un insieme di attributi X contenuti in U (cioè $X\subseteq U$): la **chiusura** di X rispetto ad F, indicata con $X^+_F$ , è l’insieme degli attributi che dipendono funzionalmente da X:
$$X^+_{F}= \{A|A\in U\land\text{F implica}\space X\to A\}$$
Se A appartiene a $X^+_F$ allora $X\to A$ è implicata da F

#### Calcolo di $X^+_F$

**Input** : un insieme X di attributi e un insieme F di dipendenze funzionali
**Output** : un insieme $X_p$ di attributi

1) Inizializziamo $X_p$ con l'insieme di input X
2) Se esiste una FD $Y\to A$ in F con $Y\subseteq X_p$ e $A\not\in X_p$ , allora aggiungiamo A a $X_p$
3) Ripetiamo il passo 2 fino a quando non ci sono ulteriori attributi che possono essere aggiunti a $X_p$

### Chiusura e Chiave

Un insieme di attributi K è chiave per uno schema di relazione R(U) su cui è definito un insieme di dipendenze funzionali F se F implica $K \to U$.

L’algoritmo appena mostrato può essere utilizzato per verificare se un insieme di attributi è chiave.

### Coperture di dipendenze funzionali

Due insiemi di dipendenze funzionali $F_1$ ed $F_2$ sono **equivalenti** se $F_1$ implica ciascuna dipendenza in $F_2$ e viceversa.

Se due insiemi sono equivalenti diciamo anche che ognuno è una **copertura** dell’altro.

Questa proprietà consente di utilizzare, dato un insieme di dipendenze, un altro, a esso equivalente, ma più semplice.

#### Proprietà desiderabili di FD

Un insieme di dipendenze F è:
- **non ridondante** se non esiste dipendenza $f\in F$ tale che $F-\{f\}$ implica f
- **ridotto** se (i) è non ridondante e (ii) non esiste un insieme F' equivalente a F ottenuto eliminando attributi dai primi membri di una o più dipendenze di F

Esempio
$$\begin{align}F_{1}= \{A\to B;AB\to C;A\to C\}&\space\text{ridondante e equivalente a }F_2\\F_2=\{A\to B;AB\to C\}&\space\text{non ridondante ma non ridotto}\\F_3=\{A\to B;A\to C\}&\space\text{RIDOTTO}\end{align}$$

### Calcolo copertura ridotta

1. Sostituiamo l’insieme dato con quello equivalente che ha tutti i secondi membri costituiti da singoli attributi;
2. Eliminiamo le dipendenze ridondanti;
3. Per ogni dipendenza verifichiamo se esistono attributi eliminabili dal primo membro

In pratica, per ogni dipendenza $Y \to A \in F$, verifichiamo se esiste $Y \subseteq X$ tale che F è equivalente a $F − \{X \to A\} \cup \{Y \to A\}$

### Progettazione e normalizzazione

La teoria della normalizzazione può essere usata nella progettazione logica per verificare lo schema relazionionale finale

**Si può usare anche durante la progettazione concettuale per verificare la qualità dello schema concenttuale**

