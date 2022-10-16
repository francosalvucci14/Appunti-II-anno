# Ricorsione, tecniche di progettazione e equazioni di ricorrenza

## Soluzione esercizio calcolo tempo medio con algoritmo di pesatura

>Alg1
>1. for i=2 to n do
>2. if peso($x_1$)>peso($x_i$) then return $x_1$
>3. if peso($x_1$)<peso($x_i$) then return $x_i$

$T_{avg}(n)=\sum_{\text{istanze I di dimensione n}}(Pr(I)\cdot numpesate(I))$
$\implies \sum_{j=1}^n\underbrace{Pr(\text{"moneta falsa è in posizione j in I"})}_{1/n}\underbrace{numpesate(I)}_{\text{1 se j=1, j-1 altrimenti}}=(1/n)(1+\sum_{j=2}^n(j-1))$
$\implies (1/n)(1+\sum_{j=1}^{n-1}(j))=(1/n)(1+(n-1)(n/2))=\frac{1}{n}\cdot \frac{(n-1)}{2}\implies \frac{(n-1)}{2}$ 

Quindi $T_{avg}(n)=\frac{n-1}{2}$ 

## Sommario
- **Complessità** di algoritmi ricorsivi e **equazioni di ricorrenza**
- Una tecnica di progettazione algoritmica: **divide et impera**
- Metodi per risolvere equazioni di ricorrenza:
	- [[Lezione 3 - Capitolo 2#Metodo dell'iterazione|Iterazione]]
	- **albero della ricorsione**
	- **sostituzione**
	- **teorema Master**
	- **cambiamento di variabile**

## Equazioni di ricorrenza

_Def_
La **complessità computazionale** di un algoritmo ricorsivo può essere espressa in modo naturale attraverso una **equazione di ricorrenza**

**Esempi**
- $T(n)=T(n/3)+2T(n/4)+O(nlog(n))$ 
- $T(n)=T(n-1)+O(1)$
- $T(n)=T(n/3)+T(2n/3)+n$

>Caso base : $T(costante)=cost\: (oppure\: T(1)=1)$

### Metodo dell'iterazione

_Idea_: "Srotolare" la ricorsione, ottenendo una sommatoria dipendente solo dalla dimensione n del problema iniziale

**Esempio**
$T(n)=c+T(n/2)$$T(n)=c+T(n/2)\implies T(n/2)=2c+T(n/4)\implies T(n/4)=3c+T(n/8)...T(n/i)=ic+T(n/2^i)$
Continuo a srotolare fin quando non trovo il caso base,in questo caso quando $i=log_2(n)$, infatti:
$T(n)=c\cdot log_2n+T(\frac{n}{2^{log_2n}})\implies c\cdot log_2n+T(\frac{\cancel{n}}{\cancel{n}})\implies c\cdot log_2n+T(1)=\Theta(log(n))$ 

**Esempio**

$T(n)=T(n-1)+1$
$T(n)=T(n-1)+1\implies T(n-2)+2\implies T(n-3)+3\implies ...T(n-i)+i$
In questo caso il caso base lo abbiamo quando $i=n-1$ e infatti abbiamo:
$T(n)=T(1)+n-1=\Theta(n)$

