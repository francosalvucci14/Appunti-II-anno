# Introduzione

## Dati, informazioni e sistemi informativi
- **Dati**: In informatica. la singola informazio ecodificabile o codificata. Ciò che è immediatamente presente alla conoscenza, prima di ogni elaborazione
- **Informazione**: notizia, dato o elemento che consente di avere conoscenza più o meno esatta di fatti, situazioni, modi di essere
- [[#Sistema informativo]] 


**Esempio**
8 e Ferrari scritti su un foglio di carta sono due dati, da soli non segnificano nulla...

...se il folgio di carta è relativpo alle ordinazioni in un ristorante e sono note le regole che i camerieri devono eseguire allora il foglio rappresenta l'ordinazione di una bottiglia di spumante marca Ferrari da addebbitare alla stanza 8

**Con le indicazioni aggiuntive i dati diventano informazioni e arricchiscono la conoscenza**

- **L'evoluzione della tecnologia** permette oggi di raccogliere una grande quantità di dati, continuamente e in maniera pervasiva
**Conseguenza**: corretta e efficente gestione dati, che è sempre stata fondamentale per la buona realizzazione di qualsiasi sistema informativo

### Risorse di una organizzazione
- persone
- denaro
- materiali
- informazioni
### Funzioni di un sistema informativo
- acquisizione delle informazioni
- conservazione delle informazioni
- elaborazioni delle informazioni
- distribuzione, scambio di informazioni

### Sistema informativo
_Def_:
è la componente (**sottosistema**) di un'organizzazione che gestisce (acquisisce, elabora, conserva, produce) le informazioni d'interesse:
- Ogni organizzazione ha un sistema informativo, eventualemente non esplicitato nella struttura.
- Quasi sempre,il sistema informativo è di supporto ad altri sottosistemi, va quindi studiato nel contesto in cui è inserito
- Il sistema informativo è in genere suddiviso in sottosistemi più o meno fortemente integrati

Il concetto di "**sistema informativo**" è indipendente da qualsiasi automazione:
- Esistono organizzazioni la cui ragion d'essere è la gestione d'informazioni
Per la porzione automatizzata del sistema informativo, al giorno d'oggi viene usato il termine **sistema informatico**, termine usato oggi per distinguere tutti i sistemi informativi

>Sistema Azienda
>>SIistema Informativo
>>>Sistema Informatico

Nelle attività standadrizzate dei sistemi informativi complessi, sono state introdotte nel tempo forme di organizzazione e codifica delle informazioni
Nei sistemi informatici, le informazioni vengono rappresentate in modo essenziale attraverso i dati

## Informazioni e dati
Nei sistemi informatici, le informazioni vengono rappresentate in modo essenziale, attraverso i **dati**
Dal Vocabolario della lingua italiana:
- **Informazione**: notizia, dato o elemento che consente di avere conoscenza più o meno esatta di fatti, situazioni, etc...
- **Dato**: ciò che è immediatamente presente alla conoscenza, prima di ogni elaborazione;

I dati costituiscono spesso una risorsa strategica, perchè più stabili nel tempo di altre componenti
**Esempio**
- I dati bancari hanno una struttura invariata da decenni. Le applicazioni che operano su essi invece cambiano di frequente. La nuova procedure "eredità" i dati dalla vecchia con opportune trasformazioni
- I dati vista la loro stabilità costituiscono una risorsa per l'organizzazione, un patrimonio da sfruttare e proteggere

All'interno del sistema informativo, la collezione di dati è chiamata **Basi di dati** o **Database**
- Compito della base di dati è non solo di memorizzare ma di rappresentare le relazioni tra essi
All'interno del sistema informativo il software atto specificatamente a gestire i dati è detto Sistema di Gestione della base di dati o **Database Management System**

## Basi di dati

_Def metodologica:_ Insieme organizzato di dati utilizzati per il supporto allo svolgimento delle attività
_Def metodologica e tecnologica:_ insieme di dati gestito dal DBMS

**Data Independence:** La struttura di un DB deve dare garanzia che modifiche dei dati non richiedano modifiche ai programmi applicativi e/o alle tecniche di accesso ai dati stessi

**Basi di dati o Database**
Collezione di informazioni registrate in formato leggibile dell'elaboratore elettronico e relativa ad un preciso dominio di conoscenze, organizzata allo scopo di poter essere consultata dai suoi utilizzatori

### DMBS
Sistema (**prodotto software**) in grado di gestire **collezione di dati** che siano:
- **grandi**: di dimensioni molto maggiori della memoria centrale dei sistemi di calcolo
- **persistenti**: con un periodo di vita indipendente dalle singole esecuzioni dei programmi
- **condivise**: utilizzate da applicazioni e utenti diversi
garantendo **affidabilità** (resistenza a malfunzionamenti hardware e software) e **privatezza**(con una disciplina e un controllo degli accessi). Come ogni prodotto informatico, un DBMS deve essere **efficente**(utilizzando al meglio le risorse di spazio e tempo) ed **efficace**(rendendo produttive le attività dei suoi utilizzatori)