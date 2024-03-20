# Nucleo di rete

Il nucleo di rete è una maglia (mesh) di commutatori di pacchetti e colelgamenti che interconnettono i sistemi periferici di Internet

**Commutazione di pacchetto (packet-switching)**

I sistemi periferici suddividono i messaggi di livello applicativo in **pacchetti (packets)**
- La rete **inoltra(forwards)** i pacchetti da un router al successivo attraverso i collegamenti (links), lungo un **percorso (path o route)** dalla sorgente alla destinazione

## Due funzioni chiave del nucleo di rete

![[Pasted image 20240319151347.png|center|600]]

## Commutazione di Pacchetto

### Store-and-Forward

![[Pasted image 20240319151649.png|center|500]]

**Ritardo (delay) di trasmissione** : Servono $\frac{L}{R}$ secondi per trasmettere (transmit) pacchetti di $L$ bit attraversi un collegamento a $R$ bps

**Store and Forward** : Il router deve aver ricevuto l'intero pacchetto prima di poter cominciare a trasmettere sul collegamento in uscita

**Esempio Numerico**

- $L=10$ kbit
- $R=100$ Mbps
- Ritardo di trasmissione $$\frac{\text{10 kbit}}{\text{1000 Mbps}}=\frac{10*10^{3}\text{ bit}}{100*10^6\frac{\text{bit}}{\text{s}}}=0.1*10^{-3}s=\text{0.1 ms}$$
Altri esempi

![[Pasted image 20240319152053.png|center|500]]
![[Pasted image 20240319152108.png|center|500]]

>[!definition]- Formula del ritardo da un capo all'altro di 1 pacchetto
>Il ritardo da un capo all'altro (end-to-end) per la trasmissione di 1 pacchetto su un percorso di N collegamenti di pari velocità R è $$d_{\text{end-to-end}}=N\frac{L}{R}$$

**Trascurando il ritardo di propagazione e altre forme di ritardo**

>[!definition]- Formula del ritardo da un capo all'altro di P pacchetti
>Il ritardo da un capo all'altro (end-to-end) per la trasmissione di P pacchetti su un percorso di N collegamenti di pari velocità R è $$d_{\text{end-to-end}}=(N+P-1)\frac{L}{R}$$

**Trascurando il ritardo di propagazione e altre forme di ritardo**

### Accodamento

L' **accodamento** (queuing) si verifica quando il lavoro arriva più velocemente di quanto possa essere servito

![[Pasted image 20240319154148.png|center|500]]

>[!definition]- Accodamento dei pacchetti e perdite
>Se il tasso di arrivo (arrival rate) (in bps) al collegamento eccede il tasso di trasmissione (bps) del collegamento per un certo periodo di tempo, si verificano i seguenti casi:
>- I pacchetti si accodano in attesa di essere trasmessi sul collegamento in uscita
>- I pacchetti possono essere scartati (persi) se la memoria (buffer) si riempie

## Commutazione di circuito

Le risosrse richieste lungo un percorso (buffer e velocità di trasmissione sui collegamenti) per consentire la comunicazione tra sistemi periferici sono riservate per lìintera durata della sessione di comunicazione

- Risorse dedicate : Nessuna condivisione
	- Trasferimento dati a velocità costante
- I segmenti del circuito restano inattivi se non utilizzati (nessuna condivisione)
- Usato comunemente nella rete telefonica

![[Pasted image 20240319154841.png|center|400]]

### FDM e TDM

**Multiplexing a Divisione di Frequenza (FDM)** :
- Spettro di frequenza di un collegamento suddiviso in bande (band)
- Ogni circuito ha una propria banda, può trasmettere alla velocità massima di quella banda ristretta

![[Pasted image 20240319154902.png|center|400]]

**Multiplexing a Divisione di Tempo (TDM)** :
- Tempo suddiviso (frame) di durata fissa, ripartiti in un numero fisso di slot
- Ciascun circuito riceve slot periodici, può trasmettere alla massima velocità della banda di frequenza più ampia, solo nei propri slot temporali

![[Pasted image 20240319154925.png|center|400]]

## Commutazione di pacchetto vs commutazione di circuito

Esempio
- Collegamento a 1 GB/s
- Ogni utente
	- 100 Mb/s quando "attivo"
	- attivo per il $10\%$ del tempo

**D**: quanti utenti possono usare questa rete sotto la commutazione di circuito e sotto la commutazione di pacchetto ?

**R1** : Con commutazione di circuito abbiamo 10 utenti
**R2** : Con commutazione di pacchetto : con 35 utenti, la probabilità che $\gt 10$ utenti attivi in contemporanea è meno di $0.0004$ [^1]

La commutazione di pacchetto è una "vincitrice assoluta" ?

- Ottimo per i dati a "raffica"
	- Più semplice, non necessità l'impostazione delal chiamata
- **Eccessiva congestione** : Ritardo e perdita di pacchetti in caso di buffer overflow
	- Sono necessari protocolli per il trasferimento affidabile dei dati e per il controllo della congestione
- **Ritardi end-to-end variabili e imprevedibili** : A causa della variabilità e imprevedibilità dei ritardi di accodamento
	- Servizi in tempo reale

## Struttura di internet : "rete di reti"

I sistemi periferici accedono a Internet tramite i cosidetti **Internet Service Provider (ISP)** di accesso

Gli ISP di accesso devono essere interconnessi a loro volta, in modo che due host qualsiasi possano inviare pacchetti l'uno all'altro

La rete di reti risultatno è molto complessa

![[Pasted image 20240320111943.png|center|500]]

**Domanda** : Dati milioni di ISP di accesso, come collegarli tra loro?

![[Pasted image 20240320112105.png|center|500]]

![[Pasted image 20240320112546.png|center|500]]

**Opzione** : Collegare ogni ISP di accesso a un ISP globale di transito

![[Pasted image 20240320112558.png|center|500]]

Ma se un ISP globale è un attività vantaggiosa, ci saranno concorrenti

![[Pasted image 20240320112716.png|center|500]]

![[Pasted image 20240320112738.png|center|500]]

![[Pasted image 20240320112805.png|center|500]]

![[Pasted image 20240320112850.png|center|500]]

![[Pasted image 20240320112910.png|center|500]]

Al "centro" : un piccolo numero di grandi reti ben connesse
- **ISP commerciali "tier-1"** : Copertura nazionale & internazionale
- **Rete di fornitori di contenuti** : reti private che connetono i suoi data center a Internet, spesso aggirando ISP tier-1 e regionali

# Prestazioni

## Come si verificano ritardi e perdite?

I pacchetti si **accodano** nei bufferi dei router, aspettando il proprio turno per la trasmissione
- La lunghezza della cosa cresce quando il tasso di arrivo dei pacchetti sul collegamento eccede (temporaneamente) la capacità del collegamento di evaderli

La **perdita** di pacchetti di verifica quando la memoria che contiene la coda dei pacchetti si riempie

![[Pasted image 20240320113510.png|center|500]]

### Ritardo per i pacchetti : quattro cause

![[Pasted image 20240320113644.png|center|500]]

$$d_{\text{nodo}}=d_{\text{elab}}+d_{\text{acc}}+d_{\text{trasm}}+d_{\text{prop}}$$

$d_{\text{elab}}$ = **elaborazione di nodo**
- Controllo errori sui bit
- Determinazione del canale in uscita
- Tipicamente $\lt$ microsecondi

$d_{\text{acc}}$ = **ritardo di accodamento**
- Attesa di trasmissione
- Dipende dal livello di congestione del router

$d_{\text{trasm}}$ = **ritardo di trasmissione**
- $L$ : Lunghezza del pacchetto (in bit)
- $R$ : Tasso di trasmissione del collegamento (in bps)
- $d_{\text{trasm}} = \frac{L}{R}$

$d_{\text{prop}}$ = **ritardo di propagazione**
- $d$ : lunghezza del collegamento fisico
- $v$ :  velocità di propagazione ($\simeq 2\times 10^8\frac{m}{s}$ )
- $d_{\text{prop}} = \frac{d}{v}$

In genere $d_{\text{elab}},d_{\text{prop}}$ sono molto diversi

## Commutazione di pacchetto : ritardo end-to-end

I ritardi totali di nodo cui è in corso un pacchetto lungo il suo percorso, dalla sorgente alla destinazione si accumulano, determinando un ritardo end-to-end pari a
$$d_{\text{end-to-end}}=\sum\limits_i(d_{\text{elab}_i}+d_{\text{acc}_i}+d_{\text{trasm}_i}+d_{\text{prop}_i})$$
## Ritardo dei pacchetti (rivisitato)

- $a$ velocità media di arrivo dei pacchetti
- $L$ : lunghezza del pacchetto (in bit)
- $R$ : velocità di trasmissione (in bit/s)

**Intensità di traffico** : $\frac{La}{R}=\frac{\text{velocità di arrivo dei bit}}{\text{velocità di servizio dei bit}}$

![[Pasted image 20240320121228.png|center|300]]

- $\frac{La}{R}\sim0$ : Ritardo medio di accodamento piccolo
- $\frac{La}{R}\sim1$ : Ritardo medio di accodamento grande
- $\frac{La}{R}\gt1$ : Più "lavoro" in arrivo di quanto possa essere servito - ritardo tende all'infinito

### Ritardi e percorsi in Internet

Ma cosa significano effettivamente ritardi e perdite nella "vera" Internet?

**Traceroute** : Programma diagnostico che fornisce una misura del ritardo dalla sorgente al router lungo i percorsi Internet punto-punto verso la destinazione
Per ogni i:
- Invia tra pacchetti che raggiungeranno il router i sul percorso verso la destinazione (con il campo time-to-live uguale i)
- Il router i restituirà i pacchetti al mittente
- Il mittente calcola l'intervallo tra trasmissione e risposta

![[Pasted image 20240320134036.png|center|500]]

**Esempio di traceroute**

![[Pasted image 20240320134149.png|center|600]]


[^1]: 0.0004 si ottiene dalla formula $$1-\sum\limits_{i=0}^{10}P(\text{utenti attivi}=i)=1-\sum\limits_{i=0}^{10}{35\choose i}0.1^i(1-0.1)^{35-i}=1-\sum\limits_{i=0}^{10}\frac{35!}{i!(35-i)!}0.1^i(1-0.1)^{35-i}\leq0.0004$$