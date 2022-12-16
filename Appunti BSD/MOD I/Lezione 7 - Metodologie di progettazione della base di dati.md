# Progettazione di una base di dati

Progettare una base di dati significa definirne struttura, caratteristiche e contenuto. E quindi prevede l'uso di opportune metodologie. In base al grado di astrazione, la progettazione prevede:

- **Modello concettuale**: rappresenta la realtà dei dati e le relazioni tra essi attraverso uno schema
- **Modello logico**: descrive il modo attraverso il quale i dati sono oragnizzati negli archivi del calcolatore
- **Modello fisico**: descrive come i dati sono registrati nelle memorie di massa

## Modello logico

Obiettivo della fase di progettazione logica è pervenire, **a partire dallo schema concettuale**, a uno schema logico che lo rappresenti in modo fedele, "efficiente" e indipendente dal particolare DBMS adottato. A tal fine questa fase di progettazione può essere suddivisa in 2 passi:
1. **Ristrutturazione dello schema Entità-Relazione**: è una fase indipendente dal modello logico e si basa su criteri di ottimizzazione dello schema
2. **Traduzione verso il modello logico**: fa riferimento ad uno specifico modello logico (**modello relazionale**)

## Ciclo di vita di un sistema informativo

1. **Studio di fattibilità**: definisce le varie alternative possibili,i relativi costi e le priorità di realizzazione
2. **Raccolta e analisi dei requisiti**: individua proprietà e funzionalità del sistema tramite interazione con gli utenti e definizione informale dei dati e delle operazioni
3. **Progettazione**: divisa in progettazione dei dati e progettazione delle applicazioni. Individua struttura e organizzazione dei dati e caratteristiche degli applicativi che vi dovranno accedere
4. **Implementazione**: realizza la base di dati e il codice dei programmi conformemente alle specifiche
5. **Validazione e collaudo**: verifica il corretto funzionamento del sistemas informativo
6. **Funzionamento**: il sistema informativo diviene operativo

