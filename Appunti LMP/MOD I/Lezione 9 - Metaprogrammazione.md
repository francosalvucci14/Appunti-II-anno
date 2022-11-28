# Annotazioni

Le annotazioni, una forma di metadati, forniscono dati su un programma che non fa parte del programma stesso. Le annotazioni non hanno alcun effetto diretto sul funzionamento del codice che annotano.

Le annotazioni hanno una serie di usi, tra cui:

- **Informazioni per il compilatore**: le annotazioni possono essere utilizzate dal compilatore per rilevare errori o sopprimere avvisi.
- **Elaborazione in fase di compilazione e distribuzione**: gli strumenti software possono elaborare le informazioni di annotazione per generare codice, file XML e così via.
- **Elaborazione in fase di esecuzione**: alcune annotazioni sono disponibili per essere esaminate in fase di esecuzione.

Questa lezione spiega dove è possibile utilizzare le annotazioni, come applicare le annotazioni, quali tipi di annotazioni predefiniti sono disponibili nella piattaforma Java, Standard Edition (API Java SE), in che modo le annotazioni di tipo possono essere utilizzate insieme a sistemi di tipi collegabili per scrivere codice con maggiore controllo del tipo e come implementare le annotazioni ripetute.

## Nozioni di base sulle annotazioni

### Formato di un annotazione
Nella sua forma più semplice, un'annotazione ha il seguente aspetto:
```java
@Entity
```

Il carattere di chiocciola (@) indica al compilatore che ciò che segue è un'annotazione. Nell'esempio seguente, il nome dell'annotazione è Override:
```java
@Override
void mySuperMetod() { ... }
```

L'annotazione può includere elementi, che possono essere nominati o senza nome, e ci sono valori per questi elementi:

```java
@Author(
   name = "Benjamin Franklin",
   date = "3/27/2003"
)
class MyClass { ... }
```

Oppure:
```java
@SuppressWarnings(value = "unchecked")
void myMethod() { ... }
```

Se c'è un solo elemento denominato valore, allora il nome può essere omesso, come in:
```java
@SuppressWarnings("unchecked")
void myMetod() { ... }
```

Se l'annotazione non ha elementi, le parentesi possono essere omesse, come mostrato nell'esempio precedente di @Override.

È anche possibile utilizzare più annotazioni sulla stessa dichiarazione:
```java
@Author(name = "Jane Doe")
@EBook
class MyClass { ... }
```

Se le annotazioni hanno lo stesso tipo, si parla di annotazione ripetuta:
```java
@Author(name = "Jane Doe")
@Author(name = "John Smith")
class MyClass { ... }
```

Il tipo di annotazione può essere uno dei tipi definiti nei pacchetti java.lang o java.lang.annotation dell'API Java SE. Negli esempi precedenti, Override e SuppressWarnings sono annotazioni Java predefinite. È anche possibile definire il proprio tipo di annotazione. Le annotazioni Autore ed Ebook nell'esempio precedente sono tipi di annotazione personalizzati.

### Dove possono essere utilizzate le annotazioni

Le annotazioni possono essere applicate alle dichiarazioni: dichiarazioni di classi, campi, metodi e altri elementi del programma. Quando viene utilizzata su una dichiarazione, ogni annotazione appare spesso, per convenzione, su una propria riga.

A partire dalla versione Java SE 8, le annotazioni possono essere applicate anche all'uso dei tipi. Ecco alcuni esempi:

- Espressione di creazione dell'istanza di classe:
```java
new @Interned MyObject();
```
- Tipo cast:
```java
```miaStringa = (@StringaNonNull) str;
```
- clausola _implements_:
```java
class UnmodifiableList<T> implements
    @Readonly List<@Readonly T> { ... }
```
- Dichiarazione di eccezione generata:
```java
void monitorTemperature() lancia
    @Critical TemperatureException { ... }
```

Questa forma di annotazione è chiamata annotazione di tipo (_type annotation_).

## Dichiarare un tipo di annotazione


