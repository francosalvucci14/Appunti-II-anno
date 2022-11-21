# Pumping Lemma

>[!important]- Pumping Lemma
>Ogni stringa sufficientemente lunga appartenente ad un linguaggio regolare presenta delle regolarità: in particolare, contiene una sottostringa che può essere ripetuta quanto si vuole, ottenendo sempre stringhe del linguaggio

Più precisamente:
Sia $L$ un linguaggio regolare: allora $\exists n\gt 0$ tale che $\forall z\in L:|z|\geq n$ possiamo scrivere $z=uvw$, con $|uv|\leq n,|v|\geq1$ e ottenere che $\forall i\gt0, uv^iw\in L$

