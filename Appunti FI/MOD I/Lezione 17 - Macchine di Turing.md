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
- 