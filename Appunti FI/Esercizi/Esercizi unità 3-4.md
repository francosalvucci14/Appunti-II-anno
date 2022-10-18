## Esercizio 2
determinare il linguaggio definito dall'espressione regolare $a^\star((aa)^\star b+(bb)^\star a)b^\star$ 

$$L=a^\star((aa)^\star b+(bb)^\star a)b^\star\implies L(a)^\star\circ [[(L(a)\circ L(a))^\star\circ L(b)]\cup [(L(b)\circ L(b))^\star\circ L(a)]]\circ L(b)^\star\implies$$
$$\lbrace a\rbrace^\star\circ[[\lbrace aa\rbrace^\star\circ\lbrace b\rbrace]\cup[\lbrace bb\rbrace^\star\circ\lbrace a\rbrace]]\circ\lbrace b\rbrace^\star\implies\lbrace a\rbrace^\star\circ[\lbrace aa,bb\rbrace^\star\circ\lbrace a,b\rbrace]\circ\lbrace b\rbrace^\star$$


