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





