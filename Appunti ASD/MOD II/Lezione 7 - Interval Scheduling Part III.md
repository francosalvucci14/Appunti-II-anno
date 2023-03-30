
# Scheduling to Minimize Lateness

**Minimizing lateness problem**.
- **Single** resource processes **one** job at a time.
- Job j requires $t_j$ units of processing time and is due at time $d_j$. (**deadline**)
- Solution: If j starts at time $s_j$, it finishes at time $f_j = s_j +t_j$.
- Lateness: $l_j = max \{ 0,f_j - d_j \}$
- _**Goal**: schedule all jobs to minimize **maximum** lateness $L = max \{l_j\}$_

Note: input elements are in blue, solution elements are in red, cost
elements are in violet -> Vedi pdf

![[appunti asd/mod ii/immagini/Pasted image 20230330143531.png|center|550]]


## Greedy Algorithms

**Greedy template**. Consider jobs in some order.

- $[\text{Shortest processing time first}]$ Consider jobs in ascending order of processing time $t_j$.
- $[text{Earliest deadline first}]$ Consider jobs in ascending order of deadline $d_j$.
- $[\text{Smallest slack}]$ Consider jobs in ascending order of slack $d_j - t_j$.

**G1**: Shortest processing time first Consider jobs in ascending order of processing time $t_j$

![[appunti asd/mod ii/immagini/Pasted image 20230330145645.png|center|300]]

**G1** solution: Job 1; Job 2 --> Latency = 1
_Optimal Solution: Job 2; Job 1 --> Latency = 0_

**G2** Smallest slack : Consider jobs in **ascending** order of slack $d_j - t_j$.
G2 Solution: Job 2; Job 1. Latency = 10
_Optimal: Job 1; Job 2. Latency = 1_

![[appunti asd/mod ii/immagini/Pasted image 20230330145755.png|center|300]]

**G3**. Earliest deadline d first
Input: $\{ (t_1,d_1),\dots, (t_j,d_j),\dots(t_n,d_n) \}$

![[appunti asd/mod ii/immagini/Pasted image 20230330150421.png|center|500]]

![[appunti asd/mod ii/immagini/Pasted image 20230330150437.png|center|500]]

## No Idle Time

**Observation**. There exists an **optimal** schedule with no idle time.

![[appunti asd/mod ii/immagini/Pasted image 20230330152006.png|center]]

**Observation**. _The greedy schedule has no idle time_

>[!info]- 
>L'ottimo ha una struttura che ammette sempre assenza di tempi morti

## Inversion

>[!definition]- Inversion
>Given a schedule S, an inversion is a pair of jobs i and j such that:
>$$i < j (i.e. d_i <= d_j)\text{but j scheduled before i.}$$

![[appunti asd/mod ii/immagini/Pasted image 20230330152718.png|center|550]]

**Observation**. Greedy schedule has no inversions.

**Observation**. If a schedule (with no idle time) has an inversion, it has
one with a pair of inverted jobs scheduled **consecutively**.

$a \leq b \leq c \dots c' : c''\dots \leq f : f' :$
If $b \gt f'$ then for some consecutive c’, c’’ it must holds $c' \gt c''$

![[appunti asd/mod ii/immagini/Pasted image 20230330153149.png|center|550]]

>[!definition]- Lemma (Exchange Arg.)
>Swapping two consecutive, inverted jobs **reduces** the
>number of inversions by **one** and _does not increase the max lateness (the sum is
>commutative!)._

**Pf.**
- Let L be the lateness before the swap, and let L ' be it afterwards.
- $l'_k = l_k\forall k\neq i, j$
- $l'_i \leq l_i$
- If job j is late: -> ![[appunti asd/mod ii/immagini/Pasted image 20230330153625.png|center|300]]

## Analysis of Greedy Algorithm

**Theorem**. Greedy schedule S is optimal.
**Pf**. 
- Define $S^\star$ to be an optimal schedule that has the **fewest** number of **inversions**, and let's see what happens.
- Can assume $S^\star$ has no **idle time.**
- If $S^\star$ has no inversions, then $S = S^\star.$
- If $S^\star$ has an inversion, let i-j be an **adjacent** inversion.
	- swapping i and j <u>does not increase</u> the maximum lateness and strictly <u>decreases</u> the number of inversions
	- this contradicts definition of $S^\star$

# Greedy Analysis Strategies

**Greedy algorithm stays ahead**. Show that after each step of the greedy algorithm, its solution is at least as good as any other algorithm's.

**Structural**. Discover a simple "structural" bound asserting that every possible solution must have a certain value. Then show that your algorithm always achieves this bound.

**Exchange argument**. Gradually transform any solution to the one found by the greedy algorithm without hurting its quality.

**Soluzione esercizio** [[Lezione 6 - Interval Scheduling Part II]]

![[appunti asd/mod ii/immagini/Pasted image 20230330154331.png]]

**Esercizio 2 pg 185**

BUYING ITEMS OF INCREASING COSTS
DO AS HOMEWORK!
HINTS: DON’T LOOK AT THE BOOK, TRY GREEDY SOLUTIONS,
and PROVE :
• INVERSIONS in the good greedy ORDERING imply CONTRADICTIONS
• How prove CONTRADICTIONS? exchange argument

