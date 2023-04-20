
# Knapsack Problem

**Knapsack problem**.
Input
- Given n objects $I = \{(w_i,v_i): i=1,\dots,n\}$ and a **Knapsack**
- Item **i** weighs $w_i \gt 0$ kilograms and has value $v_i \gt 0$.
- **Knapsack** has capacity of **W** kilograms.
End input
- **Feasible Sol**: $S \subseteq I : \sum\limits_{j\in S} w_i$
- **Goal**: fill knapsack so as to _**maximize**_ total SUM of values: $\sum\limits_{j\in S} v_i$ 
Ex: $S=\{3,4\}=40$

![[appunti asd/mod ii/immagini/Pasted image 20230420143732.png|center|500]]

**Greedy**: repeatedly add item with maximum ratio $\frac{v_i}{w_i}$.
Ex: { 5, 2, 1 } achieves only value = 35 $\to$ greedy not optimal.

## Dynamic Programming : 1st approach

>[!definition]- Definition OPT(i)
>Max profit subset of items $1, \dots, i$. (Which Ordering?)

<u>Case 1</u>: OPT does not select item **i**.
- OPT selects best of $\{ 1, 2, \dots, i-1 \}$
<u>Case 2</u>: OPT selects item **i**. (Which sub-problems must recursively be invoked?)
- accepting item i does not immediately imply that we will have to reject **other items** $k \lt i$.
- without knowing what other items were selected before i,we don'teven know if we have enough room for i

Conclusion: Need <u>more</u> sub-problems, i.e. more parameters than just index i

## Dynamic Programming : Adding a new variable

>[!definition]- Def.
>For any fixed pair $i \in I$ and $w \in \{0,1,\dots,W\}$ consider:
>$OPT(i, w)$ = **max** <u>profit</u> subset of items $1, \dots, i$ with _weight parameter_ **w**.

<u>Case 1</u>: OPT does not select item i.
- OPT selects best of sub-probl $\{ 1, 2, \dots, i-1 \}$ using **weight limit w**
<u>Case 2</u>: OPT selects item i
- new weight limit = $w - w_i$
- OPT selects **best** of $\{ 1, 2, \dots, i-1 \}$ using this **new weight limit**

$$OPT(i,w)=\begin{cases}0&\text{if i=0}\\OPT(i-1,w)&\text{if } w_i\gt w\\max\{\underbrace{OPT(i-1,w)}_\text{case 1},\underbrace{v_i+OPT(i-1,w-w_i)}_\text{case 2}\}&\text{otherwise}\end{cases}$$

Q. How to fill-up the matrix $M(i, w)$, for all $i = 1\dots n; w= 0\dots W$??
Answer: _**Nice Ordering Property**_
In order to compute row i, you need the values of rows $j \lt i$ only

## Knapsack Problem : Bottom-Up

Knapsack. Fill up an $n \times W$ array.
The **good ordering** for sub-problems

![[appunti asd/mod ii/immagini/Pasted image 20230420145921.png|center|650]]

