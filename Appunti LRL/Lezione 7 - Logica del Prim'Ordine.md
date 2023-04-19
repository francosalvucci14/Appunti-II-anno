
# Antipasto

Prima di addentrarci nelle descrizione precisa di sintassi (quali sono i simboli che usiamo, le formule ben formate, . . . ) e semantica (cos’è una interpretazione, quando una formula è vera o falsa, . . . ) della logica del primo ordine, vediamo qualche esempio che dovrebbe essere comprensibile attingendo a ciò che già sappiamo e usando un po’ di intuito.  

Consideriamo la seguente sequenza di simboli
$$\forall x[P(x)\lor Q(x)](1)$$
Si ricordi che, nel caso della logica proposizionale, una interpretazione di una formula ben è una assegnazione di verità per le variabili. Data una interpretazione, abbiamo visto che una formula risulta T oppure F.  
Secondo voi quale può essere una “interpretazione” di una formula tipo la (1)? 
Vediamo. Dobbiamo specificare due cose:  
1. Un dominio all’interno del quale si muove la variabile x;  
2. Una proprietà per ognuna delle due lettere predicative P e Q.  
Una volta che specifichiamo queste due cose la formula in (1) diventa T o F. 
Facciamo qualche esempio

**Esempio**. Prendiamo come dominio i numeri naturali $\mathbb N$. Per quanto riguarda le due lettere predicative P e Q, assegnamogli queste proprietà $P (x)$ è “x è pari” e $Q(x)$ è “x è dispari”. 
In questa interpretazione la Formula (1) diventa “Per ogni numero naturale x, x è pari oppure x è dispari”. 
Direi che è senz’altro vera

**Esempio**. Dominio $\mathbb N$, $P (x)$ = “x è un numero primo”, $Q(x)$ = “x è una potenza di 2”.  
In questa interpretazione la (1) è falsa. Infatti, per esempio, il numero naturale 6 non è ne un numero primo ne una potenza di 2.

Nella formula (1) le lettere predicative, P e Q, hanno un solo argomento, indicano quindi una proprietà degli elementi del dominio. Le lettere predicative posso avere più argomenti, nel qual caso indicano delle relazioni fra gli elementi del dominio.

**Esempio**. Consideriamo la formula  
$$\exists x\forall yP(x,y)(2)$$
<u>Interpretazione 1</u>: Prendiamo come dominio $\mathbb N$ e come $P (x, y)$ la relazione “x è minore o  
uguale a y”. In questa interpretazione la Formula (2) risulta “Esiste un numero naturale x tale che per ogni numero naturale y, abbiamo che x è minore o uguale a y”. Possiamo anche scriverla con la usuale simbologia usata in matematica
$$\exists x\in\mathbb N:\forall y\in\mathbb N,x\leq y$$
Sarete d’accordo che la (2) è vera in questa interpretazione. Infatti, c’è il numero naturale 1, per cui vale che tutti i numeri naturali sono maggiori o uguali a 1. D’altra parte, è facile trovare delle interpretazioni in cui la (2) è falsa, per esempio: <u>Interpretazione 2:</u> Dominio $\mathbb Z$ e $P (x, y)$ come prima; oppure <u>Interpretazione 3:</u> Dominio $\mathbb N$ e $P (x, y)$ con la disuguaglianza invertita $(x \geq y)$.

Ora considerate questa formula  
$$\forall xP (x) \to\exists xP (x) (3)  $$

Ragioniamo intuitivamente. La Formula (3) è una implicazione. Quindi, per quello che sappiamo dalla logica proposizionale, l’unico caso in cui è F è quando la premessa è T e la conseguenza è F. Nella (3) la premessa è $\forall xP (x)$ e la conseguenza è $\exists xP (x)$. Ora osservate che qualunque dominio scegliete e qualunque sia la proprietà P che considerate, se la premessa risulta vera (ossia, à vero che la proprietà P vale per tutti gli elementi del dominio) deve per forza valere anche la conseguenza (ossia, esiste un elemento del dominio per cui vale la proprietà P ). Quindi la Formula (3) deve essere vera in ogni interpretazione.  

Considerate la formula seguente,  
$$[\exists xP (x) \land\exists xQ(x)] \to\exists x[P (x) \land Q(x)] (4) $$ 
pensate che sia vera in ogni interpretazione oppure no? E l’implicazione nel verso opposto?  
$$\exists x[P (x) \land Q(x)] \to [\exists xP (x) \land \exists xQ(x)](5)$$

# Sintassi e semantica

I simboli che usiamo nella logica del primo ordine sono:  
- I connettivi $(\neg, \lor, \land, \to, \dots )$ usati anche nella logica proposizionale.  
- Le variabili (x, y, z, . . . oppure $x_1, x_2, x_3, \dots$ ), che qui chiamiamo individuali, per distinguerle dalle variabili Booleane della logica proposizionale. Le variabili individuali possono assumere valori in qualunque dominio.  
- Le lettere predicative (P , Q, R, . . . oppure $P_1, P_2, P_3,\dots$). A volte può essere utile indicare con un apice il numero di argomenti (per esempio, $P^{(n)}$).  
- I quantificatori ($\forall$ e $\exists$).  

In aggiunta ai simboli qui sopra, che abbiamo già utilizzato intuitivamente nella  
sezione precedente, useremo anche altri simboli:  

- Le costanti (a, b, c, . . . oppure $a_1, a_2, a_3,\dots$), che servono ad indicare specifici elementi del dominio.  
- Le lettere funzionali (f , g, h, . . . oppure $f_1, f_2, f_3, \dots$). Per esempio, $f (x_1, x_2)$ indicherà una funzione che mappa una coppia ordinata $(x_1, x_2)$ di elementi del dominio in un altro elemento del dominio $f (x_1, x_2)$. Come per le lettere predicative, anche nel caso delle lettere funzionali può essere utile indicare con un apice il numero di argomenti della funzione.  

Dobbiamo definire cosa si intende per formula ben formata nella logica del primo  
ordine. Per farlo, abbiamo prima bisogno di definire cos’è un **termine.**

>[!definition]- Definizione 2.1 (Termine)
>Le variabili e le costanti sono termini. Se $t_1, \dots, t_n$ sono termini e $f^{(n)}$ è una lettera funzionale con n argomenti, allora anche $f^{(n)}(t_1,\dots, t_n)$ è un **termine**

Ora possiamo dare una definizione precisa di formula ben formata

>[!definition]- Definizione 2.2 (Formula ben formata) [^1]
>Se $t_1,\dots , t_n$ sono termini e $P^{(n)}$ è una lettera predicativa con n argomenti, allora $P^{(n)}(t_1, \dots , t_n)$ è una **formula ben formata** (f.b.f.).  
>Queste si chiamano formule _**atomiche**_. Inoltre:
>- Se $\mathcal F$ è una f.b.f., allora anche $\neg\mathcal F$ è una f.b.f. 
>- Se $\mathcal F$ e $\mathcal G$ sono f.b.f. allora anche $\mathcal F\circ\mathcal G$ è una f.b.f., dove con $\circ$ abbiamo indicato uno qualunque dei connettivi $\land, \lor, \to, \equiv$. 
>- Infine, se $\mathcal F$ è una f.b.f. e x è una variabile, allora anche $\forall x\mathcal F$ e $\exists x\mathcal F$ sono f.b.f.
>- Nient’altro è una f.b.f

Ora che abbiamo definito con precisione quali sono le formule ben formate (la sintassi) della logica del primo ordine, andiamo a descriverne il significato (la semantica).

>[!definition]- Definizione 2.3 (Interpretazione)
>Data una f.b.f. $\mathcal F$, una sua interpretazione consiste in  
>- Un insieme non vuoto D che chiamiamo dominio; 
>- Una proprietà o una relazione per ogni lettera predicativa $\mathcal P$ in $\mathcal F$;  
>- Una funzione per ogni lettera funzionale $f$ in $\mathcal F$; 
>- Un elemento del dominio per ogni costante $a$ in $\mathcal F$.

Nel determinare la verità o meno di una formula in una data interpretazione, il significato dei connettivi che hanno nella logica proposizionale, il significato dei quantificatori e quello usuale.

Esempio. Consideriamo la formula  
$$\forall x\exists yP (f (x, a), y) (6)  $$

<u>Interpretazione 1</u>. Dominio $\mathbb N$; $P (x, y)$ = “x è uguale a y”; $f (x, y) = x^y$; $a = 2$. 
In questa interpretazione la formula si legge “Per ogni numero naturale x esiste un numero naturale y tale che $x^2 = y$”. Direi che è T. 

<u>Interpretazione 2.</u> Tutto come nell’Interpretazione 1, tranne che $P (x, y)$ = “x è maggiore di y”.
In questa interpretazione la (6) si legge, “Per ogni numero naturale x esiste un numero naturale y tale che $x^2$ è maggiore di y”. Quindi è F, perch è non è vera per $x = 1.$

# Variabili libere e vincolate. Formule chiuse

Per tutte le formule viste finora, una volta data una interpretazione I, la formula risultava T o F nell’interpretazione I. Tuttavia, questo non è vero per ogni f.b.f. in accordo alla Definizione 2.2[^1]. Per esempio, osservate che la formula $\forall xP (x, y)$ è una f.b.f. secondo la Definizione 2.2. Proviamo a darne una interpretazione: dominio $\mathbb N$ e $P (x, y)$ =“x è maggiore di y”. In questa interpretazione la formula si legge “Per ogni numero naturale x si ha che x è maggiore di y”. Vera o falsa? Non si può dire perch è non sappiamo chi è y. In quella formula si dice che x è una _variabile vincolata_, mentre y è _libera._

>[!definition]- Definizione 3.1 (Variabili libere e vincolate)
>In una f.b.f. si dice **vincolata** una variabile che sta nel campo d’azione di un quantificatore. Altrimenti la variabile si dice **libera**

Osservate che una stessa variabile può anche comparire libera in alcune occorrenze e vincolata in altre. Per esempio, nella formula seguente la prima occorrenza della variabile y è libera, mentre la seconda è vincolata.
$$\forall x[P (x) \land Q(y)] \to\exists yQ(y)$$

>[!definition]- Definizione 3.2 (Formule chiuse).
>Una f.b.f. senza variabili libere si dice **chiusa**.

# Formule valide vs tautologie

>[!definition]- Definizione 4.1. (Formule valide)
>Una formula $\mathcal F$ vera in ogni interpretazione si dice **valida**.

Perchè non le chiamiamo tautologie, come nel caso della logica proposizionale? Perchè vogliamo riservare il termine tautologie per un sottoinsieme delle formule valide. Per esempio, considerate la formula seguente  
$$\forall xP (x) \lor \neg(\forall xP (x))  $$
Questa formula del tipo $\mathcal F \lor \neg\mathcal F$, quindi chiaramente deve essere vera in ogni interpretazione. Nella logica del primo ordine si chiamano tautologie le formule che sono istanze di tautologie della logica proposizionale. Per esempio, la formula  
$$\forall xP (x) \to (\exists xQ(x) \to \forall xP (x)) (7)  $$
Si ottiene dalla formula $X \to (Y \to X)$ sostituendo $\forall xP (x)$ a X e $\exists xQ(x)$. La  
formule (7) pertanto è una tautologia mentre, per esempio la (3), pur essendo valida, non  
è una tautologia.  
Si noti che una tautologia è vera in ogni interpretazione _indipendentemente_ dal significato che hanno i quantificatori, mentre una formula valida che non è una tautologia è vera in ogni interpretazione per il significato che hanno i quantificatori.

# Interdipendenza tra connettivi

I due quantificatori $\forall$ e $\exists$ non sono indipendenti, nel senso che si può “definire” uno in funzione dell’altro. Per esempio, la formula $\neg\exists xP (x)$ è equivalente alla formula $\forall x\neg P (x).$

Infatti, data una qualunque interpretazione, la prima sta dicendo che “non esiste un  
elemento del dominio per cui vale la proprietà P ”, la seconda sta dicendo che “per ogni  
elemento del dominio non vale la proprietà P ”



[^1]: Vedi qui