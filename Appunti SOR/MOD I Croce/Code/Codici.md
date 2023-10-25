In questo file verrano scritti tutti i codici fatti durante le lezioni

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
#define PIPE_RD 0
#define PIPE_WR 1

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
	close(fd1[0]); //chiudo stream di lettura
	srand(getpid());
	while(1){
		int num = rand() % 101;
		if (num%2 != 0){
			//printf("Sono il figlio 1 e ho generato il numero: %d\n",num);
			write(fd1[1],&num,sizeof(int));
		}
	}
	close(fd1[1]);//chiudo pipe per scrittura
} else {
	p2 = fork();
	if (p2 == 0) { // Codice eseguito dal secondo figlio (p2)
		close(fd2[0]); // Chiudi il lato di lettura
		srand(getpid());
		while (1) {
			int num = rand() % 101;
			if (num % 2 == 0) {
			//printf("Sono il figlio 2 e ho generato il numero: %d\n",num);
				write(fd2[1], &num, sizeof(int)); // Invia il numero pari al padre
			}
		}
		close(fd2[1]);
	}else{
		close(fd1[1]);//chiudi stream scrittura del primo figlio
		close(fd2[1]);//chiudi stream scrittura del secondo figlio
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
				printf("Sono il padre, e ho ucciso i processi (figli) con PID : %d (p1),%d (p2)\n",p1,p2 );
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

