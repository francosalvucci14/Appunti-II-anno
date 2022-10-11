# Complessità nel caso medio
## Testo
Analizazre la complessità nel caso medio del primo algoritmo di pesatura (Alg1) visto nella prima lezione. Rispetto alla distribuzione di probabilità sulle istanza, si assuma che la moneta falsa possa trovarsi in modo equiprobabile in una delle qualsiasi delle n posizioni.

## Svolgimento
Data la parola chiave "equiprobabile" possiamo dedurre che la probabilità sulle istanze, quindi $P(\mathcal{I})$è uguale a $\frac{1}{n}$

Il tempo tempo($\mathcal{I}$) su ogni istanza di dimesione n è n-1

Di conseguenza possiamo utilizzare la formula e il costo nel caso medio è pari a:
$$T_{avg}(n)=\sum_{i=1}^n \frac{1}{n}\cdot (n-1)=\underbrace{\frac{n-1}{n}+\frac{n-1}{n}+...+\frac{n-1}{n}}_{\text {n volte}}=\frac{\cancel{n}(n-1)}{\cancel{n}}=n-1$$
Quindi : $T_{avg}(n)=n-1$ 