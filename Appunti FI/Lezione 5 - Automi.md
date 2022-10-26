# Automa

Dispositivo astratto che, data una stringa x fornitagli in input, esegue una **computazione**
Se la computazione termina,restituisce,secondo una qualche modalità, un valore

Nel caso del problema di riconoscimento, il valore restituito è booleano

![[appunti fi/immagini/Pasted image 20221026150139.png|center|500]]

"Si" lo abbiamo se $x\in L$, altrimenti avremo "No" $x\not\in L$

## Composizione

- Dispositivo interno, che ad ogni istante assume un **stato** in un possibile insieme finito predefinito
- Uno o più dispositivi di memoria (nastri), sui quali è possibile memorizzare delle informazioni, sotto forma di stringhe di caratteri da alfabeti predefiniti
- Nastri costituiti da celle; ogni cella può contenere un carattere
- Caratteri letti o scritti per mezzo di **testine** che possono muoversi lungo i nastri, posizionandosi sulle diverse celle

## Configurazione di un automa
_Def_
Insieme delle informazioni necessarie e sufficienti per determinare, in un certo istante, il comportamento futuro dell'automa

1. Stato interno dell'automa
2. Contenuto di tutti i nastri di memoria
3. Posizione di tutte le testine sui nastri

L'insieme di 1,2,3 è la **configurazione** dell'automa

### Configurazione iniziale

Configurazione in cui si assume si trovi inizialmente un automa, in presenza di una stringa in input

Ad esempio:
1. Stato predefinito come iniziale;
2. Nastri di memoria vuoti eccetto il nastro di input, contenente la stringa;
3. Testina del nastro di input sulla cella contenente il primo carattere della stringa

### Funzione di transizione

Induce una **relazione di transizione** tra configurazioni, che associa ad una configurazionne un'altra (o più di una), **configurazione successiva**

Definita non sull'insieme delle possibili configurazioni, ma su domini e codomini che rappresentano parti di configurazioni, quelle che effettivamente determinano e sono determinate dalla transizione.

L'applicazione della funzione di transizione ad una configurazione si dice **transizione** o **mossa** o **passo computazionale** dell'automa.

#### Transizioni

Dato un automa $\mathcal A$ e due sue configurazioni $c_i,c_j$ la notazione $$c_i\vdash_{\mathcal A} c_j$$indica che $c_j$ deriva da $c_i$ per effetto dell'applicazione della funzione di transizione di $\mathcal A$

### Configurazioni di accettazione

Sottoinsieme delle possibili configurazioni: determinano, se raggiunte, l'accettazione della stringa in input da parte dell'automa

Tutte le altre configurazioni sono definite come **configurazioni di non accettazione**, o di **rifiuto**

## Computazione

Un automa esegue una computazione applicando iterativamente, ad ogni istante, la propria funzione di transizione alla configurazione attuale, a parte dalla configurazione iniziale.

Sequenze di configurazioni attraversate $c_0,c_1,c_2,...$ tale che $c_i\yields_{\mathcal A} c_{i+1}$ per $i=0,1,...$

**Chiusura transitiva**
$\vdash_{\mathcal A}^\star$: chiusura transitiva e riflessiva della relazione $\vdash_{\mathcal A}$   
Date due configurazioni $c_i,c_j$ di $\mathcal A$,
$$c_i\yields_{\mathcal A}^\star c_j$$
se e solo se esiste una computazione che porta $\mathcal A\:da\:c_i\:a\:c_j$

### Computazione massimale

Una computazione si dice massimale se:

1. $c_0,c_1,c_2,...,c_n$ ha lunghezza finita
2. non esiste nessuna configurazione c tale che $c_n\yields_{\mathcal A} c$

la computazione **termina**

### Esiti di una computazione

- $c_n$ esiste ed è una configurazione di accettazione, l'automa accetta la stringa in input
- $c_n$ esiste ed non è una configurazione di accettazione, l'automa rifiuta la stringa in input
- $c_n$ non esiste, la computazione non termina


# Automi deterministici
Ad ogni stringa di input associa una sola computazione, e quindi una singola sequenza di configurazioni

![[appunti fi/immagini/Pasted image 20221026162346.png|center|600]]

Un automa deterministico, data una stringa in input, può eseguire una sola computazione: se la computazione termina in una configurazione di accettazione, allora la stringa viene accettata

## Stringhe e linguaggio accettato

1. Automa deterministico $\mathcal A$
2. Stringa x in input
3. $c_0(x)$ configurazione iniziale di $\mathcal A$ corrispondente alla stringa x 

$\mathcal A$ accetta x se e solo se esiste una configurazione di accettazione c di $\mathcal A$ per la quale $$c_0(x)\yields_{\mathcal A}^\star c$$
Il linguaggio **accettato** da $\mathcal A$ è l'insieme $L(\mathcal A)$ di tutte le stringhe x accettate da $\mathcal A$
