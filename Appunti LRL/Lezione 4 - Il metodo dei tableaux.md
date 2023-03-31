
# Antipasto

Sia $\mathcal F$ la formula seguente
$$((p\land q)\implies r)\implies(\neg p\lor(q\implies r))$$
$\mathcal F$ è una tautologia? Basta fare la tabella, ma ora usiamo un'altro ragionamento

1. Prendiamo la sua negazione $\neg\mathcal F$ $$\neg[((p\land q)\implies r)\implies(\neg p\lor(q\implies r))]\space(1)$$e prima di tutto osserviamo che la formula (1) è vera in qualche interpretazione se e solo se $\mathcal F$ non è tautologia. _Quindi per vedere se $\mathcal F$ non è una tautologia possiamo dimenticarci di $\mathcal F$ e vedere se esiste una interpretazione che rende la (1) vera_.
2. La formula (1) è del tipo $\neg[\mathcal F_1\implies\mathcal F_2]$, dove $\mathcal F_1=((p\land q)\implies r)$ e $\mathcal F_2=\neg p\lor(q\implies r)$ Quindi è vera se e soltanto se $\mathcal F_1$ è vera e $\mathcal F_2$ è falsa, ossia se e soltanto se $\mathcal F_1$ e $\neg\mathcal F_2$ sono entrambe vere. La formula (1) quindi è vera se e solo se sono vere entrambe le formule (2) e (3) qui sotto ![[appunti lrl/immagini/Pasted image 20230331150320.png|center]]Quindi per vedere se esiste un’interpretazione che rende (1) vera, possiamo dimenticarci di (1) e vedere se esite una interpretazione che rende vere _entrambe_ (2) e (3).
3. Passiamo a considerare (2): è una implicazione, quindi è vera quando o $(p \land q)$ è falso oppure quando r è vero. In altre parole, quando almeno una è vera, fra le due formule (4) ed (5) qui sotto ![[appunti lrl/immagini/Pasted image 20230331150538.png|center]]Si osservi che (4) e (5) non le abbiamo messe una sotto l’altra, come avevamo fatto con (2) e (3), ma abbiamo creato due “rami”. Questo perch ́e per vedere se esiste una interpretazione che rende vere sia (2) che (3), possiamo dimenticarci di (2) e vedere se esiste un’interpretazione che rende vera (3) e _almeno una_ fra (4) e (5)
4. Andiamo a considerare (3): è la negazione di un or, quindi è vera se e solo se $\neg p$ e $(q\implies r)$ sono entrambe false, in altre parole, quando entrambe le formule (6) e (7) qui sotto sono vere ![[appunti lrl/immagini/Pasted image 20230331150830.png|center]]Si osservi che (6) e (7) le abbiamo messe una sotto l’altra e ripetute sotto entrambi i rami. Infatti, per vedere se esiste una interpretazione che rende vera (3) e almeno una fra (4) e (5), possiamo dimenticarci di (3) e vedere se esiste una interpretazione che rende vere (4), (6) e (7), oppure (5), (6) e (7)
5. Andiamo a (4): è la negazione di un and, quindi è vera quando almeno una delle due fra p e q è falsa, ossia quando o la (8) è vera oppure la (9) è vera ![[appunti lrl/immagini/Pasted image 20230331150946.png|center]]Per vedere se esiste una interpretazione che rende vere (4), (6) e (7) perciò possiamo dimenticarci di (4) e vedere se esiste una interpretazione che rende vere (6), (7) e (8), oppure (6), (7) e (9). Tuttavia, una interpretazione che renda vere (6), (7), e (8) non può esistere, perchè per rendere vera (6) la variabile p dovrebbe essere T mentre per rendere vera (8) dovrebbe essere F. Diciamo che quel ramo è chiuso e nello schema ho indicato questo fatto con una X. Per vedere se esiste un’interpretazione che rende vere (6), (7) e (9) dobbiamo ancora procedere fino a scomporre la (7).
6. Per quanto riguarda le formule (5) e (6), sono già delle variabili quindi non c’è più niente da scomporre. Ci resta da considerare la formula (7): è la negazione di un’implicazione, quindi...![[appunti lrl/immagini/Pasted image 20230331151140.png|center]]Anche il secondo e il terzo ramo si chiudono: il secondo perch ́e non può esistere una interpretazione che renda vere entrambe le formule (9) e (10), il terzo perch ́è non può esisere una interpretazione che renda vere entrambe le formule (5) e (11).

Non c’è più niente da scomporre e abbiamo un albero con tutti i rami chiusi. Che cosa  
significa? Torniamo un attimo indietro e vediamo di ripercorrere quello che abbiamo  
fatto con riferimento al nostro schema di formule

- Avevamo la nostra formula $\mathcal F$ e volevamo scoprire se è una tautologia oppure no. Siamo partiti da $\neg\mathcal F$, la formula (1), e abbiamo osservato che $\mathcal F$ non è una tautologia se e solo se esiste un’interpretazione che rende T la formula (1).
- Esiste un’interpretazione che rende T la formula (1) se e solo se esiste un’interpretazione che rende T entrambe le formule (2) e (3) $$\{(\text{2 e 3})\}$$
- Esiste un’interpretazione che rende T la formula (2) se e solo se esiste un’interpretazione che rende T la formula (4) o la formula (5) $$\{\text{(3 e 4) oppure (3 e 5)}\}$$
- Esiste un’interpretazione che rende T la formula (3) se e solo se esiste un’interpretazione che rende T entrambe le formule (6) e (7)
$$\{\text{(4, 6 e 7) oppure (5, 6 e 7)}\} $$ 
- Esiste un’interpretazione che rende T la formula (4) se e solo se esiste un’interpretazione che rende T la formula (8) o la formula (9)  
$$\{\text{(6, 7 e 8) oppure (6, 7 e 9) oppure (5, 6 e 7)}\}$$
- Non esiste nessuna interpretazione che rende T sia la formula (6) che la formula (8).  
$$\{\text{(6, 7 e 9) oppure (5, 6 e 7)}\}$$  
- Esiste un’interpretazione che rende T la formula (7) se e solo se esiste un’interpretazione che rende T entrambe le formule (10) e (11)  
$$\{\text{(6, 9, 10, e 11) oppure (5, 6, 10 e 11)}\}$$  
- Non esiste nessuna interpretazione che rende T sia la formula (9) che la formula (10).  
$$\{\text{(5, 6, 10 e 11)}\}$$  
- Non esiste nessuna interpretazione che rende T sia la formula (5) che la formula (11).$$\emptyset$$
Quindi non esiste nessuna interpretazione che renda la (1) vera. Perciò tutte le interpretazioni rendono vera $\mathcal F$.

**Esercizio 1**

# Le regole del gioco

Nell’ esempio visto in dettaglio nella sezione precedente, abbiamo costruito un “albero” (il  
tableaux) in cui, scendendo dalla radice $\neg\mathcal F$ alle foglie troviamo via via formule con meno  
simboli, fino ad arrivare a formule che sono o variabili o variabili negate. Ogni volta che  
abbiamo “sviluppato” una formula in formule più semplici, l’abbiamo fatto preservandone  
la soddisfacibilità (l’esistenza di interpretazioni che rendono vere le formule).

Cerchiamo ora di derivare le regole che ci consentono di costruire “meccanicamente”  
un tableaux come quello della sezione precedente per ogni formula $\mathcal F$, in modo da poter  
eventualmente istruire un computer a farlo per noi.[^1]  
Osserviamo che ogni formula ben formata $\mathcal F$ che non è una variabile o una variabile negata è sempre, tranne un paio di casi particolari, equivalente all’AND di due formule o all’OR di due formule. 

Per esempio, $\mathcal F_1\implies\mathcal F_2$ è equivalente a $\neg\mathcal F_1\lor\mathcal F_2$ mentre $\neg(\mathcal F_1 \implies \mathcal F_2)$ è equivalente a $\mathcal F_1\land\neg\mathcal F_2$.  

Nella costruzione del tableaux si procede come segue: se abbiamo una formula $\alpha$ equivalente all’AND di due formule $\alpha_1\land\alpha_2$, la sostituiamo con $\alpha_1$ e $\alpha_2$, messe una sotto l’altra,  
mentre se abbiamo una formula $\beta$ equivalente all’OR di due formule $\beta_1\lor\beta_2$, la sostuiamo  
con due “rami”, uno con $\beta_1$ e l’altro con $\beta_2$

![[appunti lrl/immagini/Pasted image 20230331153931.png|center|300]]
**Esercizi da 2 a 7**

# Conclusioni

In questo episodio abbiamo studiato un metodo automatico per costruire un albero (ta-  
bleau) a partire da una formula $\neg\mathcal F$ della logica proposizionale. 

Siccome ogni volta che applichiamo una regola otteniamo formule con meno simboli, il metodo termina sempre dopo un numero finito di applicazioni delle regole. Abbiamo definito una formula $\mathcal F$ dimostrabile con il metodo dei tableaux se, quando non ci sono più formule a cui appplicare le regole, il tableaux risultante a partire da $\mathcal F$ ha tutti i rami _chiusi_.


