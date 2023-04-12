
![[appunti asd/mod ii/immagini/Pasted image 20230405090935.png|center|550]]

# Data Compression

Q. Given a text that uses alphabet S of 32 symbols, how can we encode this text in **bits**?

A. We can **encode** $2^5$ different symbols using a **fixed** length of 5 bits per symbol.
- $C: S \to \{0,1\}^5$ This is called _**fixed length encoding.**_

Q. Some symbols **(e, t, a, o, i, n)** are used far **more often** than others. How can we use this to _reduce_ our encoding?

A. Encode these characters with **fewer** bits, and the others with **more** bits.

Q. How do we know when the next symbol begins?

A. Use a separation symbol (like the pause in Morse), or make sure that there is
no **ambiguity** by ensuring that **_no_ code is a _prefix_ of another one**.

![[appunti asd/mod ii/immagini/Pasted image 20230405093739.png|center|300]]


## Prefix Codes

>[!definition]- Definition (Prefix Codes)
>A **prefix code** for a set S is a function c that maps each $x\in S$ to $\{0,1\}^\star$ in such a way that $$\forall x,y\in S, x\neq y, \text{c(x) is not a prefix of c(y)}$$

![[appunti asd/mod ii/immagini/Pasted image 20230405094215.png|center|300]]

### Optimal Prefix Codes

>[!definition]- Definition (Average Bits per Letter)
>The **average bits per letter** of a prefix code c is the sum over all symbols of: 
>( its frequency ) * (the number of bits of its encoding): $$ABL(c)=\sum_{x\in S}f_x\cdot|c(x)|$$

_**Optimization Problem**_:
- **Input**. A finite alphabet S with symbol freq. $\{f_x : x \in S \}$
- **Goal**: find a _**prefix code c**_ that has the _lowest_ possible _average bits per letter_.

We can model a code in a binary tree…

#### Representing Prefix Codes using Binary Trees

![[appunti asd/mod ii/immagini/Pasted image 20230405095910.png|center|550]]

![[appunti asd/mod ii/immagini/Pasted image 20230405100854.png|center|550]]

![[appunti asd/mod ii/immagini/Pasted image 20230405100933.png|center|550]]

>[!definition]- Definition (Tree is Full)
>A tree is **full** if every node that is not a leaf has two children.

**Claim**. The binary tree corresponding to an _optimal_ prefix code is _**full**_.

![[appunti asd/mod ii/immagini/Pasted image 20230405101119.png|center|200]]

**Proof (by contradiction)**

- Suppose T is binary tree of optimal prefix code and is not full.
- This means there is a node **u** with only one child **v**.
	- Case 1: **u** is the root; delete **u** and use **v** as the root
	- Case 2: **u** is not the root
		- Let **w** be the parent of **u**
		- Delete **u** and make **v** be a child of **w** in place of **u**
- In both cases the number of bits needed to encode any leaf in the subtree of v is _**decreased**_. The rest of the tree T is not affected.
- Clearly this new tree T’ has a smaller ABL than T. _**Contradiction**_.

### Optimal Prefix Codes : False Start

Q. Where in the tree of an optimal prefix code should letters be placed with a high frequency?
A. Near the top! Use recursive structure of trees.

**Greedy template.**
Create tree _**top-down**_, split S into two sets $S_1$ and $S_2$ with **(almost) equal frequencies** Recursively build tree for $S_1$ and $S_2$.

$[\text{Shannon-Fano,1949}]\to f_a=0.32, f_e=0.25, f_k=0.20, f_l=0.18, f_u=0.05$ 

![[appunti asd/mod ii/immagini/Pasted image 20230412091701.png|center|500]]


