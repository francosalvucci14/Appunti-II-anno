
# Basic I/O

## I/O Streams

Un flusso di I/O rappresenta una sorgente di input o una destinazione di output. Un flusso può rappresentare molti tipi diversi di origini e destinazioni, inclusi file su disco, dispositivi, altri programmi e array di memoria.

Gli stream supportano molti tipi diversi di dati, inclusi byte semplici, tipi di dati primitivi, caratteri localizzati e oggetti. Alcuni flussi semplicemente trasmettono dati; altri manipolano e trasformano i dati in modi utili.

Indipendentemente da come funzionino internamente, tutti i flussi presentano lo stesso semplice modello ai programmi che li utilizzano: un flusso è una sequenza di dati. Un programma utilizza un flusso di input per leggere i dati da una fonte, un elemento alla volta:

![[appunti lmp/mod i/immagini/io-ins.gif|center]]

Un programma utilizza un flusso di output per scrivere i dati in una destinazione, un elemento alla volta:

![[appunti lmp/mod i/immagini/Pasted image 20221221111833.png|center|500]]


In questa lezione vedremo flussi in grado di gestire tutti i tipi di dati, dai valori primitivi agli oggetti avanzati.

L'origine dati e la destinazione dei dati raffigurate sopra possono essere qualsiasi cosa contenga, generi o consumi dati. Ovviamente questo include i file su disco, ma una sorgente o una destinazione può anche essere un altro programma, un dispositivo periferico, un socket di rete o un array.

Nella sezione successiva, utilizzeremo il tipo più elementare di flussi, flussi di byte, per dimostrare le operazioni comuni di Stream I/O.

### Byte Streams

I programmi utilizzano flussi di byte per eseguire l'input e l'output di byte a 8 bit. Tutte le classi del flusso di byte discendono da InputStream e OutputStream.

Esistono molte classi di flusso di byte. Per dimostrare come funzionano i flussi di byte, ci concentreremo sui flussi di byte di file I/O, FileInputStream e FileOutputStream. Altri tipi di flussi di byte vengono utilizzati più o meno allo stesso modo; differiscono principalmente nel modo in cui sono costruiti.

#### Utilizzo di flussi di byte

Esploreremo FileInputStream e FileOutputStream esaminando un programma di esempio denominato CopyBytes, che utilizza flussi di byte per copiare xanadu.txt, un byte alla volta.

```java
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;

public class CopyBytes {
    public static void main(String[] args) throws IOException {

        FileInputStream in = null;
        FileOutputStream out = null;

        try {
            in = new FileInputStream("xanadu.txt");
            out = new FileOutputStream("outagain.txt");
            int c;

            while ((c = in.read()) != -1) {
                out.write(c);
            }
        } finally {
            if (in != null) {
                in.close();
            }
            if (out != null) {
                out.close();
            }
        }
    }
}
```

CopyBytes passa la maggior parte del suo tempo in un ciclo semplice che legge il flusso di input e scrive il flusso di output, un byte alla volta, come mostrato nella figura seguente.

![[appunti lmp/mod i/immagini/byteStream.gif|center]]

