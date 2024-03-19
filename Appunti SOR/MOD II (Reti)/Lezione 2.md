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

[^1]: 0.0004 si ottiene dalla formula $$1-\sum\limits_{i=0}^{10}P(\text{utenti attivi}=i)=1-\sum\limits_{i=0}^{10}{35\choose i}0.1^i(1-0.1)^{35-i}=1-\sum\limits_{i=0}^{10}\frac{35!}{i!(35-i)!}0.1^i(1-0.1)^{35-i}\leq0.0004$$