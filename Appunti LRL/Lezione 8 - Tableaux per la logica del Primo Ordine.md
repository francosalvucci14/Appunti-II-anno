# Le regole per i quantificatori

Abbiamo visto che possiamo classificare essenzialmente tutte le formule della logica proposizionale in due tipi: $\alpha$-formule (quelle di tipo and) e $\beta$-formule (quelle di tipo or)

![[appunti lrl/immagini/Pasted image 20230419151935.png|center|350]]

Ad ogni formula corrisponde una regola di estensione nei tableaux

![[appunti lrl/immagini/Pasted image 20230419152032.png|center|200]]

Nella logica del primo ordine, in aggiunta alle $\alpha$-formule e $\beta$-formule, abbiamo anche le formule che coinvolgono i quantificatori: per esempio, $\forall xP (x)$ e $\exists xP (x)$. 
Quali saranno le regole di estensione dei tableaux per questi tipi di formule? Vediamo.

![[appunti lrl/immagini/Pasted image 20230419152206.png|center|200]]

Un momento. . . la stessa regola per entrambi? Non può essere. . . infatti manca ancora qualcosa, ma prima di andare a vedere cosa manca riflettiamo un attimo sul significato delle due regole qui sopra. La prima traduce il ragionamento seguente: se è vero che la proprietà P vale per ogni elemento del dominio $[ossia, \forall xP (x)]$ allora prendiamo un elemento a per cui la proprietà P vale $[ossia, P (a)]$. La seconda, questo: se è vero che deve esistere un elemento del dominio per cui vale la proprietà P $[ossia, \exists xP (x)]$, allora prendiamo un elemento a per cui la proprietà P vale $[ossia, P (a)]$. Entrambi i ragionamenti sembrano corretti. Allora, cos’è che manca?

Quando incontriamo per la prima volta una formula del tipo $\exists xP (x)$ e aggiungiamo $P (a)$ al nostro tableau, questo è perfettamente legittimo, per il ragionamento che abbiamo fatto sopra. Ma immaginate che poi nel nostro percorso di scomposizione troviamo un’altra formula del tipo $\exists xQ(x)$. E' legittimo aggiungere al nostro tableau $Q(a)$? Beh, riflettete un attimo sul fatto che la risposta è no, non è legittimo: perch è anche se esiste un elemento del dominio per cui vale la proprietà Q, questo elemento non è necessariamente lo stesso per cui vale la proprietà P . Quindi in questo caso dobbiamo istanziare la proprietà Q su un altro elemento, diciamo b.
E se dopo aver esteso $\exists xP (x)$ con $P (a)$ incontriamo una formula del tipo $\forall xQ(x)$?  
Abbiamo lo stesso problema? Beh, no, perch ́e siccome Q vale per tutti gli elementi del dominio, varrà anche per l’elemento a per cui vale la proprietà P .  
Quindi, possiamo completare le nostre regole in questo modo

![[appunti lrl/immagini/Pasted image 20230419152800.png|center|350]]

Oltre a quelle qui sopra, dobbiamo stabilire altre due regole: una per $\neg\exists xP (x)$ l’altra per $\neg\forall xP (x)$

Osservate che le formule $\forall xP (x)$ e $\neg\exists xP (x)$ sono di tipo _**universale**_, cioè si riferiscono a tutti gli elementi del dominio. Invece le formule $\exists xP (x)$ e $\neg\forall xP (x)$ sono di tipo _**esistenziale**_, cioè si riferiscono ad almeno uno degli elementi del dominio.  
In analogia con quanto fatto per le formule della logica proposizionale, possiamo quindi classificare le formule della logica del primo ordine che coinvolgono i quantificatori in due categorie: le $\gamma$-formule (quelle di tipo _universale_) e le $\delta$-formule (quelle di tipo _esistenziale_) con le relative regole di estensione dei tableaux.

![[appunti lrl/immagini/Pasted image 20230419153120.png|center|500]]

Come nel caso della logica proposizionale, diciamo che un ramo di un tableau è chiuso se sul ramo c’è sia una formula che la sua negata. Diciamo che un tableau è chiuso se tutti i suoi rami sono chiusi e diciamo che una formula $\mathcal F$ è dimostrabile col metodo dei tableaux se partendo da $\neg\mathcal F$ e applicando le regole per le $\alpha, \beta, \gamma, \delta$ formule riusciamo a ottenere un tableau chiuso.

# Esempio

**Esempio 1**

Consideriamo la formula 
$$\forall xP (x) \to \exists x P (x)$$
Nell’episodio precedente, ragionando intuitivamente abbiamo osservato che è impossibile trovare una interpretazione che la rende falsa, quindi la formula è valida. Facciamo vedere che è dimostrabile col metodo dei tableaux

![[appunti lrl/immagini/Pasted image 20230421141726.png|center|300]]

Le formule (2) e (3) vengono dalla (1) applicando la regola $\alpha$, la (4) viene dalla (2) tramite la regola $\gamma$ e la (5) dalla (3) sempre tramite la regola $\gamma$. La (4) e la (5) sono in contraddizione quindi il tableau, che ha un unico ramo, è chiuso.

**Esempio 2**

Consideriamo la formula

$$\exists x(P (x) \land Q(x)) \to \exists xP (x) \land \exists xQ(x)$$
Vediamo che è dimostrabile col metodo dei tableaux

![[appunti lrl/immagini/Pasted image 20230421141940.png|center|350]]

Le formule (2) e (3) vengono da (1) (regola $\alpha$), la (4) dalla (2) (regola $\delta$), (5) e (6) da (4) (regola $\alpha$), (7) e (8) da (3) (regola $\beta$), infine (9) e (10) da (7) e (8) rispettivamente (entrambe regole $\gamma$). Le formule (9) e (5) sono in contraddizione, così come le formule (10) e (6). Quindi entrambi i rami sono chiusi. La formula è dimostrata

**Esempio 3**

Consideriamo la seguente formula
$$\exists y[P (y) \to \forall xP (x)]$$
Pensate che sia valida oppure no? Intanto vediamo che è dimostrabile

![[appunti lrl/immagini/Pasted image 20230421142235.png|center|300]]

La (2) viene dalla (1) (regola $\gamma$), (3) e (4) vengono dalla (2) (regola $\alpha$). La (5) viene dalla (4) (regola $\delta$), ma osservate che non ho potuto mettere $\neg P (a)$ e trovare una contraddizione con la (3), perchè la (4) è di tipo esistenziale, quindi devo usare un parametro che non ho già usato prima. Quindi? Il tableau non si chiude e la formula non è dimostrabile?

La formula (1) è di tipo universale, quindi posso riusarla con un altro parametro!

![[appunti lrl/immagini/Pasted image 20230421142534.png|center|300]]

La (6) viene dalla (1), la (7) e la (8) vengono dalla (6) e non c’è bisogno di proseguire sviluppando la (8) perch è la (7) e la (5) sono in contraddizione e il tableau è chiuso.

# Conclusioni

In questo episodio abbiamo visto come si estende il metodo dei tableaux alla logica del  
primo ordine. Sono sicuro che sapete già cosa ci aspetta nel prossimo episodio. . . Dobbiamo dimostrare che il metodo è corretto (ogni formula dimostrabile col metodo dei tableaux è valida) e completo (ogni formula valida è dimostrabile col metodo dei tableaux ).



