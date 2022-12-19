# Usi meno scontati della visita DFS

## Informazioni utili: tenere il tempo

![[appunti asd/mod i/immagini/Pasted image 20221219160725.png|center|600]]

pre(v) = tempo in cui viene "scoperto" v
post(v) = tempo in cui si "abbandona" v

## Quando non tutti i nodi sono raggiungibili dal punto di partenza

![[appunti asd/mod i/immagini/Pasted image 20221219160919.png|center|600]]

### Esempio

![[appunti asd/mod i/immagini/Pasted image 20221219161301.png|center]]


### Proprietà

Per ogni coppia di nodi u e v, gli intervalli $[pre(u),post(u)]$ e $[pre(v),post(v)]$ o sono disgiunyi o l'uno è contenuto nell'altro

u è antenato di v nell'albero DFS, se $pre(u)\lt pre(v)\lt post(v)\lt post(u)$ condizione che rappresentiamo così:

![[appunti asd/mod i/immagini/Pasted image 20221219161714.png|center]]

![[appunti asd/mod i/immagini/Pasted image 20221219161757.png|center|300]]

Possiamo usare i tempi di visiita per riconoscere il tipo di un generico arco (u,v) nel grafo?

### ...riconoscere i tipi di arco

![[appunti asd/mod i/immagini/Pasted image 20221219161932.png|center|600]]


# Cicli,DAG e ordinamenti topologici

## Riconoscere la presenza di un ciclo in un grafo diretto

**Algoritmo**: fai una visita DFS e controlla se c'è un arco all'indietro

>[!important]- Proprietà
>Un grafo diretto G ha un ciclo se e solo se la visita DFS rivela un arco all'indietro

$(\leftarrow):$ se c'è arco all'indietro, chairamente G ha un ciclo
$(\to):$ se c'è ciclo $<v_0,v_1,..,v_k=v_0>$ 

sia $v_i$ il primo nodo scoperto nella visita:
- $v_i$ termina la visita dopo che $v_{i+1}$ ha terminato la sua
- $v_{i+1}$ termina la visita dopo che $v_{i+2}$ ha terminato la sua
- ...
- quindi, per transitività, $v_i$ termina la visita dopo che $v_{i-1}$ ha temrinato la sua
- allora $(v_{i-1},v_i)$ è un arco all'indietro

![[appunti asd/mod i/immagini/Pasted image 20221219163048.png|center|150]]

>[!important]- Definizione
>Un **grafo diretto aciclico (DAG)** è un grafo diretto G che non contiene cicli (diretti)

>[!important]- Definizione
>Un ordinamento topologico di un grafo diretto G=(V,E) è una funzione biettiva $\sigma:V\to\{1,2,...,n\}$ tale che per ogni arco $(u,v)\in E,\sigma(u)\lt\sigma(v)$

![[appunti asd/mod i/immagini/Pasted image 20221219163503.png|center|600]]






