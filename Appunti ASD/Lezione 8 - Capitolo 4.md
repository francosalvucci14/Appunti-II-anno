Ritornando alla [[Lezione 7 - Capitolo 4]]

# BucketSort
Per ordinare n record con chiavi intere $[1,k]$

**Esempio**: ordinare n record con campi:
- nome,cognome,anno di nascita,matricola,...
Si potrebbe voler ordinare per matricola o per anno di nascita

**Input** del problema:
- n record mantenuti in un array
- ogni elemento dell'array è un record con:
	- campo chiave (rispetto al quale ordinare)
	- altri campi associati alla chiave (informazione satellite)

- Basta mantenere un array di liste, anzichè di contatori, ed operare come per [[Lezione 7 - Capitolo 4#IntegerSort|IntegerSort]]
- La lista $Y[i]$ conterrà gli elementi con chiave uguale a i
- Concatenare poi le liste

Tempo $O(n+k)$ come per IntegerSort

**Esempio**
![[appunti asd/immagini/Pasted image 20221107161441.png|center|500]]
![[appunti asd/immagini/Pasted image 20221107161547.png|center|500]]
![[appunti asd/immagini/Pasted image 20221107161643.png|center|500]]
... e così via...
![[appunti asd/immagini/Pasted image 20221107161742.png|center|500]]
![[appunti asd/immagini/Pasted image 20221107161822.png|center|500]]
fino a...
![[appunti asd/immagini/Pasted image 20221107161857.png|center|500]]






