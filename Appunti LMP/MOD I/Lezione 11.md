
# Eccezioni

## Cos'è un'eccezione?

Il termine eccezione è una scorciatoia per la frase "evento eccezionale".

>[!important]- Definizione
>Un'eccezione è un evento, che si verifica durante l'esecuzione di un programma, che interrompe il normale flusso delle istruzioni del programma.

Quando si verifica un errore all'interno di un metodo, il metodo crea un oggetto e lo passa al sistema di runtime. L'oggetto, chiamato oggetto eccezione, contiene informazioni sull'errore, incluso il tipo e lo stato del programma quando si è verificato l'errore. La creazione di un oggetto eccezione e la sua consegna al sistema di runtime è chiamata generazione di un'eccezione.

Dopo che un metodo genera un'eccezione, il sistema di runtime tenta di trovare qualcosa per gestirla. L'insieme di possibili "qualcosa" per gestire l'eccezione è l'elenco ordinato di metodi che sono stati chiamati per arrivare al metodo in cui si è verificato l'errore. L'elenco dei metodi è noto come stack di chiamate (vedere la figura successiva).

![[appunti lmp/mod i/immagini/exceptions-callstack.gif|center|300]]

Il sistema di runtime cerca nello stack di chiamate un metodo che contenga un blocco di codice in grado di gestire l'eccezione. Questo blocco di codice è chiamato gestore di eccezioni. La ricerca inizia con il metodo in cui si è verificato l'errore e procede attraverso lo stack di chiamate nell'ordine inverso rispetto a quello in cui sono stati chiamati i metodi. Quando viene trovato un gestore appropriato, il sistema di runtime passa l'eccezione al gestore. Un gestore di eccezioni è considerato appropriato se il tipo dell'oggetto eccezione generato corrisponde al tipo che può essere gestito dal gestore.

Si dice che il gestore di eccezioni scelto rilevi l'eccezione. Se il sistema di runtime cerca in modo esaustivo tutti i metodi nello stack di chiamate senza trovare un gestore di eccezioni appropriato, come mostrato nella figura successiva, il sistema di runtime (e, di conseguenza, il programma) termina.
![[appunti lmp/mod i/immagini/exceptions-errorOccurs.gif|center|400]]

