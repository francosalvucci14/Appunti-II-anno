
# Espressioni,Blocchi e Statements
## Espressioni
_Def_
Un'espressione è un costrutto formato da variabili,operatori, invocazioni di metodi, che vengono costruiti accordandosi alla sintassi del linguaggio
**Esempio**
```java
int cadence = 0;
anArray[0] = 100;
System.out.println("Element 1 at index 0: "+anArray[0]);
in result = 1+2;
if(value1==value2)
	System.out.println("value1==value2");
```
Il tipo di dati del valore restituito da un'espressione dipende dagli elementi utilizzati nell'espressione. L'espressione cadence = 0 restituisce un int perché l'operatore di assegnazione restituisce un valore dello stesso tipo di dati dell'operando di sinistra; in questo caso, la cadenza è un int
Il linguaggio di programmazione Java consente di costruire espressioni composte da varie espressioni più piccole purché il tipo di dati richiesto da una parte dell'espressione corrisponda al tipo di dati dell'altra. Ecco un esempio di espressione composta:
```java
1*2*3
```

In questo esempio particolare, l'ordine in cui viene valutata l'espressione non è importante perché il risultato della moltiplicazione è indipendente dall'ordine; il risultato è sempre lo stesso, indipendentemente dall'ordine in cui si applicano le moltiplicazioni. Tuttavia, questo non è vero per tutte le espressioni. Ad esempio, l'espressione seguente fornisce risultati diversi, a seconda che si esegua prima l'operazione di addizione o divisione:

```java
x + y / 100 // ambiguo
```
È possibile specificare esattamente come verrà valutata un'espressione utilizzando le parentesi bilanciate: ( e ). Ad esempio, per rendere univoca l'espressione precedente, puoi scrivere quanto segue:
```java
(x + y) / 100 // non ambiguo, consigliato
```

Se non si indica esplicitamente l'ordine per le operazioni da eseguire, l'ordine è determinato dalla precedenza assegnata agli operatori in uso all'interno dell'espressione. Gli operatori che hanno una precedenza più alta vengono valutati per primi. Ad esempio, l'operatore di divisione ha una precedenza maggiore rispetto all'operatore di addizione. Pertanto, le due affermazioni seguenti sono equivalenti:
```java
x + y / 100
x + (y / 100) // non ambiguo, consigliato
```

Quando si scrivono espressioni composte, sii esplicito e indica tra parentesi quali operatori devono essere valutati per primi. Questa pratica semplifica la lettura e la manutenzione del codice.
## Statements

GLi statements sono più o meno equivalenti alle frasi nelle lingue naturali. Un'istruzione costituisce un'unità di esecuzione completa. I seguenti tipi di espressioni possono essere trasformati in un'istruzione terminando l'espressione con un punto e virgola (;).
- Espressioni di assegnazione
- Qualsiasi uso di ++ o --
- Invocazioni di metodo
- Espressioni di creazione di oggetti

Tali affermazioni sono dette espressioni di espressione
Di seguito sono riportati alcuni esempi di affermazioni di espressione.
```java
// frase di assegnazione
aValore = 8933.234;
// istruzione di incremento
aValore++;
// Istruzione di invocazione del metodo
System.out.println("Ciao mondo!");
// istruzione di creazione dell'oggetto
Bicicletta myBike = nuova Bicicletta();
```

## Blocchi
Un blocco è un gruppo di zero o più istruzioni tra parentesi graffe e può essere utilizzato ovunque sia consentita una singola istruzione. L'esempio seguente, BlockDemo, illustra l'uso dei blocchi:
```java
class BlockDemo {
     public static void main(String[] args) {
          boolean condition = true;
          if (condition) { **// begin block 1**
               System.out.println("Condition is true.");
          } **// end block one**
          else { **// begin block 2**
               System.out.println("Condition is false.");
          } **// end block 2**
     }
}
```

# Control Flow Statements