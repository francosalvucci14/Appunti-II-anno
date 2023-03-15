
# Implementazione dell'append

Questa è l'implementazione dell'append
```prolog
append([],L,L). %passo base%
append([HX|TX],L,[HX|TZ]):- %passo induttivo%
    append(TX,L,TZ).
```
**Esempi**

Query : `append([a,b],X,[a,b,c,d]).`
Risultato : `X = [c, d]`

Query : `append(Y,X,[a,b,c,d]).`
Risposta: 
```
X = [a, b, c, d],  
Y = []

X = [b, c, d],  
Y = [a]

X = [c, d],  
Y = [a, b]

X = [d],  
Y = [a, b, c]

X = [],  
Y = [a, b, c, d]
```

E cosi via..