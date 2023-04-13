
# Algorithmic Paradigms

**Greedy**. Build up a solution incrementally, myopically optimizing some local criterion.

**Divide-and-conquer**. Break up a problem into sub-problems, solve each sub-problem independently, and combine solution to sub-problems to form solution to original problem.

**Dynamic programming**. Break up a problem into a series of overlapping sub-problems, and build up solutions to larger and larger sub-problems.

# Dynamic Programming

## Dynamic Programming History

`Bellman. [1950s]`  Pioneered the systematic study of dynamic programming.

**Etymology.**
- Dynamic programming = planning over time.
- Secretary of Defense was hostile to mathematical research.
- Bellman sought an impressive name to avoid confrontation.

>[!quote]
>"it's impossible to use dynamic in a pejorative sense"
>"something not even a Congressman could object to"
>\-Bellman, R. E. Eye of the Hurricane, An Autobiography.

## Dynamic Programming Applications

**Areas**.
- Bioinformatics.
- Control theory.
- Information theory.
- Operations research.
- Computer science: theory, graphics, AI, compilers, systems, ….

**Some famous dynamic programming algorithms.**
- Unix diff for comparing two files.
- Viterbi for hidden Markov models.
- Smith-Waterman for genetic sequence alignment.
- Bellman-Ford for shortest path routing in networks.
- Cocke-Kasami-Younger for parsing context free grammars.

## Weighted Interval Scheduling

**Weighted Interval Scheduling problem**

- Job j starts at $s_j$, finishes at $f_j$, and has weight or value $v_j$ .
- Two jobs _**compatible**_ if they don't overlap.
- Goal: find maximum _**weight**_ subset of mutually compatible jobs.

![[appunti asd/mod ii/immagini/Pasted image 20230413144239.png|center|550]]


### Unweighted Interval Scheduling Review

**Recall**. Greedy algorithm works if all weights are 1.
- Consider jobs in ascending order of finish time.
- Add job to subset if it is compatible with previously chosen jobs.

>[!info]- Observation
>Greedy algorithm _**can fail**_ spectacularly if arbitrary weights are allowed.

![[appunti asd/mod ii/immagini/Pasted image 20230413144534.png|center|550]]


**Notation**. Order jobs by finishing time: $f_1 \leq f_2 \leq\dots\leq f_n$ . 

>[!definition]- Def. 
>$p(j)$ = **largest** index $i < j$ such that job i is compatible with j.

Ex: p(8) = 5, p(7) = 3, p(2) = 0.

![[appunti asd/mod ii/immagini/Pasted image 20230413144959.png|center|550]]

### Dynamic Programming: Binary Choice

**_Notation._** 
**OPT(j)** = value of optimal solution to the problem consisting of job requests 1, 2, ..., j. (Istanza formata dai primi j intervalli, IMPORTANTE)

- <u>Case 1</u>: OPT _selects_ job j.
	- collect profit $v_j$
	- can't use incompatible jobs $\{ p(j) + 1, p(j) + 2, \dots, j - 1 \}$
		- must **include optimal** solution to **sub-problem** consisting of remaining compatible jobs 1, 2, ..., p(j)
- <u>Case 2</u>: OPT does _not select_ job j.
	- must include optimal solution to **sub-problem** consisting of remaining compatible jobs 1, 2, ..., j-1

$$OPT(j)=\begin{cases}0&j=0\\max\{ v_j+OPT(p(j)),OPT(j-1)\}&otherwise\end{cases}$$

### Brute Force

**Brute-force algorithm.**

![[appunti asd/mod ii/immagini/Pasted image 20230413145847.png|center|550]]

**Optimal Cost** for the Input of size n is computed by function:
$$Compute-Opt(j\coloneqq n)$$

>[!info]- Observation. 
>**Recursive** algorithm **fails** spectacularly because of **redundant** sub-problems $\implies$ **exponential** algorithms.
  
Ex. Number of recursive calls for family of "layered" instances grows like Fibonacci sequence.

![[appunti asd/mod ii/immagini/Pasted image 20230413150329.png|center|550]]


But…..
Q. How many different subproblems we have?
A. **Only n**

Q. Can we fix an ordering to compute them? …..
A. Yes!

Define an Array $M[1,\dots,n]$, where
$M[j] \coloneqq OPT(j) \equiv$ Optimum for the sub-problem $\{1,\dots,j\}$

**Key-Fact**: To compute $M[j]$, we needs only the entries $M[0], M[1], \dots, M[j-2], M[j-1]$

We can apply induction!

### ITERATIVE dynamic programming algorithm

**Bottom-up dynamic programming**. remove recursion.

![[appunti asd/mod ii/immagini/Pasted image 20230413151337.png|center|550]]

<u>Crucial Issue</u>: Find the correct order for computing the subproblems!

### Finding a Solution

Q. Dynamic programming algorithms computes optimal _value_ “only”. What if we want the _solution_ itself?
A. Do some **_post-processing._**

![[appunti asd/mod ii/immagini/Pasted image 20230413151627.png|center|550]]

Number of recursive calls $\leq n\implies O(n)$.
Remark. $O(n)$ if jobs are pre-sorted by start and finish times.

### Memoization

>[!definition]- Memoization
> Use Recursion but start a new call **only if** the required value has not been computed yet.

Store results of each sub-problem in a cache; lookup as needed.

![[appunti asd/mod ii/immagini/Pasted image 20230413152449.png|center|550]]


### Running Time

![[appunti asd/mod ii/immagini/Pasted image 20230413152736.png|center|600]]


## Paradigm of Dynamic Programming (Informal Description)

Partition of the initial problem $P(n)$ into a set ofsubproblems $P_1(n_1), P_2(n_2),\dots, P_k(n_k)$ such that
- $n_i \lt n$ for all $i=1,\dots,k$
- $k = poly(n)$
- P(n) can be computed from $P_1(n_1), P_2(n_2),\dots, P_k(n_k)$ in poly-time
- There is a natural _ordering_ (from _smaller_ to _bigger_) of the subproblems so that **recursion** can be applied efficiently.

