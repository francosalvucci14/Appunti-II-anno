
# Pumping Lemma

>[!important]- Teorema
>Sia $L\subseteq V_T^\star$ un linguaggio non contestuale. Esiste allora una costante n tale che se $z\in L$ e $|z|\geq n$ allora esistono 5 stringhe $u,v,w,x,y\in V_T^\star$ tali che $$\begin{align}i)&uvwxy=z\\ii)&|vx|\geq1\\iii)&|vwx|\leq n\\iv)&\forall i\geq0\:uv^iwx^iy\in L\end{align}$$

## Interpretazione come gioco a due

Se $L$ è contex free, Alice vince sempre questo gioco con Bob:
(Alice = $\exists$ e Bob = $\forall$)

1. Alice fissa un intero $n\gt0$ opportuno
2. Bob sceglie una stringa $z\in L$ con $|z|\gt n$
3. Alice divide z in cinque parti uvwxy con $|vwx|\leq n$ e $|vx|\geq1$
4. Bob sceglie un intero $i\geq0$
5. Alice mostra a Bob che $uv^iwx^iy\in L$

**Dimostrazione**

Grammatica $\mathcal G=\langle V_T,V_N,P,S\rangle$ in CNF che genera $L=L(\mathcal G)$ e sia $k=|V_N|$ il numero di simboli non terminali in $\mathcal G$ 

Qualunque albero sintattico $A(\sigma)$ relativo ad una stringa $\sigma\in V_T^\star$ derivata in $\mathcal G$ sarà tale da avere tutti i nodi interni (corrispondenti ai simboli non terminali) di grado 2,eccetto quelli aventi foglie dell'albero come figli, che hanno grado 1

- Se h è l'altezza di $A$ (numero massimo di archi, e anche numero massimo di nodi interni, in un cammino dalla radice ad una foglia), il massimo numero di foglie $l(h)$ è dato dal caso in cui l'albero è completo (i nodi interni hanno due figli, eccetto i padri di foglie, che ne hanno uno). SI può facilmente verificare che in tal caso abbiamo $l(h)=2^{h-1}$, in quanto $l(1)=1=2^0$ e $l(h+1)=2\cdot l(h)=2\cdot 2^{h-1}=2^h$ 
- Se l'albero sintattico $A(\sigma)$ relativo alla stringa $\sigma\in L$ ha altezza $h(\sigma)$, la lunghezza di $\sigma$ è allora $|\sigma|\leq 2^{h(\sigma)-1}$, e quindi $h(\sigma)\geq 1+log_2|\sigma|$
- Se $\sigma$ è una stringa sufficientemente lunga (in questo caso,$|\sigma|\gt 2^{|V_N|-1}$), ne risulta che $h(\sigma)\geq 1+log_2|\sigma|\gt|V_N|$
- Quindi, se $|\sigma|\gt 2^{|V_N|-1}$ esiste almeno un cammino c dalla radice ad una foglia di $A(\sigma)$ che attraversa almeno $|V_N|+1$ nodi interni

- I nodi interni di $A(\sigma)$ sono etichettati da simboli non terminali (le aprti sinistre delle produzioni nella derivazione di $\sigma$)
- Dato che i simboli non temrinli sono $|V_N|$ mentre i nodi interni in c sono più di $|V_N|$, deve esistere (per il pigeonhole principle) un simbolo non terminale A che compare in due diversi nodi di c
- Di questi due nodi, indichiamo con _r_ il nodo più vicino alla radice e _s_ il nodo associato ad A più vicino alla foglia
- Indichiamo con $r(\sigma),s(\sigma)$ le sottostringhe di $\sigma$ corrispondenti alle foglie dei due sottoalberi $R(\sigma),S(\sigma)$ di $A(\sigma)$ aventi radice _r_ e _s_
- Dato che _s_ è un discendente di _r_, necessariamente $s(\sigma)$ è una sottostringa di $r(\sigma)$, per cui esistono due sottostringhe di v,x di $\sigma$ tali che $r(\sigma)=v\cdot s(\sigma)\cdot x$

- La grammatica considerata è in CNF, per cui non sono presenti produzioni unitarie (a parte quelle relatice alle foglie): di conseguenza, non può essere $s(\sigma)=r(\sigma)$, e quindi $|vx|\gt1$
- Senza perdere generalità, possiamo assumere che $r(\sigma)$ sia il nodo in c più vicino alle foglie per il quale c'è un nodo sottostante $s(\sigma)$ associato allo stesso non terminale: quindi, il cammino più lungo da $r(\sigma)$ ad una foglia attraversa al più $|V_N|+1$ nodi interni (esso stesso incluso)
- Dalle osservazioni precedenti, ne deriva che $r(\sigma)$ ha lunghezza al più $2^{|V_N|+1-1}=2^{|V_N|}$

Poniamo $s(\sigma)=w$ e $r(\sigma)=vwx$

![[appunti fi/mod i/immagini/Pasted image 20221206094941.png|center|400]]

![[appunti fi/mod i/immagini/Pasted image 20221206095016.png|center|400]]

- Gli alberi $R(\sigma),S(\sigma)$ possono essere sostituiti (avendo radice corrispondente allo stesso non terminale) l'uno all'altro all'interno di qualunque albero sintattico
- Quindi, anche la stringa $uvy$ è generata dalla grammatica (sostituendo in $A(\sigma),R(\sigma)\:e\:S(\sigma)$)
- Mediante la sostituzione opposta, anche la stringa $uvwxy$ risulta generabile

$\square$

## Interpretazione come gioco a due

La proprietà mostrata fornisce soltanto una condizione necessaria perchè un linguaggio sia context free: non può essere utilizzata per mostrare la non contestualità di un linguaggio, ma solo per dimostrarne la contestualità

$$\begin{align}&\text{L contestuale}\implies\text{pumping lemma verificato}\\&\text{pumping lemma non verificato}\implies\text{L non contestuale}\end{align}$$

Se Alice vince sempre questo gioco con Bob, allora $L$ non è CF
(Alice = $\exists$ e Bob = $\forall$)

1. Bob sceglie un interno $n\gt0$
2. Alice sceglie una stringa $z\in L$ con $|z|\gt n$
3. Bob divide $z$ in cinque parti $uvwxy$ con $|vwx|\leq n$ e $|vx|\geq1$
4. Alice sceglie un intero $i\geq0$
5. Alice mostra a Bob che $uv^iwx^iy\not\in L$

