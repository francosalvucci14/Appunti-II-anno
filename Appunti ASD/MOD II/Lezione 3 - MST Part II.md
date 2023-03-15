
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
>Let S be any subset of nodes, and let **e** be the **min cost edge** with exactly one endpoint in **S**. Then the **MST** $T^\star$ _contains_ **e**

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


# Prim's algorithm

## Implementation

Use a priority queue ala Dijkstra
Maintain set of **explored** nodes **S**
For each _**unexplored**_ nove v, maintain _attachment cost_ $a[v]=\text{cost of cheapest edge v to a node in S}$

**Pseudocode**

![[appunti asd/mod ii/immagini/Pasted image 20230315094137.png|center|600]]

## Proof of correctness

`[Jarnik 1930,DIjkstra 1957, Prim 1959]`

Proof:

- Initialize S = any node
- Apply **cut property** to S
- Add **min cost edge** in cutset $D(S)$ to $T$, and add one new explored node u to S

![[appunti asd/mod ii/immagini/Pasted image 20230315095343.png|center|500]]

### Key Facts of the Proof

**What is S? How growes?**
- At each round, a new unexplored node is inserted in S. So,at each round of the WHILE loop, $|S|$ increases by 1 : $S_0=\{u_1\},...,S_t=\{u_1,u_2,...,u_t\},...,S_{n-1}=V$
**Connectivity of G**:
- The algorithm **terminates**! AND whene it terminates, T **spans all nodes** of V (It is a Graph Search!)
**Why T is an MST?**
- At each WHILE loop, apply the **CUT property**! Where? On the (current) CUT : $(S_T=\{\text{explored nodes till round t}\},V-S_t),t=1,..,n-1$

## Time complexity of Prim's algorithm

The time complexity is 
- $O(n^2)$ if is implemented by linear structure
- $O(m\cdot log(n))$ if is implemented by Heap

For any visited node $u\in V$, update $O(deg(u))$ keys in Q $\implies\sum_udeg(u)=O(m)$
Each update costs $O(log n)$ (using Heap)
Total : $O(m\cdot log(n))$


# Kruskal's Algorithm

## Proof of correctness

**Kruskal's algorithm**:
- Consider edges in ascending order of weight
- Case 1 : If adding **e** to **T** creates a _**cycle**_, discard **e** according to cycle property
- Case 2 : Otherwise, insert **e = (u,v)** into T according to cut property where S = set of nodes in **u's connected component**

![[appunti asd/mod ii/immagini/Pasted image 20230315101226.png|center|500]]

