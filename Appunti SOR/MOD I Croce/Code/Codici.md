In questo file verrano scritti tutti i codici fatti durante le lezioni

---
# Primo programma con fork e pipe

Questo programma deve creare due processi P1 e P2, che eseguono le seguenti operazioni:

- P1 genera un numero random compreso tra 0 e 100, e ad ogni iterazione del ciclo invia al padre il numero, se e solo se il numero è dispari
- P2 esegue le stesse cose però con i numeri pari
- Il padre legge i numeri che gli vengono inviati dai figli ed esegue la somma, se la somma supera il valore 190, allora il padre invia un segnale di terminazione ai figli e termina l'esecuzione del programma


```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>

#define STDIN 0
#define STDOUT 1

int main(int argc,char** argv){

pid_t p1,p2;
//int fd[2];
int fd1[2],fd2[2]; //file descriptor per letture/scrittura di p1/p2
  
if (pipe(fd1) == -1 || pipe(fd2) == -1){
	perror("Errore nella creazione delle pipe");
	exit(1);
}
  
p1 = fork();
if(p1 == 0){
	//sto nel figlio p1
	close(fd1[0]); //chiudo stream di lettura, va bene anche con close(fd1[STDOUT])
	srand(getpid());
	while(1){
		int num = rand() % 101;
		if (num%2 != 0){
			//printf("Sono il figlio 1 e ho generato il numero: %d\n",num);
			write(fd1[1],&num,sizeof(int));
		}
	}
	close(fd1[1]);//chiudo pipe per scrittura,close(fd1[STDIN])
} else {
	p2 = fork();
	if (p2 == 0) { // Codice eseguito dal secondo figlio (p2)
		close(fd2[0]); // Chiudi il lato di lettura, stessa cosa di p1
		srand(getpid());
		while (1) {
			int num = rand() % 101;
			if (num % 2 == 0) {
			//printf("Sono il figlio 2 e ho generato il numero: %d\n",num);
				write(fd2[1], &num, sizeof(int)); // Invia il numero pari al padre
			}
		}
		close(fd2[1]);//anche qui
	}else{
		close(fd1[1]);//chiudi stream scrittura (STDIN) del primo figlio
		close(fd2[1]);//chiudi stream scrittura (STDIN) del secondo figlio
		int sum = 0;
		while(1){
			int num1,num2;
			read(fd1[0],&num1,sizeof(int));// Leggi il numero dispari dal primo figlio
			read(fd2[0], &num2, sizeof(int)); // Leggi il numero pari dal secondo figlio
			sum = num1 + num2;
			printf("Somma: %d + %d = %d\n", num1, num2, sum);
			if (sum > 190) {
				// Invia un segnale di terminazione ai figli
				kill(p1, SIGTERM);
				kill(p2, SIGTERM);
				printf("Sono il padre, e ho terminato i processi (figli) con PID : %d (p1),%d (p2)\n",p1,p2 );
				break;
			}
		}
		close(fd1[0]);
		close(fd2[0]);
		// Aspetta che i figli terminino
		wait(NULL);
		wait(NULL);
	}
}
return 0;
}
```

---

# Secondo programma: Copy file with seek (puntatore)

Questo programma deve prendere in input 3 argomenti:
- file di partenza, ovvero il file che verrà copiato
- file di destinazione, ovvero la copia del file in input
- indice del puntatore, ovvero l'indice del puntatore che indica l'inizio della copia (es indice = 10 significa che la copia da A a B avverrà a partire dalla posizione 10 in A, e quindi in B ci sarà la copia di A senza i primi 10 caratteri)

Il programma, presi in input questi 3 argomenti, restituirà in output un file, che sarà la copia del file di input (totale -> indice $= 0$ o parziale -> indice $\neq0$ )

```c
/* Programma di copia di file con controllo errori minimale e reportistica. */

#include <fcntl.h> //Contiene le costanti che vengono utilizzate nelle chiamate di sistema relative al controllo dei file descriptors. In questo programma, O_RDONLY viene utilizzato per aprire il file di input in modalità sola lettura.
#include <stdio.h>
#include <stdlib.h>
#include <sys/stat.h>
#include <unistd.h>

#define BUF_SIZE 8       // Dimensione del buffer: 8 byte
#define OUTPUT_MODE 0700 // Bit di protezione per file di output

#define TRUE 1

long fileSize(const char *filename) {
  struct stat st;
  if (stat(filename, &st) == 0) {
    return st.st_size;
  } else {
    perror("[ERROR]: Error getting file size");
    return -1; // Indicates an error
  }
}

int main(int argc, char *argv[]) {
  int in_fd, out_fd;      // File descriptor per i file di input e output
  int rd_count, wt_count; // Contatori per la lettura e scrittura
  long size;
  char buffer[BUF_SIZE]; // Buffer per la lettura e scrittura dei dati

  char *source_code_file = argv[0];

  // Controllo del numero di argomenti
  if (argc != 4) {
    // Stampa un messaggio di errore se il numero di argomenti non è
    // corretto
    fprintf(stderr,
            "[ERROR]: Errore di sintassi. Uso: %s input_file_path "
            "output_file_path indice_inziale \n",
            source_code_file);
    exit(1); // scrivo su STD_ERROR
  }

  char *input_filename = argv[1];
  char *output_filename = argv[2];
  long index = (long)atoi(// converte una stringa in intero poi esegue il cast in long
      argv[3]); 

  // Apertura del file di input
  in_fd = open(input_filename, O_RDONLY); // Apre il file di origine
  if (in_fd < 0)
    exit(2); // Se non può aprirlo, esce

  size = fileSize(input_filename);
  printf("[INFO]: size = %ld\n", size);

  if (index > size) {
    fprintf(stderr,
            "[ERROR]: L'indice (%ld) iniziale supera la lunghezza del file\n",
            index);
    exit(4);
  }
  printf("[INFO]: index = %ld\n", index);

  out_fd = creat(output_filename, OUTPUT_MODE); // Crea il file di destinazione
  if (out_fd < 0)
    exit(3); // Se non può crearlo, esce

  if (lseek(in_fd, index, SEEK_CUR) == -1)
    exit(4); // se non riesce a creare il cursore

  while (TRUE) {
    rd_count = read(in_fd, buffer, BUF_SIZE); // Legge un blocco di dati
    if (rd_count <= 0)
      break; // Se fine del file o errore, esce dal ciclo

    wt_count = write(out_fd, buffer, rd_count); // Scrive i dati
    if (wt_count <= 0)
      exit(5); // wt_count <= 0 è un errore
  }

  // Chiusura dei file
  close(in_fd);
  close(out_fd);

  if (rd_count == 0)
    exit(0); // Nessun errore sull’ultima lettura
  else
    exit(6); // Errore sull’ultima lettura
}
```

Attualmente il codice non fa alcuna verifica sui permessi del file.

La modifica che sarà da applicare è quella di verificare i permessi del file in input PRIMA dell'operazione open, in modo tale da avere la condizione:
- se permessi_input_file = r (lettura) allora prosegui
- altrimenti esci e dai errore

Ecco il codice che controlla i permessi del file

```c
int check_permission(const char *filename) {
	struct stat file;

	if (stat(filename, &file) < 0) return -1;

	int check = file.st_mode & S_IRUSR;

	return check;
}
```

---

# Terzo programma (Simulazione Esame)


Il processo eseguito, inizialmente crea un buffer come array di 11 numeri interi, inizializzati a zero. In seguito genera tre thread utilizzando le librerie POSIX secondo le seguenti specifiche:
- Il primo thread sceglie casualmente una cella del buffer e vi scrive il numero +1, qualsiasi sia il valore presente nella cella.
- Il secondo thread sceglie casualmente una cella del buffer e vi scrive il numero -1, qualsiasi sia il valore presente nella cella.
- Il terzo thread controlla se tutte le celle del buffer sono state inizializzate. In caso positivo, determina se il numero di celle contententi un valore pari a +1 è maggiore di quelle con -1 e termina tutti e tre i thread.

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
