```table-of-contents
title: 
style: nestedList # TOC style (nestedList|inlineFirstLevel)
minLevel: 0 # Include headings from the specified level
maxLevel: 0 # Include headings up to the specified level
includeLinks: true # Make headings clickable
debugInConsole: false # Print debug info in Obsidian console
```
# Streaming video e reti di distribuzione di contenuti

## Streaming video e CDN : Contesto

Traffico video in streaming :
- Grando consumantore di larghezza di banda Internet

**Sfida** : Scalabilità - Come raggiungere $\sim 1B$ utenti?
**Sfida** : Eterogeneità - Utenti diversi hanno esigenze diverse (ad esempio cablati o mobili; ricchi di banda o poveri di banda; etc...)

**Soluzione** : Infrastruttura distribuita a livello di applicazione

## Contenuti multimediali : Video

>[!definition]- Video
>Un video è una sequenza di immagini visualizzate a tasso costante (**frame rate**)

>[!definition]- Immagine digitale
>Un immagine digitale è un **array di pixel**, dove ogni pixel è rappresentato da un bit

>[!definition]- Codifica
>Utilizzare la ridondanza ***all'interno*** e ***tra*** le immagini per ridurre il numero di bit utilizzati per la codifica dell'immagine
>Ci sono 2 tipi di codifica :
>- **Spaziale** : Si trova all'interno dell'immagine
>- **Temporale** : Si trova da un'immagine all'altra


![[Pasted image 20240427112054.png|center|350]]

Diamo ancora un paio di definizioni

>[!definition]- CBR (Constant Bit Rate)
>Bit rate costante

>[!definition]- VBR (Variable Bit Rate)
>Bit rate che cambia con la quantità di codifica spaziale e temporale

## Streaming video di contenuti registrati

Scenario semplice

![[Pasted image 20240427112347.png|center|400]]

Sfide principali :
- La larghezza di banda da server a client varia nel tempo, con il variare dei livelli di congestione della rete
- La perdità di pacchetti, i ritardi dovuti alla congestione ritardano la riproduzione o comportano una scarsa qualità video

![[Pasted image 20240427112624.png|center|500]]

**Vincolo di riproduzione continua** : quando la riproduzione inizia, dovrebbe procedere secondo i tempi di registrazione origianali
- Ma i ritardi di rete sono variaibli (**jitter**), quindi avrà bisogno di un buffer lato client per soddisfare i vincoli di riproduzione continua

Altre sfide :
- Interattività del client : Pausa, avanzamento veloce, riavvolgimento, salti attraverso il video
- I pacchetti video possono essere persi, ritrasmessi

