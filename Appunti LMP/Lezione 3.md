# Domande che possono capitare all'esame
## Quanti tipi di variabili si possono usare?
- Globali
- Locali
- Parametri
- Campi
## A cosa serve l'interfaccia in Java?
Forniscono un vocabolario unificante per interagire con oggetti aventi implementazioni differenti (cioè basati su classi diverse)

## Quanti tipi si conoscono in Java?
- Primitivi:
	- int
	- string
	- float
	- double
	- boolean
- Oggetti:
	- classi
	- interfacce

# Concetti della programmazione Object-Oriented
- **Cos'è un oggetto?** : Un oggetto è un pacchetto software di stati e comportamenti correlati.Gli oggetti software sono spesso utilizzati per modellare gli oggetti della vita reale che puoi trovare ogni giorno
- **Cos'è una classe?**: Una classe è lo schema o prototipo da cui sono creati gli oggetti
- **Cos'è l'ereditarietà?**: L'ereditarietà fornisce un meccanismo potente e naturale per organizzare e strutturare software
- **Cos'è un interfaccia?**: L'interfaccia è un "contratto" tra una classe e il mondo esterno. Quando una classe implementa un'interfaccia, promette di fornire il comportamento pubblicato da quell'interfaccia.
- **Cos'è un pacchetto?**: Un pacchetto è uno spazio dei nomi che serve ad organizzare classi e interfaccie in maniera logica. Inserire il codice nei pacchetti semplifica la gestione di progetti software di grandi dimensioni

## Oggetto
Gli oggetti sono la chiave per capire la tecnologia object-oriented. Ci sono vari esempi di oggetti nella vita reale: un cane, la scrivania, etc...
Gli oggetti condividono due caratteristiche:
- stati(state)
- comportamenti(behavior)
Identificare lo stato e il comportamento di un oggetto nella vita reale è una grande idea per iniziare a pensare in termini di OOP

![[appunti lmp/immagini/Pasted image 20221016174127.png|center]]

Gli oggetti software sono concettualmente simili agli oggetti nella vita reale: anche loro sono cpomposti da stati e comportamenti. Un oggetto software salva i suoi stati nei _fields_(campi)(variabili in qualche linguaggio di programmazione) ed espone i suoi comportamenti tramite i _methods_(metodi)(funzioni in qualche linguaggio di programmazione). I metodi operano sullo stato interno di un oggetto e servono come il meccanismo primario per la comunicazione object-to-object.
Nascondere lo stato interno e richiedere che tutte le interazioni vengano eseguite attraverso i metodi di un oggetto è noto come incapsulamento dei dati(**data encapsulation**), un principio fondamentale della programmazione orientata agli oggetti

Raggruppare il codice in oggetti software individuali fornisce un numero di benefits, inclusi:
- **Modularità**: il codice sorgente per un oggeto può essere scritto e mantenuto indipendentemente dal codice sorgente di altri oggetti
- **Informatio-hiding**: interaggendo solo con i metodi dell'oggetto, i dettagli delle implementazioni interne rimane nascosto al mondo esterno
- **Riutilizzo del codice**: se un oggetto già esiste, puoi usare quell'oggetto nel tuo programma
- **Collegabilità e debugging facili**: Se un particolare oggetto risulta essere problematico, puoi semplicemente rimuoverlo dall'applicazione e collegare un oggetto diverso come sostituto.