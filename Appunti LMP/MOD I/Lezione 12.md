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

### Metodi statici
