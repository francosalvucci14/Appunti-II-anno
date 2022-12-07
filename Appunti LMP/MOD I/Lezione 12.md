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



### Metodi statici
