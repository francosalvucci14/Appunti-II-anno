# Pumping Lemma

>[!important]- Pumping Lemma
>Ogni stringa sufficientemente lunga appartenente ad un linguaggio regolare presenta delle regolarità: in particolare, contiene una sottostringa che può essere ripetuta quanto si vuole, ottenendo sempre stringhe del linguaggio

Più precisamente:
Sia $L$ un linguaggio regolare: allora $\exists n\gt 0$ tale che $\forall z\in L:|z|\geq n$ possiamo scrivere $z=uvw$, con $|uv|\leq n,|v|\geq1$ e ottenere che $\forall i\geq0, uv^iw\in L$

Se $L$ è regolare, sia l'ASFD $\mathcal A$ che lo decide e che ha il minimo numero n di stati

Una stringa $z\in L$ di lunghezza $m\geq n$ in input a $\mathcal A$ gli fa eseguire m transizioni e quindi attraversare $m+1\gt n$ stati, quindi esiste almeno uno stato che viene attraversato più volte

