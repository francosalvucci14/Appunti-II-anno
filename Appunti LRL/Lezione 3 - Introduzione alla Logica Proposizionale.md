
# Logica Proposizionale

- $p,q\in\{T,F\}$
- $\land,\lor,\implies,\equiv,\neg,\oplus$

Indichiamo con $p, q, r, . . .$ delle variabili _Booleane_, ossia variabili che possono assumere valore True (Vero, che d’ora in poi indicheremo con T) o False (che d’ora in poi indicheremo con F). 
Chiamiamo _lettere proposizionali_ i simboli $p, q, r, . . .$ con cui indichiamo le variabili.
A partire dalle lettere proposizionali possiamo costruire delle formule più complesse usando i _connettivi_: data una variabile p, indichiamo con$\neg p$  la formula che è T se e solo se p è F; indichiamo con $p\lor q$ la formula che è T se e solo se almeno una fra p e q è T e con $p\land q$ la formula che è T quando p e q sono entrambe T. Possiamo sintetizzare queste affermazioni nelle cosiddette tabelle di verità

| p   | q   | $\neg p$ | $p\lor q$ | $p\land q$ |
| --- | --- | -------- | --------- | ---------- |
| T   | T   | F        | T         | T          |
| T   | F   | F        | T         | F          |
| F   | T   | T        | T         | F          |
| F   | F   | T        | F         | F          |

In tutto ci possono essere $2^4$ tabelle distinte, per due variabili p e q

## Formule ben formate

Ad ogni "formula" della logica proposizionale, possiamo assocaire una tabella di verità
Per esempio, la formula $p\land (q\lor\neg r)$ vale T se e soltanto se $P$ è T e ($q$ è T oppure $R$ è F), quindi avrà la seguente tabella di verità

| p   | q   | r   | $p\land(q\lor\neg r)$ |
| --- | --- | --- | --------------------- |
| T   | T   | T   | T                     |
| T   | T   | F   | T                     |
| T   | F   | T   | F                     |
| T   | F   | F   | T                     |
| F   | T   | T   | F                     |
| F   | T   | F   | F                     |
| F   | F   | T   | F                     |
| F   | F   | F   | F                     |

**Vedi esercizio su pdf**

Si osservi che non tutte le sequenze di lettere proposizionale e connettivi sono formule di cui possiamo dare una tabella di verità.
Per esempio, provate a dare una tabella di verità per 
$$p\implies\neg\lor(q\land r)\equiv$$

Abbiamo bisogno di una **formula ben formata**

>[!definition]- Definizione (formula ben formata)
>Le lettere proposizionali sono formule ben formate.
>Inoltre:
>1. Se $\mathcal F$ è una f.b.f allora anche $\neg F$ è una f.b.f
>2. Se $\mathcal F$ è una f.b.f allora anche $\mathcal F\circ\mathcal G$ è una f.b.f, dove con $\circ$ abbiamo indicato uno qualunque dei connettivi
>3. Nient'altro è una f.b.f

**Esercizio 3**

Osservate che tutte le formule dell’Esercizio 2 sono f.b.f. secondo la definizione precedente, mentre la sequenza di simboli in (1) non lo è. Ogni formula ben formata ha la sua tabella di verità. Viceversa, data una qualunque tabella di verità possiamo sempre trovare una formula (tante, in realtà) che ha quella data come tabella di verità

**Esercizio 4**
Per ognuna delle seguenti tabelle di verità, trovare una formula corrispondente

![[appunti lrl/immagini/Pasted image 20230320144011.png|center|300]]

## Tautologie, Contraddizioni, Contingenze

Sicuramente già si conoscono le formule di De Morgan. 
Quindi, come sarà fatta la tabella di verità della formula (2)?
$$\neg(p\lor q)\equiv(\neg p\land\neg q) (2)$$
E della formula (3)?
$$(\neg p\lor\neg q)\equiv\neg(p\land q)(3)$$

**Esercizio 6** Scrivere le tabelle di verità delle formule (2) e (3)

Data una formula, chiamiamo _interpretazione_ della formula un'assegnazione di verità alle sue variabili (in una tabella di verità, ogni riga rappresenta una diversa interpretazione)
Data una formula $\mathcal F$ e una sua intepretazione $\tau$, fa formula $\mathcal F$ è o T o F nell'interpretazione $\tau$

Per esempio, la formula 
$$(p\lor q)\land\neg r$$
è F nell'interpretazione $(p,q,r)=(T,F,T)$ mentre è T nell'interpretazione $(p,q,r)=(T,F,F)$

>[!definition]- Tautologie,Contraddizioni,Contingenze
>Si chiamano **tautologie** le formule che sono T in _ogni_ interpretazione, **contraddizioni** quelle che sono F in _ogni_ interpretazione, e **contingenze** le altre

**Esercizio 7 (Vedi pdf)**

Osservate che $\mathcal F$ è una tautologia se e soltanto se $\neg\mathcal F$ è una contraddizione, e viceversa
Diciamo che due formule sono _equivalenti_ se hanno la stessa tabella di verità.
$\mathcal F,\mathcal G$ sono equivalenti se e soltanto se $\mathcal F\equiv\mathcal G$ è una tautologia

## Costanti

Abbiamo usato le lettere proposizionali p, q, r, . . . per indicare delle variabili Booleane.
è utile aggiungere due lettere proposizionali, t e f, per indicare le due _costanti_ Booleane T e F. Si osservi, per esempio, che 
- $p\land f$ è equivalente a **f** mentre $p\land t$ è equivalente a **p** ;
- $p\lor f$ è equivalente a **p** mentre $p\lor t$ è equivalente a **t** ; 
- $f\land t$ è equivalente a **f** mentre $f\lor t$ è equivalente a **t**.

è interessante osservare che ogni formula che contiene **t** e/o **f** è sempre o equivalente a una formula che non contiene ne t ne f oppure è equivalente o a **t** o a **f**.

**Esercizio 8 vedi pdf**

## Interdipendenza dei connettivi

Finora nelle nostre formule asbbiamo usato i connettivi $\neg,\land,\lor,\implies,\equiv$ 
Si osservi he questi non sono tutti "necessari", perchè per esempio:

- $p\implies q$ è equivalente a $\neg p\lor q$, possiamo dire che il connettivo $\implies$ può essere definito in termini dei connettivi $\neg,\lor$
- $p\land q$ è equivalente a $\neg(\neg p\lor\neg q)$, possiamo dire che $\land$ può essere definito in termini di $\neg,\lor$
- $p\equiv q$ è equivalente a $(p\implies q)\land(q\implies p)$ o anche $(p\land q)\lor(\neg p\land\neg q)$, e quindi anche $\equiv$ può essere definito in termini di $\neg,\lor$

Quindi, potremmo riscrivere tutte le formule viste finora usando soltanto i due connettivi $\neg,\lor$

**Esercizi 9,10 vedi pdf**

Piccola domanda : 
> Esiste un connettivo che, da solo, può essere usato per definire tutti gli altri?

Consideriamo il connettivo seguente, che chiamiamo _joint denial_ (lo chiameremo NOR quando parleremo di circuiti)

| p   | q   | $p\downarrow q$ |
| --- | --- | --------------- |
| T   | T   | F               |
| T   | F   | F               |
| F   | T   | F               |
| F   | F   | T               |

Si osservi che:

1. $p\downarrow p$ è F quando p è T ed è T quando p è F. In altri termini, $p\downarrow p$ è equivalente a $\neg p$
2. La tabella di verità di $\downarrow$ è la negazione di quella di $\lor$, ossia $p\downarrow q$ è equivalente a $\neg(p\lor q)$. Ma allora $p\lor q$ deve essere equivalente a $\neg(p\downarrow q)$, che a sua volta, per il punto precedente, deve essere equivalente a $(p\downarrow q)\downarrow(p\downarrow q)$ 

**Esercizio 11 vedi pdf**

Siccome possiamo definire i connettivi $\neg,\lor$ in termini del connettivo $\downarrow$ per quanti visto all'inizio di questa sezione, possiamo definire anche tutti gli altri connettivi in termini del connettivo $\downarrow$ 

Oltre a $\downarrow$, c'è un'altro connettivo che, da solo, può essere usato per definire tutti gli altri : lo indichiamo con $|$ e lo chiamiamo _alternative denial_ (oppure NAND)

![[appunti lrl/immagini/Pasted image 20230320182234.png|center]]

**Esercizio 12 vedi pdf**

## Notazione polacca

Se scriviamo $[\implies pq]$ al posto di $[p\implies q]$, $[\land pq]$ al posto di $[p\land q]$, $[\lor pq]$ al posto di $[p\lor q]$ e $[\equiv pq]$ al posto di $[p\equiv q]$ è possibile scrivere ogni formula ben formata in modo non ambiguo senza l'utilizzo di parentesi. 
Questo tipo di sintassi è detta _notazione polacca_.

Ad esempio, la formula $\neg p\land(q\implies\neg r)$ diventa $\land\neg p\implies q\neg r$ 

>[!definition]- Definizione (F.b.f in notazione polacca)
>Ogni lettera proposizionale è una f.b.f. Inoltre,
>1. Se $\mathcal F$ è una f.b.f allora anche $\neg\mathcal F$ è una f.b.f
>2. Se $\mathcal F,\mathcal G$ sono f.b.f allora anche $\circ\mathcal F\mathcal G$ è una f.b.f, dove con il simbolo $\circ$ intendiamo qualunque connettivo
>3. Nient'altro è una f.b.f

**Esercizi 13,14 vedi pdf**
