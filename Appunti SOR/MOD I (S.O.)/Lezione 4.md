# Struttura di un SO

## Struttura sistema monolitico

In un SO **monolitico**, il programma principale invoca le chiamate di sistema richieste

Il kernel è un blocco monolitico con:
- Procedure di servizio che eseguono le chiamate di sistema
- Procedure di utilità che aiutano a implementare le procedure di servizio

![[Pasted image 20231018120543.png|center|500]]

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

L'organizzazione stratificata dei sistemi operativi è una generalizzazione dell'approccio monolitico

Il sistema THE fu uno dei primi a implementare questa idea, con sei livelli gerarchici:
- Questi livelli gestivano l'allocazione del processore, la memoria, la comunicazione, l'I/O, i dispositivi, e gli utenti

Il sistema MULTICS usava anelli concentrici per definire i privilegi, con livelli interni più privilegiati di quelli esterni

Vantaggi :
- Protezione delle risorse e dati critici
- Separazione chiara dei compiti

![[Pasted image 20231018122049.png|center|400]]

- **Kernel Unificato** : Tutte le funzionalità centralizzate in un unico kernel
- **Interconnesione** : Ogni componente ha la capacità di richiamare qualsiasi altro componente
- **Scalabilità** : Questa struttura può diventare complessa e meno gestibile con l'evoluzione del sistema

![[Pasted image 20231018122247.png|center|400]]

## Struttura di un sistema operativo: Virtualizzazione

Inventato negli anni '70 per separare la multiprogrammazione della macchina estesa. Oggi di nuovo interesse in diversi ambiti. N interfacce di chiamata di sistema indipendenti dal sistema operativo. 

![[Pasted image 20231025114905.png|center|450]]

Virtual Machine Monitor (_VMM_) o Hypervisor emula l'hardware.

- _Type 1_ : VMM viene eseguito sul "pezzo di ferro" ( direttamente su HW, come Xen);
- _Type 2_ : VMM ospitato nel sistema operativo ( esempio: QEMU);
- _Hybrid_ : VMM all'interno del sistema operativo ( esempio: KVM). 

![[Pasted image 20231025115043.png|center|500]]
## Container

I container possono eseguire più istanze di un sistema operativo su una singola macchina. Ogni container divide il kernel del sistema operativo host e i file binari e le librerie ( il container non contiene il sistema operativo completo e può quindi essere leggero ). Gli svantaggi dei container:

1. Non è possibile eseguire un container con un sistema operativo completamente diverso da quello dell'host;
2. A differenza delle macchine virtuali, non esiste un rigido partizionamento delle risorse;
3. I container sono isolati a livello di processo ( se un container altera la stabilità del kernel sottostante, ciò può influire sugli altri container ).

## Struttura di un sistema operativo : EXOKERNEL

_Idea_: Separare il controllo delle risorse dalla macchina estesa. Simile ad un VMM/Hypervisor, ma:

- Exokernel non emula l'hardware.
- Fornisce solo una condivisione sicura delle risorse a basso livello. Ogni macchina virtuale a livello utente esegue il suo sistema operativo, ma è limitata a utilizzare solo le risorse assegnate. Rispetto ad altri approcci, l'exokernel elimina la necessità di mappature complesse, concentrandosi solo su quale macchina virtuale ha accesso a quali risorse.

## Struttura di un sistema operativo : UNIKERNEL

Gli Unikernel sono sistemi minimi basati su LibOS, progettati per eseguire una singola applicazione su una macchina virtuale ( es. WebServer ). Questi sistemi contengono solo la funzionalità necessaria per supportare l'applicazione specifica, come un server web, su una macchina virtuale. Gli unikernel sono altamente efficienti poiché non richiedono protezione tra il sistema operativo (LibOS). Esiste solo un'applicazione per macchina virtuale. Il concetto degli unikernel è stato recentemente riscoperto, offrendo una soluzione leggera ed efficiente per eseguire applicazioni isolate su macchine virtuali.

## Struttura di un sistema operativo: MicroKernel-based client/server

Organizza le _service procedure_ che vengono eseguiti in modo separato. processes _System Servers/Drivers_ I processi di sistema comunicano attraverso il passaggio di messaggi. Le chiamate di sistema si basano sullo stesso meccanismo di messaggistica. Meccanismo di messaggistica implementato nel kernel minimale

_Microkernel_. 

![[Pasted image 20231025115425.png|center|500]]

_Pro_: è più facile aderire al Principle of Least Authority (POLA):
- Trusted Computing Base ( TCB ) relativamente "piccolo";
- Ogni processo del sistema operativo può fare solo ciò che è necessario per svolgere il proprio compito;
- La compromissione, ad esempio, del driver di stampa non influisce sul resto del sistema operativo.

_Contro_:
- Il passaggio di messaggi è più lento di una chiamata di funzione (come in un kernel monolitico).







