
# L'Halting Problem

## Macchine=parole=numeri

Siamo a pag. 11 della dispensa 2: avevamo descritto una macchina di Turing T 
- con alfabeto $\{0,1\}$, 
- insieme degli stati $Q_T = \{\omega_0,\dots,\omega_{k-1}\}$ , con stato iniziale $\omega_0$, stato di accettazione $\omega_1$, e stato di rigetto $\omega_2$ – osservate: $|Q_T|=k$
- e insieme delle quintuple $P = \{p_1,\dots, p_h\}$ , dove la sua i-esima quintupla è $$ p_i = \langle \omega_{i_1} ,b_{i_1} , b_{i_2} , \omega_{i_2} , m_i \rangle$$
mediante la parolona 
- $$\begin{align}\rho_T &= \omega_0 - \omega_1\otimes \omega_{1_1} - b_{1_1} - b_{1_2} - \omega_{1_2} - m_1\oplus \omega_{2_1} - b_{2_1} - b_{2_2} - \omega_{2_2} - m_2 \oplus\\&\dots\oplus \omega_{h_1} - b_{h_1} - b_{h_2} - \omega_{h_2} - m_h \oplus\end{align}$$

Poi, a pag. 13 (dispensa 2) avevamo introdotto una codifica binaria $b^Q$ dell’insieme $Q_T$ degli stati di T, che, nella lezione 4, avevamo semplificato come segue:
- $b^Q : Q_T  \to \{ 0,1 \}^k$, ossia, la codifica $b^Q$ rappresenta uno stato di T mediante una parola di k bit
- $b^Q(\omega_i)$ è la parola che ha un 1 in posizione i+1 e 0 altrove

A questo punto, avevamo rappresentato T mediante la seguente parolona nell’alfabeto $\Sigma = \{0, 1, \oplus, \otimes, -, f , s, d\}$ :
 - $$\begin{align}&b^Q(\omega_0) - b^Q( \omega_1) \otimes b^Q(\omega_{1_1}) - b_{11} - b_{12} - b^Q(\omega_{12}) - m_1 \oplus b^Q(\omega_{21}) - b_{21} - b_{22} - \\&b^Q(\omega_{22}) - m_2 \oplus\dots\oplus b^Q(\omega_{h1}) - b_{h1} - b_{h2} - b^Q(\omega_{h2}) - m_h\oplus 
\end{align}$$
Quello che viene fatto nel paragrafo 5.1 (dispensa 5) è trasformare la parola  in un numero sostituiamo in  :
- ogni carattere ‘s’  con il carattere ‘5’, ogni carattere ‘f’ con il carattere ‘6’, e ogni carattere ‘d’ con il carattere ‘7’; 
- ogni carattere '$-$' con il carattere ‘4’, ogni carattere ‘$\oplus$’ con il carattere ‘3’ e ogni carattere ‘$\otimes$’ con il carattere ‘2’; 
- ogni carattere ‘$\square$’ con il carattere ‘9’;

Infine, premettiamo il carattere ‘8’ alla parola ottenuta. 

A questo punto quello che abbiamo ottenuto è un numero intero

Abbiamo associato ad ogni macchina di Turing un numero intero
- e l’associazione è univoca: a macchine di Turing diverse sono associati interi diversi
- o, equivalentemente, un intero non può corrispondere a due macchine di Turing 

Cioè, abbiamo visto come rappresentare le macchine di Turing mediante numeri naturali

## Problemi irrisolvibili

Turing considerò il seguente linguaggio, sottoinsieme di $\mathbb N\times\mathbb N$:                              																		      			$$L_H = \{ (i,x) : \text{i è la codifica di una macchina di Turing} \space T_i\land T_i(x)\space termina \}$$

Che si chiama **_Halting Problem_**

Turing dimostrò che 
- $L_H$ è accettabile
- e dimostrò anche che $L_H$ non è decidibile

Ma prima cerchiamo di capire che senso ha domandarsi, data $(i,x)\in\mathbb N\times\mathbb N$ , se $(i,x)\in  L_H$    

### A chi importa dell'Halting Problem?

Sei informatico, ti capiterà, qualche volta nella vita, di scrivere un programma
complicatissimo

Bene, dopo tutta questa fatica, lanci il tuo programma su un certo input x
- x è un’istanza del problema risolto dal tuo programma della quale è importantissimissimo calcolare la soluzione!
e attendi la risposta…
... e attendi ...
... e attendi ...

Ti viene un dubbio atroce: e se fosse andato in loop?!

Certo sarebbe bello se esistesse un programma che, se gli do in input un altro programma P e un suo input x, quello mi dice se  l’esecuzione di P su x termina oppure no
- ovvero, un programma che decide l’Halting Problem

## Ritornando a Problemi Irrisolvibili

Dimostriamo che: 
- $L_H$ è accettabile
- e dimostrò anche che $L_H$ non è decidibile

### $L_h$ è accettabile - Teorema 5.4

Questo è facile: si prende la macchina Universale U e si fanno un paio di modifiche - trasformandola nella macchina U’:
- la prima modifica serve a fare in modo che U’ verifichi se l’input i scritto sul suo primo nastro è davvero la codifica di una macchina di Turing $T_i$
	- se non è così, U’(i,x) rigetta
- La seconda modifica, serve a fare in modo che, se i è la codifica di una macchina di Turing $T_i$ , U’ accetti la coppia (i,x) ogni qualvolta $T_i (x)$  termina, ossia, sia nel caso in cui accetta sia nel caso in cui rigetta:
	- accertato che i è la codifica di una macchina di Turing $T_i$, U’(i,x) simula U(i,x) e 
		- se U(i,x) accetta allora U’(i,x) accetta
		- se U(i,x) rigetta allora U’(i,x) accetta

Quindi U’(i,x) accetta tutte e sole le coppie (i,x) che appartengono a $L_H$ – ossia, $L_H$ è accettabile

### $L_h$ non è decidibile - Teorema 5.5

La dimostrazione è per assurdo: supponiamo che $L_H$ sia decidibile

Se $L_H$ è decidibile, allora esiste una macchina T tale che, per ogni (i,x):
$$T(x)=\begin{cases}q_A\iff(i,x)\in L_h\\q_R\iff(i,x)\not\in L_h\end{cases}$$

Ebbene, se abbiamo T, possiamo utilizzare T per costruire una nuova macchina T’ tale che:
$$T'(x)=\begin{cases}q_A\iff(i,x)\not\in L_h\\q_R\iff(i,x)\in L_h\end{cases}$$
Come è fatta T’? Beh, prendiamo T, la smontiamo e invertiamo gli stati di accettazione e di rigetto.

Ora, di nuovo con la “tecnica della scatola nera”, a partire da T’, costruiamo una macchina T’’, che:
$$T''(x)=\begin{cases}q_A\iff(i,x)\not\in L_h\\\text{non termina}\iff(i,x)\in L_h\end{cases}$$

è sufficiente aggiungere una quintupla che manda in loop la macchina

Compreso che come input di T, T’ e T’’ possiamo usare una coppia (i,x) tale che x=i, di nuovo con la “tecnica della scatola nera”, a partire da T’’, costruiamo un’ultima macchina $T^\star$ che lavora con un solo input e tale che l’esito della computazione $T^\star( i )$ coincide con l’esito della computazione $T''( i, i )$

Ossia, se i è la codifica di una macchina di Turing, allora
- $T^\star( i )$ accetta se $( i, i )\not\in L_h$ , ossia se $T_i ( i )$ non termina, 
- $T^\star( i )$ non termina se $( i, i )\in L_h$ , ossia se $T_i ( i )$ termina

Poiché abbiamo supposto che T esiste, allora anche $T^\star$ esiste

E, se $T^\star$ esiste, allora la posso codificare come intero – lo abbiamo visto all’inizio di questa lezione

Chiamiamo k il codice di $T^\star$ ottenuto applicando il procedimento illustrato all'inizio di questa lezione

Cioè, $T^\star = T_k$

Ma k è un intero

Allora, k può essere input di $T^\star$ - ossia, input di $T_k$

Quindi possiamo considerare la computazione $T_k ( k )$

E quindi, quale è l’esito della computazione $T^\star( k ) = T_k ( k )$?

Abbiamo due casi :  $T^\star( k ) = T_k ( k )$ o accetta oppure non termina

1. Se $T^\star( k ) = T_k ( k )$ accetta, abbiamo che $( k, k )\not\in L_h$ , e quindi $T_k(k)=q_A\iff T^\star( k ) = T_k ( k )$ non termina (assurdo)

2. Se $T^\star( k ) = T_k ( k )$ non termina , abbiamo che $( k, k )\in L_h$ ,e quindi $T^\star( k ) = T_k ( k )$ non termina solo se $T^\star( k ) = T_k ( k )$ termina (assurdo)

Ma, dato che la computazione $T^\star( k ) = T_k ( k )$ non può esistere, questo significa che $T^\star$ **non** esiste

E quindi, se $\not\exists T^\star\implies\not\exists T''\implies\not\exists T'$ e quindi $L_h$ non è decidibile
