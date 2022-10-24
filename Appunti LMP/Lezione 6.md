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

## Dichiarare variabili
Esistono diversi tipi di variabili:
- Variabili membro in una classe: queste sono chiamate campi.
- Variabili in un metodo o blocco di codice: queste sono chiamate variabili locali.
- Variabili nelle dichiarazioni di metodo: queste sono chiamate parametri.

Le dichiarazioni di campo sono composte da tre componenti, nell'ordine:
- Zero o più modificatori, come public o private.
- Il tipo del campo.
- Il nome del campo.

## Accedere ai modificatori

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

## Tipi
Tutte le variabili devono avere un tipo. Puoi usare tipi primitivi come int, float, boolean, ecc. Oppure puoi usare tipi di riferimento, come stringhe, array o oggetti.
## Nomi delle variabili
Tutte le variabili, siano esse campi, variabili locali o parametri, seguono le stesse regole e convenzioni di denominazione trattate nella lezione Nozioni di base sul linguaggio, Variabili - Denominazione.

In questa lezione, tieni presente che le stesse regole e convenzioni di denominazione vengono utilizzate per i nomi dei metodi e delle classi, tranne quello
- la prima lettera del nome di una classe dovrebbe essere in maiuscolo, e
- la prima (o l'unica) parola nel nome di un metodo dovrebbe essere un verbo.

