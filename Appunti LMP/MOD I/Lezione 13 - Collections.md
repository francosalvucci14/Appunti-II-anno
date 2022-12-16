# Collections

Una colelctions, a volte chiamata container, è semplicemente un oggetto che raggruppa più elementi in una singola unità. Le raccolte vengono utilizzate per archiviare, recuperare, manipolare e comunicare dati aggregati. In genere, rappresentano elementi di dati che formano un gruppo naturale, come una mano di poker (una raccolta di carte), una cartella di posta (una raccolta di lettere) o un elenco telefonico (una mappatura di nomi su numeri di telefono). Se hai utilizzato il linguaggio di programmazione Java, o qualsiasi altro linguaggio di programmazione, hai già familiarità con le raccolte.

## Che cos'è un framework di collections?

Un framework di raccolte è un'architettura unificata per rappresentare e manipolare le raccolte. Tutti i framework delle raccolte contengono quanto segue:

- **Interfacce**: si tratta di tipi di dati astratti che rappresentano raccolte. Le interfacce consentono di manipolare le collezioni indipendentemente dai dettagli della loro rappresentazione. Nei linguaggi orientati agli oggetti, le interfacce generalmente formano una gerarchia.
- **Implementazioni**: Queste sono le implementazioni concrete delle interfacce di raccolta. In sostanza, sono strutture dati riutilizzabili.
- **Algoritmi**: questi sono i metodi che eseguono calcoli utili, come la ricerca e l'ordinamento, su oggetti che implementano le interfacce di raccolta. Si dice che gli algoritmi siano polimorfici: ovvero, lo stesso metodo può essere utilizzato su molte diverse implementazioni dell'interfaccia di raccolta appropriata. In sostanza, gli algoritmi sono funzionalità riutilizzabili.

## Vantaggi di Java Collections Framework

Il Java Collections Framework offre i seguenti vantaggi:

- **Riduce lo sforzo di programmazione**: fornendo utili strutture di dati e algoritmi, Collections Framework ti consente di concentrarti sulle parti importanti del tuo programma piuttosto che sulle "idrauliche" di basso livello necessarie per farlo funzionare. Facilitando l'interoperabilità tra API non correlate, Java Collections Framework ti libera dalla scrittura di oggetti adattatore o codice di conversione per connettere le API.
- **Aumenta la velocità e la qualità del programma**: questo framework di raccolte fornisce implementazioni ad alte prestazioni e di alta qualità di utili strutture di dati e algoritmi. Le varie implementazioni di ciascuna interfaccia sono intercambiabili, quindi i programmi possono essere facilmente ottimizzati cambiando le implementazioni della raccolta. Poiché sei liberato dalla fatica di scrivere le tue strutture di dati, avrai più tempo da dedicare al miglioramento della qualità e delle prestazioni dei programmi.
- **Consente l'interoperabilità tra API non correlate**: le interfacce di raccolta sono il vernacolo con cui le API passano le raccolte avanti e indietro. Se la mia API di amministrazione di rete fornisce una raccolta di nomi di nodi e se il tuo toolkit GUI prevede una raccolta di intestazioni di colonna, le nostre API interagiranno senza problemi, anche se sono state scritte in modo indipendente.
- **Riduce lo sforzo per apprendere e utilizzare nuove API**: molte API accettano naturalmente raccolte in input e le forniscono come output. In passato, ciascuna di queste API aveva una piccola API secondaria dedicata alla manipolazione delle sue raccolte. C'era poca coerenza tra queste sotto-API di raccolte ad hoc, quindi dovevi imparare ognuna da zero ed era facile commettere errori quando le utilizzavi. Con l'avvento delle interfacce di raccolta standard, il problema è scomparso.
- **Riduce lo sforzo per progettare nuove API**: questo è il rovescio della medaglia del vantaggio precedente. I progettisti e gli implementatori non devono reinventare la ruota ogni volta che creano un'API che si basa su raccolte; invece, possono utilizzare interfacce di raccolta standard.
- **Favorisce il riutilizzo del software**: le nuove strutture di dati conformi alle interfacce di raccolta standard sono per natura riutilizzabili. Lo stesso vale per i nuovi algoritmi che operano su oggetti che implementano queste interfacce.

### Interfaces

Le _core collection interfaces_ incapsulano diversi tipi di raccolte, mostrati nella figura seguente. Queste interfacce consentono di manipolare le raccolte indipendentemente dai dettagli della loro rappresentazione. Le interfacce di raccolta principali sono la base di Java Collections Framework. Come puoi vedere nella figura seguente, le interfacce della raccolta principale formano una gerarchia.

![[appunti lmp/mod i/immagini/colls-coreInterfaces.gif|center]]

Un Set è un tipo speciale di Collection, un SortedSet è un tipo speciale di Set e così via. Si noti inoltre che la gerarchia è composta da due alberi distinti: una Map non è una vera raccolta.

Si noti che tutte le interfacce della raccolta principale sono generiche. Ad esempio, questa è la dichiarazione dell'interfaccia Collection.

```java
public interface Collection<E>...
```

La sintassi `<E>` indica che l'interfaccia è generica. Quando dichiari un'istanza Collection puoi e dovresti specificare il tipo di oggetto contenuto nella collection. La specifica del tipo consente al compilatore di verificare (in fase di compilazione) che il tipo di oggetto inserito nella raccolta sia corretto, riducendo così gli errori in fase di esecuzione.

Per mantenere gestibile il numero di interfacce di raccolta principali, la piattaforma Java non fornisce interfacce separate per ogni variante di ciascun tipo di raccolta. (Tali varianti potrebbero includere immutabili, di dimensioni fisse e di sola aggiunta.) Invece, le operazioni di modifica in ciascuna interfaccia sono designate come facoltative: una data implementazione può scegliere di non supportare tutte le operazioni. Se viene richiamata un'operazione non supportata, una raccolta genera un'eccezione UnsupportedOperationException. Le implementazioni sono responsabili della documentazione delle operazioni facoltative che supportano. Tutte le implementazioni generiche della piattaforma Java supportano tutte le operazioni facoltative.

L'elenco seguente descrive le interfacce principali della raccolta:
- **Raccolta (Collection)**: la radice della gerarchia della raccolta. Una raccolta rappresenta un gruppo di oggetti noti come i suoi elementi. L'interfaccia Collection è il minimo comune denominatore implementato da tutte le raccolte e viene utilizzata per passare raccolte e manipolarle quando si desidera la massima generalità. Alcuni tipi di raccolte consentono elementi duplicati e altri no. Alcuni sono ordinati e altri non sono ordinati. La piattaforma Java non fornisce implementazioni dirette di questa interfaccia ma fornisce implementazioni di sottointerfacce più specifiche, come Set e List. Vedi anche la sezione [[Lezione 13 - Collections#Raccolta (Collection)|Raccolta (Collection)]] 
- **Set**: una raccolta che non può contenere elementi duplicati. Questa interfaccia modella l'astrazione dell'insieme matematico e viene utilizzata per rappresentare insiemi, come le carte che compongono una mano di poker, i corsi che costituiscono il programma di uno studente oi processi in esecuzione su una macchina. Vedi anche la sezione Set Interface.
- **Lista**: una raccolta ordinata (a volte chiamata sequenza). Gli elenchi possono contenere elementi duplicati. L'utente di una lista generalmente ha un controllo preciso su dove è inserito ogni elemento nella lista e può accedere agli elementi tramite il loro indice intero (posizione). Se hai utilizzato Vector, hai familiarità con il sapore generale di List. Vedi anche la sezione L'interfaccia della lista.
- **Coda**: una raccolta utilizzata per contenere più elementi prima dell'elaborazione. Oltre alle operazioni di raccolta di base, una coda fornisce ulteriori operazioni di inserimento, estrazione e ispezione.Le code in genere, ma non necessariamente, ordinano gli elementi in un modo FIFO (first-in, first-out). Tra le eccezioni vi sono le code di priorità, che ordinano gli elementi in base a un comparatore fornito o all'ordinamento naturale degli elementi. Qualunque sia l'ordinamento utilizzato, l'inizio della coda è l'elemento che verrebbe rimosso da una chiamata a remove o poll. In una coda FIFO, tutti i nuovi elementi vengono inseriti in coda alla coda. Altri tipi di code possono utilizzare regole di posizionamento differenti. Ogni implementazione di Queue deve specificare le proprie proprietà di ordinamento. Vedere anche la sezione L'interfaccia della coda.
- **Deque**: una raccolta utilizzata per contenere più elementi prima dell'elaborazione. Oltre alle operazioni di raccolta di base, una Deque fornisce ulteriori operazioni di inserimento, estrazione e ispezione.Deques può essere utilizzato sia come FIFO (first-in, first-out) che LIFO (last-in, first-out). In una deque tutti i nuovi elementi possono essere inseriti, recuperati e rimossi alle due estremità. Vedi anche la sezione L'interfaccia Deque.
- **Mappa**: un oggetto che mappa le chiavi ai valori. Una mappa non può contenere chiavi duplicate; ogni chiave può mappare al massimo un valore. Se hai utilizzato Hashtable, hai già familiarità con le basi di Map. Vedi anche la sezione L'interfaccia della mappa.

Le ultime due interfacce di raccolta principali sono semplicemente versioni ordinate di Set e Map:
- **SortedSet** — un Set che mantiene i suoi elementi in ordine crescente. Diverse operazioni aggiuntive sono fornite per sfruttare l'ordine. Gli insiemi ordinati vengono utilizzati per insiemi ordinati in modo naturale, come elenchi di parole e elenchi di appartenenza.
- **SortedMap**: una mappa che mantiene le proprie mappature in ordine di chiave crescente. Questo è l'analogo Mappa di SortedSet. Le mappe ordinate vengono utilizzate per raccolte ordinate in modo naturale di coppie chiave/valore, come dizionari ed elenchi telefonici.


#### Raccolta (Collection)

Una Collection rappresenta un gruppo di oggetti noti come i suoi elementi. L'interfaccia Collection viene utilizzata per passare raccolte di oggetti in cui si desidera la massima generalità. Ad esempio, per convenzione tutte le implementazioni di collection generiche hanno un costruttore che accetta un argomento Collection. Questo costruttore, noto come costruttore di conversione, inizializza la nuova raccolta per contenere tutti gli elementi nella raccolta specificata, indipendentemente dalla sottointerfaccia o dal tipo di implementazione della raccolta specificata. In altre parole, permette di convertire il tipo della collezione.

Supponiamo, ad esempio, di avere una `Collection<String>` c, che può essere una List, una Set o un altro tipo di Collection. Questo idioma crea un nuovo ArrayList (un'implementazione dell'interfaccia List), contenente inizialmente tutti gli elementi in c.

```java
List<String> list = new ArrayList<String>(c);
```

L'interfaccia Collection contiene metodi che eseguono operazioni di base, come int size(), boolean isEmpty(), boolean contains(Object element), boolean add(E element), boolean remove(Object element) e `Iterator<E> iterator( )`.

Contiene anche metodi che operano su intere raccolte, come boolean `containsAll(Collection<?> c)`, `boolean addAll(Collection<? extends E> c)`, boolean `removeAll(Collection<?> c)`, boolean `retainAll(Collection<? > c)` e void clear().

Esistono anche metodi aggiuntivi per le operazioni sugli array (come `Object[] toArray()` e `<T> T[] toArray(T[] a)`.

L'interfaccia Collection fa ciò che ti aspetteresti dato che una Collection rappresenta un gruppo di oggetti. Ha metodi che ti dicono quanti elementi ci sono nella collezione (size, isEmpty), metodi che controllano se un dato oggetto è nella collezione (contiene), metodi che aggiungono e rimuovono un elemento dalla collezione (aggiungi, rimuovi), e metodi che forniscono un iteratore sulla raccolta (iteratore).

Il metodo add è definito in modo abbastanza generale da avere senso per le raccolte che consentono i duplicati e per quelle che non lo consentono. Garantisce che la Collection conterrà l'elemento specificato dopo il completamento della chiamata e restituisce true se la Collection cambia in seguito alla chiamata. Allo stesso modo, il metodo remove è progettato per rimuovere una singola istanza dell'elemento specificato dalla Collection, supponendo che contenga l'elemento con cui iniziare, e per restituire true se la Collection è stata modificata di conseguenza.

##### Collezioni di attraversamento

Esistono tre modi per attraversare le raccolte: (1) utilizzando operazioni di aggregazione (2) con il costrutto for-each e (3) utilizzando gli iteratori.

###### Operazioni aggregate

In JDK 8 e versioni successive, il metodo preferito di iterazione su una raccolta consiste nell'ottenere un flusso ed eseguire operazioni di aggregazione su di esso. Le operazioni di aggregazione vengono spesso utilizzate insieme alle espressioni lambda per rendere la programmazione più espressiva, utilizzando meno righe di codice. Il codice seguente scorre in sequenza una raccolta di forme e stampa gli oggetti rossi:

```java
myShapesCollection.stream()
.filter(e -> e.getColor() == Color.RED)
.forEach(e -> System.out.println(e.getName()));
```

Allo stesso modo, potresti facilmente richiedere un flusso parallelo, che potrebbe avere senso se la raccolta è abbastanza grande e il tuo computer ha abbastanza core:

```java
myShapesCollection.parallelStream()
.filter(e -> e.getColor() == Color.RED)
.forEach(e -> System.out.println(e.getName()));
```

Esistono molti modi diversi per raccogliere dati con questa API. Ad esempio, potresti voler convertire gli elementi di una Collection in oggetti String, quindi unirli, separati da virgole:

```java
String joined = elements.stream()
    .map(Object::toString)
    .collect(Collectors.joining(", "));
```

O forse sommare gli stipendi di tutti i dipendenti:

```java
int total = employees.stream()
.collect(Collectors.summingInt(Employee::getSalary)));
```

Questi sono solo alcuni esempi di ciò che puoi fare con i flussi e le operazioni di aggregazione. Per ulteriori informazioni ed esempi, vedere la lezione intitolata Operazioni di aggregazione.

Il framework Collections ha sempre fornito una serie di cosiddette "operazioni di massa" come parte della sua API. Questi includono metodi che operano su intere raccolte, come containsAll, addAll, removeAll, ecc. Non confondere questi metodi con le operazioni di aggregazione introdotte in JDK 8. La differenza fondamentale tra le nuove operazioni di aggregazione e le operazioni di massa esistenti (containsAll , addAll, ecc.) è che le vecchie versioni sono tutte mutative, nel senso che modificano tutte la raccolta sottostante. Al contrario, le nuove operazioni di aggregazione non modificano la raccolta sottostante. Quando si utilizzano le nuove operazioni di aggregazione e le espressioni lambda, è necessario fare attenzione a evitare la mutazione in modo da non introdurre problemi in futuro, nel caso in cui il codice venga eseguito successivamente da un flusso parallelo.

###### Costrutto for-each

Il costrutto for-each consente di attraversare in modo conciso una raccolta o un array utilizzando un ciclo for — vedere L'istruzione for. Il codice seguente utilizza il costrutto for-each per stampare ogni elemento di una raccolta su una riga separata.

```java
for (Oggetto o : collection)
    System.out.println(o);
```

###### Itaratori

Un Iterator è un oggetto che consente di attraversare una raccolta e di rimuovere gli elementi dalla raccolta in modo selettivo, se lo si desidera. Ottieni un iteratore per una raccolta chiamando il suo metodo iteratore. Quella che segue è l'interfaccia di Iterator.

```java
public interface Iterator<E> {
    boolean hasNext();
    E next();
    void remove(); //optional
}
```

Il metodo hasNext restituisce true se l'iterazione ha più elementi e il metodo next restituisce l'elemento successivo nell'iterazione. Il metodo remove rimuove l'ultimo elemento restituito da next dalla Collection sottostante. Il metodo remove può essere chiamato solo una volta per chiamata a next e genera un'eccezione se questa regola viene violata.

Si noti che Iterator.remove è l'unico modo sicuro per modificare una raccolta durante l'iterazione; il comportamento non è specificato se la raccolta sottostante viene modificata in qualsiasi altro modo mentre l'iterazione è in corso.

Usa Iterator invece del costrutto for-each quando devi:

- Rimuovi l'elemento corrente. Il costrutto for-each nasconde l'iteratore, quindi non puoi chiamare remove. Pertanto, il costrutto for-each non è utilizzabile per il filtraggio.
- Itera su più raccolte in parallelo.

Il metodo seguente mostra come utilizzare un iteratore per filtrare una raccolta arbitraria, ovvero attraversare la raccolta rimuovendo elementi specifici.

```java
static void filter(Collection<?> c) {
    for (Iterator<?> it = c.iterator(); it.hasNext(); )
        if (!cond(it.next()))
            it.remove();
}
```

##### Operazioni di bulk dell'interfaccia di raccolta

Le operazioni di bulk eseguono un'operazione su un'intera raccolta. È possibile implementare queste operazioni abbreviate utilizzando le operazioni di base, sebbene nella maggior parte dei casi tali implementazioni sarebbero meno efficienti. Di seguito sono riportate le operazioni di massa:

- containsAll — restituisce true se la Collection di destinazione contiene tutti gli elementi nella Collection specificata.
- addAll — aggiunge tutti gli elementi nella Collection specificata alla Collection di destinazione.
- removeAll — rimuove dalla Collection di destinazione tutti i suoi elementi che sono contenuti anche nella Collection specificata.
- retainAll — rimuove dalla Collection di destinazione tutti i suoi elementi che non sono contenuti anche nella Collection specificata. Ovvero, conserva solo quegli elementi nella Collection di destinazione che sono contenuti anche nella Collection specificata.
- clear — rimuove tutti gli elementi dalla Collection.

I metodi addAll, removeAll e retainAll restituiscono tutti true se la Collection di destinazione è stata modificata durante il processo di esecuzione dell'operazione.

Come semplice esempio della potenza delle operazioni di massa, si consideri il seguente idioma per rimuovere tutte le istanze di un elemento specificato, e, da una Collection, c.

```java
c.removeAll(Collections.singleton(e));
```

Più specificamente, supponiamo di voler rimuovere tutti gli elementi nulli da una Collection.

```java
c.removeAll(Collections.singleton(null));
```

Questo idioma usa Collections.singleton, che è un metodo factory statico che restituisce un Set immutabile contenente solo l'elemento specificato.

##### Operazioni sugli array dell'interfaccia di raccolta

I metodi toArray vengono forniti come ponte tra raccolte e API meno recenti che prevedono matrici in input. Le operazioni sugli array consentono di tradurre il contenuto di una Collection in un array. La forma semplice senza argomenti crea un nuovo array di Object. La forma più complessa consente al chiamante di fornire un array o di scegliere il tipo di runtime dell'array di output.

Ad esempio, supponiamo che c sia una raccolta. Il seguente frammento scarica il contenuto di c in un array di Object appena allocato la cui lunghezza è identica al numero di elementi in c.

```java
Object[] a = c.toArray();
```

Supponiamo che c sia noto per contenere solo stringhe (forse perché c è di tipo `Collection<String>`). Il seguente frammento scarica il contenuto di c in un array di String appena allocato la cui lunghezza è identica al numero di elementi in c.

```java
String[] a = c.toArray(new String[0]);
```

#### Set

Un Set è una Collezione che non può contenere elementi duplicati. Modella l'astrazione dell'insieme matematico. L'interfaccia Set contiene solo metodi ereditati da Collection e aggiunge la restrizione che gli elementi duplicati sono proibiti. Set aggiunge anche un contratto più forte sul comportamento delle operazioni equals e hashCode, consentendo alle istanze di Set di essere confrontate in modo significativo anche se i loro tipi di implementazione differiscono. Due istanze di Set sono uguali se contengono gli stessi elementi.

La piattaforma Java contiene tre implementazioni Set generiche: HashSet, TreeSet e LinkedHashSet. HashSet, che memorizza i suoi elementi in una tabella hash, è l'implementazione con le migliori prestazioni; tuttavia non fornisce alcuna garanzia in merito all'ordine di iterazione. TreeSet, che memorizza i suoi elementi in un albero rosso-nero, ordina i suoi elementi in base ai loro valori; è sostanzialmente più lento di HashSet. LinkedHashSet, che è implementato come una tabella hash con un elenco collegato che lo attraversa, ordina i suoi elementi in base all'ordine in cui sono stati inseriti nel set (ordine di inserimento). LinkedHashSet risparmia i suoi clienti dall'ordinamento non specificato e generalmente caotico fornito da HashSet a un costo solo leggermente superiore.

Ecco un semplice ma utile linguaggio Set. Supponiamo di avere una Collection, c, e di voler creare un'altra Collection contenente gli stessi elementi ma con tutti i duplicati eliminati. La seguente battuta fa il trucco.

```java
Collection<Type> noDups = new HashSet<Type>(c);
```

Funziona creando un Set (che, per definizione, non può contenere duplicati), contenente inizialmente tutti gli elementi in c. Usa il costruttore di conversione standard descritto nella sezione The Collection Interface.

Oppure, se utilizzi JDK 8 o versioni successive, puoi facilmente raccogliere in un set utilizzando operazioni di aggregazione:

```java
c.stream()
.collect(Collectors.toSet()); // no duplicates
```

Ecco un esempio leggermente più lungo che accumula una raccolta di nomi in un TreeSet:

```java
Set<String> set = people.stream()
.map(Person::getName)
.collect(Collectors.toCollection(TreeSet::new));
```

E la seguente è una variante minore del primo idioma che conserva l'ordine della raccolta originale rimuovendo gli elementi duplicati:

```java
Collection<Type> noDups = new LinkedHashSet<Type>(c);
```

Il seguente è un metodo generico che incapsula l'idioma precedente, restituendo un Set dello stesso tipo generico di quello passato.

```java
public static <E> Set<E> removeDups(Collection<E> c) {
    return new LinkedHashSet<E>(c);
}
```

##### Operazioni di base dell'interfaccia Set

L'operazione size restituisce il numero di elementi nell'insieme (la sua cardinalità). Il metodo isEmpty fa esattamente quello che pensi che farebbe. Il metodo add aggiunge l'elemento specificato al Set se non è già presente e restituisce un valore booleano che indica se l'elemento è stato aggiunto. Allo stesso modo, il metodo remove rimuove l'elemento specificato dal Set se è presente e restituisce un valore booleano che indica se l'elemento era presente. Il metodo iteratore restituisce un iteratore sul set.

Il seguente programma stampa tutte le parole distinte nella sua lista di argomenti. Sono fornite due versioni di questo programma. Il primo utilizza operazioni di aggregazione JDK 8. Il secondo usa il costrutto for-each.

Utilizzo delle operazioni di aggregazione JDK 8:

```java
import java.util.*;
import java.util.stream.*;

public class FindDups {
    public static void main(String[] args) {
        Set<String> distinctWords = Arrays.asList(args).stream()
		.collect(Collectors.toSet()); 
        System.out.println(distinctWords.size()+ 
                           " distinct words: " + 
                           distinctWords);
    }
}
```

Usando il costrutto for-each:

```java
import java.util.*;

public class FindDups {
    public static void main(String[] args) {
        Set<String> s = new HashSet<String>();
        for (String a : args)
               s.add(a);
        System.out.println(s.size() + " distinct words: " + s);
    }
}
```

Si noti che il codice fa sempre riferimento alla Collection in base al tipo di interfaccia (Set) anziché al tipo di implementazione. Questa è una pratica di programmazione fortemente consigliata perché offre la flessibilità di modificare le implementazioni semplicemente modificando il costruttore. Se una delle variabili utilizzate per archiviare una raccolta o i parametri utilizzati per passarla in giro sono dichiarati essere del tipo di implementazione della raccolta piuttosto che del suo tipo di interfaccia, tutte queste variabili e parametri devono essere modificati per modificare il tipo di implementazione.

Inoltre, non vi è alcuna garanzia che il programma risultante funzioni. Se il programma utilizza operazioni non standard presenti nel tipo di implementazione originale ma non in quello nuovo, il programma fallirà. Fare riferimento alle raccolte solo tramite la loro interfaccia impedisce di utilizzare qualsiasi operazione non standard.

Il tipo di implementazione del Set nell'esempio precedente è HashSet, che non garantisce l'ordine degli elementi nel Set. Se vuoi che il programma stampi l'elenco delle parole in ordine alfabetico, cambia semplicemente il tipo di implementazione del Set da HashSet a TreeSet. Apportando questa banale modifica di una riga, la riga di comando nell'esempio precedente genera il seguente output.

##### Operazioni di bulk dell'interfaccia Set

Le operazioni di massa sono particolarmente adatte ai set; quando applicati, eseguono operazioni insiemistiche standard. Supponiamo che s1 e s2 siano insiemi. Ecco cosa fanno le operazioni in blocco:

- s1.containsAll(s2) — restituisce vero se s2 è un sottoinsieme di s1. (s2 è un sottoinsieme di s1 se l'insieme s1 contiene tutti gli elementi di s2.)
- s1.addAll(s2) — trasforma s1 nell'unione di s1 e s2. (L'unione di due insiemi è l'insieme che contiene tutti gli elementi contenuti in entrambi gli insiemi.)
- s1.retainAll(s2) — trasforma s1 nell'intersezione di s1 e s2. (L'intersezione di due insiemi è l'insieme contenente solo gli elementi comuni a entrambi gli insiemi.)
- s1.removeAll(s2) — trasforma s1 nella differenza insiemi (asimmetrica) di s1 e s2. (Ad esempio, la differenza insiemistica di s1 meno s2 è l'insieme contenente tutti gli elementi trovati in s1 ma non in s2.)

Per calcolare l'unione, l'intersezione o la differenza di insiemi di due insiemi in modo non distruttivo (senza modificare nessuno degli insiemi), il chiamante deve copiare un insieme prima di chiamare l'operazione di massa appropriata. I seguenti sono gli idiomi risultanti.

```java
Set<Type> union = new HashSet<Type>(s1);
union.addAll(s2);

Set<Type> intersection = new HashSet<Type>(s1);
intersection.retainAll(s2);

Set<Type> difference = new HashSet<Type>(s1);
difference.removeAll(s2);
```

Il tipo di implementazione del set di risultati negli idiomi precedenti è HashSet, che è, come già accennato, la migliore implementazione completa di Set nella piattaforma Java. Tuttavia, qualsiasi implementazione Set generica potrebbe essere sostituita.

Rivisitiamo il programma FindDups. Si supponga di voler sapere quali parole nell'elenco degli argomenti ricorrono solo una volta e quali ricorrono più di una volta, ma non si desidera che i duplicati vengano stampati ripetutamente. Questo effetto può essere ottenuto generando due insiemi: uno contenente ogni parola nell'elenco degli argomenti e l'altro contenente solo i duplicati. Le parole che ricorrono una sola volta sono la differenza insiemistica di questi due insiemi, che sappiamo come calcolare. Ecco come appare il programma risultante.

```java
import java.util.*;

public class FindDups2 {
    public static void main(String[] args) {
        Set<String> uniques = new HashSet<String>();
        Set<String> dups    = new HashSet<String>();

        for (String a : args)
            if (!uniques.add(a))
                dups.add(a);

        // Destructive set-difference
        uniques.removeAll(dups);

        System.out.println("Unique words:    " + uniques);
        System.out.println("Duplicate words: " + dups);
    }
}
```

Un'operazione set-algebrica meno comune è la differenza di insieme simmetrico — l'insieme di elementi contenuti in uno dei due insiemi specificati ma non in entrambi. Il codice seguente calcola la differenza di set simmetrica di due set in modo non distruttivo.

```java
Set<Type> symmetricDiff = new HashSet<Type>(s1);
symmetricDiff.addAll(s2);
Set<Type> tmp = new HashSet<Type>(s1);
tmp.retainAll(s2);
symmetricDiff.removeAll(tmp);
```

##### Operazioni sull'array dell'interfaccia Set

Le operazioni sugli array non fanno nulla di speciale per i set oltre a ciò che fanno per qualsiasi altra raccolta



Collections, fino a SortedMap