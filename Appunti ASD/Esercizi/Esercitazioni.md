
# Esercitazione 1

>Dimostrare o confutare la seguente affermazione:
>Date $f(n)$ e $g(n)$, allora vale che:
>$f(n)=O(g(n))\implies 2^{f(n)}=O(2^{n/2})$

Soluzione:

prendiamo $f(n)=n\:e\:g(n)=n/2$
Così vale che $n=O(n/2)$, ma $2^n\neq O(2^{n/2})$
Infatti:

$lim_{n\to\infty}\frac{n}{n/2}=1/2\lt\infty$ e quindi $n=O(n/2)$
Ma:

$lim_{n\to\infty}\frac{2^n}{2^{n/2}}=2^{n/2}=\infty$ e quindi $2^n=\omega(2^{n/2})$


