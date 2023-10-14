# Introduzione ai concetti base dei S.O

Un **moderno calcolatore** è tipicamente formato da:
- Uno o più processori
- Memoria centrale
- Dischi, stampanti e altre periferiche I/O

I dettagli di basso livello sono **molto complessi**

Gestire tutte queste componenti richiede uno strato intermedio software : il **Sistema Operativo**

## Lo zoo dei sistemi operativi

Esistono vari tipi di SO, per vari scopi:

- SO per mainframe
- SO per server
- SO per PC
- SO per smartphone e computer palmari
- SO per IOT e SO embedded
- SO real-time
- SO per smart card

**Cosa hanno in comune?**

_Extendet Machine_ : 
- Estensione delle funzionalità hardware
- Astrazione dell'hardware
- Nascondere i dettagli al programmatore

_Resourcer Manager_ : 
- Protegge l'uso simultaneo/non sicuro delle risorse
- Condivisione equa delle risorse
- Resource accountig/limiting

## Concetti "base" di un SO

Il SO offre funzionalità attraverso le chiamate di sistema

Gruppi di chiamate di sistema implementano vari servizi, ad esempio : 

- File System Service
- Process Management Service
- ...

>[!definition]- Processi
>I **processi** sono astrazioni a livello utente, che servono ad eseguire un programma per conto dell'utente

Ogni processo ha il proprio spazio di indirizzamento

I dati coinvolti nell'elaborazione vengono recuperati e memorizzati in file.

I file persistono rispetto ai processi

### Cosa è un processo?

Concetto chiave in tutti i sistemi operativi

>[!definition]-  Programma in esecuzione
>Il processo è associato : 
>- a uno spazio di indirizzi[^1]
>- un insieme di risorse
>	- registri
>	- file aperti
>	- allarmi
>	- ...

Il processo può essere pensato come un contenitore
- Contiene tutte le informazioni necessarie per l'esecuzione del programma

#### Il layout di un processo

Il layout di un processo dipende da : 
- Archiettura della macchina
- Il SO
- Il programma

Very basic layout :

- Stack: Active call data
- Data : Program variables
- Text: Program code

![[appunti sor/mod i croce/img/Pasted image 20231013112427.png|center|200]]

#### Il ciclo di vita di un processo

Le informazioni sui processi sono conservate nella tabella dei processi del sistema operativo

Un processo sospeso consiste in un voce della tabella dei processi (registri salvati e altre informazioni necessarie per riavviare il processo) e nel suo spazio degli indirizzi

Durante il suo ciclo di vita, il processo attraversa vari stati : 

- **NEW** : il programma è stato richiesto e aspetta di entrare in memoria centrale
- **READY** : il programma è diventato una serie di processi,sta in MC, e aspetta di poter utilizzare la CPU
- **RUNNING** : il processo è in esecuzione perchè gli è stato assegnato il processore, e da questa situazione può uscire se : 
	- termina
	- arriva un processo con maggiore priorità
	- è finito il tempo di esecuzione a disposizione
	- se deve operare in I/O
- **WAITING** : il processo si trova in questo stato quando aspetta di svolgere un'operazione di I/O
- **TERMINATED** : il processo ha svolto il suo compito e rilascia l'output, insieme a tutte le risorse da lui utilizzate

Gestione dei processi : 
- Operazioni come la **creazione**,la **terminazione**, la **pausa** e la **ripresa** di un processo

Un processo può creare un'altro processo, conosciuto come "processo figlio". Questo crea una gerarchia (o albero) di processi

**Esempio di albero dei processi**

![[appunti sor/mod i croce/img/Pasted image 20231013113841.png|center|300]]

Come possiamo vedere, il processo A ha creato due figli, B e C. Il processo B ha creato altri tre figli, i processi D,E,F

#### Chi "possiede" un processo?

I processi sono "di proprietà"  di un utente, che viene identificato da un **UID** (User ID)
- Ogni processo, tipicamente, contiene l'UID dell'utente che lo ha generato
- Su sistemi UNIX, un processo figlio ha lo stesso UID del processo padre
- Gli utenti possono essere membri di gruppi, indetificati da un **GUID** (Group User ID)

Un processo (lanciato da superuser/root/administrator) è speciale, perchè ha più privilegi e quindi più liberta nelle operazioni

**Esempio di processo**

![[appunti sor/mod i croce/img/Pasted image 20231013115002.png|center]]

Possiamo notare dall'immagine che il processo che esegue il comando "gnome-shell", ha come **PID** (Process ID) il numero 2968, ed è associato all'utente "acronimo"

### File

>[!definition]-  File
>Un **file** è un'astrazione di un dispositivo di memorizzazione (eventualmente) reale (ad esempio, un disco)

è possibile leggere e scrivere dati da/su file fornendo una posizione e una quantità di dati da trasferire

I file vengono collocati in directory (o cartelle):
- Una directory conserva un identificatore per ogni file che contiene
- Una directory è un file a se stante

Le directory e i file formano una gerarchia : 
- La gerarchia inizia dalla "directory principale" (detta anche "directory radice", o più banalmente **root**), indicata con il simbolo `/` 
- è possibile accedere ai file in due modi :
	1) tramite percorsi assoluti (absolute path), tipo `/home/ast/todo-list`
	2) tramite percorsi relativi a partire dalla directory di lavoro corrente, ad esempio `../courses/slides1.pdf`
- Altri file possono essere montati (da **mount**) nella root, in questo caso avremo la gerarchia della sottodirectory mnt, in questo modo `/mnt/windows`

#### Diritti di accesso

I file sono "protetti" da tuple a tre bit, che sono divise per il **proprietario (owner)**, il **gruppo (group)** e gli **altri utenti (other users)**

Le tuple contengono un bit (r)ead, (w)rite e un bit e(x)ecute (ma sono disponibili più bit)

**Esempio**

![[appunti sor/mod i croce/img/Pasted image 20231013120032.png|center]]

- Il proprietario del file (in rosso), è abilitato alla scrittura,lettura ed esecuzione del file
- Il gruppo (in verde) è abilitato alla scrittura e alla lettura, ma non all'esecuzione
- Gli altri utenti (in blu) sono abilitati solamente all'esecuzione del file

**Esempio di organizzazione di un file system**

![[appunti sor/mod i croce/img/Pasted image 20231013120833.png|center|500]]

#### Accesso ai file

Di seguito viene riportata una sequenza di comandi per l'accesso ai file.

![[appunti sor/mod i croce/img/Pasted image 20231013121114.png|center|400]]

Di seguito l'elenco dei comandi : 
- **pwd** : Stampa a video l'absolute path della directory corrente
- **cd** : Entra nella directory Desktop
- **mkdir** : Crea una nuova directory
- **cat > test/hello.sh** : Permette di fare varie cose : 
	- crea il file hello.sh nella cartella test, creata precedentemente da mkdir
	- lo apre nel terminale e permette la scrittura di dati
- **chmod** : Permette di modificare i permessi del file hello.sh, nell'esempio specifico il file viene modificato in modo che sia un file eseguibile
- Nell'ultima riga viene eseguito il file hello.sh, che stampa in output "Hello World"

#### File e Pipe

Una pipe e' vista come uno pseudofile che permette la connessione tra un processo A e un processo B.

La comunicazione avviene tramite canale FIFO[^2]

> _Ex_: Se due processi A e B vogliono comunicare tramite una pipe, devono prima configurarla. Se A vuole mandare dei file a B, scrive sulla pipe come se fosse un file di output. Infatti l'implementazione di una pipe e' molto simile a quella di un file. Il processo B puo' leggere i dati di una pipe come se fosse un file di input.

Quindi in UNIX le comunicazioni tra processi sono molto simili alla normale scrittura e lettura di un file

![[appunti sor/mod i croce/img/Pasted image 20231014093317.png|center|300]]



[^2]: https://it.wikipedia.org/wiki/Pipe_(informatica)#FIFO_o_named_pipe
[^1]: https://github.com/SwagSpaad/Swag-Appunti/blob/main/SOR1.5/Lezione%202.md#spazi-degli-indirizzi

