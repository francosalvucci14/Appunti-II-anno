# Ritornando a [[Lezione 10#Interfacce ed ereditarietà|Lezione 10 - Interfacce]]

## Interfacce in evoluzione

Considera un'interfaccia che hai sviluppato chiamata DoIt:

```java
public interface DoIt {
   void doSomething(int i, double x);
   int doSomethingElse(String s);
}
```

Supponiamo che, in un secondo momento, vogliate aggiungere un terzo metodo a DoIt, in modo che l'interfaccia diventi ora:

```java
public interface DoIt {

   void doSomething(int i, double x);
   int doSomethingElse(String s);
   boolean didItWork(int i, double x, String s);
   
}
```

Se apporti questa modifica, tutte le classi che implementano la vecchia interfaccia DoIt si interromperanno perché non implementano più la vecchia interfaccia. I programmatori che si affidano a questa interfaccia protesteranno ad alta voce.

Prova ad anticipare tutti gli usi per la tua interfaccia e specificala completamente dall'inizio. Se vuoi aggiungere altri metodi a un'interfaccia, hai diverse opzioni. Potresti creare un'interfaccia DoItPlus che estenda DoIt:

```java
public interface DoItPlus extends DoIt {

   boolean didItWork(int i, double x, String s);
   
}
```

Ora gli utenti del tuo codice possono scegliere di continuare a utilizzare la vecchia interfaccia o eseguire l'upgrade alla nuova interfaccia.

In alternativa, puoi definire i tuoi nuovi metodi come metodi predefiniti. L'esempio seguente definisce un [[Lezione 12#Metodi predefiniti|metodo predefinito]] denominato didItWork:

```java
public interface DoIt {

   void doSomething(int i, double x);
   int doSomethingElse(String s);
   **default boolean didItWork(int i, double x, String s) {
       // Method body 
   }**
   
}
```

Si noti che è necessario fornire un'implementazione per i metodi predefiniti. È inoltre possibile definire nuovi [[Lezione 12#Metodi statici|metodi statici]] per le interfacce esistenti. Gli utenti che dispongono di classi che implementano interfacce migliorate con nuovi metodi predefiniti o statici non devono modificarle o ricompilarle per adattarle ai metodi aggiuntivi.

## Metodi predefiniti

La sezione Interfacce descrive un esempio che coinvolge produttori di auto controllate da computer che pubblicano interfacce standard del settore che descrivono quali metodi possono essere invocati per far funzionare le proprie auto. E se quelle case automobilistiche controllate da computer aggiungessero nuove funzionalità, come il volo, alle loro auto? Questi produttori dovrebbero specificare nuovi metodi per consentire ad altre società (come i produttori di strumenti di guida elettronica) di adattare il loro software alle auto volanti. Dove dichiarerebbero queste case automobilistiche questi nuovi metodi relativi al volo? Se li aggiungono alle loro interfacce originali, i programmatori che hanno implementato tali interfacce dovrebbero riscrivere le loro implementazioni. Se li aggiungono come metodi statici, i programmatori li considererebbero come metodi di utilità, non come metodi di base essenziali.

I metodi predefiniti consentono di aggiungere nuove funzionalità alle interfacce delle librerie e garantiscono la compatibilità binaria con il codice scritto per le versioni precedenti di tali interfacce.

Si consideri la seguente interfaccia, TimeClient:

```java
import java.time.*; 
 
public interface TimeClient {
    void setTime(int hour, int minute, int second);
    void setDate(int day, int month, int year);
    void setDateAndTime(int day, int month, int year,
                               int hour, int minute, int second);
    LocalDateTime getLocalDateTime();
}
```

La seguente classe, SimpleTimeClient, implementa TimeClient:

```java
package defaultmethods;

import java.time.*;
import java.lang.*;
import java.util.*;

public class SimpleTimeClient implements TimeClient {
    
    private LocalDateTime dateAndTime;
    
    public SimpleTimeClient() {
        dateAndTime = LocalDateTime.now();
    }
    
    public void setTime(int hour, int minute, int second) {
        LocalDate currentDate = LocalDate.from(dateAndTime);
        LocalTime timeToSet = LocalTime.of(hour, minute, second);
        dateAndTime = LocalDateTime.of(currentDate, timeToSet);
    }
    
    public void setDate(int day, int month, int year) {
        LocalDate dateToSet = LocalDate.of(day, month, year);
        LocalTime currentTime = LocalTime.from(dateAndTime);
        dateAndTime = LocalDateTime.of(dateToSet, currentTime);
    }
    
    public void setDateAndTime(int day, int month, int year,
                               int hour, int minute, int second) {
        LocalDate dateToSet = LocalDate.of(day, month, year);
        LocalTime timeToSet = LocalTime.of(hour, minute, second); 
        dateAndTime = LocalDateTime.of(dateToSet, timeToSet);
    }
    
    public LocalDateTime getLocalDateTime() {
        return dateAndTime;
    }
    
    public String toString() {
        return dateAndTime.toString();
    }
    
    public static void main(String... args) {
        TimeClient myTimeClient = new SimpleTimeClient();
        System.out.println(myTimeClient.toString());
    }
}
```

Supponiamo di voler aggiungere nuove funzionalità all'interfaccia TimeClient, come la possibilità di specificare un fuso orario tramite un oggetto ZonedDateTime (che è simile a un oggetto LocalDateTime tranne per il fatto che memorizza le informazioni sul fuso orario):

```java
public interface TimeClient {
    void setTime(int hour, int minute, int second);
    void setDate(int day, int month, int year);
    void setDateAndTime(int day, int month, int year,
        int hour, int minute, int second);
    LocalDateTime getLocalDateTime();                           
    **ZonedDateTime getZonedDateTime(String zoneString);**
}
```

Dopo questa modifica all'interfaccia TimeClient, dovresti anche modificare la classe SimpleTimeClient e implementare il metodo getZonedDateTime. Tuttavia, invece di lasciare getZonedDateTime come astratto (come nell'esempio precedente), è invece possibile definire un'implementazione predefinita. (Ricorda che un metodo astratto è un metodo dichiarato senza un'implementazione.)

```java
package defaultmethods;
 
import java.time.*;

public interface TimeClient {
    void setTime(int hour, int minute, int second);
    void setDate(int day, int month, int year);
    void setDateAndTime(int day, int month, int year,
                               int hour, int minute, int second);
    LocalDateTime getLocalDateTime();
    
    static ZoneId getZoneId (String zoneString) {
        try {
            return ZoneId.of(zoneString);
        } catch (DateTimeException e) {
            System.err.println("Invalid time zone: " + zoneString +
                "; using default time zone instead.");
            return ZoneId.systemDefault();
        }
    }
        
    default ZonedDateTime getZonedDateTime(String zoneString) {
        return ZonedDateTime.of(getLocalDateTime(), getZoneId(zoneString));
    }
}
```

Si specifica che una definizione di metodo in un'interfaccia è un metodo predefinito con la parola chiave predefinita all'inizio della firma del metodo. Tutte le dichiarazioni di metodo in un'interfaccia, inclusi i metodi predefiniti, sono implicitamente pubbliche, pertanto è possibile omettere il modificatore public.

Con questa interfaccia, non è necessario modificare la classe SimpleTimeClient, e questa classe (e qualsiasi classe che implementa l'interfaccia TimeClient), avrà il metodo getZonedDateTime già definito. L'esempio seguente, TestSimpleTimeClient, richiama il metodo getZonedDateTime da un'istanza di SimpleTimeClient

```java
package defaultmethods;
 
import java.time.*;
import java.lang.*;
import java.util.*;

public class TestSimpleTimeClient {
    public static void main(String... args) {
        TimeClient myTimeClient = new SimpleTimeClient();
        System.out.println("Current time: " + myTimeClient.toString());
        System.out.println("Time in California: " +
            myTimeClient.getZonedDateTime("Blah blah").toString());
    }
}
```

### Estensione di interfacce che contengono metodi predefiniti

Quando estendi un'interfaccia che contiene un metodo predefinito, puoi eseguire le seguenti operazioni:

- Non menzionare affatto il metodo predefinito, che consente alla tua interfaccia estesa di ereditare il metodo predefinito.
- Ridichiarare il metodo predefinito, che lo rende astratto.
- Ridefinire il metodo predefinito, che lo sovrascrive.

Supponiamo di estendere l'interfaccia TimeClient come segue:

```java
public interface AnotherTimeClient extends TimeClient { }
```

Qualsiasi classe che implementa l'interfaccia AnotherTimeClient avrà l'implementazione specificata dal metodo predefinito TimeClient.getZonedDateTime.

Supponiamo di estendere l'interfaccia TimeClient come segue:

```java
public interface AbstractZoneTimeClient extends TimeClient {
    public ZonedDateTime getZonedDateTime(String zoneString);
}
```

Qualsiasi classe che implementa l'interfaccia AbstractZoneTimeClient dovrà implementare il metodo getZonedDateTime; questo metodo è un metodo astratto come tutti gli altri metodi non predefiniti (e non statici) in un'interfaccia.

Supponiamo di estendere l'interfaccia TimeClient come segue:

```java
public interface HandleInvalidTimeZoneClient extends TimeClient {
    default public ZonedDateTime getZonedDateTime(String zoneString) {
        try {
            return ZonedDateTime.of(getLocalDateTime(),ZoneId.of(zoneString)); 
        } catch (DateTimeException e) {
            System.err.println("Invalid zone ID: " + zoneString +
                "; using the default time zone instead.");
            return ZonedDateTime.of(getLocalDateTime(),ZoneId.systemDefault());
        }
    }
}
```

Qualsiasi classe che implementa l'interfaccia HandleInvalidTimeZoneClient utilizzerà l'implementazione di getZonedDateTime specificata da questa interfaccia invece di quella specificata dall'interfaccia TimeClient.

### Metodi statici

Oltre ai metodi predefiniti, è possibile definire [[Lezione 6#Metodi della classe|metodi statici]] nelle interfacce. (Un metodo statico è un metodo associato alla classe in cui è definito piuttosto che a qualsiasi oggetto. Ogni istanza della classe condivide i suoi metodi statici.) Ciò semplifica l'organizzazione dei metodi di supporto nelle librerie; puoi mantenere metodi statici specifici per un'interfaccia nella stessa interfaccia piuttosto che in una classe separata. L'esempio seguente definisce un metodo statico che recupera un oggetto ZoneId corrispondente a un identificatore di fuso orario; utilizza il fuso orario predefinito del sistema se non esiste alcun oggetto ZoneId corrispondente all'identificatore specificato. (Di conseguenza, puoi semplificare il metodo getZonedDateTime):

```java
public interface TimeClient {
    // ...
    static public ZoneId getZoneId (String zoneString) {
        try {
            return ZoneId.of(zoneString);
        } catch (DateTimeException e) {
            System.err.println("Invalid time zone: " + zoneString +
                "; using default time zone instead.");
            return ZoneId.systemDefault();
        }
    }

    default public ZonedDateTime getZonedDateTime(String zoneString) {
        return ZonedDateTime.of(getLocalDateTime(), getZoneId(zoneString));
    }    
}
```

Analogamente ai metodi statici nelle classi, si specifica che una definizione di metodo in un'interfaccia è un metodo statico con la parola chiave static all'inizio della firma del metodo. Tutte le dichiarazioni di metodo in un'interfaccia, inclusi i metodi statici, sono implicitamente pubbliche, pertanto è possibile omettere il modificatore public.

# Ereditarietà

>[!important]- Definizione
>Una classe derivata da un'altra classe è chiamata sottoclasse (anche classe derivata, classe estesa o classe figlia). La classe da cui deriva la sottoclasse è chiamata superclasse (anche classe base o classe genitore).
>Ad eccezione di Object, che non ha superclasse, ogni classe ha una e una sola superclasse diretta (eredità singola). In assenza di qualsiasi altra superclasse esplicita, ogni classe è implicitamente una sottoclasse di Object.
>Le classi possono essere derivate da classi derivate da classi derivate da classi e così via, e infine derivate dalla classe più in alto, Object. Si dice che una tale classe discenda da tutte le classi nella catena di ereditarietà che risale a Object.

L'idea dell'ereditarietà è semplice ma potente: quando vuoi creare una nuova classe ed esiste già una classe che include parte del codice che desideri, puoi derivare la tua nuova classe dalla classe esistente. In questo modo, puoi riutilizzare i campi ei metodi della classe esistente senza doverli scrivere (ed eseguire il debug!) da soli.

Una sottoclasse eredita tutti i membri (campi, metodi e classi nidificate) dalla sua superclasse. I costruttori non sono membri, quindi non vengono ereditati dalle sottoclassi, ma il costruttore della superclasse può essere richiamato dalla sottoclasse.

## Ereditarietà multipla di stato, implementazione e tipo

Una differenza significativa tra classi e interfacce è che le classi possono avere campi mentre le interfacce no. Inoltre, puoi istanziare una classe per creare un oggetto, cosa che non puoi fare con le interfacce. Come spiegato nella sezione Cos'è un oggetto?, un oggetto memorizza il suo stato in campi, che sono definiti in classi. Uno dei motivi per cui il linguaggio di programmazione Java non consente di estendere più di una classe è evitare i problemi di ereditarietà multipla dello stato, ovvero la possibilità di ereditare campi da più classi. Si supponga, ad esempio, di poter definire una nuova classe che estenda più classi. Quando crei un oggetto istanziando quella classe, quell'oggetto erediterà i campi da tutte le superclassi della classe. Cosa succede se metodi o costruttori di diverse superclassi istanziano lo stesso campo? Quale metodo o costruttore avrà la precedenza? Poiché le interfacce non contengono campi, non è necessario preoccuparsi dei problemi derivanti dall'ereditarietà multipla dello stato.

L'ereditarietà multipla dell'implementazione è la capacità di ereditare le definizioni dei metodi da più classi. I problemi sorgono con questo tipo di ereditarietà multipla, come i conflitti di nome e l'ambiguità. Quando i compilatori di linguaggi di programmazione che supportano questo tipo di ereditarietà multipla incontrano superclassi che contengono metodi con lo stesso nome, a volte non sono in grado di determinare a quale membro o metodo accedere o richiamare. Inoltre, un programmatore può involontariamente introdurre un conflitto di nomi aggiungendo un nuovo metodo a una superclasse. I metodi predefiniti introducono una forma di ereditarietà multipla dell'implementazione. Una classe può implementare più di un'interfaccia, che può contenere metodi predefiniti con lo stesso nome. Il compilatore Java fornisce alcune regole per determinare quale metodo predefinito utilizza una particolare classe.

Il linguaggio di programmazione Java supporta l'ereditarietà multipla del tipo, ovvero la capacità di una classe di implementare più di un'interfaccia. Un oggetto può avere più tipi: il tipo della propria classe ei tipi di tutte le interfacce implementate dalla classe. Ciò significa che se una variabile viene dichiarata essere il tipo di un'interfaccia, il suo valore può fare riferimento a qualsiasi oggetto istanziato da qualsiasi classe che implementa l'interfaccia. Questo è discusso nella sezione Utilizzo di un'interfaccia come tipo.

Come per l'ereditarietà multipla dell'implementazione, una classe può ereditare diverse implementazioni di un metodo definito (come predefinito o statico) nelle interfacce che estende. In questo caso, il compilatore o l'utente deve decidere quale utilizzare.

## Scrivere classi e metodi finali

Puoi dichiarare alcuni o tutti i metodi di una classe final. Si utilizza la parola chiave final in una dichiarazione di metodo per indicare che il metodo non può essere sovrascritto dalle sottoclassi. La classe Object fa questo: molti dei suoi metodi sono definitivi.

Potresti voler rendere definitivo un metodo se ha un'implementazione che non deve essere modificata ed è fondamentale per lo stato coerente dell'oggetto. Ad esempio, potresti voler rendere finale il metodo getFirstPlayer in questa classe ChessAlgorithm:

```java
class ChessAlgorithm {
    enum ChessPlayer { WHITE, BLACK }
    ...
    **final** ChessPlayer getFirstPlayer() {
        return ChessPlayer.WHITE;
    }
    ...
}
```

I metodi chiamati dai costruttori dovrebbero generalmente essere dichiarati final. Se un costruttore chiama un metodo non finale, una sottoclasse può ridefinire quel metodo con risultati sorprendenti o indesiderati.

Nota che puoi anche dichiarare finale un'intera classe. Una classe dichiarata final non può essere sottoclasse. Ciò è particolarmente utile, ad esempio, quando si crea una classe immutabile come la classe String.

