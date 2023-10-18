# Struttura di un SO

## Struttura sistema monolitico

In un SO **monolitico**, il programma principale invoca le chiamate di sistema richieste

Il kernel è un blocco monolitico con:
- Procedure di servizio che eseguono le chiamate di sistema
- Procedure di utilità che aiutano a implementare le procedure di servizio

![[appunti sor/mod i croce/img/Pasted image 20231018120543.png|center|500]]

### Alcune considerazioni

1) **Sistemi Operativi Monolitici** : Un approccio al desgin `tutto in uno`
	- Il kernel è un'unica unità grande e interconnessa
	- Tutte le funzioni del SO, come la gestione dei processi, la gestione della memoria e la gestione dei dispositivi I/O, sono strettamente integrate in un unico spazio di indirizzamento

2) **Flassibilità vs Complessità** : 
	- Offre una certa flessibilità in termini di prestazioni e design
	- Tuttavia, dato che è strettamente interconnesso, un bug o un errore in una parte del sistema può causare problemi in altre parti, potenzialmente portando a crash sistemici

3) **Compilazione e Collegamento** : 
	- Tutte le funzioni e procedure del sistema operativo devono essere compilate e collegate in un unio eseguibile del kernel

4) **Mancanza di occultamento** : 
	- Tutte le procedure possono, in teoria, accedere a qualsiasi altra procedura o variabile all'interno del kernel
	- Non c'è un vero e proprio "occultamento" o isolamento tra le diverse parti del sistema

5) **Utilizzo di "trap"** : 
	- Meccanismo attraverso il quale un programma può richiedere i servizi del sistema operativo
	- Avviene attraverso interruzioni software che trasferiscono il controllo al sistema operativo

6) **Una "struttura a tre strati"** : 
	- Una suddivisione del sistema in livelli, spesso user mode, kernel mode e hardware, con il "trap" che agisce come meccanismo di comunicazione tra questi livelli

7) **Estensioni cariabili** : 
	- Molti sistemi operativi permettono di caricare dinamicamente componenti aggiuntivi, come driver di dispositivi o file system, senza dover riavviare o ricompilare l'intero sistema operativo
	- Questi componenti possono essere caricati e scaricati a seconda delle necessità, offrendo una certa modularità anche in un sistema monolitico

8) **Librerie Condivise e DLL** :
	- Sia UNIX che Windows supportanto l'idea di librerie di codice che possono essere condivise tra più programmi:
		- In UNIX, queste sono chiamate "librerie condivise"
		- In Windows sono chiamate "DYnamic Link Libraries (DLL)"
	- Contengono codice che può essere eseguito da più programmi contemporaneamente, riducendo la necessità di avere copie multiple del medesimo codice in memoria





