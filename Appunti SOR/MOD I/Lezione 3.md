# Le chiamate di sistema (o System Call)

Le chiamate di sistema sono **l'interfaccia che il sistema operativo offre alle applicazioni per richiedere servizi**

**Problema** : 
- Il meccanismo delle system call è **altamente specifico** del SO e dell'hardware
- La **necessità di efficienza esaspera** questo problema

**Soluzione** : 
- Incapsulare le chiamate di sistema nella libreria C (libc)
- Tipicamente esporta **una chiamata di libreria per ogni chiamata di sistema**
- UNIX libc si basa sulla libreria C POSIX

## I 10 passi per effettuare una chiamata di sistema

Per vedere i passagi vedi figura

- **Preparazione dei parametri** . il programma chiamate prepara i parametri, solitamente memorizzandoli nei registri o nello stack (RDI,RSI,RDX) (passaggi da 1 a 3)
- **Chiamata alla procedura di libreria**: Il programma effettua la chiamata alla procedura di libreria (passaggio 4)
- **Collocazione del numero di chiamata di sistema** : Colloca il numero della chiamata di sistema in un registro, come RAX (passaggio 5)
- **Passagio a modalità kernel** : Si esegue un'istruzione "**trap**" (ad esempio, SYSCALL in x86-64) (passaggio 6)
	- l'istruzione "trap" è simile a una chiamata di procedura ma cambia la modalità in modalità kernel
	- può saltare solo ad indirizzi specifici o indici di una tabella di memoria, a differenza della chiamata di procedura.
- **Esecuzione del gestore di chiamate di sistema** : Il gestore di chiamate di sistema specifico viene eseguito (passaggio 8)
- **Ritorno alla procedura di libreria utente** : Il controllo può essere restitutio alla procedura di libreria utente (passaggio 9)
- **Possibilità di blocco** : La chiamata di sistema può bloccare il chiamante,ad esempio, se l'input desiderato non è disponibile
	- Il SO può quindi eseguire altri processi
- **Ripresa dopo il blocco** : Quando l'input o le condizioni desiderate sono disponibili, il processo bloccato viene ripreso :
	- Tornando alla procedura di libreria utente e procedento all'istruzione successiva (passaggio 10)

![[Pasted image 20231014095842.png|center|500]]

## Chiamate di sistema per la gestione dei processi

| Call                              | Descrizione                                               |
| --------------------------------- | --------------------------------------------------------- |
| pid fork()                        | Creare un processo figlio identico al padre               |
| pid waitpid(pid,&statloc,options) | Attendere che un processo figlio termini                  |
| s = execve(name,argv,environp)    | Sostituire l'immagine centrale di un processo             |
| exit(status)                      | Terminare l'esecuzione del processo e restituire lo stato |

Queste sono alcune delle principali chiamate del sistema POSIX

## Chiamate di sistema per la gestione dei file

| Call                               | Descrizione                                      |
| ---------------------------------- | ------------------------------------------------ |
| fd = open(file,how,...)            | Apre un file per la lettura,scrittura o entrambe |
| s = close(fd)                      | Chiude un file aperto                            |
| n = read(fd,buffer,nbytes)         | Legge dati da un file in un buffer               |
| n = write(fd,buffer,nbytes)        | Scrive dati da un buffer in un file              |
| position = lseek(fd,offset,whence) | Sposta il puntatore del file                     |
| s = stat(name,&buf)                | Ottiene informazioni sullo stato di un file      |

- fd è un descrittore di file
- n è il conteggio di byte
- position è l'offset all'interno di un file

## Chiamate di sistema per la gestione del file system

| Call                         | Descrizione                                   |
| ---------------------------- | --------------------------------------------- |
| s = mkdir(name,mode)         | Crea una nuova directory                      |
| s = rmdir(name)              | Rimuove una directory vuota                   |
| s = link(name1,name2)        | Crea una nuova voce, nome2, che punta a nome1 |
| s = unlink(name)             | Rimuove una voce dalla directory              |
| s = mount(special,name,flag) | Monta un file system                          |
| s = umount(special)          | Smonta un file system                         |

 

