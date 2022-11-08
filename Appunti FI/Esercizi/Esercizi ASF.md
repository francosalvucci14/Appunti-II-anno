# Esercizio 1

Definire un ASFD che riconosce le stringhe su $\lbrace a,b\rbrace$ caratterizzate dal fatto che il penultimo carattere è b

Soluzione:

![[appunti fi/esercizi/imges/Pasted image 20221102192816.png|center|500]]
Stringhe di esempio:

1. stringa aaba $$\delta(q_0,abba)=q_0\to\delta(q_0,bba)=q_1\to\delta(q_1,ba)=q_3\to\delta(q_3,a)=q_2$$
2. stringa bbb $$\delta(q_0,bbb)=q_1\to\delta(q_1,bb)=q_3\to\delta(q_3,b)=q_3$$
Altri esempi nel file Esercizi ASF qui -> [[Esercizi_ASF_2_nov_2022.pdf]]


# Esercizio 2


