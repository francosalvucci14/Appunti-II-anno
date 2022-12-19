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








