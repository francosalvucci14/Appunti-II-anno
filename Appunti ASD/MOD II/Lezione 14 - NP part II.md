# The main question : P versus NP

![[appunti asd/mod ii/immagini/Pasted image 20230510095258.png|center|600]]

# NP-Completeness

## Polynomial Transformation

**Polynomial Transformation**

>[!definition]- Def. [Polynomially reduces (Cook)]
>Problem X **_polynomially_ reduces** (**Cook**) to problem Y if arbitrary instances of
>problem X can be solved using:
>- Polynomial number of standard computational steps, plus
>- Polynomial number of calls to oracle that solves problem Y.

>[!definition]- Def. [Polynomially transforms (Karp)]
>Problem X **_polynomially_ transforms** (**Karp**) to problem Y if $F:\Sigma^\star\to\Sigma^\star$ exists such that:
>1. F can be computed in $poly(|x|)$ time
>2. x is a yes instance of X,iff $y= F(x)$ is a yes instance of Y (Prop. 1 implies $|y|$ to be of size polynomial in $|x|$)

**Note**. **Polynomial transformation** is **polynomial reduction** with <u>just one call</u> to oracle for Y,
exactly at the end of the algorithm for X. 
Almost all our reductions will be of this form.

Open question.
Are these two concepts the same with respect to NP? (we abuse notation $\preceq_p$ and blur distinction)

![[appunti asd/mod ii/immagini/Pasted image 20230510091307.png|center|550]]


### Polynomial (Karp) Reduction: Algorithmic use

>[!definition]- THM 1.
>IF $X\preceq_p Y$ and $Y \in P$ THEN $X \in P$ (So, class P is closed w.r.t. $\preceq_p$ )

**Proof**.
By Hyp. there is a poly reduction $F:\Sigma^\star\to\Sigma^\star$ from X to Y and a deterministic poly-time algorithm ALG solving Y.  Let p() and g() the polynomial time-bounds for computing F and ALG, respectively

Then, consider any instance $x\in\Sigma^\star$ and make the following steps:
1. Compute $F(x) = y\in\Sigma^\star$; ( Note: Time is $p(|x|)$ and $|y|\leq p(|x|)$ )
2. Compute $ALG(y)$; (Note: Time is $g(|y|) \leq g(p(|x|)$ so it all $poly(|x|)$ ! )
3. If ALG(y) = yes THEN return **yes** ELSE return **no**

![[appunti asd/mod ii/immagini/Pasted image 20230510091643.png|center|500]]

### Polynomial Reduction: NP-Completeness

>[!definition]- Def. [NP-Completeness]
>A problem Y is NP-Complete if:
>1. $Y\in NP$
>2. For every problem $X \in NP$, it holds: $X\preceq_{p}Y.$

>[!definition]- THM 2.
>Suppose Y is an NP-complete problem.
>Then: Y is solvable in poly-time ( i.e. $Y\in P$ ) $\iff$ $P = NP$

**Proof**. $\leftarrow$ If $P = NP$ then Y **can be solved in poly-time** since $Y\in NP$.
**Proof**. $\to$ Suppose Y can be solved in poly-time
- Let X be any problem in NP. Since $X\preceq_p Y$, from THM 1, we can solve X in **poly-time**.
- This implies $NP\subseteq P$
- We already know. $P\subseteq NP$. Thus $P = NP\space\square$

**Fundamental question**. Do there exist "natural" NP-complete problems?

## A first NP-Complete Problem: Circuit Satisfiability

**CIRCUIT-SAT**. Given a combinational **circuit K** built out of **AND, OR**, and
**NOT** gates, is there a way to set the circuit inputs so that the output is 1?
Namely, is circuit $K(x_1,x_2,\dots,x_n ; t_1,t_2,\dots,t_m)$ satisfiable ?

![[appunti asd/mod ii/immagini/Pasted image 20230510092612.png|center|550]]


>[!definition]- THM.
>CIRCUIT-SAT is NP-complete. [Cook 1971, Levin 1973]

**Proof**. (sketch)
- Any **algorithm** that takes a fixed number of bits N as input and produces a yes/no answer can be represented by such a **circuit**. Moreover, if algorithm takes **poly-time**, then circuit is of **poly-size**.
	- _sketchy part of proof_; fixing the number n of bits is important, and reflects basic distinction between algorithms and circuits
- Consider some problem X in NP. By Hyp. It has a poly-time certifier C(s, t). To determine whether $s\in X$, need to know if there exists a certificate t of length $p(|s|)$ such that $C(s, t) = yes$.
- View C(s, t) as an <u>algorithm</u> on $|s| + p(|s|)$ bits (input s, certificate t) and convert it into a poly-size circuit $K(s_1,s_2,\dots,s_n ; t_1,t_2,\dots,t_m)$
	- first n=|s| bits are hard-coded with input s
	- remaining m= p(|s|) bits represent bits of the certificate t
- Circuit K is **satisfiable** iff C(s, t) = yes.

### Example of reduction to Circuit-SAT

Ex. Construction below creates a circuit K whose inputs can be set so that K outputs true iff graph G has an **independent set** of size 2.

![[appunti asd/mod ii/immagini/Pasted image 20230510093413.png|center|600]]


## Establishing NP-Completeness via poly-time reductions

**Remark**. Once we establish first "natural" NP-complete problem, others fall like dominoes.

**Recipe to establish NP-completeness of problem Y.**
- Step 1. Show that Y is in NP.
- Step 2. Choose an _old_ NP-complete problem X.
- Step 3. Prove that $X\preceq_p Y$.

>[!definition]- THM.
>If X is an NP-complete problem, and Y is a problem in NP with the property that $X\preceq_p Y$ then Y is NP-complete, as well

**Pf**. Let W be any problem in NP. Then $W\underbrace{\preceq_p}_{\text{by definition of NP-Complete}} X\underbrace{\preceq_p}_{\text{by assumption}} Y$.
- By _**transitivity**_, $W\preceq_{p}Y$
- Hence Y is **NP-Complete**

## 3-SAT is NP-Complete

>[!definition]- THM
>3-SAT is NP-complete.

**Pf**. Suffices to show that $CIRCUIT-SAT\preceq_p 3-SAT$ since 3-SAT is in NP.
- Let K be any circuit. 
- Create a 3-SAT variable $x_i$ for each **circuit element i**.
- Make circuit compute correct values at each node:
	- $x_2=\neg x_3\to$ ad 2 clauses: $x_{2}\lor x_3;\neg x_2\lor\neg x_3$ 
	- $x_1 = x_4 \lor x_5 \to$ add 3 clauses : $x_1 \lor\neg x_4 , x_1 \lor\neg x_5 ,\neg x_1 \lor x_4 \lor x_5$
	- $x_0 = x_1 \land x_2 \to$ add 3 clauses: $\neg x_0 \lor x_1 ,\neg x_0 \lor x_2 , x_0 \lor\neg x_1\lor\neg x_2$
- **Hard-coded** input values and output value.
	- $x_5 = 0 \to$ add 1 clause: $\neg x_5$
	- $x_0 = 1 \to$ add 1 clause: $x_0$
- **Final step**: turn clauses of length $\lt 3$ into clauses of length exactly 3.

![[appunti asd/mod ii/immagini/Pasted image 20230510094813.png|center|300]]

# Back to NP-Completeness

>[!warning]- Observation. 
>All problems below are NP-complete and polynomial reduce to one another!

![[appunti asd/mod ii/immagini/Pasted image 20230510094951.png|center|550]]


# Some NP-Complete Problems

Six basic genres of NP-complete problems and paradigmatic examples.
- Packing problems: SET-PACKING, INDEPENDENT SET.
- Covering problems: SET-COVER, VERTEX-COVER.
- Constraint satisfaction problems: SAT, 3-SAT.
- Sequencing problems: HAMILTONIAN-CYCLE, TSP.
- Partitioning problems: 3D-MATCHING 3-COLOR.
- Numerical problems: SUBSET-SUM, KNAPSACK.

**Practice**. Most NP problems are either known to be in P or NP-complete.
**Notable exceptions**. Factoring, graph isomorphism, Nash equilibrium.



