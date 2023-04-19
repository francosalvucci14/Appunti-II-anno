
# Segmented Least Squares

**_Least squares._**
- Foundational problem in statistic and numerical analysis.
- Given n points in the plane: $I =\{(x_1, y_1), (x_2, y_2) , \dots , (x_n, y_n)\}.$
- Find a line $y = ax + b$ that minimizes the sum of the squared error:

![[appunti asd/mod ii/immagini/Pasted image 20230419095038.png|center|550]]

**Solution**

![[appunti asd/mod ii/immagini/Pasted image 20230419095105.png|center|550]]

But for some sequence of points, the approximation given by _just one line_ might be terrible....

**Idea**: find a good _**trade-off**_ between _number of lines_ and _approximation quality_

_**Segmented least squares.**_
- Points lie roughly on a sequence of several line segments.
- Given n points in the plane $I= \{(x_1, y_1), (x_2, y_2) ,\dots , (x_n, y_n)\}$ with $x_1 \lt x_2 \lt \dots \lt x_n$, find a sequence of lines that minimizes $f(x).$

Q. What's a reasonable choice for f(x) to balance $\underbrace{accuracy}_{\text{goodnes of fit}}$ and $\underbrace{parsimony}_{\text{number of lines}}$?

![[appunti asd/mod ii/immagini/Pasted image 20230419095420.png|center|550]]

Given n points in the plane $I= \{(x_1, y_1), (x_2, y_2) ,\dots , (x_n, y_n)\}$ with $x_1 \lt x_2 \lt \dots \lt x_n$, find a **sequence of lines** that minimizes:
- the **sum** of the **sums** of the **squared errors** E in each segment: $E(i,j)=SSE(i,j)$
- the **number** of lines L 
- **Tradeoff function** : $E + c L$, for some constant $c > 0$. (Funzione obiettivo)

![[appunti asd/mod ii/immagini/Pasted image 20230419095626.png|center|550]]

## Dynamic Programming: Multiway Choice

**_Notation._**
- $OPT(j)$ = minimum cost for points $p_1,\dots, p_i , \dots , p_j.$
- $e(i, j)$ = minimum sum of squares for points $p_i, p_{i+1} ,\dots , p_j$, according to Eq.s (1) and (2)

>[!error]- Observation (Optimal Structure).
>Find a possible ‘’recursion’’: let $[p_i, p_j]$ be the <u>rightmost</u> segment in $OPT(j)$, then
>$$OPT(j) = OPT(i-1) + (1 \times C) + e(i,j), 1 \leq i \leq j$$

So the problem is to find the ‘’optimal’’ **i**
Try All and get the best = Dynamic Programming!

