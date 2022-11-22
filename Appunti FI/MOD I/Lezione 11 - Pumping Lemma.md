# Pumping Lemma

>[!important]- Pumping Lemma
>Ogni stringa sufficientemente lunga appartenente ad un linguaggio regolare presenta delle regolarità: in particolare, contiene una sottostringa che può essere ripetuta quanto si vuole, ottenendo sempre stringhe del linguaggio

Più precisamente:
Sia $L$ un linguaggio regolare: allora $\exists n\gt 0$ tale che $\forall z\in L:|z|\geq n$ possiamo scrivere $z=uvw$, con $|uv|\leq n,|v|\geq1$ e ottenere che $\forall i\geq0, uv^iw\in L$

## Dimostrazione
Se $L$ è regolare, sia l'ASFD $\mathcal A$ che lo decide e che ha il minimo numero n di stati

Una stringa $z\in L$ di lunghezza $m\geq n$ in input a $\mathcal A$ gli fa eseguire m transizioni e quindi attraversare $m+1\gt n$ stati, quindi esiste almeno uno stato che viene attraversato più volte (Principio Della Piccionaia)

$\square$

## Interpretazione come gioco a due

Se $L$ è regolare, ALice vince sempre questo gioco con Bob:

1. Alice fissa un intero $n\gt0$ opportuno
2. Bob sceglie una stringa $z\in L$ con $|z|\gt n$
3. Alice divide z in tre parti $uvw$ con $|uv|\leq n\:e\:|v|\geq1$
4. Bob scelgie un intero $i\gt0$
5. Alice mostra a Bob che $uv^iw\in L$


Il pumping lemma evidezia in fatto che gli automi finiti: non possono contare, Il numero di situazioni diverse che possono memorizzare è finito

Fornisce soltatno una condizione necessaria perchè un linguaggio sia regolare: non può essere utilizzato per mostrare la regolarità di un linguaggio, ma solo per dimostrarne la non regolarità
$$\begin{align}L\:\text{regolare}\implies \text{pumping lemma verificato}\\\text{pumping lemma non verificato}\implies L\:\text{non regolare}\end{align}$$

Sia $L$ un liinguaggio e supponiamo che $\forall n\gt0$ si abbia che $\exists x\in L:|z|\geq n$ tale che comunque dividiamo $z$ in $z=uvw$ con $|uv|\leq n,|v|\geq1,\exists i\geq0$ tale che $uv^iw\not\in L$. Allora, $L$ non è regolare

Se $L$ non è regolare, Alice vince sempre questo gioco con Bob:

1. Bob fissa un intero $n\gt0$
2. Alice sceglie una stringa opportuna $z\in L$, con $|z|\gt n$
3. Bob divide z in tre parti $uvw$ con $|uv|\leq n$ e $|v|\geq1$
4. Alice sceglie un intero $i\geq0$ e mostra a Bob che $uv^iw\not\in L$

**Esempio**

Si consideri il linguaggio $L=\lbrace w\overline{w}|w\in\lbrace a,b\rbrace^\star\rbrace$, ove si è indicata con $\overline w$ la stringa ottenuta invertendo i caratteri presenti in $w$
Dimostrare, usando il pumping lemma, che tale linguaggio non è regolare

Svolgimento:

Interpretiamo il ruolo di Alice nel gioco.

1. Bob fissa un intero $n\gt0$
2. Scegliamo la stringa $z=a^nbba^n$
3. Bob divide z in tre parti $uvw$ con $|uv|\leq n,|v|\geq1$: per la struttura di z, necessariamente $uv=a^h$, con $1\lt h\leq n$. Quindi,$v=a^l$, con $1\lt l\leq h$ e corrispondentemente $u=a^{h-l}$, inoltre $w=a^{n-h}bba^n$
4. Scegliamo l'intero 2 e mostriamo a Bob che $$uv^2w=a^{h-l}a^la^la^{n-h}bba^n=a^{n+l}bba^n\not\in L$$
Quindi il linguaggio $L=\lbrace w\overline{w}|w\in\lbrace a,b\rbrace^\star\rbrace$ non è regolare