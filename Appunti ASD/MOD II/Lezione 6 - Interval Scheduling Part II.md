# Interval Partitioning

Per delle informazioni leggermente più dettagliate vedi qui -> [Interval Scheduling-Partitioning](https://stumash.github.io/Algorithm_Notes/greedy/intervals/intervals.html)

**Interval partitioning**.
- Lecture j starts at $s_j$ and finishes at $f_j$.
- **Goal**: find _**minimum**_ number of _classrooms_ to schedule _**all**_ lectures
- so that no two occur at the same time in the same room.

Ex: This schedule uses 4 classrooms to schedule 10 lectures.

![[appunti asd/mod ii/immagini/Pasted image 20230329093504.png|center]]

Ex: This schedule uses only 3.

![[appunti asd/mod ii/immagini/Pasted image 20230329094927.png|center]]

## Lower Bound on Optimal Solution

>[!definition]- Depth
>The **depth** of a set of open intervals is the maximum number that contain
>any given time.

>[!definition]- TH (Lower Bound)
>$\forall$ istanza $I=\{(s_1,f_1),\dots,(s_n,f_n)\}$ del problema IP sia definita $depth(I)\equiv\max_t\{depth(t)\}$ allora
>$$OPT(I)\geq depth(I)$$

**Key observation**. Number of classrooms **needed** $\geq$ _depth_
**Ex**: depth of schedule below $=3\implies$ schedule below is **optimal**

a, b, c all contain 9:30 (depth of 9.30 = 3)

**Q**. Does there always exist a schedule equal to depth of intervals?

![[appunti asd/mod ii/immagini/Pasted image 20230329095349.png|center]]

>[!info]- Osservation
>$depth(I)=max\{depth_I(t)\},t\in\{s_1,f_n\}$
>Time = $\Theta(n)$
>In poche parole, la depth dell'istanza I è la massima depth tra tutti gli intervalli di tempo (che al massimo sono $2n$)

## Greedy Algorithm

**Greedy algorithm**. Consider lectures in increasing order of _**start time**_: assign lecture to _**any compatible**_ classroom.

![[appunti asd/mod ii/immagini/Pasted image 20230329100745.png|center]]


**Implementation**. 
- Time = $O(n\log n)$
- For each classroom k, maintain the finish time of the last job added.
- Keep the classrooms in a _priority queue._ (use Heap)

### Analysis

**Observation**. Greedy algorithm **never** schedules two incompatible lectures in the same classroom.

**Theorem.** Greedy algorithm is _**optimal.**_
Pf.
1. Let d = number of classrooms that the greedy algorithm allocates.
2. Classroom d is opened because we needed to schedule a job, say _j_, that is **incompatible** with all d-1 other classrooms (i.e. d-1 jobs)
3. These d jobs, **each must** end after $s_j$. (since they are incompatible with j)
4. Since we sorted by start time, all these incompatibilities are caused by jobs that _start no later than $s_j$._
5. Thus, we have d jobs overlapping at time $s_j+\varepsilon$.
6. Key observation (Lower Bound) $\implies$ all schedules use $\geq d$ classrooms.

![[appunti asd/mod ii/immagini/Pasted image 20230329102814.png|center|550]]

