
# Definizione di Macchina di Turing

La macchina di Turing che abbiamo visto informalmente durante la scorsa lezione utilizza 3 nastri: sui primi due nastri, prima che la macchina inizi ad operare, vengono scritti (dall’utente) i due numeri da sommare, sul terzo, inizialmente vuoto, la macchina scrive il risultato nel corso della sua computazione

Dobbiamo, ora, formalizzare questi concetti e, allo scopo, cominciamo con il limitarci a considerare macchine di Turing che utilizzano un **solo nastro**

La definizione 1.3 a pag. 9 della dispensa 1 presenta una macchina di Turing ad un nastro come:

- una unità di controllo che, ad ogni istante, può trovarsi in uno stato interno appartenente ad un certo insieme Q che contiene, fra gli altri, lo stato particolare q_0 che fa partire la computazione e un sottoinsieme QF di stati che fanno terminare la computazione
- un nastro suddiviso in un infinito numero di celle, ciascuna delle quali, ad ogni istante, può essere vuota o contenere un simbolo appartenente ad un alfabeto Σ, e sul quale nastro si muove una testina di lettura/scrittura
- ad ogni istante, dipendentemente dallo stato interno e da ciò che è letto dalla testina, viene eseguita una quintupla scelta in un insieme P di quintuple

E come funziona una macchina di Turing? Facile: quando l’unità di controllo si trova nello stato $q_0$, la testina legge il simbolo contenuto nella cella che sta scandendo, cerca una quintupla i cui primi due elementi sono $q_0$ e il simbolo letto dalla testina (che può anche essere il simbolo blank $\square$) e, se trova una tale quintupla, la esegue

- se non la trova ... non compie alcuna azione (ci torneremo più avanti) e la computazione termina

Eseguire una quintupla significa eseguire le tre azioni in essa indicate:

- sovrascrivere il simbolo nella cella scandita dalla testina con il simbolo indicato nella quintupla
- cambiare (eventualmente) stato interno
	- eventualmente, ossia, a meno che nella quintupla non sia indicato di rimanere nel medesimo stato in cui ci si trovava prima della sua esecuzione
- muovere (eventualmente) la testina
	- eventualmente, ossia a meno che nella quintupla sia indicato “ferma”

Eseguita la prima quintupla, si cerca un’altra quintupla da eseguire (ossia, una quintupla i cui primi due elementi sono lo stato in cui si trova la machina e il simbolo letto dalla testina) e così via, fino a quando nessuna quintupla può essere eseguita

## Esempio di Macchina di Turing

Consideriamo una macchina di Turing ad un nastro, $T_{parità}$ , definita sull’alfabeto $\Sigma=\langle 0,1,p,d\rangle$ e sull’insieme di stati $Q=\langle q_0,q_p,q_d,q_f\rangle$ con stato iniziale $q_0$ e stato finale $q_f$ il cui insieme delle quintuple è :
$$\begin{align}P=&\{\langle q_0,0,\square,q_p,dx\rangle,\langle q_0,1,\square,q_d,dx\rangle\\&\langle q_p,0,\square,q_p,dx\rangle,\langle q_d,0,\square,q_d,dx\rangle\\&\langle q_p,1,\square,q_d,dx\rangle,\langle q_d,1,\square,q_p,dx\rangle\\&\langle q_p,\square,p,q_f,stop\rangle,\langle q_d,\square,d,q_f,stop\rangle\}\end{align}$$
La macchina $T_{parità}$ scandisce la sequenza di caratteri scritta sul suo nastro, cancellandoli via via che vengono scanditi, e verificando se tale sequenza contiene un numero pari o un numero dispari di ‘1’: al termine della scansione, nel primo caso scrive ‘p’ e termina, nel secondo caso scrive ‘d’ e termina

Vediamo ora la macchina $T_{parità}$  in azione:

- poniamo la macchina nello stato q_0
- scriviamo una sequenza di caratteri sul nastro – che era precedentemente vuoto
- posizioniamo la testina sul carattere più a sinistra fra quelli scritti sul nastro
- ![[appunti fi/mod ii/immagini/Pasted image 20230308153924.png|center|500]]
- .. e vediamo cosa succede

Osserviamo che P contiene la quintupla $\langle q_0 , 1, \square, q_d , dx\rangle$ e che essa può essere eseguita

![[appunti fi/mod ii/immagini/Pasted image 20230308154102.png|center|500]]

eseguiamo, la quintupla, $\langle q_0 , 1, \square, q_d , dx\rangle$ : 

![[appunti fi/mod ii/immagini/Pasted image 20230308154155.png|center|500]]

E cosi via...

Naturalmente, sul nastro di $T_{parità}$ possiamo scrivere ciò che vogliamo:

- ad esempio, possiamo scrivere la sequenza di caratteri p010
- e vedere cosa succede facendo partire questa nuova computazione:
- ![[appunti fi/mod ii/immagini/Pasted image 20230308154333.png|center|500]]
.. Attenzione! P non contiene alcuna quintupla che inizia con la coppia $(q_0,p)$
- quindi, nessuna quintupla può essere eseguita

