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
- **Set**: una raccolta che non può contenere elementi duplicati. Questa interfaccia modella l'astrazione dell'insieme matematico e viene utilizzata per rappresentare insiemi, come le carte che compongono una mano di poker, i corsi che costituiscono il programma di uno studente oi processi in esecuzione su una macchina. Vedi anche la sezione [[Lezione 13 - Collections#Set|Set]].
- **Lista**: una raccolta ordinata (a volte chiamata sequenza). Gli elenchi possono contenere elementi duplicati. L'utente di una lista generalmente ha un controllo preciso su dove è inserito ogni elemento nella lista e può accedere agli elementi tramite il loro indice intero (posizione). Se hai utilizzato Vector, hai familiarità con il sapore generale di List. Vedi anche la sezione [[Lezione 13 - Collections#Liste|Liste]]
- **Coda**: una raccolta utilizzata per contenere più elementi prima dell'elaborazione. Oltre alle operazioni di raccolta di base, una coda fornisce ulteriori operazioni di inserimento, estrazione e ispezione.Le code in genere, ma non necessariamente, ordinano gli elementi in un modo **FIFO (first-in, first-out)**. Tra le eccezioni vi sono le code di priorità, che ordinano gli elementi in base a un comparatore fornito o all'ordinamento naturale degli elementi. Qualunque sia l'ordinamento utilizzato, l'inizio della coda è l'elemento che verrebbe rimosso da una chiamata a remove o poll. In una coda FIFO, tutti i nuovi elementi vengono inseriti in coda alla coda. Altri tipi di code possono utilizzare regole di posizionamento differenti. Ogni implementazione di Queue deve specificare le proprie proprietà di ordinamento. Vedere anche la sezione [[Lezione 13 - Collections#Coda|Coda]].
- **Deque**: una raccolta utilizzata per contenere più elementi prima dell'elaborazione. Oltre alle operazioni di raccolta di base, una Deque fornisce ulteriori operazioni di inserimento, estrazione e ispezione.Deques può essere utilizzato sia come **FIFO (first-in, first-out) che LIFO (last-in, first-out)**. In una deque tutti i nuovi elementi possono essere inseriti, recuperati e rimossi alle due estremità. Vedi anche la sezione [[Lezione 13 - Collections#Deque|Deque]].
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

#### Liste

Una lista è una raccolta ordinata (a volte chiamata sequenza). Gli elenchi possono contenere elementi duplicati. Oltre alle operazioni ereditate da Collection, l'interfaccia List include operazioni per quanto segue:

- **Accesso posizionale**: manipola gli elementi in base alla loro posizione numerica nell'elenco. Questo include metodi come get, set, add, addAll e remove.
- **Cerca**: ricerca un oggetto specificato nell'elenco e ne restituisce la posizione numerica. I metodi di ricerca includono indexOf e lastIndexOf.
- **Iterazione**: estende la semantica di Iterator per sfruttare la natura sequenziale dell'elenco. I metodi listIterator forniscono questo comportamento.
- **Range-view**: Il metodo sublist esegue operazioni arbitrarie sull'elenco.

La piattaforma Java contiene due implementazioni List generiche. ArrayList, che di solito è l'implementazione con prestazioni migliori, e LinkedList che offre prestazioni migliori in determinate circostanze.

##### Operazioni di riscossione

Le operazioni ereditate da Collection fanno tutte ciò che ti aspetteresti che facciano, supponendo che tu le abbia già familiarità. Se non li conosci da Collection, ora sarebbe un buon momento per leggere la sezione The Collection Interface. L'operazione di rimozione rimuove sempre la prima occorrenza dell'elemento specificato dall'elenco. Le operazioni add e addAll aggiungono sempre i nuovi elementi alla fine dell'elenco. Pertanto, il seguente idioma concatena un elenco a un altro.

```java
list1.addAll(list2);
```

Ecco una forma non distruttiva di questo idioma, che produce un terzo elenco costituito dal secondo elenco aggiunto al primo.

```java
List<Type> list3 = new ArrayList<Type>(list1);
list3.addAll(list2);
```

Si noti che l'idioma, nella sua forma non distruttiva, sfrutta il costruttore di conversione standard di ArrayList.

Ed ecco un esempio (JDK 8 e versioni successive) che aggrega alcuni nomi in una lista

```java
List<String> list = people.stream()
.map(Person::getName)
.collect(Collectors.toList());
```

Come l'interfaccia Set, List rafforza i requisiti sui metodi equals e hashCode in modo che due oggetti List possano essere confrontati per l'uguaglianza logica indipendentemente dalle loro classi di implementazione. Due oggetti List sono uguali se contengono gli stessi elementi nello stesso ordine.

##### Accesso posizionale e operazioni di ricerca

Le operazioni di accesso posizionale di base sono get, set, add e remove. (Le operazioni set e remove restituiscono il vecchio valore che viene sovrascritto o rimosso.) Altre operazioni (indexOf e lastIndexOf) restituiscono il primo o l'ultimo indice dell'elemento specificato nell'elenco.
L'operazione addAll inserisce tutti gli elementi della Collection specificata a partire dalla posizione specificata. Gli elementi vengono inseriti nell'ordine in cui vengono restituiti dall'iteratore della Collection specificato. Questa chiamata è l'analogo di accesso posizionale dell'operazione addAll di Collection.

Ecco un piccolo metodo per scambiare due valori indicizzati in una lista.

```java
public static <E> void swap(List<E> a, int i, int j) {
    E tmp = a.get(i);
    a.set(i, a.get(j));
    a.set(j, tmp);
}
```

Certo, c'è una grande differenza. Questo è un algoritmo polimorfico: scambia due elementi in qualsiasi elenco, indipendentemente dal tipo di implementazione. Ecco un altro algoritmo polimorfico che utilizza il precedente metodo di scambio.

```java
public static void shuffle(List<?> list, Random rnd) {
    for (int i = list.size(); i > 1; i--)
        swap(list, i - 1, rnd.nextInt(i));
}
```

Questo algoritmo, incluso nella classe Collections della piattaforma Java, permuta in modo casuale l'elenco specificato utilizzando l'origine di casualità specificata. È un po' sottile: risale l'elenco dal basso, scambiando ripetutamente un elemento selezionato a caso nella posizione corrente. A differenza della maggior parte dei tentativi ingenui di mescolamento, è giusto (tutte le permutazioni si verificano con uguale probabilità, assumendo una fonte imparziale di casualità) e veloce (richiede esattamente list.size()-1 swap). Il seguente programma utilizza questo algoritmo per stampare le parole nella sua lista di argomenti in ordine casuale.

```java
import java.util.*;

public class Shuffle {
    public static void main(String[] args) {
        List<String> list = new ArrayList<String>();
        for (String a : args)
            list.add(a);
        Collections.shuffle(list, new Random());
        System.out.println(list);
    }
}
```

In effetti, questo programma può essere reso ancora più breve e veloce. La classe Arrays ha un metodo factory statico chiamato asList, che consente di visualizzare un array come un elenco. Questo metodo non copia l'array. Le modifiche nell'elenco vengono scritte nell'array e viceversa. L'elenco risultante non è un'implementazione di elenco generica, poiché non implementa le operazioni di aggiunta e rimozione (facoltative): gli array non sono ridimensionabili. Sfruttando Arrays.asList e chiamando la versione della libreria di shuffle, che utilizza una sorgente predefinita di casualità, si ottiene il seguente minuscolo programma il cui comportamento è identico al programma precedente.

```java
import java.util.*;

public class Shuffle {
    public static void main(String[] args) {
        List<String> list = Arrays.asList(args);
        Collections.shuffle(list);
        System.out.println(list);
    }
}
```

##### Iteratori

Come ci si aspetterebbe, l'Iterator restituito dall'operazione iteratore di List restituisce gli elementi dell'elenco nella sequenza corretta. List fornisce anche un iteratore più ricco, chiamato ListIterator, che consente di attraversare l'elenco in entrambe le direzioni, modificare l'elenco durante l'iterazione e ottenere la posizione corrente dell'iteratore.

I tre metodi che ListIterator eredita da Iterator (hasNext, next e remove) fanno esattamente la stessa cosa in entrambe le interfacce. Le operazioni hasPrevious e previous sono analoghi esatti di hasNext e next. Le prime operazioni si riferiscono all'elemento prima del cursore (implicito), mentre le seconde si riferiscono all'elemento dopo il cursore. L'operazione precedente sposta il cursore indietro, mentre quella successiva lo sposta in avanti.

Ecco l'idioma standard per l'iterazione all'indietro di un elenco.

```java
for (ListIterator<Type> it = list.listIterator(list.size()); it.hasPrevious(); ) {
    Type t = it.previous();
    ...
}
```

Nota l'argomento di listIterator nell'idioma precedente. L'interfaccia List ha due forme del metodo listIterator. Il form senza argomenti restituisce un ListIterator posizionato all'inizio della lista; il form con un argomento int restituisce un ListIterator posizionato all'indice specificato. L'indice si riferisce all'elemento che verrebbe restituito da una chiamata iniziale a next. Una chiamata iniziale a previous restituirebbe l'elemento il cui indice era index-1. In un elenco di lunghezza n, sono presenti n+1 valori validi per index, da 0 a n inclusi.

Intuitivamente parlando, il cursore si trova sempre tra due elementi: quello che verrebbe restituito da una chiamata a previous e quello che verrebbe restituito da una chiamata a next. Gli n+1 valori di indice validi corrispondono agli n+1 spazi tra gli elementi, dallo spazio prima del primo elemento allo spazio dopo l'ultimo. La figura seguente mostra le cinque possibili posizioni del cursore in un elenco contenente quattro elementi.

![[appunti lmp/mod i/immagini/colls-fivePossibleCursor.gif|center]]

Le chiamate al successivo e al precedente possono essere mescolate, ma devi stare un po' attento. La prima chiamata a previous restituisce lo stesso elemento dell'ultima chiamata a next. Allo stesso modo, la prima chiamata a next dopo una sequenza di chiamate a previous restituisce lo stesso elemento dell'ultima chiamata a previous.

Non dovrebbe sorprendere che il metodo nextIndex restituisca l'indice dell'elemento che verrebbe restituito da una successiva chiamata a next, e previousIndex restituisca l'indice dell'elemento che verrebbe restituito da una successiva chiamata a previous. Queste chiamate vengono in genere utilizzate per segnalare la posizione in cui è stato trovato qualcosa o per registrare la posizione di ListIterator in modo da poter creare un altro ListIterator con posizione identica.

Non dovrebbe inoltre sorprendere il fatto che il numero restituito da nextIndex sia sempre maggiore di uno rispetto al numero restituito da previousIndex. Ciò implica il comportamento dei due casi limite: (1) una chiamata a previousIndex quando il cursore è prima dell'elemento iniziale restituisce -1 e (2) una chiamata a nextIndex quando il cursore è dopo l'elemento finale restituisce list.size() . Per rendere tutto questo concreto, la seguente è una possibile implementazione di List.indexOf.

```java
public int indexOf(E e) {
    for (ListIterator<E> it = listIterator(); it.hasNext(); )
        if (e == null ? it.next() == null : e.equals(it.next()))
            return it.previousIndex();
    // Element not found
    return -1;
}
```

Si noti che il metodo indexOf restituisce it.previousIndex() anche se sta attraversando l'elenco in avanti. Il motivo è che it.nextIndex() restituirebbe l'indice dell'elemento che stiamo per esaminare, e noi vogliamo restituire l'indice dell'elemento appena esaminato.

L'interfaccia Iterator fornisce l'operazione di rimozione per rimuovere l'ultimo elemento restituito da next dalla Collection. Per ListIterator, questa operazione rimuove l'ultimo elemento restituito da next o previous. L'interfaccia ListIterator fornisce due operazioni aggiuntive per modificare l'elenco: impostare e aggiungere. Il metodo set sovrascrive l'ultimo elemento restituito da next o previous con l'elemento specificato. Il seguente algoritmo polimorfico usa set per sostituire tutte le occorrenze di un valore specificato con un altro.

```java
public static <E> void replace(List<E> list, E val, E newVal) {
    for (ListIterator<E> it = list.listIterator(); it.hasNext(); )
        if (val == null ? it.next() == null : val.equals(it.next()))
            it.set(newVal);
}
```

L'unica complicazione in questo esempio è il test di uguaglianza tra val e it.next. È necessario inserire in un caso speciale un valore val nullo per evitare un'eccezione NullPointerException.

Il metodo add inserisce un nuovo elemento nell'elenco immediatamente prima della posizione corrente del cursore. Questo metodo è illustrato nel seguente algoritmo polimorfico per sostituire tutte le occorrenze di un valore specificato con la sequenza di valori contenuta nell'elenco specificato.

```java
public static <E> 
    void replace(List<E> list, E val, List<? extends E> newVals) {
    for (ListIterator<E> it = list.listIterator(); it.hasNext(); ){
        if (val == null ? it.next() == null : val.equals(it.next())) {
            it.remove();
            for (E e : newVals)
                it.add(e);
        }
    }
}
```

##### Operazione Range-View

L'operazione di visualizzazione dell'intervallo, subList(int fromIndex, int toIndex), restituisce una visualizzazione List della parte di questo elenco i cui indici vanno da fromIndex, inclusivo, a toIndex, esclusivo. Questa gamma semiaperta rispecchia il tipico ciclo for.

```java
for (int i = fromIndex; i < toIndex; i++) {
    ...
}
```

Come implica il termine view, l'elenco restituito è supportato dall'elenco su cui è stato chiamato subList, quindi i cambiamenti nel primo si riflettono nel secondo.

Questo metodo elimina la necessità di operazioni di intervallo esplicite (del tipo che esiste comunemente per gli array). Qualsiasi operazione che prevede un elenco può essere utilizzata come un'operazione di intervallo passando una vista sottolista invece di un intero elenco. Ad esempio, il seguente idioma rimuove un intervallo di elementi da un elenco.

```java
list.subList(fromIndex, toIndex).clear();
```

Idiomi simili possono essere costruiti per cercare un elemento in un intervallo.

```java
int i = list.subList(fromIndex, toIndex).indexOf(o);
int j = list.subList(fromIndex, toIndex).lastIndexOf(o);
```

Si noti che gli idiomi precedenti restituiscono l'indice dell'elemento trovato nel subList, non l'indice nell'elenco di supporto.

Qualsiasi algoritmo polimorfico che opera su un elenco, come gli esempi di sostituzione e shuffle, funziona con l'elenco restituito da subList.

Ecco un algoritmo polimorfico la cui implementazione utilizza subList per distribuire una mano da un mazzo. Cioè, restituisce una nuova lista (la "mano") contenente il numero specificato di elementi presi dalla fine della lista specificata (il "mazzo"). Gli elementi restituiti in mano vengono rimossi dal mazzo.

```java
public static <E> List<E> dealHand(List<E> deck, int n) {
    int deckSize = deck.size();
    List<E> handView = deck.subList(deckSize - n, deckSize);
    List<E> hand = new ArrayList<E>(handView);
    handView.clear();
    return hand;
}
```

Nota che questo algoritmo rimuove la mano dalla fine del mazzo. Per molte implementazioni comuni di List, come ArrayList, le prestazioni della rimozione di elementi dalla fine dell'elenco sono sostanzialmente migliori rispetto a quelle della rimozione di elementi dall'inizio.

Quello che segue è un programma che utilizza il metodo dealHand in combinazione con Collections.shuffle per generare mani da un normale mazzo da 52 carte. Il programma accetta due argomenti della riga di comando: (1) il numero di mani da distribuire e (2) il numero di carte in ciascuna mano.

```java
import java.util.*;

public class Deal {
    public static void main(String[] args) {
        if (args.length < 2) {
            System.out.println("Usage: Deal hands cards");
            return;
        }
        int numHands = Integer.parseInt(args[0]);
        int cardsPerHand = Integer.parseInt(args[1]);
    
        // Make a normal 52-card deck.
        String[] suit = new String[] {
            "spades", "hearts", 
            "diamonds", "clubs" 
        };
        String[] rank = new String[] {
            "ace", "2", "3", "4",
            "5", "6", "7", "8", "9", "10", 
            "jack", "queen", "king" 
        };

        List<String> deck = new ArrayList<String>();
        for (int i = 0; i < suit.length; i++)
            for (int j = 0; j < rank.length; j++)
                deck.add(rank[j] + " of " + suit[i]);
    
        // Shuffle the deck.
        Collections.shuffle(deck);
    
        if (numHands * cardsPerHand > deck.size()) {
            System.out.println("Not enough cards.");
            return;
        }
    
        for (int i = 0; i < numHands; i++)
            System.out.println(dealHand(deck, cardsPerHand));
    }
  
    public static <E> List<E> dealHand(List<E> deck, int n) {
        int deckSize = deck.size();
        List<E> handView = deck.subList(deckSize - n, deckSize);
        List<E> hand = new ArrayList<E>(handView);
        handView.clear();
        return hand;
    }
}
```

Sebbene l'operazione subList sia estremamente potente, è necessario prestare attenzione quando la si utilizza. La semantica dell'elenco restituito da subList diventa indefinita se gli elementi vengono aggiunti o rimossi dall'elenco di supporto in qualsiasi modo diverso dall'elenco restituito. Pertanto, si consiglia vivamente di utilizzare l'elenco restituito da subList solo come oggetto transitorio, per eseguire una o una sequenza di operazioni di intervallo sull'elenco di supporto. Più a lungo utilizzi l'istanza subList, maggiore è la probabilità che tu la comprometta modificando l'elenco di supporto direttamente o tramite un altro oggetto subList. Si noti che è consentito modificare una sottolista di una sottolista e continuare a utilizzare la sottolista originale (anche se non contemporaneamente).

##### Algoritmi delle liste

La maggior parte degli algoritmi polimorfici nella classe Collections si applica specificamente a List. Avere tutti questi algoritmi a tua disposizione rende molto facile manipolare gli elenchi. Di seguito è riportato un riepilogo di questi algoritmi

- **sort**:ordina un elenco utilizzando un algoritmo di ordinamento di tipo merge, che fornisce un ordinamento veloce e stabile. (Un ordinamento stabile è quello che non riordina elementi uguali.)
- **shuffle**: permuta casualmente gli elementi in una lista.
- **reverse**: inverte l'ordine degli elementi in un elenco.
- **ruotare**: ruota tutti gli elementi in un elenco di una distanza specificata.
- **swap**: scambia gli elementi in posizioni specificate in un elenco.
- **replaceAll**: sostituisce tutte le occorrenze di un valore specificato con un altro.
- **fill** : sovrascrive ogni elemento in una lista con il valore specificato.
- **copy** : copia l'elenco di origine nell'elenco di destinazione.
- **binarySearch**: cerca un elemento in un elenco ordinato utilizzando l'algoritmo di ricerca binaria.
- **indexOfSubList** : restituisce l'indice del primo sottoelenco di un elenco uguale a un altro.
- **lastIndexOfSubList**: restituisce l'indice dell'ultimo sottoelenco di un elenco uguale a un altro.

#### Coda

Una coda è una raccolta per conservare gli elementi prima dell'elaborazione. Oltre alle operazioni di raccolta di base, le code forniscono ulteriori operazioni di inserimento, rimozione e ispezione. Segue l'interfaccia della coda.

```java
public interface Queue<E> extends Collection<E> {
    E element();
    boolean offer(E e);
    E peek();
    E poll();
    E remove();
}
```

Ogni metodo Queue esiste in due forme: (1) una genera un'eccezione se l'operazione fallisce e (2) l'altra restituisce un valore speciale se l'operazione fallisce (null o false, a seconda dell'operazione). La struttura regolare dell'interfaccia è illustrata nella tabella seguente.

| **Operazione** | **Eccezione** | **Return valore speciale** |
| -------------- | ------------- | -------------------------- |
| Insert         | add(e)        | offer(e)                   |
| Remove         | remove()      | poll()                     |
| Examine        | element()     | peek()                     |

Le code in genere, ma non necessariamente, ordinano gli elementi in un modo FIFO (first-in-first-out). Tra le eccezioni vi sono le code di priorità, che ordinano gli elementi in base ai loro valori (vedere la sezione Ordinamento degli oggetti per i dettagli). Qualunque sia l'ordinamento utilizzato, l'inizio della coda è l'elemento che verrebbe rimosso da una chiamata a remove o poll. In una coda FIFO, tutti i nuovi elementi vengono inseriti in coda alla coda. Altri tipi di code possono utilizzare regole di posizionamento differenti. Ogni implementazione di Queue deve specificare le proprie proprietà di ordinamento.

È possibile che un'implementazione di Queue limiti il numero di elementi che contiene; tali code sono note come limitate. Alcune implementazioni di Queue in java.util.concurrent sono limitate, ma le implementazioni in java.util non lo sono.

Il metodo add, che Queue eredita da Collection, inserisce un elemento a meno che non violi le restrizioni di capacità della coda, nel qual caso genera IllegalStateException. Il metodo offer, destinato esclusivamente all'uso su code limitate, differisce da add only in quanto indica il mancato inserimento di un elemento restituendo false.

I metodi remove e poll rimuovono e restituiscono l'inizio della coda. Esattamente quale elemento viene rimosso è una funzione della politica di ordinazione della coda. I metodi remove e poll differiscono nel loro comportamento solo quando la coda è vuota. In queste circostanze, remove genera NoSuchElementException, mentre poll restituisce null.

I metodi element e peek restituiscono, ma non rimuovono, l'inizio della coda. Differiscono l'uno dall'altro esattamente nello stesso modo di remove e poll: se la coda è vuota, element lancia NoSuchElementException, mentre peek restituisce null.

Le implementazioni della coda generalmente non consentono l'inserimento di elementi nulli. L'implementazione LinkedList, che è stata adattata per implementare Queue, è un'eccezione. Per ragioni storiche, consente elementi null, ma dovresti evitare di trarne vantaggio, poiché null viene utilizzato come valore di ritorno speciale dai metodi poll e peek.

Le implementazioni della coda in genere non definiscono le versioni basate sugli elementi dei metodi equals e hashCode, ma ereditano invece le versioni basate sull'identità da Object.

L'interfaccia Queue non definisce i metodi di coda di blocco, che sono comuni nella programmazione concorrente. Questi metodi, che attendono la comparsa di elementi o la disponibilità di spazio, sono definiti nell'interfaccia java.util.concurrent.BlockingQueue, che estende Queue.

Nel seguente programma di esempio, viene utilizzata una coda per implementare un timer per il conto alla rovescia. La coda è precaricata con tutti i valori interi da un numero specificato nella riga di comando a zero, in ordine decrescente. Quindi, i valori vengono rimossi dalla coda e stampati a intervalli di un secondo. Il programma è artificiale in quanto sarebbe più naturale fare la stessa cosa senza usare una coda, ma illustra l'uso di una coda per memorizzare elementi prima della successiva elaborazione.

```java
import java.util.*;

public class Countdown {
    public static void main(String[] args) throws InterruptedException {
        int time = Integer.parseInt(args[0]);
        Queue<Integer> queue = new LinkedList<Integer>();

        for (int i = time; i >= 0; i--)
            queue.add(i);

        while (!queue.isEmpty()) {
            System.out.println(queue.remove());
            Thread.sleep(1000);
        }
    }
}
```

Nell'esempio seguente viene utilizzata una coda di priorità per ordinare una raccolta di elementi. Ancora una volta questo programma è artificiale in quanto non c'è motivo di usarlo a favore del metodo di ordinamento fornito in Collections, ma illustra il comportamento delle code di priorità.

```java
static <E> List<E> heapSort(Collection<E> c) {
    Queue<E> queue = new PriorityQueue<E>(c);
    List<E> result = new ArrayList<E>();

    while (!queue.isEmpty())
        result.add(queue.remove());

    return result;
}
```


#### Deque

Solitamente pronunciato come mazzo, un deque è una coda a doppia estremità. Una coda a doppia estremità è una raccolta lineare di elementi che supporta l'inserimento e la rimozione di elementi in entrambi i punti finali. L'interfaccia Deque è un tipo di dati astratto più ricco rispetto sia a Stack che a Queue perché implementa contemporaneamente sia stack che code. L'interfaccia Deque definisce i metodi per accedere agli elementi su entrambe le estremità dell'istanza Deque. Vengono forniti metodi per inserire, rimuovere ed esaminare gli elementi. Classi predefinite come ArrayDeque e LinkedList implementano l'interfaccia Deque.

Si noti che l'interfaccia Deque può essere utilizzata sia come stack last-in-first-out che come code first-in-first-out. I metodi forniti nell'interfaccia Deque sono divisi in tre parti:

- Insert: I metodi addfirst e offerFirst inseriscono elementi all'inizio dell'istanza Deque. I metodi addLast e offerLast inseriscono elementi alla fine dell'istanza Deque. Quando la capacità dell'istanza Deque è limitata, i metodi preferiti sono offerFirst e offerLast perché addFirst potrebbe non riuscire a generare un'eccezione se è piena.
- Remove:I metodi removeFirst e pollFirst rimuovono elementi dall'inizio dell'istanza Deque. I metodi removeLast e pollLast rimuovono gli elementi dalla fine. I metodi pollFirst e pollLast restituiscono null se Deque è vuoto, mentre i metodi removeFirst e removeLast generano un'eccezione se l'istanza Deque è vuota.
- Retrieve:I metodi getFirst e peekFirst recuperano il primo elemento dell'istanza Deque. Questi metodi non rimuovono il valore dall'istanza Deque. Allo stesso modo, i metodi getLast e peekLast recuperano l'ultimo elemento. I metodi getFirst e getLast generano un'eccezione se l'istanza deque è vuota mentre i metodi peekFirst e peekLast restituiscono NULL.

I 12 metodi per l'inserimento, la rimozione e il recupero degli elementi Deque sono riassunti nella seguente tabella:

| **Operazioni** | **First Element**         | **Last Element**        |
| -------------- | ------------------------- | ----------------------- |
| Insert         | addFirst(e),offerFirst(e) | addLast(e),offerLast(e) |
| Remove         | removeFirst(),pullFirst() | removeLast(),pullLast() |
| Examine        | getFirst(),peekFirst()    | getLast(),peekLast()    |

Oltre a questi metodi di base per inserire, rimuovere ed esaminare un'istanza Deque, l'interfaccia Deque ha anche altri metodi predefiniti. Uno di questi è removeFirstOccurence, questo metodo rimuove la prima occorrenza dell'elemento specificato se esiste nell'istanza Deque. Se l'elemento non esiste, l'istanza Deque rimane invariata. Un altro metodo simile è removeLastOccurence; questo metodo rimuove l'ultima occorrenza dell'elemento specificato nell'istanza Deque. Il tipo restituito di questi metodi è booleano e restituiscono true se l'elemento esiste nell'istanza Deque.

#### Map

Una mappa è un oggetto che mappa le chiavi ai valori. Una mappa non può contenere chiavi duplicate: ogni chiave può mappare al massimo un valore. Modella l'astrazione della funzione matematica. L'interfaccia Map include metodi per operazioni di base (come put, get, remove, containsKey, containsValue, size e empty), operazioni di massa (come putAll e clear) e viste di raccolta (come keySet, entrySet e valori) .

La piattaforma Java contiene tre implementazioni di mappe generiche: HashMap, TreeMap e LinkedHashMap. Il loro comportamento e le loro prestazioni sono esattamente analoghi a HashSet, TreeSet e LinkedHashSet, come descritto nella sezione The Set Interface.

Il resto di questa pagina discute in dettaglio l'interfaccia Mappa. Ma prima, ecco alcuni altri esempi di raccolta su Maps utilizzando le operazioni di aggregazione JDK 8. La modellazione di oggetti del mondo reale è un'attività comune nella programmazione orientata agli oggetti, quindi è ragionevole pensare che alcuni programmi potrebbero, ad esempio, raggruppare i dipendenti per dipartimento:

```java
// Group employees by department
Map<Department, List<Employee>> byDept = employees.stream()
.collect(Collectors.groupingBy(Employee::getDepartment));
```

Oppure calcola la somma di tutti gli stipendi per dipartimento:

```java
// Compute sum of salaries by department
Map<Department, Integer> totalByDept = employees.stream()
.collect(Collectors.groupingBy(Employee::getDepartment,
Collectors.summingInt(Employee::getSalary)));
```

O forse raggruppare gli studenti superando o fallendo i voti:

```java
// Partition students into passing and failing
Map<Boolean, List<Student>> passingFailing = students.stream()
.collect(Collectors.partitioningBy(s -> s.getGrade()>= PASS_THRESHOLD));
```

Puoi anche raggruppare le persone per città:

```java
// Classify Person objects by city
Map<String, List<Person>> peopleByCity
         = personStream.collect(Collectors.groupingBy(Person::getCity));
```

O anche mettere in cascata due raccoglitori per classificare le persone per stato e città:

```java
// Cascade Collectors 
Map<String, Map<String, List<Person>>> peopleByStateAndCity
  = personStream.collect(Collectors.groupingBy(Person::getState,
  Collectors.groupingBy(Person::getCity)))
```

##### Operazioni base sull'interfaccia Map

Le operazioni di base di Map (put, get, containsKey, containsValue, size e isEmpty) si comportano esattamente come le loro controparti in Hashtable. Il seguente programma genera una tabella di frequenza delle parole trovate nella sua lista di argomenti. La tabella delle frequenze associa ogni parola al numero di volte in cui ricorre nell'elenco degli argomenti.

```java
import java.util.*;

public class Freq {
    public static void main(String[] args) {
        Map<String, Integer> m = new HashMap<String, Integer>();

        // Initialize frequency table from command line
        for (String a : args) {
            Integer freq = m.get(a);
            m.put(a, (freq == null) ? 1 : freq + 1);
        }

        System.out.println(m.size() + " distinct words:");
        System.out.println(m);
    }
}
```

Come le interfacce Set e List, Map rafforza i requisiti sui metodi equals e hashCode in modo che due oggetti Map possano essere confrontati per l'uguaglianza logica indipendentemente dai loro tipi di implementazione. Due istanze Map sono uguali se rappresentano le stesse mappature chiave-valore.

Per convenzione, tutte le implementazioni di Map generiche forniscono costruttori che accettano un oggetto Map e inizializzano il nuovo Map per contenere tutti i mapping di valori-chiave nella Map specificata. Questo costruttore di conversione Map standard è del tutto analogo al costruttore Collection standard: consente al chiamante di creare una mappa di un tipo di implementazione desiderato che inizialmente contiene tutte le mappature in un'altra mappa, indipendentemente dal tipo di implementazione dell'altra mappa. Ad esempio, supponi di avere una mappa, denominata m. Il seguente one-liner crea una nuova HashMap contenente inizialmente tutte le stesse mappature chiave-valore di m.

```java
Map<K, V> copy = new HashMap<K, V>(m);
```

##### Operazioni di bulk sull'interfaccia Map

L'operazione di cancellazione fa esattamente ciò che si potrebbe pensare: rimuove tutte le mappature dalla mappa. L'operazione putAll è l'analogo Map dell'operazione addAll dell'interfaccia Collection. Oltre al suo ovvio uso di scaricare una mappa in un'altra, ha un secondo uso più sottile. Supponiamo che una mappa venga utilizzata per rappresentare una raccolta di coppie attributo-valore; l'operazione putAll, in combinazione con il costruttore di conversione Map, fornisce un modo accurato per implementare la creazione di mappe di attributi con valori predefiniti. Di seguito è riportato un metodo factory statico che illustra questa tecnica.

```java
static <K, V> Map<K, V> newAttributeMap(Map<K, V>defaults, Map<K, V> overrides) {
    Map<K, V> result = new HashMap<K, V>(defaults);
    result.putAll(overrides);
    return result;
}
```

##### Viste di raccolta

I metodi di visualizzazione della raccolta consentono di visualizzare una mappa come una raccolta in questi tre modi:

- keySet — l'insieme di chiavi contenute nella mappa.
- values — La raccolta di valori contenuti nella mappa. Questa Collection non è un Set, perché più chiavi possono essere associate allo stesso valore.
- entrySet — l'insieme di coppie chiave-valore contenute nella mappa. L'interfaccia Map fornisce una piccola interfaccia nidificata chiamata Map.Entry, il tipo degli elementi in questo Set.

Le viste Collection forniscono l'unico mezzo per iterare su una mappa. Questo esempio illustra l'idioma standard per iterare sulle chiavi in una mappa con un costrutto for-each:

```java
for (KeyType key : m.keySet())
    System.out.println(key);
```

e con un iteratore:

```java
// Filter a map based on some 
// property of its keys.
for (Iterator<Type> it = m.keySet().iterator(); it.hasNext(); )
    if (it.next().isBogus())
        it.remove();
```

L'idioma per iterare sui valori è analogo. Di seguito è riportato l'idioma per l'iterazione sulle coppie chiave-valore.

```java
for (Map.Entry<KeyType, ValType> e : m.entrySet())
    System.out.println(e.getKey() + ": " + e.getValue());
```

All'inizio, molte persone temono che questi idiomi possano essere lenti perché Map deve creare una nuova istanza Collection ogni volta che viene chiamata un'operazione di visualizzazione Collection. Stai tranquillo: non c'è motivo per cui una mappa non possa restituire sempre lo stesso oggetto ogni volta che viene richiesta una determinata visualizzazione della raccolta. Questo è esattamente ciò che fanno tutte le implementazioni di Map in java.util.

Con tutte e tre le visualizzazioni Collection, chiamando l'operazione di rimozione di un iteratore viene rimossa la voce associata dalla mappa di supporto, presupponendo che la mappa di supporto supporti la rimozione dell'elemento per cominciare. Ciò è illustrato dall'idioma di filtraggio precedente.

Con la vista entrySet, è anche possibile modificare il valore associato a una chiave chiamando il metodo setValue di Map.Entry durante l'iterazione (di nuovo, supponendo che la mappa supporti la modifica del valore per cominciare). Si noti che questi sono gli unici modi sicuri per modificare una mappa durante l'iterazione; il comportamento non è specificato se la mappa sottostante viene modificata in qualsiasi altro modo mentre l'iterazione è in corso.

Le viste Collection supportano la rimozione degli elementi in tutte le sue numerose forme: operazioni remove, removeAll, retainAll e clear, nonché l'operazione Iterator.remove. (Ancora una volta, questo presuppone che la mappa di supporto supporti la rimozione degli elementi.)

Le viste Raccolta non supportano l'aggiunta di elementi in nessun caso. Non avrebbe senso per le viste keySet e values, e non è necessario per la vista entrySet, perché i metodi put e putAll della mappa di supporto forniscono la stessa funzionalità.

Collections, fino a SortedMap