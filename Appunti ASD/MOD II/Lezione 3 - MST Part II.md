
Per un approfondimento su ST e MST in ITALIANO vedi qui --> [Approfondimenti ST e MST](http://www.mat.uniroma2.it/~guala/08_Kruskal_2015.pdf)

# Cycles and Cuts

**Cycle**:  Set of edges the form a-b,b-c,c-d,...,y-z,z-a

![[appunti asd/mod ii/immagini/Pasted image 20230315091633.png|center|600]]

**Cutset** : A **CUT** is determinated by some S. The corresponding **CUTSET D** is the subset of edges with exactly one endpoint in S

![[appunti asd/mod ii/immagini/Pasted image 20230315091759.png|center|600]]


## Property : Cycle-Cut Intersection

>[!definition]- Claim
>A cycle and a cutset intersect in an **even** number of edges

![[appunti asd/mod ii/immagini/Pasted image 20230315091940.png|center|600]]

Proof. (by picture)

![[appunti asd/mod ii/immagini/Pasted image 20230315092019.png|center|500]]


## Cut property : proof

**Simplifying assumption** : All edge costs $c_e$ are distinct

>[!definition]- Definition (Cut property)
>Let S be anny subset of nodes, and let **e** be the min cost edge with exactly one ednpoint in **S**. THen the **MST** $T^\star$ _contains_ **e**

Proof (**exchange argument**) :

- Suppose **e** does not belong to $T^\star$, and let's see what happens
- Adding **e** to $T^\star$ creates a **cycle** C in $T^\star$ 
- Edge **e** is both in the cycle C and in the cutset D corresponding to S $\implies$ then exists another edge, say f, that is in both C and D
- Consider $T'=T^\star\cup\{e\}-\{f\}$ : it is also a **spanning tree** 
- Since $c_e\lt c_f\implies cost(T')\lt cost(T^\star)$
- This is a **contradiction**

![[appunti asd/mod ii/immagini/Pasted image 20230315092639.png|center|400]]


## Cycle property : proof

**Simplifying assumption** : All edge costs $c_e$ are distinct

>[!definition]- Definition (Cycle prorperty)
>Let C be any cycle in G, and let f be the **max cost edge** belonging to C. Then the **MST** $T^\star$ _does not_ contain f

Proof (**exchange argument**)

- Suppose f belongs to $T^\star$, and let's see what happens
- Deleting f from $T^\star$ creates a **cut S** in $T^\star$
- Edge f is both in the cycle C and in the cutset D corresponding to S $\implies$ there exists another edge, say **e**, that is in both C and D
- $T'=T^\star\cup\{e\}-\{f\}$ is also a spanning tree
- Since $c_e\lt c_f\implies cost(T')\lt cost(T^\star)$
- This is a **contradiction**

![[appunti asd/mod ii/immagini/Pasted image 20230315093858.png|center|400]]

