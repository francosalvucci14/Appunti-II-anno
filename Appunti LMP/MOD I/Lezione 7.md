
# Ritornando alla [[Lezione 6]]

## Classi nidificate
Il linguaggio di programmazione Java consente di definire una classe all'interno di un'altra classe. Tale classe è chiamata classe nidificata ed è illustrata qui:
```java
class OuterClass {
    ...
    class NestedClass {
        ...
    }
}
```
Una classe nidificata è un membro della sua classe che la racchiude. Le classi nidificate non statiche (classi interne) hanno accesso ad altri membri della classe che lo racchiude, anche se sono dichiarate private. Le classi nidificate statiche non hanno accesso ad altri membri della classe di inclusione. Come membro di OuterClass, una classe nidificata può essere dichiarata privata, pubblica, protetta o privata del pacchetto. (Ricorda che le classi esterne possono essere dichiarate solo pubbliche o private del pacchetto.)

### Perchè usare le classi nidificate?
I motivi convincenti per l'utilizzo di classi nidificate includono quanto segue:
- **È un modo per raggruppare logicamente le classi che vengono utilizzate solo in un posto**: se una classe è utile solo a un'altra classe, è logico incorporarla in quella classe e tenerle insieme. L'annidamento di tali "classi di supporto" rende il loro pacchetto più snello.
- **Aumenta l'incapsulamento**: considera due classi di primo livello, A e B, in cui B ha bisogno dell'accesso ai membri di A che altrimenti sarebbero dichiarati privati. Nascondendo la classe B all'interno della classe A, i membri di A possono essere dichiarati privati e B può accedervi. Inoltre, B stesso può essere nascosto dal mondo esterno.
- **Può portare a un codice più leggibile e gestibile**: l'annidamento di classi piccole all'interno di classi di livello superiore posiziona il codice più vicino a dove viene utilizzato.

### Classi interne
Come per i metodi e le variabili di istanza, una classe interna è associata a un'istanza della sua classe di inclusione e ha accesso diretto ai metodi e ai campi di quell'oggetto. Inoltre, poiché una classe interna è associata a un'istanza, non può definire alcun membro statico.

Gli oggetti che sono istanze di una classe interna esistono all'interno di un'istanza della classe esterna. Considera le seguenti classi:
```java
class OuterClass {
    ...
    class InnerClass {
        ...
    }
}
```
Un'istanza di InnerClass può esistere solo all'interno di un'istanza di OuterClass e ha accesso diretto ai metodi e ai campi della sua istanza di inclusione.

Per creare un'istanza di una classe interna, devi prima istanziare la classe esterna. Quindi, crea l'oggetto interno all'interno dell'oggetto esterno con questa sintassi:

```java
OuterClass outerObject = new OuterClass();
OuterClass.InnerClass innerObject = outerObject.new InnerClass();
```

### Classi nidificate statiche
Come per i metodi e le variabili di classe, una classe nidificata statica è associata alla sua classe esterna. E come i metodi di classe static, una classe nidificata statica non può fare riferimento direttamente a variabili di istanza o metodi definiti nella sua classe che li racchiude: può usarli solo attraverso un riferimento a un oggetto

Istanzia una classe nidificata statica allo stesso modo di una classe di primo livello:

```java
StaticNestedClass staticNestedObject = new StaticNestedClass();
```

### Esempio di classe interna e classe statica nidificata
L'esempio seguente, OuterClass, insieme a TopLevelClass, mostra a quali membri della classe di OuterClass possono accedere una classe interna (InnerClass), una classe statica nidificata (StaticNestedClass) e una classe di livello superiore (TopLevelClass):

OuterClass.java
```java
public class OuterClass {

    String outerField = "Outer field";
    static String staticOuterField = "Static outer field";

    class InnerClass {
        void accessMembers() {
            System.out.println(outerField);
            System.out.println(staticOuterField);
        }
    }

    static class StaticNestedClass {
        void accessMembers(OuterClass outer) {
            // Compiler error: Cannot make a static reference to the non-static
            //     field outerField
            // System.out.println(outerField);
            System.out.println(outer.outerField);
            System.out.println(staticOuterField);
        }
    }

    public static void main(String[] args) {
        System.out.println("Inner class:");
        System.out.println("------------");
        OuterClass outerObject = new OuterClass();
        OuterClass.InnerClass innerObject = outerObject.new InnerClass();
        innerObject.accessMembers();

        System.out.println("\nStatic nested class:");
        System.out.println("--------------------");
        StaticNestedClass staticNestedObject = new StaticNestedClass();        
        staticNestedObject.accessMembers(outerObject);
        
        System.out.println("\nTop-level class:");
        System.out.println("--------------------");
        TopLevelClass topLevelObject = new TopLevelClass();        
        topLevelObject.accessMembers(outerObject);                
    }
}
```

TopLevelClass.java
```java
public class TopLevelClass {

    void accessMembers(OuterClass outer) {     
        // Compiler error: Cannot make a static reference to the non-static
        //     field OuterClass.outerField
        // System.out.println(OuterClass.outerField);
        System.out.println(outer.outerField);
        System.out.println(OuterClass.staticOuterField);
    }  
}
```

Si noti che una classe nidificata statica interagisce con i membri di istanza della sua classe esterna proprio come qualsiasi altra classe di primo livello. La classe nidificata statica StaticNestedClass non può accedere direttamente a outerField perché è una variabile di istanza della classe di inclusione, OuterClass. Il compilatore Java genera un errore nell'istruzione evidenziata:
```java
static class StaticNestedClass {
    void accessMembers(OuterClass outer) {
       // Compiler error: Cannot make a static reference to the non-static
       //     field outerField
       **System.out.println(outerField);**
    }
}
```
Per correggere questo errore, accedi a externalField tramite un riferimento a un oggetto:
```java
System.out.println(outer.outerField);
```
Allo stesso modo, neanche la classe di primo livello TopLevelClass può accedere direttamente a outerField.

### Shadowing
Se una dichiarazione di un tipo (come una variabile membro o un nome di parametro) in un particolare ambito (come una classe interna o una definizione di metodo) ha lo stesso nome di un'altra dichiarazione nell'ambito di inclusione, la dichiarazione oscura la dichiarazione dell'ambito di inclusione. Non puoi fare riferimento a una dichiarazione ombreggiata solo con il suo nome. L'esempio seguente, ShadowTest, lo dimostra:
```java
public class ShadowTest {

    public int x = 0;

    class FirstLevel {

        public int x = 1;

        void methodInFirstLevel(int x) {
            System.out.println("x = " + x);
            System.out.println("this.x = " + this.x);
            System.out.println("ShadowTest.this.x = " + ShadowTest.this.x);
        }
    }

    public static void main(String... args) {
        ShadowTest st = new ShadowTest();
        ShadowTest.FirstLevel fl = st.new FirstLevel();
        fl.methodInFirstLevel(23);
    }
}
```
Questo esempio definisce tre variabili denominate x: la variabile membro della classe ShadowTest, la variabile membro della classe interna FirstLevel e il parametro nel metodo methodInFirstLevel. La variabile x definita come parametro del metodo methodInFirstLevel oscura la variabile della classe interna FirstLevel. Di conseguenza, quando si utilizza la variabile x nel metodo methodInFirstLevel, fa riferimento al parametro del metodo. Per fare riferimento alla variabile membro della classe interna FirstLevel, utilizzare la parola chiave this per rappresentare l'ambito di inclusione:
```java
System.out.println("this.x = " + this.x);
```
Fare riferimento alle variabili membro che racchiudono ambiti più grandi in base al nome della classe a cui appartengono. Ad esempio, la seguente istruzione accede alla variabile membro della classe ShadowTest dal metodo methodInFirstLevel:
```java
System.out.println("ShadowTest.this.x = " + ShadowTest.this.x);
```

### Serializzazione
La serializzazione delle classi interne, comprese le classi locali e anonime, è fortemente sconsigliata. Quando il compilatore Java compila determinati costrutti, come le classi interne, crea costrutti sintetici; si tratta di classi, metodi, campi e altri costrutti che non hanno un costrutto corrispondente nel codice sorgente. I costrutti sintetici consentono ai compilatori Java di implementare nuove funzionalità del linguaggio Java senza modifiche alla JVM. Tuttavia, i costrutti sintetici possono variare tra le diverse implementazioni del compilatore Java, il che significa che anche i file .class possono variare tra le diverse implementazioni. Di conseguenza, potresti avere problemi di compatibilità se serializzi una classe interna e poi la deserializzi con un'implementazione JRE diversa. Vedere la sezione Parametri impliciti e sintetici nella sezione Ottenere nomi di parametri di metodo per ulteriori informazioni sui costrutti sintetici generati quando viene compilata una classe interna.

### Esempio di Inner Class
Per vedere una classe interna in uso, considera prima un array. Nell'esempio seguente si crea una matrice, la si riempie con valori interi e quindi si generano solo i valori di indici pari della matrice in ordine crescente.

L'esempio DataStructure.java che segue è costituito da:

- La classe esterna di DataStructure, che include un costruttore per creare un'istanza di DataStructure contenente una matrice riempita con valori interi consecutivi (0, 1, 2, 3 e così via) e un metodo che stampa gli elementi della matrice che hanno un indice pari valore.
- La classe interna EvenIterator, che implementa l'interfaccia DataStructureIterator, che estende l'interfaccia Iterator< Integer>. Gli iteratori vengono utilizzati per scorrere una struttura di dati e in genere dispongono di metodi per verificare l'ultimo elemento, recuperare l'elemento corrente e passare all'elemento successivo.
- Un metodo principale che crea un'istanza di un oggetto DataStructure (ds), quindi richiama il metodo printEven per stampare gli elementi dell'array arrayOfInts che hanno un valore di indice pari.

```java
public class DataStructure {
    
    // Create an array
    private final static int SIZE = 15;
    private int[] arrayOfInts = new int[SIZE];
    
    public DataStructure() {
        // fill the array with ascending integer values
        for (int i = 0; i < SIZE; i++) {
            arrayOfInts[i] = i;
        }
    }
    
    public void printEven() {
        
        // Print out values of even indices of the array
        DataStructureIterator iterator = this.new EvenIterator();
        while (iterator.hasNext()) {
            System.out.print(iterator.next() + " ");
        }
        System.out.println();
    }
    
    interface DataStructureIterator extends java.util.Iterator<Integer> { } 

    // Inner class implements the DataStructureIterator interface,
    // which extends the Iterator<Integer> interface
    
    private class EvenIterator implements DataStructureIterator {
        
        // Start stepping through the array from the beginning
        private int nextIndex = 0;
        
        public boolean hasNext() {
            
            // Check if the current element is the last in the array
            return (nextIndex <= SIZE - 1);
        }        
        
        public Integer next() {
            
            // Record a value of an even index of the array
            Integer retValue = Integer.valueOf(arrayOfInts[nextIndex]);
            
            // Get the next even element
            nextIndex += 2;
            return retValue;
        }
    }
    
    public static void main(String s[]) {
        
        // Fill the array with integer values and print out only
        // values of even indices
        DataStructure ds = new DataStructure();
        ds.printEven();
    }
}
```
Si noti che la classe EvenIterator fa riferimento direttamente alla variabile di istanza arrayOfInts dell'oggetto DataStructure.

È possibile utilizzare le classi interne per implementare classi helper come quella mostrata in questo esempio. Per gestire gli eventi dell'interfaccia utente, è necessario sapere come utilizzare le classi interne, poiché il meccanismo di gestione degli eventi ne fa ampio uso.

#### Classi locali e anonime
Ci sono due tipi aggiuntivi di classi interne. Puoi dichiarare una classe interna all'interno del corpo di un metodo. Queste classi sono conosciute come classi locali. Puoi anche dichiarare una classe interna all'interno del corpo di un metodo senza nominare la classe. Queste classi sono note come classi anonime.

#### Modificatori
Puoi usare gli stessi modificatori per le classi interne che usi per gli altri membri della classe esterna. Ad esempio, puoi utilizzare gli identificatori di accesso private, public e protected per limitare l'accesso alle classi interne, proprio come li usi per limitare l'accesso agli altri membri della classe.

#### Classi Locali
Puoi usare gli stessi modificatori per le classi interne che usi per gli altri membri della classe esterna. Ad esempio, puoi utilizzare gli identificatori di accesso private, public e protected per limitare l'accesso alle classi interne, proprio come li usi per limitare l'accesso agli altri membri della classe.

##### Dichiarare classi locali
È possibile definire una classe locale all'interno di qualsiasi blocco (consultare Espressioni, istruzioni e blocchi per ulteriori informazioni). Ad esempio, puoi definire una classe locale nel corpo di un metodo, un ciclo for o una clausola if.

L'esempio seguente, LocalClassExample, convalida due numeri di telefono. Definisce la classe locale PhoneNumber nel metodo validatePhoneNumber:
```java
public class LocalClassExample {
  
    static String regularExpression = "[^0-9]";
  
    public static void validatePhoneNumber(
        String phoneNumber1, String phoneNumber2) {
      
        final int numberLength = 10;
        
        // Valid in JDK 8 and later:
       
        // int numberLength = 10;
       
        class PhoneNumber {
            
            String formattedPhoneNumber = null;

            PhoneNumber(String phoneNumber){
                // numberLength = 7;
                String currentNumber = phoneNumber.replaceAll(
                  regularExpression, "");
                if (currentNumber.length() == numberLength)
                    formattedPhoneNumber = currentNumber;
                else
                    formattedPhoneNumber = null;
            }

            public String getNumber() {
                return formattedPhoneNumber;
            }
            
            // Valid in JDK 8 and later:

//            public void printOriginalNumbers() {
//                System.out.println("Original numbers are " + phoneNumber1 +
//                    " and " + phoneNumber2);
//            }
        }

        PhoneNumber myNumber1 = new PhoneNumber(phoneNumber1);
        PhoneNumber myNumber2 = new PhoneNumber(phoneNumber2);
        
        // Valid in JDK 8 and later:

//        myNumber1.printOriginalNumbers();

        if (myNumber1.getNumber() == null) 
            System.out.println("First number is invalid");
        else
            System.out.println("First number is " + myNumber1.getNumber());
        if (myNumber2.getNumber() == null)
            System.out.println("Second number is invalid");
        else
            System.out.println("Second number is " + myNumber2.getNumber());

    }

    public static void main(String... args) {
        validatePhoneNumber("123-456-7890", "456-7890");
    }
}
```


# Interfacce ed ereditarietà (forse lezione 9)

## Interfacce
Ci sono un certo numero di situazioni nell'ingegneria del software in cui è importante che gruppi disparati di programmatori accettino un "contratto" che spieghi come interagisce il loro software. Ogni gruppo dovrebbe essere in grado di scrivere il proprio codice senza alcuna conoscenza di come viene scritto il codice dell'altro gruppo. In generale, le interfacce sono tali contratti.

Ad esempio, immagina una società futuristica in cui auto robotiche controllate da computer trasportano passeggeri per le strade della città senza un operatore umano. Le case automobilistiche scrivono software (Java, ovviamente) che aziona l'automobile: fermati, avvia, accelera, gira a sinistra e così via. Un altro gruppo industriale, produttori di strumenti di guida elettronica, realizza sistemi informatici che ricevono dati di posizione GPS (Global Positioning System) e trasmissione wireless delle condizioni del traffico e utilizzano tali informazioni per guidare l'auto.

Le case automobilistiche devono pubblicare un'interfaccia standard del settore che spieghi in dettaglio quali metodi possono essere invocati per far muovere l'auto (qualsiasi auto, di qualsiasi produttore). I produttori di guida possono quindi scrivere un software che richiami i metodi descritti nell'interfaccia per comandare l'auto. Nessuno dei due gruppi industriali deve sapere come viene implementato il software dell'altro gruppo. Ciascun gruppo, infatti, considera il proprio software altamente proprietario e si riserva il diritto di modificarlo in qualsiasi momento, purché continui ad aderire all'interfaccia pubblicata.

### Interfacce in Java
Nel linguaggio di programmazione Java, un'interfaccia è un tipo di riferimento, simile a una classe, che può contenere solo costanti, firme di metodo, metodi predefiniti, metodi statici e tipi nidificati. I corpi dei metodi esistono solo per i metodi predefiniti e per i metodi statici. Le interfacce non possono essere istanziate: possono essere implementate solo da classi o estese da altre interfacce. L'estensione è discussa più avanti in questa lezione.

La definizione di un'interfaccia è simile alla creazione di una nuova classe:
```java
public interface OperateCar {

   // constant declarations, if any

   // method signatures
   
   // An enum with values RIGHT, LEFT
   int turn(Direction direction,
            double radius,
            double startSpeed,
            double endSpeed);
   int changeLanes(Direction direction,
                   double startSpeed,
                   double endSpeed);
   int signalTurn(Direction direction,
                  boolean signalOn);
   int getRadarFront(double distanceToCar,
                     double speedOfCar);
   int getRadarRear(double distanceToCar,
                    double speedOfCar);
         ......
   // more method signatures
}
```

Si noti che le firme del metodo non hanno parentesi graffe e terminano con un punto e virgola.

Per utilizzare un'interfaccia, scrivi una classe che implementa l'interfaccia. Quando una classe istanziabile implementa un'interfaccia, fornisce un corpo del metodo per ciascuno dei metodi dichiarati nell'interfaccia. Per esempio,
```java
public class OperateBMW760i implements OperateCar {

    // the OperateCar method signatures, with implementation --
    // for example:
    public int signalTurn(Direction direction, boolean signalOn) {
       // code to turn BMW's LEFT turn indicator lights on
       // code to turn BMW's LEFT turn indicator lights off
       // code to turn BMW's RIGHT turn indicator lights on
       // code to turn BMW's RIGHT turn indicator lights off
    }

    // other members, as needed -- for example, helper classes not 
    // visible to clients of the interface
}
```
Nell'esempio dell'auto robotica sopra, sono le case automobilistiche che implementeranno l'interfaccia. L'implementazione di Chevrolet sarà sostanzialmente diversa da quella di Toyota, ovviamente, ma entrambi i produttori aderiranno alla stessa interfaccia. I produttori di guide, che sono i clienti dell'interfaccia, costruiranno sistemi che utilizzano i dati GPS sulla posizione di un'auto, mappe stradali digitali e dati sul traffico per guidare l'auto. In tal modo, i sistemi di guida invocheranno i metodi di interfaccia: svoltare, cambiare corsia, frenare, accelerare e così via.

### Interfacce come API
L'esempio dell'auto robotica mostra un'interfaccia utilizzata come API (Application Programming Interface) standard del settore. Le API sono comuni anche nei prodotti software commerciali. In genere, un'azienda vende un pacchetto software che contiene metodi complessi che un'altra azienda desidera utilizzare nel proprio prodotto software. Un esempio potrebbe essere un pacchetto di metodi di elaborazione delle immagini digitali che vengono venduti alle aziende che producono programmi di grafica per utenti finali. La società di elaborazione delle immagini scrive le sue classi per implementare un'interfaccia, che rende pubblica ai propri clienti. L'azienda grafica richiama quindi i metodi di elaborazione delle immagini utilizzando le firme ei tipi restituiti definiti nell'interfaccia. Sebbene l'API dell'azienda di elaborazione delle immagini sia resa pubblica (ai suoi clienti), la sua implementazione dell'API è tenuta segreta e gelosamente custodita, infatti potrebbe rivedere l'implementazione in un secondo momento purché continui a implementare l'interfaccia originale su cui i suoi clienti hanno fatto affidamento.

### Definire un Interfaccia
Una dichiarazione di interfaccia è composta da modificatori, la parola chiave interface, il nome dell'interfaccia, un elenco separato da virgole di interfacce padre (se presenti) e il corpo dell'interfaccia. Per esempio:
```java
public interface GroupedInterface extends Interface1, Interface2, Interface3 {

    // constant declarations
    
    // base of natural logarithms
    double E = 2.718282;
 
    // method signatures
    void doSomething (int i, double x);
    int doSomethingElse(String s);
}
```
L'identificatore di accesso pubblico indica che l'interfaccia può essere utilizzata da qualsiasi classe in qualsiasi pacchetto. Se non specifichi che l'interfaccia è pubblica, la tua interfaccia è accessibile solo alle classi definite nello stesso pacchetto dell'interfaccia.

Un'interfaccia può estendere altre interfacce, proprio come una sottoclasse di classe o estendere un'altra classe. Tuttavia, mentre una classe può estendere solo un'altra classe, un'interfaccia può estendere un numero qualsiasi di interfacce. La dichiarazione dell'interfaccia include un elenco separato da virgole di tutte le interfacce che estende.

#### Corpo dell'interfaccia
Il corpo dell'interfaccia può contenere metodi astratti, metodi predefiniti e metodi statici. Un metodo astratto all'interno di un'interfaccia è seguito da un punto e virgola, ma senza parentesi graffe (un metodo astratto non contiene un'implementazione). I metodi predefiniti sono definiti con il modificatore predefinito e i metodi statici con la parola chiave static. Tutti i metodi astratti, predefiniti e statici in un'interfaccia sono implicitamente pubblici, quindi puoi omettere il modificatore public.

Inoltre, un'interfaccia può contenere dichiarazioni di costanti. Tutti i valori costanti definiti in un'interfaccia sono implicitamente pubblici, statici e finali. Ancora una volta, puoi omettere questi modificatori.

### Implementare un interfaccia

Per dichiarare una classe che implementa un'interfaccia, includi una clausola implements nella dichiarazione di classe. La tua classe può implementare più di un'interfaccia, quindi la parola chiave implements è seguita da un elenco separato da virgole delle interfacce implementate dalla classe. Per convenzione, la clausola implements segue la clausola extends, se presente.

#### Un'interfaccia di esempio, Relatable

Si consideri un'interfaccia che definisce come confrontare le dimensioni degli oggetti.
```java
public interface Relatable {
        
    // this (object calling isLargerThan)
    // and other must be instances of 
    // the same class returns 1, 0, -1 
    // if this is greater than, 
    // equal to, or less than other
    public int isLargerThan(Relatable other);
}
```
Se vuoi essere in grado di confrontare le dimensioni di oggetti simili, indipendentemente da cosa siano, la classe che li istanzia dovrebbe implementare Relatable.

Qualsiasi classe può implementare Relatable se esiste un modo per confrontare la "dimensione" relativa degli oggetti istanziati dalla classe. Per le stringhe, potrebbe essere il numero di caratteri; per i libri, potrebbe essere il numero di pagine; per gli studenti, potrebbe essere peso; e così via. Per gli oggetti geometrici planari, l'area sarebbe una buona scelta (vedi la classe RectanglePlus che segue), mentre il volume funzionerebbe per gli oggetti geometrici tridimensionali. Tutte queste classi possono implementare il metodo isLargerThan().

Se sai che una classe implementa Relatable, allora sai che puoi confrontare la dimensione degli oggetti istanziati da quella classe.

#### Implementazione dell'interfaccia Relatable
Ecco la classe Rectangle che è stata presentata nella sezione [[Lezione 6#Creare oggetti|Lezione 6 - Creare oggetti]], riscritta per implementare Relatable.
```java
public class RectanglePlus 
    implements Relatable {
    public int width = 0;
    public int height = 0;
    public Point origin;

    // four constructors
    public RectanglePlus() {
        origin = new Point(0, 0);
    }
    public RectanglePlus(Point p) {
        origin = p;
    }
    public RectanglePlus(int w, int h) {
        origin = new Point(0, 0);
        width = w;
        height = h;
    }
    public RectanglePlus(Point p, int w, int h) {
        origin = p;
        width = w;
        height = h;
    }

    // a method for moving the rectangle
    public void move(int x, int y) {
        origin.x = x;
        origin.y = y;
    }

    // a method for computing
    // the area of the rectangle
    public int getArea() {
        return width * height;
    }
    
    // a method required to implement
    // the Relatable interface
    public int isLargerThan(Relatable other) {
        **RectanglePlus otherRect 
            = (RectanglePlus)other;**
        if (this.getArea() < otherRect.getArea())
            return -1;
        else if (this.getArea() > otherRect.getArea())
            return 1;
        else
            return 0;               
    }
}
```

