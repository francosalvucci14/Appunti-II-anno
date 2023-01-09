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





