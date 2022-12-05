
# Eccezioni

## Cos'è un'eccezione?

Il termine eccezione è una scorciatoia per la frase "evento eccezionale".

>[!important]- Definizione
>Un'eccezione è un evento, che si verifica durante l'esecuzione di un programma, che interrompe il normale flusso delle istruzioni del programma.

Quando si verifica un errore all'interno di un metodo, il metodo crea un oggetto e lo passa al sistema di runtime. L'oggetto, chiamato oggetto eccezione, contiene informazioni sull'errore, incluso il tipo e lo stato del programma quando si è verificato l'errore. La creazione di un oggetto eccezione e la sua consegna al sistema di runtime è chiamata generazione di un'eccezione.

Dopo che un metodo genera un'eccezione, il sistema di runtime tenta di trovare qualcosa per gestirla. L'insieme di possibili "qualcosa" per gestire l'eccezione è l'elenco ordinato di metodi che sono stati chiamati per arrivare al metodo in cui si è verificato l'errore. L'elenco dei metodi è noto come stack di chiamate (vedere la figura successiva).

![[appunti lmp/mod i/immagini/exceptions-callstack.gif|center|300]]

Il sistema di runtime cerca nello stack di chiamate un metodo che contenga un blocco di codice in grado di gestire l'eccezione. Questo blocco di codice è chiamato gestore di eccezioni. La ricerca inizia con il metodo in cui si è verificato l'errore e procede attraverso lo stack di chiamate nell'ordine inverso rispetto a quello in cui sono stati chiamati i metodi. Quando viene trovato un gestore appropriato, il sistema di runtime passa l'eccezione al gestore. Un gestore di eccezioni è considerato appropriato se il tipo dell'oggetto eccezione generato corrisponde al tipo che può essere gestito dal gestore.

Si dice che il gestore di eccezioni scelto rilevi l'eccezione. Se il sistema di runtime cerca in modo esaustivo tutti i metodi nello stack di chiamate senza trovare un gestore di eccezioni appropriato, come mostrato nella figura successiva, il sistema di runtime (e, di conseguenza, il programma) termina.
![[appunti lmp/mod i/immagini/exceptions-errorOccurs.gif|center|400]]

L'utilizzo delle eccezioni per gestire gli errori presenta alcuni vantaggi rispetto alle tradizionali tecniche di gestione degli errori

## Il Requisito Catch o Specify

Il codice del linguaggio di programmazione Java valido deve soddisfare il requisito Catch o Specify. Ciò significa che il codice che potrebbe generare determinate eccezioni deve essere racchiuso da uno dei seguenti elementi:

- Un'istruzione try che intercetta l'eccezione. Il try deve fornire un gestore per l'eccezione
- Metodo che specifica che può generare l'eccezione. Il metodo deve fornire una clausola throws che elenchi l'eccezione

Il codice che non soddisfa i requisiti Catch o Specify non verrà compilato.

Non tutte le eccezioni sono soggette al requisito di catch o specify. Per comprenderne il motivo, dobbiamo esaminare le tre categorie fondamentali di eccezioni, di cui solo una è soggetta al Requisito.

### I tre tipi di eccezioni

- Il primo tipo di eccezione è l'eccezione verificata (_checked exception_). Queste sono condizioni eccezionali che un'applicazione ben scritta dovrebbe prevedere e recuperare. Ad esempio, supponiamo che un'applicazione richieda a un utente un nome di file di input, quindi apra il file passando il nome al costruttore per java.io.FileReader. Normalmente, l'utente fornisce il nome di un file esistente e leggibile, quindi la costruzione dell'oggetto FileReader riesce e l'esecuzione dell'applicazione procede normalmente. Ma a volte l'utente fornisce il nome di un file inesistente e il costruttore genera java.io.FileNotFoundException. Un programma ben scritto rileverà questa eccezione e avviserà l'utente dell'errore, eventualmente richiedendo un nome file corretto.

Le eccezioni verificate sono soggette al requisito Catch o Specify. Tutte le eccezioni sono eccezioni controllate, tranne quelle indicate da Error, RuntimeException e le loro sottoclassi.

- Il secondo tipo di eccezione è l'errore (_error_). Si tratta di condizioni eccezionali che sono esterne all'applicazione e che l'applicazione di solito non può prevedere o recuperare. Ad esempio, supponiamo che un'applicazione apra correttamente un file per l'input, ma non sia in grado di leggere il file a causa di un malfunzionamento dell'hardware o del sistema. La lettura non riuscita genererà java.io.IOError. Un'applicazione potrebbe scegliere di rilevare questa eccezione, al fine di notificare all'utente il problema, ma potrebbe anche avere senso che il programma stampi una traccia dello stack e esca.

Gli errori non sono soggetti al requisito di Catch o Specify. Gli errori sono quelle eccezioni indicate da Error e dalle sue sottoclassi.

- Il terzo tipo di eccezione è l'eccezione di runtime (_runtime exception_). Si tratta di condizioni eccezionali interne all'applicazione e che l'applicazione in genere non è in grado di prevedere o recuperare. Questi di solito indicano bug di programmazione, come errori logici o uso improprio di un'API. Ad esempio, si consideri l'applicazione descritta in precedenza che passa un nome di file al costruttore per FileReader. Se un errore logico causa il passaggio di un null al costruttore, il costruttore genererà NullPointerException. L'applicazione può intercettare questa eccezione, ma probabilmente ha più senso eliminare il bug che ha provocato l'eccezione.

Le eccezioni di runtime non sono soggette al requisito di Catch o Specify. Le eccezioni di runtime sono quelle indicate da RuntimeException e dalle sue sottoclassi.

Gli errori e le eccezioni di runtime sono noti collettivamente come eccezioni non controllate.

### Bypassare Catch o Specify

Alcuni programmatori considerano il requisito Catch o Specify un grave difetto nel meccanismo delle eccezioni e lo aggirano utilizzando eccezioni non controllate al posto di eccezioni controllate. In generale, questo non è raccomandato.

## Cattura e gestione delle eccezioni

Questa sezione descrive come utilizzare i tre componenti del gestore delle eccezioni — try, catch e infine i blocchi — per scrivere un gestore delle eccezioni. Quindi, viene spiegata l'istruzione try-with-resources, introdotta in Java SE 7. L'istruzione try-with-resources è particolarmente adatta a situazioni che utilizzano risorse Closeable, come i flussi.

L'ultima parte di questa sezione illustra un esempio e analizza ciò che accade durante vari scenari.

L'esempio seguente definisce e implementa una classe denominata ListOfNumbers. Una volta costruito, ListOfNumbers crea un ArrayList che contiene 10 elementi Integer con valori sequenziali da 0 a 9. La classe ListOfNumbers definisce anche un metodo denominato writeList, che scrive l'elenco di numeri in un file di testo denominato OutFile.txt. Questo esempio utilizza le classi di output definite in java.io

```java
// Note: This class will not compile yet.
import java.io.*;
import java.util.List;
import java.util.ArrayList;

public class ListOfNumbers {

    private List<Integer> list;
    private static final int SIZE = 10;

    public ListOfNumbers () {
        list = new ArrayList<Integer>(SIZE);
        for (int i = 0; i < SIZE; i++) {
            list.add(new Integer(i));
        }
    }

    public void writeList() {
	// The FileWriter constructor throws IOException, which must be caught.
        PrintWriter out = new PrintWriter(**new FileWriter("OutFile.txt")**);

        for (int i = 0; i < SIZE; i++) {
            // The get(int) method throws IndexOutOfBoundsException, which must be caught.
            out.println("Value at: " + i + " = " + **list.get(i)**);
        }
        out.close();
    }
}
```

La prima riga in grassetto è una chiamata a un costruttore. Il costruttore inizializza un flusso di output su un file. Se il file non può essere aperto, il costruttore lancia un'eccezione IOException. La seconda riga in grassetto è una chiamata al metodo get della classe ArrayList, che genera un'eccezione IndexOutOfBoundsException se il valore del suo argomento è troppo piccolo (minore di 0) o troppo grande (più del numero di elementi attualmente contenuti da ArrayList).

Se si tenta di compilare la classe ListOfNumbers, il compilatore stampa un messaggio di errore relativo all'eccezione generata dal costruttore FileWriter. Tuttavia, non visualizza un messaggio di errore relativo all'eccezione generata da get. Il motivo è che l'eccezione generata dal costruttore, IOException, è un'eccezione controllata e quella generata dal metodo get, IndexOutOfBoundsException, è un'eccezione non controllata.

### Il blocco Try

Il primo passaggio nella costruzione di un gestore di eccezioni consiste nel racchiudere il codice che potrebbe generare un'eccezione all'interno di un blocco try. In generale, un blocco try è simile al seguente:

```java
try {
    _code_
}
catch and finally blocks . . .
```

Il segmento nel codice etichettato di esempio contiene una o più righe di codice valide che potrebbero generare un'eccezione. (Il fermo e infine i blocchi sono spiegati nelle prossime due sottosezioni.)

Per costruire un gestore di eccezioni per il metodo writeList dalla classe ListOfNumbers, racchiudere le istruzioni che generano eccezioni del metodo writeList all'interno di un blocco try. C'è più di un modo per farlo. È possibile inserire ogni riga di codice che potrebbe generare un'eccezione all'interno del proprio blocco try e fornire gestori di eccezioni separati per ciascuno. In alternativa, puoi inserire tutto il codice writeList all'interno di un singolo blocco try e associarvi più gestori. Il listato seguente utilizza un blocco try per l'intero metodo perché il codice in questione è molto breve.

```java
private List<Integer> list;
private static final int SIZE = 10;

public void writeList() {
    PrintWriter out = null;
    try {
        System.out.println("Entered try statement");
        FileWriter f = new FileWriter("OutFile.txt");
        out = new PrintWriter(f);
        for (int i = 0; i < SIZE; i++) {
            out.println("Value at: " + i + " = " + list.get(i));
        }
    }
    catch and finally blocks  . . .
}
```

Se si verifica un'eccezione all'interno del blocco try, tale eccezione viene gestita da un gestore di eccezioni ad esso associato. Per associare un gestore di eccezioni a un blocco try, devi inserire un blocco catch dopo di esso;

### Il blocco Catch

Puoi associare i gestori di eccezioni a un blocco try fornendo uno o più blocchi catch direttamente dopo il blocco try. Nessun codice può trovarsi tra la fine del blocco try e l'inizio del primo blocco catch.

```java
try {

} catch (_ExceptionType name_) {

} catch (_ExceptionType name_) {

}
```

Ogni blocco catch è un gestore di eccezioni che gestisce il tipo di eccezione indicato dal suo argomento. Il tipo di argomento, ExceptionType, dichiara il tipo di eccezione che il gestore può gestire e deve essere il nome di una classe che eredita dalla classe Throwable. Il gestore può fare riferimento all'eccezione con il nome.

Il blocco catch contiene il codice che viene eseguito se e quando viene richiamato il gestore delle eccezioni. Il sistema di runtime richiama il gestore di eccezioni quando il gestore è il primo nello stack di chiamate il cui ExceptionType corrisponde al tipo di eccezione generata. Il sistema lo considera una corrispondenza se l'oggetto lanciato può essere legalmente assegnato all'argomento del gestore di eccezioni.

Di seguito sono riportati due gestori di eccezioni per il metodo writeList:

```java
try {

} catch (IndexOutOfBoundsException e) {
    System.err.println("IndexOutOfBoundsException: " + e.getMessage());
} catch (IOException e) {
    System.err.println("Caught IOException: " + e.getMessage());
}
```

