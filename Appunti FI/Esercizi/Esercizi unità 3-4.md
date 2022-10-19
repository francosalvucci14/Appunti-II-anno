![[appunti fi/esercizi/imges/Pasted image 20221018182856.png]]

Immagine degli esercizi svolti su Nebo

## Esercizio 2
determinare il linguaggio definito dall'espressione regolare $a^\star((aa)^\star b+(bb)^\star a)b^\star$ 

$$L=a^\star((aa)^\star b+(bb)^\star a)b^\star\implies L(a)^\star\circ [[(L(a)\circ L(a))^\star\circ L(b)]\cup [(L(b)\circ L(b))^\star\circ L(a)]]\circ L(b)^\star\implies$$
$$\lbrace a\rbrace^\star\circ[[\lbrace aa\rbrace^\star\circ\lbrace b\rbrace]\cup[\lbrace bb\rbrace^\star\circ\lbrace a\rbrace]]\circ\lbrace b\rbrace^\star\implies\lbrace a\rbrace^\star\circ[\lbrace aa,bb\rbrace^\star\circ\lbrace a,b\rbrace]\circ\lbrace b\rbrace^\star$$

Da rivedere

## Esercizio 1
determinare l'espressione regolare che, sull'alfabeto $\lbrace a,b\rbrace$, definisce l'insieme delle stringhe il cui terzultimo carattere è una b

$$r=(\underbrace{\lbrace ab\rbrace^\star}_{s_1}\circ\underbrace{\lbrace b\rbrace}_{s_2}\circ\underbrace{[(a+b)\circ(a+b)]}_{s_3})$$
$s_1=\text{Una sequenza(potenzialmente infinita) della coppia ab}$
$s_2=\text{il carattere b}$
$s_3=\text{la stringa finisce o con 2 "a" o con 2 "b" o con la coppia ab}$




