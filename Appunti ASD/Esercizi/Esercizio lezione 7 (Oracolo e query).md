Dato un vettore X di n interi in $[1,k]$, costruire in tempo $O(n+k)$ una struttura dati (**oracolo**) che sappia rispondere a domande (**query**) in tempo $O(1)$ del tipo : "quanti interi in X cadono nell'intervallo $[a,b]$?", per ogni a e b

Soluzione:
Codice CreaOracolo
```pseudo
CreaOracolo(X,k)
Y array di dimensione k
for i=1 to k do Y[i]=0
for i=1 to n do incremento Y[X[i]]
for i=2 to k do Y[i]=Y[i]+Y[i-1]
```
Codice ChiamaOracolo
```pseudo
ChiamaOracolo(Y,a,b,k)
if b>k then b=k
if a <= 1 then return Y[b]
		  else return (Y[b]-Y[a-1])
```
