# Struttura dell'esame

Ci sono 3 tipologie di esercizi nell'esame di S.O.

1) 12 domande a risposta multipla
2) Un'esercizio di coding (**programmazione concorrente**)
	1) L'esercizio volgerà su una delle due categorie di codici su programmazione concorrente: Processi o Thread
		1) Per i processi, si tratterà di creare 3 o più processi, che facciano delle cose, e che poi comunichino il tutto al processo padre, tramite le PIPE. Alla fine, il processo padre analizza i dati e termina i processi figli
		2) Per i thread, è più o meno la stessa cosa, solo che invece che comunicare tramite le PIPE, bisogna gestire tutto il discorso della mutua esclusione, regione critica,etc.. tramite l'uso di mutex e/o semafori
3) 1 o 2 domanda/e a risposta aperta, tipo:
	1) **Domanda1:** Il candidato discuta l'importanza dello scheduling nei sistemi batch, con particolare attenzione ai parametri che si cercano di ottimizzare in questi sistemi. Si chiede di presentare e descrivere almeno tre metodi di scheduling differenti applicati nei sistemi batch, specificando
		1) quali aspetti di performance ciascuno di essi mira a migliorare
		2) gli eventuali limiti
	2) **Domanda2**: Il candidato spieghi il concetto di memoria virtuale e il suo ruolo nella gestione della memoria RAM da parte di un sistema operativo moderno. Si discuta come la memoria virtuale permetta di gestire programmi che superano la capacità della memoria fisica disponibile. Si descrivano inoltre le tecniche di paging e segmentazione, evidenziando come queste tecniche abbiano migliorato l'efficienza e la gestione della memoria nei computer.

# Soluzione della simulazione d'esame

## Esercizio 1

Di seguito la tabella contenente la domanda con la risposta esatta

| Domanda                                                                              | Risposte                                                                                                                                                                                                                                                                                                                                                  | Risposta Esatta                                                                    |
| ------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| Qual'è la principale sfida nella selezione della dimensione delle pagine             | Bilanciare frammentazione interna e overhead delle pagine,Scegliere tra paginazione e segmentazione,Bilanciare/Gestire il rapporto tra allocazione equa e proporzionale, Massimizzare frammentazione interna e overhead delle pagine                                                                                                                      | Bilanciare frammentazione interna e overhead delle pagine                          |
| Cosa accade quando si invia un segnale al processo                                   | Il processo viene terminato, sospeso temporaneamente, duplicato, riavviato                                                                                                                                                                                                                                                                                | Il processo può essere interroto o sospeso                                         |
| Qual è il ruolo delle chiamate di sistema in un S.O                                  | Connettersi a internet, interfacciare hardware e software,Gestire l'interfaccia utente,eseguire le applicazioni di terze parti                                                                                                                                                                                                                            | Fornire un'interfaccia tra le applicazioni e il kernel del S.O                     |
| Qual è il comando UNIX per contare il numero di righe, parole e caratteri in un file | count,countfile,filecount,num                                                                                                                                                                                                                                                                                                                             | `wc`                                                                               |
| Cos'è una regione critica                                                            |                                                                                                                                                                                                                                                                                                                                                           | Una parte di programma che non deve essere eseguita concorrentemente da più thread |
| Qual'è uno degli algoritmi di sostituzione delle pagine                              | Priority scheduling, nessuna delle alternative, Multilevel queue, shortest job first, FIFO                                                                                                                                                                                                                                                                | FIFO                                                                               |
| Quale problema principale affrontano le architetture Batch                           | Mancanza di interfaccia utente, CPU inattesa di I/O, Elevato consumo energetico,Basso throughput in proporzione al numero di periferiche disponibili, Complessità di programmazione                                                                                                                                                                       | CPU inattesa di I/O                                                                |
| Qual'è l'effetto principale delle CPU più veloci sui processi                        | I processi tendono ad essere più I/O bound, I processi diventano meno dipendenti dalla velocità del disco,i processi tendono ad essere più CPU bound, Miglioramento del throughput generale del sistema, Riduzione del bisogno di scheduling                                                                                                              | I processi tendono ad essere più I/O bound                                         |
| Qual è la funzione principale di un I-node nei file systems UNIX-like                | Contenere le informazioni su un file compresi il nome e il contenuto, Contenere le informazioni su un file esclusi il nome e il contenuto, nessuna delle alternative è corretta, Contenere le informazioni su un file esclusi il nome e i diritti di accesso al file,Contenere le informazioni su un file compresi il nome e i diritti di accesso al file | Contenere le informazioni su un file esclusi il nome e il contenuto                |
| Cosa consente l'astrazione del file nel file system                                  | Riduzione del tempo di acccesso ai dati, MInimizzazione dello spazio di memorizzazione, Incremento della velocità di scrittura dei dati, nessuna delle risposte                                                                                                                                                                                           | nessuna delle risposte                                                             |
| Quale delle seguenti è una funzione per stampare "Hello World" sulla console C       | `write(char *str)`,`print(char *str)`,`printf(char *str)`,`echo(char *str)`,`display(char *str)`                                                                                                                                                                                                                                                          | `printf(char *str)`                                                                |
| Quale tecnica viene usata per separare e proteggere i programmi in esecuzione        | L'astrazione della memoria con spazi di indirizzi unici, La divisione della memoria fisica in segmenti diversi, La memorizzazione dei dati in registri base e limite, L'uso di sistemi di swapping avanzati, L'implementazione di algoritmi di gestione della memoria                                                                                                                                                                                                                                                                                                                                                          | L'astrazione della memoria con spazi di indirizzi unici                                                                                   |

## Esercizio 2

Scrivere un programma C che segue le seguenti specifiche.
Il processo eseguito, inizialmente crea un buffer come array di 11 numeri interi, inizializzati a zero. In seguito genera tre thread utilizzando le librerie POSIX secondo le seguenti specifiche:
- Il primo thread in un ciclo infinito sceglie casualmente una cella del buffer e vi scrive il numero +1, qualsiasi sia il valore presente nella cella.
- Il secondo thread in un ciclo infinito sceglie casualmente una cella del buffer e vi scrive il numero -1, qualsiasi sia il valore presente nella cella.
- Il terzo thread in un ciclo infinito controlla se tutte le celle del buffer sono state inizializzate ad un valore diverso da 0. In caso positivo, determina se il numero di celle contenenti un valore pari a +1 è maggiore di quelle con -1 e termina tutti e tre i thread.

Mentre un thread ha accesso al buffer, nessun altro thread deve accedervi.
Una volta che un thread ha acceduto in lettura o scrittura al buffer, deve attendere un numero di secondi random tra 0 e 3

```C
#include <pthread.h>
#include <signal.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>

#define N 11

pthread_mutex_t the_mutex;
pthread_cond_t cond_control;

int buffer[N] = {0};
pthread_t p1, p2, p3;

void print_buffer() {
  printf("[");
  for (int i = 0; i < N - 1; i++) {
    printf("%3d,", buffer[i]);
  }
  printf("%3d ]\n", buffer[N - 1]);
}

void *set_one(void *args) {
  while (1) {
    pthread_mutex_lock(&the_mutex);
    int index = rand() % N;
    buffer[index] = 1;
    printf("[INFO]: sono thread 1, ho generato l'indice: %d\n", index);
    print_buffer();
    pthread_cond_signal(&cond_control);
    pthread_mutex_unlock(&the_mutex);
    sleep(rand() % 4);
  }
}

void *set_neg_one(void *args) {
  while (1) {
    pthread_mutex_lock(&the_mutex);
    int index = rand() % N;
    buffer[index] = -1;
    printf("[INFO]: Sono thread 2, ho generato l'indice: %d\n", index);
    print_buffer();
    pthread_cond_signal(&cond_control);
    pthread_mutex_unlock(&the_mutex);
    sleep(rand() % 4);
  }
}

int check_init() {
  for (int i = 0; i < N; ++i) {
    if (buffer[i] == 0) {
      return 0;
    }
  }
  return 1;
}

void *control(void *args) {
  while (1) {
    pthread_mutex_lock(&the_mutex);

    // controllo se tutti i elementi dell'array sono inizializzatise
    // se lo sono allora il thread va avanti, altrimenti lascia il mutex e rifà
    // il controllo.
    while (check_init() == 0) {
      sleep(rand() % 4);
      pthread_cond_wait(&cond_control, &the_mutex);
    }
    int n_ones = 0, n_neg_ones = 0;
    for (int i = 0; i < N; i++) {
      if (buffer[i] == 1)
        n_ones++;
      if (buffer[i] == -1)
        n_neg_ones++;
    }

    if (n_ones > n_neg_ones) {
      printf("[INFO]: Ha vinto il thread 1, impostando %d -> '1'\n", n_ones);
    } else {
      printf("[INFO]: Ha vinto il thread 2, impostando %d -> '-1'\n",
             n_neg_ones);
    }
    printf("[INFO]: sono il 3 thread\n");
    pthread_kill(p1, SIGINT);
    pthread_kill(p2, SIGINT);
    pthread_mutex_unlock(&the_mutex);

    pthread_exit(0); // Termina il thread
  }
}
int main() {
  srand(time(NULL));

  pthread_mutex_init(&the_mutex, NULL);
  pthread_cond_init(&cond_control, NULL);

  pthread_create(&p1, NULL, set_one, NULL);
  pthread_create(&p2, NULL, set_neg_one, NULL);
  pthread_create(&p3, NULL, control, NULL);
  
  pthread_join(p1, NULL);
  pthread_join(p2, NULL);
  pthread_join(p3, NULL);

  pthread_cond_destroy(&cond_control);
  pthread_mutex_destroy(&the_mutex);
  return 0;
}
```

## Esercizio 3

### Domanda 1

### Domanda 2