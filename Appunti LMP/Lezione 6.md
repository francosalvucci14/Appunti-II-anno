# Classi
L'introduzione ai concetti orientati agli oggetti ha utilizzato una classe di biciclette come esempio, con biciclette da corsa, mountain bike e biciclette tandem come sottoclassi. Ecco un codice di esempio per una possibile implementazione di una classe Bicycle, per darti una panoramica di una dichiarazione di classe. Le sezioni successive di questa lezione eseguiranno il backup e spiegheranno passo dopo passo le dichiarazioni di classe

```java
public class Bicycle {
        
    // **the Bicycle class has**
    // **three _fields_**
    public int cadence;
    public int gear;
    public int speed;
        
    // **the Bicycle class has**
    // **one _constructor_**
    public Bicycle(int startCadence, int startSpeed, int startGear) {
        gear = startGear;
        cadence = startCadence;
        speed = startSpeed;
    }
        
    // **the Bicycle class has**
    // **four _methods_**
    public void setCadence(int newValue) {
        cadence = newValue;
    }
        
    public void setGear(int newValue) {
        gear = newValue;
    }
        
    public void applyBrake(int decrement) {
        speed -= decrement;
    }
        
    public void speedUp(int increment) {
        speed += increment;
    }
        
}
```
Una dichiarazione di classe per una classe MountainBike che è una sottoclasse di Bicycle potrebbe assomigliare a questa:
```java
public class MountainBike extends Bicycle {
        
    // **the MountainBike subclass has**
    // **one _field_**
    public int seatHeight;

    // **the MountainBike subclass has**
    // **one _constructor_**
    public MountainBike(int startHeight, int startCadence,
                        int startSpeed, int startGear) {
        super(startCadence, startSpeed, startGear);
        seatHeight = startHeight;
    }   
        
    // **the MountainBike subclass has**
    // **one _method_**
    public void setHeight(int newValue) {
        seatHeight = newValue;
    }   

}
```
MountainBike eredita tutti i campi e i metodi di Bicycle e aggiunge il field seatHeight e un metodo per impostarlo (le mountain bike hanno i sedili che possono essere spostati su e giù a seconda del terreno).

## Dichiarare una classe

Hai visto classi definite nel modo seguente:
```java
class _MyClass_ {
    // field, constructor, and 
    // method declarations
}
```

Questa è una dichiarazione di classe. Il corpo della classe (l'area tra le parentesi graffe) contiene tutto il codice che prevede il ciclo di vita degli oggetti creati dalla classe: costruttori per inizializzare nuovi oggetti, dichiarazioni per i campi che forniscono lo stato della classe e dei suoi oggetti, e metodi per implementare il comportamento della classe e dei suoi oggetti.

La precedente dichiarazione di classe è minima. Contiene solo quei componenti di una dichiarazione di classe che sono richiesti. Puoi fornire maggiori informazioni sulla classe, come il nome della sua superclasse, se implementa interfacce e così via, all'inizio della dichiarazione di classe. Per esempio,
```java
class _MyClass extends MySuperClass implements YourInterface_ {
    // field, constructor, and
    // method declarations
}
```

significa che MyClass è una sottoclasse di MySuperClass e che implementa l'interfaccia YourInterface.

Puoi anche aggiungere modificatori come public o private all'inizio, così puoi vedere che la riga di apertura di una dichiarazione di classe può diventare piuttosto complicata. I modificatori public e private, che determinano a quali altre classi possono accedere MyClass, sono discussi più avanti in questa lezione. La lezione sulle interfacce e sull'ereditarietà spiegherà come e perché dovresti usare le parole chiave extends e implementa in una dichiarazione di classe. Per il momento non devi preoccuparti di queste complicazioni extra.

In generale, le dichiarazioni di classe possono includere questi componenti, nell'ordine:
- Modificatori come public, private e molti altri che incontrerai in seguito. (Tuttavia, tieni presente che il modificatore privato può essere applicato solo alle classi nidificate.)
- Il nome della classe, con la lettera iniziale maiuscola per convenzione.
- Il nome del genitore della classe (superclasse), se presente, preceduto dalla parola chiave extends. Una classe può estendere (sottoclasse) solo un genitore.
- Un elenco separato da virgole di interfacce implementate dalla classe, se presente, preceduto dalla parola chiave implementa. Una classe può implementare più di un'interfaccia.
- Il corpo della classe, racchiuso tra parentesi graffe, {}.

## Dichiarazione delle variabili membro

Esistono diversi tipi di variabili:
- Variabili membro in una classe: queste sono chiamate campi.
- Variabili in un metodo o blocco di codice: queste sono chiamate variabili locali.
- Variabili nelle dichiarazioni di metodo: queste sono chiamate parametri.

Le dichiarazioni di campo sono composte da tre componenti, nell'ordine:
- Zero o più modificatori, come public o private.
- Il tipo del campo.
- Il nome del campo.

### Accedere ai modificatori

Il primo modificatore (più a sinistra) utilizzato consente di controllare quali altre classi hanno accesso a un campo membro. Per il momento, considera solo pubblico e privato. Altri modificatori di accesso verranno discussi in seguito.
- public modificatore: il campo è accessibile da tutte le classi.
- modificatore privato: il campo è accessibile solo all'interno della propria classe.

Nello spirito dell'incapsulamento, è comune rendere privati i campi. Ciò significa che è possibile accedervi direttamente solo dalla classe Bicicletta. Tuttavia, abbiamo ancora bisogno di accedere a questi valori. Questo può essere fatto indirettamente aggiungendo metodi pubblici che ottengono i valori di campo per noi:

```java
public class Bicycle {
        
    private int cadence;
    private int gear;
    private int speed;
        
    public Bicycle(int startCadence, int startSpeed, int startGear) {
        gear = startGear;
        cadence = startCadence;
        speed = startSpeed;
    }
        
    public int getCadence() {
        return cadence;
    }
        
    public void setCadence(int newValue) {
        cadence = newValue;
    }
        
    public int getGear() {
        return gear;
    }
        
    public void setGear(int newValue) {
        gear = newValue;
    }
        
    public int getSpeed() {
        return speed;
    }
        
    public void applyBrake(int decrement) {
        speed -= decrement;
    }
        
    public void speedUp(int increment) {
        speed += increment;
    }
}
```

### Tipi
Tutte le variabili devono avere un tipo. Puoi usare tipi primitivi come int, float, boolean, ecc. Oppure puoi usare tipi di riferimento, come stringhe, array o oggetti.
### Nomi delle variabili
Tutte le variabili, siano esse campi, variabili locali o parametri, seguono le stesse regole e convenzioni di denominazione trattate nella lezione Nozioni di base sul linguaggio, Variabili - Denominazione.

In questa lezione, tieni presente che le stesse regole e convenzioni di denominazione vengono utilizzate per i nomi dei metodi e delle classi, tranne quello
- la prima lettera del nome di una classe dovrebbe essere in maiuscolo, e
- la prima (o l'unica) parola nel nome di un metodo dovrebbe essere un verbo.

## Definire i metodi

Ecco un esempio di una tipica dichiarazione di metodo:
```java
public double calculateAnswer(double wingSpan, int numberOfEngines,
                              double length, double grossTons) {
    //do the calculation here
}
```

Gli unici elementi richiesti di una dichiarazione di metodo sono il tipo restituito del metodo, il nome, una coppia di parentesi (()) e un corpo tra parentesi graffe, {}.

Più in generale, le dichiarazioni di metodo hanno sei componenti, nell'ordine:
- Modificatori: come pubblico, privato e altri di cui imparerai in seguito.
- Il tipo restituito: il tipo di dati del valore restituito dal metodo o void se il metodo non restituisce un valore.
- Il nome del metodo: le regole per i nomi dei campi si applicano anche ai nomi dei metodi, ma la convenzione è leggermente diversa.
- L'elenco dei parametri tra parentesi: un elenco delimitato da virgole di parametri di input, preceduto dai relativi tipi di dati, racchiuso tra parentesi, (). Se non ci sono parametri, è necessario utilizzare parentesi vuote.
- Un elenco di eccezioni, di cui parleremo più avanti.
- Il corpo del metodo, racchiuso tra parentesi graffe: il codice del metodo, inclusa la dichiarazione delle variabili locali, va qui.

La firma del metodo sopra dichiarato è:
```java
calculateAnswer(double, int, double, double)
```

### Dare un nome a un metodo

Sebbene un nome di metodo possa essere qualsiasi identificatore legale, le convenzioni di codice limitano i nomi di metodo. Per convenzione, i nomi dei metodi dovrebbero essere un verbo in minuscolo o un nome composto da più parole che inizia con un verbo in minuscolo, seguito da aggettivi, nomi, ecc. Nei nomi composti da più parole, la prima lettera di ciascuna delle seconde parole e le seguenti dovrebbe essere in maiuscolo. Ecco alcuni esempi:

- run
- runFast
- getBackground
- getFinalData
- compareTo
- setX
- isEmpty

In genere, un metodo ha un nome univoco all'interno della sua classe. Tuttavia, un metodo potrebbe avere lo stesso nome di altri metodi a causa del sovraccarico del metodo.

### Sovraccarico dei metodi

Il linguaggio di programmazione Java supporta i metodi di sovraccarico e Java può distinguere tra metodi con diverse firme di metodo. Ciò significa che i metodi all'interno di una classe possono avere lo stesso nome se hanno elenchi di parametri diversi (ci sono alcune qualifiche che verranno discusse nella lezione intitolata "Interfacce ed ereditarietà").

Si supponga di avere una classe in grado di utilizzare la calligrafia per disegnare vari tipi di dati (stringhe, numeri interi e così via) e che contenga un metodo per disegnare ogni tipo di dati. È complicato utilizzare un nuovo nome per ogni metodo, ad esempio drawString, drawInteger, drawFloat e così via. Nel linguaggio di programmazione Java è possibile utilizzare lo stesso nome per tutti i metodi di disegno ma passare un elenco di argomenti diverso a ciascun metodo. Pertanto, la classe di disegno dati potrebbe dichiarare quattro metodi denominati draw, ognuno dei quali ha un elenco di parametri diverso.

```java
public class DataArtist {
    ...
    public void draw(String s) {
        ...
    }
    public void draw(int i) {
        ...
    }
    public void draw(double f) {
        ...
    }
    public void draw(int i, double f) {
        ...
    }
}
```

I metodi sovraccaricati si differenziano per il numero e il tipo degli argomenti passati nel metodo. Nell'esempio di codice, draw(String s) e draw(int i) sono metodi distinti e univoci perché richiedono tipi di argomenti diversi.

Non puoi dichiarare più di un metodo con lo stesso nome e lo stesso numero e tipo di argomenti, perché il compilatore non può distinguerli.

Il compilatore non considera il tipo restituito durante la differenziazione dei metodi, quindi non è possibile dichiarare due metodi con la stessa firma anche se hanno un tipo restituito diverso.

## Fornire costruttori per le tue classi

Una classe contiene costruttori che vengono invocati per creare oggetti dal progetto della classe. Le dichiarazioni del costruttore sembrano dichiarazioni di metodo, tranne per il fatto che usano il nome della classe e non hanno un tipo restituito. Ad esempio, Bicycle ha un costruttore:

```java
public Bicycle(int startCadence, int startSpeed, int startGear) {
    gear = startGear;
    cadence = startCadence;
    speed = startSpeed;
}
```

Per creare un nuovo oggetto Bicycle chiamato myBike, viene chiamato un costruttore dall'operatore new:
```java
Bicycle myBike = new Bicycle(30, 0, 8);
```

Sebbene Bicycle abbia un solo costruttore, potrebbe averne altri, incluso un costruttore senza argomenti:
```java
public Bicycle() {
    gear = 1;
    cadence = 10;
    speed = 0;
}
```
Entrambi i costruttori avrebbero potuto essere dichiarati in Bicycle perché hanno elenchi di argomenti diversi. Come per i metodi, la piattaforma Java differenzia i costruttori in base al numero di argomenti nell'elenco e ai loro tipi. Non puoi scrivere due costruttori che hanno lo stesso numero e tipo di argomenti per la stessa classe, perché la piattaforma non sarebbe in grado di distinguerli. Ciò provoca un errore in fase di compilazione.

Non devi fornire alcun costruttore per la tua classe, ma devi stare attento quando lo fai. Il compilatore fornisce automaticamente un costruttore predefinito senza argomenti per qualsiasi classe senza costruttori. Questo costruttore predefinito chiamerà il costruttore senza argomenti della superclasse. In questa situazione, il compilatore si lamenterà se la superclasse non ha un costruttore senza argomenti, quindi è necessario verificare che lo sia. Se la tua classe non ha una superclasse esplicita, allora ha una superclasse implicita di Object, che ha un costruttore senza argomenti.

Puoi usare tu stesso un costruttore di superclassi. La lezione di MountainBike all'inizio di questa lezione ha fatto proprio questo. Questo sarà discusso più avanti, nella lezione sulle interfacce e l'ereditarietà.

È possibile utilizzare i modificatori di accesso nella dichiarazione di un costruttore per controllare quali altre classi possono chiamare il costruttore.

## Passare informazioni a un metodo oa un costruttore

La dichiarazione per un metodo o un costruttore dichiara il numero e il tipo degli argomenti per quel metodo o costruttore. Ad esempio, il seguente è un metodo che calcola le rate mensili di un mutuo per la casa, in base all'importo del prestito, al tasso di interesse, alla durata del prestito (il numero di periodi) e al valore futuro del prestito:
```java
public double computePayment(
                  double **loanAmt**,
                  double **rate**,
                  double **futureValue**,
                  int **numPeriods**) {
    double interest = **rate** / 100.0;
    double partial1 = Math.pow((1 + interest), 
                    - **numPeriods**);
    double denominator = (1 - partial1) / interest;
    double answer = (-**loanAmt** / denominator)
                    - ((**futureValue** * partial1) / denominator);
    return answer;
}
```

Questo metodo ha quattro parametri: l'importo del prestito, il tasso di interesse, il valore futuro e il numero di periodi. I primi tre sono numeri in virgola mobile a precisione doppia e il quarto è un numero intero. I parametri vengono utilizzati nel corpo del metodo e in fase di esecuzione assumeranno i valori degli argomenti passati.

### Tipi di parametri

È possibile utilizzare qualsiasi tipo di dati per un parametro di un metodo o un costruttore. Ciò include tipi di dati primitivi, come double, float e interi, come hai visto nel metodo computePayment, e tipi di dati di riferimento, come oggetti e matrici.

Ecco un esempio di metodo che accetta un array come argomento. In questo esempio, il metodo crea un nuovo oggetto Polygon e lo inizializza da una matrice di oggetti Point (supponiamo che Point sia una classe che rappresenta una coordinata x, y):

```java
public Polygon polygonFrom(Point[] corners) {
    // method body goes here
}
```

### Numero arbitrario di argomenti
È possibile utilizzare un costrutto chiamato varargs per passare un numero arbitrario di valori a un metodo. Usi varargs quando non sai quanti argomenti di un particolare tipo verranno passati al metodo. È una scorciatoia per creare manualmente un array (il metodo precedente avrebbe potuto utilizzare varags anziché un array).

Per utilizzare varargs, segui il tipo dell'ultimo parametro con i puntini di sospensione (tre punti, ...), quindi uno spazio e il nome del parametro. Il metodo può quindi essere chiamato con qualsiasi numero di quel parametro, incluso nessuno.
```java
public Polygon polygonFrom(Point... corners) {
    int numberOfSides = corners.length;
    double squareOfSide1, lengthOfSide1;
    squareOfSide1 = (corners[1].x - corners[0].x)
                     * (corners[1].x - corners[0].x) 
                     + (corners[1].y - corners[0].y)
                     * (corners[1].y - corners[0].y);
    lengthOfSide1 = Math.sqrt(squareOfSide1);

    // more method body code follows that creates and returns a 
    // polygon connecting the Points
}
```

Puoi vedere che, all'interno del metodo, gli angoli sono trattati come un array. Il metodo può essere chiamato con un array o con una sequenza di argomenti. Il codice nel corpo del metodo tratterà il parametro come una matrice in entrambi i casi.

Vedrai più comunemente varag con i metodi di stampa; ad esempio, questo metodo printf:
```java
public PrintStream printf(String format, Object... args)
```
consente di stampare un numero arbitrario di oggetti. Può essere chiamato così:
```java
System.out.printf("%s: %d, %s%n", name, idnum, address);
```
o così
```java
System.out.printf("%s: %d, %s, %s, %s%n", name, idnum, address, phone, email);
```
### Nomi dei parametri

Quando dichiari un parametro a un metodo oa un costruttore, fornisci un nome per quel parametro. Questo nome viene utilizzato all'interno del corpo del metodo per fare riferimento all'argomento passato.

Il nome di un parametro deve essere univoco nel suo ambito. Non può essere uguale al nome di un altro parametro per lo stesso metodo o costruttore e non può essere il nome di una variabile locale all'interno del metodo o del costruttore.

Un parametro può avere lo stesso nome di uno dei campi della classe. Se questo è il caso, si dice che il parametro ombreggia il campo. L'ombreggiatura dei campi può rendere difficile la lettura del codice e viene convenzionalmente utilizzato solo all'interno di costruttori e metodi che impostano un campo particolare. Ad esempio, considera la seguente classe Circle e il relativo metodo setOrigin:
```java
public class Circle {
    private int x, y, radius;
    public void setOrigin(int x, int y) {
        ...
    }
}
```
La classe Circle ha tre campi: x, y e raggio. Il metodo setOrigin ha due parametri, ognuno dei quali ha lo stesso nome di uno dei campi. Ciascun parametro del metodo oscura il campo che ne condivide il nome. Quindi l'uso dei nomi semplici x o y all'interno del corpo del metodo si riferisce al parametro, non al campo. Per accedere al campo è necessario utilizzare un nome qualificato. Questo sarà discusso più avanti in questa lezione nella sezione intitolata "Uso di questa parola chiave".

### Passaggio di argomenti di tipo di dati primitivi
Gli argomenti primitivi, come un int o un double, vengono passati ai metodi in base al valore. Ciò significa che eventuali modifiche ai valori dei parametri esistono solo nell'ambito del metodo. Quando il metodo ritorna, i parametri sono spariti e qualsiasi modifica ad essi viene persa. Ecco un esempio:
```java
public class PassPrimitiveByValue {

    public static void main(String[] args) {
           
        int x = 3;
           
        // invoke passMethod() with 
        // x as argument
        passMethod(x);
           
        // print x to see if its 
        // value has changed
        System.out.println("After invoking passMethod, x = " + x);
           
    }
        
    // change parameter in passMethod()
    public static void passMethod(int p) {
        p = 10;
    }
}
```

### Passaggio di argomenti del tipo di dati di riferimento
Anche i parametri del tipo di dati eference, come gli oggetti, vengono passati ai metodi in base al valore. Ciò significa che quando il metodo ritorna, il riferimento passato fa ancora riferimento allo stesso oggetto di prima. Tuttavia, i valori dei campi dell'oggetto possono essere modificati nel metodo, se dispongono del livello di accesso appropriato.

Ad esempio, considera un metodo in una classe arbitraria che sposta gli oggetti Circle:
```java
public void moveCircle(Circle circle, int deltaX, int deltaY) {
    // code to move origin of circle to x+deltaX, y+deltaY
    circle.setX(circle.getX() + deltaX);
    circle.setY(circle.getY() + deltaY);
        
    // code to assign a new reference to circle
    circle = new Circle(0, 0);
}
```
Sia invocato il metodo con questi argomenti:
```java
moveCircle(myCircle, 23, 56)
```
All'interno del metodo, circle inizialmente si riferisce a myCircle. Il metodo cambia le coordinate xey dell'oggetto a cui fa riferimento il cerchio (ovvero myCircle) rispettivamente di 23 e 56. Queste modifiche persisteranno quando il metodo ritorna. Quindi al cerchio viene assegnato un riferimento a un nuovo oggetto Cerchio con x = y = 0. Questa riassegnazione non ha però alcuna permanenza, perché il riferimento è stato passato per valore e non può cambiare. All'interno del metodo, l'oggetto puntato da circle è cambiato, ma, quando il metodo ritorna, myCircle fa ancora riferimento allo stesso oggetto Circle di prima che il metodo fosse chiamato.

## Oggetti
Un tipico programma Java crea molti oggetti che, come sapete, interagiscono invocando metodi. Attraverso queste interazioni tra oggetti, un programma può svolgere varie attività, come implementare una GUI, eseguire un'animazione o inviare e ricevere informazioni su una rete. Una volta che un oggetto ha completato il lavoro per il quale è stato creato, le sue risorse vengono riciclate per essere utilizzate da altri oggetti.

Ecco un piccolo programma, chiamato CreateObjectDemo, che crea tre oggetti: un oggetto Point e due oggetti Rectangle. Avrai bisogno di tutti e tre i file sorgente per compilare questo programma.
```java
public class CreateObjectDemo {

    public static void main(String[] args) {
		
        // Declare and create a point object and two rectangle objects.
        Point originOne = new Point(23, 94);
        Rectangle rectOne = new Rectangle(originOne, 100, 200);
        Rectangle rectTwo = new Rectangle(50, 100);
		
        // display rectOne's width, height, and area
        System.out.println("Width of rectOne: " + rectOne.width);
        System.out.println("Height of rectOne: " + rectOne.height);
        System.out.println("Area of rectOne: " + rectOne.getArea());
		
        // set rectTwo's position
        rectTwo.origin = originOne;
		
        // display rectTwo's position
        System.out.println("X Position of rectTwo: " + rectTwo.origin.x);
        System.out.println("Y Position of rectTwo: " + rectTwo.origin.y);
		
        // move rectTwo and display its new position
        rectTwo.move(40, 72);
        System.out.println("X Position of rectTwo: " + rectTwo.origin.x);
        System.out.println("Y Position of rectTwo: " + rectTwo.origin.y);
    }
}
```

### Creare oggetti
Come sapete, una classe fornisce il progetto per gli oggetti; crei un oggetto da una classe. Ciascuna delle seguenti istruzioni tratte dal programma CreateObjectDemo crea un oggetto e lo assegna a una variabile:
```java
**Point originOne** = new Point(23, 94);
**Rectangle rectOne** = new Rectangle(originOne, 100, 200);
**Rectangle rectTwo** = new Rectangle(50, 100);
```

La prima riga crea un oggetto della classe Point e la seconda e la terza riga creano ciascuna un oggetto della classe Rectangle.

Ognuna di queste affermazioni ha tre parti (discusse in dettaglio di seguito):

- **Dichiarazione**: Il codice impostato in grassetto sono tutte dichiarazioni di variabili che associano un nome di variabile a un tipo di oggetto.
- **Istanza**: la nuova parola chiave è un operatore Java che crea l'oggetto.
- **Inizializzazione**: l'operatore new è seguito da una chiamata a un costruttore, che inizializza il nuovo oggetto.

### Dichiarare una variabile

In precedenza, hai imparato che per dichiarare una variabile, scrivi:
```java
type name;
```
Questo notifica al compilatore che utilizzerai name per fare riferimento ai dati il cui tipo è type. Con una variabile primitiva, questa dichiarazione riserva anche la giusta quantità di memoria per la variabile.
Puoi anche dichiarare una variabile di riferimento su una propria riga. Per esempio:
```java
Point originOne;
```

Se dichiari originOne in questo modo, il suo valore sarà indeterminato fino a quando non verrà effettivamente creato e assegnato un oggetto. La semplice dichiarazione di una variabile di riferimento non crea un oggetto. Per questo, è necessario utilizzare il nuovo operatore, come descritto nella sezione successiva. Devi assegnare un oggetto a originOne prima di usarlo nel tuo codice. Altrimenti, otterrai un errore del compilatore.

Una variabile in questo stato, che attualmente non fa riferimento a nessun oggetto, può essere illustrata come segue (il nome della variabile, originOne, più un riferimento che non punta a nulla):
![[appunti lmp/immagini/objects-null.gif|center|300]]
### Istanziare una classe
L'operatore new crea un'istanza di una classe allocando memoria per un nuovo oggetto e restituendo un riferimento a quella memoria. L'operatore new richiama anche il costruttore di oggetti.
L'operatore new richiede un singolo argomento suffisso: una chiamata a un costruttore. Il nome del costruttore fornisce il nome della classe di cui creare un'istanza.

L'operatore new restituisce un riferimento all'oggetto che ha creato. Questo riferimento è solitamente assegnato a una variabile del tipo appropriato, come:

```java
Point originOne = new Point(23, 94);
```
Il riferimento restituito dall'operatore new non deve essere assegnato a una variabile. Può anche essere utilizzato direttamente in un'espressione. Per esempio:
```java
int height = new Rectangle().height;
```

### Inizializzare un oggetto
Ecco il codice per la classe Point:
```java
public class Point {
    public int x = 0;
    public int y = 0;
    **//constructor
    public Point(int a, int b) {
        x = a;
        y = b;
    }**
}
```

Questa classe contiene un singolo costruttore. Puoi riconoscere un costruttore perché la sua dichiarazione usa lo stesso nome della classe e non ha un tipo restituito. Il costruttore nella classe Point accetta due argomenti interi, come dichiarato dal codice (int a, int b). La seguente istruzione fornisce 23 e 94 come valori per quegli argomenti:

```java
Point originOne = new Point(23, 94);
```
Il risultato dell'esecuzione di questa affermazione può essere illustrato nella figura seguente:
![[appunti lmp/immagini/objects-oneRef.gif|center|500]]
Ecco il codice per la classe Rectangle, che contiene quattro costruttori:
```java
public class Rectangle {
    public int width = 0;
    public int height = 0;
    public Point origin;

    // four constructors
    public Rectangle() {
        origin = new Point(0, 0);
    }
    public Rectangle(Point p) {
        origin = p;
    }
    public Rectangle(int w, int h) {
        origin = new Point(0, 0);
        width = w;
        height = h;
    }
    public Rectangle(Point p, int w, int h) {
        origin = p;
        width = w;
        height = h;
    }

    // a method for moving the rectangle
    public void move(int x, int y) {
        origin.x = x;
        origin.y = y;
    }

    // a method for computing the area of the rectangle
    public int getArea() {
        return width * height;
    }
}
```
Ciascun costruttore consente di fornire i valori iniziali per l'origine, la larghezza e l'altezza del rettangolo, utilizzando sia i tipi primitivi che quelli di riferimento. Se una classe ha più costruttori, devono avere firme diverse. Il compilatore Java differenzia i costruttori in base al numero e al tipo degli argomenti. Quando il compilatore Java incontra il codice seguente, sa chiamare il costruttore nella classe Rectangle che richiede un argomento Point seguito da due argomenti interi:
```java
Rectangle rectOne = new Rectangle(originOne, 100, 200);
```
Questo chiama uno dei costruttori di Rectangle che inizializza origin su originOne. Inoltre, il costruttore imposta la larghezza su 100 e l'altezza su 200. Ora ci sono due riferimenti allo stesso oggetto Punto: un oggetto può avere più riferimenti ad esso, come mostrato nella figura seguente:


![[appunti lmp/immagini/objects-multipleRefs.gif|center|500]]

La riga di codice seguente chiama il costruttore Rectangle che richiede due argomenti interi, che forniscono i valori iniziali per larghezza e altezza. Se ispezioni il codice all'interno del costruttore, vedrai che crea un nuovo oggetto Point i cui valori xey sono inizializzati su 0:
```java
Rectangle rectTwo = new Rectangle(50, 100);
```
Il costruttore Rectangle utilizzato nella seguente istruzione non accetta argomenti, quindi è chiamato costruttore senza argomenti:
```java
Rectangle rect = new Rectangle();
```
Tutte le classi hanno almeno un costruttore. Se una classe non ne dichiara alcuna esplicitamente, il compilatore Java fornisce automaticamente un costruttore senza argomenti, chiamato costruttore predefinito. Questo costruttore predefinito chiama il costruttore no-argument del genitore della classe o il costruttore Object se la classe non ha altro genitore. Se il genitore non ha un costruttore (Object ne ha uno), il compilatore rifiuterà il programma.

MANCA PARTE USING OBJECTS E GARBAGE COLLECTOR