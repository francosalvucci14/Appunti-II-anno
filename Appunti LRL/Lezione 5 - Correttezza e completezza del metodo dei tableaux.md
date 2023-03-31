
# Insiemi soddisfacibili e correttezza del metodo

Diciamo che una formula $\mathcal F$ è soddisfacibile se esiste una interpretazione in cui è T (osser-  
vate che una formula è soddisfacibile se e solo se è o una tautologia o una contingenza).  

Diciamo che un insieme S di formule è soddisfacibile, se esiste una interpretazione in cui  
tutte le formule di S sono T

**Esercizio 1**

Nell’episodio precedente abbiamo visto che una formula $\mathcal F$ della logica proposizionale  
può essere soltanto di due tipi: una $\alpha$-formula o una $\beta$-formula (con una eccezione,  
l’equivalenza $\equiv$, che però abbiamo visto che può essere spezzata a sua volta in due  
formule, una di tipo $\beta$ e una di tipo $\alpha$)

![[appunti lrl/immagini/Pasted image 20230331155648.png|center|350]]

Se F è una $\alpha$-formula (rispettivamente, $\beta$-formula) chiamiamo le formule $\alpha_1$ e $\alpha_2$ (rispettivamente, $\beta_1$ e $\beta_2$) le componenti della formula $\mathcal F$.

**Esercizio 2 e 3**

Ricordiamo che con il metodo dei tableaux quello che facciamo è costruire una sequenza  
$T_0, T_1, T_2,\dots$ di tableaux, in cui ogni $T_i$ è ottenuto “estendendo” il precedente $T_{i−1}$ tramite  
una “regola $\alpha$” o una “regola $\beta$”

![[appunti lrl/immagini/Pasted image 20230331160114.png|center]]

a seconda che la formula che si sta espandendo sia una $\alpha$-formula o una $\beta$-formula.  
Per esempio, con riferimento al caso visto in dettaglio nella prima parte dell’episodio precedente, dove abbiamo applicato il metodo dei tableaux alla formula $\mathcal F = ((p\land q)\implies r)\implies(\neg p\lor(q\implies r))$, il primo tableau $T_0$ è la negazione di $\mathcal F$

![[appunti lrl/immagini/Pasted image 20230331160524.png|center]]

Siccome la (1) è una $\alpha$-formula, $T_1$ è ottenuto estendendo $T_0$ tramite una regola $\alpha$

![[appunti lrl/immagini/Pasted image 20230331150320.png|center]]

Siccome la (2) è una $\beta$-formula, $T_2$ è ottenuto estendendo $T_1$ tramite una regola $\beta$

![[appunti lrl/immagini/Pasted image 20230331150538.png|center]]

Ad ogni “ramo” $\theta$ di un tableau possiamo associare l’insieme $S_{\theta}$ di tutte le formule che  
compaiono su quel ramo. 
Per esempio, nel tableau qui sopra ci sono due rami, uno contiene le formule (1), (2), (3) e (4), l’altro contiene le formule (1), (2), (3) e (5). 

Diciamo che un ramo $\theta$ è soddisfacibile se l’insieme $S_\theta$ delle sue formule è soddisfacibile.  

Diciamo che un tableau T è soddisfacibile, se almeno uno dei suoi rami è soddisfacibile.

**Esercizio 4**

Diciamo che un ramo è chiuso se contiene sia una formula $\mathcal F$ sia la sua negata $\neg\mathcal F$. 
In caso contrario diciamo che è aperto. Diciamo che un tableau è chiuso se tutti i suoi rami  
sono chius

**Esercizio 5**

Ricordiamo che una formula $\mathcal F$ si dice dimostrabile con il metodo dei tableaux se  
c’è un tableau T chiuso per $\neg\mathcal F$. 
In questo caso diciamo anche che il tableau T è una dimostrazione di $\mathcal F$ e che $\mathcal F$ è un teorema nel sistema dei tableaux.  

A questo punto possiamo facilmente dimostrare che ogni formula della logica proposizionale dimostrabile col metodo dei tableaux è una tautologia.

>[!definition]- Teorema 1.1 (Correttezza)
>Se $\mathcal F$ è dimostrabile con il metodo dei tableaux allora è una tautologia.

**Dimostrazione**. Se $\mathcal F$ non fosse una tautologia, allora $\neg\mathcal F$ sarebbe soddisfacibile. 
Quindi ogni tableau che si ottiene da $\neg\mathcal F$ dovrebbe essere soddisfacibile (per l’Esercizio 4). Ma questo è assurdo perchè per ipotesi $\mathcal F$ è dimostrabile col metodo dei tableaux, quindi c’è un tableau chiuso per $\neg\mathcal F$.

# Insiemi di Hitikka e completezza del metodo

Per dimostrare la correttezza del metodo abbiamo usato la definizione di insiemi di formu-  
le soddisfacibili. Per dimostrarne la completezza introduciamo un’altra classe di insiemi  
di formule, che chiamiamo insiemi di Hintikka dal nome del filosofo che li ha utilizzati  
per primo.

>[!definition]- Definizione 2.1 (Insiemi di Hitikka)
>Un insieme di formule S per cui valgono le tre proprietà seguenti si chiama insieme di Hintikka: 
>- $H_0$ : S non contiene sia una variabile $p$ che la sua negata $\neg p$;  
>- $H_1$ : Se S contiene una $\alpha$-formula, allora S contiene anche entrambe le sue componenti $\alpha_1$ e $\alpha_2$;  
>- $H_2$ : Se S contiene una $\beta$-formula allora S contiene anche almeno una delle sue componenti $\beta_1$ e $\beta_2$

**Esercizio 6**

Diciamo che un tableau è completo se è chiuso, oppure se ogni formula $\mathcal F$ (che non sia  
una variabile o una variabile negata) sui rami aperti del tableau è stata espansa. Per  
esempio, il tableau in alto nella pagina precedente non è completo, perchè le formule (3)  
e (4) non sono state espanse.

**Esercizio 7**

A questo punto abbiamo tutto quello che ci serve per dimostrare che ogni tautologia è dimostrabile col metodo dei tableaux.

>[!definition]- Teorema 2.2 (Completezza). 
>Se F è una tautologia allora è dimostrabile con il metodo dei tableaux.  

**Dimostrazione**. Se non fosse dimostrabile allora partendo da $\neg\mathcal F$ ed espandendo tutte  
le formule si otterrebbe un tableau completo con almeno un ramo aperto $\theta$. 
L’insieme delle formule sul ramo $\theta$ quindi sarebbe un insieme di Hintikka (per l’Esercizio 7). Ma ogni insieme di Hintikka è soddisfacibile (per l’Esercizio 6). Quindi in particolare sarebbe  
soddisfacibile la formula $\neg\mathcal F$, che è assurdo perchè per ipotesi $\mathcal F$ è una tautologia.

# Conclusioni

L’insieme delle tautologie è definito in termini semantici (una tautologia è una formula  
“vera” in ogni interpretazione). In questo episodio abbiamo analizzato il metodo dei  
tableaux e abbiamo visto che, facendo soltanto operazioni sintattiche sulle formule (ap-  
plicazioni delle regole $\alpha$ e $\beta$), ci consente di decidere se una data formula è una tautologia oppure no.
Perchè questo è importante per noi informatici? Beh, osservate che è difficile  
spiegare a un computer come distinguere ciò che è vero da ciò che è falso, ma è facile  
fargli eseguire delle istruzioni. . .  
Il metodo dei tableaux è un metodo di refutazione: per dimostrare che $\mathcal F$ è una  
tautologia, partiamo da $\neg\mathcal F$ e verifichiamo che non è soddisfacibile (si noti l’analogia con  
le dimostrazioni per assurdo).