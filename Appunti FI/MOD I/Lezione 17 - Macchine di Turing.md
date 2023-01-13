# Macchine di Turing a nastro singolo

Dispositivo che accede ad un **nastro** potenzialmente illimitato diviso in celle contenenti ciascuna un simbolo appartenente a un alfabeto $\Gamma$, ampliato con il carattere speciale $\square$ (blank)  che rappresenta la situazione di cella non contenente caratteri.

All'inizio del calcolo solo una porzione finita del nastro contiene simboli di $\Gamma$. La macchina di Turing opera su tale nastro tramite una testina, la quale può scorrere su di esso in entrambe le direzioni.
Su ogni cella la testina può leggere o scrivere caratteri appartenenti all'alfabeto $\Gamma$ oppure il simbolo $\square$

![[appunti fi/mod i/immagini/Pasted image 20230109112412.png|center|500]]

## Macchina di Turing deterministica

Sestupla $\mathcal M=\langle\Gamma,\square,Q,q_0,F,\delta\rangle$ dove:
- $\Gamma$: alfabeto dei simboli di nastro
- $\square\not\in\Gamma$: carattere speciale denominato **blank**
- $Q$: insieme finito e non vuoto di **stati**
- $q_0\in Q$: **stato iniziale**
- $F\subseteq Q$: insieme degli **stati finali**
- $\delta$: funzione di transizione definita come $$\delta:(Q-F)\times(\Gamma\cup\{\square\})\to Q\times(\Gamma\cup\{\square\})\times(\to,\leftarrow,\circ)$$ in cui $\to,\leftarrow,\circ$ indicano rispettivamente, lo spostamento a destra, a sinistra o l'immobilità della testina

**Esempio**

![[appunti fi/mod i/immagini/Pasted image 20230109121029.png|center|500]]

### DTM (Deterministic Turing Machine)

- DTM utilizzabili per il calcolo di funzioni, o per riconoscere o accettare stringhe su un alfabeto di input $\Sigma\subseteq\Gamma$
- DTM usate per accettare stringhe vengono dette di tipo _riconoscitore_
- DTM usare per calcolare funzioni vengono dette di tipo _trasduttore_
- In entrambi i casi, all'inizio del calcolo, solo una porzione finita del nastro contiene simboli diversi da blank che costituiscono l'input del calcolo stesso

#### Configurazione di una DTM

SI definisce configurazione istantaneta o configurazione di una macchina di Turing con alfabeto di nastro $\Gamma$ ed insieme degli stati $Q$, una stringa $c=xqy$, con (assumendo $\overline\Gamma=\Gamma\cup\{\square\}$):

1. $x\in\Gamma\overline\Gamma^\star\cup\{\varepsilon\}$
2. $q\in Q$
3. $y\in\overline\Gamma^\star\Gamma\cup\{\square\}$

L'interpretazione data ad una stringa $xqy$ è che $xy$ rappresenti il contenuto della sezione non vuota del nastro, che lo stato attuale sia $q$ e che la testina sia posizionata sul primo carattere di $y$. Nel caso in cui $x=\varepsilon$ abbiamo che a sinistra della testina compaiono solo simboli $\square$, mentre se $y=\square$ sulla cella attuale e a destra della testina compaiono soltanto simboli $\square$

##### Configurazione iniziale

La configurazione iniziale di MT rispetto a una stringa di input $\sigma$ prevede che:

- il nastro contenga la stringa $\sigma$ in una sequenza di celle
- tutte le altre celle del nastro siano vuote (contengano $\square$)
- lo stato attuale sia lo stato iniziale $q_0$
- la testina si trovi sulla cella contenente il primo carattere di $\sigma$

Una configurazione $xqy$ è quindi iniziale se $x=\varepsilon,q=q_0,y=\sigma$

##### Configurazione finale

Una configurazione $c=xqy$ si dice **finale** se $q\in F$

Quindi, una macchina di Turing si trova in una configurazione finale se il suo stato attuale è lo stato finale, indipendentemente dal contenuto del nastro e dalla posizione della testina

#### Matrice di transizione

La funzione di transizione può essere rappresentata mediante **matrici di transizione** e **grafi di transizione**

**Esempio**

![[appunti fi/mod i/immagini/Pasted image 20230110110553.png|center|500]]

In generale, assumiamo che uno stato finale non abbia transizioni uscenti definite.

#### Grafo di transizione

![[appunti fi/mod i/immagini/Pasted image 20230110110701.png|center|600]]

**Esercizio**

Considerata la macchina di Turing deterministica definita sopra e assumendo la configurazione iniziale $q_010$:

1. determinare la computazione effettuata dalla macchina, indicando la configurazione finale che viene raggiunta
2. descrivere informalmente il comportamento della macchina su un input generico

#### Accettazione e rifiuto di stringhe

- **Computazione massimale**: computazione che non può prolungarsi (non esistono transizioni applicabili alla configurazione raggiunta)
- **Computazione di accettazione**: computazione massimale che termina in una configurazione finale
- **Computazione di rifiuto**: computazione massimale che si conclude in una configurazione non finale

Dato un alfabeto di input $\Sigma\subseteq\Gamma$, una stringa $x\in\Sigma^\star$ è _accettata (rifiutata)_ da una MT $\mathcal M$ se esiste una computazione di accettazione (di rifiuto) di $\mathcal M$ con $c_0=q_0x$

- Terza possibilità: non esiste alcuna computazione massimale con $c_0=q_0x$; in altre parole, la computazione di $\mathcal M$ su input x non termina

Data una MT $\mathcal M$ con alfabeto di input $\Sigma$, l'insieme $\Sigma^\star$ è partizionato in tre linguaggi:

- L'insieme $L(\mathcal M)$ delle stringhe **accettate** da $\mathcal M$
- L'insieme $\overline L(\mathcal M)$ delle stringhe **rifiutate** da $\mathcal M$
- L'insieme $\Sigma^\star-(L(\mathcal M)\cup\overline L(\mathcal M))$ delle stringhe sulle quali la computazione effettuata da $\mathcal M$ non termina

**Definizioni equivalenti**

1. esistono due soli stati finali, $q_1,q_2$, tutte le computazioni massimmali terminano in uno stato finale ed una stringa x è accettata se $q_0x\vdash_{\mathcal M}^\star wq_1z$, mentre è rifiutata se $q_0x\vdash_{\mathcal M}^\star wq_2z$
2. esiste un solo stato finale $q_F$, l'alfabeto di nastro contiene due simboli speciali $Y,N\not\in\Sigma$ (Y=yes, N=no), tutte le computazioni massimali terminano nello stato finale ed una stringa x è accettata se $q_0x\vdash_{\mathcal M}^\star q_FY$, mentre è rifiutata se $q_0x\vdash_{\mathcal M}^\star q_FN$

#### Riconoscimento di linguaggi

- Data una MT deterministica $\mathcal M=\langle\Gamma,\square,Q,q_0,F,\delta\rangle$ 
- Dato un alfabeto di input $\Sigma\subseteq\Gamma$
- $\mathcal M$ **riconosce (decide)** un linguaggio $L\in\Sigma^\star$ se e solo se per ogni $x\in\Sigma^\star$:
	- esiste una computazione massimale $q_0x\vdash_{\mathcal M}^\star wqz$
	- $q\in F$ se e solo se $x\in L$
	- $w\in\Gamma\overline\Gamma^\star\cup\{\varepsilon\}$ e $z\in\overline\Gamma^\star\Gamma\cup\{\square\}$ rappresentano il contenuto delle porzioni di nastro significative prima e dopo la posizione della testina
- Afficnhè un linguaggiosia riconosciuto, $\mathcal M$ deve fermarsi per ogni $x\in\Sigma^\star$

#### Accettazione di linguaggi

- Data una MT deterministica $\mathcal M=\langle\Gamma,\square,Q,q_0,F,\delta\rangle$ 
- Dato un alfabeto di input $\Sigma\subseteq\Gamma$
- $\mathcal M$ **accetta** un linguaggio $L\in\Sigma^\star$ se e solo se: $L=\{x\in\Sigma^\star|q_0x\vdash_{\mathcal M}^\star wqz;q\in F\}$
- Quindi, L è l'insieme delle stringhe per le quali la computazione effettuata da $\mathcal M$ temrina in uno stato finale
- Che succede per $x\not\in L?$ La computazione effettuata da $\mathcal M$ può:
	- terminare in uno stato $q\in Q-F$
	- non terminare

### Turing-decidibilità

- Un linguaggio $L$ è detto **Turing-decidibile** se esiste una DTM che lo riconosce
- Un linguaggio $L$ è detto **Turing-semidecidibile** se esiste una DTM che lo accetta

# Macchine di Turing a più nastri

Una MTM (**Multi-tape Turing Machine**) a k nastri ($k\geq2$) è una sestupla $\mathcal M^{(k)}=\langle\Gamma,\square,Q,q_0,F,\delta^{(k)}\rangle$ 
dove:

- $\Gamma=\bigcup_{i=1}^{(k)}\Gamma_i$ è l'unione dei k **alfabeti di nastro** $\Gamma_1,...,\Gamma_k$ non necessariamente distinti
- $Q,q_0,F$ hanno lo stesso significato che nel caso della macchina di Turing ad 1 nastro 
- la funzione di transizione $\delta^{(k)}$ è definita come: $$\delta^{(k)}:(Q-F)\times\overline\Gamma[1]\times...\times\overline\Gamma[k]\times\{\to,\leftarrow,\circ\}^k$$


